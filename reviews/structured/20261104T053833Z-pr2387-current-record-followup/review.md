# PR 2387: current-input review of ten records and adversarial follow-up

- Review: 20261104T053833Z-pr2387-current-record-followup
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-11-04T05:27:06.673128Z
- Finished UTC: 2026-11-04T05:38:33Z
- Reviewer: Codex root synthesis with three independent read-only adversarial reviewers (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Current-input successor for all ten PR2387 records. DNA gyrase was stale and substantively refreshed: its two new graph-node family groundings are supported, while its deposition-scope finding remains open. All five inherited scientific findings persist across four records (one major, four minor); six morphology records retain qualified positive outcomes. Three formal expression-only applicability exclusions and seven failed-access evidence-kind occurrences are corrected, while all seven genuine morphology-only exclusions remain justified. All 20 original artifacts remain immutable; only this linked review pair is added.

## Scope And Provenance

Exact ten-record PR cohort reassessed against current main 3b62e24ac00545bbec0797390e6b89389e27992c. Changed inputs are substantively reassessed. Scientific records remain unchanged.

Selection: Complete cohort of ten maintained records reviewed in original PR head 830127e8d6581acf5f927f1ff91f1dca0805257b.
Coverage: full; 10 reviewed / 10 in the declared population.
Source: working_tree at Git base dbdd66f36d1363c94eab2c58305c2f58a68baf09.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0097685 | data/structures/other/dinoflagellate_apical_groove.yaml | maintained | dinoflagellate apical groove |
| GO:0097686 | data/structures/other/dinoflagellate_apical_horn.yaml | maintained | dinoflagellate apical horn |
| GO:0097611 | data/structures/other/dinoflagellate_cingulum.yaml | maintained | dinoflagellate cingulum |
| GO:0097613 | data/structures/other/dinoflagellate_epicone.yaml | maintained | dinoflagellate epicone |
| GO:0097614 | data/structures/other/dinoflagellate_hypocone.yaml | maintained | dinoflagellate hypocone |
| GO:0097618 | data/structures/other/dinoflagellate_sulcal_notch.yaml | maintained | dinoflagellate sulcal notch |
| GO:0097612 | data/structures/other/dinoflagellate_sulcus.yaml | maintained | dinoflagellate sulcus |
| GO:0120217 | data/structures/other/dna_gyrase_complex.yaml | maintained | DNA gyrase complex |
| GO:0044775 | data/structures/other/dna_polymerase_iii_beta_sliding_clamp_processivity_factor_complex.yaml | maintained | DNA polymerase III, beta sliding clamp processivity factor complex |
| GO:0043847 | data/structures/other/dna_polymerase_iii_clamp_loader_chi_psi_subcomplex.yaml | maintained | DNA polymerase III, clamp loader chi/psi subcomplex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full native QC | passed | True | GO:0097685, GO:0097686, GO:0097611, GO:0097613, GO:0097614, GO:0097618, GO:0097612, GO:0120217, GO:0044775, GO:0043847 | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| Native label correspondence | passed | True | GO:0097685, GO:0097686, GO:0097611, GO:0097613, GO:0097614, GO:0097618, GO:0097612, GO:0120217, GO:0044775, GO:0043847 | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| TraitMech references | passed | True | GO:0097685, GO:0097686, GO:0097611, GO:0097613, GO:0097614, GO:0097618, GO:0097612, GO:0120217, GO:0044775, GO:0043847 | Native TraitMech link check passed. |
| Pinned governed files | passed | True | GO:0097685, GO:0097686, GO:0097611, GO:0097613, GO:0097614, GO:0097618, GO:0097612, GO:0120217, GO:0044775, GO:0043847 | Pinned governed files match; native vendored check passed. |
| Native identifier resolver | passed | True | GO:0097685, GO:0097686, GO:0097611, GO:0097613, GO:0097614, GO:0097618, GO:0097612, GO:0120217, GO:0044775, GO:0043847 | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| validate GO:0097685 | passed | True | GO:0097685 | Documented focused command passed. |
| validate-strict GO:0097685 | passed | True | GO:0097685 | Documented focused command passed. |
| validate GO:0097686 | passed | True | GO:0097686 | Documented focused command passed. |
| validate-strict GO:0097686 | passed | True | GO:0097686 | Documented focused command passed. |
| validate GO:0097611 | passed | True | GO:0097611 | Documented focused command passed. |
| validate-strict GO:0097611 | passed | True | GO:0097611 | Documented focused command passed. |
| validate GO:0097613 | passed | True | GO:0097613 | Documented focused command passed. |
| validate-strict GO:0097613 | passed | True | GO:0097613 | Documented focused command passed. |
| validate GO:0097614 | passed | True | GO:0097614 | Documented focused command passed. |
| validate-strict GO:0097614 | passed | True | GO:0097614 | Documented focused command passed. |
| validate GO:0097618 | passed | True | GO:0097618 | Documented focused command passed. |
| validate-strict GO:0097618 | passed | True | GO:0097618 | Documented focused command passed. |
| validate GO:0097612 | passed | True | GO:0097612 | Documented focused command passed. |
| validate-strict GO:0097612 | passed | True | GO:0097612 | Documented focused command passed. |
| validate GO:0120217 | passed | True | GO:0120217 | Documented focused command passed. |
| validate-strict GO:0120217 | passed | True | GO:0120217 | Documented focused command passed. |
| validate GO:0044775 | passed | True | GO:0044775 | Documented focused command passed. |
| validate-strict GO:0044775 | passed | True | GO:0044775 | Documented focused command passed. |
| validate GO:0043847 | passed | True | GO:0043847 | Documented focused command passed. |
| validate-strict GO:0043847 | passed | True | GO:0043847 | Documented focused command passed. |
| Supplemental bounded PMID authority checks | passed | True | GO:0097685, GO:0097686, GO:0097611, GO:0097613, GO:0097614, GO:0097618, GO:0097612, GO:0120217, GO:0044775, GO:0043847 | 909 PMIDs all OK in bounded native requests; full-command limitations remain separate. |
| Official structured-source applicability and covered-dataset cross-checks | passed | False | GO:0097685, GO:0097686, GO:0097611, GO:0097613, GO:0097614, GO:0097618, GO:0097612, GO:0120217, GO:0044775, GO:0043847 | Whole-record applicability was assessed for all ten targets. Gyrase, beta clamp and chi/psi make positive molecular or replication-pathway claims, so their formal expression-only exclusions are corrected. The seven dinoflagellate records assert morphology and topology while deferring molecular claims, so their prose exclusions remain justified. The complete current official catalogue contains no matching dinoflagellate host. The real E. coli precise1k dataset lists five strains; seven exact loci each returned 201 module rows. Only holD b4372 exceeds the ppGpp module 145 threshold, independently confirmed in its 70-gene list. These computational observations do not establish physical assembly, formation, direct regulation or localization; threshold-negative results are not biological absence. BL21(DE3) and MC1061 experimental preparations are not claimed covered by exact strain. Historical runner unavailability is not presented as a fresh invocation. |
| Independent claim-level source review | passed | True | GO:0097685, GO:0097686, GO:0097611, GO:0097613, GO:0097614, GO:0097618, GO:0097612, GO:0120217, GO:0044775, GO:0043847 | Three read-only reviewers covered the complete ten-record cohort, including changed inputs, with explicit scientific findings and source-access limits. Final artifact/head acceptance occurs after saving. |
| Retained historical adapter runner availability | unavailable | False | GO:0097685, GO:0097686, GO:0097611, GO:0097613, GO:0097614, GO:0097618, GO:0097612, GO:0120217, GO:0044775, GO:0043847 | Historical00:49Z invocation unavailable due to OS access restriction. Official catalogue fallback was inspected separately; no fresh invocation is claimed. Actual historical exit1 is retained in the evidence receipt; the native unavailable-check model has no execution exit-code field. |
| Native dinoflagellate apical groove UniProt verify check | passed | True | GO:0097685 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native dinoflagellate apical groove UniProt causal check | passed | True | GO:0097685 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native dinoflagellate apical horn UniProt verify check | passed | True | GO:0097686 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native dinoflagellate apical horn UniProt causal check | passed | True | GO:0097686 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native dinoflagellate cingulum UniProt verify check | passed | True | GO:0097611 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native dinoflagellate cingulum UniProt causal check | passed | True | GO:0097611 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native dinoflagellate epicone UniProt verify check | passed | True | GO:0097613 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native dinoflagellate epicone UniProt causal check | passed | True | GO:0097613 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native dinoflagellate hypocone UniProt verify check | passed | True | GO:0097614 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native dinoflagellate hypocone UniProt causal check | passed | True | GO:0097614 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native dinoflagellate sulcal notch UniProt verify check | passed | True | GO:0097618 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native dinoflagellate sulcal notch UniProt causal check | passed | True | GO:0097618 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native dinoflagellate sulcus UniProt verify check | passed | True | GO:0097612 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native dinoflagellate sulcus UniProt causal check | passed | True | GO:0097612 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native DNA gyrase complex UniProt verify check | passed | True | GO:0120217 | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native DNA gyrase complex UniProt causal check | passed | True | GO:0120217 | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native DNA polymerase III, beta sliding clamp processivity factor complex UniProt verify check | passed | True | GO:0044775 | 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native DNA polymerase III, beta sliding clamp processivity factor complex UniProt causal check | passed | True | GO:0044775 | 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native DNA polymerase III, clamp loader chi/psi subcomplex UniProt verify check | passed | True | GO:0043847 | 2 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native DNA polymerase III, clamp loader chi/psi subcomplex UniProt causal check | passed | True | GO:0043847 | 2 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |

## Scientific And Domain Assessments

### Exact complex and hierarchy

identity: supported. Targets: GO:0120217.

GO0120217/GO0009330 identify bacterial typeII gyrase, with declared GyrA2B2 constituent architecture. GO negative-supercoiling term is activity, not a structure. Species variation in supercoiling proficiency is not silently replaced with universal quantitative activity.

### Substantive stale graph-grounding refresh

provenance: supported. Targets: GO:0120217.

Only dated history and exact family groundings on two existing component_ref nodes changed. IPR005743/GyrA andIPR011557/GyrB are full families matching P0AES4/P0AES6 and the component definitions; new node groundings are supported. No new edge or constituent/necessity claim was introduced; deposition F1 remains independent.

### Reference proteins and current singleton searches

grounding: supported. Targets: GO:0120217.

Reviewed K12 P0AES4/gyrA/b2231 andP0AES6/gyrB/b3699 agree with exact current queries andRCSB entities. Current singleton queries do not certify the October search history. K12 source is distinct from BL21(DE3) recombinant expression.

### Domain versus overall canonical model

evidence: concern. Targets: GO:0120217.

Fresh native6RKU title/entity detail and primary MethodsSec17 identify the closed DNA-binding/cleavage-domain model.6RKW is the overall model. Current canonical note still calls6RKU complete; inherited minor finding persists without disputing correct2:2 proteins or full-length sample identities.

### Activity and experimental preparation limits

evidence: supported. Targets: GO:0120217.

Purified reconstituted E.coli gyrase supports ATP-dependent negative supercoiling and the coarse activity class. Drug/AMP-PNP/DNA trapping used for EM is distinct from supercoiling/ATPase assays. No intact-cell localization, all-species proficiency or precise catalytic sequence is inferred.

### Declared nonmechanistic functional scope

graph: supported. Targets: GO:0120217.

Two constituent contributions, complex enables negative-supercoiling activity and activity acts on DNA are consistent with current source scopes. Explicit NONMECHANISTIC/FUNCTION limits exclude gate dynamics, strand-passage order and specific drug mechanism; no universal formation claim is required.

### Bacterial beta versus PCNA class boundary

identity: concern. Targets: GO:0044775.

The record faithfully reproduces GO0044775 wording, but its claim homodimeric in prokaryotes/homotrimeric in other species conflates named bacterial beta with distinct PCNA/phage classes and misplaces archaeal PCNA. Kong structure, nativeIPR001001 and reviewed archaealO73947 with primaryPCNA abstract establish the conflict. Keep valid GOidentity/E.coli dimer; explicitly document upstream scope conflict.

### Named PolIII subassembly and canonical example

identity: supported. Targets: GO:0044775.

GO0044775 is the exact named beta processivity complex; GO0032991 parent andGO0009360 parthood remain appropriate. Canonical E.coli Kong1992 beta dimer is supported. This does not license transferring every PCNA activity or archaeal identity into this record.

### Verified full beta family

grounding: concern. Targets: GO:0044775.

IPR001001 is a native whole-family entry with matching P0A988 xref, not merely a ring-shaped domain. The current class remains REVIEWED_LABEL_ONLY with unresolved current source-neutral mapping. Inherited minor exact-family finding persists; historical rationale must remain preserved.

### DnaN example and isoform qualification

grounding: supported. Targets: GO:0044775.

Reviewed P0A988/dnaN/b3701 tax83333 matches the current singleton query. Standard beta is a homodimer; native shorter beta* alternative-product notes preclude an invented invariant oligomeric claim for all derived isoforms. Reference K12 identity does not add an experimentally verified exact strain to Kong species-level canonical scope.

### Processivity outline versus direct structural evidence

graph: supported. Targets: GO:0044775.

Kong shows the ring architecture with modeled DNA fit, not a DNA co-crystal. Coarse tethering/encirclement function is independently supported by native authority and prior biochemical context; the graph explicitly withholds ATP-dependent loading sequence and unknown assembly requirements. Exact coreGO0044776 is external partner, not an extra beta constituent.

### Chi/psi heterodimer and hierarchy

identity: supported. Targets: GO:0043847.

GO0043847 matches the1:1 HolC/HolD adaptor; is_a complex and part_of GO0043846 clamp loader are supported. Larger DnaX/SSB partners are excluded from this two-component constituent inventory by explicit scope.

### HolC/HolD and external actors

grounding: supported. Targets: GO:0043847.

Reviewed P28905/holC/b4259 andP28632/holD/b4372 tax83333 match current singleton queries. P06710 correctly covers tau/gamma alternative products; P0AGE0 is SSB. The latter two are external graph actors with UniProt xrefs, appropriately UNANCHORED_WITH_UNIPROT rather than missing component examples.

### Exact whole-family assignments

grounding: concern. Targets: GO:0043847.

Native full-protein HolC IPR007459 and generic HolD IPR004615 agree with the maintained example xrefs; label-only current grounding remains. IPR018382 is a narrower subgroup and need not replace generic psi. Old generic family functional prose does not supersede primary association/function evidence.

### Physical1:1 assembly and partner interaction scope

evidence: supported. Targets: GO:0043847.

Fresh XiaoIII/IV primary abstracts support cloning/identities and1:1 dimer with psi-gamma contact; full bodies remain inaccessible403. Independently read Olson body supports coexpression-soluble complex, sedimentation, tau/gamma affinity and clamp-loader reconstitution. MC1061 artificial-operon preparation and high-concentration bypass are explicit; no universal formation ESSENTIAL or native-cell absence inferred.

### Gamma versus tau and SSB provenance

graph: supported. Targets: GO:0043847.

The psi→gamma wording is bounded to XiaoIV abstract; assembled dimer→tau/gamma is supported by Olson purified-binding experiments. SSB bridge is GO/native HolC/SSB annotation and secondary-review context, not an Olson SSB interaction assay. NONMECHANISTIC/FUNCTION graph does not claim an ordered loading cycle or direct-regulation causality.

### Actual matched dataset and bounded module membership

scope: supported. Targets: GO:0120217.

Official precise1k spans five listed K12-related strains, not exact BL21(DE3) orMC1061 preparations. Each selected native locus was checked across201 returned module rows. All selected loci are threshold-negative. These results do not establish biological absence, direct regulation, physical association, formation or localization.

### Whole-record molecular applicability

scope: concern. Targets: GO:0120217.

Original formal iModulon check excludes cross-checks solely because no expression claim appears, despite positive molecular/replication pathway assertions. Current official catalogue, strain metadata and actual gene/module fallback repair that rationale. Historical unavailable runner is separately dated, never described as newly executed.

### Taxonomic occurrence and experimental limits

scope: supported. Targets: GO:0120217.

COMMON prevalence is qualitative, not a whole-species strain census. Exact native K12 examples differ from species-level canonical examples and experimental expression derivatives; selected dataset has only its five listed strains. No universal prevalence or sample-to-reference strain equality inferred.

### Append-only history and exact predecessor lineage

provenance: supported. Targets: GO:0120217.

Original findings/actions and current discussions/history were read. Historical rationale is preserved as provenance; current exact family/source corrections are separate from dated rationale. No group/category or neighboring issue is resolved by inference; all four original finding keys persist with exact predecessors.

### Actual native checks with finite coverage

schema: supported. Targets: GO:0120217.

All three original pairs validate/render exactly and39 historical input occurrences agree. Actual current protein checks pass: own5 examples and7 typed nodes comprise5 COVERED plus2 external UNANCHORED_WITH_UNIPROT actors, not7covered. Schema success is not source truth or family completeness.

### Complete assigned scope and explicit limits

completeness: supported. Targets: GO:0120217.

Entire current record and immutable pair reviewed. No maintained images/measured-properties require pixel/unit work. Primary bodies/abstracts, secondary review and native authorities remain explicitly separate. No optional example or generic-family type defect is invented.

### Current independent verdict

other: concern. Targets: GO:0120217.

needs_curation: one inherited minor deposition-scope finding; new graph groundings supported.

### Actual matched dataset and bounded module membership

scope: supported. Targets: GO:0044775.

Official precise1k spans five listed K12-related strains, not exact BL21(DE3) orMC1061 preparations. Each selected native locus was checked across201 returned module rows. All selected loci are threshold-negative. These results do not establish biological absence, direct regulation, physical association, formation or localization.

### Whole-record molecular applicability

scope: concern. Targets: GO:0044775.

Original formal iModulon check excludes cross-checks solely because no expression claim appears, despite positive molecular/replication pathway assertions. Current official catalogue, strain metadata and actual gene/module fallback repair that rationale. Historical unavailable runner is separately dated, never described as newly executed.

### Taxonomic occurrence and experimental limits

scope: supported. Targets: GO:0044775.

COMMON prevalence is qualitative, not a whole-species strain census. Exact native K12 examples differ from species-level canonical examples and experimental expression derivatives; selected dataset has only its five listed strains. No universal prevalence or sample-to-reference strain equality inferred.

### Append-only history and exact predecessor lineage

provenance: supported. Targets: GO:0044775.

Original findings/actions and current discussions/history were read. Historical rationale is preserved as provenance; current exact family/source corrections are separate from dated rationale. No group/category or neighboring issue is resolved by inference; all four original finding keys persist with exact predecessors.

### Actual native checks with finite coverage

schema: supported. Targets: GO:0044775.

All three original pairs validate/render exactly and39 historical input occurrences agree. Actual current protein checks pass: own5 examples and7 typed nodes comprise5 COVERED plus2 external UNANCHORED_WITH_UNIPROT actors, not7covered. Schema success is not source truth or family completeness.

### Complete assigned scope and explicit limits

completeness: supported. Targets: GO:0044775.

Entire current record and immutable pair reviewed. No maintained images/measured-properties require pixel/unit work. Primary bodies/abstracts, secondary review and native authorities remain explicitly separate. No optional example or generic-family type defect is invented.

### Current independent verdict

other: concern. Targets: GO:0044775.

needs_curation: one inherited major class-definition finding and one minor exact-family finding; valid E.coli identity retained.

### Actual matched dataset and bounded module membership

scope: supported. Targets: GO:0043847.

Official precise1k spans five listed K12-related strains, not exact BL21(DE3) orMC1061 preparations. Each selected native locus was checked across201 returned module rows. holD alone exceeds ppGpp module145 threshold; the70-gene weight list corroborates that hit, without relying on generated narrative. Other three loci are threshold-negative. These results do not establish biological absence, direct regulation, physical association, formation or localization.

### Whole-record molecular applicability

scope: concern. Targets: GO:0043847.

Original formal iModulon check excludes cross-checks solely because no expression claim appears, despite positive molecular/replication pathway assertions. Current official catalogue, strain metadata and actual gene/module fallback repair that rationale. Historical unavailable runner is separately dated, never described as newly executed.

### Taxonomic occurrence and experimental limits

scope: supported. Targets: GO:0043847.

COMMON prevalence is qualitative, not a whole-species strain census. Exact native K12 examples differ from species-level canonical examples and experimental expression derivatives; selected dataset has only its five listed strains. No universal prevalence or sample-to-reference strain equality inferred.

### Append-only history and exact predecessor lineage

provenance: supported. Targets: GO:0043847.

Original findings/actions and current discussions/history were read. Historical rationale is preserved as provenance; current exact family/source corrections are separate from dated rationale. No group/category or neighboring issue is resolved by inference; all four original finding keys persist with exact predecessors.

### Actual native checks with finite coverage

schema: supported. Targets: GO:0043847.

All three original pairs validate/render exactly and39 historical input occurrences agree. Actual current protein checks pass: own5 examples and7 typed nodes comprise5 COVERED plus2 external UNANCHORED_WITH_UNIPROT actors, not7covered. Schema success is not source truth or family completeness.

### Complete assigned scope and explicit limits

completeness: supported. Targets: GO:0043847.

Entire current record and immutable pair reviewed. No maintained images/measured-properties require pixel/unit work. Primary bodies/abstracts, secondary review and native authorities remain explicitly separate. No optional example or generic-family type defect is invented.

### Current independent verdict

other: concern. Targets: GO:0043847.

needs_curation: one inherited minor two-family grounding finding; primary1:1/partner outline supported.

### Historical access-kind correction

provenance: concern. Targets: GO:0043847.

The original honestly reports HTTP403 and context_only but uses kind database. Correct only to validation/context_only; retain original timestamp/hash and do not allege a false body read or infer scientific refutation.

### Historical access-kind correction

provenance: concern. Targets: GO:0043847.

The original honestly reports HTTP403 and context_only but uses kind database. Correct only to validation/context_only; retain original timestamp/hash and do not allege a false body read or infer scientific refutation.

### taxonomy

scope: supported. Targets: GO:0097685.

Dinophyceae restriction and VARIABLE class occurrence are supported without asserting every member bears every specialized morphology. Species77300 identity and diagnostic groove agree; COMMON is qualitative diagnostic morphology, not a numerical census, and no experimental strain is invented.

### composition

grounding: supported. Targets: GO:0097685.

No molecular constituents/protein examples are positively asserted; targeted openTODO correctly awaits direct localization and exact family evidence. Whole-cell cellulose, membranes, tubulin or flagellar apparatus cannot be inserted as region-specific constituents without support.

### formation necessity

scope: unknown. Targets: GO:0097685.

Morphology, location and class membership do not establish molecular assembly necessity. There are no component essentiality values or depletion assays to reinterpret; acknowledged unknown is not a curation finding.

### structured source

evidence: not_applicable. Targets: GO:0097685.

The full record states morphological identity, taxon scope and descriptive topology, without a positive gene/regulator/pathway/stress/trait/expression-module assertion. Original notes[1] already gives morphology-based exclusion; this is genuineN/A, not an expression-only exemption or omitted assessment. Complete current catalogue separately lacks matching natural hosts; no foreign-host module proxy.

### completeness

completeness: supported. Targets: GO:0097685.

Complete maintained fields and original pair assessed. No maintained images, numerical physical properties, molecular components or mechanism are asserted. Optional fields and targeted molecularTODOs do not require invented enrichment.

### history provenance

provenance: supported. Targets: GO:0097685.

All original target bytes unchanged and original findings/actions empty. Preserve PROPOSED status, dated rationale and prior history; no neighboring/grouped issue resolution inferred. Old shared-base corpus gates remain historical, not fresh execution.

### native validation

schema: supported. Targets: GO:0097685.

Native original validate/render and exact frozen-input proof passed; current actual native protein/graph checks passed with zero examples/zero typednodes. Schema/coverage does not certify scientific truth.

### taxonomy

scope: supported. Targets: GO:0097686.

Dinophyceae restriction and VARIABLE class occurrence are supported without asserting every member bears every specialized morphology. The record makes no compulsory canonical-species or quantitative-prevalence assertion.

### composition

grounding: supported. Targets: GO:0097686.

No molecular constituents/protein examples are positively asserted; targeted openTODO correctly awaits direct localization and exact family evidence. Whole-cell cellulose, membranes, tubulin or flagellar apparatus cannot be inserted as region-specific constituents without support.

### formation necessity

scope: unknown. Targets: GO:0097686.

Morphology, location and class membership do not establish molecular assembly necessity. There are no component essentiality values or depletion assays to reinterpret; acknowledged unknown is not a curation finding.

### structured source

evidence: not_applicable. Targets: GO:0097686.

The full record states morphological identity, taxon scope and descriptive topology, without a positive gene/regulator/pathway/stress/trait/expression-module assertion. Original notes[1] already gives morphology-based exclusion; this is genuineN/A, not an expression-only exemption or omitted assessment. Complete current catalogue separately lacks matching natural hosts; no foreign-host module proxy.

### completeness

completeness: supported. Targets: GO:0097686.

Complete maintained fields and original pair assessed. No maintained images, numerical physical properties, molecular components or mechanism are asserted. Optional fields and targeted molecularTODOs do not require invented enrichment.

### history provenance

provenance: supported. Targets: GO:0097686.

All original target bytes unchanged and original findings/actions empty. Preserve PROPOSED status, dated rationale and prior history; no neighboring/grouped issue resolution inferred. Old shared-base corpus gates remain historical, not fresh execution.

### native validation

schema: supported. Targets: GO:0097686.

Native original validate/render and exact frozen-input proof passed; current actual native protein/graph checks passed with zero examples/zero typednodes. Schema/coverage does not certify scientific truth.

### taxonomy

scope: supported. Targets: GO:0097611.

Dinophyceae restriction and VARIABLE class occurrence are supported without asserting every member bears every specialized morphology. The record makes no compulsory canonical-species or quantitative-prevalence assertion.

### composition

grounding: supported. Targets: GO:0097611.

No molecular constituents/protein examples are positively asserted; targeted openTODO correctly awaits direct localization and exact family evidence. Whole-cell cellulose, membranes, tubulin or flagellar apparatus cannot be inserted as region-specific constituents without support.

### formation necessity

scope: unknown. Targets: GO:0097611.

Morphology, location and class membership do not establish molecular assembly necessity. There are no component essentiality values or depletion assays to reinterpret; acknowledged unknown is not a curation finding.

### structured source

evidence: not_applicable. Targets: GO:0097611.

The full record states morphological identity, taxon scope and descriptive topology, without a positive gene/regulator/pathway/stress/trait/expression-module assertion. Original notes[1] already gives morphology-based exclusion; this is genuineN/A, not an expression-only exemption or omitted assessment. Complete current catalogue separately lacks matching natural hosts; no foreign-host module proxy.

### completeness

completeness: supported. Targets: GO:0097611.

Complete maintained fields and original pair assessed. No maintained images, numerical physical properties, molecular components or mechanism are asserted. Optional fields and targeted molecularTODOs do not require invented enrichment.

### history provenance

provenance: supported. Targets: GO:0097611.

All original target bytes unchanged and original findings/actions empty. Preserve PROPOSED status, dated rationale and prior history; no neighboring/grouped issue resolution inferred. Old shared-base corpus gates remain historical, not fresh execution.

### native validation

schema: supported. Targets: GO:0097611.

Native original validate/render and exact frozen-input proof passed; current actual native protein/graph checks passed with zero examples/zero typednodes. Schema/coverage does not certify scientific truth.

### taxonomy

scope: supported. Targets: GO:0097613.

Dinophyceae restriction and VARIABLE class occurrence are supported without asserting every member bears every specialized morphology. The record makes no compulsory canonical-species or quantitative-prevalence assertion.

### composition

grounding: supported. Targets: GO:0097613.

No molecular constituents/protein examples are positively asserted; targeted openTODO correctly awaits direct localization and exact family evidence. Whole-cell cellulose, membranes, tubulin or flagellar apparatus cannot be inserted as region-specific constituents without support.

### formation necessity

scope: unknown. Targets: GO:0097613.

Morphology, location and class membership do not establish molecular assembly necessity. There are no component essentiality values or depletion assays to reinterpret; acknowledged unknown is not a curation finding.

### structured source

evidence: not_applicable. Targets: GO:0097613.

The full record states morphological identity, taxon scope and descriptive topology, without a positive gene/regulator/pathway/stress/trait/expression-module assertion. Original notes[1] already gives morphology-based exclusion; this is genuineN/A, not an expression-only exemption or omitted assessment. Complete current catalogue separately lacks matching natural hosts; no foreign-host module proxy.

### completeness

completeness: supported. Targets: GO:0097613.

Complete maintained fields and original pair assessed. No maintained images, numerical physical properties, molecular components or mechanism are asserted. Optional fields and targeted molecularTODOs do not require invented enrichment.

### history provenance

provenance: supported. Targets: GO:0097613.

All original target bytes unchanged and original findings/actions empty. Preserve PROPOSED status, dated rationale and prior history; no neighboring/grouped issue resolution inferred. Old shared-base corpus gates remain historical, not fresh execution.

### native validation

schema: supported. Targets: GO:0097613.

Native original validate/render and exact frozen-input proof passed; current actual native protein/graph checks passed with zero examples/zero typednodes. Schema/coverage does not certify scientific truth.

### identity

identity: supported. Targets: GO:0097685.

GO0097685 exactly denotes an apical surface groove rather than whole apex/epicone or flagellar apparatus. Typical looping morphology accommodates the directly described U-shaped species example. Current native taxon77300 bridges old Cochlodinium name to Margalefidinium.

### graph

graph: supported. Targets: GO:0097685.

Two exact direct edges are supported: groove is_aGO0097610 and part_ofGO0097613; Iwataki abstract independently places groove on dorsal epicone. NONMECHANISTIC graph does not imply assembly order or a physiological mechanism.

### source placement

evidence: supported. Targets: GO:0097685.

2010 source supports ultrastructural morphology, whereas2017source supports formal name transfer/genus diagnosis. Gomez ownPuertoRicoLM did not resolve groove andSEM was obscured; no replacement of2010experiment or strain/figure claim. DOI/PMID and authors independently checked.

### identity

identity: supported. Targets: GO:0097686.

GO0097686 is the specialized horn-shaped thecate apex, not generic apex or whole epicone. Exact is_a parent and thecate qualifier agree with current ontology; broad class morphology is not a universal species inventory.

### graph

graph: supported. Targets: GO:0097686.

Horn is_aapex and apex part_ofepicone are direct typed links; horn containment is inherited through that explicit path. Current edge evidence says through-parent, so generic scope wording is not interpreted as a false independent direct GOedge or complete transitive closure.

### bibliography

provenance: supported. Targets: GO:0097686.

Taylor exact title/year/PMID/DOI matches GOxref. Record explicitly limits historical unread review to bibliographic corroboration; current secondary abstract supplies no detailed horn formation evidence and publisher403 is not bodyaccess.

### identity

identity: supported. Targets: GO:0097611.

GO0097611 is transverse cell-surface furrow, with broadcingulum andrelatedgirdle/transversegroove synonyms. Transverseflagellum location does not make flagellar molecular apparatus the groove. Expert account explicitly distinguishes groove-free desmokont flagellation.

### graph

graph: supported. Targets: GO:0097611.

The two-node one-edge graph states exact is_aGO0097610. It does not reconstruct propulsion or furrow assembly; optional motility mechanism is not required to enlarge the topology.

### bibliography

provenance: supported. Targets: GO:0097611.

Taylor citation is explicitly metadata-only historical context, with exact identity corroborated now; current expert morphology andGO support the anatomy. No inaccessible review body is represented as read.

### identity

identity: supported. Targets: GO:0097613.

GO0097613 is anterior region above cingulum, distinct from apex part and posterior hypocone. Relatedepitheca/episome terminology is not asserted as universal exact synonymy across naked/thecate forms.

### graph

graph: supported. Targets: GO:0097613.

Direct native children show apex/groovepart_ofepicone, while definition supports cingulum boundary and anterior/posterior separation. Descriptive has_part is not treated as proof that every species/cell bears apicalgroove or as a literal partition membrane. CurrentVARIABLE scope and NONMECHANISTIC wording retain this limit.

### scope boundaries

scope: supported. Targets: GO:0097613.

Resolved discussions distinguish part-versuswhole apex and siblinghypocone. The word narrower in a historical prompt is qualified by explicit part_of rationale/resolution; no synonym conflation or historical rewrite needed.

### failed access kind

provenance: concern. Targets: GO:0097685.

The original disclosed unsuccessful publisher response is typed database/context_only. Correct successor kind tovalidation/context_only, preserving historical URL/time/status and explicitly scoped scientific evidence. This is a bundle classification issue only, not a record-science defect or allegation of false bodyaccess.

### failed access kind

provenance: concern. Targets: GO:0097686.

The original disclosed unsuccessful publisher response is typed database/context_only. Correct successor kind tovalidation/context_only, preserving historical URL/time/status and explicitly scoped scientific evidence. This is a bundle classification issue only, not a record-science defect or allegation of false bodyaccess.

### failed access kind

provenance: concern. Targets: GO:0097611.

The original disclosed unsuccessful publisher response is typed database/context_only. Correct successor kind tovalidation/context_only, preserving historical URL/time/status and explicitly scoped scientific evidence. This is a bundle classification issue only, not a record-science defect or allegation of false bodyaccess.

### Exact structure identity and synonym scope

identity: supported. Targets: GO:0097614.

Exact posterior region below the cingulum, separated from epicone, matches GO0097614 and the authored orientation text. Broad hypocone and related hyposome/hypotheca scopes preserve athecate/thecate distinctions; antapex is a part, not an exact synonym.

### Typed parentage and regional boundaries

identity: supported. Targets: GO:0097614.

GO0110165 is the direct hypocone parent and GO0097684 is a part_of child; related epicone is its anterior counterpart, not part or synonym.

### Taxonomic restriction without universality

scope: supported. Targets: GO:0097614.

Current only_in_taxon2864 and native ENA class identity agree. VARIABLE is compatible with varied morphotypes and groove-free desmokont forms; no prevalence percentage, majority or universal assertion is inferred.

### Optional constituent inventory

grounding: supported. Targets: GO:0097614.

No components, protein examples or gene/protein nodes occur. Historical OPEN molecular-constituent TODO preserves the source limits of that pass; it is not a claim that no molecule could contribute. Generic whole-cell material is not a localized regional component, and optional slots alone do not require curation.

### Formation necessity not established

grounding: unknown. Targets: GO:0097614.

The record makes no molecular assembly, component essentiality or formation-necessity assertion. Morphological definitions and topology do not identify molecules required for formation; no universal formation requirement is invented.

### Complete descriptive topology

graph: supported. Targets: GO:0097614.

Seven structure nodes/eight edges support is-a,parental regional parthood,the cingulum/epicone boundary and the specialized notch extension/appearance. Reciprocal cingulum edges describe the same spatial boundary, not independent causal experiments. FUNCTION/NONMECHANISTIC scope is accurate; no missing molecular step is inferred.

### Antapex authority discrepancy kept bounded

evidence: supported. Targets: GO:0097614.

GO0097684 itself retains anterior wording, but GO0097618 and the directly inspected orientation authority specify posterior antapex. These three targets use the supported posterior orientation; the neighboring definition error is neither imported as a new target defect nor claimed resolved.

### No invented numerical or image requirements

completeness: not_applicable. Targets: GO:0097614.

No maintained image, measured dimension, stoichiometry or physical-property value is asserted. ToL captions and text were read, no pixels/raw microscopy/supplements; no visual measurement or licence-transfer claim.

### Historical rationale and current assertions

provenance: supported. Targets: GO:0097614.

Dated curation and discussion rationales remain historical and append-only. Current subtype/boundary claims are assessed directly; no history rewrite, status promotion, optional inventory issue or unrelated record disposition is authorized.

### Whole-record structured-source applicability

evidence: not_applicable. Targets: GO:0097614.

All positive assertions concern anatomical regions,furrow placement and descriptive topology; molecular constituents/mechanisms are expressly deferred. Original prose physical-scope exclusion is justified, even without a formal adapter row. Complete current catalogue also lacks a matching Dinophyceae host; no unrelated proxy, downstream query or biological absence inference.

### Frozen inputs and original native contract

schema: supported. Targets: GO:0097614.

Current target matches original frozen hash. Original validate/render exit0, exact Markdown and all15 historical input occurrences verified; separate root protein checks exit0 with empty scope. Old batch26 global gate receipts remain historical; this does not certify future saved-head or CI checks.

### Independent current scientific disposition

consistency: supported. Targets: GO:0097614.

Pass with limitations: exact anatomy,typed topology and bounded taxonomic scope are positively supported, with no confirmed current record finding. Molecular formation and optional constituents remain unknown.

### Exact structure identity and synonym scope

identity: supported. Targets: GO:0097618.

Exact narrower sulcus extending to the posterior antapex and producing bilobed hypocone appearance matches GO0097618. Exact dinoflagellate sulcus notch and related sulcal notch synonyms are correct. Is-a sulcus is distinct from reaching antapex or changing hypocone appearance.

### Typed parentage and regional boundaries

identity: supported. Targets: GO:0097618.

GO0097618 is_a GO0097612; posterior extension and hypocone appearance do not make it a subtype of antapex/hypocone.

### Taxonomic restriction without universality

scope: supported. Targets: GO:0097618.

Current only_in_taxon2864 and native ENA class identity agree. VARIABLE is compatible with varied morphotypes and groove-free desmokont forms; no prevalence percentage, majority or universal assertion is inferred.

### Optional constituent inventory

grounding: supported. Targets: GO:0097618.

No components, protein examples or gene/protein nodes occur. Historical OPEN molecular-constituent TODO preserves the source limits of that pass; it is not a claim that no molecule could contribute. Generic whole-cell material is not a localized regional component, and optional slots alone do not require curation.

### Formation necessity not established

grounding: unknown. Targets: GO:0097618.

The record makes no molecular assembly, component essentiality or formation-necessity assertion. Morphological definitions and topology do not identify molecules required for formation; no universal formation requirement is invented.

### Complete descriptive topology

graph: supported. Targets: GO:0097618.

Four structure nodes/three edges support is-a sulcus, extension to antapex and bilobed hypocone appearance at exact GO morphology tier. FUNCTION/NONMECHANISTIC scope is accurate; no missing molecular step is inferred.

### Antapex authority discrepancy kept bounded

evidence: supported. Targets: GO:0097618.

GO0097684 itself retains anterior wording, but GO0097618 and the directly inspected orientation authority specify posterior antapex. These three targets use the supported posterior orientation; the neighboring definition error is neither imported as a new target defect nor claimed resolved.

### No invented numerical or image requirements

completeness: not_applicable. Targets: GO:0097618.

No maintained image, measured dimension, stoichiometry or physical-property value is asserted. ToL captions and text were read, no pixels/raw microscopy/supplements; no visual measurement or licence-transfer claim.

### Historical rationale and current assertions

provenance: supported. Targets: GO:0097618.

Dated curation and discussion rationales remain historical and append-only. Current subtype/boundary claims are assessed directly; no history rewrite, status promotion, optional inventory issue or unrelated record disposition is authorized.

### Whole-record structured-source applicability

evidence: not_applicable. Targets: GO:0097618.

All positive assertions concern anatomical regions,furrow placement and descriptive topology; molecular constituents/mechanisms are expressly deferred. Original prose physical-scope exclusion is justified, even without a formal adapter row. Complete current catalogue also lacks a matching Dinophyceae host; no unrelated proxy, downstream query or biological absence inference.

### Frozen inputs and original native contract

schema: supported. Targets: GO:0097618.

Current target matches original frozen hash. Original validate/render exit0, exact Markdown and all15 historical input occurrences verified; separate root protein checks exit0 with empty scope. Old batch26 global gate receipts remain historical; this does not certify future saved-head or CI checks.

### Exact ontology-to-paper attribution

provenance: supported. Targets: GO:0097618.

Current GO0097618 definition.xrefs does cite Taylor PMID7002229; metadata confirms title/author/year/DOI and the record honestly limits it to bibliography. GO supports bilobed anatomy; Taylor body has not been independently inspected.

### Independent current scientific disposition

consistency: supported. Targets: GO:0097618.

Pass with limitations: exact anatomy,typed topology and bounded taxonomic scope are positively supported, with no confirmed current record finding. Molecular formation and optional constituents remain unknown.

### Exact structure identity and synonym scope

identity: supported. Targets: GO:0097612.

Exact ventral cell-surface furrow partially housing the longitudinal flagellum and intersecting the cingulum matches GO0097612. Broad sulcus and related longitudinal furrow/groove synonyms retain scope; narrower notch remains a separate subclass.

### Typed parentage and regional boundaries

identity: supported. Targets: GO:0097612.

GO0097612 is_a GO0097610 cell surface furrow; GO0097618 is its narrower child, not a synonym.

### Taxonomic restriction without universality

scope: supported. Targets: GO:0097612.

Current only_in_taxon2864 and native ENA class identity agree. VARIABLE is compatible with varied morphotypes and groove-free desmokont forms; no prevalence percentage, majority or universal assertion is inferred.

### Optional constituent inventory

grounding: supported. Targets: GO:0097612.

No components, protein examples or gene/protein nodes occur. Historical OPEN molecular-constituent TODO preserves the source limits of that pass; it is not a claim that no molecule could contribute. Generic whole-cell material is not a localized regional component, and optional slots alone do not require curation.

### Formation necessity not established

grounding: unknown. Targets: GO:0097612.

The record makes no molecular assembly, component essentiality or formation-necessity assertion. Morphological definitions and topology do not identify molecules required for formation; no universal formation requirement is invented.

### Complete descriptive topology

graph: supported. Targets: GO:0097612.

Three structure nodes/two edges support is-a cell surface furrow and ventral cingulum intersection. FUNCTION/NONMECHANISTIC scope is accurate; no missing molecular step is inferred.

### Antapex authority discrepancy kept bounded

evidence: supported. Targets: GO:0097612.

GO0097684 itself retains anterior wording, but GO0097618 and the directly inspected orientation authority specify posterior antapex. These three targets use the supported posterior orientation; the neighboring definition error is neither imported as a new target defect nor claimed resolved.

### No invented numerical or image requirements

completeness: not_applicable. Targets: GO:0097612.

No maintained image, measured dimension, stoichiometry or physical-property value is asserted. ToL captions and text were read, no pixels/raw microscopy/supplements; no visual measurement or licence-transfer claim.

### Historical rationale and current assertions

provenance: supported. Targets: GO:0097612.

Dated curation and discussion rationales remain historical and append-only. Current subtype/boundary claims are assessed directly; no history rewrite, status promotion, optional inventory issue or unrelated record disposition is authorized.

### Whole-record structured-source applicability

evidence: not_applicable. Targets: GO:0097612.

All positive assertions concern anatomical regions,furrow placement and descriptive topology; molecular constituents/mechanisms are expressly deferred. Original prose physical-scope exclusion is justified, even without a formal adapter row. Complete current catalogue also lacks a matching Dinophyceae host; no unrelated proxy, downstream query or biological absence inference.

### Frozen inputs and original native contract

schema: supported. Targets: GO:0097612.

Current target matches original frozen hash. Original validate/render exit0, exact Markdown and all15 historical input occurrences verified; separate root protein checks exit0 with empty scope. Old batch26 global gate receipts remain historical; this does not certify future saved-head or CI checks.

### Exact ontology-to-paper attribution

provenance: concern. Targets: GO:0097612.

Current GO0097612 definition.xrefs cites PMID20561119, verified as Iwataki2010, rather than Taylor7002229. Both current evidence notes wrongly connect Taylor to this exact GO definition. Taylor may support general background, but unknown body access neither proves nor refutes that; correct only the specific attribution.

### Independent current scientific disposition

consistency: concern. Targets: GO:0097612.

Needs curation for one confirmed inherited minor current GO-definition bibliography attribution; anatomy,scope and topology retain positive support.

### Complete frozen-input comparison and bounded refresh

provenance: supported. Targets: GO:0097685, GO:0097686, GO:0097611, GO:0097613, GO:0097614, GO:0097618, GO:0097612, GO:0120217, GO:0044775, GO:0043847.

1 of ten original target hashes differ from current main. The changed content is substantively reassessed in the target-specific assessments; original observations remain historical and unchanged. All current target and used context bytes are frozen.

## Findings

### micro-F1: Distinguish the cleavage-domain and overall gyrase depositions

minor / open / confirmed; issue key: gyrase-deposition-scope.

The canonical example calls PDB6RKU the complete GyrA2-GyrB2 cryo-EM assembly. Its native title and primary Methods Sec17 identify6RKU as the closed DNA-binding/cleavage-domain model and6RKW as the overall model. The two correct protein entity mappings and2:2 stoichiometry are unaffected.

### micro-F2: Keep the beta-clamp definition distinct from PCNA

major / open / confirmed; issue key: beta-clamp-cross-class-definition.

The definition asserts that this DNA polymeraseIII beta subcomplex is homodimeric in prokaryotes and homotrimeric in other species. Kong1992 instead distinguishes the bacterial beta ring from analogous PCNA and phage factors, and native IPR001001 separates the classes. GO0044775 carries the same conflation; its own cited O73947 is an archaeal PCNA homotrimer.

### micro-F3: Ground the beta subunit with its exact family

minor / open / confirmed; issue key: beta-clamp-exact-family.

IPR001001 directly identifies the full beta sliding-clamp family and is carried by the maintained P0A988 example, but the component remains REVIEWED_LABEL_ONLY and the current TODO defers that mapping.

### micro-F4: Ground HolC and HolD with their exact families

minor / open / confirmed; issue key: chi-psi-exact-families.

The two named rows remain REVIEWED_LABEL_ONLY despite native full-protein families IPR007459 for HolC and IPR004615 for HolD and matching reviewed-example xrefs. The narrower psi subgroup is not required to map the generic psi class.

### septin-dinoflagellate_sulcus-F1: Correct the claimed GO sulcus definition reference

minor / open / confirmed; issue key: dinoflagellate-sulcus-go-definition-reference-attribution.

The record’s PMID7002229 note calls Taylor1980 the review cited by GO0097612, and the matching DOI note calls it corroboration for that definition xref. The inspected current GO0097612 definition.xrefs lists PMID20561119, Tree of Life and Wikipedia; native PMID20561119 is Iwataki et al.2010. Taylor7002229 is a valid paper and is cited by the neighboring notch term, but that does not establish this claimed exact GO-to-paper link. No claim is made that Taylor lacks sulcus content or that the historical failed-access notes are false. Fresh current QuickGO and exact MED records independently reconfirm this same localized attribution defect. Preserve the legitimate posterior/ventral anatomy and historical access statements.

## Recommended Actions And Acceptance Checks

### micro-A1

In separately authorized record curation, qualify6RKU as the domain-focused State1 deposition, or use the verified6RKW entry for an explicitly overall-model canonical example; retain6RKU where its GyrA/B entity mapping is the relevant evidence.

- Keep K12 source distinct from BL21(DE3) expression.
- Do not describe full sample sequences as proof of complete atomic coverage.
- Preserve supported identifiers, examples and biological scope; pass applicable native validation.
- Preserve historical discussions.rationale, posed_date and dated history; append provenance and update current notes/prompt only as supported.
- No record edits occur in this review PR. Keep primary body/abstract/authority tiers and experimental strain/formation limits explicit.

### micro-A2

In separately authorized record curation, retain GO0044775 and the bacterial DnaN identity, but replace the cross-class stoichiometry sentence with source-backed bacterial beta scope; use bacterial or explicitly E.coli wording in the corresponding component claims. Record the upstream GO conflict explicitly, and keep PCNA/phage analogies separate.

- Do not silently relabel PCNA as a PolIII beta subcomplex.
- Preserve the correct dimeric E.coli canonical example and P0A988.
- Do not assert invariant oligomerization for every DnaN-derived isoform.
- Preserve supported identifiers, examples and biological scope; pass applicable native validation.
- Preserve historical discussions.rationale, posed_date and dated history; append provenance and update current notes/prompt only as supported.
- No record edits occur in this review PR. Keep primary body/abstract/authority tiers and experimental strain/formation limits explicit.

### micro-A3

In separately authorized record curation, use verified IPR001001 for the DnaN beta class and update current grounding notes/TODO, preserving the taxon-specific example.

- Confirm native family type/name/signatures and P0A988 membership; do not substitute clamp domains.
- Preserve supported identifiers, examples and biological scope; pass applicable native validation.
- Preserve historical discussions.rationale, posed_date and dated history; append provenance and update current notes/prompt only as supported.
- No record edits occur in this review PR. Keep primary body/abstract/authority tiers and experimental strain/formation limits explicit.

### micro-A4

In separately authorized record curation, use the two verified exact families and update current grounding status/notes/TODO, preserving correct proteins,1:1 stoichiometry and gamma-versus-tau edge scope.

- Check native whole-family type/name/signature and example xrefs.
- Do not use a broad superfamily or promote stale family functional prose over primary experiments.
- Preserve supported identifiers, examples and biological scope; pass applicable native validation.
- Preserve historical discussions.rationale, posed_date and dated history; append provenance and update current notes/prompt only as supported.
- No record edits occur in this review PR. Keep primary body/abstract/authority tiers and experimental strain/formation limits explicit.

### septin-dinoflagellate_sulcus-A1

Correct the current GO0097612 bibliography description to its inspected PMID20561119 reference, verifying any new bibliography and retaining the actual readable tier. Taylor may remain as clearly labeled general background or historical context if useful, but must not be described as this current GO definition’s xref. Preserve the valid morphology and honest historical access limitation. Change only current scientific notes or append a clearly dated clarification through separately authorized guarded curation; preserve all dated rationale/history. Record curation stays outside this review PR.

- The exact current GO0097612-to-PMID attribution agrees with the native definition.xrefs response.
- Any Taylor evidence is explicitly general or historical rather than falsely attributed to the current GO definition.
- Native schema, strict and CURIE checks pass after separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| current-record-0 | data/structures/other/dinoflagellate_apical_groove.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 7577f4358ce9bcc9753ec38e0295a7e496261827869f77353480ef2b130ad1f4; current SHA256 7577f4358ce9bcc9753ec38e0295a7e496261827869f77353480ef2b130ad1f4. Record bytes unchanged since the original review. |
| original-review-0 | reviews/structured/20261022T054302Z-dinoflagellate-apical-groove-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-1 | data/structures/other/dinoflagellate_apical_horn.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 77b2ec19b71236a91786a44611abcc34eb6a7e927763f6ff641f2c879813c344; current SHA256 77b2ec19b71236a91786a44611abcc34eb6a7e927763f6ff641f2c879813c344. Record bytes unchanged since the original review. |
| original-review-1 | reviews/structured/20261022T054304Z-dinoflagellate-apical-horn-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-2 | data/structures/other/dinoflagellate_cingulum.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 c29822ebb0e810421c4516a4db5b8e6d648739e5c563e491d584850a65011513; current SHA256 c29822ebb0e810421c4516a4db5b8e6d648739e5c563e491d584850a65011513. Record bytes unchanged since the original review. |
| original-review-2 | reviews/structured/20261022T054304Z-dinoflagellate-cingulum-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-3 | data/structures/other/dinoflagellate_epicone.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 30e41a70bae04d4698b3b0bc40226fb51727a9f8664c4031c3ae8145216dfcdd; current SHA256 30e41a70bae04d4698b3b0bc40226fb51727a9f8664c4031c3ae8145216dfcdd. Record bytes unchanged since the original review. |
| original-review-3 | reviews/structured/20261022T054305Z-dinoflagellate-epicone-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-4 | data/structures/other/dinoflagellate_hypocone.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 0a596b02f63ce6799d10b49b4cf34a921fb2ae92e1208ee599a96ed47c5f40a1; current SHA256 0a596b02f63ce6799d10b49b4cf34a921fb2ae92e1208ee599a96ed47c5f40a1. Record bytes unchanged since the original review. |
| original-review-4 | reviews/structured/20261022T054306Z-dinoflagellate-hypocone-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-5 | data/structures/other/dinoflagellate_sulcal_notch.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 0e3dace360a1a70bc43f318649972ebb63a50628897c7681bb81c9c75f18c7b1; current SHA256 0e3dace360a1a70bc43f318649972ebb63a50628897c7681bb81c9c75f18c7b1. Record bytes unchanged since the original review. |
| original-review-5 | reviews/structured/20261022T054307Z-dinoflagellate-sulcal-notch-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-6 | data/structures/other/dinoflagellate_sulcus.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 b3606a5c03fbc85a602f3ea6927c22e49eedbcd00d1e9607c85ac080205bd356; current SHA256 b3606a5c03fbc85a602f3ea6927c22e49eedbcd00d1e9607c85ac080205bd356. Record bytes unchanged since the original review. |
| original-review-6 | reviews/structured/20261022T054307Z-dinoflagellate-sulcus-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-7 | data/structures/other/dna_gyrase_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 5f4e9e6f29de383572bdbea4aabb06fd250a5faeedd5facf716a7d57c860a263; current SHA256 5e7e1a94281ec5bb4c72ea205e6e44bc4545175d4051eab98df531f709ac35b8. Changed record reassessed against current sources. |
| original-review-7 | reviews/structured/20261022T054333Z-dna-gyrase-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-8 | data/structures/other/dna_polymerase_iii_beta_sliding_clamp_processivity_factor_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 0369f6dedbb1719e899d2bc9895033ab1dc7652865adb0597e10901b4e5ce664; current SHA256 0369f6dedbb1719e899d2bc9895033ab1dc7652865adb0597e10901b4e5ce664. Record bytes unchanged since the original review. |
| original-review-8 | reviews/structured/20261022T054334Z-dna-polymerase-iii-beta-sliding-clamp-processivity-factor-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-9 | data/structures/other/dna_polymerase_iii_clamp_loader_chi_psi_subcomplex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 ae7299b0c7b889f3f035fe582e2b6c8fddb1a507dd0e1ceadda8c1d8e73a60cb; current SHA256 ae7299b0c7b889f3f035fe582e2b6c8fddb1a507dd0e1ceadda8c1d8e73a60cb. Record bytes unchanged since the original review. |
| original-review-9 | reviews/structured/20261022T054335Z-dna-polymerase-iii-clamp-loader-chi-psi-subcomplex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| micro-record-0 | data/structures/other/dna_gyrase_complex.yaml; Complete current maintained YAML at dbdd66f36d1363c94eab2c58305c2f58a68baf09 | supports | Entire identity/hierarchy/components/examples/taxonomy/functions/graph/discussions/history reviewed; no maintained image or measurement rows. Protein and gene classes are distinguished from the complex and external graph actors. |
| micro-prior-0 | reviews/structured/20261022T054333Z-dna-gyrase-complex-audit/review.yaml; Complete immutable original YAML and derived Markdown | supports | Original checks, evidence access limits, assessments, findings and actions read; old source reads remain historical and are not certified as fresh retrieval. |
| micro-delta-0 | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/7-stale.diff; Original frozen record versus current main 3b62e24ac00545bbec0797390e6b89389e27992c | supports | Only gyrase differs: dated history plus InterPro groundings on two existing component_ref graph nodes. Beta and chi/psi remain byte-identical. No constituent/edge was added by this delta. |
| micro-record-1 | data/structures/other/dna_polymerase_iii_beta_sliding_clamp_processivity_factor_complex.yaml; Complete current maintained YAML at dbdd66f36d1363c94eab2c58305c2f58a68baf09 | supports | Entire identity/hierarchy/components/examples/taxonomy/functions/graph/discussions/history reviewed; no maintained image or measurement rows. Protein and gene classes are distinguished from the complex and external graph actors. |
| micro-prior-1 | reviews/structured/20261022T054334Z-dna-polymerase-iii-beta-sliding-clamp-processivity-factor-complex-audit/review.yaml; Complete immutable original YAML and derived Markdown | supports | Original checks, evidence access limits, assessments, findings and actions read; old source reads remain historical and are not certified as fresh retrieval. |
| micro-delta-1 | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/8-stale.diff; Original frozen record versus current main 3b62e24ac00545bbec0797390e6b89389e27992c | supports | Only gyrase differs: dated history plus InterPro groundings on two existing component_ref graph nodes. Beta and chi/psi remain byte-identical. No constituent/edge was added by this delta. |
| micro-record-2 | data/structures/other/dna_polymerase_iii_clamp_loader_chi_psi_subcomplex.yaml; Complete current maintained YAML at dbdd66f36d1363c94eab2c58305c2f58a68baf09 | supports | Entire identity/hierarchy/components/examples/taxonomy/functions/graph/discussions/history reviewed; no maintained image or measurement rows. Protein and gene classes are distinguished from the complex and external graph actors. |
| micro-prior-2 | reviews/structured/20261022T054335Z-dna-polymerase-iii-clamp-loader-chi-psi-subcomplex-audit/review.yaml; Complete immutable original YAML and derived Markdown | supports | Original checks, evidence access limits, assessments, findings and actions read; old source reads remain historical and are not certified as fresh retrieval. |
| micro-delta-2 | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/9-stale.diff; Original frozen record versus current main 3b62e24ac00545bbec0797390e6b89389e27992c | supports | Only gyrase differs: dated history plus InterPro groundings on two existing component_ref graph nodes. Beta and chi/psi remain byte-identical. No constituent/edge was added by this delta. |
| micro-policy | docs/CURATION.md; Exact class/family grounding; formation versus function; discussions append-only rationale/history | supports | Verified full-protein class mapping is separate from reference-strain examples. UNKNOWN formation is not automatically a finding. Preserve historical rationale/posed_date; update current notes and append provenance after supported curation. |
| micro-schema | src/cellstructuremech/schema/cellstructuremech.yaml; Component classes, graph actors/scope, hierarchy and essentiality | supports | Generic families and scoped nonmechanistic outlines are permitted. External DnaX/SSB actors need not become chi/psi constituents or optional examples. |
| micro-native-policy | .claude/skills/review-yaml-record/SKILL.md; Structured Source Cross-Checks with profile/config/checklist | supports | Positive molecular/pathway claims trigger applicability; no expression assertion is not sufficient exclusion. Catalogue and actual gene/module checks retain strain and computational limits. Seventeen common inputs match previously read bytes; current review skill/profile/config and pertinent policies reread. |
| micro-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Constituent references and NONMECHANISTIC FUNCTION outlines | supports | Coarse contributes-to and functional edges are evaluated within explicit scope, without adding ordered reactions, universal essentiality or exact atomic interfaces. |
| micro-original-audit | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/original-audit.json; Six actual original validate/render commands;39 historical input occurrences;6 original artifacts | supports | All original YAMLs validate and deterministically render their retained Markdown. All39 historical input hashes agree at their recorded source revision; all6 original artifacts match the original PR head. |
| micro-up-O73947 | https://rest.uniprot.org/uniprotkb/O73947.json; Native accession/status/name/primary gene/loci/taxon/InterPro and relevant complete FUNCTION/SUBUNIT/alternative-products clauses; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/up-O73947.raw | supports | O73947: UniProtKB reviewed (Swiss-Prot); DNA polymerase sliding clamp; genes ['pcn']; loci ['PF0983']; taxon 186497; InterPro ['IPR046938', 'IPR000730', 'IPR022649', 'IPR022659', 'IPR022648']. Current native identity, family links and pertinent function/subunit annotations; linked studies are not all independently body-read. Archaeal PCNA homotrimer in Pyrococcus furiosus reference strain, not a bacterial PolIII beta protein. |
| micro-up-P06710 | https://rest.uniprot.org/uniprotkb/P06710.json; Native accession/status/name/primary gene/loci/taxon/InterPro and relevant complete FUNCTION/SUBUNIT/alternative-products clauses; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/up-P06710.raw | supports | P06710: UniProtKB reviewed (Swiss-Prot); DNA polymerase III subunit tau; genes ['dnaX']; loci ['b0470', 'JW0459']; taxon 83333; InterPro ['IPR003593', 'IPR001270', 'IPR008921', 'IPR022001', 'IPR022754', 'IPR012763', 'IPR021029', 'IPR050238', 'IPR045085', 'IPR027417', 'IPR038249']. Current native identity, family links and pertinent function/subunit annotations; linked studies are not all independently body-read. Tau/gamma arise through programmed frameshifting; these are external partner products, not added chi/psi constituents. |
| micro-up-P0A988 | https://rest.uniprot.org/uniprotkb/P0A988.json; Native accession/status/name/primary gene/loci/taxon/InterPro and relevant complete FUNCTION/SUBUNIT/alternative-products clauses; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/up-P0A988.raw | supports | P0A988: UniProtKB reviewed (Swiss-Prot); Beta sliding clamp; genes ['dnaN']; loci ['b3701', 'JW3678']; taxon 83333; InterPro ['IPR046938', 'IPR001001', 'IPR022635', 'IPR022637', 'IPR022634']. Current native identity, family links and pertinent function/subunit annotations; linked studies are not all independently body-read. Full-length beta homodimer is distinguished from a shorter beta* isoform; no invariant oligomerization assertion for all isoforms. |
| micro-up-P0AES4 | https://rest.uniprot.org/uniprotkb/P0AES4.json; Native accession/status/name/primary gene/loci/taxon/InterPro and relevant complete FUNCTION/SUBUNIT/alternative-products clauses; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/up-P0AES4.raw | supports | P0AES4: UniProtKB reviewed (Swiss-Prot); DNA gyrase subunit A; genes ['gyrA']; loci ['b2231', 'JW2225']; taxon 83333; InterPro ['IPR005743', 'IPR006691', 'IPR035516', 'IPR013760', 'IPR013758', 'IPR013757', 'IPR002205', 'IPR050220']. Current native identity, family links and pertinent function/subunit annotations; linked studies are not all independently body-read. |
| micro-up-P0AES6 | https://rest.uniprot.org/uniprotkb/P0AES6.json; Native accession/status/name/primary gene/loci/taxon/InterPro and relevant complete FUNCTION/SUBUNIT/alternative-products clauses; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/up-P0AES6.raw | supports | P0AES6: UniProtKB reviewed (Swiss-Prot); DNA gyrase subunit B; genes ['gyrB']; loci ['b3699', 'JW5625']; taxon 83333; InterPro ['IPR002288', 'IPR011557', 'IPR049353', 'IPR041423', 'IPR036890', 'IPR003594', 'IPR020568', 'IPR014721', 'IPR001241', 'IPR013760', 'IPR000565', 'IPR013759', 'IPR013506', 'IPR018522', 'IPR006171', 'IPR034160']. Current native identity, family links and pertinent function/subunit annotations; linked studies are not all independently body-read. |
| micro-up-P0AGE0 | https://rest.uniprot.org/uniprotkb/P0AGE0.json; Native accession/status/name/primary gene/loci/taxon/InterPro and relevant complete FUNCTION/SUBUNIT/alternative-products clauses; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/up-P0AGE0.raw | supports | P0AGE0: UniProtKB reviewed (Swiss-Prot); Single-stranded DNA-binding protein; genes ['ssb']; loci ['b4059', 'JW4020']; taxon 83333; InterPro ['IPR012340', 'IPR000424', 'IPR011344']. Current native identity, family links and pertinent function/subunit annotations; linked studies are not all independently body-read. SSB/HolC contact is native annotation context, not an Olson1995 SSB-binding measurement. |
| micro-up-P28632 | https://rest.uniprot.org/uniprotkb/P28632.json; Native accession/status/name/primary gene/loci/taxon/InterPro and relevant complete FUNCTION/SUBUNIT/alternative-products clauses; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/up-P28632.raw | supports | P28632: UniProtKB reviewed (Swiss-Prot); DNA polymerase III subunit psi; genes ['holD']; loci ['b4372', 'JW4334']; taxon 83333; InterPro ['IPR004615', 'IPR036654', 'IPR018382']. Current native identity, family links and pertinent function/subunit annotations; linked studies are not all independently body-read. |
| micro-up-P28905 | https://rest.uniprot.org/uniprotkb/P28905.json; Native accession/status/name/primary gene/loci/taxon/InterPro and relevant complete FUNCTION/SUBUNIT/alternative-products clauses; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/up-P28905.raw | supports | P28905: UniProtKB reviewed (Swiss-Prot); DNA polymerase III subunit chi; genes ['holC']; loci ['b4259', 'JW4216']; taxon 83333; InterPro ['IPR007459', 'IPR036768']. Current native identity, family links and pertinent function/subunit annotations; linked studies are not all independently body-read. |
| micro-query-dnaN | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdnaN%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete exact reviewed gene/taxon returned page; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/query-dnaN.raw | supports | Current bounded query returns ['P0A988']; singleton matches the maintained example. This does not reconstruct an October selection query or prove physical membership. |
| micro-query-gyrA | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AgyrA%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete exact reviewed gene/taxon returned page; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/query-gyrA.raw | supports | Current bounded query returns ['P0AES4']; singleton matches the maintained example. This does not reconstruct an October selection query or prove physical membership. |
| micro-query-gyrB | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AgyrB%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete exact reviewed gene/taxon returned page; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/query-gyrB.raw | supports | Current bounded query returns ['P0AES6']; singleton matches the maintained example. This does not reconstruct an October selection query or prove physical membership. |
| micro-query-holC | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AholC%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete exact reviewed gene/taxon returned page; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/query-holC.raw | supports | Current bounded query returns ['P28905']; singleton matches the maintained example. This does not reconstruct an October selection query or prove physical membership. |
| micro-query-holD | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AholD%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete exact reviewed gene/taxon returned page; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/query-holD.raw | supports | Current bounded query returns ['P28632']; singleton matches the maintained example. This does not reconstruct an October selection query or prove physical membership. |
| micro-tax-186497 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/186497; Exact taxon identity/name/rank/lineage; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/tax-186497.raw | supports | 186497: Pyrococcus furiosus DSM 3638, rank strain, lineage Archaea; Methanobacteriati; Methanobacteriota; Thermococci; Thermococcales; Thermococcaceae; Pyrococcus; . K12 source/reference, BL21(DE3) expression and species-level examples remain distinct. |
| micro-tax-469008 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/469008; Exact taxon identity/name/rank/lineage; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/tax-469008.raw | supports | 469008: Escherichia coli BL21(DE3), rank strain, lineage Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria; Enterobacterales; Enterobacteriaceae; Escherichia; . K12 source/reference, BL21(DE3) expression and species-level examples remain distinct. |
| micro-tax-562 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562; Exact taxon identity/name/rank/lineage; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/tax-562.raw | supports | 562: Escherichia coli, rank species, lineage Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria; Enterobacterales; Enterobacteriaceae; Escherichia; . K12 source/reference, BL21(DE3) expression and species-level examples remain distinct. |
| micro-tax-83333 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333; Exact taxon identity/name/rank/lineage; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/tax-83333.raw | supports | 83333: Escherichia coli K-12, rank strain, lineage Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria; Enterobacterales; Enterobacteriaceae; Escherichia; . K12 source/reference, BL21(DE3) expression and species-level examples remain distinct. |
| micro-go-0003918 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0003918; Exact active term identity, definition, synonyms and relevant child relationship records; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/go-0003918.raw | supports | GO:0003918: DNA topoisomerase type II (double strand cut, ATP-hydrolyzing) activity; obsolete=False; definition: {'text': 'Catalysis of a DNA topological transformation by transiently cleaving a pair of complementary DNA strands to form a gate through which a second double-stranded DNA segment is passed, after which the severed strands in the first DNA segment are rejoined, driven by ATP hydrolysis. The enzyme changes the linking number in multiples of 2.', 'xrefs': [{'dbCode': 'PMID', 'dbId': '8811192'}]}. Native ontology wording is separately checked against primary biology; GO0044775 itself contains the disputed cross-class language. |
| micro-go-0006260 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0006260; Exact active term identity, definition, synonyms and relevant child relationship records; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/go-0006260.raw | supports | GO:0006260: DNA replication; obsolete=False; definition: {'text': 'The cellular metabolic process in which a cell duplicates one or more molecules of DNA. DNA replication begins when specific sequences, known as origins of replication, are recognized and bound by the origin recognition complex, and ends when the original DNA molecule has been completely duplicated and the copies topologically separated. The unit of replication usually corresponds to the genome of the cell, an organelle, or a virus. The template for replication can either be an existing DNA molecule or RNA.'}. Native ontology wording is separately checked against primary biology; GO0044775 itself contains the disputed cross-class language. |
| micro-go-0009330 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009330; Exact active term identity, definition, synonyms and relevant child relationship records; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/go-0009330.raw | supports | GO:0009330: DNA topoisomerase type II (double strand cut, ATP-hydrolyzing) complex; obsolete=False; definition: {'text': 'Complex that possesses DNA topoisomerase II (double strand cut, ATP-hydrolyzing) activity.', 'xrefs': [{'dbCode': 'WikiPedia', 'dbId': 'Type_II_topoisomerase'}]}. Native ontology wording is separately checked against primary biology; GO0044775 itself contains the disputed cross-class language. |
| micro-go-0009360 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009360; Exact active term identity, definition, synonyms and relevant child relationship records; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/go-0009360.raw | supports | GO:0009360: DNA polymerase III complex; obsolete=False; definition: {'text': "The DNA polymerase III holoenzyme is a complex that contains 10 different types of subunits. These subunits are organized into 3 functionally essential sub-assemblies: the pol III core, the beta sliding clamp processivity factor and the clamp-loading complex. The pol III core carries out the polymerase and the 3'-5' exonuclease proofreading activities. The polymerase is tethered to the template via the sliding clamp processivity factor. The clamp-loading complex assembles the beta processivity factor onto the primer template and plays a central role in the organization and communication at the replication fork.", 'xrefs': [{'dbCode': 'PMID', 'dbId': '11525729'}, {'dbCode': 'PMID', 'dbId': '12940977'}, {'dbCode': 'UniProt', 'dbId': 'P06710'}]}. Native ontology wording is separately checked against primary biology; GO0044775 itself contains the disputed cross-class language. |
| micro-go-0032991 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032991; Exact active term identity, definition, synonyms and relevant child relationship records; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/go-0032991.raw | supports | GO:0032991: protein-containing complex; obsolete=False; definition: {'text': 'A stable assembly of two or more macromolecules, i.e. proteins, nucleic acids, carbohydrates or lipids, in which at least one component is a protein and the constituent parts function together.'}. Native ontology wording is separately checked against primary biology; GO0044775 itself contains the disputed cross-class language. |
| micro-go-0034335 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0034335; Exact active term identity, definition, synonyms and relevant child relationship records; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/go-0034335.raw | supports | GO:0034335: DNA negative supercoiling activity; obsolete=False; definition: {'text': 'Catalytic introduction of negative supercoils into a DNA molecule or region thereof. In bacteria, negative supercoils are only introduced by DNA gyrase, a type II topoisomerase, but not all DNA gyrases are capable of introducing supercoils. In bacteria, the level of supercoiling varies widely between species and has been characterized properly in only a handful of organisms. The best characterized enzyme, from E.coli, is exceptionally proficient at supercoiling and this ability is not representative of all bacteria.', 'xrefs': [{'dbCode': 'WikiPedia', 'dbId': 'DNA_gyrase'}]}. Native ontology wording is separately checked against primary biology; GO0044775 itself contains the disputed cross-class language. |
| micro-go-0043846 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0043846; Exact active term identity, definition, synonyms and relevant child relationship records; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/go-0043846.raw | supports | GO:0043846: DNA polymerase III, clamp loader complex; obsolete=False; definition: {'text': 'A heptamer that includes the tau and gamma products of the dnaX gene and the chi/psi subcomplex. Confers structural asymmetry that allows the polymerase to replicate both leading and lagging strands.', 'xrefs': [{'dbCode': 'PMID', 'dbId': '12940977'}]}. Native ontology wording is separately checked against primary biology; GO0044775 itself contains the disputed cross-class language. |
| micro-go-0043847 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0043847; Exact active term identity, definition, synonyms and relevant child relationship records; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/go-0043847.raw | supports | GO:0043847: DNA polymerase III, clamp loader chi/psi subcomplex; obsolete=False; definition: {'text': 'A dimer composed of the chi and psi subunits which is a subassembly of the DNA polymerase III clamp loader complex and serves as a bridge between the DnaX complex and the single-stranded DNA-binding protein (SSB).', 'xrefs': [{'dbCode': 'PMID', 'dbId': '12940977'}]}. Native ontology wording is separately checked against primary biology; GO0044775 itself contains the disputed cross-class language. |
| micro-go-0044775 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0044775; Exact active term identity, definition, synonyms and relevant child relationship records; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/go-0044775.raw | supports | GO:0044775: DNA polymerase III, beta sliding clamp processivity factor complex; obsolete=False; definition: {'text': 'A subcomplex of the DNA polymerase III holoenzyme which is responsible for tethering the catalytic subunit of DNA polymerase to DNA during high-speed replication. The complex is homodimeric in prokaryotes, and homotrimeric in other species.', 'xrefs': [{'dbCode': 'UniProt', 'dbId': 'O73947'}]}. Native ontology wording is separately checked against primary biology; GO0044775 itself contains the disputed cross-class language. |
| micro-go-0044776 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0044776; Exact active term identity, definition, synonyms and relevant child relationship records; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/go-0044776.raw | supports | GO:0044776: DNA polymerase III, core complex; obsolete=False; definition: {'text': "The DNA polymerase III core complex consists of the alpha,epsilon and theta subunits and is carries out the polymerase and the 3'-5' exonuclease proofreading activities.", 'xrefs': [{'dbCode': 'UniProt', 'dbId': 'P06710'}]}. Native ontology wording is separately checked against primary biology; GO0044775 itself contains the disputed cross-class language. |
| micro-go-0120217 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0120217; Exact active term identity, definition, synonyms and relevant child relationship records; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/go-0120217.raw | supports | GO:0120217: DNA gyrase complex; obsolete=False; definition: {'text': 'A bacterial type IIA topoisomerase that is unique in its function of introducing negative supercoils into DNA at the expense of ATP hydrolysis and is also capable of relaxing positive supercoils, an activity shared with topoisomerase IV. Typically, it is composed of two copies each of an A subunit (GyrA) and a B subunit (GyrB).', 'xrefs': [{'dbCode': 'PMID', 'dbId': '1657531'}, {'dbCode': 'PMID', 'dbId': '20675723'}, {'dbCode': 'Wikipedia', 'dbId': 'DNA_gyrase'}]}. Native ontology wording is separately checked against primary biology; GO0044775 itself contains the disputed cross-class language. |
| micro-isa-0043847 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0043847/ancestors?relations=is_a; Complete explicitly is_a-filtered ancestor response; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/isa-0043847.raw | supports | Exact ancestry is checked independently of parthood; the named complex parent relationship is supported. Raw response retained for typed ancestor audit; no mixed-relation closure inferred. |
| micro-isa-0044775 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0044775/ancestors?relations=is_a; Complete explicitly is_a-filtered ancestor response; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/isa-0044775.raw | supports | Exact ancestry is checked independently of parthood; the named complex parent relationship is supported. Raw response retained for typed ancestor audit; no mixed-relation closure inferred. |
| micro-isa-0120217 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0120217/ancestors?relations=is_a; Complete explicitly is_a-filtered ancestor response; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/isa-0120217.raw | supports | Exact ancestry is checked independently of parthood; the named complex parent relationship is supported. Raw response retained for typed ancestor audit; no mixed-relation closure inferred. |
| micro-ipr-IPR005743 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005743/; Complete native name/type/hierarchy/integrated signatures, description and curation flags; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/ipr-IPR005743.raw | supports | IPR005743: {'name': 'DNA gyrase, subunit A', 'short': 'GyrA'}; type family; signatures {'hamap': {'MF_01897': 'DNA gyrase subunit A [gyrA]'}}. Exact whole-protein family and matching maintained UniProt example xref. |
| micro-ipr-IPR011557 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR011557/; Complete native name/type/hierarchy/integrated signatures, description and curation flags; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/ipr-IPR011557.raw | supports | IPR011557: {'name': 'DNA gyrase, subunit B', 'short': 'GyrB'}; type family; signatures {'hamap': {'MF_01898': 'DNA gyrase subunit B [gyrB]'}, 'ncbifam': {'TIGR01059': 'DNA gyrase subunit B'}}. Exact whole-protein family and matching maintained UniProt example xref. |
| micro-ipr-IPR001001-retry | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001001/; Complete native name/type/hierarchy/integrated signatures, description and curation flags; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/ipr-IPR001001-retry.raw | supports | IPR001001: {'name': 'DNA polymerase III, beta sliding clamp', 'short': 'DNA_polIII_beta'}; type family; signatures {'pirsf': {'PIRSF000804': 'Predicted DNA-directed DNA polymerase III, beta subunit'}, 'cdd': {'cd00140': 'beta_clamp'}, 'panther': {'PTHR30478': 'DNA POLYMERASE III SUBUNIT BETA'}, 'ncbifam': {'TIGR00663': 'DNA polymerase III subunit beta'}, 'smart': {'SM00480': 'DNA polymerase III beta subunit'}}. Exact whole-protein family and matching maintained UniProt example xref. Native family distinguishes bacterial beta from archaeal/eukaryotic PCNA; generic functional prose is not primary experimental evidence. |
| micro-ipr-IPR007459 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007459/; Complete native name/type/hierarchy/integrated signatures, description and curation flags; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/ipr-IPR007459.raw | supports | IPR007459: {'name': 'DNA polymerase III chi subunit, HolC', 'short': 'DNA_pol3_chi'}; type family; signatures {'panther': {'PTHR38767': 'DNA POLYMERASE III SUBUNIT CHI'}, 'pfam': {'PF04364': 'DNA polymerase III chi subunit, HolC'}}. Exact whole-protein family and matching maintained UniProt example xref. |
| micro-ipr-IPR004615 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004615/; Complete native name/type/hierarchy/integrated signatures, description and curation flags; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/ipr-IPR004615.raw | supports | IPR004615: {'name': 'DNA polymerase III, psi subunit', 'short': 'DNA_pol_III_psi'}; type family; signatures {'pirsf': {'PIRSF029225': 'DNA polymerase III, psi subunit'}, 'pfam': {'PF03603': 'DNA polymerase III psi subunit'}}. Exact whole-protein family and matching maintained UniProt example xref. Historical generic unknown-function prose does not supersede Xiao/Olson primary observations. |
| micro-ipr-IPR018382 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR018382/; Complete native name/type/hierarchy/integrated signatures, description and curation flags; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/ipr-IPR018382.raw | context_only | IPR018382: {'name': 'DNA polymerase III, psi subunit, subgroup', 'short': 'DNA_pol_III_psi_subgr'}; type family; signatures {'ncbifam': {'TIGR00664': 'DNA polymerase III subunit psi'}}. Narrower HolD subgroup under IPR004615, not required to ground the generic psi class. |
| micro-pmid-11266590 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11266590+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=1000; Complete exact MED title/authors/year/DOI and deposited abstract; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/pmid-11266590.raw | supports | 11266590: Crystal structure of an archaeal DNA sliding clamp: proliferating cell nuclear antigen from Pyrococcus furiosus.; DOI 10.1110/ps.36401. Primary-study abstract, independently read completely. No full-body read is implied by this row. |
| micro-pmid-12940977 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12940977+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=1000; Complete exact MED title/authors/year/DOI and deposited abstract; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/pmid-12940977.raw | context_only | 12940977: Chromosomal replicases as asymmetric dimers: studies of subunit arrangement and functional consequences.; DOI 10.1046/j.1365-2958.2003.03645.x. Secondary review abstract; context only. No full-body read is implied by this row. |
| micro-pmid-1349852 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A1349852+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=1000; Complete exact MED title/authors/year/DOI and deposited abstract; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/pmid-1349852.raw | supports | 1349852: Three-dimensional structure of the beta subunit of E. coli DNA polymerase III holoenzyme: a sliding DNA clamp.; DOI 10.1016/0092-8674(92)90445-i. Primary-study abstract, independently read completely. No full-body read is implied by this row. |
| micro-pmid-31666516 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A31666516+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=1000; Complete exact MED title/authors/year/DOI and deposited abstract; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/pmid-31666516.raw | supports | 31666516: Cryo-EM structure of the complete E. coli DNA gyrase nucleoprotein complex.; DOI 10.1038/s41467-019-12914-y. Primary-study abstract, independently read completely. No full-body read is implied by this row. |
| micro-pmid-7494000 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A7494000+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=1000; Complete exact MED title/authors/year/DOI and deposited abstract; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/pmid-7494000.raw | supports | 7494000: DnaX complex of Escherichia coli DNA polymerase III holoenzyme. The chi psi complex functions by increasing the affinity of tau and gamma for delta.delta' to a physiologically relevant range.; DOI 10.1074/jbc.270.49.29570. Primary-study abstract, independently read completely. No full-body read is implied by this row. |
| micro-pmid-8389364 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8389364+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=1000; Complete exact MED title/authors/year/DOI and deposited abstract; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/pmid-8389364.raw | supports | 8389364: DNA polymerase III accessory proteins. III. holC and holD encoding chi and psi.; DOI 10.1016/s0021-9258(19)50266-6. Primary-study abstract, independently read completely. No full-body read is implied by this row. |
| micro-pmid-8505305 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8505305+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=1000; Complete exact MED title/authors/year/DOI and deposited abstract; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/pmid-8505305.raw | supports | 8505305: DNA polymerase III accessory proteins. IV. Characterization of chi and psi.; DOI 10.1016/s0021-9258(19)50267-8. Primary-study abstract, independently read completely. No full-body read is implied by this row. |
| micro-gyrase2019-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC6821735.1/PMC6821735.1.xml; Genuine JATS Introduction Sec1; Results Sec3–4 and Fig1–3 text captions; Discussion Sec8; Methods Sec10–13,17,20–21; no pixels/supplements/coordinates; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/gyrase2019-jats.raw | supports | Full-length proteins expressed in BL21(DE3) were purified and reconstituted; trapped gepotidacin/AMP-PNP/DNA cryo-EM preparations differ from activity assays. Sec17 explicitly distinguishes closed cleavage-domain6RKU from overall6RKW. K12 protein source and correct2:2 protein stoichiometry are unaffected; complete sample sequences do not imply complete atomic coordinates. |
| micro-pdb-6RKU-entry | https://data.rcsb.org/rest/v1/core/entry/6RKU; Exact native title/citation/experimental method/resolution and entry assembly information; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/pdb-6RKU-entry.raw | supports | 6RKU is the DNA-binding/cleavage-domain State1 model at4.0Å. Both link the same2019 study; no coordinate/pixel inspection claimed. |
| micro-pdb-6RKU-assembly | https://data.rcsb.org/rest/v1/core/assembly/6RKU/1; Complete assembly1 protein/NA counts and modeled versus total polymer monomers; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/pdb-6RKU-assembly.raw | supports | 6RKU models1848 of3422 polymer monomers. Both have4 protein instances and4 DNA-chain instances; the portal octamer count is not8 protein subunits. Protein entities and sample lengths are distinct from modeled coverage. |
| micro-pdb-6RKW-entry | https://data.rcsb.org/rest/v1/core/entry/6RKW; Exact native title/citation/experimental method/resolution and entry assembly information; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/pdb-6RKW-entry.raw | supports | 6RKW is the complete/overall gyrase-DNA model at6.6Å. Both link the same2019 study; no coordinate/pixel inspection claimed. |
| micro-pdb-6RKW-assembly | https://data.rcsb.org/rest/v1/core/assembly/6RKW/1; Complete assembly1 protein/NA counts and modeled versus total polymer monomers; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/pdb-6RKW-assembly.raw | supports | 6RKW models3458 of3598 polymer monomers. Both have4 protein instances and4 DNA-chain instances; the portal octamer count is not8 protein subunits. Protein entities and sample lengths are distinct from modeled coverage. |
| micro-pdb-6RKU-entity1 | https://data.rcsb.org/rest/v1/core/polymer_entity/6RKU/1; Native polymer entity identity/details/copy count/sample length/UniProt/source and expression taxa; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/pdb-6RKU-entity1.raw | supports | Entity1 is GyrA P0AES4,875 sample residues,2 copies. SourceK12 tax83333, expressionBL21(DE3) tax469008; details explicitly identify DNA-binding/cleavage-domain scope. Full sample sequences remain consistent with incomplete modeled coordinates. |
| micro-pdb-6RKU-entity2 | https://data.rcsb.org/rest/v1/core/polymer_entity/6RKU/2; Native polymer entity identity/details/copy count/sample length/UniProt/source and expression taxa; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/pdb-6RKU-entity2.raw | supports | Entity2 is GyrB P0AES6,804 sample residues,2 copies. SourceK12 tax83333, expressionBL21(DE3) tax469008; details explicitly identify DNA-binding/cleavage-domain scope. Full sample sequences remain consistent with incomplete modeled coordinates. |
| micro-kong1992-pdf | https://odonnell.rockefeller.edu/assets/pdfs/27.pdf; Genuine author-hosted PDF; extracted pp425,427,432–434: Summary/Introduction, architecture and Fig2–3 text captions, sequence comparison/Fig9 caption, conclusion and crystallization/data-collection paragraphs; no pixels; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/kong1992-pdf.raw | supports | E.coli beta forms a homodimer with three domains per monomer at2.5Å. DNA placement in the central hole is modeled rather than an observed DNA co-crystal. PCNA/phage clamp analogies are distinguished from bacterial beta identity; the later archaealPCNA primary abstract supplies trimer context. No claim of complete-paper or figure-pixel inspection. |
| micro-olson1995-pdf | https://www.colorado.edu/lab/mchenry/sites/default/files/attached-files/1995_14285_jbc_270_29570.pdf; Genuine author-hosted PDF pp29570–29576 main Introduction, Methods, Results and Discussion; TablesI/II and Fig1–7 text captions; no pixels/raw data; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/olson1995-pdf.raw | supports | MC1061/pMAF310 holC-holD overexpression yields a soluble1:1 complex; purified partner-binding and reconstitution assays support tau/gamma association and enhanced delta/delta-prime affinity. This is not an SSB contact assay or universal native essentiality proof. High other-subunit concentrations permit omission in vitro; experimental MC1061 is not a listed precise1k strain. |
| micro-xiao1993iii-publisher-access | https://www.jbc.org/article/S0021-9258(19)50266-6/fulltext; Actual retained access response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/xiao1993iii-publisher.raw | context_only | HTTP403 access diagnostic only; no source body supported. Independent abstract or successful exact-authority retry is separately recorded. |
| micro-xiao1993iv-publisher-access | https://www.jbc.org/article/S0021-9258(19)50267-8/fulltext; Actual retained access response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/xiao1993iv-publisher.raw | context_only | HTTP403 access diagnostic only; no source body supported. Independent abstract or successful exact-authority retry is separately recorded. |
| micro-ipr-IPR001001-access | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001001/; Actual retained access response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/ipr-IPR001001.raw | context_only | HTTP429 access diagnostic only; no source body supported. Independent abstract or successful exact-authority retry is separately recorded. |
| micro-historical-replication50-agent-xiao1993iii-publisher | https://www.jbc.org/article/S0021-9258(19)50266-6/fulltext; Retained publisher access response | context_only | Publisher fulltext request returned HTTP403; no primary body was obtained from this route. Original timestamp/hash preserved; no fresh retrieval claim. Kind corrected from database to validation/context_only; original already disclosed failed access. |
| micro-historical-replication50-agent-xiao1993iv-publisher | https://www.jbc.org/article/S0021-9258(19)50267-8/fulltext; Retained publisher access response | context_only | Publisher fulltext request returned HTTP403; no primary body was obtained from this route. Original timestamp/hash preserved; no fresh retrieval claim. Kind corrected from database to validation/context_only; original already disclosed failed access. |
| micro-catalogue | https://imodulondb.org/api/datasets; Complete official organism/dataset catalogue response; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/catalogue.raw | supports | All20 returned organism rows and dataset listings inspected; E.coli precise1k is an actual available host/dataset. Selection is not a universal catalogue or future coverage claim. |
| micro-ecoli-meta | https://imodulondb.org/api/datasets/e_coli/precise1k/meta; Complete precise1k metadata and five-strain list; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/ecoli-meta.raw | context_only | Five strains BW25113,DGF-298,GMOS,MG1655,W3110;1035 samples,518 conditions,201 modules,4257 genes. This selected K12-related reference context is not exact MC1061 or BL21(DE3) experimental coverage. |
| micro-ecoli-modules | https://imodulondb.org/api/datasets/e_coli/precise1k/imodulons; Complete201 module-list metadata, names/regulators/functions; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/ecoli-modules.raw | context_only | All201 returned entries assessed as a bounded dataset inventory; module naming alone is not mechanism or biological evidence. |
| micro-ecoli-gene-b2231 | https://imodulondb.org/api/genes/b2231/imodulons?organism=e_coli&amp;dataset=precise1k; All201 exact-locus weight/threshold/membership rows; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/ecoli-gene-b2231.raw | context_only | Native locus b2231 returns201 rows; above-threshold hits []. Computational threshold membership/nonmembership does not establish physical assembly, formation, localization, dispensability or direct regulation. |
| micro-ecoli-gene-b3699 | https://imodulondb.org/api/genes/b3699/imodulons?organism=e_coli&amp;dataset=precise1k; All201 exact-locus weight/threshold/membership rows; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/ecoli-gene-b3699.raw | context_only | Native locus b3699 returns201 rows; above-threshold hits []. Computational threshold membership/nonmembership does not establish physical assembly, formation, localization, dispensability or direct regulation. |
| micro-ecoli-gene-b3701 | https://imodulondb.org/api/genes/b3701/imodulons?organism=e_coli&amp;dataset=precise1k; All201 exact-locus weight/threshold/membership rows; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/ecoli-gene-b3701.raw | context_only | Native locus b3701 returns201 rows; above-threshold hits []. Computational threshold membership/nonmembership does not establish physical assembly, formation, localization, dispensability or direct regulation. |
| micro-ecoli-gene-b4259 | https://imodulondb.org/api/genes/b4259/imodulons?organism=e_coli&amp;dataset=precise1k; All201 exact-locus weight/threshold/membership rows; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/ecoli-gene-b4259.raw | context_only | Native locus b4259 returns201 rows; above-threshold hits []. Computational threshold membership/nonmembership does not establish physical assembly, formation, localization, dispensability or direct regulation. |
| micro-ecoli-gene-b4372 | https://imodulondb.org/api/genes/b4372/imodulons?organism=e_coli&amp;dataset=precise1k; All201 exact-locus weight/threshold/membership rows; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/ecoli-gene-b4372.raw | context_only | Native locus b4372 returns201 rows; above-threshold hits [{"k": 145, "name": "ppGpp", "regulator": ["ppGpp"], "function": "Stringent response", "category": "Global Stress", "weight": 0.055361181, "threshold": 0.048379363, "in_imodulon": true}]. Computational threshold membership/nonmembership does not establish physical assembly, formation, localization, dispensability or direct regulation. |
| micro-ecoli-gene-b0470 | https://imodulondb.org/api/genes/b0470/imodulons?organism=e_coli&amp;dataset=precise1k; All201 exact-locus weight/threshold/membership rows; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/ecoli-gene-b0470.raw | context_only | Native locus b0470 returns201 rows; above-threshold hits []. Computational threshold membership/nonmembership does not establish physical assembly, formation, localization, dispensability or direct regulation. |
| micro-ecoli-gene-b4059 | https://imodulondb.org/api/genes/b4059/imodulons?organism=e_coli&amp;dataset=precise1k; All201 exact-locus weight/threshold/membership rows; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/ecoli-gene-b4059.raw | context_only | Native locus b4059 returns201 rows; above-threshold hits []. Computational threshold membership/nonmembership does not establish physical assembly, formation, localization, dispensability or direct regulation. |
| micro-ecoli-module-145 | https://imodulondb.org/api/imodulons/e_coli/precise1k/145; Actual module145 metadata and complete70-gene weight list; threshold0.048379363; AI summary/activity narrative excluded; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/ecoli-module-145.raw | context_only | Module145 is ppGpp/Stringent response/Global Stress; holD b4372 weight0.055361181 exceeds threshold0.048379363. The70-gene module is computational context, not a chi/psi assembly or direct regulation experiment. Generated AI prose and unsupported inferred pathway narratives are not used. |
| micro-historical-runner | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Actual historical2026-11-03T00:49:00.848907–00:49:00.863225Z runner receipt | context_only | Historical unavailable/exit1 permission limitation only; no fresh invocation claimed. Current official API fallback independently inspected above. |
| micro-native-dna_gyrase_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dna_gyrase_complex-uniprot-verify-receipt.json; Actual command receipt; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dna_gyrase_complex-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0; 2 reviewed examples/2 COVERED typed nodes. This implemented accession/example coverage does not certify biological completeness or exact source-neutral family mapping. |
| micro-native-dna_gyrase_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dna_gyrase_complex-uniprot-causal-receipt.json; Actual command receipt; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dna_gyrase_complex-uniprot-causal.log SHA256 e9925e98caefb278bed69f8a980ae3af6087a314dde6560afdf7442ac66a91b6 | supports | Actual exit0; 2 reviewed examples/2 COVERED typed nodes. This implemented accession/example coverage does not certify biological completeness or exact source-neutral family mapping. |
| micro-native-dna_polymerase_iii_beta_sliding_clamp_processivity_factor_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dna_polymerase_iii_beta_sliding_clamp_processivity_factor_complex-uniprot-verify-receipt.json; Actual command receipt; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dna_polymerase_iii_beta_sliding_clamp_processivity_factor_complex-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0; 1 reviewed example/1 COVERED typed node. This implemented accession/example coverage does not certify biological completeness or exact source-neutral family mapping. |
| micro-native-dna_polymerase_iii_beta_sliding_clamp_processivity_factor_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dna_polymerase_iii_beta_sliding_clamp_processivity_factor_complex-uniprot-causal-receipt.json; Actual command receipt; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dna_polymerase_iii_beta_sliding_clamp_processivity_factor_complex-uniprot-causal.log SHA256 f767c55c18149a7ee0e0ecba42cf7bf6e538b498174ff3403619159559db03b6 | supports | Actual exit0; 1 reviewed example/1 COVERED typed node. This implemented accession/example coverage does not certify biological completeness or exact source-neutral family mapping. |
| micro-native-dna_polymerase_iii_clamp_loader_chi_psi_subcomplex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dna_polymerase_iii_clamp_loader_chi_psi_subcomplex-uniprot-verify-receipt.json; Actual command receipt; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dna_polymerase_iii_clamp_loader_chi_psi_subcomplex-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0; 2 reviewed examples/2 COVERED plus2 UNANCHORED_WITH_UNIPROT typed nodes (DnaX andSSB external actors). This implemented accession/example coverage does not certify biological completeness or exact source-neutral family mapping. |
| micro-native-dna_polymerase_iii_clamp_loader_chi_psi_subcomplex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dna_polymerase_iii_clamp_loader_chi_psi_subcomplex-uniprot-causal-receipt.json; Actual command receipt; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dna_polymerase_iii_clamp_loader_chi_psi_subcomplex-uniprot-causal.log SHA256 b18c6192090adcab5331b9e6ba8404fd4684eab9585b0e5b5e6f36d94b560551 | supports | Actual exit0; 2 reviewed examples/2 COVERED plus2 UNANCHORED_WITH_UNIPROT typed nodes (DnaX andSSB external actors). This implemented accession/example coverage does not certify biological completeness or exact source-neutral family mapping. |
| plaque-current-0 | data/structures/other/dinoflagellate_apical_groove.yaml; Entire maintained record at frozen source dbdd66f36d1363c94eab2c58305c2f58a68baf09 | supports | Complete definition, hierarchy, taxonomic distribution, evidence, graph, discussions and history independently read. Original target bytes unchanged. No molecular components, protein examples, measurements or maintained images asserted. |
| plaque-original-0-yaml | reviews/structured/20261022T054302Z-dinoflagellate-apical-groove-audit/review.yaml; Historical complete paired observation and deterministic Markdown equivalence | supports | Original qualified verdict, all scientific assessments/evidence scopes and empty findings/actions independently reassessed; original corpus runs remain historical, not current execution. |
| plaque-original-0-md | reviews/structured/20261022T054302Z-dinoflagellate-apical-groove-audit/review.md; Historical complete paired observation and deterministic Markdown equivalence | supports | Original qualified verdict, all scientific assessments/evidence scopes and empty findings/actions independently reassessed; original corpus runs remain historical, not current execution. |
| plaque-current-1 | data/structures/other/dinoflagellate_apical_horn.yaml; Entire maintained record at frozen source dbdd66f36d1363c94eab2c58305c2f58a68baf09 | supports | Complete definition, hierarchy, taxonomic distribution, evidence, graph, discussions and history independently read. Original target bytes unchanged. No molecular components, protein examples, measurements or maintained images asserted. |
| plaque-original-1-yaml | reviews/structured/20261022T054304Z-dinoflagellate-apical-horn-audit/review.yaml; Historical complete paired observation and deterministic Markdown equivalence | supports | Original qualified verdict, all scientific assessments/evidence scopes and empty findings/actions independently reassessed; original corpus runs remain historical, not current execution. |
| plaque-original-1-md | reviews/structured/20261022T054304Z-dinoflagellate-apical-horn-audit/review.md; Historical complete paired observation and deterministic Markdown equivalence | supports | Original qualified verdict, all scientific assessments/evidence scopes and empty findings/actions independently reassessed; original corpus runs remain historical, not current execution. |
| plaque-current-2 | data/structures/other/dinoflagellate_cingulum.yaml; Entire maintained record at frozen source dbdd66f36d1363c94eab2c58305c2f58a68baf09 | supports | Complete definition, hierarchy, taxonomic distribution, evidence, graph, discussions and history independently read. Original target bytes unchanged. No molecular components, protein examples, measurements or maintained images asserted. |
| plaque-original-2-yaml | reviews/structured/20261022T054304Z-dinoflagellate-cingulum-audit/review.yaml; Historical complete paired observation and deterministic Markdown equivalence | supports | Original qualified verdict, all scientific assessments/evidence scopes and empty findings/actions independently reassessed; original corpus runs remain historical, not current execution. |
| plaque-original-2-md | reviews/structured/20261022T054304Z-dinoflagellate-cingulum-audit/review.md; Historical complete paired observation and deterministic Markdown equivalence | supports | Original qualified verdict, all scientific assessments/evidence scopes and empty findings/actions independently reassessed; original corpus runs remain historical, not current execution. |
| plaque-current-3 | data/structures/other/dinoflagellate_epicone.yaml; Entire maintained record at frozen source dbdd66f36d1363c94eab2c58305c2f58a68baf09 | supports | Complete definition, hierarchy, taxonomic distribution, evidence, graph, discussions and history independently read. Original target bytes unchanged. No molecular components, protein examples, measurements or maintained images asserted. |
| plaque-original-3-yaml | reviews/structured/20261022T054305Z-dinoflagellate-epicone-audit/review.yaml; Historical complete paired observation and deterministic Markdown equivalence | supports | Original qualified verdict, all scientific assessments/evidence scopes and empty findings/actions independently reassessed; original corpus runs remain historical, not current execution. |
| plaque-original-3-md | reviews/structured/20261022T054305Z-dinoflagellate-epicone-audit/review.md; Historical complete paired observation and deterministic Markdown equivalence | supports | Original qualified verdict, all scientific assessments/evidence scopes and empty findings/actions independently reassessed; original corpus runs remain historical, not current execution. |
| plaque-policy | docs/CURATION.md; Frozen local policy/schema applied | supports | Exact structure and mereology, source scope, optional inventory and append-only discussion/history rules. |
| plaque-schema | src/cellstructuremech/schema/cellstructuremech.yaml; Frozen local policy/schema applied | supports | Subcellular region, hierarchy/parthood, descriptive graph, taxonomic presence and evidence semantics. |
| plaque-review-skill | .claude/skills/review-yaml-record/SKILL.md; Frozen local policy/schema applied | supports | Native molecular/pathway structured-source trigger assessed from full record, not mandatory optional fields. |
| plaque-review-profile | docs/record-review-profile.md; Frozen local policy/schema applied | supports | Issue-bearing immutable batch successor; clean scientific observations are not fabricated curation findings. |
| plaque-review-schema | schema/record_review.yaml; Frozen local policy/schema applied | supports | Native evidence kinds/assessment enums and immutable lineage contract. |
| plaque-checklist | .claude/skills/curate-yaml-record/references/review-checklist.md; Frozen local policy/schema applied | supports | Complete field-by-field bounded review; unknown molecular assembly is not automatic defect. |
| plaque-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Frozen local policy/schema applied | supports | NONMECHANISTIC physical/topological graphs need supported exact edges, not invented mechanism. |
| plaque-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097685,GO:0097686,GO:0097611,GO:0097613,GO:0097683,GO:0097614,GO:0097610,GO:0110165; All requested identity/status/definition/synonyms/xrefs and only relevant direct typed children; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-plaque/go.raw | supports | Eight active exact identities, definitions and synonyms agree. Parent children directly expose groove/cingulum is_a surface furrow; epicone is_a cellular anatomical structure; apex/groove part_of epicone; horn is_a apex. No unrelated GO0110165 child is judged. |
| plaque-go-0097685-constraints | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097685/constraints; Focal taxonConstraints and identity only; blacklist entries are not constituent evidence; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-plaque/go-0097685-constraints.raw | supports | Focal only_in_taxon explicitly restricts this structure to NCBITaxon2864 Dinophyceae, without universal presence or a numerical census. Inherited blacklist annotations are not interpreted as structure proteins. |
| plaque-go-0097685-history | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097685/history; Complete focal history array; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-plaque/go-0097685-history.raw | supports | Complete dated term/definition/relation/synonym history supports the current declared relations; uninformative Bad taxon ID rendering does not replace explicit constraints endpoint. |
| plaque-go-0097686-constraints | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097686/constraints; Focal taxonConstraints and identity only; blacklist entries are not constituent evidence; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-plaque/go-0097686-constraints.raw | supports | Focal only_in_taxon explicitly restricts this structure to NCBITaxon2864 Dinophyceae, without universal presence or a numerical census. Inherited blacklist annotations are not interpreted as structure proteins. |
| plaque-go-0097686-history | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097686/history; Complete focal history array; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-plaque/go-0097686-history.raw | supports | Complete dated term/definition/relation/synonym history supports the current declared relations; uninformative Bad taxon ID rendering does not replace explicit constraints endpoint. |
| plaque-go-0097611-constraints | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097611/constraints; Focal taxonConstraints and identity only; blacklist entries are not constituent evidence; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-plaque/go-0097611-constraints.raw | supports | Focal only_in_taxon explicitly restricts this structure to NCBITaxon2864 Dinophyceae, without universal presence or a numerical census. Inherited blacklist annotations are not interpreted as structure proteins. |
| plaque-go-0097611-history | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097611/history; Complete focal history array; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-plaque/go-0097611-history.raw | supports | Complete dated term/definition/relation/synonym history supports the current declared relations; uninformative Bad taxon ID rendering does not replace explicit constraints endpoint. |
| plaque-go-0097613-constraints | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097613/constraints; Focal taxonConstraints and identity only; blacklist entries are not constituent evidence; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-plaque/go-0097613-constraints.raw | supports | Focal only_in_taxon explicitly restricts this structure to NCBITaxon2864 Dinophyceae, without universal presence or a numerical census. Inherited blacklist annotations are not interpreted as structure proteins. |
| plaque-go-0097613-history | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097613/history; Complete focal history array; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-plaque/go-0097613-history.raw | supports | Complete dated term/definition/relation/synonym history supports the current declared relations; uninformative Bad taxon ID rendering does not replace explicit constraints endpoint. |
| plaque-horn-epicone-path | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097686/paths/GO:0097613; Complete one-path two-edge result; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-plaque/horn-epicone-path.raw | supports | The sole exact path is GO0097686 is_a GO0097683 then part_of GO0097613. Horn containment is inherited via the apex; no direct independent GO horn-to-epicone edge is claimed. |
| plaque-tax-2864 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2864; Complete native scientificName/rank/lineage/aliases; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-plaque/tax-2864.raw | supports | Native class2864 is Dinophyceae, with dinoflagellate/Dinophyta aliases and eukaryote/Sar/Alveolata lineage; taxon identity is not prevalence. |
| plaque-tax-77300 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/77300; Complete native species identity/name/lineage/aliases; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-plaque/tax-77300.raw | supports | Native species77300 is Margalefidinium polykrikoides and explicitly retains Cochlodinium polykrikoides synonym; no strain identifier is invented. |
| plaque-iwataki2010-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A20561119+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=5; Exact PMID matched native identity/authors/year/DOI and complete primary abstract; no full Methods/body/images; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-plaque/iwataki2010-meta.raw | supports | Unique MED20561119/DOI10.1111/j.1550-7408.2010.00491.x is Iwataki,Hansen,Moestrup,Matsuoka2010. Complete primary abstract explicitly describes U-shaped groove connected to anterior sulcal extension on dorsal epicone. Flagellar/eyespot results are not promoted to groove-specific constituents. |
| plaque-gomez2017-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.hal.2017.01.008%22&amp;format=json&amp;resultType=core&amp;pageSize=5; Exact DOI query one MED record; identity/authors/year and complete primary abstract; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-plaque/gomez2017-meta.raw | supports | Unique MED28366398/DOI10.1016/j.hal.2017.01.008 is Gomez,Richlen,Anderson2017; complete abstract supports formal Margalefidinium transfer distinct from Iwataki morphology evidence. |
| plaque-taylor1980-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A7002229+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=5; Complete indexed secondary-review abstract and metadata; no article body; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-plaque/taylor1980-meta.raw | context_only | Unique MED7002229/DOI10.1016/0303-2647(80)90006-4 is Taylor1980 On dinoflagellate evolution, Biosystems13:65-108. Secondary review abstract is broad evolutionary synthesis, used for exact bibliography only, not independent detailed horn/cingulum anatomy. |
| plaque-gomez2017-s3 | https://pmc-oa-opendata.s3.amazonaws.com/PMC6276129.1/PMC6276129.1.xml; Front identity/permissions; complete MethodsS3,ResultsS8 includingS9,TaxonomyS10/allnestedsubsections,ConclusionsS30,Table1 andFig3/4/5text captions; no pixels/supplements; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-plaque/gomez2017-s3.raw | supports | Genuine JATS formally diagnoses U-shaped dorsal episomal groove and establishes Margalefidinium polykrikoides from Cochlodinium. Its own Puerto Rico LM did not visualize groove/anterior sulcal extension; SEM details were obscured by filamentous material. These specimens are not substituted for2010 ultrastructure. Figure5 is redrawn morphology; no pixel measurements claimed. |
| plaque-tol-orientation | https://tolweb.org/articles/?article_id=4756; Complete main orientation prose, overview caption, authorship/date/text licence; no pixels; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-plaque/tol-orientation.raw | supports | Hoppenrath2008 expert orientation note distinguishes anterior episome/epicone/epitheca and posterior counterparts relative to cingulum, apex at anterior tip and possible athecate apical groove. Terms are not universally exact synonyms. TextCCBY-NC3.0; image rights are separate and no images used. |
| plaque-tol-dinoflagellates | https://tolweb.org/Dinoflagellates/2445; Introduction and opening Characteristics through Flagella/desmokont exception, associated text captions; later cell biology not relied on; no pixels; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-plaque/tol-dinoflagellates.raw | supports | Expert Characteristics/Flagella account places transverse flagellum in cingulum and longitudinal flagellum in sulcus; desmokont flagellation lacks these grooves. This supports VARIABLE scope, not a universal groove or molecular inventory. |
| plaque-iwataki2010-publisher | https://onlinelibrary.wiley.com/doi/full/10.1111/j.1550-7408.2010.00491.x; HTTP status, response readability and blocked page only; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-plaque/iwataki2010-publisher.raw | context_only | Actual fresh publisher route returnedHTTP403. No article body, Methods, original figure pixels or experimental strain details certified by this response. The corresponding abstract/authority and historical failure remain distinct. |
| plaque-taylor1980-publisher | https://www.sciencedirect.com/science/article/pii/0303264780900064; HTTP status, response readability and blocked page only; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-plaque/taylor1980-publisher.raw | context_only | Actual fresh publisher route returnedHTTP403. No article body, Methods, original figure pixels or experimental strain details certified by this response. The corresponding abstract/authority and historical failure remain distinct. |
| plaque-catalogue | https://imodulondb.org/api/datasets; Complete same-PR fresh official catalogue independently reread; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/catalogue.raw | context_only | Complete20 organism rows/28 organism-dataset pairs independently read; no Dinophyceae/Margalefidinium/Cochlodinium coverage. These records already have genuine morphology-only applicability exclusions. |
| plaque-catalogue-search | https://imodulondb.org/api/datasets; Complete same-PR fresh official catalogue independently reread; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/catalogue.raw | context_only | Bounded catalogue coverage screen has no matching natural host; not biological absence and no unrelated bacterial downstream query. |
| plaque-historical-adapter-unavailable | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Original runner availability receipt only; no fresh invocation | context_only | Historical2026-11-03T00:49Z exit1 PermissionError reading configured pyvenv.cfg; not a current scientific check or completed runner invocation. Fresh source catalogue inspection separately reported. |
| plaque-original-current-validation | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-plaque/originals-current-proof.json; Four original native validate/render pairs;52historical input occurrences;47current source/worktree hashes | supports | All original YAML validates and Markdown renders byte-identically. Historical inputs match their exact source commit, resolving CLAUDE symlink. All four targets are unchanged; no stale science refresh or prior finding disposition required. |
| plaque-historical-failed-access-0 | reviews/structured/20261022T054302Z-dinoflagellate-apical-groove-audit/review.yaml; evidence#root50-iwataki2010-publisher; historical responseSHA 792cc7833ab90870c2e3df1a8ab44e09ea0506fe4fe02c2542d238b991b4eda3; originalaccess 2026-10-22T05:31:12.422043Z | context_only | The immutable original labels a disclosed403response database/context_only. Correct successor classification is validation/context_only; preserve original request/time/failure. Original response bytes are not independently refetched here and later access does not erase historical failure. |
| plaque-historical-failed-access-1 | reviews/structured/20261022T054304Z-dinoflagellate-apical-horn-audit/review.yaml; evidence#root50-taylor1980-publisher; historical responseSHA 14dd40deb21794994e8cbc95036a781eb7e7b41de1fbcc216c4af476bd5948f7; originalaccess 2026-10-21T09:08:56.074246Z | context_only | The immutable original labels a disclosed403response database/context_only. Correct successor classification is validation/context_only; preserve original request/time/failure. Original response bytes are not independently refetched here and later access does not erase historical failure. |
| plaque-historical-failed-access-2 | reviews/structured/20261022T054304Z-dinoflagellate-cingulum-audit/review.yaml; evidence#root50-taylor1980-publisher; historical responseSHA 14dd40deb21794994e8cbc95036a781eb7e7b41de1fbcc216c4af476bd5948f7; originalaccess 2026-10-21T09:08:56.074246Z | context_only | The immutable original labels a disclosed403response database/context_only. Correct successor classification is validation/context_only; preserve original request/time/failure. Original response bytes are not independently refetched here and later access does not erase historical failure. |
| plaque-native-dinoflagellate_apical_groove-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_apical_groove-uniprot-verify-receipt.json; Actual ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/dinoflagellate_apical_groove.yaml', '--verify']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_apical_groove-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual current-source command exit0; zero protein_examples and zero typedGENE_OR_PROTEINnodes independently confirmed. Empty-inventory success does not certify molecular completeness. |
| plaque-native-dinoflagellate_apical_groove-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_apical_groove-uniprot-causal-receipt.json; Actual ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/dinoflagellate_apical_groove.yaml', '--causal-graphs']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_apical_groove-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Actual current-source command exit0; zero protein_examples and zero typedGENE_OR_PROTEINnodes independently confirmed. Empty-inventory success does not certify molecular completeness. |
| plaque-native-dinoflagellate_apical_horn-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_apical_horn-uniprot-verify-receipt.json; Actual ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/dinoflagellate_apical_horn.yaml', '--verify']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_apical_horn-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual current-source command exit0; zero protein_examples and zero typedGENE_OR_PROTEINnodes independently confirmed. Empty-inventory success does not certify molecular completeness. |
| plaque-native-dinoflagellate_apical_horn-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_apical_horn-uniprot-causal-receipt.json; Actual ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/dinoflagellate_apical_horn.yaml', '--causal-graphs']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_apical_horn-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Actual current-source command exit0; zero protein_examples and zero typedGENE_OR_PROTEINnodes independently confirmed. Empty-inventory success does not certify molecular completeness. |
| plaque-native-dinoflagellate_cingulum-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_cingulum-uniprot-verify-receipt.json; Actual ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/dinoflagellate_cingulum.yaml', '--verify']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_cingulum-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual current-source command exit0; zero protein_examples and zero typedGENE_OR_PROTEINnodes independently confirmed. Empty-inventory success does not certify molecular completeness. |
| plaque-native-dinoflagellate_cingulum-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_cingulum-uniprot-causal-receipt.json; Actual ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/dinoflagellate_cingulum.yaml', '--causal-graphs']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_cingulum-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Actual current-source command exit0; zero protein_examples and zero typedGENE_OR_PROTEINnodes independently confirmed. Empty-inventory success does not certify molecular completeness. |
| plaque-native-dinoflagellate_epicone-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_epicone-uniprot-verify-receipt.json; Actual ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/dinoflagellate_epicone.yaml', '--verify']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_epicone-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual current-source command exit0; zero protein_examples and zero typedGENE_OR_PROTEINnodes independently confirmed. Empty-inventory success does not certify molecular completeness. |
| plaque-native-dinoflagellate_epicone-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_epicone-uniprot-causal-receipt.json; Actual ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/dinoflagellate_epicone.yaml', '--causal-graphs']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_epicone-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Actual current-source command exit0; zero protein_examples and zero typedGENE_OR_PROTEINnodes independently confirmed. Empty-inventory success does not certify molecular completeness. |
| septin-review-policy | .claude/skills/review-yaml-record/SKILL.md; Full-record evidence and structured-source trigger | supports | Actual positive molecular/pathway claims trigger structured-source coverage; genuine physical morphology with no such assertions can be excluded. Empty optional inventories do not establish defects. |
| septin-curation-policy | docs/CURATION.md; Exact identity, source scope and append-only Discussions | supports | Preserve dated rationale/history. Source-specific evidence supports its narrow claim; optional components, images or numerical properties are not mandatory fill targets. |
| septin-schema-policy | src/cellstructuremech/schema/cellstructuremech.yaml; Identity, synonym, PresenceEnum, graph and optional component fields | supports | SUBCELLULAR_REGION and OTHER permit these anatomical entities. VARIABLE is not universal presence; descriptive FUNCTION/NONMECHANISTIC does not establish formation necessity. |
| septin-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Edge evidence, boundaries and descriptive scope | supports | Exact class, parthood and spatial relations must remain distinct. A morphology graph may deliberately exclude molecular mechanism without a missing-step defect. |
| septin-literature-policy | .claude/skills/literature-evidence/SKILL.md; Source access and actual read tiers | supports | Metadata/abstract, authored authority text, complete primary bodies, captions/pixels and failed retrievals are distinct evidence scopes. |
| septin-review-schema | schema/record_review.yaml; ReviewEvidence kinds and finding lineage | supports | Failed HTTP access is validation context, not database scientific content. Exact predecessor references retain repository, review_id and finding_id. |
| septin-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097614,GO:0097618,GO:0097612,GO:0097684,GO:0097611,GO:0097613,GO:0097610,GO:0110165; All eight requested active IDs/names/definitions/xrefs/synonyms/comments and relevant typed child links; not all unrelated GO0110165 descendants | supports | GO0097614 is the posterior hypocone; GO0097618 is the antapex-reaching, bilobed-hypocone sulcus subtype; GO0097612 is the ventral furrow partially housing the longitudinal flagellum and intersecting the cingulum. Typed parents and antapex parthood match. Sulcus definition.xrefs cites PMID20561119, notch cites PMID7002229. GO0097684 retains anterior wording in conflict with the posterior notch definition and expert orientation; this error is not copied into the three targets. |
| septin-go-0097614-history | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097614/history; Complete current term/history array, including direct RELATION and DEFINITION events | supports | History confirms replacement of obsolete cell-part parent by GO0110165 in2019, posterior definition and related hyposome/hypotheca synonyms. Historical Bad taxon ID display entries are not treated as current taxonomic constraints or scientific refutation. |
| septin-go-0097614-constraints | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097614/constraints; Exact current taxonConstraints entry; unrelated inherited protein-annotation blacklist not used | supports | Exact term only_in_taxon NCBITaxon2864 Dinophyceae. This restriction identifies allowed host lineage, not a class-wide prevalence measurement or a localized protein inventory. |
| septin-go-0097618-history | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097618/history; Complete current term/history array, including direct RELATION and DEFINITION events | supports | History confirms direct is_a GO0097612 and posterior-reaching/bilobed morphology. Historical Bad taxon ID display entries are not treated as current taxonomic constraints or scientific refutation. |
| septin-go-0097618-constraints | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097618/constraints; Exact current taxonConstraints entry; unrelated inherited protein-annotation blacklist not used | supports | Exact term only_in_taxon NCBITaxon2864 Dinophyceae. This restriction identifies allowed host lineage, not a class-wide prevalence measurement or a localized protein inventory. |
| septin-go-0097612-history | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097612/history; Complete current term/history array, including direct RELATION and DEFINITION events | supports | History confirms direct is_a GO0097610 and ventral flagellum-housing/intersecting definition. Historical Bad taxon ID display entries are not treated as current taxonomic constraints or scientific refutation. |
| septin-go-0097612-constraints | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097612/constraints; Exact current taxonConstraints entry; unrelated inherited protein-annotation blacklist not used | supports | Exact term only_in_taxon NCBITaxon2864 Dinophyceae. This restriction identifies allowed host lineage, not a class-wide prevalence measurement or a localized protein inventory. |
| septin-tax-2864 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2864; Complete native taxId/scientificName/rank/lineage/otherNames response, independently read from fresh peer packet | supports | ENA2864 is class Dinophyceae with dinoflagellate common name and Dinophyta/Dinoflagellata aliases. Identity and rank verified; no numerical frequency inferred. |
| septin-tol-orientation | https://tolweb.org/articles/?article_id=4756; Complete authored main text, overview caption and About This Page attribution/text licence; no image pixels | supports | Mona Hoppenrath2008 divides the motile cell at the cingulum into upper episome and lower hyposome; hypocone is athecate and hypotheca thecate terminology. Antapex is the bottom of the hyposome; below-cingulum is posterior; sulcus side is ventral. Expert secondary terminology, not a new formation experiment. Text CC-BY-NC3.0 does not confer identical rights on each image; no images reused. |
| septin-tol-dinoflagellates | https://tolweb.org/Dinoflagellates/2445; Authorship, Introduction morphology diversity, Characteristics opening and complete Flagella subsection with Figs1–8 captions; later biological sections not used for target assertions; no pixels | supports | Hoppenrath/Saldarriaga state that the longitudinal flagellum lies in the sulcus while its distal portion projects behind the cell; desmokont Prorocentrum flagella are not groove-associated. Supports qualified anatomical occurrence, not universal prevalence or a constituent/formation assay. Broad whole-cell molecular claims elsewhere on the page are not imported into these regional records. |
| septin-taylor1980-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A7002229+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=5; Unique MED title/authors/year/DOI/access-route flags and complete abstractText; fresh peer receipt independently read | supports | Taylor FJ1980, On dinoflagellate evolution, Biosystems13:65–108, DOI10.1016/0303-2647(80)90006-4, is a secondary review. Complete abstract is broad evolutionary synthesis, not a direct generic-notch experiment. This verifies current bibliography, not every attached anatomical claim or historical retrieval. |
| septin-iwataki2010-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A20561119+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=5; Unique MED title/authors/year/DOI/access-route flags and complete abstractText; fresh peer receipt independently read | supports | Iwataki,Hansen,Moestrup,Matsuoka2010, DOI10.1111/j.1550-7408.2010.00491.x, concerns Cochlodinium polykrikoides ultrastructure. Complete primary-paper abstract describes species-specific groove/flagellar architecture; no inspected body, Methods strain or figures, and no class-wide extrapolation. This verifies current bibliography, not every attached anatomical claim or historical retrieval. |
| septin-taylor1980-publisher | https://www.sciencedirect.com/science/article/pii/0303264780900064; Current HTTP403 response and visible error/challenge text, independently inspected | context_only | Current route did not supply an article body. The actual current receipt is separate from October failures; no universal claim that a body is unavailable everywhere, and no primary scientific conclusion from the error page. |
| septin-iwataki2010-publisher | https://onlinelibrary.wiley.com/doi/full/10.1111/j.1550-7408.2010.00491.x; Current HTTP403 response and visible error/challenge text, independently inspected | context_only | Current route did not supply an article body. The actual current receipt is separate from October failures; no universal claim that a body is unavailable everywhere, and no primary scientific conclusion from the error page. |
| septin-catalogue | https://imodulondb.org/api/datasets; Complete fresh official20-organism catalogue and all dataset keys, independently read from micro reviewer packet | supports | Finite current response contains no Dinophyceae/dinoflagellate host. These three records are already genuinely morphology-only, so no downstream gene/module query is indicated; unrelated bacterial taxa are not proxies. Noncoverage is not biological absence. |
| septin-adapter-runner-historical | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Actual prior command receipt and unavailable reason | context_only | Historical runner attempt exited1 on PermissionError reading pyvenv.cfg at Nov3 00:49Z; no new invocation. Current catalogue read is a separate official source fallback, not runner execution. |
| septin-original-native-checks | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-septin/original-checks.json; Actual three original native validate/render runs and all45 historical input occurrences | supports | All three pairs validate exit0 and render byte-identically; all45 manifested historical inputs match git revision f97b1abe2d78971b6f66b9083087d7a94cf3c0cc, and all three current target hashes equal their old inputs. Historical batch26 global executions are explicitly scoped to that old source, not claimed as current tests. |
| septin-record-dinoflagellate_hypocone | data/structures/other/dinoflagellate_hypocone.yaml; Entire current maintained YAML: definitions,synonyms,taxonomy,evidence,all graph nodes/edges,discussions/history | context_only | Complete nonstale record read at the frozen source; morphology/topology only. Exact authoritative anatomy and current bibliographic claims are assessed separately from retained historical rationale. |
| septin-original-dinoflagellate_hypocone | reviews/structured/20261022T054306Z-dinoflagellate-hypocone-audit/review.yaml; Entire immutable original YAML and deterministic Markdown pair | context_only | Original pass_with_limitations with 0 finding(s), exact predecessor scope and prose applicability note independently reviewed. Old global batch26 execution provenance is legitimate historical reuse, not a mislabeled current execution. |
| septin-native-dinoflagellate_hypocone-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dinoflagellate_hypocone.yaml --verify; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_hypocone-uniprot-verify-receipt.json; receiptSHA256 41a0294e458b62ef551fae0493442c0a6f3cc61e44ea0e41128279abaa36cc68; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_hypocone-uniprot-verify.log | supports | Actual command exit0. Actual maintained inventory0 protein examples/0 typed GENE_OR_PROTEIN nodes. Empty-scope native success is not positive biological member, formation or localization coverage. |
| septin-native-dinoflagellate_hypocone-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dinoflagellate_hypocone.yaml --causal-graphs; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_hypocone-uniprot-causal-receipt.json; receiptSHA256 510c50f43effb11b15d2b68ce3e717e5a7edbcef5175a38ae560568743fec6d6; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_hypocone-uniprot-causal.log | supports | Actual command exit0. Actual maintained inventory0 protein examples/0 typed GENE_OR_PROTEIN nodes. Empty-scope native success is not positive biological member, formation or localization coverage. |
| septin-record-dinoflagellate_sulcal_notch | data/structures/other/dinoflagellate_sulcal_notch.yaml; Entire current maintained YAML: definitions,synonyms,taxonomy,evidence,all graph nodes/edges,discussions/history | context_only | Complete nonstale record read at the frozen source; morphology/topology only. Exact authoritative anatomy and current bibliographic claims are assessed separately from retained historical rationale. |
| septin-original-dinoflagellate_sulcal_notch | reviews/structured/20261022T054307Z-dinoflagellate-sulcal-notch-audit/review.yaml; Entire immutable original YAML and deterministic Markdown pair | context_only | Original pass_with_limitations with 0 finding(s), exact predecessor scope and prose applicability note independently reviewed. Old global batch26 execution provenance is legitimate historical reuse, not a mislabeled current execution. |
| septin-native-dinoflagellate_sulcal_notch-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dinoflagellate_sulcal_notch.yaml --verify; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_sulcal_notch-uniprot-verify-receipt.json; receiptSHA256 d1ee6a2a01c7ddf32addba78ed57820876f551150f91a3804a20bc8acfaecd75; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_sulcal_notch-uniprot-verify.log | supports | Actual command exit0. Actual maintained inventory0 protein examples/0 typed GENE_OR_PROTEIN nodes. Empty-scope native success is not positive biological member, formation or localization coverage. |
| septin-native-dinoflagellate_sulcal_notch-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dinoflagellate_sulcal_notch.yaml --causal-graphs; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_sulcal_notch-uniprot-causal-receipt.json; receiptSHA256 752ff55254e0b76729df47cd558f3fb28138a31d997faf1be9abfe3fd9faa331; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_sulcal_notch-uniprot-causal.log | supports | Actual command exit0. Actual maintained inventory0 protein examples/0 typed GENE_OR_PROTEIN nodes. Empty-scope native success is not positive biological member, formation or localization coverage. |
| septin-historical-failed-access-dinoflagellate_sulcal_notch | reviews/structured/20261022T054307Z-dinoflagellate-sulcal-notch-audit/review.yaml#micro50-taylor1980-publisher; Retained original evidence row; quoted historical access timestamp/hash, not a fresh raw re-fetch | context_only | Original historical HTTP403 observation was explicitly context_only and said no body. Reclassify only database→validation in the successor; retain actual Oct21 date and original snapshot 14dd40deb21794994e8cbc95036a781eb7e7b41de1fbcc216c4af476bd5948f7. No allegation of falsely claiming body access. |
| septin-record-dinoflagellate_sulcus | data/structures/other/dinoflagellate_sulcus.yaml; Entire current maintained YAML: definitions,synonyms,taxonomy,evidence,all graph nodes/edges,discussions/history | context_only | Complete nonstale record read at the frozen source; morphology/topology only. Exact authoritative anatomy and current bibliographic claims are assessed separately from retained historical rationale. |
| septin-original-dinoflagellate_sulcus | reviews/structured/20261022T054307Z-dinoflagellate-sulcus-audit/review.yaml; Entire immutable original YAML and deterministic Markdown pair | context_only | Original needs_curation with 1 finding(s), exact predecessor scope and prose applicability note independently reviewed. Old global batch26 execution provenance is legitimate historical reuse, not a mislabeled current execution. |
| septin-native-dinoflagellate_sulcus-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dinoflagellate_sulcus.yaml --verify; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_sulcus-uniprot-verify-receipt.json; receiptSHA256 80ab921dce57a64a64d9e5447af652aa02ec8a335b842dd69c2f16bbab869221; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_sulcus-uniprot-verify.log | supports | Actual command exit0. Actual maintained inventory0 protein examples/0 typed GENE_OR_PROTEIN nodes. Empty-scope native success is not positive biological member, formation or localization coverage. |
| septin-native-dinoflagellate_sulcus-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dinoflagellate_sulcus.yaml --causal-graphs; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_sulcus-uniprot-causal-receipt.json; receiptSHA256 7d998cd21185ec3efc47c396030e3c029a33adf3ebbad077659dc21b09f566ee; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_sulcus-uniprot-causal.log | supports | Actual command exit0. Actual maintained inventory0 protein examples/0 typed GENE_OR_PROTEIN nodes. Empty-scope native success is not positive biological member, formation or localization coverage. |
| septin-historical-failed-access-dinoflagellate_sulcus | reviews/structured/20261022T054307Z-dinoflagellate-sulcus-audit/review.yaml#micro50-taylor1980-publisher; Retained original evidence row; quoted historical access timestamp/hash, not a fresh raw re-fetch | context_only | Original historical HTTP403 observation was explicitly context_only and said no body. Reclassify only database→validation in the successor; retain actual Oct21 date and original snapshot 14dd40deb21794994e8cbc95036a781eb7e7b41de1fbcc216c4af476bd5948f7. No allegation of falsely claiming body access. |
| check-qc | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/qc.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| check-labels | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/labels.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| check-trait-links | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/trait-links.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Native TraitMech link check passed. |
| check-vendored | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/vendored.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Pinned governed files match; native vendored check passed. |
| check-curies | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/curies.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| focused | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/focused-results.json; All twenty actual target schema/strict command outputs | supports | Ten schema and ten strict commands returned exit zero. |
| supplemental-pmid | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/pmid-chunks-receipt.json; Complete native-report PMID set checked with unchanged resolver in batches of at most fifty | supports | 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers remain unverified. |
| historical-adapter-runner-availability | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical runner invocation receipt; exact retained SHA256 reverified during PR2387 synthesis | context_only | Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS PermissionError reading the configured runner pyvenv.cfg. This is retained historical availability evidence, not a fresh attempt or a scientific validation failure. Native policy permits inspected source-catalogue fallback. |
| root-native-dinoflagellate_apical_groove-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_apical_groove-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dinoflagellate_apical_groove-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_apical_groove-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dinoflagellate_apical_horn-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_apical_horn-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dinoflagellate_apical_horn-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_apical_horn-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dinoflagellate_cingulum-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_cingulum-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dinoflagellate_cingulum-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_cingulum-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dinoflagellate_epicone-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_epicone-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dinoflagellate_epicone-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_epicone-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dinoflagellate_hypocone-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_hypocone-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dinoflagellate_hypocone-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_hypocone-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dinoflagellate_sulcal_notch-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_sulcal_notch-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dinoflagellate_sulcal_notch-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_sulcal_notch-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dinoflagellate_sulcus-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_sulcus-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dinoflagellate_sulcus-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_sulcus-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dna_gyrase_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dna_gyrase_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dna_gyrase_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dna_gyrase_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dna_polymerase_iii_beta_sliding_clamp_processivity_factor_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dna_polymerase_iii_beta_sliding_clamp_processivity_factor_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dna_polymerase_iii_beta_sliding_clamp_processivity_factor_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dna_polymerase_iii_beta_sliding_clamp_processivity_factor_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dna_polymerase_iii_clamp_loader_chi_psi_subcomplex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dna_polymerase_iii_clamp_loader_chi_psi_subcomplex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 2 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dna_polymerase_iii_clamp_loader_chi_psi_subcomplex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dna_polymerase_iii_clamp_loader_chi_psi_subcomplex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 2 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |

## Limits And Additional Notes

- Gyrase, beta clamp and chi/psi independent review: Only gyrase, beta clamp and chi/psi are scientifically judged by this slice. Other seven targets and neighboring/group/category issues are not disposed. All records, originals, Git and GitHub remain unchanged.
- Gyrase, beta clamp and chi/psi independent review: Gyrase2019 genuine JATS read only at the declared Introduction/Results/Discussion/Methods and text captions. No figure pixels, raw coordinates, supplements or complete catalytic-cycle reanalysis. RCSB sample sequences/entity mapping are distinct from incomplete modeled coordinates; K12 source differs from BL21(DE3) expression.
- Gyrase, beta clamp and chi/psi independent review: Kong1992 genuine author PDF read at declared pp425,427,432–434 passages/text captions only; no pixels or complete-paper certification. Central DNA fit is modeled, not an observed DNA co-crystal. Archaeal PCNA Matsumiya2001 is full primary abstract/native authority only, not body.
- Gyrase, beta clamp and chi/psi independent review: XiaoIII/IV current full primary abstracts are read; publisher bodies returned403. Olson1995 main pp29570–29576 text/Methods/Results/Discussion/tables/captions were read, not raw figures. Its artificial-operon MC1061 and purified-assay scope does not establish universal native essentiality or an SSB contact measurement.
- Gyrase, beta clamp and chi/psi independent review: McHenry2003 is a secondary-review abstract only. GO/UniProt/InterPro reference annotations and exact identifiers are not newly verified primary experiments for all linked papers. Historical generic functional descriptions and AI-generated dataset prose are not promoted to primary biology.
- Gyrase, beta clamp and chi/psi independent review: GO0044775 genuinely contains the disputed cross-class definition and O73947 xref. This is an upstream scientific scope conflict, not a local misquotation; retain exact structure identity and E.coli examples. Native beta* isoform notes prevent an invented invariant dimer claim for every DnaN-derived product.
- Gyrase, beta clamp and chi/psi independent review: Fresh five-strain precise1k dataset is not exact experimental BL21(DE3)/MC1061 coverage. Seven exact native loci each return201 module rows; only holD exceeds module145 threshold, independently matched to its70-gene list. Threshold-negative results are not gene absence or dispensability; the hit does not establish physical association, direct regulation, formation or localization. AI module summary and activity stories excluded.
- Gyrase, beta clamp and chi/psi independent review: Historical runner unavailable/exit1 is dated2026-11-03T00:49:00Z, not a fresh invocation. Six own native protein commands are actual source-head receipts:5reviewed examples,5COVERED plus2 external UNANCHORED_WITH_UNIPROT typed actors. No false all-covered or full biological validation claim.
- Gyrase, beta clamp and chi/psi independent review: All four inherited findings remain open with exact predecessor identities. Current family-grounding actions preserve dated rationale/history and correct current mapping separately. No new scientific finding, compulsory optional example, new experiment or universal formation classification is proposed.
- Gyrase, beta clamp and chi/psi independent review: Root owns global QC, later saved-head gates, CI and queue. These later stages are not certified by this source report; source-access failures are contextual diagnostics, not scientific refutations.
- Apical groove, horn, cingulum and epicone independent review: Iwataki2010 remains complete primary abstract/metadata only after fresh Wiley403. No original2010microscopy pixels, fullMethods, experimental strain or supplementary movies are certified.
- Apical groove, horn, cingulum and epicone independent review: Gomez2017 genuine fresh JATS was read only at the declaredMethodsS3/ResultsS8includingS9/TaxonomyS10/ConclusionsS30/Table1/Fig3–5textcaptions. No figure pixels, all-figure review, phylogenetic reanalysis or supplements. Formal U-shaped diagnosis is distinguished from its own unreadable groove inLM/obscuredSEM.
- Apical groove, horn, cingulum and epicone independent review: Taylor1980 is a secondary-review complete indexedabstract/metadata tier; freshSD403 supplies no body. No detailed anatomy or experiments are inferred from its title/abstract alone.
- Apical groove, horn, cingulum and epicone independent review: ToL is authored expert secondary terminology, not a primary assembly experiment; exactmainorientation and relevantflagellarscope read. Textlicence does not establish image rights; no images downloaded for reuse or judged as pixels.
- Apical groove, horn, cingulum and epicone independent review: All four records are physical morphological regions with no molecular inventories, images or quantities. Zero native proteinexamples/nodes is an empty-inventory pass, not proof of absent proteins or molecular completeness. Unknown formation necessity and optionalfields are not findings.
- Apical groove, horn, cingulum and epicone independent review: Direct ontology relations are distinguished from inheritedhorn→apex→epicone containment. Epicone has_part is descriptive scope, not universal apicalgroove prevalence. Dinophyceaeonly_in_taxon/VARIABLE and speciesdiagnosis do not certify a taxon-wide numerical census.
- Apical groove, horn, cingulum and epicone independent review: All four structured-source exclusions are genuinely morphology-only; freshcompletecatalogue also lacks naturalhostcoverage. No downstream bacterialproxyquery or negative biological inference. Historicalrunnerfailure remains2026-11-03T00:49Z, not a freshinvocation.
- Apical groove, horn, cingulum and epicone independent review: Four originalpairs/52historicalinputoccurrences/47currentinputhashes verified; all fourtargetsunchanged. Original corpus checks remain historical. Parent owns currentglobalQC, post-save/finalhead/CI/queue/merge gates; none precertified here.
- Apical groove, horn, cingulum and epicone independent review: No original scientific findings/actions or new recordcuration findings in this slice. Three historicalfailed-accesskind occurrences require successorcorrection; originalfiles stayimmutable. No neighboring/group/category issue disposition inferred.
- Hypocone, sulcal notch and sulcus independent review: All three targets are unchanged from original frozen bytes. One inherited minor sulcus bibliography finding remains open; hypocone and sulcal notch retain qualified positive scientific assessments. No new scientific finding or neighbor disposition.
- Hypocone, sulcal notch and sulcus independent review: Current morphology is supported by exact GO authority and directly inspected authored expert terminology. Taylor1980 secondary review and Iwataki2010 primary paper were read only at complete native abstract/metadata tier; current403 publisher responses are validation context, not scientific bodies. Iwataki is species-specific Cochlodinium polykrikoides evidence, not a class-wide experiment. No Methods strain,paper figures,supplements or microscopy pixels inspected.
- Hypocone, sulcal notch and sulcus independent review: Current GO0097684 anterior wording conflicts with posterior antapex in GO0097618 and expert orientation. The assigned targets use the correct supported posterior orientation; no neighboring record repair or universal endorsement of every ontology sentence is claimed.
- Hypocone, sulcal notch and sulcus independent review: No localized constituent inventory, molecular formation requirement, quantitative prevalence census or physical dimension established. Three records have0examples/0typedprotein nodes; six native successes reflect empty scope. Optional fields are not automatic findings.
- Hypocone, sulcal notch and sulcus independent review: Three original physical/morphology prose exclusions are legitimate. Official catalogue complete20organism response has no Dinophyceae match; no unrelated host proxy, downstream module query or biological absence inference. Historical runner receipt remains Nov3 00:49Z unavailable; no new runner invocation.
- Hypocone, sulcal notch and sulcus independent review: Two original micro50-taylor1980-publisher rows need kind-only database→validation correction; both already stated HTTP403/context_only/no body. Their original timestamps and bundle bytes remain preserved; current publisher failures are separate observations.
- Hypocone, sulcal notch and sulcus independent review: All45 original historical input occurrences and three native YAML/Markdown pairs verified. Historical batch26 global gate execution was explicitly reused at the old shared base and is not a provenance defect or a new-head success claim. Root current global gates, saved-head check, CI,queue,merge and deletion are separate attestations.
- Hypocone, sulcal notch and sulcus independent review: Initial scratch HTML extraction was corrected for unavailable bs4 and actual Latin-1 encoding, without repository edits or scientific source substitution. Source packets are external scratch; no additional maintained context outside the26 listed inputs was used.
- Historical observations remain immutable; their old checks are not represented as current-head execution.
- The adapter runner was not rerun after the canary established OS access failure. Catalogue-based coverage is assessed directly; fresh and reused responses retain actual access timestamps.
- Native label checks include 923 no-adapter skips. Native identifier checks include 909 PMID transport failures and 254 skipped identifiers; bounded supplemental checks independently resolve the 909 PMIDs.
- Scientific record-curation findings stay in separate issues; no record is edited by this review PR.
- Final trusted-base post-save review-check, exact-head independent acceptance, final-head CI and merge-group CI occur after saving this immutable observation and are not represented here as already completed.
- This ten-record successor preserves all 20 original artifacts and exact predecessor finding lineage. Bundle issues #2912, #2913 and #2914 cover one stale target, three formal applicability exclusions and seven failed-access kind occurrences.
- DNA gyrase current changes add only history and InterPro groundings to two existing component_ref graph nodes. Those family identities and their graph usage are reassessed separately from the original deposition-scope finding.
- The native inventory contains five component protein examples and seven typed GENE_OR_PROTEIN nodes: five COVERED and two UNANCHORED_WITH_UNIPROT contextual DnaX/SSB nodes. The latter are contextual partners rather than missing chi/psi constituents. Seven morphology records have zero protein examples and zero typed protein nodes; their zero-exit checks do not imply experimental constituent coverage.
- All historical failed publisher responses already disclose HTTP403 and context_only support. Their successor classification is validation; no successful article-body access is retroactively claimed. Fresh, retained and unavailable source tiers keep their actual timestamps and inspection scopes.
- Record curation remains separate, preserving dated rationale and history with appended clarification where needed. This review-only PR edits no records. Final post-save validation, saved-head independent acceptance, final-head CI and merge-group CI are later gates.
- Current GO source wording is not assumed infallible: the beta-clamp finding explicitly preserves the faithful upstream quotation while distinguishing bacterial DnaN from archaeal/eukaryotic PCNA. Correct E. coli dimer evidence is retained without claiming invariant oligomerization of every derived isoform.
- Sulcus current GO definition xrefs identify Iwataki2010 PMID20561119, whereas the neighboring notch cites Taylor1980 PMID7002229. The finding corrects only the sulcus attribution and does not claim that Taylor lacks sulcus content or that historical failed-access statements are false.
- Gomez2017 supports the formal Margalefidinium name transfer; its own light-microscopy observations did not resolve the groove and its SEM details were obscured. Iwataki2010 primary abstract separately supports the dorsal U-shaped groove. Text/caption inspection is not microscopy-pixel inspection.
- Full local QC, all 20 focused schema/strict checks and all 20 native protein checks passed before saving. Existing #2514 retains the native bulk-PMID reporting limitation; unchanged resolver requests bounded to at most 50 verified all 909 affected PMIDs, without changing the original report or cache.
- Gyrase sources distinguish closed cleavage-domain deposition 6RKU from overall model 6RKW, while retaining correct GyrA/GyrB identity, K-12 source, 2:2 protein counts and BL21(DE3) expression limits. Full sample sequences are not complete modeled coordinates. Chi/psi 1:1 membership, psi-to-gamma and assembled dimer-to-tau/gamma assays remain separately scoped; SSB bridge authority is not attributed to the Olson purified-binding assay.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261104T053833Z-pr2387-current-record-followup
kind: batch
repository: CultureBotAI/CellStructureMech
title: 'PR 2387: current-input review of ten records and adversarial follow-up'
started_at: '2026-11-04T05:27:06.673128Z'
finished_at: '2026-11-04T05:38:33Z'
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
summary: 'Current-input successor for all ten PR2387 records. DNA gyrase was stale
  and substantively refreshed: its two new graph-node family groundings are supported,
  while its deposition-scope finding remains open. All five inherited scientific findings
  persist across four records (one major, four minor); six morphology records retain
  qualified positive outcomes. Three formal expression-only applicability exclusions
  and seven failed-access evidence-kind occurrences are corrected, while all seven
  genuine morphology-only exclusions remain justified. All 20 original artifacts remain
  immutable; only this linked review pair is added.'
source:
  git_revision: dbdd66f36d1363c94eab2c58305c2f58a68baf09
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
  - path: data/structures/other/dinoflagellate_apical_groove.yaml
    sha256: 7577f4358ce9bcc9753ec38e0295a7e496261827869f77353480ef2b130ad1f4
    role: target
  - path: data/structures/other/dinoflagellate_apical_horn.yaml
    sha256: 77b2ec19b71236a91786a44611abcc34eb6a7e927763f6ff641f2c879813c344
    role: target
  - path: data/structures/other/dinoflagellate_cingulum.yaml
    sha256: c29822ebb0e810421c4516a4db5b8e6d648739e5c563e491d584850a65011513
    role: target
  - path: data/structures/other/dinoflagellate_epicone.yaml
    sha256: 30e41a70bae04d4698b3b0bc40226fb51727a9f8664c4031c3ae8145216dfcdd
    role: target
  - path: data/structures/other/dinoflagellate_hypocone.yaml
    sha256: 0a596b02f63ce6799d10b49b4cf34a921fb2ae92e1208ee599a96ed47c5f40a1
    role: target
  - path: data/structures/other/dinoflagellate_sulcal_notch.yaml
    sha256: 0e3dace360a1a70bc43f318649972ebb63a50628897c7681bb81c9c75f18c7b1
    role: target
  - path: data/structures/other/dinoflagellate_sulcus.yaml
    sha256: b3606a5c03fbc85a602f3ea6927c22e49eedbcd00d1e9607c85ac080205bd356
    role: target
  - path: data/structures/other/dna_gyrase_complex.yaml
    sha256: 5e7e1a94281ec5bb4c72ea205e6e44bc4545175d4051eab98df531f709ac35b8
    role: target
  - path: data/structures/other/dna_polymerase_iii_beta_sliding_clamp_processivity_factor_complex.yaml
    sha256: 0369f6dedbb1719e899d2bc9895033ab1dc7652865adb0597e10901b4e5ce664
    role: target
  - path: data/structures/other/dna_polymerase_iii_clamp_loader_chi_psi_subcomplex.yaml
    sha256: ae7299b0c7b889f3f035fe582e2b6c8fddb1a507dd0e1ceadda8c1d8e73a60cb
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
  - path: reviews/structured/20261022T054302Z-dinoflagellate-apical-groove-audit/review.md
    sha256: 85ad2cd90c206a93f1a5e75373e6696d81e3ffdcdca0f14040dec36cad44ac71
    role: context
  - path: reviews/structured/20261022T054302Z-dinoflagellate-apical-groove-audit/review.yaml
    sha256: f605131be90cc3b54b26cfafe3e17d6268979c5937a227f25411cfdf18e25971
    role: context
  - path: reviews/structured/20261022T054304Z-dinoflagellate-apical-horn-audit/review.md
    sha256: e145632bb665547354f060e0b589d40245ae9127757a69b1e3c45dece0e03c0b
    role: context
  - path: reviews/structured/20261022T054304Z-dinoflagellate-apical-horn-audit/review.yaml
    sha256: f6ee1ed0e9d0154aa075463a0c6b5407216fc6b6d595cf5c87d47aa15073e6fe
    role: context
  - path: reviews/structured/20261022T054304Z-dinoflagellate-cingulum-audit/review.md
    sha256: a7f33b7eaf4fbf0fe6e356d789dd3cc7bfa72ef343d3c808afb98507e70f81fc
    role: context
  - path: reviews/structured/20261022T054304Z-dinoflagellate-cingulum-audit/review.yaml
    sha256: 9f2327be51767cbf946ef143bdace86d855ba02f5ec8e15df34dc62440399d7f
    role: context
  - path: reviews/structured/20261022T054305Z-dinoflagellate-epicone-audit/review.md
    sha256: 711b0594884de3b37bcc47f35e8e2539c0c8e0ef7368d61c8189cbc5f87d7535
    role: context
  - path: reviews/structured/20261022T054305Z-dinoflagellate-epicone-audit/review.yaml
    sha256: 6d966b5dd38100535f6632d4ac31fd436f690a2b0d0acca9f7c1d6466fa88579
    role: context
  - path: reviews/structured/20261022T054306Z-dinoflagellate-hypocone-audit/review.md
    sha256: 5a2381e7f988cd5b20fa2c917fc30462ff7f5f7344155876680c9fe2a3fe8771
    role: context
  - path: reviews/structured/20261022T054306Z-dinoflagellate-hypocone-audit/review.yaml
    sha256: 9808828a60ce9d3accad23938b10e300ecda029aeb6a2822448eb1e32734acee
    role: context
  - path: reviews/structured/20261022T054307Z-dinoflagellate-sulcal-notch-audit/review.md
    sha256: a43ffdd5f10ab7eaea6bdeef1fa38e15a7af7b89eb8c641d1765ff24e74b6acc
    role: context
  - path: reviews/structured/20261022T054307Z-dinoflagellate-sulcal-notch-audit/review.yaml
    sha256: 599567d90a1060af4e54f540be250d609a9ce6ea8092f826317f4bb31a75f4e7
    role: context
  - path: reviews/structured/20261022T054307Z-dinoflagellate-sulcus-audit/review.md
    sha256: f428003c8dc33153c7c9cbbeaa5163599d20acba466d55f462e7e8c716dd9d9e
    role: context
  - path: reviews/structured/20261022T054307Z-dinoflagellate-sulcus-audit/review.yaml
    sha256: 92ecf76bae282ad0410728eee21b4fcac7653e0d76c1544fca4d05d7dc8acd49
    role: context
  - path: reviews/structured/20261022T054333Z-dna-gyrase-complex-audit/review.md
    sha256: c72288f53240e8739b319a02f1ea9ffba30b6d470799b8bc8cf7d6142703d701
    role: context
  - path: reviews/structured/20261022T054333Z-dna-gyrase-complex-audit/review.yaml
    sha256: 065f7e481454309ec43695ba570d27b86a7298934be115e11a484ea07d7f6fa3
    role: context
  - path: reviews/structured/20261022T054334Z-dna-polymerase-iii-beta-sliding-clamp-processivity-factor-complex-audit/review.md
    sha256: c89e1091f0a30eee84b8546d7b878332037cdfbb7c6dd63476c1f5f0f71a2342
    role: context
  - path: reviews/structured/20261022T054334Z-dna-polymerase-iii-beta-sliding-clamp-processivity-factor-complex-audit/review.yaml
    sha256: 84e5adb96b8a522d949bae027ae872b20bfc79d81a1085e5985110a76847d8a9
    role: context
  - path: reviews/structured/20261022T054335Z-dna-polymerase-iii-clamp-loader-chi-psi-subcomplex-audit/review.md
    sha256: 152228f31792910dcd21997e1be3fd55f5144cff673af8de1c42bc3a33e78782
    role: context
  - path: reviews/structured/20261022T054335Z-dna-polymerase-iii-clamp-loader-chi-psi-subcomplex-audit/review.yaml
    sha256: f0a3078cb532265918ce2a60882bf5bfd50a743e50c7effbd8c2e88e05442037
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
- target_id: GO:0097685
  path: data/structures/other/dinoflagellate_apical_groove.yaml
  label: dinoflagellate apical groove
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dinoflagellate_apical_groove.yaml
    role: maintained scientific record
- target_id: GO:0097686
  path: data/structures/other/dinoflagellate_apical_horn.yaml
  label: dinoflagellate apical horn
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dinoflagellate_apical_horn.yaml
    role: maintained scientific record
- target_id: GO:0097611
  path: data/structures/other/dinoflagellate_cingulum.yaml
  label: dinoflagellate cingulum
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dinoflagellate_cingulum.yaml
    role: maintained scientific record
- target_id: GO:0097613
  path: data/structures/other/dinoflagellate_epicone.yaml
  label: dinoflagellate epicone
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dinoflagellate_epicone.yaml
    role: maintained scientific record
- target_id: GO:0097614
  path: data/structures/other/dinoflagellate_hypocone.yaml
  label: dinoflagellate hypocone
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dinoflagellate_hypocone.yaml
    role: maintained scientific record
- target_id: GO:0097618
  path: data/structures/other/dinoflagellate_sulcal_notch.yaml
  label: dinoflagellate sulcal notch
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dinoflagellate_sulcal_notch.yaml
    role: maintained scientific record
- target_id: GO:0097612
  path: data/structures/other/dinoflagellate_sulcus.yaml
  label: dinoflagellate sulcus
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dinoflagellate_sulcus.yaml
    role: maintained scientific record
- target_id: GO:0120217
  path: data/structures/other/dna_gyrase_complex.yaml
  label: DNA gyrase complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_gyrase_complex.yaml
    role: maintained scientific record
- target_id: GO:0044775
  path: data/structures/other/dna_polymerase_iii_beta_sliding_clamp_processivity_factor_complex.yaml
  label: DNA polymerase III, beta sliding clamp processivity factor complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_polymerase_iii_beta_sliding_clamp_processivity_factor_complex.yaml
    role: maintained scientific record
- target_id: GO:0043847
  path: data/structures/other/dna_polymerase_iii_clamp_loader_chi_psi_subcomplex.yaml
  label: DNA polymerase III, clamp loader chi/psi subcomplex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_polymerase_iii_clamp_loader_chi_psi_subcomplex.yaml
    role: maintained scientific record
scope:
  description: Exact ten-record PR cohort reassessed against current main 3b62e24ac00545bbec0797390e6b89389e27992c.
    Changed inputs are substantively reassessed. Scientific records remain unchanged.
  selection: Complete cohort of ten maintained records reviewed in original PR head
    830127e8d6581acf5f927f1ff91f1dca0805257b.
  coverage: full
  population_size: 10
  reviewed_target_ids:
  - GO:0097685
  - GO:0097686
  - GO:0097611
  - GO:0097613
  - GO:0097614
  - GO:0097618
  - GO:0097612
  - GO:0120217
  - GO:0044775
  - GO:0043847
checks:
- check_id: qc
  name: Full native QC
  status: passed
  required: true
  target_ids:
  - GO:0097685
  - GO:0097686
  - GO:0097611
  - GO:0097613
  - GO:0097614
  - GO:0097618
  - GO:0097612
  - GO:0120217
  - GO:0044775
  - GO:0043847
  command: just qc
  exit_code: 0
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  scope_note: Actual local execution at main-merge head dbdd66f36d1363c94eab2c58305c2f58a68baf09.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-qc
- check_id: labels
  name: Native label correspondence
  status: passed
  required: true
  target_ids:
  - GO:0097685
  - GO:0097686
  - GO:0097611
  - GO:0097613
  - GO:0097614
  - GO:0097618
  - GO:0097612
  - GO:0120217
  - GO:0044775
  - GO:0043847
  command: just validate-products
  exit_code: 0
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  scope_note: Actual local execution at main-merge head dbdd66f36d1363c94eab2c58305c2f58a68baf09.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-labels
- check_id: trait-links
  name: TraitMech references
  status: passed
  required: true
  target_ids:
  - GO:0097685
  - GO:0097686
  - GO:0097611
  - GO:0097613
  - GO:0097614
  - GO:0097618
  - GO:0097612
  - GO:0120217
  - GO:0044775
  - GO:0043847
  command: just check-trait-links --check
  exit_code: 0
  summary: Native TraitMech link check passed.
  scope_note: Actual local execution at main-merge head dbdd66f36d1363c94eab2c58305c2f58a68baf09.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-trait-links
- check_id: vendored
  name: Pinned governed files
  status: passed
  required: true
  target_ids:
  - GO:0097685
  - GO:0097686
  - GO:0097611
  - GO:0097613
  - GO:0097614
  - GO:0097618
  - GO:0097612
  - GO:0120217
  - GO:0044775
  - GO:0043847
  command: just vendored-check
  exit_code: 0
  summary: Pinned governed files match; native vendored check passed.
  scope_note: Actual local execution at main-merge head dbdd66f36d1363c94eab2c58305c2f58a68baf09.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-vendored
- check_id: curies
  name: Native identifier resolver
  status: passed
  required: true
  target_ids:
  - GO:0097685
  - GO:0097686
  - GO:0097611
  - GO:0097613
  - GO:0097614
  - GO:0097618
  - GO:0097612
  - GO:0120217
  - GO:0044775
  - GO:0043847
  command: just check-curies-strict
  exit_code: 0
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  scope_note: Actual local execution at main-merge head dbdd66f36d1363c94eab2c58305c2f58a68baf09.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-curies
- check_id: focused-0
  name: validate GO:0097685
  status: passed
  required: true
  target_ids:
  - GO:0097685
  command: just validate data/structures/other/dinoflagellate_apical_groove.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-1
  name: validate-strict GO:0097685
  status: passed
  required: true
  target_ids:
  - GO:0097685
  command: just validate-strict data/structures/other/dinoflagellate_apical_groove.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-2
  name: validate GO:0097686
  status: passed
  required: true
  target_ids:
  - GO:0097686
  command: just validate data/structures/other/dinoflagellate_apical_horn.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-3
  name: validate-strict GO:0097686
  status: passed
  required: true
  target_ids:
  - GO:0097686
  command: just validate-strict data/structures/other/dinoflagellate_apical_horn.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-4
  name: validate GO:0097611
  status: passed
  required: true
  target_ids:
  - GO:0097611
  command: just validate data/structures/other/dinoflagellate_cingulum.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-5
  name: validate-strict GO:0097611
  status: passed
  required: true
  target_ids:
  - GO:0097611
  command: just validate-strict data/structures/other/dinoflagellate_cingulum.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-6
  name: validate GO:0097613
  status: passed
  required: true
  target_ids:
  - GO:0097613
  command: just validate data/structures/other/dinoflagellate_epicone.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-7
  name: validate-strict GO:0097613
  status: passed
  required: true
  target_ids:
  - GO:0097613
  command: just validate-strict data/structures/other/dinoflagellate_epicone.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-8
  name: validate GO:0097614
  status: passed
  required: true
  target_ids:
  - GO:0097614
  command: just validate data/structures/other/dinoflagellate_hypocone.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-9
  name: validate-strict GO:0097614
  status: passed
  required: true
  target_ids:
  - GO:0097614
  command: just validate-strict data/structures/other/dinoflagellate_hypocone.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-10
  name: validate GO:0097618
  status: passed
  required: true
  target_ids:
  - GO:0097618
  command: just validate data/structures/other/dinoflagellate_sulcal_notch.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-11
  name: validate-strict GO:0097618
  status: passed
  required: true
  target_ids:
  - GO:0097618
  command: just validate-strict data/structures/other/dinoflagellate_sulcal_notch.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-12
  name: validate GO:0097612
  status: passed
  required: true
  target_ids:
  - GO:0097612
  command: just validate data/structures/other/dinoflagellate_sulcus.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-13
  name: validate-strict GO:0097612
  status: passed
  required: true
  target_ids:
  - GO:0097612
  command: just validate-strict data/structures/other/dinoflagellate_sulcus.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-14
  name: validate GO:0120217
  status: passed
  required: true
  target_ids:
  - GO:0120217
  command: just validate data/structures/other/dna_gyrase_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-15
  name: validate-strict GO:0120217
  status: passed
  required: true
  target_ids:
  - GO:0120217
  command: just validate-strict data/structures/other/dna_gyrase_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-16
  name: validate GO:0044775
  status: passed
  required: true
  target_ids:
  - GO:0044775
  command: just validate data/structures/other/dna_polymerase_iii_beta_sliding_clamp_processivity_factor_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-17
  name: validate-strict GO:0044775
  status: passed
  required: true
  target_ids:
  - GO:0044775
  command: just validate-strict data/structures/other/dna_polymerase_iii_beta_sliding_clamp_processivity_factor_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-18
  name: validate GO:0043847
  status: passed
  required: true
  target_ids:
  - GO:0043847
  command: just validate data/structures/other/dna_polymerase_iii_clamp_loader_chi_psi_subcomplex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-19
  name: validate-strict GO:0043847
  status: passed
  required: true
  target_ids:
  - GO:0043847
  command: just validate-strict data/structures/other/dna_polymerase_iii_clamp_loader_chi_psi_subcomplex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: supplemental-pmid
  name: Supplemental bounded PMID authority checks
  status: passed
  required: true
  target_ids:
  - GO:0097685
  - GO:0097686
  - GO:0097611
  - GO:0097613
  - GO:0097614
  - GO:0097618
  - GO:0097612
  - GO:0120217
  - GO:0044775
  - GO:0043847
  command: .venv/bin/python /private/tmp/cellstructure-batches-2346-2397-20261103/check_pmid_chunks.py
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387
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
  - GO:0097685
  - GO:0097686
  - GO:0097611
  - GO:0097613
  - GO:0097614
  - GO:0097618
  - GO:0097612
  - GO:0120217
  - GO:0044775
  - GO:0043847
  summary: Whole-record applicability was assessed for all ten targets. Gyrase, beta
    clamp and chi/psi make positive molecular or replication-pathway claims, so their
    formal expression-only exclusions are corrected. The seven dinoflagellate records
    assert morphology and topology while deferring molecular claims, so their prose
    exclusions remain justified. The complete current official catalogue contains
    no matching dinoflagellate host. The real E. coli precise1k dataset lists five
    strains; seven exact loci each returned 201 module rows. Only holD b4372 exceeds
    the ppGpp module 145 threshold, independently confirmed in its 70-gene list. These
    computational observations do not establish physical assembly, formation, direct
    regulation or localization; threshold-negative results are not biological absence.
    BL21(DE3) and MC1061 experimental preparations are not claimed covered by exact
    strain. Historical runner unavailability is not presented as a fresh invocation.
  evidence_ids:
  - micro-catalogue
  - micro-ecoli-meta
  - micro-ecoli-modules
  - micro-ecoli-gene-b2231
  - micro-ecoli-gene-b3699
  - micro-ecoli-gene-b3701
  - micro-ecoli-gene-b4259
  - micro-ecoli-gene-b4372
  - micro-ecoli-gene-b0470
  - micro-ecoli-gene-b4059
  - micro-ecoli-module-145
  - plaque-catalogue
  - plaque-catalogue-search
  - septin-catalogue
- check_id: independent-scientific-review
  name: Independent claim-level source review
  status: passed
  required: true
  target_ids:
  - GO:0097685
  - GO:0097686
  - GO:0097611
  - GO:0097613
  - GO:0097614
  - GO:0097618
  - GO:0097612
  - GO:0120217
  - GO:0044775
  - GO:0043847
  summary: Three read-only reviewers covered the complete ten-record cohort, including
    changed inputs, with explicit scientific findings and source-access limits. Final
    artifact/head acceptance occurs after saving.
  evidence_ids:
  - micro-policy
  - micro-schema
  - micro-native-policy
  - micro-graph-policy
  - micro-up-O73947
  - micro-up-P06710
  - micro-up-P0A988
  - micro-up-P0AES4
  - micro-up-P0AES6
  - micro-up-P0AGE0
  - micro-up-P28632
  - micro-up-P28905
  - micro-tax-186497
  - micro-tax-469008
  - micro-tax-562
  - micro-tax-83333
  - micro-go-0003918
  - micro-go-0006260
  - micro-go-0009330
  - micro-go-0009360
  - micro-go-0032991
  - micro-go-0034335
  - micro-go-0043846
  - micro-go-0043847
  - micro-go-0044775
  - micro-go-0044776
  - micro-go-0120217
  - micro-isa-0043847
  - micro-isa-0044775
  - micro-isa-0120217
  - micro-ipr-IPR005743
  - micro-ipr-IPR011557
  - micro-ipr-IPR001001-retry
  - micro-ipr-IPR007459
  - micro-ipr-IPR004615
  - micro-ipr-IPR018382
  - micro-pmid-11266590
  - micro-pmid-12940977
  - micro-pmid-1349852
  - micro-pmid-31666516
  - micro-pmid-7494000
  - micro-pmid-8389364
  - micro-pmid-8505305
  - micro-gyrase2019-jats
  - micro-pdb-6RKU-entry
  - micro-pdb-6RKU-assembly
  - micro-pdb-6RKW-entry
  - micro-pdb-6RKW-assembly
  - micro-pdb-6RKU-entity1
  - micro-pdb-6RKU-entity2
  - micro-kong1992-pdf
  - micro-olson1995-pdf
  - micro-ecoli-meta
  - micro-ecoli-module-145
  - plaque-policy
  - plaque-schema
  - plaque-review-skill
  - plaque-review-profile
  - plaque-review-schema
  - plaque-checklist
  - plaque-graph-policy
  - plaque-go
  - plaque-go-0097685-constraints
  - plaque-go-0097685-history
  - plaque-go-0097686-constraints
  - plaque-go-0097686-history
  - plaque-go-0097611-constraints
  - plaque-go-0097611-history
  - plaque-go-0097613-constraints
  - plaque-go-0097613-history
  - plaque-horn-epicone-path
  - plaque-tax-2864
  - plaque-tax-77300
  - plaque-iwataki2010-meta
  - plaque-gomez2017-meta
  - plaque-taylor1980-meta
  - plaque-gomez2017-s3
  - plaque-tol-orientation
  - plaque-tol-dinoflagellates
  - plaque-catalogue
  - septin-review-policy
  - septin-curation-policy
  - septin-schema-policy
  - septin-graph-policy
  - septin-literature-policy
  - septin-review-schema
  - septin-go
  - septin-go-0097614-history
  - septin-go-0097614-constraints
  - septin-go-0097618-history
  - septin-go-0097618-constraints
  - septin-go-0097612-history
  - septin-go-0097612-constraints
  - septin-tax-2864
  - septin-tol-orientation
  - septin-tol-dinoflagellates
  - septin-taylor1980-meta
  - septin-iwataki2010-meta
  - septin-catalogue
- check_id: historical-adapter-runner
  name: Retained historical adapter runner availability
  status: unavailable
  required: false
  target_ids:
  - GO:0097685
  - GO:0097686
  - GO:0097611
  - GO:0097613
  - GO:0097614
  - GO:0097618
  - GO:0097612
  - GO:0120217
  - GO:0044775
  - GO:0043847
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb datasets
  summary: Historical00:49Z invocation unavailable due to OS access restriction. Official
    catalogue fallback was inspected separately; no fresh invocation is claimed. Actual
    historical exit1 is retained in the evidence receipt; the native unavailable-check
    model has no execution exit-code field.
  scope_note: Historical canary receipt reread and hash-verified. Native policy permits
    source-page fallback.
  evidence_ids:
  - historical-adapter-runner-availability
- check_id: dinoflagellate_apical_groove-uniprot-verify
  name: Native dinoflagellate apical groove UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0097685
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dinoflagellate_apical_groove.yaml
    --verify
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dinoflagellate_apical_groove-uniprot-verify
- check_id: dinoflagellate_apical_groove-uniprot-causal
  name: Native dinoflagellate apical groove UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0097685
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dinoflagellate_apical_groove.yaml
    --causal-graphs
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dinoflagellate_apical_groove-uniprot-causal
- check_id: dinoflagellate_apical_horn-uniprot-verify
  name: Native dinoflagellate apical horn UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0097686
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dinoflagellate_apical_horn.yaml
    --verify
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dinoflagellate_apical_horn-uniprot-verify
- check_id: dinoflagellate_apical_horn-uniprot-causal
  name: Native dinoflagellate apical horn UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0097686
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dinoflagellate_apical_horn.yaml
    --causal-graphs
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dinoflagellate_apical_horn-uniprot-causal
- check_id: dinoflagellate_cingulum-uniprot-verify
  name: Native dinoflagellate cingulum UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0097611
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dinoflagellate_cingulum.yaml
    --verify
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dinoflagellate_cingulum-uniprot-verify
- check_id: dinoflagellate_cingulum-uniprot-causal
  name: Native dinoflagellate cingulum UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0097611
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dinoflagellate_cingulum.yaml
    --causal-graphs
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dinoflagellate_cingulum-uniprot-causal
- check_id: dinoflagellate_epicone-uniprot-verify
  name: Native dinoflagellate epicone UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0097613
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dinoflagellate_epicone.yaml
    --verify
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dinoflagellate_epicone-uniprot-verify
- check_id: dinoflagellate_epicone-uniprot-causal
  name: Native dinoflagellate epicone UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0097613
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dinoflagellate_epicone.yaml
    --causal-graphs
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dinoflagellate_epicone-uniprot-causal
- check_id: dinoflagellate_hypocone-uniprot-verify
  name: Native dinoflagellate hypocone UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0097614
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dinoflagellate_hypocone.yaml
    --verify
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dinoflagellate_hypocone-uniprot-verify
- check_id: dinoflagellate_hypocone-uniprot-causal
  name: Native dinoflagellate hypocone UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0097614
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dinoflagellate_hypocone.yaml
    --causal-graphs
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dinoflagellate_hypocone-uniprot-causal
- check_id: dinoflagellate_sulcal_notch-uniprot-verify
  name: Native dinoflagellate sulcal notch UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0097618
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dinoflagellate_sulcal_notch.yaml
    --verify
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dinoflagellate_sulcal_notch-uniprot-verify
- check_id: dinoflagellate_sulcal_notch-uniprot-causal
  name: Native dinoflagellate sulcal notch UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0097618
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dinoflagellate_sulcal_notch.yaml
    --causal-graphs
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dinoflagellate_sulcal_notch-uniprot-causal
- check_id: dinoflagellate_sulcus-uniprot-verify
  name: Native dinoflagellate sulcus UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0097612
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dinoflagellate_sulcus.yaml
    --verify
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dinoflagellate_sulcus-uniprot-verify
- check_id: dinoflagellate_sulcus-uniprot-causal
  name: Native dinoflagellate sulcus UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0097612
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dinoflagellate_sulcus.yaml
    --causal-graphs
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dinoflagellate_sulcus-uniprot-causal
- check_id: dna_gyrase_complex-uniprot-verify
  name: Native DNA gyrase complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0120217
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dna_gyrase_complex.yaml
    --verify
  exit_code: 0
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dna_gyrase_complex-uniprot-verify
- check_id: dna_gyrase_complex-uniprot-causal
  name: Native DNA gyrase complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0120217
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dna_gyrase_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dna_gyrase_complex-uniprot-causal
- check_id: dna_polymerase_iii_beta_sliding_clamp_processivity_factor_complex-uniprot-verify
  name: Native DNA polymerase III, beta sliding clamp processivity factor complex
    UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0044775
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dna_polymerase_iii_beta_sliding_clamp_processivity_factor_complex.yaml
    --verify
  exit_code: 0
  summary: 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dna_polymerase_iii_beta_sliding_clamp_processivity_factor_complex-uniprot-verify
- check_id: dna_polymerase_iii_beta_sliding_clamp_processivity_factor_complex-uniprot-causal
  name: Native DNA polymerase III, beta sliding clamp processivity factor complex
    UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0044775
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dna_polymerase_iii_beta_sliding_clamp_processivity_factor_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dna_polymerase_iii_beta_sliding_clamp_processivity_factor_complex-uniprot-causal
- check_id: dna_polymerase_iii_clamp_loader_chi_psi_subcomplex-uniprot-verify
  name: Native DNA polymerase III, clamp loader chi/psi subcomplex UniProt verify
    check
  status: passed
  required: true
  target_ids:
  - GO:0043847
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dna_polymerase_iii_clamp_loader_chi_psi_subcomplex.yaml
    --verify
  exit_code: 0
  summary: 2 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dna_polymerase_iii_clamp_loader_chi_psi_subcomplex-uniprot-verify
- check_id: dna_polymerase_iii_clamp_loader_chi_psi_subcomplex-uniprot-causal
  name: Native DNA polymerase III, clamp loader chi/psi subcomplex UniProt causal
    check
  status: passed
  required: true
  target_ids:
  - GO:0043847
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dna_polymerase_iii_clamp_loader_chi_psi_subcomplex.yaml
    --causal-graphs
  exit_code: 0
  summary: 2 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dna_polymerase_iii_clamp_loader_chi_psi_subcomplex-uniprot-causal
evidence:
- evidence_id: current-record-0
  kind: record_content
  reference: data/structures/other/dinoflagellate_apical_groove.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T05:38:33Z'
  support: context_only
  summary: Original frozen SHA256 7577f4358ce9bcc9753ec38e0295a7e496261827869f77353480ef2b130ad1f4;
    current SHA256 7577f4358ce9bcc9753ec38e0295a7e496261827869f77353480ef2b130ad1f4.
    Record bytes unchanged since the original review.
  snapshot_sha256: 7577f4358ce9bcc9753ec38e0295a7e496261827869f77353480ef2b130ad1f4
- evidence_id: original-review-0
  kind: prior_review
  reference: reviews/structured/20261022T054302Z-dinoflagellate-apical-groove-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T05:38:33Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: f605131be90cc3b54b26cfafe3e17d6268979c5937a227f25411cfdf18e25971
- evidence_id: current-record-1
  kind: record_content
  reference: data/structures/other/dinoflagellate_apical_horn.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T05:38:33Z'
  support: context_only
  summary: Original frozen SHA256 77b2ec19b71236a91786a44611abcc34eb6a7e927763f6ff641f2c879813c344;
    current SHA256 77b2ec19b71236a91786a44611abcc34eb6a7e927763f6ff641f2c879813c344.
    Record bytes unchanged since the original review.
  snapshot_sha256: 77b2ec19b71236a91786a44611abcc34eb6a7e927763f6ff641f2c879813c344
- evidence_id: original-review-1
  kind: prior_review
  reference: reviews/structured/20261022T054304Z-dinoflagellate-apical-horn-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T05:38:33Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: f6ee1ed0e9d0154aa075463a0c6b5407216fc6b6d595cf5c87d47aa15073e6fe
- evidence_id: current-record-2
  kind: record_content
  reference: data/structures/other/dinoflagellate_cingulum.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T05:38:33Z'
  support: context_only
  summary: Original frozen SHA256 c29822ebb0e810421c4516a4db5b8e6d648739e5c563e491d584850a65011513;
    current SHA256 c29822ebb0e810421c4516a4db5b8e6d648739e5c563e491d584850a65011513.
    Record bytes unchanged since the original review.
  snapshot_sha256: c29822ebb0e810421c4516a4db5b8e6d648739e5c563e491d584850a65011513
- evidence_id: original-review-2
  kind: prior_review
  reference: reviews/structured/20261022T054304Z-dinoflagellate-cingulum-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T05:38:33Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 9f2327be51767cbf946ef143bdace86d855ba02f5ec8e15df34dc62440399d7f
- evidence_id: current-record-3
  kind: record_content
  reference: data/structures/other/dinoflagellate_epicone.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T05:38:33Z'
  support: context_only
  summary: Original frozen SHA256 30e41a70bae04d4698b3b0bc40226fb51727a9f8664c4031c3ae8145216dfcdd;
    current SHA256 30e41a70bae04d4698b3b0bc40226fb51727a9f8664c4031c3ae8145216dfcdd.
    Record bytes unchanged since the original review.
  snapshot_sha256: 30e41a70bae04d4698b3b0bc40226fb51727a9f8664c4031c3ae8145216dfcdd
- evidence_id: original-review-3
  kind: prior_review
  reference: reviews/structured/20261022T054305Z-dinoflagellate-epicone-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T05:38:33Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 6d966b5dd38100535f6632d4ac31fd436f690a2b0d0acca9f7c1d6466fa88579
- evidence_id: current-record-4
  kind: record_content
  reference: data/structures/other/dinoflagellate_hypocone.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T05:38:33Z'
  support: context_only
  summary: Original frozen SHA256 0a596b02f63ce6799d10b49b4cf34a921fb2ae92e1208ee599a96ed47c5f40a1;
    current SHA256 0a596b02f63ce6799d10b49b4cf34a921fb2ae92e1208ee599a96ed47c5f40a1.
    Record bytes unchanged since the original review.
  snapshot_sha256: 0a596b02f63ce6799d10b49b4cf34a921fb2ae92e1208ee599a96ed47c5f40a1
- evidence_id: original-review-4
  kind: prior_review
  reference: reviews/structured/20261022T054306Z-dinoflagellate-hypocone-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T05:38:33Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 9808828a60ce9d3accad23938b10e300ecda029aeb6a2822448eb1e32734acee
- evidence_id: current-record-5
  kind: record_content
  reference: data/structures/other/dinoflagellate_sulcal_notch.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T05:38:33Z'
  support: context_only
  summary: Original frozen SHA256 0e3dace360a1a70bc43f318649972ebb63a50628897c7681bb81c9c75f18c7b1;
    current SHA256 0e3dace360a1a70bc43f318649972ebb63a50628897c7681bb81c9c75f18c7b1.
    Record bytes unchanged since the original review.
  snapshot_sha256: 0e3dace360a1a70bc43f318649972ebb63a50628897c7681bb81c9c75f18c7b1
- evidence_id: original-review-5
  kind: prior_review
  reference: reviews/structured/20261022T054307Z-dinoflagellate-sulcal-notch-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T05:38:33Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 599567d90a1060af4e54f540be250d609a9ce6ea8092f826317f4bb31a75f4e7
- evidence_id: current-record-6
  kind: record_content
  reference: data/structures/other/dinoflagellate_sulcus.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T05:38:33Z'
  support: context_only
  summary: Original frozen SHA256 b3606a5c03fbc85a602f3ea6927c22e49eedbcd00d1e9607c85ac080205bd356;
    current SHA256 b3606a5c03fbc85a602f3ea6927c22e49eedbcd00d1e9607c85ac080205bd356.
    Record bytes unchanged since the original review.
  snapshot_sha256: b3606a5c03fbc85a602f3ea6927c22e49eedbcd00d1e9607c85ac080205bd356
- evidence_id: original-review-6
  kind: prior_review
  reference: reviews/structured/20261022T054307Z-dinoflagellate-sulcus-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T05:38:33Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 92ecf76bae282ad0410728eee21b4fcac7653e0d76c1544fca4d05d7dc8acd49
- evidence_id: current-record-7
  kind: record_content
  reference: data/structures/other/dna_gyrase_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T05:38:33Z'
  support: context_only
  summary: Original frozen SHA256 5f4e9e6f29de383572bdbea4aabb06fd250a5faeedd5facf716a7d57c860a263;
    current SHA256 5e7e1a94281ec5bb4c72ea205e6e44bc4545175d4051eab98df531f709ac35b8.
    Changed record reassessed against current sources.
  snapshot_sha256: 5e7e1a94281ec5bb4c72ea205e6e44bc4545175d4051eab98df531f709ac35b8
- evidence_id: original-review-7
  kind: prior_review
  reference: reviews/structured/20261022T054333Z-dna-gyrase-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T05:38:33Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 065f7e481454309ec43695ba570d27b86a7298934be115e11a484ea07d7f6fa3
- evidence_id: current-record-8
  kind: record_content
  reference: data/structures/other/dna_polymerase_iii_beta_sliding_clamp_processivity_factor_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T05:38:33Z'
  support: context_only
  summary: Original frozen SHA256 0369f6dedbb1719e899d2bc9895033ab1dc7652865adb0597e10901b4e5ce664;
    current SHA256 0369f6dedbb1719e899d2bc9895033ab1dc7652865adb0597e10901b4e5ce664.
    Record bytes unchanged since the original review.
  snapshot_sha256: 0369f6dedbb1719e899d2bc9895033ab1dc7652865adb0597e10901b4e5ce664
- evidence_id: original-review-8
  kind: prior_review
  reference: reviews/structured/20261022T054334Z-dna-polymerase-iii-beta-sliding-clamp-processivity-factor-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T05:38:33Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 84e5adb96b8a522d949bae027ae872b20bfc79d81a1085e5985110a76847d8a9
- evidence_id: current-record-9
  kind: record_content
  reference: data/structures/other/dna_polymerase_iii_clamp_loader_chi_psi_subcomplex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T05:38:33Z'
  support: context_only
  summary: Original frozen SHA256 ae7299b0c7b889f3f035fe582e2b6c8fddb1a507dd0e1ceadda8c1d8e73a60cb;
    current SHA256 ae7299b0c7b889f3f035fe582e2b6c8fddb1a507dd0e1ceadda8c1d8e73a60cb.
    Record bytes unchanged since the original review.
  snapshot_sha256: ae7299b0c7b889f3f035fe582e2b6c8fddb1a507dd0e1ceadda8c1d8e73a60cb
- evidence_id: original-review-9
  kind: prior_review
  reference: reviews/structured/20261022T054335Z-dna-polymerase-iii-clamp-loader-chi-psi-subcomplex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T05:38:33Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: f0a3078cb532265918ce2a60882bf5bfd50a743e50c7effbd8c2e88e05442037
- evidence_id: micro-record-0
  kind: record_content
  reference: data/structures/other/dna_gyrase_complex.yaml
  locator: Complete current maintained YAML at dbdd66f36d1363c94eab2c58305c2f58a68baf09
  accessed_at: '2026-11-04T05:36:32.876537Z'
  support: supports
  summary: Entire identity/hierarchy/components/examples/taxonomy/functions/graph/discussions/history
    reviewed; no maintained image or measurement rows. Protein and gene classes are
    distinguished from the complex and external graph actors.
  snapshot_sha256: 5e7e1a94281ec5bb4c72ea205e6e44bc4545175d4051eab98df531f709ac35b8
- evidence_id: micro-prior-0
  kind: prior_review
  reference: reviews/structured/20261022T054333Z-dna-gyrase-complex-audit/review.yaml
  locator: Complete immutable original YAML and derived Markdown
  accessed_at: '2026-11-04T05:36:32.876624Z'
  support: supports
  summary: Original checks, evidence access limits, assessments, findings and actions
    read; old source reads remain historical and are not certified as fresh retrieval.
  snapshot_sha256: 065f7e481454309ec43695ba570d27b86a7298934be115e11a484ea07d7f6fa3
- evidence_id: micro-delta-0
  kind: record_content
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/7-stale.diff
  locator: Original frozen record versus current main 3b62e24ac00545bbec0797390e6b89389e27992c
  accessed_at: '2026-11-04T05:36:32.876658Z'
  support: supports
  summary: 'Only gyrase differs: dated history plus InterPro groundings on two existing
    component_ref graph nodes. Beta and chi/psi remain byte-identical. No constituent/edge
    was added by this delta.'
  snapshot_sha256: 024af411a92a6ccd1afd1f60438e3c2bc525b1328dda4a58c41d0cca2f003ff4
- evidence_id: micro-record-1
  kind: record_content
  reference: data/structures/other/dna_polymerase_iii_beta_sliding_clamp_processivity_factor_complex.yaml
  locator: Complete current maintained YAML at dbdd66f36d1363c94eab2c58305c2f58a68baf09
  accessed_at: '2026-11-04T05:36:32.876684Z'
  support: supports
  summary: Entire identity/hierarchy/components/examples/taxonomy/functions/graph/discussions/history
    reviewed; no maintained image or measurement rows. Protein and gene classes are
    distinguished from the complex and external graph actors.
  snapshot_sha256: 0369f6dedbb1719e899d2bc9895033ab1dc7652865adb0597e10901b4e5ce664
- evidence_id: micro-prior-1
  kind: prior_review
  reference: reviews/structured/20261022T054334Z-dna-polymerase-iii-beta-sliding-clamp-processivity-factor-complex-audit/review.yaml
  locator: Complete immutable original YAML and derived Markdown
  accessed_at: '2026-11-04T05:36:32.876704Z'
  support: supports
  summary: Original checks, evidence access limits, assessments, findings and actions
    read; old source reads remain historical and are not certified as fresh retrieval.
  snapshot_sha256: 84e5adb96b8a522d949bae027ae872b20bfc79d81a1085e5985110a76847d8a9
- evidence_id: micro-delta-1
  kind: record_content
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/8-stale.diff
  locator: Original frozen record versus current main 3b62e24ac00545bbec0797390e6b89389e27992c
  accessed_at: '2026-11-04T05:36:32.876735Z'
  support: supports
  summary: 'Only gyrase differs: dated history plus InterPro groundings on two existing
    component_ref graph nodes. Beta and chi/psi remain byte-identical. No constituent/edge
    was added by this delta.'
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: micro-record-2
  kind: record_content
  reference: data/structures/other/dna_polymerase_iii_clamp_loader_chi_psi_subcomplex.yaml
  locator: Complete current maintained YAML at dbdd66f36d1363c94eab2c58305c2f58a68baf09
  accessed_at: '2026-11-04T05:36:32.876757Z'
  support: supports
  summary: Entire identity/hierarchy/components/examples/taxonomy/functions/graph/discussions/history
    reviewed; no maintained image or measurement rows. Protein and gene classes are
    distinguished from the complex and external graph actors.
  snapshot_sha256: ae7299b0c7b889f3f035fe582e2b6c8fddb1a507dd0e1ceadda8c1d8e73a60cb
- evidence_id: micro-prior-2
  kind: prior_review
  reference: reviews/structured/20261022T054335Z-dna-polymerase-iii-clamp-loader-chi-psi-subcomplex-audit/review.yaml
  locator: Complete immutable original YAML and derived Markdown
  accessed_at: '2026-11-04T05:36:32.876777Z'
  support: supports
  summary: Original checks, evidence access limits, assessments, findings and actions
    read; old source reads remain historical and are not certified as fresh retrieval.
  snapshot_sha256: f0a3078cb532265918ce2a60882bf5bfd50a743e50c7effbd8c2e88e05442037
- evidence_id: micro-delta-2
  kind: record_content
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/9-stale.diff
  locator: Original frozen record versus current main 3b62e24ac00545bbec0797390e6b89389e27992c
  accessed_at: '2026-11-04T05:36:32.876818Z'
  support: supports
  summary: 'Only gyrase differs: dated history plus InterPro groundings on two existing
    component_ref graph nodes. Beta and chi/psi remain byte-identical. No constituent/edge
    was added by this delta.'
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: micro-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Exact class/family grounding; formation versus function; discussions append-only
    rationale/history
  accessed_at: '2026-11-04T05:36:32.876843Z'
  support: supports
  summary: Verified full-protein class mapping is separate from reference-strain examples.
    UNKNOWN formation is not automatically a finding. Preserve historical rationale/posed_date;
    update current notes and append provenance after supported curation.
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
- evidence_id: micro-schema
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Component classes, graph actors/scope, hierarchy and essentiality
  accessed_at: '2026-11-04T05:36:32.876865Z'
  support: supports
  summary: Generic families and scoped nonmechanistic outlines are permitted. External
    DnaX/SSB actors need not become chi/psi constituents or optional examples.
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: micro-native-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Structured Source Cross-Checks with profile/config/checklist
  accessed_at: '2026-11-04T05:36:32.876896Z'
  support: supports
  summary: Positive molecular/pathway claims trigger applicability; no expression
    assertion is not sufficient exclusion. Catalogue and actual gene/module checks
    retain strain and computational limits. Seventeen common inputs match previously
    read bytes; current review skill/profile/config and pertinent policies reread.
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: micro-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Constituent references and NONMECHANISTIC FUNCTION outlines
  accessed_at: '2026-11-04T05:36:32.876915Z'
  support: supports
  summary: Coarse contributes-to and functional edges are evaluated within explicit
    scope, without adding ordered reactions, universal essentiality or exact atomic
    interfaces.
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: micro-original-audit
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/original-audit.json
  locator: Six actual original validate/render commands;39 historical input occurrences;6
    original artifacts
  accessed_at: '2026-11-04T05:29:07.132106Z'
  support: supports
  summary: All original YAMLs validate and deterministically render their retained
    Markdown. All39 historical input hashes agree at their recorded source revision;
    all6 original artifacts match the original PR head.
  snapshot_sha256: 2a173556a1f051701dd81576f3891064dd54c63e07c56dd307a4c9107d0c3d81
- evidence_id: micro-up-O73947
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/O73947.json
  locator: Native accession/status/name/primary gene/loci/taxon/InterPro and relevant
    complete FUNCTION/SUBUNIT/alternative-products clauses; exact retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/up-O73947.raw
  accessed_at: '2026-11-04T05:28:48.297669Z'
  support: supports
  summary: 'O73947: UniProtKB reviewed (Swiss-Prot); DNA polymerase sliding clamp;
    genes [''pcn'']; loci [''PF0983'']; taxon 186497; InterPro [''IPR046938'', ''IPR000730'',
    ''IPR022649'', ''IPR022659'', ''IPR022648'']. Current native identity, family
    links and pertinent function/subunit annotations; linked studies are not all independently
    body-read. Archaeal PCNA homotrimer in Pyrococcus furiosus reference strain, not
    a bacterial PolIII beta protein.'
  snapshot_sha256: 80227a87e72b1c55b65ee273befaed23165bfead07a5e9039a90f8138df48e13
- evidence_id: micro-up-P06710
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P06710.json
  locator: Native accession/status/name/primary gene/loci/taxon/InterPro and relevant
    complete FUNCTION/SUBUNIT/alternative-products clauses; exact retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/up-P06710.raw
  accessed_at: '2026-11-04T05:28:46.161034Z'
  support: supports
  summary: 'P06710: UniProtKB reviewed (Swiss-Prot); DNA polymerase III subunit tau;
    genes [''dnaX'']; loci [''b0470'', ''JW0459'']; taxon 83333; InterPro [''IPR003593'',
    ''IPR001270'', ''IPR008921'', ''IPR022001'', ''IPR022754'', ''IPR012763'', ''IPR021029'',
    ''IPR050238'', ''IPR045085'', ''IPR027417'', ''IPR038249'']. Current native identity,
    family links and pertinent function/subunit annotations; linked studies are not
    all independently body-read. Tau/gamma arise through programmed frameshifting;
    these are external partner products, not added chi/psi constituents.'
  snapshot_sha256: 9dda9544a27ae2699f7d77382a528089a2ff9fff43ab2d5106c4b1817d3db291
- evidence_id: micro-up-P0A988
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0A988.json
  locator: Native accession/status/name/primary gene/loci/taxon/InterPro and relevant
    complete FUNCTION/SUBUNIT/alternative-products clauses; exact retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/up-P0A988.raw
  accessed_at: '2026-11-04T05:28:46.577600Z'
  support: supports
  summary: 'P0A988: UniProtKB reviewed (Swiss-Prot); Beta sliding clamp; genes [''dnaN''];
    loci [''b3701'', ''JW3678'']; taxon 83333; InterPro [''IPR046938'', ''IPR001001'',
    ''IPR022635'', ''IPR022637'', ''IPR022634'']. Current native identity, family
    links and pertinent function/subunit annotations; linked studies are not all independently
    body-read. Full-length beta homodimer is distinguished from a shorter beta* isoform;
    no invariant oligomerization assertion for all isoforms.'
  snapshot_sha256: 41e5cead43ae6b73cc4fedfee2b9e111259e12f217532aba8590e487ea82f65f
- evidence_id: micro-up-P0AES4
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0AES4.json
  locator: Native accession/status/name/primary gene/loci/taxon/InterPro and relevant
    complete FUNCTION/SUBUNIT/alternative-products clauses; exact retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/up-P0AES4.raw
  accessed_at: '2026-11-04T05:28:44.535606Z'
  support: supports
  summary: 'P0AES4: UniProtKB reviewed (Swiss-Prot); DNA gyrase subunit A; genes [''gyrA''];
    loci [''b2231'', ''JW2225'']; taxon 83333; InterPro [''IPR005743'', ''IPR006691'',
    ''IPR035516'', ''IPR013760'', ''IPR013758'', ''IPR013757'', ''IPR002205'', ''IPR050220''].
    Current native identity, family links and pertinent function/subunit annotations;
    linked studies are not all independently body-read.'
  snapshot_sha256: a69da3b0cb03f1092f1dbd6b3a9fadc93e98b7be0791b11f89c235a5681ce7e0
- evidence_id: micro-up-P0AES6
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0AES6.json
  locator: Native accession/status/name/primary gene/loci/taxon/InterPro and relevant
    complete FUNCTION/SUBUNIT/alternative-products clauses; exact retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/up-P0AES6.raw
  accessed_at: '2026-11-04T05:28:43.550611Z'
  support: supports
  summary: 'P0AES6: UniProtKB reviewed (Swiss-Prot); DNA gyrase subunit B; genes [''gyrB''];
    loci [''b3699'', ''JW5625'']; taxon 83333; InterPro [''IPR002288'', ''IPR011557'',
    ''IPR049353'', ''IPR041423'', ''IPR036890'', ''IPR003594'', ''IPR020568'', ''IPR014721'',
    ''IPR001241'', ''IPR013760'', ''IPR000565'', ''IPR013759'', ''IPR013506'', ''IPR018522'',
    ''IPR006171'', ''IPR034160'']. Current native identity, family links and pertinent
    function/subunit annotations; linked studies are not all independently body-read.'
  snapshot_sha256: 0173a94c0ecd654e17e8da52dd9806a2d215b177d9474473cc73f50b740a19b4
- evidence_id: micro-up-P0AGE0
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0AGE0.json
  locator: Native accession/status/name/primary gene/loci/taxon/InterPro and relevant
    complete FUNCTION/SUBUNIT/alternative-products clauses; exact retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/up-P0AGE0.raw
  accessed_at: '2026-11-04T05:28:47.062601Z'
  support: supports
  summary: 'P0AGE0: UniProtKB reviewed (Swiss-Prot); Single-stranded DNA-binding protein;
    genes [''ssb'']; loci [''b4059'', ''JW4020'']; taxon 83333; InterPro [''IPR012340'',
    ''IPR000424'', ''IPR011344'']. Current native identity, family links and pertinent
    function/subunit annotations; linked studies are not all independently body-read.
    SSB/HolC contact is native annotation context, not an Olson1995 SSB-binding measurement.'
  snapshot_sha256: 9cc7842d10fb4d4084cc8d8a6c64e7a053dd441120a2c3676b7e5acac7835711
- evidence_id: micro-up-P28632
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P28632.json
  locator: Native accession/status/name/primary gene/loci/taxon/InterPro and relevant
    complete FUNCTION/SUBUNIT/alternative-products clauses; exact retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/up-P28632.raw
  accessed_at: '2026-11-04T05:28:43.193447Z'
  support: supports
  summary: 'P28632: UniProtKB reviewed (Swiss-Prot); DNA polymerase III subunit psi;
    genes [''holD'']; loci [''b4372'', ''JW4334'']; taxon 83333; InterPro [''IPR004615'',
    ''IPR036654'', ''IPR018382'']. Current native identity, family links and pertinent
    function/subunit annotations; linked studies are not all independently body-read.'
  snapshot_sha256: 5b0d2927c696ac3aee8304d1e0bca6ff313e6655c90a21fa618a247a7e1dc7b2
- evidence_id: micro-up-P28905
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P28905.json
  locator: Native accession/status/name/primary gene/loci/taxon/InterPro and relevant
    complete FUNCTION/SUBUNIT/alternative-products clauses; exact retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/up-P28905.raw
  accessed_at: '2026-11-04T05:28:45.401513Z'
  support: supports
  summary: 'P28905: UniProtKB reviewed (Swiss-Prot); DNA polymerase III subunit chi;
    genes [''holC'']; loci [''b4259'', ''JW4216'']; taxon 83333; InterPro [''IPR007459'',
    ''IPR036768'']. Current native identity, family links and pertinent function/subunit
    annotations; linked studies are not all independently body-read.'
  snapshot_sha256: 7b36f4f87de6692ef228e17ced56294a628188d88a248f1debd62a912eef5f57
- evidence_id: micro-query-dnaN
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdnaN%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete exact reviewed gene/taxon returned page; exact retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/query-dnaN.raw
  accessed_at: '2026-11-04T05:28:48.554909Z'
  support: supports
  summary: Current bounded query returns ['P0A988']; singleton matches the maintained
    example. This does not reconstruct an October selection query or prove physical
    membership.
  snapshot_sha256: 1887ae15fef4c0ae00bfb78438785bb21e2ed00e22c11ddbe95db13d89030426
  search_scope: UniProtKB REST literal URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdnaN%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500;
    actual 2026-11-04T05:28:48.554909Z; requested size500, complete returned singleton
    page. Exact reviewed gene and taxon83333 only; no all-alias/all-taxon/historical
    uniqueness claim.
- evidence_id: micro-query-gyrA
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AgyrA%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete exact reviewed gene/taxon returned page; exact retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/query-gyrA.raw
  accessed_at: '2026-11-04T05:28:45.697448Z'
  support: supports
  summary: Current bounded query returns ['P0AES4']; singleton matches the maintained
    example. This does not reconstruct an October selection query or prove physical
    membership.
  snapshot_sha256: eae5fd1ed4476e99c4d1aa676438fb80d0881a91be441011e89c98a80668045f
  search_scope: UniProtKB REST literal URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AgyrA%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500;
    actual 2026-11-04T05:28:45.697448Z; requested size500, complete returned singleton
    page. Exact reviewed gene and taxon83333 only; no all-alias/all-taxon/historical
    uniqueness claim.
- evidence_id: micro-query-gyrB
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AgyrB%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete exact reviewed gene/taxon returned page; exact retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/query-gyrB.raw
  accessed_at: '2026-11-04T05:28:46.630063Z'
  support: supports
  summary: Current bounded query returns ['P0AES6']; singleton matches the maintained
    example. This does not reconstruct an October selection query or prove physical
    membership.
  snapshot_sha256: 7f291d2a8b59d8769fc4f789d9cfbace8c08bbd60ebffae2638b28a0072bed02
  search_scope: UniProtKB REST literal URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AgyrB%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500;
    actual 2026-11-04T05:28:46.630063Z; requested size500, complete returned singleton
    page. Exact reviewed gene and taxon83333 only; no all-alias/all-taxon/historical
    uniqueness claim.
- evidence_id: micro-query-holC
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AholC%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete exact reviewed gene/taxon returned page; exact retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/query-holC.raw
  accessed_at: '2026-11-04T05:28:47.362648Z'
  support: supports
  summary: Current bounded query returns ['P28905']; singleton matches the maintained
    example. This does not reconstruct an October selection query or prove physical
    membership.
  snapshot_sha256: 9ffe9c8d9221032fc7915464e2c8e9e9ab26683e7b264268b35ffe517dc856f0
  search_scope: UniProtKB REST literal URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AholC%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500;
    actual 2026-11-04T05:28:47.362648Z; requested size500, complete returned singleton
    page. Exact reviewed gene and taxon83333 only; no all-alias/all-taxon/historical
    uniqueness claim.
- evidence_id: micro-query-holD
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AholD%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete exact reviewed gene/taxon returned page; exact retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/query-holD.raw
  accessed_at: '2026-11-04T05:28:47.545779Z'
  support: supports
  summary: Current bounded query returns ['P28632']; singleton matches the maintained
    example. This does not reconstruct an October selection query or prove physical
    membership.
  snapshot_sha256: 7a9744a2b70bad7c77358c27cbde2c7602185f088d552801264210ebf52453c5
  search_scope: UniProtKB REST literal URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AholD%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500;
    actual 2026-11-04T05:28:47.545779Z; requested size500, complete returned singleton
    page. Exact reviewed gene and taxon83333 only; no all-alias/all-taxon/historical
    uniqueness claim.
- evidence_id: micro-tax-186497
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/186497
  locator: Exact taxon identity/name/rank/lineage; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/tax-186497.raw
  accessed_at: '2026-11-04T05:29:46.008805Z'
  support: supports
  summary: '186497: Pyrococcus furiosus DSM 3638, rank strain, lineage Archaea; Methanobacteriati;
    Methanobacteriota; Thermococci; Thermococcales; Thermococcaceae; Pyrococcus; .
    K12 source/reference, BL21(DE3) expression and species-level examples remain distinct.'
  snapshot_sha256: 8444ca1fba9ae3efd3cc3af260e82a9ba750c9a3d331f493dcc3ef2b706ed161
- evidence_id: micro-tax-469008
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/469008
  locator: Exact taxon identity/name/rank/lineage; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/tax-469008.raw
  accessed_at: '2026-11-04T05:28:47.037355Z'
  support: supports
  summary: '469008: Escherichia coli BL21(DE3), rank strain, lineage Bacteria; Pseudomonadati;
    Pseudomonadota; Gammaproteobacteria; Enterobacterales; Enterobacteriaceae; Escherichia;
    . K12 source/reference, BL21(DE3) expression and species-level examples remain
    distinct.'
  snapshot_sha256: 07cb4fa698b87d71164e352377fb19fe9378e32c57ff44cbb5bdd98639a7d969
- evidence_id: micro-tax-562
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562
  locator: Exact taxon identity/name/rank/lineage; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/tax-562.raw
  accessed_at: '2026-11-04T05:28:46.308634Z'
  support: supports
  summary: '562: Escherichia coli, rank species, lineage Bacteria; Pseudomonadati;
    Pseudomonadota; Gammaproteobacteria; Enterobacterales; Enterobacteriaceae; Escherichia;
    . K12 source/reference, BL21(DE3) expression and species-level examples remain
    distinct.'
  snapshot_sha256: 66d5c5c74569e24b72fd7b011961dc221b58d841db7db3023337fb534733e200
- evidence_id: micro-tax-83333
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333
  locator: Exact taxon identity/name/rank/lineage; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/tax-83333.raw
  accessed_at: '2026-11-04T05:28:46.338858Z'
  support: supports
  summary: '83333: Escherichia coli K-12, rank strain, lineage Bacteria; Pseudomonadati;
    Pseudomonadota; Gammaproteobacteria; Enterobacterales; Enterobacteriaceae; Escherichia;
    . K12 source/reference, BL21(DE3) expression and species-level examples remain
    distinct.'
  snapshot_sha256: f499fde9e4fcea85ff811b58a76a405669d32465a62eaf74240a48331b63d8e6
- evidence_id: micro-go-0003918
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0003918
  locator: Exact active term identity, definition, synonyms and relevant child relationship
    records; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/go-0003918.raw
  accessed_at: '2026-11-04T05:28:47.823526Z'
  support: supports
  summary: 'GO:0003918: DNA topoisomerase type II (double strand cut, ATP-hydrolyzing)
    activity; obsolete=False; definition: {''text'': ''Catalysis of a DNA topological
    transformation by transiently cleaving a pair of complementary DNA strands to
    form a gate through which a second double-stranded DNA segment is passed, after
    which the severed strands in the first DNA segment are rejoined, driven by ATP
    hydrolysis. The enzyme changes the linking number in multiples of 2.'', ''xrefs'':
    [{''dbCode'': ''PMID'', ''dbId'': ''8811192''}]}. Native ontology wording is separately
    checked against primary biology; GO0044775 itself contains the disputed cross-class
    language.'
  snapshot_sha256: 3aa2cf3100a7786c3eedb4f05aa17fb692d8f929f36ecb6004d962a404b900a5
- evidence_id: micro-go-0006260
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0006260
  locator: Exact active term identity, definition, synonyms and relevant child relationship
    records; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/go-0006260.raw
  accessed_at: '2026-11-04T05:28:47.852574Z'
  support: supports
  summary: 'GO:0006260: DNA replication; obsolete=False; definition: {''text'': ''The
    cellular metabolic process in which a cell duplicates one or more molecules of
    DNA. DNA replication begins when specific sequences, known as origins of replication,
    are recognized and bound by the origin recognition complex, and ends when the
    original DNA molecule has been completely duplicated and the copies topologically
    separated. The unit of replication usually corresponds to the genome of the cell,
    an organelle, or a virus. The template for replication can either be an existing
    DNA molecule or RNA.''}. Native ontology wording is separately checked against
    primary biology; GO0044775 itself contains the disputed cross-class language.'
  snapshot_sha256: dc45c0feccd11a684f3d3f838297ef32f5b69a7b59a61d655120b7ac89ec8fba
- evidence_id: micro-go-0009330
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009330
  locator: Exact active term identity, definition, synonyms and relevant child relationship
    records; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/go-0009330.raw
  accessed_at: '2026-11-04T05:28:47.934556Z'
  support: supports
  summary: 'GO:0009330: DNA topoisomerase type II (double strand cut, ATP-hydrolyzing)
    complex; obsolete=False; definition: {''text'': ''Complex that possesses DNA topoisomerase
    II (double strand cut, ATP-hydrolyzing) activity.'', ''xrefs'': [{''dbCode'':
    ''WikiPedia'', ''dbId'': ''Type_II_topoisomerase''}]}. Native ontology wording
    is separately checked against primary biology; GO0044775 itself contains the disputed
    cross-class language.'
  snapshot_sha256: 962af0c76b3f0b74aa3e4d9dbe531a272764ed2b29b84c93919a65c0339a22fa
- evidence_id: micro-go-0009360
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009360
  locator: Exact active term identity, definition, synonyms and relevant child relationship
    records; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/go-0009360.raw
  accessed_at: '2026-11-04T05:28:48.189043Z'
  support: supports
  summary: 'GO:0009360: DNA polymerase III complex; obsolete=False; definition: {''text'':
    "The DNA polymerase III holoenzyme is a complex that contains 10 different types
    of subunits. These subunits are organized into 3 functionally essential sub-assemblies:
    the pol III core, the beta sliding clamp processivity factor and the clamp-loading
    complex. The pol III core carries out the polymerase and the 3''-5'' exonuclease
    proofreading activities. The polymerase is tethered to the template via the sliding
    clamp processivity factor. The clamp-loading complex assembles the beta processivity
    factor onto the primer template and plays a central role in the organization and
    communication at the replication fork.", ''xrefs'': [{''dbCode'': ''PMID'', ''dbId'':
    ''11525729''}, {''dbCode'': ''PMID'', ''dbId'': ''12940977''}, {''dbCode'': ''UniProt'',
    ''dbId'': ''P06710''}]}. Native ontology wording is separately checked against
    primary biology; GO0044775 itself contains the disputed cross-class language.'
  snapshot_sha256: 4b5038b620c1b4a860e4500335d17a12aec81b36fa6def186d4716389e3ba757
- evidence_id: micro-go-0032991
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032991
  locator: Exact active term identity, definition, synonyms and relevant child relationship
    records; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/go-0032991.raw
  accessed_at: '2026-11-04T05:28:48.187111Z'
  support: supports
  summary: 'GO:0032991: protein-containing complex; obsolete=False; definition: {''text'':
    ''A stable assembly of two or more macromolecules, i.e. proteins, nucleic acids,
    carbohydrates or lipids, in which at least one component is a protein and the
    constituent parts function together.''}. Native ontology wording is separately
    checked against primary biology; GO0044775 itself contains the disputed cross-class
    language.'
  snapshot_sha256: 480165003b2c8a406006ff17c4cfe836fc000541ad5dac1ca0f585ed30c02e87
- evidence_id: micro-go-0034335
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0034335
  locator: Exact active term identity, definition, synonyms and relevant child relationship
    records; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/go-0034335.raw
  accessed_at: '2026-11-04T05:28:48.215240Z'
  support: supports
  summary: 'GO:0034335: DNA negative supercoiling activity; obsolete=False; definition:
    {''text'': ''Catalytic introduction of negative supercoils into a DNA molecule
    or region thereof. In bacteria, negative supercoils are only introduced by DNA
    gyrase, a type II topoisomerase, but not all DNA gyrases are capable of introducing
    supercoils. In bacteria, the level of supercoiling varies widely between species
    and has been characterized properly in only a handful of organisms. The best characterized
    enzyme, from E.coli, is exceptionally proficient at supercoiling and this ability
    is not representative of all bacteria.'', ''xrefs'': [{''dbCode'': ''WikiPedia'',
    ''dbId'': ''DNA_gyrase''}]}. Native ontology wording is separately checked against
    primary biology; GO0044775 itself contains the disputed cross-class language.'
  snapshot_sha256: 6504dd13f0a1234c2325758cf6dacae5b76da953ab0ef736dd07ea10fc644482
- evidence_id: micro-go-0043846
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0043846
  locator: Exact active term identity, definition, synonyms and relevant child relationship
    records; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/go-0043846.raw
  accessed_at: '2026-11-04T05:28:48.306542Z'
  support: supports
  summary: 'GO:0043846: DNA polymerase III, clamp loader complex; obsolete=False;
    definition: {''text'': ''A heptamer that includes the tau and gamma products of
    the dnaX gene and the chi/psi subcomplex. Confers structural asymmetry that allows
    the polymerase to replicate both leading and lagging strands.'', ''xrefs'': [{''dbCode'':
    ''PMID'', ''dbId'': ''12940977''}]}. Native ontology wording is separately checked
    against primary biology; GO0044775 itself contains the disputed cross-class language.'
  snapshot_sha256: eeed7abe4e2c1402377d625d38b7f0dbe90bea19418a5da79d8f232ed383c447
- evidence_id: micro-go-0043847
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0043847
  locator: Exact active term identity, definition, synonyms and relevant child relationship
    records; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/go-0043847.raw
  accessed_at: '2026-11-04T05:28:48.504900Z'
  support: supports
  summary: 'GO:0043847: DNA polymerase III, clamp loader chi/psi subcomplex; obsolete=False;
    definition: {''text'': ''A dimer composed of the chi and psi subunits which is
    a subassembly of the DNA polymerase III clamp loader complex and serves as a bridge
    between the DnaX complex and the single-stranded DNA-binding protein (SSB).'',
    ''xrefs'': [{''dbCode'': ''PMID'', ''dbId'': ''12940977''}]}. Native ontology
    wording is separately checked against primary biology; GO0044775 itself contains
    the disputed cross-class language.'
  snapshot_sha256: 272d831705e0da87c0327899fd1d5ca431768e874ce856a4457759d74b11a45f
- evidence_id: micro-go-0044775
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0044775
  locator: Exact active term identity, definition, synonyms and relevant child relationship
    records; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/go-0044775.raw
  accessed_at: '2026-11-04T05:28:48.595649Z'
  support: supports
  summary: 'GO:0044775: DNA polymerase III, beta sliding clamp processivity factor
    complex; obsolete=False; definition: {''text'': ''A subcomplex of the DNA polymerase
    III holoenzyme which is responsible for tethering the catalytic subunit of DNA
    polymerase to DNA during high-speed replication. The complex is homodimeric in
    prokaryotes, and homotrimeric in other species.'', ''xrefs'': [{''dbCode'': ''UniProt'',
    ''dbId'': ''O73947''}]}. Native ontology wording is separately checked against
    primary biology; GO0044775 itself contains the disputed cross-class language.'
  snapshot_sha256: aab63fe0f13574e5cdb4285ac6c21025c42bd555213b4bdd48c4fe1328c9dba8
- evidence_id: micro-go-0044776
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0044776
  locator: Exact active term identity, definition, synonyms and relevant child relationship
    records; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/go-0044776.raw
  accessed_at: '2026-11-04T05:28:48.643170Z'
  support: supports
  summary: 'GO:0044776: DNA polymerase III, core complex; obsolete=False; definition:
    {''text'': "The DNA polymerase III core complex consists of the alpha,epsilon
    and theta subunits and is carries out the polymerase and the 3''-5'' exonuclease
    proofreading activities.", ''xrefs'': [{''dbCode'': ''UniProt'', ''dbId'': ''P06710''}]}.
    Native ontology wording is separately checked against primary biology; GO0044775
    itself contains the disputed cross-class language.'
  snapshot_sha256: 982b73157eba30d19078e0d907e9bfbf961c71042efafc23c62aec999f229282
- evidence_id: micro-go-0120217
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0120217
  locator: Exact active term identity, definition, synonyms and relevant child relationship
    records; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/go-0120217.raw
  accessed_at: '2026-11-04T05:28:48.671930Z'
  support: supports
  summary: 'GO:0120217: DNA gyrase complex; obsolete=False; definition: {''text'':
    ''A bacterial type IIA topoisomerase that is unique in its function of introducing
    negative supercoils into DNA at the expense of ATP hydrolysis and is also capable
    of relaxing positive supercoils, an activity shared with topoisomerase IV. Typically,
    it is composed of two copies each of an A subunit (GyrA) and a B subunit (GyrB).'',
    ''xrefs'': [{''dbCode'': ''PMID'', ''dbId'': ''1657531''}, {''dbCode'': ''PMID'',
    ''dbId'': ''20675723''}, {''dbCode'': ''Wikipedia'', ''dbId'': ''DNA_gyrase''}]}.
    Native ontology wording is separately checked against primary biology; GO0044775
    itself contains the disputed cross-class language.'
  snapshot_sha256: f0de592dfb5c30c29a89a07677fafb81c8040683df37b02189c3f6f73811e73a
- evidence_id: micro-isa-0043847
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0043847/ancestors?relations=is_a
  locator: Complete explicitly is_a-filtered ancestor response; exact retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/isa-0043847.raw
  accessed_at: '2026-11-04T05:28:48.982243Z'
  support: supports
  summary: Exact ancestry is checked independently of parthood; the named complex
    parent relationship is supported. Raw response retained for typed ancestor audit;
    no mixed-relation closure inferred.
  snapshot_sha256: 2be25b17d48731416570f9873998e7dd67798ca005af84bd899e3132c0f10e8a
- evidence_id: micro-isa-0044775
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0044775/ancestors?relations=is_a
  locator: Complete explicitly is_a-filtered ancestor response; exact retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/isa-0044775.raw
  accessed_at: '2026-11-04T05:28:49.031185Z'
  support: supports
  summary: Exact ancestry is checked independently of parthood; the named complex
    parent relationship is supported. Raw response retained for typed ancestor audit;
    no mixed-relation closure inferred.
  snapshot_sha256: 65b6ba6aea9a0d17b4816daa5ffa66bc1af0952c5d163dc004ef6c50c27fb839
- evidence_id: micro-isa-0120217
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0120217/ancestors?relations=is_a
  locator: Complete explicitly is_a-filtered ancestor response; exact retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/isa-0120217.raw
  accessed_at: '2026-11-04T05:28:48.941553Z'
  support: supports
  summary: Exact ancestry is checked independently of parthood; the named complex
    parent relationship is supported. Raw response retained for typed ancestor audit;
    no mixed-relation closure inferred.
  snapshot_sha256: 1dea80039cb095819ebb286636b8c48dc1c3e455fab3d10d921c69159ecbc640
- evidence_id: micro-ipr-IPR005743
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005743/
  locator: Complete native name/type/hierarchy/integrated signatures, description
    and curation flags; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/ipr-IPR005743.raw
  accessed_at: '2026-11-04T05:28:43.587382Z'
  support: supports
  summary: 'IPR005743: {''name'': ''DNA gyrase, subunit A'', ''short'': ''GyrA''};
    type family; signatures {''hamap'': {''MF_01897'': ''DNA gyrase subunit A [gyrA]''}}.
    Exact whole-protein family and matching maintained UniProt example xref.'
  snapshot_sha256: 3381bdfb7148e154fda31bde2ba43fa7b703fb61ff2e064a153cdb84f6fd231b
- evidence_id: micro-ipr-IPR011557
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR011557/
  locator: Complete native name/type/hierarchy/integrated signatures, description
    and curation flags; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/ipr-IPR011557.raw
  accessed_at: '2026-11-04T05:28:44.144893Z'
  support: supports
  summary: 'IPR011557: {''name'': ''DNA gyrase, subunit B'', ''short'': ''GyrB''};
    type family; signatures {''hamap'': {''MF_01898'': ''DNA gyrase subunit B [gyrB]''},
    ''ncbifam'': {''TIGR01059'': ''DNA gyrase subunit B''}}. Exact whole-protein family
    and matching maintained UniProt example xref.'
  snapshot_sha256: 4d68f4e62fbab9095f45069c2ac8461c4de9942f13db1ebe84315906e2197560
- evidence_id: micro-ipr-IPR001001-retry
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001001/
  locator: Complete native name/type/hierarchy/integrated signatures, description
    and curation flags; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/ipr-IPR001001-retry.raw
  accessed_at: '2026-11-04T05:29:45.941575Z'
  support: supports
  summary: 'IPR001001: {''name'': ''DNA polymerase III, beta sliding clamp'', ''short'':
    ''DNA_polIII_beta''}; type family; signatures {''pirsf'': {''PIRSF000804'': ''Predicted
    DNA-directed DNA polymerase III, beta subunit''}, ''cdd'': {''cd00140'': ''beta_clamp''},
    ''panther'': {''PTHR30478'': ''DNA POLYMERASE III SUBUNIT BETA''}, ''ncbifam'':
    {''TIGR00663'': ''DNA polymerase III subunit beta''}, ''smart'': {''SM00480'':
    ''DNA polymerase III beta subunit''}}. Exact whole-protein family and matching
    maintained UniProt example xref. Native family distinguishes bacterial beta from
    archaeal/eukaryotic PCNA; generic functional prose is not primary experimental
    evidence.'
  snapshot_sha256: f8b49add1156ee4d460fbd89cad0810cffb7f20ce4dacd4961ffebfcd384a538
- evidence_id: micro-ipr-IPR007459
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007459/
  locator: Complete native name/type/hierarchy/integrated signatures, description
    and curation flags; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/ipr-IPR007459.raw
  accessed_at: '2026-11-04T05:28:44.311537Z'
  support: supports
  summary: 'IPR007459: {''name'': ''DNA polymerase III chi subunit, HolC'', ''short'':
    ''DNA_pol3_chi''}; type family; signatures {''panther'': {''PTHR38767'': ''DNA
    POLYMERASE III SUBUNIT CHI''}, ''pfam'': {''PF04364'': ''DNA polymerase III chi
    subunit, HolC''}}. Exact whole-protein family and matching maintained UniProt
    example xref.'
  snapshot_sha256: 5f9af2b066940512eac57ef0e983bf79616c8e00846a7fdaf4ac3eeacc116d12
- evidence_id: micro-ipr-IPR004615
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004615/
  locator: Complete native name/type/hierarchy/integrated signatures, description
    and curation flags; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/ipr-IPR004615.raw
  accessed_at: '2026-11-04T05:28:44.319917Z'
  support: supports
  summary: 'IPR004615: {''name'': ''DNA polymerase III, psi subunit'', ''short'':
    ''DNA_pol_III_psi''}; type family; signatures {''pirsf'': {''PIRSF029225'': ''DNA
    polymerase III, psi subunit''}, ''pfam'': {''PF03603'': ''DNA polymerase III psi
    subunit''}}. Exact whole-protein family and matching maintained UniProt example
    xref. Historical generic unknown-function prose does not supersede Xiao/Olson
    primary observations.'
  snapshot_sha256: 2c70542817958052c37c630066b6135d817759e1421ab5d91b21e0af5118a654
- evidence_id: micro-ipr-IPR018382
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR018382/
  locator: Complete native name/type/hierarchy/integrated signatures, description
    and curation flags; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/ipr-IPR018382.raw
  accessed_at: '2026-11-04T05:28:44.884280Z'
  support: context_only
  summary: 'IPR018382: {''name'': ''DNA polymerase III, psi subunit, subgroup'', ''short'':
    ''DNA_pol_III_psi_subgr''}; type family; signatures {''ncbifam'': {''TIGR00664'':
    ''DNA polymerase III subunit psi''}}. Narrower HolD subgroup under IPR004615,
    not required to ground the generic psi class.'
  snapshot_sha256: e1010a989bf869c59bdd15abe4642337b9952b7a0597c4ac6581ef9b11c2a1d6
- evidence_id: micro-pmid-11266590
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11266590+AND+SRC%3AMED&format=json&resultType=core&pageSize=1000
  locator: Complete exact MED title/authors/year/DOI and deposited abstract; exact
    retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/pmid-11266590.raw
  accessed_at: '2026-11-04T05:29:45.837788Z'
  support: supports
  summary: '11266590: Crystal structure of an archaeal DNA sliding clamp: proliferating
    cell nuclear antigen from Pyrococcus furiosus.; DOI 10.1110/ps.36401. Primary-study
    abstract, independently read completely. No full-body read is implied by this
    row.'
  snapshot_sha256: d5f4db9960b7bb956f48446f5900c3d2d2b3380969c604d74785eeda9889f1bc
- evidence_id: micro-pmid-12940977
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12940977+AND+SRC%3AMED&format=json&resultType=core&pageSize=1000
  locator: Complete exact MED title/authors/year/DOI and deposited abstract; exact
    retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/pmid-12940977.raw
  accessed_at: '2026-11-04T05:28:47.194162Z'
  support: context_only
  summary: '12940977: Chromosomal replicases as asymmetric dimers: studies of subunit
    arrangement and functional consequences.; DOI 10.1046/j.1365-2958.2003.03645.x.
    Secondary review abstract; context only. No full-body read is implied by this
    row.'
  snapshot_sha256: aad6b63ace81a7445d5853ff89368388b265ca915696bd7d874152b36eb89d1b
- evidence_id: micro-pmid-1349852
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A1349852+AND+SRC%3AMED&format=json&resultType=core&pageSize=1000
  locator: Complete exact MED title/authors/year/DOI and deposited abstract; exact
    retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/pmid-1349852.raw
  accessed_at: '2026-11-04T05:28:47.068958Z'
  support: supports
  summary: '1349852: Three-dimensional structure of the beta subunit of E. coli DNA
    polymerase III holoenzyme: a sliding DNA clamp.; DOI 10.1016/0092-8674(92)90445-i.
    Primary-study abstract, independently read completely. No full-body read is implied
    by this row.'
  snapshot_sha256: 045dbc791d9b8f2d44fc824154897c0c7e1be90a5d1c61b47f8d448cb63d8a5d
- evidence_id: micro-pmid-31666516
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A31666516+AND+SRC%3AMED&format=json&resultType=core&pageSize=1000
  locator: Complete exact MED title/authors/year/DOI and deposited abstract; exact
    retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/pmid-31666516.raw
  accessed_at: '2026-11-04T05:28:47.054579Z'
  support: supports
  summary: '31666516: Cryo-EM structure of the complete E. coli DNA gyrase nucleoprotein
    complex.; DOI 10.1038/s41467-019-12914-y. Primary-study abstract, independently
    read completely. No full-body read is implied by this row.'
  snapshot_sha256: 6fbd9783ccf42d0efb712c1b611e4aab4fa805571f5a6841de596b673388beb4
- evidence_id: micro-pmid-7494000
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A7494000+AND+SRC%3AMED&format=json&resultType=core&pageSize=1000
  locator: Complete exact MED title/authors/year/DOI and deposited abstract; exact
    retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/pmid-7494000.raw
  accessed_at: '2026-11-04T05:28:47.391692Z'
  support: supports
  summary: '7494000: DnaX complex of Escherichia coli DNA polymerase III holoenzyme.
    The chi psi complex functions by increasing the affinity of tau and gamma for
    delta.delta'' to a physiologically relevant range.; DOI 10.1074/jbc.270.49.29570.
    Primary-study abstract, independently read completely. No full-body read is implied
    by this row.'
  snapshot_sha256: eb9807f3285d2122d5783ff682049bcd8f8699e5b42efa2e9efc8d810fa3278a
- evidence_id: micro-pmid-8389364
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8389364+AND+SRC%3AMED&format=json&resultType=core&pageSize=1000
  locator: Complete exact MED title/authors/year/DOI and deposited abstract; exact
    retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/pmid-8389364.raw
  accessed_at: '2026-11-04T05:28:47.669446Z'
  support: supports
  summary: '8389364: DNA polymerase III accessory proteins. III. holC and holD encoding
    chi and psi.; DOI 10.1016/s0021-9258(19)50266-6. Primary-study abstract, independently
    read completely. No full-body read is implied by this row.'
  snapshot_sha256: 4b71940eee5dd14fd6725415e8334781b89d5f0156cec9c6094cde054fdda8b4
- evidence_id: micro-pmid-8505305
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8505305+AND+SRC%3AMED&format=json&resultType=core&pageSize=1000
  locator: Complete exact MED title/authors/year/DOI and deposited abstract; exact
    retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/pmid-8505305.raw
  accessed_at: '2026-11-04T05:28:47.946971Z'
  support: supports
  summary: '8505305: DNA polymerase III accessory proteins. IV. Characterization of
    chi and psi.; DOI 10.1016/s0021-9258(19)50267-8. Primary-study abstract, independently
    read completely. No full-body read is implied by this row.'
  snapshot_sha256: 629441af31d2d0ef72f16ffe91af661fbb788f1f5396f4fd2acb433e04b02300
- evidence_id: micro-gyrase2019-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC6821735.1/PMC6821735.1.xml
  locator: Genuine JATS Introduction Sec1; Results Sec3–4 and Fig1–3 text captions;
    Discussion Sec8; Methods Sec10–13,17,20–21; no pixels/supplements/coordinates;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/gyrase2019-jats.raw
  accessed_at: '2026-11-04T05:28:49.292465Z'
  support: supports
  summary: Full-length proteins expressed in BL21(DE3) were purified and reconstituted;
    trapped gepotidacin/AMP-PNP/DNA cryo-EM preparations differ from activity assays.
    Sec17 explicitly distinguishes closed cleavage-domain6RKU from overall6RKW. K12
    protein source and correct2:2 protein stoichiometry are unaffected; complete sample
    sequences do not imply complete atomic coordinates.
  snapshot_sha256: 785daafe42b0ac243354e1036741c3475a3b5e10769d3e0e4e96398e5d841bf5
- evidence_id: micro-pdb-6RKU-entry
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/entry/6RKU
  locator: Exact native title/citation/experimental method/resolution and entry assembly
    information; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/pdb-6RKU-entry.raw
  accessed_at: '2026-11-04T05:28:48.564992Z'
  support: supports
  summary: 6RKU is the DNA-binding/cleavage-domain State1 model at4.0Å. Both link
    the same2019 study; no coordinate/pixel inspection claimed.
  snapshot_sha256: a4f8c7d36049c1d57991d8474271b4a0c10b7b6cd21f94ff7fc2b8ec84d167da
- evidence_id: micro-pdb-6RKU-assembly
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/assembly/6RKU/1
  locator: Complete assembly1 protein/NA counts and modeled versus total polymer monomers;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/pdb-6RKU-assembly.raw
  accessed_at: '2026-11-04T05:28:48.576063Z'
  support: supports
  summary: 6RKU models1848 of3422 polymer monomers. Both have4 protein instances and4
    DNA-chain instances; the portal octamer count is not8 protein subunits. Protein
    entities and sample lengths are distinct from modeled coverage.
  snapshot_sha256: 1186bd23f7f504961033028d9f0d7be4139ee62f811bdd3db49146dd8378729f
- evidence_id: micro-pdb-6RKW-entry
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/entry/6RKW
  locator: Exact native title/citation/experimental method/resolution and entry assembly
    information; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/pdb-6RKW-entry.raw
  accessed_at: '2026-11-04T05:28:48.680312Z'
  support: supports
  summary: 6RKW is the complete/overall gyrase-DNA model at6.6Å. Both link the same2019
    study; no coordinate/pixel inspection claimed.
  snapshot_sha256: e96c06cf26895043a7d0292e9de5f1048aebfe171333e3a29b366308125b290b
- evidence_id: micro-pdb-6RKW-assembly
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/assembly/6RKW/1
  locator: Complete assembly1 protein/NA counts and modeled versus total polymer monomers;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/pdb-6RKW-assembly.raw
  accessed_at: '2026-11-04T05:28:48.677043Z'
  support: supports
  summary: 6RKW models3458 of3598 polymer monomers. Both have4 protein instances and4
    DNA-chain instances; the portal octamer count is not8 protein subunits. Protein
    entities and sample lengths are distinct from modeled coverage.
  snapshot_sha256: 3ff9bdffdf1f1a2a4089621ad907d9416726c6c3e5cb3ce5ec8f843dbee74c24
- evidence_id: micro-pdb-6RKU-entity1
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/6RKU/1
  locator: Native polymer entity identity/details/copy count/sample length/UniProt/source
    and expression taxa; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/pdb-6RKU-entity1.raw
  accessed_at: '2026-11-04T05:28:48.726825Z'
  support: supports
  summary: Entity1 is GyrA P0AES4,875 sample residues,2 copies. SourceK12 tax83333,
    expressionBL21(DE3) tax469008; details explicitly identify DNA-binding/cleavage-domain
    scope. Full sample sequences remain consistent with incomplete modeled coordinates.
  snapshot_sha256: f61be1487076be77cb0214b855bbfcda7d512a911c63de6139217cb5681e9692
- evidence_id: micro-pdb-6RKU-entity2
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/6RKU/2
  locator: Native polymer entity identity/details/copy count/sample length/UniProt/source
    and expression taxa; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/pdb-6RKU-entity2.raw
  accessed_at: '2026-11-04T05:28:48.798503Z'
  support: supports
  summary: Entity2 is GyrB P0AES6,804 sample residues,2 copies. SourceK12 tax83333,
    expressionBL21(DE3) tax469008; details explicitly identify DNA-binding/cleavage-domain
    scope. Full sample sequences remain consistent with incomplete modeled coordinates.
  snapshot_sha256: 365d78fe074144d463a7078df2f07f4614224a9083b562891909fb0bba63facd
- evidence_id: micro-kong1992-pdf
  kind: primary_source
  reference: https://odonnell.rockefeller.edu/assets/pdfs/27.pdf
  locator: 'Genuine author-hosted PDF; extracted pp425,427,432–434: Summary/Introduction,
    architecture and Fig2–3 text captions, sequence comparison/Fig9 caption, conclusion
    and crystallization/data-collection paragraphs; no pixels; exact retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/kong1992-pdf.raw'
  accessed_at: '2026-11-04T05:28:54.217453Z'
  support: supports
  summary: E.coli beta forms a homodimer with three domains per monomer at2.5Å. DNA
    placement in the central hole is modeled rather than an observed DNA co-crystal.
    PCNA/phage clamp analogies are distinguished from bacterial beta identity; the
    later archaealPCNA primary abstract supplies trimer context. No claim of complete-paper
    or figure-pixel inspection.
  snapshot_sha256: 37747ac2c4a2846c81da93e332b820e774cfbf08c897807290e5d71ba2fae57c
- evidence_id: micro-olson1995-pdf
  kind: primary_source
  reference: https://www.colorado.edu/lab/mchenry/sites/default/files/attached-files/1995_14285_jbc_270_29570.pdf
  locator: Genuine author-hosted PDF pp29570–29576 main Introduction, Methods, Results
    and Discussion; TablesI/II and Fig1–7 text captions; no pixels/raw data; exact
    retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/olson1995-pdf.raw
  accessed_at: '2026-11-04T05:28:49.145645Z'
  support: supports
  summary: MC1061/pMAF310 holC-holD overexpression yields a soluble1:1 complex; purified
    partner-binding and reconstitution assays support tau/gamma association and enhanced
    delta/delta-prime affinity. This is not an SSB contact assay or universal native
    essentiality proof. High other-subunit concentrations permit omission in vitro;
    experimental MC1061 is not a listed precise1k strain.
  snapshot_sha256: 89c7a5c87c99d9152214217dac917db605f5a14bc6f1b6e9e5f10354a8592c23
- evidence_id: micro-xiao1993iii-publisher-access
  kind: validation
  reference: https://www.jbc.org/article/S0021-9258(19)50266-6/fulltext
  locator: Actual retained access response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/xiao1993iii-publisher.raw
  accessed_at: '2026-11-04T05:29:45.402095Z'
  support: context_only
  summary: HTTP403 access diagnostic only; no source body supported. Independent abstract
    or successful exact-authority retry is separately recorded.
  snapshot_sha256: 5774c5f5e35252c566d3a55e087a68fe11fa9451d64021eccde85e147a5e034c
- evidence_id: micro-xiao1993iv-publisher-access
  kind: validation
  reference: https://www.jbc.org/article/S0021-9258(19)50267-8/fulltext
  locator: Actual retained access response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/xiao1993iv-publisher.raw
  accessed_at: '2026-11-04T05:29:45.362419Z'
  support: context_only
  summary: HTTP403 access diagnostic only; no source body supported. Independent abstract
    or successful exact-authority retry is separately recorded.
  snapshot_sha256: cf269b4984c7b636f949d82729c3312a2d0568b96dabe80a6cda6f5da2109349
- evidence_id: micro-ipr-IPR001001-access
  kind: validation
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001001/
  locator: Actual retained access response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/ipr-IPR001001.raw
  accessed_at: '2026-11-04T05:28:44.310552Z'
  support: context_only
  summary: HTTP429 access diagnostic only; no source body supported. Independent abstract
    or successful exact-authority retry is separately recorded.
  snapshot_sha256: 9abf9cb941ee77b8e8a3348aa3517c7fbb81c7ae7cb580ff9d1b87961335b26f
- evidence_id: micro-historical-replication50-agent-xiao1993iii-publisher
  kind: validation
  reference: https://www.jbc.org/article/S0021-9258(19)50266-6/fulltext
  locator: Retained publisher access response
  accessed_at: '2026-10-22T05:33:26.898984Z'
  support: context_only
  summary: Publisher fulltext request returned HTTP403; no primary body was obtained
    from this route. Original timestamp/hash preserved; no fresh retrieval claim.
    Kind corrected from database to validation/context_only; original already disclosed
    failed access.
  snapshot_sha256: fa8dd2ccea114dc31a3ec23e71fd13fc732805c61ff6a261ad518478f9c736b5
- evidence_id: micro-historical-replication50-agent-xiao1993iv-publisher
  kind: validation
  reference: https://www.jbc.org/article/S0021-9258(19)50267-8/fulltext
  locator: Retained publisher access response
  accessed_at: '2026-10-22T05:33:26.898919Z'
  support: context_only
  summary: Publisher fulltext request returned HTTP403; no primary body was obtained
    from this route. Original timestamp/hash preserved; no fresh retrieval claim.
    Kind corrected from database to validation/context_only; original already disclosed
    failed access.
  snapshot_sha256: 285983a1306bb443abb0730572e6b0e5a298c7b950ae474020f46e76b3f05f23
- evidence_id: micro-catalogue
  kind: search
  reference: https://imodulondb.org/api/datasets
  locator: Complete official organism/dataset catalogue response; exact retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/catalogue.raw
  accessed_at: '2026-11-04T05:28:42.917849Z'
  support: supports
  summary: All20 returned organism rows and dataset listings inspected; E.coli precise1k
    is an actual available host/dataset. Selection is not a universal catalogue or
    future coverage claim.
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  search_scope: iModulonDB GET /api/datasets at 2026-11-04T05:28:42.917849Z; complete20
    organism rows/all listed datasets, no pagination or truncated result. Exact E.coli
    host/key selection; no unrelated proxy.
- evidence_id: micro-ecoli-meta
  kind: database
  reference: https://imodulondb.org/api/datasets/e_coli/precise1k/meta
  locator: Complete precise1k metadata and five-strain list; exact retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/ecoli-meta.raw
  accessed_at: '2026-11-04T05:28:43.478439Z'
  support: context_only
  summary: Five strains BW25113,DGF-298,GMOS,MG1655,W3110;1035 samples,518 conditions,201
    modules,4257 genes. This selected K12-related reference context is not exact MC1061
    or BL21(DE3) experimental coverage.
  snapshot_sha256: 6cd60b3e363a11c95c2b5b1d160fe360687c0a680a5b95c18c6c76e7c5d99865
- evidence_id: micro-ecoli-modules
  kind: search
  reference: https://imodulondb.org/api/datasets/e_coli/precise1k/imodulons
  locator: Complete201 module-list metadata, names/regulators/functions; exact retained
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/ecoli-modules.raw
  accessed_at: '2026-11-04T05:28:42.798220Z'
  support: context_only
  summary: All201 returned entries assessed as a bounded dataset inventory; module
    naming alone is not mechanism or biological evidence.
  snapshot_sha256: c9f7564cc9fa212686b00f75d35b5438d9d8660066eada141b263e580634e26d
  search_scope: iModulonDB e_coli/precise1k /imodulons at 2026-11-04T05:28:42.798220Z;
    all201 returned entries; no other dataset or uninspected activity experiment covered.
- evidence_id: micro-ecoli-gene-b2231
  kind: search
  reference: https://imodulondb.org/api/genes/b2231/imodulons?organism=e_coli&dataset=precise1k
  locator: All201 exact-locus weight/threshold/membership rows; exact retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/ecoli-gene-b2231.raw
  accessed_at: '2026-11-04T05:29:45.380057Z'
  support: context_only
  summary: Native locus b2231 returns201 rows; above-threshold hits []. Computational
    threshold membership/nonmembership does not establish physical assembly, formation,
    localization, dispensability or direct regulation.
  snapshot_sha256: 9f59a3a3f4f6d66f7a9ebe30e65451ea2f95b402ab5d4913811a72042443a93b
  search_scope: iModulonDB GET https://imodulondb.org/api/genes/b2231/imodulons?organism=e_coli&dataset=precise1k
    at 2026-11-04T05:29:45.380057Z; exact native locus, all201 returned module rows
    evaluated. Selected five-strain precise1k only; no alias/all-dataset/universal
    absence claim.
- evidence_id: micro-ecoli-gene-b3699
  kind: search
  reference: https://imodulondb.org/api/genes/b3699/imodulons?organism=e_coli&dataset=precise1k
  locator: All201 exact-locus weight/threshold/membership rows; exact retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/ecoli-gene-b3699.raw
  accessed_at: '2026-11-04T05:29:45.374852Z'
  support: context_only
  summary: Native locus b3699 returns201 rows; above-threshold hits []. Computational
    threshold membership/nonmembership does not establish physical assembly, formation,
    localization, dispensability or direct regulation.
  snapshot_sha256: 83ada913bdb84591331ee0cba793304d53b93fd86cd2aa9ef0d1960213135208
  search_scope: iModulonDB GET https://imodulondb.org/api/genes/b3699/imodulons?organism=e_coli&dataset=precise1k
    at 2026-11-04T05:29:45.374852Z; exact native locus, all201 returned module rows
    evaluated. Selected five-strain precise1k only; no alias/all-dataset/universal
    absence claim.
- evidence_id: micro-ecoli-gene-b3701
  kind: search
  reference: https://imodulondb.org/api/genes/b3701/imodulons?organism=e_coli&dataset=precise1k
  locator: All201 exact-locus weight/threshold/membership rows; exact retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/ecoli-gene-b3701.raw
  accessed_at: '2026-11-04T05:29:45.374811Z'
  support: context_only
  summary: Native locus b3701 returns201 rows; above-threshold hits []. Computational
    threshold membership/nonmembership does not establish physical assembly, formation,
    localization, dispensability or direct regulation.
  snapshot_sha256: d5e604543410b34561ac751e5b38c067a221e6ff1983dc41a90a52a22cc6670a
  search_scope: iModulonDB GET https://imodulondb.org/api/genes/b3701/imodulons?organism=e_coli&dataset=precise1k
    at 2026-11-04T05:29:45.374811Z; exact native locus, all201 returned module rows
    evaluated. Selected five-strain precise1k only; no alias/all-dataset/universal
    absence claim.
- evidence_id: micro-ecoli-gene-b4259
  kind: search
  reference: https://imodulondb.org/api/genes/b4259/imodulons?organism=e_coli&dataset=precise1k
  locator: All201 exact-locus weight/threshold/membership rows; exact retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/ecoli-gene-b4259.raw
  accessed_at: '2026-11-04T05:29:45.455900Z'
  support: context_only
  summary: Native locus b4259 returns201 rows; above-threshold hits []. Computational
    threshold membership/nonmembership does not establish physical assembly, formation,
    localization, dispensability or direct regulation.
  snapshot_sha256: be8fe859fb1c07c2e7a323c11e0c60e1a95b628d87875b7b37124f5bef8caf9b
  search_scope: iModulonDB GET https://imodulondb.org/api/genes/b4259/imodulons?organism=e_coli&dataset=precise1k
    at 2026-11-04T05:29:45.455900Z; exact native locus, all201 returned module rows
    evaluated. Selected five-strain precise1k only; no alias/all-dataset/universal
    absence claim.
- evidence_id: micro-ecoli-gene-b4372
  kind: search
  reference: https://imodulondb.org/api/genes/b4372/imodulons?organism=e_coli&dataset=precise1k
  locator: All201 exact-locus weight/threshold/membership rows; exact retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/ecoli-gene-b4372.raw
  accessed_at: '2026-11-04T05:29:45.455836Z'
  support: context_only
  summary: 'Native locus b4372 returns201 rows; above-threshold hits [{"k": 145, "name":
    "ppGpp", "regulator": ["ppGpp"], "function": "Stringent response", "category":
    "Global Stress", "weight": 0.055361181, "threshold": 0.048379363, "in_imodulon":
    true}]. Computational threshold membership/nonmembership does not establish physical
    assembly, formation, localization, dispensability or direct regulation.'
  snapshot_sha256: a7d1d16bb4c67ee5f721614cf65f823f0c6ee5764843fb782934a3033180ad8a
  search_scope: iModulonDB GET https://imodulondb.org/api/genes/b4372/imodulons?organism=e_coli&dataset=precise1k
    at 2026-11-04T05:29:45.455836Z; exact native locus, all201 returned module rows
    evaluated. Selected five-strain precise1k only; no alias/all-dataset/universal
    absence claim.
- evidence_id: micro-ecoli-gene-b0470
  kind: search
  reference: https://imodulondb.org/api/genes/b0470/imodulons?organism=e_coli&dataset=precise1k
  locator: All201 exact-locus weight/threshold/membership rows; exact retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/ecoli-gene-b0470.raw
  accessed_at: '2026-11-04T05:29:45.567554Z'
  support: context_only
  summary: Native locus b0470 returns201 rows; above-threshold hits []. Computational
    threshold membership/nonmembership does not establish physical assembly, formation,
    localization, dispensability or direct regulation.
  snapshot_sha256: 310f63e12eaf82829d04b8ada01acc7a111b5db11ccd96401f264ab62e66a758
  search_scope: iModulonDB GET https://imodulondb.org/api/genes/b0470/imodulons?organism=e_coli&dataset=precise1k
    at 2026-11-04T05:29:45.567554Z; exact native locus, all201 returned module rows
    evaluated. Selected five-strain precise1k only; no alias/all-dataset/universal
    absence claim.
- evidence_id: micro-ecoli-gene-b4059
  kind: search
  reference: https://imodulondb.org/api/genes/b4059/imodulons?organism=e_coli&dataset=precise1k
  locator: All201 exact-locus weight/threshold/membership rows; exact retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/ecoli-gene-b4059.raw
  accessed_at: '2026-11-04T05:29:45.553565Z'
  support: context_only
  summary: Native locus b4059 returns201 rows; above-threshold hits []. Computational
    threshold membership/nonmembership does not establish physical assembly, formation,
    localization, dispensability or direct regulation.
  snapshot_sha256: 19ce00cde1de93f45da1ec150047c9fbe674bb445470e6e03414b745855b11fb
  search_scope: iModulonDB GET https://imodulondb.org/api/genes/b4059/imodulons?organism=e_coli&dataset=precise1k
    at 2026-11-04T05:29:45.553565Z; exact native locus, all201 returned module rows
    evaluated. Selected five-strain precise1k only; no alias/all-dataset/universal
    absence claim.
- evidence_id: micro-ecoli-module-145
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise1k/145
  locator: Actual module145 metadata and complete70-gene weight list; threshold0.048379363;
    AI summary/activity narrative excluded; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/ecoli-module-145.raw
  accessed_at: '2026-11-04T05:32:51.235618Z'
  support: context_only
  summary: Module145 is ppGpp/Stringent response/Global Stress; holD b4372 weight0.055361181
    exceeds threshold0.048379363. The70-gene module is computational context, not
    a chi/psi assembly or direct regulation experiment. Generated AI prose and unsupported
    inferred pathway narratives are not used.
  snapshot_sha256: 830f9a931fa5b6577f9ad87c99a4cbc198961cbd72c61ad8ff4d42812846f2dd
- evidence_id: micro-historical-runner
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Actual historical2026-11-03T00:49:00.848907–00:49:00.863225Z runner receipt
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  summary: Historical unavailable/exit1 permission limitation only; no fresh invocation
    claimed. Current official API fallback independently inspected above.
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: micro-native-dna_gyrase_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dna_gyrase_complex-uniprot-verify-receipt.json
  locator: Actual command receipt; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dna_gyrase_complex-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T05:28:04.848428Z'
  support: supports
  summary: Actual exit0; 2 reviewed examples/2 COVERED typed nodes. This implemented
    accession/example coverage does not certify biological completeness or exact source-neutral
    family mapping.
  snapshot_sha256: d6117d92e9886ab85760ecc2931e4ee1acecf44cc732098bdc3254a539e3cc0a
- evidence_id: micro-native-dna_gyrase_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dna_gyrase_complex-uniprot-causal-receipt.json
  locator: Actual command receipt; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dna_gyrase_complex-uniprot-causal.log
    SHA256 e9925e98caefb278bed69f8a980ae3af6087a314dde6560afdf7442ac66a91b6
  accessed_at: '2026-11-04T05:28:05.287630Z'
  support: supports
  summary: Actual exit0; 2 reviewed examples/2 COVERED typed nodes. This implemented
    accession/example coverage does not certify biological completeness or exact source-neutral
    family mapping.
  snapshot_sha256: c115db0ad3a51f36155609c0888cb8b528dcafffcdb717babc5a70656ac87ffe
- evidence_id: micro-native-dna_polymerase_iii_beta_sliding_clamp_processivity_factor_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dna_polymerase_iii_beta_sliding_clamp_processivity_factor_complex-uniprot-verify-receipt.json
  locator: Actual command receipt; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dna_polymerase_iii_beta_sliding_clamp_processivity_factor_complex-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T05:28:06.498864Z'
  support: supports
  summary: Actual exit0; 1 reviewed example/1 COVERED typed node. This implemented
    accession/example coverage does not certify biological completeness or exact source-neutral
    family mapping.
  snapshot_sha256: 88e4a3ad79a93218b8c2f35e53af55cb5a6618d17b377a81090f39a6c7a26bed
- evidence_id: micro-native-dna_polymerase_iii_beta_sliding_clamp_processivity_factor_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dna_polymerase_iii_beta_sliding_clamp_processivity_factor_complex-uniprot-causal-receipt.json
  locator: Actual command receipt; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dna_polymerase_iii_beta_sliding_clamp_processivity_factor_complex-uniprot-causal.log
    SHA256 f767c55c18149a7ee0e0ecba42cf7bf6e538b498174ff3403619159559db03b6
  accessed_at: '2026-11-04T05:28:06.934813Z'
  support: supports
  summary: Actual exit0; 1 reviewed example/1 COVERED typed node. This implemented
    accession/example coverage does not certify biological completeness or exact source-neutral
    family mapping.
  snapshot_sha256: a0e057c3497e707d198483bccbaab15843e1d3ab59a5218021142a750b041e8c
- evidence_id: micro-native-dna_polymerase_iii_clamp_loader_chi_psi_subcomplex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dna_polymerase_iii_clamp_loader_chi_psi_subcomplex-uniprot-verify-receipt.json
  locator: Actual command receipt; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dna_polymerase_iii_clamp_loader_chi_psi_subcomplex-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T05:28:08.268775Z'
  support: supports
  summary: Actual exit0; 2 reviewed examples/2 COVERED plus2 UNANCHORED_WITH_UNIPROT
    typed nodes (DnaX andSSB external actors). This implemented accession/example
    coverage does not certify biological completeness or exact source-neutral family
    mapping.
  snapshot_sha256: b89851dad8eb3e6dde841f4c95003cec41db7aeb672bfce6dfd95a6c64d2654f
- evidence_id: micro-native-dna_polymerase_iii_clamp_loader_chi_psi_subcomplex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dna_polymerase_iii_clamp_loader_chi_psi_subcomplex-uniprot-causal-receipt.json
  locator: Actual command receipt; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dna_polymerase_iii_clamp_loader_chi_psi_subcomplex-uniprot-causal.log
    SHA256 b18c6192090adcab5331b9e6ba8404fd4684eab9585b0e5b5e6f36d94b560551
  accessed_at: '2026-11-04T05:28:08.702161Z'
  support: supports
  summary: Actual exit0; 2 reviewed examples/2 COVERED plus2 UNANCHORED_WITH_UNIPROT
    typed nodes (DnaX andSSB external actors). This implemented accession/example
    coverage does not certify biological completeness or exact source-neutral family
    mapping.
  snapshot_sha256: 939837d8879ac8f71adc152352126a518b171aa00df404cbea681d9064913a05
- evidence_id: plaque-current-0
  kind: record_content
  reference: data/structures/other/dinoflagellate_apical_groove.yaml
  locator: Entire maintained record at frozen source dbdd66f36d1363c94eab2c58305c2f58a68baf09
  accessed_at: '2026-11-04T05:32:33.011043Z'
  snapshot_sha256: 7577f4358ce9bcc9753ec38e0295a7e496261827869f77353480ef2b130ad1f4
  summary: Complete definition, hierarchy, taxonomic distribution, evidence, graph,
    discussions and history independently read. Original target bytes unchanged. No
    molecular components, protein examples, measurements or maintained images asserted.
  support: supports
- evidence_id: plaque-original-0-yaml
  kind: prior_review
  reference: reviews/structured/20261022T054302Z-dinoflagellate-apical-groove-audit/review.yaml
  locator: Historical complete paired observation and deterministic Markdown equivalence
  accessed_at: '2026-11-04T05:32:33.011043Z'
  snapshot_sha256: f605131be90cc3b54b26cfafe3e17d6268979c5937a227f25411cfdf18e25971
  summary: Original qualified verdict, all scientific assessments/evidence scopes
    and empty findings/actions independently reassessed; original corpus runs remain
    historical, not current execution.
  support: supports
- evidence_id: plaque-original-0-md
  kind: prior_review
  reference: reviews/structured/20261022T054302Z-dinoflagellate-apical-groove-audit/review.md
  locator: Historical complete paired observation and deterministic Markdown equivalence
  accessed_at: '2026-11-04T05:32:33.011043Z'
  snapshot_sha256: 85ad2cd90c206a93f1a5e75373e6696d81e3ffdcdca0f14040dec36cad44ac71
  summary: Original qualified verdict, all scientific assessments/evidence scopes
    and empty findings/actions independently reassessed; original corpus runs remain
    historical, not current execution.
  support: supports
- evidence_id: plaque-current-1
  kind: record_content
  reference: data/structures/other/dinoflagellate_apical_horn.yaml
  locator: Entire maintained record at frozen source dbdd66f36d1363c94eab2c58305c2f58a68baf09
  accessed_at: '2026-11-04T05:32:33.011043Z'
  snapshot_sha256: 77b2ec19b71236a91786a44611abcc34eb6a7e927763f6ff641f2c879813c344
  summary: Complete definition, hierarchy, taxonomic distribution, evidence, graph,
    discussions and history independently read. Original target bytes unchanged. No
    molecular components, protein examples, measurements or maintained images asserted.
  support: supports
- evidence_id: plaque-original-1-yaml
  kind: prior_review
  reference: reviews/structured/20261022T054304Z-dinoflagellate-apical-horn-audit/review.yaml
  locator: Historical complete paired observation and deterministic Markdown equivalence
  accessed_at: '2026-11-04T05:32:33.011043Z'
  snapshot_sha256: f6ee1ed0e9d0154aa075463a0c6b5407216fc6b6d595cf5c87d47aa15073e6fe
  summary: Original qualified verdict, all scientific assessments/evidence scopes
    and empty findings/actions independently reassessed; original corpus runs remain
    historical, not current execution.
  support: supports
- evidence_id: plaque-original-1-md
  kind: prior_review
  reference: reviews/structured/20261022T054304Z-dinoflagellate-apical-horn-audit/review.md
  locator: Historical complete paired observation and deterministic Markdown equivalence
  accessed_at: '2026-11-04T05:32:33.011043Z'
  snapshot_sha256: e145632bb665547354f060e0b589d40245ae9127757a69b1e3c45dece0e03c0b
  summary: Original qualified verdict, all scientific assessments/evidence scopes
    and empty findings/actions independently reassessed; original corpus runs remain
    historical, not current execution.
  support: supports
- evidence_id: plaque-current-2
  kind: record_content
  reference: data/structures/other/dinoflagellate_cingulum.yaml
  locator: Entire maintained record at frozen source dbdd66f36d1363c94eab2c58305c2f58a68baf09
  accessed_at: '2026-11-04T05:32:33.011043Z'
  snapshot_sha256: c29822ebb0e810421c4516a4db5b8e6d648739e5c563e491d584850a65011513
  summary: Complete definition, hierarchy, taxonomic distribution, evidence, graph,
    discussions and history independently read. Original target bytes unchanged. No
    molecular components, protein examples, measurements or maintained images asserted.
  support: supports
- evidence_id: plaque-original-2-yaml
  kind: prior_review
  reference: reviews/structured/20261022T054304Z-dinoflagellate-cingulum-audit/review.yaml
  locator: Historical complete paired observation and deterministic Markdown equivalence
  accessed_at: '2026-11-04T05:32:33.011043Z'
  snapshot_sha256: 9f2327be51767cbf946ef143bdace86d855ba02f5ec8e15df34dc62440399d7f
  summary: Original qualified verdict, all scientific assessments/evidence scopes
    and empty findings/actions independently reassessed; original corpus runs remain
    historical, not current execution.
  support: supports
- evidence_id: plaque-original-2-md
  kind: prior_review
  reference: reviews/structured/20261022T054304Z-dinoflagellate-cingulum-audit/review.md
  locator: Historical complete paired observation and deterministic Markdown equivalence
  accessed_at: '2026-11-04T05:32:33.011043Z'
  snapshot_sha256: a7f33b7eaf4fbf0fe6e356d789dd3cc7bfa72ef343d3c808afb98507e70f81fc
  summary: Original qualified verdict, all scientific assessments/evidence scopes
    and empty findings/actions independently reassessed; original corpus runs remain
    historical, not current execution.
  support: supports
- evidence_id: plaque-current-3
  kind: record_content
  reference: data/structures/other/dinoflagellate_epicone.yaml
  locator: Entire maintained record at frozen source dbdd66f36d1363c94eab2c58305c2f58a68baf09
  accessed_at: '2026-11-04T05:32:33.011043Z'
  snapshot_sha256: 30e41a70bae04d4698b3b0bc40226fb51727a9f8664c4031c3ae8145216dfcdd
  summary: Complete definition, hierarchy, taxonomic distribution, evidence, graph,
    discussions and history independently read. Original target bytes unchanged. No
    molecular components, protein examples, measurements or maintained images asserted.
  support: supports
- evidence_id: plaque-original-3-yaml
  kind: prior_review
  reference: reviews/structured/20261022T054305Z-dinoflagellate-epicone-audit/review.yaml
  locator: Historical complete paired observation and deterministic Markdown equivalence
  accessed_at: '2026-11-04T05:32:33.011043Z'
  snapshot_sha256: 6d966b5dd38100535f6632d4ac31fd436f690a2b0d0acca9f7c1d6466fa88579
  summary: Original qualified verdict, all scientific assessments/evidence scopes
    and empty findings/actions independently reassessed; original corpus runs remain
    historical, not current execution.
  support: supports
- evidence_id: plaque-original-3-md
  kind: prior_review
  reference: reviews/structured/20261022T054305Z-dinoflagellate-epicone-audit/review.md
  locator: Historical complete paired observation and deterministic Markdown equivalence
  accessed_at: '2026-11-04T05:32:33.011043Z'
  snapshot_sha256: 711b0594884de3b37bcc47f35e8e2539c0c8e0ef7368d61c8189cbc5f87d7535
  summary: Original qualified verdict, all scientific assessments/evidence scopes
    and empty findings/actions independently reassessed; original corpus runs remain
    historical, not current execution.
  support: supports
- evidence_id: plaque-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Frozen local policy/schema applied
  accessed_at: '2026-11-04T05:32:33.011043Z'
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
  summary: Exact structure and mereology, source scope, optional inventory and append-only
    discussion/history rules.
  support: supports
- evidence_id: plaque-schema
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Frozen local policy/schema applied
  accessed_at: '2026-11-04T05:32:33.011043Z'
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
  summary: Subcellular region, hierarchy/parthood, descriptive graph, taxonomic presence
    and evidence semantics.
  support: supports
- evidence_id: plaque-review-skill
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Frozen local policy/schema applied
  accessed_at: '2026-11-04T05:32:33.011043Z'
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
  summary: Native molecular/pathway structured-source trigger assessed from full record,
    not mandatory optional fields.
  support: supports
- evidence_id: plaque-review-profile
  kind: authority
  reference: docs/record-review-profile.md
  locator: Frozen local policy/schema applied
  accessed_at: '2026-11-04T05:32:33.011043Z'
  snapshot_sha256: 6a49c8d35f0a94082a9ad0b8bd8c6a929d85de8339141955f3779bd7ab0eb7e4
  summary: Issue-bearing immutable batch successor; clean scientific observations
    are not fabricated curation findings.
  support: supports
- evidence_id: plaque-review-schema
  kind: authority
  reference: schema/record_review.yaml
  locator: Frozen local policy/schema applied
  accessed_at: '2026-11-04T05:32:33.011043Z'
  snapshot_sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
  summary: Native evidence kinds/assessment enums and immutable lineage contract.
  support: supports
- evidence_id: plaque-checklist
  kind: authority
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Frozen local policy/schema applied
  accessed_at: '2026-11-04T05:32:33.011043Z'
  snapshot_sha256: e6b9e4b16a58c54402bed7bbee2c8b94a91d37562e8b0ee8b94ff0c829184a70
  summary: Complete field-by-field bounded review; unknown molecular assembly is not
    automatic defect.
  support: supports
- evidence_id: plaque-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Frozen local policy/schema applied
  accessed_at: '2026-11-04T05:32:33.011043Z'
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
  summary: NONMECHANISTIC physical/topological graphs need supported exact edges,
    not invented mechanism.
  support: supports
- evidence_id: plaque-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097685,GO:0097686,GO:0097611,GO:0097613,GO:0097683,GO:0097614,GO:0097610,GO:0110165
  locator: All requested identity/status/definition/synonyms/xrefs and only relevant
    direct typed children; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-plaque/go.raw
  accessed_at: '2026-11-04T05:29:09.165246Z'
  snapshot_sha256: 728d23e8f48df235e1d286d42796040aeef04f727c1da32f3bab38c5d3285935
  summary: Eight active exact identities, definitions and synonyms agree. Parent children
    directly expose groove/cingulum is_a surface furrow; epicone is_a cellular anatomical
    structure; apex/groove part_of epicone; horn is_a apex. No unrelated GO0110165
    child is judged.
  support: supports
- evidence_id: plaque-go-0097685-constraints
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097685/constraints
  locator: Focal taxonConstraints and identity only; blacklist entries are not constituent
    evidence; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-plaque/go-0097685-constraints.raw
  accessed_at: '2026-11-04T05:29:08.999885Z'
  snapshot_sha256: dd75a85b0ec0d3a82a85d6b6a5e23171598de4ecbc57b9dd7fa33ce71034f599
  summary: Focal only_in_taxon explicitly restricts this structure to NCBITaxon2864
    Dinophyceae, without universal presence or a numerical census. Inherited blacklist
    annotations are not interpreted as structure proteins.
  support: supports
- evidence_id: plaque-go-0097685-history
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097685/history
  locator: Complete focal history array; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-plaque/go-0097685-history.raw
  accessed_at: '2026-11-04T05:29:08.919142Z'
  snapshot_sha256: aec2f55dd69f3539e73da407ce409741edae2b3cbd7f23d7b61131e2e1c6e875
  summary: Complete dated term/definition/relation/synonym history supports the current
    declared relations; uninformative Bad taxon ID rendering does not replace explicit
    constraints endpoint.
  support: supports
- evidence_id: plaque-go-0097686-constraints
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097686/constraints
  locator: Focal taxonConstraints and identity only; blacklist entries are not constituent
    evidence; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-plaque/go-0097686-constraints.raw
  accessed_at: '2026-11-04T05:29:08.771798Z'
  snapshot_sha256: 3c4909bf450416ba64bc99b43e7d4bedc81411c21baa3d8b8de77701437940bf
  summary: Focal only_in_taxon explicitly restricts this structure to NCBITaxon2864
    Dinophyceae, without universal presence or a numerical census. Inherited blacklist
    annotations are not interpreted as structure proteins.
  support: supports
- evidence_id: plaque-go-0097686-history
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097686/history
  locator: Complete focal history array; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-plaque/go-0097686-history.raw
  accessed_at: '2026-11-04T05:29:08.997611Z'
  snapshot_sha256: 6e909ec7e939affc3ac5ffd4fbc7919c4b7977ffc05a5a84614399da6d891b8e
  summary: Complete dated term/definition/relation/synonym history supports the current
    declared relations; uninformative Bad taxon ID rendering does not replace explicit
    constraints endpoint.
  support: supports
- evidence_id: plaque-go-0097611-constraints
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097611/constraints
  locator: Focal taxonConstraints and identity only; blacklist entries are not constituent
    evidence; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-plaque/go-0097611-constraints.raw
  accessed_at: '2026-11-04T05:29:08.893088Z'
  snapshot_sha256: 3caa2c01ede1c3988f7142533fd7437838287042de1d59031c3b2e819d53c1b3
  summary: Focal only_in_taxon explicitly restricts this structure to NCBITaxon2864
    Dinophyceae, without universal presence or a numerical census. Inherited blacklist
    annotations are not interpreted as structure proteins.
  support: supports
- evidence_id: plaque-go-0097611-history
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097611/history
  locator: Complete focal history array; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-plaque/go-0097611-history.raw
  accessed_at: '2026-11-04T05:29:08.979300Z'
  snapshot_sha256: 1fe8204133b5321bd675ef447c1489b9bf6079cae61f3518c36413e29d008b63
  summary: Complete dated term/definition/relation/synonym history supports the current
    declared relations; uninformative Bad taxon ID rendering does not replace explicit
    constraints endpoint.
  support: supports
- evidence_id: plaque-go-0097613-constraints
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097613/constraints
  locator: Focal taxonConstraints and identity only; blacklist entries are not constituent
    evidence; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-plaque/go-0097613-constraints.raw
  accessed_at: '2026-11-04T05:29:08.919081Z'
  snapshot_sha256: 479e041e549bb29e20b476b031fa9087d3223eb477f1dad0ab7555589d503e7b
  summary: Focal only_in_taxon explicitly restricts this structure to NCBITaxon2864
    Dinophyceae, without universal presence or a numerical census. Inherited blacklist
    annotations are not interpreted as structure proteins.
  support: supports
- evidence_id: plaque-go-0097613-history
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097613/history
  locator: Complete focal history array; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-plaque/go-0097613-history.raw
  accessed_at: '2026-11-04T05:29:09.381141Z'
  snapshot_sha256: d80b1790f725e9404b5e47d5f57caaa0a5717c67929bd95b1c17dadd753a0757
  summary: Complete dated term/definition/relation/synonym history supports the current
    declared relations; uninformative Bad taxon ID rendering does not replace explicit
    constraints endpoint.
  support: supports
- evidence_id: plaque-horn-epicone-path
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097686/paths/GO:0097613
  locator: Complete one-path two-edge result; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-plaque/horn-epicone-path.raw
  accessed_at: '2026-11-04T05:29:09.620827Z'
  snapshot_sha256: 0203e6be54d71ffa7fe810e8f5e431311cd9ff2c73a3f084ab3271bf6a814d68
  summary: The sole exact path is GO0097686 is_a GO0097683 then part_of GO0097613.
    Horn containment is inherited via the apex; no direct independent GO horn-to-epicone
    edge is claimed.
  support: supports
- evidence_id: plaque-tax-2864
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2864
  locator: Complete native scientificName/rank/lineage/aliases; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-plaque/tax-2864.raw
  accessed_at: '2026-11-04T05:29:09.572890Z'
  snapshot_sha256: 9054e3d0f5c26df06f9c5ed034d064c96b9ba37ed54473ad6669f9dcb699026b
  summary: Native class2864 is Dinophyceae, with dinoflagellate/Dinophyta aliases
    and eukaryote/Sar/Alveolata lineage; taxon identity is not prevalence.
  support: supports
- evidence_id: plaque-tax-77300
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/77300
  locator: Complete native species identity/name/lineage/aliases; actual response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-plaque/tax-77300.raw
  accessed_at: '2026-11-04T05:29:09.701882Z'
  snapshot_sha256: 396e3ce6c4259f21145716995c5bc20dc469cf291b5941c925c0a258ae50ed35
  summary: Native species77300 is Margalefidinium polykrikoides and explicitly retains
    Cochlodinium polykrikoides synonym; no strain identifier is invented.
  support: supports
- evidence_id: plaque-iwataki2010-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A20561119+AND+SRC%3AMED&format=json&resultType=core&pageSize=5
  locator: Exact PMID matched native identity/authors/year/DOI and complete primary
    abstract; no full Methods/body/images; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-plaque/iwataki2010-meta.raw
  accessed_at: '2026-11-04T05:29:09.609734Z'
  snapshot_sha256: 752957b9c869a701b60dd8ba1d498136bd7c794c51ab2f576e3d45192b625db4
  summary: Unique MED20561119/DOI10.1111/j.1550-7408.2010.00491.x is Iwataki,Hansen,Moestrup,Matsuoka2010.
    Complete primary abstract explicitly describes U-shaped groove connected to anterior
    sulcal extension on dorsal epicone. Flagellar/eyespot results are not promoted
    to groove-specific constituents.
  support: supports
- evidence_id: plaque-gomez2017-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.hal.2017.01.008%22&format=json&resultType=core&pageSize=5
  locator: Exact DOI query one MED record; identity/authors/year and complete primary
    abstract; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-plaque/gomez2017-meta.raw
  accessed_at: '2026-11-04T05:29:09.910574Z'
  snapshot_sha256: 0b1a18f12e1e6ebd2756470b24edfeba1f511f3027b237c29d4b6843fbaae4a6
  summary: Unique MED28366398/DOI10.1016/j.hal.2017.01.008 is Gomez,Richlen,Anderson2017;
    complete abstract supports formal Margalefidinium transfer distinct from Iwataki
    morphology evidence.
  support: supports
- evidence_id: plaque-taylor1980-meta
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A7002229+AND+SRC%3AMED&format=json&resultType=core&pageSize=5
  locator: Complete indexed secondary-review abstract and metadata; no article body;
    actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-plaque/taylor1980-meta.raw
  accessed_at: '2026-11-04T05:29:09.730491Z'
  snapshot_sha256: c05e15563c6a6072220755d9e282e4bb9da8073c1a70737203542882344bb446
  summary: Unique MED7002229/DOI10.1016/0303-2647(80)90006-4 is Taylor1980 On dinoflagellate
    evolution, Biosystems13:65-108. Secondary review abstract is broad evolutionary
    synthesis, used for exact bibliography only, not independent detailed horn/cingulum
    anatomy.
  support: context_only
- evidence_id: plaque-gomez2017-s3
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC6276129.1/PMC6276129.1.xml
  locator: Front identity/permissions; complete MethodsS3,ResultsS8 includingS9,TaxonomyS10/allnestedsubsections,ConclusionsS30,Table1
    andFig3/4/5text captions; no pixels/supplements; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-plaque/gomez2017-s3.raw
  accessed_at: '2026-11-04T05:29:10.170408Z'
  snapshot_sha256: 2cdf87667ad55afffee10f73f34c636e62e421105d27e4c065d329081352e522
  summary: Genuine JATS formally diagnoses U-shaped dorsal episomal groove and establishes
    Margalefidinium polykrikoides from Cochlodinium. Its own Puerto Rico LM did not
    visualize groove/anterior sulcal extension; SEM details were obscured by filamentous
    material. These specimens are not substituted for2010 ultrastructure. Figure5
    is redrawn morphology; no pixel measurements claimed.
  support: supports
- evidence_id: plaque-tol-orientation
  kind: authority
  reference: https://tolweb.org/articles/?article_id=4756
  locator: Complete main orientation prose, overview caption, authorship/date/text
    licence; no pixels; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-plaque/tol-orientation.raw
  accessed_at: '2026-11-04T05:29:09.292935Z'
  snapshot_sha256: 406916e9c83d51de4ec6f7dee8a7b129c6ab8e1781a65a3ec28d83734970370e
  summary: Hoppenrath2008 expert orientation note distinguishes anterior episome/epicone/epitheca
    and posterior counterparts relative to cingulum, apex at anterior tip and possible
    athecate apical groove. Terms are not universally exact synonyms. TextCCBY-NC3.0;
    image rights are separate and no images used.
  support: supports
- evidence_id: plaque-tol-dinoflagellates
  kind: authority
  reference: https://tolweb.org/Dinoflagellates/2445
  locator: Introduction and opening Characteristics through Flagella/desmokont exception,
    associated text captions; later cell biology not relied on; no pixels; actual
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-plaque/tol-dinoflagellates.raw
  accessed_at: '2026-11-04T05:29:09.568708Z'
  snapshot_sha256: 5957a1388500247ac00f15d5ffaccc4df3ee19b07daf5986bd7a96fa5fc3df47
  summary: Expert Characteristics/Flagella account places transverse flagellum in
    cingulum and longitudinal flagellum in sulcus; desmokont flagellation lacks these
    grooves. This supports VARIABLE scope, not a universal groove or molecular inventory.
  support: supports
- evidence_id: plaque-iwataki2010-publisher
  kind: validation
  reference: https://onlinelibrary.wiley.com/doi/full/10.1111/j.1550-7408.2010.00491.x
  locator: HTTP status, response readability and blocked page only; actual response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-plaque/iwataki2010-publisher.raw
  accessed_at: '2026-11-04T05:29:09.827108Z'
  snapshot_sha256: 3537cd90fe4e522417a3a0cb210e61853d3843bdafe8f8655feb294078e889ec
  summary: Actual fresh publisher route returnedHTTP403. No article body, Methods,
    original figure pixels or experimental strain details certified by this response.
    The corresponding abstract/authority and historical failure remain distinct.
  support: context_only
- evidence_id: plaque-taylor1980-publisher
  kind: validation
  reference: https://www.sciencedirect.com/science/article/pii/0303264780900064
  locator: HTTP status, response readability and blocked page only; actual response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-plaque/taylor1980-publisher.raw
  accessed_at: '2026-11-04T05:29:09.894467Z'
  snapshot_sha256: 1d1b615156fab1e5f419ce955caed229134965fdfbec54355a0ec2ce230cd872
  summary: Actual fresh publisher route returnedHTTP403. No article body, Methods,
    original figure pixels or experimental strain details certified by this response.
    The corresponding abstract/authority and historical failure remain distinct.
  support: context_only
- evidence_id: plaque-catalogue
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Complete same-PR fresh official catalogue independently reread; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/catalogue.raw
  accessed_at: '2026-11-04T05:28:42.917849Z'
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  summary: Complete20 organism rows/28 organism-dataset pairs independently read;
    no Dinophyceae/Margalefidinium/Cochlodinium coverage. These records already have
    genuine morphology-only applicability exclusions.
  support: context_only
- evidence_id: plaque-catalogue-search
  kind: search
  reference: https://imodulondb.org/api/datasets
  locator: Complete same-PR fresh official catalogue independently reread; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-microtubule/catalogue.raw
  accessed_at: '2026-11-04T05:28:42.917849Z'
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  summary: Bounded catalogue coverage screen has no matching natural host; not biological
    absence and no unrelated bacterial downstream query.
  support: context_only
  search_scope: Official iModulonDB /api/datasets, all20organism rows/28organism-dataset
    pairs at 2026-11-04T05:28:42.917849Z; exact/lexical Dinophyceae,dinoflagellate,Margalefidinium,polykrikoides,Cochlodinium.
    No other database/strain scope or downstream module search asserted.
- evidence_id: plaque-historical-adapter-unavailable
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Original runner availability receipt only; no fresh invocation
  accessed_at: '2026-11-03T00:49:00.863225Z'
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  summary: Historical2026-11-03T00:49Z exit1 PermissionError reading configured pyvenv.cfg;
    not a current scientific check or completed runner invocation. Fresh source catalogue
    inspection separately reported.
  support: context_only
- evidence_id: plaque-original-current-validation
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-plaque/originals-current-proof.json
  locator: Four original native validate/render pairs;52historical input occurrences;47current
    source/worktree hashes
  accessed_at: '2026-11-04T05:28:57.490598Z'
  snapshot_sha256: c46fe41d3c00b49cbe4a008b4aa6be050565696a931a2d025a355339ba769285
  summary: All original YAML validates and Markdown renders byte-identically. Historical
    inputs match their exact source commit, resolving CLAUDE symlink. All four targets
    are unchanged; no stale science refresh or prior finding disposition required.
  support: supports
- evidence_id: plaque-historical-failed-access-0
  kind: validation
  reference: reviews/structured/20261022T054302Z-dinoflagellate-apical-groove-audit/review.yaml
  locator: evidence#root50-iwataki2010-publisher; historical responseSHA 792cc7833ab90870c2e3df1a8ab44e09ea0506fe4fe02c2542d238b991b4eda3;
    originalaccess 2026-10-22T05:31:12.422043Z
  accessed_at: '2026-11-04T05:32:33.011043Z'
  snapshot_sha256: f605131be90cc3b54b26cfafe3e17d6268979c5937a227f25411cfdf18e25971
  summary: The immutable original labels a disclosed403response database/context_only.
    Correct successor classification is validation/context_only; preserve original
    request/time/failure. Original response bytes are not independently refetched
    here and later access does not erase historical failure.
  support: context_only
- evidence_id: plaque-historical-failed-access-1
  kind: validation
  reference: reviews/structured/20261022T054304Z-dinoflagellate-apical-horn-audit/review.yaml
  locator: evidence#root50-taylor1980-publisher; historical responseSHA 14dd40deb21794994e8cbc95036a781eb7e7b41de1fbcc216c4af476bd5948f7;
    originalaccess 2026-10-21T09:08:56.074246Z
  accessed_at: '2026-11-04T05:32:33.011043Z'
  snapshot_sha256: f6ee1ed0e9d0154aa075463a0c6b5407216fc6b6d595cf5c87d47aa15073e6fe
  summary: The immutable original labels a disclosed403response database/context_only.
    Correct successor classification is validation/context_only; preserve original
    request/time/failure. Original response bytes are not independently refetched
    here and later access does not erase historical failure.
  support: context_only
- evidence_id: plaque-historical-failed-access-2
  kind: validation
  reference: reviews/structured/20261022T054304Z-dinoflagellate-cingulum-audit/review.yaml
  locator: evidence#root50-taylor1980-publisher; historical responseSHA 14dd40deb21794994e8cbc95036a781eb7e7b41de1fbcc216c4af476bd5948f7;
    originalaccess 2026-10-21T09:08:56.074246Z
  accessed_at: '2026-11-04T05:32:33.011043Z'
  snapshot_sha256: 9f2327be51767cbf946ef143bdace86d855ba02f5ec8e15df34dc62440399d7f
  summary: The immutable original labels a disclosed403response database/context_only.
    Correct successor classification is validation/context_only; preserve original
    request/time/failure. Original response bytes are not independently refetched
    here and later access does not erase historical failure.
  support: context_only
- evidence_id: plaque-native-dinoflagellate_apical_groove-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_apical_groove-uniprot-verify-receipt.json
  locator: Actual ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/dinoflagellate_apical_groove.yaml',
    '--verify']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_apical_groove-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T05:27:57.521404Z'
  snapshot_sha256: fdd2a4b45196574453cc52fd6c3d42c3d3fb054be0f2bf1c4f1b58dee0210485
  summary: Actual current-source command exit0; zero protein_examples and zero typedGENE_OR_PROTEINnodes
    independently confirmed. Empty-inventory success does not certify molecular completeness.
  support: supports
- evidence_id: plaque-native-dinoflagellate_apical_groove-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_apical_groove-uniprot-causal-receipt.json
  locator: Actual ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/dinoflagellate_apical_groove.yaml',
    '--causal-graphs']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_apical_groove-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-04T05:27:57.951681Z'
  snapshot_sha256: b7babe2b9f7716c97398fe3cc12f2827c22ae171cc6c95ee8fda2e80ec7dc728
  summary: Actual current-source command exit0; zero protein_examples and zero typedGENE_OR_PROTEINnodes
    independently confirmed. Empty-inventory success does not certify molecular completeness.
  support: supports
- evidence_id: plaque-native-dinoflagellate_apical_horn-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_apical_horn-uniprot-verify-receipt.json
  locator: Actual ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/dinoflagellate_apical_horn.yaml',
    '--verify']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_apical_horn-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T05:27:58.384636Z'
  snapshot_sha256: acca7d23aa0b5d865e1d9715ca71104fc8b6c63aa8cab6e24fbe323a3aacb5f9
  summary: Actual current-source command exit0; zero protein_examples and zero typedGENE_OR_PROTEINnodes
    independently confirmed. Empty-inventory success does not certify molecular completeness.
  support: supports
- evidence_id: plaque-native-dinoflagellate_apical_horn-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_apical_horn-uniprot-causal-receipt.json
  locator: Actual ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/dinoflagellate_apical_horn.yaml',
    '--causal-graphs']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_apical_horn-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-04T05:27:58.832599Z'
  snapshot_sha256: 9720f9206cbf138e0a1db4ac4727aea41a8671eaf80a923b04ad633eae061ae1
  summary: Actual current-source command exit0; zero protein_examples and zero typedGENE_OR_PROTEINnodes
    independently confirmed. Empty-inventory success does not certify molecular completeness.
  support: supports
- evidence_id: plaque-native-dinoflagellate_cingulum-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_cingulum-uniprot-verify-receipt.json
  locator: Actual ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/dinoflagellate_cingulum.yaml',
    '--verify']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_cingulum-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T05:27:59.280025Z'
  snapshot_sha256: 0000088ffbf8062816590b4688308ec2d9a47bd42bd3c7d49b10d780317ae3c5
  summary: Actual current-source command exit0; zero protein_examples and zero typedGENE_OR_PROTEINnodes
    independently confirmed. Empty-inventory success does not certify molecular completeness.
  support: supports
- evidence_id: plaque-native-dinoflagellate_cingulum-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_cingulum-uniprot-causal-receipt.json
  locator: Actual ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/dinoflagellate_cingulum.yaml',
    '--causal-graphs']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_cingulum-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-04T05:27:59.725230Z'
  snapshot_sha256: c8e844f29cbc6cb1c19aa0d589ddbfaa4e00dab1e7d3aaefe842b676675abab2
  summary: Actual current-source command exit0; zero protein_examples and zero typedGENE_OR_PROTEINnodes
    independently confirmed. Empty-inventory success does not certify molecular completeness.
  support: supports
- evidence_id: plaque-native-dinoflagellate_epicone-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_epicone-uniprot-verify-receipt.json
  locator: Actual ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/dinoflagellate_epicone.yaml',
    '--verify']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_epicone-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T05:28:00.188188Z'
  snapshot_sha256: d5955a946acad2dbec03052355be925798bc05b824d11579cb1b231c1bf18bd3
  summary: Actual current-source command exit0; zero protein_examples and zero typedGENE_OR_PROTEINnodes
    independently confirmed. Empty-inventory success does not certify molecular completeness.
  support: supports
- evidence_id: plaque-native-dinoflagellate_epicone-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_epicone-uniprot-causal-receipt.json
  locator: Actual ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/dinoflagellate_epicone.yaml',
    '--causal-graphs']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_epicone-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-04T05:28:00.641233Z'
  snapshot_sha256: 8968421a9f02f4f39dbff20a89acb4a4191b1e842a5d79202cfdf2204457dbfe
  summary: Actual current-source command exit0; zero protein_examples and zero typedGENE_OR_PROTEINnodes
    independently confirmed. Empty-inventory success does not certify molecular completeness.
  support: supports
- evidence_id: septin-review-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Full-record evidence and structured-source trigger
  summary: Actual positive molecular/pathway claims trigger structured-source coverage;
    genuine physical morphology with no such assertions can be excluded. Empty optional
    inventories do not establish defects.
  accessed_at: '2026-11-04T05:33:32.048325Z'
  support: supports
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: septin-curation-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Exact identity, source scope and append-only Discussions
  summary: Preserve dated rationale/history. Source-specific evidence supports its
    narrow claim; optional components, images or numerical properties are not mandatory
    fill targets.
  accessed_at: '2026-11-04T05:33:32.048325Z'
  support: supports
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
- evidence_id: septin-schema-policy
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Identity, synonym, PresenceEnum, graph and optional component fields
  summary: SUBCELLULAR_REGION and OTHER permit these anatomical entities. VARIABLE
    is not universal presence; descriptive FUNCTION/NONMECHANISTIC does not establish
    formation necessity.
  accessed_at: '2026-11-04T05:33:32.048325Z'
  support: supports
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: septin-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Edge evidence, boundaries and descriptive scope
  summary: Exact class, parthood and spatial relations must remain distinct. A morphology
    graph may deliberately exclude molecular mechanism without a missing-step defect.
  accessed_at: '2026-11-04T05:33:32.048325Z'
  support: supports
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: septin-literature-policy
  kind: authority
  reference: .claude/skills/literature-evidence/SKILL.md
  locator: Source access and actual read tiers
  summary: Metadata/abstract, authored authority text, complete primary bodies, captions/pixels
    and failed retrievals are distinct evidence scopes.
  accessed_at: '2026-11-04T05:33:32.048325Z'
  support: supports
  snapshot_sha256: f7c3c594b5fb2cd7d4d700844fce3b97c91cc382d4fdca8b2e2a96cf16abd41b
- evidence_id: septin-review-schema
  kind: authority
  reference: schema/record_review.yaml
  locator: ReviewEvidence kinds and finding lineage
  summary: Failed HTTP access is validation context, not database scientific content.
    Exact predecessor references retain repository, review_id and finding_id.
  accessed_at: '2026-11-04T05:33:32.048325Z'
  support: supports
  snapshot_sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
- evidence_id: septin-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097614,GO:0097618,GO:0097612,GO:0097684,GO:0097611,GO:0097613,GO:0097610,GO:0110165
  locator: All eight requested active IDs/names/definitions/xrefs/synonyms/comments
    and relevant typed child links; not all unrelated GO0110165 descendants
  summary: GO0097614 is the posterior hypocone; GO0097618 is the antapex-reaching,
    bilobed-hypocone sulcus subtype; GO0097612 is the ventral furrow partially housing
    the longitudinal flagellum and intersecting the cingulum. Typed parents and antapex
    parthood match. Sulcus definition.xrefs cites PMID20561119, notch cites PMID7002229.
    GO0097684 retains anterior wording in conflict with the posterior notch definition
    and expert orientation; this error is not copied into the three targets.
  accessed_at: '2026-11-04T05:30:08.121432Z'
  support: supports
  snapshot_sha256: e3cb4fd2db22a3acdb0b7e517b3364982243c26cc20c609f4447a79e85780aa0
- evidence_id: septin-go-0097614-history
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097614/history
  locator: Complete current term/history array, including direct RELATION and DEFINITION
    events
  summary: History confirms replacement of obsolete cell-part parent by GO0110165
    in2019, posterior definition and related hyposome/hypotheca synonyms. Historical
    Bad taxon ID display entries are not treated as current taxonomic constraints
    or scientific refutation.
  accessed_at: '2026-11-04T05:30:07.940792Z'
  support: supports
  snapshot_sha256: 2f5d04454440a491f3c86ad9b45340bf7cbcfeb49531ee8e9ab13e44387fcaa7
- evidence_id: septin-go-0097614-constraints
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097614/constraints
  locator: Exact current taxonConstraints entry; unrelated inherited protein-annotation
    blacklist not used
  summary: Exact term only_in_taxon NCBITaxon2864 Dinophyceae. This restriction identifies
    allowed host lineage, not a class-wide prevalence measurement or a localized protein
    inventory.
  accessed_at: '2026-11-04T05:30:08.034731Z'
  support: supports
  snapshot_sha256: d93f8dd3967d6aa81ea0a9b50aaaa97013e10f3039acc8854cead11d23f972c5
- evidence_id: septin-go-0097618-history
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097618/history
  locator: Complete current term/history array, including direct RELATION and DEFINITION
    events
  summary: History confirms direct is_a GO0097612 and posterior-reaching/bilobed morphology.
    Historical Bad taxon ID display entries are not treated as current taxonomic constraints
    or scientific refutation.
  accessed_at: '2026-11-04T05:30:08.041871Z'
  support: supports
  snapshot_sha256: 48fd054344ee485d39a29a69d94bb1b351e8f17308d0e716cc3dfc87f9c3289b
- evidence_id: septin-go-0097618-constraints
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097618/constraints
  locator: Exact current taxonConstraints entry; unrelated inherited protein-annotation
    blacklist not used
  summary: Exact term only_in_taxon NCBITaxon2864 Dinophyceae. This restriction identifies
    allowed host lineage, not a class-wide prevalence measurement or a localized protein
    inventory.
  accessed_at: '2026-11-04T05:30:07.938393Z'
  support: supports
  snapshot_sha256: 33e619b672dc492461b1ba4560aed8f3c88e15fd6dc4890bedafffe748648f50
- evidence_id: septin-go-0097612-history
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097612/history
  locator: Complete current term/history array, including direct RELATION and DEFINITION
    events
  summary: History confirms direct is_a GO0097610 and ventral flagellum-housing/intersecting
    definition. Historical Bad taxon ID display entries are not treated as current
    taxonomic constraints or scientific refutation.
  accessed_at: '2026-11-04T05:30:07.824516Z'
  support: supports
  snapshot_sha256: 5c37e02973e4e7bab017cbf7beb545f918c71b4d0145378115c5adfa46ccaaaf
- evidence_id: septin-go-0097612-constraints
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097612/constraints
  locator: Exact current taxonConstraints entry; unrelated inherited protein-annotation
    blacklist not used
  summary: Exact term only_in_taxon NCBITaxon2864 Dinophyceae. This restriction identifies
    allowed host lineage, not a class-wide prevalence measurement or a localized protein
    inventory.
  accessed_at: '2026-11-04T05:30:07.950229Z'
  support: supports
  snapshot_sha256: 5d98ceabe5d6022237b58ed4870aceae0d91c63ad581c042b55b825c977cd468
- evidence_id: septin-tax-2864
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2864
  locator: Complete native taxId/scientificName/rank/lineage/otherNames response,
    independently read from fresh peer packet
  summary: ENA2864 is class Dinophyceae with dinoflagellate common name and Dinophyta/Dinoflagellata
    aliases. Identity and rank verified; no numerical frequency inferred.
  accessed_at: '2026-11-04T05:29:09.572890Z'
  support: supports
  snapshot_sha256: 9054e3d0f5c26df06f9c5ed034d064c96b9ba37ed54473ad6669f9dcb699026b
- evidence_id: septin-tol-orientation
  kind: authority
  reference: https://tolweb.org/articles/?article_id=4756
  locator: Complete authored main text, overview caption and About This Page attribution/text
    licence; no image pixels
  summary: Mona Hoppenrath2008 divides the motile cell at the cingulum into upper
    episome and lower hyposome; hypocone is athecate and hypotheca thecate terminology.
    Antapex is the bottom of the hyposome; below-cingulum is posterior; sulcus side
    is ventral. Expert secondary terminology, not a new formation experiment. Text
    CC-BY-NC3.0 does not confer identical rights on each image; no images reused.
  accessed_at: '2026-11-04T05:29:09.292935Z'
  support: supports
  snapshot_sha256: 406916e9c83d51de4ec6f7dee8a7b129c6ab8e1781a65a3ec28d83734970370e
- evidence_id: septin-tol-dinoflagellates
  kind: authority
  reference: https://tolweb.org/Dinoflagellates/2445
  locator: Authorship, Introduction morphology diversity, Characteristics opening
    and complete Flagella subsection with Figs1–8 captions; later biological sections
    not used for target assertions; no pixels
  summary: Hoppenrath/Saldarriaga state that the longitudinal flagellum lies in the
    sulcus while its distal portion projects behind the cell; desmokont Prorocentrum
    flagella are not groove-associated. Supports qualified anatomical occurrence,
    not universal prevalence or a constituent/formation assay. Broad whole-cell molecular
    claims elsewhere on the page are not imported into these regional records.
  accessed_at: '2026-11-04T05:29:09.568708Z'
  support: supports
  snapshot_sha256: 5957a1388500247ac00f15d5ffaccc4df3ee19b07daf5986bd7a96fa5fc3df47
- evidence_id: septin-taylor1980-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A7002229+AND+SRC%3AMED&format=json&resultType=core&pageSize=5
  locator: Unique MED title/authors/year/DOI/access-route flags and complete abstractText;
    fresh peer receipt independently read
  summary: Taylor FJ1980, On dinoflagellate evolution, Biosystems13:65–108, DOI10.1016/0303-2647(80)90006-4,
    is a secondary review. Complete abstract is broad evolutionary synthesis, not
    a direct generic-notch experiment. This verifies current bibliography, not every
    attached anatomical claim or historical retrieval.
  accessed_at: '2026-11-04T05:29:09.730491Z'
  support: supports
  snapshot_sha256: c05e15563c6a6072220755d9e282e4bb9da8073c1a70737203542882344bb446
  search_scope: EuropePMC exact EXT_ID:7002229 AND SRC:MED; CORE JSON,pageSize5,cursor*,no
    date filter; all one returned result read at 2026-11-04T05:29:09.730491Z.
- evidence_id: septin-iwataki2010-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A20561119+AND+SRC%3AMED&format=json&resultType=core&pageSize=5
  locator: Unique MED title/authors/year/DOI/access-route flags and complete abstractText;
    fresh peer receipt independently read
  summary: Iwataki,Hansen,Moestrup,Matsuoka2010, DOI10.1111/j.1550-7408.2010.00491.x,
    concerns Cochlodinium polykrikoides ultrastructure. Complete primary-paper abstract
    describes species-specific groove/flagellar architecture; no inspected body, Methods
    strain or figures, and no class-wide extrapolation. This verifies current bibliography,
    not every attached anatomical claim or historical retrieval.
  accessed_at: '2026-11-04T05:29:09.609734Z'
  support: supports
  snapshot_sha256: 752957b9c869a701b60dd8ba1d498136bd7c794c51ab2f576e3d45192b625db4
  search_scope: EuropePMC exact EXT_ID:20561119 AND SRC:MED; CORE JSON,pageSize5,cursor*,no
    date filter; all one returned result read at 2026-11-04T05:29:09.609734Z.
- evidence_id: septin-taylor1980-publisher
  kind: validation
  reference: https://www.sciencedirect.com/science/article/pii/0303264780900064
  locator: Current HTTP403 response and visible error/challenge text, independently
    inspected
  summary: Current route did not supply an article body. The actual current receipt
    is separate from October failures; no universal claim that a body is unavailable
    everywhere, and no primary scientific conclusion from the error page.
  accessed_at: '2026-11-04T05:29:09.894467Z'
  support: context_only
  snapshot_sha256: 1d1b615156fab1e5f419ce955caed229134965fdfbec54355a0ec2ce230cd872
- evidence_id: septin-iwataki2010-publisher
  kind: validation
  reference: https://onlinelibrary.wiley.com/doi/full/10.1111/j.1550-7408.2010.00491.x
  locator: Current HTTP403 response and visible error/challenge text, independently
    inspected
  summary: Current route did not supply an article body. The actual current receipt
    is separate from October failures; no universal claim that a body is unavailable
    everywhere, and no primary scientific conclusion from the error page.
  accessed_at: '2026-11-04T05:29:09.827108Z'
  support: context_only
  snapshot_sha256: 3537cd90fe4e522417a3a0cb210e61853d3843bdafe8f8655feb294078e889ec
- evidence_id: septin-catalogue
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Complete fresh official20-organism catalogue and all dataset keys, independently
    read from micro reviewer packet
  summary: Finite current response contains no Dinophyceae/dinoflagellate host. These
    three records are already genuinely morphology-only, so no downstream gene/module
    query is indicated; unrelated bacterial taxa are not proxies. Noncoverage is not
    biological absence.
  accessed_at: '2026-11-04T05:28:42.917849Z'
  support: supports
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  search_scope: Official https://imodulondb.org/api/datasets complete unpaginated
    response; inspected all20 organism IDs/names and all returned keys for Dinophyceae,Dinoflagellata,Dinophyta,dinoflagellate.
    No date filter; actual fetch 2026-11-04T05:28:42.917849Z.
- evidence_id: septin-adapter-runner-historical
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Actual prior command receipt and unavailable reason
  summary: Historical runner attempt exited1 on PermissionError reading pyvenv.cfg
    at Nov3 00:49Z; no new invocation. Current catalogue read is a separate official
    source fallback, not runner execution.
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: septin-original-native-checks
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/adversary-septin/original-checks.json
  locator: Actual three original native validate/render runs and all45 historical
    input occurrences
  summary: All three pairs validate exit0 and render byte-identically; all45 manifested
    historical inputs match git revision f97b1abe2d78971b6f66b9083087d7a94cf3c0cc,
    and all three current target hashes equal their old inputs. Historical batch26
    global executions are explicitly scoped to that old source, not claimed as current
    tests.
  accessed_at: '2026-11-04T05:29:56.038712Z'
  support: supports
  snapshot_sha256: 23810c7a8da1a84a39083d39fb06060ed98eff3fd54cc2e40b8616d01499350c
- evidence_id: septin-record-dinoflagellate_hypocone
  kind: record_content
  reference: data/structures/other/dinoflagellate_hypocone.yaml
  locator: 'Entire current maintained YAML: definitions,synonyms,taxonomy,evidence,all
    graph nodes/edges,discussions/history'
  summary: Complete nonstale record read at the frozen source; morphology/topology
    only. Exact authoritative anatomy and current bibliographic claims are assessed
    separately from retained historical rationale.
  accessed_at: '2026-11-04T05:33:32.048325Z'
  support: context_only
  snapshot_sha256: 0a596b02f63ce6799d10b49b4cf34a921fb2ae92e1208ee599a96ed47c5f40a1
- evidence_id: septin-original-dinoflagellate_hypocone
  kind: record_content
  reference: reviews/structured/20261022T054306Z-dinoflagellate-hypocone-audit/review.yaml
  locator: Entire immutable original YAML and deterministic Markdown pair
  summary: Original pass_with_limitations with 0 finding(s), exact predecessor scope
    and prose applicability note independently reviewed. Old global batch26 execution
    provenance is legitimate historical reuse, not a mislabeled current execution.
  accessed_at: '2026-11-04T05:33:32.048325Z'
  support: context_only
  snapshot_sha256: 9808828a60ce9d3accad23938b10e300ecda029aeb6a2822448eb1e32734acee
- evidence_id: septin-native-dinoflagellate_hypocone-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dinoflagellate_hypocone.yaml
    --verify
  locator: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_hypocone-uniprot-verify-receipt.json;
    receiptSHA256 41a0294e458b62ef551fae0493442c0a6f3cc61e44ea0e41128279abaa36cc68;
    log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_hypocone-uniprot-verify.log
  summary: Actual command exit0. Actual maintained inventory0 protein examples/0 typed
    GENE_OR_PROTEIN nodes. Empty-scope native success is not positive biological member,
    formation or localization coverage.
  accessed_at: '2026-11-04T05:28:01.092776Z'
  support: supports
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: septin-native-dinoflagellate_hypocone-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dinoflagellate_hypocone.yaml
    --causal-graphs
  locator: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_hypocone-uniprot-causal-receipt.json;
    receiptSHA256 510c50f43effb11b15d2b68ce3e717e5a7edbcef5175a38ae560568743fec6d6;
    log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_hypocone-uniprot-causal.log
  summary: Actual command exit0. Actual maintained inventory0 protein examples/0 typed
    GENE_OR_PROTEIN nodes. Empty-scope native success is not positive biological member,
    formation or localization coverage.
  accessed_at: '2026-11-04T05:28:01.537295Z'
  support: supports
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
- evidence_id: septin-record-dinoflagellate_sulcal_notch
  kind: record_content
  reference: data/structures/other/dinoflagellate_sulcal_notch.yaml
  locator: 'Entire current maintained YAML: definitions,synonyms,taxonomy,evidence,all
    graph nodes/edges,discussions/history'
  summary: Complete nonstale record read at the frozen source; morphology/topology
    only. Exact authoritative anatomy and current bibliographic claims are assessed
    separately from retained historical rationale.
  accessed_at: '2026-11-04T05:33:32.048325Z'
  support: context_only
  snapshot_sha256: 0e3dace360a1a70bc43f318649972ebb63a50628897c7681bb81c9c75f18c7b1
- evidence_id: septin-original-dinoflagellate_sulcal_notch
  kind: record_content
  reference: reviews/structured/20261022T054307Z-dinoflagellate-sulcal-notch-audit/review.yaml
  locator: Entire immutable original YAML and deterministic Markdown pair
  summary: Original pass_with_limitations with 0 finding(s), exact predecessor scope
    and prose applicability note independently reviewed. Old global batch26 execution
    provenance is legitimate historical reuse, not a mislabeled current execution.
  accessed_at: '2026-11-04T05:33:32.048325Z'
  support: context_only
  snapshot_sha256: 599567d90a1060af4e54f540be250d609a9ce6ea8092f826317f4bb31a75f4e7
- evidence_id: septin-native-dinoflagellate_sulcal_notch-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dinoflagellate_sulcal_notch.yaml
    --verify
  locator: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_sulcal_notch-uniprot-verify-receipt.json;
    receiptSHA256 d1ee6a2a01c7ddf32addba78ed57820876f551150f91a3804a20bc8acfaecd75;
    log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_sulcal_notch-uniprot-verify.log
  summary: Actual command exit0. Actual maintained inventory0 protein examples/0 typed
    GENE_OR_PROTEIN nodes. Empty-scope native success is not positive biological member,
    formation or localization coverage.
  accessed_at: '2026-11-04T05:28:01.984551Z'
  support: supports
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: septin-native-dinoflagellate_sulcal_notch-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dinoflagellate_sulcal_notch.yaml
    --causal-graphs
  locator: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_sulcal_notch-uniprot-causal-receipt.json;
    receiptSHA256 752ff55254e0b76729df47cd558f3fb28138a31d997faf1be9abfe3fd9faa331;
    log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_sulcal_notch-uniprot-causal.log
  summary: Actual command exit0. Actual maintained inventory0 protein examples/0 typed
    GENE_OR_PROTEIN nodes. Empty-scope native success is not positive biological member,
    formation or localization coverage.
  accessed_at: '2026-11-04T05:28:02.436030Z'
  support: supports
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
- evidence_id: septin-historical-failed-access-dinoflagellate_sulcal_notch
  kind: validation
  reference: reviews/structured/20261022T054307Z-dinoflagellate-sulcal-notch-audit/review.yaml#micro50-taylor1980-publisher
  locator: Retained original evidence row; quoted historical access timestamp/hash,
    not a fresh raw re-fetch
  summary: Original historical HTTP403 observation was explicitly context_only and
    said no body. Reclassify only database→validation in the successor; retain actual
    Oct21 date and original snapshot 14dd40deb21794994e8cbc95036a781eb7e7b41de1fbcc216c4af476bd5948f7.
    No allegation of falsely claiming body access.
  accessed_at: '2026-10-21T09:08:56.074246Z'
  support: context_only
  snapshot_sha256: 599567d90a1060af4e54f540be250d609a9ce6ea8092f826317f4bb31a75f4e7
- evidence_id: septin-record-dinoflagellate_sulcus
  kind: record_content
  reference: data/structures/other/dinoflagellate_sulcus.yaml
  locator: 'Entire current maintained YAML: definitions,synonyms,taxonomy,evidence,all
    graph nodes/edges,discussions/history'
  summary: Complete nonstale record read at the frozen source; morphology/topology
    only. Exact authoritative anatomy and current bibliographic claims are assessed
    separately from retained historical rationale.
  accessed_at: '2026-11-04T05:33:32.048325Z'
  support: context_only
  snapshot_sha256: b3606a5c03fbc85a602f3ea6927c22e49eedbcd00d1e9607c85ac080205bd356
- evidence_id: septin-original-dinoflagellate_sulcus
  kind: record_content
  reference: reviews/structured/20261022T054307Z-dinoflagellate-sulcus-audit/review.yaml
  locator: Entire immutable original YAML and deterministic Markdown pair
  summary: Original needs_curation with 1 finding(s), exact predecessor scope and
    prose applicability note independently reviewed. Old global batch26 execution
    provenance is legitimate historical reuse, not a mislabeled current execution.
  accessed_at: '2026-11-04T05:33:32.048325Z'
  support: context_only
  snapshot_sha256: 92ecf76bae282ad0410728eee21b4fcac7653e0d76c1544fca4d05d7dc8acd49
- evidence_id: septin-native-dinoflagellate_sulcus-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dinoflagellate_sulcus.yaml
    --verify
  locator: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_sulcus-uniprot-verify-receipt.json;
    receiptSHA256 80ab921dce57a64a64d9e5447af652aa02ec8a335b842dd69c2f16bbab869221;
    log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_sulcus-uniprot-verify.log
  summary: Actual command exit0. Actual maintained inventory0 protein examples/0 typed
    GENE_OR_PROTEIN nodes. Empty-scope native success is not positive biological member,
    formation or localization coverage.
  accessed_at: '2026-11-04T05:28:02.885339Z'
  support: supports
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: septin-native-dinoflagellate_sulcus-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dinoflagellate_sulcus.yaml
    --causal-graphs
  locator: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_sulcus-uniprot-causal-receipt.json;
    receiptSHA256 7d998cd21185ec3efc47c396030e3c029a33adf3ebbad077659dc21b09f566ee;
    log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_sulcus-uniprot-causal.log
  summary: Actual command exit0. Actual maintained inventory0 protein examples/0 typed
    GENE_OR_PROTEIN nodes. Empty-scope native success is not positive biological member,
    formation or localization coverage.
  accessed_at: '2026-11-04T05:28:03.345506Z'
  support: supports
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
- evidence_id: septin-historical-failed-access-dinoflagellate_sulcus
  kind: validation
  reference: reviews/structured/20261022T054307Z-dinoflagellate-sulcus-audit/review.yaml#micro50-taylor1980-publisher
  locator: Retained original evidence row; quoted historical access timestamp/hash,
    not a fresh raw re-fetch
  summary: Original historical HTTP403 observation was explicitly context_only and
    said no body. Reclassify only database→validation in the successor; retain actual
    Oct21 date and original snapshot 14dd40deb21794994e8cbc95036a781eb7e7b41de1fbcc216c4af476bd5948f7.
    No allegation of falsely claiming body access.
  accessed_at: '2026-10-21T09:08:56.074246Z'
  support: context_only
  snapshot_sha256: 92ecf76bae282ad0410728eee21b4fcac7653e0d76c1544fca4d05d7dc8acd49
- evidence_id: check-qc
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/qc.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T05:33:42.729426Z'
  support: supports
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  snapshot_sha256: 438fe87d8fd1f42ef6fe57fac50b94cefc21b7b18fbe282e1754e7cdb3556805
- evidence_id: check-labels
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/labels.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T05:28:24.350495Z'
  support: supports
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  snapshot_sha256: 6cdfb05df9a27194f05a5fd7f851783f817ac1523ca0bbfa54fe0e0d18775905
- evidence_id: check-trait-links
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/trait-links.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T05:28:04.023043Z'
  support: supports
  summary: Native TraitMech link check passed.
  snapshot_sha256: 8b336cdefbbd3daf6da8787990efdbe346c95e2c8361d50b7eb68a18f2d5a44a
- evidence_id: check-vendored
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/vendored.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T05:28:03.247629Z'
  support: supports
  summary: Pinned governed files match; native vendored check passed.
  snapshot_sha256: b1f169d103aaefa930745468bcca171e5867b9cc49e4e74311e458097e3252a6
- evidence_id: check-curies
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/curies.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T05:28:32.704878Z'
  support: supports
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  snapshot_sha256: fb3be251020aac118f6df680372ae7aaa32c2a1dd3366648cde95494f19d9dd2
- evidence_id: focused
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/focused-results.json
  locator: All twenty actual target schema/strict command outputs
  accessed_at: '2026-11-04T05:38:33Z'
  support: supports
  summary: Ten schema and ten strict commands returned exit zero.
  snapshot_sha256: 6ff796f7dea529fca416076511f06127dd28f7aa8730c26a1368cd8a4a9b1575
- evidence_id: supplemental-pmid
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/pmid-chunks-receipt.json
  locator: Complete native-report PMID set checked with unchanged resolver in batches
    of at most fifty
  accessed_at: '2026-11-04T05:29:33.829761Z'
  support: supports
  summary: 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers
    remain unverified.
  snapshot_sha256: 08fcfd3dc01b12c79b8671ba93e10d1657ea096fda7dbc75f18c59299ec65721
- evidence_id: historical-adapter-runner-availability
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical runner invocation receipt; exact retained SHA256 reverified
    during PR2387 synthesis
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  summary: Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS
    PermissionError reading the configured runner pyvenv.cfg. This is retained historical
    availability evidence, not a fresh attempt or a scientific validation failure.
    Native policy permits inspected source-catalogue fallback.
- evidence_id: root-native-dinoflagellate_apical_groove-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_apical_groove-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T05:27:57.521404Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dinoflagellate_apical_groove-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_apical_groove-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T05:27:57.951681Z'
  support: context_only
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dinoflagellate_apical_horn-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_apical_horn-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T05:27:58.384636Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dinoflagellate_apical_horn-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_apical_horn-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T05:27:58.832599Z'
  support: context_only
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dinoflagellate_cingulum-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_cingulum-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T05:27:59.280025Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dinoflagellate_cingulum-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_cingulum-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T05:27:59.725230Z'
  support: context_only
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dinoflagellate_epicone-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_epicone-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T05:28:00.188188Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dinoflagellate_epicone-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_epicone-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T05:28:00.641233Z'
  support: context_only
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dinoflagellate_hypocone-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_hypocone-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T05:28:01.092776Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dinoflagellate_hypocone-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_hypocone-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T05:28:01.537295Z'
  support: context_only
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dinoflagellate_sulcal_notch-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_sulcal_notch-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T05:28:01.984551Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dinoflagellate_sulcal_notch-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_sulcal_notch-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T05:28:02.436030Z'
  support: context_only
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dinoflagellate_sulcus-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_sulcus-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T05:28:02.885339Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dinoflagellate_sulcus-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dinoflagellate_sulcus-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T05:28:03.345506Z'
  support: context_only
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dna_gyrase_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dna_gyrase_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T05:28:04.848428Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dna_gyrase_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dna_gyrase_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T05:28:05.287630Z'
  support: context_only
  snapshot_sha256: e9925e98caefb278bed69f8a980ae3af6087a314dde6560afdf7442ac66a91b6
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dna_polymerase_iii_beta_sliding_clamp_processivity_factor_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dna_polymerase_iii_beta_sliding_clamp_processivity_factor_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T05:28:06.498864Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dna_polymerase_iii_beta_sliding_clamp_processivity_factor_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dna_polymerase_iii_beta_sliding_clamp_processivity_factor_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T05:28:06.934813Z'
  support: context_only
  snapshot_sha256: f767c55c18149a7ee0e0ecba42cf7bf6e538b498174ff3403619159559db03b6
  summary: 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dna_polymerase_iii_clamp_loader_chi_psi_subcomplex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dna_polymerase_iii_clamp_loader_chi_psi_subcomplex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T05:28:08.268775Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 2 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dna_polymerase_iii_clamp_loader_chi_psi_subcomplex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2387/dna_polymerase_iii_clamp_loader_chi_psi_subcomplex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T05:28:08.702161Z'
  support: context_only
  snapshot_sha256: b18c6192090adcab5331b9e6ba8404fd4684eab9585b0e5b5e6f36d94b560551
  summary: 2 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
assessments:
- assessment_id: micro-gyrase-identity
  area: identity
  topic: Exact complex and hierarchy
  outcome: supported
  summary: GO0120217/GO0009330 identify bacterial typeII gyrase, with declared GyrA2B2
    constituent architecture. GO negative-supercoiling term is activity, not a structure.
    Species variation in supercoiling proficiency is not silently replaced with universal
    quantitative activity.
  target_ids:
  - GO:0120217
  evidence_ids:
  - micro-record-0
  - micro-go-0120217
  - micro-go-0009330
  - micro-go-0003918
  - micro-go-0034335
  - micro-isa-0120217
  - micro-gyrase2019-jats
- assessment_id: micro-gyrase-refresh
  area: provenance
  topic: Substantive stale graph-grounding refresh
  outcome: supported
  summary: Only dated history and exact family groundings on two existing component_ref
    nodes changed. IPR005743/GyrA andIPR011557/GyrB are full families matching P0AES4/P0AES6
    and the component definitions; new node groundings are supported. No new edge
    or constituent/necessity claim was introduced; deposition F1 remains independent.
  target_ids:
  - GO:0120217
  evidence_ids:
  - micro-record-0
  - micro-delta-0
  - micro-prior-0
  - micro-ipr-IPR005743
  - micro-ipr-IPR011557
  - micro-up-P0AES4
  - micro-up-P0AES6
  - micro-graph-policy
- assessment_id: micro-gyrase-proteins
  area: grounding
  topic: Reference proteins and current singleton searches
  outcome: supported
  summary: Reviewed K12 P0AES4/gyrA/b2231 andP0AES6/gyrB/b3699 agree with exact current
    queries andRCSB entities. Current singleton queries do not certify the October
    search history. K12 source is distinct from BL21(DE3) recombinant expression.
  target_ids:
  - GO:0120217
  evidence_ids:
  - micro-record-0
  - micro-up-P0AES4
  - micro-up-P0AES6
  - micro-query-gyrA
  - micro-query-gyrB
  - micro-tax-83333
  - micro-tax-469008
  - micro-pdb-6RKU-entity1
  - micro-pdb-6RKU-entity2
- assessment_id: micro-gyrase-deposition
  area: evidence
  topic: Domain versus overall canonical model
  outcome: concern
  summary: Fresh native6RKU title/entity detail and primary MethodsSec17 identify
    the closed DNA-binding/cleavage-domain model.6RKW is the overall model. Current
    canonical note still calls6RKU complete; inherited minor finding persists without
    disputing correct2:2 proteins or full-length sample identities.
  target_ids:
  - GO:0120217
  evidence_ids:
  - micro-record-0
  - micro-gyrase2019-jats
  - micro-pdb-6RKU-entry
  - micro-pdb-6RKU-assembly
  - micro-pdb-6RKW-entry
  - micro-pdb-6RKW-assembly
- assessment_id: micro-gyrase-function
  area: evidence
  topic: Activity and experimental preparation limits
  outcome: supported
  summary: Purified reconstituted E.coli gyrase supports ATP-dependent negative supercoiling
    and the coarse activity class. Drug/AMP-PNP/DNA trapping used for EM is distinct
    from supercoiling/ATPase assays. No intact-cell localization, all-species proficiency
    or precise catalytic sequence is inferred.
  target_ids:
  - GO:0120217
  evidence_ids:
  - micro-record-0
  - micro-gyrase2019-jats
  - micro-up-P0AES4
  - micro-up-P0AES6
  - micro-go-0003918
  - micro-go-0034335
- assessment_id: micro-gyrase-graph
  area: graph
  topic: Declared nonmechanistic functional scope
  outcome: supported
  summary: Two constituent contributions, complex enables negative-supercoiling activity
    and activity acts on DNA are consistent with current source scopes. Explicit NONMECHANISTIC/FUNCTION
    limits exclude gate dynamics, strand-passage order and specific drug mechanism;
    no universal formation claim is required.
  target_ids:
  - GO:0120217
  evidence_ids:
  - micro-record-0
  - micro-graph-policy
  - micro-gyrase2019-jats
  - micro-schema
- assessment_id: micro-beta-identity
  area: identity
  topic: Bacterial beta versus PCNA class boundary
  outcome: concern
  summary: The record faithfully reproduces GO0044775 wording, but its claim homodimeric
    in prokaryotes/homotrimeric in other species conflates named bacterial beta with
    distinct PCNA/phage classes and misplaces archaeal PCNA. Kong structure, nativeIPR001001
    and reviewed archaealO73947 with primaryPCNA abstract establish the conflict.
    Keep valid GOidentity/E.coli dimer; explicitly document upstream scope conflict.
  target_ids:
  - GO:0044775
  evidence_ids:
  - micro-record-1
  - micro-go-0044775
  - micro-kong1992-pdf
  - micro-ipr-IPR001001-retry
  - micro-up-O73947
  - micro-pmid-11266590
  - micro-tax-186497
- assessment_id: micro-beta-hierarchy
  area: identity
  topic: Named PolIII subassembly and canonical example
  outcome: supported
  summary: GO0044775 is the exact named beta processivity complex; GO0032991 parent
    andGO0009360 parthood remain appropriate. Canonical E.coli Kong1992 beta dimer
    is supported. This does not license transferring every PCNA activity or archaeal
    identity into this record.
  target_ids:
  - GO:0044775
  evidence_ids:
  - micro-record-1
  - micro-go-0044775
  - micro-go-0032991
  - micro-go-0009360
  - micro-isa-0044775
  - micro-kong1992-pdf
  - micro-pmid-1349852
  - micro-tax-562
- assessment_id: micro-beta-family
  area: grounding
  topic: Verified full beta family
  outcome: concern
  summary: IPR001001 is a native whole-family entry with matching P0A988 xref, not
    merely a ring-shaped domain. The current class remains REVIEWED_LABEL_ONLY with
    unresolved current source-neutral mapping. Inherited minor exact-family finding
    persists; historical rationale must remain preserved.
  target_ids:
  - GO:0044775
  evidence_ids:
  - micro-record-1
  - micro-policy
  - micro-ipr-IPR001001-retry
  - micro-up-P0A988
- assessment_id: micro-beta-protein
  area: grounding
  topic: DnaN example and isoform qualification
  outcome: supported
  summary: Reviewed P0A988/dnaN/b3701 tax83333 matches the current singleton query.
    Standard beta is a homodimer; native shorter beta* alternative-product notes preclude
    an invented invariant oligomeric claim for all derived isoforms. Reference K12
    identity does not add an experimentally verified exact strain to Kong species-level
    canonical scope.
  target_ids:
  - GO:0044775
  evidence_ids:
  - micro-record-1
  - micro-up-P0A988
  - micro-query-dnaN
  - micro-tax-83333
  - micro-tax-562
  - micro-kong1992-pdf
- assessment_id: micro-beta-function-graph
  area: graph
  topic: Processivity outline versus direct structural evidence
  outcome: supported
  summary: Kong shows the ring architecture with modeled DNA fit, not a DNA co-crystal.
    Coarse tethering/encirclement function is independently supported by native authority
    and prior biochemical context; the graph explicitly withholds ATP-dependent loading
    sequence and unknown assembly requirements. Exact coreGO0044776 is external partner,
    not an extra beta constituent.
  target_ids:
  - GO:0044775
  evidence_ids:
  - micro-record-1
  - micro-kong1992-pdf
  - micro-up-P0A988
  - micro-go-0044776
  - micro-go-0006260
  - micro-graph-policy
  - micro-schema
- assessment_id: micro-chi-identity
  area: identity
  topic: Chi/psi heterodimer and hierarchy
  outcome: supported
  summary: GO0043847 matches the1:1 HolC/HolD adaptor; is_a complex and part_of GO0043846
    clamp loader are supported. Larger DnaX/SSB partners are excluded from this two-component
    constituent inventory by explicit scope.
  target_ids:
  - GO:0043847
  evidence_ids:
  - micro-record-2
  - micro-go-0043847
  - micro-go-0043846
  - micro-go-0032991
  - micro-isa-0043847
  - micro-pmid-8505305
  - micro-olson1995-pdf
- assessment_id: micro-chi-proteins
  area: grounding
  topic: HolC/HolD and external actors
  outcome: supported
  summary: Reviewed P28905/holC/b4259 andP28632/holD/b4372 tax83333 match current
    singleton queries. P06710 correctly covers tau/gamma alternative products; P0AGE0
    is SSB. The latter two are external graph actors with UniProt xrefs, appropriately
    UNANCHORED_WITH_UNIPROT rather than missing component examples.
  target_ids:
  - GO:0043847
  evidence_ids:
  - micro-record-2
  - micro-up-P28905
  - micro-up-P28632
  - micro-up-P06710
  - micro-up-P0AGE0
  - micro-query-holC
  - micro-query-holD
  - micro-tax-83333
  - micro-native-dna_polymerase_iii_clamp_loader_chi_psi_subcomplex-causal
- assessment_id: micro-chi-families
  area: grounding
  topic: Exact whole-family assignments
  outcome: concern
  summary: Native full-protein HolC IPR007459 and generic HolD IPR004615 agree with
    the maintained example xrefs; label-only current grounding remains. IPR018382
    is a narrower subgroup and need not replace generic psi. Old generic family functional
    prose does not supersede primary association/function evidence.
  target_ids:
  - GO:0043847
  evidence_ids:
  - micro-record-2
  - micro-policy
  - micro-ipr-IPR007459
  - micro-ipr-IPR004615
  - micro-ipr-IPR018382
  - micro-up-P28905
  - micro-up-P28632
- assessment_id: micro-chi-primary
  area: evidence
  topic: Physical1:1 assembly and partner interaction scope
  outcome: supported
  summary: Fresh XiaoIII/IV primary abstracts support cloning/identities and1:1 dimer
    with psi-gamma contact; full bodies remain inaccessible403. Independently read
    Olson body supports coexpression-soluble complex, sedimentation, tau/gamma affinity
    and clamp-loader reconstitution. MC1061 artificial-operon preparation and high-concentration
    bypass are explicit; no universal formation ESSENTIAL or native-cell absence inferred.
  target_ids:
  - GO:0043847
  evidence_ids:
  - micro-record-2
  - micro-pmid-8389364
  - micro-pmid-8505305
  - micro-olson1995-pdf
  - micro-xiao1993iii-publisher-access
  - micro-xiao1993iv-publisher-access
  - micro-schema
- assessment_id: micro-chi-graph
  area: graph
  topic: Gamma versus tau and SSB provenance
  outcome: supported
  summary: The psi→gamma wording is bounded to XiaoIV abstract; assembled dimer→tau/gamma
    is supported by Olson purified-binding experiments. SSB bridge is GO/native HolC/SSB
    annotation and secondary-review context, not an Olson SSB interaction assay. NONMECHANISTIC/FUNCTION
    graph does not claim an ordered loading cycle or direct-regulation causality.
  target_ids:
  - GO:0043847
  evidence_ids:
  - micro-record-2
  - micro-pmid-8505305
  - micro-olson1995-pdf
  - micro-pmid-12940977
  - micro-up-P28905
  - micro-up-P0AGE0
  - micro-go-0043847
  - micro-graph-policy
- assessment_id: micro-dataset-0
  area: scope
  topic: Actual matched dataset and bounded module membership
  outcome: supported
  summary: Official precise1k spans five listed K12-related strains, not exact BL21(DE3)
    orMC1061 preparations. Each selected native locus was checked across201 returned
    module rows. All selected loci are threshold-negative. These results do not establish
    biological absence, direct regulation, physical association, formation or localization.
  target_ids:
  - GO:0120217
  evidence_ids:
  - micro-catalogue
  - micro-ecoli-meta
  - micro-ecoli-modules
  - micro-ecoli-gene-b2231
  - micro-ecoli-gene-b3699
- assessment_id: micro-adapter-0
  area: scope
  topic: Whole-record molecular applicability
  outcome: concern
  summary: Original formal iModulon check excludes cross-checks solely because no
    expression claim appears, despite positive molecular/replication pathway assertions.
    Current official catalogue, strain metadata and actual gene/module fallback repair
    that rationale. Historical unavailable runner is separately dated, never described
    as newly executed.
  target_ids:
  - GO:0120217
  evidence_ids:
  - micro-record-0
  - micro-prior-0
  - micro-native-policy
  - micro-catalogue
  - micro-historical-runner
  - micro-ecoli-meta
  - micro-ecoli-gene-b2231
  - micro-ecoli-gene-b3699
- assessment_id: micro-taxonomy-0
  area: scope
  topic: Taxonomic occurrence and experimental limits
  outcome: supported
  summary: COMMON prevalence is qualitative, not a whole-species strain census. Exact
    native K12 examples differ from species-level canonical examples and experimental
    expression derivatives; selected dataset has only its five listed strains. No
    universal prevalence or sample-to-reference strain equality inferred.
  target_ids:
  - GO:0120217
  evidence_ids:
  - micro-record-0
  - micro-tax-562
  - micro-tax-83333
  - micro-ecoli-meta
  - micro-tax-469008
  - micro-gyrase2019-jats
- assessment_id: micro-history-0
  area: provenance
  topic: Append-only history and exact predecessor lineage
  outcome: supported
  summary: Original findings/actions and current discussions/history were read. Historical
    rationale is preserved as provenance; current exact family/source corrections
    are separate from dated rationale. No group/category or neighboring issue is resolved
    by inference; all four original finding keys persist with exact predecessors.
  target_ids:
  - GO:0120217
  evidence_ids:
  - micro-record-0
  - micro-prior-0
  - micro-policy
  - micro-delta-0
  - micro-original-audit
- assessment_id: micro-schema-0
  area: schema
  topic: Actual native checks with finite coverage
  outcome: supported
  summary: 'All three original pairs validate/render exactly and39 historical input
    occurrences agree. Actual current protein checks pass: own5 examples and7 typed
    nodes comprise5 COVERED plus2 external UNANCHORED_WITH_UNIPROT actors, not7covered.
    Schema success is not source truth or family completeness.'
  target_ids:
  - GO:0120217
  evidence_ids:
  - micro-original-audit
  - micro-native-dna_gyrase_complex-verify
  - micro-native-dna_gyrase_complex-causal
- assessment_id: micro-coverage-0
  area: completeness
  topic: Complete assigned scope and explicit limits
  outcome: supported
  summary: Entire current record and immutable pair reviewed. No maintained images/measured-properties
    require pixel/unit work. Primary bodies/abstracts, secondary review and native
    authorities remain explicitly separate. No optional example or generic-family
    type defect is invented.
  target_ids:
  - GO:0120217
  evidence_ids:
  - micro-record-0
  - micro-prior-0
  - micro-schema
- assessment_id: micro-verdict-0
  area: other
  topic: Current independent verdict
  outcome: concern
  summary: 'needs_curation: one inherited minor deposition-scope finding; new graph
    groundings supported.'
  target_ids:
  - GO:0120217
  evidence_ids:
  - micro-record-0
  - micro-prior-0
  - micro-policy
- assessment_id: micro-dataset-1
  area: scope
  topic: Actual matched dataset and bounded module membership
  outcome: supported
  summary: Official precise1k spans five listed K12-related strains, not exact BL21(DE3)
    orMC1061 preparations. Each selected native locus was checked across201 returned
    module rows. All selected loci are threshold-negative. These results do not establish
    biological absence, direct regulation, physical association, formation or localization.
  target_ids:
  - GO:0044775
  evidence_ids:
  - micro-catalogue
  - micro-ecoli-meta
  - micro-ecoli-modules
  - micro-ecoli-gene-b3701
- assessment_id: micro-adapter-1
  area: scope
  topic: Whole-record molecular applicability
  outcome: concern
  summary: Original formal iModulon check excludes cross-checks solely because no
    expression claim appears, despite positive molecular/replication pathway assertions.
    Current official catalogue, strain metadata and actual gene/module fallback repair
    that rationale. Historical unavailable runner is separately dated, never described
    as newly executed.
  target_ids:
  - GO:0044775
  evidence_ids:
  - micro-record-1
  - micro-prior-1
  - micro-native-policy
  - micro-catalogue
  - micro-historical-runner
  - micro-ecoli-meta
  - micro-ecoli-gene-b3701
- assessment_id: micro-taxonomy-1
  area: scope
  topic: Taxonomic occurrence and experimental limits
  outcome: supported
  summary: COMMON prevalence is qualitative, not a whole-species strain census. Exact
    native K12 examples differ from species-level canonical examples and experimental
    expression derivatives; selected dataset has only its five listed strains. No
    universal prevalence or sample-to-reference strain equality inferred.
  target_ids:
  - GO:0044775
  evidence_ids:
  - micro-record-1
  - micro-tax-562
  - micro-tax-83333
  - micro-ecoli-meta
  - micro-kong1992-pdf
- assessment_id: micro-history-1
  area: provenance
  topic: Append-only history and exact predecessor lineage
  outcome: supported
  summary: Original findings/actions and current discussions/history were read. Historical
    rationale is preserved as provenance; current exact family/source corrections
    are separate from dated rationale. No group/category or neighboring issue is resolved
    by inference; all four original finding keys persist with exact predecessors.
  target_ids:
  - GO:0044775
  evidence_ids:
  - micro-record-1
  - micro-prior-1
  - micro-policy
  - micro-delta-1
  - micro-original-audit
- assessment_id: micro-schema-1
  area: schema
  topic: Actual native checks with finite coverage
  outcome: supported
  summary: 'All three original pairs validate/render exactly and39 historical input
    occurrences agree. Actual current protein checks pass: own5 examples and7 typed
    nodes comprise5 COVERED plus2 external UNANCHORED_WITH_UNIPROT actors, not7covered.
    Schema success is not source truth or family completeness.'
  target_ids:
  - GO:0044775
  evidence_ids:
  - micro-original-audit
  - micro-native-dna_polymerase_iii_beta_sliding_clamp_processivity_factor_complex-verify
  - micro-native-dna_polymerase_iii_beta_sliding_clamp_processivity_factor_complex-causal
- assessment_id: micro-coverage-1
  area: completeness
  topic: Complete assigned scope and explicit limits
  outcome: supported
  summary: Entire current record and immutable pair reviewed. No maintained images/measured-properties
    require pixel/unit work. Primary bodies/abstracts, secondary review and native
    authorities remain explicitly separate. No optional example or generic-family
    type defect is invented.
  target_ids:
  - GO:0044775
  evidence_ids:
  - micro-record-1
  - micro-prior-1
  - micro-schema
- assessment_id: micro-verdict-1
  area: other
  topic: Current independent verdict
  outcome: concern
  summary: 'needs_curation: one inherited major class-definition finding and one minor
    exact-family finding; valid E.coli identity retained.'
  target_ids:
  - GO:0044775
  evidence_ids:
  - micro-record-1
  - micro-prior-1
  - micro-policy
- assessment_id: micro-dataset-2
  area: scope
  topic: Actual matched dataset and bounded module membership
  outcome: supported
  summary: Official precise1k spans five listed K12-related strains, not exact BL21(DE3)
    orMC1061 preparations. Each selected native locus was checked across201 returned
    module rows. holD alone exceeds ppGpp module145 threshold; the70-gene weight list
    corroborates that hit, without relying on generated narrative. Other three loci
    are threshold-negative. These results do not establish biological absence, direct
    regulation, physical association, formation or localization.
  target_ids:
  - GO:0043847
  evidence_ids:
  - micro-catalogue
  - micro-ecoli-meta
  - micro-ecoli-modules
  - micro-ecoli-gene-b4259
  - micro-ecoli-gene-b4372
  - micro-ecoli-gene-b0470
  - micro-ecoli-gene-b4059
  - micro-ecoli-module-145
- assessment_id: micro-adapter-2
  area: scope
  topic: Whole-record molecular applicability
  outcome: concern
  summary: Original formal iModulon check excludes cross-checks solely because no
    expression claim appears, despite positive molecular/replication pathway assertions.
    Current official catalogue, strain metadata and actual gene/module fallback repair
    that rationale. Historical unavailable runner is separately dated, never described
    as newly executed.
  target_ids:
  - GO:0043847
  evidence_ids:
  - micro-record-2
  - micro-prior-2
  - micro-native-policy
  - micro-catalogue
  - micro-historical-runner
  - micro-ecoli-meta
  - micro-ecoli-gene-b4259
  - micro-ecoli-gene-b4372
  - micro-ecoli-gene-b0470
  - micro-ecoli-gene-b4059
- assessment_id: micro-taxonomy-2
  area: scope
  topic: Taxonomic occurrence and experimental limits
  outcome: supported
  summary: COMMON prevalence is qualitative, not a whole-species strain census. Exact
    native K12 examples differ from species-level canonical examples and experimental
    expression derivatives; selected dataset has only its five listed strains. No
    universal prevalence or sample-to-reference strain equality inferred.
  target_ids:
  - GO:0043847
  evidence_ids:
  - micro-record-2
  - micro-tax-562
  - micro-tax-83333
  - micro-ecoli-meta
  - micro-olson1995-pdf
- assessment_id: micro-history-2
  area: provenance
  topic: Append-only history and exact predecessor lineage
  outcome: supported
  summary: Original findings/actions and current discussions/history were read. Historical
    rationale is preserved as provenance; current exact family/source corrections
    are separate from dated rationale. No group/category or neighboring issue is resolved
    by inference; all four original finding keys persist with exact predecessors.
  target_ids:
  - GO:0043847
  evidence_ids:
  - micro-record-2
  - micro-prior-2
  - micro-policy
  - micro-delta-2
  - micro-original-audit
- assessment_id: micro-schema-2
  area: schema
  topic: Actual native checks with finite coverage
  outcome: supported
  summary: 'All three original pairs validate/render exactly and39 historical input
    occurrences agree. Actual current protein checks pass: own5 examples and7 typed
    nodes comprise5 COVERED plus2 external UNANCHORED_WITH_UNIPROT actors, not7covered.
    Schema success is not source truth or family completeness.'
  target_ids:
  - GO:0043847
  evidence_ids:
  - micro-original-audit
  - micro-native-dna_polymerase_iii_clamp_loader_chi_psi_subcomplex-verify
  - micro-native-dna_polymerase_iii_clamp_loader_chi_psi_subcomplex-causal
- assessment_id: micro-coverage-2
  area: completeness
  topic: Complete assigned scope and explicit limits
  outcome: supported
  summary: Entire current record and immutable pair reviewed. No maintained images/measured-properties
    require pixel/unit work. Primary bodies/abstracts, secondary review and native
    authorities remain explicitly separate. No optional example or generic-family
    type defect is invented.
  target_ids:
  - GO:0043847
  evidence_ids:
  - micro-record-2
  - micro-prior-2
  - micro-schema
- assessment_id: micro-verdict-2
  area: other
  topic: Current independent verdict
  outcome: concern
  summary: 'needs_curation: one inherited minor two-family grounding finding; primary1:1/partner
    outline supported.'
  target_ids:
  - GO:0043847
  evidence_ids:
  - micro-record-2
  - micro-prior-2
  - micro-policy
- assessment_id: micro-kind-replication50-agent-xiao1993iii-publisher
  area: provenance
  topic: Historical access-kind correction
  outcome: concern
  summary: The original honestly reports HTTP403 and context_only but uses kind database.
    Correct only to validation/context_only; retain original timestamp/hash and do
    not allege a false body read or infer scientific refutation.
  target_ids:
  - GO:0043847
  evidence_ids:
  - micro-prior-2
  - micro-historical-replication50-agent-xiao1993iii-publisher
- assessment_id: micro-kind-replication50-agent-xiao1993iv-publisher
  area: provenance
  topic: Historical access-kind correction
  outcome: concern
  summary: The original honestly reports HTTP403 and context_only but uses kind database.
    Correct only to validation/context_only; retain original timestamp/hash and do
    not allege a false body read or infer scientific refutation.
  target_ids:
  - GO:0043847
  evidence_ids:
  - micro-prior-2
  - micro-historical-replication50-agent-xiao1993iv-publisher
- assessment_id: plaque-t0-taxonomy
  area: scope
  topic: taxonomy
  outcome: supported
  summary: Dinophyceae restriction and VARIABLE class occurrence are supported without
    asserting every member bears every specialized morphology. Species77300 identity
    and diagnostic groove agree; COMMON is qualitative diagnostic morphology, not
    a numerical census, and no experimental strain is invented.
  target_ids:
  - GO:0097685
  evidence_ids:
  - plaque-current-0
  - plaque-go
  - plaque-tax-2864
  - plaque-go-0097685-constraints
  - plaque-tol-orientation
  - plaque-tax-77300
  - plaque-iwataki2010-meta
  - plaque-gomez2017-s3
- assessment_id: plaque-t0-composition
  area: grounding
  topic: composition
  outcome: supported
  summary: No molecular constituents/protein examples are positively asserted; targeted
    openTODO correctly awaits direct localization and exact family evidence. Whole-cell
    cellulose, membranes, tubulin or flagellar apparatus cannot be inserted as region-specific
    constituents without support.
  target_ids:
  - GO:0097685
  evidence_ids:
  - plaque-current-0
  - plaque-policy
  - plaque-checklist
- assessment_id: plaque-t0-formation-necessity
  area: scope
  topic: formation necessity
  outcome: unknown
  summary: Morphology, location and class membership do not establish molecular assembly
    necessity. There are no component essentiality values or depletion assays to reinterpret;
    acknowledged unknown is not a curation finding.
  target_ids:
  - GO:0097685
  evidence_ids:
  - plaque-current-0
  - plaque-schema
  - plaque-checklist
- assessment_id: plaque-t0-structured-source
  area: evidence
  topic: structured source
  outcome: not_applicable
  summary: The full record states morphological identity, taxon scope and descriptive
    topology, without a positive gene/regulator/pathway/stress/trait/expression-module
    assertion. Original notes[1] already gives morphology-based exclusion; this is
    genuineN/A, not an expression-only exemption or omitted assessment. Complete current
    catalogue separately lacks matching natural hosts; no foreign-host module proxy.
  target_ids:
  - GO:0097685
  evidence_ids:
  - plaque-current-0
  - plaque-original-0-yaml
  - plaque-review-skill
  - plaque-catalogue
  - plaque-catalogue-search
  - plaque-historical-adapter-unavailable
- assessment_id: plaque-t0-completeness
  area: completeness
  topic: completeness
  outcome: supported
  summary: Complete maintained fields and original pair assessed. No maintained images,
    numerical physical properties, molecular components or mechanism are asserted.
    Optional fields and targeted molecularTODOs do not require invented enrichment.
  target_ids:
  - GO:0097685
  evidence_ids:
  - plaque-current-0
  - plaque-checklist
  - plaque-policy
- assessment_id: plaque-t0-history-provenance
  area: provenance
  topic: history provenance
  outcome: supported
  summary: All original target bytes unchanged and original findings/actions empty.
    Preserve PROPOSED status, dated rationale and prior history; no neighboring/grouped
    issue resolution inferred. Old shared-base corpus gates remain historical, not
    fresh execution.
  target_ids:
  - GO:0097685
  evidence_ids:
  - plaque-current-0
  - plaque-original-0-yaml
  - plaque-original-0-md
  - plaque-policy
  - plaque-original-current-validation
- assessment_id: plaque-t0-native-validation
  area: schema
  topic: native validation
  outcome: supported
  summary: Native original validate/render and exact frozen-input proof passed; current
    actual native protein/graph checks passed with zero examples/zero typednodes.
    Schema/coverage does not certify scientific truth.
  target_ids:
  - GO:0097685
  evidence_ids:
  - plaque-current-0
  - plaque-original-current-validation
  - plaque-native-dinoflagellate_apical_groove-verify
  - plaque-native-dinoflagellate_apical_groove-causal
- assessment_id: plaque-t1-taxonomy
  area: scope
  topic: taxonomy
  outcome: supported
  summary: Dinophyceae restriction and VARIABLE class occurrence are supported without
    asserting every member bears every specialized morphology. The record makes no
    compulsory canonical-species or quantitative-prevalence assertion.
  target_ids:
  - GO:0097686
  evidence_ids:
  - plaque-current-1
  - plaque-go
  - plaque-tax-2864
  - plaque-go-0097686-constraints
  - plaque-tol-orientation
- assessment_id: plaque-t1-composition
  area: grounding
  topic: composition
  outcome: supported
  summary: No molecular constituents/protein examples are positively asserted; targeted
    openTODO correctly awaits direct localization and exact family evidence. Whole-cell
    cellulose, membranes, tubulin or flagellar apparatus cannot be inserted as region-specific
    constituents without support.
  target_ids:
  - GO:0097686
  evidence_ids:
  - plaque-current-1
  - plaque-policy
  - plaque-checklist
- assessment_id: plaque-t1-formation-necessity
  area: scope
  topic: formation necessity
  outcome: unknown
  summary: Morphology, location and class membership do not establish molecular assembly
    necessity. There are no component essentiality values or depletion assays to reinterpret;
    acknowledged unknown is not a curation finding.
  target_ids:
  - GO:0097686
  evidence_ids:
  - plaque-current-1
  - plaque-schema
  - plaque-checklist
- assessment_id: plaque-t1-structured-source
  area: evidence
  topic: structured source
  outcome: not_applicable
  summary: The full record states morphological identity, taxon scope and descriptive
    topology, without a positive gene/regulator/pathway/stress/trait/expression-module
    assertion. Original notes[1] already gives morphology-based exclusion; this is
    genuineN/A, not an expression-only exemption or omitted assessment. Complete current
    catalogue separately lacks matching natural hosts; no foreign-host module proxy.
  target_ids:
  - GO:0097686
  evidence_ids:
  - plaque-current-1
  - plaque-original-1-yaml
  - plaque-review-skill
  - plaque-catalogue
  - plaque-catalogue-search
  - plaque-historical-adapter-unavailable
- assessment_id: plaque-t1-completeness
  area: completeness
  topic: completeness
  outcome: supported
  summary: Complete maintained fields and original pair assessed. No maintained images,
    numerical physical properties, molecular components or mechanism are asserted.
    Optional fields and targeted molecularTODOs do not require invented enrichment.
  target_ids:
  - GO:0097686
  evidence_ids:
  - plaque-current-1
  - plaque-checklist
  - plaque-policy
- assessment_id: plaque-t1-history-provenance
  area: provenance
  topic: history provenance
  outcome: supported
  summary: All original target bytes unchanged and original findings/actions empty.
    Preserve PROPOSED status, dated rationale and prior history; no neighboring/grouped
    issue resolution inferred. Old shared-base corpus gates remain historical, not
    fresh execution.
  target_ids:
  - GO:0097686
  evidence_ids:
  - plaque-current-1
  - plaque-original-1-yaml
  - plaque-original-1-md
  - plaque-policy
  - plaque-original-current-validation
- assessment_id: plaque-t1-native-validation
  area: schema
  topic: native validation
  outcome: supported
  summary: Native original validate/render and exact frozen-input proof passed; current
    actual native protein/graph checks passed with zero examples/zero typednodes.
    Schema/coverage does not certify scientific truth.
  target_ids:
  - GO:0097686
  evidence_ids:
  - plaque-current-1
  - plaque-original-current-validation
  - plaque-native-dinoflagellate_apical_horn-verify
  - plaque-native-dinoflagellate_apical_horn-causal
- assessment_id: plaque-t2-taxonomy
  area: scope
  topic: taxonomy
  outcome: supported
  summary: Dinophyceae restriction and VARIABLE class occurrence are supported without
    asserting every member bears every specialized morphology. The record makes no
    compulsory canonical-species or quantitative-prevalence assertion.
  target_ids:
  - GO:0097611
  evidence_ids:
  - plaque-current-2
  - plaque-go
  - plaque-tax-2864
  - plaque-go-0097611-constraints
  - plaque-tol-orientation
- assessment_id: plaque-t2-composition
  area: grounding
  topic: composition
  outcome: supported
  summary: No molecular constituents/protein examples are positively asserted; targeted
    openTODO correctly awaits direct localization and exact family evidence. Whole-cell
    cellulose, membranes, tubulin or flagellar apparatus cannot be inserted as region-specific
    constituents without support.
  target_ids:
  - GO:0097611
  evidence_ids:
  - plaque-current-2
  - plaque-policy
  - plaque-checklist
- assessment_id: plaque-t2-formation-necessity
  area: scope
  topic: formation necessity
  outcome: unknown
  summary: Morphology, location and class membership do not establish molecular assembly
    necessity. There are no component essentiality values or depletion assays to reinterpret;
    acknowledged unknown is not a curation finding.
  target_ids:
  - GO:0097611
  evidence_ids:
  - plaque-current-2
  - plaque-schema
  - plaque-checklist
- assessment_id: plaque-t2-structured-source
  area: evidence
  topic: structured source
  outcome: not_applicable
  summary: The full record states morphological identity, taxon scope and descriptive
    topology, without a positive gene/regulator/pathway/stress/trait/expression-module
    assertion. Original notes[1] already gives morphology-based exclusion; this is
    genuineN/A, not an expression-only exemption or omitted assessment. Complete current
    catalogue separately lacks matching natural hosts; no foreign-host module proxy.
  target_ids:
  - GO:0097611
  evidence_ids:
  - plaque-current-2
  - plaque-original-2-yaml
  - plaque-review-skill
  - plaque-catalogue
  - plaque-catalogue-search
  - plaque-historical-adapter-unavailable
- assessment_id: plaque-t2-completeness
  area: completeness
  topic: completeness
  outcome: supported
  summary: Complete maintained fields and original pair assessed. No maintained images,
    numerical physical properties, molecular components or mechanism are asserted.
    Optional fields and targeted molecularTODOs do not require invented enrichment.
  target_ids:
  - GO:0097611
  evidence_ids:
  - plaque-current-2
  - plaque-checklist
  - plaque-policy
- assessment_id: plaque-t2-history-provenance
  area: provenance
  topic: history provenance
  outcome: supported
  summary: All original target bytes unchanged and original findings/actions empty.
    Preserve PROPOSED status, dated rationale and prior history; no neighboring/grouped
    issue resolution inferred. Old shared-base corpus gates remain historical, not
    fresh execution.
  target_ids:
  - GO:0097611
  evidence_ids:
  - plaque-current-2
  - plaque-original-2-yaml
  - plaque-original-2-md
  - plaque-policy
  - plaque-original-current-validation
- assessment_id: plaque-t2-native-validation
  area: schema
  topic: native validation
  outcome: supported
  summary: Native original validate/render and exact frozen-input proof passed; current
    actual native protein/graph checks passed with zero examples/zero typednodes.
    Schema/coverage does not certify scientific truth.
  target_ids:
  - GO:0097611
  evidence_ids:
  - plaque-current-2
  - plaque-original-current-validation
  - plaque-native-dinoflagellate_cingulum-verify
  - plaque-native-dinoflagellate_cingulum-causal
- assessment_id: plaque-t3-taxonomy
  area: scope
  topic: taxonomy
  outcome: supported
  summary: Dinophyceae restriction and VARIABLE class occurrence are supported without
    asserting every member bears every specialized morphology. The record makes no
    compulsory canonical-species or quantitative-prevalence assertion.
  target_ids:
  - GO:0097613
  evidence_ids:
  - plaque-current-3
  - plaque-go
  - plaque-tax-2864
  - plaque-go-0097613-constraints
  - plaque-tol-orientation
- assessment_id: plaque-t3-composition
  area: grounding
  topic: composition
  outcome: supported
  summary: No molecular constituents/protein examples are positively asserted; targeted
    openTODO correctly awaits direct localization and exact family evidence. Whole-cell
    cellulose, membranes, tubulin or flagellar apparatus cannot be inserted as region-specific
    constituents without support.
  target_ids:
  - GO:0097613
  evidence_ids:
  - plaque-current-3
  - plaque-policy
  - plaque-checklist
- assessment_id: plaque-t3-formation-necessity
  area: scope
  topic: formation necessity
  outcome: unknown
  summary: Morphology, location and class membership do not establish molecular assembly
    necessity. There are no component essentiality values or depletion assays to reinterpret;
    acknowledged unknown is not a curation finding.
  target_ids:
  - GO:0097613
  evidence_ids:
  - plaque-current-3
  - plaque-schema
  - plaque-checklist
- assessment_id: plaque-t3-structured-source
  area: evidence
  topic: structured source
  outcome: not_applicable
  summary: The full record states morphological identity, taxon scope and descriptive
    topology, without a positive gene/regulator/pathway/stress/trait/expression-module
    assertion. Original notes[1] already gives morphology-based exclusion; this is
    genuineN/A, not an expression-only exemption or omitted assessment. Complete current
    catalogue separately lacks matching natural hosts; no foreign-host module proxy.
  target_ids:
  - GO:0097613
  evidence_ids:
  - plaque-current-3
  - plaque-original-3-yaml
  - plaque-review-skill
  - plaque-catalogue
  - plaque-catalogue-search
  - plaque-historical-adapter-unavailable
- assessment_id: plaque-t3-completeness
  area: completeness
  topic: completeness
  outcome: supported
  summary: Complete maintained fields and original pair assessed. No maintained images,
    numerical physical properties, molecular components or mechanism are asserted.
    Optional fields and targeted molecularTODOs do not require invented enrichment.
  target_ids:
  - GO:0097613
  evidence_ids:
  - plaque-current-3
  - plaque-checklist
  - plaque-policy
- assessment_id: plaque-t3-history-provenance
  area: provenance
  topic: history provenance
  outcome: supported
  summary: All original target bytes unchanged and original findings/actions empty.
    Preserve PROPOSED status, dated rationale and prior history; no neighboring/grouped
    issue resolution inferred. Old shared-base corpus gates remain historical, not
    fresh execution.
  target_ids:
  - GO:0097613
  evidence_ids:
  - plaque-current-3
  - plaque-original-3-yaml
  - plaque-original-3-md
  - plaque-policy
  - plaque-original-current-validation
- assessment_id: plaque-t3-native-validation
  area: schema
  topic: native validation
  outcome: supported
  summary: Native original validate/render and exact frozen-input proof passed; current
    actual native protein/graph checks passed with zero examples/zero typednodes.
    Schema/coverage does not certify scientific truth.
  target_ids:
  - GO:0097613
  evidence_ids:
  - plaque-current-3
  - plaque-original-current-validation
  - plaque-native-dinoflagellate_epicone-verify
  - plaque-native-dinoflagellate_epicone-causal
- assessment_id: plaque-t0-identity
  area: identity
  topic: identity
  outcome: supported
  summary: GO0097685 exactly denotes an apical surface groove rather than whole apex/epicone
    or flagellar apparatus. Typical looping morphology accommodates the directly described
    U-shaped species example. Current native taxon77300 bridges old Cochlodinium name
    to Margalefidinium.
  target_ids:
  - GO:0097685
  evidence_ids:
  - plaque-current-0
  - plaque-go
  - plaque-tax-77300
  - plaque-iwataki2010-meta
  - plaque-gomez2017-s3
- assessment_id: plaque-t0-graph
  area: graph
  topic: graph
  outcome: supported
  summary: 'Two exact direct edges are supported: groove is_aGO0097610 and part_ofGO0097613;
    Iwataki abstract independently places groove on dorsal epicone. NONMECHANISTIC
    graph does not imply assembly order or a physiological mechanism.'
  target_ids:
  - GO:0097685
  evidence_ids:
  - plaque-current-0
  - plaque-go
  - plaque-go-0097685-history
  - plaque-iwataki2010-meta
  - plaque-graph-policy
- assessment_id: plaque-t0-source-placement
  area: evidence
  topic: source placement
  outcome: supported
  summary: 2010 source supports ultrastructural morphology, whereas2017source supports
    formal name transfer/genus diagnosis. Gomez ownPuertoRicoLM did not resolve groove
    andSEM was obscured; no replacement of2010experiment or strain/figure claim. DOI/PMID
    and authors independently checked.
  target_ids:
  - GO:0097685
  evidence_ids:
  - plaque-current-0
  - plaque-iwataki2010-meta
  - plaque-gomez2017-meta
  - plaque-gomez2017-s3
  - plaque-iwataki2010-publisher
- assessment_id: plaque-t1-identity
  area: identity
  topic: identity
  outcome: supported
  summary: GO0097686 is the specialized horn-shaped thecate apex, not generic apex
    or whole epicone. Exact is_a parent and thecate qualifier agree with current ontology;
    broad class morphology is not a universal species inventory.
  target_ids:
  - GO:0097686
  evidence_ids:
  - plaque-current-1
  - plaque-go
  - plaque-go-0097686-history
  - plaque-tol-orientation
- assessment_id: plaque-t1-graph
  area: graph
  topic: graph
  outcome: supported
  summary: Horn is_aapex and apex part_ofepicone are direct typed links; horn containment
    is inherited through that explicit path. Current edge evidence says through-parent,
    so generic scope wording is not interpreted as a false independent direct GOedge
    or complete transitive closure.
  target_ids:
  - GO:0097686
  evidence_ids:
  - plaque-current-1
  - plaque-go
  - plaque-horn-epicone-path
  - plaque-graph-policy
- assessment_id: plaque-t1-bibliography
  area: provenance
  topic: bibliography
  outcome: supported
  summary: Taylor exact title/year/PMID/DOI matches GOxref. Record explicitly limits
    historical unread review to bibliographic corroboration; current secondary abstract
    supplies no detailed horn formation evidence and publisher403 is not bodyaccess.
  target_ids:
  - GO:0097686
  evidence_ids:
  - plaque-current-1
  - plaque-go
  - plaque-taylor1980-meta
  - plaque-taylor1980-publisher
- assessment_id: plaque-t2-identity
  area: identity
  topic: identity
  outcome: supported
  summary: GO0097611 is transverse cell-surface furrow, with broadcingulum andrelatedgirdle/transversegroove
    synonyms. Transverseflagellum location does not make flagellar molecular apparatus
    the groove. Expert account explicitly distinguishes groove-free desmokont flagellation.
  target_ids:
  - GO:0097611
  evidence_ids:
  - plaque-current-2
  - plaque-go
  - plaque-tol-dinoflagellates
- assessment_id: plaque-t2-graph
  area: graph
  topic: graph
  outcome: supported
  summary: The two-node one-edge graph states exact is_aGO0097610. It does not reconstruct
    propulsion or furrow assembly; optional motility mechanism is not required to
    enlarge the topology.
  target_ids:
  - GO:0097611
  evidence_ids:
  - plaque-current-2
  - plaque-go
  - plaque-go-0097611-history
  - plaque-graph-policy
- assessment_id: plaque-t2-bibliography
  area: provenance
  topic: bibliography
  outcome: supported
  summary: Taylor citation is explicitly metadata-only historical context, with exact
    identity corroborated now; current expert morphology andGO support the anatomy.
    No inaccessible review body is represented as read.
  target_ids:
  - GO:0097611
  evidence_ids:
  - plaque-current-2
  - plaque-go
  - plaque-taylor1980-meta
  - plaque-taylor1980-publisher
  - plaque-tol-dinoflagellates
- assessment_id: plaque-t3-identity
  area: identity
  topic: identity
  outcome: supported
  summary: GO0097613 is anterior region above cingulum, distinct from apex part and
    posterior hypocone. Relatedepitheca/episome terminology is not asserted as universal
    exact synonymy across naked/thecate forms.
  target_ids:
  - GO:0097613
  evidence_ids:
  - plaque-current-3
  - plaque-go
  - plaque-tol-orientation
- assessment_id: plaque-t3-graph
  area: graph
  topic: graph
  outcome: supported
  summary: Direct native children show apex/groovepart_ofepicone, while definition
    supports cingulum boundary and anterior/posterior separation. Descriptive has_part
    is not treated as proof that every species/cell bears apicalgroove or as a literal
    partition membrane. CurrentVARIABLE scope and NONMECHANISTIC wording retain this
    limit.
  target_ids:
  - GO:0097613
  evidence_ids:
  - plaque-current-3
  - plaque-go
  - plaque-go-0097613-history
  - plaque-tol-orientation
  - plaque-graph-policy
- assessment_id: plaque-t3-scope-boundaries
  area: scope
  topic: scope boundaries
  outcome: supported
  summary: Resolved discussions distinguish part-versuswhole apex and siblinghypocone.
    The word narrower in a historical prompt is qualified by explicit part_of rationale/resolution;
    no synonym conflation or historical rewrite needed.
  target_ids:
  - GO:0097613
  evidence_ids:
  - plaque-current-3
  - plaque-go
  - plaque-policy
- assessment_id: plaque-t0-failed-access-kind
  area: provenance
  topic: failed access kind
  outcome: concern
  summary: The original disclosed unsuccessful publisher response is typed database/context_only.
    Correct successor kind tovalidation/context_only, preserving historical URL/time/status
    and explicitly scoped scientific evidence. This is a bundle classification issue
    only, not a record-science defect or allegation of false bodyaccess.
  target_ids:
  - GO:0097685
  evidence_ids:
  - plaque-historical-failed-access-0
  - plaque-original-0-yaml
  - plaque-review-schema
- assessment_id: plaque-t1-failed-access-kind
  area: provenance
  topic: failed access kind
  outcome: concern
  summary: The original disclosed unsuccessful publisher response is typed database/context_only.
    Correct successor kind tovalidation/context_only, preserving historical URL/time/status
    and explicitly scoped scientific evidence. This is a bundle classification issue
    only, not a record-science defect or allegation of false bodyaccess.
  target_ids:
  - GO:0097686
  evidence_ids:
  - plaque-historical-failed-access-1
  - plaque-original-1-yaml
  - plaque-review-schema
- assessment_id: plaque-t2-failed-access-kind
  area: provenance
  topic: failed access kind
  outcome: concern
  summary: The original disclosed unsuccessful publisher response is typed database/context_only.
    Correct successor kind tovalidation/context_only, preserving historical URL/time/status
    and explicitly scoped scientific evidence. This is a bundle classification issue
    only, not a record-science defect or allegation of false bodyaccess.
  target_ids:
  - GO:0097611
  evidence_ids:
  - plaque-historical-failed-access-2
  - plaque-original-2-yaml
  - plaque-review-schema
- assessment_id: septin-dinoflagellate_hypocone-identity
  area: identity
  topic: Exact structure identity and synonym scope
  outcome: supported
  summary: Exact posterior region below the cingulum, separated from epicone, matches
    GO0097614 and the authored orientation text. Broad hypocone and related hyposome/hypotheca
    scopes preserve athecate/thecate distinctions; antapex is a part, not an exact
    synonym.
  target_ids:
  - GO:0097614
  evidence_ids:
  - septin-record-dinoflagellate_hypocone
  - septin-go
  - septin-go-0097614-history
  - septin-go-0097614-constraints
  - septin-tax-2864
  - septin-tol-orientation
  - septin-tol-dinoflagellates
  - septin-schema-policy
- assessment_id: septin-dinoflagellate_hypocone-hierarchy
  area: identity
  topic: Typed parentage and regional boundaries
  outcome: supported
  summary: GO0110165 is the direct hypocone parent and GO0097684 is a part_of child;
    related epicone is its anterior counterpart, not part or synonym.
  target_ids:
  - GO:0097614
  evidence_ids:
  - septin-record-dinoflagellate_hypocone
  - septin-go
  - septin-go-0097614-history
  - septin-go-0097614-constraints
  - septin-tax-2864
  - septin-tol-orientation
  - septin-tol-dinoflagellates
- assessment_id: septin-dinoflagellate_hypocone-taxonomy
  area: scope
  topic: Taxonomic restriction without universality
  outcome: supported
  summary: Current only_in_taxon2864 and native ENA class identity agree. VARIABLE
    is compatible with varied morphotypes and groove-free desmokont forms; no prevalence
    percentage, majority or universal assertion is inferred.
  target_ids:
  - GO:0097614
  evidence_ids:
  - septin-record-dinoflagellate_hypocone
  - septin-go
  - septin-go-0097614-history
  - septin-go-0097614-constraints
  - septin-tax-2864
  - septin-tol-orientation
  - septin-tol-dinoflagellates
- assessment_id: septin-dinoflagellate_hypocone-composition
  area: grounding
  topic: Optional constituent inventory
  outcome: supported
  summary: No components, protein examples or gene/protein nodes occur. Historical
    OPEN molecular-constituent TODO preserves the source limits of that pass; it is
    not a claim that no molecule could contribute. Generic whole-cell material is
    not a localized regional component, and optional slots alone do not require curation.
  target_ids:
  - GO:0097614
  evidence_ids:
  - septin-record-dinoflagellate_hypocone
  - septin-go
  - septin-go-0097614-history
  - septin-go-0097614-constraints
  - septin-tax-2864
  - septin-tol-orientation
  - septin-tol-dinoflagellates
  - septin-curation-policy
  - septin-native-dinoflagellate_hypocone-verify
  - septin-native-dinoflagellate_hypocone-causal
- assessment_id: septin-dinoflagellate_hypocone-formation
  area: grounding
  topic: Formation necessity not established
  outcome: unknown
  summary: The record makes no molecular assembly, component essentiality or formation-necessity
    assertion. Morphological definitions and topology do not identify molecules required
    for formation; no universal formation requirement is invented.
  target_ids:
  - GO:0097614
  evidence_ids:
  - septin-record-dinoflagellate_hypocone
  - septin-go
  - septin-go-0097614-history
  - septin-go-0097614-constraints
  - septin-tax-2864
  - septin-tol-orientation
  - septin-tol-dinoflagellates
  - septin-schema-policy
- assessment_id: septin-dinoflagellate_hypocone-graph
  area: graph
  topic: Complete descriptive topology
  outcome: supported
  summary: Seven structure nodes/eight edges support is-a,parental regional parthood,the
    cingulum/epicone boundary and the specialized notch extension/appearance. Reciprocal
    cingulum edges describe the same spatial boundary, not independent causal experiments.
    FUNCTION/NONMECHANISTIC scope is accurate; no missing molecular step is inferred.
  target_ids:
  - GO:0097614
  evidence_ids:
  - septin-record-dinoflagellate_hypocone
  - septin-go
  - septin-go-0097614-history
  - septin-go-0097614-constraints
  - septin-tax-2864
  - septin-tol-orientation
  - septin-tol-dinoflagellates
  - septin-graph-policy
- assessment_id: septin-dinoflagellate_hypocone-source-conflict
  area: evidence
  topic: Antapex authority discrepancy kept bounded
  outcome: supported
  summary: GO0097684 itself retains anterior wording, but GO0097618 and the directly
    inspected orientation authority specify posterior antapex. These three targets
    use the supported posterior orientation; the neighboring definition error is neither
    imported as a new target defect nor claimed resolved.
  target_ids:
  - GO:0097614
  evidence_ids:
  - septin-record-dinoflagellate_hypocone
  - septin-go
  - septin-go-0097614-history
  - septin-go-0097614-constraints
  - septin-tax-2864
  - septin-tol-orientation
  - septin-tol-dinoflagellates
- assessment_id: septin-dinoflagellate_hypocone-measurements-images
  area: completeness
  topic: No invented numerical or image requirements
  outcome: not_applicable
  summary: No maintained image, measured dimension, stoichiometry or physical-property
    value is asserted. ToL captions and text were read, no pixels/raw microscopy/supplements;
    no visual measurement or licence-transfer claim.
  target_ids:
  - GO:0097614
  evidence_ids:
  - septin-record-dinoflagellate_hypocone
  - septin-go
  - septin-go-0097614-history
  - septin-go-0097614-constraints
  - septin-tax-2864
  - septin-tol-orientation
  - septin-tol-dinoflagellates
  - septin-literature-policy
- assessment_id: septin-dinoflagellate_hypocone-history
  area: provenance
  topic: Historical rationale and current assertions
  outcome: supported
  summary: Dated curation and discussion rationales remain historical and append-only.
    Current subtype/boundary claims are assessed directly; no history rewrite, status
    promotion, optional inventory issue or unrelated record disposition is authorized.
  target_ids:
  - GO:0097614
  evidence_ids:
  - septin-record-dinoflagellate_hypocone
  - septin-original-dinoflagellate_hypocone
  - septin-curation-policy
- assessment_id: septin-dinoflagellate_hypocone-adapter
  area: evidence
  topic: Whole-record structured-source applicability
  outcome: not_applicable
  summary: All positive assertions concern anatomical regions,furrow placement and
    descriptive topology; molecular constituents/mechanisms are expressly deferred.
    Original prose physical-scope exclusion is justified, even without a formal adapter
    row. Complete current catalogue also lacks a matching Dinophyceae host; no unrelated
    proxy, downstream query or biological absence inference.
  target_ids:
  - GO:0097614
  evidence_ids:
  - septin-record-dinoflagellate_hypocone
  - septin-go
  - septin-go-0097614-history
  - septin-go-0097614-constraints
  - septin-tax-2864
  - septin-tol-orientation
  - septin-tol-dinoflagellates
  - septin-original-dinoflagellate_hypocone
  - septin-review-policy
  - septin-catalogue
  - septin-adapter-runner-historical
- assessment_id: septin-dinoflagellate_hypocone-schema
  area: schema
  topic: Frozen inputs and original native contract
  outcome: supported
  summary: Current target matches original frozen hash. Original validate/render exit0,
    exact Markdown and all15 historical input occurrences verified; separate root
    protein checks exit0 with empty scope. Old batch26 global gate receipts remain
    historical; this does not certify future saved-head or CI checks.
  target_ids:
  - GO:0097614
  evidence_ids:
  - septin-record-dinoflagellate_hypocone
  - septin-original-dinoflagellate_hypocone
  - septin-original-native-checks
  - septin-native-dinoflagellate_hypocone-verify
  - septin-native-dinoflagellate_hypocone-causal
- assessment_id: septin-dinoflagellate_hypocone-verdict
  area: consistency
  topic: Independent current scientific disposition
  outcome: supported
  summary: 'Pass with limitations: exact anatomy,typed topology and bounded taxonomic
    scope are positively supported, with no confirmed current record finding. Molecular
    formation and optional constituents remain unknown.'
  target_ids:
  - GO:0097614
  evidence_ids:
  - septin-record-dinoflagellate_hypocone
  - septin-go
  - septin-go-0097614-history
  - septin-go-0097614-constraints
  - septin-tax-2864
  - septin-tol-orientation
  - septin-tol-dinoflagellates
  - septin-original-dinoflagellate_hypocone
  - septin-original-native-checks
- assessment_id: septin-dinoflagellate_sulcal_notch-identity
  area: identity
  topic: Exact structure identity and synonym scope
  outcome: supported
  summary: Exact narrower sulcus extending to the posterior antapex and producing
    bilobed hypocone appearance matches GO0097618. Exact dinoflagellate sulcus notch
    and related sulcal notch synonyms are correct. Is-a sulcus is distinct from reaching
    antapex or changing hypocone appearance.
  target_ids:
  - GO:0097618
  evidence_ids:
  - septin-record-dinoflagellate_sulcal_notch
  - septin-go
  - septin-go-0097618-history
  - septin-go-0097618-constraints
  - septin-tax-2864
  - septin-tol-orientation
  - septin-tol-dinoflagellates
  - septin-schema-policy
- assessment_id: septin-dinoflagellate_sulcal_notch-hierarchy
  area: identity
  topic: Typed parentage and regional boundaries
  outcome: supported
  summary: GO0097618 is_a GO0097612; posterior extension and hypocone appearance do
    not make it a subtype of antapex/hypocone.
  target_ids:
  - GO:0097618
  evidence_ids:
  - septin-record-dinoflagellate_sulcal_notch
  - septin-go
  - septin-go-0097618-history
  - septin-go-0097618-constraints
  - septin-tax-2864
  - septin-tol-orientation
  - septin-tol-dinoflagellates
- assessment_id: septin-dinoflagellate_sulcal_notch-taxonomy
  area: scope
  topic: Taxonomic restriction without universality
  outcome: supported
  summary: Current only_in_taxon2864 and native ENA class identity agree. VARIABLE
    is compatible with varied morphotypes and groove-free desmokont forms; no prevalence
    percentage, majority or universal assertion is inferred.
  target_ids:
  - GO:0097618
  evidence_ids:
  - septin-record-dinoflagellate_sulcal_notch
  - septin-go
  - septin-go-0097618-history
  - septin-go-0097618-constraints
  - septin-tax-2864
  - septin-tol-orientation
  - septin-tol-dinoflagellates
- assessment_id: septin-dinoflagellate_sulcal_notch-composition
  area: grounding
  topic: Optional constituent inventory
  outcome: supported
  summary: No components, protein examples or gene/protein nodes occur. Historical
    OPEN molecular-constituent TODO preserves the source limits of that pass; it is
    not a claim that no molecule could contribute. Generic whole-cell material is
    not a localized regional component, and optional slots alone do not require curation.
  target_ids:
  - GO:0097618
  evidence_ids:
  - septin-record-dinoflagellate_sulcal_notch
  - septin-go
  - septin-go-0097618-history
  - septin-go-0097618-constraints
  - septin-tax-2864
  - septin-tol-orientation
  - septin-tol-dinoflagellates
  - septin-curation-policy
  - septin-native-dinoflagellate_sulcal_notch-verify
  - septin-native-dinoflagellate_sulcal_notch-causal
- assessment_id: septin-dinoflagellate_sulcal_notch-formation
  area: grounding
  topic: Formation necessity not established
  outcome: unknown
  summary: The record makes no molecular assembly, component essentiality or formation-necessity
    assertion. Morphological definitions and topology do not identify molecules required
    for formation; no universal formation requirement is invented.
  target_ids:
  - GO:0097618
  evidence_ids:
  - septin-record-dinoflagellate_sulcal_notch
  - septin-go
  - septin-go-0097618-history
  - septin-go-0097618-constraints
  - septin-tax-2864
  - septin-tol-orientation
  - septin-tol-dinoflagellates
  - septin-schema-policy
- assessment_id: septin-dinoflagellate_sulcal_notch-graph
  area: graph
  topic: Complete descriptive topology
  outcome: supported
  summary: Four structure nodes/three edges support is-a sulcus, extension to antapex
    and bilobed hypocone appearance at exact GO morphology tier. FUNCTION/NONMECHANISTIC
    scope is accurate; no missing molecular step is inferred.
  target_ids:
  - GO:0097618
  evidence_ids:
  - septin-record-dinoflagellate_sulcal_notch
  - septin-go
  - septin-go-0097618-history
  - septin-go-0097618-constraints
  - septin-tax-2864
  - septin-tol-orientation
  - septin-tol-dinoflagellates
  - septin-graph-policy
- assessment_id: septin-dinoflagellate_sulcal_notch-source-conflict
  area: evidence
  topic: Antapex authority discrepancy kept bounded
  outcome: supported
  summary: GO0097684 itself retains anterior wording, but GO0097618 and the directly
    inspected orientation authority specify posterior antapex. These three targets
    use the supported posterior orientation; the neighboring definition error is neither
    imported as a new target defect nor claimed resolved.
  target_ids:
  - GO:0097618
  evidence_ids:
  - septin-record-dinoflagellate_sulcal_notch
  - septin-go
  - septin-go-0097618-history
  - septin-go-0097618-constraints
  - septin-tax-2864
  - septin-tol-orientation
  - septin-tol-dinoflagellates
- assessment_id: septin-dinoflagellate_sulcal_notch-measurements-images
  area: completeness
  topic: No invented numerical or image requirements
  outcome: not_applicable
  summary: No maintained image, measured dimension, stoichiometry or physical-property
    value is asserted. ToL captions and text were read, no pixels/raw microscopy/supplements;
    no visual measurement or licence-transfer claim.
  target_ids:
  - GO:0097618
  evidence_ids:
  - septin-record-dinoflagellate_sulcal_notch
  - septin-go
  - septin-go-0097618-history
  - septin-go-0097618-constraints
  - septin-tax-2864
  - septin-tol-orientation
  - septin-tol-dinoflagellates
  - septin-literature-policy
- assessment_id: septin-dinoflagellate_sulcal_notch-history
  area: provenance
  topic: Historical rationale and current assertions
  outcome: supported
  summary: Dated curation and discussion rationales remain historical and append-only.
    Current subtype/boundary claims are assessed directly; no history rewrite, status
    promotion, optional inventory issue or unrelated record disposition is authorized.
  target_ids:
  - GO:0097618
  evidence_ids:
  - septin-record-dinoflagellate_sulcal_notch
  - septin-original-dinoflagellate_sulcal_notch
  - septin-curation-policy
- assessment_id: septin-dinoflagellate_sulcal_notch-adapter
  area: evidence
  topic: Whole-record structured-source applicability
  outcome: not_applicable
  summary: All positive assertions concern anatomical regions,furrow placement and
    descriptive topology; molecular constituents/mechanisms are expressly deferred.
    Original prose physical-scope exclusion is justified, even without a formal adapter
    row. Complete current catalogue also lacks a matching Dinophyceae host; no unrelated
    proxy, downstream query or biological absence inference.
  target_ids:
  - GO:0097618
  evidence_ids:
  - septin-record-dinoflagellate_sulcal_notch
  - septin-go
  - septin-go-0097618-history
  - septin-go-0097618-constraints
  - septin-tax-2864
  - septin-tol-orientation
  - septin-tol-dinoflagellates
  - septin-original-dinoflagellate_sulcal_notch
  - septin-review-policy
  - septin-catalogue
  - septin-adapter-runner-historical
- assessment_id: septin-dinoflagellate_sulcal_notch-schema
  area: schema
  topic: Frozen inputs and original native contract
  outcome: supported
  summary: Current target matches original frozen hash. Original validate/render exit0,
    exact Markdown and all15 historical input occurrences verified; separate root
    protein checks exit0 with empty scope. Old batch26 global gate receipts remain
    historical; this does not certify future saved-head or CI checks.
  target_ids:
  - GO:0097618
  evidence_ids:
  - septin-record-dinoflagellate_sulcal_notch
  - septin-original-dinoflagellate_sulcal_notch
  - septin-original-native-checks
  - septin-native-dinoflagellate_sulcal_notch-verify
  - septin-native-dinoflagellate_sulcal_notch-causal
- assessment_id: septin-dinoflagellate_sulcal_notch-bibliography
  area: provenance
  topic: Exact ontology-to-paper attribution
  outcome: supported
  summary: Current GO0097618 definition.xrefs does cite Taylor PMID7002229; metadata
    confirms title/author/year/DOI and the record honestly limits it to bibliography.
    GO supports bilobed anatomy; Taylor body has not been independently inspected.
  target_ids:
  - GO:0097618
  evidence_ids:
  - septin-record-dinoflagellate_sulcal_notch
  - septin-go
  - septin-taylor1980-meta
  - septin-iwataki2010-meta
  - septin-taylor1980-publisher
  - septin-iwataki2010-publisher
- assessment_id: septin-dinoflagellate_sulcal_notch-verdict
  area: consistency
  topic: Independent current scientific disposition
  outcome: supported
  summary: 'Pass with limitations: exact anatomy,typed topology and bounded taxonomic
    scope are positively supported, with no confirmed current record finding. Molecular
    formation and optional constituents remain unknown.'
  target_ids:
  - GO:0097618
  evidence_ids:
  - septin-record-dinoflagellate_sulcal_notch
  - septin-go
  - septin-go-0097618-history
  - septin-go-0097618-constraints
  - septin-tax-2864
  - septin-tol-orientation
  - septin-tol-dinoflagellates
  - septin-original-dinoflagellate_sulcal_notch
  - septin-original-native-checks
- assessment_id: septin-dinoflagellate_sulcus-identity
  area: identity
  topic: Exact structure identity and synonym scope
  outcome: supported
  summary: Exact ventral cell-surface furrow partially housing the longitudinal flagellum
    and intersecting the cingulum matches GO0097612. Broad sulcus and related longitudinal
    furrow/groove synonyms retain scope; narrower notch remains a separate subclass.
  target_ids:
  - GO:0097612
  evidence_ids:
  - septin-record-dinoflagellate_sulcus
  - septin-go
  - septin-go-0097612-history
  - septin-go-0097612-constraints
  - septin-tax-2864
  - septin-tol-orientation
  - septin-tol-dinoflagellates
  - septin-schema-policy
- assessment_id: septin-dinoflagellate_sulcus-hierarchy
  area: identity
  topic: Typed parentage and regional boundaries
  outcome: supported
  summary: GO0097612 is_a GO0097610 cell surface furrow; GO0097618 is its narrower
    child, not a synonym.
  target_ids:
  - GO:0097612
  evidence_ids:
  - septin-record-dinoflagellate_sulcus
  - septin-go
  - septin-go-0097612-history
  - septin-go-0097612-constraints
  - septin-tax-2864
  - septin-tol-orientation
  - septin-tol-dinoflagellates
- assessment_id: septin-dinoflagellate_sulcus-taxonomy
  area: scope
  topic: Taxonomic restriction without universality
  outcome: supported
  summary: Current only_in_taxon2864 and native ENA class identity agree. VARIABLE
    is compatible with varied morphotypes and groove-free desmokont forms; no prevalence
    percentage, majority or universal assertion is inferred.
  target_ids:
  - GO:0097612
  evidence_ids:
  - septin-record-dinoflagellate_sulcus
  - septin-go
  - septin-go-0097612-history
  - septin-go-0097612-constraints
  - septin-tax-2864
  - septin-tol-orientation
  - septin-tol-dinoflagellates
- assessment_id: septin-dinoflagellate_sulcus-composition
  area: grounding
  topic: Optional constituent inventory
  outcome: supported
  summary: No components, protein examples or gene/protein nodes occur. Historical
    OPEN molecular-constituent TODO preserves the source limits of that pass; it is
    not a claim that no molecule could contribute. Generic whole-cell material is
    not a localized regional component, and optional slots alone do not require curation.
  target_ids:
  - GO:0097612
  evidence_ids:
  - septin-record-dinoflagellate_sulcus
  - septin-go
  - septin-go-0097612-history
  - septin-go-0097612-constraints
  - septin-tax-2864
  - septin-tol-orientation
  - septin-tol-dinoflagellates
  - septin-curation-policy
  - septin-native-dinoflagellate_sulcus-verify
  - septin-native-dinoflagellate_sulcus-causal
- assessment_id: septin-dinoflagellate_sulcus-formation
  area: grounding
  topic: Formation necessity not established
  outcome: unknown
  summary: The record makes no molecular assembly, component essentiality or formation-necessity
    assertion. Morphological definitions and topology do not identify molecules required
    for formation; no universal formation requirement is invented.
  target_ids:
  - GO:0097612
  evidence_ids:
  - septin-record-dinoflagellate_sulcus
  - septin-go
  - septin-go-0097612-history
  - septin-go-0097612-constraints
  - septin-tax-2864
  - septin-tol-orientation
  - septin-tol-dinoflagellates
  - septin-schema-policy
- assessment_id: septin-dinoflagellate_sulcus-graph
  area: graph
  topic: Complete descriptive topology
  outcome: supported
  summary: Three structure nodes/two edges support is-a cell surface furrow and ventral
    cingulum intersection. FUNCTION/NONMECHANISTIC scope is accurate; no missing molecular
    step is inferred.
  target_ids:
  - GO:0097612
  evidence_ids:
  - septin-record-dinoflagellate_sulcus
  - septin-go
  - septin-go-0097612-history
  - septin-go-0097612-constraints
  - septin-tax-2864
  - septin-tol-orientation
  - septin-tol-dinoflagellates
  - septin-graph-policy
- assessment_id: septin-dinoflagellate_sulcus-source-conflict
  area: evidence
  topic: Antapex authority discrepancy kept bounded
  outcome: supported
  summary: GO0097684 itself retains anterior wording, but GO0097618 and the directly
    inspected orientation authority specify posterior antapex. These three targets
    use the supported posterior orientation; the neighboring definition error is neither
    imported as a new target defect nor claimed resolved.
  target_ids:
  - GO:0097612
  evidence_ids:
  - septin-record-dinoflagellate_sulcus
  - septin-go
  - septin-go-0097612-history
  - septin-go-0097612-constraints
  - septin-tax-2864
  - septin-tol-orientation
  - septin-tol-dinoflagellates
- assessment_id: septin-dinoflagellate_sulcus-measurements-images
  area: completeness
  topic: No invented numerical or image requirements
  outcome: not_applicable
  summary: No maintained image, measured dimension, stoichiometry or physical-property
    value is asserted. ToL captions and text were read, no pixels/raw microscopy/supplements;
    no visual measurement or licence-transfer claim.
  target_ids:
  - GO:0097612
  evidence_ids:
  - septin-record-dinoflagellate_sulcus
  - septin-go
  - septin-go-0097612-history
  - septin-go-0097612-constraints
  - septin-tax-2864
  - septin-tol-orientation
  - septin-tol-dinoflagellates
  - septin-literature-policy
- assessment_id: septin-dinoflagellate_sulcus-history
  area: provenance
  topic: Historical rationale and current assertions
  outcome: supported
  summary: Dated curation and discussion rationales remain historical and append-only.
    Current subtype/boundary claims are assessed directly; no history rewrite, status
    promotion, optional inventory issue or unrelated record disposition is authorized.
  target_ids:
  - GO:0097612
  evidence_ids:
  - septin-record-dinoflagellate_sulcus
  - septin-original-dinoflagellate_sulcus
  - septin-curation-policy
- assessment_id: septin-dinoflagellate_sulcus-adapter
  area: evidence
  topic: Whole-record structured-source applicability
  outcome: not_applicable
  summary: All positive assertions concern anatomical regions,furrow placement and
    descriptive topology; molecular constituents/mechanisms are expressly deferred.
    Original prose physical-scope exclusion is justified, even without a formal adapter
    row. Complete current catalogue also lacks a matching Dinophyceae host; no unrelated
    proxy, downstream query or biological absence inference.
  target_ids:
  - GO:0097612
  evidence_ids:
  - septin-record-dinoflagellate_sulcus
  - septin-go
  - septin-go-0097612-history
  - septin-go-0097612-constraints
  - septin-tax-2864
  - septin-tol-orientation
  - septin-tol-dinoflagellates
  - septin-original-dinoflagellate_sulcus
  - septin-review-policy
  - septin-catalogue
  - septin-adapter-runner-historical
- assessment_id: septin-dinoflagellate_sulcus-schema
  area: schema
  topic: Frozen inputs and original native contract
  outcome: supported
  summary: Current target matches original frozen hash. Original validate/render exit0,
    exact Markdown and all15 historical input occurrences verified; separate root
    protein checks exit0 with empty scope. Old batch26 global gate receipts remain
    historical; this does not certify future saved-head or CI checks.
  target_ids:
  - GO:0097612
  evidence_ids:
  - septin-record-dinoflagellate_sulcus
  - septin-original-dinoflagellate_sulcus
  - septin-original-native-checks
  - septin-native-dinoflagellate_sulcus-verify
  - septin-native-dinoflagellate_sulcus-causal
- assessment_id: septin-dinoflagellate_sulcus-bibliography
  area: provenance
  topic: Exact ontology-to-paper attribution
  outcome: concern
  summary: Current GO0097612 definition.xrefs cites PMID20561119, verified as Iwataki2010,
    rather than Taylor7002229. Both current evidence notes wrongly connect Taylor
    to this exact GO definition. Taylor may support general background, but unknown
    body access neither proves nor refutes that; correct only the specific attribution.
  target_ids:
  - GO:0097612
  evidence_ids:
  - septin-record-dinoflagellate_sulcus
  - septin-go
  - septin-taylor1980-meta
  - septin-iwataki2010-meta
  - septin-taylor1980-publisher
  - septin-iwataki2010-publisher
- assessment_id: septin-dinoflagellate_sulcus-verdict
  area: consistency
  topic: Independent current scientific disposition
  outcome: concern
  summary: Needs curation for one confirmed inherited minor current GO-definition
    bibliography attribution; anatomy,scope and topology retain positive support.
  target_ids:
  - GO:0097612
  evidence_ids:
  - septin-record-dinoflagellate_sulcus
  - septin-go
  - septin-go-0097612-history
  - septin-go-0097612-constraints
  - septin-tax-2864
  - septin-tol-orientation
  - septin-tol-dinoflagellates
  - septin-original-dinoflagellate_sulcus
  - septin-original-native-checks
  - septin-taylor1980-meta
  - septin-iwataki2010-meta
- assessment_id: current-input-comparison
  area: provenance
  topic: Complete frozen-input comparison and bounded refresh
  outcome: supported
  summary: 1 of ten original target hashes differ from current main. The changed content
    is substantively reassessed in the target-specific assessments; original observations
    remain historical and unchanged. All current target and used context bytes are
    frozen.
  target_ids:
  - GO:0097685
  - GO:0097686
  - GO:0097611
  - GO:0097613
  - GO:0097614
  - GO:0097618
  - GO:0097612
  - GO:0120217
  - GO:0044775
  - GO:0043847
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
  issue_key: gyrase-deposition-scope
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Distinguish the cleavage-domain and overall gyrase depositions
  description: The canonical example calls PDB6RKU the complete GyrA2-GyrB2 cryo-EM
    assembly. Its native title and primary Methods Sec17 identify6RKU as the closed
    DNA-binding/cleavage-domain model and6RKW as the overall model. The two correct
    protein entity mappings and2:2 stoichiometry are unaffected.
  target_ids:
  - GO:0120217
  field_paths:
  - canonical_examples[0].note
  - canonical_examples[0].reference
  evidence_ids:
  - micro-record-0
  - micro-gyrase2019-jats
  - micro-pdb-6RKU-entry
  - micro-pdb-6RKW-entry
  - micro-pdb-6RKU-assembly
  - micro-pdb-6RKU-entity1
  - micro-pdb-6RKU-entity2
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_gyrase_complex.yaml
    role: maintained scientific record
  rule_id: Source-specific identity, scope and exact component grounding
  native_severity: minor
  normalization_reason: The maintained complex identity, correct protein examples
    and supported coarse function remain intact; the defect is localized source precision
    or exact family grounding.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T054333Z-dna-gyrase-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2916
- finding_id: micro-F2
  issue_key: beta-clamp-cross-class-definition
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Keep the beta-clamp definition distinct from PCNA
  description: The definition asserts that this DNA polymeraseIII beta subcomplex
    is homodimeric in prokaryotes and homotrimeric in other species. Kong1992 instead
    distinguishes the bacterial beta ring from analogous PCNA and phage factors, and
    native IPR001001 separates the classes. GO0044775 carries the same conflation;
    its own cited O73947 is an archaeal PCNA homotrimer.
  target_ids:
  - GO:0044775
  field_paths:
  - definition
  - definition_source
  - components#dnaN_beta_subunit.stoichiometry
  - components#dnaN_beta_subunit.role
  evidence_ids:
  - micro-record-1
  - micro-go-0044775
  - micro-kong1992-pdf
  - micro-ipr-IPR001001-retry
  - micro-up-O73947
  - micro-pmid-11266590
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_polymerase_iii_beta_sliding_clamp_processivity_factor_complex.yaml
    role: maintained scientific record
  rule_id: Source-specific identity, scope and exact component grounding
  native_severity: major
  normalization_reason: The defining text materially expands the named beta/PolIII
    class into other polymerase processivity-factor classes and misstates archaeal
    scope; correct local examples do not cure that class-level error.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T054334Z-dna-polymerase-iii-beta-sliding-clamp-processivity-factor-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2917
- finding_id: micro-F3
  issue_key: beta-clamp-exact-family
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground the beta subunit with its exact family
  description: IPR001001 directly identifies the full beta sliding-clamp family and
    is carried by the maintained P0A988 example, but the component remains REVIEWED_LABEL_ONLY
    and the current TODO defers that mapping.
  target_ids:
  - GO:0044775
  field_paths:
  - components#dnaN_beta_subunit.grounding_status
  - discussions#resolve_pol_iii_beta_clamp_grounding
  evidence_ids:
  - micro-record-1
  - micro-policy
  - micro-ipr-IPR001001-retry
  - micro-up-P0A988
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_polymerase_iii_beta_sliding_clamp_processivity_factor_complex.yaml
    role: maintained scientific record
  rule_id: Source-specific identity, scope and exact component grounding
  native_severity: minor
  normalization_reason: The maintained complex identity, correct protein examples
    and supported coarse function remain intact; the defect is localized source precision
    or exact family grounding.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T054334Z-dna-polymerase-iii-beta-sliding-clamp-processivity-factor-complex-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2918
- finding_id: micro-F4
  issue_key: chi-psi-exact-families
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground HolC and HolD with their exact families
  description: The two named rows remain REVIEWED_LABEL_ONLY despite native full-protein
    families IPR007459 for HolC and IPR004615 for HolD and matching reviewed-example
    xrefs. The narrower psi subgroup is not required to map the generic psi class.
  target_ids:
  - GO:0043847
  field_paths:
  - components#chi_subunit.grounding_status
  - components#psi_subunit.grounding_status
  - discussions#resolve_pol_iii_chi_psi_groundings
  evidence_ids:
  - micro-record-2
  - micro-policy
  - micro-ipr-IPR007459
  - micro-ipr-IPR004615
  - micro-ipr-IPR018382
  - micro-up-P28905
  - micro-up-P28632
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_polymerase_iii_clamp_loader_chi_psi_subcomplex.yaml
    role: maintained scientific record
  rule_id: Source-specific identity, scope and exact component grounding
  native_severity: minor
  normalization_reason: The maintained complex identity, correct protein examples
    and supported coarse function remain intact; the defect is localized source precision
    or exact family grounding.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T054335Z-dna-polymerase-iii-clamp-loader-chi-psi-subcomplex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2919
- finding_id: septin-dinoflagellate_sulcus-F1
  issue_key: dinoflagellate-sulcus-go-definition-reference-attribution
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Correct the claimed GO sulcus definition reference
  description: The record’s PMID7002229 note calls Taylor1980 the review cited by
    GO0097612, and the matching DOI note calls it corroboration for that definition
    xref. The inspected current GO0097612 definition.xrefs lists PMID20561119, Tree
    of Life and Wikipedia; native PMID20561119 is Iwataki et al.2010. Taylor7002229
    is a valid paper and is cited by the neighboring notch term, but that does not
    establish this claimed exact GO-to-paper link. No claim is made that Taylor lacks
    sulcus content or that the historical failed-access notes are false. Fresh current
    QuickGO and exact MED records independently reconfirm this same localized attribution
    defect. Preserve the legitimate posterior/ventral anatomy and historical access
    statements.
  target_ids:
  - GO:0097612
  field_paths:
  - evidence[3].notes
  - evidence[4].notes
  evidence_ids:
  - septin-record-dinoflagellate_sulcus
  - septin-original-dinoflagellate_sulcus
  - septin-go
  - septin-taylor1980-meta
  - septin-iwataki2010-meta
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dinoflagellate_sulcus.yaml
    role: maintained scientific record
  rule_id: Exact claim-level source attribution and current ontology provenance
  native_severity: minor
  normalization_reason: The anatomical definition, exact class and topology remain
    correct and authority-supported. The defect is a localized bibliographic relationship,
    not wrong structure identity or unsupported biology.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T054307Z-dinoflagellate-sulcus-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2915
actions:
- action_id: micro-A1
  finding_ids:
  - micro-F1
  target_ids:
  - GO:0120217
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_gyrase_complex.yaml
    role: maintained scientific record
  description: In separately authorized record curation, qualify6RKU as the domain-focused
    State1 deposition, or use the verified6RKW entry for an explicitly overall-model
    canonical example; retain6RKU where its GyrA/B entity mapping is the relevant
    evidence.
  acceptance_checks:
  - Keep K12 source distinct from BL21(DE3) expression.
  - Do not describe full sample sequences as proof of complete atomic coverage.
  - Preserve supported identifiers, examples and biological scope; pass applicable
    native validation.
  - Preserve historical discussions.rationale, posed_date and dated history; append
    provenance and update current notes/prompt only as supported.
  - No record edits occur in this review PR. Keep primary body/abstract/authority
    tiers and experimental strain/formation limits explicit.
- action_id: micro-A2
  finding_ids:
  - micro-F2
  target_ids:
  - GO:0044775
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_polymerase_iii_beta_sliding_clamp_processivity_factor_complex.yaml
    role: maintained scientific record
  description: In separately authorized record curation, retain GO0044775 and the
    bacterial DnaN identity, but replace the cross-class stoichiometry sentence with
    source-backed bacterial beta scope; use bacterial or explicitly E.coli wording
    in the corresponding component claims. Record the upstream GO conflict explicitly,
    and keep PCNA/phage analogies separate.
  acceptance_checks:
  - Do not silently relabel PCNA as a PolIII beta subcomplex.
  - Preserve the correct dimeric E.coli canonical example and P0A988.
  - Do not assert invariant oligomerization for every DnaN-derived isoform.
  - Preserve supported identifiers, examples and biological scope; pass applicable
    native validation.
  - Preserve historical discussions.rationale, posed_date and dated history; append
    provenance and update current notes/prompt only as supported.
  - No record edits occur in this review PR. Keep primary body/abstract/authority
    tiers and experimental strain/formation limits explicit.
- action_id: micro-A3
  finding_ids:
  - micro-F3
  target_ids:
  - GO:0044775
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_polymerase_iii_beta_sliding_clamp_processivity_factor_complex.yaml
    role: maintained scientific record
  description: In separately authorized record curation, use verified IPR001001 for
    the DnaN beta class and update current grounding notes/TODO, preserving the taxon-specific
    example.
  acceptance_checks:
  - Confirm native family type/name/signatures and P0A988 membership; do not substitute
    clamp domains.
  - Preserve supported identifiers, examples and biological scope; pass applicable
    native validation.
  - Preserve historical discussions.rationale, posed_date and dated history; append
    provenance and update current notes/prompt only as supported.
  - No record edits occur in this review PR. Keep primary body/abstract/authority
    tiers and experimental strain/formation limits explicit.
- action_id: micro-A4
  finding_ids:
  - micro-F4
  target_ids:
  - GO:0043847
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_polymerase_iii_clamp_loader_chi_psi_subcomplex.yaml
    role: maintained scientific record
  description: In separately authorized record curation, use the two verified exact
    families and update current grounding status/notes/TODO, preserving correct proteins,1:1
    stoichiometry and gamma-versus-tau edge scope.
  acceptance_checks:
  - Check native whole-family type/name/signature and example xrefs.
  - Do not use a broad superfamily or promote stale family functional prose over primary
    experiments.
  - Preserve supported identifiers, examples and biological scope; pass applicable
    native validation.
  - Preserve historical discussions.rationale, posed_date and dated history; append
    provenance and update current notes/prompt only as supported.
  - No record edits occur in this review PR. Keep primary body/abstract/authority
    tiers and experimental strain/formation limits explicit.
- action_id: septin-dinoflagellate_sulcus-A1
  finding_ids:
  - septin-dinoflagellate_sulcus-F1
  target_ids:
  - GO:0097612
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dinoflagellate_sulcus.yaml
    role: maintained scientific record
  description: Correct the current GO0097612 bibliography description to its inspected
    PMID20561119 reference, verifying any new bibliography and retaining the actual
    readable tier. Taylor may remain as clearly labeled general background or historical
    context if useful, but must not be described as this current GO definition’s xref.
    Preserve the valid morphology and honest historical access limitation. Change
    only current scientific notes or append a clearly dated clarification through
    separately authorized guarded curation; preserve all dated rationale/history.
    Record curation stays outside this review PR.
  acceptance_checks:
  - The exact current GO0097612-to-PMID attribution agrees with the native definition.xrefs
    response.
  - Any Taylor evidence is explicitly general or historical rather than falsely attributed
    to the current GO definition.
  - Native schema, strict and CURIE checks pass after separately authorized curation.
limitations:
- 'Gyrase, beta clamp and chi/psi independent review: Only gyrase, beta clamp and
  chi/psi are scientifically judged by this slice. Other seven targets and neighboring/group/category
  issues are not disposed. All records, originals, Git and GitHub remain unchanged.'
- 'Gyrase, beta clamp and chi/psi independent review: Gyrase2019 genuine JATS read
  only at the declared Introduction/Results/Discussion/Methods and text captions.
  No figure pixels, raw coordinates, supplements or complete catalytic-cycle reanalysis.
  RCSB sample sequences/entity mapping are distinct from incomplete modeled coordinates;
  K12 source differs from BL21(DE3) expression.'
- 'Gyrase, beta clamp and chi/psi independent review: Kong1992 genuine author PDF
  read at declared pp425,427,432–434 passages/text captions only; no pixels or complete-paper
  certification. Central DNA fit is modeled, not an observed DNA co-crystal. Archaeal
  PCNA Matsumiya2001 is full primary abstract/native authority only, not body.'
- 'Gyrase, beta clamp and chi/psi independent review: XiaoIII/IV current full primary
  abstracts are read; publisher bodies returned403. Olson1995 main pp29570–29576 text/Methods/Results/Discussion/tables/captions
  were read, not raw figures. Its artificial-operon MC1061 and purified-assay scope
  does not establish universal native essentiality or an SSB contact measurement.'
- 'Gyrase, beta clamp and chi/psi independent review: McHenry2003 is a secondary-review
  abstract only. GO/UniProt/InterPro reference annotations and exact identifiers are
  not newly verified primary experiments for all linked papers. Historical generic
  functional descriptions and AI-generated dataset prose are not promoted to primary
  biology.'
- 'Gyrase, beta clamp and chi/psi independent review: GO0044775 genuinely contains
  the disputed cross-class definition and O73947 xref. This is an upstream scientific
  scope conflict, not a local misquotation; retain exact structure identity and E.coli
  examples. Native beta* isoform notes prevent an invented invariant dimer claim for
  every DnaN-derived product.'
- 'Gyrase, beta clamp and chi/psi independent review: Fresh five-strain precise1k
  dataset is not exact experimental BL21(DE3)/MC1061 coverage. Seven exact native
  loci each return201 module rows; only holD exceeds module145 threshold, independently
  matched to its70-gene list. Threshold-negative results are not gene absence or dispensability;
  the hit does not establish physical association, direct regulation, formation or
  localization. AI module summary and activity stories excluded.'
- 'Gyrase, beta clamp and chi/psi independent review: Historical runner unavailable/exit1
  is dated2026-11-03T00:49:00Z, not a fresh invocation. Six own native protein commands
  are actual source-head receipts:5reviewed examples,5COVERED plus2 external UNANCHORED_WITH_UNIPROT
  typed actors. No false all-covered or full biological validation claim.'
- 'Gyrase, beta clamp and chi/psi independent review: All four inherited findings
  remain open with exact predecessor identities. Current family-grounding actions
  preserve dated rationale/history and correct current mapping separately. No new
  scientific finding, compulsory optional example, new experiment or universal formation
  classification is proposed.'
- 'Gyrase, beta clamp and chi/psi independent review: Root owns global QC, later saved-head
  gates, CI and queue. These later stages are not certified by this source report;
  source-access failures are contextual diagnostics, not scientific refutations.'
- 'Apical groove, horn, cingulum and epicone independent review: Iwataki2010 remains
  complete primary abstract/metadata only after fresh Wiley403. No original2010microscopy
  pixels, fullMethods, experimental strain or supplementary movies are certified.'
- 'Apical groove, horn, cingulum and epicone independent review: Gomez2017 genuine
  fresh JATS was read only at the declaredMethodsS3/ResultsS8includingS9/TaxonomyS10/ConclusionsS30/Table1/Fig3–5textcaptions.
  No figure pixels, all-figure review, phylogenetic reanalysis or supplements. Formal
  U-shaped diagnosis is distinguished from its own unreadable groove inLM/obscuredSEM.'
- 'Apical groove, horn, cingulum and epicone independent review: Taylor1980 is a secondary-review
  complete indexedabstract/metadata tier; freshSD403 supplies no body. No detailed
  anatomy or experiments are inferred from its title/abstract alone.'
- 'Apical groove, horn, cingulum and epicone independent review: ToL is authored expert
  secondary terminology, not a primary assembly experiment; exactmainorientation and
  relevantflagellarscope read. Textlicence does not establish image rights; no images
  downloaded for reuse or judged as pixels.'
- 'Apical groove, horn, cingulum and epicone independent review: All four records
  are physical morphological regions with no molecular inventories, images or quantities.
  Zero native proteinexamples/nodes is an empty-inventory pass, not proof of absent
  proteins or molecular completeness. Unknown formation necessity and optionalfields
  are not findings.'
- 'Apical groove, horn, cingulum and epicone independent review: Direct ontology relations
  are distinguished from inheritedhorn→apex→epicone containment. Epicone has_part
  is descriptive scope, not universal apicalgroove prevalence. Dinophyceaeonly_in_taxon/VARIABLE
  and speciesdiagnosis do not certify a taxon-wide numerical census.'
- 'Apical groove, horn, cingulum and epicone independent review: All four structured-source
  exclusions are genuinely morphology-only; freshcompletecatalogue also lacks naturalhostcoverage.
  No downstream bacterialproxyquery or negative biological inference. Historicalrunnerfailure
  remains2026-11-03T00:49Z, not a freshinvocation.'
- 'Apical groove, horn, cingulum and epicone independent review: Four originalpairs/52historicalinputoccurrences/47currentinputhashes
  verified; all fourtargetsunchanged. Original corpus checks remain historical. Parent
  owns currentglobalQC, post-save/finalhead/CI/queue/merge gates; none precertified
  here.'
- 'Apical groove, horn, cingulum and epicone independent review: No original scientific
  findings/actions or new recordcuration findings in this slice. Three historicalfailed-accesskind
  occurrences require successorcorrection; originalfiles stayimmutable. No neighboring/group/category
  issue disposition inferred.'
- 'Hypocone, sulcal notch and sulcus independent review: All three targets are unchanged
  from original frozen bytes. One inherited minor sulcus bibliography finding remains
  open; hypocone and sulcal notch retain qualified positive scientific assessments.
  No new scientific finding or neighbor disposition.'
- 'Hypocone, sulcal notch and sulcus independent review: Current morphology is supported
  by exact GO authority and directly inspected authored expert terminology. Taylor1980
  secondary review and Iwataki2010 primary paper were read only at complete native
  abstract/metadata tier; current403 publisher responses are validation context, not
  scientific bodies. Iwataki is species-specific Cochlodinium polykrikoides evidence,
  not a class-wide experiment. No Methods strain,paper figures,supplements or microscopy
  pixels inspected.'
- 'Hypocone, sulcal notch and sulcus independent review: Current GO0097684 anterior
  wording conflicts with posterior antapex in GO0097618 and expert orientation. The
  assigned targets use the correct supported posterior orientation; no neighboring
  record repair or universal endorsement of every ontology sentence is claimed.'
- 'Hypocone, sulcal notch and sulcus independent review: No localized constituent
  inventory, molecular formation requirement, quantitative prevalence census or physical
  dimension established. Three records have0examples/0typedprotein nodes; six native
  successes reflect empty scope. Optional fields are not automatic findings.'
- 'Hypocone, sulcal notch and sulcus independent review: Three original physical/morphology
  prose exclusions are legitimate. Official catalogue complete20organism response
  has no Dinophyceae match; no unrelated host proxy, downstream module query or biological
  absence inference. Historical runner receipt remains Nov3 00:49Z unavailable; no
  new runner invocation.'
- 'Hypocone, sulcal notch and sulcus independent review: Two original micro50-taylor1980-publisher
  rows need kind-only database→validation correction; both already stated HTTP403/context_only/no
  body. Their original timestamps and bundle bytes remain preserved; current publisher
  failures are separate observations.'
- 'Hypocone, sulcal notch and sulcus independent review: All45 original historical
  input occurrences and three native YAML/Markdown pairs verified. Historical batch26
  global gate execution was explicitly reused at the old shared base and is not a
  provenance defect or a new-head success claim. Root current global gates, saved-head
  check, CI,queue,merge and deletion are separate attestations.'
- 'Hypocone, sulcal notch and sulcus independent review: Initial scratch HTML extraction
  was corrected for unavailable bs4 and actual Latin-1 encoding, without repository
  edits or scientific source substitution. Source packets are external scratch; no
  additional maintained context outside the26 listed inputs was used.'
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
- 'This ten-record successor preserves all 20 original artifacts and exact predecessor
  finding lineage. Bundle issues #2912, #2913 and #2914 cover one stale target, three
  formal applicability exclusions and seven failed-access kind occurrences.'
- DNA gyrase current changes add only history and InterPro groundings to two existing
  component_ref graph nodes. Those family identities and their graph usage are reassessed
  separately from the original deposition-scope finding.
- 'The native inventory contains five component protein examples and seven typed GENE_OR_PROTEIN
  nodes: five COVERED and two UNANCHORED_WITH_UNIPROT contextual DnaX/SSB nodes. The
  latter are contextual partners rather than missing chi/psi constituents. Seven morphology
  records have zero protein examples and zero typed protein nodes; their zero-exit
  checks do not imply experimental constituent coverage.'
- All historical failed publisher responses already disclose HTTP403 and context_only
  support. Their successor classification is validation; no successful article-body
  access is retroactively claimed. Fresh, retained and unavailable source tiers keep
  their actual timestamps and inspection scopes.
- Record curation remains separate, preserving dated rationale and history with appended
  clarification where needed. This review-only PR edits no records. Final post-save
  validation, saved-head independent acceptance, final-head CI and merge-group CI
  are later gates.
- 'Current GO source wording is not assumed infallible: the beta-clamp finding explicitly
  preserves the faithful upstream quotation while distinguishing bacterial DnaN from
  archaeal/eukaryotic PCNA. Correct E. coli dimer evidence is retained without claiming
  invariant oligomerization of every derived isoform.'
- Sulcus current GO definition xrefs identify Iwataki2010 PMID20561119, whereas the
  neighboring notch cites Taylor1980 PMID7002229. The finding corrects only the sulcus
  attribution and does not claim that Taylor lacks sulcus content or that historical
  failed-access statements are false.
- Gomez2017 supports the formal Margalefidinium name transfer; its own light-microscopy
  observations did not resolve the groove and its SEM details were obscured. Iwataki2010
  primary abstract separately supports the dorsal U-shaped groove. Text/caption inspection
  is not microscopy-pixel inspection.
- 'Full local QC, all 20 focused schema/strict checks and all 20 native protein checks
  passed before saving. Existing #2514 retains the native bulk-PMID reporting limitation;
  unchanged resolver requests bounded to at most 50 verified all 909 affected PMIDs,
  without changing the original report or cache.'
- Gyrase sources distinguish closed cleavage-domain deposition 6RKU from overall model
  6RKW, while retaining correct GyrA/GyrB identity, K-12 source, 2:2 protein counts
  and BL21(DE3) expression limits. Full sample sequences are not complete modeled
  coordinates. Chi/psi 1:1 membership, psi-to-gamma and assembled dimer-to-tau/gamma
  assays remain separately scoped; SSB bridge authority is not attributed to the Olson
  purified-binding assay.
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T054302Z-dinoflagellate-apical-groove-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T054304Z-dinoflagellate-apical-horn-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T054304Z-dinoflagellate-cingulum-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T054305Z-dinoflagellate-epicone-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T054306Z-dinoflagellate-hypocone-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T054307Z-dinoflagellate-sulcal-notch-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T054307Z-dinoflagellate-sulcus-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T054333Z-dna-gyrase-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T054334Z-dna-polymerase-iii-beta-sliding-clamp-processivity-factor-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T054335Z-dna-polymerase-iii-clamp-loader-chi-psi-subcomplex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
links:
- https://github.com/CultureBotAI/CellStructureMech/pull/2387
- https://github.com/CultureBotAI/CellStructureMech/issues/2514
- https://github.com/CultureBotAI/CellStructureMech/issues/2912
- https://github.com/CultureBotAI/CellStructureMech/issues/2913
- https://github.com/CultureBotAI/CellStructureMech/issues/2914
- https://github.com/CultureBotAI/CellStructureMech/issues/2915
- https://github.com/CultureBotAI/CellStructureMech/issues/2916
- https://github.com/CultureBotAI/CellStructureMech/issues/2917
- https://github.com/CultureBotAI/CellStructureMech/issues/2918
- https://github.com/CultureBotAI/CellStructureMech/issues/2919
```
