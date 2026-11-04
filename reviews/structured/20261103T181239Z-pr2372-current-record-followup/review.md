# PR 2372: current-input review of ten records and adversarial follow-up

- Review: 20261103T181239Z-pr2372-current-record-followup
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-11-03T18:01:05.412555Z
- Finished UTC: 2026-11-03T18:12:39Z
- Reviewer: Codex root synthesis with three independent read-only adversarial reviewers (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Current-input adversarial follow-up for the complete ten-record cohort after merging main. One stale organellar chromatophore review is substantively refreshed against its added thylakoid-membrane parthood edge and source scopes. Eight unsupported expression-only structured-source exclusions are corrected; nuclear envelope lumen and nuclear net retain genuine physical/topology exclusions. Two inherited rationale-only findings are explicitly rejected under native historical-provenance policy. Four other inherited findings remain open (two major and two minor) across three records; seven targets retain qualified positive assessments. All original review observations and scientific records remain unchanged.

## Scope And Provenance

Exact ten-record PR cohort reassessed against current main c32b945b410050078133707a85f58ed8206ec5cc. Changed inputs are substantively reassessed. Scientific records remain unchanged.

Selection: Complete cohort of ten maintained records reviewed in original PR head 1552d23408ac2c2ba304241fdd8b465fb8256820.
Coverage: full; 10 reviewed / 10 in the declared population.
Source: working_tree at Git base e2edc3550e41792c2bb6f24eb2918b7d33d8a58c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:nitroplast | data/structures/membrane_organelle/nitroplast.yaml | maintained | nitroplast |
| GO:0005635 | data/structures/membrane_organelle/nuclear_envelope.yaml | maintained | nuclear envelope |
| GO:0005641 | data/structures/membrane_organelle/nuclear_envelope_lumen.yaml | maintained | nuclear envelope lumen |
| GO:0005637 | data/structures/membrane_organelle/nuclear_inner_membrane.yaml | maintained | nuclear inner membrane |
| GO:0031981 | data/structures/membrane_organelle/nuclear_lumen.yaml | maintained | nuclear lumen |
| cellstructuremech:nuclear_net | data/structures/membrane_organelle/nuclear_net.yaml | maintained | nuclear net |
| GO:0005640 | data/structures/membrane_organelle/nuclear_outer_membrane.yaml | maintained | nuclear outer membrane |
| GO:0033009 | data/structures/membrane_organelle/nucleomorph.yaml | maintained | nucleomorph |
| GO:0005634 | data/structures/membrane_organelle/nucleus.yaml | maintained | nucleus |
| GO:0070111 | data/structures/membrane_organelle/organellar_chromatophore.yaml | maintained | organellar chromatophore |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full native QC | passed | True | cellstructuremech:nitroplast, GO:0005635, GO:0005641, GO:0005637, GO:0031981, cellstructuremech:nuclear_net, GO:0005640, GO:0033009, GO:0005634, GO:0070111 | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| Native label correspondence | passed | True | cellstructuremech:nitroplast, GO:0005635, GO:0005641, GO:0005637, GO:0031981, cellstructuremech:nuclear_net, GO:0005640, GO:0033009, GO:0005634, GO:0070111 | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| TraitMech references | passed | True | cellstructuremech:nitroplast, GO:0005635, GO:0005641, GO:0005637, GO:0031981, cellstructuremech:nuclear_net, GO:0005640, GO:0033009, GO:0005634, GO:0070111 | Native TraitMech link check passed. |
| Pinned governed files | passed | True | cellstructuremech:nitroplast, GO:0005635, GO:0005641, GO:0005637, GO:0031981, cellstructuremech:nuclear_net, GO:0005640, GO:0033009, GO:0005634, GO:0070111 | Pinned governed files match; native vendored check passed. |
| Native identifier resolver | passed | True | cellstructuremech:nitroplast, GO:0005635, GO:0005641, GO:0005637, GO:0031981, cellstructuremech:nuclear_net, GO:0005640, GO:0033009, GO:0005634, GO:0070111 | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| validate cellstructuremech:nitroplast | passed | True | cellstructuremech:nitroplast | Documented focused command passed. |
| validate-strict cellstructuremech:nitroplast | passed | True | cellstructuremech:nitroplast | Documented focused command passed. |
| validate GO:0005635 | passed | True | GO:0005635 | Documented focused command passed. |
| validate-strict GO:0005635 | passed | True | GO:0005635 | Documented focused command passed. |
| validate GO:0005641 | passed | True | GO:0005641 | Documented focused command passed. |
| validate-strict GO:0005641 | passed | True | GO:0005641 | Documented focused command passed. |
| validate GO:0005637 | passed | True | GO:0005637 | Documented focused command passed. |
| validate-strict GO:0005637 | passed | True | GO:0005637 | Documented focused command passed. |
| validate GO:0031981 | passed | True | GO:0031981 | Documented focused command passed. |
| validate-strict GO:0031981 | passed | True | GO:0031981 | Documented focused command passed. |
| validate cellstructuremech:nuclear_net | passed | True | cellstructuremech:nuclear_net | Documented focused command passed. |
| validate-strict cellstructuremech:nuclear_net | passed | True | cellstructuremech:nuclear_net | Documented focused command passed. |
| validate GO:0005640 | passed | True | GO:0005640 | Documented focused command passed. |
| validate-strict GO:0005640 | passed | True | GO:0005640 | Documented focused command passed. |
| validate GO:0033009 | passed | True | GO:0033009 | Documented focused command passed. |
| validate-strict GO:0033009 | passed | True | GO:0033009 | Documented focused command passed. |
| validate GO:0005634 | passed | True | GO:0005634 | Documented focused command passed. |
| validate-strict GO:0005634 | passed | True | GO:0005634 | Documented focused command passed. |
| validate GO:0070111 | passed | True | GO:0070111 | Documented focused command passed. |
| validate-strict GO:0070111 | passed | True | GO:0070111 | Documented focused command passed. |
| Supplemental bounded PMID authority checks | passed | True | cellstructuremech:nitroplast, GO:0005635, GO:0005641, GO:0005637, GO:0031981, cellstructuremech:nuclear_net, GO:0005640, GO:0033009, GO:0005634, GO:0070111 | 909 PMIDs all OK in bounded native requests; full-command limitations remain separate. |
| Official structured-source applicability and covered-dataset cross-checks | passed | False | cellstructuremech:nitroplast, GO:0005635, GO:0005641, GO:0005637, GO:0031981, cellstructuremech:nuclear_net, GO:0005640, GO:0033009, GO:0005634, GO:0070111 | Eight records make positive molecular/pathway claims and require applicability assessment: nitroplast, nuclear envelope, nuclear inner membrane, nuclear lumen, nuclear outer membrane, nucleomorph, nucleus and organellar chromatophore. Complete current official iModulonDB catalogue responses provide no exact applicable eukaryotic host/strain or UCYN-A symbiont dataset; unrelated bacterial or Synechococcus datasets are not used as proxies. Nuclear envelope lumen and nuclear net retain genuine material/topology scope with molecular mechanisms excluded or withheld. Historical00:49Z runner unavailability stays historical; current public-source fallback records its actual search scope and does not imply biological absence. |
| Independent claim-level source review | passed | True | cellstructuremech:nitroplast, GO:0005635, GO:0005641, GO:0005637, GO:0031981, cellstructuremech:nuclear_net, GO:0005640, GO:0033009, GO:0005634, GO:0070111 | Three read-only reviewers covered the complete ten-record cohort, including changed inputs, with explicit scientific findings and source-access limits. Final artifact/head acceptance occurs after saving. |
| Retained historical adapter runner availability | unavailable | False | cellstructuremech:nitroplast, GO:0005635, GO:0005641, GO:0005637, GO:0031981, cellstructuremech:nuclear_net, GO:0005640, GO:0033009, GO:0005634, GO:0070111 | Historical 00:49Z invocation unavailable due to OS access restriction. Official catalogue source fallback was inspected separately; no current invocation or successful adapter execution is claimed. The actual historical exit code 1 is retained in the evidence receipt, since the native unavailable-check model has no execution exit-code field. |
| Native nitroplast UniProt verify check | passed | True | cellstructuremech:nitroplast | Read-only native command returned zero. No protein examples or typed molecular nodes. Positive molecular/pathway assertions and genuine physical-scope exclusions are assessed separately. |
| Native nitroplast UniProt causal check | passed | True | cellstructuremech:nitroplast | Read-only native command returned zero. No protein examples or typed molecular nodes. Positive molecular/pathway assertions and genuine physical-scope exclusions are assessed separately. |
| Native nuclear envelope UniProt verify check | passed | True | GO:0005635 | Read-only native command returned zero. No protein examples or typed molecular nodes. Positive molecular/pathway assertions and genuine physical-scope exclusions are assessed separately. |
| Native nuclear envelope UniProt causal check | passed | True | GO:0005635 | Read-only native command returned zero. No protein examples or typed molecular nodes. Positive molecular/pathway assertions and genuine physical-scope exclusions are assessed separately. |
| Native nuclear envelope lumen UniProt verify check | passed | True | GO:0005641 | Read-only native command returned zero. No protein examples or typed molecular nodes. Positive molecular/pathway assertions and genuine physical-scope exclusions are assessed separately. |
| Native nuclear envelope lumen UniProt causal check | passed | True | GO:0005641 | Read-only native command returned zero. No protein examples or typed molecular nodes. Positive molecular/pathway assertions and genuine physical-scope exclusions are assessed separately. |
| Native nuclear inner membrane UniProt verify check | passed | True | GO:0005637 | Read-only native command returned zero. No protein examples; three UNANCHORED_WITH_UNIPROT typed nodes. Native identifier presence is separate from full Kap60/Kap95 system identity and source-supported Heh1p/Heh2p targeting. |
| Native nuclear inner membrane UniProt causal check | passed | True | GO:0005637 | Read-only native command returned zero. No protein examples; three UNANCHORED_WITH_UNIPROT typed nodes. Native identifier presence is separate from full Kap60/Kap95 system identity and source-supported Heh1p/Heh2p targeting. |
| Native nuclear lumen UniProt verify check | passed | True | GO:0031981 | Read-only native command returned zero. No protein examples or typed molecular nodes. Positive molecular/pathway assertions and genuine physical-scope exclusions are assessed separately. |
| Native nuclear lumen UniProt causal check | passed | True | GO:0031981 | Read-only native command returned zero. No protein examples or typed molecular nodes. Positive molecular/pathway assertions and genuine physical-scope exclusions are assessed separately. |
| Native nuclear net UniProt verify check | passed | True | cellstructuremech:nuclear_net | Read-only native command returned zero. No protein examples or typed molecular nodes. Positive molecular/pathway assertions and genuine physical-scope exclusions are assessed separately. |
| Native nuclear net UniProt causal check | passed | True | cellstructuremech:nuclear_net | Read-only native command returned zero. No protein examples or typed molecular nodes. Positive molecular/pathway assertions and genuine physical-scope exclusions are assessed separately. |
| Native nuclear outer membrane UniProt verify check | passed | True | GO:0005640 | Read-only native command returned zero. No protein examples; two UNANCHORED_WITH_UNIPROT typed nodes. Native identifier presence is separate from source-specific Nvj1p/Vac8p localization, intervention and junction evidence. |
| Native nuclear outer membrane UniProt causal check | passed | True | GO:0005640 | Read-only native command returned zero. No protein examples; two UNANCHORED_WITH_UNIPROT typed nodes. Native identifier presence is separate from source-specific Nvj1p/Vac8p localization, intervention and junction evidence. |
| Native nucleomorph UniProt verify check | passed | True | GO:0033009 | Read-only native command returned zero. No protein examples or typed molecular nodes. Positive molecular/pathway assertions and genuine physical-scope exclusions are assessed separately. |
| Native nucleomorph UniProt causal check | passed | True | GO:0033009 | Read-only native command returned zero. No protein examples or typed molecular nodes. Positive molecular/pathway assertions and genuine physical-scope exclusions are assessed separately. |
| Native nucleus UniProt verify check | passed | True | GO:0005634 | Read-only native command returned zero. No protein examples or typed molecular nodes. Positive molecular/pathway assertions and genuine physical-scope exclusions are assessed separately. |
| Native nucleus UniProt causal check | passed | True | GO:0005634 | Read-only native command returned zero. No protein examples or typed molecular nodes. Positive molecular/pathway assertions and genuine physical-scope exclusions are assessed separately. |
| Native organellar chromatophore UniProt verify check | passed | True | GO:0070111 | Read-only native command returned zero. No protein examples or typed molecular nodes. Positive molecular/pathway assertions and genuine physical-scope exclusions are assessed separately. |
| Native organellar chromatophore UniProt causal check | passed | True | GO:0070111 | Read-only native command returned zero. No protein examples or typed molecular nodes. Positive molecular/pathway assertions and genuine physical-scope exclusions are assessed separately. |

## Scientific And Domain Assessments

### Original native validation/render and source binding

schema: supported. Targets: cellstructuremech:nitroplast.

Original native validation/render passes with exact Markdown and verified historical target hash. Current target remains byte-identical to its historical review input. Schema success is not a scientific verdict.

### Actual molecular identifier coverage

provenance: supported. Targets: cellstructuremech:nitroplast.

Both native commands exit0 over independently verified zero examples/typed molecular nodes/UniProt graph xrefs. Narrative proteins/pathways still require scientific review; generic success does not establish inventory completeness.

### Full-claim molecular applicability and matched catalogue

scope: supported. Targets: cellstructuremech:nitroplast.

Nitrogenase/NifH, nitrogen fixation, host-protein import and uTP claims trigger the native structured-source assessment. The original expression-only rationale is insufficient. Fresh complete catalogue has no matched host/endosymbiont; downstream gene/module calls are not applicable to unmatched taxa. Current primary/authority fallback is explicit, historical runner failure retains its actual time.

### Original native validation/render and source binding

schema: supported. Targets: GO:0033009.

Original native validation/render passes with exact Markdown and verified historical target hash. Current target remains byte-identical to its historical review input. Schema success is not a scientific verdict.

### Actual molecular identifier coverage

provenance: supported. Targets: GO:0033009.

Both native commands exit0 over independently verified zero examples/typed molecular nodes/UniProt graph xrefs. Narrative proteins/pathways still require scientific review; generic success does not establish inventory completeness.

### Full-claim molecular applicability and matched catalogue

scope: supported. Targets: GO:0033009.

Residual essential genes, replication and host cell-cycle coordination trigger the native structured-source assessment. The original expression-only rationale is insufficient. Fresh complete catalogue has no matched host/endosymbiont; downstream gene/module calls are not applicable to unmatched taxa. Current primary/authority fallback is explicit, historical runner failure retains its actual time.

### Original native validation/render and source binding

schema: supported. Targets: GO:0070111.

Original native validation/render passes with exact Markdown and verified historical target hash. Current chromatophore differs by a graph-parthood edge and curation event; frozen current bytes are fully reassessed. Schema success is not a scientific verdict.

### Actual molecular identifier coverage

provenance: supported. Targets: GO:0070111.

Both native commands exit0 over independently verified zero examples/typed molecular nodes/UniProt graph xrefs. Narrative proteins/pathways still require scientific review; generic success does not establish inventory completeness.

### Full-claim molecular applicability and matched catalogue

scope: supported. Targets: GO:0070111.

Photosynthesis, protein import and thylakoid light-complex claims trigger the native structured-source assessment. The original expression-only rationale is insufficient. Fresh complete catalogue has no matched host/endosymbiont; downstream gene/module calls are not applicable to unmatched taxa. Current primary/authority fallback is explicit, historical runner failure retains its actual time.

### Local organelle identity and boundary

identity: supported. Targets: cellstructuremech:nitroplast.

A compartment identity is distinguished from the host/cyanobacterial taxon and frozen diazoplast neighbor. Bounded exact GO search supports local identity with broad intracellular-organelle parent; related UCYN-A spheroid-body wording is qualified by host/import scope.

### Verified host, strain and qualitative variation

scope: supported. Targets: cellstructuremech:nitroplast.

Current taxon373042 and Hagino genotypeIII/FR12/FR21 mapping agree. Coale supplement identifies FR21=NIES4399; KC1-P2 culture loss supports cautious VARIABLE occurrence, not an environmental frequency or proven loss mechanism.

### Collective membrane OTHER and nitrogenase complex

grounding: supported. Targets: cellstructuremech:nitroplast.

Membrane GO0016020 is deliberately structural OTHER, supported by native structural-constituent precedent and actual lamellar images. Nitrogenase GO0016610 is a proper complex identity; NifH enrichment/activity support membership without asserting exact subunits or stoichiometry.

### Formation essentiality remains untested

evidence: unknown. Targets: cellstructuremech:nitroplast.

Both components retain UNKNOWN assembly essentiality. Source localization, enrichment and acetylene reduction do not establish an organelle-formation knockout, molecular stoichiometry or a specific import apparatus.

### Nitrogen fixation experimental scope

evidence: supported. Targets: cellstructuremech:nitroplast.

Relative daytime acetylene reduction in triplicate FR21 culture supports nitrogenase activity and the nitrogen-fixation function. Whole-culture measurements are not claimed as isolated-organelle flux or raw isotopic transfer measurements.

### Import evidence and prediction boundary

evidence: supported. Targets: cellstructuremech:nitroplast.

Enrichment-based host-protein import and coordinated division support the organelle description. Predicted-only uTP candidates remain excluded; no proven uTP cleavage, translocon identity, mitochondrial ATP delivery or candidate-specific causal role is asserted.

### Transport discussion preserves preprint limits

evidence: supported. Targets: cellstructuremech:nitroplast.

Current XML identifies Li2026 version1 as a preprint. Its discussion explicitly withholds cargo/direction/substrate identification and mechanistic proof from static architecture. The record leaves this open and adds no invented density identity or transport edge.

### Actually inspected TEM panels and copyright

provenance: supported. Targets: cellstructuremech:nitroplast.

Fresh genuine PDF and actual pixel inspection verify FR21 Fig28/29, Nit labels and1um scale; adjacent OTR22-B Fig30/31 is excluded. Copyright appears on the article first page (PDF2). Link-only OTHER/attribution is appropriate; no redistribution permission is inferred.

### Qualified sparse record, history and absent graph

completeness: supported. Targets: cellstructuremech:nitroplast.

PROPOSED history and explicit resolved/open discussion boundaries remain coherent. No causal graph, protein examples, associated trait, numeric measurement field or verbatim snippet requires invented completion. Optional graph/protein absence is not a defect.

### Current scientific verdict

completeness: supported. Targets: cellstructuremech:nitroplast.

pass_with_limitations: no confirmed scientific finding, with source/prediction/preprint/formation and empty-native-coverage limits retained. Applicability bundle correction is separate.

### Exact nucleus identity, synonymy and parthood

identity: supported. Targets: GO:0033009.

GO0033009 matches the vestigial eukaryotic nucleus. GO0043231 parent and GO0009536 plastid parthood are distinct; red/green endosymbiont origins and residual/remnant nucleus synonymy are supported by Tanifuji background and Curtis abstract.

### Taxa and canonical examples

scope: supported. Targets: GO:0033009.

Cryptophyceae3027, Chlorarachniophyceae29197, G.theta55529 and B.natans227086 match authority. Qualitative COMMON is not a numeric survey; precise experimental scope is G.theta CCMP2712 and comparative L.oceanica CCMP622, not every strain.

### Collective chromosome DNA and label-only identity

grounding: supported. Targets: GO:0033009.

Tanifuji directly resolves three linear chromosomes in L.oceanica, with repeat-size uncertainty. DNA constituent remains reviewed-label-only instead of a guessed exact chromosome CURIE. ESSENTIAL describes the collectively retained genome, not each chromosome/gene universally required for organelle assembly.

### Individual formation requirements untested

evidence: unknown. Targets: GO:0033009.

Sequence retention and essential-gene evolutionary interpretation do not establish individual chromosome/gene depletion, division machinery or an envelope-formation pathway. Optional machinery and exact cross-lineage constituents remain explicitly open.

### Cell-cycle replication measured at bounded scope

evidence: supported. Targets: GO:0033009.

Onuma localization and EdU experiments support the G.theta replication example. The experiment is only partially synchronized and nucleomorph replication is later/longer than nuclear synthesis. Functional edge explicitly names G.theta; scope_notes call it an example, so the general graph description is read in that bounded context.

### All four descriptive genome-retention edges

graph: supported. Targets: GO:0033009.

Chromosomes housed in nucleomorph, nucleomorph part_of plastid, residual essential genes encoded, and G.theta replication example have direct cited support. NONMECHANISTIC scope excludes envelope/replication machinery. No causal intervention or universal phase identity is inferred.

### Actual access tiers and historical boundaries

provenance: supported. Targets: GO:0033009.

Curtis is complete abstract only after publisher challenge; Tanifuji and Onuma are genuine body sections and captions, not pixels or raw sequence/EdU reanalysis. Historical519/520 curation and open inventory TODO are context, not newly resolved issues. No image/trait/snippet scope occurs.

### Current scientific verdict

completeness: supported. Targets: GO:0033009.

pass_with_limitations: no confirmed new finding; preserve collective-versus-individual necessity, experimental scope, abstract/body access and empty-native coverage. Applicability bundle correction is separate.

### Exact organelle, synonym, plastid and parts

identity: supported. Targets: GO:0070111.

GO0070111 and SL0351 support exact organelle identity, Paulinella-type synonym and plastid class. Exact membrane/IMS/thylakoid/lumen identities remain structural parts, not chemical lipids. Hierarchy paths are distinguished from direct source relations.

### Paulinella source and strain scope

scope: supported. Targets: GO:0070111.

NCBITaxon39717 matches P.chromatophora; Nowack2012 uses CCAC0185, subisolate M0880/a. Secondary Nowack2014/Gabr2020 abstracts supply qualitative context, not numerical COMMON prevalence or all-strain import equivalence.

### Inherited F1 whole-membrane molecular grounding

grounding: concern. Targets: GO:0070111.

Three LIPID rows identify whole GO membranes and are joined to STRUCTURE graph nodes. This remains the original major F1. Preserve anatomical parts; separately curate structural types or supported chemical materials without guessed lipid identifiers.

### Supported residual wall and unresolved chemical detail

grounding: supported. Targets: GO:0070111.

SL0351 directly places residual peptidoglycan between envelope membranes. Label-only status and UNKNOWN necessity avoid unsupported exact polymer chemistry and assembly claims; import machinery remains an explicit TODO.

### Bounded demonstrated import and inferred routes

evidence: supported. Targets: GO:0070111.

Nowack experimental localization/PSI purification/labelling supports nuclear-protein import. Singer complete abstract corroborates wider import but combines experimental and predicted catalogue entries. The maintained record does not assert a complete translocon or proven Golgi route.

### Inherited F2 GO definition scope

evidence: concern. Targets: GO:0070111.

GO0070118 defines the thylakoid bilayer, not a light-reaction-complex system. Component note expands this to an internal photosynthetic system and graph edge3 explicitly credits GO with light complexes. Keep original F2 fields and attach inspected primary PSI evidence to the biological claim.

### Substantive refresh of new thylakoid parthood edge

graph: supported. Targets: GO:0070111.

Current edge5 correctly states the transitive GO route0070118→0070116→0070111; it does not falsely call this direct. SL0351 supplies broader whole-organelle thylakoid context, not an exact membrane definition. Nowack localization/topology supports the internal photosynthetic system. New curation event records this topology addition; no new scientific finding is established.

### Full current six-edge topology/function graph

graph: supported. Targets: GO:0070111.

Outer/inner boundaries, retained wall, thylakoid photosynthetic support, import and new parthood are scientifically coherent at NONMECHANISTIC scope. Existing molecular joins and source-note defects remain F1/F2; no complete machinery or individual necessity is certified.

### Formation evidence remains unknown

evidence: unknown. Targets: GO:0070111.

All component essentialities remain UNKNOWN. Imported protein association and anatomical descriptions do not establish individual membrane/lipid/protein formation requirements. No optional protein-example or generic-class enum finding is manufactured.

### Current scientific verdict

completeness: concern. Targets: GO:0070111.

needs_curation for two confirmed inherited findings, one major grounding and one minor attribution. Stale edge is substantively refreshed and supported; no new scientific finding. No image, trait or snippet assessment is invented.

### Actual native coverage

schema: supported. Targets: GO:0031981.

Actual inventory has zero protein_examples and zero GENE_OR_PROTEIN nodes. Native pass is empty represented accession/typed-node coverage, not proof of narrative molecular identity, pathway support or necessity.

### Original rendering and frozen inputs

schema: supported. Targets: GO:0031981.

Original native validation and exact Markdown render pass; every historical input and unchanged current target verified. PROPOSED status retained. Optional inventories are not fabricated requirements.

### Actual native coverage

schema: supported. Targets: cellstructuremech:nuclear_net.

Actual inventory has zero protein_examples and zero GENE_OR_PROTEIN nodes. Native pass is empty represented accession/typed-node coverage, not proof of narrative molecular identity, pathway support or necessity.

### Original rendering and frozen inputs

schema: supported. Targets: cellstructuremech:nuclear_net.

Original native validation and exact Markdown render pass; every historical input and unchanged current target verified. PROPOSED status retained. Optional inventories are not fabricated requirements.

### Actual native coverage

schema: supported. Targets: GO:0005634.

Actual inventory has zero protein_examples and zero GENE_OR_PROTEIN nodes. Native pass is empty represented accession/typed-node coverage, not proof of narrative molecular identity, pathway support or necessity.

### Original rendering and frozen inputs

schema: supported. Targets: GO:0005634.

Original native validation and exact Markdown render pass; every historical input and unchanged current target verified. PROPOSED status retained. Optional inventories are not fabricated requirements.

### Exact nuclear enclosed volume

identity: supported. Targets: GO:0031981.

GO0031981 denotes volume inside nuclear inner membrane, with0070013 is_a ancestry and nucleus parthood. This is distinct from the space between envelope membranes.

### Contained chromosome and nucleolus structural parts

grounding: supported. Targets: GO:0031981.

OTHER components name exact structural constituents0000228 and0005730; both are typed part_of children of lumen. They are not asserted as single chemical DNA/RNA/protein identities. Explicit OTHER and maintained regression precedent prevent an automatic molecular-type finding; broader class-prose tension is not a confirmed record defect.

### Bounded yeast genome-model support

evidence: supported. Targets: GO:0031981.

Duan primary population-based model supports the bounded yeast nuclear-genome organization note. BY4741-derived formaldehyde/3C methods and model limitations are explicit; no per-cell or all-lineage topology, raw-data validation or exact universal chromosome positions inferred.

### Ribosome-biogenesis functions

evidence: supported. Targets: GO:0031981.

Current GO plus complete Boisvert review abstract/Key Points support rDNA transcription, pre-rRNA processing and early ribosomal assembly. These are positive molecular/pathway assertions despite the overall topology scope; full review body and cited-primary experiments were not inspected.

### Four descriptive topology edges

graph: supported. Targets: GO:0031981.

Inner membrane delimits lumen, lumen is nuclear part, chromosome/nucleolus reside inside. Intact-nucleus phase restriction is preserved; topology does not assert assembly causality or a complete matrix/protein repertoire.

### Nucleoplasm boundary and optional substructures

scope: supported. Targets: GO:0031981.

Current GO nucleoplasm definition excludes chromosome/nucleolus and lists it as lumen part. Maintained discussion merely says exact synonymy was not established; it does not equate the regions or impose an unsupported size comparison. Open additional-substructure TODO acknowledges a bounded inventory.

### Positive nucleolar molecular functions trigger assessment

evidence: supported. Targets: GO:0031981.

rDNA transcription/pre-rRNA processing/ribosome assembly trigger native applicability. Original explicit no-expression exemption requires correction. Fresh catalogue has no matching eukaryotic host; no downstream foreign-host queries or negative biology.

### Qualified compartment support

evidence: unknown. Targets: GO:0031981.

No source pixels, raw conformation-capture data, supplemental datasets or whole Boisvert body inspected. No complete nuclear inventory, quantified prevalence or universal exact chromosome arrangement established.

### Named reticulating network and conservative ontology scope

identity: supported. Targets: cellstructuremech:nuclear_net.

Primary Results directly describe double-membrane strands, internal swellings and tunnel/peripheral-envelope continuity. GO0005622 broad parent and envelope parthood are appropriate; no separate sealed organelle asserted. Bounded current search does not turn historical589-hit survey into fresh exhaustive absence proof;0044195 adds lamina/function scope not verified here.

### Structural membrane constituent

grounding: supported. Targets: cellstructuremech:nuclear_net.

OTHER membrane row names a structural constituent with native0016020 identity, not a chemical lipid class or exact molecular composition. UNKNOWN formation necessity retained; primary morphology is not depletion/reconstitution evidence.

### One reconstructed cell and complementary specimens

scope: supported. Targets: cellstructuremech:nuclear_net.

Taxon271679 is Polykrikos kofoidii. One wild-collected cell was reconstructed by FIB-SEM after high-pressure freezing/freeze substitution; TEM and confocal preparations were separate. Neither six tunnels nor full reticulating architecture is generalized as universal species/clade prevalence.

### Pixel-level figure provenance and licence

evidence: supported. Targets: cellstructuremech:nuclear_net.

Frozen image SHA matches fresh complete Fig3 bytes. All panels A-G visually inspected and match source caption/rendered red network, section insets and six numbered tunnels. SEM modality reflects FIB-SEM sections plus segmentation, not TEM/confocal or a live mechanism. All eight authors and CC BY4.0 permission agree; no separate restrictive figure credit.

### Molecular, dynamic and taxonomic restraint

graph: supported. Targets: cellstructuremech:nuclear_net.

No causal graph. Centrin proximity and tubulin-positive tunnel spindles are explicitly withheld as net molecular constituents; super-resolution confirmation remains proposed. Flow, causal assembly and division function unresolved. Primary double-membrane description is supported but supplementary ultrastructure not independently measured.

### Later Prorocentrum study remains prospective

evidence: supported. Targets: cellstructuremech:nuclear_net.

Kalvelage Conclusion explicitly proposes further nuclear-net work and dynamics. It does not independently reconstruct the Polykrikos network or identify its molecular inventory; no lineage-wide absence claim follows.

### Genuine morphology and topology exclusion

evidence: not_applicable. Targets: cellstructuremech:nuclear_net.

Complete positive claims concern observed membrane architecture, preparation, taxon and image provenance. Centrin/tubulin, flow and mitotic machinery are discussed only as withheld assignments/questions. No positive molecular/pathway/stress/trait claim requiring module query is added merely from nearby protein names. Original N/A stands with this clarified rationale, not a bundle defect.

### Qualified net observation

evidence: unknown. Targets: cellstructuremech:nuclear_net.

Only maintained Fig3 pixels inspected. Other figure captions read; supplements, movies and raw microscopy not reanalyzed. Single reconstructed cell and multiple complementary fixed specimens do not establish dynamics, exact molecular composition or universal prevalence.

### Exact nucleus and anatomical parts

identity: supported. Targets: GO:0005634.

GO0005634 exact identity/synonym and0043231 parent agree. Envelope/lumen/pore links are supported at anatomical level. Shortened generic definition does not explicitly claim specialized nuclei lack native exceptions; no new universal RNA-metabolism/DNA-replication finding inferred.

### Exact pore protein-complex component

grounding: supported. Targets: GO:0005634.

GO0005643 explicitly denotes NPC protein complex; type and descriptive exchange role agree. UNKNOWN whole-nucleus formation essentiality is distinct from transport function, and one protein example is not required to stand for the entire NPC.

### Budding-yeast nuclear contact example

scope: supported. Targets: GO:0005634.

Pan YEF473/L40-based association/localization evidence supports the qualitative yeast NV-junction example. Source direct-interaction interpretation retains its explicit remote-indirect caveat; current record does not assert purified binary reconstitution, complete machinery sufficiency or nucleus formation requirement. COMMON remains qualitative.

### Four envelope and exchange edges

graph: supported. Targets: GO:0005634.

Envelope bounds lumen/encloses nucleus; NPC spans envelope and mediates nucleocytoplasmic transport. Native authority and explicitly secondary Aitchison support NONMECHANISTIC scope. Gating is not a literal mechanical door or a claim that whole transport is energy-free; no complete Nup inventory inferred.

### Inherited Lu and Drubin attribution

evidence: concern. Targets: GO:0005634.

Evidence[5].notes says Luo et al2022, but fresh metadata and genuine article name Michelle S Lu and David G Drubin. DOI/title and2022 volume year match; online2021 date distinguished. Preserve exact inherited minor nucleus-lu-drubin-attribution finding, not a new organelle/mechanism defect.

### Observed Cdc42 localization versus proposals

evidence: supported. Targets: GO:0005634.

Bounded Lu Results and Discussion distinguish cell-cycle-associated Nvj1/Cdc42 localization from possible future functional roles. Maintained record only cites the paper bibliographically; no inferred new Cdc42 pathway is imported.

### Positive NPC, transport and contact proteins trigger assessment

evidence: supported. Targets: GO:0005634.

NPC/nucleocytoplasmic transport and named Vac8p–Nvj1p interactions trigger native applicability despite no expression module assertion. Fresh catalogue has no exact Saccharomyces host; no downstream foreign-strain proxy or inferred absence. Correct original explicit exemption in linked review only.

### Bounded sources and optional molecular completeness

evidence: unknown. Targets: GO:0005634.

Pan selected primary sections and Lu selected primary Results/Discussion inspected; Aitchison is secondary. No pixels, supplements or raw microscopy for these sources, no complete nuclear machinery census, and no terminal older category/neighbor disposition. Optional chromatin/nucleolar cohorts remain curated TODOs.

### Exact identity, hierarchy and boundaries

identity: supported. Targets: GO:0005635.

ActiveGO5635 definition and organelle-envelope ancestry match the whole double envelope. Nucleus parthood and distinct inner/outer/lumen/pore has_part relations retain topology. Native20–40nm/lamina wording is ontology-derived, not an independent universal yeast measurement.

### Molecular constituents versus whole bilayer identities

grounding: concern. Targets: GO:0005635.

Two LIPID rows use whole-membraneGO5637/5640 as molecular groundings; their STRUCTURE component_refs repeat the mismatch. Correct parthood is preserved. NPC PROTEIN_COMPLEXGO5643 remains valid.

### Every directed edge and source-specific scope

graph: supported. Targets: GO:0005635.

All5 NONMECHANISTIC edges reviewed: inner/outerpart_of envelope; envelope contains lumen; NPC spans envelope and mediates transport. Topology/transport supported; two molecular component_ref associations remain subject to F1 grounding correction.

### Function and experimental context

scope: supported. Targets: GO:0005635.

NPC transportGO6913 and envelopeorganizationGO6998 agree with secondary-source syntheses; eukaryotic occurrence and Pan yeast NVJ canonical example are bounded qualitative claims.

### Qualitative occurrence versus reference and assay strains

scope: supported. Targets: GO:0005635.

Species4932 and broad envelope context are correct. Primary Pan usesYEF473/L40; King supplement usesW303 with namedexceptions. ReviewedUniProt559292 references identify proteins without converting every assay intoS288C or establishing quantitative prevalence.

### Frozen originals, deterministic rendering and exact protein coverage

schema: supported. Targets: GO:0005635.

All68 original input entries match retained source; all4 pairs validate/render exactly; owncurrenttarget unchanged. Zero examples and zero GENE_OR_PROTEIN nodes; NPC GO complex independently checked. Empty verifier pass is not molecular completeness.

### Original explicit applicability exclusion

provenance: concern. Targets: GO:0005635.

Original exclusion exists but its expression-only rationale is insufficient: NPC-mediated transport and envelopeorganization positively trigger actual host coverage assessment. Not an omission.

### Current bounded host applicability

evidence: not_applicable. Targets: GO:0005635.

Fresh official catalogue has no matching Saccharomyces/eukaryotic host dataset. No downstream matched-gene search or module summary is warranted. Historical runner failure and current successful source fallback are separate; no biological-negative inference.

### Actual primary, secondary and authority access tiers

evidence: supported. Targets: GO:0005635.

Hetzer and Aitchison are secondary reviews read at declared body sections; Pan is primary body read at stated Methods/Results/Discussion/captions.

### Complete target and optional claims

completeness: supported. Targets: GO:0005635.

Entire record/history/discussions/graphs/evidence read. No images, verbatim snippets or physical-property objects on this target require pixel/licence/measurement validation. StatusPROPOSED and histories remain unchanged. Optional exact lipid species, full protein inventory and family mappings are not automatically findings.

### Constitutive bilayer versus molecular formation requirement

evidence: unknown. Targets: GO:0005635.

Collective bilayer is constitutive of membrane identity. ESSENTIAL does not identify particular lipid species or proteins required for global membrane formation. Targeting/contact experiments and review-tier assembly discussion do not establish universal individual molecular necessity.

### Exact identity, hierarchy and boundaries

identity: supported. Targets: GO:0005641.

ActiveGO5641 exactly denotes perinuclear space between envelope bilayers, not nucleoplasm. Exact synonym and organelle-envelope-lumen ancestry agree; ER-lumen continuity is source-supported physical topology.

### Molecular constituents versus whole bilayer identities

grounding: supported. Targets: GO:0005641.

No component inventory, molecular essentiality or transport mechanism is asserted for this volume; bounding membranes remain external topology nodes.

### Every directed edge and source-specific scope

graph: supported. Targets: GO:0005641.

All4 NONMECHANISTIC edges reviewed: lumenpart_of envelope; inner/outer boundaries delimit lumen; lumen continuous withER lumen. No autonomous transport, resident-protein inventory or chemical composition is asserted.

### Function and experimental context

scope: supported. Targets: GO:0005641.

No functional pathway or named resident molecule is assigned; perinuclear/ER continuity does not by itself assert active transport.

### Qualitative occurrence versus reference and assay strains

scope: supported. Targets: GO:0005641.

Eukaryota2759 is correctly identified; COMMON is qualitative and not an intact-envelope census through every cell-cycle stage.

### Frozen originals, deterministic rendering and exact protein coverage

schema: supported. Targets: GO:0005641.

All68 original input entries match retained source; all4 pairs validate/render exactly; owncurrenttarget unchanged. Zero examples and zero GENE_OR_PROTEIN nodes; this lumen asserts physical boundaries without resident proteins or transport machinery.

### Original explicit applicability exclusion

provenance: supported. Targets: GO:0005641.

The lumen has no positive protein/pathway assertion; explicit sparse physical/topology scope warrants a genuine exclusion despite the original generic expression-only phrasing. No manufactured query defect.

### Current bounded host applicability

evidence: not_applicable. Targets: GO:0005641.

Physical/topology-only scope is a genuine exclusion. Catalogue was inspected for neighboring assigned molecular targets, not required to invent a lumen pathway.

### Actual primary, secondary and authority access tiers

evidence: supported. Targets: GO:0005641.

Hetzer is secondary review body, exact declared sections/caption; GO is definition/topology authority.

### Complete target and optional claims

completeness: supported. Targets: GO:0005641.

Entire record/history/discussions/graphs/evidence read. No images, verbatim snippets or physical-property objects on this target require pixel/licence/measurement validation. StatusPROPOSED and histories remain unchanged. Optional exact lipid species, full protein inventory and family mappings are not automatically findings.

### Exact identity, hierarchy and boundaries

identity: supported. Targets: GO:0005637.

ActiveGO5637 exactly denotes the inner bilayer; native synonym, organelle-membrane ancestry and envelope parthood are supported. Paired outer bilayer and perinuclear lumen remain distinct neighboring structures.

### Molecular constituents versus whole bilayer identities

grounding: supported. Targets: GO:0005637.

Collective lipid bilayer is REVIEWED_LABEL_ONLY without a whole-structure GO chemical grounding. This is a permissible constitutive-material description; named transport/contact actors are not forced into stable membrane components.

### Every directed edge and source-specific scope

graph: supported. Targets: GO:0005637.

All9 NONMECHANISTIC edges reviewed: inner membrane part_of envelope, lumen borders both bilayers, Kap60/Kap95 mediates targeting, process targetsINM, Heh1/Heh2 localizeINM and are cargo of process. King experiments support this bounded yeast pathway; not all INM proteins universally require this route.

### Function and experimental context

scope: supported. Targets: GO:0005637.

IntegralINM targeting is explicitly the source yeast Heh1/Heh2 example. Ran/Kap60/Kap95 dependence concerns cargo delivery, not formation of allINM material.

### Qualitative occurrence versus reference and assay strains

scope: supported. Targets: GO:0005637.

Species4932 and broad envelope context are correct. Primary Pan usesYEF473/L40; King supplement usesW303 with namedexceptions. ReviewedUniProt559292 references identify proteins without converting every assay intoS288C or establishing quantitative prevalence.

### Frozen originals, deterministic rendering and exact protein coverage

schema: supported. Targets: GO:0005637.

All68 original input entries match retained source; all4 pairs validate/render exactly; owncurrenttarget unchanged. Zero examples, three UNANCHORED_WITH_UNIPROT nodes with Q02821/Q03707/Q03281. Q02821 verifies only Kap60 within the named Kap60/Kap95 system, not complete pair coverage.

### Original explicit applicability exclusion

provenance: concern. Targets: GO:0005637.

Original exclusion exists but its expression-only rationale is insufficient: named Heh1/Heh2/Kap60/Kap95 targeting positively trigger actual host coverage assessment. Not an omission.

### Current bounded host applicability

evidence: not_applicable. Targets: GO:0005637.

Fresh official catalogue has no matching Saccharomyces/eukaryotic host dataset. No downstream matched-gene search or module summary is warranted. Historical runner failure and current successful source fallback are separate; no biological-negative inference.

### Actual primary, secondary and authority access tiers

evidence: supported. Targets: GO:0005637.

King primary author-uploaded browser excerpts plus genuine publisher supplement inspected. Main-PDF URL yielded HTML, not PDF; no pixels, unread body lines or independent new assay claimed.

### Complete target and optional claims

completeness: supported. Targets: GO:0005637.

Entire record/history/discussions/graphs/evidence read. No images, verbatim snippets or physical-property objects on this target require pixel/licence/measurement validation. StatusPROPOSED and histories remain unchanged. Optional exact lipid species, full protein inventory and family mappings are not automatically findings.

### Constitutive bilayer versus molecular formation requirement

evidence: unknown. Targets: GO:0005637.

Collective bilayer is constitutive of membrane identity. ESSENTIAL does not identify particular lipid species or proteins required for global membrane formation. Targeting/contact experiments and review-tier assembly discussion do not establish universal individual molecular necessity.

### Exact current reference proteins and bounded family checks

grounding: supported. Targets: GO:0005637.

Zero examples, three UNANCHORED_WITH_UNIPROT nodes with Q02821/Q03707/Q03281. Q02821 verifies only Kap60 within the named Kap60/Kap95 system, not complete pair coverage. All accessions are reviewedS288C; primary names/synonyms/loci checked. InterPro exact-association responses distinguish family/domain/repeat; P38881 HTTP204 is bounded nonreturn, not universal family absence.

### Reject inherited rationale-only finding under native history policy

provenance: supported. Targets: GO:0005637.

The September rationale is historical provenance. Current prompt still requests source-neutral grounding, which instance xrefs do not complete; October18 history explicitly records added xrefs. No material record defect is established by absence of an optional current-state note. Preserve original rationale and validOPEN family task; reject exact inherited minorF1, not resolve a nonexistent record fix or close a wider category finding.

### Exact identity, hierarchy and boundaries

identity: supported. Targets: GO:0005640.

ActiveGO5640 exactly denotes the cytoplasm-facing outer bilayer; native definition supports ER continuity and organelle-membrane ancestry. The source yeast NVJ example does not change record identity into a junction.

### Molecular constituents versus whole bilayer identities

grounding: supported. Targets: GO:0005640.

Collective lipid bilayer is REVIEWED_LABEL_ONLY without a whole-structure GO chemical grounding. This is a permissible constitutive-material description; named transport/contact actors are not forced into stable membrane components.

### Every directed edge and source-specific scope

graph: supported. Targets: GO:0005640.

All6 NONMECHANISTIC edges reviewed: outerpart_of envelope, lumen borders outer/inner bilayers, Nvj1 localizesONM, Vac8 localizesvacuolar membrane, and the pair interacts. Pan interprets direct interaction with an explicit remote indirect possibility; no minimal purified reconstitution or entire membrane assembly claim.

### Function and experimental context

scope: supported. Targets: GO:0005640.

NVJ formation is specifically the budding-yeast Nvj1/Vac8 contact process; source manipulation supports that contact, not assembly of the entireONM.

### Qualitative occurrence versus reference and assay strains

scope: supported. Targets: GO:0005640.

Species4932 and broad envelope context are correct. Primary Pan usesYEF473/L40; King supplement usesW303 with namedexceptions. ReviewedUniProt559292 references identify proteins without converting every assay intoS288C or establishing quantitative prevalence.

### Frozen originals, deterministic rendering and exact protein coverage

schema: supported. Targets: GO:0005640.

All68 original input entries match retained source; all4 pairs validate/render exactly; owncurrenttarget unchanged. Zero examples, two UNANCHORED_WITH_UNIPROT nodes with P38881/P39968; permissible node xrefs independently checked, not source-neutral family grounding.

### Original explicit applicability exclusion

provenance: concern. Targets: GO:0005640.

Original exclusion exists but its expression-only rationale is insufficient: named Nvj1/Vac8 contact formation positively trigger actual host coverage assessment. Not an omission.

### Current bounded host applicability

evidence: not_applicable. Targets: GO:0005640.

Fresh official catalogue has no matching Saccharomyces/eukaryotic host dataset. No downstream matched-gene search or module summary is warranted. Historical runner failure and current successful source fallback are separate; no biological-negative inference.

### Actual primary, secondary and authority access tiers

evidence: supported. Targets: GO:0005640.

Pan genuine primary body read at Methods3-6,9; Results11-17; Discussion18-20/captions. Direct-interaction qualification retained; nativeUniProt andInterPro are authority context.

### Complete target and optional claims

completeness: supported. Targets: GO:0005640.

Entire record/history/discussions/graphs/evidence read. No images, verbatim snippets or physical-property objects on this target require pixel/licence/measurement validation. StatusPROPOSED and histories remain unchanged. Optional exact lipid species, full protein inventory and family mappings are not automatically findings.

### Constitutive bilayer versus molecular formation requirement

evidence: unknown. Targets: GO:0005640.

Collective bilayer is constitutive of membrane identity. ESSENTIAL does not identify particular lipid species or proteins required for global membrane formation. Targeting/contact experiments and review-tier assembly discussion do not establish universal individual molecular necessity.

### Exact current reference proteins and bounded family checks

grounding: supported. Targets: GO:0005640.

Zero examples, two UNANCHORED_WITH_UNIPROT nodes with P38881/P39968; permissible node xrefs independently checked, not source-neutral family grounding. All accessions are reviewedS288C; primary names/synonyms/loci checked. InterPro exact-association responses distinguish family/domain/repeat; P38881 HTTP204 is bounded nonreturn, not universal family absence.

### Reject inherited rationale-only finding under native history policy

provenance: supported. Targets: GO:0005640.

The September rationale is historical provenance. Current prompt still requests source-neutral grounding, which instance xrefs do not complete; October18 history explicitly records added xrefs. No material record defect is established by absence of an optional current-state note. Preserve original rationale and validOPEN family task; reject exact inherited minorF1, not resolve a nonexistent record fix or close a wider category finding.

### Complete frozen-input comparison and bounded refresh

provenance: supported. Targets: cellstructuremech:nitroplast, GO:0005635, GO:0005641, GO:0005637, GO:0031981, cellstructuremech:nuclear_net, GO:0005640, GO:0033009, GO:0005634, GO:0070111.

1 of ten original target hashes differ from current main. The changed content is substantively reassessed in the target-specific assessments; original observations remain historical and unchanged. All current target and used context bytes are frozen.

## Findings

### septin-organellar_chromatophore-F1: Separate whole membrane parts from molecular lipid components

major / open / confirmed; issue key: organellar-chromatophore-membrane-lipid-grounding.

Components0–2 are typed LIPID but their labels and GO0070114/13/18 groundings identify entire anatomical membranes. These identities are valid structural parts, not lipid entities. The corresponding structural graph nodes also carry component_ref links to those misclassified molecular rows.

### septin-organellar_chromatophore-F2: Attach the light-reaction complex claim to its primary evidence

minor / open / confirmed; issue key: organellar-chromatophore-thylakoid-go-source-overstatement.

The component and graph source notes say GO0070118 defines an internal photosynthetic membrane system carrying light-reaction complexes. Its actual definition only identifies the thylakoid lipid-bilayer membrane. The inspected Nowack2012 Results directly support thylakoid-associated PSI proteins and provide the appropriate experimental source.

### plaque-t8-F1: Correct the Lu and Drubin citation attribution

minor / open / confirmed; issue key: nucleus-lu-drubin-attribution.

evidence[5].notes attributes DOI10.1080/21541248.2021.1993714 to Luo et al2022. Both native MED metadata and the primary article identify Michelle S Lu and David G Drubin as its two authors. The DOI, title and2022 volume year otherwise match.

### micro-F1: Separate whole membrane parts from molecular lipid groundings

major / open / confirmed; issue key: nuclear-envelope-whole-membranes-as-lipid-groundings.

The inner and outer membrane components are typed LIPID but grounded to whole cellular-component identities GO0005637 and GO0005640. The schema requires molecular lipid grounding; these GO entries denote complete bilayers containing more than the lipid identity. The linked STRUCTURE nodes repeat the same mismatch through component_ref. Correct has_part and topology assertions remain valid.

### micro-F2: Update the open protein-grounding rationale to acknowledge verified xrefs

minor / rejected / confirmed; issue key: nuclear-inner-membrane-stale-protein-grounding-rationale.

The rationale says the named protein nodes are left ungrounded until exact UniProt or family identifiers can be verified. Current graph nodes already carry verified accessions, and the October curation event records their addition. The remaining task needs to distinguish completed instance verification from any unresolved family or grouped-actor coverage.

Disposition: The original minor finding treated a dated historical rationale as an inaccurate current task description. Native CURATION says discussions are provenance, rationale is appended to and never replaced, and notes hold current state. The current prompt still asks for source-neutral grounding; organism-specific UniProt xrefs do not complete that family-level task. The October18 curation history explicitly records instance-xref additions. No material erroneous current assertion or required missing representation is established merely because the September rationale is unchanged. Optional appended progress notes can help, but do not justify mandatory record curation. Original action also said preserve historical context; this rejection does not falsely characterize it as an explicit order to erase history.

### micro-F3: Update the open protein-grounding rationale to acknowledge verified xrefs

minor / rejected / confirmed; issue key: nuclear-outer-membrane-stale-protein-grounding-rationale.

The rationale says the named protein nodes are left ungrounded until exact UniProt or family identifiers can be verified. Current graph nodes already carry verified accessions, and the October curation event records their addition. The remaining task needs to distinguish completed instance verification from any unresolved family or grouped-actor coverage.

Disposition: The original minor finding treated a dated historical rationale as an inaccurate current task description. Native CURATION says discussions are provenance, rationale is appended to and never replaced, and notes hold current state. The current prompt still asks for source-neutral grounding; organism-specific UniProt xrefs do not complete that family-level task. The October18 curation history explicitly records instance-xref additions. No material erroneous current assertion or required missing representation is established merely because the September rationale is unchanged. Optional appended progress notes can help, but do not justify mandatory record curation. Original action also said preserve historical context; this rejection does not falsely characterize it as an explicit order to erase history.

## Recommended Actions And Acceptance Checks

### septin-organellar_chromatophore-A1

Preserve supported membrane parts/topology. Represent whole structural constituents with an appropriate structural type if retained, or model supported lipid materials separately with exact chemical grounding or justified reviewed-label-only status; align graph component_ref joins to that distinction.

- Verify each LIPID row denotes a molecular lipid/material identity rather than a GO membrane location.
- Run focused schema, strict and graph checks after separately authorized curation.

### septin-organellar_chromatophore-A2

Restrict the GO note to the compartment definition and attach the relevant primary localization/PSI evidence to the light-complex statement.

- Re-read GO0070118 definition and Nowack2012 Results sec2–4.
- Ensure the updated evidence note states only what its cited source establishes.

### plaque-t8-A1

Correct the evidence note to Lu and Drubin(2022), retaining the verified DOI/title and treating the article functional proposals as proposals.

- Verify exact authors/title/DOI against the native source.
- After separately authorized curation, run the focused schema and strict validation recipes.

### micro-A1

In separately authorized curation, retain correct inner/outer has_part links and graph topology while correcting the component representation: represent structural parts with a scientifically accurate permitted type, or represent molecular lipid material with verified chemical grounding or candid label-only status. Reconcile component_ref links with the chosen scope and retain the valid pore complex. Do not invent a lipid species or change membrane identity.

- Neither LIPID row uses an identifier that denotes the entire nuclear membrane.
- Inner/outer parthood, lumen boundaries and NPC topology are preserved; each component_ref matches the intended component scope.
- Native schema, strict, product, identifier, graph and history gates pass after authorized curation.

### micro-A2

Correct the review disposition with exact predecessor lineage; preserve the immutable original and unchanged scientific record. Do not mandate replacing historical rationale or closing a still-valid source-neutral grounding task. Optional current-state notes remain separately discretionary.

- Successor records rejected status and evidence-backed disposition for this exact original F1/key.
- No scientific record, historical rationale, original bundle or valid UniProt xref is changed as this review remedy.
- Any optional later discussion update preserves rationale and posed_date and separates instance verification from family grounding.

### micro-A3

Correct the review disposition with exact predecessor lineage; preserve the immutable original and unchanged scientific record. Do not mandate replacing historical rationale or closing a still-valid source-neutral grounding task. Optional current-state notes remain separately discretionary.

- Successor records rejected status and evidence-backed disposition for this exact original F1/key.
- No scientific record, historical rationale, original bundle or valid UniProt xref is changed as this review remedy.
- Any optional later discussion update preserves rationale and posed_date and separates instance verification from family grounding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| current-record-0 | data/structures/membrane_organelle/nitroplast.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 3f7dc36b6c5e8389c881e64839227e1e5cdde49edb55277e245b180f0de8d6a8; current SHA256 3f7dc36b6c5e8389c881e64839227e1e5cdde49edb55277e245b180f0de8d6a8. Record bytes unchanged since the original review. |
| original-review-0 | reviews/structured/20261022T025104Z-nitroplast-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-1 | data/structures/membrane_organelle/nuclear_envelope.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 226a12a5500d39f1afbc5baa0f3a81891d6ae4918f4d6c29e8ce05de0df9979a; current SHA256 226a12a5500d39f1afbc5baa0f3a81891d6ae4918f4d6c29e8ce05de0df9979a. Record bytes unchanged since the original review. |
| original-review-1 | reviews/structured/20261022T025105Z-nuclear-envelope-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-2 | data/structures/membrane_organelle/nuclear_envelope_lumen.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 1c45350eaa4a19474f4689125aadc8aa93d1824d41303e3c4aaff1f7e1db6019; current SHA256 1c45350eaa4a19474f4689125aadc8aa93d1824d41303e3c4aaff1f7e1db6019. Record bytes unchanged since the original review. |
| original-review-2 | reviews/structured/20261022T025106Z-nuclear-envelope-lumen-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-3 | data/structures/membrane_organelle/nuclear_inner_membrane.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 c0484a80c2b1568174ca7f9c96805a6ce2749a3ba27b700e21fb1de2aef4e4df; current SHA256 c0484a80c2b1568174ca7f9c96805a6ce2749a3ba27b700e21fb1de2aef4e4df. Record bytes unchanged since the original review. |
| original-review-3 | reviews/structured/20261022T025106Z-nuclear-inner-membrane-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-4 | data/structures/membrane_organelle/nuclear_lumen.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 dbb07d267c0272e4deb338a2e8a0e29892a6f1d28f279160c3d42f730410fb49; current SHA256 dbb07d267c0272e4deb338a2e8a0e29892a6f1d28f279160c3d42f730410fb49. Record bytes unchanged since the original review. |
| original-review-4 | reviews/structured/20261022T025107Z-nuclear-lumen-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-5 | data/structures/membrane_organelle/nuclear_net.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 8b4a54d13a70cfb4fdce9bd18ae990793f9de9627fdca067573c033335d847ba; current SHA256 8b4a54d13a70cfb4fdce9bd18ae990793f9de9627fdca067573c033335d847ba. Record bytes unchanged since the original review. |
| original-review-5 | reviews/structured/20261022T025108Z-nuclear-net-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-6 | data/structures/membrane_organelle/nuclear_outer_membrane.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 a760b04919cb0a80c89fd2eee5c1d4a0c940fc15a17b77b4b1810b9e1d2b2ffb; current SHA256 a760b04919cb0a80c89fd2eee5c1d4a0c940fc15a17b77b4b1810b9e1d2b2ffb. Record bytes unchanged since the original review. |
| original-review-6 | reviews/structured/20261022T025109Z-nuclear-outer-membrane-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-7 | data/structures/membrane_organelle/nucleomorph.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 9653087b981991e28b537ec1eb809e442f5215f4ff4c994687106b74ed6338ad; current SHA256 9653087b981991e28b537ec1eb809e442f5215f4ff4c994687106b74ed6338ad. Record bytes unchanged since the original review. |
| original-review-7 | reviews/structured/20261022T025109Z-nucleomorph-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-8 | data/structures/membrane_organelle/nucleus.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 889818b3c6a37074924a97bc81271f43ef236dc9112a871c5e521dae123e497d; current SHA256 889818b3c6a37074924a97bc81271f43ef236dc9112a871c5e521dae123e497d. Record bytes unchanged since the original review. |
| original-review-8 | reviews/structured/20261022T025110Z-nucleus-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-9 | data/structures/membrane_organelle/organellar_chromatophore.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 6e9805392c72104f5f1d6e9ee70767c49f480b22130da0e6f293bcf8f6a1bec0; current SHA256 b217af7ad434f269a5b8cba2428be5cd988746a75c34a999d7b69909160fcba4. Changed record reassessed against current sources. |
| original-review-9 | reviews/structured/20261022T025111Z-organellar-chromatophore-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| septin-review-policy | .claude/skills/review-yaml-record/SKILL.md; Whole-record assertions, structured sources and severity rubric | supports | Positive molecular/pathway assertions require a real applicability assessment; absence of expression claims alone is not an exemption. Keep source scope, uncertainty and original finding identity; record curation is separate. |
| septin-curation-policy | docs/CURATION.md; Structural components, molecular grounding and family-or-class guidance | supports | Whole assembled membranes are structures; a LIPID component denotes molecular material and cannot use a complete membrane identity as exact chemical grounding. Taxon-agnostic protein families OR classes are permitted. An optional example inventory is not automatically required for every generic class. |
| septin-schema-policy | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, ComponentTypeEnum and grounding contract | supports | Molecular components and whole structures have different identities. Label-only supported lipid material is possible without inventing exact chemical composition. PROTEIN enum prose is interpreted with explicit CURATION generic-class permission; no automatic complex assertion follows from a heterogeneous class. |
| septin-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Graph nodes, component correspondence, source scope and necessity | supports | Descriptive boundary graphs can remain NONMECHANISTIC; source-specific localization, molecular identity and organelle-formation necessity must not be conflated. |
| septin-protein-policy | .claude/skills/uniprot-protein-examples/SKILL.md; Step2 generic classes and native coverage report | supports | Generic class components are explicitly recognized. A zero-example inventory or NO_GENE_SYMBOLS node is a stated coverage limit, not proof that the protein class does not exist or that its members form one stable complex. |
| septin-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0043229,GO:0016020,GO:0016610,GO:0009399,GO:0033009,GO:0043231,GO:0009536,GO:0070111,GO:0070113,GO:0070114,GO:0070115,GO:0070116,GO:0070117,GO:0070118,GO:0015979; All15 exact returned active terms: definitions, synonyms, aspects and child relations | supports | Exact nucleomorph and chromatophore identities and structural/process parents match. GO0070118 defines only a thylakoid bilayer; GO0070116 lists it part_of, while GO0070111 lists GO0070116 part_of. GO0016020 describes a collective membrane, not a lipid molecule. GO0016610 is nitrogenase complex; its generic definition does not measure nitroplast stoichiometry. |
| septin-go-search-nitroplast | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=nitroplast&amp;limit=100&amp;page=1; Entire bounded exact-word search response: numberOfHits0 | supports | The exact-word nitroplast search returned no term; this supports retaining the local identity with a broad organelle parent, without claiming exhaustive ontology absence. |
| septin-SL0351 | https://rest.uniprot.org/locations/SL-0351.json; Complete exact location JSON including nested plastid parent | supports | Exact whole-chromatophore entry supports photosynthesis, CO2 fixation, two surrounding membranes, intervening residual peptidoglycan and contained thylakoids. It does not define a separate thylakoid-membrane location or name its molecular composition; that narrower identity comes from GO0070118. |
| septin-tax373042 | https://rest.uniprot.org/taxonomy/373042.json; Exact current taxonomy identity/rank/lineage fields | supports | Braarudosphaera bigelowii species matches the record. Taxonomic identity does not establish experimental strain, prevalence, a universal phenotype or molecular necessity. |
| septin-tax3027 | https://rest.uniprot.org/taxonomy/3027.json; Exact current taxonomy identity/rank/lineage fields | supports | Cryptophyceae class matches the record. Taxonomic identity does not establish experimental strain, prevalence, a universal phenotype or molecular necessity. |
| septin-tax29197 | https://rest.uniprot.org/taxonomy/29197.json; Exact current taxonomy identity/rank/lineage fields | supports | Chlorarachniophyceae class matches the record. Taxonomic identity does not establish experimental strain, prevalence, a universal phenotype or molecular necessity. |
| septin-tax55529 | https://rest.uniprot.org/taxonomy/55529.json; Exact current taxonomy identity/rank/lineage fields | supports | Guillardia theta species matches the record. Taxonomic identity does not establish experimental strain, prevalence, a universal phenotype or molecular necessity. |
| septin-tax227086 | https://rest.uniprot.org/taxonomy/227086.json; Exact current taxonomy identity/rank/lineage fields | supports | Bigelowiella natans species matches the record. Taxonomic identity does not establish experimental strain, prevalence, a universal phenotype or molecular necessity. |
| septin-tax39717 | https://rest.uniprot.org/taxonomy/39717.json; Exact current taxonomy identity/rank/lineage fields | supports | Paulinella chromatophora species matches the record. Taxonomic identity does not establish experimental strain, prevalence, a universal phenotype or molecular necessity. |
| septin-coale2024-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1126%2Fscience.adk1075%22&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact DOI search: bibliographic fields and complete abstractText | supports | Coale et al.2024, Nitrogen-fixing organelle in a marine alga, DOI10.1126/science.adk1075; bibliography and complete abstract match. Actual article/supplement text is separately scoped. |
| septin-curtis2012-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fnature11681%22&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact DOI search: bibliographic fields and complete abstractText | supports | Curtis et al.2012, Algal genomes reveal evolutionary mosaicism and the fate of nucleomorphs, DOI10.1038/nature11681. Complete abstract supports the two compared species and retained essential-gene residues; publisher body access failed and is not claimed. |
| septin-tanifuji2014-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1186%2F1471-2164-15-374%22&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact DOI search: bibliographic fields and complete abstractText | supports | Tanifuji et al.2014 bibliographic identity and complete abstract agree with genuine XML body below. |
| septin-onuma2017-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fs41598-017-02668-2%22&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact DOI search: bibliographic fields and complete abstractText | supports | Onuma et al.2017 bibliographic identity and complete abstract agree with genuine XML body below. |
| septin-nowack2012-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1073%2Fpnas.1118800109%22&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact DOI search: bibliographic fields and complete abstractText | supports | Nowack and Grossman2012 bibliographic identity and complete abstract agree with genuine PMC body below. |
| septin-singer2017-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.cub.2017.08.010%22&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact DOI search: bibliographic fields and complete abstractText | supports | Singer et al.2017 complete abstract supports proteomic import and a combined experimental/predicted protein catalogue; the conserved long-protein targeting signal and two routes are putative. Full body, supplements and individual candidates are not independently read. |
| septin-gabr2020-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1111%2Fjpy.13003%22&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact DOI search: bibliographic fields and complete abstractText | supports | Gabr et al.2020 complete secondary abstract supports Paulinella as an organellogenesis model and import/metabolic integration context. No full-body or primary-experimental certification is claimed. |
| septin-li2026-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.64898%2F2026.04.11.717942%22&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact DOI search: bibliographic fields and complete abstractText | supports | Li et al.2026 preprint metadata/abstract matches DOI10.64898/2026.04.11.717942; retrieved XML independently identifies version1/preprint status. |
| septin-nowack2014-crossref | https://api.crossref.org/works/10.5586/asbp.2014.049; Exact DOI metadata and complete deposited secondary abstract | supports | Nowack2014 review title,author,year and qualitative Paulinella context match. Secondary abstract is not a primary experiment or a numerical prevalence estimate. |
| septin-coale2024-main-page1 | https://html.scribdassets.com/5pd08as4w0cdtz4x/pages/1-6ee1ae9510.jsonp; Article p217, title/abstract and opening architecture/division text; fresh public article-page HTML/JSONP text, gzip decoded; not platform-generated prose | supports | UCYN-A2 association and organelle interpretation; location and coordinated division in the studied culture. |
| septin-coale2024-main-page3 | https://html.scribdassets.com/5pd08as4w0cdtz4x/pages/3-56a5ec096d.jsonp; Article p219, import Results and Fig2 caption text; fresh public article-page HTML/JSONP text, gzip decoded; not platform-generated prose | supports | Enrichment-based import evidence is distinguished from detection and prediction; NifH enrichment supports nitrogenase membership. |
| septin-coale2024-main-page4 | https://html.scribdassets.com/5pd08as4w0cdtz4x/pages/4-3a12e3746a.jsonp; Article p220, uTP Results and Fig3 caption text; fresh public article-page HTML/JSONP text, gzip decoded; not platform-generated prose | supports | uTP predictions include undetected proteins; missing C-terminal peptides permit cleavage or lack of translation. No measured cleavage mechanism is established. |
| septin-coale2024-main-page5 | https://html.scribdassets.com/5pd08as4w0cdtz4x/pages/5-c1a70e6f2c.jsonp; Article p221, UCYN-A as nitrogen-fixing organelle conclusion; fresh public article-page HTML/JSONP text, gzip decoded; not platform-generated prose | supports | Authors interpret the combined division/import observations as early organellogenesis; this does not equate every UCYN-A lineage with the tested culture. |
| septin-coale2024-supp-page2 | https://html.scribdassets.com/4a1aolh8hsce62xa/pages/2-349cb1d046.jsonp; Supplement p2, isolation/culture and diel sampling Methods; fresh public article-page HTML/JSONP text, gzip decoded; not platform-generated prose | supports | FR-21=NIES4399; proteomics used N-deplete culture and SXT N-replete culture. FR-12 is a separate isolate. |
| septin-coale2024-supp-page7 | https://html.scribdassets.com/4a1aolh8hsce62xa/pages/7-952a50e37b.jsonp; Supplement p7, nitrogen fixation rates Methods; fresh public article-page HTML/JSONP text, gzip decoded; not platform-generated prose | supports | Triplicate cultures and daytime acetylene-reduction measurements support nitrogenase activity, without an organelle-assembly knockout. |
| septin-coale2024-supp-page11 | https://html.scribdassets.com/4a1aolh8hsce62xa/pages/11-ca621b2751.jsonp; Supplement p11, FigS3 caption text only; fresh public article-page HTML/JSONP text, gzip decoded; not platform-generated prose | supports | Caption reports growth, nitrogenase activity and photosynthetic efficiency; image pixels and quantitative plotted values were not inspected. |
| septin-hagino2026-body | https://wakemanlaboratory.com/wp-content/uploads/2026/07/taxonomic-re-evaluation-of-the-braarudosphaera-bigelowii-species-complex-prymnesiophyceae-_compressed.pdf; Genuine PDF: article first page copyright (PDF2), TEM Methods (PDF6/printed5), cytology Results (PDF9/printed8), Table2/discussion (PDF13/printed12), Fig28–31 caption and pixels (PDF14/printed13), taxonomy/culture-loss discussion (PDF17/printed16) | supports | FR12/FR21 are genotypeIII B.bigelowii sensu stricto; FR21=NIES4399. Table2 separates nitroplast-bearing cultures from KC1-P2 loss. Fig28/29 show FR21 Nit bodies with 1um bars; Fig30/31 are OTR22-B. Copyright is International Phycological Society; link-only OTHER does not assert a redistribution licence. Culture loss does not establish wild prevalence or its cause. |
| septin-pixels-hagino2026-p1 | https://wakemanlaboratory.com/wp-content/uploads/2026/07/taxonomic-re-evaluation-of-the-braarudosphaera-bigelowii-species-complex-prymnesiophyceae-_compressed.pdf; Publisher cover/title pixels; locally rendered derivative /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/adversary-septin/hagino2026-p1.png | supports | Actual view_image inspection; panels/strains/scale are evaluated with the parent PDF caption and copyright. No image edit or repository image write. |
| septin-pixels-hagino2026-13 | https://wakemanlaboratory.com/wp-content/uploads/2026/07/taxonomic-re-evaluation-of-the-braarudosphaera-bigelowii-species-complex-prymnesiophyceae-_compressed.pdf; PDF13 Table2 and taxonomy discussion pixels; locally rendered derivative /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/adversary-septin/hagino2026-13.png | supports | Actual view_image inspection; panels/strains/scale are evaluated with the parent PDF caption and copyright. No image edit or repository image write. |
| septin-pixels-hagino2026-14 | https://wakemanlaboratory.com/wp-content/uploads/2026/07/taxonomic-re-evaluation-of-the-braarudosphaera-bigelowii-species-complex-prymnesiophyceae-_compressed.pdf; PDF14 Fig28–31 full-page pixels; locally rendered derivative /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/adversary-septin/hagino2026-14.png | supports | Actual view_image inspection; panels/strains/scale are evaluated with the parent PDF caption and copyright. No image edit or repository image write. |
| septin-tanifuji2014-xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4035089/fullTextXML; Genuine Europe PMC XML: Background; first Results subsection on L.oceanica genome; Fig1 caption; Methods culturing, sequencing and assembly (derived section indices0,2,10–12) | supports | L.oceanica CCMP622 has three linear nucleomorph chromosomes. Repetitive chromosomeI leaves exact size uncertain; assembly and PCR support the chromosome description. Background separates red/green origins. Genome sequencing is not individual-gene deletion or formation-necessity evidence; no figure pixels inspected. |
| septin-onuma2017-xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5443833/fullTextXML; Genuine Europe PMC XML: H2A localization and replication Results, Fig2–4 captions, replication Discussion, culture/IF/EdU Methods (derived indices3,4,7,12,14,17) | supports | G.theta CCMP2712 was synchronized under8h light/16h dark; only about30% divided. H2A localization and timed EdU pulses support a cell-cycle-linked replication example with later/longer nucleomorph synthesis. Not every cell or lineage was experimentally shown to replicate identically; no figure pixels inspected. |
| septin-li2026-xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13104995/fullTextXML; Genuine Europe PMC XML front version/status and Discussion hybrid envelope, diel remodeling, and Limitations (derived indices9–11) | supports | Version1 remains a preprint. Static ultrastructure does not identify vesicle cargo/direction, exchanged substrates or a transport mechanism; the record correctly leaves these unresolved. No new constituent or causal edge is inferred from unidentified densities; pixels were not inspected. |
| septin-nowack2012-prefixed | https://pmc.ncbi.nlm.nih.gov/articles/PMC3325729/; Genuine PMC body: Results PsaE localization, PSI purification, translational-inhibitor labelling and Golgi observation; Fig1–4 captions; Discussion import/trafficking/targeting; Methods strain, antibodies, EM, PSI isolation/protein identification and radiolabelling | supports | In P.chromatophora CCAC0185, localization, purified PSI and inhibitor-labelling support host synthesis/import and PSI association of PsaE/PsaK. Golgi routing is suggested, not mechanistically proven. This is the primary basis for the light-complex claim, separate from GO compartment definition. Captions, not microscopy pixels or supplements, were read. |
| septin-catalogue | https://imodulondb.org/api/datasets; Complete current official organism/dataset catalogue | supports | No matched Braarudosphaera/UCYN-A/Atelocyanobacterium, cryptophyte/chlorarachniophyte/Guillardia/Bigelowiella/Lotharella or Paulinella dataset is present. Synechococcus elongatus is not a matched host/strain proxy. Molecular claims trigger assessment, but downstream queries are not applicable without a matching dataset. No biological absence is inferred. |
| septin-adapter-runner-historical | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical attempted runner, not a fresh invocation | supports | Actual2026-11-03T00:49:00.848907Z–00:49:00.863225Z ended exit1 PermissionError reading pyvenv.cfg. Historical availability is distinct from fresh official catalogue and primary-source fallback. |
| septin-context-diazoplast | data/structures/membrane_organelle/diazoplast.yaml; Frozen identity,definition,hierarchy and boundary evidence only | supports | Boundary context read after freezing: distinct diazoplast and general plastid identities. Neighbor molecular findings and historical dispositions are not independently assessed or resolved. |
| septin-context-plastid | data/structures/membrane_organelle/plastid.yaml; Frozen identity,definition,hierarchy and boundary evidence only | supports | Boundary context read after freezing: distinct diazoplast and general plastid identities. Neighbor molecular findings and historical dispositions are not independently assessed or resolved. |
| septin-structural-other-precedent | tests/test_trypanosome_structure_evidence.py; test_faz1_rnai_does_not_establish_null_assembly_essentiality, structural OTHER assertion only | supports | Frozen native test recognizes OTHER for a structural constituent. Together with native schema this supports nitroplast collective membrane OTHER; no unrelated FAZ science is reviewed or transferred. |
| septin-retrieval-source-receipts | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/adversary-septin/source-receipts.json; Actual saved request outcomes, times and SHA256 | supports | HTTP200 challenge bodies are not paper bodies. Fresh alternate genuine XML/PMC/article-page requests are separately identified; failed requests are retained. No old source body timestamp is represented as a fresh fetch. |
| septin-retrieval-additional-source-receipts | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/adversary-septin/additional-source-receipts.json; Actual saved request outcomes, times and SHA256 | supports | HTTP200 challenge bodies are not paper bodies. Fresh alternate genuine XML/PMC/article-page requests are separately identified; failed requests are retained. No old source body timestamp is represented as a fresh fetch. |
| septin-retrieval-recovery-source-receipts | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/adversary-septin/recovery-source-receipts.json; Actual saved request outcomes, times and SHA256 | supports | HTTP200 challenge bodies are not paper bodies. Fresh alternate genuine XML/PMC/article-page requests are separately identified; failed requests are retained. No old source body timestamp is represented as a fresh fetch. |
| septin-retrieval-final-source-receipts | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/adversary-septin/final-source-receipts.json; Actual saved request outcomes, times and SHA256 | supports | HTTP200 challenge bodies are not paper bodies. Fresh alternate genuine XML/PMC/article-page requests are separately identified; failed requests are retained. No old source body timestamp is represented as a fresh fetch. |
| septin-record-nitroplast | data/structures/membrane_organelle/nitroplast.yaml; Complete current record at e2edc3550e41792c2bb6f24eb2918b7d33d8a58c | supports | All identity,history,synonym,hierarchy,component,scope,canonical,evidence,discussion and graph/image fields read. Current content independently reassessed; historical review verdict is not automatically carried forward. |
| septin-original-nitroplast | reviews/structured/20261022T025104Z-nitroplast-audit/review.yaml; Complete immutable original YAML/Markdown, scientific claims/findings/actions/checks/limits | supports | Original native validate/render succeeds with exact Markdown. Original target hash verified at its frozen source; target remains byte-identical. |
| septin-original-validation-nitroplast | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/adversary-septin/original-checks.json; Actual native original schema/render and historical target hash check | supports | Both commands exit0, Markdown exact. Frozen and current target hashes remain distinct for the stale chromatophore. |
| septin-native-nitroplast-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nitroplast-uniprot-verify-receipt.json; Actual receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nitroplast-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0. Independent whole-record inventory confirms zero protein examples, zero GENE_OR_PROTEIN nodes and no UniProtKB graph xrefs. Exit0 validates only that empty represented identifier scope; it does not certify complete molecular composition or biological claims. |
| septin-native-nitroplast-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nitroplast-uniprot-causal-receipt.json; Actual receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nitroplast-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Exit0. Independent whole-record inventory confirms zero protein examples, zero GENE_OR_PROTEIN nodes and no UniProtKB graph xrefs. Exit0 validates only that empty represented identifier scope; it does not certify complete molecular composition or biological claims. |
| septin-record-nucleomorph | data/structures/membrane_organelle/nucleomorph.yaml; Complete current record at e2edc3550e41792c2bb6f24eb2918b7d33d8a58c | supports | All identity,history,synonym,hierarchy,component,scope,canonical,evidence,discussion and graph/image fields read. Current content independently reassessed; historical review verdict is not automatically carried forward. |
| septin-original-nucleomorph | reviews/structured/20261022T025109Z-nucleomorph-audit/review.yaml; Complete immutable original YAML/Markdown, scientific claims/findings/actions/checks/limits | supports | Original native validate/render succeeds with exact Markdown. Original target hash verified at its frozen source; target remains byte-identical. |
| septin-original-validation-nucleomorph | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/adversary-septin/original-checks.json; Actual native original schema/render and historical target hash check | supports | Both commands exit0, Markdown exact. Frozen and current target hashes remain distinct for the stale chromatophore. |
| septin-native-nucleomorph-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nucleomorph-uniprot-verify-receipt.json; Actual receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nucleomorph-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0. Independent whole-record inventory confirms zero protein examples, zero GENE_OR_PROTEIN nodes and no UniProtKB graph xrefs. Exit0 validates only that empty represented identifier scope; it does not certify complete molecular composition or biological claims. |
| septin-native-nucleomorph-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nucleomorph-uniprot-causal-receipt.json; Actual receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nucleomorph-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Exit0. Independent whole-record inventory confirms zero protein examples, zero GENE_OR_PROTEIN nodes and no UniProtKB graph xrefs. Exit0 validates only that empty represented identifier scope; it does not certify complete molecular composition or biological claims. |
| septin-record-organellar_chromatophore | data/structures/membrane_organelle/organellar_chromatophore.yaml; Complete current record at e2edc3550e41792c2bb6f24eb2918b7d33d8a58c | supports | All identity,history,synonym,hierarchy,component,scope,canonical,evidence,discussion and graph/image fields read. Current content independently reassessed; historical review verdict is not automatically carried forward. |
| septin-original-organellar_chromatophore | reviews/structured/20261022T025111Z-organellar-chromatophore-audit/review.yaml; Complete immutable original YAML/Markdown, scientific claims/findings/actions/checks/limits | supports | Original native validate/render succeeds with exact Markdown. Original target hash verified at its frozen source; current target changed and is substantively reassessed. |
| septin-original-validation-organellar_chromatophore | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/adversary-septin/original-checks.json; Actual native original schema/render and historical target hash check | supports | Both commands exit0, Markdown exact. Frozen and current target hashes remain distinct for the stale chromatophore. |
| septin-native-organellar_chromatophore-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/organellar_chromatophore-uniprot-verify-receipt.json; Actual receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/organellar_chromatophore-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0. Independent whole-record inventory confirms zero protein examples, zero GENE_OR_PROTEIN nodes and no UniProtKB graph xrefs. Exit0 validates only that empty represented identifier scope; it does not certify complete molecular composition or biological claims. |
| septin-native-organellar_chromatophore-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/organellar_chromatophore-uniprot-causal-receipt.json; Actual receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/organellar_chromatophore-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Exit0. Independent whole-record inventory confirms zero protein examples, zero GENE_OR_PROTEIN nodes and no UniProtKB graph xrefs. Exit0 validates only that empty represented identifier scope; it does not certify complete molecular composition or biological claims. |
| plaque-current-4 | data/structures/membrane_organelle/nuclear_lumen.yaml; Entire current maintained record at e2edc3550e41792c2bb6f24eb2918b7d33d8a58c, including all components, graphs, discussions, history and image metadata | supports | Independently read current target; unchanged from original frozen target. |
| plaque-original-4 | reviews/structured/20261022T025107Z-nuclear-lumen-audit/review.yaml; Exact staleness-selected YAML plus native-rendered Markdown; source/check/assessment/finding/action fields | supports | Original native validation/rendering and every historical frozen input verified. Qualified pass with no scientific finding/action. |
| plaque-current-5 | data/structures/membrane_organelle/nuclear_net.yaml; Entire current maintained record at e2edc3550e41792c2bb6f24eb2918b7d33d8a58c, including all components, graphs, discussions, history and image metadata | supports | Independently read current target; unchanged from original frozen target. |
| plaque-original-5 | reviews/structured/20261022T025108Z-nuclear-net-audit/review.yaml; Exact staleness-selected YAML plus native-rendered Markdown; source/check/assessment/finding/action fields | supports | Original native validation/rendering and every historical frozen input verified. Qualified pass with no scientific finding/action. |
| plaque-current-8 | data/structures/membrane_organelle/nucleus.yaml; Entire current maintained record at e2edc3550e41792c2bb6f24eb2918b7d33d8a58c, including all components, graphs, discussions, history and image metadata | supports | Independently read current target; unchanged from original frozen target. |
| plaque-original-8 | reviews/structured/20261022T025110Z-nucleus-audit/review.yaml; Exact staleness-selected YAML plus native-rendered Markdown; source/check/assessment/finding/action fields | supports | Original native validation/rendering and every historical frozen input verified. One inherited minor author-attribution finding retained. |
| plaque-policy | .claude/skills/review-yaml-record/SKILL.md; Previously read frozen native policy bytes unchanged; current source/enum contract used | context_only | Native applicability includes named proteins, pathways, stress and traits; expression-module absence alone does not justify exclusion. Actual morphology/material-only scope can be genuinely excluded. |
| plaque-rubric | .claude/skills/curate-yaml-record/references/review-checklist.md; Previously read frozen native policy bytes unchanged; current source/enum contract used | context_only | Exact identity, source support, taxonomy, mechanism and necessity assessed separately. Optional inventory slots and uninspected-source absence are not automatic defects. |
| plaque-graph-rubric | .claude/skills/curate-causal-graphs/SKILL.md; Previously read frozen native policy bytes unchanged; current source/enum contract used | context_only | Descriptive topology and localization are distinct from mechanistic proof or necessity. |
| plaque-protein-contract | .claude/skills/uniprot-protein-examples/SKILL.md; Previously read frozen native policy bytes unchanged; current source/enum contract used | context_only | Native empty accession/node coverage is not evidence for every narrative molecular or pathway assertion. |
| plaque-schema-policy | src/cellstructuremech/schema/cellstructuremech.yaml; Previously read frozen native policy bytes unchanged; current source/enum contract used | context_only | OTHER is explicitly permitted; class prose emphasizing molecular building blocks does not alone establish a confirmed type defect for a correctly identified structural constituent. Complexes/families are permitted GENE_OR_PROTEIN nodes. |
| plaque-other-precedent | tests/test_trypanosome_structure_evidence.py; Freshly inspected test_faz1_rnai_does_not_establish_null_assembly_essentiality; exact OTHER structural-constituent assertion around line76 | context_only | Frozen before inspection. Maintained regression explicitly accepts structural FAZ filament as OTHER. This is bounded native modeling precedent, not biological evidence for nuclear structures or permission to retype a lipid incorrectly. |
| plaque-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031981,GO:0070013,GO:0005634,GO:0005637,GO:0000228,GO:0005730,GO:0005635,GO:0005643,GO:0006913,GO:0043231,GO:0005622,GO:0016020,GO:0044195,GO:0005654; Complete exact14-term response; definitions, synonyms, comments and typed children | supports | Exact nucleus/lumen/pore/inner membrane/chromosome/nucleolus identities and direct typed topology agree. Nucleoplasm is a nuclear-lumen part with definition excluding chromosomes/nucleolus, not an asserted exact synonym. GO0044195 includes lamina-associated channels and does not by itself exactly map the Polykrikos net; GO0005622 is a conservative broader parent. |
| plaque-GO0031981-isa | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031981/ancestors?relations=is_a; Complete exact current is_a ancestor response and typed children | supports | Nuclear lumen has intracellular organelle lumen ancestor0070013 and direct part_of chromosome/nucleolus/nucleoplasm children. Contains-part assertions are not inferred from untyped mixed ancestors. |
| plaque-GO0005634-isa | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005634/ancestors?relations=is_a; Complete exact current is_a ancestor response and typed children | supports | Nucleus has intracellular membrane-bounded organelle ancestor0043231, exact cell-nucleus synonym and envelope/lumen part_of children. Native definition preserves specialized RNA-metabolism/DNA-replication exceptions. |
| plaque-tax271679 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/271679; Complete current ENA identity, rank, lineage and aliases | supports | 271679 resolves to Polykrikos kofoidii species. Wild-collected pseudocolonies are not a named culture strain or species-wide prevalence sample. |
| plaque-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete current ENA identity, rank, lineage and aliases | supports | 4932 resolves to Saccharomyces cerevisiae species; BY4741-derived Duan and YEF473/L40 Pan preparations are kept distinct. |
| plaque-net-go-search | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=nuclear%20net&amp;limit=100&amp;page=1; QuickGO nuclear net query first100 returned terms; all returned names inspected, with exact candidate definitions checked in the separate14-term response | supports | Returned589 total hits; this bounded first page has no exact nuclear-net identity. Nucleoplasmic reticulum is a nearby candidate with extra lamina/function scope, not automatic equivalence. The record historical589-result survey is not represented as a newly exhaustive search. |
| plaque-duan2010-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038/nature08973&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact DOI bibliographic identity and complete native abstract | supports | Verified title, authors, DOI, publication year and returned source identifier. Primary/secondary distinctions are retained; abstract does not certify unread body or pixels. |
| plaque-boisvert2007-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038/nrm2184&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact DOI bibliographic identity and complete native abstract | supports | Verified title, authors, DOI, publication year and returned source identifier. Primary/secondary distinctions are retained; abstract does not certify unread body or pixels. |
| plaque-gavelis2019-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038/s41598-018-37065-w&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact DOI bibliographic identity and complete native abstract | supports | Verified title, authors, DOI, publication year and returned source identifier. Primary/secondary distinctions are retained; abstract does not certify unread body or pixels. |
| plaque-kalvelage2023-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128/msphere.00038-23&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact DOI bibliographic identity and complete native abstract | supports | Verified title, authors, DOI, publication year and returned source identifier. Primary/secondary distinctions are retained; abstract does not certify unread body or pixels. |
| plaque-lu2022-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1080/21541248.2021.1993714&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact DOI bibliographic identity and complete native abstract | supports | Verified title, authors, DOI, publication year and returned source identifier. Primary/secondary distinctions are retained; abstract does not certify unread body or pixels. |
| plaque-pan2000-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1091/mbc.11.7.2445%22&amp;format=json&amp;resultType=core&amp;pageSize=20; Exact DOI bibliographic identity and complete native abstract | supports | Verified title, authors, DOI, publication year and returned source identifier. Primary/secondary distinctions are retained; abstract does not certify unread body or pixels. |
| plaque-aitchison2012-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1534/genetics.111.127803%22&amp;format=json&amp;resultType=core&amp;pageSize=20; Exact DOI bibliographic identity and complete native abstract | supports | Verified title, authors, DOI, publication year and returned source identifier. Primary/secondary distinctions are retained; abstract does not certify unread body or pixels. |
| plaque-duan2010-bioc | https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_xml/PMC2874121/unicode; Genuine NCBI BioC text; passages2,6,12,13,14,16, independently read in full; title/DOI matched genuine numeric PMC HTML | supports | BY4741 bar1-derived haploid yeast formaldehyde crosslinking and genome-wide conformation capture support a population-based three-dimensional genome model. Model combines contact probabilities and known spatial landmarks; authors explicitly limit it as coarse-grained and population-based, not every-cell chromosome topology or all-eukaryote architecture. |
| plaque-duan2010-numeric | https://pmc.ncbi.nlm.nih.gov/articles/2874121/; Genuine PMC2874121 numeric HTML; title/DOI, complete Methods Summary S1 and Figure5 caption; no figure pixels/supplementary datasets | supports | Independent matching body verifies the BY4741-derived preparation, FDR strategy and modeled nuclear chromosome/nucleolus arrangement. Original canonical route returned a recaptcha challenge and was not article evidence. |
| plaque-boisvert2007-publisher | https://www.nature.com/articles/nrm2184; Publisher landing page SECONDARY REVIEW; title/authors, complete Key Points and Abstract only. Paywall offer and article metadata distinguished from unavailable full main text. | supports | Supports nucleolus ribosomal DNA transcription, pre-rRNA processing and ribosomal subunit assembly. This is a secondary synthesis, not a newly inspected primary perturbation or full article body. Additional stress/cell-cycle topics on the page are not imported into the maintained lumen record. |
| plaque-gavelis2019-body | https://pmc-oa-opendata.s3.amazonaws.com/PMC6351617.1/PMC6351617.1.xml; Genuine PMC6351617.1 JATS; entire Sec1 Introduction, Sec2 Results and Figure1–5 captions, Sec3 Discussion, Sec4 Conclusion, Sec5 Methods including Sec6–9; article authors, permissions and Fig3 graphic metadata | supports | Wild-collected Polykrikos pseudocolonies: one high-pressure-frozen/freeze-substituted FIB-SEM cell, four chemically fixed TEM cells and eight confocal specimens. Results explicitly describe double-membrane strands continuous with tunnels/envelope and periodic swellings; chemical fixation disrupts fine network. Super-resolution confirmation of centrin overlap, dynamic division and flow remain open. Only Fig3 pixels inspected; supplementary double-membrane image not independently inspected, so no new bilayer measurement claimed. |
| plaque-gavelis2019-fig3 | https://pmc-oa-opendata.s3.amazonaws.com/PMC6351617.1/41598_2018_37065_Fig3_HTML.jpg; Fresh complete figure binary, SHA256 compared byte-for-byte with frozen local image; all maintained panels A–G visually inspected through local view_image | supports | Image matches maintained file exactly. Grayscale sections with nodes/arrows and rendered red strands/tunnels1–6 agree with caption. Six is the depicted specimen count. Rendering does not demonstrate molecular composition, flow or causal division. JATS grants CC BY4.0 including images absent separate restrictive credit; Fig3 has no such credit. |
| plaque-stored-image | data/images/membrane_organelle/nuclear_net/pmc6351617_fig3.jpg; All pixels inspected with view_image; separate scratch image-inspection.json records observation and time | supports | All panels A-G visually inspected using view_image. A-C grayscale section insets show round/elongated light profiles and red arrowheads; C has5um scale. D-F show red segmented reticulating strands and tubes superimposed on section/green-blue surrounding anatomy; D has15um scale. G shows red connecting strands/swellings with six labelled tubes1-6. Image supports depicted segmentation/anatomy only; no molecular label, flow, causal mechanism, double-bilayer measurement or universal tunnel count inferred. |
| plaque-kalvelage2023-body | https://pmc-oa-opendata.s3.amazonaws.com/PMC10449503.1/PMC10449503.1.xml; Genuine PMC10449503.1 JATS; matching title/DOI, complete Conclusion s2-4 only; complete native abstract separately inspected. Remaining Results/Methods/supplements/pixels not read. | supports | Prorocentrum cordatum CCMP1329 study explicitly leaves nuclear-net investigation and dynamics for future work. It is not an independent full reconstruction of the Polykrikos-type network, and its broad proteomics does not identify nuclear-net constituents here. |
| plaque-pan2000-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC14931/; Same-PR fresh shared genuine PMC14931 HTML; independently reread Methods sec3, Results sec11/sec13/sec15 with included captions, Discussion sec19. No figure pixels, remaining Results or supplements. Original fetch timestamp preserved. | supports | YEF473/L40 yeast two-hybrid, cell-extract copurification and imaging support Vac8p–Nvj1p association at nucleus–vacuole junctions. Source infers direct interaction while explicitly acknowledging a remote indirect possibility; not purified binary reconstitution. Current canonical contact example is supported without extrapolating to whole-nucleus formation necessity or quantified species prevalence. |
| plaque-aitchison2012-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC3296253.1/PMC3296253.1.xml; Same-PR fresh shared genuine PMC3296253.1 JATS SECONDARY review; independently read opening body paragraph, s2 Overall Composition, s3 Membrane Ring and first3 direct paragraphs of s14 Mechanism of Nuclear Transport; no pixels or cited-primary rereview | supports | Supports NPC protein-complex identity and envelope openings/gated transport at the stated descriptive level. Selectivity and transport energy differ; virtual gating is not a literal opening/shutting gate or energy-free whole transport. Detailed Nup mechanisms and assembly necessities remain outside this record review. |
| plaque-lu2022-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC9707532/; Genuine PMC9707532 HTML title/DOI/citation_author metadata; full Results s0002-s2002 including Fig2 caption and Discussion s0003 including Fig5 caption. No other Results, movies, supplements or pixels inspected. | supports | Article explicitly names Michelle S Lu and David G Drubin, not Luo et al.2022.2021 online date and2022 volume year are distinguished. Cell-cycle-dependent Cdc42/Nvj1 fluorescence association supports bounded observations and proposed additional functions, not proven novel nuclear pathways. Maintained error is bibliographic attribution only. |
| plaque-catalogue | https://imodulondb.org/api/datasets; Complete fresh official /api/datasets response; every returned organism/dataset pair inspected | supports | No Saccharomyces, Polykrikos or other represented eukaryotic host. Positive lumen ribosome-biogenesis and nucleus transport/protein claims trigger applicability followed by bounded noncoverage; no downstream matched-gene/module query applies. Nuclear net exclusion rests on actual morphology-only claims, not catalogue absence. |
| plaque-historical-runner | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical00:49Z unavailable runner and retained stdout/stderr hashes | context_only | Historical PermissionError reading pyvenv.cfg is not a fresh invocation or success. Current catalogue and source fallback are separately documented. |
| plaque-original-checks | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/adversary-plaque/original-checks.json; Three original native validate/render executions plus historical/current hash checks | supports | Original pairs validate and render exactly;13/14/12 frozen historical inputs match retained source and all three target hashes remain unchanged. |
| plaque-native-nuclear_lumen-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/nuclear_lumen.yaml --verify; Actual root receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nuclear_lumen-uniprot-verify-receipt.json; stdoutSHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual inventory has zero protein_examples and zero GENE_OR_PROTEIN nodes. Native pass is empty represented accession/typed-node coverage, not proof of narrative molecular identity, pathway support or necessity. |
| plaque-native-nuclear_lumen-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/nuclear_lumen.yaml --causal-graphs; Actual root receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nuclear_lumen-uniprot-causal-receipt.json; stdoutSHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Actual inventory has zero protein_examples and zero GENE_OR_PROTEIN nodes. Native pass is empty represented accession/typed-node coverage, not proof of narrative molecular identity, pathway support or necessity. |
| plaque-native-nuclear_net-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/nuclear_net.yaml --verify; Actual root receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nuclear_net-uniprot-verify-receipt.json; stdoutSHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual inventory has zero protein_examples and zero GENE_OR_PROTEIN nodes. Native pass is empty represented accession/typed-node coverage, not proof of narrative molecular identity, pathway support or necessity. |
| plaque-native-nuclear_net-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/nuclear_net.yaml --causal-graphs; Actual root receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nuclear_net-uniprot-causal-receipt.json; stdoutSHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Actual inventory has zero protein_examples and zero GENE_OR_PROTEIN nodes. Native pass is empty represented accession/typed-node coverage, not proof of narrative molecular identity, pathway support or necessity. |
| plaque-native-nucleus-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/nucleus.yaml --verify; Actual root receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nucleus-uniprot-verify-receipt.json; stdoutSHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual inventory has zero protein_examples and zero GENE_OR_PROTEIN nodes. Native pass is empty represented accession/typed-node coverage, not proof of narrative molecular identity, pathway support or necessity. |
| plaque-native-nucleus-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/nucleus.yaml --causal-graphs; Actual root receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nucleus-uniprot-causal-receipt.json; stdoutSHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Actual inventory has zero protein_examples and zero GENE_OR_PROTEIN nodes. Native pass is empty represented accession/typed-node coverage, not proof of narrative molecular identity, pathway support or necessity. |
| micro-policy | .claude/skills/review-yaml-record/SKILL.md; Native skill, profile/config/output contract and checklist; structured-source section | context_only | Actual protein/pathway assertions trigger host coverage assessment, independent of whether expression data are asserted. No automatic query obligation for physical topology with molecular assertions explicitly withheld. |
| micro-component-policy | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent391-445, CausalNode and ComponentTypeEnum; native family/instance guidance | context_only | Molecular LIPID grounding differs from complete cellular-component membrane identity. Collective label-only material is permitted; source-neutral family/complex grounding differs from organism-specific xrefs. Essentiality concerns structure formation. Complexes are permitted under GENE_OR_PROTEIN; no enum-only defect. |
| micro-discussion-policy | docs/CURATION.md; Complete Discussions section305-324 and molecular-family/instance guidance | context_only | A discussion is provenance rather than a task description: prompt may be narrowed, rationale appended to and never replaced, notes hold current state, posed_date preserved. Historical rationale is not automatically a current erroneous scientific assertion. |
| micro-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Graph scope/edge evidence contract; frozen UniProt skill and verifier coverage | context_only | Coarse NONMECHANISTIC topology/transport edges retain source scope. UniProt xrefs on unanchored nodes are allowed; a representative accession does not identify all members of a grouped actor. |
| micro-record-nuclear_envelope | data/structures/membrane_organelle/nuclear_envelope.yaml; Entire maintained record, including history, all evidence/functions/components/graph edges/discussions | supports | Current target matches original frozen input exactly and was independently reassessed; no stale input in this slice. |
| micro-prior-nuclear_envelope | reviews/structured/20261022T025105Z-nuclear-envelope-audit/review.yaml; Complete native original envelope/checks/evidence/assessments/findings/actions/limitations and exact rendered Markdown | context_only | Historical verdict needs_curation; 1 original findings; explicit expression-only applicability exclusion, not an omitted row. Historical commands/access remain historical. |
| micro-native-nuclear_envelope-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nuclear_envelope-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/nuclear_envelope.yaml --verify; full log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nuclear_envelope-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0 at exact source. Zero examples and zero GENE_OR_PROTEIN nodes; NPC GO complex independently checked. Empty verifier pass is not molecular completeness. |
| micro-native-nuclear_envelope-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nuclear_envelope-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/nuclear_envelope.yaml --causal-graphs; full log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nuclear_envelope-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Exit0 at exact source. Zero examples and zero GENE_OR_PROTEIN nodes; NPC GO complex independently checked. Empty verifier pass is not molecular completeness. |
| micro-record-nuclear_envelope_lumen | data/structures/membrane_organelle/nuclear_envelope_lumen.yaml; Entire maintained record, including history, all evidence/functions/components/graph edges/discussions | supports | Current target matches original frozen input exactly and was independently reassessed; no stale input in this slice. |
| micro-prior-nuclear_envelope_lumen | reviews/structured/20261022T025106Z-nuclear-envelope-lumen-audit/review.yaml; Complete native original envelope/checks/evidence/assessments/findings/actions/limitations and exact rendered Markdown | context_only | Historical verdict pass_with_limitations; 0 original findings; explicit expression-only applicability exclusion, not an omitted row. Historical commands/access remain historical. |
| micro-native-nuclear_envelope_lumen-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nuclear_envelope_lumen-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/nuclear_envelope_lumen.yaml --verify; full log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nuclear_envelope_lumen-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0 at exact source. Zero examples and zero GENE_OR_PROTEIN nodes; this lumen asserts physical boundaries without resident proteins or transport machinery. |
| micro-native-nuclear_envelope_lumen-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nuclear_envelope_lumen-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/nuclear_envelope_lumen.yaml --causal-graphs; full log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nuclear_envelope_lumen-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Exit0 at exact source. Zero examples and zero GENE_OR_PROTEIN nodes; this lumen asserts physical boundaries without resident proteins or transport machinery. |
| micro-record-nuclear_inner_membrane | data/structures/membrane_organelle/nuclear_inner_membrane.yaml; Entire maintained record, including history, all evidence/functions/components/graph edges/discussions | supports | Current target matches original frozen input exactly and was independently reassessed; no stale input in this slice. |
| micro-prior-nuclear_inner_membrane | reviews/structured/20261022T025106Z-nuclear-inner-membrane-audit/review.yaml; Complete native original envelope/checks/evidence/assessments/findings/actions/limitations and exact rendered Markdown | context_only | Historical verdict needs_curation; 1 original findings; explicit expression-only applicability exclusion, not an omitted row. Historical commands/access remain historical. |
| micro-native-nuclear_inner_membrane-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nuclear_inner_membrane-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/nuclear_inner_membrane.yaml --verify; full log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nuclear_inner_membrane-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0 at exact source. Zero examples, three UNANCHORED_WITH_UNIPROT nodes with Q02821/Q03707/Q03281. Q02821 verifies only Kap60 within the named Kap60/Kap95 system, not complete pair coverage. |
| micro-native-nuclear_inner_membrane-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nuclear_inner_membrane-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/nuclear_inner_membrane.yaml --causal-graphs; full log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nuclear_inner_membrane-uniprot-causal.log SHA256 fb6b9ed140965b1c16457568c6a3389352df6b75ca5bc065608ed07296439c87 | supports | Exit0 at exact source. Zero examples, three UNANCHORED_WITH_UNIPROT nodes with Q02821/Q03707/Q03281. Q02821 verifies only Kap60 within the named Kap60/Kap95 system, not complete pair coverage. |
| micro-record-nuclear_outer_membrane | data/structures/membrane_organelle/nuclear_outer_membrane.yaml; Entire maintained record, including history, all evidence/functions/components/graph edges/discussions | supports | Current target matches original frozen input exactly and was independently reassessed; no stale input in this slice. |
| micro-prior-nuclear_outer_membrane | reviews/structured/20261022T025109Z-nuclear-outer-membrane-audit/review.yaml; Complete native original envelope/checks/evidence/assessments/findings/actions/limitations and exact rendered Markdown | context_only | Historical verdict needs_curation; 1 original findings; explicit expression-only applicability exclusion, not an omitted row. Historical commands/access remain historical. |
| micro-native-nuclear_outer_membrane-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nuclear_outer_membrane-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/nuclear_outer_membrane.yaml --verify; full log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nuclear_outer_membrane-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0 at exact source. Zero examples, two UNANCHORED_WITH_UNIPROT nodes with P38881/P39968; permissible node xrefs independently checked, not source-neutral family grounding. |
| micro-native-nuclear_outer_membrane-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nuclear_outer_membrane-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/nuclear_outer_membrane.yaml --causal-graphs; full log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nuclear_outer_membrane-uniprot-causal.log SHA256 20ca030cdfeb1a45fdd86dc1db1c8361c2cd5f5569a0fd1e3468470442253e23 | supports | Exit0 at exact source. Zero examples, two UNANCHORED_WITH_UNIPROT nodes with P38881/P39968; permissible node xrefs independently checked, not source-neutral family grounding. |
| micro-original-pairs | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/adversary-microtubule/original-checks.json; Four actual native validates and four render --content calls; exact Markdown comparisons | supports | All four original pairs validate and render exactly. |
| micro-original-inputs | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/adversary-microtubule/original-frozen-inputs.json; All68 original frozen input entries at their retained original source revisions | supports | All original hashes verify and four current targets are unchanged. Historical input hashing is provenance validation, not new scientific judgment of unfrozen context. |
| micro-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005635,GO:0031967,GO:0005634,GO:0005637,GO:0005640,GO:0005641,GO:0005643,GO:0006913,GO:0006998,GO:0031970,GO:0005788,GO:0031090,GO:0005774; Complete13 exact active terms: identities, definitions, synonyms and typed child relations | supports | Exact envelope5635, lumen5641, inner5637, outer5640 and pore5643 definitions distinguish whole structure, boundary bilayers, enclosed volume and protein complex. Envelope definition itself supplies20–40nm/lamina wording; it is not an independent experiment or universal taxon-specific measurement. NPC definition supports legitimate PROTEIN_COMPLEX grounding. |
| micro-go-0005635-isa | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005635/ancestors?relations=is_a; Complete relations=is_a ancestor response; no immediate-parent inference from transitive list | supports | Exact is_a ancestry supports organelle envelope0031967. Typed child relations and source topology separately support parthood. |
| micro-go-0005641-isa | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005641/ancestors?relations=is_a; Complete relations=is_a ancestor response; no immediate-parent inference from transitive list | supports | Exact is_a ancestry supports organelle envelope lumen0031970. Typed child relations and source topology separately support parthood. |
| micro-go-0005637-isa | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005637/ancestors?relations=is_a; Complete relations=is_a ancestor response; no immediate-parent inference from transitive list | supports | Exact is_a ancestry supports organelle membrane0031090. Typed child relations and source topology separately support parthood. |
| micro-go-0005640-isa | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005640/ancestors?relations=is_a; Complete relations=is_a ancestor response; no immediate-parent inference from transitive list | supports | Exact is_a ancestry supports organelle membrane0031090. Typed child relations and source topology separately support parthood. |
| micro-tax2759 | https://rest.uniprot.org/taxonomy/2759.json; taxonId, scientificName, rank and available parent/lineage | supports | Native taxonomy confirms 2759 Eukaryota (domain). Species/strain references do not establish experimental background or numerical prevalence. |
| micro-tax4932 | https://rest.uniprot.org/taxonomy/4932.json; taxonId, scientificName, rank and available parent/lineage | supports | Native taxonomy confirms 4932 Saccharomyces cerevisiae (species). Species/strain references do not establish experimental background or numerical prevalence. |
| micro-tax559292 | https://rest.uniprot.org/taxonomy/559292.json; taxonId, scientificName, rank and available parent/lineage | supports | Native taxonomy confirms 559292 Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (strain). Species/strain references do not establish experimental background or numerical prevalence. |
| micro-protein-Q02821 | https://rest.uniprot.org/uniprotkb/Q02821.json; primaryAccession, reviewed status, recommended protein name, primary/synonym/locus gene fields, taxon559292; FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments | supports | Reviewed S288C reference Q02821: SRP1, synonym KAP60, YNL189W. Correct reference instance and source-compatible role; not every assay strain or a complete source-neutral family inventory. |
| micro-family-Q02821 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q02821/?page_size=200; Exact InterPro integrated-entry association endpoint; page_size200; complete available results | supports | Exact protein-associated InterPro response has 7 entries; family entries IPR024931 Importin subunit alpha. Domains/repeats/superfamilies remain distinct; no proposed automatic record mutation. |
| micro-protein-Q03707 | https://rest.uniprot.org/uniprotkb/Q03707.json; primaryAccession, reviewed status, recommended protein name, primary/synonym/locus gene fields, taxon559292; FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments | supports | Reviewed S288C reference Q03707: SRC1, synonym HEH1, YML034W (YML033W ORF alias). Correct reference instance and source-compatible role; not every assay strain or a complete source-neutral family inventory. |
| micro-family-Q03707 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q03707/?page_size=200; Exact InterPro integrated-entry association endpoint; page_size200; complete available results | supports | Exact protein-associated InterPro response has 4 entries; family entries IPR044780 Heh2/Src1-like. Domains/repeats/superfamilies remain distinct; no proposed automatic record mutation. |
| micro-protein-Q03281 | https://rest.uniprot.org/uniprotkb/Q03281.json; primaryAccession, reviewed status, recommended protein name, primary/synonym/locus gene fields, taxon559292; FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments | supports | Reviewed S288C reference Q03281: HEH2, YDR458C. Correct reference instance and source-compatible role; not every assay strain or a complete source-neutral family inventory. |
| micro-family-Q03281 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q03281/?page_size=200; Exact InterPro integrated-entry association endpoint; page_size200; complete available results | supports | Exact protein-associated InterPro response has 5 entries; family entries IPR044780 Heh2/Src1-like. Domains/repeats/superfamilies remain distinct; no proposed automatic record mutation. |
| micro-protein-P38881 | https://rest.uniprot.org/uniprotkb/P38881.json; primaryAccession, reviewed status, recommended protein name, primary/synonym/locus gene fields, taxon559292; FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments | supports | Reviewed S288C reference P38881: NVJ1, synonym VAB36, YHR195W. Correct reference instance and source-compatible role; not every assay strain or a complete source-neutral family inventory. |
| micro-family-P38881 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P38881/?page_size=200; Exact InterPro integrated-entry association endpoint; page_size200; complete available results | supports | Exact P38881 association request returned204/no content. This bounded response does not establish global absence of an Nvj1 family or justify guessing one. |
| micro-protein-P39968 | https://rest.uniprot.org/uniprotkb/P39968.json; primaryAccession, reviewed status, recommended protein name, primary/synonym/locus gene fields, taxon559292; FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments | supports | Reviewed S288C reference P39968: VAC8, synonym YEB3, YEL013W. Correct reference instance and source-compatible role; not every assay strain or a complete source-neutral family inventory. |
| micro-family-P39968 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P39968/?page_size=200; Exact InterPro integrated-entry association endpoint; page_size200; complete available results | supports | Exact protein-associated InterPro response has 4 entries; family entries IPR045156 Vacuolar protein 8. Domains/repeats/superfamilies remain distinct; no proposed automatic record mutation. |
| micro-hetzer2010-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1101/cshperspect.a000539%22&amp;format=json&amp;resultType=core&amp;pageSize=20; Exact quoted DOI EuropePMC core search, pageSize20, unique MED title/authors/year/DOI/PMID and complete abstract | context_only | Citation identity and complete abstract agree with the inspected secondary review; record title/year and narrow biological scope checked. Metadata alone is not full-body reading. |
| micro-aitchison2012-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1534/genetics.111.127803%22&amp;format=json&amp;resultType=core&amp;pageSize=20; Exact quoted DOI EuropePMC core search, pageSize20, unique MED title/authors/year/DOI/PMID and complete abstract | context_only | Citation identity and complete abstract agree with the inspected secondary review; record title/year and narrow biological scope checked. Metadata alone is not full-body reading. |
| micro-pan2000-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1091/mbc.11.7.2445%22&amp;format=json&amp;resultType=core&amp;pageSize=20; Exact quoted DOI EuropePMC core search, pageSize20, unique MED title/authors/year/DOI/PMID and complete abstract | supports | Citation identity and complete abstract agree with the inspected primary study; record title/year and narrow biological scope checked. Metadata alone is not full-body reading. |
| micro-king2006-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038/nature05075%22&amp;format=json&amp;resultType=core&amp;pageSize=20; Exact quoted DOI EuropePMC core search, pageSize20, unique MED title/authors/year/DOI/PMID and complete abstract | supports | Citation identity and complete abstract agree with the inspected primary study; record title/year and narrow biological scope checked. Metadata alone is not full-body reading. |
| micro-hetzer2010-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC2829960/; Genuine canonical PMC body: opening paragraphs/Table1 context/Figure1 caption, complete s1,s7,s9,s10 and embedded captions; no image pixels | context_only | Secondary review supports double-envelope topology, perinuclear/ER continuity, pore transport and organization. Closed yeast/fungal mitosis differs from metazoan envelope breakdown. In-vitro assembly systems and debated mechanisms do not establish universal molecular formation necessity. |
| micro-aitchison2012-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC3296253.1/PMC3296253.1.xml; Genuine JATS opening main paragraphs, complete s1-s3,s10,s14 with embedded captions; partial s11 text not used for additional claims; no pixels | context_only | Secondary yeast NPC review supports protein-complex architecture, envelope span and selective nucleocytoplasmic transport. Transport driving gradients and soluble machinery are distinct from intrinsic pore gating; no pore-powered universal mechanism or complete inventory inferred. |
| micro-pan2000-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC14931/; Genuine PMC body Methodssec3-6,9; Resultssec11-17 and complete Discussionsec18-20, embedded Figure1-9 captions; no pixels or unlisted Methods | supports | YEF473/L40 yeast localization, two-hybrid, copurification, deletion/overexpression and TEM support Nvj1 nuclear-envelope/Vac8 vacuole contacts. Authors interpret direct interaction but explicitly retain a remote indirect-binding possibility insec11. NVJ necessity is not entire nuclear-membrane formation necessity; bacterial/strain conflation avoided. |
| micro-king2006-supp | https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fnature05075/MediaObjects/41586_2006_BFnature05075_MOESM1_ESM.pdf; Genuine publisher PDF: textual FiguresS1-S5 captions, complete Supplementary Methods and Tables1-2 including strain footnote; no pixels | supports | Heh localization/Ran-mutant assays, NLS constructs and strain details support yeast targeting scope. Strains are W303-derived except named backgrounds including BY4741; not uniformly S288C. S1 is a model and predicted NLSs are distinguished from tested sequences. |
| micro-king2006-browser-opening | https://www.researchgate.net/publication/6859612_King_MC_Lusk_CP_Blobel_G_Karyopherin-mediated_import_of_integral_inner_nuclear_membrane_proteins_Nature_442_1003-1007; Browser-displayed author-uploaded primary opening/Introduction and selected Results/Discussion/Methods; printed1003-1006, displayed lines67-848 in returned excerpt | supports | Actual current browser-displayed primary author text supports named yeast Heh1/Heh2 cargo targeting via Ran/Kap60/Kap95, with direct Heh2-Kap60 binding and NLS perturbation. Retention and proposed NPC rearrangements remain limited interpretations. Browser snapshot is not a native HTTP200 full-PDF attestation; no image pixels or unread lines certified. |
| micro-king2006-browser-body | https://www.researchgate.net/publication/6859612_King_MC_Lusk_CP_Blobel_G_Karyopherin-mediated_import_of_integral_inner_nuclear_membrane_proteins_Nature_442_1003-1007; Additional browser excerpts displayed lines41-415 and345-715, including Heh1/Heh2 identity/localization, Kap60 pull-down, NLS-deletion/swap results and Figure1-3 captions | supports | Actual current browser-displayed primary author text supports named yeast Heh1/Heh2 cargo targeting via Ran/Kap60/Kap95, with direct Heh2-Kap60 binding and NLS perturbation. Retention and proposed NPC rearrangements remain limited interpretations. Browser snapshot is not a native HTTP200 full-PDF attestation; no image pixels or unread lines certified. |
| micro-king2006-main-access | https://www.nature.com/articles/nature05075.pdf; Inspected HTTP200 body begins HTML, not PDF; attempted pdftotext rejected non-PDF bytes | context_only | Publisher main-PDF route returned subscription-preview HTML, not a recovered PDF. Scientific body assessment uses separately timestamped browser author text and genuine supplement. Hetzer/Pan S3 candidate routes returned404; their canonical PMC bodies succeeded. |
| micro-catalogue | https://imodulondb.org/api/datasets; Complete official array: all20 organism rows/28 organism-dataset pairs inspected | supports | No Saccharomyces/cerevisiae/S288C/W303/YEF473/L40 or eukaryotic host dataset occurs in this bounded catalogue. No matched downstream gene/module search or bacterial surrogate is warranted. Noncoverage does not refute nuclear-envelope biology. |
| micro-historical-runner | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical00:49Z runner attempt/exit1/PermissionError reading pyvenv.cfg | context_only | Historical optional runner unavailable, not rerun or falsely dated current. Current official catalogue fallback succeeded independently. |
| check-qc | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/qc.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| check-labels | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/labels.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| check-trait-links | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/trait-links.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Native TraitMech link check passed. |
| check-vendored | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/vendored.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Pinned governed files match; native vendored check passed. |
| check-curies | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/curies.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| focused | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/focused-results.json; All twenty actual target schema/strict command outputs | supports | Ten schema and ten strict commands returned exit zero. |
| supplemental-pmid | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/pmid-chunks-receipt.json; Complete native-report PMID set checked with unchanged resolver in batches of at most fifty | supports | 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers remain unverified. |
| historical-adapter-runner-availability | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical runner invocation receipt, exact SHA256 reverified during PR2372 synthesis | context_only | Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS PermissionError reading the configured runner pyvenv.cfg. This is a retained historical availability observation, not a fresh attempt or a scientific validation failure. Native policy permits inspected source-catalogue fallback. |

## Limits And Additional Notes

- Nitroplast, nucleomorph and organellar chromatophore independent subreview: Read-only independent source review of three assigned targets; root owns issue dedup/publication and global gates. No repository/record/GitHub mutation and no certification of later saved-head, CI or queue.
- Nitroplast, nucleomorph and organellar chromatophore independent subreview: Two original inputs are unchanged; chromatophore changed only by a parthood edge and historical curation event. Original historical source hashes/native schema/render were verified separately from frozen current bytes, and the complete current record was reassessed.
- Nitroplast, nucleomorph and organellar chromatophore independent subreview: All substantive source snapshots used here were freshly fetched with actual receipts. Initial publisher/PMC HTTP200 challenge bodies and later failed XML requests are explicitly not treated as full text. Subsequent genuine Nowack PMC and Tanifuji/Onuma/Li XML are separately scoped; no cached historical body is silently relabeled fresh.
- Nitroplast, nucleomorph and organellar chromatophore independent subreview: Coale primary article page text is a public manuscript/article-page representation, not platform-generated summary prose; read pages1,3,4,5 and supplement2,7,11. Figure captions are text access, not raw image/pixel quantification; FigS3 only caption was inspected. Predicted uTP candidates remain distinct from enriched proteins.
- Nitroplast, nucleomorph and organellar chromatophore independent subreview: Hagino genuine PDF sections and actual rendered cover/Table2/Fig28–31 pixels were inspected. FR21 panels28/29 are distinguished from OTR22-B panels30/31; copyright checked on article first page PDF2. Linked OTHER is not a redistribution licence. Culture-specific loss is not wild prevalence or a proven causal mechanism.
- Nitroplast, nucleomorph and organellar chromatophore independent subreview: Curtis2012 and Singer2017 are complete primary abstracts plus verified metadata, not full bodies. Nowack2014 and Gabr2020 are secondary abstracts. Unread source details remain uncertain; access limitation does not refute their science.
- Nitroplast, nucleomorph and organellar chromatophore independent subreview: Tanifuji and Onuma were read at stated body sections/captions/Methods only. No raw sequence, supplementary datasets, figure pixels or quantitative reanalysis. L.oceanica chromosomeI repeat uncertainty and partial G.theta synchronization limit extrapolation.
- Nitroplast, nucleomorph and organellar chromatophore independent subreview: Li2026 XML identifies version1 preprint; only stated Discussion/limitations and front metadata were read. No proof of vesicle cargo/direction, transporter identity, gating causality or density composition is inferred.
- Nitroplast, nucleomorph and organellar chromatophore independent subreview: Native six protein commands pass on zero examples, zero typed molecular nodes and zero UniProt graph xrefs. This empty represented coverage does not validate all narrative molecular claims, composition completeness or formation necessity.
- Nitroplast, nucleomorph and organellar chromatophore independent subreview: Fresh full catalogue has20organisms/28organism-dataset pairs/22distinct strings and no matched named host/endosymbiont. Synechococcus elongatus is not an interchangeable cyanobacterial organelle proxy. All three full-record molecular scopes trigger applicability assessment; downstream calls are N/A for lack of matched coverage, not biological absence. Historical00:49Z runner failure is not a fresh invocation.
- Nitroplast, nucleomorph and organellar chromatophore independent subreview: Two exact chromatophore findings/actions preserve original severity, stable keys and repository/review/finding lineage. No new scientific finding. Nitroplast structural OTHER is supported by the native schema/test; nucleomorph collective DNA essentiality is not mistaken for a measured individual formation requirement.
- Nitroplast, nucleomorph and organellar chromatophore independent subreview: All29 actually used local repository inputs were frozen before use:17 common policies/scripts/schema,3targets,6original artifacts,2boundary neighbors and1structural-type test. Neighbor findings, prior grouped/category issues and historical curation dispositions are not resolved by this review.
- Nuclear lumen, nuclear net and nucleus independent subreview: All three targets unchanged; nuclear lumen and nuclear net remain pass_with_limitations, nucleus needs_curation only for inherited minor nucleus-lu-drubin-attribution. No new scientific finding.
- Nuclear lumen, nuclear net and nucleus independent subreview: Original native validation/exact rendering and13/14/12 historical frozen input hashes match. No records/originals edited; old history mentions and historical589-result ontology survey are not freshly exhaustive or terminally re-adjudicated.
- Nuclear lumen, nuclear net and nucleus independent subreview: Duan primary model is population-based BY4741-derived conformation capture, not all-cell/all-eukaryote topology. Selected BioC passages, matching numeric PMC Methods Summary and Fig5 caption read; no pixels/supplements/raw contact matrices. Original canonical fetch returned recaptcha, not usable body.
- Nuclear lumen, nuclear net and nucleus independent subreview: Boisvert secondary review is complete abstract and publisher Key Points only; full main article is paywalled and not claimed read. Aitchison secondary review is limited to opening body/s2/s3/first3s14 paragraphs, not a cited-primary assay audit.
- Nuclear lumen, nuclear net and nucleus independent subreview: Gavelis main Introduction/Results/Discussion/Conclusion/Methods and Fig1–5 captions read; only maintained Fig3 pixels inspected. Primary Results describe double membranes using supplementary evidence not independently viewed, so no new bilayer measurement. One reconstructed wild specimen plus four TEM/eight confocal specimens do not establish universal count, dynamics, molecular inventory or prevalence.
- Nuclear lumen, nuclear net and nucleus independent subreview: Fresh Fig3 bytes equal stored SHA; source permission is CC BY4.0, eight author attribution and caption/modality agree. No restrictive separate Fig3 credit. Rendered topology does not establish flow, centrin incorporation or a division mechanism.
- Nuclear lumen, nuclear net and nucleus independent subreview: Kalvelage complete Conclusion and native abstract only; future nuclear-net work remains prospective. Current bounded QuickGO first100/589-result query is not exhaustive absence proof; historical full search remains historical.
- Nuclear lumen, nuclear net and nucleus independent subreview: Pan shared fresh body independently reread Methods3/Results11,13,15/Discussion19 with included captions. Direct interaction is the paper interpretation of two-hybrid/copurification with a remote indirect caveat, not purified binary reconstitution. Lu genuine body metadata/Results s0002-s2002/Discussion s0003 and Fig2/5 captions read; other Results/pixels/movies not claimed.
- Nuclear lumen, nuclear net and nucleus independent subreview: All six actual native protein commands pass on zero examples/zero typed nodes. This does not validate narrative protein/pathway claims; GO-grounded NPC structural actor is checked manually. OTHER structural components and permitted complex node types are not automatic enum or chemical defects.
- Nuclear lumen, nuclear net and nucleus independent subreview: Lumen/nucleus explicit no-expression exclusions require correction from actual positive claims. Nuclear net is a genuine morphology/topology exclusion with molecular actors expressly withheld. Fresh full catalogue has no exact eukaryotic host; no downstream query or foreign proxy, and no negative biology. Historical00:49Z runner failure remains historical unavailable.
- Nuclear lumen, nuclear net and nucleus independent subreview: Root owns global QC, issue publication, successor writing, final CI and merge. This source report only binds independent current assessment and scratch native preflight; no future gate certification.
- Nuclear envelope and three boundary compartment independent subreview: Four complete unchanged nuclear-envelope targets independently reassessed. One inherited major molecular-grounding finding remains open; two inherited minor rationale-only findings are rejected with exact predecessor lineage under native discussion-provenance policy. No new scientific finding, record edit or broader issue/category disposition.
- Nuclear envelope and three boundary compartment independent subreview: Hetzer2010 and Aitchison2012 are secondary reviews, not direct primary experiments. Their exact declared body sections/captions were inspected; no pixels or unlisted sections certified. Native GO20–40nm/lamina wording is ontology-derived; it is not a universal source-specific measurement or universal yeast lamina statement.
- Nuclear envelope and three boundary compartment independent subreview: Pan2000 primary body scope is Methods3-6,9; Results11-17; Discussion18-20 and embedded captions. Two-hybrid/copurification/contact perturbations support authors direct-interaction interpretation with their explicit remote indirect-binding caveat. Assays useYEF473/L40 backgrounds, not automaticallyS288C. No entire-membrane formation requirement inferred.
- Nuclear envelope and three boundary compartment independent subreview: King2006 main-PDF URL returnedHTML preview and pdftotext rejected it. Current author-uploaded browser excerpts cover stated results/discussion/methods passages; separate genuine publisher supplement provides captions/Methods/Tables includingW303/namedexceptions. No native full main-PDF recovery, image pixels or unshown browser lines certified. No universal INM targeting mechanism inferred.
- Nuclear envelope and three boundary compartment independent subreview: Five current reviewedUniProt references support exact names/synonyms/loci/taxa. Nativeinner3 andouter2 UNANCHORED_WITH_UNIPROT are permissible xref coverage; other2 targets zero examples/nodes. RepresentativeKap60 does not identifyKap95. Protein instances, source-neutral families, localization and formation necessity remain distinct.
- Nuclear envelope and three boundary compartment independent subreview: InterPro association requests are bounded to five exact protein accessions, page_size200; four complete returned lists, oneP38881HTTP204. No universal family absence, automatic groundings or mandatory new inventory inferred.
- Nuclear envelope and three boundary compartment independent subreview: Wholeenvelope/inner/outer original explicit expression-only exclusions need corrected actual-host assessment; lumen is a genuine physical/topology exclusion. Fresh official catalogue has no matching yeast/eukaryotic dataset. Historical00:49Z runner failure is not a new execution; successful catalogue fallback does not imply matched downstream module queries.
- Nuclear envelope and three boundary compartment independent subreview: The rejected original actions did include preserve-historical-context language. Their unsupported defect and acceptance criterion are corrected without alleging they explicitly ordered wholesale history deletion. Optional progress notes can be useful but are not required scientific curation; source-neutral prompts remainvalid.
- Nuclear envelope and three boundary compartment independent subreview: All68 original input entries were provenance-hashed at originalrevision; only29 actually used current local inputs are listed. No historicalcontext file was newly assessed merely because its hash was checked. No repository or GitHub mutation; root owns globalQC/finalCI/queue and this source report does not precertify them.
- Historical observations remain immutable; their old checks are not represented as current-head execution.
- The adapter runner was not rerun after the canary established OS access failure. Catalogue-based coverage is assessed directly; fresh and reused responses retain actual access timestamps.
- Native label checks include 923 no-adapter skips. Native identifier checks include 909 PMID transport failures and 254 skipped identifiers; bounded supplemental checks independently resolve the 909 PMIDs.
- Scientific record-curation findings stay in separate issues; no record is edited by this review PR.
- Final trusted-base post-save review-check, exact-head independent acceptance, final-head CI and merge-group CI occur after saving this immutable observation and are not represented here as already completed.
- All ten original YAML/Markdown pairs remain unchanged. Current main was merged normally and pushed without force.
- This explicit issue-bearing ten-record cohort follows native persistence policy. Inherited scientific findings retain stable keys and exact predecessor repository/review/finding identities; any new finding has no invented predecessor.
- Issue2748 tracks the stale organellar chromatophore review. The new thylakoid-membrane parthood edge and history require substantive current-source verification of ontology path, source scope and biological claim, not a hash-only refresh.
- Issue2749 tracks eight unsupported expression-only applicability exclusions. Nuclear envelope lumen and nuclear net retain genuine physical/material-topology scope with molecular machinery explicitly excluded or withheld. All ten originals contained explicit exclusions; none was missing.
- Issue2750 corrects the two inherited inner/outer membrane stale-rationale findings. Their unchanged rationale is append-only historical provenance, their prompts still seek source-neutral grounding, and organism-specific xrefs do not complete family or grouped-actor grounding. Explicit rejected dispositions preserve exact predecessors; optional progress notes are not elevated to mandatory record curation.
- Source commit e2edc3550e41792c2bb6f24eb2918b7d33d8a58c is retained by tag review-base/pr2372-current-record-followup-20261103.
- CLAUDE.md aliases AGENTS.md; canonical regular AGENTS.md bytes are frozen. Every used local context input is frozen before its assessment.
- Fresh and reused source snapshots retain actual access times and inspection tiers. Native identifier identity does not independently establish structure membership, experimental intervention scope or assembly necessity.
- All twenty native protein commands returned zero. None of the ten records has protein examples. Nuclear inner membrane has three UNANCHORED_WITH_UNIPROT typed nodes and nuclear outer membrane has two; these are not falsely called COVERED. The other eight records have zero typed molecular nodes. Optional example absence alone is not a scientific defect.
- The nuclear-net local image is a frozen review input; its pixels, primary caption, preparation and source permissions are assessed independently of molecular-composition claims.
- Current CausalNode schema permits protein families and complexes as GENE_OR_PROTEIN nodes. Optional protein/chemical slots, allowed structural OTHER constituents and unread-source absence are not invented findings.
- Native-validator2514 remains open and reused; no scientific record or native resolver is edited in this review-only PR.
- Final trusted-base review-check, exact-head independent acceptance, final-head CI and merge-group CI occur after this immutable observation and are not represented as already completed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T181239Z-pr2372-current-record-followup
kind: batch
repository: CultureBotAI/CellStructureMech
title: 'PR 2372: current-input review of ten records and adversarial follow-up'
started_at: '2026-11-03T18:01:05.412555Z'
finished_at: '2026-11-03T18:12:39Z'
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
summary: Current-input adversarial follow-up for the complete ten-record cohort after
  merging main. One stale organellar chromatophore review is substantively refreshed
  against its added thylakoid-membrane parthood edge and source scopes. Eight unsupported
  expression-only structured-source exclusions are corrected; nuclear envelope lumen
  and nuclear net retain genuine physical/topology exclusions. Two inherited rationale-only
  findings are explicitly rejected under native historical-provenance policy. Four
  other inherited findings remain open (two major and two minor) across three records;
  seven targets retain qualified positive assessments. All original review observations
  and scientific records remain unchanged.
source:
  git_revision: e2edc3550e41792c2bb6f24eb2918b7d33d8a58c
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
  - path: data/images/membrane_organelle/nuclear_net/pmc6351617_fig3.jpg
    sha256: 9f2cd13af66cdb9f0321d5a23b6381a3cf3fd7d087be5e87b68c1176619db3de
    role: context
  - path: data/structures/membrane_organelle/diazoplast.yaml
    sha256: fd3948e827eb4a9870bc4eccb09689dd5c82f5caef443f1e319daabbf21bb038
    role: context
  - path: data/structures/membrane_organelle/nitroplast.yaml
    sha256: 3f7dc36b6c5e8389c881e64839227e1e5cdde49edb55277e245b180f0de8d6a8
    role: target
  - path: data/structures/membrane_organelle/nuclear_envelope.yaml
    sha256: 226a12a5500d39f1afbc5baa0f3a81891d6ae4918f4d6c29e8ce05de0df9979a
    role: target
  - path: data/structures/membrane_organelle/nuclear_envelope_lumen.yaml
    sha256: 1c45350eaa4a19474f4689125aadc8aa93d1824d41303e3c4aaff1f7e1db6019
    role: target
  - path: data/structures/membrane_organelle/nuclear_inner_membrane.yaml
    sha256: c0484a80c2b1568174ca7f9c96805a6ce2749a3ba27b700e21fb1de2aef4e4df
    role: target
  - path: data/structures/membrane_organelle/nuclear_lumen.yaml
    sha256: dbb07d267c0272e4deb338a2e8a0e29892a6f1d28f279160c3d42f730410fb49
    role: target
  - path: data/structures/membrane_organelle/nuclear_net.yaml
    sha256: 8b4a54d13a70cfb4fdce9bd18ae990793f9de9627fdca067573c033335d847ba
    role: target
  - path: data/structures/membrane_organelle/nuclear_outer_membrane.yaml
    sha256: a760b04919cb0a80c89fd2eee5c1d4a0c940fc15a17b77b4b1810b9e1d2b2ffb
    role: target
  - path: data/structures/membrane_organelle/nucleomorph.yaml
    sha256: 9653087b981991e28b537ec1eb809e442f5215f4ff4c994687106b74ed6338ad
    role: target
  - path: data/structures/membrane_organelle/nucleus.yaml
    sha256: 889818b3c6a37074924a97bc81271f43ef236dc9112a871c5e521dae123e497d
    role: target
  - path: data/structures/membrane_organelle/organellar_chromatophore.yaml
    sha256: b217af7ad434f269a5b8cba2428be5cd988746a75c34a999d7b69909160fcba4
    role: target
  - path: data/structures/membrane_organelle/plastid.yaml
    sha256: 1be30ab06bc2fbae9294930ceaf74b20a2d43d8af60986aa9ed0e07b9645ae81
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
  - path: reviews/structured/20261022T025104Z-nitroplast-audit/review.md
    sha256: 1b6d1ceabaeab117092471e6342bd2aa8cd721fe94282f727f8c304c8229392c
    role: context
  - path: reviews/structured/20261022T025104Z-nitroplast-audit/review.yaml
    sha256: f034b9ac17575a9ca841adbd8ae13fa6c7c9ddb8087d88f7d298ed9adb00fa3f
    role: context
  - path: reviews/structured/20261022T025105Z-nuclear-envelope-audit/review.md
    sha256: f8715357e67aa36e647644d19871f024b533cc1eac4e2e01d55b18e5e3e37f69
    role: context
  - path: reviews/structured/20261022T025105Z-nuclear-envelope-audit/review.yaml
    sha256: cd4b3af2f9828842fac4d7513911c27c8e2f027f6e5f1ff86e3f0ce4f7c2cfdc
    role: context
  - path: reviews/structured/20261022T025106Z-nuclear-envelope-lumen-audit/review.md
    sha256: ac747a8c6a714229780e9deceaec95bccc41bb7f038ca0168bfe73eed946855b
    role: context
  - path: reviews/structured/20261022T025106Z-nuclear-envelope-lumen-audit/review.yaml
    sha256: 9d2d2460b5eff950722b451fa44e83a238438569b3d2bf470cb7a0826f73d41b
    role: context
  - path: reviews/structured/20261022T025106Z-nuclear-inner-membrane-audit/review.md
    sha256: 409a9efec40f847b3bac6918c873a945f8c62f5683655aaccfd06b77aea43b9f
    role: context
  - path: reviews/structured/20261022T025106Z-nuclear-inner-membrane-audit/review.yaml
    sha256: 535d5cd2e1edd2fd3ae0a9bad913cd1a02b7aef1c1540d4fd90a5e4aa794e995
    role: context
  - path: reviews/structured/20261022T025107Z-nuclear-lumen-audit/review.md
    sha256: e14ab37212ad0790b23947a2771fc3099547def847dcf1acd85a99b0786695ba
    role: context
  - path: reviews/structured/20261022T025107Z-nuclear-lumen-audit/review.yaml
    sha256: 353fc9e94a16c04dee2d5496757cda72a8c963a63a1b1dd0ae7f22cf3aa80b80
    role: context
  - path: reviews/structured/20261022T025108Z-nuclear-net-audit/review.md
    sha256: ecf2aab9a5f17a1769d8d9a129bf73b88734b0c9b9fac01b8336d60ce2cd08ab
    role: context
  - path: reviews/structured/20261022T025108Z-nuclear-net-audit/review.yaml
    sha256: 93203662120118e658e0b1c4b153b0b57eabea264ee93c911050f433d0934c7f
    role: context
  - path: reviews/structured/20261022T025109Z-nuclear-outer-membrane-audit/review.md
    sha256: 7391f00ab6adc80b4d68a998067cc200c6c473ffe32b624e2030e02943a227db
    role: context
  - path: reviews/structured/20261022T025109Z-nuclear-outer-membrane-audit/review.yaml
    sha256: c0ff2eb9462a8d2dd8a32dd25b10ba8e30cb69766b5715134e47d08a626410c5
    role: context
  - path: reviews/structured/20261022T025109Z-nucleomorph-audit/review.md
    sha256: f3e80944d48ae3e57646f0018610ef58c2b5d7136e115575359e37d86d167ff2
    role: context
  - path: reviews/structured/20261022T025109Z-nucleomorph-audit/review.yaml
    sha256: c22769a4c692c08d6ebbbe0c6e2ca1fd2831137527e64f953e57b96308ef7b8e
    role: context
  - path: reviews/structured/20261022T025110Z-nucleus-audit/review.md
    sha256: 6b23ffd1302071847655611a607b42106047b35168eb3e38d89bfda577bbd6c3
    role: context
  - path: reviews/structured/20261022T025110Z-nucleus-audit/review.yaml
    sha256: fcb0c90aec7a09925a927546f6692961337c99e8ee195d3fab6912c1b7e6b27c
    role: context
  - path: reviews/structured/20261022T025111Z-organellar-chromatophore-audit/review.md
    sha256: 619a63bbe0dfffa64b8b57bca1f4bd2425196c30a17d049fa001dc039d2391ab
    role: context
  - path: reviews/structured/20261022T025111Z-organellar-chromatophore-audit/review.yaml
    sha256: b2527e711f4050d12ae0fed598c88bd0f02d93578180ed97bdba96bcf8cd35f7
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
  - path: tests/test_trypanosome_structure_evidence.py
    sha256: 7ce1dfa869f9295e836fff7a7956e62685ac291969283c5311e08c7fad5cf79b
    role: context
targets:
- target_id: cellstructuremech:nitroplast
  path: data/structures/membrane_organelle/nitroplast.yaml
  label: nitroplast
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/nitroplast.yaml
    role: maintained scientific record
- target_id: GO:0005635
  path: data/structures/membrane_organelle/nuclear_envelope.yaml
  label: nuclear envelope
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/nuclear_envelope.yaml
    role: maintained scientific record
- target_id: GO:0005641
  path: data/structures/membrane_organelle/nuclear_envelope_lumen.yaml
  label: nuclear envelope lumen
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/nuclear_envelope_lumen.yaml
    role: maintained scientific record
- target_id: GO:0005637
  path: data/structures/membrane_organelle/nuclear_inner_membrane.yaml
  label: nuclear inner membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/nuclear_inner_membrane.yaml
    role: maintained scientific record
- target_id: GO:0031981
  path: data/structures/membrane_organelle/nuclear_lumen.yaml
  label: nuclear lumen
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/nuclear_lumen.yaml
    role: maintained scientific record
- target_id: cellstructuremech:nuclear_net
  path: data/structures/membrane_organelle/nuclear_net.yaml
  label: nuclear net
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/nuclear_net.yaml
    role: maintained scientific record
- target_id: GO:0005640
  path: data/structures/membrane_organelle/nuclear_outer_membrane.yaml
  label: nuclear outer membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/nuclear_outer_membrane.yaml
    role: maintained scientific record
- target_id: GO:0033009
  path: data/structures/membrane_organelle/nucleomorph.yaml
  label: nucleomorph
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/nucleomorph.yaml
    role: maintained scientific record
- target_id: GO:0005634
  path: data/structures/membrane_organelle/nucleus.yaml
  label: nucleus
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/nucleus.yaml
    role: maintained scientific record
- target_id: GO:0070111
  path: data/structures/membrane_organelle/organellar_chromatophore.yaml
  label: organellar chromatophore
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/organellar_chromatophore.yaml
    role: maintained scientific record
scope:
  description: Exact ten-record PR cohort reassessed against current main c32b945b410050078133707a85f58ed8206ec5cc.
    Changed inputs are substantively reassessed. Scientific records remain unchanged.
  selection: Complete cohort of ten maintained records reviewed in original PR head
    1552d23408ac2c2ba304241fdd8b465fb8256820.
  coverage: full
  population_size: 10
  reviewed_target_ids:
  - cellstructuremech:nitroplast
  - GO:0005635
  - GO:0005641
  - GO:0005637
  - GO:0031981
  - cellstructuremech:nuclear_net
  - GO:0005640
  - GO:0033009
  - GO:0005634
  - GO:0070111
checks:
- check_id: qc
  name: Full native QC
  status: passed
  required: true
  target_ids:
  - cellstructuremech:nitroplast
  - GO:0005635
  - GO:0005641
  - GO:0005637
  - GO:0031981
  - cellstructuremech:nuclear_net
  - GO:0005640
  - GO:0033009
  - GO:0005634
  - GO:0070111
  command: just qc
  exit_code: 0
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  scope_note: Actual local execution at main-merge head e2edc3550e41792c2bb6f24eb2918b7d33d8a58c.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-qc
- check_id: labels
  name: Native label correspondence
  status: passed
  required: true
  target_ids:
  - cellstructuremech:nitroplast
  - GO:0005635
  - GO:0005641
  - GO:0005637
  - GO:0031981
  - cellstructuremech:nuclear_net
  - GO:0005640
  - GO:0033009
  - GO:0005634
  - GO:0070111
  command: just validate-products
  exit_code: 0
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  scope_note: Actual local execution at main-merge head e2edc3550e41792c2bb6f24eb2918b7d33d8a58c.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-labels
- check_id: trait-links
  name: TraitMech references
  status: passed
  required: true
  target_ids:
  - cellstructuremech:nitroplast
  - GO:0005635
  - GO:0005641
  - GO:0005637
  - GO:0031981
  - cellstructuremech:nuclear_net
  - GO:0005640
  - GO:0033009
  - GO:0005634
  - GO:0070111
  command: just check-trait-links --check
  exit_code: 0
  summary: Native TraitMech link check passed.
  scope_note: Actual local execution at main-merge head e2edc3550e41792c2bb6f24eb2918b7d33d8a58c.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-trait-links
- check_id: vendored
  name: Pinned governed files
  status: passed
  required: true
  target_ids:
  - cellstructuremech:nitroplast
  - GO:0005635
  - GO:0005641
  - GO:0005637
  - GO:0031981
  - cellstructuremech:nuclear_net
  - GO:0005640
  - GO:0033009
  - GO:0005634
  - GO:0070111
  command: just vendored-check
  exit_code: 0
  summary: Pinned governed files match; native vendored check passed.
  scope_note: Actual local execution at main-merge head e2edc3550e41792c2bb6f24eb2918b7d33d8a58c.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-vendored
- check_id: curies
  name: Native identifier resolver
  status: passed
  required: true
  target_ids:
  - cellstructuremech:nitroplast
  - GO:0005635
  - GO:0005641
  - GO:0005637
  - GO:0031981
  - cellstructuremech:nuclear_net
  - GO:0005640
  - GO:0033009
  - GO:0005634
  - GO:0070111
  command: just check-curies
  exit_code: 0
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  scope_note: Actual local execution at main-merge head e2edc3550e41792c2bb6f24eb2918b7d33d8a58c.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-curies
- check_id: focused-0
  name: validate cellstructuremech:nitroplast
  status: passed
  required: true
  target_ids:
  - cellstructuremech:nitroplast
  command: just validate data/structures/membrane_organelle/nitroplast.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-1
  name: validate-strict cellstructuremech:nitroplast
  status: passed
  required: true
  target_ids:
  - cellstructuremech:nitroplast
  command: just validate-strict data/structures/membrane_organelle/nitroplast.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-2
  name: validate GO:0005635
  status: passed
  required: true
  target_ids:
  - GO:0005635
  command: just validate data/structures/membrane_organelle/nuclear_envelope.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-3
  name: validate-strict GO:0005635
  status: passed
  required: true
  target_ids:
  - GO:0005635
  command: just validate-strict data/structures/membrane_organelle/nuclear_envelope.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-4
  name: validate GO:0005641
  status: passed
  required: true
  target_ids:
  - GO:0005641
  command: just validate data/structures/membrane_organelle/nuclear_envelope_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-5
  name: validate-strict GO:0005641
  status: passed
  required: true
  target_ids:
  - GO:0005641
  command: just validate-strict data/structures/membrane_organelle/nuclear_envelope_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-6
  name: validate GO:0005637
  status: passed
  required: true
  target_ids:
  - GO:0005637
  command: just validate data/structures/membrane_organelle/nuclear_inner_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-7
  name: validate-strict GO:0005637
  status: passed
  required: true
  target_ids:
  - GO:0005637
  command: just validate-strict data/structures/membrane_organelle/nuclear_inner_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-8
  name: validate GO:0031981
  status: passed
  required: true
  target_ids:
  - GO:0031981
  command: just validate data/structures/membrane_organelle/nuclear_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-9
  name: validate-strict GO:0031981
  status: passed
  required: true
  target_ids:
  - GO:0031981
  command: just validate-strict data/structures/membrane_organelle/nuclear_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-10
  name: validate cellstructuremech:nuclear_net
  status: passed
  required: true
  target_ids:
  - cellstructuremech:nuclear_net
  command: just validate data/structures/membrane_organelle/nuclear_net.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-11
  name: validate-strict cellstructuremech:nuclear_net
  status: passed
  required: true
  target_ids:
  - cellstructuremech:nuclear_net
  command: just validate-strict data/structures/membrane_organelle/nuclear_net.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-12
  name: validate GO:0005640
  status: passed
  required: true
  target_ids:
  - GO:0005640
  command: just validate data/structures/membrane_organelle/nuclear_outer_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-13
  name: validate-strict GO:0005640
  status: passed
  required: true
  target_ids:
  - GO:0005640
  command: just validate-strict data/structures/membrane_organelle/nuclear_outer_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-14
  name: validate GO:0033009
  status: passed
  required: true
  target_ids:
  - GO:0033009
  command: just validate data/structures/membrane_organelle/nucleomorph.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-15
  name: validate-strict GO:0033009
  status: passed
  required: true
  target_ids:
  - GO:0033009
  command: just validate-strict data/structures/membrane_organelle/nucleomorph.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-16
  name: validate GO:0005634
  status: passed
  required: true
  target_ids:
  - GO:0005634
  command: just validate data/structures/membrane_organelle/nucleus.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-17
  name: validate-strict GO:0005634
  status: passed
  required: true
  target_ids:
  - GO:0005634
  command: just validate-strict data/structures/membrane_organelle/nucleus.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-18
  name: validate GO:0070111
  status: passed
  required: true
  target_ids:
  - GO:0070111
  command: just validate data/structures/membrane_organelle/organellar_chromatophore.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-19
  name: validate-strict GO:0070111
  status: passed
  required: true
  target_ids:
  - GO:0070111
  command: just validate-strict data/structures/membrane_organelle/organellar_chromatophore.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: supplemental-pmid
  name: Supplemental bounded PMID authority checks
  status: passed
  required: true
  target_ids:
  - cellstructuremech:nitroplast
  - GO:0005635
  - GO:0005641
  - GO:0005637
  - GO:0031981
  - cellstructuremech:nuclear_net
  - GO:0005640
  - GO:0033009
  - GO:0005634
  - GO:0070111
  command: .venv/bin/python /private/tmp/cellstructure-batches-2346-2397-20261103/check_pmid_chunks.py
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372
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
  - cellstructuremech:nitroplast
  - GO:0005635
  - GO:0005641
  - GO:0005637
  - GO:0031981
  - cellstructuremech:nuclear_net
  - GO:0005640
  - GO:0033009
  - GO:0005634
  - GO:0070111
  summary: 'Eight records make positive molecular/pathway claims and require applicability
    assessment: nitroplast, nuclear envelope, nuclear inner membrane, nuclear lumen,
    nuclear outer membrane, nucleomorph, nucleus and organellar chromatophore. Complete
    current official iModulonDB catalogue responses provide no exact applicable eukaryotic
    host/strain or UCYN-A symbiont dataset; unrelated bacterial or Synechococcus datasets
    are not used as proxies. Nuclear envelope lumen and nuclear net retain genuine
    material/topology scope with molecular mechanisms excluded or withheld. Historical00:49Z
    runner unavailability stays historical; current public-source fallback records
    its actual search scope and does not imply biological absence.'
  evidence_ids:
  - septin-catalogue
  - plaque-catalogue
  - micro-catalogue
- check_id: independent-scientific-review
  name: Independent claim-level source review
  status: passed
  required: true
  target_ids:
  - cellstructuremech:nitroplast
  - GO:0005635
  - GO:0005641
  - GO:0005637
  - GO:0031981
  - cellstructuremech:nuclear_net
  - GO:0005640
  - GO:0033009
  - GO:0005634
  - GO:0070111
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
  - septin-SL0351
  - septin-tax373042
  - septin-tax3027
  - septin-tax29197
  - septin-tax55529
  - septin-tax227086
  - septin-tax39717
  - septin-coale2024-meta
  - septin-curtis2012-meta
  - septin-tanifuji2014-meta
  - septin-onuma2017-meta
  - septin-nowack2012-meta
  - septin-singer2017-meta
  - septin-gabr2020-meta
  - septin-li2026-meta
  - septin-nowack2014-crossref
  - septin-coale2024-main-page1
  - septin-coale2024-main-page3
  - septin-coale2024-main-page4
  - septin-coale2024-main-page5
  - septin-coale2024-supp-page2
  - septin-coale2024-supp-page7
  - septin-coale2024-supp-page11
  - septin-hagino2026-body
  - septin-pixels-hagino2026-p1
  - septin-pixels-hagino2026-13
  - septin-pixels-hagino2026-14
  - septin-tanifuji2014-xml
  - septin-onuma2017-xml
  - septin-li2026-xml
  - septin-nowack2012-prefixed
  - septin-structural-other-precedent
  - plaque-policy
  - plaque-rubric
  - plaque-graph-rubric
  - plaque-protein-contract
  - plaque-schema-policy
  - plaque-other-precedent
  - plaque-go
  - plaque-GO0031981-isa
  - plaque-GO0005634-isa
  - plaque-tax271679
  - plaque-tax4932
  - plaque-duan2010-meta
  - plaque-boisvert2007-meta
  - plaque-gavelis2019-meta
  - plaque-kalvelage2023-meta
  - plaque-lu2022-meta
  - plaque-pan2000-meta
  - plaque-aitchison2012-meta
  - plaque-duan2010-bioc
  - plaque-duan2010-numeric
  - plaque-boisvert2007-publisher
  - plaque-gavelis2019-body
  - plaque-gavelis2019-fig3
  - plaque-kalvelage2023-body
  - plaque-pan2000-pmc
  - plaque-aitchison2012-jats
  - plaque-lu2022-pmc
  - plaque-catalogue
  - micro-policy
  - micro-component-policy
  - micro-discussion-policy
  - micro-graph-policy
  - micro-go
  - micro-go-0005635-isa
  - micro-go-0005641-isa
  - micro-go-0005637-isa
  - micro-go-0005640-isa
  - micro-tax2759
  - micro-tax4932
  - micro-tax559292
  - micro-protein-Q02821
  - micro-protein-Q03707
  - micro-protein-Q03281
  - micro-protein-P38881
  - micro-protein-P39968
  - micro-hetzer2010-meta
  - micro-aitchison2012-meta
  - micro-pan2000-meta
  - micro-king2006-meta
  - micro-hetzer2010-pmc
  - micro-aitchison2012-jats
  - micro-pan2000-pmc
  - micro-king2006-supp
  - micro-king2006-browser-opening
  - micro-king2006-browser-body
- check_id: historical-adapter-runner
  name: Retained historical adapter runner availability
  status: unavailable
  required: false
  target_ids:
  - cellstructuremech:nitroplast
  - GO:0005635
  - GO:0005641
  - GO:0005637
  - GO:0031981
  - cellstructuremech:nuclear_net
  - GO:0005640
  - GO:0033009
  - GO:0005634
  - GO:0070111
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
- check_id: nitroplast-uniprot-verify
  name: Native nitroplast UniProt verify check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:nitroplast
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/nitroplast.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples or typed molecular
    nodes. Positive molecular/pathway assertions and genuine physical-scope exclusions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-nitroplast-verify
- check_id: nitroplast-uniprot-causal
  name: Native nitroplast UniProt causal check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:nitroplast
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/nitroplast.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples or typed molecular
    nodes. Positive molecular/pathway assertions and genuine physical-scope exclusions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-nitroplast-causal
- check_id: nuclear_envelope-uniprot-verify
  name: Native nuclear envelope UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0005635
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/nuclear_envelope.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples or typed molecular
    nodes. Positive molecular/pathway assertions and genuine physical-scope exclusions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-nuclear_envelope-verify
- check_id: nuclear_envelope-uniprot-causal
  name: Native nuclear envelope UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0005635
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/nuclear_envelope.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples or typed molecular
    nodes. Positive molecular/pathway assertions and genuine physical-scope exclusions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-nuclear_envelope-causal
- check_id: nuclear_envelope_lumen-uniprot-verify
  name: Native nuclear envelope lumen UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0005641
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/nuclear_envelope_lumen.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples or typed molecular
    nodes. Positive molecular/pathway assertions and genuine physical-scope exclusions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-nuclear_envelope_lumen-verify
- check_id: nuclear_envelope_lumen-uniprot-causal
  name: Native nuclear envelope lumen UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0005641
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/nuclear_envelope_lumen.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples or typed molecular
    nodes. Positive molecular/pathway assertions and genuine physical-scope exclusions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-nuclear_envelope_lumen-causal
- check_id: nuclear_inner_membrane-uniprot-verify
  name: Native nuclear inner membrane UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0005637
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/nuclear_inner_membrane.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples; three UNANCHORED_WITH_UNIPROT
    typed nodes. Native identifier presence is separate from full Kap60/Kap95 system
    identity and source-supported Heh1p/Heh2p targeting.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-nuclear_inner_membrane-verify
- check_id: nuclear_inner_membrane-uniprot-causal
  name: Native nuclear inner membrane UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0005637
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/nuclear_inner_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples; three UNANCHORED_WITH_UNIPROT
    typed nodes. Native identifier presence is separate from full Kap60/Kap95 system
    identity and source-supported Heh1p/Heh2p targeting.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-nuclear_inner_membrane-causal
- check_id: nuclear_lumen-uniprot-verify
  name: Native nuclear lumen UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0031981
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/nuclear_lumen.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples or typed molecular
    nodes. Positive molecular/pathway assertions and genuine physical-scope exclusions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-nuclear_lumen-verify
- check_id: nuclear_lumen-uniprot-causal
  name: Native nuclear lumen UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0031981
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/nuclear_lumen.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples or typed molecular
    nodes. Positive molecular/pathway assertions and genuine physical-scope exclusions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-nuclear_lumen-causal
- check_id: nuclear_net-uniprot-verify
  name: Native nuclear net UniProt verify check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:nuclear_net
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/nuclear_net.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples or typed molecular
    nodes. Positive molecular/pathway assertions and genuine physical-scope exclusions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-nuclear_net-verify
- check_id: nuclear_net-uniprot-causal
  name: Native nuclear net UniProt causal check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:nuclear_net
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/nuclear_net.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples or typed molecular
    nodes. Positive molecular/pathway assertions and genuine physical-scope exclusions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-nuclear_net-causal
- check_id: nuclear_outer_membrane-uniprot-verify
  name: Native nuclear outer membrane UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0005640
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/nuclear_outer_membrane.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples; two UNANCHORED_WITH_UNIPROT
    typed nodes. Native identifier presence is separate from source-specific Nvj1p/Vac8p
    localization, intervention and junction evidence.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-nuclear_outer_membrane-verify
- check_id: nuclear_outer_membrane-uniprot-causal
  name: Native nuclear outer membrane UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0005640
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/nuclear_outer_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples; two UNANCHORED_WITH_UNIPROT
    typed nodes. Native identifier presence is separate from source-specific Nvj1p/Vac8p
    localization, intervention and junction evidence.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-nuclear_outer_membrane-causal
- check_id: nucleomorph-uniprot-verify
  name: Native nucleomorph UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0033009
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/nucleomorph.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples or typed molecular
    nodes. Positive molecular/pathway assertions and genuine physical-scope exclusions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-nucleomorph-verify
- check_id: nucleomorph-uniprot-causal
  name: Native nucleomorph UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0033009
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/nucleomorph.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples or typed molecular
    nodes. Positive molecular/pathway assertions and genuine physical-scope exclusions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-nucleomorph-causal
- check_id: nucleus-uniprot-verify
  name: Native nucleus UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0005634
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/nucleus.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples or typed molecular
    nodes. Positive molecular/pathway assertions and genuine physical-scope exclusions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-nucleus-verify
- check_id: nucleus-uniprot-causal
  name: Native nucleus UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0005634
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/nucleus.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples or typed molecular
    nodes. Positive molecular/pathway assertions and genuine physical-scope exclusions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-nucleus-causal
- check_id: organellar_chromatophore-uniprot-verify
  name: Native organellar chromatophore UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0070111
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/organellar_chromatophore.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples or typed molecular
    nodes. Positive molecular/pathway assertions and genuine physical-scope exclusions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-organellar_chromatophore-verify
- check_id: organellar_chromatophore-uniprot-causal
  name: Native organellar chromatophore UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0070111
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/organellar_chromatophore.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples or typed molecular
    nodes. Positive molecular/pathway assertions and genuine physical-scope exclusions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-organellar_chromatophore-causal
evidence:
- evidence_id: current-record-0
  kind: record_content
  reference: data/structures/membrane_organelle/nitroplast.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T18:12:39Z'
  support: context_only
  summary: Original frozen SHA256 3f7dc36b6c5e8389c881e64839227e1e5cdde49edb55277e245b180f0de8d6a8;
    current SHA256 3f7dc36b6c5e8389c881e64839227e1e5cdde49edb55277e245b180f0de8d6a8.
    Record bytes unchanged since the original review.
  snapshot_sha256: 3f7dc36b6c5e8389c881e64839227e1e5cdde49edb55277e245b180f0de8d6a8
- evidence_id: original-review-0
  kind: prior_review
  reference: reviews/structured/20261022T025104Z-nitroplast-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T18:12:39Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: f034b9ac17575a9ca841adbd8ae13fa6c7c9ddb8087d88f7d298ed9adb00fa3f
- evidence_id: current-record-1
  kind: record_content
  reference: data/structures/membrane_organelle/nuclear_envelope.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T18:12:39Z'
  support: context_only
  summary: Original frozen SHA256 226a12a5500d39f1afbc5baa0f3a81891d6ae4918f4d6c29e8ce05de0df9979a;
    current SHA256 226a12a5500d39f1afbc5baa0f3a81891d6ae4918f4d6c29e8ce05de0df9979a.
    Record bytes unchanged since the original review.
  snapshot_sha256: 226a12a5500d39f1afbc5baa0f3a81891d6ae4918f4d6c29e8ce05de0df9979a
- evidence_id: original-review-1
  kind: prior_review
  reference: reviews/structured/20261022T025105Z-nuclear-envelope-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T18:12:39Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: cd4b3af2f9828842fac4d7513911c27c8e2f027f6e5f1ff86e3f0ce4f7c2cfdc
- evidence_id: current-record-2
  kind: record_content
  reference: data/structures/membrane_organelle/nuclear_envelope_lumen.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T18:12:39Z'
  support: context_only
  summary: Original frozen SHA256 1c45350eaa4a19474f4689125aadc8aa93d1824d41303e3c4aaff1f7e1db6019;
    current SHA256 1c45350eaa4a19474f4689125aadc8aa93d1824d41303e3c4aaff1f7e1db6019.
    Record bytes unchanged since the original review.
  snapshot_sha256: 1c45350eaa4a19474f4689125aadc8aa93d1824d41303e3c4aaff1f7e1db6019
- evidence_id: original-review-2
  kind: prior_review
  reference: reviews/structured/20261022T025106Z-nuclear-envelope-lumen-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T18:12:39Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 9d2d2460b5eff950722b451fa44e83a238438569b3d2bf470cb7a0826f73d41b
- evidence_id: current-record-3
  kind: record_content
  reference: data/structures/membrane_organelle/nuclear_inner_membrane.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T18:12:39Z'
  support: context_only
  summary: Original frozen SHA256 c0484a80c2b1568174ca7f9c96805a6ce2749a3ba27b700e21fb1de2aef4e4df;
    current SHA256 c0484a80c2b1568174ca7f9c96805a6ce2749a3ba27b700e21fb1de2aef4e4df.
    Record bytes unchanged since the original review.
  snapshot_sha256: c0484a80c2b1568174ca7f9c96805a6ce2749a3ba27b700e21fb1de2aef4e4df
- evidence_id: original-review-3
  kind: prior_review
  reference: reviews/structured/20261022T025106Z-nuclear-inner-membrane-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T18:12:39Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 535d5cd2e1edd2fd3ae0a9bad913cd1a02b7aef1c1540d4fd90a5e4aa794e995
- evidence_id: current-record-4
  kind: record_content
  reference: data/structures/membrane_organelle/nuclear_lumen.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T18:12:39Z'
  support: context_only
  summary: Original frozen SHA256 dbb07d267c0272e4deb338a2e8a0e29892a6f1d28f279160c3d42f730410fb49;
    current SHA256 dbb07d267c0272e4deb338a2e8a0e29892a6f1d28f279160c3d42f730410fb49.
    Record bytes unchanged since the original review.
  snapshot_sha256: dbb07d267c0272e4deb338a2e8a0e29892a6f1d28f279160c3d42f730410fb49
- evidence_id: original-review-4
  kind: prior_review
  reference: reviews/structured/20261022T025107Z-nuclear-lumen-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T18:12:39Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 353fc9e94a16c04dee2d5496757cda72a8c963a63a1b1dd0ae7f22cf3aa80b80
- evidence_id: current-record-5
  kind: record_content
  reference: data/structures/membrane_organelle/nuclear_net.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T18:12:39Z'
  support: context_only
  summary: Original frozen SHA256 8b4a54d13a70cfb4fdce9bd18ae990793f9de9627fdca067573c033335d847ba;
    current SHA256 8b4a54d13a70cfb4fdce9bd18ae990793f9de9627fdca067573c033335d847ba.
    Record bytes unchanged since the original review.
  snapshot_sha256: 8b4a54d13a70cfb4fdce9bd18ae990793f9de9627fdca067573c033335d847ba
- evidence_id: original-review-5
  kind: prior_review
  reference: reviews/structured/20261022T025108Z-nuclear-net-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T18:12:39Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 93203662120118e658e0b1c4b153b0b57eabea264ee93c911050f433d0934c7f
- evidence_id: current-record-6
  kind: record_content
  reference: data/structures/membrane_organelle/nuclear_outer_membrane.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T18:12:39Z'
  support: context_only
  summary: Original frozen SHA256 a760b04919cb0a80c89fd2eee5c1d4a0c940fc15a17b77b4b1810b9e1d2b2ffb;
    current SHA256 a760b04919cb0a80c89fd2eee5c1d4a0c940fc15a17b77b4b1810b9e1d2b2ffb.
    Record bytes unchanged since the original review.
  snapshot_sha256: a760b04919cb0a80c89fd2eee5c1d4a0c940fc15a17b77b4b1810b9e1d2b2ffb
- evidence_id: original-review-6
  kind: prior_review
  reference: reviews/structured/20261022T025109Z-nuclear-outer-membrane-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T18:12:39Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: c0ff2eb9462a8d2dd8a32dd25b10ba8e30cb69766b5715134e47d08a626410c5
- evidence_id: current-record-7
  kind: record_content
  reference: data/structures/membrane_organelle/nucleomorph.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T18:12:39Z'
  support: context_only
  summary: Original frozen SHA256 9653087b981991e28b537ec1eb809e442f5215f4ff4c994687106b74ed6338ad;
    current SHA256 9653087b981991e28b537ec1eb809e442f5215f4ff4c994687106b74ed6338ad.
    Record bytes unchanged since the original review.
  snapshot_sha256: 9653087b981991e28b537ec1eb809e442f5215f4ff4c994687106b74ed6338ad
- evidence_id: original-review-7
  kind: prior_review
  reference: reviews/structured/20261022T025109Z-nucleomorph-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T18:12:39Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: c22769a4c692c08d6ebbbe0c6e2ca1fd2831137527e64f953e57b96308ef7b8e
- evidence_id: current-record-8
  kind: record_content
  reference: data/structures/membrane_organelle/nucleus.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T18:12:39Z'
  support: context_only
  summary: Original frozen SHA256 889818b3c6a37074924a97bc81271f43ef236dc9112a871c5e521dae123e497d;
    current SHA256 889818b3c6a37074924a97bc81271f43ef236dc9112a871c5e521dae123e497d.
    Record bytes unchanged since the original review.
  snapshot_sha256: 889818b3c6a37074924a97bc81271f43ef236dc9112a871c5e521dae123e497d
- evidence_id: original-review-8
  kind: prior_review
  reference: reviews/structured/20261022T025110Z-nucleus-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T18:12:39Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: fcb0c90aec7a09925a927546f6692961337c99e8ee195d3fab6912c1b7e6b27c
- evidence_id: current-record-9
  kind: record_content
  reference: data/structures/membrane_organelle/organellar_chromatophore.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T18:12:39Z'
  support: context_only
  summary: Original frozen SHA256 6e9805392c72104f5f1d6e9ee70767c49f480b22130da0e6f293bcf8f6a1bec0;
    current SHA256 b217af7ad434f269a5b8cba2428be5cd988746a75c34a999d7b69909160fcba4.
    Changed record reassessed against current sources.
  snapshot_sha256: b217af7ad434f269a5b8cba2428be5cd988746a75c34a999d7b69909160fcba4
- evidence_id: original-review-9
  kind: prior_review
  reference: reviews/structured/20261022T025111Z-organellar-chromatophore-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T18:12:39Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: b2527e711f4050d12ae0fed598c88bd0f02d93578180ed97bdba96bcf8cd35f7
- evidence_id: septin-review-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Whole-record assertions, structured sources and severity rubric
  summary: Positive molecular/pathway assertions require a real applicability assessment;
    absence of expression claims alone is not an exemption. Keep source scope, uncertainty
    and original finding identity; record curation is separate.
  accessed_at: '2026-11-03T18:11:28.052331Z'
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
  accessed_at: '2026-11-03T18:11:28.052331Z'
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
  accessed_at: '2026-11-03T18:11:28.052331Z'
  support: supports
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: septin-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Graph nodes, component correspondence, source scope and necessity
  summary: Descriptive boundary graphs can remain NONMECHANISTIC; source-specific
    localization, molecular identity and organelle-formation necessity must not be
    conflated.
  accessed_at: '2026-11-03T18:11:28.052331Z'
  support: supports
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: septin-protein-policy
  kind: authority
  reference: .claude/skills/uniprot-protein-examples/SKILL.md
  locator: Step2 generic classes and native coverage report
  summary: Generic class components are explicitly recognized. A zero-example inventory
    or NO_GENE_SYMBOLS node is a stated coverage limit, not proof that the protein
    class does not exist or that its members form one stable complex.
  accessed_at: '2026-11-03T18:11:28.052331Z'
  support: supports
  snapshot_sha256: 6462894c8257823bae2b175c34693cd42f11ff9269a3829c15b9286ba6d7c876
- evidence_id: septin-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0043229,GO:0016020,GO:0016610,GO:0009399,GO:0033009,GO:0043231,GO:0009536,GO:0070111,GO:0070113,GO:0070114,GO:0070115,GO:0070116,GO:0070117,GO:0070118,GO:0015979
  locator: 'All15 exact returned active terms: definitions, synonyms, aspects and
    child relations'
  summary: Exact nucleomorph and chromatophore identities and structural/process parents
    match. GO0070118 defines only a thylakoid bilayer; GO0070116 lists it part_of,
    while GO0070111 lists GO0070116 part_of. GO0016020 describes a collective membrane,
    not a lipid molecule. GO0016610 is nitrogenase complex; its generic definition
    does not measure nitroplast stoichiometry.
  accessed_at: '2026-11-03T18:03:00.499036Z'
  support: supports
  snapshot_sha256: 69cc9be96f00645870402a7e397023de5f7bd02f12312714723a4a830fca3249
- evidence_id: septin-go-search-nitroplast
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=nitroplast&limit=100&page=1
  locator: 'Entire bounded exact-word search response: numberOfHits0'
  summary: The exact-word nitroplast search returned no term; this supports retaining
    the local identity with a broad organelle parent, without claiming exhaustive
    ontology absence.
  accessed_at: '2026-11-03T18:03:00.499315Z'
  support: supports
  snapshot_sha256: f3a7dae9b1e9335291e3940cdf0e5f8dadf9335da7b9547710606b5106c63f86
  search_scope: QuickGO ontology/go/search query=nitroplast, limit100,page1,no date
    filter; actual fetch 2026-11-03T18:03:00.499315Z; entire response numberOfHits0.
    No semantic synonym expansion or exhaustive ontology sweep.
- evidence_id: septin-SL0351
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0351.json
  locator: Complete exact location JSON including nested plastid parent
  summary: Exact whole-chromatophore entry supports photosynthesis, CO2 fixation,
    two surrounding membranes, intervening residual peptidoglycan and contained thylakoids.
    It does not define a separate thylakoid-membrane location or name its molecular
    composition; that narrower identity comes from GO0070118.
  accessed_at: '2026-11-03T18:03:00.499387Z'
  support: supports
  snapshot_sha256: 8a511ebab3aeb225c94971707064b4de8201b1bc8f6672c0e32f550ee72ae5c2
- evidence_id: septin-tax373042
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/373042.json
  locator: Exact current taxonomy identity/rank/lineage fields
  summary: Braarudosphaera bigelowii species matches the record. Taxonomic identity
    does not establish experimental strain, prevalence, a universal phenotype or molecular
    necessity.
  accessed_at: '2026-11-03T18:03:00.499485Z'
  support: supports
  snapshot_sha256: 6cdee90cb62ead292c1778ba3905353639b5217a8528339f2474849eed0c8441
- evidence_id: septin-tax3027
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/3027.json
  locator: Exact current taxonomy identity/rank/lineage fields
  summary: Cryptophyceae class matches the record. Taxonomic identity does not establish
    experimental strain, prevalence, a universal phenotype or molecular necessity.
  accessed_at: '2026-11-03T18:03:00.689453Z'
  support: supports
  snapshot_sha256: 72a0682db96631ffc9f0b222e6bcace19f918d59866e3502ad92a9ba166292f5
- evidence_id: septin-tax29197
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/29197.json
  locator: Exact current taxonomy identity/rank/lineage fields
  summary: Chlorarachniophyceae class matches the record. Taxonomic identity does
    not establish experimental strain, prevalence, a universal phenotype or molecular
    necessity.
  accessed_at: '2026-11-03T18:03:01.221592Z'
  support: supports
  snapshot_sha256: 0947ed25a593cee9efd92ef0f889209a8f51e282940663b4ba775d61f1fe7dcf
- evidence_id: septin-tax55529
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/55529.json
  locator: Exact current taxonomy identity/rank/lineage fields
  summary: Guillardia theta species matches the record. Taxonomic identity does not
    establish experimental strain, prevalence, a universal phenotype or molecular
    necessity.
  accessed_at: '2026-11-03T18:03:01.221661Z'
  support: supports
  snapshot_sha256: 0c0ebfc3e6aeb0b277d2eec1eaa17b7b81ddfb09ba1ee6be5814826d943aad24
- evidence_id: septin-tax227086
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/227086.json
  locator: Exact current taxonomy identity/rank/lineage fields
  summary: Bigelowiella natans species matches the record. Taxonomic identity does
    not establish experimental strain, prevalence, a universal phenotype or molecular
    necessity.
  accessed_at: '2026-11-03T18:03:01.247837Z'
  support: supports
  snapshot_sha256: bf5947b51ae6bd528dd7dc8630de62d8fa712f5dc95489505731dcff7bfd52ec
- evidence_id: septin-tax39717
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/39717.json
  locator: Exact current taxonomy identity/rank/lineage fields
  summary: Paulinella chromatophora species matches the record. Taxonomic identity
    does not establish experimental strain, prevalence, a universal phenotype or molecular
    necessity.
  accessed_at: '2026-11-03T18:03:01.259538Z'
  support: supports
  snapshot_sha256: f3534e3c32299238a36f87d7ba474db869e62a1636bb45879426bb0f4081f420
- evidence_id: septin-coale2024-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1126%2Fscience.adk1075%22&format=json&resultType=core&pageSize=25
  locator: 'Exact DOI search: bibliographic fields and complete abstractText'
  summary: Coale et al.2024, Nitrogen-fixing organelle in a marine alga, DOI10.1126/science.adk1075;
    bibliography and complete abstract match. Actual article/supplement text is separately
    scoped.
  accessed_at: '2026-11-03T18:03:01.433097Z'
  support: supports
  snapshot_sha256: 5c468a9d7c9b2587fc31fc5de3767b54420cd89f11d033784f7ea807fd7434fa
  search_scope: Europe PMC exact DOI query in https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1126%2Fscience.adk1075%22&format=json&resultType=core&pageSize=25;
    resultType=core,pageSize25,no date filter; fetched 2026-11-03T18:03:01.433097Z.
    Only exact DOI result inspected; not exhaustive literature search.
- evidence_id: septin-curtis2012-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fnature11681%22&format=json&resultType=core&pageSize=25
  locator: 'Exact DOI search: bibliographic fields and complete abstractText'
  summary: Curtis et al.2012, Algal genomes reveal evolutionary mosaicism and the
    fate of nucleomorphs, DOI10.1038/nature11681. Complete abstract supports the two
    compared species and retained essential-gene residues; publisher body access failed
    and is not claimed.
  accessed_at: '2026-11-03T18:03:01.803060Z'
  support: supports
  snapshot_sha256: 3b0e5135d07d100dcc31074215572a575c9b054192e69bde7db9a31d5948fb18
  search_scope: Europe PMC exact DOI query in https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fnature11681%22&format=json&resultType=core&pageSize=25;
    resultType=core,pageSize25,no date filter; fetched 2026-11-03T18:03:01.803060Z.
    Only exact DOI result inspected; not exhaustive literature search.
- evidence_id: septin-tanifuji2014-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1186%2F1471-2164-15-374%22&format=json&resultType=core&pageSize=25
  locator: 'Exact DOI search: bibliographic fields and complete abstractText'
  summary: Tanifuji et al.2014 bibliographic identity and complete abstract agree
    with genuine XML body below.
  accessed_at: '2026-11-03T18:03:02.079857Z'
  support: supports
  snapshot_sha256: 208d1a1a246dc75c805ba9d375a9b2cecbc9f24762a016ebd72ec1ff5f7eaaa4
  search_scope: Europe PMC exact DOI query in https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1186%2F1471-2164-15-374%22&format=json&resultType=core&pageSize=25;
    resultType=core,pageSize25,no date filter; fetched 2026-11-03T18:03:02.079857Z.
    Only exact DOI result inspected; not exhaustive literature search.
- evidence_id: septin-onuma2017-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fs41598-017-02668-2%22&format=json&resultType=core&pageSize=25
  locator: 'Exact DOI search: bibliographic fields and complete abstractText'
  summary: Onuma et al.2017 bibliographic identity and complete abstract agree with
    genuine XML body below.
  accessed_at: '2026-11-03T18:03:02.439209Z'
  support: supports
  snapshot_sha256: 61697fdd1dd80c4868ca7ef4d00963abf7ba4f84f3191ef5572b7cff83e4f5f2
  search_scope: Europe PMC exact DOI query in https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fs41598-017-02668-2%22&format=json&resultType=core&pageSize=25;
    resultType=core,pageSize25,no date filter; fetched 2026-11-03T18:03:02.439209Z.
    Only exact DOI result inspected; not exhaustive literature search.
- evidence_id: septin-nowack2012-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1073%2Fpnas.1118800109%22&format=json&resultType=core&pageSize=25
  locator: 'Exact DOI search: bibliographic fields and complete abstractText'
  summary: Nowack and Grossman2012 bibliographic identity and complete abstract agree
    with genuine PMC body below.
  accessed_at: '2026-11-03T18:03:02.474695Z'
  support: supports
  snapshot_sha256: 951c112a9828dbd2f97cd034e856f0cfaf5593109d5f793c785a532001a486d5
  search_scope: Europe PMC exact DOI query in https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1073%2Fpnas.1118800109%22&format=json&resultType=core&pageSize=25;
    resultType=core,pageSize25,no date filter; fetched 2026-11-03T18:03:02.474695Z.
    Only exact DOI result inspected; not exhaustive literature search.
- evidence_id: septin-singer2017-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.cub.2017.08.010%22&format=json&resultType=core&pageSize=25
  locator: 'Exact DOI search: bibliographic fields and complete abstractText'
  summary: Singer et al.2017 complete abstract supports proteomic import and a combined
    experimental/predicted protein catalogue; the conserved long-protein targeting
    signal and two routes are putative. Full body, supplements and individual candidates
    are not independently read.
  accessed_at: '2026-11-03T18:03:02.482492Z'
  support: supports
  snapshot_sha256: 93403db722c9ed34b112a4d95f056fe2373122629e88b720df5dff7f63fa1591
  search_scope: Europe PMC exact DOI query in https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.cub.2017.08.010%22&format=json&resultType=core&pageSize=25;
    resultType=core,pageSize25,no date filter; fetched 2026-11-03T18:03:02.482492Z.
    Only exact DOI result inspected; not exhaustive literature search.
- evidence_id: septin-gabr2020-meta
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1111%2Fjpy.13003%22&format=json&resultType=core&pageSize=25
  locator: 'Exact DOI search: bibliographic fields and complete abstractText'
  summary: Gabr et al.2020 complete secondary abstract supports Paulinella as an organellogenesis
    model and import/metabolic integration context. No full-body or primary-experimental
    certification is claimed.
  accessed_at: '2026-11-03T18:03:02.726782Z'
  support: supports
  snapshot_sha256: c87f440e2e07ee1d17591fe114f793f02bdbaec963b6148d60775f9ecfa34a13
  search_scope: Europe PMC exact DOI query in https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1111%2Fjpy.13003%22&format=json&resultType=core&pageSize=25;
    resultType=core,pageSize25,no date filter; fetched 2026-11-03T18:03:02.726782Z.
    Only exact DOI result inspected; not exhaustive literature search.
- evidence_id: septin-li2026-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.64898%2F2026.04.11.717942%22&format=json&resultType=core&pageSize=25
  locator: 'Exact DOI search: bibliographic fields and complete abstractText'
  summary: Li et al.2026 preprint metadata/abstract matches DOI10.64898/2026.04.11.717942;
    retrieved XML independently identifies version1/preprint status.
  accessed_at: '2026-11-03T18:03:03.087151Z'
  support: supports
  snapshot_sha256: cf0d942c55a84b15e79eea4c5fbc8f143511c9d9ebca3547d4117fa4a9ac7856
  search_scope: Europe PMC exact DOI query in https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.64898%2F2026.04.11.717942%22&format=json&resultType=core&pageSize=25;
    resultType=core,pageSize25,no date filter; fetched 2026-11-03T18:03:03.087151Z.
    Only exact DOI result inspected; not exhaustive literature search.
- evidence_id: septin-nowack2014-crossref
  kind: authority
  reference: https://api.crossref.org/works/10.5586/asbp.2014.049
  locator: Exact DOI metadata and complete deposited secondary abstract
  summary: Nowack2014 review title,author,year and qualitative Paulinella context
    match. Secondary abstract is not a primary experiment or a numerical prevalence
    estimate.
  accessed_at: '2026-11-03T18:03:03.520052Z'
  support: supports
  snapshot_sha256: 7a5635c186a67f8d0f6b1eebbe0d69651d31f4f794592f79583b8106e2e2e16d
- evidence_id: septin-coale2024-main-page1
  kind: primary_source
  reference: https://html.scribdassets.com/5pd08as4w0cdtz4x/pages/1-6ee1ae9510.jsonp
  locator: Article p217, title/abstract and opening architecture/division text; fresh
    public article-page HTML/JSONP text, gzip decoded; not platform-generated prose
  summary: UCYN-A2 association and organelle interpretation; location and coordinated
    division in the studied culture.
  accessed_at: '2026-11-03T18:03:34.315947Z'
  support: supports
  snapshot_sha256: 13aaeaf28b4cc8c137e524e6a5f75339de16f2db242c3e8b75181fc61f63ac0e
- evidence_id: septin-coale2024-main-page3
  kind: primary_source
  reference: https://html.scribdassets.com/5pd08as4w0cdtz4x/pages/3-56a5ec096d.jsonp
  locator: Article p219, import Results and Fig2 caption text; fresh public article-page
    HTML/JSONP text, gzip decoded; not platform-generated prose
  summary: Enrichment-based import evidence is distinguished from detection and prediction;
    NifH enrichment supports nitrogenase membership.
  accessed_at: '2026-11-03T18:03:34.316213Z'
  support: supports
  snapshot_sha256: 5be8adecfe2e9b69c6a233bde074c621e4748bc075df694e43e6eb9a74c808a5
- evidence_id: septin-coale2024-main-page4
  kind: primary_source
  reference: https://html.scribdassets.com/5pd08as4w0cdtz4x/pages/4-3a12e3746a.jsonp
  locator: Article p220, uTP Results and Fig3 caption text; fresh public article-page
    HTML/JSONP text, gzip decoded; not platform-generated prose
  summary: uTP predictions include undetected proteins; missing C-terminal peptides
    permit cleavage or lack of translation. No measured cleavage mechanism is established.
  accessed_at: '2026-11-03T18:03:34.316300Z'
  support: supports
  snapshot_sha256: f0ddd5bd80892e3cfb9455676e5b9b7c7ca83ed9b1798e263fd3c5a8fa613894
- evidence_id: septin-coale2024-main-page5
  kind: primary_source
  reference: https://html.scribdassets.com/5pd08as4w0cdtz4x/pages/5-c1a70e6f2c.jsonp
  locator: Article p221, UCYN-A as nitrogen-fixing organelle conclusion; fresh public
    article-page HTML/JSONP text, gzip decoded; not platform-generated prose
  summary: Authors interpret the combined division/import observations as early organellogenesis;
    this does not equate every UCYN-A lineage with the tested culture.
  accessed_at: '2026-11-03T18:03:34.316361Z'
  support: supports
  snapshot_sha256: 1201951b6ca91e723644783b27d79d6b2cd5d56d9774d3db5f35dfb5a32e5010
- evidence_id: septin-coale2024-supp-page2
  kind: primary_source
  reference: https://html.scribdassets.com/4a1aolh8hsce62xa/pages/2-349cb1d046.jsonp
  locator: Supplement p2, isolation/culture and diel sampling Methods; fresh public
    article-page HTML/JSONP text, gzip decoded; not platform-generated prose
  summary: FR-21=NIES4399; proteomics used N-deplete culture and SXT N-replete culture.
    FR-12 is a separate isolate.
  accessed_at: '2026-11-03T18:03:34.316404Z'
  support: supports
  snapshot_sha256: f374344d9a46cc2b263d4500baac89a72a34ef5a1274875111c96a699786f57d
- evidence_id: septin-coale2024-supp-page7
  kind: primary_source
  reference: https://html.scribdassets.com/4a1aolh8hsce62xa/pages/7-952a50e37b.jsonp
  locator: Supplement p7, nitrogen fixation rates Methods; fresh public article-page
    HTML/JSONP text, gzip decoded; not platform-generated prose
  summary: Triplicate cultures and daytime acetylene-reduction measurements support
    nitrogenase activity, without an organelle-assembly knockout.
  accessed_at: '2026-11-03T18:03:34.571235Z'
  support: supports
  snapshot_sha256: 7869472ee2ac9289480b322b3a265e6a9363e7c7986694ed69b26fff15d523fe
- evidence_id: septin-coale2024-supp-page11
  kind: primary_source
  reference: https://html.scribdassets.com/4a1aolh8hsce62xa/pages/11-ca621b2751.jsonp
  locator: Supplement p11, FigS3 caption text only; fresh public article-page HTML/JSONP
    text, gzip decoded; not platform-generated prose
  summary: Caption reports growth, nitrogenase activity and photosynthetic efficiency;
    image pixels and quantitative plotted values were not inspected.
  accessed_at: '2026-11-03T18:03:34.580795Z'
  support: supports
  snapshot_sha256: 9dc4929fd5dde857496109a7d6595f0db51f38fc17acd35726147d57706ef344
- evidence_id: septin-hagino2026-body
  kind: primary_source
  reference: https://wakemanlaboratory.com/wp-content/uploads/2026/07/taxonomic-re-evaluation-of-the-braarudosphaera-bigelowii-species-complex-prymnesiophyceae-_compressed.pdf
  locator: 'Genuine PDF: article first page copyright (PDF2), TEM Methods (PDF6/printed5),
    cytology Results (PDF9/printed8), Table2/discussion (PDF13/printed12), Fig28–31
    caption and pixels (PDF14/printed13), taxonomy/culture-loss discussion (PDF17/printed16)'
  summary: FR12/FR21 are genotypeIII B.bigelowii sensu stricto; FR21=NIES4399. Table2
    separates nitroplast-bearing cultures from KC1-P2 loss. Fig28/29 show FR21 Nit
    bodies with 1um bars; Fig30/31 are OTR22-B. Copyright is International Phycological
    Society; link-only OTHER does not assert a redistribution licence. Culture loss
    does not establish wild prevalence or its cause.
  accessed_at: '2026-11-03T18:03:03.429111Z'
  support: supports
  snapshot_sha256: 8ba2e99a97d10cf23220f0d80dcc3ed3aac1ee1e6b22260036c7cea4544813ac
- evidence_id: septin-pixels-hagino2026-p1
  kind: primary_source
  reference: https://wakemanlaboratory.com/wp-content/uploads/2026/07/taxonomic-re-evaluation-of-the-braarudosphaera-bigelowii-species-complex-prymnesiophyceae-_compressed.pdf
  locator: Publisher cover/title pixels; locally rendered derivative /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/adversary-septin/hagino2026-p1.png
  summary: Actual view_image inspection; panels/strains/scale are evaluated with the
    parent PDF caption and copyright. No image edit or repository image write.
  accessed_at: '2026-11-03T18:11:28.052331Z'
  support: supports
  snapshot_sha256: 401d4c1e06e3a6696df95c3e67ade34805c23055aea1e423e6a93e24c0a16066
- evidence_id: septin-pixels-hagino2026-13
  kind: primary_source
  reference: https://wakemanlaboratory.com/wp-content/uploads/2026/07/taxonomic-re-evaluation-of-the-braarudosphaera-bigelowii-species-complex-prymnesiophyceae-_compressed.pdf
  locator: PDF13 Table2 and taxonomy discussion pixels; locally rendered derivative
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/adversary-septin/hagino2026-13.png
  summary: Actual view_image inspection; panels/strains/scale are evaluated with the
    parent PDF caption and copyright. No image edit or repository image write.
  accessed_at: '2026-11-03T18:11:28.052331Z'
  support: supports
  snapshot_sha256: 065a83260a895c5316730bfe0369815357bae3bc2dfa9ffead5d74a2fd8e915b
- evidence_id: septin-pixels-hagino2026-14
  kind: primary_source
  reference: https://wakemanlaboratory.com/wp-content/uploads/2026/07/taxonomic-re-evaluation-of-the-braarudosphaera-bigelowii-species-complex-prymnesiophyceae-_compressed.pdf
  locator: PDF14 Fig28–31 full-page pixels; locally rendered derivative /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/adversary-septin/hagino2026-14.png
  summary: Actual view_image inspection; panels/strains/scale are evaluated with the
    parent PDF caption and copyright. No image edit or repository image write.
  accessed_at: '2026-11-03T18:11:28.052331Z'
  support: supports
  snapshot_sha256: 0f79de476f63caf6040a7930b6cbf500b090576dcdf0c331a1f2750f9732b9e0
- evidence_id: septin-tanifuji2014-xml
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4035089/fullTextXML
  locator: 'Genuine Europe PMC XML: Background; first Results subsection on L.oceanica
    genome; Fig1 caption; Methods culturing, sequencing and assembly (derived section
    indices0,2,10–12)'
  summary: L.oceanica CCMP622 has three linear nucleomorph chromosomes. Repetitive
    chromosomeI leaves exact size uncertain; assembly and PCR support the chromosome
    description. Background separates red/green origins. Genome sequencing is not
    individual-gene deletion or formation-necessity evidence; no figure pixels inspected.
  accessed_at: '2026-11-03T18:07:28.605593Z'
  support: supports
  snapshot_sha256: 4d81845786049d3a003bb6574f7f3e5db3f10df6c0edc72448819b22a3397184
- evidence_id: septin-onuma2017-xml
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5443833/fullTextXML
  locator: 'Genuine Europe PMC XML: H2A localization and replication Results, Fig2–4
    captions, replication Discussion, culture/IF/EdU Methods (derived indices3,4,7,12,14,17)'
  summary: G.theta CCMP2712 was synchronized under8h light/16h dark; only about30%
    divided. H2A localization and timed EdU pulses support a cell-cycle-linked replication
    example with later/longer nucleomorph synthesis. Not every cell or lineage was
    experimentally shown to replicate identically; no figure pixels inspected.
  accessed_at: '2026-11-03T18:07:28.605879Z'
  support: supports
  snapshot_sha256: 31745abad3bebcc8eb9b18b48b72f18593a6b97848ea039c5ff734a863220621
- evidence_id: septin-li2026-xml
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13104995/fullTextXML
  locator: Genuine Europe PMC XML front version/status and Discussion hybrid envelope,
    diel remodeling, and Limitations (derived indices9–11)
  summary: Version1 remains a preprint. Static ultrastructure does not identify vesicle
    cargo/direction, exchanged substrates or a transport mechanism; the record correctly
    leaves these unresolved. No new constituent or causal edge is inferred from unidentified
    densities; pixels were not inspected.
  accessed_at: '2026-11-03T18:07:28.606138Z'
  support: supports
  snapshot_sha256: 518acd79f6062d84eb4367d33fb8f37dd8e8a30e825adbec458d265d1c5ccf8f
- evidence_id: septin-nowack2012-prefixed
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3325729/
  locator: 'Genuine PMC body: Results PsaE localization, PSI purification, translational-inhibitor
    labelling and Golgi observation; Fig1–4 captions; Discussion import/trafficking/targeting;
    Methods strain, antibodies, EM, PSI isolation/protein identification and radiolabelling'
  summary: In P.chromatophora CCAC0185, localization, purified PSI and inhibitor-labelling
    support host synthesis/import and PSI association of PsaE/PsaK. Golgi routing
    is suggested, not mechanistically proven. This is the primary basis for the light-complex
    claim, separate from GO compartment definition. Captions, not microscopy pixels
    or supplements, were read.
  accessed_at: '2026-11-03T18:08:44.263032Z'
  support: supports
  snapshot_sha256: 3c62e25e8dde341faf854bc462eb3e03a4cf927ce0761d0888bde710bcf07bfb
- evidence_id: septin-catalogue
  kind: search
  reference: https://imodulondb.org/api/datasets
  locator: Complete current official organism/dataset catalogue
  summary: No matched Braarudosphaera/UCYN-A/Atelocyanobacterium, cryptophyte/chlorarachniophyte/Guillardia/Bigelowiella/Lotharella
    or Paulinella dataset is present. Synechococcus elongatus is not a matched host/strain
    proxy. Molecular claims trigger assessment, but downstream queries are not applicable
    without a matching dataset. No biological absence is inferred.
  accessed_at: '2026-11-03T18:03:00.499439Z'
  support: supports
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  search_scope: GET https://imodulondb.org/api/datasets at 2026-11-03T18:03:00.499439Z;
    complete20organism rows/28organism-dataset pairs/22distinct dataset strings, no
    filter or truncation. Inspected names,ids,descriptions and keys against the named
    hosts/endosymbionts; no sequence-derived host substitution.
- evidence_id: septin-adapter-runner-historical
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical attempted runner, not a fresh invocation
  summary: Actual2026-11-03T00:49:00.848907Z–00:49:00.863225Z ended exit1 PermissionError
    reading pyvenv.cfg. Historical availability is distinct from fresh official catalogue
    and primary-source fallback.
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: supports
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: septin-context-diazoplast
  kind: record_content
  reference: data/structures/membrane_organelle/diazoplast.yaml
  locator: Frozen identity,definition,hierarchy and boundary evidence only
  summary: 'Boundary context read after freezing: distinct diazoplast and general
    plastid identities. Neighbor molecular findings and historical dispositions are
    not independently assessed or resolved.'
  accessed_at: '2026-11-03T18:11:28.052331Z'
  support: supports
  snapshot_sha256: fd3948e827eb4a9870bc4eccb09689dd5c82f5caef443f1e319daabbf21bb038
- evidence_id: septin-context-plastid
  kind: record_content
  reference: data/structures/membrane_organelle/plastid.yaml
  locator: Frozen identity,definition,hierarchy and boundary evidence only
  summary: 'Boundary context read after freezing: distinct diazoplast and general
    plastid identities. Neighbor molecular findings and historical dispositions are
    not independently assessed or resolved.'
  accessed_at: '2026-11-03T18:11:28.052331Z'
  support: supports
  snapshot_sha256: 1be30ab06bc2fbae9294930ceaf74b20a2d43d8af60986aa9ed0e07b9645ae81
- evidence_id: septin-structural-other-precedent
  kind: authority
  reference: tests/test_trypanosome_structure_evidence.py
  locator: test_faz1_rnai_does_not_establish_null_assembly_essentiality, structural
    OTHER assertion only
  summary: Frozen native test recognizes OTHER for a structural constituent. Together
    with native schema this supports nitroplast collective membrane OTHER; no unrelated
    FAZ science is reviewed or transferred.
  accessed_at: '2026-11-03T18:11:28.052331Z'
  support: supports
  snapshot_sha256: 7ce1dfa869f9295e836fff7a7956e62685ac291969283c5311e08c7fad5cf79b
- evidence_id: septin-retrieval-source-receipts
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/adversary-septin/source-receipts.json
  locator: Actual saved request outcomes, times and SHA256
  summary: HTTP200 challenge bodies are not paper bodies. Fresh alternate genuine
    XML/PMC/article-page requests are separately identified; failed requests are retained.
    No old source body timestamp is represented as a fresh fetch.
  accessed_at: '2026-11-03T18:11:28.052331Z'
  support: supports
  snapshot_sha256: 32928d72f3b8d9538247ab546ecd7fbb6b228cabf9317629aebd13e2729dc740
- evidence_id: septin-retrieval-additional-source-receipts
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/adversary-septin/additional-source-receipts.json
  locator: Actual saved request outcomes, times and SHA256
  summary: HTTP200 challenge bodies are not paper bodies. Fresh alternate genuine
    XML/PMC/article-page requests are separately identified; failed requests are retained.
    No old source body timestamp is represented as a fresh fetch.
  accessed_at: '2026-11-03T18:11:28.052331Z'
  support: supports
  snapshot_sha256: 1e86f4d0dbe247f127e79edafc6e1fbe9e3e75998ffdf977291519632d20565f
- evidence_id: septin-retrieval-recovery-source-receipts
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/adversary-septin/recovery-source-receipts.json
  locator: Actual saved request outcomes, times and SHA256
  summary: HTTP200 challenge bodies are not paper bodies. Fresh alternate genuine
    XML/PMC/article-page requests are separately identified; failed requests are retained.
    No old source body timestamp is represented as a fresh fetch.
  accessed_at: '2026-11-03T18:11:28.052331Z'
  support: supports
  snapshot_sha256: 917ee8c8b9783a466042e8a3e10a9b2a67b432da6696be4d6afe780500ae85ed
- evidence_id: septin-retrieval-final-source-receipts
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/adversary-septin/final-source-receipts.json
  locator: Actual saved request outcomes, times and SHA256
  summary: HTTP200 challenge bodies are not paper bodies. Fresh alternate genuine
    XML/PMC/article-page requests are separately identified; failed requests are retained.
    No old source body timestamp is represented as a fresh fetch.
  accessed_at: '2026-11-03T18:11:28.052331Z'
  support: supports
  snapshot_sha256: 689212a07e05ea11a2188eed0d1382735c28eaf6f1728495ccfd18e51f19bf54
- evidence_id: septin-record-nitroplast
  kind: record_content
  reference: data/structures/membrane_organelle/nitroplast.yaml
  locator: Complete current record at e2edc3550e41792c2bb6f24eb2918b7d33d8a58c
  summary: All identity,history,synonym,hierarchy,component,scope,canonical,evidence,discussion
    and graph/image fields read. Current content independently reassessed; historical
    review verdict is not automatically carried forward.
  accessed_at: '2026-11-03T18:11:28.052331Z'
  support: supports
  snapshot_sha256: 3f7dc36b6c5e8389c881e64839227e1e5cdde49edb55277e245b180f0de8d6a8
- evidence_id: septin-original-nitroplast
  kind: prior_review
  reference: reviews/structured/20261022T025104Z-nitroplast-audit/review.yaml
  locator: Complete immutable original YAML/Markdown, scientific claims/findings/actions/checks/limits
  summary: Original native validate/render succeeds with exact Markdown. Original
    target hash verified at its frozen source; target remains byte-identical.
  accessed_at: '2026-11-03T18:11:28.052331Z'
  support: supports
  snapshot_sha256: f034b9ac17575a9ca841adbd8ae13fa6c7c9ddb8087d88f7d298ed9adb00fa3f
- evidence_id: septin-original-validation-nitroplast
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/adversary-septin/original-checks.json
  locator: Actual native original schema/render and historical target hash check
  summary: Both commands exit0, Markdown exact. Frozen and current target hashes remain
    distinct for the stale chromatophore.
  accessed_at: '2026-11-03T18:03:30.006697Z'
  support: supports
  snapshot_sha256: 92053a0fa6251abfa1cc02f992bd206606a4f0b8bc9c9f61be5a4a0054cf2fc3
- evidence_id: septin-native-nitroplast-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nitroplast-uniprot-verify-receipt.json
  locator: Actual receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nitroplast-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: Exit0. Independent whole-record inventory confirms zero protein examples,
    zero GENE_OR_PROTEIN nodes and no UniProtKB graph xrefs. Exit0 validates only
    that empty represented identifier scope; it does not certify complete molecular
    composition or biological claims.
  accessed_at: '2026-11-03T18:02:09.274576Z'
  support: supports
  snapshot_sha256: 6cf137fff4f150aeeeedf1a954a7e634ea397730a20e940a6f1732c17db6403a
- evidence_id: septin-native-nitroplast-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nitroplast-uniprot-causal-receipt.json
  locator: Actual receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nitroplast-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: Exit0. Independent whole-record inventory confirms zero protein examples,
    zero GENE_OR_PROTEIN nodes and no UniProtKB graph xrefs. Exit0 validates only
    that empty represented identifier scope; it does not certify complete molecular
    composition or biological claims.
  accessed_at: '2026-11-03T18:02:09.641705Z'
  support: supports
  snapshot_sha256: 29c32facaa8fd294fcb98793603611af9c110743bdd2feee5058f4a15ba78bcb
- evidence_id: septin-record-nucleomorph
  kind: record_content
  reference: data/structures/membrane_organelle/nucleomorph.yaml
  locator: Complete current record at e2edc3550e41792c2bb6f24eb2918b7d33d8a58c
  summary: All identity,history,synonym,hierarchy,component,scope,canonical,evidence,discussion
    and graph/image fields read. Current content independently reassessed; historical
    review verdict is not automatically carried forward.
  accessed_at: '2026-11-03T18:11:28.052331Z'
  support: supports
  snapshot_sha256: 9653087b981991e28b537ec1eb809e442f5215f4ff4c994687106b74ed6338ad
- evidence_id: septin-original-nucleomorph
  kind: prior_review
  reference: reviews/structured/20261022T025109Z-nucleomorph-audit/review.yaml
  locator: Complete immutable original YAML/Markdown, scientific claims/findings/actions/checks/limits
  summary: Original native validate/render succeeds with exact Markdown. Original
    target hash verified at its frozen source; target remains byte-identical.
  accessed_at: '2026-11-03T18:11:28.052331Z'
  support: supports
  snapshot_sha256: c22769a4c692c08d6ebbbe0c6e2ca1fd2831137527e64f953e57b96308ef7b8e
- evidence_id: septin-original-validation-nucleomorph
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/adversary-septin/original-checks.json
  locator: Actual native original schema/render and historical target hash check
  summary: Both commands exit0, Markdown exact. Frozen and current target hashes remain
    distinct for the stale chromatophore.
  accessed_at: '2026-11-03T18:03:31.120022Z'
  support: supports
  snapshot_sha256: 92053a0fa6251abfa1cc02f992bd206606a4f0b8bc9c9f61be5a4a0054cf2fc3
- evidence_id: septin-native-nucleomorph-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nucleomorph-uniprot-verify-receipt.json
  locator: Actual receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nucleomorph-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: Exit0. Independent whole-record inventory confirms zero protein examples,
    zero GENE_OR_PROTEIN nodes and no UniProtKB graph xrefs. Exit0 validates only
    that empty represented identifier scope; it does not certify complete molecular
    composition or biological claims.
  accessed_at: '2026-11-03T18:02:16.440480Z'
  support: supports
  snapshot_sha256: 4475c0720589be44eb9d3b2413fff4905ee550a5ba8b07cf4d3bac739ca66bb4
- evidence_id: septin-native-nucleomorph-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nucleomorph-uniprot-causal-receipt.json
  locator: Actual receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nucleomorph-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: Exit0. Independent whole-record inventory confirms zero protein examples,
    zero GENE_OR_PROTEIN nodes and no UniProtKB graph xrefs. Exit0 validates only
    that empty represented identifier scope; it does not certify complete molecular
    composition or biological claims.
  accessed_at: '2026-11-03T18:02:16.860011Z'
  support: supports
  snapshot_sha256: 87da53473c7ddf0b83990f06fc890d9b853bb161b4bcdd4249c868af0b419e63
- evidence_id: septin-record-organellar_chromatophore
  kind: record_content
  reference: data/structures/membrane_organelle/organellar_chromatophore.yaml
  locator: Complete current record at e2edc3550e41792c2bb6f24eb2918b7d33d8a58c
  summary: All identity,history,synonym,hierarchy,component,scope,canonical,evidence,discussion
    and graph/image fields read. Current content independently reassessed; historical
    review verdict is not automatically carried forward.
  accessed_at: '2026-11-03T18:11:28.052331Z'
  support: supports
  snapshot_sha256: b217af7ad434f269a5b8cba2428be5cd988746a75c34a999d7b69909160fcba4
- evidence_id: septin-original-organellar_chromatophore
  kind: prior_review
  reference: reviews/structured/20261022T025111Z-organellar-chromatophore-audit/review.yaml
  locator: Complete immutable original YAML/Markdown, scientific claims/findings/actions/checks/limits
  summary: Original native validate/render succeeds with exact Markdown. Original
    target hash verified at its frozen source; current target changed and is substantively
    reassessed.
  accessed_at: '2026-11-03T18:11:28.052331Z'
  support: supports
  snapshot_sha256: b2527e711f4050d12ae0fed598c88bd0f02d93578180ed97bdba96bcf8cd35f7
- evidence_id: septin-original-validation-organellar_chromatophore
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/adversary-septin/original-checks.json
  locator: Actual native original schema/render and historical target hash check
  summary: Both commands exit0, Markdown exact. Frozen and current target hashes remain
    distinct for the stale chromatophore.
  accessed_at: '2026-11-03T18:03:32.248091Z'
  support: supports
  snapshot_sha256: 92053a0fa6251abfa1cc02f992bd206606a4f0b8bc9c9f61be5a4a0054cf2fc3
- evidence_id: septin-native-organellar_chromatophore-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/organellar_chromatophore-uniprot-verify-receipt.json
  locator: Actual receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/organellar_chromatophore-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: Exit0. Independent whole-record inventory confirms zero protein examples,
    zero GENE_OR_PROTEIN nodes and no UniProtKB graph xrefs. Exit0 validates only
    that empty represented identifier scope; it does not certify complete molecular
    composition or biological claims.
  accessed_at: '2026-11-03T18:02:18.112553Z'
  support: supports
  snapshot_sha256: 1df98b47737783e9b4fe7aa99d171c391a60c7cba46c169e275da092ebd0d73a
- evidence_id: septin-native-organellar_chromatophore-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/organellar_chromatophore-uniprot-causal-receipt.json
  locator: Actual receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/organellar_chromatophore-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: Exit0. Independent whole-record inventory confirms zero protein examples,
    zero GENE_OR_PROTEIN nodes and no UniProtKB graph xrefs. Exit0 validates only
    that empty represented identifier scope; it does not certify complete molecular
    composition or biological claims.
  accessed_at: '2026-11-03T18:02:18.516408Z'
  support: supports
  snapshot_sha256: d9954c8efba3b5fdd1518904ae5b9dfe001e4a64953a55207078ac77b4174d4d
- evidence_id: plaque-current-4
  kind: record_content
  reference: data/structures/membrane_organelle/nuclear_lumen.yaml
  locator: Entire current maintained record at e2edc3550e41792c2bb6f24eb2918b7d33d8a58c,
    including all components, graphs, discussions, history and image metadata
  summary: Independently read current target; unchanged from original frozen target.
  accessed_at: '2026-11-03T18:07:05.066737Z'
  support: supports
  snapshot_sha256: dbb07d267c0272e4deb338a2e8a0e29892a6f1d28f279160c3d42f730410fb49
- evidence_id: plaque-original-4
  kind: prior_review
  reference: reviews/structured/20261022T025107Z-nuclear-lumen-audit/review.yaml
  locator: Exact staleness-selected YAML plus native-rendered Markdown; source/check/assessment/finding/action
    fields
  summary: Original native validation/rendering and every historical frozen input
    verified. Qualified pass with no scientific finding/action.
  accessed_at: '2026-11-03T18:07:05.066737Z'
  support: supports
  snapshot_sha256: 353fc9e94a16c04dee2d5496757cda72a8c963a63a1b1dd0ae7f22cf3aa80b80
- evidence_id: plaque-current-5
  kind: record_content
  reference: data/structures/membrane_organelle/nuclear_net.yaml
  locator: Entire current maintained record at e2edc3550e41792c2bb6f24eb2918b7d33d8a58c,
    including all components, graphs, discussions, history and image metadata
  summary: Independently read current target; unchanged from original frozen target.
  accessed_at: '2026-11-03T18:07:05.066737Z'
  support: supports
  snapshot_sha256: 8b4a54d13a70cfb4fdce9bd18ae990793f9de9627fdca067573c033335d847ba
- evidence_id: plaque-original-5
  kind: prior_review
  reference: reviews/structured/20261022T025108Z-nuclear-net-audit/review.yaml
  locator: Exact staleness-selected YAML plus native-rendered Markdown; source/check/assessment/finding/action
    fields
  summary: Original native validation/rendering and every historical frozen input
    verified. Qualified pass with no scientific finding/action.
  accessed_at: '2026-11-03T18:07:05.066737Z'
  support: supports
  snapshot_sha256: 93203662120118e658e0b1c4b153b0b57eabea264ee93c911050f433d0934c7f
- evidence_id: plaque-current-8
  kind: record_content
  reference: data/structures/membrane_organelle/nucleus.yaml
  locator: Entire current maintained record at e2edc3550e41792c2bb6f24eb2918b7d33d8a58c,
    including all components, graphs, discussions, history and image metadata
  summary: Independently read current target; unchanged from original frozen target.
  accessed_at: '2026-11-03T18:07:05.066737Z'
  support: supports
  snapshot_sha256: 889818b3c6a37074924a97bc81271f43ef236dc9112a871c5e521dae123e497d
- evidence_id: plaque-original-8
  kind: prior_review
  reference: reviews/structured/20261022T025110Z-nucleus-audit/review.yaml
  locator: Exact staleness-selected YAML plus native-rendered Markdown; source/check/assessment/finding/action
    fields
  summary: Original native validation/rendering and every historical frozen input
    verified. One inherited minor author-attribution finding retained.
  accessed_at: '2026-11-03T18:07:05.066737Z'
  support: supports
  snapshot_sha256: fcb0c90aec7a09925a927546f6692961337c99e8ee195d3fab6912c1b7e6b27c
- evidence_id: plaque-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Previously read frozen native policy bytes unchanged; current source/enum
    contract used
  summary: Native applicability includes named proteins, pathways, stress and traits;
    expression-module absence alone does not justify exclusion. Actual morphology/material-only
    scope can be genuinely excluded.
  accessed_at: '2026-11-03T18:07:05.066737Z'
  support: context_only
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: plaque-rubric
  kind: authority
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Previously read frozen native policy bytes unchanged; current source/enum
    contract used
  summary: Exact identity, source support, taxonomy, mechanism and necessity assessed
    separately. Optional inventory slots and uninspected-source absence are not automatic
    defects.
  accessed_at: '2026-11-03T18:07:05.066737Z'
  support: context_only
  snapshot_sha256: e6b9e4b16a58c54402bed7bbee2c8b94a91d37562e8b0ee8b94ff0c829184a70
- evidence_id: plaque-graph-rubric
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Previously read frozen native policy bytes unchanged; current source/enum
    contract used
  summary: Descriptive topology and localization are distinct from mechanistic proof
    or necessity.
  accessed_at: '2026-11-03T18:07:05.066737Z'
  support: context_only
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: plaque-protein-contract
  kind: authority
  reference: .claude/skills/uniprot-protein-examples/SKILL.md
  locator: Previously read frozen native policy bytes unchanged; current source/enum
    contract used
  summary: Native empty accession/node coverage is not evidence for every narrative
    molecular or pathway assertion.
  accessed_at: '2026-11-03T18:07:05.066737Z'
  support: context_only
  snapshot_sha256: 6462894c8257823bae2b175c34693cd42f11ff9269a3829c15b9286ba6d7c876
- evidence_id: plaque-schema-policy
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Previously read frozen native policy bytes unchanged; current source/enum
    contract used
  summary: OTHER is explicitly permitted; class prose emphasizing molecular building
    blocks does not alone establish a confirmed type defect for a correctly identified
    structural constituent. Complexes/families are permitted GENE_OR_PROTEIN nodes.
  accessed_at: '2026-11-03T18:07:05.066737Z'
  support: context_only
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: plaque-other-precedent
  kind: authority
  reference: tests/test_trypanosome_structure_evidence.py
  locator: Freshly inspected test_faz1_rnai_does_not_establish_null_assembly_essentiality;
    exact OTHER structural-constituent assertion around line76
  summary: Frozen before inspection. Maintained regression explicitly accepts structural
    FAZ filament as OTHER. This is bounded native modeling precedent, not biological
    evidence for nuclear structures or permission to retype a lipid incorrectly.
  accessed_at: '2026-11-03T18:07:05.066737Z'
  support: context_only
  snapshot_sha256: 7ce1dfa869f9295e836fff7a7956e62685ac291969283c5311e08c7fad5cf79b
- evidence_id: plaque-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031981,GO:0070013,GO:0005634,GO:0005637,GO:0000228,GO:0005730,GO:0005635,GO:0005643,GO:0006913,GO:0043231,GO:0005622,GO:0016020,GO:0044195,GO:0005654
  locator: Complete exact14-term response; definitions, synonyms, comments and typed
    children
  summary: Exact nucleus/lumen/pore/inner membrane/chromosome/nucleolus identities
    and direct typed topology agree. Nucleoplasm is a nuclear-lumen part with definition
    excluding chromosomes/nucleolus, not an asserted exact synonym. GO0044195 includes
    lamina-associated channels and does not by itself exactly map the Polykrikos net;
    GO0005622 is a conservative broader parent.
  accessed_at: '2026-11-03T18:03:01.541851Z'
  support: supports
  snapshot_sha256: 13b54763ed18f847b3ba28726a402adf0bbcb05dd986695f67ac64820907075a
- evidence_id: plaque-GO0031981-isa
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031981/ancestors?relations=is_a
  locator: Complete exact current is_a ancestor response and typed children
  summary: Nuclear lumen has intracellular organelle lumen ancestor0070013 and direct
    part_of chromosome/nucleolus/nucleoplasm children. Contains-part assertions are
    not inferred from untyped mixed ancestors.
  accessed_at: '2026-11-03T18:03:01.542058Z'
  support: supports
  snapshot_sha256: ef6fbbf5c3207e09ce7a113d1e60f557339cf92f7fd2c3f43f4c9b6b9525c909
- evidence_id: plaque-GO0005634-isa
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005634/ancestors?relations=is_a
  locator: Complete exact current is_a ancestor response and typed children
  summary: Nucleus has intracellular membrane-bounded organelle ancestor0043231, exact
    cell-nucleus synonym and envelope/lumen part_of children. Native definition preserves
    specialized RNA-metabolism/DNA-replication exceptions.
  accessed_at: '2026-11-03T18:03:01.542118Z'
  support: supports
  snapshot_sha256: b91ce8b43246ceaa126f60dd5edb560810685ac917f2f27b9b8cd7bf34e91091
- evidence_id: plaque-tax271679
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/271679
  locator: Complete current ENA identity, rank, lineage and aliases
  summary: 271679 resolves to Polykrikos kofoidii species. Wild-collected pseudocolonies
    are not a named culture strain or species-wide prevalence sample.
  accessed_at: '2026-11-03T18:03:01.542181Z'
  support: supports
  snapshot_sha256: 69cb7b45b417f8736d4242226f0b0b8b82fe08c8e4a9e82c667d7a8fa0b26f98
- evidence_id: plaque-tax4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete current ENA identity, rank, lineage and aliases
  summary: 4932 resolves to Saccharomyces cerevisiae species; BY4741-derived Duan
    and YEF473/L40 Pan preparations are kept distinct.
  accessed_at: '2026-11-03T18:03:01.542230Z'
  support: supports
  snapshot_sha256: 38f43dd1593a1d47416228ae385464f30aeb8302c3aadb45b3588d03744bc814
- evidence_id: plaque-net-go-search
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=nuclear%20net&limit=100&page=1
  locator: QuickGO nuclear net query first100 returned terms; all returned names inspected,
    with exact candidate definitions checked in the separate14-term response
  summary: Returned589 total hits; this bounded first page has no exact nuclear-net
    identity. Nucleoplasmic reticulum is a nearby candidate with extra lamina/function
    scope, not automatic equivalence. The record historical589-result survey is not
    represented as a newly exhaustive search.
  accessed_at: '2026-11-03T18:03:47.363225Z'
  support: supports
  search_scope: QuickGO ontology/go/search query=nuclear net, limit100,page1 at 2026-11-03T18:03:47.363225Z;100
    returned results of589,total6pages. Remaining pages not inspected; no ontology-wide
    absence proof.
  snapshot_sha256: 2a1b33564e4955a6c1e4197039a10f3a38c8aa62a136b313617e71f1139cf824
- evidence_id: plaque-duan2010-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038/nature08973&format=json&resultType=core&pageSize=25
  locator: Exact DOI bibliographic identity and complete native abstract
  summary: Verified title, authors, DOI, publication year and returned source identifier.
    Primary/secondary distinctions are retained; abstract does not certify unread
    body or pixels.
  accessed_at: '2026-11-03T18:03:01.542553Z'
  support: supports
  search_scope: EuropePMC exact DOI query https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038/nature08973&format=json&resultType=core&pageSize=25;
    bounded pageSize from URL at 2026-11-03T18:03:01.542553Z; 1 returned metadata
    record inspected; no open-ended search or automatic full-text claim.
  snapshot_sha256: 4911a80cb6c504b39d4fcdadfd5ede15af377addd35579125a2bff45f889b25e
- evidence_id: plaque-boisvert2007-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038/nrm2184&format=json&resultType=core&pageSize=25
  locator: Exact DOI bibliographic identity and complete native abstract
  summary: Verified title, authors, DOI, publication year and returned source identifier.
    Primary/secondary distinctions are retained; abstract does not certify unread
    body or pixels.
  accessed_at: '2026-11-03T18:03:01.545274Z'
  support: supports
  search_scope: EuropePMC exact DOI query https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038/nrm2184&format=json&resultType=core&pageSize=25;
    bounded pageSize from URL at 2026-11-03T18:03:01.545274Z; 1 returned metadata
    record inspected; no open-ended search or automatic full-text claim.
  snapshot_sha256: e87af8e93e8a304b3feb50a0c03d019688ef500c557ad4b43bfcbada7935b2f2
- evidence_id: plaque-gavelis2019-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038/s41598-018-37065-w&format=json&resultType=core&pageSize=25
  locator: Exact DOI bibliographic identity and complete native abstract
  summary: Verified title, authors, DOI, publication year and returned source identifier.
    Primary/secondary distinctions are retained; abstract does not certify unread
    body or pixels.
  accessed_at: '2026-11-03T18:03:01.547222Z'
  support: supports
  search_scope: EuropePMC exact DOI query https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038/s41598-018-37065-w&format=json&resultType=core&pageSize=25;
    bounded pageSize from URL at 2026-11-03T18:03:01.547222Z; 1 returned metadata
    record inspected; no open-ended search or automatic full-text claim.
  snapshot_sha256: 9444234e8a0c5c4a0a2a99618d13b91eabab826993b8d64eca87e95b6c4c764f
- evidence_id: plaque-kalvelage2023-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128/msphere.00038-23&format=json&resultType=core&pageSize=25
  locator: Exact DOI bibliographic identity and complete native abstract
  summary: Verified title, authors, DOI, publication year and returned source identifier.
    Primary/secondary distinctions are retained; abstract does not certify unread
    body or pixels.
  accessed_at: '2026-11-03T18:03:02.140818Z'
  support: supports
  search_scope: EuropePMC exact DOI query https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128/msphere.00038-23&format=json&resultType=core&pageSize=25;
    bounded pageSize from URL at 2026-11-03T18:03:02.140818Z; 1 returned metadata
    record inspected; no open-ended search or automatic full-text claim.
  snapshot_sha256: 540a14612f6b95e1b8cc8bfc12fbbc9d32c5072bb2b2bdec18374becc6cd3cb7
- evidence_id: plaque-lu2022-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1080/21541248.2021.1993714&format=json&resultType=core&pageSize=25
  locator: Exact DOI bibliographic identity and complete native abstract
  summary: Verified title, authors, DOI, publication year and returned source identifier.
    Primary/secondary distinctions are retained; abstract does not certify unread
    body or pixels.
  accessed_at: '2026-11-03T18:03:02.178265Z'
  support: supports
  search_scope: EuropePMC exact DOI query https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1080/21541248.2021.1993714&format=json&resultType=core&pageSize=25;
    bounded pageSize from URL at 2026-11-03T18:03:02.178265Z; 1 returned metadata
    record inspected; no open-ended search or automatic full-text claim.
  snapshot_sha256: ed8c33e1575579a18ce6120626a062cccb9288cbd6511a30fe04b53d91e08ee0
- evidence_id: plaque-pan2000-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1091/mbc.11.7.2445%22&format=json&resultType=core&pageSize=20
  locator: Exact DOI bibliographic identity and complete native abstract
  summary: Verified title, authors, DOI, publication year and returned source identifier.
    Primary/secondary distinctions are retained; abstract does not certify unread
    body or pixels.
  accessed_at: '2026-11-03T18:02:39.496221Z'
  support: supports
  search_scope: EuropePMC exact DOI query https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1091/mbc.11.7.2445%22&format=json&resultType=core&pageSize=20;
    bounded pageSize from URL at 2026-11-03T18:02:39.496221Z; 1 returned metadata
    record inspected; no open-ended search or automatic full-text claim.
  snapshot_sha256: f58ac090f70c0a13d7468f4406d98509469dc283ca3579d405f7ff65b1d11d15
- evidence_id: plaque-aitchison2012-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1534/genetics.111.127803%22&format=json&resultType=core&pageSize=20
  locator: Exact DOI bibliographic identity and complete native abstract
  summary: Verified title, authors, DOI, publication year and returned source identifier.
    Primary/secondary distinctions are retained; abstract does not certify unread
    body or pixels.
  accessed_at: '2026-11-03T18:02:39.306618Z'
  support: supports
  search_scope: EuropePMC exact DOI query https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1534/genetics.111.127803%22&format=json&resultType=core&pageSize=20;
    bounded pageSize from URL at 2026-11-03T18:02:39.306618Z; 1 returned metadata
    record inspected; no open-ended search or automatic full-text claim.
  snapshot_sha256: e1b5996512104993b29a34d16c788770f778a17b3e241d73d42de9b1685b14bf
- evidence_id: plaque-duan2010-bioc
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_xml/PMC2874121/unicode
  locator: Genuine NCBI BioC text; passages2,6,12,13,14,16, independently read in
    full; title/DOI matched genuine numeric PMC HTML
  summary: BY4741 bar1-derived haploid yeast formaldehyde crosslinking and genome-wide
    conformation capture support a population-based three-dimensional genome model.
    Model combines contact probabilities and known spatial landmarks; authors explicitly
    limit it as coarse-grained and population-based, not every-cell chromosome topology
    or all-eukaryote architecture.
  accessed_at: '2026-11-03T18:03:47.361670Z'
  support: supports
  snapshot_sha256: 336168383f8b18bc0ef54f599543c0dfa6889bf6f8ef5ab9fdb1a6d24149063e
- evidence_id: plaque-duan2010-numeric
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/2874121/
  locator: Genuine PMC2874121 numeric HTML; title/DOI, complete Methods Summary S1
    and Figure5 caption; no figure pixels/supplementary datasets
  summary: Independent matching body verifies the BY4741-derived preparation, FDR
    strategy and modeled nuclear chromosome/nucleolus arrangement. Original canonical
    route returned a recaptcha challenge and was not article evidence.
  accessed_at: '2026-11-03T18:03:47.361437Z'
  support: supports
  snapshot_sha256: 7816acb5600678d70d8aefc29e8d57b24d02592e79c1c0751d0ce076f6a7a567
- evidence_id: plaque-boisvert2007-publisher
  kind: authority
  reference: https://www.nature.com/articles/nrm2184
  locator: Publisher landing page SECONDARY REVIEW; title/authors, complete Key Points
    and Abstract only. Paywall offer and article metadata distinguished from unavailable
    full main text.
  summary: Supports nucleolus ribosomal DNA transcription, pre-rRNA processing and
    ribosomal subunit assembly. This is a secondary synthesis, not a newly inspected
    primary perturbation or full article body. Additional stress/cell-cycle topics
    on the page are not imported into the maintained lumen record.
  accessed_at: '2026-11-03T18:03:02.670839Z'
  support: supports
  snapshot_sha256: d4b232e7c86888224f6fcbeb924348acdef740e44aa52bd895a929759d898d11
- evidence_id: plaque-gavelis2019-body
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC6351617.1/PMC6351617.1.xml
  locator: Genuine PMC6351617.1 JATS; entire Sec1 Introduction, Sec2 Results and Figure1–5
    captions, Sec3 Discussion, Sec4 Conclusion, Sec5 Methods including Sec6–9; article
    authors, permissions and Fig3 graphic metadata
  summary: 'Wild-collected Polykrikos pseudocolonies: one high-pressure-frozen/freeze-substituted
    FIB-SEM cell, four chemically fixed TEM cells and eight confocal specimens. Results
    explicitly describe double-membrane strands continuous with tunnels/envelope and
    periodic swellings; chemical fixation disrupts fine network. Super-resolution
    confirmation of centrin overlap, dynamic division and flow remain open. Only Fig3
    pixels inspected; supplementary double-membrane image not independently inspected,
    so no new bilayer measurement claimed.'
  accessed_at: '2026-11-03T18:03:02.184548Z'
  support: supports
  snapshot_sha256: e9da1c1df53b0558143b645859b9cf77aa266778027d41a42b10d78502bad9f4
- evidence_id: plaque-gavelis2019-fig3
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC6351617.1/41598_2018_37065_Fig3_HTML.jpg
  locator: Fresh complete figure binary, SHA256 compared byte-for-byte with frozen
    local image; all maintained panels A–G visually inspected through local view_image
  summary: Image matches maintained file exactly. Grayscale sections with nodes/arrows
    and rendered red strands/tunnels1–6 agree with caption. Six is the depicted specimen
    count. Rendering does not demonstrate molecular composition, flow or causal division.
    JATS grants CC BY4.0 including images absent separate restrictive credit; Fig3
    has no such credit.
  accessed_at: '2026-11-03T18:03:02.195865Z'
  support: supports
  snapshot_sha256: 9f2cd13af66cdb9f0321d5a23b6381a3cf3fd7d087be5e87b68c1176619db3de
- evidence_id: plaque-stored-image
  kind: record_content
  reference: data/images/membrane_organelle/nuclear_net/pmc6351617_fig3.jpg
  locator: All pixels inspected with view_image; separate scratch image-inspection.json
    records observation and time
  summary: All panels A-G visually inspected using view_image. A-C grayscale section
    insets show round/elongated light profiles and red arrowheads; C has5um scale.
    D-F show red segmented reticulating strands and tubes superimposed on section/green-blue
    surrounding anatomy; D has15um scale. G shows red connecting strands/swellings
    with six labelled tubes1-6. Image supports depicted segmentation/anatomy only;
    no molecular label, flow, causal mechanism, double-bilayer measurement or universal
    tunnel count inferred.
  accessed_at: '2026-11-03T18:03:18.343369Z'
  support: supports
  snapshot_sha256: 9f2cd13af66cdb9f0321d5a23b6381a3cf3fd7d087be5e87b68c1176619db3de
- evidence_id: plaque-kalvelage2023-body
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC10449503.1/PMC10449503.1.xml
  locator: Genuine PMC10449503.1 JATS; matching title/DOI, complete Conclusion s2-4
    only; complete native abstract separately inspected. Remaining Results/Methods/supplements/pixels
    not read.
  summary: Prorocentrum cordatum CCMP1329 study explicitly leaves nuclear-net investigation
    and dynamics for future work. It is not an independent full reconstruction of
    the Polykrikos-type network, and its broad proteomics does not identify nuclear-net
    constituents here.
  accessed_at: '2026-11-03T18:03:02.225688Z'
  support: supports
  snapshot_sha256: 173c89087072dc5f4e250f725ac09023d6fab5289bf13d2bb5bb5e08b4e0c6ef
- evidence_id: plaque-pan2000-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC14931/
  locator: Same-PR fresh shared genuine PMC14931 HTML; independently reread Methods
    sec3, Results sec11/sec13/sec15 with included captions, Discussion sec19. No figure
    pixels, remaining Results or supplements. Original fetch timestamp preserved.
  summary: YEF473/L40 yeast two-hybrid, cell-extract copurification and imaging support
    Vac8p–Nvj1p association at nucleus–vacuole junctions. Source infers direct interaction
    while explicitly acknowledging a remote indirect possibility; not purified binary
    reconstitution. Current canonical contact example is supported without extrapolating
    to whole-nucleus formation necessity or quantified species prevalence.
  accessed_at: '2026-11-03T18:04:17.870110Z'
  support: supports
  snapshot_sha256: 8bd997f8509fdbd22d9aa789a327bf45569958c821f8f9b26176a0f9d6acdc38
- evidence_id: plaque-aitchison2012-jats
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3296253.1/PMC3296253.1.xml
  locator: Same-PR fresh shared genuine PMC3296253.1 JATS SECONDARY review; independently
    read opening body paragraph, s2 Overall Composition, s3 Membrane Ring and first3
    direct paragraphs of s14 Mechanism of Nuclear Transport; no pixels or cited-primary
    rereview
  summary: Supports NPC protein-complex identity and envelope openings/gated transport
    at the stated descriptive level. Selectivity and transport energy differ; virtual
    gating is not a literal opening/shutting gate or energy-free whole transport.
    Detailed Nup mechanisms and assembly necessities remain outside this record review.
  accessed_at: '2026-11-03T18:04:17.869977Z'
  support: supports
  snapshot_sha256: 86f99d67fca3b4ce43a29b17335d4b8ba0b21653ccf508d16ee01163a2be6422
- evidence_id: plaque-lu2022-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC9707532/
  locator: Genuine PMC9707532 HTML title/DOI/citation_author metadata; full Results
    s0002-s2002 including Fig2 caption and Discussion s0003 including Fig5 caption.
    No other Results, movies, supplements or pixels inspected.
  summary: Article explicitly names Michelle S Lu and David G Drubin, not Luo et al.2022.2021
    online date and2022 volume year are distinguished. Cell-cycle-dependent Cdc42/Nvj1
    fluorescence association supports bounded observations and proposed additional
    functions, not proven novel nuclear pathways. Maintained error is bibliographic
    attribution only.
  accessed_at: '2026-11-03T18:03:47.361735Z'
  support: supports
  snapshot_sha256: aacbde1464e7da6f8f9ae09c550f12f4594ba2cd1414062a1e5d9d24a12fa976
- evidence_id: plaque-catalogue
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Complete fresh official /api/datasets response; every returned organism/dataset
    pair inspected
  summary: No Saccharomyces, Polykrikos or other represented eukaryotic host. Positive
    lumen ribosome-biogenesis and nucleus transport/protein claims trigger applicability
    followed by bounded noncoverage; no downstream matched-gene/module query applies.
    Nuclear net exclusion rests on actual morphology-only claims, not catalogue absence.
  accessed_at: '2026-11-03T18:03:02.684210Z'
  support: supports
  search_scope: Official iModulonDB complete datasets response at 2026-11-03T18:03:02.684210Z;
    all returned host/dataset pairs inspected for exact target-host coverage. No foreign-strain
    proxy, generated module prose or negative biology.
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: plaque-historical-runner
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical00:49Z unavailable runner and retained stdout/stderr hashes
  summary: Historical PermissionError reading pyvenv.cfg is not a fresh invocation
    or success. Current catalogue and source fallback are separately documented.
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: plaque-original-checks
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/adversary-plaque/original-checks.json
  locator: Three original native validate/render executions plus historical/current
    hash checks
  summary: Original pairs validate and render exactly;13/14/12 frozen historical inputs
    match retained source and all three target hashes remain unchanged.
  accessed_at: '2026-11-03T18:02:51.580959Z'
  support: supports
  snapshot_sha256: 17ce4d711e733ad36e567738b4dd0e148da82b0c939a7e6e3a9b7b97d38aa679
- evidence_id: plaque-native-nuclear_lumen-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/nuclear_lumen.yaml
    --verify
  locator: Actual root receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nuclear_lumen-uniprot-verify-receipt.json;
    stdoutSHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: Actual inventory has zero protein_examples and zero GENE_OR_PROTEIN nodes.
    Native pass is empty represented accession/typed-node coverage, not proof of narrative
    molecular identity, pathway support or necessity.
  accessed_at: '2026-11-03T18:02:13.185445Z'
  support: supports
  snapshot_sha256: 8eb81b15255c083c558d8e403e966573ec1b1ec7fd9d0d7170cbfac96caae44a
- evidence_id: plaque-native-nuclear_lumen-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/nuclear_lumen.yaml
    --causal-graphs
  locator: Actual root receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nuclear_lumen-uniprot-causal-receipt.json;
    stdoutSHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: Actual inventory has zero protein_examples and zero GENE_OR_PROTEIN nodes.
    Native pass is empty represented accession/typed-node coverage, not proof of narrative
    molecular identity, pathway support or necessity.
  accessed_at: '2026-11-03T18:02:13.611032Z'
  support: supports
  snapshot_sha256: 862401cc72ace5244c4a2f5602ce50cabda084e4fd5024078b1d6434d37768c2
- evidence_id: plaque-native-nuclear_net-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/nuclear_net.yaml
    --verify
  locator: Actual root receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nuclear_net-uniprot-verify-receipt.json;
    stdoutSHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: Actual inventory has zero protein_examples and zero GENE_OR_PROTEIN nodes.
    Native pass is empty represented accession/typed-node coverage, not proof of narrative
    molecular identity, pathway support or necessity.
  accessed_at: '2026-11-03T18:02:14.024786Z'
  support: supports
  snapshot_sha256: 07d899ee2053fffa458a1343def9078b9b7c9b856c018a2ad9d5cc06a04fc92d
- evidence_id: plaque-native-nuclear_net-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/nuclear_net.yaml
    --causal-graphs
  locator: Actual root receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nuclear_net-uniprot-causal-receipt.json;
    stdoutSHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: Actual inventory has zero protein_examples and zero GENE_OR_PROTEIN nodes.
    Native pass is empty represented accession/typed-node coverage, not proof of narrative
    molecular identity, pathway support or necessity.
  accessed_at: '2026-11-03T18:02:14.453348Z'
  support: supports
  snapshot_sha256: 371bc0f7a64a4b00a93fd33e47d0b29dd483f4684b40ac7f0b3a3039235eed4d
- evidence_id: plaque-native-nucleus-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/nucleus.yaml
    --verify
  locator: Actual root receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nucleus-uniprot-verify-receipt.json;
    stdoutSHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: Actual inventory has zero protein_examples and zero GENE_OR_PROTEIN nodes.
    Native pass is empty represented accession/typed-node coverage, not proof of narrative
    molecular identity, pathway support or necessity.
  accessed_at: '2026-11-03T18:02:17.281826Z'
  support: supports
  snapshot_sha256: ee8e7504b7b9fd8e7b1cf1696a6ac8160c9439b5c7b5cbd3741c87eb3a0ae4d2
- evidence_id: plaque-native-nucleus-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/nucleus.yaml
    --causal-graphs
  locator: Actual root receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nucleus-uniprot-causal-receipt.json;
    stdoutSHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: Actual inventory has zero protein_examples and zero GENE_OR_PROTEIN nodes.
    Native pass is empty represented accession/typed-node coverage, not proof of narrative
    molecular identity, pathway support or necessity.
  accessed_at: '2026-11-03T18:02:17.701727Z'
  support: supports
  snapshot_sha256: 9c1682167a6d52d565fbb49a5b30fc326283bc9ab7dff58d6be2d1e5c8022962
- evidence_id: micro-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Native skill, profile/config/output contract and checklist; structured-source
    section
  accessed_at: '2026-11-03T18:09:45.511264Z'
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
  summary: Actual protein/pathway assertions trigger host coverage assessment, independent
    of whether expression data are asserted. No automatic query obligation for physical
    topology with molecular assertions explicitly withheld.
  support: context_only
- evidence_id: micro-component-policy
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent391-445, CausalNode and ComponentTypeEnum; native family/instance
    guidance
  accessed_at: '2026-11-03T18:09:45.511264Z'
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
  summary: Molecular LIPID grounding differs from complete cellular-component membrane
    identity. Collective label-only material is permitted; source-neutral family/complex
    grounding differs from organism-specific xrefs. Essentiality concerns structure
    formation. Complexes are permitted under GENE_OR_PROTEIN; no enum-only defect.
  support: context_only
- evidence_id: micro-discussion-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Complete Discussions section305-324 and molecular-family/instance guidance
  accessed_at: '2026-11-03T18:09:45.511264Z'
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
  summary: 'A discussion is provenance rather than a task description: prompt may
    be narrowed, rationale appended to and never replaced, notes hold current state,
    posed_date preserved. Historical rationale is not automatically a current erroneous
    scientific assertion.'
  support: context_only
- evidence_id: micro-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Graph scope/edge evidence contract; frozen UniProt skill and verifier coverage
  accessed_at: '2026-11-03T18:09:45.511264Z'
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
  summary: Coarse NONMECHANISTIC topology/transport edges retain source scope. UniProt
    xrefs on unanchored nodes are allowed; a representative accession does not identify
    all members of a grouped actor.
  support: context_only
- evidence_id: micro-record-nuclear_envelope
  kind: record_content
  reference: data/structures/membrane_organelle/nuclear_envelope.yaml
  locator: Entire maintained record, including history, all evidence/functions/components/graph
    edges/discussions
  accessed_at: '2026-11-03T18:09:45.511264Z'
  snapshot_sha256: 226a12a5500d39f1afbc5baa0f3a81891d6ae4918f4d6c29e8ce05de0df9979a
  summary: Current target matches original frozen input exactly and was independently
    reassessed; no stale input in this slice.
  support: supports
- evidence_id: micro-prior-nuclear_envelope
  kind: prior_review
  reference: reviews/structured/20261022T025105Z-nuclear-envelope-audit/review.yaml
  locator: Complete native original envelope/checks/evidence/assessments/findings/actions/limitations
    and exact rendered Markdown
  accessed_at: '2026-11-03T18:09:45.511264Z'
  snapshot_sha256: cd4b3af2f9828842fac4d7513911c27c8e2f027f6e5f1ff86e3f0ce4f7c2cfdc
  summary: Historical verdict needs_curation; 1 original findings; explicit expression-only
    applicability exclusion, not an omitted row. Historical commands/access remain
    historical.
  support: context_only
- evidence_id: micro-native-nuclear_envelope-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nuclear_envelope-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/nuclear_envelope.yaml
    --verify; full log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nuclear_envelope-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T18:02:10.015822Z'
  snapshot_sha256: d8fcc0c354797853692ff297c13fc8cb8b2d70587516027de6c20a7a100da32e
  summary: Exit0 at exact source. Zero examples and zero GENE_OR_PROTEIN nodes; NPC
    GO complex independently checked. Empty verifier pass is not molecular completeness.
  support: supports
- evidence_id: micro-native-nuclear_envelope-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nuclear_envelope-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/nuclear_envelope.yaml
    --causal-graphs; full log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nuclear_envelope-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-03T18:02:10.389405Z'
  snapshot_sha256: 5249330c5d9d5e40a99f81309dfff474442bb766bca124940b13c50682994183
  summary: Exit0 at exact source. Zero examples and zero GENE_OR_PROTEIN nodes; NPC
    GO complex independently checked. Empty verifier pass is not molecular completeness.
  support: supports
- evidence_id: micro-record-nuclear_envelope_lumen
  kind: record_content
  reference: data/structures/membrane_organelle/nuclear_envelope_lumen.yaml
  locator: Entire maintained record, including history, all evidence/functions/components/graph
    edges/discussions
  accessed_at: '2026-11-03T18:09:45.511264Z'
  snapshot_sha256: 1c45350eaa4a19474f4689125aadc8aa93d1824d41303e3c4aaff1f7e1db6019
  summary: Current target matches original frozen input exactly and was independently
    reassessed; no stale input in this slice.
  support: supports
- evidence_id: micro-prior-nuclear_envelope_lumen
  kind: prior_review
  reference: reviews/structured/20261022T025106Z-nuclear-envelope-lumen-audit/review.yaml
  locator: Complete native original envelope/checks/evidence/assessments/findings/actions/limitations
    and exact rendered Markdown
  accessed_at: '2026-11-03T18:09:45.511264Z'
  snapshot_sha256: 9d2d2460b5eff950722b451fa44e83a238438569b3d2bf470cb7a0826f73d41b
  summary: Historical verdict pass_with_limitations; 0 original findings; explicit
    expression-only applicability exclusion, not an omitted row. Historical commands/access
    remain historical.
  support: context_only
- evidence_id: micro-native-nuclear_envelope_lumen-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nuclear_envelope_lumen-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/nuclear_envelope_lumen.yaml
    --verify; full log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nuclear_envelope_lumen-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T18:02:10.759393Z'
  snapshot_sha256: 71bf015ce89f6bb896d47a445fe27c08c3b7cbe6a829056c8a69d24de84c9d91
  summary: Exit0 at exact source. Zero examples and zero GENE_OR_PROTEIN nodes; this
    lumen asserts physical boundaries without resident proteins or transport machinery.
  support: supports
- evidence_id: micro-native-nuclear_envelope_lumen-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nuclear_envelope_lumen-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/nuclear_envelope_lumen.yaml
    --causal-graphs; full log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nuclear_envelope_lumen-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-03T18:02:11.126955Z'
  snapshot_sha256: 7a8843a9a0b3ab71c16bf2f6c8b5ce201dca4d6ea720a09463f7763002652c3b
  summary: Exit0 at exact source. Zero examples and zero GENE_OR_PROTEIN nodes; this
    lumen asserts physical boundaries without resident proteins or transport machinery.
  support: supports
- evidence_id: micro-record-nuclear_inner_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/nuclear_inner_membrane.yaml
  locator: Entire maintained record, including history, all evidence/functions/components/graph
    edges/discussions
  accessed_at: '2026-11-03T18:09:45.511264Z'
  snapshot_sha256: c0484a80c2b1568174ca7f9c96805a6ce2749a3ba27b700e21fb1de2aef4e4df
  summary: Current target matches original frozen input exactly and was independently
    reassessed; no stale input in this slice.
  support: supports
- evidence_id: micro-prior-nuclear_inner_membrane
  kind: prior_review
  reference: reviews/structured/20261022T025106Z-nuclear-inner-membrane-audit/review.yaml
  locator: Complete native original envelope/checks/evidence/assessments/findings/actions/limitations
    and exact rendered Markdown
  accessed_at: '2026-11-03T18:09:45.511264Z'
  snapshot_sha256: 535d5cd2e1edd2fd3ae0a9bad913cd1a02b7aef1c1540d4fd90a5e4aa794e995
  summary: Historical verdict needs_curation; 1 original findings; explicit expression-only
    applicability exclusion, not an omitted row. Historical commands/access remain
    historical.
  support: context_only
- evidence_id: micro-native-nuclear_inner_membrane-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nuclear_inner_membrane-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/nuclear_inner_membrane.yaml
    --verify; full log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nuclear_inner_membrane-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T18:02:12.313712Z'
  snapshot_sha256: 253253f882c6eaa7e6acfea319322cab6305096e02947103e3de5d4e4792d27b
  summary: Exit0 at exact source. Zero examples, three UNANCHORED_WITH_UNIPROT nodes
    with Q02821/Q03707/Q03281. Q02821 verifies only Kap60 within the named Kap60/Kap95
    system, not complete pair coverage.
  support: supports
- evidence_id: micro-native-nuclear_inner_membrane-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nuclear_inner_membrane-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/nuclear_inner_membrane.yaml
    --causal-graphs; full log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nuclear_inner_membrane-uniprot-causal.log
    SHA256 fb6b9ed140965b1c16457568c6a3389352df6b75ca5bc065608ed07296439c87
  accessed_at: '2026-11-03T18:02:12.753484Z'
  snapshot_sha256: 59d0154454cd9a159d378319a13610a5a16821c6b13f314cf7700b872546dcf0
  summary: Exit0 at exact source. Zero examples, three UNANCHORED_WITH_UNIPROT nodes
    with Q02821/Q03707/Q03281. Q02821 verifies only Kap60 within the named Kap60/Kap95
    system, not complete pair coverage.
  support: supports
- evidence_id: micro-record-nuclear_outer_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/nuclear_outer_membrane.yaml
  locator: Entire maintained record, including history, all evidence/functions/components/graph
    edges/discussions
  accessed_at: '2026-11-03T18:09:45.511264Z'
  snapshot_sha256: a760b04919cb0a80c89fd2eee5c1d4a0c940fc15a17b77b4b1810b9e1d2b2ffb
  summary: Current target matches original frozen input exactly and was independently
    reassessed; no stale input in this slice.
  support: supports
- evidence_id: micro-prior-nuclear_outer_membrane
  kind: prior_review
  reference: reviews/structured/20261022T025109Z-nuclear-outer-membrane-audit/review.yaml
  locator: Complete native original envelope/checks/evidence/assessments/findings/actions/limitations
    and exact rendered Markdown
  accessed_at: '2026-11-03T18:09:45.511264Z'
  snapshot_sha256: c0ff2eb9462a8d2dd8a32dd25b10ba8e30cb69766b5715134e47d08a626410c5
  summary: Historical verdict needs_curation; 1 original findings; explicit expression-only
    applicability exclusion, not an omitted row. Historical commands/access remain
    historical.
  support: context_only
- evidence_id: micro-native-nuclear_outer_membrane-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nuclear_outer_membrane-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/nuclear_outer_membrane.yaml
    --verify; full log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nuclear_outer_membrane-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T18:02:15.560548Z'
  snapshot_sha256: 96a81320230b75f6170a85f12222f0a6885b412c42a360b4583c0794c4438f32
  summary: Exit0 at exact source. Zero examples, two UNANCHORED_WITH_UNIPROT nodes
    with P38881/P39968; permissible node xrefs independently checked, not source-neutral
    family grounding.
  support: supports
- evidence_id: micro-native-nuclear_outer_membrane-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nuclear_outer_membrane-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/nuclear_outer_membrane.yaml
    --causal-graphs; full log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/nuclear_outer_membrane-uniprot-causal.log
    SHA256 20ca030cdfeb1a45fdd86dc1db1c8361c2cd5f5569a0fd1e3468470442253e23
  accessed_at: '2026-11-03T18:02:15.999638Z'
  snapshot_sha256: ac9596f706c73bd9274bfb61e590a86c12bc1ae3c974892f9625b5f180f1a2b3
  summary: Exit0 at exact source. Zero examples, two UNANCHORED_WITH_UNIPROT nodes
    with P38881/P39968; permissible node xrefs independently checked, not source-neutral
    family grounding.
  support: supports
- evidence_id: micro-original-pairs
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/adversary-microtubule/original-checks.json
  locator: Four actual native validates and four render --content calls; exact Markdown
    comparisons
  accessed_at: '2026-11-03T18:06:45.706566Z'
  snapshot_sha256: 643cdee4f3bf12b0ed5a31989573703f9f7111dd9387b2eab3246f0f6bab43f1
  summary: All four original pairs validate and render exactly.
  support: supports
- evidence_id: micro-original-inputs
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/adversary-microtubule/original-frozen-inputs.json
  locator: All68 original frozen input entries at their retained original source revisions
  accessed_at: '2026-11-03T18:09:45.511264Z'
  snapshot_sha256: 7c3e7ee0b90c9e260baf23e83cd3c11ec9dd4cb9c412c68c48df5e6240d3b2f2
  summary: All original hashes verify and four current targets are unchanged. Historical
    input hashing is provenance validation, not new scientific judgment of unfrozen
    context.
  support: supports
- evidence_id: micro-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005635,GO:0031967,GO:0005634,GO:0005637,GO:0005640,GO:0005641,GO:0005643,GO:0006913,GO:0006998,GO:0031970,GO:0005788,GO:0031090,GO:0005774
  locator: 'Complete13 exact active terms: identities, definitions, synonyms and typed
    child relations'
  accessed_at: '2026-11-03T18:02:36.236201Z'
  snapshot_sha256: 18627a592c0f8bace3b7cf3d8847639aae864fec38a5ee52dbf84c4746d35298
  summary: Exact envelope5635, lumen5641, inner5637, outer5640 and pore5643 definitions
    distinguish whole structure, boundary bilayers, enclosed volume and protein complex.
    Envelope definition itself supplies20–40nm/lamina wording; it is not an independent
    experiment or universal taxon-specific measurement. NPC definition supports legitimate
    PROTEIN_COMPLEX grounding.
  support: supports
- evidence_id: micro-go-0005635-isa
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005635/ancestors?relations=is_a
  locator: Complete relations=is_a ancestor response; no immediate-parent inference
    from transitive list
  accessed_at: '2026-11-03T18:02:36.236491Z'
  snapshot_sha256: 1057aa263feafde1564e5982e181e8dc1fb6e477c3f11cdf52f9f68a374d00dd
  summary: Exact is_a ancestry supports organelle envelope0031967. Typed child relations
    and source topology separately support parthood.
  support: supports
- evidence_id: micro-go-0005641-isa
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005641/ancestors?relations=is_a
  locator: Complete relations=is_a ancestor response; no immediate-parent inference
    from transitive list
  accessed_at: '2026-11-03T18:02:36.236579Z'
  snapshot_sha256: 8ac28f361c499fed2900602d7cc264f635cfe43618293abad299313b98e4cb37
  summary: Exact is_a ancestry supports organelle envelope lumen0031970. Typed child
    relations and source topology separately support parthood.
  support: supports
- evidence_id: micro-go-0005637-isa
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005637/ancestors?relations=is_a
  locator: Complete relations=is_a ancestor response; no immediate-parent inference
    from transitive list
  accessed_at: '2026-11-03T18:02:36.236637Z'
  snapshot_sha256: e3fdcfb1e6860613b57aacb0fe8ebbae8b30ad15ebe24917179d7b1384b445ca
  summary: Exact is_a ancestry supports organelle membrane0031090. Typed child relations
    and source topology separately support parthood.
  support: supports
- evidence_id: micro-go-0005640-isa
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005640/ancestors?relations=is_a
  locator: Complete relations=is_a ancestor response; no immediate-parent inference
    from transitive list
  accessed_at: '2026-11-03T18:02:36.236682Z'
  snapshot_sha256: e6df423117a695b4c03b922d9d6b8e9bb87d8123f4ae5fae82172142f9e2865c
  summary: Exact is_a ancestry supports organelle membrane0031090. Typed child relations
    and source topology separately support parthood.
  support: supports
- evidence_id: micro-tax2759
  kind: database
  reference: https://rest.uniprot.org/taxonomy/2759.json
  locator: taxonId, scientificName, rank and available parent/lineage
  accessed_at: '2026-11-03T18:02:36.236721Z'
  snapshot_sha256: af5ba762219fdecb11d214126bb8184c0eb28fc6474d14777c4aaa7f7dd89369
  summary: Native taxonomy confirms 2759 Eukaryota (domain). Species/strain references
    do not establish experimental background or numerical prevalence.
  support: supports
- evidence_id: micro-tax4932
  kind: database
  reference: https://rest.uniprot.org/taxonomy/4932.json
  locator: taxonId, scientificName, rank and available parent/lineage
  accessed_at: '2026-11-03T18:02:36.861630Z'
  snapshot_sha256: 963bbf3503fd0aa9e69dc25b64c5ae903f871991b37c4c593353b945c8e31688
  summary: Native taxonomy confirms 4932 Saccharomyces cerevisiae (species). Species/strain
    references do not establish experimental background or numerical prevalence.
  support: supports
- evidence_id: micro-tax559292
  kind: database
  reference: https://rest.uniprot.org/taxonomy/559292.json
  locator: taxonId, scientificName, rank and available parent/lineage
  accessed_at: '2026-11-03T18:02:37.033789Z'
  snapshot_sha256: 9ebcfe8a317cc0c25c329a3a6a7cc9eaa863bb2dfebe5eaff9a34628c6684810
  summary: Native taxonomy confirms 559292 Saccharomyces cerevisiae (strain ATCC 204508
    / S288c) (strain). Species/strain references do not establish experimental background
    or numerical prevalence.
  support: supports
- evidence_id: micro-protein-Q02821
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q02821.json
  locator: primaryAccession, reviewed status, recommended protein name, primary/synonym/locus
    gene fields, taxon559292; FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments
  accessed_at: '2026-11-03T18:02:37.041709Z'
  snapshot_sha256: 00fe385eee1db7cc3bc79dc0863b3e2a8b7007b9928fa357b4b4a301fcaf55ff
  summary: 'Reviewed S288C reference Q02821: SRP1, synonym KAP60, YNL189W. Correct
    reference instance and source-compatible role; not every assay strain or a complete
    source-neutral family inventory.'
  support: supports
- evidence_id: micro-family-Q02821
  kind: search
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q02821/?page_size=200
  locator: Exact InterPro integrated-entry association endpoint; page_size200; complete
    available results
  accessed_at: '2026-11-03T18:02:37.065976Z'
  snapshot_sha256: 30934f92146c4f37062b59142774992ba3380e526f66cfd91183aff7fcdea2ee
  summary: Exact protein-associated InterPro response has 7 entries; family entries
    IPR024931 Importin subunit alpha. Domains/repeats/superfamilies remain distinct;
    no proposed automatic record mutation.
  support: supports
  search_scope: InterPro API at 2026-11-03T18:02:37.065976Z, exact protein/uniprot/Q02821
    association request, integrated InterPro entries only, page_size200. All7 returned
    rows inspected; next=null.
- evidence_id: micro-protein-Q03707
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q03707.json
  locator: primaryAccession, reviewed status, recommended protein name, primary/synonym/locus
    gene fields, taxon559292; FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments
  accessed_at: '2026-11-03T18:02:37.076847Z'
  snapshot_sha256: f912f0a72abde9d834e9283910f7481d57e4fe676e96de9a61e96af84b6f7fc5
  summary: 'Reviewed S288C reference Q03707: SRC1, synonym HEH1, YML034W (YML033W
    ORF alias). Correct reference instance and source-compatible role; not every assay
    strain or a complete source-neutral family inventory.'
  support: supports
- evidence_id: micro-family-Q03707
  kind: search
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q03707/?page_size=200
  locator: Exact InterPro integrated-entry association endpoint; page_size200; complete
    available results
  accessed_at: '2026-11-03T18:02:37.271557Z'
  snapshot_sha256: 23fabdea5c06ad4b3d9f397c44253b70d1459c0c744c03ac413b71ea5fe3380d
  summary: Exact protein-associated InterPro response has 4 entries; family entries
    IPR044780 Heh2/Src1-like. Domains/repeats/superfamilies remain distinct; no proposed
    automatic record mutation.
  support: supports
  search_scope: InterPro API at 2026-11-03T18:02:37.271557Z, exact protein/uniprot/Q03707
    association request, integrated InterPro entries only, page_size200. All4 returned
    rows inspected; next=null.
- evidence_id: micro-protein-Q03281
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q03281.json
  locator: primaryAccession, reviewed status, recommended protein name, primary/synonym/locus
    gene fields, taxon559292; FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments
  accessed_at: '2026-11-03T18:02:37.471788Z'
  snapshot_sha256: 126694adc5baf08f02c78888ce625c88cc57643abc6da19ba6a68b7313b51045
  summary: 'Reviewed S288C reference Q03281: HEH2, YDR458C. Correct reference instance
    and source-compatible role; not every assay strain or a complete source-neutral
    family inventory.'
  support: supports
- evidence_id: micro-family-Q03281
  kind: search
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q03281/?page_size=200
  locator: Exact InterPro integrated-entry association endpoint; page_size200; complete
    available results
  accessed_at: '2026-11-03T18:02:37.616513Z'
  snapshot_sha256: d87c0f4b58677f82f84a96eab6bbfcd0bd88c42d30d4d6004a94fe47ee26f731
  summary: Exact protein-associated InterPro response has 5 entries; family entries
    IPR044780 Heh2/Src1-like. Domains/repeats/superfamilies remain distinct; no proposed
    automatic record mutation.
  support: supports
  search_scope: InterPro API at 2026-11-03T18:02:37.616513Z, exact protein/uniprot/Q03281
    association request, integrated InterPro entries only, page_size200. All5 returned
    rows inspected; next=null.
- evidence_id: micro-protein-P38881
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P38881.json
  locator: primaryAccession, reviewed status, recommended protein name, primary/synonym/locus
    gene fields, taxon559292; FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments
  accessed_at: '2026-11-03T18:02:38.415541Z'
  snapshot_sha256: 4e3daf10d4a641ffad9c2e3c2850dd073e2a69da5e833626c484de0d5807b86b
  summary: 'Reviewed S288C reference P38881: NVJ1, synonym VAB36, YHR195W. Correct
    reference instance and source-compatible role; not every assay strain or a complete
    source-neutral family inventory.'
  support: supports
- evidence_id: micro-family-P38881
  kind: search
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P38881/?page_size=200
  locator: Exact InterPro integrated-entry association endpoint; page_size200; complete
    available results
  accessed_at: '2026-11-03T18:02:38.444219Z'
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
  summary: Exact P38881 association request returned204/no content. This bounded response
    does not establish global absence of an Nvj1 family or justify guessing one.
  support: supports
  search_scope: InterPro API at 2026-11-03T18:02:38.444219Z, exact protein/uniprot/P38881
    association request, integrated InterPro entries only, page_size200. HTTP204 empty
    response; no expanded name search or universal absence claim.
- evidence_id: micro-protein-P39968
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P39968.json
  locator: primaryAccession, reviewed status, recommended protein name, primary/synonym/locus
    gene fields, taxon559292; FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments
  accessed_at: '2026-11-03T18:02:38.571812Z'
  snapshot_sha256: 8717485852a2be10a3d083ada88ed1cbbfbfe2a8ac02095c565a428ad14a6be8
  summary: 'Reviewed S288C reference P39968: VAC8, synonym YEB3, YEL013W. Correct
    reference instance and source-compatible role; not every assay strain or a complete
    source-neutral family inventory.'
  support: supports
- evidence_id: micro-family-P39968
  kind: search
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P39968/?page_size=200
  locator: Exact InterPro integrated-entry association endpoint; page_size200; complete
    available results
  accessed_at: '2026-11-03T18:02:38.740436Z'
  snapshot_sha256: c3c9179ac58aa61c9b277e28992ae9c2b3dc458640ccb3acd48ead8b1f2d484d
  summary: Exact protein-associated InterPro response has 4 entries; family entries
    IPR045156 Vacuolar protein 8. Domains/repeats/superfamilies remain distinct; no
    proposed automatic record mutation.
  support: supports
  search_scope: InterPro API at 2026-11-03T18:02:38.740436Z, exact protein/uniprot/P39968
    association request, integrated InterPro entries only, page_size200. All4 returned
    rows inspected; next=null.
- evidence_id: micro-hetzer2010-meta
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1101/cshperspect.a000539%22&format=json&resultType=core&pageSize=20
  locator: Exact quoted DOI EuropePMC core search, pageSize20, unique MED title/authors/year/DOI/PMID
    and complete abstract
  accessed_at: '2026-11-03T18:02:38.869452Z'
  snapshot_sha256: 3eed09b16c94934759f1a2d78c545f38942e0c1184f612cf94bb2d347873f6e3
  summary: Citation identity and complete abstract agree with the inspected secondary
    review; record title/year and narrow biological scope checked. Metadata alone
    is not full-body reading.
  support: context_only
- evidence_id: micro-aitchison2012-meta
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1534/genetics.111.127803%22&format=json&resultType=core&pageSize=20
  locator: Exact quoted DOI EuropePMC core search, pageSize20, unique MED title/authors/year/DOI/PMID
    and complete abstract
  accessed_at: '2026-11-03T18:02:39.306618Z'
  snapshot_sha256: e1b5996512104993b29a34d16c788770f778a17b3e241d73d42de9b1685b14bf
  summary: Citation identity and complete abstract agree with the inspected secondary
    review; record title/year and narrow biological scope checked. Metadata alone
    is not full-body reading.
  support: context_only
- evidence_id: micro-pan2000-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1091/mbc.11.7.2445%22&format=json&resultType=core&pageSize=20
  locator: Exact quoted DOI EuropePMC core search, pageSize20, unique MED title/authors/year/DOI/PMID
    and complete abstract
  accessed_at: '2026-11-03T18:02:39.496221Z'
  snapshot_sha256: f58ac090f70c0a13d7468f4406d98509469dc283ca3579d405f7ff65b1d11d15
  summary: Citation identity and complete abstract agree with the inspected primary
    study; record title/year and narrow biological scope checked. Metadata alone is
    not full-body reading.
  support: supports
- evidence_id: micro-king2006-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038/nature05075%22&format=json&resultType=core&pageSize=20
  locator: Exact quoted DOI EuropePMC core search, pageSize20, unique MED title/authors/year/DOI/PMID
    and complete abstract
  accessed_at: '2026-11-03T18:02:39.653954Z'
  snapshot_sha256: f6eb52e0b738928f454469dcc19ede605df9c10716cb592e97cddfdfcd0ef55f
  summary: Citation identity and complete abstract agree with the inspected primary
    study; record title/year and narrow biological scope checked. Metadata alone is
    not full-body reading.
  support: supports
- evidence_id: micro-hetzer2010-pmc
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2829960/
  locator: 'Genuine canonical PMC body: opening paragraphs/Table1 context/Figure1
    caption, complete s1,s7,s9,s10 and embedded captions; no image pixels'
  accessed_at: '2026-11-03T18:04:17.869889Z'
  snapshot_sha256: 6109676d737dfd53d013027192d728a4a4b2d0626e7ab3b4ed5592b0ce410a83
  summary: Secondary review supports double-envelope topology, perinuclear/ER continuity,
    pore transport and organization. Closed yeast/fungal mitosis differs from metazoan
    envelope breakdown. In-vitro assembly systems and debated mechanisms do not establish
    universal molecular formation necessity.
  support: context_only
- evidence_id: micro-aitchison2012-jats
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3296253.1/PMC3296253.1.xml
  locator: Genuine JATS opening main paragraphs, complete s1-s3,s10,s14 with embedded
    captions; partial s11 text not used for additional claims; no pixels
  accessed_at: '2026-11-03T18:04:17.869977Z'
  snapshot_sha256: 86f99d67fca3b4ce43a29b17335d4b8ba0b21653ccf508d16ee01163a2be6422
  summary: Secondary yeast NPC review supports protein-complex architecture, envelope
    span and selective nucleocytoplasmic transport. Transport driving gradients and
    soluble machinery are distinct from intrinsic pore gating; no pore-powered universal
    mechanism or complete inventory inferred.
  support: context_only
- evidence_id: micro-pan2000-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC14931/
  locator: Genuine PMC body Methodssec3-6,9; Resultssec11-17 and complete Discussionsec18-20,
    embedded Figure1-9 captions; no pixels or unlisted Methods
  accessed_at: '2026-11-03T18:04:17.870110Z'
  snapshot_sha256: 8bd997f8509fdbd22d9aa789a327bf45569958c821f8f9b26176a0f9d6acdc38
  summary: YEF473/L40 yeast localization, two-hybrid, copurification, deletion/overexpression
    and TEM support Nvj1 nuclear-envelope/Vac8 vacuole contacts. Authors interpret
    direct interaction but explicitly retain a remote indirect-binding possibility
    insec11. NVJ necessity is not entire nuclear-membrane formation necessity; bacterial/strain
    conflation avoided.
  support: supports
- evidence_id: micro-king2006-supp
  kind: primary_source
  reference: https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fnature05075/MediaObjects/41586_2006_BFnature05075_MOESM1_ESM.pdf
  locator: 'Genuine publisher PDF: textual FiguresS1-S5 captions, complete Supplementary
    Methods and Tables1-2 including strain footnote; no pixels'
  accessed_at: '2026-11-03T18:05:06.471297Z'
  snapshot_sha256: 76a228dbcf25e557d794c15e7d6f977d4092aef6fad2b7647a34a8cc37f00ec9
  summary: Heh localization/Ran-mutant assays, NLS constructs and strain details support
    yeast targeting scope. Strains are W303-derived except named backgrounds including
    BY4741; not uniformly S288C. S1 is a model and predicted NLSs are distinguished
    from tested sequences.
  support: supports
- evidence_id: micro-king2006-browser-opening
  kind: primary_source
  reference: https://www.researchgate.net/publication/6859612_King_MC_Lusk_CP_Blobel_G_Karyopherin-mediated_import_of_integral_inner_nuclear_membrane_proteins_Nature_442_1003-1007
  locator: Browser-displayed author-uploaded primary opening/Introduction and selected
    Results/Discussion/Methods; printed1003-1006, displayed lines67-848 in returned
    excerpt
  accessed_at: '2026-11-03T18:04:53Z'
  snapshot_sha256: 688c2c4035ab2f751c4b271db647d4854492a80fae0a945e1f15857c4936afb4
  summary: Actual current browser-displayed primary author text supports named yeast
    Heh1/Heh2 cargo targeting via Ran/Kap60/Kap95, with direct Heh2-Kap60 binding
    and NLS perturbation. Retention and proposed NPC rearrangements remain limited
    interpretations. Browser snapshot is not a native HTTP200 full-PDF attestation;
    no image pixels or unread lines certified.
  support: supports
- evidence_id: micro-king2006-browser-body
  kind: primary_source
  reference: https://www.researchgate.net/publication/6859612_King_MC_Lusk_CP_Blobel_G_Karyopherin-mediated_import_of_integral_inner_nuclear_membrane_proteins_Nature_442_1003-1007
  locator: Additional browser excerpts displayed lines41-415 and345-715, including
    Heh1/Heh2 identity/localization, Kap60 pull-down, NLS-deletion/swap results and
    Figure1-3 captions
  accessed_at: '2026-11-03T18:05:37Z'
  snapshot_sha256: 927f0ce0738cd68242fff6cdb42d3b1856ea61c6dbbddf26ae93ba86b83e43ff
  summary: Actual current browser-displayed primary author text supports named yeast
    Heh1/Heh2 cargo targeting via Ran/Kap60/Kap95, with direct Heh2-Kap60 binding
    and NLS perturbation. Retention and proposed NPC rearrangements remain limited
    interpretations. Browser snapshot is not a native HTTP200 full-PDF attestation;
    no image pixels or unread lines certified.
  support: supports
- evidence_id: micro-king2006-main-access
  kind: validation
  reference: https://www.nature.com/articles/nature05075.pdf
  locator: Inspected HTTP200 body begins HTML, not PDF; attempted pdftotext rejected
    non-PDF bytes
  accessed_at: '2026-11-03T18:04:18.141855Z'
  snapshot_sha256: fa4ebf82f56ba40b35d3c7eadb8ddda59405a7dd392e037be81642f116f5903d
  summary: Publisher main-PDF route returned subscription-preview HTML, not a recovered
    PDF. Scientific body assessment uses separately timestamped browser author text
    and genuine supplement. Hetzer/Pan S3 candidate routes returned404; their canonical
    PMC bodies succeeded.
  support: context_only
- evidence_id: micro-catalogue
  kind: search
  reference: https://imodulondb.org/api/datasets
  locator: 'Complete official array: all20 organism rows/28 organism-dataset pairs
    inspected'
  accessed_at: '2026-11-03T18:02:38.805726Z'
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  summary: No Saccharomyces/cerevisiae/S288C/W303/YEF473/L40 or eukaryotic host dataset
    occurs in this bounded catalogue. No matched downstream gene/module search or
    bacterial surrogate is warranted. Noncoverage does not refute nuclear-envelope
    biology.
  support: supports
  search_scope: Official iModulonDB /api/datasets at 2026-11-03T18:02:38.805726Z;
    complete20 rows/28 organism-dataset pairs, no pagination. All names/keys inspected
    and Saccharomyces/cerevisiae/yeast/S288C/W303/YEF473/L40 compared. No universal
    transcriptomic or biological absence conclusion.
- evidence_id: micro-historical-runner
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical00:49Z runner attempt/exit1/PermissionError reading pyvenv.cfg
  accessed_at: '2026-11-03T00:49:00.863225Z'
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  summary: Historical optional runner unavailable, not rerun or falsely dated current.
    Current official catalogue fallback succeeded independently.
  support: context_only
- evidence_id: check-qc
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/qc.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T18:07:19.576488Z'
  support: supports
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  snapshot_sha256: 676f862a4e4202396d6aa783204944b49e27f600b60d99e33901bf1c060be12f
- evidence_id: check-labels
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/labels.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T18:02:39.520119Z'
  support: supports
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  snapshot_sha256: 6cdfb05df9a27194f05a5fd7f851783f817ac1523ca0bbfa54fe0e0d18775905
- evidence_id: check-trait-links
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/trait-links.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T18:02:17.302307Z'
  support: supports
  summary: Native TraitMech link check passed.
  snapshot_sha256: 8b336cdefbbd3daf6da8787990efdbe346c95e2c8361d50b7eb68a18f2d5a44a
- evidence_id: check-vendored
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/vendored.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T18:02:14.817714Z'
  support: supports
  summary: Pinned governed files match; native vendored check passed.
  snapshot_sha256: b1f169d103aaefa930745468bcca171e5867b9cc49e4e74311e458097e3252a6
- evidence_id: check-curies
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/curies.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T18:02:17.512731Z'
  support: supports
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  snapshot_sha256: bc12b1285f5747707643f7a98e03dbb3a6c88fb062ad49f99db9cb42ececf3d2
- evidence_id: focused
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/focused-results.json
  locator: All twenty actual target schema/strict command outputs
  accessed_at: '2026-11-03T18:12:39Z'
  support: supports
  summary: Ten schema and ten strict commands returned exit zero.
  snapshot_sha256: 11ac3e1515c615ebff9bf5e2a8704e36f50df651d35c0777c6a347f999df3176
- evidence_id: supplemental-pmid
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2372/pmid-chunks-receipt.json
  locator: Complete native-report PMID set checked with unchanged resolver in batches
    of at most fifty
  accessed_at: '2026-11-03T18:03:04.388972Z'
  support: supports
  summary: 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers
    remain unverified.
  snapshot_sha256: 76b47fded285092eb7af2d466186368e283f58e9042fa45c9bf389f60dd9fcbe
- evidence_id: historical-adapter-runner-availability
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical runner invocation receipt, exact SHA256 reverified during PR2372
    synthesis
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  summary: Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS
    PermissionError reading the configured runner pyvenv.cfg. This is a retained historical
    availability observation, not a fresh attempt or a scientific validation failure.
    Native policy permits inspected source-catalogue fallback.
assessments:
- assessment_id: septin-nitroplast-schema
  area: schema
  topic: Original native validation/render and source binding
  outcome: supported
  summary: Original native validation/render passes with exact Markdown and verified
    historical target hash. Current target remains byte-identical to its historical
    review input. Schema success is not a scientific verdict.
  target_ids:
  - cellstructuremech:nitroplast
  evidence_ids:
  - septin-record-nitroplast
  - septin-original-nitroplast
  - septin-original-validation-nitroplast
- assessment_id: septin-nitroplast-native
  area: provenance
  topic: Actual molecular identifier coverage
  outcome: supported
  summary: Both native commands exit0 over independently verified zero examples/typed
    molecular nodes/UniProt graph xrefs. Narrative proteins/pathways still require
    scientific review; generic success does not establish inventory completeness.
  target_ids:
  - cellstructuremech:nitroplast
  evidence_ids:
  - septin-record-nitroplast
  - septin-native-nitroplast-verify
  - septin-native-nitroplast-causal
- assessment_id: septin-nitroplast-adapter
  area: scope
  topic: Full-claim molecular applicability and matched catalogue
  outcome: supported
  summary: Nitrogenase/NifH, nitrogen fixation, host-protein import and uTP claims
    trigger the native structured-source assessment. The original expression-only
    rationale is insufficient. Fresh complete catalogue has no matched host/endosymbiont;
    downstream gene/module calls are not applicable to unmatched taxa. Current primary/authority
    fallback is explicit, historical runner failure retains its actual time.
  target_ids:
  - cellstructuremech:nitroplast
  evidence_ids:
  - septin-record-nitroplast
  - septin-original-nitroplast
  - septin-review-policy
  - septin-catalogue
  - septin-adapter-runner-historical
- assessment_id: septin-nucleomorph-schema
  area: schema
  topic: Original native validation/render and source binding
  outcome: supported
  summary: Original native validation/render passes with exact Markdown and verified
    historical target hash. Current target remains byte-identical to its historical
    review input. Schema success is not a scientific verdict.
  target_ids:
  - GO:0033009
  evidence_ids:
  - septin-record-nucleomorph
  - septin-original-nucleomorph
  - septin-original-validation-nucleomorph
- assessment_id: septin-nucleomorph-native
  area: provenance
  topic: Actual molecular identifier coverage
  outcome: supported
  summary: Both native commands exit0 over independently verified zero examples/typed
    molecular nodes/UniProt graph xrefs. Narrative proteins/pathways still require
    scientific review; generic success does not establish inventory completeness.
  target_ids:
  - GO:0033009
  evidence_ids:
  - septin-record-nucleomorph
  - septin-native-nucleomorph-verify
  - septin-native-nucleomorph-causal
- assessment_id: septin-nucleomorph-adapter
  area: scope
  topic: Full-claim molecular applicability and matched catalogue
  outcome: supported
  summary: Residual essential genes, replication and host cell-cycle coordination
    trigger the native structured-source assessment. The original expression-only
    rationale is insufficient. Fresh complete catalogue has no matched host/endosymbiont;
    downstream gene/module calls are not applicable to unmatched taxa. Current primary/authority
    fallback is explicit, historical runner failure retains its actual time.
  target_ids:
  - GO:0033009
  evidence_ids:
  - septin-record-nucleomorph
  - septin-original-nucleomorph
  - septin-review-policy
  - septin-catalogue
  - septin-adapter-runner-historical
- assessment_id: septin-organellar_chromatophore-schema
  area: schema
  topic: Original native validation/render and source binding
  outcome: supported
  summary: Original native validation/render passes with exact Markdown and verified
    historical target hash. Current chromatophore differs by a graph-parthood edge
    and curation event; frozen current bytes are fully reassessed. Schema success
    is not a scientific verdict.
  target_ids:
  - GO:0070111
  evidence_ids:
  - septin-record-organellar_chromatophore
  - septin-original-organellar_chromatophore
  - septin-original-validation-organellar_chromatophore
- assessment_id: septin-organellar_chromatophore-native
  area: provenance
  topic: Actual molecular identifier coverage
  outcome: supported
  summary: Both native commands exit0 over independently verified zero examples/typed
    molecular nodes/UniProt graph xrefs. Narrative proteins/pathways still require
    scientific review; generic success does not establish inventory completeness.
  target_ids:
  - GO:0070111
  evidence_ids:
  - septin-record-organellar_chromatophore
  - septin-native-organellar_chromatophore-verify
  - septin-native-organellar_chromatophore-causal
- assessment_id: septin-organellar_chromatophore-adapter
  area: scope
  topic: Full-claim molecular applicability and matched catalogue
  outcome: supported
  summary: Photosynthesis, protein import and thylakoid light-complex claims trigger
    the native structured-source assessment. The original expression-only rationale
    is insufficient. Fresh complete catalogue has no matched host/endosymbiont; downstream
    gene/module calls are not applicable to unmatched taxa. Current primary/authority
    fallback is explicit, historical runner failure retains its actual time.
  target_ids:
  - GO:0070111
  evidence_ids:
  - septin-record-organellar_chromatophore
  - septin-original-organellar_chromatophore
  - septin-review-policy
  - septin-catalogue
  - septin-adapter-runner-historical
- assessment_id: septin-nitroplast-identity
  area: identity
  topic: Local organelle identity and boundary
  outcome: supported
  summary: A compartment identity is distinguished from the host/cyanobacterial taxon
    and frozen diazoplast neighbor. Bounded exact GO search supports local identity
    with broad intracellular-organelle parent; related UCYN-A spheroid-body wording
    is qualified by host/import scope.
  target_ids:
  - cellstructuremech:nitroplast
  evidence_ids:
  - septin-record-nitroplast
  - septin-go
  - septin-go-search-nitroplast
  - septin-coale2024-main-page1
  - septin-context-diazoplast
- assessment_id: septin-nitroplast-scope
  area: scope
  topic: Verified host, strain and qualitative variation
  outcome: supported
  summary: Current taxon373042 and Hagino genotypeIII/FR12/FR21 mapping agree. Coale
    supplement identifies FR21=NIES4399; KC1-P2 culture loss supports cautious VARIABLE
    occurrence, not an environmental frequency or proven loss mechanism.
  target_ids:
  - cellstructuremech:nitroplast
  evidence_ids:
  - septin-record-nitroplast
  - septin-tax373042
  - septin-hagino2026-body
  - septin-coale2024-supp-page2
- assessment_id: septin-nitroplast-components
  area: grounding
  topic: Collective membrane OTHER and nitrogenase complex
  outcome: supported
  summary: Membrane GO0016020 is deliberately structural OTHER, supported by native
    structural-constituent precedent and actual lamellar images. Nitrogenase GO0016610
    is a proper complex identity; NifH enrichment/activity support membership without
    asserting exact subunits or stoichiometry.
  target_ids:
  - cellstructuremech:nitroplast
  evidence_ids:
  - septin-record-nitroplast
  - septin-go
  - septin-structural-other-precedent
  - septin-schema-policy
  - septin-hagino2026-body
  - septin-coale2024-main-page3
  - septin-coale2024-supp-page7
- assessment_id: septin-nitroplast-necessity
  area: evidence
  topic: Formation essentiality remains untested
  outcome: unknown
  summary: Both components retain UNKNOWN assembly essentiality. Source localization,
    enrichment and acetylene reduction do not establish an organelle-formation knockout,
    molecular stoichiometry or a specific import apparatus.
  target_ids:
  - cellstructuremech:nitroplast
  evidence_ids:
  - septin-record-nitroplast
  - septin-coale2024-main-page3
  - septin-coale2024-supp-page7
  - septin-protein-policy
- assessment_id: septin-nitroplast-function
  area: evidence
  topic: Nitrogen fixation experimental scope
  outcome: supported
  summary: Relative daytime acetylene reduction in triplicate FR21 culture supports
    nitrogenase activity and the nitrogen-fixation function. Whole-culture measurements
    are not claimed as isolated-organelle flux or raw isotopic transfer measurements.
  target_ids:
  - cellstructuremech:nitroplast
  evidence_ids:
  - septin-record-nitroplast
  - septin-go
  - septin-coale2024-supp-page2
  - septin-coale2024-supp-page7
  - septin-coale2024-supp-page11
- assessment_id: septin-nitroplast-import
  area: evidence
  topic: Import evidence and prediction boundary
  outcome: supported
  summary: Enrichment-based host-protein import and coordinated division support the
    organelle description. Predicted-only uTP candidates remain excluded; no proven
    uTP cleavage, translocon identity, mitochondrial ATP delivery or candidate-specific
    causal role is asserted.
  target_ids:
  - cellstructuremech:nitroplast
  evidence_ids:
  - septin-record-nitroplast
  - septin-coale2024-main-page1
  - septin-coale2024-main-page3
  - septin-coale2024-main-page4
  - septin-coale2024-main-page5
- assessment_id: septin-nitroplast-preprint
  area: evidence
  topic: Transport discussion preserves preprint limits
  outcome: supported
  summary: Current XML identifies Li2026 version1 as a preprint. Its discussion explicitly
    withholds cargo/direction/substrate identification and mechanistic proof from
    static architecture. The record leaves this open and adds no invented density
    identity or transport edge.
  target_ids:
  - cellstructuremech:nitroplast
  evidence_ids:
  - septin-record-nitroplast
  - septin-li2026-meta
  - septin-li2026-xml
- assessment_id: septin-nitroplast-image
  area: provenance
  topic: Actually inspected TEM panels and copyright
  outcome: supported
  summary: Fresh genuine PDF and actual pixel inspection verify FR21 Fig28/29, Nit
    labels and1um scale; adjacent OTR22-B Fig30/31 is excluded. Copyright appears
    on the article first page (PDF2). Link-only OTHER/attribution is appropriate;
    no redistribution permission is inferred.
  target_ids:
  - cellstructuremech:nitroplast
  evidence_ids:
  - septin-record-nitroplast
  - septin-hagino2026-body
  - septin-pixels-hagino2026-p1
  - septin-pixels-hagino2026-13
  - septin-pixels-hagino2026-14
- assessment_id: septin-nitroplast-completeness
  area: completeness
  topic: Qualified sparse record, history and absent graph
  outcome: supported
  summary: PROPOSED history and explicit resolved/open discussion boundaries remain
    coherent. No causal graph, protein examples, associated trait, numeric measurement
    field or verbatim snippet requires invented completion. Optional graph/protein
    absence is not a defect.
  target_ids:
  - cellstructuremech:nitroplast
  evidence_ids:
  - septin-record-nitroplast
  - septin-review-policy
  - septin-graph-policy
  - septin-protein-policy
- assessment_id: septin-nitroplast-verdict
  area: completeness
  topic: Current scientific verdict
  outcome: supported
  summary: 'pass_with_limitations: no confirmed scientific finding, with source/prediction/preprint/formation
    and empty-native-coverage limits retained. Applicability bundle correction is
    separate.'
  target_ids:
  - cellstructuremech:nitroplast
  evidence_ids:
  - septin-record-nitroplast
  - septin-go
  - septin-hagino2026-body
  - septin-coale2024-main-page3
  - septin-li2026-xml
- assessment_id: septin-nucleomorph-identity
  area: identity
  topic: Exact nucleus identity, synonymy and parthood
  outcome: supported
  summary: GO0033009 matches the vestigial eukaryotic nucleus. GO0043231 parent and
    GO0009536 plastid parthood are distinct; red/green endosymbiont origins and residual/remnant
    nucleus synonymy are supported by Tanifuji background and Curtis abstract.
  target_ids:
  - GO:0033009
  evidence_ids:
  - septin-record-nucleomorph
  - septin-go
  - septin-curtis2012-meta
  - septin-tanifuji2014-xml
  - septin-context-plastid
- assessment_id: septin-nucleomorph-scope
  area: scope
  topic: Taxa and canonical examples
  outcome: supported
  summary: Cryptophyceae3027, Chlorarachniophyceae29197, G.theta55529 and B.natans227086
    match authority. Qualitative COMMON is not a numeric survey; precise experimental
    scope is G.theta CCMP2712 and comparative L.oceanica CCMP622, not every strain.
  target_ids:
  - GO:0033009
  evidence_ids:
  - septin-record-nucleomorph
  - septin-tax3027
  - septin-tax29197
  - septin-tax55529
  - septin-tax227086
  - septin-curtis2012-meta
  - septin-tanifuji2014-xml
  - septin-onuma2017-xml
- assessment_id: septin-nucleomorph-components
  area: grounding
  topic: Collective chromosome DNA and label-only identity
  outcome: supported
  summary: Tanifuji directly resolves three linear chromosomes in L.oceanica, with
    repeat-size uncertainty. DNA constituent remains reviewed-label-only instead of
    a guessed exact chromosome CURIE. ESSENTIAL describes the collectively retained
    genome, not each chromosome/gene universally required for organelle assembly.
  target_ids:
  - GO:0033009
  evidence_ids:
  - septin-record-nucleomorph
  - septin-tanifuji2014-xml
  - septin-curtis2012-meta
  - septin-curation-policy
  - septin-schema-policy
- assessment_id: septin-nucleomorph-necessity
  area: evidence
  topic: Individual formation requirements untested
  outcome: unknown
  summary: Sequence retention and essential-gene evolutionary interpretation do not
    establish individual chromosome/gene depletion, division machinery or an envelope-formation
    pathway. Optional machinery and exact cross-lineage constituents remain explicitly
    open.
  target_ids:
  - GO:0033009
  evidence_ids:
  - septin-record-nucleomorph
  - septin-curtis2012-meta
  - septin-tanifuji2014-xml
  - septin-onuma2017-xml
- assessment_id: septin-nucleomorph-replication
  area: evidence
  topic: Cell-cycle replication measured at bounded scope
  outcome: supported
  summary: Onuma localization and EdU experiments support the G.theta replication
    example. The experiment is only partially synchronized and nucleomorph replication
    is later/longer than nuclear synthesis. Functional edge explicitly names G.theta;
    scope_notes call it an example, so the general graph description is read in that
    bounded context.
  target_ids:
  - GO:0033009
  evidence_ids:
  - septin-record-nucleomorph
  - septin-onuma2017-xml
- assessment_id: septin-nucleomorph-graph
  area: graph
  topic: All four descriptive genome-retention edges
  outcome: supported
  summary: Chromosomes housed in nucleomorph, nucleomorph part_of plastid, residual
    essential genes encoded, and G.theta replication example have direct cited support.
    NONMECHANISTIC scope excludes envelope/replication machinery. No causal intervention
    or universal phase identity is inferred.
  target_ids:
  - GO:0033009
  evidence_ids:
  - septin-record-nucleomorph
  - septin-go
  - septin-tanifuji2014-xml
  - septin-curtis2012-meta
  - septin-onuma2017-xml
  - septin-graph-policy
- assessment_id: septin-nucleomorph-limits
  area: provenance
  topic: Actual access tiers and historical boundaries
  outcome: supported
  summary: Curtis is complete abstract only after publisher challenge; Tanifuji and
    Onuma are genuine body sections and captions, not pixels or raw sequence/EdU reanalysis.
    Historical519/520 curation and open inventory TODO are context, not newly resolved
    issues. No image/trait/snippet scope occurs.
  target_ids:
  - GO:0033009
  evidence_ids:
  - septin-record-nucleomorph
  - septin-curtis2012-meta
  - septin-tanifuji2014-xml
  - septin-onuma2017-xml
- assessment_id: septin-nucleomorph-verdict
  area: completeness
  topic: Current scientific verdict
  outcome: supported
  summary: 'pass_with_limitations: no confirmed new finding; preserve collective-versus-individual
    necessity, experimental scope, abstract/body access and empty-native coverage.
    Applicability bundle correction is separate.'
  target_ids:
  - GO:0033009
  evidence_ids:
  - septin-record-nucleomorph
  - septin-go
  - septin-tanifuji2014-xml
  - septin-onuma2017-xml
  - septin-curtis2012-meta
- assessment_id: septin-organellar_chromatophore-identity
  area: identity
  topic: Exact organelle, synonym, plastid and parts
  outcome: supported
  summary: GO0070111 and SL0351 support exact organelle identity, Paulinella-type
    synonym and plastid class. Exact membrane/IMS/thylakoid/lumen identities remain
    structural parts, not chemical lipids. Hierarchy paths are distinguished from
    direct source relations.
  target_ids:
  - GO:0070111
  evidence_ids:
  - septin-record-organellar_chromatophore
  - septin-go
  - septin-SL0351
  - septin-context-plastid
- assessment_id: septin-organellar_chromatophore-scope
  area: scope
  topic: Paulinella source and strain scope
  outcome: supported
  summary: NCBITaxon39717 matches P.chromatophora; Nowack2012 uses CCAC0185, subisolate
    M0880/a. Secondary Nowack2014/Gabr2020 abstracts supply qualitative context, not
    numerical COMMON prevalence or all-strain import equivalence.
  target_ids:
  - GO:0070111
  evidence_ids:
  - septin-record-organellar_chromatophore
  - septin-tax39717
  - septin-nowack2012-prefixed
  - septin-nowack2014-crossref
  - septin-gabr2020-meta
- assessment_id: septin-organellar_chromatophore-lipids
  area: grounding
  topic: Inherited F1 whole-membrane molecular grounding
  outcome: concern
  summary: Three LIPID rows identify whole GO membranes and are joined to STRUCTURE
    graph nodes. This remains the original major F1. Preserve anatomical parts; separately
    curate structural types or supported chemical materials without guessed lipid
    identifiers.
  target_ids:
  - GO:0070111
  evidence_ids:
  - septin-record-organellar_chromatophore
  - septin-original-organellar_chromatophore
  - septin-go
  - septin-SL0351
  - septin-schema-policy
- assessment_id: septin-organellar_chromatophore-peptidoglycan
  area: grounding
  topic: Supported residual wall and unresolved chemical detail
  outcome: supported
  summary: SL0351 directly places residual peptidoglycan between envelope membranes.
    Label-only status and UNKNOWN necessity avoid unsupported exact polymer chemistry
    and assembly claims; import machinery remains an explicit TODO.
  target_ids:
  - GO:0070111
  evidence_ids:
  - septin-record-organellar_chromatophore
  - septin-SL0351
  - septin-curation-policy
- assessment_id: septin-organellar_chromatophore-import
  area: evidence
  topic: Bounded demonstrated import and inferred routes
  outcome: supported
  summary: Nowack experimental localization/PSI purification/labelling supports nuclear-protein
    import. Singer complete abstract corroborates wider import but combines experimental
    and predicted catalogue entries. The maintained record does not assert a complete
    translocon or proven Golgi route.
  target_ids:
  - GO:0070111
  evidence_ids:
  - septin-record-organellar_chromatophore
  - septin-nowack2012-prefixed
  - septin-singer2017-meta
- assessment_id: septin-organellar_chromatophore-attribution
  area: evidence
  topic: Inherited F2 GO definition scope
  outcome: concern
  summary: GO0070118 defines the thylakoid bilayer, not a light-reaction-complex system.
    Component note expands this to an internal photosynthetic system and graph edge3
    explicitly credits GO with light complexes. Keep original F2 fields and attach
    inspected primary PSI evidence to the biological claim.
  target_ids:
  - GO:0070111
  evidence_ids:
  - septin-record-organellar_chromatophore
  - septin-original-organellar_chromatophore
  - septin-go
  - septin-nowack2012-prefixed
- assessment_id: septin-organellar_chromatophore-stale-edge
  area: graph
  topic: Substantive refresh of new thylakoid parthood edge
  outcome: supported
  summary: Current edge5 correctly states the transitive GO route0070118→0070116→0070111;
    it does not falsely call this direct. SL0351 supplies broader whole-organelle
    thylakoid context, not an exact membrane definition. Nowack localization/topology
    supports the internal photosynthetic system. New curation event records this topology
    addition; no new scientific finding is established.
  target_ids:
  - GO:0070111
  evidence_ids:
  - septin-record-organellar_chromatophore
  - septin-original-organellar_chromatophore
  - septin-go
  - septin-SL0351
  - septin-nowack2012-prefixed
- assessment_id: septin-organellar_chromatophore-graph
  area: graph
  topic: Full current six-edge topology/function graph
  outcome: supported
  summary: Outer/inner boundaries, retained wall, thylakoid photosynthetic support,
    import and new parthood are scientifically coherent at NONMECHANISTIC scope. Existing
    molecular joins and source-note defects remain F1/F2; no complete machinery or
    individual necessity is certified.
  target_ids:
  - GO:0070111
  evidence_ids:
  - septin-record-organellar_chromatophore
  - septin-go
  - septin-SL0351
  - septin-nowack2012-prefixed
  - septin-graph-policy
- assessment_id: septin-organellar_chromatophore-necessity
  area: evidence
  topic: Formation evidence remains unknown
  outcome: unknown
  summary: All component essentialities remain UNKNOWN. Imported protein association
    and anatomical descriptions do not establish individual membrane/lipid/protein
    formation requirements. No optional protein-example or generic-class enum finding
    is manufactured.
  target_ids:
  - GO:0070111
  evidence_ids:
  - septin-record-organellar_chromatophore
  - septin-nowack2012-prefixed
  - septin-singer2017-meta
  - septin-protein-policy
- assessment_id: septin-organellar_chromatophore-verdict
  area: completeness
  topic: Current scientific verdict
  outcome: concern
  summary: needs_curation for two confirmed inherited findings, one major grounding
    and one minor attribution. Stale edge is substantively refreshed and supported;
    no new scientific finding. No image, trait or snippet assessment is invented.
  target_ids:
  - GO:0070111
  evidence_ids:
  - septin-record-organellar_chromatophore
  - septin-original-organellar_chromatophore
  - septin-go
  - septin-SL0351
  - septin-nowack2012-prefixed
- assessment_id: plaque-t4-native
  area: schema
  topic: Actual native coverage
  outcome: supported
  summary: Actual inventory has zero protein_examples and zero GENE_OR_PROTEIN nodes.
    Native pass is empty represented accession/typed-node coverage, not proof of narrative
    molecular identity, pathway support or necessity.
  target_ids:
  - GO:0031981
  evidence_ids:
  - plaque-current-4
  - plaque-native-nuclear_lumen-verify
  - plaque-native-nuclear_lumen-causal
  - plaque-protein-contract
- assessment_id: plaque-t4-schema
  area: schema
  topic: Original rendering and frozen inputs
  outcome: supported
  summary: Original native validation and exact Markdown render pass; every historical
    input and unchanged current target verified. PROPOSED status retained. Optional
    inventories are not fabricated requirements.
  target_ids:
  - GO:0031981
  evidence_ids:
  - plaque-current-4
  - plaque-original-4
  - plaque-original-checks
  - plaque-rubric
- assessment_id: plaque-t5-native
  area: schema
  topic: Actual native coverage
  outcome: supported
  summary: Actual inventory has zero protein_examples and zero GENE_OR_PROTEIN nodes.
    Native pass is empty represented accession/typed-node coverage, not proof of narrative
    molecular identity, pathway support or necessity.
  target_ids:
  - cellstructuremech:nuclear_net
  evidence_ids:
  - plaque-current-5
  - plaque-native-nuclear_net-verify
  - plaque-native-nuclear_net-causal
  - plaque-protein-contract
- assessment_id: plaque-t5-schema
  area: schema
  topic: Original rendering and frozen inputs
  outcome: supported
  summary: Original native validation and exact Markdown render pass; every historical
    input and unchanged current target verified. PROPOSED status retained. Optional
    inventories are not fabricated requirements.
  target_ids:
  - cellstructuremech:nuclear_net
  evidence_ids:
  - plaque-current-5
  - plaque-original-5
  - plaque-original-checks
  - plaque-rubric
- assessment_id: plaque-t8-native
  area: schema
  topic: Actual native coverage
  outcome: supported
  summary: Actual inventory has zero protein_examples and zero GENE_OR_PROTEIN nodes.
    Native pass is empty represented accession/typed-node coverage, not proof of narrative
    molecular identity, pathway support or necessity.
  target_ids:
  - GO:0005634
  evidence_ids:
  - plaque-current-8
  - plaque-native-nucleus-verify
  - plaque-native-nucleus-causal
  - plaque-protein-contract
- assessment_id: plaque-t8-schema
  area: schema
  topic: Original rendering and frozen inputs
  outcome: supported
  summary: Original native validation and exact Markdown render pass; every historical
    input and unchanged current target verified. PROPOSED status retained. Optional
    inventories are not fabricated requirements.
  target_ids:
  - GO:0005634
  evidence_ids:
  - plaque-current-8
  - plaque-original-8
  - plaque-original-checks
  - plaque-rubric
- assessment_id: plaque-t4-identity
  area: identity
  topic: Exact nuclear enclosed volume
  outcome: supported
  summary: GO0031981 denotes volume inside nuclear inner membrane, with0070013 is_a
    ancestry and nucleus parthood. This is distinct from the space between envelope
    membranes.
  target_ids:
  - GO:0031981
  evidence_ids:
  - plaque-current-4
  - plaque-go
  - plaque-GO0031981-isa
- assessment_id: plaque-t4-parts
  area: grounding
  topic: Contained chromosome and nucleolus structural parts
  outcome: supported
  summary: OTHER components name exact structural constituents0000228 and0005730;
    both are typed part_of children of lumen. They are not asserted as single chemical
    DNA/RNA/protein identities. Explicit OTHER and maintained regression precedent
    prevent an automatic molecular-type finding; broader class-prose tension is not
    a confirmed record defect.
  target_ids:
  - GO:0031981
  evidence_ids:
  - plaque-current-4
  - plaque-go
  - plaque-schema-policy
  - plaque-other-precedent
- assessment_id: plaque-t4-genome
  area: evidence
  topic: Bounded yeast genome-model support
  outcome: supported
  summary: Duan primary population-based model supports the bounded yeast nuclear-genome
    organization note. BY4741-derived formaldehyde/3C methods and model limitations
    are explicit; no per-cell or all-lineage topology, raw-data validation or exact
    universal chromosome positions inferred.
  target_ids:
  - GO:0031981
  evidence_ids:
  - plaque-current-4
  - plaque-duan2010-meta
  - plaque-duan2010-bioc
  - plaque-duan2010-numeric
- assessment_id: plaque-t4-nucleolus
  area: evidence
  topic: Ribosome-biogenesis functions
  outcome: supported
  summary: Current GO plus complete Boisvert review abstract/Key Points support rDNA
    transcription, pre-rRNA processing and early ribosomal assembly. These are positive
    molecular/pathway assertions despite the overall topology scope; full review body
    and cited-primary experiments were not inspected.
  target_ids:
  - GO:0031981
  evidence_ids:
  - plaque-current-4
  - plaque-go
  - plaque-boisvert2007-meta
  - plaque-boisvert2007-publisher
- assessment_id: plaque-t4-graph
  area: graph
  topic: Four descriptive topology edges
  outcome: supported
  summary: Inner membrane delimits lumen, lumen is nuclear part, chromosome/nucleolus
    reside inside. Intact-nucleus phase restriction is preserved; topology does not
    assert assembly causality or a complete matrix/protein repertoire.
  target_ids:
  - GO:0031981
  evidence_ids:
  - plaque-current-4
  - plaque-go
  - plaque-graph-rubric
- assessment_id: plaque-t4-boundary
  area: scope
  topic: Nucleoplasm boundary and optional substructures
  outcome: supported
  summary: Current GO nucleoplasm definition excludes chromosome/nucleolus and lists
    it as lumen part. Maintained discussion merely says exact synonymy was not established;
    it does not equate the regions or impose an unsupported size comparison. Open
    additional-substructure TODO acknowledges a bounded inventory.
  target_ids:
  - GO:0031981
  evidence_ids:
  - plaque-current-4
  - plaque-go
  - plaque-rubric
- assessment_id: plaque-t4-adapter
  area: evidence
  topic: Positive nucleolar molecular functions trigger assessment
  outcome: supported
  summary: rDNA transcription/pre-rRNA processing/ribosome assembly trigger native
    applicability. Original explicit no-expression exemption requires correction.
    Fresh catalogue has no matching eukaryotic host; no downstream foreign-host queries
    or negative biology.
  target_ids:
  - GO:0031981
  evidence_ids:
  - plaque-current-4
  - plaque-original-4
  - plaque-policy
  - plaque-catalogue
  - plaque-historical-runner
- assessment_id: plaque-t4-limits
  area: evidence
  topic: Qualified compartment support
  outcome: unknown
  summary: No source pixels, raw conformation-capture data, supplemental datasets
    or whole Boisvert body inspected. No complete nuclear inventory, quantified prevalence
    or universal exact chromosome arrangement established.
  target_ids:
  - GO:0031981
  evidence_ids:
  - plaque-current-4
  - plaque-duan2010-bioc
  - plaque-duan2010-numeric
  - plaque-boisvert2007-publisher
- assessment_id: plaque-t5-identity
  area: identity
  topic: Named reticulating network and conservative ontology scope
  outcome: supported
  summary: Primary Results directly describe double-membrane strands, internal swellings
    and tunnel/peripheral-envelope continuity. GO0005622 broad parent and envelope
    parthood are appropriate; no separate sealed organelle asserted. Bounded current
    search does not turn historical589-hit survey into fresh exhaustive absence proof;0044195
    adds lamina/function scope not verified here.
  target_ids:
  - cellstructuremech:nuclear_net
  evidence_ids:
  - plaque-current-5
  - plaque-go
  - plaque-net-go-search
  - plaque-gavelis2019-body
- assessment_id: plaque-t5-material
  area: grounding
  topic: Structural membrane constituent
  outcome: supported
  summary: OTHER membrane row names a structural constituent with native0016020 identity,
    not a chemical lipid class or exact molecular composition. UNKNOWN formation necessity
    retained; primary morphology is not depletion/reconstitution evidence.
  target_ids:
  - cellstructuremech:nuclear_net
  evidence_ids:
  - plaque-current-5
  - plaque-go
  - plaque-gavelis2019-body
  - plaque-schema-policy
  - plaque-other-precedent
- assessment_id: plaque-t5-taxa
  area: scope
  topic: One reconstructed cell and complementary specimens
  outcome: supported
  summary: Taxon271679 is Polykrikos kofoidii. One wild-collected cell was reconstructed
    by FIB-SEM after high-pressure freezing/freeze substitution; TEM and confocal
    preparations were separate. Neither six tunnels nor full reticulating architecture
    is generalized as universal species/clade prevalence.
  target_ids:
  - cellstructuremech:nuclear_net
  evidence_ids:
  - plaque-current-5
  - plaque-tax271679
  - plaque-gavelis2019-body
- assessment_id: plaque-t5-image
  area: evidence
  topic: Pixel-level figure provenance and licence
  outcome: supported
  summary: Frozen image SHA matches fresh complete Fig3 bytes. All panels A-G visually
    inspected and match source caption/rendered red network, section insets and six
    numbered tunnels. SEM modality reflects FIB-SEM sections plus segmentation, not
    TEM/confocal or a live mechanism. All eight authors and CC BY4.0 permission agree;
    no separate restrictive figure credit.
  target_ids:
  - cellstructuremech:nuclear_net
  evidence_ids:
  - plaque-current-5
  - plaque-stored-image
  - plaque-gavelis2019-fig3
  - plaque-gavelis2019-body
- assessment_id: plaque-t5-mechanism
  area: graph
  topic: Molecular, dynamic and taxonomic restraint
  outcome: supported
  summary: No causal graph. Centrin proximity and tubulin-positive tunnel spindles
    are explicitly withheld as net molecular constituents; super-resolution confirmation
    remains proposed. Flow, causal assembly and division function unresolved. Primary
    double-membrane description is supported but supplementary ultrastructure not
    independently measured.
  target_ids:
  - cellstructuremech:nuclear_net
  evidence_ids:
  - plaque-current-5
  - plaque-gavelis2019-body
  - plaque-graph-rubric
- assessment_id: plaque-t5-later
  area: evidence
  topic: Later Prorocentrum study remains prospective
  outcome: supported
  summary: Kalvelage Conclusion explicitly proposes further nuclear-net work and dynamics.
    It does not independently reconstruct the Polykrikos network or identify its molecular
    inventory; no lineage-wide absence claim follows.
  target_ids:
  - cellstructuremech:nuclear_net
  evidence_ids:
  - plaque-current-5
  - plaque-kalvelage2023-meta
  - plaque-kalvelage2023-body
- assessment_id: plaque-t5-adapter
  area: evidence
  topic: Genuine morphology and topology exclusion
  outcome: not_applicable
  summary: Complete positive claims concern observed membrane architecture, preparation,
    taxon and image provenance. Centrin/tubulin, flow and mitotic machinery are discussed
    only as withheld assignments/questions. No positive molecular/pathway/stress/trait
    claim requiring module query is added merely from nearby protein names. Original
    N/A stands with this clarified rationale, not a bundle defect.
  target_ids:
  - cellstructuremech:nuclear_net
  evidence_ids:
  - plaque-current-5
  - plaque-original-5
  - plaque-policy
  - plaque-catalogue
  - plaque-gavelis2019-body
- assessment_id: plaque-t5-limits
  area: evidence
  topic: Qualified net observation
  outcome: unknown
  summary: Only maintained Fig3 pixels inspected. Other figure captions read; supplements,
    movies and raw microscopy not reanalyzed. Single reconstructed cell and multiple
    complementary fixed specimens do not establish dynamics, exact molecular composition
    or universal prevalence.
  target_ids:
  - cellstructuremech:nuclear_net
  evidence_ids:
  - plaque-current-5
  - plaque-stored-image
  - plaque-gavelis2019-body
  - plaque-kalvelage2023-body
- assessment_id: plaque-t8-identity
  area: identity
  topic: Exact nucleus and anatomical parts
  outcome: supported
  summary: GO0005634 exact identity/synonym and0043231 parent agree. Envelope/lumen/pore
    links are supported at anatomical level. Shortened generic definition does not
    explicitly claim specialized nuclei lack native exceptions; no new universal RNA-metabolism/DNA-replication
    finding inferred.
  target_ids:
  - GO:0005634
  evidence_ids:
  - plaque-current-8
  - plaque-go
  - plaque-GO0005634-isa
- assessment_id: plaque-t8-pore
  area: grounding
  topic: Exact pore protein-complex component
  outcome: supported
  summary: GO0005643 explicitly denotes NPC protein complex; type and descriptive
    exchange role agree. UNKNOWN whole-nucleus formation essentiality is distinct
    from transport function, and one protein example is not required to stand for
    the entire NPC.
  target_ids:
  - GO:0005634
  evidence_ids:
  - plaque-current-8
  - plaque-go
  - plaque-aitchison2012-jats
  - plaque-schema-policy
- assessment_id: plaque-t8-example
  area: scope
  topic: Budding-yeast nuclear contact example
  outcome: supported
  summary: Pan YEF473/L40-based association/localization evidence supports the qualitative
    yeast NV-junction example. Source direct-interaction interpretation retains its
    explicit remote-indirect caveat; current record does not assert purified binary
    reconstitution, complete machinery sufficiency or nucleus formation requirement.
    COMMON remains qualitative.
  target_ids:
  - GO:0005634
  evidence_ids:
  - plaque-current-8
  - plaque-tax4932
  - plaque-pan2000-meta
  - plaque-pan2000-pmc
- assessment_id: plaque-t8-graph
  area: graph
  topic: Four envelope and exchange edges
  outcome: supported
  summary: Envelope bounds lumen/encloses nucleus; NPC spans envelope and mediates
    nucleocytoplasmic transport. Native authority and explicitly secondary Aitchison
    support NONMECHANISTIC scope. Gating is not a literal mechanical door or a claim
    that whole transport is energy-free; no complete Nup inventory inferred.
  target_ids:
  - GO:0005634
  evidence_ids:
  - plaque-current-8
  - plaque-go
  - plaque-aitchison2012-jats
  - plaque-graph-rubric
- assessment_id: plaque-t8-F1
  area: evidence
  topic: Inherited Lu and Drubin attribution
  outcome: concern
  summary: Evidence[5].notes says Luo et al2022, but fresh metadata and genuine article
    name Michelle S Lu and David G Drubin. DOI/title and2022 volume year match; online2021
    date distinguished. Preserve exact inherited minor nucleus-lu-drubin-attribution
    finding, not a new organelle/mechanism defect.
  target_ids:
  - GO:0005634
  evidence_ids:
  - plaque-current-8
  - plaque-original-8
  - plaque-lu2022-meta
  - plaque-lu2022-pmc
- assessment_id: plaque-t8-lu-scope
  area: evidence
  topic: Observed Cdc42 localization versus proposals
  outcome: supported
  summary: Bounded Lu Results and Discussion distinguish cell-cycle-associated Nvj1/Cdc42
    localization from possible future functional roles. Maintained record only cites
    the paper bibliographically; no inferred new Cdc42 pathway is imported.
  target_ids:
  - GO:0005634
  evidence_ids:
  - plaque-current-8
  - plaque-lu2022-pmc
- assessment_id: plaque-t8-adapter
  area: evidence
  topic: Positive NPC, transport and contact proteins trigger assessment
  outcome: supported
  summary: NPC/nucleocytoplasmic transport and named Vac8p–Nvj1p interactions trigger
    native applicability despite no expression module assertion. Fresh catalogue has
    no exact Saccharomyces host; no downstream foreign-strain proxy or inferred absence.
    Correct original explicit exemption in linked review only.
  target_ids:
  - GO:0005634
  evidence_ids:
  - plaque-current-8
  - plaque-original-8
  - plaque-policy
  - plaque-catalogue
  - plaque-historical-runner
- assessment_id: plaque-t8-limits
  area: evidence
  topic: Bounded sources and optional molecular completeness
  outcome: unknown
  summary: Pan selected primary sections and Lu selected primary Results/Discussion
    inspected; Aitchison is secondary. No pixels, supplements or raw microscopy for
    these sources, no complete nuclear machinery census, and no terminal older category/neighbor
    disposition. Optional chromatin/nucleolar cohorts remain curated TODOs.
  target_ids:
  - GO:0005634
  evidence_ids:
  - plaque-current-8
  - plaque-pan2000-pmc
  - plaque-lu2022-pmc
  - plaque-aitchison2012-jats
  - plaque-rubric
- assessment_id: micro-nuclear_envelope-identity
  area: identity
  topic: Exact identity, hierarchy and boundaries
  outcome: supported
  summary: ActiveGO5635 definition and organelle-envelope ancestry match the whole
    double envelope. Nucleus parthood and distinct inner/outer/lumen/pore has_part
    relations retain topology. Native20–40nm/lamina wording is ontology-derived, not
    an independent universal yeast measurement.
  target_ids:
  - GO:0005635
  evidence_ids:
  - micro-record-nuclear_envelope
  - micro-go
  - micro-go-0005635-isa
  - micro-hetzer2010-pmc
- assessment_id: micro-nuclear_envelope-components
  area: grounding
  topic: Molecular constituents versus whole bilayer identities
  outcome: concern
  summary: Two LIPID rows use whole-membraneGO5637/5640 as molecular groundings; their
    STRUCTURE component_refs repeat the mismatch. Correct parthood is preserved. NPC
    PROTEIN_COMPLEXGO5643 remains valid.
  target_ids:
  - GO:0005635
  evidence_ids:
  - micro-record-nuclear_envelope
  - micro-component-policy
  - micro-go
- assessment_id: micro-nuclear_envelope-graph
  area: graph
  topic: Every directed edge and source-specific scope
  outcome: supported
  summary: 'All5 NONMECHANISTIC edges reviewed: inner/outerpart_of envelope; envelope
    contains lumen; NPC spans envelope and mediates transport. Topology/transport
    supported; two molecular component_ref associations remain subject to F1 grounding
    correction.'
  target_ids:
  - GO:0005635
  evidence_ids:
  - micro-record-nuclear_envelope
  - micro-go
  - micro-graph-policy
  - micro-hetzer2010-pmc
  - micro-aitchison2012-jats
- assessment_id: micro-nuclear_envelope-function
  area: scope
  topic: Function and experimental context
  outcome: supported
  summary: NPC transportGO6913 and envelopeorganizationGO6998 agree with secondary-source
    syntheses; eukaryotic occurrence and Pan yeast NVJ canonical example are bounded
    qualitative claims.
  target_ids:
  - GO:0005635
  evidence_ids:
  - micro-record-nuclear_envelope
  - micro-go
  - micro-tax4932
  - micro-tax2759
  - micro-pan2000-pmc
- assessment_id: micro-nuclear_envelope-taxon
  area: scope
  topic: Qualitative occurrence versus reference and assay strains
  outcome: supported
  summary: Species4932 and broad envelope context are correct. Primary Pan usesYEF473/L40;
    King supplement usesW303 with namedexceptions. ReviewedUniProt559292 references
    identify proteins without converting every assay intoS288C or establishing quantitative
    prevalence.
  target_ids:
  - GO:0005635
  evidence_ids:
  - micro-record-nuclear_envelope
  - micro-tax2759
  - micro-tax4932
  - micro-tax559292
  - micro-hetzer2010-pmc
  - micro-pan2000-pmc
- assessment_id: micro-nuclear_envelope-native
  area: schema
  topic: Frozen originals, deterministic rendering and exact protein coverage
  outcome: supported
  summary: All68 original input entries match retained source; all4 pairs validate/render
    exactly; owncurrenttarget unchanged. Zero examples and zero GENE_OR_PROTEIN nodes;
    NPC GO complex independently checked. Empty verifier pass is not molecular completeness.
  target_ids:
  - GO:0005635
  evidence_ids:
  - micro-prior-nuclear_envelope
  - micro-original-inputs
  - micro-original-pairs
  - micro-native-nuclear_envelope-verify
  - micro-native-nuclear_envelope-causal
  - micro-graph-policy
- assessment_id: micro-nuclear_envelope-adapter-original
  area: provenance
  topic: Original explicit applicability exclusion
  outcome: concern
  summary: 'Original exclusion exists but its expression-only rationale is insufficient:
    NPC-mediated transport and envelopeorganization positively trigger actual host
    coverage assessment. Not an omission.'
  target_ids:
  - GO:0005635
  evidence_ids:
  - micro-record-nuclear_envelope
  - micro-prior-nuclear_envelope
  - micro-policy
- assessment_id: micro-nuclear_envelope-adapter-current
  area: evidence
  topic: Current bounded host applicability
  outcome: not_applicable
  summary: Fresh official catalogue has no matching Saccharomyces/eukaryotic host
    dataset. No downstream matched-gene search or module summary is warranted. Historical
    runner failure and current successful source fallback are separate; no biological-negative
    inference.
  target_ids:
  - GO:0005635
  evidence_ids:
  - micro-record-nuclear_envelope
  - micro-catalogue
  - micro-historical-runner
  - micro-policy
- assessment_id: micro-nuclear_envelope-access
  area: evidence
  topic: Actual primary, secondary and authority access tiers
  outcome: supported
  summary: Hetzer and Aitchison are secondary reviews read at declared body sections;
    Pan is primary body read at stated Methods/Results/Discussion/captions.
  target_ids:
  - GO:0005635
  evidence_ids:
  - micro-record-nuclear_envelope
  - micro-hetzer2010-pmc
  - micro-aitchison2012-jats
  - micro-pan2000-pmc
- assessment_id: micro-nuclear_envelope-coverage
  area: completeness
  topic: Complete target and optional claims
  outcome: supported
  summary: Entire record/history/discussions/graphs/evidence read. No images, verbatim
    snippets or physical-property objects on this target require pixel/licence/measurement
    validation. StatusPROPOSED and histories remain unchanged. Optional exact lipid
    species, full protein inventory and family mappings are not automatically findings.
  target_ids:
  - GO:0005635
  evidence_ids:
  - micro-record-nuclear_envelope
  - micro-prior-nuclear_envelope
  - micro-component-policy
  - micro-policy
- assessment_id: micro-nuclear_envelope-necessity
  area: evidence
  topic: Constitutive bilayer versus molecular formation requirement
  outcome: unknown
  summary: Collective bilayer is constitutive of membrane identity. ESSENTIAL does
    not identify particular lipid species or proteins required for global membrane
    formation. Targeting/contact experiments and review-tier assembly discussion do
    not establish universal individual molecular necessity.
  target_ids:
  - GO:0005635
  evidence_ids:
  - micro-record-nuclear_envelope
  - micro-component-policy
  - micro-go
  - micro-pan2000-pmc
  - micro-hetzer2010-pmc
- assessment_id: micro-nuclear_envelope_lumen-identity
  area: identity
  topic: Exact identity, hierarchy and boundaries
  outcome: supported
  summary: ActiveGO5641 exactly denotes perinuclear space between envelope bilayers,
    not nucleoplasm. Exact synonym and organelle-envelope-lumen ancestry agree; ER-lumen
    continuity is source-supported physical topology.
  target_ids:
  - GO:0005641
  evidence_ids:
  - micro-record-nuclear_envelope_lumen
  - micro-go
  - micro-go-0005641-isa
  - micro-hetzer2010-pmc
- assessment_id: micro-nuclear_envelope_lumen-components
  area: grounding
  topic: Molecular constituents versus whole bilayer identities
  outcome: supported
  summary: No component inventory, molecular essentiality or transport mechanism is
    asserted for this volume; bounding membranes remain external topology nodes.
  target_ids:
  - GO:0005641
  evidence_ids:
  - micro-record-nuclear_envelope_lumen
  - micro-component-policy
  - micro-go
- assessment_id: micro-nuclear_envelope_lumen-graph
  area: graph
  topic: Every directed edge and source-specific scope
  outcome: supported
  summary: 'All4 NONMECHANISTIC edges reviewed: lumenpart_of envelope; inner/outer
    boundaries delimit lumen; lumen continuous withER lumen. No autonomous transport,
    resident-protein inventory or chemical composition is asserted.'
  target_ids:
  - GO:0005641
  evidence_ids:
  - micro-record-nuclear_envelope_lumen
  - micro-go
  - micro-graph-policy
  - micro-hetzer2010-pmc
- assessment_id: micro-nuclear_envelope_lumen-function
  area: scope
  topic: Function and experimental context
  outcome: supported
  summary: No functional pathway or named resident molecule is assigned; perinuclear/ER
    continuity does not by itself assert active transport.
  target_ids:
  - GO:0005641
  evidence_ids:
  - micro-record-nuclear_envelope_lumen
  - micro-go
  - micro-tax4932
  - micro-tax2759
  - micro-hetzer2010-pmc
- assessment_id: micro-nuclear_envelope_lumen-taxon
  area: scope
  topic: Qualitative occurrence versus reference and assay strains
  outcome: supported
  summary: Eukaryota2759 is correctly identified; COMMON is qualitative and not an
    intact-envelope census through every cell-cycle stage.
  target_ids:
  - GO:0005641
  evidence_ids:
  - micro-record-nuclear_envelope_lumen
  - micro-tax2759
  - micro-tax4932
  - micro-tax559292
  - micro-hetzer2010-pmc
- assessment_id: micro-nuclear_envelope_lumen-native
  area: schema
  topic: Frozen originals, deterministic rendering and exact protein coverage
  outcome: supported
  summary: All68 original input entries match retained source; all4 pairs validate/render
    exactly; owncurrenttarget unchanged. Zero examples and zero GENE_OR_PROTEIN nodes;
    this lumen asserts physical boundaries without resident proteins or transport
    machinery.
  target_ids:
  - GO:0005641
  evidence_ids:
  - micro-prior-nuclear_envelope_lumen
  - micro-original-inputs
  - micro-original-pairs
  - micro-native-nuclear_envelope_lumen-verify
  - micro-native-nuclear_envelope_lumen-causal
  - micro-graph-policy
- assessment_id: micro-nuclear_envelope_lumen-adapter-original
  area: provenance
  topic: Original explicit applicability exclusion
  outcome: supported
  summary: The lumen has no positive protein/pathway assertion; explicit sparse physical/topology
    scope warrants a genuine exclusion despite the original generic expression-only
    phrasing. No manufactured query defect.
  target_ids:
  - GO:0005641
  evidence_ids:
  - micro-record-nuclear_envelope_lumen
  - micro-prior-nuclear_envelope_lumen
  - micro-policy
- assessment_id: micro-nuclear_envelope_lumen-adapter-current
  area: evidence
  topic: Current bounded host applicability
  outcome: not_applicable
  summary: Physical/topology-only scope is a genuine exclusion. Catalogue was inspected
    for neighboring assigned molecular targets, not required to invent a lumen pathway.
  target_ids:
  - GO:0005641
  evidence_ids:
  - micro-record-nuclear_envelope_lumen
  - micro-catalogue
  - micro-historical-runner
  - micro-policy
- assessment_id: micro-nuclear_envelope_lumen-access
  area: evidence
  topic: Actual primary, secondary and authority access tiers
  outcome: supported
  summary: Hetzer is secondary review body, exact declared sections/caption; GO is
    definition/topology authority.
  target_ids:
  - GO:0005641
  evidence_ids:
  - micro-record-nuclear_envelope_lumen
  - micro-hetzer2010-pmc
- assessment_id: micro-nuclear_envelope_lumen-coverage
  area: completeness
  topic: Complete target and optional claims
  outcome: supported
  summary: Entire record/history/discussions/graphs/evidence read. No images, verbatim
    snippets or physical-property objects on this target require pixel/licence/measurement
    validation. StatusPROPOSED and histories remain unchanged. Optional exact lipid
    species, full protein inventory and family mappings are not automatically findings.
  target_ids:
  - GO:0005641
  evidence_ids:
  - micro-record-nuclear_envelope_lumen
  - micro-prior-nuclear_envelope_lumen
  - micro-component-policy
  - micro-policy
- assessment_id: micro-nuclear_inner_membrane-identity
  area: identity
  topic: Exact identity, hierarchy and boundaries
  outcome: supported
  summary: ActiveGO5637 exactly denotes the inner bilayer; native synonym, organelle-membrane
    ancestry and envelope parthood are supported. Paired outer bilayer and perinuclear
    lumen remain distinct neighboring structures.
  target_ids:
  - GO:0005637
  evidence_ids:
  - micro-record-nuclear_inner_membrane
  - micro-go
  - micro-go-0005637-isa
  - micro-hetzer2010-pmc
- assessment_id: micro-nuclear_inner_membrane-components
  area: grounding
  topic: Molecular constituents versus whole bilayer identities
  outcome: supported
  summary: Collective lipid bilayer is REVIEWED_LABEL_ONLY without a whole-structure
    GO chemical grounding. This is a permissible constitutive-material description;
    named transport/contact actors are not forced into stable membrane components.
  target_ids:
  - GO:0005637
  evidence_ids:
  - micro-record-nuclear_inner_membrane
  - micro-component-policy
  - micro-go
- assessment_id: micro-nuclear_inner_membrane-graph
  area: graph
  topic: Every directed edge and source-specific scope
  outcome: supported
  summary: 'All9 NONMECHANISTIC edges reviewed: inner membrane part_of envelope, lumen
    borders both bilayers, Kap60/Kap95 mediates targeting, process targetsINM, Heh1/Heh2
    localizeINM and are cargo of process. King experiments support this bounded yeast
    pathway; not all INM proteins universally require this route.'
  target_ids:
  - GO:0005637
  evidence_ids:
  - micro-record-nuclear_inner_membrane
  - micro-go
  - micro-graph-policy
  - micro-king2006-browser-opening
  - micro-king2006-browser-body
  - micro-king2006-supp
- assessment_id: micro-nuclear_inner_membrane-function
  area: scope
  topic: Function and experimental context
  outcome: supported
  summary: IntegralINM targeting is explicitly the source yeast Heh1/Heh2 example.
    Ran/Kap60/Kap95 dependence concerns cargo delivery, not formation of allINM material.
  target_ids:
  - GO:0005637
  evidence_ids:
  - micro-record-nuclear_inner_membrane
  - micro-go
  - micro-tax4932
  - micro-tax2759
  - micro-king2006-browser-body
  - micro-king2006-supp
- assessment_id: micro-nuclear_inner_membrane-taxon
  area: scope
  topic: Qualitative occurrence versus reference and assay strains
  outcome: supported
  summary: Species4932 and broad envelope context are correct. Primary Pan usesYEF473/L40;
    King supplement usesW303 with namedexceptions. ReviewedUniProt559292 references
    identify proteins without converting every assay intoS288C or establishing quantitative
    prevalence.
  target_ids:
  - GO:0005637
  evidence_ids:
  - micro-record-nuclear_inner_membrane
  - micro-tax2759
  - micro-tax4932
  - micro-tax559292
  - micro-hetzer2010-pmc
  - micro-king2006-supp
- assessment_id: micro-nuclear_inner_membrane-native
  area: schema
  topic: Frozen originals, deterministic rendering and exact protein coverage
  outcome: supported
  summary: All68 original input entries match retained source; all4 pairs validate/render
    exactly; owncurrenttarget unchanged. Zero examples, three UNANCHORED_WITH_UNIPROT
    nodes with Q02821/Q03707/Q03281. Q02821 verifies only Kap60 within the named Kap60/Kap95
    system, not complete pair coverage.
  target_ids:
  - GO:0005637
  evidence_ids:
  - micro-prior-nuclear_inner_membrane
  - micro-original-inputs
  - micro-original-pairs
  - micro-native-nuclear_inner_membrane-verify
  - micro-native-nuclear_inner_membrane-causal
  - micro-graph-policy
- assessment_id: micro-nuclear_inner_membrane-adapter-original
  area: provenance
  topic: Original explicit applicability exclusion
  outcome: concern
  summary: 'Original exclusion exists but its expression-only rationale is insufficient:
    named Heh1/Heh2/Kap60/Kap95 targeting positively trigger actual host coverage
    assessment. Not an omission.'
  target_ids:
  - GO:0005637
  evidence_ids:
  - micro-record-nuclear_inner_membrane
  - micro-prior-nuclear_inner_membrane
  - micro-policy
- assessment_id: micro-nuclear_inner_membrane-adapter-current
  area: evidence
  topic: Current bounded host applicability
  outcome: not_applicable
  summary: Fresh official catalogue has no matching Saccharomyces/eukaryotic host
    dataset. No downstream matched-gene search or module summary is warranted. Historical
    runner failure and current successful source fallback are separate; no biological-negative
    inference.
  target_ids:
  - GO:0005637
  evidence_ids:
  - micro-record-nuclear_inner_membrane
  - micro-catalogue
  - micro-historical-runner
  - micro-policy
- assessment_id: micro-nuclear_inner_membrane-access
  area: evidence
  topic: Actual primary, secondary and authority access tiers
  outcome: supported
  summary: King primary author-uploaded browser excerpts plus genuine publisher supplement
    inspected. Main-PDF URL yielded HTML, not PDF; no pixels, unread body lines or
    independent new assay claimed.
  target_ids:
  - GO:0005637
  evidence_ids:
  - micro-record-nuclear_inner_membrane
  - micro-hetzer2010-pmc
  - micro-king2006-browser-opening
  - micro-king2006-browser-body
  - micro-king2006-supp
  - micro-king2006-main-access
- assessment_id: micro-nuclear_inner_membrane-coverage
  area: completeness
  topic: Complete target and optional claims
  outcome: supported
  summary: Entire record/history/discussions/graphs/evidence read. No images, verbatim
    snippets or physical-property objects on this target require pixel/licence/measurement
    validation. StatusPROPOSED and histories remain unchanged. Optional exact lipid
    species, full protein inventory and family mappings are not automatically findings.
  target_ids:
  - GO:0005637
  evidence_ids:
  - micro-record-nuclear_inner_membrane
  - micro-prior-nuclear_inner_membrane
  - micro-component-policy
  - micro-policy
- assessment_id: micro-nuclear_inner_membrane-necessity
  area: evidence
  topic: Constitutive bilayer versus molecular formation requirement
  outcome: unknown
  summary: Collective bilayer is constitutive of membrane identity. ESSENTIAL does
    not identify particular lipid species or proteins required for global membrane
    formation. Targeting/contact experiments and review-tier assembly discussion do
    not establish universal individual molecular necessity.
  target_ids:
  - GO:0005637
  evidence_ids:
  - micro-record-nuclear_inner_membrane
  - micro-component-policy
  - micro-go
  - micro-pan2000-pmc
  - micro-hetzer2010-pmc
- assessment_id: micro-nuclear_inner_membrane-proteins
  area: grounding
  topic: Exact current reference proteins and bounded family checks
  outcome: supported
  summary: Zero examples, three UNANCHORED_WITH_UNIPROT nodes with Q02821/Q03707/Q03281.
    Q02821 verifies only Kap60 within the named Kap60/Kap95 system, not complete pair
    coverage. All accessions are reviewedS288C; primary names/synonyms/loci checked.
    InterPro exact-association responses distinguish family/domain/repeat; P38881
    HTTP204 is bounded nonreturn, not universal family absence.
  target_ids:
  - GO:0005637
  evidence_ids:
  - micro-record-nuclear_inner_membrane
  - micro-tax559292
  - micro-component-policy
  - micro-protein-Q02821
  - micro-protein-Q03707
  - micro-protein-Q03281
  - micro-family-Q02821
  - micro-family-Q03707
  - micro-family-Q03281
- assessment_id: micro-nuclear_inner_membrane-discussion-disposition
  area: provenance
  topic: Reject inherited rationale-only finding under native history policy
  outcome: supported
  summary: The September rationale is historical provenance. Current prompt still
    requests source-neutral grounding, which instance xrefs do not complete; October18
    history explicitly records added xrefs. No material record defect is established
    by absence of an optional current-state note. Preserve original rationale and
    validOPEN family task; reject exact inherited minorF1, not resolve a nonexistent
    record fix or close a wider category finding.
  target_ids:
  - GO:0005637
  evidence_ids:
  - micro-record-nuclear_inner_membrane
  - micro-prior-nuclear_inner_membrane
  - micro-discussion-policy
  - micro-component-policy
  - micro-protein-Q02821
  - micro-protein-Q03707
  - micro-protein-Q03281
- assessment_id: micro-nuclear_outer_membrane-identity
  area: identity
  topic: Exact identity, hierarchy and boundaries
  outcome: supported
  summary: ActiveGO5640 exactly denotes the cytoplasm-facing outer bilayer; native
    definition supports ER continuity and organelle-membrane ancestry. The source
    yeast NVJ example does not change record identity into a junction.
  target_ids:
  - GO:0005640
  evidence_ids:
  - micro-record-nuclear_outer_membrane
  - micro-go
  - micro-go-0005640-isa
  - micro-hetzer2010-pmc
- assessment_id: micro-nuclear_outer_membrane-components
  area: grounding
  topic: Molecular constituents versus whole bilayer identities
  outcome: supported
  summary: Collective lipid bilayer is REVIEWED_LABEL_ONLY without a whole-structure
    GO chemical grounding. This is a permissible constitutive-material description;
    named transport/contact actors are not forced into stable membrane components.
  target_ids:
  - GO:0005640
  evidence_ids:
  - micro-record-nuclear_outer_membrane
  - micro-component-policy
  - micro-go
- assessment_id: micro-nuclear_outer_membrane-graph
  area: graph
  topic: Every directed edge and source-specific scope
  outcome: supported
  summary: 'All6 NONMECHANISTIC edges reviewed: outerpart_of envelope, lumen borders
    outer/inner bilayers, Nvj1 localizesONM, Vac8 localizesvacuolar membrane, and
    the pair interacts. Pan interprets direct interaction with an explicit remote
    indirect possibility; no minimal purified reconstitution or entire membrane assembly
    claim.'
  target_ids:
  - GO:0005640
  evidence_ids:
  - micro-record-nuclear_outer_membrane
  - micro-go
  - micro-graph-policy
  - micro-pan2000-pmc
- assessment_id: micro-nuclear_outer_membrane-function
  area: scope
  topic: Function and experimental context
  outcome: supported
  summary: NVJ formation is specifically the budding-yeast Nvj1/Vac8 contact process;
    source manipulation supports that contact, not assembly of the entireONM.
  target_ids:
  - GO:0005640
  evidence_ids:
  - micro-record-nuclear_outer_membrane
  - micro-go
  - micro-tax4932
  - micro-tax2759
  - micro-pan2000-pmc
- assessment_id: micro-nuclear_outer_membrane-taxon
  area: scope
  topic: Qualitative occurrence versus reference and assay strains
  outcome: supported
  summary: Species4932 and broad envelope context are correct. Primary Pan usesYEF473/L40;
    King supplement usesW303 with namedexceptions. ReviewedUniProt559292 references
    identify proteins without converting every assay intoS288C or establishing quantitative
    prevalence.
  target_ids:
  - GO:0005640
  evidence_ids:
  - micro-record-nuclear_outer_membrane
  - micro-tax2759
  - micro-tax4932
  - micro-tax559292
  - micro-hetzer2010-pmc
  - micro-pan2000-pmc
- assessment_id: micro-nuclear_outer_membrane-native
  area: schema
  topic: Frozen originals, deterministic rendering and exact protein coverage
  outcome: supported
  summary: All68 original input entries match retained source; all4 pairs validate/render
    exactly; owncurrenttarget unchanged. Zero examples, two UNANCHORED_WITH_UNIPROT
    nodes with P38881/P39968; permissible node xrefs independently checked, not source-neutral
    family grounding.
  target_ids:
  - GO:0005640
  evidence_ids:
  - micro-prior-nuclear_outer_membrane
  - micro-original-inputs
  - micro-original-pairs
  - micro-native-nuclear_outer_membrane-verify
  - micro-native-nuclear_outer_membrane-causal
  - micro-graph-policy
- assessment_id: micro-nuclear_outer_membrane-adapter-original
  area: provenance
  topic: Original explicit applicability exclusion
  outcome: concern
  summary: 'Original exclusion exists but its expression-only rationale is insufficient:
    named Nvj1/Vac8 contact formation positively trigger actual host coverage assessment.
    Not an omission.'
  target_ids:
  - GO:0005640
  evidence_ids:
  - micro-record-nuclear_outer_membrane
  - micro-prior-nuclear_outer_membrane
  - micro-policy
- assessment_id: micro-nuclear_outer_membrane-adapter-current
  area: evidence
  topic: Current bounded host applicability
  outcome: not_applicable
  summary: Fresh official catalogue has no matching Saccharomyces/eukaryotic host
    dataset. No downstream matched-gene search or module summary is warranted. Historical
    runner failure and current successful source fallback are separate; no biological-negative
    inference.
  target_ids:
  - GO:0005640
  evidence_ids:
  - micro-record-nuclear_outer_membrane
  - micro-catalogue
  - micro-historical-runner
  - micro-policy
- assessment_id: micro-nuclear_outer_membrane-access
  area: evidence
  topic: Actual primary, secondary and authority access tiers
  outcome: supported
  summary: Pan genuine primary body read at Methods3-6,9; Results11-17; Discussion18-20/captions.
    Direct-interaction qualification retained; nativeUniProt andInterPro are authority
    context.
  target_ids:
  - GO:0005640
  evidence_ids:
  - micro-record-nuclear_outer_membrane
  - micro-hetzer2010-pmc
  - micro-pan2000-pmc
- assessment_id: micro-nuclear_outer_membrane-coverage
  area: completeness
  topic: Complete target and optional claims
  outcome: supported
  summary: Entire record/history/discussions/graphs/evidence read. No images, verbatim
    snippets or physical-property objects on this target require pixel/licence/measurement
    validation. StatusPROPOSED and histories remain unchanged. Optional exact lipid
    species, full protein inventory and family mappings are not automatically findings.
  target_ids:
  - GO:0005640
  evidence_ids:
  - micro-record-nuclear_outer_membrane
  - micro-prior-nuclear_outer_membrane
  - micro-component-policy
  - micro-policy
- assessment_id: micro-nuclear_outer_membrane-necessity
  area: evidence
  topic: Constitutive bilayer versus molecular formation requirement
  outcome: unknown
  summary: Collective bilayer is constitutive of membrane identity. ESSENTIAL does
    not identify particular lipid species or proteins required for global membrane
    formation. Targeting/contact experiments and review-tier assembly discussion do
    not establish universal individual molecular necessity.
  target_ids:
  - GO:0005640
  evidence_ids:
  - micro-record-nuclear_outer_membrane
  - micro-component-policy
  - micro-go
  - micro-pan2000-pmc
  - micro-hetzer2010-pmc
- assessment_id: micro-nuclear_outer_membrane-proteins
  area: grounding
  topic: Exact current reference proteins and bounded family checks
  outcome: supported
  summary: Zero examples, two UNANCHORED_WITH_UNIPROT nodes with P38881/P39968; permissible
    node xrefs independently checked, not source-neutral family grounding. All accessions
    are reviewedS288C; primary names/synonyms/loci checked. InterPro exact-association
    responses distinguish family/domain/repeat; P38881 HTTP204 is bounded nonreturn,
    not universal family absence.
  target_ids:
  - GO:0005640
  evidence_ids:
  - micro-record-nuclear_outer_membrane
  - micro-tax559292
  - micro-component-policy
  - micro-protein-P38881
  - micro-protein-P39968
  - micro-family-P38881
  - micro-family-P39968
- assessment_id: micro-nuclear_outer_membrane-discussion-disposition
  area: provenance
  topic: Reject inherited rationale-only finding under native history policy
  outcome: supported
  summary: The September rationale is historical provenance. Current prompt still
    requests source-neutral grounding, which instance xrefs do not complete; October18
    history explicitly records added xrefs. No material record defect is established
    by absence of an optional current-state note. Preserve original rationale and
    validOPEN family task; reject exact inherited minorF1, not resolve a nonexistent
    record fix or close a wider category finding.
  target_ids:
  - GO:0005640
  evidence_ids:
  - micro-record-nuclear_outer_membrane
  - micro-prior-nuclear_outer_membrane
  - micro-discussion-policy
  - micro-component-policy
  - micro-protein-P38881
  - micro-protein-P39968
- assessment_id: current-input-comparison
  area: provenance
  topic: Complete frozen-input comparison and bounded refresh
  outcome: supported
  summary: 1 of ten original target hashes differ from current main. The changed content
    is substantively reassessed in the target-specific assessments; original observations
    remain historical and unchanged. All current target and used context bytes are
    frozen.
  target_ids:
  - cellstructuremech:nitroplast
  - GO:0005635
  - GO:0005641
  - GO:0005637
  - GO:0031981
  - cellstructuremech:nuclear_net
  - GO:0005640
  - GO:0033009
  - GO:0005634
  - GO:0070111
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
- finding_id: septin-organellar_chromatophore-F1
  issue_key: organellar-chromatophore-membrane-lipid-grounding
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Separate whole membrane parts from molecular lipid components
  description: Components0–2 are typed LIPID but their labels and GO0070114/13/18
    groundings identify entire anatomical membranes. These identities are valid structural
    parts, not lipid entities. The corresponding structural graph nodes also carry
    component_ref links to those misclassified molecular rows.
  target_ids:
  - GO:0070111
  field_paths:
  - components[0].component_type
  - components[0].grounding
  - components[1].component_type
  - components[1].grounding
  - components[2].component_type
  - components[2].grounding
  - causal_graphs[0].nodes[1].component_ref
  - causal_graphs[0].nodes[2].component_ref
  - causal_graphs[0].nodes[4].component_ref
  evidence_ids:
  - septin-record-organellar_chromatophore
  - septin-original-organellar_chromatophore
  - septin-go
  - septin-SL0351
  - septin-schema-policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/organellar_chromatophore.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:component grounding; StructuralComponent
  native_severity: major
  normalization_reason: Major wrong molecular grounding/type across three components,
    propagated through graph joins; correct anatomical parthood is preserved and not
    rejected.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T025111Z-organellar-chromatophore-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2753
- finding_id: septin-organellar_chromatophore-F2
  issue_key: organellar-chromatophore-thylakoid-go-source-overstatement
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Attach the light-reaction complex claim to its primary evidence
  description: The component and graph source notes say GO0070118 defines an internal
    photosynthetic membrane system carrying light-reaction complexes. Its actual definition
    only identifies the thylakoid lipid-bilayer membrane. The inspected Nowack2012
    Results directly support thylakoid-associated PSI proteins and provide the appropriate
    experimental source.
  target_ids:
  - GO:0070111
  field_paths:
  - components[2].evidence[0].notes
  - causal_graphs[0].edges[3].evidence[0].notes
  evidence_ids:
  - septin-record-organellar_chromatophore
  - septin-original-organellar_chromatophore
  - septin-go
  - septin-nowack2012-prefixed
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/organellar_chromatophore.yaml
    role: maintained scientific record
  rule_id: .claude/skills/review-yaml-record/SKILL.md:narrowest source claim
  native_severity: minor
  normalization_reason: Minor source-attribution overstatement because the biological
    assertion itself is supported by an already-cited primary study; no false photosynthesis
    mechanism is alleged.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T025111Z-organellar-chromatophore-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2754
- finding_id: plaque-t8-F1
  issue_key: nucleus-lu-drubin-attribution
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Correct the Lu and Drubin citation attribution
  description: evidence[5].notes attributes DOI10.1080/21541248.2021.1993714 to Luo
    et al2022. Both native MED metadata and the primary article identify Michelle
    S Lu and David G Drubin as its two authors. The DOI, title and2022 volume year
    otherwise match.
  target_ids:
  - GO:0005634
  field_paths:
  - evidence[5].notes
  evidence_ids:
  - plaque-current-8
  - plaque-original-8
  - plaque-lu2022-meta
  - plaque-lu2022-pmc
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/nucleus.yaml
    role: maintained scientific record
  rule_id: .claude/skills/review-yaml-record/SKILL.md:exact source identity
  native_severity: minor
  normalization_reason: Minor bounded bibliographic attribution correction; organelle
    identity and cited biological scope remain sound.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T025110Z-nucleus-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2751
- finding_id: micro-F1
  issue_key: nuclear-envelope-whole-membranes-as-lipid-groundings
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Separate whole membrane parts from molecular lipid groundings
  description: The inner and outer membrane components are typed LIPID but grounded
    to whole cellular-component identities GO0005637 and GO0005640. The schema requires
    molecular lipid grounding; these GO entries denote complete bilayers containing
    more than the lipid identity. The linked STRUCTURE nodes repeat the same mismatch
    through component_ref. Correct has_part and topology assertions remain valid.
  target_ids:
  - GO:0005635
  field_paths:
  - components[0].component_type
  - components[0].grounding
  - components[1].component_type
  - components[1].grounding
  - causal_graphs[0].nodes[1].component_ref
  - causal_graphs[0].nodes[2].component_ref
  evidence_ids:
  - micro-record-nuclear_envelope
  - micro-go
  - micro-component-policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/nuclear_envelope.yaml
    role: maintained scientific record
  rule_id: StructuralComponent.grounding and ComponentTypeEnum
  native_severity: major
  normalization_reason: A concrete chemical-category/whole-structure identity mismatch
    materially corrupts component groundings. The envelope concept and parthood are
    correct, so this is not a blocker or a finding against accurate OTHER structural
    constituents.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T025105Z-nuclear-envelope-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2752
- finding_id: micro-F2
  issue_key: nuclear-inner-membrane-stale-protein-grounding-rationale
  category: provenance
  severity: minor
  status: rejected
  certainty: confirmed
  title: Update the open protein-grounding rationale to acknowledge verified xrefs
  description: The rationale says the named protein nodes are left ungrounded until
    exact UniProt or family identifiers can be verified. Current graph nodes already
    carry verified accessions, and the October curation event records their addition.
    The remaining task needs to distinguish completed instance verification from any
    unresolved family or grouped-actor coverage.
  target_ids:
  - GO:0005637
  field_paths:
  - discussions[1].rationale
  - discussions[1].status
  evidence_ids:
  - micro-record-nuclear_inner_membrane
  - micro-prior-nuclear_inner_membrane
  - micro-discussion-policy
  - micro-component-policy
  - micro-protein-Q02821
  - micro-protein-Q03707
  - micro-protein-Q03281
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/nuclear_inner_membrane.yaml
    role: maintained scientific record
  rule_id: Evidence placement and current discussion provenance
  native_severity: minor
  normalization_reason: Original minor severity is retained to identify the historical
    finding; the current evidence-backed disposition rejects its claimed defect. No
    optional current-state annotation or unresolved family mapping is promoted into
    a new finding.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T025106Z-nuclear-inner-membrane-audit
    finding_id: F1
  disposition_reason: The original minor finding treated a dated historical rationale
    as an inaccurate current task description. Native CURATION says discussions are
    provenance, rationale is appended to and never replaced, and notes hold current
    state. The current prompt still asks for source-neutral grounding; organism-specific
    UniProt xrefs do not complete that family-level task. The October18 curation history
    explicitly records instance-xref additions. No material erroneous current assertion
    or required missing representation is established merely because the September
    rationale is unchanged. Optional appended progress notes can help, but do not
    justify mandatory record curation. Original action also said preserve historical
    context; this rejection does not falsely characterize it as an explicit order
    to erase history.
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2750
- finding_id: micro-F3
  issue_key: nuclear-outer-membrane-stale-protein-grounding-rationale
  category: provenance
  severity: minor
  status: rejected
  certainty: confirmed
  title: Update the open protein-grounding rationale to acknowledge verified xrefs
  description: The rationale says the named protein nodes are left ungrounded until
    exact UniProt or family identifiers can be verified. Current graph nodes already
    carry verified accessions, and the October curation event records their addition.
    The remaining task needs to distinguish completed instance verification from any
    unresolved family or grouped-actor coverage.
  target_ids:
  - GO:0005640
  field_paths:
  - discussions[1].rationale
  - discussions[1].status
  evidence_ids:
  - micro-record-nuclear_outer_membrane
  - micro-prior-nuclear_outer_membrane
  - micro-discussion-policy
  - micro-component-policy
  - micro-protein-P38881
  - micro-protein-P39968
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/nuclear_outer_membrane.yaml
    role: maintained scientific record
  rule_id: Evidence placement and current discussion provenance
  native_severity: minor
  normalization_reason: Original minor severity is retained to identify the historical
    finding; the current evidence-backed disposition rejects its claimed defect. No
    optional current-state annotation or unresolved family mapping is promoted into
    a new finding.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T025109Z-nuclear-outer-membrane-audit
    finding_id: F1
  disposition_reason: The original minor finding treated a dated historical rationale
    as an inaccurate current task description. Native CURATION says discussions are
    provenance, rationale is appended to and never replaced, and notes hold current
    state. The current prompt still asks for source-neutral grounding; organism-specific
    UniProt xrefs do not complete that family-level task. The October18 curation history
    explicitly records instance-xref additions. No material erroneous current assertion
    or required missing representation is established merely because the September
    rationale is unchanged. Optional appended progress notes can help, but do not
    justify mandatory record curation. Original action also said preserve historical
    context; this rejection does not falsely characterize it as an explicit order
    to erase history.
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2750
actions:
- action_id: septin-organellar_chromatophore-A1
  finding_ids:
  - septin-organellar_chromatophore-F1
  target_ids:
  - GO:0070111
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/organellar_chromatophore.yaml
    role: maintained scientific record
  description: Preserve supported membrane parts/topology. Represent whole structural
    constituents with an appropriate structural type if retained, or model supported
    lipid materials separately with exact chemical grounding or justified reviewed-label-only
    status; align graph component_ref joins to that distinction.
  acceptance_checks:
  - Verify each LIPID row denotes a molecular lipid/material identity rather than
    a GO membrane location.
  - Run focused schema, strict and graph checks after separately authorized curation.
- action_id: septin-organellar_chromatophore-A2
  finding_ids:
  - septin-organellar_chromatophore-F2
  target_ids:
  - GO:0070111
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/organellar_chromatophore.yaml
    role: maintained scientific record
  description: Restrict the GO note to the compartment definition and attach the relevant
    primary localization/PSI evidence to the light-complex statement.
  acceptance_checks:
  - Re-read GO0070118 definition and Nowack2012 Results sec2–4.
  - Ensure the updated evidence note states only what its cited source establishes.
- action_id: plaque-t8-A1
  finding_ids:
  - plaque-t8-F1
  target_ids:
  - GO:0005634
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/nucleus.yaml
    role: maintained scientific record
  description: Correct the evidence note to Lu and Drubin(2022), retaining the verified
    DOI/title and treating the article functional proposals as proposals.
  acceptance_checks:
  - Verify exact authors/title/DOI against the native source.
  - After separately authorized curation, run the focused schema and strict validation
    recipes.
- action_id: micro-A1
  finding_ids:
  - micro-F1
  target_ids:
  - GO:0005635
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/nuclear_envelope.yaml
    role: maintained scientific record
  description: 'In separately authorized curation, retain correct inner/outer has_part
    links and graph topology while correcting the component representation: represent
    structural parts with a scientifically accurate permitted type, or represent molecular
    lipid material with verified chemical grounding or candid label-only status. Reconcile
    component_ref links with the chosen scope and retain the valid pore complex. Do
    not invent a lipid species or change membrane identity.'
  acceptance_checks:
  - Neither LIPID row uses an identifier that denotes the entire nuclear membrane.
  - Inner/outer parthood, lumen boundaries and NPC topology are preserved; each component_ref
    matches the intended component scope.
  - Native schema, strict, product, identifier, graph and history gates pass after
    authorized curation.
- action_id: micro-A2
  finding_ids:
  - micro-F2
  target_ids:
  - GO:0005637
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: reviews/structured/20261022T025106Z-nuclear-inner-membrane-audit/review.yaml
    role: immutable historical review; correction belongs in linked successor
  description: Correct the review disposition with exact predecessor lineage; preserve
    the immutable original and unchanged scientific record. Do not mandate replacing
    historical rationale or closing a still-valid source-neutral grounding task. Optional
    current-state notes remain separately discretionary.
  acceptance_checks:
  - Successor records rejected status and evidence-backed disposition for this exact
    original F1/key.
  - No scientific record, historical rationale, original bundle or valid UniProt xref
    is changed as this review remedy.
  - Any optional later discussion update preserves rationale and posed_date and separates
    instance verification from family grounding.
- action_id: micro-A3
  finding_ids:
  - micro-F3
  target_ids:
  - GO:0005640
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: reviews/structured/20261022T025109Z-nuclear-outer-membrane-audit/review.yaml
    role: immutable historical review; correction belongs in linked successor
  description: Correct the review disposition with exact predecessor lineage; preserve
    the immutable original and unchanged scientific record. Do not mandate replacing
    historical rationale or closing a still-valid source-neutral grounding task. Optional
    current-state notes remain separately discretionary.
  acceptance_checks:
  - Successor records rejected status and evidence-backed disposition for this exact
    original F1/key.
  - No scientific record, historical rationale, original bundle or valid UniProt xref
    is changed as this review remedy.
  - Any optional later discussion update preserves rationale and posed_date and separates
    instance verification from family grounding.
limitations:
- 'Nitroplast, nucleomorph and organellar chromatophore independent subreview: Read-only
  independent source review of three assigned targets; root owns issue dedup/publication
  and global gates. No repository/record/GitHub mutation and no certification of later
  saved-head, CI or queue.'
- 'Nitroplast, nucleomorph and organellar chromatophore independent subreview: Two
  original inputs are unchanged; chromatophore changed only by a parthood edge and
  historical curation event. Original historical source hashes/native schema/render
  were verified separately from frozen current bytes, and the complete current record
  was reassessed.'
- 'Nitroplast, nucleomorph and organellar chromatophore independent subreview: All
  substantive source snapshots used here were freshly fetched with actual receipts.
  Initial publisher/PMC HTTP200 challenge bodies and later failed XML requests are
  explicitly not treated as full text. Subsequent genuine Nowack PMC and Tanifuji/Onuma/Li
  XML are separately scoped; no cached historical body is silently relabeled fresh.'
- 'Nitroplast, nucleomorph and organellar chromatophore independent subreview: Coale
  primary article page text is a public manuscript/article-page representation, not
  platform-generated summary prose; read pages1,3,4,5 and supplement2,7,11. Figure
  captions are text access, not raw image/pixel quantification; FigS3 only caption
  was inspected. Predicted uTP candidates remain distinct from enriched proteins.'
- 'Nitroplast, nucleomorph and organellar chromatophore independent subreview: Hagino
  genuine PDF sections and actual rendered cover/Table2/Fig28–31 pixels were inspected.
  FR21 panels28/29 are distinguished from OTR22-B panels30/31; copyright checked on
  article first page PDF2. Linked OTHER is not a redistribution licence. Culture-specific
  loss is not wild prevalence or a proven causal mechanism.'
- 'Nitroplast, nucleomorph and organellar chromatophore independent subreview: Curtis2012
  and Singer2017 are complete primary abstracts plus verified metadata, not full bodies.
  Nowack2014 and Gabr2020 are secondary abstracts. Unread source details remain uncertain;
  access limitation does not refute their science.'
- 'Nitroplast, nucleomorph and organellar chromatophore independent subreview: Tanifuji
  and Onuma were read at stated body sections/captions/Methods only. No raw sequence,
  supplementary datasets, figure pixels or quantitative reanalysis. L.oceanica chromosomeI
  repeat uncertainty and partial G.theta synchronization limit extrapolation.'
- 'Nitroplast, nucleomorph and organellar chromatophore independent subreview: Li2026
  XML identifies version1 preprint; only stated Discussion/limitations and front metadata
  were read. No proof of vesicle cargo/direction, transporter identity, gating causality
  or density composition is inferred.'
- 'Nitroplast, nucleomorph and organellar chromatophore independent subreview: Native
  six protein commands pass on zero examples, zero typed molecular nodes and zero
  UniProt graph xrefs. This empty represented coverage does not validate all narrative
  molecular claims, composition completeness or formation necessity.'
- 'Nitroplast, nucleomorph and organellar chromatophore independent subreview: Fresh
  full catalogue has20organisms/28organism-dataset pairs/22distinct strings and no
  matched named host/endosymbiont. Synechococcus elongatus is not an interchangeable
  cyanobacterial organelle proxy. All three full-record molecular scopes trigger applicability
  assessment; downstream calls are N/A for lack of matched coverage, not biological
  absence. Historical00:49Z runner failure is not a fresh invocation.'
- 'Nitroplast, nucleomorph and organellar chromatophore independent subreview: Two
  exact chromatophore findings/actions preserve original severity, stable keys and
  repository/review/finding lineage. No new scientific finding. Nitroplast structural
  OTHER is supported by the native schema/test; nucleomorph collective DNA essentiality
  is not mistaken for a measured individual formation requirement.'
- 'Nitroplast, nucleomorph and organellar chromatophore independent subreview: All29
  actually used local repository inputs were frozen before use:17 common policies/scripts/schema,3targets,6original
  artifacts,2boundary neighbors and1structural-type test. Neighbor findings, prior
  grouped/category issues and historical curation dispositions are not resolved by
  this review.'
- 'Nuclear lumen, nuclear net and nucleus independent subreview: All three targets
  unchanged; nuclear lumen and nuclear net remain pass_with_limitations, nucleus needs_curation
  only for inherited minor nucleus-lu-drubin-attribution. No new scientific finding.'
- 'Nuclear lumen, nuclear net and nucleus independent subreview: Original native validation/exact
  rendering and13/14/12 historical frozen input hashes match. No records/originals
  edited; old history mentions and historical589-result ontology survey are not freshly
  exhaustive or terminally re-adjudicated.'
- 'Nuclear lumen, nuclear net and nucleus independent subreview: Duan primary model
  is population-based BY4741-derived conformation capture, not all-cell/all-eukaryote
  topology. Selected BioC passages, matching numeric PMC Methods Summary and Fig5
  caption read; no pixels/supplements/raw contact matrices. Original canonical fetch
  returned recaptcha, not usable body.'
- 'Nuclear lumen, nuclear net and nucleus independent subreview: Boisvert secondary
  review is complete abstract and publisher Key Points only; full main article is
  paywalled and not claimed read. Aitchison secondary review is limited to opening
  body/s2/s3/first3s14 paragraphs, not a cited-primary assay audit.'
- 'Nuclear lumen, nuclear net and nucleus independent subreview: Gavelis main Introduction/Results/Discussion/Conclusion/Methods
  and Fig1–5 captions read; only maintained Fig3 pixels inspected. Primary Results
  describe double membranes using supplementary evidence not independently viewed,
  so no new bilayer measurement. One reconstructed wild specimen plus four TEM/eight
  confocal specimens do not establish universal count, dynamics, molecular inventory
  or prevalence.'
- 'Nuclear lumen, nuclear net and nucleus independent subreview: Fresh Fig3 bytes
  equal stored SHA; source permission is CC BY4.0, eight author attribution and caption/modality
  agree. No restrictive separate Fig3 credit. Rendered topology does not establish
  flow, centrin incorporation or a division mechanism.'
- 'Nuclear lumen, nuclear net and nucleus independent subreview: Kalvelage complete
  Conclusion and native abstract only; future nuclear-net work remains prospective.
  Current bounded QuickGO first100/589-result query is not exhaustive absence proof;
  historical full search remains historical.'
- 'Nuclear lumen, nuclear net and nucleus independent subreview: Pan shared fresh
  body independently reread Methods3/Results11,13,15/Discussion19 with included captions.
  Direct interaction is the paper interpretation of two-hybrid/copurification with
  a remote indirect caveat, not purified binary reconstitution. Lu genuine body metadata/Results
  s0002-s2002/Discussion s0003 and Fig2/5 captions read; other Results/pixels/movies
  not claimed.'
- 'Nuclear lumen, nuclear net and nucleus independent subreview: All six actual native
  protein commands pass on zero examples/zero typed nodes. This does not validate
  narrative protein/pathway claims; GO-grounded NPC structural actor is checked manually.
  OTHER structural components and permitted complex node types are not automatic enum
  or chemical defects.'
- 'Nuclear lumen, nuclear net and nucleus independent subreview: Lumen/nucleus explicit
  no-expression exclusions require correction from actual positive claims. Nuclear
  net is a genuine morphology/topology exclusion with molecular actors expressly withheld.
  Fresh full catalogue has no exact eukaryotic host; no downstream query or foreign
  proxy, and no negative biology. Historical00:49Z runner failure remains historical
  unavailable.'
- 'Nuclear lumen, nuclear net and nucleus independent subreview: Root owns global
  QC, issue publication, successor writing, final CI and merge. This source report
  only binds independent current assessment and scratch native preflight; no future
  gate certification.'
- 'Nuclear envelope and three boundary compartment independent subreview: Four complete
  unchanged nuclear-envelope targets independently reassessed. One inherited major
  molecular-grounding finding remains open; two inherited minor rationale-only findings
  are rejected with exact predecessor lineage under native discussion-provenance policy.
  No new scientific finding, record edit or broader issue/category disposition.'
- 'Nuclear envelope and three boundary compartment independent subreview: Hetzer2010
  and Aitchison2012 are secondary reviews, not direct primary experiments. Their exact
  declared body sections/captions were inspected; no pixels or unlisted sections certified.
  Native GO20–40nm/lamina wording is ontology-derived; it is not a universal source-specific
  measurement or universal yeast lamina statement.'
- 'Nuclear envelope and three boundary compartment independent subreview: Pan2000
  primary body scope is Methods3-6,9; Results11-17; Discussion18-20 and embedded captions.
  Two-hybrid/copurification/contact perturbations support authors direct-interaction
  interpretation with their explicit remote indirect-binding caveat. Assays useYEF473/L40
  backgrounds, not automaticallyS288C. No entire-membrane formation requirement inferred.'
- 'Nuclear envelope and three boundary compartment independent subreview: King2006
  main-PDF URL returnedHTML preview and pdftotext rejected it. Current author-uploaded
  browser excerpts cover stated results/discussion/methods passages; separate genuine
  publisher supplement provides captions/Methods/Tables includingW303/namedexceptions.
  No native full main-PDF recovery, image pixels or unshown browser lines certified.
  No universal INM targeting mechanism inferred.'
- 'Nuclear envelope and three boundary compartment independent subreview: Five current
  reviewedUniProt references support exact names/synonyms/loci/taxa. Nativeinner3
  andouter2 UNANCHORED_WITH_UNIPROT are permissible xref coverage; other2 targets
  zero examples/nodes. RepresentativeKap60 does not identifyKap95. Protein instances,
  source-neutral families, localization and formation necessity remain distinct.'
- 'Nuclear envelope and three boundary compartment independent subreview: InterPro
  association requests are bounded to five exact protein accessions, page_size200;
  four complete returned lists, oneP38881HTTP204. No universal family absence, automatic
  groundings or mandatory new inventory inferred.'
- 'Nuclear envelope and three boundary compartment independent subreview: Wholeenvelope/inner/outer
  original explicit expression-only exclusions need corrected actual-host assessment;
  lumen is a genuine physical/topology exclusion. Fresh official catalogue has no
  matching yeast/eukaryotic dataset. Historical00:49Z runner failure is not a new
  execution; successful catalogue fallback does not imply matched downstream module
  queries.'
- 'Nuclear envelope and three boundary compartment independent subreview: The rejected
  original actions did include preserve-historical-context language. Their unsupported
  defect and acceptance criterion are corrected without alleging they explicitly ordered
  wholesale history deletion. Optional progress notes can be useful but are not required
  scientific curation; source-neutral prompts remainvalid.'
- 'Nuclear envelope and three boundary compartment independent subreview: All68 original
  input entries were provenance-hashed at originalrevision; only29 actually used current
  local inputs are listed. No historicalcontext file was newly assessed merely because
  its hash was checked. No repository or GitHub mutation; root owns globalQC/finalCI/queue
  and this source report does not precertify them.'
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
- Issue2748 tracks the stale organellar chromatophore review. The new thylakoid-membrane
  parthood edge and history require substantive current-source verification of ontology
  path, source scope and biological claim, not a hash-only refresh.
- Issue2749 tracks eight unsupported expression-only applicability exclusions. Nuclear
  envelope lumen and nuclear net retain genuine physical/material-topology scope with
  molecular machinery explicitly excluded or withheld. All ten originals contained
  explicit exclusions; none was missing.
- Issue2750 corrects the two inherited inner/outer membrane stale-rationale findings.
  Their unchanged rationale is append-only historical provenance, their prompts still
  seek source-neutral grounding, and organism-specific xrefs do not complete family
  or grouped-actor grounding. Explicit rejected dispositions preserve exact predecessors;
  optional progress notes are not elevated to mandatory record curation.
- Source commit e2edc3550e41792c2bb6f24eb2918b7d33d8a58c is retained by tag review-base/pr2372-current-record-followup-20261103.
- CLAUDE.md aliases AGENTS.md; canonical regular AGENTS.md bytes are frozen. Every
  used local context input is frozen before its assessment.
- Fresh and reused source snapshots retain actual access times and inspection tiers.
  Native identifier identity does not independently establish structure membership,
  experimental intervention scope or assembly necessity.
- All twenty native protein commands returned zero. None of the ten records has protein
  examples. Nuclear inner membrane has three UNANCHORED_WITH_UNIPROT typed nodes and
  nuclear outer membrane has two; these are not falsely called COVERED. The other
  eight records have zero typed molecular nodes. Optional example absence alone is
  not a scientific defect.
- The nuclear-net local image is a frozen review input; its pixels, primary caption,
  preparation and source permissions are assessed independently of molecular-composition
  claims.
- Current CausalNode schema permits protein families and complexes as GENE_OR_PROTEIN
  nodes. Optional protein/chemical slots, allowed structural OTHER constituents and
  unread-source absence are not invented findings.
- Native-validator2514 remains open and reused; no scientific record or native resolver
  is edited in this review-only PR.
- Final trusted-base review-check, exact-head independent acceptance, final-head CI
  and merge-group CI occur after this immutable observation and are not represented
  as already completed.
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T025104Z-nitroplast-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T025105Z-nuclear-envelope-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T025106Z-nuclear-envelope-lumen-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T025106Z-nuclear-inner-membrane-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T025107Z-nuclear-lumen-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T025108Z-nuclear-net-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T025109Z-nuclear-outer-membrane-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T025109Z-nucleomorph-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T025110Z-nucleus-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T025111Z-organellar-chromatophore-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
links:
- https://github.com/CultureBotAI/CellStructureMech/pull/2372
- https://github.com/CultureBotAI/CellStructureMech/issues/2514
- https://github.com/CultureBotAI/CellStructureMech/issues/2748
- https://github.com/CultureBotAI/CellStructureMech/issues/2749
- https://github.com/CultureBotAI/CellStructureMech/issues/2750
- https://github.com/CultureBotAI/CellStructureMech/issues/2751
- https://github.com/CultureBotAI/CellStructureMech/issues/2752
- https://github.com/CultureBotAI/CellStructureMech/issues/2753
- https://github.com/CultureBotAI/CellStructureMech/issues/2754
```
