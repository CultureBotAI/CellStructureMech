# PR 2351: current-input review of ten records and adversarial follow-up

- Review: 20261103T051803Z-pr2351-current-record-followup
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-11-03T05:05:44.598270Z
- Finished UTC: 2026-11-03T05:18:03Z
- Reviewer: Codex root synthesis with three independent read-only adversarial reviewers (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Current-input reassessment of all ten records in PR2351. Four stale records are substantively refreshed: MCR graph grounding propagation, the predicted/unreviewed phycobilisome-rod CpcD example, the respiratory complex I peripheral-arm contribution and complex II constituent edges. Five records retain five minor scientific curation findings; five receive qualified supported assessments. The historical MCR category-review finding is resolved on current main and remains linked to already-closed #2432, without claiming this PR repaired the record. The successor corrects structured-source coverage for eight original bundles. No scientific record is edited.

## Scope And Provenance

Exact ten-record PR cohort reassessed against current main f9abc3a0c7d0727083ab824899e576a8d7db2938. Changed inputs are substantively reassessed. Scientific records remain unchanged.

Selection: Complete cohort of ten maintained records reviewed in original PR head bdebfd046d61b5dd82d56001ee1753841ccf912f.
Coverage: full; 10 reviewed / 10 in the declared population.
Source: working_tree at Git base 3266d0f7239a80f17d74bb0d6e2b3e260000b8dc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0044674 | data/structures/energy_complex/methyl_coenzyme_m_reductase_complex.yaml | maintained | methyl coenzyme M reductase complex |
| GO:0009523 | data/structures/energy_complex/photosystem_ii.yaml | maintained | photosystem II |
| cellstructuremech:phycobilisome_rod | data/structures/energy_complex/phycobilisome_rod.yaml | maintained | phycobilisome rod |
| GO:0030096 | data/structures/energy_complex/plasma_membrane_derived_thylakoid_photosystem_ii.yaml | maintained | plasma membrane-derived thylakoid photosystem II |
| cellstructuremech:rc_lh1_pufx_core_complex | data/structures/energy_complex/rc_lh1_pufx_core_complex.yaml | maintained | RC-LH1-PufX core complex |
| GO:0045271 | data/structures/energy_complex/respiratory_chain_complex_i.yaml | maintained | respiratory chain complex I |
| GO:0045273 | data/structures/energy_complex/respiratory_chain_complex_ii_succinate_dehydrogenase.yaml | maintained | respiratory chain complex II (succinate dehydrogenase) |
| GO:0000220 | data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_v0_domain.yaml | maintained | vacuolar proton-transporting V-type ATPase, V0 domain |
| GO:0000221 | data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_v1_domain.yaml | maintained | vacuolar proton-transporting V-type ATPase, V1 domain |
| GO:0009279 | data/structures/envelope/cell_outer_membrane.yaml | maintained | cell outer membrane |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full native QC | passed | True | GO:0044674, GO:0009523, cellstructuremech:phycobilisome_rod, GO:0030096, cellstructuremech:rc_lh1_pufx_core_complex, GO:0045271, GO:0045273, GO:0000220, GO:0000221, GO:0009279 | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| Native label correspondence | passed | True | GO:0044674, GO:0009523, cellstructuremech:phycobilisome_rod, GO:0030096, cellstructuremech:rc_lh1_pufx_core_complex, GO:0045271, GO:0045273, GO:0000220, GO:0000221, GO:0009279 | 4232 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| TraitMech references | passed | True | GO:0044674, GO:0009523, cellstructuremech:phycobilisome_rod, GO:0030096, cellstructuremech:rc_lh1_pufx_core_complex, GO:0045271, GO:0045273, GO:0000220, GO:0000221, GO:0009279 | Native TraitMech link check passed. |
| Pinned governed files | passed | True | GO:0044674, GO:0009523, cellstructuremech:phycobilisome_rod, GO:0030096, cellstructuremech:rc_lh1_pufx_core_complex, GO:0045271, GO:0045273, GO:0000220, GO:0000221, GO:0009279 | Pinned governed files match; native vendored check passed. |
| Native identifier resolver | passed | True | GO:0044674, GO:0009523, cellstructuremech:phycobilisome_rod, GO:0030096, cellstructuremech:rc_lh1_pufx_core_complex, GO:0045271, GO:0045273, GO:0000220, GO:0000221, GO:0009279 | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| validate GO:0044674 | passed | True | GO:0044674 | Documented focused command passed. |
| validate-strict GO:0044674 | passed | True | GO:0044674 | Documented focused command passed. |
| validate GO:0009523 | passed | True | GO:0009523 | Documented focused command passed. |
| validate-strict GO:0009523 | passed | True | GO:0009523 | Documented focused command passed. |
| validate cellstructuremech:phycobilisome_rod | passed | True | cellstructuremech:phycobilisome_rod | Documented focused command passed. |
| validate-strict cellstructuremech:phycobilisome_rod | passed | True | cellstructuremech:phycobilisome_rod | Documented focused command passed. |
| validate GO:0030096 | passed | True | GO:0030096 | Documented focused command passed. |
| validate-strict GO:0030096 | passed | True | GO:0030096 | Documented focused command passed. |
| validate cellstructuremech:rc_lh1_pufx_core_complex | passed | True | cellstructuremech:rc_lh1_pufx_core_complex | Documented focused command passed. |
| validate-strict cellstructuremech:rc_lh1_pufx_core_complex | passed | True | cellstructuremech:rc_lh1_pufx_core_complex | Documented focused command passed. |
| validate GO:0045271 | passed | True | GO:0045271 | Documented focused command passed. |
| validate-strict GO:0045271 | passed | True | GO:0045271 | Documented focused command passed. |
| validate GO:0045273 | passed | True | GO:0045273 | Documented focused command passed. |
| validate-strict GO:0045273 | passed | True | GO:0045273 | Documented focused command passed. |
| validate GO:0000220 | passed | True | GO:0000220 | Documented focused command passed. |
| validate-strict GO:0000220 | passed | True | GO:0000220 | Documented focused command passed. |
| validate GO:0000221 | passed | True | GO:0000221 | Documented focused command passed. |
| validate-strict GO:0000221 | passed | True | GO:0000221 | Documented focused command passed. |
| validate GO:0009279 | passed | True | GO:0009279 | Documented focused command passed. |
| validate-strict GO:0009279 | passed | True | GO:0009279 | Documented focused command passed. |
| Supplemental bounded PMID authority checks | passed | True | GO:0044674, GO:0009523, cellstructuremech:phycobilisome_rod, GO:0030096, cellstructuremech:rc_lh1_pufx_core_complex, GO:0045271, GO:0045273, GO:0000220, GO:0000221, GO:0009279 | 909 PMIDs all OK in bounded native requests; full-command limitations remain separate. |
| Official structured-source applicability and covered-dataset cross-checks | passed | False | GO:0044674, GO:0009523, cellstructuremech:phycobilisome_rod, GO:0030096, cellstructuremech:rc_lh1_pufx_core_complex, GO:0045271, GO:0045273, GO:0000220, GO:0000221, GO:0009279 | Applicability was assessed for all ten records using the complete official catalogue and bounded source API fallback. Matched E. coli datasets provide gene and module context for complex II and outer membrane; covered Synechococcus elongatus provides bounded cyanobacterial photosynthesis context without being equated to the exact Thermostichus or Nostoc strains. No matching catalogue datasets exist for the named Methanothermobacter, Thermus, Cereibacter/Rhodobacter or yeast examples. V0/V1 are excluded from the molecular-coverage defect. Exact dataset, query, limits and threshold scope remain in the evidence. Expression observations do not establish structural membership, physical interaction, necessity or mechanism. Historical runner unavailability remains separate; no successful or fresh runner invocation is claimed. |
| Independent claim-level source review | passed | True | GO:0044674, GO:0009523, cellstructuremech:phycobilisome_rod, GO:0030096, cellstructuremech:rc_lh1_pufx_core_complex, GO:0045271, GO:0045273, GO:0000220, GO:0000221, GO:0009279 | Three read-only reviewers covered the complete ten-record cohort, including changed inputs, with explicit scientific findings and source-access limits. Final artifact/head acceptance occurs after saving. |
| Retained historical adapter runner availability | unavailable | False | GO:0044674, GO:0009523, cellstructuremech:phycobilisome_rod, GO:0030096, cellstructuremech:rc_lh1_pufx_core_complex, GO:0045271, GO:0045273, GO:0009279 | Historical 00:49Z invocation unavailable due to OS access restriction. Official catalogue source fallback was inspected separately; no current invocation or successful adapter execution is claimed. The actual historical exit code 1 is retained in the evidence receipt, since the native unavailable-check model has no execution exit-code field. |
| Native photosystem-ii UniProt verify check | passed | True | GO:0009523 | Read-only native command returned zero. Exact inventory coverage and claim-level limitations remain in its evidence; no record edits were applied. |
| Native photosystem-ii UniProt causal check | passed | True | GO:0009523 | Read-only native command returned zero. Exact inventory coverage and claim-level limitations remain in its evidence; no record edits were applied. |
| Native phycobilisome-rod UniProt verify check | passed | True | cellstructuremech:phycobilisome_rod | Read-only native command returned zero. Exact inventory coverage and claim-level limitations remain in its evidence; no record edits were applied. |
| Native phycobilisome-rod UniProt causal check | passed | True | cellstructuremech:phycobilisome_rod | Read-only native command returned zero. Exact inventory coverage and claim-level limitations remain in its evidence; no record edits were applied. |
| Native outer-membrane UniProt verify check | passed | True | GO:0009279 | Read-only native command returned zero. Exact inventory coverage and claim-level limitations remain in its evidence; no record edits were applied. |
| Native outer-membrane UniProt causal check | passed | True | GO:0009279 | Read-only native command returned zero. Exact inventory coverage and claim-level limitations remain in its evidence; no record edits were applied. |
| Native mcr UniProt verify check | passed | True | GO:0044674 | Read-only native command returned zero. Exact inventory coverage and claim-level limitations remain in its evidence; no record edits were applied. |
| Native mcr UniProt causal check | passed | True | GO:0044674 | Read-only native command returned zero. Exact inventory coverage and claim-level limitations remain in its evidence; no record edits were applied. |
| Native complex-i UniProt verify check | passed | True | GO:0045271 | Read-only native command returned zero. Exact inventory coverage and claim-level limitations remain in its evidence; no record edits were applied. |
| Native complex-i UniProt causal check | passed | True | GO:0045271 | Read-only native command returned zero. Exact inventory coverage and claim-level limitations remain in its evidence; no record edits were applied. |
| Native complex-ii UniProt verify check | passed | True | GO:0045273 | Read-only native command returned zero. Exact inventory coverage and claim-level limitations remain in its evidence; no record edits were applied. |
| Native complex-ii UniProt causal check | passed | True | GO:0045273 | Read-only native command returned zero. Exact inventory coverage and claim-level limitations remain in its evidence; no record edits were applied. |

## Scientific And Domain Assessments

### Hexamer identity and source-scoped reaction

identity: supported. Targets: GO:0044674.

GO0044674, native 1MRO assembly and primary transcription support the hexameric MCR target. Exact M.marburgensis mcrA/B/G examples and three InterPro families match the components and reaction context. Wrede2013 supports source-scoped localization of assembled MCR antigen, not universal membrane exclusion or isolated-subunit localization.

### Current graph propagation and historical F2 disposition

graph: supported. Targets: GO:0044674.

All three added graph grounding values now match their referenced components: alpha IPR016212, beta IPR003179 and gamma IPR003178. This substantively refreshes the stale review and resolves the exact category-review F2 observation. The repair pre-existed PR2351; the successor records the inspected disposition and preserves stable issue lineage.

### Whole complex and conserved-arm architecture

identity: supported. Targets: GO:0045271.

GO0045271 fits the L-shaped respiratory complex. Primary Results/Methods and supplemental Tables3-4 support the two maintained arm components; 14 named reviewed HB8 examples are verified. The source preparation additionally has Nqo15/Nqo16; the record does not claim only14 total chains in 4HEA. All16 deposited entity mappings were checked. Proposed coupling pathways remain qualified.

### Peripheral-arm contribution edge refresh

graph: supported. Targets: GO:0045271.

The added peripheral_arm→nadh_ubiquinone_activity contribution edge is supported by the source FMN/FeS electron-transfer architecture. A whole-complex GO activity name does not assert exclusive native ubiquinone usage in Thermus, where the paper identifies menaquinone8 and uses a decyl-ubiquinone analogue. The edge remains a coarse functional contribution, not a demonstrated kinetic coupling sequence.

### Whole-arm grounding specificity

evidence: supported. Targets: GO:0045271.

IPR001750 and IPR006137 are domains, not exact whole-arm identities. GO0042652/GO0042653 are obsolete. Bounded first-page GO searches and named candidate inspection support retaining reviewed label-only arms; they do not establish exhaustive absence of a future exact ontology term. The named core subunits are represented within the arm components, not omitted pending family identification.

### Four-chain complex and current graph refresh

identity: supported. Targets: GO:0045273.

GO0045273, primary abstract, deposited1NEK structure and reviewed SdhA-D entries support the maintained four-chain complex with catalytic SdhA, electron-transfer SdhB and SdhCD anchor module. Added contribution edges correctly identify SdhA flavin, the three SdhB FeS cluster classes and heme-bearing membrane module. These are whole-complex contributions; no isolated SdhCD activity or proton-pumping mechanism is asserted.

### Bounded family scope and localization provenance

evidence: supported. Targets: GO:0045273.

Integrated matches and named candidate definitions do not supply exact broad SdhA/SdhB/whole-SdhCD identities: several span fumarate reductases, are narrower clades, or denote only one anchor subunit. Additional current SdhB matchIPR050573 explicitly spans SDH/FRD by integrated family name; its unchecked LLM prose is excluded. UniProt attributes SdhA/B membrane localization to Stenberg2005 and SdhD to Daley2005; this verifies attribution without claiming a renewed full-body audit of those studies.

### Fresh catalogue-based source adapter applicability

evidence: supported. Targets: GO:0044674.

Fresh complete public catalogue has no matching Methanothermobacter marburgensis dataset. Not-applicable downstream module checks follow this actual organism-coverage result, not the absence of an expression claim. No close-relative dataset is silently substituted.

### Fresh catalogue-based source adapter applicability

evidence: supported. Targets: GO:0045271.

Fresh complete public catalogue has no matching Thermus thermophilus dataset. Not-applicable downstream module checks follow this actual organism-coverage result, not the absence of an expression claim. No close-relative dataset is silently substituted.

### Matched MG1655 gene and module context

evidence: supported. Targets: GO:0045273.

Fresh source fallback resolves sdhA/b0723,sdhB/b0724,sdhC/b0721,sdhD/b0722 in precise_mg1655. All four are thresholded members of Crp(k1) and ArcA-2(k10); sdhA/C/D also belong to ArcA-1(k14), while sdhB is below that threshold. Module annotations and all returned member identifier/weight rows were read. These bounded expression observations do not prove assembly, stoichiometry, essentiality or direct regulation; AI module prose and activity matrices are excluded.

### Assembly necessity remains unknown

evidence: unknown. Targets: GO:0044674.

Retain the original explicit uncertainty: structural membership and catalytic role alone do not establish whether the complete structure forms after deletion of a component. No target-specific deletion/assembly experiment was independently checked, and no new contrary result is confirmed in the inspected source scope.

### Assembly necessity remains unknown

evidence: unknown. Targets: GO:0045271.

Retain the original explicit uncertainty: structural membership and catalytic role alone do not establish whether the complete structure forms after deletion of a component. No target-specific deletion/assembly experiment was independently checked, and no new contrary result is confirmed in the inspected source scope.

### Assembly necessity remains unknown

evidence: unknown. Targets: GO:0045273.

Retain the original explicit uncertainty: structural membership and catalytic role alone do not establish whether the complete structure forms after deletion of a component. No target-specific deletion/assembly experiment was independently checked, and no new contrary result is confirmed in the inspected source scope.

### Current native protein and causal-node coverage checks

evidence: supported. Targets: GO:0044674.

Both root-executed native read-only commands exited0 at the reviewed source head; this independent reviewer read their logs and verified the bound stdout hashes. All declared gene symbols have matching examples. These checks supplement the source-level identity assessment and do not establish biochemical causality or essentiality.

### Current native protein and causal-node coverage checks

evidence: supported. Targets: GO:0045271.

Both root-executed native read-only commands exited0 at the reviewed source head; this independent reviewer read their logs and verified the bound stdout hashes. All declared gene symbols have matching examples. These checks supplement the source-level identity assessment and do not establish biochemical causality or essentiality.

### Current native protein and causal-node coverage checks

evidence: supported. Targets: GO:0045273.

Both root-executed native read-only commands exited0 at the reviewed source head; this independent reviewer read their logs and verified the bound stdout hashes. All declared gene symbols have matching examples. These checks supplement the source-level identity assessment and do not establish biochemical causality or essentiality.

### Exact PSII structure and named taxa

identity: supported. Targets: GO:0009523.

The generic photosystem parent, exact GO identity, grouped core and oxygenic canonical example remain coherent. Broader anoxygenic comparison is inherited GO definition text, not a new cyanobacterial species claim. No protein/phenotype identity collapse.

### Mixed core, metal cluster and pigments

grounding: supported. Targets: GO:0009523.

Umena supports represented core/cofactor classes. Exact D1 or D2 families and broad L/M cannot individually ground the complete mixed reaction-center core; no exhaustive family absence claim. Known central membership is represented rather than postponed wholesale.

### Assembly necessity remains an explicit limitation

scope: unknown. Targets: GO:0009523.

Canonical presence/catalytic importance is supported; the inspected structures and halide activity experiment do not independently establish assembly loss on removal of each grouped metal/pigment class. ESSENTIAL is not upgraded to a demonstrated knockout, universal member requirement or organism-viability result. No contradictory assembly experiment was established in this bounded review.

### Exact D1/D2 examples and expanded primary access

evidence: supported. Targets: GO:0009523.

Reviewed P51765 psbA and D0VWR8 psbD match native taxon, status and location-annotation citations; two-result query supports uniqueness per symbol in scope. Current Kamiya2003 and Kawakami2009 body access succeeds and supersedes the old access limitation only for this observation. Kamiya model-sequence borrowing is disclosed; annotation does not by itself prove all assembly details.

### Five broad functional edges

graph: supported. Targets: GO:0009523.

The NONMECHANISTIC graph preserves light excitation, water-derived electron supply, quinone reduction and initiation of the photosynthetic chain. It does not assert atomistic S-state routes, ATP production by PSII or exact universal subunit stoichiometry. Native graph audit1/1COVERED.

### Substantive refresh of added CpcD example

provenance: supported. Targets: cellstructuremech:phycobilisome_rod.

Current record differs from frozen input by the added A0ABT0CFU3/JX360_17400 example and associated curation event. Fresh UniProt and source GenPept explicitly annotate a predicted CpcD linker in Rupite, supporting this identity-only example. It is not a unique paralog claim, experimental localization or a resolution of the independent cpcC issue. Current graph audit is2/2COVERED, superseding the historical optional cpcD gap.

### Peripheral rod versus core and entire antenna

identity: supported. Targets: cellstructuremech:phycobilisome_rod.

The local rod is a source-supported peripheral subassembly; GO0030076 is the broader parent and whole-PBS GO0030089 is parthood. The local allophycocyanin-core graph reference resolves to a distinct central structure. No intact atomic whole-PBS claim is made.

### Mixed rod constituents and family scope

grounding: supported. Targets: cellstructuremech:phycobilisome_rod.

CpcA/B-rich phycobiliproteins, mixed rod/rod-terminal/rod-core linkers and covalent bilins match the primary preparation. Broad phycobiliprotein family includes core members; linker domains span multiple classes, so they are not exact whole-cohort replacements. CpcG2 assignment is tentative in the paper’s heterogeneous rods.

### cpcC finding persists despite native checks

provenance: concern. Targets: cellstructuremech:phycobilisome_rod.

The valid A0ABT0C7D6 accession/ORF/taxon passes native verification, but JX360_02095 is only a generic predicted rod-core linker in UniProt and GenPept. NIES-2134 primary text and BP-1 model-sequence context do not establish the exact Rupite cpcC mapping. Freshly reassessed original F1 remains open; no replacement accession is inferred from domain or length comparisons.

### Primary strain and comparative taxa

scope: supported. Targets: cellstructuremech:phycobilisome_rod.

Direct cryo-EM experiment is NIES-2134 T. vulcanus; Rupite examples are predicted identity annotations. Red-algal architecture is comparative context in the primary Introduction. Native taxon labels are valid; no cross-strain localization, abundance measurement or universal stoichiometry is inferred.

### Five bounded assembly/light-harvesting edges

graph: supported. Targets: cellstructuremech:phycobilisome_rod.

Disk assembly, linker organization, covalent pigments and inward excitation transfer are supported at the stated broad NONMECHANISTIC tier. Detailed energy-level tuning/pathways in the paper remain structural interpretations with prior spectroscopy, not measured time-resolved transfer by that experiment. No new required optional class or exhaustive family mapping is invented.

### Exact bacterial-thylakoid subtype and partonomy

identity: supported. Targets: GO:0030096.

GO0030096 exactly identifies the membrane-derived bacterial-thylakoid PSII subtype with generic PSII parent and thylakoid-membrane parthood. Its scoped synonym and structure category avoid collapsing whole PBS, protein or generic PSII identity. Ontology terminology does not establish a new direct membrane-biogenesis experiment.

### Canonical prepared-particle association

evidence: supported. Targets: GO:0030096.

Chang2015 supports some Nostoc/Anabaena PCC7120 PBS particles associated with PSII, using low-resolution density, D1/D2 immunoblot and D1 immunogold. It does not show all PBS particles bind PSII, a live-cell atomic interface or a catalytically intact oxygen-evolving preparation.21Å PBS-only and34ÅPBS–PSII maps remain distinct.

### Known D1/D2 membership is postponed unnecessarily

completeness: concern. Targets: GO:0030096.

Current record still has no components and explicitly defers all subunit rows until exact source-neutral families are resolved. The cited Results/Fig1G directly identify D1/D2 reaction-center subunits; known membership can be recorded with unresolved family groundings. Original F1 remains open. This does not demand every optional accessory subunit or interpret PsbO nondetection as universal absence.

### Four broad graph edges and access tiers

graph: supported. Targets: GO:0030096.

Exact GO supplies water-to-plastoquinone physiology and membrane identity; primary Chang supplies limited PBS association. This observation independently supports the broad graph with those sources. Perez2024 is secondary context: its fresh abstract/metadata were readable, but native403 and browser fulltext failure prevent claiming a newly inspected body. The old body-excerpt provenance is left historical.

### Named strain and qualitative cyanobacterial distribution

scope: supported. Targets: GO:0030096.

Native nomenclature agrees with Anabaena/NostocPCC7120 equivalence. COMMON is qualitative within cyanobacteria having internal thylakoids, not prevalence data or an assertion of identical architecture in all cyanobacteria. No new strain-specific accession inventory, images or measured properties are asserted.

### Covered cyanobacterial expression context with strict limits

evidence: supported. Targets: GO:0009523.

All3 original bundles omit the structured-source applicability step despite named genes/proteins or photosynthetic pathways. Current catalogue and s_elongatus/elprecise300 PCC7942 metadata establish bounded cyanobacterial coverage; exact psbA/D and cpcA/B/C/D/G table matches, all57module memberships for13loci, and selected modules1/6/38 were inspected. Photosystems38 and RpaB6 include different subsets; PSII1 excludes the selected psbA/D loci despite its name. Regulator fields are null. This computational expression context neither changes the scientific verdict nor establishes canonical-strain orthology, physical localization or direct regulation. Native runner availability is to be disclosed from the root’s actual retained receipt; this reviewer used inspected official API fallback, not a new runner execution.

### Frozen inputs and historical native review pair

schema: supported. Targets: GO:0009523.

Historical source bytes match the original frozen input; native validation and rendered Markdown pass. Current target bytes remain identical to the original input. Current broad QC/labels/history/strict receipts are owned by the root synthesis, not claimed executed by this reviewer.

### Covered cyanobacterial expression context with strict limits

evidence: supported. Targets: cellstructuremech:phycobilisome_rod.

All3 original bundles omit the structured-source applicability step despite named genes/proteins or photosynthetic pathways. Current catalogue and s_elongatus/elprecise300 PCC7942 metadata establish bounded cyanobacterial coverage; exact psbA/D and cpcA/B/C/D/G table matches, all57module memberships for13loci, and selected modules1/6/38 were inspected. Photosystems38 and RpaB6 include different subsets; PSII1 excludes the selected psbA/D loci despite its name. Regulator fields are null. This computational expression context neither changes the scientific verdict nor establishes canonical-strain orthology, physical localization or direct regulation. Native runner availability is to be disclosed from the root’s actual retained receipt; this reviewer used inspected official API fallback, not a new runner execution.

### Frozen inputs and historical native review pair

schema: supported. Targets: cellstructuremech:phycobilisome_rod.

Historical source bytes match the original frozen input; native validation and rendered Markdown pass. Current input is substantively refreshed above, without altering old bundle bytes. Current broad QC/labels/history/strict receipts are owned by the root synthesis, not claimed executed by this reviewer.

### Covered cyanobacterial expression context with strict limits

evidence: supported. Targets: GO:0030096.

All3 original bundles omit the structured-source applicability step despite named genes/proteins or photosynthetic pathways. Current catalogue and s_elongatus/elprecise300 PCC7942 metadata establish bounded cyanobacterial coverage; exact psbA/D and cpcA/B/C/D/G table matches, all57module memberships for13loci, and selected modules1/6/38 were inspected. Photosystems38 and RpaB6 include different subsets; PSII1 excludes the selected psbA/D loci despite its name. Regulator fields are null. This computational expression context neither changes the scientific verdict nor establishes canonical-strain orthology, physical localization or direct regulation. Native runner availability is to be disclosed from the root’s actual retained receipt; this reviewer used inspected official API fallback, not a new runner execution.

### Frozen inputs and historical native review pair

schema: supported. Targets: GO:0030096.

Historical source bytes match the original frozen input; native validation and rendered Markdown pass. Current target bytes remain identical to the original input. Current broad QC/labels/history/strict receipts are owned by the root synthesis, not claimed executed by this reviewer.

### RC-LH1-PufX identity, topology and neighbor

identity: supported. Targets: cellstructuremech:rc_lh1_pufx_core_complex.

Local complex identity is narrower than its chromatophore membrane context GO0042717. Tax1063 is current Cereibacter sphaeroides with Rhodobacter synonym. Frozen LH2 record resolves the distinct external antenna link, and GO0009767 is the photosynthetic electron-transport process, not structure identity.

### RC architecture and bounded functional links

evidence: supported. Targets: cellstructuremech:rc_lh1_pufx_core_complex.

Bahatyrova AFM supports native membrane-patch core/LH2 organization; Comayras optical assays support isolated-core/chromatophore excitation and quinone context. The four NON_MECHANISTIC edges stay at membrane placement, LH2 energy input, quinone reduction and contribution to the photosynthetic chain. They do not assert a detailed cofactor path, PufX-specific kinetics or universal interdimer transfer.

### RC known core remains unnecessarily deferred

grounding: concern. Targets: cellstructuremech:rc_lh1_pufx_core_complex.

Original F1 remains confirmed: no component rows are present, while the TODO makes exact family mapping a prerequisite. Source-bounded RC L/M/H, LH1 alpha/beta and PufX-containing-complex membership can be recorded without guessed CURIEs; the AFM paper explicitly did not resolve PufX itself.

### RC structured-source applicability

scope: supported. Targets: cellstructuremech:rc_lh1_pufx_core_complex.

Named PufX/photosynthetic pathway requires applicability assessment. The fresh official catalogue contains no Cereibacter/Rhodobacter match, so matched downstream queries are not applicable for this exact strain context. This is not absence of a gene, and unrelated phototrophic organisms were not substituted.

### V0 identity and intact-enzyme scope

identity: supported. Targets: GO:0000220.

The specific vacuolar sector is correctly distinguished from its broader sector parent and complete GO0016471 V-ATPase. Yeast4932 is a bounded example. V0 membrane transport is expressly inside the intact enzyme, not a freely leaking detached pore.

### V0 established subunits remain deferred

grounding: concern. Targets: GO:0000220.

Original F1 remains confirmed. Kane secondary synthesis explicitly lists yeast V0 a, c, c-prime, c-double-prime, d and e. Evidence-backed label-only component rows are permitted now; unresolved exact families/copy numbers do not justify omitting the known inventory. Membership does not automatically imply assembly necessity.

### V0 source tier, isoform and adapter boundary

scope: supported. Targets: GO:0000220.

Kane is review-tier evidence, with vacuolar Vph1 versus Golgi/endosomal Stv1 and dissociation limits retained. Current record names sectors rather than genes/loci/accessions or a regulator/transcriptomic claim; do not manufacture a named-gene adapter omission for this sparse scope. Catalogue also has no Saccharomyces coverage.

### V1 identity and intact-enzyme scope

identity: supported. Targets: GO:0000221.

The specific vacuolar sector is correctly distinguished from its broader sector parent and complete GO0016471 V-ATPase. Yeast4932 is a bounded example. V1 hydrolysis/rotation couples to V0 in the intact enzyme; ungrounded ATP-hydrolysis node avoids treating whole proton transport as an isolated V1 activity.

### V1 established subunits remain deferred

grounding: concern. Targets: GO:0000221.

Original F1 remains confirmed. Kane secondary synthesis explicitly lists yeast V1 A, B, C, D, E, F, G and H. Evidence-backed label-only component rows are permitted now; unresolved exact families/copy numbers do not justify omitting the known inventory. Membership does not automatically imply assembly necessity.

### V1 source tier, isoform and adapter boundary

scope: supported. Targets: GO:0000221.

Kane is review-tier evidence, with vacuolar Vph1 versus Golgi/endosomal Stv1 and dissociation limits retained. Current record names sectors rather than genes/loci/accessions or a regulator/transcriptomic claim; do not manufacture a named-gene adapter omission for this sparse scope. Catalogue also has no Saccharomyces coverage. Forgac is fresh abstract/metadata only; historical Key Points access is not a fresh complete body read.

### Outer membrane broad identity and conditional composition

identity: supported. Targets: GO:0009279.

GO0009279/GO0016020 and tax2/562/83333 match their authorities. Definition distinguishes the broad diderm outer membrane from canonical Gram-negative asymmetry. LPS is CONDITIONAL, consistent with exceptional LPS-free envelopes. A generic beta-barrel cohort spans OmpA/porin/BamA families and does not warrant one guessed family ID.

### Outer membrane examples and exact source attribution

evidence: supported. Targets: GO:0009279.

All eight named products are reviewed K12 accessions matching their genes. For four protein examples, native UniProt directly assigns the record-listed location PMIDs to SL0040. Exact primary abstracts distinguish refolded OmpA channels, elastase exposure, envelope-complex proteomics, porin heterotrimers and BamA structure/CDI. Individual full primary tables/methods were not audited.

### Canonical Lpt/BAM assembly and permeability mechanisms

graph: supported. Targets: GO:0009279.

Secondary source bodies support Lpt-mediated LPS delivery, BAM beta-barrel assembly, ordered LPS barrier and selective porin paths in canonical Gram-negative envelopes. LptD-only and BAM A/B/C/D xrefs are representative links, not inventories. Schema permits protein complexes as GENE_OR_PROTEIN. Excludes is explicitly reduced influx; no absolute permeability or detailed atomic sequence is asserted.

### Collective beta-barrel assembly necessity remains unresolved

scope: unknown. Targets: GO:0009279.

The generic beta-barrel component is marked ESSENTIAL, but inspected review-tier mechanism and localization sources do not independently test whether the whole structure forms without that collective cohort. Retain the original unknown limitation; membership, permeability, activity and cell viability are not interchangeable with assembly necessity. No new contradictory deletion result or universal essentiality claim was established.

### Matched E. coli expression context

scope: supported. Targets: GO:0009279.

Fresh precise1k searches resolve ompA b0957, ompC b2215, ompF b0929, bamA b0177, bamB b2512, bamC b2477, bamD b2595 and lptD b0054. In each returned 201-module array, only ompF has thresholded memberships: k86 UC-3, k88 Nitrogen/Nac, k25 Lrp and k22 SoxS. Read structured module metadata; excluded AI prose and nonexact substring hits. These are expression associations, not physical or necessity proof.

### Complete frozen-input comparison and bounded refresh

provenance: supported. Targets: GO:0044674, GO:0009523, cellstructuremech:phycobilisome_rod, GO:0030096, cellstructuremech:rc_lh1_pufx_core_complex, GO:0045271, GO:0045273, GO:0000220, GO:0000221, GO:0009279.

4 of ten original target hashes differ from current main. The changed content is substantively reassessed in the target-specific assessments; original observations remain historical and unchanged. All current target and used context bytes are frozen.

## Findings

### plaque-MCR-resolved-F2: MCR graph nodes now retain verified component groundings

minor / resolved / confirmed; issue key: energy-complex-mcr-causal-node-component-ref-grounding.

The three historical omissions are absent from the current record: nodes[1..3] now carry InterPro:IPR016212,InterPro:IPR003179,InterPro:IPR003178 matching their referenced components. Fresh native family definitions and exact protein examples support those identities.

Disposition: Current inspected record resolves all three exact omissions from category-review F2. The record repair was already present on main and associated issue2432 was already closed; PR2351 adds a current review disposition, not a record fix.

### micro-F1: The cpcC-to-Rupite-locus mapping lacks exact source support

minor / open / confirmed; issue key: phycobilisome-rod-cpcc-locus-mapping-unverified.

The A0ABT0C7D6 example asserts that cpcC maps to JX360_02095. Its native UniProt and source GenPept instead provide only that ORF and a generic predicted rod-core linker annotation. The cited NIES-2134 structural paper does not map this Rupite locus. Verify exact orthology with an inspectable source, or remove/rephrase the unsupported cpcC identity assertion; retain the verified accession/taxon and distinguish generic linker membership from gene identity. A different Rupite candidate is not established as a replacement.

### micro-F2: Separate known reaction-center membership from family-grounding uncertainty

minor / open / confirmed; issue key: bacterial-psii-known-core-deferred-for-family-grounding.

The psii_subunit_boundaries prompt defers adding all subunit-level components until exact family groundings are resolved. Yet the cited Chang2015 Results and Figure1G identify D1 and D2 as reaction-center subunits in the associated PBS preparation. These known core constituents can be represented with source-backed labels and unresolved groundings. The consequential gap is the blanket deferral of established membership, not the lack of every optional PSII detail.

### septin-S2351-F1: Separate the established core constituents from family-mapping work

minor / open / confirmed; issue key: rc-lh1-pufx-known-core-deferred-for-family-grounding.

The record has no component rows, and its rc_lh1_pufx_subunit_boundaries prompt makes exact family resolution a prerequisite for representing the named reaction-center/LH1/PufX constituents. The cited native-array paper already supplies the core architecture and reaction-center L/M/H context, while the functional study characterizes isolated RC-LH1 complexes. Supported labels can preserve known membership without guessed family identifiers or unsupported PufX density assignments.

### septin-S2351-F2: Represent known V0 subunits without waiting for exact family CURIEs

minor / open / confirmed; issue key: v0-known-subunits-deferred-for-family-grounding.

The open v0_subunit_grounding_todo rationale makes family grounding a prerequisite to all subunit-level components. Yet the cited Kane2006 review explicitly identifies yeast V0 subunits a, c, c-prime, c-double-prime, d and e. Evidence-backed label-only component rows are allowed and can retain unresolved family identifiers and copy numbers. Revise the blanket deferral and represent at least the established core membership, preserving source/taxon boundaries. This finding concerns a concrete known inventory and the stated blocking rationale, not a general requirement to populate every optional field.

### septin-S2351-F3: Represent known V1 subunits without waiting for exact family CURIEs

minor / open / confirmed; issue key: v1-known-subunits-deferred-for-family-grounding.

The open v1_subunit_grounding_todo rationale makes family grounding a prerequisite to all subunit-level components. Yet the cited Kane2006 review explicitly identifies yeast V1 subunits A, B, C, D, E, F, G and H. Evidence-backed label-only component rows are allowed and can retain unresolved family identifiers and copy numbers. Revise the blanket deferral and represent at least the established core membership, preserving source/taxon boundaries. This finding concerns a concrete known inventory and the stated blocking rationale, not a general requirement to populate every optional field.

## Recommended Actions And Acceptance Checks

### micro-A1

In authorized curation, verify the exact cpcC-to-JX360_02095 mapping with an explicit native gene/orthology source or retract that role/evidence mapping. Do not select another accession from length or generic linker annotation alone.

- Inspect exact accession, gene/ORF mapping and strain provenance in the supporting source.
- Keep NIES-2134 experimental evidence separate from Rupite identity-only examples and BP-1 model sequence references.
- Run native protein verify and graph audit in addition to schema/strict/history checks; verify role-level mapping manually.

### micro-A2

Add source-backed D1/D2 core constituent rows without guessed identifiers, and distinguish exact family resolution from known membership in discussion progress. Keep PBS proteins, transient assembly/repair factors and accessory-subunit variation separate.

- Use the cited Results/immunoblot evidence for D1/D2 membership; do not assert that all photosystem subunits were detected in this preparation.
- Do not interpret missing PsbO detection as native universal absence or claim a measured oxygen-evolution rate.
- Use the guarded record writer, append curation/repository history, regenerate pages, and pass native schema/strict/products/history/qc gates in separately authorized curation.

### septin-S2351-AC1

Represent source-supported core constituents with evidence and explicit unresolved groundings where needed. Distinguish directly resolved reaction-center features, established LH1 membership and the paper’s PufX-containing complex interpretation; retain exact family and stoichiometry work in the discussion.

- Do not claim Bahatyrova2004 directly located the PufX polypeptide; the paper explicitly could not identify it.
- Keep external LH2, cytochrome bc1 and mobile quinone pools distinct from constitutive protein members; avoid universal small-subunit stoichiometry.
- Use the guarded record writer, append curation/repository history, regenerate pages, and pass native schema/strict/products/history/qc gates in separately authorized curation.

### septin-S2351-AC2

During authorized curation, add source-backed label-only V0 subunit components and narrow the TODO to unresolved family mappings/copy numbers.

- Use the cited review at its actual review evidence tier; retain yeast and vacuolar-isoform boundaries.
- Distinguish final constituents from dedicated assembly factors; do not assign ESSENTIAL from membership or catalytic activity.
- Leave unverified family CURIEs and numerical stoichiometry unresolved rather than borrowing broad domains or newer unsupported counts.
- Run the required focused schema, strict-reference and review validations.

### septin-S2351-AC3

During authorized curation, add source-backed label-only V1 subunit components and narrow the TODO to unresolved family mappings/copy numbers.

- Use the cited review at its actual review evidence tier; retain yeast and vacuolar-isoform boundaries.
- Distinguish final constituents from dedicated assembly factors; do not assign ESSENTIAL from membership or catalytic activity.
- Leave unverified family CURIEs and numerical stoichiometry unresolved rather than borrowing broad domains or newer unsupported counts.
- Run the required focused schema, strict-reference and review validations.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| current-record-0 | data/structures/energy_complex/methyl_coenzyme_m_reductase_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 ef43ab9df3e0a3d8ed86e0347c9801db59ced9efd1d0313f8ab2a9b3b1420338; current SHA256 369ad320d4bc19c72a79fb14037b46c5e12f6eddaa64bd0bb04572e9a8ea685e. Changed record reassessed against current sources. |
| original-review-0 | reviews/structured/20261021T091345Z-methyl-coenzyme-m-reductase-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-1 | data/structures/energy_complex/photosystem_ii.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 fc05496451f76ed16643edb2ca590803fd07569abfe432111e31314375687a16; current SHA256 fc05496451f76ed16643edb2ca590803fd07569abfe432111e31314375687a16. Record bytes unchanged since the original review. |
| original-review-1 | reviews/structured/20261021T091346Z-photosystem-ii-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-2 | data/structures/energy_complex/phycobilisome_rod.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 612013ed996da72581fa218e57c90acce39e6d069c3bbd2b75958cac0b273616; current SHA256 f610a707b8f8fea3edfd28574b996a315eaf1e2d245de7efce9edf96b49943d1. Changed record reassessed against current sources. |
| original-review-2 | reviews/structured/20261021T091347Z-phycobilisome-rod-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-3 | data/structures/energy_complex/plasma_membrane_derived_thylakoid_photosystem_ii.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 7629a2480ce3d823e87431d0c26be93c45101095021fd60087301f5f1d9a58ef; current SHA256 7629a2480ce3d823e87431d0c26be93c45101095021fd60087301f5f1d9a58ef. Record bytes unchanged since the original review. |
| original-review-3 | reviews/structured/20261021T091348Z-plasma-membrane-derived-thylakoid-photosystem-ii-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-4 | data/structures/energy_complex/rc_lh1_pufx_core_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 0a3a6fcfe54b7a355fd2903992f521fb2fc293ce984d4ede356dbc8460071824; current SHA256 0a3a6fcfe54b7a355fd2903992f521fb2fc293ce984d4ede356dbc8460071824. Record bytes unchanged since the original review. |
| original-review-4 | reviews/structured/20261021T091349Z-rc-lh1-pufx-core-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-5 | data/structures/energy_complex/respiratory_chain_complex_i.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 412f85b2aeb446f9635a89f69cef1dc90c124dbade5bc41f1c5b568461a31e4a; current SHA256 0d0f4b5c3346e25dbbd3595d959c03d40dc9943e3e6055dcca3746fd4bf67540. Changed record reassessed against current sources. |
| original-review-5 | reviews/structured/20261021T091350Z-respiratory-chain-complex-i-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-6 | data/structures/energy_complex/respiratory_chain_complex_ii_succinate_dehydrogenase.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 9660cbd309d7c81353bf0b1fe1a3cd5a883f6ec574e3a0d9e990166dd861de0f; current SHA256 4e6914fa2c29221809c1a172d98aa541c5adc01bc5090cc8c0eb55b56a3d463d. Changed record reassessed against current sources. |
| original-review-6 | reviews/structured/20261021T091351Z-respiratory-chain-complex-ii-succinate-dehydrogenase-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-7 | data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_v0_domain.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 b76891f7e50630db7612669a25299babae68eb2e480724de8209094cc1953c48; current SHA256 b76891f7e50630db7612669a25299babae68eb2e480724de8209094cc1953c48. Record bytes unchanged since the original review. |
| original-review-7 | reviews/structured/20261021T091352Z-vacuolar-proton-transporting-v-type-atpase-v0-domain-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-8 | data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_v1_domain.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 fabfca0b7f5ff5ee1340a6874918e4505c242d7939734a2e9ef8f3df5ebeeb22; current SHA256 fabfca0b7f5ff5ee1340a6874918e4505c242d7939734a2e9ef8f3df5ebeeb22. Record bytes unchanged since the original review. |
| original-review-8 | reviews/structured/20261021T091354Z-vacuolar-proton-transporting-v-type-atpase-v1-domain-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-9 | data/structures/envelope/cell_outer_membrane.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 6a21a7409a3e93aa290cbff61f4734629b927f04a33c469e6166ef1b24673fab; current SHA256 6a21a7409a3e93aa290cbff61f4734629b927f04a33c469e6166ef1b24673fab. Record bytes unchanged since the original review. |
| original-review-9 | reviews/structured/20261021T091355Z-cell-outer-membrane-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| plaque-mcr-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0044674,GO:1990234,GO:0050524; results[].id/name/aspect/definition/isObsolete | supports | Current authority terms inspected: [('GO:1990234', 'transferase complex', False), ('GO:0044674', 'methyl coenzyme M reductase complex', False), ('GO:0050524', 'coenzyme-B sulfoethylthiotransferase activity', False)]. Obsolete arm terms do not supply current exact component identities. |
| plaque-mcr-agent-tax-79929 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/79929; taxId, scientificName and lineage | supports | Native taxonomy checks the exact organism/strain identifier; species-level deposited source and strain-specific examples remain distinct. |
| plaque-mcr-agent-IPR016212 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016212/; metadata.accession/type/name, integrated member signatures and description | supports | Inspected family IPR016212, Methyl coenzyme M reductase, alpha subunit, against exact whole-component scope. |
| plaque-mcr-agent-IPR003179 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR003179/; metadata.accession/type/name, integrated member signatures and description | supports | Inspected family IPR003179, Methyl-coenzyme M reductase, beta subunit, against exact whole-component scope. |
| plaque-mcr-agent-pdb-1mro | https://data.rcsb.org/rest/v1/core/entry/1MRO; struct.title, primary citation, resolution and polymer identities | supports | Deposited structure METHYL-COENZYME M REDUCTASE; native primary citation and structure identifiers checked, without raw-coordinate reanalysis. |
| plaque-mcr-agent-pdb-1mro-assembly1 | https://data.rcsb.org/rest/v1/core/assembly/1MRO/1; pdbx_struct_assembly and rcsb_assembly_info | supports | Biological assembly annotation is hexameric with 6 protein instances. This deposited annotation is not an independent in-cell stoichiometry measurement. |
| plaque-mcr-agent-pdb-1mro-entity1 | https://data.rcsb.org/rest/v1/core/polymer_entity/1MRO/1; rcsb_polymer_entity, source organism and SIFTS reference identifiers | supports | Deposited polymer identity and reference mapping inspected: [('P11558', 1.0)]. Source taxon [79929]. No coordinate reanalysis. |
| plaque-mcr-agent-pdb-1mro-entity2 | https://data.rcsb.org/rest/v1/core/polymer_entity/1MRO/2; rcsb_polymer_entity, source organism and SIFTS reference identifiers | supports | Deposited polymer identity and reference mapping inspected: [('P11560', 1.0)]. Source taxon [79929]. No coordinate reanalysis. |
| plaque-mcr-agent-pdb-1mro-entity3 | https://data.rcsb.org/rest/v1/core/polymer_entity/1MRO/3; rcsb_polymer_entity, source organism and SIFTS reference identifiers | supports | Deposited polymer identity and reference mapping inspected: [('P11562', 1.0)]. Source taxon [79929]. No coordinate reanalysis. |
| plaque-mcr-agent-P11558 | https://rest.uniprot.org/uniprotkb/P11558.json; primaryAccession, organism, genes, protein description, FUNCTION/SUBUNIT/COFACTOR/location comments and complete InterPro cross-references | supports | Native reviewed P11558 identifies mcrA in taxon 79929; accession, role, location evidence attribution and family candidates checked within this annotated source. |
| plaque-mcr-agent-P11560 | https://rest.uniprot.org/uniprotkb/P11560.json; primaryAccession, organism, genes, protein description, FUNCTION/SUBUNIT/COFACTOR/location comments and complete InterPro cross-references | supports | Native reviewed P11560 identifies mcrB in taxon 79929; accession, role, location evidence attribution and family candidates checked within this annotated source. |
| plaque-mcr-agent-P11562 | https://rest.uniprot.org/uniprotkb/P11562.json; primaryAccession, organism, genes, protein description, FUNCTION/SUBUNIT/COFACTOR/location comments and complete InterPro cross-references | supports | Native reviewed P11562 identifies mcrG in taxon 79929; accession, role, location evidence attribution and family candidates checked within this annotated source. |
| plaque-mcr-agent-uniprot-unique | https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue%20AND%20taxonomy_id%3A79929%20AND%20%28gene_exact%3AmcrA%20OR%20gene_exact%3AmcrB%20OR%20gene_exact%3AmcrG%29&amp;format=json&amp;size=100; results[].primaryAccession, genes, organism | supports | Native bounded query returns [('P11562', 79929), ('P11560', 79929), ('P11558', 79929)]. |
| plaque-mcr-agent-wrede2013-jats | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3596918/fullTextXML; Abstract; Methods purification/immunolabeling; Results and Discussion; figure captions | supports | Purified M.marburgensis MCR I antigen supports the localization experiment. Signal is cytoplasmic in routine cultures, with condition-dependent membrane association under nickel limitation or levulinic acid. This does not separately localize every isolated subunit or establish universal cytoplasmic exclusivity. |
| plaque-mcr-agent-epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A9367957%20OR%20EXT_ID%3A23533332; Europe PMC publication metadata and abstract | supports | Fresh title/author/DOI/PMID and abstract inspected. Full-text access is only claimed for separately identified body evidence. |
| plaque-complex-i-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0045271%2CGO%3A0098803%2CGO%3A0008137; results[].id/name/aspect/definition/isObsolete | supports | Current authority terms inspected: [('GO:0045271', 'respiratory chain complex I', False), ('GO:0008137', 'NADH dehydrogenase (ubiquinone) activity', False), ('GO:0098803', 'respiratory chain complex', False)]. Obsolete arm terms do not supply current exact component identities. |
| plaque-complex-i-agent-go-arm-candidates | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0042652%2CGO%3A0042653; results[].id/name/aspect/definition/isObsolete | supports | Current authority terms inspected: [('GO:0042652', 'obsolete mitochondrial respiratory chain complex I, peripheral segment', True), ('GO:0042653', 'obsolete mitochondrial respiratory chain complex I, membrane segment', True)]. Obsolete arm terms do not supply current exact component identities. |
| plaque-complex-i-agent-go-peripheral-search | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=peripheral%20arm&amp;limit=100; Returned first page GO name/definition/isObsolete results | supports | Inspected bounded arm-term candidates. The returned candidates do not justify replacing the maintained whole-arm label with an obsolete or mismatched GO term. This is not exhaustive absence evidence. |
| plaque-complex-i-agent-go-membrane-arm-search | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=membrane%20arm&amp;limit=100; Returned first page GO name/definition/isObsolete results | supports | Inspected bounded arm-term candidates. The returned candidates do not justify replacing the maintained whole-arm label with an obsolete or mismatched GO term. This is not exhaustive absence evidence. |
| plaque-complex-i-agent-tax-274 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/274; taxId, scientificName and lineage | supports | Native taxonomy checks the exact organism/strain identifier; species-level deposited source and strain-specific examples remain distinct. |
| plaque-complex-i-agent-tax-300852 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/300852; taxId, scientificName and lineage | supports | Native taxonomy checks the exact organism/strain identifier; species-level deposited source and strain-specific examples remain distinct. |
| plaque-complex-i-agent-epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A23417064%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core; Europe PMC publication metadata and abstract | supports | Fresh title/author/DOI/PMID and abstract inspected. Full-text access is only claimed for separately identified body evidence. |
| plaque-complex-i-agent-baradaran2013-jats | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3672946/fullTextXML; Introduction; Results S1-S4; Methods S6-S11; associated figure captions | supports | Primary structure separates seven conserved hydrophilic and seven conserved membrane subunits, with two additional proteins in this preparation. FMN/FeS NADH electron transfer supports the refreshed peripheral-arm contribution edge. Native Thermus menaquinone is distinct from the decyl-ubiquinone analogue; coupling channels and water networks remain structural proposals, not direct kinetic observations. |
| plaque-complex-i-agent-baradaran2013-supplement-epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3672946/supplementaryFiles; Europe PMC publication metadata and abstract | supports | Fresh title/author/DOI/PMID and abstract inspected. Full-text access is only claimed for separately identified body evidence. |
| plaque-complex-i-agent-pdb-4HEA | https://data.rcsb.org/rest/v1/core/entry/4HEA; struct.title, primary citation, resolution and polymer identities | supports | Deposited structure Crystal structure of the entire respiratory complex I from Thermus thermophilus; native primary citation and structure identifiers checked, without raw-coordinate reanalysis. |
| plaque-complex-i-agent-assembly-4HEA | https://data.rcsb.org/rest/v1/core/assembly/4HEA/1; pdbx_struct_assembly and rcsb_assembly_info | supports | Biological assembly annotation is hexadecameric with 16 protein instances. This deposited annotation is not an independent in-cell stoichiometry measurement. |
| plaque-complex-i-agent-4HEA-entity-1 | https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/1; rcsb_polymer_entity, source organism and SIFTS reference identifiers | supports | Deposited polymer identity and reference mapping inspected: [('Q56222', 1.0)]. Source taxon [300852]. No coordinate reanalysis. |
| plaque-complex-i-agent-4HEA-entity-2 | https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/2; rcsb_polymer_entity, source organism and SIFTS reference identifiers | supports | Deposited polymer identity and reference mapping inspected: [('Q56221', 1.0)]. Source taxon [300852]. No coordinate reanalysis. |
| plaque-complex-i-agent-4HEA-entity-3 | https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/3; rcsb_polymer_entity, source organism and SIFTS reference identifiers | supports | Deposited polymer identity and reference mapping inspected: [('Q56223', 1.0)]. Source taxon [300852]. No coordinate reanalysis. |
| plaque-complex-i-agent-4HEA-entity-4 | https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/4; rcsb_polymer_entity, source organism and SIFTS reference identifiers | supports | Deposited polymer identity and reference mapping inspected: [('Q56220', 1.0)]. Source taxon [300852]. No coordinate reanalysis. |
| plaque-complex-i-agent-4HEA-entity-5 | https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/5; rcsb_polymer_entity, source organism and SIFTS reference identifiers | supports | Deposited polymer identity and reference mapping inspected: [('Q56219', 1.0)]. Source taxon [300852]. No coordinate reanalysis. |
| plaque-complex-i-agent-4HEA-entity-6 | https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/6; rcsb_polymer_entity, source organism and SIFTS reference identifiers | supports | Deposited polymer identity and reference mapping inspected: [('Q56218', 1.0)]. Source taxon [300852]. No coordinate reanalysis. |
| plaque-complex-i-agent-4HEA-entity-7 | https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/7; rcsb_polymer_entity, source organism and SIFTS reference identifiers | supports | Deposited polymer identity and reference mapping inspected: [('Q56224', 1.0)]. Source taxon [300852]. No coordinate reanalysis. |
| plaque-complex-i-agent-4HEA-entity-8 | https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/8; rcsb_polymer_entity, source organism and SIFTS reference identifiers | supports | Deposited polymer identity and reference mapping inspected: [('Q5SKZ7', 1.0)]. Source taxon [300852]. No coordinate reanalysis. |
| plaque-complex-i-agent-4HEA-entity-9 | https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/9; rcsb_polymer_entity, source organism and SIFTS reference identifiers | supports | Deposited polymer identity and reference mapping inspected: [('Q5SI52', 1.0)]. Source taxon [300852]. No coordinate reanalysis. |
| plaque-complex-i-agent-4HEA-entity-10 | https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/10; rcsb_polymer_entity, source organism and SIFTS reference identifiers | supports | Deposited polymer identity and reference mapping inspected: [('Q56217', 1.0)]. Source taxon [300852]. No coordinate reanalysis. |
| plaque-complex-i-agent-4HEA-entity-11 | https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/11; rcsb_polymer_entity, source organism and SIFTS reference identifiers | supports | Deposited polymer identity and reference mapping inspected: [('Q56225', 1.0)]. Source taxon [300852]. No coordinate reanalysis. |
| plaque-complex-i-agent-4HEA-entity-12 | https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/12; rcsb_polymer_entity, source organism and SIFTS reference identifiers | supports | Deposited polymer identity and reference mapping inspected: [('Q56226', 1.0)]. Source taxon [300852]. No coordinate reanalysis. |
| plaque-complex-i-agent-4HEA-entity-13 | https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/13; rcsb_polymer_entity, source organism and SIFTS reference identifiers | supports | Deposited polymer identity and reference mapping inspected: [('Q56227', 1.0)]. Source taxon [300852]. No coordinate reanalysis. |
| plaque-complex-i-agent-4HEA-entity-14 | https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/14; rcsb_polymer_entity, source organism and SIFTS reference identifiers | supports | Deposited polymer identity and reference mapping inspected: [('Q56228', 1.0)]. Source taxon [300852]. No coordinate reanalysis. |
| plaque-complex-i-agent-4HEA-entity-15 | https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/15; rcsb_polymer_entity, source organism and SIFTS reference identifiers | supports | Deposited polymer identity and reference mapping inspected: [('Q56229', 1.0)]. Source taxon [300852]. No coordinate reanalysis. |
| plaque-complex-i-agent-4HEA-entity-16 | https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/16; rcsb_polymer_entity, source organism and SIFTS reference identifiers | supports | Deposited polymer identity and reference mapping inspected: [('Q60019', 1.0)]. Source taxon [300852]. No coordinate reanalysis. |
| plaque-complex-i-agent-Q56222 | https://rest.uniprot.org/uniprotkb/Q56222.json; primaryAccession, organism, genes, protein description, FUNCTION/SUBUNIT/COFACTOR/location comments and complete InterPro cross-references | supports | Native reviewed Q56222 identifies nqo1 in taxon 300852; accession, role, location evidence attribution and family candidates checked within this annotated source. |
| plaque-complex-i-agent-Q56221 | https://rest.uniprot.org/uniprotkb/Q56221.json; primaryAccession, organism, genes, protein description, FUNCTION/SUBUNIT/COFACTOR/location comments and complete InterPro cross-references | supports | Native reviewed Q56221 identifies nqo2 in taxon 300852; accession, role, location evidence attribution and family candidates checked within this annotated source. |
| plaque-complex-i-agent-Q56223 | https://rest.uniprot.org/uniprotkb/Q56223.json; primaryAccession, organism, genes, protein description, FUNCTION/SUBUNIT/COFACTOR/location comments and complete InterPro cross-references | supports | Native reviewed Q56223 identifies nqo3 in taxon 300852; accession, role, location evidence attribution and family candidates checked within this annotated source. |
| plaque-complex-i-agent-Q56220 | https://rest.uniprot.org/uniprotkb/Q56220.json; primaryAccession, organism, genes, protein description, FUNCTION/SUBUNIT/COFACTOR/location comments and complete InterPro cross-references | supports | Native reviewed Q56220 identifies nqo4 in taxon 300852; accession, role, location evidence attribution and family candidates checked within this annotated source. |
| plaque-complex-i-agent-Q56219 | https://rest.uniprot.org/uniprotkb/Q56219.json; primaryAccession, organism, genes, protein description, FUNCTION/SUBUNIT/COFACTOR/location comments and complete InterPro cross-references | supports | Native reviewed Q56219 identifies nqo5 in taxon 300852; accession, role, location evidence attribution and family candidates checked within this annotated source. |
| plaque-complex-i-agent-Q56218 | https://rest.uniprot.org/uniprotkb/Q56218.json; primaryAccession, organism, genes, protein description, FUNCTION/SUBUNIT/COFACTOR/location comments and complete InterPro cross-references | supports | Native reviewed Q56218 identifies nqo6 in taxon 300852; accession, role, location evidence attribution and family candidates checked within this annotated source. |
| plaque-complex-i-agent-Q56224 | https://rest.uniprot.org/uniprotkb/Q56224.json; primaryAccession, organism, genes, protein description, FUNCTION/SUBUNIT/COFACTOR/location comments and complete InterPro cross-references | supports | Native reviewed Q56224 identifies nqo9 in taxon 300852; accession, role, location evidence attribution and family candidates checked within this annotated source. |
| plaque-complex-i-agent-Q56217 | https://rest.uniprot.org/uniprotkb/Q56217.json; primaryAccession, organism, genes, protein description, FUNCTION/SUBUNIT/COFACTOR/location comments and complete InterPro cross-references | supports | Native reviewed Q56217 identifies nqo7 in taxon 300852; accession, role, location evidence attribution and family candidates checked within this annotated source. |
| plaque-complex-i-agent-Q56225 | https://rest.uniprot.org/uniprotkb/Q56225.json; primaryAccession, organism, genes, protein description, FUNCTION/SUBUNIT/COFACTOR/location comments and complete InterPro cross-references | supports | Native reviewed Q56225 identifies nqo10 in taxon 300852; accession, role, location evidence attribution and family candidates checked within this annotated source. |
| plaque-complex-i-agent-Q56226 | https://rest.uniprot.org/uniprotkb/Q56226.json; primaryAccession, organism, genes, protein description, FUNCTION/SUBUNIT/COFACTOR/location comments and complete InterPro cross-references | supports | Native reviewed Q56226 identifies nqo11 in taxon 300852; accession, role, location evidence attribution and family candidates checked within this annotated source. |
| plaque-complex-i-agent-Q56227 | https://rest.uniprot.org/uniprotkb/Q56227.json; primaryAccession, organism, genes, protein description, FUNCTION/SUBUNIT/COFACTOR/location comments and complete InterPro cross-references | supports | Native reviewed Q56227 identifies nqo12 in taxon 300852; accession, role, location evidence attribution and family candidates checked within this annotated source. |
| plaque-complex-i-agent-Q56228 | https://rest.uniprot.org/uniprotkb/Q56228.json; primaryAccession, organism, genes, protein description, FUNCTION/SUBUNIT/COFACTOR/location comments and complete InterPro cross-references | supports | Native reviewed Q56228 identifies nqo13 in taxon 300852; accession, role, location evidence attribution and family candidates checked within this annotated source. |
| plaque-complex-i-agent-Q56229 | https://rest.uniprot.org/uniprotkb/Q56229.json; primaryAccession, organism, genes, protein description, FUNCTION/SUBUNIT/COFACTOR/location comments and complete InterPro cross-references | supports | Native reviewed Q56229 identifies nqo14 in taxon 300852; accession, role, location evidence attribution and family candidates checked within this annotated source. |
| plaque-complex-i-agent-Q60019 | https://rest.uniprot.org/uniprotkb/Q60019.json; primaryAccession, organism, genes, protein description, FUNCTION/SUBUNIT/COFACTOR/location comments and complete InterPro cross-references | supports | Native reviewed Q60019 identifies nqo8 in taxon 300852; accession, role, location evidence attribution and family candidates checked within this annotated source. |
| plaque-complex-i-agent-query-nqo | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=%28gene%3Anqo%2A%29%20AND%20%28organism_id%3A300852%29%20AND%20%28reviewed%3Atrue%29; results[].primaryAccession, genes, organism | supports | Native bounded query returns [('Q56221', 300852), ('Q56223', 300852), ('Q56218', 300852), ('Q56224', 300852), ('Q56222', 300852), ('Q5SKZ7', 300852), ('Q56225', 300852), ('Q56219', 300852), ('Q56220', 300852), ('Q56226', 300852), ('Q56228', 300852), ('Q56229', 300852), ('Q60019', 300852), ('Q56217', 300852), ('Q56227', 300852)]. |
| plaque-complex-i-agent-ipr-001750 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001750/; metadata.accession/type/name, integrated member signatures and description | supports | Inspected domain IPR001750, NADH:quinone oxidoreductase/Mrp antiporter, transmembrane domain, against exact whole-component scope. |
| plaque-complex-i-agent-ipr-006137 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006137/; metadata.accession/type/name, integrated member signatures and description | supports | Inspected domain IPR006137, NADH:ubiquinone oxidoreductase-like, 20kDa subunit, against exact whole-component scope. |
| plaque-sdh-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0008177,GO:0045273,GO:0098803; results[].id/name/aspect/definition/isObsolete | supports | Current authority terms inspected: [('GO:0045273', 'respiratory chain complex II (succinate dehydrogenase)', False), ('GO:0008177', 'succinate dehydrogenase (quinone) activity', False), ('GO:0098803', 'respiratory chain complex', False)]. Obsolete arm terms do not supply current exact component identities. |
| plaque-sdh-agent-tax-562 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562; taxId, scientificName and lineage | supports | Native taxonomy checks the exact organism/strain identifier; species-level deposited source and strain-specific examples remain distinct. |
| plaque-sdh-agent-tax-83333 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333; taxId, scientificName and lineage | supports | Native taxonomy checks the exact organism/strain identifier; species-level deposited source and strain-specific examples remain distinct. |
| plaque-sdh-agent-P0AC41 | https://rest.uniprot.org/uniprotkb/P0AC41.json; primaryAccession, organism, genes, protein description, FUNCTION/SUBUNIT/COFACTOR/location comments and complete InterPro cross-references | supports | Native reviewed P0AC41 identifies sdhA in taxon 83333; accession, role, location evidence attribution and family candidates checked within this annotated source. |
| plaque-sdh-agent-query-sdhA | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AsdhA%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29; results[].primaryAccession, genes, organism | supports | Native bounded query returns [('P0AC41', 83333)]. |
| plaque-sdh-agent-P07014 | https://rest.uniprot.org/uniprotkb/P07014.json; primaryAccession, organism, genes, protein description, FUNCTION/SUBUNIT/COFACTOR/location comments and complete InterPro cross-references | supports | Native reviewed P07014 identifies sdhB in taxon 83333; accession, role, location evidence attribution and family candidates checked within this annotated source. |
| plaque-sdh-agent-query-sdhB | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AsdhB%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29; results[].primaryAccession, genes, organism | supports | Native bounded query returns [('P07014', 83333)]. |
| plaque-sdh-agent-P69054 | https://rest.uniprot.org/uniprotkb/P69054.json; primaryAccession, organism, genes, protein description, FUNCTION/SUBUNIT/COFACTOR/location comments and complete InterPro cross-references | supports | Native reviewed P69054 identifies sdhC in taxon 83333; accession, role, location evidence attribution and family candidates checked within this annotated source. |
| plaque-sdh-agent-query-sdhC | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AsdhC%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29; results[].primaryAccession, genes, organism | supports | Native bounded query returns [('P69054', 83333)]. |
| plaque-sdh-agent-P0AC44 | https://rest.uniprot.org/uniprotkb/P0AC44.json; primaryAccession, organism, genes, protein description, FUNCTION/SUBUNIT/COFACTOR/location comments and complete InterPro cross-references | supports | Native reviewed P0AC44 identifies sdhD in taxon 83333; accession, role, location evidence attribution and family candidates checked within this annotated source. |
| plaque-sdh-agent-query-sdhD | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AsdhD%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29; results[].primaryAccession, genes, organism | supports | Native bounded query returns [('P0AC44', 83333)]. |
| plaque-sdh-agent-matches-P0AC41 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P0AC41/?page_size=200; Complete returned integrated InterPro entries for exact accession | supports | Current native protein-to-InterPro match list inspected, including the additional P07014 IPR050573 family. Matches are candidates, not automatic exact grounding. |
| plaque-sdh-agent-matches-P07014 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P07014/?page_size=200; Complete returned integrated InterPro entries for exact accession | supports | Current native protein-to-InterPro match list inspected, including the additional P07014 IPR050573 family. Matches are candidates, not automatic exact grounding. |
| plaque-sdh-agent-matches-P69054 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P69054/?page_size=200; Complete returned integrated InterPro entries for exact accession | supports | Current native protein-to-InterPro match list inspected, including the additional P07014 IPR050573 family. Matches are candidates, not automatic exact grounding. |
| plaque-sdh-agent-matches-P0AC44 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P0AC44/?page_size=200; Complete returned integrated InterPro entries for exact accession | supports | Current native protein-to-InterPro match list inspected, including the additional P07014 IPR050573 family. Matches are candidates, not automatic exact grounding. |
| plaque-sdh-agent-IPR011281 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR011281/; metadata.accession/type/name, integrated member signatures and description | supports | Inspected family IPR011281, Succinate dehydrogenase, flavoprotein subunit, against exact whole-component scope. |
| plaque-sdh-agent-IPR014006 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR014006/; metadata.accession/type/name, integrated member signatures and description | supports | Inspected family IPR014006, Succinate dehydrogenase/fumarate reductase, flavoprotein subunit, against exact whole-component scope. |
| plaque-sdh-agent-IPR030664 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR030664/; metadata.accession/type/name, integrated member signatures and description | supports | Inspected family IPR030664, FAD-dependent oxidoreductase SdhA/FrdA/AprA, against exact whole-component scope. |
| plaque-sdh-agent-IPR065464 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR065464/; metadata.accession/type/name, integrated member signatures and description | supports | Inspected family IPR065464, Succinate dehydrogenase hydrophobic membrane anchor subunit, against exact whole-component scope. |
| plaque-sdh-agent-pdb-1NEK | https://data.rcsb.org/rest/v1/core/entry/1NEK; struct.title, primary citation, resolution and polymer identities | supports | Deposited structure Complex II (Succinate Dehydrogenase) From E. Coli with ubiquinone bound; native primary citation and structure identifiers checked, without raw-coordinate reanalysis. |
| plaque-sdh-agent-assembly-1NEK | https://data.rcsb.org/rest/v1/core/assembly/1NEK/1; pdbx_struct_assembly and rcsb_assembly_info | supports | Biological assembly annotation is tetrameric with 4 protein instances. This deposited annotation is not an independent in-cell stoichiometry measurement. |
| plaque-sdh-agent-1NEK-entity-1 | https://data.rcsb.org/rest/v1/core/polymer_entity/1NEK/1; rcsb_polymer_entity, source organism and SIFTS reference identifiers | supports | Deposited polymer identity and reference mapping inspected: [('P0AC41', 1.0)]. Source taxon [562]. No coordinate reanalysis. |
| plaque-sdh-agent-1NEK-entity-2 | https://data.rcsb.org/rest/v1/core/polymer_entity/1NEK/2; rcsb_polymer_entity, source organism and SIFTS reference identifiers | supports | Deposited polymer identity and reference mapping inspected: [('P07014', 1.0)]. Source taxon [562]. No coordinate reanalysis. |
| plaque-sdh-agent-1NEK-entity-3 | https://data.rcsb.org/rest/v1/core/polymer_entity/1NEK/3; rcsb_polymer_entity, source organism and SIFTS reference identifiers | supports | Deposited polymer identity and reference mapping inspected: [('P69054', 1.0)]. Source taxon [562]. No coordinate reanalysis. |
| plaque-sdh-agent-1NEK-entity-4 | https://data.rcsb.org/rest/v1/core/polymer_entity/1NEK/4; rcsb_polymer_entity, source organism and SIFTS reference identifiers | supports | Deposited polymer identity and reference mapping inspected: [('P0AC44', 1.0)]. Source taxon [562]. No coordinate reanalysis. |
| plaque-sdh-agent-pmid-12560550 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID:12560550%20AND%20SRC:MED; Europe PMC publication metadata and abstract | supports | Fresh title/author/DOI/PMID and abstract inspected. Full-text access is only claimed for separately identified body evidence. |
| plaque-sdh-agent-pmid-15919996 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID:15919996%20AND%20SRC:MED; Europe PMC publication metadata and abstract | supports | Fresh title/author/DOI/PMID and abstract inspected. Full-text access is only claimed for separately identified body evidence. |
| plaque-sdh-agent-pmid-16079137 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID:16079137%20AND%20SRC:MED; Europe PMC publication metadata and abstract | supports | Fresh title/author/DOI/PMID and abstract inspected. Full-text access is only claimed for separately identified body evidence. |
| plaque-adapter-datasets | https://imodulondb.org/api/datasets; Complete public dataset catalogue, all organism and dataset labels | supports | Catalogue covers E.coli, including precise_mg1655. No Methanothermobacter marburgensis or Thermus thermophilus dataset is listed; the listed Sulfolobus archaeal datasets do not match the methanogen target. Absence is bounded to this retrieved catalogue. |
| plaque-adapter-frontend | https://imodulondb.org/assets/index-3_RVHvkS.js; Public frontend route declarations for dataset, gene search, gene-to-module membership and module member tables | supports | Read-only public source routes inspected; no authentication or mutation route was used. |
| plaque-adapter-meta | https://imodulondb.org/api/datasets/e_coli/precise_mg1655/meta; organism, dataset, strains, sample/condition/module counts, publication_url | supports | Selected E.coli precise_mg1655 dataset identifies MG1655,586 samples,281 conditions and115 modules; publication_url is null. This is dataset coverage, not structural evidence. |
| plaque-adapter-search-sdhA | https://imodulondb.org/api/search?organism=e_coli&amp;dataset=precise_mg1655&amp;query=sdhA&amp;limit=50; Returned genes and imodulons arrays | supports | Exact sdhA search resolves [('b0723', 'sdhA')]. Memberships were checked separately. |
| plaque-adapter-search-sdhB | https://imodulondb.org/api/search?organism=e_coli&amp;dataset=precise_mg1655&amp;query=sdhB&amp;limit=50; Returned genes and imodulons arrays | supports | Exact sdhB search resolves [('b0724', 'sdhB')]. Memberships were checked separately. |
| plaque-adapter-search-sdhC | https://imodulondb.org/api/search?organism=e_coli&amp;dataset=precise_mg1655&amp;query=sdhC&amp;limit=50; Returned genes and imodulons arrays | supports | Exact sdhC search resolves [('b0721', 'sdhC')]. Memberships were checked separately. |
| plaque-adapter-search-sdhD | https://imodulondb.org/api/search?organism=e_coli&amp;dataset=precise_mg1655&amp;query=sdhD&amp;limit=50; Returned genes and imodulons arrays | supports | Exact sdhD search resolves [('b0722', 'sdhD')]. Memberships were checked separately. |
| plaque-mcr-agent-IPR003178-retry | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR003178/; metadata.accession/type/name, integrated member signatures and description | supports | Inspected family IPR003178, Methyl-coenzyme M reductase, gamma subunit, against exact whole-component scope. |
| plaque-sdh-agent-IPR004489-retry | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004489/; metadata.accession/type/name, integrated member signatures and description | supports | Inspected family IPR004489, Succinate dehydrogenase/fumarate reductase iron-sulphur protein, against exact whole-component scope. |
| plaque-sdh-agent-IPR014314-retry | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR014314/; metadata.accession/type/name, integrated member signatures and description | supports | Inspected family IPR014314, Succinate dehydrogenase, cytochrome b556 subunit, against exact whole-component scope. |
| plaque-sdh-agent-IPR014312-retry | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR014312/; metadata.accession/type/name, integrated member signatures and description | supports | Inspected family IPR014312, Succinate dehydrogenase, hydrophobic membrane anchor, against exact whole-component scope. |
| plaque-adapter-gene-modules-sdhC | https://imodulondb.org/api/genes/e_coli/precise_mg1655/b0721/imodulons; All returned membership flags, weights and thresholds for sdhC | supports | Thresholded memberships (k,name,weight): [(1, 'Crp', '0.113468878'), (14, 'ArcA-1', '0.110789085'), (10, 'ArcA-2', '0.081351196')]. Below-threshold membership is not evidence against physical complex membership. |
| plaque-adapter-gene-modules-sdhA | https://imodulondb.org/api/genes/e_coli/precise_mg1655/b0723/imodulons; All returned membership flags, weights and thresholds for sdhA | supports | Thresholded memberships (k,name,weight): [(10, 'ArcA-2', '0.109620945'), (1, 'Crp', '0.096358976'), (14, 'ArcA-1', '0.079630832')]. Below-threshold membership is not evidence against physical complex membership. |
| plaque-adapter-gene-modules-sdhB | https://imodulondb.org/api/genes/e_coli/precise_mg1655/b0724/imodulons; All returned membership flags, weights and thresholds for sdhB | supports | Thresholded memberships (k,name,weight): [(10, 'ArcA-2', '0.10452537'), (1, 'Crp', '0.097856111')]. Below-threshold membership is not evidence against physical complex membership. |
| plaque-adapter-gene-modules-sdhD | https://imodulondb.org/api/genes/e_coli/precise_mg1655/b0722/imodulons; All returned membership flags, weights and thresholds for sdhD | supports | Thresholded memberships (k,name,weight): [(14, 'ArcA-1', '0.100289611'), (1, 'Crp', '0.09939565'), (10, 'ArcA-2', '0.088084304')]. Below-threshold membership is not evidence against physical complex membership. |
| plaque-sdh-agent-IPR050573 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050573/; metadata.type/name, integrated PANTHER PTHR11921, description provenance flags | supports | Current P07014 match is a family explicitly named Succinate Dehydrogenase/Fumarate Reductase Iron-Sulfur. Its description is flagged LLM-generated and unchecked and was not used as biological evidence; the broad integrated family label does not establish exact SdhB-only equivalence. |
| plaque-adapter-summary-1 | https://imodulondb.org/api/imodulons/e_coli/precise_mg1655/1; k, imodulon_name, regulator, function_description, n_genes, threshold | supports | Native module 1 (Crp) has 32 thresholded genes; threshold 0.068750263; source annotation carbohydrate transport and metabolism. AI-generated narrative and activity matrices were excluded from biological inference. |
| plaque-adapter-members-1 | https://imodulondb.org/api/imodulons/e_coli/precise_mg1655/1/genes?limit=50; genes[].gene_id/gene_name/weight/in_imodulon/uniprot_id; request limit=50 | supports | Inspected all 32 returned member identifier/weight rows and matched the Sdh components; observed [('sdhC', 'P69054'), ('sdhD', 'P0AC44'), ('sdhB', 'P07014'), ('sdhA', 'P0AC41')]. No physical assembly or causal claim is inferred. |
| plaque-adapter-summary-10 | https://imodulondb.org/api/imodulons/e_coli/precise_mg1655/10; k, imodulon_name, regulator, function_description, n_genes, threshold | supports | Native module 10 (ArcA-2) has 37 thresholded genes; threshold 0.061542713; source annotation anaerobiosis/repression of aerobic growth genes during anaerobic growth. AI-generated narrative and activity matrices were excluded from biological inference. |
| plaque-adapter-members-10 | https://imodulondb.org/api/imodulons/e_coli/precise_mg1655/10/genes?limit=50; genes[].gene_id/gene_name/weight/in_imodulon/uniprot_id; request limit=50 | supports | Inspected all 37 returned member identifier/weight rows and matched the Sdh components; observed [('sdhA', 'P0AC41'), ('sdhB', 'P07014'), ('sdhD', 'P0AC44'), ('sdhC', 'P69054')]. No physical assembly or causal claim is inferred. |
| plaque-adapter-summary-14 | https://imodulondb.org/api/imodulons/e_coli/precise_mg1655/14; k, imodulon_name, regulator, function_description, n_genes, threshold | supports | Native module 14 (ArcA-1) has 23 thresholded genes; threshold 0.07235406; source annotation anaerobiosis/repression of aerobic growth genes during anaerobic growth. AI-generated narrative and activity matrices were excluded from biological inference. |
| plaque-adapter-members-14 | https://imodulondb.org/api/imodulons/e_coli/precise_mg1655/14/genes?limit=50; genes[].gene_id/gene_name/weight/in_imodulon/uniprot_id; request limit=50 | supports | Inspected all 23 returned member identifier/weight rows and matched the Sdh components; observed [('sdhC', 'P69054'), ('sdhD', 'P0AC44'), ('sdhA', 'P0AC41')]. No physical assembly or causal claim is inferred. |
| plaque-mcr-primary-browser | https://go.gale.com/ps/i.do?asid=294e1b4d&amp;id=GALE%7CA20105096&amp;it=r&amp;p=AONE&amp;u=googlescholar&amp;v=2.1; Fresh browser-extracted Ermler1997 primary transcription, claim-bearing structure/reaction paragraphs36-77 | supports | Primary article transcription supports alpha2beta2gamma2 architecture and two F430 sites. Crystals were inactive enzyme states; the mechanistic proposal is not a direct observation of active turnover. Hash binds serialized browser extraction, not publisher PDF bytes. |
| plaque-sdh-stenberg-browser | https://doi.org/10.1074/jbc.M506479200; Fresh indexed publisher Methods passages; full-page browser open failed500 | supports | Inspected indexed primary Methods describing BL21(DE3)pLysS cultures and membrane preparation/BN-PAGE. This pass did not independently reread the Sdh result subsection or figure pixels; native UniProt separately verifies citation attribution. Hash binds serialized browser results, not a complete publisher body. |
| plaque-current-0 | data/structures/energy_complex/methyl_coenzyme_m_reductase_complex.yaml; Entire current record and causal graph/history | supports | Stale frozen target compared with current bytes and substantively reassessed; the original historical input attestation remains unchanged. |
| plaque-original-0 | reviews/structured/20261021T091345Z-methyl-coenzyme-m-reductase-complex-audit/review.yaml; Original whole review, findings, assessments and limitations | supports | Original qualified pass has no findings; historical native validation, Markdown render and frozen input hashes independently pass. |
| plaque-current-1 | data/structures/energy_complex/respiratory_chain_complex_i.yaml; Entire current record and causal graph/history | supports | Stale frozen target compared with current bytes and substantively reassessed; the original historical input attestation remains unchanged. |
| plaque-original-1 | reviews/structured/20261021T091350Z-respiratory-chain-complex-i-audit/review.yaml; Original whole review, findings, assessments and limitations | supports | Original qualified pass has no findings; historical native validation, Markdown render and frozen input hashes independently pass. |
| plaque-current-2 | data/structures/energy_complex/respiratory_chain_complex_ii_succinate_dehydrogenase.yaml; Entire current record and causal graph/history | supports | Stale frozen target compared with current bytes and substantively reassessed; the original historical input attestation remains unchanged. |
| plaque-original-2 | reviews/structured/20261021T091351Z-respiratory-chain-complex-ii-succinate-dehydrogenase-audit/review.yaml; Original whole review, findings, assessments and limitations | supports | Original qualified pass has no findings; historical native validation, Markdown render and frozen input hashes independently pass. |
| plaque-mcr-category-prior | reviews/structured/20261025T071006Z-energy-complex-category-review/review.yaml; F2; exact category review identity, affected target and grounding field paths | supports | Prior minor finding identifies three omitted component-ref node groundings. Current record has all three corresponding verified InterPro values. The root confirms associated issue2432 was already closed; no record repair is attributed to PR2351. |
| plaque-original-validation | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2351/adversary-plaque/original-validation.json; Original three native validate/render and historical input hash checks | supports | All three original bundle validation/render/hash checks pass against their historical revisions. |
| plaque-mcr-native-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2351/mcr-uniprot-verify-receipt.json; Complete receipt and linked log; stdout SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Root-executed native verifier passes: all current UniProtKB protein_examples and causal graph xrefs verified. Independently inspected receipt and log; this reviewer did not rerun the command. |
| plaque-mcr-native-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2351/mcr-uniprot-causal-receipt.json; Complete receipt and linked log; stdout SHA256 8076de7f3af7f26f94f4ebdd894d164d3ffff744f5afc092ba8cd60e97cc1798 | supports | Root-executed native causal graph audit passes: 3 GENE_OR_PROTEIN nodes COVERED; all other reported categories zero. Coverage means examples cover declared gene symbols, not experimental assembly necessity. Independently inspected receipt and log; this reviewer did not rerun the command. |
| plaque-complex-i-native-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2351/complex-i-uniprot-verify-receipt.json; Complete receipt and linked log; stdout SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Root-executed native verifier passes: all current UniProtKB protein_examples and causal graph xrefs verified. Independently inspected receipt and log; this reviewer did not rerun the command. |
| plaque-complex-i-native-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2351/complex-i-uniprot-causal-receipt.json; Complete receipt and linked log; stdout SHA256 633f42f63c3f46c078be270a8917a0d33c4e99bf9677469acf36fd3061d11a35 | supports | Root-executed native causal graph audit passes: 2 GENE_OR_PROTEIN nodes COVERED; all other reported categories zero. Coverage means examples cover declared gene symbols, not experimental assembly necessity. Independently inspected receipt and log; this reviewer did not rerun the command. |
| plaque-complex-ii-native-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2351/complex-ii-uniprot-verify-receipt.json; Complete receipt and linked log; stdout SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Root-executed native verifier passes: all current UniProtKB protein_examples and causal graph xrefs verified. Independently inspected receipt and log; this reviewer did not rerun the command. |
| plaque-complex-ii-native-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2351/complex-ii-uniprot-causal-receipt.json; Complete receipt and linked log; stdout SHA256 80d0a4439ebf3fc5efc9c149ca8dd16309e5c2482d4a18223120024cb5e555d1 | supports | Root-executed native causal graph audit passes: 3 GENE_OR_PROTEIN nodes COVERED; all other reported categories zero. Coverage means examples cover declared gene symbols, not experimental assembly necessity. Independently inspected receipt and log; this reviewer did not rerun the command. |
| micro-record-psii | data/structures/energy_complex/photosystem_ii.yaml; Entire current maintained YAML, including provenance, discussions, component examples and all graph edges. | supports | Current source-head input; SHA matches native inspect. Target bytes unchanged since the original frozen review. |
| micro-prior-psii | reviews/structured/20261021T091346Z-photosystem-ii-audit/review.yaml; Original full YAML assessments, checks, evidence access scopes, findings/actions and source hashes; paired Markdown checked by native renderer. | supports | Historical original preserved. Its timestamps/checks are historical, not newly executed. Original disposition is retained only where freshly supported. |
| micro-record-rod | data/structures/energy_complex/phycobilisome_rod.yaml; Entire current maintained YAML, including provenance, discussions, component examples and all graph edges. | supports | Current source-head input; SHA matches native inspect. Changed since original: one CpcD identity-only example and its curation event were added. |
| micro-prior-rod | reviews/structured/20261021T091347Z-phycobilisome-rod-audit/review.yaml; Original full YAML assessments, checks, evidence access scopes, findings/actions and source hashes; paired Markdown checked by native renderer. | supports | Historical original preserved. Its timestamps/checks are historical, not newly executed. Original F1 remains open and current example additions require reassessment. |
| micro-record-bacterial-psii | data/structures/energy_complex/plasma_membrane_derived_thylakoid_photosystem_ii.yaml; Entire current maintained YAML, including provenance, discussions, component examples and all graph edges. | supports | Current source-head input; SHA matches native inspect. Target bytes unchanged since the original frozen review. |
| micro-prior-bacterial-psii | reviews/structured/20261021T091348Z-plasma-membrane-derived-thylakoid-photosystem-ii-audit/review.yaml; Original full YAML assessments, checks, evidence access scopes, findings/actions and source hashes; paired Markdown checked by native renderer. | supports | Historical original preserved. Its timestamps/checks are historical, not newly executed. Original disposition is retained only where freshly supported. |
| micro-policy | docs/CURATION.md; Evidence rules and Components, especially label-only grounding and assembly essentiality. | supports | Known component membership may be represented without guessed family identifiers; essentiality concerns structure formation, not organism viability. |
| micro-protein-policy | .claude/skills/uniprot-protein-examples/SKILL.md; Rules 2–5 and read-only verify/causal audit. | supports | Exact native gene/ORF and taxon/status checks are distinct from support for literature-symbol mapping and experimental membership. |
| micro-adapter-policy | .claude/skills/review-yaml-record/SKILL.md; Structured Source Cross-Checks. | supports | Named genes, proteins and pathways trigger catalogue applicability and bounded covered-dataset checks; expression modules do not prove structure membership. |
| micro-local-core | data/structures/energy_complex/phycobilisome_core.yaml; Identifier, label, definition, parent_structures and part_of only. | supports | The rod graph reference resolves to the distinct central allophycocyanin core. No independent full review of this neighboring record is claimed. |
| micro-native-verifier | scripts/uniprot_genes.py; verify_records checks on accessions/status/protein labels/gene tokens/taxa and component_ref; read-only CLI mode declarations. | supports | Native success verifies asserted ORF identity and graph coverage, not the independent cpcC orthology asserted in free-text role/evidence. |
| micro-workflow-config | conf/record_review.yaml; Entire route and rubric configuration, reread against newly frozen49-input inspect at2026-11-03T05:16:19Z. | supports | Routes include record/category/curation-audit/literature-evidence with the same inspected native rubrics. An earlier route-only read preceded its addition to inspect; this final workflow applicability assessment follows the frozen-byte reread. No changed rule or scientific judgment results. |
| micro-psii-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009523,GO:0009521,GO:0009767; Native QuickGO exact requested term results: IDs, names, definitions, synonyms, aspects and returned child relations. | supports | Exact ontology boundaries and physiological functions inspected. Whole phycobilisome, peripheral rod, generic PSII and bacterial-thylakoid PSII remain distinct; no exhaustive ontology search is claimed. |
| micro-rod-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030076,GO:0030089,GO:0009765; Native QuickGO exact requested term results: IDs, names, definitions, synonyms, aspects and returned child relations. | supports | Exact ontology boundaries and physiological functions inspected. Whole phycobilisome, peripheral rod, generic PSII and bacterial-thylakoid PSII remain distinct; no exhaustive ontology search is claimed. |
| micro-psii-prep-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009523,GO:0009767,GO:0030075,GO:0030089,GO:0030096,GO:0031676; Native QuickGO exact requested term results: IDs, names, definitions, synonyms, aspects and returned child relations. | supports | Exact ontology boundaries and physiological functions inspected. Whole phycobilisome, peripheral rod, generic PSII and bacterial-thylakoid PSII remain distinct; no exhaustive ontology search is claimed. |
| micro-psii-agent-tax-1117 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1117; Native taxonomy JSON taxId, scientificName, rank, lineage and otherNames. | supports | Authority confirms the cited taxon label/identifier. Thermostichus vulcanus and Rupite strain are not interchangeable; Nostoc PCC7120 includes the paper’s Anabaena name. |
| micro-psii-agent-tax-32053 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/32053; Native taxonomy JSON taxId, scientificName, rank, lineage and otherNames. | supports | Authority confirms the cited taxon label/identifier. Thermostichus vulcanus and Rupite strain are not interchangeable; Nostoc PCC7120 includes the paper’s Anabaena name. |
| micro-rod-agent-tax-2763 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2763; Native taxonomy JSON taxId, scientificName, rank, lineage and otherNames. | supports | Authority confirms the cited taxon label/identifier. Thermostichus vulcanus and Rupite strain are not interchangeable; Nostoc PCC7120 includes the paper’s Anabaena name. |
| micro-rod-agent-tax-2813851 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2813851; Native taxonomy JSON taxId, scientificName, rank, lineage and otherNames. | supports | Authority confirms the cited taxon label/identifier. Thermostichus vulcanus and Rupite strain are not interchangeable; Nostoc PCC7120 includes the paper’s Anabaena name. |
| micro-psii-prep-tax-103690 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/103690; Native taxonomy JSON taxId, scientificName, rank, lineage and otherNames. | supports | Authority confirms the cited taxon label/identifier. Thermostichus vulcanus and Rupite strain are not interchangeable; Nostoc PCC7120 includes the paper’s Anabaena name. |
| micro-psii-agent-umena2011-pdf | https://chemie.uni-muenchen.de/ac/kluefers/homepage/L/bac/oec_2011.pdf; Umena et al. 2011, Nature 473:55–60 and online Methods; extracted primary body, abstract, composition/Mn4CaO5/pigment/quinone sections and figure captions; no figure-pixel or diffraction reanalysis. | supports | Purified oxygen-evolving T. vulcanus PSII resolved at 1.9 Å supports core proteins, Mn4CaO5 cluster, chlorophyll/pheophytin/carotenoid cofactors and donor/acceptor architecture. Modeled 19 subunits versus canonical 20 reflects PsbY lost during preparation; no universal stoichiometry or depletion/assembly necessity is inferred. |
| micro-psii-kamiya2003-html | https://pmc.ncbi.nlm.nih.gov/articles/PMC140893/; PMC140893 readable primary HTML: Abstract, Introduction, Materials/Methods and selected Results on subunit/cofactor architecture; paragraph extraction indices 12–16, 24–27 and corresponding captions. | supports | Current full-body access succeeds, unlike the original historical access attempt. Purified active T. vulcanus PSII at 3.7 Å contains D1/D2, CP43/CP47 and cofactors. Methods used T. vulcanus D1/cyt c550 sequences and T. elongatus sequences for other subunits; this is not exact native sequence proof for every T. vulcanus protein. |
| micro-psii-kawakami2009-html | https://pmc.ncbi.nlm.nih.gov/articles/PMC2688974/; PMC2688974 readable HTML: Abstract; Results oxygen evolution with Br/I substitution and reconstitution; Discussion; purification/crystallization and oxygen-evolution Methods (extraction paragraphs 16,19–21,24,26,47–51,54–55,60). | supports | Current body access succeeds. T. vulcanus purified PSII halide experiments correlate two anion sites with oxygen evolution. Their functional perturbation does not test assembly necessity of every pigment or metal-cluster class. |
| micro-psii-agent-P51765 | https://rest.uniprot.org/uniprotkb/P51765.json; Native UniProt entry accession/status, exact geneName, organism, protein name, functional/cofactor annotations and SUBCELLULAR LOCATION evidence. | supports | Reviewed T. vulcanus psbA/D1 and psbD/D2 examples match their native gene/status/taxon; listed PMIDs12518057,19433803,21499260 are actually carried as ECO:0000269 thylakoid annotations. These annotations and inspected primary structures are kept distinct. |
| micro-psii-agent-D0VWR8 | https://rest.uniprot.org/uniprotkb/D0VWR8.json; Native UniProt entry accession/status, exact geneName, organism, protein name, functional/cofactor annotations and SUBCELLULAR LOCATION evidence. | supports | Reviewed T. vulcanus psbA/D1 and psbD/D2 examples match their native gene/status/taxon; listed PMIDs12518057,19433803,21499260 are actually carried as ECO:0000269 thylakoid annotations. These annotations and inspected primary structures are kept distinct. |
| micro-psii-agent-uniprot-unique | https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue%20AND%20taxonomy_id%3A32053%20AND%20%28gene_exact%3ApsbA%20OR%20gene_exact%3ApsbD%29&amp;format=json&amp;size=100; Native query response and X-Total-Results=2; no next-page Link header. | supports | The bounded exact reviewed psbA/psbD query returns P51765 and D0VWR8; this supports the present single reviewed entry per symbol in this taxon query. |
| micro-psii-agent-epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A21499260%20OR%20EXT_ID%3A12518057%20OR%20EXT_ID%3A19433803; Exact three cited PMID metadata and abstracts, not surrogate full-body evidence. | supports | Citation identities verified; primary bodies/PDF are separately inspected and cited. |
| micro-psii-agent-IPR005867 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005867/; Native InterPro metadata accession/name/type and explanatory domain/family scope; selected description paragraphs. | supports | Exact candidate scope inspected: D1/D2 families cannot individually ground the mixed PSII core; broad L/M includes homologous bacterial reaction-center subunits. Phycobiliprotein alpha/beta family also includes core proteins; linker domain/superfamily/family candidates do not establish exact identity of the mixed rod/rod-cap/rod-core cohort. These are candidate inspections, not universal family-absence proof. |
| micro-psii-agent-IPR005868 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005868/; Native InterPro metadata accession/name/type and explanatory domain/family scope; selected description paragraphs. | supports | Exact candidate scope inspected: D1/D2 families cannot individually ground the mixed PSII core; broad L/M includes homologous bacterial reaction-center subunits. Phycobiliprotein alpha/beta family also includes core proteins; linker domain/superfamily/family candidates do not establish exact identity of the mixed rod/rod-cap/rod-core cohort. These are candidate inspections, not universal family-absence proof. |
| micro-psii-agent-IPR000484 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000484/; Native InterPro metadata accession/name/type and explanatory domain/family scope; selected description paragraphs. | supports | Exact candidate scope inspected: D1/D2 families cannot individually ground the mixed PSII core; broad L/M includes homologous bacterial reaction-center subunits. Phycobiliprotein alpha/beta family also includes core proteins; linker domain/superfamily/family candidates do not establish exact identity of the mixed rod/rod-cap/rod-core cohort. These are candidate inspections, not universal family-absence proof. |
| micro-rod-agent-IPR012128 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR012128/; Native InterPro metadata accession/name/type and explanatory domain/family scope; selected description paragraphs. | supports | Exact candidate scope inspected: D1/D2 families cannot individually ground the mixed PSII core; broad L/M includes homologous bacterial reaction-center subunits. Phycobiliprotein alpha/beta family also includes core proteins; linker domain/superfamily/family candidates do not establish exact identity of the mixed rod/rod-cap/rod-core cohort. These are candidate inspections, not universal family-absence proof. |
| micro-rod-agent-IPR001297 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001297/; Native InterPro metadata accession/name/type and explanatory domain/family scope; selected description paragraphs. | supports | Exact candidate scope inspected: D1/D2 families cannot individually ground the mixed PSII core; broad L/M includes homologous bacterial reaction-center subunits. Phycobiliprotein alpha/beta family also includes core proteins; linker domain/superfamily/family candidates do not establish exact identity of the mixed rod/rod-cap/rod-core cohort. These are candidate inspections, not universal family-absence proof. |
| micro-rod-agent-IPR038255 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR038255/; Native InterPro metadata accession/name/type and explanatory domain/family scope; selected description paragraphs. | supports | Exact candidate scope inspected: D1/D2 families cannot individually ground the mixed PSII core; broad L/M includes homologous bacterial reaction-center subunits. Phycobiliprotein alpha/beta family also includes core proteins; linker domain/superfamily/family candidates do not establish exact identity of the mixed rod/rod-cap/rod-core cohort. These are candidate inspections, not universal family-absence proof. |
| micro-rod-agent-IPR016470 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016470/; Native InterPro metadata accession/name/type and explanatory domain/family scope; selected description paragraphs. | supports | Exact candidate scope inspected: D1/D2 families cannot individually ground the mixed PSII core; broad L/M includes homologous bacterial reaction-center subunits. Phycobiliprotein alpha/beta family also includes core proteins; linker domain/superfamily/family candidates do not establish exact identity of the mixed rod/rod-cap/rod-core cohort. These are candidate inspections, not universal family-absence proof. |
| micro-rod-agent-kawakami2022-jats | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9205905/fullTextXML; PMC9205905 JATS: Introduction, Sec3 subunit composition, Sec7 PC-rod structure, Sec8 possible energy transfer, Sec10 preparation, Sec17 MS, Figures6–8 captions; source text, not raw cryo-EM data or figure pixels. | supports | NIES-2134 rods were dissociated from PBS at reduced phosphate and reconstructed at 4.2 Å. CpcA/B, bound bilins and CpcC/D/G linker architecture support grouped rod constituents and broad function. CpcG2 identity was tentative in heterogeneous CpcG rods; precise energy routes/tuning are structural interpretations with prior spectroscopy, not time-resolved proof. The paper does not establish Rupite JX360_02095=cpcC. |
| micro-rod-agent-A0ABT0C7V5 | https://rest.uniprot.org/uniprotkb/A0ABT0C7V5.json; Native UniProt accession/status, protein name, genes/ORF tokens, taxon, sequence length, evidence tier and family/domain cross-references. | supports | A0ABT0C7V5: Phycocyanin subunit alpha; UniProtKB unreviewed (TrEMBL); taxon 2813851, 162 aa. Identity/predicted annotation scope only. This entry is not used to infer cross-strain experimental localization or to nominate a replacement cpcC accession. |
| micro-rod-agent-A0ABT0C7V6 | https://rest.uniprot.org/uniprotkb/A0ABT0C7V6.json; Native UniProt accession/status, protein name, genes/ORF tokens, taxon, sequence length, evidence tier and family/domain cross-references. | supports | A0ABT0C7V6: Phycocyanin subunit beta; UniProtKB unreviewed (TrEMBL); taxon 2813851, 172 aa. Identity/predicted annotation scope only. This entry is not used to infer cross-strain experimental localization or to nominate a replacement cpcC accession. |
| micro-rod-agent-A0ABT0C7V3 | https://rest.uniprot.org/uniprotkb/A0ABT0C7V3.json; Native UniProt accession/status, protein name, genes/ORF tokens, taxon, sequence length, evidence tier and family/domain cross-references. | supports | A0ABT0C7V3: Phycobilisome rod-core linker polypeptide; UniProtKB unreviewed (TrEMBL); taxon 2813851, 241 aa. Identity/predicted annotation scope only. This entry is not used to infer cross-strain experimental localization or to nominate a replacement cpcC accession. |
| micro-rod-agent-A0ABT0C7D6 | https://rest.uniprot.org/uniprotkb/A0ABT0C7D6.json; Native UniProt accession/status, protein name, genes/ORF tokens, taxon, sequence length, evidence tier and family/domain cross-references. | supports | A0ABT0C7D6: Phycobilisome rod-core linker polypeptide; UniProtKB unreviewed (TrEMBL); taxon 2813851, 172 aa. Identity/predicted annotation scope only. No cpcC token is present; generic rod-core linker annotation does not establish the role-level cpcC mapping. |
| micro-rod-agent-A0ABT0C9G9 | https://rest.uniprot.org/uniprotkb/A0ABT0C9G9.json; Native UniProt accession/status, protein name, genes/ORF tokens, taxon, sequence length, evidence tier and family/domain cross-references. | supports | A0ABT0C9G9: Phycobilisome rod-core linker polypeptide; UniProtKB unreviewed (TrEMBL); taxon 2813851, 285 aa. Identity/predicted annotation scope only. This entry is not used to infer cross-strain experimental localization or to nominate a replacement cpcC accession. |
| micro-rod-agent-P50034 | https://rest.uniprot.org/uniprotkb/P50034.json; Native UniProt accession/status, protein name, genes/ORF tokens, taxon, sequence length, evidence tier and family/domain cross-references. | supports | P50034: Phycobilisome 32.1 kDa linker polypeptide, phycocyanin-associated, rod; UniProtKB reviewed (Swiss-Prot); taxon 197221, 287 aa. Identity/predicted annotation scope only. This entry is not used to infer cross-strain experimental localization or to nominate a replacement cpcC accession. |
| micro-rod-new-A0ABT0CFU3 | https://rest.uniprot.org/uniprotkb/A0ABT0CFU3.json; Native UniProt accession/status, protein name, genes/ORF tokens, taxon, sequence length, evidence tier and family/domain cross-references. | supports | A0ABT0CFU3: CpcD phycobilisome linker protein; UniProtKB unreviewed (TrEMBL); taxon 2813851, 159 aa. Identity/predicted annotation scope only. The explicit submitted CpcD protein name supports the new predicted example; JX360_17400 remains an ORF token, not an experimental localization or unique ortholog claim. |
| micro-rod-agent-MCJ2541704.1-genpept | https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=MCJ2541704.1&amp;db=protein&amp;report=genpept&amp;retmode=text; NCBI GenPept definition, organism/strain, Protein product and CDS locus_tag/inference qualifiers. | supports | JX360_02095 is a predicted generic phycobilisome rod-core linker; this source does not establish cpcC. |
| micro-rod-agent-pdb-7veb-entity4 | https://data.rcsb.org/rest/v1/core/polymer_entity/7VEB/4; RCSB 7VEB entity4 native polymer sequence length and entity_src_nat/rcsb_entity_source_organism. | context_only | The CpcC model entity has 287 residues and a BP-1 source/model-sequence taxon annotation, distinct from the paper’s NIES-2134 sample and Rupite example. This scope mismatch cannot establish an exact Rupite locus mapping. |
| micro-rod-agent-rupite-linkers | https://rest.uniprot.org/uniprotkb/search?query=taxonomy_id%3A2813851%20AND%20%28protein_name%3Alinker%20OR%20gene_exact%3AcpcC%20OR%20gene_exact%3AcpcG%20OR%20gene_exact%3AcpcD%29&amp;format=json&amp;size=500; Native complete seven-hit response, accession/gene ORF/protein names, status, lengths and family cross-references; no next-page link. | supports | Multiple predicted Rupite linker candidates exist, including two submitted CpcD proteins. No accession is selected as cpcC from length or generic domain architecture. |
| micro-rod-new-genpept | https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=MCJ2544653.1&amp;db=protein&amp;report=genpept&amp;retmode=text; MCJ2544653.1 definition and Protein product; CDS locus_tag JX360_17400, PGAP provenance and automated homology inference. | supports | New CpcD example matches the source product annotation, exact ORF and Rupite taxon; annotation is computational, not measured rod localization. |
| micro-rod-new-IPR008213 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR008213/; Native InterPro entry name/type, member-domain scope and description; bibliographic list not used as primary evidence. | supports | CpcD-like domain occurs across CpcD, the C terminus of CpcC, ApcC and FNR; domain presence alone is not exact orthology. New example support instead includes its explicit source protein product. |
| micro-psii-prep-chang2015-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1038/cr.2015.59; Exact DOI/title/authors/PMID and abstract. | supports | Primary paper identity verified; the full primary text is separately inspected. |
| micro-psii-prep-chang2015-pmc-html | https://pmc.ncbi.nlm.nih.gov/articles/PMC4456626/; PMC4456626: Abstract; Introduction; overall-structure Results; Fig1 and5 captions; energy-transfer Discussion; purification, negative-stain EM, reconstruction, immunoblot and immunogold Methods. Extraction paragraphs18,21–24,27–31,48–51,53–56,59,61–65,67–68,77,79. | supports | Anabaena/Nostoc PCC7120 purified PBS preparations contain selected PSII-associated particles. D1/D2 immunoblot and D1 immunogold support PSII identity. PBS-only21Å and PBS–PSII34Å reconstructions differ; French pressure,2%TritonX100 and negative staining preclude calling this an intact live-cell or atomic catalytic experiment. PsbO/PsaA nondetection is preparation-specific. |
| micro-psii-prep-perez2024-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1146/annurev-cellbio-120823-022747; Europe PMC exact DOI metadata and abstract only. | context_only | The secondary review discusses thylakoid structural diversity and molecular organization; its current abstract alone is not exact body-level support for the individual electron-carrier sentence. |
| micro-publisher | https://www.annualreviews.org/content/journals/10.1146/annurev-cellbio-120823-022747; Fresh native publisher request returned HTTP403 challenge body; this snapshot is access evidence, not scientific article text. | context_only | The attempted native Annual Reviews route did not yield the cited secondary body. |
| micro-perez-publisher-browser | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2351/adversary-microtubule/perez/publisher-browser.json; Fresh browser-tool capture of publisher abstract/metadata or fulltext-route access error; captured tool output, not native publisher HTML. | supports | Only abstract/metadata and full-text loading placeholder were recovered; body route failed. Do not carry the historical body-excerpt access claim forward as a fresh read. |
| micro-perez-body-browser-unavailable | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2351/adversary-microtubule/perez/body-browser-unavailable.json; Fresh browser-tool capture of publisher abstract/metadata or fulltext-route access error; captured tool output, not native publisher HTML. | supports | Only abstract/metadata and full-text loading placeholder were recovered; body route failed. Do not carry the historical body-excerpt access claim forward as a fresh read. |
| micro-adapter-catalogue | https://imodulondb.org/api/datasets; Entire official datasets catalogue: organism/dataset keys. | context_only | Twenty organisms and28datasets include s_elongatus/elprecise300. This is a relevant cyanobacterial context for the broad Cyanobacteriota distribution, not direct canonical Thermostichus/Nostoc or red-algal coverage. |
| micro-adapter-client-js | https://imodulondb.org/assets/index-3_RVHvkS.js; Official frontend source endpoint definitions for datasets/meta, genes and gene/module membership; no generated biological summaries used. | context_only | API route discovery only; not scientific evidence. |
| micro-meta | https://imodulondb.org/api/datasets/s_elongatus/elprecise300/meta; s_elongatus/elprecise300 official metadata fields organism, strain, publication URL and dataset counts. | context_only | Covered strain PCC7942;300samples,57modules and2669genes. Source publication is DOI10.1073/pnas.2410492121. No identity transfer to Rupite/Nostoc. |
| micro-genes | https://imodulondb.org/api/genes?organism=s_elongatus&amp;dataset=elprecise300&amp;limit=10000; Official gene-table response locally filtered on exact gene_name pattern (psb[AD]&#124;cpc[ABCDG]) followed by optional numeric suffix. | context_only | The2669-row table contains13matched loci: five psbA/D and eight cpcA/B/C/D/G. Exact matches retain locus identifiers; no functional absence or orthology claim. |
| micro-imodulons | https://imodulondb.org/api/datasets/s_elongatus/elprecise300/imodulons; Official57-row module list locally filtered on case-insensitive photo/light/pigment/psb/cpc in metadata; selected1PSII,6RpaB,38Photosystems for detailed inspection. | context_only | Named modules are leads only. The selected modules’ actual members and thresholds were subsequently inspected; no structural membership is inferred from names. |
| micro-gene-Synpcc7942_0424 | https://imodulondb.org/api/genes/Synpcc7942_0424/imodulons?organism=s_elongatus&amp;dataset=elprecise300; Exact locus query in s_elongatus/elprecise300; all57module rows, thresholds, weights and in_imodulon flags. | context_only | Bounded computational context for Synpcc7942_0424; positive memberships: none at this dataset threshold. Nonmembership is not biological absence. |
| micro-gene-Synpcc7942_0655 | https://imodulondb.org/api/genes/Synpcc7942_0655/imodulons?organism=s_elongatus&amp;dataset=elprecise300; Exact locus query in s_elongatus/elprecise300; all57module rows, thresholds, weights and in_imodulon flags. | context_only | Bounded computational context for Synpcc7942_0655; positive memberships: 38:Photosystems. Nonmembership is not biological absence. |
| micro-gene-Synpcc7942_0893 | https://imodulondb.org/api/genes/Synpcc7942_0893/imodulons?organism=s_elongatus&amp;dataset=elprecise300; Exact locus query in s_elongatus/elprecise300; all57module rows, thresholds, weights and in_imodulon flags. | context_only | Bounded computational context for Synpcc7942_0893; positive memberships: 6:RpaB, 38:Photosystems. Nonmembership is not biological absence. |
| micro-gene-Synpcc7942_1047 | https://imodulondb.org/api/genes/Synpcc7942_1047/imodulons?organism=s_elongatus&amp;dataset=elprecise300; Exact locus query in s_elongatus/elprecise300; all57module rows, thresholds, weights and in_imodulon flags. | context_only | Bounded computational context for Synpcc7942_1047; positive memberships: 6:RpaB, 38:Photosystems. Nonmembership is not biological absence. |
| micro-gene-Synpcc7942_1048 | https://imodulondb.org/api/genes/Synpcc7942_1048/imodulons?organism=s_elongatus&amp;dataset=elprecise300; Exact locus query in s_elongatus/elprecise300; all57module rows, thresholds, weights and in_imodulon flags. | context_only | Bounded computational context for Synpcc7942_1048; positive memberships: 6:RpaB, 38:Photosystems. Nonmembership is not biological absence. |
| micro-gene-Synpcc7942_1049 | https://imodulondb.org/api/genes/Synpcc7942_1049/imodulons?organism=s_elongatus&amp;dataset=elprecise300; Exact locus query in s_elongatus/elprecise300; all57module rows, thresholds, weights and in_imodulon flags. | context_only | Bounded computational context for Synpcc7942_1049; positive memberships: 6:RpaB, 38:Photosystems. Nonmembership is not biological absence. |
| micro-gene-Synpcc7942_1050 | https://imodulondb.org/api/genes/Synpcc7942_1050/imodulons?organism=s_elongatus&amp;dataset=elprecise300; Exact locus query in s_elongatus/elprecise300; all57module rows, thresholds, weights and in_imodulon flags. | context_only | Bounded computational context for Synpcc7942_1050; positive memberships: 6:RpaB, 38:Photosystems. Nonmembership is not biological absence. |
| micro-gene-Synpcc7942_1051 | https://imodulondb.org/api/genes/Synpcc7942_1051/imodulons?organism=s_elongatus&amp;dataset=elprecise300; Exact locus query in s_elongatus/elprecise300; all57module rows, thresholds, weights and in_imodulon flags. | context_only | Bounded computational context for Synpcc7942_1051; positive memberships: 6:RpaB, 38:Photosystems. Nonmembership is not biological absence. |
| micro-gene-Synpcc7942_1052 | https://imodulondb.org/api/genes/Synpcc7942_1052/imodulons?organism=s_elongatus&amp;dataset=elprecise300; Exact locus query in s_elongatus/elprecise300; all57module rows, thresholds, weights and in_imodulon flags. | context_only | Bounded computational context for Synpcc7942_1052; positive memberships: 6:RpaB, 38:Photosystems. Nonmembership is not biological absence. |
| micro-gene-Synpcc7942_1053 | https://imodulondb.org/api/genes/Synpcc7942_1053/imodulons?organism=s_elongatus&amp;dataset=elprecise300; Exact locus query in s_elongatus/elprecise300; all57module rows, thresholds, weights and in_imodulon flags. | context_only | Bounded computational context for Synpcc7942_1053; positive memberships: 6:RpaB, 38:Photosystems. Nonmembership is not biological absence. |
| micro-gene-Synpcc7942_1389 | https://imodulondb.org/api/genes/Synpcc7942_1389/imodulons?organism=s_elongatus&amp;dataset=elprecise300; Exact locus query in s_elongatus/elprecise300; all57module rows, thresholds, weights and in_imodulon flags. | context_only | Bounded computational context for Synpcc7942_1389; positive memberships: 6:RpaB. Nonmembership is not biological absence. |
| micro-gene-Synpcc7942_1637 | https://imodulondb.org/api/genes/Synpcc7942_1637/imodulons?organism=s_elongatus&amp;dataset=elprecise300; Exact locus query in s_elongatus/elprecise300; all57module rows, thresholds, weights and in_imodulon flags. | context_only | Bounded computational context for Synpcc7942_1637; positive memberships: 6:RpaB, 38:Photosystems. Nonmembership is not biological absence. |
| micro-gene-Synpcc7942_2030 | https://imodulondb.org/api/genes/Synpcc7942_2030/imodulons?organism=s_elongatus&amp;dataset=elprecise300; Exact locus query in s_elongatus/elprecise300; all57module rows, thresholds, weights and in_imodulon flags. | context_only | Bounded computational context for Synpcc7942_2030; positive memberships: 6:RpaB, 38:Photosystems. Nonmembership is not biological absence. |
| micro-module-1 | https://imodulondb.org/api/imodulons/s_elongatus/elprecise300/1; Exact official module metadata or all=true gene-weight table; inspect in_imodulon=true rows and the selected psb/cpc loci; exclude AI summary fields. | context_only | Module1 PSII: declared21members and21true rows among2669returned gene-weight rows, threshold0.068537145; regulator field is null. Selected psb/cpc members: none. Module1includes other PSII-associated genes but does not contain the selected psbA/D loci. Computational expression context does not validate direct regulation, orthology, structural composition or causal mechanism. |
| micro-module-1-genes | https://imodulondb.org/api/imodulons/s_elongatus/elprecise300/1/genes?all=true; Exact official module metadata or all=true gene-weight table; inspect in_imodulon=true rows and the selected psb/cpc loci; exclude AI summary fields. | context_only | Module1 PSII: declared21members and21true rows among2669returned gene-weight rows, threshold0.068537145; regulator field is null. Selected psb/cpc members: none. Module1includes other PSII-associated genes but does not contain the selected psbA/D loci. Computational expression context does not validate direct regulation, orthology, structural composition or causal mechanism. |
| micro-module-6 | https://imodulondb.org/api/imodulons/s_elongatus/elprecise300/6; Exact official module metadata or all=true gene-weight table; inspect in_imodulon=true rows and the selected psb/cpc loci; exclude AI summary fields. | context_only | Module6 RpaB: declared77members and77true rows among2669returned gene-weight rows, threshold0.048868289; regulator field is null. Selected psb/cpc members: psbA3, cpcB1, cpcA1, cpcC1, cpcC2, cpcD, cpcB2, cpcA2, psbA2, psbD2, cpcG. Module1includes other PSII-associated genes but does not contain the selected psbA/D loci. Computational expression context does not validate direct regulation, orthology, structural composition or causal mechanism. |
| micro-module-6-genes | https://imodulondb.org/api/imodulons/s_elongatus/elprecise300/6/genes?all=true; Exact official module metadata or all=true gene-weight table; inspect in_imodulon=true rows and the selected psb/cpc loci; exclude AI summary fields. | context_only | Module6 RpaB: declared77members and77true rows among2669returned gene-weight rows, threshold0.048868289; regulator field is null. Selected psb/cpc members: psbA3, cpcB1, cpcA1, cpcC1, cpcC2, cpcD, cpcB2, cpcA2, psbA2, psbD2, cpcG. Module1includes other PSII-associated genes but does not contain the selected psbA/D loci. Computational expression context does not validate direct regulation, orthology, structural composition or causal mechanism. |
| micro-module-38 | https://imodulondb.org/api/imodulons/s_elongatus/elprecise300/38; Exact official module metadata or all=true gene-weight table; inspect in_imodulon=true rows and the selected psb/cpc loci; exclude AI summary fields. | context_only | Module38 Photosystems: declared44members and44true rows among2669returned gene-weight rows, threshold0.063088206; regulator field is null. Selected psb/cpc members: psbD1, psbA3, cpcB1, cpcA1, cpcC1, cpcC2, cpcD, cpcB2, cpcA2, psbD2, cpcG. Module1includes other PSII-associated genes but does not contain the selected psbA/D loci. Computational expression context does not validate direct regulation, orthology, structural composition or causal mechanism. |
| micro-module-38-genes | https://imodulondb.org/api/imodulons/s_elongatus/elprecise300/38/genes?all=true; Exact official module metadata or all=true gene-weight table; inspect in_imodulon=true rows and the selected psb/cpc loci; exclude AI summary fields. | context_only | Module38 Photosystems: declared44members and44true rows among2669returned gene-weight rows, threshold0.063088206; regulator field is null. Selected psb/cpc members: psbD1, psbA3, cpcB1, cpcA1, cpcC1, cpcC2, cpcD, cpcB2, cpcA2, psbD2, cpcG. Module1includes other PSII-associated genes but does not contain the selected psbA/D loci. Computational expression context does not validate direct regulation, orthology, structural composition or causal mechanism. |
| micro-adapter-publication | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1073/pnas.2410492121; Europe PMC exact DOI metadata and abstract only for the dataset publication. | context_only | The study uses independent-component analysis of300RNA-seq datasets from Synechococcus elongatus PCC7942 to derive57modules. Abstract scope only; full study methods and data were not reanalyzed. |
| micro-native-photosystem-ii-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2351/photosystem-ii-uniprot-verify-receipt.json; Actual root-executed current-head command receipt and adjacent stdout; exit0; stdout SHA verified. | supports | Command .venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/photosystem_ii.yaml --verify passed. Native exact accession/status/token/taxon checks; not free-text orthology validation. |
| micro-native-photosystem-ii-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2351/photosystem-ii-uniprot-causal-receipt.json; Actual root-executed current-head command receipt and adjacent stdout; exit0; stdout SHA verified. | supports | Command .venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/photosystem_ii.yaml --causal-graphs passed. Current graph coverage is 1COVERED/1total, with zero dangling refs and no uncovered symbol category. |
| micro-native-phycobilisome-rod-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2351/phycobilisome-rod-uniprot-verify-receipt.json; Actual root-executed current-head command receipt and adjacent stdout; exit0; stdout SHA verified. | supports | Command .venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/phycobilisome_rod.yaml --verify passed. Native exact accession/status/token/taxon checks; not free-text orthology validation. |
| micro-native-phycobilisome-rod-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2351/phycobilisome-rod-uniprot-causal-receipt.json; Actual root-executed current-head command receipt and adjacent stdout; exit0; stdout SHA verified. | supports | Command .venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/phycobilisome_rod.yaml --causal-graphs passed. Current graph coverage is 2COVERED/2total, with zero dangling refs and no uncovered symbol category. |
| micro-original-checks | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2351/adversary-microtubule/original-checks.json; Actual independent native validate/render and frozen-input comparisons for all3 originals. | supports | All3native validations exit0; renderer --content matches each paired Markdown. Original frozen hashes match historical source trees; current matches are true, with rod alone changed. |
| septin-s2351-rc-prep-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009767,GO:0042717; Native issuing-authority response: exact identifier, label, taxon and returned annotation scope. | supports | Exact current record identifiers and bounded authority annotations checked. Database attribution is distinguished from independent experimental inspection. |
| septin-s2351-rc-prep-tax-1063 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1063; Native issuing-authority response: exact identifier, label, taxon and returned annotation scope. | supports | Exact current record identifiers and bounded authority annotations checked. Database attribution is distinguished from independent experimental inspection. |
| septin-s2351-rc-prep-bahatyrova2004-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1038/nature02823; Europe PMC exact DOI primary abstract and bibliographic metadata only. | supports | Source identity and RC-LH1/LH2 organization checked; native PDF supplies the separate, explicitly bounded body evidence. |
| septin-s2351-rc-prep-bahatyrova2004-whiterose-pdf | https://eprints.whiterose.ac.uk/id/eprint/102/1/huntercn1.pdf; Primary paper abstract, Introduction, claim-bearing Results pp1059–1061, Figure1–3 captions and membrane-preparation/AFM Methods; not figure pixels or raw AFM. | supports | NCIB8253 membrane patches show RC-LH1 arrays and LH2 clusters. RC L/M/H and LH1 constituents are described, but PufX itself was not resolved. Isolated detergent-treated, mica-adsorbed membranes do not constitute intact-cell dynamics. Potential interdimer energy transfer is interpretation, not a new measured transfer rate. |
| septin-s2351-rc-prep-comayras2005-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1074/jbc.M412088200; Europe PMC exact DOI primary abstract and bibliographic metadata only. | supports | Comayras/Jungas/Lavergne compare isolated monomers/dimers and chromatophores by excitation and photoreducible-quinone assays. Their limited-domain interpretation does not license universal long-range interdimer transfer. |
| septin-s2351-v0-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000220,GO:0005774,GO:0016471,GO:0033179; Native issuing-authority response: exact identifier, label, taxon and returned annotation scope. | supports | Exact current record identifiers and bounded authority annotations checked. Database attribution is distinguished from independent experimental inspection. |
| septin-s2351-v0-agent-tax-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Native issuing-authority response: exact identifier, label, taxon and returned annotation scope. | supports | Exact current record identifiers and bounded authority annotations checked. Database attribution is distinguished from independent experimental inspection. |
| septin-s2351-v0-agent-doi-MMBR_70_1_177-191_2006 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1128/MMBR.70.1.177-191.2006; Europe PMC exact DOI secondary-review abstract and author/title metadata. | supports | Kane2006 is review-tier synthesis of the S. cerevisiae V-ATPase, not an independent primary experiment. |
| septin-s2351-v0-agent-kane2006-legacy-html | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1393255/; Secondary review: Structure and Mechanism, V-ATPase Assembly, vacuolar/Golgi isoform targeting and reversible-dissociation passages, plus relevant captions; not every regulation section or cited primary experiment. | supports | Kane identifies yeast V0 a/c/c-prime/c-double-prime/d/e and V1 A–H. Rotation couples ATP hydrolysis to transport in the intact enzyme; dissociated-sector inhibition and isoform localization bound the record. Historical stalk/c-ring models are not imported as current fixed stoichiometry. |
| septin-s2351-v1-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000220,GO:0000221,GO:0016471,GO:0033180,GO:0046961; Native issuing-authority response: exact identifier, label, taxon and returned annotation scope. | supports | Exact current record identifiers and bounded authority annotations checked. Database attribution is distinguished from independent experimental inspection. |
| septin-s2351-v1-agent-doi-nrm2272 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1038/nrm2272; Europe PMC exact DOI secondary-review abstract and author/title metadata only. | supports | Forgac2007 source identity and broad ATP-driven proton-pump context checked. Native publisher request returned authorization HTML, so no fresh complete body or Key Points inspection is claimed. |
| septin-s2351-v1-agent-ro-native | https://raw.githubusercontent.com/oborel/obo-relations/master/ro.json; Native issuing-authority response: exact identifier, label, taxon and returned annotation scope. | supports | Exact current record identifiers and bounded authority annotations checked. Database attribution is distinguished from independent experimental inspection. |
| septin-s2351-outer-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009279,GO:0016020; Native issuing-authority response: exact identifier, label, taxon and returned annotation scope. | supports | Exact current record identifiers and bounded authority annotations checked. Database attribution is distinguished from independent experimental inspection. |
| septin-s2351-outer-agent-sl-0040 | https://rest.uniprot.org/locations/SL-0040.json; Native issuing-authority response: exact identifier, label, taxon and returned annotation scope. | supports | Exact current record identifiers and bounded authority annotations checked. Database attribution is distinguished from independent experimental inspection. |
| septin-s2351-outer-agent-chebi-16412 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/16412/; Native issuing-authority response: exact identifier, label, taxon and returned annotation scope. | supports | Exact current record identifiers and bounded authority annotations checked. Database attribution is distinguished from independent experimental inspection. |
| septin-s2351-outer-agent-tax-2 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2; Native issuing-authority response: exact identifier, label, taxon and returned annotation scope. | supports | Exact current record identifiers and bounded authority annotations checked. Database attribution is distinguished from independent experimental inspection. |
| septin-s2351-outer-agent-tax-562 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562; Native issuing-authority response: exact identifier, label, taxon and returned annotation scope. | supports | Exact current record identifiers and bounded authority annotations checked. Database attribution is distinguished from independent experimental inspection. |
| septin-s2351-outer-agent-tax-83333 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333; Native issuing-authority response: exact identifier, label, taxon and returned annotation scope. | supports | Exact current record identifiers and bounded authority annotations checked. Database attribution is distinguished from independent experimental inspection. |
| septin-s2351-outer-agent-P0A910 | https://rest.uniprot.org/uniprotkb/P0A910.json; Native issuing-authority response: exact identifier, label, taxon and returned annotation scope. | supports | Exact current record identifiers and bounded authority annotations checked. Database attribution is distinguished from independent experimental inspection. |
| septin-s2351-outer-agent-query-ompA | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AompA%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29; Exact request URL and returned identity/metadata/abstract results. | supports | Bounded query with no universal absence claim; metadata and abstracts are not full scientific-body reads. |
| septin-s2351-outer-agent-P06996 | https://rest.uniprot.org/uniprotkb/P06996.json; Native issuing-authority response: exact identifier, label, taxon and returned annotation scope. | supports | Exact current record identifiers and bounded authority annotations checked. Database attribution is distinguished from independent experimental inspection. |
| septin-s2351-outer-agent-query-ompC | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AompC%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29; Exact request URL and returned identity/metadata/abstract results. | supports | Bounded query with no universal absence claim; metadata and abstracts are not full scientific-body reads. |
| septin-s2351-outer-agent-P02931 | https://rest.uniprot.org/uniprotkb/P02931.json; Native issuing-authority response: exact identifier, label, taxon and returned annotation scope. | supports | Exact current record identifiers and bounded authority annotations checked. Database attribution is distinguished from independent experimental inspection. |
| septin-s2351-outer-agent-query-ompF | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AompF%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29; Exact request URL and returned identity/metadata/abstract results. | supports | Bounded query with no universal absence claim; metadata and abstracts are not full scientific-body reads. |
| septin-s2351-outer-agent-P0A940 | https://rest.uniprot.org/uniprotkb/P0A940.json; Native issuing-authority response: exact identifier, label, taxon and returned annotation scope. | supports | Exact current record identifiers and bounded authority annotations checked. Database attribution is distinguished from independent experimental inspection. |
| septin-s2351-outer-agent-query-bamA | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AbamA%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29; Exact request URL and returned identity/metadata/abstract results. | supports | Bounded query with no universal absence claim; metadata and abstracts are not full scientific-body reads. |
| septin-s2351-outer-agent-P31554 | https://rest.uniprot.org/uniprotkb/P31554.json; Native issuing-authority response: exact identifier, label, taxon and returned annotation scope. | supports | Exact current record identifiers and bounded authority annotations checked. Database attribution is distinguished from independent experimental inspection. |
| septin-s2351-outer-agent-query-lptD | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AlptD%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29; Exact request URL and returned identity/metadata/abstract results. | supports | Bounded query with no universal absence claim; metadata and abstracts are not full scientific-body reads. |
| septin-s2351-outer-agent-P77774 | https://rest.uniprot.org/uniprotkb/P77774.json; Native issuing-authority response: exact identifier, label, taxon and returned annotation scope. | supports | Exact current record identifiers and bounded authority annotations checked. Database attribution is distinguished from independent experimental inspection. |
| septin-s2351-outer-agent-query-bamB | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AbamB%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29; Exact request URL and returned identity/metadata/abstract results. | supports | Bounded query with no universal absence claim; metadata and abstracts are not full scientific-body reads. |
| septin-s2351-outer-agent-P0A903 | https://rest.uniprot.org/uniprotkb/P0A903.json; Native issuing-authority response: exact identifier, label, taxon and returned annotation scope. | supports | Exact current record identifiers and bounded authority annotations checked. Database attribution is distinguished from independent experimental inspection. |
| septin-s2351-outer-agent-query-bamC | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AbamC%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29; Exact request URL and returned identity/metadata/abstract results. | supports | Bounded query with no universal absence claim; metadata and abstracts are not full scientific-body reads. |
| septin-s2351-outer-agent-P0AC02 | https://rest.uniprot.org/uniprotkb/P0AC02.json; Native issuing-authority response: exact identifier, label, taxon and returned annotation scope. | supports | Exact current record identifiers and bounded authority annotations checked. Database attribution is distinguished from independent experimental inspection. |
| septin-s2351-outer-agent-query-bamD | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AbamD%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29; Exact request URL and returned identity/metadata/abstract results. | supports | Bounded query with no universal absence claim; metadata and abstracts are not full scientific-body reads. |
| septin-s2351-outer-agent-matches-P0A910 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P0A910/?page_size=200; Native InterPro protein matches with metadata accession/name/type fields. | supports | OmpA, porins and BamA span distinct families and domains; no one family CURIE covers the generic beta-barrel component. Family labels are not borrowed from domain or broad superfamily entries. |
| septin-s2351-outer-agent-matches-P06996 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P06996/?page_size=200; Native InterPro protein matches with metadata accession/name/type fields. | supports | OmpA, porins and BamA span distinct families and domains; no one family CURIE covers the generic beta-barrel component. Family labels are not borrowed from domain or broad superfamily entries. |
| septin-s2351-outer-agent-matches-P02931 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P02931/?page_size=200; Native InterPro protein matches with metadata accession/name/type fields. | supports | OmpA, porins and BamA span distinct families and domains; no one family CURIE covers the generic beta-barrel component. Family labels are not borrowed from domain or broad superfamily entries. |
| septin-s2351-outer-agent-pmid-10636850 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID:10636850%20AND%20SRC:MED; Europe PMC exact PMID primary abstract and metadata only. | supports | Arora2000 refolded detergent-purified OmpA into planar bilayers and measured two conductance states. UniProt supplies the direct location-citation attribution; the abstract is not a full localization-method audit. |
| septin-s2351-outer-agent-pmid-10947984 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID:10947984%20AND%20SRC:MED; Europe PMC exact PMID primary abstract and metadata only. | supports | Belaaouaj2000 describes OmpA surface localization and neutrophil-elastase degradation; exact UniProt citation attribution was separately checked. |
| septin-s2351-outer-agent-pmid-16079137 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID:16079137%20AND%20SRC:MED; Europe PMC exact PMID primary abstract and metadata only. | supports | Stenberg2005 reports blue native PAGE, second-dimension SDS-PAGE and mass spectrometry of E. coli envelope complexes. Individual protein-result tables and full experimental-stock methods were not read; reviewed K12 accession identity is not proof of stock equivalence. |
| septin-s2351-outer-agent-pmid-23882017 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID:23882017%20AND%20SRC:MED; Europe PMC exact PMID primary abstract and metadata only. | supports | Ruhe2013 identifies BamA as the CdiA-EC93 receptor and bounds species/loop specificity. Location attribution is verified directly in UniProt; not all CDI experiments were independently reviewed. |
| septin-s2351-outer-agent-pmid-24619089 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID:24619089%20AND%20SRC:MED; Europe PMC exact PMID primary abstract and metadata only. | supports | Ni2014 reports the E. coli BamA barrel structure and mutational effects. Proposed substrate-insertion details remain proposal-tier; the current record only needs the bounded outer-membrane assembly claim. |
| septin-s2351-outer-agent-pmid-2464593 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID:2464593%20AND%20SRC:MED; Europe PMC exact PMID primary abstract and metadata only. | supports | Gehring/Nikaido1989 reports purification of K12 OmpC/OmpF/PhoE heterotrimers and expression-dependent distribution; this corroborates source identity, not a universal three-protein membrane inventory. |
| septin-s2351-outer-agent-doi-cshperspect_a000414 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1101/cshperspect.a000414; Exact request URL and returned identity/metadata/abstract results. | supports | Bounded query with no universal absence claim; metadata and abstracts are not full scientific-body reads. |
| septin-s2351-outer-agent-doi-jbc_R117_802512 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1074/jbc.R117.802512; Exact request URL and returned identity/metadata/abstract results. | supports | Bounded query with no universal absence claim; metadata and abstracts are not full scientific-body reads. |
| septin-s2351-outer-agent-doi-annurev-biochem-061408-144611 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1146/annurev-biochem-061408-144611; Exact request URL and returned identity/metadata/abstract results. | supports | Bounded query with no universal absence claim; metadata and abstracts are not full scientific-body reads. |
| septin-s2351-outer-agent-doi-MMBR_67_4_593-656_2003 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1128/MMBR.67.4.593-656.2003; Exact request URL and returned identity/metadata/abstract results. | supports | Bounded query with no universal absence claim; metadata and abstracts are not full scientific-body reads. |
| septin-s2351-outer-agent-silhavy2010-legacy-html | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2857177/; Secondary review: Gram-negative outer membrane composition/assembly and Corynebacterineae sections. | supports | Canonical Gram-negative LPS/phospholipid asymmetry, beta-barrel proteins and porin-mediated permeability are supported. The review separately describes a mycolic outer membrane with different composition and no obvious BAM homologs; canonical graphs must retain their Gram-negative scope. |
| septin-s2351-outer-agent-sperandeo2017-legacy-html | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5672026/; Secondary review: LPS structure/essentiality exceptions, LPS transport and LptB2CFG/LptA/LptDE sections, corresponding captions; underlying studies not independently reproduced. | supports | Seven E. coli Lpt proteins form a transenvelope machine; extraction follows MsbA flipping, and LptDE delivers LPS to the outer membrane. Canonical transport has noncanonical exceptions. LPS-deficient Neisseria, Moraxella and Acinetobacter examples support retaining CONDITIONAL rather than universal LPS indispensability. |
| septin-s2351-outer-agent-hagan2011-pdf | https://prokaryotics.com/wp-content/uploads/2017/02/Hagan-et-al-2011.pdf; Secondary review PDF: overview/Figure1 caption, BAM composition, folding/insertion and BamB efficiency passages, pp191–202; no figure pixels or underlying primary raw data. | supports | The five-protein E. coli BAM complex folds and inserts beta-barrel proteins. A/B/C/D xrefs in the record are representative rather than a full inventory; absence of BamE from those links is not a claim of its biological absence. Activity, efficiency and membership do not prove universal assembly necessity. |
| septin-s2351-outer-agent-nikaido2003-browser1 | https://pmc.ncbi.nlm.nih.gov/articles/PMC309051; Genuine freshly retrieved PMC secondary-review body: Protein Channels, porin selectivity/regulation, ordered LPS layer and lipid-bilayer permeability passages. | supports | Porins admit hydrophilic solutes selectively; ordered LPS slows lipid-phase entry. This supports the explicitly reduced-influx meaning of excludes, not absolute impermeability. Historical failure to fetch this body no longer describes this current successful retrieval. |
| septin-s2351-current-adapter-catalogue | https://imodulondb.org/api/datasets; Entire official /api/datasets response: 20 organism objects and 28 dataset keys. | supports | No Cereibacter/Rhodobacter or Saccharomyces dataset occurs in this returned catalogue. E. coli precise1k matches outer-membrane examples. This bounded catalogue result does not imply biological gene absence; unrelated Bradyrhizobium or cyanobacterial datasets are not substituted for the RC-LH1 strain. |
| septin-s2351-adapter-search-ompA | https://imodulondb.org/api/search?organism=e_coli&amp;dataset=precise1k&amp;query=ompA&amp;limit=50; Exact request URL and returned identity/metadata/abstract results. | supports | Bounded query with no universal absence claim; metadata and abstracts are not full scientific-body reads. |
| septin-s2351-adapter-search-ompC | https://imodulondb.org/api/search?organism=e_coli&amp;dataset=precise1k&amp;query=ompC&amp;limit=50; Exact request URL and returned identity/metadata/abstract results. | supports | Bounded query with no universal absence claim; metadata and abstracts are not full scientific-body reads. |
| septin-s2351-adapter-search-ompF | https://imodulondb.org/api/search?organism=e_coli&amp;dataset=precise1k&amp;query=ompF&amp;limit=50; Exact request URL and returned identity/metadata/abstract results. | supports | Bounded query with no universal absence claim; metadata and abstracts are not full scientific-body reads. |
| septin-s2351-adapter-search-bamA | https://imodulondb.org/api/search?organism=e_coli&amp;dataset=precise1k&amp;query=bamA&amp;limit=50; Exact request URL and returned identity/metadata/abstract results. | supports | Bounded query with no universal absence claim; metadata and abstracts are not full scientific-body reads. |
| septin-s2351-adapter-search-bamB | https://imodulondb.org/api/search?organism=e_coli&amp;dataset=precise1k&amp;query=bamB&amp;limit=50; Exact request URL and returned identity/metadata/abstract results. | supports | Bounded query with no universal absence claim; metadata and abstracts are not full scientific-body reads. |
| septin-s2351-adapter-search-bamC | https://imodulondb.org/api/search?organism=e_coli&amp;dataset=precise1k&amp;query=bamC&amp;limit=50; Exact request URL and returned identity/metadata/abstract results. | supports | Bounded query with no universal absence claim; metadata and abstracts are not full scientific-body reads. |
| septin-s2351-adapter-search-bamD | https://imodulondb.org/api/search?organism=e_coli&amp;dataset=precise1k&amp;query=bamD&amp;limit=50; Exact request URL and returned identity/metadata/abstract results. | supports | Bounded query with no universal absence claim; metadata and abstracts are not full scientific-body reads. |
| septin-s2351-adapter-search-lptD | https://imodulondb.org/api/search?organism=e_coli&amp;dataset=precise1k&amp;query=lptD&amp;limit=50; Exact request URL and returned identity/metadata/abstract results. | supports | Bounded query with no universal absence claim; metadata and abstracts are not full scientific-body reads. |
| septin-s2351-outer-agent-matches-P0A940-retry | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P0A940/?page_size=200; Native InterPro protein matches with metadata accession/name/type fields. | supports | OmpA, porins and BamA span distinct families and domains; no one family CURIE covers the generic beta-barrel component. Family labels are not borrowed from domain or broad superfamily entries. |
| septin-s2351-adapter-gene-ompA | https://imodulondb.org/api/genes/e_coli/precise1k/b0957; Exact E. coli precise1k gene identity or complete 201-item returned gene-module array; is_in_imodulon, gene_weight and threshold fields. | supports | Eight exact gene identities agree with their UniProt/locus mappings. Only ompF has positive memberships in the inspected arrays: UC-3 k86, Nitrogen k88, Lrp k25 and SoxS k22. Seven empty positive sets mean only no thresholded membership in this one returned dataset. |
| septin-s2351-adapter-modules-ompA | https://imodulondb.org/api/genes/e_coli/precise1k/b0957/imodulons; Exact E. coli precise1k gene identity or complete 201-item returned gene-module array; is_in_imodulon, gene_weight and threshold fields. | supports | Eight exact gene identities agree with their UniProt/locus mappings. Only ompF has positive memberships in the inspected arrays: UC-3 k86, Nitrogen k88, Lrp k25 and SoxS k22. Seven empty positive sets mean only no thresholded membership in this one returned dataset. |
| septin-s2351-adapter-gene-ompC | https://imodulondb.org/api/genes/e_coli/precise1k/b2215; Exact E. coli precise1k gene identity or complete 201-item returned gene-module array; is_in_imodulon, gene_weight and threshold fields. | supports | Eight exact gene identities agree with their UniProt/locus mappings. Only ompF has positive memberships in the inspected arrays: UC-3 k86, Nitrogen k88, Lrp k25 and SoxS k22. Seven empty positive sets mean only no thresholded membership in this one returned dataset. |
| septin-s2351-adapter-modules-ompC | https://imodulondb.org/api/genes/e_coli/precise1k/b2215/imodulons; Exact E. coli precise1k gene identity or complete 201-item returned gene-module array; is_in_imodulon, gene_weight and threshold fields. | supports | Eight exact gene identities agree with their UniProt/locus mappings. Only ompF has positive memberships in the inspected arrays: UC-3 k86, Nitrogen k88, Lrp k25 and SoxS k22. Seven empty positive sets mean only no thresholded membership in this one returned dataset. |
| septin-s2351-adapter-gene-ompF | https://imodulondb.org/api/genes/e_coli/precise1k/b0929; Exact E. coli precise1k gene identity or complete 201-item returned gene-module array; is_in_imodulon, gene_weight and threshold fields. | supports | Eight exact gene identities agree with their UniProt/locus mappings. Only ompF has positive memberships in the inspected arrays: UC-3 k86, Nitrogen k88, Lrp k25 and SoxS k22. Seven empty positive sets mean only no thresholded membership in this one returned dataset. |
| septin-s2351-adapter-modules-ompF | https://imodulondb.org/api/genes/e_coli/precise1k/b0929/imodulons; Exact E. coli precise1k gene identity or complete 201-item returned gene-module array; is_in_imodulon, gene_weight and threshold fields. | supports | Eight exact gene identities agree with their UniProt/locus mappings. Only ompF has positive memberships in the inspected arrays: UC-3 k86, Nitrogen k88, Lrp k25 and SoxS k22. Seven empty positive sets mean only no thresholded membership in this one returned dataset. |
| septin-s2351-adapter-gene-bamA | https://imodulondb.org/api/genes/e_coli/precise1k/b0177; Exact E. coli precise1k gene identity or complete 201-item returned gene-module array; is_in_imodulon, gene_weight and threshold fields. | supports | Eight exact gene identities agree with their UniProt/locus mappings. Only ompF has positive memberships in the inspected arrays: UC-3 k86, Nitrogen k88, Lrp k25 and SoxS k22. Seven empty positive sets mean only no thresholded membership in this one returned dataset. |
| septin-s2351-adapter-modules-bamA | https://imodulondb.org/api/genes/e_coli/precise1k/b0177/imodulons; Exact E. coli precise1k gene identity or complete 201-item returned gene-module array; is_in_imodulon, gene_weight and threshold fields. | supports | Eight exact gene identities agree with their UniProt/locus mappings. Only ompF has positive memberships in the inspected arrays: UC-3 k86, Nitrogen k88, Lrp k25 and SoxS k22. Seven empty positive sets mean only no thresholded membership in this one returned dataset. |
| septin-s2351-adapter-gene-bamB | https://imodulondb.org/api/genes/e_coli/precise1k/b2512; Exact E. coli precise1k gene identity or complete 201-item returned gene-module array; is_in_imodulon, gene_weight and threshold fields. | supports | Eight exact gene identities agree with their UniProt/locus mappings. Only ompF has positive memberships in the inspected arrays: UC-3 k86, Nitrogen k88, Lrp k25 and SoxS k22. Seven empty positive sets mean only no thresholded membership in this one returned dataset. |
| septin-s2351-adapter-modules-bamB | https://imodulondb.org/api/genes/e_coli/precise1k/b2512/imodulons; Exact E. coli precise1k gene identity or complete 201-item returned gene-module array; is_in_imodulon, gene_weight and threshold fields. | supports | Eight exact gene identities agree with their UniProt/locus mappings. Only ompF has positive memberships in the inspected arrays: UC-3 k86, Nitrogen k88, Lrp k25 and SoxS k22. Seven empty positive sets mean only no thresholded membership in this one returned dataset. |
| septin-s2351-adapter-gene-bamC | https://imodulondb.org/api/genes/e_coli/precise1k/b2477; Exact E. coli precise1k gene identity or complete 201-item returned gene-module array; is_in_imodulon, gene_weight and threshold fields. | supports | Eight exact gene identities agree with their UniProt/locus mappings. Only ompF has positive memberships in the inspected arrays: UC-3 k86, Nitrogen k88, Lrp k25 and SoxS k22. Seven empty positive sets mean only no thresholded membership in this one returned dataset. |
| septin-s2351-adapter-modules-bamC | https://imodulondb.org/api/genes/e_coli/precise1k/b2477/imodulons; Exact E. coli precise1k gene identity or complete 201-item returned gene-module array; is_in_imodulon, gene_weight and threshold fields. | supports | Eight exact gene identities agree with their UniProt/locus mappings. Only ompF has positive memberships in the inspected arrays: UC-3 k86, Nitrogen k88, Lrp k25 and SoxS k22. Seven empty positive sets mean only no thresholded membership in this one returned dataset. |
| septin-s2351-adapter-gene-bamD | https://imodulondb.org/api/genes/e_coli/precise1k/b2595; Exact E. coli precise1k gene identity or complete 201-item returned gene-module array; is_in_imodulon, gene_weight and threshold fields. | supports | Eight exact gene identities agree with their UniProt/locus mappings. Only ompF has positive memberships in the inspected arrays: UC-3 k86, Nitrogen k88, Lrp k25 and SoxS k22. Seven empty positive sets mean only no thresholded membership in this one returned dataset. |
| septin-s2351-adapter-modules-bamD | https://imodulondb.org/api/genes/e_coli/precise1k/b2595/imodulons; Exact E. coli precise1k gene identity or complete 201-item returned gene-module array; is_in_imodulon, gene_weight and threshold fields. | supports | Eight exact gene identities agree with their UniProt/locus mappings. Only ompF has positive memberships in the inspected arrays: UC-3 k86, Nitrogen k88, Lrp k25 and SoxS k22. Seven empty positive sets mean only no thresholded membership in this one returned dataset. |
| septin-s2351-adapter-gene-lptD | https://imodulondb.org/api/genes/e_coli/precise1k/b0054; Exact E. coli precise1k gene identity or complete 201-item returned gene-module array; is_in_imodulon, gene_weight and threshold fields. | supports | Eight exact gene identities agree with their UniProt/locus mappings. Only ompF has positive memberships in the inspected arrays: UC-3 k86, Nitrogen k88, Lrp k25 and SoxS k22. Seven empty positive sets mean only no thresholded membership in this one returned dataset. |
| septin-s2351-adapter-modules-lptD | https://imodulondb.org/api/genes/e_coli/precise1k/b0054/imodulons; Exact E. coli precise1k gene identity or complete 201-item returned gene-module array; is_in_imodulon, gene_weight and threshold fields. | supports | Eight exact gene identities agree with their UniProt/locus mappings. Only ompF has positive memberships in the inspected arrays: UC-3 k86, Nitrogen k88, Lrp k25 and SoxS k22. Seven empty positive sets mean only no thresholded membership in this one returned dataset. |
| septin-s2351-adapter-module-86 | https://imodulondb.org/api/imodulons/e_coli/precise1k/86; Native precise1k module identity, regulator, function_description, threshold and gene-membership fields. ai_summary and other generated prose excluded. | supports | Structured expression context only; module association does not establish physical membership, assembly necessity, cell viability or causal function. UC-3 is unknown; other relevant labels are Nac/nitrogen limitation, Lrp and SoxS. |
| septin-s2351-adapter-module-88 | https://imodulondb.org/api/imodulons/e_coli/precise1k/88; Native precise1k module identity, regulator, function_description, threshold and gene-membership fields. ai_summary and other generated prose excluded. | supports | Structured expression context only; module association does not establish physical membership, assembly necessity, cell viability or causal function. UC-3 is unknown; other relevant labels are Nac/nitrogen limitation, Lrp and SoxS. |
| septin-s2351-adapter-module-25 | https://imodulondb.org/api/imodulons/e_coli/precise1k/25; Native precise1k module identity, regulator, function_description, threshold and gene-membership fields. ai_summary and other generated prose excluded. | supports | Structured expression context only; module association does not establish physical membership, assembly necessity, cell viability or causal function. UC-3 is unknown; other relevant labels are Nac/nitrogen limitation, Lrp and SoxS. |
| septin-s2351-adapter-module-22 | https://imodulondb.org/api/imodulons/e_coli/precise1k/22; Native precise1k module identity, regulator, function_description, threshold and gene-membership fields. ai_summary and other generated prose excluded. | supports | Structured expression context only; module association does not establish physical membership, assembly necessity, cell viability or causal function. UC-3 is unknown; other relevant labels are Nac/nitrogen limitation, Lrp and SoxS. |
| septin-s2351-comayras-indexed-body | https://www.researchgate.net/publication/8099149_Functional_consequences_of_the_organization_of_the_photosynthetic_apparatus_in_Rhodobacter_sphaeroides_I_Quinone_domains_and_excitation_transfer_in_chromatophores_and_reaction_centerantenna_complexes; Fresh indexed coauthor-shared primary-paper rendering, returned lines0–626: abstract, figure captions, Introduction, strain/preparation Methods and beginning of spectroscopy/photoreduction methods. Remaining body/supplement not claimed read. | supports | Ga-strain monomers/dimers and chromatophores, optical excitation/quinone assays, purified-complex context and related PufX prior literature are distinguishable. No new whole-body/native download, universal interdimer transport or directly located PufX is claimed. The native URL returned403; this evidence is the browser-indexed passage. |
| septin-s2351-bounded-publication-search | https://doi.org/10.1074/jbc.M412088200; Saved browser returned search response; only exact matching Comayras source and Forgac metadata used. Unrelated returned papers were not treated as evidence. | supports | Indexed publisher result qualifies interdimer excitation as infrequent. Search finds source access routes; it does not show full-paper reading or literature absence. |
| septin-s2351-record-rc_lh1_pufx_core_complex | data/structures/energy_complex/rc_lh1_pufx_core_complex.yaml; Complete current YAML at source head3266d0f7239a80f17d74bb0d6e2b3e260000b8dc, all nodes/edges, evidence, examples and discussions. | supports | Current bytes equal original target frozen hash. Complete read-only scientific assessment; no record edit. |
| septin-s2351-record-vacuolar_proton_transporting_v_type_atpase_v0_domain | data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_v0_domain.yaml; Complete current YAML at source head3266d0f7239a80f17d74bb0d6e2b3e260000b8dc, all nodes/edges, evidence, examples and discussions. | supports | Current bytes equal original target frozen hash. Complete read-only scientific assessment; no record edit. |
| septin-s2351-record-vacuolar_proton_transporting_v_type_atpase_v1_domain | data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_v1_domain.yaml; Complete current YAML at source head3266d0f7239a80f17d74bb0d6e2b3e260000b8dc, all nodes/edges, evidence, examples and discussions. | supports | Current bytes equal original target frozen hash. Complete read-only scientific assessment; no record edit. |
| septin-s2351-record-cell_outer_membrane | data/structures/envelope/cell_outer_membrane.yaml; Complete current YAML at source head3266d0f7239a80f17d74bb0d6e2b3e260000b8dc, all nodes/edges, evidence, examples and discussions. | supports | Current bytes equal original target frozen hash. Complete read-only scientific assessment; no record edit. |
| septin-s2351-policy | docs/CURATION.md; Current frozen local source; relevant components, context-link or CausalNodeTypeEnum passage. | supports | Known constituents may use source-bounded labels without guessed family IDs. Named genes/pathways require structured-source applicability assessment. |
| septin-s2351-lh2-context | data/structures/energy_complex/lh2_peripheral_light_harvesting_antenna_complex.yaml; Current frozen local source; relevant components, context-link or CausalNodeTypeEnum passage. | supports | Frozen LH2 neighbor resolves the local graph link and bounds core receiver context to C. sphaeroides; it is not independent external evidence. |
| septin-s2351-node-types | src/cellstructuremech/schema/cellstructuremech.yaml; Current frozen local source; relevant components, context-link or CausalNodeTypeEnum passage. | supports | GENE_OR_PROTEIN explicitly includes complexes; BAM/Lpt complex node types are allowed, and representative UniProt links are not full inventories. |
| septin-s2351-original-native-checks | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2351/adversary-septin/original-checks.json; Four native validate invocations, four render --content invocations and byte/hash comparisons, actual start/end timestamps. | supports | All four validate/render exits0; render bytes equal committed original Markdown and target SHA equals historical frozen SHA. Deprecation warning only. No full QC or CI executed by this subreview. |
| septin-s2351-outer-native-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2351/outer-membrane-uniprot-verify-receipt.json; Root-run native command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/envelope/cell_outer_membrane.yaml', '--verify']; independently read exact receipt and log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2351/outer-membrane-uniprot-verify.log; head 3266d0f7239a80f17d74bb0d6e2b3e260000b8dc. | supports | Exit0: all protein_examples and causal graph UniProt xrefs verify. |
| septin-s2351-outer-native-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2351/outer-membrane-uniprot-causal-receipt.json; Root-run native command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/envelope/cell_outer_membrane.yaml', '--causal-graphs']; independently read exact receipt and log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2351/outer-membrane-uniprot-causal.log; head 3266d0f7239a80f17d74bb0d6e2b3e260000b8dc. | supports | Exit0: two COVERED and two UNANCHORED_WITH_UNIPROT nodes; latter are Lpt/BAM representative links. No dangling reference. This classification is not a demand to invent a full complex inventory. |
| check-qc | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2351/qc.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| check-labels | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2351/labels.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | 4232 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| check-trait-links | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2351/trait-links.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Native TraitMech link check passed. |
| check-vendored | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2351/vendored.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Pinned governed files match; native vendored check passed. |
| check-curies | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2351/curies.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| focused | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2351/focused-results.json; All twenty actual target schema/strict command outputs | supports | Ten schema and ten strict commands returned exit zero. |
| supplemental-pmid | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2351/pmid-chunks-receipt.json; Complete native-report PMID set checked with unchanged resolver in batches of at most fifty | supports | 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers remain unverified. |
| historical-adapter-runner-availability | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical runner invocation receipt, cross-checked against exact stdout/stderr hashes; reread during PR2351 synthesis | context_only | Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS PermissionError reading the configured runner pyvenv.cfg. This is a retained historical availability observation, not a fresh attempt or a scientific validation failure. Native policy permits inspected source-catalogue fallback. |

## Limits And Additional Notes

- MCR, respiratory complex I and complex II independent subreview: All three targets retain the historical explicitly unknown assembly-necessity assessment. Qualified passes cover inspected claims, not proof of every ESSENTIAL assertion.
- MCR, respiratory complex I and complex II independent subreview: Ermler1997 was freshly inspected through browser-extracted primary transcription. Direct native Gale retrieval yielded an invalid-parameter HTML page and the alternate PDF returned404; neither is represented as a paper body. Figure pixels, Table1 and raw coordinates were not independently analyzed. Hashes of browser evidence bind serialized tool output.
- MCR, respiratory complex I and complex II independent subreview: Wrede2013 claim-bearing Methods/Results and captions were inspected; immunolabeling concerns assembled MCR antigen and culture-dependent localization. It is not separate experimental localization of each subunit.
- MCR, respiratory complex I and complex II independent subreview: Baradaran2013 JATS Introduction/Results/Methods and associated captions were read, plus supplementary Tables3-4 text. Other supplemental alignments/figure pixels and raw maps were not reanalyzed. Proton-channel paths and predicted waters remain model-level interpretation.
- MCR, respiratory complex I and complex II independent subreview: Yankovskaya2003 is freshly abstract-only plus native1NEK deposition/UniProt evidence; no renewed full-body access is claimed. Stenberg2005 fresh indexed Methods passages are limited, full-page open returned500 and native DOI retrieval was a redirect page. Its detailed Sdh result subsection was not independently reread. Daley2005 remains abstract-only plus native annotation attribution.
- MCR, respiratory complex I and complex II independent subreview: Four initial InterPro429 responses were followed by successful bounded retries; both receipts retained. Candidate searches are bounded to exact current protein matches and inspected named definitions. IPR050573 unchecked LLM description and iModulonDB AI summaries are excluded from biological evidence.
- MCR, respiratory complex I and complex II independent subreview: The historical iModulonDB runner limitation is not a new execution result. Current public API fallback checked complete organism catalogue, one matching MG1655 dataset, exact four genes, returned module weights/thresholds and three module annotation/member tables. Other E.coli datasets, expression conditions and activity matrices were not reassessed. A below-threshold gene does not refute physical membership.
- MCR, respiratory complex I and complex II independent subreview: Category-review YAML/Markdown were requested and frozen by root before use. No tracked image or neighboring record was used by this reviewer. Root owns current full-corpus QC and CI; historical counts in original reviews are not represented as fresh outcomes.
- Photosystem II, phycobilisome rod and bacterial PSII independent subreview: PSII: Umena/Kamiya/Kawakami assess purified preparations and selected claim-bearing text/captions. No raw diffraction data or figure-pixel reanalysis; PsbY loss, model-sequence borrowing and halide substitutions remain preparation-specific. Assembly necessity of each metal/pigment class was not independently established.
- Photosystem II, phycobilisome rod and bacterial PSII independent subreview: Phycobilisome rod: NIES-2134 dissociated cryo-EM rods are not Rupite localization experiments. CpcG2 assignment and precise energy-transfer paths remain tentative. Red-algal context is comparative; no exact cpcC replacement is established by length/domain similarity.
- Photosystem II, phycobilisome rod and bacterial PSII independent subreview: Phycobilisome rod: new A0ABT0CFU3 is a predicted CpcD identity example with an ORF token. Another submitted CpcD paralog occurs in the bounded search; the record does not assert uniqueness. Native2/2COVERED does not settle the cpcC free-text mapping.
- Photosystem II, phycobilisome rod and bacterial PSII independent subreview: Bacterial PSII: Chang2015 used French pressure,2%TritonX100, gradients and negative staining. D1/D2 and limited association are supported; oxygen-evolution activity and intact native accessory composition are not newly established. Figures1/5 captions were read, not pixels or every supplementary table.
- Photosystem II, phycobilisome rod and bacterial PSII independent subreview: Bacterial PSII: Perez2024 fresh access is abstract/metadata only; native publisher returned403 and browser fulltext route failed. Old browser-indexed body-excerpt access remains historical rather than being represented as freshly recovered. Exact GO independently supports current broad physiology.
- Photosystem II, phycobilisome rod and bacterial PSII independent subreview: All3 targets: official iModulonDB fallback is computational PCC7942 context for the broader cyanobacterial scope, not direct Thermostichus/Nostoc/red-algal coverage, expression-to-structure proof, direct regulation or universal absence. No new native adapter runner execution occurred in this subreview; root retains actual historical availability receipt.
- Photosystem II, phycobilisome rod and bacterial PSII independent subreview: All3 targets: ontology/family inspection is bounded to named exact candidates; no exhaustive universal absence claims. Primary bodies/source authorities were freshly fetched; no old HTTP result is restamped as fresh. Root owns corpus/CI gates and GitHub issue deduplication/mutations.
- Photosystem II, phycobilisome rod and bacterial PSII independent subreview: Workflow inventory: conf/record_review.yaml was first read only as route/rubric guidance before being added to inspect. Root then froze it in the49-input inventory; exact bytes were reread and workflow applicability reassessed at2026-11-03T05:16:19Z. This timing correction is disclosed; there is no claim that this one config was captured before its initial route-only read.
- RC-LH1-PufX, V0, V1 and outer membrane independent subreview: Bahatyrova native PDF body/captions and Methods were read in the stated scope; no figure pixels, AFM maps, raw spectroscopy or supplements were reanalyzed. PufX was not directly located; source-reported structure is distinguished from inferred physiological transfer.
- RC-LH1-PufX, V0, V1 and outer membrane independent subreview: Comayras fresh native retrieval returned403. Fresh indexed coauthor rendering provides abstract, figure captions, Introduction and Methods through the start of photoreduction; complete later Results, supplemental models and raw data were not read. Original discontinuous-body limitation remains inherited, not proof of current whole-body access.
- RC-LH1-PufX, V0, V1 and outer membrane independent subreview: Kane, Forgac, Silhavy, Sperandeo, Hagan and Nikaido are secondary reviews. Specific native claim-bearing bodies were read except Forgac, where authorization HTML was excluded and exact abstract/metadata used. Historical Forgac Key Points access is attributed to the original review. Underlying primary experiments are not all independently reviewed.
- RC-LH1-PufX, V0, V1 and outer membrane independent subreview: Outer-membrane individual primary studies were freshly checked at abstract/metadata plus direct UniProt attribution. Full protein-specific proteomic tables, stock-level Methods and mechanistic raw data were not inspected. Reviewed K12 protein identity does not assert every experiment used K12.
- RC-LH1-PufX, V0, V1 and outer membrane independent subreview: The original outer-membrane collective beta-barrel ESSENTIAL assertion remains an explicit unknown assessment: no collective-depletion/assembly experiment was inspected. Representative complex xrefs are partial, and expression modules do not establish assembly necessity or structural membership.
- RC-LH1-PufX, V0, V1 and outer membrane independent subreview: V0/V1 source-supported known labels do not imply verified family CURIEs, exact modern ring/stalk copy numbers, assembly factors as constituents, universal isoform placement or necessity. Sparse sector-level records are not falsely counted as named-gene adapter omissions.
- RC-LH1-PufX, V0, V1 and outer membrane independent subreview: Official dataset coverage is bounded to the returned20 organisms/28 dataset keys. No exact Rhodobacter/Cereibacter or yeast match; the E. coli work covers one precise1k dataset, eight exact queries and selected relevant module metadata. False substring hits and AI-generated module prose are excluded. Empty positive sets are not gene/structure absence.
- RC-LH1-PufX, V0, V1 and outer membrane independent subreview: Historical runner failure at2026-11-03T00:49Z remains root-owned prior receipt, not a newly invoked runner here. The source APIs provide fallback evidence. One native InterPro BamA request initially returned429; later bounded request succeeded. Original native validate/render checks all passed; no full corpus QC/CI or GitHub mutation performed by this subreview.
- RC-LH1-PufX, V0, V1 and outer membrane independent subreview: Original global-gate coverage totals are historical subreview limitations, not current final CI/QC counts. Root owns refreshed corpus gates and current native outer-membrane protein/graph verifier receipts.
- Historical observations remain immutable; their old checks are not represented as current-head execution.
- The adapter runner was not rerun after the canary established OS access failure. Catalogue-based coverage is assessed directly; fresh and reused responses retain actual access timestamps.
- Native label checks include 923 no-adapter skips. Native identifier checks include 909 PMID transport failures and 254 skipped identifiers; bounded supplemental checks independently resolve the 909 PMIDs.
- Scientific record-curation findings stay in separate issues; no record is edited by this review PR.
- Final trusted-base post-save review-check, exact-head independent acceptance, final-head CI and merge-group CI occur after saving this immutable observation and are not represented here as already completed.
- All ten original YAML/Markdown pairs are preserved unchanged. Current main was merged normally and pushed without force.
- One explicit issue-bearing ten-record cohort follows the repository persistence policy. Supported records are assessed within that cohort without fabricated findings.
- Bundle issues #2541 (four stale reviews) and #2542 (eight structured-source coverage defects) are addressed here. Five scientific findings remain in #2543, #2544, #2545, #2546 and #2547; existing validator #2514 remains open. MCR #2432 was already closed before this review and is not a fix made by this PR.
- Source commit 3266d0f7239a80f17d74bb0d6e2b3e260000b8dc is retained by tag review-base/pr2351-current-record-followup-20261103.
- CLAUDE.md is an alias of AGENTS.md; canonical regular AGENTS.md bytes are frozen.
- Every source-access and check limitation is attributed to its independent subreview. Fresh fetches, cached response re-reading, abstract-only evidence and full-body passages retain distinct scopes.
- Seven original bundles omit structured-source applicability, and complex I contains an unsupported exemption rationale. MCR omits a formal check rather than containing that complex-I check. Sparse V0 and V1 sector records are excluded from this molecular-coverage defect.
- Returned AI-generated module prose and unchecked InterPro generated descriptions are excluded from scientific support. Bounded transcriptomic context is not structural membership, physical interaction or necessity evidence; below-threshold results are not biological absence.
- Used scientific local context was frozen before assessment, including the prior MCR category-review pair, phycobilisome core and LH2 neighbor, and native UniProt verifier source. Final inventory also added conf/record_review.yaml, previously read only for workflow routes; workflow applicability was rechecked against its frozen bytes before the final verdict.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T051803Z-pr2351-current-record-followup
kind: batch
repository: CultureBotAI/CellStructureMech
title: 'PR 2351: current-input review of ten records and adversarial follow-up'
started_at: '2026-11-03T05:05:44.598270Z'
finished_at: '2026-11-03T05:18:03Z'
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
summary: 'Current-input reassessment of all ten records in PR2351. Four stale records
  are substantively refreshed: MCR graph grounding propagation, the predicted/unreviewed
  phycobilisome-rod CpcD example, the respiratory complex I peripheral-arm contribution
  and complex II constituent edges. Five records retain five minor scientific curation
  findings; five receive qualified supported assessments. The historical MCR category-review
  finding is resolved on current main and remains linked to already-closed #2432,
  without claiming this PR repaired the record. The successor corrects structured-source
  coverage for eight original bundles. No scientific record is edited.'
source:
  git_revision: 3266d0f7239a80f17d74bb0d6e2b3e260000b8dc
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
  - path: AGENTS.md
    sha256: ef74a980161b55cd24f1851e38d1c0b2e004fcf8837f1bc70da1874e4e8380f0
    role: context
  - path: conf/record_review.yaml
    sha256: d3334a12b8a616a7638f1195748085d2b543fba7df67ad4ff8fcc0ac18f2d3ee
    role: context
  - path: data/structures/energy_complex/lh2_peripheral_light_harvesting_antenna_complex.yaml
    sha256: 4bb84c48c2bb27f1a8dded06f479771b494070977ef26e0b14f0708bc446a7ce
    role: context
  - path: data/structures/energy_complex/methyl_coenzyme_m_reductase_complex.yaml
    sha256: 369ad320d4bc19c72a79fb14037b46c5e12f6eddaa64bd0bb04572e9a8ea685e
    role: target
  - path: data/structures/energy_complex/photosystem_ii.yaml
    sha256: fc05496451f76ed16643edb2ca590803fd07569abfe432111e31314375687a16
    role: target
  - path: data/structures/energy_complex/phycobilisome_core.yaml
    sha256: 34cca2a846f5b2b84b95c6c2db929370814b4e2898eee052f3e2cbfecafde554
    role: context
  - path: data/structures/energy_complex/phycobilisome_rod.yaml
    sha256: f610a707b8f8fea3edfd28574b996a315eaf1e2d245de7efce9edf96b49943d1
    role: target
  - path: data/structures/energy_complex/plasma_membrane_derived_thylakoid_photosystem_ii.yaml
    sha256: 7629a2480ce3d823e87431d0c26be93c45101095021fd60087301f5f1d9a58ef
    role: target
  - path: data/structures/energy_complex/rc_lh1_pufx_core_complex.yaml
    sha256: 0a3a6fcfe54b7a355fd2903992f521fb2fc293ce984d4ede356dbc8460071824
    role: target
  - path: data/structures/energy_complex/respiratory_chain_complex_i.yaml
    sha256: 0d0f4b5c3346e25dbbd3595d959c03d40dc9943e3e6055dcca3746fd4bf67540
    role: target
  - path: data/structures/energy_complex/respiratory_chain_complex_ii_succinate_dehydrogenase.yaml
    sha256: 4e6914fa2c29221809c1a172d98aa541c5adc01bc5090cc8c0eb55b56a3d463d
    role: target
  - path: data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_v0_domain.yaml
    sha256: b76891f7e50630db7612669a25299babae68eb2e480724de8209094cc1953c48
    role: target
  - path: data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_v1_domain.yaml
    sha256: fabfca0b7f5ff5ee1340a6874918e4505c242d7939734a2e9ef8f3df5ebeeb22
    role: target
  - path: data/structures/envelope/cell_outer_membrane.yaml
    sha256: 6a21a7409a3e93aa290cbff61f4734629b927f04a33c469e6166ef1b24673fab
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
  - path: reviews/structured/20261021T091345Z-methyl-coenzyme-m-reductase-complex-audit/review.md
    sha256: 5c4770870ac673bed4466aa60101ca07630d681cebf149841e5f529d04f19fc1
    role: context
  - path: reviews/structured/20261021T091345Z-methyl-coenzyme-m-reductase-complex-audit/review.yaml
    sha256: 10c87a197c78b725f0a92b31d638ef50bca24fe5837e7a59c3660804cae4b089
    role: context
  - path: reviews/structured/20261021T091346Z-photosystem-ii-audit/review.md
    sha256: 5228cc933a2f99c819119f3ebb187e5d7d8e4e514c2200091eefa2dae3f51e00
    role: context
  - path: reviews/structured/20261021T091346Z-photosystem-ii-audit/review.yaml
    sha256: 5138fd0d9d80523573027ab48105acfc6915554a6ecacb5bf8aa6e8cfccc17b2
    role: context
  - path: reviews/structured/20261021T091347Z-phycobilisome-rod-audit/review.md
    sha256: 436b874f6801775974cf392d2bcdf2ace745579d59a32c5375283cdd8f42e3a5
    role: context
  - path: reviews/structured/20261021T091347Z-phycobilisome-rod-audit/review.yaml
    sha256: 5de19cc2aeb828652a3d90d22d578645985e8259bd6206abb59e62ecdf11daf9
    role: context
  - path: reviews/structured/20261021T091348Z-plasma-membrane-derived-thylakoid-photosystem-ii-audit/review.md
    sha256: a41447312ceee8f6eb0df3c198c23451c9216cdc3da3a596e6bfcf7b794a02ba
    role: context
  - path: reviews/structured/20261021T091348Z-plasma-membrane-derived-thylakoid-photosystem-ii-audit/review.yaml
    sha256: c60ea9147f742d25275b0dff673fc6957fc7497b55ee1862482c20358b2333b4
    role: context
  - path: reviews/structured/20261021T091349Z-rc-lh1-pufx-core-complex-audit/review.md
    sha256: 5a2346b707482efd29741b8f4c2ba7d00e342331c2519000ccbcd0f298603e44
    role: context
  - path: reviews/structured/20261021T091349Z-rc-lh1-pufx-core-complex-audit/review.yaml
    sha256: 8dbe30a3e38992ffce97d3e9ed303b413f769b7be2820b6f3052b338a647d1de
    role: context
  - path: reviews/structured/20261021T091350Z-respiratory-chain-complex-i-audit/review.md
    sha256: 0c2ed12d8381bb81402864486e538d9ab12d8984c6c28815b30acc0cac4e2c51
    role: context
  - path: reviews/structured/20261021T091350Z-respiratory-chain-complex-i-audit/review.yaml
    sha256: 40d426bae2756cbf27bea5822fa3e323eebe2d00fce3e53716ad33584aa52ae8
    role: context
  - path: reviews/structured/20261021T091351Z-respiratory-chain-complex-ii-succinate-dehydrogenase-audit/review.md
    sha256: 663eede0c12c28dca025e4d490bb5ab806bce5866dd43e5ee4d8dc3bdddac977
    role: context
  - path: reviews/structured/20261021T091351Z-respiratory-chain-complex-ii-succinate-dehydrogenase-audit/review.yaml
    sha256: 7d846c8c936360c7e05a670be52a0c1bc49a444e40d4c21f9ce044bba8c49d1a
    role: context
  - path: reviews/structured/20261021T091352Z-vacuolar-proton-transporting-v-type-atpase-v0-domain-audit/review.md
    sha256: b4f95d79384bbc9c3bc68287445de702fa28b29b28fcc9d2a34a0a2258b5ba20
    role: context
  - path: reviews/structured/20261021T091352Z-vacuolar-proton-transporting-v-type-atpase-v0-domain-audit/review.yaml
    sha256: 0ffb74ceefe0d2d5041d8745977f28dec10202cfc753d844a5e7c8237e33827c
    role: context
  - path: reviews/structured/20261021T091354Z-vacuolar-proton-transporting-v-type-atpase-v1-domain-audit/review.md
    sha256: fcbf726829b407e61a811fcce1368e703d5d8d1fb26897156d7c4c7dc0b2e03b
    role: context
  - path: reviews/structured/20261021T091354Z-vacuolar-proton-transporting-v-type-atpase-v1-domain-audit/review.yaml
    sha256: 886587cea44f281a30b9b8ac553b4d0fed42cfa51901e86d602d1bd0c3ca2460
    role: context
  - path: reviews/structured/20261021T091355Z-cell-outer-membrane-audit/review.md
    sha256: f66fee2f9719eca599c65ce0b2239a4fa25415ef6dc4934d785d2137cc4942d7
    role: context
  - path: reviews/structured/20261021T091355Z-cell-outer-membrane-audit/review.yaml
    sha256: 6238f43a75d18940317c72df2a026d44c21593e6d713a79475454e57b26b8d21
    role: context
  - path: reviews/structured/20261025T071006Z-energy-complex-category-review/review.md
    sha256: aec9a24175bb27b39b83d0c00ff41688ea40f32925c9da06638a2a612fedeb29
    role: context
  - path: reviews/structured/20261025T071006Z-energy-complex-category-review/review.yaml
    sha256: e711d5f5b710f0bf33facd08863a8d1e206b2d0a185906a359acbd886a728146
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
- target_id: GO:0044674
  path: data/structures/energy_complex/methyl_coenzyme_m_reductase_complex.yaml
  label: methyl coenzyme M reductase complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/methyl_coenzyme_m_reductase_complex.yaml
    role: maintained scientific record
- target_id: GO:0009523
  path: data/structures/energy_complex/photosystem_ii.yaml
  label: photosystem II
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/photosystem_ii.yaml
    role: maintained scientific record
- target_id: cellstructuremech:phycobilisome_rod
  path: data/structures/energy_complex/phycobilisome_rod.yaml
  label: phycobilisome rod
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/phycobilisome_rod.yaml
    role: maintained scientific record
- target_id: GO:0030096
  path: data/structures/energy_complex/plasma_membrane_derived_thylakoid_photosystem_ii.yaml
  label: plasma membrane-derived thylakoid photosystem II
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/plasma_membrane_derived_thylakoid_photosystem_ii.yaml
    role: maintained scientific record
- target_id: cellstructuremech:rc_lh1_pufx_core_complex
  path: data/structures/energy_complex/rc_lh1_pufx_core_complex.yaml
  label: RC-LH1-PufX core complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/rc_lh1_pufx_core_complex.yaml
    role: maintained scientific record
- target_id: GO:0045271
  path: data/structures/energy_complex/respiratory_chain_complex_i.yaml
  label: respiratory chain complex I
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/respiratory_chain_complex_i.yaml
    role: maintained scientific record
- target_id: GO:0045273
  path: data/structures/energy_complex/respiratory_chain_complex_ii_succinate_dehydrogenase.yaml
  label: respiratory chain complex II (succinate dehydrogenase)
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/respiratory_chain_complex_ii_succinate_dehydrogenase.yaml
    role: maintained scientific record
- target_id: GO:0000220
  path: data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_v0_domain.yaml
  label: vacuolar proton-transporting V-type ATPase, V0 domain
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_v0_domain.yaml
    role: maintained scientific record
- target_id: GO:0000221
  path: data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_v1_domain.yaml
  label: vacuolar proton-transporting V-type ATPase, V1 domain
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_v1_domain.yaml
    role: maintained scientific record
- target_id: GO:0009279
  path: data/structures/envelope/cell_outer_membrane.yaml
  label: cell outer membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/envelope/cell_outer_membrane.yaml
    role: maintained scientific record
scope:
  description: Exact ten-record PR cohort reassessed against current main f9abc3a0c7d0727083ab824899e576a8d7db2938.
    Changed inputs are substantively reassessed. Scientific records remain unchanged.
  selection: Complete cohort of ten maintained records reviewed in original PR head
    bdebfd046d61b5dd82d56001ee1753841ccf912f.
  coverage: full
  population_size: 10
  reviewed_target_ids:
  - GO:0044674
  - GO:0009523
  - cellstructuremech:phycobilisome_rod
  - GO:0030096
  - cellstructuremech:rc_lh1_pufx_core_complex
  - GO:0045271
  - GO:0045273
  - GO:0000220
  - GO:0000221
  - GO:0009279
checks:
- check_id: qc
  name: Full native QC
  status: passed
  required: true
  target_ids:
  - GO:0044674
  - GO:0009523
  - cellstructuremech:phycobilisome_rod
  - GO:0030096
  - cellstructuremech:rc_lh1_pufx_core_complex
  - GO:0045271
  - GO:0045273
  - GO:0000220
  - GO:0000221
  - GO:0009279
  command: just qc
  exit_code: 0
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  scope_note: Actual local execution at main-merge head 3266d0f7239a80f17d74bb0d6e2b3e260000b8dc.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-qc
- check_id: labels
  name: Native label correspondence
  status: passed
  required: true
  target_ids:
  - GO:0044674
  - GO:0009523
  - cellstructuremech:phycobilisome_rod
  - GO:0030096
  - cellstructuremech:rc_lh1_pufx_core_complex
  - GO:0045271
  - GO:0045273
  - GO:0000220
  - GO:0000221
  - GO:0009279
  command: just validate-products
  exit_code: 0
  summary: 4232 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  scope_note: Actual local execution at main-merge head 3266d0f7239a80f17d74bb0d6e2b3e260000b8dc.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-labels
- check_id: trait-links
  name: TraitMech references
  status: passed
  required: true
  target_ids:
  - GO:0044674
  - GO:0009523
  - cellstructuremech:phycobilisome_rod
  - GO:0030096
  - cellstructuremech:rc_lh1_pufx_core_complex
  - GO:0045271
  - GO:0045273
  - GO:0000220
  - GO:0000221
  - GO:0009279
  command: just check-trait-links --check
  exit_code: 0
  summary: Native TraitMech link check passed.
  scope_note: Actual local execution at main-merge head 3266d0f7239a80f17d74bb0d6e2b3e260000b8dc.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-trait-links
- check_id: vendored
  name: Pinned governed files
  status: passed
  required: true
  target_ids:
  - GO:0044674
  - GO:0009523
  - cellstructuremech:phycobilisome_rod
  - GO:0030096
  - cellstructuremech:rc_lh1_pufx_core_complex
  - GO:0045271
  - GO:0045273
  - GO:0000220
  - GO:0000221
  - GO:0009279
  command: just vendored-check
  exit_code: 0
  summary: Pinned governed files match; native vendored check passed.
  scope_note: Actual local execution at main-merge head 3266d0f7239a80f17d74bb0d6e2b3e260000b8dc.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-vendored
- check_id: curies
  name: Native identifier resolver
  status: passed
  required: true
  target_ids:
  - GO:0044674
  - GO:0009523
  - cellstructuremech:phycobilisome_rod
  - GO:0030096
  - cellstructuremech:rc_lh1_pufx_core_complex
  - GO:0045271
  - GO:0045273
  - GO:0000220
  - GO:0000221
  - GO:0009279
  command: just check-curies-strict
  exit_code: 0
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  scope_note: Actual local execution at main-merge head 3266d0f7239a80f17d74bb0d6e2b3e260000b8dc.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-curies
- check_id: focused-0
  name: validate GO:0044674
  status: passed
  required: true
  target_ids:
  - GO:0044674
  command: just validate data/structures/energy_complex/methyl_coenzyme_m_reductase_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-1
  name: validate-strict GO:0044674
  status: passed
  required: true
  target_ids:
  - GO:0044674
  command: just validate-strict data/structures/energy_complex/methyl_coenzyme_m_reductase_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-2
  name: validate GO:0009523
  status: passed
  required: true
  target_ids:
  - GO:0009523
  command: just validate data/structures/energy_complex/photosystem_ii.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-3
  name: validate-strict GO:0009523
  status: passed
  required: true
  target_ids:
  - GO:0009523
  command: just validate-strict data/structures/energy_complex/photosystem_ii.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-4
  name: validate cellstructuremech:phycobilisome_rod
  status: passed
  required: true
  target_ids:
  - cellstructuremech:phycobilisome_rod
  command: just validate data/structures/energy_complex/phycobilisome_rod.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-5
  name: validate-strict cellstructuremech:phycobilisome_rod
  status: passed
  required: true
  target_ids:
  - cellstructuremech:phycobilisome_rod
  command: just validate-strict data/structures/energy_complex/phycobilisome_rod.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-6
  name: validate GO:0030096
  status: passed
  required: true
  target_ids:
  - GO:0030096
  command: just validate data/structures/energy_complex/plasma_membrane_derived_thylakoid_photosystem_ii.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-7
  name: validate-strict GO:0030096
  status: passed
  required: true
  target_ids:
  - GO:0030096
  command: just validate-strict data/structures/energy_complex/plasma_membrane_derived_thylakoid_photosystem_ii.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-8
  name: validate cellstructuremech:rc_lh1_pufx_core_complex
  status: passed
  required: true
  target_ids:
  - cellstructuremech:rc_lh1_pufx_core_complex
  command: just validate data/structures/energy_complex/rc_lh1_pufx_core_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-9
  name: validate-strict cellstructuremech:rc_lh1_pufx_core_complex
  status: passed
  required: true
  target_ids:
  - cellstructuremech:rc_lh1_pufx_core_complex
  command: just validate-strict data/structures/energy_complex/rc_lh1_pufx_core_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-10
  name: validate GO:0045271
  status: passed
  required: true
  target_ids:
  - GO:0045271
  command: just validate data/structures/energy_complex/respiratory_chain_complex_i.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-11
  name: validate-strict GO:0045271
  status: passed
  required: true
  target_ids:
  - GO:0045271
  command: just validate-strict data/structures/energy_complex/respiratory_chain_complex_i.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-12
  name: validate GO:0045273
  status: passed
  required: true
  target_ids:
  - GO:0045273
  command: just validate data/structures/energy_complex/respiratory_chain_complex_ii_succinate_dehydrogenase.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-13
  name: validate-strict GO:0045273
  status: passed
  required: true
  target_ids:
  - GO:0045273
  command: just validate-strict data/structures/energy_complex/respiratory_chain_complex_ii_succinate_dehydrogenase.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-14
  name: validate GO:0000220
  status: passed
  required: true
  target_ids:
  - GO:0000220
  command: just validate data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_v0_domain.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-15
  name: validate-strict GO:0000220
  status: passed
  required: true
  target_ids:
  - GO:0000220
  command: just validate-strict data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_v0_domain.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-16
  name: validate GO:0000221
  status: passed
  required: true
  target_ids:
  - GO:0000221
  command: just validate data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_v1_domain.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-17
  name: validate-strict GO:0000221
  status: passed
  required: true
  target_ids:
  - GO:0000221
  command: just validate-strict data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_v1_domain.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-18
  name: validate GO:0009279
  status: passed
  required: true
  target_ids:
  - GO:0009279
  command: just validate data/structures/envelope/cell_outer_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-19
  name: validate-strict GO:0009279
  status: passed
  required: true
  target_ids:
  - GO:0009279
  command: just validate-strict data/structures/envelope/cell_outer_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: supplemental-pmid
  name: Supplemental bounded PMID authority checks
  status: passed
  required: true
  target_ids:
  - GO:0044674
  - GO:0009523
  - cellstructuremech:phycobilisome_rod
  - GO:0030096
  - cellstructuremech:rc_lh1_pufx_core_complex
  - GO:0045271
  - GO:0045273
  - GO:0000220
  - GO:0000221
  - GO:0009279
  command: .venv/bin/python /private/tmp/cellstructure-batches-2346-2397-20261103/check_pmid_chunks.py
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2351
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
  - GO:0044674
  - GO:0009523
  - cellstructuremech:phycobilisome_rod
  - GO:0030096
  - cellstructuremech:rc_lh1_pufx_core_complex
  - GO:0045271
  - GO:0045273
  - GO:0000220
  - GO:0000221
  - GO:0009279
  summary: Applicability was assessed for all ten records using the complete official
    catalogue and bounded source API fallback. Matched E. coli datasets provide gene
    and module context for complex II and outer membrane; covered Synechococcus elongatus
    provides bounded cyanobacterial photosynthesis context without being equated to
    the exact Thermostichus or Nostoc strains. No matching catalogue datasets exist
    for the named Methanothermobacter, Thermus, Cereibacter/Rhodobacter or yeast examples.
    V0/V1 are excluded from the molecular-coverage defect. Exact dataset, query, limits
    and threshold scope remain in the evidence. Expression observations do not establish
    structural membership, physical interaction, necessity or mechanism. Historical
    runner unavailability remains separate; no successful or fresh runner invocation
    is claimed.
  evidence_ids:
  - plaque-adapter-datasets
  - plaque-adapter-frontend
  - plaque-adapter-meta
  - plaque-adapter-search-sdhA
  - plaque-adapter-search-sdhB
  - plaque-adapter-search-sdhC
  - plaque-adapter-search-sdhD
  - plaque-adapter-gene-modules-sdhC
  - plaque-adapter-gene-modules-sdhA
  - plaque-adapter-gene-modules-sdhB
  - plaque-adapter-gene-modules-sdhD
  - plaque-adapter-summary-1
  - plaque-adapter-members-1
  - plaque-adapter-summary-10
  - plaque-adapter-members-10
  - plaque-adapter-summary-14
  - plaque-adapter-members-14
  - micro-adapter-catalogue
  - micro-adapter-client-js
  - micro-meta
  - micro-genes
  - micro-imodulons
  - micro-gene-Synpcc7942_0424
  - micro-gene-Synpcc7942_0655
  - micro-gene-Synpcc7942_0893
  - micro-gene-Synpcc7942_1047
  - micro-gene-Synpcc7942_1048
  - micro-gene-Synpcc7942_1049
  - micro-gene-Synpcc7942_1050
  - micro-gene-Synpcc7942_1051
  - micro-gene-Synpcc7942_1052
  - micro-gene-Synpcc7942_1053
  - micro-gene-Synpcc7942_1389
  - micro-gene-Synpcc7942_1637
  - micro-gene-Synpcc7942_2030
  - micro-module-1
  - micro-module-1-genes
  - micro-module-6
  - micro-module-6-genes
  - micro-module-38
  - micro-module-38-genes
  - septin-s2351-current-adapter-catalogue
  - septin-s2351-adapter-search-ompA
  - septin-s2351-adapter-search-ompC
  - septin-s2351-adapter-search-ompF
  - septin-s2351-adapter-search-bamA
  - septin-s2351-adapter-search-bamB
  - septin-s2351-adapter-search-bamC
  - septin-s2351-adapter-search-bamD
  - septin-s2351-adapter-search-lptD
  - septin-s2351-adapter-gene-ompA
  - septin-s2351-adapter-modules-ompA
  - septin-s2351-adapter-gene-ompC
  - septin-s2351-adapter-modules-ompC
  - septin-s2351-adapter-gene-ompF
  - septin-s2351-adapter-modules-ompF
  - septin-s2351-adapter-gene-bamA
  - septin-s2351-adapter-modules-bamA
  - septin-s2351-adapter-gene-bamB
  - septin-s2351-adapter-modules-bamB
  - septin-s2351-adapter-gene-bamC
  - septin-s2351-adapter-modules-bamC
  - septin-s2351-adapter-gene-bamD
  - septin-s2351-adapter-modules-bamD
  - septin-s2351-adapter-gene-lptD
  - septin-s2351-adapter-modules-lptD
  - septin-s2351-adapter-module-86
  - septin-s2351-adapter-module-88
  - septin-s2351-adapter-module-25
  - septin-s2351-adapter-module-22
- check_id: independent-scientific-review
  name: Independent claim-level source review
  status: passed
  required: true
  target_ids:
  - GO:0044674
  - GO:0009523
  - cellstructuremech:phycobilisome_rod
  - GO:0030096
  - cellstructuremech:rc_lh1_pufx_core_complex
  - GO:0045271
  - GO:0045273
  - GO:0000220
  - GO:0000221
  - GO:0009279
  summary: Three read-only reviewers covered the complete ten-record cohort, including
    changed inputs, with explicit scientific findings and source-access limits. Final
    artifact/head acceptance occurs after saving.
  evidence_ids:
  - plaque-mcr-agent-go
  - plaque-mcr-agent-tax-79929
  - plaque-mcr-agent-IPR016212
  - plaque-mcr-agent-IPR003179
  - plaque-mcr-agent-pdb-1mro
  - plaque-mcr-agent-pdb-1mro-assembly1
  - plaque-mcr-agent-pdb-1mro-entity1
  - plaque-mcr-agent-pdb-1mro-entity2
  - plaque-mcr-agent-pdb-1mro-entity3
  - plaque-mcr-agent-P11558
  - plaque-mcr-agent-P11560
  - plaque-mcr-agent-P11562
  - plaque-mcr-agent-wrede2013-jats
  - plaque-mcr-agent-epmc
  - plaque-complex-i-agent-go
  - plaque-complex-i-agent-go-arm-candidates
  - plaque-complex-i-agent-tax-274
  - plaque-complex-i-agent-tax-300852
  - plaque-complex-i-agent-epmc
  - plaque-complex-i-agent-baradaran2013-jats
  - plaque-complex-i-agent-baradaran2013-supplement-epmc
  - plaque-complex-i-agent-pdb-4HEA
  - plaque-complex-i-agent-assembly-4HEA
  - plaque-complex-i-agent-4HEA-entity-1
  - plaque-complex-i-agent-4HEA-entity-2
  - plaque-complex-i-agent-4HEA-entity-3
  - plaque-complex-i-agent-4HEA-entity-4
  - plaque-complex-i-agent-4HEA-entity-5
  - plaque-complex-i-agent-4HEA-entity-6
  - plaque-complex-i-agent-4HEA-entity-7
  - plaque-complex-i-agent-4HEA-entity-8
  - plaque-complex-i-agent-4HEA-entity-9
  - plaque-complex-i-agent-4HEA-entity-10
  - plaque-complex-i-agent-4HEA-entity-11
  - plaque-complex-i-agent-4HEA-entity-12
  - plaque-complex-i-agent-4HEA-entity-13
  - plaque-complex-i-agent-4HEA-entity-14
  - plaque-complex-i-agent-4HEA-entity-15
  - plaque-complex-i-agent-4HEA-entity-16
  - plaque-complex-i-agent-Q56222
  - plaque-complex-i-agent-Q56221
  - plaque-complex-i-agent-Q56223
  - plaque-complex-i-agent-Q56220
  - plaque-complex-i-agent-Q56219
  - plaque-complex-i-agent-Q56218
  - plaque-complex-i-agent-Q56224
  - plaque-complex-i-agent-Q56217
  - plaque-complex-i-agent-Q56225
  - plaque-complex-i-agent-Q56226
  - plaque-complex-i-agent-Q56227
  - plaque-complex-i-agent-Q56228
  - plaque-complex-i-agent-Q56229
  - plaque-complex-i-agent-Q60019
  - plaque-complex-i-agent-ipr-001750
  - plaque-complex-i-agent-ipr-006137
  - plaque-sdh-agent-go
  - plaque-sdh-agent-tax-562
  - plaque-sdh-agent-tax-83333
  - plaque-sdh-agent-P0AC41
  - plaque-sdh-agent-P07014
  - plaque-sdh-agent-P69054
  - plaque-sdh-agent-P0AC44
  - plaque-sdh-agent-matches-P0AC41
  - plaque-sdh-agent-matches-P07014
  - plaque-sdh-agent-matches-P69054
  - plaque-sdh-agent-matches-P0AC44
  - plaque-sdh-agent-IPR011281
  - plaque-sdh-agent-IPR014006
  - plaque-sdh-agent-IPR030664
  - plaque-sdh-agent-IPR065464
  - plaque-sdh-agent-pdb-1NEK
  - plaque-sdh-agent-assembly-1NEK
  - plaque-sdh-agent-1NEK-entity-1
  - plaque-sdh-agent-1NEK-entity-2
  - plaque-sdh-agent-1NEK-entity-3
  - plaque-sdh-agent-1NEK-entity-4
  - plaque-sdh-agent-pmid-12560550
  - plaque-sdh-agent-pmid-15919996
  - plaque-sdh-agent-pmid-16079137
  - plaque-adapter-datasets
  - plaque-adapter-frontend
  - plaque-adapter-meta
  - plaque-mcr-agent-IPR003178-retry
  - plaque-sdh-agent-IPR004489-retry
  - plaque-sdh-agent-IPR014314-retry
  - plaque-sdh-agent-IPR014312-retry
  - plaque-adapter-gene-modules-sdhC
  - plaque-adapter-gene-modules-sdhA
  - plaque-adapter-gene-modules-sdhB
  - plaque-adapter-gene-modules-sdhD
  - plaque-sdh-agent-IPR050573
  - plaque-adapter-summary-1
  - plaque-adapter-members-1
  - plaque-adapter-summary-10
  - plaque-adapter-members-10
  - plaque-adapter-summary-14
  - plaque-adapter-members-14
  - plaque-mcr-primary-browser
  - plaque-sdh-stenberg-browser
  - micro-policy
  - micro-protein-policy
  - micro-adapter-policy
  - micro-native-verifier
  - micro-workflow-config
  - micro-psii-agent-go
  - micro-rod-agent-go
  - micro-psii-prep-go
  - micro-psii-agent-tax-1117
  - micro-psii-agent-tax-32053
  - micro-rod-agent-tax-2763
  - micro-rod-agent-tax-2813851
  - micro-psii-prep-tax-103690
  - micro-psii-agent-umena2011-pdf
  - micro-psii-kamiya2003-html
  - micro-psii-kawakami2009-html
  - micro-psii-agent-P51765
  - micro-psii-agent-D0VWR8
  - micro-psii-agent-epmc
  - micro-psii-agent-IPR005867
  - micro-psii-agent-IPR005868
  - micro-psii-agent-IPR000484
  - micro-rod-agent-IPR012128
  - micro-rod-agent-IPR001297
  - micro-rod-agent-IPR038255
  - micro-rod-agent-IPR016470
  - micro-rod-agent-kawakami2022-jats
  - micro-rod-agent-A0ABT0C7V5
  - micro-rod-agent-A0ABT0C7V6
  - micro-rod-agent-A0ABT0C7V3
  - micro-rod-agent-A0ABT0C7D6
  - micro-rod-agent-A0ABT0C9G9
  - micro-rod-agent-P50034
  - micro-rod-new-A0ABT0CFU3
  - micro-rod-agent-MCJ2541704.1-genpept
  - micro-rod-agent-pdb-7veb-entity4
  - micro-rod-new-genpept
  - micro-rod-new-IPR008213
  - micro-psii-prep-chang2015-meta
  - micro-psii-prep-chang2015-pmc-html
  - micro-psii-prep-perez2024-meta
  - micro-publisher
  - micro-perez-publisher-browser
  - micro-perez-body-browser-unavailable
  - micro-adapter-catalogue
  - micro-adapter-client-js
  - micro-meta
  - micro-gene-Synpcc7942_0424
  - micro-gene-Synpcc7942_0655
  - micro-gene-Synpcc7942_0893
  - micro-gene-Synpcc7942_1047
  - micro-gene-Synpcc7942_1048
  - micro-gene-Synpcc7942_1049
  - micro-gene-Synpcc7942_1050
  - micro-gene-Synpcc7942_1051
  - micro-gene-Synpcc7942_1052
  - micro-gene-Synpcc7942_1053
  - micro-gene-Synpcc7942_1389
  - micro-gene-Synpcc7942_1637
  - micro-gene-Synpcc7942_2030
  - micro-module-1
  - micro-module-1-genes
  - micro-module-6
  - micro-module-6-genes
  - micro-module-38
  - micro-module-38-genes
  - micro-adapter-publication
  - septin-s2351-rc-prep-go
  - septin-s2351-rc-prep-tax-1063
  - septin-s2351-rc-prep-bahatyrova2004-whiterose-pdf
  - septin-s2351-v0-agent-go
  - septin-s2351-v0-agent-tax-4932
  - septin-s2351-v0-agent-kane2006-legacy-html
  - septin-s2351-v1-agent-go
  - septin-s2351-v1-agent-ro-native
  - septin-s2351-outer-agent-go
  - septin-s2351-outer-agent-sl-0040
  - septin-s2351-outer-agent-chebi-16412
  - septin-s2351-outer-agent-tax-2
  - septin-s2351-outer-agent-tax-562
  - septin-s2351-outer-agent-tax-83333
  - septin-s2351-outer-agent-P0A910
  - septin-s2351-outer-agent-P06996
  - septin-s2351-outer-agent-P02931
  - septin-s2351-outer-agent-P0A940
  - septin-s2351-outer-agent-P31554
  - septin-s2351-outer-agent-P77774
  - septin-s2351-outer-agent-P0A903
  - septin-s2351-outer-agent-P0AC02
  - septin-s2351-outer-agent-matches-P0A910
  - septin-s2351-outer-agent-matches-P06996
  - septin-s2351-outer-agent-matches-P02931
  - septin-s2351-outer-agent-silhavy2010-legacy-html
  - septin-s2351-outer-agent-sperandeo2017-legacy-html
  - septin-s2351-outer-agent-hagan2011-pdf
  - septin-s2351-outer-agent-nikaido2003-browser1
  - septin-s2351-current-adapter-catalogue
  - septin-s2351-outer-agent-matches-P0A940-retry
  - septin-s2351-adapter-gene-ompA
  - septin-s2351-adapter-modules-ompA
  - septin-s2351-adapter-gene-ompC
  - septin-s2351-adapter-modules-ompC
  - septin-s2351-adapter-gene-ompF
  - septin-s2351-adapter-modules-ompF
  - septin-s2351-adapter-gene-bamA
  - septin-s2351-adapter-modules-bamA
  - septin-s2351-adapter-gene-bamB
  - septin-s2351-adapter-modules-bamB
  - septin-s2351-adapter-gene-bamC
  - septin-s2351-adapter-modules-bamC
  - septin-s2351-adapter-gene-bamD
  - septin-s2351-adapter-modules-bamD
  - septin-s2351-adapter-gene-lptD
  - septin-s2351-adapter-modules-lptD
  - septin-s2351-adapter-module-86
  - septin-s2351-adapter-module-88
  - septin-s2351-adapter-module-25
  - septin-s2351-adapter-module-22
  - septin-s2351-comayras-indexed-body
  - septin-s2351-policy
  - septin-s2351-node-types
- check_id: historical-adapter-runner
  name: Retained historical adapter runner availability
  status: unavailable
  required: false
  target_ids:
  - GO:0044674
  - GO:0009523
  - cellstructuremech:phycobilisome_rod
  - GO:0030096
  - cellstructuremech:rc_lh1_pufx_core_complex
  - GO:0045271
  - GO:0045273
  - GO:0009279
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
- check_id: photosystem-ii-uniprot-verify
  name: Native photosystem-ii UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0009523
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/photosystem_ii.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact inventory coverage and claim-level
    limitations remain in its evidence; no record edits were applied.
  scope_note: Actual execution at current main-merge head; verifier source bytes frozen
    in native inspect.
  evidence_ids:
  - micro-native-photosystem-ii-verify
- check_id: photosystem-ii-uniprot-causal
  name: Native photosystem-ii UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0009523
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/photosystem_ii.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact inventory coverage and claim-level
    limitations remain in its evidence; no record edits were applied.
  scope_note: Actual execution at current main-merge head; verifier source bytes frozen
    in native inspect.
  evidence_ids:
  - micro-native-photosystem-ii-causal
- check_id: phycobilisome-rod-uniprot-verify
  name: Native phycobilisome-rod UniProt verify check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:phycobilisome_rod
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/phycobilisome_rod.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact inventory coverage and claim-level
    limitations remain in its evidence; no record edits were applied.
  scope_note: Actual execution at current main-merge head; verifier source bytes frozen
    in native inspect.
  evidence_ids:
  - micro-native-phycobilisome-rod-verify
- check_id: phycobilisome-rod-uniprot-causal
  name: Native phycobilisome-rod UniProt causal check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:phycobilisome_rod
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/phycobilisome_rod.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact inventory coverage and claim-level
    limitations remain in its evidence; no record edits were applied.
  scope_note: Actual execution at current main-merge head; verifier source bytes frozen
    in native inspect.
  evidence_ids:
  - micro-native-phycobilisome-rod-causal
- check_id: outer-membrane-uniprot-verify
  name: Native outer-membrane UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0009279
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/envelope/cell_outer_membrane.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact inventory coverage and claim-level
    limitations remain in its evidence; no record edits were applied.
  scope_note: Actual execution at current main-merge head; verifier source bytes frozen
    in native inspect.
  evidence_ids:
  - septin-s2351-outer-native-verify
- check_id: outer-membrane-uniprot-causal
  name: Native outer-membrane UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0009279
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/envelope/cell_outer_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact inventory coverage and claim-level
    limitations remain in its evidence; no record edits were applied.
  scope_note: Actual execution at current main-merge head; verifier source bytes frozen
    in native inspect.
  evidence_ids:
  - septin-s2351-outer-native-causal
- check_id: mcr-uniprot-verify
  name: Native mcr UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0044674
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/methyl_coenzyme_m_reductase_complex.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact inventory coverage and claim-level
    limitations remain in its evidence; no record edits were applied.
  scope_note: Actual execution at current main-merge head; verifier source bytes frozen
    in native inspect.
  evidence_ids:
  - plaque-mcr-native-uniprot-verify
- check_id: mcr-uniprot-causal
  name: Native mcr UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0044674
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/methyl_coenzyme_m_reductase_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact inventory coverage and claim-level
    limitations remain in its evidence; no record edits were applied.
  scope_note: Actual execution at current main-merge head; verifier source bytes frozen
    in native inspect.
  evidence_ids:
  - plaque-mcr-native-uniprot-causal
- check_id: complex-i-uniprot-verify
  name: Native complex-i UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0045271
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/respiratory_chain_complex_i.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact inventory coverage and claim-level
    limitations remain in its evidence; no record edits were applied.
  scope_note: Actual execution at current main-merge head; verifier source bytes frozen
    in native inspect.
  evidence_ids:
  - plaque-complex-i-native-uniprot-verify
- check_id: complex-i-uniprot-causal
  name: Native complex-i UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0045271
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/respiratory_chain_complex_i.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact inventory coverage and claim-level
    limitations remain in its evidence; no record edits were applied.
  scope_note: Actual execution at current main-merge head; verifier source bytes frozen
    in native inspect.
  evidence_ids:
  - plaque-complex-i-native-uniprot-causal
- check_id: complex-ii-uniprot-verify
  name: Native complex-ii UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0045273
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/respiratory_chain_complex_ii_succinate_dehydrogenase.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact inventory coverage and claim-level
    limitations remain in its evidence; no record edits were applied.
  scope_note: Actual execution at current main-merge head; verifier source bytes frozen
    in native inspect.
  evidence_ids:
  - plaque-complex-ii-native-uniprot-verify
- check_id: complex-ii-uniprot-causal
  name: Native complex-ii UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0045273
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/respiratory_chain_complex_ii_succinate_dehydrogenase.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact inventory coverage and claim-level
    limitations remain in its evidence; no record edits were applied.
  scope_note: Actual execution at current main-merge head; verifier source bytes frozen
    in native inspect.
  evidence_ids:
  - plaque-complex-ii-native-uniprot-causal
evidence:
- evidence_id: current-record-0
  kind: record_content
  reference: data/structures/energy_complex/methyl_coenzyme_m_reductase_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T05:18:03Z'
  support: context_only
  summary: Original frozen SHA256 ef43ab9df3e0a3d8ed86e0347c9801db59ced9efd1d0313f8ab2a9b3b1420338;
    current SHA256 369ad320d4bc19c72a79fb14037b46c5e12f6eddaa64bd0bb04572e9a8ea685e.
    Changed record reassessed against current sources.
  snapshot_sha256: 369ad320d4bc19c72a79fb14037b46c5e12f6eddaa64bd0bb04572e9a8ea685e
- evidence_id: original-review-0
  kind: prior_review
  reference: reviews/structured/20261021T091345Z-methyl-coenzyme-m-reductase-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T05:18:03Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 10c87a197c78b725f0a92b31d638ef50bca24fe5837e7a59c3660804cae4b089
- evidence_id: current-record-1
  kind: record_content
  reference: data/structures/energy_complex/photosystem_ii.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T05:18:03Z'
  support: context_only
  summary: Original frozen SHA256 fc05496451f76ed16643edb2ca590803fd07569abfe432111e31314375687a16;
    current SHA256 fc05496451f76ed16643edb2ca590803fd07569abfe432111e31314375687a16.
    Record bytes unchanged since the original review.
  snapshot_sha256: fc05496451f76ed16643edb2ca590803fd07569abfe432111e31314375687a16
- evidence_id: original-review-1
  kind: prior_review
  reference: reviews/structured/20261021T091346Z-photosystem-ii-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T05:18:03Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 5138fd0d9d80523573027ab48105acfc6915554a6ecacb5bf8aa6e8cfccc17b2
- evidence_id: current-record-2
  kind: record_content
  reference: data/structures/energy_complex/phycobilisome_rod.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T05:18:03Z'
  support: context_only
  summary: Original frozen SHA256 612013ed996da72581fa218e57c90acce39e6d069c3bbd2b75958cac0b273616;
    current SHA256 f610a707b8f8fea3edfd28574b996a315eaf1e2d245de7efce9edf96b49943d1.
    Changed record reassessed against current sources.
  snapshot_sha256: f610a707b8f8fea3edfd28574b996a315eaf1e2d245de7efce9edf96b49943d1
- evidence_id: original-review-2
  kind: prior_review
  reference: reviews/structured/20261021T091347Z-phycobilisome-rod-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T05:18:03Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 5de19cc2aeb828652a3d90d22d578645985e8259bd6206abb59e62ecdf11daf9
- evidence_id: current-record-3
  kind: record_content
  reference: data/structures/energy_complex/plasma_membrane_derived_thylakoid_photosystem_ii.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T05:18:03Z'
  support: context_only
  summary: Original frozen SHA256 7629a2480ce3d823e87431d0c26be93c45101095021fd60087301f5f1d9a58ef;
    current SHA256 7629a2480ce3d823e87431d0c26be93c45101095021fd60087301f5f1d9a58ef.
    Record bytes unchanged since the original review.
  snapshot_sha256: 7629a2480ce3d823e87431d0c26be93c45101095021fd60087301f5f1d9a58ef
- evidence_id: original-review-3
  kind: prior_review
  reference: reviews/structured/20261021T091348Z-plasma-membrane-derived-thylakoid-photosystem-ii-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T05:18:03Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: c60ea9147f742d25275b0dff673fc6957fc7497b55ee1862482c20358b2333b4
- evidence_id: current-record-4
  kind: record_content
  reference: data/structures/energy_complex/rc_lh1_pufx_core_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T05:18:03Z'
  support: context_only
  summary: Original frozen SHA256 0a3a6fcfe54b7a355fd2903992f521fb2fc293ce984d4ede356dbc8460071824;
    current SHA256 0a3a6fcfe54b7a355fd2903992f521fb2fc293ce984d4ede356dbc8460071824.
    Record bytes unchanged since the original review.
  snapshot_sha256: 0a3a6fcfe54b7a355fd2903992f521fb2fc293ce984d4ede356dbc8460071824
- evidence_id: original-review-4
  kind: prior_review
  reference: reviews/structured/20261021T091349Z-rc-lh1-pufx-core-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T05:18:03Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 8dbe30a3e38992ffce97d3e9ed303b413f769b7be2820b6f3052b338a647d1de
- evidence_id: current-record-5
  kind: record_content
  reference: data/structures/energy_complex/respiratory_chain_complex_i.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T05:18:03Z'
  support: context_only
  summary: Original frozen SHA256 412f85b2aeb446f9635a89f69cef1dc90c124dbade5bc41f1c5b568461a31e4a;
    current SHA256 0d0f4b5c3346e25dbbd3595d959c03d40dc9943e3e6055dcca3746fd4bf67540.
    Changed record reassessed against current sources.
  snapshot_sha256: 0d0f4b5c3346e25dbbd3595d959c03d40dc9943e3e6055dcca3746fd4bf67540
- evidence_id: original-review-5
  kind: prior_review
  reference: reviews/structured/20261021T091350Z-respiratory-chain-complex-i-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T05:18:03Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 40d426bae2756cbf27bea5822fa3e323eebe2d00fce3e53716ad33584aa52ae8
- evidence_id: current-record-6
  kind: record_content
  reference: data/structures/energy_complex/respiratory_chain_complex_ii_succinate_dehydrogenase.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T05:18:03Z'
  support: context_only
  summary: Original frozen SHA256 9660cbd309d7c81353bf0b1fe1a3cd5a883f6ec574e3a0d9e990166dd861de0f;
    current SHA256 4e6914fa2c29221809c1a172d98aa541c5adc01bc5090cc8c0eb55b56a3d463d.
    Changed record reassessed against current sources.
  snapshot_sha256: 4e6914fa2c29221809c1a172d98aa541c5adc01bc5090cc8c0eb55b56a3d463d
- evidence_id: original-review-6
  kind: prior_review
  reference: reviews/structured/20261021T091351Z-respiratory-chain-complex-ii-succinate-dehydrogenase-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T05:18:03Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 7d846c8c936360c7e05a670be52a0c1bc49a444e40d4c21f9ce044bba8c49d1a
- evidence_id: current-record-7
  kind: record_content
  reference: data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_v0_domain.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T05:18:03Z'
  support: context_only
  summary: Original frozen SHA256 b76891f7e50630db7612669a25299babae68eb2e480724de8209094cc1953c48;
    current SHA256 b76891f7e50630db7612669a25299babae68eb2e480724de8209094cc1953c48.
    Record bytes unchanged since the original review.
  snapshot_sha256: b76891f7e50630db7612669a25299babae68eb2e480724de8209094cc1953c48
- evidence_id: original-review-7
  kind: prior_review
  reference: reviews/structured/20261021T091352Z-vacuolar-proton-transporting-v-type-atpase-v0-domain-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T05:18:03Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 0ffb74ceefe0d2d5041d8745977f28dec10202cfc753d844a5e7c8237e33827c
- evidence_id: current-record-8
  kind: record_content
  reference: data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_v1_domain.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T05:18:03Z'
  support: context_only
  summary: Original frozen SHA256 fabfca0b7f5ff5ee1340a6874918e4505c242d7939734a2e9ef8f3df5ebeeb22;
    current SHA256 fabfca0b7f5ff5ee1340a6874918e4505c242d7939734a2e9ef8f3df5ebeeb22.
    Record bytes unchanged since the original review.
  snapshot_sha256: fabfca0b7f5ff5ee1340a6874918e4505c242d7939734a2e9ef8f3df5ebeeb22
- evidence_id: original-review-8
  kind: prior_review
  reference: reviews/structured/20261021T091354Z-vacuolar-proton-transporting-v-type-atpase-v1-domain-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T05:18:03Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 886587cea44f281a30b9b8ac553b4d0fed42cfa51901e86d602d1bd0c3ca2460
- evidence_id: current-record-9
  kind: record_content
  reference: data/structures/envelope/cell_outer_membrane.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T05:18:03Z'
  support: context_only
  summary: Original frozen SHA256 6a21a7409a3e93aa290cbff61f4734629b927f04a33c469e6166ef1b24673fab;
    current SHA256 6a21a7409a3e93aa290cbff61f4734629b927f04a33c469e6166ef1b24673fab.
    Record bytes unchanged since the original review.
  snapshot_sha256: 6a21a7409a3e93aa290cbff61f4734629b927f04a33c469e6166ef1b24673fab
- evidence_id: original-review-9
  kind: prior_review
  reference: reviews/structured/20261021T091355Z-cell-outer-membrane-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T05:18:03Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 6238f43a75d18940317c72df2a026d44c21593e6d713a79475454e57b26b8d21
- evidence_id: plaque-mcr-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0044674,GO:1990234,GO:0050524
  locator: results[].id/name/aspect/definition/isObsolete
  accessed_at: '2026-11-03T05:07:18.854224Z'
  snapshot_sha256: 66c04b751e4d3928e4df616e36a07256f2031bb160f7b1f3ef5a1480db2e7208
  summary: 'Current authority terms inspected: [(''GO:1990234'', ''transferase complex'',
    False), (''GO:0044674'', ''methyl coenzyme M reductase complex'', False), (''GO:0050524'',
    ''coenzyme-B sulfoethylthiotransferase activity'', False)]. Obsolete arm terms
    do not supply current exact component identities.'
  support: supports
- evidence_id: plaque-mcr-agent-tax-79929
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/79929
  locator: taxId, scientificName and lineage
  accessed_at: '2026-11-03T05:07:18.854499Z'
  snapshot_sha256: c523c797d7333f99abc7a89439b81df8e7efa5fd247d757cf6d7609c64fc3eda
  summary: Native taxonomy checks the exact organism/strain identifier; species-level
    deposited source and strain-specific examples remain distinct.
  support: supports
- evidence_id: plaque-mcr-agent-IPR016212
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016212/
  locator: metadata.accession/type/name, integrated member signatures and description
  accessed_at: '2026-11-03T05:07:18.854621Z'
  snapshot_sha256: ad31c23e114a38e4ee38a2a989d209b1fbf6988a16a9ff522fc72ec3cebf4215
  summary: Inspected family IPR016212, Methyl coenzyme M reductase, alpha subunit,
    against exact whole-component scope.
  support: supports
- evidence_id: plaque-mcr-agent-IPR003179
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR003179/
  locator: metadata.accession/type/name, integrated member signatures and description
  accessed_at: '2026-11-03T05:07:18.854693Z'
  snapshot_sha256: df4e03d663e0db1ed327e4cef550c892f82f8dcc4dc241591c0f9d735ce43906
  summary: Inspected family IPR003179, Methyl-coenzyme M reductase, beta subunit,
    against exact whole-component scope.
  support: supports
- evidence_id: plaque-mcr-agent-pdb-1mro
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/entry/1MRO
  locator: struct.title, primary citation, resolution and polymer identities
  accessed_at: '2026-11-03T05:07:19.509759Z'
  snapshot_sha256: 78181422f5730747ab616e8921659c2bceb209d6b435852c85c2f63acb3d8f1f
  summary: Deposited structure METHYL-COENZYME M REDUCTASE; native primary citation
    and structure identifiers checked, without raw-coordinate reanalysis.
  support: supports
- evidence_id: plaque-mcr-agent-pdb-1mro-assembly1
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/assembly/1MRO/1
  locator: pdbx_struct_assembly and rcsb_assembly_info
  accessed_at: '2026-11-03T05:07:19.569406Z'
  snapshot_sha256: 664a5c9cc48727cc34f810cd96029d3c158ef1fff5beb57963393f71de4e091d
  summary: Biological assembly annotation is hexameric with 6 protein instances. This
    deposited annotation is not an independent in-cell stoichiometry measurement.
  support: supports
- evidence_id: plaque-mcr-agent-pdb-1mro-entity1
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/1MRO/1
  locator: rcsb_polymer_entity, source organism and SIFTS reference identifiers
  accessed_at: '2026-11-03T05:07:19.618670Z'
  snapshot_sha256: 9a93c7842f822a4aea1359e56092d4f28be487524675da462365cbaaee61caf1
  summary: 'Deposited polymer identity and reference mapping inspected: [(''P11558'',
    1.0)]. Source taxon [79929]. No coordinate reanalysis.'
  support: supports
- evidence_id: plaque-mcr-agent-pdb-1mro-entity2
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/1MRO/2
  locator: rcsb_polymer_entity, source organism and SIFTS reference identifiers
  accessed_at: '2026-11-03T05:07:19.649899Z'
  snapshot_sha256: da2a09d567c4962696c0c801fcd14b03dbd2f2b860402cf13a4b370240ebc29c
  summary: 'Deposited polymer identity and reference mapping inspected: [(''P11560'',
    1.0)]. Source taxon [79929]. No coordinate reanalysis.'
  support: supports
- evidence_id: plaque-mcr-agent-pdb-1mro-entity3
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/1MRO/3
  locator: rcsb_polymer_entity, source organism and SIFTS reference identifiers
  accessed_at: '2026-11-03T05:07:19.729559Z'
  snapshot_sha256: 1bd30940b64e61e2e95d5419bd77523406b759b9d4352a90d59bfa65d9f9adde
  summary: 'Deposited polymer identity and reference mapping inspected: [(''P11562'',
    1.0)]. Source taxon [79929]. No coordinate reanalysis.'
  support: supports
- evidence_id: plaque-mcr-agent-P11558
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P11558.json
  locator: primaryAccession, organism, genes, protein description, FUNCTION/SUBUNIT/COFACTOR/location
    comments and complete InterPro cross-references
  accessed_at: '2026-11-03T05:07:19.774451Z'
  snapshot_sha256: a050e39a361a6cc0adbd3444033066d9a325d93ecffe60012d99a731a415e5b1
  summary: Native reviewed P11558 identifies mcrA in taxon 79929; accession, role,
    location evidence attribution and family candidates checked within this annotated
    source.
  support: supports
- evidence_id: plaque-mcr-agent-P11560
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P11560.json
  locator: primaryAccession, organism, genes, protein description, FUNCTION/SUBUNIT/COFACTOR/location
    comments and complete InterPro cross-references
  accessed_at: '2026-11-03T05:07:19.825197Z'
  snapshot_sha256: 373e288ecb275c113a75ab9ac2cce9c25992366ec8e6db84c1cd3be95b4cd0e9
  summary: Native reviewed P11560 identifies mcrB in taxon 79929; accession, role,
    location evidence attribution and family candidates checked within this annotated
    source.
  support: supports
- evidence_id: plaque-mcr-agent-P11562
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P11562.json
  locator: primaryAccession, organism, genes, protein description, FUNCTION/SUBUNIT/COFACTOR/location
    comments and complete InterPro cross-references
  accessed_at: '2026-11-03T05:07:20.073546Z'
  snapshot_sha256: a66aa1a2bb69cac4b2faaa70f03d4207ca07d09e3cccf45bce23a4f8890c7384
  summary: Native reviewed P11562 identifies mcrG in taxon 79929; accession, role,
    location evidence attribution and family candidates checked within this annotated
    source.
  support: supports
- evidence_id: plaque-mcr-agent-uniprot-unique
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue%20AND%20taxonomy_id%3A79929%20AND%20%28gene_exact%3AmcrA%20OR%20gene_exact%3AmcrB%20OR%20gene_exact%3AmcrG%29&format=json&size=100
  locator: results[].primaryAccession, genes, organism
  accessed_at: '2026-11-03T05:07:20.121495Z'
  snapshot_sha256: 060953d2d172766d47f3f9f19686f761eae33e39be88addb296d3439240ae5c3
  summary: Native bounded query returns [('P11562', 79929), ('P11560', 79929), ('P11558',
    79929)].
  search_scope: UniProt REST; query=reviewed:true AND taxonomy_id:79929 AND (gene_exact:mcrA
    OR gene_exact:mcrB OR gene_exact:mcrG)&format=json&size=100; accessed 2026-11-03T05:07:20.121495Z;
    exact named gene/taxon criteria only.
  support: supports
- evidence_id: plaque-mcr-agent-wrede2013-jats
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3596918/fullTextXML
  locator: Abstract; Methods purification/immunolabeling; Results and Discussion;
    figure captions
  accessed_at: '2026-11-03T05:07:20.679837Z'
  snapshot_sha256: 54db6f8f1cacc65e7d138456bcd0a5b6a5d4cb0b3bad12f8768eaa03890fded9
  summary: Purified M.marburgensis MCR I antigen supports the localization experiment.
    Signal is cytoplasmic in routine cultures, with condition-dependent membrane association
    under nickel limitation or levulinic acid. This does not separately localize every
    isolated subunit or establish universal cytoplasmic exclusivity.
  support: supports
- evidence_id: plaque-mcr-agent-epmc
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A9367957%20OR%20EXT_ID%3A23533332
  locator: Europe PMC publication metadata and abstract
  accessed_at: '2026-11-03T05:07:21.708962Z'
  snapshot_sha256: 81a20de243ae3b18ab02a5699321512f41a9e7c121d53a6e2aa8d01aca647573
  summary: Fresh title/author/DOI/PMID and abstract inspected. Full-text access is
    only claimed for separately identified body evidence.
  support: supports
- evidence_id: plaque-complex-i-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0045271%2CGO%3A0098803%2CGO%3A0008137
  locator: results[].id/name/aspect/definition/isObsolete
  accessed_at: '2026-11-03T05:07:21.759641Z'
  snapshot_sha256: f6470e88b26349bf06188cbe20c816cc0853c70629f5a5f81ad750d05f26d134
  summary: 'Current authority terms inspected: [(''GO:0045271'', ''respiratory chain
    complex I'', False), (''GO:0008137'', ''NADH dehydrogenase (ubiquinone) activity'',
    False), (''GO:0098803'', ''respiratory chain complex'', False)]. Obsolete arm
    terms do not supply current exact component identities.'
  support: supports
- evidence_id: plaque-complex-i-agent-go-arm-candidates
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0042652%2CGO%3A0042653
  locator: results[].id/name/aspect/definition/isObsolete
  accessed_at: '2026-11-03T05:07:22.168562Z'
  snapshot_sha256: eb5f72a796b4605c79ad4d23b242d16fc0f4fe4a1593d721ee43d7e03df78715
  summary: 'Current authority terms inspected: [(''GO:0042652'', ''obsolete mitochondrial
    respiratory chain complex I, peripheral segment'', True), (''GO:0042653'', ''obsolete
    mitochondrial respiratory chain complex I, membrane segment'', True)]. Obsolete
    arm terms do not supply current exact component identities.'
  support: supports
- evidence_id: plaque-complex-i-agent-go-peripheral-search
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=peripheral%20arm&limit=100
  locator: Returned first page GO name/definition/isObsolete results
  accessed_at: '2026-11-03T05:07:22.270858Z'
  snapshot_sha256: e2ed242fc15aac7fe46b9adcf0677f9c93d3bebb09fb30415daed1ebb80cb42f
  summary: Inspected bounded arm-term candidates. The returned candidates do not justify
    replacing the maintained whole-arm label with an obsolete or mismatched GO term.
    This is not exhaustive absence evidence.
  search_scope: QuickGO search; query=peripheral arm&limit=100; accessed 2026-11-03T05:07:22.270858Z;
    first page only; peripheral search reports96 total, membrane-arm search1643 total,
    page limit100.
  support: supports
- evidence_id: plaque-complex-i-agent-go-membrane-arm-search
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=membrane%20arm&limit=100
  locator: Returned first page GO name/definition/isObsolete results
  accessed_at: '2026-11-03T05:07:22.369141Z'
  snapshot_sha256: 8e299f1f143c36a4c03aa0d039a94a5c392923acba2b8d0810d05e3faa8bebfd
  summary: Inspected bounded arm-term candidates. The returned candidates do not justify
    replacing the maintained whole-arm label with an obsolete or mismatched GO term.
    This is not exhaustive absence evidence.
  search_scope: QuickGO search; query=membrane arm&limit=100; accessed 2026-11-03T05:07:22.369141Z;
    first page only; peripheral search reports96 total, membrane-arm search1643 total,
    page limit100.
  support: supports
- evidence_id: plaque-complex-i-agent-tax-274
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/274
  locator: taxId, scientificName and lineage
  accessed_at: '2026-11-03T05:07:22.533706Z'
  snapshot_sha256: 0720b4a9378b4edef256362f3bc75f4c79e9fd6b59e1283f697d23edfc8ca2b1
  summary: Native taxonomy checks the exact organism/strain identifier; species-level
    deposited source and strain-specific examples remain distinct.
  support: supports
- evidence_id: plaque-complex-i-agent-tax-300852
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/300852
  locator: taxId, scientificName and lineage
  accessed_at: '2026-11-03T05:07:22.767761Z'
  snapshot_sha256: ee73cb5e482a05be5d1cd30cba11d5c60458034cf7dfc07ef06f7241ac313aaf
  summary: Native taxonomy checks the exact organism/strain identifier; species-level
    deposited source and strain-specific examples remain distinct.
  support: supports
- evidence_id: plaque-complex-i-agent-epmc
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A23417064%20AND%20SRC%3AMED&format=json&resultType=core
  locator: Europe PMC publication metadata and abstract
  accessed_at: '2026-11-03T05:07:23.129641Z'
  snapshot_sha256: e4f964559f6abe6c81690f7c0a86ad78e81be96813c6a67874f703a1845000f7
  summary: Fresh title/author/DOI/PMID and abstract inspected. Full-text access is
    only claimed for separately identified body evidence.
  support: supports
- evidence_id: plaque-complex-i-agent-baradaran2013-jats
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3672946/fullTextXML
  locator: Introduction; Results S1-S4; Methods S6-S11; associated figure captions
  accessed_at: '2026-11-03T05:07:23.156783Z'
  snapshot_sha256: 8e4a9762e39f0f334983f805c1d8c699a6e6abf719e7f93690412eddf7f365a2
  summary: Primary structure separates seven conserved hydrophilic and seven conserved
    membrane subunits, with two additional proteins in this preparation. FMN/FeS NADH
    electron transfer supports the refreshed peripheral-arm contribution edge. Native
    Thermus menaquinone is distinct from the decyl-ubiquinone analogue; coupling channels
    and water networks remain structural proposals, not direct kinetic observations.
  support: supports
- evidence_id: plaque-complex-i-agent-baradaran2013-supplement-epmc
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3672946/supplementaryFiles
  locator: Europe PMC publication metadata and abstract
  accessed_at: '2026-11-03T05:07:23.416583Z'
  snapshot_sha256: 17569dc5ee886d484e620965c00ce054f880ba00f9a6d5a47059269d17e3d316
  summary: Fresh title/author/DOI/PMID and abstract inspected. Full-text access is
    only claimed for separately identified body evidence.
  support: supports
- evidence_id: plaque-complex-i-agent-pdb-4HEA
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/entry/4HEA
  locator: struct.title, primary citation, resolution and polymer identities
  accessed_at: '2026-11-03T05:07:23.441371Z'
  snapshot_sha256: 1cd71f61f6c41d66dd33611cccc924cd814366e5bfd8189221030c069fa8c442
  summary: Deposited structure Crystal structure of the entire respiratory complex
    I from Thermus thermophilus; native primary citation and structure identifiers
    checked, without raw-coordinate reanalysis.
  support: supports
- evidence_id: plaque-complex-i-agent-assembly-4HEA
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/assembly/4HEA/1
  locator: pdbx_struct_assembly and rcsb_assembly_info
  accessed_at: '2026-11-03T05:07:23.579816Z'
  snapshot_sha256: de39f0c8edd60408ebc712c38cbb5cf86479331c3935ef3415e931416092a96f
  summary: Biological assembly annotation is hexadecameric with 16 protein instances.
    This deposited annotation is not an independent in-cell stoichiometry measurement.
  support: supports
- evidence_id: plaque-complex-i-agent-4HEA-entity-1
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/1
  locator: rcsb_polymer_entity, source organism and SIFTS reference identifiers
  accessed_at: '2026-11-03T05:07:23.650623Z'
  snapshot_sha256: 12d43e44fc007b94f783980cc1d3a57b81ebddb50b59b1cf86b2b4bdd7360d10
  summary: 'Deposited polymer identity and reference mapping inspected: [(''Q56222'',
    1.0)]. Source taxon [300852]. No coordinate reanalysis.'
  support: supports
- evidence_id: plaque-complex-i-agent-4HEA-entity-2
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/2
  locator: rcsb_polymer_entity, source organism and SIFTS reference identifiers
  accessed_at: '2026-11-03T05:07:23.784960Z'
  snapshot_sha256: 4a6a974c3823b50893afc59f90e4776c16568b8ce1327da392beac9f7ea53658
  summary: 'Deposited polymer identity and reference mapping inspected: [(''Q56221'',
    1.0)]. Source taxon [300852]. No coordinate reanalysis.'
  support: supports
- evidence_id: plaque-complex-i-agent-4HEA-entity-3
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/3
  locator: rcsb_polymer_entity, source organism and SIFTS reference identifiers
  accessed_at: '2026-11-03T05:07:23.854121Z'
  snapshot_sha256: fbb909ee38290c2f96d4f56538cb35c05d05d279abe51e39a1e989dc9771720d
  summary: 'Deposited polymer identity and reference mapping inspected: [(''Q56223'',
    1.0)]. Source taxon [300852]. No coordinate reanalysis.'
  support: supports
- evidence_id: plaque-complex-i-agent-4HEA-entity-4
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/4
  locator: rcsb_polymer_entity, source organism and SIFTS reference identifiers
  accessed_at: '2026-11-03T05:07:23.871559Z'
  snapshot_sha256: 13bcfaabd117132acbdab7955d929b7b85c522f97611498b7a0516c4e72653ff
  summary: 'Deposited polymer identity and reference mapping inspected: [(''Q56220'',
    1.0)]. Source taxon [300852]. No coordinate reanalysis.'
  support: supports
- evidence_id: plaque-complex-i-agent-4HEA-entity-5
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/5
  locator: rcsb_polymer_entity, source organism and SIFTS reference identifiers
  accessed_at: '2026-11-03T05:07:23.985143Z'
  snapshot_sha256: 57b10dc94c1de0dad11df0a210cf9e5ba0ed883786e676bfcb442d870125c2c4
  summary: 'Deposited polymer identity and reference mapping inspected: [(''Q56219'',
    1.0)]. Source taxon [300852]. No coordinate reanalysis.'
  support: supports
- evidence_id: plaque-complex-i-agent-4HEA-entity-6
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/6
  locator: rcsb_polymer_entity, source organism and SIFTS reference identifiers
  accessed_at: '2026-11-03T05:07:24.025554Z'
  snapshot_sha256: fa1ca99503ac5af27664b1ddb2df614f046becb57d68d78aea36af13a2c9edea
  summary: 'Deposited polymer identity and reference mapping inspected: [(''Q56218'',
    1.0)]. Source taxon [300852]. No coordinate reanalysis.'
  support: supports
- evidence_id: plaque-complex-i-agent-4HEA-entity-7
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/7
  locator: rcsb_polymer_entity, source organism and SIFTS reference identifiers
  accessed_at: '2026-11-03T05:07:24.074911Z'
  snapshot_sha256: e79142a53b1077be930915a9d62e95b0dcb453a4966dd6670305f8460ec2b07f
  summary: 'Deposited polymer identity and reference mapping inspected: [(''Q56224'',
    1.0)]. Source taxon [300852]. No coordinate reanalysis.'
  support: supports
- evidence_id: plaque-complex-i-agent-4HEA-entity-8
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/8
  locator: rcsb_polymer_entity, source organism and SIFTS reference identifiers
  accessed_at: '2026-11-03T05:07:24.138776Z'
  snapshot_sha256: a352e415639cf04e34867649f8fc4f0c7f335969973f7f559aea0181b3e7d639
  summary: 'Deposited polymer identity and reference mapping inspected: [(''Q5SKZ7'',
    1.0)]. Source taxon [300852]. No coordinate reanalysis.'
  support: supports
- evidence_id: plaque-complex-i-agent-4HEA-entity-9
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/9
  locator: rcsb_polymer_entity, source organism and SIFTS reference identifiers
  accessed_at: '2026-11-03T05:07:24.201060Z'
  snapshot_sha256: 502091ad11f408b59933d729db6a0f3469b0968e907a5d405fb88dbdc554a000
  summary: 'Deposited polymer identity and reference mapping inspected: [(''Q5SI52'',
    1.0)]. Source taxon [300852]. No coordinate reanalysis.'
  support: supports
- evidence_id: plaque-complex-i-agent-4HEA-entity-10
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/10
  locator: rcsb_polymer_entity, source organism and SIFTS reference identifiers
  accessed_at: '2026-11-03T05:07:24.229023Z'
  snapshot_sha256: f827053d6968ac2afd109c17af87c48d14ac81ba942ad9d3c668d820bd44c044
  summary: 'Deposited polymer identity and reference mapping inspected: [(''Q56217'',
    1.0)]. Source taxon [300852]. No coordinate reanalysis.'
  support: supports
- evidence_id: plaque-complex-i-agent-4HEA-entity-11
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/11
  locator: rcsb_polymer_entity, source organism and SIFTS reference identifiers
  accessed_at: '2026-11-03T05:07:24.300334Z'
  snapshot_sha256: f5fec2fcdf9c104cc712af4a434a2f729d4084e21e7300c084c91ea521e59f18
  summary: 'Deposited polymer identity and reference mapping inspected: [(''Q56225'',
    1.0)]. Source taxon [300852]. No coordinate reanalysis.'
  support: supports
- evidence_id: plaque-complex-i-agent-4HEA-entity-12
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/12
  locator: rcsb_polymer_entity, source organism and SIFTS reference identifiers
  accessed_at: '2026-11-03T05:07:24.313568Z'
  snapshot_sha256: f3d7d37b025d5092ab1223f1f41e4246a757bc548deed9b163c1bcf2e4569317
  summary: 'Deposited polymer identity and reference mapping inspected: [(''Q56226'',
    1.0)]. Source taxon [300852]. No coordinate reanalysis.'
  support: supports
- evidence_id: plaque-complex-i-agent-4HEA-entity-13
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/13
  locator: rcsb_polymer_entity, source organism and SIFTS reference identifiers
  accessed_at: '2026-11-03T05:07:24.425009Z'
  snapshot_sha256: a1100c34b891fb48aa5c51905f27f3e6f14059c40d1f65d2d2b7e91ed23448c3
  summary: 'Deposited polymer identity and reference mapping inspected: [(''Q56227'',
    1.0)]. Source taxon [300852]. No coordinate reanalysis.'
  support: supports
- evidence_id: plaque-complex-i-agent-4HEA-entity-14
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/14
  locator: rcsb_polymer_entity, source organism and SIFTS reference identifiers
  accessed_at: '2026-11-03T05:07:24.445282Z'
  snapshot_sha256: b4cc157742d2b2a73bb5468b0dd0ce2aa971c9dcbfedb6f0a4771af16a8d0961
  summary: 'Deposited polymer identity and reference mapping inspected: [(''Q56228'',
    1.0)]. Source taxon [300852]. No coordinate reanalysis.'
  support: supports
- evidence_id: plaque-complex-i-agent-4HEA-entity-15
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/15
  locator: rcsb_polymer_entity, source organism and SIFTS reference identifiers
  accessed_at: '2026-11-03T05:07:24.530734Z'
  snapshot_sha256: aaecc8f724e3d93e7b8f5da77a7f6c8b2e57ce5edc21c86084a8e15c2f1f0fd2
  summary: 'Deposited polymer identity and reference mapping inspected: [(''Q56229'',
    1.0)]. Source taxon [300852]. No coordinate reanalysis.'
  support: supports
- evidence_id: plaque-complex-i-agent-4HEA-entity-16
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/4HEA/16
  locator: rcsb_polymer_entity, source organism and SIFTS reference identifiers
  accessed_at: '2026-11-03T05:07:24.564746Z'
  snapshot_sha256: 299be73a46a92c4bbb038a28569c126ce58efda2cc5a1601e9ce4ed56e9ae3e1
  summary: 'Deposited polymer identity and reference mapping inspected: [(''Q60019'',
    1.0)]. Source taxon [300852]. No coordinate reanalysis.'
  support: supports
- evidence_id: plaque-complex-i-agent-Q56222
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q56222.json
  locator: primaryAccession, organism, genes, protein description, FUNCTION/SUBUNIT/COFACTOR/location
    comments and complete InterPro cross-references
  accessed_at: '2026-11-03T05:07:24.649481Z'
  snapshot_sha256: 65d3f939390c7247952e7090232fceb6bc690ca1cfbb555b393e4eba54cdd018
  summary: Native reviewed Q56222 identifies nqo1 in taxon 300852; accession, role,
    location evidence attribution and family candidates checked within this annotated
    source.
  support: supports
- evidence_id: plaque-complex-i-agent-Q56221
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q56221.json
  locator: primaryAccession, organism, genes, protein description, FUNCTION/SUBUNIT/COFACTOR/location
    comments and complete InterPro cross-references
  accessed_at: '2026-11-03T05:07:24.719471Z'
  snapshot_sha256: 7bc5943f43a587c683a10d9b7270b73b1f75c3bcb9b2a88fa6317c2feee9c8ea
  summary: Native reviewed Q56221 identifies nqo2 in taxon 300852; accession, role,
    location evidence attribution and family candidates checked within this annotated
    source.
  support: supports
- evidence_id: plaque-complex-i-agent-Q56223
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q56223.json
  locator: primaryAccession, organism, genes, protein description, FUNCTION/SUBUNIT/COFACTOR/location
    comments and complete InterPro cross-references
  accessed_at: '2026-11-03T05:07:25.449404Z'
  snapshot_sha256: b6afcc94e603a5e6e59330d501cc9b5e551d6a8f75ae99f2a9970de2010ab2ff
  summary: Native reviewed Q56223 identifies nqo3 in taxon 300852; accession, role,
    location evidence attribution and family candidates checked within this annotated
    source.
  support: supports
- evidence_id: plaque-complex-i-agent-Q56220
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q56220.json
  locator: primaryAccession, organism, genes, protein description, FUNCTION/SUBUNIT/COFACTOR/location
    comments and complete InterPro cross-references
  accessed_at: '2026-11-03T05:07:25.456383Z'
  snapshot_sha256: fda7ee94d139ceed29ca6536ea2327f507089f8c38e4e57a3e17ee1798852f40
  summary: Native reviewed Q56220 identifies nqo4 in taxon 300852; accession, role,
    location evidence attribution and family candidates checked within this annotated
    source.
  support: supports
- evidence_id: plaque-complex-i-agent-Q56219
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q56219.json
  locator: primaryAccession, organism, genes, protein description, FUNCTION/SUBUNIT/COFACTOR/location
    comments and complete InterPro cross-references
  accessed_at: '2026-11-03T05:07:26.289644Z'
  snapshot_sha256: 558f1926ca287faa7c12df80990c104aefec4b6365361b4331f5acd513e308c4
  summary: Native reviewed Q56219 identifies nqo5 in taxon 300852; accession, role,
    location evidence attribution and family candidates checked within this annotated
    source.
  support: supports
- evidence_id: plaque-complex-i-agent-Q56218
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q56218.json
  locator: primaryAccession, organism, genes, protein description, FUNCTION/SUBUNIT/COFACTOR/location
    comments and complete InterPro cross-references
  accessed_at: '2026-11-03T05:07:26.311172Z'
  snapshot_sha256: 46722f4c655b655775989329970613c904bd4e858ce9f5fe75966ac9c0799bde
  summary: Native reviewed Q56218 identifies nqo6 in taxon 300852; accession, role,
    location evidence attribution and family candidates checked within this annotated
    source.
  support: supports
- evidence_id: plaque-complex-i-agent-Q56224
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q56224.json
  locator: primaryAccession, organism, genes, protein description, FUNCTION/SUBUNIT/COFACTOR/location
    comments and complete InterPro cross-references
  accessed_at: '2026-11-03T05:07:27.082435Z'
  snapshot_sha256: 49666b37f32e2ecb3d8d6fe41733347ed38eb8be989dca486f4bc535957838a7
  summary: Native reviewed Q56224 identifies nqo9 in taxon 300852; accession, role,
    location evidence attribution and family candidates checked within this annotated
    source.
  support: supports
- evidence_id: plaque-complex-i-agent-Q56217
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q56217.json
  locator: primaryAccession, organism, genes, protein description, FUNCTION/SUBUNIT/COFACTOR/location
    comments and complete InterPro cross-references
  accessed_at: '2026-11-03T05:07:27.104179Z'
  snapshot_sha256: 1e95b26ed571fb3b93ae9a02cf1b654a8c1906426aed66c22d0494a2aa9effb6
  summary: Native reviewed Q56217 identifies nqo7 in taxon 300852; accession, role,
    location evidence attribution and family candidates checked within this annotated
    source.
  support: supports
- evidence_id: plaque-complex-i-agent-Q56225
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q56225.json
  locator: primaryAccession, organism, genes, protein description, FUNCTION/SUBUNIT/COFACTOR/location
    comments and complete InterPro cross-references
  accessed_at: '2026-11-03T05:07:27.794458Z'
  snapshot_sha256: 5c166ed79a5e345a5b5476bf614f2117f07b2c1933c135415689793185c4b621
  summary: Native reviewed Q56225 identifies nqo10 in taxon 300852; accession, role,
    location evidence attribution and family candidates checked within this annotated
    source.
  support: supports
- evidence_id: plaque-complex-i-agent-Q56226
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q56226.json
  locator: primaryAccession, organism, genes, protein description, FUNCTION/SUBUNIT/COFACTOR/location
    comments and complete InterPro cross-references
  accessed_at: '2026-11-03T05:07:27.916254Z'
  snapshot_sha256: e091cd1aa3a6e985e00e7f48b68c8569965c521df87424d6dba9c2e561c4dd99
  summary: Native reviewed Q56226 identifies nqo11 in taxon 300852; accession, role,
    location evidence attribution and family candidates checked within this annotated
    source.
  support: supports
- evidence_id: plaque-complex-i-agent-Q56227
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q56227.json
  locator: primaryAccession, organism, genes, protein description, FUNCTION/SUBUNIT/COFACTOR/location
    comments and complete InterPro cross-references
  accessed_at: '2026-11-03T05:07:28.396974Z'
  snapshot_sha256: 9619291210f3795763fdfc70c2b846299f5a368664479325400dc1ae363fcd3e
  summary: Native reviewed Q56227 identifies nqo12 in taxon 300852; accession, role,
    location evidence attribution and family candidates checked within this annotated
    source.
  support: supports
- evidence_id: plaque-complex-i-agent-Q56228
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q56228.json
  locator: primaryAccession, organism, genes, protein description, FUNCTION/SUBUNIT/COFACTOR/location
    comments and complete InterPro cross-references
  accessed_at: '2026-11-03T05:07:28.502283Z'
  snapshot_sha256: 0a371f8f1ecaed6e9123c7e42e47932234b50159751f98a1886d587528a0bbd5
  summary: Native reviewed Q56228 identifies nqo13 in taxon 300852; accession, role,
    location evidence attribution and family candidates checked within this annotated
    source.
  support: supports
- evidence_id: plaque-complex-i-agent-Q56229
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q56229.json
  locator: primaryAccession, organism, genes, protein description, FUNCTION/SUBUNIT/COFACTOR/location
    comments and complete InterPro cross-references
  accessed_at: '2026-11-03T05:07:28.720466Z'
  snapshot_sha256: 7bbaeb9eed0029cbfdf9e53c21c2bd20956910320e42caf45ebb2260a9d6be68
  summary: Native reviewed Q56229 identifies nqo14 in taxon 300852; accession, role,
    location evidence attribution and family candidates checked within this annotated
    source.
  support: supports
- evidence_id: plaque-complex-i-agent-Q60019
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q60019.json
  locator: primaryAccession, organism, genes, protein description, FUNCTION/SUBUNIT/COFACTOR/location
    comments and complete InterPro cross-references
  accessed_at: '2026-11-03T05:07:29.689721Z'
  snapshot_sha256: d2c6eeb6c4cef280a32ab4be2bbee457fbbd771bf9f6e3b1967ce085dfd51764
  summary: Native reviewed Q60019 identifies nqo8 in taxon 300852; accession, role,
    location evidence attribution and family candidates checked within this annotated
    source.
  support: supports
- evidence_id: plaque-complex-i-agent-query-nqo
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene%3Anqo%2A%29%20AND%20%28organism_id%3A300852%29%20AND%20%28reviewed%3Atrue%29
  locator: results[].primaryAccession, genes, organism
  accessed_at: '2026-11-03T05:07:29.878176Z'
  snapshot_sha256: 1a49d555d0e684de6a1dee4efd0711b5a3e39b1a8f2c8ce23315ff94b78f4348
  summary: Native bounded query returns [('Q56221', 300852), ('Q56223', 300852), ('Q56218',
    300852), ('Q56224', 300852), ('Q56222', 300852), ('Q5SKZ7', 300852), ('Q56225',
    300852), ('Q56219', 300852), ('Q56220', 300852), ('Q56226', 300852), ('Q56228',
    300852), ('Q56229', 300852), ('Q60019', 300852), ('Q56217', 300852), ('Q56227',
    300852)].
  search_scope: UniProt REST; format=json&size=500&query=(gene:nqo*) AND (organism_id:300852)
    AND (reviewed:true); accessed 2026-11-03T05:07:29.878176Z; exact named gene/taxon
    criteria only.
  support: supports
- evidence_id: plaque-complex-i-agent-ipr-001750
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001750/
  locator: metadata.accession/type/name, integrated member signatures and description
  accessed_at: '2026-11-03T05:07:30.519261Z'
  snapshot_sha256: 750b245da5231826a6c4423122008e35d4d7460f51fbfa18754cca952021149b
  summary: Inspected domain IPR001750, NADH:quinone oxidoreductase/Mrp antiporter,
    transmembrane domain, against exact whole-component scope.
  support: supports
- evidence_id: plaque-complex-i-agent-ipr-006137
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006137/
  locator: metadata.accession/type/name, integrated member signatures and description
  accessed_at: '2026-11-03T05:07:30.552772Z'
  snapshot_sha256: 3b1cb07da540d4be40dd91a3669d8645931474c55adec9684d911276cd4ac9fc
  summary: Inspected domain IPR006137, NADH:ubiquinone oxidoreductase-like, 20kDa
    subunit, against exact whole-component scope.
  support: supports
- evidence_id: plaque-sdh-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0008177,GO:0045273,GO:0098803
  locator: results[].id/name/aspect/definition/isObsolete
  accessed_at: '2026-11-03T05:07:31.170244Z'
  snapshot_sha256: ce33121b76b994e5243ffe282c6d5b7b3c3c642d65bb785681c579e1a9b7b667
  summary: 'Current authority terms inspected: [(''GO:0045273'', ''respiratory chain
    complex II (succinate dehydrogenase)'', False), (''GO:0008177'', ''succinate dehydrogenase
    (quinone) activity'', False), (''GO:0098803'', ''respiratory chain complex'',
    False)]. Obsolete arm terms do not supply current exact component identities.'
  support: supports
- evidence_id: plaque-sdh-agent-tax-562
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562
  locator: taxId, scientificName and lineage
  accessed_at: '2026-11-03T05:07:31.197241Z'
  snapshot_sha256: ea038c30da3aab3426b7df16ce7a137cf2985e73d6ad8281971b9c390a74d2a8
  summary: Native taxonomy checks the exact organism/strain identifier; species-level
    deposited source and strain-specific examples remain distinct.
  support: supports
- evidence_id: plaque-sdh-agent-tax-83333
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333
  locator: taxId, scientificName and lineage
  accessed_at: '2026-11-03T05:07:31.789088Z'
  snapshot_sha256: f499fde9e4fcea85ff811b58a76a405669d32465a62eaf74240a48331b63d8e6
  summary: Native taxonomy checks the exact organism/strain identifier; species-level
    deposited source and strain-specific examples remain distinct.
  support: supports
- evidence_id: plaque-sdh-agent-P0AC41
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0AC41.json
  locator: primaryAccession, organism, genes, protein description, FUNCTION/SUBUNIT/COFACTOR/location
    comments and complete InterPro cross-references
  accessed_at: '2026-11-03T05:07:31.817530Z'
  snapshot_sha256: dd974a9bf8408ea362e9ac736d2c54fb179c9ec71e753aefdda9943218e22561
  summary: Native reviewed P0AC41 identifies sdhA in taxon 83333; accession, role,
    location evidence attribution and family candidates checked within this annotated
    source.
  support: supports
- evidence_id: plaque-sdh-agent-query-sdhA
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AsdhA%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29
  locator: results[].primaryAccession, genes, organism
  accessed_at: '2026-11-03T05:07:32.370491Z'
  snapshot_sha256: 1f2cfc59ff0d3fa0ad2703fafe26899f7598120362d6446eec48f44f0f31a3ea
  summary: Native bounded query returns [('P0AC41', 83333)].
  search_scope: UniProt REST; format=json&query=(gene_exact:sdhA) AND (organism_id:83333)
    AND (reviewed:true); accessed 2026-11-03T05:07:32.370491Z; exact named gene/taxon
    criteria only.
  support: supports
- evidence_id: plaque-sdh-agent-P07014
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P07014.json
  locator: primaryAccession, organism, genes, protein description, FUNCTION/SUBUNIT/COFACTOR/location
    comments and complete InterPro cross-references
  accessed_at: '2026-11-03T05:07:32.431577Z'
  snapshot_sha256: 0ab790707f2f780f7a2787ed1065de449585f5fb7d97d51e4672ca1e083b2736
  summary: Native reviewed P07014 identifies sdhB in taxon 83333; accession, role,
    location evidence attribution and family candidates checked within this annotated
    source.
  support: supports
- evidence_id: plaque-sdh-agent-query-sdhB
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AsdhB%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29
  locator: results[].primaryAccession, genes, organism
  accessed_at: '2026-11-03T05:07:32.645494Z'
  snapshot_sha256: a8decfb2a151fdd947d339e1b5997d58a0c9ff7def1969b040913b3a43a9ac09
  summary: Native bounded query returns [('P07014', 83333)].
  search_scope: UniProt REST; format=json&query=(gene_exact:sdhB) AND (organism_id:83333)
    AND (reviewed:true); accessed 2026-11-03T05:07:32.645494Z; exact named gene/taxon
    criteria only.
  support: supports
- evidence_id: plaque-sdh-agent-P69054
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P69054.json
  locator: primaryAccession, organism, genes, protein description, FUNCTION/SUBUNIT/COFACTOR/location
    comments and complete InterPro cross-references
  accessed_at: '2026-11-03T05:07:33.223797Z'
  snapshot_sha256: a861e4627427556398758d3c17389bc35671c262623fd9edd9d9a4d57bf696d1
  summary: Native reviewed P69054 identifies sdhC in taxon 83333; accession, role,
    location evidence attribution and family candidates checked within this annotated
    source.
  support: supports
- evidence_id: plaque-sdh-agent-query-sdhC
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AsdhC%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29
  locator: results[].primaryAccession, genes, organism
  accessed_at: '2026-11-03T05:07:33.286229Z'
  snapshot_sha256: 3be29b01ee51542249b33ba8fcede02afabe4cda988598d0f12e4004e0b628f6
  summary: Native bounded query returns [('P69054', 83333)].
  search_scope: UniProt REST; format=json&query=(gene_exact:sdhC) AND (organism_id:83333)
    AND (reviewed:true); accessed 2026-11-03T05:07:33.286229Z; exact named gene/taxon
    criteria only.
  support: supports
- evidence_id: plaque-sdh-agent-P0AC44
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0AC44.json
  locator: primaryAccession, organism, genes, protein description, FUNCTION/SUBUNIT/COFACTOR/location
    comments and complete InterPro cross-references
  accessed_at: '2026-11-03T05:07:33.708104Z'
  snapshot_sha256: 5993ab7762d4158d75a9b2798535745537aa8bb7a4b8592a3cc14fdbdefb057d
  summary: Native reviewed P0AC44 identifies sdhD in taxon 83333; accession, role,
    location evidence attribution and family candidates checked within this annotated
    source.
  support: supports
- evidence_id: plaque-sdh-agent-query-sdhD
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AsdhD%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29
  locator: results[].primaryAccession, genes, organism
  accessed_at: '2026-11-03T05:07:34.042715Z'
  snapshot_sha256: 1d1c674d03162fc285526244a3fadf841db347ce11abbf47b7f8fbdc7b90e8a6
  summary: Native bounded query returns [('P0AC44', 83333)].
  search_scope: UniProt REST; format=json&query=(gene_exact:sdhD) AND (organism_id:83333)
    AND (reviewed:true); accessed 2026-11-03T05:07:34.042715Z; exact named gene/taxon
    criteria only.
  support: supports
- evidence_id: plaque-sdh-agent-matches-P0AC41
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P0AC41/?page_size=200
  locator: Complete returned integrated InterPro entries for exact accession
  accessed_at: '2026-11-03T05:07:34.626340Z'
  snapshot_sha256: 8274cf4827b0355b467e34f081fef73b6792bf2166631bda0ca3fd2ee2eabc70
  summary: Current native protein-to-InterPro match list inspected, including the
    additional P07014 IPR050573 family. Matches are candidates, not automatic exact
    grounding.
  support: supports
- evidence_id: plaque-sdh-agent-matches-P07014
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P07014/?page_size=200
  locator: Complete returned integrated InterPro entries for exact accession
  accessed_at: '2026-11-03T05:07:34.748204Z'
  snapshot_sha256: bab7babafd234baa21b3d71e24fa6443e8b7a7371a957839d887d7cbde728b3c
  summary: Current native protein-to-InterPro match list inspected, including the
    additional P07014 IPR050573 family. Matches are candidates, not automatic exact
    grounding.
  support: supports
- evidence_id: plaque-sdh-agent-matches-P69054
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P69054/?page_size=200
  locator: Complete returned integrated InterPro entries for exact accession
  accessed_at: '2026-11-03T05:07:34.820704Z'
  snapshot_sha256: 189f2eec401afa419d2fb1778284ec73cc8bbb9b1fffd4b4ab507fc034645800
  summary: Current native protein-to-InterPro match list inspected, including the
    additional P07014 IPR050573 family. Matches are candidates, not automatic exact
    grounding.
  support: supports
- evidence_id: plaque-sdh-agent-matches-P0AC44
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P0AC44/?page_size=200
  locator: Complete returned integrated InterPro entries for exact accession
  accessed_at: '2026-11-03T05:07:35.799671Z'
  snapshot_sha256: 1ce420bbd621053ef31a694288f3a3a402b643bb591745967dc595bb04534e96
  summary: Current native protein-to-InterPro match list inspected, including the
    additional P07014 IPR050573 family. Matches are candidates, not automatic exact
    grounding.
  support: supports
- evidence_id: plaque-sdh-agent-IPR011281
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR011281/
  locator: metadata.accession/type/name, integrated member signatures and description
  accessed_at: '2026-11-03T05:07:35.824234Z'
  snapshot_sha256: 1af86e373e062b9a8d4461556d679cd22b9266ce7e295b5cf56ba530e5787fa9
  summary: Inspected family IPR011281, Succinate dehydrogenase, flavoprotein subunit,
    against exact whole-component scope.
  support: supports
- evidence_id: plaque-sdh-agent-IPR014006
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR014006/
  locator: metadata.accession/type/name, integrated member signatures and description
  accessed_at: '2026-11-03T05:07:35.849070Z'
  snapshot_sha256: 98addafe843653636aafa954821cc9126e53ae8d87669d6ceb3debf304347fe9
  summary: Inspected family IPR014006, Succinate dehydrogenase/fumarate reductase,
    flavoprotein subunit, against exact whole-component scope.
  support: supports
- evidence_id: plaque-sdh-agent-IPR030664
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR030664/
  locator: metadata.accession/type/name, integrated member signatures and description
  accessed_at: '2026-11-03T05:07:35.990019Z'
  snapshot_sha256: 03a1506a2c0c2378f7a2c4923f6e160036c42080411192aa59051bb76ffb71a4
  summary: Inspected family IPR030664, FAD-dependent oxidoreductase SdhA/FrdA/AprA,
    against exact whole-component scope.
  support: supports
- evidence_id: plaque-sdh-agent-IPR065464
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR065464/
  locator: metadata.accession/type/name, integrated member signatures and description
  accessed_at: '2026-11-03T05:07:36.736307Z'
  snapshot_sha256: 41dc0a638addd973d1546cfb086d0c2d3e3090c9b0f52c1ddf9fa232e16903ca
  summary: Inspected family IPR065464, Succinate dehydrogenase hydrophobic membrane
    anchor subunit, against exact whole-component scope.
  support: supports
- evidence_id: plaque-sdh-agent-pdb-1NEK
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/entry/1NEK
  locator: struct.title, primary citation, resolution and polymer identities
  accessed_at: '2026-11-03T05:07:37.042133Z'
  snapshot_sha256: 914721e829789202d7e7c2a2285bb956ac9e53a5290ff0ef0fe098b91c7f094e
  summary: Deposited structure Complex II (Succinate Dehydrogenase) From E. Coli with
    ubiquinone bound; native primary citation and structure identifiers checked, without
    raw-coordinate reanalysis.
  support: supports
- evidence_id: plaque-sdh-agent-assembly-1NEK
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/assembly/1NEK/1
  locator: pdbx_struct_assembly and rcsb_assembly_info
  accessed_at: '2026-11-03T05:07:37.068224Z'
  snapshot_sha256: a38b4de61bb4f1e282d0fba783ff44d64e6e8a78143e8a905d879a7cabc28dfa
  summary: Biological assembly annotation is tetrameric with 4 protein instances.
    This deposited annotation is not an independent in-cell stoichiometry measurement.
  support: supports
- evidence_id: plaque-sdh-agent-1NEK-entity-1
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/1NEK/1
  locator: rcsb_polymer_entity, source organism and SIFTS reference identifiers
  accessed_at: '2026-11-03T05:07:37.131232Z'
  snapshot_sha256: fb9a9dcbfe0b21e3c3ff978d3ab9c59145afead9633344d5939cc26b433cc28c
  summary: 'Deposited polymer identity and reference mapping inspected: [(''P0AC41'',
    1.0)]. Source taxon [562]. No coordinate reanalysis.'
  support: supports
- evidence_id: plaque-sdh-agent-1NEK-entity-2
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/1NEK/2
  locator: rcsb_polymer_entity, source organism and SIFTS reference identifiers
  accessed_at: '2026-11-03T05:07:37.138638Z'
  snapshot_sha256: b0aa737d0e82b74785dac73142546fdbc7128fe0901b42ab12478d745f4c96ae
  summary: 'Deposited polymer identity and reference mapping inspected: [(''P07014'',
    1.0)]. Source taxon [562]. No coordinate reanalysis.'
  support: supports
- evidence_id: plaque-sdh-agent-1NEK-entity-3
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/1NEK/3
  locator: rcsb_polymer_entity, source organism and SIFTS reference identifiers
  accessed_at: '2026-11-03T05:07:37.189624Z'
  snapshot_sha256: 058981359863f7960ec319905bdfa92739bca3f97c4c9ebf501a75381cab3386
  summary: 'Deposited polymer identity and reference mapping inspected: [(''P69054'',
    1.0)]. Source taxon [562]. No coordinate reanalysis.'
  support: supports
- evidence_id: plaque-sdh-agent-1NEK-entity-4
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/1NEK/4
  locator: rcsb_polymer_entity, source organism and SIFTS reference identifiers
  accessed_at: '2026-11-03T05:07:37.226985Z'
  snapshot_sha256: 6d7f8840d13e6f7ede1ec1244271d3fa863a478534cd739f37d27b4cf24b44dc
  summary: 'Deposited polymer identity and reference mapping inspected: [(''P0AC44'',
    1.0)]. Source taxon [562]. No coordinate reanalysis.'
  support: supports
- evidence_id: plaque-sdh-agent-pmid-12560550
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID:12560550%20AND%20SRC:MED
  locator: Europe PMC publication metadata and abstract
  accessed_at: '2026-11-03T05:07:37.283226Z'
  snapshot_sha256: 7421eb54c7b6796349ede318f6198c5ff062ea07f13c1198b580acb6d5ac8513
  summary: Fresh title/author/DOI/PMID and abstract inspected. Full-text access is
    only claimed for separately identified body evidence.
  support: supports
- evidence_id: plaque-sdh-agent-pmid-15919996
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID:15919996%20AND%20SRC:MED
  locator: Europe PMC publication metadata and abstract
  accessed_at: '2026-11-03T05:07:37.319039Z'
  snapshot_sha256: bf238a68f2eaffe3abc2659ccf4a6bdd1cc0660ac62559a2661c58032d4502f5
  summary: Fresh title/author/DOI/PMID and abstract inspected. Full-text access is
    only claimed for separately identified body evidence.
  support: supports
- evidence_id: plaque-sdh-agent-pmid-16079137
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID:16079137%20AND%20SRC:MED
  locator: Europe PMC publication metadata and abstract
  accessed_at: '2026-11-03T05:07:37.342700Z'
  snapshot_sha256: cf1c57d1a5343edc60d65a0b5d128f9d7b78f0006ac9526b7a31be6d9945918a
  summary: Fresh title/author/DOI/PMID and abstract inspected. Full-text access is
    only claimed for separately identified body evidence.
  support: supports
- evidence_id: plaque-adapter-datasets
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Complete public dataset catalogue, all organism and dataset labels
  accessed_at: '2026-11-03T05:07:37.840201Z'
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  summary: Catalogue covers E.coli, including precise_mg1655. No Methanothermobacter
    marburgensis or Thermus thermophilus dataset is listed; the listed Sulfolobus
    archaeal datasets do not match the methanogen target. Absence is bounded to this
    retrieved catalogue.
  support: supports
- evidence_id: plaque-adapter-frontend
  kind: database
  reference: https://imodulondb.org/assets/index-3_RVHvkS.js
  locator: Public frontend route declarations for dataset, gene search, gene-to-module
    membership and module member tables
  accessed_at: '2026-11-03T05:07:37.912910Z'
  snapshot_sha256: 64c73f41c40268c8d5da3e8a10ef12bd9ef948e2bd2595e62f5a16409d0df1b9
  summary: Read-only public source routes inspected; no authentication or mutation
    route was used.
  support: supports
- evidence_id: plaque-adapter-meta
  kind: database
  reference: https://imodulondb.org/api/datasets/e_coli/precise_mg1655/meta
  locator: organism, dataset, strains, sample/condition/module counts, publication_url
  accessed_at: '2026-11-03T05:08:42.830070Z'
  snapshot_sha256: 0722bb1ccec69ac0d7ebc2784fc7cbdf1cfe612d739b8fb66d54a441a8b3db91
  summary: Selected E.coli precise_mg1655 dataset identifies MG1655,586 samples,281
    conditions and115 modules; publication_url is null. This is dataset coverage,
    not structural evidence.
  support: supports
- evidence_id: plaque-adapter-search-sdhA
  kind: search
  reference: https://imodulondb.org/api/search?organism=e_coli&dataset=precise_mg1655&query=sdhA&limit=50
  locator: Returned genes and imodulons arrays
  accessed_at: '2026-11-03T05:08:42.830285Z'
  snapshot_sha256: cf152ea7e41e5275cab8c2d18c5040396e67f3d0c280a4438b3055f5cf9fed12
  summary: Exact sdhA search resolves [('b0723', 'sdhA')]. Memberships were checked
    separately.
  search_scope: iModulonDB public search API; organism=e_coli; dataset=precise_mg1655;
    query=sdhA; limit=50; accessed 2026-11-03T05:08:42.830285Z; one dataset only.
  support: supports
- evidence_id: plaque-adapter-search-sdhB
  kind: search
  reference: https://imodulondb.org/api/search?organism=e_coli&dataset=precise_mg1655&query=sdhB&limit=50
  locator: Returned genes and imodulons arrays
  accessed_at: '2026-11-03T05:08:42.830391Z'
  snapshot_sha256: 491b18f13c4312a2f9d8a8c58050dfce9698fe707ad200b3391c4b4c1c8b25cc
  summary: Exact sdhB search resolves [('b0724', 'sdhB')]. Memberships were checked
    separately.
  search_scope: iModulonDB public search API; organism=e_coli; dataset=precise_mg1655;
    query=sdhB; limit=50; accessed 2026-11-03T05:08:42.830391Z; one dataset only.
  support: supports
- evidence_id: plaque-adapter-search-sdhC
  kind: search
  reference: https://imodulondb.org/api/search?organism=e_coli&dataset=precise_mg1655&query=sdhC&limit=50
  locator: Returned genes and imodulons arrays
  accessed_at: '2026-11-03T05:08:42.830445Z'
  snapshot_sha256: 130638ad02f6134043ecf6d52bf8a352a177b1b46c6e420aa14ab9542d4be227
  summary: Exact sdhC search resolves [('b0721', 'sdhC')]. Memberships were checked
    separately.
  search_scope: iModulonDB public search API; organism=e_coli; dataset=precise_mg1655;
    query=sdhC; limit=50; accessed 2026-11-03T05:08:42.830445Z; one dataset only.
  support: supports
- evidence_id: plaque-adapter-search-sdhD
  kind: search
  reference: https://imodulondb.org/api/search?organism=e_coli&dataset=precise_mg1655&query=sdhD&limit=50
  locator: Returned genes and imodulons arrays
  accessed_at: '2026-11-03T05:08:42.930390Z'
  snapshot_sha256: b304f8cdbce5c97aee510fd46ebf5661e204f1d315b74ed595859a06c75fc40f
  summary: Exact sdhD search resolves [('b0722', 'sdhD')]. Memberships were checked
    separately.
  search_scope: iModulonDB public search API; organism=e_coli; dataset=precise_mg1655;
    query=sdhD; limit=50; accessed 2026-11-03T05:08:42.930390Z; one dataset only.
  support: supports
- evidence_id: plaque-mcr-agent-IPR003178-retry
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR003178/
  locator: metadata.accession/type/name, integrated member signatures and description
  accessed_at: '2026-11-03T05:08:42.933067Z'
  snapshot_sha256: 238db841c9851499923ea9e44034ae800965432cbdec3bd39deef91e14879263
  summary: Inspected family IPR003178, Methyl-coenzyme M reductase, gamma subunit,
    against exact whole-component scope.
  support: supports
- evidence_id: plaque-sdh-agent-IPR004489-retry
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004489/
  locator: metadata.accession/type/name, integrated member signatures and description
  accessed_at: '2026-11-03T05:08:42.934325Z'
  snapshot_sha256: f5209b776ca14700e78ca9330b389e07a61e46b0aea6fae21c6d558cdd1c58a7
  summary: Inspected family IPR004489, Succinate dehydrogenase/fumarate reductase
    iron-sulphur protein, against exact whole-component scope.
  support: supports
- evidence_id: plaque-sdh-agent-IPR014314-retry
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR014314/
  locator: metadata.accession/type/name, integrated member signatures and description
  accessed_at: '2026-11-03T05:08:42.991639Z'
  snapshot_sha256: 3405c338c549cf5d8432d424e7615fcae9b97b062cb9a707b1deba3dad5dbd0a
  summary: Inspected family IPR014314, Succinate dehydrogenase, cytochrome b556 subunit,
    against exact whole-component scope.
  support: supports
- evidence_id: plaque-sdh-agent-IPR014312-retry
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR014312/
  locator: metadata.accession/type/name, integrated member signatures and description
  accessed_at: '2026-11-03T05:08:43.423673Z'
  snapshot_sha256: bb62534fdf2691d88a787eb05e6650f54f4f62490a8c0026aaeb61fc9055dd93
  summary: Inspected family IPR014312, Succinate dehydrogenase, hydrophobic membrane
    anchor, against exact whole-component scope.
  support: supports
- evidence_id: plaque-adapter-gene-modules-sdhC
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise_mg1655/b0721/imodulons
  locator: All returned membership flags, weights and thresholds for sdhC
  accessed_at: '2026-11-03T05:11:07.858191Z'
  snapshot_sha256: 054f6791b9a11dc635870e4b6ab84c873eeceec495ae912944a0ad958542d863
  summary: 'Thresholded memberships (k,name,weight): [(1, ''Crp'', ''0.113468878''),
    (14, ''ArcA-1'', ''0.110789085''), (10, ''ArcA-2'', ''0.081351196'')]. Below-threshold
    membership is not evidence against physical complex membership.'
  support: supports
- evidence_id: plaque-adapter-gene-modules-sdhA
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise_mg1655/b0723/imodulons
  locator: All returned membership flags, weights and thresholds for sdhA
  accessed_at: '2026-11-03T05:11:07.859195Z'
  snapshot_sha256: de4b4f4c82276bff068a40e154890bb2d095634d0c568f5b231f32982f7df5ac
  summary: 'Thresholded memberships (k,name,weight): [(10, ''ArcA-2'', ''0.109620945''),
    (1, ''Crp'', ''0.096358976''), (14, ''ArcA-1'', ''0.079630832'')]. Below-threshold
    membership is not evidence against physical complex membership.'
  support: supports
- evidence_id: plaque-adapter-gene-modules-sdhB
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise_mg1655/b0724/imodulons
  locator: All returned membership flags, weights and thresholds for sdhB
  accessed_at: '2026-11-03T05:11:07.859455Z'
  snapshot_sha256: 8293441b51ff89bb500f535d3b87618797e839f3ff87240d54808eea7c0365c0
  summary: 'Thresholded memberships (k,name,weight): [(10, ''ArcA-2'', ''0.10452537''),
    (1, ''Crp'', ''0.097856111'')]. Below-threshold membership is not evidence against
    physical complex membership.'
  support: supports
- evidence_id: plaque-adapter-gene-modules-sdhD
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise_mg1655/b0722/imodulons
  locator: All returned membership flags, weights and thresholds for sdhD
  accessed_at: '2026-11-03T05:11:07.861735Z'
  snapshot_sha256: 5896bc29fb411085e46a953b34abd281822550182f430a79e6da0d2d38343198
  summary: 'Thresholded memberships (k,name,weight): [(14, ''ArcA-1'', ''0.100289611''),
    (1, ''Crp'', ''0.09939565''), (10, ''ArcA-2'', ''0.088084304'')]. Below-threshold
    membership is not evidence against physical complex membership.'
  support: supports
- evidence_id: plaque-sdh-agent-IPR050573
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050573/
  locator: metadata.type/name, integrated PANTHER PTHR11921, description provenance
    flags
  accessed_at: '2026-11-03T05:11:08.309942Z'
  snapshot_sha256: e45bd3bbc31d9bbb21eec4371a19aa219458cfc06caea922d000179721f01ee0
  summary: Current P07014 match is a family explicitly named Succinate Dehydrogenase/Fumarate
    Reductase Iron-Sulfur. Its description is flagged LLM-generated and unchecked
    and was not used as biological evidence; the broad integrated family label does
    not establish exact SdhB-only equivalence.
  support: supports
- evidence_id: plaque-adapter-summary-1
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise_mg1655/1
  locator: k, imodulon_name, regulator, function_description, n_genes, threshold
  accessed_at: '2026-11-03T05:11:20.400056Z'
  snapshot_sha256: 6bb0d8f1326488b63ed7c71b810d643cc8886bac2b26cbbeaeed79f8fc933889
  summary: Native module 1 (Crp) has 32 thresholded genes; threshold 0.068750263;
    source annotation carbohydrate transport and metabolism. AI-generated narrative
    and activity matrices were excluded from biological inference.
  support: supports
- evidence_id: plaque-adapter-members-1
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise_mg1655/1/genes?limit=50
  locator: genes[].gene_id/gene_name/weight/in_imodulon/uniprot_id; request limit=50
  accessed_at: '2026-11-03T05:11:20.401335Z'
  snapshot_sha256: 9771a7b5bbcb5d97a79334b17f97d3961dfffb453bfc8a92472a6187841e62b6
  summary: Inspected all 32 returned member identifier/weight rows and matched the
    Sdh components; observed [('sdhC', 'P69054'), ('sdhD', 'P0AC44'), ('sdhB', 'P07014'),
    ('sdhA', 'P0AC41')]. No physical assembly or causal claim is inferred.
  support: supports
- evidence_id: plaque-adapter-summary-10
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise_mg1655/10
  locator: k, imodulon_name, regulator, function_description, n_genes, threshold
  accessed_at: '2026-11-03T05:11:20.402970Z'
  snapshot_sha256: c93436092d97c6e9e35b5aa320317d8a59bd43977d73802cf629a307835a48b8
  summary: Native module 10 (ArcA-2) has 37 thresholded genes; threshold 0.061542713;
    source annotation anaerobiosis/repression of aerobic growth genes during anaerobic
    growth. AI-generated narrative and activity matrices were excluded from biological
    inference.
  support: supports
- evidence_id: plaque-adapter-members-10
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise_mg1655/10/genes?limit=50
  locator: genes[].gene_id/gene_name/weight/in_imodulon/uniprot_id; request limit=50
  accessed_at: '2026-11-03T05:11:20.404285Z'
  snapshot_sha256: 43864d57c4c320453f54af349354f3c8ceead86b1e53daa8eda067c5b5c7cc88
  summary: Inspected all 37 returned member identifier/weight rows and matched the
    Sdh components; observed [('sdhA', 'P0AC41'), ('sdhB', 'P07014'), ('sdhD', 'P0AC44'),
    ('sdhC', 'P69054')]. No physical assembly or causal claim is inferred.
  support: supports
- evidence_id: plaque-adapter-summary-14
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise_mg1655/14
  locator: k, imodulon_name, regulator, function_description, n_genes, threshold
  accessed_at: '2026-11-03T05:11:20.501581Z'
  snapshot_sha256: 9fa4b1a902d1e11c5f0508a460cd86aad15f1763adc9775cedeecfdd012ebf40
  summary: Native module 14 (ArcA-1) has 23 thresholded genes; threshold 0.07235406;
    source annotation anaerobiosis/repression of aerobic growth genes during anaerobic
    growth. AI-generated narrative and activity matrices were excluded from biological
    inference.
  support: supports
- evidence_id: plaque-adapter-members-14
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise_mg1655/14/genes?limit=50
  locator: genes[].gene_id/gene_name/weight/in_imodulon/uniprot_id; request limit=50
  accessed_at: '2026-11-03T05:11:20.509325Z'
  snapshot_sha256: 12810762cc0ddeca83081b14bf425e6461eea5a5f95c3d62addc5282ebf1c2c5
  summary: Inspected all 23 returned member identifier/weight rows and matched the
    Sdh components; observed [('sdhC', 'P69054'), ('sdhD', 'P0AC44'), ('sdhA', 'P0AC41')].
    No physical assembly or causal claim is inferred.
  support: supports
- evidence_id: plaque-mcr-primary-browser
  kind: primary_source
  reference: https://go.gale.com/ps/i.do?asid=294e1b4d&id=GALE%7CA20105096&it=r&p=AONE&u=googlescholar&v=2.1
  locator: Fresh browser-extracted Ermler1997 primary transcription, claim-bearing
    structure/reaction paragraphs36-77
  accessed_at: '2026-11-03T05:07:50.575Z'
  snapshot_sha256: ea95dfa5ef483644548aaae0799067a45c8b20af0045858b5a826de80f95d609
  summary: Primary article transcription supports alpha2beta2gamma2 architecture and
    two F430 sites. Crystals were inactive enzyme states; the mechanistic proposal
    is not a direct observation of active turnover. Hash binds serialized browser
    extraction, not publisher PDF bytes.
  support: supports
- evidence_id: plaque-sdh-stenberg-browser
  kind: primary_source
  reference: https://doi.org/10.1074/jbc.M506479200
  locator: Fresh indexed publisher Methods passages; full-page browser open failed500
  accessed_at: '2026-11-03T05:09:04.810Z'
  snapshot_sha256: 29e08c25939ad9e1907b32a2bb0c058b6ddbb0e33cfe177f7411214dd87f69e1
  summary: Inspected indexed primary Methods describing BL21(DE3)pLysS cultures and
    membrane preparation/BN-PAGE. This pass did not independently reread the Sdh result
    subsection or figure pixels; native UniProt separately verifies citation attribution.
    Hash binds serialized browser results, not a complete publisher body.
  support: supports
- evidence_id: plaque-current-0
  kind: record_content
  reference: data/structures/energy_complex/methyl_coenzyme_m_reductase_complex.yaml
  locator: Entire current record and causal graph/history
  accessed_at: '2026-11-03T05:13:25.804168Z'
  snapshot_sha256: 369ad320d4bc19c72a79fb14037b46c5e12f6eddaa64bd0bb04572e9a8ea685e
  summary: Stale frozen target compared with current bytes and substantively reassessed;
    the original historical input attestation remains unchanged.
  support: supports
- evidence_id: plaque-original-0
  kind: prior_review
  reference: reviews/structured/20261021T091345Z-methyl-coenzyme-m-reductase-complex-audit/review.yaml
  locator: Original whole review, findings, assessments and limitations
  accessed_at: '2026-11-03T05:13:25.804168Z'
  snapshot_sha256: 10c87a197c78b725f0a92b31d638ef50bca24fe5837e7a59c3660804cae4b089
  summary: Original qualified pass has no findings; historical native validation,
    Markdown render and frozen input hashes independently pass.
  support: supports
- evidence_id: plaque-current-1
  kind: record_content
  reference: data/structures/energy_complex/respiratory_chain_complex_i.yaml
  locator: Entire current record and causal graph/history
  accessed_at: '2026-11-03T05:13:25.804168Z'
  snapshot_sha256: 0d0f4b5c3346e25dbbd3595d959c03d40dc9943e3e6055dcca3746fd4bf67540
  summary: Stale frozen target compared with current bytes and substantively reassessed;
    the original historical input attestation remains unchanged.
  support: supports
- evidence_id: plaque-original-1
  kind: prior_review
  reference: reviews/structured/20261021T091350Z-respiratory-chain-complex-i-audit/review.yaml
  locator: Original whole review, findings, assessments and limitations
  accessed_at: '2026-11-03T05:13:25.804168Z'
  snapshot_sha256: 40d426bae2756cbf27bea5822fa3e323eebe2d00fce3e53716ad33584aa52ae8
  summary: Original qualified pass has no findings; historical native validation,
    Markdown render and frozen input hashes independently pass.
  support: supports
- evidence_id: plaque-current-2
  kind: record_content
  reference: data/structures/energy_complex/respiratory_chain_complex_ii_succinate_dehydrogenase.yaml
  locator: Entire current record and causal graph/history
  accessed_at: '2026-11-03T05:13:25.804168Z'
  snapshot_sha256: 4e6914fa2c29221809c1a172d98aa541c5adc01bc5090cc8c0eb55b56a3d463d
  summary: Stale frozen target compared with current bytes and substantively reassessed;
    the original historical input attestation remains unchanged.
  support: supports
- evidence_id: plaque-original-2
  kind: prior_review
  reference: reviews/structured/20261021T091351Z-respiratory-chain-complex-ii-succinate-dehydrogenase-audit/review.yaml
  locator: Original whole review, findings, assessments and limitations
  accessed_at: '2026-11-03T05:13:25.804168Z'
  snapshot_sha256: 7d846c8c936360c7e05a670be52a0c1bc49a444e40d4c21f9ce044bba8c49d1a
  summary: Original qualified pass has no findings; historical native validation,
    Markdown render and frozen input hashes independently pass.
  support: supports
- evidence_id: plaque-mcr-category-prior
  kind: prior_review
  reference: reviews/structured/20261025T071006Z-energy-complex-category-review/review.yaml
  locator: F2; exact category review identity, affected target and grounding field
    paths
  accessed_at: '2026-11-03T05:13:25.804168Z'
  snapshot_sha256: e711d5f5b710f0bf33facd08863a8d1e206b2d0a185906a359acbd886a728146
  summary: Prior minor finding identifies three omitted component-ref node groundings.
    Current record has all three corresponding verified InterPro values. The root
    confirms associated issue2432 was already closed; no record repair is attributed
    to PR2351.
  support: supports
- evidence_id: plaque-original-validation
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2351/adversary-plaque/original-validation.json
  locator: Original three native validate/render and historical input hash checks
  accessed_at: '2026-11-03T05:13:25.804168Z'
  snapshot_sha256: 07b6a5ac38d6c96c47c7a7b75a43db981c1bb254f1c94b949e230134cf5020c9
  summary: All three original bundle validation/render/hash checks pass against their
    historical revisions.
  support: supports
- evidence_id: plaque-mcr-native-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2351/mcr-uniprot-verify-receipt.json
  locator: Complete receipt and linked log; stdout SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T05:15:03.221010Z'
  snapshot_sha256: 0e8aa8eb8ebb3d434377d1aa7c89810c3d97ea1da1b05ad522e1cb628f0f7bb4
  summary: 'Root-executed native verifier passes: all current UniProtKB protein_examples
    and causal graph xrefs verified. Independently inspected receipt and log; this
    reviewer did not rerun the command.'
  support: supports
- evidence_id: plaque-mcr-native-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2351/mcr-uniprot-causal-receipt.json
  locator: Complete receipt and linked log; stdout SHA256 8076de7f3af7f26f94f4ebdd894d164d3ffff744f5afc092ba8cd60e97cc1798
  accessed_at: '2026-11-03T05:15:03.732493Z'
  snapshot_sha256: e9a31456475ddb2270a394877c601396a55cab9e3f221f9240080ff75ef705c9
  summary: 'Root-executed native causal graph audit passes: 3 GENE_OR_PROTEIN nodes
    COVERED; all other reported categories zero. Coverage means examples cover declared
    gene symbols, not experimental assembly necessity. Independently inspected receipt
    and log; this reviewer did not rerun the command.'
  support: supports
- evidence_id: plaque-complex-i-native-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2351/complex-i-uniprot-verify-receipt.json
  locator: Complete receipt and linked log; stdout SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T05:15:05.304542Z'
  snapshot_sha256: 95281c23ec3d01aa16d41e8372fe47efe0862bdcb793a07a89380332e872b086
  summary: 'Root-executed native verifier passes: all current UniProtKB protein_examples
    and causal graph xrefs verified. Independently inspected receipt and log; this
    reviewer did not rerun the command.'
  support: supports
- evidence_id: plaque-complex-i-native-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2351/complex-i-uniprot-causal-receipt.json
  locator: Complete receipt and linked log; stdout SHA256 633f42f63c3f46c078be270a8917a0d33c4e99bf9677469acf36fd3061d11a35
  accessed_at: '2026-11-03T05:15:05.788014Z'
  snapshot_sha256: 055764f5f39eccaf643387880dc871d230616e3b25c69119c3bb222ff95c9b4b
  summary: 'Root-executed native causal graph audit passes: 2 GENE_OR_PROTEIN nodes
    COVERED; all other reported categories zero. Coverage means examples cover declared
    gene symbols, not experimental assembly necessity. Independently inspected receipt
    and log; this reviewer did not rerun the command.'
  support: supports
- evidence_id: plaque-complex-ii-native-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2351/complex-ii-uniprot-verify-receipt.json
  locator: Complete receipt and linked log; stdout SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T05:15:07.018777Z'
  snapshot_sha256: 177e0444fe0168d08eee4fbd31ced20e630821523d7077b90c4f8d3f535aa5d2
  summary: 'Root-executed native verifier passes: all current UniProtKB protein_examples
    and causal graph xrefs verified. Independently inspected receipt and log; this
    reviewer did not rerun the command.'
  support: supports
- evidence_id: plaque-complex-ii-native-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2351/complex-ii-uniprot-causal-receipt.json
  locator: Complete receipt and linked log; stdout SHA256 80d0a4439ebf3fc5efc9c149ca8dd16309e5c2482d4a18223120024cb5e555d1
  accessed_at: '2026-11-03T05:15:07.570151Z'
  snapshot_sha256: 4ab13d37a899ccf7400534f59d80dd645de13159b6d697d3208dc1a43781a6a4
  summary: 'Root-executed native causal graph audit passes: 3 GENE_OR_PROTEIN nodes
    COVERED; all other reported categories zero. Coverage means examples cover declared
    gene symbols, not experimental assembly necessity. Independently inspected receipt
    and log; this reviewer did not rerun the command.'
  support: supports
- evidence_id: micro-record-psii
  kind: record_content
  reference: data/structures/energy_complex/photosystem_ii.yaml
  locator: Entire current maintained YAML, including provenance, discussions, component
    examples and all graph edges.
  accessed_at: '2026-11-03T05:16:30.397073Z'
  snapshot_sha256: fc05496451f76ed16643edb2ca590803fd07569abfe432111e31314375687a16
  summary: Current source-head input; SHA matches native inspect. Target bytes unchanged
    since the original frozen review.
  support: supports
- evidence_id: micro-prior-psii
  kind: prior_review
  reference: reviews/structured/20261021T091346Z-photosystem-ii-audit/review.yaml
  locator: Original full YAML assessments, checks, evidence access scopes, findings/actions
    and source hashes; paired Markdown checked by native renderer.
  accessed_at: '2026-11-03T05:16:30.397073Z'
  snapshot_sha256: 5138fd0d9d80523573027ab48105acfc6915554a6ecacb5bf8aa6e8cfccc17b2
  summary: Historical original preserved. Its timestamps/checks are historical, not
    newly executed. Original disposition is retained only where freshly supported.
  support: supports
- evidence_id: micro-record-rod
  kind: record_content
  reference: data/structures/energy_complex/phycobilisome_rod.yaml
  locator: Entire current maintained YAML, including provenance, discussions, component
    examples and all graph edges.
  accessed_at: '2026-11-03T05:16:30.397073Z'
  snapshot_sha256: f610a707b8f8fea3edfd28574b996a315eaf1e2d245de7efce9edf96b49943d1
  summary: 'Current source-head input; SHA matches native inspect. Changed since original:
    one CpcD identity-only example and its curation event were added.'
  support: supports
- evidence_id: micro-prior-rod
  kind: prior_review
  reference: reviews/structured/20261021T091347Z-phycobilisome-rod-audit/review.yaml
  locator: Original full YAML assessments, checks, evidence access scopes, findings/actions
    and source hashes; paired Markdown checked by native renderer.
  accessed_at: '2026-11-03T05:16:30.397073Z'
  snapshot_sha256: 5de19cc2aeb828652a3d90d22d578645985e8259bd6206abb59e62ecdf11daf9
  summary: Historical original preserved. Its timestamps/checks are historical, not
    newly executed. Original F1 remains open and current example additions require
    reassessment.
  support: supports
- evidence_id: micro-record-bacterial-psii
  kind: record_content
  reference: data/structures/energy_complex/plasma_membrane_derived_thylakoid_photosystem_ii.yaml
  locator: Entire current maintained YAML, including provenance, discussions, component
    examples and all graph edges.
  accessed_at: '2026-11-03T05:16:30.397073Z'
  snapshot_sha256: 7629a2480ce3d823e87431d0c26be93c45101095021fd60087301f5f1d9a58ef
  summary: Current source-head input; SHA matches native inspect. Target bytes unchanged
    since the original frozen review.
  support: supports
- evidence_id: micro-prior-bacterial-psii
  kind: prior_review
  reference: reviews/structured/20261021T091348Z-plasma-membrane-derived-thylakoid-photosystem-ii-audit/review.yaml
  locator: Original full YAML assessments, checks, evidence access scopes, findings/actions
    and source hashes; paired Markdown checked by native renderer.
  accessed_at: '2026-11-03T05:16:30.397073Z'
  snapshot_sha256: c60ea9147f742d25275b0dff673fc6957fc7497b55ee1862482c20358b2333b4
  summary: Historical original preserved. Its timestamps/checks are historical, not
    newly executed. Original disposition is retained only where freshly supported.
  support: supports
- evidence_id: micro-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Evidence rules and Components, especially label-only grounding and assembly
    essentiality.
  accessed_at: '2026-11-03T05:16:30.397073Z'
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
  summary: Known component membership may be represented without guessed family identifiers;
    essentiality concerns structure formation, not organism viability.
  support: supports
- evidence_id: micro-protein-policy
  kind: authority
  reference: .claude/skills/uniprot-protein-examples/SKILL.md
  locator: Rules 2–5 and read-only verify/causal audit.
  accessed_at: '2026-11-03T05:16:30.397073Z'
  snapshot_sha256: 6462894c8257823bae2b175c34693cd42f11ff9269a3829c15b9286ba6d7c876
  summary: Exact native gene/ORF and taxon/status checks are distinct from support
    for literature-symbol mapping and experimental membership.
  support: supports
- evidence_id: micro-adapter-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Structured Source Cross-Checks.
  accessed_at: '2026-11-03T05:16:30.397073Z'
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
  summary: Named genes, proteins and pathways trigger catalogue applicability and
    bounded covered-dataset checks; expression modules do not prove structure membership.
  support: supports
- evidence_id: micro-local-core
  kind: record_content
  reference: data/structures/energy_complex/phycobilisome_core.yaml
  locator: Identifier, label, definition, parent_structures and part_of only.
  accessed_at: '2026-11-03T05:16:30.397073Z'
  snapshot_sha256: 34cca2a846f5b2b84b95c6c2db929370814b4e2898eee052f3e2cbfecafde554
  summary: The rod graph reference resolves to the distinct central allophycocyanin
    core. No independent full review of this neighboring record is claimed.
  support: supports
- evidence_id: micro-native-verifier
  kind: authority
  reference: scripts/uniprot_genes.py
  locator: verify_records checks on accessions/status/protein labels/gene tokens/taxa
    and component_ref; read-only CLI mode declarations.
  accessed_at: '2026-11-03T05:16:30.397073Z'
  snapshot_sha256: 8eaca44c9977fed92594e9bb2376d9e03a167546fd08932f2aa8b7d504605aa4
  summary: Native success verifies asserted ORF identity and graph coverage, not the
    independent cpcC orthology asserted in free-text role/evidence.
  support: supports
- evidence_id: micro-workflow-config
  kind: authority
  reference: conf/record_review.yaml
  locator: Entire route and rubric configuration, reread against newly frozen49-input
    inspect at2026-11-03T05:16:19Z.
  accessed_at: '2026-11-03T05:16:19.599408Z'
  snapshot_sha256: d3334a12b8a616a7638f1195748085d2b543fba7df67ad4ff8fcc0ac18f2d3ee
  summary: Routes include record/category/curation-audit/literature-evidence with
    the same inspected native rubrics. An earlier route-only read preceded its addition
    to inspect; this final workflow applicability assessment follows the frozen-byte
    reread. No changed rule or scientific judgment results.
  support: supports
- evidence_id: micro-psii-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009523,GO:0009521,GO:0009767
  locator: 'Native QuickGO exact requested term results: IDs, names, definitions,
    synonyms, aspects and returned child relations.'
  accessed_at: '2026-11-03T05:07:04.515318Z'
  snapshot_sha256: 453e4448a23ef80ffebd9ffa18ff1f8ca95f9e543eebbe6db5262a2c6a7fd288
  summary: Exact ontology boundaries and physiological functions inspected. Whole
    phycobilisome, peripheral rod, generic PSII and bacterial-thylakoid PSII remain
    distinct; no exhaustive ontology search is claimed.
  support: supports
- evidence_id: micro-rod-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030076,GO:0030089,GO:0009765
  locator: 'Native QuickGO exact requested term results: IDs, names, definitions,
    synonyms, aspects and returned child relations.'
  accessed_at: '2026-11-03T05:07:05.977391Z'
  snapshot_sha256: b4871465e93372dd482ee7d60e01d82de4f68e4c30c501145f24f31a738ea20f
  summary: Exact ontology boundaries and physiological functions inspected. Whole
    phycobilisome, peripheral rod, generic PSII and bacterial-thylakoid PSII remain
    distinct; no exhaustive ontology search is claimed.
  support: supports
- evidence_id: micro-psii-prep-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009523,GO:0009767,GO:0030075,GO:0030089,GO:0030096,GO:0031676
  locator: 'Native QuickGO exact requested term results: IDs, names, definitions,
    synonyms, aspects and returned child relations.'
  accessed_at: '2026-11-03T05:07:08.477337Z'
  snapshot_sha256: 854d31e60c2a54924a10a2bfa72e30e53acea3047b1d7e6614c8fe63b6ba20ad
  summary: Exact ontology boundaries and physiological functions inspected. Whole
    phycobilisome, peripheral rod, generic PSII and bacterial-thylakoid PSII remain
    distinct; no exhaustive ontology search is claimed.
  support: supports
- evidence_id: micro-psii-agent-tax-1117
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1117
  locator: Native taxonomy JSON taxId, scientificName, rank, lineage and otherNames.
  accessed_at: '2026-11-03T05:07:04.515763Z'
  snapshot_sha256: 5f4919ad6f362a82291b587d27134147f277ffc5fa593f6076f1983a704cd985
  summary: Authority confirms the cited taxon label/identifier. Thermostichus vulcanus
    and Rupite strain are not interchangeable; Nostoc PCC7120 includes the paper’s
    Anabaena name.
  support: supports
- evidence_id: micro-psii-agent-tax-32053
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/32053
  locator: Native taxonomy JSON taxId, scientificName, rank, lineage and otherNames.
  accessed_at: '2026-11-03T05:07:04.515864Z'
  snapshot_sha256: 22e01d3cfa17a447e15eeb62ce0bc9e9f698799dc9e5e2586e3408b075a1829e
  summary: Authority confirms the cited taxon label/identifier. Thermostichus vulcanus
    and Rupite strain are not interchangeable; Nostoc PCC7120 includes the paper’s
    Anabaena name.
  support: supports
- evidence_id: micro-rod-agent-tax-2763
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2763
  locator: Native taxonomy JSON taxId, scientificName, rank, lineage and otherNames.
  accessed_at: '2026-11-03T05:07:05.977484Z'
  snapshot_sha256: 73c5fb9f4e663ee9f81162bbef7158f567879f7e39c91ee4823564289385434b
  summary: Authority confirms the cited taxon label/identifier. Thermostichus vulcanus
    and Rupite strain are not interchangeable; Nostoc PCC7120 includes the paper’s
    Anabaena name.
  support: supports
- evidence_id: micro-rod-agent-tax-2813851
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2813851
  locator: Native taxonomy JSON taxId, scientificName, rank, lineage and otherNames.
  accessed_at: '2026-11-03T05:07:06.215125Z'
  snapshot_sha256: 5dbd710f7409b10ef40f3c02ab8226cf6654f0e74b703ecfb94dbb1abe8613c6
  summary: Authority confirms the cited taxon label/identifier. Thermostichus vulcanus
    and Rupite strain are not interchangeable; Nostoc PCC7120 includes the paper’s
    Anabaena name.
  support: supports
- evidence_id: micro-psii-prep-tax-103690
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/103690
  locator: Native taxonomy JSON taxId, scientificName, rank, lineage and otherNames.
  accessed_at: '2026-11-03T05:07:08.539183Z'
  snapshot_sha256: 2b8526d70a7802fcadfd60e403d42636751a51761eeca9a143da868eb9a9b30d
  summary: Authority confirms the cited taxon label/identifier. Thermostichus vulcanus
    and Rupite strain are not interchangeable; Nostoc PCC7120 includes the paper’s
    Anabaena name.
  support: supports
- evidence_id: micro-psii-agent-umena2011-pdf
  kind: primary_source
  reference: https://chemie.uni-muenchen.de/ac/kluefers/homepage/L/bac/oec_2011.pdf
  locator: Umena et al. 2011, Nature 473:55–60 and online Methods; extracted primary
    body, abstract, composition/Mn4CaO5/pigment/quinone sections and figure captions;
    no figure-pixel or diffraction reanalysis.
  accessed_at: '2026-11-03T05:07:04.515925Z'
  snapshot_sha256: 29e5d7be00bc7ccf1acf26fe3276d2176b6fe92fe5736280637602b52623f693
  summary: Purified oxygen-evolving T. vulcanus PSII resolved at 1.9 Å supports core
    proteins, Mn4CaO5 cluster, chlorophyll/pheophytin/carotenoid cofactors and donor/acceptor
    architecture. Modeled 19 subunits versus canonical 20 reflects PsbY lost during
    preparation; no universal stoichiometry or depletion/assembly necessity is inferred.
  support: supports
- evidence_id: micro-psii-kamiya2003-html
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC140893/
  locator: 'PMC140893 readable primary HTML: Abstract, Introduction, Materials/Methods
    and selected Results on subunit/cofactor architecture; paragraph extraction indices
    12–16, 24–27 and corresponding captions.'
  accessed_at: '2026-11-03T05:07:09.718389Z'
  snapshot_sha256: deafa98805ab10cfc52ce5aa1087ee528d1321aeaeba2163bc2d2254909d7967
  summary: Current full-body access succeeds, unlike the original historical access
    attempt. Purified active T. vulcanus PSII at 3.7 Å contains D1/D2, CP43/CP47 and
    cofactors. Methods used T. vulcanus D1/cyt c550 sequences and T. elongatus sequences
    for other subunits; this is not exact native sequence proof for every T. vulcanus
    protein.
  support: supports
- evidence_id: micro-psii-kawakami2009-html
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2688974/
  locator: 'PMC2688974 readable HTML: Abstract; Results oxygen evolution with Br/I
    substitution and reconstitution; Discussion; purification/crystallization and
    oxygen-evolution Methods (extraction paragraphs 16,19–21,24,26,47–51,54–55,60).'
  accessed_at: '2026-11-03T05:07:09.720754Z'
  snapshot_sha256: 97db08a38f937ce1b047ee2d60bcf3b2103ad21a67cad40970f48b67490ae334
  summary: Current body access succeeds. T. vulcanus purified PSII halide experiments
    correlate two anion sites with oxygen evolution. Their functional perturbation
    does not test assembly necessity of every pigment or metal-cluster class.
  support: supports
- evidence_id: micro-psii-agent-P51765
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P51765.json
  locator: Native UniProt entry accession/status, exact geneName, organism, protein
    name, functional/cofactor annotations and SUBCELLULAR LOCATION evidence.
  accessed_at: '2026-11-03T05:07:04.516031Z'
  snapshot_sha256: 04887fcce267947732efc1a8148837c6691f19aedf33874357ac93e63338b2f7
  summary: Reviewed T. vulcanus psbA/D1 and psbD/D2 examples match their native gene/status/taxon;
    listed PMIDs12518057,19433803,21499260 are actually carried as ECO:0000269 thylakoid
    annotations. These annotations and inspected primary structures are kept distinct.
  support: supports
- evidence_id: micro-psii-agent-D0VWR8
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/D0VWR8.json
  locator: Native UniProt entry accession/status, exact geneName, organism, protein
    name, functional/cofactor annotations and SUBCELLULAR LOCATION evidence.
  accessed_at: '2026-11-03T05:07:04.516150Z'
  snapshot_sha256: 3b383aa42a19d3fd926532422025ccb924def2c56cf45f212de3d50786155663
  summary: Reviewed T. vulcanus psbA/D1 and psbD/D2 examples match their native gene/status/taxon;
    listed PMIDs12518057,19433803,21499260 are actually carried as ECO:0000269 thylakoid
    annotations. These annotations and inspected primary structures are kept distinct.
  support: supports
- evidence_id: micro-psii-agent-uniprot-unique
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue%20AND%20taxonomy_id%3A32053%20AND%20%28gene_exact%3ApsbA%20OR%20gene_exact%3ApsbD%29&format=json&size=100
  locator: Native query response and X-Total-Results=2; no next-page Link header.
  accessed_at: '2026-11-03T05:07:05.322046Z'
  snapshot_sha256: e384401ab283e369cbd5420ec28f61a00684b2868f42cb5b9b7a7bffb1dea974
  summary: The bounded exact reviewed psbA/psbD query returns P51765 and D0VWR8; this
    supports the present single reviewed entry per symbol in this taxon query.
  search_scope: 'UniProtKB on 2026-11-03: reviewed:true AND taxonomy_id:32053 AND
    (gene_exact:psbA OR gene_exact:psbD), JSON size=100. Two returned entries match
    total_results=2, no next-page link. Their native geneName fields were separately
    inspected; no claim about other taxa, unreviewed entries or all proteins.'
  support: supports
- evidence_id: micro-psii-agent-epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A21499260%20OR%20EXT_ID%3A12518057%20OR%20EXT_ID%3A19433803
  locator: Exact three cited PMID metadata and abstracts, not surrogate full-body
    evidence.
  accessed_at: '2026-11-03T05:07:05.792011Z'
  snapshot_sha256: 3c650dc041318d1e2333535684a4895edf8a6384bf623561788d6c538cfdea61
  summary: Citation identities verified; primary bodies/PDF are separately inspected
    and cited.
  support: supports
- evidence_id: micro-psii-agent-IPR005867
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005867/
  locator: Native InterPro metadata accession/name/type and explanatory domain/family
    scope; selected description paragraphs.
  accessed_at: '2026-11-03T05:07:05.324018Z'
  snapshot_sha256: faa113a0f5552d7f408c1f01950cfacd1859166aa8d679c30989cb105f8c1a46
  summary: 'Exact candidate scope inspected: D1/D2 families cannot individually ground
    the mixed PSII core; broad L/M includes homologous bacterial reaction-center subunits.
    Phycobiliprotein alpha/beta family also includes core proteins; linker domain/superfamily/family
    candidates do not establish exact identity of the mixed rod/rod-cap/rod-core cohort.
    These are candidate inspections, not universal family-absence proof.'
  support: supports
- evidence_id: micro-psii-agent-IPR005868
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005868/
  locator: Native InterPro metadata accession/name/type and explanatory domain/family
    scope; selected description paragraphs.
  accessed_at: '2026-11-03T05:07:05.337052Z'
  snapshot_sha256: 4f698a778bf556dfaf7c827388d3eade093a92f055c47ef1734aef5e36bdad9a
  summary: 'Exact candidate scope inspected: D1/D2 families cannot individually ground
    the mixed PSII core; broad L/M includes homologous bacterial reaction-center subunits.
    Phycobiliprotein alpha/beta family also includes core proteins; linker domain/superfamily/family
    candidates do not establish exact identity of the mixed rod/rod-cap/rod-core cohort.
    These are candidate inspections, not universal family-absence proof.'
  support: supports
- evidence_id: micro-psii-agent-IPR000484
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000484/
  locator: Native InterPro metadata accession/name/type and explanatory domain/family
    scope; selected description paragraphs.
  accessed_at: '2026-11-03T05:07:05.549541Z'
  snapshot_sha256: d8aae07dcf579cb89473e738ece6d8310e55a73c30ac5e8e6ef32a94d2cc9ae5
  summary: 'Exact candidate scope inspected: D1/D2 families cannot individually ground
    the mixed PSII core; broad L/M includes homologous bacterial reaction-center subunits.
    Phycobiliprotein alpha/beta family also includes core proteins; linker domain/superfamily/family
    candidates do not establish exact identity of the mixed rod/rod-cap/rod-core cohort.
    These are candidate inspections, not universal family-absence proof.'
  support: supports
- evidence_id: micro-rod-agent-IPR012128
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR012128/
  locator: Native InterPro metadata accession/name/type and explanatory domain/family
    scope; selected description paragraphs.
  accessed_at: '2026-11-03T05:07:06.575324Z'
  snapshot_sha256: 7de870a6ff5da7e35feb341d61ad7f902c7f7d78fcb8370e124adf8a85728c58
  summary: 'Exact candidate scope inspected: D1/D2 families cannot individually ground
    the mixed PSII core; broad L/M includes homologous bacterial reaction-center subunits.
    Phycobiliprotein alpha/beta family also includes core proteins; linker domain/superfamily/family
    candidates do not establish exact identity of the mixed rod/rod-cap/rod-core cohort.
    These are candidate inspections, not universal family-absence proof.'
  support: supports
- evidence_id: micro-rod-agent-IPR001297
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001297/
  locator: Native InterPro metadata accession/name/type and explanatory domain/family
    scope; selected description paragraphs.
  accessed_at: '2026-11-03T05:07:06.585753Z'
  snapshot_sha256: 66a740823ed894519ff244d02540651633989c0fa16f581c0625354a9ca2b831
  summary: 'Exact candidate scope inspected: D1/D2 families cannot individually ground
    the mixed PSII core; broad L/M includes homologous bacterial reaction-center subunits.
    Phycobiliprotein alpha/beta family also includes core proteins; linker domain/superfamily/family
    candidates do not establish exact identity of the mixed rod/rod-cap/rod-core cohort.
    These are candidate inspections, not universal family-absence proof.'
  support: supports
- evidence_id: micro-rod-agent-IPR038255
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR038255/
  locator: Native InterPro metadata accession/name/type and explanatory domain/family
    scope; selected description paragraphs.
  accessed_at: '2026-11-03T05:07:06.648963Z'
  snapshot_sha256: 9cff262c0e9f667225a0e684f2661399b61f81c58368f0aeb49719713665b7ed
  summary: 'Exact candidate scope inspected: D1/D2 families cannot individually ground
    the mixed PSII core; broad L/M includes homologous bacterial reaction-center subunits.
    Phycobiliprotein alpha/beta family also includes core proteins; linker domain/superfamily/family
    candidates do not establish exact identity of the mixed rod/rod-cap/rod-core cohort.
    These are candidate inspections, not universal family-absence proof.'
  support: supports
- evidence_id: micro-rod-agent-IPR016470
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016470/
  locator: Native InterPro metadata accession/name/type and explanatory domain/family
    scope; selected description paragraphs.
  accessed_at: '2026-11-03T05:07:06.893364Z'
  snapshot_sha256: 4f5ab2b535dee706d9b8d31f7be25fc069adadef5454d3573683e399706202eb
  summary: 'Exact candidate scope inspected: D1/D2 families cannot individually ground
    the mixed PSII core; broad L/M includes homologous bacterial reaction-center subunits.
    Phycobiliprotein alpha/beta family also includes core proteins; linker domain/superfamily/family
    candidates do not establish exact identity of the mixed rod/rod-cap/rod-core cohort.
    These are candidate inspections, not universal family-absence proof.'
  support: supports
- evidence_id: micro-rod-agent-kawakami2022-jats
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9205905/fullTextXML
  locator: 'PMC9205905 JATS: Introduction, Sec3 subunit composition, Sec7 PC-rod structure,
    Sec8 possible energy transfer, Sec10 preparation, Sec17 MS, Figures6–8 captions;
    source text, not raw cryo-EM data or figure pixels.'
  accessed_at: '2026-11-03T05:07:06.475293Z'
  snapshot_sha256: d428f0c1cc2ccea5b0e4e343d5841355b892f65e6cb694481ee1ff13c9087713
  summary: NIES-2134 rods were dissociated from PBS at reduced phosphate and reconstructed
    at 4.2 Å. CpcA/B, bound bilins and CpcC/D/G linker architecture support grouped
    rod constituents and broad function. CpcG2 identity was tentative in heterogeneous
    CpcG rods; precise energy routes/tuning are structural interpretations with prior
    spectroscopy, not time-resolved proof. The paper does not establish Rupite JX360_02095=cpcC.
  support: supports
- evidence_id: micro-rod-agent-A0ABT0C7V5
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/A0ABT0C7V5.json
  locator: Native UniProt accession/status, protein name, genes/ORF tokens, taxon,
    sequence length, evidence tier and family/domain cross-references.
  accessed_at: '2026-11-03T05:07:07.128303Z'
  snapshot_sha256: dda82df881e3ce27aa2794e2deef3984c9b8391a3d07dca2452884523d58a842
  summary: 'A0ABT0C7V5: Phycocyanin subunit alpha; UniProtKB unreviewed (TrEMBL);
    taxon 2813851, 162 aa. Identity/predicted annotation scope only. This entry is
    not used to infer cross-strain experimental localization or to nominate a replacement
    cpcC accession.'
  support: supports
- evidence_id: micro-rod-agent-A0ABT0C7V6
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/A0ABT0C7V6.json
  locator: Native UniProt accession/status, protein name, genes/ORF tokens, taxon,
    sequence length, evidence tier and family/domain cross-references.
  accessed_at: '2026-11-03T05:07:07.188658Z'
  snapshot_sha256: c88aa1be83dba1e643cca17e159edf063a98f91f632213c22ea8652077cf6cad
  summary: 'A0ABT0C7V6: Phycocyanin subunit beta; UniProtKB unreviewed (TrEMBL); taxon
    2813851, 172 aa. Identity/predicted annotation scope only. This entry is not used
    to infer cross-strain experimental localization or to nominate a replacement cpcC
    accession.'
  support: supports
- evidence_id: micro-rod-agent-A0ABT0C7V3
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/A0ABT0C7V3.json
  locator: Native UniProt accession/status, protein name, genes/ORF tokens, taxon,
    sequence length, evidence tier and family/domain cross-references.
  accessed_at: '2026-11-03T05:07:07.204406Z'
  snapshot_sha256: 84b7e5f2cd126c4172b653028377112ab3d41557c3ae15968804cdef4e65a818
  summary: 'A0ABT0C7V3: Phycobilisome rod-core linker polypeptide; UniProtKB unreviewed
    (TrEMBL); taxon 2813851, 241 aa. Identity/predicted annotation scope only. This
    entry is not used to infer cross-strain experimental localization or to nominate
    a replacement cpcC accession.'
  support: supports
- evidence_id: micro-rod-agent-A0ABT0C7D6
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/A0ABT0C7D6.json
  locator: Native UniProt accession/status, protein name, genes/ORF tokens, taxon,
    sequence length, evidence tier and family/domain cross-references.
  accessed_at: '2026-11-03T05:07:07.244293Z'
  snapshot_sha256: c1fcb9b60d36f25177316177ea0239890ec5e6444d9faecd85d959ab80834bab
  summary: 'A0ABT0C7D6: Phycobilisome rod-core linker polypeptide; UniProtKB unreviewed
    (TrEMBL); taxon 2813851, 172 aa. Identity/predicted annotation scope only. No
    cpcC token is present; generic rod-core linker annotation does not establish the
    role-level cpcC mapping.'
  support: supports
- evidence_id: micro-rod-agent-A0ABT0C9G9
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/A0ABT0C9G9.json
  locator: Native UniProt accession/status, protein name, genes/ORF tokens, taxon,
    sequence length, evidence tier and family/domain cross-references.
  accessed_at: '2026-11-03T05:07:07.881538Z'
  snapshot_sha256: 670be0a88c17efd16e0213cbafc3bd67783323a8cf9850f96cde0ba6fef1fc06
  summary: 'A0ABT0C9G9: Phycobilisome rod-core linker polypeptide; UniProtKB unreviewed
    (TrEMBL); taxon 2813851, 285 aa. Identity/predicted annotation scope only. This
    entry is not used to infer cross-strain experimental localization or to nominate
    a replacement cpcC accession.'
  support: supports
- evidence_id: micro-rod-agent-P50034
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P50034.json
  locator: Native UniProt accession/status, protein name, genes/ORF tokens, taxon,
    sequence length, evidence tier and family/domain cross-references.
  accessed_at: '2026-11-03T05:07:07.748392Z'
  snapshot_sha256: 3a6c5f28ac97d8f12ddbaa40329cecd5095ebdbe2ebeac8d492b430f186ccd98
  summary: 'P50034: Phycobilisome 32.1 kDa linker polypeptide, phycocyanin-associated,
    rod; UniProtKB reviewed (Swiss-Prot); taxon 197221, 287 aa. Identity/predicted
    annotation scope only. This entry is not used to infer cross-strain experimental
    localization or to nominate a replacement cpcC accession.'
  support: supports
- evidence_id: micro-rod-new-A0ABT0CFU3
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/A0ABT0CFU3.json
  locator: Native UniProt accession/status, protein name, genes/ORF tokens, taxon,
    sequence length, evidence tier and family/domain cross-references.
  accessed_at: '2026-11-03T05:07:09.537277Z'
  snapshot_sha256: 5cb4ba3b0d222618fd064bc9f8c4c125f4b79f730e9b30f5a761cb52e6f1a6e0
  summary: 'A0ABT0CFU3: CpcD phycobilisome linker protein; UniProtKB unreviewed (TrEMBL);
    taxon 2813851, 159 aa. Identity/predicted annotation scope only. The explicit
    submitted CpcD protein name supports the new predicted example; JX360_17400 remains
    an ORF token, not an experimental localization or unique ortholog claim.'
  support: supports
- evidence_id: micro-rod-agent-MCJ2541704.1-genpept
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=MCJ2541704.1&db=protein&report=genpept&retmode=text
  locator: NCBI GenPept definition, organism/strain, Protein product and CDS locus_tag/inference
    qualifiers.
  accessed_at: '2026-11-03T05:07:07.492101Z'
  snapshot_sha256: f37c9de8d1f38f25d3caa7b3be35a4d2e4867637bee0c91ddfa87f42709c119b
  summary: JX360_02095 is a predicted generic phycobilisome rod-core linker; this
    source does not establish cpcC.
  support: supports
- evidence_id: micro-rod-agent-pdb-7veb-entity4
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/7VEB/4
  locator: RCSB 7VEB entity4 native polymer sequence length and entity_src_nat/rcsb_entity_source_organism.
  accessed_at: '2026-11-03T05:07:07.800534Z'
  snapshot_sha256: 6686d1a74c47684846d09d5395a5121b9978109ba80dbe4a9387071b3cfff9a6
  summary: The CpcC model entity has 287 residues and a BP-1 source/model-sequence
    taxon annotation, distinct from the paper’s NIES-2134 sample and Rupite example.
    This scope mismatch cannot establish an exact Rupite locus mapping.
  support: context_only
- evidence_id: micro-rod-agent-rupite-linkers
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=taxonomy_id%3A2813851%20AND%20%28protein_name%3Alinker%20OR%20gene_exact%3AcpcC%20OR%20gene_exact%3AcpcG%20OR%20gene_exact%3AcpcD%29&format=json&size=500
  locator: Native complete seven-hit response, accession/gene ORF/protein names, status,
    lengths and family cross-references; no next-page link.
  accessed_at: '2026-11-03T05:07:07.958164Z'
  snapshot_sha256: 6723bea8cb29ac66c856ddc1458480c1e2d5e0f4db8798c3cf966cdb9eb80068
  summary: Multiple predicted Rupite linker candidates exist, including two submitted
    CpcD proteins. No accession is selected as cpcC from length or generic domain
    architecture.
  search_scope: 'UniProtKB on 2026-11-03: taxonomy_id:2813851 AND (protein_name:linker
    OR gene_exact:cpcC OR gene_exact:cpcG OR gene_exact:cpcD), JSON size=500. Seven
    returned entries equal total_results=7, no next-page link. Bounded linker/token
    query only; neither exhaustive orthology inference nor proof that cpcC is biologically
    absent.'
  support: supports
- evidence_id: micro-rod-new-genpept
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=MCJ2544653.1&db=protein&report=genpept&retmode=text
  locator: MCJ2544653.1 definition and Protein product; CDS locus_tag JX360_17400,
    PGAP provenance and automated homology inference.
  accessed_at: '2026-11-03T05:08:04.515570Z'
  snapshot_sha256: e45ed6bd864ea1f6659f17069c9e9d1aa1e9fbc53fe3d59308ed33f113f914f3
  summary: New CpcD example matches the source product annotation, exact ORF and Rupite
    taxon; annotation is computational, not measured rod localization.
  support: supports
- evidence_id: micro-rod-new-IPR008213
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR008213/
  locator: Native InterPro entry name/type, member-domain scope and description; bibliographic
    list not used as primary evidence.
  accessed_at: '2026-11-03T05:08:04.515647Z'
  snapshot_sha256: 95d8564631a0996c961a8d560eb7cafabd0ba056ccf37948419c8d80dbc6059d
  summary: CpcD-like domain occurs across CpcD, the C terminus of CpcC, ApcC and FNR;
    domain presence alone is not exact orthology. New example support instead includes
    its explicit source protein product.
  support: supports
- evidence_id: micro-psii-prep-chang2015-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1038/cr.2015.59
  locator: Exact DOI/title/authors/PMID and abstract.
  accessed_at: '2026-11-03T05:07:09.093332Z'
  snapshot_sha256: 529cc77b3b228da781814b110110b11848c2fcab43cbc7907306c4b96584e0f5
  summary: Primary paper identity verified; the full primary text is separately inspected.
  support: supports
- evidence_id: micro-psii-prep-chang2015-pmc-html
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC4456626/
  locator: 'PMC4456626: Abstract; Introduction; overall-structure Results; Fig1 and5
    captions; energy-transfer Discussion; purification, negative-stain EM, reconstruction,
    immunoblot and immunogold Methods. Extraction paragraphs18,21–24,27–31,48–51,53–56,59,61–65,67–68,77,79.'
  accessed_at: '2026-11-03T05:07:09.141161Z'
  snapshot_sha256: af99713ec2b8bc28f16d385d1f55a3684086e89c2fde38541c2434eed51a3486
  summary: Anabaena/Nostoc PCC7120 purified PBS preparations contain selected PSII-associated
    particles. D1/D2 immunoblot and D1 immunogold support PSII identity. PBS-only21Å
    and PBS–PSII34Å reconstructions differ; French pressure,2%TritonX100 and negative
    staining preclude calling this an intact live-cell or atomic catalytic experiment.
    PsbO/PsaA nondetection is preparation-specific.
  support: supports
- evidence_id: micro-psii-prep-perez2024-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1146/annurev-cellbio-120823-022747
  locator: Europe PMC exact DOI metadata and abstract only.
  accessed_at: '2026-11-03T05:07:09.519769Z'
  snapshot_sha256: b92ede9a7453c7ac90e0c6daf55c01cf6d7e4451f25ecf0086b733c5dd8fa552
  summary: The secondary review discusses thylakoid structural diversity and molecular
    organization; its current abstract alone is not exact body-level support for the
    individual electron-carrier sentence.
  support: context_only
- evidence_id: micro-publisher
  kind: authority
  reference: https://www.annualreviews.org/content/journals/10.1146/annurev-cellbio-120823-022747
  locator: Fresh native publisher request returned HTTP403 challenge body; this snapshot
    is access evidence, not scientific article text.
  accessed_at: '2026-11-03T05:11:33.581168Z'
  snapshot_sha256: 5bcaee7d8a3044f3cbe260e6e5c3022e8eb84a1c38688641b3b256afd035e6e7
  summary: The attempted native Annual Reviews route did not yield the cited secondary
    body.
  support: context_only
- evidence_id: micro-perez-publisher-browser
  kind: authority
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2351/adversary-microtubule/perez/publisher-browser.json
  locator: Fresh browser-tool capture of publisher abstract/metadata or fulltext-route
    access error; captured tool output, not native publisher HTML.
  accessed_at: '2026-11-03T05:12:05Z'
  snapshot_sha256: 219dbc7498e0f3806fcab6af3edd18177d381d743d5ac004225836ed5e6c1c85
  summary: Only abstract/metadata and full-text loading placeholder were recovered;
    body route failed. Do not carry the historical body-excerpt access claim forward
    as a fresh read.
  support: supports
- evidence_id: micro-perez-body-browser-unavailable
  kind: authority
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2351/adversary-microtubule/perez/body-browser-unavailable.json
  locator: Fresh browser-tool capture of publisher abstract/metadata or fulltext-route
    access error; captured tool output, not native publisher HTML.
  accessed_at: '2026-11-03T05:12:00Z'
  snapshot_sha256: 6fcbcbdd41346711b356df2b032b492b97a18b3ccd0e8ba82c6dac0c5639a0fa
  summary: Only abstract/metadata and full-text loading placeholder were recovered;
    body route failed. Do not carry the historical body-excerpt access claim forward
    as a fresh read.
  support: supports
- evidence_id: micro-adapter-catalogue
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: 'Entire official datasets catalogue: organism/dataset keys.'
  accessed_at: '2026-11-03T05:07:09.625489Z'
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  summary: Twenty organisms and28datasets include s_elongatus/elprecise300. This is
    a relevant cyanobacterial context for the broad Cyanobacteriota distribution,
    not direct canonical Thermostichus/Nostoc or red-algal coverage.
  support: context_only
- evidence_id: micro-adapter-client-js
  kind: database
  reference: https://imodulondb.org/assets/index-3_RVHvkS.js
  locator: Official frontend source endpoint definitions for datasets/meta, genes
    and gene/module membership; no generated biological summaries used.
  accessed_at: '2026-11-03T05:08:04.515286Z'
  snapshot_sha256: 64c73f41c40268c8d5da3e8a10ef12bd9ef948e2bd2595e62f5a16409d0df1b9
  summary: API route discovery only; not scientific evidence.
  support: context_only
- evidence_id: micro-meta
  kind: database
  reference: https://imodulondb.org/api/datasets/s_elongatus/elprecise300/meta
  locator: s_elongatus/elprecise300 official metadata fields organism, strain, publication
    URL and dataset counts.
  accessed_at: '2026-11-03T05:10:05.463970Z'
  snapshot_sha256: ab1cea70cad9bdb6214c6350d7a8bf92ddddf13bdc928620cbc5ba76badc947f
  summary: Covered strain PCC7942;300samples,57modules and2669genes. Source publication
    is DOI10.1073/pnas.2410492121. No identity transfer to Rupite/Nostoc.
  support: context_only
- evidence_id: micro-genes
  kind: search
  reference: https://imodulondb.org/api/genes?organism=s_elongatus&dataset=elprecise300&limit=10000
  locator: Official gene-table response locally filtered on exact gene_name pattern
    (psb[AD]|cpc[ABCDG]) followed by optional numeric suffix.
  accessed_at: '2026-11-03T05:10:05.464346Z'
  snapshot_sha256: 79ffc38e3ba875ceebbfd73630da2e3b4f5491ef980220f079ed8d0bc8680609
  summary: 'The2669-row table contains13matched loci: five psbA/D and eight cpcA/B/C/D/G.
    Exact matches retain locus identifiers; no functional absence or orthology claim.'
  support: context_only
  search_scope: iModulonDB on 2026-11-03, organism=s_elongatus,dataset=elprecise300,strain=PCC7942;
    GET /api/genes?organism=s_elongatus&dataset=elprecise300&limit=10000 returned2669rows
    matching metadata total2669. Local exact gene_name regex (psb[AD]|cpc[ABCDG])\d*
    selected13rows. This filters this dataset only and does not search every alias
    or unrelated organism.
- evidence_id: micro-imodulons
  kind: search
  reference: https://imodulondb.org/api/datasets/s_elongatus/elprecise300/imodulons
  locator: Official57-row module list locally filtered on case-insensitive photo/light/pigment/psb/cpc
    in metadata; selected1PSII,6RpaB,38Photosystems for detailed inspection.
  accessed_at: '2026-11-03T05:10:05.464271Z'
  snapshot_sha256: 83e2436b8486f9c25800d7ef6848302f3b72fec4bde1df321588b0671672e625
  summary: Named modules are leads only. The selected modules’ actual members and
    thresholds were subsequently inspected; no structural membership is inferred from
    names.
  support: context_only
  search_scope: iModulonDB on2026-11-03, s_elongatus/elprecise300 official /imodulons
    endpoint returned57rows equal metadata57. Local case-insensitive substring filter
    photo|light|pigment|psb|cpc returned four rows (including phototaxis36); selected
    PSII1,RpaB6,Photosystems38 for gene-context inspection. No claim of exhaustive
    module biology or direct experimental support.
- evidence_id: micro-gene-Synpcc7942_0424
  kind: database
  reference: https://imodulondb.org/api/genes/Synpcc7942_0424/imodulons?organism=s_elongatus&dataset=elprecise300
  locator: Exact locus query in s_elongatus/elprecise300; all57module rows, thresholds,
    weights and in_imodulon flags.
  accessed_at: '2026-11-03T05:10:33.719294Z'
  snapshot_sha256: 433b2a6e29bd046b8ebea7f2126e3a6ae344cf4ff496dd4d176a8baf22e47ccd
  summary: 'Bounded computational context for Synpcc7942_0424; positive memberships:
    none at this dataset threshold. Nonmembership is not biological absence.'
  support: context_only
- evidence_id: micro-gene-Synpcc7942_0655
  kind: database
  reference: https://imodulondb.org/api/genes/Synpcc7942_0655/imodulons?organism=s_elongatus&dataset=elprecise300
  locator: Exact locus query in s_elongatus/elprecise300; all57module rows, thresholds,
    weights and in_imodulon flags.
  accessed_at: '2026-11-03T05:10:33.719678Z'
  snapshot_sha256: e1f2d6c944b8d1e58327c907097176183567244683dd97a123bc8e9c7e40f744
  summary: 'Bounded computational context for Synpcc7942_0655; positive memberships:
    38:Photosystems. Nonmembership is not biological absence.'
  support: context_only
- evidence_id: micro-gene-Synpcc7942_0893
  kind: database
  reference: https://imodulondb.org/api/genes/Synpcc7942_0893/imodulons?organism=s_elongatus&dataset=elprecise300
  locator: Exact locus query in s_elongatus/elprecise300; all57module rows, thresholds,
    weights and in_imodulon flags.
  accessed_at: '2026-11-03T05:10:33.719766Z'
  snapshot_sha256: 098fcbfc39fb26122f795ddaea77262596615fc3f0ac537ead0adf460c43d13b
  summary: 'Bounded computational context for Synpcc7942_0893; positive memberships:
    6:RpaB, 38:Photosystems. Nonmembership is not biological absence.'
  support: context_only
- evidence_id: micro-gene-Synpcc7942_1047
  kind: database
  reference: https://imodulondb.org/api/genes/Synpcc7942_1047/imodulons?organism=s_elongatus&dataset=elprecise300
  locator: Exact locus query in s_elongatus/elprecise300; all57module rows, thresholds,
    weights and in_imodulon flags.
  accessed_at: '2026-11-03T05:10:33.719848Z'
  snapshot_sha256: 9424142404d439c96f0a01fac770c8e2979d65594a335bb3abd1fe88586215ab
  summary: 'Bounded computational context for Synpcc7942_1047; positive memberships:
    6:RpaB, 38:Photosystems. Nonmembership is not biological absence.'
  support: context_only
- evidence_id: micro-gene-Synpcc7942_1048
  kind: database
  reference: https://imodulondb.org/api/genes/Synpcc7942_1048/imodulons?organism=s_elongatus&dataset=elprecise300
  locator: Exact locus query in s_elongatus/elprecise300; all57module rows, thresholds,
    weights and in_imodulon flags.
  accessed_at: '2026-11-03T05:10:33.719924Z'
  snapshot_sha256: 138c33670e42d05808aedb5bdb67565d741695488218143837a74ae494efe327
  summary: 'Bounded computational context for Synpcc7942_1048; positive memberships:
    6:RpaB, 38:Photosystems. Nonmembership is not biological absence.'
  support: context_only
- evidence_id: micro-gene-Synpcc7942_1049
  kind: database
  reference: https://imodulondb.org/api/genes/Synpcc7942_1049/imodulons?organism=s_elongatus&dataset=elprecise300
  locator: Exact locus query in s_elongatus/elprecise300; all57module rows, thresholds,
    weights and in_imodulon flags.
  accessed_at: '2026-11-03T05:10:33.719981Z'
  snapshot_sha256: 9740eab9c8e43e57f13c5e956b36eb6b0fa514fcad9c3356aa1a922a48e9cd8a
  summary: 'Bounded computational context for Synpcc7942_1049; positive memberships:
    6:RpaB, 38:Photosystems. Nonmembership is not biological absence.'
  support: context_only
- evidence_id: micro-gene-Synpcc7942_1050
  kind: database
  reference: https://imodulondb.org/api/genes/Synpcc7942_1050/imodulons?organism=s_elongatus&dataset=elprecise300
  locator: Exact locus query in s_elongatus/elprecise300; all57module rows, thresholds,
    weights and in_imodulon flags.
  accessed_at: '2026-11-03T05:10:33.914945Z'
  snapshot_sha256: 6039585e8ccc5c58a2b2cb3ce29291f8013653bf9909dfa017cd38e33cf997d5
  summary: 'Bounded computational context for Synpcc7942_1050; positive memberships:
    6:RpaB, 38:Photosystems. Nonmembership is not biological absence.'
  support: context_only
- evidence_id: micro-gene-Synpcc7942_1051
  kind: database
  reference: https://imodulondb.org/api/genes/Synpcc7942_1051/imodulons?organism=s_elongatus&dataset=elprecise300
  locator: Exact locus query in s_elongatus/elprecise300; all57module rows, thresholds,
    weights and in_imodulon flags.
  accessed_at: '2026-11-03T05:10:33.921538Z'
  snapshot_sha256: 0b8dc92439bf74d6bec2ca7f118ca3c7c3e482931f02b0f6ac376e1960fb086c
  summary: 'Bounded computational context for Synpcc7942_1051; positive memberships:
    6:RpaB, 38:Photosystems. Nonmembership is not biological absence.'
  support: context_only
- evidence_id: micro-gene-Synpcc7942_1052
  kind: database
  reference: https://imodulondb.org/api/genes/Synpcc7942_1052/imodulons?organism=s_elongatus&dataset=elprecise300
  locator: Exact locus query in s_elongatus/elprecise300; all57module rows, thresholds,
    weights and in_imodulon flags.
  accessed_at: '2026-11-03T05:10:33.926251Z'
  snapshot_sha256: e2f3c2d60d1244e9c3a3e814bc1b7d108956ab4bd631d4c381a38ddb0ece750d
  summary: 'Bounded computational context for Synpcc7942_1052; positive memberships:
    6:RpaB, 38:Photosystems. Nonmembership is not biological absence.'
  support: context_only
- evidence_id: micro-gene-Synpcc7942_1053
  kind: database
  reference: https://imodulondb.org/api/genes/Synpcc7942_1053/imodulons?organism=s_elongatus&dataset=elprecise300
  locator: Exact locus query in s_elongatus/elprecise300; all57module rows, thresholds,
    weights and in_imodulon flags.
  accessed_at: '2026-11-03T05:10:33.946772Z'
  snapshot_sha256: 2eaa0c5226e0441777f78af38a65d2948a9bd7d27b917a1742db107895c54c08
  summary: 'Bounded computational context for Synpcc7942_1053; positive memberships:
    6:RpaB, 38:Photosystems. Nonmembership is not biological absence.'
  support: context_only
- evidence_id: micro-gene-Synpcc7942_1389
  kind: database
  reference: https://imodulondb.org/api/genes/Synpcc7942_1389/imodulons?organism=s_elongatus&dataset=elprecise300
  locator: Exact locus query in s_elongatus/elprecise300; all57module rows, thresholds,
    weights and in_imodulon flags.
  accessed_at: '2026-11-03T05:10:33.947678Z'
  snapshot_sha256: 4918a9e985eb8e1a110304fe15c7527ab6b9a02775722437207c95978cbdfe70
  summary: 'Bounded computational context for Synpcc7942_1389; positive memberships:
    6:RpaB. Nonmembership is not biological absence.'
  support: context_only
- evidence_id: micro-gene-Synpcc7942_1637
  kind: database
  reference: https://imodulondb.org/api/genes/Synpcc7942_1637/imodulons?organism=s_elongatus&dataset=elprecise300
  locator: Exact locus query in s_elongatus/elprecise300; all57module rows, thresholds,
    weights and in_imodulon flags.
  accessed_at: '2026-11-03T05:10:33.971626Z'
  snapshot_sha256: cd6a067eda523b73cc9f5695402653690f9d55fd6b98a1a93cd7eabee1bcec49
  summary: 'Bounded computational context for Synpcc7942_1637; positive memberships:
    6:RpaB, 38:Photosystems. Nonmembership is not biological absence.'
  support: context_only
- evidence_id: micro-gene-Synpcc7942_2030
  kind: database
  reference: https://imodulondb.org/api/genes/Synpcc7942_2030/imodulons?organism=s_elongatus&dataset=elprecise300
  locator: Exact locus query in s_elongatus/elprecise300; all57module rows, thresholds,
    weights and in_imodulon flags.
  accessed_at: '2026-11-03T05:10:33.977280Z'
  snapshot_sha256: 350815e32e2f138c40dc79f971df26fd2ecdea1fcea72bb2e2773f7f02da9064
  summary: 'Bounded computational context for Synpcc7942_2030; positive memberships:
    6:RpaB, 38:Photosystems. Nonmembership is not biological absence.'
  support: context_only
- evidence_id: micro-module-1
  kind: database
  reference: https://imodulondb.org/api/imodulons/s_elongatus/elprecise300/1
  locator: Exact official module metadata or all=true gene-weight table; inspect in_imodulon=true
    rows and the selected psb/cpc loci; exclude AI summary fields.
  accessed_at: '2026-11-03T05:10:33.978339Z'
  snapshot_sha256: fe180c45de0f7400ffc349de6340de2a5f2fa1530e48f7995d8adcb60c9f0c59
  summary: 'Module1 PSII: declared21members and21true rows among2669returned gene-weight
    rows, threshold0.068537145; regulator field is null. Selected psb/cpc members:
    none. Module1includes other PSII-associated genes but does not contain the selected
    psbA/D loci. Computational expression context does not validate direct regulation,
    orthology, structural composition or causal mechanism.'
  support: context_only
- evidence_id: micro-module-1-genes
  kind: database
  reference: https://imodulondb.org/api/imodulons/s_elongatus/elprecise300/1/genes?all=true
  locator: Exact official module metadata or all=true gene-weight table; inspect in_imodulon=true
    rows and the selected psb/cpc loci; exclude AI summary fields.
  accessed_at: '2026-11-03T05:10:34.011968Z'
  snapshot_sha256: 96c66a5b0112dbf158fd59a54085dbf3577ad5ae171e25d6bb3f38d2a14ca575
  summary: 'Module1 PSII: declared21members and21true rows among2669returned gene-weight
    rows, threshold0.068537145; regulator field is null. Selected psb/cpc members:
    none. Module1includes other PSII-associated genes but does not contain the selected
    psbA/D loci. Computational expression context does not validate direct regulation,
    orthology, structural composition or causal mechanism.'
  support: context_only
- evidence_id: micro-module-6
  kind: database
  reference: https://imodulondb.org/api/imodulons/s_elongatus/elprecise300/6
  locator: Exact official module metadata or all=true gene-weight table; inspect in_imodulon=true
    rows and the selected psb/cpc loci; exclude AI summary fields.
  accessed_at: '2026-11-03T05:10:33.983063Z'
  snapshot_sha256: 076a21c4016fdd0316c41546581114dcaffc6efb4fb755d592db1649e24e4171
  summary: 'Module6 RpaB: declared77members and77true rows among2669returned gene-weight
    rows, threshold0.048868289; regulator field is null. Selected psb/cpc members:
    psbA3, cpcB1, cpcA1, cpcC1, cpcC2, cpcD, cpcB2, cpcA2, psbA2, psbD2, cpcG. Module1includes
    other PSII-associated genes but does not contain the selected psbA/D loci. Computational
    expression context does not validate direct regulation, orthology, structural
    composition or causal mechanism.'
  support: context_only
- evidence_id: micro-module-6-genes
  kind: database
  reference: https://imodulondb.org/api/imodulons/s_elongatus/elprecise300/6/genes?all=true
  locator: Exact official module metadata or all=true gene-weight table; inspect in_imodulon=true
    rows and the selected psb/cpc loci; exclude AI summary fields.
  accessed_at: '2026-11-03T05:10:34.014453Z'
  snapshot_sha256: 9584c24dc95c3841780219905201f120b7836f616558d3f66623b5a22e395f73
  summary: 'Module6 RpaB: declared77members and77true rows among2669returned gene-weight
    rows, threshold0.048868289; regulator field is null. Selected psb/cpc members:
    psbA3, cpcB1, cpcA1, cpcC1, cpcC2, cpcD, cpcB2, cpcA2, psbA2, psbD2, cpcG. Module1includes
    other PSII-associated genes but does not contain the selected psbA/D loci. Computational
    expression context does not validate direct regulation, orthology, structural
    composition or causal mechanism.'
  support: context_only
- evidence_id: micro-module-38
  kind: database
  reference: https://imodulondb.org/api/imodulons/s_elongatus/elprecise300/38
  locator: Exact official module metadata or all=true gene-weight table; inspect in_imodulon=true
    rows and the selected psb/cpc loci; exclude AI summary fields.
  accessed_at: '2026-11-03T05:10:33.983171Z'
  snapshot_sha256: 7236e5234640b6a379fa25dc2ac44375ba96a07d69f7a020e06741bcd94c0965
  summary: 'Module38 Photosystems: declared44members and44true rows among2669returned
    gene-weight rows, threshold0.063088206; regulator field is null. Selected psb/cpc
    members: psbD1, psbA3, cpcB1, cpcA1, cpcC1, cpcC2, cpcD, cpcB2, cpcA2, psbD2,
    cpcG. Module1includes other PSII-associated genes but does not contain the selected
    psbA/D loci. Computational expression context does not validate direct regulation,
    orthology, structural composition or causal mechanism.'
  support: context_only
- evidence_id: micro-module-38-genes
  kind: database
  reference: https://imodulondb.org/api/imodulons/s_elongatus/elprecise300/38/genes?all=true
  locator: Exact official module metadata or all=true gene-weight table; inspect in_imodulon=true
    rows and the selected psb/cpc loci; exclude AI summary fields.
  accessed_at: '2026-11-03T05:10:34.045320Z'
  snapshot_sha256: bc29d128e45c9abd6d13fd56bcc6bc9bac8ae25756a067ce614475f8b0258b3a
  summary: 'Module38 Photosystems: declared44members and44true rows among2669returned
    gene-weight rows, threshold0.063088206; regulator field is null. Selected psb/cpc
    members: psbD1, psbA3, cpcB1, cpcA1, cpcC1, cpcC2, cpcD, cpcB2, cpcA2, psbD2,
    cpcG. Module1includes other PSII-associated genes but does not contain the selected
    psbA/D loci. Computational expression context does not validate direct regulation,
    orthology, structural composition or causal mechanism.'
  support: context_only
- evidence_id: micro-adapter-publication
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1073/pnas.2410492121
  locator: Europe PMC exact DOI metadata and abstract only for the dataset publication.
  accessed_at: '2026-11-03T05:11:33.581446Z'
  snapshot_sha256: 1526b43a10192eccc527bb76d5c9df405fe50a86eab7ddc412461234393f986c
  summary: The study uses independent-component analysis of300RNA-seq datasets from
    Synechococcus elongatus PCC7942 to derive57modules. Abstract scope only; full
    study methods and data were not reanalyzed.
  support: context_only
- evidence_id: micro-native-photosystem-ii-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2351/photosystem-ii-uniprot-verify-receipt.json
  locator: Actual root-executed current-head command receipt and adjacent stdout;
    exit0; stdout SHA verified.
  accessed_at: '2026-11-03T05:07:43.991175Z'
  snapshot_sha256: 07d529db12abbcf21f910a076cd8e812c425342afdba35fcb7bfe2dddec771c6
  summary: Command .venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/photosystem_ii.yaml
    --verify passed. Native exact accession/status/token/taxon checks; not free-text
    orthology validation.
  support: supports
- evidence_id: micro-native-photosystem-ii-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2351/photosystem-ii-uniprot-causal-receipt.json
  locator: Actual root-executed current-head command receipt and adjacent stdout;
    exit0; stdout SHA verified.
  accessed_at: '2026-11-03T05:07:44.412836Z'
  snapshot_sha256: e0dd0ba33bcbd12de411f19d3670ae5abf51a2009f7109b46c2166171c24ed3d
  summary: Command .venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/photosystem_ii.yaml
    --causal-graphs passed. Current graph coverage is 1COVERED/1total, with zero dangling
    refs and no uncovered symbol category.
  support: supports
- evidence_id: micro-native-phycobilisome-rod-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2351/phycobilisome-rod-uniprot-verify-receipt.json
  locator: Actual root-executed current-head command receipt and adjacent stdout;
    exit0; stdout SHA verified.
  accessed_at: '2026-11-03T05:07:45.743996Z'
  snapshot_sha256: a6a5d2a13cb30bd0c59efabbc78b2f120eb1f147a29f1abf4a44e979e3ebaadd
  summary: Command .venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/phycobilisome_rod.yaml
    --verify passed. Native exact accession/status/token/taxon checks; not free-text
    orthology validation.
  support: supports
- evidence_id: micro-native-phycobilisome-rod-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2351/phycobilisome-rod-uniprot-causal-receipt.json
  locator: Actual root-executed current-head command receipt and adjacent stdout;
    exit0; stdout SHA verified.
  accessed_at: '2026-11-03T05:07:46.170524Z'
  snapshot_sha256: 038902abb80e91ad596cd49f98c3c514a1339f9101fdb81e282c41edc2246828
  summary: Command .venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/phycobilisome_rod.yaml
    --causal-graphs passed. Current graph coverage is 2COVERED/2total, with zero dangling
    refs and no uncovered symbol category.
  support: supports
- evidence_id: micro-original-checks
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2351/adversary-microtubule/original-checks.json
  locator: Actual independent native validate/render and frozen-input comparisons
    for all3 originals.
  accessed_at: '2026-11-03T05:07:37.605472Z'
  snapshot_sha256: 5ab7885a5ec6bca48e8fcaa96ed6eb9039cc009d3a28a3f3c0bf32157f0bbf9b
  summary: All3native validations exit0; renderer --content matches each paired Markdown.
    Original frozen hashes match historical source trees; current matches are true,
    with rod alone changed.
  support: supports
- evidence_id: septin-s2351-rc-prep-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009767,GO:0042717
  locator: 'Native issuing-authority response: exact identifier, label, taxon and
    returned annotation scope.'
  accessed_at: '2026-11-03T05:07:07.983269Z'
  support: supports
  summary: Exact current record identifiers and bounded authority annotations checked.
    Database attribution is distinguished from independent experimental inspection.
  snapshot_sha256: a9ebf46fb99807cbd088c421c45834e88fc68f21d1abdd1f394e70ef458c0271
- evidence_id: septin-s2351-rc-prep-tax-1063
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1063
  locator: 'Native issuing-authority response: exact identifier, label, taxon and
    returned annotation scope.'
  accessed_at: '2026-11-03T05:07:07.983562Z'
  support: supports
  summary: Exact current record identifiers and bounded authority annotations checked.
    Database attribution is distinguished from independent experimental inspection.
  snapshot_sha256: 8285496c8734b387fd123717f2706cee39315debabb01990f225569e47e4420d
- evidence_id: septin-s2351-rc-prep-bahatyrova2004-meta
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1038/nature02823
  locator: Europe PMC exact DOI primary abstract and bibliographic metadata only.
  accessed_at: '2026-11-03T05:07:07.983644Z'
  support: supports
  summary: Source identity and RC-LH1/LH2 organization checked; native PDF supplies
    the separate, explicitly bounded body evidence.
  snapshot_sha256: cdd0a3a0fab5cf8136a8c5e9e2246441b2cbf420c78c71eaf28cf9620293f722
  search_scope: Database/request https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1038/nature02823;
    exact query and pagination/limit encoded in that URL, executed 2026-11-03T05:07:07.983644Z;
    no publication-date restriction. Only returned results inspected. No exhaustive
    literature/biological absence assertion.
- evidence_id: septin-s2351-rc-prep-bahatyrova2004-whiterose-pdf
  kind: primary_source
  reference: https://eprints.whiterose.ac.uk/id/eprint/102/1/huntercn1.pdf
  locator: Primary paper abstract, Introduction, claim-bearing Results pp1059–1061,
    Figure1–3 captions and membrane-preparation/AFM Methods; not figure pixels or
    raw AFM.
  accessed_at: '2026-11-03T05:07:07.983699Z'
  support: supports
  summary: NCIB8253 membrane patches show RC-LH1 arrays and LH2 clusters. RC L/M/H
    and LH1 constituents are described, but PufX itself was not resolved. Isolated
    detergent-treated, mica-adsorbed membranes do not constitute intact-cell dynamics.
    Potential interdimer energy transfer is interpretation, not a new measured transfer
    rate.
  snapshot_sha256: 18b555872af69d3ebed8f51dcfab485e048eaa892d83e9ac71cb998564f3bd25
- evidence_id: septin-s2351-rc-prep-comayras2005-meta
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1074/jbc.M412088200
  locator: Europe PMC exact DOI primary abstract and bibliographic metadata only.
  accessed_at: '2026-11-03T05:07:07.983746Z'
  support: supports
  summary: Comayras/Jungas/Lavergne compare isolated monomers/dimers and chromatophores
    by excitation and photoreducible-quinone assays. Their limited-domain interpretation
    does not license universal long-range interdimer transfer.
  snapshot_sha256: f0a2f6d4c18cf31ffaaddcebf08e2e79dffad94e116ffecf30b579b254acd745
  search_scope: Database/request https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1074/jbc.M412088200;
    exact query and pagination/limit encoded in that URL, executed 2026-11-03T05:07:07.983746Z;
    no publication-date restriction. Only returned results inspected. No exhaustive
    literature/biological absence assertion.
- evidence_id: septin-s2351-v0-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000220,GO:0005774,GO:0016471,GO:0033179
  locator: 'Native issuing-authority response: exact identifier, label, taxon and
    returned annotation scope.'
  accessed_at: '2026-11-03T05:07:08.756865Z'
  support: supports
  summary: Exact current record identifiers and bounded authority annotations checked.
    Database attribution is distinguished from independent experimental inspection.
  snapshot_sha256: 8c65c213952668f23b81a92a303628e1109642ff484b46d1f2de8bb5978ffff4
- evidence_id: septin-s2351-v0-agent-tax-4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: 'Native issuing-authority response: exact identifier, label, taxon and
    returned annotation scope.'
  accessed_at: '2026-11-03T05:07:08.769243Z'
  support: supports
  summary: Exact current record identifiers and bounded authority annotations checked.
    Database attribution is distinguished from independent experimental inspection.
  snapshot_sha256: 38f43dd1593a1d47416228ae385464f30aeb8302c3aadb45b3588d03744bc814
- evidence_id: septin-s2351-v0-agent-doi-MMBR_70_1_177-191_2006
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1128/MMBR.70.1.177-191.2006
  locator: Europe PMC exact DOI secondary-review abstract and author/title metadata.
  accessed_at: '2026-11-03T05:07:08.776362Z'
  support: supports
  summary: Kane2006 is review-tier synthesis of the S. cerevisiae V-ATPase, not an
    independent primary experiment.
  snapshot_sha256: 8eac776a8869a547a37502fd79db9798cb0c58b42f84374f991ffb3f499e303e
  search_scope: Database/request https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1128/MMBR.70.1.177-191.2006;
    exact query and pagination/limit encoded in that URL, executed 2026-11-03T05:07:08.776362Z;
    no publication-date restriction. Only returned results inspected. No exhaustive
    literature/biological absence assertion.
- evidence_id: septin-s2351-v0-agent-kane2006-legacy-html
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1393255/
  locator: 'Secondary review: Structure and Mechanism, V-ATPase Assembly, vacuolar/Golgi
    isoform targeting and reversible-dissociation passages, plus relevant captions;
    not every regulation section or cited primary experiment.'
  accessed_at: '2026-11-03T05:07:08.796361Z'
  support: supports
  summary: Kane identifies yeast V0 a/c/c-prime/c-double-prime/d/e and V1 A–H. Rotation
    couples ATP hydrolysis to transport in the intact enzyme; dissociated-sector inhibition
    and isoform localization bound the record. Historical stalk/c-ring models are
    not imported as current fixed stoichiometry.
  snapshot_sha256: b5d48de029bed6727efa11e5c38018b86645dd3d1bf7485ed978cc858c56334d
- evidence_id: septin-s2351-v1-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000220,GO:0000221,GO:0016471,GO:0033180,GO:0046961
  locator: 'Native issuing-authority response: exact identifier, label, taxon and
    returned annotation scope.'
  accessed_at: '2026-11-03T05:07:09.340174Z'
  support: supports
  summary: Exact current record identifiers and bounded authority annotations checked.
    Database attribution is distinguished from independent experimental inspection.
  snapshot_sha256: 9bbbd96a8e65f44352a83fb48dce584787fddff024e8bea38675d1fa43435d75
- evidence_id: septin-s2351-v1-agent-doi-nrm2272
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1038/nrm2272
  locator: Europe PMC exact DOI secondary-review abstract and author/title metadata
    only.
  accessed_at: '2026-11-03T05:07:09.346993Z'
  support: supports
  summary: Forgac2007 source identity and broad ATP-driven proton-pump context checked.
    Native publisher request returned authorization HTML, so no fresh complete body
    or Key Points inspection is claimed.
  snapshot_sha256: 55c0c1a8752adaa99a6255c1a99ee11cf7e2202a38e78c8fc936d05da82548f4
  search_scope: Database/request https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1038/nrm2272;
    exact query and pagination/limit encoded in that URL, executed 2026-11-03T05:07:09.346993Z;
    no publication-date restriction. Only returned results inspected. No exhaustive
    literature/biological absence assertion.
- evidence_id: septin-s2351-v1-agent-ro-native
  kind: authority
  reference: https://raw.githubusercontent.com/oborel/obo-relations/master/ro.json
  locator: 'Native issuing-authority response: exact identifier, label, taxon and
    returned annotation scope.'
  accessed_at: '2026-11-03T05:07:09.388546Z'
  support: supports
  summary: Exact current record identifiers and bounded authority annotations checked.
    Database attribution is distinguished from independent experimental inspection.
  snapshot_sha256: 17eab8be4f47c73d2905ba45752154ae8e2e7b0bf03ba3cc62a326b42a38e5a5
- evidence_id: septin-s2351-outer-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009279,GO:0016020
  locator: 'Native issuing-authority response: exact identifier, label, taxon and
    returned annotation scope.'
  accessed_at: '2026-11-03T05:07:09.456197Z'
  support: supports
  summary: Exact current record identifiers and bounded authority annotations checked.
    Database attribution is distinguished from independent experimental inspection.
  snapshot_sha256: 4dab2fbd6cdf3233f76bc8d2da58dabff083fa6204c95a319289c6c61a318372
- evidence_id: septin-s2351-outer-agent-sl-0040
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0040.json
  locator: 'Native issuing-authority response: exact identifier, label, taxon and
    returned annotation scope.'
  accessed_at: '2026-11-03T05:07:09.483331Z'
  support: supports
  summary: Exact current record identifiers and bounded authority annotations checked.
    Database attribution is distinguished from independent experimental inspection.
  snapshot_sha256: 8a16f96e1b81277a31e7eb3c3384cb13f7786c94b59dcb95424bdeb5bb14a7d9
- evidence_id: septin-s2351-outer-agent-chebi-16412
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/16412/
  locator: 'Native issuing-authority response: exact identifier, label, taxon and
    returned annotation scope.'
  accessed_at: '2026-11-03T05:07:09.687173Z'
  support: supports
  summary: Exact current record identifiers and bounded authority annotations checked.
    Database attribution is distinguished from independent experimental inspection.
  snapshot_sha256: 1761021018cb0217a35ea9c6f9b5593f27e56c2c7d406dbeeb24f6870b43e940
- evidence_id: septin-s2351-outer-agent-tax-2
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2
  locator: 'Native issuing-authority response: exact identifier, label, taxon and
    returned annotation scope.'
  accessed_at: '2026-11-03T05:07:09.930623Z'
  support: supports
  summary: Exact current record identifiers and bounded authority annotations checked.
    Database attribution is distinguished from independent experimental inspection.
  snapshot_sha256: 314bd7723b8dea04f1840809fb74e06c514664fba9c6a0619e8f12e2a6dceef1
- evidence_id: septin-s2351-outer-agent-tax-562
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562
  locator: 'Native issuing-authority response: exact identifier, label, taxon and
    returned annotation scope.'
  accessed_at: '2026-11-03T05:07:10.004505Z'
  support: supports
  summary: Exact current record identifiers and bounded authority annotations checked.
    Database attribution is distinguished from independent experimental inspection.
  snapshot_sha256: ea038c30da3aab3426b7df16ce7a137cf2985e73d6ad8281971b9c390a74d2a8
- evidence_id: septin-s2351-outer-agent-tax-83333
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333
  locator: 'Native issuing-authority response: exact identifier, label, taxon and
    returned annotation scope.'
  accessed_at: '2026-11-03T05:07:10.032683Z'
  support: supports
  summary: Exact current record identifiers and bounded authority annotations checked.
    Database attribution is distinguished from independent experimental inspection.
  snapshot_sha256: f499fde9e4fcea85ff811b58a76a405669d32465a62eaf74240a48331b63d8e6
- evidence_id: septin-s2351-outer-agent-P0A910
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0A910.json
  locator: 'Native issuing-authority response: exact identifier, label, taxon and
    returned annotation scope.'
  accessed_at: '2026-11-03T05:07:10.460655Z'
  support: supports
  summary: Exact current record identifiers and bounded authority annotations checked.
    Database attribution is distinguished from independent experimental inspection.
  snapshot_sha256: f9c3d1a94ebd004e99060766ee6a38dd5cd3600b57586db84e3fc1a9d59bf0f8
- evidence_id: septin-s2351-outer-agent-query-ompA
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AompA%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29
  locator: Exact request URL and returned identity/metadata/abstract results.
  accessed_at: '2026-11-03T05:07:10.540312Z'
  support: supports
  summary: Bounded query with no universal absence claim; metadata and abstracts are
    not full scientific-body reads.
  snapshot_sha256: 6d5afaa99881ccc27553912308248a0ae9a68d686e019b97fa3fdb9ec3dc47aa
  search_scope: Database/request https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AompA%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29;
    exact query and pagination/limit encoded in that URL, executed 2026-11-03T05:07:10.540312Z;
    no publication-date restriction. Only returned results inspected. No exhaustive
    literature/biological absence assertion.
- evidence_id: septin-s2351-outer-agent-P06996
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P06996.json
  locator: 'Native issuing-authority response: exact identifier, label, taxon and
    returned annotation scope.'
  accessed_at: '2026-11-03T05:07:10.554157Z'
  support: supports
  summary: Exact current record identifiers and bounded authority annotations checked.
    Database attribution is distinguished from independent experimental inspection.
  snapshot_sha256: 54a36b2e065d96b31213df239cf617c89b616f16f030f303ee548d7fe56dc9c8
- evidence_id: septin-s2351-outer-agent-query-ompC
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AompC%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29
  locator: Exact request URL and returned identity/metadata/abstract results.
  accessed_at: '2026-11-03T05:07:10.596828Z'
  support: supports
  summary: Bounded query with no universal absence claim; metadata and abstracts are
    not full scientific-body reads.
  snapshot_sha256: 3427cbb25176813fe2877ce6da2675d0931c673339c36b58af3fc4340ff9f14b
  search_scope: Database/request https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AompC%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29;
    exact query and pagination/limit encoded in that URL, executed 2026-11-03T05:07:10.596828Z;
    no publication-date restriction. Only returned results inspected. No exhaustive
    literature/biological absence assertion.
- evidence_id: septin-s2351-outer-agent-P02931
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P02931.json
  locator: 'Native issuing-authority response: exact identifier, label, taxon and
    returned annotation scope.'
  accessed_at: '2026-11-03T05:07:10.644857Z'
  support: supports
  summary: Exact current record identifiers and bounded authority annotations checked.
    Database attribution is distinguished from independent experimental inspection.
  snapshot_sha256: 2579d79d43b13c340905e07df7efed1871c19dbe5a67eb133857f2d6e4df8a50
- evidence_id: septin-s2351-outer-agent-query-ompF
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AompF%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29
  locator: Exact request URL and returned identity/metadata/abstract results.
  accessed_at: '2026-11-03T05:07:11.870141Z'
  support: supports
  summary: Bounded query with no universal absence claim; metadata and abstracts are
    not full scientific-body reads.
  snapshot_sha256: ec6003b929dd8d0601b31f254d76acbff398acbd4cd7def61df3f1327ba18820
  search_scope: Database/request https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AompF%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29;
    exact query and pagination/limit encoded in that URL, executed 2026-11-03T05:07:11.870141Z;
    no publication-date restriction. Only returned results inspected. No exhaustive
    literature/biological absence assertion.
- evidence_id: septin-s2351-outer-agent-P0A940
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0A940.json
  locator: 'Native issuing-authority response: exact identifier, label, taxon and
    returned annotation scope.'
  accessed_at: '2026-11-03T05:07:12.905280Z'
  support: supports
  summary: Exact current record identifiers and bounded authority annotations checked.
    Database attribution is distinguished from independent experimental inspection.
  snapshot_sha256: 2ff846ae12669c4bab0ccd5ee26ee045bc2c77b2c49c18bfcf90adaee3a2296d
- evidence_id: septin-s2351-outer-agent-query-bamA
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AbamA%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29
  locator: Exact request URL and returned identity/metadata/abstract results.
  accessed_at: '2026-11-03T05:07:12.983493Z'
  support: supports
  summary: Bounded query with no universal absence claim; metadata and abstracts are
    not full scientific-body reads.
  snapshot_sha256: eedefca132b33d6adebab88357ec41c7c549af0160a80fe342ec9c5c2ed76809
  search_scope: Database/request https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AbamA%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29;
    exact query and pagination/limit encoded in that URL, executed 2026-11-03T05:07:12.983493Z;
    no publication-date restriction. Only returned results inspected. No exhaustive
    literature/biological absence assertion.
- evidence_id: septin-s2351-outer-agent-P31554
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P31554.json
  locator: 'Native issuing-authority response: exact identifier, label, taxon and
    returned annotation scope.'
  accessed_at: '2026-11-03T05:07:13.753256Z'
  support: supports
  summary: Exact current record identifiers and bounded authority annotations checked.
    Database attribution is distinguished from independent experimental inspection.
  snapshot_sha256: dbab992a253dc68cd2b7543da5236b46111557f1f37b9fdd619b4b81794bf178
- evidence_id: septin-s2351-outer-agent-query-lptD
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AlptD%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29
  locator: Exact request URL and returned identity/metadata/abstract results.
  accessed_at: '2026-11-03T05:07:13.923952Z'
  support: supports
  summary: Bounded query with no universal absence claim; metadata and abstracts are
    not full scientific-body reads.
  snapshot_sha256: 1cefffb7d372496094e05d2fcba958a834d1b35316006f0c3e13d60d143c15e5
  search_scope: Database/request https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AlptD%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29;
    exact query and pagination/limit encoded in that URL, executed 2026-11-03T05:07:13.923952Z;
    no publication-date restriction. Only returned results inspected. No exhaustive
    literature/biological absence assertion.
- evidence_id: septin-s2351-outer-agent-P77774
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P77774.json
  locator: 'Native issuing-authority response: exact identifier, label, taxon and
    returned annotation scope.'
  accessed_at: '2026-11-03T05:07:14.664299Z'
  support: supports
  summary: Exact current record identifiers and bounded authority annotations checked.
    Database attribution is distinguished from independent experimental inspection.
  snapshot_sha256: 2ef03b2f0a01756551013ff513ba85409096bdb8d13b57be1991bd465d1376e1
- evidence_id: septin-s2351-outer-agent-query-bamB
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AbamB%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29
  locator: Exact request URL and returned identity/metadata/abstract results.
  accessed_at: '2026-11-03T05:07:14.807690Z'
  support: supports
  summary: Bounded query with no universal absence claim; metadata and abstracts are
    not full scientific-body reads.
  snapshot_sha256: a5fb6bdb8a6d22d3789192420f7891e4f381de850cf4cc724acdffe4383b890e
  search_scope: Database/request https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AbamB%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29;
    exact query and pagination/limit encoded in that URL, executed 2026-11-03T05:07:14.807690Z;
    no publication-date restriction. Only returned results inspected. No exhaustive
    literature/biological absence assertion.
- evidence_id: septin-s2351-outer-agent-P0A903
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0A903.json
  locator: 'Native issuing-authority response: exact identifier, label, taxon and
    returned annotation scope.'
  accessed_at: '2026-11-03T05:07:15.842205Z'
  support: supports
  summary: Exact current record identifiers and bounded authority annotations checked.
    Database attribution is distinguished from independent experimental inspection.
  snapshot_sha256: 584c056225b866005264ce4b2288722d06ff5adf60d6f217a65b59e6b0c22c60
- evidence_id: septin-s2351-outer-agent-query-bamC
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AbamC%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29
  locator: Exact request URL and returned identity/metadata/abstract results.
  accessed_at: '2026-11-03T05:07:16.109899Z'
  support: supports
  summary: Bounded query with no universal absence claim; metadata and abstracts are
    not full scientific-body reads.
  snapshot_sha256: 073444923c46fbd03e5e35ea4c1d56f51a2e76205a35aee6e9b0d426378fd5f4
  search_scope: Database/request https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AbamC%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29;
    exact query and pagination/limit encoded in that URL, executed 2026-11-03T05:07:16.109899Z;
    no publication-date restriction. Only returned results inspected. No exhaustive
    literature/biological absence assertion.
- evidence_id: septin-s2351-outer-agent-P0AC02
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0AC02.json
  locator: 'Native issuing-authority response: exact identifier, label, taxon and
    returned annotation scope.'
  accessed_at: '2026-11-03T05:07:16.770728Z'
  support: supports
  summary: Exact current record identifiers and bounded authority annotations checked.
    Database attribution is distinguished from independent experimental inspection.
  snapshot_sha256: 97262e786c9e1d055dd17acbcc26d085df95a8e0206f10d3ad247dc545a4902b
- evidence_id: septin-s2351-outer-agent-query-bamD
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AbamD%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29
  locator: Exact request URL and returned identity/metadata/abstract results.
  accessed_at: '2026-11-03T05:07:17.855133Z'
  support: supports
  summary: Bounded query with no universal absence claim; metadata and abstracts are
    not full scientific-body reads.
  snapshot_sha256: 3863cd5db0a7c555cf2dba77d3a52ae3a8ebd3681a6821e8628e854c010497ca
  search_scope: Database/request https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AbamD%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29;
    exact query and pagination/limit encoded in that URL, executed 2026-11-03T05:07:17.855133Z;
    no publication-date restriction. Only returned results inspected. No exhaustive
    literature/biological absence assertion.
- evidence_id: septin-s2351-outer-agent-matches-P0A910
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P0A910/?page_size=200
  locator: Native InterPro protein matches with metadata accession/name/type fields.
  accessed_at: '2026-11-03T05:07:17.937649Z'
  support: supports
  summary: OmpA, porins and BamA span distinct families and domains; no one family
    CURIE covers the generic beta-barrel component. Family labels are not borrowed
    from domain or broad superfamily entries.
  snapshot_sha256: 0ec8cef330188977db2d695ed1bff88c43fa4dd7213eb2846cb058f488170496
- evidence_id: septin-s2351-outer-agent-matches-P06996
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P06996/?page_size=200
  locator: Native InterPro protein matches with metadata accession/name/type fields.
  accessed_at: '2026-11-03T05:07:18.792781Z'
  support: supports
  summary: OmpA, porins and BamA span distinct families and domains; no one family
    CURIE covers the generic beta-barrel component. Family labels are not borrowed
    from domain or broad superfamily entries.
  snapshot_sha256: 282f81594e0478ea33a48528727a19876beac6498ca177039e369a11e13a4cdb
- evidence_id: septin-s2351-outer-agent-matches-P02931
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P02931/?page_size=200
  locator: Native InterPro protein matches with metadata accession/name/type fields.
  accessed_at: '2026-11-03T05:07:19.116023Z'
  support: supports
  summary: OmpA, porins and BamA span distinct families and domains; no one family
    CURIE covers the generic beta-barrel component. Family labels are not borrowed
    from domain or broad superfamily entries.
  snapshot_sha256: fe51a1dea6b6cce726ced25038d8a4ff0291fccc15352e2b67c7d87dcf93f6c2
- evidence_id: septin-s2351-outer-agent-pmid-10636850
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID:10636850%20AND%20SRC:MED
  locator: Europe PMC exact PMID primary abstract and metadata only.
  accessed_at: '2026-11-03T05:07:19.735693Z'
  support: supports
  summary: Arora2000 refolded detergent-purified OmpA into planar bilayers and measured
    two conductance states. UniProt supplies the direct location-citation attribution;
    the abstract is not a full localization-method audit.
  snapshot_sha256: 6c68a6c4a20af32afa2878e1f9c0c3ae3aa5af483c997ac4e416d0c758eca9bd
  search_scope: Database/request https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID:10636850%20AND%20SRC:MED;
    exact query and pagination/limit encoded in that URL, executed 2026-11-03T05:07:19.735693Z;
    no publication-date restriction. Only returned results inspected. No exhaustive
    literature/biological absence assertion.
- evidence_id: septin-s2351-outer-agent-pmid-10947984
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID:10947984%20AND%20SRC:MED
  locator: Europe PMC exact PMID primary abstract and metadata only.
  accessed_at: '2026-11-03T05:07:19.754044Z'
  support: supports
  summary: Belaaouaj2000 describes OmpA surface localization and neutrophil-elastase
    degradation; exact UniProt citation attribution was separately checked.
  snapshot_sha256: 48f244f8ded248da943fd69f7754220a23c14ba0607363dcc0751a80f95b5928
  search_scope: Database/request https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID:10947984%20AND%20SRC:MED;
    exact query and pagination/limit encoded in that URL, executed 2026-11-03T05:07:19.754044Z;
    no publication-date restriction. Only returned results inspected. No exhaustive
    literature/biological absence assertion.
- evidence_id: septin-s2351-outer-agent-pmid-16079137
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID:16079137%20AND%20SRC:MED
  locator: Europe PMC exact PMID primary abstract and metadata only.
  accessed_at: '2026-11-03T05:07:19.991051Z'
  support: supports
  summary: Stenberg2005 reports blue native PAGE, second-dimension SDS-PAGE and mass
    spectrometry of E. coli envelope complexes. Individual protein-result tables and
    full experimental-stock methods were not read; reviewed K12 accession identity
    is not proof of stock equivalence.
  snapshot_sha256: 0c8a782dd1022fdd5016d2f9b2ca9cdb04e46072105f4233ec07edeff9af1d38
  search_scope: Database/request https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID:16079137%20AND%20SRC:MED;
    exact query and pagination/limit encoded in that URL, executed 2026-11-03T05:07:19.991051Z;
    no publication-date restriction. Only returned results inspected. No exhaustive
    literature/biological absence assertion.
- evidence_id: septin-s2351-outer-agent-pmid-23882017
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID:23882017%20AND%20SRC:MED
  locator: Europe PMC exact PMID primary abstract and metadata only.
  accessed_at: '2026-11-03T05:07:20.068660Z'
  support: supports
  summary: Ruhe2013 identifies BamA as the CdiA-EC93 receptor and bounds species/loop
    specificity. Location attribution is verified directly in UniProt; not all CDI
    experiments were independently reviewed.
  snapshot_sha256: d1fc76a41efb3d14a5349774a16b7033c4200c9fb052b648065a170ed65738a5
  search_scope: Database/request https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID:23882017%20AND%20SRC:MED;
    exact query and pagination/limit encoded in that URL, executed 2026-11-03T05:07:20.068660Z;
    no publication-date restriction. Only returned results inspected. No exhaustive
    literature/biological absence assertion.
- evidence_id: septin-s2351-outer-agent-pmid-24619089
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID:24619089%20AND%20SRC:MED
  locator: Europe PMC exact PMID primary abstract and metadata only.
  accessed_at: '2026-11-03T05:07:20.356973Z'
  support: supports
  summary: Ni2014 reports the E. coli BamA barrel structure and mutational effects.
    Proposed substrate-insertion details remain proposal-tier; the current record
    only needs the bounded outer-membrane assembly claim.
  snapshot_sha256: 3bf39231ef314853e692c8623395a61975e81ced049781a81fa178ed3ef25824
  search_scope: Database/request https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID:24619089%20AND%20SRC:MED;
    exact query and pagination/limit encoded in that URL, executed 2026-11-03T05:07:20.356973Z;
    no publication-date restriction. Only returned results inspected. No exhaustive
    literature/biological absence assertion.
- evidence_id: septin-s2351-outer-agent-pmid-2464593
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID:2464593%20AND%20SRC:MED
  locator: Europe PMC exact PMID primary abstract and metadata only.
  accessed_at: '2026-11-03T05:07:20.399636Z'
  support: supports
  summary: Gehring/Nikaido1989 reports purification of K12 OmpC/OmpF/PhoE heterotrimers
    and expression-dependent distribution; this corroborates source identity, not
    a universal three-protein membrane inventory.
  snapshot_sha256: 0e12629ff3fa85f38336a4940f54b4f000651afcd6a0a08eeef91b97438edc55
  search_scope: Database/request https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID:2464593%20AND%20SRC:MED;
    exact query and pagination/limit encoded in that URL, executed 2026-11-03T05:07:20.399636Z;
    no publication-date restriction. Only returned results inspected. No exhaustive
    literature/biological absence assertion.
- evidence_id: septin-s2351-outer-agent-doi-cshperspect_a000414
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1101/cshperspect.a000414
  locator: Exact request URL and returned identity/metadata/abstract results.
  accessed_at: '2026-11-03T05:07:20.454795Z'
  support: supports
  summary: Bounded query with no universal absence claim; metadata and abstracts are
    not full scientific-body reads.
  snapshot_sha256: 6dbe4b87edaa5c136c12c86c9d1dd160a184f8e75b68e56095dcffb08d567992
  search_scope: Database/request https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1101/cshperspect.a000414;
    exact query and pagination/limit encoded in that URL, executed 2026-11-03T05:07:20.454795Z;
    no publication-date restriction. Only returned results inspected. No exhaustive
    literature/biological absence assertion.
- evidence_id: septin-s2351-outer-agent-doi-jbc_R117_802512
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1074/jbc.R117.802512
  locator: Exact request URL and returned identity/metadata/abstract results.
  accessed_at: '2026-11-03T05:07:20.624601Z'
  support: supports
  summary: Bounded query with no universal absence claim; metadata and abstracts are
    not full scientific-body reads.
  snapshot_sha256: 98254752516a0fc494415ca975d762b2b158a3b477720e19c9ef73ed9f90e7fa
  search_scope: Database/request https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1074/jbc.R117.802512;
    exact query and pagination/limit encoded in that URL, executed 2026-11-03T05:07:20.624601Z;
    no publication-date restriction. Only returned results inspected. No exhaustive
    literature/biological absence assertion.
- evidence_id: septin-s2351-outer-agent-doi-annurev-biochem-061408-144611
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1146/annurev-biochem-061408-144611
  locator: Exact request URL and returned identity/metadata/abstract results.
  accessed_at: '2026-11-03T05:07:20.671709Z'
  support: supports
  summary: Bounded query with no universal absence claim; metadata and abstracts are
    not full scientific-body reads.
  snapshot_sha256: 725afd2f9dc5bbc1ec004051a5e4958c9bfbcdc9e6471ca6c82e5bcc27295455
  search_scope: Database/request https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1146/annurev-biochem-061408-144611;
    exact query and pagination/limit encoded in that URL, executed 2026-11-03T05:07:20.671709Z;
    no publication-date restriction. Only returned results inspected. No exhaustive
    literature/biological absence assertion.
- evidence_id: septin-s2351-outer-agent-doi-MMBR_67_4_593-656_2003
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1128/MMBR.67.4.593-656.2003
  locator: Exact request URL and returned identity/metadata/abstract results.
  accessed_at: '2026-11-03T05:07:21.011966Z'
  support: supports
  summary: Bounded query with no universal absence claim; metadata and abstracts are
    not full scientific-body reads.
  snapshot_sha256: c84f43596bae4ea42f992fa8627c1db390ed2c9640e41223452b4317ad6aff55
  search_scope: Database/request https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1128/MMBR.67.4.593-656.2003;
    exact query and pagination/limit encoded in that URL, executed 2026-11-03T05:07:21.011966Z;
    no publication-date restriction. Only returned results inspected. No exhaustive
    literature/biological absence assertion.
- evidence_id: septin-s2351-outer-agent-silhavy2010-legacy-html
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2857177/
  locator: 'Secondary review: Gram-negative outer membrane composition/assembly and
    Corynebacterineae sections.'
  accessed_at: '2026-11-03T05:07:21.032298Z'
  support: supports
  summary: Canonical Gram-negative LPS/phospholipid asymmetry, beta-barrel proteins
    and porin-mediated permeability are supported. The review separately describes
    a mycolic outer membrane with different composition and no obvious BAM homologs;
    canonical graphs must retain their Gram-negative scope.
  snapshot_sha256: bf8bf5bab219f9b017cfeee6b5a9ba9682a372a708e9459067b15ca71eb19fc4
- evidence_id: septin-s2351-outer-agent-sperandeo2017-legacy-html
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5672026/
  locator: 'Secondary review: LPS structure/essentiality exceptions, LPS transport
    and LptB2CFG/LptA/LptDE sections, corresponding captions; underlying studies not
    independently reproduced.'
  accessed_at: '2026-11-03T05:07:21.095027Z'
  support: supports
  summary: Seven E. coli Lpt proteins form a transenvelope machine; extraction follows
    MsbA flipping, and LptDE delivers LPS to the outer membrane. Canonical transport
    has noncanonical exceptions. LPS-deficient Neisseria, Moraxella and Acinetobacter
    examples support retaining CONDITIONAL rather than universal LPS indispensability.
  snapshot_sha256: b9da62d7ffa8f7a26fc049a08c41b9fc7a47c2b575b2cae8513dff229951f911
- evidence_id: septin-s2351-outer-agent-hagan2011-pdf
  kind: authority
  reference: https://prokaryotics.com/wp-content/uploads/2017/02/Hagan-et-al-2011.pdf
  locator: 'Secondary review PDF: overview/Figure1 caption, BAM composition, folding/insertion
    and BamB efficiency passages, pp191–202; no figure pixels or underlying primary
    raw data.'
  accessed_at: '2026-11-03T05:07:21.281504Z'
  support: supports
  summary: The five-protein E. coli BAM complex folds and inserts beta-barrel proteins.
    A/B/C/D xrefs in the record are representative rather than a full inventory; absence
    of BamE from those links is not a claim of its biological absence. Activity, efficiency
    and membership do not prove universal assembly necessity.
  snapshot_sha256: 669fe7858117af4b8e258e732d00b1e47af168cf23a6c3665a027f1232d59276
- evidence_id: septin-s2351-outer-agent-nikaido2003-browser1
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC309051
  locator: 'Genuine freshly retrieved PMC secondary-review body: Protein Channels,
    porin selectivity/regulation, ordered LPS layer and lipid-bilayer permeability
    passages.'
  accessed_at: '2026-11-03T05:07:21.369158Z'
  support: supports
  summary: Porins admit hydrophilic solutes selectively; ordered LPS slows lipid-phase
    entry. This supports the explicitly reduced-influx meaning of excludes, not absolute
    impermeability. Historical failure to fetch this body no longer describes this
    current successful retrieval.
  snapshot_sha256: 208143e0deaf0cc841ec751005c52650953ddae65e885dad769a97db8cc9d531
- evidence_id: septin-s2351-current-adapter-catalogue
  kind: authority
  reference: https://imodulondb.org/api/datasets
  locator: 'Entire official /api/datasets response: 20 organism objects and 28 dataset
    keys.'
  accessed_at: '2026-11-03T05:07:21.546677Z'
  support: supports
  summary: No Cereibacter/Rhodobacter or Saccharomyces dataset occurs in this returned
    catalogue. E. coli precise1k matches outer-membrane examples. This bounded catalogue
    result does not imply biological gene absence; unrelated Bradyrhizobium or cyanobacterial
    datasets are not substituted for the RC-LH1 strain.
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: septin-s2351-adapter-search-ompA
  kind: search
  reference: https://imodulondb.org/api/search?organism=e_coli&dataset=precise1k&query=ompA&limit=50
  locator: Exact request URL and returned identity/metadata/abstract results.
  accessed_at: '2026-11-03T05:08:13.371100Z'
  support: supports
  summary: Bounded query with no universal absence claim; metadata and abstracts are
    not full scientific-body reads.
  snapshot_sha256: 57d373c02845346c24cf7342860ca2020ec7af02400cf12a7f80b8ce451a93a3
  search_scope: Database/request https://imodulondb.org/api/search?organism=e_coli&dataset=precise1k&query=ompA&limit=50;
    exact query and pagination/limit encoded in that URL, executed 2026-11-03T05:08:13.371100Z;
    no publication-date restriction. Only returned results inspected. No exhaustive
    literature/biological absence assertion.
- evidence_id: septin-s2351-adapter-search-ompC
  kind: search
  reference: https://imodulondb.org/api/search?organism=e_coli&dataset=precise1k&query=ompC&limit=50
  locator: Exact request URL and returned identity/metadata/abstract results.
  accessed_at: '2026-11-03T05:08:13.371374Z'
  support: supports
  summary: Bounded query with no universal absence claim; metadata and abstracts are
    not full scientific-body reads.
  snapshot_sha256: 2d0a4fdab6983c7b364374a2351dde8f119173d7382a155c9c3b5bca890f9486
  search_scope: Database/request https://imodulondb.org/api/search?organism=e_coli&dataset=precise1k&query=ompC&limit=50;
    exact query and pagination/limit encoded in that URL, executed 2026-11-03T05:08:13.371374Z;
    no publication-date restriction. Only returned results inspected. No exhaustive
    literature/biological absence assertion.
- evidence_id: septin-s2351-adapter-search-ompF
  kind: search
  reference: https://imodulondb.org/api/search?organism=e_coli&dataset=precise1k&query=ompF&limit=50
  locator: Exact request URL and returned identity/metadata/abstract results.
  accessed_at: '2026-11-03T05:08:13.371447Z'
  support: supports
  summary: Bounded query with no universal absence claim; metadata and abstracts are
    not full scientific-body reads.
  snapshot_sha256: d6ad04affed0791761664803d356eaea18fb63825f077e7ad563e4060a01604c
  search_scope: Database/request https://imodulondb.org/api/search?organism=e_coli&dataset=precise1k&query=ompF&limit=50;
    exact query and pagination/limit encoded in that URL, executed 2026-11-03T05:08:13.371447Z;
    no publication-date restriction. Only returned results inspected. No exhaustive
    literature/biological absence assertion.
- evidence_id: septin-s2351-adapter-search-bamA
  kind: search
  reference: https://imodulondb.org/api/search?organism=e_coli&dataset=precise1k&query=bamA&limit=50
  locator: Exact request URL and returned identity/metadata/abstract results.
  accessed_at: '2026-11-03T05:08:13.371505Z'
  support: supports
  summary: Bounded query with no universal absence claim; metadata and abstracts are
    not full scientific-body reads.
  snapshot_sha256: 6c0f62a47247f94710b21140f0a251b70ed692496dbe13c3d297624a5620f1a4
  search_scope: Database/request https://imodulondb.org/api/search?organism=e_coli&dataset=precise1k&query=bamA&limit=50;
    exact query and pagination/limit encoded in that URL, executed 2026-11-03T05:08:13.371505Z;
    no publication-date restriction. Only returned results inspected. No exhaustive
    literature/biological absence assertion.
- evidence_id: septin-s2351-adapter-search-bamB
  kind: search
  reference: https://imodulondb.org/api/search?organism=e_coli&dataset=precise1k&query=bamB&limit=50
  locator: Exact request URL and returned identity/metadata/abstract results.
  accessed_at: '2026-11-03T05:08:13.538116Z'
  support: supports
  summary: Bounded query with no universal absence claim; metadata and abstracts are
    not full scientific-body reads.
  snapshot_sha256: d2990c6a0b01e4312334f51776c0feaf80dfbc2e8d04da526ffcd6cc792b819a
  search_scope: Database/request https://imodulondb.org/api/search?organism=e_coli&dataset=precise1k&query=bamB&limit=50;
    exact query and pagination/limit encoded in that URL, executed 2026-11-03T05:08:13.538116Z;
    no publication-date restriction. Only returned results inspected. No exhaustive
    literature/biological absence assertion.
- evidence_id: septin-s2351-adapter-search-bamC
  kind: search
  reference: https://imodulondb.org/api/search?organism=e_coli&dataset=precise1k&query=bamC&limit=50
  locator: Exact request URL and returned identity/metadata/abstract results.
  accessed_at: '2026-11-03T05:08:13.552115Z'
  support: supports
  summary: Bounded query with no universal absence claim; metadata and abstracts are
    not full scientific-body reads.
  snapshot_sha256: f4621e9ed5f2fda06713de3602f9929636cb1b8cea05f96fb6985cd483e32b1a
  search_scope: Database/request https://imodulondb.org/api/search?organism=e_coli&dataset=precise1k&query=bamC&limit=50;
    exact query and pagination/limit encoded in that URL, executed 2026-11-03T05:08:13.552115Z;
    no publication-date restriction. Only returned results inspected. No exhaustive
    literature/biological absence assertion.
- evidence_id: septin-s2351-adapter-search-bamD
  kind: search
  reference: https://imodulondb.org/api/search?organism=e_coli&dataset=precise1k&query=bamD&limit=50
  locator: Exact request URL and returned identity/metadata/abstract results.
  accessed_at: '2026-11-03T05:08:13.552198Z'
  support: supports
  summary: Bounded query with no universal absence claim; metadata and abstracts are
    not full scientific-body reads.
  snapshot_sha256: a9db3aaf2fa953eb669bd4e572ba7f6a0e007429d7ce3a5b47944f673b7f6e6a
  search_scope: Database/request https://imodulondb.org/api/search?organism=e_coli&dataset=precise1k&query=bamD&limit=50;
    exact query and pagination/limit encoded in that URL, executed 2026-11-03T05:08:13.552198Z;
    no publication-date restriction. Only returned results inspected. No exhaustive
    literature/biological absence assertion.
- evidence_id: septin-s2351-adapter-search-lptD
  kind: search
  reference: https://imodulondb.org/api/search?organism=e_coli&dataset=precise1k&query=lptD&limit=50
  locator: Exact request URL and returned identity/metadata/abstract results.
  accessed_at: '2026-11-03T05:08:13.552279Z'
  support: supports
  summary: Bounded query with no universal absence claim; metadata and abstracts are
    not full scientific-body reads.
  snapshot_sha256: 10033adff8da3183e3df0eab00c9a918104a3a019e10d30096aac4e656199d20
  search_scope: Database/request https://imodulondb.org/api/search?organism=e_coli&dataset=precise1k&query=lptD&limit=50;
    exact query and pagination/limit encoded in that URL, executed 2026-11-03T05:08:13.552279Z;
    no publication-date restriction. Only returned results inspected. No exhaustive
    literature/biological absence assertion.
- evidence_id: septin-s2351-outer-agent-matches-P0A940-retry
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P0A940/?page_size=200
  locator: Native InterPro protein matches with metadata accession/name/type fields.
  accessed_at: '2026-11-03T05:08:13.577524Z'
  support: supports
  summary: OmpA, porins and BamA span distinct families and domains; no one family
    CURIE covers the generic beta-barrel component. Family labels are not borrowed
    from domain or broad superfamily entries.
  snapshot_sha256: 3ef38d21a63df56c8548383507aa702e5e0eb353bd04a67d3e7e6b2503ed5fc6
- evidence_id: septin-s2351-adapter-gene-ompA
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b0957
  locator: Exact E. coli precise1k gene identity or complete 201-item returned gene-module
    array; is_in_imodulon, gene_weight and threshold fields.
  accessed_at: '2026-11-03T05:10:39.118051Z'
  support: supports
  summary: 'Eight exact gene identities agree with their UniProt/locus mappings. Only
    ompF has positive memberships in the inspected arrays: UC-3 k86, Nitrogen k88,
    Lrp k25 and SoxS k22. Seven empty positive sets mean only no thresholded membership
    in this one returned dataset.'
  snapshot_sha256: 255be02a9edb276bfb29651f1e6053d893ff28a5e1c988cabcce87f43aed41c8
- evidence_id: septin-s2351-adapter-modules-ompA
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b0957/imodulons
  locator: Exact E. coli precise1k gene identity or complete 201-item returned gene-module
    array; is_in_imodulon, gene_weight and threshold fields.
  accessed_at: '2026-11-03T05:10:39.118324Z'
  support: supports
  summary: 'Eight exact gene identities agree with their UniProt/locus mappings. Only
    ompF has positive memberships in the inspected arrays: UC-3 k86, Nitrogen k88,
    Lrp k25 and SoxS k22. Seven empty positive sets mean only no thresholded membership
    in this one returned dataset.'
  snapshot_sha256: 6ff6279882b415cc2194933218f174d05ce02fdfe3ff967c79466f67644c5910
- evidence_id: septin-s2351-adapter-gene-ompC
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b2215
  locator: Exact E. coli precise1k gene identity or complete 201-item returned gene-module
    array; is_in_imodulon, gene_weight and threshold fields.
  accessed_at: '2026-11-03T05:10:39.118425Z'
  support: supports
  summary: 'Eight exact gene identities agree with their UniProt/locus mappings. Only
    ompF has positive memberships in the inspected arrays: UC-3 k86, Nitrogen k88,
    Lrp k25 and SoxS k22. Seven empty positive sets mean only no thresholded membership
    in this one returned dataset.'
  snapshot_sha256: b226c373883f01798e411b415810f76f4adaa316bb2b6c66d61383fa69973bdd
- evidence_id: septin-s2351-adapter-modules-ompC
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b2215/imodulons
  locator: Exact E. coli precise1k gene identity or complete 201-item returned gene-module
    array; is_in_imodulon, gene_weight and threshold fields.
  accessed_at: '2026-11-03T05:10:39.118480Z'
  support: supports
  summary: 'Eight exact gene identities agree with their UniProt/locus mappings. Only
    ompF has positive memberships in the inspected arrays: UC-3 k86, Nitrogen k88,
    Lrp k25 and SoxS k22. Seven empty positive sets mean only no thresholded membership
    in this one returned dataset.'
  snapshot_sha256: 03d2d8ce328157b51445eb27815b3e60da30176ef4bcad345daa0926870be27a
- evidence_id: septin-s2351-adapter-gene-ompF
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b0929
  locator: Exact E. coli precise1k gene identity or complete 201-item returned gene-module
    array; is_in_imodulon, gene_weight and threshold fields.
  accessed_at: '2026-11-03T05:10:39.118528Z'
  support: supports
  summary: 'Eight exact gene identities agree with their UniProt/locus mappings. Only
    ompF has positive memberships in the inspected arrays: UC-3 k86, Nitrogen k88,
    Lrp k25 and SoxS k22. Seven empty positive sets mean only no thresholded membership
    in this one returned dataset.'
  snapshot_sha256: d382e44f5e7c704e98ba7862590a03751a4092658e072a7a68cab0c5cfa70e78
- evidence_id: septin-s2351-adapter-modules-ompF
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b0929/imodulons
  locator: Exact E. coli precise1k gene identity or complete 201-item returned gene-module
    array; is_in_imodulon, gene_weight and threshold fields.
  accessed_at: '2026-11-03T05:10:39.302907Z'
  support: supports
  summary: 'Eight exact gene identities agree with their UniProt/locus mappings. Only
    ompF has positive memberships in the inspected arrays: UC-3 k86, Nitrogen k88,
    Lrp k25 and SoxS k22. Seven empty positive sets mean only no thresholded membership
    in this one returned dataset.'
  snapshot_sha256: 89765eaa8083bb03039e6d65594a94b37548293e2218c0f35a0b0b5c1420b213
- evidence_id: septin-s2351-adapter-gene-bamA
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b0177
  locator: Exact E. coli precise1k gene identity or complete 201-item returned gene-module
    array; is_in_imodulon, gene_weight and threshold fields.
  accessed_at: '2026-11-03T05:10:39.306065Z'
  support: supports
  summary: 'Eight exact gene identities agree with their UniProt/locus mappings. Only
    ompF has positive memberships in the inspected arrays: UC-3 k86, Nitrogen k88,
    Lrp k25 and SoxS k22. Seven empty positive sets mean only no thresholded membership
    in this one returned dataset.'
  snapshot_sha256: 135ba88f229400ab1167339abcd218a0d7ab9285cad0161d824f5b0b682850ba
- evidence_id: septin-s2351-adapter-modules-bamA
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b0177/imodulons
  locator: Exact E. coli precise1k gene identity or complete 201-item returned gene-module
    array; is_in_imodulon, gene_weight and threshold fields.
  accessed_at: '2026-11-03T05:10:39.323879Z'
  support: supports
  summary: 'Eight exact gene identities agree with their UniProt/locus mappings. Only
    ompF has positive memberships in the inspected arrays: UC-3 k86, Nitrogen k88,
    Lrp k25 and SoxS k22. Seven empty positive sets mean only no thresholded membership
    in this one returned dataset.'
  snapshot_sha256: cf2ad3165680870022ee6e8471ebe6641d84983d60b919240bbcd8ddc4055919
- evidence_id: septin-s2351-adapter-gene-bamB
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b2512
  locator: Exact E. coli precise1k gene identity or complete 201-item returned gene-module
    array; is_in_imodulon, gene_weight and threshold fields.
  accessed_at: '2026-11-03T05:10:39.347616Z'
  support: supports
  summary: 'Eight exact gene identities agree with their UniProt/locus mappings. Only
    ompF has positive memberships in the inspected arrays: UC-3 k86, Nitrogen k88,
    Lrp k25 and SoxS k22. Seven empty positive sets mean only no thresholded membership
    in this one returned dataset.'
  snapshot_sha256: 1077a0b58591f3cb857ae41eda3bf64c818d3ed374c2142b5019f95bd6bedc33
- evidence_id: septin-s2351-adapter-modules-bamB
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b2512/imodulons
  locator: Exact E. coli precise1k gene identity or complete 201-item returned gene-module
    array; is_in_imodulon, gene_weight and threshold fields.
  accessed_at: '2026-11-03T05:10:39.351898Z'
  support: supports
  summary: 'Eight exact gene identities agree with their UniProt/locus mappings. Only
    ompF has positive memberships in the inspected arrays: UC-3 k86, Nitrogen k88,
    Lrp k25 and SoxS k22. Seven empty positive sets mean only no thresholded membership
    in this one returned dataset.'
  snapshot_sha256: 3c644cbd1c71c6e7daab29f4ecd164fb64e0948464cd0573b540d9eec15da026
- evidence_id: septin-s2351-adapter-gene-bamC
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b2477
  locator: Exact E. coli precise1k gene identity or complete 201-item returned gene-module
    array; is_in_imodulon, gene_weight and threshold fields.
  accessed_at: '2026-11-03T05:10:39.364201Z'
  support: supports
  summary: 'Eight exact gene identities agree with their UniProt/locus mappings. Only
    ompF has positive memberships in the inspected arrays: UC-3 k86, Nitrogen k88,
    Lrp k25 and SoxS k22. Seven empty positive sets mean only no thresholded membership
    in this one returned dataset.'
  snapshot_sha256: 63a8d9a6310af64249784420953f4ac10ad6000ffece93fc2501569e66d11b7a
- evidence_id: septin-s2351-adapter-modules-bamC
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b2477/imodulons
  locator: Exact E. coli precise1k gene identity or complete 201-item returned gene-module
    array; is_in_imodulon, gene_weight and threshold fields.
  accessed_at: '2026-11-03T05:10:39.377919Z'
  support: supports
  summary: 'Eight exact gene identities agree with their UniProt/locus mappings. Only
    ompF has positive memberships in the inspected arrays: UC-3 k86, Nitrogen k88,
    Lrp k25 and SoxS k22. Seven empty positive sets mean only no thresholded membership
    in this one returned dataset.'
  snapshot_sha256: 8875aa634a0d63a739af351aff803c2c6242dc87579bbdbc325825f91cf49ade
- evidence_id: septin-s2351-adapter-gene-bamD
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b2595
  locator: Exact E. coli precise1k gene identity or complete 201-item returned gene-module
    array; is_in_imodulon, gene_weight and threshold fields.
  accessed_at: '2026-11-03T05:10:39.394055Z'
  support: supports
  summary: 'Eight exact gene identities agree with their UniProt/locus mappings. Only
    ompF has positive memberships in the inspected arrays: UC-3 k86, Nitrogen k88,
    Lrp k25 and SoxS k22. Seven empty positive sets mean only no thresholded membership
    in this one returned dataset.'
  snapshot_sha256: 5379dadf0de6300cf3e0da69d550ecd454aacfa05428a0ec4c42ba39a272f7db
- evidence_id: septin-s2351-adapter-modules-bamD
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b2595/imodulons
  locator: Exact E. coli precise1k gene identity or complete 201-item returned gene-module
    array; is_in_imodulon, gene_weight and threshold fields.
  accessed_at: '2026-11-03T05:10:39.397881Z'
  support: supports
  summary: 'Eight exact gene identities agree with their UniProt/locus mappings. Only
    ompF has positive memberships in the inspected arrays: UC-3 k86, Nitrogen k88,
    Lrp k25 and SoxS k22. Seven empty positive sets mean only no thresholded membership
    in this one returned dataset.'
  snapshot_sha256: 85618d471c808bcbc0c96f6b390f1db965e6b7e5cf2ad1d415bb766ff75e728e
- evidence_id: septin-s2351-adapter-gene-lptD
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b0054
  locator: Exact E. coli precise1k gene identity or complete 201-item returned gene-module
    array; is_in_imodulon, gene_weight and threshold fields.
  accessed_at: '2026-11-03T05:10:39.409256Z'
  support: supports
  summary: 'Eight exact gene identities agree with their UniProt/locus mappings. Only
    ompF has positive memberships in the inspected arrays: UC-3 k86, Nitrogen k88,
    Lrp k25 and SoxS k22. Seven empty positive sets mean only no thresholded membership
    in this one returned dataset.'
  snapshot_sha256: afbb01c7d50a3e0554edc74d97d72c73233e9bb57ebdc0f3084414473b766bd6
- evidence_id: septin-s2351-adapter-modules-lptD
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b0054/imodulons
  locator: Exact E. coli precise1k gene identity or complete 201-item returned gene-module
    array; is_in_imodulon, gene_weight and threshold fields.
  accessed_at: '2026-11-03T05:10:39.418578Z'
  support: supports
  summary: 'Eight exact gene identities agree with their UniProt/locus mappings. Only
    ompF has positive memberships in the inspected arrays: UC-3 k86, Nitrogen k88,
    Lrp k25 and SoxS k22. Seven empty positive sets mean only no thresholded membership
    in this one returned dataset.'
  snapshot_sha256: b7cb5257aaf8002c3e66ba15137cf03baa4e2ad2808259ece68763901d61df4e
- evidence_id: septin-s2351-adapter-module-86
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise1k/86
  locator: Native precise1k module identity, regulator, function_description, threshold
    and gene-membership fields. ai_summary and other generated prose excluded.
  accessed_at: '2026-11-03T05:11:04.077542Z'
  support: supports
  summary: Structured expression context only; module association does not establish
    physical membership, assembly necessity, cell viability or causal function. UC-3
    is unknown; other relevant labels are Nac/nitrogen limitation, Lrp and SoxS.
  snapshot_sha256: dc010f69722e02c028497d05f252908be133ea75b0326156e53b8c3701ac8c8b
- evidence_id: septin-s2351-adapter-module-88
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise1k/88
  locator: Native precise1k module identity, regulator, function_description, threshold
    and gene-membership fields. ai_summary and other generated prose excluded.
  accessed_at: '2026-11-03T05:11:04.077898Z'
  support: supports
  summary: Structured expression context only; module association does not establish
    physical membership, assembly necessity, cell viability or causal function. UC-3
    is unknown; other relevant labels are Nac/nitrogen limitation, Lrp and SoxS.
  snapshot_sha256: 68d0e2ac5b8f540bcaa80ba7f5f49fc27cfc313ad5e57b194df6d57c14210c23
- evidence_id: septin-s2351-adapter-module-25
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise1k/25
  locator: Native precise1k module identity, regulator, function_description, threshold
    and gene-membership fields. ai_summary and other generated prose excluded.
  accessed_at: '2026-11-03T05:11:04.077997Z'
  support: supports
  summary: Structured expression context only; module association does not establish
    physical membership, assembly necessity, cell viability or causal function. UC-3
    is unknown; other relevant labels are Nac/nitrogen limitation, Lrp and SoxS.
  snapshot_sha256: c9b5cb0e23bfd76f68f6d36d05f1e7b4e86c817963c523a440a5a01068f1f288
- evidence_id: septin-s2351-adapter-module-22
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise1k/22
  locator: Native precise1k module identity, regulator, function_description, threshold
    and gene-membership fields. ai_summary and other generated prose excluded.
  accessed_at: '2026-11-03T05:11:04.078058Z'
  support: supports
  summary: Structured expression context only; module association does not establish
    physical membership, assembly necessity, cell viability or causal function. UC-3
    is unknown; other relevant labels are Nac/nitrogen limitation, Lrp and SoxS.
  snapshot_sha256: 75c93e893c864c0c0a515a7fb566fa97ed84141f008da563c9174b27e41e2703
- evidence_id: septin-s2351-comayras-indexed-body
  kind: primary_source
  reference: https://www.researchgate.net/publication/8099149_Functional_consequences_of_the_organization_of_the_photosynthetic_apparatus_in_Rhodobacter_sphaeroides_I_Quinone_domains_and_excitation_transfer_in_chromatophores_and_reaction_centerantenna_complexes
  locator: 'Fresh indexed coauthor-shared primary-paper rendering, returned lines0–626:
    abstract, figure captions, Introduction, strain/preparation Methods and beginning
    of spectroscopy/photoreduction methods. Remaining body/supplement not claimed
    read.'
  accessed_at: '2026-11-03T05:11:49.615Z'
  support: supports
  summary: Ga-strain monomers/dimers and chromatophores, optical excitation/quinone
    assays, purified-complex context and related PufX prior literature are distinguishable.
    No new whole-body/native download, universal interdimer transport or directly
    located PufX is claimed. The native URL returned403; this evidence is the browser-indexed
    passage.
  snapshot_sha256: 7dbc7845cc44297f5094757bdf6a10456f62dc084889447eea4355c9f1866f1e
- evidence_id: septin-s2351-bounded-publication-search
  kind: search
  reference: https://doi.org/10.1074/jbc.M412088200
  locator: Saved browser returned search response; only exact matching Comayras source
    and Forgac metadata used. Unrelated returned papers were not treated as evidence.
  accessed_at: '2026-11-03T05:11:42.138Z'
  support: supports
  summary: Indexed publisher result qualifies interdimer excitation as infrequent.
    Search finds source access routes; it does not show full-paper reading or literature
    absence.
  search_scope: Web search executed 2026-11-03T05:11:42.138Z; three exact queries
    ['"10.1074/jbc.M412088200" "interdimer" "quinone"', '"10.1074/jbc.M412088200"
    "PufX" "excitation"', '"10.1038/nrm2272" "ATP hydrolysis" "V1"']; response_length
    long, no date/domain restriction, no result pagination or follow-up exhaustive
    search. Only explicitly cited returned sources used.
  snapshot_sha256: 7dbc7845cc44297f5094757bdf6a10456f62dc084889447eea4355c9f1866f1e
- evidence_id: septin-s2351-record-rc_lh1_pufx_core_complex
  kind: record_content
  reference: data/structures/energy_complex/rc_lh1_pufx_core_complex.yaml
  locator: Complete current YAML at source head3266d0f7239a80f17d74bb0d6e2b3e260000b8dc,
    all nodes/edges, evidence, examples and discussions.
  accessed_at: '2026-11-03T05:15:01.515968Z'
  support: supports
  summary: Current bytes equal original target frozen hash. Complete read-only scientific
    assessment; no record edit.
  snapshot_sha256: 0a3a6fcfe54b7a355fd2903992f521fb2fc293ce984d4ede356dbc8460071824
- evidence_id: septin-s2351-record-vacuolar_proton_transporting_v_type_atpase_v0_domain
  kind: record_content
  reference: data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_v0_domain.yaml
  locator: Complete current YAML at source head3266d0f7239a80f17d74bb0d6e2b3e260000b8dc,
    all nodes/edges, evidence, examples and discussions.
  accessed_at: '2026-11-03T05:15:01.515968Z'
  support: supports
  summary: Current bytes equal original target frozen hash. Complete read-only scientific
    assessment; no record edit.
  snapshot_sha256: b76891f7e50630db7612669a25299babae68eb2e480724de8209094cc1953c48
- evidence_id: septin-s2351-record-vacuolar_proton_transporting_v_type_atpase_v1_domain
  kind: record_content
  reference: data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_v1_domain.yaml
  locator: Complete current YAML at source head3266d0f7239a80f17d74bb0d6e2b3e260000b8dc,
    all nodes/edges, evidence, examples and discussions.
  accessed_at: '2026-11-03T05:15:01.515968Z'
  support: supports
  summary: Current bytes equal original target frozen hash. Complete read-only scientific
    assessment; no record edit.
  snapshot_sha256: fabfca0b7f5ff5ee1340a6874918e4505c242d7939734a2e9ef8f3df5ebeeb22
- evidence_id: septin-s2351-record-cell_outer_membrane
  kind: record_content
  reference: data/structures/envelope/cell_outer_membrane.yaml
  locator: Complete current YAML at source head3266d0f7239a80f17d74bb0d6e2b3e260000b8dc,
    all nodes/edges, evidence, examples and discussions.
  accessed_at: '2026-11-03T05:15:01.515968Z'
  support: supports
  summary: Current bytes equal original target frozen hash. Complete read-only scientific
    assessment; no record edit.
  snapshot_sha256: 6a21a7409a3e93aa290cbff61f4734629b927f04a33c469e6166ef1b24673fab
- evidence_id: septin-s2351-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Current frozen local source; relevant components, context-link or CausalNodeTypeEnum
    passage.
  accessed_at: '2026-11-03T05:15:01.515968Z'
  support: supports
  summary: Known constituents may use source-bounded labels without guessed family
    IDs. Named genes/pathways require structured-source applicability assessment.
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
- evidence_id: septin-s2351-lh2-context
  kind: record_content
  reference: data/structures/energy_complex/lh2_peripheral_light_harvesting_antenna_complex.yaml
  locator: Current frozen local source; relevant components, context-link or CausalNodeTypeEnum
    passage.
  accessed_at: '2026-11-03T05:15:01.515968Z'
  support: supports
  summary: Frozen LH2 neighbor resolves the local graph link and bounds core receiver
    context to C. sphaeroides; it is not independent external evidence.
  snapshot_sha256: 4bb84c48c2bb27f1a8dded06f479771b494070977ef26e0b14f0708bc446a7ce
- evidence_id: septin-s2351-node-types
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Current frozen local source; relevant components, context-link or CausalNodeTypeEnum
    passage.
  accessed_at: '2026-11-03T05:15:01.515968Z'
  support: supports
  summary: GENE_OR_PROTEIN explicitly includes complexes; BAM/Lpt complex node types
    are allowed, and representative UniProt links are not full inventories.
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: septin-s2351-original-native-checks
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2351/adversary-septin/original-checks.json
  locator: Four native validate invocations, four render --content invocations and
    byte/hash comparisons, actual start/end timestamps.
  accessed_at: '2026-11-03T05:15:01.515968Z'
  support: supports
  summary: All four validate/render exits0; render bytes equal committed original
    Markdown and target SHA equals historical frozen SHA. Deprecation warning only.
    No full QC or CI executed by this subreview.
  snapshot_sha256: a6ff010c1941623c23f080c884917c3402091935e1b59e308fb8115c406e0999
- evidence_id: septin-s2351-outer-native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2351/outer-membrane-uniprot-verify-receipt.json
  locator: Root-run native command ['.venv/bin/python', 'scripts/uniprot_genes.py',
    '--record', 'data/structures/envelope/cell_outer_membrane.yaml', '--verify'];
    independently read exact receipt and log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2351/outer-membrane-uniprot-verify.log;
    head 3266d0f7239a80f17d74bb0d6e2b3e260000b8dc.
  accessed_at: '2026-11-03T05:13:18.667297Z'
  support: supports
  summary: 'Exit0: all protein_examples and causal graph UniProt xrefs verify.'
  snapshot_sha256: a28922ed157aa5ddeca4b9287ccf6979406a54694b04126f1a22523415dc9c12
- evidence_id: septin-s2351-outer-native-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2351/outer-membrane-uniprot-causal-receipt.json
  locator: Root-run native command ['.venv/bin/python', 'scripts/uniprot_genes.py',
    '--record', 'data/structures/envelope/cell_outer_membrane.yaml', '--causal-graphs'];
    independently read exact receipt and log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2351/outer-membrane-uniprot-causal.log;
    head 3266d0f7239a80f17d74bb0d6e2b3e260000b8dc.
  accessed_at: '2026-11-03T05:13:27.295388Z'
  support: supports
  summary: 'Exit0: two COVERED and two UNANCHORED_WITH_UNIPROT nodes; latter are Lpt/BAM
    representative links. No dangling reference. This classification is not a demand
    to invent a full complex inventory.'
  snapshot_sha256: 98c2345768bdf4c00faca93cce58049a7860bb3e8ac0870528ff6bba90f7a0a8
- evidence_id: check-qc
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2351/qc.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T05:12:32.766390Z'
  support: supports
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  snapshot_sha256: ffa0ff86bb91adfa1df641ab8ee76cc7ac8d720987648ddbc6b2b365f6458437
- evidence_id: check-labels
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2351/labels.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T05:07:22.796312Z'
  support: supports
  summary: 4232 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  snapshot_sha256: d8200b370ec584f49336f01ed9035fbe21f0aa191ad0257a9a421938e9f17ecb
- evidence_id: check-trait-links
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2351/trait-links.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T05:06:59.320551Z'
  support: supports
  summary: Native TraitMech link check passed.
  snapshot_sha256: 8b336cdefbbd3daf6da8787990efdbe346c95e2c8361d50b7eb68a18f2d5a44a
- evidence_id: check-vendored
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2351/vendored.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T05:06:55.772991Z'
  support: supports
  summary: Pinned governed files match; native vendored check passed.
  snapshot_sha256: b1f169d103aaefa930745468bcca171e5867b9cc49e4e74311e458097e3252a6
- evidence_id: check-curies
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2351/curies.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T05:07:24.177273Z'
  support: supports
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  snapshot_sha256: fb3be251020aac118f6df680372ae7aaa32c2a1dd3366648cde95494f19d9dd2
- evidence_id: focused
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2351/focused-results.json
  locator: All twenty actual target schema/strict command outputs
  accessed_at: '2026-11-03T05:18:03Z'
  support: supports
  summary: Ten schema and ten strict commands returned exit zero.
  snapshot_sha256: 74e15633e1177297fee37a575381747695df9065f9cbdc1224d15fa1e008e76b
- evidence_id: supplemental-pmid
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2351/pmid-chunks-receipt.json
  locator: Complete native-report PMID set checked with unchanged resolver in batches
    of at most fifty
  accessed_at: '2026-11-03T05:09:07.000589Z'
  support: supports
  summary: 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers
    remain unverified.
  snapshot_sha256: d8c88d680a3b297dcb570d6b4b046890e957d8b25e3d54a28dc4af5ef9500f62
- evidence_id: historical-adapter-runner-availability
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical runner invocation receipt, cross-checked against exact stdout/stderr
    hashes; reread during PR2351 synthesis
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  summary: Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS
    PermissionError reading the configured runner pyvenv.cfg. This is a retained historical
    availability observation, not a fresh attempt or a scientific validation failure.
    Native policy permits inspected source-catalogue fallback.
assessments:
- assessment_id: plaque-mcr-current
  area: identity
  topic: Hexamer identity and source-scoped reaction
  outcome: supported
  summary: GO0044674, native 1MRO assembly and primary transcription support the hexameric
    MCR target. Exact M.marburgensis mcrA/B/G examples and three InterPro families
    match the components and reaction context. Wrede2013 supports source-scoped localization
    of assembled MCR antigen, not universal membrane exclusion or isolated-subunit
    localization.
  target_ids:
  - GO:0044674
  evidence_ids:
  - plaque-current-0
  - plaque-mcr-primary-browser
  - plaque-mcr-agent-wrede2013-jats
  - plaque-mcr-agent-go
  - plaque-mcr-agent-IPR016212
  - plaque-mcr-agent-IPR003179
  - plaque-mcr-agent-pdb-1mro
  - plaque-mcr-agent-pdb-1mro-assembly1
  - plaque-mcr-agent-pdb-1mro-entity1
  - plaque-mcr-agent-pdb-1mro-entity2
  - plaque-mcr-agent-pdb-1mro-entity3
  - plaque-mcr-agent-P11558
  - plaque-mcr-agent-P11560
  - plaque-mcr-agent-P11562
  - plaque-mcr-agent-IPR003178-retry
- assessment_id: plaque-mcr-grounding-refresh
  area: graph
  topic: Current graph propagation and historical F2 disposition
  outcome: supported
  summary: 'All three added graph grounding values now match their referenced components:
    alpha IPR016212, beta IPR003179 and gamma IPR003178. This substantively refreshes
    the stale review and resolves the exact category-review F2 observation. The repair
    pre-existed PR2351; the successor records the inspected disposition and preserves
    stable issue lineage.'
  target_ids:
  - GO:0044674
  evidence_ids:
  - plaque-current-0
  - plaque-original-0
  - plaque-mcr-category-prior
  - plaque-mcr-agent-IPR016212
  - plaque-mcr-agent-IPR003179
  - plaque-mcr-agent-IPR003178-retry
- assessment_id: plaque-complex-i-current
  area: identity
  topic: Whole complex and conserved-arm architecture
  outcome: supported
  summary: GO0045271 fits the L-shaped respiratory complex. Primary Results/Methods
    and supplemental Tables3-4 support the two maintained arm components; 14 named
    reviewed HB8 examples are verified. The source preparation additionally has Nqo15/Nqo16;
    the record does not claim only14 total chains in 4HEA. All16 deposited entity
    mappings were checked. Proposed coupling pathways remain qualified.
  target_ids:
  - GO:0045271
  evidence_ids:
  - plaque-current-1
  - plaque-complex-i-agent-baradaran2013-jats
  - plaque-complex-i-agent-baradaran2013-supplement-epmc
  - plaque-complex-i-agent-go
  - plaque-complex-i-agent-go-arm-candidates
  - plaque-complex-i-agent-go-peripheral-search
  - plaque-complex-i-agent-go-membrane-arm-search
  - plaque-complex-i-agent-assembly-4HEA
  - plaque-complex-i-agent-4HEA-entity-1
  - plaque-complex-i-agent-4HEA-entity-2
  - plaque-complex-i-agent-4HEA-entity-3
  - plaque-complex-i-agent-4HEA-entity-4
  - plaque-complex-i-agent-4HEA-entity-5
  - plaque-complex-i-agent-4HEA-entity-6
  - plaque-complex-i-agent-4HEA-entity-7
  - plaque-complex-i-agent-4HEA-entity-8
  - plaque-complex-i-agent-4HEA-entity-9
  - plaque-complex-i-agent-4HEA-entity-10
  - plaque-complex-i-agent-4HEA-entity-11
  - plaque-complex-i-agent-4HEA-entity-12
  - plaque-complex-i-agent-4HEA-entity-13
  - plaque-complex-i-agent-4HEA-entity-14
  - plaque-complex-i-agent-4HEA-entity-15
  - plaque-complex-i-agent-4HEA-entity-16
  - plaque-complex-i-agent-Q56222
  - plaque-complex-i-agent-Q56221
  - plaque-complex-i-agent-Q56223
  - plaque-complex-i-agent-Q56220
  - plaque-complex-i-agent-Q56219
  - plaque-complex-i-agent-Q56218
  - plaque-complex-i-agent-Q56224
  - plaque-complex-i-agent-Q56217
  - plaque-complex-i-agent-Q56225
  - plaque-complex-i-agent-Q56226
  - plaque-complex-i-agent-Q56227
  - plaque-complex-i-agent-Q56228
  - plaque-complex-i-agent-Q56229
  - plaque-complex-i-agent-Q60019
- assessment_id: plaque-complex-i-graph-refresh
  area: graph
  topic: Peripheral-arm contribution edge refresh
  outcome: supported
  summary: The added peripheral_arm→nadh_ubiquinone_activity contribution edge is
    supported by the source FMN/FeS electron-transfer architecture. A whole-complex
    GO activity name does not assert exclusive native ubiquinone usage in Thermus,
    where the paper identifies menaquinone8 and uses a decyl-ubiquinone analogue.
    The edge remains a coarse functional contribution, not a demonstrated kinetic
    coupling sequence.
  target_ids:
  - GO:0045271
  evidence_ids:
  - plaque-current-1
  - plaque-original-1
  - plaque-complex-i-agent-baradaran2013-jats
  - plaque-complex-i-agent-go
- assessment_id: plaque-complex-i-family
  area: evidence
  topic: Whole-arm grounding specificity
  outcome: supported
  summary: IPR001750 and IPR006137 are domains, not exact whole-arm identities. GO0042652/GO0042653
    are obsolete. Bounded first-page GO searches and named candidate inspection support
    retaining reviewed label-only arms; they do not establish exhaustive absence of
    a future exact ontology term. The named core subunits are represented within the
    arm components, not omitted pending family identification.
  target_ids:
  - GO:0045271
  evidence_ids:
  - plaque-complex-i-agent-go-arm-candidates
  - plaque-complex-i-agent-go-peripheral-search
  - plaque-complex-i-agent-go-membrane-arm-search
  - plaque-complex-i-agent-ipr-001750
  - plaque-complex-i-agent-ipr-006137
- assessment_id: plaque-sdh-current
  area: identity
  topic: Four-chain complex and current graph refresh
  outcome: supported
  summary: GO0045273, primary abstract, deposited1NEK structure and reviewed SdhA-D
    entries support the maintained four-chain complex with catalytic SdhA, electron-transfer
    SdhB and SdhCD anchor module. Added contribution edges correctly identify SdhA
    flavin, the three SdhB FeS cluster classes and heme-bearing membrane module. These
    are whole-complex contributions; no isolated SdhCD activity or proton-pumping
    mechanism is asserted.
  target_ids:
  - GO:0045273
  evidence_ids:
  - plaque-current-2
  - plaque-original-2
  - plaque-sdh-agent-pmid-12560550
  - plaque-sdh-agent-go
  - plaque-sdh-agent-P0AC41
  - plaque-sdh-agent-P07014
  - plaque-sdh-agent-P69054
  - plaque-sdh-agent-P0AC44
  - plaque-sdh-agent-pdb-1NEK
  - plaque-sdh-agent-assembly-1NEK
  - plaque-sdh-agent-1NEK-entity-1
  - plaque-sdh-agent-1NEK-entity-2
  - plaque-sdh-agent-1NEK-entity-3
  - plaque-sdh-agent-1NEK-entity-4
- assessment_id: plaque-sdh-family
  area: evidence
  topic: Bounded family scope and localization provenance
  outcome: supported
  summary: 'Integrated matches and named candidate definitions do not supply exact
    broad SdhA/SdhB/whole-SdhCD identities: several span fumarate reductases, are
    narrower clades, or denote only one anchor subunit. Additional current SdhB matchIPR050573
    explicitly spans SDH/FRD by integrated family name; its unchecked LLM prose is
    excluded. UniProt attributes SdhA/B membrane localization to Stenberg2005 and
    SdhD to Daley2005; this verifies attribution without claiming a renewed full-body
    audit of those studies.'
  target_ids:
  - GO:0045273
  evidence_ids:
  - plaque-sdh-stenberg-browser
  - plaque-sdh-agent-pmid-15919996
  - plaque-sdh-agent-pmid-16079137
  - plaque-sdh-agent-P0AC41
  - plaque-sdh-agent-P07014
  - plaque-sdh-agent-P69054
  - plaque-sdh-agent-P0AC44
  - plaque-sdh-agent-matches-P0AC41
  - plaque-sdh-agent-matches-P07014
  - plaque-sdh-agent-matches-P69054
  - plaque-sdh-agent-matches-P0AC44
  - plaque-sdh-agent-IPR011281
  - plaque-sdh-agent-IPR014006
  - plaque-sdh-agent-IPR030664
  - plaque-sdh-agent-IPR065464
  - plaque-sdh-agent-IPR004489-retry
  - plaque-sdh-agent-IPR014314-retry
  - plaque-sdh-agent-IPR014312-retry
  - plaque-sdh-agent-IPR050573
- assessment_id: plaque-adapter-0
  area: evidence
  topic: Fresh catalogue-based source adapter applicability
  outcome: supported
  summary: Fresh complete public catalogue has no matching Methanothermobacter marburgensis
    dataset. Not-applicable downstream module checks follow this actual organism-coverage
    result, not the absence of an expression claim. No close-relative dataset is silently
    substituted.
  target_ids:
  - GO:0044674
  evidence_ids:
  - plaque-adapter-datasets
  - plaque-current-0
- assessment_id: plaque-adapter-1
  area: evidence
  topic: Fresh catalogue-based source adapter applicability
  outcome: supported
  summary: Fresh complete public catalogue has no matching Thermus thermophilus dataset.
    Not-applicable downstream module checks follow this actual organism-coverage result,
    not the absence of an expression claim. No close-relative dataset is silently
    substituted.
  target_ids:
  - GO:0045271
  evidence_ids:
  - plaque-adapter-datasets
  - plaque-current-1
- assessment_id: plaque-adapter-2
  area: evidence
  topic: Matched MG1655 gene and module context
  outcome: supported
  summary: Fresh source fallback resolves sdhA/b0723,sdhB/b0724,sdhC/b0721,sdhD/b0722
    in precise_mg1655. All four are thresholded members of Crp(k1) and ArcA-2(k10);
    sdhA/C/D also belong to ArcA-1(k14), while sdhB is below that threshold. Module
    annotations and all returned member identifier/weight rows were read. These bounded
    expression observations do not prove assembly, stoichiometry, essentiality or
    direct regulation; AI module prose and activity matrices are excluded.
  target_ids:
  - GO:0045273
  evidence_ids:
  - plaque-adapter-datasets
  - plaque-adapter-frontend
  - plaque-adapter-meta
  - plaque-adapter-search-sdhA
  - plaque-adapter-search-sdhB
  - plaque-adapter-search-sdhC
  - plaque-adapter-search-sdhD
  - plaque-adapter-gene-modules-sdhC
  - plaque-adapter-gene-modules-sdhA
  - plaque-adapter-gene-modules-sdhB
  - plaque-adapter-gene-modules-sdhD
  - plaque-adapter-summary-1
  - plaque-adapter-members-1
  - plaque-adapter-summary-10
  - plaque-adapter-members-10
  - plaque-adapter-summary-14
  - plaque-adapter-members-14
- assessment_id: plaque-assembly-necessity-0
  area: evidence
  topic: Assembly necessity remains unknown
  outcome: unknown
  summary: 'Retain the original explicit uncertainty: structural membership and catalytic
    role alone do not establish whether the complete structure forms after deletion
    of a component. No target-specific deletion/assembly experiment was independently
    checked, and no new contrary result is confirmed in the inspected source scope.'
  target_ids:
  - GO:0044674
  evidence_ids:
  - plaque-current-0
  - plaque-original-0
- assessment_id: plaque-assembly-necessity-1
  area: evidence
  topic: Assembly necessity remains unknown
  outcome: unknown
  summary: 'Retain the original explicit uncertainty: structural membership and catalytic
    role alone do not establish whether the complete structure forms after deletion
    of a component. No target-specific deletion/assembly experiment was independently
    checked, and no new contrary result is confirmed in the inspected source scope.'
  target_ids:
  - GO:0045271
  evidence_ids:
  - plaque-current-1
  - plaque-original-1
- assessment_id: plaque-assembly-necessity-2
  area: evidence
  topic: Assembly necessity remains unknown
  outcome: unknown
  summary: 'Retain the original explicit uncertainty: structural membership and catalytic
    role alone do not establish whether the complete structure forms after deletion
    of a component. No target-specific deletion/assembly experiment was independently
    checked, and no new contrary result is confirmed in the inspected source scope.'
  target_ids:
  - GO:0045273
  evidence_ids:
  - plaque-current-2
  - plaque-original-2
- assessment_id: plaque-mcr-native-protein-gates
  area: evidence
  topic: Current native protein and causal-node coverage checks
  outcome: supported
  summary: Both root-executed native read-only commands exited0 at the reviewed source
    head; this independent reviewer read their logs and verified the bound stdout
    hashes. All declared gene symbols have matching examples. These checks supplement
    the source-level identity assessment and do not establish biochemical causality
    or essentiality.
  target_ids:
  - GO:0044674
  evidence_ids:
  - plaque-mcr-native-uniprot-verify
  - plaque-mcr-native-uniprot-causal
- assessment_id: plaque-complex-i-native-protein-gates
  area: evidence
  topic: Current native protein and causal-node coverage checks
  outcome: supported
  summary: Both root-executed native read-only commands exited0 at the reviewed source
    head; this independent reviewer read their logs and verified the bound stdout
    hashes. All declared gene symbols have matching examples. These checks supplement
    the source-level identity assessment and do not establish biochemical causality
    or essentiality.
  target_ids:
  - GO:0045271
  evidence_ids:
  - plaque-complex-i-native-uniprot-verify
  - plaque-complex-i-native-uniprot-causal
- assessment_id: plaque-complex-ii-native-protein-gates
  area: evidence
  topic: Current native protein and causal-node coverage checks
  outcome: supported
  summary: Both root-executed native read-only commands exited0 at the reviewed source
    head; this independent reviewer read their logs and verified the bound stdout
    hashes. All declared gene symbols have matching examples. These checks supplement
    the source-level identity assessment and do not establish biochemical causality
    or essentiality.
  target_ids:
  - GO:0045273
  evidence_ids:
  - plaque-complex-ii-native-uniprot-verify
  - plaque-complex-ii-native-uniprot-causal
- assessment_id: micro-psii-identity
  area: identity
  topic: Exact PSII structure and named taxa
  outcome: supported
  target_ids:
  - GO:0009523
  summary: The generic photosystem parent, exact GO identity, grouped core and oxygenic
    canonical example remain coherent. Broader anoxygenic comparison is inherited
    GO definition text, not a new cyanobacterial species claim. No protein/phenotype
    identity collapse.
  evidence_ids:
  - micro-record-psii
  - micro-psii-agent-go
  - micro-psii-agent-tax-1117
  - micro-psii-agent-tax-32053
  - micro-psii-agent-umena2011-pdf
- assessment_id: micro-psii-composition
  area: grounding
  topic: Mixed core, metal cluster and pigments
  outcome: supported
  target_ids:
  - GO:0009523
  summary: Umena supports represented core/cofactor classes. Exact D1 or D2 families
    and broad L/M cannot individually ground the complete mixed reaction-center core;
    no exhaustive family absence claim. Known central membership is represented rather
    than postponed wholesale.
  evidence_ids:
  - micro-record-psii
  - micro-psii-agent-umena2011-pdf
  - micro-psii-agent-IPR005867
  - micro-psii-agent-IPR005868
  - micro-psii-agent-IPR000484
  - micro-policy
- assessment_id: micro-psii-essentiality
  area: scope
  topic: Assembly necessity remains an explicit limitation
  outcome: unknown
  target_ids:
  - GO:0009523
  summary: Canonical presence/catalytic importance is supported; the inspected structures
    and halide activity experiment do not independently establish assembly loss on
    removal of each grouped metal/pigment class. ESSENTIAL is not upgraded to a demonstrated
    knockout, universal member requirement or organism-viability result. No contradictory
    assembly experiment was established in this bounded review.
  evidence_ids:
  - micro-psii-agent-umena2011-pdf
  - micro-psii-kawakami2009-html
  - micro-policy
- assessment_id: micro-psii-proteins
  area: evidence
  topic: Exact D1/D2 examples and expanded primary access
  outcome: supported
  target_ids:
  - GO:0009523
  summary: Reviewed P51765 psbA and D0VWR8 psbD match native taxon, status and location-annotation
    citations; two-result query supports uniqueness per symbol in scope. Current Kamiya2003
    and Kawakami2009 body access succeeds and supersedes the old access limitation
    only for this observation. Kamiya model-sequence borrowing is disclosed; annotation
    does not by itself prove all assembly details.
  evidence_ids:
  - micro-psii-agent-P51765
  - micro-psii-agent-D0VWR8
  - micro-psii-agent-uniprot-unique
  - micro-psii-agent-epmc
  - micro-psii-kamiya2003-html
  - micro-psii-kawakami2009-html
  - micro-psii-agent-umena2011-pdf
  - micro-native-photosystem-ii-verify
- assessment_id: micro-psii-graph
  area: graph
  topic: Five broad functional edges
  outcome: supported
  target_ids:
  - GO:0009523
  summary: The NONMECHANISTIC graph preserves light excitation, water-derived electron
    supply, quinone reduction and initiation of the photosynthetic chain. It does
    not assert atomistic S-state routes, ATP production by PSII or exact universal
    subunit stoichiometry. Native graph audit1/1COVERED.
  evidence_ids:
  - micro-record-psii
  - micro-psii-agent-go
  - micro-psii-agent-umena2011-pdf
  - micro-native-photosystem-ii-causal
- assessment_id: micro-rod-staleness
  area: provenance
  topic: Substantive refresh of added CpcD example
  outcome: supported
  target_ids:
  - cellstructuremech:phycobilisome_rod
  summary: Current record differs from frozen input by the added A0ABT0CFU3/JX360_17400
    example and associated curation event. Fresh UniProt and source GenPept explicitly
    annotate a predicted CpcD linker in Rupite, supporting this identity-only example.
    It is not a unique paralog claim, experimental localization or a resolution of
    the independent cpcC issue. Current graph audit is2/2COVERED, superseding the
    historical optional cpcD gap.
  evidence_ids:
  - micro-record-rod
  - micro-prior-rod
  - micro-rod-new-A0ABT0CFU3
  - micro-rod-new-genpept
  - micro-rod-new-IPR008213
  - micro-rod-agent-rupite-linkers
  - micro-native-phycobilisome-rod-verify
  - micro-native-phycobilisome-rod-causal
- assessment_id: micro-rod-identity
  area: identity
  topic: Peripheral rod versus core and entire antenna
  outcome: supported
  target_ids:
  - cellstructuremech:phycobilisome_rod
  summary: The local rod is a source-supported peripheral subassembly; GO0030076 is
    the broader parent and whole-PBS GO0030089 is parthood. The local allophycocyanin-core
    graph reference resolves to a distinct central structure. No intact atomic whole-PBS
    claim is made.
  evidence_ids:
  - micro-record-rod
  - micro-rod-agent-go
  - micro-rod-agent-kawakami2022-jats
  - micro-local-core
- assessment_id: micro-rod-composition
  area: grounding
  topic: Mixed rod constituents and family scope
  outcome: supported
  target_ids:
  - cellstructuremech:phycobilisome_rod
  summary: CpcA/B-rich phycobiliproteins, mixed rod/rod-terminal/rod-core linkers
    and covalent bilins match the primary preparation. Broad phycobiliprotein family
    includes core members; linker domains span multiple classes, so they are not exact
    whole-cohort replacements. CpcG2 assignment is tentative in the paper’s heterogeneous
    rods.
  evidence_ids:
  - micro-rod-agent-kawakami2022-jats
  - micro-rod-agent-IPR012128
  - micro-rod-agent-IPR001297
  - micro-rod-agent-IPR038255
  - micro-rod-agent-IPR016470
  - micro-rod-new-IPR008213
- assessment_id: micro-rod-proteins
  area: provenance
  topic: cpcC finding persists despite native checks
  outcome: concern
  target_ids:
  - cellstructuremech:phycobilisome_rod
  summary: The valid A0ABT0C7D6 accession/ORF/taxon passes native verification, but
    JX360_02095 is only a generic predicted rod-core linker in UniProt and GenPept.
    NIES-2134 primary text and BP-1 model-sequence context do not establish the exact
    Rupite cpcC mapping. Freshly reassessed original F1 remains open; no replacement
    accession is inferred from domain or length comparisons.
  evidence_ids:
  - micro-rod-agent-A0ABT0C7D6
  - micro-rod-agent-MCJ2541704.1-genpept
  - micro-rod-agent-kawakami2022-jats
  - micro-rod-agent-P50034
  - micro-rod-agent-pdb-7veb-entity4
  - micro-rod-agent-A0ABT0C9G9
  - micro-rod-agent-rupite-linkers
  - micro-protein-policy
  - micro-native-phycobilisome-rod-verify
- assessment_id: micro-rod-taxa
  area: scope
  topic: Primary strain and comparative taxa
  outcome: supported
  target_ids:
  - cellstructuremech:phycobilisome_rod
  summary: Direct cryo-EM experiment is NIES-2134 T. vulcanus; Rupite examples are
    predicted identity annotations. Red-algal architecture is comparative context
    in the primary Introduction. Native taxon labels are valid; no cross-strain localization,
    abundance measurement or universal stoichiometry is inferred.
  evidence_ids:
  - micro-rod-agent-kawakami2022-jats
  - micro-psii-agent-tax-1117
  - micro-psii-agent-tax-32053
  - micro-rod-agent-tax-2813851
  - micro-rod-agent-tax-2763
  - micro-rod-agent-A0ABT0C7V5
  - micro-rod-agent-A0ABT0C7V6
  - micro-rod-agent-A0ABT0C7V3
- assessment_id: micro-rod-function
  area: graph
  topic: Five bounded assembly/light-harvesting edges
  outcome: supported
  target_ids:
  - cellstructuremech:phycobilisome_rod
  summary: Disk assembly, linker organization, covalent pigments and inward excitation
    transfer are supported at the stated broad NONMECHANISTIC tier. Detailed energy-level
    tuning/pathways in the paper remain structural interpretations with prior spectroscopy,
    not measured time-resolved transfer by that experiment. No new required optional
    class or exhaustive family mapping is invented.
  evidence_ids:
  - micro-record-rod
  - micro-rod-agent-kawakami2022-jats
  - micro-rod-agent-go
  - micro-native-phycobilisome-rod-causal
- assessment_id: micro-bacterial-psii-identity
  area: identity
  topic: Exact bacterial-thylakoid subtype and partonomy
  outcome: supported
  target_ids:
  - GO:0030096
  summary: GO0030096 exactly identifies the membrane-derived bacterial-thylakoid PSII
    subtype with generic PSII parent and thylakoid-membrane parthood. Its scoped synonym
    and structure category avoid collapsing whole PBS, protein or generic PSII identity.
    Ontology terminology does not establish a new direct membrane-biogenesis experiment.
  evidence_ids:
  - micro-record-bacterial-psii
  - micro-psii-prep-go
  - micro-psii-prep-chang2015-pmc-html
- assessment_id: micro-bacterial-psii-association
  area: evidence
  topic: Canonical prepared-particle association
  outcome: supported
  target_ids:
  - GO:0030096
  summary: Chang2015 supports some Nostoc/Anabaena PCC7120 PBS particles associated
    with PSII, using low-resolution density, D1/D2 immunoblot and D1 immunogold. It
    does not show all PBS particles bind PSII, a live-cell atomic interface or a catalytically
    intact oxygen-evolving preparation.21Å PBS-only and34ÅPBS–PSII maps remain distinct.
  evidence_ids:
  - micro-psii-prep-chang2015-pmc-html
  - micro-psii-prep-tax-103690
  - micro-record-bacterial-psii
- assessment_id: micro-bacterial-psii-composition
  area: completeness
  topic: Known D1/D2 membership is postponed unnecessarily
  outcome: concern
  target_ids:
  - GO:0030096
  summary: Current record still has no components and explicitly defers all subunit
    rows until exact source-neutral families are resolved. The cited Results/Fig1G
    directly identify D1/D2 reaction-center subunits; known membership can be recorded
    with unresolved family groundings. Original F1 remains open. This does not demand
    every optional accessory subunit or interpret PsbO nondetection as universal absence.
  evidence_ids:
  - micro-record-bacterial-psii
  - micro-prior-bacterial-psii
  - micro-psii-prep-chang2015-pmc-html
  - micro-policy
- assessment_id: micro-bacterial-psii-function
  area: graph
  topic: Four broad graph edges and access tiers
  outcome: supported
  target_ids:
  - GO:0030096
  summary: 'Exact GO supplies water-to-plastoquinone physiology and membrane identity;
    primary Chang supplies limited PBS association. This observation independently
    supports the broad graph with those sources. Perez2024 is secondary context: its
    fresh abstract/metadata were readable, but native403 and browser fulltext failure
    prevent claiming a newly inspected body. The old body-excerpt provenance is left
    historical.'
  evidence_ids:
  - micro-record-bacterial-psii
  - micro-psii-prep-go
  - micro-psii-prep-chang2015-pmc-html
  - micro-psii-prep-perez2024-meta
  - micro-publisher
  - micro-perez-publisher-browser
  - micro-perez-body-browser-unavailable
- assessment_id: micro-bacterial-psii-taxa
  area: scope
  topic: Named strain and qualitative cyanobacterial distribution
  outcome: supported
  target_ids:
  - GO:0030096
  summary: Native nomenclature agrees with Anabaena/NostocPCC7120 equivalence. COMMON
    is qualitative within cyanobacteria having internal thylakoids, not prevalence
    data or an assertion of identical architecture in all cyanobacteria. No new strain-specific
    accession inventory, images or measured properties are asserted.
  evidence_ids:
  - micro-record-bacterial-psii
  - micro-psii-prep-tax-103690
  - micro-psii-agent-tax-1117
  - micro-psii-prep-go
  - micro-psii-prep-chang2015-pmc-html
- assessment_id: micro-psii-adapter
  area: evidence
  topic: Covered cyanobacterial expression context with strict limits
  outcome: supported
  target_ids:
  - GO:0009523
  summary: All3 original bundles omit the structured-source applicability step despite
    named genes/proteins or photosynthetic pathways. Current catalogue and s_elongatus/elprecise300
    PCC7942 metadata establish bounded cyanobacterial coverage; exact psbA/D and cpcA/B/C/D/G
    table matches, all57module memberships for13loci, and selected modules1/6/38 were
    inspected. Photosystems38 and RpaB6 include different subsets; PSII1 excludes
    the selected psbA/D loci despite its name. Regulator fields are null. This computational
    expression context neither changes the scientific verdict nor establishes canonical-strain
    orthology, physical localization or direct regulation. Native runner availability
    is to be disclosed from the root’s actual retained receipt; this reviewer used
    inspected official API fallback, not a new runner execution.
  evidence_ids:
  - micro-adapter-policy
  - micro-adapter-catalogue
  - micro-meta
  - micro-genes
  - micro-imodulons
  - micro-module-1
  - micro-module-1-genes
  - micro-module-6
  - micro-module-6-genes
  - micro-module-38
  - micro-module-38-genes
  - micro-adapter-publication
- assessment_id: micro-psii-native
  area: schema
  topic: Frozen inputs and historical native review pair
  outcome: supported
  target_ids:
  - GO:0009523
  summary: Historical source bytes match the original frozen input; native validation
    and rendered Markdown pass. Current target bytes remain identical to the original
    input. Current broad QC/labels/history/strict receipts are owned by the root synthesis,
    not claimed executed by this reviewer.
  evidence_ids:
  - micro-original-checks
  - micro-prior-psii
  - micro-record-psii
- assessment_id: micro-rod-adapter
  area: evidence
  topic: Covered cyanobacterial expression context with strict limits
  outcome: supported
  target_ids:
  - cellstructuremech:phycobilisome_rod
  summary: All3 original bundles omit the structured-source applicability step despite
    named genes/proteins or photosynthetic pathways. Current catalogue and s_elongatus/elprecise300
    PCC7942 metadata establish bounded cyanobacterial coverage; exact psbA/D and cpcA/B/C/D/G
    table matches, all57module memberships for13loci, and selected modules1/6/38 were
    inspected. Photosystems38 and RpaB6 include different subsets; PSII1 excludes
    the selected psbA/D loci despite its name. Regulator fields are null. This computational
    expression context neither changes the scientific verdict nor establishes canonical-strain
    orthology, physical localization or direct regulation. Native runner availability
    is to be disclosed from the root’s actual retained receipt; this reviewer used
    inspected official API fallback, not a new runner execution.
  evidence_ids:
  - micro-adapter-policy
  - micro-adapter-catalogue
  - micro-meta
  - micro-genes
  - micro-imodulons
  - micro-module-1
  - micro-module-1-genes
  - micro-module-6
  - micro-module-6-genes
  - micro-module-38
  - micro-module-38-genes
  - micro-adapter-publication
- assessment_id: micro-rod-native
  area: schema
  topic: Frozen inputs and historical native review pair
  outcome: supported
  target_ids:
  - cellstructuremech:phycobilisome_rod
  summary: Historical source bytes match the original frozen input; native validation
    and rendered Markdown pass. Current input is substantively refreshed above, without
    altering old bundle bytes. Current broad QC/labels/history/strict receipts are
    owned by the root synthesis, not claimed executed by this reviewer.
  evidence_ids:
  - micro-original-checks
  - micro-prior-rod
  - micro-record-rod
- assessment_id: micro-bacterial-psii-adapter
  area: evidence
  topic: Covered cyanobacterial expression context with strict limits
  outcome: supported
  target_ids:
  - GO:0030096
  summary: All3 original bundles omit the structured-source applicability step despite
    named genes/proteins or photosynthetic pathways. Current catalogue and s_elongatus/elprecise300
    PCC7942 metadata establish bounded cyanobacterial coverage; exact psbA/D and cpcA/B/C/D/G
    table matches, all57module memberships for13loci, and selected modules1/6/38 were
    inspected. Photosystems38 and RpaB6 include different subsets; PSII1 excludes
    the selected psbA/D loci despite its name. Regulator fields are null. This computational
    expression context neither changes the scientific verdict nor establishes canonical-strain
    orthology, physical localization or direct regulation. Native runner availability
    is to be disclosed from the root’s actual retained receipt; this reviewer used
    inspected official API fallback, not a new runner execution.
  evidence_ids:
  - micro-adapter-policy
  - micro-adapter-catalogue
  - micro-meta
  - micro-genes
  - micro-imodulons
  - micro-module-1
  - micro-module-1-genes
  - micro-module-6
  - micro-module-6-genes
  - micro-module-38
  - micro-module-38-genes
  - micro-adapter-publication
- assessment_id: micro-bacterial-psii-native
  area: schema
  topic: Frozen inputs and historical native review pair
  outcome: supported
  target_ids:
  - GO:0030096
  summary: Historical source bytes match the original frozen input; native validation
    and rendered Markdown pass. Current target bytes remain identical to the original
    input. Current broad QC/labels/history/strict receipts are owned by the root synthesis,
    not claimed executed by this reviewer.
  evidence_ids:
  - micro-original-checks
  - micro-prior-bacterial-psii
  - micro-record-bacterial-psii
- assessment_id: septin-S2351-A1
  area: identity
  topic: RC-LH1-PufX identity, topology and neighbor
  outcome: supported
  summary: Local complex identity is narrower than its chromatophore membrane context
    GO0042717. Tax1063 is current Cereibacter sphaeroides with Rhodobacter synonym.
    Frozen LH2 record resolves the distinct external antenna link, and GO0009767 is
    the photosynthetic electron-transport process, not structure identity.
  target_ids:
  - cellstructuremech:rc_lh1_pufx_core_complex
  evidence_ids:
  - septin-s2351-record-rc_lh1_pufx_core_complex
  - septin-s2351-rc-prep-go
  - septin-s2351-rc-prep-tax-1063
  - septin-s2351-lh2-context
- assessment_id: septin-S2351-A2
  area: evidence
  topic: RC architecture and bounded functional links
  outcome: supported
  summary: Bahatyrova AFM supports native membrane-patch core/LH2 organization; Comayras
    optical assays support isolated-core/chromatophore excitation and quinone context.
    The four NON_MECHANISTIC edges stay at membrane placement, LH2 energy input, quinone
    reduction and contribution to the photosynthetic chain. They do not assert a detailed
    cofactor path, PufX-specific kinetics or universal interdimer transfer.
  target_ids:
  - cellstructuremech:rc_lh1_pufx_core_complex
  evidence_ids:
  - septin-s2351-rc-prep-bahatyrova2004-whiterose-pdf
  - septin-s2351-comayras-indexed-body
  - septin-s2351-rc-prep-comayras2005-meta
  - septin-s2351-bounded-publication-search
- assessment_id: septin-S2351-A3
  area: grounding
  topic: RC known core remains unnecessarily deferred
  outcome: concern
  summary: 'Original F1 remains confirmed: no component rows are present, while the
    TODO makes exact family mapping a prerequisite. Source-bounded RC L/M/H, LH1 alpha/beta
    and PufX-containing-complex membership can be recorded without guessed CURIEs;
    the AFM paper explicitly did not resolve PufX itself.'
  target_ids:
  - cellstructuremech:rc_lh1_pufx_core_complex
  evidence_ids:
  - septin-s2351-record-rc_lh1_pufx_core_complex
  - septin-s2351-rc-prep-bahatyrova2004-whiterose-pdf
  - septin-s2351-comayras-indexed-body
  - septin-s2351-policy
- assessment_id: septin-S2351-A4
  area: scope
  topic: RC structured-source applicability
  outcome: supported
  summary: Named PufX/photosynthetic pathway requires applicability assessment. The
    fresh official catalogue contains no Cereibacter/Rhodobacter match, so matched
    downstream queries are not applicable for this exact strain context. This is not
    absence of a gene, and unrelated phototrophic organisms were not substituted.
  target_ids:
  - cellstructuremech:rc_lh1_pufx_core_complex
  evidence_ids:
  - septin-s2351-current-adapter-catalogue
  - septin-s2351-record-rc_lh1_pufx_core_complex
  - septin-s2351-policy
- assessment_id: septin-S2351-A5
  area: identity
  topic: V0 identity and intact-enzyme scope
  outcome: supported
  summary: The specific vacuolar sector is correctly distinguished from its broader
    sector parent and complete GO0016471 V-ATPase. Yeast4932 is a bounded example.
    V0 membrane transport is expressly inside the intact enzyme, not a freely leaking
    detached pore.
  target_ids:
  - GO:0000220
  evidence_ids:
  - septin-s2351-record-vacuolar_proton_transporting_v_type_atpase_v0_domain
  - septin-s2351-v0-agent-go
  - septin-s2351-v0-agent-tax-4932
  - septin-s2351-v0-agent-kane2006-legacy-html
- assessment_id: septin-S2351-A6
  area: grounding
  topic: V0 established subunits remain deferred
  outcome: concern
  summary: Original F1 remains confirmed. Kane secondary synthesis explicitly lists
    yeast V0 a, c, c-prime, c-double-prime, d and e. Evidence-backed label-only component
    rows are permitted now; unresolved exact families/copy numbers do not justify
    omitting the known inventory. Membership does not automatically imply assembly
    necessity.
  target_ids:
  - GO:0000220
  evidence_ids:
  - septin-s2351-record-vacuolar_proton_transporting_v_type_atpase_v0_domain
  - septin-s2351-v0-agent-go
  - septin-s2351-v0-agent-kane2006-legacy-html
  - septin-s2351-policy
- assessment_id: septin-S2351-A7
  area: scope
  topic: V0 source tier, isoform and adapter boundary
  outcome: supported
  summary: Kane is review-tier evidence, with vacuolar Vph1 versus Golgi/endosomal
    Stv1 and dissociation limits retained. Current record names sectors rather than
    genes/loci/accessions or a regulator/transcriptomic claim; do not manufacture
    a named-gene adapter omission for this sparse scope. Catalogue also has no Saccharomyces
    coverage.
  target_ids:
  - GO:0000220
  evidence_ids:
  - septin-s2351-v0-agent-kane2006-legacy-html
  - septin-s2351-current-adapter-catalogue
  - septin-s2351-record-vacuolar_proton_transporting_v_type_atpase_v0_domain
- assessment_id: septin-S2351-A8
  area: identity
  topic: V1 identity and intact-enzyme scope
  outcome: supported
  summary: The specific vacuolar sector is correctly distinguished from its broader
    sector parent and complete GO0016471 V-ATPase. Yeast4932 is a bounded example.
    V1 hydrolysis/rotation couples to V0 in the intact enzyme; ungrounded ATP-hydrolysis
    node avoids treating whole proton transport as an isolated V1 activity.
  target_ids:
  - GO:0000221
  evidence_ids:
  - septin-s2351-record-vacuolar_proton_transporting_v_type_atpase_v1_domain
  - septin-s2351-v1-agent-go
  - septin-s2351-v0-agent-tax-4932
  - septin-s2351-v0-agent-kane2006-legacy-html
- assessment_id: septin-S2351-A9
  area: grounding
  topic: V1 established subunits remain deferred
  outcome: concern
  summary: Original F1 remains confirmed. Kane secondary synthesis explicitly lists
    yeast V1 A, B, C, D, E, F, G and H. Evidence-backed label-only component rows
    are permitted now; unresolved exact families/copy numbers do not justify omitting
    the known inventory. Membership does not automatically imply assembly necessity.
  target_ids:
  - GO:0000221
  evidence_ids:
  - septin-s2351-record-vacuolar_proton_transporting_v_type_atpase_v1_domain
  - septin-s2351-v1-agent-go
  - septin-s2351-v0-agent-kane2006-legacy-html
  - septin-s2351-policy
- assessment_id: septin-S2351-A10
  area: scope
  topic: V1 source tier, isoform and adapter boundary
  outcome: supported
  summary: Kane is review-tier evidence, with vacuolar Vph1 versus Golgi/endosomal
    Stv1 and dissociation limits retained. Current record names sectors rather than
    genes/loci/accessions or a regulator/transcriptomic claim; do not manufacture
    a named-gene adapter omission for this sparse scope. Catalogue also has no Saccharomyces
    coverage. Forgac is fresh abstract/metadata only; historical Key Points access
    is not a fresh complete body read.
  target_ids:
  - GO:0000221
  evidence_ids:
  - septin-s2351-v0-agent-kane2006-legacy-html
  - septin-s2351-current-adapter-catalogue
  - septin-s2351-record-vacuolar_proton_transporting_v_type_atpase_v1_domain
  - septin-s2351-v1-agent-doi-nrm2272
  - septin-s2351-v1-agent-ro-native
- assessment_id: septin-S2351-A11
  area: identity
  topic: Outer membrane broad identity and conditional composition
  outcome: supported
  summary: GO0009279/GO0016020 and tax2/562/83333 match their authorities. Definition
    distinguishes the broad diderm outer membrane from canonical Gram-negative asymmetry.
    LPS is CONDITIONAL, consistent with exceptional LPS-free envelopes. A generic
    beta-barrel cohort spans OmpA/porin/BamA families and does not warrant one guessed
    family ID.
  target_ids:
  - GO:0009279
  evidence_ids:
  - septin-s2351-outer-agent-go
  - septin-s2351-outer-agent-tax-2
  - septin-s2351-outer-agent-tax-562
  - septin-s2351-outer-agent-tax-83333
  - septin-s2351-outer-agent-chebi-16412
  - septin-s2351-outer-agent-sl-0040
  - septin-s2351-outer-agent-matches-P0A910
  - septin-s2351-outer-agent-matches-P06996
  - septin-s2351-outer-agent-matches-P02931
  - septin-s2351-outer-agent-matches-P0A940-retry
  - septin-s2351-outer-agent-silhavy2010-legacy-html
  - septin-s2351-outer-agent-sperandeo2017-legacy-html
- assessment_id: septin-S2351-A12
  area: evidence
  topic: Outer membrane examples and exact source attribution
  outcome: supported
  summary: All eight named products are reviewed K12 accessions matching their genes.
    For four protein examples, native UniProt directly assigns the record-listed location
    PMIDs to SL0040. Exact primary abstracts distinguish refolded OmpA channels, elastase
    exposure, envelope-complex proteomics, porin heterotrimers and BamA structure/CDI.
    Individual full primary tables/methods were not audited.
  target_ids:
  - GO:0009279
  evidence_ids:
  - septin-s2351-outer-agent-P0A910
  - septin-s2351-outer-agent-P06996
  - septin-s2351-outer-agent-P02931
  - septin-s2351-outer-agent-P0A940
  - septin-s2351-outer-agent-P77774
  - septin-s2351-outer-agent-P0A903
  - septin-s2351-outer-agent-P0AC02
  - septin-s2351-outer-agent-P31554
  - septin-s2351-outer-agent-pmid-10636850
  - septin-s2351-outer-agent-pmid-10947984
  - septin-s2351-outer-agent-pmid-16079137
  - septin-s2351-outer-agent-pmid-2464593
  - septin-s2351-outer-agent-pmid-23882017
  - septin-s2351-outer-agent-pmid-24619089
- assessment_id: septin-S2351-A13
  area: graph
  topic: Canonical Lpt/BAM assembly and permeability mechanisms
  outcome: supported
  summary: Secondary source bodies support Lpt-mediated LPS delivery, BAM beta-barrel
    assembly, ordered LPS barrier and selective porin paths in canonical Gram-negative
    envelopes. LptD-only and BAM A/B/C/D xrefs are representative links, not inventories.
    Schema permits protein complexes as GENE_OR_PROTEIN. Excludes is explicitly reduced
    influx; no absolute permeability or detailed atomic sequence is asserted.
  target_ids:
  - GO:0009279
  evidence_ids:
  - septin-s2351-record-cell_outer_membrane
  - septin-s2351-outer-agent-sperandeo2017-legacy-html
  - septin-s2351-outer-agent-hagan2011-pdf
  - septin-s2351-outer-agent-silhavy2010-legacy-html
  - septin-s2351-outer-agent-nikaido2003-browser1
  - septin-s2351-node-types
- assessment_id: septin-S2351-A14
  area: scope
  topic: Collective beta-barrel assembly necessity remains unresolved
  outcome: unknown
  summary: The generic beta-barrel component is marked ESSENTIAL, but inspected review-tier
    mechanism and localization sources do not independently test whether the whole
    structure forms without that collective cohort. Retain the original unknown limitation;
    membership, permeability, activity and cell viability are not interchangeable
    with assembly necessity. No new contradictory deletion result or universal essentiality
    claim was established.
  target_ids:
  - GO:0009279
  evidence_ids:
  - septin-s2351-record-cell_outer_membrane
  - septin-s2351-outer-agent-hagan2011-pdf
  - septin-s2351-outer-agent-silhavy2010-legacy-html
- assessment_id: septin-S2351-A15
  area: scope
  topic: Matched E. coli expression context
  outcome: supported
  summary: 'Fresh precise1k searches resolve ompA b0957, ompC b2215, ompF b0929, bamA
    b0177, bamB b2512, bamC b2477, bamD b2595 and lptD b0054. In each returned 201-module
    array, only ompF has thresholded memberships: k86 UC-3, k88 Nitrogen/Nac, k25
    Lrp and k22 SoxS. Read structured module metadata; excluded AI prose and nonexact
    substring hits. These are expression associations, not physical or necessity proof.'
  target_ids:
  - GO:0009279
  evidence_ids:
  - septin-s2351-current-adapter-catalogue
  - septin-s2351-adapter-search-ompA
  - septin-s2351-adapter-search-ompC
  - septin-s2351-adapter-search-ompF
  - septin-s2351-adapter-search-bamA
  - septin-s2351-adapter-search-bamB
  - septin-s2351-adapter-search-bamC
  - septin-s2351-adapter-search-bamD
  - septin-s2351-adapter-search-lptD
  - septin-s2351-adapter-modules-ompA
  - septin-s2351-adapter-modules-ompC
  - septin-s2351-adapter-modules-ompF
  - septin-s2351-adapter-modules-bamA
  - septin-s2351-adapter-modules-bamB
  - septin-s2351-adapter-modules-bamC
  - septin-s2351-adapter-modules-bamD
  - septin-s2351-adapter-modules-lptD
  - septin-s2351-adapter-module-86
  - septin-s2351-adapter-module-88
  - septin-s2351-adapter-module-25
  - septin-s2351-adapter-module-22
- assessment_id: current-input-comparison
  area: provenance
  topic: Complete frozen-input comparison and bounded refresh
  outcome: supported
  summary: 4 of ten original target hashes differ from current main. The changed content
    is substantively reassessed in the target-specific assessments; original observations
    remain historical and unchanged. All current target and used context bytes are
    frozen.
  target_ids:
  - GO:0044674
  - GO:0009523
  - cellstructuremech:phycobilisome_rod
  - GO:0030096
  - cellstructuremech:rc_lh1_pufx_core_complex
  - GO:0045271
  - GO:0045273
  - GO:0000220
  - GO:0000221
  - GO:0009279
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
- finding_id: plaque-MCR-resolved-F2
  issue_key: energy-complex-mcr-causal-node-component-ref-grounding
  category: graph
  severity: minor
  status: resolved
  certainty: confirmed
  title: MCR graph nodes now retain verified component groundings
  description: 'The three historical omissions are absent from the current record:
    nodes[1..3] now carry InterPro:IPR016212,InterPro:IPR003179,InterPro:IPR003178
    matching their referenced components. Fresh native family definitions and exact
    protein examples support those identities.'
  target_ids:
  - GO:0044674
  field_paths:
  - causal_graphs[0].nodes[1].grounding
  - causal_graphs[0].nodes[2].grounding
  - causal_graphs[0].nodes[3].grounding
  evidence_ids:
  - plaque-current-0
  - plaque-mcr-category-prior
  - plaque-mcr-agent-IPR016212
  - plaque-mcr-agent-IPR003179
  - plaque-mcr-agent-IPR003178-retry
  rule_id: docs/SCHEMA.md:CausalNode-grounding
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/methyl_coenzyme_m_reductase_complex.yaml
    role: maintained_record
  tags:
  - causal-graphs
  - grounding
  - component-ref
  - stage4-record-review
  disposition_reason: Current inspected record resolves all three exact omissions
    from category-review F2. The record repair was already present on main and associated
    issue2432 was already closed; PR2351 adds a current review disposition, not a
    record fix.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261025T071006Z-energy-complex-category-review
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2432
- finding_id: micro-F1
  issue_key: phycobilisome-rod-cpcc-locus-mapping-unverified
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: The cpcC-to-Rupite-locus mapping lacks exact source support
  description: The A0ABT0C7D6 example asserts that cpcC maps to JX360_02095. Its native
    UniProt and source GenPept instead provide only that ORF and a generic predicted
    rod-core linker annotation. The cited NIES-2134 structural paper does not map
    this Rupite locus. Verify exact orthology with an inspectable source, or remove/rephrase
    the unsupported cpcC identity assertion; retain the verified accession/taxon and
    distinguish generic linker membership from gene identity. A different Rupite candidate
    is not established as a replacement.
  target_ids:
  - cellstructuremech:phycobilisome_rod
  field_paths:
  - components[component_id=rod_linker_polypeptides].protein_examples[uniprot_id=UniProtKB:A0ABT0C7D6].role
  - components[component_id=rod_linker_polypeptides].protein_examples[uniprot_id=UniProtKB:A0ABT0C7D6].evidence
  evidence_ids:
  - micro-rod-agent-A0ABT0C7D6
  - micro-rod-agent-MCJ2541704.1-genpept
  - micro-rod-agent-kawakami2022-jats
  - micro-rod-agent-P50034
  - micro-rod-agent-pdb-7veb-entity4
  - micro-protein-policy
  - micro-record-rod
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/phycobilisome_rod.yaml
    role: maintained scientific record
  rule_id: .claude/skills/uniprot-protein-examples/SKILL.md:Rules 2–4
  native_severity: minor
  normalization_reason: This is a bounded example-level provenance gap; rod identity,
    constituent classes and source-backed function remain supported. The review does
    not establish a wrong replacement accession.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T091347Z-phycobilisome-rod-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2543
- finding_id: micro-F2
  issue_key: bacterial-psii-known-core-deferred-for-family-grounding
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Separate known reaction-center membership from family-grounding uncertainty
  description: The psii_subunit_boundaries prompt defers adding all subunit-level
    components until exact family groundings are resolved. Yet the cited Chang2015
    Results and Figure1G identify D1 and D2 as reaction-center subunits in the associated
    PBS preparation. These known core constituents can be represented with source-backed
    labels and unresolved groundings. The consequential gap is the blanket deferral
    of established membership, not the lack of every optional PSII detail.
  target_ids:
  - GO:0030096
  field_paths:
  - components
  - discussions[discussion_id=psii_subunit_boundaries]
  evidence_ids:
  - micro-psii-prep-chang2015-pmc-html
  - micro-record-bacterial-psii
  - micro-policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/plasma_membrane_derived_thylakoid_photosystem_ii.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Components
  native_severity: minor
  normalization_reason: Minor actionable core-composition gap; the exact structure,
    association and physiological role remain supported.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T091348Z-plasma-membrane-derived-thylakoid-photosystem-ii-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2544
- finding_id: septin-S2351-F1
  issue_key: rc-lh1-pufx-known-core-deferred-for-family-grounding
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Separate the established core constituents from family-mapping work
  description: The record has no component rows, and its rc_lh1_pufx_subunit_boundaries
    prompt makes exact family resolution a prerequisite for representing the named
    reaction-center/LH1/PufX constituents. The cited native-array paper already supplies
    the core architecture and reaction-center L/M/H context, while the functional
    study characterizes isolated RC-LH1 complexes. Supported labels can preserve known
    membership without guessed family identifiers or unsupported PufX density assignments.
  target_ids:
  - cellstructuremech:rc_lh1_pufx_core_complex
  field_paths:
  - components
  - discussions[discussion_id=rc_lh1_pufx_subunit_boundaries]
  evidence_ids:
  - septin-s2351-rc-prep-bahatyrova2004-whiterose-pdf
  - septin-s2351-comayras-indexed-body
  - septin-s2351-record-rc_lh1_pufx_core_complex
  - septin-s2351-policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/rc_lh1_pufx_core_complex.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Components
  native_severity: minor
  normalization_reason: Minor consequential known-composition gap; exact core identity
    and bounded functional graph are supported.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T091349Z-rc-lh1-pufx-core-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2545
- finding_id: septin-S2351-F2
  issue_key: v0-known-subunits-deferred-for-family-grounding
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Represent known V0 subunits without waiting for exact family CURIEs
  description: The open v0_subunit_grounding_todo rationale makes family grounding
    a prerequisite to all subunit-level components. Yet the cited Kane2006 review
    explicitly identifies yeast V0 subunits a, c, c-prime, c-double-prime, d and e.
    Evidence-backed label-only component rows are allowed and can retain unresolved
    family identifiers and copy numbers. Revise the blanket deferral and represent
    at least the established core membership, preserving source/taxon boundaries.
    This finding concerns a concrete known inventory and the stated blocking rationale,
    not a general requirement to populate every optional field.
  target_ids:
  - GO:0000220
  field_paths:
  - components
  - discussions[discussion_id=v0_subunit_grounding_todo].rationale
  evidence_ids:
  - septin-s2351-v0-agent-kane2006-legacy-html
  - septin-s2351-v0-agent-go
  - septin-s2351-record-vacuolar_proton_transporting_v_type_atpase_v0_domain
  - septin-s2351-policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_v0_domain.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Composition
    and completeness
  native_severity: minor
  normalization_reason: The sector identity, topology and functions are correct. This
    is a non-blocking recoverable composition gap caused by an unnecessary grounding
    prerequisite, not wrong structure identity or a demand for exact stoichiometry.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T091352Z-vacuolar-proton-transporting-v-type-atpase-v0-domain-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2546
- finding_id: septin-S2351-F3
  issue_key: v1-known-subunits-deferred-for-family-grounding
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Represent known V1 subunits without waiting for exact family CURIEs
  description: The open v1_subunit_grounding_todo rationale makes family grounding
    a prerequisite to all subunit-level components. Yet the cited Kane2006 review
    explicitly identifies yeast V1 subunits A, B, C, D, E, F, G and H. Evidence-backed
    label-only component rows are allowed and can retain unresolved family identifiers
    and copy numbers. Revise the blanket deferral and represent at least the established
    core membership, preserving source/taxon boundaries. This finding concerns a concrete
    known inventory and the stated blocking rationale, not a general requirement to
    populate every optional field.
  target_ids:
  - GO:0000221
  field_paths:
  - components
  - discussions[discussion_id=v1_subunit_grounding_todo].rationale
  evidence_ids:
  - septin-s2351-v0-agent-kane2006-legacy-html
  - septin-s2351-v1-agent-go
  - septin-s2351-record-vacuolar_proton_transporting_v_type_atpase_v1_domain
  - septin-s2351-policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_v1_domain.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Composition
    and completeness
  native_severity: minor
  normalization_reason: The sector identity, topology and functions are correct. This
    is a non-blocking recoverable composition gap caused by an unnecessary grounding
    prerequisite, not wrong structure identity or a demand for exact stoichiometry.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T091354Z-vacuolar-proton-transporting-v-type-atpase-v1-domain-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2547
actions:
- action_id: micro-A1
  finding_ids:
  - micro-F1
  target_ids:
  - cellstructuremech:phycobilisome_rod
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/phycobilisome_rod.yaml
    role: maintained scientific record
  description: In authorized curation, verify the exact cpcC-to-JX360_02095 mapping
    with an explicit native gene/orthology source or retract that role/evidence mapping.
    Do not select another accession from length or generic linker annotation alone.
  acceptance_checks:
  - Inspect exact accession, gene/ORF mapping and strain provenance in the supporting
    source.
  - Keep NIES-2134 experimental evidence separate from Rupite identity-only examples
    and BP-1 model sequence references.
  - Run native protein verify and graph audit in addition to schema/strict/history
    checks; verify role-level mapping manually.
  generator: Maintained structure YAML; derived pages regenerate only after authorized
    curation.
- action_id: micro-A2
  finding_ids:
  - micro-F2
  target_ids:
  - GO:0030096
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/plasma_membrane_derived_thylakoid_photosystem_ii.yaml
    role: maintained scientific record
  description: Add source-backed D1/D2 core constituent rows without guessed identifiers,
    and distinguish exact family resolution from known membership in discussion progress.
    Keep PBS proteins, transient assembly/repair factors and accessory-subunit variation
    separate.
  acceptance_checks:
  - Use the cited Results/immunoblot evidence for D1/D2 membership; do not assert
    that all photosystem subunits were detected in this preparation.
  - Do not interpret missing PsbO detection as native universal absence or claim a
    measured oxygen-evolution rate.
  - Use the guarded record writer, append curation/repository history, regenerate
    pages, and pass native schema/strict/products/history/qc gates in separately authorized
    curation.
  generator: Maintained structure YAML; generated pages derive from it.
- action_id: septin-S2351-AC1
  finding_ids:
  - septin-S2351-F1
  target_ids:
  - cellstructuremech:rc_lh1_pufx_core_complex
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/rc_lh1_pufx_core_complex.yaml
    role: maintained scientific record
  description: Represent source-supported core constituents with evidence and explicit
    unresolved groundings where needed. Distinguish directly resolved reaction-center
    features, established LH1 membership and the paper’s PufX-containing complex interpretation;
    retain exact family and stoichiometry work in the discussion.
  acceptance_checks:
  - Do not claim Bahatyrova2004 directly located the PufX polypeptide; the paper explicitly
    could not identify it.
  - Keep external LH2, cytochrome bc1 and mobile quinone pools distinct from constitutive
    protein members; avoid universal small-subunit stoichiometry.
  - Use the guarded record writer, append curation/repository history, regenerate
    pages, and pass native schema/strict/products/history/qc gates in separately authorized
    curation.
  generator: Maintained structure YAML; generated pages derive from it.
- action_id: septin-S2351-AC2
  finding_ids:
  - septin-S2351-F2
  target_ids:
  - GO:0000220
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_v0_domain.yaml
    role: maintained scientific record
  description: During authorized curation, add source-backed label-only V0 subunit
    components and narrow the TODO to unresolved family mappings/copy numbers.
  acceptance_checks:
  - Use the cited review at its actual review evidence tier; retain yeast and vacuolar-isoform
    boundaries.
  - Distinguish final constituents from dedicated assembly factors; do not assign
    ESSENTIAL from membership or catalytic activity.
  - Leave unverified family CURIEs and numerical stoichiometry unresolved rather than
    borrowing broad domains or newer unsupported counts.
  - Run the required focused schema, strict-reference and review validations.
- action_id: septin-S2351-AC3
  finding_ids:
  - septin-S2351-F3
  target_ids:
  - GO:0000221
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_v1_domain.yaml
    role: maintained scientific record
  description: During authorized curation, add source-backed label-only V1 subunit
    components and narrow the TODO to unresolved family mappings/copy numbers.
  acceptance_checks:
  - Use the cited review at its actual review evidence tier; retain yeast and vacuolar-isoform
    boundaries.
  - Distinguish final constituents from dedicated assembly factors; do not assign
    ESSENTIAL from membership or catalytic activity.
  - Leave unverified family CURIEs and numerical stoichiometry unresolved rather than
    borrowing broad domains or newer unsupported counts.
  - Run the required focused schema, strict-reference and review validations.
limitations:
- 'MCR, respiratory complex I and complex II independent subreview: All three targets
  retain the historical explicitly unknown assembly-necessity assessment. Qualified
  passes cover inspected claims, not proof of every ESSENTIAL assertion.'
- 'MCR, respiratory complex I and complex II independent subreview: Ermler1997 was
  freshly inspected through browser-extracted primary transcription. Direct native
  Gale retrieval yielded an invalid-parameter HTML page and the alternate PDF returned404;
  neither is represented as a paper body. Figure pixels, Table1 and raw coordinates
  were not independently analyzed. Hashes of browser evidence bind serialized tool
  output.'
- 'MCR, respiratory complex I and complex II independent subreview: Wrede2013 claim-bearing
  Methods/Results and captions were inspected; immunolabeling concerns assembled MCR
  antigen and culture-dependent localization. It is not separate experimental localization
  of each subunit.'
- 'MCR, respiratory complex I and complex II independent subreview: Baradaran2013
  JATS Introduction/Results/Methods and associated captions were read, plus supplementary
  Tables3-4 text. Other supplemental alignments/figure pixels and raw maps were not
  reanalyzed. Proton-channel paths and predicted waters remain model-level interpretation.'
- 'MCR, respiratory complex I and complex II independent subreview: Yankovskaya2003
  is freshly abstract-only plus native1NEK deposition/UniProt evidence; no renewed
  full-body access is claimed. Stenberg2005 fresh indexed Methods passages are limited,
  full-page open returned500 and native DOI retrieval was a redirect page. Its detailed
  Sdh result subsection was not independently reread. Daley2005 remains abstract-only
  plus native annotation attribution.'
- 'MCR, respiratory complex I and complex II independent subreview: Four initial InterPro429
  responses were followed by successful bounded retries; both receipts retained. Candidate
  searches are bounded to exact current protein matches and inspected named definitions.
  IPR050573 unchecked LLM description and iModulonDB AI summaries are excluded from
  biological evidence.'
- 'MCR, respiratory complex I and complex II independent subreview: The historical
  iModulonDB runner limitation is not a new execution result. Current public API fallback
  checked complete organism catalogue, one matching MG1655 dataset, exact four genes,
  returned module weights/thresholds and three module annotation/member tables. Other
  E.coli datasets, expression conditions and activity matrices were not reassessed.
  A below-threshold gene does not refute physical membership.'
- 'MCR, respiratory complex I and complex II independent subreview: Category-review
  YAML/Markdown were requested and frozen by root before use. No tracked image or
  neighboring record was used by this reviewer. Root owns current full-corpus QC and
  CI; historical counts in original reviews are not represented as fresh outcomes.'
- 'Photosystem II, phycobilisome rod and bacterial PSII independent subreview: PSII:
  Umena/Kamiya/Kawakami assess purified preparations and selected claim-bearing text/captions.
  No raw diffraction data or figure-pixel reanalysis; PsbY loss, model-sequence borrowing
  and halide substitutions remain preparation-specific. Assembly necessity of each
  metal/pigment class was not independently established.'
- 'Photosystem II, phycobilisome rod and bacterial PSII independent subreview: Phycobilisome
  rod: NIES-2134 dissociated cryo-EM rods are not Rupite localization experiments.
  CpcG2 assignment and precise energy-transfer paths remain tentative. Red-algal context
  is comparative; no exact cpcC replacement is established by length/domain similarity.'
- 'Photosystem II, phycobilisome rod and bacterial PSII independent subreview: Phycobilisome
  rod: new A0ABT0CFU3 is a predicted CpcD identity example with an ORF token. Another
  submitted CpcD paralog occurs in the bounded search; the record does not assert
  uniqueness. Native2/2COVERED does not settle the cpcC free-text mapping.'
- 'Photosystem II, phycobilisome rod and bacterial PSII independent subreview: Bacterial
  PSII: Chang2015 used French pressure,2%TritonX100, gradients and negative staining.
  D1/D2 and limited association are supported; oxygen-evolution activity and intact
  native accessory composition are not newly established. Figures1/5 captions were
  read, not pixels or every supplementary table.'
- 'Photosystem II, phycobilisome rod and bacterial PSII independent subreview: Bacterial
  PSII: Perez2024 fresh access is abstract/metadata only; native publisher returned403
  and browser fulltext route failed. Old browser-indexed body-excerpt access remains
  historical rather than being represented as freshly recovered. Exact GO independently
  supports current broad physiology.'
- 'Photosystem II, phycobilisome rod and bacterial PSII independent subreview: All3
  targets: official iModulonDB fallback is computational PCC7942 context for the broader
  cyanobacterial scope, not direct Thermostichus/Nostoc/red-algal coverage, expression-to-structure
  proof, direct regulation or universal absence. No new native adapter runner execution
  occurred in this subreview; root retains actual historical availability receipt.'
- 'Photosystem II, phycobilisome rod and bacterial PSII independent subreview: All3
  targets: ontology/family inspection is bounded to named exact candidates; no exhaustive
  universal absence claims. Primary bodies/source authorities were freshly fetched;
  no old HTTP result is restamped as fresh. Root owns corpus/CI gates and GitHub issue
  deduplication/mutations.'
- 'Photosystem II, phycobilisome rod and bacterial PSII independent subreview: Workflow
  inventory: conf/record_review.yaml was first read only as route/rubric guidance
  before being added to inspect. Root then froze it in the49-input inventory; exact
  bytes were reread and workflow applicability reassessed at2026-11-03T05:16:19Z.
  This timing correction is disclosed; there is no claim that this one config was
  captured before its initial route-only read.'
- 'RC-LH1-PufX, V0, V1 and outer membrane independent subreview: Bahatyrova native
  PDF body/captions and Methods were read in the stated scope; no figure pixels, AFM
  maps, raw spectroscopy or supplements were reanalyzed. PufX was not directly located;
  source-reported structure is distinguished from inferred physiological transfer.'
- 'RC-LH1-PufX, V0, V1 and outer membrane independent subreview: Comayras fresh native
  retrieval returned403. Fresh indexed coauthor rendering provides abstract, figure
  captions, Introduction and Methods through the start of photoreduction; complete
  later Results, supplemental models and raw data were not read. Original discontinuous-body
  limitation remains inherited, not proof of current whole-body access.'
- 'RC-LH1-PufX, V0, V1 and outer membrane independent subreview: Kane, Forgac, Silhavy,
  Sperandeo, Hagan and Nikaido are secondary reviews. Specific native claim-bearing
  bodies were read except Forgac, where authorization HTML was excluded and exact
  abstract/metadata used. Historical Forgac Key Points access is attributed to the
  original review. Underlying primary experiments are not all independently reviewed.'
- 'RC-LH1-PufX, V0, V1 and outer membrane independent subreview: Outer-membrane individual
  primary studies were freshly checked at abstract/metadata plus direct UniProt attribution.
  Full protein-specific proteomic tables, stock-level Methods and mechanistic raw
  data were not inspected. Reviewed K12 protein identity does not assert every experiment
  used K12.'
- 'RC-LH1-PufX, V0, V1 and outer membrane independent subreview: The original outer-membrane
  collective beta-barrel ESSENTIAL assertion remains an explicit unknown assessment:
  no collective-depletion/assembly experiment was inspected. Representative complex
  xrefs are partial, and expression modules do not establish assembly necessity or
  structural membership.'
- 'RC-LH1-PufX, V0, V1 and outer membrane independent subreview: V0/V1 source-supported
  known labels do not imply verified family CURIEs, exact modern ring/stalk copy numbers,
  assembly factors as constituents, universal isoform placement or necessity. Sparse
  sector-level records are not falsely counted as named-gene adapter omissions.'
- 'RC-LH1-PufX, V0, V1 and outer membrane independent subreview: Official dataset
  coverage is bounded to the returned20 organisms/28 dataset keys. No exact Rhodobacter/Cereibacter
  or yeast match; the E. coli work covers one precise1k dataset, eight exact queries
  and selected relevant module metadata. False substring hits and AI-generated module
  prose are excluded. Empty positive sets are not gene/structure absence.'
- 'RC-LH1-PufX, V0, V1 and outer membrane independent subreview: Historical runner
  failure at2026-11-03T00:49Z remains root-owned prior receipt, not a newly invoked
  runner here. The source APIs provide fallback evidence. One native InterPro BamA
  request initially returned429; later bounded request succeeded. Original native
  validate/render checks all passed; no full corpus QC/CI or GitHub mutation performed
  by this subreview.'
- 'RC-LH1-PufX, V0, V1 and outer membrane independent subreview: Original global-gate
  coverage totals are historical subreview limitations, not current final CI/QC counts.
  Root owns refreshed corpus gates and current native outer-membrane protein/graph
  verifier receipts.'
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
- All ten original YAML/Markdown pairs are preserved unchanged. Current main was merged
  normally and pushed without force.
- One explicit issue-bearing ten-record cohort follows the repository persistence
  policy. Supported records are assessed within that cohort without fabricated findings.
- 'Bundle issues #2541 (four stale reviews) and #2542 (eight structured-source coverage
  defects) are addressed here. Five scientific findings remain in #2543, #2544, #2545,
  #2546 and #2547; existing validator #2514 remains open. MCR #2432 was already closed
  before this review and is not a fix made by this PR.'
- Source commit 3266d0f7239a80f17d74bb0d6e2b3e260000b8dc is retained by tag review-base/pr2351-current-record-followup-20261103.
- CLAUDE.md is an alias of AGENTS.md; canonical regular AGENTS.md bytes are frozen.
- Every source-access and check limitation is attributed to its independent subreview.
  Fresh fetches, cached response re-reading, abstract-only evidence and full-body
  passages retain distinct scopes.
- Seven original bundles omit structured-source applicability, and complex I contains
  an unsupported exemption rationale. MCR omits a formal check rather than containing
  that complex-I check. Sparse V0 and V1 sector records are excluded from this molecular-coverage
  defect.
- Returned AI-generated module prose and unchecked InterPro generated descriptions
  are excluded from scientific support. Bounded transcriptomic context is not structural
  membership, physical interaction or necessity evidence; below-threshold results
  are not biological absence.
- Used scientific local context was frozen before assessment, including the prior
  MCR category-review pair, phycobilisome core and LH2 neighbor, and native UniProt
  verifier source. Final inventory also added conf/record_review.yaml, previously
  read only for workflow routes; workflow applicability was rechecked against its
  frozen bytes before the final verdict.
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T091345Z-methyl-coenzyme-m-reductase-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T091346Z-photosystem-ii-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T091347Z-phycobilisome-rod-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T091348Z-plasma-membrane-derived-thylakoid-photosystem-ii-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T091349Z-rc-lh1-pufx-core-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T091350Z-respiratory-chain-complex-i-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T091351Z-respiratory-chain-complex-ii-succinate-dehydrogenase-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T091352Z-vacuolar-proton-transporting-v-type-atpase-v0-domain-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T091354Z-vacuolar-proton-transporting-v-type-atpase-v1-domain-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T091355Z-cell-outer-membrane-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
links:
- https://github.com/CultureBotAI/CellStructureMech/pull/2351
- https://github.com/CultureBotAI/CellStructureMech/issues/2432
- https://github.com/CultureBotAI/CellStructureMech/issues/2514
- https://github.com/CultureBotAI/CellStructureMech/issues/2541
- https://github.com/CultureBotAI/CellStructureMech/issues/2542
- https://github.com/CultureBotAI/CellStructureMech/issues/2543
- https://github.com/CultureBotAI/CellStructureMech/issues/2544
- https://github.com/CultureBotAI/CellStructureMech/issues/2545
- https://github.com/CultureBotAI/CellStructureMech/issues/2546
- https://github.com/CultureBotAI/CellStructureMech/issues/2547
```
