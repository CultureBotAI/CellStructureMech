# PR 2369: current-input review of ten records and adversarial follow-up

- Review: 20261103T161755Z-pr2369-current-record-followup
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-11-03T16:06:50.712558Z
- Finished UTC: 2026-11-03T16:17:55Z
- Reviewer: Codex root synthesis with three independent read-only adversarial reviewers (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

All ten records are reassessed against current main with47 frozen local inputs. Four stale reviews are substantively refreshed: Maurer cleft REX1, methane-organelle pmoC1 and microneme M2AP additions, plus crista-junction MICOS typing. Nine unsupported expression-only source exclusions are corrected; the posterior-vacuole record retains a justified sparse physical-scope exclusion. Eight inherited scientific findings remain (one major, seven minor) across five records; five other records receive qualified passes within explicit source limits. Bundle issues2721 and2722 are addressed by the successor. Scientific curation and reused validator2514 remain separate and open. No record is edited.

## Scope And Provenance

Exact ten-record PR cohort reassessed against current main 2e0792c49e1040ad8b89b9a5f7c81fea69c995cc. Changed inputs are substantively reassessed. Scientific records remain unchanged.

Selection: Complete cohort of ten maintained records reviewed in original PR head 5a91e2c6b6d716170c0a3414ebadc6578d261632.
Coverage: full; 10 reviewed / 10 in the declared population.
Source: working_tree at Git base 61d3617ae8700b99198e2aaf01f3b2437933de6c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0020036 | data/structures/membrane_organelle/maurer_s_cleft.yaml | maintained | Maurer's cleft |
| GO:0044227 | data/structures/membrane_organelle/methane_oxidizing_organelle.yaml | maintained | methane-oxidizing organelle |
| GO:0020009 | data/structures/membrane_organelle/microneme.yaml | maintained | microneme |
| GO:0034494 | data/structures/membrane_organelle/microneme_lumen.yaml | maintained | microneme lumen |
| GO:0033163 | data/structures/membrane_organelle/microneme_membrane.yaml | maintained | microneme membrane |
| GO:0031040 | data/structures/membrane_organelle/micronucleus.yaml | maintained | micronucleus |
| cellstructuremech:microsporidian_posterior_vacuole | data/structures/membrane_organelle/microsporidian_posterior_vacuole.yaml | maintained | microsporidian posterior vacuole |
| GO:0030061 | data/structures/membrane_organelle/mitochondrial_crista.yaml | maintained | mitochondrial crista |
| GO:0044284 | data/structures/membrane_organelle/mitochondrial_crista_junction.yaml | maintained | mitochondrial crista junction |
| cellstructuremech:mitochondrial_derived_compartment | data/structures/membrane_organelle/mitochondrial_derived_compartment.yaml | maintained | mitochondrial-derived compartment |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full native QC | passed | True | GO:0020036, GO:0044227, GO:0020009, GO:0034494, GO:0033163, GO:0031040, cellstructuremech:microsporidian_posterior_vacuole, GO:0030061, GO:0044284, cellstructuremech:mitochondrial_derived_compartment | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| Native label correspondence | passed | True | GO:0020036, GO:0044227, GO:0020009, GO:0034494, GO:0033163, GO:0031040, cellstructuremech:microsporidian_posterior_vacuole, GO:0030061, GO:0044284, cellstructuremech:mitochondrial_derived_compartment | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| TraitMech references | passed | True | GO:0020036, GO:0044227, GO:0020009, GO:0034494, GO:0033163, GO:0031040, cellstructuremech:microsporidian_posterior_vacuole, GO:0030061, GO:0044284, cellstructuremech:mitochondrial_derived_compartment | Native TraitMech link check passed. |
| Pinned governed files | passed | True | GO:0020036, GO:0044227, GO:0020009, GO:0034494, GO:0033163, GO:0031040, cellstructuremech:microsporidian_posterior_vacuole, GO:0030061, GO:0044284, cellstructuremech:mitochondrial_derived_compartment | Pinned governed files match; native vendored check passed. |
| Native identifier resolver | passed | True | GO:0020036, GO:0044227, GO:0020009, GO:0034494, GO:0033163, GO:0031040, cellstructuremech:microsporidian_posterior_vacuole, GO:0030061, GO:0044284, cellstructuremech:mitochondrial_derived_compartment | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| validate GO:0020036 | passed | True | GO:0020036 | Documented focused command passed. |
| validate-strict GO:0020036 | passed | True | GO:0020036 | Documented focused command passed. |
| validate GO:0044227 | passed | True | GO:0044227 | Documented focused command passed. |
| validate-strict GO:0044227 | passed | True | GO:0044227 | Documented focused command passed. |
| validate GO:0020009 | passed | True | GO:0020009 | Documented focused command passed. |
| validate-strict GO:0020009 | passed | True | GO:0020009 | Documented focused command passed. |
| validate GO:0034494 | passed | True | GO:0034494 | Documented focused command passed. |
| validate-strict GO:0034494 | passed | True | GO:0034494 | Documented focused command passed. |
| validate GO:0033163 | passed | True | GO:0033163 | Documented focused command passed. |
| validate-strict GO:0033163 | passed | True | GO:0033163 | Documented focused command passed. |
| validate GO:0031040 | passed | True | GO:0031040 | Documented focused command passed. |
| validate-strict GO:0031040 | passed | True | GO:0031040 | Documented focused command passed. |
| validate cellstructuremech:microsporidian_posterior_vacuole | passed | True | cellstructuremech:microsporidian_posterior_vacuole | Documented focused command passed. |
| validate-strict cellstructuremech:microsporidian_posterior_vacuole | passed | True | cellstructuremech:microsporidian_posterior_vacuole | Documented focused command passed. |
| validate GO:0030061 | passed | True | GO:0030061 | Documented focused command passed. |
| validate-strict GO:0030061 | passed | True | GO:0030061 | Documented focused command passed. |
| validate GO:0044284 | passed | True | GO:0044284 | Documented focused command passed. |
| validate-strict GO:0044284 | passed | True | GO:0044284 | Documented focused command passed. |
| validate cellstructuremech:mitochondrial_derived_compartment | passed | True | cellstructuremech:mitochondrial_derived_compartment | Documented focused command passed. |
| validate-strict cellstructuremech:mitochondrial_derived_compartment | passed | True | cellstructuremech:mitochondrial_derived_compartment | Documented focused command passed. |
| Supplemental bounded PMID authority checks | passed | True | GO:0020036, GO:0044227, GO:0020009, GO:0034494, GO:0033163, GO:0031040, cellstructuremech:microsporidian_posterior_vacuole, GO:0030061, GO:0044284, cellstructuremech:mitochondrial_derived_compartment | 909 PMIDs all OK in bounded native requests; full-command limitations remain separate. |
| Official structured-source applicability and covered-dataset cross-checks | passed | False | GO:0020036, GO:0044227, GO:0020009, GO:0034494, GO:0033163, GO:0031040, cellstructuremech:microsporidian_posterior_vacuole, GO:0030061, GO:0044284, cellstructuremech:mitochondrial_derived_compartment | Nine original expression-only exclusions were reassessed against whole-record molecular/pathway claims and fresh complete official iModulonDB catalogue coverage. No matching Plasmodium/Toxoplasma, Methylococcus Bath, Tetrahymena or Saccharomyces experimental-host dataset was found in the documented complete catalogue inspection. The sparse posterior-vacuole record has a justified physical morphology/expansion exclusion with unresolved molecular composition. No foreign-host proxy or biological-absence inference is made. Historical runner unavailability is not presented as a fresh invocation. |
| Independent claim-level source review | passed | True | GO:0020036, GO:0044227, GO:0020009, GO:0034494, GO:0033163, GO:0031040, cellstructuremech:microsporidian_posterior_vacuole, GO:0030061, GO:0044284, cellstructuremech:mitochondrial_derived_compartment | Three read-only reviewers covered the complete ten-record cohort, including changed inputs, with explicit scientific findings and source-access limits. Final artifact/head acceptance occurs after saving. |
| Retained historical adapter runner availability | unavailable | False | GO:0020036, GO:0044227, GO:0020009, GO:0034494, GO:0033163, GO:0031040, cellstructuremech:microsporidian_posterior_vacuole, GO:0030061, GO:0044284, cellstructuremech:mitochondrial_derived_compartment | Historical 00:49Z invocation unavailable due to OS access restriction. Official catalogue source fallback was inspected separately; no current invocation or successful adapter execution is claimed. The actual historical exit code 1 is retained in the evidence receipt, since the native unavailable-check model has no execution exit-code field. |
| Native maurer s cleft UniProt verify check | passed | True | GO:0020036 | Read-only native command returned zero. Three unreviewed examples and two COVERED nodes. Native identity is distinct from source-supported trafficking/localization and necessity. |
| Native maurer s cleft UniProt causal check | passed | True | GO:0020036 | Read-only native command returned zero. Three unreviewed examples and two COVERED nodes. Native identity is distinct from source-supported trafficking/localization and necessity. |
| Native methane oxidizing organelle UniProt verify check | passed | True | GO:0044227 | Read-only native command returned zero. Two reviewed and one unreviewed examples; one COVERED pMMO node. Native pmoA1/pmoB1/pmoC1 identity is distinguished from exact biochemical, structural and strain evidence. |
| Native methane oxidizing organelle UniProt causal check | passed | True | GO:0044227 | Read-only native command returned zero. Two reviewed and one unreviewed examples; one COVERED pMMO node. Native pmoA1/pmoB1/pmoC1 identity is distinguished from exact biochemical, structural and strain evidence. |
| Native microneme UniProt verify check | passed | True | GO:0020009 | Read-only native command returned zero. Five example occurrences across four distinct accessions: two reviewed plus three unreviewed occurrences. MIC2 occurs under both an adhesin cohort and the MIC2-M2AP complex; both typed nodes are COVERED. Identity does not determine lumen topology or complex function. |
| Native microneme UniProt causal check | passed | True | GO:0020009 | Read-only native command returned zero. Five example occurrences across four distinct accessions: two reviewed plus three unreviewed occurrences. MIC2 occurs under both an adhesin cohort and the MIC2-M2AP complex; both typed nodes are COVERED. Identity does not determine lumen topology or complex function. |
| Native microneme lumen UniProt verify check | passed | True | GO:0034494 | Read-only native command returned zero. No represented protein examples or typed molecular nodes; positive narrative molecular/pathway assertions and physical-scope exclusions are assessed separately. |
| Native microneme lumen UniProt causal check | passed | True | GO:0034494 | Read-only native command returned zero. No represented protein examples or typed molecular nodes; positive narrative molecular/pathway assertions and physical-scope exclusions are assessed separately. |
| Native microneme membrane UniProt verify check | passed | True | GO:0033163 | Read-only native command returned zero. No represented protein examples or typed molecular nodes; positive narrative molecular/pathway assertions and physical-scope exclusions are assessed separately. |
| Native microneme membrane UniProt causal check | passed | True | GO:0033163 | Read-only native command returned zero. No represented protein examples or typed molecular nodes; positive narrative molecular/pathway assertions and physical-scope exclusions are assessed separately. |
| Native micronucleus UniProt verify check | passed | True | GO:0031040 | Read-only native command returned zero. No represented protein examples or typed molecular nodes; positive narrative molecular/pathway assertions and physical-scope exclusions are assessed separately. |
| Native micronucleus UniProt causal check | passed | True | GO:0031040 | Read-only native command returned zero. No represented protein examples or typed molecular nodes; positive narrative molecular/pathway assertions and physical-scope exclusions are assessed separately. |
| Native microsporidian posterior vacuole UniProt verify check | passed | True | cellstructuremech:microsporidian_posterior_vacuole | Read-only native command returned zero. No represented protein examples or typed molecular nodes; positive narrative molecular/pathway assertions and physical-scope exclusions are assessed separately. |
| Native microsporidian posterior vacuole UniProt causal check | passed | True | cellstructuremech:microsporidian_posterior_vacuole | Read-only native command returned zero. No represented protein examples or typed molecular nodes; positive narrative molecular/pathway assertions and physical-scope exclusions are assessed separately. |
| Native mitochondrial crista UniProt verify check | passed | True | GO:0030061 | Read-only native command returned zero. No represented protein examples or typed molecular nodes; positive narrative molecular/pathway assertions and physical-scope exclusions are assessed separately. |
| Native mitochondrial crista UniProt causal check | passed | True | GO:0030061 | Read-only native command returned zero. No represented protein examples or typed molecular nodes; positive narrative molecular/pathway assertions and physical-scope exclusions are assessed separately. |
| Native mitochondrial crista junction UniProt verify check | passed | True | GO:0044284 | Read-only native command returned zero. No represented protein examples or typed molecular nodes; positive narrative molecular/pathway assertions and physical-scope exclusions are assessed separately. |
| Native mitochondrial crista junction UniProt causal check | passed | True | GO:0044284 | Read-only native command returned zero. No represented protein examples or typed molecular nodes; positive narrative molecular/pathway assertions and physical-scope exclusions are assessed separately. |
| Native mitochondrial derived compartment UniProt verify check | passed | True | cellstructuremech:mitochondrial_derived_compartment | Read-only native command returned zero. Three reviewed examples (TOM70/P07213, TOM71/P38825, DNM1/P54861); zero typed GENE_OR_PROTEIN nodes. Protein identities are separate from source-specific induction, deletion background, physical recruitment and necessity. |
| Native mitochondrial derived compartment UniProt causal check | passed | True | cellstructuremech:mitochondrial_derived_compartment | Read-only native command returned zero. Three reviewed examples (TOM70/P07213, TOM71/P38825, DNM1/P54861); zero typed GENE_OR_PROTEIN nodes. Protein identities are separate from source-specific induction, deletion background, physical recruitment and necessity. |

## Scientific And Domain Assessments

### Frozen original schema/render and current input comparison

schema: supported. Targets: GO:0020036.

Original validation/render and historical hash checks pass. Stale target gains one unreviewed protein example and curation history; both new identity and scientific membership context are reassessed. Schema validity is not scientific/source certification.

### Actual native protein inventory and command coverage

provenance: supported. Targets: GO:0020036.

Three UNREVIEWED example occurrences and three distinct accessions Q6V0W9,Q8I2G1,Q9NFF5; two COVERED GENE_OR_PROTEIN nodes. Q6V0W9 is a fragment. Native identity/coverage does not demonstrate accession-specific membership, complete composition, causality or formation necessity.

### Images, physical measurements, traits and snippets

scope: not_applicable. Targets: GO:0020036.

No maintained image, numeric physical measurement, associated trait or verbatim snippet is asserted. Source captions are distinguished from uninspected figure pixels; no image licence or raw-data reanalysis is certified.

### Status and bounded historical lineage

provenance: supported. Targets: GO:0020036.

PROPOSED status and current history are retained. Original occurrences are linked only to their maintained target; no neighbor/group/category issue is declared resolved.

### Frozen original schema/render and current input comparison

schema: supported. Targets: GO:0020009.

Original validation/render and historical hash checks pass. Stale target gains one unreviewed protein example and curation history; both new identity and scientific membership context are reassessed. Schema validity is not scientific/source certification.

### Actual native protein inventory and command coverage

provenance: supported. Targets: GO:0020009.

Five protein-example occurrences but four distinct accessions: MIC2/S8F9G8 occurs under both adhesin cohort and MIC2-M2AP complex. Two REVIEWED occurrences O00834/B6KAM0 and three UNREVIEWED occurrences S8F9G8 twice/S8GDJ1 once; two COVERED GENE_OR_PROTEIN nodes. Correct identity and symbol coverage do not prove complete complex stoichiometry, localization topology or causal necessity.

### Images, physical measurements, traits and snippets

scope: not_applicable. Targets: GO:0020009.

No maintained image, numeric physical measurement, associated trait or verbatim snippet is asserted. Source captions are distinguished from uninspected figure pixels; no image licence or raw-data reanalysis is certified.

### Status and bounded historical lineage

provenance: supported. Targets: GO:0020009.

PROPOSED status and current history are retained. Original occurrences are linked only to their maintained target; no neighbor/group/category issue is declared resolved.

### Frozen original schema/render and current input comparison

schema: supported. Targets: GO:0034494.

Original validation/render and historical hash checks pass. Current target is byte-identical to original input, with scientific claims reassessed. Schema validity is not scientific/source certification.

### Actual native protein inventory and command coverage

provenance: supported. Targets: GO:0034494.

Zero protein examples and zero typed GENE_OR_PROTEIN nodes; no represented UniProtKB graph xrefs. Exit0 validates an empty identifier inventory, not the complete secretion/pathway narrative.

### Images, physical measurements, traits and snippets

scope: not_applicable. Targets: GO:0034494.

No maintained image, numeric physical measurement, associated trait or verbatim snippet is asserted. Source captions are distinguished from uninspected figure pixels; no image licence or raw-data reanalysis is certified.

### Status and bounded historical lineage

provenance: supported. Targets: GO:0034494.

PROPOSED status and current history are retained. Original occurrences are linked only to their maintained target; no neighbor/group/category issue is declared resolved.

### Frozen original schema/render and current input comparison

schema: supported. Targets: GO:0033163.

Original validation/render and historical hash checks pass. Current target is byte-identical to original input, with scientific claims reassessed. Schema validity is not scientific/source certification.

### Actual native protein inventory and command coverage

provenance: supported. Targets: GO:0033163.

Zero protein examples and zero typed GENE_OR_PROTEIN nodes; no represented UniProtKB graph xrefs. Exit0 validates an empty identifier inventory, not the complete exocytosis/pathway narrative.

### Images, physical measurements, traits and snippets

scope: not_applicable. Targets: GO:0033163.

No maintained image, numeric physical measurement, associated trait or verbatim snippet is asserted. Source captions are distinguished from uninspected figure pixels; no image licence or raw-data reanalysis is certified.

### Status and bounded historical lineage

provenance: supported. Targets: GO:0033163.

PROPOSED status and current history are retained. Original occurrences are linked only to their maintained target; no neighbor/group/category issue is declared resolved.

### Full molecular/pathway narrative applicability

scope: supported. Targets: GO:0020036.

This record asserts PfEMP1 trafficking and named SBP1/MAHRP1/REX residents, so expression-only exclusion is unsupported. Current official catalogue has no matching parasite host; downstream gene/module queries are therefore not applicable within this catalogue, not biologically refuted. Runner receipt is historical.

### Full molecular/pathway narrative applicability

scope: supported. Targets: GO:0020009.

This record asserts adhesin-complex trafficking, regulated exocytosis and invasion, so expression-only exclusion is unsupported. Current official catalogue has no matching parasite host; downstream gene/module queries are therefore not applicable within this catalogue, not biologically refuted. Runner receipt is historical.

### Full molecular/pathway narrative applicability

scope: supported. Targets: GO:0034494.

This record asserts secretory cargo storage and regulated release, so expression-only exclusion is unsupported. Current official catalogue has no matching parasite host; downstream gene/module queries are therefore not applicable within this catalogue, not biologically refuted. Runner receipt is historical.

### Full molecular/pathway narrative applicability

scope: supported. Targets: GO:0033163.

This record asserts regulated membrane fusion/exocytosis and cargo release, so expression-only exclusion is unsupported. Current official catalogue has no matching parasite host; downstream gene/module queries are therefore not applicable within this catalogue, not biologically refuted. Runner receipt is historical.

### Exact Maurer cleft and host/parasite boundary

identity: supported. Targets: GO:0020036.

GO0020036 denotes parasite-derived membranous clefts in infected erythrocyte cytoplasm. The parasite is the canonical organism; host red-cell compartment is localization context. Broader membrane-bounded-organelle parent is biologically compatible but not a claimed native GO is_a edge in this response.

### New REX1 accession and current experimental scope

grounding: supported. Targets: GO:0020036.

New Q8I2G1 is UNREVIEWED REX1, taxon36329 and ORF PF3D7_0935900. It lacks a formal primary geneName field, so no such authority-field claim is certified. Correct locus/protein identity plus Cooke Rex cleft-marker context supports the representative example; no exact knock-out/necessity result follows from this accession.

### Collective bilayer and heterogeneous resident class

grounding: supported. Targets: GO:0020036.

Label-only LIPID row denotes collective bilayer material without an exact whole-GO chemical identity. Resident PROTEIN class explicitly groups proteins without claiming one family/complex; UNKNOWN essentiality and separate SBP1 row are compatible with native class policy.

### Named examples and unresolved exact family grounding

grounding: unknown. Targets: GO:0020036.

MAHRP1 fragment and SBP1 unreviewed entries are identity examples, not complete experimental constructs. A single-accession204 and mismatched automatic InterPro family hit do not certify no family or justify a forced grounding; retain existing bounded family TODO.

### Species, host and qualitative stage prevalence

scope: supported. Targets: GO:0020036.

Pf5833 and isolate3D7 identities verify. Cooke uses3D7-infected human erythrocytes; broad COMMON asexual-stage wording remains qualitative. Rodent antibody conservation observations are not substituted for exact Pf genetics or all-species universal morphology.

### Trafficking versus precise molecular mechanism

evidence: supported. Targets: GO:0020036.

Cooke SBP1 loss retains PfEMP1 at clefts and complementation restores surface display/adhesion; Spycher MAHRP1 genetic effects are a distinct intervention. Neither guarantees direct SBP1-PfEMP1 binding, a complete transport pathway, or absence of clefts on protein loss.

### Five descriptive trafficking/localization edges

graph: supported. Targets: GO:0020036.

All five NONMECHANISTIC edges retain membrane/cohort containment and source-supported SBP1 trafficking/host surface-display context; direct binding, precise transport chemistry and organelle-formation necessity are not asserted. Component_refs resolve and descriptive graph scope stays bounded.

### Bilayer constitution and protein necessity

evidence: unknown. Targets: GO:0020036.

Collective membrane material is constitutional to the membranous structure; no individual lipid-species removal experiment is implied. SBP1 knockout clefts persist and resident protein UNKNOWN essentiality is conservative; transport necessity is not identical to structure-formation necessity.

### Canonical genetic-study citation placement

provenance: concern. Targets: GO:0020036.

Canonical note combines SBP1 and MAHRP1 genetic studies under sole Cooke2006 reference. Cooke is SBP1; Spycher2008 is MAHRP1. Preserve inherited F1 and scope-corrective action without changing the underlying supported biological claims.

### Exact whole microneme, boundaries and synonyms

identity: supported. Targets: GO:0020009.

GO0020009/related sarconeme synonym, GO0043231 ancestry, apical-complex parthood and distinct membrane/lumen child identities agree. Whole organelle is not identical to its molecular lipid material or lumen.

### New M2AP accession and separate RH experiment

grounding: supported. Targets: GO:0020009.

S8GDJ1 is UNREVIEWED ME49 M2AP with ORF TGME49_214940 and matching protein name; no formal primary geneName field is certified. Native identity and automatic signal peptide do not establish causality. Primary Huynh abstract/body independently support soluble M2AP partnering with transmembrane MIC2 in RH-derived experiments; ME49 is a representative, not the exact experimental construct.

### Whole-membrane GO identity on a LIPID constituent

grounding: concern. Targets: GO:0020009.

LIPID component microneme_membrane currently uses whole membrane GO0033163. Preserve whole-membrane has_part and structural node, but separate molecular material identity from the cellular boundary; inherited major F1 remains. No new lipid species or removal requirement is invented.

### Heterogeneous adhesins and legitimate complex node type

grounding: supported. Targets: GO:0020009.

MIC1/MIC2/AMA1 is explicitly heterogeneous, which native family-or-class policy allows. MIC2-M2AP is a named PROTEIN_COMPLEX component. Exact CausalNode schema lines845–846 explicitly permits protein complexes within GENE_OR_PROTEIN; this node type is not a confirmed defect and is not automatically retyped STRUCTURE. Neither a universal family nor exact complex stoichiometry is inferred.

### Representative identities and evidence-code limits

grounding: supported. Targets: GO:0020009.

MIC1/O00834 and AMA1/B6KAM0 are reviewed; MIC2/S8F9G8 and M2AP/S8GDJ1 unreviewed. Current MIC1/AMA1 source-linked location/shedding evidence is checked against complete primary abstracts, while predicted topology and automatic annotations stay distinct. Different species/VEG/ME49 representatives are not silently equated with RH experimental constructs.

### Phylum/subset and exact strain scopes

scope: supported. Targets: GO:0020009.

Eukaryota RARE and Apicomplexa COMMON are explicitly qualitative and stage/lineage-dependent. Tg species/VEG/ME49 identities verify; Huynh2006 conditional MIC2 work is RH-derived with HFF culture. No universal microneme composition or all-stage invasion role follows.

### Secretion, adhesion and invasion evidence

evidence: supported. Targets: GO:0020009.

1997 complete primary abstract supports ordered secretion; Huynh primary abstract/body support MIC2-M2AP trafficking and reduced attachment/invasion; Brown complete primary abstract supports in vitro PKG/cGMP-dependent secretion at its actual stimulus context. Residual invasion, distinct gliding modes and retained other microneme cargos prevent absolute formation-necessity claims.

### Two over-specific whole-cargo lumen endpoints

graph: concern. Targets: GO:0020009.

MIC2 and AMA1 span a membrane and have cytoplasmic portions; soluble M2AP/adhesive domains do not make the full complex/cohort entirely luminal. The two whole-entity lumen edges retain inherited F2; descriptions already support whole-organelle localization. Narrow endpoint or explicitly represent portions without inventing detailed orientation for every member.

### Remaining six mechanistic graph edges

graph: supported. Targets: GO:0020009.

Correct whole-organelle membrane/lumen parthood and PKG/exocytosis/cargo-release/complex-invasion/cohort-support relations match stated source scopes. The two lumen endpoints are separately flagged; no absolute requirement or entire fusion machinery is certified by simplified aggregate edges.

### Constitutional membrane and protein formation requirements

evidence: unknown. Targets: GO:0020009.

Bilayer material is constitutional but its present whole-GO chemical grounding remains defective. MIC2/M2AP intervention changes trafficking/invasion, while other cargos persist and residual invasion remains; UNKNOWN protein essentiality is not converted into universal organelle-formation necessity.

### Multiple study clauses under a 1997 source

provenance: concern. Targets: GO:0020009.

Canonical PMID9208224 supports sequential secretion, not later MIC2-M2AP genetic work and PKG experiments. Those sources are present elsewhere and verified at explicit tiers; retain inherited F3, scope-correct each clause, and preserve Tg/RH context.

### Family TODO and bounded complex census

completeness: unknown. Targets: GO:0020009.

MIC1/AMA1 domain/family xrefs do not ground the entire heterogeneous cohort; M2AP beta-domain does not identify a whole complex. Existing TODO is retained without a guessed identifier. Inventory is representative, not a complete all-stage complex or microneme proteome.

### Exact compartment identity and boundary topology

identity: supported. Targets: GO:0034494.

GO0034494 is the enclosed volume, with organelle-lumen is_a ancestry and whole-microneme parthood; membrane remains a boundary rather than a lumen constituent.

### Taxonomic and experimental scope

scope: supported. Targets: GO:0034494.

Apicomplexa COMMON is qualitative and stage/lineage-qualified; canonical T.gondii sequential secretion is supported by the complete1997 primary abstract. Review synthesis supplies broad topology/cargo context without asserting universal composition or exact all-strain mechanism.

### Storage/release and exocytosis scope

evidence: supported. Targets: GO:0034494.

Temporary lumen cargo storage/release is supported at soluble cargo/adhesive-domain scope. This generic statement does not itself place an entire transmembrane complex in the lumen and does not inherit the separate whole-record F2.

### Sparse contents/material scope

grounding: supported. Targets: GO:0034494.

No molecular components are asserted. The internal volume is not grounded to a whole membrane or a specific protein; no undisclosed complete cargo inventory is certified.

### Every descriptive boundary graph edge

graph: supported. Targets: GO:0034494.

Two NONMECHANISTIC edges correctly express lumen parthood and membrane enclosure; no whole-complex luminal topology is asserted.

### Existing discussion and intentionally sparse inventory

completeness: supported. Targets: GO:0034494.

Existing boundary/material discussion is interpreted at its actual target only. Sparse molecular inventory, empty native typed-node checks and body-access limits remain explicit; no other maintained-record/category issue is disposed by inference.

### Exact compartment identity and boundary topology

identity: supported. Targets: GO:0033163.

GO0033163 is the complete surrounding bilayer, with organelle-membrane is_a ancestry and whole-microneme parthood; the lumen and organelle stay distinct.

### Taxonomic and experimental scope

scope: supported. Targets: GO:0033163.

Apicomplexa COMMON is qualitative and stage/lineage-qualified; canonical T.gondii sequential secretion is supported by the complete1997 primary abstract. Review synthesis supplies broad topology/cargo context without asserting universal composition or exact all-strain mechanism.

### Storage/release and exocytosis scope

evidence: supported. Targets: GO:0033163.

Membrane boundary and regulated release context are supported; the graph attributes exocytosis support to the whole microneme, not an isolated bilayer as sufficient molecular machinery. No exact fusion-protein census or universal pathway is asserted.

### Sparse contents/material scope

grounding: supported. Targets: GO:0033163.

The LIPID row is reviewed-label-only collective bilayer material, without the whole-GO chemical grounding error in the whole record. ESSENTIAL is constitutional material scope, not tested necessity of a specific lipid species; existing exact-lipid TODO remains open.

### Every descriptive boundary graph edge

graph: supported. Targets: GO:0033163.

Three NONMECHANISTIC edges retain membrane parthood, lumen enclosure and whole-microneme exocytosis support. Structural-to-material component_ref is bounded by its collective material label; no molecular-equivalence or independent-bilayer causal sufficiency is asserted.

### Existing discussion and intentionally sparse inventory

completeness: supported. Targets: GO:0033163.

Existing boundary/material discussion is interpreted at its actual target only. Sparse molecular inventory, empty native typed-node checks and body-access limits remain explicit; no other maintained-record/category issue is disposed by inference.

### Current scoped scientific verdict

completeness: concern. Targets: GO:0020036.

needs_curation: 1 exact inherited findings remain, with no additional confirmed scientific finding. Stale accession additions are substantively refreshed without changing records.

### Current scoped scientific verdict

completeness: concern. Targets: GO:0020009.

needs_curation: 3 exact inherited findings remain, with no additional confirmed scientific finding. Stale accession additions are substantively refreshed without changing records.

### Current scoped scientific verdict

completeness: supported. Targets: GO:0034494.

pass_with_limitations: stated source tiers support current bounded identity/topology/function. Empty protein inventory and access/necessity limits prevent an unqualified pass; no confirmed curation finding.

### Current scoped scientific verdict

completeness: supported. Targets: GO:0033163.

pass_with_limitations: stated source tiers support current bounded identity/topology/function. Empty protein inventory and access/necessity limits prevent an unqualified pass; no confirmed curation finding.

### Native accession and causal-node coverage

schema: supported. Targets: GO:0044227.

Actual maintained inventory has 3 protein_examples and 1 typed GENE_OR_PROTEIN nodes. Two reviewed and one unreviewed Bath accession; pMMO component_ref has native COVERED status. This is identity/symbol coverage, not membership/necessity or exact copper mechanism.

### Historical pair, current bytes and optional fields

schema: supported. Targets: GO:0044227.

Original native pair validates and exact rendered Markdown agrees; all historical hashes match. Current stale accession delta was independently refreshed. PROPOSED status retained. No images, datasets or measured physical-property assertions require assessment in this target.

### Native accession and causal-node coverage

schema: supported. Targets: GO:0031040.

Actual maintained inventory has 0 protein_examples and 0 typed GENE_OR_PROTEIN nodes. Empty native accession/typed-node coverage does not certify all narrative claims.

### Historical pair, current bytes and optional fields

schema: supported. Targets: GO:0031040.

Original native pair validates and exact rendered Markdown agrees; all historical hashes match. Current target equals frozen original. PROPOSED status retained. No images, datasets or measured physical-property assertions require assessment in this target.

### Native accession and causal-node coverage

schema: supported. Targets: cellstructuremech:microsporidian_posterior_vacuole.

Actual maintained inventory has 0 protein_examples and 0 typed GENE_OR_PROTEIN nodes. Empty native accession/typed-node coverage does not certify all narrative claims.

### Historical pair, current bytes and optional fields

schema: supported. Targets: cellstructuremech:microsporidian_posterior_vacuole.

Original native pair validates and exact rendered Markdown agrees; all historical hashes match. Current target equals frozen original. PROPOSED status retained. No images, datasets or measured physical-property assertions require assessment in this target.

### Exact organelle versus membrane enzyme

identity: supported. Targets: GO:0044227.

GO0044227 and its exact aliases denote the membrane-bounded methane compartment; pMMO is a constituent complex rather than the record identity.0043231 is correct broader parent; no imported whole-enzyme or chemical grounding.

### Collective bilayer and pMMO trimer

grounding: supported. Targets: GO:0044227.

LIPID constituent describes collective inner-derived ICM bilayer; ESSENTIAL applies to that boundary material, not a specific lipid species. pMMO PROTEIN_COMPLEX is a trimer of three PmoA/B/C heterotrimers; UNKNOWN necessity retained, no exact complex CURIE invented. Native graph enum explicitly admits protein complexes.

### Stale pmoC1 addition substantively reassessed

provenance: supported. Targets: GO:0044227.

Q603F1 accession, submission label, primary pmoC1 name,243233Bath and UNREVIEWED status agree. Both locus names are retained as authority context; record makes no unique-locus claim. Exact pmoC1 resolves the entry despite empty exact pmoC query. Identity-only role avoids localization/necessity inflation. Original reviewed-only pmoC limitation remains truthful historically.

### Reviewed examples and source attribution

provenance: supported. Targets: GO:0044227.

Q607G3 andG1UBD1 primary names, aliases, taxon/status and cited native membrane evidence agree. Two genomic copy rows are not two distinct reviewed accessions. Smith2011 primary subject is Methylocystis strainM with updated Bath model; record attributes a UniProt evidence link, not a new Bath localization experiment.

### Exact Bath canonical example and broader subset

scope: supported. Targets: GO:0044227.

Zhu copper-replete Bath cells directly support canonical example243233; Whiddon main20Z plus other type-I species provide separately scoped membrane context, not interchangeable strain evidence. Broad bacterial RARE is qualitative subset language, not prevalence measurement or all-methanotroph obligation.

### All seven topology/assembly/chemistry edges

graph: supported. Targets: GO:0044227.

ICM boundary and native pMMO arrays, methane oxidation to methanol and initial catabolic step are supported. Invagination is explicitly an interpretation in evidence note; static continuity alone is not complete biogenesis proof. Graph does not claim array packing alone increases activity, exact active-site location, obligatory MDH complex or PmoB salt-bridge sufficiency.

### Methane chemistry and independent expression source

evidence: supported. Targets: GO:0044227.

GO0046188 and primary activity assays support pMMO first oxidative step. Stolyar complete abstract supports only its narrow transcript/gene-fusion note for two Bath gene clusters; unsupported full-body exact-copy conclusions are not inferred.

### Protein/metabolism trigger and exact catalogue scope

evidence: supported. Targets: GO:0044227.

pmoA/B/C, three native accessions and methane catabolism require applicability assessment despite absence of expression-module claims. Fresh official catalogue has no matched Methylococcus/Bath host; unrelated Bacteria entries are not proxies. Historical runner unavailable is separate from current bounded source fallback.

### Bounded primary access and experimental limits

evidence: unknown. Targets: GO:0044227.

Zhu/Whiddon selected bodies and relevant captions were read, not source figure pixels/raw data. Stolyar body routes failed; full abstract only. Three historical localization PMIDs reviewed at abstract/native-authority tier. Exact copper chemistry, full biogenesis and expression-network membership not newly certified.

### Ciliate micronucleus and nucleus parent

identity: supported. Targets: GO:0031040.

GO0031040 definition and0005634 parent agree; record denotes diploid ciliate germline organelle, not chromosome material or somatic macronucleus. Definition genic-transcription wording matches current GO; mature Tetrahymena graph explicitly excludes meiosis/zygote/MAC rearrangement.

### Germline chromosomal DNA versus chromosome structure

grounding: supported. Targets: GO:0031040.

DNA constituent is collective germline genetic material; ESSENTIAL at that scope does not claim every sequence is required or nuclear-envelope assembly cannot persist without DNA. GO0000228 denotes whole chromosome and is correctly not misused for DNA molecules. Optional exact SO grounding remains unresolved, not an established missing-required-ID issue.

### Tetrahymena species and SB210 preparation

scope: supported. Targets: GO:0031040.

Taxon5911 is T.thermophila; source Methods validates all five SB210 chromosomes before isolating MICs and sequencing. Qualitative COMMON concerns this nuclear dimorphism, not every life-cycle stage or a quantitative prevalence. No other ciliate strain substituted.

### Mature germline genome maintenance

evidence: supported. Targets: GO:0031040.

Source supports diploid transcriptionally silent germline nuclear compartment and transmission through sexual generations. Descriptive record does not erase developmental noncoding transcription or generalize SB210 assembly results to gapless assemblies in every ciliate.

### Four descriptive containment/transmission edges

graph: supported. Targets: GO:0031040.

DNA is housed in MIC, constitutes germline genome, MIC preserves it and genetic material is transmitted during sexual reproduction. Five chromosome-length superassemblies are source-supported but retain assembly gaps; NONMECHANISTIC scope does not imply actual rearrangement chronology or DNA alone suffices for reproduction.

### Optional grounding and earlier correction remain scoped

consistency: supported. Targets: GO:0031040.

Current GO0019953 final process agrees. Historical issue1290 resolution is merely recorded history; no new terminal disposition of an unfrozen earlier review. Exact DNA-grounding TODO is not elevated into a required curation finding.

### Genic-transcription/genome program triggers applicability

evidence: supported. Targets: GO:0031040.

Complete definition/function/graph include genic transcription, germline genome maintenance and sexual transmission; explicit expression-module-only exclusion bypasses required assessment. Fresh catalogue has no Tetrahymena/ciliate host. No foreign microbial dataset query or biological-absence conclusion follows.

### Source and assembly limits

evidence: unknown. Targets: GO:0031040.

Selected Hamilton Introduction/assembly/Methods were inspected without raw-read reassembly or figure-pixel review. Current authority and mature scope support claims; no exhaustive whole-life-cycle transcription survey or exhaustive SO search performed.

### Posterior vesicle distinct from polar tube/peroxisome

identity: supported. Targets: cellstructuremech:microsporidian_posterior_vacuole.

Minted membrane-bounded posterior organelle identity matches primary spore morphology; exact polar tube0044099 remains a distinct node. First25 QuickGO posterior-vacuole matches offered no exact identity; no exhaustive absence claim or broader vacuole substitution. Findley biochemical analogy is not imported as peroxisome identity.

### Bounded membrane material and unresolved mechanism

grounding: supported. Targets: cellstructuremech:microsporidian_posterior_vacuole.

Single limiting membrane observed by2D TEM supports collective LIPID boundary; UNKNOWN molecular necessity retained. Exact lipids, osmolytes and driving proteins are explicitly unresolved; empty optional inventory alone is not a scientific defect and source-specific catalase observations are not universalized.

### Infectious spores and species-specific observations

scope: supported. Targets: cellstructuremech:microsporidian_posterior_vacuole.

6029Microsporidia and6039V.necatrix identities agree. S.lophii,A.algerae,E.aedis andV.necatrix are separately scoped observations; COMMON is qualitative infectious-spore context, not every vegetative stage. Secondary chapter abstract has no quantitative posterior-vacuole prevalence claim.

### Source modality and imaged-object mismatch

evidence: concern. Targets: cellstructuremech:microsporidian_posterior_vacuole.

Inherited F1 remains: Jaroenlak2020 SBFSEM plus2D TEM is incorrectly called electron tomography; Sharma2024 firing dynamics are light microscopy while cryoET excluded spores and sampled tube regions. Correct source notes without rejecting supported organelle occurrence or membrane topology.

### Proposed driver overclaimed in final edge

evidence: concern. Targets: cellstructuremech:microsporidian_posterior_vacuole.

Inherited F2 remains: final enters-edge description/evidence upgrades Troemel2015 apparent/likely vacuolar pushing to unqualified pushes/drives. Other descriptions already retain implication. Restore qualification or describe only observed cargo passage; no isolated-force mechanism proven.

### Remaining four edges and temporal context

graph: supported. Targets: cellstructuremech:microsporidian_posterior_vacuole.

Membrane encloses vesicle, posterior location, expansion during firing and separately qualified pushing interpretation agree with source scopes. Sharma light-dynamic imaging supports the qualified preceding note, not a false cryoET movie. Final edge correction is precisely F2, not rejection of temporal sequence/cargo passage.

### Genuine sparse physical/physiological exclusion

evidence: not_applicable. Targets: cellstructuremech:microsporidian_posterior_vacuole.

Complete record asserts boundary topology, position, swelling and proposed physical pressure/cargo movement; no positively specified gene, protein, regulator, molecular pathway, stress-response trait or transcriptomic dataset is asserted. Composition is explicitly unresolved. Generic firing alone and molecular details merely present in cited papers do not create a record-level adapter trigger. Original exclusion can stand with this precise rationale; not counted as a bundle defect.

### Historical boundary repair and live optional TODO

consistency: supported. Targets: cellstructuremech:microsporidian_posterior_vacuole.

Current membrane component_ref is on boundary node, not organelle. Historical issue778 resolution not re-certified beyond current representation, and optional composition TODO is not automatically an untracked request-curation finding. Two explicit inherited findings/actions retained exactly.

### Body/abstract/pixel and mechanism boundaries

evidence: unknown. Targets: cellstructuremech:microsporidian_posterior_vacuole.

Findley PDF selected main pages and Jaroenlak/Sharma selected genuine bodies/captions read; Troemel main body read but videos not replayed. No source figure pixels or raw data reviewed for this target.2022 chapter abstract only; phylum prevalence not measured. Microscopy and causal-scope defects are established from explicit Methods/text, not absence of access.

### Exact structure identity and boundaries

identity: supported. Targets: GO:0030061.

Whole crista is an inward IMM fold; junction is its connection to the boundary membrane. Exact GO identity/part_of and anatomical has_part interpretation remain distinct.

### Taxon identities and experimental strains

scope: supported. Targets: GO:0030061.

Exact species/strain identities agree; source-specific W303, BY/S288C-derived and other named yeast experimental strains are not all equated to unmodified S288C. COMMON/VARIABLE are qualitative; no quantitative prevalence survey performed.

### Original pairs and native protein scope

schema: supported. Targets: GO:0030061.

Original native validation/render and frozen source hashes passed. No component protein examples and zero GENE_OR_PROTEIN nodes; complex STRUCTURE actors are outside the typed-node denominator.

### Present but unsupported expression-only exclusion

provenance: concern. Targets: GO:0030061.

Original check row is present, not omitted. Its lack-of-expression rationale misses named architecture/respiration or MDC protein, stress and intervention pathways, which trigger applicability assessment under native policy.

### Current exact-host catalogue fallback

evidence: not_applicable. Targets: GO:0030061.

Fresh full official catalogue has no matching yeast/eukaryotic experimental host. No unmatched organism proxy or downstream module claim is warranted. Historical runner failure remains separately dated/unavailable, not a new run.

### Complete record, optional enrichment and scope

completeness: supported. Targets: GO:0030061.

Entire target and original scientific findings/actions read. Optional inventories, exact molecular additions and raw experiments are not invented; native PROPOSED status and history remain unchanged. No neighboring/grouped/category issue is terminally resolved.

### Exact structure identity and boundaries

identity: supported. Targets: GO:0044284.

Junction is a subcellular contact region, not MICOS itself; direct is_a contact-site and IMM part_of authority relations agree.

### Taxon identities and experimental strains

scope: supported. Targets: GO:0044284.

Exact species/strain identities agree; source-specific W303, BY/S288C-derived and other named yeast experimental strains are not all equated to unmodified S288C. COMMON/VARIABLE are qualitative; no quantitative prevalence survey performed.

### Original pairs and native protein scope

schema: supported. Targets: GO:0044284.

Original native validation/render and frozen source hashes passed. No component examples and zero GENE_OR_PROTEIN nodes after MICOS retyping. STRUCTURE-node P36112 is skipped by native protein verification and independently verified from fresh authority JSON.

### Present but unsupported expression-only exclusion

provenance: concern. Targets: GO:0044284.

Original check row is present, not omitted. Its lack-of-expression rationale misses named architecture/respiration or MDC protein, stress and intervention pathways, which trigger applicability assessment under native policy.

### Current exact-host catalogue fallback

evidence: not_applicable. Targets: GO:0044284.

Fresh full official catalogue has no matching yeast/eukaryotic experimental host. No unmatched organism proxy or downstream module claim is warranted. Historical runner failure remains separately dated/unavailable, not a new run.

### Complete record, optional enrichment and scope

completeness: supported. Targets: GO:0044284.

Entire target and original scientific findings/actions read. Optional inventories, exact molecular additions and raw experiments are not invented; native PROPOSED status and history remain unchanged. No neighboring/grouped/category issue is terminally resolved.

### Exact structure identity and boundaries

identity: supported. Targets: cellstructuremech:mitochondrial_derived_compartment.

Local MDC identity denotes yeast OMM-derived multilamellar domains, distinct from generic MDVs, protein aggregates or universal closed vesicles. Broad organelle parent is not substituted as exact identity.

### Taxon identities and experimental strains

scope: supported. Targets: cellstructuremech:mitochondrial_derived_compartment.

Exact species/strain identities agree; source-specific W303, BY/S288C-derived and other named yeast experimental strains are not all equated to unmodified S288C. COMMON/VARIABLE are qualitative; no quantitative prevalence survey performed.

### Original pairs and native protein scope

schema: supported. Targets: cellstructuremech:mitochondrial_derived_compartment.

Original native validation/render and frozen source hashes passed. Three reviewed component examples TOM70/P07213, TOM71/P38825 and DNM1/P54861 in tax559292; zero GENE_OR_PROTEIN nodes because intervention/capability nodes are STATE.

### Present but unsupported expression-only exclusion

provenance: concern. Targets: cellstructuremech:mitochondrial_derived_compartment.

Original check row is present, not omitted. Its lack-of-expression rationale misses named architecture/respiration or MDC protein, stress and intervention pathways, which trigger applicability assessment under native policy.

### Current exact-host catalogue fallback

evidence: not_applicable. Targets: cellstructuremech:mitochondrial_derived_compartment.

Fresh full official catalogue has no matching yeast/eukaryotic experimental host. No unmatched organism proxy or downstream module claim is warranted. Historical runner failure remains separately dated/unavailable, not a new run.

### Complete record, optional enrichment and scope

completeness: supported. Targets: cellstructuremech:mitochondrial_derived_compartment.

Entire target and original scientific findings/actions read. Optional inventories, exact molecular additions and raw experiments are not invented; native PROPOSED status and history remain unchanged. No neighboring/grouped/category issue is terminally resolved.

### All current nonmechanistic topology and architecture edges

graph: supported. Targets: GO:0030061.

MICOS maintenance, junction connections and (whole crista) ATP-synthase ridge shaping/respiratory support have bounded yeast primary and GO support. MICOS subcomplex-localization inference uses marker adjacency; direct junction immuno-EM failed. Detailed assembly/cardiolipin/remodeling mechanism is not asserted.

### General lineage and taxon constraint limits

scope: unknown. Targets: GO:0030061.

Exact GO responses contain no explicit taxon constraints; inspected secondary passage does not establish every reduced anaerobic-organelle exception. Eukaryotic mitochondrial context is supported, but no exhaustive lineage/absence survey was done. Unknown scope is not refutation.

### All current nonmechanistic topology and architecture edges

graph: supported. Targets: GO:0044284.

MICOS maintenance, junction connections and (whole crista) ATP-synthase ridge shaping/respiratory support have bounded yeast primary and GO support. MICOS subcomplex-localization inference uses marker adjacency; direct junction immuno-EM failed. Detailed assembly/cardiolipin/remodeling mechanism is not asserted.

### General lineage and taxon constraint limits

scope: unknown. Targets: GO:0044284.

Exact GO responses contain no explicit taxon constraints; inspected secondary passage does not establish every reduced anaerobic-organelle exception. Eukaryotic mitochondrial context is supported, but no exhaustive lineage/absence survey was done. Unknown scope is not refutation.

### Complex roles and formation necessity

grounding: supported. Targets: GO:0030061.

MICOS remains associated architecture machinery with UNKNOWN necessity; resident ATP synthase is a constituent with UNKNOWN necessity. Perturbed lamellar morphology does not prove every complex/subunit is universally necessary for any inward fold. Source-neutral complex abstractions are valid; optional subunits/lipids are not a consequential omission.

### Substantive MICOS actor retyping refresh

provenance: supported. Targets: GO:0044284.

GO0061617 correctly denotes MICOS as STRUCTURE; P36112 separately verifies a Mic60 member and does not identify the whole complex. Current maintenance edge remains source-supported. Closed2419 is historical context, not disposition of its whole group or of the inherited microscopy attribution.

### Inherited microscopy-method attribution

evidence: concern. Targets: GO:0044284.

Friedman2015 Methods report fixed resin sections/TEM plus fluorescence. Current canonical example wrongly calls this tomography; inherited stable-key finding remains open without refuting yeast MICOS biology.

### Five constituent and associated-machinery classes

grounding: supported. Targets: cellstructuremech:mitochondrial_derived_compartment.

Heterogeneous lipid bilayers and cytosolic cargo are appropriately label-only. Tom70/Tom71 are sampled cargo with UNKNOWN necessity. Dnm1 is DISPENSABLE associated release machinery in bounded ConcA formation assay. Regulators and contact-site machinery are not automatically canonical constituents; no invariant stoichiometry asserted.

### Exact three examples and bounded family searches

grounding: supported. Targets: cellstructuremech:mitochondrial_derived_compartment.

TOM70/TOM71/DNM1 names/loci/review status/S288C identity and one-reviewed-hit searches agree. Tom70 exact IPR005687 is present. Tom71 integrated endpoint returns only TPR classes; Dynamin IPR022812 is broader than mitochondrial Dnm1. No arbitrary family is transferred from similarity or generic domain.

### Revised cargo and conditional routing

scope: supported. Targets: cellstructuremech:mitochondrial_derived_compartment.

2024 tag-orientation/localization results revise2016 carrier model: functional IMM carriers are not routine cargo, assembled core TOM proteins are not uniformly enriched. Selected OMM cargo and partial protection are supported. ConcA-associated vacuolar routing is distinct from initial formation and not universal fate.

### Nine assay-bounded intervention/capability edges

graph: concern. Targets: cellstructuremech:mitochondrial_derived_compartment.

Rap induction, selected-cargo/cytosol sequestration, MMM1/GEM1 effects, DNM1 release and PSD1/CRD1 directions are supported with source conditions and partiality. Tom70/Tom71 edge has inherited assay-attribution mismatch: sole cited Hughes2016 experiment is ConcA2h in dnm1Δ, not rapamycin. No direct-binding/universal linear pathway claimed.

### Actual pixels, measurement conditions and license

evidence: supported. Targets: cellstructuremech:mitochondrial_derived_compartment.

Figure1C0.41µm/n104 and FigureS1C0.36µm/n49 apply to spherical Rap200nM or ConcA500nM2h MDCs. Both axes read µm; initial glyph-misreading hypothesis was rejected after independent challenge and own original-detail reinspection. Figure1 mixed modality/attribution/scale bars/yeast and link-only CC BY-NC-SA4 are correct. TEM section thickness is not diameter.

### Preserved study-specific lipid discrepancy

evidence: supported. Targets: cellstructuremech:mitochondrial_derived_compartment.

2020 tested lipid mutants did not impair formation;2024 shows CL suppression and PE-dependent promotion/partial bypass. Record correctly retains discrepancy without invented reconciliation, isolated-MDC composition or universal enzyme necessity.

### 2026 models and actual access tiers

evidence: unknown. Targets: cellstructuremech:mitochondrial_derived_compartment.

Both exact2026 DOI/PMID identities and official reviewed-preprintv1 metadata are verified. First PMC artifact is an availability stub; second Discussion explicitly cannot isolate MDC-specific fitness/buffering contribution. Publisher Results not certified read. Historical access notes remain historical; these models are not promoted into canonical graph/components.

### Complete frozen-input comparison and bounded refresh

provenance: supported. Targets: GO:0020036, GO:0044227, GO:0020009, GO:0034494, GO:0033163, GO:0031040, cellstructuremech:microsporidian_posterior_vacuole, GO:0030061, GO:0044284, cellstructuremech:mitochondrial_derived_compartment.

4 of ten original target hashes differ from current main. The changed content is substantively reassessed in the target-specific assessments; original observations remain historical and unchanged. All current target and used context bytes are frozen.

## Findings

### septin-maurer_s_cleft-F1: Align the canonical genetic-study note with its cited paper

minor / open / confirmed; issue key: maurer-canonical-genetic-study-attribution.

The canonical note attributes genetic testing of both SBP1 and MAHRP1 to its sole Cooke2006 citation. Cooke tests SBP1 deletion/complementation; the MAHRP1 genetic test is in Spycher2008, already listed elsewhere in the record.

### septin-microneme-F1: Separate the lipid constituent from the complete membrane identity

major / open / confirmed; issue key: microneme-lipid-whole-membrane-grounding.

The microneme_membrane LIPID component uses GO0033163, the entire microneme membrane, as molecular grounding; the graph membrane node also links to that component. The frozen schema distinguishes molecular lipid identity from a whole cellular structure.

### septin-microneme-F2: Qualify lumen localization of transmembrane adhesin complexes

minor / open / confirmed; issue key: microneme-transmembrane-cargo-lumen-qualification.

The whole MIC2–M2AP complex and MIC1/MIC2/AMA1 cohort are linked as residing in the lumen. MIC2 and AMA1 span membranes and have cytosolic domains; the whole complex is not identical to its luminal adhesive domains or soluble M2AP.

### septin-microneme-F3: Match the canonical example clauses to their supporting studies

minor / open / confirmed; issue key: microneme-canonical-multiple-study-attribution.

The sole canonical PMID9208224 supports sequential secretion, but its note also names MIC2–M2AP and PKG-regulated exocytosis experiments supplied by other papers already present in the record.

### plaque-t6-F1: Correct microscopy descriptions and their observational scope

minor / open / confirmed; issue key: posterior-vacuole-microscopy-source-scope.

Jaroenlak2020 used serial block-face SEM and 2D TEM, whereas the component evidence note adds electron tomography. Sharma2024 used light microscopy for germination dynamics and cryoET for extruded tube segments; its Methods explicitly excluded spores from tilt-series collection. The canonical example note therefore overstates what was imaged by cryoET. This does not refute V.necatrix organelle occurrence or the supported membrane topology.

### plaque-t6-F2: Retain the source’s qualification of the pushing mechanism

minor / open / confirmed; issue key: posterior-vacuole-cargo-causal-qualification.

The final enters edge asserts without qualification that vacuole expansion pushes and drives sporoplasm passage. The cited Troemel2015 main text presents this as an interpretation of the video, with uncertain mechanism. Restore that epistemic scope, consistent with the record definition and preceding qualified edge; observed cargo entry is supported.

### micro-F1: Correct the imaging modality attributed to Friedman2015

minor / open / confirmed; issue key: mitochondrial-crista-junction-1.

The canonical example says the cited Friedman2015 study used electron tomography. Its electron-microscopy Methods specify fixed resin sections observed by transmission electron microscopy, alongside fluorescence. The paper remains relevant to yeast MICOS-dependent architecture; the incorrect modality is a bounded provenance error.

### micro-F2: Restore the cited Tom70/Tom71 experiment condition

minor / open / confirmed; issue key: mitochondrial-derived-compartment-1.

The Tom70/Tom71 double-deletion edge description calls the experiment rapamycin-induced, while its only cited source Hughes2016 Fig7C uses concanamycin A for2h in a dnm1Δ background. This conflicts with the graph scope promise that edges retain individual assay conditions. The source supports the dependency under ConcA, so this is a bounded attribution error rather than evidence that the dependency itself is false.

## Recommended Actions And Acceptance Checks

### septin-maurer_s_cleft-A1

In separately authorized curation, narrow the Cooke-linked canonical note to SBP1 or represent the MAHRP1 clause with the exact Spycher2008 supporting source.

- Cooke2006 is attached only to its SBP1 intervention and observed phenotype.
- Any retained MAHRP1 genetic-test clause has Spycher2008 claim-level support; preserve correct P. falciparum identity and differing intervention effects.

### septin-microneme-A1

In separately authorized curation, represent collective lipid material with justified chemical grounding or reviewed label-only status, and retain the complete membrane as a structural part without an invalid molecular equivalence.

- Retain GO0033163 for the whole membrane and correct has_part relation.
- A LIPID component no longer asserts GO0033163 as its chemical identity; any graph component_ref has a defensible material-to-boundary meaning.
- Do not invent microneme-specific lipid species or assembly requirements.

### septin-microneme-A2

In separately authorized curation, point the whole cohort/complex localization to the microneme or explicitly distinguish soluble/luminal portions from transmembrane and cytosolic domains.

- Whole MIC2–M2AP and transmembrane AMA1 are not represented as wholly soluble lumen contents.
- Preserve valid luminal M2AP/adhesive-domain context and source-supported microneme localization; do not infer detailed orientation for every cohort member.

### septin-microneme-A3

In separately authorized curation, narrow the canonical note to the1997 experiment or attach the separately verified complex and PKG studies to their respective clauses.

- The1997 citation is not the sole evidentiary support for later MIC2–M2AP or PKG experiments.
- Preserve correct Toxoplasma identity and actual RH-derived contexts.

### plaque-t6-A1

In separately authorized curation, Describe the actual microscopy modalities and imaged objects; support any direct V.necatrix posterior-vacuole example with an appropriately scoped primary source.

- Match source-specific species, microscopy modality, imaged object and causal certainty.
- Retain directly observed topology and cargo passage.
- Run focused native schema and strict checks after scientific curation.

### plaque-t6-A2

In separately authorized curation, Qualify the proposed vacuole-driven mechanism or restrict the enters edge to observed cargo passage, preserving the directly observed temporal relationship.

- Match source-specific species, microscopy modality, imaged object and causal certainty.
- Retain directly observed topology and cargo passage.
- Run focused native schema and strict checks after scientific curation.

### micro-A1

Replace the tomography attribution with the actually reported fluorescence and thin-section TEM/genetic analyses, or separately cite a genuine tomography study.

- Preserve the supported biological scope and source experimental conditions.
- Run focused native schema, strict and applicable graph/protein checks after separately authorized curation.

### micro-A2

Replace the rapamycin attribution with the actual ConcA/fission-deficient assay context, or cite and accurately delimit a direct rapamycin experiment. Preserve the conditional dependency and formation-versus-release distinction.

- Preserve the supported biological scope and source experimental conditions.
- Run focused native schema, strict and applicable graph/protein checks after separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| current-record-0 | data/structures/membrane_organelle/maurer_s_cleft.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 e8745451600446a168d2c417a41d1628fe36a02952f9d64157a9764e7ab44455; current SHA256 8eed10ce23b6b30eb30d69fc14e8686bc350a5906ac9b7fbe4b6601ebe3616a9. Changed record reassessed against current sources. |
| original-review-0 | reviews/structured/20261022T022231Z-maurer-s-cleft-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-1 | data/structures/membrane_organelle/methane_oxidizing_organelle.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 467cea27775a831c959b7a2e05a1f396a9ef026e2b1c012059a59d023570da3b; current SHA256 8d513f399ed2555737573ae9d0c888514408062fcd5f2ec60bc19bad9e93f2c8. Changed record reassessed against current sources. |
| original-review-1 | reviews/structured/20261022T022232Z-methane-oxidizing-organelle-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-2 | data/structures/membrane_organelle/microneme.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 12358b0b6b393cc14973846c2d86f59e3716f1b9d3513ff2914c3e6b28193cc9; current SHA256 8c260a40b26529407d136e11511c846d6554d975d54a3a45f444876aa0b51da8. Changed record reassessed against current sources. |
| original-review-2 | reviews/structured/20261022T022233Z-microneme-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-3 | data/structures/membrane_organelle/microneme_lumen.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 c40d221eea42af12fcb06a6a5dbcc7d3592f289ad31f52a275acad4d6666af38; current SHA256 c40d221eea42af12fcb06a6a5dbcc7d3592f289ad31f52a275acad4d6666af38. Record bytes unchanged since the original review. |
| original-review-3 | reviews/structured/20261022T022235Z-microneme-lumen-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-4 | data/structures/membrane_organelle/microneme_membrane.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 f3c40aeb98a8d3eec6950ea6a3875db63372a5e72c66a75130e4ec821f0dc4ad; current SHA256 f3c40aeb98a8d3eec6950ea6a3875db63372a5e72c66a75130e4ec821f0dc4ad. Record bytes unchanged since the original review. |
| original-review-4 | reviews/structured/20261022T022236Z-microneme-membrane-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-5 | data/structures/membrane_organelle/micronucleus.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 fe6086eb62e1499109082d20f9a25ff776a68482d0ab89253469f6f3bfcbb8c1; current SHA256 fe6086eb62e1499109082d20f9a25ff776a68482d0ab89253469f6f3bfcbb8c1. Record bytes unchanged since the original review. |
| original-review-5 | reviews/structured/20261022T022237Z-micronucleus-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-6 | data/structures/membrane_organelle/microsporidian_posterior_vacuole.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 db2c2e1271b64aa7037885eeb2f1e39c6e3ee5d769b83e8374ed96d2e768f6b8; current SHA256 db2c2e1271b64aa7037885eeb2f1e39c6e3ee5d769b83e8374ed96d2e768f6b8. Record bytes unchanged since the original review. |
| original-review-6 | reviews/structured/20261022T022238Z-microsporidian-posterior-vacuole-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-7 | data/structures/membrane_organelle/mitochondrial_crista.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 d7f734bbcd5e5af1c899f0c2034d2bc72656eaeb71d5861cf185613c65f4bda6; current SHA256 d7f734bbcd5e5af1c899f0c2034d2bc72656eaeb71d5861cf185613c65f4bda6. Record bytes unchanged since the original review. |
| original-review-7 | reviews/structured/20261022T022238Z-mitochondrial-crista-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-8 | data/structures/membrane_organelle/mitochondrial_crista_junction.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 fccd57bdf4448897c74fae433fbec5a596152571a8ad7e21034643d8d4379653; current SHA256 b994a1d51d584f4614c50fb97db455db7a6cf72b2f886da419fcbf3b77ba3adb. Changed record reassessed against current sources. |
| original-review-8 | reviews/structured/20261022T022239Z-mitochondrial-crista-junction-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-9 | data/structures/membrane_organelle/mitochondrial_derived_compartment.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 c7a83f3db0bb05a7016b5c3991e79bd21c9a6ec4f723335fc3a1d14864d1c5c8; current SHA256 c7a83f3db0bb05a7016b5c3991e79bd21c9a6ec4f723335fc3a1d14864d1c5c8. Record bytes unchanged since the original review. |
| original-review-9 | reviews/structured/20261022T022241Z-mitochondrial-derived-compartment-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| septin-review-policy | .claude/skills/review-yaml-record/SKILL.md; Whole-record assertions, structured sources and severity rubric | supports | Positive molecular/pathway assertions require a real applicability assessment; absence of expression claims alone is not an exemption. Keep source scope, uncertainty and original finding identity; record curation is separate. |
| septin-curation-policy | docs/CURATION.md; Structural components, molecular grounding and family-or-class guidance | supports | Whole assembled membranes are structures; a LIPID component denotes molecular material and cannot use a complete membrane identity as exact chemical grounding. Taxon-agnostic protein families OR classes are permitted. An optional example inventory is not automatically required for every generic class. |
| septin-schema-policy | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, ComponentTypeEnum and grounding contract | supports | Molecular components and whole structures have different identities. Label-only supported lipid material is possible without inventing exact chemical composition. PROTEIN enum prose is interpreted with explicit CURATION generic-class permission; no automatic complex assertion follows from a heterogeneous class. |
| septin-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Graph nodes, component correspondence, source scope and necessity | supports | Descriptive boundary graphs can remain NONMECHANISTIC; source-specific localization, molecular identity and organelle-formation necessity must not be conflated. |
| septin-protein-policy | .claude/skills/uniprot-protein-examples/SKILL.md; Step2 generic classes and native coverage report | supports | Generic class components are explicitly recognized. A zero-example inventory or NO_GENE_SYMBOLS node is a stated coverage limit, not proof that the protein class does not exist or that its members form one stable complex. |
| septin-record-maurer_s_cleft | data/structures/membrane_organelle/maurer_s_cleft.yaml; Complete current record at 61d3617ae8700b99198e2aaf01f3b2437933de6c | supports | Read all identity/boundaries, components/examples, taxa/canonical scopes, functions, bibliography, all graph nodes/edges, discussions and history. No maintained image, numeric physical-property, associated-trait or verbatim-snippet fields. |
| septin-original-maurer_s_cleft | reviews/structured/20261022T022231Z-maurer-s-cleft-audit/review.yaml; Complete original YAML and Markdown, frozen inputs/checks/assessments/findings/actions and access limits | supports | Historical observations remain historical; original artifacts are unchanged. Current target is stale and substantively reassessed. Exact inherited findings are retained where present; no other-target/category issue disposition follows. |
| septin-original-validation-maurer_s_cleft | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/adversary-septin/original-checks.json; Actual original native validate/render and historical target-hash verification | supports | Both native commands exit0; original Markdown matches deterministic render and historical target hash equals frozen input. |
| septin-native-maurer_s_cleft-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/maurer_s_cleft-uniprot-verify-receipt.json; Actual receipt; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/maurer_s_cleft-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0. Three UNREVIEWED example occurrences and three distinct accessions Q6V0W9,Q8I2G1,Q9NFF5; two COVERED GENE_OR_PROTEIN nodes. Q6V0W9 is a fragment. Native identity/coverage does not demonstrate accession-specific membership, complete composition, causality or formation necessity. |
| septin-native-maurer_s_cleft-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/maurer_s_cleft-uniprot-causal-receipt.json; Actual receipt; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/maurer_s_cleft-uniprot-causal.log SHA256 0ccd24fe81e43c2fc407db2d76bb5aa040c8ac2f3ddd67c4c60ff1b16ea135d3 | supports | Exit0. Three UNREVIEWED example occurrences and three distinct accessions Q6V0W9,Q8I2G1,Q9NFF5; two COVERED GENE_OR_PROTEIN nodes. Q6V0W9 is a fragment. Native identity/coverage does not demonstrate accession-specific membership, complete composition, causality or formation necessity. |
| septin-record-microneme | data/structures/membrane_organelle/microneme.yaml; Complete current record at 61d3617ae8700b99198e2aaf01f3b2437933de6c | supports | Read all identity/boundaries, components/examples, taxa/canonical scopes, functions, bibliography, all graph nodes/edges, discussions and history. No maintained image, numeric physical-property, associated-trait or verbatim-snippet fields. |
| septin-original-microneme | reviews/structured/20261022T022233Z-microneme-audit/review.yaml; Complete original YAML and Markdown, frozen inputs/checks/assessments/findings/actions and access limits | supports | Historical observations remain historical; original artifacts are unchanged. Current target is stale and substantively reassessed. Exact inherited findings are retained where present; no other-target/category issue disposition follows. |
| septin-original-validation-microneme | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/adversary-septin/original-checks.json; Actual original native validate/render and historical target-hash verification | supports | Both native commands exit0; original Markdown matches deterministic render and historical target hash equals frozen input. |
| septin-native-microneme-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/microneme-uniprot-verify-receipt.json; Actual receipt; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/microneme-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0. Five protein-example occurrences but four distinct accessions: MIC2/S8F9G8 occurs under both adhesin cohort and MIC2-M2AP complex. Two REVIEWED occurrences O00834/B6KAM0 and three UNREVIEWED occurrences S8F9G8 twice/S8GDJ1 once; two COVERED GENE_OR_PROTEIN nodes. Correct identity and symbol coverage do not prove complete complex stoichiometry, localization topology or causal necessity. |
| septin-native-microneme-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/microneme-uniprot-causal-receipt.json; Actual receipt; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/microneme-uniprot-causal.log SHA256 eb7a8d48aaebc612f3134392b96306cfc1973f5dedd06a3cfc8937855fdeb6b0 | supports | Exit0. Five protein-example occurrences but four distinct accessions: MIC2/S8F9G8 occurs under both adhesin cohort and MIC2-M2AP complex. Two REVIEWED occurrences O00834/B6KAM0 and three UNREVIEWED occurrences S8F9G8 twice/S8GDJ1 once; two COVERED GENE_OR_PROTEIN nodes. Correct identity and symbol coverage do not prove complete complex stoichiometry, localization topology or causal necessity. |
| septin-record-microneme_lumen | data/structures/membrane_organelle/microneme_lumen.yaml; Complete current record at 61d3617ae8700b99198e2aaf01f3b2437933de6c | supports | Read all identity/boundaries, components/examples, taxa/canonical scopes, functions, bibliography, all graph nodes/edges, discussions and history. No maintained image, numeric physical-property, associated-trait or verbatim-snippet fields. |
| septin-original-microneme_lumen | reviews/structured/20261022T022235Z-microneme-lumen-audit/review.yaml; Complete original YAML and Markdown, frozen inputs/checks/assessments/findings/actions and access limits | supports | Historical observations remain historical; original artifacts are unchanged. Current target is byte-unchanged. Exact inherited findings are retained where present; no other-target/category issue disposition follows. |
| septin-original-validation-microneme_lumen | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/adversary-septin/original-checks.json; Actual original native validate/render and historical target-hash verification | supports | Both native commands exit0; original Markdown matches deterministic render and historical target hash equals frozen input. |
| septin-native-microneme_lumen-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/microneme_lumen-uniprot-verify-receipt.json; Actual receipt; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/microneme_lumen-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0. Zero protein examples and zero typed GENE_OR_PROTEIN nodes; no represented UniProtKB graph xrefs. Exit0 validates an empty identifier inventory, not the complete secretion/pathway narrative. |
| septin-native-microneme_lumen-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/microneme_lumen-uniprot-causal-receipt.json; Actual receipt; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/microneme_lumen-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Exit0. Zero protein examples and zero typed GENE_OR_PROTEIN nodes; no represented UniProtKB graph xrefs. Exit0 validates an empty identifier inventory, not the complete secretion/pathway narrative. |
| septin-record-microneme_membrane | data/structures/membrane_organelle/microneme_membrane.yaml; Complete current record at 61d3617ae8700b99198e2aaf01f3b2437933de6c | supports | Read all identity/boundaries, components/examples, taxa/canonical scopes, functions, bibliography, all graph nodes/edges, discussions and history. No maintained image, numeric physical-property, associated-trait or verbatim-snippet fields. |
| septin-original-microneme_membrane | reviews/structured/20261022T022236Z-microneme-membrane-audit/review.yaml; Complete original YAML and Markdown, frozen inputs/checks/assessments/findings/actions and access limits | supports | Historical observations remain historical; original artifacts are unchanged. Current target is byte-unchanged. Exact inherited findings are retained where present; no other-target/category issue disposition follows. |
| septin-original-validation-microneme_membrane | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/adversary-septin/original-checks.json; Actual original native validate/render and historical target-hash verification | supports | Both native commands exit0; original Markdown matches deterministic render and historical target hash equals frozen input. |
| septin-native-microneme_membrane-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/microneme_membrane-uniprot-verify-receipt.json; Actual receipt; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/microneme_membrane-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0. Zero protein examples and zero typed GENE_OR_PROTEIN nodes; no represented UniProtKB graph xrefs. Exit0 validates an empty identifier inventory, not the complete exocytosis/pathway narrative. |
| septin-native-microneme_membrane-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/microneme_membrane-uniprot-causal-receipt.json; Actual receipt; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/microneme_membrane-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Exit0. Zero protein examples and zero typed GENE_OR_PROTEIN nodes; no represented UniProtKB graph xrefs. Exit0 validates an empty identifier inventory, not the complete exocytosis/pathway narrative. |
| septin-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0020036,GO%3A0043231,GO%3A0020009,GO%3A0020007,GO%3A0033163,GO%3A0034494,GO%3A0031090,GO%3A0043233; Eight exact active GO definitions, synonyms and relation-bearing children | supports | GO0020036 is Maurer cleft; GO0020009 whole microneme, GO0034494 lumen and GO0033163 membrane remain distinct. Lumen is volume enclosed by the membrane; whole membrane is a cellular structure rather than a molecular lipid. GO0020007 apical complex and the declared broader organelle/lumen/membrane identities are separately verified. |
| septin-ancestors-0020036 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0020036/ancestors?relations=is_a; Complete exact GO ancestors response restricted to relations=is_a | supports | GO0043231 is not in this is_a-only response; the broader membrane-bounded-organelle parent is definition/biology-compatible, not claimed as a native GO ancestry edge. |
| septin-ancestors-0020009 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0020009/ancestors?relations=is_a; Complete exact GO ancestors response restricted to relations=is_a | supports | GO0043231 is a native is_a ancestor; apical-complex parthood is a separate relation, not is_a. |
| septin-ancestors-0034494 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0034494/ancestors?relations=is_a; Complete exact GO ancestors response restricted to relations=is_a | supports | GO0043233 organelle lumen is a native is_a ancestor; whole-organelle parthood is separately represented. |
| septin-ancestors-0033163 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0033163/ancestors?relations=is_a; Complete exact GO ancestors response restricted to relations=is_a | supports | GO0031090 organelle membrane is a native is_a ancestor; whole-organelle parthood is separate. |
| septin-tax5833 | https://rest.uniprot.org/taxonomy/5833.json; Exact UniProt taxonomy taxonId/scientific name/rank/lineage | supports | Plasmodium falciparum species. Taxonomic identity does not prove experimental strain or organelle membership. |
| septin-tax36329 | https://rest.uniprot.org/taxonomy/36329.json; Exact UniProt taxonomy taxonId/scientific name/rank/lineage | supports | Plasmodium falciparum3D7 isolate. Taxonomic identity does not prove experimental strain or organelle membership. |
| septin-tax2759 | https://rest.uniprot.org/taxonomy/2759.json; Exact UniProt taxonomy taxonId/scientific name/rank/lineage | supports | Eukaryota domain; broad RARE occurrence is qualitative, not a numeric prevalence estimate. Taxonomic identity does not prove experimental strain or organelle membership. |
| septin-tax5794 | https://rest.uniprot.org/taxonomy/5794.json; Exact UniProt taxonomy taxonId/scientific name/rank/lineage | supports | Apicomplexa phylum; stage/lineage restrictions remain. Taxonomic identity does not prove experimental strain or organelle membership. |
| septin-tax5811 | https://rest.uniprot.org/taxonomy/5811.json; Exact UniProt taxonomy taxonId/scientific name/rank/lineage | supports | Toxoplasma gondii species. Taxonomic identity does not prove experimental strain or organelle membership. |
| septin-tax432359 | https://rest.uniprot.org/taxonomy/432359.json; Exact UniProt taxonomy taxonId/scientific name/rank/lineage | supports | Toxoplasma gondii VEG strain, under typeIII lineage; not the RH experimental strain. Taxonomic identity does not prove experimental strain or organelle membership. |
| septin-tax508771 | https://rest.uniprot.org/taxonomy/508771.json; Exact UniProt taxonomy taxonId/scientific name/rank/lineage | supports | Toxoplasma gondii ME49 strain; not the RH experimental strain. Taxonomic identity does not prove experimental strain or organelle membership. |
| septin-protein-Q6V0W9 | https://rest.uniprot.org/uniprotkb/Q6V0W9.json; Exact current accession/status/name/gene fields/taxon/comments/features/cross-references | supports | UNREVIEWED P.falciparum5833 MAHRP1 fragment with geneName mahrp1; no native functional/localization comments or InterPro xrefs. Fragment identity is not exact identity of a full experimental construct. |
| septin-protein-Q8I2G1 | https://rest.uniprot.org/uniprotkb/Q8I2G1.json; Exact current accession/status/name/gene fields/taxon/comments/features/cross-references | supports | New REX1 example is UNREVIEWED P.falciparum3D7 taxon36329 with ORF-name PF3D7_0935900 and matching REX1 protein name. It has no formal primary geneName field; automatic transmembrane feature and entry identity do not establish causal necessity. Cooke primary body independently supplies Rex cleft-marker context. |
| septin-protein-Q9NFF5 | https://rest.uniprot.org/uniprotkb/Q9NFF5.json; Exact current accession/status/name/gene fields/taxon/comments/features/cross-references | supports | UNREVIEWED P.falciparum5833 skeleton-binding protein1 with geneName sbp1; automatic transmembrane feature, no native functional comments. Experimental membership and trafficking follow Blisnick/Cooke, not TrEMBL identity alone. |
| septin-protein-O00834 | https://rest.uniprot.org/uniprotkb/O00834.json; Exact current accession/status/name/gene fields/taxon/comments/features/cross-references | supports | REVIEWED T.gondii5811 MIC1; soluble adhesin in MIC6/MIC1/MIC4 context. Cell-location evidence cites PMID11157983,15684324,18818666, which are separately checked at complete primary-abstract scope. IPR008117 is a MIC1-family candidate, not identity of the entire heterogeneous adhesin cohort. |
| septin-protein-B6KAM0 | https://rest.uniprot.org/uniprotkb/B6KAM0.json; Exact current accession/status/name/gene fields/taxon/comments/features/cross-references | supports | REVIEWED T.gondiiVEG432359 AMA1 with geneName AMA1 and ORF TGVEG_255260. Single-pass typeI topology and predicted cytoplasmic-domain annotation are distinguished from primary-abstract evidence for microneme localization/shedding. Exact cited PMIDs11083833,11087913,16102004 are checked. VEG entry identity is not an RH-specific experiment. |
| septin-protein-S8F9G8 | https://rest.uniprot.org/uniprotkb/S8F9G8.json; Exact current accession/status/name/gene fields/taxon/comments/features/cross-references | supports | UNREVIEWED T.gondiiME49508771 MIC2, geneName MIC2 and ORF TGME49_201780. Automatic secretion annotation and domain xrefs do not replace primary transmembrane/topology experiments. This same accession appears in two component inventories; no fifth distinct accession is inferred. |
| septin-protein-S8GDJ1 | https://rest.uniprot.org/uniprotkb/S8GDJ1.json; Exact current accession/status/name/gene fields/taxon/comments/features/cross-references | supports | New UNREVIEWED T.gondiiME49508771 MIC2-associated proteinM2AP, ORF-name TGME49_214940 and matching protein name; no formal primary geneName field. Automatic signal peptide and IPR054124 beta-domain link do not establish whole-complex identity or the exact RH experimental construct. Primary studies independently support soluble M2AP/MIC2 complex membership. |
| septin-lanzer2006-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1016%2Fj.ijpara.2005.10.001%22&amp;pageSize=25; Exact MED metadata: title/ordered authors/date/complete abstractText | supports | Complete secondary abstract and bibliography support Maurer trafficking/background; speculative multiple roles are not treated as new demonstrated mechanisms. |
| septin-blisnick2000-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1016%2FS0166-6851%2800%2900301-7%22&amp;pageSize=25; Exact MED metadata: title/ordered authors/date/complete abstractText | supports | Complete primary abstract: SBP1 integral cleft membrane, host-cytoplasmic C-terminal interaction context and proposed anchoring; no current full-body/pixel claim. Rodent antibody observations are not imported as exact P.falciparum genetic evidence. |
| septin-cooke2006-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1083%2Fjcb.200509122%22&amp;pageSize=25; Exact MED metadata: title/ordered authors/date/complete abstractText | supports | Exact bibliography and complete primary abstract for SBP1 disruption/complementation and PfEMP1 display; actual primary body scope is recorded separately. |
| septin-spycher2008-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1111%2Fj.1365-2958.2008.06235.x%22&amp;pageSize=25; Exact MED metadata: title/ordered authors/date/complete abstractText | supports | Complete primary abstract and exact bibliography distinguish MAHRP1 disruption/complementation from the Cooke SBP1 study. This saved evidence does not certify a complete fresh publisher body. |
| septin-carruthers2008-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1007%2F978-0-387-78267-6_2%22&amp;pageSize=25; Exact MED metadata: title/ordered authors/date/complete abstractText | supports | Exact chapter/review bibliography and complete secondary abstract only. No current full-body verification is claimed from failed body endpoints or inherited review-body claims. |
| septin-dubois2019-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1111%2Fcmi.13018%22&amp;pageSize=25; Exact MED metadata: title/ordered authors/date/complete abstractText | supports | Exact review bibliography and complete abstract; accepted manuscript sections read are separately bounded. |
| septin-huynh2003-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1093%2Femboj%2Fcdg217%22&amp;pageSize=25; Exact MED metadata: title/ordered authors/date/complete abstractText | supports | Complete primary abstract: M2AP disruption causes MIC2 misrouting, impaired rapid secretion and strongly reduced invasion, not absolute loss or proven microneme-formation necessity. Fresh full body was not retrieved. |
| septin-huynh2006-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1371%2Fjournal.ppat.0020084%22&amp;pageSize=25; Exact MED metadata: title/ordered authors/date/complete abstractText | supports | Exact primary bibliography and complete abstract; actual current body supports MIC2 topology and RH-derived conditional-depletion interpretation. |
| septin-brown2016-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1074%2Fjbc.m115.700518%22&amp;pageSize=25; Exact MED metadata: title/ordered authors/date/complete abstractText | supports | Complete primary abstract: in vitro serum albumin/PKG-cGMP pathway, ethanol/calcium and zaprinast contexts are distinct. No current full Methods/body or universal secretion mechanism is certified. |
| septin-pmid-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A%289208224%20OR%2011157983%20OR%2015684324%20OR%2018818666%20OR%2011083833%20OR%2011087913%20OR%2016102004%29%20AND%20SRC%3AMED&amp;pageSize=25; Seven exact MED records: complete bibliography and abstractText for9208224,11157983,15684324,18818666,11083833,11087913,16102004 | supports | Carruthers/Sibley1997 supports sequential MIC2 then Rop1 then dense-granule secretion. Reiss2001 supports MIC6 escort and soluble MIC1/MIC4 versus transmembrane escort topology. Cerede2005 and Sawmynaden2008 concern soluble adhesins/function/domain interactions. Hehl2000 and Donahue2000 support AMA1 microneme localization/typeI topology; Howell2005 distinguishes shedding routes. These are complete primary abstracts, not current whole-body, figure or raw-data inspections. |
| septin-cooke2006-bioc | https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_json/PMC2063733/unicode; Genuine BioC: complete Abstract/Introduction/Results/Discussion; main Methods through adhesion assays; Figure1–7 captions and supplementary-material description. Supplementary data, image pixels and raw measurements not inspected | supports | P.falciparum3D7 infected human erythrocytes, SBP1 knockouts1G8/2D8/1G5 and EYFP complementation. Clefts/knobs persist; PfEMP1 remains in clefts rather than reaching host surface; complementation restores display/adhesion. Rex and MAHRP cleft-marker context supports resident membership. This is an SBP1 experiment, not MAHRP1 genetic disruption. Proposed anchoring/direct-binding interpretations are not promoted to demonstrated molecular mechanisms. |
| septin-huynh2006-bioc | https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_json/PMC1550269/unicode; Genuine BioC: complete Introduction/Results/Discussion, Figure1–7 captions; selected Methods plasmids, parasites/transfection/selection, primers, quantitative Western, secretion and invasion/attachment. Table1 heading only; no table numerical reanalysis, pixels, videos or supplements | supports | RH-derived tTA-dhfr versus conditional MIC2 depletion in HFF context supports membrane-spanning MIC2 with extracellular adhesive domains and short cytoplasmic tail, soluble M2AP partnership, and M2AP misrouting upon MIC2 depletion. Other MIC5/AMA1 localization persists; residual invasion and distinct gliding modes preclude absolute organelle-formation/whole-class necessity. VEG/ME49 representative entries are not identified as these exact experimental constructs. |
| septin-dubois2019-pdf | https://access.archive-ouverte.unige.ch/access/metadata/8d9f50fe-0548-4e4f-bc29-4b05a43e7ddc/download; Genuine accepted review manuscript; extracted text lines40–578: Abstract,Introduction,microneme diversity/structure,contents/conservation,biogenesis/maturation/trafficking and signaling cascade. Later preparing-secretion/fusion/insights/conclusion,Table1,figures/pixels not comprehensively inspected | supports | Secondary synthesis supports lineage/stage variation, microneme cargo complexes and soluble versus transmembrane/cytoplasmic portions. It distinguishes named complex components from all-stage universal composition and hypotheses from demonstrated steps. Accepted-manuscript copyright does not grant an image-hosting licence; no source image is adopted. |
| septin-gene-MIC1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AMIC1%29%20AND%20%28organism_id%3A5811%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Exact reviewed UniProt gene-name/organism query | supports | One exact reviewed MIC1 entry O00834 returned for organism5811. This supports the chosen representative only, not complete taxonomic distribution, membership or necessity. |
| septin-gene-AMA1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AAMA1%29%20AND%20%28organism_id%3A432359%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Exact reviewed UniProt gene-name/organism query | supports | One exact reviewed AMA1 entry B6KAM0 returned for organism432359. This supports the chosen representative only, not complete taxonomic distribution, membership or necessity. |
| septin-ipr-mahrp1 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q6V0W9/?page_size=200; Exact Q6V0W9 InterPro entry lookup; HTTP204 no body | supports | No InterPro entries returned by this bounded single-accession endpoint. This is not evidence that MAHRP1 lacks a biological family or that related proteins are absent. Existing grounding TODO remains open. |
| septin-ipr-sbp1 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q9NFF5/?page_size=200; Exact Q9NFF5 InterPro response; single family hit IPR044661 | supports | Returned family name is Mediator RNA polymeraseII transcription15a/b/c-like; this automatic/domain context does not independently establish exact SBP1 structural identity. No unrelated family grounding is adopted or absence inferred. |
| septin-rex1-search | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=TITLE_ABS%3AREX1%20AND%20TITLE_ABS%3APlasmodium&amp;pageSize=25; Bounded title/abstract query result metadata; eight returned titles inspected | supports | The result list provides discovery context only; it is not eight independently read full abstracts or bodies and supplies no new mechanistic finding. REX resident context is independently supported by the current Cooke primary body. |
| septin-retrieval-source-receipts | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/adversary-septin/source-receipts.json; Actual source retrieval outcomes, request dates and returned-file hashes | supports | Transport/endpoint availability evidence only. HTTP200 BioC service/error packets for Carruthers1997/Huynh2003/Brown2016 are not scientific bodies; later S3 and EuropePMC fallbacks failed. Spycher direct publisher403 and later web timeouts do not negate its complete primary abstract or the selected publisher text actually displayed. REX2015 optional body retrieval429 is not scientific absence. |
| septin-retrieval-additional-source-receipts | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/adversary-septin/additional-source-receipts.json; Actual source retrieval outcomes, request dates and returned-file hashes | supports | Transport/endpoint availability evidence only. HTTP200 BioC service/error packets for Carruthers1997/Huynh2003/Brown2016 are not scientific bodies; later S3 and EuropePMC fallbacks failed. Spycher direct publisher403 and later web timeouts do not negate its complete primary abstract or the selected publisher text actually displayed. REX2015 optional body retrieval429 is not scientific absence. |
| septin-retrieval-fallback-source-receipts | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/adversary-septin/fallback-source-receipts.json; Actual source retrieval outcomes, request dates and returned-file hashes | supports | Transport/endpoint availability evidence only. HTTP200 BioC service/error packets for Carruthers1997/Huynh2003/Brown2016 are not scientific bodies; later S3 and EuropePMC fallbacks failed. Spycher direct publisher403 and later web timeouts do not negate its complete primary abstract or the selected publisher text actually displayed. REX2015 optional body retrieval429 is not scientific absence. |
| septin-catalogue | https://imodulondb.org/api/datasets; Complete current official iModulonDB organism names/ids and dataset-key fields | supports | No matching Plasmodium falciparum/3D7, Toxoplasma gondii/VEG/ME49 or broader apicomplexan/eukaryotic host occurs. Whole record molecular/pathway claims require assessment even where the native protein inventory is empty. No unrelated bacterial downstream query or biological absence inference is justified. |
| septin-adapter-runner-historical | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Actual historical00:49Z invocation, no new runner execution | supports | Attempt2026-11-03T00:49:00.848907Z–00:49:00.863225Z exited1 with PermissionError reading pyvenv.cfg. Fresh official catalogue is a separately evidenced fallback; no successful/fresh runner invocation is claimed. |
| plaque-current-1 | data/structures/membrane_organelle/methane_oxidizing_organelle.yaml; Entire current maintained record at 61d3617ae8700b99198e2aaf01f3b2437933de6c including all graphs/history/discussions | supports | Current frozen target independently read. Stale delta is added unreviewed Q603F1 identity example plus history; reassessed substantively. |
| plaque-original-1 | reviews/structured/20261022T022232Z-methane-oxidizing-organelle-audit/review.yaml; Exact staleness-selected authoritative YAML and derived Markdown, all source/check/assessment/finding/action fields | supports | Historical pair independently validates/renders; every historical source hash matches. Qualified pass had no scientific findings. |
| plaque-current-5 | data/structures/membrane_organelle/micronucleus.yaml; Entire current maintained record at 61d3617ae8700b99198e2aaf01f3b2437933de6c including all graphs/history/discussions | supports | Current frozen target independently read. Current bytes match original frozen target; original scientific findings/dispositions reassessed. |
| plaque-original-5 | reviews/structured/20261022T022237Z-micronucleus-audit/review.yaml; Exact staleness-selected authoritative YAML and derived Markdown, all source/check/assessment/finding/action fields | supports | Historical pair independently validates/renders; every historical source hash matches. Qualified pass had no scientific findings. |
| plaque-current-6 | data/structures/membrane_organelle/microsporidian_posterior_vacuole.yaml; Entire current maintained record at 61d3617ae8700b99198e2aaf01f3b2437933de6c including all graphs/history/discussions | supports | Current frozen target independently read. Current bytes match original frozen target; original scientific findings/dispositions reassessed. |
| plaque-original-6 | reviews/structured/20261022T022238Z-microsporidian-posterior-vacuole-audit/review.yaml; Exact staleness-selected authoritative YAML and derived Markdown, all source/check/assessment/finding/action fields | supports | Historical pair independently validates/renders; every historical source hash matches. Two original minor findings remain confirmed with exact lineage; no target correction made. |
| plaque-policy | .claude/skills/review-yaml-record/SKILL.md; Frozen native contract; current bytes independently compared with previously read PR2368 policies; record skill/profile and CausalNode definition freshly reread | context_only | Genes, proteins, pathways and stress/trait claims trigger applicability without an expression-module assertion. Genuine sparse physical morphology is distinguished. |
| plaque-rubric | .claude/skills/curate-yaml-record/references/review-checklist.md; Frozen native contract; current bytes independently compared with previously read PR2368 policies; record skill/profile and CausalNode definition freshly reread | context_only | Claim-scoped identity, chemistry/material, taxonomy, roles, necessity, graphs and experimental modalities are separate questions; optional unfilled slots alone are not issues. |
| plaque-graph-rubric | .claude/skills/curate-causal-graphs/SKILL.md; Frozen native contract; current bytes independently compared with previously read PR2368 policies; record skill/profile and CausalNode definition freshly reread | context_only | Preserve epistemic scope and source taxon; descriptive topology does not prove a physical driver. |
| plaque-protein-contract | .claude/skills/uniprot-protein-examples/SKILL.md; Frozen native contract; current bytes independently compared with previously read PR2368 policies; record skill/profile and CausalNode definition freshly reread | context_only | Native accession verification is identity coverage, not structure membership or necessity; protein complexes may be covered by component_ref. |
| plaque-schema-policy | src/cellstructuremech/schema/cellstructuremech.yaml; Frozen native contract; current bytes independently compared with previously read PR2368 policies; record skill/profile and CausalNode definition freshly reread | context_only | CausalNode explicitly allows GENE_OR_PROTEIN for proteins, protein families and protein complexes. No mandatory pMMO retyping is inferred from complex membership. |
| plaque-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0044227,GO:0043231,GO:0046188,GO:0031040,GO:0005634,GO:0000228,GO:0019953,GO:0044099; Complete exact responses for0044227,0043231,0046188,0031040,0005634,0000228,0019953,0044099; definitions/synonyms/typed children inspected | supports | Exact methane-organelle identity and aliases, intracellular membrane-bounded parent, methane catabolism, ciliate micronucleus/nucleus parent, chromosome-versus-DNA distinction, sexual reproduction and microsporidian polar-tube identities agree. Current GO micronucleus definition explicitly says genic transcription is absent; graph remains mature Tetrahymena scope. |
| plaque-tax2 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2; Complete native ENA taxonomy identity/rank/aliases/lineage response | supports | Bacteria is domain2; record explicitly restricts occurrence to the methanotrophic subset with pMMO ICMs, not all bacteria. |
| plaque-tax243233 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/243233; Complete native ENA taxonomy identity/rank/aliases/lineage response | supports | 243233 is Methylococcus capsulatus strain Bath, including ATCC33009/NCIB11132 aliases; exact Zhu primary strain and reference proteins match. |
| plaque-tax5911 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5911; Complete native ENA taxonomy identity/rank/aliases/lineage response | supports | 5911 is Tetrahymena thermophila species; Hamilton sequenced SB210, kept as a named experimental strain rather than an inferred new strain CURIE. |
| plaque-tax6029 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/6029; Complete native ENA taxonomy identity/rank/aliases/lineage response | supports | 6029 is phylum Microsporidia; infectious-spore scope is distinct from every intracellular vegetative stage. |
| plaque-tax6039 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/6039; Complete native ENA taxonomy identity/rank/aliases/lineage response | supports | 6039 is Vairimorpha necatrix species; source cultivated spores through Helicoverpa zea, not a taxon synonym for other microsporidia. |
| plaque-protein-Q607G3 | https://rest.uniprot.org/uniprotkb/Q607G3.json; Native entryType/protein names/all gene rows/organism; FUNCTION,SUBUNIT,SUBCELLULAR LOCATION and evidence pointers | supports | Reviewed beta/PmoA entry lists pmoA1/MCA1797 and pmoA2/MCA2854 with pmoA alias in Bath243233. pMMO is a nonamer of three heterotrimeric protomers; membrane annotation is cited correctly. Entry identity is not unique-locus assignment or independent record membership proof. |
| plaque-protein-G1UBD1 | https://rest.uniprot.org/uniprotkb/G1UBD1.json; Native entryType/protein names/all gene rows/organism; FUNCTION,SUBUNIT,SUBCELLULAR LOCATION and CAUTION | supports | Reviewed alpha/PmoB entry lists pmoB1/MCA1796 and pmoB2/MCA2853 with pmoB alias in Bath243233. Membrane evidence PMIDs match. Native caution on proposed copper active site is not converted into a settled mechanistic record claim. |
| plaque-protein-Q603F1 | https://rest.uniprot.org/uniprotkb/Q603F1.json; Complete unreviewed entry identity, submission names, geneName, both ordered locus names and organism | supports | Added Q603F1 is unreviewed TrEMBL, submission name matches the record, primary gene pmoC1 and taxon243233. Entry contains MCA1798 and MCA2855; current role only asserts a representative identity, not a unique locus, reviewed status, direct localization or necessity. No guessed equivalence to unrelated strain used. |
| plaque-query-pmoA-reviewed | https://rest.uniprot.org/uniprotkb/search?query=organism_id%3A243233+AND+gene_exact%3ApmoA+AND+reviewed%3Atrue&amp;format=json&amp;size=25; Complete returned native UniProtKB query page; suggestions ignored | supports | Exact query returned ['Q607G3']. pmoA/pmoB aliases resolve reviewed examples; exact pmoC returns zero whereas exact primary pmoC1 returns Q603F1. This is a query/alias boundary, not protein absence or a contradiction of the representative example. |
| plaque-query-pmoA-all | https://rest.uniprot.org/uniprotkb/search?query=organism_id%3A243233+AND+gene_exact%3ApmoA&amp;format=json&amp;size=25; Complete returned native UniProtKB query page; suggestions ignored | supports | Exact query returned ['Q607G3']. pmoA/pmoB aliases resolve reviewed examples; exact pmoC returns zero whereas exact primary pmoC1 returns Q603F1. This is a query/alias boundary, not protein absence or a contradiction of the representative example. |
| plaque-query-pmoB-reviewed | https://rest.uniprot.org/uniprotkb/search?query=organism_id%3A243233+AND+gene_exact%3ApmoB+AND+reviewed%3Atrue&amp;format=json&amp;size=25; Complete returned native UniProtKB query page; suggestions ignored | supports | Exact query returned ['G1UBD1']. pmoA/pmoB aliases resolve reviewed examples; exact pmoC returns zero whereas exact primary pmoC1 returns Q603F1. This is a query/alias boundary, not protein absence or a contradiction of the representative example. |
| plaque-query-pmoB-all | https://rest.uniprot.org/uniprotkb/search?query=organism_id%3A243233+AND+gene_exact%3ApmoB&amp;format=json&amp;size=25; Complete returned native UniProtKB query page; suggestions ignored | supports | Exact query returned ['G1UBD1']. pmoA/pmoB aliases resolve reviewed examples; exact pmoC returns zero whereas exact primary pmoC1 returns Q603F1. This is a query/alias boundary, not protein absence or a contradiction of the representative example. |
| plaque-query-pmoC-reviewed | https://rest.uniprot.org/uniprotkb/search?query=organism_id%3A243233+AND+gene_exact%3ApmoC+AND+reviewed%3Atrue&amp;format=json&amp;size=25; Complete returned native UniProtKB query page; suggestions ignored | supports | Exact query returned []. pmoA/pmoB aliases resolve reviewed examples; exact pmoC returns zero whereas exact primary pmoC1 returns Q603F1. This is a query/alias boundary, not protein absence or a contradiction of the representative example. |
| plaque-query-pmoC-all | https://rest.uniprot.org/uniprotkb/search?query=organism_id%3A243233+AND+gene_exact%3ApmoC&amp;format=json&amp;size=25; Complete returned native UniProtKB query page; suggestions ignored | supports | Exact query returned []. pmoA/pmoB aliases resolve reviewed examples; exact pmoC returns zero whereas exact primary pmoC1 returns Q603F1. This is a query/alias boundary, not protein absence or a contradiction of the representative example. |
| plaque-query-pmoC1-all | https://rest.uniprot.org/uniprotkb/search?query=%28organism_id%3A243233%29%20AND%20%28gene_exact%3ApmoC1%29&amp;format=json&amp;size=25; Complete returned native UniProtKB query page; suggestions ignored | supports | Exact query returned ['Q603F1']. pmoA/pmoB aliases resolve reviewed examples; exact pmoC returns zero whereas exact primary pmoC1 returns Q603F1. This is a query/alias boundary, not protein absence or a contradiction of the representative example. |
| plaque-PMID12379148 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12379148+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=25; Complete exact PMID metadata and primary abstract only | supports | Basu2003 primary abstract describes purified Bath membrane-associated pMMO complex and subunits; native cited membrane evidence identity agrees. |
| plaque-PMID15674245 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15674245+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=25; Complete exact PMID metadata and primary abstract only | supports | Lieberman2005 primary abstract reports Bath membrane enzyme with alpha3beta3gamma3 arrangement at2.8A; supports exact assembly identity, not every modern active-site conclusion. |
| plaque-PMID22013879 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A22013879+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=25; Complete exact PMID metadata and primary abstract only | supports | Smith2011 primary abstract concerns Methylocystis strain M and includes revised Bath structural models. Record accurately attributes this as UniProt evidence pointer; not represented here as direct Bath-cell localization experiment. |
| plaque-zhu2022-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fs41467-022-32752-9%22&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact DOI metadata title/authors/year/PMID/PMC | supports | Zhu et al.2022 DOI/PMID36064719/PMC9445010 identity and title agree; claims assessed in genuine body. |
| plaque-whiddon2019-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1111%2F1751-7915.13458%22&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact DOI metadata title/authors/year/PMID/PMC | supports | Whiddon et al.2019 DOI/PMID31264365/PMC6680624 identity agrees; body has explicit type-I strain limits. |
| plaque-hamilton2016-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.7554%2FeLife.19090%22&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact DOI metadata title/authors/year/PMID/PMC | supports | Hamilton et al.2016 DOI/PMID27892853/PMC5182062 identity agrees; genuine eLife JATS supports current scope. |
| plaque-findley2005-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.14411%2Ffp.2005.014%22&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact DOI metadata title/authors/year/PMID/PMC | supports | Findley et al.2005 DOI/PMID16004370 identity agrees; publisher PDF independently read. |
| plaque-jaroenlak2020-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1371%2Fjournal.ppat.1008738%22&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact DOI metadata title/authors/year/PMID/PMC | supports | Jaroenlak et al.2020 DOI/PMID32946515/PMC7526891 identity agrees; current source body distinguishes SBFSEM and2D TEM. |
| plaque-sharma2024-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1371%2Fjournal.pbio.3002533%22&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact DOI metadata title/authors/year/PMID/PMC | supports | Sharma et al.2024 DOI/PMID38422169/PMC10931468 identity agrees; current body limits cryoET to tube regions. |
| plaque-troemel2015-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.fgb.2015.08.007%22&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact DOI metadata title/authors/year/PMID/PMC | supports | Troemel/Becnel2015 DOI/PMID26300319/PMC4587305 identity agrees; primary firing observations examined in body. |
| plaque-zhu2022-body | https://pmc-oa-opendata.s3.amazonaws.com/PMC9445010.1/PMC9445010.1.xml; Genuine PMC9445010.1 JATS: Introduction; Results Sec3–6, figure1–4 captions; Discussion; Methods Sec9–11; no figure pixels or raw-data reanalysis | supports | Copper-replete Bath ICMs and arrays observed by serial cryoFIB/SEM/cellular cryoET; isolated native membranes resolve the trimer of PmoA/B/C heterotrimers. Continuity supports authors invagination interpretation but static data alone cannot distinguish every biogenesis event. Reconstituted larger nanodiscs correlate with higher methane oxidation; graph does not assert array-alone sufficiency, exact active site or direct PmoB salt-bridge necessity. Methane→methanol chemistry supported in bounded activity assays. |
| plaque-whiddon2019-body | https://pmc-oa-opendata.s3.amazonaws.com/PMC6680624.1/PMC6680624.1.xml; Genuine PMC6680624.1 JATS: Introduction, Results staining/copper dependence/connectivity, Discussion and bacterial strain/growth Methods; figure captions read, not pixels | supports | Main strain Methylotuvimicrobium alcaliphilum20Z plus Methyloprofundus sedimenti and Methylomonas methanicaS1; no Bath experiment transferred. Lipophilic staining, FRAP and MDH colocalization are consistent with ICM connectivity; authors retain cycling/isolated-stack alternatives and resolution limits. Supports membrane-material description, not invariant complete mechanism. |
| plaque-stolyar2001-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1128%2FJB.183.5.1810-1812.2001%22&amp;format=json&amp;resultType=core&amp;pageSize=25; Complete exact DOI primary abstract only | supports | Transcripts and chromosomal gene fusions assay two Bath pmo gene clusters; functional redundancy and copper-dependent relative expression support the record narrow expression-study note. Full text was not recovered; not used to certify exact operon or every pmoC copy. |
| plaque-stolyar2001-body | https://pmc-oa-opendata.s3.amazonaws.com/PMC95072.1/PMC95072.1.xml; Attempted primary body route only; S3 returned404 or BioC returned explicit No result text | context_only | No usable full body retrieved on this route; body-scoped claims not inferred from status200 or metadata. Complete primary abstract used for the narrow cited claim. |
| plaque-stolyar2001-bioc | https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_xml/PMC95072/unicode; Attempted primary body route only; S3 returned404 or BioC returned explicit No result text | context_only | No usable full body retrieved on this route; body-scoped claims not inferred from status200 or metadata. Complete primary abstract used for the narrow cited claim. |
| plaque-hamilton2016-body | https://elifesciences.org/articles/19090.xml; Genuine publisher eLife JATS: Introduction s1; Results s2-1-1 chromosome-length assembly; Methods s3-1,s3-2,s3-4; captions in these sections; no figure pixels/raw genome reassembly | supports | Mature diploid transcriptionally silent germline nucleus differs from somatic MAC; IES/rearrangement examples vary across ciliates. SB210 was checked for five intact MIC chromosomes before purified-nucleus sequencing. Five near-full chromosome superassemblies retain small gaps/ordering uncertainties; current record does not claim gapless raw genome or all-stage absence of transcription. |
| plaque-findley2005-pdf | https://folia.paru.cas.cz/doi/10.14411/fp.2005.014.pdf; Actual publisher seven-page PDF text: p111–115 Abstract, Introduction, Methods, Results and Discussion; figure3/4 captions; no figure pixels or raw assays | supports | S.lophii activated/fixed EM supports posterior vesicle swelling during firing, not exact molecular force proof. Catalase/ACOX/nervonic-acid assays are source-specific observations; they are not positively asserted constituents in this sparse current record and do not automatically turn its generic physiological description into a structured gene-pathway claim. No peroxisome identity or microsporidian-wide protein composition inferred. |
| plaque-troemel2015-body | https://pmc-oa-opendata.s3.amazonaws.com/PMC4587305.1/PMC4587305.1.xml; Genuine PMC4587305.1 JATS: complete Introduction/main sections2–4 including firing section3 and Conclusions; video itself not independently replayed | supports | E.aedis firing observations show late posterior expansion; source explicitly presents pushing as appearance/likelihood and says underlying mechanism is poorly understood. Direct passage supports temporal/topological record claims; unqualified drives/pushes on final graph edge exceeds this source scope. |
| plaque-jaroenlak2020-body | https://journals.plos.org/plospathogens/article/file?id=10.1371/journal.ppat.1008738&amp;type=manuscript; Genuine publisher JATS: Introduction; Results sec003–005 and Fig1/2 captions; Discussion sec010 plus Fig6 caption; no figure pixels/videos/raw reconstructions | supports | Dormant A.algerae SBFSEM reconstructs a posterior bowl-shaped vacuole;2D TEM Fig2E resolves its single membrane and interdigitation. Source describes SBFSEM and2D TEM, not electron tomography. Proposed active role in PT/cargo movement remains tentative. Other species and germination states are distinguished. |
| plaque-sharma2024-body | https://journals.plos.org/plosbiology/article/file?id=10.1371/journal.pbio.3002533&amp;type=manuscript; Genuine publisher JATS: Results sec003 and Discussion sec007; Methods sec009–012, specifically light microscopy and on-grid tilt-series selection; relevant captions only, no pixels/raw tomograms | supports | V.necatrix germination dynamics were captured by light microscopy; cryoET examined extruded tube segments/cargo. Methods explicitly exclude spores and tube tips with ejected cargo from tilt-series collection. Static cryoET states have no time resolution and ordering is hypothetical. Correct taxon occurrence does not rescue the canonical example microscopy claim. |
| plaque-jaroenlak2022-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1007%2F978-3-030-93306-7_9%22&amp;format=json&amp;resultType=core&amp;pageSize=25; Complete exact DOI metadata and SECONDARY chapter abstract only | supports | Chapter discusses phylum-level polar-tube/spore apparatus and transport; full chapter not obtained. It does not independently measure posterior-vacuole prevalence. Broad infectious-spore context is triangulated with inspected primary species studies, not universal vegetative-stage or exact protein claims. |
| plaque-posterior-go-query | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=posterior%20vacuole&amp;limit=25&amp;page=1; Complete first25 returned QuickGO matches for posterior vacuole | supports | No exact microsporidian posterior-vacuole identity among these25 results; broad vacuole/polar structures are not substituted for this structure. Bounded result supports retaining minted identity, not exhaustive ontology-absence proof. |
| plaque-catalogue | https://imodulondb.org/api/datasets; Fresh complete official /api/datasets response, all20 organism rows and dataset listings inspected | supports | No Methylococcus/Bath methanotroph host, Tetrahymena or microsporidian host is listed. Broad Bacteria distribution is not a license to substitute unrelated bacterial/archaeal datasets. Methane proteins/metabolism and micronuclear genic-transcription/genome program trigger applicability, but no matched downstream gene/module query applies. Posterior vacuole itself is genuinely sparse physical morphology. Noncoverage is not negative biology; no generated module prose used. |
| plaque-historical-runner | /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources imodulondb datasets; Actual historical00:49Z receipt and stdout/stderr independently hash-checked | context_only | Historical adapter runner failed before data retrieval due pyvenv.cfg PermissionError. No current invocation or execution success claimed. Fresh official catalogue/native source inspection is bounded fallback. |
| plaque-original-checks | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/adversary-plaque/original-checks.json; Actual three original native validations/deterministic renders and all44 historical frozen input hashes | supports | Original14/16/14 source input sets match. Only methane current target changed; originals remain truthful immutable observations at their source. Current pmoC1 delta substantively refreshed; micronucleus/posterior targets unchanged. |
| plaque-methane-delta | data/structures/membrane_organelle/methane_oxidizing_organelle.yaml; Actual git diff retained in scratch from original frozen source to current HEAD | supports | Only scientific delta is addition of Q603F1/pmoC1 UNREVIEWED example plus curation event. Existing organelle, components and graph claims unchanged; current entry/query/primary body checks support refreshed qualified pass. |
| plaque-native-methane_oxidizing_organelle-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/methane_oxidizing_organelle.yaml --verify; Actual root command receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/methane_oxidizing_organelle-uniprot-verify-receipt.json and exact logSHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual maintained inventory has 3 protein_examples and 1 typed GENE_OR_PROTEIN nodes. Two reviewed and one unreviewed Bath accession; pMMO component_ref has native COVERED status. This is identity/symbol coverage, not membership/necessity or exact copper mechanism. |
| plaque-native-methane_oxidizing_organelle-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/methane_oxidizing_organelle.yaml --causal-graphs; Actual root command receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/methane_oxidizing_organelle-uniprot-causal-receipt.json and exact logSHA256 8bdfb4b272fb0dd0644bc13f57c6141919be9f5f5934c3a51d7a64a22136660f | supports | Actual maintained inventory has 3 protein_examples and 1 typed GENE_OR_PROTEIN nodes. Two reviewed and one unreviewed Bath accession; pMMO component_ref has native COVERED status. This is identity/symbol coverage, not membership/necessity or exact copper mechanism. |
| plaque-native-micronucleus-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/micronucleus.yaml --verify; Actual root command receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/micronucleus-uniprot-verify-receipt.json and exact logSHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual maintained inventory has 0 protein_examples and 0 typed GENE_OR_PROTEIN nodes. Empty native accession/typed-node coverage does not certify all narrative claims. |
| plaque-native-micronucleus-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/micronucleus.yaml --causal-graphs; Actual root command receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/micronucleus-uniprot-causal-receipt.json and exact logSHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Actual maintained inventory has 0 protein_examples and 0 typed GENE_OR_PROTEIN nodes. Empty native accession/typed-node coverage does not certify all narrative claims. |
| plaque-native-microsporidian_posterior_vacuole-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/microsporidian_posterior_vacuole.yaml --verify; Actual root command receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/microsporidian_posterior_vacuole-uniprot-verify-receipt.json and exact logSHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual maintained inventory has 0 protein_examples and 0 typed GENE_OR_PROTEIN nodes. Empty native accession/typed-node coverage does not certify all narrative claims. |
| plaque-native-microsporidian_posterior_vacuole-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/microsporidian_posterior_vacuole.yaml --causal-graphs; Actual root command receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/microsporidian_posterior_vacuole-uniprot-causal-receipt.json and exact logSHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Actual maintained inventory has 0 protein_examples and 0 typed GENE_OR_PROTEIN nodes. Empty native accession/typed-node coverage does not certify all narrative claims. |
| micro-policy | .claude/skills/review-yaml-record/SKILL.md; Complete review skill/profile/config/shared output contract and native checklist; CURATION evidence/components/images/graph rules | context_only | Named proteins, mitochondrial architecture, oxidative phosphorylation and MDC intervention/stress pathways trigger applicability assessment beyond expression-only claims. Review-only ownership and exact evidence scopes preserved. |
| micro-component-policy | src/cellstructuremech/schema/cellstructuremech.yaml; CausalNode/Edge, CausalNodeTypeEnum, component roles/types and essentiality; CURATION family-or-class guidance | context_only | GO cellular components may use STRUCTURE. Protein identity, constituent membership, associated maintenance/release machinery and formation necessity are distinct. The native CausalNode description also permits protein complexes under GENE_OR_PROTEIN, so the old type alone was not proof of a scientific error. |
| micro-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Complete graph skill and UniProt protein-examples rules; exact native verifier filtering at scripts/uniprot_genes.py:671-804 | context_only | Edges retain source conditions and actor scope. Native verifier only resolves UniProt xrefs on GENE_OR_PROTEIN nodes, so junction STRUCTURE-node P36112 requires the separate fresh authority check supplied here. |
| micro-record-mitochondrial_crista | data/structures/membrane_organelle/mitochondrial_crista.yaml; Entire current maintained record: all components, examples, functions, graph edges, properties/images, discussions and history | supports | Full current target inspected. Current target equals its original frozen bytes. |
| micro-prior-mitochondrial_crista | reviews/structured/20261022T022238Z-mitochondrial-crista-audit/review.yaml; Original scientific assessments, evidence scopes, checks, findings/actions, limitations and native Markdown pair | context_only | Original pass_with_limitations; 0 scientific findings. Its explicit expression-only adapter exclusion requires correction. Historical source reads and QC remain historical. |
| micro-native-mitochondrial_crista-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/mitochondrial_crista-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/mitochondrial_crista.yaml --verify; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/mitochondrial_crista-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0 on exact source head. No component protein examples and zero GENE_OR_PROTEIN nodes; complex STRUCTURE actors are outside the typed-node denominator. Command success is not a localization/assembly/necessity experiment. |
| micro-native-mitochondrial_crista-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/mitochondrial_crista-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/mitochondrial_crista.yaml --causal-graphs; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/mitochondrial_crista-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Exit0 on exact source head. No component protein examples and zero GENE_OR_PROTEIN nodes; complex STRUCTURE actors are outside the typed-node denominator. Command success is not a localization/assembly/necessity experiment. |
| micro-record-mitochondrial_crista_junction | data/structures/membrane_organelle/mitochondrial_crista_junction.yaml; Entire current maintained record: all components, examples, functions, graph edges, properties/images, discussions and history | supports | Full current target inspected. MICOS node retyping and appended history substantively reassessed. |
| micro-prior-mitochondrial_crista_junction | reviews/structured/20261022T022239Z-mitochondrial-crista-junction-audit/review.yaml; Original scientific assessments, evidence scopes, checks, findings/actions, limitations and native Markdown pair | context_only | Original needs_curation; 1 scientific findings. Its explicit expression-only adapter exclusion requires correction. Historical source reads and QC remain historical. |
| micro-native-mitochondrial_crista_junction-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/mitochondrial_crista_junction-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/mitochondrial_crista_junction.yaml --verify; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/mitochondrial_crista_junction-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0 on exact source head. No component examples and zero GENE_OR_PROTEIN nodes after MICOS retyping. STRUCTURE-node P36112 is skipped by native protein verification and independently verified from fresh authority JSON. Command success is not a localization/assembly/necessity experiment. |
| micro-native-mitochondrial_crista_junction-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/mitochondrial_crista_junction-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/mitochondrial_crista_junction.yaml --causal-graphs; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/mitochondrial_crista_junction-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Exit0 on exact source head. No component examples and zero GENE_OR_PROTEIN nodes after MICOS retyping. STRUCTURE-node P36112 is skipped by native protein verification and independently verified from fresh authority JSON. Command success is not a localization/assembly/necessity experiment. |
| micro-record-mitochondrial_derived_compartment | data/structures/membrane_organelle/mitochondrial_derived_compartment.yaml; Entire current maintained record: all components, examples, functions, graph edges, properties/images, discussions and history | supports | Full current target inspected. Current target equals its original frozen bytes. |
| micro-prior-mitochondrial_derived_compartment | reviews/structured/20261022T022241Z-mitochondrial-derived-compartment-audit/review.yaml; Original scientific assessments, evidence scopes, checks, findings/actions, limitations and native Markdown pair | context_only | Original needs_curation; 1 scientific findings. Its explicit expression-only adapter exclusion requires correction. Historical source reads and QC remain historical. |
| micro-native-mitochondrial_derived_compartment-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/mitochondrial_derived_compartment-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/mitochondrial_derived_compartment.yaml --verify; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/mitochondrial_derived_compartment-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0 on exact source head. Three reviewed component examples TOM70/P07213, TOM71/P38825 and DNM1/P54861 in tax559292; zero GENE_OR_PROTEIN nodes because intervention/capability nodes are STATE. Command success is not a localization/assembly/necessity experiment. |
| micro-native-mitochondrial_derived_compartment-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/mitochondrial_derived_compartment-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/mitochondrial_derived_compartment.yaml --causal-graphs; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/mitochondrial_derived_compartment-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Exit0 on exact source head. Three reviewed component examples TOM70/P07213, TOM71/P38825 and DNM1/P54861 in tax559292; zero GENE_OR_PROTEIN nodes because intervention/capability nodes are STATE. Command success is not a localization/assembly/necessity experiment. |
| micro-original-pairs | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/adversary-microtubule/original-checks.json; Three actual native validate and render --content commands; byte equality to original Markdown | supports | All three original pairs validate and render exactly. Original frozen target hashes verified from historical source; junction changed, crista/MDC unchanged. |
| micro-stale-delta | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/adversary-microtubule/junction-stale.diff; Complete original frozen revision to current diff | context_only | Only appended history and micos_complex GENE_OR_PROTEIN to STRUCTURE type change; GO identity, P36112 member xref and maintenance edge unchanged. |
| micro-historical-2419 | https://github.com/CultureBotAI/CellStructureMech/issues/2419; Complete root-retained body/state/comments /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/historical-issue-2419.json | context_only | Closed issue groups five node-type corrections, including this MICOS actor. Historical context only: no terminal disposition of the grouped finding and no claim it resolves the separate modality finding. |
| micro-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0030061,GO%3A0044284,GO%3A0005743,GO%3A0097002,GO%3A0061617,GO%3A0045259,GO%3A0042407,GO%3A0006119,GO%3A0044232,GO%3A0007007,GO%3A0043231,GO%3A0099073; All12 active term identities/definitions/synonyms and typed child relations | supports | Exact crista/junction/inner boundary/inner membrane, MICOS, ATP synthase, formation/organization/oxidative phosphorylation, contact site, broad organelle parent and distinct MDV identities agree. IMM directly lists crista/junction as part_of; contact site directly lists junction as is_a. No unreturned taxon constraints asserted. |
| micro-go0030061-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0030061/ancestors?relations=is_a; Complete exact is_a-only ancestor response | supports | Requested is_a ancestry confirms junction contact-site ancestry; crista has general cellular component ancestry. This response does not supply taxon-constraint data. |
| micro-go0044284-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0044284/ancestors?relations=is_a; Complete exact is_a-only ancestor response | supports | Requested is_a ancestry confirms junction contact-site ancestry; crista has general cellular component ancestry. This response does not supply taxon-constraint data. |
| micro-tax2759 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759; Exact taxId/scientificName/rank/lineage and synonyms | supports | Tax2759 = Eukaryota (domain). Identity only; not prevalence or equivalence of mutant experimental strains. |
| micro-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Exact taxId/scientificName/rank/lineage and synonyms | supports | Tax4932 = Saccharomyces cerevisiae (species). Identity only; not prevalence or equivalence of mutant experimental strains. |
| micro-tax559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Exact taxId/scientificName/rank/lineage and synonyms | supports | Tax559292 = Saccharomyces cerevisiae S288C (strain). Identity only; not prevalence or equivalence of mutant experimental strains. |
| micro-uo0000017 | https://www.ebi.ac.uk/ols4/api/ontologies/uo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FUO_0000017; Exact active term label/definition | supports | Micrometer is10^-6m; this independently verifies unit identity, not sample size or measured value. |
| micro-protein-P36112 | https://rest.uniprot.org/uniprotkb/P36112.json; entryType, primaryAccession, recommended name, genes/loci, taxon; complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments | supports | P36112 is reviewed MIC60 in tax559292; primary gene/locus and recommended protein name inspected. MIC60/FCJ1/AIM28/FMP13,YKR016W is one MICOS subunit, with experimental inner-membrane/MICOS annotations; this member xref does not redefine the whole complex. |
| micro-protein-P07213 | https://rest.uniprot.org/uniprotkb/P07213.json; entryType, primaryAccession, recommended name, genes/loci, taxon; complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments | supports | P07213 is reviewed TOM70 in tax559292; primary gene/locus and recommended protein name inspected. Native function/subunit/location annotations describe general mitochondrial roles; MDC membership and conditional effects require separately inspected primary experiments. |
| micro-protein-P38825 | https://rest.uniprot.org/uniprotkb/P38825.json; entryType, primaryAccession, recommended name, genes/loci, taxon; complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments | supports | P38825 is reviewed TOM71 in tax559292; primary gene/locus and recommended protein name inspected. Native function/subunit/location annotations describe general mitochondrial roles; MDC membership and conditional effects require separately inspected primary experiments. |
| micro-protein-P54861 | https://rest.uniprot.org/uniprotkb/P54861.json; entryType, primaryAccession, recommended name, genes/loci, taxon; complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments | supports | P54861 is reviewed DNM1 in tax559292; primary gene/locus and recommended protein name inspected. Native function/subunit/location annotations describe general mitochondrial roles; MDC membership and conditional effects require separately inspected primary experiments. |
| micro-family-P07213 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P07213/?page_size=200; All integrated result entries and types; count3, next=null | supports | Complete bounded integrated family inspection: Tom70 IPR005687 plus TPR superfamily/repeat. |
| micro-family-P38825 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P38825/?page_size=200; All integrated result entries and types; count2, next=null | supports | Complete bounded integrated family inspection: TPR repeat/superfamily only; no exact integrated Tom71 family in this endpoint. |
| micro-family-P54861 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P54861/?page_size=200; All integrated result entries and types; count9, next=null | supports | Complete bounded integrated family inspection: Broad Dynamin IPR022812 plus domains/sites/superfamilies, not exact mitochondrial Dnm1 class. |
| micro-IPR005687 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005687/; Complete native accession/name/type/member databases and description | supports | Exact Tom70 family; class grounding distinct from MDC localization. |
| micro-IPR022812 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR022812/; Complete native accession/name/type/member databases and description | supports | Exact Dynamin family is broader than mitochondrial Dnm1-type class. |
| micro-query-TOM70 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=100&amp;query=%28gene_exact%3ATOM70%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; Complete one-hit response and gene tokens | supports | Exactly P07213 with matching primary TOM70 returned; bounded uniqueness only, not membership. |
| micro-query-TOM71 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=100&amp;query=%28gene_exact%3ATOM71%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; Complete one-hit response and gene tokens | supports | Exactly P38825 with matching primary TOM71 returned; bounded uniqueness only, not membership. |
| micro-query-DNM1 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=100&amp;query=%28gene_exact%3ADNM1%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; Complete one-hit response and gene tokens | supports | Exactly P54861 with matching primary DNM1 returned; bounded uniqueness only, not membership. |
| micro-friedman2015-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=100&amp;query=DOI%3A%2210.7554/eLife.07739%22; Complete returned identity/publication-type/abstract fields; exact DOI or MED-ID query, pageSize100 | context_only | Complete bibliographic identity and returned abstracts read; DOI/title/PMID/PMC links retained without treating metadata as full-text evidence.  |
| micro-davies2012-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=100&amp;query=DOI%3A%2210.1073/pnas.1204593109%22; Complete returned identity/publication-type/abstract fields; exact DOI or MED-ID query, pageSize100 | context_only | Complete bibliographic identity and returned abstracts read; DOI/title/PMID/PMC links retained without treating metadata as full-text evidence.  |
| micro-paumard2002-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=100&amp;query=DOI%3A%2210.1093/emboj/21.3.221%22; Complete returned identity/publication-type/abstract fields; exact DOI or MED-ID query, pageSize100 | context_only | Complete bibliographic identity and returned abstracts read; DOI/title/PMID/PMC links retained without treating metadata as full-text evidence.  |
| micro-friedman2014-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=100&amp;query=DOI%3A%2210.1038/nature12985%22; Complete returned identity/publication-type/abstract fields; exact DOI or MED-ID query, pageSize100 | context_only | Complete bibliographic identity and returned abstracts read; DOI/title/PMID/PMC links retained without treating metadata as full-text evidence. Secondary review, not a primary experiment. |
| micro-hughes2016-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=100&amp;query=DOI%3A%2210.7554/eLife.13943%22; Complete returned identity/publication-type/abstract fields; exact DOI or MED-ID query, pageSize100 | context_only | Complete bibliographic identity and returned abstracts read; DOI/title/PMID/PMC links retained without treating metadata as full-text evidence.  |
| micro-wilson2024-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=100&amp;query=DOI%3A%2210.1083/jcb.202307035%22; Complete returned identity/publication-type/abstract fields; exact DOI or MED-ID query, pageSize100 | context_only | Complete bibliographic identity and returned abstracts read; DOI/title/PMID/PMC links retained without treating metadata as full-text evidence.  |
| micro-cargo2024-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=100&amp;query=DOI%3A%2210.1083/jcb.202307036%22; Complete returned identity/publication-type/abstract fields; exact DOI or MED-ID query, pageSize100 | context_only | Complete bibliographic identity and returned abstracts read; DOI/title/PMID/PMC links retained without treating metadata as full-text evidence.  |
| micro-ermes2020-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=100&amp;query=DOI%3A%2210.1083/jcb.202002144%22; Complete returned identity/publication-type/abstract fields; exact DOI or MED-ID query, pageSize100 | context_only | Complete bibliographic identity and returned abstracts read; DOI/title/PMID/PMC links retained without treating metadata as full-text evidence.  |
| micro-lipids2024-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=100&amp;query=DOI%3A%2210.1083/jcb.202302069%22; Complete returned identity/publication-type/abstract fields; exact DOI or MED-ID query, pageSize100 | context_only | Complete bibliographic identity and returned abstracts read; DOI/title/PMID/PMC links retained without treating metadata as full-text evidence.  |
| micro-preprintA2026-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=100&amp;query=DOI%3A%2210.64898/2026.04.03.716366%22; Complete returned identity/publication-type/abstract fields; exact DOI or MED-ID query, pageSize100 | context_only | Complete bibliographic identity and returned abstracts read; DOI/title/PMID/PMC links retained without treating metadata as full-text evidence. Preprint identity/status retained; no version-of-record claim. The first DOI query returns a PMC stub entry plus the matching PPR abstract, not two independent experiments. |
| micro-preprintB2026-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=100&amp;query=DOI%3A%2210.64898/2026.06.09.731211%22; Complete returned identity/publication-type/abstract fields; exact DOI or MED-ID query, pageSize100 | context_only | Complete bibliographic identity and returned abstracts read; DOI/title/PMID/PMC links retained without treating metadata as full-text evidence. Preprint identity/status retained; no version-of-record claim. The first DOI query returns a PMC stub entry plus the matching PPR abstract, not two independent experiments. |
| micro-PMID42798366 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=100&amp;query=EXT_ID:42798366%20AND%20SRC:MED; Complete returned identity/publication-type/abstract fields; exact DOI or MED-ID query, pageSize100 | context_only | Complete bibliographic identity and returned abstracts read; DOI/title/PMID/PMC links retained without treating metadata as full-text evidence. Preprint identity/status retained; no version-of-record claim. The first DOI query returns a PMC stub entry plus the matching PPR abstract, not two independent experiments. |
| micro-PMID42327138 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=100&amp;query=EXT_ID:42327138%20AND%20SRC:MED; Complete returned identity/publication-type/abstract fields; exact DOI or MED-ID query, pageSize100 | context_only | Complete bibliographic identity and returned abstracts read; DOI/title/PMID/PMC links retained without treating metadata as full-text evidence. Preprint identity/status retained; no version-of-record claim. The first DOI query returns a PMC stub entry plus the matching PPR abstract, not two independent experiments. |
| micro-friedman2015-body | https://pmc-oa-opendata.s3.amazonaws.com/PMC4434539.1/PMC4434539.1.xml; JATS Results s2-1,s2-3 through s2-7; selected s2-2 assembly paragraphs; full Discussion s3; Methods s4-1,s4-3,s4-4; main embedded captions inspected where returned; no pixels/raw supplement analysis | supports | W303 deletion/reconstitution, fluorescence and fixed-section TEM support MICOS architecture and subcomplex organization. Direct junction immuno-EM was unsuccessful; adjacency to crista markers supports localization inference. Mic19 copy-number regulation remains proposed. Methods explicitly use resin sections/TEM, not tomography: inherited F1 remains confirmed. |
| micro-friedman2014-body | https://pmc-oa-opendata.s3.amazonaws.com/PMC4075653.1/PMC4075653.1.xml; Complete S5 Internal determinants of mitochondrial division and abstract; other body sections not certified | context_only | Secondary synthesis supports distinct boundary/crista regions, junctions, MICOS scaffold and ATP-synthase ridges. This inspected extent does not independently establish all reduced-anaerobic-lineage exceptions or exact GO taxon constraints. |
| micro-davies2012-pmc | https://pmc.ncbi.nlm.nih.gov/articles/3427116/; Genuine primary HTML sections sec2,sec4,sec5,sec9,SEC3,sec12,sec13; no figure pixels or supplements | supports | Cryotomography in specified yeast strains resolves dimer rows on curved ridges; e/g/su4TM1 mutants retain monomers but lose typical lamellar cristae. Membrane-energy-driven assembly is a simulation/model, not a directly proven universal assembly sequence. |
| micro-paumard2002-pmc | https://pmc.ncbi.nlm.nih.gov/articles/125827/; Primary HTML sec3,sec7,sec8 excluding nested modelsec9; Methods sec11,sec13,sec14; no pixels or raw data | supports | Yeast e/g deletion alters inner-membrane morphology while rho+ ATP-synthesis function can remain. TEM/immunogold and mutant controls support architecture roles; no universal requirement for every membrane fold inferred. |
| micro-PMC4889329-body | https://pmc-oa-opendata.s3.amazonaws.com/PMC4889329.1/PMC4889329.1.xml; JATS Results s2-4 through s2-7, Table1 and Methods s4-4; Figure7 caption inspected separately; earlier aging Results not certified | supports | ConcA assays distinguish formation from Dnm1-dependent release and Atg5-dependent vacuolar routing. Table1 includes Tom71 cargo. Tom70/Tom71 loss blocks Cox7-GFP-marked formation in dnm1Δ under ConcA; the record incorrectly calls this cited experiment rapamycin-induced. Original carrier interpretation is revised by2024 evidence. |
| micro-PMC11320809-body | https://pmc-oa-opendata.s3.amazonaws.com/PMC11320809.1/PMC11320809.1.xml; JATS all main Results s3-s9 and Discussion s10; Methods s12/s14; Figure1/FigureS1 complete captions and permissions; exact figure pixels separately inspected | supports | Primary TEM/tomography, fluorescence and degron experiments support OMM-derived multilamellar domains with selective cargo and cytosolic enclosure in a subset. Closure, membrane number and protection are not invariant. Spherical Rap mean0.41µm,n104 and ConcA mean0.36µm,n49 with2h/200nM or500nM scopes agree; S288C-derived strains and link-only CC BY-NC-SA4 after6months confirmed. |
| micro-PMC11320589-body | https://pmc-oa-opendata.s3.amazonaws.com/PMC11320589.1/PMC11320589.1.xml; JATS complete Results s3,s6,s7 and Discussion s9; other Results/Methods not claimed read | supports | Functional N-terminal GFP-Oac1 is excluded; nonfunctional C-terminal fusion is mistargeted to OMM and enriched. OMM localization and assembly affect selectivity; assembled TOM-core proteins are not uniformly captured. Cargo-selection mechanism remains a model. |
| micro-PMC7588143-body | https://pmc-oa-opendata.s3.amazonaws.com/PMC7588143.1/PMC7588143.1.xml; JATS Results/Discussion s4,s5,s7 and s8 suppressor experiments (not its closing general summary); Methods s10/s12 | supports | ERMES/Gem1 requirements are tested conditional interventions and contact localization, not proof all contact machinery is constitutive MDC cargo. Tested psd1/ups1/crd1 perturbations did not impair formation here; retain contrast with2024 results. VPS13/ChiMERA versus Mcp1 suppressors differ. |
| micro-PMC10949074-body | https://pmc-oa-opendata.s3.amazonaws.com/PMC10949074.1/PMC10949074.1.xml; JATS complete Results s5-s8; abstract separately; no raw lipidomics, figure pixels or supplement tables | supports | CL depletion reduces MDC frequency without eliminating every small/large structure; PE-pathway disruption induces subsets. PSD1 rescue of mmm1Δ VPS13(D716H) and gem1Δ is condition-dependent/partial. Whole-cell or mitochondrial membrane fractions do not establish isolated-MDC lipid composition. |
| micro-PMC13605720-body | https://pmc-oa-opendata.s3.amazonaws.com/PMC13605720.1/PMC13605720.1.xml; Complete Full Text Availability notice only, no Results | context_only | The artifact is a license/unavailability stub, not a primary scientific body. Actual abstract and official reviewed-preprint metadata are separately inspected. |
| micro-PMC13278180-body | https://pmc-oa-opendata.s3.amazonaws.com/PMC13278180.1/PMC13278180.1.xml; Full Discussion S9 and abstract; no Results certified | context_only | Acute-adaptation/Snf1/Mig1 protein-load-buffering model remains a proposal; Discussion explicitly says available interventions do not isolate MDC-specific functional contribution. No new canonical component or edge inferred. |
| micro-elife111713 | https://elifesciences.org/reviewed-preprints/111713v1; Official citation title/authors/DOI/date/abstract metadata and Reviewed Preprint version banner only | context_only | Version v1 has DOI10.7554/eLife.111713.1 and reviewed-preprint status. Available publisher body is not certified as read Results; historical access notes remain historical. |
| micro-elife112436 | https://elifesciences.org/reviewed-preprints/112436v1; Official citation title/authors/DOI/date/abstract metadata and Reviewed Preprint version banner only | context_only | Version v1 has DOI10.7554/eLife.112436.1 and reviewed-preprint status. Available publisher body is not certified as read Results; historical access notes remain historical. |
| micro-wilson2024-Fig1 | https://pmc-oa-opendata.s3.amazonaws.com/PMC11320809.1/JCB_202307035_Fig1.jpg; Actual complete multipanel pixels viewed; panelC axes/shape label and microscopy modality/scale bars; captions and license in JATS | supports | PanelC uses micrometers and limits measurement to spherical MDCs. Figure1 mixes fluorescence, quantitative plots, thin-section TEM and immunogold, agreeing with OTHER modality and panel-specific scale bars. Exact historical media MD5 bf54de482c22108855cf3cc0f37eeb8d matches; no tracked image bytes changed. |
| micro-wilson2024-FigS1 | https://pmc-oa-opendata.s3.amazonaws.com/PMC11320809.1/JCB_202307035_FigS1.jpg; Actual complete multipanel pixels viewed; panelC axes/shape label and microscopy modality/scale bars; captions and license in JATS | supports | PanelC uses micrometers and limits measurement to spherical MDCs. FigureS1 axis is µm; initial small-glyph misreading was withdrawn after independent challenge and own original-detail reinspection. Caption agrees mean0.36µm,n49. Exact historical media MD5 5b329e0ccfd3de22c02265e8439eda9f matches; no tracked image bytes changed. |
| micro-image-independent-challenge | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/adversary-plaque/mdc-figs1-axis-challenge.json; Complete independent pixel/caption/record scope challenge receipt | context_only | Proposed axis-contradiction hypothesis rejected: actual glyph is µm and agrees with caption/body/record. No scientific or bundle image defect; only two inherited findings retained. |
| micro-catalogue | https://imodulondb.org/api/datasets; Complete official catalogue array; all organism names,keys and datasets | supports | No Saccharomyces cerevisiae,W303,BY/S288C or other named eukaryotic model-host match. No bacterial proxy is substituted for mitochondrial yeast pathways; no matched downstream search/summary applies. |
| micro-historical-runner | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Actual historical00:49Z command and PermissionError pyvenv.cfg | context_only | Historical optional runner unavailable, actual exit1 retained here, not a fresh execution. Current official catalogue fallback independently fetched/read. |
| check-qc | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/qc.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| check-labels | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/labels.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| check-trait-links | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/trait-links.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Native TraitMech link check passed. |
| check-vendored | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/vendored.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Pinned governed files match; native vendored check passed. |
| check-curies | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/curies.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| focused | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/focused-results.json; All twenty actual target schema/strict command outputs | supports | Ten schema and ten strict commands returned exit zero. |
| supplemental-pmid | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/pmid-chunks-receipt.json; Complete native-report PMID set checked with unchanged resolver in batches of at most fifty | supports | 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers remain unverified. |
| historical-adapter-runner-availability | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical runner invocation receipt, exact SHA256 reverified during PR2369 synthesis | context_only | Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS PermissionError reading the configured runner pyvenv.cfg. This is a retained historical availability observation, not a fresh attempt or a scientific validation failure. Native policy permits inspected source-catalogue fallback. |

## Limits And Additional Notes

- Maurer cleft and microneme boundary trio independent subreview: Read-only independent source review of four assigned records. Root owns repository/GitHub writes, issue dedup/publication, global gates, CI and queue. No record or original artifact was edited and no future final-head/CI result is certified.
- Maurer cleft and microneme boundary trio independent subreview: Maurer and microneme stale changes add REX1 and M2AP unreviewed examples plus history. Current identity/taxon/status/ORF names verify; biological membership is independently supported at cited experimental scope. A UniProt identity check is not causal or formation-necessity proof, and 3D7/VEG/ME49 representative entries are not all exact RH experimental constructs.
- Maurer cleft and microneme boundary trio independent subreview: Maurer has3UNREVIEWED examples/3distinct accessions and2COVERED nodes; Q6V0W9 is a fragment. Microneme has5occurrences/4distinct accessions because MIC2 repeats,2REVIEWED+3UNREVIEWED occurrences and2COVERED nodes. Lumen/membrane have0examples and0typednodes. All8native commands pass only these exact inventories.
- Maurer cleft and microneme boundary trio independent subreview: Current REX1 and M2AP locus identifiers are ORF-name fields, not formal primary geneName fields. Correct common protein/locus identities support examples, but loose primary-name prose is not independently certified as an exact authority-field statement. No separate identity/causality defect is inferred from that phrasing alone.
- Maurer cleft and microneme boundary trio independent subreview: Cooke genuine BioC main text was read through main adhesion-assay Methods, with all Results/Discussion and Figure1–7 captions; supplements and pixels were not inspected. SBP1 genetic trafficking effects remain distinct from Spycher MAHRP1 experiments and from direct protein binding.
- Maurer cleft and microneme boundary trio independent subreview: Current Spycher saved source evidence is exact metadata/complete primary abstract. An initial successful browser view also displayed Summary/Introduction and Results through Figure5 before complementation heading; later direct403 and browser timeouts did not provide the rest. No saved complete-body hash, full-body access or exact timestamp for that unpersisted browser observation is invented; findings use saved primary abstract plus Cooke body.
- Maurer cleft and microneme boundary trio independent subreview: Huynh2006 genuine BioC complete Introduction/Results/Discussion, Figure1–7 captions and enumerated plasmid/parasite/primer/Western/secretion/invasion Methods were read; Table1 numerical contents, pixels/videos/supplements and unenumerated Methods were not inspected. Residual invasion, RH-derived strain and unchanged other microneme cargos limit necessity claims.
- Maurer cleft and microneme boundary trio independent subreview: Carruthers1997,Huynh2003,Brown2016 and the7exact protein-location PMIDs are complete primary-abstract evidence in this current review; their full-text fallback attempts failed or returned service packets. Carruthers2008 and Lanzer2006 are complete secondary abstracts only. Blisnick2000 is complete primary abstract only. Unavailable body access is not scientific refutation.
- Maurer cleft and microneme boundary trio independent subreview: Dubois2019 accepted review manuscript was read only through extracted text lines40–578 (Abstract through signaling cascade). Later sections, Table1 and figures/pixels were not comprehensively inspected. It is secondary synthesis, not direct reanalysis of every primary experiment, and no reuse licence or image claim is inferred.
- Maurer cleft and microneme boundary trio independent subreview: Exact single-accession InterPro lookups and exact reviewed gene queries have bounded scopes; absence in an endpoint is not biological absence. SBP1 automatic Mediator-like hit is not adopted as exact family identity; heterogeneous protein classes are allowed. Native CausalNode explicitly allows protein complexes under GENE_OR_PROTEIN, so MIC2-M2AP node type is not a new finding.
- Maurer cleft and microneme boundary trio independent subreview: All4original adapter rows are explicit expression-only exclusions, not omissions. Whole molecular/pathway narratives require coverage assessment, including the otherwise sparse lumen/membrane. Fresh complete official catalogue contains no matching parasite host; no unrelated bacterial downstream query or biological absence claim. Runner receipt remains actual00:49Zhistorical failure, not a new invocation.
- Maurer cleft and microneme boundary trio independent subreview: Twenty-nine repository inputs were actually used:17common policy/schema/native files,4current targets and8original artifacts. The microneme trio supplies mutually assigned boundary context without extra unfrozen neighbors. Original findings are retained exactly for their own targets; no neighboring/group/category issue is newly resolved. No maintained image, measured physical property, trait or verbatim snippet is asserted.
- Methane-oxidizing organelle, micronucleus and posterior vacuole independent subreview: Assigned source review covers methane-oxidizing organelle, micronucleus and posterior vacuole. One stale methane target was substantively refreshed; first two scientifically pass_with_limitations, posterior needs_curation for two inherited minor findings. No new scientific finding or fabricated predecessor.
- Methane-oxidizing organelle, micronucleus and posterior vacuole independent subreview: Original three pairs native validate/render with14/16/14 historical input hashes matching retained source. No original mutated. Historical record fixes/issues1290/778 are not terminally re-adjudicated; optional DNA/composition grounding gaps are not automatically required defects.
- Methane-oxidizing organelle, micronucleus and posterior vacuole independent subreview: Current policies were hash-compared to the independently read PR2368 set and unchanged. Record-review skill/profile and CausalNode contract freshly reread; protein-complex use of GENE_OR_PROTEIN is explicitly permitted. No automatic graph retyping issue.
- Methane-oxidizing organelle, micronucleus and posterior vacuole independent subreview: Methane sources Zhu2022 andWhiddon2019 are genuine primary JATS selected sections/captions as evidence locators state; no figure pixels/raw data assessed. Bath arrays and20Z fluorescence contexts remain distinct; static continuity/array activity correlation is not full biogenesis or causal sufficiency.
- Methane-oxidizing organelle, micronucleus and posterior vacuole independent subreview: Stolyar2001 full body routes returned404/no-result despite BioC HTTP200; complete primary abstract supports only narrow gene-expression note. Three native localization PMIDs assessed as complete abstracts/native evidence-pointer verification; Smith2011 Methylocystis strainM is not substituted for Bath direct experiment.
- Methane-oxidizing organelle, micronucleus and posterior vacuole independent subreview: Q603F1 is unreviewed Bath pmoC1 identity with two locus names, not exact membership/unique locus/necessity evidence. Exact pmoC searches returnedzero, primary pmoC1 search foundQ603F1; alias boundary is not biological absence. No guessed chemical/complex/family CURIE was added.
- Methane-oxidizing organelle, micronucleus and posterior vacuole independent subreview: Hamilton selected Introduction, assembly Results and Methods were read; no raw sequencing or figure-pixel assessment. Mature MIC scope retains assembly uncertainties and does not claim absence of all developmental transcription.
- Methane-oxidizing organelle, micronucleus and posterior vacuole independent subreview: Findley2005 selected p111–115 PDF text, Troemel2015 mainbody and Jaroenlak2020/Sharma2024 selected primary bodies/captions establish posterior topology and the two narrow source/causal defects. No figure pixels/videos/raw tomograms inspected for these targets;2022 secondary chapter abstract only. No quantified phylum prevalence or exact swelling mechanism established.
- Methane-oxidizing organelle, micronucleus and posterior vacuole independent subreview: Only methane and micronucleus original exclusions are adapter defects in this slice. Posterior has genuine sparse morphology/physical-physiological scope with unresolved molecular composition. Fresh official catalogue has no exact represented hosts; no matched downstream module query applies, and unrelated bacterial/archaeal coverage is not a proxy.
- Methane-oxidizing organelle, micronucleus and posterior vacuole independent subreview: Historical00:49Z runner PermissionError remains historical unavailable, not a fresh failed/successful run. Actual six native protein commands pass with methane3examples(2reviewed1unreviewed)/1coverednode and other2records0/0. Native empty coverage does not waive positive molecular assertions.
- Methane-oxidizing organelle, micronucleus and posterior vacuole independent subreview: Auxiliary MDC FigureS1 challenge was separately scoped and receipt-bound: independent pixels and caption support µm; proposed axis contradiction rejected. That fourth local target was already frozen and used only for its physical-property note, not given a new full-record verdict.
- Methane-oxidizing organelle, micronucleus and posterior vacuole independent subreview: Root owns global gates, issue publication and final lifecycle. This report does not precertify final-head CI/merge. Scratch native preflight establishes contract validity, not automatic scientific truth. All reviewer writes are scratch only.
- Mitochondrial crista, crista junction and derived compartment independent subreview: Assigned scope: three complete mitochondrial records only. Junction stale MICOS typing/history substantively reassessed; crista and MDC current bytes unchanged. Exactly two inherited minor scientific findings retain repository/review/F1 predecessors. Closed grouped2419 is historical context only.
- Mitochondrial crista, crista junction and derived compartment independent subreview: All current public source reads have actual fresh receipt timestamps and exact locators. Body reading is restricted to listed sections; Davies/Paumard S3 archive404 responses are not scientific text, while genuine PMC HTML was successfully read. Friedman2014 is secondary context. No unseen full body or raw experimental reanalysis claimed.
- Mitochondrial crista, crista junction and derived compartment independent subreview: Only Wilson2024 Figure1/FigureS1 actual pixels were inspected. Caption/Methods/license and shape-specific means agree; a proposed axis contradiction was withdrawn after independent challenge and own original-detail review. No image-related finding remains. Movies, raw tomography, lipidomics and other figure pixels/supplement datasets were not reanalyzed.
- Mitochondrial crista, crista junction and derived compartment independent subreview: General Eukaryota prevalence, precise GO taxon constraints and reduced anaerobic-lineage exceptions remain bounded unknowns at inspected extent. This is not a biological refutation or universal absence inference.
- Mitochondrial crista, crista junction and derived compartment independent subreview: Native verifier has0examples/0typed nodes for crista and junction, with the junction STRUCTURE-node Mic60 xref independently verified; MDC has3examples/0typed nodes. Success is not experimental localization, association, or formation necessity. Exact reviewed strain searches are bounded to stated query/date/result limits.
- Mitochondrial crista, crista junction and derived compartment independent subreview: 2020/2024 lipid-perturbation differences remain unresolved.2026 preprint models retain preprint status and limited access; current publisher metadata is not certification of unread Results. Conditional dependencies, partial bypass, cargo enrichment and permanent isolation remain distinct.
- Mitochondrial crista, crista junction and derived compartment independent subreview: All three explicit original source-adapter exclusions need corrected rationale; fresh catalogue lacks the actual yeast hosts, so no matched downstream module check applies. Historical00:49Z runner failure remains historical, not a fresh invocation.
- Mitochondrial crista, crista junction and derived compartment independent subreview: Read-only repository/Git/GitHub review. Root owns global QC, final CI, issue dedup and publication; no future gate result borrowed. Native scripts are frozen execution inputs with selected coverage-filter inspection, not exhaustive code review. Curation actions are proposed separately; no maintained record/status/history was edited.
- Historical observations remain immutable; their old checks are not represented as current-head execution.
- The adapter runner was not rerun after the canary established OS access failure. Catalogue-based coverage is assessed directly; fresh and reused responses retain actual access timestamps.
- Native label checks include 923 no-adapter skips. Native identifier checks include 909 PMID transport failures and 254 skipped identifiers; bounded supplemental checks independently resolve the 909 PMIDs.
- Scientific record-curation findings stay in separate issues; no record is edited by this review PR.
- Final trusted-base post-save review-check, exact-head independent acceptance, final-head CI and merge-group CI occur after saving this immutable observation and are not represented here as already completed.
- All ten original YAML/Markdown pairs remain unchanged. Current main was merged normally and pushed without force.
- This explicit issue-bearing ten-record cohort follows native persistence policy. Inherited scientific findings retain stable keys and exact predecessor repository/review/finding identities; any new finding has no invented predecessor.
- Issue2721 tracks four stale targets: added REX1/Q8I2G1 at Maurer cleft, pmoC1/Q603F1 at methane-oxidizing organelle, M2AP/S8GDJ1 at microneme, and MICOS STRUCTURE retyping at crista junction. Native identities, status, taxonomy, membership and complex/subunit scope are substantively reassessed.
- Issue2722 tracks nine unsupported expression-only applicability exclusions. The posterior-vacuole record has a genuine sparse physical-topology/expansion exclusion with composition unresolved, not a tenth invented defect. All ten originals contained explicit exclusions; none was missing.
- Source commit 61d3617ae8700b99198e2aaf01f3b2437933de6c is retained by tag review-base/pr2369-current-record-followup-20261103.
- CLAUDE.md aliases AGENTS.md; canonical regular AGENTS.md bytes are frozen. Every used local context input is frozen before its assessment.
- Fresh and reused source snapshots retain actual access times and inspection tiers. Native identifier identity does not independently establish structure membership, experimental intervention scope or assembly necessity.
- All twenty native protein commands returned zero. Maurer cleft has three unreviewed examples and two COVERED nodes; methane organelle has two reviewed and one unreviewed examples with one COVERED node; microneme has five example occurrences across four distinct accessions (two reviewed and three unreviewed occurrences) and two COVERED nodes. MIC2 appears in two distinct component contexts. MDC has three reviewed examples and zero typed molecular nodes. The other six targets have no examples or typed molecular nodes. Native success does not certify every narrative claim.
- Current CausalNode schema explicitly permits protein families and complexes as GENE_OR_PROTEIN nodes. The pMMO and MIC2-M2AP node enums alone are not scientific defects. Existing material-to-membrane identity and whole-complex lumen topology concerns are assessed separately.
- Closed grouped issue2419 is historical context for the crista-junction MICOS node change. No broad disposition of the five grouped records or their findings is made. Native-validator2514 remains open and reused.
- Final trusted-base review-check, exact-head independent acceptance, final-head CI and merge-group CI occur after this immutable observation and are not represented as already completed.
- A tentative FigureS1 axis-provenance contradiction was independently challenged and withdrawn after exact full-resolution pixel inspection. The axis reads micrometers and agrees with the caption’s 0.36 micrometers (n49); no scientific or bundle finding is created from the initial glyph misread. The separate assay-condition finding remains.
- After MICOS retyping, the native protein verifier skips xrefs on the crista-junction STRUCTURE node. Its zero-example/zero-typed-node pass therefore does not validate Mic60/P36112; the independent reviewer separately inspects fresh authority identity and treats that xref as a representative subunit, not whole-complex equivalence.
- The final scientific set consists of eight inherited findings (one major, seven minor) on Maurer cleft, microneme, posterior vacuole, crista junction and MDC. Five other targets retain qualified passes. No new finding or predecessor is invented, and scientific curation remains open separately from the two bundle fixes.
- Scientific findings are tracked as issues2723–2730, in exact finding-key order recorded in the issue ledger; all remain open. Bundle fixes2721/2722 do not close scientific curation. Existing validator2514 remains reused, and closed grouped2419 remains historical context only.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T161755Z-pr2369-current-record-followup
kind: batch
repository: CultureBotAI/CellStructureMech
title: 'PR 2369: current-input review of ten records and adversarial follow-up'
started_at: '2026-11-03T16:06:50.712558Z'
finished_at: '2026-11-03T16:17:55Z'
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
summary: 'All ten records are reassessed against current main with47 frozen local
  inputs. Four stale reviews are substantively refreshed: Maurer cleft REX1, methane-organelle
  pmoC1 and microneme M2AP additions, plus crista-junction MICOS typing. Nine unsupported
  expression-only source exclusions are corrected; the posterior-vacuole record retains
  a justified sparse physical-scope exclusion. Eight inherited scientific findings
  remain (one major, seven minor) across five records; five other records receive
  qualified passes within explicit source limits. Bundle issues2721 and2722 are addressed
  by the successor. Scientific curation and reused validator2514 remain separate and
  open. No record is edited.'
source:
  git_revision: 61d3617ae8700b99198e2aaf01f3b2437933de6c
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
  - path: data/structures/membrane_organelle/maurer_s_cleft.yaml
    sha256: 8eed10ce23b6b30eb30d69fc14e8686bc350a5906ac9b7fbe4b6601ebe3616a9
    role: target
  - path: data/structures/membrane_organelle/methane_oxidizing_organelle.yaml
    sha256: 8d513f399ed2555737573ae9d0c888514408062fcd5f2ec60bc19bad9e93f2c8
    role: target
  - path: data/structures/membrane_organelle/microneme.yaml
    sha256: 8c260a40b26529407d136e11511c846d6554d975d54a3a45f444876aa0b51da8
    role: target
  - path: data/structures/membrane_organelle/microneme_lumen.yaml
    sha256: c40d221eea42af12fcb06a6a5dbcc7d3592f289ad31f52a275acad4d6666af38
    role: target
  - path: data/structures/membrane_organelle/microneme_membrane.yaml
    sha256: f3c40aeb98a8d3eec6950ea6a3875db63372a5e72c66a75130e4ec821f0dc4ad
    role: target
  - path: data/structures/membrane_organelle/micronucleus.yaml
    sha256: fe6086eb62e1499109082d20f9a25ff776a68482d0ab89253469f6f3bfcbb8c1
    role: target
  - path: data/structures/membrane_organelle/microsporidian_posterior_vacuole.yaml
    sha256: db2c2e1271b64aa7037885eeb2f1e39c6e3ee5d769b83e8374ed96d2e768f6b8
    role: target
  - path: data/structures/membrane_organelle/mitochondrial_crista.yaml
    sha256: d7f734bbcd5e5af1c899f0c2034d2bc72656eaeb71d5861cf185613c65f4bda6
    role: target
  - path: data/structures/membrane_organelle/mitochondrial_crista_junction.yaml
    sha256: b994a1d51d584f4614c50fb97db455db7a6cf72b2f886da419fcbf3b77ba3adb
    role: target
  - path: data/structures/membrane_organelle/mitochondrial_derived_compartment.yaml
    sha256: c7a83f3db0bb05a7016b5c3991e79bd21c9a6ec4f723335fc3a1d14864d1c5c8
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
  - path: reviews/structured/20261022T022231Z-maurer-s-cleft-audit/review.md
    sha256: 760f0ec5009219cbac8001ec80d0d86618a4bea19a2d9f9451741b00a3989236
    role: context
  - path: reviews/structured/20261022T022231Z-maurer-s-cleft-audit/review.yaml
    sha256: 6236c1a6388454222604a8d54bcc081a077c2cf7edd83c6ddc6f0e174687cd68
    role: context
  - path: reviews/structured/20261022T022232Z-methane-oxidizing-organelle-audit/review.md
    sha256: 1be99f4c97ee95ebb48d75be40c4ca14dab76cd72c8c4f9e691127bdc6e9048b
    role: context
  - path: reviews/structured/20261022T022232Z-methane-oxidizing-organelle-audit/review.yaml
    sha256: 0864d9f497ea8b445ff162b6c6bbfe2bb72aa8e7450f0d7032ca197679e9151b
    role: context
  - path: reviews/structured/20261022T022233Z-microneme-audit/review.md
    sha256: e6a83bed3bfb153b35f4b6f7f4d33ff47ad185883856fb224b5f03953eaf098f
    role: context
  - path: reviews/structured/20261022T022233Z-microneme-audit/review.yaml
    sha256: a2e2cd863d1912f27d2cec34a222e508a9d686de13d7def030eb53de90de8b88
    role: context
  - path: reviews/structured/20261022T022235Z-microneme-lumen-audit/review.md
    sha256: 3e45af3f890b7ab53ef0aa32a5f95f74b395802f5ca48eb7d63c560171081e97
    role: context
  - path: reviews/structured/20261022T022235Z-microneme-lumen-audit/review.yaml
    sha256: 7eed59c251a3aaf29f4f672df03c7354b85a3606324f2b669a21ea1b5b8353d8
    role: context
  - path: reviews/structured/20261022T022236Z-microneme-membrane-audit/review.md
    sha256: 8c1a4d1c48fc4872a2817c3e1f7ca219d5bd7624fa09695874f674c0295785aa
    role: context
  - path: reviews/structured/20261022T022236Z-microneme-membrane-audit/review.yaml
    sha256: bcacc4edb8d3ad6e959d23de9b6e4429b62b0c84053107f71bc013b288488469
    role: context
  - path: reviews/structured/20261022T022237Z-micronucleus-audit/review.md
    sha256: 3c0380e872ca2de7e3bbc47a390386945dd9f92a15627074642024f94951dee7
    role: context
  - path: reviews/structured/20261022T022237Z-micronucleus-audit/review.yaml
    sha256: de79f648d1fa9ea63b8a29ce2725c2a3d8e6c81cc35ca3e6f0e41c2aaee0367c
    role: context
  - path: reviews/structured/20261022T022238Z-microsporidian-posterior-vacuole-audit/review.md
    sha256: 9994b2f955d664d3b193dc52a0abdef19199c3b95afbf5e7dbc936e484f44395
    role: context
  - path: reviews/structured/20261022T022238Z-microsporidian-posterior-vacuole-audit/review.yaml
    sha256: b3fb563d38edb33f94e0de1bdf485a430468f9c8695f82d83d04ebbdb61390e8
    role: context
  - path: reviews/structured/20261022T022238Z-mitochondrial-crista-audit/review.md
    sha256: 39077c2dd12cf149b74ca631d8bff5225fc5fef64a32fc0efe9d4a19592c2d06
    role: context
  - path: reviews/structured/20261022T022238Z-mitochondrial-crista-audit/review.yaml
    sha256: 8e7fcd2bf0433a33698142957cc06549648ff14c8fe8bfe047dd7cc22530f5ee
    role: context
  - path: reviews/structured/20261022T022239Z-mitochondrial-crista-junction-audit/review.md
    sha256: 21d367dba532d55e69e4da44b8e82cf4946131375e7e5d2ec4231a9a92402f34
    role: context
  - path: reviews/structured/20261022T022239Z-mitochondrial-crista-junction-audit/review.yaml
    sha256: 61c6e878b42552da90908c4096400f6a3dd72adecbbdcc5dbd89e76134725a1c
    role: context
  - path: reviews/structured/20261022T022241Z-mitochondrial-derived-compartment-audit/review.md
    sha256: 95935f654f723434645fd06fe363042ab310267a44eea2ecad3867ddf6cc62a2
    role: context
  - path: reviews/structured/20261022T022241Z-mitochondrial-derived-compartment-audit/review.yaml
    sha256: 2d4970f0670d8b53508e37cfd606b0f5089087230f7ead44afbfd546f819488e
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
- target_id: GO:0020036
  path: data/structures/membrane_organelle/maurer_s_cleft.yaml
  label: Maurer's cleft
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/maurer_s_cleft.yaml
    role: maintained scientific record
- target_id: GO:0044227
  path: data/structures/membrane_organelle/methane_oxidizing_organelle.yaml
  label: methane-oxidizing organelle
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/methane_oxidizing_organelle.yaml
    role: maintained scientific record
- target_id: GO:0020009
  path: data/structures/membrane_organelle/microneme.yaml
  label: microneme
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/microneme.yaml
    role: maintained scientific record
- target_id: GO:0034494
  path: data/structures/membrane_organelle/microneme_lumen.yaml
  label: microneme lumen
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/microneme_lumen.yaml
    role: maintained scientific record
- target_id: GO:0033163
  path: data/structures/membrane_organelle/microneme_membrane.yaml
  label: microneme membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/microneme_membrane.yaml
    role: maintained scientific record
- target_id: GO:0031040
  path: data/structures/membrane_organelle/micronucleus.yaml
  label: micronucleus
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/micronucleus.yaml
    role: maintained scientific record
- target_id: cellstructuremech:microsporidian_posterior_vacuole
  path: data/structures/membrane_organelle/microsporidian_posterior_vacuole.yaml
  label: microsporidian posterior vacuole
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/microsporidian_posterior_vacuole.yaml
    role: maintained scientific record
- target_id: GO:0030061
  path: data/structures/membrane_organelle/mitochondrial_crista.yaml
  label: mitochondrial crista
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/mitochondrial_crista.yaml
    role: maintained scientific record
- target_id: GO:0044284
  path: data/structures/membrane_organelle/mitochondrial_crista_junction.yaml
  label: mitochondrial crista junction
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/mitochondrial_crista_junction.yaml
    role: maintained scientific record
- target_id: cellstructuremech:mitochondrial_derived_compartment
  path: data/structures/membrane_organelle/mitochondrial_derived_compartment.yaml
  label: mitochondrial-derived compartment
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/mitochondrial_derived_compartment.yaml
    role: maintained scientific record
scope:
  description: Exact ten-record PR cohort reassessed against current main 2e0792c49e1040ad8b89b9a5f7c81fea69c995cc.
    Changed inputs are substantively reassessed. Scientific records remain unchanged.
  selection: Complete cohort of ten maintained records reviewed in original PR head
    5a91e2c6b6d716170c0a3414ebadc6578d261632.
  coverage: full
  population_size: 10
  reviewed_target_ids:
  - GO:0020036
  - GO:0044227
  - GO:0020009
  - GO:0034494
  - GO:0033163
  - GO:0031040
  - cellstructuremech:microsporidian_posterior_vacuole
  - GO:0030061
  - GO:0044284
  - cellstructuremech:mitochondrial_derived_compartment
checks:
- check_id: qc
  name: Full native QC
  status: passed
  required: true
  target_ids:
  - GO:0020036
  - GO:0044227
  - GO:0020009
  - GO:0034494
  - GO:0033163
  - GO:0031040
  - cellstructuremech:microsporidian_posterior_vacuole
  - GO:0030061
  - GO:0044284
  - cellstructuremech:mitochondrial_derived_compartment
  command: just qc
  exit_code: 0
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  scope_note: Actual local execution at main-merge head 61d3617ae8700b99198e2aaf01f3b2437933de6c.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-qc
- check_id: labels
  name: Native label correspondence
  status: passed
  required: true
  target_ids:
  - GO:0020036
  - GO:0044227
  - GO:0020009
  - GO:0034494
  - GO:0033163
  - GO:0031040
  - cellstructuremech:microsporidian_posterior_vacuole
  - GO:0030061
  - GO:0044284
  - cellstructuremech:mitochondrial_derived_compartment
  command: just validate-products
  exit_code: 0
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  scope_note: Actual local execution at main-merge head 61d3617ae8700b99198e2aaf01f3b2437933de6c.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-labels
- check_id: trait-links
  name: TraitMech references
  status: passed
  required: true
  target_ids:
  - GO:0020036
  - GO:0044227
  - GO:0020009
  - GO:0034494
  - GO:0033163
  - GO:0031040
  - cellstructuremech:microsporidian_posterior_vacuole
  - GO:0030061
  - GO:0044284
  - cellstructuremech:mitochondrial_derived_compartment
  command: just check-trait-links --check
  exit_code: 0
  summary: Native TraitMech link check passed.
  scope_note: Actual local execution at main-merge head 61d3617ae8700b99198e2aaf01f3b2437933de6c.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-trait-links
- check_id: vendored
  name: Pinned governed files
  status: passed
  required: true
  target_ids:
  - GO:0020036
  - GO:0044227
  - GO:0020009
  - GO:0034494
  - GO:0033163
  - GO:0031040
  - cellstructuremech:microsporidian_posterior_vacuole
  - GO:0030061
  - GO:0044284
  - cellstructuremech:mitochondrial_derived_compartment
  command: just vendored-check
  exit_code: 0
  summary: Pinned governed files match; native vendored check passed.
  scope_note: Actual local execution at main-merge head 61d3617ae8700b99198e2aaf01f3b2437933de6c.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-vendored
- check_id: curies
  name: Native identifier resolver
  status: passed
  required: true
  target_ids:
  - GO:0020036
  - GO:0044227
  - GO:0020009
  - GO:0034494
  - GO:0033163
  - GO:0031040
  - cellstructuremech:microsporidian_posterior_vacuole
  - GO:0030061
  - GO:0044284
  - cellstructuremech:mitochondrial_derived_compartment
  command: just check-curies
  exit_code: 0
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  scope_note: Actual local execution at main-merge head 61d3617ae8700b99198e2aaf01f3b2437933de6c.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-curies
- check_id: focused-0
  name: validate GO:0020036
  status: passed
  required: true
  target_ids:
  - GO:0020036
  command: just validate data/structures/membrane_organelle/maurer_s_cleft.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-1
  name: validate-strict GO:0020036
  status: passed
  required: true
  target_ids:
  - GO:0020036
  command: just validate-strict data/structures/membrane_organelle/maurer_s_cleft.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-2
  name: validate GO:0044227
  status: passed
  required: true
  target_ids:
  - GO:0044227
  command: just validate data/structures/membrane_organelle/methane_oxidizing_organelle.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-3
  name: validate-strict GO:0044227
  status: passed
  required: true
  target_ids:
  - GO:0044227
  command: just validate-strict data/structures/membrane_organelle/methane_oxidizing_organelle.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-4
  name: validate GO:0020009
  status: passed
  required: true
  target_ids:
  - GO:0020009
  command: just validate data/structures/membrane_organelle/microneme.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-5
  name: validate-strict GO:0020009
  status: passed
  required: true
  target_ids:
  - GO:0020009
  command: just validate-strict data/structures/membrane_organelle/microneme.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-6
  name: validate GO:0034494
  status: passed
  required: true
  target_ids:
  - GO:0034494
  command: just validate data/structures/membrane_organelle/microneme_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-7
  name: validate-strict GO:0034494
  status: passed
  required: true
  target_ids:
  - GO:0034494
  command: just validate-strict data/structures/membrane_organelle/microneme_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-8
  name: validate GO:0033163
  status: passed
  required: true
  target_ids:
  - GO:0033163
  command: just validate data/structures/membrane_organelle/microneme_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-9
  name: validate-strict GO:0033163
  status: passed
  required: true
  target_ids:
  - GO:0033163
  command: just validate-strict data/structures/membrane_organelle/microneme_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-10
  name: validate GO:0031040
  status: passed
  required: true
  target_ids:
  - GO:0031040
  command: just validate data/structures/membrane_organelle/micronucleus.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-11
  name: validate-strict GO:0031040
  status: passed
  required: true
  target_ids:
  - GO:0031040
  command: just validate-strict data/structures/membrane_organelle/micronucleus.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-12
  name: validate cellstructuremech:microsporidian_posterior_vacuole
  status: passed
  required: true
  target_ids:
  - cellstructuremech:microsporidian_posterior_vacuole
  command: just validate data/structures/membrane_organelle/microsporidian_posterior_vacuole.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-13
  name: validate-strict cellstructuremech:microsporidian_posterior_vacuole
  status: passed
  required: true
  target_ids:
  - cellstructuremech:microsporidian_posterior_vacuole
  command: just validate-strict data/structures/membrane_organelle/microsporidian_posterior_vacuole.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-14
  name: validate GO:0030061
  status: passed
  required: true
  target_ids:
  - GO:0030061
  command: just validate data/structures/membrane_organelle/mitochondrial_crista.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-15
  name: validate-strict GO:0030061
  status: passed
  required: true
  target_ids:
  - GO:0030061
  command: just validate-strict data/structures/membrane_organelle/mitochondrial_crista.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-16
  name: validate GO:0044284
  status: passed
  required: true
  target_ids:
  - GO:0044284
  command: just validate data/structures/membrane_organelle/mitochondrial_crista_junction.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-17
  name: validate-strict GO:0044284
  status: passed
  required: true
  target_ids:
  - GO:0044284
  command: just validate-strict data/structures/membrane_organelle/mitochondrial_crista_junction.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-18
  name: validate cellstructuremech:mitochondrial_derived_compartment
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitochondrial_derived_compartment
  command: just validate data/structures/membrane_organelle/mitochondrial_derived_compartment.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-19
  name: validate-strict cellstructuremech:mitochondrial_derived_compartment
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitochondrial_derived_compartment
  command: just validate-strict data/structures/membrane_organelle/mitochondrial_derived_compartment.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: supplemental-pmid
  name: Supplemental bounded PMID authority checks
  status: passed
  required: true
  target_ids:
  - GO:0020036
  - GO:0044227
  - GO:0020009
  - GO:0034494
  - GO:0033163
  - GO:0031040
  - cellstructuremech:microsporidian_posterior_vacuole
  - GO:0030061
  - GO:0044284
  - cellstructuremech:mitochondrial_derived_compartment
  command: .venv/bin/python /private/tmp/cellstructure-batches-2346-2397-20261103/check_pmid_chunks.py
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369
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
  - GO:0020036
  - GO:0044227
  - GO:0020009
  - GO:0034494
  - GO:0033163
  - GO:0031040
  - cellstructuremech:microsporidian_posterior_vacuole
  - GO:0030061
  - GO:0044284
  - cellstructuremech:mitochondrial_derived_compartment
  summary: Nine original expression-only exclusions were reassessed against whole-record
    molecular/pathway claims and fresh complete official iModulonDB catalogue coverage.
    No matching Plasmodium/Toxoplasma, Methylococcus Bath, Tetrahymena or Saccharomyces
    experimental-host dataset was found in the documented complete catalogue inspection.
    The sparse posterior-vacuole record has a justified physical morphology/expansion
    exclusion with unresolved molecular composition. No foreign-host proxy or biological-absence
    inference is made. Historical runner unavailability is not presented as a fresh
    invocation.
  evidence_ids:
  - septin-catalogue
  - plaque-catalogue
  - plaque-historical-runner
  - micro-catalogue
- check_id: independent-scientific-review
  name: Independent claim-level source review
  status: passed
  required: true
  target_ids:
  - GO:0020036
  - GO:0044227
  - GO:0020009
  - GO:0034494
  - GO:0033163
  - GO:0031040
  - cellstructuremech:microsporidian_posterior_vacuole
  - GO:0030061
  - GO:0044284
  - cellstructuremech:mitochondrial_derived_compartment
  summary: Three read-only reviewers covered the complete ten-record cohort, including
    changed inputs, with explicit scientific findings and source-access limits. Final
    artifact/head acceptance occurs after saving.
  evidence_ids:
  - septin-review-policy
  - septin-curation-policy
  - septin-schema-policy
  - septin-graph-policy
  - septin-protein-policy
  - septin-go
  - septin-ancestors-0020036
  - septin-ancestors-0020009
  - septin-ancestors-0034494
  - septin-ancestors-0033163
  - septin-tax5833
  - septin-tax36329
  - septin-tax2759
  - septin-tax5794
  - septin-tax5811
  - septin-tax432359
  - septin-tax508771
  - septin-protein-Q6V0W9
  - septin-protein-Q8I2G1
  - septin-protein-Q9NFF5
  - septin-protein-O00834
  - septin-protein-B6KAM0
  - septin-protein-S8F9G8
  - septin-protein-S8GDJ1
  - septin-lanzer2006-meta
  - septin-blisnick2000-meta
  - septin-cooke2006-meta
  - septin-spycher2008-meta
  - septin-carruthers2008-meta
  - septin-dubois2019-meta
  - septin-huynh2003-meta
  - septin-huynh2006-meta
  - septin-brown2016-meta
  - septin-pmid-meta
  - septin-cooke2006-bioc
  - septin-huynh2006-bioc
  - septin-dubois2019-pdf
  - plaque-policy
  - plaque-rubric
  - plaque-graph-rubric
  - plaque-protein-contract
  - plaque-schema-policy
  - plaque-go
  - plaque-tax2
  - plaque-tax243233
  - plaque-tax5911
  - plaque-tax6029
  - plaque-tax6039
  - plaque-protein-Q607G3
  - plaque-protein-G1UBD1
  - plaque-protein-Q603F1
  - plaque-PMID12379148
  - plaque-PMID15674245
  - plaque-PMID22013879
  - plaque-zhu2022-meta
  - plaque-whiddon2019-meta
  - plaque-hamilton2016-meta
  - plaque-findley2005-meta
  - plaque-jaroenlak2020-meta
  - plaque-sharma2024-meta
  - plaque-troemel2015-meta
  - plaque-zhu2022-body
  - plaque-whiddon2019-body
  - plaque-stolyar2001-meta
  - plaque-stolyar2001-body
  - plaque-stolyar2001-bioc
  - plaque-hamilton2016-body
  - plaque-findley2005-pdf
  - plaque-troemel2015-body
  - plaque-jaroenlak2020-body
  - plaque-sharma2024-body
  - plaque-jaroenlak2022-meta
  - plaque-catalogue
  - micro-policy
  - micro-component-policy
  - micro-graph-policy
  - micro-go
  - micro-go0030061-ancestors
  - micro-go0044284-ancestors
  - micro-tax2759
  - micro-tax4932
  - micro-tax559292
  - micro-uo0000017
  - micro-protein-P36112
  - micro-protein-P07213
  - micro-protein-P38825
  - micro-protein-P54861
  - micro-family-P07213
  - micro-family-P38825
  - micro-family-P54861
  - micro-IPR005687
  - micro-IPR022812
  - micro-friedman2015-meta
  - micro-davies2012-meta
  - micro-paumard2002-meta
  - micro-friedman2014-meta
  - micro-hughes2016-meta
  - micro-wilson2024-meta
  - micro-cargo2024-meta
  - micro-ermes2020-meta
  - micro-lipids2024-meta
  - micro-preprintA2026-meta
  - micro-preprintB2026-meta
  - micro-PMID42798366
  - micro-PMID42327138
  - micro-friedman2015-body
  - micro-friedman2014-body
  - micro-davies2012-pmc
  - micro-paumard2002-pmc
  - micro-PMC4889329-body
  - micro-PMC11320809-body
  - micro-PMC11320589-body
  - micro-PMC7588143-body
  - micro-PMC10949074-body
  - micro-PMC13605720-body
  - micro-PMC13278180-body
  - micro-elife111713
  - micro-elife112436
  - micro-wilson2024-Fig1
  - micro-wilson2024-FigS1
- check_id: historical-adapter-runner
  name: Retained historical adapter runner availability
  status: unavailable
  required: false
  target_ids:
  - GO:0020036
  - GO:0044227
  - GO:0020009
  - GO:0034494
  - GO:0033163
  - GO:0031040
  - cellstructuremech:microsporidian_posterior_vacuole
  - GO:0030061
  - GO:0044284
  - cellstructuremech:mitochondrial_derived_compartment
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
- check_id: maurer_s_cleft-uniprot-verify
  name: Native maurer s cleft UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0020036
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/maurer_s_cleft.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Three unreviewed examples and two
    COVERED nodes. Native identity is distinct from source-supported trafficking/localization
    and necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-maurer_s_cleft-verify
- check_id: maurer_s_cleft-uniprot-causal
  name: Native maurer s cleft UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0020036
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/maurer_s_cleft.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Three unreviewed examples and two
    COVERED nodes. Native identity is distinct from source-supported trafficking/localization
    and necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-maurer_s_cleft-causal
- check_id: methane_oxidizing_organelle-uniprot-verify
  name: Native methane oxidizing organelle UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0044227
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/methane_oxidizing_organelle.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Two reviewed and one unreviewed
    examples; one COVERED pMMO node. Native pmoA1/pmoB1/pmoC1 identity is distinguished
    from exact biochemical, structural and strain evidence.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-methane_oxidizing_organelle-verify
- check_id: methane_oxidizing_organelle-uniprot-causal
  name: Native methane oxidizing organelle UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0044227
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/methane_oxidizing_organelle.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Two reviewed and one unreviewed
    examples; one COVERED pMMO node. Native pmoA1/pmoB1/pmoC1 identity is distinguished
    from exact biochemical, structural and strain evidence.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-methane_oxidizing_organelle-causal
- check_id: microneme-uniprot-verify
  name: Native microneme UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0020009
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/microneme.yaml
    --verify
  exit_code: 0
  summary: 'Read-only native command returned zero. Five example occurrences across
    four distinct accessions: two reviewed plus three unreviewed occurrences. MIC2
    occurs under both an adhesin cohort and the MIC2-M2AP complex; both typed nodes
    are COVERED. Identity does not determine lumen topology or complex function.'
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-microneme-verify
- check_id: microneme-uniprot-causal
  name: Native microneme UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0020009
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/microneme.yaml
    --causal-graphs
  exit_code: 0
  summary: 'Read-only native command returned zero. Five example occurrences across
    four distinct accessions: two reviewed plus three unreviewed occurrences. MIC2
    occurs under both an adhesin cohort and the MIC2-M2AP complex; both typed nodes
    are COVERED. Identity does not determine lumen topology or complex function.'
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-microneme-causal
- check_id: microneme_lumen-uniprot-verify
  name: Native microneme lumen UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0034494
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/microneme_lumen.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. No represented protein examples
    or typed molecular nodes; positive narrative molecular/pathway assertions and
    physical-scope exclusions are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-microneme_lumen-verify
- check_id: microneme_lumen-uniprot-causal
  name: Native microneme lumen UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0034494
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/microneme_lumen.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. No represented protein examples
    or typed molecular nodes; positive narrative molecular/pathway assertions and
    physical-scope exclusions are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-microneme_lumen-causal
- check_id: microneme_membrane-uniprot-verify
  name: Native microneme membrane UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0033163
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/microneme_membrane.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. No represented protein examples
    or typed molecular nodes; positive narrative molecular/pathway assertions and
    physical-scope exclusions are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-microneme_membrane-verify
- check_id: microneme_membrane-uniprot-causal
  name: Native microneme membrane UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0033163
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/microneme_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. No represented protein examples
    or typed molecular nodes; positive narrative molecular/pathway assertions and
    physical-scope exclusions are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-microneme_membrane-causal
- check_id: micronucleus-uniprot-verify
  name: Native micronucleus UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0031040
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/micronucleus.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. No represented protein examples
    or typed molecular nodes; positive narrative molecular/pathway assertions and
    physical-scope exclusions are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-micronucleus-verify
- check_id: micronucleus-uniprot-causal
  name: Native micronucleus UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0031040
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/micronucleus.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. No represented protein examples
    or typed molecular nodes; positive narrative molecular/pathway assertions and
    physical-scope exclusions are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-micronucleus-causal
- check_id: microsporidian_posterior_vacuole-uniprot-verify
  name: Native microsporidian posterior vacuole UniProt verify check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:microsporidian_posterior_vacuole
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/microsporidian_posterior_vacuole.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. No represented protein examples
    or typed molecular nodes; positive narrative molecular/pathway assertions and
    physical-scope exclusions are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-microsporidian_posterior_vacuole-verify
- check_id: microsporidian_posterior_vacuole-uniprot-causal
  name: Native microsporidian posterior vacuole UniProt causal check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:microsporidian_posterior_vacuole
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/microsporidian_posterior_vacuole.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. No represented protein examples
    or typed molecular nodes; positive narrative molecular/pathway assertions and
    physical-scope exclusions are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-microsporidian_posterior_vacuole-causal
- check_id: mitochondrial_crista-uniprot-verify
  name: Native mitochondrial crista UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0030061
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/mitochondrial_crista.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. No represented protein examples
    or typed molecular nodes; positive narrative molecular/pathway assertions and
    physical-scope exclusions are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-mitochondrial_crista-verify
- check_id: mitochondrial_crista-uniprot-causal
  name: Native mitochondrial crista UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0030061
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/mitochondrial_crista.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. No represented protein examples
    or typed molecular nodes; positive narrative molecular/pathway assertions and
    physical-scope exclusions are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-mitochondrial_crista-causal
- check_id: mitochondrial_crista_junction-uniprot-verify
  name: Native mitochondrial crista junction UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0044284
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/mitochondrial_crista_junction.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. No represented protein examples
    or typed molecular nodes; positive narrative molecular/pathway assertions and
    physical-scope exclusions are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-mitochondrial_crista_junction-verify
- check_id: mitochondrial_crista_junction-uniprot-causal
  name: Native mitochondrial crista junction UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0044284
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/mitochondrial_crista_junction.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. No represented protein examples
    or typed molecular nodes; positive narrative molecular/pathway assertions and
    physical-scope exclusions are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-mitochondrial_crista_junction-causal
- check_id: mitochondrial_derived_compartment-uniprot-verify
  name: Native mitochondrial derived compartment UniProt verify check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitochondrial_derived_compartment
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/mitochondrial_derived_compartment.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Three reviewed examples (TOM70/P07213,
    TOM71/P38825, DNM1/P54861); zero typed GENE_OR_PROTEIN nodes. Protein identities
    are separate from source-specific induction, deletion background, physical recruitment
    and necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-mitochondrial_derived_compartment-verify
- check_id: mitochondrial_derived_compartment-uniprot-causal
  name: Native mitochondrial derived compartment UniProt causal check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitochondrial_derived_compartment
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/mitochondrial_derived_compartment.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Three reviewed examples (TOM70/P07213,
    TOM71/P38825, DNM1/P54861); zero typed GENE_OR_PROTEIN nodes. Protein identities
    are separate from source-specific induction, deletion background, physical recruitment
    and necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-mitochondrial_derived_compartment-causal
evidence:
- evidence_id: current-record-0
  kind: record_content
  reference: data/structures/membrane_organelle/maurer_s_cleft.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T16:17:55Z'
  support: context_only
  summary: Original frozen SHA256 e8745451600446a168d2c417a41d1628fe36a02952f9d64157a9764e7ab44455;
    current SHA256 8eed10ce23b6b30eb30d69fc14e8686bc350a5906ac9b7fbe4b6601ebe3616a9.
    Changed record reassessed against current sources.
  snapshot_sha256: 8eed10ce23b6b30eb30d69fc14e8686bc350a5906ac9b7fbe4b6601ebe3616a9
- evidence_id: original-review-0
  kind: prior_review
  reference: reviews/structured/20261022T022231Z-maurer-s-cleft-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T16:17:55Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 6236c1a6388454222604a8d54bcc081a077c2cf7edd83c6ddc6f0e174687cd68
- evidence_id: current-record-1
  kind: record_content
  reference: data/structures/membrane_organelle/methane_oxidizing_organelle.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T16:17:55Z'
  support: context_only
  summary: Original frozen SHA256 467cea27775a831c959b7a2e05a1f396a9ef026e2b1c012059a59d023570da3b;
    current SHA256 8d513f399ed2555737573ae9d0c888514408062fcd5f2ec60bc19bad9e93f2c8.
    Changed record reassessed against current sources.
  snapshot_sha256: 8d513f399ed2555737573ae9d0c888514408062fcd5f2ec60bc19bad9e93f2c8
- evidence_id: original-review-1
  kind: prior_review
  reference: reviews/structured/20261022T022232Z-methane-oxidizing-organelle-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T16:17:55Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 0864d9f497ea8b445ff162b6c6bbfe2bb72aa8e7450f0d7032ca197679e9151b
- evidence_id: current-record-2
  kind: record_content
  reference: data/structures/membrane_organelle/microneme.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T16:17:55Z'
  support: context_only
  summary: Original frozen SHA256 12358b0b6b393cc14973846c2d86f59e3716f1b9d3513ff2914c3e6b28193cc9;
    current SHA256 8c260a40b26529407d136e11511c846d6554d975d54a3a45f444876aa0b51da8.
    Changed record reassessed against current sources.
  snapshot_sha256: 8c260a40b26529407d136e11511c846d6554d975d54a3a45f444876aa0b51da8
- evidence_id: original-review-2
  kind: prior_review
  reference: reviews/structured/20261022T022233Z-microneme-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T16:17:55Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: a2e2cd863d1912f27d2cec34a222e508a9d686de13d7def030eb53de90de8b88
- evidence_id: current-record-3
  kind: record_content
  reference: data/structures/membrane_organelle/microneme_lumen.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T16:17:55Z'
  support: context_only
  summary: Original frozen SHA256 c40d221eea42af12fcb06a6a5dbcc7d3592f289ad31f52a275acad4d6666af38;
    current SHA256 c40d221eea42af12fcb06a6a5dbcc7d3592f289ad31f52a275acad4d6666af38.
    Record bytes unchanged since the original review.
  snapshot_sha256: c40d221eea42af12fcb06a6a5dbcc7d3592f289ad31f52a275acad4d6666af38
- evidence_id: original-review-3
  kind: prior_review
  reference: reviews/structured/20261022T022235Z-microneme-lumen-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T16:17:55Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 7eed59c251a3aaf29f4f672df03c7354b85a3606324f2b669a21ea1b5b8353d8
- evidence_id: current-record-4
  kind: record_content
  reference: data/structures/membrane_organelle/microneme_membrane.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T16:17:55Z'
  support: context_only
  summary: Original frozen SHA256 f3c40aeb98a8d3eec6950ea6a3875db63372a5e72c66a75130e4ec821f0dc4ad;
    current SHA256 f3c40aeb98a8d3eec6950ea6a3875db63372a5e72c66a75130e4ec821f0dc4ad.
    Record bytes unchanged since the original review.
  snapshot_sha256: f3c40aeb98a8d3eec6950ea6a3875db63372a5e72c66a75130e4ec821f0dc4ad
- evidence_id: original-review-4
  kind: prior_review
  reference: reviews/structured/20261022T022236Z-microneme-membrane-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T16:17:55Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: bcacc4edb8d3ad6e959d23de9b6e4429b62b0c84053107f71bc013b288488469
- evidence_id: current-record-5
  kind: record_content
  reference: data/structures/membrane_organelle/micronucleus.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T16:17:55Z'
  support: context_only
  summary: Original frozen SHA256 fe6086eb62e1499109082d20f9a25ff776a68482d0ab89253469f6f3bfcbb8c1;
    current SHA256 fe6086eb62e1499109082d20f9a25ff776a68482d0ab89253469f6f3bfcbb8c1.
    Record bytes unchanged since the original review.
  snapshot_sha256: fe6086eb62e1499109082d20f9a25ff776a68482d0ab89253469f6f3bfcbb8c1
- evidence_id: original-review-5
  kind: prior_review
  reference: reviews/structured/20261022T022237Z-micronucleus-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T16:17:55Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: de79f648d1fa9ea63b8a29ce2725c2a3d8e6c81cc35ca3e6f0e41c2aaee0367c
- evidence_id: current-record-6
  kind: record_content
  reference: data/structures/membrane_organelle/microsporidian_posterior_vacuole.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T16:17:55Z'
  support: context_only
  summary: Original frozen SHA256 db2c2e1271b64aa7037885eeb2f1e39c6e3ee5d769b83e8374ed96d2e768f6b8;
    current SHA256 db2c2e1271b64aa7037885eeb2f1e39c6e3ee5d769b83e8374ed96d2e768f6b8.
    Record bytes unchanged since the original review.
  snapshot_sha256: db2c2e1271b64aa7037885eeb2f1e39c6e3ee5d769b83e8374ed96d2e768f6b8
- evidence_id: original-review-6
  kind: prior_review
  reference: reviews/structured/20261022T022238Z-microsporidian-posterior-vacuole-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T16:17:55Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: b3fb563d38edb33f94e0de1bdf485a430468f9c8695f82d83d04ebbdb61390e8
- evidence_id: current-record-7
  kind: record_content
  reference: data/structures/membrane_organelle/mitochondrial_crista.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T16:17:55Z'
  support: context_only
  summary: Original frozen SHA256 d7f734bbcd5e5af1c899f0c2034d2bc72656eaeb71d5861cf185613c65f4bda6;
    current SHA256 d7f734bbcd5e5af1c899f0c2034d2bc72656eaeb71d5861cf185613c65f4bda6.
    Record bytes unchanged since the original review.
  snapshot_sha256: d7f734bbcd5e5af1c899f0c2034d2bc72656eaeb71d5861cf185613c65f4bda6
- evidence_id: original-review-7
  kind: prior_review
  reference: reviews/structured/20261022T022238Z-mitochondrial-crista-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T16:17:55Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 8e7fcd2bf0433a33698142957cc06549648ff14c8fe8bfe047dd7cc22530f5ee
- evidence_id: current-record-8
  kind: record_content
  reference: data/structures/membrane_organelle/mitochondrial_crista_junction.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T16:17:55Z'
  support: context_only
  summary: Original frozen SHA256 fccd57bdf4448897c74fae433fbec5a596152571a8ad7e21034643d8d4379653;
    current SHA256 b994a1d51d584f4614c50fb97db455db7a6cf72b2f886da419fcbf3b77ba3adb.
    Changed record reassessed against current sources.
  snapshot_sha256: b994a1d51d584f4614c50fb97db455db7a6cf72b2f886da419fcbf3b77ba3adb
- evidence_id: original-review-8
  kind: prior_review
  reference: reviews/structured/20261022T022239Z-mitochondrial-crista-junction-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T16:17:55Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 61c6e878b42552da90908c4096400f6a3dd72adecbbdcc5dbd89e76134725a1c
- evidence_id: current-record-9
  kind: record_content
  reference: data/structures/membrane_organelle/mitochondrial_derived_compartment.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T16:17:55Z'
  support: context_only
  summary: Original frozen SHA256 c7a83f3db0bb05a7016b5c3991e79bd21c9a6ec4f723335fc3a1d14864d1c5c8;
    current SHA256 c7a83f3db0bb05a7016b5c3991e79bd21c9a6ec4f723335fc3a1d14864d1c5c8.
    Record bytes unchanged since the original review.
  snapshot_sha256: c7a83f3db0bb05a7016b5c3991e79bd21c9a6ec4f723335fc3a1d14864d1c5c8
- evidence_id: original-review-9
  kind: prior_review
  reference: reviews/structured/20261022T022241Z-mitochondrial-derived-compartment-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T16:17:55Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 2d4970f0670d8b53508e37cfd606b0f5089087230f7ead44afbfd546f819488e
- evidence_id: septin-review-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Whole-record assertions, structured sources and severity rubric
  summary: Positive molecular/pathway assertions require a real applicability assessment;
    absence of expression claims alone is not an exemption. Keep source scope, uncertainty
    and original finding identity; record curation is separate.
  accessed_at: '2026-11-03T16:16:15.443886Z'
  support: supports
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: septin-curation-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Structural components, molecular grounding and family-or-class guidance
  summary: Whole assembled membranes are structures; a LIPID component denotes molecular
    material and cannot use a complete membrane identity as exact chemical grounding.
    Taxon-agnostic protein families OR classes are permitted. An optional example
    inventory is not automatically required for every generic class.
  accessed_at: '2026-11-03T16:16:15.443886Z'
  support: supports
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
- evidence_id: septin-schema-policy
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, ComponentTypeEnum and grounding contract
  summary: Molecular components and whole structures have different identities. Label-only
    supported lipid material is possible without inventing exact chemical composition.
    PROTEIN enum prose is interpreted with explicit CURATION generic-class permission;
    no automatic complex assertion follows from a heterogeneous class.
  accessed_at: '2026-11-03T16:16:15.443886Z'
  support: supports
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: septin-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Graph nodes, component correspondence, source scope and necessity
  summary: Descriptive boundary graphs can remain NONMECHANISTIC; source-specific
    localization, molecular identity and organelle-formation necessity must not be
    conflated.
  accessed_at: '2026-11-03T16:16:15.443886Z'
  support: supports
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: septin-protein-policy
  kind: authority
  reference: .claude/skills/uniprot-protein-examples/SKILL.md
  locator: Step2 generic classes and native coverage report
  summary: Generic class components are explicitly recognized. A zero-example inventory
    or NO_GENE_SYMBOLS node is a stated coverage limit, not proof that the protein
    class does not exist or that its members form one stable complex.
  accessed_at: '2026-11-03T16:16:15.443886Z'
  support: supports
  snapshot_sha256: 6462894c8257823bae2b175c34693cd42f11ff9269a3829c15b9286ba6d7c876
- evidence_id: septin-record-maurer_s_cleft
  kind: record_content
  reference: data/structures/membrane_organelle/maurer_s_cleft.yaml
  locator: Complete current record at 61d3617ae8700b99198e2aaf01f3b2437933de6c
  summary: Read all identity/boundaries, components/examples, taxa/canonical scopes,
    functions, bibliography, all graph nodes/edges, discussions and history. No maintained
    image, numeric physical-property, associated-trait or verbatim-snippet fields.
  accessed_at: '2026-11-03T16:16:15.443886Z'
  support: supports
  snapshot_sha256: 8eed10ce23b6b30eb30d69fc14e8686bc350a5906ac9b7fbe4b6601ebe3616a9
- evidence_id: septin-original-maurer_s_cleft
  kind: prior_review
  reference: reviews/structured/20261022T022231Z-maurer-s-cleft-audit/review.yaml
  locator: Complete original YAML and Markdown, frozen inputs/checks/assessments/findings/actions
    and access limits
  summary: Historical observations remain historical; original artifacts are unchanged.
    Current target is stale and substantively reassessed. Exact inherited findings
    are retained where present; no other-target/category issue disposition follows.
  accessed_at: '2026-11-03T16:16:15.443886Z'
  support: supports
  snapshot_sha256: 6236c1a6388454222604a8d54bcc081a077c2cf7edd83c6ddc6f0e174687cd68
- evidence_id: septin-original-validation-maurer_s_cleft
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/adversary-septin/original-checks.json
  locator: Actual original native validate/render and historical target-hash verification
  summary: Both native commands exit0; original Markdown matches deterministic render
    and historical target hash equals frozen input.
  accessed_at: '2026-11-03T16:08:20.641607Z'
  support: supports
  snapshot_sha256: 7a92d12671053fdce21ca159bbd5944664efb76e9438bf5793341b7bae315d25
- evidence_id: septin-native-maurer_s_cleft-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/maurer_s_cleft-uniprot-verify-receipt.json
  locator: Actual receipt; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/maurer_s_cleft-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: Exit0. Three UNREVIEWED example occurrences and three distinct accessions
    Q6V0W9,Q8I2G1,Q9NFF5; two COVERED GENE_OR_PROTEIN nodes. Q6V0W9 is a fragment.
    Native identity/coverage does not demonstrate accession-specific membership, complete
    composition, causality or formation necessity.
  accessed_at: '2026-11-03T16:07:53.747690Z'
  support: supports
  snapshot_sha256: 544b69062dd5016eeeeeab92df5cbf8572db751b4aaac9c67251040e7234f077
- evidence_id: septin-native-maurer_s_cleft-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/maurer_s_cleft-uniprot-causal-receipt.json
  locator: Actual receipt; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/maurer_s_cleft-uniprot-causal.log
    SHA256 0ccd24fe81e43c2fc407db2d76bb5aa040c8ac2f3ddd67c4c60ff1b16ea135d3
  summary: Exit0. Three UNREVIEWED example occurrences and three distinct accessions
    Q6V0W9,Q8I2G1,Q9NFF5; two COVERED GENE_OR_PROTEIN nodes. Q6V0W9 is a fragment.
    Native identity/coverage does not demonstrate accession-specific membership, complete
    composition, causality or formation necessity.
  accessed_at: '2026-11-03T16:07:54.196318Z'
  support: supports
  snapshot_sha256: d5b8b3228c1d0e1a4d6dd93f51ed265dc3f4bc7f4c53f752aad30cf6e3fb3f04
- evidence_id: septin-record-microneme
  kind: record_content
  reference: data/structures/membrane_organelle/microneme.yaml
  locator: Complete current record at 61d3617ae8700b99198e2aaf01f3b2437933de6c
  summary: Read all identity/boundaries, components/examples, taxa/canonical scopes,
    functions, bibliography, all graph nodes/edges, discussions and history. No maintained
    image, numeric physical-property, associated-trait or verbatim-snippet fields.
  accessed_at: '2026-11-03T16:16:15.443886Z'
  support: supports
  snapshot_sha256: 8c260a40b26529407d136e11511c846d6554d975d54a3a45f444876aa0b51da8
- evidence_id: septin-original-microneme
  kind: prior_review
  reference: reviews/structured/20261022T022233Z-microneme-audit/review.yaml
  locator: Complete original YAML and Markdown, frozen inputs/checks/assessments/findings/actions
    and access limits
  summary: Historical observations remain historical; original artifacts are unchanged.
    Current target is stale and substantively reassessed. Exact inherited findings
    are retained where present; no other-target/category issue disposition follows.
  accessed_at: '2026-11-03T16:16:15.443886Z'
  support: supports
  snapshot_sha256: a2e2cd863d1912f27d2cec34a222e508a9d686de13d7def030eb53de90de8b88
- evidence_id: septin-original-validation-microneme
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/adversary-septin/original-checks.json
  locator: Actual original native validate/render and historical target-hash verification
  summary: Both native commands exit0; original Markdown matches deterministic render
    and historical target hash equals frozen input.
  accessed_at: '2026-11-03T16:08:21.812652Z'
  support: supports
  snapshot_sha256: 7a92d12671053fdce21ca159bbd5944664efb76e9438bf5793341b7bae315d25
- evidence_id: septin-native-microneme-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/microneme-uniprot-verify-receipt.json
  locator: Actual receipt; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/microneme-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 'Exit0. Five protein-example occurrences but four distinct accessions:
    MIC2/S8F9G8 occurs under both adhesin cohort and MIC2-M2AP complex. Two REVIEWED
    occurrences O00834/B6KAM0 and three UNREVIEWED occurrences S8F9G8 twice/S8GDJ1
    once; two COVERED GENE_OR_PROTEIN nodes. Correct identity and symbol coverage
    do not prove complete complex stoichiometry, localization topology or causal necessity.'
  accessed_at: '2026-11-03T16:07:57.924056Z'
  support: supports
  snapshot_sha256: 635735778a2ba1272ec9cba3a617d2e0e61e0ba0abd81cece571a0cb2c1b7323
- evidence_id: septin-native-microneme-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/microneme-uniprot-causal-receipt.json
  locator: Actual receipt; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/microneme-uniprot-causal.log
    SHA256 eb7a8d48aaebc612f3134392b96306cfc1973f5dedd06a3cfc8937855fdeb6b0
  summary: 'Exit0. Five protein-example occurrences but four distinct accessions:
    MIC2/S8F9G8 occurs under both adhesin cohort and MIC2-M2AP complex. Two REVIEWED
    occurrences O00834/B6KAM0 and three UNREVIEWED occurrences S8F9G8 twice/S8GDJ1
    once; two COVERED GENE_OR_PROTEIN nodes. Correct identity and symbol coverage
    do not prove complete complex stoichiometry, localization topology or causal necessity.'
  accessed_at: '2026-11-03T16:07:58.344217Z'
  support: supports
  snapshot_sha256: 7399e3f17714a17c044fe14e47905eef8f94684a0bc69086268a306b0434f2dc
- evidence_id: septin-record-microneme_lumen
  kind: record_content
  reference: data/structures/membrane_organelle/microneme_lumen.yaml
  locator: Complete current record at 61d3617ae8700b99198e2aaf01f3b2437933de6c
  summary: Read all identity/boundaries, components/examples, taxa/canonical scopes,
    functions, bibliography, all graph nodes/edges, discussions and history. No maintained
    image, numeric physical-property, associated-trait or verbatim-snippet fields.
  accessed_at: '2026-11-03T16:16:15.443886Z'
  support: supports
  snapshot_sha256: c40d221eea42af12fcb06a6a5dbcc7d3592f289ad31f52a275acad4d6666af38
- evidence_id: septin-original-microneme_lumen
  kind: prior_review
  reference: reviews/structured/20261022T022235Z-microneme-lumen-audit/review.yaml
  locator: Complete original YAML and Markdown, frozen inputs/checks/assessments/findings/actions
    and access limits
  summary: Historical observations remain historical; original artifacts are unchanged.
    Current target is byte-unchanged. Exact inherited findings are retained where
    present; no other-target/category issue disposition follows.
  accessed_at: '2026-11-03T16:16:15.443886Z'
  support: supports
  snapshot_sha256: 7eed59c251a3aaf29f4f672df03c7354b85a3606324f2b669a21ea1b5b8353d8
- evidence_id: septin-original-validation-microneme_lumen
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/adversary-septin/original-checks.json
  locator: Actual original native validate/render and historical target-hash verification
  summary: Both native commands exit0; original Markdown matches deterministic render
    and historical target hash equals frozen input.
  accessed_at: '2026-11-03T16:08:22.954191Z'
  support: supports
  snapshot_sha256: 7a92d12671053fdce21ca159bbd5944664efb76e9438bf5793341b7bae315d25
- evidence_id: septin-native-microneme_lumen-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/microneme_lumen-uniprot-verify-receipt.json
  locator: Actual receipt; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/microneme_lumen-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: Exit0. Zero protein examples and zero typed GENE_OR_PROTEIN nodes; no represented
    UniProtKB graph xrefs. Exit0 validates an empty identifier inventory, not the
    complete secretion/pathway narrative.
  accessed_at: '2026-11-03T16:07:58.759401Z'
  support: supports
  snapshot_sha256: 0823b00b71417065dbb42da1376dd65a9500794fff5c7a99d30f4f7cda39748c
- evidence_id: septin-native-microneme_lumen-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/microneme_lumen-uniprot-causal-receipt.json
  locator: Actual receipt; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/microneme_lumen-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: Exit0. Zero protein examples and zero typed GENE_OR_PROTEIN nodes; no represented
    UniProtKB graph xrefs. Exit0 validates an empty identifier inventory, not the
    complete secretion/pathway narrative.
  accessed_at: '2026-11-03T16:07:59.172936Z'
  support: supports
  snapshot_sha256: a3eb9e04182dacc3f058521b1af854a09408ae39548c094027e8dfa35a7bfffa
- evidence_id: septin-record-microneme_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/microneme_membrane.yaml
  locator: Complete current record at 61d3617ae8700b99198e2aaf01f3b2437933de6c
  summary: Read all identity/boundaries, components/examples, taxa/canonical scopes,
    functions, bibliography, all graph nodes/edges, discussions and history. No maintained
    image, numeric physical-property, associated-trait or verbatim-snippet fields.
  accessed_at: '2026-11-03T16:16:15.443886Z'
  support: supports
  snapshot_sha256: f3c40aeb98a8d3eec6950ea6a3875db63372a5e72c66a75130e4ec821f0dc4ad
- evidence_id: septin-original-microneme_membrane
  kind: prior_review
  reference: reviews/structured/20261022T022236Z-microneme-membrane-audit/review.yaml
  locator: Complete original YAML and Markdown, frozen inputs/checks/assessments/findings/actions
    and access limits
  summary: Historical observations remain historical; original artifacts are unchanged.
    Current target is byte-unchanged. Exact inherited findings are retained where
    present; no other-target/category issue disposition follows.
  accessed_at: '2026-11-03T16:16:15.443886Z'
  support: supports
  snapshot_sha256: bcacc4edb8d3ad6e959d23de9b6e4429b62b0c84053107f71bc013b288488469
- evidence_id: septin-original-validation-microneme_membrane
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/adversary-septin/original-checks.json
  locator: Actual original native validate/render and historical target-hash verification
  summary: Both native commands exit0; original Markdown matches deterministic render
    and historical target hash equals frozen input.
  accessed_at: '2026-11-03T16:08:24.090269Z'
  support: supports
  snapshot_sha256: 7a92d12671053fdce21ca159bbd5944664efb76e9438bf5793341b7bae315d25
- evidence_id: septin-native-microneme_membrane-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/microneme_membrane-uniprot-verify-receipt.json
  locator: Actual receipt; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/microneme_membrane-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: Exit0. Zero protein examples and zero typed GENE_OR_PROTEIN nodes; no represented
    UniProtKB graph xrefs. Exit0 validates an empty identifier inventory, not the
    complete exocytosis/pathway narrative.
  accessed_at: '2026-11-03T16:07:59.592330Z'
  support: supports
  snapshot_sha256: ef256510d2c1a587fc8864fbc2738d41e9b91e81aa5806c5a5df06ddd8339492
- evidence_id: septin-native-microneme_membrane-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/microneme_membrane-uniprot-causal-receipt.json
  locator: Actual receipt; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/microneme_membrane-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: Exit0. Zero protein examples and zero typed GENE_OR_PROTEIN nodes; no represented
    UniProtKB graph xrefs. Exit0 validates an empty identifier inventory, not the
    complete exocytosis/pathway narrative.
  accessed_at: '2026-11-03T16:08:00.009781Z'
  support: supports
  snapshot_sha256: 4184701432b736f4e7cf1303503b26e6f55d53dc8728593bd4684a34ceaa1aa7
- evidence_id: septin-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0020036,GO%3A0043231,GO%3A0020009,GO%3A0020007,GO%3A0033163,GO%3A0034494,GO%3A0031090,GO%3A0043233
  locator: Eight exact active GO definitions, synonyms and relation-bearing children
  summary: GO0020036 is Maurer cleft; GO0020009 whole microneme, GO0034494 lumen and
    GO0033163 membrane remain distinct. Lumen is volume enclosed by the membrane;
    whole membrane is a cellular structure rather than a molecular lipid. GO0020007
    apical complex and the declared broader organelle/lumen/membrane identities are
    separately verified.
  accessed_at: '2026-11-03T16:08:18.366082Z'
  support: supports
  snapshot_sha256: dc7e43ede424b37265590e61fd27ff04a6e8a85acdf7c78cac0dcdd0976e364c
- evidence_id: septin-ancestors-0020036
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0020036/ancestors?relations=is_a
  locator: Complete exact GO ancestors response restricted to relations=is_a
  summary: GO0043231 is not in this is_a-only response; the broader membrane-bounded-organelle
    parent is definition/biology-compatible, not claimed as a native GO ancestry edge.
  accessed_at: '2026-11-03T16:08:18.366356Z'
  support: supports
  snapshot_sha256: 63658dde37d546ce418ec334558fbd539a13b444aca80c5465233aff687700c4
- evidence_id: septin-ancestors-0020009
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0020009/ancestors?relations=is_a
  locator: Complete exact GO ancestors response restricted to relations=is_a
  summary: GO0043231 is a native is_a ancestor; apical-complex parthood is a separate
    relation, not is_a.
  accessed_at: '2026-11-03T16:08:18.366449Z'
  support: supports
  snapshot_sha256: 92bbd39302dc985a204aa0c2e016f44875cbb4c5844dbce53352270a14cd18c5
- evidence_id: septin-ancestors-0034494
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0034494/ancestors?relations=is_a
  locator: Complete exact GO ancestors response restricted to relations=is_a
  summary: GO0043233 organelle lumen is a native is_a ancestor; whole-organelle parthood
    is separately represented.
  accessed_at: '2026-11-03T16:08:18.366569Z'
  support: supports
  snapshot_sha256: d14c82859cda42fcf5e8c193ec6b9b0c3c1441db96b65cba6690b4ba52f580d4
- evidence_id: septin-ancestors-0033163
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0033163/ancestors?relations=is_a
  locator: Complete exact GO ancestors response restricted to relations=is_a
  summary: GO0031090 organelle membrane is a native is_a ancestor; whole-organelle
    parthood is separate.
  accessed_at: '2026-11-03T16:08:18.366515Z'
  support: supports
  snapshot_sha256: 71a24790bb029cd34196bb88261f5b5a9904637c0c9b3acbecead39ad3bb6a4a
- evidence_id: septin-tax5833
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/5833.json
  locator: Exact UniProt taxonomy taxonId/scientific name/rank/lineage
  summary: Plasmodium falciparum species. Taxonomic identity does not prove experimental
    strain or organelle membership.
  accessed_at: '2026-11-03T16:08:19.118984Z'
  support: supports
  snapshot_sha256: d7d03d6d835c759fc948d3261e551119cf1b928883a2e5b711e9f8b08b5690bd
- evidence_id: septin-tax36329
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/36329.json
  locator: Exact UniProt taxonomy taxonId/scientific name/rank/lineage
  summary: Plasmodium falciparum3D7 isolate. Taxonomic identity does not prove experimental
    strain or organelle membership.
  accessed_at: '2026-11-03T16:08:19.120062Z'
  support: supports
  snapshot_sha256: 5bbd74668f30ca223a1bda0ac54cc00a68e98f1209ec190d531100a850ea6170
- evidence_id: septin-tax2759
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/2759.json
  locator: Exact UniProt taxonomy taxonId/scientific name/rank/lineage
  summary: Eukaryota domain; broad RARE occurrence is qualitative, not a numeric prevalence
    estimate. Taxonomic identity does not prove experimental strain or organelle membership.
  accessed_at: '2026-11-03T16:08:19.122269Z'
  support: supports
  snapshot_sha256: af5ba762219fdecb11d214126bb8184c0eb28fc6474d14777c4aaa7f7dd89369
- evidence_id: septin-tax5794
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/5794.json
  locator: Exact UniProt taxonomy taxonId/scientific name/rank/lineage
  summary: Apicomplexa phylum; stage/lineage restrictions remain. Taxonomic identity
    does not prove experimental strain or organelle membership.
  accessed_at: '2026-11-03T16:08:19.124580Z'
  support: supports
  snapshot_sha256: 74c77af3be4cd05287834d94df5d50d8d4a888cd1674592bea89ff4d71c582fb
- evidence_id: septin-tax5811
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/5811.json
  locator: Exact UniProt taxonomy taxonId/scientific name/rank/lineage
  summary: Toxoplasma gondii species. Taxonomic identity does not prove experimental
    strain or organelle membership.
  accessed_at: '2026-11-03T16:08:19.131429Z'
  support: supports
  snapshot_sha256: 7cf9cbbe5a0e057701afe52d9e189c47df0ef51d9a5b7edbbe7a21d199ad246a
- evidence_id: septin-tax432359
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/432359.json
  locator: Exact UniProt taxonomy taxonId/scientific name/rank/lineage
  summary: Toxoplasma gondii VEG strain, under typeIII lineage; not the RH experimental
    strain. Taxonomic identity does not prove experimental strain or organelle membership.
  accessed_at: '2026-11-03T16:08:19.700983Z'
  support: supports
  snapshot_sha256: 446700298ec920dda857b3cb29eaf5c459cbcc9e923db7ab63a7c6fdd9193cc8
- evidence_id: septin-tax508771
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/508771.json
  locator: Exact UniProt taxonomy taxonId/scientific name/rank/lineage
  summary: Toxoplasma gondii ME49 strain; not the RH experimental strain. Taxonomic
    identity does not prove experimental strain or organelle membership.
  accessed_at: '2026-11-03T16:08:19.708073Z'
  support: supports
  snapshot_sha256: 555d95d2e7f62312cd3eed13be08d4d102b0156ae8a6bf21a9732db2d52e9a98
- evidence_id: septin-protein-Q6V0W9
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q6V0W9.json
  locator: Exact current accession/status/name/gene fields/taxon/comments/features/cross-references
  summary: UNREVIEWED P.falciparum5833 MAHRP1 fragment with geneName mahrp1; no native
    functional/localization comments or InterPro xrefs. Fragment identity is not exact
    identity of a full experimental construct.
  accessed_at: '2026-11-03T16:08:20.636985Z'
  support: supports
  snapshot_sha256: 09072d663ec1d345fac57842b18f828aca1785367468892b3b8a58b554dd7df5
- evidence_id: septin-protein-Q8I2G1
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q8I2G1.json
  locator: Exact current accession/status/name/gene fields/taxon/comments/features/cross-references
  summary: New REX1 example is UNREVIEWED P.falciparum3D7 taxon36329 with ORF-name
    PF3D7_0935900 and matching REX1 protein name. It has no formal primary geneName
    field; automatic transmembrane feature and entry identity do not establish causal
    necessity. Cooke primary body independently supplies Rex cleft-marker context.
  accessed_at: '2026-11-03T16:08:20.669562Z'
  support: supports
  snapshot_sha256: a3bd8e77934085690b4d2c108d5bc2927db5961f091747a48265b70874b7b50e
- evidence_id: septin-protein-Q9NFF5
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q9NFF5.json
  locator: Exact current accession/status/name/gene fields/taxon/comments/features/cross-references
  summary: UNREVIEWED P.falciparum5833 skeleton-binding protein1 with geneName sbp1;
    automatic transmembrane feature, no native functional comments. Experimental membership
    and trafficking follow Blisnick/Cooke, not TrEMBL identity alone.
  accessed_at: '2026-11-03T16:08:21.687324Z'
  support: supports
  snapshot_sha256: 59a86d923f7785e2771d46622599d0521312197891f59801c67aa72557a16242
- evidence_id: septin-protein-O00834
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/O00834.json
  locator: Exact current accession/status/name/gene fields/taxon/comments/features/cross-references
  summary: REVIEWED T.gondii5811 MIC1; soluble adhesin in MIC6/MIC1/MIC4 context.
    Cell-location evidence cites PMID11157983,15684324,18818666, which are separately
    checked at complete primary-abstract scope. IPR008117 is a MIC1-family candidate,
    not identity of the entire heterogeneous adhesin cohort.
  accessed_at: '2026-11-03T16:08:21.837674Z'
  support: supports
  snapshot_sha256: 91ae758e987cebd33da8283f87593cdc075411958721e4ad11ea3ccd42facd5f
- evidence_id: septin-protein-B6KAM0
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/B6KAM0.json
  locator: Exact current accession/status/name/gene fields/taxon/comments/features/cross-references
  summary: REVIEWED T.gondiiVEG432359 AMA1 with geneName AMA1 and ORF TGVEG_255260.
    Single-pass typeI topology and predicted cytoplasmic-domain annotation are distinguished
    from primary-abstract evidence for microneme localization/shedding. Exact cited
    PMIDs11083833,11087913,16102004 are checked. VEG entry identity is not an RH-specific
    experiment.
  accessed_at: '2026-11-03T16:08:22.655307Z'
  support: supports
  snapshot_sha256: 4d2e1f02042185bd0e48ba219785074ea81b40138c898375d94186ed8a09b901
- evidence_id: septin-protein-S8F9G8
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/S8F9G8.json
  locator: Exact current accession/status/name/gene fields/taxon/comments/features/cross-references
  summary: UNREVIEWED T.gondiiME49508771 MIC2, geneName MIC2 and ORF TGME49_201780.
    Automatic secretion annotation and domain xrefs do not replace primary transmembrane/topology
    experiments. This same accession appears in two component inventories; no fifth
    distinct accession is inferred.
  accessed_at: '2026-11-03T16:08:22.737158Z'
  support: supports
  snapshot_sha256: a47669f628985ff8181df86bdd27deff69317dc93082a48dd78b9e82827394f1
- evidence_id: septin-protein-S8GDJ1
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/S8GDJ1.json
  locator: Exact current accession/status/name/gene fields/taxon/comments/features/cross-references
  summary: New UNREVIEWED T.gondiiME49508771 MIC2-associated proteinM2AP, ORF-name
    TGME49_214940 and matching protein name; no formal primary geneName field. Automatic
    signal peptide and IPR054124 beta-domain link do not establish whole-complex identity
    or the exact RH experimental construct. Primary studies independently support
    soluble M2AP/MIC2 complex membership.
  accessed_at: '2026-11-03T16:08:23.637717Z'
  support: supports
  snapshot_sha256: f04614b34f8612d417d054004b8b00d28d44b03ccf59fd98ebbd4457f29a7985
- evidence_id: septin-lanzer2006-meta
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1016%2Fj.ijpara.2005.10.001%22&pageSize=25
  locator: 'Exact MED metadata: title/ordered authors/date/complete abstractText'
  summary: Complete secondary abstract and bibliography support Maurer trafficking/background;
    speculative multiple roles are not treated as new demonstrated mechanisms.
  accessed_at: '2026-11-03T16:08:23.932628Z'
  support: supports
  snapshot_sha256: fbcb55adcc1174a2930d4c8fd01704cbb12f46ae30f2c4736618bdea88539f36
  search_scope: Europe PMC exact quoted DOI:10.1016/j.ijpara.2005.10.001; resultType=core,pageSize25,no
    date filter; actual fetch 2026-11-03T16:08:23.932628Z. Identifier lookup, not
    exhaustive literature search.
- evidence_id: septin-blisnick2000-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1016%2FS0166-6851%2800%2900301-7%22&pageSize=25
  locator: 'Exact MED metadata: title/ordered authors/date/complete abstractText'
  summary: 'Complete primary abstract: SBP1 integral cleft membrane, host-cytoplasmic
    C-terminal interaction context and proposed anchoring; no current full-body/pixel
    claim. Rodent antibody observations are not imported as exact P.falciparum genetic
    evidence.'
  accessed_at: '2026-11-03T16:08:24.547999Z'
  support: supports
  snapshot_sha256: d06f0c5ef96cc530cdfa49a33c042f41d4250d90496949542df94b279d00be82
  search_scope: Europe PMC exact quoted DOI:10.1016/S0166-6851(00)00301-7; resultType=core,pageSize25,no
    date filter; actual fetch 2026-11-03T16:08:24.547999Z. Identifier lookup, not
    exhaustive literature search.
- evidence_id: septin-cooke2006-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1083%2Fjcb.200509122%22&pageSize=25
  locator: 'Exact MED metadata: title/ordered authors/date/complete abstractText'
  summary: Exact bibliography and complete primary abstract for SBP1 disruption/complementation
    and PfEMP1 display; actual primary body scope is recorded separately.
  accessed_at: '2026-11-03T16:08:24.725139Z'
  support: supports
  snapshot_sha256: f2103c7d6c90b043a1ed970229bec49322741255bb55c4ba2c62ee786ba1b510
  search_scope: Europe PMC exact quoted DOI:10.1083/jcb.200509122; resultType=core,pageSize25,no
    date filter; actual fetch 2026-11-03T16:08:24.725139Z. Identifier lookup, not
    exhaustive literature search.
- evidence_id: septin-spycher2008-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1111%2Fj.1365-2958.2008.06235.x%22&pageSize=25
  locator: 'Exact MED metadata: title/ordered authors/date/complete abstractText'
  summary: Complete primary abstract and exact bibliography distinguish MAHRP1 disruption/complementation
    from the Cooke SBP1 study. This saved evidence does not certify a complete fresh
    publisher body.
  accessed_at: '2026-11-03T16:08:24.926375Z'
  support: supports
  snapshot_sha256: 5f366d6fc6b04f9222111c0ed6419a6b0aa751f35cfae75aad3242adf123f726
  search_scope: Europe PMC exact quoted DOI:10.1111/j.1365-2958.2008.06235.x; resultType=core,pageSize25,no
    date filter; actual fetch 2026-11-03T16:08:24.926375Z. Identifier lookup, not
    exhaustive literature search.
- evidence_id: septin-carruthers2008-meta
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1007%2F978-0-387-78267-6_2%22&pageSize=25
  locator: 'Exact MED metadata: title/ordered authors/date/complete abstractText'
  summary: Exact chapter/review bibliography and complete secondary abstract only.
    No current full-body verification is claimed from failed body endpoints or inherited
    review-body claims.
  accessed_at: '2026-11-03T16:08:25.416586Z'
  support: supports
  snapshot_sha256: fdb7173cc8fbb0f89d6fb6e0f6a6290240cb725bfc8e7e0b43d4312085b2e538
  search_scope: Europe PMC exact quoted DOI:10.1007/978-0-387-78267-6_2; resultType=core,pageSize25,no
    date filter; actual fetch 2026-11-03T16:08:25.416586Z. Identifier lookup, not
    exhaustive literature search.
- evidence_id: septin-dubois2019-meta
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1111%2Fcmi.13018%22&pageSize=25
  locator: 'Exact MED metadata: title/ordered authors/date/complete abstractText'
  summary: Exact review bibliography and complete abstract; accepted manuscript sections
    read are separately bounded.
  accessed_at: '2026-11-03T16:08:25.553117Z'
  support: supports
  snapshot_sha256: 296933a488842ec93f4f6e5ad08422c1f6069ab009116b7ed07f2be6bf61a7f9
  search_scope: Europe PMC exact quoted DOI:10.1111/cmi.13018; resultType=core,pageSize25,no
    date filter; actual fetch 2026-11-03T16:08:25.553117Z. Identifier lookup, not
    exhaustive literature search.
- evidence_id: septin-huynh2003-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1093%2Femboj%2Fcdg217%22&pageSize=25
  locator: 'Exact MED metadata: title/ordered authors/date/complete abstractText'
  summary: 'Complete primary abstract: M2AP disruption causes MIC2 misrouting, impaired
    rapid secretion and strongly reduced invasion, not absolute loss or proven microneme-formation
    necessity. Fresh full body was not retrieved.'
  accessed_at: '2026-11-03T16:08:25.747183Z'
  support: supports
  snapshot_sha256: 3ca2afc6a5f52374565268401b68ddf71a2b7a6cb9f9c448986e05e33bfda419
  search_scope: Europe PMC exact quoted DOI:10.1093/emboj/cdg217; resultType=core,pageSize25,no
    date filter; actual fetch 2026-11-03T16:08:25.747183Z. Identifier lookup, not
    exhaustive literature search.
- evidence_id: septin-huynh2006-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1371%2Fjournal.ppat.0020084%22&pageSize=25
  locator: 'Exact MED metadata: title/ordered authors/date/complete abstractText'
  summary: Exact primary bibliography and complete abstract; actual current body supports
    MIC2 topology and RH-derived conditional-depletion interpretation.
  accessed_at: '2026-11-03T16:08:25.785589Z'
  support: supports
  snapshot_sha256: aa3f3ba77500cbedc3ef7d1d0d049f2aa90b0c52f84e13ebc5405e727a56dd4c
  search_scope: Europe PMC exact quoted DOI:10.1371/journal.ppat.0020084; resultType=core,pageSize25,no
    date filter; actual fetch 2026-11-03T16:08:25.785589Z. Identifier lookup, not
    exhaustive literature search.
- evidence_id: septin-brown2016-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1074%2Fjbc.m115.700518%22&pageSize=25
  locator: 'Exact MED metadata: title/ordered authors/date/complete abstractText'
  summary: 'Complete primary abstract: in vitro serum albumin/PKG-cGMP pathway, ethanol/calcium
    and zaprinast contexts are distinct. No current full Methods/body or universal
    secretion mechanism is certified.'
  accessed_at: '2026-11-03T16:08:25.830183Z'
  support: supports
  snapshot_sha256: 5e021422449a431b5628b59d89332f9c226079c8b730e79586424c7dc398aa50
  search_scope: Europe PMC exact quoted DOI:10.1074/jbc.m115.700518; resultType=core,pageSize25,no
    date filter; actual fetch 2026-11-03T16:08:25.830183Z. Identifier lookup, not
    exhaustive literature search.
- evidence_id: septin-pmid-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A%289208224%20OR%2011157983%20OR%2015684324%20OR%2018818666%20OR%2011083833%20OR%2011087913%20OR%2016102004%29%20AND%20SRC%3AMED&pageSize=25
  locator: 'Seven exact MED records: complete bibliography and abstractText for9208224,11157983,15684324,18818666,11083833,11087913,16102004'
  summary: Carruthers/Sibley1997 supports sequential MIC2 then Rop1 then dense-granule
    secretion. Reiss2001 supports MIC6 escort and soluble MIC1/MIC4 versus transmembrane
    escort topology. Cerede2005 and Sawmynaden2008 concern soluble adhesins/function/domain
    interactions. Hehl2000 and Donahue2000 support AMA1 microneme localization/typeI
    topology; Howell2005 distinguishes shedding routes. These are complete primary
    abstracts, not current whole-body, figure or raw-data inspections.
  accessed_at: '2026-11-03T16:08:26.049589Z'
  support: supports
  snapshot_sha256: 15db8206f3bce5912e56add3e2565c3ea0e3ca832d1636cd32c260fb23a04ab4
  search_scope: Europe PMC EXT_ID:(9208224 OR11157983 OR15684324 OR18818666 OR11083833
    OR11087913 OR16102004) AND SRC:MED; resultType=core,pageSize25,no date filter;
    seven exact returned records inspected at 2026-11-03T16:08:26.049589Z.
- evidence_id: septin-cooke2006-bioc
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_json/PMC2063733/unicode
  locator: 'Genuine BioC: complete Abstract/Introduction/Results/Discussion; main
    Methods through adhesion assays; Figure1–7 captions and supplementary-material
    description. Supplementary data, image pixels and raw measurements not inspected'
  summary: P.falciparum3D7 infected human erythrocytes, SBP1 knockouts1G8/2D8/1G5
    and EYFP complementation. Clefts/knobs persist; PfEMP1 remains in clefts rather
    than reaching host surface; complementation restores display/adhesion. Rex and
    MAHRP cleft-marker context supports resident membership. This is an SBP1 experiment,
    not MAHRP1 genetic disruption. Proposed anchoring/direct-binding interpretations
    are not promoted to demonstrated molecular mechanisms.
  accessed_at: '2026-11-03T16:08:26.199825Z'
  support: supports
  snapshot_sha256: 0ac55d9ec24f55fb366b1cf56e136f67dba25a864fb1ce12557cd3d723a9ad35
- evidence_id: septin-huynh2006-bioc
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_json/PMC1550269/unicode
  locator: 'Genuine BioC: complete Introduction/Results/Discussion, Figure1–7 captions;
    selected Methods plasmids, parasites/transfection/selection, primers, quantitative
    Western, secretion and invasion/attachment. Table1 heading only; no table numerical
    reanalysis, pixels, videos or supplements'
  summary: RH-derived tTA-dhfr versus conditional MIC2 depletion in HFF context supports
    membrane-spanning MIC2 with extracellular adhesive domains and short cytoplasmic
    tail, soluble M2AP partnership, and M2AP misrouting upon MIC2 depletion. Other
    MIC5/AMA1 localization persists; residual invasion and distinct gliding modes
    preclude absolute organelle-formation/whole-class necessity. VEG/ME49 representative
    entries are not identified as these exact experimental constructs.
  accessed_at: '2026-11-03T16:08:26.447549Z'
  support: supports
  snapshot_sha256: 446eff196318bfd47c2542160e3aa5bdd9e01b867cf15d569cc8eb1adf0f2a8a
- evidence_id: septin-dubois2019-pdf
  kind: authority
  reference: https://access.archive-ouverte.unige.ch/access/metadata/8d9f50fe-0548-4e4f-bc29-4b05a43e7ddc/download
  locator: 'Genuine accepted review manuscript; extracted text lines40–578: Abstract,Introduction,microneme
    diversity/structure,contents/conservation,biogenesis/maturation/trafficking and
    signaling cascade. Later preparing-secretion/fusion/insights/conclusion,Table1,figures/pixels
    not comprehensively inspected'
  summary: Secondary synthesis supports lineage/stage variation, microneme cargo complexes
    and soluble versus transmembrane/cytoplasmic portions. It distinguishes named
    complex components from all-stage universal composition and hypotheses from demonstrated
    steps. Accepted-manuscript copyright does not grant an image-hosting licence;
    no source image is adopted.
  accessed_at: '2026-11-03T16:09:07.902055Z'
  support: supports
  snapshot_sha256: b9604930c84058ad9c4812ceb293f1af012bdea81120ddd4025b56527154e0b2
- evidence_id: septin-gene-MIC1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AMIC1%29%20AND%20%28organism_id%3A5811%29%20AND%20%28reviewed%3Atrue%29&format=json&size=100
  locator: Exact reviewed UniProt gene-name/organism query
  summary: One exact reviewed MIC1 entry O00834 returned for organism5811. This supports
    the chosen representative only, not complete taxonomic distribution, membership
    or necessity.
  accessed_at: '2026-11-03T16:08:26.651161Z'
  support: supports
  snapshot_sha256: 53e2eb2ddfa3ca14039163ebd77d1ed03cb6972f168411567ddb31e3b35c6f26
  search_scope: UniProtKB gene_exact:MIC1 AND organism_id:5811 AND reviewed:true;
    format=json,size100,no date filter; one returned record, exact organism query,
    no descendant expansion or gene absence conclusion; fetch 2026-11-03T16:08:26.651161Z.
- evidence_id: septin-gene-AMA1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AAMA1%29%20AND%20%28organism_id%3A432359%29%20AND%20%28reviewed%3Atrue%29&format=json&size=100
  locator: Exact reviewed UniProt gene-name/organism query
  summary: One exact reviewed AMA1 entry B6KAM0 returned for organism432359. This
    supports the chosen representative only, not complete taxonomic distribution,
    membership or necessity.
  accessed_at: '2026-11-03T16:08:26.724041Z'
  support: supports
  snapshot_sha256: cf7a69f7fa39099a8f5449e7d474a9e80b78b14e4aeaf0ba4463c6f035810da6
  search_scope: UniProtKB gene_exact:AMA1 AND organism_id:432359 AND reviewed:true;
    format=json,size100,no date filter; one returned record, exact organism query,
    no descendant expansion or gene absence conclusion; fetch 2026-11-03T16:08:26.724041Z.
- evidence_id: septin-ipr-mahrp1
  kind: search
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q6V0W9/?page_size=200
  locator: Exact Q6V0W9 InterPro entry lookup; HTTP204 no body
  summary: No InterPro entries returned by this bounded single-accession endpoint.
    This is not evidence that MAHRP1 lacks a biological family or that related proteins
    are absent. Existing grounding TODO remains open.
  accessed_at: '2026-11-03T16:09:08.187790Z'
  support: supports
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
  search_scope: InterPro /entry/interpro/protein/uniprot/Q6V0W9/?page_size=200 at
    2026-11-03T16:09:08.187790Z; one accession,no date filter,HTTP204; no exhaustive
    family/name/sequence search.
- evidence_id: septin-ipr-sbp1
  kind: search
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q9NFF5/?page_size=200
  locator: Exact Q9NFF5 InterPro response; single family hit IPR044661
  summary: Returned family name is Mediator RNA polymeraseII transcription15a/b/c-like;
    this automatic/domain context does not independently establish exact SBP1 structural
    identity. No unrelated family grounding is adopted or absence inferred.
  accessed_at: '2026-11-03T16:09:08.206398Z'
  support: supports
  snapshot_sha256: 60a68fb3ff1de33c4f842517b5d0c3819055913e241200a31cfa3593610d3f8d
  search_scope: InterPro /entry/interpro/protein/uniprot/Q9NFF5/?page_size=200 at
    2026-11-03T16:09:08.206398Z; exact accession,one returned hit,no date filter;
    not an exhaustive family search.
- evidence_id: septin-rex1-search
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=TITLE_ABS%3AREX1%20AND%20TITLE_ABS%3APlasmodium&pageSize=25
  locator: Bounded title/abstract query result metadata; eight returned titles inspected
  summary: The result list provides discovery context only; it is not eight independently
    read full abstracts or bodies and supplies no new mechanistic finding. REX resident
    context is independently supported by the current Cooke primary body.
  accessed_at: '2026-11-03T16:09:08.175254Z'
  support: supports
  snapshot_sha256: 28766e6e0f8a25047d70e80c63095c7f80d0fb7b657ad45f762ddfad8adc71da
  search_scope: Europe PMC TITLE_ABS:REX1 AND TITLE_ABS:Plasmodium; resultType=core,pageSize25,no
    date restriction;eight results, title/metadata inspection only,actual fetch 2026-11-03T16:09:08.175254Z.
- evidence_id: septin-retrieval-source-receipts
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/adversary-septin/source-receipts.json
  locator: Actual source retrieval outcomes, request dates and returned-file hashes
  summary: Transport/endpoint availability evidence only. HTTP200 BioC service/error
    packets for Carruthers1997/Huynh2003/Brown2016 are not scientific bodies; later
    S3 and EuropePMC fallbacks failed. Spycher direct publisher403 and later web timeouts
    do not negate its complete primary abstract or the selected publisher text actually
    displayed. REX2015 optional body retrieval429 is not scientific absence.
  accessed_at: '2026-11-03T16:16:15.443886Z'
  support: supports
  snapshot_sha256: 47814c463ea8c56a8c1bae11e5e85f2846c6c429a3fffe2a96ec0071af42eadd
- evidence_id: septin-retrieval-additional-source-receipts
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/adversary-septin/additional-source-receipts.json
  locator: Actual source retrieval outcomes, request dates and returned-file hashes
  summary: Transport/endpoint availability evidence only. HTTP200 BioC service/error
    packets for Carruthers1997/Huynh2003/Brown2016 are not scientific bodies; later
    S3 and EuropePMC fallbacks failed. Spycher direct publisher403 and later web timeouts
    do not negate its complete primary abstract or the selected publisher text actually
    displayed. REX2015 optional body retrieval429 is not scientific absence.
  accessed_at: '2026-11-03T16:16:15.443886Z'
  support: supports
  snapshot_sha256: dd4da204fbdad868023f728549405248b099073c2a93e15242fd314d2dd288b3
- evidence_id: septin-retrieval-fallback-source-receipts
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/adversary-septin/fallback-source-receipts.json
  locator: Actual source retrieval outcomes, request dates and returned-file hashes
  summary: Transport/endpoint availability evidence only. HTTP200 BioC service/error
    packets for Carruthers1997/Huynh2003/Brown2016 are not scientific bodies; later
    S3 and EuropePMC fallbacks failed. Spycher direct publisher403 and later web timeouts
    do not negate its complete primary abstract or the selected publisher text actually
    displayed. REX2015 optional body retrieval429 is not scientific absence.
  accessed_at: '2026-11-03T16:16:15.443886Z'
  support: supports
  snapshot_sha256: da77e5b603cdc799930d836b66e6a37cb64adfd00b3b24ac8b84a593b0c42dd3
- evidence_id: septin-catalogue
  kind: search
  reference: https://imodulondb.org/api/datasets
  locator: Complete current official iModulonDB organism names/ids and dataset-key
    fields
  summary: No matching Plasmodium falciparum/3D7, Toxoplasma gondii/VEG/ME49 or broader
    apicomplexan/eukaryotic host occurs. Whole record molecular/pathway claims require
    assessment even where the native protein inventory is empty. No unrelated bacterial
    downstream query or biological absence inference is justified.
  accessed_at: '2026-11-03T16:08:26.624780Z'
  support: supports
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  search_scope: GET https://imodulondb.org/api/datasets at 2026-11-03T16:08:26.624780Z;
    complete20-organism response,no date filter or pagination truncation; inspect
    all id/name/dataset fields for Plasmodium/falciparum/3D7,Toxoplasma/gondii/VEG/ME49,Apicomplexa
    and eukaryotic context. Noncoverage is restricted to this catalogue snapshot.
- evidence_id: septin-adapter-runner-historical
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Actual historical00:49Z invocation, no new runner execution
  summary: Attempt2026-11-03T00:49:00.848907Z–00:49:00.863225Z exited1 with PermissionError
    reading pyvenv.cfg. Fresh official catalogue is a separately evidenced fallback;
    no successful/fresh runner invocation is claimed.
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: supports
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: plaque-current-1
  kind: record_content
  reference: data/structures/membrane_organelle/methane_oxidizing_organelle.yaml
  locator: Entire current maintained record at 61d3617ae8700b99198e2aaf01f3b2437933de6c
    including all graphs/history/discussions
  summary: Current frozen target independently read. Stale delta is added unreviewed
    Q603F1 identity example plus history; reassessed substantively.
  accessed_at: '2026-11-03T16:16:31.441887Z'
  support: supports
  snapshot_sha256: 8d513f399ed2555737573ae9d0c888514408062fcd5f2ec60bc19bad9e93f2c8
- evidence_id: plaque-original-1
  kind: prior_review
  reference: reviews/structured/20261022T022232Z-methane-oxidizing-organelle-audit/review.yaml
  locator: Exact staleness-selected authoritative YAML and derived Markdown, all source/check/assessment/finding/action
    fields
  summary: Historical pair independently validates/renders; every historical source
    hash matches. Qualified pass had no scientific findings.
  accessed_at: '2026-11-03T16:16:31.441887Z'
  support: supports
  snapshot_sha256: 0864d9f497ea8b445ff162b6c6bbfe2bb72aa8e7450f0d7032ca197679e9151b
- evidence_id: plaque-current-5
  kind: record_content
  reference: data/structures/membrane_organelle/micronucleus.yaml
  locator: Entire current maintained record at 61d3617ae8700b99198e2aaf01f3b2437933de6c
    including all graphs/history/discussions
  summary: Current frozen target independently read. Current bytes match original
    frozen target; original scientific findings/dispositions reassessed.
  accessed_at: '2026-11-03T16:16:31.441887Z'
  support: supports
  snapshot_sha256: fe6086eb62e1499109082d20f9a25ff776a68482d0ab89253469f6f3bfcbb8c1
- evidence_id: plaque-original-5
  kind: prior_review
  reference: reviews/structured/20261022T022237Z-micronucleus-audit/review.yaml
  locator: Exact staleness-selected authoritative YAML and derived Markdown, all source/check/assessment/finding/action
    fields
  summary: Historical pair independently validates/renders; every historical source
    hash matches. Qualified pass had no scientific findings.
  accessed_at: '2026-11-03T16:16:31.441887Z'
  support: supports
  snapshot_sha256: de79f648d1fa9ea63b8a29ce2725c2a3d8e6c81cc35ca3e6f0e41c2aaee0367c
- evidence_id: plaque-current-6
  kind: record_content
  reference: data/structures/membrane_organelle/microsporidian_posterior_vacuole.yaml
  locator: Entire current maintained record at 61d3617ae8700b99198e2aaf01f3b2437933de6c
    including all graphs/history/discussions
  summary: Current frozen target independently read. Current bytes match original
    frozen target; original scientific findings/dispositions reassessed.
  accessed_at: '2026-11-03T16:16:31.441887Z'
  support: supports
  snapshot_sha256: db2c2e1271b64aa7037885eeb2f1e39c6e3ee5d769b83e8374ed96d2e768f6b8
- evidence_id: plaque-original-6
  kind: prior_review
  reference: reviews/structured/20261022T022238Z-microsporidian-posterior-vacuole-audit/review.yaml
  locator: Exact staleness-selected authoritative YAML and derived Markdown, all source/check/assessment/finding/action
    fields
  summary: Historical pair independently validates/renders; every historical source
    hash matches. Two original minor findings remain confirmed with exact lineage;
    no target correction made.
  accessed_at: '2026-11-03T16:16:31.441887Z'
  support: supports
  snapshot_sha256: b3fb563d38edb33f94e0de1bdf485a430468f9c8695f82d83d04ebbdb61390e8
- evidence_id: plaque-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Frozen native contract; current bytes independently compared with previously
    read PR2368 policies; record skill/profile and CausalNode definition freshly reread
  summary: Genes, proteins, pathways and stress/trait claims trigger applicability
    without an expression-module assertion. Genuine sparse physical morphology is
    distinguished.
  accessed_at: '2026-11-03T16:16:31.441887Z'
  support: context_only
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: plaque-rubric
  kind: authority
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Frozen native contract; current bytes independently compared with previously
    read PR2368 policies; record skill/profile and CausalNode definition freshly reread
  summary: Claim-scoped identity, chemistry/material, taxonomy, roles, necessity,
    graphs and experimental modalities are separate questions; optional unfilled slots
    alone are not issues.
  accessed_at: '2026-11-03T16:16:31.441887Z'
  support: context_only
  snapshot_sha256: e6b9e4b16a58c54402bed7bbee2c8b94a91d37562e8b0ee8b94ff0c829184a70
- evidence_id: plaque-graph-rubric
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Frozen native contract; current bytes independently compared with previously
    read PR2368 policies; record skill/profile and CausalNode definition freshly reread
  summary: Preserve epistemic scope and source taxon; descriptive topology does not
    prove a physical driver.
  accessed_at: '2026-11-03T16:16:31.441887Z'
  support: context_only
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: plaque-protein-contract
  kind: authority
  reference: .claude/skills/uniprot-protein-examples/SKILL.md
  locator: Frozen native contract; current bytes independently compared with previously
    read PR2368 policies; record skill/profile and CausalNode definition freshly reread
  summary: Native accession verification is identity coverage, not structure membership
    or necessity; protein complexes may be covered by component_ref.
  accessed_at: '2026-11-03T16:16:31.441887Z'
  support: context_only
  snapshot_sha256: 6462894c8257823bae2b175c34693cd42f11ff9269a3829c15b9286ba6d7c876
- evidence_id: plaque-schema-policy
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Frozen native contract; current bytes independently compared with previously
    read PR2368 policies; record skill/profile and CausalNode definition freshly reread
  summary: CausalNode explicitly allows GENE_OR_PROTEIN for proteins, protein families
    and protein complexes. No mandatory pMMO retyping is inferred from complex membership.
  accessed_at: '2026-11-03T16:16:31.441887Z'
  support: context_only
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: plaque-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0044227,GO:0043231,GO:0046188,GO:0031040,GO:0005634,GO:0000228,GO:0019953,GO:0044099
  locator: Complete exact responses for0044227,0043231,0046188,0031040,0005634,0000228,0019953,0044099;
    definitions/synonyms/typed children inspected
  summary: Exact methane-organelle identity and aliases, intracellular membrane-bounded
    parent, methane catabolism, ciliate micronucleus/nucleus parent, chromosome-versus-DNA
    distinction, sexual reproduction and microsporidian polar-tube identities agree.
    Current GO micronucleus definition explicitly says genic transcription is absent;
    graph remains mature Tetrahymena scope.
  accessed_at: '2026-11-03T16:08:40.083192Z'
  support: supports
  snapshot_sha256: 5109e403885edc18c685d1056d00e94740d3288c92ab4981b5696b1074055ab6
- evidence_id: plaque-tax2
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2
  locator: Complete native ENA taxonomy identity/rank/aliases/lineage response
  summary: Bacteria is domain2; record explicitly restricts occurrence to the methanotrophic
    subset with pMMO ICMs, not all bacteria.
  accessed_at: '2026-11-03T16:08:40.083287Z'
  support: supports
  snapshot_sha256: 314bd7723b8dea04f1840809fb74e06c514664fba9c6a0619e8f12e2a6dceef1
- evidence_id: plaque-tax243233
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/243233
  locator: Complete native ENA taxonomy identity/rank/aliases/lineage response
  summary: 243233 is Methylococcus capsulatus strain Bath, including ATCC33009/NCIB11132
    aliases; exact Zhu primary strain and reference proteins match.
  accessed_at: '2026-11-03T16:08:40.083340Z'
  support: supports
  snapshot_sha256: 6e0d814039b9cd0fda6aed3f32644db66ec2201d0f88fcfeb2d8aace5b3cb9ff
- evidence_id: plaque-tax5911
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5911
  locator: Complete native ENA taxonomy identity/rank/aliases/lineage response
  summary: 5911 is Tetrahymena thermophila species; Hamilton sequenced SB210, kept
    as a named experimental strain rather than an inferred new strain CURIE.
  accessed_at: '2026-11-03T16:08:40.083760Z'
  support: supports
  snapshot_sha256: 42cc1d612d8aa31ffc6e484dfb7b846348bea7e26ca272eb4b5f4e7739df4ce6
- evidence_id: plaque-tax6029
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/6029
  locator: Complete native ENA taxonomy identity/rank/aliases/lineage response
  summary: 6029 is phylum Microsporidia; infectious-spore scope is distinct from every
    intracellular vegetative stage.
  accessed_at: '2026-11-03T16:08:40.086742Z'
  support: supports
  snapshot_sha256: 5a4e56118a35563f14efbf594aef989903527ec8c8aea7e85d5a2ff21ea44243
- evidence_id: plaque-tax6039
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/6039
  locator: Complete native ENA taxonomy identity/rank/aliases/lineage response
  summary: 6039 is Vairimorpha necatrix species; source cultivated spores through
    Helicoverpa zea, not a taxon synonym for other microsporidia.
  accessed_at: '2026-11-03T16:08:40.089480Z'
  support: supports
  snapshot_sha256: 5fe781a5d5fc3a7d7e7ad15ad63b15f2492dae7d8b7c1fddb417bf2830285258
- evidence_id: plaque-protein-Q607G3
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q607G3.json
  locator: Native entryType/protein names/all gene rows/organism; FUNCTION,SUBUNIT,SUBCELLULAR
    LOCATION and evidence pointers
  summary: Reviewed beta/PmoA entry lists pmoA1/MCA1797 and pmoA2/MCA2854 with pmoA
    alias in Bath243233. pMMO is a nonamer of three heterotrimeric protomers; membrane
    annotation is cited correctly. Entry identity is not unique-locus assignment or
    independent record membership proof.
  accessed_at: '2026-11-03T16:08:40.090815Z'
  support: supports
  snapshot_sha256: 43cb1956e5bdf800750c2df52e35997d4c5c9ab46fa70fd1e8680f707b824446
- evidence_id: plaque-protein-G1UBD1
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/G1UBD1.json
  locator: Native entryType/protein names/all gene rows/organism; FUNCTION,SUBUNIT,SUBCELLULAR
    LOCATION and CAUTION
  summary: Reviewed alpha/PmoB entry lists pmoB1/MCA1796 and pmoB2/MCA2853 with pmoB
    alias in Bath243233. Membrane evidence PMIDs match. Native caution on proposed
    copper active site is not converted into a settled mechanistic record claim.
  accessed_at: '2026-11-03T16:08:40.165981Z'
  support: supports
  snapshot_sha256: 125e292aec089f2a4942cf71ad10b34bd161af50a6d425a32497f49a8883a6d0
- evidence_id: plaque-protein-Q603F1
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q603F1.json
  locator: Complete unreviewed entry identity, submission names, geneName, both ordered
    locus names and organism
  summary: Added Q603F1 is unreviewed TrEMBL, submission name matches the record,
    primary gene pmoC1 and taxon243233. Entry contains MCA1798 and MCA2855; current
    role only asserts a representative identity, not a unique locus, reviewed status,
    direct localization or necessity. No guessed equivalence to unrelated strain used.
  accessed_at: '2026-11-03T16:08:40.690267Z'
  support: supports
  snapshot_sha256: c6a9c6349c1242344d7289cc687b9b5fe17da01bdbeb8438b530d519f3006b86
- evidence_id: plaque-query-pmoA-reviewed
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=organism_id%3A243233+AND+gene_exact%3ApmoA+AND+reviewed%3Atrue&format=json&size=25
  locator: Complete returned native UniProtKB query page; suggestions ignored
  summary: Exact query returned ['Q607G3']. pmoA/pmoB aliases resolve reviewed examples;
    exact pmoC returns zero whereas exact primary pmoC1 returns Q603F1. This is a
    query/alias boundary, not protein absence or a contradiction of the representative
    example.
  accessed_at: '2026-11-03T16:08:42.229233Z'
  support: supports
  search_scope: UniProtKB organism_id243233 AND exact gene pmoA; reviewed:true; size25
    at 2026-11-03T16:08:42.229233Z; inspected 1 returned entries. No other strain
    or suggested relaxed query substituted.
  snapshot_sha256: 84fc73bb2b94052e0d8fff599c38dd307c90fddd2e7cb7a6c623566206a11e2f
- evidence_id: plaque-query-pmoA-all
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=organism_id%3A243233+AND+gene_exact%3ApmoA&format=json&size=25
  locator: Complete returned native UniProtKB query page; suggestions ignored
  summary: Exact query returned ['Q607G3']. pmoA/pmoB aliases resolve reviewed examples;
    exact pmoC returns zero whereas exact primary pmoC1 returns Q603F1. This is a
    query/alias boundary, not protein absence or a contradiction of the representative
    example.
  accessed_at: '2026-11-03T16:08:42.399169Z'
  support: supports
  search_scope: UniProtKB organism_id243233 AND exact gene pmoA; all statuses; size25
    at 2026-11-03T16:08:42.399169Z; inspected 1 returned entries. No other strain
    or suggested relaxed query substituted.
  snapshot_sha256: 84fc73bb2b94052e0d8fff599c38dd307c90fddd2e7cb7a6c623566206a11e2f
- evidence_id: plaque-query-pmoB-reviewed
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=organism_id%3A243233+AND+gene_exact%3ApmoB+AND+reviewed%3Atrue&format=json&size=25
  locator: Complete returned native UniProtKB query page; suggestions ignored
  summary: Exact query returned ['G1UBD1']. pmoA/pmoB aliases resolve reviewed examples;
    exact pmoC returns zero whereas exact primary pmoC1 returns Q603F1. This is a
    query/alias boundary, not protein absence or a contradiction of the representative
    example.
  accessed_at: '2026-11-03T16:08:42.453095Z'
  support: supports
  search_scope: UniProtKB organism_id243233 AND exact gene pmoB; reviewed:true; size25
    at 2026-11-03T16:08:42.453095Z; inspected 1 returned entries. No other strain
    or suggested relaxed query substituted.
  snapshot_sha256: 8d550b83583596e145d82c3df4d98801d85ad571593eb06f31ebefb09f1c37b7
- evidence_id: plaque-query-pmoB-all
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=organism_id%3A243233+AND+gene_exact%3ApmoB&format=json&size=25
  locator: Complete returned native UniProtKB query page; suggestions ignored
  summary: Exact query returned ['G1UBD1']. pmoA/pmoB aliases resolve reviewed examples;
    exact pmoC returns zero whereas exact primary pmoC1 returns Q603F1. This is a
    query/alias boundary, not protein absence or a contradiction of the representative
    example.
  accessed_at: '2026-11-03T16:08:42.471872Z'
  support: supports
  search_scope: UniProtKB organism_id243233 AND exact gene pmoB; all statuses; size25
    at 2026-11-03T16:08:42.471872Z; inspected 1 returned entries. No other strain
    or suggested relaxed query substituted.
  snapshot_sha256: 8d550b83583596e145d82c3df4d98801d85ad571593eb06f31ebefb09f1c37b7
- evidence_id: plaque-query-pmoC-reviewed
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=organism_id%3A243233+AND+gene_exact%3ApmoC+AND+reviewed%3Atrue&format=json&size=25
  locator: Complete returned native UniProtKB query page; suggestions ignored
  summary: Exact query returned []. pmoA/pmoB aliases resolve reviewed examples; exact
    pmoC returns zero whereas exact primary pmoC1 returns Q603F1. This is a query/alias
    boundary, not protein absence or a contradiction of the representative example.
  accessed_at: '2026-11-03T16:08:42.485308Z'
  support: supports
  search_scope: UniProtKB organism_id243233 AND exact gene pmoC; reviewed:true; size25
    at 2026-11-03T16:08:42.485308Z; inspected 0 returned entries. No other strain
    or suggested relaxed query substituted.
  snapshot_sha256: 5021e624e752b001ce3e3846e8f158ed4aeb93a4c9a72fdb35a0c5b14a0eea84
- evidence_id: plaque-query-pmoC-all
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=organism_id%3A243233+AND+gene_exact%3ApmoC&format=json&size=25
  locator: Complete returned native UniProtKB query page; suggestions ignored
  summary: Exact query returned []. pmoA/pmoB aliases resolve reviewed examples; exact
    pmoC returns zero whereas exact primary pmoC1 returns Q603F1. This is a query/alias
    boundary, not protein absence or a contradiction of the representative example.
  accessed_at: '2026-11-03T16:08:42.567896Z'
  support: supports
  search_scope: UniProtKB organism_id243233 AND exact gene pmoC; all statuses; size25
    at 2026-11-03T16:08:42.567896Z; inspected 0 returned entries. No other strain
    or suggested relaxed query substituted.
  snapshot_sha256: dfa83c9e1843cc06b2835d58166492330e698b670a594d84660b6ed24843b5fd
- evidence_id: plaque-query-pmoC1-all
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28organism_id%3A243233%29%20AND%20%28gene_exact%3ApmoC1%29&format=json&size=25
  locator: Complete returned native UniProtKB query page; suggestions ignored
  summary: Exact query returned ['Q603F1']. pmoA/pmoB aliases resolve reviewed examples;
    exact pmoC returns zero whereas exact primary pmoC1 returns Q603F1. This is a
    query/alias boundary, not protein absence or a contradiction of the representative
    example.
  accessed_at: '2026-11-03T16:11:34.527649Z'
  support: supports
  search_scope: UniProtKB organism_id243233 AND exact gene pmoC1; all statuses; size25
    at 2026-11-03T16:11:34.527649Z; inspected 1 returned entries. No other strain
    or suggested relaxed query substituted.
  snapshot_sha256: e5fb931087c81640db384ea0551ba88b997361062126f1d38613040e6fcd0c78
- evidence_id: plaque-PMID12379148
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12379148+AND+SRC%3AMED&format=json&resultType=core&pageSize=25
  locator: Complete exact PMID metadata and primary abstract only
  summary: Basu2003 primary abstract describes purified Bath membrane-associated pMMO
    complex and subunits; native cited membrane evidence identity agrees.
  accessed_at: '2026-11-03T16:08:41.361376Z'
  support: supports
  search_scope: Bounded EuropePMC exact DOI or PMID query https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12379148+AND+SRC%3AMED&format=json&resultType=core&pageSize=25
    at 2026-11-03T16:08:41.361376Z; pageSize25; 1 metadata/abstract match inspected.
    No open-ended search or full-text inference.
  snapshot_sha256: faf3f906a3399c5704a368b8747c0d7334fb7fac8103d1ef28d98a5c0cb32978
- evidence_id: plaque-PMID15674245
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15674245+AND+SRC%3AMED&format=json&resultType=core&pageSize=25
  locator: Complete exact PMID metadata and primary abstract only
  summary: Lieberman2005 primary abstract reports Bath membrane enzyme with alpha3beta3gamma3
    arrangement at2.8A; supports exact assembly identity, not every modern active-site
    conclusion.
  accessed_at: '2026-11-03T16:08:41.613967Z'
  support: supports
  search_scope: Bounded EuropePMC exact DOI or PMID query https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15674245+AND+SRC%3AMED&format=json&resultType=core&pageSize=25
    at 2026-11-03T16:08:41.613967Z; pageSize25; 1 metadata/abstract match inspected.
    No open-ended search or full-text inference.
  snapshot_sha256: 91fa087bf3f4b52693a764ba65f065814504f9f4102e8d1acee62e3f513c34f4
- evidence_id: plaque-PMID22013879
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A22013879+AND+SRC%3AMED&format=json&resultType=core&pageSize=25
  locator: Complete exact PMID metadata and primary abstract only
  summary: Smith2011 primary abstract concerns Methylocystis strain M and includes
    revised Bath structural models. Record accurately attributes this as UniProt evidence
    pointer; not represented here as direct Bath-cell localization experiment.
  accessed_at: '2026-11-03T16:08:41.766713Z'
  support: supports
  search_scope: Bounded EuropePMC exact DOI or PMID query https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A22013879+AND+SRC%3AMED&format=json&resultType=core&pageSize=25
    at 2026-11-03T16:08:41.766713Z; pageSize25; 1 metadata/abstract match inspected.
    No open-ended search or full-text inference.
  snapshot_sha256: 463803cf106c89e5fffd9f5588d87702d07d879bc0aca5cebc9933dbc2a34928
- evidence_id: plaque-zhu2022-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fs41467-022-32752-9%22&format=json&resultType=core&pageSize=25
  locator: Exact DOI metadata title/authors/year/PMID/PMC
  summary: Zhu et al.2022 DOI/PMID36064719/PMC9445010 identity and title agree; claims
    assessed in genuine body.
  accessed_at: '2026-11-03T16:08:40.690353Z'
  support: supports
  search_scope: Bounded EuropePMC exact DOI or PMID query https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fs41467-022-32752-9%22&format=json&resultType=core&pageSize=25
    at 2026-11-03T16:08:40.690353Z; pageSize25; 1 metadata/abstract match inspected.
    No open-ended search or full-text inference.
  snapshot_sha256: f891f1769f8da9293421c782d5a2c85713373fa04b4d9a6d85b6f919cf21352a
- evidence_id: plaque-whiddon2019-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1111%2F1751-7915.13458%22&format=json&resultType=core&pageSize=25
  locator: Exact DOI metadata title/authors/year/PMID/PMC
  summary: Whiddon et al.2019 DOI/PMID31264365/PMC6680624 identity agrees; body has
    explicit type-I strain limits.
  accessed_at: '2026-11-03T16:08:40.694111Z'
  support: supports
  search_scope: Bounded EuropePMC exact DOI or PMID query https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1111%2F1751-7915.13458%22&format=json&resultType=core&pageSize=25
    at 2026-11-03T16:08:40.694111Z; pageSize25; 1 metadata/abstract match inspected.
    No open-ended search or full-text inference.
  snapshot_sha256: 1d35c5147a5033d4c191cd7bd5c54c7cda2c4c805249ab22465fb930bacc8f2c
- evidence_id: plaque-hamilton2016-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.7554%2FeLife.19090%22&format=json&resultType=core&pageSize=25
  locator: Exact DOI metadata title/authors/year/PMID/PMC
  summary: Hamilton et al.2016 DOI/PMID27892853/PMC5182062 identity agrees; genuine
    eLife JATS supports current scope.
  accessed_at: '2026-11-03T16:08:40.734959Z'
  support: supports
  search_scope: Bounded EuropePMC exact DOI or PMID query https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.7554%2FeLife.19090%22&format=json&resultType=core&pageSize=25
    at 2026-11-03T16:08:40.734959Z; pageSize25; 1 metadata/abstract match inspected.
    No open-ended search or full-text inference.
  snapshot_sha256: add684cabf2318c15f0fcc9831a0b0129ceaf4450c4227a38dbcc0a630237f89
- evidence_id: plaque-findley2005-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.14411%2Ffp.2005.014%22&format=json&resultType=core&pageSize=25
  locator: Exact DOI metadata title/authors/year/PMID/PMC
  summary: Findley et al.2005 DOI/PMID16004370 identity agrees; publisher PDF independently
    read.
  accessed_at: '2026-11-03T16:08:40.744223Z'
  support: supports
  search_scope: Bounded EuropePMC exact DOI or PMID query https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.14411%2Ffp.2005.014%22&format=json&resultType=core&pageSize=25
    at 2026-11-03T16:08:40.744223Z; pageSize25; 1 metadata/abstract match inspected.
    No open-ended search or full-text inference.
  snapshot_sha256: 9120d2034f1821f7f4530db70ef308cd7aa553d00a29cd04925511fd2168b38e
- evidence_id: plaque-jaroenlak2020-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1371%2Fjournal.ppat.1008738%22&format=json&resultType=core&pageSize=25
  locator: Exact DOI metadata title/authors/year/PMID/PMC
  summary: Jaroenlak et al.2020 DOI/PMID32946515/PMC7526891 identity agrees; current
    source body distinguishes SBFSEM and2D TEM.
  accessed_at: '2026-11-03T16:08:40.950331Z'
  support: supports
  search_scope: Bounded EuropePMC exact DOI or PMID query https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1371%2Fjournal.ppat.1008738%22&format=json&resultType=core&pageSize=25
    at 2026-11-03T16:08:40.950331Z; pageSize25; 1 metadata/abstract match inspected.
    No open-ended search or full-text inference.
  snapshot_sha256: bea17235718303e5ef0a4def2acfaf4daa54be06f1d2f39116b3c8b1b487ca06
- evidence_id: plaque-sharma2024-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1371%2Fjournal.pbio.3002533%22&format=json&resultType=core&pageSize=25
  locator: Exact DOI metadata title/authors/year/PMID/PMC
  summary: Sharma et al.2024 DOI/PMID38422169/PMC10931468 identity agrees; current
    body limits cryoET to tube regions.
  accessed_at: '2026-11-03T16:08:41.349428Z'
  support: supports
  search_scope: Bounded EuropePMC exact DOI or PMID query https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1371%2Fjournal.pbio.3002533%22&format=json&resultType=core&pageSize=25
    at 2026-11-03T16:08:41.349428Z; pageSize25; 1 metadata/abstract match inspected.
    No open-ended search or full-text inference.
  snapshot_sha256: 0b2b398578b10a62477c42c6bd95873681978114e76461952c22af8b6f423349
- evidence_id: plaque-troemel2015-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.fgb.2015.08.007%22&format=json&resultType=core&pageSize=25
  locator: Exact DOI metadata title/authors/year/PMID/PMC
  summary: Troemel/Becnel2015 DOI/PMID26300319/PMC4587305 identity agrees; primary
    firing observations examined in body.
  accessed_at: '2026-11-03T16:08:40.856523Z'
  support: supports
  search_scope: Bounded EuropePMC exact DOI or PMID query https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.fgb.2015.08.007%22&format=json&resultType=core&pageSize=25
    at 2026-11-03T16:08:40.856523Z; pageSize25; 1 metadata/abstract match inspected.
    No open-ended search or full-text inference.
  snapshot_sha256: a31bc847a7304ebcb9f69314bceca69a0a7e7b92d9ae780dd21b885621a6b0c8
- evidence_id: plaque-zhu2022-body
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC9445010.1/PMC9445010.1.xml
  locator: 'Genuine PMC9445010.1 JATS: Introduction; Results Sec3–6, figure1–4 captions;
    Discussion; Methods Sec9–11; no figure pixels or raw-data reanalysis'
  summary: Copper-replete Bath ICMs and arrays observed by serial cryoFIB/SEM/cellular
    cryoET; isolated native membranes resolve the trimer of PmoA/B/C heterotrimers.
    Continuity supports authors invagination interpretation but static data alone
    cannot distinguish every biogenesis event. Reconstituted larger nanodiscs correlate
    with higher methane oxidation; graph does not assert array-alone sufficiency,
    exact active site or direct PmoB salt-bridge necessity. Methane→methanol chemistry
    supported in bounded activity assays.
  accessed_at: '2026-11-03T16:09:05.727035Z'
  support: supports
  snapshot_sha256: 0746414b5ec7991901750327dfba636e5eef7c7f8a9aab192cd30d1c8b619fd6
- evidence_id: plaque-whiddon2019-body
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC6680624.1/PMC6680624.1.xml
  locator: 'Genuine PMC6680624.1 JATS: Introduction, Results staining/copper dependence/connectivity,
    Discussion and bacterial strain/growth Methods; figure captions read, not pixels'
  summary: Main strain Methylotuvimicrobium alcaliphilum20Z plus Methyloprofundus
    sedimenti and Methylomonas methanicaS1; no Bath experiment transferred. Lipophilic
    staining, FRAP and MDH colocalization are consistent with ICM connectivity; authors
    retain cycling/isolated-stack alternatives and resolution limits. Supports membrane-material
    description, not invariant complete mechanism.
  accessed_at: '2026-11-03T16:09:05.727282Z'
  support: supports
  snapshot_sha256: e8eba8f9c089eaa12d0f334becd518923c523a063f7351950f94efeaab95b916
- evidence_id: plaque-stolyar2001-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1128%2FJB.183.5.1810-1812.2001%22&format=json&resultType=core&pageSize=25
  locator: Complete exact DOI primary abstract only
  summary: Transcripts and chromosomal gene fusions assay two Bath pmo gene clusters;
    functional redundancy and copper-dependent relative expression support the record
    narrow expression-study note. Full text was not recovered; not used to certify
    exact operon or every pmoC copy.
  accessed_at: '2026-11-03T16:08:40.716125Z'
  support: supports
  search_scope: Bounded EuropePMC exact DOI or PMID query https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1128%2FJB.183.5.1810-1812.2001%22&format=json&resultType=core&pageSize=25
    at 2026-11-03T16:08:40.716125Z; pageSize25; 1 metadata/abstract match inspected.
    No open-ended search or full-text inference.
  snapshot_sha256: 04595a0090ef48d71a60a68829dc97aca59ca8d1bbf988da2a3491d99e0809ca
- evidence_id: plaque-stolyar2001-body
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC95072.1/PMC95072.1.xml
  locator: Attempted primary body route only; S3 returned404 or BioC returned explicit
    No result text
  summary: No usable full body retrieved on this route; body-scoped claims not inferred
    from status200 or metadata. Complete primary abstract used for the narrow cited
    claim.
  accessed_at: '2026-11-03T16:09:05.727364Z'
  support: context_only
  snapshot_sha256: f6f8cc522fdfba0a2517f35e088d01f8088f1dee90713fe8e3abf3729dd860fa
- evidence_id: plaque-stolyar2001-bioc
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_xml/PMC95072/unicode
  locator: Attempted primary body route only; S3 returned404 or BioC returned explicit
    No result text
  summary: No usable full body retrieved on this route; body-scoped claims not inferred
    from status200 or metadata. Complete primary abstract used for the narrow cited
    claim.
  accessed_at: '2026-11-03T16:11:34.525330Z'
  support: context_only
  snapshot_sha256: 478f38e0765ee9c406831bb2fc27e8019ac5227c20c6b28ca0de582d8449354a
- evidence_id: plaque-hamilton2016-body
  kind: primary_source
  reference: https://elifesciences.org/articles/19090.xml
  locator: 'Genuine publisher eLife JATS: Introduction s1; Results s2-1-1 chromosome-length
    assembly; Methods s3-1,s3-2,s3-4; captions in these sections; no figure pixels/raw
    genome reassembly'
  summary: Mature diploid transcriptionally silent germline nucleus differs from somatic
    MAC; IES/rearrangement examples vary across ciliates. SB210 was checked for five
    intact MIC chromosomes before purified-nucleus sequencing. Five near-full chromosome
    superassemblies retain small gaps/ordering uncertainties; current record does
    not claim gapless raw genome or all-stage absence of transcription.
  accessed_at: '2026-11-03T16:08:41.990497Z'
  support: supports
  snapshot_sha256: 3f40b07efdb6553647086529606c8f899d4731d0c17122cbf137aa36f440790b
- evidence_id: plaque-findley2005-pdf
  kind: primary_source
  reference: https://folia.paru.cas.cz/doi/10.14411/fp.2005.014.pdf
  locator: 'Actual publisher seven-page PDF text: p111–115 Abstract, Introduction,
    Methods, Results and Discussion; figure3/4 captions; no figure pixels or raw assays'
  summary: S.lophii activated/fixed EM supports posterior vesicle swelling during
    firing, not exact molecular force proof. Catalase/ACOX/nervonic-acid assays are
    source-specific observations; they are not positively asserted constituents in
    this sparse current record and do not automatically turn its generic physiological
    description into a structured gene-pathway claim. No peroxisome identity or microsporidian-wide
    protein composition inferred.
  accessed_at: '2026-11-03T16:09:05.727509Z'
  support: supports
  snapshot_sha256: 7721a29d8cc26889a87b20b17124dbfe1d90e6c049ba9a373c4acf16741c1588
- evidence_id: plaque-troemel2015-body
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4587305.1/PMC4587305.1.xml
  locator: 'Genuine PMC4587305.1 JATS: complete Introduction/main sections2–4 including
    firing section3 and Conclusions; video itself not independently replayed'
  summary: E.aedis firing observations show late posterior expansion; source explicitly
    presents pushing as appearance/likelihood and says underlying mechanism is poorly
    understood. Direct passage supports temporal/topological record claims; unqualified
    drives/pushes on final graph edge exceeds this source scope.
  accessed_at: '2026-11-03T16:09:05.727419Z'
  support: supports
  snapshot_sha256: 050ac5f6c989bebb195088da5d189222f2262d8129d132403eb961a9bc119b42
- evidence_id: plaque-jaroenlak2020-body
  kind: primary_source
  reference: https://journals.plos.org/plospathogens/article/file?id=10.1371/journal.ppat.1008738&type=manuscript
  locator: 'Genuine publisher JATS: Introduction; Results sec003–005 and Fig1/2 captions;
    Discussion sec010 plus Fig6 caption; no figure pixels/videos/raw reconstructions'
  summary: Dormant A.algerae SBFSEM reconstructs a posterior bowl-shaped vacuole;2D
    TEM Fig2E resolves its single membrane and interdigitation. Source describes SBFSEM
    and2D TEM, not electron tomography. Proposed active role in PT/cargo movement
    remains tentative. Other species and germination states are distinguished.
  accessed_at: '2026-11-03T16:08:41.784771Z'
  support: supports
  snapshot_sha256: 9afa23ee9a5b6f7d4717a4fa48bb5f2b0407e770caefa374c710b0d65543cf05
- evidence_id: plaque-sharma2024-body
  kind: primary_source
  reference: https://journals.plos.org/plosbiology/article/file?id=10.1371/journal.pbio.3002533&type=manuscript
  locator: 'Genuine publisher JATS: Results sec003 and Discussion sec007; Methods
    sec009–012, specifically light microscopy and on-grid tilt-series selection; relevant
    captions only, no pixels/raw tomograms'
  summary: V.necatrix germination dynamics were captured by light microscopy; cryoET
    examined extruded tube segments/cargo. Methods explicitly exclude spores and tube
    tips with ejected cargo from tilt-series collection. Static cryoET states have
    no time resolution and ordering is hypothetical. Correct taxon occurrence does
    not rescue the canonical example microscopy claim.
  accessed_at: '2026-11-03T16:08:41.977777Z'
  support: supports
  snapshot_sha256: 3b4e41fc3308ba1c825184d21355515f03a6e43b6a3ee25d85f7070ba33989ed
- evidence_id: plaque-jaroenlak2022-meta
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1007%2F978-3-030-93306-7_9%22&format=json&resultType=core&pageSize=25
  locator: Complete exact DOI metadata and SECONDARY chapter abstract only
  summary: Chapter discusses phylum-level polar-tube/spore apparatus and transport;
    full chapter not obtained. It does not independently measure posterior-vacuole
    prevalence. Broad infectious-spore context is triangulated with inspected primary
    species studies, not universal vegetative-stage or exact protein claims.
  accessed_at: '2026-11-03T16:08:41.348281Z'
  support: supports
  search_scope: Bounded EuropePMC exact DOI or PMID query https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1007%2F978-3-030-93306-7_9%22&format=json&resultType=core&pageSize=25
    at 2026-11-03T16:08:41.348281Z; pageSize25; 1 metadata/abstract match inspected.
    No open-ended search or full-text inference.
  snapshot_sha256: 1e7a89fbf7cddfd64b2c55246b623eccf7b433356ec00b696936ee2c57afcdfe
- evidence_id: plaque-posterior-go-query
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=posterior%20vacuole&limit=25&page=1
  locator: Complete first25 returned QuickGO matches for posterior vacuole
  summary: No exact microsporidian posterior-vacuole identity among these25 results;
    broad vacuole/polar structures are not substituted for this structure. Bounded
    result supports retaining minted identity, not exhaustive ontology-absence proof.
  accessed_at: '2026-11-03T16:09:05.727580Z'
  support: supports
  search_scope: QuickGO ontology search query posterior vacuole; limit25,page1 at
    2026-11-03T16:09:05.727580Z; all25 returned terms inspected; no subsequent pages
    or exhaustive synonym search claimed.
  snapshot_sha256: 7ba83a5ed2245e4e8f3c404b6d8ca8ffcbb7feeea4e3bf0bb8d4002b2e77d21b
- evidence_id: plaque-catalogue
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Fresh complete official /api/datasets response, all20 organism rows and
    dataset listings inspected
  summary: No Methylococcus/Bath methanotroph host, Tetrahymena or microsporidian
    host is listed. Broad Bacteria distribution is not a license to substitute unrelated
    bacterial/archaeal datasets. Methane proteins/metabolism and micronuclear genic-transcription/genome
    program trigger applicability, but no matched downstream gene/module query applies.
    Posterior vacuole itself is genuinely sparse physical morphology. Noncoverage
    is not negative biology; no generated module prose used.
  accessed_at: '2026-11-03T16:08:40.083023Z'
  support: supports
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: plaque-historical-runner
  kind: validation
  reference: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb datasets
  locator: Actual historical00:49Z receipt and stdout/stderr independently hash-checked
  summary: Historical adapter runner failed before data retrieval due pyvenv.cfg PermissionError.
    No current invocation or execution success claimed. Fresh official catalogue/native
    source inspection is bounded fallback.
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: plaque-original-checks
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/adversary-plaque/original-checks.json
  locator: Actual three original native validations/deterministic renders and all44
    historical frozen input hashes
  summary: Original14/16/14 source input sets match. Only methane current target changed;
    originals remain truthful immutable observations at their source. Current pmoC1
    delta substantively refreshed; micronucleus/posterior targets unchanged.
  accessed_at: '2026-11-03T16:11:39.361153Z'
  support: supports
  snapshot_sha256: 46d9189c57a8d231fab21e9b149abe4b123b35ef306613be02a000d8e960bfe9
- evidence_id: plaque-methane-delta
  kind: record_content
  reference: data/structures/membrane_organelle/methane_oxidizing_organelle.yaml
  locator: Actual git diff retained in scratch from original frozen source to current
    HEAD
  summary: Only scientific delta is addition of Q603F1/pmoC1 UNREVIEWED example plus
    curation event. Existing organelle, components and graph claims unchanged; current
    entry/query/primary body checks support refreshed qualified pass.
  accessed_at: '2026-11-03T16:16:31.441887Z'
  support: supports
  snapshot_sha256: eb4e4423439a8aab54337fdac2faabf42bfa7700441eca77588397cf6f498c44
- evidence_id: plaque-native-methane_oxidizing_organelle-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/methane_oxidizing_organelle.yaml
    --verify
  locator: Actual root command receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/methane_oxidizing_organelle-uniprot-verify-receipt.json
    and exact logSHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: Actual maintained inventory has 3 protein_examples and 1 typed GENE_OR_PROTEIN
    nodes. Two reviewed and one unreviewed Bath accession; pMMO component_ref has
    native COVERED status. This is identity/symbol coverage, not membership/necessity
    or exact copper mechanism.
  accessed_at: '2026-11-03T16:07:55.743442Z'
  support: supports
  snapshot_sha256: e947e620c4704c066d3612f17e6d2083db62fb7b6da8ba04ed69c797c9e6abda
- evidence_id: plaque-native-methane_oxidizing_organelle-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/methane_oxidizing_organelle.yaml
    --causal-graphs
  locator: Actual root command receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/methane_oxidizing_organelle-uniprot-causal-receipt.json
    and exact logSHA256 8bdfb4b272fb0dd0644bc13f57c6141919be9f5f5934c3a51d7a64a22136660f
  summary: Actual maintained inventory has 3 protein_examples and 1 typed GENE_OR_PROTEIN
    nodes. Two reviewed and one unreviewed Bath accession; pMMO component_ref has
    native COVERED status. This is identity/symbol coverage, not membership/necessity
    or exact copper mechanism.
  accessed_at: '2026-11-03T16:07:56.175424Z'
  support: supports
  snapshot_sha256: a8dd755478ce279b464b52362c4a73042e95afc6aa6a6c96b933f7ef7758b507
- evidence_id: plaque-native-micronucleus-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/micronucleus.yaml
    --verify
  locator: Actual root command receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/micronucleus-uniprot-verify-receipt.json
    and exact logSHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: Actual maintained inventory has 0 protein_examples and 0 typed GENE_OR_PROTEIN
    nodes. Empty native accession/typed-node coverage does not certify all narrative
    claims.
  accessed_at: '2026-11-03T16:08:00.422332Z'
  support: supports
  snapshot_sha256: 9769d66c6b2c09fa1a1716a260df65db5f1faaeafd969b1e66d7d678d8ded475
- evidence_id: plaque-native-micronucleus-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/micronucleus.yaml
    --causal-graphs
  locator: Actual root command receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/micronucleus-uniprot-causal-receipt.json
    and exact logSHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: Actual maintained inventory has 0 protein_examples and 0 typed GENE_OR_PROTEIN
    nodes. Empty native accession/typed-node coverage does not certify all narrative
    claims.
  accessed_at: '2026-11-03T16:08:00.847336Z'
  support: supports
  snapshot_sha256: 63395aa74f7209729e5c72ae760bdfb9f605d0c629f59da7f17fab44224ffc05
- evidence_id: plaque-native-microsporidian_posterior_vacuole-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/microsporidian_posterior_vacuole.yaml
    --verify
  locator: Actual root command receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/microsporidian_posterior_vacuole-uniprot-verify-receipt.json
    and exact logSHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: Actual maintained inventory has 0 protein_examples and 0 typed GENE_OR_PROTEIN
    nodes. Empty native accession/typed-node coverage does not certify all narrative
    claims.
  accessed_at: '2026-11-03T16:08:01.264025Z'
  support: supports
  snapshot_sha256: a8210f6c35681fc1d27fc2131f8825e5e979545c4ea419ccb1c9c741fe928239
- evidence_id: plaque-native-microsporidian_posterior_vacuole-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/microsporidian_posterior_vacuole.yaml
    --causal-graphs
  locator: Actual root command receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/microsporidian_posterior_vacuole-uniprot-causal-receipt.json
    and exact logSHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: Actual maintained inventory has 0 protein_examples and 0 typed GENE_OR_PROTEIN
    nodes. Empty native accession/typed-node coverage does not certify all narrative
    claims.
  accessed_at: '2026-11-03T16:08:01.693477Z'
  support: supports
  snapshot_sha256: 918b59ff2c06284956d52ec5838bad1731ebd11948204b3f51980335a1a5e096
- evidence_id: micro-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Complete review skill/profile/config/shared output contract and native
    checklist; CURATION evidence/components/images/graph rules
  accessed_at: '2026-11-03T16:16:37.946794Z'
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
  summary: Named proteins, mitochondrial architecture, oxidative phosphorylation and
    MDC intervention/stress pathways trigger applicability assessment beyond expression-only
    claims. Review-only ownership and exact evidence scopes preserved.
  support: context_only
- evidence_id: micro-component-policy
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: CausalNode/Edge, CausalNodeTypeEnum, component roles/types and essentiality;
    CURATION family-or-class guidance
  accessed_at: '2026-11-03T16:16:37.946794Z'
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
  summary: GO cellular components may use STRUCTURE. Protein identity, constituent
    membership, associated maintenance/release machinery and formation necessity are
    distinct. The native CausalNode description also permits protein complexes under
    GENE_OR_PROTEIN, so the old type alone was not proof of a scientific error.
  support: context_only
- evidence_id: micro-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Complete graph skill and UniProt protein-examples rules; exact native verifier
    filtering at scripts/uniprot_genes.py:671-804
  accessed_at: '2026-11-03T16:16:37.946794Z'
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
  summary: Edges retain source conditions and actor scope. Native verifier only resolves
    UniProt xrefs on GENE_OR_PROTEIN nodes, so junction STRUCTURE-node P36112 requires
    the separate fresh authority check supplied here.
  support: context_only
- evidence_id: micro-record-mitochondrial_crista
  kind: record_content
  reference: data/structures/membrane_organelle/mitochondrial_crista.yaml
  locator: 'Entire current maintained record: all components, examples, functions,
    graph edges, properties/images, discussions and history'
  accessed_at: '2026-11-03T16:16:37.946794Z'
  snapshot_sha256: d7f734bbcd5e5af1c899f0c2034d2bc72656eaeb71d5861cf185613c65f4bda6
  summary: Full current target inspected. Current target equals its original frozen
    bytes.
  support: supports
- evidence_id: micro-prior-mitochondrial_crista
  kind: prior_review
  reference: reviews/structured/20261022T022238Z-mitochondrial-crista-audit/review.yaml
  locator: Original scientific assessments, evidence scopes, checks, findings/actions,
    limitations and native Markdown pair
  accessed_at: '2026-11-03T16:16:37.946794Z'
  snapshot_sha256: 8e7fcd2bf0433a33698142957cc06549648ff14c8fe8bfe047dd7cc22530f5ee
  summary: Original pass_with_limitations; 0 scientific findings. Its explicit expression-only
    adapter exclusion requires correction. Historical source reads and QC remain historical.
  support: context_only
- evidence_id: micro-native-mitochondrial_crista-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/mitochondrial_crista-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/mitochondrial_crista.yaml
    --verify; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/mitochondrial_crista-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T16:08:02.111918Z'
  snapshot_sha256: fe80d89ceaf1a180644b5b8e140161b9b1434d10bf8e0811a140ec4a8ef8381c
  summary: Exit0 on exact source head. No component protein examples and zero GENE_OR_PROTEIN
    nodes; complex STRUCTURE actors are outside the typed-node denominator. Command
    success is not a localization/assembly/necessity experiment.
  support: supports
- evidence_id: micro-native-mitochondrial_crista-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/mitochondrial_crista-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/mitochondrial_crista.yaml
    --causal-graphs; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/mitochondrial_crista-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-03T16:08:02.531702Z'
  snapshot_sha256: 6576e60b590e350ed949e92c256b68ae455346a7c4c54386168804bbc731827e
  summary: Exit0 on exact source head. No component protein examples and zero GENE_OR_PROTEIN
    nodes; complex STRUCTURE actors are outside the typed-node denominator. Command
    success is not a localization/assembly/necessity experiment.
  support: supports
- evidence_id: micro-record-mitochondrial_crista_junction
  kind: record_content
  reference: data/structures/membrane_organelle/mitochondrial_crista_junction.yaml
  locator: 'Entire current maintained record: all components, examples, functions,
    graph edges, properties/images, discussions and history'
  accessed_at: '2026-11-03T16:16:37.946794Z'
  snapshot_sha256: b994a1d51d584f4614c50fb97db455db7a6cf72b2f886da419fcbf3b77ba3adb
  summary: Full current target inspected. MICOS node retyping and appended history
    substantively reassessed.
  support: supports
- evidence_id: micro-prior-mitochondrial_crista_junction
  kind: prior_review
  reference: reviews/structured/20261022T022239Z-mitochondrial-crista-junction-audit/review.yaml
  locator: Original scientific assessments, evidence scopes, checks, findings/actions,
    limitations and native Markdown pair
  accessed_at: '2026-11-03T16:16:37.946794Z'
  snapshot_sha256: 61c6e878b42552da90908c4096400f6a3dd72adecbbdcc5dbd89e76134725a1c
  summary: Original needs_curation; 1 scientific findings. Its explicit expression-only
    adapter exclusion requires correction. Historical source reads and QC remain historical.
  support: context_only
- evidence_id: micro-native-mitochondrial_crista_junction-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/mitochondrial_crista_junction-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/mitochondrial_crista_junction.yaml
    --verify; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/mitochondrial_crista_junction-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T16:08:02.948102Z'
  snapshot_sha256: 6d09aea1751e4d4bc4707f1577a41862d32cd9ac557b97771f989957198051ad
  summary: Exit0 on exact source head. No component examples and zero GENE_OR_PROTEIN
    nodes after MICOS retyping. STRUCTURE-node P36112 is skipped by native protein
    verification and independently verified from fresh authority JSON. Command success
    is not a localization/assembly/necessity experiment.
  support: supports
- evidence_id: micro-native-mitochondrial_crista_junction-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/mitochondrial_crista_junction-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/mitochondrial_crista_junction.yaml
    --causal-graphs; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/mitochondrial_crista_junction-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-03T16:08:03.362255Z'
  snapshot_sha256: 9362e4d2a74841cf441f16340b23fea27d666c9eb1248d8d27f405a21b017b73
  summary: Exit0 on exact source head. No component examples and zero GENE_OR_PROTEIN
    nodes after MICOS retyping. STRUCTURE-node P36112 is skipped by native protein
    verification and independently verified from fresh authority JSON. Command success
    is not a localization/assembly/necessity experiment.
  support: supports
- evidence_id: micro-record-mitochondrial_derived_compartment
  kind: record_content
  reference: data/structures/membrane_organelle/mitochondrial_derived_compartment.yaml
  locator: 'Entire current maintained record: all components, examples, functions,
    graph edges, properties/images, discussions and history'
  accessed_at: '2026-11-03T16:16:37.946794Z'
  snapshot_sha256: c7a83f3db0bb05a7016b5c3991e79bd21c9a6ec4f723335fc3a1d14864d1c5c8
  summary: Full current target inspected. Current target equals its original frozen
    bytes.
  support: supports
- evidence_id: micro-prior-mitochondrial_derived_compartment
  kind: prior_review
  reference: reviews/structured/20261022T022241Z-mitochondrial-derived-compartment-audit/review.yaml
  locator: Original scientific assessments, evidence scopes, checks, findings/actions,
    limitations and native Markdown pair
  accessed_at: '2026-11-03T16:16:37.946794Z'
  snapshot_sha256: 2d4970f0670d8b53508e37cfd606b0f5089087230f7ead44afbfd546f819488e
  summary: Original needs_curation; 1 scientific findings. Its explicit expression-only
    adapter exclusion requires correction. Historical source reads and QC remain historical.
  support: context_only
- evidence_id: micro-native-mitochondrial_derived_compartment-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/mitochondrial_derived_compartment-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/mitochondrial_derived_compartment.yaml
    --verify; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/mitochondrial_derived_compartment-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T16:08:04.511659Z'
  snapshot_sha256: 6bfc1d7fa33e6e25fa3d988127be23d2a7afded177e3f1e4ab4f85ac2496dbde
  summary: Exit0 on exact source head. Three reviewed component examples TOM70/P07213,
    TOM71/P38825 and DNM1/P54861 in tax559292; zero GENE_OR_PROTEIN nodes because
    intervention/capability nodes are STATE. Command success is not a localization/assembly/necessity
    experiment.
  support: supports
- evidence_id: micro-native-mitochondrial_derived_compartment-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/mitochondrial_derived_compartment-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/mitochondrial_derived_compartment.yaml
    --causal-graphs; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/mitochondrial_derived_compartment-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-03T16:08:04.938786Z'
  snapshot_sha256: 233a0a1987a6209d07433ded34f2615df515240585560a273cc09cf9108b6ed9
  summary: Exit0 on exact source head. Three reviewed component examples TOM70/P07213,
    TOM71/P38825 and DNM1/P54861 in tax559292; zero GENE_OR_PROTEIN nodes because
    intervention/capability nodes are STATE. Command success is not a localization/assembly/necessity
    experiment.
  support: supports
- evidence_id: micro-original-pairs
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/adversary-microtubule/original-checks.json
  locator: Three actual native validate and render --content commands; byte equality
    to original Markdown
  accessed_at: '2026-11-03T16:11:50.410560Z'
  snapshot_sha256: 055341116a16fc8494c42018326b66ee0b9027c02c5252dce3074b4105c0478d
  summary: All three original pairs validate and render exactly. Original frozen target
    hashes verified from historical source; junction changed, crista/MDC unchanged.
  support: supports
- evidence_id: micro-stale-delta
  kind: record_content
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/adversary-microtubule/junction-stale.diff
  locator: Complete original frozen revision to current diff
  accessed_at: '2026-11-03T16:16:37.946794Z'
  snapshot_sha256: 99e8bd864682d8969525af4d204e2ecaf3bc85b294bd6aec9aab9a252acab614
  summary: Only appended history and micos_complex GENE_OR_PROTEIN to STRUCTURE type
    change; GO identity, P36112 member xref and maintenance edge unchanged.
  support: context_only
- evidence_id: micro-historical-2419
  kind: prior_review
  reference: https://github.com/CultureBotAI/CellStructureMech/issues/2419
  locator: Complete root-retained body/state/comments /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/historical-issue-2419.json
  accessed_at: '2026-11-03T16:16:37.946794Z'
  snapshot_sha256: d16beeb2520f5ef295df6b2543306136c094696277f2d801c96507bb4185ad1d
  summary: 'Closed issue groups five node-type corrections, including this MICOS actor.
    Historical context only: no terminal disposition of the grouped finding and no
    claim it resolves the separate modality finding.'
  support: context_only
- evidence_id: micro-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0030061,GO%3A0044284,GO%3A0005743,GO%3A0097002,GO%3A0061617,GO%3A0045259,GO%3A0042407,GO%3A0006119,GO%3A0044232,GO%3A0007007,GO%3A0043231,GO%3A0099073
  locator: All12 active term identities/definitions/synonyms and typed child relations
  accessed_at: '2026-11-03T16:10:05.860469Z'
  snapshot_sha256: afaf19281f4da56926647b0b284e0076a9e1d422a3b88f4e2aa2ce013a645464
  summary: Exact crista/junction/inner boundary/inner membrane, MICOS, ATP synthase,
    formation/organization/oxidative phosphorylation, contact site, broad organelle
    parent and distinct MDV identities agree. IMM directly lists crista/junction as
    part_of; contact site directly lists junction as is_a. No unreturned taxon constraints
    asserted.
  support: supports
- evidence_id: micro-go0030061-ancestors
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0030061/ancestors?relations=is_a
  locator: Complete exact is_a-only ancestor response
  accessed_at: '2026-11-03T16:10:38.422404Z'
  snapshot_sha256: e045717e49d54f41d35c2dac4b0af09cf50374c0e6b7792086431f1adff22257
  summary: Requested is_a ancestry confirms junction contact-site ancestry; crista
    has general cellular component ancestry. This response does not supply taxon-constraint
    data.
  support: supports
- evidence_id: micro-go0044284-ancestors
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0044284/ancestors?relations=is_a
  locator: Complete exact is_a-only ancestor response
  accessed_at: '2026-11-03T16:10:38.463003Z'
  snapshot_sha256: 286336013ac1d3544a075e6d66c4a6ecac4776dc71a511557f8958cbd5d81fc8
  summary: Requested is_a ancestry confirms junction contact-site ancestry; crista
    has general cellular component ancestry. This response does not supply taxon-constraint
    data.
  support: supports
- evidence_id: micro-tax2759
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759
  locator: Exact taxId/scientificName/rank/lineage and synonyms
  accessed_at: '2026-11-03T16:10:05.864627Z'
  snapshot_sha256: 61a68c76c70762c97e0b218568ab037d9a30c0207847247e9e055b5764a61634
  summary: Tax2759 = Eukaryota (domain). Identity only; not prevalence or equivalence
    of mutant experimental strains.
  support: supports
- evidence_id: micro-tax4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Exact taxId/scientificName/rank/lineage and synonyms
  accessed_at: '2026-11-03T16:10:06.152549Z'
  snapshot_sha256: 38f43dd1593a1d47416228ae385464f30aeb8302c3aadb45b3588d03744bc814
  summary: Tax4932 = Saccharomyces cerevisiae (species). Identity only; not prevalence
    or equivalence of mutant experimental strains.
  support: supports
- evidence_id: micro-tax559292
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Exact taxId/scientificName/rank/lineage and synonyms
  accessed_at: '2026-11-03T16:10:06.238227Z'
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
  summary: Tax559292 = Saccharomyces cerevisiae S288C (strain). Identity only; not
    prevalence or equivalence of mutant experimental strains.
  support: supports
- evidence_id: micro-uo0000017
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FUO_0000017
  locator: Exact active term label/definition
  accessed_at: '2026-11-03T16:10:06.457693Z'
  snapshot_sha256: 786ed7f6d5b07e4ec6f0a105ced79a4e4b5f025329b403c7ffc7e1d0566e2951
  summary: Micrometer is10^-6m; this independently verifies unit identity, not sample
    size or measured value.
  support: supports
- evidence_id: micro-protein-P36112
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P36112.json
  locator: entryType, primaryAccession, recommended name, genes/loci, taxon; complete
    FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments
  accessed_at: '2026-11-03T16:10:04.742639Z'
  snapshot_sha256: af85f86cc85b531190411594cc45d9566c6f54a174d135030fbd445f07c7c803
  summary: P36112 is reviewed MIC60 in tax559292; primary gene/locus and recommended
    protein name inspected. MIC60/FCJ1/AIM28/FMP13,YKR016W is one MICOS subunit, with
    experimental inner-membrane/MICOS annotations; this member xref does not redefine
    the whole complex.
  support: supports
- evidence_id: micro-protein-P07213
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P07213.json
  locator: entryType, primaryAccession, recommended name, genes/loci, taxon; complete
    FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments
  accessed_at: '2026-11-03T16:10:04.778983Z'
  snapshot_sha256: 8721213a38f896df35cbe59b2f14264e4b27b5b72786790d15fd33a408ec73d9
  summary: P07213 is reviewed TOM70 in tax559292; primary gene/locus and recommended
    protein name inspected. Native function/subunit/location annotations describe
    general mitochondrial roles; MDC membership and conditional effects require separately
    inspected primary experiments.
  support: supports
- evidence_id: micro-protein-P38825
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P38825.json
  locator: entryType, primaryAccession, recommended name, genes/loci, taxon; complete
    FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments
  accessed_at: '2026-11-03T16:10:04.794192Z'
  snapshot_sha256: a32a6bd2fc3c07c52c11b4a29307231c62789f41f99925174f9b00d5cb515437
  summary: P38825 is reviewed TOM71 in tax559292; primary gene/locus and recommended
    protein name inspected. Native function/subunit/location annotations describe
    general mitochondrial roles; MDC membership and conditional effects require separately
    inspected primary experiments.
  support: supports
- evidence_id: micro-protein-P54861
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P54861.json
  locator: entryType, primaryAccession, recommended name, genes/loci, taxon; complete
    FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments
  accessed_at: '2026-11-03T16:10:04.798889Z'
  snapshot_sha256: 05d16021893445d2fc7837966b6ebafb2f57a5355805e14bf5f99b1f08505458
  summary: P54861 is reviewed DNM1 in tax559292; primary gene/locus and recommended
    protein name inspected. Native function/subunit/location annotations describe
    general mitochondrial roles; MDC membership and conditional effects require separately
    inspected primary experiments.
  support: supports
- evidence_id: micro-family-P07213
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P07213/?page_size=200
  locator: All integrated result entries and types; count3, next=null
  accessed_at: '2026-11-03T16:10:04.822639Z'
  snapshot_sha256: ac9e5dfbbc1974b2b31bb8b979b195c62928b23f45b55ae6f7c76633ae1523b8
  summary: 'Complete bounded integrated family inspection: Tom70 IPR005687 plus TPR
    superfamily/repeat.'
  support: supports
- evidence_id: micro-family-P38825
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P38825/?page_size=200
  locator: All integrated result entries and types; count2, next=null
  accessed_at: '2026-11-03T16:10:05.067342Z'
  snapshot_sha256: cb9720ddd1465404bc5b436b526b08ab6e2225310f5aad58d2e938b255bf27e8
  summary: 'Complete bounded integrated family inspection: TPR repeat/superfamily
    only; no exact integrated Tom71 family in this endpoint.'
  support: supports
- evidence_id: micro-family-P54861
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P54861/?page_size=200
  locator: All integrated result entries and types; count9, next=null
  accessed_at: '2026-11-03T16:10:05.456913Z'
  snapshot_sha256: 881f99048b849559d3401734ab92238d7b62df2d1004a3d8c531d9d1eeef53d3
  summary: 'Complete bounded integrated family inspection: Broad Dynamin IPR022812
    plus domains/sites/superfamilies, not exact mitochondrial Dnm1 class.'
  support: supports
- evidence_id: micro-IPR005687
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005687/
  locator: Complete native accession/name/type/member databases and description
  accessed_at: '2026-11-03T16:10:05.590900Z'
  snapshot_sha256: 61d5ce706787a28482fe55aa414e5103b36e8cabe5456cccfbdaf047703a2821
  summary: Exact Tom70 family; class grounding distinct from MDC localization.
  support: supports
- evidence_id: micro-IPR022812
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR022812/
  locator: Complete native accession/name/type/member databases and description
  accessed_at: '2026-11-03T16:10:38.506108Z'
  snapshot_sha256: 467ff8e6d094e6334eddd9aed8611af71881874a13187bf02c2841fcbba6b0c0
  summary: Exact Dynamin family is broader than mitochondrial Dnm1-type class.
  support: supports
- evidence_id: micro-query-TOM70
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=100&query=%28gene_exact%3ATOM70%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete one-hit response and gene tokens
  accessed_at: '2026-11-03T16:10:38.378397Z'
  snapshot_sha256: a3686fc7de1c641fbfe919665059e83fe51cc74a2e90027670e8c140193720d4
  summary: Exactly P07213 with matching primary TOM70 returned; bounded uniqueness
    only, not membership.
  support: supports
  search_scope: UniProtKB at 2026-11-03T16:10:38.378397Z; literal query (gene_exact:TOM70)
    AND (organism_id:559292) AND (reviewed:true);format=json,size100; total1,no next-page
    Link; exact reviewed strain559292 only.
- evidence_id: micro-query-TOM71
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=100&query=%28gene_exact%3ATOM71%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete one-hit response and gene tokens
  accessed_at: '2026-11-03T16:10:38.399631Z'
  snapshot_sha256: 889c6171cb5711ab92ccabdd7f16c61b76852276351d796a14d65194d0bcf3e9
  summary: Exactly P38825 with matching primary TOM71 returned; bounded uniqueness
    only, not membership.
  support: supports
  search_scope: UniProtKB at 2026-11-03T16:10:38.399631Z; literal query (gene_exact:TOM71)
    AND (organism_id:559292) AND (reviewed:true);format=json,size100; total1,no next-page
    Link; exact reviewed strain559292 only.
- evidence_id: micro-query-DNM1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=100&query=%28gene_exact%3ADNM1%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete one-hit response and gene tokens
  accessed_at: '2026-11-03T16:10:38.407611Z'
  snapshot_sha256: b98fc986113fdba2b328d1b0af31edb44ecee40dd15264581000b11042678864
  summary: Exactly P54861 with matching primary DNM1 returned; bounded uniqueness
    only, not membership.
  support: supports
  search_scope: UniProtKB at 2026-11-03T16:10:38.407611Z; literal query (gene_exact:DNM1)
    AND (organism_id:559292) AND (reviewed:true);format=json,size100; total1,no next-page
    Link; exact reviewed strain559292 only.
- evidence_id: micro-friedman2015-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=100&query=DOI%3A%2210.7554/eLife.07739%22
  locator: Complete returned identity/publication-type/abstract fields; exact DOI
    or MED-ID query, pageSize100
  accessed_at: '2026-11-03T16:10:02.976650Z'
  snapshot_sha256: 1e582fe3389b22f988ea237a9101299a58fe1f7a7780e7bc6f663bc44cadfbd5
  summary: 'Complete bibliographic identity and returned abstracts read; DOI/title/PMID/PMC
    links retained without treating metadata as full-text evidence. '
  support: context_only
- evidence_id: micro-davies2012-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=100&query=DOI%3A%2210.1073/pnas.1204593109%22
  locator: Complete returned identity/publication-type/abstract fields; exact DOI
    or MED-ID query, pageSize100
  accessed_at: '2026-11-03T16:10:02.976775Z'
  snapshot_sha256: aeb92b1ab7ab8e5398a3ea70a894ef7e974cdc86bb11d746929e394159483c1c
  summary: 'Complete bibliographic identity and returned abstracts read; DOI/title/PMID/PMC
    links retained without treating metadata as full-text evidence. '
  support: context_only
- evidence_id: micro-paumard2002-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=100&query=DOI%3A%2210.1093/emboj/21.3.221%22
  locator: Complete returned identity/publication-type/abstract fields; exact DOI
    or MED-ID query, pageSize100
  accessed_at: '2026-11-03T16:10:02.976842Z'
  snapshot_sha256: cb4d63dc3fcfb05ec9d41eab8f72fa5a09ebf208c591d64fa7f7c70f7cbb77f0
  summary: 'Complete bibliographic identity and returned abstracts read; DOI/title/PMID/PMC
    links retained without treating metadata as full-text evidence. '
  support: context_only
- evidence_id: micro-friedman2014-meta
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=100&query=DOI%3A%2210.1038/nature12985%22
  locator: Complete returned identity/publication-type/abstract fields; exact DOI
    or MED-ID query, pageSize100
  accessed_at: '2026-11-03T16:10:02.976913Z'
  snapshot_sha256: 7b8902422f1e409eb1f77ecf02c170677308cda7665a84b0edac03beb2bfad29
  summary: Complete bibliographic identity and returned abstracts read; DOI/title/PMID/PMC
    links retained without treating metadata as full-text evidence. Secondary review,
    not a primary experiment.
  support: context_only
- evidence_id: micro-hughes2016-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=100&query=DOI%3A%2210.7554/eLife.13943%22
  locator: Complete returned identity/publication-type/abstract fields; exact DOI
    or MED-ID query, pageSize100
  accessed_at: '2026-11-03T16:10:02.976963Z'
  snapshot_sha256: c992df6c1168cc1b33fbbfca94661131396b430f73ea0d7a5647dc02b345699b
  summary: 'Complete bibliographic identity and returned abstracts read; DOI/title/PMID/PMC
    links retained without treating metadata as full-text evidence. '
  support: context_only
- evidence_id: micro-wilson2024-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=100&query=DOI%3A%2210.1083/jcb.202307035%22
  locator: Complete returned identity/publication-type/abstract fields; exact DOI
    or MED-ID query, pageSize100
  accessed_at: '2026-11-03T16:10:03.054281Z'
  snapshot_sha256: 50ec1ac5c3134b2308cebbd5596c6618b37e57f42f33ed9b6d002f6b65d18fff
  summary: 'Complete bibliographic identity and returned abstracts read; DOI/title/PMID/PMC
    links retained without treating metadata as full-text evidence. '
  support: context_only
- evidence_id: micro-cargo2024-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=100&query=DOI%3A%2210.1083/jcb.202307036%22
  locator: Complete returned identity/publication-type/abstract fields; exact DOI
    or MED-ID query, pageSize100
  accessed_at: '2026-11-03T16:10:03.613426Z'
  snapshot_sha256: b565e1c42c75093dd32aeaf669872115241ec56c2e4c9cdc033e8ed198ef8c22
  summary: 'Complete bibliographic identity and returned abstracts read; DOI/title/PMID/PMC
    links retained without treating metadata as full-text evidence. '
  support: context_only
- evidence_id: micro-ermes2020-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=100&query=DOI%3A%2210.1083/jcb.202002144%22
  locator: Complete returned identity/publication-type/abstract fields; exact DOI
    or MED-ID query, pageSize100
  accessed_at: '2026-11-03T16:10:03.618729Z'
  snapshot_sha256: 44447a6f5b10cd28700440598b563527fd18864eb4c35c179837303834c52dec
  summary: 'Complete bibliographic identity and returned abstracts read; DOI/title/PMID/PMC
    links retained without treating metadata as full-text evidence. '
  support: context_only
- evidence_id: micro-lipids2024-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=100&query=DOI%3A%2210.1083/jcb.202302069%22
  locator: Complete returned identity/publication-type/abstract fields; exact DOI
    or MED-ID query, pageSize100
  accessed_at: '2026-11-03T16:10:03.624477Z'
  snapshot_sha256: be8a148dd92561751e9c8719303cafe30a9e713aa17c2d86aa1ee30f37261801
  summary: 'Complete bibliographic identity and returned abstracts read; DOI/title/PMID/PMC
    links retained without treating metadata as full-text evidence. '
  support: context_only
- evidence_id: micro-preprintA2026-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=100&query=DOI%3A%2210.64898/2026.04.03.716366%22
  locator: Complete returned identity/publication-type/abstract fields; exact DOI
    or MED-ID query, pageSize100
  accessed_at: '2026-11-03T16:10:03.633105Z'
  snapshot_sha256: 23ad6c9dd02e80ec2e775e5f8ecb982ee4e00afc6a87964dcb1e5d7faa358c76
  summary: Complete bibliographic identity and returned abstracts read; DOI/title/PMID/PMC
    links retained without treating metadata as full-text evidence. Preprint identity/status
    retained; no version-of-record claim. The first DOI query returns a PMC stub entry
    plus the matching PPR abstract, not two independent experiments.
  support: context_only
- evidence_id: micro-preprintB2026-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=100&query=DOI%3A%2210.64898/2026.06.09.731211%22
  locator: Complete returned identity/publication-type/abstract fields; exact DOI
    or MED-ID query, pageSize100
  accessed_at: '2026-11-03T16:10:03.912242Z'
  snapshot_sha256: 7e93cbf1aa3bb0a82708d612f5324b55ba080dc627f076ba4ca97cb6f7c1ad8f
  summary: Complete bibliographic identity and returned abstracts read; DOI/title/PMID/PMC
    links retained without treating metadata as full-text evidence. Preprint identity/status
    retained; no version-of-record claim. The first DOI query returns a PMC stub entry
    plus the matching PPR abstract, not two independent experiments.
  support: context_only
- evidence_id: micro-PMID42798366
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=100&query=EXT_ID:42798366%20AND%20SRC:MED
  locator: Complete returned identity/publication-type/abstract fields; exact DOI
    or MED-ID query, pageSize100
  accessed_at: '2026-11-03T16:11:59.157637Z'
  snapshot_sha256: ae7f68b2f656e59c56b8ef0d47cec74e5b4638f1ff31eaf2212b336bbe06b53e
  summary: Complete bibliographic identity and returned abstracts read; DOI/title/PMID/PMC
    links retained without treating metadata as full-text evidence. Preprint identity/status
    retained; no version-of-record claim. The first DOI query returns a PMC stub entry
    plus the matching PPR abstract, not two independent experiments.
  support: context_only
- evidence_id: micro-PMID42327138
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=100&query=EXT_ID:42327138%20AND%20SRC:MED
  locator: Complete returned identity/publication-type/abstract fields; exact DOI
    or MED-ID query, pageSize100
  accessed_at: '2026-11-03T16:11:59.157707Z'
  snapshot_sha256: 53f66aec482e7a08786cf857caafab1cda522e948682cc948c90ab2df29e7fa6
  summary: Complete bibliographic identity and returned abstracts read; DOI/title/PMID/PMC
    links retained without treating metadata as full-text evidence. Preprint identity/status
    retained; no version-of-record claim. The first DOI query returns a PMC stub entry
    plus the matching PPR abstract, not two independent experiments.
  support: context_only
- evidence_id: micro-friedman2015-body
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4434539.1/PMC4434539.1.xml
  locator: JATS Results s2-1,s2-3 through s2-7; selected s2-2 assembly paragraphs;
    full Discussion s3; Methods s4-1,s4-3,s4-4; main embedded captions inspected where
    returned; no pixels/raw supplement analysis
  accessed_at: '2026-11-03T16:10:37.835564Z'
  snapshot_sha256: 8d1082e98a558176fbd86c80851d3467e7bf41c986f38b8dfe00810c3903a345
  summary: 'W303 deletion/reconstitution, fluorescence and fixed-section TEM support
    MICOS architecture and subcomplex organization. Direct junction immuno-EM was
    unsuccessful; adjacency to crista markers supports localization inference. Mic19
    copy-number regulation remains proposed. Methods explicitly use resin sections/TEM,
    not tomography: inherited F1 remains confirmed.'
  support: supports
- evidence_id: micro-friedman2014-body
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4075653.1/PMC4075653.1.xml
  locator: Complete S5 Internal determinants of mitochondrial division and abstract;
    other body sections not certified
  accessed_at: '2026-11-03T16:10:37.835834Z'
  snapshot_sha256: 37cb298ab74e8ff5524164dcfa6563f44b3fc8f0833ce2049dad7d11f8e6ae97
  summary: Secondary synthesis supports distinct boundary/crista regions, junctions,
    MICOS scaffold and ATP-synthase ridges. This inspected extent does not independently
    establish all reduced-anaerobic-lineage exceptions or exact GO taxon constraints.
  support: context_only
- evidence_id: micro-davies2012-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/3427116/
  locator: Genuine primary HTML sections sec2,sec4,sec5,sec9,SEC3,sec12,sec13; no
    figure pixels or supplements
  accessed_at: '2026-11-03T16:11:59.157284Z'
  snapshot_sha256: 01a1c8bad93ce91ca985fd8d71b4be254dce0458960959005040286a9908aeb5
  summary: Cryotomography in specified yeast strains resolves dimer rows on curved
    ridges; e/g/su4TM1 mutants retain monomers but lose typical lamellar cristae.
    Membrane-energy-driven assembly is a simulation/model, not a directly proven universal
    assembly sequence.
  support: supports
- evidence_id: micro-paumard2002-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/125827/
  locator: Primary HTML sec3,sec7,sec8 excluding nested modelsec9; Methods sec11,sec13,sec14;
    no pixels or raw data
  accessed_at: '2026-11-03T16:11:59.157540Z'
  snapshot_sha256: b3e67bccc076332eb2f59e634733a5f16757200fcef8e13dfb360f90c4eb0946
  summary: Yeast e/g deletion alters inner-membrane morphology while rho+ ATP-synthesis
    function can remain. TEM/immunogold and mutant controls support architecture roles;
    no universal requirement for every membrane fold inferred.
  support: supports
- evidence_id: micro-PMC4889329-body
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4889329.1/PMC4889329.1.xml
  locator: JATS Results s2-4 through s2-7, Table1 and Methods s4-4; Figure7 caption
    inspected separately; earlier aging Results not certified
  accessed_at: '2026-11-03T16:10:03.977792Z'
  snapshot_sha256: a80c297ed4982138db01f4ff62db026596d1041b5afb3a1cc170caac7007f8b3
  summary: ConcA assays distinguish formation from Dnm1-dependent release and Atg5-dependent
    vacuolar routing. Table1 includes Tom71 cargo. Tom70/Tom71 loss blocks Cox7-GFP-marked
    formation in dnm1Δ under ConcA; the record incorrectly calls this cited experiment
    rapamycin-induced. Original carrier interpretation is revised by2024 evidence.
  support: supports
- evidence_id: micro-PMC11320809-body
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC11320809.1/PMC11320809.1.xml
  locator: JATS all main Results s3-s9 and Discussion s10; Methods s12/s14; Figure1/FigureS1
    complete captions and permissions; exact figure pixels separately inspected
  accessed_at: '2026-11-03T16:10:04.237876Z'
  snapshot_sha256: 063fc310463613feaca3f38a5c38a0a00e597de6d457212dde67bc5f6310d777
  summary: Primary TEM/tomography, fluorescence and degron experiments support OMM-derived
    multilamellar domains with selective cargo and cytosolic enclosure in a subset.
    Closure, membrane number and protection are not invariant. Spherical Rap mean0.41µm,n104
    and ConcA mean0.36µm,n49 with2h/200nM or500nM scopes agree; S288C-derived strains
    and link-only CC BY-NC-SA4 after6months confirmed.
  support: supports
- evidence_id: micro-PMC11320589-body
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC11320589.1/PMC11320589.1.xml
  locator: JATS complete Results s3,s6,s7 and Discussion s9; other Results/Methods
    not claimed read
  accessed_at: '2026-11-03T16:10:04.242292Z'
  snapshot_sha256: e5dc61eb50c8064532641e980c9b966270c83777d400bef0abc0359b8a1bfad0
  summary: Functional N-terminal GFP-Oac1 is excluded; nonfunctional C-terminal fusion
    is mistargeted to OMM and enriched. OMM localization and assembly affect selectivity;
    assembled TOM-core proteins are not uniformly captured. Cargo-selection mechanism
    remains a model.
  support: supports
- evidence_id: micro-PMC7588143-body
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC7588143.1/PMC7588143.1.xml
  locator: JATS Results/Discussion s4,s5,s7 and s8 suppressor experiments (not its
    closing general summary); Methods s10/s12
  accessed_at: '2026-11-03T16:10:04.248752Z'
  snapshot_sha256: dab0ceb58ce1f9e9d04a616487ee7265b064fb4ea1d8dbf52a704194f99e4adb
  summary: ERMES/Gem1 requirements are tested conditional interventions and contact
    localization, not proof all contact machinery is constitutive MDC cargo. Tested
    psd1/ups1/crd1 perturbations did not impair formation here; retain contrast with2024
    results. VPS13/ChiMERA versus Mcp1 suppressors differ.
  support: supports
- evidence_id: micro-PMC10949074-body
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC10949074.1/PMC10949074.1.xml
  locator: JATS complete Results s5-s8; abstract separately; no raw lipidomics, figure
    pixels or supplement tables
  accessed_at: '2026-11-03T16:10:04.253527Z'
  snapshot_sha256: 4799bece666b89423ccccf0064ad0325ec557ab6d8f9cc990551bb6e9c25bf3d
  summary: CL depletion reduces MDC frequency without eliminating every small/large
    structure; PE-pathway disruption induces subsets. PSD1 rescue of mmm1Δ VPS13(D716H)
    and gem1Δ is condition-dependent/partial. Whole-cell or mitochondrial membrane
    fractions do not establish isolated-MDC lipid composition.
  support: supports
- evidence_id: micro-PMC13605720-body
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC13605720.1/PMC13605720.1.xml
  locator: Complete Full Text Availability notice only, no Results
  accessed_at: '2026-11-03T16:10:04.527844Z'
  snapshot_sha256: 3d489b473c531068a9d583e9bd01e0fa6ca41c6d0eaa168b4bec2269f59b689f
  summary: The artifact is a license/unavailability stub, not a primary scientific
    body. Actual abstract and official reviewed-preprint metadata are separately inspected.
  support: context_only
- evidence_id: micro-PMC13278180-body
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC13278180.1/PMC13278180.1.xml
  locator: Full Discussion S9 and abstract; no Results certified
  accessed_at: '2026-11-03T16:10:04.539646Z'
  snapshot_sha256: 749730eaa9957e55873552f3da7d4bddcc2c4b1df15785055dc2d60752a952a9
  summary: Acute-adaptation/Snf1/Mig1 protein-load-buffering model remains a proposal;
    Discussion explicitly says available interventions do not isolate MDC-specific
    functional contribution. No new canonical component or edge inferred.
  support: context_only
- evidence_id: micro-elife111713
  kind: authority
  reference: https://elifesciences.org/reviewed-preprints/111713v1
  locator: Official citation title/authors/DOI/date/abstract metadata and Reviewed
    Preprint version banner only
  accessed_at: '2026-11-03T16:10:38.100158Z'
  snapshot_sha256: e36dccaccc4b0c8ba048483c9179b1aec6041c74c2332b8709316fa6462d4d32
  summary: Version v1 has DOI10.7554/eLife.111713.1 and reviewed-preprint status.
    Available publisher body is not certified as read Results; historical access notes
    remain historical.
  support: context_only
- evidence_id: micro-elife112436
  kind: authority
  reference: https://elifesciences.org/reviewed-preprints/112436v1
  locator: Official citation title/authors/DOI/date/abstract metadata and Reviewed
    Preprint version banner only
  accessed_at: '2026-11-03T16:10:38.114201Z'
  snapshot_sha256: 68f5fcbaa2a5dbb7f1e395fccbf4fa963097ed5e4bce35d32e7dfe711923f2e4
  summary: Version v1 has DOI10.7554/eLife.112436.1 and reviewed-preprint status.
    Available publisher body is not certified as read Results; historical access notes
    remain historical.
  support: context_only
- evidence_id: micro-wilson2024-Fig1
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC11320809.1/JCB_202307035_Fig1.jpg
  locator: Actual complete multipanel pixels viewed; panelC axes/shape label and microscopy
    modality/scale bars; captions and license in JATS
  accessed_at: '2026-11-03T16:10:37.836021Z'
  snapshot_sha256: c1a528b26d0bfa3faf0cea25471e8d110d39469a934c1d71face8966a27d05e5
  summary: PanelC uses micrometers and limits measurement to spherical MDCs. Figure1
    mixes fluorescence, quantitative plots, thin-section TEM and immunogold, agreeing
    with OTHER modality and panel-specific scale bars. Exact historical media MD5
    bf54de482c22108855cf3cc0f37eeb8d matches; no tracked image bytes changed.
  support: supports
- evidence_id: micro-wilson2024-FigS1
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC11320809.1/JCB_202307035_FigS1.jpg
  locator: Actual complete multipanel pixels viewed; panelC axes/shape label and microscopy
    modality/scale bars; captions and license in JATS
  accessed_at: '2026-11-03T16:10:37.836059Z'
  snapshot_sha256: ec906e21b72bfb18ccc52794ada8f75a37ab4a4091b8535bdc88f42936b0bc0f
  summary: PanelC uses micrometers and limits measurement to spherical MDCs. FigureS1
    axis is µm; initial small-glyph misreading was withdrawn after independent challenge
    and own original-detail reinspection. Caption agrees mean0.36µm,n49. Exact historical
    media MD5 5b329e0ccfd3de22c02265e8439eda9f matches; no tracked image bytes changed.
  support: supports
- evidence_id: micro-image-independent-challenge
  kind: prior_review
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/adversary-plaque/mdc-figs1-axis-challenge.json
  locator: Complete independent pixel/caption/record scope challenge receipt
  accessed_at: '2026-11-03T16:16:37.946794Z'
  snapshot_sha256: b10bea7b1440db91d3a6b7d82afac375edf638d48ac8225fae2d525ae6942a34
  summary: 'Proposed axis-contradiction hypothesis rejected: actual glyph is µm and
    agrees with caption/body/record. No scientific or bundle image defect; only two
    inherited findings retained.'
  support: context_only
- evidence_id: micro-catalogue
  kind: search
  reference: https://imodulondb.org/api/datasets
  locator: Complete official catalogue array; all organism names,keys and datasets
  accessed_at: '2026-11-03T16:10:02.976364Z'
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  summary: No Saccharomyces cerevisiae,W303,BY/S288C or other named eukaryotic model-host
    match. No bacterial proxy is substituted for mitochondrial yeast pathways; no
    matched downstream search/summary applies.
  support: supports
  search_scope: Official iModulonDB /api/datasets at 2026-11-03T16:10:02.976364Z;
    complete returned20 organism rows/28 organism-dataset pairs; no query limit or
    pagination. Exact Saccharomyces/yeast/S288C/BY/W303 names and keys checked across
    full response. Bounded catalogue noncoverage only, not biological absence.
- evidence_id: micro-historical-runner
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Actual historical00:49Z command and PermissionError pyvenv.cfg
  accessed_at: '2026-11-03T00:49:00.863225Z'
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  summary: Historical optional runner unavailable, actual exit1 retained here, not
    a fresh execution. Current official catalogue fallback independently fetched/read.
  support: context_only
- evidence_id: check-qc
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/qc.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T16:13:08.464142Z'
  support: supports
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  snapshot_sha256: 32fafed5eed5e74b9a24f5a39bf9d7f69868b95599c4ef89e9aec9cd89b03e1d
- evidence_id: check-labels
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/labels.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T16:09:12.301809Z'
  support: supports
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  snapshot_sha256: 6cdfb05df9a27194f05a5fd7f851783f817ac1523ca0bbfa54fe0e0d18775905
- evidence_id: check-trait-links
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/trait-links.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T16:08:48.033566Z'
  support: supports
  summary: Native TraitMech link check passed.
  snapshot_sha256: 8b336cdefbbd3daf6da8787990efdbe346c95e2c8361d50b7eb68a18f2d5a44a
- evidence_id: check-vendored
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/vendored.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T16:08:46.414040Z'
  support: supports
  summary: Pinned governed files match; native vendored check passed.
  snapshot_sha256: b1f169d103aaefa930745468bcca171e5867b9cc49e4e74311e458097e3252a6
- evidence_id: check-curies
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/curies.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T16:07:57.426663Z'
  support: supports
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  snapshot_sha256: bc12b1285f5747707643f7a98e03dbb3a6c88fb062ad49f99db9cb42ececf3d2
- evidence_id: focused
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/focused-results.json
  locator: All twenty actual target schema/strict command outputs
  accessed_at: '2026-11-03T16:17:55Z'
  support: supports
  summary: Ten schema and ten strict commands returned exit zero.
  snapshot_sha256: 45fcba986af042c167281de1916eab82f31e609fcf61b9c0f8496c75d10424bc
- evidence_id: supplemental-pmid
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2369/pmid-chunks-receipt.json
  locator: Complete native-report PMID set checked with unchanged resolver in batches
    of at most fifty
  accessed_at: '2026-11-03T16:09:50.617754Z'
  support: supports
  summary: 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers
    remain unverified.
  snapshot_sha256: 42ae79a3f9c4c23f92495c7fdd18b8a2d48f1b783d15cce02cfaa72f9a33d57d
- evidence_id: historical-adapter-runner-availability
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical runner invocation receipt, exact SHA256 reverified during PR2369
    synthesis
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  summary: Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS
    PermissionError reading the configured runner pyvenv.cfg. This is a retained historical
    availability observation, not a fresh attempt or a scientific validation failure.
    Native policy permits inspected source-catalogue fallback.
assessments:
- assessment_id: septin-maurer_s_cleft-schema
  area: schema
  topic: Frozen original schema/render and current input comparison
  outcome: supported
  summary: Original validation/render and historical hash checks pass. Stale target
    gains one unreviewed protein example and curation history; both new identity and
    scientific membership context are reassessed. Schema validity is not scientific/source
    certification.
  target_ids:
  - GO:0020036
  evidence_ids:
  - septin-record-maurer_s_cleft
  - septin-original-validation-maurer_s_cleft
- assessment_id: septin-maurer_s_cleft-inventory
  area: provenance
  topic: Actual native protein inventory and command coverage
  outcome: supported
  summary: Three UNREVIEWED example occurrences and three distinct accessions Q6V0W9,Q8I2G1,Q9NFF5;
    two COVERED GENE_OR_PROTEIN nodes. Q6V0W9 is a fragment. Native identity/coverage
    does not demonstrate accession-specific membership, complete composition, causality
    or formation necessity.
  target_ids:
  - GO:0020036
  evidence_ids:
  - septin-record-maurer_s_cleft
  - septin-native-maurer_s_cleft-verify
  - septin-native-maurer_s_cleft-causal
- assessment_id: septin-maurer_s_cleft-nonasserted
  area: scope
  topic: Images, physical measurements, traits and snippets
  outcome: not_applicable
  summary: No maintained image, numeric physical measurement, associated trait or
    verbatim snippet is asserted. Source captions are distinguished from uninspected
    figure pixels; no image licence or raw-data reanalysis is certified.
  target_ids:
  - GO:0020036
  evidence_ids:
  - septin-record-maurer_s_cleft
- assessment_id: septin-maurer_s_cleft-history
  area: provenance
  topic: Status and bounded historical lineage
  outcome: supported
  summary: PROPOSED status and current history are retained. Original occurrences
    are linked only to their maintained target; no neighbor/group/category issue is
    declared resolved.
  target_ids:
  - GO:0020036
  evidence_ids:
  - septin-record-maurer_s_cleft
  - septin-original-maurer_s_cleft
- assessment_id: septin-microneme-schema
  area: schema
  topic: Frozen original schema/render and current input comparison
  outcome: supported
  summary: Original validation/render and historical hash checks pass. Stale target
    gains one unreviewed protein example and curation history; both new identity and
    scientific membership context are reassessed. Schema validity is not scientific/source
    certification.
  target_ids:
  - GO:0020009
  evidence_ids:
  - septin-record-microneme
  - septin-original-validation-microneme
- assessment_id: septin-microneme-inventory
  area: provenance
  topic: Actual native protein inventory and command coverage
  outcome: supported
  summary: 'Five protein-example occurrences but four distinct accessions: MIC2/S8F9G8
    occurs under both adhesin cohort and MIC2-M2AP complex. Two REVIEWED occurrences
    O00834/B6KAM0 and three UNREVIEWED occurrences S8F9G8 twice/S8GDJ1 once; two COVERED
    GENE_OR_PROTEIN nodes. Correct identity and symbol coverage do not prove complete
    complex stoichiometry, localization topology or causal necessity.'
  target_ids:
  - GO:0020009
  evidence_ids:
  - septin-record-microneme
  - septin-native-microneme-verify
  - septin-native-microneme-causal
- assessment_id: septin-microneme-nonasserted
  area: scope
  topic: Images, physical measurements, traits and snippets
  outcome: not_applicable
  summary: No maintained image, numeric physical measurement, associated trait or
    verbatim snippet is asserted. Source captions are distinguished from uninspected
    figure pixels; no image licence or raw-data reanalysis is certified.
  target_ids:
  - GO:0020009
  evidence_ids:
  - septin-record-microneme
- assessment_id: septin-microneme-history
  area: provenance
  topic: Status and bounded historical lineage
  outcome: supported
  summary: PROPOSED status and current history are retained. Original occurrences
    are linked only to their maintained target; no neighbor/group/category issue is
    declared resolved.
  target_ids:
  - GO:0020009
  evidence_ids:
  - septin-record-microneme
  - septin-original-microneme
- assessment_id: septin-microneme_lumen-schema
  area: schema
  topic: Frozen original schema/render and current input comparison
  outcome: supported
  summary: Original validation/render and historical hash checks pass. Current target
    is byte-identical to original input, with scientific claims reassessed. Schema
    validity is not scientific/source certification.
  target_ids:
  - GO:0034494
  evidence_ids:
  - septin-record-microneme_lumen
  - septin-original-validation-microneme_lumen
- assessment_id: septin-microneme_lumen-inventory
  area: provenance
  topic: Actual native protein inventory and command coverage
  outcome: supported
  summary: Zero protein examples and zero typed GENE_OR_PROTEIN nodes; no represented
    UniProtKB graph xrefs. Exit0 validates an empty identifier inventory, not the
    complete secretion/pathway narrative.
  target_ids:
  - GO:0034494
  evidence_ids:
  - septin-record-microneme_lumen
  - septin-native-microneme_lumen-verify
  - septin-native-microneme_lumen-causal
- assessment_id: septin-microneme_lumen-nonasserted
  area: scope
  topic: Images, physical measurements, traits and snippets
  outcome: not_applicable
  summary: No maintained image, numeric physical measurement, associated trait or
    verbatim snippet is asserted. Source captions are distinguished from uninspected
    figure pixels; no image licence or raw-data reanalysis is certified.
  target_ids:
  - GO:0034494
  evidence_ids:
  - septin-record-microneme_lumen
- assessment_id: septin-microneme_lumen-history
  area: provenance
  topic: Status and bounded historical lineage
  outcome: supported
  summary: PROPOSED status and current history are retained. Original occurrences
    are linked only to their maintained target; no neighbor/group/category issue is
    declared resolved.
  target_ids:
  - GO:0034494
  evidence_ids:
  - septin-record-microneme_lumen
  - septin-original-microneme_lumen
- assessment_id: septin-microneme_membrane-schema
  area: schema
  topic: Frozen original schema/render and current input comparison
  outcome: supported
  summary: Original validation/render and historical hash checks pass. Current target
    is byte-identical to original input, with scientific claims reassessed. Schema
    validity is not scientific/source certification.
  target_ids:
  - GO:0033163
  evidence_ids:
  - septin-record-microneme_membrane
  - septin-original-validation-microneme_membrane
- assessment_id: septin-microneme_membrane-inventory
  area: provenance
  topic: Actual native protein inventory and command coverage
  outcome: supported
  summary: Zero protein examples and zero typed GENE_OR_PROTEIN nodes; no represented
    UniProtKB graph xrefs. Exit0 validates an empty identifier inventory, not the
    complete exocytosis/pathway narrative.
  target_ids:
  - GO:0033163
  evidence_ids:
  - septin-record-microneme_membrane
  - septin-native-microneme_membrane-verify
  - septin-native-microneme_membrane-causal
- assessment_id: septin-microneme_membrane-nonasserted
  area: scope
  topic: Images, physical measurements, traits and snippets
  outcome: not_applicable
  summary: No maintained image, numeric physical measurement, associated trait or
    verbatim snippet is asserted. Source captions are distinguished from uninspected
    figure pixels; no image licence or raw-data reanalysis is certified.
  target_ids:
  - GO:0033163
  evidence_ids:
  - septin-record-microneme_membrane
- assessment_id: septin-microneme_membrane-history
  area: provenance
  topic: Status and bounded historical lineage
  outcome: supported
  summary: PROPOSED status and current history are retained. Original occurrences
    are linked only to their maintained target; no neighbor/group/category issue is
    declared resolved.
  target_ids:
  - GO:0033163
  evidence_ids:
  - septin-record-microneme_membrane
  - septin-original-microneme_membrane
- assessment_id: septin-maurer_s_cleft-adapter
  area: scope
  topic: Full molecular/pathway narrative applicability
  outcome: supported
  summary: This record asserts PfEMP1 trafficking and named SBP1/MAHRP1/REX residents,
    so expression-only exclusion is unsupported. Current official catalogue has no
    matching parasite host; downstream gene/module queries are therefore not applicable
    within this catalogue, not biologically refuted. Runner receipt is historical.
  target_ids:
  - GO:0020036
  evidence_ids:
  - septin-record-maurer_s_cleft
  - septin-review-policy
  - septin-catalogue
  - septin-adapter-runner-historical
- assessment_id: septin-microneme-adapter
  area: scope
  topic: Full molecular/pathway narrative applicability
  outcome: supported
  summary: This record asserts adhesin-complex trafficking, regulated exocytosis and
    invasion, so expression-only exclusion is unsupported. Current official catalogue
    has no matching parasite host; downstream gene/module queries are therefore not
    applicable within this catalogue, not biologically refuted. Runner receipt is
    historical.
  target_ids:
  - GO:0020009
  evidence_ids:
  - septin-record-microneme
  - septin-review-policy
  - septin-catalogue
  - septin-adapter-runner-historical
- assessment_id: septin-microneme_lumen-adapter
  area: scope
  topic: Full molecular/pathway narrative applicability
  outcome: supported
  summary: This record asserts secretory cargo storage and regulated release, so expression-only
    exclusion is unsupported. Current official catalogue has no matching parasite
    host; downstream gene/module queries are therefore not applicable within this
    catalogue, not biologically refuted. Runner receipt is historical.
  target_ids:
  - GO:0034494
  evidence_ids:
  - septin-record-microneme_lumen
  - septin-review-policy
  - septin-catalogue
  - septin-adapter-runner-historical
- assessment_id: septin-microneme_membrane-adapter
  area: scope
  topic: Full molecular/pathway narrative applicability
  outcome: supported
  summary: This record asserts regulated membrane fusion/exocytosis and cargo release,
    so expression-only exclusion is unsupported. Current official catalogue has no
    matching parasite host; downstream gene/module queries are therefore not applicable
    within this catalogue, not biologically refuted. Runner receipt is historical.
  target_ids:
  - GO:0033163
  evidence_ids:
  - septin-record-microneme_membrane
  - septin-review-policy
  - septin-catalogue
  - septin-adapter-runner-historical
- assessment_id: septin-maurer_s_cleft-identity
  area: identity
  topic: Exact Maurer cleft and host/parasite boundary
  outcome: supported
  summary: GO0020036 denotes parasite-derived membranous clefts in infected erythrocyte
    cytoplasm. The parasite is the canonical organism; host red-cell compartment is
    localization context. Broader membrane-bounded-organelle parent is biologically
    compatible but not a claimed native GO is_a edge in this response.
  target_ids:
  - GO:0020036
  evidence_ids:
  - septin-record-maurer_s_cleft
  - septin-go
  - septin-ancestors-0020036
  - septin-cooke2006-bioc
- assessment_id: septin-maurer_s_cleft-stale
  area: grounding
  topic: New REX1 accession and current experimental scope
  outcome: supported
  summary: New Q8I2G1 is UNREVIEWED REX1, taxon36329 and ORF PF3D7_0935900. It lacks
    a formal primary geneName field, so no such authority-field claim is certified.
    Correct locus/protein identity plus Cooke Rex cleft-marker context supports the
    representative example; no exact knock-out/necessity result follows from this
    accession.
  target_ids:
  - GO:0020036
  evidence_ids:
  - septin-record-maurer_s_cleft
  - septin-protein-Q8I2G1
  - septin-tax36329
  - septin-cooke2006-bioc
- assessment_id: septin-maurer_s_cleft-composition
  area: grounding
  topic: Collective bilayer and heterogeneous resident class
  outcome: supported
  summary: Label-only LIPID row denotes collective bilayer material without an exact
    whole-GO chemical identity. Resident PROTEIN class explicitly groups proteins
    without claiming one family/complex; UNKNOWN essentiality and separate SBP1 row
    are compatible with native class policy.
  target_ids:
  - GO:0020036
  evidence_ids:
  - septin-record-maurer_s_cleft
  - septin-curation-policy
  - septin-schema-policy
  - septin-protein-policy
  - septin-cooke2006-bioc
- assessment_id: septin-maurer_s_cleft-family
  area: grounding
  topic: Named examples and unresolved exact family grounding
  outcome: unknown
  summary: MAHRP1 fragment and SBP1 unreviewed entries are identity examples, not
    complete experimental constructs. A single-accession204 and mismatched automatic
    InterPro family hit do not certify no family or justify a forced grounding; retain
    existing bounded family TODO.
  target_ids:
  - GO:0020036
  evidence_ids:
  - septin-record-maurer_s_cleft
  - septin-protein-Q6V0W9
  - septin-protein-Q9NFF5
  - septin-ipr-mahrp1
  - septin-ipr-sbp1
  - septin-blisnick2000-meta
  - septin-cooke2006-bioc
- assessment_id: septin-maurer_s_cleft-scope
  area: scope
  topic: Species, host and qualitative stage prevalence
  outcome: supported
  summary: Pf5833 and isolate3D7 identities verify. Cooke uses3D7-infected human erythrocytes;
    broad COMMON asexual-stage wording remains qualitative. Rodent antibody conservation
    observations are not substituted for exact Pf genetics or all-species universal
    morphology.
  target_ids:
  - GO:0020036
  evidence_ids:
  - septin-record-maurer_s_cleft
  - septin-tax5833
  - septin-tax36329
  - septin-cooke2006-bioc
  - septin-blisnick2000-meta
  - septin-lanzer2006-meta
- assessment_id: septin-maurer_s_cleft-functions
  area: evidence
  topic: Trafficking versus precise molecular mechanism
  outcome: supported
  summary: Cooke SBP1 loss retains PfEMP1 at clefts and complementation restores surface
    display/adhesion; Spycher MAHRP1 genetic effects are a distinct intervention.
    Neither guarantees direct SBP1-PfEMP1 binding, a complete transport pathway, or
    absence of clefts on protein loss.
  target_ids:
  - GO:0020036
  evidence_ids:
  - septin-record-maurer_s_cleft
  - septin-cooke2006-bioc
  - septin-spycher2008-meta
  - septin-blisnick2000-meta
- assessment_id: septin-maurer_s_cleft-graph
  area: graph
  topic: Five descriptive trafficking/localization edges
  outcome: supported
  summary: All five NONMECHANISTIC edges retain membrane/cohort containment and source-supported
    SBP1 trafficking/host surface-display context; direct binding, precise transport
    chemistry and organelle-formation necessity are not asserted. Component_refs resolve
    and descriptive graph scope stays bounded.
  target_ids:
  - GO:0020036
  evidence_ids:
  - septin-record-maurer_s_cleft
  - septin-graph-policy
  - septin-cooke2006-bioc
  - septin-spycher2008-meta
- assessment_id: septin-maurer_s_cleft-necessity
  area: evidence
  topic: Bilayer constitution and protein necessity
  outcome: unknown
  summary: Collective membrane material is constitutional to the membranous structure;
    no individual lipid-species removal experiment is implied. SBP1 knockout clefts
    persist and resident protein UNKNOWN essentiality is conservative; transport necessity
    is not identical to structure-formation necessity.
  target_ids:
  - GO:0020036
  evidence_ids:
  - septin-record-maurer_s_cleft
  - septin-curation-policy
  - septin-cooke2006-bioc
- assessment_id: septin-maurer_s_cleft-canonical
  area: provenance
  topic: Canonical genetic-study citation placement
  outcome: concern
  summary: Canonical note combines SBP1 and MAHRP1 genetic studies under sole Cooke2006
    reference. Cooke is SBP1; Spycher2008 is MAHRP1. Preserve inherited F1 and scope-corrective
    action without changing the underlying supported biological claims.
  target_ids:
  - GO:0020036
  evidence_ids:
  - septin-record-maurer_s_cleft
  - septin-original-maurer_s_cleft
  - septin-cooke2006-bioc
  - septin-spycher2008-meta
- assessment_id: septin-microneme-identity
  area: identity
  topic: Exact whole microneme, boundaries and synonyms
  outcome: supported
  summary: GO0020009/related sarconeme synonym, GO0043231 ancestry, apical-complex
    parthood and distinct membrane/lumen child identities agree. Whole organelle is
    not identical to its molecular lipid material or lumen.
  target_ids:
  - GO:0020009
  evidence_ids:
  - septin-record-microneme
  - septin-go
  - septin-ancestors-0020009
  - septin-record-microneme_lumen
  - septin-record-microneme_membrane
- assessment_id: septin-microneme-stale
  area: grounding
  topic: New M2AP accession and separate RH experiment
  outcome: supported
  summary: S8GDJ1 is UNREVIEWED ME49 M2AP with ORF TGME49_214940 and matching protein
    name; no formal primary geneName field is certified. Native identity and automatic
    signal peptide do not establish causality. Primary Huynh abstract/body independently
    support soluble M2AP partnering with transmembrane MIC2 in RH-derived experiments;
    ME49 is a representative, not the exact experimental construct.
  target_ids:
  - GO:0020009
  evidence_ids:
  - septin-record-microneme
  - septin-protein-S8GDJ1
  - septin-tax508771
  - septin-huynh2003-meta
  - septin-huynh2006-bioc
- assessment_id: septin-microneme-material
  area: grounding
  topic: Whole-membrane GO identity on a LIPID constituent
  outcome: concern
  summary: LIPID component microneme_membrane currently uses whole membrane GO0033163.
    Preserve whole-membrane has_part and structural node, but separate molecular material
    identity from the cellular boundary; inherited major F1 remains. No new lipid
    species or removal requirement is invented.
  target_ids:
  - GO:0020009
  evidence_ids:
  - septin-record-microneme
  - septin-go
  - septin-schema-policy
  - septin-curation-policy
  - septin-record-microneme_membrane
- assessment_id: septin-microneme-cohort
  area: grounding
  topic: Heterogeneous adhesins and legitimate complex node type
  outcome: supported
  summary: MIC1/MIC2/AMA1 is explicitly heterogeneous, which native family-or-class
    policy allows. MIC2-M2AP is a named PROTEIN_COMPLEX component. Exact CausalNode
    schema lines845–846 explicitly permits protein complexes within GENE_OR_PROTEIN;
    this node type is not a confirmed defect and is not automatically retyped STRUCTURE.
    Neither a universal family nor exact complex stoichiometry is inferred.
  target_ids:
  - GO:0020009
  evidence_ids:
  - septin-record-microneme
  - septin-schema-policy
  - septin-curation-policy
  - septin-protein-policy
  - septin-huynh2006-bioc
  - septin-huynh2003-meta
- assessment_id: septin-microneme-examples
  area: grounding
  topic: Representative identities and evidence-code limits
  outcome: supported
  summary: MIC1/O00834 and AMA1/B6KAM0 are reviewed; MIC2/S8F9G8 and M2AP/S8GDJ1 unreviewed.
    Current MIC1/AMA1 source-linked location/shedding evidence is checked against
    complete primary abstracts, while predicted topology and automatic annotations
    stay distinct. Different species/VEG/ME49 representatives are not silently equated
    with RH experimental constructs.
  target_ids:
  - GO:0020009
  evidence_ids:
  - septin-record-microneme
  - septin-protein-O00834
  - septin-protein-B6KAM0
  - septin-protein-S8F9G8
  - septin-protein-S8GDJ1
  - septin-pmid-meta
  - septin-gene-MIC1
  - septin-gene-AMA1
- assessment_id: septin-microneme-taxon
  area: scope
  topic: Phylum/subset and exact strain scopes
  outcome: supported
  summary: Eukaryota RARE and Apicomplexa COMMON are explicitly qualitative and stage/lineage-dependent.
    Tg species/VEG/ME49 identities verify; Huynh2006 conditional MIC2 work is RH-derived
    with HFF culture. No universal microneme composition or all-stage invasion role
    follows.
  target_ids:
  - GO:0020009
  evidence_ids:
  - septin-record-microneme
  - septin-tax2759
  - septin-tax5794
  - septin-tax5811
  - septin-tax432359
  - septin-tax508771
  - septin-dubois2019-pdf
  - septin-huynh2006-bioc
- assessment_id: septin-microneme-function
  area: evidence
  topic: Secretion, adhesion and invasion evidence
  outcome: supported
  summary: 1997 complete primary abstract supports ordered secretion; Huynh primary
    abstract/body support MIC2-M2AP trafficking and reduced attachment/invasion; Brown
    complete primary abstract supports in vitro PKG/cGMP-dependent secretion at its
    actual stimulus context. Residual invasion, distinct gliding modes and retained
    other microneme cargos prevent absolute formation-necessity claims.
  target_ids:
  - GO:0020009
  evidence_ids:
  - septin-record-microneme
  - septin-pmid-meta
  - septin-huynh2003-meta
  - septin-huynh2006-bioc
  - septin-brown2016-meta
- assessment_id: septin-microneme-topology
  area: graph
  topic: Two over-specific whole-cargo lumen endpoints
  outcome: concern
  summary: MIC2 and AMA1 span a membrane and have cytoplasmic portions; soluble M2AP/adhesive
    domains do not make the full complex/cohort entirely luminal. The two whole-entity
    lumen edges retain inherited F2; descriptions already support whole-organelle
    localization. Narrow endpoint or explicitly represent portions without inventing
    detailed orientation for every member.
  target_ids:
  - GO:0020009
  evidence_ids:
  - septin-record-microneme
  - septin-huynh2006-bioc
  - septin-protein-B6KAM0
  - septin-protein-O00834
  - septin-pmid-meta
  - septin-dubois2019-pdf
- assessment_id: septin-microneme-graph-other
  area: graph
  topic: Remaining six mechanistic graph edges
  outcome: supported
  summary: Correct whole-organelle membrane/lumen parthood and PKG/exocytosis/cargo-release/complex-invasion/cohort-support
    relations match stated source scopes. The two lumen endpoints are separately flagged;
    no absolute requirement or entire fusion machinery is certified by simplified
    aggregate edges.
  target_ids:
  - GO:0020009
  evidence_ids:
  - septin-record-microneme
  - septin-graph-policy
  - septin-go
  - septin-pmid-meta
  - septin-huynh2003-meta
  - septin-huynh2006-bioc
  - septin-brown2016-meta
  - septin-dubois2019-pdf
- assessment_id: septin-microneme-necessity
  area: evidence
  topic: Constitutional membrane and protein formation requirements
  outcome: unknown
  summary: Bilayer material is constitutional but its present whole-GO chemical grounding
    remains defective. MIC2/M2AP intervention changes trafficking/invasion, while
    other cargos persist and residual invasion remains; UNKNOWN protein essentiality
    is not converted into universal organelle-formation necessity.
  target_ids:
  - GO:0020009
  evidence_ids:
  - septin-record-microneme
  - septin-huynh2003-meta
  - septin-huynh2006-bioc
  - septin-curation-policy
- assessment_id: septin-microneme-canonical
  area: provenance
  topic: Multiple study clauses under a 1997 source
  outcome: concern
  summary: Canonical PMID9208224 supports sequential secretion, not later MIC2-M2AP
    genetic work and PKG experiments. Those sources are present elsewhere and verified
    at explicit tiers; retain inherited F3, scope-correct each clause, and preserve
    Tg/RH context.
  target_ids:
  - GO:0020009
  evidence_ids:
  - septin-record-microneme
  - septin-original-microneme
  - septin-pmid-meta
  - septin-huynh2003-meta
  - septin-huynh2006-meta
  - septin-brown2016-meta
- assessment_id: septin-microneme-completeness
  area: completeness
  topic: Family TODO and bounded complex census
  outcome: unknown
  summary: MIC1/AMA1 domain/family xrefs do not ground the entire heterogeneous cohort;
    M2AP beta-domain does not identify a whole complex. Existing TODO is retained
    without a guessed identifier. Inventory is representative, not a complete all-stage
    complex or microneme proteome.
  target_ids:
  - GO:0020009
  evidence_ids:
  - septin-record-microneme
  - septin-protein-O00834
  - septin-protein-B6KAM0
  - septin-protein-S8F9G8
  - septin-protein-S8GDJ1
  - septin-dubois2019-pdf
  - septin-curation-policy
- assessment_id: septin-microneme_lumen-identity
  area: identity
  topic: Exact compartment identity and boundary topology
  outcome: supported
  summary: GO0034494 is the enclosed volume, with organelle-lumen is_a ancestry and
    whole-microneme parthood; membrane remains a boundary rather than a lumen constituent.
  target_ids:
  - GO:0034494
  evidence_ids:
  - septin-record-microneme_lumen
  - septin-go
  - septin-ancestors-0034494
  - septin-record-microneme
- assessment_id: septin-microneme_lumen-scope
  area: scope
  topic: Taxonomic and experimental scope
  outcome: supported
  summary: Apicomplexa COMMON is qualitative and stage/lineage-qualified; canonical
    T.gondii sequential secretion is supported by the complete1997 primary abstract.
    Review synthesis supplies broad topology/cargo context without asserting universal
    composition or exact all-strain mechanism.
  target_ids:
  - GO:0034494
  evidence_ids:
  - septin-record-microneme_lumen
  - septin-tax5794
  - septin-tax5811
  - septin-pmid-meta
  - septin-dubois2019-pdf
  - septin-carruthers2008-meta
- assessment_id: septin-microneme_lumen-function
  area: evidence
  topic: Storage/release and exocytosis scope
  outcome: supported
  summary: Temporary lumen cargo storage/release is supported at soluble cargo/adhesive-domain
    scope. This generic statement does not itself place an entire transmembrane complex
    in the lumen and does not inherit the separate whole-record F2.
  target_ids:
  - GO:0034494
  evidence_ids:
  - septin-record-microneme_lumen
  - septin-pmid-meta
  - septin-dubois2019-pdf
  - septin-huynh2006-bioc
- assessment_id: septin-microneme_lumen-composition
  area: grounding
  topic: Sparse contents/material scope
  outcome: supported
  summary: No molecular components are asserted. The internal volume is not grounded
    to a whole membrane or a specific protein; no undisclosed complete cargo inventory
    is certified.
  target_ids:
  - GO:0034494
  evidence_ids:
  - septin-record-microneme_lumen
  - septin-curation-policy
  - septin-schema-policy
  - septin-go
- assessment_id: septin-microneme_lumen-graph
  area: graph
  topic: Every descriptive boundary graph edge
  outcome: supported
  summary: Two NONMECHANISTIC edges correctly express lumen parthood and membrane
    enclosure; no whole-complex luminal topology is asserted.
  target_ids:
  - GO:0034494
  evidence_ids:
  - septin-record-microneme_lumen
  - septin-graph-policy
  - septin-go
  - septin-dubois2019-pdf
- assessment_id: septin-microneme_lumen-completeness
  area: completeness
  topic: Existing discussion and intentionally sparse inventory
  outcome: supported
  summary: Existing boundary/material discussion is interpreted at its actual target
    only. Sparse molecular inventory, empty native typed-node checks and body-access
    limits remain explicit; no other maintained-record/category issue is disposed
    by inference.
  target_ids:
  - GO:0034494
  evidence_ids:
  - septin-record-microneme_lumen
  - septin-original-microneme_lumen
  - septin-native-microneme_lumen-causal
  - septin-curation-policy
- assessment_id: septin-microneme_membrane-identity
  area: identity
  topic: Exact compartment identity and boundary topology
  outcome: supported
  summary: GO0033163 is the complete surrounding bilayer, with organelle-membrane
    is_a ancestry and whole-microneme parthood; the lumen and organelle stay distinct.
  target_ids:
  - GO:0033163
  evidence_ids:
  - septin-record-microneme_membrane
  - septin-go
  - septin-ancestors-0033163
  - septin-record-microneme
- assessment_id: septin-microneme_membrane-scope
  area: scope
  topic: Taxonomic and experimental scope
  outcome: supported
  summary: Apicomplexa COMMON is qualitative and stage/lineage-qualified; canonical
    T.gondii sequential secretion is supported by the complete1997 primary abstract.
    Review synthesis supplies broad topology/cargo context without asserting universal
    composition or exact all-strain mechanism.
  target_ids:
  - GO:0033163
  evidence_ids:
  - septin-record-microneme_membrane
  - septin-tax5794
  - septin-tax5811
  - septin-pmid-meta
  - septin-dubois2019-pdf
  - septin-carruthers2008-meta
- assessment_id: septin-microneme_membrane-function
  area: evidence
  topic: Storage/release and exocytosis scope
  outcome: supported
  summary: Membrane boundary and regulated release context are supported; the graph
    attributes exocytosis support to the whole microneme, not an isolated bilayer
    as sufficient molecular machinery. No exact fusion-protein census or universal
    pathway is asserted.
  target_ids:
  - GO:0033163
  evidence_ids:
  - septin-record-microneme_membrane
  - septin-pmid-meta
  - septin-dubois2019-pdf
  - septin-huynh2006-bioc
- assessment_id: septin-microneme_membrane-composition
  area: grounding
  topic: Sparse contents/material scope
  outcome: supported
  summary: The LIPID row is reviewed-label-only collective bilayer material, without
    the whole-GO chemical grounding error in the whole record. ESSENTIAL is constitutional
    material scope, not tested necessity of a specific lipid species; existing exact-lipid
    TODO remains open.
  target_ids:
  - GO:0033163
  evidence_ids:
  - septin-record-microneme_membrane
  - septin-curation-policy
  - septin-schema-policy
  - septin-go
- assessment_id: septin-microneme_membrane-graph
  area: graph
  topic: Every descriptive boundary graph edge
  outcome: supported
  summary: Three NONMECHANISTIC edges retain membrane parthood, lumen enclosure and
    whole-microneme exocytosis support. Structural-to-material component_ref is bounded
    by its collective material label; no molecular-equivalence or independent-bilayer
    causal sufficiency is asserted.
  target_ids:
  - GO:0033163
  evidence_ids:
  - septin-record-microneme_membrane
  - septin-graph-policy
  - septin-go
  - septin-dubois2019-pdf
- assessment_id: septin-microneme_membrane-completeness
  area: completeness
  topic: Existing discussion and intentionally sparse inventory
  outcome: supported
  summary: Existing boundary/material discussion is interpreted at its actual target
    only. Sparse molecular inventory, empty native typed-node checks and body-access
    limits remain explicit; no other maintained-record/category issue is disposed
    by inference.
  target_ids:
  - GO:0033163
  evidence_ids:
  - septin-record-microneme_membrane
  - septin-original-microneme_membrane
  - septin-native-microneme_membrane-causal
  - septin-curation-policy
- assessment_id: septin-maurer_s_cleft-verdict
  area: completeness
  topic: Current scoped scientific verdict
  outcome: concern
  summary: 'needs_curation: 1 exact inherited findings remain, with no additional
    confirmed scientific finding. Stale accession additions are substantively refreshed
    without changing records.'
  target_ids:
  - GO:0020036
  evidence_ids:
  - septin-record-maurer_s_cleft
  - septin-original-maurer_s_cleft
  - septin-cooke2006-bioc
  - septin-spycher2008-meta
- assessment_id: septin-microneme-verdict
  area: completeness
  topic: Current scoped scientific verdict
  outcome: concern
  summary: 'needs_curation: 3 exact inherited findings remain, with no additional
    confirmed scientific finding. Stale accession additions are substantively refreshed
    without changing records.'
  target_ids:
  - GO:0020009
  evidence_ids:
  - septin-record-microneme
  - septin-original-microneme
  - septin-go
  - septin-huynh2006-bioc
  - septin-pmid-meta
  - septin-dubois2019-pdf
- assessment_id: septin-microneme_lumen-verdict
  area: completeness
  topic: Current scoped scientific verdict
  outcome: supported
  summary: 'pass_with_limitations: stated source tiers support current bounded identity/topology/function.
    Empty protein inventory and access/necessity limits prevent an unqualified pass;
    no confirmed curation finding.'
  target_ids:
  - GO:0034494
  evidence_ids:
  - septin-record-microneme_lumen
  - septin-original-microneme_lumen
  - septin-go
  - septin-huynh2006-bioc
  - septin-pmid-meta
  - septin-dubois2019-pdf
- assessment_id: septin-microneme_membrane-verdict
  area: completeness
  topic: Current scoped scientific verdict
  outcome: supported
  summary: 'pass_with_limitations: stated source tiers support current bounded identity/topology/function.
    Empty protein inventory and access/necessity limits prevent an unqualified pass;
    no confirmed curation finding.'
  target_ids:
  - GO:0033163
  evidence_ids:
  - septin-record-microneme_membrane
  - septin-original-microneme_membrane
  - septin-go
  - septin-huynh2006-bioc
  - septin-pmid-meta
  - septin-dubois2019-pdf
- assessment_id: plaque-t1-native
  area: schema
  topic: Native accession and causal-node coverage
  outcome: supported
  summary: Actual maintained inventory has 3 protein_examples and 1 typed GENE_OR_PROTEIN
    nodes. Two reviewed and one unreviewed Bath accession; pMMO component_ref has
    native COVERED status. This is identity/symbol coverage, not membership/necessity
    or exact copper mechanism.
  target_ids:
  - GO:0044227
  evidence_ids:
  - plaque-current-1
  - plaque-native-methane_oxidizing_organelle-verify
  - plaque-native-methane_oxidizing_organelle-causal
  - plaque-protein-contract
  - plaque-schema-policy
- assessment_id: plaque-t1-schema
  area: schema
  topic: Historical pair, current bytes and optional fields
  outcome: supported
  summary: Original native pair validates and exact rendered Markdown agrees; all
    historical hashes match. Current stale accession delta was independently refreshed.
    PROPOSED status retained. No images, datasets or measured physical-property assertions
    require assessment in this target.
  target_ids:
  - GO:0044227
  evidence_ids:
  - plaque-current-1
  - plaque-original-1
  - plaque-original-checks
  - plaque-rubric
- assessment_id: plaque-t5-native
  area: schema
  topic: Native accession and causal-node coverage
  outcome: supported
  summary: Actual maintained inventory has 0 protein_examples and 0 typed GENE_OR_PROTEIN
    nodes. Empty native accession/typed-node coverage does not certify all narrative
    claims.
  target_ids:
  - GO:0031040
  evidence_ids:
  - plaque-current-5
  - plaque-native-micronucleus-verify
  - plaque-native-micronucleus-causal
  - plaque-protein-contract
  - plaque-schema-policy
- assessment_id: plaque-t5-schema
  area: schema
  topic: Historical pair, current bytes and optional fields
  outcome: supported
  summary: Original native pair validates and exact rendered Markdown agrees; all
    historical hashes match. Current target equals frozen original. PROPOSED status
    retained. No images, datasets or measured physical-property assertions require
    assessment in this target.
  target_ids:
  - GO:0031040
  evidence_ids:
  - plaque-current-5
  - plaque-original-5
  - plaque-original-checks
  - plaque-rubric
- assessment_id: plaque-t6-native
  area: schema
  topic: Native accession and causal-node coverage
  outcome: supported
  summary: Actual maintained inventory has 0 protein_examples and 0 typed GENE_OR_PROTEIN
    nodes. Empty native accession/typed-node coverage does not certify all narrative
    claims.
  target_ids:
  - cellstructuremech:microsporidian_posterior_vacuole
  evidence_ids:
  - plaque-current-6
  - plaque-native-microsporidian_posterior_vacuole-verify
  - plaque-native-microsporidian_posterior_vacuole-causal
  - plaque-protein-contract
  - plaque-schema-policy
- assessment_id: plaque-t6-schema
  area: schema
  topic: Historical pair, current bytes and optional fields
  outcome: supported
  summary: Original native pair validates and exact rendered Markdown agrees; all
    historical hashes match. Current target equals frozen original. PROPOSED status
    retained. No images, datasets or measured physical-property assertions require
    assessment in this target.
  target_ids:
  - cellstructuremech:microsporidian_posterior_vacuole
  evidence_ids:
  - plaque-current-6
  - plaque-original-6
  - plaque-original-checks
  - plaque-rubric
- assessment_id: plaque-t1-identity
  area: identity
  topic: Exact organelle versus membrane enzyme
  outcome: supported
  summary: GO0044227 and its exact aliases denote the membrane-bounded methane compartment;
    pMMO is a constituent complex rather than the record identity.0043231 is correct
    broader parent; no imported whole-enzyme or chemical grounding.
  target_ids:
  - GO:0044227
  evidence_ids:
  - plaque-current-1
  - plaque-go
  - plaque-zhu2022-body
- assessment_id: plaque-t1-composition
  area: grounding
  topic: Collective bilayer and pMMO trimer
  outcome: supported
  summary: LIPID constituent describes collective inner-derived ICM bilayer; ESSENTIAL
    applies to that boundary material, not a specific lipid species. pMMO PROTEIN_COMPLEX
    is a trimer of three PmoA/B/C heterotrimers; UNKNOWN necessity retained, no exact
    complex CURIE invented. Native graph enum explicitly admits protein complexes.
  target_ids:
  - GO:0044227
  evidence_ids:
  - plaque-current-1
  - plaque-zhu2022-body
  - plaque-whiddon2019-body
  - plaque-protein-Q607G3
  - plaque-protein-G1UBD1
  - plaque-schema-policy
- assessment_id: plaque-t1-refresh
  area: provenance
  topic: Stale pmoC1 addition substantively reassessed
  outcome: supported
  summary: Q603F1 accession, submission label, primary pmoC1 name,243233Bath and UNREVIEWED
    status agree. Both locus names are retained as authority context; record makes
    no unique-locus claim. Exact pmoC1 resolves the entry despite empty exact pmoC
    query. Identity-only role avoids localization/necessity inflation. Original reviewed-only
    pmoC limitation remains truthful historically.
  target_ids:
  - GO:0044227
  evidence_ids:
  - plaque-current-1
  - plaque-original-1
  - plaque-methane-delta
  - plaque-protein-Q603F1
  - plaque-query-pmoC1-all
  - plaque-query-pmoC-reviewed
  - plaque-query-pmoC-all
  - plaque-zhu2022-body
- assessment_id: plaque-t1-examples
  area: provenance
  topic: Reviewed examples and source attribution
  outcome: supported
  summary: Q607G3 andG1UBD1 primary names, aliases, taxon/status and cited native
    membrane evidence agree. Two genomic copy rows are not two distinct reviewed accessions.
    Smith2011 primary subject is Methylocystis strainM with updated Bath model; record
    attributes a UniProt evidence link, not a new Bath localization experiment.
  target_ids:
  - GO:0044227
  evidence_ids:
  - plaque-current-1
  - plaque-protein-Q607G3
  - plaque-protein-G1UBD1
  - plaque-query-pmoA-reviewed
  - plaque-query-pmoB-reviewed
  - plaque-PMID12379148
  - plaque-PMID15674245
  - plaque-PMID22013879
- assessment_id: plaque-t1-taxonomy
  area: scope
  topic: Exact Bath canonical example and broader subset
  outcome: supported
  summary: Zhu copper-replete Bath cells directly support canonical example243233;
    Whiddon main20Z plus other type-I species provide separately scoped membrane context,
    not interchangeable strain evidence. Broad bacterial RARE is qualitative subset
    language, not prevalence measurement or all-methanotroph obligation.
  target_ids:
  - GO:0044227
  evidence_ids:
  - plaque-current-1
  - plaque-tax2
  - plaque-tax243233
  - plaque-zhu2022-body
  - plaque-whiddon2019-body
- assessment_id: plaque-t1-graph
  area: graph
  topic: All seven topology/assembly/chemistry edges
  outcome: supported
  summary: ICM boundary and native pMMO arrays, methane oxidation to methanol and
    initial catabolic step are supported. Invagination is explicitly an interpretation
    in evidence note; static continuity alone is not complete biogenesis proof. Graph
    does not claim array packing alone increases activity, exact active-site location,
    obligatory MDH complex or PmoB salt-bridge sufficiency.
  target_ids:
  - GO:0044227
  evidence_ids:
  - plaque-current-1
  - plaque-zhu2022-body
  - plaque-go
  - plaque-graph-rubric
- assessment_id: plaque-t1-function
  area: evidence
  topic: Methane chemistry and independent expression source
  outcome: supported
  summary: GO0046188 and primary activity assays support pMMO first oxidative step.
    Stolyar complete abstract supports only its narrow transcript/gene-fusion note
    for two Bath gene clusters; unsupported full-body exact-copy conclusions are not
    inferred.
  target_ids:
  - GO:0044227
  evidence_ids:
  - plaque-current-1
  - plaque-go
  - plaque-zhu2022-body
  - plaque-stolyar2001-meta
- assessment_id: plaque-t1-adapter
  area: evidence
  topic: Protein/metabolism trigger and exact catalogue scope
  outcome: supported
  summary: pmoA/B/C, three native accessions and methane catabolism require applicability
    assessment despite absence of expression-module claims. Fresh official catalogue
    has no matched Methylococcus/Bath host; unrelated Bacteria entries are not proxies.
    Historical runner unavailable is separate from current bounded source fallback.
  target_ids:
  - GO:0044227
  evidence_ids:
  - plaque-current-1
  - plaque-original-1
  - plaque-policy
  - plaque-catalogue
  - plaque-historical-runner
  - plaque-zhu2022-body
- assessment_id: plaque-t1-limits
  area: evidence
  topic: Bounded primary access and experimental limits
  outcome: unknown
  summary: Zhu/Whiddon selected bodies and relevant captions were read, not source
    figure pixels/raw data. Stolyar body routes failed; full abstract only. Three
    historical localization PMIDs reviewed at abstract/native-authority tier. Exact
    copper chemistry, full biogenesis and expression-network membership not newly
    certified.
  target_ids:
  - GO:0044227
  evidence_ids:
  - plaque-current-1
  - plaque-zhu2022-body
  - plaque-whiddon2019-body
  - plaque-stolyar2001-meta
  - plaque-stolyar2001-body
  - plaque-stolyar2001-bioc
  - plaque-PMID22013879
- assessment_id: plaque-t5-identity
  area: identity
  topic: Ciliate micronucleus and nucleus parent
  outcome: supported
  summary: GO0031040 definition and0005634 parent agree; record denotes diploid ciliate
    germline organelle, not chromosome material or somatic macronucleus. Definition
    genic-transcription wording matches current GO; mature Tetrahymena graph explicitly
    excludes meiosis/zygote/MAC rearrangement.
  target_ids:
  - GO:0031040
  evidence_ids:
  - plaque-current-5
  - plaque-go
  - plaque-hamilton2016-body
- assessment_id: plaque-t5-composition
  area: grounding
  topic: Germline chromosomal DNA versus chromosome structure
  outcome: supported
  summary: DNA constituent is collective germline genetic material; ESSENTIAL at that
    scope does not claim every sequence is required or nuclear-envelope assembly cannot
    persist without DNA. GO0000228 denotes whole chromosome and is correctly not misused
    for DNA molecules. Optional exact SO grounding remains unresolved, not an established
    missing-required-ID issue.
  target_ids:
  - GO:0031040
  evidence_ids:
  - plaque-current-5
  - plaque-go
  - plaque-hamilton2016-body
  - plaque-schema-policy
- assessment_id: plaque-t5-taxonomy
  area: scope
  topic: Tetrahymena species and SB210 preparation
  outcome: supported
  summary: Taxon5911 is T.thermophila; source Methods validates all five SB210 chromosomes
    before isolating MICs and sequencing. Qualitative COMMON concerns this nuclear
    dimorphism, not every life-cycle stage or a quantitative prevalence. No other
    ciliate strain substituted.
  target_ids:
  - GO:0031040
  evidence_ids:
  - plaque-current-5
  - plaque-tax5911
  - plaque-hamilton2016-body
- assessment_id: plaque-t5-function
  area: evidence
  topic: Mature germline genome maintenance
  outcome: supported
  summary: Source supports diploid transcriptionally silent germline nuclear compartment
    and transmission through sexual generations. Descriptive record does not erase
    developmental noncoding transcription or generalize SB210 assembly results to
    gapless assemblies in every ciliate.
  target_ids:
  - GO:0031040
  evidence_ids:
  - plaque-current-5
  - plaque-hamilton2016-body
  - plaque-go
- assessment_id: plaque-t5-graph
  area: graph
  topic: Four descriptive containment/transmission edges
  outcome: supported
  summary: DNA is housed in MIC, constitutes germline genome, MIC preserves it and
    genetic material is transmitted during sexual reproduction. Five chromosome-length
    superassemblies are source-supported but retain assembly gaps; NONMECHANISTIC
    scope does not imply actual rearrangement chronology or DNA alone suffices for
    reproduction.
  target_ids:
  - GO:0031040
  evidence_ids:
  - plaque-current-5
  - plaque-hamilton2016-body
  - plaque-go
  - plaque-graph-rubric
- assessment_id: plaque-t5-history
  area: consistency
  topic: Optional grounding and earlier correction remain scoped
  outcome: supported
  summary: Current GO0019953 final process agrees. Historical issue1290 resolution
    is merely recorded history; no new terminal disposition of an unfrozen earlier
    review. Exact DNA-grounding TODO is not elevated into a required curation finding.
  target_ids:
  - GO:0031040
  evidence_ids:
  - plaque-current-5
  - plaque-go
  - plaque-rubric
- assessment_id: plaque-t5-adapter
  area: evidence
  topic: Genic-transcription/genome program triggers applicability
  outcome: supported
  summary: Complete definition/function/graph include genic transcription, germline
    genome maintenance and sexual transmission; explicit expression-module-only exclusion
    bypasses required assessment. Fresh catalogue has no Tetrahymena/ciliate host.
    No foreign microbial dataset query or biological-absence conclusion follows.
  target_ids:
  - GO:0031040
  evidence_ids:
  - plaque-current-5
  - plaque-original-5
  - plaque-policy
  - plaque-catalogue
  - plaque-historical-runner
  - plaque-hamilton2016-body
- assessment_id: plaque-t5-limits
  area: evidence
  topic: Source and assembly limits
  outcome: unknown
  summary: Selected Hamilton Introduction/assembly/Methods were inspected without
    raw-read reassembly or figure-pixel review. Current authority and mature scope
    support claims; no exhaustive whole-life-cycle transcription survey or exhaustive
    SO search performed.
  target_ids:
  - GO:0031040
  evidence_ids:
  - plaque-current-5
  - plaque-hamilton2016-body
  - plaque-go
- assessment_id: plaque-t6-identity
  area: identity
  topic: Posterior vesicle distinct from polar tube/peroxisome
  outcome: supported
  summary: Minted membrane-bounded posterior organelle identity matches primary spore
    morphology; exact polar tube0044099 remains a distinct node. First25 QuickGO posterior-vacuole
    matches offered no exact identity; no exhaustive absence claim or broader vacuole
    substitution. Findley biochemical analogy is not imported as peroxisome identity.
  target_ids:
  - cellstructuremech:microsporidian_posterior_vacuole
  evidence_ids:
  - plaque-current-6
  - plaque-go
  - plaque-posterior-go-query
  - plaque-findley2005-pdf
  - plaque-jaroenlak2020-body
- assessment_id: plaque-t6-composition
  area: grounding
  topic: Bounded membrane material and unresolved mechanism
  outcome: supported
  summary: Single limiting membrane observed by2D TEM supports collective LIPID boundary;
    UNKNOWN molecular necessity retained. Exact lipids, osmolytes and driving proteins
    are explicitly unresolved; empty optional inventory alone is not a scientific
    defect and source-specific catalase observations are not universalized.
  target_ids:
  - cellstructuremech:microsporidian_posterior_vacuole
  evidence_ids:
  - plaque-current-6
  - plaque-jaroenlak2020-body
  - plaque-findley2005-pdf
  - plaque-schema-policy
- assessment_id: plaque-t6-taxonomy
  area: scope
  topic: Infectious spores and species-specific observations
  outcome: supported
  summary: 6029Microsporidia and6039V.necatrix identities agree. S.lophii,A.algerae,E.aedis
    andV.necatrix are separately scoped observations; COMMON is qualitative infectious-spore
    context, not every vegetative stage. Secondary chapter abstract has no quantitative
    posterior-vacuole prevalence claim.
  target_ids:
  - cellstructuremech:microsporidian_posterior_vacuole
  evidence_ids:
  - plaque-current-6
  - plaque-tax6029
  - plaque-tax6039
  - plaque-findley2005-pdf
  - plaque-jaroenlak2020-body
  - plaque-troemel2015-body
  - plaque-sharma2024-body
  - plaque-jaroenlak2022-meta
- assessment_id: plaque-t6-F1
  area: evidence
  topic: Source modality and imaged-object mismatch
  outcome: concern
  summary: 'Inherited F1 remains: Jaroenlak2020 SBFSEM plus2D TEM is incorrectly called
    electron tomography; Sharma2024 firing dynamics are light microscopy while cryoET
    excluded spores and sampled tube regions. Correct source notes without rejecting
    supported organelle occurrence or membrane topology.'
  target_ids:
  - cellstructuremech:microsporidian_posterior_vacuole
  evidence_ids:
  - plaque-current-6
  - plaque-original-6
  - plaque-jaroenlak2020-body
  - plaque-sharma2024-body
- assessment_id: plaque-t6-F2
  area: evidence
  topic: Proposed driver overclaimed in final edge
  outcome: concern
  summary: 'Inherited F2 remains: final enters-edge description/evidence upgrades
    Troemel2015 apparent/likely vacuolar pushing to unqualified pushes/drives. Other
    descriptions already retain implication. Restore qualification or describe only
    observed cargo passage; no isolated-force mechanism proven.'
  target_ids:
  - cellstructuremech:microsporidian_posterior_vacuole
  evidence_ids:
  - plaque-current-6
  - plaque-original-6
  - plaque-troemel2015-body
  - plaque-graph-rubric
- assessment_id: plaque-t6-graph
  area: graph
  topic: Remaining four edges and temporal context
  outcome: supported
  summary: Membrane encloses vesicle, posterior location, expansion during firing
    and separately qualified pushing interpretation agree with source scopes. Sharma
    light-dynamic imaging supports the qualified preceding note, not a false cryoET
    movie. Final edge correction is precisely F2, not rejection of temporal sequence/cargo
    passage.
  target_ids:
  - cellstructuremech:microsporidian_posterior_vacuole
  evidence_ids:
  - plaque-current-6
  - plaque-findley2005-pdf
  - plaque-troemel2015-body
  - plaque-jaroenlak2020-body
  - plaque-sharma2024-body
- assessment_id: plaque-t6-adapter
  area: evidence
  topic: Genuine sparse physical/physiological exclusion
  outcome: not_applicable
  summary: Complete record asserts boundary topology, position, swelling and proposed
    physical pressure/cargo movement; no positively specified gene, protein, regulator,
    molecular pathway, stress-response trait or transcriptomic dataset is asserted.
    Composition is explicitly unresolved. Generic firing alone and molecular details
    merely present in cited papers do not create a record-level adapter trigger. Original
    exclusion can stand with this precise rationale; not counted as a bundle defect.
  target_ids:
  - cellstructuremech:microsporidian_posterior_vacuole
  evidence_ids:
  - plaque-current-6
  - plaque-original-6
  - plaque-policy
  - plaque-catalogue
- assessment_id: plaque-t6-history
  area: consistency
  topic: Historical boundary repair and live optional TODO
  outcome: supported
  summary: Current membrane component_ref is on boundary node, not organelle. Historical
    issue778 resolution not re-certified beyond current representation, and optional
    composition TODO is not automatically an untracked request-curation finding. Two
    explicit inherited findings/actions retained exactly.
  target_ids:
  - cellstructuremech:microsporidian_posterior_vacuole
  evidence_ids:
  - plaque-current-6
  - plaque-original-6
  - plaque-schema-policy
- assessment_id: plaque-t6-limits
  area: evidence
  topic: Body/abstract/pixel and mechanism boundaries
  outcome: unknown
  summary: Findley PDF selected main pages and Jaroenlak/Sharma selected genuine bodies/captions
    read; Troemel main body read but videos not replayed. No source figure pixels
    or raw data reviewed for this target.2022 chapter abstract only; phylum prevalence
    not measured. Microscopy and causal-scope defects are established from explicit
    Methods/text, not absence of access.
  target_ids:
  - cellstructuremech:microsporidian_posterior_vacuole
  evidence_ids:
  - plaque-current-6
  - plaque-findley2005-pdf
  - plaque-troemel2015-body
  - plaque-jaroenlak2020-body
  - plaque-sharma2024-body
  - plaque-jaroenlak2022-meta
- assessment_id: micro-mitochondrial_crista-identity
  area: identity
  topic: Exact structure identity and boundaries
  outcome: supported
  summary: Whole crista is an inward IMM fold; junction is its connection to the boundary
    membrane. Exact GO identity/part_of and anatomical has_part interpretation remain
    distinct.
  target_ids:
  - GO:0030061
  evidence_ids:
  - micro-record-mitochondrial_crista
  - micro-go
  - micro-friedman2015-body
- assessment_id: micro-mitochondrial_crista-taxa
  area: scope
  topic: Taxon identities and experimental strains
  outcome: supported
  summary: Exact species/strain identities agree; source-specific W303, BY/S288C-derived
    and other named yeast experimental strains are not all equated to unmodified S288C.
    COMMON/VARIABLE are qualitative; no quantitative prevalence survey performed.
  target_ids:
  - GO:0030061
  evidence_ids:
  - micro-record-mitochondrial_crista
  - micro-tax2759
  - micro-tax4932
  - micro-tax559292
  - micro-friedman2015-body
  - micro-davies2012-pmc
  - micro-PMC11320809-body
- assessment_id: micro-mitochondrial_crista-native
  area: schema
  topic: Original pairs and native protein scope
  outcome: supported
  summary: Original native validation/render and frozen source hashes passed. No component
    protein examples and zero GENE_OR_PROTEIN nodes; complex STRUCTURE actors are
    outside the typed-node denominator.
  target_ids:
  - GO:0030061
  evidence_ids:
  - micro-prior-mitochondrial_crista
  - micro-original-pairs
  - micro-native-mitochondrial_crista-verify
  - micro-native-mitochondrial_crista-causal
  - micro-graph-policy
- assessment_id: micro-mitochondrial_crista-adapter-original
  area: provenance
  topic: Present but unsupported expression-only exclusion
  outcome: concern
  summary: Original check row is present, not omitted. Its lack-of-expression rationale
    misses named architecture/respiration or MDC protein, stress and intervention
    pathways, which trigger applicability assessment under native policy.
  target_ids:
  - GO:0030061
  evidence_ids:
  - micro-record-mitochondrial_crista
  - micro-prior-mitochondrial_crista
  - micro-policy
- assessment_id: micro-mitochondrial_crista-adapter-current
  area: evidence
  topic: Current exact-host catalogue fallback
  outcome: not_applicable
  summary: Fresh full official catalogue has no matching yeast/eukaryotic experimental
    host. No unmatched organism proxy or downstream module claim is warranted. Historical
    runner failure remains separately dated/unavailable, not a new run.
  target_ids:
  - GO:0030061
  evidence_ids:
  - micro-record-mitochondrial_crista
  - micro-catalogue
  - micro-historical-runner
  - micro-policy
- assessment_id: micro-mitochondrial_crista-status
  area: completeness
  topic: Complete record, optional enrichment and scope
  outcome: supported
  summary: Entire target and original scientific findings/actions read. Optional inventories,
    exact molecular additions and raw experiments are not invented; native PROPOSED
    status and history remain unchanged. No neighboring/grouped/category issue is
    terminally resolved.
  target_ids:
  - GO:0030061
  evidence_ids:
  - micro-record-mitochondrial_crista
  - micro-prior-mitochondrial_crista
  - micro-policy
- assessment_id: micro-mitochondrial_crista_junction-identity
  area: identity
  topic: Exact structure identity and boundaries
  outcome: supported
  summary: Junction is a subcellular contact region, not MICOS itself; direct is_a
    contact-site and IMM part_of authority relations agree.
  target_ids:
  - GO:0044284
  evidence_ids:
  - micro-record-mitochondrial_crista_junction
  - micro-go
  - micro-friedman2015-body
- assessment_id: micro-mitochondrial_crista_junction-taxa
  area: scope
  topic: Taxon identities and experimental strains
  outcome: supported
  summary: Exact species/strain identities agree; source-specific W303, BY/S288C-derived
    and other named yeast experimental strains are not all equated to unmodified S288C.
    COMMON/VARIABLE are qualitative; no quantitative prevalence survey performed.
  target_ids:
  - GO:0044284
  evidence_ids:
  - micro-record-mitochondrial_crista_junction
  - micro-tax2759
  - micro-tax4932
  - micro-tax559292
  - micro-friedman2015-body
  - micro-davies2012-pmc
  - micro-PMC11320809-body
- assessment_id: micro-mitochondrial_crista_junction-native
  area: schema
  topic: Original pairs and native protein scope
  outcome: supported
  summary: Original native validation/render and frozen source hashes passed. No component
    examples and zero GENE_OR_PROTEIN nodes after MICOS retyping. STRUCTURE-node P36112
    is skipped by native protein verification and independently verified from fresh
    authority JSON.
  target_ids:
  - GO:0044284
  evidence_ids:
  - micro-prior-mitochondrial_crista_junction
  - micro-original-pairs
  - micro-native-mitochondrial_crista_junction-verify
  - micro-native-mitochondrial_crista_junction-causal
  - micro-graph-policy
- assessment_id: micro-mitochondrial_crista_junction-adapter-original
  area: provenance
  topic: Present but unsupported expression-only exclusion
  outcome: concern
  summary: Original check row is present, not omitted. Its lack-of-expression rationale
    misses named architecture/respiration or MDC protein, stress and intervention
    pathways, which trigger applicability assessment under native policy.
  target_ids:
  - GO:0044284
  evidence_ids:
  - micro-record-mitochondrial_crista_junction
  - micro-prior-mitochondrial_crista_junction
  - micro-policy
- assessment_id: micro-mitochondrial_crista_junction-adapter-current
  area: evidence
  topic: Current exact-host catalogue fallback
  outcome: not_applicable
  summary: Fresh full official catalogue has no matching yeast/eukaryotic experimental
    host. No unmatched organism proxy or downstream module claim is warranted. Historical
    runner failure remains separately dated/unavailable, not a new run.
  target_ids:
  - GO:0044284
  evidence_ids:
  - micro-record-mitochondrial_crista_junction
  - micro-catalogue
  - micro-historical-runner
  - micro-policy
- assessment_id: micro-mitochondrial_crista_junction-status
  area: completeness
  topic: Complete record, optional enrichment and scope
  outcome: supported
  summary: Entire target and original scientific findings/actions read. Optional inventories,
    exact molecular additions and raw experiments are not invented; native PROPOSED
    status and history remain unchanged. No neighboring/grouped/category issue is
    terminally resolved.
  target_ids:
  - GO:0044284
  evidence_ids:
  - micro-record-mitochondrial_crista_junction
  - micro-prior-mitochondrial_crista_junction
  - micro-policy
- assessment_id: micro-mitochondrial_derived_compartment-identity
  area: identity
  topic: Exact structure identity and boundaries
  outcome: supported
  summary: Local MDC identity denotes yeast OMM-derived multilamellar domains, distinct
    from generic MDVs, protein aggregates or universal closed vesicles. Broad organelle
    parent is not substituted as exact identity.
  target_ids:
  - cellstructuremech:mitochondrial_derived_compartment
  evidence_ids:
  - micro-record-mitochondrial_derived_compartment
  - micro-go
  - micro-PMC11320809-body
- assessment_id: micro-mitochondrial_derived_compartment-taxa
  area: scope
  topic: Taxon identities and experimental strains
  outcome: supported
  summary: Exact species/strain identities agree; source-specific W303, BY/S288C-derived
    and other named yeast experimental strains are not all equated to unmodified S288C.
    COMMON/VARIABLE are qualitative; no quantitative prevalence survey performed.
  target_ids:
  - cellstructuremech:mitochondrial_derived_compartment
  evidence_ids:
  - micro-record-mitochondrial_derived_compartment
  - micro-tax2759
  - micro-tax4932
  - micro-tax559292
  - micro-friedman2015-body
  - micro-davies2012-pmc
  - micro-PMC11320809-body
- assessment_id: micro-mitochondrial_derived_compartment-native
  area: schema
  topic: Original pairs and native protein scope
  outcome: supported
  summary: Original native validation/render and frozen source hashes passed. Three
    reviewed component examples TOM70/P07213, TOM71/P38825 and DNM1/P54861 in tax559292;
    zero GENE_OR_PROTEIN nodes because intervention/capability nodes are STATE.
  target_ids:
  - cellstructuremech:mitochondrial_derived_compartment
  evidence_ids:
  - micro-prior-mitochondrial_derived_compartment
  - micro-original-pairs
  - micro-native-mitochondrial_derived_compartment-verify
  - micro-native-mitochondrial_derived_compartment-causal
  - micro-graph-policy
- assessment_id: micro-mitochondrial_derived_compartment-adapter-original
  area: provenance
  topic: Present but unsupported expression-only exclusion
  outcome: concern
  summary: Original check row is present, not omitted. Its lack-of-expression rationale
    misses named architecture/respiration or MDC protein, stress and intervention
    pathways, which trigger applicability assessment under native policy.
  target_ids:
  - cellstructuremech:mitochondrial_derived_compartment
  evidence_ids:
  - micro-record-mitochondrial_derived_compartment
  - micro-prior-mitochondrial_derived_compartment
  - micro-policy
- assessment_id: micro-mitochondrial_derived_compartment-adapter-current
  area: evidence
  topic: Current exact-host catalogue fallback
  outcome: not_applicable
  summary: Fresh full official catalogue has no matching yeast/eukaryotic experimental
    host. No unmatched organism proxy or downstream module claim is warranted. Historical
    runner failure remains separately dated/unavailable, not a new run.
  target_ids:
  - cellstructuremech:mitochondrial_derived_compartment
  evidence_ids:
  - micro-record-mitochondrial_derived_compartment
  - micro-catalogue
  - micro-historical-runner
  - micro-policy
- assessment_id: micro-mitochondrial_derived_compartment-status
  area: completeness
  topic: Complete record, optional enrichment and scope
  outcome: supported
  summary: Entire target and original scientific findings/actions read. Optional inventories,
    exact molecular additions and raw experiments are not invented; native PROPOSED
    status and history remain unchanged. No neighboring/grouped/category issue is
    terminally resolved.
  target_ids:
  - cellstructuremech:mitochondrial_derived_compartment
  evidence_ids:
  - micro-record-mitochondrial_derived_compartment
  - micro-prior-mitochondrial_derived_compartment
  - micro-policy
- assessment_id: micro-mitochondrial_crista-architecture
  area: graph
  topic: All current nonmechanistic topology and architecture edges
  outcome: supported
  summary: MICOS maintenance, junction connections and (whole crista) ATP-synthase
    ridge shaping/respiratory support have bounded yeast primary and GO support. MICOS
    subcomplex-localization inference uses marker adjacency; direct junction immuno-EM
    failed. Detailed assembly/cardiolipin/remodeling mechanism is not asserted.
  target_ids:
  - GO:0030061
  evidence_ids:
  - micro-record-mitochondrial_crista
  - micro-go
  - micro-friedman2015-body
  - micro-davies2012-pmc
  - micro-paumard2002-pmc
- assessment_id: micro-mitochondrial_crista-general-limits
  area: scope
  topic: General lineage and taxon constraint limits
  outcome: unknown
  summary: Exact GO responses contain no explicit taxon constraints; inspected secondary
    passage does not establish every reduced anaerobic-organelle exception. Eukaryotic
    mitochondrial context is supported, but no exhaustive lineage/absence survey was
    done. Unknown scope is not refutation.
  target_ids:
  - GO:0030061
  evidence_ids:
  - micro-record-mitochondrial_crista
  - micro-go
  - micro-friedman2014-body
  - micro-tax2759
- assessment_id: micro-mitochondrial_crista_junction-architecture
  area: graph
  topic: All current nonmechanistic topology and architecture edges
  outcome: supported
  summary: MICOS maintenance, junction connections and (whole crista) ATP-synthase
    ridge shaping/respiratory support have bounded yeast primary and GO support. MICOS
    subcomplex-localization inference uses marker adjacency; direct junction immuno-EM
    failed. Detailed assembly/cardiolipin/remodeling mechanism is not asserted.
  target_ids:
  - GO:0044284
  evidence_ids:
  - micro-record-mitochondrial_crista_junction
  - micro-go
  - micro-friedman2015-body
  - micro-davies2012-pmc
  - micro-paumard2002-pmc
- assessment_id: micro-mitochondrial_crista_junction-general-limits
  area: scope
  topic: General lineage and taxon constraint limits
  outcome: unknown
  summary: Exact GO responses contain no explicit taxon constraints; inspected secondary
    passage does not establish every reduced anaerobic-organelle exception. Eukaryotic
    mitochondrial context is supported, but no exhaustive lineage/absence survey was
    done. Unknown scope is not refutation.
  target_ids:
  - GO:0044284
  evidence_ids:
  - micro-record-mitochondrial_crista_junction
  - micro-go
  - micro-friedman2014-body
  - micro-tax2759
- assessment_id: micro-crista-components
  area: grounding
  topic: Complex roles and formation necessity
  outcome: supported
  summary: MICOS remains associated architecture machinery with UNKNOWN necessity;
    resident ATP synthase is a constituent with UNKNOWN necessity. Perturbed lamellar
    morphology does not prove every complex/subunit is universally necessary for any
    inward fold. Source-neutral complex abstractions are valid; optional subunits/lipids
    are not a consequential omission.
  target_ids:
  - GO:0030061
  evidence_ids:
  - micro-record-mitochondrial_crista
  - micro-component-policy
  - micro-go
  - micro-friedman2015-body
  - micro-davies2012-pmc
  - micro-paumard2002-pmc
- assessment_id: micro-junction-stale-refresh
  area: provenance
  topic: Substantive MICOS actor retyping refresh
  outcome: supported
  summary: GO0061617 correctly denotes MICOS as STRUCTURE; P36112 separately verifies
    a Mic60 member and does not identify the whole complex. Current maintenance edge
    remains source-supported. Closed2419 is historical context, not disposition of
    its whole group or of the inherited microscopy attribution.
  target_ids:
  - GO:0044284
  evidence_ids:
  - micro-record-mitochondrial_crista_junction
  - micro-stale-delta
  - micro-component-policy
  - micro-protein-P36112
  - micro-go
  - micro-friedman2015-body
  - micro-historical-2419
- assessment_id: micro-junction-modality
  area: evidence
  topic: Inherited microscopy-method attribution
  outcome: concern
  summary: Friedman2015 Methods report fixed resin sections/TEM plus fluorescence.
    Current canonical example wrongly calls this tomography; inherited stable-key
    finding remains open without refuting yeast MICOS biology.
  target_ids:
  - GO:0044284
  evidence_ids:
  - micro-record-mitochondrial_crista_junction
  - micro-friedman2015-body
- assessment_id: micro-mdc-components
  area: grounding
  topic: Five constituent and associated-machinery classes
  outcome: supported
  summary: Heterogeneous lipid bilayers and cytosolic cargo are appropriately label-only.
    Tom70/Tom71 are sampled cargo with UNKNOWN necessity. Dnm1 is DISPENSABLE associated
    release machinery in bounded ConcA formation assay. Regulators and contact-site
    machinery are not automatically canonical constituents; no invariant stoichiometry
    asserted.
  target_ids:
  - cellstructuremech:mitochondrial_derived_compartment
  evidence_ids:
  - micro-record-mitochondrial_derived_compartment
  - micro-component-policy
  - micro-PMC4889329-body
  - micro-PMC11320809-body
  - micro-PMC11320589-body
  - micro-PMC7588143-body
- assessment_id: micro-mdc-proteins
  area: grounding
  topic: Exact three examples and bounded family searches
  outcome: supported
  summary: TOM70/TOM71/DNM1 names/loci/review status/S288C identity and one-reviewed-hit
    searches agree. Tom70 exact IPR005687 is present. Tom71 integrated endpoint returns
    only TPR classes; Dynamin IPR022812 is broader than mitochondrial Dnm1. No arbitrary
    family is transferred from similarity or generic domain.
  target_ids:
  - cellstructuremech:mitochondrial_derived_compartment
  evidence_ids:
  - micro-protein-P07213
  - micro-protein-P38825
  - micro-protein-P54861
  - micro-family-P07213
  - micro-family-P38825
  - micro-family-P54861
  - micro-IPR005687
  - micro-IPR022812
  - micro-query-TOM70
  - micro-query-TOM71
  - micro-query-DNM1
- assessment_id: micro-mdc-function
  area: scope
  topic: Revised cargo and conditional routing
  outcome: supported
  summary: '2024 tag-orientation/localization results revise2016 carrier model: functional
    IMM carriers are not routine cargo, assembled core TOM proteins are not uniformly
    enriched. Selected OMM cargo and partial protection are supported. ConcA-associated
    vacuolar routing is distinct from initial formation and not universal fate.'
  target_ids:
  - cellstructuremech:mitochondrial_derived_compartment
  evidence_ids:
  - micro-record-mitochondrial_derived_compartment
  - micro-PMC4889329-body
  - micro-PMC11320809-body
  - micro-PMC11320589-body
- assessment_id: micro-mdc-edges
  area: graph
  topic: Nine assay-bounded intervention/capability edges
  outcome: concern
  summary: 'Rap induction, selected-cargo/cytosol sequestration, MMM1/GEM1 effects,
    DNM1 release and PSD1/CRD1 directions are supported with source conditions and
    partiality. Tom70/Tom71 edge has inherited assay-attribution mismatch: sole cited
    Hughes2016 experiment is ConcA2h in dnm1Δ, not rapamycin. No direct-binding/universal
    linear pathway claimed.'
  target_ids:
  - cellstructuremech:mitochondrial_derived_compartment
  evidence_ids:
  - micro-record-mitochondrial_derived_compartment
  - micro-PMC4889329-body
  - micro-PMC11320809-body
  - micro-PMC11320589-body
  - micro-PMC7588143-body
  - micro-PMC10949074-body
- assessment_id: micro-mdc-measurements-image
  area: evidence
  topic: Actual pixels, measurement conditions and license
  outcome: supported
  summary: Figure1C0.41µm/n104 and FigureS1C0.36µm/n49 apply to spherical Rap200nM
    or ConcA500nM2h MDCs. Both axes read µm; initial glyph-misreading hypothesis was
    rejected after independent challenge and own original-detail reinspection. Figure1
    mixed modality/attribution/scale bars/yeast and link-only CC BY-NC-SA4 are correct.
    TEM section thickness is not diameter.
  target_ids:
  - cellstructuremech:mitochondrial_derived_compartment
  evidence_ids:
  - micro-record-mitochondrial_derived_compartment
  - micro-PMC11320809-body
  - micro-wilson2024-Fig1
  - micro-wilson2024-FigS1
  - micro-uo0000017
  - micro-image-independent-challenge
- assessment_id: micro-mdc-lipid-conflict
  area: evidence
  topic: Preserved study-specific lipid discrepancy
  outcome: supported
  summary: 2020 tested lipid mutants did not impair formation;2024 shows CL suppression
    and PE-dependent promotion/partial bypass. Record correctly retains discrepancy
    without invented reconciliation, isolated-MDC composition or universal enzyme
    necessity.
  target_ids:
  - cellstructuremech:mitochondrial_derived_compartment
  evidence_ids:
  - micro-record-mitochondrial_derived_compartment
  - micro-PMC7588143-body
  - micro-PMC10949074-body
- assessment_id: micro-mdc-preprints
  area: evidence
  topic: 2026 models and actual access tiers
  outcome: unknown
  summary: Both exact2026 DOI/PMID identities and official reviewed-preprintv1 metadata
    are verified. First PMC artifact is an availability stub; second Discussion explicitly
    cannot isolate MDC-specific fitness/buffering contribution. Publisher Results
    not certified read. Historical access notes remain historical; these models are
    not promoted into canonical graph/components.
  target_ids:
  - cellstructuremech:mitochondrial_derived_compartment
  evidence_ids:
  - micro-record-mitochondrial_derived_compartment
  - micro-PMID42798366
  - micro-PMID42327138
  - micro-preprintA2026-meta
  - micro-preprintB2026-meta
  - micro-PMC13605720-body
  - micro-PMC13278180-body
  - micro-elife111713
  - micro-elife112436
- assessment_id: current-input-comparison
  area: provenance
  topic: Complete frozen-input comparison and bounded refresh
  outcome: supported
  summary: 4 of ten original target hashes differ from current main. The changed content
    is substantively reassessed in the target-specific assessments; original observations
    remain historical and unchanged. All current target and used context bytes are
    frozen.
  target_ids:
  - GO:0020036
  - GO:0044227
  - GO:0020009
  - GO:0034494
  - GO:0033163
  - GO:0031040
  - cellstructuremech:microsporidian_posterior_vacuole
  - GO:0030061
  - GO:0044284
  - cellstructuremech:mitochondrial_derived_compartment
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
- finding_id: septin-maurer_s_cleft-F1
  issue_key: maurer-canonical-genetic-study-attribution
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Align the canonical genetic-study note with its cited paper
  description: The canonical note attributes genetic testing of both SBP1 and MAHRP1
    to its sole Cooke2006 citation. Cooke tests SBP1 deletion/complementation; the
    MAHRP1 genetic test is in Spycher2008, already listed elsewhere in the record.
  target_ids:
  - GO:0020036
  field_paths:
  - canonical_examples[0].note
  - canonical_examples[0].reference
  evidence_ids:
  - septin-record-maurer_s_cleft
  - septin-original-maurer_s_cleft
  - septin-cooke2006-bioc
  - septin-spycher2008-meta
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/maurer_s_cleft.yaml
    role: maintained scientific record
  rule_id: .claude/skills/review-yaml-record/SKILL.md:claim-level evidence placement
  native_severity: minor
  normalization_reason: The species, organelle and genetic findings are supported;
    this is a bounded citation-placement error, not a biological identity or mechanism
    contradiction.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T022231Z-maurer-s-cleft-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2723
- finding_id: septin-microneme-F1
  issue_key: microneme-lipid-whole-membrane-grounding
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Separate the lipid constituent from the complete membrane identity
  description: The microneme_membrane LIPID component uses GO0033163, the entire microneme
    membrane, as molecular grounding; the graph membrane node also links to that component.
    The frozen schema distinguishes molecular lipid identity from a whole cellular
    structure.
  target_ids:
  - GO:0020009
  field_paths:
  - components[component_id=microneme_membrane].grounding
  - components[component_id=microneme_membrane].component_type
  - causal_graphs[graph_id=microneme_exocytosis_host_invasion].nodes[node_id=microneme_membrane].component_ref
  evidence_ids:
  - septin-record-microneme
  - septin-original-microneme
  - septin-schema-policy
  - septin-go
  - septin-record-microneme_membrane
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/microneme.yaml
    role: maintained scientific record
  rule_id: .claude/skills/review-yaml-record/SKILL.md:identity and source scope
  native_severity: major
  normalization_reason: This materially misidentifies the structured molecular constituent,
    despite correct organelle identity and has_part topology. It requires a scientific
    representation correction, not just a citation-format change.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T022233Z-microneme-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2724
- finding_id: septin-microneme-F2
  issue_key: microneme-transmembrane-cargo-lumen-qualification
  category: graph
  severity: minor
  status: open
  certainty: confirmed
  title: Qualify lumen localization of transmembrane adhesin complexes
  description: The whole MIC2–M2AP complex and MIC1/MIC2/AMA1 cohort are linked as
    residing in the lumen. MIC2 and AMA1 span membranes and have cytosolic domains;
    the whole complex is not identical to its luminal adhesive domains or soluble
    M2AP.
  target_ids:
  - GO:0020009
  field_paths:
  - causal_graphs[graph_id=microneme_exocytosis_host_invasion].edges[subject=microneme_adhesins,object=microneme_lumen]
  - causal_graphs[graph_id=microneme_exocytosis_host_invasion].edges[subject=mic2_m2ap_complex,object=microneme_lumen]
  evidence_ids:
  - septin-record-microneme
  - septin-original-microneme
  - septin-huynh2006-bioc
  - septin-protein-B6KAM0
  - septin-pmid-meta
  - septin-dubois2019-pdf
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/microneme.yaml
    role: maintained scientific record
  rule_id: .claude/skills/review-yaml-record/SKILL.md:identity and source scope
  native_severity: minor
  normalization_reason: The underlying microneme localization, membership and causal
    function are correct, and edge descriptions already state whole-organelle storage.
    The error is the local over-specific lumen endpoint, correctable without replacing
    the organelle or mechanism.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T022233Z-microneme-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2725
- finding_id: septin-microneme-F3
  issue_key: microneme-canonical-multiple-study-attribution
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Match the canonical example clauses to their supporting studies
  description: The sole canonical PMID9208224 supports sequential secretion, but its
    note also names MIC2–M2AP and PKG-regulated exocytosis experiments supplied by
    other papers already present in the record.
  target_ids:
  - GO:0020009
  field_paths:
  - canonical_examples[0].note
  - canonical_examples[0].reference
  evidence_ids:
  - septin-record-microneme
  - septin-original-microneme
  - septin-pmid-meta
  - septin-huynh2003-meta
  - septin-brown2016-meta
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/microneme.yaml
    role: maintained scientific record
  rule_id: .claude/skills/review-yaml-record/SKILL.md:identity and source scope
  native_severity: minor
  normalization_reason: All biological claims are supported elsewhere in the record;
    the defect is bounded claim-level citation placement.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T022233Z-microneme-audit
    finding_id: F3
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2726
- finding_id: plaque-t6-F1
  issue_key: posterior-vacuole-microscopy-source-scope
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Correct microscopy descriptions and their observational scope
  description: Jaroenlak2020 used serial block-face SEM and 2D TEM, whereas the component
    evidence note adds electron tomography. Sharma2024 used light microscopy for germination
    dynamics and cryoET for extruded tube segments; its Methods explicitly excluded
    spores from tilt-series collection. The canonical example note therefore overstates
    what was imaged by cryoET. This does not refute V.necatrix organelle occurrence
    or the supported membrane topology.
  target_ids:
  - cellstructuremech:microsporidian_posterior_vacuole
  field_paths:
  - components#posterior_vacuole_membrane.evidence[1].notes
  - canonical_examples[0].note
  evidence_ids:
  - plaque-current-6
  - plaque-original-6
  - plaque-jaroenlak2020-body
  - plaque-sharma2024-body
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/microsporidian_posterior_vacuole.yaml
    role: maintained scientific record
  rule_id: .claude/skills/review-yaml-record/SKILL.md:claim support and evidence placement
  native_severity: minor
  normalization_reason: Bounded source-description or causal-qualification defect;
    core organelle identity and observed topology/cargo passage remain supported.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T022238Z-microsporidian-posterior-vacuole-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2727
- finding_id: plaque-t6-F2
  issue_key: posterior-vacuole-cargo-causal-qualification
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Retain the source’s qualification of the pushing mechanism
  description: The final enters edge asserts without qualification that vacuole expansion
    pushes and drives sporoplasm passage. The cited Troemel2015 main text presents
    this as an interpretation of the video, with uncertain mechanism. Restore that
    epistemic scope, consistent with the record definition and preceding qualified
    edge; observed cargo entry is supported.
  target_ids:
  - cellstructuremech:microsporidian_posterior_vacuole
  field_paths:
  - causal_graphs#posterior_vacuole_expansion_supports_firing.edges[4].description
  - causal_graphs#posterior_vacuole_expansion_supports_firing.edges[4].evidence[0].notes
  evidence_ids:
  - plaque-current-6
  - plaque-original-6
  - plaque-troemel2015-body
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/microsporidian_posterior_vacuole.yaml
    role: maintained scientific record
  rule_id: .claude/skills/review-yaml-record/SKILL.md:claim support and evidence placement
  native_severity: minor
  normalization_reason: Bounded source-description or causal-qualification defect;
    core organelle identity and observed topology/cargo passage remain supported.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T022238Z-microsporidian-posterior-vacuole-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2728
- finding_id: micro-F1
  issue_key: mitochondrial-crista-junction-1
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Correct the imaging modality attributed to Friedman2015
  description: The canonical example says the cited Friedman2015 study used electron
    tomography. Its electron-microscopy Methods specify fixed resin sections observed
    by transmission electron microscopy, alongside fluorescence. The paper remains
    relevant to yeast MICOS-dependent architecture; the incorrect modality is a bounded
    provenance error.
  target_ids:
  - GO:0044284
  field_paths:
  - canonical_examples[0].note
  evidence_ids:
  - micro-record-mitochondrial_crista_junction
  - micro-friedman2015-body
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/mitochondrial_crista_junction.yaml
    role: maintained scientific record
  rule_id: .claude/skills/review-yaml-record/SKILL.md:exact identity and claim-level
    support
  native_severity: minor
  normalization_reason: Minor source-method attribution error with the biological
    model and phenotype interpretation otherwise supported.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T022239Z-mitochondrial-crista-junction-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2729
- finding_id: micro-F2
  issue_key: mitochondrial-derived-compartment-1
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Restore the cited Tom70/Tom71 experiment condition
  description: The Tom70/Tom71 double-deletion edge description calls the experiment
    rapamycin-induced, while its only cited source Hughes2016 Fig7C uses concanamycin
    A for2h in a dnm1Δ background. This conflicts with the graph scope promise that
    edges retain individual assay conditions. The source supports the dependency under
    ConcA, so this is a bounded attribution error rather than evidence that the dependency
    itself is false.
  target_ids:
  - cellstructuremech:mitochondrial_derived_compartment
  field_paths:
  - causal_graphs[0].edges[3].description
  evidence_ids:
  - micro-record-mitochondrial_derived_compartment
  - micro-PMC4889329-body
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/mitochondrial_derived_compartment.yaml
    role: maintained scientific record
  rule_id: .claude/skills/review-yaml-record/SKILL.md:exact identity and claim-level
    support
  native_severity: minor
  normalization_reason: Minor experimental-condition/source-attribution error; the
    supported direction and yeast-specific biological relationship remain intact.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T022241Z-mitochondrial-derived-compartment-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2730
actions:
- action_id: septin-maurer_s_cleft-A1
  finding_ids:
  - septin-maurer_s_cleft-F1
  target_ids:
  - GO:0020036
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/maurer_s_cleft.yaml
    role: maintained scientific record
  description: In separately authorized curation, narrow the Cooke-linked canonical
    note to SBP1 or represent the MAHRP1 clause with the exact Spycher2008 supporting
    source.
  acceptance_checks:
  - Cooke2006 is attached only to its SBP1 intervention and observed phenotype.
  - Any retained MAHRP1 genetic-test clause has Spycher2008 claim-level support; preserve
    correct P. falciparum identity and differing intervention effects.
- action_id: septin-microneme-A1
  finding_ids:
  - septin-microneme-F1
  target_ids:
  - GO:0020009
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/microneme.yaml
    role: maintained scientific record
  description: In separately authorized curation, represent collective lipid material
    with justified chemical grounding or reviewed label-only status, and retain the
    complete membrane as a structural part without an invalid molecular equivalence.
  acceptance_checks:
  - Retain GO0033163 for the whole membrane and correct has_part relation.
  - A LIPID component no longer asserts GO0033163 as its chemical identity; any graph
    component_ref has a defensible material-to-boundary meaning.
  - Do not invent microneme-specific lipid species or assembly requirements.
- action_id: septin-microneme-A2
  finding_ids:
  - septin-microneme-F2
  target_ids:
  - GO:0020009
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/microneme.yaml
    role: maintained scientific record
  description: In separately authorized curation, point the whole cohort/complex localization
    to the microneme or explicitly distinguish soluble/luminal portions from transmembrane
    and cytosolic domains.
  acceptance_checks:
  - Whole MIC2–M2AP and transmembrane AMA1 are not represented as wholly soluble lumen
    contents.
  - Preserve valid luminal M2AP/adhesive-domain context and source-supported microneme
    localization; do not infer detailed orientation for every cohort member.
- action_id: septin-microneme-A3
  finding_ids:
  - septin-microneme-F3
  target_ids:
  - GO:0020009
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/microneme.yaml
    role: maintained scientific record
  description: In separately authorized curation, narrow the canonical note to the1997
    experiment or attach the separately verified complex and PKG studies to their
    respective clauses.
  acceptance_checks:
  - The1997 citation is not the sole evidentiary support for later MIC2–M2AP or PKG
    experiments.
  - Preserve correct Toxoplasma identity and actual RH-derived contexts.
- action_id: plaque-t6-A1
  finding_ids:
  - plaque-t6-F1
  target_ids:
  - cellstructuremech:microsporidian_posterior_vacuole
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/microsporidian_posterior_vacuole.yaml
    role: maintained scientific record
  description: In separately authorized curation, Describe the actual microscopy modalities
    and imaged objects; support any direct V.necatrix posterior-vacuole example with
    an appropriately scoped primary source.
  acceptance_checks:
  - Match source-specific species, microscopy modality, imaged object and causal certainty.
  - Retain directly observed topology and cargo passage.
  - Run focused native schema and strict checks after scientific curation.
- action_id: plaque-t6-A2
  finding_ids:
  - plaque-t6-F2
  target_ids:
  - cellstructuremech:microsporidian_posterior_vacuole
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/microsporidian_posterior_vacuole.yaml
    role: maintained scientific record
  description: In separately authorized curation, Qualify the proposed vacuole-driven
    mechanism or restrict the enters edge to observed cargo passage, preserving the
    directly observed temporal relationship.
  acceptance_checks:
  - Match source-specific species, microscopy modality, imaged object and causal certainty.
  - Retain directly observed topology and cargo passage.
  - Run focused native schema and strict checks after scientific curation.
- action_id: micro-A1
  finding_ids:
  - micro-F1
  target_ids:
  - GO:0044284
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/mitochondrial_crista_junction.yaml
    role: maintained scientific record
  description: Replace the tomography attribution with the actually reported fluorescence
    and thin-section TEM/genetic analyses, or separately cite a genuine tomography
    study.
  acceptance_checks:
  - Preserve the supported biological scope and source experimental conditions.
  - Run focused native schema, strict and applicable graph/protein checks after separately
    authorized curation.
- action_id: micro-A2
  finding_ids:
  - micro-F2
  target_ids:
  - cellstructuremech:mitochondrial_derived_compartment
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/mitochondrial_derived_compartment.yaml
    role: maintained scientific record
  description: Replace the rapamycin attribution with the actual ConcA/fission-deficient
    assay context, or cite and accurately delimit a direct rapamycin experiment. Preserve
    the conditional dependency and formation-versus-release distinction.
  acceptance_checks:
  - Preserve the supported biological scope and source experimental conditions.
  - Run focused native schema, strict and applicable graph/protein checks after separately
    authorized curation.
limitations:
- 'Maurer cleft and microneme boundary trio independent subreview: Read-only independent
  source review of four assigned records. Root owns repository/GitHub writes, issue
  dedup/publication, global gates, CI and queue. No record or original artifact was
  edited and no future final-head/CI result is certified.'
- 'Maurer cleft and microneme boundary trio independent subreview: Maurer and microneme
  stale changes add REX1 and M2AP unreviewed examples plus history. Current identity/taxon/status/ORF
  names verify; biological membership is independently supported at cited experimental
  scope. A UniProt identity check is not causal or formation-necessity proof, and
  3D7/VEG/ME49 representative entries are not all exact RH experimental constructs.'
- 'Maurer cleft and microneme boundary trio independent subreview: Maurer has3UNREVIEWED
  examples/3distinct accessions and2COVERED nodes; Q6V0W9 is a fragment. Microneme
  has5occurrences/4distinct accessions because MIC2 repeats,2REVIEWED+3UNREVIEWED
  occurrences and2COVERED nodes. Lumen/membrane have0examples and0typednodes. All8native
  commands pass only these exact inventories.'
- 'Maurer cleft and microneme boundary trio independent subreview: Current REX1 and
  M2AP locus identifiers are ORF-name fields, not formal primary geneName fields.
  Correct common protein/locus identities support examples, but loose primary-name
  prose is not independently certified as an exact authority-field statement. No separate
  identity/causality defect is inferred from that phrasing alone.'
- 'Maurer cleft and microneme boundary trio independent subreview: Cooke genuine BioC
  main text was read through main adhesion-assay Methods, with all Results/Discussion
  and Figure1–7 captions; supplements and pixels were not inspected. SBP1 genetic
  trafficking effects remain distinct from Spycher MAHRP1 experiments and from direct
  protein binding.'
- 'Maurer cleft and microneme boundary trio independent subreview: Current Spycher
  saved source evidence is exact metadata/complete primary abstract. An initial successful
  browser view also displayed Summary/Introduction and Results through Figure5 before
  complementation heading; later direct403 and browser timeouts did not provide the
  rest. No saved complete-body hash, full-body access or exact timestamp for that
  unpersisted browser observation is invented; findings use saved primary abstract
  plus Cooke body.'
- 'Maurer cleft and microneme boundary trio independent subreview: Huynh2006 genuine
  BioC complete Introduction/Results/Discussion, Figure1–7 captions and enumerated
  plasmid/parasite/primer/Western/secretion/invasion Methods were read; Table1 numerical
  contents, pixels/videos/supplements and unenumerated Methods were not inspected.
  Residual invasion, RH-derived strain and unchanged other microneme cargos limit
  necessity claims.'
- 'Maurer cleft and microneme boundary trio independent subreview: Carruthers1997,Huynh2003,Brown2016
  and the7exact protein-location PMIDs are complete primary-abstract evidence in this
  current review; their full-text fallback attempts failed or returned service packets.
  Carruthers2008 and Lanzer2006 are complete secondary abstracts only. Blisnick2000
  is complete primary abstract only. Unavailable body access is not scientific refutation.'
- 'Maurer cleft and microneme boundary trio independent subreview: Dubois2019 accepted
  review manuscript was read only through extracted text lines40–578 (Abstract through
  signaling cascade). Later sections, Table1 and figures/pixels were not comprehensively
  inspected. It is secondary synthesis, not direct reanalysis of every primary experiment,
  and no reuse licence or image claim is inferred.'
- 'Maurer cleft and microneme boundary trio independent subreview: Exact single-accession
  InterPro lookups and exact reviewed gene queries have bounded scopes; absence in
  an endpoint is not biological absence. SBP1 automatic Mediator-like hit is not adopted
  as exact family identity; heterogeneous protein classes are allowed. Native CausalNode
  explicitly allows protein complexes under GENE_OR_PROTEIN, so MIC2-M2AP node type
  is not a new finding.'
- 'Maurer cleft and microneme boundary trio independent subreview: All4original adapter
  rows are explicit expression-only exclusions, not omissions. Whole molecular/pathway
  narratives require coverage assessment, including the otherwise sparse lumen/membrane.
  Fresh complete official catalogue contains no matching parasite host; no unrelated
  bacterial downstream query or biological absence claim. Runner receipt remains actual00:49Zhistorical
  failure, not a new invocation.'
- 'Maurer cleft and microneme boundary trio independent subreview: Twenty-nine repository
  inputs were actually used:17common policy/schema/native files,4current targets and8original
  artifacts. The microneme trio supplies mutually assigned boundary context without
  extra unfrozen neighbors. Original findings are retained exactly for their own targets;
  no neighboring/group/category issue is newly resolved. No maintained image, measured
  physical property, trait or verbatim snippet is asserted.'
- 'Methane-oxidizing organelle, micronucleus and posterior vacuole independent subreview:
  Assigned source review covers methane-oxidizing organelle, micronucleus and posterior
  vacuole. One stale methane target was substantively refreshed; first two scientifically
  pass_with_limitations, posterior needs_curation for two inherited minor findings.
  No new scientific finding or fabricated predecessor.'
- 'Methane-oxidizing organelle, micronucleus and posterior vacuole independent subreview:
  Original three pairs native validate/render with14/16/14 historical input hashes
  matching retained source. No original mutated. Historical record fixes/issues1290/778
  are not terminally re-adjudicated; optional DNA/composition grounding gaps are not
  automatically required defects.'
- 'Methane-oxidizing organelle, micronucleus and posterior vacuole independent subreview:
  Current policies were hash-compared to the independently read PR2368 set and unchanged.
  Record-review skill/profile and CausalNode contract freshly reread; protein-complex
  use of GENE_OR_PROTEIN is explicitly permitted. No automatic graph retyping issue.'
- 'Methane-oxidizing organelle, micronucleus and posterior vacuole independent subreview:
  Methane sources Zhu2022 andWhiddon2019 are genuine primary JATS selected sections/captions
  as evidence locators state; no figure pixels/raw data assessed. Bath arrays and20Z
  fluorescence contexts remain distinct; static continuity/array activity correlation
  is not full biogenesis or causal sufficiency.'
- 'Methane-oxidizing organelle, micronucleus and posterior vacuole independent subreview:
  Stolyar2001 full body routes returned404/no-result despite BioC HTTP200; complete
  primary abstract supports only narrow gene-expression note. Three native localization
  PMIDs assessed as complete abstracts/native evidence-pointer verification; Smith2011
  Methylocystis strainM is not substituted for Bath direct experiment.'
- 'Methane-oxidizing organelle, micronucleus and posterior vacuole independent subreview:
  Q603F1 is unreviewed Bath pmoC1 identity with two locus names, not exact membership/unique
  locus/necessity evidence. Exact pmoC searches returnedzero, primary pmoC1 search
  foundQ603F1; alias boundary is not biological absence. No guessed chemical/complex/family
  CURIE was added.'
- 'Methane-oxidizing organelle, micronucleus and posterior vacuole independent subreview:
  Hamilton selected Introduction, assembly Results and Methods were read; no raw sequencing
  or figure-pixel assessment. Mature MIC scope retains assembly uncertainties and
  does not claim absence of all developmental transcription.'
- 'Methane-oxidizing organelle, micronucleus and posterior vacuole independent subreview:
  Findley2005 selected p111–115 PDF text, Troemel2015 mainbody and Jaroenlak2020/Sharma2024
  selected primary bodies/captions establish posterior topology and the two narrow
  source/causal defects. No figure pixels/videos/raw tomograms inspected for these
  targets;2022 secondary chapter abstract only. No quantified phylum prevalence or
  exact swelling mechanism established.'
- 'Methane-oxidizing organelle, micronucleus and posterior vacuole independent subreview:
  Only methane and micronucleus original exclusions are adapter defects in this slice.
  Posterior has genuine sparse morphology/physical-physiological scope with unresolved
  molecular composition. Fresh official catalogue has no exact represented hosts;
  no matched downstream module query applies, and unrelated bacterial/archaeal coverage
  is not a proxy.'
- 'Methane-oxidizing organelle, micronucleus and posterior vacuole independent subreview:
  Historical00:49Z runner PermissionError remains historical unavailable, not a fresh
  failed/successful run. Actual six native protein commands pass with methane3examples(2reviewed1unreviewed)/1coverednode
  and other2records0/0. Native empty coverage does not waive positive molecular assertions.'
- 'Methane-oxidizing organelle, micronucleus and posterior vacuole independent subreview:
  Auxiliary MDC FigureS1 challenge was separately scoped and receipt-bound: independent
  pixels and caption support µm; proposed axis contradiction rejected. That fourth
  local target was already frozen and used only for its physical-property note, not
  given a new full-record verdict.'
- 'Methane-oxidizing organelle, micronucleus and posterior vacuole independent subreview:
  Root owns global gates, issue publication and final lifecycle. This report does
  not precertify final-head CI/merge. Scratch native preflight establishes contract
  validity, not automatic scientific truth. All reviewer writes are scratch only.'
- 'Mitochondrial crista, crista junction and derived compartment independent subreview:
  Assigned scope: three complete mitochondrial records only. Junction stale MICOS
  typing/history substantively reassessed; crista and MDC current bytes unchanged.
  Exactly two inherited minor scientific findings retain repository/review/F1 predecessors.
  Closed grouped2419 is historical context only.'
- 'Mitochondrial crista, crista junction and derived compartment independent subreview:
  All current public source reads have actual fresh receipt timestamps and exact locators.
  Body reading is restricted to listed sections; Davies/Paumard S3 archive404 responses
  are not scientific text, while genuine PMC HTML was successfully read. Friedman2014
  is secondary context. No unseen full body or raw experimental reanalysis claimed.'
- 'Mitochondrial crista, crista junction and derived compartment independent subreview:
  Only Wilson2024 Figure1/FigureS1 actual pixels were inspected. Caption/Methods/license
  and shape-specific means agree; a proposed axis contradiction was withdrawn after
  independent challenge and own original-detail review. No image-related finding remains.
  Movies, raw tomography, lipidomics and other figure pixels/supplement datasets were
  not reanalyzed.'
- 'Mitochondrial crista, crista junction and derived compartment independent subreview:
  General Eukaryota prevalence, precise GO taxon constraints and reduced anaerobic-lineage
  exceptions remain bounded unknowns at inspected extent. This is not a biological
  refutation or universal absence inference.'
- 'Mitochondrial crista, crista junction and derived compartment independent subreview:
  Native verifier has0examples/0typed nodes for crista and junction, with the junction
  STRUCTURE-node Mic60 xref independently verified; MDC has3examples/0typed nodes.
  Success is not experimental localization, association, or formation necessity. Exact
  reviewed strain searches are bounded to stated query/date/result limits.'
- 'Mitochondrial crista, crista junction and derived compartment independent subreview:
  2020/2024 lipid-perturbation differences remain unresolved.2026 preprint models
  retain preprint status and limited access; current publisher metadata is not certification
  of unread Results. Conditional dependencies, partial bypass, cargo enrichment and
  permanent isolation remain distinct.'
- 'Mitochondrial crista, crista junction and derived compartment independent subreview:
  All three explicit original source-adapter exclusions need corrected rationale;
  fresh catalogue lacks the actual yeast hosts, so no matched downstream module check
  applies. Historical00:49Z runner failure remains historical, not a fresh invocation.'
- 'Mitochondrial crista, crista junction and derived compartment independent subreview:
  Read-only repository/Git/GitHub review. Root owns global QC, final CI, issue dedup
  and publication; no future gate result borrowed. Native scripts are frozen execution
  inputs with selected coverage-filter inspection, not exhaustive code review. Curation
  actions are proposed separately; no maintained record/status/history was edited.'
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
- This explicit issue-bearing ten-record cohort follows native persistence policy.
  Inherited scientific findings retain stable keys and exact predecessor repository/review/finding
  identities; any new finding has no invented predecessor.
- 'Issue2721 tracks four stale targets: added REX1/Q8I2G1 at Maurer cleft, pmoC1/Q603F1
  at methane-oxidizing organelle, M2AP/S8GDJ1 at microneme, and MICOS STRUCTURE retyping
  at crista junction. Native identities, status, taxonomy, membership and complex/subunit
  scope are substantively reassessed.'
- Issue2722 tracks nine unsupported expression-only applicability exclusions. The
  posterior-vacuole record has a genuine sparse physical-topology/expansion exclusion
  with composition unresolved, not a tenth invented defect. All ten originals contained
  explicit exclusions; none was missing.
- Source commit 61d3617ae8700b99198e2aaf01f3b2437933de6c is retained by tag review-base/pr2369-current-record-followup-20261103.
- CLAUDE.md aliases AGENTS.md; canonical regular AGENTS.md bytes are frozen. Every
  used local context input is frozen before its assessment.
- Fresh and reused source snapshots retain actual access times and inspection tiers.
  Native identifier identity does not independently establish structure membership,
  experimental intervention scope or assembly necessity.
- All twenty native protein commands returned zero. Maurer cleft has three unreviewed
  examples and two COVERED nodes; methane organelle has two reviewed and one unreviewed
  examples with one COVERED node; microneme has five example occurrences across four
  distinct accessions (two reviewed and three unreviewed occurrences) and two COVERED
  nodes. MIC2 appears in two distinct component contexts. MDC has three reviewed examples
  and zero typed molecular nodes. The other six targets have no examples or typed
  molecular nodes. Native success does not certify every narrative claim.
- Current CausalNode schema explicitly permits protein families and complexes as GENE_OR_PROTEIN
  nodes. The pMMO and MIC2-M2AP node enums alone are not scientific defects. Existing
  material-to-membrane identity and whole-complex lumen topology concerns are assessed
  separately.
- Closed grouped issue2419 is historical context for the crista-junction MICOS node
  change. No broad disposition of the five grouped records or their findings is made.
  Native-validator2514 remains open and reused.
- Final trusted-base review-check, exact-head independent acceptance, final-head CI
  and merge-group CI occur after this immutable observation and are not represented
  as already completed.
- A tentative FigureS1 axis-provenance contradiction was independently challenged
  and withdrawn after exact full-resolution pixel inspection. The axis reads micrometers
  and agrees with the caption’s 0.36 micrometers (n49); no scientific or bundle finding
  is created from the initial glyph misread. The separate assay-condition finding
  remains.
- After MICOS retyping, the native protein verifier skips xrefs on the crista-junction
  STRUCTURE node. Its zero-example/zero-typed-node pass therefore does not validate
  Mic60/P36112; the independent reviewer separately inspects fresh authority identity
  and treats that xref as a representative subunit, not whole-complex equivalence.
- The final scientific set consists of eight inherited findings (one major, seven
  minor) on Maurer cleft, microneme, posterior vacuole, crista junction and MDC. Five
  other targets retain qualified passes. No new finding or predecessor is invented,
  and scientific curation remains open separately from the two bundle fixes.
- Scientific findings are tracked as issues2723–2730, in exact finding-key order recorded
  in the issue ledger; all remain open. Bundle fixes2721/2722 do not close scientific
  curation. Existing validator2514 remains reused, and closed grouped2419 remains
  historical context only.
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T022231Z-maurer-s-cleft-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T022232Z-methane-oxidizing-organelle-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T022233Z-microneme-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T022235Z-microneme-lumen-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T022236Z-microneme-membrane-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T022237Z-micronucleus-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T022238Z-microsporidian-posterior-vacuole-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T022238Z-mitochondrial-crista-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T022239Z-mitochondrial-crista-junction-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T022241Z-mitochondrial-derived-compartment-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
links:
- https://github.com/CultureBotAI/CellStructureMech/pull/2369
- https://github.com/CultureBotAI/CellStructureMech/issues/2419
- https://github.com/CultureBotAI/CellStructureMech/issues/2514
- https://github.com/CultureBotAI/CellStructureMech/issues/2721
- https://github.com/CultureBotAI/CellStructureMech/issues/2722
- https://github.com/CultureBotAI/CellStructureMech/issues/2723
- https://github.com/CultureBotAI/CellStructureMech/issues/2724
- https://github.com/CultureBotAI/CellStructureMech/issues/2725
- https://github.com/CultureBotAI/CellStructureMech/issues/2726
- https://github.com/CultureBotAI/CellStructureMech/issues/2727
- https://github.com/CultureBotAI/CellStructureMech/issues/2728
- https://github.com/CultureBotAI/CellStructureMech/issues/2729
- https://github.com/CultureBotAI/CellStructureMech/issues/2730
```
