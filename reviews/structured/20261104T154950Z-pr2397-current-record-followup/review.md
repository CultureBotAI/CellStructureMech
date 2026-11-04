# PR 2397: current-input review of ten records and adversarial follow-up

- Review: 20261104T154950Z-pr2397-current-record-followup
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-11-04T15:21:52.094888Z
- Finished UTC: 2026-11-04T15:49:50Z
- Reviewer: Codex root synthesis with three independent read-only adversarial reviewers (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Independent current-source review of all ten records refreshes three stale reviews (MICOS, MIM and MIS12/MIND). Four minor record-curation findings remain open across MIM, MIS12/MIND and TOM; seven records pass with explicit source and scope limitations. The immutable successor corrects ten structured-source applicability assessments and eleven historical evidence-kind occurrences while preserving the original bundles and exact inherited finding lineage. No maintained records are edited.

## Scope And Provenance

Exact ten-record PR cohort reassessed against current main 52a4db8d611558a6bc665e275e207f05c1eb81b2. Changed inputs are substantively reassessed. Scientific records remain unchanged.

Selection: Complete cohort of ten maintained records reviewed in original PR head 32d5d3d0cd6124c17063e87c175be8945602148f.
Coverage: full; 10 reviewed / 10 in the declared population.
Source: working_tree at Git base c9fe63bdff984abad241949c21dab3b13e975d1f.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:mic10_subcomplex | data/structures/other/mic10_subcomplex.yaml | maintained | MIC10 subcomplex |
| cellstructuremech:mic60_mic19_complex | data/structures/other/mic60_mic19_complex.yaml | maintained | Mic60-Mic19 complex |
| GO:0061617 | data/structures/other/micos_complex.yaml | maintained | MICOS complex |
| GO:0140595 | data/structures/other/mim_complex.yaml | maintained | MIM complex |
| GO:0000444 | data/structures/other/mis12_mind_type_complex.yaml | maintained | MIS12/MIND type complex |
| GO:0042720 | data/structures/other/mitochondrial_inner_membrane_peptidase_complex.yaml | maintained | mitochondrial inner membrane peptidase complex |
| cellstructuremech:mitochondrial_lon_protease_complex | data/structures/other/mitochondrial_lon_protease_complex.yaml | maintained | mitochondrial Lon protease complex |
| cellstructuremech:mitochondrial_multifunctional_assembly | data/structures/other/mitochondrial_multifunctional_assembly.yaml | maintained | mitochondrial multifunctional assembly |
| GO:0005742 | data/structures/other/mitochondrial_outer_membrane_translocase_complex.yaml | maintained | mitochondrial outer membrane translocase complex |
| GO:0035632 | data/structures/other/mitochondrial_prohibitin_complex.yaml | maintained | mitochondrial prohibitin complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full native QC | passed | True | cellstructuremech:mic10_subcomplex, cellstructuremech:mic60_mic19_complex, GO:0061617, GO:0140595, GO:0000444, GO:0042720, cellstructuremech:mitochondrial_lon_protease_complex, cellstructuremech:mitochondrial_multifunctional_assembly, GO:0005742, GO:0035632 | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| Native label correspondence | passed | True | cellstructuremech:mic10_subcomplex, cellstructuremech:mic60_mic19_complex, GO:0061617, GO:0140595, GO:0000444, GO:0042720, cellstructuremech:mitochondrial_lon_protease_complex, cellstructuremech:mitochondrial_multifunctional_assembly, GO:0005742, GO:0035632 | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| TraitMech references | passed | True | cellstructuremech:mic10_subcomplex, cellstructuremech:mic60_mic19_complex, GO:0061617, GO:0140595, GO:0000444, GO:0042720, cellstructuremech:mitochondrial_lon_protease_complex, cellstructuremech:mitochondrial_multifunctional_assembly, GO:0005742, GO:0035632 | Native TraitMech check passed: all 10 links resolve with matching labels against the 1130-trait source index. |
| Pinned governed files | passed | True | cellstructuremech:mic10_subcomplex, cellstructuremech:mic60_mic19_complex, GO:0061617, GO:0140595, GO:0000444, GO:0042720, cellstructuremech:mitochondrial_lon_protease_complex, cellstructuremech:mitochondrial_multifunctional_assembly, GO:0005742, GO:0035632 | All 22 governed artifacts match the pinned CLAW revision. |
| Native identifier resolver | passed | True | cellstructuremech:mic10_subcomplex, cellstructuremech:mic60_mic19_complex, GO:0061617, GO:0140595, GO:0000444, GO:0042720, cellstructuremech:mitochondrial_lon_protease_complex, cellstructuremech:mitochondrial_multifunctional_assembly, GO:0005742, GO:0035632 | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified all 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| validate cellstructuremech:mic10_subcomplex | passed | True | cellstructuremech:mic10_subcomplex | Documented focused command passed. |
| validate-strict cellstructuremech:mic10_subcomplex | passed | True | cellstructuremech:mic10_subcomplex | Documented focused command passed. |
| validate cellstructuremech:mic60_mic19_complex | passed | True | cellstructuremech:mic60_mic19_complex | Documented focused command passed. |
| validate-strict cellstructuremech:mic60_mic19_complex | passed | True | cellstructuremech:mic60_mic19_complex | Documented focused command passed. |
| validate GO:0061617 | passed | True | GO:0061617 | Documented focused command passed. |
| validate-strict GO:0061617 | passed | True | GO:0061617 | Documented focused command passed. |
| validate GO:0140595 | passed | True | GO:0140595 | Documented focused command passed. |
| validate-strict GO:0140595 | passed | True | GO:0140595 | Documented focused command passed. |
| validate GO:0000444 | passed | True | GO:0000444 | Documented focused command passed. |
| validate-strict GO:0000444 | passed | True | GO:0000444 | Documented focused command passed. |
| validate GO:0042720 | passed | True | GO:0042720 | Documented focused command passed. |
| validate-strict GO:0042720 | passed | True | GO:0042720 | Documented focused command passed. |
| validate cellstructuremech:mitochondrial_lon_protease_complex | passed | True | cellstructuremech:mitochondrial_lon_protease_complex | Documented focused command passed. |
| validate-strict cellstructuremech:mitochondrial_lon_protease_complex | passed | True | cellstructuremech:mitochondrial_lon_protease_complex | Documented focused command passed. |
| validate cellstructuremech:mitochondrial_multifunctional_assembly | passed | True | cellstructuremech:mitochondrial_multifunctional_assembly | Documented focused command passed. |
| validate-strict cellstructuremech:mitochondrial_multifunctional_assembly | passed | True | cellstructuremech:mitochondrial_multifunctional_assembly | Documented focused command passed. |
| validate GO:0005742 | passed | True | GO:0005742 | Documented focused command passed. |
| validate-strict GO:0005742 | passed | True | GO:0005742 | Documented focused command passed. |
| validate GO:0035632 | passed | True | GO:0035632 | Documented focused command passed. |
| validate-strict GO:0035632 | passed | True | GO:0035632 | Documented focused command passed. |
| Supplemental bounded PMID authority checks | passed | True | cellstructuremech:mic10_subcomplex, cellstructuremech:mic60_mic19_complex, GO:0061617, GO:0140595, GO:0000444, GO:0042720, cellstructuremech:mitochondrial_lon_protease_complex, cellstructuremech:mitochondrial_multifunctional_assembly, GO:0005742, GO:0035632 | 909 PMIDs all OK in bounded native requests; full-command limitations remain separate. |
| Official structured-source applicability and covered-dataset cross-checks | not_applicable | False | cellstructuremech:mic10_subcomplex, cellstructuremech:mic60_mic19_complex, GO:0061617, GO:0140595, GO:0000444, GO:0042720, cellstructuremech:mitochondrial_lon_protease_complex, cellstructuremech:mitochondrial_multifunctional_assembly, GO:0005742, GO:0035632 | All ten records contain positive molecular or pathway claims requiring structured-source applicability assessment. The current complete official catalogue covers 20 organisms and 28 datasets, with no matching natural biological host for these eukaryotic targets. Recombinant Escherichia coli and unrelated Sulfolobus datasets are not substitutes. Preserve the actual historical Nov3 runner PermissionError as historical; current primary literature and native authority checks provide the bounded fallback. No fresh successful adapter invocation is claimed. |
| Independent claim-level source review | passed | True | cellstructuremech:mic10_subcomplex, cellstructuremech:mic60_mic19_complex, GO:0061617, GO:0140595, GO:0000444, GO:0042720, cellstructuremech:mitochondrial_lon_protease_complex, cellstructuremech:mitochondrial_multifunctional_assembly, GO:0005742, GO:0035632 | Three read-only reviewers covered the complete ten-record cohort, including changed inputs, with explicit scientific findings and source-access limits. Final artifact/head acceptance occurs after saving. |
| Retained historical adapter runner availability | unavailable | False | cellstructuremech:mic10_subcomplex, cellstructuremech:mic60_mic19_complex, GO:0061617, GO:0140595, GO:0000444, GO:0042720, cellstructuremech:mitochondrial_lon_protease_complex, cellstructuremech:mitochondrial_multifunctional_assembly, GO:0005742, GO:0035632 | Historical00:49Z invocation unavailable due to OS access restriction. Official catalogue fallback was inspected separately; no fresh invocation is claimed. Actual historical exit1 is retained in the evidence receipt; the native unavailable-check model has no execution exit-code field. |
| Native MIC10 subcomplex UniProt verify check | passed | True | cellstructuremech:mic10_subcomplex | 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native MIC10 subcomplex UniProt causal check | passed | True | cellstructuremech:mic10_subcomplex | 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native Mic60-Mic19 complex UniProt verify check | passed | True | cellstructuremech:mic60_mic19_complex | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native Mic60-Mic19 complex UniProt causal check | passed | True | cellstructuremech:mic60_mic19_complex | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native MICOS complex UniProt verify check | passed | True | GO:0061617 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native MICOS complex UniProt causal check | passed | True | GO:0061617 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native MIM complex UniProt verify check | passed | True | GO:0140595 | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native MIM complex UniProt causal check | passed | True | GO:0140595 | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native MIS12/MIND type complex UniProt verify check | passed | True | GO:0000444 | 4 represented protein examples; 5 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native MIS12/MIND type complex UniProt causal check | passed | True | GO:0000444 | 4 represented protein examples; 5 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native mitochondrial inner membrane peptidase complex UniProt verify check | passed | True | GO:0042720 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native mitochondrial inner membrane peptidase complex UniProt causal check | passed | True | GO:0042720 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native mitochondrial Lon protease complex UniProt verify check | passed | True | cellstructuremech:mitochondrial_lon_protease_complex | 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native mitochondrial Lon protease complex UniProt causal check | passed | True | cellstructuremech:mitochondrial_lon_protease_complex | 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native mitochondrial multifunctional assembly UniProt verify check | passed | True | cellstructuremech:mitochondrial_multifunctional_assembly | 5 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native mitochondrial multifunctional assembly UniProt causal check | passed | True | cellstructuremech:mitochondrial_multifunctional_assembly | 5 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native mitochondrial outer membrane translocase complex UniProt verify check | passed | True | GO:0005742 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native mitochondrial outer membrane translocase complex UniProt causal check | passed | True | GO:0005742 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native mitochondrial prohibitin complex UniProt verify check | passed | True | GO:0035632 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native mitochondrial prohibitin complex UniProt causal check | passed | True | GO:0035632 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |

## Scientific And Domain Assessments

### Current and historical artifact verification

provenance: supported. Targets: cellstructuremech:mic10_subcomplex.

Complete current record and original native pair read; all 44 declared historical input occurrences and six deterministic original commands passed. Current target equals original target and reviewed main.

### Whole-record structured-source applicability

scope: concern. Targets: cellstructuremech:mic10_subcomplex.

Positive Mic10/Mic12/Mic26/Mic27 assembly, lipid regulation and contact-site pathways makes the original formal expression-only exemption unsupported. Fresh full catalogue has no matched biological host; no downstream proxy is substituted. Historical unavailable runner receipt remains old, not a new invocation.

### Actual native protein inventory and coverage

schema: supported. Targets: cellstructuremech:mic10_subcomplex.

4 reviewed S288C protein examples and4 COVERED typed nodes. Generic verify success is not an assertion that an empty inventory was populated. Root current commands and logs are independently hash-bound.

### Current scientific disposition and original finding lineage

scope: supported. Targets: cellstructuremech:mic10_subcomplex.

No original scientific finding/action exists to carry, close or reject. Current full-record reassessment supports a qualified pass with stated access, assay, taxon and architecture limits. Review-bundle corrections are separate from record curation.

### Current and historical artifact verification

provenance: supported. Targets: cellstructuremech:mic60_mic19_complex.

Complete current record and original native pair read; all 44 declared historical input occurrences and six deterministic original commands passed. Current target equals original target and reviewed main.

### Whole-record structured-source applicability

scope: concern. Targets: cellstructuremech:mic60_mic19_complex.

Positive Mic60/Mic19 binding, remodeling and junction-formation functions makes the original formal expression-only exemption unsupported. Fresh full catalogue has no matched biological host; no downstream proxy is substituted. Historical unavailable runner receipt remains old, not a new invocation.

### Actual native protein inventory and coverage

schema: supported. Targets: cellstructuremech:mic60_mic19_complex.

2 reviewed S288C protein examples and2 COVERED typed nodes. Generic verify success is not an assertion that an empty inventory was populated. Root current commands and logs are independently hash-bound.

### Current scientific disposition and original finding lineage

scope: supported. Targets: cellstructuremech:mic60_mic19_complex.

No original scientific finding/action exists to carry, close or reject. Current full-record reassessment supports a qualified pass with stated access, assay, taxon and architecture limits. Review-bundle corrections are separate from record curation.

### Current and historical artifact verification

provenance: supported. Targets: GO:0061617.

Complete current record and original native pair read; all 44 declared historical input occurrences and six deterministic original commands passed. Original target differs only by reciprocal has_part/history; substantive source assessment below.

### Whole-record structured-source applicability

scope: concern. Targets: GO:0061617.

Positive six-subunit MICOS and membrane organization/contact-site functions makes the original formal expression-only exemption unsupported. Fresh full catalogue has no matched biological host; no downstream proxy is substituted. Historical unavailable runner receipt remains old, not a new invocation.

### Actual native protein inventory and coverage

schema: supported. Targets: GO:0061617.

0 protein examples and0 typed GENE_OR_PROTEIN nodes; empty check is not molecular validation. Generic verify success is not an assertion that an empty inventory was populated. Root current commands and logs are independently hash-bound.

### Current scientific disposition and original finding lineage

scope: supported. Targets: GO:0061617.

No original scientific finding/action exists to carry, close or reject. Current full-record reassessment supports a qualified pass with stated access, assay, taxon and architecture limits. Review-bundle corrections are separate from record curation.

### Exact structure identities and typed hierarchy

identity: supported. Targets: cellstructuremech:mic10_subcomplex, cellstructuremech:mic60_mic19_complex, GO:0061617.

MICOS remains active exact GO0061617; the two minted subcomplexes are narrower source-defined structures with reciprocal parthood. Current bounded text searches returned no exact-named hits; this is not exhaustive ontology absence. GO0098800 is is_a parent and GO0005743 containing membrane, not alternate identities.

### Four subunit families and lineage boundaries

grounding: supported. Targets: cellstructuremech:mic10_subcomplex.

IPR007512 Mic10 and IPR031463 Mic12 are exact families; IPR033181 is fungal Mic26 and IPR061953 Saccharomycetaceae Mic27. Both lineage labels are retained. Normal four-protein module is compatible with conditional Mic10/Mic12/Mic27 assembly; no forced broad family or missing optional row.

### Four current reviewed yeast references

identity: supported. Targets: cellstructuremech:mic10_subcomplex.

MIC10/Q96VH5, MIC12/P38341, MIC26/P50087 and MIC27/P50945 each match reviewed S288C 559292 with correct primary symbols, loci and aliases; each exact current query has one result. Identity-only examples do not retrofit S288C onto W303 or YPH499 experiments.

### Mic26/Mic27 antagonism and cardiolipin

evidence: supported. Targets: cellstructuremech:mic10_subcomplex.

Rampelt native gels/crosslinking in YPH499 support larger Mic10 assemblies after mic26 deletion and opposite effects after mic27 deletion, with cardiolipin stabilization. These do not give universal native copy counts or a directly mapped cardiolipin-binding site. Record preserves the four-subunit scope.

### Conditional subcomplex assembly and junction proximity

evidence: supported. Targets: cellstructuremech:mic10_subcomplex.

Friedman W303 reconstitution supports Mic10 dependence of Mic27 foci and reduced rather than abolished foci without Mic12 in the tested context. Crosslinked conditional core and normal four-member module differ. Crista-junction placement relies on fluorescent-marker proximity after unsuccessful immuno-EM, which the record explicitly qualifies.

### ERMES, Vps13 and lipids

scope: supported. Targets: cellstructuremech:mic10_subcomplex.

Tirrell independently separates contact proximity and ERMES functional dependence from direct obligatory template binding; Vps13 bypass is compatible. Cardiolipin, ERMES andVps13 remain context/regulators rather than constituent subunits. Native architecture remains unresolved.

### All five current assembly edges

graph: supported. Targets: cellstructuremech:mic10_subcomplex.

Mic10 oligomerization, Mic26 destabilization, Mic27 stabilization and the Mic10/Mic12 effects on Mic27 foci match the precise assays. Types/component_refs and native grounding agree; no universal formation necessity is silently added.

### Complete Figure3 pixels, caption and licence

evidence: supported. Targets: cellstructuremech:mic10_subcomplex.

Maintained image is byte-identical to fresh source; full A–G panels were visually inspected. W303 confocal/co-IP/counting context, OTHER modality and explicit nonmolecular-image caption match; CC BY 4.0 article permissions and attribution support reuse. No raw imaging reanalysis or new package MD5 verification claimed.

### Mic60 family and unresolved Mic19 candidate

grounding: supported. Targets: cellstructuremech:mic60_mic19_complex.

IPR019133 supports exact Mic60. NativeP43594 carries IPR012471/PF07956, but the authority calls it uncharacterised fungal DUF1690, not exact universal Mic19. REVIEWED_LABEL_ONLY with open source-neutral question is valid; no optional grounding mandate or invented absence claim.

### Current Mic60/Mic19 instances and reference strain

identity: supported. Targets: cellstructuremech:mic60_mic19_complex.

Reviewed P36112/MIC60 aliases FCJ1/AIM28/FMP13 and P43594/MIC19 aliases AIM13/MCS19 match S288C 559292. Both current exact queries return one entry. These references remain distinct from YPH499 cellular assays and thermophilic purified constructs.

### Direct binding, liposome recruitment and remodeling

evidence: supported. Targets: cellstructuremech:mic60_mic19_complex.

Hessenberger purified C. thermophilum Mic60sol/Mic19 supports direct CHCH/mitofilin binding, recruitment and enhanced Folch tubulation, with LBS/domain controls. The current graph explicitly separates constructs and yeast rescue. Leakage is not physiological barrier behavior.

### Construct-specific tetramer and strut model

evidence: supported. Targets: cellstructuremech:mic60_mic19_complex.

Bock-Bierbaum L. thermotolerans coiled-coil and C. thermophilum engineered complexes support tetramer/heteromer models; YPH499 assays are separate. Native filament identity and strut/barrier interpretation remain unresolved. Current notes do not assert universal 4:4 or directly observed native barrier.

### All five current remodeling edges

graph: supported. Targets: cellstructuremech:mic60_mic19_complex.

Direct Mic19/Mic60 binding, lipid recruitment, higher-order assembly and tubulation edges are supported at their expressly in-vitro construct scope. Explicit lipid-dependent complex is not confused with an obligatory extra protein. Native types and references agree.

### Complete Figure4 pixels, caption and licence

evidence: supported. Targets: cellstructuremech:mic60_mic19_complex.

Fresh image equals maintained bytes; complete a–i visually inspected. YPH499 affinity/growth/cryo-TEM500 nm/counts/respiratory activities are contextual cellular evidence, not an isolatedMic60–Mic19 structure. Full-multipanel OTHER modality and CC BY 4.0 rights are consistent.

### Protein-example localization bibliography

evidence: supported. Targets: cellstructuremech:mic10_subcomplex, cellstructuremech:mic60_mic19_complex.

Current native location comments and exact indexed PMIDs support the cited reference attributions. Reinders 2006, Huh 2003, Rabl 2009 and von der Malsburg 2011 were read at complete indexed abstract/native annotation tier only, not full experiments. Hoppins body was separately read. No localisation citation is inflated into universal formation proof.

### Substantive reciprocal subcomplex refresh

graph: supported. Targets: GO:0061617.

Newhas_part Mic10 and Mic60–Mic19 links reciprocate the actual child part_of GO:0061617. Friedman independent subcomplexes and Rampelt normal four-protein Mic10 module support the partition; Mic60–Mic19 primary interaction/body supports the other module. Links do not impose universal stoichiometry, identical conditional assembly or physical exclusivity. Historical#2462 is not given a new grouped disposition.

### Whole MICOS architecture and junction maintenance

evidence: supported. Targets: GO:0061617.

Hoppins W303 purifications, localization and mutant microscopy support six-member MICOS/MitOS organization and membrane contacts. Residual junctions in mutant sections/tomograms expressly limit universal formation necessity. Recordmaintenance/organization functions preserve that bound. Harner and vonderMalsburg are complete abstracts only in this review.

### MICOS/MINOS/MitOS aliases and six yeast names

identity: supported. Targets: GO:0061617.

Pfanner 2014 complete nomenclature body/Table 1 supports exact aliases and standardized Mic names, explicitly distinguishes mammalian Mic25 and lineage variations. It is consensus authority, not an independent primary assembly experiment.

### Source-neutral deferred inventory

scope: supported. Targets: GO:0061617.

No individual component rows or proteinexamples does not contradict the correct whole-complex definition, current parthood or declared deferred groundings. Optional expansion is not a confirmed defect. No new blanket family/formation requirement or resolution of the broad inventory task is inferred.

### Three current nonmechanistic function relations

graph: supported. Targets: GO:0061617.

Whole MICOS parthood in inner membrane, junction maintenance and organization relations match currentGO/primary scopes. FUNCTION/NONMECHANISTIC qualification correctly withholds a detailed assembly mechanism and does not claim every junction requires MICOS.

### Exact old Harner access observation

provenance: concern. Targets: GO:0061617.

The original HTTP500/no-body prose is honest, but kindauthority is inappropriate for transport-only evidence. Successor must use validation/context_only without rewriting old timestamps/hashes or claiming current challenge/404 bodies contain science.

### Occurrence, strain and preserved provenance

scope: supported. Targets: cellstructuremech:mic10_subcomplex, cellstructuremech:mic60_mic19_complex, GO:0061617.

COMMON is qualitative occurrence with exceptions, not a measured strain census. W303, YPH499, referenceS288C, C. thermophilum and L. thermotolerans contexts stay separate. Historical discussion rationale remains append-only and open native architecture/grounding questions remain open; later examples do not retroactively invalidate historical provenance.

### Exact MIM identity and anatomical boundary

identity: supported. Targets: GO:0140595.

GO0140595 identifies MIM, distinct from TOM/SAM and the outer membrane itself. Current parent/part_of and import-function scope agree with native authority. No partner or substrate is turned into an intrinsic MIM constituent.

### Constituent family and species-example grounding

grounding: supported. Targets: GO:0140595.

IPR013262 and IPR037652 are actual families for Mim1/Tom13 and Mim2; Q08176 and Q3E798 are reviewed S288C examples. Legacy beta-barrel-biogenesis descriptions are indirect assembly history, not a claim that MIM forms the beta-barrel insertase.

### Import mechanism versus assay dependence

evidence: supported. Targets: GO:0140595.

Selected Doan import experiments support the represented single-spanning substrates and TOM/SAM-associated populations. Vitali steady-state/localization evidence retains substrate variability and indirect-effect limits. The record already distinguishes these assays rather than requiring every helical client to use MIM exclusively.

### Coassembly, stoichiometry and stabilization scope

scope: supported. Targets: GO:0140595.

Added Mim1/Mim2 coassembly is supported. Multiple Mim1/one-or-two Mim2 is a cited background inference, not a fixed directly counted universal stoichiometry. Additional Dimmer Results support a Mim2 contribution to Mim1 abundance/native assembly while overexpressed Mim1 can oligomerize without Mim2. The graph does not assign universal ESSENTIAL formation status; existing architecture uncertainty remains appropriate.

### Three new quoted snippets require verbatim correction

provenance: concern. Targets: GO:0140595.

The two repeated Doan snippets combine the import and composition assertions into wording different from the inspected passage; the Vitali combined sentence is absent from the normalized complete JATS. Composition remains supported. Move paraphrase into notes or recopy exact source wording; do not reverse biological membership.

### Natural host, experimental strain and heterologous rescue

scope: supported. Targets: GO:0140595.

Natural yeast/fungal MIM scope is distinct from S288C sequence examples, YPH499 Doan assays and W303 Vitali experiments. Heterologous Mim1/Mim2 expression in T. brucei and pATOM36 rescue in yeast demonstrate partial functional exchange, not native trypanosome MIM occurrence.

### Current graph actors and changed assembly edges

consistency: supported. Targets: GO:0140595.

Two added component_ref actors are correctly anchored to the represented families/examples. Existing TOM-associated and SAM-associated populations are distinct; dynamic exchange remains proposed rather than directly visualized, and the Tom6 SAM intermediate is supported by native-gel/shift assays. New evidence wording is addressed separately.

### Actual Figure5 pixels, attribution and modality

evidence: supported. Targets: GO:0140595.

All maintained pixels were viewed; source JPEG is byte-identical. Caption and CC BY4.0 permissions support author/source attribution. Mito-GFP/brightfield panels and morphology proportions demonstrate rescue in deletion strains, not localization or molecular structure of MIM.

### Native inventory and original contract

schema: supported. Targets: GO:0140595.

Fresh verify and causal checks pass for two reviewed examples/two COVERED nodes. Original pair validates/renders exactly and historical inputs verify; changed current claims were reassessed. Identity coverage does not establish functional necessity.

### Whole-record structured-source assessment

scope: not_applicable. Targets: GO:0140595.

Original lacks both a formal applicability check and prose assessment. The current protein/import narrative triggers a check; complete current official catalogue has no matched natural fungal host. No foreign-host downstream proxy is used, and catalogue noncoverage is not biological absence.

### Scoped disposition

completeness: concern. Targets: GO:0140595.

Current MIM needs curation only for the new minor verbatim-provenance finding. Optional architecture, stoichiometry and mechanism unknowns are not separate defects. Historical failed-route kinds and stale review inputs require successor correction, not alteration of the original pair.

### Exact MIS12/MIND identity and current hierarchy

identity: supported. Targets: GO:0000444.

The cross-eukaryotic complex identity remains correct. Changed GO0032991 parent and GO0000940/GO0000776 parthood preserve complex-versus-whole-kinetochore boundaries. Prior group hierarchy history does not resolve the separate family or synonym findings.

### Reconfirmed class-grounding finding

grounding: concern. Targets: GO:0000444.

Four exact current family authorities plus member UniProt cross-references support IPR008685/IPR013218/IPR013950/IPR007128 for the already named classes. IPR016851 is narrower. This is a current active grounding gap, not falsification of a dated search or a requirement that every class acquire extra species examples.

### Reconfirmed authority qualifier mismatch

identity: concern. Targets: GO:0000444.

Native GO gives MIND complex EXACT, Mis12 complex NARROW, and the expanded Mtw1p and nuclear phrases RELATED. The maintained four-EXACT representation overstates only these qualifier scopes; primary identity and synonym text remain valid.

### Yeast association and human reconstitution independently verified

evidence: supported. Targets: GO:0000444.

De Wulf supports the yeast four-protein MIND cohort with multiple hydrodynamic states. Kline genuinely coexpressed/purified four human proteins from E. coli and compared endogenous HeLa behavior. The new reconstituted-human-complex note is supported; it is not a yeast reconstitution or a natural bacterial complex.

### Conditional assembly/localization versus universal requirement

scope: supported. Targets: GO:0000444.

Yeast conditional partner stability/CEN association and vertebrate depletion/localization outcomes have distinct experimental scopes. These results do not compel universal all-species ESSENTIAL assignments or a new assay. Existing UNKNOWN formation necessity is retained.

### Bibliography and primary access limits

provenance: supported. Targets: GO:0000444.

Primary bodies substantiate scoped De Wulf/Kline association and recruitment claims. Euskirchen/Pinsky/Scharfenberger were read at complete native abstract tier, sufficient for bounded example descriptions but not an unclaimed Methods or figure inspection.

### Reference accessions and experimental models

scope: supported. Targets: GO:0000444.

All four maintained examples are reviewed budding-yeast S288C entries; natural species taxon4932 is separate. Kline human and chicken assays and recombinant bacterial production are not conflated with De Wulf W303-congenic cultures. The class labels may span orthologues without requiring exhaustive example inventory.

### New component anchors and external recruited actors

consistency: supported. Targets: GO:0000444.

Four new component_ref nodes/edges correctly distinguish intrinsic classes from the Ndc80/Nuf2/Spc24 outer microtubule-binding actor. Gene/UniProt correspondence is valid. Coarse NONMECHANISTIC bridge/recruitment does not assert a universal yeast MIND-to-Ndc80 assembly dependency or make recruited proteins MIND constituents.

### Actual native coverage diagnostics

schema: supported. Targets: GO:0000444.

Four examples verify. Five typed nodes yield 2 COVERED, 2 PARTIAL_EXAMPLES for additional class symbols MIS12/PMF1, and 1 UNANCHORED_WITH_UNIPROT external actor. These accurate diagnostics do not mandate optional extra examples or turn the external actor into a constituent. Original native pair and historical hashes pass.

### Molecular narrative triggers assessment despite absent catalogue host

scope: not_applicable. Targets: GO:0000444.

Original has no formal or prose structured-source applicability assessment. Current protein/recruitment claims require checking; the complete official catalogue has no yeast, human or chicken host dataset. No E. coli expression-host proxy or absent-module biological claim is made.

### Two inherited minor findings remain open

completeness: concern. Targets: GO:0000444.

Both exact original stable keys are reconfirmed with complete repository/review/finding lineage. The stale hierarchy/component-edge additions are substantively supported and do not close either finding. Current historical rationale remains append-only; actions change current fields/notes.

### IMP identity, parents and membrane boundary

identity: supported. Targets: GO:0042720.

GO0042720 exactly denotes the mitochondrial inner membrane peptidase complex, with the represented membrane/serine endopeptidase parents and inner-membrane location. Substrates targeted to the intermembrane space do not relocate the enzyme complex into the lumen.

### Optional inventory and named-subunit scope

completeness: supported. Targets: GO:0042720.

Jan primary abstract describes Imp1/Imp2 and proposed third component Som1. The record does not deny those proteins; it deliberately leaves optional constituent/examples fields unpopulated while tracking curation. No empty-field or compulsory family-enrichment finding is established.

### Som1 association versus complex-formation necessity

scope: supported. Targets: GO:0042720.

Jan abstract supports a physical Som1/Imp1 interaction and proposed component role, not a universal loss-of-whole-complex claim. No formation essentiality is assigned or inferred from processing activity. A qualified pass is appropriate at this evidence tier.

### Processing of nuclear and mitochondrial substrates

evidence: supported. Targets: GO:0042720.

GO definition and primary abstract support membrane-associated cleavage/processing with precursor/substrate differences. The record correctly avoids an after-import-only restriction and preserves nuclear- and mitochondrially encoded substrate scope. Gakh review abstract is secondary context, not a fresh primary mechanistic assay.

### Actual reference tiers and access limits

provenance: supported. Targets: GO:0042720.

Jan is independently read at complete primary abstract tier, current publisher route remains limited. Gakh is a secondary review read at native abstract tier. Original two Jan challenge observations belong to validation/context_only and the DOI-returned Crossref row to database/context_only, preserving original dates/hashes.

### Species-level example without invented strain

scope: supported. Targets: GO:0042720.

The S. cerevisiae example remains species-level. Neither unread Jan Methods nor a secondary abstract justifies inventing a strain or treating S288C as the exact experimental culture. COMMON is retained for species occurrence, not recast as a measured prevalence percentage.

### Coarse descriptive graph matches evidence

consistency: supported. Targets: GO:0042720.

The two NONMECHANISTIC parthood/processing relations stay at supported anatomical and functional resolution. No omitted universal pathway intermediate, component essentiality or mechanistic causal chain is required.

### No maintained image claim

scope: not_applicable. Targets: GO:0042720.

This target has no maintained image; no image evidence or licence is invented. Absence of an optional image is not a finding.

### Empty inventory and immutable original

schema: supported. Targets: GO:0042720.

Fresh native commands exit0 with zero examples/typed nodes. This is an actual empty-inventory result, not proof of molecular completeness. Original pair validates and renders exactly, target bytes remain unchanged, and historical inputs verify.

### Proteolysis narrative requires structured-source assessment

scope: not_applicable. Targets: GO:0042720.

Original omits a formal check and any prose applicability decision. Positive peptidase/processing assertions trigger current catalogue inspection despite zero examples. No matched natural yeast host exists in the complete response; no foreign proxy or biological absence is inferred.

### Qualified pass with bounded access

completeness: supported. Targets: GO:0042720.

No scientific record finding is established. Keep the qualified pass with Jan abstract/Gakh secondary limits; successor repairs the original applicability omission and historical evidence kinds without rewriting original artefacts or claiming a full primary-body inspection.

### Original envelope, frozen inputs and current native inventory

schema: supported. Targets: cellstructuremech:mitochondrial_lon_protease_complex.

Original native validation and Markdown reproduction pass, with unchanged target bytes. Current native inventory is 1 protein examples and one COVERED typed node. Reference validation is distinct from source-specific scientific membership or causal necessity.

### Required structured-source applicability

evidence: supported. Targets: cellstructuremech:mitochondrial_lon_protease_complex.

Positive protease, import, protein-complex, metabolic or mitochondrial-organization claims trigger assessment. The original formal expression-only N/A rationale is unsupported. Current full catalogue has no matching biological host; disclose this bounded coverage limit, retain actual historical runner failure and use inspected primary/native authorities. No downstream unmatched E. coli proxy or expression-to-assembly inference.

### Citation, historical rationale and exact input provenance

provenance: supported. Targets: cellstructuremech:mitochondrial_lon_protease_complex.

Original YAML/Markdown and dated discussions remain immutable. Original same-base global checks identify their actual historical batch26 execution; this is not an erroneous current cohort label. No record edits or terminal resolution of neighboring/group issues. Current records contain no verbatim snippets to certify.

### Historical source access classification

evidence: supported. Targets: cellstructuremech:mitochondrial_lon_protease_complex.

All original evidence rows read. The original failed XML/empty PANTHER diagnostics named in the grouped bundle defect must use validation, with context_only and explicit failure retained; no original body-claim fabrication is alleged.

### Original envelope, frozen inputs and current native inventory

schema: supported. Targets: cellstructuremech:mitochondrial_multifunctional_assembly.

Original native validation and Markdown reproduction pass, with unchanged target bytes. Current native inventory is 5 protein examples and one COVERED typed node. Reference validation is distinct from source-specific scientific membership or causal necessity.

### Required structured-source applicability

evidence: supported. Targets: cellstructuremech:mitochondrial_multifunctional_assembly.

Positive protease, import, protein-complex, metabolic or mitochondrial-organization claims trigger assessment. The original formal expression-only N/A rationale is unsupported. Current full catalogue has no matching biological host; disclose this bounded coverage limit, retain actual historical runner failure and use inspected primary/native authorities. No downstream unmatched E. coli proxy or expression-to-assembly inference.

### Citation, historical rationale and exact input provenance

provenance: supported. Targets: cellstructuremech:mitochondrial_multifunctional_assembly.

Original YAML/Markdown and dated discussions remain immutable. Original same-base global checks identify their actual historical batch26 execution; this is not an erroneous current cohort label. No record edits or terminal resolution of neighboring/group issues. Current records contain no verbatim snippets to certify.

### Historical source access classification

evidence: supported. Targets: cellstructuremech:mitochondrial_multifunctional_assembly.

All original evidence rows read. The original failed XML/empty PANTHER diagnostics named in the grouped bundle defect must use validation, with context_only and explicit failure retained; no original body-claim fabrication is alleged.

### Original envelope, frozen inputs and current native inventory

schema: supported. Targets: GO:0005742.

Original native validation and Markdown reproduction pass, with unchanged target bytes. Current native inventory is 0 protein examples and zero typed nodes; empty coverage is not evidence of complete molecular representation. Reference validation is distinct from source-specific scientific membership or causal necessity.

### Required structured-source applicability

evidence: supported. Targets: GO:0005742.

Positive protease, import, protein-complex, metabolic or mitochondrial-organization claims trigger assessment. The original formal expression-only N/A rationale is unsupported. Current full catalogue has no matching biological host; disclose this bounded coverage limit, retain actual historical runner failure and use inspected primary/native authorities. No downstream unmatched E. coli proxy or expression-to-assembly inference.

### Citation, historical rationale and exact input provenance

provenance: supported. Targets: GO:0005742.

Original YAML/Markdown and dated discussions remain immutable. Original same-base global checks identify their actual historical batch26 execution; this is not an erroneous current cohort label. No record edits or terminal resolution of neighboring/group issues. Current records contain no verbatim snippets to certify.

### Historical source access classification

evidence: supported. Targets: GO:0005742.

All original evidence rows read. No additional access-kind defect established in this original; the scientific synonym finding remains separate.

### Original envelope, frozen inputs and current native inventory

schema: supported. Targets: GO:0035632.

Original native validation and Markdown reproduction pass, with unchanged target bytes. Current native inventory is 0 protein examples and zero typed nodes; empty coverage is not evidence of complete molecular representation. Reference validation is distinct from source-specific scientific membership or causal necessity.

### Required structured-source applicability

evidence: supported. Targets: GO:0035632.

Positive protease, import, protein-complex, metabolic or mitochondrial-organization claims trigger assessment. The original formal expression-only N/A rationale is unsupported. Current full catalogue has no matching biological host; disclose this bounded coverage limit, retain actual historical runner failure and use inspected primary/native authorities. No downstream unmatched E. coli proxy or expression-to-assembly inference.

### Citation, historical rationale and exact input provenance

provenance: supported. Targets: GO:0035632.

Original YAML/Markdown and dated discussions remain immutable. Original same-base global checks identify their actual historical batch26 execution; this is not an erroneous current cohort label. No record edits or terminal resolution of neighboring/group issues. Current records contain no verbatim snippets to certify.

### Historical source access classification

evidence: supported. Targets: GO:0035632.

All original evidence rows read. The original failed XML/empty PANTHER diagnostics named in the grouped bundle defect must use validation, with context_only and explicit failure retained; no original body-claim fabrication is alleged.

### Mitochondrial oligomer versus protein and broader family

identity: supported. Targets: cellstructuremech:mitochondrial_lon_protease_complex.

Local identity denotes a mitochondrial peptidase assembly, not an isolated Lon protein or all chloroplastic members of IPR027503. GO1905368 parent and matrix location are appropriate. Bounded GO searches did not establish an exact alternative; broad search first pages are not exhaustive.

### Pim1 identity and reference-strain membership

grounding: supported. Targets: cellstructuremech:mitochondrial_lon_protease_complex.

Reviewed P36775 is primary PIM1 with LON alias in S288C; both current bounded queries return this entry. IPR027503 is broader chloroplastic/mitochondrial family, explicitly scoped to mitochondrial yeast instance. Native localization and primary structural membership are separately verified. No gene-name or strain substitution.

### Conflicting purified preparations and archive chain accounting

quantity: supported. Targets: cellstructuremech:mitochondrial_lon_protease_complex.

1999 mitochondrial-extract C-terminally tagged preparation gives seven subunits; 2022 bacterially expressed mature substrate-bound preparation gives six. Current record preserves conflict and no universal count. PDB A6B1 contains six Pim1 chains and one substrate, not seven enzyme chains. Archive3.3A versus paper approximately3.21A and 4ATP/2ADP are properly distinguished.

### Paper accession conflict independently checked

evidence: supported. Targets: cellstructuremech:mitochondrial_lon_protease_complex.

Paper Data availability names EMD25505/7XSO, but fresh archive content names unrelated spike/Craspase structures. Native EMD25502/7SXO citation and Pim1 entity mapping corroborate the record correction; no source conflict is concealed.

### Formation versus enzymatic activity

completeness: supported. Targets: cellstructuremech:mitochondrial_lon_protease_complex.

Pim1 is the defining enzyme constituent, yet the source does not make its substrate-bound static state a complete assembly pathway. S1015A assays concern proteolytic function; INSdel/GSlink retained activity is bounded to the beta-casein assay, not all substrates/adaptor binding/native viability. Existing UNKNOWN necessity and restrained formation claims remain appropriate.

### Function graph and mechanistic interpretation

graph: supported. Targets: cellstructuremech:mitochondrial_lon_protease_complex.

The graph separates structural membership, assay proteolysis, catalytic loss and insertion perturbations. Hand-over-hand translocation is a structure-supported model, not a directly time-resolved trajectory. C-terminal release/adaptor hypotheses remain unresolved. No unwarranted assembly-loss or universal native-essentiality inference.

### Actual pixels, attribution and license

representation: supported. Targets: cellstructuremech:mitochondrial_lon_protease_complex.

Maintained Figure1 pixels were inspected and matched fresh source media exactly; model and pore-loop panels support the bounded caption, not an in situ micrograph. JATS CC BY4.0 and article authors support licensing/attribution. Figure3 pixels were separately read only for the displayed assay, not as quantitative kinetics.

### Current independent verdict

scope: supported. Targets: cellstructuremech:mitochondrial_lon_protease_complex.

pass_with_limitations: supported structure and source-specific function/quantity boundaries; no scientific curation finding. Preparation differences, archive conflict, static-mechanism inference and source-specific assays remain explicit.

### Distinct MIMAS protein-lipid assembly

identity: supported. Targets: cellstructuremech:mitochondrial_multifunctional_assembly.

Horten2024 establishes an isolatable inner-membrane mega-assembly with selected carriers, respiratory biogenesis factors, dehydrogenases and lipid enzymes. It is distinct from respirasome, ATP synthase, prohibitin and MICOS. Local identifier and parent/part_of distinction are supported; bounded GO searches are not a global absence claim.

### Five scoped representative components

grounding: supported. Targets: cellstructuremech:mitochondrial_multifunctional_assembly.

AAC2/PET9 P18239, RCF1 Q03713, PSD1 P39006, NDE1 P40215 and TAZ1 Q06510 are reviewed S288C reference identities, not claimed study strains. Horten affinity, migration and crosslinking support selected MIMAS pools. Native family labels support AAC/RCF1/PSD1/tafazzin; broad NDH2 family does not justify an external-Nde1-specific grounding, so label-only status is appropriate.

### Study strains versus examples and localization sources

scope: supported. Targets: cellstructuremech:mitochondrial_multifunctional_assembly.

Horten Methods uses YPH499/W303 derivatives and a Neurospora AAC construct in import methods; S288C examples are reference identity only. Native PET9 also has peroxisomal localization and Taz1 both membranes; those do not negate the experimentally isolated mitochondrial MIMAS fraction. Huh/Sickmann and other cited localization sources were checked at complete abstract/native-annotation tier, not uninspected body tier.

### Psd1 catalysis, PE and MIMAS integrity

completeness: supported. Targets: cellstructuremech:mitochondrial_multifunctional_assembly.

Psd1-S463A can join wild-type MIMAS but fails to rescue the psd1-null assembly while active Psd1 does. This supports enzyme-product-dependent integrity, not a direct PE binding site, universal lipid concentration or complete formation order. Current UNKNOWN component essentiality is not contradicted by the scoped perturbation evidence.

### Bounded PE-dependent causal graph

graph: supported. Targets: cellstructuremech:mitochondrial_multifunctional_assembly.

Psd1 activity produces PE and supports MIMAS integrity under the tested yeast preparation; no added mechanistic edges are inferred simply from co-migration. Protein abundance control, crd1 comparison and mutant rescue distinguish stability from trivial protein loss and lipid-general assertions.

### Rcf1 and Cox13 functional limits

evidence: supported. Targets: cellstructuremech:mitochondrial_multifunctional_assembly.

Rcf1 R67A loses MIMAS association whereas Q61/71A increases it in rcf1/rcf2 background. Cox13 import/chase supports transient association, not a mature stoichiometric constituent or direct handoff demonstrated in real time. Authors explicitly state import is not a quantitative occupancy measure and exact composition/stoichiometry remains future work.

### Apparent size and dataset provenance

quantity: supported. Targets: cellstructuremech:mitochondrial_multifunctional_assembly.

MIMAS-A/B approximately3.3/2.5MDa migration peaks are apparent assemblies, not exact protein counts. PRIDE PARTIAL dataset and placeholder PMID0 are properly distinguished from the correct paper DOI. No raw MS reanalysis or quantitative occupancy is claimed.

### Primary versus secondary and image limits

evidence: supported. Targets: cellstructuremech:mitochondrial_multifunctional_assembly.

Horten2024 body is primary; 2026 MIMAS review is secondary. IPR050355 generated unchecked prose is excluded as mechanistic support. Current manuscript captions were read but MIMAS figure pixels were not viewed in this review; no inherited reviewer pixel claim is borrowed. CC BY-NC-ND4.0 does not support an unqualified reusable local illustration; none is maintained.

### Current independent verdict

scope: supported. Targets: cellstructuremech:mitochondrial_multifunctional_assembly.

pass_with_limitations: coherent stable protein-lipid assembly at the source-defined fraction/strain scope. Exact stoichiometry, direct handoff, substrate-streamlining and broad component necessity remain unsettled; no confirmed scientific finding.

### Whole TOM identity and narrower GIP core

identity: concern. Targets: GO:0005742.

GO0005742 whole TOM identity, outer-membrane location and parent remain supported. The current GIP EXACT_SYNONYM still disagrees with fresh native GO narrow designation; retain original F1 and stable key tom-gip-synonym-scope.

### Reference identities and family boundaries without forced inventory

grounding: supported. Targets: GO:0005742.

Current native S288C Tom40/22/20/70/5/6/7 identities and candidate family boundaries were inspected. Broad/fungal family choices require scoped later curation, but missing optional component/examples is not itself a scientific defect. Empty native inventory does not certify complete composition.

### Import gate and downstream pathway distinction

scope: supported. Targets: GO:0005742.

Chacinska2009 is a genuine secondary review body. TOM mediates outer-membrane entry toward all mitochondrial compartments; complete GO0030150 matrix import additionally requires TIM23/PAM. The current record explicitly limits its graph to topology and entry role and does not assert TOM alone crosses both membranes.

### Assembly evidence versus universal requirement

completeness: supported. Targets: GO:0005742.

Secondary review describes Tom22 organization and small-Tom subunit effects, but these are not new primary experimental checks or a universal organism-wide formation necessity claim. Empty optional composition and explicit unresolved family grounding do not warrant manufactured findings.

### Nonmechanistic anatomy and functional graph

graph: supported. Targets: GO:0005742.

Current NONMECHANISTIC graph captures whole-complex outer-membrane topology and contribution to import. No individual family or detailed TIM23/PAM mechanism is falsely added. GIP synonym correction preserves all supported graph meaning.

### Qualitative occurrence and source scope

scope: supported. Targets: GO:0005742.

S.cerevisiae evidence supports the canonical mitochondrial setting; Eukaryota VARIABLE avoids universal retention in reduced organelles. COMMON is qualitative record context rather than an experimentally measured prevalence census.

### Current independent verdict

scope: concern. Targets: GO:0005742.

needs_curation solely for inherited minor GIP synonym scope. Supported whole TOM identity, location, import function and current restrained inventory remain intact; original source lineage and bounded action preserved.

### Prohibitin repeating heterodimeric complex

identity: supported. Targets: GO:0035632.

Native GO0035632 and Back2002 primary abstract support PHB1/PHB2 repeating heterodimeric building blocks in an inner-membrane assembly. No exact universal subunit number or atomic experimental structure is asserted in the record.

### Prohibitin reference identities and broad family

grounding: supported. Targets: GO:0035632.

Fresh native queries identify reviewed S288C PHB1 P40961 and PHB2 P50085. IPR000163 is shared prohibitin family, not a verified exact split for each paralogue. No empty optional-component or forced-chemical/complex-grounding finding is justified.

### Current primary abstract and genuine secondary body

evidence: supported. Targets: GO:0035632.

Back2002 complete primary abstract supports crosslink/MS spatial restraints and modeled repeating heterodimer building block. Current canonical routes are challenge markup, EPXML500, publisher403 and S3version1 not available; no primary full-body Methods or image inspection is claimed. Artal2010 genuine review body is secondary. Historical successful original access is retained as historical, not represented as fresh.

### Organization and condition-sensitive biological function

scope: supported. Targets: GO:0035632.

GO0007005 mitochondrial biogenesis exact synonym and the current organization wording are coherent. Secondary review separates yeast growth/aging from animal development and context-sensitive lifespan effects; the record does not make a universal viability or direction-of-aging claim.

### Source-limited assembly and necessity

completeness: supported. Targets: GO:0035632.

Physical PHB1-PHB2 interactions and repeating building block are supported at primary-abstract tier. Detailed perturbation claims described in the review are not reclassified as independently inspected primary assays. The record remains cautious and no optional family inventory or universal essentiality requirement is imposed.

### Nonmechanistic topology and organization

graph: supported. Targets: GO:0035632.

The graph restricts itself to complex identity, inner-membrane parthood and broad mitochondrial organization. It does not imply exact PHB1/PHB2 family groundings, atomistic assembly pathway or fixed stoichiometry.

### Current independent verdict

scope: supported. Targets: GO:0035632.

pass_with_limitations: core identity/topology and broad function are supported; primary full-body/Methods/pixel access is unavailable now and explicitly limited. No scientific finding is established by that access limitation alone.

### Complete frozen-input comparison and bounded refresh

provenance: supported. Targets: cellstructuremech:mic10_subcomplex, cellstructuremech:mic60_mic19_complex, GO:0061617, GO:0140595, GO:0000444, GO:0042720, cellstructuremech:mitochondrial_lon_protease_complex, cellstructuremech:mitochondrial_multifunctional_assembly, GO:0005742, GO:0035632.

3 of ten original target hashes differ from current main. The changed content is substantively reassessed in the target-specific assessments; original observations remain historical and unchanged. All current target and used context bytes are frozen.

## Findings

### plaque-t3-F1: Make the new MIM assembly snippets verbatim or move paraphrases to notes

minor / open / confirmed; issue key: mim-complex-assembly-snippets-nonverbatim.

The two new assembly edges contain three snippet occurrences: a repeated combined Doan import/composition sentence and a combined Vitali sentence. Their wording differs from the inspected source passages; the Vitali sentence is absent from the complete normalized genuine JATS. Doan access is the retained indexed official PDF representation, not a fresh complete terminal PDF. These are supported scientific paraphrases presented as quotations. Correct quotation form without rejecting multiple Mim1/one-or-two Mim2 background composition or imposing universal formation necessity.

### plaque-t4-F1: Ground the four represented MIS12/MIND subunit classes

minor / open / confirmed; issue key: mis12-mind-exact-family-groundings.

Four existing protein classes remain REVIEWED_LABEL_ONLY. Native whole-family definitions and independent member identities now support IPR008685, IPR013218, IPR013950 and IPR007128 respectively. This is an actionable class-grounding gap, not a claim that the dated earlier search was false.

Disposition: Reconfirmed against current unchanged affected fields and fresh native authority/member evidence; new hierarchy and component edges do not remedy this separate finding.

### plaque-t4-F2: Preserve the GO synonym scopes

minor / open / confirmed; issue key: mis12-mind-synonym-qualifiers.

The record attributes four EXACT synonyms to GO0000444, but the current native term classifies Mis12 complex as narrow and the expanded Mtw1p and nuclear MIS12/MIND phrases as related. Only MIND complex is exact. The labels themselves are not rejected; their source-specific qualifiers are overstated.

Disposition: Reconfirmed against current unchanged affected fields and fresh native authority/member evidence; new hierarchy and component edges do not remedy this separate finding.

### septin-tom-F1: Retain GIP as a narrower synonym

minor / open / confirmed; issue key: tom-gip-synonym-scope.

The current synonym row types GIP complex as EXACT_SYNONYM and attributes it to GO0005742. The native GO response marks GIP as narrow. The Tom22 authority independently distinguishes docking Tom20/Tom70 onto the general Tom40 import-pore complex, supporting the narrower-core boundary while preserving whole TOM identity.

## Recommended Actions And Acceptance Checks

### plaque-t3-A1

For all three added snippet occurrences, either copy a short exact passage from the inspected cited source or move the supported paraphrase to notes and omit snippet. Retain source-qualified composition, coassembly and uncertainty; preserve existing dated history.

- Every retained snippet exactly matches a cited inspected passage, including wording; paraphrase appears only in notes.
- Doan background copy range is not misrepresented as a direct universal stoichiometry measurement; stabilization/coassembly does not imply absolute Mim2 necessity.
- Primary body/indexed-text access tiers and experimental limits remain explicit; native schema and focused evidence checks pass after separately authorized curation.

### plaque-t4-A1

Add the four exact family groundings and update current grounding status/notes and the open task. Retain the verified species examples and UNKNOWN essentiality; use IPR007128 for the joint Nnf1/PMF1 class. Do not propagate the malformed InterPro organism phrase.

- The amended field matches the exact native authority scope and preserves independently supported scientific identity.
- Original historical statements are retained as history; current grounding or source qualifiers are updated explicitly.
- Native schema, strict and CURIE checks pass after separately authorized curation.

### plaque-t4-A2

Retain the synonym text and GO source but use NARROW_SYNONYM for Mis12 complex and RELATED_SYNONYM for the two related phrases; retain EXACT_SYNONYM for MIND complex.

- The amended field matches the exact native authority scope and preserves independently supported scientific identity.
- Original historical statements are retained as history; current grounding or source qualifiers are updated explicitly.
- Native schema, strict and CURIE checks pass after separately authorized curation.

### septin-tom-A1

Change only the GIP synonym scope to NARROW_SYNONYM or supply an explicitly scoped alternative supported by a direct source. Preserve the exact whole TOM identifier and the other exact synonym.

- Recheck the native GO synonym type and retain the pore-core versus whole-complex distinction.
- Pass schema, strict and applicable identifier checks after separately authorized curation.
- Preserve immutable original bundles and dated historical rationale; change only separately authorized current synonym scope or append a source-supported clarification.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| current-record-0 | data/structures/other/mic10_subcomplex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 9d98461e5b91bf4eb28fffe1797678d45d3f6aa51391b289282b7b6155a22601; current SHA256 9d98461e5b91bf4eb28fffe1797678d45d3f6aa51391b289282b7b6155a22601. Record bytes unchanged since the original review. |
| original-review-0 | reviews/structured/20261022T084805Z-mic10-subcomplex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-1 | data/structures/other/mic60_mic19_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 f69ade5a57e4946d6bb529c33ab623059348fd9a4c43609cea0b33b50d591cb7; current SHA256 f69ade5a57e4946d6bb529c33ab623059348fd9a4c43609cea0b33b50d591cb7. Record bytes unchanged since the original review. |
| original-review-1 | reviews/structured/20261022T084806Z-mic60-mic19-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-2 | data/structures/other/micos_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 95c3aa4af71bf436a4c5dbbd527d47ff46c73d484843425fdd9c44615782375f; current SHA256 756a5b48fd9109266e6ace5805f5f9fd4aaac9940ff39660960bb8603374f5aa. Changed record reassessed against current sources. |
| original-review-2 | reviews/structured/20261022T084806Z-micos-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-3 | data/structures/other/mim_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 dc0d4007dfe5d82f22b45d46cc12e3c934ce3ebe92d7ed7b48c25be1ea715c5f; current SHA256 61bfb31d9aca0a2be252843e729f32e2b8ff9f3d02c77ba43e06d6f5a9229916. Changed record reassessed against current sources. |
| original-review-3 | reviews/structured/20261022T084807Z-mim-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-4 | data/structures/other/mis12_mind_type_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 6b16e919810eceb24433ded999d28a548adbb8c5e0d55af4eb63fe3e4eaac1a6; current SHA256 029ac75e12045a39ff6da937c63cff087715e76aadf1b65ad773f30bdfc4e944. Changed record reassessed against current sources. |
| original-review-4 | reviews/structured/20261022T084808Z-mis12-mind-type-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-5 | data/structures/other/mitochondrial_inner_membrane_peptidase_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 8eb6f174c969fc2aef5a84a2a473fe42a66158531ae26422ccfd8ae3407227e0; current SHA256 8eb6f174c969fc2aef5a84a2a473fe42a66158531ae26422ccfd8ae3407227e0. Record bytes unchanged since the original review. |
| original-review-5 | reviews/structured/20261022T084808Z-mitochondrial-inner-membrane-peptidase-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-6 | data/structures/other/mitochondrial_lon_protease_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 22c985cbd94a32e0a04e1ba4b7f77e796ef99815390b9165a3b15b987429d5d6; current SHA256 22c985cbd94a32e0a04e1ba4b7f77e796ef99815390b9165a3b15b987429d5d6. Record bytes unchanged since the original review. |
| original-review-6 | reviews/structured/20261022T084809Z-mitochondrial-lon-protease-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-7 | data/structures/other/mitochondrial_multifunctional_assembly.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 bb1a36eee48a44140250e04951a42f149f5de60affd5e146ba8f89f8a6e48858; current SHA256 bb1a36eee48a44140250e04951a42f149f5de60affd5e146ba8f89f8a6e48858. Record bytes unchanged since the original review. |
| original-review-7 | reviews/structured/20261022T084810Z-mitochondrial-multifunctional-assembly-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-8 | data/structures/other/mitochondrial_outer_membrane_translocase_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 a9facce19eda1794aefb3bef7b36fe07ba5c3a942220a4379c5569de4150022e; current SHA256 a9facce19eda1794aefb3bef7b36fe07ba5c3a942220a4379c5569de4150022e. Record bytes unchanged since the original review. |
| original-review-8 | reviews/structured/20261022T084810Z-mitochondrial-outer-membrane-translocase-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-9 | data/structures/other/mitochondrial_prohibitin_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 a2a0c89fc814c0dba32ef8a1b90246ced003e274382c67d78794cbd86e9b7453; current SHA256 a2a0c89fc814c0dba32ef8a1b90246ced003e274382c67d78794cbd86e9b7453. Record bytes unchanged since the original review. |
| original-review-9 | reviews/structured/20261022T084811Z-mitochondrial-prohibitin-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| micro-record-0 | data/structures/other/mic10_subcomplex.yaml; Complete current maintained record at source HEAD | context_only | All identity, taxa, components/examples, function/evidence, every graph edge, discussions/history and images where present were read. Current bytes match reviewed main. Target is nonstale against its original frozen input. |
| micro-prior-0 | reviews/structured/20261022T084805Z-mic10-subcomplex-audit/review.yaml; Complete immutable original YAML and derived Markdown; findings/actions/checks/evidence scopes | context_only | Original qualified pass has no scientific findings or actions. Original source access, all formal checks and limitations reassessed; fresh retrieval does not retrospectively upgrade historical observations. |
| micro-record-1 | data/structures/other/mic60_mic19_complex.yaml; Complete current maintained record at source HEAD | context_only | All identity, taxa, components/examples, function/evidence, every graph edge, discussions/history and images where present were read. Current bytes match reviewed main. Target is nonstale against its original frozen input. |
| micro-prior-1 | reviews/structured/20261022T084806Z-mic60-mic19-complex-audit/review.yaml; Complete immutable original YAML and derived Markdown; findings/actions/checks/evidence scopes | context_only | Original qualified pass has no scientific findings or actions. Original source access, all formal checks and limitations reassessed; fresh retrieval does not retrospectively upgrade historical observations. |
| micro-record-2 | data/structures/other/micos_complex.yaml; Complete current maintained record at source HEAD | context_only | All identity, taxa, components/examples, function/evidence, every graph edge, discussions/history and images where present were read. Current bytes match reviewed main. MICOS changed only by reciprocal has_part links and appended history. |
| micro-prior-2 | reviews/structured/20261022T084806Z-micos-complex-audit/review.yaml; Complete immutable original YAML and derived Markdown; findings/actions/checks/evidence scopes | context_only | Original qualified pass has no scientific findings or actions. Original source access, all formal checks and limitations reassessed; fresh retrieval does not retrospectively upgrade historical observations. |
| micro-policy | docs/CURATION.md; Components, evidence and append-only discussion rules | context_only | Exact family/class scope, supported positive claims and preserved historical rationale; optional missing examples or component rows are not automatic defects. |
| micro-schema | src/cellstructuremech/schema/cellstructuremech.yaml; Evidence, component type/essentiality, graph relations and image definitions | context_only | Formation is distinct from activity and viability; families/complex nodes may be represented. snippet is verbatim-only, notes is paraphrase. No universal knockout requirement follows. |
| micro-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Native graph review contract | context_only | Check actual actor/edge/grounding and explicitly bounded mechanism/function scope without demanding unasserted mechanisms. |
| micro-native-policy | .claude/skills/review-yaml-record/SKILL.md; Complete native read-only workflow and structured-source applicability | context_only | Positive molecular and pathway claims trigger bounded source assessment regardless of whether an expression-module claim is asserted. |
| micro-native-config | conf/record_review.yaml; Native configured review requirements | context_only | Root owns whole-corpus gates and successor publication; this scratch review does not certify future gates. |
| micro-original-audit | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/original-audit.json; Six actual native validate/render commands and 44 historical input occurrences | supports | All six commands exited zero and each rendered Markdown equals the immutable original. Six original artifact bytes match the original PR commit; declared historical input hashes match exact source revisions. Current targets match source and main, with exactly one stale assigned target. |
| micro-micos-stale-delta | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/micos_complex-historical-current.diff; Actual original declared source to current source Git diff | supports | Only appended 2026-10-30 parthood history and has_part links to the two assigned subcomplex records changed. No component, function, graph or experimental source assertion changed. |
| micro-protein-P38341-retry | https://rest.uniprot.org/uniprotkb/P38341?format=json; Native accession/status, complete gene tokens/taxon/name; FUNCTION, SUBUNIT, SUBCELLULAR LOCATION and SIMILARITY comments; relevant InterPro/Pfam/SGD references; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/protein-P38341-retry.raw | supports | P38341: reviewed MICOS complex subunit MIC12; taxon 559292; genes [{'geneName': {'value': 'MIC12'}, 'synonyms': [{'value': 'AIM5'}, {'value': 'FMP51'}, {'value': 'MCS12'}], 'orderedLocusNames': [{'value': 'YBR262C'}], 'orfNames': [{'value': 'YBR1731'}]}]. Native identity/location annotations remain distinct from directly inspected primary formation or experiment-strain evidence. |
| micro-protein-P50087-retry | https://rest.uniprot.org/uniprotkb/P50087?format=json; Native accession/status, complete gene tokens/taxon/name; FUNCTION, SUBUNIT, SUBCELLULAR LOCATION and SIMILARITY comments; relevant InterPro/Pfam/SGD references; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/protein-P50087-retry.raw | supports | P50087: reviewed MICOS subunit MIC26; taxon 559292; genes [{'geneName': {'value': 'MIC26'}, 'synonyms': [{'value': 'MCS29'}, {'value': 'MIO27'}, {'value': 'MOS2'}], 'orderedLocusNames': [{'value': 'YGR235C'}], 'orfNames': [{'value': 'G8575'}]}]. Native identity/location annotations remain distinct from directly inspected primary formation or experiment-strain evidence. |
| micro-protein-P50945-retry | https://rest.uniprot.org/uniprotkb/P50945?format=json; Native accession/status, complete gene tokens/taxon/name; FUNCTION, SUBUNIT, SUBCELLULAR LOCATION and SIMILARITY comments; relevant InterPro/Pfam/SGD references; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/protein-P50945-retry.raw | supports | P50945: reviewed MICOS complex subunit MIC27; taxon 559292; genes [{'geneName': {'value': 'MIC27'}, 'synonyms': [{'value': 'AIM37'}, {'value': 'MCS27'}], 'orderedLocusNames': [{'value': 'YNL100W'}], 'orfNames': [{'value': 'N2190'}]}]. Native identity/location annotations remain distinct from directly inspected primary formation or experiment-strain evidence. |
| micro-protein-P36112-retry | https://rest.uniprot.org/uniprotkb/P36112?format=json; Native accession/status, complete gene tokens/taxon/name; FUNCTION, SUBUNIT, SUBCELLULAR LOCATION and SIMILARITY comments; relevant InterPro/Pfam/SGD references; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/protein-P36112-retry.raw | supports | P36112: reviewed MICOS complex subunit MIC60; taxon 559292; genes [{'geneName': {'value': 'MIC60'}, 'synonyms': [{'value': 'AIM28'}, {'value': 'FCJ1'}, {'value': 'FMP13'}], 'orderedLocusNames': [{'value': 'YKR016W'}]}]. Native identity/location annotations remain distinct from directly inspected primary formation or experiment-strain evidence. |
| micro-protein-P43594-retry | https://rest.uniprot.org/uniprotkb/P43594?format=json; Native accession/status, complete gene tokens/taxon/name; FUNCTION, SUBUNIT, SUBCELLULAR LOCATION and SIMILARITY comments; relevant InterPro/Pfam/SGD references; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/protein-P43594-retry.raw | supports | P43594: reviewed MICOS complex subunit MIC19; taxon 559292; genes [{'geneName': {'value': 'MIC19'}, 'synonyms': [{'value': 'AIM13'}, {'value': 'MCS19'}], 'orderedLocusNames': [{'value': 'YFR011C'}]}]. Native identity/location annotations remain distinct from directly inspected primary formation or experiment-strain evidence. |
| micro-protein-Q96VH5-final | https://rest.uniprot.org/uniprotkb/Q96VH5.txt; Complete current UniProt flat file, including identity/gene/taxon, bibliography, FUNCTION/SUBUNIT/LOCATION/SIMILARITY and family references; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/protein-Q96VH5-final.raw | supports | Q96VH5 is reviewed MIC10, aliases MCS10/MIO10/MOS1, locus YCL057C-A, S288c559292; IPR007512. Native annotation is not an independent new primary experiment. |
| micro-query-MIC10-retry | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AMIC10%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100&amp;fields=accession%2Cid%2Cprotein_name%2Cgene_names%2Corganism_id%2Creviewed; Complete exact gene/taxon/reviewed response and total-results/Link headers; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/query-MIC10-retry.raw | supports | One current reviewed accession Q96VH5, matching primary gene MIC10 and taxon 559292. No next page. Current uniqueness does not reconstruct the dated October selection. |
| micro-query-MIC12-retry | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AMIC12%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100&amp;fields=accession%2Cid%2Cprotein_name%2Cgene_names%2Corganism_id%2Creviewed; Complete exact gene/taxon/reviewed response and total-results/Link headers; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/query-MIC12-retry.raw | supports | One current reviewed accession P38341, matching primary gene MIC12 and taxon 559292. No next page. Current uniqueness does not reconstruct the dated October selection. |
| micro-query-MIC26-final | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AMIC26+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=100&amp;fields=accession%2Cid%2Cprotein_name%2Cgene_names%2Corganism_id%2Creviewed; Complete exact gene/taxon/reviewed response and total-results/Link headers; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/query-MIC26-final.raw | supports | One current reviewed accession P50087, matching primary gene MIC26 and taxon 559292. No next page. Current uniqueness does not reconstruct the dated October selection. |
| micro-query-MIC27-retry | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AMIC27%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100&amp;fields=accession%2Cid%2Cprotein_name%2Cgene_names%2Corganism_id%2Creviewed; Complete exact gene/taxon/reviewed response and total-results/Link headers; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/query-MIC27-retry.raw | supports | One current reviewed accession P50945, matching primary gene MIC27 and taxon 559292. No next page. Current uniqueness does not reconstruct the dated October selection. |
| micro-query-MIC60-final | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AMIC60+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=100&amp;fields=accession%2Cid%2Cprotein_name%2Cgene_names%2Corganism_id%2Creviewed; Complete exact gene/taxon/reviewed response and total-results/Link headers; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/query-MIC60-final.raw | supports | One current reviewed accession P36112, matching primary gene MIC60 and taxon 559292. No next page. Current uniqueness does not reconstruct the dated October selection. |
| micro-query-MIC19-retry | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AMIC19%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100&amp;fields=accession%2Cid%2Cprotein_name%2Cgene_names%2Corganism_id%2Creviewed; Complete exact gene/taxon/reviewed response and total-results/Link headers; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/query-MIC19-retry.raw | supports | One current reviewed accession P43594, matching primary gene MIC19 and taxon 559292. No next page. Current uniqueness does not reconstruct the dated October selection. |
| micro-ipr-IPR007512 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007512/; Native name/type, complete description, relevant hierarchy and member signatures; description quality flags; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/ipr-IPR007512.raw | supports | IPR007512: MICOS complex subunit Mic10, type family. Exact Mic10 family. No sequence alignment or exhaustive alternate-family search performed. |
| micro-ipr-IPR031463 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR031463/; Native name/type, complete description, relevant hierarchy and member signatures; description quality flags; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/ipr-IPR031463.raw | supports | IPR031463: MICOS complex subunit Mic12, type family. Exact Mic12 family, with historical conditional three-protein subcomplex description. No sequence alignment or exhaustive alternate-family search performed. |
| micro-ipr-IPR033181 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR033181/; Native name/type, complete description, relevant hierarchy and member signatures; description quality flags; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/ipr-IPR033181.raw | supports | IPR033181: MICOS subunit Mic26, fungi, type family. Explicit fungal Mic26 branch, not a universal Mic26/Mic27 identity. No sequence alignment or exhaustive alternate-family search performed. |
| micro-ipr-IPR061953 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR061953/; Native name/type, complete description, relevant hierarchy and member signatures; description quality flags; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/ipr-IPR061953.raw | supports | IPR061953: MICOS complex subunit MIC27, type family. Explicit Saccharomycetaceae Mic27 family. No sequence alignment or exhaustive alternate-family search performed. |
| micro-ipr-IPR019133-retry | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR019133/?format=json; Native name/type, complete description, relevant hierarchy and member signatures; description quality flags; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/ipr-IPR019133-retry.raw | supports | IPR019133: MICOS complex subunit MIC60, type family. Exact Mic60 family; description domain coordinates are not automatically transferred between taxa. No sequence alignment or exhaustive alternate-family search performed. |
| micro-ipr-IPR012471-retry | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR012471/?format=json; Native name/type, complete description, relevant hierarchy and member signatures; description quality flags; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/ipr-IPR012471-retry.raw | supports | IPR012471: Protein of unknown function DUF1690, type family. Family of uncharacterised fungal proteins (DUF1690), not authority wording establishing the exact universal Mic19 class. No sequence alignment or exhaustive alternate-family search performed. |
| micro-tax-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete native taxon name/rank/lineage response; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/tax-4932.raw | supports | 4932: Saccharomyces cerevisiae, rank species. Species/reference strain is not substituted for W303, YPH499 or thermophilic source proteins. |
| micro-tax-559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Complete native taxon name/rank/lineage response; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/tax-559292.raw | supports | 559292: Saccharomyces cerevisiae S288C, rank strain. Species/reference strain is not substituted for W303, YPH499 or thermophilic source proteins. |
| micro-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005743,GO:0007007,GO:0042407,GO:0044284,GO:0061617,GO:0098800; All six exact current GO terms: status, full definitions/synonyms and returned typed child links; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/go.raw | supports | GO0061617 remains exact MICOS identity with six named yeast subunits; GO0098800 is the broader inner-membrane protein-complex parent, GO0005743 containing membrane, GO0044284 junction, GO0007007 organization and GO0042407 cristae formation. Active terms, no is_a/parthood interchange. |
| micro-GO0061617-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0061617/ancestors?relations=is_a; Complete is_a-only ancestor response; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/GO0061617-ancestors.raw | supports | Confirms the appropriate generic membrane protein-complex ancestry; does not turn either source-defined subcomplex into the whole MICOS identity. |
| micro-GO0098800-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0098800/ancestors?relations=is_a; Complete is_a-only ancestor response; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/GO0098800-ancestors.raw | supports | Confirms the appropriate generic membrane protein-complex ancestry; does not turn either source-defined subcomplex into the whole MICOS identity. |
| micro-go-search-Mic10 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=Mic10&amp;limit=100&amp;page=1; Complete first page and hit/page counts; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/go-search-Mic10.raw | supports | The specified current QuickGO text query returned zero hits. This bounded query supports retaining the existing source-defined minted identity but does not prove global ontology absence under every synonym. |
| micro-go-search-Mic60-Mic19 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=Mic60+Mic19&amp;limit=100&amp;page=1; Complete first page and hit/page counts; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/go-search-Mic60-Mic19.raw | supports | The specified current QuickGO text query returned zero hits. This bounded query supports retaining the existing source-defined minted identity but does not prove global ontology absence under every synonym. |
| micro-bock2022-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1126%2Fsciadv.abo4946%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact MED bibliographic identity, authors/DOI and complete indexed abstract; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/bock2022-meta.raw | context_only | Structural insights into crista junction formation by the Mic60-Mic19 complex.; authors Bock-Bierbaum T, Funck K, Wollweber F, Lisicki E, von der Malsburg K, von der Malsburg A, Laborenz J, Noel JK, Hessenberger M, Jungbluth S, Bernert C, Kunz S, Riedel D, Lilie H, Jakobs S, van der Laan M, Daumke O.; PMID36044574, DOI10.1126/sciadv.abo4946. Complete abstract and metadata read; no body claim unless separately listed. Pfanner 2014 is nomenclature synthesis rather than an independent primary experiment. |
| micro-friedman2015-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.7554%2Felife.07739%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact MED bibliographic identity, authors/DOI and complete indexed abstract; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/friedman2015-meta.raw | context_only | MICOS coordinates with respiratory complexes and lipids to establish mitochondrial inner membrane architecture.; authors Friedman JR, Mourier A, Yamada J, McCaffery JM, Nunnari J.; PMID25918844, DOI10.7554/elife.07739. Complete abstract and metadata read; no body claim unless separately listed. Pfanner 2014 is nomenclature synthesis rather than an independent primary experiment. |
| micro-harner2011-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Femboj.2011.379%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact MED bibliographic identity, authors/DOI and complete indexed abstract; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/harner2011-meta.raw | context_only | The mitochondrial contact site complex, a determinant of mitochondrial architecture.; authors Harner M, Körner C, Walther D, Mokranjac D, Kaesmacher J, Welsch U, Griffith J, Mann M, Reggiori F, Neupert W.; PMID22009199, DOI10.1038/emboj.2011.379. Complete abstract and metadata read; no body claim unless separately listed. Pfanner 2014 is nomenclature synthesis rather than an independent primary experiment. |
| micro-hessenberger2017-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fncomms15258%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact MED bibliographic identity, authors/DOI and complete indexed abstract; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/hessenberger2017-meta.raw | context_only | Regulated membrane remodeling by Mic60 controls formation of mitochondrial crista junctions.; authors Hessenberger M, Zerbes RM, Rampelt H, Kunz S, Xavier AH, Purfürst B, Lilie H, Pfanner N, van der Laan M, Daumke O.; PMID28561061, DOI10.1038/ncomms15258. Complete abstract and metadata read; no body claim unless separately listed. Pfanner 2014 is nomenclature synthesis rather than an independent primary experiment. |
| micro-hoppins2011-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1083%2Fjcb.201107053%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact MED bibliographic identity, authors/DOI and complete indexed abstract; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/hoppins2011-meta.raw | context_only | A mitochondrial-focused genetic interaction map reveals a scaffold-like complex required for inner membrane organization in mitochondria.; authors Hoppins S, Collins SR, Cassidy-Stone A, Hummel E, Devay RM, Lackner LL, Westermann B, Schuldiner M, Weissman JS, Nunnari J.; PMID21987634, DOI10.1083/jcb.201107053. Complete abstract and metadata read; no body claim unless separately listed. Pfanner 2014 is nomenclature synthesis rather than an independent primary experiment. |
| micro-malsburg2011-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.devcel.2011.08.026%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact MED bibliographic identity, authors/DOI and complete indexed abstract; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/malsburg2011-meta.raw | context_only | Dual role of mitofilin in mitochondrial membrane organization and protein biogenesis.; authors von der Malsburg K, Müller JM, Bohnert M, Oeljeklaus S, Kwiatkowska P, Becker T, Loniewska-Lwowska A, Wiese S, Rao S, Milenkovic D, Hutu DP, Zerbes RM, Schulze-Specking A, Meyer HE, Martinou JC, Rospert S, Rehling P, Meisinger C, Veenhuis M, Warscheid B, van der Klei IJ, Pfanner N, Chacinska A, van der Laan M.; PMID21944719, DOI10.1016/j.devcel.2011.08.026. Complete abstract and metadata read; no body claim unless separately listed. Pfanner 2014 is nomenclature synthesis rather than an independent primary experiment. |
| micro-pfanner2014-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1083%2Fjcb.201401006%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact MED bibliographic identity, authors/DOI and complete indexed abstract; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/pfanner2014-meta.raw | context_only | Uniform nomenclature for the mitochondrial contact site and cristae organizing system.; authors Pfanner N, van der Laan M, Amati P, Capaldi RA, Caudy AA, Chacinska A, Darshi M, Deckers M, Hoppins S, Icho T, Jakobs S, Ji J, Kozjak-Pavlovic V, Meisinger C, Odgren PR, Park SK, Rehling P, Reichert AS, Sheikh MS, Taylor SS, Tsuchida N, van der Bliek AM, van der Klei IJ, Weissman JS, Westermann B, Zha J, Neupert W, Nunnari J.; PMID24687277, DOI10.1083/jcb.201401006. Complete abstract and metadata read; no body claim unless separately listed. Pfanner 2014 is nomenclature synthesis rather than an independent primary experiment. |
| micro-rampelt2018-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.jmb.2018.04.037%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact MED bibliographic identity, authors/DOI and complete indexed abstract; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/rampelt2018-meta.raw | context_only | Assembly of the Mitochondrial Cristae Organizer Mic10 Is Regulated by Mic26-Mic27 Antagonism and Cardiolipin.; authors Rampelt H, Wollweber F, Gerke C, de Boer R, van der Klei IJ, Bohnert M, Pfanner N, van der Laan M.; PMID29733859, DOI10.1016/j.jmb.2018.04.037. Complete abstract and metadata read; no body claim unless separately listed. Pfanner 2014 is nomenclature synthesis rather than an independent primary experiment. |
| micro-tirrell2020-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1083%2Fjcb.202003024%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact MED bibliographic identity, authors/DOI and complete indexed abstract; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/tirrell2020-meta.raw | context_only | MICOS subcomplexes assemble independently on the mitochondrial inner membrane in proximity to ER contact sites.; authors Tirrell PS, Nguyen KN, Luby-Phelps K, Friedman JR.; PMID33053165, DOI10.1083/jcb.202003024. Complete abstract and metadata read; no body claim unless separately listed. Pfanner 2014 is nomenclature synthesis rather than an independent primary experiment. |
| micro-pmid-14562095 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact MED bibliographic identity, authors/DOI and complete indexed abstract; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/pmid-14562095.raw | context_only | Global analysis of protein localization in budding yeast.; authors Huh WK, Falvo JV, Gerke LC, Carroll AS, Howson RW, Weissman JS, O'Shea EK.; PMID14562095, DOI10.1038/nature02026. Complete abstract and metadata read; no body claim unless separately listed. Pfanner 2014 is nomenclature synthesis rather than an independent primary experiment. |
| micro-pmid-16823961 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A16823961+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact MED bibliographic identity, authors/DOI and complete indexed abstract; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/pmid-16823961.raw | context_only | Toward the complete yeast mitochondrial proteome: multidimensional separation techniques for mitochondrial proteomics.; authors Reinders J, Zahedi RP, Pfanner N, Meisinger C, Sickmann A.; PMID16823961, DOI10.1021/pr050477f. Complete abstract and metadata read; no body claim unless separately listed. Pfanner 2014 is nomenclature synthesis rather than an independent primary experiment. |
| micro-pmid-19528297 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A19528297+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact MED bibliographic identity, authors/DOI and complete indexed abstract; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/pmid-19528297.raw | context_only | Formation of cristae and crista junctions in mitochondria depends on antagonism between Fcj1 and Su e/g.; authors Rabl R, Soubannier V, Scholz R, Vogel F, Mendl N, Vasiljev-Neumeyer A, Körner C, Jagasia R, Keil T, Baumeister W, Cyrklaff M, Neupert W, Reichert AS.; PMID19528297, DOI10.1083/jcb.200811099. Complete abstract and metadata read; no body claim unless separately listed. Pfanner 2014 is nomenclature synthesis rather than an independent primary experiment. |
| micro-pmid-21944719 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A21944719+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact MED bibliographic identity, authors/DOI and complete indexed abstract; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/pmid-21944719.raw | context_only | Dual role of mitofilin in mitochondrial membrane organization and protein biogenesis.; authors von der Malsburg K, Müller JM, Bohnert M, Oeljeklaus S, Kwiatkowska P, Becker T, Loniewska-Lwowska A, Wiese S, Rao S, Milenkovic D, Hutu DP, Zerbes RM, Schulze-Specking A, Meyer HE, Martinou JC, Rospert S, Rehling P, Meisinger C, Veenhuis M, Warscheid B, van der Klei IJ, Pfanner N, Chacinska A, van der Laan M.; PMID21944719, DOI10.1016/j.devcel.2011.08.026. Complete abstract and metadata read; no body claim unless separately listed. Pfanner 2014 is nomenclature synthesis rather than an independent primary experiment. |
| micro-pmid-21987634 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A21987634+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact MED bibliographic identity, authors/DOI and complete indexed abstract; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/pmid-21987634.raw | context_only | A mitochondrial-focused genetic interaction map reveals a scaffold-like complex required for inner membrane organization in mitochondria.; authors Hoppins S, Collins SR, Cassidy-Stone A, Hummel E, Devay RM, Lackner LL, Westermann B, Schuldiner M, Weissman JS, Nunnari J.; PMID21987634, DOI10.1083/jcb.201107053. Complete abstract and metadata read; no body claim unless separately listed. Pfanner 2014 is nomenclature synthesis rather than an independent primary experiment. |
| micro-rampelt2018-pdf | https://pure.rug.nl/ws/portalfiles/portal/61925901/1_s2.0_S0022283618303498_main_1_.pdf; Genuine institutional PDF extracted text lines1–360, main printed pages1883–1888 including Figures1–4 text captions and embedded methods; no figure pixels or unread references/supplements; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/rampelt2018-pdf.raw | supports | YPH499 glycerol-grown mitochondria, native gels and crosslinking support Mic26/Mic27 antagonism affecting Mic10 oligomers; normal four-component module differs from conditional three-component core. Cardiolipin stabilizes oligomers; direct binding site and universal copy count are not established. |
| micro-friedman2015-s3 | https://pmc-oa-opendata.s3.amazonaws.com/PMC4434539.1/PMC4434539.1.xml; Genuine JATS Results s2-2,s2-3,s2-4,s2-5,s2-7 and Methods s4-1,s4-3,s4-6 fully read with embedded captions; only Figure3 pixels separately inspected; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/friedman2015-s3.raw | supports | W303 conditional deletion/reconstitution, fluorescence and crosslinked co-IP/MS distinguish Mic60 and Mic10/12/27 subcomplexes. Mic10 requirement for Mic27 foci differs from Mic12 reduction; Mic26 not recovered in the conditional core does not erase normal membership. Crista proximity inferred from fluorescent markers after unsuccessful direct immuno-EM, not direct junction localization proof. ERMES/lipids are not automatically constituents. |
| micro-tirrell2020-s3 | https://pmc-oa-opendata.s3.amazonaws.com/PMC7545361.1/PMC7545361.1.xml; Genuine JATS sections s3,s4,s11 fully read, embedded Figure1/2/S1/S2 and video captions; no movies, pixels, separate supplements or other sections; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/tirrell2020-s3.raw | supports | W303 and explicitly separate BY4741/42 bypass contexts: Mic10 module assembly depends on ERMES function; Vps13 bypass restores organization. Mic60 self-assembles independently. Proximity and functional rescue do not prove obligatory direct-template binding or add ERMES/Vps13 as subunits. |
| micro-hessenberger2017-s3 | https://pmc-oa-opendata.s3.amazonaws.com/PMC5460017.1/PMC5460017.1.xml; Genuine JATS sections Mic60 binds and remodels liposomes; Mic19 binds to Mic60 and enhances membrane remodelling; LBS1 plays a critical role in IM ultrastructure and function; Discussion; Expression and purification; EM; Yeast strains and plasmids; full Figure4 caption/pixels; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/hessenberger2017-s3.raw | supports | Purified C. thermophilum Mic60sol208–691 and Mic19 in Folch liposomes support direct interaction, lipid recruitment and tubulation enhancement, with engineered/domain-specific limits. YPH499 mutant/cristae/respiratory assays are separate. Leakage readout is not physiological permeability; native universal 4:4/barrier is not proved. |
| micro-bock2022-s3 | https://pmc-oa-opendata.s3.amazonaws.com/PMC9432830.1/PMC9432830.1.xml; Genuine JATS entire RESULTS four subsections plus embedded Figures2–4 captions, DISCUSSION/Figure5 caption, Cloning and plasmids, S.cerevisiae strains and plasmids, Isolation of S.cerevisiae mitochondria; no pixels/supplements/raw density; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/bock2022-s3.raw | supports | L. thermotolerans coiled-coil and engineered C. thermophilum Mic60/Mic19 constructs support a tetramer/heteromer model; YPH499 validation is distinct. Suggested strut/barrier architecture remains a model, native filament identity unresolved, and these constructs do not establish universal native4:4 stoichiometry. |
| micro-hoppins2011-s3 | https://pmc-oa-opendata.s3.amazonaws.com/PMC3198156.1/PMC3198156.1.xml; Genuine JATS Results sections6–9 by retained section index (Fcj1-containing complex; conserved inner membrane complex; inner membrane organization; complex structures), Discussion, Yeast strains generation and manipulation, complete Proteomic analysis and Electron microscopy analysis; embedded captions only; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/hoppins2011-s3.raw | supports | W303 tagged purifications/proteomics identify six subunits and suborganization. Deletion/ultrathin sections and tomography find residual junctions, so the paper explicitly does not establish universal junction-formation essentiality. Inner membrane scaffold/maintenance and contact interactions support the current qualified FUNCTION graph; direct native architecture is not resolved. |
| micro-pfanner2014-s3 | https://pmc-oa-opendata.s3.amazonaws.com/PMC3971754.1/PMC3971754.1.xml; Complete body, Figure1 textual caption and Table1 nomenclature including all naming guidelines; no figure pixels; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/pfanner2014-s3.raw | supports | Consensus nomenclature unifies MICOS/MINOS/MitOS and six yeast names; mammalian extra Mic25 and lineage differences are explicit. This is secondary/nomenclature authority, not new formation experiment. |
| micro-friedman2015-fig3 | https://pmc-oa-opendata.s3.amazonaws.com/PMC4434539.1/elife07739f003.jpg; Actual complete multipanel pixels viewed in maintained file; fresh source image is byte-identical; caption/licence read in corresponding JATS; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/friedman2015-fig3.raw | supports | Contextual cellular/mutant assays, not a purified molecular-complex image. Figure3 A–G includes W303 confocal deletion/reconstitution, foci counts and peptide co-purification; record scope/OTHER modality is accurate. Article permissions explicitly CC BY 4.0; relevant caption contains no contrary third-party credit. |
| micro-image-0 | data/images/other/mic10_subcomplex/pmc4434539_fig3.jpg; Actual maintained image bytes and independently viewed complete panels | context_only | Fresh source bytes equal maintained file_sha256; full-panel scope and licence/attribution checked against current genuine JATS. No new OA package MD5 query was made. |
| micro-hessenberger2017-fig4 | https://pmc-oa-opendata.s3.amazonaws.com/PMC5460017.1/ncomms15258-f4.jpg; Actual complete multipanel pixels viewed in maintained file; fresh source image is byte-identical; caption/licence read in corresponding JATS; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/hessenberger2017-fig4.raw | supports | Contextual cellular/mutant assays, not a purified molecular-complex image. Figure4 a–i includes YPH499 affinity/growth, cryo-TEM c–f with500 nm scale bars, junction counts and respiratory activities; full-multipanel OTHER modality and contextual scope are accurate. Article permissions explicitly CC BY 4.0; relevant caption contains no contrary third-party credit. |
| micro-image-1 | data/images/other/mic60_mic19_complex/pmc5460017_f4.jpg; Actual maintained image bytes and independently viewed complete panels | context_only | Fresh source bytes equal maintained file_sha256; full-panel scope and licence/attribution checked against current genuine JATS. No new OA package MD5 query was made. |
| micro-harner2011-s3 | https://pmc-oa-opendata.s3.amazonaws.com/PMC3230385.1/PMC3230385.1.xml; Actual status/response only; no scientific body claim; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/harner2011-s3.raw | context_only | HTTP 404, bytes 320; unavailable/rate-limited/timeout/challenge. Harner legacy HTTP200 is a reCAPTCHA page, not article text. Genuine successful alternate responses have separate dates/hashes. |
| micro-harner2011-legacy | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3230385/; Actual status/response only; no scientific body claim; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/harner2011-legacy.raw | context_only | HTTP 200, bytes 21411; unavailable/rate-limited/timeout/challenge. Harner legacy HTTP200 is a reCAPTCHA page, not article text. Genuine successful alternate responses have separate dates/hashes. |
| micro-protein-Q96VH5 | https://rest.uniprot.org/uniprotkb/Q96VH5.json; Actual status/response only; no scientific body claim; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/protein-Q96VH5.raw | context_only | HTTP 503, bytes 286; unavailable/rate-limited/timeout/challenge. Harner legacy HTTP200 is a reCAPTCHA page, not article text. Genuine successful alternate responses have separate dates/hashes. |
| micro-protein-Q96VH5-retry | https://rest.uniprot.org/uniprotkb/Q96VH5?format=json; Actual status/response only; no scientific body claim; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/protein-Q96VH5-retry.raw | context_only | HTTP None, bytes 0; unavailable/rate-limited/timeout/challenge. Harner legacy HTTP200 is a reCAPTCHA page, not article text. Genuine successful alternate responses have separate dates/hashes. |
| micro-ipr-IPR019133 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR019133/; Actual status/response only; no scientific body claim; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/ipr-IPR019133.raw | context_only | HTTP 429, bytes 61; unavailable/rate-limited/timeout/challenge. Harner legacy HTTP200 is a reCAPTCHA page, not article text. Genuine successful alternate responses have separate dates/hashes. |
| micro-ipr-IPR012471 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR012471/; Actual status/response only; no scientific body claim; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/ipr-IPR012471.raw | context_only | HTTP 429, bytes 61; unavailable/rate-limited/timeout/challenge. Harner legacy HTTP200 is a reCAPTCHA page, not article text. Genuine successful alternate responses have separate dates/hashes. |
| micro-query-MIC26-retry | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AMIC26%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100&amp;fields=accession%2Cid%2Cprotein_name%2Cgene_names%2Corganism_id%2Creviewed; Actual status/response only; no scientific body claim; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/query-MIC26-retry.raw | context_only | HTTP None, bytes 0; unavailable/rate-limited/timeout/challenge. Harner legacy HTTP200 is a reCAPTCHA page, not article text. Genuine successful alternate responses have separate dates/hashes. |
| micro-query-MIC60-retry | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AMIC60%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100&amp;fields=accession%2Cid%2Cprotein_name%2Cgene_names%2Corganism_id%2Creviewed; Actual status/response only; no scientific body claim; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/query-MIC60-retry.raw | context_only | HTTP None, bytes 0; unavailable/rate-limited/timeout/challenge. Harner legacy HTTP200 is a reCAPTCHA page, not article text. Genuine successful alternate responses have separate dates/hashes. |
| micro-retrieval-index | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/source-receipts.json; All48 actual initial authorized retrieval receipts; earlier sandbox DNS failures separately retained in initial-sandbox-dns-attempt | context_only | Index records actual URLs/statuses/response hashes and times; failed UniProt/InterPro entries are not biological evidence. Successful retry receipts are separately bound in the individual evidence rows. |
| micro-adapter-catalogue | https://imodulondb.org/api/organisms; Complete official organism/dataset response; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/adapter-catalogue.raw | supports | All 20 organisms and 28 dataset entries inspected. No Saccharomyces or other relevant fungal/metazoan biological-host dataset appears; bacterial recombinant expression is not a host proxy. All three records are applicable because they make positive molecular/pathway assertions. No foreign-host gene/module queries or expression-to-assembly inference. |
| micro-native-mic10_subcomplex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mic10_subcomplex-uniprot-verify-receipt.json; Full actual command receipt; complete stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mic10_subcomplex-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | 4 reviewed S288C protein examples and4 COVERED typed nodes. Native exit0 checks accession/coverage, not primary membership or physical formation. |
| micro-native-mic10_subcomplex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mic10_subcomplex-uniprot-causal-receipt.json; Full actual command receipt; complete stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mic10_subcomplex-uniprot-causal.log SHA256 6c1d97f2cb25045ddae5e20a9aa6562b9fa6be6961f961243b68c041557dc83c | supports | 4 reviewed S288C protein examples and4 COVERED typed nodes. Native exit0 checks accession/coverage, not primary membership or physical formation. |
| micro-native-mic60_mic19_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mic60_mic19_complex-uniprot-verify-receipt.json; Full actual command receipt; complete stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mic60_mic19_complex-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | 2 reviewed S288C protein examples and2 COVERED typed nodes. Native exit0 checks accession/coverage, not primary membership or physical formation. |
| micro-native-mic60_mic19_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mic60_mic19_complex-uniprot-causal-receipt.json; Full actual command receipt; complete stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mic60_mic19_complex-uniprot-causal.log SHA256 22d7a0d901ab4f94314139e8db344060d6646aebc95400a3456ce381afa664b4 | supports | 2 reviewed S288C protein examples and2 COVERED typed nodes. Native exit0 checks accession/coverage, not primary membership or physical formation. |
| micro-native-micos_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/micos_complex-uniprot-verify-receipt.json; Full actual command receipt; complete stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/micos_complex-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | 0 protein examples and0 typed GENE_OR_PROTEIN nodes; empty check is not molecular validation. Native exit0 checks accession/coverage, not primary membership or physical formation. |
| micro-native-micos_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/micos_complex-uniprot-causal-receipt.json; Full actual command receipt; complete stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/micos_complex-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | 0 protein examples and0 typed GENE_OR_PROTEIN nodes; empty check is not molecular validation. Native exit0 checks accession/coverage, not primary membership or physical formation. |
| micro-historical-harner-access | reviews/structured/20261022T084806Z-micos-complex-audit/review.yaml; Immutable original evidence access-PMC3230385-xml | context_only | Historical kind authority/context_only actually describes HTTP500 transport only. Original URL=https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3230385/fullTextXML; access=2026-10-22T08:08:06.830531Z; response SHA=ff1bf7f29cdfbc01884ed64e7196167b6065c7d2b29c3f5d47cb6d98f01adc8d; original summary=Harner2011 XML route returnedHTTP500; the native bibliography and complete abstract were read separately. No primary body was inspected from this response.. No old source bytes are newly retrieved or upgraded. Successor should classify validation/context_only while retaining original provenance. |
| plaque-record-3 | data/structures/other/mim_complex.yaml; Entire current maintained record, all fields/graphs/history; source HEAD c9fe63bdff984abad241949c21dab3b13e975d1f | context_only | Current complete record read; old frozen SHA dc0d4007dfe5d82f22b45d46cc12e3c934ce3ebe92d7ed7b48c25be1ea715c5f; current SHA 61bfb31d9aca0a2be252843e729f32e2b8ff9f3d02c77ba43e06d6f5a9229916. |
| plaque-original-3 | reviews/structured/20261022T084807Z-mim-complex-audit/review.yaml; Complete original YAML and paired Markdown, scientific findings/actions, declared access and historical input ownership | context_only | Original observation retained without changing historical evidence or promoting its old executions to fresh results. |
| plaque-record-4 | data/structures/other/mis12_mind_type_complex.yaml; Entire current maintained record, all fields/graphs/history; source HEAD c9fe63bdff984abad241949c21dab3b13e975d1f | context_only | Current complete record read; old frozen SHA 6b16e919810eceb24433ded999d28a548adbb8c5e0d55af4eb63fe3e4eaac1a6; current SHA 029ac75e12045a39ff6da937c63cff087715e76aadf1b65ad773f30bdfc4e944. |
| plaque-original-4 | reviews/structured/20261022T084808Z-mis12-mind-type-complex-audit/review.yaml; Complete original YAML and paired Markdown, scientific findings/actions, declared access and historical input ownership | context_only | Original observation retained without changing historical evidence or promoting its old executions to fresh results. |
| plaque-record-5 | data/structures/other/mitochondrial_inner_membrane_peptidase_complex.yaml; Entire current maintained record, all fields/graphs/history; source HEAD c9fe63bdff984abad241949c21dab3b13e975d1f | context_only | Current complete record read; old frozen SHA 8eb6f174c969fc2aef5a84a2a473fe42a66158531ae26422ccfd8ae3407227e0; current SHA 8eb6f174c969fc2aef5a84a2a473fe42a66158531ae26422ccfd8ae3407227e0. |
| plaque-original-5 | reviews/structured/20261022T084808Z-mitochondrial-inner-membrane-peptidase-complex-audit/review.yaml; Complete original YAML and paired Markdown, scientific findings/actions, declared access and historical input ownership | context_only | Original observation retained without changing historical evidence or promoting its old executions to fresh results. |
| plaque-policy | docs/CURATION.md; Evidence/snippet contract; taxon-agnostic component classes, reviewed-label grounding, formation versus function and append-only discussion rationale | context_only | Frozen native requirements independently applied, including actual access scope and optional-field limits. |
| plaque-schema | src/cellstructuremech/schema/cellstructuremech.yaml; Current component, essentiality, graph-node and evidence fields | context_only | Frozen native requirements independently applied, including actual access scope and optional-field limits. |
| plaque-review-policy | docs/record-reviews.md; Complete native provenance, checks, finding lineage, verdict and save contract | context_only | Frozen native requirements independently applied, including actual access scope and optional-field limits. |
| plaque-profile | docs/record-review-profile.md; Complete local review profile | context_only | Frozen native requirements independently applied, including actual access scope and optional-field limits. |
| plaque-skill | .claude/skills/review-yaml-record/SKILL.md; Complete single-record skill, whole-record structured-source triggers and bounded search rules | context_only | Frozen native requirements independently applied, including actual access scope and optional-field limits. |
| plaque-original-native-checks | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/original-checks.json; All three actual original validate/render commands; historical input hashes; current 51 frozen inputs | supports | Three original pairs validate and render byte-identically, all their historical inputs match retained Git revisions, and all 51 current input hashes match source and worktree. Receipt contains actual command times and logs. |
| plaque-delta-3 | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/t3-stale.diff; Exact old frozen record to current source diff | context_only | Substantive changed claims independently assessed; original review unchanged. |
| plaque-delta-4 | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/t4-stale.diff; Exact old frozen record to current source diff | context_only | Substantive changed claims independently assessed; original review unchanged. |
| plaque-native-mim_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mim_complex-uniprot-verify-receipt.json; Actual command receipt; separate stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mim_complex-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0 at current source; 2 reviewed examples and 2 COVERED nodes. |
| plaque-native-mim_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mim_complex-uniprot-causal-receipt.json; Actual command receipt; separate stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mim_complex-uniprot-causal.log SHA256 4d2fc324bc37f34d33055b3b2a52a9e6d8020dd8c109abbf7d0cf67d8ff88743 | supports | Actual exit0 at current source; 2 reviewed examples and 2 COVERED nodes. |
| plaque-native-mis12_mind_type_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mis12_mind_type_complex-uniprot-verify-receipt.json; Actual command receipt; separate stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mis12_mind_type_complex-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0 at current source; 4 reviewed examples; 5 typed nodes: 2 COVERED, 2 PARTIAL_EXAMPLES for MIS12/PMF1 class symbols, and 1 UNANCHORED_WITH_UNIPROT external outer-kinetochore actor. |
| plaque-native-mis12_mind_type_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mis12_mind_type_complex-uniprot-causal-receipt.json; Actual command receipt; separate stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mis12_mind_type_complex-uniprot-causal.log SHA256 fad6678665a9bc3509cf409f377cc2e2229d22e04659cf35e9025cb818052429 | supports | Actual exit0 at current source; 4 reviewed examples; 5 typed nodes: 2 COVERED, 2 PARTIAL_EXAMPLES for MIS12/PMF1 class symbols, and 1 UNANCHORED_WITH_UNIPROT external outer-kinetochore actor. |
| plaque-native-mitochondrial_inner_membrane_peptidase_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_inner_membrane_peptidase_complex-uniprot-verify-receipt.json; Actual command receipt; separate stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_inner_membrane_peptidase_complex-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0 at current source; 0 examples and 0 typed nodes; empty inventory is not scientific completeness proof. |
| plaque-native-mitochondrial_inner_membrane_peptidase_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_inner_membrane_peptidase_complex-uniprot-causal-receipt.json; Actual command receipt; separate stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_inner_membrane_peptidase_complex-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Actual exit0 at current source; 0 examples and 0 typed nodes; empty inventory is not scientific completeness proof. |
| plaque-go-0000444-parents | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000444/ancestors?relations=is_a,part_of; Complete requested ancestor response; mixed is_a/part_of traversal is transitive context, not an assertion of a direct edge. Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0000444-parents.raw SHA256 4cfb74a00e09da5aa1ce323dfb9f23b49616831d5ece5126bf77ca56276cc80e; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0000444-parents.receipt.json SHA256 1f633db068997205aba5039117bb8159c7e8a62372b4f771118dfcd9e7e6d1fd. | supports | Current GO authority for 0000444; exact identity and anatomical/function scope assessed without converting transitive ancestors into direct parthood. |
| plaque-go-0000444 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000444; Exact current term identity, definition, obsolete flag, synonym qualifier strings and typed children where present. Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0000444.raw SHA256 9fed03461fbad8116800ebf65bc0e08646d504abeb84f859b14e23cc836cbc2a; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0000444.receipt.json SHA256 64dd80e0fb2d6dcef5c0ceb25f25ae5dcccbc3ee3432f1108e5daccee78beb96. | supports | Current GO authority for 0000444; exact identity and anatomical/function scope assessed without converting transitive ancestors into direct parthood. |
| plaque-go-0000776 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000776; Exact current term identity, definition, obsolete flag, synonym qualifier strings and typed children where present. Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0000776.raw SHA256 1b1d92f2f3ec584f7fe8d61021ebb433586609a130c97e9ec37a07cfda864c76; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0000776.receipt.json SHA256 94dc1b4d874552f77001ed1991fbb177ef5a070201ecc6a0af089eac0614e0c7. | supports | Current GO authority for 0000776; exact identity and anatomical/function scope assessed without converting transitive ancestors into direct parthood. |
| plaque-go-0000940-parents | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000940/ancestors?relations=is_a,part_of; Complete requested ancestor response; mixed is_a/part_of traversal is transitive context, not an assertion of a direct edge. Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0000940-parents.raw SHA256 f8578421ec888eeace5a4ada21783cee98be90e03e091348c536dfd85207213c; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0000940-parents.receipt.json SHA256 9ab35dbf3fd4ed9c3248581ae19c666b315bae2c44dc71c592c4a742f1a4aeeb. | supports | Current GO authority for 0000940; exact identity and anatomical/function scope assessed without converting transitive ancestors into direct parthood. |
| plaque-go-0000940 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000940; Exact current term identity, definition, obsolete flag, synonym qualifier strings and typed children where present. Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0000940.raw SHA256 10873acde0d686071f570f5abe217c347fff5836f301f7f9b1e05ceab4ded9e8; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0000940.receipt.json SHA256 3de0a651305aa93736db397d796c2316f7989ccacba09de6b2058b8a258f8751. | supports | Current GO authority for 0000940; exact identity and anatomical/function scope assessed without converting transitive ancestors into direct parthood. |
| plaque-go-0005741 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005741; Exact current term identity, definition, obsolete flag, synonym qualifier strings and typed children where present. Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0005741.raw SHA256 701047b3a306f8b0b4bb945bce5d7e5e99dafe21be3fc7a97c10b63f9cbe2ca6; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0005741.receipt.json SHA256 35b531ba87af32fb8e84bd9eee68f0f40101dd29d3338fc6d6a6cf16bc45c6b5. | supports | Current GO authority for 0005741; exact identity and anatomical/function scope assessed without converting transitive ancestors into direct parthood. |
| plaque-go-0005743 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005743; Exact current term identity, definition, obsolete flag, synonym qualifier strings and typed children where present. Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0005743.raw SHA256 ba28e8a48bcde74c14009e24937b39e33b51a79d50486259b47b8a3bfb4122e4; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0005743.receipt.json SHA256 96ccfe51578bb2ab2550c942470a4c2b3c670a501cb82ab5bc3cdd4e9a0eb733. | supports | Current GO authority for 0005743; exact identity and anatomical/function scope assessed without converting transitive ancestors into direct parthood. |
| plaque-go-0032991 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032991; Exact current term identity, definition, obsolete flag, synonym qualifier strings and typed children where present. Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0032991.raw SHA256 480165003b2c8a406006ff17c4cfe836fc000541ad5dac1ca0f585ed30c02e87; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0032991.receipt.json SHA256 5e10b5379b43076983fd1c096d9a77fed93fc3fe4dea65da3befb6f9c5d2878a. | supports | Current GO authority for 0032991; exact identity and anatomical/function scope assessed without converting transitive ancestors into direct parthood. |
| plaque-go-0034982 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0034982; Exact current term identity, definition, obsolete flag, synonym qualifier strings and typed children where present. Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0034982.raw SHA256 29be07b90645f1ae78346a2b15e315fdac3c150b300c238c28e9c6faf20f61aa; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0034982.receipt.json SHA256 382d9193aba3d9be3ab863b60e05b63ecc293967b9acabed9b8ca6260e429893. | supports | Current GO authority for 0034982; exact identity and anatomical/function scope assessed without converting transitive ancestors into direct parthood. |
| plaque-go-0042720-parents | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0042720/ancestors?relations=is_a,part_of; Complete requested ancestor response; mixed is_a/part_of traversal is transitive context, not an assertion of a direct edge. Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0042720-parents.raw SHA256 05474ce864a39e43ecefb2910b2d920b131426e0af4fc858f3a15ee3e0165fcb; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0042720-parents.receipt.json SHA256 c74a640232b3c0d77e22faa94684f250f12fca543761468ada20059d652c28e7. | supports | Current GO authority for 0042720; exact identity and anatomical/function scope assessed without converting transitive ancestors into direct parthood. |
| plaque-go-0042720 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0042720; Exact current term identity, definition, obsolete flag, synonym qualifier strings and typed children where present. Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0042720.raw SHA256 9f5e79e0da4d08825a74c43fbe221d3e08d4ea52e1d69b5f176eb9daa0476a47; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0042720.receipt.json SHA256 a3b19dd6b45235e46c57a6e64a7fec4cd611cd262d6df482f0e2600004427228. | supports | Current GO authority for 0042720; exact identity and anatomical/function scope assessed without converting transitive ancestors into direct parthood. |
| plaque-go-0098799 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0098799; Exact current term identity, definition, obsolete flag, synonym qualifier strings and typed children where present. Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0098799.raw SHA256 91e7dcb5172450141beb63b1231dd018f7f517db9c5cf1c0fc4699d8a4f0654c; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0098799.receipt.json SHA256 1b427512530ef2ed9615a9a3d057d471c2ba5c3a9993ae32ef6bf507d9faa92a. | supports | Current GO authority for 0098799; exact identity and anatomical/function scope assessed without converting transitive ancestors into direct parthood. |
| plaque-go-0098800 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0098800; Exact current term identity, definition, obsolete flag, synonym qualifier strings and typed children where present. Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0098800.raw SHA256 b5d2eb220eb1a1a42ad99cfe91d358cb21597a3adea956e3d2c88cb2dae93ce6; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0098800.receipt.json SHA256 e929fbcff97e280e76f5ca2a797ae42cb9e2c618121aa7eb0aff12b763f3823f. | supports | Current GO authority for 0098800; exact identity and anatomical/function scope assessed without converting transitive ancestors into direct parthood. |
| plaque-go-0140595-parents | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0140595/ancestors?relations=is_a,part_of; Complete requested ancestor response; mixed is_a/part_of traversal is transitive context, not an assertion of a direct edge. Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0140595-parents.raw SHA256 6efb033f6382bbccc6595e8489d29ed01e79a5b50e9b1187c47070c66d764bae; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0140595-parents.receipt.json SHA256 62b39c0ac9df5a4503d6c7329b365ac4c91f1a50bad9bcc0dae8175424d91b96. | supports | Current GO authority for 0140595; exact identity and anatomical/function scope assessed without converting transitive ancestors into direct parthood. |
| plaque-go-0140595 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0140595; Exact current term identity, definition, obsolete flag, synonym qualifier strings and typed children where present. Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0140595.raw SHA256 1d25381be57c943c9ce45320cc5ff140781ff399fff4a60bbf31f0460683e865; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0140595.receipt.json SHA256 ec7becf53c37b77a27380f2781dca06ac3522d19a59cc7ec8e694ae8c81557a3. | supports | Current GO authority for 0140595; exact identity and anatomical/function scope assessed without converting transitive ancestors into direct parthood. |
| plaque-go-1905370 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1905370; Exact current term identity, definition, obsolete flag, synonym qualifier strings and typed children where present. Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-1905370.raw SHA256 1989830b762b86f5ae7f05bfbdb47ce9327f3008df33eda95975a955ec1cf7c3; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-1905370.receipt.json SHA256 c3f57e05370885dbb0d7d39f4df5915561755179abd7a3480f51b9a6f5ca8b6b. | supports | Current GO authority for 1905370; exact identity and anatomical/function scope assessed without converting transitive ancestors into direct parthood. |
| plaque-go-7770059 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:7770059; Exact current term identity, definition, obsolete flag, synonym qualifier strings and typed children where present. Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-7770059.raw SHA256 8723d41f0bcd227a4fe858c0c0bd2dc8e05582d14c494bf417df483bcac3cdd9; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-7770059.receipt.json SHA256 200201569d5b8c596ceb6be1d8ee8d6db5b3cf36489551a3ea6c3b0610050e32. | supports | Current GO authority for 7770059; exact identity and anatomical/function scope assessed without converting transitive ancestors into direct parthood. |
| plaque-ipr-IPR013262 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013262/; Complete metadata type/name/description/member signatures; protein membership checked separately Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/ipr-IPR013262.raw SHA256 d8611a20731dfadc51d22a9fb4c2adec8ece54df8833f8b5f0f09afeb9453748; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/ipr-IPR013262.receipt.json SHA256 19f5ef8f84b3c3dd2f326810d7ccab2032c3937e414812884a28a729ef40ccd5. | supports | IPR013262 is type family: Outer membrane protein, MIM1/TOM13, mitochondrial. IPR016851 is narrower than the joint PMF1/Nnf1 class; the malformed IPR008685 organism phrase is not adopted. |
| plaque-ipr-IPR037652 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR037652/; Complete metadata type/name/description/member signatures; protein membership checked separately Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/ipr-IPR037652.raw SHA256 112d5a2021eabf25044253c0dee72db297d4099162b73ee2f355ab61f91ef866; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/ipr-IPR037652.receipt.json SHA256 f7d4a751934cffb686b9876b97133d1f3ed59c11a3aa24ab4016f57ef5d9d76b. | supports | IPR037652 is type family: Mim2. IPR016851 is narrower than the joint PMF1/Nnf1 class; the malformed IPR008685 organism phrase is not adopted. |
| plaque-ipr-IPR008685 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR008685/; Complete metadata type/name/description/member signatures; protein membership checked separately Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/ipr-IPR008685.raw SHA256 e06c4648173ec5ba44dd1528257de9374b2ed303a086b31e4e0990d8bc8be118; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/ipr-IPR008685.receipt.json SHA256 e394e445a7a3921c476e5a9ce10714e34049b98649b57cc16b7455731fbc4e6b. | supports | IPR008685 is type family: Centromere protein Mis12. IPR016851 is narrower than the joint PMF1/Nnf1 class; the malformed IPR008685 organism phrase is not adopted. |
| plaque-ipr-IPR013218 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013218/; Complete metadata type/name/description/member signatures; protein membership checked separately Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/ipr-IPR013218.raw SHA256 568c9f62ea14d27c815c8017bf6e92d6af320d04216eda090b565e925ff903c8; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/ipr-IPR013218.receipt.json SHA256 77e2c96d517aa69b55c94b83988757d6078c11534f5739f7c014a907ad1289d6. | supports | IPR013218 is type family: Kinetochore-associated protein Dsn1/Mis13. IPR016851 is narrower than the joint PMF1/Nnf1 class; the malformed IPR008685 organism phrase is not adopted. |
| plaque-ipr-IPR013950 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013950/; Complete metadata type/name/description/member signatures; protein membership checked separately Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/ipr-IPR013950.raw SHA256 925c729248004dc084e61343626a714a7be901e7d14e4ee16a1bae9ca63d94d8; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/ipr-IPR013950.receipt.json SHA256 bd181b2fc583e0019f79b3b49ebc22db40e7bc899c2c587e1f09902c838c0a43. | supports | IPR013950 is type family: Kinetochore Mis14/Nsl1. IPR016851 is narrower than the joint PMF1/Nnf1 class; the malformed IPR008685 organism phrase is not adopted. |
| plaque-ipr-IPR007128 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007128/; Complete metadata type/name/description/member signatures; protein membership checked separately Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/ipr-IPR007128.raw SHA256 65cb586ba7a68eaefdedad33aed45452e7b415359b3113570ca6a3919c4c57b2; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/ipr-IPR007128.receipt.json SHA256 9d50f322d899b6819acdd61344399b4602a99259471cc4f38c7999053bf4bfe7. | supports | IPR007128 is type family: Nuclear MIS12/MIND complex subunit PMF1/Nnf1. IPR016851 is narrower than the joint PMF1/Nnf1 class; the malformed IPR008685 organism phrase is not adopted. |
| plaque-ipr-IPR016851 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016851/; Complete metadata type/name/description/member signatures; protein membership checked separately Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/ipr-IPR016851.raw SHA256 39908cca1a702741dcf764a2e5e746206eb9cc5736580c8992a2db7a529a4a40; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/ipr-IPR016851.receipt.json SHA256 37499978aa8836fa5f084351db7bed76d2dffa58c45a929a7ee17a12742d6d43. | supports | IPR016851 is type family: Kinetochore-associated protein Nnf1. IPR016851 is narrower than the joint PMF1/Nnf1 class; the malformed IPR008685 organism phrase is not adopted. |
| plaque-up-Q08176-retry | https://rest.uniprot.org/uniprotkb/Q08176.json?format=json; Full native identity/status/primary gene/taxon, FUNCTION, SUBUNIT and SUBCELLULAR LOCATION comments and InterPro cross-references Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/up-Q08176-retry.raw SHA256 9a0724b67d38baaf0c88eda5fdf178ceb1063d1759cf9a636fdadb8b52c74bde; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/up-Q08176-retry.receipt.json SHA256 fa6a9f5e445e44c15b35b5a4c4021f22644d530c3add1d8794d58f497e909f5b. | supports | Reviewed Q08176 identifies MIM1 in reference strain S288C taxon559292. Species examples and class membership are distinct; annotation papers not otherwise listed are not certified read. |
| plaque-up-Q3E798 | https://rest.uniprot.org/uniprotkb/Q3E798.json; Full native identity/status/primary gene/taxon, FUNCTION, SUBUNIT and SUBCELLULAR LOCATION comments and InterPro cross-references Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/up-Q3E798.raw SHA256 ec7a45ad13c2710c794dee0db6e46e69b78d80d519f0370b84e9ee1616303772; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/up-Q3E798.receipt.json SHA256 0701161da36aed997229b82c2e6ee7fbc4b284527584888e13650f5d9033c983. | supports | Reviewed Q3E798 identifies MIM2 in reference strain S288C taxon559292. Species examples and class membership are distinct; annotation papers not otherwise listed are not certified read. |
| plaque-up-P39731 | https://rest.uniprot.org/uniprotkb/P39731.json; Full native identity/status/primary gene/taxon, FUNCTION, SUBUNIT and SUBCELLULAR LOCATION comments and InterPro cross-references Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/up-P39731.raw SHA256 0c3844f9cc37b32b6f30e038acc0c3895d2549aa18703aaa3a846fc445eaf6a3; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/up-P39731.receipt.json SHA256 b37d7d5db2bd1e35fbf0deedc5c7c0b22120892041c303841c0caeef42a6a79a. | supports | Reviewed P39731 identifies MTW1 in reference strain S288C taxon559292. Species examples and class membership are distinct; annotation papers not otherwise listed are not certified read. |
| plaque-up-P40568 | https://rest.uniprot.org/uniprotkb/P40568.json; Full native identity/status/primary gene/taxon, FUNCTION, SUBUNIT and SUBCELLULAR LOCATION comments and InterPro cross-references Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/up-P40568.raw SHA256 8ee197059c0d47c233e91caecae5be56ebdba607af0fc0bce1159519d084281d; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/up-P40568.receipt.json SHA256 4310f5b04a4c9cba9a3a7c0b747ad2de5140e3b0eb6bcd60b250bf2b816626c0. | supports | Reviewed P40568 identifies DSN1 in reference strain S288C taxon559292. Species examples and class membership are distinct; annotation papers not otherwise listed are not certified read. |
| plaque-up-Q12143 | https://rest.uniprot.org/uniprotkb/Q12143.json; Full native identity/status/primary gene/taxon, FUNCTION, SUBUNIT and SUBCELLULAR LOCATION comments and InterPro cross-references Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/up-Q12143.raw SHA256 ad535ce87e143bd05cd8ee7be4206f30339e2eb5423010eaa7e87f1e06a682a0; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/up-Q12143.receipt.json SHA256 f11bf0bb5387902fc04c0acfc5f97363e5055d34b0bd2c03157df5a65334eb89. | supports | Reviewed Q12143 identifies NSL1 in reference strain S288C taxon559292. Species examples and class membership are distinct; annotation papers not otherwise listed are not certified read. |
| plaque-up-P47149-retry | https://rest.uniprot.org/uniprotkb/P47149.json?format=json; Full native identity/status/primary gene/taxon, FUNCTION, SUBUNIT and SUBCELLULAR LOCATION comments and InterPro cross-references Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/up-P47149-retry.raw SHA256 6b3ba871504fdb8a5759cf7d1d7c99175cde494559e6571876239b629e3c4218; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/up-P47149-retry.receipt.json SHA256 4d3a35849b85838b22f4dfc3baaefad8f85630dc2bffa79f3ab96dd3388cb657. | supports | Reviewed P47149 identifies NNF1 in reference strain S288C taxon559292. Species examples and class membership are distinct; annotation papers not otherwise listed are not certified read. |
| plaque-up-P40460 | https://rest.uniprot.org/uniprotkb/P40460.json; Full native identity/status/primary gene/taxon, FUNCTION, SUBUNIT and SUBCELLULAR LOCATION comments and InterPro cross-references Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/up-P40460.raw SHA256 bb7b0fa4786334b7a92ecefb6915feaaaaa05d231552da89d9f38a459c981051; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/up-P40460.receipt.json SHA256 7d93d993e7197310f3c9e981e0f3e8c8222fddbc65df593f30016491cd30f180. | supports | Reviewed P40460 identifies NDC80 in reference strain S288C taxon559292. Species examples and class membership are distinct; annotation papers not otherwise listed are not certified read. |
| plaque-up-P33895 | https://rest.uniprot.org/uniprotkb/P33895.json; Full native identity/status/primary gene/taxon, FUNCTION, SUBUNIT and SUBCELLULAR LOCATION comments and InterPro cross-references Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/up-P33895.raw SHA256 2a0630d209109e36f7ee437e3298f75916c46b69683101f55276f4a0394eee58; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/up-P33895.receipt.json SHA256 ab6ebabc1762bbaed0c0d527d3fc5695eb1d7e06ed1484b8690921f49fdcb710. | supports | Reviewed P33895 identifies NUF2 in reference strain S288C taxon559292. Species examples and class membership are distinct; annotation papers not otherwise listed are not certified read. |
| plaque-up-Q04477-retry | https://rest.uniprot.org/uniprotkb/Q04477.json?format=json; Full native identity/status/primary gene/taxon, FUNCTION, SUBUNIT and SUBCELLULAR LOCATION comments and InterPro cross-references Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/up-Q04477-retry.raw SHA256 d87de5336ad58ff4d2a8616f6382c52938c1188c3bb3ec1222bf986bd86e983b; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/up-Q04477-retry.receipt.json SHA256 c8e5cf590c5afdbcc19b2d7af88fcf11c096e5d7f5bc2cac8b6cf7fa012dac0b. | supports | Reviewed Q04477 identifies SPC24 in reference strain S288C taxon559292. Species examples and class membership are distinct; annotation papers not otherwise listed are not certified read. |
| plaque-tax-4932 | https://rest.uniprot.org/taxonomy/4932.json; Complete taxId/name/rank/lineage/synonyms Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/tax-4932.raw SHA256 1a6c0b4fc804f45969573b7d0cec1e375ac361a2aae51313e7bb76ecfbff3c0b; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/tax-4932.receipt.json SHA256 6f2154ab908290b13fb7c80fbbb45f99d346296e9a6793c54f14b0d7baa4e63f. | supports | Taxon 4932 distinguishes S. cerevisiae species from S288C reference strain; experimental cultures are separately scoped. |
| plaque-tax-559292 | https://rest.uniprot.org/taxonomy/559292.json; Complete taxId/name/rank/lineage/synonyms Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/tax-559292.raw SHA256 9ebcfe8a317cc0c25c329a3a6a7cc9eaa863bb2dfebe5eaff9a34628c6684810; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/tax-559292.receipt.json SHA256 df32e80b9136f473fde4889b6454c38f11e84dd545a4d886f98de415e5824be1. | supports | Taxon 559292 distinguishes S. cerevisiae species from S288C reference strain; experimental cultures are separately scoped. |
| plaque-doan2020-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1016%2Fj.celrep.2020.107567&amp;format=json&amp;resultType=core&amp;pageSize=5; Unique MED identity, bibliographic fields and complete abstractText; not a full-body claim Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/doan2020-metadata.raw SHA256 58c00ab0347acee7cb726ad95e5452768238dae6354752943ea8758a7d300807; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/doan2020-metadata.receipt.json SHA256 7a7b500437b696543ad076dd81fc38ce85d05ed3b968812611ec6deb9c3ab8c6. | supports | PMID32348752: The Mitochondrial Import Complex MIM Functions as Main Translocase for α-Helical Outer Membrane Proteins. (2020); DOI 10.1016/j.celrep.2020.107567. Primary abstract scope only, except Gakh2002 which is a secondary review abstract. |
| plaque-vitali2018-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.7554%2FeLife.34488&amp;format=json&amp;resultType=core&amp;pageSize=5; Unique MED identity, bibliographic fields and complete abstractText; not a full-body claim Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/vitali2018-metadata.raw SHA256 e45eff19aa5454f5d77466c27b88e72f2e43fc793418408a9010a786613471a0; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/vitali2018-metadata.receipt.json SHA256 1fcbb5f9f5902ba08134ce048202549efb222f16f2e6547422c64d66ffa2a131. | supports | PMID29923829: Independent evolution of functionally exchangeable mitochondrial outer membrane import complexes. (2018); DOI 10.7554/elife.34488. Primary abstract scope only, except Gakh2002 which is a secondary review abstract. |
| plaque-vitali2019-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1016%2Fj.isci.2019.100779&amp;format=json&amp;resultType=core&amp;pageSize=5; Unique MED identity, bibliographic fields and complete abstractText; not a full-body claim Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/vitali2019-metadata.raw SHA256 7d2b257afeda15507c45354b89e048fb023835c042cec3a9384cc6caf114e40e; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/vitali2019-metadata.receipt.json SHA256 ec55c5ac875716b8cb1a11f185e422e3978e82f9dc23d1dd93ac2bc3ce640bb5. | supports | PMID31945731: The Biogenesis of Mitochondrial Outer Membrane Proteins Show Variable Dependence on Import Factors. (2020); DOI 10.1016/j.isci.2019.100779. Primary abstract scope only, except Gakh2002 which is a secondary review abstract. |
| plaque-dewulf2003-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1101%2Fgad.1144403&amp;format=json&amp;resultType=core&amp;pageSize=5; Unique MED identity, bibliographic fields and complete abstractText; not a full-body claim Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/dewulf2003-metadata.raw SHA256 6aa87e0293d064b13af37abee34e2a713615583020e5c99e20f8dff64da6b4cf; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/dewulf2003-metadata.receipt.json SHA256 b1754169c2c9d119b3fd9399702054732514807ec1ad4e14bd11f3841b46af47. | supports | PMID14633972: Hierarchical assembly of the budding yeast kinetochore from multiple subcomplexes. (2003); DOI 10.1101/gad.1144403. Primary abstract scope only, except Gakh2002 which is a secondary review abstract. |
| plaque-kline2006-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1083%2Fjcb.200509158&amp;format=json&amp;resultType=core&amp;pageSize=5; Unique MED identity, bibliographic fields and complete abstractText; not a full-body claim Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/kline2006-metadata.raw SHA256 f2c34edce1781cfc8fd07061c9c5bf0e10c1f30160c31685bf3fa75cd90bd1f1; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/kline2006-metadata.receipt.json SHA256 1e9e3db6f2995a33322a6f72cfe5c20523d9a74dfcdb82da5d86de63850e9caa. | supports | PMID16585270: The human Mis12 complex is required for kinetochore assembly and proper chromosome segregation. (2006); DOI 10.1083/jcb.200509158. Primary abstract scope only, except Gakh2002 which is a secondary review abstract. |
| plaque-jan2000-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1007%2Fs004380051192&amp;format=json&amp;resultType=core&amp;pageSize=5; Unique MED identity, bibliographic fields and complete abstractText; not a full-body claim Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/jan2000-metadata.raw SHA256 50383e9108694c2b34d9b81299971ffc07cfffb33604c8ec9770b35e88a1c37a; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/jan2000-metadata.receipt.json SHA256 c15434fd03939170b5925e582b33bc6488299914613c1b4f6e8ecfcda285af87. | supports | PMID10821182: Som1, a third component of the yeast mitochondrial inner membrane peptidase complex that contains Imp1 and Imp2. (2000); DOI 10.1007/s004380051192. Primary abstract scope only, except Gakh2002 which is a secondary review abstract. |
| plaque-gakh2002-pmid | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12191769%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=5; Unique MED identity, bibliographic fields and complete abstractText; not a full-body claim Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/gakh2002-pmid.raw SHA256 9cc68c5f2927320631d6b96479e0d617c2f9580dfaf4d2b3bb6eb6a9ad9bfcb4; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/gakh2002-pmid.receipt.json SHA256 d4502cb5be7e453b29189d345ff88a329ae87167b15bbc74f809733f6f6933d0. | supports | PMID12191769: Mitochondrial processing peptidases. (2002); DOI 10.1016/s0167-4889(02)00265-3. Primary abstract scope only, except Gakh2002 which is a secondary review abstract. |
| plaque-pmid-15326197 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15326197+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=5; Unique MED identity, bibliographic fields and complete abstractText; not a full-body claim Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/pmid-15326197.raw SHA256 9d6a470beaa641f625abb34a43ae2575d313100ead1a1a0b77f74ed5b5f529d7; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/pmid-15326197.receipt.json SHA256 652b182e7e171942e685d959dcc3e3790e64e2061d14c43f00daf2bc6fdd179d. | supports | PMID15326197: Two novel proteins in the mitochondrial outer membrane mediate beta-barrel protein assembly. (2004); DOI 10.1083/jcb.200405138. Primary abstract scope only, except Gakh2002 which is a secondary review abstract. |
| plaque-pmid-15608614 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15608614+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=5; Unique MED identity, bibliographic fields and complete abstractText; not a full-body claim Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/pmid-15608614.raw SHA256 efdb387426e5ea4a442048f2d57a1f779a340490a5a175f254c07d185a58d805; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/pmid-15608614.receipt.json SHA256 68f8ab61f68c04416f63ae71b10edae7d708b9095be139d740c1874efc3566bf. | supports | PMID15608614: Mim1, a protein required for the assembly of the TOM complex of mitochondria. (2005); DOI 10.1038/sj.embor.7400318. Primary abstract scope only, except Gakh2002 which is a secondary review abstract. |
| plaque-pmid-22467864 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A22467864+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=5; Unique MED identity, bibliographic fields and complete abstractText; not a full-body claim Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/pmid-22467864.raw SHA256 eca00c33ab3d6608b727bc5cf4147da7f23bd76fbc7e6c0119c5bd0c9cce44f9; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/pmid-22467864.receipt.json SHA256 6a17998c80b07f5e8bd9bf093fdf167a67f0caf23ee86a3cbd505be94aea45dd. | supports | PMID22467864: A crucial role for Mim2 in the biogenesis of mitochondrial outer membrane proteins. (2012); DOI 10.1242/jcs.103804. Primary abstract scope only, except Gakh2002 which is a secondary review abstract. |
| plaque-pmid-12455957 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12455957+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=5; Unique MED identity, bibliographic fields and complete abstractText; not a full-body claim Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/pmid-12455957.raw SHA256 e189e398c1778f6ff1d60c589aed6705fddfc847facd4df7eb9199871f9b1681; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/pmid-12455957.receipt.json SHA256 510ae39a0a69b7655d875ce0857c3eaea15266e2a085a09c04dba90e97436b9e. | supports | PMID12455957: Nnf1p, Dsn1p, Mtw1p, and Nsl1p: a new group of proteins important for chromosome segregation in Saccharomyces cerevisiae. (2002); DOI 10.1128/ec.1.2.229-240.2002. Primary abstract scope only, except Gakh2002 which is a secondary review abstract. |
| plaque-pmid-14602074 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14602074+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=5; Unique MED identity, bibliographic fields and complete abstractText; not a full-body claim Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/pmid-14602074.raw SHA256 d1e73dc06e71e15cdb6cb51be8ec8320ed74adcd91395ea60acaa4951185a96f; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/pmid-14602074.receipt.json SHA256 7373a8b6bef88c33b8cc2c043b28dfe7253aea78c46c85406bb85f32b913f2c5. | supports | PMID14602074: An Mtw1 complex promotes kinetochore biorientation that is monitored by the Ipl1/Aurora protein kinase. (2003); DOI 10.1016/s1534-5807(03)00322-8. Primary abstract scope only, except Gakh2002 which is a secondary review abstract. |
| plaque-pmid-14657030 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14657030+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=5; Unique MED identity, bibliographic fields and complete abstractText; not a full-body claim Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/pmid-14657030.raw SHA256 a0765ceea39156739ed26d1326de1f92f6bffd5186c85f31757a5c3b55080ac1; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/pmid-14657030.receipt.json SHA256 654b643933c99aaa11530f9833cf2121c6be98dbd031bafdddcca88bc8f55cf5. | supports | PMID14657030: Nsl1p is essential for the establishment of bipolarity and the localization of the Dam-Duo complex. (2003); DOI 10.1093/emboj/cdg636. Primary abstract scope only, except Gakh2002 which is a secondary review abstract. |
| plaque-gene-MTW1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AMTW1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned reviewed gene_exact MTW1 organism559292 identities Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/gene-MTW1.raw SHA256 5e9157a45fe17da2b2ab661323a2729aa82b93b050fd8fd46303046151fb1e7a; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/gene-MTW1.receipt.json SHA256 e1f34c4199f98589f41f344a5f219761650628fdc4dc7456c9d52994e1982cec. | supports | Only P39731 returned in this bounded current query. Other current gene-query transport failures do not support uniqueness claims. |
| plaque-gene-MIM1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AMIM1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Actual response/transport receipt only Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/gene-MIM1.raw SHA256 7a85c8e2aeaafe9d1dff1cc7777a70a62f620ca35b59b506ef7cddfabcd2014d; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/gene-MIM1.receipt.json SHA256 dac51121133576157760353ae0bd3d1f7754146025e65fbde95cbb0ba400e4ad. | context_only | Current route status 503; HTTP Error 503: Backend fetch failed. No successful body or negative scientific conclusion derived. Successful retries/abstracts/indexed excerpts are separately scoped. |
| plaque-gene-MIM2 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AMIM2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Actual response/transport receipt only Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/gene-MIM2.raw SHA256 339bdc071ebd0b2630ef50fd516a2af944df77e599d7cd4e4403046ea8ff0dc9; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/gene-MIM2.receipt.json SHA256 7ce7671e7b45251b6c501417f8ce7f0e06c01cf798a0791f46ab8da77a10ccde. | context_only | Current route status 503; HTTP Error 503: Backend fetch failed. No successful body or negative scientific conclusion derived. Successful retries/abstracts/indexed excerpts are separately scoped. |
| plaque-gene-DSN1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ADSN1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Actual response/transport receipt only Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/gene-DSN1.raw SHA256 150a09ca9f45bb4acb35b8da51af1701469b28844ece5ccb2d5a34a39ebf4096; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/gene-DSN1.receipt.json SHA256 13e728ca022cb9d11893e311ecf0fa9c81e944b5d1d5e68dec81a5c0d15fc37b. | context_only | Current route status 503; HTTP Error 503: Backend fetch failed. No successful body or negative scientific conclusion derived. Successful retries/abstracts/indexed excerpts are separately scoped. |
| plaque-gene-NSL1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ANSL1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Actual response/transport receipt only Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/gene-NSL1.raw SHA256 36cee505381f1e02bc919356a1352f71a7ec886d98883b5232ac0a3411b330f5; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/gene-NSL1.receipt.json SHA256 fe4119b264b1739aba0feac9b151489cff387d7a2e1b92b444c06414aee3ba4d. | context_only | Current route status 503; HTTP Error 503: Backend fetch failed. No successful body or negative scientific conclusion derived. Successful retries/abstracts/indexed excerpts are separately scoped. |
| plaque-gene-NNF1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ANNF1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Actual response/transport receipt only Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/gene-NNF1.raw SHA256 77272e5b973d90476a4037e7e8875088a93089cd07d89fbac04f5f85b9084c32; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/gene-NNF1.receipt.json SHA256 1162430073d33f212a7b2946a98e842638a6235ad33c2d289fee58aff8dab22b. | context_only | Current route status 503; HTTP Error 503: Backend fetch failed. No successful body or negative scientific conclusion derived. Successful retries/abstracts/indexed excerpts are separately scoped. |
| plaque-up-Q08176 | https://rest.uniprot.org/uniprotkb/Q08176.json; Actual response/transport receipt only Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/up-Q08176.raw SHA256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/up-Q08176.receipt.json SHA256 0ce2c55244ca36cf0740b9e58c03af36919bcf6cd9d586110b01de89bf21f6ea. | context_only | Current route status 0; The read operation timed out. No successful body or negative scientific conclusion derived. Successful retries/abstracts/indexed excerpts are separately scoped. |
| plaque-up-P47149 | https://rest.uniprot.org/uniprotkb/P47149.json; Actual response/transport receipt only Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/up-P47149.raw SHA256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/up-P47149.receipt.json SHA256 bf4fbf35890119d8face8cfdbaf1e202edaedb3a7917735fea63527761d3af79. | context_only | Current route status 0; The read operation timed out. No successful body or negative scientific conclusion derived. Successful retries/abstracts/indexed excerpts are separately scoped. |
| plaque-up-Q04477 | https://rest.uniprot.org/uniprotkb/Q04477.json; Actual response/transport receipt only Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/up-Q04477.raw SHA256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/up-Q04477.receipt.json SHA256 8b9acf0c922a3b256f51468d25e4133f05556cff4fd5ceb2c52f75a6b719e289. | context_only | Current route status 0; The read operation timed out. No successful body or negative scientific conclusion derived. Successful retries/abstracts/indexed excerpts are separately scoped. |
| plaque-doan2020-freidok | https://freidok.uni-freiburg.de/files/165604/PIIS2211124720305167.pdf; Actual response/transport receipt only Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/doan2020-freidok.raw SHA256 54403a34b81a851f50e1a2f57298aebc30b408d952317020dbe43ac59fc732eb; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/doan2020-freidok.receipt.json SHA256 174131330b79b8aafd8c32f82001582f4861f596383d4f9d5c7884dff5db862e. | context_only | Current route status 404; HTTP Error 404: Not Found. No successful body or negative scientific conclusion derived. Successful retries/abstracts/indexed excerpts are separately scoped. |
| plaque-doan2020-storage | https://storage.freidok.ub.uni-freiburg.de/publications/165604/ieaccMPhkWq1nfS5/PIIS2211124720305167.pdf; Actual response/transport receipt only Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/doan2020-storage.raw SHA256 0586debc1a74fa198c100b14dfbc0629cbd2a9d71150b021a8f0f262ea3c9354; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/doan2020-storage.receipt.json SHA256 46583c06da71099dc31eed2572c63bde784224a3c3a87e3a22a254f9aeb26e6e. | context_only | Current route status 403; HTTP Error 403: Forbidden. No successful body or negative scientific conclusion derived. Successful retries/abstracts/indexed excerpts are separately scoped. |
| plaque-doan2020-cell | https://www.cell.com/cell-reports/pdf/S2211-1247(20)30516-7.pdf; Actual response/transport receipt only Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/doan2020-cell.raw SHA256 e324f28d6c62553784fede6337ac7a4a3daaac914fee1eccf4741bdc776e56d4; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/doan2020-cell.receipt.json SHA256 48f920e85a4818bd1b5ad2fa879291c77c7a0ac1b846af65989a6149b015cbb2. | context_only | Current route status 403; HTTP Error 403: Forbidden. No successful body or negative scientific conclusion derived. Successful retries/abstracts/indexed excerpts are separately scoped. |
| plaque-doan2020-rg | https://www.researchgate.net/publication/340985619_The_Mitochondrial_Import_Complex_MIM_Functions_as_Main_Translocase_for_a-Helical_Outer_Membrane_Proteins; Actual response/transport receipt only Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/doan2020-rg.raw SHA256 f2fd10a5da17a30301197e56a4488fc6d72246a2e7fd2a404af1201ae1de8058; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/doan2020-rg.receipt.json SHA256 778f2862a8119bafdb6eec47492e654e1146c7644de86b8fa3babccbb1e923d8. | context_only | Current route status 403; HTTP Error 403: Forbidden. No successful body or negative scientific conclusion derived. Successful retries/abstracts/indexed excerpts are separately scoped. |
| plaque-jan2000-publisher | https://link.springer.com/article/10.1007/s004380051192; Actual response/transport receipt only Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/jan2000-publisher.raw SHA256 861d40bd2fd962728560720c26365ce8ba5d7530462bc73d123e3374eeec53c3; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/jan2000-publisher.receipt.json SHA256 1dae59da5cc198450b41ffeea740b67231cc49233deabce41fd09fa11fa550b2. | context_only | Current route status 200; None. No successful body or negative scientific conclusion derived. Successful retries/abstracts/indexed excerpts are separately scoped. |
| plaque-dewulf2003-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC289150.1/PMC289150.1.xml; Actual response/transport receipt only Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/dewulf2003-jats.raw SHA256 28d8b32688722232ca9d1168cb41a11b3f74d8cef50d0b2cfc0bc4250e894261; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/dewulf2003-jats.receipt.json SHA256 8b662ff6712002385e0a404da5513a45c08ab1c7a26addafee10768d8ee8212f. | context_only | Current route status 404; HTTP Error 404: Not Found. No successful body or negative scientific conclusion derived. Successful retries/abstracts/indexed excerpts are separately scoped. |
| plaque-gakh2002-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1016%2Fs0167-4889%2802%2900265-3&amp;format=json&amp;resultType=core&amp;pageSize=5; Exact DOI query returned zero results Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/gakh2002-metadata.raw SHA256 5a2ef4b85b2dcb59a9277d9a2b162de6491a1bf366b8e1c15b2b62f8b194218a; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/gakh2002-metadata.receipt.json SHA256 e0db96a69f95f9f72764d7c5330d446021ac8d2e77009fc027ed284f81b65092. | context_only | This spelling/query produced no match; PMID12191769 separately succeeds. No claim that the citation or review is absent. |
| plaque-PMC6010339-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC6010339.1/PMC6010339.1.xml; Genuine JATS Introduction s1, Results s2-1 through s2-5, Discussion s3, Methods s4-1 and s4-4 through s4-7; embedded captions; front permissions. No separate supplements or non-Fig5 pixels. Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/PMC6010339-jats.raw SHA256 b3015693fe625623165bc43f68c28ecaf411a5927a5d5bd092ee9f8b48746f5c; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/PMC6010339-jats.receipt.json SHA256 1f1c31caa1bc03a0d6d916c343f219666ce0e3491af3eb2da7ef2e9dfe810675. | supports | Native MIM composition and reciprocal heterologous complementation are supported with substrate and host limits. Figure5 measures mitochondrial morphology rescue in W303 yeast, not direct MIM localization. pATOM36 remains an evolutionarily distinct trypanosome protein. |
| plaque-PMC6965732-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC6965732.1/PMC6965732.1.xml; Genuine JATS Results sec2.1/sec2.3/sec2.4 and Discussion sec3 including limitations, Fig1/2/4/7 text captions; no other Methods/supplements/pixels Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/PMC6965732-jats.raw SHA256 f6bd13aad6474886ce6b05e1865979c0b31b7433d66486451676b59b12c29447; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/PMC6965732-jats.receipt.json SHA256 c6890e8f5b571a52ddde75a0c77a4c73f958f88b9c6d7409e19daecbaaf255ca. | supports | Steady-state/localization assays distinguish strong Msp1, moderate Gem1 and largely independent Fis1/Mcr1 behavior. This does not refute context-specific in-vitro import dependence; indirect effects and alternate paths remain explicit. |
| plaque-kline2006-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC2063780.1/PMC2063780.1.xml; Genuine JATS Introduction, Results subsections and Fig1-5 captions, protein expression/chromatography and IF Methods; no figure pixels, movies or independent supplementary data Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/kline2006-jats.raw SHA256 c31e71239af3e5dbd54160b0c4567cf64f5f0f08e186b2b10c170f741400b28f; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/kline2006-jats.receipt.json SHA256 a7414a442932858714388cdc2818f9be0df730d6d76fd06481da7afd99bcf1c7. | supports | Four human proteins were coexpressed in E. coli and copurified as a stable complex. Endogenous HeLa fractionation and human/chicken depletion/localization experiments are distinct. This genuinely supports the new reconstituted-human-complex note, without treating E. coli as a native MIS12 host. |
| plaque-dewulf2003-legacy | https://pmc.ncbi.nlm.nih.gov/articles/PMC289150/; Genuine HTML abstract/Introduction and focused Mtw1 Results paragraphs extracted at text lines1481-1510, selected Discussion1542/1547/1549 and Methods1559; no pixels or supplements Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/dewulf2003-legacy.raw SHA256 6d37dc17fba5e8d452776b6fec67ac84fb6e0fcdb9056a51019e7f27a61be122; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/dewulf2003-legacy.receipt.json SHA256 a771b3b7bd7f503f84517923914aa0b66aaf4df46bc39888d8854ab639fb1d5d. | supports | Yeast Mtw1/Nnf1/Nsl1/Dsn1 association, heterogeneous hydrodynamic species and conditional partner stability/CEN localization support bounded membership. The studied MIND, COMA and Ndc80 CEN-association independence prevents a universal yeast recruitment-dependency inference. |
| plaque-doan2020-web-indexed | https://doi.org/10.1016/j.celrep.2020.107567; Returned indexed official Freiburg PDF introduction/composition and selected initial Results only; indexed crawl predates review, current local reinspection time retained; no terminal HTTP200 PDF or pixel claim Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/doan2020-web-indexed.json SHA256 c46c65a969788b17ab990aecb7c18952fb94183671312e99e2abbb66dde69372; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/doan2020-web-indexed.receipt.json SHA256 2f8ace48fa8289cbc7785418080e0bfb16e9c6d9d6114940b78726d8e8bfdd30. | partial | Bounded primary-paper text supports MIM import/partner populations with distinct experiments and background composition. Exchange is a proposed model; no single TOM-MIM-SAM supercomplex or universal copy-count assay is inferred. |
| plaque-doan2020-web-sections | https://doi.org/10.1016/j.celrep.2020.107567; Returned indexed official Freiburg PDF Results/excerpt lines113-177,194-209,234-346,347-422 and partial Discussion445-468, selected resource table830-878; indexed crawl predates review, current local reinspection time retained; no terminal HTTP200 PDF or pixel claim Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/doan2020-web-sections.json SHA256 11f57186e0c34cf14f07d6c915fdc805bd6882b42e426379ed402f21ff1408dd; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/doan2020-web-sections.receipt.json SHA256 a6e91dbb97ca71e868f9f6e0105e41d52f18ff7d30e0ac31d396787ce7b3313a. | partial | Bounded primary-paper text supports MIM import/partner populations with distinct experiments and background composition. Exchange is a proposed model; no single TOM-MIM-SAM supercomplex or universal copy-count assay is inferred. |
| plaque-doan2020-web-methods | https://doi.org/10.1016/j.celrep.2020.107567; Returned indexed official Freiburg PDF lines391-497,876-954,982-1040 including SAM/Tom6, Discussion, YPH499 backgrounds and selected import Methods; indexed crawl predates review, current local reinspection time retained; no terminal HTTP200 PDF or pixel claim Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/doan2020-web-methods.json SHA256 0ff99bc65a90b78ebc30318b871af09d8c1bdeda141f94831c20002695bb2275; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/doan2020-web-methods.receipt.json SHA256 76d46759288dc799826544d54b284f7c0dd48242b80e0adee0db4e56e669c4ff. | partial | Bounded primary-paper text supports MIM import/partner populations with distinct experiments and background composition. Exchange is a proposed model; no single TOM-MIM-SAM supercomplex or universal copy-count assay is inferred. |
| plaque-dimmer2012-web-search | https://pubmed.ncbi.nlm.nih.gov/22467864/; Only returned primary-paper indexed text; composition/association Results around Fig2, Discussion and W303/YPH499 Methods; no full PDF or pixels claimed Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/dimmer2012-web-search.json SHA256 c5022801dbb564d8e936a328d397950d2cd94da3413ce64972bf6d5e7497b7fc; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/dimmer2012-web-search.receipt.json SHA256 466ec24938ab463a41024c02971b9191e9ab36f9954010b22bee8b5e230d7ff8. | context_only | Mim2 affects Mim1 abundance/native assembly, while Mim1 overexpression can produce an oligomer without Mim2. Supports a contribution rather than universal absolute necessity. Copy-range inference remains qualified. |
| plaque-dimmer2012-web-indexed | https://doi.org/10.1242/jcs.103804; Only returned primary-paper indexed text; composition/association Results around Fig2, Discussion and W303/YPH499 Methods; no full PDF or pixels claimed Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/dimmer2012-web-indexed.json SHA256 3cadce26ae441356a143acc53574d195a2ae3ed7ae9ded4a4bd6a9004226153e; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/dimmer2012-web-indexed.receipt.json SHA256 523e2cca9b5790911ec29746e0e41db546dcb40a58b197dc615a42d052df3ac2. | partial | Mim2 affects Mim1 abundance/native assembly, while Mim1 overexpression can produce an oligomer without Mim2. Supports a contribution rather than universal absolute necessity. Copy-range inference remains qualified. |
| plaque-dimmer2012-web-sections | https://doi.org/10.1242/jcs.103804; Only returned primary-paper indexed text; composition/association Results around Fig2, Discussion and W303/YPH499 Methods; no full PDF or pixels claimed Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/dimmer2012-web-sections.json SHA256 727342004b66532532b585c47e359222c31bdf4aea3fcbd26b6e13fd602ee6ba; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/dimmer2012-web-sections.receipt.json SHA256 fb6e2f03b469b3e7c42e4e3509bfc1451d2b73dea1114c812586ab294bf8b086. | partial | Mim2 affects Mim1 abundance/native assembly, while Mim1 overexpression can produce an oligomer without Mim2. Supports a contribution rather than universal absolute necessity. Copy-range inference remains qualified. |
| plaque-mim-figure5 | https://pmc-oa-opendata.s3.amazonaws.com/PMC6010339.1/elife-34488-fig5.jpg; Actual retrieved Fig5 JPEG; every panel viewed independently; byte comparison with maintained image Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/mim-figure5.raw SHA256 cdfb8f43e86424b85aa88ac2baa741035d8f107d58fe3b26ad48d595017a5af1; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/mim-figure5.receipt.json SHA256 92438c7403fa751fb9530686f6e9c3ba1afea1f59cf132b1c1d83b03adefa616. | supports | Source JPEG and maintained image are byte-identical, SHA256 cdfb8f43e86424b85aa88ac2baa741035d8f107d58fe3b26ad48d595017a5af1; MD5 be1d9b473460fba31d802e0c3ea5a1bc. Mito-GFP/brightfield morphology and quantified rescue, not MIM molecular localization. W303 context, 5 micrometer scale and three experiments/at least100 cells each follow caption. |
| plaque-mim-package | https://pmc-oa-opendata.s3.amazonaws.com/?list-type=2&amp;prefix=PMC6010339.1/; Complete bounded object listing prefix PMC6010339.1, Fig5 object entry only used Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/mim-package.raw SHA256 340f03ca3f6ab6f9e5dec87a5d99328e7b3b39bac9099fdca581d0fc3be55de1; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/mim-package.receipt.json SHA256 95fbb06b3abff1ae3032eb76c243d1260a0b927b5d5cbcbbc24bc41562973739. | supports | Package Fig5 ETag/size agree with downloaded JPEG. Rights come from genuine article CC BY4.0 permissions, not an inferred listing license. |
| plaque-maintained-image | data/images/other/mim_complex/pmc6010339_fig5.jpg; Actual maintained pixels and image metadata; compared to primary Figure5/caption/permissions | supports | Displayed image matches source bytewise; author credit and CC BY4.0 attribution are supported; no new image or derivative created. |
| plaque-adapter-catalogue | https://imodulondb.org/api/organisms; Complete official 20 organism rows and 28 organism-dataset entries independently reread Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/adapter-catalogue.raw SHA256 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/adapter-catalogue.receipt.json SHA256 2a10b30f380db880f8cad367d0403031d9cddd6478acdf8f16909187be175c0e. | context_only | No Saccharomyces, other fungal, human or chicken dataset occurs in this catalogue response. Positive MIM import, MIS12 assembly/recruitment and IMP proteolysis require applicability assessment, but no matched natural-host downstream query is justified. Heterologous bacterial expression is not an E. coli biological proxy. |
| plaque-mim-peer-challenge | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/mim-snippet-provenance-challenge.json; Separate independent bounded snippet comparison and source-tier challenge | supports | Independent reader corroborates the wording correction while preserving supported composition and no universal necessity reversal. |
| plaque-historical-t3-micro60-doan2020-freidok | https://freidok.uni-freiburg.de/files/165604/PIIS2211124720305167.pdf; Historical original row micro60-doan2020-freidok in reviews/structured/20261022T084807Z-mim-complex-audit/review.yaml. Actual final response title/body and transport metadata; unsuccessful body retrieval. | context_only | Historical observation, not a fresh fetch: This HTTP200 response is an institutional IT/security notice, not the cited paper body. Its bytes are excluded from scientific support; genuine bounded browser text is separately retained. |
| plaque-historical-t3-micro60-doan2020-storage | https://storage.freidok.ub.uni-freiburg.de/publications/165604/ieaccMPhkWq1nfS5/PIIS2211124720305167.pdf; Historical original row micro60-doan2020-storage in reviews/structured/20261022T084807Z-mim-complex-audit/review.yaml. Actual final response title/body and transport metadata; unsuccessful body retrieval. | context_only | Historical observation, not a fresh fetch: This HTTP200 response is an institutional IT/security notice, not the cited paper body. Its bytes are excluded from scientific support; genuine bounded browser text is separately retained. |
| plaque-historical-t5-micro60-jan2000-publisher | https://link.springer.com/article/10.1007/s004380051192; Historical original row micro60-jan2000-publisher in reviews/structured/20261022T084808Z-mitochondrial-inner-membrane-peptidase-complex-audit/review.yaml. Actual response content/transport and 3038-byte challenge payload. | context_only | Historical observation, not a fresh fetch: The retained HTTP200 response is a short client challenge, not the cited primary article body. Scientific support is limited to the independently retained complete MED abstract. |
| plaque-historical-t5-micro60-jan2000-pdf | https://link.springer.com/content/pdf/10.1007/s004380051192.pdf; Historical original row micro60-jan2000-pdf in reviews/structured/20261022T084808Z-mitochondrial-inner-membrane-peptidase-complex-audit/review.yaml. Actual response content/transport and 3038-byte challenge payload. | context_only | Historical observation, not a fresh fetch: The retained HTTP200 response is a short client challenge, not the cited primary article body. Scientific support is limited to the independently retained complete MED abstract. |
| plaque-historical-t5-micro60-gakh2002-publisher | https://doi.org/10.1016/s0167-4889(02)00265-3; Historical original row micro60-gakh2002-publisher in reviews/structured/20261022T084808Z-mitochondrial-inner-membrane-peptidase-complex-audit/review.yaml. Actual returned JSON type and metadata; no publisher full-text claim. | context_only | Historical observation, not a fresh fetch: The DOI route returned Crossref JSON bibliographic metadata, not the review body. The secondary review is assessed only at complete native abstract tier. |
| septin-review-policy | .claude/skills/review-yaml-record/SKILL.md; Applicable native review instructions | supports | Whole-record molecular and pathway assertions trigger structured-source coverage checks; a lack of expression inference is not an adequate exemption. |
| septin-curation-policy | docs/CURATION.md; Applicable native review instructions | supports | Structure identity, exact source scope, valid protein families/classes, unknown necessity and append-only historical discussion contract. |
| septin-protein-policy | .claude/skills/uniprot-protein-examples/SKILL.md; Applicable native review instructions | supports | Verify exact accession, primary gene/alias, taxon and current query scope; example identity is distinct from membership, activity and necessity. |
| septin-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Applicable native review instructions | supports | Preserve explicit formation versus function scope and distinguish structural membership from time-resolved assembly or loss-of-formation experiments. |
| septin-literature-policy | .claude/skills/literature-evidence/SKILL.md; Applicable native review instructions | supports | Read actual source content; distinguish metadata, abstract, body, image and failed access. No paraphrase may be represented as a verbatim snippet. |
| septin-record-mitochondrial_lon_protease_complex | data/structures/other/mitochondrial_lon_protease_complex.yaml; Complete current YAML, including discussions, quantities, components, evidence and graph | supports | All current assertions independently inspected. Current record hash equals the original frozen target hash; no stale refresh is required for this assigned target. |
| septin-original-mitochondrial_lon_protease_complex | reviews/structured/20261022T084809Z-mitochondrial-lon-protease-complex-audit/review.yaml; Complete immutable original review and exact target/finding/check/evidence scope | supports | Original verdict, all evidence rows, formal applicability exclusion, findings and actions read. Historical global check execution is attributed to its actual earlier batch, not misrepresented as a new execution. |
| septin-record-mitochondrial_multifunctional_assembly | data/structures/other/mitochondrial_multifunctional_assembly.yaml; Complete current YAML, including discussions, quantities, components, evidence and graph | supports | All current assertions independently inspected. Current record hash equals the original frozen target hash; no stale refresh is required for this assigned target. |
| septin-original-mitochondrial_multifunctional_assembly | reviews/structured/20261022T084810Z-mitochondrial-multifunctional-assembly-audit/review.yaml; Complete immutable original review and exact target/finding/check/evidence scope | supports | Original verdict, all evidence rows, formal applicability exclusion, findings and actions read. Historical global check execution is attributed to its actual earlier batch, not misrepresented as a new execution. |
| septin-record-mitochondrial_outer_membrane_translocase_complex | data/structures/other/mitochondrial_outer_membrane_translocase_complex.yaml; Complete current YAML, including discussions, quantities, components, evidence and graph | supports | All current assertions independently inspected. Current record hash equals the original frozen target hash; no stale refresh is required for this assigned target. |
| septin-original-mitochondrial_outer_membrane_translocase_complex | reviews/structured/20261022T084810Z-mitochondrial-outer-membrane-translocase-complex-audit/review.yaml; Complete immutable original review and exact target/finding/check/evidence scope | supports | Original verdict, all evidence rows, formal applicability exclusion, findings and actions read. Historical global check execution is attributed to its actual earlier batch, not misrepresented as a new execution. |
| septin-record-mitochondrial_prohibitin_complex | data/structures/other/mitochondrial_prohibitin_complex.yaml; Complete current YAML, including discussions, quantities, components, evidence and graph | supports | All current assertions independently inspected. Current record hash equals the original frozen target hash; no stale refresh is required for this assigned target. |
| septin-original-mitochondrial_prohibitin_complex | reviews/structured/20261022T084811Z-mitochondrial-prohibitin-complex-audit/review.yaml; Complete immutable original review and exact target/finding/check/evidence scope | supports | Original verdict, all evidence rows, formal applicability exclusion, findings and actions read. Historical global check execution is attributed to its actual earlier batch, not misrepresented as a new execution. |
| septin-original-native-checks | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/original-checks.json; Fresh guarded PR2397 four-pair validation/render and 53 historical input occurrences | supports | All four original envelopes validate and render exactly to their committed Markdown. All 51 current frozen inputs match worktree and source commit, and all 53 original historical input occurrences match their original commits. Uses only current PR2397 receipt bytes; no old PR2396 auxiliary receipt is a dependency. |
| septin-native-mitochondrial_lon_protease_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_lon_protease_complex-uniprot-verify-receipt.json; Actual command [".venv/bin/python", "scripts/uniprot_genes.py", "--record", "data/structures/other/mitochondrial_lon_protease_complex.yaml", "--verify"]; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_lon_protease_complex-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | 1 maintained protein-example occurrences; 1 typed GENE_OR_PROTEIN nodes. The one node is COVERED at the reference-correspondence level. Accession checks do not prove membership or necessity. Receipt SHA256 01465efc8a87c6aaa26e72f9a741208bbeb9d5d78932363d1c96a714165c5c94. |
| septin-native-mitochondrial_lon_protease_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_lon_protease_complex-uniprot-causal-receipt.json; Actual command [".venv/bin/python", "scripts/uniprot_genes.py", "--record", "data/structures/other/mitochondrial_lon_protease_complex.yaml", "--causal-graphs"]; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_lon_protease_complex-uniprot-causal.log SHA256 593a4556e111d3a1cfcf401fad0bc11ad1edf7df8b98ea85523db231d52f846b | supports | 1 maintained protein-example occurrences; 1 typed GENE_OR_PROTEIN nodes. The one node is COVERED at the reference-correspondence level. Accession checks do not prove membership or necessity. Receipt SHA256 f6c97cc1a9cc4e920e1c7060fcbae5c90761da82273502c42665daa936c88699. |
| septin-native-mitochondrial_multifunctional_assembly-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_multifunctional_assembly-uniprot-verify-receipt.json; Actual command [".venv/bin/python", "scripts/uniprot_genes.py", "--record", "data/structures/other/mitochondrial_multifunctional_assembly.yaml", "--verify"]; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_multifunctional_assembly-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | 5 maintained protein-example occurrences; 1 typed GENE_OR_PROTEIN nodes. The one node is COVERED at the reference-correspondence level. Accession checks do not prove membership or necessity. Receipt SHA256 94c00fb08c4a1ba0d01f6347201fdd495e613ff5c6abfb5af8bd1ee84bdeb303. |
| septin-native-mitochondrial_multifunctional_assembly-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_multifunctional_assembly-uniprot-causal-receipt.json; Actual command [".venv/bin/python", "scripts/uniprot_genes.py", "--record", "data/structures/other/mitochondrial_multifunctional_assembly.yaml", "--causal-graphs"]; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_multifunctional_assembly-uniprot-causal.log SHA256 2b1888389fba30f8794923be1fc9b5ba2c9bcaf92ef659ae0378f0c848a48d47 | supports | 5 maintained protein-example occurrences; 1 typed GENE_OR_PROTEIN nodes. The one node is COVERED at the reference-correspondence level. Accession checks do not prove membership or necessity. Receipt SHA256 67d79650ca9667aa2ad109fcf1ec135fb5940c2bcc93d523a1f8f7ad8c802347. |
| septin-native-mitochondrial_outer_membrane_translocase_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_outer_membrane_translocase_complex-uniprot-verify-receipt.json; Actual command [".venv/bin/python", "scripts/uniprot_genes.py", "--record", "data/structures/other/mitochondrial_outer_membrane_translocase_complex.yaml", "--verify"]; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_outer_membrane_translocase_complex-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | 0 maintained protein-example occurrences; 0 typed GENE_OR_PROTEIN nodes. The inventory and typed-node scope are empty; exit0 does not certify unrepresented molecular coverage. Accession checks do not prove membership or necessity. Receipt SHA256 72ee8e67c723c5a5ea530c67c701bc972ef5527094395b7b549b3e2cb60e43eb. |
| septin-native-mitochondrial_outer_membrane_translocase_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_outer_membrane_translocase_complex-uniprot-causal-receipt.json; Actual command [".venv/bin/python", "scripts/uniprot_genes.py", "--record", "data/structures/other/mitochondrial_outer_membrane_translocase_complex.yaml", "--causal-graphs"]; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_outer_membrane_translocase_complex-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | 0 maintained protein-example occurrences; 0 typed GENE_OR_PROTEIN nodes. The inventory and typed-node scope are empty; exit0 does not certify unrepresented molecular coverage. Accession checks do not prove membership or necessity. Receipt SHA256 1b2129f94baf96bed2f0c72c4f68c439c81f1063f02cf0a9af95ec6dda6018be. |
| septin-native-mitochondrial_prohibitin_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_prohibitin_complex-uniprot-verify-receipt.json; Actual command [".venv/bin/python", "scripts/uniprot_genes.py", "--record", "data/structures/other/mitochondrial_prohibitin_complex.yaml", "--verify"]; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_prohibitin_complex-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | 0 maintained protein-example occurrences; 0 typed GENE_OR_PROTEIN nodes. The inventory and typed-node scope are empty; exit0 does not certify unrepresented molecular coverage. Accession checks do not prove membership or necessity. Receipt SHA256 9bee8fa67f45ef4cf49f4685a60555891f81b8b65ca9762c8c14f1c1ca060500. |
| septin-native-mitochondrial_prohibitin_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_prohibitin_complex-uniprot-causal-receipt.json; Actual command [".venv/bin/python", "scripts/uniprot_genes.py", "--record", "data/structures/other/mitochondrial_prohibitin_complex.yaml", "--causal-graphs"]; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_prohibitin_complex-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | 0 maintained protein-example occurrences; 0 typed GENE_OR_PROTEIN nodes. The inventory and typed-node scope are empty; exit0 does not certify unrepresented molecular coverage. Accession checks do not prove membership or necessity. Receipt SHA256 c1701bcb77aa9ee93f3983ad3ad7058fd12eeb738a73a44250afa9d63f12ee6d. |
| septin-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0004176,GO:0005741,GO:0005742,GO:0005743,GO:0005759,GO:0007005,GO:0030150,GO:0035632,GO:0098799,GO:0098800,GO:1905368; Complete eleven-term native response: labels, definitions, synonym types and child relations; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/go.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/go.receipt.json | supports | GO:0005742 explicitly makes GIP complex a narrow synonym; other exact labels and anatomical/function scopes support the records. GO:0030150 covers the complete TOM-TIM23-PAM import route, while the TOM record limits its contribution to outer-membrane entry. GO:0035632 describes repeating PHB1/PHB2 heterodimers; GO:0007005 retains mitochondrial biogenesis as an exact synonym. |
| septin-go-0005742-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005742/ancestors?relations=is_a; Complete native is_a ancestor response; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/go-0005742-ancestors.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/go-0005742-ancestors.receipt.json | supports | Direct current parent and broader ancestry support the recorded mitochondrial outer/inner membrane protein-complex classifications; parthood is not inferred from is_a alone. |
| septin-go-0035632-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0035632/ancestors?relations=is_a; Complete native is_a ancestor response; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/go-0035632-ancestors.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/go-0035632-ancestors.receipt.json | supports | Direct current parent and broader ancestry support the recorded mitochondrial outer/inner membrane protein-complex classifications; parthood is not inferred from is_a alone. |
| septin-tax-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Native taxon identity and lineage; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/tax-4932.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/tax-4932.receipt.json | supports | Saccharomyces cerevisiae species, S288C reference strain, and Eukaryota are distinct scopes. Reference strain examples do not identify every experimental strain or establish universal prevalence. |
| septin-tax-559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Native taxon identity and lineage; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/tax-559292.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/tax-559292.receipt.json | supports | Saccharomyces cerevisiae species, S288C reference strain, and Eukaryota are distinct scopes. Reference strain examples do not identify every experimental strain or establish universal prevalence. |
| septin-tax-2759 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759; Native taxon identity and lineage; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/tax-2759.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/tax-2759.receipt.json | supports | Saccharomyces cerevisiae species, S288C reference strain, and Eukaryota are distinct scopes. Reference strain examples do not identify every experimental strain or establish universal prevalence. |
| septin-go-search-lon | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=Lon+protease&amp;limit=100; Actual returned QuickGO term-search page; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/go-search-lon.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/go-search-lon.receipt.json | context_only | Inspected 100 returned terms of 204 reported hits. No exact alternative structure identity was established within this bounded search; broad Lon/multifunctional requests were not exhaustive. The PIM1 response is an obsolete activity term, not an exact mitochondrial oligomer identity. |
| septin-go-search-pim1 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=Pim1&amp;limit=100; Actual returned QuickGO term-search page; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/go-search-pim1.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/go-search-pim1.receipt.json | context_only | Inspected 1 returned terms of 1 reported hits. No exact alternative structure identity was established within this bounded search; broad Lon/multifunctional requests were not exhaustive. The PIM1 response is an obsolete activity term, not an exact mitochondrial oligomer identity. |
| septin-go-search-mimas | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=MIMAS&amp;limit=100; Actual returned QuickGO term-search page; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/go-search-mimas.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/go-search-mimas.receipt.json | context_only | Inspected 0 returned terms of 0 reported hits. No exact alternative structure identity was established within this bounded search; broad Lon/multifunctional requests were not exhaustive. The PIM1 response is an obsolete activity term, not an exact mitochondrial oligomer identity. |
| septin-go-search-multifunctional | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=mitochondrial+multifunctional+assembly&amp;limit=100; Actual returned QuickGO term-search page; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/go-search-multifunctional.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/go-search-multifunctional.receipt.json | context_only | Inspected 100 returned terms of 1353 reported hits. No exact alternative structure identity was established within this bounded search; broad Lon/multifunctional requests were not exhaustive. The PIM1 response is an obsolete activity term, not an exact mitochondrial oligomer identity. |
| septin-ipr-IPR000163 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000163/; Native metadata, type, family name, signatures and description flags; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR000163.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR000163.receipt.json | supports | IPR000163 is type family, named Prohibitin. Native member-signature identifiers and family boundary inspected. Shared prohibitin family is not an exact PHB1-versus-PHB2 paralogue split. |
| septin-ipr-IPR000872 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000872/; Native metadata, type, family name, signatures and description flags; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR000872.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR000872.receipt.json | supports | IPR000872 is type family, named Tafazzin. Native member-signature identifiers and family boundary inspected. |
| septin-ipr-IPR002056 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002056/; Native metadata, type, family name, signatures and description flags; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR002056.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR002056.receipt.json | supports | IPR002056 is type family, named Protein import receptor MAS20. Native member-signature identifiers and family boundary inspected. |
| septin-ipr-IPR002113 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002113/; Native metadata, type, family name, signatures and description flags; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR002113.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR002113.receipt.json | supports | IPR002113 is type family, named ADP/ATP carrier protein, eukaryotic type. Native member-signature identifiers and family boundary inspected. |
| septin-ipr-IPR005683 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005683/; Native metadata, type, family name, signatures and description flags; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR005683.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR005683.receipt.json | supports | IPR005683 is type family, named Mitochondrial import receptor subunit Tom22. Native member-signature identifiers and family boundary inspected. |
| septin-ipr-IPR005686 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005686/; Native metadata, type, family name, signatures and description flags; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR005686.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR005686.receipt.json | supports | IPR005686 is type family, named Mitochondrial import receptor subunit Tom40, fungi. Native member-signature identifiers and family boundary inspected. |
| septin-ipr-IPR005687 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005687/; Native metadata, type, family name, signatures and description flags; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR005687.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR005687.receipt.json | supports | IPR005687 is type family, named Mitochondrial outer membrane translocase complex, subunit Tom70. Native member-signature identifiers and family boundary inspected. |
| septin-ipr-IPR012621 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR012621/; Native metadata, type, family name, signatures and description flags; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR012621.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR012621.receipt.json | supports | IPR012621 is type family, named Mitochondrial import receptor subunit TOM7. Native member-signature identifiers and family boundary inspected. |
| septin-ipr-IPR019603 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR019603/; Native metadata, type, family name, signatures and description flags; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR019603.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR019603.receipt.json | supports | IPR019603 is type family, named Mitochondrial outer membrane translocase complex, subunit Tom5. Native member-signature identifiers and family boundary inspected. |
| septin-ipr-IPR020266 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR020266/; Native metadata, type, family name, signatures and description flags; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR020266.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR020266.receipt.json | supports | IPR020266 is type family, named Mitochondrial import receptor subunit Tom6. Native member-signature identifiers and family boundary inspected. |
| septin-ipr-IPR020951 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR020951/; Native metadata, type, family name, signatures and description flags; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR020951.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR020951.receipt.json | supports | IPR020951 is type family, named Mitochondrial import receptor subunit Tom22, fungi. Native member-signature identifiers and family boundary inspected. |
| septin-ipr-IPR027503 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR027503/; Native metadata, type, family name, signatures and description flags; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR027503.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR027503.receipt.json | supports | IPR027503 is type family, named Lon protease homologue, chloroplastic/mitochondrial. Native member-signature identifiers and family boundary inspected. |
| septin-ipr-IPR033661 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR033661/; Native metadata, type, family name, signatures and description flags; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR033661.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR033661.receipt.json | supports | IPR033661 is type family, named Phosphatidylserine decarboxylase, eukaryotic type 1. Native member-signature identifiers and family boundary inspected. |
| septin-ipr-IPR037930 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR037930/; Native metadata, type, family name, signatures and description flags; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR037930.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR037930.receipt.json | supports | IPR037930 is type family, named Tom40. Native member-signature identifiers and family boundary inspected. |
| septin-ipr-IPR045024 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR045024/; Native metadata, type, family name, signatures and description flags; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR045024.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR045024.receipt.json | supports | IPR045024 is type family, named Alternative NADH dehydrogenase. Native member-signature identifiers and family boundary inspected. This broad alternative NADH-dehydrogenase family does not isolate the external Nde1 lineage from matrix-facing Ndi1 and bacterial members. |
| septin-ipr-IPR050355 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050355/; Native metadata, type, family name, signatures and description flags; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR050355.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR050355.receipt.json | supports | IPR050355 is type family, named Mitochondrial Respiratory Supercomplex Factor 1. Native member-signature identifiers and family boundary inspected. The description is flagged llm=true, checked=false and is not used as independent primary mechanistic evidence. |
| septin-protein-P18239 | https://rest.uniprot.org/uniprotkb/P18239.json; Complete native entry: identity, primary genes/aliases, taxon, family cross-references and source-qualified localization/subunit annotations; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/protein-P18239.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/protein-P18239.receipt.json | supports | P18239; UniProtKB reviewed (Swiss-Prot); taxon 559292; genes [{"geneName": {"value": "PET9"}, "synonyms": [{"value": "AAC2"}], "orderedLocusNames": [{"value": "YBL030C"}], "orfNames": [{"value": "YBL0421"}]}]. Localization annotation and primary-source membership are separately assessed; a family match does not establish formation necessity. |
| septin-protein-P36775 | https://rest.uniprot.org/uniprotkb/P36775.json; Complete native entry: identity, primary genes/aliases, taxon, family cross-references and source-qualified localization/subunit annotations; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/protein-P36775.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/protein-P36775.receipt.json | supports | P36775; UniProtKB reviewed (Swiss-Prot); taxon 559292; genes [{"geneName": {"evidences": [{"evidenceCode": "ECO:0000255", "source": "HAMAP-Rule", "id": "MF_03120"}], "value": "PIM1"}, "synonyms": [{"value": "LON"}], "orderedLocusNames": [{"value": "YBL022C"}], "orfNames": [{"value": "YBL0440"}]}]. Localization annotation and primary-source membership are separately assessed; a family match does not establish formation necessity. |
| septin-protein-P39006 | https://rest.uniprot.org/uniprotkb/P39006.json; Complete native entry: identity, primary genes/aliases, taxon, family cross-references and source-qualified localization/subunit annotations; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/protein-P39006.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/protein-P39006.receipt.json | supports | P39006; UniProtKB reviewed (Swiss-Prot); taxon 559292; genes [{"geneName": {"evidences": [{"evidenceCode": "ECO:0000255", "source": "HAMAP-Rule", "id": "MF_03208"}, {"evidenceCode": "ECO:0000303", "source": "PubMed", "id": "8227017"}], "value": "PSD1"}, "orderedLocusNames": [{"evidences": [{"evidenceCode": "ECO:0000312", "source": "SGD", "id": "S000005113"}], "value": "YNL169C"}], "orfNames": [{"value": "N1692"}]}]. Localization annotation and primary-source membership are separately assessed; a family match does not establish formation necessity. |
| septin-protein-P40215 | https://rest.uniprot.org/uniprotkb/P40215.json; Complete native entry: identity, primary genes/aliases, taxon, family cross-references and source-qualified localization/subunit annotations; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/protein-P40215.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/protein-P40215.receipt.json | supports | P40215; UniProtKB reviewed (Swiss-Prot); taxon 559292; genes [{"geneName": {"value": "NDE1"}, "synonyms": [{"value": "NDH1"}], "orderedLocusNames": [{"value": "YMR145C"}], "orfNames": [{"value": "YM9375.14C"}]}]. Localization annotation and primary-source membership are separately assessed; a family match does not establish formation necessity. |
| septin-protein-Q03713 | https://rest.uniprot.org/uniprotkb/Q03713.json; Complete native entry: identity, primary genes/aliases, taxon, family cross-references and source-qualified localization/subunit annotations; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/protein-Q03713.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/protein-Q03713.receipt.json | supports | Q03713; UniProtKB reviewed (Swiss-Prot); taxon 559292; genes [{"geneName": {"value": "RCF1"}, "synonyms": [{"value": "AIM31"}], "orderedLocusNames": [{"value": "YML030W"}]}]. Localization annotation and primary-source membership are separately assessed; a family match does not establish formation necessity. |
| septin-protein-Q06510 | https://rest.uniprot.org/uniprotkb/Q06510.json; Complete native entry: identity, primary genes/aliases, taxon, family cross-references and source-qualified localization/subunit annotations; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/protein-Q06510.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/protein-Q06510.receipt.json | supports | Q06510; UniProtKB reviewed (Swiss-Prot); taxon 559292; genes [{"geneName": {"value": "TAZ1"}, "orderedLocusNames": [{"evidences": [{"evidenceCode": "ECO:0000303", "source": "PubMed", "id": "15588229"}], "value": "YPR140W"}]}]. Localization annotation and primary-source membership are separately assessed; a family match does not establish formation necessity. |
| septin-gene-AAC2 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AAAC2+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=500; Complete returned reviewed S288C gene request; primary-name versus alias fields; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-AAC2.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-AAC2.receipt.json | context_only | Current returned identities [('P18239', 'PET9', 559292)]. Query scope is the explicit request, not a reconstruction of historical seeding. S288C is a reference context, not a substitute for source strain or an assembly assay. |
| septin-gene-NDE1 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ANDE1+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=500; Complete returned reviewed S288C gene request; primary-name versus alias fields; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-NDE1.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-NDE1.receipt.json | context_only | Current returned identities [('P40215', 'NDE1', 559292)]. Query scope is the explicit request, not a reconstruction of historical seeding. S288C is a reference context, not a substitute for source strain or an assembly assay. |
| septin-gene-PET9 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3APET9+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=500; Complete returned reviewed S288C gene request; primary-name versus alias fields; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-PET9.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-PET9.receipt.json | context_only | Current returned identities [('P18239', 'PET9', 559292)]. Query scope is the explicit request, not a reconstruction of historical seeding. S288C is a reference context, not a substitute for source strain or an assembly assay. |
| septin-gene-PHB1 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3APHB1+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=500; Complete returned reviewed S288C gene request; primary-name versus alias fields; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-PHB1.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-PHB1.receipt.json | context_only | Current returned identities [('P40961', 'PHB1', 559292)]. Query scope is the explicit request, not a reconstruction of historical seeding. S288C is a reference context, not a substitute for source strain or an assembly assay. |
| septin-gene-PHB2 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3APHB2+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=500; Complete returned reviewed S288C gene request; primary-name versus alias fields; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-PHB2.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-PHB2.receipt.json | context_only | Current returned identities [('P50085', 'PHB2', 559292)]. Query scope is the explicit request, not a reconstruction of historical seeding. S288C is a reference context, not a substitute for source strain or an assembly assay. |
| septin-gene-TOM22 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ATOM22+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=500; Complete returned reviewed S288C gene request; primary-name versus alias fields; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-TOM22.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-TOM22.receipt.json | context_only | Current returned identities [('P49334', 'TOM22', 559292)]. Query scope is the explicit request, not a reconstruction of historical seeding. S288C is a reference context, not a substitute for source strain or an assembly assay. |
| septin-gene-TOM40 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ATOM40+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=500; Complete returned reviewed S288C gene request; primary-name versus alias fields; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-TOM40.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-TOM40.receipt.json | context_only | Current returned identities [('P23644', 'TOM40', 559292)]. Query scope is the explicit request, not a reconstruction of historical seeding. S288C is a reference context, not a substitute for source strain or an assembly assay. |
| septin-gene-TOM6 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ATOM6+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=500; Complete returned reviewed S288C gene request; primary-name versus alias fields; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-TOM6.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-TOM6.receipt.json | context_only | Current returned identities [('P33448', 'TOM6', 559292)]. Query scope is the explicit request, not a reconstruction of historical seeding. S288C is a reference context, not a substitute for source strain or an assembly assay. |
| septin-gene-TOM7 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ATOM7+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=500; Complete returned reviewed S288C gene request; primary-name versus alias fields; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-TOM7.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-TOM7.receipt.json | context_only | Current returned identities [('P53507', 'TOM7', 559292)]. Query scope is the explicit request, not a reconstruction of historical seeding. S288C is a reference context, not a substitute for source strain or an assembly assay. |
| septin-gene-TOM70 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ATOM70+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=500; Complete returned reviewed S288C gene request; primary-name versus alias fields; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-TOM70.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-TOM70.receipt.json | context_only | Current returned identities [('P07213', 'TOM70', 559292)]. Query scope is the explicit request, not a reconstruction of historical seeding. S288C is a reference context, not a substitute for source strain or an assembly assay. |
| septin-query-retry-LON | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ALON%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned reviewed S288C gene request; primary-name versus alias fields; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/query-retry-LON.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/query-retry-LON.receipt.json | context_only | Current returned identities [('P36775', 'PIM1', 559292)]. Query scope is the explicit request, not a reconstruction of historical seeding. S288C is a reference context, not a substitute for source strain or an assembly assay. |
| septin-query-retry-PIM1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3APIM1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned reviewed S288C gene request; primary-name versus alias fields; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/query-retry-PIM1.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/query-retry-PIM1.receipt.json | context_only | Current returned identities [('P36775', 'PIM1', 559292)]. Query scope is the explicit request, not a reconstruction of historical seeding. S288C is a reference context, not a substitute for source strain or an assembly assay. |
| septin-query-retry-PSD1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3APSD1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned reviewed S288C gene request; primary-name versus alias fields; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/query-retry-PSD1.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/query-retry-PSD1.receipt.json | context_only | Current returned identities [('P39006', 'PSD1', 559292)]. Query scope is the explicit request, not a reconstruction of historical seeding. S288C is a reference context, not a substitute for source strain or an assembly assay. |
| septin-query-retry-RCF1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARCF1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned reviewed S288C gene request; primary-name versus alias fields; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/query-retry-RCF1.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/query-retry-RCF1.receipt.json | context_only | Current returned identities [('Q03713', 'RCF1', 559292)]. Query scope is the explicit request, not a reconstruction of historical seeding. S288C is a reference context, not a substitute for source strain or an assembly assay. |
| septin-query-retry-TAZ1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ATAZ1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned reviewed S288C gene request; primary-name versus alias fields; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/query-retry-TAZ1.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/query-retry-TAZ1.receipt.json | context_only | Current returned identities [('Q06510', 'TAZ1', 559292)]. Query scope is the explicit request, not a reconstruction of historical seeding. S288C is a reference context, not a substitute for source strain or an assembly assay. |
| septin-query-retry-TOM20 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ATOM20%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned reviewed S288C gene request; primary-name versus alias fields; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/query-retry-TOM20.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/query-retry-TOM20.receipt.json | context_only | Current returned identities [('P35180', 'TOM20', 559292)]. Query scope is the explicit request, not a reconstruction of historical seeding. S288C is a reference context, not a substitute for source strain or an assembly assay. |
| septin-query-retry-TOM5 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ATOM5%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned reviewed S288C gene request; primary-name versus alias fields; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/query-retry-TOM5.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/query-retry-TOM5.receipt.json | context_only | Current returned identities [('P80967', 'TOM5', 559292)]. Query scope is the explicit request, not a reconstruction of historical seeding. S288C is a reference context, not a substitute for source strain or an assembly assay. |
| septin-doi-10.1016_j.cell.2009.08.005 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.cell.2009.08.005%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Europe PMC native bibliographic record and complete available abstract; no paper body implied; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/doi-10.1016_j.cell.2009.08.005.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/doi-10.1016_j.cell.2009.08.005.receipt.json | context_only | Importing mitochondrial proteins: machineries and mechanisms. Authors: Chacinska A, Koehler CM, Milenkovic D, Lithgow T, Pfanner N.. DOI/PMID metadata reconciled. Metadata and abstract are not full-text methods or figure evidence. |
| septin-doi-10.1016_j.jbc.2022.101694 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.jbc.2022.101694%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Europe PMC native bibliographic record and complete available abstract; no paper body implied; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/doi-10.1016_j.jbc.2022.101694.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/doi-10.1016_j.jbc.2022.101694.receipt.json | context_only | Cryo-EM structure of hexameric yeast Lon protease (PIM1) highlights the importance of conserved structural elements. Authors: Yang J, Song AS, Wiseman RL, Lander GC.. DOI/PMID metadata reconciled. Metadata and abstract are not full-text methods or figure evidence. |
| septin-doi-10.1073_pnas.96.12.6787 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1073%2Fpnas.96.12.6787%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Europe PMC native bibliographic record and complete available abstract; no paper body implied; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/doi-10.1073_pnas.96.12.6787.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/doi-10.1073_pnas.96.12.6787.receipt.json | context_only | Mitochondrial Lon of Saccharomyces cerevisiae is a ring-shaped protease with seven flexible subunits. Authors: Stahlberg H, Kutejová E, Suda K, Wolpensinger B, Lustig A, Schatz G, Engel A, Suzuki CK.. DOI/PMID metadata reconciled. Metadata and abstract are not full-text methods or figure evidence. |
| septin-doi-10.1110_ps.0212602 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1110%2Fps.0212602%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Europe PMC native bibliographic record and complete available abstract; no paper body implied; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/doi-10.1110_ps.0212602.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/doi-10.1110_ps.0212602.receipt.json | context_only | A structure for the yeast prohibitin complex: Structure prediction and evidence from chemical crosslinking and mass spectrometry. Authors: Back JW, Sanz MA, De Jong L, De Koning LJ, Nijtmans LG, De Koster CG, Grivell LA, Van Der Spek H, Muijsers AO.. DOI/PMID metadata reconciled. Metadata and abstract are not full-text methods or figure evidence. |
| septin-doi-10.18632_aging.100246 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.18632%2Faging.100246%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Europe PMC native bibliographic record and complete available abstract; no paper body implied; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/doi-10.18632_aging.100246.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/doi-10.18632_aging.100246.receipt.json | context_only | Opposing function of mitochondrial prohibitin in aging. Authors: Artal-Sanz M, Tavernarakis N.. DOI/PMID metadata reconciled. Metadata and abstract are not full-text methods or figure evidence. |
| septin-pmid-14562095 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Europe PMC native bibliographic record and complete available abstract; no paper body implied; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pmid-14562095.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pmid-14562095.receipt.json | context_only | Global analysis of protein localization in budding yeast. Authors: Huh WK, Falvo JV, Gerke LC, Carroll AS, Howson RW, Weissman JS, O'Shea EK.. DOI/PMID metadata reconciled. Metadata and abstract are not full-text methods or figure evidence. |
| septin-pmid-14576278 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14576278+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Europe PMC native bibliographic record and complete available abstract; no paper body implied; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pmid-14576278.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pmid-14576278.receipt.json | context_only | The proteome of Saccharomyces cerevisiae mitochondria. Authors: Sickmann A, Reinders J, Wagner Y, Joppich C, Zahedi R, Meyer HE, Schönfisch B, Perschil I, Chacinska A, Guiard B, Rehling P, Pfanner N, Meisinger C.. DOI/PMID metadata reconciled. Metadata and abstract are not full-text methods or figure evidence. |
| septin-pmid-15588229 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15588229+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Europe PMC native bibliographic record and complete available abstract; no paper body implied; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pmid-15588229.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pmid-15588229.receipt.json | context_only | Ypr140wp, 'the yeast tafazzin', displays a mitochondrial lysophosphatidylcholine (lyso-PC) acyltransferase activity related to triacylglycerol and mitochondrial lipid synthesis. Authors: Testet E, Laroche-Traineau J, Noubhani A, Coulon D, Bunoust O, Camougrand N, Manon S, Lessire R, Bessoule JJ.. DOI/PMID metadata reconciled. Metadata and abstract are not full-text methods or figure evidence. |
| septin-pmid-16135531 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A16135531+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Europe PMC native bibliographic record and complete available abstract; no paper body implied; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pmid-16135531.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pmid-16135531.receipt.json | context_only | Taz1, an outer mitochondrial membrane protein, affects stability and assembly of inner membrane protein complexes: implications for Barth Syndrome. Authors: Brandner K, Mick DU, Frazier AE, Taylor RD, Meisinger C, Rehling P.. DOI/PMID metadata reconciled. Metadata and abstract are not full-text methods or figure evidence. |
| septin-pmid-16880272 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A16880272+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Europe PMC native bibliographic record and complete available abstract; no paper body implied; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pmid-16880272.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pmid-16880272.receipt.json | context_only | Mitochondrial mislocalization and altered assembly of a cluster of Barth syndrome mutant tafazzins. Authors: Claypool SM, McCaffery JM, Koehler CM.. DOI/PMID metadata reconciled. Metadata and abstract are not full-text methods or figure evidence. |
| septin-pmid-22984266 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A22984266+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Europe PMC native bibliographic record and complete available abstract; no paper body implied; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pmid-22984266.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pmid-22984266.receipt.json | context_only | Processing and topology of the yeast mitochondrial phosphatidylserine decarboxylase 1. Authors: Horvath SE, Böttinger L, Vögtle FN, Wiedemann N, Meisinger C, Becker T, Daum G.. DOI/PMID metadata reconciled. Metadata and abstract are not full-text methods or figure evidence. |
| septin-pmid-23124206 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A23124206+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Europe PMC native bibliographic record and complete available abstract; no paper body implied; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pmid-23124206.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pmid-23124206.receipt.json | context_only | Phosphatidylethanolamine biosynthesis in mitochondria: phosphatidylserine (PS) trafficking is independent of a PS decarboxylase and intermembrane space proteins UPS1P and UPS2P. Authors: Tamura Y, Onguka O, Itoh K, Endo T, Iijima M, Claypool SM, Sesaki H.. DOI/PMID metadata reconciled. Metadata and abstract are not full-text methods or figure evidence. |
| septin-pmid-35127709 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A35127709+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Europe PMC native bibliographic record and complete available abstract; no paper body implied; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pmid-35127709.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pmid-35127709.receipt.json | context_only | Peroxisomal ATP Uptake Is Provided by Two Adenine Nucleotide Transporters and the ABCD Transporters. Authors: van Roermund CWT, IJlst L, Linka N, Wanders RJA, Waterham HR.. DOI/PMID metadata reconciled. Metadata and abstract are not full-text methods or figure evidence. |
| septin-pmid-38393949 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A38393949+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Europe PMC native bibliographic record and complete available abstract; no paper body implied; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pmid-38393949.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pmid-38393949.receipt.json | context_only | Identification of MIMAS, a multifunctional mega-assembly integrating metabolic and respiratory biogenesis factors of mitochondria. Authors: Horten P, Song K, Garlich J, Hardt R, Colina-Tenorio L, Horvath SE, Schulte U, Fakler B, van der Laan M, Becker T, Stuart RA, Pfanner N, Rampelt H.. DOI/PMID metadata reconciled. Metadata and abstract are not full-text methods or figure evidence. |
| septin-pmid-42178653 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A42178653+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Europe PMC native bibliographic record and complete available abstract; no paper body implied; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pmid-42178653.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pmid-42178653.receipt.json | context_only | MICOS and MIMAS, multifunctional assemblies linking mitochondrial biogenesis, architecture, and function. Authors: Horten P, Song K, Pfanner N, Rampelt H.. DOI/PMID metadata reconciled. Metadata and abstract are not full-text methods or figure evidence. |
| septin-pmid-795470 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A795470+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Europe PMC native bibliographic record and complete available abstract; no paper body implied; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pmid-795470.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pmid-795470.receipt.json | context_only | Effect of genetic and physiological manipulations onthe kinetic and binding parameters of the adenine nucleotide translocator in Saccharomyces cervisiae and Candida utilis. Authors: Lauquin G, Lunardi J, Vignais PV.. DOI/PMID metadata reconciled. Metadata and abstract are not full-text methods or figure evidence. |
| septin-back2002-abstract | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1110%2Fps.0212602%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete Back et al. 2002 abstract, PMID12237468; fresh full text unavailable; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/doi-10.1110_ps.0212602.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/doi-10.1110_ps.0212602.receipt.json | partial | Primary abstract reports lysine crosslinking, MS spatial restraints and predicted structures leading to a PHB1-PHB2 heterodimeric building block and a proposed repeated palisade arrangement. It does not report an atomic experimental structure or require the current record to adopt a fixed universal count. No current Methods/pixel verification is claimed. |
| septin-yang2022-xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8913295/fullTextXML; Complete main Results, Discussion, Experimental procedures and Figure1/2/3 captions; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/yang2022-xml.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/yang2022-xml.receipt.json | supports | Recombinant mature yeast Pim1 expressed in E. coli BL21(DE3) Codon Plus RIPL; ATPgammaS-prepared substrate-bound hexamer. Static structural translocation model distinguished from trajectory observation. S1015A and insertion mutants tested with beta-casein, 0.1 mg/ml protease, 0.08 mg/ml substrate, 5 mM ATP, 37 C, one hour; activity is distinct from assembly formation or native viability. Data-availability accession errors are independently reconciled against archives. |
| septin-stahlberg1999-legacy | https://pmc.ncbi.nlm.nih.gov/articles/PMC21993/; Genuine canonical PMC HTML: complete Methods, Results, Discussion and captions; no pixel reading; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/stahlberg1999-legacy.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/stahlberg1999-legacy.receipt.json | supports | Yeast-overexpressed C-terminally tagged Pim1 isolated from mitochondrial extracts; nucleotide stabilization, crosslinked STEM/cryonegative staining and ultracentrifugation support the reported heptamer under that preparation. Conflict with the later recombinant substrate-bound hexamer remains explicit; no universal native stoichiometry is inferred. |
| septin-horten2024-xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11010658/fullTextXML; Complete main Results/Discussion/Limitations and STAR Methods including source strains, crosslinking, rescue, import/chase and MS; figure captions, no pixels; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/horten2024-xml.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/horten2024-xml.receipt.json | supports | YPH499/W303-derived yeast mitochondria. Co-migration, Psd1 affinity isolation and Nde1-AAC crosslinking support a selected MIMAS pool. Active Psd1, not S463A, rescues stability in psd1 deletion; inactive Psd1 can enter wild-type MIMAS. Rcf1 mutations shift localization; transient Cox13 import does not make mature Cox13 a stable constituent. PE dependence is not a directly resolved binding site or universal formation sequence; apparent 3.3/2.5 MDa peaks are not exact stoichiometry. |
| septin-review2026-xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13240547/fullTextXML; Secondary review body Section1.1 and Figure1 caption; no pixels; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/review2026-xml.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/review2026-xml.receipt.json | partial | Horten et al. 2026 summarizes MIMAS inner-membrane organization and states that matrix/outer-membrane association remains unresolved. It is secondary support, not an independent new experiment. |
| septin-chacinska2009-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC4099469.1/PMC4099469.1.xml; Secondary review body TOM portal, targeting, TIM23/PAM coupling and outer membrane assembly sections; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/chacinska2009-jats.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/chacinska2009-jats.receipt.json | partial | Chacinska et al. 2009 distinguishes Tom40 channel, Tom20/Tom70 recognition and Tom22 organization; downstream TIM23/PAM is separate. The record uses nonmechanistic topology/function edges. Cited perturbation work is described as reviewed literature, not freshly inspected primary experiments. |
| septin-artal2010-xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3034168/fullTextXML; Secondary review main Introduction and aging/metabolism/biogenesis discussion; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/artal2010-xml.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/artal2010-xml.receipt.json | partial | Artal-Sanz and Tavernarakis 2010 reviews repeating mitochondrial PHB complexes and condition-dependent functions. Yeast laboratory growth, animal development and aging effects are distinct; no universal loss-of-formation requirement is asserted. |
| septin-pride-PXD047946 | https://www.ebi.ac.uk/pride/ws/archive/v2/projects/PXD047946; Native project accession, title, species, submission type and publication link; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pride-PXD047946.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pride-PXD047946.receipt.json | context_only | PRIDE PXD047946 is a PARTIAL Saccharomyces MIMAS dataset with matching DOI; its pubmedID=0 field is a placeholder. Dataset metadata is provenance, not independent member quantification or reanalysis. |
| septin-pdb-7SXO | https://data.rcsb.org/rest/v1/core/entry/7SXO; Native structural archive entity/assembly/ligand or EMDB metadata; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pdb-7SXO.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pdb-7SXO.receipt.json | supports | 7SXO/EMD-25502 identify Yang 2022 yeast Pim1: six P36775-mapped protease chains plus one endogenous substrate entity, four ATP and two ADP, archive resolution3.3A. The A6B1 hetero-seven-chain aggregate is not seven Pim1 subunits. PDB7XSO and EMD-25505 name unrelated structures and corroborate the disclosed paper accession conflict. Archive source organism and bacterial expression/substrate context are not interchangeable. |
| septin-pdb-7SXO-assembly1 | https://data.rcsb.org/rest/v1/core/assembly/7SXO/1; Native structural archive entity/assembly/ligand or EMDB metadata; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pdb-7SXO-assembly1.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pdb-7SXO-assembly1.receipt.json | supports | 7SXO/EMD-25502 identify Yang 2022 yeast Pim1: six P36775-mapped protease chains plus one endogenous substrate entity, four ATP and two ADP, archive resolution3.3A. The A6B1 hetero-seven-chain aggregate is not seven Pim1 subunits. PDB7XSO and EMD-25505 name unrelated structures and corroborate the disclosed paper accession conflict. Archive source organism and bacterial expression/substrate context are not interchangeable. |
| septin-pdb-7SXO-entity1 | https://data.rcsb.org/rest/v1/core/polymer_entity/7SXO/1; Native structural archive entity/assembly/ligand or EMDB metadata; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pdb-7SXO-entity1.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pdb-7SXO-entity1.receipt.json | supports | 7SXO/EMD-25502 identify Yang 2022 yeast Pim1: six P36775-mapped protease chains plus one endogenous substrate entity, four ATP and two ADP, archive resolution3.3A. The A6B1 hetero-seven-chain aggregate is not seven Pim1 subunits. PDB7XSO and EMD-25505 name unrelated structures and corroborate the disclosed paper accession conflict. Archive source organism and bacterial expression/substrate context are not interchangeable. |
| septin-pdb-7SXO-entity2 | https://data.rcsb.org/rest/v1/core/polymer_entity/7SXO/2; Native structural archive entity/assembly/ligand or EMDB metadata; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pdb-7SXO-entity2.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pdb-7SXO-entity2.receipt.json | supports | 7SXO/EMD-25502 identify Yang 2022 yeast Pim1: six P36775-mapped protease chains plus one endogenous substrate entity, four ATP and two ADP, archive resolution3.3A. The A6B1 hetero-seven-chain aggregate is not seven Pim1 subunits. PDB7XSO and EMD-25505 name unrelated structures and corroborate the disclosed paper accession conflict. Archive source organism and bacterial expression/substrate context are not interchangeable. |
| septin-pdb-7SXO-nonpolymer3 | https://data.rcsb.org/rest/v1/core/nonpolymer_entity/7SXO/3; Native structural archive entity/assembly/ligand or EMDB metadata; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pdb-7SXO-nonpolymer3.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pdb-7SXO-nonpolymer3.receipt.json | supports | 7SXO/EMD-25502 identify Yang 2022 yeast Pim1: six P36775-mapped protease chains plus one endogenous substrate entity, four ATP and two ADP, archive resolution3.3A. The A6B1 hetero-seven-chain aggregate is not seven Pim1 subunits. PDB7XSO and EMD-25505 name unrelated structures and corroborate the disclosed paper accession conflict. Archive source organism and bacterial expression/substrate context are not interchangeable. |
| septin-pdb-7SXO-nonpolymer4 | https://data.rcsb.org/rest/v1/core/nonpolymer_entity/7SXO/4; Native structural archive entity/assembly/ligand or EMDB metadata; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pdb-7SXO-nonpolymer4.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pdb-7SXO-nonpolymer4.receipt.json | supports | 7SXO/EMD-25502 identify Yang 2022 yeast Pim1: six P36775-mapped protease chains plus one endogenous substrate entity, four ATP and two ADP, archive resolution3.3A. The A6B1 hetero-seven-chain aggregate is not seven Pim1 subunits. PDB7XSO and EMD-25505 name unrelated structures and corroborate the disclosed paper accession conflict. Archive source organism and bacterial expression/substrate context are not interchangeable. |
| septin-pdb-7SXO-nonpolymer5 | https://data.rcsb.org/rest/v1/core/nonpolymer_entity/7SXO/5; Native structural archive entity/assembly/ligand or EMDB metadata; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pdb-7SXO-nonpolymer5.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pdb-7SXO-nonpolymer5.receipt.json | supports | 7SXO/EMD-25502 identify Yang 2022 yeast Pim1: six P36775-mapped protease chains plus one endogenous substrate entity, four ATP and two ADP, archive resolution3.3A. The A6B1 hetero-seven-chain aggregate is not seven Pim1 subunits. PDB7XSO and EMD-25505 name unrelated structures and corroborate the disclosed paper accession conflict. Archive source organism and bacterial expression/substrate context are not interchangeable. |
| septin-emdb-25502 | https://files.wwpdb.org/pub/emdb/structures/EMD-25502/header/emd-25502.xml; Native structural archive entity/assembly/ligand or EMDB metadata; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/emdb-25502.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/emdb-25502.receipt.json | supports | 7SXO/EMD-25502 identify Yang 2022 yeast Pim1: six P36775-mapped protease chains plus one endogenous substrate entity, four ATP and two ADP, archive resolution3.3A. The A6B1 hetero-seven-chain aggregate is not seven Pim1 subunits. PDB7XSO and EMD-25505 name unrelated structures and corroborate the disclosed paper accession conflict. Archive source organism and bacterial expression/substrate context are not interchangeable. |
| septin-pdb-7XSO | https://data.rcsb.org/rest/v1/core/entry/7XSO; Native structural archive entity/assembly/ligand or EMDB metadata; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pdb-7XSO.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pdb-7XSO.receipt.json | supports | 7SXO/EMD-25502 identify Yang 2022 yeast Pim1: six P36775-mapped protease chains plus one endogenous substrate entity, four ATP and two ADP, archive resolution3.3A. The A6B1 hetero-seven-chain aggregate is not seven Pim1 subunits. PDB7XSO and EMD-25505 name unrelated structures and corroborate the disclosed paper accession conflict. Archive source organism and bacterial expression/substrate context are not interchangeable. |
| septin-emdb-25505 | https://files.wwpdb.org/pub/emdb/structures/EMD-25505/header/emd-25505.xml; Native structural archive entity/assembly/ligand or EMDB metadata; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/emdb-25505.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/emdb-25505.receipt.json | supports | 7SXO/EMD-25502 identify Yang 2022 yeast Pim1: six P36775-mapped protease chains plus one endogenous substrate entity, four ATP and two ADP, archive resolution3.3A. The A6B1 hetero-seven-chain aggregate is not seven Pim1 subunits. PDB7XSO and EMD-25505 name unrelated structures and corroborate the disclosed paper accession conflict. Archive source organism and bacterial expression/substrate context are not interchangeable. |
| septin-back2002-legacy | https://pmc.ncbi.nlm.nih.gov/articles/PMC2373692/; Actual failed or challenged current full-text route; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/back2002-legacy.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/back2002-legacy.receipt.json | context_only | Access diagnostic only: HTTP 200. Canonical HTTP200 responses contain browser/challenge markup, not a genuine article body. EP XML500, publisher403 and S3version1 absence do not refute the paper or its biology. |
| septin-back2002-epmc-fresh | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2373692/fullTextXML; Actual failed or challenged current full-text route; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/back2002-epmc-fresh.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/back2002-epmc-fresh.receipt.json | context_only | Access diagnostic only: HTTP 500. Canonical HTTP200 responses contain browser/challenge markup, not a genuine article body. EP XML500, publisher403 and S3version1 absence do not refute the paper or its biology. |
| septin-back2002-canonical-fresh | https://pmc.ncbi.nlm.nih.gov/articles/PMC2373692/?report=xml; Actual failed or challenged current full-text route; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/back2002-canonical-fresh.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/back2002-canonical-fresh.receipt.json | context_only | Access diagnostic only: HTTP 200. Canonical HTTP200 responses contain browser/challenge markup, not a genuine article body. EP XML500, publisher403 and S3version1 absence do not refute the paper or its biology. |
| septin-back2002-publisher-fresh | https://onlinelibrary.wiley.com/doi/full/10.1110/ps.0212602; Actual failed or challenged current full-text route; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/back2002-publisher-fresh.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/back2002-publisher-fresh.receipt.json | context_only | Access diagnostic only: HTTP 403. Canonical HTTP200 responses contain browser/challenge markup, not a genuine article body. EP XML500, publisher403 and S3version1 absence do not refute the paper or its biology. |
| septin-PMC2373692-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC2373692.1/PMC2373692.1.xml; Actual failed or challenged current full-text route; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/PMC2373692-jats.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/PMC2373692-jats.receipt.json | context_only | Access diagnostic only: HTTP 404. Canonical HTTP200 responses contain browser/challenge markup, not a genuine article body. EP XML500, publisher403 and S3version1 absence do not refute the paper or its biology. |
| septin-gene-PIM1 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3APIM1+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=500; Initial timed-out native query, later distinct retry retained; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-PIM1.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-PIM1.receipt.json | context_only | The initial request timed out; genuine later retry results are separate evidence. Failure is not zero hits or biological absence. |
| septin-gene-LON | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ALON+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=500; Initial timed-out native query, later distinct retry retained; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-LON.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-LON.receipt.json | context_only | The initial request timed out; genuine later retry results are separate evidence. Failure is not zero hits or biological absence. |
| septin-gene-RCF1 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ARCF1+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=500; Initial timed-out native query, later distinct retry retained; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-RCF1.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-RCF1.receipt.json | context_only | The initial request timed out; genuine later retry results are separate evidence. Failure is not zero hits or biological absence. |
| septin-gene-PSD1 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3APSD1+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=500; Initial timed-out native query, later distinct retry retained; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-PSD1.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-PSD1.receipt.json | context_only | The initial request timed out; genuine later retry results are separate evidence. Failure is not zero hits or biological absence. |
| septin-gene-TAZ1 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ATAZ1+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=500; Initial timed-out native query, later distinct retry retained; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-TAZ1.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-TAZ1.receipt.json | context_only | The initial request timed out; genuine later retry results are separate evidence. Failure is not zero hits or biological absence. |
| septin-gene-TOM20 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ATOM20+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=500; Initial timed-out native query, later distinct retry retained; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-TOM20.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-TOM20.receipt.json | context_only | The initial request timed out; genuine later retry results are separate evidence. Failure is not zero hits or biological absence. |
| septin-gene-TOM5 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ATOM5+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=500; Initial timed-out native query, later distinct retry retained; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-TOM5.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-TOM5.receipt.json | context_only | The initial request timed out; genuine later retry results are separate evidence. Failure is not zero hits or biological absence. |
| septin-lon-image-pixels | data/images/other/mitochondrial_lon_protease_complex/pmc8913295_fig1.jpg; Actual view_image inspection of complete Figure1 A/B pixels | supports | Observed model panels show colored substrate-bound Pim1 assembly, ATPase/protease orthogonal views and pore-loop/substrate close-up. This is a structural model illustration, not a raw micrograph or direct native-cell image. Six enzyme chains are distinct from substrate. |
| septin-yang2022-fig1 | https://pmc-oa-opendata.s3.amazonaws.com/PMC8913295.1/gr1.jpg; Fresh public gr1 media compared bytewise with the maintained image; Figure1 caption read; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/yang2022-fig1.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/yang2022-fig1.receipt.json | supports | Fresh gr1 and the maintained image are byte-identical, SHA256 a5c78bd75286956f9389092a1f0070b7df894266773b793201748c6a24b3ba6b. Image appearance agrees with the structural-model caption. |
| septin-yang2022-s3-gr3-jpg | https://pmc-oa-opendata.s3.amazonaws.com/PMC8913295.1/gr3.jpg; Actual view_image inspection of complete Figure3 A/B/C pixels and matching caption; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/yang2022-s3-gr3-jpg.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/yang2022-s3-gr3-jpg.receipt.json | supports | Construct diagrams and beta-casein gel time courses were visually inspected. Protease-inactive control retains casein; insertion deletion and G/S linker retain substantial degradation over the depicted hour. No numerical kinetic fit, assembly-loss test, native viability or all-substrate conclusion is inferred. |
| septin-yang2022-s3-PMC8913295-1-json | https://pmc-oa-opendata.s3.amazonaws.com/PMC8913295.1/PMC8913295.1.json; PMC package article/media metadata and gr1 MD5; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/yang2022-s3-PMC8913295-1-json.raw; retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/yang2022-s3-PMC8913295-1-json.receipt.json | context_only | Package identifies Yang, Song, Wiseman and Lander 2022, PMID35143841, DOI10.1016/j.jbc.2022.101694; CC BY metadata and matching gr1 MD5 fd98aa3d48b65d293f30c18c33dc815a. JATS permissions explicitly give CC BY4.0; maintained attribution is supported. |
| septin-adapter-catalogue | https://imodulondb.org/api/organisms; Complete current catalogue /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/adapter-catalogue.raw; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/adapter-catalogue.receipt.json | context_only | All 20 returned organism rows and 28 organism-dataset entries inspected. None covers Saccharomyces or another named fungal/mammalian biological host in this slice. E. coli recombinant expression or substrate annotation is not a matched mitochondrial host. No mismatched gene/module proxy query was used. |
| septin-historical-adapter-runner | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical 2026-11-03 00:49Z runner-canary receipt; no fresh invocation | context_only | The actual prior runner event was unavailable with PermissionError on pyvenv.cfg. It is reused only as historical tooling provenance; fresh official-source catalogue/authority checks provide the current fallback. |
| check-qc | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/qc.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| check-labels | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/labels.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| check-trait-links | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/trait-links.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Native TraitMech check passed: all 10 links resolve with matching labels against the 1130-trait source index. |
| check-vendored | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/vendored.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | All 22 governed artifacts match the pinned CLAW revision. |
| check-curies | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/curies.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified all 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| focused | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/focused-results.json; All twenty actual target schema/strict command outputs | supports | Ten schema and ten strict commands returned exit zero. |
| supplemental-pmid | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/pmid-chunks-receipt.json; Complete native-report PMID set checked with unchanged resolver in batches of at most fifty | supports | 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers remain unverified. |
| historical-adapter-runner-availability | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical runner invocation receipt; exact retained SHA256 reverified during PR2396 synthesis | context_only | Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS PermissionError reading the configured runner pyvenv.cfg. This is retained historical availability evidence, not a fresh attempt or a scientific validation failure. Native policy permits inspected source-catalogue fallback. |
| root-native-mic10_subcomplex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mic10_subcomplex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-mic10_subcomplex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mic10_subcomplex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-mic60_mic19_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mic60_mic19_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-mic60_mic19_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mic60_mic19_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-micos_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/micos_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-micos_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/micos_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-mim_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mim_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-mim_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mim_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-mis12_mind_type_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mis12_mind_type_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 4 represented protein examples; 5 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-mis12_mind_type_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mis12_mind_type_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 4 represented protein examples; 5 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-mitochondrial_inner_membrane_peptidase_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_inner_membrane_peptidase_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-mitochondrial_inner_membrane_peptidase_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_inner_membrane_peptidase_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-mitochondrial_lon_protease_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_lon_protease_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-mitochondrial_lon_protease_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_lon_protease_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-mitochondrial_multifunctional_assembly-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_multifunctional_assembly-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 5 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-mitochondrial_multifunctional_assembly-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_multifunctional_assembly-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 5 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-mitochondrial_outer_membrane_translocase_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_outer_membrane_translocase_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-mitochondrial_outer_membrane_translocase_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_outer_membrane_translocase_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-mitochondrial_prohibitin_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_prohibitin_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-mitochondrial_prohibitin_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_prohibitin_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |

## Limits And Additional Notes

- MIC10 subcomplex, Mic60-Mic19 complex and MICOS independent review: Assigned scientific coverage is indices0–2, with complete current records and immutable original pairs. All three have no inherited scientific findings. One staleMICOS target was substantively refreshed; two targets are unchanged. Additional frozen MIM record was read only for the separate quotation challenge owned by plaque. No new record-curation finding is established for the assigned trio.
- MIC10 subcomplex, Mic60-Mic19 complex and MICOS independent review: All 44 historical input occurrences and six original native validate/render commands passed; current source/main target hashes verified. Root six current native protein commands cover6 examples / 6 COVERED nodes (4+2); MICOS has 0 / 0. Empty native checks are not positive molecular validation. Root corpus/final successor/CI/queue gates remain separate.
- MIC10 subcomplex, Mic60-Mic19 complex and MICOS independent review: Primary read scopes are exactly those in each evidence locator: Rampelt main1883–1888; Friedman listed Results/Methods; Tirrell s3/s4/s11; Hessenberger seven named sections; Bock-Bierbaum Results/Discussion and specified Methods; Hoppins specified Results/Discussion/Methods. Only maintained Figure 3/4 pixels were inspected; other captions are text only. No raw data, density maps, movies or separately downloaded supplements were reanalysed.
- MIC10 subcomplex, Mic60-Mic19 complex and MICOS independent review: Harner 2011 current S3 failed404 and legacy HTTP 200 is reCAPTCHA; its complete indexed abstract was read. von der Malsburg 2011, Reinders 2006, Huh 2003 and Rabl 2009 remain indexed abstract/native-annotation tier. Pfanner 2014 complete text is nomenclature authority. Original historical access limits are not upgraded.
- MIC10 subcomplex, Mic60-Mic19 complex and MICOS independent review: Current five JSON UniProt entries plus one complete Mic10 flatfile and six exact gene/taxon/reviewed queries were independently inspected; each query has one matching result/no next page. Initial503/timeouts/rate limits are retained separately. Native reference strain does not identify every experimental strain.
- MIC10 subcomplex, Mic60-Mic19 complex and MICOS independent review: Family candidates were checked at current native descriptions/hierarchy; Mic19 DUF1690 remains an uncharacterised fungal family, not asserted as exact universal Mic19. Two zero-hitQuickGO text searches are bounded query results, not exhaustive ontology absence. No sequence alignment or guessed identifier.
- MIC10 subcomplex, Mic60-Mic19 complex and MICOS independent review: All three formal expression-only source exclusions are unsupported; fresh complete official catalogue: 20 organisms / 28 datasets has no matched biological-host dataset. Recombinant E. coli and unrelated Sulfolobus are not proxies. No downstream expression-module inference is made. Historical source-runner unavailable observation remains Nov 3 00:49Z and was not rerun here.
- MIC10 subcomplex, Mic60-Mic19 complex and MICOS independent review: Images equal current source downloads bytewise, exact permissions/figure captions inspected. No fresh OA metadataMD5 request or original Oct 4 retrieval recertification. Native strut/barrier, universal 4:4 stoichiometry, direct cardiolipin site and strain-prevalence census remain unresolved.
- MIC10 subcomplex, Mic60-Mic19 complex and MICOS independent review: Bundle defects are three formal applicability corrections, one historical access-kind occurrence and one stale target refresh. No scientific findings/actions/predecessors are invented, and no neighbor/group issue is terminally resolved by inference.
- MIC10 subcomplex, Mic60-Mic19 complex and MICOS independent review: Separate recovery search for a damaged PR2396 scratch receipt was written as an isolated audit. It is not a biological evidence source for this report and does not mutate any previous artifacts.
- MIM, MIS12/MIND and mitochondrial inner membrane peptidase independent review: Review is confined to assigned indices3,4,5 at source c9fe63bdff984abad241949c21dab3b13e975d1f; other frozen paths were hash-checked, not silently scientifically reviewed. No repository, record, Git or GitHub mutation was performed.
- MIM, MIS12/MIND and mitochondrial inner membrane peptidase independent review: Doan current direct body routes failed; scientific reading uses complete primary abstract plus explicitly retained indexed official PDF excerpts whose crawl predates this review. No fresh complete PDF, exhaustive Doan quotation absence or figure-pixel claim is made.
- MIM, MIS12/MIND and mitochondrial inner membrane peptidase independent review: Dimmer2012 corroboration uses indexed primary-paper text with explicit returned scope; no fresh downloaded PDF or independently viewed figure pixels. It supports bounded assembly contribution and counterlimits, not universal necessity.
- MIM, MIS12/MIND and mitochondrial inner membrane peptidase independent review: Vitali2018/2019, De Wulf and Kline were read only in declared sections; unlisted Methods, supplements, figures and papers cited in database annotations are not certified. Jan2000 remains complete primary abstract only; Gakh2002 is a secondary review abstract.
- MIM, MIS12/MIND and mitochondrial inner membrane peptidase independent review: Five corrected historical access/metadata observations retain original dates and hashes and are not fresh retrieval claims. Current access failures and successful alternative tiers are distinct.
- MIM, MIS12/MIND and mitochondrial inner membrane peptidase independent review: Only the MTW1 fresh bounded gene query succeeded; other fresh query transport failures do not certify uniqueness. Exact reviewed accessions and native current identity checks independently support the maintained examples.
- MIM, MIS12/MIND and mitochondrial inner membrane peptidase independent review: Catalogue absence is limited to all20 current organism rows/28 entries; no natural-host matches and no proxy downstream query. Computational expression membership would not establish assembly or necessity. Historical runner unavailability is not presented as a new invocation.
- MIM, MIS12/MIND and mitochondrial inner membrane peptidase independent review: All actual native coverage diagnostics are retained, including two MIS12 partial-example class symbols and the external outer-kinetochore actor; neither optional example absence nor unknown essentiality alone creates a finding.
- MIM, MIS12/MIND and mitochondrial inner membrane peptidase independent review: Original historical hashes and current51 frozen inputs are verified by the current original-check receipt. Global corpus gates, issue dedup/publication, final saved-head review and CI remain root-owned and are not precertified here.
- MIM, MIS12/MIND and mitochondrial inner membrane peptidase independent review: The separately documented loss of an unrelated PR2396 scratch receipt is not used as a scientific or validation dependency in this PR2397 report. No claim of byte restoration or fully reproducible historical replay is made.
- Mitochondrial Lon, multifunctional assembly, TOM and prohibitin independent review: Read-only assigned source review; no maintained record, original bundle, Git or GitHub mutation. Root owns global QC, persistence, final head/CI and publication. No future gate result is certified.
- Mitochondrial Lon, multifunctional assembly, TOM and prohibitin independent review: Back2002 fresh body unavailable after bounded genuine routes; complete abstract, native GO and genuine secondary review used with explicit scope. No Back2002 figure or Methods verification claimed.
- Mitochondrial Lon, multifunctional assembly, TOM and prohibitin independent review: Current pixel assessment is limited to maintained YangFigure1 and fresh YangFigure3. MIMAS and other source figure captions were read without current pixels; historical reviewer image claims are not inherited as fresh observations.
- Mitochondrial Lon, multifunctional assembly, TOM and prohibitin independent review: Native protein verification covers six represented examples and two COVERED nodes only; TOM/prohibitin inventories are empty. Identity, localization, structural membership and formation necessity remain distinct.
- Mitochondrial Lon, multifunctional assembly, TOM and prohibitin independent review: All four positive molecular scopes require source applicability assessment, but the complete current official catalogue contains no matching biological host. Historical Nov3 runner failure is not a fresh invocation; E.coli recombinant expression is not a host substitute.
- Mitochondrial Lon, multifunctional assembly, TOM and prohibitin independent review: Broad QuickGO search pages and exact gene queries have stated finite bounds. No global term absence, unseen full text, universal taxonomic prevalence, fixed generic stoichiometry or optional-inventory defect is inferred.
- Mitochondrial Lon, multifunctional assembly, TOM and prohibitin independent review: This report depends only on fresh current PR2397 original checks and intact current frozen inputs; the separately documented older auxiliary receipt retention loss is not restored or silently replaced.
- Historical retention limitation tracked by #3057: one PR2396 auxiliary validation receipt cannot be replayed byte-for-byte after a scratch overwrite. Its genuine prior execution and pre-incident hash observations remain evidenced. This review does not use that lost receipt or certify complete historical snapshot retention; current source snapshots and receipt bindings are reviewed independently.
- During preparation of this PR, a scratch helper overwrote one external auxiliary validation receipt from already-merged PR #2396. Issue #3057 records the exact loss, preserved genuine prior execution event and independent pre-incident hash observations. The old bytes are not restored; all current PR2397 inputs and checks are independent. A guarded current helper verifies its explicit workspace and source and refuses output overwrite. No scientific record, saved review or Git object was changed by the incident.
- All twenty native protein commands passed with eighteen represented examples and fifteen typed protein nodes: twelve COVERED, two PARTIAL_EXAMPLES in MIS12/MIND and one UNANCHORED_WITH_UNIPROT outer-kinetochore actor. These diagnostic classes and optional cross-species example limits are retained without treating them as automatic scientific defects.
- The seven original formal expression-only exclusions and three omitted applicability assessments are corrected using the actual current catalogue scope. Eleven original context-only evidence occurrences are reclassified: ten failed-access diagnostics as validation and one Crossref metadata item as database. Original timestamps and access limits are preserved.
- Four confirmed minor record-curation findings remain open: MIM assembly snippets, two MIS12/MIND family/synonym findings, and inherited TOM GIP synonym scope. The three inherited findings retain their exact predecessor occurrence identifiers; the new MIM finding has no invented predecessor.
- All 51 frozen inputs comprise ten current targets, twenty original review files, seventeen repository context files and four maintained images. Three independently authored reports retain their actual reading tiers, bounded searches, retrieval receipts and image-inspection limits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261104T154950Z-pr2397-current-record-followup
kind: batch
repository: CultureBotAI/CellStructureMech
title: 'PR 2397: current-input review of ten records and adversarial follow-up'
started_at: '2026-11-04T15:21:52.094888Z'
finished_at: '2026-11-04T15:49:50Z'
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
summary: Independent current-source review of all ten records refreshes three stale
  reviews (MICOS, MIM and MIS12/MIND). Four minor record-curation findings remain
  open across MIM, MIS12/MIND and TOM; seven records pass with explicit source and
  scope limitations. The immutable successor corrects ten structured-source applicability
  assessments and eleven historical evidence-kind occurrences while preserving the
  original bundles and exact inherited finding lineage. No maintained records are
  edited.
source:
  git_revision: c9fe63bdff984abad241949c21dab3b13e975d1f
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
  - path: data/images/other/mic10_subcomplex/pmc4434539_fig3.jpg
    sha256: af23bf8f6f0e98c05adf50c869b1a63705423d54278c9af60657b308361189c8
    role: context
  - path: data/images/other/mic60_mic19_complex/pmc5460017_f4.jpg
    sha256: 4a86dfab5f2d4d49925989b9566c18ffac1d087292f5ece4cd0dedcf9cf36954
    role: context
  - path: data/images/other/mim_complex/pmc6010339_fig5.jpg
    sha256: cdfb8f43e86424b85aa88ac2baa741035d8f107d58fe3b26ad48d595017a5af1
    role: context
  - path: data/images/other/mitochondrial_lon_protease_complex/pmc8913295_fig1.jpg
    sha256: a5c78bd75286956f9389092a1f0070b7df894266773b793201748c6a24b3ba6b
    role: context
  - path: data/structures/other/mic10_subcomplex.yaml
    sha256: 9d98461e5b91bf4eb28fffe1797678d45d3f6aa51391b289282b7b6155a22601
    role: target
  - path: data/structures/other/mic60_mic19_complex.yaml
    sha256: f69ade5a57e4946d6bb529c33ab623059348fd9a4c43609cea0b33b50d591cb7
    role: target
  - path: data/structures/other/micos_complex.yaml
    sha256: 756a5b48fd9109266e6ace5805f5f9fd4aaac9940ff39660960bb8603374f5aa
    role: target
  - path: data/structures/other/mim_complex.yaml
    sha256: 61bfb31d9aca0a2be252843e729f32e2b8ff9f3d02c77ba43e06d6f5a9229916
    role: target
  - path: data/structures/other/mis12_mind_type_complex.yaml
    sha256: 029ac75e12045a39ff6da937c63cff087715e76aadf1b65ad773f30bdfc4e944
    role: target
  - path: data/structures/other/mitochondrial_inner_membrane_peptidase_complex.yaml
    sha256: 8eb6f174c969fc2aef5a84a2a473fe42a66158531ae26422ccfd8ae3407227e0
    role: target
  - path: data/structures/other/mitochondrial_lon_protease_complex.yaml
    sha256: 22c985cbd94a32e0a04e1ba4b7f77e796ef99815390b9165a3b15b987429d5d6
    role: target
  - path: data/structures/other/mitochondrial_multifunctional_assembly.yaml
    sha256: bb1a36eee48a44140250e04951a42f149f5de60affd5e146ba8f89f8a6e48858
    role: target
  - path: data/structures/other/mitochondrial_outer_membrane_translocase_complex.yaml
    sha256: a9facce19eda1794aefb3bef7b36fe07ba5c3a942220a4379c5569de4150022e
    role: target
  - path: data/structures/other/mitochondrial_prohibitin_complex.yaml
    sha256: a2a0c89fc814c0dba32ef8a1b90246ced003e274382c67d78794cbd86e9b7453
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
  - path: reviews/structured/20261022T084805Z-mic10-subcomplex-audit/review.md
    sha256: 87a19c26616ebb1ebe9084d506a231befef698fa3ddbb0d5799d0df2138f6deb
    role: context
  - path: reviews/structured/20261022T084805Z-mic10-subcomplex-audit/review.yaml
    sha256: 8b9b5b2e1275daa508b1f23bf797a2890fbdc1fd0c0fcdc0254cfdbcbee22271
    role: context
  - path: reviews/structured/20261022T084806Z-mic60-mic19-complex-audit/review.md
    sha256: 15370205f88fb3cd307348bc7e583be61fcf438f35ec2089b07869ec11ec2f81
    role: context
  - path: reviews/structured/20261022T084806Z-mic60-mic19-complex-audit/review.yaml
    sha256: 86cf74dfa21d30946634247871ef5bacc3a360b821de2fba53a3b5d2327efd5f
    role: context
  - path: reviews/structured/20261022T084806Z-micos-complex-audit/review.md
    sha256: f240ce7aa709443de002d2b3b819833db4b2ecc7af8ba5cba5d2437a5c2523ac
    role: context
  - path: reviews/structured/20261022T084806Z-micos-complex-audit/review.yaml
    sha256: fe076d23b6e6b8cce8b3e5e73f3b2f3288f19f305d2084684b64468eb77328d4
    role: context
  - path: reviews/structured/20261022T084807Z-mim-complex-audit/review.md
    sha256: b0c977d0793e887ed80d64955e286c1825cf5e4f73b61b6663d35dc11a6e7c8e
    role: context
  - path: reviews/structured/20261022T084807Z-mim-complex-audit/review.yaml
    sha256: 6f1170d640c261dca83cb7003770c16b9181a00e841a49eadeff057bd0748785
    role: context
  - path: reviews/structured/20261022T084808Z-mis12-mind-type-complex-audit/review.md
    sha256: 4f88e1ea22e8671dd8bba6fe13dd91b59c1e5e5c4ac3db153fcfe099a562480c
    role: context
  - path: reviews/structured/20261022T084808Z-mis12-mind-type-complex-audit/review.yaml
    sha256: b155982f70cb3c45961366da6da82566a268839b6d3ef6f916a390c04719c39f
    role: context
  - path: reviews/structured/20261022T084808Z-mitochondrial-inner-membrane-peptidase-complex-audit/review.md
    sha256: 8cbc0eca4bfd31a74c6c7fa9e649f94e360bc63073abe77236581adb50e55ad7
    role: context
  - path: reviews/structured/20261022T084808Z-mitochondrial-inner-membrane-peptidase-complex-audit/review.yaml
    sha256: 5ec6c6f0d6b3aad3d0388740337689e5fab22a2a0e52b42f17ccd95e858ed9dc
    role: context
  - path: reviews/structured/20261022T084809Z-mitochondrial-lon-protease-complex-audit/review.md
    sha256: 12099cc97ccfca3aca18795671bee5cc5e3a08f38063d3e077b71617807e9435
    role: context
  - path: reviews/structured/20261022T084809Z-mitochondrial-lon-protease-complex-audit/review.yaml
    sha256: 45c479278c71463c35d945a3042c7275494464a564b7f16595ca190e42c0ca38
    role: context
  - path: reviews/structured/20261022T084810Z-mitochondrial-multifunctional-assembly-audit/review.md
    sha256: eb85675f462c6455e80610dd4b48e7b1215c9245eeded978f7fd7f066e80e59a
    role: context
  - path: reviews/structured/20261022T084810Z-mitochondrial-multifunctional-assembly-audit/review.yaml
    sha256: b8b8e993357ca73262007d2b28664ed80d09cdbd06c88cbc8466b759c36ce7d4
    role: context
  - path: reviews/structured/20261022T084810Z-mitochondrial-outer-membrane-translocase-complex-audit/review.md
    sha256: 16b2b49cd2dc650e1927f8cacdd5049c40f99fba622abb77f2cbca73ffba5784
    role: context
  - path: reviews/structured/20261022T084810Z-mitochondrial-outer-membrane-translocase-complex-audit/review.yaml
    sha256: 72a7419c81e55ff10873a91cfddab435d2d646018402fc578dcfda39d7d8def0
    role: context
  - path: reviews/structured/20261022T084811Z-mitochondrial-prohibitin-complex-audit/review.md
    sha256: efe9cdc00a01cc80b91c2a081393674144af2927444dd69906d5a5af4f1922a5
    role: context
  - path: reviews/structured/20261022T084811Z-mitochondrial-prohibitin-complex-audit/review.yaml
    sha256: d9157ec12ac92d7f92166d6921a1542bdc796a7ce9cf4c7bb81dd1e3c4efd17f
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
- target_id: cellstructuremech:mic10_subcomplex
  path: data/structures/other/mic10_subcomplex.yaml
  label: MIC10 subcomplex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/mic10_subcomplex.yaml
    role: maintained scientific record
- target_id: cellstructuremech:mic60_mic19_complex
  path: data/structures/other/mic60_mic19_complex.yaml
  label: Mic60-Mic19 complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/mic60_mic19_complex.yaml
    role: maintained scientific record
- target_id: GO:0061617
  path: data/structures/other/micos_complex.yaml
  label: MICOS complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/micos_complex.yaml
    role: maintained scientific record
- target_id: GO:0140595
  path: data/structures/other/mim_complex.yaml
  label: MIM complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/mim_complex.yaml
    role: maintained scientific record
- target_id: GO:0000444
  path: data/structures/other/mis12_mind_type_complex.yaml
  label: MIS12/MIND type complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/mis12_mind_type_complex.yaml
    role: maintained scientific record
- target_id: GO:0042720
  path: data/structures/other/mitochondrial_inner_membrane_peptidase_complex.yaml
  label: mitochondrial inner membrane peptidase complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/mitochondrial_inner_membrane_peptidase_complex.yaml
    role: maintained scientific record
- target_id: cellstructuremech:mitochondrial_lon_protease_complex
  path: data/structures/other/mitochondrial_lon_protease_complex.yaml
  label: mitochondrial Lon protease complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/mitochondrial_lon_protease_complex.yaml
    role: maintained scientific record
- target_id: cellstructuremech:mitochondrial_multifunctional_assembly
  path: data/structures/other/mitochondrial_multifunctional_assembly.yaml
  label: mitochondrial multifunctional assembly
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/mitochondrial_multifunctional_assembly.yaml
    role: maintained scientific record
- target_id: GO:0005742
  path: data/structures/other/mitochondrial_outer_membrane_translocase_complex.yaml
  label: mitochondrial outer membrane translocase complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/mitochondrial_outer_membrane_translocase_complex.yaml
    role: maintained scientific record
- target_id: GO:0035632
  path: data/structures/other/mitochondrial_prohibitin_complex.yaml
  label: mitochondrial prohibitin complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/mitochondrial_prohibitin_complex.yaml
    role: maintained scientific record
scope:
  description: Exact ten-record PR cohort reassessed against current main 52a4db8d611558a6bc665e275e207f05c1eb81b2.
    Changed inputs are substantively reassessed. Scientific records remain unchanged.
  selection: Complete cohort of ten maintained records reviewed in original PR head
    32d5d3d0cd6124c17063e87c175be8945602148f.
  coverage: full
  population_size: 10
  reviewed_target_ids:
  - cellstructuremech:mic10_subcomplex
  - cellstructuremech:mic60_mic19_complex
  - GO:0061617
  - GO:0140595
  - GO:0000444
  - GO:0042720
  - cellstructuremech:mitochondrial_lon_protease_complex
  - cellstructuremech:mitochondrial_multifunctional_assembly
  - GO:0005742
  - GO:0035632
checks:
- check_id: qc
  name: Full native QC
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mic10_subcomplex
  - cellstructuremech:mic60_mic19_complex
  - GO:0061617
  - GO:0140595
  - GO:0000444
  - GO:0042720
  - cellstructuremech:mitochondrial_lon_protease_complex
  - cellstructuremech:mitochondrial_multifunctional_assembly
  - GO:0005742
  - GO:0035632
  command: just qc
  exit_code: 0
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  scope_note: Actual local execution at main-merge head c9fe63bdff984abad241949c21dab3b13e975d1f.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-qc
- check_id: labels
  name: Native label correspondence
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mic10_subcomplex
  - cellstructuremech:mic60_mic19_complex
  - GO:0061617
  - GO:0140595
  - GO:0000444
  - GO:0042720
  - cellstructuremech:mitochondrial_lon_protease_complex
  - cellstructuremech:mitochondrial_multifunctional_assembly
  - GO:0005742
  - GO:0035632
  command: just validate-products
  exit_code: 0
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  scope_note: Actual local execution at main-merge head c9fe63bdff984abad241949c21dab3b13e975d1f.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-labels
- check_id: trait-links
  name: TraitMech references
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mic10_subcomplex
  - cellstructuremech:mic60_mic19_complex
  - GO:0061617
  - GO:0140595
  - GO:0000444
  - GO:0042720
  - cellstructuremech:mitochondrial_lon_protease_complex
  - cellstructuremech:mitochondrial_multifunctional_assembly
  - GO:0005742
  - GO:0035632
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Native TraitMech check passed: all 10 links resolve with matching labels
    against the 1130-trait source index.'
  scope_note: Actual local execution at main-merge head c9fe63bdff984abad241949c21dab3b13e975d1f.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-trait-links
- check_id: vendored
  name: Pinned governed files
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mic10_subcomplex
  - cellstructuremech:mic60_mic19_complex
  - GO:0061617
  - GO:0140595
  - GO:0000444
  - GO:0042720
  - cellstructuremech:mitochondrial_lon_protease_complex
  - cellstructuremech:mitochondrial_multifunctional_assembly
  - GO:0005742
  - GO:0035632
  command: just vendored-check
  exit_code: 0
  summary: All 22 governed artifacts match the pinned CLAW revision.
  scope_note: Actual local execution at main-merge head c9fe63bdff984abad241949c21dab3b13e975d1f.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-vendored
- check_id: curies
  name: Native identifier resolver
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mic10_subcomplex
  - cellstructuremech:mic60_mic19_complex
  - GO:0061617
  - GO:0140595
  - GO:0000444
  - GO:0042720
  - cellstructuremech:mitochondrial_lon_protease_complex
  - cellstructuremech:mitochondrial_multifunctional_assembly
  - GO:0005742
  - GO:0035632
  command: just check-curies-strict
  exit_code: 0
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    all 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  scope_note: Actual local execution at main-merge head c9fe63bdff984abad241949c21dab3b13e975d1f.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-curies
- check_id: focused-0
  name: validate cellstructuremech:mic10_subcomplex
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mic10_subcomplex
  command: just validate data/structures/other/mic10_subcomplex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-1
  name: validate-strict cellstructuremech:mic10_subcomplex
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mic10_subcomplex
  command: just validate-strict data/structures/other/mic10_subcomplex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-2
  name: validate cellstructuremech:mic60_mic19_complex
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mic60_mic19_complex
  command: just validate data/structures/other/mic60_mic19_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-3
  name: validate-strict cellstructuremech:mic60_mic19_complex
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mic60_mic19_complex
  command: just validate-strict data/structures/other/mic60_mic19_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-4
  name: validate GO:0061617
  status: passed
  required: true
  target_ids:
  - GO:0061617
  command: just validate data/structures/other/micos_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-5
  name: validate-strict GO:0061617
  status: passed
  required: true
  target_ids:
  - GO:0061617
  command: just validate-strict data/structures/other/micos_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-6
  name: validate GO:0140595
  status: passed
  required: true
  target_ids:
  - GO:0140595
  command: just validate data/structures/other/mim_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-7
  name: validate-strict GO:0140595
  status: passed
  required: true
  target_ids:
  - GO:0140595
  command: just validate-strict data/structures/other/mim_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-8
  name: validate GO:0000444
  status: passed
  required: true
  target_ids:
  - GO:0000444
  command: just validate data/structures/other/mis12_mind_type_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-9
  name: validate-strict GO:0000444
  status: passed
  required: true
  target_ids:
  - GO:0000444
  command: just validate-strict data/structures/other/mis12_mind_type_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-10
  name: validate GO:0042720
  status: passed
  required: true
  target_ids:
  - GO:0042720
  command: just validate data/structures/other/mitochondrial_inner_membrane_peptidase_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-11
  name: validate-strict GO:0042720
  status: passed
  required: true
  target_ids:
  - GO:0042720
  command: just validate-strict data/structures/other/mitochondrial_inner_membrane_peptidase_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-12
  name: validate cellstructuremech:mitochondrial_lon_protease_complex
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitochondrial_lon_protease_complex
  command: just validate data/structures/other/mitochondrial_lon_protease_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-13
  name: validate-strict cellstructuremech:mitochondrial_lon_protease_complex
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitochondrial_lon_protease_complex
  command: just validate-strict data/structures/other/mitochondrial_lon_protease_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-14
  name: validate cellstructuremech:mitochondrial_multifunctional_assembly
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitochondrial_multifunctional_assembly
  command: just validate data/structures/other/mitochondrial_multifunctional_assembly.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-15
  name: validate-strict cellstructuremech:mitochondrial_multifunctional_assembly
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitochondrial_multifunctional_assembly
  command: just validate-strict data/structures/other/mitochondrial_multifunctional_assembly.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-16
  name: validate GO:0005742
  status: passed
  required: true
  target_ids:
  - GO:0005742
  command: just validate data/structures/other/mitochondrial_outer_membrane_translocase_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-17
  name: validate-strict GO:0005742
  status: passed
  required: true
  target_ids:
  - GO:0005742
  command: just validate-strict data/structures/other/mitochondrial_outer_membrane_translocase_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-18
  name: validate GO:0035632
  status: passed
  required: true
  target_ids:
  - GO:0035632
  command: just validate data/structures/other/mitochondrial_prohibitin_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-19
  name: validate-strict GO:0035632
  status: passed
  required: true
  target_ids:
  - GO:0035632
  command: just validate-strict data/structures/other/mitochondrial_prohibitin_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: supplemental-pmid
  name: Supplemental bounded PMID authority checks
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mic10_subcomplex
  - cellstructuremech:mic60_mic19_complex
  - GO:0061617
  - GO:0140595
  - GO:0000444
  - GO:0042720
  - cellstructuremech:mitochondrial_lon_protease_complex
  - cellstructuremech:mitochondrial_multifunctional_assembly
  - GO:0005742
  - GO:0035632
  command: .venv/bin/python /private/tmp/cellstructure-batches-2346-2397-20261103/check_pmid_chunks.py
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397
  exit_code: 0
  summary: 909 PMIDs all OK in bounded native requests; full-command limitations remain
    separate.
  evidence_ids:
  - supplemental-pmid
- check_id: structured-source-applicability
  name: Official structured-source applicability and covered-dataset cross-checks
  status: not_applicable
  required: false
  target_ids:
  - cellstructuremech:mic10_subcomplex
  - cellstructuremech:mic60_mic19_complex
  - GO:0061617
  - GO:0140595
  - GO:0000444
  - GO:0042720
  - cellstructuremech:mitochondrial_lon_protease_complex
  - cellstructuremech:mitochondrial_multifunctional_assembly
  - GO:0005742
  - GO:0035632
  summary: All ten records contain positive molecular or pathway claims requiring
    structured-source applicability assessment. The current complete official catalogue
    covers 20 organisms and 28 datasets, with no matching natural biological host
    for these eukaryotic targets. Recombinant Escherichia coli and unrelated Sulfolobus
    datasets are not substitutes. Preserve the actual historical Nov3 runner PermissionError
    as historical; current primary literature and native authority checks provide
    the bounded fallback. No fresh successful adapter invocation is claimed.
  evidence_ids:
  - micro-adapter-catalogue
  - plaque-adapter-catalogue
  - septin-adapter-catalogue
- check_id: independent-scientific-review
  name: Independent claim-level source review
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mic10_subcomplex
  - cellstructuremech:mic60_mic19_complex
  - GO:0061617
  - GO:0140595
  - GO:0000444
  - GO:0042720
  - cellstructuremech:mitochondrial_lon_protease_complex
  - cellstructuremech:mitochondrial_multifunctional_assembly
  - GO:0005742
  - GO:0035632
  summary: Three read-only reviewers covered the complete ten-record cohort, including
    changed inputs, with explicit scientific findings and source-access limits. Final
    artifact/head acceptance occurs after saving.
  evidence_ids:
  - micro-policy
  - micro-schema
  - micro-graph-policy
  - micro-native-policy
  - micro-native-config
  - micro-protein-P38341-retry
  - micro-protein-P50087-retry
  - micro-protein-P50945-retry
  - micro-protein-P36112-retry
  - micro-protein-P43594-retry
  - micro-protein-Q96VH5-final
  - micro-ipr-IPR007512
  - micro-ipr-IPR031463
  - micro-ipr-IPR033181
  - micro-ipr-IPR061953
  - micro-ipr-IPR019133-retry
  - micro-ipr-IPR012471-retry
  - micro-tax-4932
  - micro-tax-559292
  - micro-go
  - micro-GO0061617-ancestors
  - micro-GO0098800-ancestors
  - micro-bock2022-meta
  - micro-friedman2015-meta
  - micro-harner2011-meta
  - micro-hessenberger2017-meta
  - micro-hoppins2011-meta
  - micro-malsburg2011-meta
  - micro-pfanner2014-meta
  - micro-rampelt2018-meta
  - micro-tirrell2020-meta
  - micro-pmid-14562095
  - micro-pmid-16823961
  - micro-pmid-19528297
  - micro-pmid-21944719
  - micro-pmid-21987634
  - micro-rampelt2018-pdf
  - micro-friedman2015-s3
  - micro-tirrell2020-s3
  - micro-hessenberger2017-s3
  - micro-bock2022-s3
  - micro-hoppins2011-s3
  - micro-pfanner2014-s3
  - micro-friedman2015-fig3
  - micro-hessenberger2017-fig4
  - plaque-go-0000444-parents
  - plaque-go-0000444
  - plaque-go-0000776
  - plaque-go-0000940-parents
  - plaque-go-0000940
  - plaque-go-0005741
  - plaque-go-0005743
  - plaque-go-0032991
  - plaque-go-0034982
  - plaque-go-0042720-parents
  - plaque-go-0042720
  - plaque-go-0098799
  - plaque-go-0098800
  - plaque-go-0140595-parents
  - plaque-go-0140595
  - plaque-go-1905370
  - plaque-go-7770059
  - plaque-ipr-IPR013262
  - plaque-ipr-IPR037652
  - plaque-ipr-IPR008685
  - plaque-ipr-IPR013218
  - plaque-ipr-IPR013950
  - plaque-ipr-IPR007128
  - plaque-ipr-IPR016851
  - plaque-up-Q08176-retry
  - plaque-up-Q3E798
  - plaque-up-P39731
  - plaque-up-P40568
  - plaque-up-Q12143
  - plaque-up-P47149-retry
  - plaque-up-P40460
  - plaque-up-P33895
  - plaque-up-Q04477-retry
  - plaque-tax-4932
  - plaque-tax-559292
  - plaque-doan2020-metadata
  - plaque-vitali2018-metadata
  - plaque-vitali2019-metadata
  - plaque-dewulf2003-metadata
  - plaque-kline2006-metadata
  - plaque-jan2000-metadata
  - plaque-gakh2002-pmid
  - plaque-pmid-15326197
  - plaque-pmid-15608614
  - plaque-pmid-22467864
  - plaque-pmid-12455957
  - plaque-pmid-14602074
  - plaque-pmid-14657030
  - plaque-PMC6010339-jats
  - plaque-PMC6965732-jats
  - plaque-kline2006-jats
  - plaque-dewulf2003-legacy
  - plaque-doan2020-web-indexed
  - plaque-doan2020-web-sections
  - plaque-doan2020-web-methods
  - plaque-dimmer2012-web-indexed
  - plaque-dimmer2012-web-sections
  - plaque-mim-figure5
  - plaque-mim-package
  - plaque-historical-t5-micro60-gakh2002-publisher
  - septin-review-policy
  - septin-curation-policy
  - septin-protein-policy
  - septin-graph-policy
  - septin-literature-policy
  - septin-go
  - septin-go-0005742-ancestors
  - septin-go-0035632-ancestors
  - septin-tax-4932
  - septin-tax-559292
  - septin-tax-2759
  - septin-ipr-IPR000163
  - septin-ipr-IPR000872
  - septin-ipr-IPR002056
  - septin-ipr-IPR002113
  - septin-ipr-IPR005683
  - septin-ipr-IPR005686
  - septin-ipr-IPR005687
  - septin-ipr-IPR012621
  - septin-ipr-IPR019603
  - septin-ipr-IPR020266
  - septin-ipr-IPR020951
  - septin-ipr-IPR027503
  - septin-ipr-IPR033661
  - septin-ipr-IPR037930
  - septin-ipr-IPR045024
  - septin-ipr-IPR050355
  - septin-protein-P18239
  - septin-protein-P36775
  - septin-protein-P39006
  - septin-protein-P40215
  - septin-protein-Q03713
  - septin-protein-Q06510
  - septin-doi-10.1016_j.cell.2009.08.005
  - septin-doi-10.1016_j.jbc.2022.101694
  - septin-doi-10.1073_pnas.96.12.6787
  - septin-doi-10.1110_ps.0212602
  - septin-doi-10.18632_aging.100246
  - septin-pmid-14562095
  - septin-pmid-14576278
  - septin-pmid-15588229
  - septin-pmid-16135531
  - septin-pmid-16880272
  - septin-pmid-22984266
  - septin-pmid-23124206
  - septin-pmid-35127709
  - septin-pmid-38393949
  - septin-pmid-42178653
  - septin-pmid-795470
  - septin-back2002-abstract
  - septin-yang2022-xml
  - septin-stahlberg1999-legacy
  - septin-horten2024-xml
  - septin-review2026-xml
  - septin-chacinska2009-jats
  - septin-artal2010-xml
  - septin-pride-PXD047946
  - septin-pdb-7SXO
  - septin-pdb-7SXO-assembly1
  - septin-pdb-7SXO-entity1
  - septin-pdb-7SXO-entity2
  - septin-pdb-7SXO-nonpolymer3
  - septin-pdb-7SXO-nonpolymer4
  - septin-pdb-7SXO-nonpolymer5
  - septin-emdb-25502
  - septin-pdb-7XSO
  - septin-emdb-25505
  - septin-yang2022-fig1
  - septin-yang2022-s3-gr3-jpg
  - septin-yang2022-s3-PMC8913295-1-json
- check_id: historical-adapter-runner
  name: Retained historical adapter runner availability
  status: unavailable
  required: false
  target_ids:
  - cellstructuremech:mic10_subcomplex
  - cellstructuremech:mic60_mic19_complex
  - GO:0061617
  - GO:0140595
  - GO:0000444
  - GO:0042720
  - cellstructuremech:mitochondrial_lon_protease_complex
  - cellstructuremech:mitochondrial_multifunctional_assembly
  - GO:0005742
  - GO:0035632
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
- check_id: mic10_subcomplex-uniprot-verify
  name: Native MIC10 subcomplex UniProt verify check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mic10_subcomplex
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/mic10_subcomplex.yaml
    --verify
  exit_code: 0
  summary: 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-mic10_subcomplex-uniprot-verify
- check_id: mic10_subcomplex-uniprot-causal
  name: Native MIC10 subcomplex UniProt causal check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mic10_subcomplex
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/mic10_subcomplex.yaml
    --causal-graphs
  exit_code: 0
  summary: 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-mic10_subcomplex-uniprot-causal
- check_id: mic60_mic19_complex-uniprot-verify
  name: Native Mic60-Mic19 complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mic60_mic19_complex
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/mic60_mic19_complex.yaml
    --verify
  exit_code: 0
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-mic60_mic19_complex-uniprot-verify
- check_id: mic60_mic19_complex-uniprot-causal
  name: Native Mic60-Mic19 complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mic60_mic19_complex
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/mic60_mic19_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-mic60_mic19_complex-uniprot-causal
- check_id: micos_complex-uniprot-verify
  name: Native MICOS complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0061617
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/micos_complex.yaml
    --verify
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-micos_complex-uniprot-verify
- check_id: micos_complex-uniprot-causal
  name: Native MICOS complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0061617
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/micos_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-micos_complex-uniprot-causal
- check_id: mim_complex-uniprot-verify
  name: Native MIM complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0140595
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/mim_complex.yaml
    --verify
  exit_code: 0
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-mim_complex-uniprot-verify
- check_id: mim_complex-uniprot-causal
  name: Native MIM complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0140595
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/mim_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-mim_complex-uniprot-causal
- check_id: mis12_mind_type_complex-uniprot-verify
  name: Native MIS12/MIND type complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0000444
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/mis12_mind_type_complex.yaml
    --verify
  exit_code: 0
  summary: 4 represented protein examples; 5 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-mis12_mind_type_complex-uniprot-verify
- check_id: mis12_mind_type_complex-uniprot-causal
  name: Native MIS12/MIND type complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0000444
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/mis12_mind_type_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 4 represented protein examples; 5 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-mis12_mind_type_complex-uniprot-causal
- check_id: mitochondrial_inner_membrane_peptidase_complex-uniprot-verify
  name: Native mitochondrial inner membrane peptidase complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0042720
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/mitochondrial_inner_membrane_peptidase_complex.yaml
    --verify
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-mitochondrial_inner_membrane_peptidase_complex-uniprot-verify
- check_id: mitochondrial_inner_membrane_peptidase_complex-uniprot-causal
  name: Native mitochondrial inner membrane peptidase complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0042720
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/mitochondrial_inner_membrane_peptidase_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-mitochondrial_inner_membrane_peptidase_complex-uniprot-causal
- check_id: mitochondrial_lon_protease_complex-uniprot-verify
  name: Native mitochondrial Lon protease complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitochondrial_lon_protease_complex
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/mitochondrial_lon_protease_complex.yaml
    --verify
  exit_code: 0
  summary: 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-mitochondrial_lon_protease_complex-uniprot-verify
- check_id: mitochondrial_lon_protease_complex-uniprot-causal
  name: Native mitochondrial Lon protease complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitochondrial_lon_protease_complex
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/mitochondrial_lon_protease_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-mitochondrial_lon_protease_complex-uniprot-causal
- check_id: mitochondrial_multifunctional_assembly-uniprot-verify
  name: Native mitochondrial multifunctional assembly UniProt verify check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitochondrial_multifunctional_assembly
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/mitochondrial_multifunctional_assembly.yaml
    --verify
  exit_code: 0
  summary: 5 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-mitochondrial_multifunctional_assembly-uniprot-verify
- check_id: mitochondrial_multifunctional_assembly-uniprot-causal
  name: Native mitochondrial multifunctional assembly UniProt causal check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitochondrial_multifunctional_assembly
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/mitochondrial_multifunctional_assembly.yaml
    --causal-graphs
  exit_code: 0
  summary: 5 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-mitochondrial_multifunctional_assembly-uniprot-causal
- check_id: mitochondrial_outer_membrane_translocase_complex-uniprot-verify
  name: Native mitochondrial outer membrane translocase complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0005742
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/mitochondrial_outer_membrane_translocase_complex.yaml
    --verify
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-mitochondrial_outer_membrane_translocase_complex-uniprot-verify
- check_id: mitochondrial_outer_membrane_translocase_complex-uniprot-causal
  name: Native mitochondrial outer membrane translocase complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0005742
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/mitochondrial_outer_membrane_translocase_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-mitochondrial_outer_membrane_translocase_complex-uniprot-causal
- check_id: mitochondrial_prohibitin_complex-uniprot-verify
  name: Native mitochondrial prohibitin complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0035632
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/mitochondrial_prohibitin_complex.yaml
    --verify
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-mitochondrial_prohibitin_complex-uniprot-verify
- check_id: mitochondrial_prohibitin_complex-uniprot-causal
  name: Native mitochondrial prohibitin complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0035632
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/mitochondrial_prohibitin_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-mitochondrial_prohibitin_complex-uniprot-causal
evidence:
- evidence_id: current-record-0
  kind: record_content
  reference: data/structures/other/mic10_subcomplex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T15:49:50Z'
  support: context_only
  summary: Original frozen SHA256 9d98461e5b91bf4eb28fffe1797678d45d3f6aa51391b289282b7b6155a22601;
    current SHA256 9d98461e5b91bf4eb28fffe1797678d45d3f6aa51391b289282b7b6155a22601.
    Record bytes unchanged since the original review.
  snapshot_sha256: 9d98461e5b91bf4eb28fffe1797678d45d3f6aa51391b289282b7b6155a22601
- evidence_id: original-review-0
  kind: prior_review
  reference: reviews/structured/20261022T084805Z-mic10-subcomplex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T15:49:50Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 8b9b5b2e1275daa508b1f23bf797a2890fbdc1fd0c0fcdc0254cfdbcbee22271
- evidence_id: current-record-1
  kind: record_content
  reference: data/structures/other/mic60_mic19_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T15:49:50Z'
  support: context_only
  summary: Original frozen SHA256 f69ade5a57e4946d6bb529c33ab623059348fd9a4c43609cea0b33b50d591cb7;
    current SHA256 f69ade5a57e4946d6bb529c33ab623059348fd9a4c43609cea0b33b50d591cb7.
    Record bytes unchanged since the original review.
  snapshot_sha256: f69ade5a57e4946d6bb529c33ab623059348fd9a4c43609cea0b33b50d591cb7
- evidence_id: original-review-1
  kind: prior_review
  reference: reviews/structured/20261022T084806Z-mic60-mic19-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T15:49:50Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 86cf74dfa21d30946634247871ef5bacc3a360b821de2fba53a3b5d2327efd5f
- evidence_id: current-record-2
  kind: record_content
  reference: data/structures/other/micos_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T15:49:50Z'
  support: context_only
  summary: Original frozen SHA256 95c3aa4af71bf436a4c5dbbd527d47ff46c73d484843425fdd9c44615782375f;
    current SHA256 756a5b48fd9109266e6ace5805f5f9fd4aaac9940ff39660960bb8603374f5aa.
    Changed record reassessed against current sources.
  snapshot_sha256: 756a5b48fd9109266e6ace5805f5f9fd4aaac9940ff39660960bb8603374f5aa
- evidence_id: original-review-2
  kind: prior_review
  reference: reviews/structured/20261022T084806Z-micos-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T15:49:50Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: fe076d23b6e6b8cce8b3e5e73f3b2f3288f19f305d2084684b64468eb77328d4
- evidence_id: current-record-3
  kind: record_content
  reference: data/structures/other/mim_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T15:49:50Z'
  support: context_only
  summary: Original frozen SHA256 dc0d4007dfe5d82f22b45d46cc12e3c934ce3ebe92d7ed7b48c25be1ea715c5f;
    current SHA256 61bfb31d9aca0a2be252843e729f32e2b8ff9f3d02c77ba43e06d6f5a9229916.
    Changed record reassessed against current sources.
  snapshot_sha256: 61bfb31d9aca0a2be252843e729f32e2b8ff9f3d02c77ba43e06d6f5a9229916
- evidence_id: original-review-3
  kind: prior_review
  reference: reviews/structured/20261022T084807Z-mim-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T15:49:50Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 6f1170d640c261dca83cb7003770c16b9181a00e841a49eadeff057bd0748785
- evidence_id: current-record-4
  kind: record_content
  reference: data/structures/other/mis12_mind_type_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T15:49:50Z'
  support: context_only
  summary: Original frozen SHA256 6b16e919810eceb24433ded999d28a548adbb8c5e0d55af4eb63fe3e4eaac1a6;
    current SHA256 029ac75e12045a39ff6da937c63cff087715e76aadf1b65ad773f30bdfc4e944.
    Changed record reassessed against current sources.
  snapshot_sha256: 029ac75e12045a39ff6da937c63cff087715e76aadf1b65ad773f30bdfc4e944
- evidence_id: original-review-4
  kind: prior_review
  reference: reviews/structured/20261022T084808Z-mis12-mind-type-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T15:49:50Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: b155982f70cb3c45961366da6da82566a268839b6d3ef6f916a390c04719c39f
- evidence_id: current-record-5
  kind: record_content
  reference: data/structures/other/mitochondrial_inner_membrane_peptidase_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T15:49:50Z'
  support: context_only
  summary: Original frozen SHA256 8eb6f174c969fc2aef5a84a2a473fe42a66158531ae26422ccfd8ae3407227e0;
    current SHA256 8eb6f174c969fc2aef5a84a2a473fe42a66158531ae26422ccfd8ae3407227e0.
    Record bytes unchanged since the original review.
  snapshot_sha256: 8eb6f174c969fc2aef5a84a2a473fe42a66158531ae26422ccfd8ae3407227e0
- evidence_id: original-review-5
  kind: prior_review
  reference: reviews/structured/20261022T084808Z-mitochondrial-inner-membrane-peptidase-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T15:49:50Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 5ec6c6f0d6b3aad3d0388740337689e5fab22a2a0e52b42f17ccd95e858ed9dc
- evidence_id: current-record-6
  kind: record_content
  reference: data/structures/other/mitochondrial_lon_protease_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T15:49:50Z'
  support: context_only
  summary: Original frozen SHA256 22c985cbd94a32e0a04e1ba4b7f77e796ef99815390b9165a3b15b987429d5d6;
    current SHA256 22c985cbd94a32e0a04e1ba4b7f77e796ef99815390b9165a3b15b987429d5d6.
    Record bytes unchanged since the original review.
  snapshot_sha256: 22c985cbd94a32e0a04e1ba4b7f77e796ef99815390b9165a3b15b987429d5d6
- evidence_id: original-review-6
  kind: prior_review
  reference: reviews/structured/20261022T084809Z-mitochondrial-lon-protease-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T15:49:50Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 45c479278c71463c35d945a3042c7275494464a564b7f16595ca190e42c0ca38
- evidence_id: current-record-7
  kind: record_content
  reference: data/structures/other/mitochondrial_multifunctional_assembly.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T15:49:50Z'
  support: context_only
  summary: Original frozen SHA256 bb1a36eee48a44140250e04951a42f149f5de60affd5e146ba8f89f8a6e48858;
    current SHA256 bb1a36eee48a44140250e04951a42f149f5de60affd5e146ba8f89f8a6e48858.
    Record bytes unchanged since the original review.
  snapshot_sha256: bb1a36eee48a44140250e04951a42f149f5de60affd5e146ba8f89f8a6e48858
- evidence_id: original-review-7
  kind: prior_review
  reference: reviews/structured/20261022T084810Z-mitochondrial-multifunctional-assembly-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T15:49:50Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: b8b8e993357ca73262007d2b28664ed80d09cdbd06c88cbc8466b759c36ce7d4
- evidence_id: current-record-8
  kind: record_content
  reference: data/structures/other/mitochondrial_outer_membrane_translocase_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T15:49:50Z'
  support: context_only
  summary: Original frozen SHA256 a9facce19eda1794aefb3bef7b36fe07ba5c3a942220a4379c5569de4150022e;
    current SHA256 a9facce19eda1794aefb3bef7b36fe07ba5c3a942220a4379c5569de4150022e.
    Record bytes unchanged since the original review.
  snapshot_sha256: a9facce19eda1794aefb3bef7b36fe07ba5c3a942220a4379c5569de4150022e
- evidence_id: original-review-8
  kind: prior_review
  reference: reviews/structured/20261022T084810Z-mitochondrial-outer-membrane-translocase-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T15:49:50Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 72a7419c81e55ff10873a91cfddab435d2d646018402fc578dcfda39d7d8def0
- evidence_id: current-record-9
  kind: record_content
  reference: data/structures/other/mitochondrial_prohibitin_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T15:49:50Z'
  support: context_only
  summary: Original frozen SHA256 a2a0c89fc814c0dba32ef8a1b90246ced003e274382c67d78794cbd86e9b7453;
    current SHA256 a2a0c89fc814c0dba32ef8a1b90246ced003e274382c67d78794cbd86e9b7453.
    Record bytes unchanged since the original review.
  snapshot_sha256: a2a0c89fc814c0dba32ef8a1b90246ced003e274382c67d78794cbd86e9b7453
- evidence_id: original-review-9
  kind: prior_review
  reference: reviews/structured/20261022T084811Z-mitochondrial-prohibitin-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T15:49:50Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: d9157ec12ac92d7f92166d6921a1542bdc796a7ce9cf4c7bb81dd1e3c4efd17f
- evidence_id: micro-record-0
  kind: record_content
  reference: data/structures/other/mic10_subcomplex.yaml
  locator: Complete current maintained record at source HEAD
  accessed_at: '2026-11-04T15:38:03.539550Z'
  support: context_only
  summary: All identity, taxa, components/examples, function/evidence, every graph
    edge, discussions/history and images where present were read. Current bytes match
    reviewed main. Target is nonstale against its original frozen input.
  snapshot_sha256: 9d98461e5b91bf4eb28fffe1797678d45d3f6aa51391b289282b7b6155a22601
- evidence_id: micro-prior-0
  kind: prior_review
  reference: reviews/structured/20261022T084805Z-mic10-subcomplex-audit/review.yaml
  locator: Complete immutable original YAML and derived Markdown; findings/actions/checks/evidence
    scopes
  accessed_at: '2026-11-04T15:38:03.539633Z'
  support: context_only
  summary: Original qualified pass has no scientific findings or actions. Original
    source access, all formal checks and limitations reassessed; fresh retrieval does
    not retrospectively upgrade historical observations.
  snapshot_sha256: 8b9b5b2e1275daa508b1f23bf797a2890fbdc1fd0c0fcdc0254cfdbcbee22271
- evidence_id: micro-record-1
  kind: record_content
  reference: data/structures/other/mic60_mic19_complex.yaml
  locator: Complete current maintained record at source HEAD
  accessed_at: '2026-11-04T15:38:03.539666Z'
  support: context_only
  summary: All identity, taxa, components/examples, function/evidence, every graph
    edge, discussions/history and images where present were read. Current bytes match
    reviewed main. Target is nonstale against its original frozen input.
  snapshot_sha256: f69ade5a57e4946d6bb529c33ab623059348fd9a4c43609cea0b33b50d591cb7
- evidence_id: micro-prior-1
  kind: prior_review
  reference: reviews/structured/20261022T084806Z-mic60-mic19-complex-audit/review.yaml
  locator: Complete immutable original YAML and derived Markdown; findings/actions/checks/evidence
    scopes
  accessed_at: '2026-11-04T15:38:03.539687Z'
  support: context_only
  summary: Original qualified pass has no scientific findings or actions. Original
    source access, all formal checks and limitations reassessed; fresh retrieval does
    not retrospectively upgrade historical observations.
  snapshot_sha256: 86cf74dfa21d30946634247871ef5bacc3a360b821de2fba53a3b5d2327efd5f
- evidence_id: micro-record-2
  kind: record_content
  reference: data/structures/other/micos_complex.yaml
  locator: Complete current maintained record at source HEAD
  accessed_at: '2026-11-04T15:38:03.539715Z'
  support: context_only
  summary: All identity, taxa, components/examples, function/evidence, every graph
    edge, discussions/history and images where present were read. Current bytes match
    reviewed main. MICOS changed only by reciprocal has_part links and appended history.
  snapshot_sha256: 756a5b48fd9109266e6ace5805f5f9fd4aaac9940ff39660960bb8603374f5aa
- evidence_id: micro-prior-2
  kind: prior_review
  reference: reviews/structured/20261022T084806Z-micos-complex-audit/review.yaml
  locator: Complete immutable original YAML and derived Markdown; findings/actions/checks/evidence
    scopes
  accessed_at: '2026-11-04T15:38:03.539733Z'
  support: context_only
  summary: Original qualified pass has no scientific findings or actions. Original
    source access, all formal checks and limitations reassessed; fresh retrieval does
    not retrospectively upgrade historical observations.
  snapshot_sha256: fe076d23b6e6b8cce8b3e5e73f3b2f3288f19f305d2084684b64468eb77328d4
- evidence_id: micro-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Components, evidence and append-only discussion rules
  accessed_at: '2026-11-04T15:38:03.539762Z'
  support: context_only
  summary: Exact family/class scope, supported positive claims and preserved historical
    rationale; optional missing examples or component rows are not automatic defects.
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
- evidence_id: micro-schema
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Evidence, component type/essentiality, graph relations and image definitions
  accessed_at: '2026-11-04T15:38:03.539783Z'
  support: context_only
  summary: Formation is distinct from activity and viability; families/complex nodes
    may be represented. snippet is verbatim-only, notes is paraphrase. No universal
    knockout requirement follows.
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: micro-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Native graph review contract
  accessed_at: '2026-11-04T15:38:03.539811Z'
  support: context_only
  summary: Check actual actor/edge/grounding and explicitly bounded mechanism/function
    scope without demanding unasserted mechanisms.
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: micro-native-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Complete native read-only workflow and structured-source applicability
  accessed_at: '2026-11-04T15:38:03.539828Z'
  support: context_only
  summary: Positive molecular and pathway claims trigger bounded source assessment
    regardless of whether an expression-module claim is asserted.
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: micro-native-config
  kind: authority
  reference: conf/record_review.yaml
  locator: Native configured review requirements
  accessed_at: '2026-11-04T15:38:03.539846Z'
  support: context_only
  summary: Root owns whole-corpus gates and successor publication; this scratch review
    does not certify future gates.
  snapshot_sha256: d3334a12b8a616a7638f1195748085d2b543fba7df67ad4ff8fcc0ac18f2d3ee
- evidence_id: micro-original-audit
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/original-audit.json
  locator: Six actual native validate/render commands and 44 historical input occurrences
  accessed_at: '2026-11-04T15:31:48.373142Z'
  support: supports
  summary: All six commands exited zero and each rendered Markdown equals the immutable
    original. Six original artifact bytes match the original PR commit; declared historical
    input hashes match exact source revisions. Current targets match source and main,
    with exactly one stale assigned target.
  snapshot_sha256: 7dc067ce3be4913cf360751fd0956a70b071cdcbe03096ec6e431027fdb4283c
- evidence_id: micro-micos-stale-delta
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/micos_complex-historical-current.diff
  locator: Actual original declared source to current source Git diff
  accessed_at: '2026-11-04T15:38:03.539940Z'
  support: supports
  summary: Only appended 2026-10-30 parthood history and has_part links to the two
    assigned subcomplex records changed. No component, function, graph or experimental
    source assertion changed.
  snapshot_sha256: e713d2440d22bc5d3fdeba77e410208ed09c9410af7426c4d657d56afc9cecdd
- evidence_id: micro-protein-P38341-retry
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P38341?format=json
  locator: Native accession/status, complete gene tokens/taxon/name; FUNCTION, SUBUNIT,
    SUBCELLULAR LOCATION and SIMILARITY comments; relevant InterPro/Pfam/SGD references;
    raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/protein-P38341-retry.raw
  accessed_at: '2026-11-04T15:26:03.131795Z'
  support: supports
  summary: 'P38341: reviewed MICOS complex subunit MIC12; taxon 559292; genes [{''geneName'':
    {''value'': ''MIC12''}, ''synonyms'': [{''value'': ''AIM5''}, {''value'': ''FMP51''},
    {''value'': ''MCS12''}], ''orderedLocusNames'': [{''value'': ''YBR262C''}], ''orfNames'':
    [{''value'': ''YBR1731''}]}]. Native identity/location annotations remain distinct
    from directly inspected primary formation or experiment-strain evidence.'
  snapshot_sha256: 55ae602ece92f04bf808b2749dbfcb5323f0af846790a0ccbd797c3d93c746f4
- evidence_id: micro-protein-P50087-retry
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P50087?format=json
  locator: Native accession/status, complete gene tokens/taxon/name; FUNCTION, SUBUNIT,
    SUBCELLULAR LOCATION and SIMILARITY comments; relevant InterPro/Pfam/SGD references;
    raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/protein-P50087-retry.raw
  accessed_at: '2026-11-04T15:26:12.483157Z'
  support: supports
  summary: 'P50087: reviewed MICOS subunit MIC26; taxon 559292; genes [{''geneName'':
    {''value'': ''MIC26''}, ''synonyms'': [{''value'': ''MCS29''}, {''value'': ''MIO27''},
    {''value'': ''MOS2''}], ''orderedLocusNames'': [{''value'': ''YGR235C''}], ''orfNames'':
    [{''value'': ''G8575''}]}]. Native identity/location annotations remain distinct
    from directly inspected primary formation or experiment-strain evidence.'
  snapshot_sha256: 6365334c7faf01e4d923fa4593b5bbd92dc6e4ae702b8c95a82d78f6bde871e3
- evidence_id: micro-protein-P50945-retry
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P50945?format=json
  locator: Native accession/status, complete gene tokens/taxon/name; FUNCTION, SUBUNIT,
    SUBCELLULAR LOCATION and SIMILARITY comments; relevant InterPro/Pfam/SGD references;
    raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/protein-P50945-retry.raw
  accessed_at: '2026-11-04T15:26:07.931823Z'
  support: supports
  summary: 'P50945: reviewed MICOS complex subunit MIC27; taxon 559292; genes [{''geneName'':
    {''value'': ''MIC27''}, ''synonyms'': [{''value'': ''AIM37''}, {''value'': ''MCS27''}],
    ''orderedLocusNames'': [{''value'': ''YNL100W''}], ''orfNames'': [{''value'':
    ''N2190''}]}]. Native identity/location annotations remain distinct from directly
    inspected primary formation or experiment-strain evidence.'
  snapshot_sha256: a0ec0c1970e1b102f16f9aec68028e1ad98ed4d0dbb8995c2180501e382f8660
- evidence_id: micro-protein-P36112-retry
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P36112?format=json
  locator: Native accession/status, complete gene tokens/taxon/name; FUNCTION, SUBUNIT,
    SUBCELLULAR LOCATION and SIMILARITY comments; relevant InterPro/Pfam/SGD references;
    raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/protein-P36112-retry.raw
  accessed_at: '2026-11-04T15:26:22.499497Z'
  support: supports
  summary: 'P36112: reviewed MICOS complex subunit MIC60; taxon 559292; genes [{''geneName'':
    {''value'': ''MIC60''}, ''synonyms'': [{''value'': ''AIM28''}, {''value'': ''FCJ1''},
    {''value'': ''FMP13''}], ''orderedLocusNames'': [{''value'': ''YKR016W''}]}].
    Native identity/location annotations remain distinct from directly inspected primary
    formation or experiment-strain evidence.'
  snapshot_sha256: c9fa6b91f6cf8673dc3c316bf4321c1023f0505dbb2eac77bc619724b1c3c460
- evidence_id: micro-protein-P43594-retry
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P43594?format=json
  locator: Native accession/status, complete gene tokens/taxon/name; FUNCTION, SUBUNIT,
    SUBCELLULAR LOCATION and SIMILARITY comments; relevant InterPro/Pfam/SGD references;
    raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/protein-P43594-retry.raw
  accessed_at: '2026-11-04T15:26:31.621107Z'
  support: supports
  summary: 'P43594: reviewed MICOS complex subunit MIC19; taxon 559292; genes [{''geneName'':
    {''value'': ''MIC19''}, ''synonyms'': [{''value'': ''AIM13''}, {''value'': ''MCS19''}],
    ''orderedLocusNames'': [{''value'': ''YFR011C''}]}]. Native identity/location
    annotations remain distinct from directly inspected primary formation or experiment-strain
    evidence.'
  snapshot_sha256: 1944520b92c5b51f6d7624d1171ca7c0c15efda400ee37fb68b39f5fdc0fbf60
- evidence_id: micro-protein-Q96VH5-final
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q96VH5.txt
  locator: Complete current UniProt flat file, including identity/gene/taxon, bibliography,
    FUNCTION/SUBUNIT/LOCATION/SIMILARITY and family references; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/protein-Q96VH5-final.raw
  accessed_at: '2026-11-04T15:31:18.295839Z'
  support: supports
  summary: Q96VH5 is reviewed MIC10, aliases MCS10/MIO10/MOS1, locus YCL057C-A, S288c559292;
    IPR007512. Native annotation is not an independent new primary experiment.
  snapshot_sha256: 3547824c3e1d6a00f65f94be7c5b50130d5f3fff06a72fc50a6bad66b58b61d2
- evidence_id: micro-query-MIC10-retry
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AMIC10%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100&fields=accession%2Cid%2Cprotein_name%2Cgene_names%2Corganism_id%2Creviewed
  locator: Complete exact gene/taxon/reviewed response and total-results/Link headers;
    raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/query-MIC10-retry.raw
  accessed_at: '2026-11-04T15:26:23.175300Z'
  support: supports
  summary: One current reviewed accession Q96VH5, matching primary gene MIC10 and
    taxon 559292. No next page. Current uniqueness does not reconstruct the dated
    October selection.
  snapshot_sha256: ced1e5cc4815b1c177e482d22752d28614741bff41d823bc586ef4462a9724b0
  search_scope: UniProtKB; query (gene_exact:MIC10) AND (organism_id:559292) AND (reviewed:true);
    actual access 2026-11-04T15:26:23.175300Z; bound First100 identities; total and
    Link inspected; no historical-query reconstruction; only the retrieved response
    was inspected.
- evidence_id: micro-query-MIC12-retry
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AMIC12%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100&fields=accession%2Cid%2Cprotein_name%2Cgene_names%2Corganism_id%2Creviewed
  locator: Complete exact gene/taxon/reviewed response and total-results/Link headers;
    raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/query-MIC12-retry.raw
  accessed_at: '2026-11-04T15:26:23.860718Z'
  support: supports
  summary: One current reviewed accession P38341, matching primary gene MIC12 and
    taxon 559292. No next page. Current uniqueness does not reconstruct the dated
    October selection.
  snapshot_sha256: 3195533aed1f368529f69440f8df3cad36c9fe1c03ab92f7471df6cdac7928b2
  search_scope: UniProtKB; query (gene_exact:MIC12) AND (organism_id:559292) AND (reviewed:true);
    actual access 2026-11-04T15:26:23.860718Z; bound First100 identities; total and
    Link inspected; no historical-query reconstruction; only the retrieved response
    was inspected.
- evidence_id: micro-query-MIC26-final
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AMIC26+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=100&fields=accession%2Cid%2Cprotein_name%2Cgene_names%2Corganism_id%2Creviewed
  locator: Complete exact gene/taxon/reviewed response and total-results/Link headers;
    raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/query-MIC26-final.raw
  accessed_at: '2026-11-04T15:31:19.039352Z'
  support: supports
  summary: One current reviewed accession P50087, matching primary gene MIC26 and
    taxon 559292. No next page. Current uniqueness does not reconstruct the dated
    October selection.
  snapshot_sha256: 312d6afa6fb10fa6814c02b1e7b0713f728f01040be8df05ed3b0d6d093472dd
  search_scope: UniProtKB; query gene_exact:MIC26 AND organism_id:559292 AND reviewed:true;
    actual access 2026-11-04T15:31:19.039352Z; bound First100 response rows and pagination
    headers; primary-name and alias membership distinguished; only the retrieved response
    was inspected.
- evidence_id: micro-query-MIC27-retry
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AMIC27%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100&fields=accession%2Cid%2Cprotein_name%2Cgene_names%2Corganism_id%2Creviewed
  locator: Complete exact gene/taxon/reviewed response and total-results/Link headers;
    raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/query-MIC27-retry.raw
  accessed_at: '2026-11-04T15:26:32.297987Z'
  support: supports
  summary: One current reviewed accession P50945, matching primary gene MIC27 and
    taxon 559292. No next page. Current uniqueness does not reconstruct the dated
    October selection.
  snapshot_sha256: 6e1d8eef50f13460ceb0074913d831269818d64f5144a20a1729ac01c8769a12
  search_scope: UniProtKB; query (gene_exact:MIC27) AND (organism_id:559292) AND (reviewed:true);
    actual access 2026-11-04T15:26:32.297987Z; bound First100 identities; total and
    Link inspected; no historical-query reconstruction; only the retrieved response
    was inspected.
- evidence_id: micro-query-MIC60-final
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AMIC60+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=100&fields=accession%2Cid%2Cprotein_name%2Cgene_names%2Corganism_id%2Creviewed
  locator: Complete exact gene/taxon/reviewed response and total-results/Link headers;
    raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/query-MIC60-final.raw
  accessed_at: '2026-11-04T15:31:19.194597Z'
  support: supports
  summary: One current reviewed accession P36112, matching primary gene MIC60 and
    taxon 559292. No next page. Current uniqueness does not reconstruct the dated
    October selection.
  snapshot_sha256: d12cad1e6007da2b77db4379de641626bea16b42ca1c6068d5abe301ed400edb
  search_scope: UniProtKB; query gene_exact:MIC60 AND organism_id:559292 AND reviewed:true;
    actual access 2026-11-04T15:31:19.194597Z; bound First100 response rows and pagination
    headers; primary-name and alias membership distinguished; only the retrieved response
    was inspected.
- evidence_id: micro-query-MIC19-retry
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AMIC19%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100&fields=accession%2Cid%2Cprotein_name%2Cgene_names%2Corganism_id%2Creviewed
  locator: Complete exact gene/taxon/reviewed response and total-results/Link headers;
    raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/query-MIC19-retry.raw
  accessed_at: '2026-11-04T15:26:52.714520Z'
  support: supports
  summary: One current reviewed accession P43594, matching primary gene MIC19 and
    taxon 559292. No next page. Current uniqueness does not reconstruct the dated
    October selection.
  snapshot_sha256: 4d725794383c7d4939ada7647a64cbde1cfa5120b0babf86d2e8135a2f4dde30
  search_scope: UniProtKB; query (gene_exact:MIC19) AND (organism_id:559292) AND (reviewed:true);
    actual access 2026-11-04T15:26:52.714520Z; bound First100 identities; total and
    Link inspected; no historical-query reconstruction; only the retrieved response
    was inspected.
- evidence_id: micro-ipr-IPR007512
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007512/
  locator: Native name/type, complete description, relevant hierarchy and member signatures;
    description quality flags; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/ipr-IPR007512.raw
  accessed_at: '2026-11-04T15:24:58.860303Z'
  support: supports
  summary: 'IPR007512: MICOS complex subunit Mic10, type family. Exact Mic10 family.
    No sequence alignment or exhaustive alternate-family search performed.'
  snapshot_sha256: ab29d06d5609772f1f3e50501fff0100ee0aa7b9e928c9478eb2c1d47a1b6a7c
- evidence_id: micro-ipr-IPR031463
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR031463/
  locator: Native name/type, complete description, relevant hierarchy and member signatures;
    description quality flags; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/ipr-IPR031463.raw
  accessed_at: '2026-11-04T15:24:58.900226Z'
  support: supports
  summary: 'IPR031463: MICOS complex subunit Mic12, type family. Exact Mic12 family,
    with historical conditional three-protein subcomplex description. No sequence
    alignment or exhaustive alternate-family search performed.'
  snapshot_sha256: 42330e9a7b9b096f72c5d9f57c49451bb537c680955090510772535a9b4d2a2a
- evidence_id: micro-ipr-IPR033181
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR033181/
  locator: Native name/type, complete description, relevant hierarchy and member signatures;
    description quality flags; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/ipr-IPR033181.raw
  accessed_at: '2026-11-04T15:24:58.948906Z'
  support: supports
  summary: 'IPR033181: MICOS subunit Mic26, fungi, type family. Explicit fungal Mic26
    branch, not a universal Mic26/Mic27 identity. No sequence alignment or exhaustive
    alternate-family search performed.'
  snapshot_sha256: 2f775ac76a18b7528dabd08c88fb488eb8fc79607b8aeadfc6f70520ad23456a
- evidence_id: micro-ipr-IPR061953
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR061953/
  locator: Native name/type, complete description, relevant hierarchy and member signatures;
    description quality flags; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/ipr-IPR061953.raw
  accessed_at: '2026-11-04T15:24:59.484926Z'
  support: supports
  summary: 'IPR061953: MICOS complex subunit MIC27, type family. Explicit Saccharomycetaceae
    Mic27 family. No sequence alignment or exhaustive alternate-family search performed.'
  snapshot_sha256: ae494915a8e34830ed37899163aebe9ca500fa4058bd6b54f997b4d981bc6f12
- evidence_id: micro-ipr-IPR019133-retry
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR019133/?format=json
  locator: Native name/type, complete description, relevant hierarchy and member signatures;
    description quality flags; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/ipr-IPR019133-retry.raw
  accessed_at: '2026-11-04T15:26:53.361135Z'
  support: supports
  summary: 'IPR019133: MICOS complex subunit MIC60, type family. Exact Mic60 family;
    description domain coordinates are not automatically transferred between taxa.
    No sequence alignment or exhaustive alternate-family search performed.'
  snapshot_sha256: bf189fb5296d703e434561bc0d826555c4776d259e10cf8a6244b9fcf173f704
- evidence_id: micro-ipr-IPR012471-retry
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR012471/?format=json
  locator: Native name/type, complete description, relevant hierarchy and member signatures;
    description quality flags; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/ipr-IPR012471-retry.raw
  accessed_at: '2026-11-04T15:26:53.964584Z'
  support: supports
  summary: 'IPR012471: Protein of unknown function DUF1690, type family. Family of
    uncharacterised fungal proteins (DUF1690), not authority wording establishing
    the exact universal Mic19 class. No sequence alignment or exhaustive alternate-family
    search performed.'
  snapshot_sha256: 5e4f68a1a0a6fc4efd55783af5cdb597dd4ff682aa609b318903706dea6097c4
- evidence_id: micro-tax-4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete native taxon name/rank/lineage response; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/tax-4932.raw
  accessed_at: '2026-11-04T15:25:00.107062Z'
  support: supports
  summary: '4932: Saccharomyces cerevisiae, rank species. Species/reference strain
    is not substituted for W303, YPH499 or thermophilic source proteins.'
  snapshot_sha256: 38f43dd1593a1d47416228ae385464f30aeb8302c3aadb45b3588d03744bc814
- evidence_id: micro-tax-559292
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Complete native taxon name/rank/lineage response; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/tax-559292.raw
  accessed_at: '2026-11-04T15:25:00.127326Z'
  support: supports
  summary: '559292: Saccharomyces cerevisiae S288C, rank strain. Species/reference
    strain is not substituted for W303, YPH499 or thermophilic source proteins.'
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: micro-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005743,GO:0007007,GO:0042407,GO:0044284,GO:0061617,GO:0098800
  locator: 'All six exact current GO terms: status, full definitions/synonyms and
    returned typed child links; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/go.raw'
  accessed_at: '2026-11-04T15:25:00.127276Z'
  support: supports
  summary: GO0061617 remains exact MICOS identity with six named yeast subunits; GO0098800
    is the broader inner-membrane protein-complex parent, GO0005743 containing membrane,
    GO0044284 junction, GO0007007 organization and GO0042407 cristae formation. Active
    terms, no is_a/parthood interchange.
  snapshot_sha256: 7feda646ceb37901f4677dca468967f261a101f7ec889d8b1e55bfdeb6d4d1d1
- evidence_id: micro-GO0061617-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0061617/ancestors?relations=is_a
  locator: Complete is_a-only ancestor response; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/GO0061617-ancestors.raw
  accessed_at: '2026-11-04T15:25:00.689829Z'
  support: supports
  summary: Confirms the appropriate generic membrane protein-complex ancestry; does
    not turn either source-defined subcomplex into the whole MICOS identity.
  snapshot_sha256: e6f9a39da7ac6ffd1bfca81307ca76b14809ce311be653cda42c59d532de915f
- evidence_id: micro-GO0098800-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0098800/ancestors?relations=is_a
  locator: Complete is_a-only ancestor response; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/GO0098800-ancestors.raw
  accessed_at: '2026-11-04T15:25:00.712132Z'
  support: supports
  summary: Confirms the appropriate generic membrane protein-complex ancestry; does
    not turn either source-defined subcomplex into the whole MICOS identity.
  snapshot_sha256: f7a208c3ea7d1d4089346bf9061280714675a9f6a09b7b5c4c906374b32e0a87
- evidence_id: micro-go-search-Mic10
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=Mic10&limit=100&page=1
  locator: Complete first page and hit/page counts; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/go-search-Mic10.raw
  accessed_at: '2026-11-04T15:31:18.484561Z'
  support: supports
  summary: The specified current QuickGO text query returned zero hits. This bounded
    query supports retaining the existing source-defined minted identity but does
    not prove global ontology absence under every synonym.
  snapshot_sha256: f3a7dae9b1e9335291e3940cdf0e5f8dadf9335da7b9547710606b5106c63f86
  search_scope: QuickGO ontology search; query Mic10; actual access 2026-11-04T15:31:18.484561Z;
    bound First100 returned terms page1; inspect total hits/pages, do not infer global
    ontology absence; only the retrieved response was inspected.
- evidence_id: micro-go-search-Mic60-Mic19
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=Mic60+Mic19&limit=100&page=1
  locator: Complete first page and hit/page counts; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/go-search-Mic60-Mic19.raw
  accessed_at: '2026-11-04T15:31:18.489657Z'
  support: supports
  summary: The specified current QuickGO text query returned zero hits. This bounded
    query supports retaining the existing source-defined minted identity but does
    not prove global ontology absence under every synonym.
  snapshot_sha256: f3a7dae9b1e9335291e3940cdf0e5f8dadf9335da7b9547710606b5106c63f86
  search_scope: QuickGO ontology search; query Mic60 Mic19; actual access 2026-11-04T15:31:18.489657Z;
    bound First100 returned terms page1; inspect total hits/pages, do not infer global
    ontology absence; only the retrieved response was inspected.
- evidence_id: micro-bock2022-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1126%2Fsciadv.abo4946%22+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact MED bibliographic identity, authors/DOI and complete indexed abstract;
    raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/bock2022-meta.raw
  accessed_at: '2026-11-04T15:25:01.445312Z'
  support: context_only
  summary: Structural insights into crista junction formation by the Mic60-Mic19 complex.;
    authors Bock-Bierbaum T, Funck K, Wollweber F, Lisicki E, von der Malsburg K,
    von der Malsburg A, Laborenz J, Noel JK, Hessenberger M, Jungbluth S, Bernert
    C, Kunz S, Riedel D, Lilie H, Jakobs S, van der Laan M, Daumke O.; PMID36044574,
    DOI10.1126/sciadv.abo4946. Complete abstract and metadata read; no body claim
    unless separately listed. Pfanner 2014 is nomenclature synthesis rather than an
    independent primary experiment.
  snapshot_sha256: 363357e44438b8b02e786c58652142f15a23c80d9aa7c8086ef298ab9588191d
  search_scope: Europe PMC; query DOI:"10.1126/sciadv.abo4946" AND SRC:MED; actual
    access 2026-11-04T15:25:01.445312Z; bound First10 full core records; exact DOI
    identity and hitCount checked; only the retrieved response was inspected.
- evidence_id: micro-friedman2015-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.7554%2Felife.07739%22+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact MED bibliographic identity, authors/DOI and complete indexed abstract;
    raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/friedman2015-meta.raw
  accessed_at: '2026-11-04T15:25:01.431237Z'
  support: context_only
  summary: MICOS coordinates with respiratory complexes and lipids to establish mitochondrial
    inner membrane architecture.; authors Friedman JR, Mourier A, Yamada J, McCaffery
    JM, Nunnari J.; PMID25918844, DOI10.7554/elife.07739. Complete abstract and metadata
    read; no body claim unless separately listed. Pfanner 2014 is nomenclature synthesis
    rather than an independent primary experiment.
  snapshot_sha256: 1bbfb911c15787b255963135b326634f075b9edf3bc6b8b8167f96288850e91a
  search_scope: Europe PMC; query DOI:"10.7554/elife.07739" AND SRC:MED; actual access
    2026-11-04T15:25:01.431237Z; bound First10 full core records; exact DOI identity
    and hitCount checked; only the retrieved response was inspected.
- evidence_id: micro-harner2011-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Femboj.2011.379%22+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact MED bibliographic identity, authors/DOI and complete indexed abstract;
    raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/harner2011-meta.raw
  accessed_at: '2026-11-04T15:25:01.587975Z'
  support: context_only
  summary: The mitochondrial contact site complex, a determinant of mitochondrial
    architecture.; authors Harner M, Körner C, Walther D, Mokranjac D, Kaesmacher
    J, Welsch U, Griffith J, Mann M, Reggiori F, Neupert W.; PMID22009199, DOI10.1038/emboj.2011.379.
    Complete abstract and metadata read; no body claim unless separately listed. Pfanner
    2014 is nomenclature synthesis rather than an independent primary experiment.
  snapshot_sha256: e6febb3b2b26d0415bfa9308ea5e663dba0eb8f5503ed5a4b410311c0e42bc5e
  search_scope: Europe PMC; query DOI:"10.1038/emboj.2011.379" AND SRC:MED; actual
    access 2026-11-04T15:25:01.587975Z; bound First10 full core records; exact DOI
    identity and hitCount checked; only the retrieved response was inspected.
- evidence_id: micro-hessenberger2017-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fncomms15258%22+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact MED bibliographic identity, authors/DOI and complete indexed abstract;
    raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/hessenberger2017-meta.raw
  accessed_at: '2026-11-04T15:25:01.759829Z'
  support: context_only
  summary: Regulated membrane remodeling by Mic60 controls formation of mitochondrial
    crista junctions.; authors Hessenberger M, Zerbes RM, Rampelt H, Kunz S, Xavier
    AH, Purfürst B, Lilie H, Pfanner N, van der Laan M, Daumke O.; PMID28561061, DOI10.1038/ncomms15258.
    Complete abstract and metadata read; no body claim unless separately listed. Pfanner
    2014 is nomenclature synthesis rather than an independent primary experiment.
  snapshot_sha256: 9613f8421a6f1ecc3f433474fd62235fea3b9b71645f9417db86d3230915e52b
  search_scope: Europe PMC; query DOI:"10.1038/ncomms15258" AND SRC:MED; actual access
    2026-11-04T15:25:01.759829Z; bound First10 full core records; exact DOI identity
    and hitCount checked; only the retrieved response was inspected.
- evidence_id: micro-hoppins2011-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1083%2Fjcb.201107053%22+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact MED bibliographic identity, authors/DOI and complete indexed abstract;
    raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/hoppins2011-meta.raw
  accessed_at: '2026-11-04T15:25:01.973440Z'
  support: context_only
  summary: A mitochondrial-focused genetic interaction map reveals a scaffold-like
    complex required for inner membrane organization in mitochondria.; authors Hoppins
    S, Collins SR, Cassidy-Stone A, Hummel E, Devay RM, Lackner LL, Westermann B,
    Schuldiner M, Weissman JS, Nunnari J.; PMID21987634, DOI10.1083/jcb.201107053.
    Complete abstract and metadata read; no body claim unless separately listed. Pfanner
    2014 is nomenclature synthesis rather than an independent primary experiment.
  snapshot_sha256: 4ad07bbe0bdcc386180fef9b66269e9e8b9f6c1c86fb556c206aaa92e1a9a5ee
  search_scope: Europe PMC; query DOI:"10.1083/jcb.201107053" AND SRC:MED; actual
    access 2026-11-04T15:25:01.973440Z; bound First10 full core records; exact DOI
    identity and hitCount checked; only the retrieved response was inspected.
- evidence_id: micro-malsburg2011-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.devcel.2011.08.026%22+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact MED bibliographic identity, authors/DOI and complete indexed abstract;
    raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/malsburg2011-meta.raw
  accessed_at: '2026-11-04T15:25:01.706005Z'
  support: context_only
  summary: Dual role of mitofilin in mitochondrial membrane organization and protein
    biogenesis.; authors von der Malsburg K, Müller JM, Bohnert M, Oeljeklaus S, Kwiatkowska
    P, Becker T, Loniewska-Lwowska A, Wiese S, Rao S, Milenkovic D, Hutu DP, Zerbes
    RM, Schulze-Specking A, Meyer HE, Martinou JC, Rospert S, Rehling P, Meisinger
    C, Veenhuis M, Warscheid B, van der Klei IJ, Pfanner N, Chacinska A, van der Laan
    M.; PMID21944719, DOI10.1016/j.devcel.2011.08.026. Complete abstract and metadata
    read; no body claim unless separately listed. Pfanner 2014 is nomenclature synthesis
    rather than an independent primary experiment.
  snapshot_sha256: ddb1d7db24e40c8e63628cd274d128f7cdd10ecb70ff8effcb1081d5935eb141
  search_scope: Europe PMC; query DOI:"10.1016/j.devcel.2011.08.026" AND SRC:MED;
    actual access 2026-11-04T15:25:01.706005Z; bound First10 full core records; exact
    DOI identity and hitCount checked; only the retrieved response was inspected.
- evidence_id: micro-pfanner2014-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1083%2Fjcb.201401006%22+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact MED bibliographic identity, authors/DOI and complete indexed abstract;
    raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/pfanner2014-meta.raw
  accessed_at: '2026-11-04T15:25:01.650326Z'
  support: context_only
  summary: Uniform nomenclature for the mitochondrial contact site and cristae organizing
    system.; authors Pfanner N, van der Laan M, Amati P, Capaldi RA, Caudy AA, Chacinska
    A, Darshi M, Deckers M, Hoppins S, Icho T, Jakobs S, Ji J, Kozjak-Pavlovic V,
    Meisinger C, Odgren PR, Park SK, Rehling P, Reichert AS, Sheikh MS, Taylor SS,
    Tsuchida N, van der Bliek AM, van der Klei IJ, Weissman JS, Westermann B, Zha
    J, Neupert W, Nunnari J.; PMID24687277, DOI10.1083/jcb.201401006. Complete abstract
    and metadata read; no body claim unless separately listed. Pfanner 2014 is nomenclature
    synthesis rather than an independent primary experiment.
  snapshot_sha256: c6d6f4cd773ddabdd5795b423dee38f5f278e404ecc1f293449293ae365abae8
  search_scope: Europe PMC; query DOI:"10.1083/jcb.201401006" AND SRC:MED; actual
    access 2026-11-04T15:25:01.650326Z; bound First10 full core records; exact DOI
    identity and hitCount checked; only the retrieved response was inspected.
- evidence_id: micro-rampelt2018-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.jmb.2018.04.037%22+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact MED bibliographic identity, authors/DOI and complete indexed abstract;
    raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/rampelt2018-meta.raw
  accessed_at: '2026-11-04T15:25:00.930843Z'
  support: context_only
  summary: Assembly of the Mitochondrial Cristae Organizer Mic10 Is Regulated by Mic26-Mic27
    Antagonism and Cardiolipin.; authors Rampelt H, Wollweber F, Gerke C, de Boer
    R, van der Klei IJ, Bohnert M, Pfanner N, van der Laan M.; PMID29733859, DOI10.1016/j.jmb.2018.04.037.
    Complete abstract and metadata read; no body claim unless separately listed. Pfanner
    2014 is nomenclature synthesis rather than an independent primary experiment.
  snapshot_sha256: b4af4560d149bf975a47dead669989a20c63e83f148d97e695f163aca69f1597
  search_scope: Europe PMC; query DOI:"10.1016/j.jmb.2018.04.037" AND SRC:MED; actual
    access 2026-11-04T15:25:00.930843Z; bound First10 full core records; exact DOI
    identity and hitCount checked; only the retrieved response was inspected.
- evidence_id: micro-tirrell2020-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1083%2Fjcb.202003024%22+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact MED bibliographic identity, authors/DOI and complete indexed abstract;
    raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/tirrell2020-meta.raw
  accessed_at: '2026-11-04T15:25:01.442159Z'
  support: context_only
  summary: MICOS subcomplexes assemble independently on the mitochondrial inner membrane
    in proximity to ER contact sites.; authors Tirrell PS, Nguyen KN, Luby-Phelps
    K, Friedman JR.; PMID33053165, DOI10.1083/jcb.202003024. Complete abstract and
    metadata read; no body claim unless separately listed. Pfanner 2014 is nomenclature
    synthesis rather than an independent primary experiment.
  snapshot_sha256: 27560fc0b13850af7e643a3b2932e98d05911b1c1a23438064137f302a9ad5a3
  search_scope: Europe PMC; query DOI:"10.1083/jcb.202003024" AND SRC:MED; actual
    access 2026-11-04T15:25:01.442159Z; bound First10 full core records; exact DOI
    identity and hitCount checked; only the retrieved response was inspected.
- evidence_id: micro-pmid-14562095
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact MED bibliographic identity, authors/DOI and complete indexed abstract;
    raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/pmid-14562095.raw
  accessed_at: '2026-11-04T15:25:00.814861Z'
  support: context_only
  summary: Global analysis of protein localization in budding yeast.; authors Huh
    WK, Falvo JV, Gerke LC, Carroll AS, Howson RW, Weissman JS, O'Shea EK.; PMID14562095,
    DOI10.1038/nature02026. Complete abstract and metadata read; no body claim unless
    separately listed. Pfanner 2014 is nomenclature synthesis rather than an independent
    primary experiment.
  snapshot_sha256: 2ca60d2255a2d3bbc82faa247ab30b1c6d1fee57858075f22a949bf82e01bf23
  search_scope: Europe PMC; query EXT_ID:14562095 AND SRC:MED; actual access 2026-11-04T15:25:00.814861Z;
    bound First10 full core records; exact single MED identity expected, inspect hitCount;
    only the retrieved response was inspected.
- evidence_id: micro-pmid-16823961
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A16823961+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact MED bibliographic identity, authors/DOI and complete indexed abstract;
    raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/pmid-16823961.raw
  accessed_at: '2026-11-04T15:25:00.743487Z'
  support: context_only
  summary: 'Toward the complete yeast mitochondrial proteome: multidimensional separation
    techniques for mitochondrial proteomics.; authors Reinders J, Zahedi RP, Pfanner
    N, Meisinger C, Sickmann A.; PMID16823961, DOI10.1021/pr050477f. Complete abstract
    and metadata read; no body claim unless separately listed. Pfanner 2014 is nomenclature
    synthesis rather than an independent primary experiment.'
  snapshot_sha256: a6c7b3633d37594f1c9e5ecd7c5304e1db7cf4ff625fe19cee3e0df7056f0cf5
  search_scope: Europe PMC; query EXT_ID:16823961 AND SRC:MED; actual access 2026-11-04T15:25:00.743487Z;
    bound First10 full core records; exact single MED identity expected, inspect hitCount;
    only the retrieved response was inspected.
- evidence_id: micro-pmid-19528297
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A19528297+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact MED bibliographic identity, authors/DOI and complete indexed abstract;
    raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/pmid-19528297.raw
  accessed_at: '2026-11-04T15:25:00.808704Z'
  support: context_only
  summary: Formation of cristae and crista junctions in mitochondria depends on antagonism
    between Fcj1 and Su e/g.; authors Rabl R, Soubannier V, Scholz R, Vogel F, Mendl
    N, Vasiljev-Neumeyer A, Körner C, Jagasia R, Keil T, Baumeister W, Cyrklaff M,
    Neupert W, Reichert AS.; PMID19528297, DOI10.1083/jcb.200811099. Complete abstract
    and metadata read; no body claim unless separately listed. Pfanner 2014 is nomenclature
    synthesis rather than an independent primary experiment.
  snapshot_sha256: d1f20730cf9f1dad3e4debe47a6d4625b2a4739bfafceae45c6ccdb9df708399
  search_scope: Europe PMC; query EXT_ID:19528297 AND SRC:MED; actual access 2026-11-04T15:25:00.808704Z;
    bound First10 full core records; exact single MED identity expected, inspect hitCount;
    only the retrieved response was inspected.
- evidence_id: micro-pmid-21944719
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A21944719+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact MED bibliographic identity, authors/DOI and complete indexed abstract;
    raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/pmid-21944719.raw
  accessed_at: '2026-11-04T15:25:00.960137Z'
  support: context_only
  summary: Dual role of mitofilin in mitochondrial membrane organization and protein
    biogenesis.; authors von der Malsburg K, Müller JM, Bohnert M, Oeljeklaus S, Kwiatkowska
    P, Becker T, Loniewska-Lwowska A, Wiese S, Rao S, Milenkovic D, Hutu DP, Zerbes
    RM, Schulze-Specking A, Meyer HE, Martinou JC, Rospert S, Rehling P, Meisinger
    C, Veenhuis M, Warscheid B, van der Klei IJ, Pfanner N, Chacinska A, van der Laan
    M.; PMID21944719, DOI10.1016/j.devcel.2011.08.026. Complete abstract and metadata
    read; no body claim unless separately listed. Pfanner 2014 is nomenclature synthesis
    rather than an independent primary experiment.
  snapshot_sha256: 6c1390ac2afb181f071b262087aa09832083651570cc5a6c016beea8feaf7c12
  search_scope: Europe PMC; query EXT_ID:21944719 AND SRC:MED; actual access 2026-11-04T15:25:00.960137Z;
    bound First10 full core records; exact single MED identity expected, inspect hitCount;
    only the retrieved response was inspected.
- evidence_id: micro-pmid-21987634
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A21987634+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact MED bibliographic identity, authors/DOI and complete indexed abstract;
    raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/pmid-21987634.raw
  accessed_at: '2026-11-04T15:25:00.960193Z'
  support: context_only
  summary: A mitochondrial-focused genetic interaction map reveals a scaffold-like
    complex required for inner membrane organization in mitochondria.; authors Hoppins
    S, Collins SR, Cassidy-Stone A, Hummel E, Devay RM, Lackner LL, Westermann B,
    Schuldiner M, Weissman JS, Nunnari J.; PMID21987634, DOI10.1083/jcb.201107053.
    Complete abstract and metadata read; no body claim unless separately listed. Pfanner
    2014 is nomenclature synthesis rather than an independent primary experiment.
  snapshot_sha256: dc8d5766c52ee5679bbf42016b42409a780d08bc732162bc4ea0729d65c245cd
  search_scope: Europe PMC; query EXT_ID:21987634 AND SRC:MED; actual access 2026-11-04T15:25:00.960193Z;
    bound First10 full core records; exact single MED identity expected, inspect hitCount;
    only the retrieved response was inspected.
- evidence_id: micro-rampelt2018-pdf
  kind: primary_source
  reference: https://pure.rug.nl/ws/portalfiles/portal/61925901/1_s2.0_S0022283618303498_main_1_.pdf
  locator: Genuine institutional PDF extracted text lines1–360, main printed pages1883–1888
    including Figures1–4 text captions and embedded methods; no figure pixels or unread
    references/supplements; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/rampelt2018-pdf.raw
  accessed_at: '2026-11-04T15:25:02.749216Z'
  support: supports
  summary: YPH499 glycerol-grown mitochondria, native gels and crosslinking support
    Mic26/Mic27 antagonism affecting Mic10 oligomers; normal four-component module
    differs from conditional three-component core. Cardiolipin stabilizes oligomers;
    direct binding site and universal copy count are not established.
  snapshot_sha256: ab7cea45265d46407c5a46e2b7583204e4970cb11848f40b3ee90c8015fc688b
- evidence_id: micro-friedman2015-s3
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4434539.1/PMC4434539.1.xml
  locator: Genuine JATS Results s2-2,s2-3,s2-4,s2-5,s2-7 and Methods s4-1,s4-3,s4-6
    fully read with embedded captions; only Figure3 pixels separately inspected; raw
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/friedman2015-s3.raw
  accessed_at: '2026-11-04T15:25:01.994646Z'
  support: supports
  summary: W303 conditional deletion/reconstitution, fluorescence and crosslinked
    co-IP/MS distinguish Mic60 and Mic10/12/27 subcomplexes. Mic10 requirement for
    Mic27 foci differs from Mic12 reduction; Mic26 not recovered in the conditional
    core does not erase normal membership. Crista proximity inferred from fluorescent
    markers after unsuccessful direct immuno-EM, not direct junction localization
    proof. ERMES/lipids are not automatically constituents.
  snapshot_sha256: 8d1082e98a558176fbd86c80851d3467e7bf41c986f38b8dfe00810c3903a345
- evidence_id: micro-tirrell2020-s3
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC7545361.1/PMC7545361.1.xml
  locator: Genuine JATS sections s3,s4,s11 fully read, embedded Figure1/2/S1/S2 and
    video captions; no movies, pixels, separate supplements or other sections; raw
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/tirrell2020-s3.raw
  accessed_at: '2026-11-04T15:25:02.004358Z'
  support: supports
  summary: 'W303 and explicitly separate BY4741/42 bypass contexts: Mic10 module assembly
    depends on ERMES function; Vps13 bypass restores organization. Mic60 self-assembles
    independently. Proximity and functional rescue do not prove obligatory direct-template
    binding or add ERMES/Vps13 as subunits.'
  snapshot_sha256: 4e324acdda30eea63bf8270ce518c9cc025592e26c25be7fed3b1f1816c1516e
- evidence_id: micro-hessenberger2017-s3
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5460017.1/PMC5460017.1.xml
  locator: Genuine JATS sections Mic60 binds and remodels liposomes; Mic19 binds to
    Mic60 and enhances membrane remodelling; LBS1 plays a critical role in IM ultrastructure
    and function; Discussion; Expression and purification; EM; Yeast strains and plasmids;
    full Figure4 caption/pixels; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/hessenberger2017-s3.raw
  accessed_at: '2026-11-04T15:25:02.048548Z'
  support: supports
  summary: Purified C. thermophilum Mic60sol208–691 and Mic19 in Folch liposomes support
    direct interaction, lipid recruitment and tubulation enhancement, with engineered/domain-specific
    limits. YPH499 mutant/cristae/respiratory assays are separate. Leakage readout
    is not physiological permeability; native universal 4:4/barrier is not proved.
  snapshot_sha256: 4eeed50b9775cf66c10da792beee738a1b58eddcdc2cdb4e1b834e51530b01a9
- evidence_id: micro-bock2022-s3
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC9432830.1/PMC9432830.1.xml
  locator: Genuine JATS entire RESULTS four subsections plus embedded Figures2–4 captions,
    DISCUSSION/Figure5 caption, Cloning and plasmids, S.cerevisiae strains and plasmids,
    Isolation of S.cerevisiae mitochondria; no pixels/supplements/raw density; raw
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/bock2022-s3.raw
  accessed_at: '2026-11-04T15:25:02.285543Z'
  support: supports
  summary: L. thermotolerans coiled-coil and engineered C. thermophilum Mic60/Mic19
    constructs support a tetramer/heteromer model; YPH499 validation is distinct.
    Suggested strut/barrier architecture remains a model, native filament identity
    unresolved, and these constructs do not establish universal native4:4 stoichiometry.
  snapshot_sha256: c9616b327ecf7dbde015063529b4171b75cfe49109389f690bcea92929de4b2d
- evidence_id: micro-hoppins2011-s3
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3198156.1/PMC3198156.1.xml
  locator: Genuine JATS Results sections6–9 by retained section index (Fcj1-containing
    complex; conserved inner membrane complex; inner membrane organization; complex
    structures), Discussion, Yeast strains generation and manipulation, complete Proteomic
    analysis and Electron microscopy analysis; embedded captions only; raw snapshot
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/hoppins2011-s3.raw
  accessed_at: '2026-11-04T15:25:02.151693Z'
  support: supports
  summary: W303 tagged purifications/proteomics identify six subunits and suborganization.
    Deletion/ultrathin sections and tomography find residual junctions, so the paper
    explicitly does not establish universal junction-formation essentiality. Inner
    membrane scaffold/maintenance and contact interactions support the current qualified
    FUNCTION graph; direct native architecture is not resolved.
  snapshot_sha256: dcd377d56a3d97af8ce498222fa7efa9baf6ad79ffe718270e11cf1c55ae5731
- evidence_id: micro-pfanner2014-s3
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3971754.1/PMC3971754.1.xml
  locator: Complete body, Figure1 textual caption and Table1 nomenclature including
    all naming guidelines; no figure pixels; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/pfanner2014-s3.raw
  accessed_at: '2026-11-04T15:25:02.275367Z'
  support: supports
  summary: Consensus nomenclature unifies MICOS/MINOS/MitOS and six yeast names; mammalian
    extra Mic25 and lineage differences are explicit. This is secondary/nomenclature
    authority, not new formation experiment.
  snapshot_sha256: 82b64f6831dbd08211d69769fc6670263bbad616fb94bfe9e3455e4b66660922
- evidence_id: micro-friedman2015-fig3
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4434539.1/elife07739f003.jpg
  locator: Actual complete multipanel pixels viewed in maintained file; fresh source
    image is byte-identical; caption/licence read in corresponding JATS; raw snapshot
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/friedman2015-fig3.raw
  accessed_at: '2026-11-04T15:25:02.499838Z'
  support: supports
  summary: Contextual cellular/mutant assays, not a purified molecular-complex image.
    Figure3 A–G includes W303 confocal deletion/reconstitution, foci counts and peptide
    co-purification; record scope/OTHER modality is accurate. Article permissions
    explicitly CC BY 4.0; relevant caption contains no contrary third-party credit.
  snapshot_sha256: af23bf8f6f0e98c05adf50c869b1a63705423d54278c9af60657b308361189c8
- evidence_id: micro-image-0
  kind: record_content
  reference: data/images/other/mic10_subcomplex/pmc4434539_fig3.jpg
  locator: Actual maintained image bytes and independently viewed complete panels
  accessed_at: '2026-11-04T15:38:03.546471Z'
  support: context_only
  summary: Fresh source bytes equal maintained file_sha256; full-panel scope and licence/attribution
    checked against current genuine JATS. No new OA package MD5 query was made.
  snapshot_sha256: af23bf8f6f0e98c05adf50c869b1a63705423d54278c9af60657b308361189c8
- evidence_id: micro-hessenberger2017-fig4
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5460017.1/ncomms15258-f4.jpg
  locator: Actual complete multipanel pixels viewed in maintained file; fresh source
    image is byte-identical; caption/licence read in corresponding JATS; raw snapshot
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/hessenberger2017-fig4.raw
  accessed_at: '2026-11-04T15:25:02.651118Z'
  support: supports
  summary: Contextual cellular/mutant assays, not a purified molecular-complex image.
    Figure4 a–i includes YPH499 affinity/growth, cryo-TEM c–f with500 nm scale bars,
    junction counts and respiratory activities; full-multipanel OTHER modality and
    contextual scope are accurate. Article permissions explicitly CC BY 4.0; relevant
    caption contains no contrary third-party credit.
  snapshot_sha256: 4a86dfab5f2d4d49925989b9566c18ffac1d087292f5ece4cd0dedcf9cf36954
- evidence_id: micro-image-1
  kind: record_content
  reference: data/images/other/mic60_mic19_complex/pmc5460017_f4.jpg
  locator: Actual maintained image bytes and independently viewed complete panels
  accessed_at: '2026-11-04T15:38:03.546885Z'
  support: context_only
  summary: Fresh source bytes equal maintained file_sha256; full-panel scope and licence/attribution
    checked against current genuine JATS. No new OA package MD5 query was made.
  snapshot_sha256: 4a86dfab5f2d4d49925989b9566c18ffac1d087292f5ece4cd0dedcf9cf36954
- evidence_id: micro-harner2011-s3
  kind: validation
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3230385.1/PMC3230385.1.xml
  locator: Actual status/response only; no scientific body claim; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/harner2011-s3.raw
  accessed_at: '2026-11-04T15:25:02.064754Z'
  support: context_only
  summary: HTTP 404, bytes 320; unavailable/rate-limited/timeout/challenge. Harner
    legacy HTTP200 is a reCAPTCHA page, not article text. Genuine successful alternate
    responses have separate dates/hashes.
  snapshot_sha256: 9e5448dd34087119a6463d93e5d487794f6dfaf549a808e4fd090acdc7e7d7ee
- evidence_id: micro-harner2011-legacy
  kind: validation
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3230385/
  locator: Actual status/response only; no scientific body claim; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/harner2011-legacy.raw
  accessed_at: '2026-11-04T15:26:54.227514Z'
  support: context_only
  summary: HTTP 200, bytes 21411; unavailable/rate-limited/timeout/challenge. Harner
    legacy HTTP200 is a reCAPTCHA page, not article text. Genuine successful alternate
    responses have separate dates/hashes.
  snapshot_sha256: ce09a23af9d6148d1b18d1c7f0f4bc7f676568d269b1c9283f66ce60764b50cc
- evidence_id: micro-protein-Q96VH5
  kind: validation
  reference: https://rest.uniprot.org/uniprotkb/Q96VH5.json
  locator: Actual status/response only; no scientific body claim; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/protein-Q96VH5.raw
  accessed_at: '2026-11-04T15:25:00.178075Z'
  support: context_only
  summary: HTTP 503, bytes 286; unavailable/rate-limited/timeout/challenge. Harner
    legacy HTTP200 is a reCAPTCHA page, not article text. Genuine successful alternate
    responses have separate dates/hashes.
  snapshot_sha256: f1a0576cbed49302685e2c089f3a899dd4ef09b9f639340e550fabfe60096d82
- evidence_id: micro-protein-Q96VH5-retry
  kind: validation
  reference: https://rest.uniprot.org/uniprotkb/Q96VH5?format=json
  locator: Actual status/response only; no scientific body claim; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/protein-Q96VH5-retry.raw
  accessed_at: '2026-11-04T15:26:47.291684Z'
  support: context_only
  summary: HTTP None, bytes 0; unavailable/rate-limited/timeout/challenge. Harner
    legacy HTTP200 is a reCAPTCHA page, not article text. Genuine successful alternate
    responses have separate dates/hashes.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: micro-ipr-IPR019133
  kind: validation
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR019133/
  locator: Actual status/response only; no scientific body claim; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/ipr-IPR019133.raw
  accessed_at: '2026-11-04T15:24:59.488912Z'
  support: context_only
  summary: HTTP 429, bytes 61; unavailable/rate-limited/timeout/challenge. Harner
    legacy HTTP200 is a reCAPTCHA page, not article text. Genuine successful alternate
    responses have separate dates/hashes.
  snapshot_sha256: 9abf9cb941ee77b8e8a3348aa3517c7fbb81c7ae7cb580ff9d1b87961335b26f
- evidence_id: micro-ipr-IPR012471
  kind: validation
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR012471/
  locator: Actual status/response only; no scientific body claim; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/ipr-IPR012471.raw
  accessed_at: '2026-11-04T15:24:59.540539Z'
  support: context_only
  summary: HTTP 429, bytes 61; unavailable/rate-limited/timeout/challenge. Harner
    legacy HTTP200 is a reCAPTCHA page, not article text. Genuine successful alternate
    responses have separate dates/hashes.
  snapshot_sha256: 9abf9cb941ee77b8e8a3348aa3517c7fbb81c7ae7cb580ff9d1b87961335b26f
- evidence_id: micro-query-MIC26-retry
  kind: validation
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AMIC26%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100&fields=accession%2Cid%2Cprotein_name%2Cgene_names%2Corganism_id%2Creviewed
  locator: Actual status/response only; no scientific body claim; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/query-MIC26-retry.raw
  accessed_at: '2026-11-04T15:27:09.305166Z'
  support: context_only
  summary: HTTP None, bytes 0; unavailable/rate-limited/timeout/challenge. Harner
    legacy HTTP200 is a reCAPTCHA page, not article text. Genuine successful alternate
    responses have separate dates/hashes.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
  search_scope: UniProtKB; query (gene_exact:MIC26) AND (organism_id:559292) AND (reviewed:true);
    actual access 2026-11-04T15:27:09.305166Z; bound First100 identities; total and
    Link inspected; no historical-query reconstruction; only the retrieved response
    was inspected.
- evidence_id: micro-query-MIC60-retry
  kind: validation
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AMIC60%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100&fields=accession%2Cid%2Cprotein_name%2Cgene_names%2Corganism_id%2Creviewed
  locator: Actual status/response only; no scientific body claim; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/query-MIC60-retry.raw
  accessed_at: '2026-11-04T15:27:17.755164Z'
  support: context_only
  summary: HTTP None, bytes 0; unavailable/rate-limited/timeout/challenge. Harner
    legacy HTTP200 is a reCAPTCHA page, not article text. Genuine successful alternate
    responses have separate dates/hashes.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
  search_scope: UniProtKB; query (gene_exact:MIC60) AND (organism_id:559292) AND (reviewed:true);
    actual access 2026-11-04T15:27:17.755164Z; bound First100 identities; total and
    Link inspected; no historical-query reconstruction; only the retrieved response
    was inspected.
- evidence_id: micro-retrieval-index
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/source-receipts.json
  locator: All48 actual initial authorized retrieval receipts; earlier sandbox DNS
    failures separately retained in initial-sandbox-dns-attempt
  accessed_at: '2026-11-04T15:38:03.547574Z'
  support: context_only
  summary: Index records actual URLs/statuses/response hashes and times; failed UniProt/InterPro
    entries are not biological evidence. Successful retry receipts are separately
    bound in the individual evidence rows.
  snapshot_sha256: 07a6e054f2b088f89e93a10f4606f6c6db955dabcb477661da3f5b5a508cabb9
- evidence_id: micro-adapter-catalogue
  kind: search
  reference: https://imodulondb.org/api/organisms
  locator: Complete official organism/dataset response; raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/adapter-catalogue.raw
  accessed_at: '2026-11-04T15:24:16.251933Z'
  support: supports
  summary: All 20 organisms and 28 dataset entries inspected. No Saccharomyces or
    other relevant fungal/metazoan biological-host dataset appears; bacterial recombinant
    expression is not a host proxy. All three records are applicable because they
    make positive molecular/pathway assertions. No foreign-host gene/module queries
    or expression-to-assembly inference.
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  search_scope: Official iModulonDB catalogue; query GET /api/organisms; complete
    returned organism/dataset catalogue; actual access 2026-11-04T15:24:16.251933Z;
    bound One complete current response; actual biological hosts only, no recombinant-host
    proxy; only the retrieved response was inspected.
- evidence_id: micro-native-mic10_subcomplex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mic10_subcomplex-uniprot-verify-receipt.json
  locator: Full actual command receipt; complete stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mic10_subcomplex-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T15:22:24.272266Z'
  support: supports
  summary: 4 reviewed S288C protein examples and4 COVERED typed nodes. Native exit0
    checks accession/coverage, not primary membership or physical formation.
  snapshot_sha256: 7aebd5ff0195fbd647ee99e72917ab058664b5e7cb5be3c473ff8b78b3c4a656
- evidence_id: micro-native-mic10_subcomplex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mic10_subcomplex-uniprot-causal-receipt.json
  locator: Full actual command receipt; complete stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mic10_subcomplex-uniprot-causal.log
    SHA256 6c1d97f2cb25045ddae5e20a9aa6562b9fa6be6961f961243b68c041557dc83c
  accessed_at: '2026-11-04T15:22:24.723493Z'
  support: supports
  summary: 4 reviewed S288C protein examples and4 COVERED typed nodes. Native exit0
    checks accession/coverage, not primary membership or physical formation.
  snapshot_sha256: 5246338dd94178009f27ba0f24da8903403f4f016f9a076587bc3406c030a8cd
- evidence_id: micro-native-mic60_mic19_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mic60_mic19_complex-uniprot-verify-receipt.json
  locator: Full actual command receipt; complete stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mic60_mic19_complex-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T15:22:25.970378Z'
  support: supports
  summary: 2 reviewed S288C protein examples and2 COVERED typed nodes. Native exit0
    checks accession/coverage, not primary membership or physical formation.
  snapshot_sha256: 3822a20c74733ba73e8a16e7aba94a09577f9e488bd2d4d6dd749df33c7b6a06
- evidence_id: micro-native-mic60_mic19_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mic60_mic19_complex-uniprot-causal-receipt.json
  locator: Full actual command receipt; complete stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mic60_mic19_complex-uniprot-causal.log
    SHA256 22d7a0d901ab4f94314139e8db344060d6646aebc95400a3456ce381afa664b4
  accessed_at: '2026-11-04T15:22:26.389998Z'
  support: supports
  summary: 2 reviewed S288C protein examples and2 COVERED typed nodes. Native exit0
    checks accession/coverage, not primary membership or physical formation.
  snapshot_sha256: ce2b5b8d3da5857d5205debc920694eabf78cb984cd7345142b8d95dc01b70d7
- evidence_id: micro-native-micos_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/micos_complex-uniprot-verify-receipt.json
  locator: Full actual command receipt; complete stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/micos_complex-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T15:22:26.805708Z'
  support: supports
  summary: 0 protein examples and0 typed GENE_OR_PROTEIN nodes; empty check is not
    molecular validation. Native exit0 checks accession/coverage, not primary membership
    or physical formation.
  snapshot_sha256: 2e299566227aaf1aedfee426ab3095d05c7689be86081250439f8c21b0746b39
- evidence_id: micro-native-micos_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/micos_complex-uniprot-causal-receipt.json
  locator: Full actual command receipt; complete stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/micos_complex-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-04T15:22:27.216934Z'
  support: supports
  summary: 0 protein examples and0 typed GENE_OR_PROTEIN nodes; empty check is not
    molecular validation. Native exit0 checks accession/coverage, not primary membership
    or physical formation.
  snapshot_sha256: e5b68dfa0820668ea5691fba4e6c4674244a3e84395b6ab9a1d4309c8483c4bb
- evidence_id: micro-historical-harner-access
  kind: validation
  reference: reviews/structured/20261022T084806Z-micos-complex-audit/review.yaml
  locator: Immutable original evidence access-PMC3230385-xml
  accessed_at: '2026-11-04T15:38:03.548133Z'
  support: context_only
  summary: Historical kind authority/context_only actually describes HTTP500 transport
    only. Original URL=https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3230385/fullTextXML;
    access=2026-10-22T08:08:06.830531Z; response SHA=ff1bf7f29cdfbc01884ed64e7196167b6065c7d2b29c3f5d47cb6d98f01adc8d;
    original summary=Harner2011 XML route returnedHTTP500; the native bibliography
    and complete abstract were read separately. No primary body was inspected from
    this response.. No old source bytes are newly retrieved or upgraded. Successor
    should classify validation/context_only while retaining original provenance.
  snapshot_sha256: fe076d23b6e6b8cce8b3e5e73f3b2f3288f19f305d2084684b64468eb77328d4
- evidence_id: plaque-record-3
  kind: record_content
  reference: data/structures/other/mim_complex.yaml
  locator: Entire current maintained record, all fields/graphs/history; source HEAD
    c9fe63bdff984abad241949c21dab3b13e975d1f
  accessed_at: '2026-11-04T15:43:22.639944Z'
  support: context_only
  summary: Current complete record read; old frozen SHA dc0d4007dfe5d82f22b45d46cc12e3c934ce3ebe92d7ed7b48c25be1ea715c5f;
    current SHA 61bfb31d9aca0a2be252843e729f32e2b8ff9f3d02c77ba43e06d6f5a9229916.
  snapshot_sha256: 61bfb31d9aca0a2be252843e729f32e2b8ff9f3d02c77ba43e06d6f5a9229916
- evidence_id: plaque-original-3
  kind: prior_review
  reference: reviews/structured/20261022T084807Z-mim-complex-audit/review.yaml
  locator: Complete original YAML and paired Markdown, scientific findings/actions,
    declared access and historical input ownership
  accessed_at: '2026-11-04T15:43:22.639944Z'
  support: context_only
  summary: Original observation retained without changing historical evidence or promoting
    its old executions to fresh results.
  snapshot_sha256: 6f1170d640c261dca83cb7003770c16b9181a00e841a49eadeff057bd0748785
- evidence_id: plaque-record-4
  kind: record_content
  reference: data/structures/other/mis12_mind_type_complex.yaml
  locator: Entire current maintained record, all fields/graphs/history; source HEAD
    c9fe63bdff984abad241949c21dab3b13e975d1f
  accessed_at: '2026-11-04T15:43:22.639944Z'
  support: context_only
  summary: Current complete record read; old frozen SHA 6b16e919810eceb24433ded999d28a548adbb8c5e0d55af4eb63fe3e4eaac1a6;
    current SHA 029ac75e12045a39ff6da937c63cff087715e76aadf1b65ad773f30bdfc4e944.
  snapshot_sha256: 029ac75e12045a39ff6da937c63cff087715e76aadf1b65ad773f30bdfc4e944
- evidence_id: plaque-original-4
  kind: prior_review
  reference: reviews/structured/20261022T084808Z-mis12-mind-type-complex-audit/review.yaml
  locator: Complete original YAML and paired Markdown, scientific findings/actions,
    declared access and historical input ownership
  accessed_at: '2026-11-04T15:43:22.639944Z'
  support: context_only
  summary: Original observation retained without changing historical evidence or promoting
    its old executions to fresh results.
  snapshot_sha256: b155982f70cb3c45961366da6da82566a268839b6d3ef6f916a390c04719c39f
- evidence_id: plaque-record-5
  kind: record_content
  reference: data/structures/other/mitochondrial_inner_membrane_peptidase_complex.yaml
  locator: Entire current maintained record, all fields/graphs/history; source HEAD
    c9fe63bdff984abad241949c21dab3b13e975d1f
  accessed_at: '2026-11-04T15:43:22.639944Z'
  support: context_only
  summary: Current complete record read; old frozen SHA 8eb6f174c969fc2aef5a84a2a473fe42a66158531ae26422ccfd8ae3407227e0;
    current SHA 8eb6f174c969fc2aef5a84a2a473fe42a66158531ae26422ccfd8ae3407227e0.
  snapshot_sha256: 8eb6f174c969fc2aef5a84a2a473fe42a66158531ae26422ccfd8ae3407227e0
- evidence_id: plaque-original-5
  kind: prior_review
  reference: reviews/structured/20261022T084808Z-mitochondrial-inner-membrane-peptidase-complex-audit/review.yaml
  locator: Complete original YAML and paired Markdown, scientific findings/actions,
    declared access and historical input ownership
  accessed_at: '2026-11-04T15:43:22.639944Z'
  support: context_only
  summary: Original observation retained without changing historical evidence or promoting
    its old executions to fresh results.
  snapshot_sha256: 5ec6c6f0d6b3aad3d0388740337689e5fab22a2a0e52b42f17ccd95e858ed9dc
- evidence_id: plaque-policy
  kind: record_content
  reference: docs/CURATION.md
  locator: Evidence/snippet contract; taxon-agnostic component classes, reviewed-label
    grounding, formation versus function and append-only discussion rationale
  accessed_at: '2026-11-04T15:43:22.639944Z'
  support: context_only
  summary: Frozen native requirements independently applied, including actual access
    scope and optional-field limits.
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
- evidence_id: plaque-schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Current component, essentiality, graph-node and evidence fields
  accessed_at: '2026-11-04T15:43:22.639944Z'
  support: context_only
  summary: Frozen native requirements independently applied, including actual access
    scope and optional-field limits.
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: plaque-review-policy
  kind: record_content
  reference: docs/record-reviews.md
  locator: Complete native provenance, checks, finding lineage, verdict and save contract
  accessed_at: '2026-11-04T15:43:22.639944Z'
  support: context_only
  summary: Frozen native requirements independently applied, including actual access
    scope and optional-field limits.
  snapshot_sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
- evidence_id: plaque-profile
  kind: record_content
  reference: docs/record-review-profile.md
  locator: Complete local review profile
  accessed_at: '2026-11-04T15:43:22.639944Z'
  support: context_only
  summary: Frozen native requirements independently applied, including actual access
    scope and optional-field limits.
  snapshot_sha256: 6a49c8d35f0a94082a9ad0b8bd8c6a929d85de8339141955f3779bd7ab0eb7e4
- evidence_id: plaque-skill
  kind: record_content
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Complete single-record skill, whole-record structured-source triggers and
    bounded search rules
  accessed_at: '2026-11-04T15:43:22.639944Z'
  support: context_only
  summary: Frozen native requirements independently applied, including actual access
    scope and optional-field limits.
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: plaque-original-native-checks
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/original-checks.json
  locator: All three actual original validate/render commands; historical input hashes;
    current 51 frozen inputs
  accessed_at: '2026-11-04T15:43:22.639944Z'
  support: supports
  summary: Three original pairs validate and render byte-identically, all their historical
    inputs match retained Git revisions, and all 51 current input hashes match source
    and worktree. Receipt contains actual command times and logs.
  snapshot_sha256: c5c4ad13f752ab5835d0345912ebc6ded397d36b10bf01553558152c3edaab58
- evidence_id: plaque-delta-3
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/t3-stale.diff
  locator: Exact old frozen record to current source diff
  accessed_at: '2026-11-04T15:43:22.639944Z'
  support: context_only
  summary: Substantive changed claims independently assessed; original review unchanged.
  snapshot_sha256: ffd8e4ec1fddf075a6030edc425fb25ae5054dd9577de8d210476c9339cec0bf
- evidence_id: plaque-delta-4
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/t4-stale.diff
  locator: Exact old frozen record to current source diff
  accessed_at: '2026-11-04T15:43:22.639944Z'
  support: context_only
  summary: Substantive changed claims independently assessed; original review unchanged.
  snapshot_sha256: 4f0c40e0d5b48684038eb70e91f26cbc4a8fbd74cad8e79db340f205ea9525f0
- evidence_id: plaque-native-mim_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mim_complex-uniprot-verify-receipt.json
  locator: Actual command receipt; separate stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mim_complex-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T15:22:28.355218Z'
  support: supports
  summary: Actual exit0 at current source; 2 reviewed examples and 2 COVERED nodes.
  snapshot_sha256: b4648b3f0d690a4cc034eadde11532059567c47c524fc514f91845a2568e1b95
- evidence_id: plaque-native-mim_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mim_complex-uniprot-causal-receipt.json
  locator: Actual command receipt; separate stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mim_complex-uniprot-causal.log
    SHA256 4d2fc324bc37f34d33055b3b2a52a9e6d8020dd8c109abbf7d0cf67d8ff88743
  accessed_at: '2026-11-04T15:22:28.763785Z'
  support: supports
  summary: Actual exit0 at current source; 2 reviewed examples and 2 COVERED nodes.
  snapshot_sha256: 17bfbe935a70353b03c010cc3807e900b54f6d3cc5fc169f14d5046b5bfc2803
- evidence_id: plaque-native-mis12_mind_type_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mis12_mind_type_complex-uniprot-verify-receipt.json
  locator: Actual command receipt; separate stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mis12_mind_type_complex-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T15:22:29.944370Z'
  support: supports
  summary: 'Actual exit0 at current source; 4 reviewed examples; 5 typed nodes: 2
    COVERED, 2 PARTIAL_EXAMPLES for MIS12/PMF1 class symbols, and 1 UNANCHORED_WITH_UNIPROT
    external outer-kinetochore actor.'
  snapshot_sha256: babde09daa0c129bc8f44448b50ae3097503bddcc6d4f1dd25d93a92f45f6342
- evidence_id: plaque-native-mis12_mind_type_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mis12_mind_type_complex-uniprot-causal-receipt.json
  locator: Actual command receipt; separate stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mis12_mind_type_complex-uniprot-causal.log
    SHA256 fad6678665a9bc3509cf409f377cc2e2229d22e04659cf35e9025cb818052429
  accessed_at: '2026-11-04T15:22:30.362007Z'
  support: supports
  summary: 'Actual exit0 at current source; 4 reviewed examples; 5 typed nodes: 2
    COVERED, 2 PARTIAL_EXAMPLES for MIS12/PMF1 class symbols, and 1 UNANCHORED_WITH_UNIPROT
    external outer-kinetochore actor.'
  snapshot_sha256: 9c0d25a0831c30230d9789ed14480ba1880ecfd12bbb8ccd4b5257333e57a649
- evidence_id: plaque-native-mitochondrial_inner_membrane_peptidase_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_inner_membrane_peptidase_complex-uniprot-verify-receipt.json
  locator: Actual command receipt; separate stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_inner_membrane_peptidase_complex-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T15:22:30.760888Z'
  support: supports
  summary: Actual exit0 at current source; 0 examples and 0 typed nodes; empty inventory
    is not scientific completeness proof.
  snapshot_sha256: c52731fda0c6e23f1c411c503fca31121e0a501dea043206cac368405288385b
- evidence_id: plaque-native-mitochondrial_inner_membrane_peptidase_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_inner_membrane_peptidase_complex-uniprot-causal-receipt.json
  locator: Actual command receipt; separate stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_inner_membrane_peptidase_complex-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-04T15:22:31.162273Z'
  support: supports
  summary: Actual exit0 at current source; 0 examples and 0 typed nodes; empty inventory
    is not scientific completeness proof.
  snapshot_sha256: 167fb50aec4a23789ceda50330663304b8bfa7fa790eb7b304b7783bf3df79fd
- evidence_id: plaque-go-0000444-parents
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000444/ancestors?relations=is_a,part_of
  locator: Complete requested ancestor response; mixed is_a/part_of traversal is transitive
    context, not an assertion of a direct edge. Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0000444-parents.raw
    SHA256 4cfb74a00e09da5aa1ce323dfb9f23b49616831d5ece5126bf77ca56276cc80e; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0000444-parents.receipt.json
    SHA256 1f633db068997205aba5039117bb8159c7e8a62372b4f771118dfcd9e7e6d1fd.
  accessed_at: '2026-11-04T15:28:39.097319Z'
  support: supports
  summary: Current GO authority for 0000444; exact identity and anatomical/function
    scope assessed without converting transitive ancestors into direct parthood.
  snapshot_sha256: 4cfb74a00e09da5aa1ce323dfb9f23b49616831d5ece5126bf77ca56276cc80e
- evidence_id: plaque-go-0000444
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000444
  locator: Exact current term identity, definition, obsolete flag, synonym qualifier
    strings and typed children where present. Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0000444.raw
    SHA256 9fed03461fbad8116800ebf65bc0e08646d504abeb84f859b14e23cc836cbc2a; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0000444.receipt.json
    SHA256 64dd80e0fb2d6dcef5c0ceb25f25ae5dcccbc3ee3432f1108e5daccee78beb96.
  accessed_at: '2026-11-04T15:26:33.598418Z'
  support: supports
  summary: Current GO authority for 0000444; exact identity and anatomical/function
    scope assessed without converting transitive ancestors into direct parthood.
  snapshot_sha256: 9fed03461fbad8116800ebf65bc0e08646d504abeb84f859b14e23cc836cbc2a
- evidence_id: plaque-go-0000776
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000776
  locator: Exact current term identity, definition, obsolete flag, synonym qualifier
    strings and typed children where present. Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0000776.raw
    SHA256 1b1d92f2f3ec584f7fe8d61021ebb433586609a130c97e9ec37a07cfda864c76; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0000776.receipt.json
    SHA256 94dc1b4d874552f77001ed1991fbb177ef5a070201ecc6a0af089eac0614e0c7.
  accessed_at: '2026-11-04T15:26:34.539495Z'
  support: supports
  summary: Current GO authority for 0000776; exact identity and anatomical/function
    scope assessed without converting transitive ancestors into direct parthood.
  snapshot_sha256: 1b1d92f2f3ec584f7fe8d61021ebb433586609a130c97e9ec37a07cfda864c76
- evidence_id: plaque-go-0000940-parents
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000940/ancestors?relations=is_a,part_of
  locator: Complete requested ancestor response; mixed is_a/part_of traversal is transitive
    context, not an assertion of a direct edge. Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0000940-parents.raw
    SHA256 f8578421ec888eeace5a4ada21783cee98be90e03e091348c536dfd85207213c; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0000940-parents.receipt.json
    SHA256 9ab35dbf3fd4ed9c3248581ae19c666b315bae2c44dc71c592c4a742f1a4aeeb.
  accessed_at: '2026-11-04T15:28:39.208906Z'
  support: supports
  summary: Current GO authority for 0000940; exact identity and anatomical/function
    scope assessed without converting transitive ancestors into direct parthood.
  snapshot_sha256: f8578421ec888eeace5a4ada21783cee98be90e03e091348c536dfd85207213c
- evidence_id: plaque-go-0000940
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000940
  locator: Exact current term identity, definition, obsolete flag, synonym qualifier
    strings and typed children where present. Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0000940.raw
    SHA256 10873acde0d686071f570f5abe217c347fff5836f301f7f9b1e05ceab4ded9e8; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0000940.receipt.json
    SHA256 3de0a651305aa93736db397d796c2316f7989ccacba09de6b2058b8a258f8751.
  accessed_at: '2026-11-04T15:26:34.491177Z'
  support: supports
  summary: Current GO authority for 0000940; exact identity and anatomical/function
    scope assessed without converting transitive ancestors into direct parthood.
  snapshot_sha256: 10873acde0d686071f570f5abe217c347fff5836f301f7f9b1e05ceab4ded9e8
- evidence_id: plaque-go-0005741
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005741
  locator: Exact current term identity, definition, obsolete flag, synonym qualifier
    strings and typed children where present. Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0005741.raw
    SHA256 701047b3a306f8b0b4bb945bce5d7e5e99dafe21be3fc7a97c10b63f9cbe2ca6; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0005741.receipt.json
    SHA256 35b531ba87af32fb8e84bd9eee68f0f40101dd29d3338fc6d6a6cf16bc45c6b5.
  accessed_at: '2026-11-04T15:26:34.194331Z'
  support: supports
  summary: Current GO authority for 0005741; exact identity and anatomical/function
    scope assessed without converting transitive ancestors into direct parthood.
  snapshot_sha256: 701047b3a306f8b0b4bb945bce5d7e5e99dafe21be3fc7a97c10b63f9cbe2ca6
- evidence_id: plaque-go-0005743
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005743
  locator: Exact current term identity, definition, obsolete flag, synonym qualifier
    strings and typed children where present. Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0005743.raw
    SHA256 ba28e8a48bcde74c14009e24937b39e33b51a79d50486259b47b8a3bfb4122e4; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0005743.receipt.json
    SHA256 96ccfe51578bb2ab2550c942470a4c2b3c670a501cb82ab5bc3cdd4e9a0eb733.
  accessed_at: '2026-11-04T15:26:35.020197Z'
  support: supports
  summary: Current GO authority for 0005743; exact identity and anatomical/function
    scope assessed without converting transitive ancestors into direct parthood.
  snapshot_sha256: ba28e8a48bcde74c14009e24937b39e33b51a79d50486259b47b8a3bfb4122e4
- evidence_id: plaque-go-0032991
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032991
  locator: Exact current term identity, definition, obsolete flag, synonym qualifier
    strings and typed children where present. Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0032991.raw
    SHA256 480165003b2c8a406006ff17c4cfe836fc000541ad5dac1ca0f585ed30c02e87; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0032991.receipt.json
    SHA256 5e10b5379b43076983fd1c096d9a77fed93fc3fe4dea65da3befb6f9c5d2878a.
  accessed_at: '2026-11-04T15:26:34.416527Z'
  support: supports
  summary: Current GO authority for 0032991; exact identity and anatomical/function
    scope assessed without converting transitive ancestors into direct parthood.
  snapshot_sha256: 480165003b2c8a406006ff17c4cfe836fc000541ad5dac1ca0f585ed30c02e87
- evidence_id: plaque-go-0034982
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0034982
  locator: Exact current term identity, definition, obsolete flag, synonym qualifier
    strings and typed children where present. Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0034982.raw
    SHA256 29be07b90645f1ae78346a2b15e315fdac3c150b300c238c28e9c6faf20f61aa; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0034982.receipt.json
    SHA256 382d9193aba3d9be3ab863b60e05b63ecc293967b9acabed9b8ca6260e429893.
  accessed_at: '2026-11-04T15:26:35.129417Z'
  support: supports
  summary: Current GO authority for 0034982; exact identity and anatomical/function
    scope assessed without converting transitive ancestors into direct parthood.
  snapshot_sha256: 29be07b90645f1ae78346a2b15e315fdac3c150b300c238c28e9c6faf20f61aa
- evidence_id: plaque-go-0042720-parents
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0042720/ancestors?relations=is_a,part_of
  locator: Complete requested ancestor response; mixed is_a/part_of traversal is transitive
    context, not an assertion of a direct edge. Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0042720-parents.raw
    SHA256 05474ce864a39e43ecefb2910b2d920b131426e0af4fc858f3a15ee3e0165fcb; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0042720-parents.receipt.json
    SHA256 c74a640232b3c0d77e22faa94684f250f12fca543761468ada20059d652c28e7.
  accessed_at: '2026-11-04T15:28:39.097367Z'
  support: supports
  summary: Current GO authority for 0042720; exact identity and anatomical/function
    scope assessed without converting transitive ancestors into direct parthood.
  snapshot_sha256: 05474ce864a39e43ecefb2910b2d920b131426e0af4fc858f3a15ee3e0165fcb
- evidence_id: plaque-go-0042720
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0042720
  locator: Exact current term identity, definition, obsolete flag, synonym qualifier
    strings and typed children where present. Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0042720.raw
    SHA256 9f5e79e0da4d08825a74c43fbe221d3e08d4ea52e1d69b5f176eb9daa0476a47; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0042720.receipt.json
    SHA256 a3b19dd6b45235e46c57a6e64a7fec4cd611cd262d6df482f0e2600004427228.
  accessed_at: '2026-11-04T15:26:33.602637Z'
  support: supports
  summary: Current GO authority for 0042720; exact identity and anatomical/function
    scope assessed without converting transitive ancestors into direct parthood.
  snapshot_sha256: 9f5e79e0da4d08825a74c43fbe221d3e08d4ea52e1d69b5f176eb9daa0476a47
- evidence_id: plaque-go-0098799
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0098799
  locator: Exact current term identity, definition, obsolete flag, synonym qualifier
    strings and typed children where present. Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0098799.raw
    SHA256 91e7dcb5172450141beb63b1231dd018f7f517db9c5cf1c0fc4699d8a4f0654c; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0098799.receipt.json
    SHA256 1b427512530ef2ed9615a9a3d057d471c2ba5c3a9993ae32ef6bf507d9faa92a.
  accessed_at: '2026-11-04T15:26:33.880365Z'
  support: supports
  summary: Current GO authority for 0098799; exact identity and anatomical/function
    scope assessed without converting transitive ancestors into direct parthood.
  snapshot_sha256: 91e7dcb5172450141beb63b1231dd018f7f517db9c5cf1c0fc4699d8a4f0654c
- evidence_id: plaque-go-0098800
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0098800
  locator: Exact current term identity, definition, obsolete flag, synonym qualifier
    strings and typed children where present. Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0098800.raw
    SHA256 b5d2eb220eb1a1a42ad99cfe91d358cb21597a3adea956e3d2c88cb2dae93ce6; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0098800.receipt.json
    SHA256 e929fbcff97e280e76f5ca2a797ae42cb9e2c618121aa7eb0aff12b763f3823f.
  accessed_at: '2026-11-04T15:26:34.778906Z'
  support: supports
  summary: Current GO authority for 0098800; exact identity and anatomical/function
    scope assessed without converting transitive ancestors into direct parthood.
  snapshot_sha256: b5d2eb220eb1a1a42ad99cfe91d358cb21597a3adea956e3d2c88cb2dae93ce6
- evidence_id: plaque-go-0140595-parents
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0140595/ancestors?relations=is_a,part_of
  locator: Complete requested ancestor response; mixed is_a/part_of traversal is transitive
    context, not an assertion of a direct edge. Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0140595-parents.raw
    SHA256 6efb033f6382bbccc6595e8489d29ed01e79a5b50e9b1187c47070c66d764bae; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0140595-parents.receipt.json
    SHA256 62b39c0ac9df5a4503d6c7329b365ac4c91f1a50bad9bcc0dae8175424d91b96.
  accessed_at: '2026-11-04T15:28:39.097272Z'
  support: supports
  summary: Current GO authority for 0140595; exact identity and anatomical/function
    scope assessed without converting transitive ancestors into direct parthood.
  snapshot_sha256: 6efb033f6382bbccc6595e8489d29ed01e79a5b50e9b1187c47070c66d764bae
- evidence_id: plaque-go-0140595
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0140595
  locator: Exact current term identity, definition, obsolete flag, synonym qualifier
    strings and typed children where present. Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0140595.raw
    SHA256 1d25381be57c943c9ce45320cc5ff140781ff399fff4a60bbf31f0460683e865; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-0140595.receipt.json
    SHA256 ec7becf53c37b77a27380f2781dca06ac3522d19a59cc7ec8e694ae8c81557a3.
  accessed_at: '2026-11-04T15:26:32.953251Z'
  support: supports
  summary: Current GO authority for 0140595; exact identity and anatomical/function
    scope assessed without converting transitive ancestors into direct parthood.
  snapshot_sha256: 1d25381be57c943c9ce45320cc5ff140781ff399fff4a60bbf31f0460683e865
- evidence_id: plaque-go-1905370
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1905370
  locator: Exact current term identity, definition, obsolete flag, synonym qualifier
    strings and typed children where present. Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-1905370.raw
    SHA256 1989830b762b86f5ae7f05bfbdb47ce9327f3008df33eda95975a955ec1cf7c3; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-1905370.receipt.json
    SHA256 c3f57e05370885dbb0d7d39f4df5915561755179abd7a3480f51b9a6f5ca8b6b.
  accessed_at: '2026-11-04T15:26:34.846549Z'
  support: supports
  summary: Current GO authority for 1905370; exact identity and anatomical/function
    scope assessed without converting transitive ancestors into direct parthood.
  snapshot_sha256: 1989830b762b86f5ae7f05bfbdb47ce9327f3008df33eda95975a955ec1cf7c3
- evidence_id: plaque-go-7770059
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:7770059
  locator: Exact current term identity, definition, obsolete flag, synonym qualifier
    strings and typed children where present. Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-7770059.raw
    SHA256 8723d41f0bcd227a4fe858c0c0bd2dc8e05582d14c494bf417df483bcac3cdd9; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/go-7770059.receipt.json
    SHA256 200201569d5b8c596ceb6be1d8ee8d6db5b3cf36489551a3ea6c3b0610050e32.
  accessed_at: '2026-11-04T15:26:34.198668Z'
  support: supports
  summary: Current GO authority for 7770059; exact identity and anatomical/function
    scope assessed without converting transitive ancestors into direct parthood.
  snapshot_sha256: 8723d41f0bcd227a4fe858c0c0bd2dc8e05582d14c494bf417df483bcac3cdd9
- evidence_id: plaque-ipr-IPR013262
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013262/
  locator: Complete metadata type/name/description/member signatures; protein membership
    checked separately Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/ipr-IPR013262.raw
    SHA256 d8611a20731dfadc51d22a9fb4c2adec8ece54df8833f8b5f0f09afeb9453748; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/ipr-IPR013262.receipt.json
    SHA256 19f5ef8f84b3c3dd2f326810d7ccab2032c3937e414812884a28a729ef40ccd5.
  accessed_at: '2026-11-04T15:26:39.675985Z'
  support: supports
  summary: 'IPR013262 is type family: Outer membrane protein, MIM1/TOM13, mitochondrial.
    IPR016851 is narrower than the joint PMF1/Nnf1 class; the malformed IPR008685
    organism phrase is not adopted.'
  snapshot_sha256: d8611a20731dfadc51d22a9fb4c2adec8ece54df8833f8b5f0f09afeb9453748
- evidence_id: plaque-ipr-IPR037652
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR037652/
  locator: Complete metadata type/name/description/member signatures; protein membership
    checked separately Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/ipr-IPR037652.raw
    SHA256 112d5a2021eabf25044253c0dee72db297d4099162b73ee2f355ab61f91ef866; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/ipr-IPR037652.receipt.json
    SHA256 f7d4a751934cffb686b9876b97133d1f3ed59c11a3aa24ab4016f57ef5d9d76b.
  accessed_at: '2026-11-04T15:26:40.266407Z'
  support: supports
  summary: 'IPR037652 is type family: Mim2. IPR016851 is narrower than the joint PMF1/Nnf1
    class; the malformed IPR008685 organism phrase is not adopted.'
  snapshot_sha256: 112d5a2021eabf25044253c0dee72db297d4099162b73ee2f355ab61f91ef866
- evidence_id: plaque-ipr-IPR008685
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR008685/
  locator: Complete metadata type/name/description/member signatures; protein membership
    checked separately Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/ipr-IPR008685.raw
    SHA256 e06c4648173ec5ba44dd1528257de9374b2ed303a086b31e4e0990d8bc8be118; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/ipr-IPR008685.receipt.json
    SHA256 e394e445a7a3921c476e5a9ce10714e34049b98649b57cc16b7455731fbc4e6b.
  accessed_at: '2026-11-04T15:26:40.863841Z'
  support: supports
  summary: 'IPR008685 is type family: Centromere protein Mis12. IPR016851 is narrower
    than the joint PMF1/Nnf1 class; the malformed IPR008685 organism phrase is not
    adopted.'
  snapshot_sha256: e06c4648173ec5ba44dd1528257de9374b2ed303a086b31e4e0990d8bc8be118
- evidence_id: plaque-ipr-IPR013218
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013218/
  locator: Complete metadata type/name/description/member signatures; protein membership
    checked separately Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/ipr-IPR013218.raw
    SHA256 568c9f62ea14d27c815c8017bf6e92d6af320d04216eda090b565e925ff903c8; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/ipr-IPR013218.receipt.json
    SHA256 77e2c96d517aa69b55c94b83988757d6078c11534f5739f7c014a907ad1289d6.
  accessed_at: '2026-11-04T15:26:40.911659Z'
  support: supports
  summary: 'IPR013218 is type family: Kinetochore-associated protein Dsn1/Mis13. IPR016851
    is narrower than the joint PMF1/Nnf1 class; the malformed IPR008685 organism phrase
    is not adopted.'
  snapshot_sha256: 568c9f62ea14d27c815c8017bf6e92d6af320d04216eda090b565e925ff903c8
- evidence_id: plaque-ipr-IPR013950
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013950/
  locator: Complete metadata type/name/description/member signatures; protein membership
    checked separately Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/ipr-IPR013950.raw
    SHA256 925c729248004dc084e61343626a714a7be901e7d14e4ee16a1bae9ca63d94d8; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/ipr-IPR013950.receipt.json
    SHA256 bd181b2fc583e0019f79b3b49ebc22db40e7bc899c2c587e1f09902c838c0a43.
  accessed_at: '2026-11-04T15:26:41.458600Z'
  support: supports
  summary: 'IPR013950 is type family: Kinetochore Mis14/Nsl1. IPR016851 is narrower
    than the joint PMF1/Nnf1 class; the malformed IPR008685 organism phrase is not
    adopted.'
  snapshot_sha256: 925c729248004dc084e61343626a714a7be901e7d14e4ee16a1bae9ca63d94d8
- evidence_id: plaque-ipr-IPR007128
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007128/
  locator: Complete metadata type/name/description/member signatures; protein membership
    checked separately Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/ipr-IPR007128.raw
    SHA256 65cb586ba7a68eaefdedad33aed45452e7b415359b3113570ca6a3919c4c57b2; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/ipr-IPR007128.receipt.json
    SHA256 9d50f322d899b6819acdd61344399b4602a99259471cc4f38c7999053bf4bfe7.
  accessed_at: '2026-11-04T15:26:41.503202Z'
  support: supports
  summary: 'IPR007128 is type family: Nuclear MIS12/MIND complex subunit PMF1/Nnf1.
    IPR016851 is narrower than the joint PMF1/Nnf1 class; the malformed IPR008685
    organism phrase is not adopted.'
  snapshot_sha256: 65cb586ba7a68eaefdedad33aed45452e7b415359b3113570ca6a3919c4c57b2
- evidence_id: plaque-ipr-IPR016851
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016851/
  locator: Complete metadata type/name/description/member signatures; protein membership
    checked separately Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/ipr-IPR016851.raw
    SHA256 39908cca1a702741dcf764a2e5e746206eb9cc5736580c8992a2db7a529a4a40; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/ipr-IPR016851.receipt.json
    SHA256 37499978aa8836fa5f084351db7bed76d2dffa58c45a929a7ee17a12742d6d43.
  accessed_at: '2026-11-04T15:26:42.047986Z'
  support: supports
  summary: 'IPR016851 is type family: Kinetochore-associated protein Nnf1. IPR016851
    is narrower than the joint PMF1/Nnf1 class; the malformed IPR008685 organism phrase
    is not adopted.'
  snapshot_sha256: 39908cca1a702741dcf764a2e5e746206eb9cc5736580c8992a2db7a529a4a40
- evidence_id: plaque-up-Q08176-retry
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q08176.json?format=json
  locator: Full native identity/status/primary gene/taxon, FUNCTION, SUBUNIT and SUBCELLULAR
    LOCATION comments and InterPro cross-references Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/up-Q08176-retry.raw
    SHA256 9a0724b67d38baaf0c88eda5fdf178ceb1063d1759cf9a636fdadb8b52c74bde; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/up-Q08176-retry.receipt.json
    SHA256 fa6a9f5e445e44c15b35b5a4c4021f22644d530c3add1d8794d58f497e909f5b.
  accessed_at: '2026-11-04T15:28:39.096968Z'
  support: supports
  summary: Reviewed Q08176 identifies MIM1 in reference strain S288C taxon559292.
    Species examples and class membership are distinct; annotation papers not otherwise
    listed are not certified read.
  snapshot_sha256: 9a0724b67d38baaf0c88eda5fdf178ceb1063d1759cf9a636fdadb8b52c74bde
- evidence_id: plaque-up-Q3E798
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q3E798.json
  locator: Full native identity/status/primary gene/taxon, FUNCTION, SUBUNIT and SUBCELLULAR
    LOCATION comments and InterPro cross-references Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/up-Q3E798.raw
    SHA256 ec7a45ad13c2710c794dee0db6e46e69b78d80d519f0370b84e9ee1616303772; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/up-Q3E798.receipt.json
    SHA256 0701161da36aed997229b82c2e6ee7fbc4b284527584888e13650f5d9033c983.
  accessed_at: '2026-11-04T15:26:35.368695Z'
  support: supports
  summary: Reviewed Q3E798 identifies MIM2 in reference strain S288C taxon559292.
    Species examples and class membership are distinct; annotation papers not otherwise
    listed are not certified read.
  snapshot_sha256: ec7a45ad13c2710c794dee0db6e46e69b78d80d519f0370b84e9ee1616303772
- evidence_id: plaque-up-P39731
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P39731.json
  locator: Full native identity/status/primary gene/taxon, FUNCTION, SUBUNIT and SUBCELLULAR
    LOCATION comments and InterPro cross-references Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/up-P39731.raw
    SHA256 0c3844f9cc37b32b6f30e038acc0c3895d2549aa18703aaa3a846fc445eaf6a3; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/up-P39731.receipt.json
    SHA256 b37d7d5db2bd1e35fbf0deedc5c7c0b22120892041c303841c0caeef42a6a79a.
  accessed_at: '2026-11-04T15:26:35.446748Z'
  support: supports
  summary: Reviewed P39731 identifies MTW1 in reference strain S288C taxon559292.
    Species examples and class membership are distinct; annotation papers not otherwise
    listed are not certified read.
  snapshot_sha256: 0c3844f9cc37b32b6f30e038acc0c3895d2549aa18703aaa3a846fc445eaf6a3
- evidence_id: plaque-up-P40568
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P40568.json
  locator: Full native identity/status/primary gene/taxon, FUNCTION, SUBUNIT and SUBCELLULAR
    LOCATION comments and InterPro cross-references Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/up-P40568.raw
    SHA256 8ee197059c0d47c233e91caecae5be56ebdba607af0fc0bce1159519d084281d; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/up-P40568.receipt.json
    SHA256 4310f5b04a4c9cba9a3a7c0b747ad2de5140e3b0eb6bcd60b250bf2b816626c0.
  accessed_at: '2026-11-04T15:26:35.594808Z'
  support: supports
  summary: Reviewed P40568 identifies DSN1 in reference strain S288C taxon559292.
    Species examples and class membership are distinct; annotation papers not otherwise
    listed are not certified read.
  snapshot_sha256: 8ee197059c0d47c233e91caecae5be56ebdba607af0fc0bce1159519d084281d
- evidence_id: plaque-up-Q12143
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q12143.json
  locator: Full native identity/status/primary gene/taxon, FUNCTION, SUBUNIT and SUBCELLULAR
    LOCATION comments and InterPro cross-references Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/up-Q12143.raw
    SHA256 ad535ce87e143bd05cd8ee7be4206f30339e2eb5423010eaa7e87f1e06a682a0; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/up-Q12143.receipt.json
    SHA256 f11bf0bb5387902fc04c0acfc5f97363e5055d34b0bd2c03157df5a65334eb89.
  accessed_at: '2026-11-04T15:26:35.708883Z'
  support: supports
  summary: Reviewed Q12143 identifies NSL1 in reference strain S288C taxon559292.
    Species examples and class membership are distinct; annotation papers not otherwise
    listed are not certified read.
  snapshot_sha256: ad535ce87e143bd05cd8ee7be4206f30339e2eb5423010eaa7e87f1e06a682a0
- evidence_id: plaque-up-P47149-retry
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P47149.json?format=json
  locator: Full native identity/status/primary gene/taxon, FUNCTION, SUBUNIT and SUBCELLULAR
    LOCATION comments and InterPro cross-references Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/up-P47149-retry.raw
    SHA256 6b3ba871504fdb8a5759cf7d1d7c99175cde494559e6571876239b629e3c4218; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/up-P47149-retry.receipt.json
    SHA256 4d3a35849b85838b22f4dfc3baaefad8f85630dc2bffa79f3ab96dd3388cb657.
  accessed_at: '2026-11-04T15:28:39.097054Z'
  support: supports
  summary: Reviewed P47149 identifies NNF1 in reference strain S288C taxon559292.
    Species examples and class membership are distinct; annotation papers not otherwise
    listed are not certified read.
  snapshot_sha256: 6b3ba871504fdb8a5759cf7d1d7c99175cde494559e6571876239b629e3c4218
- evidence_id: plaque-up-P40460
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P40460.json
  locator: Full native identity/status/primary gene/taxon, FUNCTION, SUBUNIT and SUBCELLULAR
    LOCATION comments and InterPro cross-references Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/up-P40460.raw
    SHA256 bb7b0fa4786334b7a92ecefb6915feaaaaa05d231552da89d9f38a459c981051; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/up-P40460.receipt.json
    SHA256 7d93d993e7197310f3c9e981e0f3e8c8222fddbc65df593f30016491cd30f180.
  accessed_at: '2026-11-04T15:26:36.591880Z'
  support: supports
  summary: Reviewed P40460 identifies NDC80 in reference strain S288C taxon559292.
    Species examples and class membership are distinct; annotation papers not otherwise
    listed are not certified read.
  snapshot_sha256: bb7b0fa4786334b7a92ecefb6915feaaaaa05d231552da89d9f38a459c981051
- evidence_id: plaque-up-P33895
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P33895.json
  locator: Full native identity/status/primary gene/taxon, FUNCTION, SUBUNIT and SUBCELLULAR
    LOCATION comments and InterPro cross-references Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/up-P33895.raw
    SHA256 2a0630d209109e36f7ee437e3298f75916c46b69683101f55276f4a0394eee58; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/up-P33895.receipt.json
    SHA256 ab6ebabc1762bbaed0c0d527d3fc5695eb1d7e06ed1484b8690921f49fdcb710.
  accessed_at: '2026-11-04T15:26:36.603551Z'
  support: supports
  summary: Reviewed P33895 identifies NUF2 in reference strain S288C taxon559292.
    Species examples and class membership are distinct; annotation papers not otherwise
    listed are not certified read.
  snapshot_sha256: 2a0630d209109e36f7ee437e3298f75916c46b69683101f55276f4a0394eee58
- evidence_id: plaque-up-Q04477-retry
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q04477.json?format=json
  locator: Full native identity/status/primary gene/taxon, FUNCTION, SUBUNIT and SUBCELLULAR
    LOCATION comments and InterPro cross-references Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/up-Q04477-retry.raw
    SHA256 d87de5336ad58ff4d2a8616f6382c52938c1188c3bb3ec1222bf986bd86e983b; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/up-Q04477-retry.receipt.json
    SHA256 c8e5cf590c5afdbcc19b2d7af88fcf11c096e5d7f5bc2cac8b6cf7fa012dac0b.
  accessed_at: '2026-11-04T15:28:39.097112Z'
  support: supports
  summary: Reviewed Q04477 identifies SPC24 in reference strain S288C taxon559292.
    Species examples and class membership are distinct; annotation papers not otherwise
    listed are not certified read.
  snapshot_sha256: d87de5336ad58ff4d2a8616f6382c52938c1188c3bb3ec1222bf986bd86e983b
- evidence_id: plaque-tax-4932
  kind: database
  reference: https://rest.uniprot.org/taxonomy/4932.json
  locator: Complete taxId/name/rank/lineage/synonyms Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/tax-4932.raw
    SHA256 1a6c0b4fc804f45969573b7d0cec1e375ac361a2aae51313e7bb76ecfbff3c0b; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/tax-4932.receipt.json
    SHA256 6f2154ab908290b13fb7c80fbbb45f99d346296e9a6793c54f14b0d7baa4e63f.
  accessed_at: '2026-11-04T15:26:42.099789Z'
  support: supports
  summary: Taxon 4932 distinguishes S. cerevisiae species from S288C reference strain;
    experimental cultures are separately scoped.
  snapshot_sha256: 1a6c0b4fc804f45969573b7d0cec1e375ac361a2aae51313e7bb76ecfbff3c0b
- evidence_id: plaque-tax-559292
  kind: database
  reference: https://rest.uniprot.org/taxonomy/559292.json
  locator: Complete taxId/name/rank/lineage/synonyms Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/tax-559292.raw
    SHA256 9ebcfe8a317cc0c25c329a3a6a7cc9eaa863bb2dfebe5eaff9a34628c6684810; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/tax-559292.receipt.json
    SHA256 df32e80b9136f473fde4889b6454c38f11e84dd545a4d886f98de415e5824be1.
  accessed_at: '2026-11-04T15:26:42.698522Z'
  support: supports
  summary: Taxon 559292 distinguishes S. cerevisiae species from S288C reference strain;
    experimental cultures are separately scoped.
  snapshot_sha256: 9ebcfe8a317cc0c25c329a3a6a7cc9eaa863bb2dfebe5eaff9a34628c6684810
- evidence_id: plaque-doan2020-metadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1016%2Fj.celrep.2020.107567&format=json&resultType=core&pageSize=5
  locator: Unique MED identity, bibliographic fields and complete abstractText; not
    a full-body claim Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/doan2020-metadata.raw
    SHA256 58c00ab0347acee7cb726ad95e5452768238dae6354752943ea8758a7d300807; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/doan2020-metadata.receipt.json
    SHA256 7a7b500437b696543ad076dd81fc38ce85d05ed3b968812611ec6deb9c3ab8c6.
  accessed_at: '2026-11-04T15:26:32.952555Z'
  support: supports
  summary: 'PMID32348752: The Mitochondrial Import Complex MIM Functions as Main Translocase
    for α-Helical Outer Membrane Proteins. (2020); DOI 10.1016/j.celrep.2020.107567.
    Primary abstract scope only, except Gakh2002 which is a secondary review abstract.'
  snapshot_sha256: 58c00ab0347acee7cb726ad95e5452768238dae6354752943ea8758a7d300807
  search_scope: Europe PMC exact identifier query in reference URL, resultType=core,
    pageSize=5; complete returned identity set and selected complete abstract read;
    actual access timestamp retained. No title/metadata inference of Methods.
- evidence_id: plaque-vitali2018-metadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.7554%2FeLife.34488&format=json&resultType=core&pageSize=5
  locator: Unique MED identity, bibliographic fields and complete abstractText; not
    a full-body claim Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/vitali2018-metadata.raw
    SHA256 e45eff19aa5454f5d77466c27b88e72f2e43fc793418408a9010a786613471a0; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/vitali2018-metadata.receipt.json
    SHA256 1fcbb5f9f5902ba08134ce048202549efb222f16f2e6547422c64d66ffa2a131.
  accessed_at: '2026-11-04T15:26:32.952841Z'
  support: supports
  summary: 'PMID29923829: Independent evolution of functionally exchangeable mitochondrial
    outer membrane import complexes. (2018); DOI 10.7554/elife.34488. Primary abstract
    scope only, except Gakh2002 which is a secondary review abstract.'
  snapshot_sha256: e45eff19aa5454f5d77466c27b88e72f2e43fc793418408a9010a786613471a0
  search_scope: Europe PMC exact identifier query in reference URL, resultType=core,
    pageSize=5; complete returned identity set and selected complete abstract read;
    actual access timestamp retained. No title/metadata inference of Methods.
- evidence_id: plaque-vitali2019-metadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1016%2Fj.isci.2019.100779&format=json&resultType=core&pageSize=5
  locator: Unique MED identity, bibliographic fields and complete abstractText; not
    a full-body claim Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/vitali2019-metadata.raw
    SHA256 7d2b257afeda15507c45354b89e048fb023835c042cec3a9384cc6caf114e40e; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/vitali2019-metadata.receipt.json
    SHA256 ec55c5ac875716b8cb1a11f185e422e3978e82f9dc23d1dd93ac2bc3ce640bb5.
  accessed_at: '2026-11-04T15:26:32.952924Z'
  support: supports
  summary: 'PMID31945731: The Biogenesis of Mitochondrial Outer Membrane Proteins
    Show Variable Dependence on Import Factors. (2020); DOI 10.1016/j.isci.2019.100779.
    Primary abstract scope only, except Gakh2002 which is a secondary review abstract.'
  snapshot_sha256: 7d2b257afeda15507c45354b89e048fb023835c042cec3a9384cc6caf114e40e
  search_scope: Europe PMC exact identifier query in reference URL, resultType=core,
    pageSize=5; complete returned identity set and selected complete abstract read;
    actual access timestamp retained. No title/metadata inference of Methods.
- evidence_id: plaque-dewulf2003-metadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1101%2Fgad.1144403&format=json&resultType=core&pageSize=5
  locator: Unique MED identity, bibliographic fields and complete abstractText; not
    a full-body claim Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/dewulf2003-metadata.raw
    SHA256 6aa87e0293d064b13af37abee34e2a713615583020e5c99e20f8dff64da6b4cf; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/dewulf2003-metadata.receipt.json
    SHA256 b1754169c2c9d119b3fd9399702054732514807ec1ad4e14bd11f3841b46af47.
  accessed_at: '2026-11-04T15:26:32.952983Z'
  support: supports
  summary: 'PMID14633972: Hierarchical assembly of the budding yeast kinetochore from
    multiple subcomplexes. (2003); DOI 10.1101/gad.1144403. Primary abstract scope
    only, except Gakh2002 which is a secondary review abstract.'
  snapshot_sha256: 6aa87e0293d064b13af37abee34e2a713615583020e5c99e20f8dff64da6b4cf
  search_scope: Europe PMC exact identifier query in reference URL, resultType=core,
    pageSize=5; complete returned identity set and selected complete abstract read;
    actual access timestamp retained. No title/metadata inference of Methods.
- evidence_id: plaque-kline2006-metadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1083%2Fjcb.200509158&format=json&resultType=core&pageSize=5
  locator: Unique MED identity, bibliographic fields and complete abstractText; not
    a full-body claim Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/kline2006-metadata.raw
    SHA256 f2c34edce1781cfc8fd07061c9c5bf0e10c1f30160c31685bf3fa75cd90bd1f1; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/kline2006-metadata.receipt.json
    SHA256 1e9e3db6f2995a33322a6f72cfe5c20523d9a74dfcdb82da5d86de63850e9caa.
  accessed_at: '2026-11-04T15:26:32.953026Z'
  support: supports
  summary: 'PMID16585270: The human Mis12 complex is required for kinetochore assembly
    and proper chromosome segregation. (2006); DOI 10.1083/jcb.200509158. Primary
    abstract scope only, except Gakh2002 which is a secondary review abstract.'
  snapshot_sha256: f2c34edce1781cfc8fd07061c9c5bf0e10c1f30160c31685bf3fa75cd90bd1f1
  search_scope: Europe PMC exact identifier query in reference URL, resultType=core,
    pageSize=5; complete returned identity set and selected complete abstract read;
    actual access timestamp retained. No title/metadata inference of Methods.
- evidence_id: plaque-jan2000-metadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1007%2Fs004380051192&format=json&resultType=core&pageSize=5
  locator: Unique MED identity, bibliographic fields and complete abstractText; not
    a full-body claim Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/jan2000-metadata.raw
    SHA256 50383e9108694c2b34d9b81299971ffc07cfffb33604c8ec9770b35e88a1c37a; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/jan2000-metadata.receipt.json
    SHA256 c15434fd03939170b5925e582b33bc6488299914613c1b4f6e8ecfcda285af87.
  accessed_at: '2026-11-04T15:26:32.953175Z'
  support: supports
  summary: 'PMID10821182: Som1, a third component of the yeast mitochondrial inner
    membrane peptidase complex that contains Imp1 and Imp2. (2000); DOI 10.1007/s004380051192.
    Primary abstract scope only, except Gakh2002 which is a secondary review abstract.'
  snapshot_sha256: 50383e9108694c2b34d9b81299971ffc07cfffb33604c8ec9770b35e88a1c37a
  search_scope: Europe PMC exact identifier query in reference URL, resultType=core,
    pageSize=5; complete returned identity set and selected complete abstract read;
    actual access timestamp retained. No title/metadata inference of Methods.
- evidence_id: plaque-gakh2002-pmid
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12191769%20AND%20SRC%3AMED&format=json&resultType=core&pageSize=5
  locator: Unique MED identity, bibliographic fields and complete abstractText; not
    a full-body claim Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/gakh2002-pmid.raw
    SHA256 9cc68c5f2927320631d6b96479e0d617c2f9580dfaf4d2b3bb6eb6a9ad9bfcb4; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/gakh2002-pmid.receipt.json
    SHA256 d4502cb5be7e453b29189d345ff88a329ae87167b15bbc74f809733f6f6933d0.
  accessed_at: '2026-11-04T15:27:25.532245Z'
  support: supports
  summary: 'PMID12191769: Mitochondrial processing peptidases. (2002); DOI 10.1016/s0167-4889(02)00265-3.
    Primary abstract scope only, except Gakh2002 which is a secondary review abstract.'
  snapshot_sha256: 9cc68c5f2927320631d6b96479e0d617c2f9580dfaf4d2b3bb6eb6a9ad9bfcb4
  search_scope: Europe PMC exact identifier query in reference URL, resultType=core,
    pageSize=5; complete returned identity set and selected complete abstract read;
    actual access timestamp retained. No title/metadata inference of Methods.
- evidence_id: plaque-pmid-15326197
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15326197+AND+SRC%3AMED&format=json&resultType=core&pageSize=5
  locator: Unique MED identity, bibliographic fields and complete abstractText; not
    a full-body claim Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/pmid-15326197.raw
    SHA256 9d6a470beaa641f625abb34a43ae2575d313100ead1a1a0b77f74ed5b5f529d7; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/pmid-15326197.receipt.json
    SHA256 652b182e7e171942e685d959dcc3e3790e64e2061d14c43f00daf2bc6fdd179d.
  accessed_at: '2026-11-04T15:27:26.363726Z'
  support: supports
  summary: 'PMID15326197: Two novel proteins in the mitochondrial outer membrane mediate
    beta-barrel protein assembly. (2004); DOI 10.1083/jcb.200405138. Primary abstract
    scope only, except Gakh2002 which is a secondary review abstract.'
  snapshot_sha256: 9d6a470beaa641f625abb34a43ae2575d313100ead1a1a0b77f74ed5b5f529d7
  search_scope: Europe PMC exact identifier query in reference URL, resultType=core,
    pageSize=5; complete returned identity set and selected complete abstract read;
    actual access timestamp retained. No title/metadata inference of Methods.
- evidence_id: plaque-pmid-15608614
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15608614+AND+SRC%3AMED&format=json&resultType=core&pageSize=5
  locator: Unique MED identity, bibliographic fields and complete abstractText; not
    a full-body claim Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/pmid-15608614.raw
    SHA256 efdb387426e5ea4a442048f2d57a1f779a340490a5a175f254c07d185a58d805; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/pmid-15608614.receipt.json
    SHA256 68f8ab61f68c04416f63ae71b10edae7d708b9095be139d740c1874efc3566bf.
  accessed_at: '2026-11-04T15:27:26.704175Z'
  support: supports
  summary: 'PMID15608614: Mim1, a protein required for the assembly of the TOM complex
    of mitochondria. (2005); DOI 10.1038/sj.embor.7400318. Primary abstract scope
    only, except Gakh2002 which is a secondary review abstract.'
  snapshot_sha256: efdb387426e5ea4a442048f2d57a1f779a340490a5a175f254c07d185a58d805
  search_scope: Europe PMC exact identifier query in reference URL, resultType=core,
    pageSize=5; complete returned identity set and selected complete abstract read;
    actual access timestamp retained. No title/metadata inference of Methods.
- evidence_id: plaque-pmid-22467864
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A22467864+AND+SRC%3AMED&format=json&resultType=core&pageSize=5
  locator: Unique MED identity, bibliographic fields and complete abstractText; not
    a full-body claim Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/pmid-22467864.raw
    SHA256 eca00c33ab3d6608b727bc5cf4147da7f23bd76fbc7e6c0119c5bd0c9cce44f9; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/pmid-22467864.receipt.json
    SHA256 6a17998c80b07f5e8bd9bf093fdf167a67f0caf23ee86a3cbd505be94aea45dd.
  accessed_at: '2026-11-04T15:27:27.307139Z'
  support: supports
  summary: 'PMID22467864: A crucial role for Mim2 in the biogenesis of mitochondrial
    outer membrane proteins. (2012); DOI 10.1242/jcs.103804. Primary abstract scope
    only, except Gakh2002 which is a secondary review abstract.'
  snapshot_sha256: eca00c33ab3d6608b727bc5cf4147da7f23bd76fbc7e6c0119c5bd0c9cce44f9
  search_scope: Europe PMC exact identifier query in reference URL, resultType=core,
    pageSize=5; complete returned identity set and selected complete abstract read;
    actual access timestamp retained. No title/metadata inference of Methods.
- evidence_id: plaque-pmid-12455957
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12455957+AND+SRC%3AMED&format=json&resultType=core&pageSize=5
  locator: Unique MED identity, bibliographic fields and complete abstractText; not
    a full-body claim Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/pmid-12455957.raw
    SHA256 e189e398c1778f6ff1d60c589aed6705fddfc847facd4df7eb9199871f9b1681; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/pmid-12455957.receipt.json
    SHA256 510ae39a0a69b7655d875ce0857c3eaea15266e2a085a09c04dba90e97436b9e.
  accessed_at: '2026-11-04T15:27:27.998838Z'
  support: supports
  summary: 'PMID12455957: Nnf1p, Dsn1p, Mtw1p, and Nsl1p: a new group of proteins
    important for chromosome segregation in Saccharomyces cerevisiae. (2002); DOI
    10.1128/ec.1.2.229-240.2002. Primary abstract scope only, except Gakh2002 which
    is a secondary review abstract.'
  snapshot_sha256: e189e398c1778f6ff1d60c589aed6705fddfc847facd4df7eb9199871f9b1681
  search_scope: Europe PMC exact identifier query in reference URL, resultType=core,
    pageSize=5; complete returned identity set and selected complete abstract read;
    actual access timestamp retained. No title/metadata inference of Methods.
- evidence_id: plaque-pmid-14602074
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14602074+AND+SRC%3AMED&format=json&resultType=core&pageSize=5
  locator: Unique MED identity, bibliographic fields and complete abstractText; not
    a full-body claim Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/pmid-14602074.raw
    SHA256 d1e73dc06e71e15cdb6cb51be8ec8320ed74adcd91395ea60acaa4951185a96f; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/pmid-14602074.receipt.json
    SHA256 7373a8b6bef88c33b8cc2c043b28dfe7253aea78c46c85406bb85f32b913f2c5.
  accessed_at: '2026-11-04T15:27:27.355238Z'
  support: supports
  summary: 'PMID14602074: An Mtw1 complex promotes kinetochore biorientation that
    is monitored by the Ipl1/Aurora protein kinase. (2003); DOI 10.1016/s1534-5807(03)00322-8.
    Primary abstract scope only, except Gakh2002 which is a secondary review abstract.'
  snapshot_sha256: d1e73dc06e71e15cdb6cb51be8ec8320ed74adcd91395ea60acaa4951185a96f
  search_scope: Europe PMC exact identifier query in reference URL, resultType=core,
    pageSize=5; complete returned identity set and selected complete abstract read;
    actual access timestamp retained. No title/metadata inference of Methods.
- evidence_id: plaque-pmid-14657030
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14657030+AND+SRC%3AMED&format=json&resultType=core&pageSize=5
  locator: Unique MED identity, bibliographic fields and complete abstractText; not
    a full-body claim Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/pmid-14657030.raw
    SHA256 a0765ceea39156739ed26d1326de1f92f6bffd5186c85f31757a5c3b55080ac1; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/pmid-14657030.receipt.json
    SHA256 654b643933c99aaa11530f9833cf2121c6be98dbd031bafdddcca88bc8f55cf5.
  accessed_at: '2026-11-04T15:27:27.723121Z'
  support: supports
  summary: 'PMID14657030: Nsl1p is essential for the establishment of bipolarity and
    the localization of the Dam-Duo complex. (2003); DOI 10.1093/emboj/cdg636. Primary
    abstract scope only, except Gakh2002 which is a secondary review abstract.'
  snapshot_sha256: a0765ceea39156739ed26d1326de1f92f6bffd5186c85f31757a5c3b55080ac1
  search_scope: Europe PMC exact identifier query in reference URL, resultType=core,
    pageSize=5; complete returned identity set and selected complete abstract read;
    actual access timestamp retained. No title/metadata inference of Methods.
- evidence_id: plaque-gene-MTW1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AMTW1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned reviewed gene_exact MTW1 organism559292 identities Raw
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/gene-MTW1.raw
    SHA256 5e9157a45fe17da2b2ab661323a2729aa82b93b050fd8fd46303046151fb1e7a; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/gene-MTW1.receipt.json
    SHA256 e1f34c4199f98589f41f344a5f219761650628fdc4dc7456c9d52994e1982cec.
  accessed_at: '2026-11-04T15:27:25.817391Z'
  support: supports
  summary: Only P39731 returned in this bounded current query. Other current gene-query
    transport failures do not support uniqueness claims.
  snapshot_sha256: 5e9157a45fe17da2b2ab661323a2729aa82b93b050fd8fd46303046151fb1e7a
  search_scope: UniProtKB query (gene_exact:MTW1) AND (organism_id:559292) AND (reviewed:true),
    size500; complete response inspected at recorded time; not all taxa or unreviewed
    entries.
- evidence_id: plaque-gene-MIM1
  kind: validation
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AMIM1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Actual response/transport receipt only Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/gene-MIM1.raw
    SHA256 7a85c8e2aeaafe9d1dff1cc7777a70a62f620ca35b59b506ef7cddfabcd2014d; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/gene-MIM1.receipt.json
    SHA256 dac51121133576157760353ae0bd3d1f7754146025e65fbde95cbb0ba400e4ad.
  accessed_at: '2026-11-04T15:27:25.595348Z'
  support: context_only
  summary: 'Current route status 503; HTTP Error 503: Backend fetch failed. No successful
    body or negative scientific conclusion derived. Successful retries/abstracts/indexed
    excerpts are separately scoped.'
  snapshot_sha256: 7a85c8e2aeaafe9d1dff1cc7777a70a62f620ca35b59b506ef7cddfabcd2014d
  search_scope: Exact URL query only; transport failure prevents an identity-set or
    absence conclusion.
- evidence_id: plaque-gene-MIM2
  kind: validation
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AMIM2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Actual response/transport receipt only Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/gene-MIM2.raw
    SHA256 339bdc071ebd0b2630ef50fd516a2af944df77e599d7cd4e4403046ea8ff0dc9; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/gene-MIM2.receipt.json
    SHA256 7ce7671e7b45251b6c501417f8ce7f0e06c01cf798a0791f46ab8da77a10ccde.
  accessed_at: '2026-11-04T15:27:25.803454Z'
  support: context_only
  summary: 'Current route status 503; HTTP Error 503: Backend fetch failed. No successful
    body or negative scientific conclusion derived. Successful retries/abstracts/indexed
    excerpts are separately scoped.'
  snapshot_sha256: 339bdc071ebd0b2630ef50fd516a2af944df77e599d7cd4e4403046ea8ff0dc9
  search_scope: Exact URL query only; transport failure prevents an identity-set or
    absence conclusion.
- evidence_id: plaque-gene-DSN1
  kind: validation
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ADSN1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Actual response/transport receipt only Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/gene-DSN1.raw
    SHA256 150a09ca9f45bb4acb35b8da51af1701469b28844ece5ccb2d5a34a39ebf4096; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/gene-DSN1.receipt.json
    SHA256 13e728ca022cb9d11893e311ecf0fa9c81e944b5d1d5e68dec81a5c0d15fc37b.
  accessed_at: '2026-11-04T15:27:25.958057Z'
  support: context_only
  summary: 'Current route status 503; HTTP Error 503: Backend fetch failed. No successful
    body or negative scientific conclusion derived. Successful retries/abstracts/indexed
    excerpts are separately scoped.'
  snapshot_sha256: 150a09ca9f45bb4acb35b8da51af1701469b28844ece5ccb2d5a34a39ebf4096
  search_scope: Exact URL query only; transport failure prevents an identity-set or
    absence conclusion.
- evidence_id: plaque-gene-NSL1
  kind: validation
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ANSL1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Actual response/transport receipt only Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/gene-NSL1.raw
    SHA256 36cee505381f1e02bc919356a1352f71a7ec886d98883b5232ac0a3411b330f5; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/gene-NSL1.receipt.json
    SHA256 fe4119b264b1739aba0feac9b151489cff387d7a2e1b92b444c06414aee3ba4d.
  accessed_at: '2026-11-04T15:27:26.144363Z'
  support: context_only
  summary: 'Current route status 503; HTTP Error 503: Backend fetch failed. No successful
    body or negative scientific conclusion derived. Successful retries/abstracts/indexed
    excerpts are separately scoped.'
  snapshot_sha256: 36cee505381f1e02bc919356a1352f71a7ec886d98883b5232ac0a3411b330f5
  search_scope: Exact URL query only; transport failure prevents an identity-set or
    absence conclusion.
- evidence_id: plaque-gene-NNF1
  kind: validation
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ANNF1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Actual response/transport receipt only Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/gene-NNF1.raw
    SHA256 77272e5b973d90476a4037e7e8875088a93089cd07d89fbac04f5f85b9084c32; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/gene-NNF1.receipt.json
    SHA256 1162430073d33f212a7b2946a98e842638a6235ad33c2d289fee58aff8dab22b.
  accessed_at: '2026-11-04T15:27:26.184219Z'
  support: context_only
  summary: 'Current route status 503; HTTP Error 503: Backend fetch failed. No successful
    body or negative scientific conclusion derived. Successful retries/abstracts/indexed
    excerpts are separately scoped.'
  snapshot_sha256: 77272e5b973d90476a4037e7e8875088a93089cd07d89fbac04f5f85b9084c32
  search_scope: Exact URL query only; transport failure prevents an identity-set or
    absence conclusion.
- evidence_id: plaque-up-Q08176
  kind: validation
  reference: https://rest.uniprot.org/uniprotkb/Q08176.json
  locator: Actual response/transport receipt only Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/up-Q08176.raw
    SHA256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/up-Q08176.receipt.json
    SHA256 0ce2c55244ca36cf0740b9e58c03af36919bcf6cd9d586110b01de89bf21f6ea.
  accessed_at: '2026-11-04T15:26:35.207633Z'
  support: context_only
  summary: Current route status 0; The read operation timed out. No successful body
    or negative scientific conclusion derived. Successful retries/abstracts/indexed
    excerpts are separately scoped.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: plaque-up-P47149
  kind: validation
  reference: https://rest.uniprot.org/uniprotkb/P47149.json
  locator: Actual response/transport receipt only Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/up-P47149.raw
    SHA256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/up-P47149.receipt.json
    SHA256 bf4fbf35890119d8face8cfdbaf1e202edaedb3a7917735fea63527761d3af79.
  accessed_at: '2026-11-04T15:26:36.375592Z'
  support: context_only
  summary: Current route status 0; The read operation timed out. No successful body
    or negative scientific conclusion derived. Successful retries/abstracts/indexed
    excerpts are separately scoped.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: plaque-up-Q04477
  kind: validation
  reference: https://rest.uniprot.org/uniprotkb/Q04477.json
  locator: Actual response/transport receipt only Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/up-Q04477.raw
    SHA256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/up-Q04477.receipt.json
    SHA256 8b9acf0c922a3b256f51468d25e4133f05556cff4fd5ceb2c52f75a6b719e289.
  accessed_at: '2026-11-04T15:26:36.786985Z'
  support: context_only
  summary: Current route status 0; The read operation timed out. No successful body
    or negative scientific conclusion derived. Successful retries/abstracts/indexed
    excerpts are separately scoped.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: plaque-doan2020-freidok
  kind: validation
  reference: https://freidok.uni-freiburg.de/files/165604/PIIS2211124720305167.pdf
  locator: Actual response/transport receipt only Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/doan2020-freidok.raw
    SHA256 54403a34b81a851f50e1a2f57298aebc30b408d952317020dbe43ac59fc732eb; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/doan2020-freidok.receipt.json
    SHA256 174131330b79b8aafd8c32f82001582f4861f596383d4f9d5c7884dff5db862e.
  accessed_at: '2026-11-04T15:27:25.531979Z'
  support: context_only
  summary: 'Current route status 404; HTTP Error 404: Not Found. No successful body
    or negative scientific conclusion derived. Successful retries/abstracts/indexed
    excerpts are separately scoped.'
  snapshot_sha256: 54403a34b81a851f50e1a2f57298aebc30b408d952317020dbe43ac59fc732eb
- evidence_id: plaque-doan2020-storage
  kind: validation
  reference: https://storage.freidok.ub.uni-freiburg.de/publications/165604/ieaccMPhkWq1nfS5/PIIS2211124720305167.pdf
  locator: Actual response/transport receipt only Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/doan2020-storage.raw
    SHA256 0586debc1a74fa198c100b14dfbc0629cbd2a9d71150b021a8f0f262ea3c9354; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/doan2020-storage.receipt.json
    SHA256 46583c06da71099dc31eed2572c63bde784224a3c3a87e3a22a254f9aeb26e6e.
  accessed_at: '2026-11-04T15:27:25.532044Z'
  support: context_only
  summary: 'Current route status 403; HTTP Error 403: Forbidden. No successful body
    or negative scientific conclusion derived. Successful retries/abstracts/indexed
    excerpts are separately scoped.'
  snapshot_sha256: 0586debc1a74fa198c100b14dfbc0629cbd2a9d71150b021a8f0f262ea3c9354
- evidence_id: plaque-doan2020-cell
  kind: validation
  reference: https://www.cell.com/cell-reports/pdf/S2211-1247(20)30516-7.pdf
  locator: Actual response/transport receipt only Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/doan2020-cell.raw
    SHA256 e324f28d6c62553784fede6337ac7a4a3daaac914fee1eccf4741bdc776e56d4; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/doan2020-cell.receipt.json
    SHA256 48f920e85a4818bd1b5ad2fa879291c77c7a0ac1b846af65989a6149b015cbb2.
  accessed_at: '2026-11-04T15:27:25.532094Z'
  support: context_only
  summary: 'Current route status 403; HTTP Error 403: Forbidden. No successful body
    or negative scientific conclusion derived. Successful retries/abstracts/indexed
    excerpts are separately scoped.'
  snapshot_sha256: e324f28d6c62553784fede6337ac7a4a3daaac914fee1eccf4741bdc776e56d4
- evidence_id: plaque-doan2020-rg
  kind: validation
  reference: https://www.researchgate.net/publication/340985619_The_Mitochondrial_Import_Complex_MIM_Functions_as_Main_Translocase_for_a-Helical_Outer_Membrane_Proteins
  locator: Actual response/transport receipt only Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/doan2020-rg.raw
    SHA256 f2fd10a5da17a30301197e56a4488fc6d72246a2e7fd2a404af1201ae1de8058; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/doan2020-rg.receipt.json
    SHA256 778f2862a8119bafdb6eec47492e654e1146c7644de86b8fa3babccbb1e923d8.
  accessed_at: '2026-11-04T15:28:39.096856Z'
  support: context_only
  summary: 'Current route status 403; HTTP Error 403: Forbidden. No successful body
    or negative scientific conclusion derived. Successful retries/abstracts/indexed
    excerpts are separately scoped.'
  snapshot_sha256: f2fd10a5da17a30301197e56a4488fc6d72246a2e7fd2a404af1201ae1de8058
- evidence_id: plaque-jan2000-publisher
  kind: validation
  reference: https://link.springer.com/article/10.1007/s004380051192
  locator: Actual response/transport receipt only Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/jan2000-publisher.raw
    SHA256 861d40bd2fd962728560720c26365ce8ba5d7530462bc73d123e3374eeec53c3; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/jan2000-publisher.receipt.json
    SHA256 1dae59da5cc198450b41ffeea740b67231cc49233deabce41fd09fa11fa550b2.
  accessed_at: '2026-11-04T15:27:25.532285Z'
  support: context_only
  summary: Current route status 200; None. No successful body or negative scientific
    conclusion derived. Successful retries/abstracts/indexed excerpts are separately
    scoped.
  snapshot_sha256: 861d40bd2fd962728560720c26365ce8ba5d7530462bc73d123e3374eeec53c3
- evidence_id: plaque-dewulf2003-jats
  kind: validation
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC289150.1/PMC289150.1.xml
  locator: Actual response/transport receipt only Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/dewulf2003-jats.raw
    SHA256 28d8b32688722232ca9d1168cb41a11b3f74d8cef50d0b2cfc0bc4250e894261; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/dewulf2003-jats.receipt.json
    SHA256 8b662ff6712002385e0a404da5513a45c08ab1c7a26addafee10768d8ee8212f.
  accessed_at: '2026-11-04T15:27:25.531890Z'
  support: context_only
  summary: 'Current route status 404; HTTP Error 404: Not Found. No successful body
    or negative scientific conclusion derived. Successful retries/abstracts/indexed
    excerpts are separately scoped.'
  snapshot_sha256: 28d8b32688722232ca9d1168cb41a11b3f74d8cef50d0b2cfc0bc4250e894261
- evidence_id: plaque-gakh2002-metadata
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1016%2Fs0167-4889%2802%2900265-3&format=json&resultType=core&pageSize=5
  locator: Exact DOI query returned zero results Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/gakh2002-metadata.raw
    SHA256 5a2ef4b85b2dcb59a9277d9a2b162de6491a1bf366b8e1c15b2b62f8b194218a; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/gakh2002-metadata.receipt.json
    SHA256 e0db96a69f95f9f72764d7c5330d446021ac8d2e77009fc027ed284f81b65092.
  accessed_at: '2026-11-04T15:26:32.953215Z'
  support: context_only
  summary: This spelling/query produced no match; PMID12191769 separately succeeds.
    No claim that the citation or review is absent.
  snapshot_sha256: 5a2ef4b85b2dcb59a9277d9a2b162de6491a1bf366b8e1c15b2b62f8b194218a
  search_scope: Europe PMC exact DOI query in reference URL, resultType=core/pageSize5;
    only this returned response, actual timestamp. A zero query result is not bibliographic
    absence.
- evidence_id: plaque-PMC6010339-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC6010339.1/PMC6010339.1.xml
  locator: Genuine JATS Introduction s1, Results s2-1 through s2-5, Discussion s3,
    Methods s4-1 and s4-4 through s4-7; embedded captions; front permissions. No separate
    supplements or non-Fig5 pixels. Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/PMC6010339-jats.raw
    SHA256 b3015693fe625623165bc43f68c28ecaf411a5927a5d5bd092ee9f8b48746f5c; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/PMC6010339-jats.receipt.json
    SHA256 1f1c31caa1bc03a0d6d916c343f219666ce0e3491af3eb2da7ef2e9dfe810675.
  accessed_at: '2026-11-04T15:26:42.860746Z'
  support: supports
  summary: Native MIM composition and reciprocal heterologous complementation are
    supported with substrate and host limits. Figure5 measures mitochondrial morphology
    rescue in W303 yeast, not direct MIM localization. pATOM36 remains an evolutionarily
    distinct trypanosome protein.
  snapshot_sha256: b3015693fe625623165bc43f68c28ecaf411a5927a5d5bd092ee9f8b48746f5c
- evidence_id: plaque-PMC6965732-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC6965732.1/PMC6965732.1.xml
  locator: Genuine JATS Results sec2.1/sec2.3/sec2.4 and Discussion sec3 including
    limitations, Fig1/2/4/7 text captions; no other Methods/supplements/pixels Raw
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/PMC6965732-jats.raw
    SHA256 f6bd13aad6474886ce6b05e1865979c0b31b7433d66486451676b59b12c29447; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/PMC6965732-jats.receipt.json
    SHA256 c6890e8f5b571a52ddde75a0c77a4c73f958f88b9c6d7409e19daecbaaf255ca.
  accessed_at: '2026-11-04T15:26:43.303654Z'
  support: supports
  summary: Steady-state/localization assays distinguish strong Msp1, moderate Gem1
    and largely independent Fis1/Mcr1 behavior. This does not refute context-specific
    in-vitro import dependence; indirect effects and alternate paths remain explicit.
  snapshot_sha256: f6bd13aad6474886ce6b05e1865979c0b31b7433d66486451676b59b12c29447
- evidence_id: plaque-kline2006-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2063780.1/PMC2063780.1.xml
  locator: Genuine JATS Introduction, Results subsections and Fig1-5 captions, protein
    expression/chromatography and IF Methods; no figure pixels, movies or independent
    supplementary data Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/kline2006-jats.raw
    SHA256 c31e71239af3e5dbd54160b0c4567cf64f5f0f08e186b2b10c170f741400b28f; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/kline2006-jats.receipt.json
    SHA256 a7414a442932858714388cdc2818f9be0df730d6d76fd06481da7afd99bcf1c7.
  accessed_at: '2026-11-04T15:27:25.531625Z'
  support: supports
  summary: Four human proteins were coexpressed in E. coli and copurified as a stable
    complex. Endogenous HeLa fractionation and human/chicken depletion/localization
    experiments are distinct. This genuinely supports the new reconstituted-human-complex
    note, without treating E. coli as a native MIS12 host.
  snapshot_sha256: c31e71239af3e5dbd54160b0c4567cf64f5f0f08e186b2b10c170f741400b28f
- evidence_id: plaque-dewulf2003-legacy
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC289150/
  locator: Genuine HTML abstract/Introduction and focused Mtw1 Results paragraphs
    extracted at text lines1481-1510, selected Discussion1542/1547/1549 and Methods1559;
    no pixels or supplements Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/dewulf2003-legacy.raw
    SHA256 6d37dc17fba5e8d452776b6fec67ac84fb6e0fcdb9056a51019e7f27a61be122; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/dewulf2003-legacy.receipt.json
    SHA256 a771b3b7bd7f503f84517923914aa0b66aaf4df46bc39888d8854ab639fb1d5d.
  accessed_at: '2026-11-04T15:28:39.096578Z'
  support: supports
  summary: Yeast Mtw1/Nnf1/Nsl1/Dsn1 association, heterogeneous hydrodynamic species
    and conditional partner stability/CEN localization support bounded membership.
    The studied MIND, COMA and Ndc80 CEN-association independence prevents a universal
    yeast recruitment-dependency inference.
  snapshot_sha256: 6d37dc17fba5e8d452776b6fec67ac84fb6e0fcdb9056a51019e7f27a61be122
- evidence_id: plaque-doan2020-web-indexed
  kind: primary_source
  reference: https://doi.org/10.1016/j.celrep.2020.107567
  locator: Returned indexed official Freiburg PDF introduction/composition and selected
    initial Results only; indexed crawl predates review, current local reinspection
    time retained; no terminal HTTP200 PDF or pixel claim Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/doan2020-web-indexed.json
    SHA256 c46c65a969788b17ab990aecb7c18952fb94183671312e99e2abbb66dde69372; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/doan2020-web-indexed.receipt.json
    SHA256 2f8ace48fa8289cbc7785418080e0bfb16e9c6d9d6114940b78726d8e8bfdd30.
  accessed_at: '2026-11-04T15:30:27.645905Z'
  support: partial
  summary: Bounded primary-paper text supports MIM import/partner populations with
    distinct experiments and background composition. Exchange is a proposed model;
    no single TOM-MIM-SAM supercomplex or universal copy-count assay is inferred.
  snapshot_sha256: c46c65a969788b17ab990aecb7c18952fb94183671312e99e2abbb66dde69372
- evidence_id: plaque-doan2020-web-sections
  kind: primary_source
  reference: https://doi.org/10.1016/j.celrep.2020.107567
  locator: Returned indexed official Freiburg PDF Results/excerpt lines113-177,194-209,234-346,347-422
    and partial Discussion445-468, selected resource table830-878; indexed crawl predates
    review, current local reinspection time retained; no terminal HTTP200 PDF or pixel
    claim Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/doan2020-web-sections.json
    SHA256 11f57186e0c34cf14f07d6c915fdc805bd6882b42e426379ed402f21ff1408dd; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/doan2020-web-sections.receipt.json
    SHA256 a6e91dbb97ca71e868f9f6e0105e41d52f18ff7d30e0ac31d396787ce7b3313a.
  accessed_at: '2026-11-04T15:30:27.645665Z'
  support: partial
  summary: Bounded primary-paper text supports MIM import/partner populations with
    distinct experiments and background composition. Exchange is a proposed model;
    no single TOM-MIM-SAM supercomplex or universal copy-count assay is inferred.
  snapshot_sha256: 11f57186e0c34cf14f07d6c915fdc805bd6882b42e426379ed402f21ff1408dd
- evidence_id: plaque-doan2020-web-methods
  kind: primary_source
  reference: https://doi.org/10.1016/j.celrep.2020.107567
  locator: Returned indexed official Freiburg PDF lines391-497,876-954,982-1040 including
    SAM/Tom6, Discussion, YPH499 backgrounds and selected import Methods; indexed
    crawl predates review, current local reinspection time retained; no terminal HTTP200
    PDF or pixel claim Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/doan2020-web-methods.json
    SHA256 0ff99bc65a90b78ebc30318b871af09d8c1bdeda141f94831c20002695bb2275; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/doan2020-web-methods.receipt.json
    SHA256 76d46759288dc799826544d54b284f7c0dd48242b80e0adee0db4e56e669c4ff.
  accessed_at: '2026-11-04T15:36:53.505838Z'
  support: partial
  summary: Bounded primary-paper text supports MIM import/partner populations with
    distinct experiments and background composition. Exchange is a proposed model;
    no single TOM-MIM-SAM supercomplex or universal copy-count assay is inferred.
  snapshot_sha256: 0ff99bc65a90b78ebc30318b871af09d8c1bdeda141f94831c20002695bb2275
- evidence_id: plaque-dimmer2012-web-search
  kind: search
  reference: https://pubmed.ncbi.nlm.nih.gov/22467864/
  locator: Only returned primary-paper indexed text; composition/association Results
    around Fig2, Discussion and W303/YPH499 Methods; no full PDF or pixels claimed
    Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/dimmer2012-web-search.json
    SHA256 c5022801dbb564d8e936a328d397950d2cd94da3413ce64972bf6d5e7497b7fc; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/dimmer2012-web-search.receipt.json
    SHA256 466ec24938ab463a41024c02971b9191e9ab36f9954010b22bee8b5e230d7ff8.
  accessed_at: '2026-11-04T15:42:07.552396Z'
  support: context_only
  summary: Mim2 affects Mim1 abundance/native assembly, while Mim1 overexpression
    can produce an oligomer without Mim2. Supports a contribution rather than universal
    absolute necessity. Copy-range inference remains qualified.
  snapshot_sha256: c5022801dbb564d8e936a328d397950d2cd94da3413ce64972bf6d5e7497b7fc
  search_scope: 'Web search exact queries: "Mim2" "stability" "Mim1" Dimmer; "A crucial
    role for Mim2" "complex" stability. Two queries only, returned primary PubMed/paper
    representation inspected; unrelated hits excluded; actual capture time retained.'
- evidence_id: plaque-dimmer2012-web-indexed
  kind: primary_source
  reference: https://doi.org/10.1242/jcs.103804
  locator: Only returned primary-paper indexed text; composition/association Results
    around Fig2, Discussion and W303/YPH499 Methods; no full PDF or pixels claimed
    Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/dimmer2012-web-indexed.json
    SHA256 3cadce26ae441356a143acc53574d195a2ae3ed7ae9ded4a4bd6a9004226153e; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/dimmer2012-web-indexed.receipt.json
    SHA256 523e2cca9b5790911ec29746e0e41db546dcb40a58b197dc615a42d052df3ac2.
  accessed_at: '2026-11-04T15:42:07.552396Z'
  support: partial
  summary: Mim2 affects Mim1 abundance/native assembly, while Mim1 overexpression
    can produce an oligomer without Mim2. Supports a contribution rather than universal
    absolute necessity. Copy-range inference remains qualified.
  snapshot_sha256: 3cadce26ae441356a143acc53574d195a2ae3ed7ae9ded4a4bd6a9004226153e
- evidence_id: plaque-dimmer2012-web-sections
  kind: primary_source
  reference: https://doi.org/10.1242/jcs.103804
  locator: Only returned primary-paper indexed text; composition/association Results
    around Fig2, Discussion and W303/YPH499 Methods; no full PDF or pixels claimed
    Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/dimmer2012-web-sections.json
    SHA256 727342004b66532532b585c47e359222c31bdf4aea3fcbd26b6e13fd602ee6ba; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/dimmer2012-web-sections.receipt.json
    SHA256 fb6e2f03b469b3e7c42e4e3509bfc1451d2b73dea1114c812586ab294bf8b086.
  accessed_at: '2026-11-04T15:42:07.552396Z'
  support: partial
  summary: Mim2 affects Mim1 abundance/native assembly, while Mim1 overexpression
    can produce an oligomer without Mim2. Supports a contribution rather than universal
    absolute necessity. Copy-range inference remains qualified.
  snapshot_sha256: 727342004b66532532b585c47e359222c31bdf4aea3fcbd26b6e13fd602ee6ba
- evidence_id: plaque-mim-figure5
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC6010339.1/elife-34488-fig5.jpg
  locator: Actual retrieved Fig5 JPEG; every panel viewed independently; byte comparison
    with maintained image Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/mim-figure5.raw
    SHA256 cdfb8f43e86424b85aa88ac2baa741035d8f107d58fe3b26ad48d595017a5af1; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/mim-figure5.receipt.json
    SHA256 92438c7403fa751fb9530686f6e9c3ba1afea1f59cf132b1c1d83b03adefa616.
  accessed_at: '2026-11-04T15:26:43.427381Z'
  support: supports
  summary: Source JPEG and maintained image are byte-identical, SHA256 cdfb8f43e86424b85aa88ac2baa741035d8f107d58fe3b26ad48d595017a5af1;
    MD5 be1d9b473460fba31d802e0c3ea5a1bc. Mito-GFP/brightfield morphology and quantified
    rescue, not MIM molecular localization. W303 context, 5 micrometer scale and three
    experiments/at least100 cells each follow caption.
  snapshot_sha256: cdfb8f43e86424b85aa88ac2baa741035d8f107d58fe3b26ad48d595017a5af1
- evidence_id: plaque-mim-package
  kind: database
  reference: https://pmc-oa-opendata.s3.amazonaws.com/?list-type=2&prefix=PMC6010339.1/
  locator: Complete bounded object listing prefix PMC6010339.1, Fig5 object entry
    only used Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/mim-package.raw
    SHA256 340f03ca3f6ab6f9e5dec87a5d99328e7b3b39bac9099fdca581d0fc3be55de1; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-plaque/mim-package.receipt.json
    SHA256 95fbb06b3abff1ae3032eb76c243d1260a0b927b5d5cbcbbc24bc41562973739.
  accessed_at: '2026-11-04T15:27:25.532325Z'
  support: supports
  summary: Package Fig5 ETag/size agree with downloaded JPEG. Rights come from genuine
    article CC BY4.0 permissions, not an inferred listing license.
  snapshot_sha256: 340f03ca3f6ab6f9e5dec87a5d99328e7b3b39bac9099fdca581d0fc3be55de1
- evidence_id: plaque-maintained-image
  kind: record_content
  reference: data/images/other/mim_complex/pmc6010339_fig5.jpg
  locator: Actual maintained pixels and image metadata; compared to primary Figure5/caption/permissions
  accessed_at: '2026-11-04T15:43:22.639944Z'
  support: supports
  summary: Displayed image matches source bytewise; author credit and CC BY4.0 attribution
    are supported; no new image or derivative created.
  snapshot_sha256: cdfb8f43e86424b85aa88ac2baa741035d8f107d58fe3b26ad48d595017a5af1
- evidence_id: plaque-adapter-catalogue
  kind: search
  reference: https://imodulondb.org/api/organisms
  locator: Complete official 20 organism rows and 28 organism-dataset entries independently
    reread Raw snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/adapter-catalogue.raw
    SHA256 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/adapter-catalogue.receipt.json
    SHA256 2a10b30f380db880f8cad367d0403031d9cddd6478acdf8f16909187be175c0e.
  accessed_at: '2026-11-04T15:24:16.251933Z'
  support: context_only
  summary: No Saccharomyces, other fungal, human or chicken dataset occurs in this
    catalogue response. Positive MIM import, MIS12 assembly/recruitment and IMP proteolysis
    require applicability assessment, but no matched natural-host downstream query
    is justified. Heterologous bacterial expression is not an E. coli biological proxy.
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  search_scope: Official iModulonDB /api/organisms, complete returned catalogue without
    pagination or query truncation; all20 organisms/28 dataset entries inspected.
    Exact snapshot/access time of peer retrieval retained; no downstream gene/module
    query made for an uncovered host and no biological-absence inference.
- evidence_id: plaque-mim-peer-challenge
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/mim-snippet-provenance-challenge.json
  locator: Separate independent bounded snippet comparison and source-tier challenge
  accessed_at: '2026-11-04T15:43:22.639944Z'
  support: supports
  summary: Independent reader corroborates the wording correction while preserving
    supported composition and no universal necessity reversal.
  snapshot_sha256: 020a19ab303dce1241af751b051cc475fc0615002f9ceaaeb289d0aeb75930a9
- evidence_id: plaque-historical-t3-micro60-doan2020-freidok
  kind: validation
  reference: https://freidok.uni-freiburg.de/files/165604/PIIS2211124720305167.pdf
  locator: Historical original row micro60-doan2020-freidok in reviews/structured/20261022T084807Z-mim-complex-audit/review.yaml.
    Actual final response title/body and transport metadata; unsuccessful body retrieval.
  accessed_at: '2026-10-22T08:25:56.360140Z'
  support: context_only
  summary: 'Historical observation, not a fresh fetch: This HTTP200 response is an
    institutional IT/security notice, not the cited paper body. Its bytes are excluded
    from scientific support; genuine bounded browser text is separately retained.'
  snapshot_sha256: 52d302d4f2e54ce23b47ca8deb0eb52e2a4aa0a09ef50e61f372a6f864c26b1c
- evidence_id: plaque-historical-t3-micro60-doan2020-storage
  kind: validation
  reference: https://storage.freidok.ub.uni-freiburg.de/publications/165604/ieaccMPhkWq1nfS5/PIIS2211124720305167.pdf
  locator: Historical original row micro60-doan2020-storage in reviews/structured/20261022T084807Z-mim-complex-audit/review.yaml.
    Actual final response title/body and transport metadata; unsuccessful body retrieval.
  accessed_at: '2026-10-22T08:25:56.359868Z'
  support: context_only
  summary: 'Historical observation, not a fresh fetch: This HTTP200 response is an
    institutional IT/security notice, not the cited paper body. Its bytes are excluded
    from scientific support; genuine bounded browser text is separately retained.'
  snapshot_sha256: 52d302d4f2e54ce23b47ca8deb0eb52e2a4aa0a09ef50e61f372a6f864c26b1c
- evidence_id: plaque-historical-t5-micro60-jan2000-publisher
  kind: validation
  reference: https://link.springer.com/article/10.1007/s004380051192
  locator: Historical original row micro60-jan2000-publisher in reviews/structured/20261022T084808Z-mitochondrial-inner-membrane-peptidase-complex-audit/review.yaml.
    Actual response content/transport and 3038-byte challenge payload.
  accessed_at: '2026-10-22T08:25:56.360392Z'
  support: context_only
  summary: 'Historical observation, not a fresh fetch: The retained HTTP200 response
    is a short client challenge, not the cited primary article body. Scientific support
    is limited to the independently retained complete MED abstract.'
  snapshot_sha256: 32ed63159c77e21ee19ca1b9aa3213ccf0218eb59539560b132a8e68ef0e18ea
- evidence_id: plaque-historical-t5-micro60-jan2000-pdf
  kind: validation
  reference: https://link.springer.com/content/pdf/10.1007/s004380051192.pdf
  locator: Historical original row micro60-jan2000-pdf in reviews/structured/20261022T084808Z-mitochondrial-inner-membrane-peptidase-complex-audit/review.yaml.
    Actual response content/transport and 3038-byte challenge payload.
  accessed_at: '2026-10-22T08:25:56.360438Z'
  support: context_only
  summary: 'Historical observation, not a fresh fetch: The retained HTTP200 response
    is a short client challenge, not the cited primary article body. Scientific support
    is limited to the independently retained complete MED abstract.'
  snapshot_sha256: 32ed63159c77e21ee19ca1b9aa3213ccf0218eb59539560b132a8e68ef0e18ea
- evidence_id: plaque-historical-t5-micro60-gakh2002-publisher
  kind: database
  reference: https://doi.org/10.1016/s0167-4889(02)00265-3
  locator: Historical original row micro60-gakh2002-publisher in reviews/structured/20261022T084808Z-mitochondrial-inner-membrane-peptidase-complex-audit/review.yaml.
    Actual returned JSON type and metadata; no publisher full-text claim.
  accessed_at: '2026-10-22T08:25:56.563037Z'
  support: context_only
  summary: 'Historical observation, not a fresh fetch: The DOI route returned Crossref
    JSON bibliographic metadata, not the review body. The secondary review is assessed
    only at complete native abstract tier.'
  snapshot_sha256: 20301c7adc991c604e018876c17995b38e10e7756d92ab5ee352fd0def5dd392
- evidence_id: septin-review-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Applicable native review instructions
  summary: Whole-record molecular and pathway assertions trigger structured-source
    coverage checks; a lack of expression inference is not an adequate exemption.
  accessed_at: '2026-11-04T15:44:30.976471Z'
  support: supports
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: septin-curation-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Applicable native review instructions
  summary: Structure identity, exact source scope, valid protein families/classes,
    unknown necessity and append-only historical discussion contract.
  accessed_at: '2026-11-04T15:44:30.976471Z'
  support: supports
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
- evidence_id: septin-protein-policy
  kind: authority
  reference: .claude/skills/uniprot-protein-examples/SKILL.md
  locator: Applicable native review instructions
  summary: Verify exact accession, primary gene/alias, taxon and current query scope;
    example identity is distinct from membership, activity and necessity.
  accessed_at: '2026-11-04T15:44:30.976471Z'
  support: supports
  snapshot_sha256: 6462894c8257823bae2b175c34693cd42f11ff9269a3829c15b9286ba6d7c876
- evidence_id: septin-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Applicable native review instructions
  summary: Preserve explicit formation versus function scope and distinguish structural
    membership from time-resolved assembly or loss-of-formation experiments.
  accessed_at: '2026-11-04T15:44:30.976471Z'
  support: supports
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: septin-literature-policy
  kind: authority
  reference: .claude/skills/literature-evidence/SKILL.md
  locator: Applicable native review instructions
  summary: Read actual source content; distinguish metadata, abstract, body, image
    and failed access. No paraphrase may be represented as a verbatim snippet.
  accessed_at: '2026-11-04T15:44:30.976471Z'
  support: supports
  snapshot_sha256: f7c3c594b5fb2cd7d4d700844fce3b97c91cc382d4fdca8b2e2a96cf16abd41b
- evidence_id: septin-record-mitochondrial_lon_protease_complex
  kind: record_content
  reference: data/structures/other/mitochondrial_lon_protease_complex.yaml
  locator: Complete current YAML, including discussions, quantities, components, evidence
    and graph
  summary: All current assertions independently inspected. Current record hash equals
    the original frozen target hash; no stale refresh is required for this assigned
    target.
  accessed_at: '2026-11-04T15:44:30.976471Z'
  support: supports
  snapshot_sha256: 22c985cbd94a32e0a04e1ba4b7f77e796ef99815390b9165a3b15b987429d5d6
- evidence_id: septin-original-mitochondrial_lon_protease_complex
  kind: prior_review
  reference: reviews/structured/20261022T084809Z-mitochondrial-lon-protease-complex-audit/review.yaml
  locator: Complete immutable original review and exact target/finding/check/evidence
    scope
  summary: Original verdict, all evidence rows, formal applicability exclusion, findings
    and actions read. Historical global check execution is attributed to its actual
    earlier batch, not misrepresented as a new execution.
  accessed_at: '2026-11-04T15:44:30.976471Z'
  support: supports
  snapshot_sha256: 45c479278c71463c35d945a3042c7275494464a564b7f16595ca190e42c0ca38
- evidence_id: septin-record-mitochondrial_multifunctional_assembly
  kind: record_content
  reference: data/structures/other/mitochondrial_multifunctional_assembly.yaml
  locator: Complete current YAML, including discussions, quantities, components, evidence
    and graph
  summary: All current assertions independently inspected. Current record hash equals
    the original frozen target hash; no stale refresh is required for this assigned
    target.
  accessed_at: '2026-11-04T15:44:30.976471Z'
  support: supports
  snapshot_sha256: bb1a36eee48a44140250e04951a42f149f5de60affd5e146ba8f89f8a6e48858
- evidence_id: septin-original-mitochondrial_multifunctional_assembly
  kind: prior_review
  reference: reviews/structured/20261022T084810Z-mitochondrial-multifunctional-assembly-audit/review.yaml
  locator: Complete immutable original review and exact target/finding/check/evidence
    scope
  summary: Original verdict, all evidence rows, formal applicability exclusion, findings
    and actions read. Historical global check execution is attributed to its actual
    earlier batch, not misrepresented as a new execution.
  accessed_at: '2026-11-04T15:44:30.976471Z'
  support: supports
  snapshot_sha256: b8b8e993357ca73262007d2b28664ed80d09cdbd06c88cbc8466b759c36ce7d4
- evidence_id: septin-record-mitochondrial_outer_membrane_translocase_complex
  kind: record_content
  reference: data/structures/other/mitochondrial_outer_membrane_translocase_complex.yaml
  locator: Complete current YAML, including discussions, quantities, components, evidence
    and graph
  summary: All current assertions independently inspected. Current record hash equals
    the original frozen target hash; no stale refresh is required for this assigned
    target.
  accessed_at: '2026-11-04T15:44:30.976471Z'
  support: supports
  snapshot_sha256: a9facce19eda1794aefb3bef7b36fe07ba5c3a942220a4379c5569de4150022e
- evidence_id: septin-original-mitochondrial_outer_membrane_translocase_complex
  kind: prior_review
  reference: reviews/structured/20261022T084810Z-mitochondrial-outer-membrane-translocase-complex-audit/review.yaml
  locator: Complete immutable original review and exact target/finding/check/evidence
    scope
  summary: Original verdict, all evidence rows, formal applicability exclusion, findings
    and actions read. Historical global check execution is attributed to its actual
    earlier batch, not misrepresented as a new execution.
  accessed_at: '2026-11-04T15:44:30.976471Z'
  support: supports
  snapshot_sha256: 72a7419c81e55ff10873a91cfddab435d2d646018402fc578dcfda39d7d8def0
- evidence_id: septin-record-mitochondrial_prohibitin_complex
  kind: record_content
  reference: data/structures/other/mitochondrial_prohibitin_complex.yaml
  locator: Complete current YAML, including discussions, quantities, components, evidence
    and graph
  summary: All current assertions independently inspected. Current record hash equals
    the original frozen target hash; no stale refresh is required for this assigned
    target.
  accessed_at: '2026-11-04T15:44:30.976471Z'
  support: supports
  snapshot_sha256: a2a0c89fc814c0dba32ef8a1b90246ced003e274382c67d78794cbd86e9b7453
- evidence_id: septin-original-mitochondrial_prohibitin_complex
  kind: prior_review
  reference: reviews/structured/20261022T084811Z-mitochondrial-prohibitin-complex-audit/review.yaml
  locator: Complete immutable original review and exact target/finding/check/evidence
    scope
  summary: Original verdict, all evidence rows, formal applicability exclusion, findings
    and actions read. Historical global check execution is attributed to its actual
    earlier batch, not misrepresented as a new execution.
  accessed_at: '2026-11-04T15:44:30.976471Z'
  support: supports
  snapshot_sha256: d9157ec12ac92d7f92166d6921a1542bdc796a7ce9cf4c7bb81dd1e3c4efd17f
- evidence_id: septin-original-native-checks
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/original-checks.json
  locator: Fresh guarded PR2397 four-pair validation/render and 53 historical input
    occurrences
  summary: All four original envelopes validate and render exactly to their committed
    Markdown. All 51 current frozen inputs match worktree and source commit, and all
    53 original historical input occurrences match their original commits. Uses only
    current PR2397 receipt bytes; no old PR2396 auxiliary receipt is a dependency.
  accessed_at: '2026-11-04T15:44:30.976471Z'
  support: supports
  snapshot_sha256: 2e6ea42c3e7928ec210a6854005e23dd8cc42ad2e3c805e15a5e220ef72364f9
- evidence_id: septin-native-mitochondrial_lon_protease_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_lon_protease_complex-uniprot-verify-receipt.json
  locator: Actual command [".venv/bin/python", "scripts/uniprot_genes.py", "--record",
    "data/structures/other/mitochondrial_lon_protease_complex.yaml", "--verify"];
    stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_lon_protease_complex-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 1 maintained protein-example occurrences; 1 typed GENE_OR_PROTEIN nodes.
    The one node is COVERED at the reference-correspondence level. Accession checks
    do not prove membership or necessity. Receipt SHA256 01465efc8a87c6aaa26e72f9a741208bbeb9d5d78932363d1c96a714165c5c94.
  accessed_at: '2026-11-04T15:22:32.285898Z'
  support: supports
  snapshot_sha256: 01465efc8a87c6aaa26e72f9a741208bbeb9d5d78932363d1c96a714165c5c94
- evidence_id: septin-native-mitochondrial_lon_protease_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_lon_protease_complex-uniprot-causal-receipt.json
  locator: Actual command [".venv/bin/python", "scripts/uniprot_genes.py", "--record",
    "data/structures/other/mitochondrial_lon_protease_complex.yaml", "--causal-graphs"];
    stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_lon_protease_complex-uniprot-causal.log
    SHA256 593a4556e111d3a1cfcf401fad0bc11ad1edf7df8b98ea85523db231d52f846b
  summary: 1 maintained protein-example occurrences; 1 typed GENE_OR_PROTEIN nodes.
    The one node is COVERED at the reference-correspondence level. Accession checks
    do not prove membership or necessity. Receipt SHA256 f6c97cc1a9cc4e920e1c7060fcbae5c90761da82273502c42665daa936c88699.
  accessed_at: '2026-11-04T15:22:32.700334Z'
  support: supports
  snapshot_sha256: f6c97cc1a9cc4e920e1c7060fcbae5c90761da82273502c42665daa936c88699
- evidence_id: septin-native-mitochondrial_multifunctional_assembly-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_multifunctional_assembly-uniprot-verify-receipt.json
  locator: Actual command [".venv/bin/python", "scripts/uniprot_genes.py", "--record",
    "data/structures/other/mitochondrial_multifunctional_assembly.yaml", "--verify"];
    stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_multifunctional_assembly-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 5 maintained protein-example occurrences; 1 typed GENE_OR_PROTEIN nodes.
    The one node is COVERED at the reference-correspondence level. Accession checks
    do not prove membership or necessity. Receipt SHA256 94c00fb08c4a1ba0d01f6347201fdd495e613ff5c6abfb5af8bd1ee84bdeb303.
  accessed_at: '2026-11-04T15:22:33.893561Z'
  support: supports
  snapshot_sha256: 94c00fb08c4a1ba0d01f6347201fdd495e613ff5c6abfb5af8bd1ee84bdeb303
- evidence_id: septin-native-mitochondrial_multifunctional_assembly-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_multifunctional_assembly-uniprot-causal-receipt.json
  locator: Actual command [".venv/bin/python", "scripts/uniprot_genes.py", "--record",
    "data/structures/other/mitochondrial_multifunctional_assembly.yaml", "--causal-graphs"];
    stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_multifunctional_assembly-uniprot-causal.log
    SHA256 2b1888389fba30f8794923be1fc9b5ba2c9bcaf92ef659ae0378f0c848a48d47
  summary: 5 maintained protein-example occurrences; 1 typed GENE_OR_PROTEIN nodes.
    The one node is COVERED at the reference-correspondence level. Accession checks
    do not prove membership or necessity. Receipt SHA256 67d79650ca9667aa2ad109fcf1ec135fb5940c2bcc93d523a1f8f7ad8c802347.
  accessed_at: '2026-11-04T15:22:34.298796Z'
  support: supports
  snapshot_sha256: 67d79650ca9667aa2ad109fcf1ec135fb5940c2bcc93d523a1f8f7ad8c802347
- evidence_id: septin-native-mitochondrial_outer_membrane_translocase_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_outer_membrane_translocase_complex-uniprot-verify-receipt.json
  locator: Actual command [".venv/bin/python", "scripts/uniprot_genes.py", "--record",
    "data/structures/other/mitochondrial_outer_membrane_translocase_complex.yaml",
    "--verify"]; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_outer_membrane_translocase_complex-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 0 maintained protein-example occurrences; 0 typed GENE_OR_PROTEIN nodes.
    The inventory and typed-node scope are empty; exit0 does not certify unrepresented
    molecular coverage. Accession checks do not prove membership or necessity. Receipt
    SHA256 72ee8e67c723c5a5ea530c67c701bc972ef5527094395b7b549b3e2cb60e43eb.
  accessed_at: '2026-11-04T15:22:34.698937Z'
  support: supports
  snapshot_sha256: 72ee8e67c723c5a5ea530c67c701bc972ef5527094395b7b549b3e2cb60e43eb
- evidence_id: septin-native-mitochondrial_outer_membrane_translocase_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_outer_membrane_translocase_complex-uniprot-causal-receipt.json
  locator: Actual command [".venv/bin/python", "scripts/uniprot_genes.py", "--record",
    "data/structures/other/mitochondrial_outer_membrane_translocase_complex.yaml",
    "--causal-graphs"]; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_outer_membrane_translocase_complex-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: 0 maintained protein-example occurrences; 0 typed GENE_OR_PROTEIN nodes.
    The inventory and typed-node scope are empty; exit0 does not certify unrepresented
    molecular coverage. Accession checks do not prove membership or necessity. Receipt
    SHA256 1b2129f94baf96bed2f0c72c4f68c439c81f1063f02cf0a9af95ec6dda6018be.
  accessed_at: '2026-11-04T15:22:35.085772Z'
  support: supports
  snapshot_sha256: 1b2129f94baf96bed2f0c72c4f68c439c81f1063f02cf0a9af95ec6dda6018be
- evidence_id: septin-native-mitochondrial_prohibitin_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_prohibitin_complex-uniprot-verify-receipt.json
  locator: Actual command [".venv/bin/python", "scripts/uniprot_genes.py", "--record",
    "data/structures/other/mitochondrial_prohibitin_complex.yaml", "--verify"]; stdout
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_prohibitin_complex-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 0 maintained protein-example occurrences; 0 typed GENE_OR_PROTEIN nodes.
    The inventory and typed-node scope are empty; exit0 does not certify unrepresented
    molecular coverage. Accession checks do not prove membership or necessity. Receipt
    SHA256 9bee8fa67f45ef4cf49f4685a60555891f81b8b65ca9762c8c14f1c1ca060500.
  accessed_at: '2026-11-04T15:22:35.476023Z'
  support: supports
  snapshot_sha256: 9bee8fa67f45ef4cf49f4685a60555891f81b8b65ca9762c8c14f1c1ca060500
- evidence_id: septin-native-mitochondrial_prohibitin_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_prohibitin_complex-uniprot-causal-receipt.json
  locator: Actual command [".venv/bin/python", "scripts/uniprot_genes.py", "--record",
    "data/structures/other/mitochondrial_prohibitin_complex.yaml", "--causal-graphs"];
    stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_prohibitin_complex-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: 0 maintained protein-example occurrences; 0 typed GENE_OR_PROTEIN nodes.
    The inventory and typed-node scope are empty; exit0 does not certify unrepresented
    molecular coverage. Accession checks do not prove membership or necessity. Receipt
    SHA256 c1701bcb77aa9ee93f3983ad3ad7058fd12eeb738a73a44250afa9d63f12ee6d.
  accessed_at: '2026-11-04T15:22:35.866672Z'
  support: supports
  snapshot_sha256: c1701bcb77aa9ee93f3983ad3ad7058fd12eeb738a73a44250afa9d63f12ee6d
- evidence_id: septin-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0004176,GO:0005741,GO:0005742,GO:0005743,GO:0005759,GO:0007005,GO:0030150,GO:0035632,GO:0098799,GO:0098800,GO:1905368
  locator: 'Complete eleven-term native response: labels, definitions, synonym types
    and child relations; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/go.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/go.receipt.json'
  summary: GO:0005742 explicitly makes GIP complex a narrow synonym; other exact labels
    and anatomical/function scopes support the records. GO:0030150 covers the complete
    TOM-TIM23-PAM import route, while the TOM record limits its contribution to outer-membrane
    entry. GO:0035632 describes repeating PHB1/PHB2 heterodimers; GO:0007005 retains
    mitochondrial biogenesis as an exact synonym.
  accessed_at: '2026-11-04T15:25:46.880464Z'
  support: supports
  snapshot_sha256: e6a248305bc7752e1bb81d50f22d98da6c5bdd61dadb96af270f922128b26fb7
- evidence_id: septin-go-0005742-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005742/ancestors?relations=is_a
  locator: Complete native is_a ancestor response; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/go-0005742-ancestors.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/go-0005742-ancestors.receipt.json
  summary: Direct current parent and broader ancestry support the recorded mitochondrial
    outer/inner membrane protein-complex classifications; parthood is not inferred
    from is_a alone.
  accessed_at: '2026-11-04T15:26:34.432254Z'
  support: supports
  snapshot_sha256: 2997b2b57b236f7c9b169d20105062ee345a58809ef7ccd432e17a79db3ce91b
- evidence_id: septin-go-0035632-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0035632/ancestors?relations=is_a
  locator: Complete native is_a ancestor response; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/go-0035632-ancestors.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/go-0035632-ancestors.receipt.json
  summary: Direct current parent and broader ancestry support the recorded mitochondrial
    outer/inner membrane protein-complex classifications; parthood is not inferred
    from is_a alone.
  accessed_at: '2026-11-04T15:26:39.449768Z'
  support: supports
  snapshot_sha256: 8fd5b89811be37fa5e75ef2799299a6775422a592ea6ec34dafef8f90a8a6fa7
- evidence_id: septin-tax-4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Native taxon identity and lineage; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/tax-4932.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/tax-4932.receipt.json
  summary: Saccharomyces cerevisiae species, S288C reference strain, and Eukaryota
    are distinct scopes. Reference strain examples do not identify every experimental
    strain or establish universal prevalence.
  accessed_at: '2026-11-04T15:25:46.846752Z'
  support: supports
  snapshot_sha256: 38f43dd1593a1d47416228ae385464f30aeb8302c3aadb45b3588d03744bc814
- evidence_id: septin-tax-559292
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Native taxon identity and lineage; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/tax-559292.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/tax-559292.receipt.json
  summary: Saccharomyces cerevisiae species, S288C reference strain, and Eukaryota
    are distinct scopes. Reference strain examples do not identify every experimental
    strain or establish universal prevalence.
  accessed_at: '2026-11-04T15:25:46.811354Z'
  support: supports
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: septin-tax-2759
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759
  locator: Native taxon identity and lineage; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/tax-2759.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/tax-2759.receipt.json
  summary: Saccharomyces cerevisiae species, S288C reference strain, and Eukaryota
    are distinct scopes. Reference strain examples do not identify every experimental
    strain or establish universal prevalence.
  accessed_at: '2026-11-04T15:26:22.898189Z'
  support: supports
  snapshot_sha256: 61a68c76c70762c97e0b218568ab037d9a30c0207847247e9e055b5764a61634
- evidence_id: septin-go-search-lon
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=Lon+protease&limit=100
  locator: Actual returned QuickGO term-search page; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/go-search-lon.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/go-search-lon.receipt.json
  summary: Inspected 100 returned terms of 204 reported hits. No exact alternative
    structure identity was established within this bounded search; broad Lon/multifunctional
    requests were not exhaustive. The PIM1 response is an obsolete activity term,
    not an exact mitochondrial oligomer identity.
  accessed_at: '2026-11-04T15:25:47.598973Z'
  support: context_only
  snapshot_sha256: d7e2f73b2407e16fb4e542578a176cfacee440243cc05c9409753979b6ec6a50
  search_scope: 'Actual current request https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=Lon+protease&limit=100;
    request parameters {"limit": ["100"], "query": ["Lon protease"]}. Only the retained
    response was inspected; stated page bounds apply. No unrequested result pages
    or biological absence inferred.'
- evidence_id: septin-go-search-pim1
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=Pim1&limit=100
  locator: Actual returned QuickGO term-search page; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/go-search-pim1.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/go-search-pim1.receipt.json
  summary: Inspected 1 returned terms of 1 reported hits. No exact alternative structure
    identity was established within this bounded search; broad Lon/multifunctional
    requests were not exhaustive. The PIM1 response is an obsolete activity term,
    not an exact mitochondrial oligomer identity.
  accessed_at: '2026-11-04T15:25:47.500598Z'
  support: context_only
  snapshot_sha256: 7cf85192a19997aac04c39aeb4aaa07814d6ab9dd21ba88ce1ecc93c2f7dca32
  search_scope: 'Actual current request https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=Pim1&limit=100;
    request parameters {"limit": ["100"], "query": ["Pim1"]}. Only the retained response
    was inspected; stated page bounds apply. No unrequested result pages or biological
    absence inferred.'
- evidence_id: septin-go-search-mimas
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=MIMAS&limit=100
  locator: Actual returned QuickGO term-search page; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/go-search-mimas.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/go-search-mimas.receipt.json
  summary: Inspected 0 returned terms of 0 reported hits. No exact alternative structure
    identity was established within this bounded search; broad Lon/multifunctional
    requests were not exhaustive. The PIM1 response is an obsolete activity term,
    not an exact mitochondrial oligomer identity.
  accessed_at: '2026-11-04T15:26:12.860415Z'
  support: context_only
  snapshot_sha256: f3a7dae9b1e9335291e3940cdf0e5f8dadf9335da7b9547710606b5106c63f86
  search_scope: 'Actual current request https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=MIMAS&limit=100;
    request parameters {"limit": ["100"], "query": ["MIMAS"]}. Only the retained response
    was inspected; stated page bounds apply. No unrequested result pages or biological
    absence inferred.'
- evidence_id: septin-go-search-multifunctional
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=mitochondrial+multifunctional+assembly&limit=100
  locator: Actual returned QuickGO term-search page; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/go-search-multifunctional.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/go-search-multifunctional.receipt.json
  summary: Inspected 100 returned terms of 1353 reported hits. No exact alternative
    structure identity was established within this bounded search; broad Lon/multifunctional
    requests were not exhaustive. The PIM1 response is an obsolete activity term,
    not an exact mitochondrial oligomer identity.
  accessed_at: '2026-11-04T15:26:13.652205Z'
  support: context_only
  snapshot_sha256: f78d58ce5d389a2f225bb5f68c98d3e243ed62361a498312a557143124f0e67d
  search_scope: 'Actual current request https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=mitochondrial+multifunctional+assembly&limit=100;
    request parameters {"limit": ["100"], "query": ["mitochondrial multifunctional
    assembly"]}. Only the retained response was inspected; stated page bounds apply.
    No unrequested result pages or biological absence inferred.'
- evidence_id: septin-ipr-IPR000163
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000163/
  locator: Native metadata, type, family name, signatures and description flags; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR000163.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR000163.receipt.json
  summary: IPR000163 is type family, named Prohibitin. Native member-signature identifiers
    and family boundary inspected. Shared prohibitin family is not an exact PHB1-versus-PHB2
    paralogue split.
  accessed_at: '2026-11-04T15:26:40.058200Z'
  support: supports
  snapshot_sha256: a5538e91cc0c6dad68aa5d385c9f165506535acddba9e5dc8623f7bbd764256a
- evidence_id: septin-ipr-IPR000872
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000872/
  locator: Native metadata, type, family name, signatures and description flags; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR000872.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR000872.receipt.json
  summary: IPR000872 is type family, named Tafazzin. Native member-signature identifiers
    and family boundary inspected.
  accessed_at: '2026-11-04T15:26:17.645614Z'
  support: supports
  snapshot_sha256: 898276f0ae23b9b035e778d6f0291cc781d26845babfd824662c506e3639563e
- evidence_id: septin-ipr-IPR002056
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002056/
  locator: Native metadata, type, family name, signatures and description flags; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR002056.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR002056.receipt.json
  summary: IPR002056 is type family, named Protein import receptor MAS20. Native member-signature
    identifiers and family boundary inspected.
  accessed_at: '2026-11-04T15:26:36.855300Z'
  support: supports
  snapshot_sha256: 39218d6b3819ff08bb08c779c694f86ee61a14c09413ec3ea3d82c033b45f4f7
- evidence_id: septin-ipr-IPR002113
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002113/
  locator: Native metadata, type, family name, signatures and description flags; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR002113.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR002113.receipt.json
  summary: IPR002113 is type family, named ADP/ATP carrier protein, eukaryotic type.
    Native member-signature identifiers and family boundary inspected.
  accessed_at: '2026-11-04T15:26:14.368278Z'
  support: supports
  snapshot_sha256: 1a434ed1bd36951bcfa20905adf62055cd66f8074a1e85a2d7ed744edf7a4e9f
- evidence_id: septin-ipr-IPR005683
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005683/
  locator: Native metadata, type, family name, signatures and description flags; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR005683.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR005683.receipt.json
  summary: IPR005683 is type family, named Mitochondrial import receptor subunit Tom22.
    Native member-signature identifiers and family boundary inspected.
  accessed_at: '2026-11-04T15:26:36.240288Z'
  support: supports
  snapshot_sha256: 5510c6aaedb6effa6107ed8e3ca400d2a1b91799038f0fc5eecfe55f949489e7
- evidence_id: septin-ipr-IPR005686
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005686/
  locator: Native metadata, type, family name, signatures and description flags; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR005686.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR005686.receipt.json
  summary: IPR005686 is type family, named Mitochondrial import receptor subunit Tom40,
    fungi. Native member-signature identifiers and family boundary inspected.
  accessed_at: '2026-11-04T15:26:36.151183Z'
  support: supports
  snapshot_sha256: 4918743a6b99f2041f1891d7d44c74fb21f4ec9e47da25242c9d5c4d8e537427
- evidence_id: septin-ipr-IPR005687
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005687/
  locator: Native metadata, type, family name, signatures and description flags; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR005687.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR005687.receipt.json
  summary: IPR005687 is type family, named Mitochondrial outer membrane translocase
    complex, subunit Tom70. Native member-signature identifiers and family boundary
    inspected.
  accessed_at: '2026-11-04T15:26:36.867347Z'
  support: supports
  snapshot_sha256: 61d5ce706787a28482fe55aa414e5103b36e8cabe5456cccfbdaf047703a2821
- evidence_id: septin-ipr-IPR012621
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR012621/
  locator: Native metadata, type, family name, signatures and description flags; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR012621.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR012621.receipt.json
  summary: IPR012621 is type family, named Mitochondrial import receptor subunit TOM7.
    Native member-signature identifiers and family boundary inspected.
  accessed_at: '2026-11-04T15:26:37.483008Z'
  support: supports
  snapshot_sha256: 0c2ffdc1819b020bbb2e36f27dbf9256c9d95a8ee587dc890f896f372b8ae5de
- evidence_id: septin-ipr-IPR019603
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR019603/
  locator: Native metadata, type, family name, signatures and description flags; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR019603.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR019603.receipt.json
  summary: IPR019603 is type family, named Mitochondrial outer membrane translocase
    complex, subunit Tom5. Native member-signature identifiers and family boundary
    inspected.
  accessed_at: '2026-11-04T15:26:37.356212Z'
  support: supports
  snapshot_sha256: 2c7a62970335a1447895f03c096ad456f4022f63957afeceea9c301b76668283
- evidence_id: septin-ipr-IPR020266
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR020266/
  locator: Native metadata, type, family name, signatures and description flags; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR020266.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR020266.receipt.json
  summary: IPR020266 is type family, named Mitochondrial import receptor subunit Tom6.
    Native member-signature identifiers and family boundary inspected.
  accessed_at: '2026-11-04T15:26:37.484237Z'
  support: supports
  snapshot_sha256: 1d842a377c7d730dbb2104c7284f2f4f11579968fc5122dbae8f807674d26775
- evidence_id: septin-ipr-IPR020951
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR020951/
  locator: Native metadata, type, family name, signatures and description flags; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR020951.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR020951.receipt.json
  summary: IPR020951 is type family, named Mitochondrial import receptor subunit Tom22,
    fungi. Native member-signature identifiers and family boundary inspected.
  accessed_at: '2026-11-04T15:26:36.741771Z'
  support: supports
  snapshot_sha256: c1867c085bab9a8bcb79c4ce73bfcc80f2fabdb6fa086566263dbcd386a627eb
- evidence_id: septin-ipr-IPR027503
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR027503/
  locator: Native metadata, type, family name, signatures and description flags; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR027503.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR027503.receipt.json
  summary: IPR027503 is type family, named Lon protease homologue, chloroplastic/mitochondrial.
    Native member-signature identifiers and family boundary inspected.
  accessed_at: '2026-11-04T15:25:47.453369Z'
  support: supports
  snapshot_sha256: d212f7f0d10e33b337c8c02f91635416689e6db65d6cee9e3e8b4863706dce9c
- evidence_id: septin-ipr-IPR033661
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR033661/
  locator: Native metadata, type, family name, signatures and description flags; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR033661.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR033661.receipt.json
  summary: IPR033661 is type family, named Phosphatidylserine decarboxylase, eukaryotic
    type 1. Native member-signature identifiers and family boundary inspected.
  accessed_at: '2026-11-04T15:26:16.755693Z'
  support: supports
  snapshot_sha256: 11064630897f3824ffeb8391b84c83a65033dcb84af56adb1e0baa0fcf04ec98
- evidence_id: septin-ipr-IPR037930
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR037930/
  locator: Native metadata, type, family name, signatures and description flags; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR037930.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR037930.receipt.json
  summary: IPR037930 is type family, named Tom40. Native member-signature identifiers
    and family boundary inspected.
  accessed_at: '2026-11-04T15:26:35.613605Z'
  support: supports
  snapshot_sha256: 11b39b372584392de606846964e5df0135105e26ea6d933f7d39bd03a1cbbd71
- evidence_id: septin-ipr-IPR045024
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR045024/
  locator: Native metadata, type, family name, signatures and description flags; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR045024.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR045024.receipt.json
  summary: IPR045024 is type family, named Alternative NADH dehydrogenase. Native
    member-signature identifiers and family boundary inspected. This broad alternative
    NADH-dehydrogenase family does not isolate the external Nde1 lineage from matrix-facing
    Ndi1 and bacterial members.
  accessed_at: '2026-11-04T15:26:18.739178Z'
  support: supports
  snapshot_sha256: 0a6429be44ce3977360a55f7194f7b9945b2bd9518b283a154ab1115768245bc
- evidence_id: septin-ipr-IPR050355
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050355/
  locator: Native metadata, type, family name, signatures and description flags; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR050355.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/ipr-IPR050355.receipt.json
  summary: IPR050355 is type family, named Mitochondrial Respiratory Supercomplex
    Factor 1. Native member-signature identifiers and family boundary inspected. The
    description is flagged llm=true, checked=false and is not used as independent
    primary mechanistic evidence.
  accessed_at: '2026-11-04T15:26:15.393012Z'
  support: supports
  snapshot_sha256: 3e8fd31eca4dbd4714b2a0672dbe618f9ecfb192beea2968524342cd081cc143
- evidence_id: septin-protein-P18239
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P18239.json
  locator: 'Complete native entry: identity, primary genes/aliases, taxon, family
    cross-references and source-qualified localization/subunit annotations; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/protein-P18239.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/protein-P18239.receipt.json'
  summary: 'P18239; UniProtKB reviewed (Swiss-Prot); taxon 559292; genes [{"geneName":
    {"value": "PET9"}, "synonyms": [{"value": "AAC2"}], "orderedLocusNames": [{"value":
    "YBL030C"}], "orfNames": [{"value": "YBL0421"}]}]. Localization annotation and
    primary-source membership are separately assessed; a family match does not establish
    formation necessity.'
  accessed_at: '2026-11-04T15:25:52.133165Z'
  support: supports
  snapshot_sha256: d31979160619df9d61b982b2bc8c437d68b232132d10d3cd00d71afdfc4c8901
- evidence_id: septin-protein-P36775
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P36775.json
  locator: 'Complete native entry: identity, primary genes/aliases, taxon, family
    cross-references and source-qualified localization/subunit annotations; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/protein-P36775.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/protein-P36775.receipt.json'
  summary: 'P36775; UniProtKB reviewed (Swiss-Prot); taxon 559292; genes [{"geneName":
    {"evidences": [{"evidenceCode": "ECO:0000255", "source": "HAMAP-Rule", "id": "MF_03120"}],
    "value": "PIM1"}, "synonyms": [{"value": "LON"}], "orderedLocusNames": [{"value":
    "YBL022C"}], "orfNames": [{"value": "YBL0440"}]}]. Localization annotation and
    primary-source membership are separately assessed; a family match does not establish
    formation necessity.'
  accessed_at: '2026-11-04T15:25:47.948230Z'
  support: supports
  snapshot_sha256: 936e7af53e01e476de369c3a9ead1b77b17d684a857a1dee37d563a94cb48705
- evidence_id: septin-protein-P39006
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P39006.json
  locator: 'Complete native entry: identity, primary genes/aliases, taxon, family
    cross-references and source-qualified localization/subunit annotations; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/protein-P39006.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/protein-P39006.receipt.json'
  summary: 'P39006; UniProtKB reviewed (Swiss-Prot); taxon 559292; genes [{"geneName":
    {"evidences": [{"evidenceCode": "ECO:0000255", "source": "HAMAP-Rule", "id": "MF_03208"},
    {"evidenceCode": "ECO:0000303", "source": "PubMed", "id": "8227017"}], "value":
    "PSD1"}, "orderedLocusNames": [{"evidences": [{"evidenceCode": "ECO:0000312",
    "source": "SGD", "id": "S000005113"}], "value": "YNL169C"}], "orfNames": [{"value":
    "N1692"}]}]. Localization annotation and primary-source membership are separately
    assessed; a family match does not establish formation necessity.'
  accessed_at: '2026-11-04T15:25:48.862638Z'
  support: supports
  snapshot_sha256: 22169918b8b47fe1c3c993651a19ec5811244035338788ec57873d3df9a1994d
- evidence_id: septin-protein-P40215
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P40215.json
  locator: 'Complete native entry: identity, primary genes/aliases, taxon, family
    cross-references and source-qualified localization/subunit annotations; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/protein-P40215.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/protein-P40215.receipt.json'
  summary: 'P40215; UniProtKB reviewed (Swiss-Prot); taxon 559292; genes [{"geneName":
    {"value": "NDE1"}, "synonyms": [{"value": "NDH1"}], "orderedLocusNames": [{"value":
    "YMR145C"}], "orfNames": [{"value": "YM9375.14C"}]}]. Localization annotation
    and primary-source membership are separately assessed; a family match does not
    establish formation necessity.'
  accessed_at: '2026-11-04T15:25:50.092228Z'
  support: supports
  snapshot_sha256: 38d45cc2c8481d4c32c0947c41bb551b1764d9b2f7b74af7d7fdc18f50d9821e
- evidence_id: septin-protein-Q03713
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q03713.json
  locator: 'Complete native entry: identity, primary genes/aliases, taxon, family
    cross-references and source-qualified localization/subunit annotations; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/protein-Q03713.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/protein-Q03713.receipt.json'
  summary: 'Q03713; UniProtKB reviewed (Swiss-Prot); taxon 559292; genes [{"geneName":
    {"value": "RCF1"}, "synonyms": [{"value": "AIM31"}], "orderedLocusNames": [{"value":
    "YML030W"}]}]. Localization annotation and primary-source membership are separately
    assessed; a family match does not establish formation necessity.'
  accessed_at: '2026-11-04T15:26:21.778731Z'
  support: supports
  snapshot_sha256: a219abed8e7fa74942b9697184429b6cb21377053a7c525fed73f88c4590d481
- evidence_id: septin-protein-Q06510
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q06510.json
  locator: 'Complete native entry: identity, primary genes/aliases, taxon, family
    cross-references and source-qualified localization/subunit annotations; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/protein-Q06510.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/protein-Q06510.receipt.json'
  summary: 'Q06510; UniProtKB reviewed (Swiss-Prot); taxon 559292; genes [{"geneName":
    {"value": "TAZ1"}, "orderedLocusNames": [{"evidences": [{"evidenceCode": "ECO:0000303",
    "source": "PubMed", "id": "15588229"}], "value": "YPR140W"}]}]. Localization annotation
    and primary-source membership are separately assessed; a family match does not
    establish formation necessity.'
  accessed_at: '2026-11-04T15:25:53.365828Z'
  support: supports
  snapshot_sha256: 3a4d7be707e529f46398317e269e0913a2b62d7c5038fb68e1bc02e1568a9925
- evidence_id: septin-gene-AAC2
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AAAC2+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=500
  locator: Complete returned reviewed S288C gene request; primary-name versus alias
    fields; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-AAC2.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-AAC2.receipt.json
  summary: Current returned identities [('P18239', 'PET9', 559292)]. Query scope is
    the explicit request, not a reconstruction of historical seeding. S288C is a reference
    context, not a substitute for source strain or an assembly assay.
  accessed_at: '2026-11-04T15:25:50.750844Z'
  support: context_only
  snapshot_sha256: 9d23c85c1003b5a1c82b3a43549d80a2cd0da97945fe6d1b1199f640e90b9aed
  search_scope: 'Actual current request https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AAAC2+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=500;
    request parameters {"format": ["json"], "query": ["gene_exact:AAC2 AND organism_id:559292
    AND reviewed:true"], "size": ["500"]}. Only the retained response was inspected;
    stated page bounds apply. No unrequested result pages or biological absence inferred.'
- evidence_id: septin-gene-NDE1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ANDE1+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=500
  locator: Complete returned reviewed S288C gene request; primary-name versus alias
    fields; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-NDE1.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-NDE1.receipt.json
  summary: Current returned identities [('P40215', 'NDE1', 559292)]. Query scope is
    the explicit request, not a reconstruction of historical seeding. S288C is a reference
    context, not a substitute for source strain or an assembly assay.
  accessed_at: '2026-11-04T15:26:27.848144Z'
  support: context_only
  snapshot_sha256: ec2e376b9a4fd680381511dae450476608447d60b4b7c2db8fb680bb69822534
  search_scope: 'Actual current request https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ANDE1+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=500;
    request parameters {"format": ["json"], "query": ["gene_exact:NDE1 AND organism_id:559292
    AND reviewed:true"], "size": ["500"]}. Only the retained response was inspected;
    stated page bounds apply. No unrequested result pages or biological absence inferred.'
- evidence_id: septin-gene-PET9
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3APET9+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=500
  locator: Complete returned reviewed S288C gene request; primary-name versus alias
    fields; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-PET9.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-PET9.receipt.json
  summary: Current returned identities [('P18239', 'PET9', 559292)]. Query scope is
    the explicit request, not a reconstruction of historical seeding. S288C is a reference
    context, not a substitute for source strain or an assembly assay.
  accessed_at: '2026-11-04T15:25:53.213320Z'
  support: context_only
  snapshot_sha256: 9d23c85c1003b5a1c82b3a43549d80a2cd0da97945fe6d1b1199f640e90b9aed
  search_scope: 'Actual current request https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3APET9+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=500;
    request parameters {"format": ["json"], "query": ["gene_exact:PET9 AND organism_id:559292
    AND reviewed:true"], "size": ["500"]}. Only the retained response was inspected;
    stated page bounds apply. No unrequested result pages or biological absence inferred.'
- evidence_id: septin-gene-PHB1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3APHB1+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=500
  locator: Complete returned reviewed S288C gene request; primary-name versus alias
    fields; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-PHB1.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-PHB1.receipt.json
  summary: Current returned identities [('P40961', 'PHB1', 559292)]. Query scope is
    the explicit request, not a reconstruction of historical seeding. S288C is a reference
    context, not a substitute for source strain or an assembly assay.
  accessed_at: '2026-11-04T15:26:38.855232Z'
  support: context_only
  snapshot_sha256: 87781e4605bbf3328e31d81867699f02dfaf672040af6b1bd5c0a8c3e3969e65
  search_scope: 'Actual current request https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3APHB1+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=500;
    request parameters {"format": ["json"], "query": ["gene_exact:PHB1 AND organism_id:559292
    AND reviewed:true"], "size": ["500"]}. Only the retained response was inspected;
    stated page bounds apply. No unrequested result pages or biological absence inferred.'
- evidence_id: septin-gene-PHB2
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3APHB2+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=500
  locator: Complete returned reviewed S288C gene request; primary-name versus alias
    fields; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-PHB2.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-PHB2.receipt.json
  summary: Current returned identities [('P50085', 'PHB2', 559292)]. Query scope is
    the explicit request, not a reconstruction of historical seeding. S288C is a reference
    context, not a substitute for source strain or an assembly assay.
  accessed_at: '2026-11-04T15:26:38.852434Z'
  support: context_only
  snapshot_sha256: 8f8b6ac7185ef6b337b783aeade0f6cb450fa7646986725d1dcfcc3bb064e31d
  search_scope: 'Actual current request https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3APHB2+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=500;
    request parameters {"format": ["json"], "query": ["gene_exact:PHB2 AND organism_id:559292
    AND reviewed:true"], "size": ["500"]}. Only the retained response was inspected;
    stated page bounds apply. No unrequested result pages or biological absence inferred.'
- evidence_id: septin-gene-TOM22
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ATOM22+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=500
  locator: Complete returned reviewed S288C gene request; primary-name versus alias
    fields; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-TOM22.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-TOM22.receipt.json
  summary: Current returned identities [('P49334', 'TOM22', 559292)]. Query scope
    is the explicit request, not a reconstruction of historical seeding. S288C is
    a reference context, not a substitute for source strain or an assembly assay.
  accessed_at: '2026-11-04T15:26:23.836974Z'
  support: context_only
  snapshot_sha256: e809521f339a53cfee751ef31bafabb642adc8412b169de84aa80edae54e8888
  search_scope: 'Actual current request https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ATOM22+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=500;
    request parameters {"format": ["json"], "query": ["gene_exact:TOM22 AND organism_id:559292
    AND reviewed:true"], "size": ["500"]}. Only the retained response was inspected;
    stated page bounds apply. No unrequested result pages or biological absence inferred.'
- evidence_id: septin-gene-TOM40
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ATOM40+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=500
  locator: Complete returned reviewed S288C gene request; primary-name versus alias
    fields; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-TOM40.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-TOM40.receipt.json
  summary: Current returned identities [('P23644', 'TOM40', 559292)]. Query scope
    is the explicit request, not a reconstruction of historical seeding. S288C is
    a reference context, not a substitute for source strain or an assembly assay.
  accessed_at: '2026-11-04T15:26:23.258890Z'
  support: context_only
  snapshot_sha256: 461981216e9d3a5c7d014de4bb3a6669200f3bfca24dcfdc4484442687562ac2
  search_scope: 'Actual current request https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ATOM40+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=500;
    request parameters {"format": ["json"], "query": ["gene_exact:TOM40 AND organism_id:559292
    AND reviewed:true"], "size": ["500"]}. Only the retained response was inspected;
    stated page bounds apply. No unrequested result pages or biological absence inferred.'
- evidence_id: septin-gene-TOM6
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ATOM6+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=500
  locator: Complete returned reviewed S288C gene request; primary-name versus alias
    fields; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-TOM6.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-TOM6.receipt.json
  summary: Current returned identities [('P33448', 'TOM6', 559292)]. Query scope is
    the explicit request, not a reconstruction of historical seeding. S288C is a reference
    context, not a substitute for source strain or an assembly assay.
  accessed_at: '2026-11-04T15:26:32.773354Z'
  support: context_only
  snapshot_sha256: ec2c73fe3e0d3ec96fb80c96ced0f5ba0457c029b28debba6eaa6ce650f5240f
  search_scope: 'Actual current request https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ATOM6+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=500;
    request parameters {"format": ["json"], "query": ["gene_exact:TOM6 AND organism_id:559292
    AND reviewed:true"], "size": ["500"]}. Only the retained response was inspected;
    stated page bounds apply. No unrequested result pages or biological absence inferred.'
- evidence_id: septin-gene-TOM7
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ATOM7+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=500
  locator: Complete returned reviewed S288C gene request; primary-name versus alias
    fields; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-TOM7.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-TOM7.receipt.json
  summary: Current returned identities [('P53507', 'TOM7', 559292)]. Query scope is
    the explicit request, not a reconstruction of historical seeding. S288C is a reference
    context, not a substitute for source strain or an assembly assay.
  accessed_at: '2026-11-04T15:27:07.127004Z'
  support: context_only
  snapshot_sha256: 8569dfbd68ab3e5dc3d37be3ac8c0024dcad356e3842b4abf8185d1c63f1b7be
  search_scope: 'Actual current request https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ATOM7+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=500;
    request parameters {"format": ["json"], "query": ["gene_exact:TOM7 AND organism_id:559292
    AND reviewed:true"], "size": ["500"]}. Only the retained response was inspected;
    stated page bounds apply. No unrequested result pages or biological absence inferred.'
- evidence_id: septin-gene-TOM70
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ATOM70+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=500
  locator: Complete returned reviewed S288C gene request; primary-name versus alias
    fields; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-TOM70.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-TOM70.receipt.json
  summary: Current returned identities [('P07213', 'TOM70', 559292)]. Query scope
    is the explicit request, not a reconstruction of historical seeding. S288C is
    a reference context, not a substitute for source strain or an assembly assay.
  accessed_at: '2026-11-04T15:26:40.822316Z'
  support: context_only
  snapshot_sha256: 5d90ba1d380950abba838fd40ae29139e5c657ab0db42a7ccb8756f6971a0b35
  search_scope: 'Actual current request https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ATOM70+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=500;
    request parameters {"format": ["json"], "query": ["gene_exact:TOM70 AND organism_id:559292
    AND reviewed:true"], "size": ["500"]}. Only the retained response was inspected;
    stated page bounds apply. No unrequested result pages or biological absence inferred.'
- evidence_id: septin-query-retry-LON
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ALON%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned reviewed S288C gene request; primary-name versus alias
    fields; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/query-retry-LON.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/query-retry-LON.receipt.json
  summary: Current returned identities [('P36775', 'PIM1', 559292)]. Query scope is
    the explicit request, not a reconstruction of historical seeding. S288C is a reference
    context, not a substitute for source strain or an assembly assay.
  accessed_at: '2026-11-04T15:38:11.453612Z'
  support: context_only
  snapshot_sha256: 9993742923d7f9199f3fc83d442a094eb95bb6777daa4c109a9316cde47150bc
  search_scope: 'Actual current request https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ALON%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100;
    request parameters {"format": ["json"], "query": ["(gene_exact:LON) AND (organism_id:559292)
    AND (reviewed:true)"], "size": ["100"]}. Only the retained response was inspected;
    stated page bounds apply. No unrequested result pages or biological absence inferred.'
- evidence_id: septin-query-retry-PIM1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3APIM1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned reviewed S288C gene request; primary-name versus alias
    fields; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/query-retry-PIM1.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/query-retry-PIM1.receipt.json
  summary: Current returned identities [('P36775', 'PIM1', 559292)]. Query scope is
    the explicit request, not a reconstruction of historical seeding. S288C is a reference
    context, not a substitute for source strain or an assembly assay.
  accessed_at: '2026-11-04T15:38:11.344831Z'
  support: context_only
  snapshot_sha256: 9993742923d7f9199f3fc83d442a094eb95bb6777daa4c109a9316cde47150bc
  search_scope: 'Actual current request https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3APIM1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100;
    request parameters {"format": ["json"], "query": ["(gene_exact:PIM1) AND (organism_id:559292)
    AND (reviewed:true)"], "size": ["100"]}. Only the retained response was inspected;
    stated page bounds apply. No unrequested result pages or biological absence inferred.'
- evidence_id: septin-query-retry-PSD1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3APSD1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned reviewed S288C gene request; primary-name versus alias
    fields; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/query-retry-PSD1.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/query-retry-PSD1.receipt.json
  summary: Current returned identities [('P39006', 'PSD1', 559292)]. Query scope is
    the explicit request, not a reconstruction of historical seeding. S288C is a reference
    context, not a substitute for source strain or an assembly assay.
  accessed_at: '2026-11-04T15:38:11.957274Z'
  support: context_only
  snapshot_sha256: 97975f899d8866f82491bd49d3f1746d07658257c21165f0efee65d7188c5399
  search_scope: 'Actual current request https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3APSD1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100;
    request parameters {"format": ["json"], "query": ["(gene_exact:PSD1) AND (organism_id:559292)
    AND (reviewed:true)"], "size": ["100"]}. Only the retained response was inspected;
    stated page bounds apply. No unrequested result pages or biological absence inferred.'
- evidence_id: septin-query-retry-RCF1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARCF1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned reviewed S288C gene request; primary-name versus alias
    fields; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/query-retry-RCF1.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/query-retry-RCF1.receipt.json
  summary: Current returned identities [('Q03713', 'RCF1', 559292)]. Query scope is
    the explicit request, not a reconstruction of historical seeding. S288C is a reference
    context, not a substitute for source strain or an assembly assay.
  accessed_at: '2026-11-04T15:38:11.991062Z'
  support: context_only
  snapshot_sha256: 29be1bb1cb74edee40cd1c2a53df7fea5e1b21c1b90b7394dcc2bbba440300e6
  search_scope: 'Actual current request https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARCF1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100;
    request parameters {"format": ["json"], "query": ["(gene_exact:RCF1) AND (organism_id:559292)
    AND (reviewed:true)"], "size": ["100"]}. Only the retained response was inspected;
    stated page bounds apply. No unrequested result pages or biological absence inferred.'
- evidence_id: septin-query-retry-TAZ1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ATAZ1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned reviewed S288C gene request; primary-name versus alias
    fields; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/query-retry-TAZ1.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/query-retry-TAZ1.receipt.json
  summary: Current returned identities [('Q06510', 'TAZ1', 559292)]. Query scope is
    the explicit request, not a reconstruction of historical seeding. S288C is a reference
    context, not a substitute for source strain or an assembly assay.
  accessed_at: '2026-11-04T15:38:12.977711Z'
  support: context_only
  snapshot_sha256: 56dc88be866d468d37774850ce4889d80471e330d8e86d2f7dacdbfab7f5d3ee
  search_scope: 'Actual current request https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ATAZ1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100;
    request parameters {"format": ["json"], "query": ["(gene_exact:TAZ1) AND (organism_id:559292)
    AND (reviewed:true)"], "size": ["100"]}. Only the retained response was inspected;
    stated page bounds apply. No unrequested result pages or biological absence inferred.'
- evidence_id: septin-query-retry-TOM20
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ATOM20%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned reviewed S288C gene request; primary-name versus alias
    fields; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/query-retry-TOM20.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/query-retry-TOM20.receipt.json
  summary: Current returned identities [('P35180', 'TOM20', 559292)]. Query scope
    is the explicit request, not a reconstruction of historical seeding. S288C is
    a reference context, not a substitute for source strain or an assembly assay.
  accessed_at: '2026-11-04T15:38:12.986608Z'
  support: context_only
  snapshot_sha256: 0a186aed4a361f60d248c5a4cb95b1971b2bbe35d59f3a6a8a42cbb863005e90
  search_scope: 'Actual current request https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ATOM20%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100;
    request parameters {"format": ["json"], "query": ["(gene_exact:TOM20) AND (organism_id:559292)
    AND (reviewed:true)"], "size": ["100"]}. Only the retained response was inspected;
    stated page bounds apply. No unrequested result pages or biological absence inferred.'
- evidence_id: septin-query-retry-TOM5
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ATOM5%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned reviewed S288C gene request; primary-name versus alias
    fields; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/query-retry-TOM5.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/query-retry-TOM5.receipt.json
  summary: Current returned identities [('P80967', 'TOM5', 559292)]. Query scope is
    the explicit request, not a reconstruction of historical seeding. S288C is a reference
    context, not a substitute for source strain or an assembly assay.
  accessed_at: '2026-11-04T15:38:13.943632Z'
  support: context_only
  snapshot_sha256: bb712a48d2dbc9ba523b214417f044c2a1dfc7e8c9cd6b0fb4e35f58ddea6e8d
  search_scope: 'Actual current request https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ATOM5%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100;
    request parameters {"format": ["json"], "query": ["(gene_exact:TOM5) AND (organism_id:559292)
    AND (reviewed:true)"], "size": ["100"]}. Only the retained response was inspected;
    stated page bounds apply. No unrequested result pages or biological absence inferred.'
- evidence_id: septin-doi-10.1016_j.cell.2009.08.005
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.cell.2009.08.005%22+AND+SRC%3AMED&format=json&resultType=core
  locator: Europe PMC native bibliographic record and complete available abstract;
    no paper body implied; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/doi-10.1016_j.cell.2009.08.005.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/doi-10.1016_j.cell.2009.08.005.receipt.json
  summary: 'Importing mitochondrial proteins: machineries and mechanisms. Authors:
    Chacinska A, Koehler CM, Milenkovic D, Lithgow T, Pfanner N.. DOI/PMID metadata
    reconciled. Metadata and abstract are not full-text methods or figure evidence.'
  accessed_at: '2026-11-04T15:26:33.412634Z'
  support: context_only
  snapshot_sha256: 55e631d907a0835ccf87e9f5420c44b216fe9cf6ab8e3e60a764de868f830075
- evidence_id: septin-doi-10.1016_j.jbc.2022.101694
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.jbc.2022.101694%22+AND+SRC%3AMED&format=json&resultType=core
  locator: Europe PMC native bibliographic record and complete available abstract;
    no paper body implied; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/doi-10.1016_j.jbc.2022.101694.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/doi-10.1016_j.jbc.2022.101694.receipt.json
  summary: 'Cryo-EM structure of hexameric yeast Lon protease (PIM1) highlights the
    importance of conserved structural elements. Authors: Yang J, Song AS, Wiseman
    RL, Lander GC.. DOI/PMID metadata reconciled. Metadata and abstract are not full-text
    methods or figure evidence.'
  accessed_at: '2026-11-04T15:25:46.835054Z'
  support: context_only
  snapshot_sha256: 7e246310e798877fc5a5bc159ca33c6aac31b1fa77277b8fcd5f4714ca12881a
- evidence_id: septin-doi-10.1073_pnas.96.12.6787
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1073%2Fpnas.96.12.6787%22+AND+SRC%3AMED&format=json&resultType=core
  locator: Europe PMC native bibliographic record and complete available abstract;
    no paper body implied; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/doi-10.1073_pnas.96.12.6787.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/doi-10.1073_pnas.96.12.6787.receipt.json
  summary: 'Mitochondrial Lon of Saccharomyces cerevisiae is a ring-shaped protease
    with seven flexible subunits. Authors: Stahlberg H, Kutejová E, Suda K, Wolpensinger
    B, Lustig A, Schatz G, Engel A, Suzuki CK.. DOI/PMID metadata reconciled. Metadata
    and abstract are not full-text methods or figure evidence.'
  accessed_at: '2026-11-04T15:25:47.008529Z'
  support: context_only
  snapshot_sha256: 5e424dea27489d742afa2608aa3b77246de61f45d551be8dd7c95bd878886ab7
- evidence_id: septin-doi-10.1110_ps.0212602
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1110%2Fps.0212602%22+AND+SRC%3AMED&format=json&resultType=core
  locator: Europe PMC native bibliographic record and complete available abstract;
    no paper body implied; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/doi-10.1110_ps.0212602.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/doi-10.1110_ps.0212602.receipt.json
  summary: 'A structure for the yeast prohibitin complex: Structure prediction and
    evidence from chemical crosslinking and mass spectrometry. Authors: Back JW, Sanz
    MA, De Jong L, De Koning LJ, Nijtmans LG, De Koster CG, Grivell LA, Van Der Spek
    H, Muijsers AO.. DOI/PMID metadata reconciled. Metadata and abstract are not full-text
    methods or figure evidence.'
  accessed_at: '2026-11-04T15:26:40.603464Z'
  support: context_only
  snapshot_sha256: 8a6abeaf5f26e23dbf1c21da419f0514c7e8828feea4fe64b660a9c2889f910c
- evidence_id: septin-doi-10.18632_aging.100246
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.18632%2Faging.100246%22+AND+SRC%3AMED&format=json&resultType=core
  locator: Europe PMC native bibliographic record and complete available abstract;
    no paper body implied; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/doi-10.18632_aging.100246.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/doi-10.18632_aging.100246.receipt.json
  summary: 'Opposing function of mitochondrial prohibitin in aging. Authors: Artal-Sanz
    M, Tavernarakis N.. DOI/PMID metadata reconciled. Metadata and abstract are not
    full-text methods or figure evidence.'
  accessed_at: '2026-11-04T15:26:42.003135Z'
  support: context_only
  snapshot_sha256: 23b5987f72cc43dd6ff2f5f341903d364d2a7594bc34ec42a5ba97b2ac13047f
- evidence_id: septin-pmid-14562095
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Europe PMC native bibliographic record and complete available abstract;
    no paper body implied; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pmid-14562095.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pmid-14562095.receipt.json
  summary: 'Global analysis of protein localization in budding yeast. Authors: Huh
    WK, Falvo JV, Gerke LC, Carroll AS, Howson RW, Weissman JS, O''Shea EK.. DOI/PMID
    metadata reconciled. Metadata and abstract are not full-text methods or figure
    evidence.'
  accessed_at: '2026-11-04T15:25:53.994959Z'
  support: context_only
  snapshot_sha256: 22cb10c77fae30f93c6690dedcb90031ab7d7b93d5fa08626a202a6ceb9d7ba1
- evidence_id: septin-pmid-14576278
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14576278+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Europe PMC native bibliographic record and complete available abstract;
    no paper body implied; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pmid-14576278.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pmid-14576278.receipt.json
  summary: 'The proteome of Saccharomyces cerevisiae mitochondria. Authors: Sickmann
    A, Reinders J, Wagner Y, Joppich C, Zahedi R, Meyer HE, Schönfisch B, Perschil
    I, Chacinska A, Guiard B, Rehling P, Pfanner N, Meisinger C.. DOI/PMID metadata
    reconciled. Metadata and abstract are not full-text methods or figure evidence.'
  accessed_at: '2026-11-04T15:25:54.707678Z'
  support: context_only
  snapshot_sha256: 5d9e1a6c3e634d955d714a847cd9c3bd27bc592e3c1c3130f57c1300dad1d6b6
- evidence_id: septin-pmid-15588229
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15588229+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Europe PMC native bibliographic record and complete available abstract;
    no paper body implied; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pmid-15588229.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pmid-15588229.receipt.json
  summary: 'Ypr140wp, ''the yeast tafazzin'', displays a mitochondrial lysophosphatidylcholine
    (lyso-PC) acyltransferase activity related to triacylglycerol and mitochondrial
    lipid synthesis. Authors: Testet E, Laroche-Traineau J, Noubhani A, Coulon D,
    Bunoust O, Camougrand N, Manon S, Lessire R, Bessoule JJ.. DOI/PMID metadata reconciled.
    Metadata and abstract are not full-text methods or figure evidence.'
  accessed_at: '2026-11-04T15:25:57.984075Z'
  support: context_only
  snapshot_sha256: dca3cbad3a97e2d0075633215eab74c14ddcb20cdaf1374760d72a51c4000a18
- evidence_id: septin-pmid-16135531
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A16135531+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Europe PMC native bibliographic record and complete available abstract;
    no paper body implied; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pmid-16135531.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pmid-16135531.receipt.json
  summary: 'Taz1, an outer mitochondrial membrane protein, affects stability and assembly
    of inner membrane protein complexes: implications for Barth Syndrome. Authors:
    Brandner K, Mick DU, Frazier AE, Taylor RD, Meisinger C, Rehling P.. DOI/PMID
    metadata reconciled. Metadata and abstract are not full-text methods or figure
    evidence.'
  accessed_at: '2026-11-04T15:26:02.195801Z'
  support: context_only
  snapshot_sha256: f64b87619e5e88e2a392dec1c32b73fb6145f3d853b62632bc341a358598c953
- evidence_id: septin-pmid-16880272
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A16880272+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Europe PMC native bibliographic record and complete available abstract;
    no paper body implied; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pmid-16880272.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pmid-16880272.receipt.json
  summary: 'Mitochondrial mislocalization and altered assembly of a cluster of Barth
    syndrome mutant tafazzins. Authors: Claypool SM, McCaffery JM, Koehler CM.. DOI/PMID
    metadata reconciled. Metadata and abstract are not full-text methods or figure
    evidence.'
  accessed_at: '2026-11-04T15:26:03.132007Z'
  support: context_only
  snapshot_sha256: 387012b4e5e982bfeed99c1bcd562e80ab65418f94b14fb614d7a808056a94d8
- evidence_id: septin-pmid-22984266
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A22984266+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Europe PMC native bibliographic record and complete available abstract;
    no paper body implied; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pmid-22984266.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pmid-22984266.receipt.json
  summary: 'Processing and topology of the yeast mitochondrial phosphatidylserine
    decarboxylase 1. Authors: Horvath SE, Böttinger L, Vögtle FN, Wiedemann N, Meisinger
    C, Becker T, Daum G.. DOI/PMID metadata reconciled. Metadata and abstract are
    not full-text methods or figure evidence.'
  accessed_at: '2026-11-04T15:26:04.230907Z'
  support: context_only
  snapshot_sha256: 9d7172ecba31607db49f7754a4dfc11946813157cdd78047d6491d09349a093a
- evidence_id: septin-pmid-23124206
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A23124206+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Europe PMC native bibliographic record and complete available abstract;
    no paper body implied; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pmid-23124206.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pmid-23124206.receipt.json
  summary: 'Phosphatidylethanolamine biosynthesis in mitochondria: phosphatidylserine
    (PS) trafficking is independent of a PS decarboxylase and intermembrane space
    proteins UPS1P and UPS2P. Authors: Tamura Y, Onguka O, Itoh K, Endo T, Iijima
    M, Claypool SM, Sesaki H.. DOI/PMID metadata reconciled. Metadata and abstract
    are not full-text methods or figure evidence.'
  accessed_at: '2026-11-04T15:26:06.484000Z'
  support: context_only
  snapshot_sha256: 098f08de38551faad58f7d5720dd544336c5d4a20570e55df208a4147d7185ae
- evidence_id: septin-pmid-35127709
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A35127709+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Europe PMC native bibliographic record and complete available abstract;
    no paper body implied; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pmid-35127709.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pmid-35127709.receipt.json
  summary: 'Peroxisomal ATP Uptake Is Provided by Two Adenine Nucleotide Transporters
    and the ABCD Transporters. Authors: van Roermund CWT, IJlst L, Linka N, Wanders
    RJA, Waterham HR.. DOI/PMID metadata reconciled. Metadata and abstract are not
    full-text methods or figure evidence.'
  accessed_at: '2026-11-04T15:26:08.428776Z'
  support: context_only
  snapshot_sha256: 4dc6f247d38a9464b136d67425929ace285d2e8c1eca20087962e55a1f9e1ca3
- evidence_id: septin-pmid-38393949
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A38393949+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Europe PMC native bibliographic record and complete available abstract;
    no paper body implied; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pmid-38393949.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pmid-38393949.receipt.json
  summary: 'Identification of MIMAS, a multifunctional mega-assembly integrating metabolic
    and respiratory biogenesis factors of mitochondria. Authors: Horten P, Song K,
    Garlich J, Hardt R, Colina-Tenorio L, Horvath SE, Schulte U, Fakler B, van der
    Laan M, Becker T, Stuart RA, Pfanner N, Rampelt H.. DOI/PMID metadata reconciled.
    Metadata and abstract are not full-text methods or figure evidence.'
  accessed_at: '2026-11-04T15:26:09.219719Z'
  support: context_only
  snapshot_sha256: 02f434fc31ce6ed50fd699372feb2f8c87ffcf04591f5e93688127530f9179d1
- evidence_id: septin-pmid-42178653
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A42178653+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Europe PMC native bibliographic record and complete available abstract;
    no paper body implied; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pmid-42178653.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pmid-42178653.receipt.json
  summary: 'MICOS and MIMAS, multifunctional assemblies linking mitochondrial biogenesis,
    architecture, and function. Authors: Horten P, Song K, Pfanner N, Rampelt H..
    DOI/PMID metadata reconciled. Metadata and abstract are not full-text methods
    or figure evidence.'
  accessed_at: '2026-11-04T15:26:10.417490Z'
  support: context_only
  snapshot_sha256: f385bab510a3252c717d942f501efb7e7cff4e8f1a6c6767fcb874ae41e3a0ae
- evidence_id: septin-pmid-795470
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A795470+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Europe PMC native bibliographic record and complete available abstract;
    no paper body implied; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pmid-795470.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pmid-795470.receipt.json
  summary: 'Effect of genetic and physiological manipulations onthe kinetic and binding
    parameters of the adenine nucleotide translocator in Saccharomyces cervisiae and
    Candida utilis. Authors: Lauquin G, Lunardi J, Vignais PV.. DOI/PMID metadata
    reconciled. Metadata and abstract are not full-text methods or figure evidence.'
  accessed_at: '2026-11-04T15:26:11.160846Z'
  support: context_only
  snapshot_sha256: 04f3c28bba9f34c375f1bdf41270df80c6cc119df070e6ec25691b638ca59506
- evidence_id: septin-back2002-abstract
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1110%2Fps.0212602%22+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete Back et al. 2002 abstract, PMID12237468; fresh full text unavailable;
    retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/doi-10.1110_ps.0212602.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/doi-10.1110_ps.0212602.receipt.json
  summary: Primary abstract reports lysine crosslinking, MS spatial restraints and
    predicted structures leading to a PHB1-PHB2 heterodimeric building block and a
    proposed repeated palisade arrangement. It does not report an atomic experimental
    structure or require the current record to adopt a fixed universal count. No current
    Methods/pixel verification is claimed.
  accessed_at: '2026-11-04T15:26:40.603464Z'
  support: partial
  snapshot_sha256: 8a6abeaf5f26e23dbf1c21da419f0514c7e8828feea4fe64b660a9c2889f910c
- evidence_id: septin-yang2022-xml
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8913295/fullTextXML
  locator: Complete main Results, Discussion, Experimental procedures and Figure1/2/3
    captions; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/yang2022-xml.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/yang2022-xml.receipt.json
  summary: Recombinant mature yeast Pim1 expressed in E. coli BL21(DE3) Codon Plus
    RIPL; ATPgammaS-prepared substrate-bound hexamer. Static structural translocation
    model distinguished from trajectory observation. S1015A and insertion mutants
    tested with beta-casein, 0.1 mg/ml protease, 0.08 mg/ml substrate, 5 mM ATP, 37
    C, one hour; activity is distinct from assembly formation or native viability.
    Data-availability accession errors are independently reconciled against archives.
  accessed_at: '2026-11-04T15:25:48.399308Z'
  support: supports
  snapshot_sha256: 1aef18ed6da1d5cb8ce4394fb400e4680d7145059f10f6db15960b0a2058273f
- evidence_id: septin-stahlberg1999-legacy
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC21993/
  locator: 'Genuine canonical PMC HTML: complete Methods, Results, Discussion and
    captions; no pixel reading; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/stahlberg1999-legacy.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/stahlberg1999-legacy.receipt.json'
  summary: Yeast-overexpressed C-terminally tagged Pim1 isolated from mitochondrial
    extracts; nucleotide stabilization, crosslinked STEM/cryonegative staining and
    ultracentrifugation support the reported heptamer under that preparation. Conflict
    with the later recombinant substrate-bound hexamer remains explicit; no universal
    native stoichiometry is inferred.
  accessed_at: '2026-11-04T15:25:47.323744Z'
  support: supports
  snapshot_sha256: 684e6a47439bd58fa5aeb1abb5fb75fd0e4f3417b4d0778e0a5b39a55f765076
- evidence_id: septin-horten2024-xml
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11010658/fullTextXML
  locator: Complete main Results/Discussion/Limitations and STAR Methods including
    source strains, crosslinking, rescue, import/chase and MS; figure captions, no
    pixels; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/horten2024-xml.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/horten2024-xml.receipt.json
  summary: YPH499/W303-derived yeast mitochondria. Co-migration, Psd1 affinity isolation
    and Nde1-AAC crosslinking support a selected MIMAS pool. Active Psd1, not S463A,
    rescues stability in psd1 deletion; inactive Psd1 can enter wild-type MIMAS. Rcf1
    mutations shift localization; transient Cox13 import does not make mature Cox13
    a stable constituent. PE dependence is not a directly resolved binding site or
    universal formation sequence; apparent 3.3/2.5 MDa peaks are not exact stoichiometry.
  accessed_at: '2026-11-04T15:26:20.887172Z'
  support: supports
  snapshot_sha256: 8c4123686a1bd54cc76a8c1f4312e2a744960a254b1ae30f39d565ee920b9587
- evidence_id: septin-review2026-xml
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13240547/fullTextXML
  locator: Secondary review body Section1.1 and Figure1 caption; no pixels; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/review2026-xml.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/review2026-xml.receipt.json
  summary: Horten et al. 2026 summarizes MIMAS inner-membrane organization and states
    that matrix/outer-membrane association remains unresolved. It is secondary support,
    not an independent new experiment.
  accessed_at: '2026-11-04T15:26:22.260010Z'
  support: partial
  snapshot_sha256: 44f9e0a72ce39ea66cdde0b34110d44032c0ec996dceab6569156b5c247d6d65
- evidence_id: septin-chacinska2009-jats
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4099469.1/PMC4099469.1.xml
  locator: Secondary review body TOM portal, targeting, TIM23/PAM coupling and outer
    membrane assembly sections; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/chacinska2009-jats.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/chacinska2009-jats.receipt.json
  summary: Chacinska et al. 2009 distinguishes Tom40 channel, Tom20/Tom70 recognition
    and Tom22 organization; downstream TIM23/PAM is separate. The record uses nonmechanistic
    topology/function edges. Cited perturbation work is described as reviewed literature,
    not freshly inspected primary experiments.
  accessed_at: '2026-11-04T15:26:34.976371Z'
  support: partial
  snapshot_sha256: 010e4b847c377e924ee1635a33ce3479a86b63183d5e5b4524a6904ff555ceba
- evidence_id: septin-artal2010-xml
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3034168/fullTextXML
  locator: Secondary review main Introduction and aging/metabolism/biogenesis discussion;
    retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/artal2010-xml.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/artal2010-xml.receipt.json
  summary: Artal-Sanz and Tavernarakis 2010 reviews repeating mitochondrial PHB complexes
    and condition-dependent functions. Yeast laboratory growth, animal development
    and aging effects are distinct; no universal loss-of-formation requirement is
    asserted.
  accessed_at: '2026-11-04T15:26:49.410146Z'
  support: partial
  snapshot_sha256: fe8827eb4bd34216ac5d4287299ca4551ce16330e201c170ef21a3ee9784a49e
- evidence_id: septin-pride-PXD047946
  kind: database
  reference: https://www.ebi.ac.uk/pride/ws/archive/v2/projects/PXD047946
  locator: Native project accession, title, species, submission type and publication
    link; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pride-PXD047946.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pride-PXD047946.receipt.json
  summary: PRIDE PXD047946 is a PARTIAL Saccharomyces MIMAS dataset with matching
    DOI; its pubmedID=0 field is a placeholder. Dataset metadata is provenance, not
    independent member quantification or reanalysis.
  accessed_at: '2026-11-04T15:26:22.605360Z'
  support: context_only
  snapshot_sha256: 29951a851353322943482f7e2b32b342e2ddafa02e4461f044bd00125eaae95e
- evidence_id: septin-pdb-7SXO
  kind: authority
  reference: https://data.rcsb.org/rest/v1/core/entry/7SXO
  locator: Native structural archive entity/assembly/ligand or EMDB metadata; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pdb-7SXO.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pdb-7SXO.receipt.json
  summary: '7SXO/EMD-25502 identify Yang 2022 yeast Pim1: six P36775-mapped protease
    chains plus one endogenous substrate entity, four ATP and two ADP, archive resolution3.3A.
    The A6B1 hetero-seven-chain aggregate is not seven Pim1 subunits. PDB7XSO and
    EMD-25505 name unrelated structures and corroborate the disclosed paper accession
    conflict. Archive source organism and bacterial expression/substrate context are
    not interchangeable.'
  accessed_at: '2026-11-04T15:25:47.401950Z'
  support: supports
  snapshot_sha256: 83762e0b93ac8e2566f07c8a35cd0fb134be029260c3f4a4db873cffe2e2888f
- evidence_id: septin-pdb-7SXO-assembly1
  kind: authority
  reference: https://data.rcsb.org/rest/v1/core/assembly/7SXO/1
  locator: Native structural archive entity/assembly/ligand or EMDB metadata; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pdb-7SXO-assembly1.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pdb-7SXO-assembly1.receipt.json
  summary: '7SXO/EMD-25502 identify Yang 2022 yeast Pim1: six P36775-mapped protease
    chains plus one endogenous substrate entity, four ATP and two ADP, archive resolution3.3A.
    The A6B1 hetero-seven-chain aggregate is not seven Pim1 subunits. PDB7XSO and
    EMD-25505 name unrelated structures and corroborate the disclosed paper accession
    conflict. Archive source organism and bacterial expression/substrate context are
    not interchangeable.'
  accessed_at: '2026-11-04T15:25:47.469592Z'
  support: supports
  snapshot_sha256: b5eca35aec2f9992847b670bd1a769e659292a30a79f442a9b94fb58148799dc
- evidence_id: septin-pdb-7SXO-entity1
  kind: authority
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/7SXO/1
  locator: Native structural archive entity/assembly/ligand or EMDB metadata; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pdb-7SXO-entity1.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pdb-7SXO-entity1.receipt.json
  summary: '7SXO/EMD-25502 identify Yang 2022 yeast Pim1: six P36775-mapped protease
    chains plus one endogenous substrate entity, four ATP and two ADP, archive resolution3.3A.
    The A6B1 hetero-seven-chain aggregate is not seven Pim1 subunits. PDB7XSO and
    EMD-25505 name unrelated structures and corroborate the disclosed paper accession
    conflict. Archive source organism and bacterial expression/substrate context are
    not interchangeable.'
  accessed_at: '2026-11-04T15:25:47.530021Z'
  support: supports
  snapshot_sha256: a4bc73e1115c2ae6c1fdd1d923f73b46f8fb74ea93d4008ab3a043abceab3ab5
- evidence_id: septin-pdb-7SXO-entity2
  kind: authority
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/7SXO/2
  locator: Native structural archive entity/assembly/ligand or EMDB metadata; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pdb-7SXO-entity2.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pdb-7SXO-entity2.receipt.json
  summary: '7SXO/EMD-25502 identify Yang 2022 yeast Pim1: six P36775-mapped protease
    chains plus one endogenous substrate entity, four ATP and two ADP, archive resolution3.3A.
    The A6B1 hetero-seven-chain aggregate is not seven Pim1 subunits. PDB7XSO and
    EMD-25505 name unrelated structures and corroborate the disclosed paper accession
    conflict. Archive source organism and bacterial expression/substrate context are
    not interchangeable.'
  accessed_at: '2026-11-04T15:25:47.541191Z'
  support: supports
  snapshot_sha256: 49d1c2f1cbedfee7aec84afe75af3619efd2377592ce5295f3f88807fd2393e2
- evidence_id: septin-pdb-7SXO-nonpolymer3
  kind: authority
  reference: https://data.rcsb.org/rest/v1/core/nonpolymer_entity/7SXO/3
  locator: Native structural archive entity/assembly/ligand or EMDB metadata; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pdb-7SXO-nonpolymer3.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pdb-7SXO-nonpolymer3.receipt.json
  summary: '7SXO/EMD-25502 identify Yang 2022 yeast Pim1: six P36775-mapped protease
    chains plus one endogenous substrate entity, four ATP and two ADP, archive resolution3.3A.
    The A6B1 hetero-seven-chain aggregate is not seven Pim1 subunits. PDB7XSO and
    EMD-25505 name unrelated structures and corroborate the disclosed paper accession
    conflict. Archive source organism and bacterial expression/substrate context are
    not interchangeable.'
  accessed_at: '2026-11-04T15:25:47.570760Z'
  support: supports
  snapshot_sha256: a17baa6e8b9a412b4f7f48e2a9b4212d0b835a465dd9cd15ab5ccaa0c721c02d
- evidence_id: septin-pdb-7SXO-nonpolymer4
  kind: authority
  reference: https://data.rcsb.org/rest/v1/core/nonpolymer_entity/7SXO/4
  locator: Native structural archive entity/assembly/ligand or EMDB metadata; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pdb-7SXO-nonpolymer4.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pdb-7SXO-nonpolymer4.receipt.json
  summary: '7SXO/EMD-25502 identify Yang 2022 yeast Pim1: six P36775-mapped protease
    chains plus one endogenous substrate entity, four ATP and two ADP, archive resolution3.3A.
    The A6B1 hetero-seven-chain aggregate is not seven Pim1 subunits. PDB7XSO and
    EMD-25505 name unrelated structures and corroborate the disclosed paper accession
    conflict. Archive source organism and bacterial expression/substrate context are
    not interchangeable.'
  accessed_at: '2026-11-04T15:25:47.597179Z'
  support: supports
  snapshot_sha256: 9ac8b1546a1d3fe5b0fba3dccd43eb70bf23fff0b37c434323c0255faa48cbab
- evidence_id: septin-pdb-7SXO-nonpolymer5
  kind: authority
  reference: https://data.rcsb.org/rest/v1/core/nonpolymer_entity/7SXO/5
  locator: Native structural archive entity/assembly/ligand or EMDB metadata; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pdb-7SXO-nonpolymer5.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pdb-7SXO-nonpolymer5.receipt.json
  summary: '7SXO/EMD-25502 identify Yang 2022 yeast Pim1: six P36775-mapped protease
    chains plus one endogenous substrate entity, four ATP and two ADP, archive resolution3.3A.
    The A6B1 hetero-seven-chain aggregate is not seven Pim1 subunits. PDB7XSO and
    EMD-25505 name unrelated structures and corroborate the disclosed paper accession
    conflict. Archive source organism and bacterial expression/substrate context are
    not interchangeable.'
  accessed_at: '2026-11-04T15:25:47.604684Z'
  support: supports
  snapshot_sha256: faf75e00866ea5de32fa4271fe89105aa861e33b77b56d3e213c9ffdb9fec6a3
- evidence_id: septin-emdb-25502
  kind: authority
  reference: https://files.wwpdb.org/pub/emdb/structures/EMD-25502/header/emd-25502.xml
  locator: Native structural archive entity/assembly/ligand or EMDB metadata; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/emdb-25502.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/emdb-25502.receipt.json
  summary: '7SXO/EMD-25502 identify Yang 2022 yeast Pim1: six P36775-mapped protease
    chains plus one endogenous substrate entity, four ATP and two ADP, archive resolution3.3A.
    The A6B1 hetero-seven-chain aggregate is not seven Pim1 subunits. PDB7XSO and
    EMD-25505 name unrelated structures and corroborate the disclosed paper accession
    conflict. Archive source organism and bacterial expression/substrate context are
    not interchangeable.'
  accessed_at: '2026-11-04T15:25:47.851672Z'
  support: supports
  snapshot_sha256: 621e50e914f5184d6f0d6cb5903e4e525221f3dfd703fccc9145befeb9270793
- evidence_id: septin-pdb-7XSO
  kind: authority
  reference: https://data.rcsb.org/rest/v1/core/entry/7XSO
  locator: Native structural archive entity/assembly/ligand or EMDB metadata; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pdb-7XSO.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/pdb-7XSO.receipt.json
  summary: '7SXO/EMD-25502 identify Yang 2022 yeast Pim1: six P36775-mapped protease
    chains plus one endogenous substrate entity, four ATP and two ADP, archive resolution3.3A.
    The A6B1 hetero-seven-chain aggregate is not seven Pim1 subunits. PDB7XSO and
    EMD-25505 name unrelated structures and corroborate the disclosed paper accession
    conflict. Archive source organism and bacterial expression/substrate context are
    not interchangeable.'
  accessed_at: '2026-11-04T15:25:47.669370Z'
  support: supports
  snapshot_sha256: bc204c4623e35a19e444ac205b8828c473eb4dafa0c8bc67d4ec1d09d57a486e
- evidence_id: septin-emdb-25505
  kind: authority
  reference: https://files.wwpdb.org/pub/emdb/structures/EMD-25505/header/emd-25505.xml
  locator: Native structural archive entity/assembly/ligand or EMDB metadata; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/emdb-25505.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/emdb-25505.receipt.json
  summary: '7SXO/EMD-25502 identify Yang 2022 yeast Pim1: six P36775-mapped protease
    chains plus one endogenous substrate entity, four ATP and two ADP, archive resolution3.3A.
    The A6B1 hetero-seven-chain aggregate is not seven Pim1 subunits. PDB7XSO and
    EMD-25505 name unrelated structures and corroborate the disclosed paper accession
    conflict. Archive source organism and bacterial expression/substrate context are
    not interchangeable.'
  accessed_at: '2026-11-04T15:25:47.788394Z'
  support: supports
  snapshot_sha256: 6de8750e12883cc9fd248c0994e9b7a16b1eefd85510db456c9a80efad76c192
- evidence_id: septin-back2002-legacy
  kind: validation
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2373692/
  locator: Actual failed or challenged current full-text route; retained snapshot
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/back2002-legacy.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/back2002-legacy.receipt.json
  summary: 'Access diagnostic only: HTTP 200. Canonical HTTP200 responses contain
    browser/challenge markup, not a genuine article body. EP XML500, publisher403
    and S3version1 absence do not refute the paper or its biology.'
  accessed_at: '2026-11-04T15:26:39.026957Z'
  support: context_only
  snapshot_sha256: 7b360d9fe792d7d1148f5cd9262094e1f444460573bfc6fc0c95406617042ee1
- evidence_id: septin-back2002-epmc-fresh
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2373692/fullTextXML
  locator: Actual failed or challenged current full-text route; retained snapshot
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/back2002-epmc-fresh.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/back2002-epmc-fresh.receipt.json
  summary: 'Access diagnostic only: HTTP 500. Canonical HTTP200 responses contain
    browser/challenge markup, not a genuine article body. EP XML500, publisher403
    and S3version1 absence do not refute the paper or its biology.'
  accessed_at: '2026-11-04T15:38:25.171860Z'
  support: context_only
  snapshot_sha256: cd2e24878da9532281f71f3f04938b31b013310f958096d7ec8ba28fc6419d66
- evidence_id: septin-back2002-canonical-fresh
  kind: validation
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2373692/?report=xml
  locator: Actual failed or challenged current full-text route; retained snapshot
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/back2002-canonical-fresh.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/back2002-canonical-fresh.receipt.json
  summary: 'Access diagnostic only: HTTP 200. Canonical HTTP200 responses contain
    browser/challenge markup, not a genuine article body. EP XML500, publisher403
    and S3version1 absence do not refute the paper or its biology.'
  accessed_at: '2026-11-04T15:38:10.739916Z'
  support: context_only
  snapshot_sha256: 3973c08f05ee6fb9b7745bd1ecab979f526eb60071a5b860f7a97ac042af02f5
- evidence_id: septin-back2002-publisher-fresh
  kind: validation
  reference: https://onlinelibrary.wiley.com/doi/full/10.1110/ps.0212602
  locator: Actual failed or challenged current full-text route; retained snapshot
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/back2002-publisher-fresh.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/back2002-publisher-fresh.receipt.json
  summary: 'Access diagnostic only: HTTP 403. Canonical HTTP200 responses contain
    browser/challenge markup, not a genuine article body. EP XML500, publisher403
    and S3version1 absence do not refute the paper or its biology.'
  accessed_at: '2026-11-04T15:38:10.609973Z'
  support: context_only
  snapshot_sha256: f9ca20feb66ffd54ceeb6c7886e98d40ceeb1e86a2692fabf67c90b243989189
- evidence_id: septin-PMC2373692-jats
  kind: validation
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2373692.1/PMC2373692.1.xml
  locator: Actual failed or challenged current full-text route; retained snapshot
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/PMC2373692-jats.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/PMC2373692-jats.receipt.json
  summary: 'Access diagnostic only: HTTP 404. Canonical HTTP200 responses contain
    browser/challenge markup, not a genuine article body. EP XML500, publisher403
    and S3version1 absence do not refute the paper or its biology.'
  accessed_at: '2026-11-04T15:26:41.381240Z'
  support: context_only
  snapshot_sha256: 27f6c3011a6dc4b438564f2c694d31c14c3a634d76d9b48059928594ec376f83
- evidence_id: septin-gene-PIM1
  kind: validation
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3APIM1+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=500
  locator: Initial timed-out native query, later distinct retry retained; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-PIM1.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-PIM1.receipt.json
  summary: The initial request timed out; genuine later retry results are separate
    evidence. Failure is not zero hits or biological absence.
  accessed_at: '2026-11-04T15:26:31.651425Z'
  support: context_only
  snapshot_sha256: e49e97802681e55590403e688172b0f7d73c96e92560dbf2e47d25f177016ca2
- evidence_id: septin-gene-LON
  kind: validation
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ALON+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=500
  locator: Initial timed-out native query, later distinct retry retained; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-LON.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-LON.receipt.json
  summary: The initial request timed out; genuine later retry results are separate
    evidence. Failure is not zero hits or biological absence.
  accessed_at: '2026-11-04T15:26:31.659308Z'
  support: context_only
  snapshot_sha256: e49e97802681e55590403e688172b0f7d73c96e92560dbf2e47d25f177016ca2
- evidence_id: septin-gene-RCF1
  kind: validation
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ARCF1+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=500
  locator: Initial timed-out native query, later distinct retry retained; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-RCF1.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-RCF1.receipt.json
  summary: The initial request timed out; genuine later retry results are separate
    evidence. Failure is not zero hits or biological absence.
  accessed_at: '2026-11-04T15:26:35.540322Z'
  support: context_only
  snapshot_sha256: e49e97802681e55590403e688172b0f7d73c96e92560dbf2e47d25f177016ca2
- evidence_id: septin-gene-PSD1
  kind: validation
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3APSD1+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=500
  locator: Initial timed-out native query, later distinct retry retained; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-PSD1.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-PSD1.receipt.json
  summary: The initial request timed out; genuine later retry results are separate
    evidence. Failure is not zero hits or biological absence.
  accessed_at: '2026-11-04T15:26:36.193250Z'
  support: context_only
  snapshot_sha256: e49e97802681e55590403e688172b0f7d73c96e92560dbf2e47d25f177016ca2
- evidence_id: septin-gene-TAZ1
  kind: validation
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ATAZ1+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=500
  locator: Initial timed-out native query, later distinct retry retained; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-TAZ1.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-TAZ1.receipt.json
  summary: The initial request timed out; genuine later retry results are separate
    evidence. Failure is not zero hits or biological absence.
  accessed_at: '2026-11-04T15:26:38.662401Z'
  support: context_only
  snapshot_sha256: e49e97802681e55590403e688172b0f7d73c96e92560dbf2e47d25f177016ca2
- evidence_id: septin-gene-TOM20
  kind: validation
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ATOM20+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=500
  locator: Initial timed-out native query, later distinct retry retained; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-TOM20.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-TOM20.receipt.json
  summary: The initial request timed out; genuine later retry results are separate
    evidence. Failure is not zero hits or biological absence.
  accessed_at: '2026-11-04T15:27:08.713249Z'
  support: context_only
  snapshot_sha256: e49e97802681e55590403e688172b0f7d73c96e92560dbf2e47d25f177016ca2
- evidence_id: septin-gene-TOM5
  kind: validation
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ATOM5+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=500
  locator: Initial timed-out native query, later distinct retry retained; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-TOM5.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/gene-TOM5.receipt.json
  summary: The initial request timed out; genuine later retry results are separate
    evidence. Failure is not zero hits or biological absence.
  accessed_at: '2026-11-04T15:27:13.317506Z'
  support: context_only
  snapshot_sha256: e49e97802681e55590403e688172b0f7d73c96e92560dbf2e47d25f177016ca2
- evidence_id: septin-lon-image-pixels
  kind: record_content
  reference: data/images/other/mitochondrial_lon_protease_complex/pmc8913295_fig1.jpg
  locator: Actual view_image inspection of complete Figure1 A/B pixels
  summary: Observed model panels show colored substrate-bound Pim1 assembly, ATPase/protease
    orthogonal views and pore-loop/substrate close-up. This is a structural model
    illustration, not a raw micrograph or direct native-cell image. Six enzyme chains
    are distinct from substrate.
  accessed_at: '2026-11-04T15:44:30.976471Z'
  support: supports
  snapshot_sha256: a5c78bd75286956f9389092a1f0070b7df894266773b793201748c6a24b3ba6b
- evidence_id: septin-yang2022-fig1
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC8913295.1/gr1.jpg
  locator: Fresh public gr1 media compared bytewise with the maintained image; Figure1
    caption read; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/yang2022-fig1.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/yang2022-fig1.receipt.json
  summary: Fresh gr1 and the maintained image are byte-identical, SHA256 a5c78bd75286956f9389092a1f0070b7df894266773b793201748c6a24b3ba6b.
    Image appearance agrees with the structural-model caption.
  accessed_at: '2026-11-04T15:25:48.207417Z'
  support: supports
  snapshot_sha256: a5c78bd75286956f9389092a1f0070b7df894266773b793201748c6a24b3ba6b
- evidence_id: septin-yang2022-s3-gr3-jpg
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC8913295.1/gr3.jpg
  locator: Actual view_image inspection of complete Figure3 A/B/C pixels and matching
    caption; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/yang2022-s3-gr3-jpg.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/yang2022-s3-gr3-jpg.receipt.json
  summary: Construct diagrams and beta-casein gel time courses were visually inspected.
    Protease-inactive control retains casein; insertion deletion and G/S linker retain
    substantial degradation over the depicted hour. No numerical kinetic fit, assembly-loss
    test, native viability or all-substrate conclusion is inferred.
  accessed_at: '2026-11-04T15:25:48.377123Z'
  support: supports
  snapshot_sha256: 275d2a8c67beeada7c8dff4b806aaf8accb645a5de4b3d5716bb9cd80c574db5
- evidence_id: septin-yang2022-s3-PMC8913295-1-json
  kind: database
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC8913295.1/PMC8913295.1.json
  locator: PMC package article/media metadata and gr1 MD5; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/yang2022-s3-PMC8913295-1-json.raw;
    retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-septin/yang2022-s3-PMC8913295-1-json.receipt.json
  summary: Package identifies Yang, Song, Wiseman and Lander 2022, PMID35143841, DOI10.1016/j.jbc.2022.101694;
    CC BY metadata and matching gr1 MD5 fd98aa3d48b65d293f30c18c33dc815a. JATS permissions
    explicitly give CC BY4.0; maintained attribution is supported.
  accessed_at: '2026-11-04T15:25:48.175983Z'
  support: context_only
  snapshot_sha256: a4c5295badb28f331cf70072fba39f01c0bebdd3f60cfba8d3a0dfabf113df0e
- evidence_id: septin-adapter-catalogue
  kind: search
  reference: https://imodulondb.org/api/organisms
  locator: Complete current catalogue /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/adapter-catalogue.raw;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/adversary-microtubule/adapter-catalogue.receipt.json
  accessed_at: '2026-11-04T15:24:16.251933Z'
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  support: context_only
  summary: All 20 returned organism rows and 28 organism-dataset entries inspected.
    None covers Saccharomyces or another named fungal/mammalian biological host in
    this slice. E. coli recombinant expression or substrate annotation is not a matched
    mitochondrial host. No mismatched gene/module proxy query was used.
  search_scope: One complete official /api/organisms response, all rows and dataset
    keys, matched against actual yeast/eukaryotic target and source hosts; bounded
    current coverage only, not biological absence or a global survey of every expression
    resource.
- evidence_id: septin-historical-adapter-runner
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical 2026-11-03 00:49Z runner-canary receipt; no fresh invocation
  summary: The actual prior runner event was unavailable with PermissionError on pyvenv.cfg.
    It is reused only as historical tooling provenance; fresh official-source catalogue/authority
    checks provide the current fallback.
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: check-qc
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/qc.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T15:28:10.685467Z'
  support: supports
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  snapshot_sha256: f51d1113e987ba394c76c5d83cb11d78837b83b56d7e8031507fe9c3fcb4ad72
- evidence_id: check-labels
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/labels.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T15:22:48.041062Z'
  support: supports
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  snapshot_sha256: 6cdfb05df9a27194f05a5fd7f851783f817ac1523ca0bbfa54fe0e0d18775905
- evidence_id: check-trait-links
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/trait-links.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T15:22:27.588153Z'
  support: supports
  summary: 'Native TraitMech check passed: all 10 links resolve with matching labels
    against the 1130-trait source index.'
  snapshot_sha256: 8b336cdefbbd3daf6da8787990efdbe346c95e2c8361d50b7eb68a18f2d5a44a
- evidence_id: check-vendored
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/vendored.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T15:22:25.873654Z'
  support: supports
  summary: All 22 governed artifacts match the pinned CLAW revision.
  snapshot_sha256: b1f169d103aaefa930745468bcca171e5867b9cc49e4e74311e458097e3252a6
- evidence_id: check-curies
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/curies.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T15:22:50.988425Z'
  support: supports
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    all 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  snapshot_sha256: fb3be251020aac118f6df680372ae7aaa32c2a1dd3366648cde95494f19d9dd2
- evidence_id: focused
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/focused-results.json
  locator: All twenty actual target schema/strict command outputs
  accessed_at: '2026-11-04T15:49:50Z'
  support: supports
  summary: Ten schema and ten strict commands returned exit zero.
  snapshot_sha256: 46f9d7b829a91e21c768e70d7d5d7d80fbad26b8c9ade271410c6435e0d8b415
- evidence_id: supplemental-pmid
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/pmid-chunks-receipt.json
  locator: Complete native-report PMID set checked with unchanged resolver in batches
    of at most fifty
  accessed_at: '2026-11-04T15:24:25.393770Z'
  support: supports
  summary: 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers
    remain unverified.
  snapshot_sha256: f72dce9caac5e8ac3bc1c9b415ab3646a2bc1b165be1b5909f9cdd2448b83633
- evidence_id: historical-adapter-runner-availability
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical runner invocation receipt; exact retained SHA256 reverified
    during PR2396 synthesis
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  summary: Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS
    PermissionError reading the configured runner pyvenv.cfg. This is retained historical
    availability evidence, not a fresh attempt or a scientific validation failure.
    Native policy permits inspected source-catalogue fallback.
- evidence_id: root-native-mic10_subcomplex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mic10_subcomplex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T15:22:24.272266Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-mic10_subcomplex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mic10_subcomplex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T15:22:24.723493Z'
  support: context_only
  snapshot_sha256: 6c1d97f2cb25045ddae5e20a9aa6562b9fa6be6961f961243b68c041557dc83c
  summary: 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-mic60_mic19_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mic60_mic19_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T15:22:25.970378Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-mic60_mic19_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mic60_mic19_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T15:22:26.389998Z'
  support: context_only
  snapshot_sha256: 22d7a0d901ab4f94314139e8db344060d6646aebc95400a3456ce381afa664b4
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-micos_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/micos_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T15:22:26.805708Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-micos_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/micos_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T15:22:27.216934Z'
  support: context_only
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-mim_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mim_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T15:22:28.355218Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-mim_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mim_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T15:22:28.763785Z'
  support: context_only
  snapshot_sha256: 4d2fc324bc37f34d33055b3b2a52a9e6d8020dd8c109abbf7d0cf67d8ff88743
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-mis12_mind_type_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mis12_mind_type_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T15:22:29.944370Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 4 represented protein examples; 5 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-mis12_mind_type_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mis12_mind_type_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T15:22:30.362007Z'
  support: context_only
  snapshot_sha256: fad6678665a9bc3509cf409f377cc2e2229d22e04659cf35e9025cb818052429
  summary: 4 represented protein examples; 5 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-mitochondrial_inner_membrane_peptidase_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_inner_membrane_peptidase_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T15:22:30.760888Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-mitochondrial_inner_membrane_peptidase_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_inner_membrane_peptidase_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T15:22:31.162273Z'
  support: context_only
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-mitochondrial_lon_protease_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_lon_protease_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T15:22:32.285898Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-mitochondrial_lon_protease_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_lon_protease_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T15:22:32.700334Z'
  support: context_only
  snapshot_sha256: 593a4556e111d3a1cfcf401fad0bc11ad1edf7df8b98ea85523db231d52f846b
  summary: 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-mitochondrial_multifunctional_assembly-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_multifunctional_assembly-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T15:22:33.893561Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 5 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-mitochondrial_multifunctional_assembly-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_multifunctional_assembly-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T15:22:34.298796Z'
  support: context_only
  snapshot_sha256: 2b1888389fba30f8794923be1fc9b5ba2c9bcaf92ef659ae0378f0c848a48d47
  summary: 5 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-mitochondrial_outer_membrane_translocase_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_outer_membrane_translocase_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T15:22:34.698937Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-mitochondrial_outer_membrane_translocase_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_outer_membrane_translocase_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T15:22:35.085772Z'
  support: context_only
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-mitochondrial_prohibitin_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_prohibitin_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T15:22:35.476023Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-mitochondrial_prohibitin_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2397/mitochondrial_prohibitin_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T15:22:35.866672Z'
  support: context_only
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
assessments:
- assessment_id: micro-bytes-0
  area: provenance
  topic: Current and historical artifact verification
  outcome: supported
  summary: Complete current record and original native pair read; all 44 declared
    historical input occurrences and six deterministic original commands passed. Current
    target equals original target and reviewed main.
  target_ids:
  - cellstructuremech:mic10_subcomplex
  evidence_ids:
  - micro-record-0
  - micro-prior-0
  - micro-original-audit
- assessment_id: micro-applicability-0
  area: scope
  topic: Whole-record structured-source applicability
  outcome: concern
  summary: Positive Mic10/Mic12/Mic26/Mic27 assembly, lipid regulation and contact-site
    pathways makes the original formal expression-only exemption unsupported. Fresh
    full catalogue has no matched biological host; no downstream proxy is substituted.
    Historical unavailable runner receipt remains old, not a new invocation.
  target_ids:
  - cellstructuremech:mic10_subcomplex
  evidence_ids:
  - micro-record-0
  - micro-prior-0
  - micro-native-policy
  - micro-adapter-catalogue
- assessment_id: micro-native-0
  area: schema
  topic: Actual native protein inventory and coverage
  outcome: supported
  summary: 4 reviewed S288C protein examples and4 COVERED typed nodes. Generic verify
    success is not an assertion that an empty inventory was populated. Root current
    commands and logs are independently hash-bound.
  target_ids:
  - cellstructuremech:mic10_subcomplex
  evidence_ids:
  - micro-record-0
  - micro-native-mic10_subcomplex-verify
  - micro-native-mic10_subcomplex-causal
- assessment_id: micro-verdict-0
  area: scope
  topic: Current scientific disposition and original finding lineage
  outcome: supported
  summary: No original scientific finding/action exists to carry, close or reject.
    Current full-record reassessment supports a qualified pass with stated access,
    assay, taxon and architecture limits. Review-bundle corrections are separate from
    record curation.
  target_ids:
  - cellstructuremech:mic10_subcomplex
  evidence_ids:
  - micro-record-0
  - micro-prior-0
  - micro-original-audit
- assessment_id: micro-bytes-1
  area: provenance
  topic: Current and historical artifact verification
  outcome: supported
  summary: Complete current record and original native pair read; all 44 declared
    historical input occurrences and six deterministic original commands passed. Current
    target equals original target and reviewed main.
  target_ids:
  - cellstructuremech:mic60_mic19_complex
  evidence_ids:
  - micro-record-1
  - micro-prior-1
  - micro-original-audit
- assessment_id: micro-applicability-1
  area: scope
  topic: Whole-record structured-source applicability
  outcome: concern
  summary: Positive Mic60/Mic19 binding, remodeling and junction-formation functions
    makes the original formal expression-only exemption unsupported. Fresh full catalogue
    has no matched biological host; no downstream proxy is substituted. Historical
    unavailable runner receipt remains old, not a new invocation.
  target_ids:
  - cellstructuremech:mic60_mic19_complex
  evidence_ids:
  - micro-record-1
  - micro-prior-1
  - micro-native-policy
  - micro-adapter-catalogue
- assessment_id: micro-native-1
  area: schema
  topic: Actual native protein inventory and coverage
  outcome: supported
  summary: 2 reviewed S288C protein examples and2 COVERED typed nodes. Generic verify
    success is not an assertion that an empty inventory was populated. Root current
    commands and logs are independently hash-bound.
  target_ids:
  - cellstructuremech:mic60_mic19_complex
  evidence_ids:
  - micro-record-1
  - micro-native-mic60_mic19_complex-verify
  - micro-native-mic60_mic19_complex-causal
- assessment_id: micro-verdict-1
  area: scope
  topic: Current scientific disposition and original finding lineage
  outcome: supported
  summary: No original scientific finding/action exists to carry, close or reject.
    Current full-record reassessment supports a qualified pass with stated access,
    assay, taxon and architecture limits. Review-bundle corrections are separate from
    record curation.
  target_ids:
  - cellstructuremech:mic60_mic19_complex
  evidence_ids:
  - micro-record-1
  - micro-prior-1
  - micro-original-audit
- assessment_id: micro-bytes-2
  area: provenance
  topic: Current and historical artifact verification
  outcome: supported
  summary: Complete current record and original native pair read; all 44 declared
    historical input occurrences and six deterministic original commands passed. Original
    target differs only by reciprocal has_part/history; substantive source assessment
    below.
  target_ids:
  - GO:0061617
  evidence_ids:
  - micro-record-2
  - micro-prior-2
  - micro-original-audit
  - micro-micos-stale-delta
- assessment_id: micro-applicability-2
  area: scope
  topic: Whole-record structured-source applicability
  outcome: concern
  summary: Positive six-subunit MICOS and membrane organization/contact-site functions
    makes the original formal expression-only exemption unsupported. Fresh full catalogue
    has no matched biological host; no downstream proxy is substituted. Historical
    unavailable runner receipt remains old, not a new invocation.
  target_ids:
  - GO:0061617
  evidence_ids:
  - micro-record-2
  - micro-prior-2
  - micro-native-policy
  - micro-adapter-catalogue
- assessment_id: micro-native-2
  area: schema
  topic: Actual native protein inventory and coverage
  outcome: supported
  summary: 0 protein examples and0 typed GENE_OR_PROTEIN nodes; empty check is not
    molecular validation. Generic verify success is not an assertion that an empty
    inventory was populated. Root current commands and logs are independently hash-bound.
  target_ids:
  - GO:0061617
  evidence_ids:
  - micro-record-2
  - micro-native-micos_complex-verify
  - micro-native-micos_complex-causal
- assessment_id: micro-verdict-2
  area: scope
  topic: Current scientific disposition and original finding lineage
  outcome: supported
  summary: No original scientific finding/action exists to carry, close or reject.
    Current full-record reassessment supports a qualified pass with stated access,
    assay, taxon and architecture limits. Review-bundle corrections are separate from
    record curation.
  target_ids:
  - GO:0061617
  evidence_ids:
  - micro-record-2
  - micro-prior-2
  - micro-original-audit
- assessment_id: micro-ontology
  area: identity
  topic: Exact structure identities and typed hierarchy
  outcome: supported
  summary: MICOS remains active exact GO0061617; the two minted subcomplexes are narrower
    source-defined structures with reciprocal parthood. Current bounded text searches
    returned no exact-named hits; this is not exhaustive ontology absence. GO0098800
    is is_a parent and GO0005743 containing membrane, not alternate identities.
  target_ids:
  - cellstructuremech:mic10_subcomplex
  - cellstructuremech:mic60_mic19_complex
  - GO:0061617
  evidence_ids:
  - micro-go
  - micro-GO0061617-ancestors
  - micro-GO0098800-ancestors
  - micro-go-search-Mic10
  - micro-go-search-Mic60-Mic19
  - micro-record-0
  - micro-record-1
  - micro-record-2
- assessment_id: micro-mic10-families
  area: grounding
  topic: Four subunit families and lineage boundaries
  outcome: supported
  summary: IPR007512 Mic10 and IPR031463 Mic12 are exact families; IPR033181 is fungal
    Mic26 and IPR061953 Saccharomycetaceae Mic27. Both lineage labels are retained.
    Normal four-protein module is compatible with conditional Mic10/Mic12/Mic27 assembly;
    no forced broad family or missing optional row.
  target_ids:
  - cellstructuremech:mic10_subcomplex
  evidence_ids:
  - micro-record-0
  - micro-ipr-IPR007512
  - micro-ipr-IPR031463
  - micro-ipr-IPR033181
  - micro-ipr-IPR061953
  - micro-rampelt2018-pdf
  - micro-friedman2015-s3
- assessment_id: micro-mic10-identities
  area: identity
  topic: Four current reviewed yeast references
  outcome: supported
  summary: MIC10/Q96VH5, MIC12/P38341, MIC26/P50087 and MIC27/P50945 each match reviewed
    S288C 559292 with correct primary symbols, loci and aliases; each exact current
    query has one result. Identity-only examples do not retrofit S288C onto W303 or
    YPH499 experiments.
  target_ids:
  - cellstructuremech:mic10_subcomplex
  evidence_ids:
  - micro-record-0
  - micro-protein-Q96VH5-final
  - micro-protein-P38341-retry
  - micro-protein-P50087-retry
  - micro-protein-P50945-retry
  - micro-query-MIC10-retry
  - micro-query-MIC12-retry
  - micro-query-MIC26-final
  - micro-query-MIC27-retry
  - micro-tax-559292
- assessment_id: micro-mic10-oligomers
  area: evidence
  topic: Mic26/Mic27 antagonism and cardiolipin
  outcome: supported
  summary: Rampelt native gels/crosslinking in YPH499 support larger Mic10 assemblies
    after mic26 deletion and opposite effects after mic27 deletion, with cardiolipin
    stabilization. These do not give universal native copy counts or a directly mapped
    cardiolipin-binding site. Record preserves the four-subunit scope.
  target_ids:
  - cellstructuremech:mic10_subcomplex
  evidence_ids:
  - micro-record-0
  - micro-rampelt2018-pdf
- assessment_id: micro-mic10-conditional-core
  area: evidence
  topic: Conditional subcomplex assembly and junction proximity
  outcome: supported
  summary: Friedman W303 reconstitution supports Mic10 dependence of Mic27 foci and
    reduced rather than abolished foci without Mic12 in the tested context. Crosslinked
    conditional core and normal four-member module differ. Crista-junction placement
    relies on fluorescent-marker proximity after unsuccessful immuno-EM, which the
    record explicitly qualifies.
  target_ids:
  - cellstructuremech:mic10_subcomplex
  evidence_ids:
  - micro-record-0
  - micro-friedman2015-s3
- assessment_id: micro-mic10-contact-boundary
  area: scope
  topic: ERMES, Vps13 and lipids
  outcome: supported
  summary: Tirrell independently separates contact proximity and ERMES functional
    dependence from direct obligatory template binding; Vps13 bypass is compatible.
    Cardiolipin, ERMES andVps13 remain context/regulators rather than constituent
    subunits. Native architecture remains unresolved.
  target_ids:
  - cellstructuremech:mic10_subcomplex
  evidence_ids:
  - micro-record-0
  - micro-tirrell2020-s3
  - micro-rampelt2018-pdf
  - micro-policy
- assessment_id: micro-mic10-graph
  area: graph
  topic: All five current assembly edges
  outcome: supported
  summary: Mic10 oligomerization, Mic26 destabilization, Mic27 stabilization and the
    Mic10/Mic12 effects on Mic27 foci match the precise assays. Types/component_refs
    and native grounding agree; no universal formation necessity is silently added.
  target_ids:
  - cellstructuremech:mic10_subcomplex
  evidence_ids:
  - micro-record-0
  - micro-graph-policy
  - micro-friedman2015-s3
  - micro-rampelt2018-pdf
  - micro-native-mic10_subcomplex-causal
- assessment_id: micro-mic10-image
  area: evidence
  topic: Complete Figure3 pixels, caption and licence
  outcome: supported
  summary: Maintained image is byte-identical to fresh source; full A–G panels were
    visually inspected. W303 confocal/co-IP/counting context, OTHER modality and explicit
    nonmolecular-image caption match; CC BY 4.0 article permissions and attribution
    support reuse. No raw imaging reanalysis or new package MD5 verification claimed.
  target_ids:
  - cellstructuremech:mic10_subcomplex
  evidence_ids:
  - micro-record-0
  - micro-image-0
  - micro-friedman2015-fig3
  - micro-friedman2015-s3
- assessment_id: micro-mic60-grounding
  area: grounding
  topic: Mic60 family and unresolved Mic19 candidate
  outcome: supported
  summary: IPR019133 supports exact Mic60. NativeP43594 carries IPR012471/PF07956,
    but the authority calls it uncharacterised fungal DUF1690, not exact universal
    Mic19. REVIEWED_LABEL_ONLY with open source-neutral question is valid; no optional
    grounding mandate or invented absence claim.
  target_ids:
  - cellstructuremech:mic60_mic19_complex
  evidence_ids:
  - micro-record-1
  - micro-ipr-IPR019133-retry
  - micro-ipr-IPR012471-retry
  - micro-protein-P43594-retry
  - micro-policy
- assessment_id: micro-mic60-identities
  area: identity
  topic: Current Mic60/Mic19 instances and reference strain
  outcome: supported
  summary: Reviewed P36112/MIC60 aliases FCJ1/AIM28/FMP13 and P43594/MIC19 aliases
    AIM13/MCS19 match S288C 559292. Both current exact queries return one entry. These
    references remain distinct from YPH499 cellular assays and thermophilic purified
    constructs.
  target_ids:
  - cellstructuremech:mic60_mic19_complex
  evidence_ids:
  - micro-record-1
  - micro-protein-P36112-retry
  - micro-protein-P43594-retry
  - micro-query-MIC60-final
  - micro-query-MIC19-retry
  - micro-tax-559292
- assessment_id: micro-mic60-remodeling
  area: evidence
  topic: Direct binding, liposome recruitment and remodeling
  outcome: supported
  summary: Hessenberger purified C. thermophilum Mic60sol/Mic19 supports direct CHCH/mitofilin
    binding, recruitment and enhanced Folch tubulation, with LBS/domain controls.
    The current graph explicitly separates constructs and yeast rescue. Leakage is
    not physiological barrier behavior.
  target_ids:
  - cellstructuremech:mic60_mic19_complex
  evidence_ids:
  - micro-record-1
  - micro-hessenberger2017-s3
- assessment_id: micro-mic60-structure
  area: evidence
  topic: Construct-specific tetramer and strut model
  outcome: supported
  summary: Bock-Bierbaum L. thermotolerans coiled-coil and C. thermophilum engineered
    complexes support tetramer/heteromer models; YPH499 assays are separate. Native
    filament identity and strut/barrier interpretation remain unresolved. Current
    notes do not assert universal 4:4 or directly observed native barrier.
  target_ids:
  - cellstructuremech:mic60_mic19_complex
  evidence_ids:
  - micro-record-1
  - micro-bock2022-s3
- assessment_id: micro-mic60-graph
  area: graph
  topic: All five current remodeling edges
  outcome: supported
  summary: Direct Mic19/Mic60 binding, lipid recruitment, higher-order assembly and
    tubulation edges are supported at their expressly in-vitro construct scope. Explicit
    lipid-dependent complex is not confused with an obligatory extra protein. Native
    types and references agree.
  target_ids:
  - cellstructuremech:mic60_mic19_complex
  evidence_ids:
  - micro-record-1
  - micro-graph-policy
  - micro-hessenberger2017-s3
  - micro-bock2022-s3
  - micro-native-mic60_mic19_complex-causal
- assessment_id: micro-mic60-image
  area: evidence
  topic: Complete Figure4 pixels, caption and licence
  outcome: supported
  summary: Fresh image equals maintained bytes; complete a–i visually inspected. YPH499
    affinity/growth/cryo-TEM500 nm/counts/respiratory activities are contextual cellular
    evidence, not an isolatedMic60–Mic19 structure. Full-multipanel OTHER modality
    and CC BY 4.0 rights are consistent.
  target_ids:
  - cellstructuremech:mic60_mic19_complex
  evidence_ids:
  - micro-record-1
  - micro-image-1
  - micro-hessenberger2017-fig4
  - micro-hessenberger2017-s3
- assessment_id: micro-localization-citations
  area: evidence
  topic: Protein-example localization bibliography
  outcome: supported
  summary: Current native location comments and exact indexed PMIDs support the cited
    reference attributions. Reinders 2006, Huh 2003, Rabl 2009 and von der Malsburg
    2011 were read at complete indexed abstract/native annotation tier only, not full
    experiments. Hoppins body was separately read. No localisation citation is inflated
    into universal formation proof.
  target_ids:
  - cellstructuremech:mic10_subcomplex
  - cellstructuremech:mic60_mic19_complex
  evidence_ids:
  - micro-pmid-16823961
  - micro-pmid-14562095
  - micro-pmid-19528297
  - micro-pmid-21944719
  - micro-pmid-21987634
  - micro-protein-Q96VH5-final
  - micro-protein-P36112-retry
  - micro-protein-P43594-retry
  - micro-hoppins2011-s3
- assessment_id: micro-micos-parthood-refresh
  area: graph
  topic: Substantive reciprocal subcomplex refresh
  outcome: supported
  summary: Newhas_part Mic10 and Mic60–Mic19 links reciprocate the actual child part_of
    GO:0061617. Friedman independent subcomplexes and Rampelt normal four-protein
    Mic10 module support the partition; Mic60–Mic19 primary interaction/body supports
    the other module. Links do not impose universal stoichiometry, identical conditional
    assembly or physical exclusivity. Historical#2462 is not given a new grouped disposition.
  target_ids:
  - GO:0061617
  evidence_ids:
  - micro-micos-stale-delta
  - micro-record-0
  - micro-record-1
  - micro-record-2
  - micro-friedman2015-s3
  - micro-rampelt2018-pdf
  - micro-hessenberger2017-s3
- assessment_id: micro-micos-primary
  area: evidence
  topic: Whole MICOS architecture and junction maintenance
  outcome: supported
  summary: Hoppins W303 purifications, localization and mutant microscopy support
    six-member MICOS/MitOS organization and membrane contacts. Residual junctions
    in mutant sections/tomograms expressly limit universal formation necessity. Recordmaintenance/organization
    functions preserve that bound. Harner and vonderMalsburg are complete abstracts
    only in this review.
  target_ids:
  - GO:0061617
  evidence_ids:
  - micro-record-2
  - micro-hoppins2011-s3
  - micro-harner2011-meta
  - micro-malsburg2011-meta
- assessment_id: micro-micos-nomenclature
  area: identity
  topic: MICOS/MINOS/MitOS aliases and six yeast names
  outcome: supported
  summary: Pfanner 2014 complete nomenclature body/Table 1 supports exact aliases
    and standardized Mic names, explicitly distinguishes mammalian Mic25 and lineage
    variations. It is consensus authority, not an independent primary assembly experiment.
  target_ids:
  - GO:0061617
  evidence_ids:
  - micro-record-2
  - micro-pfanner2014-s3
  - micro-go
- assessment_id: micro-micos-sparse-inventory
  area: scope
  topic: Source-neutral deferred inventory
  outcome: supported
  summary: No individual component rows or proteinexamples does not contradict the
    correct whole-complex definition, current parthood or declared deferred groundings.
    Optional expansion is not a confirmed defect. No new blanket family/formation
    requirement or resolution of the broad inventory task is inferred.
  target_ids:
  - GO:0061617
  evidence_ids:
  - micro-record-2
  - micro-policy
  - micro-schema
  - micro-go
  - micro-native-micos_complex-causal
- assessment_id: micro-micos-functional-graph
  area: graph
  topic: Three current nonmechanistic function relations
  outcome: supported
  summary: Whole MICOS parthood in inner membrane, junction maintenance and organization
    relations match currentGO/primary scopes. FUNCTION/NONMECHANISTIC qualification
    correctly withholds a detailed assembly mechanism and does not claim every junction
    requires MICOS.
  target_ids:
  - GO:0061617
  evidence_ids:
  - micro-record-2
  - micro-go
  - micro-hoppins2011-s3
  - micro-graph-policy
- assessment_id: micro-historical-access-kind
  area: provenance
  topic: Exact old Harner access observation
  outcome: concern
  summary: The original HTTP500/no-body prose is honest, but kindauthority is inappropriate
    for transport-only evidence. Successor must use validation/context_only without
    rewriting old timestamps/hashes or claiming current challenge/404 bodies contain
    science.
  target_ids:
  - GO:0061617
  evidence_ids:
  - micro-prior-2
  - micro-historical-harner-access
  - micro-harner2011-s3
  - micro-harner2011-legacy
- assessment_id: micro-taxa-history-limits
  area: scope
  topic: Occurrence, strain and preserved provenance
  outcome: supported
  summary: COMMON is qualitative occurrence with exceptions, not a measured strain
    census. W303, YPH499, referenceS288C, C. thermophilum and L. thermotolerans contexts
    stay separate. Historical discussion rationale remains append-only and open native
    architecture/grounding questions remain open; later examples do not retroactively
    invalidate historical provenance.
  target_ids:
  - cellstructuremech:mic10_subcomplex
  - cellstructuremech:mic60_mic19_complex
  - GO:0061617
  evidence_ids:
  - micro-record-0
  - micro-record-1
  - micro-record-2
  - micro-policy
  - micro-tax-4932
  - micro-tax-559292
  - micro-friedman2015-s3
  - micro-hessenberger2017-s3
  - micro-bock2022-s3
- assessment_id: plaque-t3-identity
  area: identity
  topic: Exact MIM identity and anatomical boundary
  outcome: supported
  summary: GO0140595 identifies MIM, distinct from TOM/SAM and the outer membrane
    itself. Current parent/part_of and import-function scope agree with native authority.
    No partner or substrate is turned into an intrinsic MIM constituent.
  target_ids:
  - GO:0140595
  evidence_ids:
  - plaque-record-3
  - plaque-go-0140595
  - plaque-go-0098799
  - plaque-go-0005741
  - plaque-go-7770059
- assessment_id: plaque-t3-grounding
  area: grounding
  topic: Constituent family and species-example grounding
  outcome: supported
  summary: IPR013262 and IPR037652 are actual families for Mim1/Tom13 and Mim2; Q08176
    and Q3E798 are reviewed S288C examples. Legacy beta-barrel-biogenesis descriptions
    are indirect assembly history, not a claim that MIM forms the beta-barrel insertase.
  target_ids:
  - GO:0140595
  evidence_ids:
  - plaque-record-3
  - plaque-ipr-IPR013262
  - plaque-ipr-IPR037652
  - plaque-up-Q08176-retry
  - plaque-up-Q3E798
  - plaque-pmid-15326197
  - plaque-pmid-15608614
- assessment_id: plaque-t3-function
  area: evidence
  topic: Import mechanism versus assay dependence
  outcome: supported
  summary: Selected Doan import experiments support the represented single-spanning
    substrates and TOM/SAM-associated populations. Vitali steady-state/localization
    evidence retains substrate variability and indirect-effect limits. The record
    already distinguishes these assays rather than requiring every helical client
    to use MIM exclusively.
  target_ids:
  - GO:0140595
  evidence_ids:
  - plaque-record-3
  - plaque-doan2020-metadata
  - plaque-doan2020-web-sections
  - plaque-doan2020-web-methods
  - plaque-PMC6965732-jats
- assessment_id: plaque-t3-formation
  area: scope
  topic: Coassembly, stoichiometry and stabilization scope
  outcome: supported
  summary: Added Mim1/Mim2 coassembly is supported. Multiple Mim1/one-or-two Mim2
    is a cited background inference, not a fixed directly counted universal stoichiometry.
    Additional Dimmer Results support a Mim2 contribution to Mim1 abundance/native
    assembly while overexpressed Mim1 can oligomerize without Mim2. The graph does
    not assign universal ESSENTIAL formation status; existing architecture uncertainty
    remains appropriate.
  target_ids:
  - GO:0140595
  evidence_ids:
  - plaque-record-3
  - plaque-delta-3
  - plaque-PMC6010339-jats
  - plaque-doan2020-web-indexed
  - plaque-dimmer2012-web-sections
  - plaque-up-Q3E798
- assessment_id: plaque-t3-snippets
  area: provenance
  topic: Three new quoted snippets require verbatim correction
  outcome: concern
  summary: The two repeated Doan snippets combine the import and composition assertions
    into wording different from the inspected passage; the Vitali combined sentence
    is absent from the normalized complete JATS. Composition remains supported. Move
    paraphrase into notes or recopy exact source wording; do not reverse biological
    membership.
  target_ids:
  - GO:0140595
  evidence_ids:
  - plaque-record-3
  - plaque-delta-3
  - plaque-policy
  - plaque-doan2020-web-indexed
  - plaque-PMC6010339-jats
  - plaque-mim-peer-challenge
- assessment_id: plaque-t3-taxa
  area: scope
  topic: Natural host, experimental strain and heterologous rescue
  outcome: supported
  summary: Natural yeast/fungal MIM scope is distinct from S288C sequence examples,
    YPH499 Doan assays and W303 Vitali experiments. Heterologous Mim1/Mim2 expression
    in T. brucei and pATOM36 rescue in yeast demonstrate partial functional exchange,
    not native trypanosome MIM occurrence.
  target_ids:
  - GO:0140595
  evidence_ids:
  - plaque-record-3
  - plaque-tax-4932
  - plaque-tax-559292
  - plaque-doan2020-web-methods
  - plaque-PMC6010339-jats
- assessment_id: plaque-t3-graph
  area: consistency
  topic: Current graph actors and changed assembly edges
  outcome: supported
  summary: Two added component_ref actors are correctly anchored to the represented
    families/examples. Existing TOM-associated and SAM-associated populations are
    distinct; dynamic exchange remains proposed rather than directly visualized, and
    the Tom6 SAM intermediate is supported by native-gel/shift assays. New evidence
    wording is addressed separately.
  target_ids:
  - GO:0140595
  evidence_ids:
  - plaque-record-3
  - plaque-delta-3
  - plaque-doan2020-web-methods
  - plaque-native-mim_complex-causal
  - plaque-PMC6010339-jats
- assessment_id: plaque-t3-image
  area: evidence
  topic: Actual Figure5 pixels, attribution and modality
  outcome: supported
  summary: All maintained pixels were viewed; source JPEG is byte-identical. Caption
    and CC BY4.0 permissions support author/source attribution. Mito-GFP/brightfield
    panels and morphology proportions demonstrate rescue in deletion strains, not
    localization or molecular structure of MIM.
  target_ids:
  - GO:0140595
  evidence_ids:
  - plaque-maintained-image
  - plaque-mim-figure5
  - plaque-mim-package
  - plaque-PMC6010339-jats
- assessment_id: plaque-t3-native
  area: schema
  topic: Native inventory and original contract
  outcome: supported
  summary: Fresh verify and causal checks pass for two reviewed examples/two COVERED
    nodes. Original pair validates/renders exactly and historical inputs verify; changed
    current claims were reassessed. Identity coverage does not establish functional
    necessity.
  target_ids:
  - GO:0140595
  evidence_ids:
  - plaque-original-native-checks
  - plaque-native-mim_complex-verify
  - plaque-native-mim_complex-causal
  - plaque-original-3
- assessment_id: plaque-t3-applicability
  area: scope
  topic: Whole-record structured-source assessment
  outcome: not_applicable
  summary: Original lacks both a formal applicability check and prose assessment.
    The current protein/import narrative triggers a check; complete current official
    catalogue has no matched natural fungal host. No foreign-host downstream proxy
    is used, and catalogue noncoverage is not biological absence.
  target_ids:
  - GO:0140595
  evidence_ids:
  - plaque-original-3
  - plaque-skill
  - plaque-adapter-catalogue
  - plaque-record-3
- assessment_id: plaque-t3-verdict
  area: completeness
  topic: Scoped disposition
  outcome: concern
  summary: Current MIM needs curation only for the new minor verbatim-provenance finding.
    Optional architecture, stoichiometry and mechanism unknowns are not separate defects.
    Historical failed-route kinds and stale review inputs require successor correction,
    not alteration of the original pair.
  target_ids:
  - GO:0140595
  evidence_ids:
  - plaque-record-3
  - plaque-original-3
  - plaque-original-native-checks
  - plaque-mim-peer-challenge
- assessment_id: plaque-t4-identity
  area: identity
  topic: Exact MIS12/MIND identity and current hierarchy
  outcome: supported
  summary: The cross-eukaryotic complex identity remains correct. Changed GO0032991
    parent and GO0000940/GO0000776 parthood preserve complex-versus-whole-kinetochore
    boundaries. Prior group hierarchy history does not resolve the separate family
    or synonym findings.
  target_ids:
  - GO:0000444
  evidence_ids:
  - plaque-record-4
  - plaque-delta-4
  - plaque-go-0000444
  - plaque-go-0032991
  - plaque-go-0000940
  - plaque-go-0000776
- assessment_id: plaque-t4-grounding
  area: grounding
  topic: Reconfirmed class-grounding finding
  outcome: concern
  summary: Four exact current family authorities plus member UniProt cross-references
    support IPR008685/IPR013218/IPR013950/IPR007128 for the already named classes.
    IPR016851 is narrower. This is a current active grounding gap, not falsification
    of a dated search or a requirement that every class acquire extra species examples.
  target_ids:
  - GO:0000444
  evidence_ids:
  - plaque-record-4
  - plaque-policy
  - plaque-ipr-IPR008685
  - plaque-ipr-IPR013218
  - plaque-ipr-IPR013950
  - plaque-ipr-IPR007128
  - plaque-ipr-IPR016851
  - plaque-up-P39731
  - plaque-up-P40568
  - plaque-up-Q12143
  - plaque-up-P47149-retry
- assessment_id: plaque-t4-synonyms
  area: identity
  topic: Reconfirmed authority qualifier mismatch
  outcome: concern
  summary: Native GO gives MIND complex EXACT, Mis12 complex NARROW, and the expanded
    Mtw1p and nuclear phrases RELATED. The maintained four-EXACT representation overstates
    only these qualifier scopes; primary identity and synonym text remain valid.
  target_ids:
  - GO:0000444
  evidence_ids:
  - plaque-record-4
  - plaque-go-0000444
  - plaque-original-4
- assessment_id: plaque-t4-composition
  area: evidence
  topic: Yeast association and human reconstitution independently verified
  outcome: supported
  summary: De Wulf supports the yeast four-protein MIND cohort with multiple hydrodynamic
    states. Kline genuinely coexpressed/purified four human proteins from E. coli
    and compared endogenous HeLa behavior. The new reconstituted-human-complex note
    is supported; it is not a yeast reconstitution or a natural bacterial complex.
  target_ids:
  - GO:0000444
  evidence_ids:
  - plaque-record-4
  - plaque-delta-4
  - plaque-dewulf2003-legacy
  - plaque-kline2006-jats
- assessment_id: plaque-t4-formation
  area: scope
  topic: Conditional assembly/localization versus universal requirement
  outcome: supported
  summary: Yeast conditional partner stability/CEN association and vertebrate depletion/localization
    outcomes have distinct experimental scopes. These results do not compel universal
    all-species ESSENTIAL assignments or a new assay. Existing UNKNOWN formation necessity
    is retained.
  target_ids:
  - GO:0000444
  evidence_ids:
  - plaque-record-4
  - plaque-dewulf2003-legacy
  - plaque-kline2006-jats
  - plaque-schema
  - plaque-policy
- assessment_id: plaque-t4-references
  area: provenance
  topic: Bibliography and primary access limits
  outcome: supported
  summary: Primary bodies substantiate scoped De Wulf/Kline association and recruitment
    claims. Euskirchen/Pinsky/Scharfenberger were read at complete native abstract
    tier, sufficient for bounded example descriptions but not an unclaimed Methods
    or figure inspection.
  target_ids:
  - GO:0000444
  evidence_ids:
  - plaque-dewulf2003-metadata
  - plaque-kline2006-metadata
  - plaque-dewulf2003-legacy
  - plaque-kline2006-jats
  - plaque-pmid-12455957
  - plaque-pmid-14602074
  - plaque-pmid-14657030
- assessment_id: plaque-t4-taxa
  area: scope
  topic: Reference accessions and experimental models
  outcome: supported
  summary: All four maintained examples are reviewed budding-yeast S288C entries;
    natural species taxon4932 is separate. Kline human and chicken assays and recombinant
    bacterial production are not conflated with De Wulf W303-congenic cultures. The
    class labels may span orthologues without requiring exhaustive example inventory.
  target_ids:
  - GO:0000444
  evidence_ids:
  - plaque-record-4
  - plaque-tax-4932
  - plaque-tax-559292
  - plaque-up-P39731
  - plaque-up-P40568
  - plaque-up-Q12143
  - plaque-up-P47149-retry
  - plaque-dewulf2003-legacy
  - plaque-kline2006-jats
- assessment_id: plaque-t4-graph
  area: consistency
  topic: New component anchors and external recruited actors
  outcome: supported
  summary: Four new component_ref nodes/edges correctly distinguish intrinsic classes
    from the Ndc80/Nuf2/Spc24 outer microtubule-binding actor. Gene/UniProt correspondence
    is valid. Coarse NONMECHANISTIC bridge/recruitment does not assert a universal
    yeast MIND-to-Ndc80 assembly dependency or make recruited proteins MIND constituents.
  target_ids:
  - GO:0000444
  evidence_ids:
  - plaque-record-4
  - plaque-delta-4
  - plaque-up-P40460
  - plaque-up-P33895
  - plaque-up-Q04477-retry
  - plaque-dewulf2003-legacy
  - plaque-kline2006-jats
- assessment_id: plaque-t4-native
  area: schema
  topic: Actual native coverage diagnostics
  outcome: supported
  summary: Four examples verify. Five typed nodes yield 2 COVERED, 2 PARTIAL_EXAMPLES
    for additional class symbols MIS12/PMF1, and 1 UNANCHORED_WITH_UNIPROT external
    actor. These accurate diagnostics do not mandate optional extra examples or turn
    the external actor into a constituent. Original native pair and historical hashes
    pass.
  target_ids:
  - GO:0000444
  evidence_ids:
  - plaque-native-mis12_mind_type_complex-verify
  - plaque-native-mis12_mind_type_complex-causal
  - plaque-original-native-checks
  - plaque-original-4
- assessment_id: plaque-t4-applicability
  area: scope
  topic: Molecular narrative triggers assessment despite absent catalogue host
  outcome: not_applicable
  summary: Original has no formal or prose structured-source applicability assessment.
    Current protein/recruitment claims require checking; the complete official catalogue
    has no yeast, human or chicken host dataset. No E. coli expression-host proxy
    or absent-module biological claim is made.
  target_ids:
  - GO:0000444
  evidence_ids:
  - plaque-record-4
  - plaque-original-4
  - plaque-skill
  - plaque-adapter-catalogue
- assessment_id: plaque-t4-verdict
  area: completeness
  topic: Two inherited minor findings remain open
  outcome: concern
  summary: Both exact original stable keys are reconfirmed with complete repository/review/finding
    lineage. The stale hierarchy/component-edge additions are substantively supported
    and do not close either finding. Current historical rationale remains append-only;
    actions change current fields/notes.
  target_ids:
  - GO:0000444
  evidence_ids:
  - plaque-original-4
  - plaque-record-4
  - plaque-delta-4
  - plaque-go-0000444
  - plaque-ipr-IPR007128
  - plaque-policy
- assessment_id: plaque-t5-identity
  area: identity
  topic: IMP identity, parents and membrane boundary
  outcome: supported
  summary: GO0042720 exactly denotes the mitochondrial inner membrane peptidase complex,
    with the represented membrane/serine endopeptidase parents and inner-membrane
    location. Substrates targeted to the intermembrane space do not relocate the enzyme
    complex into the lumen.
  target_ids:
  - GO:0042720
  evidence_ids:
  - plaque-record-5
  - plaque-go-0042720
  - plaque-go-0098800
  - plaque-go-1905370
  - plaque-go-0005743
- assessment_id: plaque-t5-composition
  area: completeness
  topic: Optional inventory and named-subunit scope
  outcome: supported
  summary: Jan primary abstract describes Imp1/Imp2 and proposed third component Som1.
    The record does not deny those proteins; it deliberately leaves optional constituent/examples
    fields unpopulated while tracking curation. No empty-field or compulsory family-enrichment
    finding is established.
  target_ids:
  - GO:0042720
  evidence_ids:
  - plaque-record-5
  - plaque-jan2000-metadata
  - plaque-policy
- assessment_id: plaque-t5-formation
  area: scope
  topic: Som1 association versus complex-formation necessity
  outcome: supported
  summary: Jan abstract supports a physical Som1/Imp1 interaction and proposed component
    role, not a universal loss-of-whole-complex claim. No formation essentiality is
    assigned or inferred from processing activity. A qualified pass is appropriate
    at this evidence tier.
  target_ids:
  - GO:0042720
  evidence_ids:
  - plaque-record-5
  - plaque-jan2000-metadata
  - plaque-schema
- assessment_id: plaque-t5-function
  area: evidence
  topic: Processing of nuclear and mitochondrial substrates
  outcome: supported
  summary: GO definition and primary abstract support membrane-associated cleavage/processing
    with precursor/substrate differences. The record correctly avoids an after-import-only
    restriction and preserves nuclear- and mitochondrially encoded substrate scope.
    Gakh review abstract is secondary context, not a fresh primary mechanistic assay.
  target_ids:
  - GO:0042720
  evidence_ids:
  - plaque-record-5
  - plaque-go-0042720
  - plaque-go-0034982
  - plaque-jan2000-metadata
  - plaque-gakh2002-pmid
- assessment_id: plaque-t5-reference-tier
  area: provenance
  topic: Actual reference tiers and access limits
  outcome: supported
  summary: Jan is independently read at complete primary abstract tier, current publisher
    route remains limited. Gakh is a secondary review read at native abstract tier.
    Original two Jan challenge observations belong to validation/context_only and
    the DOI-returned Crossref row to database/context_only, preserving original dates/hashes.
  target_ids:
  - GO:0042720
  evidence_ids:
  - plaque-original-5
  - plaque-jan2000-metadata
  - plaque-jan2000-publisher
  - plaque-gakh2002-pmid
  - plaque-historical-t5-micro60-jan2000-publisher
  - plaque-historical-t5-micro60-jan2000-pdf
  - plaque-historical-t5-micro60-gakh2002-publisher
- assessment_id: plaque-t5-taxa
  area: scope
  topic: Species-level example without invented strain
  outcome: supported
  summary: The S. cerevisiae example remains species-level. Neither unread Jan Methods
    nor a secondary abstract justifies inventing a strain or treating S288C as the
    exact experimental culture. COMMON is retained for species occurrence, not recast
    as a measured prevalence percentage.
  target_ids:
  - GO:0042720
  evidence_ids:
  - plaque-record-5
  - plaque-tax-4932
  - plaque-jan2000-metadata
  - plaque-gakh2002-pmid
- assessment_id: plaque-t5-graph
  area: consistency
  topic: Coarse descriptive graph matches evidence
  outcome: supported
  summary: The two NONMECHANISTIC parthood/processing relations stay at supported
    anatomical and functional resolution. No omitted universal pathway intermediate,
    component essentiality or mechanistic causal chain is required.
  target_ids:
  - GO:0042720
  evidence_ids:
  - plaque-record-5
  - plaque-go-0042720
  - plaque-go-0034982
  - plaque-jan2000-metadata
- assessment_id: plaque-t5-image
  area: scope
  topic: No maintained image claim
  outcome: not_applicable
  summary: This target has no maintained image; no image evidence or licence is invented.
    Absence of an optional image is not a finding.
  target_ids:
  - GO:0042720
  evidence_ids:
  - plaque-record-5
- assessment_id: plaque-t5-native
  area: schema
  topic: Empty inventory and immutable original
  outcome: supported
  summary: Fresh native commands exit0 with zero examples/typed nodes. This is an
    actual empty-inventory result, not proof of molecular completeness. Original pair
    validates and renders exactly, target bytes remain unchanged, and historical inputs
    verify.
  target_ids:
  - GO:0042720
  evidence_ids:
  - plaque-record-5
  - plaque-original-native-checks
  - plaque-native-mitochondrial_inner_membrane_peptidase_complex-verify
  - plaque-native-mitochondrial_inner_membrane_peptidase_complex-causal
- assessment_id: plaque-t5-applicability
  area: scope
  topic: Proteolysis narrative requires structured-source assessment
  outcome: not_applicable
  summary: Original omits a formal check and any prose applicability decision. Positive
    peptidase/processing assertions trigger current catalogue inspection despite zero
    examples. No matched natural yeast host exists in the complete response; no foreign
    proxy or biological absence is inferred.
  target_ids:
  - GO:0042720
  evidence_ids:
  - plaque-record-5
  - plaque-original-5
  - plaque-skill
  - plaque-adapter-catalogue
- assessment_id: plaque-t5-verdict
  area: completeness
  topic: Qualified pass with bounded access
  outcome: supported
  summary: No scientific record finding is established. Keep the qualified pass with
    Jan abstract/Gakh secondary limits; successor repairs the original applicability
    omission and historical evidence kinds without rewriting original artefacts or
    claiming a full primary-body inspection.
  target_ids:
  - GO:0042720
  evidence_ids:
  - plaque-record-5
  - plaque-original-5
  - plaque-jan2000-metadata
  - plaque-gakh2002-pmid
  - plaque-original-native-checks
- assessment_id: septin-mitochondrial_lon_protease_complex-native
  area: schema
  topic: Original envelope, frozen inputs and current native inventory
  outcome: supported
  summary: Original native validation and Markdown reproduction pass, with unchanged
    target bytes. Current native inventory is 1 protein examples and one COVERED typed
    node. Reference validation is distinct from source-specific scientific membership
    or causal necessity.
  target_ids:
  - cellstructuremech:mitochondrial_lon_protease_complex
  evidence_ids:
  - septin-record-mitochondrial_lon_protease_complex
  - septin-original-mitochondrial_lon_protease_complex
  - septin-original-native-checks
  - septin-native-mitochondrial_lon_protease_complex-verify
  - septin-native-mitochondrial_lon_protease_complex-causal
- assessment_id: septin-mitochondrial_lon_protease_complex-applicability
  area: evidence
  topic: Required structured-source applicability
  outcome: supported
  summary: Positive protease, import, protein-complex, metabolic or mitochondrial-organization
    claims trigger assessment. The original formal expression-only N/A rationale is
    unsupported. Current full catalogue has no matching biological host; disclose
    this bounded coverage limit, retain actual historical runner failure and use inspected
    primary/native authorities. No downstream unmatched E. coli proxy or expression-to-assembly
    inference.
  target_ids:
  - cellstructuremech:mitochondrial_lon_protease_complex
  evidence_ids:
  - septin-record-mitochondrial_lon_protease_complex
  - septin-original-mitochondrial_lon_protease_complex
  - septin-review-policy
  - septin-adapter-catalogue
  - septin-historical-adapter-runner
- assessment_id: septin-mitochondrial_lon_protease_complex-provenance
  area: provenance
  topic: Citation, historical rationale and exact input provenance
  outcome: supported
  summary: Original YAML/Markdown and dated discussions remain immutable. Original
    same-base global checks identify their actual historical batch26 execution; this
    is not an erroneous current cohort label. No record edits or terminal resolution
    of neighboring/group issues. Current records contain no verbatim snippets to certify.
  target_ids:
  - cellstructuremech:mitochondrial_lon_protease_complex
  evidence_ids:
  - septin-record-mitochondrial_lon_protease_complex
  - septin-original-mitochondrial_lon_protease_complex
  - septin-original-native-checks
  - septin-curation-policy
  - septin-literature-policy
- assessment_id: septin-mitochondrial_lon_protease_complex-history-kinds
  area: evidence
  topic: Historical source access classification
  outcome: supported
  summary: All original evidence rows read. The original failed XML/empty PANTHER
    diagnostics named in the grouped bundle defect must use validation, with context_only
    and explicit failure retained; no original body-claim fabrication is alleged.
  target_ids:
  - cellstructuremech:mitochondrial_lon_protease_complex
  evidence_ids:
  - septin-record-mitochondrial_lon_protease_complex
  - septin-original-mitochondrial_lon_protease_complex
  - septin-literature-policy
- assessment_id: septin-mitochondrial_multifunctional_assembly-native
  area: schema
  topic: Original envelope, frozen inputs and current native inventory
  outcome: supported
  summary: Original native validation and Markdown reproduction pass, with unchanged
    target bytes. Current native inventory is 5 protein examples and one COVERED typed
    node. Reference validation is distinct from source-specific scientific membership
    or causal necessity.
  target_ids:
  - cellstructuremech:mitochondrial_multifunctional_assembly
  evidence_ids:
  - septin-record-mitochondrial_multifunctional_assembly
  - septin-original-mitochondrial_multifunctional_assembly
  - septin-original-native-checks
  - septin-native-mitochondrial_multifunctional_assembly-verify
  - septin-native-mitochondrial_multifunctional_assembly-causal
- assessment_id: septin-mitochondrial_multifunctional_assembly-applicability
  area: evidence
  topic: Required structured-source applicability
  outcome: supported
  summary: Positive protease, import, protein-complex, metabolic or mitochondrial-organization
    claims trigger assessment. The original formal expression-only N/A rationale is
    unsupported. Current full catalogue has no matching biological host; disclose
    this bounded coverage limit, retain actual historical runner failure and use inspected
    primary/native authorities. No downstream unmatched E. coli proxy or expression-to-assembly
    inference.
  target_ids:
  - cellstructuremech:mitochondrial_multifunctional_assembly
  evidence_ids:
  - septin-record-mitochondrial_multifunctional_assembly
  - septin-original-mitochondrial_multifunctional_assembly
  - septin-review-policy
  - septin-adapter-catalogue
  - septin-historical-adapter-runner
- assessment_id: septin-mitochondrial_multifunctional_assembly-provenance
  area: provenance
  topic: Citation, historical rationale and exact input provenance
  outcome: supported
  summary: Original YAML/Markdown and dated discussions remain immutable. Original
    same-base global checks identify their actual historical batch26 execution; this
    is not an erroneous current cohort label. No record edits or terminal resolution
    of neighboring/group issues. Current records contain no verbatim snippets to certify.
  target_ids:
  - cellstructuremech:mitochondrial_multifunctional_assembly
  evidence_ids:
  - septin-record-mitochondrial_multifunctional_assembly
  - septin-original-mitochondrial_multifunctional_assembly
  - septin-original-native-checks
  - septin-curation-policy
  - septin-literature-policy
- assessment_id: septin-mitochondrial_multifunctional_assembly-history-kinds
  area: evidence
  topic: Historical source access classification
  outcome: supported
  summary: All original evidence rows read. The original failed XML/empty PANTHER
    diagnostics named in the grouped bundle defect must use validation, with context_only
    and explicit failure retained; no original body-claim fabrication is alleged.
  target_ids:
  - cellstructuremech:mitochondrial_multifunctional_assembly
  evidence_ids:
  - septin-record-mitochondrial_multifunctional_assembly
  - septin-original-mitochondrial_multifunctional_assembly
  - septin-literature-policy
- assessment_id: septin-mitochondrial_outer_membrane_translocase_complex-native
  area: schema
  topic: Original envelope, frozen inputs and current native inventory
  outcome: supported
  summary: Original native validation and Markdown reproduction pass, with unchanged
    target bytes. Current native inventory is 0 protein examples and zero typed nodes;
    empty coverage is not evidence of complete molecular representation. Reference
    validation is distinct from source-specific scientific membership or causal necessity.
  target_ids:
  - GO:0005742
  evidence_ids:
  - septin-record-mitochondrial_outer_membrane_translocase_complex
  - septin-original-mitochondrial_outer_membrane_translocase_complex
  - septin-original-native-checks
  - septin-native-mitochondrial_outer_membrane_translocase_complex-verify
  - septin-native-mitochondrial_outer_membrane_translocase_complex-causal
- assessment_id: septin-mitochondrial_outer_membrane_translocase_complex-applicability
  area: evidence
  topic: Required structured-source applicability
  outcome: supported
  summary: Positive protease, import, protein-complex, metabolic or mitochondrial-organization
    claims trigger assessment. The original formal expression-only N/A rationale is
    unsupported. Current full catalogue has no matching biological host; disclose
    this bounded coverage limit, retain actual historical runner failure and use inspected
    primary/native authorities. No downstream unmatched E. coli proxy or expression-to-assembly
    inference.
  target_ids:
  - GO:0005742
  evidence_ids:
  - septin-record-mitochondrial_outer_membrane_translocase_complex
  - septin-original-mitochondrial_outer_membrane_translocase_complex
  - septin-review-policy
  - septin-adapter-catalogue
  - septin-historical-adapter-runner
- assessment_id: septin-mitochondrial_outer_membrane_translocase_complex-provenance
  area: provenance
  topic: Citation, historical rationale and exact input provenance
  outcome: supported
  summary: Original YAML/Markdown and dated discussions remain immutable. Original
    same-base global checks identify their actual historical batch26 execution; this
    is not an erroneous current cohort label. No record edits or terminal resolution
    of neighboring/group issues. Current records contain no verbatim snippets to certify.
  target_ids:
  - GO:0005742
  evidence_ids:
  - septin-record-mitochondrial_outer_membrane_translocase_complex
  - septin-original-mitochondrial_outer_membrane_translocase_complex
  - septin-original-native-checks
  - septin-curation-policy
  - septin-literature-policy
- assessment_id: septin-mitochondrial_outer_membrane_translocase_complex-history-kinds
  area: evidence
  topic: Historical source access classification
  outcome: supported
  summary: All original evidence rows read. No additional access-kind defect established
    in this original; the scientific synonym finding remains separate.
  target_ids:
  - GO:0005742
  evidence_ids:
  - septin-record-mitochondrial_outer_membrane_translocase_complex
  - septin-original-mitochondrial_outer_membrane_translocase_complex
  - septin-literature-policy
- assessment_id: septin-mitochondrial_prohibitin_complex-native
  area: schema
  topic: Original envelope, frozen inputs and current native inventory
  outcome: supported
  summary: Original native validation and Markdown reproduction pass, with unchanged
    target bytes. Current native inventory is 0 protein examples and zero typed nodes;
    empty coverage is not evidence of complete molecular representation. Reference
    validation is distinct from source-specific scientific membership or causal necessity.
  target_ids:
  - GO:0035632
  evidence_ids:
  - septin-record-mitochondrial_prohibitin_complex
  - septin-original-mitochondrial_prohibitin_complex
  - septin-original-native-checks
  - septin-native-mitochondrial_prohibitin_complex-verify
  - septin-native-mitochondrial_prohibitin_complex-causal
- assessment_id: septin-mitochondrial_prohibitin_complex-applicability
  area: evidence
  topic: Required structured-source applicability
  outcome: supported
  summary: Positive protease, import, protein-complex, metabolic or mitochondrial-organization
    claims trigger assessment. The original formal expression-only N/A rationale is
    unsupported. Current full catalogue has no matching biological host; disclose
    this bounded coverage limit, retain actual historical runner failure and use inspected
    primary/native authorities. No downstream unmatched E. coli proxy or expression-to-assembly
    inference.
  target_ids:
  - GO:0035632
  evidence_ids:
  - septin-record-mitochondrial_prohibitin_complex
  - septin-original-mitochondrial_prohibitin_complex
  - septin-review-policy
  - septin-adapter-catalogue
  - septin-historical-adapter-runner
- assessment_id: septin-mitochondrial_prohibitin_complex-provenance
  area: provenance
  topic: Citation, historical rationale and exact input provenance
  outcome: supported
  summary: Original YAML/Markdown and dated discussions remain immutable. Original
    same-base global checks identify their actual historical batch26 execution; this
    is not an erroneous current cohort label. No record edits or terminal resolution
    of neighboring/group issues. Current records contain no verbatim snippets to certify.
  target_ids:
  - GO:0035632
  evidence_ids:
  - septin-record-mitochondrial_prohibitin_complex
  - septin-original-mitochondrial_prohibitin_complex
  - septin-original-native-checks
  - septin-curation-policy
  - septin-literature-policy
- assessment_id: septin-mitochondrial_prohibitin_complex-history-kinds
  area: evidence
  topic: Historical source access classification
  outcome: supported
  summary: All original evidence rows read. The original failed XML/empty PANTHER
    diagnostics named in the grouped bundle defect must use validation, with context_only
    and explicit failure retained; no original body-claim fabrication is alleged.
  target_ids:
  - GO:0035632
  evidence_ids:
  - septin-record-mitochondrial_prohibitin_complex
  - septin-original-mitochondrial_prohibitin_complex
  - septin-literature-policy
- assessment_id: septin-mitochondrial_lon_protease_complex-identity
  area: identity
  topic: Mitochondrial oligomer versus protein and broader family
  outcome: supported
  summary: Local identity denotes a mitochondrial peptidase assembly, not an isolated
    Lon protein or all chloroplastic members of IPR027503. GO1905368 parent and matrix
    location are appropriate. Bounded GO searches did not establish an exact alternative;
    broad search first pages are not exhaustive.
  target_ids:
  - cellstructuremech:mitochondrial_lon_protease_complex
  evidence_ids:
  - septin-record-mitochondrial_lon_protease_complex
  - septin-original-mitochondrial_lon_protease_complex
  - septin-go
  - septin-go-search-lon
  - septin-go-search-pim1
  - septin-ipr-IPR027503
- assessment_id: septin-mitochondrial_lon_protease_complex-protein
  area: grounding
  topic: Pim1 identity and reference-strain membership
  outcome: supported
  summary: Reviewed P36775 is primary PIM1 with LON alias in S288C; both current bounded
    queries return this entry. IPR027503 is broader chloroplastic/mitochondrial family,
    explicitly scoped to mitochondrial yeast instance. Native localization and primary
    structural membership are separately verified. No gene-name or strain substitution.
  target_ids:
  - cellstructuremech:mitochondrial_lon_protease_complex
  evidence_ids:
  - septin-record-mitochondrial_lon_protease_complex
  - septin-original-mitochondrial_lon_protease_complex
  - septin-protein-P36775
  - septin-query-retry-PIM1
  - septin-query-retry-LON
  - septin-ipr-IPR027503
  - septin-tax-559292
  - septin-yang2022-xml
- assessment_id: septin-mitochondrial_lon_protease_complex-stoichiometry
  area: quantity
  topic: Conflicting purified preparations and archive chain accounting
  outcome: supported
  summary: 1999 mitochondrial-extract C-terminally tagged preparation gives seven
    subunits; 2022 bacterially expressed mature substrate-bound preparation gives
    six. Current record preserves conflict and no universal count. PDB A6B1 contains
    six Pim1 chains and one substrate, not seven enzyme chains. Archive3.3A versus
    paper approximately3.21A and 4ATP/2ADP are properly distinguished.
  target_ids:
  - cellstructuremech:mitochondrial_lon_protease_complex
  evidence_ids:
  - septin-record-mitochondrial_lon_protease_complex
  - septin-original-mitochondrial_lon_protease_complex
  - septin-stahlberg1999-legacy
  - septin-yang2022-xml
  - septin-pdb-7SXO
  - septin-pdb-7SXO-assembly1
  - septin-pdb-7SXO-entity1
  - septin-pdb-7SXO-entity2
  - septin-pdb-7SXO-nonpolymer3
  - septin-pdb-7SXO-nonpolymer5
  - septin-emdb-25502
- assessment_id: septin-mitochondrial_lon_protease_complex-archive-conflict
  area: evidence
  topic: Paper accession conflict independently checked
  outcome: supported
  summary: Paper Data availability names EMD25505/7XSO, but fresh archive content
    names unrelated spike/Craspase structures. Native EMD25502/7SXO citation and Pim1
    entity mapping corroborate the record correction; no source conflict is concealed.
  target_ids:
  - cellstructuremech:mitochondrial_lon_protease_complex
  evidence_ids:
  - septin-record-mitochondrial_lon_protease_complex
  - septin-original-mitochondrial_lon_protease_complex
  - septin-yang2022-xml
  - septin-pdb-7SXO
  - septin-emdb-25502
  - septin-pdb-7XSO
  - septin-emdb-25505
- assessment_id: septin-mitochondrial_lon_protease_complex-formation
  area: completeness
  topic: Formation versus enzymatic activity
  outcome: supported
  summary: Pim1 is the defining enzyme constituent, yet the source does not make its
    substrate-bound static state a complete assembly pathway. S1015A assays concern
    proteolytic function; INSdel/GSlink retained activity is bounded to the beta-casein
    assay, not all substrates/adaptor binding/native viability. Existing UNKNOWN necessity
    and restrained formation claims remain appropriate.
  target_ids:
  - cellstructuremech:mitochondrial_lon_protease_complex
  evidence_ids:
  - septin-record-mitochondrial_lon_protease_complex
  - septin-original-mitochondrial_lon_protease_complex
  - septin-yang2022-xml
  - septin-stahlberg1999-legacy
  - septin-protein-P36775
  - septin-graph-policy
- assessment_id: septin-mitochondrial_lon_protease_complex-graph
  area: graph
  topic: Function graph and mechanistic interpretation
  outcome: supported
  summary: The graph separates structural membership, assay proteolysis, catalytic
    loss and insertion perturbations. Hand-over-hand translocation is a structure-supported
    model, not a directly time-resolved trajectory. C-terminal release/adaptor hypotheses
    remain unresolved. No unwarranted assembly-loss or universal native-essentiality
    inference.
  target_ids:
  - cellstructuremech:mitochondrial_lon_protease_complex
  evidence_ids:
  - septin-record-mitochondrial_lon_protease_complex
  - septin-original-mitochondrial_lon_protease_complex
  - septin-yang2022-xml
  - septin-yang2022-s3-gr3-jpg
  - septin-graph-policy
- assessment_id: septin-mitochondrial_lon_protease_complex-image
  area: representation
  topic: Actual pixels, attribution and license
  outcome: supported
  summary: Maintained Figure1 pixels were inspected and matched fresh source media
    exactly; model and pore-loop panels support the bounded caption, not an in situ
    micrograph. JATS CC BY4.0 and article authors support licensing/attribution. Figure3
    pixels were separately read only for the displayed assay, not as quantitative
    kinetics.
  target_ids:
  - cellstructuremech:mitochondrial_lon_protease_complex
  evidence_ids:
  - septin-record-mitochondrial_lon_protease_complex
  - septin-original-mitochondrial_lon_protease_complex
  - septin-lon-image-pixels
  - septin-yang2022-fig1
  - septin-yang2022-s3-PMC8913295-1-json
  - septin-yang2022-xml
  - septin-yang2022-s3-gr3-jpg
- assessment_id: septin-mitochondrial_lon_protease_complex-verdict
  area: scope
  topic: Current independent verdict
  outcome: supported
  summary: 'pass_with_limitations: supported structure and source-specific function/quantity
    boundaries; no scientific curation finding. Preparation differences, archive conflict,
    static-mechanism inference and source-specific assays remain explicit.'
  target_ids:
  - cellstructuremech:mitochondrial_lon_protease_complex
  evidence_ids:
  - septin-record-mitochondrial_lon_protease_complex
  - septin-original-mitochondrial_lon_protease_complex
  - septin-yang2022-xml
  - septin-stahlberg1999-legacy
  - septin-go
- assessment_id: septin-mitochondrial_multifunctional_assembly-identity
  area: identity
  topic: Distinct MIMAS protein-lipid assembly
  outcome: supported
  summary: Horten2024 establishes an isolatable inner-membrane mega-assembly with
    selected carriers, respiratory biogenesis factors, dehydrogenases and lipid enzymes.
    It is distinct from respirasome, ATP synthase, prohibitin and MICOS. Local identifier
    and parent/part_of distinction are supported; bounded GO searches are not a global
    absence claim.
  target_ids:
  - cellstructuremech:mitochondrial_multifunctional_assembly
  evidence_ids:
  - septin-record-mitochondrial_multifunctional_assembly
  - septin-original-mitochondrial_multifunctional_assembly
  - septin-horten2024-xml
  - septin-review2026-xml
  - septin-go
  - septin-go-search-mimas
  - septin-go-search-multifunctional
- assessment_id: septin-mitochondrial_multifunctional_assembly-membership
  area: grounding
  topic: Five scoped representative components
  outcome: supported
  summary: AAC2/PET9 P18239, RCF1 Q03713, PSD1 P39006, NDE1 P40215 and TAZ1 Q06510
    are reviewed S288C reference identities, not claimed study strains. Horten affinity,
    migration and crosslinking support selected MIMAS pools. Native family labels
    support AAC/RCF1/PSD1/tafazzin; broad NDH2 family does not justify an external-Nde1-specific
    grounding, so label-only status is appropriate.
  target_ids:
  - cellstructuremech:mitochondrial_multifunctional_assembly
  evidence_ids:
  - septin-record-mitochondrial_multifunctional_assembly
  - septin-original-mitochondrial_multifunctional_assembly
  - septin-horten2024-xml
  - septin-protein-P18239
  - septin-protein-Q03713
  - septin-protein-P39006
  - septin-protein-P40215
  - septin-protein-Q06510
  - septin-ipr-IPR002113
  - septin-ipr-IPR050355
  - septin-ipr-IPR033661
  - septin-ipr-IPR000872
  - septin-ipr-IPR045024
- assessment_id: septin-mitochondrial_multifunctional_assembly-source-strain
  area: scope
  topic: Study strains versus examples and localization sources
  outcome: supported
  summary: Horten Methods uses YPH499/W303 derivatives and a Neurospora AAC construct
    in import methods; S288C examples are reference identity only. Native PET9 also
    has peroxisomal localization and Taz1 both membranes; those do not negate the
    experimentally isolated mitochondrial MIMAS fraction. Huh/Sickmann and other cited
    localization sources were checked at complete abstract/native-annotation tier,
    not uninspected body tier.
  target_ids:
  - cellstructuremech:mitochondrial_multifunctional_assembly
  evidence_ids:
  - septin-record-mitochondrial_multifunctional_assembly
  - septin-original-mitochondrial_multifunctional_assembly
  - septin-horten2024-xml
  - septin-tax-4932
  - septin-tax-559292
  - septin-pmid-14562095
  - septin-pmid-14576278
  - septin-pmid-35127709
  - septin-pmid-16880272
  - septin-pmid-16135531
- assessment_id: septin-mitochondrial_multifunctional_assembly-formation
  area: completeness
  topic: Psd1 catalysis, PE and MIMAS integrity
  outcome: supported
  summary: Psd1-S463A can join wild-type MIMAS but fails to rescue the psd1-null assembly
    while active Psd1 does. This supports enzyme-product-dependent integrity, not
    a direct PE binding site, universal lipid concentration or complete formation
    order. Current UNKNOWN component essentiality is not contradicted by the scoped
    perturbation evidence.
  target_ids:
  - cellstructuremech:mitochondrial_multifunctional_assembly
  evidence_ids:
  - septin-record-mitochondrial_multifunctional_assembly
  - septin-original-mitochondrial_multifunctional_assembly
  - septin-horten2024-xml
  - septin-graph-policy
  - septin-protein-P39006
- assessment_id: septin-mitochondrial_multifunctional_assembly-graph
  area: graph
  topic: Bounded PE-dependent causal graph
  outcome: supported
  summary: Psd1 activity produces PE and supports MIMAS integrity under the tested
    yeast preparation; no added mechanistic edges are inferred simply from co-migration.
    Protein abundance control, crd1 comparison and mutant rescue distinguish stability
    from trivial protein loss and lipid-general assertions.
  target_ids:
  - cellstructuremech:mitochondrial_multifunctional_assembly
  evidence_ids:
  - septin-record-mitochondrial_multifunctional_assembly
  - septin-original-mitochondrial_multifunctional_assembly
  - septin-horten2024-xml
  - septin-graph-policy
- assessment_id: septin-mitochondrial_multifunctional_assembly-transient
  area: evidence
  topic: Rcf1 and Cox13 functional limits
  outcome: supported
  summary: Rcf1 R67A loses MIMAS association whereas Q61/71A increases it in rcf1/rcf2
    background. Cox13 import/chase supports transient association, not a mature stoichiometric
    constituent or direct handoff demonstrated in real time. Authors explicitly state
    import is not a quantitative occupancy measure and exact composition/stoichiometry
    remains future work.
  target_ids:
  - cellstructuremech:mitochondrial_multifunctional_assembly
  evidence_ids:
  - septin-record-mitochondrial_multifunctional_assembly
  - septin-original-mitochondrial_multifunctional_assembly
  - septin-horten2024-xml
  - septin-review2026-xml
- assessment_id: septin-mitochondrial_multifunctional_assembly-quantity
  area: quantity
  topic: Apparent size and dataset provenance
  outcome: supported
  summary: MIMAS-A/B approximately3.3/2.5MDa migration peaks are apparent assemblies,
    not exact protein counts. PRIDE PARTIAL dataset and placeholder PMID0 are properly
    distinguished from the correct paper DOI. No raw MS reanalysis or quantitative
    occupancy is claimed.
  target_ids:
  - cellstructuremech:mitochondrial_multifunctional_assembly
  evidence_ids:
  - septin-record-mitochondrial_multifunctional_assembly
  - septin-original-mitochondrial_multifunctional_assembly
  - septin-horten2024-xml
  - septin-pride-PXD047946
- assessment_id: septin-mitochondrial_multifunctional_assembly-source-quality
  area: evidence
  topic: Primary versus secondary and image limits
  outcome: supported
  summary: Horten2024 body is primary; 2026 MIMAS review is secondary. IPR050355 generated
    unchecked prose is excluded as mechanistic support. Current manuscript captions
    were read but MIMAS figure pixels were not viewed in this review; no inherited
    reviewer pixel claim is borrowed. CC BY-NC-ND4.0 does not support an unqualified
    reusable local illustration; none is maintained.
  target_ids:
  - cellstructuremech:mitochondrial_multifunctional_assembly
  evidence_ids:
  - septin-record-mitochondrial_multifunctional_assembly
  - septin-original-mitochondrial_multifunctional_assembly
  - septin-horten2024-xml
  - septin-review2026-xml
  - septin-ipr-IPR050355
- assessment_id: septin-mitochondrial_multifunctional_assembly-verdict
  area: scope
  topic: Current independent verdict
  outcome: supported
  summary: 'pass_with_limitations: coherent stable protein-lipid assembly at the source-defined
    fraction/strain scope. Exact stoichiometry, direct handoff, substrate-streamlining
    and broad component necessity remain unsettled; no confirmed scientific finding.'
  target_ids:
  - cellstructuremech:mitochondrial_multifunctional_assembly
  evidence_ids:
  - septin-record-mitochondrial_multifunctional_assembly
  - septin-original-mitochondrial_multifunctional_assembly
  - septin-horten2024-xml
  - septin-review2026-xml
- assessment_id: septin-mitochondrial_outer_membrane_translocase_complex-identity
  area: identity
  topic: Whole TOM identity and narrower GIP core
  outcome: concern
  summary: GO0005742 whole TOM identity, outer-membrane location and parent remain
    supported. The current GIP EXACT_SYNONYM still disagrees with fresh native GO
    narrow designation; retain original F1 and stable key tom-gip-synonym-scope.
  target_ids:
  - GO:0005742
  evidence_ids:
  - septin-record-mitochondrial_outer_membrane_translocase_complex
  - septin-original-mitochondrial_outer_membrane_translocase_complex
  - septin-go
  - septin-go-0005742-ancestors
  - septin-gene-TOM22
  - septin-gene-TOM40
- assessment_id: septin-mitochondrial_outer_membrane_translocase_complex-protein
  area: grounding
  topic: Reference identities and family boundaries without forced inventory
  outcome: supported
  summary: Current native S288C Tom40/22/20/70/5/6/7 identities and candidate family
    boundaries were inspected. Broad/fungal family choices require scoped later curation,
    but missing optional component/examples is not itself a scientific defect. Empty
    native inventory does not certify complete composition.
  target_ids:
  - GO:0005742
  evidence_ids:
  - septin-record-mitochondrial_outer_membrane_translocase_complex
  - septin-original-mitochondrial_outer_membrane_translocase_complex
  - septin-gene-TOM40
  - septin-gene-TOM22
  - septin-query-retry-TOM20
  - septin-gene-TOM70
  - septin-query-retry-TOM5
  - septin-gene-TOM6
  - septin-gene-TOM7
  - septin-ipr-IPR005686
  - septin-ipr-IPR037930
  - septin-ipr-IPR005683
  - septin-ipr-IPR020951
  - septin-ipr-IPR002056
  - septin-ipr-IPR005687
  - septin-ipr-IPR019603
  - septin-ipr-IPR020266
  - septin-ipr-IPR012621
  - septin-protein-policy
- assessment_id: septin-mitochondrial_outer_membrane_translocase_complex-function
  area: scope
  topic: Import gate and downstream pathway distinction
  outcome: supported
  summary: Chacinska2009 is a genuine secondary review body. TOM mediates outer-membrane
    entry toward all mitochondrial compartments; complete GO0030150 matrix import
    additionally requires TIM23/PAM. The current record explicitly limits its graph
    to topology and entry role and does not assert TOM alone crosses both membranes.
  target_ids:
  - GO:0005742
  evidence_ids:
  - septin-record-mitochondrial_outer_membrane_translocase_complex
  - septin-original-mitochondrial_outer_membrane_translocase_complex
  - septin-chacinska2009-jats
  - septin-go
- assessment_id: septin-mitochondrial_outer_membrane_translocase_complex-formation
  area: completeness
  topic: Assembly evidence versus universal requirement
  outcome: supported
  summary: Secondary review describes Tom22 organization and small-Tom subunit effects,
    but these are not new primary experimental checks or a universal organism-wide
    formation necessity claim. Empty optional composition and explicit unresolved
    family grounding do not warrant manufactured findings.
  target_ids:
  - GO:0005742
  evidence_ids:
  - septin-record-mitochondrial_outer_membrane_translocase_complex
  - septin-original-mitochondrial_outer_membrane_translocase_complex
  - septin-chacinska2009-jats
  - septin-protein-policy
  - septin-curation-policy
- assessment_id: septin-mitochondrial_outer_membrane_translocase_complex-graph
  area: graph
  topic: Nonmechanistic anatomy and functional graph
  outcome: supported
  summary: Current NONMECHANISTIC graph captures whole-complex outer-membrane topology
    and contribution to import. No individual family or detailed TIM23/PAM mechanism
    is falsely added. GIP synonym correction preserves all supported graph meaning.
  target_ids:
  - GO:0005742
  evidence_ids:
  - septin-record-mitochondrial_outer_membrane_translocase_complex
  - septin-original-mitochondrial_outer_membrane_translocase_complex
  - septin-go
  - septin-chacinska2009-jats
  - septin-graph-policy
- assessment_id: septin-mitochondrial_outer_membrane_translocase_complex-taxon
  area: scope
  topic: Qualitative occurrence and source scope
  outcome: supported
  summary: S.cerevisiae evidence supports the canonical mitochondrial setting; Eukaryota
    VARIABLE avoids universal retention in reduced organelles. COMMON is qualitative
    record context rather than an experimentally measured prevalence census.
  target_ids:
  - GO:0005742
  evidence_ids:
  - septin-record-mitochondrial_outer_membrane_translocase_complex
  - septin-original-mitochondrial_outer_membrane_translocase_complex
  - septin-tax-4932
  - septin-tax-2759
  - septin-chacinska2009-jats
- assessment_id: septin-mitochondrial_outer_membrane_translocase_complex-verdict
  area: scope
  topic: Current independent verdict
  outcome: concern
  summary: needs_curation solely for inherited minor GIP synonym scope. Supported
    whole TOM identity, location, import function and current restrained inventory
    remain intact; original source lineage and bounded action preserved.
  target_ids:
  - GO:0005742
  evidence_ids:
  - septin-record-mitochondrial_outer_membrane_translocase_complex
  - septin-original-mitochondrial_outer_membrane_translocase_complex
  - septin-go
  - septin-chacinska2009-jats
- assessment_id: septin-mitochondrial_prohibitin_complex-identity
  area: identity
  topic: Prohibitin repeating heterodimeric complex
  outcome: supported
  summary: Native GO0035632 and Back2002 primary abstract support PHB1/PHB2 repeating
    heterodimeric building blocks in an inner-membrane assembly. No exact universal
    subunit number or atomic experimental structure is asserted in the record.
  target_ids:
  - GO:0035632
  evidence_ids:
  - septin-record-mitochondrial_prohibitin_complex
  - septin-original-mitochondrial_prohibitin_complex
  - septin-go
  - septin-go-0035632-ancestors
  - septin-back2002-abstract
- assessment_id: septin-mitochondrial_prohibitin_complex-protein
  area: grounding
  topic: Prohibitin reference identities and broad family
  outcome: supported
  summary: Fresh native queries identify reviewed S288C PHB1 P40961 and PHB2 P50085.
    IPR000163 is shared prohibitin family, not a verified exact split for each paralogue.
    No empty optional-component or forced-chemical/complex-grounding finding is justified.
  target_ids:
  - GO:0035632
  evidence_ids:
  - septin-record-mitochondrial_prohibitin_complex
  - septin-original-mitochondrial_prohibitin_complex
  - septin-gene-PHB1
  - septin-gene-PHB2
  - septin-ipr-IPR000163
  - septin-protein-policy
- assessment_id: septin-mitochondrial_prohibitin_complex-source-limits
  area: evidence
  topic: Current primary abstract and genuine secondary body
  outcome: supported
  summary: Back2002 complete primary abstract supports crosslink/MS spatial restraints
    and modeled repeating heterodimer building block. Current canonical routes are
    challenge markup, EPXML500, publisher403 and S3version1 not available; no primary
    full-body Methods or image inspection is claimed. Artal2010 genuine review body
    is secondary. Historical successful original access is retained as historical,
    not represented as fresh.
  target_ids:
  - GO:0035632
  evidence_ids:
  - septin-record-mitochondrial_prohibitin_complex
  - septin-original-mitochondrial_prohibitin_complex
  - septin-back2002-abstract
  - septin-back2002-legacy
  - septin-back2002-epmc-fresh
  - septin-back2002-canonical-fresh
  - septin-back2002-publisher-fresh
  - septin-PMC2373692-jats
  - septin-artal2010-xml
- assessment_id: septin-mitochondrial_prohibitin_complex-function
  area: scope
  topic: Organization and condition-sensitive biological function
  outcome: supported
  summary: GO0007005 mitochondrial biogenesis exact synonym and the current organization
    wording are coherent. Secondary review separates yeast growth/aging from animal
    development and context-sensitive lifespan effects; the record does not make a
    universal viability or direction-of-aging claim.
  target_ids:
  - GO:0035632
  evidence_ids:
  - septin-record-mitochondrial_prohibitin_complex
  - septin-original-mitochondrial_prohibitin_complex
  - septin-go
  - septin-artal2010-xml
- assessment_id: septin-mitochondrial_prohibitin_complex-formation
  area: completeness
  topic: Source-limited assembly and necessity
  outcome: supported
  summary: Physical PHB1-PHB2 interactions and repeating building block are supported
    at primary-abstract tier. Detailed perturbation claims described in the review
    are not reclassified as independently inspected primary assays. The record remains
    cautious and no optional family inventory or universal essentiality requirement
    is imposed.
  target_ids:
  - GO:0035632
  evidence_ids:
  - septin-record-mitochondrial_prohibitin_complex
  - septin-original-mitochondrial_prohibitin_complex
  - septin-back2002-abstract
  - septin-artal2010-xml
  - septin-curation-policy
- assessment_id: septin-mitochondrial_prohibitin_complex-graph
  area: graph
  topic: Nonmechanistic topology and organization
  outcome: supported
  summary: The graph restricts itself to complex identity, inner-membrane parthood
    and broad mitochondrial organization. It does not imply exact PHB1/PHB2 family
    groundings, atomistic assembly pathway or fixed stoichiometry.
  target_ids:
  - GO:0035632
  evidence_ids:
  - septin-record-mitochondrial_prohibitin_complex
  - septin-original-mitochondrial_prohibitin_complex
  - septin-go
  - septin-back2002-abstract
  - septin-graph-policy
- assessment_id: septin-mitochondrial_prohibitin_complex-verdict
  area: scope
  topic: Current independent verdict
  outcome: supported
  summary: 'pass_with_limitations: core identity/topology and broad function are supported;
    primary full-body/Methods/pixel access is unavailable now and explicitly limited.
    No scientific finding is established by that access limitation alone.'
  target_ids:
  - GO:0035632
  evidence_ids:
  - septin-record-mitochondrial_prohibitin_complex
  - septin-original-mitochondrial_prohibitin_complex
  - septin-go
  - septin-back2002-abstract
  - septin-artal2010-xml
- assessment_id: current-input-comparison
  area: provenance
  topic: Complete frozen-input comparison and bounded refresh
  outcome: supported
  summary: 3 of ten original target hashes differ from current main. The changed content
    is substantively reassessed in the target-specific assessments; original observations
    remain historical and unchanged. All current target and used context bytes are
    frozen.
  target_ids:
  - cellstructuremech:mic10_subcomplex
  - cellstructuremech:mic60_mic19_complex
  - GO:0061617
  - GO:0140595
  - GO:0000444
  - GO:0042720
  - cellstructuremech:mitochondrial_lon_protease_complex
  - cellstructuremech:mitochondrial_multifunctional_assembly
  - GO:0005742
  - GO:0035632
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
- finding_id: plaque-t3-F1
  issue_key: mim-complex-assembly-snippets-nonverbatim
  category: provenance
  severity: minor
  native_severity: minor
  normalization_reason: Underlying two-subunit composition and source-qualified copy
    range are supported; the bounded correction repairs quotation form and attribution
    without changing the biological model.
  status: open
  certainty: confirmed
  title: Make the new MIM assembly snippets verbatim or move paraphrases to notes
  description: 'The two new assembly edges contain three snippet occurrences: a repeated
    combined Doan import/composition sentence and a combined Vitali sentence. Their
    wording differs from the inspected source passages; the Vitali sentence is absent
    from the complete normalized genuine JATS. Doan access is the retained indexed
    official PDF representation, not a fresh complete terminal PDF. These are supported
    scientific paraphrases presented as quotations. Correct quotation form without
    rejecting multiple Mim1/one-or-two Mim2 background composition or imposing universal
    formation necessity.'
  target_ids:
  - GO:0140595
  field_paths:
  - causal_graphs[0].edges[0].evidence[0].snippet
  - causal_graphs[0].edges[1].evidence[0].snippet
  - causal_graphs[0].edges[1].evidence[1].snippet
  evidence_ids:
  - plaque-record-3
  - plaque-delta-3
  - plaque-policy
  - plaque-doan2020-web-indexed
  - plaque-PMC6010339-jats
  - plaque-mim-peer-challenge
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/mim_complex.yaml
    role: maintained scientific record
  rule_id: snippet is verbatim only; paraphrase belongs in notes
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/3061
- finding_id: plaque-t4-F1
  issue_key: mis12-mind-exact-family-groundings
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground the four represented MIS12/MIND subunit classes
  description: Four existing protein classes remain REVIEWED_LABEL_ONLY. Native whole-family
    definitions and independent member identities now support IPR008685, IPR013218,
    IPR013950 and IPR007128 respectively. This is an actionable class-grounding gap,
    not a claim that the dated earlier search was false.
  target_ids:
  - GO:0000444
  field_paths:
  - components[0].grounding_status
  - components[1].grounding_status
  - components[2].grounding_status
  - components[3].grounding_status
  - discussions[0]
  evidence_ids:
  - plaque-record-4
  - plaque-original-4
  - plaque-policy
  - plaque-schema
  - plaque-ipr-IPR008685
  - plaque-ipr-IPR013218
  - plaque-ipr-IPR013950
  - plaque-ipr-IPR007128
  - plaque-ipr-IPR016851
  - plaque-up-P39731
  - plaque-up-P40568
  - plaque-up-Q12143
  - plaque-up-P47149-retry
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/mis12_mind_type_complex.yaml
    role: maintained scientific record
  rule_id: Exact class grounding and source-specific synonym qualification
  native_severity: minor
  normalization_reason: All four component identities and membership are already correct.
    The localized remedy supplies verified machine-readable class identifiers without
    changing the scientific complex model.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T084808Z-mis12-mind-type-complex-audit
    finding_id: F1
  disposition_reason: Reconfirmed against current unchanged affected fields and fresh
    native authority/member evidence; new hierarchy and component edges do not remedy
    this separate finding.
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/3062
- finding_id: plaque-t4-F2
  issue_key: mis12-mind-synonym-qualifiers
  category: nomenclature
  severity: minor
  status: open
  certainty: confirmed
  title: Preserve the GO synonym scopes
  description: The record attributes four EXACT synonyms to GO0000444, but the current
    native term classifies Mis12 complex as narrow and the expanded Mtw1p and nuclear
    MIS12/MIND phrases as related. Only MIND complex is exact. The labels themselves
    are not rejected; their source-specific qualifiers are overstated.
  target_ids:
  - GO:0000444
  field_paths:
  - synonyms[1].synonym_type
  - synonyms[2].synonym_type
  - synonyms[3].synonym_type
  evidence_ids:
  - plaque-record-4
  - plaque-original-4
  - plaque-go-0000444
  - plaque-policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/mis12_mind_type_complex.yaml
    role: maintained scientific record
  rule_id: Exact class grounding and source-specific synonym qualification
  native_severity: minor
  normalization_reason: This is a bounded authority-qualification mismatch; it does
    not alter the correct primary complex identity, composition or supported recruitment
    biology.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T084808Z-mis12-mind-type-complex-audit
    finding_id: F2
  disposition_reason: Reconfirmed against current unchanged affected fields and fresh
    native authority/member evidence; new hierarchy and component edges do not remedy
    this separate finding.
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/3063
- finding_id: septin-tom-F1
  issue_key: tom-gip-synonym-scope
  category: identity
  severity: minor
  status: open
  certainty: confirmed
  title: Retain GIP as a narrower synonym
  description: The current synonym row types GIP complex as EXACT_SYNONYM and attributes
    it to GO0005742. The native GO response marks GIP as narrow. The Tom22 authority
    independently distinguishes docking Tom20/Tom70 onto the general Tom40 import-pore
    complex, supporting the narrower-core boundary while preserving whole TOM identity.
  target_ids:
  - GO:0005742
  field_paths:
  - synonyms[0].synonym_type
  evidence_ids:
  - septin-record-mitochondrial_outer_membrane_translocase_complex
  - septin-original-mitochondrial_outer_membrane_translocase_complex
  - septin-go
  - septin-gene-TOM22
  - septin-gene-TOM40
  - septin-query-retry-TOM20
  - septin-gene-TOM70
  - septin-chacinska2009-jats
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/mitochondrial_outer_membrane_translocase_complex.yaml
    role: maintained scientific record
  rule_id: Exact synonym and structure-boundary correspondence
  native_severity: minor
  normalization_reason: A bounded synonym-scope correction preserves the supported
    whole-complex identity, location and import function.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T084810Z-mitochondrial-outer-membrane-translocase-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/3064
actions:
- action_id: plaque-t3-A1
  finding_ids:
  - plaque-t3-F1
  target_ids:
  - GO:0140595
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/mim_complex.yaml
    role: maintained scientific record
  description: For all three added snippet occurrences, either copy a short exact
    passage from the inspected cited source or move the supported paraphrase to notes
    and omit snippet. Retain source-qualified composition, coassembly and uncertainty;
    preserve existing dated history.
  acceptance_checks:
  - Every retained snippet exactly matches a cited inspected passage, including wording;
    paraphrase appears only in notes.
  - Doan background copy range is not misrepresented as a direct universal stoichiometry
    measurement; stabilization/coassembly does not imply absolute Mim2 necessity.
  - Primary body/indexed-text access tiers and experimental limits remain explicit;
    native schema and focused evidence checks pass after separately authorized curation.
- action_id: plaque-t4-A1
  finding_ids:
  - plaque-t4-F1
  target_ids:
  - GO:0000444
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/mis12_mind_type_complex.yaml
    role: maintained scientific record
  description: Add the four exact family groundings and update current grounding status/notes
    and the open task. Retain the verified species examples and UNKNOWN essentiality;
    use IPR007128 for the joint Nnf1/PMF1 class. Do not propagate the malformed InterPro
    organism phrase.
  acceptance_checks:
  - The amended field matches the exact native authority scope and preserves independently
    supported scientific identity.
  - Original historical statements are retained as history; current grounding or source
    qualifiers are updated explicitly.
  - Native schema, strict and CURIE checks pass after separately authorized curation.
- action_id: plaque-t4-A2
  finding_ids:
  - plaque-t4-F2
  target_ids:
  - GO:0000444
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/mis12_mind_type_complex.yaml
    role: maintained scientific record
  description: Retain the synonym text and GO source but use NARROW_SYNONYM for Mis12
    complex and RELATED_SYNONYM for the two related phrases; retain EXACT_SYNONYM
    for MIND complex.
  acceptance_checks:
  - The amended field matches the exact native authority scope and preserves independently
    supported scientific identity.
  - Original historical statements are retained as history; current grounding or source
    qualifiers are updated explicitly.
  - Native schema, strict and CURIE checks pass after separately authorized curation.
- action_id: septin-tom-A1
  finding_ids:
  - septin-tom-F1
  target_ids:
  - GO:0005742
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/mitochondrial_outer_membrane_translocase_complex.yaml
    role: maintained scientific record
  description: Change only the GIP synonym scope to NARROW_SYNONYM or supply an explicitly
    scoped alternative supported by a direct source. Preserve the exact whole TOM
    identifier and the other exact synonym.
  acceptance_checks:
  - Recheck the native GO synonym type and retain the pore-core versus whole-complex
    distinction.
  - Pass schema, strict and applicable identifier checks after separately authorized
    curation.
  - Preserve immutable original bundles and dated historical rationale; change only
    separately authorized current synonym scope or append a source-supported clarification.
limitations:
- 'MIC10 subcomplex, Mic60-Mic19 complex and MICOS independent review: Assigned scientific
  coverage is indices0–2, with complete current records and immutable original pairs.
  All three have no inherited scientific findings. One staleMICOS target was substantively
  refreshed; two targets are unchanged. Additional frozen MIM record was read only
  for the separate quotation challenge owned by plaque. No new record-curation finding
  is established for the assigned trio.'
- 'MIC10 subcomplex, Mic60-Mic19 complex and MICOS independent review: All 44 historical
  input occurrences and six original native validate/render commands passed; current
  source/main target hashes verified. Root six current native protein commands cover6
  examples / 6 COVERED nodes (4+2); MICOS has 0 / 0. Empty native checks are not positive
  molecular validation. Root corpus/final successor/CI/queue gates remain separate.'
- 'MIC10 subcomplex, Mic60-Mic19 complex and MICOS independent review: Primary read
  scopes are exactly those in each evidence locator: Rampelt main1883–1888; Friedman
  listed Results/Methods; Tirrell s3/s4/s11; Hessenberger seven named sections; Bock-Bierbaum
  Results/Discussion and specified Methods; Hoppins specified Results/Discussion/Methods.
  Only maintained Figure 3/4 pixels were inspected; other captions are text only.
  No raw data, density maps, movies or separately downloaded supplements were reanalysed.'
- 'MIC10 subcomplex, Mic60-Mic19 complex and MICOS independent review: Harner 2011
  current S3 failed404 and legacy HTTP 200 is reCAPTCHA; its complete indexed abstract
  was read. von der Malsburg 2011, Reinders 2006, Huh 2003 and Rabl 2009 remain indexed
  abstract/native-annotation tier. Pfanner 2014 complete text is nomenclature authority.
  Original historical access limits are not upgraded.'
- 'MIC10 subcomplex, Mic60-Mic19 complex and MICOS independent review: Current five
  JSON UniProt entries plus one complete Mic10 flatfile and six exact gene/taxon/reviewed
  queries were independently inspected; each query has one matching result/no next
  page. Initial503/timeouts/rate limits are retained separately. Native reference
  strain does not identify every experimental strain.'
- 'MIC10 subcomplex, Mic60-Mic19 complex and MICOS independent review: Family candidates
  were checked at current native descriptions/hierarchy; Mic19 DUF1690 remains an
  uncharacterised fungal family, not asserted as exact universal Mic19. Two zero-hitQuickGO
  text searches are bounded query results, not exhaustive ontology absence. No sequence
  alignment or guessed identifier.'
- 'MIC10 subcomplex, Mic60-Mic19 complex and MICOS independent review: All three formal
  expression-only source exclusions are unsupported; fresh complete official catalogue:
  20 organisms / 28 datasets has no matched biological-host dataset. Recombinant E.
  coli and unrelated Sulfolobus are not proxies. No downstream expression-module inference
  is made. Historical source-runner unavailable observation remains Nov 3 00:49Z and
  was not rerun here.'
- 'MIC10 subcomplex, Mic60-Mic19 complex and MICOS independent review: Images equal
  current source downloads bytewise, exact permissions/figure captions inspected.
  No fresh OA metadataMD5 request or original Oct 4 retrieval recertification. Native
  strut/barrier, universal 4:4 stoichiometry, direct cardiolipin site and strain-prevalence
  census remain unresolved.'
- 'MIC10 subcomplex, Mic60-Mic19 complex and MICOS independent review: Bundle defects
  are three formal applicability corrections, one historical access-kind occurrence
  and one stale target refresh. No scientific findings/actions/predecessors are invented,
  and no neighbor/group issue is terminally resolved by inference.'
- 'MIC10 subcomplex, Mic60-Mic19 complex and MICOS independent review: Separate recovery
  search for a damaged PR2396 scratch receipt was written as an isolated audit. It
  is not a biological evidence source for this report and does not mutate any previous
  artifacts.'
- 'MIM, MIS12/MIND and mitochondrial inner membrane peptidase independent review:
  Review is confined to assigned indices3,4,5 at source c9fe63bdff984abad241949c21dab3b13e975d1f;
  other frozen paths were hash-checked, not silently scientifically reviewed. No repository,
  record, Git or GitHub mutation was performed.'
- 'MIM, MIS12/MIND and mitochondrial inner membrane peptidase independent review:
  Doan current direct body routes failed; scientific reading uses complete primary
  abstract plus explicitly retained indexed official PDF excerpts whose crawl predates
  this review. No fresh complete PDF, exhaustive Doan quotation absence or figure-pixel
  claim is made.'
- 'MIM, MIS12/MIND and mitochondrial inner membrane peptidase independent review:
  Dimmer2012 corroboration uses indexed primary-paper text with explicit returned
  scope; no fresh downloaded PDF or independently viewed figure pixels. It supports
  bounded assembly contribution and counterlimits, not universal necessity.'
- 'MIM, MIS12/MIND and mitochondrial inner membrane peptidase independent review:
  Vitali2018/2019, De Wulf and Kline were read only in declared sections; unlisted
  Methods, supplements, figures and papers cited in database annotations are not certified.
  Jan2000 remains complete primary abstract only; Gakh2002 is a secondary review abstract.'
- 'MIM, MIS12/MIND and mitochondrial inner membrane peptidase independent review:
  Five corrected historical access/metadata observations retain original dates and
  hashes and are not fresh retrieval claims. Current access failures and successful
  alternative tiers are distinct.'
- 'MIM, MIS12/MIND and mitochondrial inner membrane peptidase independent review:
  Only the MTW1 fresh bounded gene query succeeded; other fresh query transport failures
  do not certify uniqueness. Exact reviewed accessions and native current identity
  checks independently support the maintained examples.'
- 'MIM, MIS12/MIND and mitochondrial inner membrane peptidase independent review:
  Catalogue absence is limited to all20 current organism rows/28 entries; no natural-host
  matches and no proxy downstream query. Computational expression membership would
  not establish assembly or necessity. Historical runner unavailability is not presented
  as a new invocation.'
- 'MIM, MIS12/MIND and mitochondrial inner membrane peptidase independent review:
  All actual native coverage diagnostics are retained, including two MIS12 partial-example
  class symbols and the external outer-kinetochore actor; neither optional example
  absence nor unknown essentiality alone creates a finding.'
- 'MIM, MIS12/MIND and mitochondrial inner membrane peptidase independent review:
  Original historical hashes and current51 frozen inputs are verified by the current
  original-check receipt. Global corpus gates, issue dedup/publication, final saved-head
  review and CI remain root-owned and are not precertified here.'
- 'MIM, MIS12/MIND and mitochondrial inner membrane peptidase independent review:
  The separately documented loss of an unrelated PR2396 scratch receipt is not used
  as a scientific or validation dependency in this PR2397 report. No claim of byte
  restoration or fully reproducible historical replay is made.'
- 'Mitochondrial Lon, multifunctional assembly, TOM and prohibitin independent review:
  Read-only assigned source review; no maintained record, original bundle, Git or
  GitHub mutation. Root owns global QC, persistence, final head/CI and publication.
  No future gate result is certified.'
- 'Mitochondrial Lon, multifunctional assembly, TOM and prohibitin independent review:
  Back2002 fresh body unavailable after bounded genuine routes; complete abstract,
  native GO and genuine secondary review used with explicit scope. No Back2002 figure
  or Methods verification claimed.'
- 'Mitochondrial Lon, multifunctional assembly, TOM and prohibitin independent review:
  Current pixel assessment is limited to maintained YangFigure1 and fresh YangFigure3.
  MIMAS and other source figure captions were read without current pixels; historical
  reviewer image claims are not inherited as fresh observations.'
- 'Mitochondrial Lon, multifunctional assembly, TOM and prohibitin independent review:
  Native protein verification covers six represented examples and two COVERED nodes
  only; TOM/prohibitin inventories are empty. Identity, localization, structural membership
  and formation necessity remain distinct.'
- 'Mitochondrial Lon, multifunctional assembly, TOM and prohibitin independent review:
  All four positive molecular scopes require source applicability assessment, but
  the complete current official catalogue contains no matching biological host. Historical
  Nov3 runner failure is not a fresh invocation; E.coli recombinant expression is
  not a host substitute.'
- 'Mitochondrial Lon, multifunctional assembly, TOM and prohibitin independent review:
  Broad QuickGO search pages and exact gene queries have stated finite bounds. No
  global term absence, unseen full text, universal taxonomic prevalence, fixed generic
  stoichiometry or optional-inventory defect is inferred.'
- 'Mitochondrial Lon, multifunctional assembly, TOM and prohibitin independent review:
  This report depends only on fresh current PR2397 original checks and intact current
  frozen inputs; the separately documented older auxiliary receipt retention loss
  is not restored or silently replaced.'
- 'Historical retention limitation tracked by #3057: one PR2396 auxiliary validation
  receipt cannot be replayed byte-for-byte after a scratch overwrite. Its genuine
  prior execution and pre-incident hash observations remain evidenced. This review
  does not use that lost receipt or certify complete historical snapshot retention;
  current source snapshots and receipt bindings are reviewed independently.'
notes:
- 'During preparation of this PR, a scratch helper overwrote one external auxiliary
  validation receipt from already-merged PR #2396. Issue #3057 records the exact loss,
  preserved genuine prior execution event and independent pre-incident hash observations.
  The old bytes are not restored; all current PR2397 inputs and checks are independent.
  A guarded current helper verifies its explicit workspace and source and refuses
  output overwrite. No scientific record, saved review or Git object was changed by
  the incident.'
- 'All twenty native protein commands passed with eighteen represented examples and
  fifteen typed protein nodes: twelve COVERED, two PARTIAL_EXAMPLES in MIS12/MIND
  and one UNANCHORED_WITH_UNIPROT outer-kinetochore actor. These diagnostic classes
  and optional cross-species example limits are retained without treating them as
  automatic scientific defects.'
- 'The seven original formal expression-only exclusions and three omitted applicability
  assessments are corrected using the actual current catalogue scope. Eleven original
  context-only evidence occurrences are reclassified: ten failed-access diagnostics
  as validation and one Crossref metadata item as database. Original timestamps and
  access limits are preserved.'
- 'Four confirmed minor record-curation findings remain open: MIM assembly snippets,
  two MIS12/MIND family/synonym findings, and inherited TOM GIP synonym scope. The
  three inherited findings retain their exact predecessor occurrence identifiers;
  the new MIM finding has no invented predecessor.'
- All 51 frozen inputs comprise ten current targets, twenty original review files,
  seventeen repository context files and four maintained images. Three independently
  authored reports retain their actual reading tiers, bounded searches, retrieval
  receipts and image-inspection limits.
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T084805Z-mic10-subcomplex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T084806Z-mic60-mic19-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T084806Z-micos-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T084807Z-mim-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T084808Z-mis12-mind-type-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T084808Z-mitochondrial-inner-membrane-peptidase-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T084809Z-mitochondrial-lon-protease-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T084810Z-mitochondrial-multifunctional-assembly-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T084810Z-mitochondrial-outer-membrane-translocase-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T084811Z-mitochondrial-prohibitin-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
links:
- https://github.com/CultureBotAI/CellStructureMech/pull/2397
- https://github.com/CultureBotAI/CellStructureMech/issues/2514
- https://github.com/CultureBotAI/CellStructureMech/issues/3057
- https://github.com/CultureBotAI/CellStructureMech/issues/3058
- https://github.com/CultureBotAI/CellStructureMech/issues/3059
- https://github.com/CultureBotAI/CellStructureMech/issues/3060
- https://github.com/CultureBotAI/CellStructureMech/issues/3061
- https://github.com/CultureBotAI/CellStructureMech/issues/3062
- https://github.com/CultureBotAI/CellStructureMech/issues/3063
- https://github.com/CultureBotAI/CellStructureMech/issues/3064
```
