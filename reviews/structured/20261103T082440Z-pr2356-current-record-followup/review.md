# PR 2356: current-input review of ten records and adversarial follow-up

- Review: 20261103T082440Z-pr2356-current-record-followup
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-11-03T08:10:07.354680Z
- Finished UTC: 2026-11-03T08:24:40Z
- Reviewer: Codex root synthesis with three independent read-only adversarial reviewers (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Current-input reassessment of all ten inclusion records in PR2356. The stale IPOD and MitoStore reviews are substantively refreshed against their added self-node groundings. Independent source reviews reassess the original scientific finding and correct nine structured-source applicability defects without editing records.

## Scope And Provenance

Exact ten-record PR cohort reassessed against current main 94afdcf235c84e085e340e1a6c1dc4ab69449b03. Changed inputs are substantively reassessed. Scientific records remain unchanged.

Selection: Complete cohort of ten maintained records reviewed in original PR head d23378c3e8d1f361150365303a3eb4595893a0fa.
Coverage: full; 10 reviewed / 10 in the declared population.
Source: working_tree at Git base 7362758aca3756f5979304474ceb02a18f1a6ce6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:age_associated_protein_deposit | data/structures/inclusion/age_associated_protein_deposit.yaml | maintained | age-associated protein deposit |
| cellstructuremech:bacterial_aggresome | data/structures/inclusion/bacterial_aggresome.yaml | maintained | bacterial aggresome |
| GO:0033172 | data/structures/inclusion/gas_vesicle_shell.yaml | maintained | gas vesicle shell |
| cellstructuremech:insoluble_protein_deposit | data/structures/inclusion/insoluble_protein_deposit.yaml | maintained | insoluble protein deposit |
| cellstructuremech:intranuclear_quality_control_compartment | data/structures/inclusion/intranuclear_quality_control_compartment.yaml | maintained | intranuclear quality control compartment |
| cellstructuremech:juxtanuclear_quality_control_compartment | data/structures/inclusion/juxtanuclear_quality_control_compartment.yaml | maintained | juxtanuclear quality control compartment |
| cellstructuremech:mitostore | data/structures/inclusion/mitostore.yaml | maintained | MitoStore |
| GO:0034430 | data/structures/inclusion/monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer.yaml | maintained | monolayer-surrounded lipid storage body outer lipid monolayer |
| GO:0140602 | data/structures/inclusion/nucleolar_peripheral_inclusion_body.yaml | maintained | nucleolar peripheral inclusion body |
| cellstructuremech:parasporal_crystal | data/structures/inclusion/parasporal_crystal.yaml | maintained | parasporal crystal |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full native QC | passed | True | cellstructuremech:age_associated_protein_deposit, cellstructuremech:bacterial_aggresome, GO:0033172, cellstructuremech:insoluble_protein_deposit, cellstructuremech:intranuclear_quality_control_compartment, cellstructuremech:juxtanuclear_quality_control_compartment, cellstructuremech:mitostore, GO:0034430, GO:0140602, cellstructuremech:parasporal_crystal | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| Native label correspondence | passed | True | cellstructuremech:age_associated_protein_deposit, cellstructuremech:bacterial_aggresome, GO:0033172, cellstructuremech:insoluble_protein_deposit, cellstructuremech:intranuclear_quality_control_compartment, cellstructuremech:juxtanuclear_quality_control_compartment, cellstructuremech:mitostore, GO:0034430, GO:0140602, cellstructuremech:parasporal_crystal | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| TraitMech references | passed | True | cellstructuremech:age_associated_protein_deposit, cellstructuremech:bacterial_aggresome, GO:0033172, cellstructuremech:insoluble_protein_deposit, cellstructuremech:intranuclear_quality_control_compartment, cellstructuremech:juxtanuclear_quality_control_compartment, cellstructuremech:mitostore, GO:0034430, GO:0140602, cellstructuremech:parasporal_crystal | Native TraitMech link check passed. |
| Pinned governed files | passed | True | cellstructuremech:age_associated_protein_deposit, cellstructuremech:bacterial_aggresome, GO:0033172, cellstructuremech:insoluble_protein_deposit, cellstructuremech:intranuclear_quality_control_compartment, cellstructuremech:juxtanuclear_quality_control_compartment, cellstructuremech:mitostore, GO:0034430, GO:0140602, cellstructuremech:parasporal_crystal | Pinned governed files match; native vendored check passed. |
| Native identifier resolver | passed | True | cellstructuremech:age_associated_protein_deposit, cellstructuremech:bacterial_aggresome, GO:0033172, cellstructuremech:insoluble_protein_deposit, cellstructuremech:intranuclear_quality_control_compartment, cellstructuremech:juxtanuclear_quality_control_compartment, cellstructuremech:mitostore, GO:0034430, GO:0140602, cellstructuremech:parasporal_crystal | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| validate cellstructuremech:age_associated_protein_deposit | passed | True | cellstructuremech:age_associated_protein_deposit | Documented focused command passed. |
| validate-strict cellstructuremech:age_associated_protein_deposit | passed | True | cellstructuremech:age_associated_protein_deposit | Documented focused command passed. |
| validate cellstructuremech:bacterial_aggresome | passed | True | cellstructuremech:bacterial_aggresome | Documented focused command passed. |
| validate-strict cellstructuremech:bacterial_aggresome | passed | True | cellstructuremech:bacterial_aggresome | Documented focused command passed. |
| validate GO:0033172 | passed | True | GO:0033172 | Documented focused command passed. |
| validate-strict GO:0033172 | passed | True | GO:0033172 | Documented focused command passed. |
| validate cellstructuremech:insoluble_protein_deposit | passed | True | cellstructuremech:insoluble_protein_deposit | Documented focused command passed. |
| validate-strict cellstructuremech:insoluble_protein_deposit | passed | True | cellstructuremech:insoluble_protein_deposit | Documented focused command passed. |
| validate cellstructuremech:intranuclear_quality_control_compartment | passed | True | cellstructuremech:intranuclear_quality_control_compartment | Documented focused command passed. |
| validate-strict cellstructuremech:intranuclear_quality_control_compartment | passed | True | cellstructuremech:intranuclear_quality_control_compartment | Documented focused command passed. |
| validate cellstructuremech:juxtanuclear_quality_control_compartment | passed | True | cellstructuremech:juxtanuclear_quality_control_compartment | Documented focused command passed. |
| validate-strict cellstructuremech:juxtanuclear_quality_control_compartment | passed | True | cellstructuremech:juxtanuclear_quality_control_compartment | Documented focused command passed. |
| validate cellstructuremech:mitostore | passed | True | cellstructuremech:mitostore | Documented focused command passed. |
| validate-strict cellstructuremech:mitostore | passed | True | cellstructuremech:mitostore | Documented focused command passed. |
| validate GO:0034430 | passed | True | GO:0034430 | Documented focused command passed. |
| validate-strict GO:0034430 | passed | True | GO:0034430 | Documented focused command passed. |
| validate GO:0140602 | passed | True | GO:0140602 | Documented focused command passed. |
| validate-strict GO:0140602 | passed | True | GO:0140602 | Documented focused command passed. |
| validate cellstructuremech:parasporal_crystal | passed | True | cellstructuremech:parasporal_crystal | Documented focused command passed. |
| validate-strict cellstructuremech:parasporal_crystal | passed | True | cellstructuremech:parasporal_crystal | Documented focused command passed. |
| Supplemental bounded PMID authority checks | passed | True | cellstructuremech:age_associated_protein_deposit, cellstructuremech:bacterial_aggresome, GO:0033172, cellstructuremech:insoluble_protein_deposit, cellstructuremech:intranuclear_quality_control_compartment, cellstructuremech:juxtanuclear_quality_control_compartment, cellstructuremech:mitostore, GO:0034430, GO:0140602, cellstructuremech:parasporal_crystal | 909 PMIDs all OK in bounded native requests; full-command limitations remain separate. |
| Official structured-source applicability and covered-dataset cross-checks | passed | False | cellstructuremech:age_associated_protein_deposit, cellstructuremech:bacterial_aggresome, GO:0033172, cellstructuremech:insoluble_protein_deposit, cellstructuremech:intranuclear_quality_control_compartment, cellstructuremech:juxtanuclear_quality_control_compartment, cellstructuremech:mitostore, GO:0034430, GO:0140602, cellstructuremech:parasporal_crystal | Applicability was assessed against the official catalogue and actual molecular assertions. The six yeast-related targets have no matching Saccharomyces or Schizosaccharomyces catalogue coverage. Bacterial aggresome checks use bounded MG1655 gene/module data and retain six positive module contexts and five all-false cases as context only, not component membership, causal evidence or biological absence. Gas-shell and parasporal scopes retain organism-specific catalogue limits. The outer lipid monolayer has material/topology-only scope without an identified gene/locus/protein or molecular pathway to query. Nine original reviews require correction: three unsupported expression-only exemptions and six omissions. Historical native-runner unavailability is separate, with no fresh invocation or success claimed. |
| Independent claim-level source review | passed | True | cellstructuremech:age_associated_protein_deposit, cellstructuremech:bacterial_aggresome, GO:0033172, cellstructuremech:insoluble_protein_deposit, cellstructuremech:intranuclear_quality_control_compartment, cellstructuremech:juxtanuclear_quality_control_compartment, cellstructuremech:mitostore, GO:0034430, GO:0140602, cellstructuremech:parasporal_crystal | Three read-only reviewers covered the complete ten-record cohort, including changed inputs, with explicit scientific findings and source-access limits. Final artifact/head acceptance occurs after saving. |
| Retained historical adapter runner availability | unavailable | False | cellstructuremech:age_associated_protein_deposit, cellstructuremech:bacterial_aggresome, GO:0033172, cellstructuremech:insoluble_protein_deposit, cellstructuremech:intranuclear_quality_control_compartment, cellstructuremech:juxtanuclear_quality_control_compartment, cellstructuremech:mitostore, GO:0140602, cellstructuremech:parasporal_crystal | Historical 00:49Z invocation unavailable due to OS access restriction. Official catalogue source fallback was inspected separately; no current invocation or successful adapter execution is claimed. The actual historical exit code 1 is retained in the evidence receipt, since the native unavailable-check model has no execution exit-code field. |
| Native age-associated protein deposit UniProt verify check | passed | True | cellstructuremech:age_associated_protein_deposit | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories or zero molecular graph nodes do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native age-associated protein deposit UniProt causal check | passed | True | cellstructuremech:age_associated_protein_deposit | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories or zero molecular graph nodes do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native bacterial aggresome UniProt verify check | passed | True | cellstructuremech:bacterial_aggresome | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories or zero molecular graph nodes do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native bacterial aggresome UniProt causal check | passed | True | cellstructuremech:bacterial_aggresome | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories or zero molecular graph nodes do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native gas vesicle shell UniProt verify check | passed | True | GO:0033172 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories or zero molecular graph nodes do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native gas vesicle shell UniProt causal check | passed | True | GO:0033172 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories or zero molecular graph nodes do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native insoluble protein deposit UniProt verify check | passed | True | cellstructuremech:insoluble_protein_deposit | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories or zero molecular graph nodes do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native insoluble protein deposit UniProt causal check | passed | True | cellstructuremech:insoluble_protein_deposit | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories or zero molecular graph nodes do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native intranuclear quality control compartment UniProt verify check | passed | True | cellstructuremech:intranuclear_quality_control_compartment | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories or zero molecular graph nodes do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native intranuclear quality control compartment UniProt causal check | passed | True | cellstructuremech:intranuclear_quality_control_compartment | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories or zero molecular graph nodes do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native juxtanuclear quality control compartment UniProt verify check | passed | True | cellstructuremech:juxtanuclear_quality_control_compartment | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories or zero molecular graph nodes do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native juxtanuclear quality control compartment UniProt causal check | passed | True | cellstructuremech:juxtanuclear_quality_control_compartment | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories or zero molecular graph nodes do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native MitoStore UniProt verify check | passed | True | cellstructuremech:mitostore | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories or zero molecular graph nodes do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native MitoStore UniProt causal check | passed | True | cellstructuremech:mitostore | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories or zero molecular graph nodes do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native monolayer-surrounded lipid storage body outer lipid monolayer UniProt verify check | passed | True | GO:0034430 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories or zero molecular graph nodes do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native monolayer-surrounded lipid storage body outer lipid monolayer UniProt causal check | passed | True | GO:0034430 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories or zero molecular graph nodes do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native nucleolar peripheral inclusion body UniProt verify check | passed | True | GO:0140602 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories or zero molecular graph nodes do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native nucleolar peripheral inclusion body UniProt causal check | passed | True | GO:0140602 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories or zero molecular graph nodes do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native parasporal crystal UniProt verify check | passed | True | cellstructuremech:parasporal_crystal | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories or zero molecular graph nodes do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native parasporal crystal UniProt causal check | passed | True | cellstructuremech:parasporal_crystal | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories or zero molecular graph nodes do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |

## Scientific And Domain Assessments

### Nuclear INQ identity and local mint

identity: supported. Targets: cellstructuremech:intranuclear_quality_control_compartment.

Nuclear-envelope-resolved primary evidence distinguishes INQ from cytoplasmic JUNQ. GO0016604/0016234 are appropriate broader parents and GO0005634 parthood; GO0097165 is not substituted. Exact OLS and bounded QuickGO queries did not return an exact INQ term.

### Heterogeneous cargo and Cmr1 residency

scope: supported. Targets: cellstructuremech:intranuclear_quality_control_compartment.

Variable cargo is not a fixed complex. Gallina Fig3 and Mrc1 Results support Cmr1 as a stable conditionally recruited marker, not necessarily misfolded substrate, universal scaffold or universally required resident. The DISPENSABLE label is bounded to Mrc1-focus formation.

### Btn2 necessity and engineered rescue

evidence: supported. Targets: cellstructuremech:intranuclear_quality_control_compartment.

Miller Fig6/7 support nuclear deposition, retained import when deposition fails, Btn2 enrichment and engineered Hsp42-NLS substitution. CONDITIONAL requirement is justified; native Hsp42 residence or universal essentiality is not inferred.

### Hsp104 associated machinery

evidence: supported. Targets: cellstructuremech:intranuclear_quality_control_compartment.

Miller Fig2 directly establishes nuclear Hsp104-marked deposits; main Results describe guanidinium-sensitive dissolution. Supplemental S6 pixels remain uninspected, as disclosed in the record; associated machinery and UNKNOWN assembly necessity are proportionate.

### Stress and marker-specific assembly edges

graph: supported. Targets: cellstructuremech:intranuclear_quality_control_compartment.

All six assembly edges retain distinct NLS-LuciTs heat, Btn2 deletion/rescue and MMS/Cmr1 readouts. Gallina residual Cmr1-foci counts justify reduces, not universal loss; the Hsp42 genotoxic-stress result is not exported to every reporter assay.

### Convergence and conditional clearance

graph: supported. Targets: cellstructuremech:intranuclear_quality_control_compartment.

Sontag S3/S6-S8 support all six graph edges: distinct inclusions converge across the envelope; NVJ and Vps4 perturbations impair reporter clearance; CHM7 affects convergence in a subset. Molecular budding is a model and vacuolar routing is conditional.

### Cargo-dependent consequences

scope: supported. Targets: cellstructuremech:intranuclear_quality_control_compartment.

Miller reporter degradation persists without deposition, whereas Gallina reports Btn2-dependent Mrc1 turnover and Sontag shows reporter vacuolar clearance. The record preserves these assay differences and avoids a universal protective or degradation requirement.

### Experimental species and reference strain

scope: supported. Targets: cellstructuremech:intranuclear_quality_control_compartment.

Gallina methods distinguish RAD5 W303 defaults from S288C libraries/exceptions. Reviewed UniProt S288C examples remain reference sequences, not assignments of every experiment or image.

### Exact protein families versus domains

grounding: supported. Targets: cellstructuremech:intranuclear_quality_control_compartment.

P53286 has only BTN2-like N-terminal domain IPR062150; P31539 has broader ClpA/B families; neither is overgrounded. Q12510 belongs to exact IPR050853 family. Native reviewed exact-gene queries support all three protein examples without borrowing generated mechanism text.

### Gallina Fig3 composite

evidence: supported. Targets: cellstructuremech:intranuclear_quality_control_compartment.

Actual pixels show nuclear Cmr1/VHL overlap versus cytoplasmic VHL, partial Cct6 overlap and separate screen/blot panels. Caption scale2um, mixed assay context and whole-composite limitation agree with Fig3; exact local media MD5 and JATS CC BY4.0 match.

### Cytoplasmic JUNQ boundary

identity: supported. Targets: cellstructuremech:juxtanuclear_quality_control_compartment.

Modern nuclear-envelope-resolved imaging supports cytoplasmic perinuclear JUNQ and congregation of Q-bodies. GO0016234 parent/GO0005737 parthood are appropriate; bounded exact OLS fullname/acronym queries support retaining the local mint without global absence claims.

### Variable cargo and associated machinery

evidence: supported. Targets: cellstructuremech:juxtanuclear_quality_control_compartment.

Sontag correlated Hsp104 imaging supports cytoplasmic association. Kaganovich proteasome association remains explicitly historical and generic GO0000502, not invariant26S composition or universal assembly necessity. Cargo is variable and reporter-defined.

### Q-body and sequestrase sorting

graph: supported. Targets: cellstructuremech:juxtanuclear_quality_control_compartment.

All seven sorting edges agree with Sontag and Rolli: Q-bodies congregate; Ssa1/Ssa2 double deletion shifts to static peripheral deposits; Btn2 deletion shifts localization; Hsp42 deletion reduces peripheral foci without abolishing perinuclear deposits. Peripheral puncta are not all assumed IPOD.

### Formation versus convergence

graph: supported. Targets: cellstructuremech:juxtanuclear_quality_control_compartment.

Sontag nuclear-pore clustering and CHM7/VPS23/VPS34/VPS15 perturbations support the qualified positioning graph. No direct physical tether or obligatory formation role is inferred. Rolli expression-limited Vps15/34 observations are not treated as contradictory mechanism evidence.

### JUNQ reporter clearance

graph: supported. Targets: cellstructuremech:juxtanuclear_quality_control_compartment.

Sontag NVJ/Vps4, cytoplasmic Keima and combined pep4/PMSF results and Rolli Atg1/Atg8 results support the clearance edges. NES-Keima fields are sampled, Fig8 nuclear extrusion is not assigned to JUNQ, and proteasome contributions remain assay dependent.

### Historical recoverable fluorescence pool

scope: supported. Targets: cellstructuremech:juxtanuclear_quality_control_compartment.

Kaganovich S6 observes diffuse Ubc9Ts fluorescence recovery after cooling and Hsp104/guanidine sensitivity. Record wording correctly avoids direct catalytic recovery, universal client refolding and complete retrospective reassignment of old JUNQ to modern cytoplasmic identity.

### Reviewed Hsp104 example and broad family limits

grounding: supported. Targets: cellstructuremech:juxtanuclear_quality_control_compartment.

Reviewed P31539 is S288C HSP104 and its complete11-match integrated set includes broader ClpA/B families, not an exact Hsp104-type identity. Reference accession does not substitute for the experimental BY4741 strain.

### BY4741 experiment versus S288C reference

scope: supported. Targets: cellstructuremech:juxtanuclear_quality_control_compartment.

Rolli Methods Table2 explicitly identifies BY4741 and derived mutants; native taxonomy resolves1247190. The 2023 species-level example does not invent a strain assignment from an unread supplemental table.

### Rolli Fig2 pixel and caption scope

evidence: supported. Targets: cellstructuremech:juxtanuclear_quality_control_compartment.

Inspected multi-panel pixels show WT and mutant spatial comparisons, peripheral double-mutant/HTT comparator photobleaching and separate blots. D-E are not positive WT JUNQ. Scale1um, nuclear-dye panel discrepancy and mitochondrial-method timing limitation are retained; MD5 and exact CC BY4.0 match.

### GO0140602 and heat/starvation scope

identity: supported. Targets: GO:0140602.

Exact GO0140602 defines NuR peripheral inclusion; parent nuclear inclusion and nuclear parthood fit. Gallardo establishes acute-heat rings; Hiraoka Fig3 supports peripheral starvation-associated redistribution without proving an identical heat mechanism.

### Selective recruitment

scope: supported. Targets: GO:0140602.

Gallardo Figures1-2 distinguish recruited nuclear factors from unaffected pore proteins and central Gar2 material. Nup85/Mex67 are measured examples, not a full NPC or active RNA-export complex at NuRs.

### Chaperone residency and Mas5 requirement

evidence: supported. Targets: GO:0140602.

Boronat Fig7 supports Ssa1/Ssa2/Mas5/Hsp104 recruitment and Mas5-dependent fission-yeast reporter rings. Separate single-label images are not simultaneous colocalization; family-wide necessity and transfer to budding yeast are excluded.

### Heat and preconditioning

graph: supported. Targets: GO:0140602.

Acute heat induces the tested rings; Mas5 loss blocks the specified reporters. Gallardo main text reports residual Ssa2 after preconditioning, supporting suppresses rather than absolute prevention. Supplements remain text-reported, not independently imaged.

### Clearance and necessity

graph: supported. Targets: GO:0140602.

Gallardo Figures3-4 support recovery, delayed clearance after Hsp104 loss and repressed purg1-hsf1. Hsp104 is dispensable for assembly; Hsf1 regulation is not direct physical inclusion membership.

### Reversible sequestration versus protection model

scope: supported. Targets: GO:0140602.

Reduced Nup85/Mex67 mobility and recovery support sequestration. General shutdown/protection and regrowth correlations remain interpretations rather than an isolated NuR-only survival pathway.

### Species and preparation boundaries

scope: supported. Targets: GO:0140602.

S.pombe acute heat is separate from Boronat budding-yeast W303/BY4741 tests; only W303 is concentrated50-fold. Native972h- protein-reference taxon does not fix every mutant genotype.

### Six reviewed sequence examples

grounding: supported. Targets: GO:0140602.

Q9UUE5/nup85, Q9Y8G3/mex67, Q10265/ssa1, O59855/ssa2, O74752/mas5 and O94641/hsp104 each resolve as reviewed S.pombe284812 examples; exact reviewed gene/taxon searches return the declared accession. Identity alone does not support residence.

### Family identities and current transport limitation

grounding: supported. Targets: GO:0140602.

Integrated lists through next=null support Nup85 IPR011502, Mex67 IPR030217, both Ssa IPR013126 and Mas5 IPR044713. Direct Hsp70-family endpoint429 is disclosed; successful exact-protein match metadata independently verifies its name/type. Hsp104 broad ClpA/B hits are not adopted as exact identity.

### Boronat Fig7 mixed-species composite

evidence: supported. Targets: GO:0140602.

Pixels show S.pombe and budding-yeast reporter panels, separate chaperone localizations, a Mas5 deletion control and schematic. Figure caption scale5um and15min42C agree; taxon4896 is scoped to panelb/lefta and W303 concentration is retained. Exact media MD5 and CC BY4.0 match.

### Original artifact and current protein gates

schema: supported. Targets: cellstructuremech:intranuclear_quality_control_compartment.

Original native validation and exact render pass; all historical source input hashes match. Current root-run verify/causal receipts independently checked. No scientific finding occurred in the original; no historical curation closure is claimed.

### Current structured-source applicability

provenance: supported. Targets: cellstructuremech:intranuclear_quality_control_compartment.

Named proteins and stress-response perturbations trigger coverage assessment. Fresh complete catalogue lacks both represented yeast genera, so downstream organism-matched gene/module queries are not applicable. Historical runner failure remains separate; this is a source-fallback check, not a fresh runner success or biological negative result.

### Original artifact and current protein gates

schema: supported. Targets: cellstructuremech:juxtanuclear_quality_control_compartment.

Original native validation and exact render pass; all historical source input hashes match. Current root-run verify/causal receipts independently checked. No scientific finding occurred in the original; no historical curation closure is claimed.

### Current structured-source applicability

provenance: supported. Targets: cellstructuremech:juxtanuclear_quality_control_compartment.

Named proteins and stress-response perturbations trigger coverage assessment. Fresh complete catalogue lacks both represented yeast genera, so downstream organism-matched gene/module queries are not applicable. Historical runner failure remains separate; this is a source-fallback check, not a fresh runner success or biological negative result.

### Original artifact and current protein gates

schema: supported. Targets: GO:0140602.

Original native validation and exact render pass; all historical source input hashes match. Current root-run verify/causal receipts independently checked. No scientific finding occurred in the original; no historical curation closure is claimed.

### Current structured-source applicability

provenance: supported. Targets: GO:0140602.

Named proteins and stress-response perturbations trigger coverage assessment. Fresh complete catalogue lacks both represented yeast genera, so downstream organism-matched gene/module queries are not applicable. Historical runner failure remains separate; this is a source-fallback check, not a fresh runner success or biological negative result.

### Local identity and spatial boundary

identity: supported. Targets: cellstructuremech:age_associated_protein_deposit.

INCLUSION/INCLUSION_BODY with local identity and broader GO inclusion-body parent is coherent. Agepod/APOD nomenclature is bounded. ER association does not justify exclusive cytoplasmic parthood because the 2017 source observed an intranuclear subset.

### Source strains and occurrence

scope: supported. Targets: cellstructuremech:age_associated_protein_deposit.

Canonical species4932, explicit S288C/W303 2015 context and BY4741 2025 context are distinguished from seven reviewed S288C reference proteins. Conditional aging occurrence does not imply a structure in every young cell or every yeast lineage.

### Protein identities and family coverage

grounding: supported. Targets: cellstructuremech:age_associated_protein_deposit.

Seven examples resolve to HSP42/HSP26/HSP104/SSA1/SSA2/YDJ1/SUP35. Declared IPR031107/013126/003285 families cover their examples; broad ClpA/B and DnaJ family matches are retained as broader alternatives, not fabricated exact Hsp104/Ydj1-specific groundings.

### Formation necessity versus associated cargo

evidence: supported. Targets: cellstructuremech:age_associated_protein_deposit.

Hsp42 formation dependence does not confer the same requirement on Hsp26. Hsp104 is dispensable for deposit formation under tested conditions; Hsp70 family-wide necessity remains UNKNOWN despite separate SSA1/SSA2 effects. Ydj1 enrichment is uncommon and context-dependent; Sup35 association is prion-state-dependent cargo, not obligatory initiation.

### Chaperone and fusion graph direction

graph: supported. Targets: cellstructuremech:age_associated_protein_deposit.

The graph correctly distinguishes HSP42 loss/OE and HSP104 loss/OE directions, separate SSA1/SSA2 mutations, mating deposit merger and PRM3 perturbation of ER/nuclear fusion. Perturbations are experimental factors, not invented resident complexes.

### Lineage and precursor confinement graph

graph: supported. Targets: cellstructuremech:age_associated_protein_deposit.

BUD1/SUR2/BUD6 and YDJ1-C406S effects distinguish new daughter deposit formation from transfer of pre-existing deposits. Bud6 actin confounding and preserved mature-deposit retention/ER association after C406S are explicit. FCS/FLIP and epistasis support a proposed confinement model without identifying direct clients.

### TOR and disappearance graph scope

graph: supported. Targets: cellstructuremech:age_associated_protein_deposit.

NPR3/TCO89 aging effects are separated from acute pro3-1 screening. Young rapamycin/cycloheximide foci loss and old-cell resistance are source-supported but not equated to direct proteolysis. The internal source cycloheximide-dose discrepancy remains explicit.

### Figure and evidence provenance

provenance: supported. Targets: cellstructuremech:age_associated_protein_deposit.

Tracked Figure6 pixels/caption/CC BY attribution agree with the fresh primary package. The 2018 review is limited to nomenclature; quantitative figure annotations do not establish universal prevalence or composition.

### IPOD identity, location and neighboring compartments

identity: supported. Targets: cellstructuremech:insoluble_protein_deposit.

Local inclusion identity, IPOD acronym, cytoplasmic parthood and broader GO inclusion parent are appropriate. Perivacuolar IPOD remains distinct from JUNQ/INQ and adjacent PAS; an ontology name search is bounded, not universal absence proof.

### Cargo versus disaggregase component

grounding: supported. Targets: cellstructuremech:insoluble_protein_deposit.

Heterogeneous aggregate cargo remains label-only OTHER and engineered PrD-GFP is not misrepresented as a universal full-length native subunit. Hsp104P31539 resolves; broad ClpA/B entries are not exact Hsp104-specific groundings. UNKNOWN formation necessity is compatible with postformation inhibition and persistence.

### Species and experimental strains

scope: supported. Targets: cellstructuremech:insoluble_protein_deposit.

Yeast species4932 is supported by74D-694-derived recruitment/oxidative-stress assays; S288C559292 is a reference-protein identity, not an asserted experimental background for those assays.

### Recruitment versus structural maintenance

graph: supported. Targets: cellstructuremech:insoluble_protein_deposit.

Myo2/tropomyosin/Sec18 depletion and recovery support recruitment/coalescence, while preformed deposits persist after depletion. Proposed vesicular/tethering transport is distinguished from proof of resident transport-factor components or direct fusion of a particular vesicle.

### Cargo release and downstream turnover

graph: supported. Targets: cellstructuremech:insoluble_protein_deposit.

Guanidinium inhibition after deposit formation and MG132 experiments support Hsp104-dependent extraction and a partial proteasomal contribution. The record does not claim complete bulk autophagy, exclusive proteasomal disposal or universal irreversible storage. The2008Ubc9ts recovery assay and2016PrD-GFP slow turnover assay are distinct.

### Prion-formation counterexample

evidence: supported. Targets: cellstructuremech:insoluble_protein_deposit.

ABP1-deletion behavior is explicitly restricted to0.8mM peroxide/one-hour and wild-type versus btn2 hsp42 genetic contexts. This supports the discussion against universal IPOD necessity without inventing universal IPOD independence.

### Tracked recruitment figure provenance

provenance: supported. Targets: cellstructuremech:insoluble_protein_deposit.

Figure3A–F pixels/caption/scale/CC BY attribution agree with fresh package bytes. No original time-lapse movie or raw quantification was reanalyzed.

### MitoStore identity and spatial distinction

identity: supported. Targets: cellstructuremech:mitostore.

Local INCLUSION_BODY identity denotes cytosolic precursor granules associated with the mitochondrial surface, not matrix granules or a membrane-enclosed organelle. Neither broad protein aggregate center nor heat-induced Tom70 aggregates are asserted as exact synonyms.

### Components, identities and conditional necessity

grounding: supported. Targets: cellstructuremech:mitostore.

HSP42Q12329/HSP26P15992 share valid small-HSP familyIPR031107; HSP104P31539 remains exact with broader family unassigned. Hsp26 co-purification does not establish necessity or direct localization. Separate HSP42/HSP104 deletions support the tested Aim17 formation requirement, not a universal fixed coat or full native inventory.

### Yeast strain and conditional occurrence

scope: supported. Targets: cellstructuremech:mitostore.

YPH499-derived experiments and canonical species4932 are separated from S288C reference-protein identities. Lactate-growth basal granules, clogger induction and glucose/stationary-phase context are not generalized to constitutive occurrence in all yeast.

### Precursor assembly graph

graph: supported. Targets: cellstructuremech:mitostore.

Clogger-induced precursor accumulation, chaperone deletion and Mam33 presequence truncation have the stated condition-specific directions. Heterogeneous precursor-cargo nodes are appropriate; reporters are not automatically fixed constituent subunits.

### Recovery and survival graph

graph: supported. Targets: cellstructuremech:mitostore.

4.5h loading followed by4h chase/split-GFP supports renewed matrix import competence, without single-molecule tracing from an individual granule. RPN4 deletion/chaperone-dependent survival after24h clogger expression remains condition-specific and does not isolate granule-only causality.

### Proteomics provenance and archive inconsistency

provenance: supported. Targets: cellstructuremech:mitostore.

PXD035762 is cited through the paper as Hsp104 AP-MS provenance. Current metadata mismatch to the Ubc8 reference and2920-versus1154 filtered proteins is already documented. No raw-data reanalysis, complete native inventory or corrected archive bibliography is claimed; this is an explicit source limitation, not a new untracked record error.

### Tracked image and comparison-source scope

provenance: supported. Targets: cellstructuremech:mitostore.

Figure5 pixels, panel-specific scales, caption, primary attribution/license and media checksum agree. Tom70 heat-stress comparisons remain similarities without identity/necessity transfer. No LLPS mechanism is promoted from these observations.

### Structured source applicability after actual catalogue inspection

evidence: supported. Targets: cellstructuremech:age_associated_protein_deposit.

Named yeast protein/stress claims trigger applicability review. Fresh iModulonDB catalogue has no matching Saccharomyces organism/dataset, so downstream module/gene/activity checks are N/A within that inspected catalogue. Historical runner unavailability is explicitly dated; absence from the catalogue is not negative biological evidence. The original absent applicability coverage is repaired.

### Native protein inventory verification limits

schema: supported. Targets: cellstructuremech:age_associated_protein_deposit.

Seven examples passed, but the causal scan has zero GENE_OR_PROTEIN nodes; it does not validate every experimental factor.

### Frozen inputs, staleness and original lineage

provenance: supported. Targets: cellstructuremech:age_associated_protein_deposit.

Original validation/render passed and no scientific findings were present. Target bytes remain identical to the original frozen input. No category-wide or unrelated issue resolution is claimed.

### Scientific verdict and bounded completeness

completeness: supported. Targets: cellstructuremech:age_associated_protein_deposit.

Current whole-record assessment remains pass_with_limitations, with no confirmed record-curation finding or curation action. Existing discussions retain uncertain complete composition, experimental context and source limits. Passing schema/identifier checks is not treated as proof of all biological claims.

### Structured source applicability after actual catalogue inspection

evidence: supported. Targets: cellstructuremech:insoluble_protein_deposit.

Named yeast protein/stress claims trigger applicability review. Fresh iModulonDB catalogue has no matching Saccharomyces organism/dataset, so downstream module/gene/activity checks are N/A within that inspected catalogue. Historical runner unavailability is explicitly dated; absence from the catalogue is not negative biological evidence. The original no-expression-claim exemption is replaced by an evidenced catalogue-based conclusion.

### Native protein inventory verification limits

schema: supported. Targets: cellstructuremech:insoluble_protein_deposit.

One example passed; graph scan reports one COVERED and one NO_GENE_SYMBOLS heterogeneous cargo node, without dangling references.

### Frozen inputs, staleness and original lineage

provenance: supported. Targets: cellstructuremech:insoluble_protein_deposit.

Original validation/render passed and no scientific findings were present. Current record differs by two exact self-identity node groundings plus history; both new groundings were reassessed and accepted. Current evidence refreshes the stale assessment without rewriting the original source hashes. No category-wide or unrelated issue resolution is claimed.

### Scientific verdict and bounded completeness

completeness: supported. Targets: cellstructuremech:insoluble_protein_deposit.

Current whole-record assessment remains pass_with_limitations, with no confirmed record-curation finding or curation action. Existing discussions retain uncertain complete composition, experimental context and source limits. Passing schema/identifier checks is not treated as proof of all biological claims.

### Structured source applicability after actual catalogue inspection

evidence: supported. Targets: cellstructuremech:mitostore.

Named yeast protein/stress claims trigger applicability review. Fresh iModulonDB catalogue has no matching Saccharomyces organism/dataset, so downstream module/gene/activity checks are N/A within that inspected catalogue. Historical runner unavailability is explicitly dated; absence from the catalogue is not negative biological evidence. The original absent applicability coverage is repaired.

### Native protein inventory verification limits

schema: supported. Targets: cellstructuremech:mitostore.

Three examples passed; graph scan reports two NO_GENE_SYMBOLS heterogeneous precursor-cargo nodes, without dangling references.

### Frozen inputs, staleness and original lineage

provenance: supported. Targets: cellstructuremech:mitostore.

Original validation/render passed and no scientific findings were present. Current record differs by two exact self-identity node groundings plus history; both new groundings were reassessed and accepted. Current evidence refreshes the stale assessment without rewriting the original source hashes. No category-wide or unrelated issue resolution is claimed.

### Scientific verdict and bounded completeness

completeness: supported. Targets: cellstructuremech:mitostore.

Current whole-record assessment remains pass_with_limitations, with no confirmed record-curation finding or curation action. Existing discussions retain uncertain complete composition, experimental context and source limits. Passing schema/identifier checks is not treated as proof of all biological claims.

### Bacterial inclusion identity and neighboring condensates

identity: supported. Targets: cellstructuremech:bacterial_aggresome.

The local proposed bacterial structure is compatible with inclusion-body parent and cytoplasmic parthood. GO0016235 requires dynein-dependent microtubule transport and is not an exact identity. RNaseE BR-bodies and Hfq H-bodies remain distinct boundary records.

### Observed constituent subset

completeness: supported. Targets: cellstructuremech:bacterial_aggresome.

HslU, Kbl and AcnB are experimentally observed markers with different recruitment timing; selected mRNAs are enriched. This is a supported subset, not a complete or fixed condensate proteome. Upstream HokB and excluded wild-type RNases are correctly contextual rather than automatic constituents.

### Exact molecular identities and family scope

grounding: supported. Targets: cellstructuremech:bacterial_aggresome.

HslU IPR004491/P0A6H5, Kbl IPR011282/P0AB77, AcnB IPR004406/P36683 and mRNA SO0000234 match their declared scopes. K-12 concrete examples are distinct from the explicitly experimental MG1655 strain.

### Formation necessity remains unresolved

evidence: unknown. Targets: cellstructuremech:bacterial_aggresome.

Observed enrichment and reporter localization do not establish that every listed constituent is required to form the structure. UNKNOWN necessity is retained; charge-mutant RNase perturbations test RNA protection, not a universal minimal composition.

### Experimental strain and stress-state boundaries

scope: supported. Targets: cellstructuremech:bacterial_aggresome.

The primary experiments and taxon authorities support the scoped E. coli/MG1655 examples. Neither the local generic label nor the tested liquid-like behavior asserts universal bacterial prevalence, identical dynamics or every aggregated inclusion.

### RNase exclusion, transcript preservation and recovery graph

evidence: supported. Targets: cellstructuremech:bacterial_aggresome.

All six recorded edges preserve the tested sequence: selected RNA recruitment, exclusion of tested RNases, protection, stress-release and translation recovery. Active RNB-MO entry/depletion is distinguished from inactive ME variants; RNA itself as the repulsive agent remains proposed. Rifampicin/tetracycline controls bound the recovery interpretation, and the graph avoids a universal fitness or persistence conclusion.

### Matched structured-source context and its limits

scope: supported. Targets: cellstructuremech:bacterial_aggresome.

The molecular policy applies. Fresh official MG1655 metadata, eleven exact gene lookups, all115 module flags per gene and six positive-module membership cross-checks were inspected. Positives are hslU/RpoH, kbl/Lrp-2, acnB/ArcA-2, glpK/Glycerol, nuoJ/UC-5 and hokB/ldrD. mukF/nlpE/rnb/rbn/orn have all-false flags in this dataset; these are threshold results, never absence. No condition-specific activity analysis or condensate recruitment is inferred.

### Native verification and original bundle integrity

schema: supported. Targets: cellstructuremech:bacterial_aggresome.

Current concrete protein identity checks pass; zero typed protein graph nodes is an empty causal inventory, not independent validation of all narrative RNases/transcripts. Original schema/render and target frozen hash pass; the missing original applicability assessment is an in-scope bundle correction.

### Shell material and whole organelle boundary

identity: supported. Targets: GO:0033172.

GO0033172 exactly denotes the protein wall; parthood to GO0031411 and the related membrane synonym do not make it a lipid bilayer. Whole-organelle accessory assembly and historical findings remain context only.

### GvpA ribs and exterior GvpC

evidence: supported. Targets: GO:0033172.

Dutka and Bayro support the GvpA polymer wall; primary stripping/rebinding evidence and structural comparison support exterior GvpC strengthening. Accessory assembly proteins are not automatically persistent shell constituents. No exhaustive minor-component inventory is asserted.

### Available exact GvpA family

grounding: concern. Targets: GO:0033172.

Original F1 remains confirmed: IPR047870 is an exact GvpA family and is present on the recorded accession; the component still lacks grounding. PF00741/IPR000638 is broader GvpA-like scope. GvpC repeat entries are not exact whole-protein identities.

### GvpC conditional formation requirement

evidence: unknown. Targets: GO:0033172.

GvpA is the wall scaffold. Stripping/rebinding changes the strength of already formed shells; neither that experiment nor an unassessed formation context proves or refutes every conditional GvpC assembly requirement. This is an explicit unresolved check, not a new contradictory finding or a resolution of whole-organelle historical claims.

### Variable occurrence and distinct strain examples

scope: supported. Targets: GO:0033172.

Broad bacterial/archaeal variable occurrence is supported at review scope. The native structural preparation names Dolichospermum flos-aquae1403/13F; the two concrete protein examples instead identify Anabaena cylindrica FACHB-318 and remain unreviewed. These strains are not conflated.

### Ribs, reinforcement and gas-filled interior

evidence: supported. Targets: GO:0033172.

The graph separates GvpA polymerization, shell formation, exterior reinforcement and buoyancy-supporting gas space. Gas permeability and liquid-water exclusion are source-supported at stated primary/abstract scopes; no active gas storage, species-universal pressure threshold or complete initiation mechanism is implied.

### Applicability assessed by native source coverage

scope: supported. Targets: GO:0033172.

Named GvpA/GvpC claims trigger applicability assessment; the original no-transcriptomic-inference rationale is insufficient. The fresh catalogue has no matching native source taxon/strain dataset. Unrelated cyanobacteria and heterologous E. coli contexts are not proxies for these shell proteins, so no unmatched gene query is invented.

### Protein checks, original bundle and finding lineage

schema: supported. Targets: GO:0033172.

Both current concrete examples verify and both protein graph nodes are covered. Original validation/render and unchanged input hash pass. F1 remains curation, while the applicability rationale is fixed only in the successor bundle.

### Monolayer identity versus storage organelle

identity: supported. Targets: GO:0034430.

GO0034430 and its synonym types denote the single surface layer, distinct from the whole lipid droplet. Parthood and membrane kind agree with the scoped mature topology; an imported oil-body synonym does not certify all possible taxa or plastoglobule equivalence.

### Class-level phospholipid material

grounding: supported. Targets: GO:0034430.

CHEBI16247 matches the phospholipid class. Associated proteins belong to the explicit whole-organelle context and are not automatically members of the lipid layer. No particular lipid species or universal protein coat is required by this record.

### Material requirement versus individual species

evidence: supported. Targets: GO:0034430.

ESSENTIAL applies to the defining collective phospholipid layer; it does not promote individual phospholipid species to indispensable status. Condition-dependent primary lipidomics remains compatible with this class-level representation.

### Yeast evidence and unresolved plastid boundary

scope: supported. Targets: GO:0034430.

Yeast lipid-particle observations support the stated S. cerevisiae example. Austin primary boundary evidence concerns plant plastoglobules coupled to thylakoids; it keeps the boundary discussion open without silently extending the yeast experiment or merging neighboring structures.

### Mature surface topology

evidence: supported. Targets: GO:0034430.

The nonmechanistic graph describes phospholipid material arranged around a neutral-lipid core. It does not claim an experimentally settled ER biogenesis pathway or inherit every protein in the secondary review.

### Material-only scope supports non-applicability

scope: supported. Targets: GO:0034430.

This target asserts material and topology without named gene, protein or pathway claims. That actual scope supports N/A. Its original expression-only wording is clarified, but no missing molecular query or additional bundle defect is manufactured.

### Empty native protein inventory and original integrity

schema: supported. Targets: GO:0034430.

Verify and causal checks pass over empty protein examples/typed protein nodes. This is bounded schema coverage, not molecular validation. Original native review schema/render and target hash pass; the current verdict remains pass with limitations.

### Crystalline inclusion and bounded GO search

identity: supported. Targets: cellstructuremech:parasporal_crystal.

The local proposed identity and inclusion-body parent distinguish the crystal from a single toxin or spore. Native exact GO phrase searches are bounded and do not prove exhaustive absence. Historical parasporal-body usage is contextual, not exact equivalence of every preparation.

### Mixed Cry/Cyt cohort is not a single family

grounding: supported. Targets: cellstructuremech:parasporal_crystal.

The collective constituent covers distinct Cry lineages and Cyt proteins; label-only collective grounding is justified. Native IPR038979 and IPR001615 support different family scopes, not a universal identifier for the entire mixed crystal. No new grounding defect is established.

### Concrete protein identities

grounding: supported. Targets: cellstructuremech:parasporal_crystal.

P16480 cry4Aa, P21256 cry11Aa and P0A382 cyt1Aa are reviewed entries for israelensis1430; exact queries corroborate them. They are examples rather than an exhaustive strain inventory or a universal stoichiometry.

### Crystal formation versus toxicity

evidence: unknown. Targets: cellstructuremech:parasporal_crystal.

UNKNOWN necessity is retained for the broad constituent cohort. Biological activity after solubilization/activation and modern specific toxin structures do not establish a universal formation requirement or the minimal composition of all crystals.

### Strain and historical morphology limits

scope: supported. Targets: cellstructuremech:parasporal_crystal.

Variable Bt occurrence and the israelensis example remain bounded by strain/plasmid differences. All seven Insell primary scan pages were read, including figures: historical light/dark lattice and polypeptide fractions are not assigned to exact modern Cry/Cyt accessions.

### Packaging graph and conventional activity terminology

evidence: supported. Targets: cellstructuremech:parasporal_crystal.

The single nonmechanistic edge represents a crystalline packaging state, not a full sporulation or toxin-action mechanism. Pesticidal is conventional cohort terminology here, not demonstrated activity for every parasporin or every constituent.

### Applicability assessed without mismatched species

scope: supported. Targets: cellstructuremech:parasporal_crystal.

Named Cry/Cyt molecular claims require an applicability assessment. Fresh official catalogue includes no B. thuringiensis/israelensis dataset; B. subtilis is not a replacement and no arbitrary gene/module query is invented. The original omitted assessment is corrected in the successor.

### Current native checks and original integrity

schema: supported. Targets: cellstructuremech:parasporal_crystal.

All three examples verify and the single typed protein graph node has declared-symbol coverage. This cannot certify the entire mixed Cry/Cyt pool. Original schema/render and unchanged input hash pass.

### Complete frozen-input comparison and bounded refresh

provenance: supported. Targets: cellstructuremech:age_associated_protein_deposit, cellstructuremech:bacterial_aggresome, GO:0033172, cellstructuremech:insoluble_protein_deposit, cellstructuremech:intranuclear_quality_control_compartment, cellstructuremech:juxtanuclear_quality_control_compartment, cellstructuremech:mitostore, GO:0034430, GO:0140602, cellstructuremech:parasporal_crystal.

2 of ten original target hashes differ from current main. The changed content is substantively reassessed in the target-specific assessments; original observations remain historical and unchanged. All current target and used context bytes are frozen.

## Findings

### septin-S2356-F1: Record the verified exact GvpA family grounding

minor / open / confirmed; issue key: gas-vesicle-shell-gvpa-family-grounding.

The named GvpA constituent has no grounding or explicit unresolved-grounding discussion. Native IPR047870 specifically denotes GvpA, whereas the existing graph xref PF00741 covers a broader GvpA-like family including GvpJ. Add the exact family at the component; retain broader graph xrefs as related context. The GvpC repeat entries are not whole-protein equivalents.

## Recommended Actions And Acceptance Checks

### septin-S2356-C1

Ground the GvpA component to verified InterPro IPR047870 with exact family provenance and appropriate grounding status. Preserve the distinction between exact family identity, concrete protein examples and related graph xrefs.

- Reconfirm IPR047870 is the GvpA-specific family, with the broader GvpA-like entry kept distinct.
- Do not promote PF01304 or the GvpC repeat entries to whole-protein equivalence.
- Use separately authorized guarded curation, append-only history, focused validators, identifier/product checks and regeneration.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| current-record-0 | data/structures/inclusion/age_associated_protein_deposit.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 f782fddfb8eb004a13ce40857c05527e29272b04da88e010cec04250ca867c30; current SHA256 f782fddfb8eb004a13ce40857c05527e29272b04da88e010cec04250ca867c30. Record bytes unchanged since the original review. |
| original-review-0 | reviews/structured/20261021T103319Z-age-associated-protein-deposit-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-1 | data/structures/inclusion/bacterial_aggresome.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 8f6d6cf20835c5114b8c13bc929767a750bbb7b0db778799d7d1e1be387f8636; current SHA256 8f6d6cf20835c5114b8c13bc929767a750bbb7b0db778799d7d1e1be387f8636. Record bytes unchanged since the original review. |
| original-review-1 | reviews/structured/20261021T103320Z-bacterial-aggresome-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-2 | data/structures/inclusion/gas_vesicle_shell.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 06f0f2aa709e62b9e46e2e38d2ce26692fc0d8e0fe16a78d998aa7a51b1e0ae6; current SHA256 06f0f2aa709e62b9e46e2e38d2ce26692fc0d8e0fe16a78d998aa7a51b1e0ae6. Record bytes unchanged since the original review. |
| original-review-2 | reviews/structured/20261021T103321Z-gas-vesicle-shell-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-3 | data/structures/inclusion/insoluble_protein_deposit.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 45a74ced04c8c5714cd45f6a8a04c45ae8a5af22a04809aa51520c54884fb773; current SHA256 8bf3ffb3c2ce2ee5448d00f88d4d0de7911e3ee135e409e174a40f5c890e5f8a. Changed record reassessed against current sources. |
| original-review-3 | reviews/structured/20261021T103322Z-insoluble-protein-deposit-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-4 | data/structures/inclusion/intranuclear_quality_control_compartment.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 7e6cc3b1915d2093b6712f349dea34cad79831f2d4b93f0eaff29351b37f3c36; current SHA256 7e6cc3b1915d2093b6712f349dea34cad79831f2d4b93f0eaff29351b37f3c36. Record bytes unchanged since the original review. |
| original-review-4 | reviews/structured/20261021T103323Z-intranuclear-quality-control-compartment-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-5 | data/structures/inclusion/juxtanuclear_quality_control_compartment.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 c3fbd426fe95ef931039579f467743997b83a889fa00c53442b36f46ccd95545; current SHA256 c3fbd426fe95ef931039579f467743997b83a889fa00c53442b36f46ccd95545. Record bytes unchanged since the original review. |
| original-review-5 | reviews/structured/20261021T103324Z-juxtanuclear-quality-control-compartment-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-6 | data/structures/inclusion/mitostore.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 6863a577037a5f308979f0c7cdcccda5b49ebe7f64586192cef53ca27291347a; current SHA256 c932945c5ae1c4501b217b75333c4ae85551096cd4630bdae07f3ef84b0a7dd4. Changed record reassessed against current sources. |
| original-review-6 | reviews/structured/20261021T103324Z-mitostore-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-7 | data/structures/inclusion/monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 d72e9789b2d49d4fe380c06834e31dfe9eaf46fb6a412ddecdc9c8e1742b7a87; current SHA256 d72e9789b2d49d4fe380c06834e31dfe9eaf46fb6a412ddecdc9c8e1742b7a87. Record bytes unchanged since the original review. |
| original-review-7 | reviews/structured/20261021T103325Z-monolayer-surrounded-lipid-storage-body-outer-lipid-monolayer-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-8 | data/structures/inclusion/nucleolar_peripheral_inclusion_body.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 0882138e885027304adbb077da65d773ad7a2197cd6cb5d7ab3688a49f9c35cc; current SHA256 0882138e885027304adbb077da65d773ad7a2197cd6cb5d7ab3688a49f9c35cc. Record bytes unchanged since the original review. |
| original-review-8 | reviews/structured/20261021T103326Z-nucleolar-peripheral-inclusion-body-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-9 | data/structures/inclusion/parasporal_crystal.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 59163a5ec708789816078e74a74e62fd9d3dbd38b580c40103a658e711274052; current SHA256 59163a5ec708789816078e74a74e62fd9d3dbd38b580c40103a658e711274052. Record bytes unchanged since the original review. |
| original-review-9 | reviews/structured/20261021T103327Z-parasporal-crystal-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| plaque-current-4 | data/structures/inclusion/intranuclear_quality_control_compartment.yaml; Entire maintained record, including discussion qualifications and image metadata | supports | Complete unchanged current input independently read; scientific judgments apply to these exact bytes. |
| plaque-original-4 | reviews/structured/20261021T103323Z-intranuclear-quality-control-compartment-audit/review.yaml; Original complete YAML and paired rendered Markdown | supports | Historical original has pass_with_limitations and no findings; no prior scientific finding is silently closed. Current reassessment preserves the original unchanged. |
| plaque-image-4 | data/images/inclusion/intranuclear_quality_control_compartment/pmc4389229_f3.jpg; Actual frozen image pixels visually inspected in this review; full multi-panel composite, not just its caption | supports | Image pixels and panel labels inspected. Local SHA256 matches the record; local MD5 matches the freshly fetched native PMC package media row. Caption and exact CC BY4.0 attribution assessed separately from JATS. |
| plaque-current-5 | data/structures/inclusion/juxtanuclear_quality_control_compartment.yaml; Entire maintained record, including discussion qualifications and image metadata | supports | Complete unchanged current input independently read; scientific judgments apply to these exact bytes. |
| plaque-original-5 | reviews/structured/20261021T103324Z-juxtanuclear-quality-control-compartment-audit/review.yaml; Original complete YAML and paired rendered Markdown | supports | Historical original has pass_with_limitations and no findings; no prior scientific finding is silently closed. Current reassessment preserves the original unchanged. |
| plaque-image-5 | data/images/inclusion/juxtanuclear_quality_control_compartment/pmc11372896_f2.jpg; Actual frozen image pixels visually inspected in this review; full multi-panel composite, not just its caption | supports | Image pixels and panel labels inspected. Local SHA256 matches the record; local MD5 matches the freshly fetched native PMC package media row. Caption and exact CC BY4.0 attribution assessed separately from JATS. |
| plaque-current-8 | data/structures/inclusion/nucleolar_peripheral_inclusion_body.yaml; Entire maintained record, including discussion qualifications and image metadata | supports | Complete unchanged current input independently read; scientific judgments apply to these exact bytes. |
| plaque-original-8 | reviews/structured/20261021T103326Z-nucleolar-peripheral-inclusion-body-audit/review.yaml; Original complete YAML and paired rendered Markdown | supports | Historical original has pass_with_limitations and no findings; no prior scientific finding is silently closed. Current reassessment preserves the original unchanged. |
| plaque-image-8 | data/images/inclusion/nucleolar_peripheral_inclusion_body/pmc10342647_ijms_24_11202_f007.jpg; Actual frozen image pixels visually inspected in this review; full multi-panel composite, not just its caption | supports | Image pixels and panel labels inspected. Local SHA256 matches the record; local MD5 matches the freshly fetched native PMC package media row. Caption and exact CC BY4.0 attribution assessed separately from JATS. |
| plaque-native-review-policy | .claude/skills/review-yaml-record/SKILL.md; Structured Source Cross-Checks; Evidence Rules; native profile and current schema | supports | Named genes, proteins, pathways and stress responses require actual structured-source applicability assessment; a lack of expression claims alone does not exempt a record. Runner unavailability allows an honestly described source fallback. |
| plaque-inq-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0016604,GO:0016234,GO:0005634,GO:0097165; Native JSON response | supports | Native GO definitions/labels: GO:0005634 nucleus; GO:0016234 inclusion body; GO:0016604 nuclear body; GO:0097165 nuclear stress granule. Structural identity and is-a/parthood are assessed against the primary scope. |
| plaque-inq-go-search-0 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=INQ&amp;limit=100&amp;page=1; Native JSON response | supports | QuickGO query returned numberOfHits=0; 0 results inspected on requested first page. No exact INQ identity was observed in this bounded result set; related processes are not adopted as structural identity. |
| plaque-inq-go-search-1 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=intranuclear+quality+control&amp;limit=100&amp;page=1; Native JSON response | supports | QuickGO query returned numberOfHits=89; 89 results inspected on requested first page. No exact INQ identity was observed in this bounded result set; related processes are not adopted as structural identity. |
| plaque-inq-ols-exact | https://www.ebi.ac.uk/ols4/api/search?q=intranuclear+quality+control+compartment&amp;ontology=go&amp;exact=true&amp;rows=100; Native JSON response | supports | Exact GO-ontology OLS query returned 0 terms. This bounded search supports retaining the local mint provisionally, not exhaustive ontology absence. |
| plaque-inq-P53286 | https://rest.uniprot.org/uniprotkb/P53286.json; Native JSON response | supports | Native UniProtKB reviewed (Swiss-Prot) accession P53286; primary genes ['BTN2']; taxon 559292. Authority verifies identity, not inclusion localization or necessity. |
| plaque-inq-query-BTN2 | https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A559292+AND+gene_exact%3ABTN2&amp;format=json&amp;size=500; Native JSON response | supports | Bounded reviewed exact-gene/taxon query returned ['P53286']; corroborates declared reference-sequence example, not the experimental strain or in situ role. |
| plaque-inq-P31539 | https://rest.uniprot.org/uniprotkb/P31539.json; Native JSON response | supports | Native UniProtKB reviewed (Swiss-Prot) accession P31539; primary genes ['HSP104']; taxon 559292. Authority verifies identity, not inclusion localization or necessity. |
| plaque-inq-query-HSP104 | https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A559292+AND+gene_exact%3AHSP104&amp;format=json&amp;size=500; Native JSON response | supports | Bounded reviewed exact-gene/taxon query returned ['P31539']; corroborates declared reference-sequence example, not the experimental strain or in situ role. |
| plaque-inq-Q12510 | https://rest.uniprot.org/uniprotkb/Q12510.json; Native JSON response | supports | Native UniProtKB reviewed (Swiss-Prot) accession Q12510; primary genes ['CMR1']; taxon 559292. Authority verifies identity, not inclusion localization or necessity. |
| plaque-inq-query-CMR1 | https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A559292+AND+gene_exact%3ACMR1&amp;format=json&amp;size=500; Native JSON response | supports | Bounded reviewed exact-gene/taxon query returned ['Q12510']; corroborates declared reference-sequence example, not the experimental strain or in situ role. |
| plaque-inq-interpro-P53286 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P53286/?page_size=200; Native JSON response | supports | Integrated InterPro match set count=1, next=None: IPR062150/BTN2-like, N-terminal domain/domain. Family/domain types are distinguished; membership is not localization evidence. |
| plaque-inq-interpro-P31539 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P31539/?page_size=200; Native JSON response | supports | Integrated InterPro match set count=11, next=None: IPR001270/ClpA/B family/family; IPR003593/AAA+ ATPase domain/domain; IPR003959/ATPase, AAA-type, core/domain; IPR004176/Clp, repeat (R) N-terminal domain/domain; IPR018368/ClpA/B, conserved site 1/conserved_site; IPR019489/Clp ATPase, C-terminal/domain; IPR027417/P-loop containing nucleoside triphosphate hydrolase/homologous_superfamily; IPR028299/ClpA/B, conserved site 2/conserved_site; IPR036628/Clp, N-terminal domain superfamily/homologous_superfamily; IPR041546/ClpA/ClpB, AAA lid domain/domain; IPR050130/ATP-dependent Clp protease/Chaperone ClpA/ClpB/family. Family/domain types are distinguished; membership is not localization evidence. |
| plaque-inq-interpro-Q12510 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q12510/?page_size=200; Native JSON response | supports | Integrated InterPro match set count=5, next=None: IPR001680/WD40 repeat/repeat; IPR015943/WD40/YVTN repeat-like-containing domain superfamily/homologous_superfamily; IPR019775/WD40 repeat, conserved site/conserved_site; IPR036322/WD40-repeat-containing domain superfamily/homologous_superfamily; IPR050853/WD repeat-containing DNA damage-binding protein/family. Family/domain types are distinguished; membership is not localization evidence. |
| plaque-inq-IPR050853 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050853/; Native JSON response | supports | InterPro IPR050853 has name WD repeat-containing DNA damage-binding protein and type family. Only identity/type is used; unchecked generated descriptions are excluded. |
| plaque-inq-taxon-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Native JSON response | supports | ENA native taxonomy authority resolves 4932 to Saccharomyces cerevisiae at rank species; reference strain versus assayed mutant/strain remains separately qualified. |
| plaque-inq-taxon-559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Native JSON response | supports | ENA native taxonomy authority resolves 559292 to Saccharomyces cerevisiae S288C at rank strain; reference strain versus assayed mutant/strain remains separately qualified. |
| plaque-inq-miller2015-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC4369314/?report=xml; Full main body Results sec3/sec7/sec8, Figures2/6/7 captions, DOI/PMID article metadata | supports | Miller2015 primary full article HTML: Results on nuclear localization, Fig2, Btn2 deposition/degradation Fig6, engineered Hsp42-NLS rescue Fig7 and captions. Supplemental panels/videos not independently inspected. |
| plaque-inq-gallina2015-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC4389229.1/PMC4389229.1.xml; Results Cmr1 marks INQ; Btn2 promotes Mrc1 turnover; Discussion; Methods strain paragraph; Figure3 and JATS license | supports | Gallina2015 primary main body and Fig3 distinguish nuclear Cmr1-associated inclusions, heterogeneous cargo, marker stability, residual deletion phenotypes and stress-specific targeting. Mrc1 recruitment does not require Cmr1. Default W303 and S288C library contexts remain distinct. |
| plaque-inq-sontag2023-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC12349969.1/PMC12349969.1.xml; Main Results S1-S9; Figures1-8 captions; Methods; article DOI/PMID | supports | Sontag2023 primary main Results separate nuclear INQ from cytoplasmic JUNQ, convergence from fusion, Q-body congregation from uniform body architecture, and vacuolar clearance from universal degradation. Genetic phenotypes and Keima/turnover readouts remain reporter-specific. |
| plaque-inq-gallina2015-package | https://pmc-oa-opendata.s3.amazonaws.com/PMC4389229.1/PMC4389229.1.json; PMC article package metadata, DOI/PMID/license and exact figure media MD5 | supports | PMC package PMC4389229 version 1 identifies DOI 10.1038/ncomms7533, PMID 25817432; exact figure media MD5 matches the frozen local bytes. JATS provides exact license version. |
| plaque-junq-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000502,GO:0005737,GO:0016234; Native JSON response | supports | Native GO definitions/labels: GO:0005737 cytoplasm; GO:0016234 inclusion body; GO:0000502 proteasome complex. Structural identity and is-a/parthood are assessed against the primary scope. |
| plaque-junq-ols-exact-0 | https://www.ebi.ac.uk/ols4/api/search?ontology=go&amp;exact=true&amp;rows=100&amp;q=juxtanuclear%20quality%20control%20compartment; Native JSON response | supports | Exact GO-ontology OLS query returned 0 terms. This bounded search supports retaining the local mint provisionally, not exhaustive ontology absence. |
| plaque-junq-ols-exact-1 | https://www.ebi.ac.uk/ols4/api/search?ontology=go&amp;exact=true&amp;rows=100&amp;q=JUNQ; Native JSON response | supports | Exact GO-ontology OLS query returned 0 terms. This bounded search supports retaining the local mint provisionally, not exhaustive ontology absence. |
| plaque-junq-tax-1247190 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1247190; Native JSON response | supports | ENA native taxonomy authority resolves 1247190 to Saccharomyces cerevisiae BY4741 at rank strain; reference strain versus assayed mutant/strain remains separately qualified. |
| plaque-junq-IPR001270 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001270/; Native JSON response | supports | InterPro IPR001270 has name ClpA/B family and type family. Only identity/type is used; unchecked generated descriptions are excluded. |
| plaque-junq-IPR050130 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050130/; Native JSON response | supports | InterPro IPR050130 has name ATP-dependent Clp protease/Chaperone ClpA/ClpB and type family. Only identity/type is used; unchecked generated descriptions are excluded. |
| plaque-junq-jats-PMC11372896 | https://pmc-oa-opendata.s3.amazonaws.com/PMC11372896.1/PMC11372896.1.xml; Methods Table2 and mitochondrial-labeling method; Results3.1-3.5; Discussion; Figure2; JATS license | supports | Rolli2024 primary Results support chaperone-dependent sorting, double-Ssa1/Ssa2 peripheral deposits, Btn2/Hsp42 sorting and Atg1/Atg8-sensitive clearance. Discussion leaves vacuolar entry unresolved and excludes conclusions from Vps15/34 expression-limited assays. |
| plaque-junq-native-package-PMC11372896 | https://pmc-oa-opendata.s3.amazonaws.com/PMC11372896.1/PMC11372896.1.json; PMC article package metadata, DOI/PMID/license and exact figure media MD5 | supports | PMC package PMC11372896 version 1 identifies DOI 10.3389/fmolb.2024.1427542, PMID 39234568; exact figure media MD5 matches the frozen local bytes. JATS provides exact license version. |
| plaque-nur-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005634,GO:0042405,GO:0140602; Native JSON response | supports | Native GO definitions/labels: GO:0005634 nucleus; GO:0140602 nucleolar peripheral inclusion body; GO:0042405 nuclear inclusion body. Structural identity and is-a/parthood are assessed against the primary scope. |
| plaque-nur-tax-284812 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/284812; Native JSON response | supports | ENA native taxonomy authority resolves 284812 to Schizosaccharomyces pombe 972h- at rank strain; reference strain versus assayed mutant/strain remains separately qualified. |
| plaque-nur-tax-4896 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4896; Native JSON response | supports | ENA native taxonomy authority resolves 4896 to Schizosaccharomyces pombe at rank species; reference strain versus assayed mutant/strain remains separately qualified. |
| plaque-nur-Q9UUE5 | https://rest.uniprot.org/uniprotkb/Q9UUE5.json; Native JSON response | supports | Native UniProtKB reviewed (Swiss-Prot) accession Q9UUE5; primary genes ['nup85']; taxon 284812. Authority verifies identity, not inclusion localization or necessity. |
| plaque-nur-query-nup85 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3Anup85%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29&amp;size=100; Native JSON response | supports | Bounded reviewed exact-gene/taxon query returned ['Q9UUE5']; corroborates declared reference-sequence example, not the experimental strain or in situ role. |
| plaque-nur-Q9Y8G3 | https://rest.uniprot.org/uniprotkb/Q9Y8G3.json; Native JSON response | supports | Native UniProtKB reviewed (Swiss-Prot) accession Q9Y8G3; primary genes ['mex67']; taxon 284812. Authority verifies identity, not inclusion localization or necessity. |
| plaque-nur-query-mex67 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3Amex67%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29&amp;size=100; Native JSON response | supports | Bounded reviewed exact-gene/taxon query returned ['Q9Y8G3']; corroborates declared reference-sequence example, not the experimental strain or in situ role. |
| plaque-nur-Q10265 | https://rest.uniprot.org/uniprotkb/Q10265.json; Native JSON response | supports | Native UniProtKB reviewed (Swiss-Prot) accession Q10265; primary genes ['ssa1']; taxon 284812. Authority verifies identity, not inclusion localization or necessity. |
| plaque-nur-query-ssa1 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3Assa1%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29&amp;size=100; Native JSON response | supports | Bounded reviewed exact-gene/taxon query returned ['Q10265']; corroborates declared reference-sequence example, not the experimental strain or in situ role. |
| plaque-nur-O59855 | https://rest.uniprot.org/uniprotkb/O59855.json; Native JSON response | supports | Native UniProtKB reviewed (Swiss-Prot) accession O59855; primary genes ['ssa2']; taxon 284812. Authority verifies identity, not inclusion localization or necessity. |
| plaque-nur-query-ssa2 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3Assa2%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29&amp;size=100; Native JSON response | supports | Bounded reviewed exact-gene/taxon query returned ['O59855']; corroborates declared reference-sequence example, not the experimental strain or in situ role. |
| plaque-nur-O74752 | https://rest.uniprot.org/uniprotkb/O74752.json; Native JSON response | supports | Native UniProtKB reviewed (Swiss-Prot) accession O74752; primary genes ['mas5']; taxon 284812. Authority verifies identity, not inclusion localization or necessity. |
| plaque-nur-query-mas5 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3Amas5%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29&amp;size=100; Native JSON response | supports | Bounded reviewed exact-gene/taxon query returned ['O74752']; corroborates declared reference-sequence example, not the experimental strain or in situ role. |
| plaque-nur-O94641 | https://rest.uniprot.org/uniprotkb/O94641.json; Native JSON response | supports | Native UniProtKB reviewed (Swiss-Prot) accession O94641; primary genes ['hsp104']; taxon 284812. Authority verifies identity, not inclusion localization or necessity. |
| plaque-nur-query-hsp104 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3Ahsp104%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29&amp;size=100; Native JSON response | supports | Bounded reviewed exact-gene/taxon query returned ['O94641']; corroborates declared reference-sequence example, not the experimental strain or in situ role. |
| plaque-nur-matches-Q9UUE5 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q9UUE5/?page_size=200; Native JSON response | supports | Integrated InterPro match set count=1, next=None: IPR011502/Nucleoporin Nup85-like/family. Family/domain types are distinguished; membership is not localization evidence. |
| plaque-nur-matches-Q9Y8G3 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q9Y8G3/?page_size=200; Native JSON response | supports | Integrated InterPro match set count=10, next=None: IPR001611/Leucine-rich repeat/repeat; IPR002075/Nuclear transport factor 2 domain/domain; IPR005637/TAP C-terminal (TAP-C) domain/domain; IPR009060/UBA-like superfamily/homologous_superfamily; IPR018222/Nuclear transport factor 2, eukaryote/domain; IPR030217/Nuclear RNA export factor/family; IPR032675/Leucine-rich repeat domain superfamily/homologous_superfamily; IPR032710/NTF2-like domain superfamily/homologous_superfamily; IPR040736/Mex67, RNA recognition motif/domain; IPR057125/NXF1/2/3/5-like, leucine-rich repeat domain/domain. Family/domain types are distinguished; membership is not localization evidence. |
| plaque-nur-matches-Q10265 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q10265/?page_size=200; Native JSON response | supports | Integrated InterPro match set count=5, next=None: IPR013126/Heat shock protein 70 family/family; IPR018181/Heat shock protein 70, conserved site/conserved_site; IPR029047/Heat shock protein 70kD, peptide-binding domain superfamily/homologous_superfamily; IPR029048/Heat shock protein 70kD, C-terminal domain superfamily/homologous_superfamily; IPR043129/ATPase, nucleotide binding domain/homologous_superfamily. Family/domain types are distinguished; membership is not localization evidence. |
| plaque-nur-matches-O59855 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/O59855/?page_size=200; Native JSON response | supports | Integrated InterPro match set count=5, next=None: IPR013126/Heat shock protein 70 family/family; IPR018181/Heat shock protein 70, conserved site/conserved_site; IPR029047/Heat shock protein 70kD, peptide-binding domain superfamily/homologous_superfamily; IPR029048/Heat shock protein 70kD, C-terminal domain superfamily/homologous_superfamily; IPR043129/ATPase, nucleotide binding domain/homologous_superfamily. Family/domain types are distinguished; membership is not localization evidence. |
| plaque-nur-matches-O74752 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/O74752/?page_size=200; Native JSON response | supports | Integrated InterPro match set count=9, next=None: IPR001305/Heat shock protein DnaJ, cysteine-rich domain/domain; IPR001623/DnaJ domain/domain; IPR002939/Chaperone DnaJ, C-terminal/domain; IPR008971/HSP40/DnaJ peptide-binding/homologous_superfamily; IPR012724/Chaperone DnaJ/family; IPR018253/DnaJ domain, conserved site/conserved_site; IPR036410/Heat shock protein DnaJ, cysteine-rich domain superfamily/homologous_superfamily; IPR036869/Chaperone J-domain superfamily/homologous_superfamily; IPR044713/DnaJ homolog subfamily A member 1/2-like/family. Family/domain types are distinguished; membership is not localization evidence. |
| plaque-nur-matches-O94641 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/O94641/?page_size=200; Native JSON response | supports | Integrated InterPro match set count=11, next=None: IPR001270/ClpA/B family/family; IPR003593/AAA+ ATPase domain/domain; IPR003959/ATPase, AAA-type, core/domain; IPR004176/Clp, repeat (R) N-terminal domain/domain; IPR018368/ClpA/B, conserved site 1/conserved_site; IPR019489/Clp ATPase, C-terminal/domain; IPR027417/P-loop containing nucleoside triphosphate hydrolase/homologous_superfamily; IPR028299/ClpA/B, conserved site 2/conserved_site; IPR036628/Clp, N-terminal domain superfamily/homologous_superfamily; IPR041546/ClpA/ClpB, AAA lid domain/domain; IPR050130/ATP-dependent Clp protease/Chaperone ClpA/ClpB/family. Family/domain types are distinguished; membership is not localization evidence. |
| plaque-nur-IPR011502 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR011502/; Native JSON response | supports | InterPro IPR011502 has name Nucleoporin Nup85-like and type family. Only identity/type is used; unchecked generated descriptions are excluded. |
| plaque-nur-IPR030217 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR030217/; Native JSON response | supports | InterPro IPR030217 has name Nuclear RNA export factor and type family. Only identity/type is used; unchecked generated descriptions are excluded. |
| plaque-nur-IPR044713 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR044713/; Native JSON response | supports | InterPro IPR044713 has name DnaJ homolog subfamily A member 1/2-like and type family. Only identity/type is used; unchecked generated descriptions are excluded. |
| plaque-nur-jats-PMC10342647 | https://pmc-oa-opendata.s3.amazonaws.com/PMC10342647.1/PMC10342647.1.xml; Results2.5; Fig7a-c caption; Methods4.3; JATS exact license and DOI/PMID | supports | Boronat2023 main Results2.5, Fig7 and Methods4.3 support severe-heat NuRs, Mas5-dependent fission-yeast reporters and chaperone localization. Budding-yeast W303/BY4741 experiments and W303-specific concentration are explicitly distinct. |
| plaque-nur-native-package-PMC10342647 | https://pmc-oa-opendata.s3.amazonaws.com/PMC10342647.1/PMC10342647.1.json; PMC article package metadata, DOI/PMID/license and exact figure media MD5 | supports | PMC package PMC10342647 version 1 identifies DOI 10.3390/ijms241311202, PMID 37446379; exact figure media MD5 matches the frozen local bytes. JATS provides exact license version. |
| plaque-kaganovich-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC2746971.1/PMC2746971.1.xml; Primary article Results S3/S4/S6; Figures4-6 captions; DOI/PMID metadata | supports | Kaganovich2008 primary Results S4/S6 support historical JUNQ-designated proteasome/Hsp104 association and cooling-dependent diffuse Ubc9Ts fluorescence recovery. These historical assignments and fluorescence readouts do not prove universal modern JUNQ composition or catalytic reactivation. |
| plaque-catalogue | https://imodulondb.org/api/datasets; Entire returned organism and dataset listing | context_only | Fresh catalogue contains 20 organisms and 28 dataset keys. Every returned organism row was inspected; no Saccharomyces or Schizosaccharomyces dataset is listed. No matched gene/module lookup is warranted for these yeast targets; unrelated bacterial Hsp homologs are not substitutes. |
| plaque-btn2-domain | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR062150/; Native JSON response | supports | InterPro IPR062150 has name BTN2-like, N-terminal domain and type domain. Only identity/type is used; unchecked generated descriptions are excluded. |
| plaque-gallardo-browser-retrieval | https://www.researchgate.net/publication/346538874_Acute_Heat_Stress_Leads_to_Reversible_Aggregation_of_Nuclear_Proteins_into_Nucleolar_Rings_in_Fission_Yeast; Browser-extracted primary article body and captions; frozen retrieval JSON /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-plaque/gallardo-browser-retrieval.json | supports | Primary paper text recovered through browser extraction: selective nuclear recruitment, reduced Nup85/Mex67 mobility, heat/recovery, residual preconditioning and Hsf1/Hsp104 perturbations agree with the bounded record. Origin repository returned an HTML shell; no PDF or supplemental pixels were read. |
| plaque-hiraoka-browser-retrieval | https://www.researchgate.net/publication/370466123_CDK_actively_contributes_to_establishment_of_the_stationary_phase_state_in_fission_yeast; Browser-extracted primary article body and captions; frozen retrieval JSON /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-plaque/hiraoka-browser-retrieval.json | supports | Primary paper text recovered through browser extraction: Fig3/Results distinguish peripheral Cdc2/Cdc13/Clp1 from central Gar1/Gar2 during stationary phase/glucose depletion. This supports starvation scope without equating it mechanistically with acute heat; publisher and curl host requests returned403. |
| plaque-source-access-limitations | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-plaque/source-receipts.json; Actual fresh curl receipts/statuses and body hashes; extra-source-receipts.json records later alternatives | context_only | Nine EuropePMC metadata requests returned503; the direct IPR013126 entry returned429, but both exact Ssa protein integrated-match lists independently returned the family identity/name/type. Miller S3 JATS404 was replaced by full PMC HTML. Gallardo repository responses were HTML shells and publisher403; Hiraoka curl endpoints403. Browser primary text fallbacks are separate evidence, not successful origin downloads. |
| plaque-original-validation | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-plaque/original-validation.json; Three original native validate/render executions and all historical source.inputs checked with git show | supports | Each original validates with exit0, deterministic render matches saved Markdown exactly, and every frozen historical input hash matches its original source commit. Historical checks remain historical and are not presented as fresh scientific review. |
| plaque-native-intranuclear_quality_control_compartment-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/intranuclear_quality_control_compartment-uniprot-verify-receipt.json; Actual receipt and independently inspected /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/intranuclear_quality_control_compartment-uniprot-verify.log | supports | Root-executed native command exit0, independently read receipt/log and verified exact source head and stdout hash. All declared UniProt examples and causal xrefs verify; scientific residence remains primary-source dependent. |
| plaque-native-intranuclear_quality_control_compartment-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/intranuclear_quality_control_compartment-uniprot-causal-receipt.json; Actual receipt and independently inspected /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/intranuclear_quality_control_compartment-uniprot-causal.log | supports | Root-executed native command exit0, independently read receipt/log and verified exact source head and stdout hash. No GENE_OR_PROTEIN graph nodes occur: interventions are STATE or experimental/environmental factors, not ungrounded protein entities; this empty applicable graph subset does not validate scientific edges. |
| plaque-native-juxtanuclear_quality_control_compartment-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/juxtanuclear_quality_control_compartment-uniprot-verify-receipt.json; Actual receipt and independently inspected /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/juxtanuclear_quality_control_compartment-uniprot-verify.log | supports | Root-executed native command exit0, independently read receipt/log and verified exact source head and stdout hash. All declared UniProt examples and causal xrefs verify; scientific residence remains primary-source dependent. |
| plaque-native-juxtanuclear_quality_control_compartment-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/juxtanuclear_quality_control_compartment-uniprot-causal-receipt.json; Actual receipt and independently inspected /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/juxtanuclear_quality_control_compartment-uniprot-causal.log | supports | Root-executed native command exit0, independently read receipt/log and verified exact source head and stdout hash. No GENE_OR_PROTEIN graph nodes occur: interventions are STATE or experimental/environmental factors, not ungrounded protein entities; this empty applicable graph subset does not validate scientific edges. |
| plaque-native-nucleolar_peripheral_inclusion_body-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/nucleolar_peripheral_inclusion_body-uniprot-verify-receipt.json; Actual receipt and independently inspected /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/nucleolar_peripheral_inclusion_body-uniprot-verify.log | supports | Root-executed native command exit0, independently read receipt/log and verified exact source head and stdout hash. All declared UniProt examples and causal xrefs verify; scientific residence remains primary-source dependent. |
| plaque-native-nucleolar_peripheral_inclusion_body-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/nucleolar_peripheral_inclusion_body-uniprot-causal-receipt.json; Actual receipt and independently inspected /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/nucleolar_peripheral_inclusion_body-uniprot-causal.log | supports | Root-executed native command exit0, independently read receipt/log and verified exact source head and stdout hash. No GENE_OR_PROTEIN graph nodes occur: interventions are STATE or experimental/environmental factors, not ungrounded protein entities; this empty applicable graph subset does not validate scientific edges. |
| micro-age2015-primary | https://pmc-oa-opendata.s3.amazonaws.com/PMC4635334.1/PMC4635334.1.xml; Saarikangas and Barral 2015 DOI:10.7554/eLife.06197; JATS front, Results s2-1 through s2-7, Discussion s3, Methods s4-1 through s4-7; figure captions including Figure6 and supplement Figure1-2; permissions; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/PMC4635334.raw; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/PMC4635334.receipt.json | supports | The primary body supports persistent mother-retained age deposits, Hsp42-dependent assembly, Hsp104-independent formation with enhanced deposits when Hsp104 is lost, opposite Hsp42/Hsp104 overexpression effects, individual SSA1/SSA2 deletion phenotypes, variable Hsp26 and prion-state-dependent Sup35 association. S288C/W303 imaging contexts and functional assays are not universal prevalence or complete native composition evidence. No raw microscopy or videos reanalyzed. |
| micro-age2017-primary | https://kclpure.kcl.ac.uk/ws/files/67186035/Saarikangas_et_al.pdf; Saarikangas et al. 2017 DOI:10.1016/j.cub.2017.01.069; accepted manuscript PDF physical pp4–19 (Summary through Methods), pp22–24 figure legends, pp37–39 supplemental methods/strain table; Figure S5 physical pp35–36 rendered and directly viewed; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/saarikangas2017.raw; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/saarikangas2017.receipt.json | supports | Primary text supports ER association, observed intranuclear subset, PRM3-dependent fusion context, daughter-deposit changes after BUD1/SUR2/BUD6 or YDJ1-C406S perturbation, and the proposed precursor-confinement model. S5 pixels show N-terminal GFP-Ydj1 enrichment in 9.4% of 53 scored cells, with one scored Hsp104 deposit per cell, and preserved 99.5% ER apposition in both wild type and C406S. This does not establish Ydj1 as a universal mature-deposit coat or identify its bound precursor clients. Other figure pixels and original movies were not inspected. |
| micro-age2025-primary | https://pmc-oa-opendata.s3.amazonaws.com/PMC11849620.1/PMC11849620.1.xml; DOI:10.1016/j.jbc.2025.108172; JATS front, Results sec1.1–sec1.3, Methods sec2.1/sec2.4 and Data sec3; Figure3–5 captions; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/PMC11849620.raw; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/PMC11849620.receipt.json | supports | BY4741 aging experiments support higher age-associated foci after NPR3 deletion and lower after TCO89 deletion, and a young-versus-old response to translation inhibition. Figure5A versus Methods retain the 0.25 versus 250 micrograms/mL cycloheximide discrepancy; old isolated cells have median 12 divisions. Loss of visible Hsp104 foci is not direct proteolytic clearance. Acute pro3-1 screening and aging experiments are distinguished. No image pixels or supplementary datasets were reanalyzed. |
| micro-age2018-secondary-nomenclature | https://pmc-oa-opendata.s3.amazonaws.com/PMC6064742.1/PMC6064742.1.xml; DOI:10.3389/fnmol.2018.00249; JATS front and Figure1 caption only; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/PMC6064742.raw; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/PMC6064742.receipt.json | context_only | Secondary review Figure1 explicitly expands APOD as age-associated protein deposit. Used only for nomenclature/background, not as primary experimental support for formation, necessity or ER localization. No image pixels inspected. |
| micro-ipod2008-primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC2746971/?pdf=render; Kaganovich et al. DOI:10.1038/nature07195; authentic PMC2746971 HTML title/abstract, main narrative and figure captions, Methods Summary; derived zero-based paragraphs P12–P66; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/extra/kaganovich2008-body.raw; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/extra/kaganovich2008-body.receipt.json | supports | Primary source distinguishes poorly mobile perivacuolar IPOD from soluble JUNQ, associates Hsp104 and Atg8 while separating PAS/autophagy claims, and reports that Ubc9ts in IPOD did not regain diffuse fluorescence in its recovery assay. This assay does not prohibit slower turnover of another substrate under the later Kumar conditions. Mammalian comparison does not automatically extend this yeast record to every taxon. Supplementary files/full online Methods and image pixels were not inspected. |
| micro-ipod2016-primary | https://pmc-oa-opendata.s3.amazonaws.com/PMC5045159.1/PMC5045159.1.xml; Kumar et al. DOI:10.1371/journal.pgen.1006324; JATS front, Results sec003–sec009, Discussion sec011–sec013, Methods sec016/sec024, Figure3 caption and permissions; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/PMC5045159.raw; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/PMC5045159.receipt.json | supports | Primary body supports 74D-694-derived PrD-GFP recruitment requiring tested Myo2/tropomyosin/Sec18 functions, recovery after depletion ends, and preservation of preformed deposits. Shared vesicular delivery and tethering are proposed models, not direct establishment of each factor as a resident component. Slowly extracted PrD-GFP requires Hsp104 activity; MG132 reduces but does not eliminate turnover, and bulk autophagy is not established. Engineered Sup35 PrD cargo is not equated to a fixed full-length native subunit. |
| micro-ipod2024-primary | https://pmc-oa-opendata.s3.amazonaws.com/PMC10931478.1/PMC10931478.1.xml; Carter et al. DOI:10.1371/journal.pgen.1011194; JATS front, Results sec011 and Methods sec015/sec016/sec018; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/PMC10931478.raw; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/PMC10931478.receipt.json | supports | 74D-694-derived cells treated with 0.8mM hydrogen peroxide for one hour show ABP1-dependent increased prion formation in wild type but not the same requirement in btn2 hsp42 mutants. The source supports a genotype/assay-specific counterexample to universal IPOD necessity, not universal absence of IPOD function. Prion frequency was phenotyped and confirmed through guanidine curing. No figure pixels or raw datasets inspected. |
| micro-mitostore2023-primary | https://pmc-oa-opendata.s3.amazonaws.com/PMC10068336.1/PMC10068336.1.xml; Kraemer et al. DOI:10.15252/embj.2022112309; JATS front, Results sec0003–sec0008, Discussion sec0009, Methods sec0011/sec0012/sec0016–sec0019, Figures5–6 captions and permissions; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/PMC10068336.raw; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/PMC10068336.receipt.json | supports | Primary text supports cytosolic, mitochondrial-surface-associated precursor granules in lactate-grown and clogger-stressed yeast. Separate HSP42 and HSP104 deletions block tested Aim17 granules; Hsp26 is co-purification evidence without equal necessity/localization evidence. Presequence deletion affects Mam33 recruitment. After 4.5h induction and 4h chase, split-GFP supports matrix import competence without tracking individual proteins continuously from a granule. RPN4 deletion and chaperone dependence concern the tested clogger survival context. Hsp104 IP analysis reports 1154 filtered proteins, distinct from the 3550 whole-cell proteome and archive metadata. No raw MS, supplementary strain workbook, extended-figure pixels or original videos reanalyzed. |
| micro-mitostore-tom70-comparison | https://pmc-oa-opendata.s3.amazonaws.com/PMC10401023.1/PMC10401023.1.xml; Liu et al. DOI:10.1073/pnas.2300475120; JATS front, Results s2, Discussion s7; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/PMC10401023.raw; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/PMC10401023.receipt.json | context_only | The primary study tests Tom70-associated heat-induced aggregate recruitment and discusses similarities to MitoStores. Similarities in precursor content, chaperones and mitochondrial association do not establish exact identity or transfer every Tom70 mechanism to the Kraemer granules. Only the indicated Results subsection and full Discussion were read; other result sections and image pixels were not inspected. |
| micro-pride-mitostore | https://www.ebi.ac.uk/pride/ws/archive/v2/projects/PXD035762; PRIDE PXD035762 exact project object; accession/title/description, organism, dataProcessingProtocol and references; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/PXD035762.raw; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/PXD035762.receipt.json | context_only | Current title/description identify the MitoStore Hsp104 AP-MS dataset, but the references still point to the Ubc8 paper DOI:10.26508/LSA.202201526, and processing text says 2920 filtered proteins versus 1154 in the primary IP analysis. The record explicitly preserves these inconsistencies and uses archive provenance without inventing a full native inventory, sample count or corrected citation. Raw MS files were not downloaded. |
| micro-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0016234,GO:0140453,GO:0005737; QuickGO exact GO:0005737/GO:0016234/GO:0140453 objects, names/definitions/obsoletion flags; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/go.raw; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/go.receipt.json | supports | Cytoplasm and inclusion body resolve as active component terms; protein aggregate center has a reversible thermosensitive-protein sequestration definition and is not an exact identity replacement for all three records. Age deposits preserve uncertain intranuclear location rather than asserting universal cytoplasmic parthood; IPOD and MitoStore cytosolic location agrees with primary studies. |
| micro-go-query-APOD | https://www.ebi.ac.uk/ols4/api/search?ontology=go&amp;exact=true&amp;rows=100&amp;q=APOD; OLS4 GO-scoped search response; exact=true; q=APOD; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/go-query-APOD.raw; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/go-query-APOD.receipt.json | context_only | Returned 1 documents; APOD hits an imported pulmonary interstitial fibroblast term through marker text, not an exact deposit cellular-component identity. This is not a universal ontology absence claim. |
| micro-go-query-Agepod | https://www.ebi.ac.uk/ols4/api/search?ontology=go&amp;exact=true&amp;rows=100&amp;q=Agepod; OLS4 GO-scoped search response; exact=true; q=Agepod; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/go-query-Agepod.raw; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/go-query-Agepod.receipt.json | context_only | Returned 0 documents; no exact identity candidate in this bounded query response. This is not a universal ontology absence claim. |
| micro-go-query-IPOD | https://www.ebi.ac.uk/ols4/api/search?ontology=go&amp;exact=true&amp;rows=100&amp;q=IPOD; OLS4 GO-scoped search response; exact=true; q=IPOD; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/go-query-IPOD.raw; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/go-query-IPOD.receipt.json | context_only | Returned 0 documents; no exact identity candidate in this bounded query response. This is not a universal ontology absence claim. |
| micro-go-query-MitoStore | https://www.ebi.ac.uk/ols4/api/search?ontology=go&amp;exact=true&amp;rows=100&amp;q=MitoStore; OLS4 GO-scoped search response; exact=true; q=MitoStore; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/go-query-MitoStore.raw; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/go-query-MitoStore.receipt.json | context_only | Returned 0 documents; no exact identity candidate in this bounded query response. This is not a universal ontology absence claim. |
| micro-go-query-MitoStores | https://www.ebi.ac.uk/ols4/api/search?ontology=go&amp;exact=true&amp;rows=100&amp;q=MitoStores; OLS4 GO-scoped search response; exact=true; q=MitoStores; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/go-query-MitoStores.raw; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/go-query-MitoStores.receipt.json | context_only | Returned 0 documents; no exact identity candidate in this bounded query response. This is not a universal ontology absence claim. |
| micro-go-query-age-associated_protein_deposit | https://www.ebi.ac.uk/ols4/api/search?ontology=go&amp;exact=true&amp;rows=100&amp;q=age-associated+protein+deposit; OLS4 GO-scoped search response; exact=true; q=age-associated protein deposit; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/go-query-age-associated_protein_deposit.raw; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/go-query-age-associated_protein_deposit.receipt.json | context_only | Returned 0 documents; no exact identity candidate in this bounded query response. This is not a universal ontology absence claim. |
| micro-go-query-insoluble_protein_deposit | https://www.ebi.ac.uk/ols4/api/search?ontology=go&amp;exact=true&amp;rows=100&amp;q=insoluble+protein+deposit; OLS4 GO-scoped search response; exact=true; q=insoluble protein deposit; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/go-query-insoluble_protein_deposit.raw; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/go-query-insoluble_protein_deposit.receipt.json | context_only | Returned 0 documents; no exact identity candidate in this bounded query response. This is not a universal ontology absence claim. |
| micro-tax-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; ENA taxonomy exact taxId/scientificName/rank/lineage fields; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/tax-4932.raw; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/tax-4932.receipt.json | supports | 4932 resolves to Saccharomyces cerevisiae, rank species. Authority identity is separate from primary-paper experimental strain evidence; 74D-694 and YPH499 derivative genotypes are not silently replaced by S288C. |
| micro-tax-559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; ENA taxonomy exact taxId/scientificName/rank/lineage fields; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/tax-559292.raw; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/tax-559292.receipt.json | supports | 559292 resolves to Saccharomyces cerevisiae S288C, rank strain. Authority identity is separate from primary-paper experimental strain evidence; 74D-694 and YPH499 derivative genotypes are not silently replaced by S288C. |
| micro-tax-1247190 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1247190; ENA taxonomy exact taxId/scientificName/rank/lineage fields; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/tax-1247190.raw; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/tax-1247190.receipt.json | supports | 1247190 resolves to Saccharomyces cerevisiae BY4741, rank strain. Authority identity is separate from primary-paper experimental strain evidence; 74D-694 and YPH499 derivative genotypes are not silently replaced by S288C. |
| micro-uniprot-Q12329 | https://rest.uniprot.org/uniprotkb/Q12329.json; UniProt exact accession entryType/primaryAccession/proteinDescription/genes/organism; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/Q12329.raw; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/Q12329.receipt.json | supports | Reviewed S. cerevisiae S288C taxon559292 record maps Q12329 to HSP42; locus and displayed name checked. Identity does not establish localization, native stoichiometry or requirement for deposit formation. |
| micro-query-HSP42 | https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A559292+AND+gene_exact%3AHSP42&amp;format=json&amp;size=500; Exact reviewed gene query; returned accession/primary gene/taxon; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/query-HSP42.raw; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/query-HSP42.receipt.json | supports | The single returned reviewed S288C hit is Q12329 (HSP42); no unresolved symbol or alternative accession in this bounded response. |
| micro-matches-Q12329 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q12329/?page_size=200; InterPro entries by exact UniProt accession, page_size200; metadata accession/name/type and next/count; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/matches-Q12329.raw; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/matches-Q12329.receipt.json | supports | All 3 returned assignments inspected; next=null. IPR002068 Alpha crystallin/Hsp20 domain (domain); IPR008978 HSP20-like chaperone (homologous_superfamily); IPR031107 Small heat shock protein (family). Family/domain/superfamily types and broad-family scope are kept separate; no necessity inference from sequence assignment. |
| micro-uniprot-P15992 | https://rest.uniprot.org/uniprotkb/P15992.json; UniProt exact accession entryType/primaryAccession/proteinDescription/genes/organism; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/P15992.raw; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/P15992.receipt.json | supports | Reviewed S. cerevisiae S288C taxon559292 record maps P15992 to HSP26; locus and displayed name checked. Identity does not establish localization, native stoichiometry or requirement for deposit formation. |
| micro-query-HSP26 | https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A559292+AND+gene_exact%3AHSP26&amp;format=json&amp;size=500; Exact reviewed gene query; returned accession/primary gene/taxon; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/query-HSP26.raw; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/query-HSP26.receipt.json | supports | The single returned reviewed S288C hit is P15992 (HSP26); no unresolved symbol or alternative accession in this bounded response. |
| micro-matches-P15992 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P15992/?page_size=200; InterPro entries by exact UniProt accession, page_size200; metadata accession/name/type and next/count; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/matches-P15992.raw; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/matches-P15992.receipt.json | supports | All 3 returned assignments inspected; next=null. IPR002068 Alpha crystallin/Hsp20 domain (domain); IPR008978 HSP20-like chaperone (homologous_superfamily); IPR031107 Small heat shock protein (family). Family/domain/superfamily types and broad-family scope are kept separate; no necessity inference from sequence assignment. |
| micro-uniprot-P31539 | https://rest.uniprot.org/uniprotkb/P31539.json; UniProt exact accession entryType/primaryAccession/proteinDescription/genes/organism; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/P31539.raw; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/P31539.receipt.json | supports | Reviewed S. cerevisiae S288C taxon559292 record maps P31539 to HSP104; locus and displayed name checked. Identity does not establish localization, native stoichiometry or requirement for deposit formation. |
| micro-query-HSP104 | https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A559292+AND+gene_exact%3AHSP104&amp;format=json&amp;size=500; Exact reviewed gene query; returned accession/primary gene/taxon; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/query-HSP104.raw; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/query-HSP104.receipt.json | supports | The single returned reviewed S288C hit is P31539 (HSP104); no unresolved symbol or alternative accession in this bounded response. |
| micro-matches-P31539 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P31539/?page_size=200; InterPro entries by exact UniProt accession, page_size200; metadata accession/name/type and next/count; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/matches-P31539.raw; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/matches-P31539.receipt.json | supports | All 11 returned assignments inspected; next=null. IPR001270 ClpA/B family (family); IPR003593 AAA+ ATPase domain (domain); IPR003959 ATPase, AAA-type, core (domain); IPR004176 Clp, repeat (R) N-terminal domain (domain); IPR018368 ClpA/B, conserved site 1 (conserved_site); IPR019489 Clp ATPase, C-terminal (domain); IPR027417 P-loop containing nucleoside triphosphate hydrolase (homologous_superfamily); IPR028299 ClpA/B, conserved site 2 (conserved_site); IPR036628 Clp, N-terminal domain superfamily (homologous_superfamily); IPR041546 ClpA/ClpB, AAA lid domain (domain); IPR050130 ATP-dependent Clp protease/Chaperone ClpA/ClpB (family). Family/domain/superfamily types and broad-family scope are kept separate; no necessity inference from sequence assignment. |
| micro-uniprot-P10591 | https://rest.uniprot.org/uniprotkb/P10591.json; UniProt exact accession entryType/primaryAccession/proteinDescription/genes/organism; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/P10591.raw; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/P10591.receipt.json | supports | Reviewed S. cerevisiae S288C taxon559292 record maps P10591 to SSA1; locus and displayed name checked. Identity does not establish localization, native stoichiometry or requirement for deposit formation. |
| micro-query-SSA1 | https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A559292+AND+gene_exact%3ASSA1&amp;format=json&amp;size=500; Exact reviewed gene query; returned accession/primary gene/taxon; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/query-SSA1.raw; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/query-SSA1.receipt.json | supports | The single returned reviewed S288C hit is P10591 (SSA1); no unresolved symbol or alternative accession in this bounded response. |
| micro-matches-P10591 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P10591/?page_size=200; InterPro entries by exact UniProt accession, page_size200; metadata accession/name/type and next/count; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/matches-P10591.raw; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/matches-P10591.receipt.json | supports | All 5 returned assignments inspected; next=null. IPR013126 Heat shock protein 70 family (family); IPR018181 Heat shock protein 70, conserved site (conserved_site); IPR029047 Heat shock protein 70kD, peptide-binding domain superfamily (homologous_superfamily); IPR029048 Heat shock protein 70kD, C-terminal domain superfamily (homologous_superfamily); IPR043129 ATPase, nucleotide binding domain (homologous_superfamily). Family/domain/superfamily types and broad-family scope are kept separate; no necessity inference from sequence assignment. |
| micro-uniprot-P10592 | https://rest.uniprot.org/uniprotkb/P10592.json; UniProt exact accession entryType/primaryAccession/proteinDescription/genes/organism; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/P10592.raw; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/P10592.receipt.json | supports | Reviewed S. cerevisiae S288C taxon559292 record maps P10592 to SSA2; locus and displayed name checked. Identity does not establish localization, native stoichiometry or requirement for deposit formation. |
| micro-query-SSA2 | https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A559292+AND+gene_exact%3ASSA2&amp;format=json&amp;size=500; Exact reviewed gene query; returned accession/primary gene/taxon; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/query-SSA2.raw; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/query-SSA2.receipt.json | supports | The single returned reviewed S288C hit is P10592 (SSA2); no unresolved symbol or alternative accession in this bounded response. |
| micro-matches-P10592 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P10592/?page_size=200; InterPro entries by exact UniProt accession, page_size200; metadata accession/name/type and next/count; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/matches-P10592.raw; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/matches-P10592.receipt.json | supports | All 5 returned assignments inspected; next=null. IPR013126 Heat shock protein 70 family (family); IPR018181 Heat shock protein 70, conserved site (conserved_site); IPR029047 Heat shock protein 70kD, peptide-binding domain superfamily (homologous_superfamily); IPR029048 Heat shock protein 70kD, C-terminal domain superfamily (homologous_superfamily); IPR043129 ATPase, nucleotide binding domain (homologous_superfamily). Family/domain/superfamily types and broad-family scope are kept separate; no necessity inference from sequence assignment. |
| micro-uniprot-P25491 | https://rest.uniprot.org/uniprotkb/P25491.json; UniProt exact accession entryType/primaryAccession/proteinDescription/genes/organism; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/P25491.raw; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/P25491.receipt.json | supports | Reviewed S. cerevisiae S288C taxon559292 record maps P25491 to YDJ1; locus and displayed name checked. Identity does not establish localization, native stoichiometry or requirement for deposit formation. |
| micro-query-YDJ1 | https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A559292+AND+gene_exact%3AYDJ1&amp;format=json&amp;size=500; Exact reviewed gene query; returned accession/primary gene/taxon; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/query-YDJ1.raw; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/query-YDJ1.receipt.json | supports | The single returned reviewed S288C hit is P25491 (YDJ1); no unresolved symbol or alternative accession in this bounded response. |
| micro-matches-P25491 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P25491/?page_size=200; InterPro entries by exact UniProt accession, page_size200; metadata accession/name/type and next/count; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/matches-P25491.raw; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/matches-P25491.receipt.json | supports | All 9 returned assignments inspected; next=null. IPR001305 Heat shock protein DnaJ, cysteine-rich domain (domain); IPR001623 DnaJ domain (domain); IPR002939 Chaperone DnaJ, C-terminal (domain); IPR008971 HSP40/DnaJ peptide-binding (homologous_superfamily); IPR012724 Chaperone DnaJ (family); IPR018253 DnaJ domain, conserved site (conserved_site); IPR036410 Heat shock protein DnaJ, cysteine-rich domain superfamily (homologous_superfamily); IPR036869 Chaperone J-domain superfamily (homologous_superfamily); IPR044713 DnaJ homolog subfamily A member 1/2-like (family). Family/domain/superfamily types and broad-family scope are kept separate; no necessity inference from sequence assignment. |
| micro-uniprot-P05453 | https://rest.uniprot.org/uniprotkb/P05453.json; UniProt exact accession entryType/primaryAccession/proteinDescription/genes/organism; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/P05453.raw; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/P05453.receipt.json | supports | Reviewed S. cerevisiae S288C taxon559292 record maps P05453 to SUP35; locus and displayed name checked. Identity does not establish localization, native stoichiometry or requirement for deposit formation. |
| micro-query-SUP35 | https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A559292+AND+gene_exact%3ASUP35&amp;format=json&amp;size=500; Exact reviewed gene query; returned accession/primary gene/taxon; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/query-SUP35.raw; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/query-SUP35.receipt.json | supports | The single returned reviewed S288C hit is P05453 (SUP35); no unresolved symbol or alternative accession in this bounded response. |
| micro-matches-P05453 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P05453/?page_size=200; InterPro entries by exact UniProt accession, page_size200; metadata accession/name/type and next/count; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/matches-P05453.raw; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/matches-P05453.receipt.json | supports | All 9 returned assignments inspected; next=null. IPR000795 Translational (tr)-type GTP-binding domain (domain); IPR003285 Eukaryotic peptide chain release factor GTP-binding subunit (family); IPR004161 Translation elongation factor EFTu-like, domain 2 (domain); IPR009000 Translation protein, beta-barrel domain superfamily (homologous_superfamily); IPR009001 Translation elongation factor EF1A/initiation factor IF2gamma, C-terminal (homologous_superfamily); IPR027417 P-loop containing nucleoside triphosphate hydrolase (homologous_superfamily); IPR031157 Tr-type G domain, conserved site (conserved_site); IPR050100 Translation factor GTPase superfamily members (family); IPR054696 GTP-eEF1A, C-terminal domain (domain). Family/domain/superfamily types and broad-family scope are kept separate; no necessity inference from sequence assignment. |
| micro-family-IPR031107 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR031107/; InterPro exact entry metadata name/type/hierarchy; functional descriptions used only as classification context; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/IPR031107.raw; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/IPR031107.receipt.json | supports | IPR031107 is a family: Small heat shock protein. The small-HSP, Hsp70 and Sup35/eRF3 labels match the declared families. ClpA/B entries are broader than a yeast Hsp104-specific class and remain unassigned as exact component family groundings. No sequence-family entry establishes deposit residence or necessity. IPR050130 unreviewed machine-generated functional prose is not used for scientific support. |
| micro-family-IPR013126 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013126/; InterPro exact entry metadata name/type/hierarchy; functional descriptions used only as classification context; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/IPR013126.raw; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/IPR013126.receipt.json | supports | IPR013126 is a family: Heat shock protein 70 family. The small-HSP, Hsp70 and Sup35/eRF3 labels match the declared families. ClpA/B entries are broader than a yeast Hsp104-specific class and remain unassigned as exact component family groundings. No sequence-family entry establishes deposit residence or necessity. IPR050130 unreviewed machine-generated functional prose is not used for scientific support. |
| micro-family-IPR003285 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR003285/; InterPro exact entry metadata name/type/hierarchy; functional descriptions used only as classification context; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/IPR003285.raw; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/IPR003285.receipt.json | supports | IPR003285 is a family: Eukaryotic peptide chain release factor GTP-binding subunit. The small-HSP, Hsp70 and Sup35/eRF3 labels match the declared families. ClpA/B entries are broader than a yeast Hsp104-specific class and remain unassigned as exact component family groundings. No sequence-family entry establishes deposit residence or necessity. IPR050130 unreviewed machine-generated functional prose is not used for scientific support. |
| micro-family-IPR001270 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001270/; InterPro exact entry metadata name/type/hierarchy; functional descriptions used only as classification context; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/IPR001270.raw; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/IPR001270.receipt.json | supports | IPR001270 is a family: ClpA/B family. The small-HSP, Hsp70 and Sup35/eRF3 labels match the declared families. ClpA/B entries are broader than a yeast Hsp104-specific class and remain unassigned as exact component family groundings. No sequence-family entry establishes deposit residence or necessity. IPR050130 unreviewed machine-generated functional prose is not used for scientific support. |
| micro-family-IPR050130 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050130/; InterPro exact entry metadata name/type/hierarchy; functional descriptions used only as classification context; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/extra/IPR050130.raw; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/extra/IPR050130.receipt.json | supports | IPR050130 is a family: ATP-dependent Clp protease/Chaperone ClpA/ClpB. The small-HSP, Hsp70 and Sup35/eRF3 labels match the declared families. ClpA/B entries are broader than a yeast Hsp104-specific class and remain unassigned as exact component family groundings. No sequence-family entry establishes deposit residence or necessity. IPR050130 unreviewed machine-generated functional prose is not used for scientific support. |
| micro-adapter-catalogue | https://imodulondb.org/api/datasets; iModulonDB /api/datasets complete returned catalogue object array; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/datasets.raw; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/datasets.receipt.json | context_only | Fresh catalogue contains20 organism entries and28 named datasets; none matches Saccharomyces cerevisiae or its S288C/BY4741 strains. These records name yeast chaperones, cargo and stress responses, so applicability must be examined. In the inspected catalogue no matched organism/dataset exists: downstream gene/module/activity checks are not applicable for this cohort. This is not negative biological evidence, and recombinant expression hosts in source methods do not change the curated target taxon. |
| micro-historical-adapter-runner | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical shared runner attempt, not a PR2356 execution | context_only | Retained command ['/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources', 'imodulondb', 'datasets'] ran 2026-11-03T00:49:00.848907+00:00 to 2026-11-03T00:49:00.863225+00:00, exit1, unavailable due to PermissionError reading pyvenv.cfg. Current review uses fresh inspected source catalogue fallback; no current runner success or fresh invocation is claimed. |
| micro-review-policy | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/repo/.claude/skills/review-yaml-record/SKILL.md; Structured Source Cross-Checks and immutable review workflow | supports | Named protein/stress-response records require actual shared-source applicability; lack of an expression claim is not an exemption. Current catalogue-based no-covered-dataset result permits a bounded N/A conclusion. Original reviews remain immutable and current evidence is saved in a successor observation. |
| micro-review-config | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/repo/conf/record_review.yaml; Exact frozen repository skills/rubrics routing | supports | Repository-native skill, literature and curation checklist routing is retained. Byte identity with the previously inspected configuration was verified before current assessment; no new configuration semantics inferred. |
| micro-original-validation-inputs | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/original-validation-inputs.json; All3 original frozen hashes against their declared source revision, current hashes and native validate/render receipts | supports | All3 original native validations and render comparisons passed. Age target bytes unchanged; IPOD and MitoStore changed only two self-node groundings plus curation history. A current assessment is required for stale inputs even when scientific claims are unchanged. Original finding lists are empty; no scientific issue lineage is fabricated. |
| micro-record-age_associated_protein_deposit | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/repo/data/structures/inclusion/age_associated_protein_deposit.yaml; Entire current YAML, definitions/components/graphs/evidence/discussions/provenance | supports | Current frozen record inspected in full; its identity, source scope, experimental qualifications and evidence tiers were independently reassessed. Unchanged since the original observation. |
| micro-prior-age_associated_protein_deposit | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/repo/reviews/structured/20261021T103319Z-age-associated-protein-deposit-audit/review.yaml; Entire original YAML observation, checks/assessments/evidence/verdict/findings; paired rendered Markdown validated | supports | Original pass_with_limitations observation has no scientific findings. Its target hash remains current. Scientific support is freshly rechecked here; old source access times are not presented as new reads. |
| micro-native-age_associated_protein_deposit-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/age_associated_protein_deposit-uniprot-verify-receipt.json; .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/age_associated_protein_deposit.yaml --verify; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/age_associated_protein_deposit-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Current-source command passed, started2026-11-03T08:11:02.535921+00:00, finished2026-11-03T08:11:04.222793+00:00, exit0. Seven concrete protein examples verified; all graph perturbations are outside the GENE_OR_PROTEIN inventory and causal scan has zero such nodes. These mechanical checks do not verify biological necessity, all graph intervention factors or a complete cargo inventory. |
| micro-native-age_associated_protein_deposit-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/age_associated_protein_deposit-uniprot-causal-receipt.json; .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/age_associated_protein_deposit.yaml --causal-graphs; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/age_associated_protein_deposit-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Current-source command passed, started2026-11-03T08:11:04.255089+00:00, finished2026-11-03T08:11:04.682617+00:00, exit0. Seven concrete protein examples verified; all graph perturbations are outside the GENE_OR_PROTEIN inventory and causal scan has zero such nodes. These mechanical checks do not verify biological necessity, all graph intervention factors or a complete cargo inventory. |
| micro-image-age_associated_protein_deposit | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/repo/data/images/inclusion/age_associated_protein_deposit/pmc4635334_fig6.jpg; Original-resolution tracked JPEG directly viewed; complete stated figure panels; local SHA matches frozen input | supports | Direct pixels agree with the record caption: Figure6A–G distinguishes separate SSA1/SSA2 mutants, Hsp42 assembly and Hsp104 overexpression, scale5micrometers. Caption and primary permission statement checked separately; no raw image reanalysis claimed. |
| micro-image-package-age_associated_protein_deposit | https://pmc-oa-opendata.s3.amazonaws.com/PMC4635334.1/PMC4635334.1.json; Fresh PMC open-access media package metadata, retraction flag and exact figure JPEG entry; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/package-PMC4635334.raw; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/package-PMC4635334.receipt.json | supports | The package is not marked retracted and its figure media MD5 matches the frozen tracked JPEG: a26e590300e4ac72bb1981eb94f99db9. The primary JATS permissions state CC BY4.0; package metadata alone is not a substitute for pixel inspection. |
| micro-record-insoluble_protein_deposit | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/repo/data/structures/inclusion/insoluble_protein_deposit.yaml; Entire current YAML, definitions/components/graphs/evidence/discussions/provenance | supports | Current frozen record inspected in full; its identity, source scope, experimental qualifications and evidence tiers were independently reassessed. The added STRUCTURE self-node groundings resolve to this exact record identity; scientific mechanisms are otherwise unchanged. |
| micro-prior-insoluble_protein_deposit | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/repo/reviews/structured/20261021T103322Z-insoluble-protein-deposit-audit/review.yaml; Entire original YAML observation, checks/assessments/evidence/verdict/findings; paired rendered Markdown validated | supports | Original pass_with_limitations observation has no scientific findings. Its frozen target hash is historical and differs from current; do not silently rewrite it. Scientific support is freshly rechecked here; old source access times are not presented as new reads. |
| micro-native-insoluble_protein_deposit-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/insoluble_protein_deposit-uniprot-verify-receipt.json; .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/insoluble_protein_deposit.yaml --verify; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/insoluble_protein_deposit-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Current-source command passed, started2026-11-03T08:11:09.262171+00:00, finished2026-11-03T08:11:10.947097+00:00, exit0. One concrete Hsp104 example verified; graph scan has one COVERED Hsp104 node and one NO_GENE_SYMBOLS heterogeneous PrD cargo node, not a dangling or ungrounded named protein. These mechanical checks do not verify biological necessity, all graph intervention factors or a complete cargo inventory. |
| micro-native-insoluble_protein_deposit-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/insoluble_protein_deposit-uniprot-causal-receipt.json; .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/insoluble_protein_deposit.yaml --causal-graphs; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/insoluble_protein_deposit-uniprot-causal.log SHA256 8e60d37b122caf9871b8b643517f9c62e3c33ff73a4f68b3cf8cf5b227bed12e | supports | Current-source command passed, started2026-11-03T08:11:10.980602+00:00, finished2026-11-03T08:11:11.369667+00:00, exit0. One concrete Hsp104 example verified; graph scan has one COVERED Hsp104 node and one NO_GENE_SYMBOLS heterogeneous PrD cargo node, not a dangling or ungrounded named protein. These mechanical checks do not verify biological necessity, all graph intervention factors or a complete cargo inventory. |
| micro-image-insoluble_protein_deposit | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/repo/data/images/inclusion/insoluble_protein_deposit/pmc5045159_pgen_1006324_g003_e27e1f28.jpg; Original-resolution tracked JPEG directly viewed; complete stated figure panels; local SHA matches frozen input | supports | Direct pixels agree with the record caption: Figure3A–F depicts auxin-depletion recovery and preformed-IPOD stability, scale2micrometers. Caption and primary permission statement checked separately; no raw image reanalysis claimed. |
| micro-image-package-insoluble_protein_deposit | https://pmc-oa-opendata.s3.amazonaws.com/PMC5045159.1/PMC5045159.1.json; Fresh PMC open-access media package metadata, retraction flag and exact figure JPEG entry; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/package-PMC5045159.raw; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/package-PMC5045159.receipt.json | supports | The package is not marked retracted and its figure media MD5 matches the frozen tracked JPEG: 9fb3e11d765cf9a68d081cff9402a568. The primary JATS permissions state CC BY4.0; package metadata alone is not a substitute for pixel inspection. |
| micro-record-mitostore | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/repo/data/structures/inclusion/mitostore.yaml; Entire current YAML, definitions/components/graphs/evidence/discussions/provenance | supports | Current frozen record inspected in full; its identity, source scope, experimental qualifications and evidence tiers were independently reassessed. The added STRUCTURE self-node groundings resolve to this exact record identity; scientific mechanisms are otherwise unchanged. |
| micro-prior-mitostore | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/repo/reviews/structured/20261021T103324Z-mitostore-audit/review.yaml; Entire original YAML observation, checks/assessments/evidence/verdict/findings; paired rendered Markdown validated | supports | Original pass_with_limitations observation has no scientific findings. Its frozen target hash is historical and differs from current; do not silently rewrite it. Scientific support is freshly rechecked here; old source access times are not presented as new reads. |
| micro-native-mitostore-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/mitostore-uniprot-verify-receipt.json; .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/mitostore.yaml --verify; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/mitostore-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Current-source command passed, started2026-11-03T08:11:14.816178+00:00, finished2026-11-03T08:11:15.999007+00:00, exit0. Three concrete chaperone examples verified; graph scan has two NO_GENE_SYMBOLS heterogeneous precursor-cargo nodes and no dangling references. These mechanical checks do not verify biological necessity, all graph intervention factors or a complete cargo inventory. |
| micro-native-mitostore-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/mitostore-uniprot-causal-receipt.json; .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/mitostore.yaml --causal-graphs; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/mitostore-uniprot-causal.log SHA256 448ddff38bf088be0c748c4d74ce9a0cfffd623e46490b160132b8904cc5aa64 | supports | Current-source command passed, started2026-11-03T08:11:16.033306+00:00, finished2026-11-03T08:11:16.439258+00:00, exit0. Three concrete chaperone examples verified; graph scan has two NO_GENE_SYMBOLS heterogeneous precursor-cargo nodes and no dangling references. These mechanical checks do not verify biological necessity, all graph intervention factors or a complete cargo inventory. |
| micro-image-mitostore | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/repo/data/images/inclusion/mitostore/pmc10068336_embj2022112309_fig_0005.jpg; Original-resolution tracked JPEG directly viewed; complete stated figure panels; local SHA matches frozen input | supports | Direct pixels agree with the record caption: Figure5A–D depicts reporter/chaperone colocalization, separate deletion tests, presequence truncation and carbon-source context, with panel-specific2/10/5/10micrometer scales. Caption and primary permission statement checked separately; no raw image reanalysis claimed. |
| micro-image-package-mitostore | https://pmc-oa-opendata.s3.amazonaws.com/PMC10068336.1/PMC10068336.1.json; Fresh PMC open-access media package metadata, retraction flag and exact figure JPEG entry; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/package-PMC10068336.raw; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/package-PMC10068336.receipt.json | supports | The package is not marked retracted and its figure media MD5 matches the frozen tracked JPEG: d5aed1d2f71065dd88d6dc617a55f368. The primary JATS permissions state CC BY4.0; package metadata alone is not a substitute for pixel inspection. |
| septin-aggresome-agent-PMC8528417 | https://pmc-oa-opendata.s3.amazonaws.com/PMC8528417.1/PMC8528417.1.xml; Fresh native JATS: article identity; three experimental Results subsections (formation, LLPS, fitness), Discussion and strain/construction Methods. No simulation/raw-data or image-pixel audit. | supports | Jin 2021 observes differently timed HslU/Kbl/AcnB recruitment and liquid-like behavior in tested bacterial states. Fitness perturbations are broader context; constituent necessity and universal bacterial material state are not established. |
| septin-aggresome-agent-pei2025-aam | https://eprints.whiterose.ac.uk/id/eprint/229675/1/Aggresomes_protect_mRNA_AAM-ms_and_si.pdf; Fresh accepted-manuscript PDF, cover/abstract pp1–2; selected Main/Results pages3,5–6,8,10,12,14–16 and complete charge-exclusion/recovery/Discussion pp17–25; specified strain, imaging, fractionation, RNA, recovery and persister Methods pp25–30. Fig5/ExtendedData5 pixels pp17–18 and Fig6 pixels p20 independently viewed. Other early figure captions inspected in part; no complete mathematical supplement audit. | supports | Pei 2025 distinguishes selected transcript storage, RNase charge-mutant entry and catalytic activity, and translation recovery controls. RNA as the repulsive agent remains proposed. Opposite persistence outcomes under RNA degradation versus chemical disruption do not support a universal fitness edge. |
| septin-root19-sources-jats-PMC10185304 | https://pmc-oa-opendata.s3.amazonaws.com/PMC10185304.1/PMC10185304.1.xml; Fresh native JATS: article metadata; Introduction S1, Results S3–S7, Discussion S8, limitations S9, strain/preparation S15/S17 and key-resource strain rows. No image pixels, tomograms, supplementary models or detailed remaining computational Methods reanalysis. | supports | Dutka 2023 supports polymerized GvpA ribs and exterior GvpC reinforcement in native Anabaena/Dolichospermum shells. Stripping, homology fitting and mechanical simulation remain distinct evidence types; CCAP1403/13F is specified in the resource table. Formation necessity of GvpC is not settled by stripping assembled vesicles. |
| septin-root19-sources-legacy-PMC3271001 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3271001/; Fresh genuine PMC HTML: article metadata, complete abstract/introduction, Figure1 caption and gas-vesicle preparation Methods; bounded solid-state NMR experimental context. No spectrum, figure-pixel or full structural-model reanalysis. | supports | Bayro 2012 directly supports the recorded cross-beta wall interpretation. Native body now accessible, unlike the original abstract-only review; the sampled organism is Anabaena flos-aquae 1403/13f. |
| septin-root19-sources-legacy-PMC372955 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC372955/; Fresh native PMC HTML: title/metadata and complete secondary-review abstract only. The full article is scanned; linked scans were not read in this review. | supports | Walsby 1994 supports coarse gas-vesicle morphology, variable bacterial/archaeal occurrence and gas-permeable, water-excluding protein walls. No detailed full-body or conditional GvpC formation claim is certified. |
| septin-root19-sources-jats-PMC5947121 | https://pmc-oa-opendata.s3.amazonaws.com/PMC5947121.1/PMC5947121.1.xml; Fresh native secondary-review JATS: front metadata, opening sec0002 and direct text of biogenesis sec0003; nested protein-machinery sections excluded. | supports | Graef 2018 supports a single phospholipid surface around neutral storage lipids and separates mature topology from biogenesis models. It does not by itself supply primary formation-necessity experiments. |
| septin-root19-sources-jats-PMC3229976 | https://pmc-oa-opendata.s3.amazonaws.com/PMC3229976.1/PMC3229976.1.xml; Fresh native JATS: metadata, Introduction s0005, strain/culture s0015, fractionation s0020, lipid analysis s0030, Results s0055/s0060 and strain-context figure caption. No full proteome/raw-MS or figure-pixel analysis. | supports | Grillitsch 2011 examines isolated yeast lipid particles under glucose/oleate conditions and supports phospholipid surface material with condition-dependent lipid composition. Generic class-level necessity is not a requirement for each individual phospholipid species. |
| septin-parasporal-agent-jats-PMC4280536 | https://pmc-oa-opendata.s3.amazonaws.com/PMC4280536.1/PMC4280536.1.xml; Fresh native secondary-review JATS: metadata, sections1,2,3 opening,3.1 opening,3.1.2 and3.2. No complete underlying-primary-paper or toxicity-mechanism audit. | supports | Palma 2014 distinguishes multiple unrelated Cry lineages and Cyt proteins, and distinguishes crystals from secreted toxins. The mixed constituent label cannot be assigned one supposedly universal Cry/Cyt family. |
| septin-parasporal-agent-jats-PMC4014730 | https://pmc-oa-opendata.s3.amazonaws.com/PMC4014730.1/PMC4014730.1.xml; Fresh native secondary-review JATS: metadata, sections1–2,3 opening,3.1 major and3.2 minor proteins. Later toxicity/application sections not comprehensively audited. | supports | Ben-Dov 2014 supports a strain/plasmid-dependent Bti crystal repertoire including the three recorded examples. Modern protein identities are not inferred from historical light/dark lattice appearance. |
| septin-parasporal-agent-legacy-PMC1857359 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1857359/; Fresh genuine PMC secondary-review HTML: complete abstract and Introduction only; downstream receptor mechanisms and full section2 not independently audited. | supports | Bravo 2007 supports the coarse distinction between the crystal packaging state and activated toxin action. It is secondary contextual evidence, not a new crystal-formation experiment. |
| septin-aggresome-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0016234,GO:0016235,GO:0005737,GO:0048255; Fresh native accession, label, definition, synonym types and relevant hierarchy/parthood; broad GO child lists are not a new exhaustive ontology search. | supports | GO0016235 requires dynein-dependent microtubule transport; GO0016234 inclusion body, GO0005737 cytoplasm and GO0048255 mRNA stabilization retain their distinct scopes. |
| septin-aggresome-agent-so | https://www.ebi.ac.uk/ols4/api/ontologies/so/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FSO_0000234; Fresh native accession, label, definition, synonym types and relevant hierarchy/parthood; broad GO child lists are not a new exhaustive ontology search. | supports | SO0000234 denotes mRNA; exact molecular class identity only. |
| septin-root19-sources-gas-shell-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031411,GO:0033172; Fresh native accession, label, definition, synonym types and relevant hierarchy/parthood; broad GO child lists are not a new exhaustive ontology search. | supports | GO0033172 denotes proteinaceous gas-vesicle shell, part of GO0031411; the membrane synonym does not imply lipid bilayer. |
| septin-root19-sources-lipid-monolayer-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005811,GO:0034430; Fresh native accession, label, definition, synonym types and relevant hierarchy/parthood; broad GO child lists are not a new exhaustive ontology search. | supports | GO0034430 denotes the single phospholipid layer; GO0005811 denotes its containing lipid droplet. |
| septin-parasporal-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0016234; Fresh native accession, label, definition, synonym types and relevant hierarchy/parthood; broad GO child lists are not a new exhaustive ontology search. | supports | GO0016234 is inclusion body, a broader parent rather than an exact identity for the parasporal crystal. |
| septin-root19-sources-CHEBI-16247 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/16247/; Fresh native accession, label, definition, synonym types and relevant hierarchy/parthood; broad GO child lists are not a new exhaustive ontology search. | supports | CHEBI16247 is phospholipid, a chemical class rather than an individual lipid species. |
| septin-aggresome-agent-tax-83333 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333; ENA exact taxId, scientificName, rank and relevant alternative-name/lineage fields. | supports | Authority resolves 83333 to Escherichia coli K-12; taxonomy identity does not establish prevalence, exact strain equivalence or structural membership. |
| septin-aggresome-agent-tax-511145 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/511145; ENA exact taxId, scientificName, rank and relevant alternative-name/lineage fields. | supports | Authority resolves 511145 to Escherichia coli str. K-12 substr. MG1655; taxonomy identity does not establish prevalence, exact strain equivalence or structural membership. |
| septin-root19-sources-NCBITaxon-2 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2; ENA exact taxId, scientificName, rank and relevant alternative-name/lineage fields. | supports | Authority resolves 2 to Bacteria; taxonomy identity does not establish prevalence, exact strain equivalence or structural membership. |
| septin-root19-sources-NCBITaxon-2157 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2157; ENA exact taxId, scientificName, rank and relevant alternative-name/lineage fields. | supports | Authority resolves 2157 to Archaea; taxonomy identity does not establish prevalence, exact strain equivalence or structural membership. |
| septin-root19-sources-NCBITaxon-315271 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/315271; ENA exact taxId, scientificName, rank and relevant alternative-name/lineage fields. | supports | Authority resolves 315271 to Dolichospermum flos-aquae CCAP 1403/13F; taxonomy identity does not establish prevalence, exact strain equivalence or structural membership. |
| septin-root19-sources-NCBITaxon-2692880 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2692880; ENA exact taxId, scientificName, rank and relevant alternative-name/lineage fields. | supports | Authority resolves 2692880 to Anabaena cylindrica FACHB-318; taxonomy identity does not establish prevalence, exact strain equivalence or structural membership. |
| septin-root19-sources-NCBITaxon-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; ENA exact taxId, scientificName, rank and relevant alternative-name/lineage fields. | supports | Authority resolves 4932 to Saccharomyces cerevisiae; taxonomy identity does not establish prevalence, exact strain equivalence or structural membership. |
| septin-parasporal-agent-tax-1428 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1428; ENA exact taxId, scientificName, rank and relevant alternative-name/lineage fields. | supports | Authority resolves 1428 to Bacillus thuringiensis; taxonomy identity does not establish prevalence, exact strain equivalence or structural membership. |
| septin-parasporal-agent-tax-1430 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1430; ENA exact taxId, scientificName, rank and relevant alternative-name/lineage fields. | supports | Authority resolves 1430 to Bacillus thuringiensis serovar israelensis; taxonomy identity does not establish prevalence, exact strain equivalence or structural membership. |
| septin-aggresome-agent-P0A6H5 | https://rest.uniprot.org/uniprotkb/P0A6H5.json; Fresh UniProt primaryAccession, entryType, recommended protein name, gene, organism and InterPro cross-references; annotation is not direct experimental membership. | supports | P0A6H5: ATP-dependent protease ATPase subunit HslU; UniProtKB reviewed (Swiss-Prot); taxon 83333. Concrete identity checked independently from source-based membership and assembly necessity. |
| septin-aggresome-agent-P0AB77 | https://rest.uniprot.org/uniprotkb/P0AB77.json; Fresh UniProt primaryAccession, entryType, recommended protein name, gene, organism and InterPro cross-references; annotation is not direct experimental membership. | supports | P0AB77: 2-amino-3-ketobutyrate coenzyme A ligase; UniProtKB reviewed (Swiss-Prot); taxon 83333. Concrete identity checked independently from source-based membership and assembly necessity. |
| septin-aggresome-agent-P36683 | https://rest.uniprot.org/uniprotkb/P36683.json; Fresh UniProt primaryAccession, entryType, recommended protein name, gene, organism and InterPro cross-references; annotation is not direct experimental membership. | supports | P36683: Aconitate hydratase B; UniProtKB reviewed (Swiss-Prot); taxon 83333. Concrete identity checked independently from source-based membership and assembly necessity. |
| septin-root19-sources-UniProtKB-A0ABR7ZBW9 | https://rest.uniprot.org/uniprotkb/A0ABR7ZBW9.json; Fresh UniProt primaryAccession, entryType, recommended protein name, gene, organism and InterPro cross-references; annotation is not direct experimental membership. | supports | A0ABR7ZBW9: Gas vesicle protein A; UniProtKB unreviewed (TrEMBL); taxon 2692880. Concrete identity checked independently from source-based membership and assembly necessity. |
| septin-root19-sources-UniProtKB-A0ABR7ZCB1 | https://rest.uniprot.org/uniprotkb/A0ABR7ZCB1.json; Fresh UniProt primaryAccession, entryType, recommended protein name, gene, organism and InterPro cross-references; annotation is not direct experimental membership. | supports | A0ABR7ZCB1: Gas vesicle protein C; UniProtKB unreviewed (TrEMBL); taxon 2692880. Concrete identity checked independently from source-based membership and assembly necessity. |
| septin-parasporal-agent-P16480 | https://rest.uniprot.org/uniprotkb/P16480.json; Fresh UniProt primaryAccession, entryType, recommended protein name, gene, organism and InterPro cross-references; annotation is not direct experimental membership. | supports | P16480: Pesticidal crystal protein Cry4Aa; UniProtKB reviewed (Swiss-Prot); taxon 1430. Concrete identity checked independently from source-based membership and assembly necessity. |
| septin-parasporal-agent-P21256 | https://rest.uniprot.org/uniprotkb/P21256.json; Fresh UniProt primaryAccession, entryType, recommended protein name, gene, organism and InterPro cross-references; annotation is not direct experimental membership. | supports | P21256: Pesticidal crystal protein Cry11Aa; UniProtKB reviewed (Swiss-Prot); taxon 1430. Concrete identity checked independently from source-based membership and assembly necessity. |
| septin-parasporal-agent-P0A382 | https://rest.uniprot.org/uniprotkb/P0A382.json; Fresh UniProt primaryAccession, entryType, recommended protein name, gene, organism and InterPro cross-references; annotation is not direct experimental membership. | supports | P0A382: Type-1Aa cytolytic delta-endotoxin; UniProtKB reviewed (Swiss-Prot); taxon 1430. Concrete identity checked independently from source-based membership and assembly necessity. |
| septin-aggresome-agent-IPR004491 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004491/; Fresh InterPro/Pfam accession, name, type, hierarchy, integrated/member signatures; non-LLM IPR000638 description additionally inspected. Generated descriptions excluded. | supports | IPR004491 is type family, named Heat shock protein HslU. Native hierarchy/integration and member signatures checked; family, repeat and exact-component scopes remain distinct. |
| septin-aggresome-agent-IPR011282 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR011282/; Fresh InterPro/Pfam accession, name, type, hierarchy, integrated/member signatures; non-LLM IPR000638 description additionally inspected. Generated descriptions excluded. | supports | IPR011282 is type family, named 2-amino-3-ketobutyrate coenzyme A ligase. Native hierarchy/integration and member signatures checked; family, repeat and exact-component scopes remain distinct. |
| septin-aggresome-agent-IPR004406 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004406/; Fresh InterPro/Pfam accession, name, type, hierarchy, integrated/member signatures; non-LLM IPR000638 description additionally inspected. Generated descriptions excluded. | supports | IPR004406 is type family, named Aconitase B. Native hierarchy/integration and member signatures checked; family, repeat and exact-component scopes remain distinct. |
| septin-root19-sources-PF00741 | https://www.ebi.ac.uk/interpro/api/entry/pfam/PF00741/; Fresh InterPro/Pfam accession, name, type, hierarchy, integrated/member signatures; non-LLM IPR000638 description additionally inspected. Generated descriptions excluded. | supports | PF00741 is type family, named Gas vesicle protein. Native hierarchy/integration and member signatures checked; family, repeat and exact-component scopes remain distinct. |
| septin-root19-sources-PF01304 | https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01304/; Fresh InterPro/Pfam accession, name, type, hierarchy, integrated/member signatures; non-LLM IPR000638 description additionally inspected. Generated descriptions excluded. | supports | PF01304 is type repeat, named Gas vesicles protein GVPc repeated domain. Native hierarchy/integration and member signatures checked; family, repeat and exact-component scopes remain distinct. |
| septin-root19-sources-IPR000638 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000638/; Fresh InterPro/Pfam accession, name, type, hierarchy, integrated/member signatures; non-LLM IPR000638 description additionally inspected. Generated descriptions excluded. | supports | IPR000638 is type family, named Gas vesicle protein GvpA-like. Native hierarchy/integration and member signatures checked; family, repeat and exact-component scopes remain distinct. The non-LLM description includes related GvpJ/GvpM, supporting broader GvpA-like scope. |
| septin-root19-sources-IPR047870 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR047870/; Fresh InterPro/Pfam accession, name, type, hierarchy, integrated/member signatures; non-LLM IPR000638 description additionally inspected. Generated descriptions excluded. | supports | IPR047870 is type family, named Gas vesicle protein GvpA. Native hierarchy/integration and member signatures checked; family, repeat and exact-component scopes remain distinct. The exact GvpA child family integrates HAMAP MF_00576 and is also present on the recorded GvpA accession. |
| septin-root19-sources-IPR050530 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050530/; Fresh InterPro/Pfam accession, name, type, hierarchy, integrated/member signatures; non-LLM IPR000638 description additionally inspected. Generated descriptions excluded. | supports | IPR050530 is type family, named Gas Vesicle Protein A. Native hierarchy/integration and member signatures checked; family, repeat and exact-component scopes remain distinct. Generated description is excluded from biological evidence. |
| septin-root19-sources-IPR002003 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002003/; Fresh InterPro/Pfam accession, name, type, hierarchy, integrated/member signatures; non-LLM IPR000638 description additionally inspected. Generated descriptions excluded. | supports | IPR002003 is type repeat, named Gas vesicle protein GvpC. Native hierarchy/integration and member signatures checked; family, repeat and exact-component scopes remain distinct. |
| septin-root19-sources-IPR018185 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR018185/; Fresh InterPro/Pfam accession, name, type, hierarchy, integrated/member signatures; non-LLM IPR000638 description additionally inspected. Generated descriptions excluded. | supports | IPR018185 is type repeat, named Gas vesicle C repeat. Native hierarchy/integration and member signatures checked; family, repeat and exact-component scopes remain distinct. |
| septin-parasporal-agent-IPR038979 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR038979/; Fresh InterPro/Pfam accession, name, type, hierarchy, integrated/member signatures; non-LLM IPR000638 description additionally inspected. Generated descriptions excluded. | supports | IPR038979 is type family, named Pesticidal crystal protein. Native hierarchy/integration and member signatures checked; family, repeat and exact-component scopes remain distinct. |
| septin-parasporal-agent-IPR001615 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001615/; Fresh InterPro/Pfam accession, name, type, hierarchy, integrated/member signatures; non-LLM IPR000638 description additionally inspected. Generated descriptions excluded. | supports | IPR001615 is type family, named Delta-endotoxin CytB. Native hierarchy/integration and member signatures checked; family, repeat and exact-component scopes remain distinct. |
| septin-aggresome-agent-ipr-matches-P0A6H5 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P0A6H5/?page_size=200; Native protein-specific InterPro entry list; page_size200, accession/name/type and next/count; bounded sequence annotation. | supports | Returned 6 annotations, next=None; family identity corroboration only, without equating all Cry/Cyt proteins or converting domains into whole proteins. |
| septin-aggresome-agent-ipr-matches-P0AB77 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P0AB77/?page_size=200; Native protein-specific InterPro entry list; page_size200, accession/name/type and next/count; bounded sequence annotation. | supports | Returned 7 annotations, next=None; family identity corroboration only, without equating all Cry/Cyt proteins or converting domains into whole proteins. |
| septin-aggresome-agent-ipr-matches-P36683 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P36683/?page_size=200; Native protein-specific InterPro entry list; page_size200, accession/name/type and next/count; bounded sequence annotation. | supports | Returned 12 annotations, next=None; family identity corroboration only, without equating all Cry/Cyt proteins or converting domains into whole proteins. |
| septin-parasporal-agent-matches-P16480 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P16480/?page_size=200; Native protein-specific InterPro entry list; page_size200, accession/name/type and next/count; bounded sequence annotation. | supports | Returned 9 annotations, next=None; family identity corroboration only, without equating all Cry/Cyt proteins or converting domains into whole proteins. |
| septin-parasporal-agent-matches-P21256 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P21256/?page_size=200; Native protein-specific InterPro entry list; page_size200, accession/name/type and next/count; bounded sequence annotation. | supports | Returned 3 annotations, next=None; family identity corroboration only, without equating all Cry/Cyt proteins or converting domains into whole proteins. |
| septin-parasporal-agent-matches-P0A382 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P0A382/?page_size=200; Native protein-specific InterPro entry list; page_size200, accession/name/type and next/count; bounded sequence annotation. | supports | Returned 2 annotations, next=None; family identity corroboration only, without equating all Cry/Cyt proteins or converting domains into whole proteins. |
| septin-aggresome-agent-reviewed-uniqueness | https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A83333+AND+%28gene_exact%3AhslU+OR+gene_exact%3Akbl+OR+gene_exact%3AacnB%29&amp;format=json&amp;size=500; Exact stated reviewed/gene/taxon UniProt query; returned results only; suggestions are not substituted queries. | supports | Returned accessions ['P36683', 'P0AB77', 'P0A6H5']. Zero returned reviewed entries, where applicable, is limited to this query and is not biological absence. |
| septin-root19-sources-query-gvpA-2692880 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=%28gene_exact%3AgvpA%29%20AND%20%28taxonomy_id%3A2692880%29%20AND%20%28reviewed%3Atrue%29; Exact stated reviewed/gene/taxon UniProt query; returned results only; suggestions are not substituted queries. | supports | Returned accessions []. Zero returned reviewed entries, where applicable, is limited to this query and is not biological absence. |
| septin-root19-sources-query-gvpC-2692880 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=%28gene_exact%3AgvpC%29%20AND%20%28taxonomy_id%3A2692880%29%20AND%20%28reviewed%3Atrue%29; Exact stated reviewed/gene/taxon UniProt query; returned results only; suggestions are not substituted queries. | supports | Returned accessions []. Zero returned reviewed entries, where applicable, is limited to this query and is not biological absence. |
| septin-parasporal-agent-query-cry4Aa | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3Acry4Aa%29%20AND%20%28organism_id%3A1430%29%20AND%20%28reviewed%3Atrue%29; Exact stated reviewed/gene/taxon UniProt query; returned results only; suggestions are not substituted queries. | supports | Returned accessions ['P16480']. Zero returned reviewed entries, where applicable, is limited to this query and is not biological absence. |
| septin-parasporal-agent-query-cry11Aa | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3Acry11Aa%29%20AND%20%28organism_id%3A1430%29%20AND%20%28reviewed%3Atrue%29; Exact stated reviewed/gene/taxon UniProt query; returned results only; suggestions are not substituted queries. | supports | Returned accessions ['P21256']. Zero returned reviewed entries, where applicable, is limited to this query and is not biological absence. |
| septin-parasporal-agent-query-cyt1Aa | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3Acyt1Aa%29%20AND%20%28organism_id%3A1430%29%20AND%20%28reviewed%3Atrue%29; Exact stated reviewed/gene/taxon UniProt query; returned results only; suggestions are not substituted queries. | supports | Returned accessions ['P0A382']. Zero returned reviewed entries, where applicable, is limited to this query and is not biological absence. |
| septin-parasporal-agent-ols-exact-0 | https://www.ebi.ac.uk/ols4/api/search?ontology=go&amp;exact=true&amp;rows=100&amp;q=parasporal%20crystal; OLS GO exact phrase, rows100; native numFound/docs. | supports | Both bounded exact-phrase queries return zero terms; this does not prove exhaustive GO absence or replace identity reasoning. |
| septin-parasporal-agent-ols-exact-1 | https://www.ebi.ac.uk/ols4/api/search?ontology=go&amp;exact=true&amp;rows=100&amp;q=parasporal%20body; OLS GO exact phrase, rows100; native numFound/docs. | supports | Both bounded exact-phrase queries return zero terms; this does not prove exhaustive GO absence or replace identity reasoning. |
| septin-root19-sources-PMID-1510555 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A1510555%20AND%20SRC%3AMED; Europe PMC exact PMID native metadata and complete abstract; source tier follows article type, no full-body inference. | supports | Gas vesicles are strengthened by the outer-surface protein, GvpC. Bibliographic identity and abstract checked. GvpC removal/rebinding changes collapse strength of assembled vesicles; formation necessity is not tested. |
| septin-root19-sources-PMID-22147705 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A22147705%20AND%20SRC%3AMED; Europe PMC exact PMID native metadata and complete abstract; source tier follows article type, no full-body inference. | supports | An amyloid organelle, solid-state NMR evidence for cross-β assembly of gas vesicles. Bibliographic identity and abstract checked. Bayro is the first author; full-body scope is separately recorded. |
| septin-root19-sources-PMID-8177173 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A8177173%20AND%20SRC%3AMED; Europe PMC exact PMID native metadata and complete abstract; source tier follows article type, no full-body inference. | supports | Gas vesicles. Bibliographic identity and abstract checked. Walsby is a secondary review; coarse morphology/function scope only. |
| septin-root19-sources-permeability1992-crossref | https://api.crossref.org/works/10.1099/00221287-138-4-837; Native Crossref exact DOI/title/author/year/type metadata only; no body content. | supports | ['The gas permeability coefficient of the cyanobacterial gas vesicle wall'] Article identity; abstract separately scoped. |
| septin-parasporal-agent-crossref-book | https://api.crossref.org/works/10.1007/978-94-011-5967-8_3; Native Crossref exact DOI/title/author/year/type metadata only; no body content. | supports | ['Parasporal Body of Bacillus thuringiensis israelensis'] Publication identity only; chapter body not recovered. |
| septin-parasporal-agent-insell1985-page56 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/c298/238573/264b7d322559/aem00142-0064.png; Fresh genuine native PMC238573 scan, printed page56, independently viewed and read with view_image; complete page text and included figures/captions. | supports | Insell/Fitz-James 1985 historical preparation, morphology, polypeptide fractionation and/or discussion at this page scope. Light/dark lattice classes and polypeptide bands do not identify modern Cry/Cyt accessions; no raw-image reanalysis. |
| septin-parasporal-agent-insell1985-page57 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/c298/238573/af3db6766abb/aem00142-0065.png; Fresh genuine native PMC238573 scan, printed page57, independently viewed and read with view_image; complete page text and included figures/captions. | supports | Insell/Fitz-James 1985 historical preparation, morphology, polypeptide fractionation and/or discussion at this page scope. Light/dark lattice classes and polypeptide bands do not identify modern Cry/Cyt accessions; no raw-image reanalysis. |
| septin-parasporal-agent-insell1985-page58 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/c298/238573/031ad2528ec8/aem00142-0066.png; Fresh genuine native PMC238573 scan, printed page58, independently viewed and read with view_image; complete page text and included figures/captions. | supports | Insell/Fitz-James 1985 historical preparation, morphology, polypeptide fractionation and/or discussion at this page scope. Light/dark lattice classes and polypeptide bands do not identify modern Cry/Cyt accessions; no raw-image reanalysis. |
| septin-parasporal-agent-insell1985-page59 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/c298/238573/fefc2292df2c/aem00142-0067.png; Fresh genuine native PMC238573 scan, printed page59, independently viewed and read with view_image; complete page text and included figures/captions. | supports | Insell/Fitz-James 1985 historical preparation, morphology, polypeptide fractionation and/or discussion at this page scope. Light/dark lattice classes and polypeptide bands do not identify modern Cry/Cyt accessions; no raw-image reanalysis. |
| septin-parasporal-agent-insell1985-page60 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/c298/238573/3ec6bf7d3e74/aem00142-0068.png; Fresh genuine native PMC238573 scan, printed page60, independently viewed and read with view_image; complete page text and included figures/captions. | supports | Insell/Fitz-James 1985 historical preparation, morphology, polypeptide fractionation and/or discussion at this page scope. Light/dark lattice classes and polypeptide bands do not identify modern Cry/Cyt accessions; no raw-image reanalysis. |
| septin-parasporal-agent-insell1985-page61 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/c298/238573/07117471b85b/aem00142-0069.png; Fresh genuine native PMC238573 scan, printed page61, independently viewed and read with view_image; complete page text and included figures/captions. | supports | Insell/Fitz-James 1985 historical preparation, morphology, polypeptide fractionation and/or discussion at this page scope. Light/dark lattice classes and polypeptide bands do not identify modern Cry/Cyt accessions; no raw-image reanalysis. |
| septin-parasporal-agent-insell1985-page62 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/c298/238573/5eed4fa4bcd7/aem00142-0070.png; Fresh genuine native PMC238573 scan, printed page62, independently viewed and read with view_image; complete page text and included figures/captions. | supports | Insell/Fitz-James 1985 historical preparation, morphology, polypeptide fractionation and/or discussion at this page scope. Light/dark lattice classes and polypeptide bands do not identify modern Cry/Cyt accessions; no raw-image reanalysis. |
| septin-permeability1992-browser-current | https://www.microbiologyresearch.org/content/journal/micro/10.1099/00221287-138-4-837; Browser-indexed publisher title/authors and complete abstract lines48–52; declared crawl age5days. Full-text loader remains unrecovered. SHA256 identifies this saved derived observation receipt, not raw browser-page bytes. | supports | Oxygen microelectrode gradients across gas-vesicle and agar layers underpin diffusion-model estimates. Gas equilibration is rapid; vesicles do not actively store gas. No full Methods or raw data reanalysis. |
| septin-wang2015-browser-current | https://link.springer.com/article/10.1007/s00018-015-1903-5; Browser-indexed publisher title/author/type and complete abstract lines48–51; declared crawl age4months, subscription-body boundary. SHA256 identifies this saved derived observation receipt, not raw browser-page bytes. | supports | Secondary review concerns budding-yeast lipid-droplet storage and dynamics. The retrieved abstract does not directly expose the exact phospholipid-monolayer body passage; the coarse topology is assessed from independently fetched Graef/Grillitsch. |
| septin-austin2006-browser-current | https://pmc.ncbi.nlm.nih.gov/articles/PMC1488921/; Browser-indexed PMC, declared crawl today: title/authors/DOI/PMID and complete Abstract lines96–101; opening Results and Figure1/2 captions lines117–139 read as boundary context; no actual image pixels or raw tomograms viewed. SHA256 identifies this saved derived observation receipt, not raw browser-page bytes. | supports | Austin 2006 primary microscopy supports plastoglobule surface continuity with the stroma-side thylakoid leaflet in its studied plant context. This supports retaining the record boundary question, not automatically merging all lipid-body classes. |
| septin-current-adapter-catalogue | https://imodulondb.org/api/datasets; Fresh full official /api/datasets response, all 20 organism entries and 28 dataset keys. | supports | E. coli/precise_mg1655 matches the aggresome experimental strain. No catalogue entry matches Anabaena cylindrica FACHB-318, Dolichospermum flos-aquae or B. thuringiensis/israelensis; B. subtilis and other cyanobacteria are not substituted. Broad bacterial/archaeal occurrence does not license unrelated gene queries. |
| septin-adapter-mg1655-meta | https://imodulondb.org/api/datasets/e_coli/precise_mg1655/meta; Fresh selected-dataset metadata: organism/dataset/strains, module/gene/sample counts and publication_url field. | supports | MG1655 is the explicit strain; 115 modules and 4305 genes provide bounded expression context. Publication_url is null; no publication provenance is invented. |
| septin-adapter-search-hslU | https://imodulondb.org/api/search?organism=e_coli&amp;dataset=precise_mg1655&amp;query=hslU&amp;limit=50; Selected MG1655 gene search, q literal symbol and limit50; exact matching symbol selected among possible substring matches. | supports | Identity lookup for hslU only; no cross-species substitution or exhaustive absence inference. |
| septin-adapter-hslU-gene | https://imodulondb.org/api/genes/e_coli/precise_mg1655/b3931; Exact selected-dataset gene record: gene_id/name/product and imported UniProt ID; full function prose not used as structural evidence. | supports | hslU resolves to b3931; this contextual gene identity does not make the gene a structural component or establish condensate necessity. |
| septin-adapter-hslU-modules | https://imodulondb.org/api/genes/e_coli/precise_mg1655/b3931/imodulons; Complete returned 115 selected-dataset module rows; native is_in_imodulon flag, module ID/name, weights and thresholds. | supports | Positive flags for hslU: [(37, 'RpoH')]. All-false rows where present are threshold outcomes, not biological absence, lack of regulation or absence from aggresomes. |
| septin-adapter-search-kbl | https://imodulondb.org/api/search?organism=e_coli&amp;dataset=precise_mg1655&amp;query=kbl&amp;limit=50; Selected MG1655 gene search, q literal symbol and limit50; exact matching symbol selected among possible substring matches. | supports | Identity lookup for kbl only; no cross-species substitution or exhaustive absence inference. |
| septin-adapter-kbl-gene | https://imodulondb.org/api/genes/e_coli/precise_mg1655/b3617; Exact selected-dataset gene record: gene_id/name/product and imported UniProt ID; full function prose not used as structural evidence. | supports | kbl resolves to b3617; this contextual gene identity does not make the gene a structural component or establish condensate necessity. |
| septin-adapter-kbl-modules | https://imodulondb.org/api/genes/e_coli/precise_mg1655/b3617/imodulons; Complete returned 115 selected-dataset module rows; native is_in_imodulon flag, module ID/name, weights and thresholds. | supports | Positive flags for kbl: [(78, 'Lrp-2')]. All-false rows where present are threshold outcomes, not biological absence, lack of regulation or absence from aggresomes. |
| septin-adapter-search-acnB | https://imodulondb.org/api/search?organism=e_coli&amp;dataset=precise_mg1655&amp;query=acnB&amp;limit=50; Selected MG1655 gene search, q literal symbol and limit50; exact matching symbol selected among possible substring matches. | supports | Identity lookup for acnB only; no cross-species substitution or exhaustive absence inference. |
| septin-adapter-acnB-gene | https://imodulondb.org/api/genes/e_coli/precise_mg1655/b0118; Exact selected-dataset gene record: gene_id/name/product and imported UniProt ID; full function prose not used as structural evidence. | supports | acnB resolves to b0118; this contextual gene identity does not make the gene a structural component or establish condensate necessity. |
| septin-adapter-acnB-modules | https://imodulondb.org/api/genes/e_coli/precise_mg1655/b0118/imodulons; Complete returned 115 selected-dataset module rows; native is_in_imodulon flag, module ID/name, weights and thresholds. | supports | Positive flags for acnB: [(10, 'ArcA-2')]. All-false rows where present are threshold outcomes, not biological absence, lack of regulation or absence from aggresomes. |
| septin-adapter-search-nuoJ | https://imodulondb.org/api/search?organism=e_coli&amp;dataset=precise_mg1655&amp;query=nuoJ&amp;limit=50; Selected MG1655 gene search, q literal symbol and limit50; exact matching symbol selected among possible substring matches. | supports | Identity lookup for nuoJ only; no cross-species substitution or exhaustive absence inference. |
| septin-adapter-nuoJ-gene | https://imodulondb.org/api/genes/e_coli/precise_mg1655/b2280; Exact selected-dataset gene record: gene_id/name/product and imported UniProt ID; full function prose not used as structural evidence. | supports | nuoJ resolves to b2280; this contextual gene identity does not make the gene a structural component or establish condensate necessity. |
| septin-adapter-nuoJ-modules | https://imodulondb.org/api/genes/e_coli/precise_mg1655/b2280/imodulons; Complete returned 115 selected-dataset module rows; native is_in_imodulon flag, module ID/name, weights and thresholds. | supports | Positive flags for nuoJ: [(31, 'UC-5')]. All-false rows where present are threshold outcomes, not biological absence, lack of regulation or absence from aggresomes. |
| septin-adapter-search-nlpE | https://imodulondb.org/api/search?organism=e_coli&amp;dataset=precise_mg1655&amp;query=nlpE&amp;limit=50; Selected MG1655 gene search, q literal symbol and limit50; exact matching symbol selected among possible substring matches. | supports | Identity lookup for nlpE only; no cross-species substitution or exhaustive absence inference. |
| septin-adapter-nlpE-gene | https://imodulondb.org/api/genes/e_coli/precise_mg1655/b0192; Exact selected-dataset gene record: gene_id/name/product and imported UniProt ID; full function prose not used as structural evidence. | supports | nlpE resolves to b0192; this contextual gene identity does not make the gene a structural component or establish condensate necessity. |
| septin-adapter-nlpE-modules | https://imodulondb.org/api/genes/e_coli/precise_mg1655/b0192/imodulons; Complete returned 115 selected-dataset module rows; native is_in_imodulon flag, module ID/name, weights and thresholds. | supports | Positive flags for nlpE: []. All-false rows where present are threshold outcomes, not biological absence, lack of regulation or absence from aggresomes. |
| septin-adapter-search-glpK | https://imodulondb.org/api/search?organism=e_coli&amp;dataset=precise_mg1655&amp;query=glpK&amp;limit=50; Selected MG1655 gene search, q literal symbol and limit50; exact matching symbol selected among possible substring matches. | supports | Identity lookup for glpK only; no cross-species substitution or exhaustive absence inference. |
| septin-adapter-glpK-gene | https://imodulondb.org/api/genes/e_coli/precise_mg1655/b3926; Exact selected-dataset gene record: gene_id/name/product and imported UniProt ID; full function prose not used as structural evidence. | supports | glpK resolves to b3926; this contextual gene identity does not make the gene a structural component or establish condensate necessity. |
| septin-adapter-glpK-modules | https://imodulondb.org/api/genes/e_coli/precise_mg1655/b3926/imodulons; Complete returned 115 selected-dataset module rows; native is_in_imodulon flag, module ID/name, weights and thresholds. | supports | Positive flags for glpK: [(66, 'Glycerol')]. All-false rows where present are threshold outcomes, not biological absence, lack of regulation or absence from aggresomes. |
| septin-adapter-search-mukF | https://imodulondb.org/api/search?organism=e_coli&amp;dataset=precise_mg1655&amp;query=mukF&amp;limit=50; Selected MG1655 gene search, q literal symbol and limit50; exact matching symbol selected among possible substring matches. | supports | Identity lookup for mukF only; no cross-species substitution or exhaustive absence inference. |
| septin-adapter-mukF-gene | https://imodulondb.org/api/genes/e_coli/precise_mg1655/b0922; Exact selected-dataset gene record: gene_id/name/product and imported UniProt ID; full function prose not used as structural evidence. | supports | mukF resolves to b0922; this contextual gene identity does not make the gene a structural component or establish condensate necessity. |
| septin-adapter-mukF-modules | https://imodulondb.org/api/genes/e_coli/precise_mg1655/b0922/imodulons; Complete returned 115 selected-dataset module rows; native is_in_imodulon flag, module ID/name, weights and thresholds. | supports | Positive flags for mukF: []. All-false rows where present are threshold outcomes, not biological absence, lack of regulation or absence from aggresomes. |
| septin-adapter-search-rnb | https://imodulondb.org/api/search?organism=e_coli&amp;dataset=precise_mg1655&amp;query=rnb&amp;limit=50; Selected MG1655 gene search, q literal symbol and limit50; exact matching symbol selected among possible substring matches. | supports | Identity lookup for rnb only; no cross-species substitution or exhaustive absence inference. |
| septin-adapter-rnb-gene | https://imodulondb.org/api/genes/e_coli/precise_mg1655/b1286; Exact selected-dataset gene record: gene_id/name/product and imported UniProt ID; full function prose not used as structural evidence. | supports | rnb resolves to b1286; this contextual gene identity does not make the gene a structural component or establish condensate necessity. |
| septin-adapter-rnb-modules | https://imodulondb.org/api/genes/e_coli/precise_mg1655/b1286/imodulons; Complete returned 115 selected-dataset module rows; native is_in_imodulon flag, module ID/name, weights and thresholds. | supports | Positive flags for rnb: []. All-false rows where present are threshold outcomes, not biological absence, lack of regulation or absence from aggresomes. |
| septin-adapter-search-rbn | https://imodulondb.org/api/search?organism=e_coli&amp;dataset=precise_mg1655&amp;query=rbn&amp;limit=50; Selected MG1655 gene search, q literal symbol and limit50; exact matching symbol selected among possible substring matches. | supports | Identity lookup for rbn only; no cross-species substitution or exhaustive absence inference. |
| septin-adapter-rbn-gene | https://imodulondb.org/api/genes/e_coli/precise_mg1655/b2268; Exact selected-dataset gene record: gene_id/name/product and imported UniProt ID; full function prose not used as structural evidence. | supports | rbn resolves to b2268; this contextual gene identity does not make the gene a structural component or establish condensate necessity. |
| septin-adapter-rbn-modules | https://imodulondb.org/api/genes/e_coli/precise_mg1655/b2268/imodulons; Complete returned 115 selected-dataset module rows; native is_in_imodulon flag, module ID/name, weights and thresholds. | supports | Positive flags for rbn: []. All-false rows where present are threshold outcomes, not biological absence, lack of regulation or absence from aggresomes. |
| septin-adapter-search-orn | https://imodulondb.org/api/search?organism=e_coli&amp;dataset=precise_mg1655&amp;query=orn&amp;limit=50; Selected MG1655 gene search, q literal symbol and limit50; exact matching symbol selected among possible substring matches. | supports | Identity lookup for orn only; no cross-species substitution or exhaustive absence inference. |
| septin-adapter-orn-gene | https://imodulondb.org/api/genes/e_coli/precise_mg1655/b4162; Exact selected-dataset gene record: gene_id/name/product and imported UniProt ID; full function prose not used as structural evidence. | supports | orn resolves to b4162; this contextual gene identity does not make the gene a structural component or establish condensate necessity. |
| septin-adapter-orn-modules | https://imodulondb.org/api/genes/e_coli/precise_mg1655/b4162/imodulons; Complete returned 115 selected-dataset module rows; native is_in_imodulon flag, module ID/name, weights and thresholds. | supports | Positive flags for orn: []. All-false rows where present are threshold outcomes, not biological absence, lack of regulation or absence from aggresomes. |
| septin-adapter-search-hokB | https://imodulondb.org/api/search?organism=e_coli&amp;dataset=precise_mg1655&amp;query=hokB&amp;limit=50; Selected MG1655 gene search, q literal symbol and limit50; exact matching symbol selected among possible substring matches. | supports | Identity lookup for hokB only; no cross-species substitution or exhaustive absence inference. |
| septin-adapter-hokB-gene | https://imodulondb.org/api/genes/e_coli/precise_mg1655/b4428; Exact selected-dataset gene record: gene_id/name/product and imported UniProt ID; full function prose not used as structural evidence. | supports | hokB resolves to b4428; this contextual gene identity does not make the gene a structural component or establish condensate necessity. |
| septin-adapter-hokB-modules | https://imodulondb.org/api/genes/e_coli/precise_mg1655/b4428/imodulons; Complete returned 115 selected-dataset module rows; native is_in_imodulon flag, module ID/name, weights and thresholds. | supports | Positive flags for hokB: [(112, 'ldrD')]. All-false rows where present are threshold outcomes, not biological absence, lack of regulation or absence from aggresomes. |
| septin-adapter-module-10-detail | https://imodulondb.org/api/imodulons/e_coli/precise_mg1655/10; Exact selected module native name/regulator/function_description/category/threshold and n_genes; ai_summary and related generated fields excluded. | supports | Module10 ArcA-2: n_genes=37. Imported regulatory annotation is bounded expression context, not a causal or physical membership result. |
| septin-adapter-module-10-genes | https://imodulondb.org/api/imodulons/e_coli/precise_mg1655/10/genes; Exact module gene-membership endpoint, returned genes and threshold; named target rows cross-checked against gene-level flags. | supports | Cross-check rows [('b0118', 'acnB', True)]; no claims about unqueried datasets, stress-treatment activity or physical condensate recruitment. |
| septin-adapter-module-31-detail | https://imodulondb.org/api/imodulons/e_coli/precise_mg1655/31; Exact selected module native name/regulator/function_description/category/threshold and n_genes; ai_summary and related generated fields excluded. | supports | Module31 UC-5: n_genes=25. Imported regulatory annotation is bounded expression context, not a causal or physical membership result. |
| septin-adapter-module-31-genes | https://imodulondb.org/api/imodulons/e_coli/precise_mg1655/31/genes; Exact module gene-membership endpoint, returned genes and threshold; named target rows cross-checked against gene-level flags. | supports | Cross-check rows [('b2280', 'nuoJ', True)]; no claims about unqueried datasets, stress-treatment activity or physical condensate recruitment. |
| septin-adapter-module-37-detail | https://imodulondb.org/api/imodulons/e_coli/precise_mg1655/37; Exact selected module native name/regulator/function_description/category/threshold and n_genes; ai_summary and related generated fields excluded. | supports | Module37 RpoH: n_genes=18. Imported regulatory annotation is bounded expression context, not a causal or physical membership result. |
| septin-adapter-module-37-genes | https://imodulondb.org/api/imodulons/e_coli/precise_mg1655/37/genes; Exact module gene-membership endpoint, returned genes and threshold; named target rows cross-checked against gene-level flags. | supports | Cross-check rows [('b3931', 'hslU', True)]; no claims about unqueried datasets, stress-treatment activity or physical condensate recruitment. |
| septin-adapter-module-66-detail | https://imodulondb.org/api/imodulons/e_coli/precise_mg1655/66; Exact selected module native name/regulator/function_description/category/threshold and n_genes; ai_summary and related generated fields excluded. | supports | Module66 Glycerol: n_genes=8. Imported regulatory annotation is bounded expression context, not a causal or physical membership result. |
| septin-adapter-module-66-genes | https://imodulondb.org/api/imodulons/e_coli/precise_mg1655/66/genes; Exact module gene-membership endpoint, returned genes and threshold; named target rows cross-checked against gene-level flags. | supports | Cross-check rows [('b3926', 'glpK', True)]; no claims about unqueried datasets, stress-treatment activity or physical condensate recruitment. |
| septin-adapter-module-78-detail | https://imodulondb.org/api/imodulons/e_coli/precise_mg1655/78; Exact selected module native name/regulator/function_description/category/threshold and n_genes; ai_summary and related generated fields excluded. | supports | Module78 Lrp-2: n_genes=38. Imported regulatory annotation is bounded expression context, not a causal or physical membership result. |
| septin-adapter-module-78-genes | https://imodulondb.org/api/imodulons/e_coli/precise_mg1655/78/genes; Exact module gene-membership endpoint, returned genes and threshold; named target rows cross-checked against gene-level flags. | supports | Cross-check rows [('b3617', 'kbl', True)]; no claims about unqueried datasets, stress-treatment activity or physical condensate recruitment. |
| septin-adapter-module-112-detail | https://imodulondb.org/api/imodulons/e_coli/precise_mg1655/112; Exact selected module native name/regulator/function_description/category/threshold and n_genes; ai_summary and related generated fields excluded. | supports | Module112 ldrD: n_genes=8. Imported regulatory annotation is bounded expression context, not a causal or physical membership result. |
| septin-adapter-module-112-genes | https://imodulondb.org/api/imodulons/e_coli/precise_mg1655/112/genes; Exact module gene-membership endpoint, returned genes and threshold; named target rows cross-checked against gene-level flags. | supports | Cross-check rows [('b4428', 'hokB', True)]; no claims about unqueried datasets, stress-treatment activity or physical condensate recruitment. |
| septin-direct-access-limits | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-septin/access-limitations.json; Actual direct retrieval attempts with their individual timestamps/statuses; SHA identifies aggregate receipt. | context_only | DOI-query HTTP503, publisher403 and challenge/redirect HTML are access limitations, not negative biological evidence. Successful JATS, accepted PDF, native scans, PMID and browser fallbacks have separate source scopes. |
| septin-historical-adapter-runner-unavailable | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical actual invocation 2026-11-03T00:49:00.848907Z–00:49:00.863225Z, exit1 PermissionError reading pyvenv.cfg; receipt reused, no current invocation. | context_only | Native runner was unavailable at that earlier observation. Fresh official catalogue/API fallback is separately documented; this is not a successful new runner execution. |
| septin-native-review-policy | docs/CURATION.md; Frozen native component grounding, scientific-source, assembly-necessity and guarded-record contract; companion review process/profile/skills in context_inputs. | supports | Exact-family identity, source-scoped membership and formation necessity are distinct; structured-source fallback and issue-only review dispositions follow native policy. |
| septin-context-gas_vesicle | data/structures/inclusion/gas_vesicle.yaml; Frozen boundary fields only: identifier/label/definition/kind/hierarchy/discussions and component IDs/labels/roles. No complete neighbor evidence/graph review. | context_only | Boundary context for the assigned records only; no scientific re-review or terminal finding resolution of this neighbor. |
| septin-context-lipid_droplet | data/structures/inclusion/lipid_droplet.yaml; Frozen boundary fields only: identifier/label/definition/kind/hierarchy/discussions and component IDs/labels/roles. No complete neighbor evidence/graph review. | context_only | Boundary context for the assigned records only; no scientific re-review or terminal finding resolution of this neighbor. |
| septin-context-plastoglobule | data/structures/inclusion/plastoglobule.yaml; Frozen boundary fields only: identifier/label/definition/kind/hierarchy/discussions and component IDs/labels/roles. No complete neighbor evidence/graph review. | context_only | Boundary context for the assigned records only; no scientific re-review or terminal finding resolution of this neighbor. |
| septin-context-rnp_body | data/structures/ribonucleoprotein/rnp_body.yaml; Frozen boundary fields only: identifier/label/definition/kind/hierarchy/discussions and component IDs/labels/roles. No complete neighbor evidence/graph review. | context_only | Boundary context for the assigned records only; no scientific re-review or terminal finding resolution of this neighbor. |
| septin-context-h_body | data/structures/ribonucleoprotein/h_body.yaml; Frozen boundary fields only: identifier/label/definition/kind/hierarchy/discussions and component IDs/labels/roles. No complete neighbor evidence/graph review. | context_only | Boundary context for the assigned records only; no scientific re-review or terminal finding resolution of this neighbor. |
| septin-gas-historical-reassessment | reviews/structured/20261014T054100Z-gas-vesicle-finding-reassessment/review.yaml; Summary/assessments/findings/limitations and corresponding rendered narrative, whole-organelle target GO0031411 only. | context_only | Historical containment and GvpC essentiality allegations were rejected as unproven; conditional formation remained unknown and Bayro attribution was a different target finding. This shell review neither resolves nor reopens whole-organelle findings. |
| septin-record-bacterial_aggresome | data/structures/inclusion/bacterial_aggresome.yaml; Entire current maintained record including evidence, components/examples, functions/graphs, discussions and history; unchanged original target hash verified. | supports | Current source HEAD 7362758aca3756f5979304474ceb02a18f1a6ce6; byte-identical to the input frozen by the original review. Scientific reassessment still performed. |
| septin-original-bacterial_aggresome | reviews/structured/20261021T103320Z-bacterial-aggresome-audit/review.yaml; Entire immutable original bundle and corresponding Markdown; frozen input, source scopes, verdict, findings and native render checked. | context_only | Historical review preserved byte-for-byte; its scientific conclusions are independently reassessed rather than automatically accepted. |
| septin-native-bacterial_aggresome-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/bacterial_aggresome.yaml --verify; Root-owned current source-head command; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/bacterial_aggresome-uniprot-verify-receipt.json; started 2026-11-03T08:11:04.716245+00:00, finished 2026-11-03T08:11:06.099199+00:00; SHA256 is inspected stdout log. | supports | Exit0; three concrete protein examples verified; causal inventory has zero GENE_OR_PROTEIN nodes, so RNase/transcript narrative was checked separately. Identity/coverage is distinct from assembly necessity or universal membership. |
| septin-native-bacterial_aggresome-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/bacterial_aggresome.yaml --causal-graphs; Root-owned current source-head command; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/bacterial_aggresome-uniprot-causal-receipt.json; started 2026-11-03T08:11:06.150434+00:00, finished 2026-11-03T08:11:06.572375+00:00; SHA256 is inspected stdout log. | supports | Exit0; three concrete protein examples verified; causal inventory has zero GENE_OR_PROTEIN nodes, so RNase/transcript narrative was checked separately. Identity/coverage is distinct from assembly necessity or universal membership. |
| septin-record-gas_vesicle_shell | data/structures/inclusion/gas_vesicle_shell.yaml; Entire current maintained record including evidence, components/examples, functions/graphs, discussions and history; unchanged original target hash verified. | supports | Current source HEAD 7362758aca3756f5979304474ceb02a18f1a6ce6; byte-identical to the input frozen by the original review. Scientific reassessment still performed. |
| septin-original-gas_vesicle_shell | reviews/structured/20261021T103321Z-gas-vesicle-shell-audit/review.yaml; Entire immutable original bundle and corresponding Markdown; frozen input, source scopes, verdict, findings and native render checked. | context_only | Historical review preserved byte-for-byte; its scientific conclusions are independently reassessed rather than automatically accepted. |
| septin-native-gas_vesicle_shell-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/gas_vesicle_shell.yaml --verify; Root-owned current source-head command; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/gas_vesicle_shell-uniprot-verify-receipt.json; started 2026-11-03T08:11:06.603652+00:00, finished 2026-11-03T08:11:08.817842+00:00; SHA256 is inspected stdout log. | supports | Exit0; two concrete unreviewed examples verified; two covered GENE_OR_PROTEIN graph nodes. Identity/coverage is distinct from assembly necessity or universal membership. |
| septin-native-gas_vesicle_shell-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/gas_vesicle_shell.yaml --causal-graphs; Root-owned current source-head command; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/gas_vesicle_shell-uniprot-causal-receipt.json; started 2026-11-03T08:11:08.849436+00:00, finished 2026-11-03T08:11:09.230124+00:00; SHA256 is inspected stdout log. | supports | Exit0; two concrete unreviewed examples verified; two covered GENE_OR_PROTEIN graph nodes. Identity/coverage is distinct from assembly necessity or universal membership. |
| septin-record-monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer | data/structures/inclusion/monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer.yaml; Entire current maintained record including evidence, components/examples, functions/graphs, discussions and history; unchanged original target hash verified. | supports | Current source HEAD 7362758aca3756f5979304474ceb02a18f1a6ce6; byte-identical to the input frozen by the original review. Scientific reassessment still performed. |
| septin-original-monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer | reviews/structured/20261021T103325Z-monolayer-surrounded-lipid-storage-body-outer-lipid-monolayer-audit/review.yaml; Entire immutable original bundle and corresponding Markdown; frozen input, source scopes, verdict, findings and native render checked. | context_only | Historical review preserved byte-for-byte; its scientific conclusions are independently reassessed rather than automatically accepted. |
| septin-native-monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer.yaml --verify; Root-owned current source-head command; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer-uniprot-verify-receipt.json; started 2026-11-03T08:11:16.471749+00:00, finished 2026-11-03T08:11:16.977801+00:00; SHA256 is inspected stdout log. | supports | Exit0; empty protein-example and GENE_OR_PROTEIN inventories; this is not molecular identity coverage beyond the empty scope. Identity/coverage is distinct from assembly necessity or universal membership. |
| septin-native-monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer.yaml --causal-graphs; Root-owned current source-head command; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer-uniprot-causal-receipt.json; started 2026-11-03T08:11:17.013484+00:00, finished 2026-11-03T08:11:17.429037+00:00; SHA256 is inspected stdout log. | supports | Exit0; empty protein-example and GENE_OR_PROTEIN inventories; this is not molecular identity coverage beyond the empty scope. Identity/coverage is distinct from assembly necessity or universal membership. |
| septin-record-parasporal_crystal | data/structures/inclusion/parasporal_crystal.yaml; Entire current maintained record including evidence, components/examples, functions/graphs, discussions and history; unchanged original target hash verified. | supports | Current source HEAD 7362758aca3756f5979304474ceb02a18f1a6ce6; byte-identical to the input frozen by the original review. Scientific reassessment still performed. |
| septin-original-parasporal_crystal | reviews/structured/20261021T103327Z-parasporal-crystal-audit/review.yaml; Entire immutable original bundle and corresponding Markdown; frozen input, source scopes, verdict, findings and native render checked. | context_only | Historical review preserved byte-for-byte; its scientific conclusions are independently reassessed rather than automatically accepted. |
| septin-native-parasporal_crystal-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/parasporal_crystal.yaml --verify; Root-owned current source-head command; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/parasporal_crystal-uniprot-verify-receipt.json; started 2026-11-03T08:11:19.174501+00:00, finished 2026-11-03T08:11:20.531706+00:00; SHA256 is inspected stdout log. | supports | Exit0; three concrete examples verified; one covered mixed-cohort GENE_OR_PROTEIN node. Identity/coverage is distinct from assembly necessity or universal membership. |
| septin-native-parasporal_crystal-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/parasporal_crystal.yaml --causal-graphs; Root-owned current source-head command; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/parasporal_crystal-uniprot-causal-receipt.json; started 2026-11-03T08:11:20.567108+00:00, finished 2026-11-03T08:11:20.967472+00:00; SHA256 is inspected stdout log. | supports | Exit0; three concrete examples verified; one covered mixed-cohort GENE_OR_PROTEIN node. Identity/coverage is distinct from assembly necessity or universal membership. |
| septin-original-schema-render | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-septin/original-checks.json; Four assigned native validate/render checks with original timestamps; exact target/original YAML/Markdown hashes. | supports | All four native validations exit0 and rendered content exactly matches committed Markdown. All four target input hashes remain unchanged. |
| check-qc | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/qc.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| check-labels | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/labels.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| check-trait-links | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/trait-links.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Native TraitMech link check passed. |
| check-vendored | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/vendored.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Pinned governed files match; native vendored check passed. |
| check-curies | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/curies.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| focused | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/focused-results.json; All twenty actual target schema/strict command outputs | supports | Ten schema and ten strict commands returned exit zero. |
| supplemental-pmid | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/pmid-chunks-receipt.json; Complete native-report PMID set checked with unchanged resolver in batches of at most fifty | supports | 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers remain unverified. |
| historical-adapter-runner-availability | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical runner invocation receipt, cross-checked against exact stdout/stderr hashes; reread during PR2356 synthesis | context_only | Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS PermissionError reading the configured runner pyvenv.cfg. This is a retained historical availability observation, not a fresh attempt or a scientific validation failure. Native policy permits inspected source-catalogue fallback. |

## Limits And Additional Notes

- INQ, JUNQ and nucleolar peripheral inclusion body independent subreview: Only the three assigned current records were substantively reviewed. All are byte-unchanged; no stale record in this slice requires refresh. Current source review does not promote PROPOSED records or resolve unrelated findings.
- INQ, JUNQ and nucleolar peripheral inclusion body independent subreview: Gallardo2020 and Hiraoka2023 primary article body/captions were recovered through browser extraction of ResearchGate-hosted paper text. Gallardo repository URLs returned HTML application shells, not PDFs; publisher requests failed. Origin full PDFs and their figure pixels were not independently inspected. Native GO references corroborate bibliographic identity; root owns the bounded PMID gate.
- INQ, JUNQ and nucleolar peripheral inclusion body independent subreview: Primary main bodies and claim-bearing captions were assessed for Miller2015, Gallina2015, Sontag2023, Kaganovich2008, Rolli2024 and Boronat2023. Supplemental figures, strain tables, movies and raw data were not independently reanalysed; descriptions of them in main text remain qualified. Pixel inspection was limited to the three frozen tracked image composites.
- INQ, JUNQ and nucleolar peripheral inclusion body independent subreview: Historical JUNQ nomenclature, Sontag Keima-caption inconsistency and sampled NES-Keima fields, Rolli nuclear-dye/timing discrepancies and differing proteasome effects remain explicit rather than silently reconciled.
- INQ, JUNQ and nucleolar peripheral inclusion body independent subreview: Nine EuropePMC DOI metadata endpoints returned503; direct InterPro IPR013126 returned429. Fresh primary article metadata and successful exact protein-family match rows provide the narrower checks described, without treating these failed requests as successes.
- INQ, JUNQ and nucleolar peripheral inclusion body independent subreview: The iModulonDB result is bounded to the complete fresh20-organism/28-dataset catalogue. It does not establish biological absence, absence from other expression resources, or new runner execution. Neither yeast genus was matched, so no bacterial dataset or expression module was substituted.
- INQ, JUNQ and nucleolar peripheral inclusion body independent subreview: Full corpus QC, CI, issue deduplication and GitHub actions are root-owned. This independent reviewer performed no repository or GitHub writes. Scratch receipts and reports are the only authored files.
- Age-associated deposit, IPOD and MitoStore independent subreview: Scope: only age-associated protein deposit, IPOD and MitoStore were scientifically reviewed by this independent slice. Other PR targets and category-wide findings were not adjudicated.
- Age-associated deposit, IPOD and MitoStore independent subreview: Fresh primary sources were accessed at their individual receipt times. JATS/front/body/caption access does not mean every supplementary file, raw dataset, movie or image was analyzed. Direct pixels were inspected only for the three frozen tracked JPEGs and age2017 FigureS5 (physical PDFpp35–36).
- Age-associated deposit, IPOD and MitoStore independent subreview: Age2025 review excludes the huntingtin results subsection and supplementary datasets; age2018 is a secondary nomenclature-only caption source. Source-internal cycloheximide-dose conflict is explicitly preserved.
- Age-associated deposit, IPOD and MitoStore independent subreview: IPOD2008 primary PMC HTML was inspected after the Nature route returned a client challenge. No full online supplementary Methods or movies were retrieved. Its terminal-sequestration language is restricted to its Ubc9ts assay rather than used to deny later slow PrD-GFP turnover.
- Age-associated deposit, IPOD and MitoStore independent subreview: MitoStore2023 raw proteomics, supplemental strain workbook and extended-figure pixels were not reanalyzed. Liu2023 access is restricted to Results s2 and full Discussion; similarity is not exact identity. PXD035762 metadata conflicts remain bounded provenance already acknowledged in the record.
- Age-associated deposit, IPOD and MitoStore independent subreview: The combined EuropePMC DOI metadata request returnedHTTP503 twice and was not used as successful bibliographic evidence; article JATS fronts, authentic primary HTML and the accepted-manuscript title support the cited identities. IPR050130 initially returnedHTTP429, then a separate documented fetch succeeded; its unreviewed machine-generated functional prose is not scientific support.
- Age-associated deposit, IPOD and MitoStore independent subreview: UniProt/InterPro and taxonomy establish accession/classification identity, not localization, stoichiometry or necessity. Bounded reviewed-symbol and GO literal-name queries do not establish universal absence or cover all strains/synonyms.
- Age-associated deposit, IPOD and MitoStore independent subreview: The iModulonDB source catalogue was freshly inspected; a retained00:49Z runner PermissionError is historical and no current runner execution is claimed. No matched Saccharomyces dataset was returned, so gene/module/activity checks are N/A for this catalogue snapshot rather than negative biology.
- Age-associated deposit, IPOD and MitoStore independent subreview: Common seventeen native policy/config/schema/verifier inputs were previously read and are byte-identical to the prior accepted slice; current record/review/image inputs were freshly inspected. Only the29 listed local inputs were used; root-frozen neighbor records for other reviewers were not read here.
- Age-associated deposit, IPOD and MitoStore independent subreview: Root owns whole-corpus gates, issue deduplication and publication. This report independently inspects the six supplied target-specific native protein receipts and original-bundle validation/render evidence; it does not claim to rerun global QC.
- Bacterial aggresome, gas vesicle shell, outer lipid monolayer and parasporal crystal independent subreview: Independent agent review of these four current records and original bundles only. No repository or GitHub mutation, exhaustive literature census, neighboring whole-record review or raw-data reanalysis.
- Bacterial aggresome, gas vesicle shell, outer lipid monolayer and parasporal crystal independent subreview: Jin reading covers experimental Results, Discussion and strain/construction Methods; Pei uses the deposited accepted manuscript with explicitly bounded pages/sections and actual Figures5/6 pixels. Early model/caption passages are only partly read, and raw RNA-seq/proteomics, tracking, videos and mathematical supplements are not reanalysed.
- Bacterial aggresome, gas vesicle shell, outer lipid monolayer and parasporal crystal independent subreview: Dutka native body supports structural claims at stated section scope, with homology fitting, stripping and finite-element predictions distinguished. Bayro fresh body scope is limited to abstract/introduction and preparation context; Walsby and Hayes remain abstract scope. No new gas-vesicle image-pixel or raw NMR/tomogram audit.
- Bacterial aggresome, gas vesicle shell, outer lipid monolayer and parasporal crystal independent subreview: GvpC conditional assembly necessity remains unverified; lack of inspected proof is not a new contradictory finding. Historical whole-organelle finding dispositions are context only, not resolved or reopened by this shell review.
- Bacterial aggresome, gas vesicle shell, outer lipid monolayer and parasporal crystal independent subreview: Graef, Wang, Palma, Ben-Dov and Bravo are secondary reviews at specified scopes. Wang browser abstract does not expose the exact monolayer body passage. Austin browser-indexed primary context is distinct from direct challenge responses and does not automatically resolve the plastoglobule boundary.
- Bacterial aggresome, gas vesicle shell, outer lipid monolayer and parasporal crystal independent subreview: All seven Insell/Fitz-James1985 native scans were visually read. Historical morphology/polypeptide classes do not identify modern Cry/Cyt accessions. The1990 book chapter is metadata-only. Actual current GO phrase queries are bounded, not exhaustive ontology absence.
- Bacterial aggresome, gas vesicle shell, outer lipid monolayer and parasporal crystal independent subreview: Fresh official iModulonDB fallback is separate from the historical failed runner observation. Only precise_mg1655 and eleven named aggresome-related genes were queried; six positive modules were checked at both gene and module endpoints. All-false flags are threshold results, not absence. Generated module/InterPro prose is excluded.
- Bacterial aggresome, gas vesicle shell, outer lipid monolayer and parasporal crystal independent subreview: No matching native gas-shell or Bt dataset was found in the returned20-organism/28-dataset catalogue; no unrelated species is substituted. Material-only lipid-monolayer scope is genuinely N/A, without inventing a query defect.
- Bacterial aggresome, gas vesicle shell, outer lipid monolayer and parasporal crystal independent subreview: Native protein checks establish concrete identifier/typed-node coverage only. Aggresome and monolayer have zero typed protein nodes; monolayer also has no protein examples. Narrative molecular claims were reviewed separately where present.
- Bacterial aggresome, gas vesicle shell, outer lipid monolayer and parasporal crystal independent subreview: Root owns final corpus gates, CI, issue dedup/publication and immutable synthesis. This report records only the inspected source-head receipts, not prospective final-head success.
- Historical observations remain immutable; their old checks are not represented as current-head execution.
- The adapter runner was not rerun after the canary established OS access failure. Catalogue-based coverage is assessed directly; fresh and reused responses retain actual access timestamps.
- Native label checks include 923 no-adapter skips. Native identifier checks include 909 PMID transport failures and 254 skipped identifiers; bounded supplemental checks independently resolve the 909 PMIDs.
- Scientific record-curation findings stay in separate issues; no record is edited by this review PR.
- Final trusted-base post-save review-check, exact-head independent acceptance, final-head CI and merge-group CI occur after saving this immutable observation and are not represented here as already completed.
- All ten original YAML/Markdown pairs remain unchanged. Current main was merged normally and pushed without force.
- This explicit issue-bearing ten-record cohort follows the native persistence policy. Every inherited finding is reassessed and retains exact predecessor identity.
- Bundle issues #2628 and #2629 address two stale reviews and nine structured-source applicability defects. Scientific curation stays separately tracked and open. Existing validator #2514 remains open.
- The added self-node identifiers are assessed against current record identity, graph scope and primary sources. A historical neighboring-record review is context only; no whole-organelle finding is terminally resolved by this cohort.
- Source commit 7362758aca3756f5979304474ceb02a18f1a6ce6 is retained by tag review-base/pr2356-current-record-followup-20261103.
- CLAUDE.md is an alias of AGENTS.md; canonical regular AGENTS.md bytes are frozen.
- Used local context was frozen before assessment, including native review configuration, graph/protein policies, verifier source, six target figures, five neighboring records and the historical gas-vesicle reassessment pair. Neighbors are context, not additional curation targets.
- Three molecular-scope reviews used unsupported expression-only exemptions: gas vesicle shell, IPOD and INQ. Six omitted applicability: age-associated deposit, bacterial aggresome, JUNQ, MitoStore, nucleolar peripheral inclusion body and parasporal crystal. The lipid monolayer target has material/topology-only scope; its weak N/A wording is clarified without inventing a molecular query or extra defect.
- Fresh source inspection retains actual access dates. Primary bodies, abstracts, secondary reviews, image pixels and authority responses have distinct evidence scopes.
- Native checks with empty protein inventories or zero GENE_OR_PROTEIN nodes do not validate molecular mechanisms or names appearing only in prose. Exact represented identity, taxon, membership, location, function and assembly necessity remain separate judgments.
- One minor gas-vesicle-shell GvpA-family finding retains exact original F1 lineage and remains open for record curation. The other nine targets retain qualified scientific passes. No finding is terminally resolved by this cohort.
- Draft validation identified an invalid assessment outcome in the synthesis source. Issue #2631 tracks correcting it to the native concern enum while retaining #2630, its exact finding lineage and separate curation action. The failed uncommitted validation remains in the execution receipts.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T082440Z-pr2356-current-record-followup
kind: batch
repository: CultureBotAI/CellStructureMech
title: 'PR 2356: current-input review of ten records and adversarial follow-up'
started_at: '2026-11-03T08:10:07.354680Z'
finished_at: '2026-11-03T08:24:40Z'
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
summary: Current-input reassessment of all ten inclusion records in PR2356. The stale
  IPOD and MitoStore reviews are substantively refreshed against their added self-node
  groundings. Independent source reviews reassess the original scientific finding
  and correct nine structured-source applicability defects without editing records.
source:
  git_revision: 7362758aca3756f5979304474ceb02a18f1a6ce6
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
  - path: data/images/inclusion/age_associated_protein_deposit/pmc4635334_fig6.jpg
    sha256: abf686034f035ecdf81b1c3fb79c1504412f436b4c695c07bbcfc31525f8d74a
    role: context
  - path: data/images/inclusion/insoluble_protein_deposit/pmc5045159_pgen_1006324_g003_e27e1f28.jpg
    sha256: 89dfdd173c797ff168e0cb7be8cc0547b6b742b26324a3cec906f0d379463bd4
    role: context
  - path: data/images/inclusion/intranuclear_quality_control_compartment/pmc4389229_f3.jpg
    sha256: 9d15de2925ec7ada38d8b7281ed62110c4073fee15b464ed548b87b3687b1ecb
    role: context
  - path: data/images/inclusion/juxtanuclear_quality_control_compartment/pmc11372896_f2.jpg
    sha256: 3871c32c4ce764a616c5f0a3967acbad00edb7bc9f89a8621a06209bb2c89060
    role: context
  - path: data/images/inclusion/mitostore/pmc10068336_embj2022112309_fig_0005.jpg
    sha256: 08fe6da4832a3b949f031e367ee32323e88d73b83fece71cfd4ec02fd03e35d0
    role: context
  - path: data/images/inclusion/nucleolar_peripheral_inclusion_body/pmc10342647_ijms_24_11202_f007.jpg
    sha256: 58481911ace6752d540bdb673ede896bb5617c60b9565c83ce794a793560e22a
    role: context
  - path: data/structures/inclusion/age_associated_protein_deposit.yaml
    sha256: f782fddfb8eb004a13ce40857c05527e29272b04da88e010cec04250ca867c30
    role: target
  - path: data/structures/inclusion/bacterial_aggresome.yaml
    sha256: 8f6d6cf20835c5114b8c13bc929767a750bbb7b0db778799d7d1e1be387f8636
    role: target
  - path: data/structures/inclusion/gas_vesicle.yaml
    sha256: 7bafef7a0ce0bc91ac7189ed216f4d2cdfc786cebbd47eeb5645c5408267f7cb
    role: context
  - path: data/structures/inclusion/gas_vesicle_shell.yaml
    sha256: 06f0f2aa709e62b9e46e2e38d2ce26692fc0d8e0fe16a78d998aa7a51b1e0ae6
    role: target
  - path: data/structures/inclusion/insoluble_protein_deposit.yaml
    sha256: 8bf3ffb3c2ce2ee5448d00f88d4d0de7911e3ee135e409e174a40f5c890e5f8a
    role: target
  - path: data/structures/inclusion/intranuclear_quality_control_compartment.yaml
    sha256: 7e6cc3b1915d2093b6712f349dea34cad79831f2d4b93f0eaff29351b37f3c36
    role: target
  - path: data/structures/inclusion/juxtanuclear_quality_control_compartment.yaml
    sha256: c3fbd426fe95ef931039579f467743997b83a889fa00c53442b36f46ccd95545
    role: target
  - path: data/structures/inclusion/lipid_droplet.yaml
    sha256: 379b5b516486c6bc55055e3289a565c7854b3088a5c13ebe6f614df5c1688a7a
    role: context
  - path: data/structures/inclusion/mitostore.yaml
    sha256: c932945c5ae1c4501b217b75333c4ae85551096cd4630bdae07f3ef84b0a7dd4
    role: target
  - path: data/structures/inclusion/monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer.yaml
    sha256: d72e9789b2d49d4fe380c06834e31dfe9eaf46fb6a412ddecdc9c8e1742b7a87
    role: target
  - path: data/structures/inclusion/nucleolar_peripheral_inclusion_body.yaml
    sha256: 0882138e885027304adbb077da65d773ad7a2197cd6cb5d7ab3688a49f9c35cc
    role: target
  - path: data/structures/inclusion/parasporal_crystal.yaml
    sha256: 59163a5ec708789816078e74a74e62fd9d3dbd38b580c40103a658e711274052
    role: target
  - path: data/structures/inclusion/plastoglobule.yaml
    sha256: ba5f8ac9dd4b54fefc917e1d6ed8587fdabdb2cf6152f1e331511bfc8ee38027
    role: context
  - path: data/structures/ribonucleoprotein/h_body.yaml
    sha256: 362c852cc05cb880426858ec3392ac9fc297ebe50e9fa6f818c01bf6c8a92b8a
    role: context
  - path: data/structures/ribonucleoprotein/rnp_body.yaml
    sha256: cf7350e280e7e49db17d9218704f5190dbe6266f01aec01a7272e07f1e73637e
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
  - path: reviews/structured/20261014T054100Z-gas-vesicle-finding-reassessment/review.md
    sha256: a378369e9a8335e63e867af174c5a6b51c34358bf80207942f13ad6465bffa2b
    role: context
  - path: reviews/structured/20261014T054100Z-gas-vesicle-finding-reassessment/review.yaml
    sha256: 029b6009a71f95bed1f267a5f2928550139311a16a8fcd353db3198194548f3a
    role: context
  - path: reviews/structured/20261021T103319Z-age-associated-protein-deposit-audit/review.md
    sha256: 307b8f92be40ffec2a1795f29e20f0a4e2e21cce9b4342a3183873364c8fecf5
    role: context
  - path: reviews/structured/20261021T103319Z-age-associated-protein-deposit-audit/review.yaml
    sha256: d4a67e5e0c296086e97b1fe9dc72184c64de0c26763901d914175ba8b01cd7c1
    role: context
  - path: reviews/structured/20261021T103320Z-bacterial-aggresome-audit/review.md
    sha256: e37273dedf8d82d48f92e0ce8e2a9c5ebc57d5574da373f72008629da1f27df4
    role: context
  - path: reviews/structured/20261021T103320Z-bacterial-aggresome-audit/review.yaml
    sha256: 254d75d004f0510ec0f43a69a701f4aa35b15880047163607b0d19494e1f7996
    role: context
  - path: reviews/structured/20261021T103321Z-gas-vesicle-shell-audit/review.md
    sha256: 0fca466cd128ad89f09a643407fc081e86ff4534f650463baea8557a86fc36f8
    role: context
  - path: reviews/structured/20261021T103321Z-gas-vesicle-shell-audit/review.yaml
    sha256: 8a3c1949e16327441cfbe13ad7d3a64dff05ffc7ac69d922bb037ba23e74d6de
    role: context
  - path: reviews/structured/20261021T103322Z-insoluble-protein-deposit-audit/review.md
    sha256: 517f355667571e273d826b979c325ccda8cceee0fa0494362b77ac277bee0534
    role: context
  - path: reviews/structured/20261021T103322Z-insoluble-protein-deposit-audit/review.yaml
    sha256: 4c7447f824e0a5208a7205fd03416488eafb4d4168ee74deccdcfcb14dd99f4b
    role: context
  - path: reviews/structured/20261021T103323Z-intranuclear-quality-control-compartment-audit/review.md
    sha256: 8249af14affacd63b743bb2eba72504327f958db21ba8d48e0e7cc7864c48164
    role: context
  - path: reviews/structured/20261021T103323Z-intranuclear-quality-control-compartment-audit/review.yaml
    sha256: 93644009f66f320c56299e25142053ffdde7d7414a05a3a3aa1b23434d691b36
    role: context
  - path: reviews/structured/20261021T103324Z-juxtanuclear-quality-control-compartment-audit/review.md
    sha256: b600015dbaed42bec993385836e777fa60676edaea2b96e1d5cb17fbb1810a66
    role: context
  - path: reviews/structured/20261021T103324Z-juxtanuclear-quality-control-compartment-audit/review.yaml
    sha256: a8831fdef2d6a37efd315021570c9d64d1bbadec20dd8064b2e8795c28cfb160
    role: context
  - path: reviews/structured/20261021T103324Z-mitostore-audit/review.md
    sha256: 4e080c657040b8fd9961583962de38d00907c4bbdff7d4d9efe5003f3ec9e4e1
    role: context
  - path: reviews/structured/20261021T103324Z-mitostore-audit/review.yaml
    sha256: 92d5e6446f9ebe9066657bd78283891c3ff08545275e2d4396a5c7f083e24329
    role: context
  - path: reviews/structured/20261021T103325Z-monolayer-surrounded-lipid-storage-body-outer-lipid-monolayer-audit/review.md
    sha256: 7794560d11721ee71ab066fe108d8523edc4a97a42983937d22dcc68dce461b6
    role: context
  - path: reviews/structured/20261021T103325Z-monolayer-surrounded-lipid-storage-body-outer-lipid-monolayer-audit/review.yaml
    sha256: 0d2d19504f3f536d33f212bb370ae2b880f6c6a5e46923e1c82c32706e5ca5d7
    role: context
  - path: reviews/structured/20261021T103326Z-nucleolar-peripheral-inclusion-body-audit/review.md
    sha256: b9dc2d8b3c70dafd2d032a50acf02de5b1693f3cd53cba119d60b94bcb7c4464
    role: context
  - path: reviews/structured/20261021T103326Z-nucleolar-peripheral-inclusion-body-audit/review.yaml
    sha256: 105177fefeba1364833ea25542829cca06a6920b908d13da01d5f890cb1383fa
    role: context
  - path: reviews/structured/20261021T103327Z-parasporal-crystal-audit/review.md
    sha256: dacd0a3ca6a7c7fc980180a3bda5a597199ef5e0c8ff5cba0429f429925069e1
    role: context
  - path: reviews/structured/20261021T103327Z-parasporal-crystal-audit/review.yaml
    sha256: 9c244e37a631341163bfaa5ac5c5d254855a9be40845bf7345112bb11cc87a0b
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
- target_id: cellstructuremech:age_associated_protein_deposit
  path: data/structures/inclusion/age_associated_protein_deposit.yaml
  label: age-associated protein deposit
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/inclusion/age_associated_protein_deposit.yaml
    role: maintained scientific record
- target_id: cellstructuremech:bacterial_aggresome
  path: data/structures/inclusion/bacterial_aggresome.yaml
  label: bacterial aggresome
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/inclusion/bacterial_aggresome.yaml
    role: maintained scientific record
- target_id: GO:0033172
  path: data/structures/inclusion/gas_vesicle_shell.yaml
  label: gas vesicle shell
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/inclusion/gas_vesicle_shell.yaml
    role: maintained scientific record
- target_id: cellstructuremech:insoluble_protein_deposit
  path: data/structures/inclusion/insoluble_protein_deposit.yaml
  label: insoluble protein deposit
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/inclusion/insoluble_protein_deposit.yaml
    role: maintained scientific record
- target_id: cellstructuremech:intranuclear_quality_control_compartment
  path: data/structures/inclusion/intranuclear_quality_control_compartment.yaml
  label: intranuclear quality control compartment
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/inclusion/intranuclear_quality_control_compartment.yaml
    role: maintained scientific record
- target_id: cellstructuremech:juxtanuclear_quality_control_compartment
  path: data/structures/inclusion/juxtanuclear_quality_control_compartment.yaml
  label: juxtanuclear quality control compartment
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/inclusion/juxtanuclear_quality_control_compartment.yaml
    role: maintained scientific record
- target_id: cellstructuremech:mitostore
  path: data/structures/inclusion/mitostore.yaml
  label: MitoStore
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/inclusion/mitostore.yaml
    role: maintained scientific record
- target_id: GO:0034430
  path: data/structures/inclusion/monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer.yaml
  label: monolayer-surrounded lipid storage body outer lipid monolayer
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/inclusion/monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer.yaml
    role: maintained scientific record
- target_id: GO:0140602
  path: data/structures/inclusion/nucleolar_peripheral_inclusion_body.yaml
  label: nucleolar peripheral inclusion body
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/inclusion/nucleolar_peripheral_inclusion_body.yaml
    role: maintained scientific record
- target_id: cellstructuremech:parasporal_crystal
  path: data/structures/inclusion/parasporal_crystal.yaml
  label: parasporal crystal
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/inclusion/parasporal_crystal.yaml
    role: maintained scientific record
scope:
  description: Exact ten-record PR cohort reassessed against current main 94afdcf235c84e085e340e1a6c1dc4ab69449b03.
    Changed inputs are substantively reassessed. Scientific records remain unchanged.
  selection: Complete cohort of ten maintained records reviewed in original PR head
    d23378c3e8d1f361150365303a3eb4595893a0fa.
  coverage: full
  population_size: 10
  reviewed_target_ids:
  - cellstructuremech:age_associated_protein_deposit
  - cellstructuremech:bacterial_aggresome
  - GO:0033172
  - cellstructuremech:insoluble_protein_deposit
  - cellstructuremech:intranuclear_quality_control_compartment
  - cellstructuremech:juxtanuclear_quality_control_compartment
  - cellstructuremech:mitostore
  - GO:0034430
  - GO:0140602
  - cellstructuremech:parasporal_crystal
checks:
- check_id: qc
  name: Full native QC
  status: passed
  required: true
  target_ids:
  - cellstructuremech:age_associated_protein_deposit
  - cellstructuremech:bacterial_aggresome
  - GO:0033172
  - cellstructuremech:insoluble_protein_deposit
  - cellstructuremech:intranuclear_quality_control_compartment
  - cellstructuremech:juxtanuclear_quality_control_compartment
  - cellstructuremech:mitostore
  - GO:0034430
  - GO:0140602
  - cellstructuremech:parasporal_crystal
  command: just qc
  exit_code: 0
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  scope_note: Actual local execution at main-merge head 7362758aca3756f5979304474ceb02a18f1a6ce6.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-qc
- check_id: labels
  name: Native label correspondence
  status: passed
  required: true
  target_ids:
  - cellstructuremech:age_associated_protein_deposit
  - cellstructuremech:bacterial_aggresome
  - GO:0033172
  - cellstructuremech:insoluble_protein_deposit
  - cellstructuremech:intranuclear_quality_control_compartment
  - cellstructuremech:juxtanuclear_quality_control_compartment
  - cellstructuremech:mitostore
  - GO:0034430
  - GO:0140602
  - cellstructuremech:parasporal_crystal
  command: just validate-products
  exit_code: 0
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  scope_note: Actual local execution at main-merge head 7362758aca3756f5979304474ceb02a18f1a6ce6.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-labels
- check_id: trait-links
  name: TraitMech references
  status: passed
  required: true
  target_ids:
  - cellstructuremech:age_associated_protein_deposit
  - cellstructuremech:bacterial_aggresome
  - GO:0033172
  - cellstructuremech:insoluble_protein_deposit
  - cellstructuremech:intranuclear_quality_control_compartment
  - cellstructuremech:juxtanuclear_quality_control_compartment
  - cellstructuremech:mitostore
  - GO:0034430
  - GO:0140602
  - cellstructuremech:parasporal_crystal
  command: just check-trait-links --check
  exit_code: 0
  summary: Native TraitMech link check passed.
  scope_note: Actual local execution at main-merge head 7362758aca3756f5979304474ceb02a18f1a6ce6.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-trait-links
- check_id: vendored
  name: Pinned governed files
  status: passed
  required: true
  target_ids:
  - cellstructuremech:age_associated_protein_deposit
  - cellstructuremech:bacterial_aggresome
  - GO:0033172
  - cellstructuremech:insoluble_protein_deposit
  - cellstructuremech:intranuclear_quality_control_compartment
  - cellstructuremech:juxtanuclear_quality_control_compartment
  - cellstructuremech:mitostore
  - GO:0034430
  - GO:0140602
  - cellstructuremech:parasporal_crystal
  command: just vendored-check
  exit_code: 0
  summary: Pinned governed files match; native vendored check passed.
  scope_note: Actual local execution at main-merge head 7362758aca3756f5979304474ceb02a18f1a6ce6.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-vendored
- check_id: curies
  name: Native identifier resolver
  status: passed
  required: true
  target_ids:
  - cellstructuremech:age_associated_protein_deposit
  - cellstructuremech:bacterial_aggresome
  - GO:0033172
  - cellstructuremech:insoluble_protein_deposit
  - cellstructuremech:intranuclear_quality_control_compartment
  - cellstructuremech:juxtanuclear_quality_control_compartment
  - cellstructuremech:mitostore
  - GO:0034430
  - GO:0140602
  - cellstructuremech:parasporal_crystal
  command: just check-curies-strict
  exit_code: 0
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  scope_note: Actual local execution at main-merge head 7362758aca3756f5979304474ceb02a18f1a6ce6.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-curies
- check_id: focused-0
  name: validate cellstructuremech:age_associated_protein_deposit
  status: passed
  required: true
  target_ids:
  - cellstructuremech:age_associated_protein_deposit
  command: just validate data/structures/inclusion/age_associated_protein_deposit.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-1
  name: validate-strict cellstructuremech:age_associated_protein_deposit
  status: passed
  required: true
  target_ids:
  - cellstructuremech:age_associated_protein_deposit
  command: just validate-strict data/structures/inclusion/age_associated_protein_deposit.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-2
  name: validate cellstructuremech:bacterial_aggresome
  status: passed
  required: true
  target_ids:
  - cellstructuremech:bacterial_aggresome
  command: just validate data/structures/inclusion/bacterial_aggresome.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-3
  name: validate-strict cellstructuremech:bacterial_aggresome
  status: passed
  required: true
  target_ids:
  - cellstructuremech:bacterial_aggresome
  command: just validate-strict data/structures/inclusion/bacterial_aggresome.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-4
  name: validate GO:0033172
  status: passed
  required: true
  target_ids:
  - GO:0033172
  command: just validate data/structures/inclusion/gas_vesicle_shell.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-5
  name: validate-strict GO:0033172
  status: passed
  required: true
  target_ids:
  - GO:0033172
  command: just validate-strict data/structures/inclusion/gas_vesicle_shell.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-6
  name: validate cellstructuremech:insoluble_protein_deposit
  status: passed
  required: true
  target_ids:
  - cellstructuremech:insoluble_protein_deposit
  command: just validate data/structures/inclusion/insoluble_protein_deposit.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-7
  name: validate-strict cellstructuremech:insoluble_protein_deposit
  status: passed
  required: true
  target_ids:
  - cellstructuremech:insoluble_protein_deposit
  command: just validate-strict data/structures/inclusion/insoluble_protein_deposit.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-8
  name: validate cellstructuremech:intranuclear_quality_control_compartment
  status: passed
  required: true
  target_ids:
  - cellstructuremech:intranuclear_quality_control_compartment
  command: just validate data/structures/inclusion/intranuclear_quality_control_compartment.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-9
  name: validate-strict cellstructuremech:intranuclear_quality_control_compartment
  status: passed
  required: true
  target_ids:
  - cellstructuremech:intranuclear_quality_control_compartment
  command: just validate-strict data/structures/inclusion/intranuclear_quality_control_compartment.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-10
  name: validate cellstructuremech:juxtanuclear_quality_control_compartment
  status: passed
  required: true
  target_ids:
  - cellstructuremech:juxtanuclear_quality_control_compartment
  command: just validate data/structures/inclusion/juxtanuclear_quality_control_compartment.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-11
  name: validate-strict cellstructuremech:juxtanuclear_quality_control_compartment
  status: passed
  required: true
  target_ids:
  - cellstructuremech:juxtanuclear_quality_control_compartment
  command: just validate-strict data/structures/inclusion/juxtanuclear_quality_control_compartment.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-12
  name: validate cellstructuremech:mitostore
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitostore
  command: just validate data/structures/inclusion/mitostore.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-13
  name: validate-strict cellstructuremech:mitostore
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitostore
  command: just validate-strict data/structures/inclusion/mitostore.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-14
  name: validate GO:0034430
  status: passed
  required: true
  target_ids:
  - GO:0034430
  command: just validate data/structures/inclusion/monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-15
  name: validate-strict GO:0034430
  status: passed
  required: true
  target_ids:
  - GO:0034430
  command: just validate-strict data/structures/inclusion/monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-16
  name: validate GO:0140602
  status: passed
  required: true
  target_ids:
  - GO:0140602
  command: just validate data/structures/inclusion/nucleolar_peripheral_inclusion_body.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-17
  name: validate-strict GO:0140602
  status: passed
  required: true
  target_ids:
  - GO:0140602
  command: just validate-strict data/structures/inclusion/nucleolar_peripheral_inclusion_body.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-18
  name: validate cellstructuremech:parasporal_crystal
  status: passed
  required: true
  target_ids:
  - cellstructuremech:parasporal_crystal
  command: just validate data/structures/inclusion/parasporal_crystal.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-19
  name: validate-strict cellstructuremech:parasporal_crystal
  status: passed
  required: true
  target_ids:
  - cellstructuremech:parasporal_crystal
  command: just validate-strict data/structures/inclusion/parasporal_crystal.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: supplemental-pmid
  name: Supplemental bounded PMID authority checks
  status: passed
  required: true
  target_ids:
  - cellstructuremech:age_associated_protein_deposit
  - cellstructuremech:bacterial_aggresome
  - GO:0033172
  - cellstructuremech:insoluble_protein_deposit
  - cellstructuremech:intranuclear_quality_control_compartment
  - cellstructuremech:juxtanuclear_quality_control_compartment
  - cellstructuremech:mitostore
  - GO:0034430
  - GO:0140602
  - cellstructuremech:parasporal_crystal
  command: .venv/bin/python /private/tmp/cellstructure-batches-2346-2397-20261103/check_pmid_chunks.py
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356
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
  - cellstructuremech:age_associated_protein_deposit
  - cellstructuremech:bacterial_aggresome
  - GO:0033172
  - cellstructuremech:insoluble_protein_deposit
  - cellstructuremech:intranuclear_quality_control_compartment
  - cellstructuremech:juxtanuclear_quality_control_compartment
  - cellstructuremech:mitostore
  - GO:0034430
  - GO:0140602
  - cellstructuremech:parasporal_crystal
  summary: 'Applicability was assessed against the official catalogue and actual molecular
    assertions. The six yeast-related targets have no matching Saccharomyces or Schizosaccharomyces
    catalogue coverage. Bacterial aggresome checks use bounded MG1655 gene/module
    data and retain six positive module contexts and five all-false cases as context
    only, not component membership, causal evidence or biological absence. Gas-shell
    and parasporal scopes retain organism-specific catalogue limits. The outer lipid
    monolayer has material/topology-only scope without an identified gene/locus/protein
    or molecular pathway to query. Nine original reviews require correction: three
    unsupported expression-only exemptions and six omissions. Historical native-runner
    unavailability is separate, with no fresh invocation or success claimed.'
  evidence_ids:
  - plaque-catalogue
  - micro-adapter-catalogue
  - septin-current-adapter-catalogue
  - septin-adapter-mg1655-meta
  - septin-adapter-search-hslU
  - septin-adapter-hslU-gene
  - septin-adapter-hslU-modules
  - septin-adapter-search-kbl
  - septin-adapter-kbl-gene
  - septin-adapter-kbl-modules
  - septin-adapter-search-acnB
  - septin-adapter-acnB-gene
  - septin-adapter-acnB-modules
  - septin-adapter-search-nuoJ
  - septin-adapter-nuoJ-gene
  - septin-adapter-nuoJ-modules
  - septin-adapter-search-nlpE
  - septin-adapter-nlpE-gene
  - septin-adapter-nlpE-modules
  - septin-adapter-search-glpK
  - septin-adapter-glpK-gene
  - septin-adapter-glpK-modules
  - septin-adapter-search-mukF
  - septin-adapter-mukF-gene
  - septin-adapter-mukF-modules
  - septin-adapter-search-rnb
  - septin-adapter-rnb-gene
  - septin-adapter-rnb-modules
  - septin-adapter-search-rbn
  - septin-adapter-rbn-gene
  - septin-adapter-rbn-modules
  - septin-adapter-search-orn
  - septin-adapter-orn-gene
  - septin-adapter-orn-modules
  - septin-adapter-search-hokB
  - septin-adapter-hokB-gene
  - septin-adapter-hokB-modules
  - septin-adapter-module-10-detail
  - septin-adapter-module-10-genes
  - septin-adapter-module-31-detail
  - septin-adapter-module-31-genes
  - septin-adapter-module-37-detail
  - septin-adapter-module-37-genes
  - septin-adapter-module-66-detail
  - septin-adapter-module-66-genes
  - septin-adapter-module-78-detail
  - septin-adapter-module-78-genes
  - septin-adapter-module-112-detail
  - septin-adapter-module-112-genes
- check_id: independent-scientific-review
  name: Independent claim-level source review
  status: passed
  required: true
  target_ids:
  - cellstructuremech:age_associated_protein_deposit
  - cellstructuremech:bacterial_aggresome
  - GO:0033172
  - cellstructuremech:insoluble_protein_deposit
  - cellstructuremech:intranuclear_quality_control_compartment
  - cellstructuremech:juxtanuclear_quality_control_compartment
  - cellstructuremech:mitostore
  - GO:0034430
  - GO:0140602
  - cellstructuremech:parasporal_crystal
  summary: Three read-only reviewers covered the complete ten-record cohort, including
    changed inputs, with explicit scientific findings and source-access limits. Final
    artifact/head acceptance occurs after saving.
  evidence_ids:
  - plaque-image-4
  - plaque-image-5
  - plaque-image-8
  - plaque-native-review-policy
  - plaque-inq-go
  - plaque-inq-P53286
  - plaque-inq-P31539
  - plaque-inq-Q12510
  - plaque-inq-interpro-P53286
  - plaque-inq-interpro-P31539
  - plaque-inq-interpro-Q12510
  - plaque-inq-IPR050853
  - plaque-inq-taxon-4932
  - plaque-inq-taxon-559292
  - plaque-inq-miller2015-pmc
  - plaque-inq-gallina2015-jats
  - plaque-inq-sontag2023-jats
  - plaque-inq-gallina2015-package
  - plaque-junq-go
  - plaque-junq-tax-1247190
  - plaque-junq-IPR001270
  - plaque-junq-IPR050130
  - plaque-junq-jats-PMC11372896
  - plaque-junq-native-package-PMC11372896
  - plaque-nur-go
  - plaque-nur-tax-284812
  - plaque-nur-tax-4896
  - plaque-nur-Q9UUE5
  - plaque-nur-Q9Y8G3
  - plaque-nur-Q10265
  - plaque-nur-O59855
  - plaque-nur-O74752
  - plaque-nur-O94641
  - plaque-nur-matches-Q9UUE5
  - plaque-nur-matches-Q9Y8G3
  - plaque-nur-matches-Q10265
  - plaque-nur-matches-O59855
  - plaque-nur-matches-O74752
  - plaque-nur-matches-O94641
  - plaque-nur-IPR011502
  - plaque-nur-IPR030217
  - plaque-nur-IPR044713
  - plaque-nur-jats-PMC10342647
  - plaque-nur-native-package-PMC10342647
  - plaque-kaganovich-jats
  - plaque-btn2-domain
  - plaque-gallardo-browser-retrieval
  - plaque-hiraoka-browser-retrieval
  - micro-age2015-primary
  - micro-age2017-primary
  - micro-age2025-primary
  - micro-age2018-secondary-nomenclature
  - micro-ipod2008-primary
  - micro-ipod2016-primary
  - micro-ipod2024-primary
  - micro-mitostore2023-primary
  - micro-mitostore-tom70-comparison
  - micro-pride-mitostore
  - micro-go
  - micro-tax-4932
  - micro-tax-559292
  - micro-tax-1247190
  - micro-uniprot-Q12329
  - micro-matches-Q12329
  - micro-uniprot-P15992
  - micro-matches-P15992
  - micro-uniprot-P31539
  - micro-matches-P31539
  - micro-uniprot-P10591
  - micro-matches-P10591
  - micro-uniprot-P10592
  - micro-matches-P10592
  - micro-uniprot-P25491
  - micro-matches-P25491
  - micro-uniprot-P05453
  - micro-matches-P05453
  - micro-family-IPR031107
  - micro-family-IPR013126
  - micro-family-IPR003285
  - micro-family-IPR001270
  - micro-family-IPR050130
  - micro-adapter-catalogue
  - micro-review-policy
  - micro-review-config
  - micro-image-package-age_associated_protein_deposit
  - micro-image-package-insoluble_protein_deposit
  - micro-image-package-mitostore
  - septin-aggresome-agent-PMC8528417
  - septin-aggresome-agent-pei2025-aam
  - septin-root19-sources-jats-PMC10185304
  - septin-root19-sources-legacy-PMC3271001
  - septin-root19-sources-legacy-PMC372955
  - septin-root19-sources-jats-PMC5947121
  - septin-root19-sources-jats-PMC3229976
  - septin-parasporal-agent-jats-PMC4280536
  - septin-parasporal-agent-jats-PMC4014730
  - septin-parasporal-agent-legacy-PMC1857359
  - septin-aggresome-agent-go
  - septin-aggresome-agent-so
  - septin-root19-sources-gas-shell-go
  - septin-root19-sources-lipid-monolayer-go
  - septin-parasporal-agent-go
  - septin-root19-sources-CHEBI-16247
  - septin-aggresome-agent-tax-83333
  - septin-aggresome-agent-tax-511145
  - septin-root19-sources-NCBITaxon-2
  - septin-root19-sources-NCBITaxon-2157
  - septin-root19-sources-NCBITaxon-315271
  - septin-root19-sources-NCBITaxon-2692880
  - septin-root19-sources-NCBITaxon-4932
  - septin-parasporal-agent-tax-1428
  - septin-parasporal-agent-tax-1430
  - septin-aggresome-agent-P0A6H5
  - septin-aggresome-agent-P0AB77
  - septin-aggresome-agent-P36683
  - septin-root19-sources-UniProtKB-A0ABR7ZBW9
  - septin-root19-sources-UniProtKB-A0ABR7ZCB1
  - septin-parasporal-agent-P16480
  - septin-parasporal-agent-P21256
  - septin-parasporal-agent-P0A382
  - septin-aggresome-agent-IPR004491
  - septin-aggresome-agent-IPR011282
  - septin-aggresome-agent-IPR004406
  - septin-root19-sources-PF00741
  - septin-root19-sources-PF01304
  - septin-root19-sources-IPR000638
  - septin-root19-sources-IPR047870
  - septin-root19-sources-IPR050530
  - septin-root19-sources-IPR002003
  - septin-root19-sources-IPR018185
  - septin-parasporal-agent-IPR038979
  - septin-parasporal-agent-IPR001615
  - septin-aggresome-agent-ipr-matches-P0A6H5
  - septin-aggresome-agent-ipr-matches-P0AB77
  - septin-aggresome-agent-ipr-matches-P36683
  - septin-parasporal-agent-matches-P16480
  - septin-parasporal-agent-matches-P21256
  - septin-parasporal-agent-matches-P0A382
  - septin-root19-sources-permeability1992-crossref
  - septin-parasporal-agent-crossref-book
  - septin-parasporal-agent-insell1985-page56
  - septin-parasporal-agent-insell1985-page57
  - septin-parasporal-agent-insell1985-page58
  - septin-parasporal-agent-insell1985-page59
  - septin-parasporal-agent-insell1985-page60
  - septin-parasporal-agent-insell1985-page61
  - septin-parasporal-agent-insell1985-page62
  - septin-permeability1992-browser-current
  - septin-wang2015-browser-current
  - septin-austin2006-browser-current
  - septin-current-adapter-catalogue
  - septin-adapter-mg1655-meta
  - septin-adapter-hslU-gene
  - septin-adapter-hslU-modules
  - septin-adapter-kbl-gene
  - septin-adapter-kbl-modules
  - septin-adapter-acnB-gene
  - septin-adapter-acnB-modules
  - septin-adapter-nuoJ-gene
  - septin-adapter-nuoJ-modules
  - septin-adapter-nlpE-gene
  - septin-adapter-nlpE-modules
  - septin-adapter-glpK-gene
  - septin-adapter-glpK-modules
  - septin-adapter-mukF-gene
  - septin-adapter-mukF-modules
  - septin-adapter-rnb-gene
  - septin-adapter-rnb-modules
  - septin-adapter-rbn-gene
  - septin-adapter-rbn-modules
  - septin-adapter-orn-gene
  - septin-adapter-orn-modules
  - septin-adapter-hokB-gene
  - septin-adapter-hokB-modules
  - septin-adapter-module-10-detail
  - septin-adapter-module-10-genes
  - septin-adapter-module-31-detail
  - septin-adapter-module-31-genes
  - septin-adapter-module-37-detail
  - septin-adapter-module-37-genes
  - septin-adapter-module-66-detail
  - septin-adapter-module-66-genes
  - septin-adapter-module-78-detail
  - septin-adapter-module-78-genes
  - septin-adapter-module-112-detail
  - septin-adapter-module-112-genes
  - septin-native-review-policy
- check_id: historical-adapter-runner
  name: Retained historical adapter runner availability
  status: unavailable
  required: false
  target_ids:
  - cellstructuremech:age_associated_protein_deposit
  - cellstructuremech:bacterial_aggresome
  - GO:0033172
  - cellstructuremech:insoluble_protein_deposit
  - cellstructuremech:intranuclear_quality_control_compartment
  - cellstructuremech:juxtanuclear_quality_control_compartment
  - cellstructuremech:mitostore
  - GO:0140602
  - cellstructuremech:parasporal_crystal
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
- check_id: age_associated_protein_deposit-uniprot-verify
  name: Native age-associated protein deposit UniProt verify check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:age_associated_protein_deposit
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/age_associated_protein_deposit.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories or zero molecular
    graph nodes do not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-age_associated_protein_deposit-verify
- check_id: age_associated_protein_deposit-uniprot-causal
  name: Native age-associated protein deposit UniProt causal check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:age_associated_protein_deposit
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/age_associated_protein_deposit.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories or zero molecular
    graph nodes do not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-age_associated_protein_deposit-causal
- check_id: bacterial_aggresome-uniprot-verify
  name: Native bacterial aggresome UniProt verify check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:bacterial_aggresome
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/bacterial_aggresome.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories or zero molecular
    graph nodes do not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-bacterial_aggresome-verify
- check_id: bacterial_aggresome-uniprot-causal
  name: Native bacterial aggresome UniProt causal check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:bacterial_aggresome
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/bacterial_aggresome.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories or zero molecular
    graph nodes do not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-bacterial_aggresome-causal
- check_id: gas_vesicle_shell-uniprot-verify
  name: Native gas vesicle shell UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0033172
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/gas_vesicle_shell.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories or zero molecular
    graph nodes do not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-gas_vesicle_shell-verify
- check_id: gas_vesicle_shell-uniprot-causal
  name: Native gas vesicle shell UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0033172
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/gas_vesicle_shell.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories or zero molecular
    graph nodes do not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-gas_vesicle_shell-causal
- check_id: insoluble_protein_deposit-uniprot-verify
  name: Native insoluble protein deposit UniProt verify check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:insoluble_protein_deposit
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/insoluble_protein_deposit.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories or zero molecular
    graph nodes do not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-insoluble_protein_deposit-verify
- check_id: insoluble_protein_deposit-uniprot-causal
  name: Native insoluble protein deposit UniProt causal check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:insoluble_protein_deposit
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/insoluble_protein_deposit.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories or zero molecular
    graph nodes do not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-insoluble_protein_deposit-causal
- check_id: intranuclear_quality_control_compartment-uniprot-verify
  name: Native intranuclear quality control compartment UniProt verify check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:intranuclear_quality_control_compartment
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/intranuclear_quality_control_compartment.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories or zero molecular
    graph nodes do not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-intranuclear_quality_control_compartment-verify
- check_id: intranuclear_quality_control_compartment-uniprot-causal
  name: Native intranuclear quality control compartment UniProt causal check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:intranuclear_quality_control_compartment
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/intranuclear_quality_control_compartment.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories or zero molecular
    graph nodes do not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-intranuclear_quality_control_compartment-causal
- check_id: juxtanuclear_quality_control_compartment-uniprot-verify
  name: Native juxtanuclear quality control compartment UniProt verify check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:juxtanuclear_quality_control_compartment
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/juxtanuclear_quality_control_compartment.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories or zero molecular
    graph nodes do not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-juxtanuclear_quality_control_compartment-verify
- check_id: juxtanuclear_quality_control_compartment-uniprot-causal
  name: Native juxtanuclear quality control compartment UniProt causal check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:juxtanuclear_quality_control_compartment
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/juxtanuclear_quality_control_compartment.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories or zero molecular
    graph nodes do not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-juxtanuclear_quality_control_compartment-causal
- check_id: mitostore-uniprot-verify
  name: Native MitoStore UniProt verify check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitostore
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/mitostore.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories or zero molecular
    graph nodes do not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-mitostore-verify
- check_id: mitostore-uniprot-causal
  name: Native MitoStore UniProt causal check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitostore
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/mitostore.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories or zero molecular
    graph nodes do not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-mitostore-causal
- check_id: monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer-uniprot-verify
  name: Native monolayer-surrounded lipid storage body outer lipid monolayer UniProt
    verify check
  status: passed
  required: true
  target_ids:
  - GO:0034430
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories or zero molecular
    graph nodes do not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer-verify
- check_id: monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer-uniprot-causal
  name: Native monolayer-surrounded lipid storage body outer lipid monolayer UniProt
    causal check
  status: passed
  required: true
  target_ids:
  - GO:0034430
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories or zero molecular
    graph nodes do not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer-causal
- check_id: nucleolar_peripheral_inclusion_body-uniprot-verify
  name: Native nucleolar peripheral inclusion body UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0140602
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/nucleolar_peripheral_inclusion_body.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories or zero molecular
    graph nodes do not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-nucleolar_peripheral_inclusion_body-verify
- check_id: nucleolar_peripheral_inclusion_body-uniprot-causal
  name: Native nucleolar peripheral inclusion body UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0140602
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/nucleolar_peripheral_inclusion_body.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories or zero molecular
    graph nodes do not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-nucleolar_peripheral_inclusion_body-causal
- check_id: parasporal_crystal-uniprot-verify
  name: Native parasporal crystal UniProt verify check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:parasporal_crystal
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/parasporal_crystal.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories or zero molecular
    graph nodes do not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-parasporal_crystal-verify
- check_id: parasporal_crystal-uniprot-causal
  name: Native parasporal crystal UniProt causal check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:parasporal_crystal
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/parasporal_crystal.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories or zero molecular
    graph nodes do not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-parasporal_crystal-causal
evidence:
- evidence_id: current-record-0
  kind: record_content
  reference: data/structures/inclusion/age_associated_protein_deposit.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T08:24:40Z'
  support: context_only
  summary: Original frozen SHA256 f782fddfb8eb004a13ce40857c05527e29272b04da88e010cec04250ca867c30;
    current SHA256 f782fddfb8eb004a13ce40857c05527e29272b04da88e010cec04250ca867c30.
    Record bytes unchanged since the original review.
  snapshot_sha256: f782fddfb8eb004a13ce40857c05527e29272b04da88e010cec04250ca867c30
- evidence_id: original-review-0
  kind: prior_review
  reference: reviews/structured/20261021T103319Z-age-associated-protein-deposit-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T08:24:40Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: d4a67e5e0c296086e97b1fe9dc72184c64de0c26763901d914175ba8b01cd7c1
- evidence_id: current-record-1
  kind: record_content
  reference: data/structures/inclusion/bacterial_aggresome.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T08:24:40Z'
  support: context_only
  summary: Original frozen SHA256 8f6d6cf20835c5114b8c13bc929767a750bbb7b0db778799d7d1e1be387f8636;
    current SHA256 8f6d6cf20835c5114b8c13bc929767a750bbb7b0db778799d7d1e1be387f8636.
    Record bytes unchanged since the original review.
  snapshot_sha256: 8f6d6cf20835c5114b8c13bc929767a750bbb7b0db778799d7d1e1be387f8636
- evidence_id: original-review-1
  kind: prior_review
  reference: reviews/structured/20261021T103320Z-bacterial-aggresome-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T08:24:40Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 254d75d004f0510ec0f43a69a701f4aa35b15880047163607b0d19494e1f7996
- evidence_id: current-record-2
  kind: record_content
  reference: data/structures/inclusion/gas_vesicle_shell.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T08:24:40Z'
  support: context_only
  summary: Original frozen SHA256 06f0f2aa709e62b9e46e2e38d2ce26692fc0d8e0fe16a78d998aa7a51b1e0ae6;
    current SHA256 06f0f2aa709e62b9e46e2e38d2ce26692fc0d8e0fe16a78d998aa7a51b1e0ae6.
    Record bytes unchanged since the original review.
  snapshot_sha256: 06f0f2aa709e62b9e46e2e38d2ce26692fc0d8e0fe16a78d998aa7a51b1e0ae6
- evidence_id: original-review-2
  kind: prior_review
  reference: reviews/structured/20261021T103321Z-gas-vesicle-shell-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T08:24:40Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 8a3c1949e16327441cfbe13ad7d3a64dff05ffc7ac69d922bb037ba23e74d6de
- evidence_id: current-record-3
  kind: record_content
  reference: data/structures/inclusion/insoluble_protein_deposit.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T08:24:40Z'
  support: context_only
  summary: Original frozen SHA256 45a74ced04c8c5714cd45f6a8a04c45ae8a5af22a04809aa51520c54884fb773;
    current SHA256 8bf3ffb3c2ce2ee5448d00f88d4d0de7911e3ee135e409e174a40f5c890e5f8a.
    Changed record reassessed against current sources.
  snapshot_sha256: 8bf3ffb3c2ce2ee5448d00f88d4d0de7911e3ee135e409e174a40f5c890e5f8a
- evidence_id: original-review-3
  kind: prior_review
  reference: reviews/structured/20261021T103322Z-insoluble-protein-deposit-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T08:24:40Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 4c7447f824e0a5208a7205fd03416488eafb4d4168ee74deccdcfcb14dd99f4b
- evidence_id: current-record-4
  kind: record_content
  reference: data/structures/inclusion/intranuclear_quality_control_compartment.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T08:24:40Z'
  support: context_only
  summary: Original frozen SHA256 7e6cc3b1915d2093b6712f349dea34cad79831f2d4b93f0eaff29351b37f3c36;
    current SHA256 7e6cc3b1915d2093b6712f349dea34cad79831f2d4b93f0eaff29351b37f3c36.
    Record bytes unchanged since the original review.
  snapshot_sha256: 7e6cc3b1915d2093b6712f349dea34cad79831f2d4b93f0eaff29351b37f3c36
- evidence_id: original-review-4
  kind: prior_review
  reference: reviews/structured/20261021T103323Z-intranuclear-quality-control-compartment-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T08:24:40Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 93644009f66f320c56299e25142053ffdde7d7414a05a3a3aa1b23434d691b36
- evidence_id: current-record-5
  kind: record_content
  reference: data/structures/inclusion/juxtanuclear_quality_control_compartment.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T08:24:40Z'
  support: context_only
  summary: Original frozen SHA256 c3fbd426fe95ef931039579f467743997b83a889fa00c53442b36f46ccd95545;
    current SHA256 c3fbd426fe95ef931039579f467743997b83a889fa00c53442b36f46ccd95545.
    Record bytes unchanged since the original review.
  snapshot_sha256: c3fbd426fe95ef931039579f467743997b83a889fa00c53442b36f46ccd95545
- evidence_id: original-review-5
  kind: prior_review
  reference: reviews/structured/20261021T103324Z-juxtanuclear-quality-control-compartment-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T08:24:40Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: a8831fdef2d6a37efd315021570c9d64d1bbadec20dd8064b2e8795c28cfb160
- evidence_id: current-record-6
  kind: record_content
  reference: data/structures/inclusion/mitostore.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T08:24:40Z'
  support: context_only
  summary: Original frozen SHA256 6863a577037a5f308979f0c7cdcccda5b49ebe7f64586192cef53ca27291347a;
    current SHA256 c932945c5ae1c4501b217b75333c4ae85551096cd4630bdae07f3ef84b0a7dd4.
    Changed record reassessed against current sources.
  snapshot_sha256: c932945c5ae1c4501b217b75333c4ae85551096cd4630bdae07f3ef84b0a7dd4
- evidence_id: original-review-6
  kind: prior_review
  reference: reviews/structured/20261021T103324Z-mitostore-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T08:24:40Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 92d5e6446f9ebe9066657bd78283891c3ff08545275e2d4396a5c7f083e24329
- evidence_id: current-record-7
  kind: record_content
  reference: data/structures/inclusion/monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T08:24:40Z'
  support: context_only
  summary: Original frozen SHA256 d72e9789b2d49d4fe380c06834e31dfe9eaf46fb6a412ddecdc9c8e1742b7a87;
    current SHA256 d72e9789b2d49d4fe380c06834e31dfe9eaf46fb6a412ddecdc9c8e1742b7a87.
    Record bytes unchanged since the original review.
  snapshot_sha256: d72e9789b2d49d4fe380c06834e31dfe9eaf46fb6a412ddecdc9c8e1742b7a87
- evidence_id: original-review-7
  kind: prior_review
  reference: reviews/structured/20261021T103325Z-monolayer-surrounded-lipid-storage-body-outer-lipid-monolayer-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T08:24:40Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 0d2d19504f3f536d33f212bb370ae2b880f6c6a5e46923e1c82c32706e5ca5d7
- evidence_id: current-record-8
  kind: record_content
  reference: data/structures/inclusion/nucleolar_peripheral_inclusion_body.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T08:24:40Z'
  support: context_only
  summary: Original frozen SHA256 0882138e885027304adbb077da65d773ad7a2197cd6cb5d7ab3688a49f9c35cc;
    current SHA256 0882138e885027304adbb077da65d773ad7a2197cd6cb5d7ab3688a49f9c35cc.
    Record bytes unchanged since the original review.
  snapshot_sha256: 0882138e885027304adbb077da65d773ad7a2197cd6cb5d7ab3688a49f9c35cc
- evidence_id: original-review-8
  kind: prior_review
  reference: reviews/structured/20261021T103326Z-nucleolar-peripheral-inclusion-body-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T08:24:40Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 105177fefeba1364833ea25542829cca06a6920b908d13da01d5f890cb1383fa
- evidence_id: current-record-9
  kind: record_content
  reference: data/structures/inclusion/parasporal_crystal.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T08:24:40Z'
  support: context_only
  summary: Original frozen SHA256 59163a5ec708789816078e74a74e62fd9d3dbd38b580c40103a658e711274052;
    current SHA256 59163a5ec708789816078e74a74e62fd9d3dbd38b580c40103a658e711274052.
    Record bytes unchanged since the original review.
  snapshot_sha256: 59163a5ec708789816078e74a74e62fd9d3dbd38b580c40103a658e711274052
- evidence_id: original-review-9
  kind: prior_review
  reference: reviews/structured/20261021T103327Z-parasporal-crystal-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T08:24:40Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 9c244e37a631341163bfaa5ac5c5d254855a9be40845bf7345112bb11cc87a0b
- evidence_id: plaque-current-4
  kind: record_content
  reference: data/structures/inclusion/intranuclear_quality_control_compartment.yaml
  locator: Entire maintained record, including discussion qualifications and image
    metadata
  accessed_at: '2026-11-03T08:18:59.067381Z'
  summary: Complete unchanged current input independently read; scientific judgments
    apply to these exact bytes.
  support: supports
  snapshot_sha256: 7e6cc3b1915d2093b6712f349dea34cad79831f2d4b93f0eaff29351b37f3c36
- evidence_id: plaque-original-4
  kind: prior_review
  reference: reviews/structured/20261021T103323Z-intranuclear-quality-control-compartment-audit/review.yaml
  locator: Original complete YAML and paired rendered Markdown
  accessed_at: '2026-11-03T08:18:59.067381Z'
  summary: Historical original has pass_with_limitations and no findings; no prior
    scientific finding is silently closed. Current reassessment preserves the original
    unchanged.
  support: supports
  snapshot_sha256: 93644009f66f320c56299e25142053ffdde7d7414a05a3a3aa1b23434d691b36
- evidence_id: plaque-image-4
  kind: primary_source
  reference: data/images/inclusion/intranuclear_quality_control_compartment/pmc4389229_f3.jpg
  locator: Actual frozen image pixels visually inspected in this review; full multi-panel
    composite, not just its caption
  accessed_at: '2026-11-03T08:18:59.067381Z'
  summary: Image pixels and panel labels inspected. Local SHA256 matches the record;
    local MD5 matches the freshly fetched native PMC package media row. Caption and
    exact CC BY4.0 attribution assessed separately from JATS.
  support: supports
  snapshot_sha256: 9d15de2925ec7ada38d8b7281ed62110c4073fee15b464ed548b87b3687b1ecb
- evidence_id: plaque-current-5
  kind: record_content
  reference: data/structures/inclusion/juxtanuclear_quality_control_compartment.yaml
  locator: Entire maintained record, including discussion qualifications and image
    metadata
  accessed_at: '2026-11-03T08:18:59.067381Z'
  summary: Complete unchanged current input independently read; scientific judgments
    apply to these exact bytes.
  support: supports
  snapshot_sha256: c3fbd426fe95ef931039579f467743997b83a889fa00c53442b36f46ccd95545
- evidence_id: plaque-original-5
  kind: prior_review
  reference: reviews/structured/20261021T103324Z-juxtanuclear-quality-control-compartment-audit/review.yaml
  locator: Original complete YAML and paired rendered Markdown
  accessed_at: '2026-11-03T08:18:59.067381Z'
  summary: Historical original has pass_with_limitations and no findings; no prior
    scientific finding is silently closed. Current reassessment preserves the original
    unchanged.
  support: supports
  snapshot_sha256: a8831fdef2d6a37efd315021570c9d64d1bbadec20dd8064b2e8795c28cfb160
- evidence_id: plaque-image-5
  kind: primary_source
  reference: data/images/inclusion/juxtanuclear_quality_control_compartment/pmc11372896_f2.jpg
  locator: Actual frozen image pixels visually inspected in this review; full multi-panel
    composite, not just its caption
  accessed_at: '2026-11-03T08:18:59.067381Z'
  summary: Image pixels and panel labels inspected. Local SHA256 matches the record;
    local MD5 matches the freshly fetched native PMC package media row. Caption and
    exact CC BY4.0 attribution assessed separately from JATS.
  support: supports
  snapshot_sha256: 3871c32c4ce764a616c5f0a3967acbad00edb7bc9f89a8621a06209bb2c89060
- evidence_id: plaque-current-8
  kind: record_content
  reference: data/structures/inclusion/nucleolar_peripheral_inclusion_body.yaml
  locator: Entire maintained record, including discussion qualifications and image
    metadata
  accessed_at: '2026-11-03T08:18:59.067381Z'
  summary: Complete unchanged current input independently read; scientific judgments
    apply to these exact bytes.
  support: supports
  snapshot_sha256: 0882138e885027304adbb077da65d773ad7a2197cd6cb5d7ab3688a49f9c35cc
- evidence_id: plaque-original-8
  kind: prior_review
  reference: reviews/structured/20261021T103326Z-nucleolar-peripheral-inclusion-body-audit/review.yaml
  locator: Original complete YAML and paired rendered Markdown
  accessed_at: '2026-11-03T08:18:59.067381Z'
  summary: Historical original has pass_with_limitations and no findings; no prior
    scientific finding is silently closed. Current reassessment preserves the original
    unchanged.
  support: supports
  snapshot_sha256: 105177fefeba1364833ea25542829cca06a6920b908d13da01d5f890cb1383fa
- evidence_id: plaque-image-8
  kind: primary_source
  reference: data/images/inclusion/nucleolar_peripheral_inclusion_body/pmc10342647_ijms_24_11202_f007.jpg
  locator: Actual frozen image pixels visually inspected in this review; full multi-panel
    composite, not just its caption
  accessed_at: '2026-11-03T08:18:59.067381Z'
  summary: Image pixels and panel labels inspected. Local SHA256 matches the record;
    local MD5 matches the freshly fetched native PMC package media row. Caption and
    exact CC BY4.0 attribution assessed separately from JATS.
  support: supports
  snapshot_sha256: 58481911ace6752d540bdb673ede896bb5617c60b9565c83ce794a793560e22a
- evidence_id: plaque-native-review-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Structured Source Cross-Checks; Evidence Rules; native profile and current
    schema
  accessed_at: '2026-11-03T08:18:59.067381Z'
  summary: Named genes, proteins, pathways and stress responses require actual structured-source
    applicability assessment; a lack of expression claims alone does not exempt a
    record. Runner unavailability allows an honestly described source fallback.
  support: supports
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: plaque-inq-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0016604,GO:0016234,GO:0005634,GO:0097165
  locator: Native JSON response
  accessed_at: '2026-11-03T08:13:34.454164Z'
  summary: 'Native GO definitions/labels: GO:0005634 nucleus; GO:0016234 inclusion
    body; GO:0016604 nuclear body; GO:0097165 nuclear stress granule. Structural identity
    and is-a/parthood are assessed against the primary scope.'
  support: supports
  snapshot_sha256: 6fad49bdc72bf568b34cb2973957faf8be1273852c41d8e4b2c4cf55beda0f24
- evidence_id: plaque-inq-go-search-0
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=INQ&limit=100&page=1
  locator: Native JSON response
  accessed_at: '2026-11-03T08:13:34.455378Z'
  summary: QuickGO query returned numberOfHits=0; 0 results inspected on requested
    first page. No exact INQ identity was observed in this bounded result set; related
    processes are not adopted as structural identity.
  support: supports
  snapshot_sha256: f3a7dae9b1e9335291e3940cdf0e5f8dadf9335da7b9547710606b5106c63f86
  search_scope: 'QuickGO; exact query URL https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=INQ&limit=100&page=1;
    accessed 2026-11-03T08:13:34.455378Z; requested page=1, limit=100, returned page
    metadata {''resultsPerPage'': 100, ''current'': 0, ''total'': 0}; limited to returned
    terms, not global absence.'
- evidence_id: plaque-inq-go-search-1
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=intranuclear+quality+control&limit=100&page=1
  locator: Native JSON response
  accessed_at: '2026-11-03T08:13:34.456328Z'
  summary: QuickGO query returned numberOfHits=89; 89 results inspected on requested
    first page. No exact INQ identity was observed in this bounded result set; related
    processes are not adopted as structural identity.
  support: supports
  snapshot_sha256: c383e6530c470a4464b3c00bd16cbc3a63ca40e1f1915e20acdd4a1b5b0f1b80
  search_scope: 'QuickGO; exact query URL https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=intranuclear+quality+control&limit=100&page=1;
    accessed 2026-11-03T08:13:34.456328Z; requested page=1, limit=100, returned page
    metadata {''resultsPerPage'': 100, ''current'': 1, ''total'': 1}; limited to returned
    terms, not global absence.'
- evidence_id: plaque-inq-ols-exact
  kind: search
  reference: https://www.ebi.ac.uk/ols4/api/search?q=intranuclear+quality+control+compartment&ontology=go&exact=true&rows=100
  locator: Native JSON response
  accessed_at: '2026-11-03T08:13:34.457283Z'
  summary: Exact GO-ontology OLS query returned 0 terms. This bounded search supports
    retaining the local mint provisionally, not exhaustive ontology absence.
  support: supports
  snapshot_sha256: 8d33fdeb26a2d16294a3c5f4a7f444578bb462aa6036d45a15e9bfadfe47fbd2
  search_scope: OLS4 GO ontology; exact query URL https://www.ebi.ac.uk/ols4/api/search?q=intranuclear+quality+control+compartment&ontology=go&exact=true&rows=100;
    accessed 2026-11-03T08:13:34.457283Z; exact=true, first response rows=100; no
    other ontologies or spelling variants searched by this row.
- evidence_id: plaque-inq-P53286
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P53286.json
  locator: Native JSON response
  accessed_at: '2026-11-03T08:13:34.458353Z'
  summary: Native UniProtKB reviewed (Swiss-Prot) accession P53286; primary genes
    ['BTN2']; taxon 559292. Authority verifies identity, not inclusion localization
    or necessity.
  support: supports
  snapshot_sha256: d0122a2554484d191dfb1e8f702aeaca61392ab658f762dbc30916c27580c110
- evidence_id: plaque-inq-query-BTN2
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A559292+AND+gene_exact%3ABTN2&format=json&size=500
  locator: Native JSON response
  accessed_at: '2026-11-03T08:13:34.459296Z'
  summary: Bounded reviewed exact-gene/taxon query returned ['P53286']; corroborates
    declared reference-sequence example, not the experimental strain or in situ role.
  support: supports
  snapshot_sha256: b2f4bdbd062bb47911a6c781f0eeb60f29e4558d1e1772e425012e87471f5159
  search_scope: UniProtKB; exact query URL https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A559292+AND+gene_exact%3ABTN2&format=json&size=500;
    accessed 2026-11-03T08:13:34.459296Z; one response, size as encoded in URL (100
    or500); no unreviewed or sequence-similarity search, no biological absence inference.
- evidence_id: plaque-inq-P31539
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P31539.json
  locator: Native JSON response
  accessed_at: '2026-11-03T08:13:34.460312Z'
  summary: Native UniProtKB reviewed (Swiss-Prot) accession P31539; primary genes
    ['HSP104']; taxon 559292. Authority verifies identity, not inclusion localization
    or necessity.
  support: supports
  snapshot_sha256: 8636decea760cdb2a2da238bfa589822867a778a41fd6a04c45a74fe5802ee13
- evidence_id: plaque-inq-query-HSP104
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A559292+AND+gene_exact%3AHSP104&format=json&size=500
  locator: Native JSON response
  accessed_at: '2026-11-03T08:13:34.461308Z'
  summary: Bounded reviewed exact-gene/taxon query returned ['P31539']; corroborates
    declared reference-sequence example, not the experimental strain or in situ role.
  support: supports
  snapshot_sha256: 4e2938a5a1292a9626b18e30b225ebfc7a30d63069235f01cd0bc3d007279322
  search_scope: UniProtKB; exact query URL https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A559292+AND+gene_exact%3AHSP104&format=json&size=500;
    accessed 2026-11-03T08:13:34.461308Z; one response, size as encoded in URL (100
    or500); no unreviewed or sequence-similarity search, no biological absence inference.
- evidence_id: plaque-inq-Q12510
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q12510.json
  locator: Native JSON response
  accessed_at: '2026-11-03T08:13:35.074702Z'
  summary: Native UniProtKB reviewed (Swiss-Prot) accession Q12510; primary genes
    ['CMR1']; taxon 559292. Authority verifies identity, not inclusion localization
    or necessity.
  support: supports
  snapshot_sha256: 1239def629e5b6dff77c2943d8e36218cb3b65349df792cd534d1accb4e6c126
- evidence_id: plaque-inq-query-CMR1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A559292+AND+gene_exact%3ACMR1&format=json&size=500
  locator: Native JSON response
  accessed_at: '2026-11-03T08:13:35.081991Z'
  summary: Bounded reviewed exact-gene/taxon query returned ['Q12510']; corroborates
    declared reference-sequence example, not the experimental strain or in situ role.
  support: supports
  snapshot_sha256: 44046a9911dff52899aa764915540f9310dbfcd4465e52a163db7d7ccab21fec
  search_scope: UniProtKB; exact query URL https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A559292+AND+gene_exact%3ACMR1&format=json&size=500;
    accessed 2026-11-03T08:13:35.081991Z; one response, size as encoded in URL (100
    or500); no unreviewed or sequence-similarity search, no biological absence inference.
- evidence_id: plaque-inq-interpro-P53286
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P53286/?page_size=200
  locator: Native JSON response
  accessed_at: '2026-11-03T08:13:35.082807Z'
  summary: 'Integrated InterPro match set count=1, next=None: IPR062150/BTN2-like,
    N-terminal domain/domain. Family/domain types are distinguished; membership is
    not localization evidence.'
  support: supports
  snapshot_sha256: 2150123692223413fbe5ca58407117f0775384d53d6c3c9d16f7af500dbea6ab
- evidence_id: plaque-inq-interpro-P31539
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P31539/?page_size=200
  locator: Native JSON response
  accessed_at: '2026-11-03T08:13:35.131551Z'
  summary: 'Integrated InterPro match set count=11, next=None: IPR001270/ClpA/B family/family;
    IPR003593/AAA+ ATPase domain/domain; IPR003959/ATPase, AAA-type, core/domain;
    IPR004176/Clp, repeat (R) N-terminal domain/domain; IPR018368/ClpA/B, conserved
    site 1/conserved_site; IPR019489/Clp ATPase, C-terminal/domain; IPR027417/P-loop
    containing nucleoside triphosphate hydrolase/homologous_superfamily; IPR028299/ClpA/B,
    conserved site 2/conserved_site; IPR036628/Clp, N-terminal domain superfamily/homologous_superfamily;
    IPR041546/ClpA/ClpB, AAA lid domain/domain; IPR050130/ATP-dependent Clp protease/Chaperone
    ClpA/ClpB/family. Family/domain types are distinguished; membership is not localization
    evidence.'
  support: supports
  snapshot_sha256: 750867aa538d4dd5c6c6a982138e7401b8b788d9653ecb84bf5d145c8ff6d3ee
- evidence_id: plaque-inq-interpro-Q12510
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q12510/?page_size=200
  locator: Native JSON response
  accessed_at: '2026-11-03T08:13:35.252565Z'
  summary: 'Integrated InterPro match set count=5, next=None: IPR001680/WD40 repeat/repeat;
    IPR015943/WD40/YVTN repeat-like-containing domain superfamily/homologous_superfamily;
    IPR019775/WD40 repeat, conserved site/conserved_site; IPR036322/WD40-repeat-containing
    domain superfamily/homologous_superfamily; IPR050853/WD repeat-containing DNA
    damage-binding protein/family. Family/domain types are distinguished; membership
    is not localization evidence.'
  support: supports
  snapshot_sha256: 53626d2b59f132b8d9318a1ffbfa366ed96077f4955e5793ac029eb6e052e610
- evidence_id: plaque-inq-IPR050853
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050853/
  locator: Native JSON response
  accessed_at: '2026-11-03T08:13:35.536837Z'
  summary: InterPro IPR050853 has name WD repeat-containing DNA damage-binding protein
    and type family. Only identity/type is used; unchecked generated descriptions
    are excluded.
  support: supports
  snapshot_sha256: ea066ab30aab6f2701eebcb4ece6aeabf81226bd0203014ff051b7247895f686
- evidence_id: plaque-inq-taxon-4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Native JSON response
  accessed_at: '2026-11-03T08:13:35.745938Z'
  summary: ENA native taxonomy authority resolves 4932 to Saccharomyces cerevisiae
    at rank species; reference strain versus assayed mutant/strain remains separately
    qualified.
  support: supports
  snapshot_sha256: 38f43dd1593a1d47416228ae385464f30aeb8302c3aadb45b3588d03744bc814
- evidence_id: plaque-inq-taxon-559292
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Native JSON response
  accessed_at: '2026-11-03T08:13:35.807122Z'
  summary: ENA native taxonomy authority resolves 559292 to Saccharomyces cerevisiae
    S288C at rank strain; reference strain versus assayed mutant/strain remains separately
    qualified.
  support: supports
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: plaque-inq-miller2015-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC4369314/?report=xml
  locator: Full main body Results sec3/sec7/sec8, Figures2/6/7 captions, DOI/PMID
    article metadata
  accessed_at: '2026-11-03T08:13:36.369032Z'
  summary: 'Miller2015 primary full article HTML: Results on nuclear localization,
    Fig2, Btn2 deposition/degradation Fig6, engineered Hsp42-NLS rescue Fig7 and captions.
    Supplemental panels/videos not independently inspected.'
  support: supports
  snapshot_sha256: f20fb119597617332413ef1f89339807c5ed7ce01d6f4548b4b02a67bde467e1
- evidence_id: plaque-inq-gallina2015-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4389229.1/PMC4389229.1.xml
  locator: Results Cmr1 marks INQ; Btn2 promotes Mrc1 turnover; Discussion; Methods
    strain paragraph; Figure3 and JATS license
  accessed_at: '2026-11-03T08:13:36.397359Z'
  summary: Gallina2015 primary main body and Fig3 distinguish nuclear Cmr1-associated
    inclusions, heterogeneous cargo, marker stability, residual deletion phenotypes
    and stress-specific targeting. Mrc1 recruitment does not require Cmr1. Default
    W303 and S288C library contexts remain distinct.
  support: supports
  snapshot_sha256: ee9cb1c4fe41567584285f617bea8a6e42d5fdd99989c71689ddedd86c85ded9
- evidence_id: plaque-inq-sontag2023-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC12349969.1/PMC12349969.1.xml
  locator: Main Results S1-S9; Figures1-8 captions; Methods; article DOI/PMID
  accessed_at: '2026-11-03T08:13:36.489195Z'
  summary: Sontag2023 primary main Results separate nuclear INQ from cytoplasmic JUNQ,
    convergence from fusion, Q-body congregation from uniform body architecture, and
    vacuolar clearance from universal degradation. Genetic phenotypes and Keima/turnover
    readouts remain reporter-specific.
  support: supports
  snapshot_sha256: b01cac2d5de22e22250023435417325276855d8685f38d072c994ff3835264bb
- evidence_id: plaque-inq-gallina2015-package
  kind: database
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4389229.1/PMC4389229.1.json
  locator: PMC article package metadata, DOI/PMID/license and exact figure media MD5
  accessed_at: '2026-11-03T08:13:36.615976Z'
  summary: PMC package PMC4389229 version 1 identifies DOI 10.1038/ncomms7533, PMID
    25817432; exact figure media MD5 matches the frozen local bytes. JATS provides
    exact license version.
  support: supports
  snapshot_sha256: 7e3fcca1320858765ebb4cd1b04864f9ef2fd2233c34a18186536d3fc61a3e1a
- evidence_id: plaque-junq-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000502,GO:0005737,GO:0016234
  locator: Native JSON response
  accessed_at: '2026-11-03T08:13:36.798494Z'
  summary: 'Native GO definitions/labels: GO:0005737 cytoplasm; GO:0016234 inclusion
    body; GO:0000502 proteasome complex. Structural identity and is-a/parthood are
    assessed against the primary scope.'
  support: supports
  snapshot_sha256: ddcfd757d780f31d977e1a7839919a81610de0f00d9fd45e805eb4b3f344a931
- evidence_id: plaque-junq-ols-exact-0
  kind: search
  reference: https://www.ebi.ac.uk/ols4/api/search?ontology=go&exact=true&rows=100&q=juxtanuclear%20quality%20control%20compartment
  locator: Native JSON response
  accessed_at: '2026-11-03T08:13:36.814792Z'
  summary: Exact GO-ontology OLS query returned 0 terms. This bounded search supports
    retaining the local mint provisionally, not exhaustive ontology absence.
  support: supports
  snapshot_sha256: 8d33fdeb26a2d16294a3c5f4a7f444578bb462aa6036d45a15e9bfadfe47fbd2
  search_scope: OLS4 GO ontology; exact query URL https://www.ebi.ac.uk/ols4/api/search?ontology=go&exact=true&rows=100&q=juxtanuclear%20quality%20control%20compartment;
    accessed 2026-11-03T08:13:36.814792Z; exact=true, first response rows=100; no
    other ontologies or spelling variants searched by this row.
- evidence_id: plaque-junq-ols-exact-1
  kind: search
  reference: https://www.ebi.ac.uk/ols4/api/search?ontology=go&exact=true&rows=100&q=JUNQ
  locator: Native JSON response
  accessed_at: '2026-11-03T08:13:36.849026Z'
  summary: Exact GO-ontology OLS query returned 0 terms. This bounded search supports
    retaining the local mint provisionally, not exhaustive ontology absence.
  support: supports
  snapshot_sha256: 8d33fdeb26a2d16294a3c5f4a7f444578bb462aa6036d45a15e9bfadfe47fbd2
  search_scope: OLS4 GO ontology; exact query URL https://www.ebi.ac.uk/ols4/api/search?ontology=go&exact=true&rows=100&q=JUNQ;
    accessed 2026-11-03T08:13:36.849026Z; exact=true, first response rows=100; no
    other ontologies or spelling variants searched by this row.
- evidence_id: plaque-junq-tax-1247190
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1247190
  locator: Native JSON response
  accessed_at: '2026-11-03T08:13:36.858172Z'
  summary: ENA native taxonomy authority resolves 1247190 to Saccharomyces cerevisiae
    BY4741 at rank strain; reference strain versus assayed mutant/strain remains separately
    qualified.
  support: supports
  snapshot_sha256: caee974f39d598c4001a51c78b0dc0c7dfba575de9526277d845019da6abe202
- evidence_id: plaque-junq-IPR001270
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001270/
  locator: Native JSON response
  accessed_at: '2026-11-03T08:13:36.940760Z'
  summary: InterPro IPR001270 has name ClpA/B family and type family. Only identity/type
    is used; unchecked generated descriptions are excluded.
  support: supports
  snapshot_sha256: ed0a09c17fa611e58cd0d00b904d4dce2757228cd7e411301eddcfb9b391e0dd
- evidence_id: plaque-junq-IPR050130
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050130/
  locator: Native JSON response
  accessed_at: '2026-11-03T08:13:36.990699Z'
  summary: InterPro IPR050130 has name ATP-dependent Clp protease/Chaperone ClpA/ClpB
    and type family. Only identity/type is used; unchecked generated descriptions
    are excluded.
  support: supports
  snapshot_sha256: e654bc8d2d359d203a225be0690247071616a63341156fcd507f197717f78701
- evidence_id: plaque-junq-jats-PMC11372896
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC11372896.1/PMC11372896.1.xml
  locator: Methods Table2 and mitochondrial-labeling method; Results3.1-3.5; Discussion;
    Figure2; JATS license
  accessed_at: '2026-11-03T08:13:37.458433Z'
  summary: Rolli2024 primary Results support chaperone-dependent sorting, double-Ssa1/Ssa2
    peripheral deposits, Btn2/Hsp42 sorting and Atg1/Atg8-sensitive clearance. Discussion
    leaves vacuolar entry unresolved and excludes conclusions from Vps15/34 expression-limited
    assays.
  support: supports
  snapshot_sha256: b6be17605a2b0e162d7009f2140697abb9d5518a8b9840df19386d261964ec17
- evidence_id: plaque-junq-native-package-PMC11372896
  kind: database
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC11372896.1/PMC11372896.1.json
  locator: PMC article package metadata, DOI/PMID/license and exact figure media MD5
  accessed_at: '2026-11-03T08:13:37.585459Z'
  summary: PMC package PMC11372896 version 1 identifies DOI 10.3389/fmolb.2024.1427542,
    PMID 39234568; exact figure media MD5 matches the frozen local bytes. JATS provides
    exact license version.
  support: supports
  snapshot_sha256: 4430274db21b43506a7de60d78ba67a6a0a51db491e22a1c6a685143c0e9306d
- evidence_id: plaque-nur-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005634,GO:0042405,GO:0140602
  locator: Native JSON response
  accessed_at: '2026-11-03T08:13:37.634727Z'
  summary: 'Native GO definitions/labels: GO:0005634 nucleus; GO:0140602 nucleolar
    peripheral inclusion body; GO:0042405 nuclear inclusion body. Structural identity
    and is-a/parthood are assessed against the primary scope.'
  support: supports
  snapshot_sha256: ed0fad74f93229a98cb4bf1808c8ab547b64bf72c417834a8b99c9221918eae3
- evidence_id: plaque-nur-tax-284812
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/284812
  locator: Native JSON response
  accessed_at: '2026-11-03T08:13:37.663145Z'
  summary: ENA native taxonomy authority resolves 284812 to Schizosaccharomyces pombe
    972h- at rank strain; reference strain versus assayed mutant/strain remains separately
    qualified.
  support: supports
  snapshot_sha256: 948c040cabf6c036dff451c7b6eac22605d0ed5d60a74f471e4431e63f82f721
- evidence_id: plaque-nur-tax-4896
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4896
  locator: Native JSON response
  accessed_at: '2026-11-03T08:13:37.896352Z'
  summary: ENA native taxonomy authority resolves 4896 to Schizosaccharomyces pombe
    at rank species; reference strain versus assayed mutant/strain remains separately
    qualified.
  support: supports
  snapshot_sha256: 42c5b7d3d99341137803612d6404cd3884e2d06ec8a740b1ad38163c678f6721
- evidence_id: plaque-nur-Q9UUE5
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q9UUE5.json
  locator: Native JSON response
  accessed_at: '2026-11-03T08:13:37.901917Z'
  summary: Native UniProtKB reviewed (Swiss-Prot) accession Q9UUE5; primary genes
    ['nup85']; taxon 284812. Authority verifies identity, not inclusion localization
    or necessity.
  support: supports
  snapshot_sha256: 7f54caaf1c1943813420d66d670d02d4622dff3c10d729d4fce45142fce9e6d2
- evidence_id: plaque-nur-query-nup85
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3Anup85%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29&size=100
  locator: Native JSON response
  accessed_at: '2026-11-03T08:13:38.006464Z'
  summary: Bounded reviewed exact-gene/taxon query returned ['Q9UUE5']; corroborates
    declared reference-sequence example, not the experimental strain or in situ role.
  support: supports
  snapshot_sha256: 46e6938d84e6c36fcd7f75956c9946eb07903c2e40cf9671ba5cd9c4e31f63ee
  search_scope: UniProtKB; exact query URL https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3Anup85%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29&size=100;
    accessed 2026-11-03T08:13:38.006464Z; one response, size as encoded in URL (100
    or500); no unreviewed or sequence-similarity search, no biological absence inference.
- evidence_id: plaque-nur-Q9Y8G3
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q9Y8G3.json
  locator: Native JSON response
  accessed_at: '2026-11-03T08:13:38.013055Z'
  summary: Native UniProtKB reviewed (Swiss-Prot) accession Q9Y8G3; primary genes
    ['mex67']; taxon 284812. Authority verifies identity, not inclusion localization
    or necessity.
  support: supports
  snapshot_sha256: 1f8b9e383a57b1b9d6b4b39c9fede0989b3ce6b30562394f9b2f396b5c9fd90b
- evidence_id: plaque-nur-query-mex67
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3Amex67%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29&size=100
  locator: Native JSON response
  accessed_at: '2026-11-03T08:13:38.113933Z'
  summary: Bounded reviewed exact-gene/taxon query returned ['Q9Y8G3']; corroborates
    declared reference-sequence example, not the experimental strain or in situ role.
  support: supports
  snapshot_sha256: 24768c19d244d1dd494de671cc13474a02bd080882f5e53cb67ecc6231464ac2
  search_scope: UniProtKB; exact query URL https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3Amex67%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29&size=100;
    accessed 2026-11-03T08:13:38.113933Z; one response, size as encoded in URL (100
    or500); no unreviewed or sequence-similarity search, no biological absence inference.
- evidence_id: plaque-nur-Q10265
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q10265.json
  locator: Native JSON response
  accessed_at: '2026-11-03T08:13:38.229176Z'
  summary: Native UniProtKB reviewed (Swiss-Prot) accession Q10265; primary genes
    ['ssa1']; taxon 284812. Authority verifies identity, not inclusion localization
    or necessity.
  support: supports
  snapshot_sha256: 053fb978d20a8b4e28b6ee2afdc05e4f00c4b77e805c719cd44a044e9acc9877
- evidence_id: plaque-nur-query-ssa1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3Assa1%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29&size=100
  locator: Native JSON response
  accessed_at: '2026-11-03T08:13:38.314433Z'
  summary: Bounded reviewed exact-gene/taxon query returned ['Q10265']; corroborates
    declared reference-sequence example, not the experimental strain or in situ role.
  support: supports
  snapshot_sha256: a3d9e3d9bfd816dae011b720ca1787ae0edb99c0ea1e0330bef64947606f267e
  search_scope: UniProtKB; exact query URL https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3Assa1%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29&size=100;
    accessed 2026-11-03T08:13:38.314433Z; one response, size as encoded in URL (100
    or500); no unreviewed or sequence-similarity search, no biological absence inference.
- evidence_id: plaque-nur-O59855
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/O59855.json
  locator: Native JSON response
  accessed_at: '2026-11-03T08:13:38.493016Z'
  summary: Native UniProtKB reviewed (Swiss-Prot) accession O59855; primary genes
    ['ssa2']; taxon 284812. Authority verifies identity, not inclusion localization
    or necessity.
  support: supports
  snapshot_sha256: 2419884600b38d85190c1cf4a3e81dacd46d94f33ab2d59462247540d89951b8
- evidence_id: plaque-nur-query-ssa2
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3Assa2%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29&size=100
  locator: Native JSON response
  accessed_at: '2026-11-03T08:13:38.551843Z'
  summary: Bounded reviewed exact-gene/taxon query returned ['O59855']; corroborates
    declared reference-sequence example, not the experimental strain or in situ role.
  support: supports
  snapshot_sha256: 279c6fb862c8bea3d273e9b1f9c0979e3389c23e6b281ce6366b685a50e7cec0
  search_scope: UniProtKB; exact query URL https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3Assa2%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29&size=100;
    accessed 2026-11-03T08:13:38.551843Z; one response, size as encoded in URL (100
    or500); no unreviewed or sequence-similarity search, no biological absence inference.
- evidence_id: plaque-nur-O74752
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/O74752.json
  locator: Native JSON response
  accessed_at: '2026-11-03T08:13:38.871741Z'
  summary: Native UniProtKB reviewed (Swiss-Prot) accession O74752; primary genes
    ['mas5']; taxon 284812. Authority verifies identity, not inclusion localization
    or necessity.
  support: supports
  snapshot_sha256: cf14dd7673c8e8e8dc7c2db585494a44bccdb7dad8fb7b25015c2dd15f2a16a9
- evidence_id: plaque-nur-query-mas5
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3Amas5%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29&size=100
  locator: Native JSON response
  accessed_at: '2026-11-03T08:13:38.877732Z'
  summary: Bounded reviewed exact-gene/taxon query returned ['O74752']; corroborates
    declared reference-sequence example, not the experimental strain or in situ role.
  support: supports
  snapshot_sha256: d8be58f4e506b6901fbfdadea64bb81b7dd728aaf87359cf8bf0e4e57a5c41ac
  search_scope: UniProtKB; exact query URL https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3Amas5%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29&size=100;
    accessed 2026-11-03T08:13:38.877732Z; one response, size as encoded in URL (100
    or500); no unreviewed or sequence-similarity search, no biological absence inference.
- evidence_id: plaque-nur-O94641
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/O94641.json
  locator: Native JSON response
  accessed_at: '2026-11-03T08:13:39.574063Z'
  summary: Native UniProtKB reviewed (Swiss-Prot) accession O94641; primary genes
    ['hsp104']; taxon 284812. Authority verifies identity, not inclusion localization
    or necessity.
  support: supports
  snapshot_sha256: 2c5a7ea22c014c0ee45d20567370851bfbd9464d6f41ebde692ff0ccfdf1590c
- evidence_id: plaque-nur-query-hsp104
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3Ahsp104%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29&size=100
  locator: Native JSON response
  accessed_at: '2026-11-03T08:13:39.738782Z'
  summary: Bounded reviewed exact-gene/taxon query returned ['O94641']; corroborates
    declared reference-sequence example, not the experimental strain or in situ role.
  support: supports
  snapshot_sha256: 5067c38a1ae0b65220a9b4ea996788aafe95658d4065cd31be24c9da09d7f086
  search_scope: UniProtKB; exact query URL https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3Ahsp104%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29&size=100;
    accessed 2026-11-03T08:13:39.738782Z; one response, size as encoded in URL (100
    or500); no unreviewed or sequence-similarity search, no biological absence inference.
- evidence_id: plaque-nur-matches-Q9UUE5
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q9UUE5/?page_size=200
  locator: Native JSON response
  accessed_at: '2026-11-03T08:13:39.741237Z'
  summary: 'Integrated InterPro match set count=1, next=None: IPR011502/Nucleoporin
    Nup85-like/family. Family/domain types are distinguished; membership is not localization
    evidence.'
  support: supports
  snapshot_sha256: 933f6ebb6962cfd0e0aeb7cba2e24917c8ee5ed88da057bf372990ff75bc7f95
- evidence_id: plaque-nur-matches-Q9Y8G3
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q9Y8G3/?page_size=200
  locator: Native JSON response
  accessed_at: '2026-11-03T08:13:40.563866Z'
  summary: 'Integrated InterPro match set count=10, next=None: IPR001611/Leucine-rich
    repeat/repeat; IPR002075/Nuclear transport factor 2 domain/domain; IPR005637/TAP
    C-terminal (TAP-C) domain/domain; IPR009060/UBA-like superfamily/homologous_superfamily;
    IPR018222/Nuclear transport factor 2, eukaryote/domain; IPR030217/Nuclear RNA
    export factor/family; IPR032675/Leucine-rich repeat domain superfamily/homologous_superfamily;
    IPR032710/NTF2-like domain superfamily/homologous_superfamily; IPR040736/Mex67,
    RNA recognition motif/domain; IPR057125/NXF1/2/3/5-like, leucine-rich repeat domain/domain.
    Family/domain types are distinguished; membership is not localization evidence.'
  support: supports
  snapshot_sha256: c74aa834be55186d22ffc26f0703ec884b877f38c40bcb5cd9a982eb702e8cf8
- evidence_id: plaque-nur-matches-Q10265
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q10265/?page_size=200
  locator: Native JSON response
  accessed_at: '2026-11-03T08:13:40.780356Z'
  summary: 'Integrated InterPro match set count=5, next=None: IPR013126/Heat shock
    protein 70 family/family; IPR018181/Heat shock protein 70, conserved site/conserved_site;
    IPR029047/Heat shock protein 70kD, peptide-binding domain superfamily/homologous_superfamily;
    IPR029048/Heat shock protein 70kD, C-terminal domain superfamily/homologous_superfamily;
    IPR043129/ATPase, nucleotide binding domain/homologous_superfamily. Family/domain
    types are distinguished; membership is not localization evidence.'
  support: supports
  snapshot_sha256: 9c20e0458ce64dd17303163d283ec854640f5a44dd507335a8d073b06a5dc320
- evidence_id: plaque-nur-matches-O59855
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/O59855/?page_size=200
  locator: Native JSON response
  accessed_at: '2026-11-03T08:13:41.020870Z'
  summary: 'Integrated InterPro match set count=5, next=None: IPR013126/Heat shock
    protein 70 family/family; IPR018181/Heat shock protein 70, conserved site/conserved_site;
    IPR029047/Heat shock protein 70kD, peptide-binding domain superfamily/homologous_superfamily;
    IPR029048/Heat shock protein 70kD, C-terminal domain superfamily/homologous_superfamily;
    IPR043129/ATPase, nucleotide binding domain/homologous_superfamily. Family/domain
    types are distinguished; membership is not localization evidence.'
  support: supports
  snapshot_sha256: c45f03fc1211909a10bac4be788019b4050652e3bc58c72877c0b3826e0aa047
- evidence_id: plaque-nur-matches-O74752
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/O74752/?page_size=200
  locator: Native JSON response
  accessed_at: '2026-11-03T08:13:41.823065Z'
  summary: 'Integrated InterPro match set count=9, next=None: IPR001305/Heat shock
    protein DnaJ, cysteine-rich domain/domain; IPR001623/DnaJ domain/domain; IPR002939/Chaperone
    DnaJ, C-terminal/domain; IPR008971/HSP40/DnaJ peptide-binding/homologous_superfamily;
    IPR012724/Chaperone DnaJ/family; IPR018253/DnaJ domain, conserved site/conserved_site;
    IPR036410/Heat shock protein DnaJ, cysteine-rich domain superfamily/homologous_superfamily;
    IPR036869/Chaperone J-domain superfamily/homologous_superfamily; IPR044713/DnaJ
    homolog subfamily A member 1/2-like/family. Family/domain types are distinguished;
    membership is not localization evidence.'
  support: supports
  snapshot_sha256: a8d3b889f7bdda331026333efe9384d2f3d6394239b5a1bbbcf9d35b2a2c706b
- evidence_id: plaque-nur-matches-O94641
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/O94641/?page_size=200
  locator: Native JSON response
  accessed_at: '2026-11-03T08:13:41.917137Z'
  summary: 'Integrated InterPro match set count=11, next=None: IPR001270/ClpA/B family/family;
    IPR003593/AAA+ ATPase domain/domain; IPR003959/ATPase, AAA-type, core/domain;
    IPR004176/Clp, repeat (R) N-terminal domain/domain; IPR018368/ClpA/B, conserved
    site 1/conserved_site; IPR019489/Clp ATPase, C-terminal/domain; IPR027417/P-loop
    containing nucleoside triphosphate hydrolase/homologous_superfamily; IPR028299/ClpA/B,
    conserved site 2/conserved_site; IPR036628/Clp, N-terminal domain superfamily/homologous_superfamily;
    IPR041546/ClpA/ClpB, AAA lid domain/domain; IPR050130/ATP-dependent Clp protease/Chaperone
    ClpA/ClpB/family. Family/domain types are distinguished; membership is not localization
    evidence.'
  support: supports
  snapshot_sha256: 6e38816460aea9b8b904b1be2cb4282132d78ba079377141698fe4500d4deef7
- evidence_id: plaque-nur-IPR011502
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR011502/
  locator: Native JSON response
  accessed_at: '2026-11-03T08:13:41.958329Z'
  summary: InterPro IPR011502 has name Nucleoporin Nup85-like and type family. Only
    identity/type is used; unchecked generated descriptions are excluded.
  support: supports
  snapshot_sha256: 3fd5472f108f657d4d7af5667166f8d377cfb5c0b4bd1eeabe593e3558805467
- evidence_id: plaque-nur-IPR030217
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR030217/
  locator: Native JSON response
  accessed_at: '2026-11-03T08:13:41.969722Z'
  summary: InterPro IPR030217 has name Nuclear RNA export factor and type family.
    Only identity/type is used; unchecked generated descriptions are excluded.
  support: supports
  snapshot_sha256: 9b32f880e181cf615e36aa9320449eb6424a8ad9d8d97028e39b8f0854422501
- evidence_id: plaque-nur-IPR044713
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR044713/
  locator: Native JSON response
  accessed_at: '2026-11-03T08:13:42.593428Z'
  summary: InterPro IPR044713 has name DnaJ homolog subfamily A member 1/2-like and
    type family. Only identity/type is used; unchecked generated descriptions are
    excluded.
  support: supports
  snapshot_sha256: 3ec369677634cd064a7d7f9347ecb7e9a6ce23e468a5a2d0b4f86b835ff59b80
- evidence_id: plaque-nur-jats-PMC10342647
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC10342647.1/PMC10342647.1.xml
  locator: Results2.5; Fig7a-c caption; Methods4.3; JATS exact license and DOI/PMID
  accessed_at: '2026-11-03T08:13:43.377079Z'
  summary: Boronat2023 main Results2.5, Fig7 and Methods4.3 support severe-heat NuRs,
    Mas5-dependent fission-yeast reporters and chaperone localization. Budding-yeast
    W303/BY4741 experiments and W303-specific concentration are explicitly distinct.
  support: supports
  snapshot_sha256: 0d9e2ef9309ef2e4467b02c001c4919d47818a1423120307660a6fee775d7552
- evidence_id: plaque-nur-native-package-PMC10342647
  kind: database
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC10342647.1/PMC10342647.1.json
  locator: PMC article package metadata, DOI/PMID/license and exact figure media MD5
  accessed_at: '2026-11-03T08:13:43.491078Z'
  summary: PMC package PMC10342647 version 1 identifies DOI 10.3390/ijms241311202,
    PMID 37446379; exact figure media MD5 matches the frozen local bytes. JATS provides
    exact license version.
  support: supports
  snapshot_sha256: 3c1b51d3c79b6d45de60c44b57038bcd6baca139e8e531d549a36f570cf1eda5
- evidence_id: plaque-kaganovich-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2746971.1/PMC2746971.1.xml
  locator: Primary article Results S3/S4/S6; Figures4-6 captions; DOI/PMID metadata
  accessed_at: '2026-11-03T08:13:43.506617Z'
  summary: Kaganovich2008 primary Results S4/S6 support historical JUNQ-designated
    proteasome/Hsp104 association and cooling-dependent diffuse Ubc9Ts fluorescence
    recovery. These historical assignments and fluorescence readouts do not prove
    universal modern JUNQ composition or catalytic reactivation.
  support: supports
  snapshot_sha256: 996840915479e90023d1156f228a06a38248f8e2ea97d52db9fb0e3ca62dce5a
- evidence_id: plaque-catalogue
  kind: search
  reference: https://imodulondb.org/api/datasets
  locator: Entire returned organism and dataset listing
  accessed_at: '2026-11-03T08:13:43.657552Z'
  summary: Fresh catalogue contains 20 organisms and 28 dataset keys. Every returned
    organism row was inspected; no Saccharomyces or Schizosaccharomyces dataset is
    listed. No matched gene/module lookup is warranted for these yeast targets; unrelated
    bacterial Hsp homologs are not substitutes.
  support: context_only
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  search_scope: iModulonDB dataset catalogue; GET https://imodulondb.org/api/datasets;
    accessed 2026-11-03T08:13:43.657552Z; entire unpaginated returned 20-organism/28-key
    JSON listing, exact organism comparison for Saccharomyces cerevisiae and Schizosaccharomyces
    pombe; no broader search or biological absence claim.
- evidence_id: plaque-btn2-domain
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR062150/
  locator: Native JSON response
  accessed_at: '2026-11-03T08:13:43.733260Z'
  summary: InterPro IPR062150 has name BTN2-like, N-terminal domain and type domain.
    Only identity/type is used; unchecked generated descriptions are excluded.
  support: supports
  snapshot_sha256: 052706313e73f7f6ab7d3e132b810e14be2212db1662112174f4a522ed92fed1
- evidence_id: plaque-gallardo-browser-retrieval
  kind: primary_source
  reference: https://www.researchgate.net/publication/346538874_Acute_Heat_Stress_Leads_to_Reversible_Aggregation_of_Nuclear_Proteins_into_Nucleolar_Rings_in_Fission_Yeast
  locator: Browser-extracted primary article body and captions; frozen retrieval JSON
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-plaque/gallardo-browser-retrieval.json
  accessed_at: '2026-11-03T08:15:45.402Z'
  summary: 'Primary paper text recovered through browser extraction: selective nuclear
    recruitment, reduced Nup85/Mex67 mobility, heat/recovery, residual preconditioning
    and Hsf1/Hsp104 perturbations agree with the bounded record. Origin repository
    returned an HTML shell; no PDF or supplemental pixels were read.'
  support: supports
  snapshot_sha256: 32ae84d2c425262ac1c5875e62f7c72a0507a619076d710ec5c4392594f81276
- evidence_id: plaque-hiraoka-browser-retrieval
  kind: primary_source
  reference: https://www.researchgate.net/publication/370466123_CDK_actively_contributes_to_establishment_of_the_stationary_phase_state_in_fission_yeast
  locator: Browser-extracted primary article body and captions; frozen retrieval JSON
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-plaque/hiraoka-browser-retrieval.json
  accessed_at: '2026-11-03T08:14:33.059Z'
  summary: 'Primary paper text recovered through browser extraction: Fig3/Results
    distinguish peripheral Cdc2/Cdc13/Clp1 from central Gar1/Gar2 during stationary
    phase/glucose depletion. This supports starvation scope without equating it mechanistically
    with acute heat; publisher and curl host requests returned403.'
  support: supports
  snapshot_sha256: 9c87f0d787caf911b1aa5df38c2150370e06c0bc974b931a2ba42c921d7b1329
- evidence_id: plaque-source-access-limitations
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-plaque/source-receipts.json
  locator: Actual fresh curl receipts/statuses and body hashes; extra-source-receipts.json
    records later alternatives
  accessed_at: '2026-11-03T08:18:59.067381Z'
  summary: Nine EuropePMC metadata requests returned503; the direct IPR013126 entry
    returned429, but both exact Ssa protein integrated-match lists independently returned
    the family identity/name/type. Miller S3 JATS404 was replaced by full PMC HTML.
    Gallardo repository responses were HTML shells and publisher403; Hiraoka curl
    endpoints403. Browser primary text fallbacks are separate evidence, not successful
    origin downloads.
  support: context_only
  snapshot_sha256: 2238590352f7a4ae2f6e5617ce7a88cef3a74f7932475372641ae5d3f5f23670
- evidence_id: plaque-original-validation
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-plaque/original-validation.json
  locator: Three original native validate/render executions and all historical source.inputs
    checked with git show
  accessed_at: '2026-11-03T08:11:08.120354Z'
  summary: Each original validates with exit0, deterministic render matches saved
    Markdown exactly, and every frozen historical input hash matches its original
    source commit. Historical checks remain historical and are not presented as fresh
    scientific review.
  support: supports
  snapshot_sha256: ccbb066a36cc9b24f7c66250a1eca6cca2c16c0f547d8d05b0ea87fa8e70fc49
- evidence_id: plaque-native-intranuclear_quality_control_compartment-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/intranuclear_quality_control_compartment-uniprot-verify-receipt.json
  locator: Actual receipt and independently inspected /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/intranuclear_quality_control_compartment-uniprot-verify.log
  accessed_at: '2026-11-03T08:11:12.805505Z'
  summary: Root-executed native command exit0, independently read receipt/log and
    verified exact source head and stdout hash. All declared UniProt examples and
    causal xrefs verify; scientific residence remains primary-source dependent.
  support: supports
  snapshot_sha256: d851ec456a73c492544c73c3bf1d03acf64f813a2315d23a88c7c83fbad5231a
- evidence_id: plaque-native-intranuclear_quality_control_compartment-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/intranuclear_quality_control_compartment-uniprot-causal-receipt.json
  locator: Actual receipt and independently inspected /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/intranuclear_quality_control_compartment-uniprot-causal.log
  accessed_at: '2026-11-03T08:11:13.309734Z'
  summary: 'Root-executed native command exit0, independently read receipt/log and
    verified exact source head and stdout hash. No GENE_OR_PROTEIN graph nodes occur:
    interventions are STATE or experimental/environmental factors, not ungrounded
    protein entities; this empty applicable graph subset does not validate scientific
    edges.'
  support: supports
  snapshot_sha256: a4f2a269bc51089fff234ab53fc4bdff1625dc64af6e19b105da1e4ad0b494b3
- evidence_id: plaque-native-juxtanuclear_quality_control_compartment-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/juxtanuclear_quality_control_compartment-uniprot-verify-receipt.json
  locator: Actual receipt and independently inspected /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/juxtanuclear_quality_control_compartment-uniprot-verify.log
  accessed_at: '2026-11-03T08:11:14.340613Z'
  summary: Root-executed native command exit0, independently read receipt/log and
    verified exact source head and stdout hash. All declared UniProt examples and
    causal xrefs verify; scientific residence remains primary-source dependent.
  support: supports
  snapshot_sha256: 5582ba86bb087a176314ed1d5db250f142b0bf3aab191687a6877e51ea663878
- evidence_id: plaque-native-juxtanuclear_quality_control_compartment-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/juxtanuclear_quality_control_compartment-uniprot-causal-receipt.json
  locator: Actual receipt and independently inspected /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/juxtanuclear_quality_control_compartment-uniprot-causal.log
  accessed_at: '2026-11-03T08:11:14.783299Z'
  summary: 'Root-executed native command exit0, independently read receipt/log and
    verified exact source head and stdout hash. No GENE_OR_PROTEIN graph nodes occur:
    interventions are STATE or experimental/environmental factors, not ungrounded
    protein entities; this empty applicable graph subset does not validate scientific
    edges.'
  support: supports
  snapshot_sha256: 0d2ed0beba2faa5a53640e51b0ba5ef57b2c72499d33bf42cfda4f087a731126
- evidence_id: plaque-native-nucleolar_peripheral_inclusion_body-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/nucleolar_peripheral_inclusion_body-uniprot-verify-receipt.json
  locator: Actual receipt and independently inspected /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/nucleolar_peripheral_inclusion_body-uniprot-verify.log
  accessed_at: '2026-11-03T08:11:18.686735Z'
  summary: Root-executed native command exit0, independently read receipt/log and
    verified exact source head and stdout hash. All declared UniProt examples and
    causal xrefs verify; scientific residence remains primary-source dependent.
  support: supports
  snapshot_sha256: a2c810fde08b706140f4fb6bae7573762a3515c1c1165e0dc5dc56d1fcf48f7d
- evidence_id: plaque-native-nucleolar_peripheral_inclusion_body-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/nucleolar_peripheral_inclusion_body-uniprot-causal-receipt.json
  locator: Actual receipt and independently inspected /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/nucleolar_peripheral_inclusion_body-uniprot-causal.log
  accessed_at: '2026-11-03T08:11:19.141466Z'
  summary: 'Root-executed native command exit0, independently read receipt/log and
    verified exact source head and stdout hash. No GENE_OR_PROTEIN graph nodes occur:
    interventions are STATE or experimental/environmental factors, not ungrounded
    protein entities; this empty applicable graph subset does not validate scientific
    edges.'
  support: supports
  snapshot_sha256: aa3a836137a79acad7e0894b6e2a1ca758d3981ba0ce42ad00acaff585a1408b
- evidence_id: micro-age2015-primary
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4635334.1/PMC4635334.1.xml
  locator: Saarikangas and Barral 2015 DOI:10.7554/eLife.06197; JATS front, Results
    s2-1 through s2-7, Discussion s3, Methods s4-1 through s4-7; figure captions including
    Figure6 and supplement Figure1-2; permissions; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/PMC4635334.raw;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/PMC4635334.receipt.json
  accessed_at: '2026-11-03T08:11:48.574939Z'
  snapshot_sha256: e8931b516ea7c92b41da19c7df230bed7c0d1f390d5c4edd5a31bbacfda0ab0c
  summary: The primary body supports persistent mother-retained age deposits, Hsp42-dependent
    assembly, Hsp104-independent formation with enhanced deposits when Hsp104 is lost,
    opposite Hsp42/Hsp104 overexpression effects, individual SSA1/SSA2 deletion phenotypes,
    variable Hsp26 and prion-state-dependent Sup35 association. S288C/W303 imaging
    contexts and functional assays are not universal prevalence or complete native
    composition evidence. No raw microscopy or videos reanalyzed.
  support: supports
- evidence_id: micro-age2017-primary
  kind: primary_source
  reference: https://kclpure.kcl.ac.uk/ws/files/67186035/Saarikangas_et_al.pdf
  locator: Saarikangas et al. 2017 DOI:10.1016/j.cub.2017.01.069; accepted manuscript
    PDF physical pp4–19 (Summary through Methods), pp22–24 figure legends, pp37–39
    supplemental methods/strain table; Figure S5 physical pp35–36 rendered and directly
    viewed; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/saarikangas2017.raw;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/saarikangas2017.receipt.json
  accessed_at: '2026-11-03T08:11:49.268725Z'
  snapshot_sha256: 90b650a614125f55611274e38541f7be58110815750e9a698f6828d74427e3fc
  summary: Primary text supports ER association, observed intranuclear subset, PRM3-dependent
    fusion context, daughter-deposit changes after BUD1/SUR2/BUD6 or YDJ1-C406S perturbation,
    and the proposed precursor-confinement model. S5 pixels show N-terminal GFP-Ydj1
    enrichment in 9.4% of 53 scored cells, with one scored Hsp104 deposit per cell,
    and preserved 99.5% ER apposition in both wild type and C406S. This does not establish
    Ydj1 as a universal mature-deposit coat or identify its bound precursor clients.
    Other figure pixels and original movies were not inspected.
  support: supports
- evidence_id: micro-age2025-primary
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC11849620.1/PMC11849620.1.xml
  locator: DOI:10.1016/j.jbc.2025.108172; JATS front, Results sec1.1–sec1.3, Methods
    sec2.1/sec2.4 and Data sec3; Figure3–5 captions; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/PMC11849620.raw;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/PMC11849620.receipt.json
  accessed_at: '2026-11-03T08:11:48.575019Z'
  snapshot_sha256: e086c564436b4d9ad6f43a78ad8a5e4058e0e979c55b37a5a6bfb0791e8a96b6
  summary: BY4741 aging experiments support higher age-associated foci after NPR3
    deletion and lower after TCO89 deletion, and a young-versus-old response to translation
    inhibition. Figure5A versus Methods retain the 0.25 versus 250 micrograms/mL cycloheximide
    discrepancy; old isolated cells have median 12 divisions. Loss of visible Hsp104
    foci is not direct proteolytic clearance. Acute pro3-1 screening and aging experiments
    are distinguished. No image pixels or supplementary datasets were reanalyzed.
  support: supports
- evidence_id: micro-age2018-secondary-nomenclature
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC6064742.1/PMC6064742.1.xml
  locator: DOI:10.3389/fnmol.2018.00249; JATS front and Figure1 caption only; response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/PMC6064742.raw;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/PMC6064742.receipt.json
  accessed_at: '2026-11-03T08:11:48.575072Z'
  snapshot_sha256: d2d06af7ae94f495609e14e3cde3c072264d5a30bb84ddf83c06389e72040941
  summary: Secondary review Figure1 explicitly expands APOD as age-associated protein
    deposit. Used only for nomenclature/background, not as primary experimental support
    for formation, necessity or ER localization. No image pixels inspected.
  support: context_only
- evidence_id: micro-ipod2008-primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2746971/?pdf=render
  locator: Kaganovich et al. DOI:10.1038/nature07195; authentic PMC2746971 HTML title/abstract,
    main narrative and figure captions, Methods Summary; derived zero-based paragraphs
    P12–P66; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/extra/kaganovich2008-body.raw;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/extra/kaganovich2008-body.receipt.json
  accessed_at: '2026-11-03T08:12:36.950905Z'
  snapshot_sha256: b03d471c955e446a84390aa18e5281871adb8c1496ac09f3f4bd36219479720f
  summary: Primary source distinguishes poorly mobile perivacuolar IPOD from soluble
    JUNQ, associates Hsp104 and Atg8 while separating PAS/autophagy claims, and reports
    that Ubc9ts in IPOD did not regain diffuse fluorescence in its recovery assay.
    This assay does not prohibit slower turnover of another substrate under the later
    Kumar conditions. Mammalian comparison does not automatically extend this yeast
    record to every taxon. Supplementary files/full online Methods and image pixels
    were not inspected.
  support: supports
- evidence_id: micro-ipod2016-primary
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5045159.1/PMC5045159.1.xml
  locator: Kumar et al. DOI:10.1371/journal.pgen.1006324; JATS front, Results sec003–sec009,
    Discussion sec011–sec013, Methods sec016/sec024, Figure3 caption and permissions;
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/PMC5045159.raw;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/PMC5045159.receipt.json
  accessed_at: '2026-11-03T08:11:48.575113Z'
  snapshot_sha256: 6a9b94b36eb806af6ebccc45032211d825202eb7bc4d2bf823bb8d3b98bd6889
  summary: Primary body supports 74D-694-derived PrD-GFP recruitment requiring tested
    Myo2/tropomyosin/Sec18 functions, recovery after depletion ends, and preservation
    of preformed deposits. Shared vesicular delivery and tethering are proposed models,
    not direct establishment of each factor as a resident component. Slowly extracted
    PrD-GFP requires Hsp104 activity; MG132 reduces but does not eliminate turnover,
    and bulk autophagy is not established. Engineered Sup35 PrD cargo is not equated
    to a fixed full-length native subunit.
  support: supports
- evidence_id: micro-ipod2024-primary
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC10931478.1/PMC10931478.1.xml
  locator: Carter et al. DOI:10.1371/journal.pgen.1011194; JATS front, Results sec011
    and Methods sec015/sec016/sec018; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/PMC10931478.raw;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/PMC10931478.receipt.json
  accessed_at: '2026-11-03T08:11:48.575148Z'
  snapshot_sha256: 1494f76d7125ef44b80c836e7b10c683889909df96025862ae79d80e1fa8f746
  summary: 74D-694-derived cells treated with 0.8mM hydrogen peroxide for one hour
    show ABP1-dependent increased prion formation in wild type but not the same requirement
    in btn2 hsp42 mutants. The source supports a genotype/assay-specific counterexample
    to universal IPOD necessity, not universal absence of IPOD function. Prion frequency
    was phenotyped and confirmed through guanidine curing. No figure pixels or raw
    datasets inspected.
  support: supports
- evidence_id: micro-mitostore2023-primary
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC10068336.1/PMC10068336.1.xml
  locator: Kraemer et al. DOI:10.15252/embj.2022112309; JATS front, Results sec0003–sec0008,
    Discussion sec0009, Methods sec0011/sec0012/sec0016–sec0019, Figures5–6 captions
    and permissions; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/PMC10068336.raw;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/PMC10068336.receipt.json
  accessed_at: '2026-11-03T08:11:48.792787Z'
  snapshot_sha256: 87eb1d7c8582e4a27cf3946f75e350994be651438829164bda912c2307e46a14
  summary: Primary text supports cytosolic, mitochondrial-surface-associated precursor
    granules in lactate-grown and clogger-stressed yeast. Separate HSP42 and HSP104
    deletions block tested Aim17 granules; Hsp26 is co-purification evidence without
    equal necessity/localization evidence. Presequence deletion affects Mam33 recruitment.
    After 4.5h induction and 4h chase, split-GFP supports matrix import competence
    without tracking individual proteins continuously from a granule. RPN4 deletion
    and chaperone dependence concern the tested clogger survival context. Hsp104 IP
    analysis reports 1154 filtered proteins, distinct from the 3550 whole-cell proteome
    and archive metadata. No raw MS, supplementary strain workbook, extended-figure
    pixels or original videos reanalyzed.
  support: supports
- evidence_id: micro-mitostore-tom70-comparison
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC10401023.1/PMC10401023.1.xml
  locator: Liu et al. DOI:10.1073/pnas.2300475120; JATS front, Results s2, Discussion
    s7; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/PMC10401023.raw;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/PMC10401023.receipt.json
  accessed_at: '2026-11-03T08:11:49.208905Z'
  snapshot_sha256: 5fcea748c80a6d7c2ebdf5f52ad077883e6a6042d2334909f10cc41899c87c14
  summary: The primary study tests Tom70-associated heat-induced aggregate recruitment
    and discusses similarities to MitoStores. Similarities in precursor content, chaperones
    and mitochondrial association do not establish exact identity or transfer every
    Tom70 mechanism to the Kraemer granules. Only the indicated Results subsection
    and full Discussion were read; other result sections and image pixels were not
    inspected.
  support: context_only
- evidence_id: micro-pride-mitostore
  kind: database
  reference: https://www.ebi.ac.uk/pride/ws/archive/v2/projects/PXD035762
  locator: PRIDE PXD035762 exact project object; accession/title/description, organism,
    dataProcessingProtocol and references; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/PXD035762.raw;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/PXD035762.receipt.json
  accessed_at: '2026-11-03T08:11:49.390897Z'
  snapshot_sha256: 577bd8910d6c838acb3b99d4c99672776aa883675658250d69c2b902811879c5
  summary: Current title/description identify the MitoStore Hsp104 AP-MS dataset,
    but the references still point to the Ubc8 paper DOI:10.26508/LSA.202201526, and
    processing text says 2920 filtered proteins versus 1154 in the primary IP analysis.
    The record explicitly preserves these inconsistencies and uses archive provenance
    without inventing a full native inventory, sample count or corrected citation.
    Raw MS files were not downloaded.
  support: context_only
- evidence_id: micro-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0016234,GO:0140453,GO:0005737
  locator: QuickGO exact GO:0005737/GO:0016234/GO:0140453 objects, names/definitions/obsoletion
    flags; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/go.raw;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/go.receipt.json
  accessed_at: '2026-11-03T08:11:49.498910Z'
  snapshot_sha256: aa4d91db6165a9afa25797ecb4277afc3290ae3749049005d6ed5d348dec6023
  summary: Cytoplasm and inclusion body resolve as active component terms; protein
    aggregate center has a reversible thermosensitive-protein sequestration definition
    and is not an exact identity replacement for all three records. Age deposits preserve
    uncertain intranuclear location rather than asserting universal cytoplasmic parthood;
    IPOD and MitoStore cytosolic location agrees with primary studies.
  support: supports
- evidence_id: micro-go-query-APOD
  kind: search
  reference: https://www.ebi.ac.uk/ols4/api/search?ontology=go&exact=true&rows=100&q=APOD
  locator: OLS4 GO-scoped search response; exact=true; q=APOD; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/go-query-APOD.raw;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/go-query-APOD.receipt.json
  accessed_at: '2026-11-03T08:11:49.569574Z'
  snapshot_sha256: 8513d3bd5786ca40f0ccf003c56d6c743d8474999c8355634ef19d500c0bca22
  summary: Returned 1 documents; APOD hits an imported pulmonary interstitial fibroblast
    term through marker text, not an exact deposit cellular-component identity. This
    is not a universal ontology absence claim.
  support: context_only
  search_scope: OLS4 ontology=go, exact=true, q='APOD', rows=100, start=0, on 2026-11-03T08:11:49.569574+00:00;
    numFound=1, all returned documents inspected. Limited to these literal names,
    this endpoint and its imported terms; no all-ontology or synonym-universe claim.
- evidence_id: micro-go-query-Agepod
  kind: search
  reference: https://www.ebi.ac.uk/ols4/api/search?ontology=go&exact=true&rows=100&q=Agepod
  locator: OLS4 GO-scoped search response; exact=true; q=Agepod; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/go-query-Agepod.raw;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/go-query-Agepod.receipt.json
  accessed_at: '2026-11-03T08:11:49.569465Z'
  snapshot_sha256: 8d33fdeb26a2d16294a3c5f4a7f444578bb462aa6036d45a15e9bfadfe47fbd2
  summary: Returned 0 documents; no exact identity candidate in this bounded query
    response. This is not a universal ontology absence claim.
  support: context_only
  search_scope: OLS4 ontology=go, exact=true, q='Agepod', rows=100, start=0, on 2026-11-03T08:11:49.569465+00:00;
    numFound=0, all returned documents inspected. Limited to these literal names,
    this endpoint and its imported terms; no all-ontology or synonym-universe claim.
- evidence_id: micro-go-query-IPOD
  kind: search
  reference: https://www.ebi.ac.uk/ols4/api/search?ontology=go&exact=true&rows=100&q=IPOD
  locator: OLS4 GO-scoped search response; exact=true; q=IPOD; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/go-query-IPOD.raw;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/go-query-IPOD.receipt.json
  accessed_at: '2026-11-03T08:11:50.061463Z'
  snapshot_sha256: 818a2f6b5f20921f90b2d975f00a2604499ecaed5b47cb431bc2ecd0042041e6
  summary: Returned 0 documents; no exact identity candidate in this bounded query
    response. This is not a universal ontology absence claim.
  support: context_only
  search_scope: OLS4 ontology=go, exact=true, q='IPOD', rows=100, start=0, on 2026-11-03T08:11:50.061463+00:00;
    numFound=0, all returned documents inspected. Limited to these literal names,
    this endpoint and its imported terms; no all-ontology or synonym-universe claim.
- evidence_id: micro-go-query-MitoStore
  kind: search
  reference: https://www.ebi.ac.uk/ols4/api/search?ontology=go&exact=true&rows=100&q=MitoStore
  locator: OLS4 GO-scoped search response; exact=true; q=MitoStore; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/go-query-MitoStore.raw;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/go-query-MitoStore.receipt.json
  accessed_at: '2026-11-03T08:11:50.156102Z'
  snapshot_sha256: 8d33fdeb26a2d16294a3c5f4a7f444578bb462aa6036d45a15e9bfadfe47fbd2
  summary: Returned 0 documents; no exact identity candidate in this bounded query
    response. This is not a universal ontology absence claim.
  support: context_only
  search_scope: OLS4 ontology=go, exact=true, q='MitoStore', rows=100, start=0, on
    2026-11-03T08:11:50.156102+00:00; numFound=0, all returned documents inspected.
    Limited to these literal names, this endpoint and its imported terms; no all-ontology
    or synonym-universe claim.
- evidence_id: micro-go-query-MitoStores
  kind: search
  reference: https://www.ebi.ac.uk/ols4/api/search?ontology=go&exact=true&rows=100&q=MitoStores
  locator: OLS4 GO-scoped search response; exact=true; q=MitoStores; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/go-query-MitoStores.raw;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/go-query-MitoStores.receipt.json
  accessed_at: '2026-11-03T08:11:50.254846Z'
  snapshot_sha256: 8d33fdeb26a2d16294a3c5f4a7f444578bb462aa6036d45a15e9bfadfe47fbd2
  summary: Returned 0 documents; no exact identity candidate in this bounded query
    response. This is not a universal ontology absence claim.
  support: context_only
  search_scope: OLS4 ontology=go, exact=true, q='MitoStores', rows=100, start=0, on
    2026-11-03T08:11:50.254846+00:00; numFound=0, all returned documents inspected.
    Limited to these literal names, this endpoint and its imported terms; no all-ontology
    or synonym-universe claim.
- evidence_id: micro-go-query-age-associated_protein_deposit
  kind: search
  reference: https://www.ebi.ac.uk/ols4/api/search?ontology=go&exact=true&rows=100&q=age-associated+protein+deposit
  locator: OLS4 GO-scoped search response; exact=true; q=age-associated protein deposit;
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/go-query-age-associated_protein_deposit.raw;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/go-query-age-associated_protein_deposit.receipt.json
  accessed_at: '2026-11-03T08:11:49.670919Z'
  snapshot_sha256: 8d33fdeb26a2d16294a3c5f4a7f444578bb462aa6036d45a15e9bfadfe47fbd2
  summary: Returned 0 documents; no exact identity candidate in this bounded query
    response. This is not a universal ontology absence claim.
  support: context_only
  search_scope: OLS4 ontology=go, exact=true, q='age-associated protein deposit',
    rows=100, start=0, on 2026-11-03T08:11:49.670919+00:00; numFound=0, all returned
    documents inspected. Limited to these literal names, this endpoint and its imported
    terms; no all-ontology or synonym-universe claim.
- evidence_id: micro-go-query-insoluble_protein_deposit
  kind: search
  reference: https://www.ebi.ac.uk/ols4/api/search?ontology=go&exact=true&rows=100&q=insoluble+protein+deposit
  locator: OLS4 GO-scoped search response; exact=true; q=insoluble protein deposit;
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/go-query-insoluble_protein_deposit.raw;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/go-query-insoluble_protein_deposit.receipt.json
  accessed_at: '2026-11-03T08:11:50.105329Z'
  snapshot_sha256: 8d33fdeb26a2d16294a3c5f4a7f444578bb462aa6036d45a15e9bfadfe47fbd2
  summary: Returned 0 documents; no exact identity candidate in this bounded query
    response. This is not a universal ontology absence claim.
  support: context_only
  search_scope: OLS4 ontology=go, exact=true, q='insoluble protein deposit', rows=100,
    start=0, on 2026-11-03T08:11:50.105329+00:00; numFound=0, all returned documents
    inspected. Limited to these literal names, this endpoint and its imported terms;
    no all-ontology or synonym-universe claim.
- evidence_id: micro-tax-4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: ENA taxonomy exact taxId/scientificName/rank/lineage fields; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/tax-4932.raw;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/tax-4932.receipt.json
  accessed_at: '2026-11-03T08:11:50.273671Z'
  snapshot_sha256: 38f43dd1593a1d47416228ae385464f30aeb8302c3aadb45b3588d03744bc814
  summary: 4932 resolves to Saccharomyces cerevisiae, rank species. Authority identity
    is separate from primary-paper experimental strain evidence; 74D-694 and YPH499
    derivative genotypes are not silently replaced by S288C.
  support: supports
- evidence_id: micro-tax-559292
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: ENA taxonomy exact taxId/scientificName/rank/lineage fields; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/tax-559292.raw;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/tax-559292.receipt.json
  accessed_at: '2026-11-03T08:11:50.713976Z'
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
  summary: 559292 resolves to Saccharomyces cerevisiae S288C, rank strain. Authority
    identity is separate from primary-paper experimental strain evidence; 74D-694
    and YPH499 derivative genotypes are not silently replaced by S288C.
  support: supports
- evidence_id: micro-tax-1247190
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1247190
  locator: ENA taxonomy exact taxId/scientificName/rank/lineage fields; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/tax-1247190.raw;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/tax-1247190.receipt.json
  accessed_at: '2026-11-03T08:11:50.734040Z'
  snapshot_sha256: caee974f39d598c4001a51c78b0dc0c7dfba575de9526277d845019da6abe202
  summary: 1247190 resolves to Saccharomyces cerevisiae BY4741, rank strain. Authority
    identity is separate from primary-paper experimental strain evidence; 74D-694
    and YPH499 derivative genotypes are not silently replaced by S288C.
  support: supports
- evidence_id: micro-uniprot-Q12329
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q12329.json
  locator: UniProt exact accession entryType/primaryAccession/proteinDescription/genes/organism;
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/Q12329.raw;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/Q12329.receipt.json
  accessed_at: '2026-11-03T08:11:50.742425Z'
  snapshot_sha256: 2fd80fe65790b403d51e6d01659e4c94ec91a1455e5b4be00301e2350656a1cc
  summary: Reviewed S. cerevisiae S288C taxon559292 record maps Q12329 to HSP42; locus
    and displayed name checked. Identity does not establish localization, native stoichiometry
    or requirement for deposit formation.
  support: supports
- evidence_id: micro-query-HSP42
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A559292+AND+gene_exact%3AHSP42&format=json&size=500
  locator: Exact reviewed gene query; returned accession/primary gene/taxon; response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/query-HSP42.raw;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/query-HSP42.receipt.json
  accessed_at: '2026-11-03T08:11:50.890533Z'
  snapshot_sha256: f293170bb43d8482c94e6ef06e0447afe7d1dcb10ffa734d42c94920324e5ae4
  summary: The single returned reviewed S288C hit is Q12329 (HSP42); no unresolved
    symbol or alternative accession in this bounded response.
  support: supports
  search_scope: UniProtKB query reviewed:true AND organism_id:559292 AND gene_exact:HSP42;
    format=json,size=500, fetched 2026-11-03T08:11:50.890533+00:00; total_results=1,
    one result inspected, no next Link. Does not search every strain, unreviewed proteome
    or orthologue.
- evidence_id: micro-matches-Q12329
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q12329/?page_size=200
  locator: InterPro entries by exact UniProt accession, page_size200; metadata accession/name/type
    and next/count; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/matches-Q12329.raw;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/matches-Q12329.receipt.json
  accessed_at: '2026-11-03T08:11:50.843812Z'
  snapshot_sha256: b5fd5350c5ea8e5ac5d6bdda8ab01a8f4ab0036d09974a5a02fce9361203a6a2
  summary: All 3 returned assignments inspected; next=null. IPR002068 Alpha crystallin/Hsp20
    domain (domain); IPR008978 HSP20-like chaperone (homologous_superfamily); IPR031107
    Small heat shock protein (family). Family/domain/superfamily types and broad-family
    scope are kept separate; no necessity inference from sequence assignment.
  support: supports
- evidence_id: micro-uniprot-P15992
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P15992.json
  locator: UniProt exact accession entryType/primaryAccession/proteinDescription/genes/organism;
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/P15992.raw;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/P15992.receipt.json
  accessed_at: '2026-11-03T08:11:51.134865Z'
  snapshot_sha256: cbaa80ed16718c9eb01d31f4ae461fe665e1390d99bccaee7d6a277c4352b523
  summary: Reviewed S. cerevisiae S288C taxon559292 record maps P15992 to HSP26; locus
    and displayed name checked. Identity does not establish localization, native stoichiometry
    or requirement for deposit formation.
  support: supports
- evidence_id: micro-query-HSP26
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A559292+AND+gene_exact%3AHSP26&format=json&size=500
  locator: Exact reviewed gene query; returned accession/primary gene/taxon; response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/query-HSP26.raw;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/query-HSP26.receipt.json
  accessed_at: '2026-11-03T08:11:51.331250Z'
  snapshot_sha256: 62a0910bbcb49e0d05afd2960add90e935340ecc9909ff5d559a12353efc6d53
  summary: The single returned reviewed S288C hit is P15992 (HSP26); no unresolved
    symbol or alternative accession in this bounded response.
  support: supports
  search_scope: UniProtKB query reviewed:true AND organism_id:559292 AND gene_exact:HSP26;
    format=json,size=500, fetched 2026-11-03T08:11:51.331250+00:00; total_results=1,
    one result inspected, no next Link. Does not search every strain, unreviewed proteome
    or orthologue.
- evidence_id: micro-matches-P15992
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P15992/?page_size=200
  locator: InterPro entries by exact UniProt accession, page_size200; metadata accession/name/type
    and next/count; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/matches-P15992.raw;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/matches-P15992.receipt.json
  accessed_at: '2026-11-03T08:11:51.303148Z'
  snapshot_sha256: 2a832a0014d7563f99c26af41dd62810eda86625e204d5e0bed963bcec7b6d04
  summary: All 3 returned assignments inspected; next=null. IPR002068 Alpha crystallin/Hsp20
    domain (domain); IPR008978 HSP20-like chaperone (homologous_superfamily); IPR031107
    Small heat shock protein (family). Family/domain/superfamily types and broad-family
    scope are kept separate; no necessity inference from sequence assignment.
  support: supports
- evidence_id: micro-uniprot-P31539
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P31539.json
  locator: UniProt exact accession entryType/primaryAccession/proteinDescription/genes/organism;
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/P31539.raw;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/P31539.receipt.json
  accessed_at: '2026-11-03T08:11:51.470690Z'
  snapshot_sha256: 8636decea760cdb2a2da238bfa589822867a778a41fd6a04c45a74fe5802ee13
  summary: Reviewed S. cerevisiae S288C taxon559292 record maps P31539 to HSP104;
    locus and displayed name checked. Identity does not establish localization, native
    stoichiometry or requirement for deposit formation.
  support: supports
- evidence_id: micro-query-HSP104
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A559292+AND+gene_exact%3AHSP104&format=json&size=500
  locator: Exact reviewed gene query; returned accession/primary gene/taxon; response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/query-HSP104.raw;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/query-HSP104.receipt.json
  accessed_at: '2026-11-03T08:11:51.774698Z'
  snapshot_sha256: 4e2938a5a1292a9626b18e30b225ebfc7a30d63069235f01cd0bc3d007279322
  summary: The single returned reviewed S288C hit is P31539 (HSP104); no unresolved
    symbol or alternative accession in this bounded response.
  support: supports
  search_scope: UniProtKB query reviewed:true AND organism_id:559292 AND gene_exact:HSP104;
    format=json,size=500, fetched 2026-11-03T08:11:51.774698+00:00; total_results=1,
    one result inspected, no next Link. Does not search every strain, unreviewed proteome
    or orthologue.
- evidence_id: micro-matches-P31539
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P31539/?page_size=200
  locator: InterPro entries by exact UniProt accession, page_size200; metadata accession/name/type
    and next/count; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/matches-P31539.raw;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/matches-P31539.receipt.json
  accessed_at: '2026-11-03T08:11:51.734171Z'
  snapshot_sha256: 750867aa538d4dd5c6c6a982138e7401b8b788d9653ecb84bf5d145c8ff6d3ee
  summary: All 11 returned assignments inspected; next=null. IPR001270 ClpA/B family
    (family); IPR003593 AAA+ ATPase domain (domain); IPR003959 ATPase, AAA-type, core
    (domain); IPR004176 Clp, repeat (R) N-terminal domain (domain); IPR018368 ClpA/B,
    conserved site 1 (conserved_site); IPR019489 Clp ATPase, C-terminal (domain);
    IPR027417 P-loop containing nucleoside triphosphate hydrolase (homologous_superfamily);
    IPR028299 ClpA/B, conserved site 2 (conserved_site); IPR036628 Clp, N-terminal
    domain superfamily (homologous_superfamily); IPR041546 ClpA/ClpB, AAA lid domain
    (domain); IPR050130 ATP-dependent Clp protease/Chaperone ClpA/ClpB (family). Family/domain/superfamily
    types and broad-family scope are kept separate; no necessity inference from sequence
    assignment.
  support: supports
- evidence_id: micro-uniprot-P10591
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P10591.json
  locator: UniProt exact accession entryType/primaryAccession/proteinDescription/genes/organism;
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/P10591.raw;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/P10591.receipt.json
  accessed_at: '2026-11-03T08:11:51.847290Z'
  snapshot_sha256: 7459cff48ea4a5bb0deb45f6da0f61e77cf00ee2168622b6ea7af8949890b64e
  summary: Reviewed S. cerevisiae S288C taxon559292 record maps P10591 to SSA1; locus
    and displayed name checked. Identity does not establish localization, native stoichiometry
    or requirement for deposit formation.
  support: supports
- evidence_id: micro-query-SSA1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A559292+AND+gene_exact%3ASSA1&format=json&size=500
  locator: Exact reviewed gene query; returned accession/primary gene/taxon; response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/query-SSA1.raw;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/query-SSA1.receipt.json
  accessed_at: '2026-11-03T08:11:52.184043Z'
  snapshot_sha256: 6c0c0c6e6c88952d7e30972e20fd8e249b1f263dcff4495d0c3c5eb9863b1895
  summary: The single returned reviewed S288C hit is P10591 (SSA1); no unresolved
    symbol or alternative accession in this bounded response.
  support: supports
  search_scope: UniProtKB query reviewed:true AND organism_id:559292 AND gene_exact:SSA1;
    format=json,size=500, fetched 2026-11-03T08:11:52.184043+00:00; total_results=1,
    one result inspected, no next Link. Does not search every strain, unreviewed proteome
    or orthologue.
- evidence_id: micro-matches-P10591
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P10591/?page_size=200
  locator: InterPro entries by exact UniProt accession, page_size200; metadata accession/name/type
    and next/count; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/matches-P10591.raw;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/matches-P10591.receipt.json
  accessed_at: '2026-11-03T08:11:52.129559Z'
  snapshot_sha256: 19cd7491705e3561a05df7016c70c1091734040f5815bfc16f04ecdfcd59b082
  summary: All 5 returned assignments inspected; next=null. IPR013126 Heat shock protein
    70 family (family); IPR018181 Heat shock protein 70, conserved site (conserved_site);
    IPR029047 Heat shock protein 70kD, peptide-binding domain superfamily (homologous_superfamily);
    IPR029048 Heat shock protein 70kD, C-terminal domain superfamily (homologous_superfamily);
    IPR043129 ATPase, nucleotide binding domain (homologous_superfamily). Family/domain/superfamily
    types and broad-family scope are kept separate; no necessity inference from sequence
    assignment.
  support: supports
- evidence_id: micro-uniprot-P10592
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P10592.json
  locator: UniProt exact accession entryType/primaryAccession/proteinDescription/genes/organism;
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/P10592.raw;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/P10592.receipt.json
  accessed_at: '2026-11-03T08:11:52.955939Z'
  snapshot_sha256: 45fb36c0787ae44ba78e30b21c47ae26f4ab816e781a732073171c4a70e269f6
  summary: Reviewed S. cerevisiae S288C taxon559292 record maps P10592 to SSA2; locus
    and displayed name checked. Identity does not establish localization, native stoichiometry
    or requirement for deposit formation.
  support: supports
- evidence_id: micro-query-SSA2
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A559292+AND+gene_exact%3ASSA2&format=json&size=500
  locator: Exact reviewed gene query; returned accession/primary gene/taxon; response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/query-SSA2.raw;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/query-SSA2.receipt.json
  accessed_at: '2026-11-03T08:11:53.304582Z'
  snapshot_sha256: 3a1e1ece7729e45c9d229f8c8461448c998df0bfe823d153b6b5942a39a66c61
  summary: The single returned reviewed S288C hit is P10592 (SSA2); no unresolved
    symbol or alternative accession in this bounded response.
  support: supports
  search_scope: UniProtKB query reviewed:true AND organism_id:559292 AND gene_exact:SSA2;
    format=json,size=500, fetched 2026-11-03T08:11:53.304582+00:00; total_results=1,
    one result inspected, no next Link. Does not search every strain, unreviewed proteome
    or orthologue.
- evidence_id: micro-matches-P10592
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P10592/?page_size=200
  locator: InterPro entries by exact UniProt accession, page_size200; metadata accession/name/type
    and next/count; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/matches-P10592.raw;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/matches-P10592.receipt.json
  accessed_at: '2026-11-03T08:11:52.963149Z'
  snapshot_sha256: b78ecf727cc28004c68ea1a1b954adad836011894a71c3e845f14a11d2565952
  summary: All 5 returned assignments inspected; next=null. IPR013126 Heat shock protein
    70 family (family); IPR018181 Heat shock protein 70, conserved site (conserved_site);
    IPR029047 Heat shock protein 70kD, peptide-binding domain superfamily (homologous_superfamily);
    IPR029048 Heat shock protein 70kD, C-terminal domain superfamily (homologous_superfamily);
    IPR043129 ATPase, nucleotide binding domain (homologous_superfamily). Family/domain/superfamily
    types and broad-family scope are kept separate; no necessity inference from sequence
    assignment.
  support: supports
- evidence_id: micro-uniprot-P25491
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P25491.json
  locator: UniProt exact accession entryType/primaryAccession/proteinDescription/genes/organism;
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/P25491.raw;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/P25491.receipt.json
  accessed_at: '2026-11-03T08:11:53.356133Z'
  snapshot_sha256: 9d11d2a3ddb00c55584a3469c546628b4c7a1e5986e9d3dbd8ecba60f5af8d3b
  summary: Reviewed S. cerevisiae S288C taxon559292 record maps P25491 to YDJ1; locus
    and displayed name checked. Identity does not establish localization, native stoichiometry
    or requirement for deposit formation.
  support: supports
- evidence_id: micro-query-YDJ1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A559292+AND+gene_exact%3AYDJ1&format=json&size=500
  locator: Exact reviewed gene query; returned accession/primary gene/taxon; response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/query-YDJ1.raw;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/query-YDJ1.receipt.json
  accessed_at: '2026-11-03T08:11:54.046653Z'
  snapshot_sha256: 364cbcffc5bff6e21910383454aa4642674dd32fef8c3c1295a63c042751b673
  summary: The single returned reviewed S288C hit is P25491 (YDJ1); no unresolved
    symbol or alternative accession in this bounded response.
  support: supports
  search_scope: UniProtKB query reviewed:true AND organism_id:559292 AND gene_exact:YDJ1;
    format=json,size=500, fetched 2026-11-03T08:11:54.046653+00:00; total_results=1,
    one result inspected, no next Link. Does not search every strain, unreviewed proteome
    or orthologue.
- evidence_id: micro-matches-P25491
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P25491/?page_size=200
  locator: InterPro entries by exact UniProt accession, page_size200; metadata accession/name/type
    and next/count; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/matches-P25491.raw;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/matches-P25491.receipt.json
  accessed_at: '2026-11-03T08:11:53.982533Z'
  snapshot_sha256: 7dafb7f8631f188fc8cf64685b0db62424c61885dddefdd8ff979e543782b431
  summary: All 9 returned assignments inspected; next=null. IPR001305 Heat shock protein
    DnaJ, cysteine-rich domain (domain); IPR001623 DnaJ domain (domain); IPR002939
    Chaperone DnaJ, C-terminal (domain); IPR008971 HSP40/DnaJ peptide-binding (homologous_superfamily);
    IPR012724 Chaperone DnaJ (family); IPR018253 DnaJ domain, conserved site (conserved_site);
    IPR036410 Heat shock protein DnaJ, cysteine-rich domain superfamily (homologous_superfamily);
    IPR036869 Chaperone J-domain superfamily (homologous_superfamily); IPR044713 DnaJ
    homolog subfamily A member 1/2-like (family). Family/domain/superfamily types
    and broad-family scope are kept separate; no necessity inference from sequence
    assignment.
  support: supports
- evidence_id: micro-uniprot-P05453
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P05453.json
  locator: UniProt exact accession entryType/primaryAccession/proteinDescription/genes/organism;
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/P05453.raw;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/P05453.receipt.json
  accessed_at: '2026-11-03T08:11:54.150385Z'
  snapshot_sha256: 220c5b10197e36ddf025b193e782fac495ad6d399f1b624d769c5b62a36af85a
  summary: Reviewed S. cerevisiae S288C taxon559292 record maps P05453 to SUP35; locus
    and displayed name checked. Identity does not establish localization, native stoichiometry
    or requirement for deposit formation.
  support: supports
- evidence_id: micro-query-SUP35
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A559292+AND+gene_exact%3ASUP35&format=json&size=500
  locator: Exact reviewed gene query; returned accession/primary gene/taxon; response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/query-SUP35.raw;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/query-SUP35.receipt.json
  accessed_at: '2026-11-03T08:11:54.991298Z'
  snapshot_sha256: 03fd25e9d1aa0c34901619dea7518a28218b8ab36c693cf9cc06cda61e1d8785
  summary: The single returned reviewed S288C hit is P05453 (SUP35); no unresolved
    symbol or alternative accession in this bounded response.
  support: supports
  search_scope: UniProtKB query reviewed:true AND organism_id:559292 AND gene_exact:SUP35;
    format=json,size=500, fetched 2026-11-03T08:11:54.991298+00:00; total_results=1,
    one result inspected, no next Link. Does not search every strain, unreviewed proteome
    or orthologue.
- evidence_id: micro-matches-P05453
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P05453/?page_size=200
  locator: InterPro entries by exact UniProt accession, page_size200; metadata accession/name/type
    and next/count; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/matches-P05453.raw;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/matches-P05453.receipt.json
  accessed_at: '2026-11-03T08:11:54.932240Z'
  snapshot_sha256: 15dbf9ca4f9076cdf87ce83dcbfb2081a2d2120e028bfe885c6591223ac294a3
  summary: All 9 returned assignments inspected; next=null. IPR000795 Translational
    (tr)-type GTP-binding domain (domain); IPR003285 Eukaryotic peptide chain release
    factor GTP-binding subunit (family); IPR004161 Translation elongation factor EFTu-like,
    domain 2 (domain); IPR009000 Translation protein, beta-barrel domain superfamily
    (homologous_superfamily); IPR009001 Translation elongation factor EF1A/initiation
    factor IF2gamma, C-terminal (homologous_superfamily); IPR027417 P-loop containing
    nucleoside triphosphate hydrolase (homologous_superfamily); IPR031157 Tr-type
    G domain, conserved site (conserved_site); IPR050100 Translation factor GTPase
    superfamily members (family); IPR054696 GTP-eEF1A, C-terminal domain (domain).
    Family/domain/superfamily types and broad-family scope are kept separate; no necessity
    inference from sequence assignment.
  support: supports
- evidence_id: micro-family-IPR031107
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR031107/
  locator: InterPro exact entry metadata name/type/hierarchy; functional descriptions
    used only as classification context; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/IPR031107.raw;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/IPR031107.receipt.json
  accessed_at: '2026-11-03T08:11:55.718946Z'
  snapshot_sha256: 7db6f5da4dd897dfbcaa6435cbeb744a4691f43cb10433977995a30bb1d91293
  summary: 'IPR031107 is a family: Small heat shock protein. The small-HSP, Hsp70
    and Sup35/eRF3 labels match the declared families. ClpA/B entries are broader
    than a yeast Hsp104-specific class and remain unassigned as exact component family
    groundings. No sequence-family entry establishes deposit residence or necessity.
    IPR050130 unreviewed machine-generated functional prose is not used for scientific
    support.'
  support: supports
- evidence_id: micro-family-IPR013126
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013126/
  locator: InterPro exact entry metadata name/type/hierarchy; functional descriptions
    used only as classification context; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/IPR013126.raw;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/IPR013126.receipt.json
  accessed_at: '2026-11-03T08:11:55.882711Z'
  snapshot_sha256: 43e5cb816d24b41f9660bca2ce79602ba65d8013352745427fc0fb1f4a3a6d9c
  summary: 'IPR013126 is a family: Heat shock protein 70 family. The small-HSP, Hsp70
    and Sup35/eRF3 labels match the declared families. ClpA/B entries are broader
    than a yeast Hsp104-specific class and remain unassigned as exact component family
    groundings. No sequence-family entry establishes deposit residence or necessity.
    IPR050130 unreviewed machine-generated functional prose is not used for scientific
    support.'
  support: supports
- evidence_id: micro-family-IPR003285
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR003285/
  locator: InterPro exact entry metadata name/type/hierarchy; functional descriptions
    used only as classification context; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/IPR003285.raw;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/IPR003285.receipt.json
  accessed_at: '2026-11-03T08:11:55.945015Z'
  snapshot_sha256: 0b72fb273b4c505328a072ea7a047466f31f35fbb0507a93530de22f27c0cc3e
  summary: 'IPR003285 is a family: Eukaryotic peptide chain release factor GTP-binding
    subunit. The small-HSP, Hsp70 and Sup35/eRF3 labels match the declared families.
    ClpA/B entries are broader than a yeast Hsp104-specific class and remain unassigned
    as exact component family groundings. No sequence-family entry establishes deposit
    residence or necessity. IPR050130 unreviewed machine-generated functional prose
    is not used for scientific support.'
  support: supports
- evidence_id: micro-family-IPR001270
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001270/
  locator: InterPro exact entry metadata name/type/hierarchy; functional descriptions
    used only as classification context; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/IPR001270.raw;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/IPR001270.receipt.json
  accessed_at: '2026-11-03T08:11:56.472222Z'
  snapshot_sha256: ed0a09c17fa611e58cd0d00b904d4dce2757228cd7e411301eddcfb9b391e0dd
  summary: 'IPR001270 is a family: ClpA/B family. The small-HSP, Hsp70 and Sup35/eRF3
    labels match the declared families. ClpA/B entries are broader than a yeast Hsp104-specific
    class and remain unassigned as exact component family groundings. No sequence-family
    entry establishes deposit residence or necessity. IPR050130 unreviewed machine-generated
    functional prose is not used for scientific support.'
  support: supports
- evidence_id: micro-family-IPR050130
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050130/
  locator: InterPro exact entry metadata name/type/hierarchy; functional descriptions
    used only as classification context; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/extra/IPR050130.raw;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/extra/IPR050130.receipt.json
  accessed_at: '2026-11-03T08:12:36.951225Z'
  snapshot_sha256: e654bc8d2d359d203a225be0690247071616a63341156fcd507f197717f78701
  summary: 'IPR050130 is a family: ATP-dependent Clp protease/Chaperone ClpA/ClpB.
    The small-HSP, Hsp70 and Sup35/eRF3 labels match the declared families. ClpA/B
    entries are broader than a yeast Hsp104-specific class and remain unassigned as
    exact component family groundings. No sequence-family entry establishes deposit
    residence or necessity. IPR050130 unreviewed machine-generated functional prose
    is not used for scientific support.'
  support: supports
- evidence_id: micro-adapter-catalogue
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: iModulonDB /api/datasets complete returned catalogue object array; response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/datasets.raw;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/datasets.receipt.json
  accessed_at: '2026-11-03T08:11:48.574632Z'
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  summary: 'Fresh catalogue contains20 organism entries and28 named datasets; none
    matches Saccharomyces cerevisiae or its S288C/BY4741 strains. These records name
    yeast chaperones, cargo and stress responses, so applicability must be examined.
    In the inspected catalogue no matched organism/dataset exists: downstream gene/module/activity
    checks are not applicable for this cohort. This is not negative biological evidence,
    and recombinant expression hosts in source methods do not change the curated target
    taxon.'
  support: context_only
- evidence_id: micro-historical-adapter-runner
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical shared runner attempt, not a PR2356 execution
  accessed_at: '2026-11-03T00:49:00.863225Z'
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  summary: Retained command ['/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources',
    'imodulondb', 'datasets'] ran 2026-11-03T00:49:00.848907+00:00 to 2026-11-03T00:49:00.863225+00:00,
    exit1, unavailable due to PermissionError reading pyvenv.cfg. Current review uses
    fresh inspected source catalogue fallback; no current runner success or fresh
    invocation is claimed.
  support: context_only
- evidence_id: micro-review-policy
  kind: authority
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/repo/.claude/skills/review-yaml-record/SKILL.md
  locator: Structured Source Cross-Checks and immutable review workflow
  accessed_at: '2026-11-03T08:20:13.522247Z'
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
  summary: Named protein/stress-response records require actual shared-source applicability;
    lack of an expression claim is not an exemption. Current catalogue-based no-covered-dataset
    result permits a bounded N/A conclusion. Original reviews remain immutable and
    current evidence is saved in a successor observation.
  support: supports
- evidence_id: micro-review-config
  kind: authority
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/repo/conf/record_review.yaml
  locator: Exact frozen repository skills/rubrics routing
  accessed_at: '2026-11-03T08:20:13.522247Z'
  snapshot_sha256: d3334a12b8a616a7638f1195748085d2b543fba7df67ad4ff8fcc0ac18f2d3ee
  summary: Repository-native skill, literature and curation checklist routing is retained.
    Byte identity with the previously inspected configuration was verified before
    current assessment; no new configuration semantics inferred.
  support: supports
- evidence_id: micro-original-validation-inputs
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/original-validation-inputs.json
  locator: All3 original frozen hashes against their declared source revision, current
    hashes and native validate/render receipts
  accessed_at: '2026-11-03T08:20:13.522247Z'
  snapshot_sha256: 20a02edacad25fe87a254fa304e72749e7b75ef6b684b13957eaa2866084d4fe
  summary: All3 original native validations and render comparisons passed. Age target
    bytes unchanged; IPOD and MitoStore changed only two self-node groundings plus
    curation history. A current assessment is required for stale inputs even when
    scientific claims are unchanged. Original finding lists are empty; no scientific
    issue lineage is fabricated.
  support: supports
- evidence_id: micro-record-age_associated_protein_deposit
  kind: record_content
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/repo/data/structures/inclusion/age_associated_protein_deposit.yaml
  locator: Entire current YAML, definitions/components/graphs/evidence/discussions/provenance
  accessed_at: '2026-11-03T08:20:13.522247Z'
  snapshot_sha256: f782fddfb8eb004a13ce40857c05527e29272b04da88e010cec04250ca867c30
  summary: Current frozen record inspected in full; its identity, source scope, experimental
    qualifications and evidence tiers were independently reassessed. Unchanged since
    the original observation.
  support: supports
- evidence_id: micro-prior-age_associated_protein_deposit
  kind: prior_review
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/repo/reviews/structured/20261021T103319Z-age-associated-protein-deposit-audit/review.yaml
  locator: Entire original YAML observation, checks/assessments/evidence/verdict/findings;
    paired rendered Markdown validated
  accessed_at: '2026-11-03T08:20:13.522247Z'
  snapshot_sha256: d4a67e5e0c296086e97b1fe9dc72184c64de0c26763901d914175ba8b01cd7c1
  summary: Original pass_with_limitations observation has no scientific findings.
    Its target hash remains current. Scientific support is freshly rechecked here;
    old source access times are not presented as new reads.
  support: supports
- evidence_id: micro-native-age_associated_protein_deposit-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/age_associated_protein_deposit-uniprot-verify-receipt.json
  locator: .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/age_associated_protein_deposit.yaml
    --verify; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/age_associated_protein_deposit-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T08:11:04.222793Z'
  snapshot_sha256: 5f5e58af118eec45e4a4faec6582607405e99122fa9c1eb884eb342f95da9666
  summary: Current-source command passed, started2026-11-03T08:11:02.535921+00:00,
    finished2026-11-03T08:11:04.222793+00:00, exit0. Seven concrete protein examples
    verified; all graph perturbations are outside the GENE_OR_PROTEIN inventory and
    causal scan has zero such nodes. These mechanical checks do not verify biological
    necessity, all graph intervention factors or a complete cargo inventory.
  support: supports
- evidence_id: micro-native-age_associated_protein_deposit-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/age_associated_protein_deposit-uniprot-causal-receipt.json
  locator: .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/age_associated_protein_deposit.yaml
    --causal-graphs; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/age_associated_protein_deposit-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-03T08:11:04.682617Z'
  snapshot_sha256: 5ad7fe149a25968de5a97eb349c92ce905ecd66fd702356538ef2efe531a4c8e
  summary: Current-source command passed, started2026-11-03T08:11:04.255089+00:00,
    finished2026-11-03T08:11:04.682617+00:00, exit0. Seven concrete protein examples
    verified; all graph perturbations are outside the GENE_OR_PROTEIN inventory and
    causal scan has zero such nodes. These mechanical checks do not verify biological
    necessity, all graph intervention factors or a complete cargo inventory.
  support: supports
- evidence_id: micro-image-age_associated_protein_deposit
  kind: record_content
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/repo/data/images/inclusion/age_associated_protein_deposit/pmc4635334_fig6.jpg
  locator: Original-resolution tracked JPEG directly viewed; complete stated figure
    panels; local SHA matches frozen input
  accessed_at: '2026-11-03T08:20:13.522247Z'
  snapshot_sha256: abf686034f035ecdf81b1c3fb79c1504412f436b4c695c07bbcfc31525f8d74a
  summary: 'Direct pixels agree with the record caption: Figure6A–G distinguishes
    separate SSA1/SSA2 mutants, Hsp42 assembly and Hsp104 overexpression, scale5micrometers.
    Caption and primary permission statement checked separately; no raw image reanalysis
    claimed.'
  support: supports
- evidence_id: micro-image-package-age_associated_protein_deposit
  kind: database
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4635334.1/PMC4635334.1.json
  locator: Fresh PMC open-access media package metadata, retraction flag and exact
    figure JPEG entry; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/package-PMC4635334.raw;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/package-PMC4635334.receipt.json
  accessed_at: '2026-11-03T08:11:49.223288Z'
  snapshot_sha256: 2695c5f49fcc273cb752a0d79a02077911c85ae309b77372948ad7db2643b267
  summary: 'The package is not marked retracted and its figure media MD5 matches the
    frozen tracked JPEG: a26e590300e4ac72bb1981eb94f99db9. The primary JATS permissions
    state CC BY4.0; package metadata alone is not a substitute for pixel inspection.'
  support: supports
- evidence_id: micro-record-insoluble_protein_deposit
  kind: record_content
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/repo/data/structures/inclusion/insoluble_protein_deposit.yaml
  locator: Entire current YAML, definitions/components/graphs/evidence/discussions/provenance
  accessed_at: '2026-11-03T08:20:13.522247Z'
  snapshot_sha256: 8bf3ffb3c2ce2ee5448d00f88d4d0de7911e3ee135e409e174a40f5c890e5f8a
  summary: Current frozen record inspected in full; its identity, source scope, experimental
    qualifications and evidence tiers were independently reassessed. The added STRUCTURE
    self-node groundings resolve to this exact record identity; scientific mechanisms
    are otherwise unchanged.
  support: supports
- evidence_id: micro-prior-insoluble_protein_deposit
  kind: prior_review
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/repo/reviews/structured/20261021T103322Z-insoluble-protein-deposit-audit/review.yaml
  locator: Entire original YAML observation, checks/assessments/evidence/verdict/findings;
    paired rendered Markdown validated
  accessed_at: '2026-11-03T08:20:13.522247Z'
  snapshot_sha256: 4c7447f824e0a5208a7205fd03416488eafb4d4168ee74deccdcfcb14dd99f4b
  summary: Original pass_with_limitations observation has no scientific findings.
    Its frozen target hash is historical and differs from current; do not silently
    rewrite it. Scientific support is freshly rechecked here; old source access times
    are not presented as new reads.
  support: supports
- evidence_id: micro-native-insoluble_protein_deposit-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/insoluble_protein_deposit-uniprot-verify-receipt.json
  locator: .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/insoluble_protein_deposit.yaml
    --verify; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/insoluble_protein_deposit-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T08:11:10.947097Z'
  snapshot_sha256: db5dfb5414c7b8269cd82a63ac62c6a8654c28ca7411a93df14db27907f65a6d
  summary: Current-source command passed, started2026-11-03T08:11:09.262171+00:00,
    finished2026-11-03T08:11:10.947097+00:00, exit0. One concrete Hsp104 example verified;
    graph scan has one COVERED Hsp104 node and one NO_GENE_SYMBOLS heterogeneous PrD
    cargo node, not a dangling or ungrounded named protein. These mechanical checks
    do not verify biological necessity, all graph intervention factors or a complete
    cargo inventory.
  support: supports
- evidence_id: micro-native-insoluble_protein_deposit-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/insoluble_protein_deposit-uniprot-causal-receipt.json
  locator: .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/insoluble_protein_deposit.yaml
    --causal-graphs; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/insoluble_protein_deposit-uniprot-causal.log
    SHA256 8e60d37b122caf9871b8b643517f9c62e3c33ff73a4f68b3cf8cf5b227bed12e
  accessed_at: '2026-11-03T08:11:11.369667Z'
  snapshot_sha256: 145e592c790efa9ffc571247bd78c1ddaa35baa3b3fa9c6a3020cf2b64204e17
  summary: Current-source command passed, started2026-11-03T08:11:10.980602+00:00,
    finished2026-11-03T08:11:11.369667+00:00, exit0. One concrete Hsp104 example verified;
    graph scan has one COVERED Hsp104 node and one NO_GENE_SYMBOLS heterogeneous PrD
    cargo node, not a dangling or ungrounded named protein. These mechanical checks
    do not verify biological necessity, all graph intervention factors or a complete
    cargo inventory.
  support: supports
- evidence_id: micro-image-insoluble_protein_deposit
  kind: record_content
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/repo/data/images/inclusion/insoluble_protein_deposit/pmc5045159_pgen_1006324_g003_e27e1f28.jpg
  locator: Original-resolution tracked JPEG directly viewed; complete stated figure
    panels; local SHA matches frozen input
  accessed_at: '2026-11-03T08:20:13.522247Z'
  snapshot_sha256: 89dfdd173c797ff168e0cb7be8cc0547b6b742b26324a3cec906f0d379463bd4
  summary: 'Direct pixels agree with the record caption: Figure3A–F depicts auxin-depletion
    recovery and preformed-IPOD stability, scale2micrometers. Caption and primary
    permission statement checked separately; no raw image reanalysis claimed.'
  support: supports
- evidence_id: micro-image-package-insoluble_protein_deposit
  kind: database
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5045159.1/PMC5045159.1.json
  locator: Fresh PMC open-access media package metadata, retraction flag and exact
    figure JPEG entry; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/package-PMC5045159.raw;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/package-PMC5045159.receipt.json
  accessed_at: '2026-11-03T08:11:49.226197Z'
  snapshot_sha256: b5b904304800a1f28a1e40619552adc92359cb1a55ee21803ba2866cc978e6d0
  summary: 'The package is not marked retracted and its figure media MD5 matches the
    frozen tracked JPEG: 9fb3e11d765cf9a68d081cff9402a568. The primary JATS permissions
    state CC BY4.0; package metadata alone is not a substitute for pixel inspection.'
  support: supports
- evidence_id: micro-record-mitostore
  kind: record_content
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/repo/data/structures/inclusion/mitostore.yaml
  locator: Entire current YAML, definitions/components/graphs/evidence/discussions/provenance
  accessed_at: '2026-11-03T08:20:13.522247Z'
  snapshot_sha256: c932945c5ae1c4501b217b75333c4ae85551096cd4630bdae07f3ef84b0a7dd4
  summary: Current frozen record inspected in full; its identity, source scope, experimental
    qualifications and evidence tiers were independently reassessed. The added STRUCTURE
    self-node groundings resolve to this exact record identity; scientific mechanisms
    are otherwise unchanged.
  support: supports
- evidence_id: micro-prior-mitostore
  kind: prior_review
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/repo/reviews/structured/20261021T103324Z-mitostore-audit/review.yaml
  locator: Entire original YAML observation, checks/assessments/evidence/verdict/findings;
    paired rendered Markdown validated
  accessed_at: '2026-11-03T08:20:13.522247Z'
  snapshot_sha256: 92d5e6446f9ebe9066657bd78283891c3ff08545275e2d4396a5c7f083e24329
  summary: Original pass_with_limitations observation has no scientific findings.
    Its frozen target hash is historical and differs from current; do not silently
    rewrite it. Scientific support is freshly rechecked here; old source access times
    are not presented as new reads.
  support: supports
- evidence_id: micro-native-mitostore-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/mitostore-uniprot-verify-receipt.json
  locator: .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/mitostore.yaml
    --verify; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/mitostore-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T08:11:15.999007Z'
  snapshot_sha256: 5dd396ba8faadc304a6b8ce472e7676d0b2178b704f22e1dc0c7dfd7ec422ab8
  summary: Current-source command passed, started2026-11-03T08:11:14.816178+00:00,
    finished2026-11-03T08:11:15.999007+00:00, exit0. Three concrete chaperone examples
    verified; graph scan has two NO_GENE_SYMBOLS heterogeneous precursor-cargo nodes
    and no dangling references. These mechanical checks do not verify biological necessity,
    all graph intervention factors or a complete cargo inventory.
  support: supports
- evidence_id: micro-native-mitostore-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/mitostore-uniprot-causal-receipt.json
  locator: .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/mitostore.yaml
    --causal-graphs; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/mitostore-uniprot-causal.log
    SHA256 448ddff38bf088be0c748c4d74ce9a0cfffd623e46490b160132b8904cc5aa64
  accessed_at: '2026-11-03T08:11:16.439258Z'
  snapshot_sha256: 0a7f0fad54058528c3551df3232cd12d297ac82e863bfe539bb6622c0091f8e8
  summary: Current-source command passed, started2026-11-03T08:11:16.033306+00:00,
    finished2026-11-03T08:11:16.439258+00:00, exit0. Three concrete chaperone examples
    verified; graph scan has two NO_GENE_SYMBOLS heterogeneous precursor-cargo nodes
    and no dangling references. These mechanical checks do not verify biological necessity,
    all graph intervention factors or a complete cargo inventory.
  support: supports
- evidence_id: micro-image-mitostore
  kind: record_content
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/repo/data/images/inclusion/mitostore/pmc10068336_embj2022112309_fig_0005.jpg
  locator: Original-resolution tracked JPEG directly viewed; complete stated figure
    panels; local SHA matches frozen input
  accessed_at: '2026-11-03T08:20:13.522247Z'
  snapshot_sha256: 08fe6da4832a3b949f031e367ee32323e88d73b83fece71cfd4ec02fd03e35d0
  summary: 'Direct pixels agree with the record caption: Figure5A–D depicts reporter/chaperone
    colocalization, separate deletion tests, presequence truncation and carbon-source
    context, with panel-specific2/10/5/10micrometer scales. Caption and primary permission
    statement checked separately; no raw image reanalysis claimed.'
  support: supports
- evidence_id: micro-image-package-mitostore
  kind: database
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC10068336.1/PMC10068336.1.json
  locator: Fresh PMC open-access media package metadata, retraction flag and exact
    figure JPEG entry; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/package-PMC10068336.raw;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-microtubule/package-PMC10068336.receipt.json
  accessed_at: '2026-11-03T08:11:49.239004Z'
  snapshot_sha256: f6ece7ab1fb2387ccb182314341d9aba437b0061c4cefdc8965285dfe90d2f7b
  summary: 'The package is not marked retracted and its figure media MD5 matches the
    frozen tracked JPEG: d5aed1d2f71065dd88d6dc617a55f368. The primary JATS permissions
    state CC BY4.0; package metadata alone is not a substitute for pixel inspection.'
  support: supports
- evidence_id: septin-aggresome-agent-PMC8528417
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC8528417.1/PMC8528417.1.xml
  locator: 'Fresh native JATS: article identity; three experimental Results subsections
    (formation, LLPS, fitness), Discussion and strain/construction Methods. No simulation/raw-data
    or image-pixel audit.'
  accessed_at: '2026-11-03T08:11:28.019135Z'
  support: supports
  summary: Jin 2021 observes differently timed HslU/Kbl/AcnB recruitment and liquid-like
    behavior in tested bacterial states. Fitness perturbations are broader context;
    constituent necessity and universal bacterial material state are not established.
  snapshot_sha256: 541eafcd7f01686c8c5a80e986beb4be9cab84bcece5383651d31d9108baf1c0
- evidence_id: septin-aggresome-agent-pei2025-aam
  kind: primary_source
  reference: https://eprints.whiterose.ac.uk/id/eprint/229675/1/Aggresomes_protect_mRNA_AAM-ms_and_si.pdf
  locator: Fresh accepted-manuscript PDF, cover/abstract pp1–2; selected Main/Results
    pages3,5–6,8,10,12,14–16 and complete charge-exclusion/recovery/Discussion pp17–25;
    specified strain, imaging, fractionation, RNA, recovery and persister Methods
    pp25–30. Fig5/ExtendedData5 pixels pp17–18 and Fig6 pixels p20 independently viewed.
    Other early figure captions inspected in part; no complete mathematical supplement
    audit.
  accessed_at: '2026-11-03T08:11:28.019212Z'
  support: supports
  summary: Pei 2025 distinguishes selected transcript storage, RNase charge-mutant
    entry and catalytic activity, and translation recovery controls. RNA as the repulsive
    agent remains proposed. Opposite persistence outcomes under RNA degradation versus
    chemical disruption do not support a universal fitness edge.
  snapshot_sha256: 8390cd9dbd5f3eb121cafedcb879ec5511cf6b88988c4ded24fd18e8e3c2d852
- evidence_id: septin-root19-sources-jats-PMC10185304
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC10185304.1/PMC10185304.1.xml
  locator: 'Fresh native JATS: article metadata; Introduction S1, Results S3–S7, Discussion
    S8, limitations S9, strain/preparation S15/S17 and key-resource strain rows. No
    image pixels, tomograms, supplementary models or detailed remaining computational
    Methods reanalysis.'
  accessed_at: '2026-11-03T08:11:32.486006Z'
  support: supports
  summary: Dutka 2023 supports polymerized GvpA ribs and exterior GvpC reinforcement
    in native Anabaena/Dolichospermum shells. Stripping, homology fitting and mechanical
    simulation remain distinct evidence types; CCAP1403/13F is specified in the resource
    table. Formation necessity of GvpC is not settled by stripping assembled vesicles.
  snapshot_sha256: 95f41410081f3b81af1368a9486ba755edc0ab5c85cffe4332f8ac271ddb4583
- evidence_id: septin-root19-sources-legacy-PMC3271001
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3271001/
  locator: 'Fresh genuine PMC HTML: article metadata, complete abstract/introduction,
    Figure1 caption and gas-vesicle preparation Methods; bounded solid-state NMR experimental
    context. No spectrum, figure-pixel or full structural-model reanalysis.'
  accessed_at: '2026-11-03T08:11:34.509836Z'
  support: supports
  summary: Bayro 2012 directly supports the recorded cross-beta wall interpretation.
    Native body now accessible, unlike the original abstract-only review; the sampled
    organism is Anabaena flos-aquae 1403/13f.
  snapshot_sha256: 883c42ddcadcfca29d8d2ce78400fece5b0e15f0329c6b23e78fd672ffeac81b
- evidence_id: septin-root19-sources-legacy-PMC372955
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC372955/
  locator: 'Fresh native PMC HTML: title/metadata and complete secondary-review abstract
    only. The full article is scanned; linked scans were not read in this review.'
  accessed_at: '2026-11-03T08:11:34.529498Z'
  support: supports
  summary: Walsby 1994 supports coarse gas-vesicle morphology, variable bacterial/archaeal
    occurrence and gas-permeable, water-excluding protein walls. No detailed full-body
    or conditional GvpC formation claim is certified.
  snapshot_sha256: 17c822212d754943ce9f188b01d932b2ad781c7b9dc88e9818e88b952ec6f775
- evidence_id: septin-root19-sources-jats-PMC5947121
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5947121.1/PMC5947121.1.xml
  locator: 'Fresh native secondary-review JATS: front metadata, opening sec0002 and
    direct text of biogenesis sec0003; nested protein-machinery sections excluded.'
  accessed_at: '2026-11-03T08:11:35.622039Z'
  support: supports
  summary: Graef 2018 supports a single phospholipid surface around neutral storage
    lipids and separates mature topology from biogenesis models. It does not by itself
    supply primary formation-necessity experiments.
  snapshot_sha256: 8c520a2ae66e79618d8112cd69b5c8712ef50fcddda7e2bc07ebf920f344ef7d
- evidence_id: septin-root19-sources-jats-PMC3229976
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3229976.1/PMC3229976.1.xml
  locator: 'Fresh native JATS: metadata, Introduction s0005, strain/culture s0015,
    fractionation s0020, lipid analysis s0030, Results s0055/s0060 and strain-context
    figure caption. No full proteome/raw-MS or figure-pixel analysis.'
  accessed_at: '2026-11-03T08:11:35.869655Z'
  support: supports
  summary: Grillitsch 2011 examines isolated yeast lipid particles under glucose/oleate
    conditions and supports phospholipid surface material with condition-dependent
    lipid composition. Generic class-level necessity is not a requirement for each
    individual phospholipid species.
  snapshot_sha256: 557af7ea56ca661d74f43edabb9ad51b40ba8fe267d6d907f975306e2ff20cd2
- evidence_id: septin-parasporal-agent-jats-PMC4280536
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4280536.1/PMC4280536.1.xml
  locator: 'Fresh native secondary-review JATS: metadata, sections1,2,3 opening,3.1
    opening,3.1.2 and3.2. No complete underlying-primary-paper or toxicity-mechanism
    audit.'
  accessed_at: '2026-11-03T08:11:40.509105Z'
  support: supports
  summary: Palma 2014 distinguishes multiple unrelated Cry lineages and Cyt proteins,
    and distinguishes crystals from secreted toxins. The mixed constituent label cannot
    be assigned one supposedly universal Cry/Cyt family.
  snapshot_sha256: 7462136cb1b99214d5931f23a79d3031df6e1bc262d941f8fe459419ebd186c5
- evidence_id: septin-parasporal-agent-jats-PMC4014730
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4014730.1/PMC4014730.1.xml
  locator: 'Fresh native secondary-review JATS: metadata, sections1–2,3 opening,3.1
    major and3.2 minor proteins. Later toxicity/application sections not comprehensively
    audited.'
  accessed_at: '2026-11-03T08:11:40.525960Z'
  support: supports
  summary: Ben-Dov 2014 supports a strain/plasmid-dependent Bti crystal repertoire
    including the three recorded examples. Modern protein identities are not inferred
    from historical light/dark lattice appearance.
  snapshot_sha256: d7586294888069f26e7d707db2a336c4a19395970cb917f6d0639c90490b5de2
- evidence_id: septin-parasporal-agent-legacy-PMC1857359
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1857359/
  locator: 'Fresh genuine PMC secondary-review HTML: complete abstract and Introduction
    only; downstream receptor mechanisms and full section2 not independently audited.'
  accessed_at: '2026-11-03T08:11:40.540636Z'
  support: supports
  summary: Bravo 2007 supports the coarse distinction between the crystal packaging
    state and activated toxin action. It is secondary contextual evidence, not a new
    crystal-formation experiment.
  snapshot_sha256: 2245fc3dd2bcc09d32420bf9e3a27786cca156d127553b7cd69121f60db6ed9b
- evidence_id: septin-aggresome-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0016234,GO:0016235,GO:0005737,GO:0048255
  locator: Fresh native accession, label, definition, synonym types and relevant hierarchy/parthood;
    broad GO child lists are not a new exhaustive ontology search.
  accessed_at: '2026-11-03T08:11:28.018772Z'
  support: supports
  summary: GO0016235 requires dynein-dependent microtubule transport; GO0016234 inclusion
    body, GO0005737 cytoplasm and GO0048255 mRNA stabilization retain their distinct
    scopes.
  snapshot_sha256: f2a31c4df2153f36417cd25d3ce8f59a4743ec32f437f207b52104deb0bbcfbb
- evidence_id: septin-aggresome-agent-so
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/so/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FSO_0000234
  locator: Fresh native accession, label, definition, synonym types and relevant hierarchy/parthood;
    broad GO child lists are not a new exhaustive ontology search.
  accessed_at: '2026-11-03T08:11:28.019058Z'
  support: supports
  summary: SO0000234 denotes mRNA; exact molecular class identity only.
  snapshot_sha256: d11dcc2fd540bdf6528172e73d4bea70206ce9f9ccb212c1323642a27dd609d7
- evidence_id: septin-root19-sources-gas-shell-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031411,GO:0033172
  locator: Fresh native accession, label, definition, synonym types and relevant hierarchy/parthood;
    broad GO child lists are not a new exhaustive ontology search.
  accessed_at: '2026-11-03T08:11:31.229774Z'
  support: supports
  summary: GO0033172 denotes proteinaceous gas-vesicle shell, part of GO0031411; the
    membrane synonym does not imply lipid bilayer.
  snapshot_sha256: ad6c8c92958bfdb85c7422292bdce1ace8fce968688f8f6764494b01853897d4
- evidence_id: septin-root19-sources-lipid-monolayer-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005811,GO:0034430
  locator: Fresh native accession, label, definition, synonym types and relevant hierarchy/parthood;
    broad GO child lists are not a new exhaustive ontology search.
  accessed_at: '2026-11-03T08:11:34.664881Z'
  support: supports
  summary: GO0034430 denotes the single phospholipid layer; GO0005811 denotes its
    containing lipid droplet.
  snapshot_sha256: be2beacb7198f4be9b541c7a730115400736e3f32e29a8cb0bd23d26db532d84
- evidence_id: septin-parasporal-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0016234
  locator: Fresh native accession, label, definition, synonym types and relevant hierarchy/parthood;
    broad GO child lists are not a new exhaustive ontology search.
  accessed_at: '2026-11-03T08:11:36.288553Z'
  support: supports
  summary: GO0016234 is inclusion body, a broader parent rather than an exact identity
    for the parasporal crystal.
  snapshot_sha256: f81fa199c4b5bb4fd75f51d03590dbb142f330253d43e483e2932f8d73f6af13
- evidence_id: septin-root19-sources-CHEBI-16247
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/16247/
  locator: Fresh native accession, label, definition, synonym types and relevant hierarchy/parthood;
    broad GO child lists are not a new exhaustive ontology search.
  accessed_at: '2026-11-03T08:11:34.948276Z'
  support: supports
  summary: CHEBI16247 is phospholipid, a chemical class rather than an individual
    lipid species.
  snapshot_sha256: c43d6c08d37ee710679ce93e8a797e2fd09bc8f8fd8e800adcba56ebcc4c1f7a
- evidence_id: septin-aggresome-agent-tax-83333
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333
  locator: ENA exact taxId, scientificName, rank and relevant alternative-name/lineage
    fields.
  accessed_at: '2026-11-03T08:11:30.246421Z'
  support: supports
  summary: Authority resolves 83333 to Escherichia coli K-12; taxonomy identity does
    not establish prevalence, exact strain equivalence or structural membership.
  snapshot_sha256: f499fde9e4fcea85ff811b58a76a405669d32465a62eaf74240a48331b63d8e6
- evidence_id: septin-aggresome-agent-tax-511145
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/511145
  locator: ENA exact taxId, scientificName, rank and relevant alternative-name/lineage
    fields.
  accessed_at: '2026-11-03T08:11:30.848188Z'
  support: supports
  summary: Authority resolves 511145 to Escherichia coli str. K-12 substr. MG1655;
    taxonomy identity does not establish prevalence, exact strain equivalence or structural
    membership.
  snapshot_sha256: e3a402d3d5b5d1b11deda22f50922b38962f0bb955b7fa8edfea0a937277199e
- evidence_id: septin-root19-sources-NCBITaxon-2
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2
  locator: ENA exact taxId, scientificName, rank and relevant alternative-name/lineage
    fields.
  accessed_at: '2026-11-03T08:11:31.390670Z'
  support: supports
  summary: Authority resolves 2 to Bacteria; taxonomy identity does not establish
    prevalence, exact strain equivalence or structural membership.
  snapshot_sha256: 314bd7723b8dea04f1840809fb74e06c514664fba9c6a0619e8f12e2a6dceef1
- evidence_id: septin-root19-sources-NCBITaxon-2157
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2157
  locator: ENA exact taxId, scientificName, rank and relevant alternative-name/lineage
    fields.
  accessed_at: '2026-11-03T08:11:31.452455Z'
  support: supports
  summary: Authority resolves 2157 to Archaea; taxonomy identity does not establish
    prevalence, exact strain equivalence or structural membership.
  snapshot_sha256: 84a40b3fb3e403b1ab61ce4ab647c6eaa5526395605d947756d90105e0512a3d
- evidence_id: septin-root19-sources-NCBITaxon-315271
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/315271
  locator: ENA exact taxId, scientificName, rank and relevant alternative-name/lineage
    fields.
  accessed_at: '2026-11-03T08:11:31.838856Z'
  support: supports
  summary: Authority resolves 315271 to Dolichospermum flos-aquae CCAP 1403/13F; taxonomy
    identity does not establish prevalence, exact strain equivalence or structural
    membership.
  snapshot_sha256: 8f2267f7f1758368a7a36f3fbe2ce4d83e27cbea825e483d1c195128fd0f880f
- evidence_id: septin-root19-sources-NCBITaxon-2692880
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2692880
  locator: ENA exact taxId, scientificName, rank and relevant alternative-name/lineage
    fields.
  accessed_at: '2026-11-03T08:11:31.887752Z'
  support: supports
  summary: Authority resolves 2692880 to Anabaena cylindrica FACHB-318; taxonomy identity
    does not establish prevalence, exact strain equivalence or structural membership.
  snapshot_sha256: e4dab743ef84d8c29af966b0ff5c1625d544ad0b63ef3da600e945e569c1061d
- evidence_id: septin-root19-sources-NCBITaxon-4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: ENA exact taxId, scientificName, rank and relevant alternative-name/lineage
    fields.
  accessed_at: '2026-11-03T08:11:34.996336Z'
  support: supports
  summary: Authority resolves 4932 to Saccharomyces cerevisiae; taxonomy identity
    does not establish prevalence, exact strain equivalence or structural membership.
  snapshot_sha256: 38f43dd1593a1d47416228ae385464f30aeb8302c3aadb45b3588d03744bc814
- evidence_id: septin-parasporal-agent-tax-1428
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1428
  locator: ENA exact taxId, scientificName, rank and relevant alternative-name/lineage
    fields.
  accessed_at: '2026-11-03T08:11:36.515630Z'
  support: supports
  summary: Authority resolves 1428 to Bacillus thuringiensis; taxonomy identity does
    not establish prevalence, exact strain equivalence or structural membership.
  snapshot_sha256: f58b68f9e1af6b80692b79630ff049ff30dba2e0cdabbe924174737451ee4e85
- evidence_id: septin-parasporal-agent-tax-1430
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1430
  locator: ENA exact taxId, scientificName, rank and relevant alternative-name/lineage
    fields.
  accessed_at: '2026-11-03T08:11:36.866724Z'
  support: supports
  summary: Authority resolves 1430 to Bacillus thuringiensis serovar israelensis;
    taxonomy identity does not establish prevalence, exact strain equivalence or structural
    membership.
  snapshot_sha256: 3df9dafb0d1030c11f1728228e71a9355ae1d62caf32db7be6407eb9257671e8
- evidence_id: septin-aggresome-agent-P0A6H5
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0A6H5.json
  locator: Fresh UniProt primaryAccession, entryType, recommended protein name, gene,
    organism and InterPro cross-references; annotation is not direct experimental
    membership.
  accessed_at: '2026-11-03T08:11:28.744067Z'
  support: supports
  summary: 'P0A6H5: ATP-dependent protease ATPase subunit HslU; UniProtKB reviewed
    (Swiss-Prot); taxon 83333. Concrete identity checked independently from source-based
    membership and assembly necessity.'
  snapshot_sha256: 5b1f0a0cd15bf350edb1348cfeb803e6b9774608266b6f7b8cf1f254ca6e22b1
- evidence_id: septin-aggresome-agent-P0AB77
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0AB77.json
  locator: Fresh UniProt primaryAccession, entryType, recommended protein name, gene,
    organism and InterPro cross-references; annotation is not direct experimental
    membership.
  accessed_at: '2026-11-03T08:11:28.770204Z'
  support: supports
  summary: 'P0AB77: 2-amino-3-ketobutyrate coenzyme A ligase; UniProtKB reviewed (Swiss-Prot);
    taxon 83333. Concrete identity checked independently from source-based membership
    and assembly necessity.'
  snapshot_sha256: 9407fd76a12ceb1f0afbd7cf7ee9d2de0c48d6d60b2a965afcdd6e048e032332
- evidence_id: septin-aggresome-agent-P36683
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P36683.json
  locator: Fresh UniProt primaryAccession, entryType, recommended protein name, gene,
    organism and InterPro cross-references; annotation is not direct experimental
    membership.
  accessed_at: '2026-11-03T08:11:28.790739Z'
  support: supports
  summary: 'P36683: Aconitate hydratase B; UniProtKB reviewed (Swiss-Prot); taxon
    83333. Concrete identity checked independently from source-based membership and
    assembly necessity.'
  snapshot_sha256: 6b47f414de4336cbd14a07e459d1bc8c1a540dad0d4c1d10e899c79d2d212f45
- evidence_id: septin-root19-sources-UniProtKB-A0ABR7ZBW9
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/A0ABR7ZBW9.json
  locator: Fresh UniProt primaryAccession, entryType, recommended protein name, gene,
    organism and InterPro cross-references; annotation is not direct experimental
    membership.
  accessed_at: '2026-11-03T08:11:32.670579Z'
  support: supports
  summary: 'A0ABR7ZBW9: Gas vesicle protein A; UniProtKB unreviewed (TrEMBL); taxon
    2692880. Concrete identity checked independently from source-based membership
    and assembly necessity.'
  snapshot_sha256: 34d92f939cc1dc7899f4c142a659990a2a21ee3745864218f95778e92a569876
- evidence_id: septin-root19-sources-UniProtKB-A0ABR7ZCB1
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/A0ABR7ZCB1.json
  locator: Fresh UniProt primaryAccession, entryType, recommended protein name, gene,
    organism and InterPro cross-references; annotation is not direct experimental
    membership.
  accessed_at: '2026-11-03T08:11:32.707148Z'
  support: supports
  summary: 'A0ABR7ZCB1: Gas vesicle protein C; UniProtKB unreviewed (TrEMBL); taxon
    2692880. Concrete identity checked independently from source-based membership
    and assembly necessity.'
  snapshot_sha256: 7fb97f1d9559cd29d3a714a3e474c9b89c8a2fff0068708c4d41b12119aa2964
- evidence_id: septin-parasporal-agent-P16480
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P16480.json
  locator: Fresh UniProt primaryAccession, entryType, recommended protein name, gene,
    organism and InterPro cross-references; annotation is not direct experimental
    membership.
  accessed_at: '2026-11-03T08:11:37.050398Z'
  support: supports
  summary: 'P16480: Pesticidal crystal protein Cry4Aa; UniProtKB reviewed (Swiss-Prot);
    taxon 1430. Concrete identity checked independently from source-based membership
    and assembly necessity.'
  snapshot_sha256: a85e173a5881d66bd084d067806109b4794b7f09eecb90eca3d865375a22e2e1
- evidence_id: septin-parasporal-agent-P21256
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P21256.json
  locator: Fresh UniProt primaryAccession, entryType, recommended protein name, gene,
    organism and InterPro cross-references; annotation is not direct experimental
    membership.
  accessed_at: '2026-11-03T08:11:37.132962Z'
  support: supports
  summary: 'P21256: Pesticidal crystal protein Cry11Aa; UniProtKB reviewed (Swiss-Prot);
    taxon 1430. Concrete identity checked independently from source-based membership
    and assembly necessity.'
  snapshot_sha256: 35914c4b20d4e6706569ea2e44e0fde652c13f9b1864a392db8d49de1266bc52
- evidence_id: septin-parasporal-agent-P0A382
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0A382.json
  locator: Fresh UniProt primaryAccession, entryType, recommended protein name, gene,
    organism and InterPro cross-references; annotation is not direct experimental
    membership.
  accessed_at: '2026-11-03T08:11:37.767990Z'
  support: supports
  summary: 'P0A382: Type-1Aa cytolytic delta-endotoxin; UniProtKB reviewed (Swiss-Prot);
    taxon 1430. Concrete identity checked independently from source-based membership
    and assembly necessity.'
  snapshot_sha256: 4f0cdbd015376e14c7bd7727fe8478d0e480d9eb32ab63a4a696c9c7bdac3d8a
- evidence_id: septin-aggresome-agent-IPR004491
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004491/
  locator: Fresh InterPro/Pfam accession, name, type, hierarchy, integrated/member
    signatures; non-LLM IPR000638 description additionally inspected. Generated descriptions
    excluded.
  accessed_at: '2026-11-03T08:11:29.236527Z'
  support: supports
  summary: IPR004491 is type family, named Heat shock protein HslU. Native hierarchy/integration
    and member signatures checked; family, repeat and exact-component scopes remain
    distinct.
  snapshot_sha256: 951e85c4faccb707ab1ab1faa7439da273827a28977d4d806f1a4dddd41b64ca
- evidence_id: septin-aggresome-agent-IPR011282
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR011282/
  locator: Fresh InterPro/Pfam accession, name, type, hierarchy, integrated/member
    signatures; non-LLM IPR000638 description additionally inspected. Generated descriptions
    excluded.
  accessed_at: '2026-11-03T08:11:29.580545Z'
  support: supports
  summary: IPR011282 is type family, named 2-amino-3-ketobutyrate coenzyme A ligase.
    Native hierarchy/integration and member signatures checked; family, repeat and
    exact-component scopes remain distinct.
  snapshot_sha256: 7ad07d461c7ee5fb160f71c0148c217d445ed90e9869e24f55d8358ca5dd8654
- evidence_id: septin-aggresome-agent-IPR004406
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004406/
  locator: Fresh InterPro/Pfam accession, name, type, hierarchy, integrated/member
    signatures; non-LLM IPR000638 description additionally inspected. Generated descriptions
    excluded.
  accessed_at: '2026-11-03T08:11:29.602627Z'
  support: supports
  summary: IPR004406 is type family, named Aconitase B. Native hierarchy/integration
    and member signatures checked; family, repeat and exact-component scopes remain
    distinct.
  snapshot_sha256: 31e5072ecdf886cf06d48c0c607defcf979a412f2e6504bdb7f2c71c5a2f3900
- evidence_id: septin-root19-sources-PF00741
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF00741/
  locator: Fresh InterPro/Pfam accession, name, type, hierarchy, integrated/member
    signatures; non-LLM IPR000638 description additionally inspected. Generated descriptions
    excluded.
  accessed_at: '2026-11-03T08:11:33.054138Z'
  support: supports
  summary: PF00741 is type family, named Gas vesicle protein. Native hierarchy/integration
    and member signatures checked; family, repeat and exact-component scopes remain
    distinct.
  snapshot_sha256: 094064b336ab239cf609df86bac5b25cc3ad373caa44cd1796ebd8a4bf4a4936
- evidence_id: septin-root19-sources-PF01304
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01304/
  locator: Fresh InterPro/Pfam accession, name, type, hierarchy, integrated/member
    signatures; non-LLM IPR000638 description additionally inspected. Generated descriptions
    excluded.
  accessed_at: '2026-11-03T08:11:33.284488Z'
  support: supports
  summary: PF01304 is type repeat, named Gas vesicles protein GVPc repeated domain.
    Native hierarchy/integration and member signatures checked; family, repeat and
    exact-component scopes remain distinct.
  snapshot_sha256: ac3440f2567cdc7a520c86932e6e48572da87a6b929996f1e6825f1588ac08bb
- evidence_id: septin-root19-sources-IPR000638
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000638/
  locator: Fresh InterPro/Pfam accession, name, type, hierarchy, integrated/member
    signatures; non-LLM IPR000638 description additionally inspected. Generated descriptions
    excluded.
  accessed_at: '2026-11-03T08:11:33.302880Z'
  support: supports
  summary: IPR000638 is type family, named Gas vesicle protein GvpA-like. Native hierarchy/integration
    and member signatures checked; family, repeat and exact-component scopes remain
    distinct. The non-LLM description includes related GvpJ/GvpM, supporting broader
    GvpA-like scope.
  snapshot_sha256: b8a432cd24b4028ffa38aa595c4f64ce3b73ef3b9eca03bc4b32315b2f698905
- evidence_id: septin-root19-sources-IPR047870
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR047870/
  locator: Fresh InterPro/Pfam accession, name, type, hierarchy, integrated/member
    signatures; non-LLM IPR000638 description additionally inspected. Generated descriptions
    excluded.
  accessed_at: '2026-11-03T08:11:33.889534Z'
  support: supports
  summary: IPR047870 is type family, named Gas vesicle protein GvpA. Native hierarchy/integration
    and member signatures checked; family, repeat and exact-component scopes remain
    distinct. The exact GvpA child family integrates HAMAP MF_00576 and is also present
    on the recorded GvpA accession.
  snapshot_sha256: 0cd1400385b42f3e2e41ae75b7e5db55e227e5a7a1e3a561b9fc69349d395833
- evidence_id: septin-root19-sources-IPR050530
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050530/
  locator: Fresh InterPro/Pfam accession, name, type, hierarchy, integrated/member
    signatures; non-LLM IPR000638 description additionally inspected. Generated descriptions
    excluded.
  accessed_at: '2026-11-03T08:11:33.896276Z'
  support: supports
  summary: IPR050530 is type family, named Gas Vesicle Protein A. Native hierarchy/integration
    and member signatures checked; family, repeat and exact-component scopes remain
    distinct. Generated description is excluded from biological evidence.
  snapshot_sha256: cc3ca729aece182c5415a7eb34a6b2b813dd867864ce6cba3b32c4fc23eab0f6
- evidence_id: septin-root19-sources-IPR002003
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002003/
  locator: Fresh InterPro/Pfam accession, name, type, hierarchy, integrated/member
    signatures; non-LLM IPR000638 description additionally inspected. Generated descriptions
    excluded.
  accessed_at: '2026-11-03T08:11:33.914153Z'
  support: supports
  summary: IPR002003 is type repeat, named Gas vesicle protein GvpC. Native hierarchy/integration
    and member signatures checked; family, repeat and exact-component scopes remain
    distinct.
  snapshot_sha256: d31616233044357ce15cb317a8bdef4507b3725e7a3b3cb575631e0f95377503
- evidence_id: septin-root19-sources-IPR018185
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR018185/
  locator: Fresh InterPro/Pfam accession, name, type, hierarchy, integrated/member
    signatures; non-LLM IPR000638 description additionally inspected. Generated descriptions
    excluded.
  accessed_at: '2026-11-03T08:11:34.009941Z'
  support: supports
  summary: IPR018185 is type repeat, named Gas vesicle C repeat. Native hierarchy/integration
    and member signatures checked; family, repeat and exact-component scopes remain
    distinct.
  snapshot_sha256: 54cdbb1f2c04b33103217fd2d44fb827c0fd43350c97ef38dd081329ac6d25ef
- evidence_id: septin-parasporal-agent-IPR038979
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR038979/
  locator: Fresh InterPro/Pfam accession, name, type, hierarchy, integrated/member
    signatures; non-LLM IPR000638 description additionally inspected. Generated descriptions
    excluded.
  accessed_at: '2026-11-03T08:11:39.359508Z'
  support: supports
  summary: IPR038979 is type family, named Pesticidal crystal protein. Native hierarchy/integration
    and member signatures checked; family, repeat and exact-component scopes remain
    distinct.
  snapshot_sha256: c13fed07696f9c16865e27d32db314abdcd59edd7d193773ab8f495c4f59a54d
- evidence_id: septin-parasporal-agent-IPR001615
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001615/
  locator: Fresh InterPro/Pfam accession, name, type, hierarchy, integrated/member
    signatures; non-LLM IPR000638 description additionally inspected. Generated descriptions
    excluded.
  accessed_at: '2026-11-03T08:11:39.734071Z'
  support: supports
  summary: IPR001615 is type family, named Delta-endotoxin CytB. Native hierarchy/integration
    and member signatures checked; family, repeat and exact-component scopes remain
    distinct.
  snapshot_sha256: 9defe1bceddd9d1b0f01af80889fac5813be3af89524bbf37c5192f94c1f90d3
- evidence_id: septin-aggresome-agent-ipr-matches-P0A6H5
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P0A6H5/?page_size=200
  locator: Native protein-specific InterPro entry list; page_size200, accession/name/type
    and next/count; bounded sequence annotation.
  accessed_at: '2026-11-03T08:11:29.865108Z'
  support: supports
  summary: Returned 6 annotations, next=None; family identity corroboration only,
    without equating all Cry/Cyt proteins or converting domains into whole proteins.
  snapshot_sha256: 8b8e83bf3e83d0adda7b14bfc2211f7ffb4d3b364cf0ac4e74fb4787b55f9993
- evidence_id: septin-aggresome-agent-ipr-matches-P0AB77
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P0AB77/?page_size=200
  locator: Native protein-specific InterPro entry list; page_size200, accession/name/type
    and next/count; bounded sequence annotation.
  accessed_at: '2026-11-03T08:11:29.965726Z'
  support: supports
  summary: Returned 7 annotations, next=None; family identity corroboration only,
    without equating all Cry/Cyt proteins or converting domains into whole proteins.
  snapshot_sha256: 787db1246babcf64a482031fc244cef7e5680deeb15e62f6f228a6215d844409
- evidence_id: septin-aggresome-agent-ipr-matches-P36683
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P36683/?page_size=200
  locator: Native protein-specific InterPro entry list; page_size200, accession/name/type
    and next/count; bounded sequence annotation.
  accessed_at: '2026-11-03T08:11:30.211835Z'
  support: supports
  summary: Returned 12 annotations, next=None; family identity corroboration only,
    without equating all Cry/Cyt proteins or converting domains into whole proteins.
  snapshot_sha256: b97a111f85e809ccdf13e0fd7f8a262f418b7aae864b0298af0175233fa19085
- evidence_id: septin-parasporal-agent-matches-P16480
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P16480/?page_size=200
  locator: Native protein-specific InterPro entry list; page_size200, accession/name/type
    and next/count; bounded sequence annotation.
  accessed_at: '2026-11-03T08:11:38.721606Z'
  support: supports
  summary: Returned 9 annotations, next=None; family identity corroboration only,
    without equating all Cry/Cyt proteins or converting domains into whole proteins.
  snapshot_sha256: 7be0ac98f6ab81cb93a887afc9e407b600131d5f3d28292f08a0841c636463cf
- evidence_id: septin-parasporal-agent-matches-P21256
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P21256/?page_size=200
  locator: Native protein-specific InterPro entry list; page_size200, accession/name/type
    and next/count; bounded sequence annotation.
  accessed_at: '2026-11-03T08:11:38.779764Z'
  support: supports
  summary: Returned 3 annotations, next=None; family identity corroboration only,
    without equating all Cry/Cyt proteins or converting domains into whole proteins.
  snapshot_sha256: a100a7dd31e693f383e5e55234cb937f3d6f09b7395a640d89c59af220031e98
- evidence_id: septin-parasporal-agent-matches-P0A382
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P0A382/?page_size=200
  locator: Native protein-specific InterPro entry list; page_size200, accession/name/type
    and next/count; bounded sequence annotation.
  accessed_at: '2026-11-03T08:11:39.341975Z'
  support: supports
  summary: Returned 2 annotations, next=None; family identity corroboration only,
    without equating all Cry/Cyt proteins or converting domains into whole proteins.
  snapshot_sha256: de4dd78a4b1081abfc8a884955f77ae56c1e55675841b79a80a90c3edf9311cb
- evidence_id: septin-aggresome-agent-reviewed-uniqueness
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A83333+AND+%28gene_exact%3AhslU+OR+gene_exact%3Akbl+OR+gene_exact%3AacnB%29&format=json&size=500
  locator: Exact stated reviewed/gene/taxon UniProt query; returned results only;
    suggestions are not substituted queries.
  accessed_at: '2026-11-03T08:11:30.848474Z'
  support: supports
  summary: Returned accessions ['P36683', 'P0AB77', 'P0A6H5']. Zero returned reviewed
    entries, where applicable, is limited to this query and is not biological absence.
  snapshot_sha256: 232e256a842a61b847a0732d27eb3f10cc930638eb222407b2151080812282ae
  search_scope: 'Database rest.uniprot.org; exact endpoint https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A83333+AND+%28gene_exact%3AhslU+OR+gene_exact%3Akbl+OR+gene_exact%3AacnB%29&format=json&size=500;
    query parameters {''query'': [''reviewed:true AND organism_id:83333 AND (gene_exact:hslU
    OR gene_exact:kbl OR gene_exact:acnB)''], ''format'': [''json''], ''size'': [''500'']};
    first returned response only, no date/publication restriction; accessed 2026-11-03T08:11:30.848474Z.
    UniProt size500 where specified, otherwise server first-page limit; exact stated
    gene/taxon/reviewed constraints. No exhaustive literature, ontology or biological
    absence conclusion.'
- evidence_id: septin-root19-sources-query-gvpA-2692880
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3AgvpA%29%20AND%20%28taxonomy_id%3A2692880%29%20AND%20%28reviewed%3Atrue%29
  locator: Exact stated reviewed/gene/taxon UniProt query; returned results only;
    suggestions are not substituted queries.
  accessed_at: '2026-11-03T08:11:32.869273Z'
  support: supports
  summary: Returned accessions []. Zero returned reviewed entries, where applicable,
    is limited to this query and is not biological absence.
  snapshot_sha256: 7e5118451ca023452db92758ff8788accbfe362c60551c059442b21eb3c6ce6c
  search_scope: 'Database rest.uniprot.org; exact endpoint https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3AgvpA%29%20AND%20%28taxonomy_id%3A2692880%29%20AND%20%28reviewed%3Atrue%29;
    query parameters {''format'': [''json''], ''size'': [''500''], ''query'': [''(gene_exact:gvpA)
    AND (taxonomy_id:2692880) AND (reviewed:true)'']}; first returned response only,
    no date/publication restriction; accessed 2026-11-03T08:11:32.869273Z. UniProt
    size500 where specified, otherwise server first-page limit; exact stated gene/taxon/reviewed
    constraints. No exhaustive literature, ontology or biological absence conclusion.'
- evidence_id: septin-root19-sources-query-gvpC-2692880
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3AgvpC%29%20AND%20%28taxonomy_id%3A2692880%29%20AND%20%28reviewed%3Atrue%29
  locator: Exact stated reviewed/gene/taxon UniProt query; returned results only;
    suggestions are not substituted queries.
  accessed_at: '2026-11-03T08:11:32.965391Z'
  support: supports
  summary: Returned accessions []. Zero returned reviewed entries, where applicable,
    is limited to this query and is not biological absence.
  snapshot_sha256: 75ce72662b3715249c0c38ae60cf28f0d5a2c8133776ba6b7e5d518050cffae2
  search_scope: 'Database rest.uniprot.org; exact endpoint https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3AgvpC%29%20AND%20%28taxonomy_id%3A2692880%29%20AND%20%28reviewed%3Atrue%29;
    query parameters {''format'': [''json''], ''size'': [''500''], ''query'': [''(gene_exact:gvpC)
    AND (taxonomy_id:2692880) AND (reviewed:true)'']}; first returned response only,
    no date/publication restriction; accessed 2026-11-03T08:11:32.965391Z. UniProt
    size500 where specified, otherwise server first-page limit; exact stated gene/taxon/reviewed
    constraints. No exhaustive literature, ontology or biological absence conclusion.'
- evidence_id: septin-parasporal-agent-query-cry4Aa
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3Acry4Aa%29%20AND%20%28organism_id%3A1430%29%20AND%20%28reviewed%3Atrue%29
  locator: Exact stated reviewed/gene/taxon UniProt query; returned results only;
    suggestions are not substituted queries.
  accessed_at: '2026-11-03T08:11:37.073698Z'
  support: supports
  summary: Returned accessions ['P16480']. Zero returned reviewed entries, where applicable,
    is limited to this query and is not biological absence.
  snapshot_sha256: b1fe6c921afde1a98b0b2ee3a9f56a5efd8cd2bb608506584b7d78c85f915489
  search_scope: 'Database rest.uniprot.org; exact endpoint https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3Acry4Aa%29%20AND%20%28organism_id%3A1430%29%20AND%20%28reviewed%3Atrue%29;
    query parameters {''format'': [''json''], ''query'': [''(gene_exact:cry4Aa) AND
    (organism_id:1430) AND (reviewed:true)'']}; first returned response only, no date/publication
    restriction; accessed 2026-11-03T08:11:37.073698Z. UniProt size500 where specified,
    otherwise server first-page limit; exact stated gene/taxon/reviewed constraints.
    No exhaustive literature, ontology or biological absence conclusion.'
- evidence_id: septin-parasporal-agent-query-cry11Aa
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3Acry11Aa%29%20AND%20%28organism_id%3A1430%29%20AND%20%28reviewed%3Atrue%29
  locator: Exact stated reviewed/gene/taxon UniProt query; returned results only;
    suggestions are not substituted queries.
  accessed_at: '2026-11-03T08:11:37.453085Z'
  support: supports
  summary: Returned accessions ['P21256']. Zero returned reviewed entries, where applicable,
    is limited to this query and is not biological absence.
  snapshot_sha256: c28b5f9c7d83305f62fa1694feb2c32fb9af94185d5ebda66ec2a7ec04e2a5f9
  search_scope: 'Database rest.uniprot.org; exact endpoint https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3Acry11Aa%29%20AND%20%28organism_id%3A1430%29%20AND%20%28reviewed%3Atrue%29;
    query parameters {''format'': [''json''], ''query'': [''(gene_exact:cry11Aa) AND
    (organism_id:1430) AND (reviewed:true)'']}; first returned response only, no date/publication
    restriction; accessed 2026-11-03T08:11:37.453085Z. UniProt size500 where specified,
    otherwise server first-page limit; exact stated gene/taxon/reviewed constraints.
    No exhaustive literature, ontology or biological absence conclusion.'
- evidence_id: septin-parasporal-agent-query-cyt1Aa
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3Acyt1Aa%29%20AND%20%28organism_id%3A1430%29%20AND%20%28reviewed%3Atrue%29
  locator: Exact stated reviewed/gene/taxon UniProt query; returned results only;
    suggestions are not substituted queries.
  accessed_at: '2026-11-03T08:11:37.922351Z'
  support: supports
  summary: Returned accessions ['P0A382']. Zero returned reviewed entries, where applicable,
    is limited to this query and is not biological absence.
  snapshot_sha256: e6443b1e92ad739aa0a71ba5537b890529a61a986f9c67d1299a3d78181f592e
  search_scope: 'Database rest.uniprot.org; exact endpoint https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3Acyt1Aa%29%20AND%20%28organism_id%3A1430%29%20AND%20%28reviewed%3Atrue%29;
    query parameters {''format'': [''json''], ''query'': [''(gene_exact:cyt1Aa) AND
    (organism_id:1430) AND (reviewed:true)'']}; first returned response only, no date/publication
    restriction; accessed 2026-11-03T08:11:37.922351Z. UniProt size500 where specified,
    otherwise server first-page limit; exact stated gene/taxon/reviewed constraints.
    No exhaustive literature, ontology or biological absence conclusion.'
- evidence_id: septin-parasporal-agent-ols-exact-0
  kind: search
  reference: https://www.ebi.ac.uk/ols4/api/search?ontology=go&exact=true&rows=100&q=parasporal%20crystal
  locator: OLS GO exact phrase, rows100; native numFound/docs.
  accessed_at: '2026-11-03T08:11:36.459097Z'
  support: supports
  summary: Both bounded exact-phrase queries return zero terms; this does not prove
    exhaustive GO absence or replace identity reasoning.
  snapshot_sha256: 8d33fdeb26a2d16294a3c5f4a7f444578bb462aa6036d45a15e9bfadfe47fbd2
  search_scope: 'Database www.ebi.ac.uk; exact endpoint https://www.ebi.ac.uk/ols4/api/search?ontology=go&exact=true&rows=100&q=parasporal%20crystal;
    query parameters {''ontology'': [''go''], ''exact'': [''true''], ''rows'': [''100''],
    ''q'': [''parasporal crystal'']}; first returned response only, no date/publication
    restriction; accessed 2026-11-03T08:11:36.459097Z. OLS rows100; exact GO phrase
    only. No exhaustive literature, ontology or biological absence conclusion.'
- evidence_id: septin-parasporal-agent-ols-exact-1
  kind: search
  reference: https://www.ebi.ac.uk/ols4/api/search?ontology=go&exact=true&rows=100&q=parasporal%20body
  locator: OLS GO exact phrase, rows100; native numFound/docs.
  accessed_at: '2026-11-03T08:11:36.461804Z'
  support: supports
  summary: Both bounded exact-phrase queries return zero terms; this does not prove
    exhaustive GO absence or replace identity reasoning.
  snapshot_sha256: 8d33fdeb26a2d16294a3c5f4a7f444578bb462aa6036d45a15e9bfadfe47fbd2
  search_scope: 'Database www.ebi.ac.uk; exact endpoint https://www.ebi.ac.uk/ols4/api/search?ontology=go&exact=true&rows=100&q=parasporal%20body;
    query parameters {''ontology'': [''go''], ''exact'': [''true''], ''rows'': [''100''],
    ''q'': [''parasporal body'']}; first returned response only, no date/publication
    restriction; accessed 2026-11-03T08:11:36.461804Z. OLS rows100; exact GO phrase
    only. No exhaustive literature, ontology or biological absence conclusion.'
- evidence_id: septin-root19-sources-PMID-1510555
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A1510555%20AND%20SRC%3AMED
  locator: Europe PMC exact PMID native metadata and complete abstract; source tier
    follows article type, no full-body inference.
  accessed_at: '2026-11-03T08:11:32.048754Z'
  support: supports
  summary: Gas vesicles are strengthened by the outer-surface protein, GvpC. Bibliographic
    identity and abstract checked. GvpC removal/rebinding changes collapse strength
    of assembled vesicles; formation necessity is not tested.
  snapshot_sha256: 927ef879e68686d9c6488f9579ecfd16ff2005fa8c1da214d3a7aef2402172fa
  search_scope: 'Database www.ebi.ac.uk; exact endpoint https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A1510555%20AND%20SRC%3AMED;
    query parameters {''format'': [''json''], ''resultType'': [''core''], ''query'':
    [''EXT_ID:1510555 AND SRC:MED'']}; first returned response only, no date/publication
    restriction; accessed 2026-11-03T08:11:32.048754Z. Europe PMC pageSize25 default;
    exact PMID identity only. No exhaustive literature, ontology or biological absence
    conclusion.'
- evidence_id: septin-root19-sources-PMID-22147705
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A22147705%20AND%20SRC%3AMED
  locator: Europe PMC exact PMID native metadata and complete abstract; source tier
    follows article type, no full-body inference.
  accessed_at: '2026-11-03T08:11:31.989074Z'
  support: supports
  summary: An amyloid organelle, solid-state NMR evidence for cross-β assembly of
    gas vesicles. Bibliographic identity and abstract checked. Bayro is the first
    author; full-body scope is separately recorded.
  snapshot_sha256: c767d01fa7e084617869109579a7bb785349bf10abc477bde0a37b9d04e7befd
  search_scope: 'Database www.ebi.ac.uk; exact endpoint https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A22147705%20AND%20SRC%3AMED;
    query parameters {''format'': [''json''], ''resultType'': [''core''], ''query'':
    [''EXT_ID:22147705 AND SRC:MED'']}; first returned response only, no date/publication
    restriction; accessed 2026-11-03T08:11:31.989074Z. Europe PMC pageSize25 default;
    exact PMID identity only. No exhaustive literature, ontology or biological absence
    conclusion.'
- evidence_id: septin-root19-sources-PMID-8177173
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A8177173%20AND%20SRC%3AMED
  locator: Europe PMC exact PMID native metadata and complete abstract; source tier
    follows article type, no full-body inference.
  accessed_at: '2026-11-03T08:11:31.927691Z'
  support: supports
  summary: Gas vesicles. Bibliographic identity and abstract checked. Walsby is a
    secondary review; coarse morphology/function scope only.
  snapshot_sha256: a3f99e655b2a17b96df629f0fdfd02358a2d88a5b7a6ae8157e52887b338ccb7
  search_scope: 'Database www.ebi.ac.uk; exact endpoint https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A8177173%20AND%20SRC%3AMED;
    query parameters {''format'': [''json''], ''resultType'': [''core''], ''query'':
    [''EXT_ID:8177173 AND SRC:MED'']}; first returned response only, no date/publication
    restriction; accessed 2026-11-03T08:11:31.927691Z. Europe PMC pageSize25 default;
    exact PMID identity only. No exhaustive literature, ontology or biological absence
    conclusion.'
- evidence_id: septin-root19-sources-permeability1992-crossref
  kind: authority
  reference: https://api.crossref.org/works/10.1099/00221287-138-4-837
  locator: Native Crossref exact DOI/title/author/year/type metadata only; no body
    content.
  accessed_at: '2026-11-03T08:11:32.612713Z'
  support: supports
  summary: '[''The gas permeability coefficient of the cyanobacterial gas vesicle
    wall''] Article identity; abstract separately scoped.'
  snapshot_sha256: 70d372d8ad10f9d059a1bfc12614660bc8084a55d77246c31223e8fbd3148a28
- evidence_id: septin-parasporal-agent-crossref-book
  kind: authority
  reference: https://api.crossref.org/works/10.1007/978-94-011-5967-8_3
  locator: Native Crossref exact DOI/title/author/year/type metadata only; no body
    content.
  accessed_at: '2026-11-03T08:11:40.935763Z'
  support: supports
  summary: '[''Parasporal Body of Bacillus thuringiensis israelensis''] Publication
    identity only; chapter body not recovered.'
  snapshot_sha256: 01558c6de6e5579e984d5a310dc87718c1d2d5e2b39e6a45d0bc78bf06e417d1
- evidence_id: septin-parasporal-agent-insell1985-page56
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/c298/238573/264b7d322559/aem00142-0064.png
  locator: Fresh genuine native PMC238573 scan, printed page56, independently viewed
    and read with view_image; complete page text and included figures/captions.
  accessed_at: '2026-11-03T08:11:40.964177Z'
  support: supports
  summary: Insell/Fitz-James 1985 historical preparation, morphology, polypeptide
    fractionation and/or discussion at this page scope. Light/dark lattice classes
    and polypeptide bands do not identify modern Cry/Cyt accessions; no raw-image
    reanalysis.
  snapshot_sha256: 0a46d1881ce7121e60c3ec3afdfe2d9979334e096288205fc37d8d5ee91db53e
- evidence_id: septin-parasporal-agent-insell1985-page57
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/c298/238573/af3db6766abb/aem00142-0065.png
  locator: Fresh genuine native PMC238573 scan, printed page57, independently viewed
    and read with view_image; complete page text and included figures/captions.
  accessed_at: '2026-11-03T08:11:41.062335Z'
  support: supports
  summary: Insell/Fitz-James 1985 historical preparation, morphology, polypeptide
    fractionation and/or discussion at this page scope. Light/dark lattice classes
    and polypeptide bands do not identify modern Cry/Cyt accessions; no raw-image
    reanalysis.
  snapshot_sha256: 2ee46317de4caef8b5cb1f7f9f0977d6b2c9d6751fc22a2205ae84a8fdd57d48
- evidence_id: septin-parasporal-agent-insell1985-page58
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/c298/238573/031ad2528ec8/aem00142-0066.png
  locator: Fresh genuine native PMC238573 scan, printed page58, independently viewed
    and read with view_image; complete page text and included figures/captions.
  accessed_at: '2026-11-03T08:11:41.078797Z'
  support: supports
  summary: Insell/Fitz-James 1985 historical preparation, morphology, polypeptide
    fractionation and/or discussion at this page scope. Light/dark lattice classes
    and polypeptide bands do not identify modern Cry/Cyt accessions; no raw-image
    reanalysis.
  snapshot_sha256: 5fcf35d3c1bb5f4a4a64b7cd3f1a1c06e813a161a0631aa401b07a972bc5d857
- evidence_id: septin-parasporal-agent-insell1985-page59
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/c298/238573/fefc2292df2c/aem00142-0067.png
  locator: Fresh genuine native PMC238573 scan, printed page59, independently viewed
    and read with view_image; complete page text and included figures/captions.
  accessed_at: '2026-11-03T08:11:41.288319Z'
  support: supports
  summary: Insell/Fitz-James 1985 historical preparation, morphology, polypeptide
    fractionation and/or discussion at this page scope. Light/dark lattice classes
    and polypeptide bands do not identify modern Cry/Cyt accessions; no raw-image
    reanalysis.
  snapshot_sha256: 794f3d6385158b92cd746a77701dc383304493042db8fc73eb2e2e5739fab2a3
- evidence_id: septin-parasporal-agent-insell1985-page60
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/c298/238573/3ec6bf7d3e74/aem00142-0068.png
  locator: Fresh genuine native PMC238573 scan, printed page60, independently viewed
    and read with view_image; complete page text and included figures/captions.
  accessed_at: '2026-11-03T08:11:41.300741Z'
  support: supports
  summary: Insell/Fitz-James 1985 historical preparation, morphology, polypeptide
    fractionation and/or discussion at this page scope. Light/dark lattice classes
    and polypeptide bands do not identify modern Cry/Cyt accessions; no raw-image
    reanalysis.
  snapshot_sha256: 89916468925d307977beb792d45cc73b831af25e6d484d5cd03505159099fa58
- evidence_id: septin-parasporal-agent-insell1985-page61
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/c298/238573/07117471b85b/aem00142-0069.png
  locator: Fresh genuine native PMC238573 scan, printed page61, independently viewed
    and read with view_image; complete page text and included figures/captions.
  accessed_at: '2026-11-03T08:11:41.347232Z'
  support: supports
  summary: Insell/Fitz-James 1985 historical preparation, morphology, polypeptide
    fractionation and/or discussion at this page scope. Light/dark lattice classes
    and polypeptide bands do not identify modern Cry/Cyt accessions; no raw-image
    reanalysis.
  snapshot_sha256: 7cab38bd65a6e33e5f47a8b7e452d379bb006a67db5caac2813f85056e8e20e8
- evidence_id: septin-parasporal-agent-insell1985-page62
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/c298/238573/5eed4fa4bcd7/aem00142-0070.png
  locator: Fresh genuine native PMC238573 scan, printed page62, independently viewed
    and read with view_image; complete page text and included figures/captions.
  accessed_at: '2026-11-03T08:11:41.380759Z'
  support: supports
  summary: Insell/Fitz-James 1985 historical preparation, morphology, polypeptide
    fractionation and/or discussion at this page scope. Light/dark lattice classes
    and polypeptide bands do not identify modern Cry/Cyt accessions; no raw-image
    reanalysis.
  snapshot_sha256: 42f522497d5d19883a9e19a8343191c67583680e661ec7c419a1ea8e5eff1d04
- evidence_id: septin-permeability1992-browser-current
  kind: primary_source
  reference: https://www.microbiologyresearch.org/content/journal/micro/10.1099/00221287-138-4-837
  locator: Browser-indexed publisher title/authors and complete abstract lines48–52;
    declared crawl age5days. Full-text loader remains unrecovered. SHA256 identifies
    this saved derived observation receipt, not raw browser-page bytes.
  accessed_at: '2026-11-03T08:13:16.065986Z'
  support: supports
  summary: Oxygen microelectrode gradients across gas-vesicle and agar layers underpin
    diffusion-model estimates. Gas equilibration is rapid; vesicles do not actively
    store gas. No full Methods or raw data reanalysis.
  snapshot_sha256: b209f861d1a6aeddd8e8fcd1d4d29567e12138b09c3d645c6c7c6a2bb6567f25
- evidence_id: septin-wang2015-browser-current
  kind: authority
  reference: https://link.springer.com/article/10.1007/s00018-015-1903-5
  locator: Browser-indexed publisher title/author/type and complete abstract lines48–51;
    declared crawl age4months, subscription-body boundary. SHA256 identifies this
    saved derived observation receipt, not raw browser-page bytes.
  accessed_at: '2026-11-03T08:13:16.065986Z'
  support: supports
  summary: Secondary review concerns budding-yeast lipid-droplet storage and dynamics.
    The retrieved abstract does not directly expose the exact phospholipid-monolayer
    body passage; the coarse topology is assessed from independently fetched Graef/Grillitsch.
  snapshot_sha256: b209f861d1a6aeddd8e8fcd1d4d29567e12138b09c3d645c6c7c6a2bb6567f25
- evidence_id: septin-austin2006-browser-current
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1488921/
  locator: 'Browser-indexed PMC, declared crawl today: title/authors/DOI/PMID and
    complete Abstract lines96–101; opening Results and Figure1/2 captions lines117–139
    read as boundary context; no actual image pixels or raw tomograms viewed. SHA256
    identifies this saved derived observation receipt, not raw browser-page bytes.'
  accessed_at: '2026-11-03T08:23:00.085549Z'
  support: supports
  summary: Austin 2006 primary microscopy supports plastoglobule surface continuity
    with the stroma-side thylakoid leaflet in its studied plant context. This supports
    retaining the record boundary question, not automatically merging all lipid-body
    classes.
  snapshot_sha256: b209f861d1a6aeddd8e8fcd1d4d29567e12138b09c3d645c6c7c6a2bb6567f25
- evidence_id: septin-current-adapter-catalogue
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Fresh full official /api/datasets response, all 20 organism entries and
    28 dataset keys.
  accessed_at: '2026-11-03T08:11:41.587011Z'
  support: supports
  summary: E. coli/precise_mg1655 matches the aggresome experimental strain. No catalogue
    entry matches Anabaena cylindrica FACHB-318, Dolichospermum flos-aquae or B. thuringiensis/israelensis;
    B. subtilis and other cyanobacteria are not substituted. Broad bacterial/archaeal
    occurrence does not license unrelated gene queries.
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: septin-adapter-mg1655-meta
  kind: database
  reference: https://imodulondb.org/api/datasets/e_coli/precise_mg1655/meta
  locator: 'Fresh selected-dataset metadata: organism/dataset/strains, module/gene/sample
    counts and publication_url field.'
  accessed_at: '2026-11-03T08:12:29.290310Z'
  support: supports
  summary: MG1655 is the explicit strain; 115 modules and 4305 genes provide bounded
    expression context. Publication_url is null; no publication provenance is invented.
  snapshot_sha256: 0722bb1ccec69ac0d7ebc2784fc7cbdf1cfe612d739b8fb66d54a441a8b3db91
- evidence_id: septin-adapter-search-hslU
  kind: search
  reference: https://imodulondb.org/api/search?organism=e_coli&dataset=precise_mg1655&query=hslU&limit=50
  locator: Selected MG1655 gene search, q literal symbol and limit50; exact matching
    symbol selected among possible substring matches.
  accessed_at: '2026-11-03T08:12:29.290555Z'
  support: supports
  summary: Identity lookup for hslU only; no cross-species substitution or exhaustive
    absence inference.
  snapshot_sha256: ab596dbfdaac41ff5fd8ac1c608aee6df0911303b43e74c728f340d8d88350d6
  search_scope: 'Database imodulondb.org; exact endpoint https://imodulondb.org/api/search?organism=e_coli&dataset=precise_mg1655&query=hslU&limit=50;
    query parameters {''organism'': [''e_coli''], ''dataset'': [''precise_mg1655''],
    ''query'': [''hslU''], ''limit'': [''50'']}; first returned response only, no
    date/publication restriction; accessed 2026-11-03T08:12:29.290555Z. iModulonDB
    selected dataset precise_mg1655 only, q gene text and limit50; exact-symbol rows
    selected from returned matches. No exhaustive literature, ontology or biological
    absence conclusion.'
- evidence_id: septin-adapter-hslU-gene
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise_mg1655/b3931
  locator: 'Exact selected-dataset gene record: gene_id/name/product and imported
    UniProt ID; full function prose not used as structural evidence.'
  accessed_at: '2026-11-03T08:13:35.056199Z'
  support: supports
  summary: hslU resolves to b3931; this contextual gene identity does not make the
    gene a structural component or establish condensate necessity.
  snapshot_sha256: 33ef4e4f84949cd66315400f18288c9fa47b6a2e38b06aafc0baca4a2c830ce7
- evidence_id: septin-adapter-hslU-modules
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise_mg1655/b3931/imodulons
  locator: Complete returned 115 selected-dataset module rows; native is_in_imodulon
    flag, module ID/name, weights and thresholds.
  accessed_at: '2026-11-03T08:13:35.058561Z'
  support: supports
  summary: 'Positive flags for hslU: [(37, ''RpoH'')]. All-false rows where present
    are threshold outcomes, not biological absence, lack of regulation or absence
    from aggresomes.'
  snapshot_sha256: 75522a142cf459ddbe34d574cf677b3506d85e5e474e66e775d38099ecc38994
- evidence_id: septin-adapter-search-kbl
  kind: search
  reference: https://imodulondb.org/api/search?organism=e_coli&dataset=precise_mg1655&query=kbl&limit=50
  locator: Selected MG1655 gene search, q literal symbol and limit50; exact matching
    symbol selected among possible substring matches.
  accessed_at: '2026-11-03T08:12:29.290641Z'
  support: supports
  summary: Identity lookup for kbl only; no cross-species substitution or exhaustive
    absence inference.
  snapshot_sha256: ff8d5711d3aa9eb556f51a293cd76a468ce6a3ac177615bf66f2214a40065566
  search_scope: 'Database imodulondb.org; exact endpoint https://imodulondb.org/api/search?organism=e_coli&dataset=precise_mg1655&query=kbl&limit=50;
    query parameters {''organism'': [''e_coli''], ''dataset'': [''precise_mg1655''],
    ''query'': [''kbl''], ''limit'': [''50'']}; first returned response only, no date/publication
    restriction; accessed 2026-11-03T08:12:29.290641Z. iModulonDB selected dataset
    precise_mg1655 only, q gene text and limit50; exact-symbol rows selected from
    returned matches. No exhaustive literature, ontology or biological absence conclusion.'
- evidence_id: septin-adapter-kbl-gene
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise_mg1655/b3617
  locator: 'Exact selected-dataset gene record: gene_id/name/product and imported
    UniProt ID; full function prose not used as structural evidence.'
  accessed_at: '2026-11-03T08:13:35.073973Z'
  support: supports
  summary: kbl resolves to b3617; this contextual gene identity does not make the
    gene a structural component or establish condensate necessity.
  snapshot_sha256: cbd319e6b5ba51f7ba0095735c30ee365d8bf2160368a2ae3a8416aca4c9f391
- evidence_id: septin-adapter-kbl-modules
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise_mg1655/b3617/imodulons
  locator: Complete returned 115 selected-dataset module rows; native is_in_imodulon
    flag, module ID/name, weights and thresholds.
  accessed_at: '2026-11-03T08:13:35.074101Z'
  support: supports
  summary: 'Positive flags for kbl: [(78, ''Lrp-2'')]. All-false rows where present
    are threshold outcomes, not biological absence, lack of regulation or absence
    from aggresomes.'
  snapshot_sha256: fc280fb22cedf1c4f2f4a7e01281b7f336d751d71ff2882c74856caff51100c6
- evidence_id: septin-adapter-search-acnB
  kind: search
  reference: https://imodulondb.org/api/search?organism=e_coli&dataset=precise_mg1655&query=acnB&limit=50
  locator: Selected MG1655 gene search, q literal symbol and limit50; exact matching
    symbol selected among possible substring matches.
  accessed_at: '2026-11-03T08:12:29.290700Z'
  support: supports
  summary: Identity lookup for acnB only; no cross-species substitution or exhaustive
    absence inference.
  snapshot_sha256: 7149743b19151f2acfb6123bacc62348f8b24544bd70ae5ea3195056167e0f10
  search_scope: 'Database imodulondb.org; exact endpoint https://imodulondb.org/api/search?organism=e_coli&dataset=precise_mg1655&query=acnB&limit=50;
    query parameters {''organism'': [''e_coli''], ''dataset'': [''precise_mg1655''],
    ''query'': [''acnB''], ''limit'': [''50'']}; first returned response only, no
    date/publication restriction; accessed 2026-11-03T08:12:29.290700Z. iModulonDB
    selected dataset precise_mg1655 only, q gene text and limit50; exact-symbol rows
    selected from returned matches. No exhaustive literature, ontology or biological
    absence conclusion.'
- evidence_id: septin-adapter-acnB-gene
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise_mg1655/b0118
  locator: 'Exact selected-dataset gene record: gene_id/name/product and imported
    UniProt ID; full function prose not used as structural evidence.'
  accessed_at: '2026-11-03T08:13:34.879975Z'
  support: supports
  summary: acnB resolves to b0118; this contextual gene identity does not make the
    gene a structural component or establish condensate necessity.
  snapshot_sha256: 9b04ce199412c88350571f6e07363123163691f63ddb8a58024da7616df7f8e5
- evidence_id: septin-adapter-acnB-modules
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise_mg1655/b0118/imodulons
  locator: Complete returned 115 selected-dataset module rows; native is_in_imodulon
    flag, module ID/name, weights and thresholds.
  accessed_at: '2026-11-03T08:13:34.880242Z'
  support: supports
  summary: 'Positive flags for acnB: [(10, ''ArcA-2'')]. All-false rows where present
    are threshold outcomes, not biological absence, lack of regulation or absence
    from aggresomes.'
  snapshot_sha256: 57008f305e634d9a1e8653507435d9c47ddd930e4ee0403f8f9d4a8223bc29b2
- evidence_id: septin-adapter-search-nuoJ
  kind: search
  reference: https://imodulondb.org/api/search?organism=e_coli&dataset=precise_mg1655&query=nuoJ&limit=50
  locator: Selected MG1655 gene search, q literal symbol and limit50; exact matching
    symbol selected among possible substring matches.
  accessed_at: '2026-11-03T08:12:29.290745Z'
  support: supports
  summary: Identity lookup for nuoJ only; no cross-species substitution or exhaustive
    absence inference.
  snapshot_sha256: 1022e0a60f7a236c8d8b2db304bfc9ec452b5fb8833f3867b0f972c1754e102e
  search_scope: 'Database imodulondb.org; exact endpoint https://imodulondb.org/api/search?organism=e_coli&dataset=precise_mg1655&query=nuoJ&limit=50;
    query parameters {''organism'': [''e_coli''], ''dataset'': [''precise_mg1655''],
    ''query'': [''nuoJ''], ''limit'': [''50'']}; first returned response only, no
    date/publication restriction; accessed 2026-11-03T08:12:29.290745Z. iModulonDB
    selected dataset precise_mg1655 only, q gene text and limit50; exact-symbol rows
    selected from returned matches. No exhaustive literature, ontology or biological
    absence conclusion.'
- evidence_id: septin-adapter-nuoJ-gene
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise_mg1655/b2280
  locator: 'Exact selected-dataset gene record: gene_id/name/product and imported
    UniProt ID; full function prose not used as structural evidence.'
  accessed_at: '2026-11-03T08:13:35.117227Z'
  support: supports
  summary: nuoJ resolves to b2280; this contextual gene identity does not make the
    gene a structural component or establish condensate necessity.
  snapshot_sha256: 97971aea08dd07b7f000c46238c38ac075a8b39a2a774aeeb99ad6f6352dd560
- evidence_id: septin-adapter-nuoJ-modules
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise_mg1655/b2280/imodulons
  locator: Complete returned 115 selected-dataset module rows; native is_in_imodulon
    flag, module ID/name, weights and thresholds.
  accessed_at: '2026-11-03T08:13:35.121762Z'
  support: supports
  summary: 'Positive flags for nuoJ: [(31, ''UC-5'')]. All-false rows where present
    are threshold outcomes, not biological absence, lack of regulation or absence
    from aggresomes.'
  snapshot_sha256: fee1f8e04b3c2da73aa861b3f1a0f19da663776e4dd07654f601e91bf8e5dc78
- evidence_id: septin-adapter-search-nlpE
  kind: search
  reference: https://imodulondb.org/api/search?organism=e_coli&dataset=precise_mg1655&query=nlpE&limit=50
  locator: Selected MG1655 gene search, q literal symbol and limit50; exact matching
    symbol selected among possible substring matches.
  accessed_at: '2026-11-03T08:12:29.537456Z'
  support: supports
  summary: Identity lookup for nlpE only; no cross-species substitution or exhaustive
    absence inference.
  snapshot_sha256: 8703c5e260497cb4de575ad1c1ec1b9cf0ef00ef7fc88cfd204cbfde1ac9d644
  search_scope: 'Database imodulondb.org; exact endpoint https://imodulondb.org/api/search?organism=e_coli&dataset=precise_mg1655&query=nlpE&limit=50;
    query parameters {''organism'': [''e_coli''], ''dataset'': [''precise_mg1655''],
    ''query'': [''nlpE''], ''limit'': [''50'']}; first returned response only, no
    date/publication restriction; accessed 2026-11-03T08:12:29.537456Z. iModulonDB
    selected dataset precise_mg1655 only, q gene text and limit50; exact-symbol rows
    selected from returned matches. No exhaustive literature, ontology or biological
    absence conclusion.'
- evidence_id: septin-adapter-nlpE-gene
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise_mg1655/b0192
  locator: 'Exact selected-dataset gene record: gene_id/name/product and imported
    UniProt ID; full function prose not used as structural evidence.'
  accessed_at: '2026-11-03T08:13:35.108830Z'
  support: supports
  summary: nlpE resolves to b0192; this contextual gene identity does not make the
    gene a structural component or establish condensate necessity.
  snapshot_sha256: 8da47c62d5428a3686dd45824fb932b8c9930a10478794ec659fd088c728c88f
- evidence_id: septin-adapter-nlpE-modules
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise_mg1655/b0192/imodulons
  locator: Complete returned 115 selected-dataset module rows; native is_in_imodulon
    flag, module ID/name, weights and thresholds.
  accessed_at: '2026-11-03T08:13:35.110535Z'
  support: supports
  summary: 'Positive flags for nlpE: []. All-false rows where present are threshold
    outcomes, not biological absence, lack of regulation or absence from aggresomes.'
  snapshot_sha256: 82831290c9e5a7c5f3da699a50023c1c66c275dcdda72ba79aa8a850484977b7
- evidence_id: septin-adapter-search-glpK
  kind: search
  reference: https://imodulondb.org/api/search?organism=e_coli&dataset=precise_mg1655&query=glpK&limit=50
  locator: Selected MG1655 gene search, q literal symbol and limit50; exact matching
    symbol selected among possible substring matches.
  accessed_at: '2026-11-03T08:12:29.548213Z'
  support: supports
  summary: Identity lookup for glpK only; no cross-species substitution or exhaustive
    absence inference.
  snapshot_sha256: 80b3adbda2b998d26e32c4d6e3c91d89fc8fc996527320182918b8a1e238da12
  search_scope: 'Database imodulondb.org; exact endpoint https://imodulondb.org/api/search?organism=e_coli&dataset=precise_mg1655&query=glpK&limit=50;
    query parameters {''organism'': [''e_coli''], ''dataset'': [''precise_mg1655''],
    ''query'': [''glpK''], ''limit'': [''50'']}; first returned response only, no
    date/publication restriction; accessed 2026-11-03T08:12:29.548213Z. iModulonDB
    selected dataset precise_mg1655 only, q gene text and limit50; exact-symbol rows
    selected from returned matches. No exhaustive literature, ontology or biological
    absence conclusion.'
- evidence_id: septin-adapter-glpK-gene
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise_mg1655/b3926
  locator: 'Exact selected-dataset gene record: gene_id/name/product and imported
    UniProt ID; full function prose not used as structural evidence.'
  accessed_at: '2026-11-03T08:13:34.880330Z'
  support: supports
  summary: glpK resolves to b3926; this contextual gene identity does not make the
    gene a structural component or establish condensate necessity.
  snapshot_sha256: 4f8467aea0299e8c55c364817b1af587ca0db6492a0e7715772e1f2cf1c1d36f
- evidence_id: septin-adapter-glpK-modules
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise_mg1655/b3926/imodulons
  locator: Complete returned 115 selected-dataset module rows; native is_in_imodulon
    flag, module ID/name, weights and thresholds.
  accessed_at: '2026-11-03T08:13:34.880391Z'
  support: supports
  summary: 'Positive flags for glpK: [(66, ''Glycerol'')]. All-false rows where present
    are threshold outcomes, not biological absence, lack of regulation or absence
    from aggresomes.'
  snapshot_sha256: 6ba18af17bcab13cb4d6cf3d666834f37fdd817050a0616c313b5067c173fac3
- evidence_id: septin-adapter-search-mukF
  kind: search
  reference: https://imodulondb.org/api/search?organism=e_coli&dataset=precise_mg1655&query=mukF&limit=50
  locator: Selected MG1655 gene search, q literal symbol and limit50; exact matching
    symbol selected among possible substring matches.
  accessed_at: '2026-11-03T08:12:29.551082Z'
  support: supports
  summary: Identity lookup for mukF only; no cross-species substitution or exhaustive
    absence inference.
  snapshot_sha256: c58c230b6aa8f4fedec04ba878aa49dd9fc8faca2091447859c592cb33eb8117
  search_scope: 'Database imodulondb.org; exact endpoint https://imodulondb.org/api/search?organism=e_coli&dataset=precise_mg1655&query=mukF&limit=50;
    query parameters {''organism'': [''e_coli''], ''dataset'': [''precise_mg1655''],
    ''query'': [''mukF''], ''limit'': [''50'']}; first returned response only, no
    date/publication restriction; accessed 2026-11-03T08:12:29.551082Z. iModulonDB
    selected dataset precise_mg1655 only, q gene text and limit50; exact-symbol rows
    selected from returned matches. No exhaustive literature, ontology or biological
    absence conclusion.'
- evidence_id: septin-adapter-mukF-gene
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise_mg1655/b0922
  locator: 'Exact selected-dataset gene record: gene_id/name/product and imported
    UniProt ID; full function prose not used as structural evidence.'
  accessed_at: '2026-11-03T08:13:35.086026Z'
  support: supports
  summary: mukF resolves to b0922; this contextual gene identity does not make the
    gene a structural component or establish condensate necessity.
  snapshot_sha256: 60d26bf51da437247509956bee4dbae81d6d2fe6e83613d5721c9b3ed1d1ae30
- evidence_id: septin-adapter-mukF-modules
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise_mg1655/b0922/imodulons
  locator: Complete returned 115 selected-dataset module rows; native is_in_imodulon
    flag, module ID/name, weights and thresholds.
  accessed_at: '2026-11-03T08:13:35.097144Z'
  support: supports
  summary: 'Positive flags for mukF: []. All-false rows where present are threshold
    outcomes, not biological absence, lack of regulation or absence from aggresomes.'
  snapshot_sha256: 5147e52e3eb1df44afc3812fe6078618d3623109ffe25f6679d9bb4c178eeee5
- evidence_id: septin-adapter-search-rnb
  kind: search
  reference: https://imodulondb.org/api/search?organism=e_coli&dataset=precise_mg1655&query=rnb&limit=50
  locator: Selected MG1655 gene search, q literal symbol and limit50; exact matching
    symbol selected among possible substring matches.
  accessed_at: '2026-11-03T08:12:29.579044Z'
  support: supports
  summary: Identity lookup for rnb only; no cross-species substitution or exhaustive
    absence inference.
  snapshot_sha256: ca4aa244de6dc00413af30aa6d16b7b6c14b7804855e747a3bff3aa5870cbf35
  search_scope: 'Database imodulondb.org; exact endpoint https://imodulondb.org/api/search?organism=e_coli&dataset=precise_mg1655&query=rnb&limit=50;
    query parameters {''organism'': [''e_coli''], ''dataset'': [''precise_mg1655''],
    ''query'': [''rnb''], ''limit'': [''50'']}; first returned response only, no date/publication
    restriction; accessed 2026-11-03T08:12:29.579044Z. iModulonDB selected dataset
    precise_mg1655 only, q gene text and limit50; exact-symbol rows selected from
    returned matches. No exhaustive literature, ontology or biological absence conclusion.'
- evidence_id: septin-adapter-rnb-gene
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise_mg1655/b1286
  locator: 'Exact selected-dataset gene record: gene_id/name/product and imported
    UniProt ID; full function prose not used as structural evidence.'
  accessed_at: '2026-11-03T08:13:35.171033Z'
  support: supports
  summary: rnb resolves to b1286; this contextual gene identity does not make the
    gene a structural component or establish condensate necessity.
  snapshot_sha256: ebb9a9dc3ca097f1cfc8e753d2d056fee8a29b11a754d2abcb510a151f4ab0a2
- evidence_id: septin-adapter-rnb-modules
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise_mg1655/b1286/imodulons
  locator: Complete returned 115 selected-dataset module rows; native is_in_imodulon
    flag, module ID/name, weights and thresholds.
  accessed_at: '2026-11-03T08:13:35.182776Z'
  support: supports
  summary: 'Positive flags for rnb: []. All-false rows where present are threshold
    outcomes, not biological absence, lack of regulation or absence from aggresomes.'
  snapshot_sha256: 49b3140c4b9b820ab8e9cc7fe990c3a4ac30daac9ac7a5f210d628db4abf34b8
- evidence_id: septin-adapter-search-rbn
  kind: search
  reference: https://imodulondb.org/api/search?organism=e_coli&dataset=precise_mg1655&query=rbn&limit=50
  locator: Selected MG1655 gene search, q literal symbol and limit50; exact matching
    symbol selected among possible substring matches.
  accessed_at: '2026-11-03T08:12:29.615251Z'
  support: supports
  summary: Identity lookup for rbn only; no cross-species substitution or exhaustive
    absence inference.
  snapshot_sha256: 150b3e3e362016e9d5381e8249033df33dbc5aa93a6b04af47e59b943f3227b3
  search_scope: 'Database imodulondb.org; exact endpoint https://imodulondb.org/api/search?organism=e_coli&dataset=precise_mg1655&query=rbn&limit=50;
    query parameters {''organism'': [''e_coli''], ''dataset'': [''precise_mg1655''],
    ''query'': [''rbn''], ''limit'': [''50'']}; first returned response only, no date/publication
    restriction; accessed 2026-11-03T08:12:29.615251Z. iModulonDB selected dataset
    precise_mg1655 only, q gene text and limit50; exact-symbol rows selected from
    returned matches. No exhaustive literature, ontology or biological absence conclusion.'
- evidence_id: septin-adapter-rbn-gene
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise_mg1655/b2268
  locator: 'Exact selected-dataset gene record: gene_id/name/product and imported
    UniProt ID; full function prose not used as structural evidence.'
  accessed_at: '2026-11-03T08:13:35.151242Z'
  support: supports
  summary: rbn resolves to b2268; this contextual gene identity does not make the
    gene a structural component or establish condensate necessity.
  snapshot_sha256: 5ad99e72ed453a8f17074190a85b37cb9bbde1e5119b56845efd0db3f3824270
- evidence_id: septin-adapter-rbn-modules
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise_mg1655/b2268/imodulons
  locator: Complete returned 115 selected-dataset module rows; native is_in_imodulon
    flag, module ID/name, weights and thresholds.
  accessed_at: '2026-11-03T08:13:35.160638Z'
  support: supports
  summary: 'Positive flags for rbn: []. All-false rows where present are threshold
    outcomes, not biological absence, lack of regulation or absence from aggresomes.'
  snapshot_sha256: 7c158ebe1681bff1cce44ed1942059325290effb9f4dfba027241e17dde74d1b
- evidence_id: septin-adapter-search-orn
  kind: search
  reference: https://imodulondb.org/api/search?organism=e_coli&dataset=precise_mg1655&query=orn&limit=50
  locator: Selected MG1655 gene search, q literal symbol and limit50; exact matching
    symbol selected among possible substring matches.
  accessed_at: '2026-11-03T08:12:29.643880Z'
  support: supports
  summary: Identity lookup for orn only; no cross-species substitution or exhaustive
    absence inference.
  snapshot_sha256: 075d0f7173e058d674872be438246ad205615a84faf7f5918262745535f6027e
  search_scope: 'Database imodulondb.org; exact endpoint https://imodulondb.org/api/search?organism=e_coli&dataset=precise_mg1655&query=orn&limit=50;
    query parameters {''organism'': [''e_coli''], ''dataset'': [''precise_mg1655''],
    ''query'': [''orn''], ''limit'': [''50'']}; first returned response only, no date/publication
    restriction; accessed 2026-11-03T08:12:29.643880Z. iModulonDB selected dataset
    precise_mg1655 only, q gene text and limit50; exact-symbol rows selected from
    returned matches. No exhaustive literature, ontology or biological absence conclusion.'
- evidence_id: septin-adapter-orn-gene
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise_mg1655/b4162
  locator: 'Exact selected-dataset gene record: gene_id/name/product and imported
    UniProt ID; full function prose not used as structural evidence.'
  accessed_at: '2026-11-03T08:13:35.145963Z'
  support: supports
  summary: orn resolves to b4162; this contextual gene identity does not make the
    gene a structural component or establish condensate necessity.
  snapshot_sha256: 674e80326b71516e0f761f19f9e346b6739c9dc2468e29a6d90dfa0f400e943c
- evidence_id: septin-adapter-orn-modules
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise_mg1655/b4162/imodulons
  locator: Complete returned 115 selected-dataset module rows; native is_in_imodulon
    flag, module ID/name, weights and thresholds.
  accessed_at: '2026-11-03T08:13:35.148171Z'
  support: supports
  summary: 'Positive flags for orn: []. All-false rows where present are threshold
    outcomes, not biological absence, lack of regulation or absence from aggresomes.'
  snapshot_sha256: 0d3fffbd598b822b239ca28c444f3430f43144f09c22650b3f90e3143c8871a7
- evidence_id: septin-adapter-search-hokB
  kind: search
  reference: https://imodulondb.org/api/search?organism=e_coli&dataset=precise_mg1655&query=hokB&limit=50
  locator: Selected MG1655 gene search, q literal symbol and limit50; exact matching
    symbol selected among possible substring matches.
  accessed_at: '2026-11-03T08:12:29.643956Z'
  support: supports
  summary: Identity lookup for hokB only; no cross-species substitution or exhaustive
    absence inference.
  snapshot_sha256: e8768d4492ecc08089cda90e27eec707ef079fc94f63787c32d9d560dd1f4978
  search_scope: 'Database imodulondb.org; exact endpoint https://imodulondb.org/api/search?organism=e_coli&dataset=precise_mg1655&query=hokB&limit=50;
    query parameters {''organism'': [''e_coli''], ''dataset'': [''precise_mg1655''],
    ''query'': [''hokB''], ''limit'': [''50'']}; first returned response only, no
    date/publication restriction; accessed 2026-11-03T08:12:29.643956Z. iModulonDB
    selected dataset precise_mg1655 only, q gene text and limit50; exact-symbol rows
    selected from returned matches. No exhaustive literature, ontology or biological
    absence conclusion.'
- evidence_id: septin-adapter-hokB-gene
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise_mg1655/b4428
  locator: 'Exact selected-dataset gene record: gene_id/name/product and imported
    UniProt ID; full function prose not used as structural evidence.'
  accessed_at: '2026-11-03T08:13:34.880434Z'
  support: supports
  summary: hokB resolves to b4428; this contextual gene identity does not make the
    gene a structural component or establish condensate necessity.
  snapshot_sha256: 67bd567365c520ece9e514f251fb26ed78df28a21587a358325662e37129bdaf
- evidence_id: septin-adapter-hokB-modules
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise_mg1655/b4428/imodulons
  locator: Complete returned 115 selected-dataset module rows; native is_in_imodulon
    flag, module ID/name, weights and thresholds.
  accessed_at: '2026-11-03T08:13:35.053915Z'
  support: supports
  summary: 'Positive flags for hokB: [(112, ''ldrD'')]. All-false rows where present
    are threshold outcomes, not biological absence, lack of regulation or absence
    from aggresomes.'
  snapshot_sha256: fe21ea16c56c1882396d64a8438840eb9afaa1a4c2d2bfa98d0d8a9e6b57f666
- evidence_id: septin-adapter-module-10-detail
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise_mg1655/10
  locator: Exact selected module native name/regulator/function_description/category/threshold
    and n_genes; ai_summary and related generated fields excluded.
  accessed_at: '2026-11-03T08:16:31.573993Z'
  support: supports
  summary: 'Module10 ArcA-2: n_genes=37. Imported regulatory annotation is bounded
    expression context, not a causal or physical membership result.'
  snapshot_sha256: c93436092d97c6e9e35b5aa320317d8a59bd43977d73802cf629a307835a48b8
- evidence_id: septin-adapter-module-10-genes
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise_mg1655/10/genes
  locator: Exact module gene-membership endpoint, returned genes and threshold; named
    target rows cross-checked against gene-level flags.
  accessed_at: '2026-11-03T08:16:31.574263Z'
  support: supports
  summary: Cross-check rows [('b0118', 'acnB', True)]; no claims about unqueried datasets,
    stress-treatment activity or physical condensate recruitment.
  snapshot_sha256: 43864d57c4c320453f54af349354f3c8ceead86b1e53daa8eda067c5b5c7cc88
- evidence_id: septin-adapter-module-31-detail
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise_mg1655/31
  locator: Exact selected module native name/regulator/function_description/category/threshold
    and n_genes; ai_summary and related generated fields excluded.
  accessed_at: '2026-11-03T08:16:31.891378Z'
  support: supports
  summary: 'Module31 UC-5: n_genes=25. Imported regulatory annotation is bounded expression
    context, not a causal or physical membership result.'
  snapshot_sha256: 71a97a1941769bfeca9bf779d9185de0330d01394b32c92a870a8a31dca327fa
- evidence_id: septin-adapter-module-31-genes
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise_mg1655/31/genes
  locator: Exact module gene-membership endpoint, returned genes and threshold; named
    target rows cross-checked against gene-level flags.
  accessed_at: '2026-11-03T08:16:31.914050Z'
  support: supports
  summary: Cross-check rows [('b2280', 'nuoJ', True)]; no claims about unqueried datasets,
    stress-treatment activity or physical condensate recruitment.
  snapshot_sha256: 9f5332f26114d9324389ff5187abbbc041c93494a950999347143b8655ead8a1
- evidence_id: septin-adapter-module-37-detail
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise_mg1655/37
  locator: Exact selected module native name/regulator/function_description/category/threshold
    and n_genes; ai_summary and related generated fields excluded.
  accessed_at: '2026-11-03T08:16:31.826173Z'
  support: supports
  summary: 'Module37 RpoH: n_genes=18. Imported regulatory annotation is bounded expression
    context, not a causal or physical membership result.'
  snapshot_sha256: 74973a02a5119433cb1982dc035f5384701f1e2f711652583c91532748c6110f
- evidence_id: septin-adapter-module-37-genes
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise_mg1655/37/genes
  locator: Exact module gene-membership endpoint, returned genes and threshold; named
    target rows cross-checked against gene-level flags.
  accessed_at: '2026-11-03T08:16:31.828676Z'
  support: supports
  summary: Cross-check rows [('b3931', 'hslU', True)]; no claims about unqueried datasets,
    stress-treatment activity or physical condensate recruitment.
  snapshot_sha256: eb0fad939733e11bc84a92c7bb407e248743c641f82eb4fb23d35fe961193d7e
- evidence_id: septin-adapter-module-66-detail
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise_mg1655/66
  locator: Exact selected module native name/regulator/function_description/category/threshold
    and n_genes; ai_summary and related generated fields excluded.
  accessed_at: '2026-11-03T08:16:31.574349Z'
  support: supports
  summary: 'Module66 Glycerol: n_genes=8. Imported regulatory annotation is bounded
    expression context, not a causal or physical membership result.'
  snapshot_sha256: 4bce7778fa6fe428235c7c66629cbe4450b32f2f3f671dc37931d68b16e93f4a
- evidence_id: septin-adapter-module-66-genes
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise_mg1655/66/genes
  locator: Exact module gene-membership endpoint, returned genes and threshold; named
    target rows cross-checked against gene-level flags.
  accessed_at: '2026-11-03T08:16:31.574410Z'
  support: supports
  summary: Cross-check rows [('b3926', 'glpK', True)]; no claims about unqueried datasets,
    stress-treatment activity or physical condensate recruitment.
  snapshot_sha256: de2fe35100e2b0d79bad22e391a8afeaac58d259d18d2f4309a7425e723425a8
- evidence_id: septin-adapter-module-78-detail
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise_mg1655/78
  locator: Exact selected module native name/regulator/function_description/category/threshold
    and n_genes; ai_summary and related generated fields excluded.
  accessed_at: '2026-11-03T08:16:31.853303Z'
  support: supports
  summary: 'Module78 Lrp-2: n_genes=38. Imported regulatory annotation is bounded
    expression context, not a causal or physical membership result.'
  snapshot_sha256: 8e8af59af33149b72f5d242ff5a5935981e2399912ab84e7ac3a5f8db1c217c3
- evidence_id: septin-adapter-module-78-genes
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise_mg1655/78/genes
  locator: Exact module gene-membership endpoint, returned genes and threshold; named
    target rows cross-checked against gene-level flags.
  accessed_at: '2026-11-03T08:16:31.862438Z'
  support: supports
  summary: Cross-check rows [('b3617', 'kbl', True)]; no claims about unqueried datasets,
    stress-treatment activity or physical condensate recruitment.
  snapshot_sha256: e974b2bcb0d974287c0b3bd30973043688379a225f46cb07c3543cdc210f7c30
- evidence_id: septin-adapter-module-112-detail
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise_mg1655/112
  locator: Exact selected module native name/regulator/function_description/category/threshold
    and n_genes; ai_summary and related generated fields excluded.
  accessed_at: '2026-11-03T08:16:31.574452Z'
  support: supports
  summary: 'Module112 ldrD: n_genes=8. Imported regulatory annotation is bounded expression
    context, not a causal or physical membership result.'
  snapshot_sha256: 7e219f30819e84d3f3e031517e083fdf43be102259ec06cb4ec426ff0a8d73be
- evidence_id: septin-adapter-module-112-genes
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise_mg1655/112/genes
  locator: Exact module gene-membership endpoint, returned genes and threshold; named
    target rows cross-checked against gene-level flags.
  accessed_at: '2026-11-03T08:16:31.819099Z'
  support: supports
  summary: Cross-check rows [('b4428', 'hokB', True)]; no claims about unqueried datasets,
    stress-treatment activity or physical condensate recruitment.
  snapshot_sha256: e59b8e69389e78810e8662433026f41586345cc85b61fb53a74db4be9fd16a2c
- evidence_id: septin-direct-access-limits
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-septin/access-limitations.json
  locator: Actual direct retrieval attempts with their individual timestamps/statuses;
    SHA identifies aggregate receipt.
  accessed_at: '2026-11-03T08:23:11.026413Z'
  support: context_only
  summary: DOI-query HTTP503, publisher403 and challenge/redirect HTML are access
    limitations, not negative biological evidence. Successful JATS, accepted PDF,
    native scans, PMID and browser fallbacks have separate source scopes.
  snapshot_sha256: 059d12fea9e28205666bab40fa3c47125fb62b77b616f2417acaa9d7bf5f736f
- evidence_id: septin-historical-adapter-runner-unavailable
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical actual invocation 2026-11-03T00:49:00.848907Z–00:49:00.863225Z,
    exit1 PermissionError reading pyvenv.cfg; receipt reused, no current invocation.
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  summary: Native runner was unavailable at that earlier observation. Fresh official
    catalogue/API fallback is separately documented; this is not a successful new
    runner execution.
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: septin-native-review-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Frozen native component grounding, scientific-source, assembly-necessity
    and guarded-record contract; companion review process/profile/skills in context_inputs.
  accessed_at: '2026-11-03T08:23:11.026413Z'
  support: supports
  summary: Exact-family identity, source-scoped membership and formation necessity
    are distinct; structured-source fallback and issue-only review dispositions follow
    native policy.
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
- evidence_id: septin-context-gas_vesicle
  kind: record_content
  reference: data/structures/inclusion/gas_vesicle.yaml
  locator: 'Frozen boundary fields only: identifier/label/definition/kind/hierarchy/discussions
    and component IDs/labels/roles. No complete neighbor evidence/graph review.'
  accessed_at: '2026-11-03T08:23:11.026413Z'
  support: context_only
  summary: Boundary context for the assigned records only; no scientific re-review
    or terminal finding resolution of this neighbor.
  snapshot_sha256: 7bafef7a0ce0bc91ac7189ed216f4d2cdfc786cebbd47eeb5645c5408267f7cb
- evidence_id: septin-context-lipid_droplet
  kind: record_content
  reference: data/structures/inclusion/lipid_droplet.yaml
  locator: 'Frozen boundary fields only: identifier/label/definition/kind/hierarchy/discussions
    and component IDs/labels/roles. No complete neighbor evidence/graph review.'
  accessed_at: '2026-11-03T08:23:11.026413Z'
  support: context_only
  summary: Boundary context for the assigned records only; no scientific re-review
    or terminal finding resolution of this neighbor.
  snapshot_sha256: 379b5b516486c6bc55055e3289a565c7854b3088a5c13ebe6f614df5c1688a7a
- evidence_id: septin-context-plastoglobule
  kind: record_content
  reference: data/structures/inclusion/plastoglobule.yaml
  locator: 'Frozen boundary fields only: identifier/label/definition/kind/hierarchy/discussions
    and component IDs/labels/roles. No complete neighbor evidence/graph review.'
  accessed_at: '2026-11-03T08:23:11.026413Z'
  support: context_only
  summary: Boundary context for the assigned records only; no scientific re-review
    or terminal finding resolution of this neighbor.
  snapshot_sha256: ba5f8ac9dd4b54fefc917e1d6ed8587fdabdb2cf6152f1e331511bfc8ee38027
- evidence_id: septin-context-rnp_body
  kind: record_content
  reference: data/structures/ribonucleoprotein/rnp_body.yaml
  locator: 'Frozen boundary fields only: identifier/label/definition/kind/hierarchy/discussions
    and component IDs/labels/roles. No complete neighbor evidence/graph review.'
  accessed_at: '2026-11-03T08:23:11.026413Z'
  support: context_only
  summary: Boundary context for the assigned records only; no scientific re-review
    or terminal finding resolution of this neighbor.
  snapshot_sha256: cf7350e280e7e49db17d9218704f5190dbe6266f01aec01a7272e07f1e73637e
- evidence_id: septin-context-h_body
  kind: record_content
  reference: data/structures/ribonucleoprotein/h_body.yaml
  locator: 'Frozen boundary fields only: identifier/label/definition/kind/hierarchy/discussions
    and component IDs/labels/roles. No complete neighbor evidence/graph review.'
  accessed_at: '2026-11-03T08:23:11.026413Z'
  support: context_only
  summary: Boundary context for the assigned records only; no scientific re-review
    or terminal finding resolution of this neighbor.
  snapshot_sha256: 362c852cc05cb880426858ec3392ac9fc297ebe50e9fa6f818c01bf6c8a92b8a
- evidence_id: septin-gas-historical-reassessment
  kind: prior_review
  reference: reviews/structured/20261014T054100Z-gas-vesicle-finding-reassessment/review.yaml
  locator: Summary/assessments/findings/limitations and corresponding rendered narrative,
    whole-organelle target GO0031411 only.
  accessed_at: '2026-11-03T08:23:11.026413Z'
  support: context_only
  summary: Historical containment and GvpC essentiality allegations were rejected
    as unproven; conditional formation remained unknown and Bayro attribution was
    a different target finding. This shell review neither resolves nor reopens whole-organelle
    findings.
  snapshot_sha256: 029b6009a71f95bed1f267a5f2928550139311a16a8fcd353db3198194548f3a
- evidence_id: septin-record-bacterial_aggresome
  kind: record_content
  reference: data/structures/inclusion/bacterial_aggresome.yaml
  locator: Entire current maintained record including evidence, components/examples,
    functions/graphs, discussions and history; unchanged original target hash verified.
  accessed_at: '2026-11-03T08:23:11.026413Z'
  support: supports
  summary: Current source HEAD 7362758aca3756f5979304474ceb02a18f1a6ce6; byte-identical
    to the input frozen by the original review. Scientific reassessment still performed.
  snapshot_sha256: 8f6d6cf20835c5114b8c13bc929767a750bbb7b0db778799d7d1e1be387f8636
- evidence_id: septin-original-bacterial_aggresome
  kind: prior_review
  reference: reviews/structured/20261021T103320Z-bacterial-aggresome-audit/review.yaml
  locator: Entire immutable original bundle and corresponding Markdown; frozen input,
    source scopes, verdict, findings and native render checked.
  accessed_at: '2026-11-03T08:23:11.026413Z'
  support: context_only
  summary: Historical review preserved byte-for-byte; its scientific conclusions are
    independently reassessed rather than automatically accepted.
  snapshot_sha256: 254d75d004f0510ec0f43a69a701f4aa35b15880047163607b0d19494e1f7996
- evidence_id: septin-native-bacterial_aggresome-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/bacterial_aggresome.yaml
    --verify
  locator: Root-owned current source-head command; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/bacterial_aggresome-uniprot-verify-receipt.json;
    started 2026-11-03T08:11:04.716245+00:00, finished 2026-11-03T08:11:06.099199+00:00;
    SHA256 is inspected stdout log.
  accessed_at: '2026-11-03T08:11:06.099199Z'
  support: supports
  summary: Exit0; three concrete protein examples verified; causal inventory has zero
    GENE_OR_PROTEIN nodes, so RNase/transcript narrative was checked separately. Identity/coverage
    is distinct from assembly necessity or universal membership.
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: septin-native-bacterial_aggresome-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/bacterial_aggresome.yaml
    --causal-graphs
  locator: Root-owned current source-head command; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/bacterial_aggresome-uniprot-causal-receipt.json;
    started 2026-11-03T08:11:06.150434+00:00, finished 2026-11-03T08:11:06.572375+00:00;
    SHA256 is inspected stdout log.
  accessed_at: '2026-11-03T08:11:06.572375Z'
  support: supports
  summary: Exit0; three concrete protein examples verified; causal inventory has zero
    GENE_OR_PROTEIN nodes, so RNase/transcript narrative was checked separately. Identity/coverage
    is distinct from assembly necessity or universal membership.
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
- evidence_id: septin-record-gas_vesicle_shell
  kind: record_content
  reference: data/structures/inclusion/gas_vesicle_shell.yaml
  locator: Entire current maintained record including evidence, components/examples,
    functions/graphs, discussions and history; unchanged original target hash verified.
  accessed_at: '2026-11-03T08:23:11.026413Z'
  support: supports
  summary: Current source HEAD 7362758aca3756f5979304474ceb02a18f1a6ce6; byte-identical
    to the input frozen by the original review. Scientific reassessment still performed.
  snapshot_sha256: 06f0f2aa709e62b9e46e2e38d2ce26692fc0d8e0fe16a78d998aa7a51b1e0ae6
- evidence_id: septin-original-gas_vesicle_shell
  kind: prior_review
  reference: reviews/structured/20261021T103321Z-gas-vesicle-shell-audit/review.yaml
  locator: Entire immutable original bundle and corresponding Markdown; frozen input,
    source scopes, verdict, findings and native render checked.
  accessed_at: '2026-11-03T08:23:11.026413Z'
  support: context_only
  summary: Historical review preserved byte-for-byte; its scientific conclusions are
    independently reassessed rather than automatically accepted.
  snapshot_sha256: 8a3c1949e16327441cfbe13ad7d3a64dff05ffc7ac69d922bb037ba23e74d6de
- evidence_id: septin-native-gas_vesicle_shell-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/gas_vesicle_shell.yaml
    --verify
  locator: Root-owned current source-head command; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/gas_vesicle_shell-uniprot-verify-receipt.json;
    started 2026-11-03T08:11:06.603652+00:00, finished 2026-11-03T08:11:08.817842+00:00;
    SHA256 is inspected stdout log.
  accessed_at: '2026-11-03T08:11:08.817842Z'
  support: supports
  summary: Exit0; two concrete unreviewed examples verified; two covered GENE_OR_PROTEIN
    graph nodes. Identity/coverage is distinct from assembly necessity or universal
    membership.
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: septin-native-gas_vesicle_shell-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/gas_vesicle_shell.yaml
    --causal-graphs
  locator: Root-owned current source-head command; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/gas_vesicle_shell-uniprot-causal-receipt.json;
    started 2026-11-03T08:11:08.849436+00:00, finished 2026-11-03T08:11:09.230124+00:00;
    SHA256 is inspected stdout log.
  accessed_at: '2026-11-03T08:11:09.230124Z'
  support: supports
  summary: Exit0; two concrete unreviewed examples verified; two covered GENE_OR_PROTEIN
    graph nodes. Identity/coverage is distinct from assembly necessity or universal
    membership.
  snapshot_sha256: 9e7d806f0c580e411b6b49c7ec0d01ce5bbdcbd0a6d719d8e37be21bb7bcea18
- evidence_id: septin-record-monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer
  kind: record_content
  reference: data/structures/inclusion/monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer.yaml
  locator: Entire current maintained record including evidence, components/examples,
    functions/graphs, discussions and history; unchanged original target hash verified.
  accessed_at: '2026-11-03T08:23:11.026413Z'
  support: supports
  summary: Current source HEAD 7362758aca3756f5979304474ceb02a18f1a6ce6; byte-identical
    to the input frozen by the original review. Scientific reassessment still performed.
  snapshot_sha256: d72e9789b2d49d4fe380c06834e31dfe9eaf46fb6a412ddecdc9c8e1742b7a87
- evidence_id: septin-original-monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer
  kind: prior_review
  reference: reviews/structured/20261021T103325Z-monolayer-surrounded-lipid-storage-body-outer-lipid-monolayer-audit/review.yaml
  locator: Entire immutable original bundle and corresponding Markdown; frozen input,
    source scopes, verdict, findings and native render checked.
  accessed_at: '2026-11-03T08:23:11.026413Z'
  support: context_only
  summary: Historical review preserved byte-for-byte; its scientific conclusions are
    independently reassessed rather than automatically accepted.
  snapshot_sha256: 0d2d19504f3f536d33f212bb370ae2b880f6c6a5e46923e1c82c32706e5ca5d7
- evidence_id: septin-native-monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer.yaml
    --verify
  locator: Root-owned current source-head command; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer-uniprot-verify-receipt.json;
    started 2026-11-03T08:11:16.471749+00:00, finished 2026-11-03T08:11:16.977801+00:00;
    SHA256 is inspected stdout log.
  accessed_at: '2026-11-03T08:11:16.977801Z'
  support: supports
  summary: Exit0; empty protein-example and GENE_OR_PROTEIN inventories; this is not
    molecular identity coverage beyond the empty scope. Identity/coverage is distinct
    from assembly necessity or universal membership.
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: septin-native-monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer.yaml
    --causal-graphs
  locator: Root-owned current source-head command; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer-uniprot-causal-receipt.json;
    started 2026-11-03T08:11:17.013484+00:00, finished 2026-11-03T08:11:17.429037+00:00;
    SHA256 is inspected stdout log.
  accessed_at: '2026-11-03T08:11:17.429037Z'
  support: supports
  summary: Exit0; empty protein-example and GENE_OR_PROTEIN inventories; this is not
    molecular identity coverage beyond the empty scope. Identity/coverage is distinct
    from assembly necessity or universal membership.
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
- evidence_id: septin-record-parasporal_crystal
  kind: record_content
  reference: data/structures/inclusion/parasporal_crystal.yaml
  locator: Entire current maintained record including evidence, components/examples,
    functions/graphs, discussions and history; unchanged original target hash verified.
  accessed_at: '2026-11-03T08:23:11.026413Z'
  support: supports
  summary: Current source HEAD 7362758aca3756f5979304474ceb02a18f1a6ce6; byte-identical
    to the input frozen by the original review. Scientific reassessment still performed.
  snapshot_sha256: 59163a5ec708789816078e74a74e62fd9d3dbd38b580c40103a658e711274052
- evidence_id: septin-original-parasporal_crystal
  kind: prior_review
  reference: reviews/structured/20261021T103327Z-parasporal-crystal-audit/review.yaml
  locator: Entire immutable original bundle and corresponding Markdown; frozen input,
    source scopes, verdict, findings and native render checked.
  accessed_at: '2026-11-03T08:23:11.026413Z'
  support: context_only
  summary: Historical review preserved byte-for-byte; its scientific conclusions are
    independently reassessed rather than automatically accepted.
  snapshot_sha256: 9c244e37a631341163bfaa5ac5c5d254855a9be40845bf7345112bb11cc87a0b
- evidence_id: septin-native-parasporal_crystal-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/parasporal_crystal.yaml
    --verify
  locator: Root-owned current source-head command; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/parasporal_crystal-uniprot-verify-receipt.json;
    started 2026-11-03T08:11:19.174501+00:00, finished 2026-11-03T08:11:20.531706+00:00;
    SHA256 is inspected stdout log.
  accessed_at: '2026-11-03T08:11:20.531706Z'
  support: supports
  summary: Exit0; three concrete examples verified; one covered mixed-cohort GENE_OR_PROTEIN
    node. Identity/coverage is distinct from assembly necessity or universal membership.
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: septin-native-parasporal_crystal-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/parasporal_crystal.yaml
    --causal-graphs
  locator: Root-owned current source-head command; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/parasporal_crystal-uniprot-causal-receipt.json;
    started 2026-11-03T08:11:20.567108+00:00, finished 2026-11-03T08:11:20.967472+00:00;
    SHA256 is inspected stdout log.
  accessed_at: '2026-11-03T08:11:20.967472Z'
  support: supports
  summary: Exit0; three concrete examples verified; one covered mixed-cohort GENE_OR_PROTEIN
    node. Identity/coverage is distinct from assembly necessity or universal membership.
  snapshot_sha256: 69cfb3a226fb5fcc7a032ceda65d5c561bbbd37b36e82b8b517d7d7c300ae6dc
- evidence_id: septin-original-schema-render
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/adversary-septin/original-checks.json
  locator: Four assigned native validate/render checks with original timestamps; exact
    target/original YAML/Markdown hashes.
  accessed_at: '2026-11-03T08:23:11.026413Z'
  support: supports
  summary: All four native validations exit0 and rendered content exactly matches
    committed Markdown. All four target input hashes remain unchanged.
  snapshot_sha256: 3ea3c2a6f63e60e2cc4db85eb3069e9e3b972b64d683f5c876138546c796f427
- evidence_id: check-qc
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/qc.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T08:16:31.277529Z'
  support: supports
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  snapshot_sha256: 3100e4acea1b70b83d72b517d595af176644b0df02217362a8b63e9826dc8354
- evidence_id: check-labels
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/labels.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T08:11:43.087014Z'
  support: supports
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  snapshot_sha256: 6cdfb05df9a27194f05a5fd7f851783f817ac1523ca0bbfa54fe0e0d18775905
- evidence_id: check-trait-links
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/trait-links.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T08:11:22.406490Z'
  support: supports
  summary: Native TraitMech link check passed.
  snapshot_sha256: 8b336cdefbbd3daf6da8787990efdbe346c95e2c8361d50b7eb68a18f2d5a44a
- evidence_id: check-vendored
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/vendored.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T08:11:20.729443Z'
  support: supports
  summary: Pinned governed files match; native vendored check passed.
  snapshot_sha256: b1f169d103aaefa930745468bcca171e5867b9cc49e4e74311e458097e3252a6
- evidence_id: check-curies
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/curies.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T08:11:47.919304Z'
  support: supports
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  snapshot_sha256: fb3be251020aac118f6df680372ae7aaa32c2a1dd3366648cde95494f19d9dd2
- evidence_id: focused
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/focused-results.json
  locator: All twenty actual target schema/strict command outputs
  accessed_at: '2026-11-03T08:24:40Z'
  support: supports
  summary: Ten schema and ten strict commands returned exit zero.
  snapshot_sha256: ea8b9cdce53dd6606748133e799e8dde27402c0da38b193bcb3e41b8e49aadd2
- evidence_id: supplemental-pmid
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2356/pmid-chunks-receipt.json
  locator: Complete native-report PMID set checked with unchanged resolver in batches
    of at most fifty
  accessed_at: '2026-11-03T08:12:54.290005Z'
  support: supports
  summary: 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers
    remain unverified.
  snapshot_sha256: a31443cf19d9f615645d3353642b1c45a01dd54c9320498748963384f8bb19d9
- evidence_id: historical-adapter-runner-availability
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical runner invocation receipt, cross-checked against exact stdout/stderr
    hashes; reread during PR2356 synthesis
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  summary: Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS
    PermissionError reading the configured runner pyvenv.cfg. This is a retained historical
    availability observation, not a fresh attempt or a scientific validation failure.
    Native policy permits inspected source-catalogue fallback.
assessments:
- assessment_id: plaque-current-4-identity
  area: identity
  topic: Nuclear INQ identity and local mint
  outcome: supported
  summary: Nuclear-envelope-resolved primary evidence distinguishes INQ from cytoplasmic
    JUNQ. GO0016604/0016234 are appropriate broader parents and GO0005634 parthood;
    GO0097165 is not substituted. Exact OLS and bounded QuickGO queries did not return
    an exact INQ term.
  target_ids:
  - cellstructuremech:intranuclear_quality_control_compartment
  evidence_ids:
  - plaque-current-4
  - plaque-inq-go
  - plaque-inq-ols-exact
  - plaque-inq-go-search-0
  - plaque-inq-go-search-1
  - plaque-inq-miller2015-pmc
  - plaque-inq-sontag2023-jats
- assessment_id: plaque-current-4-cargo
  area: scope
  topic: Heterogeneous cargo and Cmr1 residency
  outcome: supported
  summary: Variable cargo is not a fixed complex. Gallina Fig3 and Mrc1 Results support
    Cmr1 as a stable conditionally recruited marker, not necessarily misfolded substrate,
    universal scaffold or universally required resident. The DISPENSABLE label is
    bounded to Mrc1-focus formation.
  target_ids:
  - cellstructuremech:intranuclear_quality_control_compartment
  evidence_ids:
  - plaque-current-4
  - plaque-inq-gallina2015-jats
- assessment_id: plaque-current-4-btn2
  area: evidence
  topic: Btn2 necessity and engineered rescue
  outcome: supported
  summary: Miller Fig6/7 support nuclear deposition, retained import when deposition
    fails, Btn2 enrichment and engineered Hsp42-NLS substitution. CONDITIONAL requirement
    is justified; native Hsp42 residence or universal essentiality is not inferred.
  target_ids:
  - cellstructuremech:intranuclear_quality_control_compartment
  evidence_ids:
  - plaque-current-4
  - plaque-inq-miller2015-pmc
- assessment_id: plaque-current-4-hsp104
  area: evidence
  topic: Hsp104 associated machinery
  outcome: supported
  summary: Miller Fig2 directly establishes nuclear Hsp104-marked deposits; main Results
    describe guanidinium-sensitive dissolution. Supplemental S6 pixels remain uninspected,
    as disclosed in the record; associated machinery and UNKNOWN assembly necessity
    are proportionate.
  target_ids:
  - cellstructuremech:intranuclear_quality_control_compartment
  evidence_ids:
  - plaque-current-4
  - plaque-inq-miller2015-pmc
- assessment_id: plaque-current-4-assembly
  area: graph
  topic: Stress and marker-specific assembly edges
  outcome: supported
  summary: All six assembly edges retain distinct NLS-LuciTs heat, Btn2 deletion/rescue
    and MMS/Cmr1 readouts. Gallina residual Cmr1-foci counts justify reduces, not
    universal loss; the Hsp42 genotoxic-stress result is not exported to every reporter
    assay.
  target_ids:
  - cellstructuremech:intranuclear_quality_control_compartment
  evidence_ids:
  - plaque-current-4
  - plaque-inq-miller2015-pmc
  - plaque-inq-gallina2015-jats
  - plaque-inq-sontag2023-jats
- assessment_id: plaque-current-4-clearance
  area: graph
  topic: Convergence and conditional clearance
  outcome: supported
  summary: 'Sontag S3/S6-S8 support all six graph edges: distinct inclusions converge
    across the envelope; NVJ and Vps4 perturbations impair reporter clearance; CHM7
    affects convergence in a subset. Molecular budding is a model and vacuolar routing
    is conditional.'
  target_ids:
  - cellstructuremech:intranuclear_quality_control_compartment
  evidence_ids:
  - plaque-current-4
  - plaque-inq-sontag2023-jats
- assessment_id: plaque-current-4-function
  area: scope
  topic: Cargo-dependent consequences
  outcome: supported
  summary: Miller reporter degradation persists without deposition, whereas Gallina
    reports Btn2-dependent Mrc1 turnover and Sontag shows reporter vacuolar clearance.
    The record preserves these assay differences and avoids a universal protective
    or degradation requirement.
  target_ids:
  - cellstructuremech:intranuclear_quality_control_compartment
  evidence_ids:
  - plaque-current-4
  - plaque-inq-miller2015-pmc
  - plaque-inq-gallina2015-jats
  - plaque-inq-sontag2023-jats
- assessment_id: plaque-current-4-examples
  area: scope
  topic: Experimental species and reference strain
  outcome: supported
  summary: Gallina methods distinguish RAD5 W303 defaults from S288C libraries/exceptions.
    Reviewed UniProt S288C examples remain reference sequences, not assignments of
    every experiment or image.
  target_ids:
  - cellstructuremech:intranuclear_quality_control_compartment
  evidence_ids:
  - plaque-current-4
  - plaque-inq-gallina2015-jats
  - plaque-inq-taxon-4932
  - plaque-inq-taxon-559292
  - plaque-inq-P53286
  - plaque-inq-P31539
  - plaque-inq-Q12510
- assessment_id: plaque-current-4-families
  area: grounding
  topic: Exact protein families versus domains
  outcome: supported
  summary: P53286 has only BTN2-like N-terminal domain IPR062150; P31539 has broader
    ClpA/B families; neither is overgrounded. Q12510 belongs to exact IPR050853 family.
    Native reviewed exact-gene queries support all three protein examples without
    borrowing generated mechanism text.
  target_ids:
  - cellstructuremech:intranuclear_quality_control_compartment
  evidence_ids:
  - plaque-current-4
  - plaque-inq-P53286
  - plaque-inq-P31539
  - plaque-inq-Q12510
  - plaque-inq-query-BTN2
  - plaque-inq-query-HSP104
  - plaque-inq-query-CMR1
  - plaque-inq-interpro-P53286
  - plaque-inq-interpro-P31539
  - plaque-inq-interpro-Q12510
  - plaque-inq-IPR050853
  - plaque-btn2-domain
- assessment_id: plaque-current-4-image
  area: evidence
  topic: Gallina Fig3 composite
  outcome: supported
  summary: Actual pixels show nuclear Cmr1/VHL overlap versus cytoplasmic VHL, partial
    Cct6 overlap and separate screen/blot panels. Caption scale2um, mixed assay context
    and whole-composite limitation agree with Fig3; exact local media MD5 and JATS
    CC BY4.0 match.
  target_ids:
  - cellstructuremech:intranuclear_quality_control_compartment
  evidence_ids:
  - plaque-current-4
  - plaque-image-4
  - plaque-inq-gallina2015-jats
  - plaque-inq-gallina2015-package
- assessment_id: plaque-current-5-identity
  area: identity
  topic: Cytoplasmic JUNQ boundary
  outcome: supported
  summary: Modern nuclear-envelope-resolved imaging supports cytoplasmic perinuclear
    JUNQ and congregation of Q-bodies. GO0016234 parent/GO0005737 parthood are appropriate;
    bounded exact OLS fullname/acronym queries support retaining the local mint without
    global absence claims.
  target_ids:
  - cellstructuremech:juxtanuclear_quality_control_compartment
  evidence_ids:
  - plaque-current-5
  - plaque-junq-go
  - plaque-junq-ols-exact-0
  - plaque-junq-ols-exact-1
  - plaque-inq-sontag2023-jats
- assessment_id: plaque-current-5-components
  area: evidence
  topic: Variable cargo and associated machinery
  outcome: supported
  summary: Sontag correlated Hsp104 imaging supports cytoplasmic association. Kaganovich
    proteasome association remains explicitly historical and generic GO0000502, not
    invariant26S composition or universal assembly necessity. Cargo is variable and
    reporter-defined.
  target_ids:
  - cellstructuremech:juxtanuclear_quality_control_compartment
  evidence_ids:
  - plaque-current-5
  - plaque-inq-sontag2023-jats
  - plaque-kaganovich-jats
  - plaque-junq-go
- assessment_id: plaque-current-5-sorting
  area: graph
  topic: Q-body and sequestrase sorting
  outcome: supported
  summary: 'All seven sorting edges agree with Sontag and Rolli: Q-bodies congregate;
    Ssa1/Ssa2 double deletion shifts to static peripheral deposits; Btn2 deletion
    shifts localization; Hsp42 deletion reduces peripheral foci without abolishing
    perinuclear deposits. Peripheral puncta are not all assumed IPOD.'
  target_ids:
  - cellstructuremech:juxtanuclear_quality_control_compartment
  evidence_ids:
  - plaque-current-5
  - plaque-inq-sontag2023-jats
  - plaque-junq-jats-PMC11372896
- assessment_id: plaque-current-5-positioning
  area: graph
  topic: Formation versus convergence
  outcome: supported
  summary: Sontag nuclear-pore clustering and CHM7/VPS23/VPS34/VPS15 perturbations
    support the qualified positioning graph. No direct physical tether or obligatory
    formation role is inferred. Rolli expression-limited Vps15/34 observations are
    not treated as contradictory mechanism evidence.
  target_ids:
  - cellstructuremech:juxtanuclear_quality_control_compartment
  evidence_ids:
  - plaque-current-5
  - plaque-inq-sontag2023-jats
  - plaque-junq-jats-PMC11372896
- assessment_id: plaque-current-5-clearance
  area: graph
  topic: JUNQ reporter clearance
  outcome: supported
  summary: Sontag NVJ/Vps4, cytoplasmic Keima and combined pep4/PMSF results and Rolli
    Atg1/Atg8 results support the clearance edges. NES-Keima fields are sampled, Fig8
    nuclear extrusion is not assigned to JUNQ, and proteasome contributions remain
    assay dependent.
  target_ids:
  - cellstructuremech:juxtanuclear_quality_control_compartment
  evidence_ids:
  - plaque-current-5
  - plaque-inq-sontag2023-jats
  - plaque-junq-jats-PMC11372896
- assessment_id: plaque-current-5-recoverable
  area: scope
  topic: Historical recoverable fluorescence pool
  outcome: supported
  summary: Kaganovich S6 observes diffuse Ubc9Ts fluorescence recovery after cooling
    and Hsp104/guanidine sensitivity. Record wording correctly avoids direct catalytic
    recovery, universal client refolding and complete retrospective reassignment of
    old JUNQ to modern cytoplasmic identity.
  target_ids:
  - cellstructuremech:juxtanuclear_quality_control_compartment
  evidence_ids:
  - plaque-current-5
  - plaque-kaganovich-jats
  - plaque-inq-sontag2023-jats
- assessment_id: plaque-current-5-proteins
  area: grounding
  topic: Reviewed Hsp104 example and broad family limits
  outcome: supported
  summary: Reviewed P31539 is S288C HSP104 and its complete11-match integrated set
    includes broader ClpA/B families, not an exact Hsp104-type identity. Reference
    accession does not substitute for the experimental BY4741 strain.
  target_ids:
  - cellstructuremech:juxtanuclear_quality_control_compartment
  evidence_ids:
  - plaque-current-5
  - plaque-inq-P31539
  - plaque-inq-query-HSP104
  - plaque-inq-interpro-P31539
  - plaque-junq-IPR001270
  - plaque-junq-IPR050130
- assessment_id: plaque-current-5-examples
  area: scope
  topic: BY4741 experiment versus S288C reference
  outcome: supported
  summary: Rolli Methods Table2 explicitly identifies BY4741 and derived mutants;
    native taxonomy resolves1247190. The 2023 species-level example does not invent
    a strain assignment from an unread supplemental table.
  target_ids:
  - cellstructuremech:juxtanuclear_quality_control_compartment
  evidence_ids:
  - plaque-current-5
  - plaque-junq-jats-PMC11372896
  - plaque-junq-tax-1247190
  - plaque-inq-taxon-4932
  - plaque-inq-taxon-559292
- assessment_id: plaque-current-5-image
  area: evidence
  topic: Rolli Fig2 pixel and caption scope
  outcome: supported
  summary: Inspected multi-panel pixels show WT and mutant spatial comparisons, peripheral
    double-mutant/HTT comparator photobleaching and separate blots. D-E are not positive
    WT JUNQ. Scale1um, nuclear-dye panel discrepancy and mitochondrial-method timing
    limitation are retained; MD5 and exact CC BY4.0 match.
  target_ids:
  - cellstructuremech:juxtanuclear_quality_control_compartment
  evidence_ids:
  - plaque-current-5
  - plaque-image-5
  - plaque-junq-jats-PMC11372896
  - plaque-junq-native-package-PMC11372896
- assessment_id: plaque-current-8-identity
  area: identity
  topic: GO0140602 and heat/starvation scope
  outcome: supported
  summary: Exact GO0140602 defines NuR peripheral inclusion; parent nuclear inclusion
    and nuclear parthood fit. Gallardo establishes acute-heat rings; Hiraoka Fig3
    supports peripheral starvation-associated redistribution without proving an identical
    heat mechanism.
  target_ids:
  - GO:0140602
  evidence_ids:
  - plaque-current-8
  - plaque-nur-go
  - plaque-gallardo-browser-retrieval
  - plaque-hiraoka-browser-retrieval
- assessment_id: plaque-current-8-cargo
  area: scope
  topic: Selective recruitment
  outcome: supported
  summary: Gallardo Figures1-2 distinguish recruited nuclear factors from unaffected
    pore proteins and central Gar2 material. Nup85/Mex67 are measured examples, not
    a full NPC or active RNA-export complex at NuRs.
  target_ids:
  - GO:0140602
  evidence_ids:
  - plaque-current-8
  - plaque-gallardo-browser-retrieval
- assessment_id: plaque-current-8-residence
  area: evidence
  topic: Chaperone residency and Mas5 requirement
  outcome: supported
  summary: Boronat Fig7 supports Ssa1/Ssa2/Mas5/Hsp104 recruitment and Mas5-dependent
    fission-yeast reporter rings. Separate single-label images are not simultaneous
    colocalization; family-wide necessity and transfer to budding yeast are excluded.
  target_ids:
  - GO:0140602
  evidence_ids:
  - plaque-current-8
  - plaque-nur-jats-PMC10342647
  - plaque-image-8
- assessment_id: plaque-current-8-assembly
  area: graph
  topic: Heat and preconditioning
  outcome: supported
  summary: Acute heat induces the tested rings; Mas5 loss blocks the specified reporters.
    Gallardo main text reports residual Ssa2 after preconditioning, supporting suppresses
    rather than absolute prevention. Supplements remain text-reported, not independently
    imaged.
  target_ids:
  - GO:0140602
  evidence_ids:
  - plaque-current-8
  - plaque-gallardo-browser-retrieval
  - plaque-nur-jats-PMC10342647
- assessment_id: plaque-current-8-recovery
  area: graph
  topic: Clearance and necessity
  outcome: supported
  summary: Gallardo Figures3-4 support recovery, delayed clearance after Hsp104 loss
    and repressed purg1-hsf1. Hsp104 is dispensable for assembly; Hsf1 regulation
    is not direct physical inclusion membership.
  target_ids:
  - GO:0140602
  evidence_ids:
  - plaque-current-8
  - plaque-gallardo-browser-retrieval
- assessment_id: plaque-current-8-function
  area: scope
  topic: Reversible sequestration versus protection model
  outcome: supported
  summary: Reduced Nup85/Mex67 mobility and recovery support sequestration. General
    shutdown/protection and regrowth correlations remain interpretations rather than
    an isolated NuR-only survival pathway.
  target_ids:
  - GO:0140602
  evidence_ids:
  - plaque-current-8
  - plaque-gallardo-browser-retrieval
- assessment_id: plaque-current-8-examples
  area: scope
  topic: Species and preparation boundaries
  outcome: supported
  summary: S.pombe acute heat is separate from Boronat budding-yeast W303/BY4741 tests;
    only W303 is concentrated50-fold. Native972h- protein-reference taxon does not
    fix every mutant genotype.
  target_ids:
  - GO:0140602
  evidence_ids:
  - plaque-current-8
  - plaque-nur-jats-PMC10342647
  - plaque-nur-tax-4896
  - plaque-inq-taxon-4932
  - plaque-nur-tax-284812
- assessment_id: plaque-current-8-proteins
  area: grounding
  topic: Six reviewed sequence examples
  outcome: supported
  summary: Q9UUE5/nup85, Q9Y8G3/mex67, Q10265/ssa1, O59855/ssa2, O74752/mas5 and O94641/hsp104
    each resolve as reviewed S.pombe284812 examples; exact reviewed gene/taxon searches
    return the declared accession. Identity alone does not support residence.
  target_ids:
  - GO:0140602
  evidence_ids:
  - plaque-current-8
  - plaque-nur-Q9UUE5
  - plaque-nur-Q9Y8G3
  - plaque-nur-Q10265
  - plaque-nur-O59855
  - plaque-nur-O74752
  - plaque-nur-O94641
  - plaque-nur-query-nup85
  - plaque-nur-query-mex67
  - plaque-nur-query-ssa1
  - plaque-nur-query-ssa2
  - plaque-nur-query-mas5
  - plaque-nur-query-hsp104
- assessment_id: plaque-current-8-families
  area: grounding
  topic: Family identities and current transport limitation
  outcome: supported
  summary: Integrated lists through next=null support Nup85 IPR011502, Mex67 IPR030217,
    both Ssa IPR013126 and Mas5 IPR044713. Direct Hsp70-family endpoint429 is disclosed;
    successful exact-protein match metadata independently verifies its name/type.
    Hsp104 broad ClpA/B hits are not adopted as exact identity.
  target_ids:
  - GO:0140602
  evidence_ids:
  - plaque-current-8
  - plaque-nur-matches-Q9UUE5
  - plaque-nur-matches-Q9Y8G3
  - plaque-nur-matches-Q10265
  - plaque-nur-matches-O59855
  - plaque-nur-matches-O74752
  - plaque-nur-matches-O94641
  - plaque-nur-IPR011502
  - plaque-nur-IPR030217
  - plaque-nur-IPR044713
  - plaque-junq-IPR001270
  - plaque-junq-IPR050130
  - plaque-source-access-limitations
- assessment_id: plaque-current-8-image
  area: evidence
  topic: Boronat Fig7 mixed-species composite
  outcome: supported
  summary: Pixels show S.pombe and budding-yeast reporter panels, separate chaperone
    localizations, a Mas5 deletion control and schematic. Figure caption scale5um
    and15min42C agree; taxon4896 is scoped to panelb/lefta and W303 concentration
    is retained. Exact media MD5 and CC BY4.0 match.
  target_ids:
  - GO:0140602
  evidence_ids:
  - plaque-current-8
  - plaque-image-8
  - plaque-nur-jats-PMC10342647
  - plaque-nur-native-package-PMC10342647
- assessment_id: plaque-current-4-schema
  area: schema
  topic: Original artifact and current protein gates
  outcome: supported
  summary: Original native validation and exact render pass; all historical source
    input hashes match. Current root-run verify/causal receipts independently checked.
    No scientific finding occurred in the original; no historical curation closure
    is claimed.
  target_ids:
  - cellstructuremech:intranuclear_quality_control_compartment
  evidence_ids:
  - plaque-current-4
  - plaque-original-4
  - plaque-original-validation
  - plaque-native-intranuclear_quality_control_compartment-verify
  - plaque-native-intranuclear_quality_control_compartment-causal
- assessment_id: plaque-current-4-adapter
  area: provenance
  topic: Current structured-source applicability
  outcome: supported
  summary: Named proteins and stress-response perturbations trigger coverage assessment.
    Fresh complete catalogue lacks both represented yeast genera, so downstream organism-matched
    gene/module queries are not applicable. Historical runner failure remains separate;
    this is a source-fallback check, not a fresh runner success or biological negative
    result.
  target_ids:
  - cellstructuremech:intranuclear_quality_control_compartment
  evidence_ids:
  - plaque-current-4
  - plaque-native-review-policy
  - plaque-catalogue
- assessment_id: plaque-current-5-schema
  area: schema
  topic: Original artifact and current protein gates
  outcome: supported
  summary: Original native validation and exact render pass; all historical source
    input hashes match. Current root-run verify/causal receipts independently checked.
    No scientific finding occurred in the original; no historical curation closure
    is claimed.
  target_ids:
  - cellstructuremech:juxtanuclear_quality_control_compartment
  evidence_ids:
  - plaque-current-5
  - plaque-original-5
  - plaque-original-validation
  - plaque-native-juxtanuclear_quality_control_compartment-verify
  - plaque-native-juxtanuclear_quality_control_compartment-causal
- assessment_id: plaque-current-5-adapter
  area: provenance
  topic: Current structured-source applicability
  outcome: supported
  summary: Named proteins and stress-response perturbations trigger coverage assessment.
    Fresh complete catalogue lacks both represented yeast genera, so downstream organism-matched
    gene/module queries are not applicable. Historical runner failure remains separate;
    this is a source-fallback check, not a fresh runner success or biological negative
    result.
  target_ids:
  - cellstructuremech:juxtanuclear_quality_control_compartment
  evidence_ids:
  - plaque-current-5
  - plaque-native-review-policy
  - plaque-catalogue
- assessment_id: plaque-current-8-schema
  area: schema
  topic: Original artifact and current protein gates
  outcome: supported
  summary: Original native validation and exact render pass; all historical source
    input hashes match. Current root-run verify/causal receipts independently checked.
    No scientific finding occurred in the original; no historical curation closure
    is claimed.
  target_ids:
  - GO:0140602
  evidence_ids:
  - plaque-current-8
  - plaque-original-8
  - plaque-original-validation
  - plaque-native-nucleolar_peripheral_inclusion_body-verify
  - plaque-native-nucleolar_peripheral_inclusion_body-causal
- assessment_id: plaque-current-8-adapter
  area: provenance
  topic: Current structured-source applicability
  outcome: supported
  summary: Named proteins and stress-response perturbations trigger coverage assessment.
    Fresh complete catalogue lacks both represented yeast genera, so downstream organism-matched
    gene/module queries are not applicable. Historical runner failure remains separate;
    this is a source-fallback check, not a fresh runner success or biological negative
    result.
  target_ids:
  - GO:0140602
  evidence_ids:
  - plaque-current-8
  - plaque-native-review-policy
  - plaque-catalogue
- assessment_id: micro-age_associated_protein_deposit-1
  area: identity
  topic: Local identity and spatial boundary
  outcome: supported
  target_ids:
  - cellstructuremech:age_associated_protein_deposit
  summary: INCLUSION/INCLUSION_BODY with local identity and broader GO inclusion-body
    parent is coherent. Agepod/APOD nomenclature is bounded. ER association does not
    justify exclusive cytoplasmic parthood because the 2017 source observed an intranuclear
    subset.
  evidence_ids:
  - micro-record-age_associated_protein_deposit
  - micro-go
  - micro-go-query-Agepod
  - micro-go-query-APOD
  - micro-go-query-age-associated_protein_deposit
  - micro-age2015-primary
  - micro-age2017-primary
  - micro-age2018-secondary-nomenclature
- assessment_id: micro-age_associated_protein_deposit-2
  area: scope
  topic: Source strains and occurrence
  outcome: supported
  target_ids:
  - cellstructuremech:age_associated_protein_deposit
  summary: Canonical species4932, explicit S288C/W303 2015 context and BY4741 2025
    context are distinguished from seven reviewed S288C reference proteins. Conditional
    aging occurrence does not imply a structure in every young cell or every yeast
    lineage.
  evidence_ids:
  - micro-record-age_associated_protein_deposit
  - micro-tax-4932
  - micro-tax-559292
  - micro-tax-1247190
  - micro-age2015-primary
  - micro-age2017-primary
  - micro-age2025-primary
- assessment_id: micro-age_associated_protein_deposit-3
  area: grounding
  topic: Protein identities and family coverage
  outcome: supported
  target_ids:
  - cellstructuremech:age_associated_protein_deposit
  summary: Seven examples resolve to HSP42/HSP26/HSP104/SSA1/SSA2/YDJ1/SUP35. Declared
    IPR031107/013126/003285 families cover their examples; broad ClpA/B and DnaJ family
    matches are retained as broader alternatives, not fabricated exact Hsp104/Ydj1-specific
    groundings.
  evidence_ids:
  - micro-record-age_associated_protein_deposit
  - micro-uniprot-Q12329
  - micro-uniprot-P15992
  - micro-uniprot-P31539
  - micro-uniprot-P10591
  - micro-uniprot-P10592
  - micro-uniprot-P25491
  - micro-uniprot-P05453
  - micro-matches-Q12329
  - micro-matches-P15992
  - micro-matches-P31539
  - micro-matches-P10591
  - micro-matches-P10592
  - micro-matches-P25491
  - micro-matches-P05453
  - micro-family-IPR031107
  - micro-family-IPR013126
  - micro-family-IPR003285
  - micro-family-IPR001270
  - micro-family-IPR050130
- assessment_id: micro-age_associated_protein_deposit-4
  area: evidence
  topic: Formation necessity versus associated cargo
  outcome: supported
  target_ids:
  - cellstructuremech:age_associated_protein_deposit
  summary: Hsp42 formation dependence does not confer the same requirement on Hsp26.
    Hsp104 is dispensable for deposit formation under tested conditions; Hsp70 family-wide
    necessity remains UNKNOWN despite separate SSA1/SSA2 effects. Ydj1 enrichment
    is uncommon and context-dependent; Sup35 association is prion-state-dependent
    cargo, not obligatory initiation.
  evidence_ids:
  - micro-record-age_associated_protein_deposit
  - micro-age2015-primary
  - micro-age2017-primary
- assessment_id: micro-age_associated_protein_deposit-5
  area: graph
  topic: Chaperone and fusion graph direction
  outcome: supported
  target_ids:
  - cellstructuremech:age_associated_protein_deposit
  summary: The graph correctly distinguishes HSP42 loss/OE and HSP104 loss/OE directions,
    separate SSA1/SSA2 mutations, mating deposit merger and PRM3 perturbation of ER/nuclear
    fusion. Perturbations are experimental factors, not invented resident complexes.
  evidence_ids:
  - micro-record-age_associated_protein_deposit
  - micro-age2015-primary
  - micro-age2017-primary
- assessment_id: micro-age_associated_protein_deposit-6
  area: graph
  topic: Lineage and precursor confinement graph
  outcome: supported
  target_ids:
  - cellstructuremech:age_associated_protein_deposit
  summary: BUD1/SUR2/BUD6 and YDJ1-C406S effects distinguish new daughter deposit
    formation from transfer of pre-existing deposits. Bud6 actin confounding and preserved
    mature-deposit retention/ER association after C406S are explicit. FCS/FLIP and
    epistasis support a proposed confinement model without identifying direct clients.
  evidence_ids:
  - micro-record-age_associated_protein_deposit
  - micro-age2017-primary
- assessment_id: micro-age_associated_protein_deposit-7
  area: graph
  topic: TOR and disappearance graph scope
  outcome: supported
  target_ids:
  - cellstructuremech:age_associated_protein_deposit
  summary: NPR3/TCO89 aging effects are separated from acute pro3-1 screening. Young
    rapamycin/cycloheximide foci loss and old-cell resistance are source-supported
    but not equated to direct proteolysis. The internal source cycloheximide-dose
    discrepancy remains explicit.
  evidence_ids:
  - micro-record-age_associated_protein_deposit
  - micro-age2025-primary
- assessment_id: micro-age_associated_protein_deposit-8
  area: provenance
  topic: Figure and evidence provenance
  outcome: supported
  target_ids:
  - cellstructuremech:age_associated_protein_deposit
  summary: Tracked Figure6 pixels/caption/CC BY attribution agree with the fresh primary
    package. The 2018 review is limited to nomenclature; quantitative figure annotations
    do not establish universal prevalence or composition.
  evidence_ids:
  - micro-record-age_associated_protein_deposit
  - micro-image-age_associated_protein_deposit
  - micro-image-package-age_associated_protein_deposit
  - micro-age2015-primary
  - micro-age2018-secondary-nomenclature
- assessment_id: micro-insoluble_protein_deposit-1
  area: identity
  topic: IPOD identity, location and neighboring compartments
  outcome: supported
  target_ids:
  - cellstructuremech:insoluble_protein_deposit
  summary: Local inclusion identity, IPOD acronym, cytoplasmic parthood and broader
    GO inclusion parent are appropriate. Perivacuolar IPOD remains distinct from JUNQ/INQ
    and adjacent PAS; an ontology name search is bounded, not universal absence proof.
  evidence_ids:
  - micro-record-insoluble_protein_deposit
  - micro-go
  - micro-go-query-IPOD
  - micro-go-query-insoluble_protein_deposit
  - micro-ipod2008-primary
  - micro-ipod2016-primary
- assessment_id: micro-insoluble_protein_deposit-2
  area: grounding
  topic: Cargo versus disaggregase component
  outcome: supported
  target_ids:
  - cellstructuremech:insoluble_protein_deposit
  summary: Heterogeneous aggregate cargo remains label-only OTHER and engineered PrD-GFP
    is not misrepresented as a universal full-length native subunit. Hsp104P31539
    resolves; broad ClpA/B entries are not exact Hsp104-specific groundings. UNKNOWN
    formation necessity is compatible with postformation inhibition and persistence.
  evidence_ids:
  - micro-record-insoluble_protein_deposit
  - micro-uniprot-P31539
  - micro-query-HSP104
  - micro-matches-P31539
  - micro-family-IPR001270
  - micro-family-IPR050130
  - micro-ipod2016-primary
- assessment_id: micro-insoluble_protein_deposit-3
  area: scope
  topic: Species and experimental strains
  outcome: supported
  target_ids:
  - cellstructuremech:insoluble_protein_deposit
  summary: Yeast species4932 is supported by74D-694-derived recruitment/oxidative-stress
    assays; S288C559292 is a reference-protein identity, not an asserted experimental
    background for those assays.
  evidence_ids:
  - micro-record-insoluble_protein_deposit
  - micro-tax-4932
  - micro-tax-559292
  - micro-ipod2016-primary
  - micro-ipod2024-primary
- assessment_id: micro-insoluble_protein_deposit-4
  area: graph
  topic: Recruitment versus structural maintenance
  outcome: supported
  target_ids:
  - cellstructuremech:insoluble_protein_deposit
  summary: Myo2/tropomyosin/Sec18 depletion and recovery support recruitment/coalescence,
    while preformed deposits persist after depletion. Proposed vesicular/tethering
    transport is distinguished from proof of resident transport-factor components
    or direct fusion of a particular vesicle.
  evidence_ids:
  - micro-record-insoluble_protein_deposit
  - micro-ipod2016-primary
- assessment_id: micro-insoluble_protein_deposit-5
  area: graph
  topic: Cargo release and downstream turnover
  outcome: supported
  target_ids:
  - cellstructuremech:insoluble_protein_deposit
  summary: Guanidinium inhibition after deposit formation and MG132 experiments support
    Hsp104-dependent extraction and a partial proteasomal contribution. The record
    does not claim complete bulk autophagy, exclusive proteasomal disposal or universal
    irreversible storage. The2008Ubc9ts recovery assay and2016PrD-GFP slow turnover
    assay are distinct.
  evidence_ids:
  - micro-record-insoluble_protein_deposit
  - micro-ipod2008-primary
  - micro-ipod2016-primary
- assessment_id: micro-insoluble_protein_deposit-6
  area: evidence
  topic: Prion-formation counterexample
  outcome: supported
  target_ids:
  - cellstructuremech:insoluble_protein_deposit
  summary: ABP1-deletion behavior is explicitly restricted to0.8mM peroxide/one-hour
    and wild-type versus btn2 hsp42 genetic contexts. This supports the discussion
    against universal IPOD necessity without inventing universal IPOD independence.
  evidence_ids:
  - micro-record-insoluble_protein_deposit
  - micro-ipod2024-primary
- assessment_id: micro-insoluble_protein_deposit-7
  area: provenance
  topic: Tracked recruitment figure provenance
  outcome: supported
  target_ids:
  - cellstructuremech:insoluble_protein_deposit
  summary: Figure3A–F pixels/caption/scale/CC BY attribution agree with fresh package
    bytes. No original time-lapse movie or raw quantification was reanalyzed.
  evidence_ids:
  - micro-record-insoluble_protein_deposit
  - micro-image-insoluble_protein_deposit
  - micro-image-package-insoluble_protein_deposit
  - micro-ipod2016-primary
- assessment_id: micro-mitostore-1
  area: identity
  topic: MitoStore identity and spatial distinction
  outcome: supported
  target_ids:
  - cellstructuremech:mitostore
  summary: Local INCLUSION_BODY identity denotes cytosolic precursor granules associated
    with the mitochondrial surface, not matrix granules or a membrane-enclosed organelle.
    Neither broad protein aggregate center nor heat-induced Tom70 aggregates are asserted
    as exact synonyms.
  evidence_ids:
  - micro-record-mitostore
  - micro-go
  - micro-go-query-MitoStore
  - micro-go-query-MitoStores
  - micro-mitostore2023-primary
  - micro-mitostore-tom70-comparison
- assessment_id: micro-mitostore-2
  area: grounding
  topic: Components, identities and conditional necessity
  outcome: supported
  target_ids:
  - cellstructuremech:mitostore
  summary: HSP42Q12329/HSP26P15992 share valid small-HSP familyIPR031107; HSP104P31539
    remains exact with broader family unassigned. Hsp26 co-purification does not establish
    necessity or direct localization. Separate HSP42/HSP104 deletions support the
    tested Aim17 formation requirement, not a universal fixed coat or full native
    inventory.
  evidence_ids:
  - micro-record-mitostore
  - micro-uniprot-Q12329
  - micro-uniprot-P15992
  - micro-uniprot-P31539
  - micro-matches-Q12329
  - micro-matches-P15992
  - micro-matches-P31539
  - micro-family-IPR031107
  - micro-mitostore2023-primary
- assessment_id: micro-mitostore-3
  area: scope
  topic: Yeast strain and conditional occurrence
  outcome: supported
  target_ids:
  - cellstructuremech:mitostore
  summary: YPH499-derived experiments and canonical species4932 are separated from
    S288C reference-protein identities. Lactate-growth basal granules, clogger induction
    and glucose/stationary-phase context are not generalized to constitutive occurrence
    in all yeast.
  evidence_ids:
  - micro-record-mitostore
  - micro-tax-4932
  - micro-tax-559292
  - micro-mitostore2023-primary
- assessment_id: micro-mitostore-4
  area: graph
  topic: Precursor assembly graph
  outcome: supported
  target_ids:
  - cellstructuremech:mitostore
  summary: Clogger-induced precursor accumulation, chaperone deletion and Mam33 presequence
    truncation have the stated condition-specific directions. Heterogeneous precursor-cargo
    nodes are appropriate; reporters are not automatically fixed constituent subunits.
  evidence_ids:
  - micro-record-mitostore
  - micro-mitostore2023-primary
- assessment_id: micro-mitostore-5
  area: graph
  topic: Recovery and survival graph
  outcome: supported
  target_ids:
  - cellstructuremech:mitostore
  summary: 4.5h loading followed by4h chase/split-GFP supports renewed matrix import
    competence, without single-molecule tracing from an individual granule. RPN4 deletion/chaperone-dependent
    survival after24h clogger expression remains condition-specific and does not isolate
    granule-only causality.
  evidence_ids:
  - micro-record-mitostore
  - micro-mitostore2023-primary
- assessment_id: micro-mitostore-6
  area: provenance
  topic: Proteomics provenance and archive inconsistency
  outcome: supported
  target_ids:
  - cellstructuremech:mitostore
  summary: PXD035762 is cited through the paper as Hsp104 AP-MS provenance. Current
    metadata mismatch to the Ubc8 reference and2920-versus1154 filtered proteins is
    already documented. No raw-data reanalysis, complete native inventory or corrected
    archive bibliography is claimed; this is an explicit source limitation, not a
    new untracked record error.
  evidence_ids:
  - micro-record-mitostore
  - micro-pride-mitostore
  - micro-mitostore2023-primary
- assessment_id: micro-mitostore-7
  area: provenance
  topic: Tracked image and comparison-source scope
  outcome: supported
  target_ids:
  - cellstructuremech:mitostore
  summary: Figure5 pixels, panel-specific scales, caption, primary attribution/license
    and media checksum agree. Tom70 heat-stress comparisons remain similarities without
    identity/necessity transfer. No LLPS mechanism is promoted from these observations.
  evidence_ids:
  - micro-record-mitostore
  - micro-image-mitostore
  - micro-image-package-mitostore
  - micro-mitostore2023-primary
  - micro-mitostore-tom70-comparison
- assessment_id: micro-age_associated_protein_deposit-9
  area: evidence
  topic: Structured source applicability after actual catalogue inspection
  outcome: supported
  target_ids:
  - cellstructuremech:age_associated_protein_deposit
  summary: Named yeast protein/stress claims trigger applicability review. Fresh iModulonDB
    catalogue has no matching Saccharomyces organism/dataset, so downstream module/gene/activity
    checks are N/A within that inspected catalogue. Historical runner unavailability
    is explicitly dated; absence from the catalogue is not negative biological evidence.
    The original absent applicability coverage is repaired.
  evidence_ids:
  - micro-record-age_associated_protein_deposit
  - micro-adapter-catalogue
  - micro-historical-adapter-runner
  - micro-review-policy
  - micro-review-config
  - micro-prior-age_associated_protein_deposit
- assessment_id: micro-age_associated_protein_deposit-10
  area: schema
  topic: Native protein inventory verification limits
  outcome: supported
  target_ids:
  - cellstructuremech:age_associated_protein_deposit
  summary: Seven examples passed, but the causal scan has zero GENE_OR_PROTEIN nodes;
    it does not validate every experimental factor.
  evidence_ids:
  - micro-record-age_associated_protein_deposit
  - micro-native-age_associated_protein_deposit-verify
  - micro-native-age_associated_protein_deposit-causal
- assessment_id: micro-age_associated_protein_deposit-11
  area: provenance
  topic: Frozen inputs, staleness and original lineage
  outcome: supported
  target_ids:
  - cellstructuremech:age_associated_protein_deposit
  summary: Original validation/render passed and no scientific findings were present.
    Target bytes remain identical to the original frozen input. No category-wide or
    unrelated issue resolution is claimed.
  evidence_ids:
  - micro-record-age_associated_protein_deposit
  - micro-prior-age_associated_protein_deposit
  - micro-original-validation-inputs
- assessment_id: micro-age_associated_protein_deposit-12
  area: completeness
  topic: Scientific verdict and bounded completeness
  outcome: supported
  target_ids:
  - cellstructuremech:age_associated_protein_deposit
  summary: Current whole-record assessment remains pass_with_limitations, with no
    confirmed record-curation finding or curation action. Existing discussions retain
    uncertain complete composition, experimental context and source limits. Passing
    schema/identifier checks is not treated as proof of all biological claims.
  evidence_ids:
  - micro-record-age_associated_protein_deposit
  - micro-prior-age_associated_protein_deposit
  - micro-age2015-primary
  - micro-age2017-primary
  - micro-age2025-primary
- assessment_id: micro-insoluble_protein_deposit-8
  area: evidence
  topic: Structured source applicability after actual catalogue inspection
  outcome: supported
  target_ids:
  - cellstructuremech:insoluble_protein_deposit
  summary: Named yeast protein/stress claims trigger applicability review. Fresh iModulonDB
    catalogue has no matching Saccharomyces organism/dataset, so downstream module/gene/activity
    checks are N/A within that inspected catalogue. Historical runner unavailability
    is explicitly dated; absence from the catalogue is not negative biological evidence.
    The original no-expression-claim exemption is replaced by an evidenced catalogue-based
    conclusion.
  evidence_ids:
  - micro-record-insoluble_protein_deposit
  - micro-adapter-catalogue
  - micro-historical-adapter-runner
  - micro-review-policy
  - micro-review-config
  - micro-prior-insoluble_protein_deposit
- assessment_id: micro-insoluble_protein_deposit-9
  area: schema
  topic: Native protein inventory verification limits
  outcome: supported
  target_ids:
  - cellstructuremech:insoluble_protein_deposit
  summary: One example passed; graph scan reports one COVERED and one NO_GENE_SYMBOLS
    heterogeneous cargo node, without dangling references.
  evidence_ids:
  - micro-record-insoluble_protein_deposit
  - micro-native-insoluble_protein_deposit-verify
  - micro-native-insoluble_protein_deposit-causal
- assessment_id: micro-insoluble_protein_deposit-10
  area: provenance
  topic: Frozen inputs, staleness and original lineage
  outcome: supported
  target_ids:
  - cellstructuremech:insoluble_protein_deposit
  summary: Original validation/render passed and no scientific findings were present.
    Current record differs by two exact self-identity node groundings plus history;
    both new groundings were reassessed and accepted. Current evidence refreshes the
    stale assessment without rewriting the original source hashes. No category-wide
    or unrelated issue resolution is claimed.
  evidence_ids:
  - micro-record-insoluble_protein_deposit
  - micro-prior-insoluble_protein_deposit
  - micro-original-validation-inputs
- assessment_id: micro-insoluble_protein_deposit-11
  area: completeness
  topic: Scientific verdict and bounded completeness
  outcome: supported
  target_ids:
  - cellstructuremech:insoluble_protein_deposit
  summary: Current whole-record assessment remains pass_with_limitations, with no
    confirmed record-curation finding or curation action. Existing discussions retain
    uncertain complete composition, experimental context and source limits. Passing
    schema/identifier checks is not treated as proof of all biological claims.
  evidence_ids:
  - micro-record-insoluble_protein_deposit
  - micro-prior-insoluble_protein_deposit
  - micro-ipod2008-primary
  - micro-ipod2016-primary
  - micro-ipod2024-primary
- assessment_id: micro-mitostore-8
  area: evidence
  topic: Structured source applicability after actual catalogue inspection
  outcome: supported
  target_ids:
  - cellstructuremech:mitostore
  summary: Named yeast protein/stress claims trigger applicability review. Fresh iModulonDB
    catalogue has no matching Saccharomyces organism/dataset, so downstream module/gene/activity
    checks are N/A within that inspected catalogue. Historical runner unavailability
    is explicitly dated; absence from the catalogue is not negative biological evidence.
    The original absent applicability coverage is repaired.
  evidence_ids:
  - micro-record-mitostore
  - micro-adapter-catalogue
  - micro-historical-adapter-runner
  - micro-review-policy
  - micro-review-config
  - micro-prior-mitostore
- assessment_id: micro-mitostore-9
  area: schema
  topic: Native protein inventory verification limits
  outcome: supported
  target_ids:
  - cellstructuremech:mitostore
  summary: Three examples passed; graph scan reports two NO_GENE_SYMBOLS heterogeneous
    precursor-cargo nodes, without dangling references.
  evidence_ids:
  - micro-record-mitostore
  - micro-native-mitostore-verify
  - micro-native-mitostore-causal
- assessment_id: micro-mitostore-10
  area: provenance
  topic: Frozen inputs, staleness and original lineage
  outcome: supported
  target_ids:
  - cellstructuremech:mitostore
  summary: Original validation/render passed and no scientific findings were present.
    Current record differs by two exact self-identity node groundings plus history;
    both new groundings were reassessed and accepted. Current evidence refreshes the
    stale assessment without rewriting the original source hashes. No category-wide
    or unrelated issue resolution is claimed.
  evidence_ids:
  - micro-record-mitostore
  - micro-prior-mitostore
  - micro-original-validation-inputs
- assessment_id: micro-mitostore-11
  area: completeness
  topic: Scientific verdict and bounded completeness
  outcome: supported
  target_ids:
  - cellstructuremech:mitostore
  summary: Current whole-record assessment remains pass_with_limitations, with no
    confirmed record-curation finding or curation action. Existing discussions retain
    uncertain complete composition, experimental context and source limits. Passing
    schema/identifier checks is not treated as proof of all biological claims.
  evidence_ids:
  - micro-record-mitostore
  - micro-prior-mitostore
  - micro-mitostore2023-primary
  - micro-pride-mitostore
  - micro-mitostore-tom70-comparison
- assessment_id: septin-bacterial_aggresome-identity
  area: identity
  topic: Bacterial inclusion identity and neighboring condensates
  outcome: supported
  summary: The local proposed bacterial structure is compatible with inclusion-body
    parent and cytoplasmic parthood. GO0016235 requires dynein-dependent microtubule
    transport and is not an exact identity. RNaseE BR-bodies and Hfq H-bodies remain
    distinct boundary records.
  target_ids:
  - cellstructuremech:bacterial_aggresome
  evidence_ids:
  - septin-record-bacterial_aggresome
  - septin-aggresome-agent-go
  - septin-aggresome-agent-PMC8528417
  - septin-aggresome-agent-pei2025-aam
  - septin-context-rnp_body
  - septin-context-h_body
- assessment_id: septin-bacterial_aggresome-components
  area: completeness
  topic: Observed constituent subset
  outcome: supported
  summary: HslU, Kbl and AcnB are experimentally observed markers with different recruitment
    timing; selected mRNAs are enriched. This is a supported subset, not a complete
    or fixed condensate proteome. Upstream HokB and excluded wild-type RNases are
    correctly contextual rather than automatic constituents.
  target_ids:
  - cellstructuremech:bacterial_aggresome
  evidence_ids:
  - septin-aggresome-agent-PMC8528417
  - septin-aggresome-agent-pei2025-aam
  - septin-record-bacterial_aggresome
- assessment_id: septin-bacterial_aggresome-grounding
  area: grounding
  topic: Exact molecular identities and family scope
  outcome: supported
  summary: HslU IPR004491/P0A6H5, Kbl IPR011282/P0AB77, AcnB IPR004406/P36683 and
    mRNA SO0000234 match their declared scopes. K-12 concrete examples are distinct
    from the explicitly experimental MG1655 strain.
  target_ids:
  - cellstructuremech:bacterial_aggresome
  evidence_ids:
  - septin-aggresome-agent-so
  - septin-aggresome-agent-IPR004491
  - septin-aggresome-agent-IPR011282
  - septin-aggresome-agent-IPR004406
  - septin-aggresome-agent-P0A6H5
  - septin-aggresome-agent-P0AB77
  - septin-aggresome-agent-P36683
  - septin-aggresome-agent-reviewed-uniqueness
- assessment_id: septin-bacterial_aggresome-necessity
  area: evidence
  topic: Formation necessity remains unresolved
  outcome: unknown
  summary: Observed enrichment and reporter localization do not establish that every
    listed constituent is required to form the structure. UNKNOWN necessity is retained;
    charge-mutant RNase perturbations test RNA protection, not a universal minimal
    composition.
  target_ids:
  - cellstructuremech:bacterial_aggresome
  evidence_ids:
  - septin-record-bacterial_aggresome
  - septin-aggresome-agent-PMC8528417
  - septin-aggresome-agent-pei2025-aam
- assessment_id: septin-bacterial_aggresome-scope
  area: scope
  topic: Experimental strain and stress-state boundaries
  outcome: supported
  summary: The primary experiments and taxon authorities support the scoped E. coli/MG1655
    examples. Neither the local generic label nor the tested liquid-like behavior
    asserts universal bacterial prevalence, identical dynamics or every aggregated
    inclusion.
  target_ids:
  - cellstructuremech:bacterial_aggresome
  evidence_ids:
  - septin-aggresome-agent-tax-83333
  - septin-aggresome-agent-tax-511145
  - septin-aggresome-agent-PMC8528417
  - septin-aggresome-agent-pei2025-aam
- assessment_id: septin-bacterial_aggresome-mechanism
  area: evidence
  topic: RNase exclusion, transcript preservation and recovery graph
  outcome: supported
  summary: 'All six recorded edges preserve the tested sequence: selected RNA recruitment,
    exclusion of tested RNases, protection, stress-release and translation recovery.
    Active RNB-MO entry/depletion is distinguished from inactive ME variants; RNA
    itself as the repulsive agent remains proposed. Rifampicin/tetracycline controls
    bound the recovery interpretation, and the graph avoids a universal fitness or
    persistence conclusion.'
  target_ids:
  - cellstructuremech:bacterial_aggresome
  evidence_ids:
  - septin-record-bacterial_aggresome
  - septin-aggresome-agent-pei2025-aam
- assessment_id: septin-bacterial_aggresome-structured
  area: scope
  topic: Matched structured-source context and its limits
  outcome: supported
  summary: The molecular policy applies. Fresh official MG1655 metadata, eleven exact
    gene lookups, all115 module flags per gene and six positive-module membership
    cross-checks were inspected. Positives are hslU/RpoH, kbl/Lrp-2, acnB/ArcA-2,
    glpK/Glycerol, nuoJ/UC-5 and hokB/ldrD. mukF/nlpE/rnb/rbn/orn have all-false flags
    in this dataset; these are threshold results, never absence. No condition-specific
    activity analysis or condensate recruitment is inferred.
  target_ids:
  - cellstructuremech:bacterial_aggresome
  evidence_ids:
  - septin-current-adapter-catalogue
  - septin-adapter-mg1655-meta
  - septin-adapter-hslU-modules
  - septin-adapter-kbl-modules
  - septin-adapter-acnB-modules
  - septin-adapter-nuoJ-modules
  - septin-adapter-nlpE-modules
  - septin-adapter-glpK-modules
  - septin-adapter-mukF-modules
  - septin-adapter-rnb-modules
  - septin-adapter-rbn-modules
  - septin-adapter-orn-modules
  - septin-adapter-hokB-modules
  - septin-adapter-module-10-genes
  - septin-adapter-module-31-genes
  - septin-adapter-module-37-genes
  - septin-adapter-module-66-genes
  - septin-adapter-module-78-genes
  - septin-adapter-module-112-genes
- assessment_id: septin-bacterial_aggresome-native
  area: schema
  topic: Native verification and original bundle integrity
  outcome: supported
  summary: Current concrete protein identity checks pass; zero typed protein graph
    nodes is an empty causal inventory, not independent validation of all narrative
    RNases/transcripts. Original schema/render and target frozen hash pass; the missing
    original applicability assessment is an in-scope bundle correction.
  target_ids:
  - cellstructuremech:bacterial_aggresome
  evidence_ids:
  - septin-native-bacterial_aggresome-verify
  - septin-native-bacterial_aggresome-causal
  - septin-original-schema-render
  - septin-original-bacterial_aggresome
  - septin-record-bacterial_aggresome
- assessment_id: septin-gas_vesicle_shell-identity
  area: identity
  topic: Shell material and whole organelle boundary
  outcome: supported
  summary: GO0033172 exactly denotes the protein wall; parthood to GO0031411 and the
    related membrane synonym do not make it a lipid bilayer. Whole-organelle accessory
    assembly and historical findings remain context only.
  target_ids:
  - GO:0033172
  evidence_ids:
  - septin-root19-sources-gas-shell-go
  - septin-record-gas_vesicle_shell
  - septin-context-gas_vesicle
  - septin-gas-historical-reassessment
- assessment_id: septin-gas_vesicle_shell-components
  area: evidence
  topic: GvpA ribs and exterior GvpC
  outcome: supported
  summary: Dutka and Bayro support the GvpA polymer wall; primary stripping/rebinding
    evidence and structural comparison support exterior GvpC strengthening. Accessory
    assembly proteins are not automatically persistent shell constituents. No exhaustive
    minor-component inventory is asserted.
  target_ids:
  - GO:0033172
  evidence_ids:
  - septin-root19-sources-jats-PMC10185304
  - septin-root19-sources-legacy-PMC3271001
  - septin-root19-sources-PMID-1510555
  - septin-record-gas_vesicle_shell
- assessment_id: septin-gas_vesicle_shell-grounding
  area: grounding
  topic: Available exact GvpA family
  outcome: concern
  summary: 'Original F1 remains confirmed: IPR047870 is an exact GvpA family and is
    present on the recorded accession; the component still lacks grounding. PF00741/IPR000638
    is broader GvpA-like scope. GvpC repeat entries are not exact whole-protein identities.'
  target_ids:
  - GO:0033172
  evidence_ids:
  - septin-root19-sources-IPR047870
  - septin-root19-sources-IPR000638
  - septin-root19-sources-PF00741
  - septin-root19-sources-UniProtKB-A0ABR7ZBW9
  - septin-root19-sources-IPR002003
  - septin-root19-sources-PF01304
  - septin-record-gas_vesicle_shell
- assessment_id: septin-gas_vesicle_shell-necessity
  area: evidence
  topic: GvpC conditional formation requirement
  outcome: unknown
  summary: GvpA is the wall scaffold. Stripping/rebinding changes the strength of
    already formed shells; neither that experiment nor an unassessed formation context
    proves or refutes every conditional GvpC assembly requirement. This is an explicit
    unresolved check, not a new contradictory finding or a resolution of whole-organelle
    historical claims.
  target_ids:
  - GO:0033172
  evidence_ids:
  - septin-root19-sources-PMID-1510555
  - septin-root19-sources-jats-PMC10185304
  - septin-gas-historical-reassessment
  - septin-record-gas_vesicle_shell
- assessment_id: septin-gas_vesicle_shell-scope
  area: scope
  topic: Variable occurrence and distinct strain examples
  outcome: supported
  summary: Broad bacterial/archaeal variable occurrence is supported at review scope.
    The native structural preparation names Dolichospermum flos-aquae1403/13F; the
    two concrete protein examples instead identify Anabaena cylindrica FACHB-318 and
    remain unreviewed. These strains are not conflated.
  target_ids:
  - GO:0033172
  evidence_ids:
  - septin-root19-sources-PMID-8177173
  - septin-root19-sources-jats-PMC10185304
  - septin-root19-sources-NCBITaxon-315271
  - septin-root19-sources-NCBITaxon-2692880
  - septin-root19-sources-UniProtKB-A0ABR7ZBW9
  - septin-root19-sources-UniProtKB-A0ABR7ZCB1
- assessment_id: septin-gas_vesicle_shell-graph
  area: evidence
  topic: Ribs, reinforcement and gas-filled interior
  outcome: supported
  summary: The graph separates GvpA polymerization, shell formation, exterior reinforcement
    and buoyancy-supporting gas space. Gas permeability and liquid-water exclusion
    are source-supported at stated primary/abstract scopes; no active gas storage,
    species-universal pressure threshold or complete initiation mechanism is implied.
  target_ids:
  - GO:0033172
  evidence_ids:
  - septin-record-gas_vesicle_shell
  - septin-root19-sources-jats-PMC10185304
  - septin-root19-sources-legacy-PMC3271001
  - septin-root19-sources-PMID-8177173
  - septin-permeability1992-browser-current
- assessment_id: septin-gas_vesicle_shell-structured
  area: scope
  topic: Applicability assessed by native source coverage
  outcome: supported
  summary: Named GvpA/GvpC claims trigger applicability assessment; the original no-transcriptomic-inference
    rationale is insufficient. The fresh catalogue has no matching native source taxon/strain
    dataset. Unrelated cyanobacteria and heterologous E. coli contexts are not proxies
    for these shell proteins, so no unmatched gene query is invented.
  target_ids:
  - GO:0033172
  evidence_ids:
  - septin-record-gas_vesicle_shell
  - septin-original-gas_vesicle_shell
  - septin-current-adapter-catalogue
  - septin-historical-adapter-runner-unavailable
- assessment_id: septin-gas_vesicle_shell-native
  area: schema
  topic: Protein checks, original bundle and finding lineage
  outcome: supported
  summary: Both current concrete examples verify and both protein graph nodes are
    covered. Original validation/render and unchanged input hash pass. F1 remains
    curation, while the applicability rationale is fixed only in the successor bundle.
  target_ids:
  - GO:0033172
  evidence_ids:
  - septin-native-gas_vesicle_shell-verify
  - septin-native-gas_vesicle_shell-causal
  - septin-original-schema-render
  - septin-original-gas_vesicle_shell
- assessment_id: septin-monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer-identity
  area: identity
  topic: Monolayer identity versus storage organelle
  outcome: supported
  summary: GO0034430 and its synonym types denote the single surface layer, distinct
    from the whole lipid droplet. Parthood and membrane kind agree with the scoped
    mature topology; an imported oil-body synonym does not certify all possible taxa
    or plastoglobule equivalence.
  target_ids:
  - GO:0034430
  evidence_ids:
  - septin-root19-sources-lipid-monolayer-go
  - septin-record-monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer
  - septin-context-lipid_droplet
  - septin-context-plastoglobule
- assessment_id: septin-monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer-material
  area: grounding
  topic: Class-level phospholipid material
  outcome: supported
  summary: CHEBI16247 matches the phospholipid class. Associated proteins belong to
    the explicit whole-organelle context and are not automatically members of the
    lipid layer. No particular lipid species or universal protein coat is required
    by this record.
  target_ids:
  - GO:0034430
  evidence_ids:
  - septin-root19-sources-CHEBI-16247
  - septin-root19-sources-jats-PMC3229976
  - septin-root19-sources-jats-PMC5947121
  - septin-record-monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer
- assessment_id: septin-monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer-necessity
  area: evidence
  topic: Material requirement versus individual species
  outcome: supported
  summary: ESSENTIAL applies to the defining collective phospholipid layer; it does
    not promote individual phospholipid species to indispensable status. Condition-dependent
    primary lipidomics remains compatible with this class-level representation.
  target_ids:
  - GO:0034430
  evidence_ids:
  - septin-root19-sources-jats-PMC3229976
  - septin-root19-sources-lipid-monolayer-go
  - septin-record-monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer
- assessment_id: septin-monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer-scope
  area: scope
  topic: Yeast evidence and unresolved plastid boundary
  outcome: supported
  summary: Yeast lipid-particle observations support the stated S. cerevisiae example.
    Austin primary boundary evidence concerns plant plastoglobules coupled to thylakoids;
    it keeps the boundary discussion open without silently extending the yeast experiment
    or merging neighboring structures.
  target_ids:
  - GO:0034430
  evidence_ids:
  - septin-root19-sources-NCBITaxon-4932
  - septin-root19-sources-jats-PMC3229976
  - septin-austin2006-browser-current
  - septin-context-plastoglobule
- assessment_id: septin-monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer-graph
  area: evidence
  topic: Mature surface topology
  outcome: supported
  summary: The nonmechanistic graph describes phospholipid material arranged around
    a neutral-lipid core. It does not claim an experimentally settled ER biogenesis
    pathway or inherit every protein in the secondary review.
  target_ids:
  - GO:0034430
  evidence_ids:
  - septin-record-monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer
  - septin-root19-sources-jats-PMC5947121
  - septin-root19-sources-jats-PMC3229976
- assessment_id: septin-monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer-structured
  area: scope
  topic: Material-only scope supports non-applicability
  outcome: supported
  summary: This target asserts material and topology without named gene, protein or
    pathway claims. That actual scope supports N/A. Its original expression-only wording
    is clarified, but no missing molecular query or additional bundle defect is manufactured.
  target_ids:
  - GO:0034430
  evidence_ids:
  - septin-record-monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer
  - septin-original-monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer
  - septin-native-review-policy
- assessment_id: septin-monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer-native
  area: schema
  topic: Empty native protein inventory and original integrity
  outcome: supported
  summary: Verify and causal checks pass over empty protein examples/typed protein
    nodes. This is bounded schema coverage, not molecular validation. Original native
    review schema/render and target hash pass; the current verdict remains pass with
    limitations.
  target_ids:
  - GO:0034430
  evidence_ids:
  - septin-native-monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer-verify
  - septin-native-monolayer_surrounded_lipid_storage_body_outer_lipid_monolayer-causal
  - septin-original-schema-render
- assessment_id: septin-parasporal_crystal-identity
  area: identity
  topic: Crystalline inclusion and bounded GO search
  outcome: supported
  summary: The local proposed identity and inclusion-body parent distinguish the crystal
    from a single toxin or spore. Native exact GO phrase searches are bounded and
    do not prove exhaustive absence. Historical parasporal-body usage is contextual,
    not exact equivalence of every preparation.
  target_ids:
  - cellstructuremech:parasporal_crystal
  evidence_ids:
  - septin-record-parasporal_crystal
  - septin-parasporal-agent-go
  - septin-parasporal-agent-ols-exact-0
  - septin-parasporal-agent-ols-exact-1
  - septin-parasporal-agent-insell1985-page56
  - septin-parasporal-agent-crossref-book
- assessment_id: septin-parasporal_crystal-components
  area: grounding
  topic: Mixed Cry/Cyt cohort is not a single family
  outcome: supported
  summary: The collective constituent covers distinct Cry lineages and Cyt proteins;
    label-only collective grounding is justified. Native IPR038979 and IPR001615 support
    different family scopes, not a universal identifier for the entire mixed crystal.
    No new grounding defect is established.
  target_ids:
  - cellstructuremech:parasporal_crystal
  evidence_ids:
  - septin-record-parasporal_crystal
  - septin-parasporal-agent-IPR038979
  - septin-parasporal-agent-IPR001615
  - septin-parasporal-agent-jats-PMC4280536
  - septin-parasporal-agent-jats-PMC4014730
- assessment_id: septin-parasporal_crystal-examples
  area: grounding
  topic: Concrete protein identities
  outcome: supported
  summary: P16480 cry4Aa, P21256 cry11Aa and P0A382 cyt1Aa are reviewed entries for
    israelensis1430; exact queries corroborate them. They are examples rather than
    an exhaustive strain inventory or a universal stoichiometry.
  target_ids:
  - cellstructuremech:parasporal_crystal
  evidence_ids:
  - septin-parasporal-agent-P16480
  - septin-parasporal-agent-P21256
  - septin-parasporal-agent-P0A382
  - septin-parasporal-agent-query-cry4Aa
  - septin-parasporal-agent-query-cry11Aa
  - septin-parasporal-agent-query-cyt1Aa
  - septin-parasporal-agent-tax-1430
- assessment_id: septin-parasporal_crystal-necessity
  area: evidence
  topic: Crystal formation versus toxicity
  outcome: unknown
  summary: UNKNOWN necessity is retained for the broad constituent cohort. Biological
    activity after solubilization/activation and modern specific toxin structures
    do not establish a universal formation requirement or the minimal composition
    of all crystals.
  target_ids:
  - cellstructuremech:parasporal_crystal
  evidence_ids:
  - septin-record-parasporal_crystal
  - septin-parasporal-agent-jats-PMC4280536
  - septin-parasporal-agent-jats-PMC4014730
  - septin-parasporal-agent-legacy-PMC1857359
- assessment_id: septin-parasporal_crystal-scope
  area: scope
  topic: Strain and historical morphology limits
  outcome: supported
  summary: 'Variable Bt occurrence and the israelensis example remain bounded by strain/plasmid
    differences. All seven Insell primary scan pages were read, including figures:
    historical light/dark lattice and polypeptide fractions are not assigned to exact
    modern Cry/Cyt accessions.'
  target_ids:
  - cellstructuremech:parasporal_crystal
  evidence_ids:
  - septin-parasporal-agent-tax-1428
  - septin-parasporal-agent-tax-1430
  - septin-parasporal-agent-jats-PMC4014730
  - septin-parasporal-agent-insell1985-page56
  - septin-parasporal-agent-insell1985-page57
  - septin-parasporal-agent-insell1985-page58
  - septin-parasporal-agent-insell1985-page59
  - septin-parasporal-agent-insell1985-page60
  - septin-parasporal-agent-insell1985-page61
  - septin-parasporal-agent-insell1985-page62
- assessment_id: septin-parasporal_crystal-graph
  area: evidence
  topic: Packaging graph and conventional activity terminology
  outcome: supported
  summary: The single nonmechanistic edge represents a crystalline packaging state,
    not a full sporulation or toxin-action mechanism. Pesticidal is conventional cohort
    terminology here, not demonstrated activity for every parasporin or every constituent.
  target_ids:
  - cellstructuremech:parasporal_crystal
  evidence_ids:
  - septin-record-parasporal_crystal
  - septin-parasporal-agent-jats-PMC4280536
  - septin-parasporal-agent-legacy-PMC1857359
  - septin-parasporal-agent-insell1985-page57
- assessment_id: septin-parasporal_crystal-structured
  area: scope
  topic: Applicability assessed without mismatched species
  outcome: supported
  summary: Named Cry/Cyt molecular claims require an applicability assessment. Fresh
    official catalogue includes no B. thuringiensis/israelensis dataset; B. subtilis
    is not a replacement and no arbitrary gene/module query is invented. The original
    omitted assessment is corrected in the successor.
  target_ids:
  - cellstructuremech:parasporal_crystal
  evidence_ids:
  - septin-record-parasporal_crystal
  - septin-original-parasporal_crystal
  - septin-current-adapter-catalogue
  - septin-historical-adapter-runner-unavailable
- assessment_id: septin-parasporal_crystal-native
  area: schema
  topic: Current native checks and original integrity
  outcome: supported
  summary: All three examples verify and the single typed protein graph node has declared-symbol
    coverage. This cannot certify the entire mixed Cry/Cyt pool. Original schema/render
    and unchanged input hash pass.
  target_ids:
  - cellstructuremech:parasporal_crystal
  evidence_ids:
  - septin-native-parasporal_crystal-verify
  - septin-native-parasporal_crystal-causal
  - septin-original-schema-render
  - septin-original-parasporal_crystal
- assessment_id: current-input-comparison
  area: provenance
  topic: Complete frozen-input comparison and bounded refresh
  outcome: supported
  summary: 2 of ten original target hashes differ from current main. The changed content
    is substantively reassessed in the target-specific assessments; original observations
    remain historical and unchanged. All current target and used context bytes are
    frozen.
  target_ids:
  - cellstructuremech:age_associated_protein_deposit
  - cellstructuremech:bacterial_aggresome
  - GO:0033172
  - cellstructuremech:insoluble_protein_deposit
  - cellstructuremech:intranuclear_quality_control_compartment
  - cellstructuremech:juxtanuclear_quality_control_compartment
  - cellstructuremech:mitostore
  - GO:0034430
  - GO:0140602
  - cellstructuremech:parasporal_crystal
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
- finding_id: septin-S2356-F1
  issue_key: gas-vesicle-shell-gvpa-family-grounding
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Record the verified exact GvpA family grounding
  description: The named GvpA constituent has no grounding or explicit unresolved-grounding
    discussion. Native IPR047870 specifically denotes GvpA, whereas the existing graph
    xref PF00741 covers a broader GvpA-like family including GvpJ. Add the exact family
    at the component; retain broader graph xrefs as related context. The GvpC repeat
    entries are not whole-protein equivalents.
  target_ids:
  - GO:0033172
  field_paths:
  - components[component_id=gvpa].grounding
  - components[component_id=gvpa].grounding_status
  evidence_ids:
  - septin-record-gas_vesicle_shell
  - septin-root19-sources-IPR047870
  - septin-root19-sources-IPR000638
  - septin-root19-sources-PF00741
  - septin-root19-sources-UniProtKB-A0ABR7ZBW9
  - septin-native-review-policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/inclusion/gas_vesicle_shell.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Components
  native_severity: minor
  normalization_reason: The biological identity, membership and existing related xref
    are sound; the correction records an available exact family without changing scientific
    scope.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T103321Z-gas-vesicle-shell-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2630
actions:
- action_id: septin-S2356-C1
  finding_ids:
  - septin-S2356-F1
  target_ids:
  - GO:0033172
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/inclusion/gas_vesicle_shell.yaml
    role: maintained scientific record
  description: Ground the GvpA component to verified InterPro IPR047870 with exact
    family provenance and appropriate grounding status. Preserve the distinction between
    exact family identity, concrete protein examples and related graph xrefs.
  acceptance_checks:
  - Reconfirm IPR047870 is the GvpA-specific family, with the broader GvpA-like entry
    kept distinct.
  - Do not promote PF01304 or the GvpC repeat entries to whole-protein equivalence.
  - Use separately authorized guarded curation, append-only history, focused validators,
    identifier/product checks and regeneration.
limitations:
- 'INQ, JUNQ and nucleolar peripheral inclusion body independent subreview: Only the
  three assigned current records were substantively reviewed. All are byte-unchanged;
  no stale record in this slice requires refresh. Current source review does not promote
  PROPOSED records or resolve unrelated findings.'
- 'INQ, JUNQ and nucleolar peripheral inclusion body independent subreview: Gallardo2020
  and Hiraoka2023 primary article body/captions were recovered through browser extraction
  of ResearchGate-hosted paper text. Gallardo repository URLs returned HTML application
  shells, not PDFs; publisher requests failed. Origin full PDFs and their figure pixels
  were not independently inspected. Native GO references corroborate bibliographic
  identity; root owns the bounded PMID gate.'
- 'INQ, JUNQ and nucleolar peripheral inclusion body independent subreview: Primary
  main bodies and claim-bearing captions were assessed for Miller2015, Gallina2015,
  Sontag2023, Kaganovich2008, Rolli2024 and Boronat2023. Supplemental figures, strain
  tables, movies and raw data were not independently reanalysed; descriptions of them
  in main text remain qualified. Pixel inspection was limited to the three frozen
  tracked image composites.'
- 'INQ, JUNQ and nucleolar peripheral inclusion body independent subreview: Historical
  JUNQ nomenclature, Sontag Keima-caption inconsistency and sampled NES-Keima fields,
  Rolli nuclear-dye/timing discrepancies and differing proteasome effects remain explicit
  rather than silently reconciled.'
- 'INQ, JUNQ and nucleolar peripheral inclusion body independent subreview: Nine EuropePMC
  DOI metadata endpoints returned503; direct InterPro IPR013126 returned429. Fresh
  primary article metadata and successful exact protein-family match rows provide
  the narrower checks described, without treating these failed requests as successes.'
- 'INQ, JUNQ and nucleolar peripheral inclusion body independent subreview: The iModulonDB
  result is bounded to the complete fresh20-organism/28-dataset catalogue. It does
  not establish biological absence, absence from other expression resources, or new
  runner execution. Neither yeast genus was matched, so no bacterial dataset or expression
  module was substituted.'
- 'INQ, JUNQ and nucleolar peripheral inclusion body independent subreview: Full corpus
  QC, CI, issue deduplication and GitHub actions are root-owned. This independent
  reviewer performed no repository or GitHub writes. Scratch receipts and reports
  are the only authored files.'
- 'Age-associated deposit, IPOD and MitoStore independent subreview: Scope: only age-associated
  protein deposit, IPOD and MitoStore were scientifically reviewed by this independent
  slice. Other PR targets and category-wide findings were not adjudicated.'
- 'Age-associated deposit, IPOD and MitoStore independent subreview: Fresh primary
  sources were accessed at their individual receipt times. JATS/front/body/caption
  access does not mean every supplementary file, raw dataset, movie or image was analyzed.
  Direct pixels were inspected only for the three frozen tracked JPEGs and age2017
  FigureS5 (physical PDFpp35–36).'
- 'Age-associated deposit, IPOD and MitoStore independent subreview: Age2025 review
  excludes the huntingtin results subsection and supplementary datasets; age2018 is
  a secondary nomenclature-only caption source. Source-internal cycloheximide-dose
  conflict is explicitly preserved.'
- 'Age-associated deposit, IPOD and MitoStore independent subreview: IPOD2008 primary
  PMC HTML was inspected after the Nature route returned a client challenge. No full
  online supplementary Methods or movies were retrieved. Its terminal-sequestration
  language is restricted to its Ubc9ts assay rather than used to deny later slow PrD-GFP
  turnover.'
- 'Age-associated deposit, IPOD and MitoStore independent subreview: MitoStore2023
  raw proteomics, supplemental strain workbook and extended-figure pixels were not
  reanalyzed. Liu2023 access is restricted to Results s2 and full Discussion; similarity
  is not exact identity. PXD035762 metadata conflicts remain bounded provenance already
  acknowledged in the record.'
- 'Age-associated deposit, IPOD and MitoStore independent subreview: The combined
  EuropePMC DOI metadata request returnedHTTP503 twice and was not used as successful
  bibliographic evidence; article JATS fronts, authentic primary HTML and the accepted-manuscript
  title support the cited identities. IPR050130 initially returnedHTTP429, then a
  separate documented fetch succeeded; its unreviewed machine-generated functional
  prose is not scientific support.'
- 'Age-associated deposit, IPOD and MitoStore independent subreview: UniProt/InterPro
  and taxonomy establish accession/classification identity, not localization, stoichiometry
  or necessity. Bounded reviewed-symbol and GO literal-name queries do not establish
  universal absence or cover all strains/synonyms.'
- 'Age-associated deposit, IPOD and MitoStore independent subreview: The iModulonDB
  source catalogue was freshly inspected; a retained00:49Z runner PermissionError
  is historical and no current runner execution is claimed. No matched Saccharomyces
  dataset was returned, so gene/module/activity checks are N/A for this catalogue
  snapshot rather than negative biology.'
- 'Age-associated deposit, IPOD and MitoStore independent subreview: Common seventeen
  native policy/config/schema/verifier inputs were previously read and are byte-identical
  to the prior accepted slice; current record/review/image inputs were freshly inspected.
  Only the29 listed local inputs were used; root-frozen neighbor records for other
  reviewers were not read here.'
- 'Age-associated deposit, IPOD and MitoStore independent subreview: Root owns whole-corpus
  gates, issue deduplication and publication. This report independently inspects the
  six supplied target-specific native protein receipts and original-bundle validation/render
  evidence; it does not claim to rerun global QC.'
- 'Bacterial aggresome, gas vesicle shell, outer lipid monolayer and parasporal crystal
  independent subreview: Independent agent review of these four current records and
  original bundles only. No repository or GitHub mutation, exhaustive literature census,
  neighboring whole-record review or raw-data reanalysis.'
- 'Bacterial aggresome, gas vesicle shell, outer lipid monolayer and parasporal crystal
  independent subreview: Jin reading covers experimental Results, Discussion and strain/construction
  Methods; Pei uses the deposited accepted manuscript with explicitly bounded pages/sections
  and actual Figures5/6 pixels. Early model/caption passages are only partly read,
  and raw RNA-seq/proteomics, tracking, videos and mathematical supplements are not
  reanalysed.'
- 'Bacterial aggresome, gas vesicle shell, outer lipid monolayer and parasporal crystal
  independent subreview: Dutka native body supports structural claims at stated section
  scope, with homology fitting, stripping and finite-element predictions distinguished.
  Bayro fresh body scope is limited to abstract/introduction and preparation context;
  Walsby and Hayes remain abstract scope. No new gas-vesicle image-pixel or raw NMR/tomogram
  audit.'
- 'Bacterial aggresome, gas vesicle shell, outer lipid monolayer and parasporal crystal
  independent subreview: GvpC conditional assembly necessity remains unverified; lack
  of inspected proof is not a new contradictory finding. Historical whole-organelle
  finding dispositions are context only, not resolved or reopened by this shell review.'
- 'Bacterial aggresome, gas vesicle shell, outer lipid monolayer and parasporal crystal
  independent subreview: Graef, Wang, Palma, Ben-Dov and Bravo are secondary reviews
  at specified scopes. Wang browser abstract does not expose the exact monolayer body
  passage. Austin browser-indexed primary context is distinct from direct challenge
  responses and does not automatically resolve the plastoglobule boundary.'
- 'Bacterial aggresome, gas vesicle shell, outer lipid monolayer and parasporal crystal
  independent subreview: All seven Insell/Fitz-James1985 native scans were visually
  read. Historical morphology/polypeptide classes do not identify modern Cry/Cyt accessions.
  The1990 book chapter is metadata-only. Actual current GO phrase queries are bounded,
  not exhaustive ontology absence.'
- 'Bacterial aggresome, gas vesicle shell, outer lipid monolayer and parasporal crystal
  independent subreview: Fresh official iModulonDB fallback is separate from the historical
  failed runner observation. Only precise_mg1655 and eleven named aggresome-related
  genes were queried; six positive modules were checked at both gene and module endpoints.
  All-false flags are threshold results, not absence. Generated module/InterPro prose
  is excluded.'
- 'Bacterial aggresome, gas vesicle shell, outer lipid monolayer and parasporal crystal
  independent subreview: No matching native gas-shell or Bt dataset was found in the
  returned20-organism/28-dataset catalogue; no unrelated species is substituted. Material-only
  lipid-monolayer scope is genuinely N/A, without inventing a query defect.'
- 'Bacterial aggresome, gas vesicle shell, outer lipid monolayer and parasporal crystal
  independent subreview: Native protein checks establish concrete identifier/typed-node
  coverage only. Aggresome and monolayer have zero typed protein nodes; monolayer
  also has no protein examples. Narrative molecular claims were reviewed separately
  where present.'
- 'Bacterial aggresome, gas vesicle shell, outer lipid monolayer and parasporal crystal
  independent subreview: Root owns final corpus gates, CI, issue dedup/publication
  and immutable synthesis. This report records only the inspected source-head receipts,
  not prospective final-head success.'
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
  Every inherited finding is reassessed and retains exact predecessor identity.
- 'Bundle issues #2628 and #2629 address two stale reviews and nine structured-source
  applicability defects. Scientific curation stays separately tracked and open. Existing
  validator #2514 remains open.'
- The added self-node identifiers are assessed against current record identity, graph
  scope and primary sources. A historical neighboring-record review is context only;
  no whole-organelle finding is terminally resolved by this cohort.
- Source commit 7362758aca3756f5979304474ceb02a18f1a6ce6 is retained by tag review-base/pr2356-current-record-followup-20261103.
- CLAUDE.md is an alias of AGENTS.md; canonical regular AGENTS.md bytes are frozen.
- Used local context was frozen before assessment, including native review configuration,
  graph/protein policies, verifier source, six target figures, five neighboring records
  and the historical gas-vesicle reassessment pair. Neighbors are context, not additional
  curation targets.
- 'Three molecular-scope reviews used unsupported expression-only exemptions: gas
  vesicle shell, IPOD and INQ. Six omitted applicability: age-associated deposit,
  bacterial aggresome, JUNQ, MitoStore, nucleolar peripheral inclusion body and parasporal
  crystal. The lipid monolayer target has material/topology-only scope; its weak N/A
  wording is clarified without inventing a molecular query or extra defect.'
- Fresh source inspection retains actual access dates. Primary bodies, abstracts,
  secondary reviews, image pixels and authority responses have distinct evidence scopes.
- Native checks with empty protein inventories or zero GENE_OR_PROTEIN nodes do not
  validate molecular mechanisms or names appearing only in prose. Exact represented
  identity, taxon, membership, location, function and assembly necessity remain separate
  judgments.
- One minor gas-vesicle-shell GvpA-family finding retains exact original F1 lineage
  and remains open for record curation. The other nine targets retain qualified scientific
  passes. No finding is terminally resolved by this cohort.
- 'Draft validation identified an invalid assessment outcome in the synthesis source.
  Issue #2631 tracks correcting it to the native concern enum while retaining #2630,
  its exact finding lineage and separate curation action. The failed uncommitted validation
  remains in the execution receipts.'
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T103319Z-age-associated-protein-deposit-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T103320Z-bacterial-aggresome-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T103321Z-gas-vesicle-shell-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T103322Z-insoluble-protein-deposit-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T103323Z-intranuclear-quality-control-compartment-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T103324Z-juxtanuclear-quality-control-compartment-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T103324Z-mitostore-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T103325Z-monolayer-surrounded-lipid-storage-body-outer-lipid-monolayer-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T103326Z-nucleolar-peripheral-inclusion-body-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T103327Z-parasporal-crystal-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
links:
- https://github.com/CultureBotAI/CellStructureMech/pull/2356
- https://github.com/CultureBotAI/CellStructureMech/issues/2514
- https://github.com/CultureBotAI/CellStructureMech/issues/2628
- https://github.com/CultureBotAI/CellStructureMech/issues/2629
- https://github.com/CultureBotAI/CellStructureMech/issues/2630
- https://github.com/CultureBotAI/CellStructureMech/issues/2631
```
