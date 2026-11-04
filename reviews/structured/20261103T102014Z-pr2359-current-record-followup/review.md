# PR 2359: current-input review of ten records and adversarial follow-up

- Review: 20261103T102014Z-pr2359-current-record-followup
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-11-03T10:09:18.407991Z
- Finished UTC: 2026-11-03T10:20:14Z
- Reviewer: Codex root synthesis with three independent read-only adversarial reviewers (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Current-input reassessment of all ten records in PR2359. Three stale reviews are substantively refreshed. Independent source assessments retain five inherited scientific findings and correct eight structured-source applicability assessments without editing records.

## Scope And Provenance

Exact ten-record PR cohort reassessed against current main 7f1c34aa706792399bb3b1c10e7ac189c4870ec1. Changed inputs are substantively reassessed. Scientific records remain unchanged.

Selection: Complete cohort of ten maintained records reviewed in original PR head 1309942a4f279271c832562d4dd7f3d099fd309f.
Coverage: full; 10 reviewed / 10 in the declared population.
Source: working_tree at Git base fa6c7f0034c57fac03d026ce0ddb8aaa4bd4b2e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0031969 | data/structures/membrane_organelle/chloroplast_membrane.yaml | maintained | chloroplast membrane |
| GO:0009707 | data/structures/membrane_organelle/chloroplast_outer_membrane.yaml | maintained | chloroplast outer membrane |
| GO:0009570 | data/structures/membrane_organelle/chloroplast_stroma.yaml | maintained | chloroplast stroma |
| GO:0009534 | data/structures/membrane_organelle/chloroplast_thylakoid.yaml | maintained | chloroplast thylakoid |
| GO:0009543 | data/structures/membrane_organelle/chloroplast_thylakoid_lumen.yaml | maintained | chloroplast thylakoid lumen |
| GO:0009535 | data/structures/membrane_organelle/chloroplast_thylakoid_membrane.yaml | maintained | chloroplast thylakoid membrane |
| GO:0046858 | data/structures/membrane_organelle/chlorosome.yaml | maintained | chlorosome |
| GO:0033105 | data/structures/membrane_organelle/chlorosome_envelope.yaml | maintained | chlorosome envelope |
| GO:0020018 | data/structures/membrane_organelle/ciliary_pocket_membrane.yaml | maintained | ciliary pocket membrane |
| GO:0005801 | data/structures/membrane_organelle/cis_golgi_network.yaml | maintained | cis-Golgi network |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full native QC | passed | True | GO:0031969, GO:0009707, GO:0009570, GO:0009534, GO:0009543, GO:0009535, GO:0046858, GO:0033105, GO:0020018, GO:0005801 | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| Native label correspondence | passed | True | GO:0031969, GO:0009707, GO:0009570, GO:0009534, GO:0009543, GO:0009535, GO:0046858, GO:0033105, GO:0020018, GO:0005801 | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| TraitMech references | passed | True | GO:0031969, GO:0009707, GO:0009570, GO:0009534, GO:0009543, GO:0009535, GO:0046858, GO:0033105, GO:0020018, GO:0005801 | Native TraitMech link check passed. |
| Pinned governed files | passed | True | GO:0031969, GO:0009707, GO:0009570, GO:0009534, GO:0009543, GO:0009535, GO:0046858, GO:0033105, GO:0020018, GO:0005801 | Pinned governed files match; native vendored check passed. |
| Native identifier resolver | passed | True | GO:0031969, GO:0009707, GO:0009570, GO:0009534, GO:0009543, GO:0009535, GO:0046858, GO:0033105, GO:0020018, GO:0005801 | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| validate GO:0031969 | passed | True | GO:0031969 | Documented focused command passed. |
| validate-strict GO:0031969 | passed | True | GO:0031969 | Documented focused command passed. |
| validate GO:0009707 | passed | True | GO:0009707 | Documented focused command passed. |
| validate-strict GO:0009707 | passed | True | GO:0009707 | Documented focused command passed. |
| validate GO:0009570 | passed | True | GO:0009570 | Documented focused command passed. |
| validate-strict GO:0009570 | passed | True | GO:0009570 | Documented focused command passed. |
| validate GO:0009534 | passed | True | GO:0009534 | Documented focused command passed. |
| validate-strict GO:0009534 | passed | True | GO:0009534 | Documented focused command passed. |
| validate GO:0009543 | passed | True | GO:0009543 | Documented focused command passed. |
| validate-strict GO:0009543 | passed | True | GO:0009543 | Documented focused command passed. |
| validate GO:0009535 | passed | True | GO:0009535 | Documented focused command passed. |
| validate-strict GO:0009535 | passed | True | GO:0009535 | Documented focused command passed. |
| validate GO:0046858 | passed | True | GO:0046858 | Documented focused command passed. |
| validate-strict GO:0046858 | passed | True | GO:0046858 | Documented focused command passed. |
| validate GO:0033105 | passed | True | GO:0033105 | Documented focused command passed. |
| validate-strict GO:0033105 | passed | True | GO:0033105 | Documented focused command passed. |
| validate GO:0020018 | passed | True | GO:0020018 | Documented focused command passed. |
| validate-strict GO:0020018 | passed | True | GO:0020018 | Documented focused command passed. |
| validate GO:0005801 | passed | True | GO:0005801 | Documented focused command passed. |
| validate-strict GO:0005801 | passed | True | GO:0005801 | Documented focused command passed. |
| Supplemental bounded PMID authority checks | passed | True | GO:0031969, GO:0009707, GO:0009570, GO:0009534, GO:0009543, GO:0009535, GO:0046858, GO:0033105, GO:0020018, GO:0005801 | 909 PMIDs all OK in bounded native requests; full-command limitations remain separate. |
| Official structured-source applicability and covered-dataset cross-checks | passed | False | GO:0031969, GO:0009707, GO:0009570, GO:0009534, GO:0009543, GO:0009535, GO:0046858, GO:0033105, GO:0020018, GO:0005801 | Eight applicability defects are corrected: five omissions (chloroplast thylakoid, thylakoid membrane, chlorosome, chlorosome envelope and cis-Golgi network), and three unsupported expression-only exclusions (chloroplast membrane, outer membrane and stroma). Thylakoid lumen and ciliary pocket membrane are genuine sparse morphology/topology exclusions. Actual complete catalogue coverage has no matched chloroplast host, chlorosome organism or relevant budding-yeast dataset. No unrelated organism dataset or downstream module query substitutes for this noncoverage. Resource noncoverage is not biological absence; retained historical runner failure is not a fresh invocation. |
| Independent claim-level source review | passed | True | GO:0031969, GO:0009707, GO:0009570, GO:0009534, GO:0009543, GO:0009535, GO:0046858, GO:0033105, GO:0020018, GO:0005801 | Three read-only reviewers covered the complete ten-record cohort, including changed inputs, with explicit scientific findings and source-access limits. Final artifact/head acceptance occurs after saving. |
| Retained historical adapter runner availability | unavailable | False | GO:0031969, GO:0009707, GO:0009570, GO:0009534, GO:0009535, GO:0046858, GO:0033105, GO:0005801 | Historical 00:49Z invocation unavailable due to OS access restriction. Official catalogue source fallback was inspected separately; no current invocation or successful adapter execution is claimed. The actual historical exit code 1 is retained in the evidence receipt, since the native unavailable-check model has no execution exit-code field. |
| Native chloroplast membrane UniProt verify check | passed | True | GO:0031969 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native chloroplast membrane UniProt causal check | passed | True | GO:0031969 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native chloroplast outer membrane UniProt verify check | passed | True | GO:0009707 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native chloroplast outer membrane UniProt causal check | passed | True | GO:0009707 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native chloroplast stroma UniProt verify check | passed | True | GO:0009570 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native chloroplast stroma UniProt causal check | passed | True | GO:0009570 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native chloroplast thylakoid UniProt verify check | passed | True | GO:0009534 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native chloroplast thylakoid UniProt causal check | passed | True | GO:0009534 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native chloroplast thylakoid lumen UniProt verify check | passed | True | GO:0009543 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native chloroplast thylakoid lumen UniProt causal check | passed | True | GO:0009543 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native chloroplast thylakoid membrane UniProt verify check | passed | True | GO:0009535 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native chloroplast thylakoid membrane UniProt causal check | passed | True | GO:0009535 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native chlorosome UniProt verify check | passed | True | GO:0046858 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native chlorosome UniProt causal check | passed | True | GO:0046858 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native chlorosome envelope UniProt verify check | passed | True | GO:0033105 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native chlorosome envelope UniProt causal check | passed | True | GO:0033105 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native ciliary pocket membrane UniProt verify check | passed | True | GO:0020018 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native ciliary pocket membrane UniProt causal check | passed | True | GO:0020018 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native cis golgi network UniProt verify check | passed | True | GO:0005801 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native cis golgi network UniProt causal check | passed | True | GO:0005801 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |

## Scientific And Domain Assessments

### Whole thylakoid, membrane and lumen are distinct

identity: supported. Targets: GO:0009534.

GO0009534 and SL0056 identify the whole chloroplast thylakoid, with plastid and broader thylakoid parents, chloroplast parthood and membrane/lumen parts. OTHER is consistent with GO’s explicit non-organelle comment and the absence of a closer non-organelle bounded-compartment kind. The membrane encloses the lumen rather than the complete membrane-plus-lumen structure.

### The own membrane part is an appropriate structural component

grounding: supported. Targets: GO:0009534.

The single membrane row identifies an actual own structural part with exact GO0009535 grounding and LIPID material type. It denotes the constituent pigmented membrane, not an individual lipid species or photosynthetic protein. No conflicting family assignment or universal inventory is asserted.

### Constituting membrane versus molecular formation requirements

evidence: unknown. Targets: GO:0009534.

A membrane is constitutive of the membrane-bounded thylakoid named by the ESSENTIAL row. The sources do not establish that each pigment, lipid species or photosynthetic complex is necessary for thylakoid formation. Proposed biogenesis routes and photosynthetic activity must remain separate from that experimental question.

### Electron transport and proton-gradient generation

evidence: supported. Targets: GO:0009534.

GO0009767 precisely matches the maintained electron-transport function; native location authority and the inspected Terashima review support the membrane site and trans-thylakoid gradient. This does not transfer stromal carbon-fixation machinery into the thylakoid or claim all light reactions are a single protein complex.

### Explicitly nonmechanistic whole-thylakoid topology

graph: supported. Targets: GO:0009534.

All five current edges were assessed: original stroma embedding, membrane-encloses-lumen and photosynthetic-function relations, plus the two added membrane/lumen part_of whole-thylakoid edges. Fresh GO typed direct children and UniProt immediate partOf hosts support both additions. They do not reintroduce membrane-bounds-the-whole, assert complete carrier chemistry or terminally dispose of historical735/736.

### Green-lineage occurrence with a direct Chlamydomonas example

scope: supported. Targets: GO:0009534.

Current taxonomy verifies Viridiplantae33090 and C.reinhardtii3055. Engel directly studies CC-124/137c in TAP under constant light; the primary body supports the native membrane/lumen species example while distinguishing algal organization from higher-plant grana. Perez/Terashima secondary context and the primary Introduction support qualitative photosynthetic green-lineage occurrence. Keeling selected secondary body preserves nonphotosynthetic-plastid limits. COMMON is not measured prevalence; no universal architecture or experimental stock transfer is inferred.

### Bounded clean assessment

completeness: supported. Targets: GO:0009534.

No scientific record-curation defect was established within the inspected claims. Optional protein inventories, images, numerical dimensions and expanded mechanisms are not mandatory. The Engel correction concerns a Figure3 scale unit absent from these records. Historical issue numbers in record history are preserved as history, not independently terminally resolved by this review. Bundle freshness/applicability corrections are separate.

### Native protein identity and graph checks

schema: supported. Targets: GO:0009534.

Both actual focused commands exited0. All three targets have empty protein-example inventories and zero GENE_OR_PROTEIN nodes. Exact material/structure nodes are not forced into protein coverage; these checks do not prove narrative molecular function, localization or assembly necessity.

### Original native artifacts and frozen target comparison

provenance: supported. Targets: GO:0009534.

Original YAML validates and Markdown is byte-identical to native render. Historical target bytes match its original frozen hash. Current whole-thylakoid differs by added history and two parthood edges; these are independently refreshed against current authorities. Immutable originals are preserved.

### Named photosynthetic pathways and covered-host assessment

scope: supported. Targets: GO:0009534.

Photosynthetic electron transport/light-reaction claims trigger applicability despite no transcriptomic assertion. The fresh complete source catalogue contains no matched Chlamydomonas/green-lineage host dataset; cyanobacterial S.elongatus cannot substitute for chloroplast evidence. No downstream gene/module search applies, and catalogue noncoverage is not biological absence. Historical runner unavailability remains separately dated.

### Enclosed volume and plastid-lumen hierarchy

identity: supported. Targets: GO:0009543.

GO0009543 and SL0057 identify the lumen as the space inside chloroplast thylakoid membranes. Plastid-thylakoid-lumen parentage and whole-thylakoid parthood are supported. The maintained definition is a faithful paraphrase of the current cavity definition, not an identity change.

### Boundary membrane is not a lumen constituent

grounding: supported. Targets: GO:0009543.

The intentionally empty component inventory is coherent for a subcellular region. Its bounding membrane is a graph boundary, not a component located inside the lumen. No exact lumenal protein inventory, necessity, stoichiometry or family grounding is asserted, so no assembly-essentiality claim needs reinterpretation.

### Minimal boundary relation with appropriate scope

graph: supported. Targets: GO:0009543.

The single encloses edge links the correct membrane and lumen authorities. NONMECHANISTIC accurately describes this topology and does not assert a proton-transfer or lumenal-protein mechanism. The absence of an optional function field is not a defect.

### Green-lineage occurrence with a direct Chlamydomonas example

scope: supported. Targets: GO:0009543.

Current taxonomy verifies Viridiplantae33090 and C.reinhardtii3055. Engel directly studies CC-124/137c in TAP under constant light; the primary body supports the native membrane/lumen species example while distinguishing algal organization from higher-plant grana. Perez/Terashima secondary context and the primary Introduction support qualitative photosynthetic green-lineage occurrence. Keeling selected secondary body preserves nonphotosynthetic-plastid limits. COMMON is not measured prevalence; no universal architecture or experimental stock transfer is inferred.

### Bounded clean assessment

completeness: supported. Targets: GO:0009543.

No scientific record-curation defect was established within the inspected claims. Optional protein inventories, images, numerical dimensions and expanded mechanisms are not mandatory. The Engel correction concerns a Figure3 scale unit absent from these records. Historical issue numbers in record history are preserved as history, not independently terminally resolved by this review. Bundle freshness/applicability corrections are separate.

### Native protein identity and graph checks

schema: supported. Targets: GO:0009543.

Both actual focused commands exited0. All three targets have empty protein-example inventories and zero GENE_OR_PROTEIN nodes. Exact material/structure nodes are not forced into protein coverage; these checks do not prove narrative molecular function, localization or assembly necessity.

### Original native artifacts and frozen target comparison

provenance: supported. Targets: GO:0009543.

Original YAML validates and Markdown is byte-identical to native render. Historical target bytes match its original frozen hash. Current target bytes remain unchanged from the original frozen input. Immutable originals are preserved.

### Sparse lumen topology and actual applicability trigger

scope: not_applicable. Targets: GO:0009543.

The lumen record asserts an enclosed region, its boundary and occurrence; it explicitly refrains from lumenal proteins and proton-transport mechanisms. No represented gene, accession, regulator, molecular pathway or stress response requires module analysis. No molecular inventory is invented. The missing original adapter row is a genuine topology-only exclusion, not a bundle defect.

### Chloroplast-specific membrane and broader parents

identity: supported. Targets: GO:0009535.

GO0009535 and SL0058 exactly identify the chloroplast thylakoid membrane. Direct plastid-thylakoid-membrane ancestry plus transitive generic thylakoid-membrane ancestry are coherent, and parthood in the whole chloroplast thylakoid is supported. Bacterial and cyanelle membranes remain broader-class context, not exact synonyms.

### Collective lipid bilayer without forced molecular grounding

grounding: supported. Targets: GO:0009535.

The component names collective thylakoid lipid material. Exact location authorities identify the complete membrane, not an individual source-neutral lipid class; reviewed-label-only representation and the open grounding discussion are appropriate. The source does not require a complete photosystem or antenna inventory in this membrane record.

### Material constitution and empirical formation requirements

evidence: unknown. Targets: GO:0009535.

The ESSENTIAL row represents constituting membrane material. None of the reviewed photosynthetic proteins, pigments or lipid species is thereby demonstrated necessary for forming a thylakoid membrane. Activity, light acclimation, proteomic localization and proposed biogenesis do not resolve those individual assembly requirements.

### Light reactions at the membrane surface

evidence: supported. Targets: GO:0009535.

GO0019684, SL0058 and the inspected Terashima/Perez review sections support the membrane’s light-reaction site, electron transfer and trans-thylakoid proton gradient. The function does not equate electron transport with carbon fixation or assert a complete source-neutral protein mechanism.

### Collective membrane node and boundary/function edges

graph: supported. Targets: GO:0009535.

The membrane node’s component_ref denotes its collective lipid-bilayer constituent, consistent with this membrane-only record; it does not identify the complete thylakoid compartment as lipid material. Encloses and supports edges correctly express boundary and general functional site. Explicit NONMECHANISTIC scope avoids unsupported complete carrier chemistry.

### Green-lineage occurrence with a direct Chlamydomonas example

scope: supported. Targets: GO:0009535.

Current taxonomy verifies Viridiplantae33090 and C.reinhardtii3055. Engel directly studies CC-124/137c in TAP under constant light; the primary body supports the native membrane/lumen species example while distinguishing algal organization from higher-plant grana. Perez/Terashima secondary context and the primary Introduction support qualitative photosynthetic green-lineage occurrence. Keeling selected secondary body preserves nonphotosynthetic-plastid limits. COMMON is not measured prevalence; no universal architecture or experimental stock transfer is inferred.

### Bounded clean assessment

completeness: supported. Targets: GO:0009535.

No scientific record-curation defect was established within the inspected claims. Optional protein inventories, images, numerical dimensions and expanded mechanisms are not mandatory. The Engel correction concerns a Figure3 scale unit absent from these records. Historical issue numbers in record history are preserved as history, not independently terminally resolved by this review. Bundle freshness/applicability corrections are separate.

### Native protein identity and graph checks

schema: supported. Targets: GO:0009535.

Both actual focused commands exited0. All three targets have empty protein-example inventories and zero GENE_OR_PROTEIN nodes. Exact material/structure nodes are not forced into protein coverage; these checks do not prove narrative molecular function, localization or assembly necessity.

### Original native artifacts and frozen target comparison

provenance: supported. Targets: GO:0009535.

Original YAML validates and Markdown is byte-identical to native render. Historical target bytes match its original frozen hash. Current target bytes remain unchanged from the original frozen input. Immutable originals are preserved.

### Named photosynthetic pathways and covered-host assessment

scope: supported. Targets: GO:0009535.

Photosynthetic electron transport/light-reaction claims trigger applicability despite no transcriptomic assertion. The fresh complete source catalogue contains no matched Chlamydomonas/green-lineage host dataset; cyanobacterial S.elongatus cannot substitute for chloroplast evidence. No downstream gene/module search applies, and catalogue noncoverage is not biological absence. Historical runner unavailability remains separately dated.

### Two newly added parthood edges

graph: supported. Targets: GO:0009534.

Current edges3 and4 add membrane0009535 and lumen0009543 as parts of whole thylakoid0009534. GO0009534 directly lists both typed part_of children; SL0057/0058 directly name SL0056 as partOf, with broader plastid-thylakoid ancestry separately represented. These facts support both additions without confusing subclass identity, enclosing boundaries or mechanism. No stale delta remains unrefreshable.

### Whole versus envelope identity and hierarchy

identity: supported. Targets: GO:0046858.

Exact active GO and UniProt definitions distinguish chlorosome, its monolayer envelope and lipid bilayers. The OTHER kind and intracellular membraneless-parent interpretation do not deny the glycolipid boundary; envelope and whole baseplate are separate scopes.

### Csm identities, reviewed status and bounded family coverage

grounding: supported. Targets: GO:0046858.

All ten declared accessions match TLS genes: seven reviewed, three unreviewed. Accessory location cohort spans distinct families/domains; no single exact family should replace that set. The baseplate denotes the assembled CsmA/BChl-a complex, not the apoprotein family. csmK query miss and H2VFJ4 match204 do not prove absence.

### Constituents versus formation necessity

evidence: concern. Targets: GO:0046858.

Inherited F1 remains confirmed: the ESSENTIAL baseplate annotation asserts target formation necessity beyond the cited experiments. Preserve positive structural integrity, antenna, attachment and viability roles. Frigaard2004 did not obtain segregated CsmA-loss mutants; Nielsen used bchK-mutant carotenosomes with a retained baseplate. Neither proves dispensability or universal failure of formation. Collective monolayer/pigment material is constitutional, not evidence that each molecular species is individually required.

### Taxon examples and distribution

scope: supported. Targets: GO:0046858.

C. tepidum structural/genetic and C. aurantiacus J-10-fl imaging sources support the bounded examples. VARIABLE Bacteria and named phototrophic groups are secondary-context scope, not universal bacterial membership. Nielsen high-resolution preparation is mutant carotenosome; its wild-type comparisons and earlier AFM context are kept explicit.

### Light harvesting and component-localization roles

evidence: supported. Targets: GO:0046858.

Pigment self-assembly, asymmetric envelope and baseplate energy transfer have authority/primary structural support. Secondary sources supply broader antenna context. Broad photosynthesis GO is not substituted for exact light harvesting, and heterogeneous accessory composition is not silently made universally essential.

### Stale refresh: baseplate node identity

graph: supported. Targets: GO:0046858.

Current csma_baseplate node is STRUCTURE and grounded to the frozen whole baseplate neighbor. This accurately denotes the assembled complex; the associated csmA example is not mistaken for the structure itself. This current-content assessment does not resolve an unfrozen multi-target category finding or all of closed issue2419.

### Stale refresh: new accessory Csm surface-localization edge

graph: supported. Targets: GO:0046858.

The added component-linked accessory Csm node localizes to the monolayer surface, consistent with the explicitly secondary Orf protein section and primary envelope studies. Location is accepted at cohort/context scope, not as a new universal assembly mechanism or a direct-contact network. Gene-family heterogeneity and K example gap remain explicit.

### Existing seven-edge pigment/baseplate energy-flow model

graph: supported. Targets: GO:0046858.

Existing self-assembly, monolayer enclosure, baseplate constituent, excitation transfer and acceptor/photochemistry edges are coarse supported organization. The MECHANISTIC label does not prove a complete molecular transfer mechanism; the generic unanchored acceptor and taxon-dependent downstream coupling remain bounded. The separate ESSENTIAL field remains F1, rather than treating a constituent forms edge as a direct deletion experiment.

### Missing original structured-source applicability assessment

scope: concern. Targets: GO:0046858.

Original review omits applicability despite explicit Csm genes/accessions and light-harvesting pathway context. Current bounded catalogue contains no matching chlorosome-bearing organism dataset. Historical runner unavailable result and current fallback are separately dated; no unmatched bacterial gene query is substituted.

### Original provenance, current checks and native limits

schema: supported. Targets: GO:0046858.

Original pair validates and deterministically renders; frozen old blob is verified and current delta substantively reassessed. Six current slice protein receipts are actual exit0. Coverage labels retain gaps rather than upgrading them to experimental membership/necessity or automatic scientific defects.

### Exact finding lineage and current verdict

provenance: concern. Targets: GO:0046858.

Retain exact original F1 occurrence and stable issue key as open confirmed major; current verdict needs_curation. Stale review refresh is feasible within a review-only successor; scientific record edits remain separately proposed.

### Whole versus envelope identity and hierarchy

identity: supported. Targets: GO:0033105.

Exact active GO and UniProt definitions distinguish chlorosome, its monolayer envelope and lipid bilayers. The OTHER kind and intracellular membraneless-parent interpretation do not deny the glycolipid boundary; envelope and whole baseplate are separate scopes.

### Csm identities, reviewed status and bounded family coverage

grounding: supported. Targets: GO:0033105.

All ten declared accessions match TLS genes: seven reviewed, three unreviewed. Accessory location cohort spans distinct families/domains; no single exact family should replace that set. The baseplate denotes the assembled CsmA/BChl-a complex, not the apoprotein family. csmK query miss and H2VFJ4 match204 do not prove absence.

### Constituents versus formation necessity

evidence: concern. Targets: GO:0033105.

Inherited F1 remains confirmed: the ESSENTIAL baseplate annotation asserts target formation necessity beyond the cited experiments. Preserve positive structural integrity, antenna, attachment and viability roles. Frigaard2004 did not obtain segregated CsmA-loss mutants; Nielsen used bchK-mutant carotenosomes with a retained baseplate. Neither proves dispensability or universal failure of formation. Collective monolayer/pigment material is constitutional, not evidence that each molecular species is individually required.

### Taxon examples and distribution

scope: supported. Targets: GO:0033105.

C. tepidum structural/genetic and C. aurantiacus J-10-fl imaging sources support the bounded examples. VARIABLE Bacteria and named phototrophic groups are secondary-context scope, not universal bacterial membership. Nielsen high-resolution preparation is mutant carotenosome; its wild-type comparisons and earlier AFM context are kept explicit.

### Light harvesting and component-localization roles

evidence: supported. Targets: GO:0033105.

Pigment self-assembly, asymmetric envelope and baseplate energy transfer have authority/primary structural support. Secondary sources supply broader antenna context. Broad photosynthesis GO is not substituted for exact light harvesting, and heterogeneous accessory composition is not silently made universally essential.

### Stale refresh: baseplate node identity

graph: supported. Targets: GO:0033105.

Current csma_baseplate node is STRUCTURE and grounded to the frozen whole baseplate neighbor. This accurately denotes the assembled complex; the associated csmA example is not mistaken for the structure itself. This current-content assessment does not resolve an unfrozen multi-target category finding or all of closed issue2419.

### Six-edge NONMECHANISTIC envelope topology

graph: supported. Targets: GO:0033105.

Envelope parthood, boundary material, embedded accessory group, pigment enclosure, baseplate position and antenna support agree with authority/structural source scopes. No residue-level contact network or complete biogenesis pathway is claimed.

### Missing original structured-source applicability assessment

scope: concern. Targets: GO:0033105.

Original review omits applicability despite explicit Csm genes/accessions and light-harvesting pathway context. Current bounded catalogue contains no matching chlorosome-bearing organism dataset. Historical runner unavailable result and current fallback are separately dated; no unmatched bacterial gene query is substituted.

### Original provenance, current checks and native limits

schema: supported. Targets: GO:0033105.

Original pair validates and deterministically renders; frozen old blob is verified and current delta substantively reassessed. Six current slice protein receipts are actual exit0. Coverage labels retain gaps rather than upgrading them to experimental membership/necessity or automatic scientific defects.

### Exact finding lineage and current verdict

provenance: concern. Targets: GO:0033105.

Retain exact original F1 occurrence and stable issue key as open confirmed major; current verdict needs_curation. Stale review refresh is feasible within a review-only successor; scientific record edits remain separately proposed.

### Network, membrane, stack and whole Golgi boundaries

identity: supported. Targets: GO:0005801.

GO:0005801 denotes a distinct ER-facing network, not a protein, lipid constituent or whole stack. Exact synonyms and Golgi-subcompartment/whole-Golgi relations are semantically appropriate; current authority comment distinguishes CGN from the stack. Neighbor context is restricted to frozen boundary fields.

### Inherited F1: experimental strain/current taxon

scope: concern. Targets: GO:0005801.

Rossanese uses PPY1 and isogenic PPY12. ATCC strain designation/reidentification and ENA source qualifiers identify PPY12 as K. phaffii460519, while the record assigns both occurrence and canonical example to K. pastoris4922. Historical species naming is insufficient; F1 remains confirmed major.

### Inherited F2: experiment-to-compartment scope

evidence: concern. Targets: GO:0005801.

Rossanese establishes ordered Golgi stacks and adjacent tER, with Sec13-positive tubulovesicular interface assigned to tER. That is not direct identification of distinct GO:0005801 CGN. Species correction alone does not repair compartment-specific occurrence/example support; Cho abstract concerns S. cerevisiae Sed5-enriched early-Golgi membranes and does not fill this gap. No biological absence is claimed.

### Inherited F3: whole-network component link

graph: concern. Targets: GO:0005801.

The complete network node grounded GO:0005801 points through component_ref to cis_golgi_network_lipid_bilayer. The schema reserves this link for the own constituent; a generic lipid material cannot identify the complete compartment. Remove the link or give the material its own node; retain minor severity and the otherwise correct topology.

### Lipid material, excluded residents and necessity

completeness: supported. Targets: GO:0005801.

Generic lipid bilayer is a legitimate collective boundary constituent, not a second whole-organelle grounding. Sed5/COPII markers are explicitly excluded as universal constitutive components; immunoisolation/localization does not establish formation necessity or a complete taxon-neutral protein inventory.

### Three topology edges and source limits

graph: supported. Targets: GO:0005801.

Membrane bounds network, network part of Golgi, and network abuts ER are supported by authority definitions. NONMECHANISTIC scope is appropriate; the broad topology does not validate the particular occurrence/canonical example.

### Missing original structured-source applicability assessment

scope: concern. Targets: GO:0005801.

Although the resident inventory is lipid-only, the record explicitly evaluates named Sed5-positive membrane compartments and COPII evidence. Native molecular-claim trigger warrants applicability review. The fresh complete catalogue has no Komagataella/Pichia/Saccharomyces dataset; no matched-organism downstream query is justified. This is not a sparse membrane-only exclusion.

### Unchanged input and zero-protein native coverage

schema: supported. Targets: GO:0005801.

Original frozen target remains byte-identical; original pair validates and renders. Current native protein verification exits0 with empty example inventory and zero protein nodes. This is structural coverage only and does not repair the independent graph component-ref semantics.

### Exact three-finding lineage/current verdict

provenance: concern. Targets: GO:0005801.

Preserve original20261021T110938Z-cis-golgi-network-audit F1/F2/F3, keys and major/major/minor severity. All remain open; current needs_curation does not authorize record edits, close neighbor issues or resolve a category-wide finding.

### Native schema, deterministic rendering and original input integrity

schema: supported. Targets: GO:0031969.

Original bundle validates and renders exactly. Its current target hash equals the frozen input and original source revision. Native protein checks pass at empty-inventory scope; scientific claims are assessed separately.

### Images and verbatim source snippets

scope: not_applicable. Targets: GO:0031969.

No maintained image or verbatim snippet is declared by this target. Source text and metadata inspection does not claim image-pixel, tomography-volume or raw-data reanalysis.

### Empty protein inventories and historical checks

provenance: supported. Targets: GO:0031969.

The two fresh native commands report zero errors and zero typed protein graph nodes. Named proteins or pathways in narrative text are not covered by this empty inventory. Historical bundle checks retain their dates and are not portrayed as current runs.

### Native schema, deterministic rendering and original input integrity

schema: supported. Targets: GO:0009707.

Original bundle validates and renders exactly. Its current target hash equals the frozen input and original source revision. Native protein checks pass at empty-inventory scope; scientific claims are assessed separately.

### Images and verbatim source snippets

scope: not_applicable. Targets: GO:0009707.

No maintained image or verbatim snippet is declared by this target. Source text and metadata inspection does not claim image-pixel, tomography-volume or raw-data reanalysis.

### Empty protein inventories and historical checks

provenance: supported. Targets: GO:0009707.

The two fresh native commands report zero errors and zero typed protein graph nodes. Named proteins or pathways in narrative text are not covered by this empty inventory. Historical bundle checks retain their dates and are not portrayed as current runs.

### Native schema, deterministic rendering and original input integrity

schema: supported. Targets: GO:0009570.

Original bundle validates and renders exactly. Its current target hash equals the frozen input and original source revision. Native protein checks pass at empty-inventory scope; scientific claims are assessed separately.

### Images and verbatim source snippets

scope: not_applicable. Targets: GO:0009570.

No maintained image or verbatim snippet is declared by this target. Source text and metadata inspection does not claim image-pixel, tomography-volume or raw-data reanalysis.

### Empty protein inventories and historical checks

provenance: supported. Targets: GO:0009570.

The two fresh native commands report zero errors and zero typed protein graph nodes. Named proteins or pathways in narrative text are not covered by this empty inventory. Historical bundle checks retain their dates and are not portrayed as current runs.

### Native schema, deterministic rendering and original input integrity

schema: supported. Targets: GO:0020018.

Original bundle validates and renders exactly. Its current target hash equals the frozen input and original source revision. Native protein checks pass at empty-inventory scope; scientific claims are assessed separately.

### Images and verbatim source snippets

scope: not_applicable. Targets: GO:0020018.

No maintained image or verbatim snippet is declared by this target. Source text and metadata inspection does not claim image-pixel, tomography-volume or raw-data reanalysis.

### Empty protein inventories and historical checks

provenance: supported. Targets: GO:0020018.

The two fresh native commands report zero errors and zero typed protein graph nodes. Named proteins or pathways in narrative text are not covered by this empty inventory. Historical bundle checks retain their dates and are not portrayed as current runs.

### Molecular/pathway scope and current organism coverage

scope: not_applicable. Targets: GO:0031969.

TOC–TIC/import claims (and HLP/nucleoid context for stroma) trigger an applicability assessment despite an empty typed protein inventory. The complete current catalogue lacks a matching green-algal organism/dataset, so downstream gene/module lookup does not apply. Historical runner unavailability is separate; no expression-only exemption or cyanobacterial substitute is used.

### Qualified green-lineage distribution and exact algal example

scope: supported. Targets: GO:0031969.

Native taxonomy identifies Viridiplantae and Chlamydomonas reinhardtii. Occurrence is qualified to chloroplast-bearing/photosynthetic members, not every tissue or nonphotosynthetic descendant. Keeling secondary body supports that context; Jin primary abstract directly names Chlamydomonas without establishing a universal experimental strain.

### Import structure and actual access tiers

evidence: supported. Targets: GO:0031969.

Jin primary abstract and author entry support the envelope-spanning assembly at Chlamydomonas scope. They do not provide a complete Methods/Results or raw structural audit. Keeling is secondary body context. Reused snapshots retain original09:33Z times; current review does not claim a fresh full paper fetch.

### Formation requirements beyond current representation

scope: unknown. Targets: GO:0031969.

Collective membrane material can be constitutional, while stroma is a spatial region without component essentiality assertions. None of these records establishes necessity of each lipid, import protein or stromal occupant for forming the whole structure. Localization and function do not substitute for formation assays.

### Positive qualified verdict with explicit limitations

consistency: supported. Targets: GO:0031969.

pass_with_limitations remains supported: exact structural identity, boundaries and scoped occurrence/import claims have positive authority/primary support. Unknown molecular formation requirements, incomplete optional inventories and stated source-access limits remain explicit. No original scientific finding or curation action exists for this target, and no new concrete record defect was established.

### Molecular/pathway scope and current organism coverage

scope: not_applicable. Targets: GO:0009707.

TOC–TIC/import claims (and HLP/nucleoid context for stroma) trigger an applicability assessment despite an empty typed protein inventory. The complete current catalogue lacks a matching green-algal organism/dataset, so downstream gene/module lookup does not apply. Historical runner unavailability is separate; no expression-only exemption or cyanobacterial substitute is used.

### Qualified green-lineage distribution and exact algal example

scope: supported. Targets: GO:0009707.

Native taxonomy identifies Viridiplantae and Chlamydomonas reinhardtii. Occurrence is qualified to chloroplast-bearing/photosynthetic members, not every tissue or nonphotosynthetic descendant. Keeling secondary body supports that context; Jin primary abstract directly names Chlamydomonas without establishing a universal experimental strain.

### Import structure and actual access tiers

evidence: supported. Targets: GO:0009707.

Jin primary abstract and author entry support the envelope-spanning assembly at Chlamydomonas scope. They do not provide a complete Methods/Results or raw structural audit. Keeling is secondary body context. Reused snapshots retain original09:33Z times; current review does not claim a fresh full paper fetch.

### Formation requirements beyond current representation

scope: unknown. Targets: GO:0009707.

Collective membrane material can be constitutional, while stroma is a spatial region without component essentiality assertions. None of these records establishes necessity of each lipid, import protein or stromal occupant for forming the whole structure. Localization and function do not substitute for formation assays.

### Positive qualified verdict with explicit limitations

consistency: supported. Targets: GO:0009707.

pass_with_limitations remains supported: exact structural identity, boundaries and scoped occurrence/import claims have positive authority/primary support. Unknown molecular formation requirements, incomplete optional inventories and stated source-access limits remain explicit. No original scientific finding or curation action exists for this target, and no new concrete record defect was established.

### Molecular/pathway scope and current organism coverage

scope: not_applicable. Targets: GO:0009570.

TOC–TIC/import claims (and HLP/nucleoid context for stroma) trigger an applicability assessment despite an empty typed protein inventory. The complete current catalogue lacks a matching green-algal organism/dataset, so downstream gene/module lookup does not apply. Historical runner unavailability is separate; no expression-only exemption or cyanobacterial substitute is used.

### Qualified green-lineage distribution and exact algal example

scope: supported. Targets: GO:0009570.

Native taxonomy identifies Viridiplantae and Chlamydomonas reinhardtii. Occurrence is qualified to chloroplast-bearing/photosynthetic members, not every tissue or nonphotosynthetic descendant. Keeling secondary body supports that context; Jin primary abstract directly names Chlamydomonas without establishing a universal experimental strain.

### Import structure and actual access tiers

evidence: supported. Targets: GO:0009570.

Jin primary abstract and author entry support the envelope-spanning assembly at Chlamydomonas scope. They do not provide a complete Methods/Results or raw structural audit. Keeling is secondary body context. Reused snapshots retain original09:33Z times; current review does not claim a fresh full paper fetch.

### Formation requirements beyond current representation

scope: unknown. Targets: GO:0009570.

Collective membrane material can be constitutional, while stroma is a spatial region without component essentiality assertions. None of these records establishes necessity of each lipid, import protein or stromal occupant for forming the whole structure. Localization and function do not substitute for formation assays.

### Positive qualified verdict with explicit limitations

consistency: supported. Targets: GO:0009570.

pass_with_limitations remains supported: exact structural identity, boundaries and scoped occurrence/import claims have positive authority/primary support. Unknown molecular formation requirements, incomplete optional inventories and stated source-access limits remain explicit. No original scientific finding or curation action exists for this target, and no new concrete record defect was established.

### Generic chloroplast envelope membrane class

identity: supported. Targets: GO:0031969.

Current GO defines either envelope bilayer, with plastid membrane as is-a parent and envelope as whole. The inner/outer membranes are explicit is-a children. Internal thylakoid membrane is distinct; broader UniProt umbrella wording is not used to expand this GO identity.

### Collective lipid constituent rather than chemical species

grounding: supported. Targets: GO:0031969.

The reviewed-label-only row represents generic envelope-bilayer material, not the whole location as a chemical grounding. ESSENTIAL is constitutional at collective bilayer scale; no exact lipid species or molecular assembly factor is declared essential. The open grounding TODO is uncertainty, not evidence that no suitable term exists.

### Three nonmechanistic identity/parthood edges

graph: supported. Targets: GO:0031969.

All three edges retain membrane part_of envelope and inner/outer is_a generic membrane. Exact GO typed children and definitions support these relations without importing thylakoids, translocase subunits or a mechanism.

### Exact outer-membrane orientation and dual parentage

identity: supported. Targets: GO:0009707.

GO0009707 and SL0054 agree on the cytoplasm-facing outer bilayer and exact location mapping. Both plastid outer membrane and chloroplast membrane parents are supported; the whole envelope and intermembrane space remain distinct.

### Constitutional outer lipid bilayer

grounding: supported. Targets: GO:0009707.

The generic lipid constituent is label-only and constitutionally essential at collective bilayer level. Whole-location identifiers are not claimed to identify a lipid species; no imported membrane protein inventory or individual necessity claim is implied.

### Three descriptive spatial relations

graph: supported. Targets: GO:0009707.

All three edges place the outer membrane in the envelope, facing cytoplasm and bounding intermembrane space. GO definitions support these directly; SL0054 parent hierarchy corroborates context without inventing a direct top-level partOf field.

### Matrix compartment excluding thylakoid lumen

identity: supported. Targets: GO:0009570.

GO0009570 and SL0055 identify the stroma, plastid-stroma parent and chloroplast parthood. The explicit lumen exclusion is retained. A spatial region does not require an invariant list of every molecule residing in it.

### Nucleoids and plastoglobules within stromal scope

grounding: supported. Targets: GO:0009570.

GO directly lists nucleoid and plastoglobule part_of children of stroma. SL0217 places plastoglobules in stroma in its definition, while direct partOf is chloroplast. Association with thylakoids does not move them into the thylakoid lumen.

### Primary nucleoid evidence versus secondary proteome context

evidence: supported. Targets: GO:0009570.

The complete Karcher primary abstract supports Chlamydomonas HLP chloroplast targeting and nucleoid association, with RNAi organization/genome effects. Terashima secondary abstract supplies comparative metabolic/protein-biogenesis context; whole-chloroplast surveys are not treated as pure stromal inventories. Direct nucleoid evidence is separately cited on the maintained graph edge.

### Four boundary, parthood and import-destination edges

graph: supported. Targets: GO:0009570.

Envelope encloses stroma; nucleoid and plastoglobule occupy it; the biological process protein import terminates in stroma. The destination compartment is not made the transporting actor. NONMECHANISTIC scope excludes complete import, lipid-remodeling and nucleoid-maintenance mechanisms.

### Sparse material/topology molecular-query exclusion

scope: not_applicable. Targets: GO:0020018.

The maintained pocket-membrane record asserts a collective lipid domain, boundaries and qualitative species occurrence. It names no resident protein, gene, regulator, exact lipid species or molecular pathway needing a matched query. The missing original adapter row is not a bundle defect. Independently inspected catalogue also has no T. brucei dataset; no biological absence follows.

### Exact membrane domain, synonyms and whole-pocket boundary

identity: supported. Targets: GO:0020018.

GO0020018 supports the membrane domain and three exact synonyms; ciliary membrane is the is-a parent and whole pocket the containing structure. The frozen collar and whole-pocket neighbors remain distinct identities.

### Collective bilayer with unresolved molecular inventory

grounding: supported. Targets: GO:0020018.

The label-only material row does not substitute the whole membrane location for an individual lipid. ESSENTIAL is constitutional for the collective bilayer. The inventory TODO does not justify importing every associated trafficking protein or cytoskeletal collar factor as a resident constituent.

### Individual formation dependencies

scope: unknown. Targets: GO:0020018.

No individual lipid or protein is shown necessary for formation of this complete membrane domain. The collective material identity does not supply such an experiment, and this review does not propose an exhaustive composition.

### T. brucei species and bounded experiment scope

scope: supported. Targets: GO:0020018.

Native taxonomy verifies the species. Exact primary abstracts support the qualitative example. Lacomble indexed Cell culture specifies procyclic T. brucei brucei strain427; that strain is not transferred to Gadelha or all life stages. COMMON is qualitative, not a measured population prevalence.

### Direct membrane-domain evidence and secondary context

evidence: supported. Targets: GO:0020018.

Gadelha primary abstract and indexed Discussion support distinct continuous membrane domains and their relationship to cytoskeletal boundaries. Field/Carrington secondary abstract supports the pocket as a membrane invagination. The maintained boundary function does not assert a universal filter/channel mechanism.

### Two nonmechanistic constitution/topology edges

graph: supported. Targets: GO:0020018.

The contributes-to and bounds edges distinguish lipid material, complete membrane domain and whole pocket. They express constitution/topology, not molecular causation or the complete associated cytoskeleton.

### Current abstract/indexed-body tiers differ from historical direct bodies

provenance: supported. Targets: GO:0020018.

Current direct PMC routes supplied challenge pages; indexed primary Discussion/Methods excerpts and exact native abstracts were read instead. Field/Halliday current access is native review abstracts; publisher challenge/stub responses are not full papers. Original wider body-reading claims remain historical and are not copied as current observations.

### Positive qualified boundary review

consistency: supported. Targets: GO:0020018.

pass_with_limitations remains supported for exact membrane identity, species example, collective material and boundary graph. Unresolved molecular inventory, unknown individual formation dependencies and current source-access tiers remain explicit. No original or new scientific correction is established.

### Complete frozen-input comparison and bounded refresh

provenance: supported. Targets: GO:0031969, GO:0009707, GO:0009570, GO:0009534, GO:0009543, GO:0009535, GO:0046858, GO:0033105, GO:0020018, GO:0005801.

3 of ten original target hashes differ from current main. The changed content is substantively reassessed in the target-specific assessments; original observations remain historical and unchanged. All current target and used context bytes are frozen.

## Findings

### micro-F1: Separate CsmA baseplate function and viability from formation necessity

major / open / confirmed; issue key: chlorosome-baseplate-assembly-necessity.

The CsmA-baseplate component is marked ESSENTIAL, which the schema defines in terms of whether the target structure forms without it. Nielsen2016 resolves a baseplate in bchK-mutant carotenosomes and compares wild-type/mutant structure; it does not remove the baseplate to test formation. Frigaard2004 reports failure of csmA transformants to segregate under its growth conditions and interprets possible essential light harvesting/viability, while the nine non-CsmA deletions retain chlorosomes. These results cannot by themselves assign an unqualified formation requirement to the baseplate across this bacterial structure class. Preserve the well-supported constituent and antenna roles, but qualify or withhold the assembly-necessity assertion unless a direct, appropriately scoped formation result is supplied. This finding does not say the baseplate is dispensable or treat vestigial pigment-free remnants as normal chlorosomes. Nielsen2016 explicitly assigns structural integrity as a baseplate function in its Introduction; retain this positive structural role while separating it from a tested universal requirement for formation.

### micro-F2: Separate CsmA baseplate function and viability from formation necessity

major / open / confirmed; issue key: chlorosome_envelope-baseplate-assembly-necessity.

The CsmA-baseplate component is marked ESSENTIAL, which the schema defines in terms of whether the target structure forms without it. Nielsen2016 resolves a baseplate in bchK-mutant carotenosomes and compares wild-type/mutant structure; it does not remove the baseplate to test formation. Frigaard2004 reports failure of csmA transformants to segregate under its growth conditions and interprets possible essential light harvesting/viability, while the nine non-CsmA deletions retain chlorosomes. These results cannot by themselves assign an unqualified formation requirement to the baseplate across this bacterial structure class. Preserve the well-supported constituent and antenna roles, but qualify or withhold the assembly-necessity assertion unless a direct, appropriately scoped formation result is supplied. This finding does not say the baseplate is dispensable or treat vestigial pigment-free remnants as normal chlorosomes. Nielsen2016 explicitly assigns structural integrity as a baseplate function in its Introduction; retain this positive structural role while separating it from a tested universal requirement for formation.

### micro-F3: The cited PPY1/PPY12 study is assigned to the wrong current species

major / open / confirmed; issue key: cis-golgi-network-ppy12-current-taxon.

Rossanese1999 used PPY1 and its isogenic PPY12 derivatives. ATCC explicitly identifies PPY12 as K. phaffii following sequence-based reidentification, independently corroborated by ENA LC815816.1 taxon460519. The maintained taxonomic_distribution and canonical_examples instead assign the experiment to K. pastoris4922. The historical Pichia pastoris name alone does not justify that current assignment.

### micro-F4: The cited stack study does not directly establish this CGN occurrence and example

major / open / confirmed; issue key: cis-golgi-network-stack-study-evidence-scope.

The occurrence and canonical-example slots belong to GO0005801, but their sole cited study directly resolves Golgi stacks and adjacent transitional ER. Native GO distinguishes CGN from the Golgi stack, and the source assigns its observed Sec13-positive tubulovesicular interface to tER. Neither early/late Golgi marker apposition nor ordered stacks alone demonstrates a distinct CGN. Correcting the species leaves this unsupported compartment-specific attribution intact.

### micro-F5: The whole-network graph node links to a lipid-material component

minor / open / confirmed; issue key: cis-golgi-network-node-lipid-component-link.

The graph node grounded to GO0005801 denotes the complete membrane-bounded network, but its component_ref names cis_golgi_network_lipid_bilayer. The schema uses component_ref when the node is an own component; native GO separately identifies the complete network and its surrounding membrane. The link therefore collapses the compartment into its lipid constituent even though the graph otherwise keeps membrane and network nodes separate.

## Recommended Actions And Acceptance Checks

### micro-A1

Revise the CsmA-baseplate formation-necessity annotation or attach direct source evidence at the relevant taxon and experimental scope.

- Keep the supported baseplate constituent identity, structural-integrity role and light-harvesting role.
- Use UNKNOWN or an appropriately qualified necessity state unless inspected evidence tests target formation after the relevant component loss.
- Do not substitute failed mutant segregation, viability or excitation-transfer loss for an assembly endpoint; retain the modified-carotenosome versus normal-chlorosome boundary.
- Apply any scientific edit only in a separately authorized guarded-writer curation PR with event/history and native validation; this review-only PR leaves the record unchanged.

### micro-A2

Revise the CsmA-baseplate formation-necessity annotation or attach direct source evidence at the relevant taxon and experimental scope.

- Keep the supported baseplate constituent identity, structural-integrity role and light-harvesting role.
- Use UNKNOWN or an appropriately qualified necessity state unless inspected evidence tests target formation after the relevant component loss.
- Do not substitute failed mutant segregation, viability or excitation-transfer loss for an assembly endpoint; retain the modified-carotenosome versus normal-chlorosome boundary.
- Apply any scientific edit only in a separately authorized guarded-writer curation PR with event/history and native validation; this review-only PR leaves the record unchanged.

### micro-A3

Correct any retained PPY1/PPY12-based example and occurrence attribution to K. phaffii460519 with a documented strain bridge; retain the historical source name in notes. Address the separate CGN-specific evidence finding before retaining this as a confirmed CGN example.

- Any retained Rossanese example uses the experimentally verified current taxon and preserves the historical name.
- The species correction is not treated as proof of a CGN distinct from Golgi stacks.
- Focused native validators pass.
- Apply any scientific edit only in a separately authorized guarded-writer curation PR with event/history and native validation; this review-only PR leaves the record unchanged.

### micro-A4

Supply direct evidence identifying the CGN in the asserted organism, or remove/defer the CGN-specific occurrence/example while retaining Rossanese as explicitly broader Golgi-stack/tER context. Do not replace the CGN identity with a whole-stack term or infer absence of CGN from this evidence gap.

- Retained occurrence/example evidence distinguishes CGN from whole Golgi stacks and transitional ER.
- The canonical example does not depend solely on whole-stack morphology or early-Golgi marker localization.
- The independent current-species error is resolved for any retained experimental attribution.
- Focused native validators pass.
- Apply any scientific edit only in a separately authorized guarded-writer curation PR with event/history and native validation; this review-only PR leaves the record unchanged.

### micro-A5

Remove the lipid component_ref from the whole-CGN node, or add a separate lipid-material node carrying that component_ref and an appropriate constituent relationship. Keep GO0005801 on the complete network and GO0033106 on its membrane.

- No whole-CGN node is locally identified as the lipid-bilayer component.
- Any added material node preserves membrane-versus-compartment scope.
- Focused native validators pass.
- Apply any scientific edit only in a separately authorized guarded-writer curation PR with event/history and native validation; this review-only PR leaves the record unchanged.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| current-record-0 | data/structures/membrane_organelle/chloroplast_membrane.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 115d9369e1b84a54e66028f079a8d140e72d40ec2fb5877e64fb592b6a085905; current SHA256 115d9369e1b84a54e66028f079a8d140e72d40ec2fb5877e64fb592b6a085905. Record bytes unchanged since the original review. |
| original-review-0 | reviews/structured/20261021T110921Z-chloroplast-membrane-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-1 | data/structures/membrane_organelle/chloroplast_outer_membrane.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 f499d6317b1546cf0d578f54d04df76a8af3c54746f29db6b2d7af0244b0075d; current SHA256 f499d6317b1546cf0d578f54d04df76a8af3c54746f29db6b2d7af0244b0075d. Record bytes unchanged since the original review. |
| original-review-1 | reviews/structured/20261021T110923Z-chloroplast-outer-membrane-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-2 | data/structures/membrane_organelle/chloroplast_stroma.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 cfdb0d3be9fba838d5288e478b39f922a4e11cbd240b689a2cbca7690c262b6a; current SHA256 cfdb0d3be9fba838d5288e478b39f922a4e11cbd240b689a2cbca7690c262b6a. Record bytes unchanged since the original review. |
| original-review-2 | reviews/structured/20261021T110927Z-chloroplast-stroma-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-3 | data/structures/membrane_organelle/chloroplast_thylakoid.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 ed335bb9dbdc4ba22ed33046fa25d64796c2eadefe71b1e04eaeb7d67156723c; current SHA256 edf435ef39aeb8c0fa0e572768a0e7f599b7177945d1c7a621d3d810bbaf17cd. Changed record reassessed against current sources. |
| original-review-3 | reviews/structured/20261021T110930Z-chloroplast-thylakoid-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-4 | data/structures/membrane_organelle/chloroplast_thylakoid_lumen.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 6efd0a2e86462ae192dc2f27f9edc945dc6b522a31d8e233458cd25e661fb2af; current SHA256 6efd0a2e86462ae192dc2f27f9edc945dc6b522a31d8e233458cd25e661fb2af. Record bytes unchanged since the original review. |
| original-review-4 | reviews/structured/20261021T110931Z-chloroplast-thylakoid-lumen-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-5 | data/structures/membrane_organelle/chloroplast_thylakoid_membrane.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 16f50bd615bee75edd15004622bae49a9a25e71dd4b9573584ca1659139d0999; current SHA256 16f50bd615bee75edd15004622bae49a9a25e71dd4b9573584ca1659139d0999. Record bytes unchanged since the original review. |
| original-review-5 | reviews/structured/20261021T110932Z-chloroplast-thylakoid-membrane-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-6 | data/structures/membrane_organelle/chlorosome.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 c68416577a67653e152c1a57c65ec074d98950a9a1c4d0023946a0510044b8e9; current SHA256 be2261521f06e087e2edd95af366813a289dba202239800a2c715033bd0105da. Changed record reassessed against current sources. |
| original-review-6 | reviews/structured/20261021T110934Z-chlorosome-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-7 | data/structures/membrane_organelle/chlorosome_envelope.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 2514acd0c5f9bd7c73e1c1d77096301858323dbfe5fa35434b09c501b5fbf8ed; current SHA256 d39583d641a4c6070008f52e29246d1659bf86b1158799b1c30caf2e272ef903. Changed record reassessed against current sources. |
| original-review-7 | reviews/structured/20261021T110935Z-chlorosome-envelope-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-8 | data/structures/membrane_organelle/ciliary_pocket_membrane.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 acdf228c05817a740e627e5885200d543b8cb91f6ac94aefa4f5bf954255b3e0; current SHA256 acdf228c05817a740e627e5885200d543b8cb91f6ac94aefa4f5bf954255b3e0. Record bytes unchanged since the original review. |
| original-review-8 | reviews/structured/20261021T110936Z-ciliary-pocket-membrane-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-9 | data/structures/membrane_organelle/cis_golgi_network.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 369cae5270aeacd25a94317be3b005167773bd89a5e4c2583061fa24cd79f31d; current SHA256 369cae5270aeacd25a94317be3b005167773bd89a5e4c2583061fa24cd79f31d. Record bytes unchanged since the original review. |
| original-review-9 | reviews/structured/20261021T110938Z-cis-golgi-network-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| plaque-current-3 | data/structures/membrane_organelle/chloroplast_thylakoid.yaml; Complete maintained YAML at frozen source fa6c7f0034c57fac03d026ce0ddb8aaa4bd4b2e3; all fields, graphs, discussions and history | supports | Entire target independently inspected. Two added parthood edges and their evidence are substantively refreshed against current authorities. Native PROPOSED status is unchanged; no target image is declared. |
| plaque-original-3 | reviews/structured/20261021T110930Z-chloroplast-thylakoid-audit/review.yaml; Entire original authoritative YAML and Markdown; source hashes, findings, checks and assessments | supports | Original native validation and exact render passed; historical target bytes match the frozen hash. No original scientific finding exists. The old observation remains immutable rather than being silently relabeled current. |
| plaque-current-4 | data/structures/membrane_organelle/chloroplast_thylakoid_lumen.yaml; Complete maintained YAML at frozen source fa6c7f0034c57fac03d026ce0ddb8aaa4bd4b2e3; all fields, graphs, discussions and history | supports | Entire target independently inspected. Current target hash matches the original frozen target hash. Native PROPOSED status is unchanged; no target image is declared. |
| plaque-original-4 | reviews/structured/20261021T110931Z-chloroplast-thylakoid-lumen-audit/review.yaml; Entire original authoritative YAML and Markdown; source hashes, findings, checks and assessments | supports | Original native validation and exact render passed; historical target bytes match the frozen hash. No original scientific finding exists. The old observation remains immutable rather than being silently relabeled current. |
| plaque-current-5 | data/structures/membrane_organelle/chloroplast_thylakoid_membrane.yaml; Complete maintained YAML at frozen source fa6c7f0034c57fac03d026ce0ddb8aaa4bd4b2e3; all fields, graphs, discussions and history | supports | Entire target independently inspected. Current target hash matches the original frozen target hash. Native PROPOSED status is unchanged; no target image is declared. |
| plaque-original-5 | reviews/structured/20261021T110932Z-chloroplast-thylakoid-membrane-audit/review.yaml; Entire original authoritative YAML and Markdown; source hashes, findings, checks and assessments | supports | Original native validation and exact render passed; historical target bytes match the frozen hash. No original scientific finding exists. The old observation remains immutable rather than being silently relabeled current. |
| plaque-policy | .claude/skills/review-yaml-record/SKILL.md; Frozen native rules for evidence, component identity, assembly necessity, graph scope and structured-source applicability | context_only | The native contract separates scientific curation from review, material constitution from molecular necessity, and exact parthood from subclass identity. Actual source coverage must be assessed when molecular pathways are named. |
| plaque-rubric | .claude/skills/curate-yaml-record/references/review-checklist.md; Frozen native rules for evidence, component identity, assembly necessity, graph scope and structured-source applicability | context_only | The native contract separates scientific curation from review, material constitution from molecular necessity, and exact parthood from subclass identity. Actual source coverage must be assessed when molecular pathways are named. |
| plaque-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Frozen native rules for evidence, component identity, assembly necessity, graph scope and structured-source applicability | context_only | The native contract separates scientific curation from review, material constitution from molecular necessity, and exact parthood from subclass identity. Actual source coverage must be assessed when molecular pathways are named. |
| plaque-schema-policy | src/cellstructuremech/schema/cellstructuremech.yaml; Frozen native rules for evidence, component identity, assembly necessity, graph scope and structured-source applicability | context_only | The native contract separates scientific curation from review, material constitution from molecular necessity, and exact parthood from subclass identity. Actual source coverage must be assessed when molecular pathways are named. |
| plaque-thylakoid-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009534,GO:0009579,GO:0031976,GO:0009507,GO:0009535,GO:0009543,GO:0009570,GO:0009767,GO:0031978,GO:0042651,GO:0055035,GO:0019684; All12 requested GO terms: definitions, exact identifiers, comment and typed children; direct GO0009534 part_of children and GO0009507 whole-thylakoid partOf child inspected | supports | Current terms separate whole thylakoid0009534, membrane0009535 and lumen0009543. GO0009534 directly lists membrane and lumen as part_of children. Definitions and biological-process entries support the bounded topology and photosynthetic functions; the thylakoid comment supplies the record’s explicit non-organelle interpretation. |
| plaque-isa-0009534 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009534/ancestors?relations=is_a; Explicit relations=is_a endpoint and complete returned ancestor list | supports | The maintained broader plastid/generic thylakoid, lumen or membrane parents are in the is_a-only closure. Parthood is separately checked using typed relations; no partOf-to-isA substitution is made. |
| plaque-isa-0009543 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009543/ancestors?relations=is_a; Explicit relations=is_a endpoint and complete returned ancestor list | supports | The maintained broader plastid/generic thylakoid, lumen or membrane parents are in the is_a-only closure. Parthood is separately checked using typed relations; no partOf-to-isA substitution is made. |
| plaque-isa-0009535 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009535/ancestors?relations=is_a; Explicit relations=is_a endpoint and complete returned ancestor list | supports | The maintained broader plastid/generic thylakoid, lumen or membrane parents are in the is_a-only closure. Parthood is separately checked using typed relations; no partOf-to-isA substitution is made. |
| plaque-thylakoid-agent-SL-0056 | https://rest.uniprot.org/locations/SL-0056.json; Native definition, GO correspondence, immediate isA and partOf objects plus inherited hierarchy | supports | SL0056 identifies whole chloroplast thylakoid under plastid thylakoid and part of chloroplast. SL0057 and SL0058 directly name chloroplast thylakoid as partOf host, while their own isA parents are plastid lumen/membrane. The broader plastid-thylakoid relationship is inherited, not a different exact structure. The source’s single-lumen statement is explicitly qualified as thought, not proven here. |
| plaque-thylakoid-agent-SL-0057 | https://rest.uniprot.org/locations/SL-0057.json; Native definition, GO correspondence, immediate isA and partOf objects plus inherited hierarchy | supports | SL0056 identifies whole chloroplast thylakoid under plastid thylakoid and part of chloroplast. SL0057 and SL0058 directly name chloroplast thylakoid as partOf host, while their own isA parents are plastid lumen/membrane. The broader plastid-thylakoid relationship is inherited, not a different exact structure. The source’s single-lumen statement is explicitly qualified as thought, not proven here. |
| plaque-thylakoid-agent-SL-0058 | https://rest.uniprot.org/locations/SL-0058.json; Native definition, GO correspondence, immediate isA and partOf objects plus inherited hierarchy | supports | SL0056 identifies whole chloroplast thylakoid under plastid thylakoid and part of chloroplast. SL0057 and SL0058 directly name chloroplast thylakoid as partOf host, while their own isA parents are plastid lumen/membrane. The broader plastid-thylakoid relationship is inherited, not a different exact structure. The source’s single-lumen statement is explicitly qualified as thought, not proven here. |
| plaque-thylakoid-agent-NCBITaxon-33090 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/33090; Native taxId, scientificName, rank and lineage; not prevalence or experimental stock | supports | ENA confirms Viridiplantae kingdom33090. Occurrence and culture context require the independently inspected literature. |
| plaque-thylakoid-agent-NCBITaxon-3055 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3055; Native taxId, scientificName, rank and lineage; not prevalence or experimental stock | supports | ENA confirms Chlamydomonas reinhardtii species3055. Occurrence and culture context require the independently inspected literature. |
| plaque-thylakoid-agent-engel2015-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.7554%2FeLife.04889; Exact DOI query: title, authors, DOI/PMID/PMCID, publication type and complete abstract | supports | Native bibliography identifies Native architecture of the Chlamydomonas chloroplast revealed by in situ cryo-electron tomography.; Engel BD, Schaffer M, Kuhn Cuellar L, Villa E, Plitzko JM, Baumeister W.. This is bibliographic/abstract evidence; body coverage is declared separately. |
| plaque-thylakoid-agent-perez2024-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1146%2Fannurev-cellbio-120823-022747&amp;format=json&amp;resultType=core; Exact DOI query: title, authors, DOI/PMID/PMCID, publication type and complete abstract | supports | Native bibliography identifies Evolution of Thylakoid Structural Diversity.; Perez-Boerema A, Engel BD, Wietrzynski W.. This is bibliographic/abstract evidence; body coverage is declared separately. |
| plaque-thylakoid-agent-doi-10.1007_s00294-011-0339-1 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1007/s00294-011-0339-1; Exact DOI query: title, authors, DOI/PMID/PMCID, publication type and complete abstract | supports | Native bibliography identifies The chloroplast proteome: a survey from the Chlamydomonas reinhardtii perspective with a focus on distinctive features.; Terashima M, Specht M, Hippler M.. This is bibliographic/abstract evidence; body coverage is declared separately. |
| plaque-thylakoid-agent-doi-10.1098_rstb.2009.0103 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1098/rstb.2009.0103; Exact DOI query: title, authors, DOI/PMID/PMCID, publication type and complete abstract | supports | Native bibliography identifies The endosymbiotic origin, diversification and fate of plastids.; Keeling PJ.. This is bibliographic/abstract evidence; body coverage is declared separately. |
| plaque-thylakoid-agent-engel2015-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC4292175.1/PMC4292175.1.xml; Primary JATS: Introduction; Results s2-1,s2-2,s2-3; Discussion s3-1,s3-2; Methods s4-1 through s4-5. Included figure captions are text, not pixel or raw tomogram inspection. | supports | Engel2015 examines native C.reinhardtii CC-124(137c), grown in TAP under constant light, using cryo-FIB and in situ cryo-ET. The body supports membrane/lumen separation and variable stacked/interconnecting architecture. Confined tomograms do not prove one globally continuous lumen; rare envelope connections and proposed exchange/biogenesis routes remain bounded interpretations, not universal formation necessities. |
| plaque-thylakoid-agent-engel2015-correction | https://elifesciences.org/articles/11383; Complete publisher correction paragraph and linked original-paper identity | context_only | The correction changes the Figure3 scale-bar unit from micrometres to nanometres, retaining200nm. None of the three records asserts that image or a numerical dimension, so no maintained claim requires correction. |
| plaque-thylakoid-agent-terashima2011-pdf | https://link.springer.com/content/pdf/10.1007/s00294-011-0339-1.pdf; Actual %PDF body, printedpp151–156: Introduction and Photosynthesis section; extracted text through the section end before Chlorophyll biosynthesis. No figure-pixel, supplementary proteome or downstream metabolic-section audit. | supports | Terashima/Specht/Hippler2011 is a secondary review. It supports thylakoid photosynthetic core complexes, electron transfer and the pH gradient, with distinct algal/vascular-plant antennae and regulatory responses. Localization, sequence comparison and qE/state-transition perturbations do not establish a universal membrane-formation requirement or a complete constituent inventory. |
| plaque-thylakoid-agent-keeling2010-pmc | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2817223/; Actual secondary PMC HTML: abstract and §1 primary-plastid/green-lineage paragraphs; §6 distinction between loss of photosynthesis and plastid loss | supports | Keeling2010 supports broad green-lineage plastid context while explicitly distinguishing retained nonphotosynthetic plastids from plastid loss. It does not independently measure thylakoid prevalence or universal photosynthetic status. |
| plaque-thylakoid-agent-perez2024-publisher | https://www.annualreviews.org/content/journals/10.1146/annurev-cellbio-120823-022747; Actual unsuccessful native HTTP response; not scientific body content | context_only | Fresh native request returnedHTTP403. Successful separately scoped alternatives do not convert this response into article evidence. |
| plaque-thylakoid-agent-keeling2010-jats | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2817223/fullTextXML; Actual unsuccessful native HTTP response; not scientific body content | context_only | Fresh native request returnedHTTP500. Successful separately scoped alternatives do not convert this response into article evidence. |
| plaque-perez-body-introduction | https://doi.org/10.1146/annurev-cellbio-120823-022747; Cached browser-returned official publisher Introduction and evolutionary diversification paragraphs; unrelated hits excluded; packet hash below, not native body HTML | supports | Perez2024 secondary body context supports thylakoid membrane/lumen compartmentalization and qualitative photosynthetic green-lineage occurrence, not every nonphotosynthetic plastid or quantitative prevalence. Reused snapshot independently reread; original09:34/09:37Z capture time is retained, not claimed fresh. |
| plaque-perez-body-electron-transport | https://doi.org/10.1146/annurev-cellbio-120823-022747; Cached browser-returned official publisher Electron Transport Chain Complexes subsection only; packet hash below, not native body HTML | supports | The secondary review locates photosystems, quinone/soluble carriers and gradient-coupled ATP production at the membrane/lumen/stroma interfaces. It supports the broad functional claims without imposing a universal experimentally necessary protein inventory. Reused snapshot independently reread; original09:34/09:37Z capture time is retained, not claimed fresh. |
| plaque-catalogue | https://imodulondb.org/api/datasets; Entire current /api/datasets response, all returned organism/dataset rows; no pagination | supports | No current catalogue organism matches Chlamydomonas or the records’ green-lineage plastid hosts. The S.elongatus dataset is a different cyanobacterial organism and cannot supply chloroplast-thylakoid molecular evidence. Downstream gene/module queries are therefore not applicable; absence from the catalogue is not biological absence. |
| plaque-historical-runner | /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources imodulondb datasets; Historical00:49Z receipt and stdout/stderr independently reread and hash-verified | context_only | Historical runner exited1 before dataset execution due OS PermissionError reading pyvenv.cfg. No fresh runner invocation or success is claimed. Current source catalogue is the separately inspected permitted fallback. |
| plaque-native-chloroplast_thylakoid-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chloroplast_thylakoid.yaml --verify; Actual root-owned receipt and exact stdout independently read and hash-verified | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| plaque-native-chloroplast_thylakoid-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chloroplast_thylakoid.yaml --causal-graphs; Actual root-owned receipt and exact stdout independently read and hash-verified | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| plaque-native-chloroplast_thylakoid_lumen-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chloroplast_thylakoid_lumen.yaml --verify; Actual root-owned receipt and exact stdout independently read and hash-verified | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| plaque-native-chloroplast_thylakoid_lumen-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chloroplast_thylakoid_lumen.yaml --causal-graphs; Actual root-owned receipt and exact stdout independently read and hash-verified | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| plaque-native-chloroplast_thylakoid_membrane-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chloroplast_thylakoid_membrane.yaml --verify; Actual root-owned receipt and exact stdout independently read and hash-verified | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| plaque-native-chloroplast_thylakoid_membrane-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chloroplast_thylakoid_membrane.yaml --causal-graphs; Actual root-owned receipt and exact stdout independently read and hash-verified | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| micro-review-policy | .claude/skills/review-yaml-record/SKILL.md; Evidence Rules; Structured Source Cross-Checks; Missing Things; Workflow | supports | Native named-gene, protein and pathway claims trigger applicability assessment irrespective of transcriptomic assertions. Source absence must be bounded. No record or immutable review mutation is authorized for this independent pass. |
| micro-review-config | conf/record_review.yaml; Active skills and rubric routes | supports | Configuration, native review skill, review profile and output contract reread. Seventeen common policy/schema/verifier inputs are byte-identical to the previous reviewed cohort; their prior contract interpretation is retained with current critical rule checks. |
| micro-review-profile | docs/record-review-profile.md; Issue-only persistence; Native questions; Native checks | supports | Issue-bearing successor may document clean refreshed claims alongside preserved unresolved findings. Native QC and source verification do not by themselves certify the scientific assertions. |
| micro-schema-necessity | src/cellstructuremech/schema/cellstructuremech.yaml; EssentialityEnum.ESSENTIAL; CausalNode.component_ref | supports | ESSENTIAL means the structure does not form without the component. A graph component_ref denotes the local own component; constituent identity, function, viability and organelle-formation necessity remain distinct. |
| micro-graph-contract | .claude/skills/curate-causal-graphs/SKILL.md; Node identity, component links and edge-level claim scope | supports | A multi-protein baseplate is a structure node. Coarse topological or energy-flow edges do not establish molecular completeness, direct universal contacts or formation necessity. |
| micro-review-schema | schema/record_review.yaml; EvidenceKind; Area; FindingReference; Action | supports | Secondary review context uses authority with explicit scope, schema is a valid assessment area, and successor findings require exact repository/review/finding lineage. |
| micro-original-validation-inputs | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/adversary-microtubule/original-validation-inputs.json; Three original validate commands, native render --content comparisons, original-source and current target blob hashes | supports | All three original bundles validate and render byte-identically. Original target hashes match git source9c0446c4. Chlorosome and envelope are stale; cis-Golgi target is unchanged. These results do not convert old full-corpus checks into current checks. |
| micro-record-chlorosome | data/structures/membrane_organelle/chlorosome.yaml; Complete current target YAML at fa6c7f0034c57fac03d026ce0ddb8aaa4bd4b2e3 | supports | Entire record inspected: identity, definition, scope, components, protein examples, functions, taxon/canonical examples, graph, evidence, discussions and history. Current target differs from the original frozen record. |
| micro-prior-chlorosome | reviews/structured/20261021T110934Z-chlorosome-audit/review.yaml; Entire immutable original YAML plus deterministic Markdown | supports | Retained original 20261021T110934Z-chlorosome-audit; verdict needs_curation. Original source access dates and check provenance remain historical. Exact finding keys and occurrences are preserved in this report. |
| micro-native-chlorosome-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/chlorosome-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chlorosome.yaml --verify; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/chlorosome-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0 at source fa6c7f0034c57fac03d026ce0ddb8aaa4bd4b2e3, 2026-11-03T10:11:24.680580+00:00 to 2026-11-03T10:11:25.935969+00:00. Ten declared examples (seven reviewed, three unreviewed); causal graph has one PARTIAL_EXAMPLES accessory node (csmK lacks example) and one UNANCHORED_NO_UNIPROT generic reaction-center acceptor node. Corrected whole baseplate is STRUCTURE, not a missing protein example. Identity/coverage success does not establish localization or necessity. |
| micro-native-chlorosome-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/chlorosome-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chlorosome.yaml --causal-graphs; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/chlorosome-uniprot-causal.log SHA256 c0b932b8875cdd028d1ca4ea4becedf1ee85d19859fdfcb5d5e0c7803d07df42 | supports | Actual exit0 at source fa6c7f0034c57fac03d026ce0ddb8aaa4bd4b2e3, 2026-11-03T10:11:25.966660+00:00 to 2026-11-03T10:11:26.357757+00:00. Ten declared examples (seven reviewed, three unreviewed); causal graph has one PARTIAL_EXAMPLES accessory node (csmK lacks example) and one UNANCHORED_NO_UNIPROT generic reaction-center acceptor node. Corrected whole baseplate is STRUCTURE, not a missing protein example. Identity/coverage success does not establish localization or necessity. |
| micro-record-chlorosome_envelope | data/structures/membrane_organelle/chlorosome_envelope.yaml; Complete current target YAML at fa6c7f0034c57fac03d026ce0ddb8aaa4bd4b2e3 | supports | Entire record inspected: identity, definition, scope, components, protein examples, functions, taxon/canonical examples, graph, evidence, discussions and history. Current target differs from the original frozen record. |
| micro-prior-chlorosome_envelope | reviews/structured/20261021T110935Z-chlorosome-envelope-audit/review.yaml; Entire immutable original YAML plus deterministic Markdown | supports | Retained original 20261021T110935Z-chlorosome-envelope-audit; verdict needs_curation. Original source access dates and check provenance remain historical. Exact finding keys and occurrences are preserved in this report. |
| micro-native-chlorosome_envelope-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/chlorosome_envelope-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chlorosome_envelope.yaml --verify; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/chlorosome_envelope-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0 at source fa6c7f0034c57fac03d026ce0ddb8aaa4bd4b2e3, 2026-11-03T10:11:26.389963+00:00 to 2026-11-03T10:11:27.380720+00:00. Ten declared examples (seven reviewed, three unreviewed); causal graph has one PARTIAL_EXAMPLES node because csmK lacks an example. Corrected baseplate structure node is not a protein inventory failure. Identity/coverage success does not establish localization or necessity. |
| micro-native-chlorosome_envelope-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/chlorosome_envelope-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chlorosome_envelope.yaml --causal-graphs; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/chlorosome_envelope-uniprot-causal.log SHA256 ce8445ca91d5abe4081756fe74beeb343e3acae44afb278945b3a29269f0f495 | supports | Actual exit0 at source fa6c7f0034c57fac03d026ce0ddb8aaa4bd4b2e3, 2026-11-03T10:11:27.412651+00:00 to 2026-11-03T10:11:27.794962+00:00. Ten declared examples (seven reviewed, three unreviewed); causal graph has one PARTIAL_EXAMPLES node because csmK lacks an example. Corrected baseplate structure node is not a protein inventory failure. Identity/coverage success does not establish localization or necessity. |
| micro-record-cis_golgi_network | data/structures/membrane_organelle/cis_golgi_network.yaml; Complete current target YAML at fa6c7f0034c57fac03d026ce0ddb8aaa4bd4b2e3 | supports | Entire record inspected: identity, definition, scope, components, protein examples, functions, taxon/canonical examples, graph, evidence, discussions and history. Target is byte-identical to the original frozen record. |
| micro-prior-cis_golgi_network | reviews/structured/20261021T110938Z-cis-golgi-network-audit/review.yaml; Entire immutable original YAML plus deterministic Markdown | supports | Retained original 20261021T110938Z-cis-golgi-network-audit; verdict needs_curation. Original source access dates and check provenance remain historical. Exact finding keys and occurrences are preserved in this report. |
| micro-native-cis_golgi_network-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/cis_golgi_network-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cis_golgi_network.yaml --verify; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/cis_golgi_network-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0 at source fa6c7f0034c57fac03d026ce0ddb8aaa4bd4b2e3, 2026-11-03T10:11:28.619985+00:00 to 2026-11-03T10:11:28.977247+00:00. Empty protein-example inventory and zero GENE_OR_PROTEIN nodes; successful empty-scope command is not experimental molecular evidence. Identity/coverage success does not establish localization or necessity. |
| micro-native-cis_golgi_network-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/cis_golgi_network-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cis_golgi_network.yaml --causal-graphs; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/cis_golgi_network-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Actual exit0 at source fa6c7f0034c57fac03d026ce0ddb8aaa4bd4b2e3, 2026-11-03T10:11:29.007528+00:00 to 2026-11-03T10:11:29.366997+00:00. Empty protein-example inventory and zero GENE_OR_PROTEIN nodes; successful empty-scope command is not experimental molecular evidence. Identity/coverage success does not establish localization or necessity. |
| micro-neighbor-baseplate | data/structures/energy_complex/chlorosome_baseplate_antenna_complex.yaml; Identity, definition, parentage, components, canonical example, graph and discussions | supports | Frozen whole CsmA/BChl-a multi-protein baseplate identity supports corrected STRUCTURE nodes and internal grounding. This neighbor is boundary context only; its separately tracked mutant-preparation claim is not re-reviewed or resolved here. |
| micro-neighbor-cgn-membrane | data/structures/membrane_organelle/cis_golgi_network_membrane.yaml; Identity, definition, hierarchy/parthood, synonyms and discussions | supports | Exact GO:0033106 boundary is distinct from the complete GO:0005801 network and generic lipid material; molecular residents are not inferred from the boundary. |
| micro-neighbor-golgi | data/structures/membrane_organelle/golgi_apparatus.yaml; Identity, definition, hierarchy/parthood, has_part and discussions | supports | Whole Golgi, stack and CGN are distinct structure scopes. Neighbor used only for boundary consistency, not a full scientific review or category-wide disposition. |
| micro-chl-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0046858,GO:0043232,GO:0033105,GO:0015979; Exact QuickGO GO:0046858/0033105/0043232/0015979 definitions, names, synonyms, active flags and child relations | supports | Chlorosome is a pigment aggregate with monolayer envelope, correctly distinguished from a lipid bilayer-bounded organelle. Envelope is not an organelle membrane/envelope bilayer; photosynthesis is broader than antenna light harvesting. |
| micro-chl-SL-0060 | https://rest.uniprot.org/locations/SL-0060.json; UniProt SL-0060 identity, definition, synonyms, GO mapping and chlorosome parthood | supports | Chlorosomal envelope is an exact synonym; asymmetric glycolipid monolayer with pigment tails differs from a bilayer. Authority description is not proof of necessity for a particular lipid species. |
| micro-chl-tax-2 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2; ENA taxonomy exact taxId/scientificName/rank/lineage/otherNames | supports | Current authority identifies 2 as Bacteria. Species and strain scope are retained; historical Pichia naming is not used as a current strain identity bridge. |
| micro-chl-tax-1097 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1097; ENA taxonomy exact taxId/scientificName/rank/lineage/otherNames | supports | Current authority identifies 1097 as Chlorobaculum tepidum. Species and strain scope are retained; historical Pichia naming is not used as a current strain identity bridge. |
| micro-chl-tax-1108 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1108; ENA taxonomy exact taxId/scientificName/rank/lineage/otherNames | supports | Current authority identifies 1108 as Chloroflexus aurantiacus. Species and strain scope are retained; historical Pichia naming is not used as a current strain identity bridge. |
| micro-chl-tax-194439 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/194439; ENA taxonomy exact taxId/scientificName/rank/lineage/otherNames | supports | Current authority identifies 194439 as Chlorobaculum tepidum TLS. Species and strain scope are retained; historical Pichia naming is not used as a current strain identity bridge. |
| micro-cis-tax-4922 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4922; ENA taxonomy exact taxId/scientificName/rank/lineage/otherNames | supports | Current authority identifies 4922 as Komagataella pastoris. Species and strain scope are retained; historical Pichia naming is not used as a current strain identity bridge. |
| micro-cis-tax-460519 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/460519; ENA taxonomy exact taxId/scientificName/rank/lineage/otherNames | supports | Current authority identifies 460519 as Komagataella phaffii. Species and strain scope are retained; historical Pichia naming is not used as a current strain identity bridge. |
| micro-chl-nielsen2016-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC4992139.1/PMC4992139.1.xml; DOI10.1038/ncomms12454; complete Introduction, all Results, complete Discussion and Methods Sample preparation | supports | Genuine JATS. bchK-mutant carotenosomes retain an intact CsmA/BChl-a baseplate; wild-type/mutant comparison and NMR/cryo-EM/spectroscopy resolve organization. Introduction positively attributes structural integrity, attachment and energy-transfer roles. It does not remove the baseplate to test chlorosome formation. AFM dimensions are earlier-work comparisons; no raw data, figures or supplement reanalysis. |
| micro-frigaard2004 | https://rcn.montana.edu/Publications/Pdf/2004/2004%20Frigaard%20et%20al.%20csm.%20J.%20Bacteriol.pdf; DOI10.1128/JB.186.3.646-653.2004; PDF pp646-652 Abstract, growth/construct Methods, Results Construction of csm mutants, biochemical characterizations and Discussion | supports | Fresh genuine primary PDF. csmA transformants remain merodiploid under tested conditions; author inference concerns essential light harvesting. Nine non-CsmA single mutants form functional chlorosomes with bounded morphology/pigment changes. This is neither a direct CsmA-loss formation assay nor universal cohort dispensability. |
| micro-psencik2009-retained-body | https://pmc.ncbi.nlm.nih.gov/articles/PMC2795307/; DOI10.1128/JB.00690-09; Methods; Results Cryo-EM, Tomographic reconstruction and X-ray scattering; Discussion Overall shape, Parallel striation, Perpendicular striation and Summary | supports | Retained genuine PMC body fetched04:31:37Z, reread for this cohort. C. aurantiacus J-10-fl culture and chlorosome imaging/scattering support canonical occurrence, lamellar pigments and crystalline baseplate. Dimer assignment is a scoped inference; projection versus tomogram resolution and contaminating-bilayer scattering are distinguished. No fresh body-fetch success or pixel audit claimed. |
| micro-chl-oostergetel2010-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC2882566.1/PMC2882566.1.xml; DOI10.1007/s11120-010-9533-0; secondary review abstract, Introduction Sec1, Chlorosomes Sec2 and Organization of the baseplate Sec5 | context_only | Secondary synthesis supplies limited phototroph distribution, self-assembled pigment and antenna/baseplate context. FMO coupling is green-sulfur-bacterial context, not universal acceptor identity. This is not a newly performed primary experiment. |
| micro-orf2013-browser | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/adversary-microtubule/orf-browser-capture.json; Author-uploaded Orf2013 secondary article; Introduction and protein/baseplate section pp322-323, browser lines1200-1389; reference https://www.researchgate.net/publication/237199940_Chlorosome_Antenna_Complexes_from_Green_Photosynthetic_Bacteria | context_only | Actual browser-readable secondary body supports surface Csm localization, up-to-eleven proteins, distinct motif groups and lineage variability. Native direct body returned403 and publisher/PDF routes challenge HTML. The new edge is accepted only as surface localization, not universal protein membership, necessity or a complete assembly mechanism. |
| micro-chl-li2006-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1021%2Fbi060776y&amp;format=json&amp;resultType=core; DOI10.1021/bi060776y; exact metadata and complete abstract only | partial | Complete primary abstract reports cross-linking in C. tepidum and mutant controls, CsmA oligomer/FMO interactions and a proposed envelope-contact model. It supports the named cohort/localization scope but is not a full Methods audit. |
| micro-chl-frigaard2005-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1007/s11120-005-1331-8&amp;format=json&amp;resultType=core; DOI10.1007/s11120-005-1331-8; exact metadata and complete abstract only | partial | Complete primary abstract distinguishes bchK-mutant vestigial carotenosomes from normal BChl-c chlorosomes; intact CsmA/BChl-a baseplate and flattened morphology do not establish baseplate-removal dispensability. |
| micro-chl-orf2013-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1007/s11120-013-9869-3; Exact DOI metadata and complete abstract: 10.1007/s11120-013-9869-3 | context_only | Verified title/DOI/organism and abstract access: Chlorosome antenna complexes from green photosynthetic bacteria.. Claim-bearing primary body or secondary-context evidence is separately scoped above. |
| micro-chl-oostergetel2010-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1007/s11120-010-9533-0; Exact DOI metadata and complete abstract: 10.1007/s11120-010-9533-0 | context_only | Verified title/DOI/organism and abstract access: The chlorosome: a prototype for efficient light harvesting in photosynthesis.. Claim-bearing primary body or secondary-context evidence is separately scoped above. |
| micro-chl-psencik2009-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1128/JB.00690-09; Exact DOI metadata and complete abstract: 10.1128/jb.00690-09 | context_only | Verified title/DOI/organism and abstract access: Structure of chlorosomes from the green filamentous bacterium Chloroflexus aurantiacus.. Claim-bearing primary body or secondary-context evidence is separately scoped above. |
| micro-chl-nielsen2016-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1038/ncomms12454; Exact DOI metadata and complete abstract: 10.1038/ncomms12454 | context_only | Verified title/DOI/organism and abstract access: In situ high-resolution structure of the baseplate antenna complex in Chlorobaculum tepidum.. Claim-bearing primary body or secondary-context evidence is separately scoped above. |
| micro-chl-frigaard2004-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128%2FJB.186.3.646-653.2004&amp;format=json&amp;resultType=core; Exact DOI metadata and complete abstract: 10.1128/jb.186.3.646-653.2004 | context_only | Verified title/DOI/organism and abstract access: Nine mutants of Chlorobium tepidum each unable to synthesize a different chlorosome protein still assemble functional chlorosomes.. Claim-bearing primary body or secondary-context evidence is separately scoped above. |
| micro-chl-P0A314 | https://rest.uniprot.org/uniprotkb/P0A314.json; UniProtKB exact accession; primaryAccession, entryType, organism, genes and proteinDescription | supports | P0A314 is UniProtKB reviewed (Swiss-Prot); gene csmA in taxon194439 C. tepidum TLS. Exact identity/status and locus support only; database names do not override experimental BChl-a baseplate specificity or establish universal localization/necessity. |
| micro-chl-matches-P0A314 | https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/P0A314/; InterPro integrated/member entry matches for exact UniProt P0A314; entire returned page; next=None | context_only | Bounded accession match inventory: G3DSA:1.20.5.950 homologous_superfamily bacteriochlorophyll c-binding protein; IPR001470 family Bacteriochlorophyll c-binding protein; IPR038387 homologous_superfamily Bacteriochlorophyll c-binding superfamily; PF02043 family Bacteriochlorophyll C binding protein; PIRSF002903 family Chlorosome protein, CsmA/CsmE types; PR00656 family BCHLROPHYLLC. Subgroup/domain matches do not denote the heterogeneous accessory Csm set or whole protein-pigment baseplate. Empty response is not proof of no family. |
| micro-chl-Q46383 | https://rest.uniprot.org/uniprotkb/Q46383.json; UniProtKB exact accession; primaryAccession, entryType, organism, genes and proteinDescription | supports | Q46383 is UniProtKB reviewed (Swiss-Prot); gene csmB in taxon194439 C. tepidum TLS. Exact identity/status and locus support only; database names do not override experimental BChl-a baseplate specificity or establish universal localization/necessity. |
| micro-chl-matches-Q46383 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q46383/?page_size=200; InterPro integrated/member entry matches for exact UniProt Q46383; entire returned page; next=None | context_only | Bounded accession match inventory: IPR059980 family CsmB chlorosome envelope protein. Subgroup/domain matches do not denote the heterogeneous accessory Csm set or whole protein-pigment baseplate. Empty response is not proof of no family. |
| micro-chl-Q46367 | https://rest.uniprot.org/uniprotkb/Q46367.json; UniProtKB exact accession; primaryAccession, entryType, organism, genes and proteinDescription | supports | Q46367 is UniProtKB reviewed (Swiss-Prot); gene csmC in taxon194439 C. tepidum TLS. Exact identity/status and locus support only; database names do not override experimental BChl-a baseplate specificity or establish universal localization/necessity. |
| micro-chl-matches-Q46367 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q46367/?page_size=200; InterPro integrated/member entry matches for exact UniProt Q46367; entire returned page; next=None | context_only | Bounded accession match inventory: IPR020995 family Chlorosome envelope protein C. Subgroup/domain matches do not denote the heterogeneous accessory Csm set or whole protein-pigment baseplate. Empty response is not proof of no family. |
| micro-chl-Q46386 | https://rest.uniprot.org/uniprotkb/Q46386.json; UniProtKB exact accession; primaryAccession, entryType, organism, genes and proteinDescription | supports | Q46386 is UniProtKB reviewed (Swiss-Prot); gene csmE in taxon194439 C. tepidum TLS. Exact identity/status and locus support only; database names do not override experimental BChl-a baseplate specificity or establish universal localization/necessity. |
| micro-chl-matches-Q46386 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q46386/?page_size=200; InterPro integrated/member entry matches for exact UniProt Q46386; entire returned page; next=None | context_only | Bounded accession match inventory: IPR001470 family Bacteriochlorophyll c-binding protein; IPR038387 homologous_superfamily Bacteriochlorophyll c-binding superfamily. Subgroup/domain matches do not denote the heterogeneous accessory Csm set or whole protein-pigment baseplate. Empty response is not proof of no family. |
| micro-chl-O68986 | https://rest.uniprot.org/uniprotkb/O68986.json; UniProtKB exact accession; primaryAccession, entryType, organism, genes and proteinDescription | supports | O68986 is UniProtKB reviewed (Swiss-Prot); gene csmF in taxon194439 C. tepidum TLS. Exact identity/status and locus support only; database names do not override experimental BChl-a baseplate specificity or establish universal localization/necessity. |
| micro-chl-matches-O68986 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/O68986/?page_size=200; InterPro integrated/member entry matches for exact UniProt O68986; entire returned page; next=None | context_only | Bounded accession match inventory: IPR059980 family CsmB chlorosome envelope protein. Subgroup/domain matches do not denote the heterogeneous accessory Csm set or whole protein-pigment baseplate. Empty response is not proof of no family. |
| micro-chl-O68988 | https://rest.uniprot.org/uniprotkb/O68988.json; UniProtKB exact accession; primaryAccession, entryType, organism, genes and proteinDescription | supports | O68988 is UniProtKB reviewed (Swiss-Prot); gene csmI in taxon194439 C. tepidum TLS. Exact identity/status and locus support only; database names do not override experimental BChl-a baseplate specificity or establish universal localization/necessity. |
| micro-chl-matches-O68988 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/O68988/?page_size=200; InterPro integrated/member entry matches for exact UniProt O68988; entire returned page; next=None | context_only | Bounded accession match inventory: IPR001041 domain 2Fe-2S ferredoxin-type iron-sulfur binding domain; IPR001055 family Adrenodoxin-like; IPR012675 homologous_superfamily Beta-grasp domain superfamily; IPR036010 homologous_superfamily 2Fe-2S ferredoxin-like superfamily. Subgroup/domain matches do not denote the heterogeneous accessory Csm set or whole protein-pigment baseplate. Empty response is not proof of no family. |
| micro-chl-O68983 | https://rest.uniprot.org/uniprotkb/O68983.json; UniProtKB exact accession; primaryAccession, entryType, organism, genes and proteinDescription | supports | O68983 is UniProtKB reviewed (Swiss-Prot); gene csmJ in taxon194439 C. tepidum TLS. Exact identity/status and locus support only; database names do not override experimental BChl-a baseplate specificity or establish universal localization/necessity. |
| micro-chl-matches-O68983 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/O68983/?page_size=200; InterPro integrated/member entry matches for exact UniProt O68983; entire returned page; next=None | context_only | Bounded accession match inventory: IPR001041 domain 2Fe-2S ferredoxin-type iron-sulfur binding domain; IPR001055 family Adrenodoxin-like; IPR012675 homologous_superfamily Beta-grasp domain superfamily; IPR036010 homologous_superfamily 2Fe-2S ferredoxin-like superfamily. Subgroup/domain matches do not denote the heterogeneous accessory Csm set or whole protein-pigment baseplate. Empty response is not proof of no family. |
| micro-chl-H2VFJ4 | https://rest.uniprot.org/uniprotkb/H2VFJ4.json; UniProtKB exact accession; primaryAccession, entryType, organism, genes and proteinDescription | supports | H2VFJ4 is UniProtKB unreviewed (TrEMBL); gene csmD in taxon194439 C. tepidum TLS. Exact identity/status and locus support only; database names do not override experimental BChl-a baseplate specificity or establish universal localization/necessity. |
| micro-chl-matches-H2VFJ4 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/H2VFJ4/?page_size=200; InterPro integrated/member entry matches for exact UniProt H2VFJ4; entire returned page; next=None | context_only | Bounded accession match inventory: HTTP204 empty response. Subgroup/domain matches do not denote the heterogeneous accessory Csm set or whole protein-pigment baseplate. Empty response is not proof of no family. |
| micro-chl-H2VFJ1 | https://rest.uniprot.org/uniprotkb/H2VFJ1.json; UniProtKB exact accession; primaryAccession, entryType, organism, genes and proteinDescription | supports | H2VFJ1 is UniProtKB unreviewed (TrEMBL); gene csmH in taxon194439 C. tepidum TLS. Exact identity/status and locus support only; database names do not override experimental BChl-a baseplate specificity or establish universal localization/necessity. |
| micro-chl-matches-H2VFJ1 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/H2VFJ1/?page_size=200; InterPro integrated/member entry matches for exact UniProt H2VFJ1; entire returned page; next=None | context_only | Bounded accession match inventory: IPR017845 repeat Chlorosome envelope protein H, CsmH; IPR040561 domain Large polyvalent protein associated domain 38. Subgroup/domain matches do not denote the heterogeneous accessory Csm set or whole protein-pigment baseplate. Empty response is not proof of no family. |
| micro-chl-Q8KEN5 | https://rest.uniprot.org/uniprotkb/Q8KEN5.json; UniProtKB exact accession; primaryAccession, entryType, organism, genes and proteinDescription | supports | Q8KEN5 is UniProtKB unreviewed (TrEMBL); gene csmX in taxon194439 C. tepidum TLS. Exact identity/status and locus support only; database names do not override experimental BChl-a baseplate specificity or establish universal localization/necessity. |
| micro-chl-matches-Q8KEN5 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q8KEN5/?page_size=200; InterPro integrated/member entry matches for exact UniProt Q8KEN5; entire returned page; next=None | context_only | Bounded accession match inventory: IPR001041 domain 2Fe-2S ferredoxin-type iron-sulfur binding domain; IPR001055 family Adrenodoxin-like; IPR012675 homologous_superfamily Beta-grasp domain superfamily; IPR036010 homologous_superfamily 2Fe-2S ferredoxin-like superfamily. Subgroup/domain matches do not denote the heterogeneous accessory Csm set or whole protein-pigment baseplate. Empty response is not proof of no family. |
| micro-chl-reviewed-csm-query | https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A194439+AND+%28gene_exact%3AcsmA+OR+gene_exact%3AcsmB+OR+gene_exact%3AcsmC+OR+gene_exact%3AcsmD+OR+gene_exact%3AcsmE+OR+gene_exact%3AcsmF+OR+gene_exact%3AcsmH+OR+gene_exact%3AcsmI+OR+gene_exact%3AcsmJ+OR+gene_exact%3AcsmK+OR+gene_exact%3AcsmX%29&amp;format=json&amp;size=500; Exact UniProt search response and pagination headers | supports | Seven reviewed entries match the queried eleven symbols in TLS. Three declared unreviewed examples are separately verified; reviewed status is not invented for them. |
| micro-chl-csmK-query | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AcsmK&amp;format=json&amp;size=500; Exact UniProt search response and pagination headers | supports | No entry returned for the literal csmK gene query. This is a bounded naming-query result, not evidence that CsmK or its family does not exist. |
| micro-cis-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005783,GO:0005794,GO:0005801,GO:0033106,GO:0098791; QuickGO exact GO:0005801/0033106/0005794/0098791/0005783 active terms, definitions, synonyms, comments and children | supports | CGN is an ER-abutting network distinct from its membrane and whole Golgi; current GO explicitly says CGN is not part of the Golgi stack. Broader cis-face synonyms are not exact identities. |
| micro-cis-jats-PMC2148216 | https://pmc-oa-opendata.s3.amazonaws.com/PMC2148216.1/PMC2148216.1.xml; DOI10.1083/jcb.145.1.69; Methods Strains and Plasmids, complete Results and complete Discussion; text only | supports | PPY1/PPY12 experiments establish coherent Golgi stacks adjacent to transitional ER. Sec13-positive tubulovesicular interface is interpreted as tER; Och1/late-marker apposition does not independently identify a distinct CGN. Whole primary narrative does not establish absence of CGN. No raw micrograph/pixel audit or full supplementary analysis. |
| micro-cis-atcc-204163 | https://www.atcc.org/products/204163; ATCC204163 product identity, Strain designation PPY12, Genotype his4 arg4, Characteristics Comments | supports | PPY12 is K. phaffii; ATCC explicitly describes the change from K. pastoris based on in-house sequence analysis. This is a strain identity bridge, not evidence of organelle occurrence. |
| micro-cis-ena-LC815816 | https://www.ebi.ac.uk/ena/browser/api/embl/LC815816.1?download=false; ENA LC815816.1 EMBL FT source qualifiers organism/strain/db_xref | supports | Source qualifiers identify Komagataella phaffii PPY12, taxon460519. Corroborates the strain bridge independently of historical name; ATG14 sequence is not evidence of CGN membership/function. |
| micro-cis-cho2000-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1016/S0014-5793%2800%2901268-0%22; DOI10.1016/S0014-5793(00)01268-0; exact metadata and complete primary abstract only | partial | S. cerevisiae Sed5 membrane immunoisolation enriches early-Golgi mannosyltransferases and excludes late-Golgi/ER markers. This limited abstract does not establish K. pastoris/phaffii CGN occurrence or universally essential resident proteins; both publisher body/PDF attempts403. |
| micro-adapter-catalogue | https://imodulondb.org/api/datasets; Full iModulonDB API organism/dataset catalogue; all returned rows | supports | No Chlorobaculum/Chlorobium, Chloroflexus, Komagataella/Pichia or Saccharomyces covered dataset was returned. Thus no matched target gene/module summary is justified; catalogue absence is not negative biological evidence. |
| micro-historical-adapter-runner | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Retained earlier kg-microbe-sources imodulondb datasets invocation; actual stdout/stderr hashes and PermissionError | context_only | Historical00:49Z runner failed with PermissionError opening pyvenv.cfg; actual exit1 retained as historical unavailable evidence. It is not a new invocation or success. Current catalogue fallback was inspected separately. |
| septin-review-policy | .claude/skills/review-yaml-record/SKILL.md; Structured Source Cross-Checks and immutable review workflow | supports | Actual named molecular or pathway assertions trigger applicability; absence of expression claims does not exempt them. Truly sparse topology scope need not invent a molecular query. Unmatched organisms permit bounded downstream non-applicability. |
| septin-curation-policy | docs/CURATION.md; Identity, components, source scope and necessity | supports | Structure identity, material composition, proteins and empirical formation dependency are distinct; a spatial region need not assert a complete invariant molecular inventory. |
| septin-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; NONMECHANISTIC graph scope | supports | Descriptive constitution, identity and spatial relations may be explicitly nonmechanistic; biological process endpoints are distinct from the containing compartment. |
| septin-record-chloroplast_membrane | data/structures/membrane_organelle/chloroplast_membrane.yaml; Entire current maintained record at fa6c7f0034c57fac03d026ce0ddb8aaa4bd4b2e3 | supports | Full record identity, synonyms, history, boundaries, components where present, taxonomic examples, functions, evidence, graph and discussions read. No attached image or verbatim snippet is declared. |
| septin-original-chloroplast_membrane | reviews/structured/20261021T110921Z-chloroplast-membrane-audit/review.yaml; Entire original YAML/Markdown pair; claims, checks, evidence tiers and verdict | supports | Original pass_with_limitations has no findings or curation actions. Historical source access and checks remain historical, not newly executed. |
| septin-original-validation-chloroplast_membrane | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/adversary-septin/original-checks.json; 20261021T110921Z-chloroplast-membrane-audit native validate/render and source/current hash comparison | supports | Validation and render exit0; deterministic Markdown is byte-identical. Original source revision, original frozen target hash and current target bytes match. |
| septin-native-chloroplast_membrane-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/chloroplast_membrane-uniprot-verify-receipt.json; Actual root-run receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/chloroplast_membrane-uniprot-verify.log | supports | Exit0 at 2026-11-03T10:11:19.993371+00:00. No protein_examples, UniProtKB protein xrefs or GENE_OR_PROTEIN graph nodes are declared. The causal inventory has zero typed protein nodes; success does not validate molecules mentioned in prose, localization, mechanism or formation necessity. |
| septin-native-chloroplast_membrane-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/chloroplast_membrane-uniprot-causal-receipt.json; Actual root-run receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/chloroplast_membrane-uniprot-causal.log | supports | Exit0 at 2026-11-03T10:11:20.413148+00:00. No protein_examples, UniProtKB protein xrefs or GENE_OR_PROTEIN graph nodes are declared. The causal inventory has zero typed protein nodes; success does not validate molecules mentioned in prose, localization, mechanism or formation necessity. |
| septin-record-chloroplast_outer_membrane | data/structures/membrane_organelle/chloroplast_outer_membrane.yaml; Entire current maintained record at fa6c7f0034c57fac03d026ce0ddb8aaa4bd4b2e3 | supports | Full record identity, synonyms, history, boundaries, components where present, taxonomic examples, functions, evidence, graph and discussions read. No attached image or verbatim snippet is declared. |
| septin-original-chloroplast_outer_membrane | reviews/structured/20261021T110923Z-chloroplast-outer-membrane-audit/review.yaml; Entire original YAML/Markdown pair; claims, checks, evidence tiers and verdict | supports | Original pass_with_limitations has no findings or curation actions. Historical source access and checks remain historical, not newly executed. |
| septin-original-validation-chloroplast_outer_membrane | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/adversary-septin/original-checks.json; 20261021T110923Z-chloroplast-outer-membrane-audit native validate/render and source/current hash comparison | supports | Validation and render exit0; deterministic Markdown is byte-identical. Original source revision, original frozen target hash and current target bytes match. |
| septin-native-chloroplast_outer_membrane-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/chloroplast_outer_membrane-uniprot-verify-receipt.json; Actual root-run receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/chloroplast_outer_membrane-uniprot-verify.log | supports | Exit0 at 2026-11-03T10:11:20.823917+00:00. No protein_examples, UniProtKB protein xrefs or GENE_OR_PROTEIN graph nodes are declared. The causal inventory has zero typed protein nodes; success does not validate molecules mentioned in prose, localization, mechanism or formation necessity. |
| septin-native-chloroplast_outer_membrane-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/chloroplast_outer_membrane-uniprot-causal-receipt.json; Actual root-run receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/chloroplast_outer_membrane-uniprot-causal.log | supports | Exit0 at 2026-11-03T10:11:21.234089+00:00. No protein_examples, UniProtKB protein xrefs or GENE_OR_PROTEIN graph nodes are declared. The causal inventory has zero typed protein nodes; success does not validate molecules mentioned in prose, localization, mechanism or formation necessity. |
| septin-record-chloroplast_stroma | data/structures/membrane_organelle/chloroplast_stroma.yaml; Entire current maintained record at fa6c7f0034c57fac03d026ce0ddb8aaa4bd4b2e3 | supports | Full record identity, synonyms, history, boundaries, components where present, taxonomic examples, functions, evidence, graph and discussions read. No attached image or verbatim snippet is declared. |
| septin-original-chloroplast_stroma | reviews/structured/20261021T110927Z-chloroplast-stroma-audit/review.yaml; Entire original YAML/Markdown pair; claims, checks, evidence tiers and verdict | supports | Original pass_with_limitations has no findings or curation actions. Historical source access and checks remain historical, not newly executed. |
| septin-original-validation-chloroplast_stroma | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/adversary-septin/original-checks.json; 20261021T110927Z-chloroplast-stroma-audit native validate/render and source/current hash comparison | supports | Validation and render exit0; deterministic Markdown is byte-identical. Original source revision, original frozen target hash and current target bytes match. |
| septin-native-chloroplast_stroma-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/chloroplast_stroma-uniprot-verify-receipt.json; Actual root-run receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/chloroplast_stroma-uniprot-verify.log | supports | Exit0 at 2026-11-03T10:11:21.659574+00:00. No protein_examples, UniProtKB protein xrefs or GENE_OR_PROTEIN graph nodes are declared. The causal inventory has zero typed protein nodes; success does not validate molecules mentioned in prose, localization, mechanism or formation necessity. |
| septin-native-chloroplast_stroma-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/chloroplast_stroma-uniprot-causal-receipt.json; Actual root-run receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/chloroplast_stroma-uniprot-causal.log | supports | Exit0 at 2026-11-03T10:11:22.099143+00:00. No protein_examples, UniProtKB protein xrefs or GENE_OR_PROTEIN graph nodes are declared. The causal inventory has zero typed protein nodes; success does not validate molecules mentioned in prose, localization, mechanism or formation necessity. |
| septin-record-ciliary_pocket_membrane | data/structures/membrane_organelle/ciliary_pocket_membrane.yaml; Entire current maintained record at fa6c7f0034c57fac03d026ce0ddb8aaa4bd4b2e3 | supports | Full record identity, synonyms, history, boundaries, components where present, taxonomic examples, functions, evidence, graph and discussions read. No attached image or verbatim snippet is declared. |
| septin-original-ciliary_pocket_membrane | reviews/structured/20261021T110936Z-ciliary-pocket-membrane-audit/review.yaml; Entire original YAML/Markdown pair; claims, checks, evidence tiers and verdict | supports | Original pass_with_limitations has no findings or curation actions. Historical source access and checks remain historical, not newly executed. |
| septin-original-validation-ciliary_pocket_membrane | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/adversary-septin/original-checks.json; 20261021T110936Z-ciliary-pocket-membrane-audit native validate/render and source/current hash comparison | supports | Validation and render exit0; deterministic Markdown is byte-identical. Original source revision, original frozen target hash and current target bytes match. |
| septin-native-ciliary_pocket_membrane-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/ciliary_pocket_membrane-uniprot-verify-receipt.json; Actual root-run receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/ciliary_pocket_membrane-uniprot-verify.log | supports | Exit0 at 2026-11-03T10:11:28.198402+00:00. No protein_examples, UniProtKB protein xrefs or GENE_OR_PROTEIN graph nodes are declared. The causal inventory has zero typed protein nodes; success does not validate molecules mentioned in prose, localization, mechanism or formation necessity. |
| septin-native-ciliary_pocket_membrane-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/ciliary_pocket_membrane-uniprot-causal-receipt.json; Actual root-run receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/ciliary_pocket_membrane-uniprot-causal.log | supports | Exit0 at 2026-11-03T10:11:28.589211+00:00. No protein_examples, UniProtKB protein xrefs or GENE_OR_PROTEIN graph nodes are declared. The causal inventory has zero typed protein nodes; success does not validate molecules mentioned in prose, localization, mechanism or formation necessity. |
| septin-context-chloroplast | data/structures/membrane_organelle/chloroplast.yaml; Only identity, label, definition, parent_structures, part_of and has_part | supports | Frozen before reading; used solely for membrane/space/whole-organelle or pocket/collar boundary consistency, not independent review of other claims or resolution of any historical finding. |
| septin-context-chloroplast_envelope | data/structures/membrane_organelle/chloroplast_envelope.yaml; Only identity, label, definition, parent_structures, part_of and has_part | supports | Frozen before reading; used solely for membrane/space/whole-organelle or pocket/collar boundary consistency, not independent review of other claims or resolution of any historical finding. |
| septin-context-chloroplast_inner_membrane | data/structures/membrane_organelle/chloroplast_inner_membrane.yaml; Only identity, label, definition, parent_structures, part_of and has_part | supports | Frozen before reading; used solely for membrane/space/whole-organelle or pocket/collar boundary consistency, not independent review of other claims or resolution of any historical finding. |
| septin-context-chloroplast_intermembrane_space | data/structures/membrane_organelle/chloroplast_intermembrane_space.yaml; Only identity, label, definition, parent_structures, part_of and has_part | supports | Frozen before reading; used solely for membrane/space/whole-organelle or pocket/collar boundary consistency, not independent review of other claims or resolution of any historical finding. |
| septin-context-flagellar_pocket | data/structures/membrane_organelle/flagellar_pocket.yaml; Only identity, label, definition, parent_structures, part_of and has_part | supports | Frozen before reading; used solely for membrane/space/whole-organelle or pocket/collar boundary consistency, not independent review of other claims or resolution of any historical finding. |
| septin-context-ciliary_pocket_collar | data/structures/cytoskeleton/ciliary_pocket_collar.yaml; Only identity, label, definition, parent_structures, part_of and has_part | supports | Frozen before reading; used solely for membrane/space/whole-organelle or pocket/collar boundary consistency, not independent review of other claims or resolution of any historical finding. |
| septin-root22-sources-membrane-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009535,GO:0009706,GO:0009707,GO:0009941,GO:0031969,GO:0042170; Requested exact GO term records: identities, definitions, obsolete flags, synonyms and relevant typed child relations | supports | Exact envelope-bilayer definition, plastid-membrane is-a parent, envelope parthood and inner/outer is-a children. Internal thylakoid membrane has a distinct definition. |
| septin-root22-sources-outer-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005737,GO:0009527,GO:0009707,GO:0009941,GO:0031969,GO:0031972; Requested exact GO term records: identities, definitions, obsolete flags, synonyms and relevant typed child relations | supports | Exact cytoplasm-facing outer bilayer with both maintained is-a parents; intermembrane-space and envelope definitions support its topology. |
| septin-root22-sources-stroma-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009507,GO:0009532,GO:0009543,GO:0009570,GO:0009941,GO:0010287,GO:0042644,GO:0045037; Requested exact GO term records: identities, definitions, obsolete flags, synonyms and relevant typed child relations | supports | Exact stroma region excludes thylakoid lumen; plastid-stroma parent and chloroplast whole are supported. Nucleoid and plastoglobule are explicit part_of children; protein-import process is distinct from its destination. |
| septin-pocket-membrane-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0020016,GO:0020018,GO:0060170,GO:1990900; Requested exact GO term records: identities, definitions, obsolete flags, synonyms and relevant typed child relations | supports | Exact pocket-membrane identity and all three exact synonyms; ciliary-membrane is-a parent and pocket parthood. The collar is a separate structural identity. |
| septin-root22-sources-SL-0054-json | https://rest.uniprot.org/locations/SL-0054.json; Exact native location id/name/definition/synonyms/GO mappings and relevant isA/partOf objects; no protein-list inference | supports | SL-0054 maps to GO:0009707 with Chloroplastic outer membrane synonym and cytoplasm-facing definition. Immediate isA parents are SL-0053 and SL-0214. Envelope parthood occurs through hierarchy, not a direct top-level partOf field. The broader SL-0053 text also mentions thylakoids; it is not substituted for the more precise maintained GO:0031969 envelope-bilayer scope. |
| septin-root22-sources-SL-0055-json | https://rest.uniprot.org/locations/SL-0055.json; Exact native location id/name/definition/synonyms/GO mappings and relevant isA/partOf objects; no protein-list inference | supports | SL-0055 maps exactly to GO:0009570 with the chloroplastic stroma synonym; its definition excludes thylakoid space. Direct isA is plastid stroma and direct partOf is chloroplast. |
| septin-root22-sources-SL-0217-json | https://rest.uniprot.org/locations/SL-0217.json; Exact native location id/name/definition/synonyms/GO mappings and relevant isA/partOf objects; no protein-list inference | supports | SL-0217 maps to plastoglobule GO:0010287. Its definition places lipid-containing plastoglobules in stroma; direct partOf is chloroplast, not a top-level stroma relation. Lipid-reservoir wording is explicitly qualified in the source. |
| septin-pocket-membrane-agent-tax-5691 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5691; Complete ENA taxonomy name, taxId, rank, lineage and aliases | supports | Native taxon5691 is species Trypanosoma brucei. Taxonomy identity does not establish an experimental strain or quantitative occurrence. |
| septin-root22-sources-doi-10.1093_mp_ssp083 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1093%2Fmp%2Fssp083; Europe PMC exact DOI result: complete abstract, title, author list, identifiers, journal and date | supports | Karcher et al.2009 complete primary abstract identifies Chlamydomonas HLP chloroplast targeting/nucleoid association and RNAi effects on nucleoid organization/genome copy number. Current access is abstract-level; it does not establish that every stromal protein or constituent is necessary. |
| septin-pocket-membrane-agent-doi-10.1073_pnas.0909289106 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1073/pnas.0909289106; Europe PMC exact DOI result: complete abstract, title, author list, identifiers, journal and date | supports | Gadelha et al.2009 primary abstract supports a distinct yet continuous T. brucei pocket membrane domain and associated cytoskeletal boundaries. Suggested channel functions remain hypotheses, not universal demonstrated mechanisms. |
| septin-pocket-membrane-agent-doi-10.1242_jcs.045740 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1242/jcs.045740; Europe PMC exact DOI result: complete abstract, title, author list, identifiers, journal and date | supports | Lacomble et al.2009 primary abstract describes procyclic trypomastigote pocket geometry and associated boundaries; the membrane domain is distinguished from surrounding collar and other cytoskeleton. |
| septin-pocket-membrane-agent-doi-10.1038_nrmicro2221 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1038/nrmicro2221; Europe PMC exact DOI result: complete abstract, title, author list, identifiers, journal and date | supports | Field and Carrington2009 secondary review abstract describes a specialized plasma-membrane invagination and trafficking context. Current access is complete native abstract, not full review body or publisher Key Points. |
| septin-pocket-membrane-agent-doi-10.1016_j.pt.2020.11.005 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.pt.2020.11.005; Europe PMC exact DOI result: complete abstract, title, author list, identifiers, journal and date | supports | Halliday et al.2021 secondary review abstract compares trypanosomatid pocket morphology/function with life-cycle and niche qualifications. Native bibliography includes Halliday, de Castro-Neto, Alcantara, Cunha-E-Silva, Vaughan and Sunter; the current record shorthand is not used as a full author list. |
| septin-root21-sources-NCBITaxon-33090 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/33090; Native taxonomy exact record | supports | Reused public-source snapshot originally fetched 2026-11-03T09:33:10.011310Z; no fresh retrieval claimed. Viridiplantae identity/rank/lineage and aliases. |
| septin-root21-sources-NCBITaxon-3055 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3055; Native taxonomy exact record | supports | Reused public-source snapshot originally fetched 2026-11-03T09:33:10.011369Z; no fresh retrieval claimed. Chlamydomonas reinhardtii identity/rank/lineage and aliases. |
| septin-root21-sources-doi-10.1098_rstb.2009.0103 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1098/rstb.2009.0103; Complete exact Europe PMC bibliography and abstract | supports | Reused public-source snapshot originally fetched 2026-11-03T09:33:10.767625Z; no fresh retrieval claimed. Keeling2010 is a secondary plastid-evolution synthesis, not primary experimental proof of every lineage or prevalence. |
| septin-root21-sources-doi-10.1016_j.cell.2022.10.030 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.cell.2022.10.030; Complete exact Europe PMC primary abstract and bibliography | supports | Reused public-source snapshot originally fetched 2026-11-03T09:33:10.803490Z; no fresh retrieval claimed. Jin2022 resolves a Chlamydomonas14-component TOC–TIC assembly spanning two envelope membranes. Its inner route is potential Tic20/YlmG architecture; no complete Results or raw cryo-EM audit is claimed. |
| septin-root21-sources-doi-10.1007_s00294-011-0339-1 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1007/s00294-011-0339-1; Complete exact Europe PMC secondary-review abstract and bibliography | supports | Reused public-source snapshot originally fetched 2026-11-03T09:33:11.481915Z; no fresh retrieval claimed. Terashima2011 compares Chlamydomonas chloroplast proteins/metabolism with plant chloroplasts; the whole-chloroplast survey is not a purified stromal proteome or direct assay of every nucleoid constituent. |
| septin-root21-sources-keeling2010-pmc | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2817223/; Genuine secondary-review PMC HTML Abstract and section1 primary-plastid origin/two-boundary-membrane body; no pixels | supports | Reused public-source snapshot originally fetched 2026-11-03T09:33:10.806914Z; no fresh retrieval claimed. Selected body supports primary-plastid green-algal/plant context with lineage qualifications. |
| septin-root21-sources-jin2022-author-publications | https://lifesciences.westlake.edu.cn/labs/zhen-yan/structural-biology-laboratory/publications/; Exact author-laboratory Jin2022 entry and complete abstract only | supports | Reused public-source snapshot originally fetched 2026-11-03T09:33:11.441964Z; no fresh retrieval claimed. Author-hosted abstract corroborates envelope-spanning Chlamydomonas assembly and potential inner pathway; it is not full paper access. |
| septin-root21-sources-terashima2011-pdf | https://link.springer.com/content/pdf/10.1007/s00294-011-0339-1.pdf; Actual nominal publisher PDF response body | supports | Reused public-source snapshot originally fetched 2026-11-03T09:33:11.567479Z; no fresh retrieval claimed. The nominal PDF returned3038-byte HTML challenge. No new full PDF read is claimed, and old original-review body access is not impersonated. |
| septin-current-adapter-catalogue | https://imodulondb.org/api/datasets; Complete official organism/dataset JSON response; all names, IDs and dataset lists inspected | supports | The complete catalogue has20 organisms,28 organism/dataset pairs and22 distinct dataset-key strings. None matches Viridiplantae, Chlamydomonas reinhardtii or Trypanosoma brucei. No mismatched organism is used for downstream gene/module inference, and noncoverage is not biological absence. |
| septin-historical-adapter-runner | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical canary runner invocation00:49:00.848907Z–00:49:00.863225Z | supports | Actual historical datasets invocation exited1 with PermissionError reading pyvenv.cfg. Receipt is reused, not a fresh invocation; current source catalogue fallback is separately fetched. |
| septin-access-source-receipts | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/adversary-septin/source-receipts.json; Actual source request outcomes/timestamps and saved response hashes | supports | Direct and legacy PMC pocket routes returned challenge HTML; Europe PMC fullTextXML returned500. Karcher publisher/PDF routes and alternate article access failed. Field publisher returned challenge HTML and Halliday DOI route a redirect stub. These are not scientific body reads. |
| septin-access-extra-receipts | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/adversary-septin/extra-receipts.json; Actual source request outcomes/timestamps and saved response hashes | supports | Direct and legacy PMC pocket routes returned challenge HTML; Europe PMC fullTextXML returned500. Karcher publisher/PDF routes and alternate article access failed. Field publisher returned challenge HTML and Halliday DOI route a redirect stub. These are not scientific body reads. |
| septin-access-browser-alternatives-receipt | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/adversary-septin/browser-alternatives-receipt.json; Actual source request outcomes/timestamps and saved response hashes | supports | Direct and legacy PMC pocket routes returned challenge HTML; Europe PMC fullTextXML returned500. Karcher publisher/PDF routes and alternate article access failed. Field publisher returned challenge HTML and Halliday DOI route a redirect stub. These are not scientific body reads. |
| septin-gadelha-indexed-body | https://pmc.ncbi.nlm.nih.gov/articles/PMC2755463/; Only returned indexed Discussion subsections Surface Membrane Domains, Boundaries Between Continuous Surface Domains and No Endocytosis Regionalization in the FP | supports | Primary discussion distinguishes membrane domains from the collar and keeps mechanisms qualified. This indexed excerpt is not a complete direct PMC body read. |
| septin-lacomble-indexed-methods | https://pmc.ncbi.nlm.nih.gov/articles/PMC2714436/; Only returned indexed Materials and Methods: Cell culture, sample preparation, TEM and cellular tomography | supports | The methods identify procyclic T. brucei brucei strain427. This limited methods access does not make a full article or image audit. |
| septin-pocket-source-search | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/adversary-septin/browser-source-receipts.json; Bounded web retrieval queries and only returned exact-primary results | supports | Queries retrieved the specifically documented primary excerpts and possible access routes. Unrelated returned pages were discarded. Failed direct opens do not erase indexed excerpt access; no exhaustive absence finding is made. |
| septin-pocket-stage-search | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/adversary-septin/browser-stage-search.json; Bounded web retrieval queries and only returned exact-primary results | supports | Queries retrieved the specifically documented primary excerpts and possible access routes. Unrelated returned pages were discarded. Failed direct opens do not erase indexed excerpt access; no exhaustive absence finding is made. |
| check-qc | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/qc.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| check-labels | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/labels.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| check-trait-links | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/trait-links.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Native TraitMech link check passed. |
| check-vendored | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/vendored.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Pinned governed files match; native vendored check passed. |
| check-curies | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/curies.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| focused | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/focused-results.json; All twenty actual target schema/strict command outputs | supports | Ten schema and ten strict commands returned exit zero. |
| supplemental-pmid | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/pmid-chunks-receipt.json; Complete native-report PMID set checked with unchanged resolver in batches of at most fifty | supports | 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers remain unverified. |
| historical-adapter-runner-availability | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical runner invocation receipt, cross-checked against exact stdout/stderr hashes; reread during PR2359 synthesis | context_only | Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS PermissionError reading the configured runner pyvenv.cfg. This is a retained historical availability observation, not a fresh attempt or a scientific validation failure. Native policy permits inspected source-catalogue fallback. |

## Limits And Additional Notes

- Chloroplast thylakoid, lumen and membrane independent subreview: Engel2015 is inspected primary JATS at the named Introduction/Results/Discussion/Methods sections; captions are text, not independent image-pixel or raw-tomogram analysis. CC-124/137c, TAP and constant light remain explicit. Limited tomogram volumes do not establish one globally continuous lumen or universal biogenesis routes.
- Chloroplast thylakoid, lumen and membrane independent subreview: Terashima2011 fresh source is an actual readable PDF, with printedpp151–156 Introduction/Photosynthesis text inspected. It is secondary synthesis; full supplementary proteomes, every cited primary experiment and later metabolic sections are outside this audit. The benign pdftotext hint-table warning did not prevent readable extraction.
- Chloroplast thylakoid, lumen and membrane independent subreview: Perez2024 uses independently reread cached official-publisher browser body packets from09:34:09Z and09:37:31Z. Actual original capture times and hashes are retained. The new native request returned403; no new browser retrieval or complete native body is claimed.
- Chloroplast thylakoid, lumen and membrane independent subreview: Keeling2010 selected fresh secondary PMC body was inspected; the failed EuropePMC JATS response remains separately disclosed. Broad plastid occurrence does not establish thylakoids in every nonphotosynthetic lineage.
- Chloroplast thylakoid, lumen and membrane independent subreview: The ontology comment supports the maintained OTHER interpretation for whole thylakoid; no wholesale reconciliation of GO’s inherited organelle classification is claimed. Exact membrane/lumen parts and green-lineage scope are independently checked.
- Chloroplast thylakoid, lumen and membrane independent subreview: Constitutional membrane material is distinct from necessary individual lipids, pigments or proteins. These targets intentionally contain no exact protein-example or family assertions, and no unsupported inventory is required.
- Chloroplast thylakoid, lumen and membrane independent subreview: Current catalogue has no matched chloroplast host. S.elongatus photosynthetic dataset coverage is not Chlamydomonas coverage. The actual historical runner failed00:49Z; no fresh invocation or successful runner execution is claimed.
- Chloroplast thylakoid, lumen and membrane independent subreview: Historical735/736/other curation numbers are read only as record history. No exact predecessor finding is newly resolved, rejected or superseded by this partial cohort.
- Chloroplast thylakoid, lumen and membrane independent subreview: All three targets declare no images or numerical measurements; no target pixel inspection is claimed. Shared mutual targets provide all needed boundary context. Root owns global QC, issue deduplication/publication and repository/GitHub mutations.
- Chlorosome, envelope and cis-Golgi network independent subreview: Assigned scope is exactly chlorosome, chlorosome envelope and cis-Golgi network. Three frozen neighbors were consulted only at declared boundary fields; no whole-category review or terminal disposition of closed grouped issue2419 is claimed.
- Chlorosome, envelope and cis-Golgi network independent subreview: Nielsen2016 genuine current JATS was read at complete Introduction/Results/Discussion plus Sample preparation Methods. Its structure is bchK-mutant carotenosome baseplate with wild-type comparisons; AFM dimensions refer to earlier work. No NMR/raw microscopy pixels, supplements or full computational pipeline audit.
- Chlorosome, envelope and cis-Golgi network independent subreview: Frigaard2004 current institutional PDF was read as text at declared Methods/Results/Discussion scope. Native PMC challenge and guessed JATS404 are retained failures, not article bodies. CsmA nonsegregation tests viability/light harvesting under its conditions, not a direct universal assembly endpoint.
- Chlorosome, envelope and cis-Golgi network independent subreview: Psencik2009 genuine PMC body snapshot was fetched2026-11-03T04:31:37.620817Z and reread now; current10:11Z PMC request returned challenge HTML and guessed JATS404. Declared Methods/structural Results/Discussion were inspected as text, not raw images or tomography/spectra reanalysis.
- Chlorosome, envelope and cis-Golgi network independent subreview: Orf2013 author-uploaded body was inspected through the browser at its actual captured time, separately from direct403 and publisher/PDF challenge HTML. It and Oostergetel2010 are secondary context; neither is recast as a new primary experiment.
- Chlorosome, envelope and cis-Golgi network independent subreview: Li2006 and Frigaard2005 were assessed from exact primary abstracts only. Cho2000 primary abstract was accessible; both attempted publisher body/PDF routes returned403. No fresh complete Methods claims are made for these articles.
- Chlorosome, envelope and cis-Golgi network independent subreview: Rossanese1999 complete Results/Discussion and Strains and Plasmids Methods were inspected; no figure pixels, full remaining Methods or supplementary analysis. Its evidence gap does not establish absence of CGN. ATCC/ENA strain identity is not organelle-occurrence evidence.
- Chlorosome, envelope and cis-Golgi network independent subreview: Ten declared chlorosome-family protein examples are verified in each record, seven reviewed and three unreviewed. InterPro match endpoints are bounded to these exact accessions; H2VFJ4 HTTP204 and exact-symbol csmK zero hits do not establish universal family/protein absence. Generic acceptor and missing csmK example remain explicitly bounded.
- Chlorosome, envelope and cis-Golgi network independent subreview: iModulonDB no-match is limited to the complete catalogue fetched10:11:10Z and assigned taxa. Historical runner PermissionError is00:49Z, not a current invocation. No uncovered-organism downstream query or module membership was fabricated.
- Chlorosome, envelope and cis-Golgi network independent subreview: Original review access and global-check dates remain historical and may have different scope. Current native six protein-command receipts were inspected; root owns current whole-corpus QC, label/identifier/trait/history gates, issue deduplication/publication and final integration.
- Chloroplast membrane, outer membrane, stroma and ciliary pocket membrane independent subreview: Assigned four unchanged targets only; all four original bundles validate/render exactly and their original frozen record hashes remain current. No original scientific findings/actions exist and none is invented.
- Chloroplast membrane, outer membrane, stroma and ciliary pocket membrane independent subreview: Public chloroplast source snapshots were reused with their original2026-11-03T09:33Z timestamps and verified hashes. Keeling body is secondary Abstract/section1 only; Jin is primary complete indexed abstract and exact author abstract entry, not full Results.
- Chloroplast membrane, outer membrane, stroma and ciliary pocket membrane independent subreview: Terashima current usable scope is its complete secondary abstract; the retained nominal PDF response is HTML challenge. The historical October original review had a wider reported body scope, which this current review does not impersonate. Karcher primary support is complete abstract only; publisher/PDF routes returned403.
- Chloroplast membrane, outer membrane, stroma and ciliary pocket membrane independent subreview: Current direct and legacy pocket PMC routes returned challenge HTML; Europe PMC fullTextXML returned500. Gadelha indexed primary Discussion and Lacomble indexed Methods were read at exact saved extents plus complete native abstracts. They are not complete direct full-body reads. Field and Halliday support is native secondary abstract only; current publisher responses are challenge/stub pages.
- Chloroplast membrane, outer membrane, stroma and ciliary pocket membrane independent subreview: No figure pixels, raw tomography, supplementary proteome lists, kinetic datasets or full quantitative inventories were audited. No unobserved source body or unsupported life-stage/strain transfer is claimed.
- Chloroplast membrane, outer membrane, stroma and ciliary pocket membrane independent subreview: The bounded web retrieval searches returned unrelated pages; only exact primary publication matches were used. Their absence of other results is not evidence of biological or bibliographic absence.
- Chloroplast membrane, outer membrane, stroma and ciliary pocket membrane independent subreview: The complete source catalogue has no matched green-algal or T. brucei organism; coverage limits do not mean biological absence. No molecular query is invented for the sparse ciliary-pocket membrane. The00:49Z runner failure is historical, separate from current official source fallback.
- Chloroplast membrane, outer membrane, stroma and ciliary pocket membrane independent subreview: All eight native protein commands pass empty inventories (zero typed protein nodes). They cannot establish TOC–TIC/HLP narrative identity, localization, protein function or assembly necessity.
- Chloroplast membrane, outer membrane, stroma and ciliary pocket membrane independent subreview: Constitutional collective bilayer material is distinct from empirical requirement for each lipid species. The spatial stroma need not assert an invariant molecular inventory; individual formation necessity remains unknown.
- Chloroplast membrane, outer membrane, stroma and ciliary pocket membrane independent subreview: The six additional frozen neighbors were read only for boundary fields. No other record, historical issue or category finding is terminally resolved. Global gates, issue dedup/publication, repository writes and merge decisions remain root-owned.
- Historical observations remain immutable; their old checks are not represented as current-head execution.
- The adapter runner was not rerun after the canary established OS access failure. Catalogue-based coverage is assessed directly; fresh and reused responses retain actual access timestamps.
- Native label checks include 923 no-adapter skips. Native identifier checks include 909 PMID transport failures and 254 skipped identifiers; bounded supplemental checks independently resolve the 909 PMIDs.
- Scientific record-curation findings stay in separate issues; no record is edited by this review PR.
- Final trusted-base post-save review-check, exact-head independent acceptance, final-head CI and merge-group CI occur after saving this immutable observation and are not represented here as already completed.
- All ten original YAML/Markdown pairs remain unchanged. Current main was merged normally and pushed without force.
- This explicit issue-bearing ten-record cohort follows the native persistence policy. Each inherited scientific finding retains exact predecessor identity.
- Issue #2657 tracks the thylakoid part_of edges and the chlorosome/baseplate node-typing and accessory-protein localization refreshes. Scientific record curation remains separately tracked and open. Existing validator #2514 remains open.
- Issue #2658 tracks five omitted applicability assessments and three unsupported expression-only exclusions. Thylakoid lumen and ciliary pocket membrane are genuine sparse topology exclusions.
- Source commit fa6c7f0034c57fac03d026ce0ddb8aaa4bd4b2e3 is retained by tag review-base/pr2359-current-record-followup-20261103.
- CLAUDE.md is an alias of AGENTS.md; canonical regular AGENTS.md bytes are frozen.
- All used local context was frozen before assessment, including nine neighbor records, native configuration, graph/protein policies and verifier source. Neighbors are context only, not additional targets or dispositions of their findings.
- Fresh and reused public-source snapshots retain actual access dates and inspection tiers. Native authority identity does not independently establish localization, mechanistic action or assembly necessity.
- Native checks with empty protein inventories or zero GENE_OR_PROTEIN nodes do not validate molecules appearing only in narrative prose.
- Thylakoid membrane/lumen part_of edges are assessed as anatomical containment. They do not reinstate the earlier bounds overclaim or establish one globally continuous lumen from local tomographic observations.
- Chlorosome baseplate complex typing and accessory protein localization are assessed separately from assembly necessity. Closed #2419 is history context for grouped node typing; this follow-up does not dispose of that grouped issue or category findings. Open #2537 concerns experimental-preparation wording in the separate baseplate-complex record.
- All five inherited scientific findings remain open for separate record curation: chlorosome and envelope baseplate assembly necessity, cis-Golgi current PPY12 taxon and stack-versus-CGN study scope (major), and whole-network-to-lipid component_ref (minor). Seven targets retain qualified positive scientific assessments. No record is edited.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T102014Z-pr2359-current-record-followup
kind: batch
repository: CultureBotAI/CellStructureMech
title: 'PR 2359: current-input review of ten records and adversarial follow-up'
started_at: '2026-11-03T10:09:18.407991Z'
finished_at: '2026-11-03T10:20:14Z'
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
summary: Current-input reassessment of all ten records in PR2359. Three stale reviews
  are substantively refreshed. Independent source assessments retain five inherited
  scientific findings and correct eight structured-source applicability assessments
  without editing records.
source:
  git_revision: fa6c7f0034c57fac03d026ce0ddb8aaa4bd4b2e3
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
  - path: data/structures/cytoskeleton/ciliary_pocket_collar.yaml
    sha256: df0530c9582d0a40d8e0c646cdaa88cc0872d1e6e034cbdcd068b2a3f426ec3a
    role: context
  - path: data/structures/energy_complex/chlorosome_baseplate_antenna_complex.yaml
    sha256: 7ea00dedcd0998fc477737d6d2e8301e4e57a08e57378d19efe5e32a6ea8c92d
    role: context
  - path: data/structures/membrane_organelle/chloroplast.yaml
    sha256: 4c13f5dadaeb23a88fabfc2b5ec65034ed0ac83cbca9d45143793618acf2e727
    role: context
  - path: data/structures/membrane_organelle/chloroplast_envelope.yaml
    sha256: 29da363489107536342db1782001be534ea54605039b80c201cba0a46de9468e
    role: context
  - path: data/structures/membrane_organelle/chloroplast_inner_membrane.yaml
    sha256: 05283f5252a6354d26bef1ff196b3a9e10fbd6e72e9a6ec17014330f7a28dbb3
    role: context
  - path: data/structures/membrane_organelle/chloroplast_intermembrane_space.yaml
    sha256: 7ab90f4d2f4c41c466e100d589fb1f1d42bf90ded515dea6db5575d54119d43a
    role: context
  - path: data/structures/membrane_organelle/chloroplast_membrane.yaml
    sha256: 115d9369e1b84a54e66028f079a8d140e72d40ec2fb5877e64fb592b6a085905
    role: target
  - path: data/structures/membrane_organelle/chloroplast_outer_membrane.yaml
    sha256: f499d6317b1546cf0d578f54d04df76a8af3c54746f29db6b2d7af0244b0075d
    role: target
  - path: data/structures/membrane_organelle/chloroplast_stroma.yaml
    sha256: cfdb0d3be9fba838d5288e478b39f922a4e11cbd240b689a2cbca7690c262b6a
    role: target
  - path: data/structures/membrane_organelle/chloroplast_thylakoid.yaml
    sha256: edf435ef39aeb8c0fa0e572768a0e7f599b7177945d1c7a621d3d810bbaf17cd
    role: target
  - path: data/structures/membrane_organelle/chloroplast_thylakoid_lumen.yaml
    sha256: 6efd0a2e86462ae192dc2f27f9edc945dc6b522a31d8e233458cd25e661fb2af
    role: target
  - path: data/structures/membrane_organelle/chloroplast_thylakoid_membrane.yaml
    sha256: 16f50bd615bee75edd15004622bae49a9a25e71dd4b9573584ca1659139d0999
    role: target
  - path: data/structures/membrane_organelle/chlorosome.yaml
    sha256: be2261521f06e087e2edd95af366813a289dba202239800a2c715033bd0105da
    role: target
  - path: data/structures/membrane_organelle/chlorosome_envelope.yaml
    sha256: d39583d641a4c6070008f52e29246d1659bf86b1158799b1c30caf2e272ef903
    role: target
  - path: data/structures/membrane_organelle/ciliary_pocket_membrane.yaml
    sha256: acdf228c05817a740e627e5885200d543b8cb91f6ac94aefa4f5bf954255b3e0
    role: target
  - path: data/structures/membrane_organelle/cis_golgi_network.yaml
    sha256: 369cae5270aeacd25a94317be3b005167773bd89a5e4c2583061fa24cd79f31d
    role: target
  - path: data/structures/membrane_organelle/cis_golgi_network_membrane.yaml
    sha256: c818f4de1c2fd8c36bc121d4389ce017c59526e083e6aefdf1b2a0041411da9c
    role: context
  - path: data/structures/membrane_organelle/flagellar_pocket.yaml
    sha256: d67c465d104f21905f63ea994b6f4f526a51502cefccf79e9e732698f4971fa8
    role: context
  - path: data/structures/membrane_organelle/golgi_apparatus.yaml
    sha256: e3df76cd9d71ba04df9e5349475bd4191c31f93156acd422ef6b0223b88facca
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
  - path: reviews/structured/20261021T110921Z-chloroplast-membrane-audit/review.md
    sha256: 7cd8b8d2d185b1304d8b3c5aa172060c988e3d69d654384eb746d76e2497cb04
    role: context
  - path: reviews/structured/20261021T110921Z-chloroplast-membrane-audit/review.yaml
    sha256: a76189a76a9dd5f2f9121ea2d9931a1eaa30242657b30eebd265187fbdeac676
    role: context
  - path: reviews/structured/20261021T110923Z-chloroplast-outer-membrane-audit/review.md
    sha256: baf02cb3a132ad159f37a9cdbb7d1a3257e1f86842c58c07e95bc878b8268f44
    role: context
  - path: reviews/structured/20261021T110923Z-chloroplast-outer-membrane-audit/review.yaml
    sha256: c8f22919f640db5735a0a8768eb75f73ab841bcc9dfc028c98d29c9bbfdd0b1d
    role: context
  - path: reviews/structured/20261021T110927Z-chloroplast-stroma-audit/review.md
    sha256: d90dadb14e3d1de4fc1b5c03c72a96adace10b0044e9254a6f82b0c60c47e9e3
    role: context
  - path: reviews/structured/20261021T110927Z-chloroplast-stroma-audit/review.yaml
    sha256: fad2c9ed334d31f3d23e9c207f85f54c2231b0f7167287251ce10ae9dfb80867
    role: context
  - path: reviews/structured/20261021T110930Z-chloroplast-thylakoid-audit/review.md
    sha256: 6c5b77fe43f7463e9d52d4225c7696ee685904e00c9abbe0fb9a2d277a5feedf
    role: context
  - path: reviews/structured/20261021T110930Z-chloroplast-thylakoid-audit/review.yaml
    sha256: b39043ffc03ba6a10006a18d878a703d33bb0864cf343b5377e39e646590ea1a
    role: context
  - path: reviews/structured/20261021T110931Z-chloroplast-thylakoid-lumen-audit/review.md
    sha256: 5b2fb9212c68e9fe8f143a4840d6a640e9517713ebe668dd221aa21994d6910a
    role: context
  - path: reviews/structured/20261021T110931Z-chloroplast-thylakoid-lumen-audit/review.yaml
    sha256: 2f261f4cc32831358b5f4ee4acecaabb66253d7bb02dcff457055b8ec368ff46
    role: context
  - path: reviews/structured/20261021T110932Z-chloroplast-thylakoid-membrane-audit/review.md
    sha256: ce4503349764d40af6865d813fb149a0256ca68a4d83987c04c46e921b3d8c81
    role: context
  - path: reviews/structured/20261021T110932Z-chloroplast-thylakoid-membrane-audit/review.yaml
    sha256: be8deef886b2ef883bd4c18f5079c12552a8bd1c4a985a15e7c69baf357a9fa2
    role: context
  - path: reviews/structured/20261021T110934Z-chlorosome-audit/review.md
    sha256: 6373dc91a3a8e53af9bb7be1293d676183a97e84958ed65c23ce80f998ba9712
    role: context
  - path: reviews/structured/20261021T110934Z-chlorosome-audit/review.yaml
    sha256: 5258ec88b9c9f6c87dae0507de4ed2f6ac9eedea0badd7bb1ef4f6edc8f5c644
    role: context
  - path: reviews/structured/20261021T110935Z-chlorosome-envelope-audit/review.md
    sha256: ff8e3c73f729b4db3c308bc8df9ac457b19db089d2e022d60440ae7dbf8b1fd0
    role: context
  - path: reviews/structured/20261021T110935Z-chlorosome-envelope-audit/review.yaml
    sha256: 71d6c9bad049169189915002337cab00a18684911c9d61043e8ca33ed476d65a
    role: context
  - path: reviews/structured/20261021T110936Z-ciliary-pocket-membrane-audit/review.md
    sha256: 28aa104af6350bcc1c21559d022d05c0a97315ff71bd7563505b675565256c59
    role: context
  - path: reviews/structured/20261021T110936Z-ciliary-pocket-membrane-audit/review.yaml
    sha256: 32694ec8da0b5a28df1fc31d0e85d4ec569f290f30ee42788653100d89bac2be
    role: context
  - path: reviews/structured/20261021T110938Z-cis-golgi-network-audit/review.md
    sha256: 3bf9afca4ac493ac0aa3fc1f8e5232d3e3a9cab08fb62543c079ea7e4beee6ad
    role: context
  - path: reviews/structured/20261021T110938Z-cis-golgi-network-audit/review.yaml
    sha256: c5490c5558528e3c04ac297eab3a35e5850a9f26d13fd543c248b26bd4416f12
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
- target_id: GO:0031969
  path: data/structures/membrane_organelle/chloroplast_membrane.yaml
  label: chloroplast membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/chloroplast_membrane.yaml
    role: maintained scientific record
- target_id: GO:0009707
  path: data/structures/membrane_organelle/chloroplast_outer_membrane.yaml
  label: chloroplast outer membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/chloroplast_outer_membrane.yaml
    role: maintained scientific record
- target_id: GO:0009570
  path: data/structures/membrane_organelle/chloroplast_stroma.yaml
  label: chloroplast stroma
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/chloroplast_stroma.yaml
    role: maintained scientific record
- target_id: GO:0009534
  path: data/structures/membrane_organelle/chloroplast_thylakoid.yaml
  label: chloroplast thylakoid
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/chloroplast_thylakoid.yaml
    role: maintained scientific record
- target_id: GO:0009543
  path: data/structures/membrane_organelle/chloroplast_thylakoid_lumen.yaml
  label: chloroplast thylakoid lumen
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/chloroplast_thylakoid_lumen.yaml
    role: maintained scientific record
- target_id: GO:0009535
  path: data/structures/membrane_organelle/chloroplast_thylakoid_membrane.yaml
  label: chloroplast thylakoid membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/chloroplast_thylakoid_membrane.yaml
    role: maintained scientific record
- target_id: GO:0046858
  path: data/structures/membrane_organelle/chlorosome.yaml
  label: chlorosome
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/chlorosome.yaml
    role: maintained scientific record
- target_id: GO:0033105
  path: data/structures/membrane_organelle/chlorosome_envelope.yaml
  label: chlorosome envelope
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/chlorosome_envelope.yaml
    role: maintained scientific record
- target_id: GO:0020018
  path: data/structures/membrane_organelle/ciliary_pocket_membrane.yaml
  label: ciliary pocket membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/ciliary_pocket_membrane.yaml
    role: maintained scientific record
- target_id: GO:0005801
  path: data/structures/membrane_organelle/cis_golgi_network.yaml
  label: cis-Golgi network
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/cis_golgi_network.yaml
    role: maintained scientific record
scope:
  description: Exact ten-record PR cohort reassessed against current main 7f1c34aa706792399bb3b1c10e7ac189c4870ec1.
    Changed inputs are substantively reassessed. Scientific records remain unchanged.
  selection: Complete cohort of ten maintained records reviewed in original PR head
    1309942a4f279271c832562d4dd7f3d099fd309f.
  coverage: full
  population_size: 10
  reviewed_target_ids:
  - GO:0031969
  - GO:0009707
  - GO:0009570
  - GO:0009534
  - GO:0009543
  - GO:0009535
  - GO:0046858
  - GO:0033105
  - GO:0020018
  - GO:0005801
checks:
- check_id: qc
  name: Full native QC
  status: passed
  required: true
  target_ids:
  - GO:0031969
  - GO:0009707
  - GO:0009570
  - GO:0009534
  - GO:0009543
  - GO:0009535
  - GO:0046858
  - GO:0033105
  - GO:0020018
  - GO:0005801
  command: just qc
  exit_code: 0
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  scope_note: Actual local execution at main-merge head fa6c7f0034c57fac03d026ce0ddb8aaa4bd4b2e3.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-qc
- check_id: labels
  name: Native label correspondence
  status: passed
  required: true
  target_ids:
  - GO:0031969
  - GO:0009707
  - GO:0009570
  - GO:0009534
  - GO:0009543
  - GO:0009535
  - GO:0046858
  - GO:0033105
  - GO:0020018
  - GO:0005801
  command: just validate-products
  exit_code: 0
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  scope_note: Actual local execution at main-merge head fa6c7f0034c57fac03d026ce0ddb8aaa4bd4b2e3.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-labels
- check_id: trait-links
  name: TraitMech references
  status: passed
  required: true
  target_ids:
  - GO:0031969
  - GO:0009707
  - GO:0009570
  - GO:0009534
  - GO:0009543
  - GO:0009535
  - GO:0046858
  - GO:0033105
  - GO:0020018
  - GO:0005801
  command: just check-trait-links --check
  exit_code: 0
  summary: Native TraitMech link check passed.
  scope_note: Actual local execution at main-merge head fa6c7f0034c57fac03d026ce0ddb8aaa4bd4b2e3.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-trait-links
- check_id: vendored
  name: Pinned governed files
  status: passed
  required: true
  target_ids:
  - GO:0031969
  - GO:0009707
  - GO:0009570
  - GO:0009534
  - GO:0009543
  - GO:0009535
  - GO:0046858
  - GO:0033105
  - GO:0020018
  - GO:0005801
  command: just vendored-check
  exit_code: 0
  summary: Pinned governed files match; native vendored check passed.
  scope_note: Actual local execution at main-merge head fa6c7f0034c57fac03d026ce0ddb8aaa4bd4b2e3.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-vendored
- check_id: curies
  name: Native identifier resolver
  status: passed
  required: true
  target_ids:
  - GO:0031969
  - GO:0009707
  - GO:0009570
  - GO:0009534
  - GO:0009543
  - GO:0009535
  - GO:0046858
  - GO:0033105
  - GO:0020018
  - GO:0005801
  command: just check-curies-strict
  exit_code: 0
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  scope_note: Actual local execution at main-merge head fa6c7f0034c57fac03d026ce0ddb8aaa4bd4b2e3.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-curies
- check_id: focused-0
  name: validate GO:0031969
  status: passed
  required: true
  target_ids:
  - GO:0031969
  command: just validate data/structures/membrane_organelle/chloroplast_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-1
  name: validate-strict GO:0031969
  status: passed
  required: true
  target_ids:
  - GO:0031969
  command: just validate-strict data/structures/membrane_organelle/chloroplast_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-2
  name: validate GO:0009707
  status: passed
  required: true
  target_ids:
  - GO:0009707
  command: just validate data/structures/membrane_organelle/chloroplast_outer_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-3
  name: validate-strict GO:0009707
  status: passed
  required: true
  target_ids:
  - GO:0009707
  command: just validate-strict data/structures/membrane_organelle/chloroplast_outer_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-4
  name: validate GO:0009570
  status: passed
  required: true
  target_ids:
  - GO:0009570
  command: just validate data/structures/membrane_organelle/chloroplast_stroma.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-5
  name: validate-strict GO:0009570
  status: passed
  required: true
  target_ids:
  - GO:0009570
  command: just validate-strict data/structures/membrane_organelle/chloroplast_stroma.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-6
  name: validate GO:0009534
  status: passed
  required: true
  target_ids:
  - GO:0009534
  command: just validate data/structures/membrane_organelle/chloroplast_thylakoid.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-7
  name: validate-strict GO:0009534
  status: passed
  required: true
  target_ids:
  - GO:0009534
  command: just validate-strict data/structures/membrane_organelle/chloroplast_thylakoid.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-8
  name: validate GO:0009543
  status: passed
  required: true
  target_ids:
  - GO:0009543
  command: just validate data/structures/membrane_organelle/chloroplast_thylakoid_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-9
  name: validate-strict GO:0009543
  status: passed
  required: true
  target_ids:
  - GO:0009543
  command: just validate-strict data/structures/membrane_organelle/chloroplast_thylakoid_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-10
  name: validate GO:0009535
  status: passed
  required: true
  target_ids:
  - GO:0009535
  command: just validate data/structures/membrane_organelle/chloroplast_thylakoid_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-11
  name: validate-strict GO:0009535
  status: passed
  required: true
  target_ids:
  - GO:0009535
  command: just validate-strict data/structures/membrane_organelle/chloroplast_thylakoid_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-12
  name: validate GO:0046858
  status: passed
  required: true
  target_ids:
  - GO:0046858
  command: just validate data/structures/membrane_organelle/chlorosome.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-13
  name: validate-strict GO:0046858
  status: passed
  required: true
  target_ids:
  - GO:0046858
  command: just validate-strict data/structures/membrane_organelle/chlorosome.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-14
  name: validate GO:0033105
  status: passed
  required: true
  target_ids:
  - GO:0033105
  command: just validate data/structures/membrane_organelle/chlorosome_envelope.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-15
  name: validate-strict GO:0033105
  status: passed
  required: true
  target_ids:
  - GO:0033105
  command: just validate-strict data/structures/membrane_organelle/chlorosome_envelope.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-16
  name: validate GO:0020018
  status: passed
  required: true
  target_ids:
  - GO:0020018
  command: just validate data/structures/membrane_organelle/ciliary_pocket_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-17
  name: validate-strict GO:0020018
  status: passed
  required: true
  target_ids:
  - GO:0020018
  command: just validate-strict data/structures/membrane_organelle/ciliary_pocket_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-18
  name: validate GO:0005801
  status: passed
  required: true
  target_ids:
  - GO:0005801
  command: just validate data/structures/membrane_organelle/cis_golgi_network.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-19
  name: validate-strict GO:0005801
  status: passed
  required: true
  target_ids:
  - GO:0005801
  command: just validate-strict data/structures/membrane_organelle/cis_golgi_network.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: supplemental-pmid
  name: Supplemental bounded PMID authority checks
  status: passed
  required: true
  target_ids:
  - GO:0031969
  - GO:0009707
  - GO:0009570
  - GO:0009534
  - GO:0009543
  - GO:0009535
  - GO:0046858
  - GO:0033105
  - GO:0020018
  - GO:0005801
  command: .venv/bin/python /private/tmp/cellstructure-batches-2346-2397-20261103/check_pmid_chunks.py
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359
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
  - GO:0031969
  - GO:0009707
  - GO:0009570
  - GO:0009534
  - GO:0009543
  - GO:0009535
  - GO:0046858
  - GO:0033105
  - GO:0020018
  - GO:0005801
  summary: 'Eight applicability defects are corrected: five omissions (chloroplast
    thylakoid, thylakoid membrane, chlorosome, chlorosome envelope and cis-Golgi network),
    and three unsupported expression-only exclusions (chloroplast membrane, outer
    membrane and stroma). Thylakoid lumen and ciliary pocket membrane are genuine
    sparse morphology/topology exclusions. Actual complete catalogue coverage has
    no matched chloroplast host, chlorosome organism or relevant budding-yeast dataset.
    No unrelated organism dataset or downstream module query substitutes for this
    noncoverage. Resource noncoverage is not biological absence; retained historical
    runner failure is not a fresh invocation.'
  evidence_ids:
  - plaque-catalogue
  - plaque-historical-runner
  - micro-adapter-catalogue
  - septin-current-adapter-catalogue
- check_id: independent-scientific-review
  name: Independent claim-level source review
  status: passed
  required: true
  target_ids:
  - GO:0031969
  - GO:0009707
  - GO:0009570
  - GO:0009534
  - GO:0009543
  - GO:0009535
  - GO:0046858
  - GO:0033105
  - GO:0020018
  - GO:0005801
  summary: Three read-only reviewers covered the complete ten-record cohort, including
    changed inputs, with explicit scientific findings and source-access limits. Final
    artifact/head acceptance occurs after saving.
  evidence_ids:
  - plaque-policy
  - plaque-rubric
  - plaque-graph-policy
  - plaque-schema-policy
  - plaque-thylakoid-agent-go
  - plaque-isa-0009534
  - plaque-isa-0009543
  - plaque-isa-0009535
  - plaque-thylakoid-agent-SL-0056
  - plaque-thylakoid-agent-SL-0057
  - plaque-thylakoid-agent-SL-0058
  - plaque-thylakoid-agent-NCBITaxon-33090
  - plaque-thylakoid-agent-NCBITaxon-3055
  - plaque-thylakoid-agent-engel2015-meta
  - plaque-thylakoid-agent-perez2024-meta
  - plaque-thylakoid-agent-doi-10.1007_s00294-011-0339-1
  - plaque-thylakoid-agent-doi-10.1098_rstb.2009.0103
  - plaque-thylakoid-agent-engel2015-jats
  - plaque-thylakoid-agent-engel2015-correction
  - plaque-thylakoid-agent-terashima2011-pdf
  - plaque-thylakoid-agent-keeling2010-pmc
  - plaque-thylakoid-agent-perez2024-publisher
  - plaque-thylakoid-agent-keeling2010-jats
  - plaque-perez-body-introduction
  - plaque-perez-body-electron-transport
  - plaque-catalogue
  - micro-review-policy
  - micro-review-config
  - micro-review-profile
  - micro-schema-necessity
  - micro-graph-contract
  - micro-review-schema
  - micro-chl-go
  - micro-chl-SL-0060
  - micro-chl-tax-2
  - micro-chl-tax-1097
  - micro-chl-tax-1108
  - micro-chl-tax-194439
  - micro-cis-tax-4922
  - micro-cis-tax-460519
  - micro-chl-nielsen2016-jats
  - micro-frigaard2004
  - micro-psencik2009-retained-body
  - micro-chl-oostergetel2010-jats
  - micro-orf2013-browser
  - micro-chl-li2006-meta
  - micro-chl-frigaard2005-meta
  - micro-chl-orf2013-meta
  - micro-chl-oostergetel2010-meta
  - micro-chl-psencik2009-meta
  - micro-chl-nielsen2016-meta
  - micro-chl-frigaard2004-meta
  - micro-chl-P0A314
  - micro-chl-matches-P0A314
  - micro-chl-Q46383
  - micro-chl-matches-Q46383
  - micro-chl-Q46367
  - micro-chl-matches-Q46367
  - micro-chl-Q46386
  - micro-chl-matches-Q46386
  - micro-chl-O68986
  - micro-chl-matches-O68986
  - micro-chl-O68988
  - micro-chl-matches-O68988
  - micro-chl-O68983
  - micro-chl-matches-O68983
  - micro-chl-H2VFJ4
  - micro-chl-matches-H2VFJ4
  - micro-chl-H2VFJ1
  - micro-chl-matches-H2VFJ1
  - micro-chl-Q8KEN5
  - micro-chl-matches-Q8KEN5
  - micro-cis-go
  - micro-cis-jats-PMC2148216
  - micro-cis-atcc-204163
  - micro-cis-ena-LC815816
  - micro-cis-cho2000-meta
  - septin-review-policy
  - septin-curation-policy
  - septin-graph-policy
  - septin-root22-sources-membrane-go
  - septin-root22-sources-outer-go
  - septin-root22-sources-stroma-go
  - septin-pocket-membrane-agent-go
  - septin-root22-sources-SL-0054-json
  - septin-root22-sources-SL-0055-json
  - septin-root22-sources-SL-0217-json
  - septin-pocket-membrane-agent-tax-5691
  - septin-root22-sources-doi-10.1093_mp_ssp083
  - septin-pocket-membrane-agent-doi-10.1073_pnas.0909289106
  - septin-pocket-membrane-agent-doi-10.1242_jcs.045740
  - septin-pocket-membrane-agent-doi-10.1038_nrmicro2221
  - septin-pocket-membrane-agent-doi-10.1016_j.pt.2020.11.005
  - septin-root21-sources-NCBITaxon-33090
  - septin-root21-sources-NCBITaxon-3055
  - septin-root21-sources-doi-10.1098_rstb.2009.0103
  - septin-root21-sources-doi-10.1016_j.cell.2022.10.030
  - septin-root21-sources-doi-10.1007_s00294-011-0339-1
  - septin-root21-sources-keeling2010-pmc
  - septin-root21-sources-jin2022-author-publications
  - septin-gadelha-indexed-body
  - septin-lacomble-indexed-methods
- check_id: historical-adapter-runner
  name: Retained historical adapter runner availability
  status: unavailable
  required: false
  target_ids:
  - GO:0031969
  - GO:0009707
  - GO:0009570
  - GO:0009534
  - GO:0009535
  - GO:0046858
  - GO:0033105
  - GO:0005801
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
- check_id: chloroplast_membrane-uniprot-verify
  name: Native chloroplast membrane UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0031969
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chloroplast_membrane.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-chloroplast_membrane-verify
- check_id: chloroplast_membrane-uniprot-causal
  name: Native chloroplast membrane UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0031969
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chloroplast_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-chloroplast_membrane-causal
- check_id: chloroplast_outer_membrane-uniprot-verify
  name: Native chloroplast outer membrane UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0009707
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chloroplast_outer_membrane.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-chloroplast_outer_membrane-verify
- check_id: chloroplast_outer_membrane-uniprot-causal
  name: Native chloroplast outer membrane UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0009707
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chloroplast_outer_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-chloroplast_outer_membrane-causal
- check_id: chloroplast_stroma-uniprot-verify
  name: Native chloroplast stroma UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0009570
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chloroplast_stroma.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-chloroplast_stroma-verify
- check_id: chloroplast_stroma-uniprot-causal
  name: Native chloroplast stroma UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0009570
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chloroplast_stroma.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-chloroplast_stroma-causal
- check_id: chloroplast_thylakoid-uniprot-verify
  name: Native chloroplast thylakoid UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0009534
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chloroplast_thylakoid.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-chloroplast_thylakoid-verify
- check_id: chloroplast_thylakoid-uniprot-causal
  name: Native chloroplast thylakoid UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0009534
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chloroplast_thylakoid.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-chloroplast_thylakoid-causal
- check_id: chloroplast_thylakoid_lumen-uniprot-verify
  name: Native chloroplast thylakoid lumen UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0009543
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chloroplast_thylakoid_lumen.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-chloroplast_thylakoid_lumen-verify
- check_id: chloroplast_thylakoid_lumen-uniprot-causal
  name: Native chloroplast thylakoid lumen UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0009543
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chloroplast_thylakoid_lumen.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-chloroplast_thylakoid_lumen-causal
- check_id: chloroplast_thylakoid_membrane-uniprot-verify
  name: Native chloroplast thylakoid membrane UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0009535
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chloroplast_thylakoid_membrane.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-chloroplast_thylakoid_membrane-verify
- check_id: chloroplast_thylakoid_membrane-uniprot-causal
  name: Native chloroplast thylakoid membrane UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0009535
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chloroplast_thylakoid_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-chloroplast_thylakoid_membrane-causal
- check_id: chlorosome-uniprot-verify
  name: Native chlorosome UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0046858
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chlorosome.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-chlorosome-verify
- check_id: chlorosome-uniprot-causal
  name: Native chlorosome UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0046858
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chlorosome.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-chlorosome-causal
- check_id: chlorosome_envelope-uniprot-verify
  name: Native chlorosome envelope UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0033105
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chlorosome_envelope.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-chlorosome_envelope-verify
- check_id: chlorosome_envelope-uniprot-causal
  name: Native chlorosome envelope UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0033105
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chlorosome_envelope.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-chlorosome_envelope-causal
- check_id: ciliary_pocket_membrane-uniprot-verify
  name: Native ciliary pocket membrane UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0020018
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/ciliary_pocket_membrane.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-ciliary_pocket_membrane-verify
- check_id: ciliary_pocket_membrane-uniprot-causal
  name: Native ciliary pocket membrane UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0020018
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/ciliary_pocket_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-ciliary_pocket_membrane-causal
- check_id: cis_golgi_network-uniprot-verify
  name: Native cis golgi network UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0005801
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cis_golgi_network.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-cis_golgi_network-verify
- check_id: cis_golgi_network-uniprot-causal
  name: Native cis golgi network UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0005801
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cis_golgi_network.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-cis_golgi_network-causal
evidence:
- evidence_id: current-record-0
  kind: record_content
  reference: data/structures/membrane_organelle/chloroplast_membrane.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T10:20:14Z'
  support: context_only
  summary: Original frozen SHA256 115d9369e1b84a54e66028f079a8d140e72d40ec2fb5877e64fb592b6a085905;
    current SHA256 115d9369e1b84a54e66028f079a8d140e72d40ec2fb5877e64fb592b6a085905.
    Record bytes unchanged since the original review.
  snapshot_sha256: 115d9369e1b84a54e66028f079a8d140e72d40ec2fb5877e64fb592b6a085905
- evidence_id: original-review-0
  kind: prior_review
  reference: reviews/structured/20261021T110921Z-chloroplast-membrane-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T10:20:14Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: a76189a76a9dd5f2f9121ea2d9931a1eaa30242657b30eebd265187fbdeac676
- evidence_id: current-record-1
  kind: record_content
  reference: data/structures/membrane_organelle/chloroplast_outer_membrane.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T10:20:14Z'
  support: context_only
  summary: Original frozen SHA256 f499d6317b1546cf0d578f54d04df76a8af3c54746f29db6b2d7af0244b0075d;
    current SHA256 f499d6317b1546cf0d578f54d04df76a8af3c54746f29db6b2d7af0244b0075d.
    Record bytes unchanged since the original review.
  snapshot_sha256: f499d6317b1546cf0d578f54d04df76a8af3c54746f29db6b2d7af0244b0075d
- evidence_id: original-review-1
  kind: prior_review
  reference: reviews/structured/20261021T110923Z-chloroplast-outer-membrane-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T10:20:14Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: c8f22919f640db5735a0a8768eb75f73ab841bcc9dfc028c98d29c9bbfdd0b1d
- evidence_id: current-record-2
  kind: record_content
  reference: data/structures/membrane_organelle/chloroplast_stroma.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T10:20:14Z'
  support: context_only
  summary: Original frozen SHA256 cfdb0d3be9fba838d5288e478b39f922a4e11cbd240b689a2cbca7690c262b6a;
    current SHA256 cfdb0d3be9fba838d5288e478b39f922a4e11cbd240b689a2cbca7690c262b6a.
    Record bytes unchanged since the original review.
  snapshot_sha256: cfdb0d3be9fba838d5288e478b39f922a4e11cbd240b689a2cbca7690c262b6a
- evidence_id: original-review-2
  kind: prior_review
  reference: reviews/structured/20261021T110927Z-chloroplast-stroma-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T10:20:14Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: fad2c9ed334d31f3d23e9c207f85f54c2231b0f7167287251ce10ae9dfb80867
- evidence_id: current-record-3
  kind: record_content
  reference: data/structures/membrane_organelle/chloroplast_thylakoid.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T10:20:14Z'
  support: context_only
  summary: Original frozen SHA256 ed335bb9dbdc4ba22ed33046fa25d64796c2eadefe71b1e04eaeb7d67156723c;
    current SHA256 edf435ef39aeb8c0fa0e572768a0e7f599b7177945d1c7a621d3d810bbaf17cd.
    Changed record reassessed against current sources.
  snapshot_sha256: edf435ef39aeb8c0fa0e572768a0e7f599b7177945d1c7a621d3d810bbaf17cd
- evidence_id: original-review-3
  kind: prior_review
  reference: reviews/structured/20261021T110930Z-chloroplast-thylakoid-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T10:20:14Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: b39043ffc03ba6a10006a18d878a703d33bb0864cf343b5377e39e646590ea1a
- evidence_id: current-record-4
  kind: record_content
  reference: data/structures/membrane_organelle/chloroplast_thylakoid_lumen.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T10:20:14Z'
  support: context_only
  summary: Original frozen SHA256 6efd0a2e86462ae192dc2f27f9edc945dc6b522a31d8e233458cd25e661fb2af;
    current SHA256 6efd0a2e86462ae192dc2f27f9edc945dc6b522a31d8e233458cd25e661fb2af.
    Record bytes unchanged since the original review.
  snapshot_sha256: 6efd0a2e86462ae192dc2f27f9edc945dc6b522a31d8e233458cd25e661fb2af
- evidence_id: original-review-4
  kind: prior_review
  reference: reviews/structured/20261021T110931Z-chloroplast-thylakoid-lumen-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T10:20:14Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 2f261f4cc32831358b5f4ee4acecaabb66253d7bb02dcff457055b8ec368ff46
- evidence_id: current-record-5
  kind: record_content
  reference: data/structures/membrane_organelle/chloroplast_thylakoid_membrane.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T10:20:14Z'
  support: context_only
  summary: Original frozen SHA256 16f50bd615bee75edd15004622bae49a9a25e71dd4b9573584ca1659139d0999;
    current SHA256 16f50bd615bee75edd15004622bae49a9a25e71dd4b9573584ca1659139d0999.
    Record bytes unchanged since the original review.
  snapshot_sha256: 16f50bd615bee75edd15004622bae49a9a25e71dd4b9573584ca1659139d0999
- evidence_id: original-review-5
  kind: prior_review
  reference: reviews/structured/20261021T110932Z-chloroplast-thylakoid-membrane-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T10:20:14Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: be8deef886b2ef883bd4c18f5079c12552a8bd1c4a985a15e7c69baf357a9fa2
- evidence_id: current-record-6
  kind: record_content
  reference: data/structures/membrane_organelle/chlorosome.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T10:20:14Z'
  support: context_only
  summary: Original frozen SHA256 c68416577a67653e152c1a57c65ec074d98950a9a1c4d0023946a0510044b8e9;
    current SHA256 be2261521f06e087e2edd95af366813a289dba202239800a2c715033bd0105da.
    Changed record reassessed against current sources.
  snapshot_sha256: be2261521f06e087e2edd95af366813a289dba202239800a2c715033bd0105da
- evidence_id: original-review-6
  kind: prior_review
  reference: reviews/structured/20261021T110934Z-chlorosome-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T10:20:14Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 5258ec88b9c9f6c87dae0507de4ed2f6ac9eedea0badd7bb1ef4f6edc8f5c644
- evidence_id: current-record-7
  kind: record_content
  reference: data/structures/membrane_organelle/chlorosome_envelope.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T10:20:14Z'
  support: context_only
  summary: Original frozen SHA256 2514acd0c5f9bd7c73e1c1d77096301858323dbfe5fa35434b09c501b5fbf8ed;
    current SHA256 d39583d641a4c6070008f52e29246d1659bf86b1158799b1c30caf2e272ef903.
    Changed record reassessed against current sources.
  snapshot_sha256: d39583d641a4c6070008f52e29246d1659bf86b1158799b1c30caf2e272ef903
- evidence_id: original-review-7
  kind: prior_review
  reference: reviews/structured/20261021T110935Z-chlorosome-envelope-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T10:20:14Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 71d6c9bad049169189915002337cab00a18684911c9d61043e8ca33ed476d65a
- evidence_id: current-record-8
  kind: record_content
  reference: data/structures/membrane_organelle/ciliary_pocket_membrane.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T10:20:14Z'
  support: context_only
  summary: Original frozen SHA256 acdf228c05817a740e627e5885200d543b8cb91f6ac94aefa4f5bf954255b3e0;
    current SHA256 acdf228c05817a740e627e5885200d543b8cb91f6ac94aefa4f5bf954255b3e0.
    Record bytes unchanged since the original review.
  snapshot_sha256: acdf228c05817a740e627e5885200d543b8cb91f6ac94aefa4f5bf954255b3e0
- evidence_id: original-review-8
  kind: prior_review
  reference: reviews/structured/20261021T110936Z-ciliary-pocket-membrane-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T10:20:14Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 32694ec8da0b5a28df1fc31d0e85d4ec569f290f30ee42788653100d89bac2be
- evidence_id: current-record-9
  kind: record_content
  reference: data/structures/membrane_organelle/cis_golgi_network.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T10:20:14Z'
  support: context_only
  summary: Original frozen SHA256 369cae5270aeacd25a94317be3b005167773bd89a5e4c2583061fa24cd79f31d;
    current SHA256 369cae5270aeacd25a94317be3b005167773bd89a5e4c2583061fa24cd79f31d.
    Record bytes unchanged since the original review.
  snapshot_sha256: 369cae5270aeacd25a94317be3b005167773bd89a5e4c2583061fa24cd79f31d
- evidence_id: original-review-9
  kind: prior_review
  reference: reviews/structured/20261021T110938Z-cis-golgi-network-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T10:20:14Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: c5490c5558528e3c04ac297eab3a35e5850a9f26d13fd543c248b26bd4416f12
- evidence_id: plaque-current-3
  kind: record_content
  reference: data/structures/membrane_organelle/chloroplast_thylakoid.yaml
  locator: Complete maintained YAML at frozen source fa6c7f0034c57fac03d026ce0ddb8aaa4bd4b2e3;
    all fields, graphs, discussions and history
  accessed_at: '2026-11-03T10:14:14.575042Z'
  summary: Entire target independently inspected. Two added parthood edges and their
    evidence are substantively refreshed against current authorities. Native PROPOSED
    status is unchanged; no target image is declared.
  support: supports
  snapshot_sha256: edf435ef39aeb8c0fa0e572768a0e7f599b7177945d1c7a621d3d810bbaf17cd
- evidence_id: plaque-original-3
  kind: prior_review
  reference: reviews/structured/20261021T110930Z-chloroplast-thylakoid-audit/review.yaml
  locator: Entire original authoritative YAML and Markdown; source hashes, findings,
    checks and assessments
  accessed_at: '2026-11-03T10:14:14.575042Z'
  summary: Original native validation and exact render passed; historical target bytes
    match the frozen hash. No original scientific finding exists. The old observation
    remains immutable rather than being silently relabeled current.
  support: supports
  snapshot_sha256: b39043ffc03ba6a10006a18d878a703d33bb0864cf343b5377e39e646590ea1a
- evidence_id: plaque-current-4
  kind: record_content
  reference: data/structures/membrane_organelle/chloroplast_thylakoid_lumen.yaml
  locator: Complete maintained YAML at frozen source fa6c7f0034c57fac03d026ce0ddb8aaa4bd4b2e3;
    all fields, graphs, discussions and history
  accessed_at: '2026-11-03T10:14:14.575042Z'
  summary: Entire target independently inspected. Current target hash matches the
    original frozen target hash. Native PROPOSED status is unchanged; no target image
    is declared.
  support: supports
  snapshot_sha256: 6efd0a2e86462ae192dc2f27f9edc945dc6b522a31d8e233458cd25e661fb2af
- evidence_id: plaque-original-4
  kind: prior_review
  reference: reviews/structured/20261021T110931Z-chloroplast-thylakoid-lumen-audit/review.yaml
  locator: Entire original authoritative YAML and Markdown; source hashes, findings,
    checks and assessments
  accessed_at: '2026-11-03T10:14:14.575042Z'
  summary: Original native validation and exact render passed; historical target bytes
    match the frozen hash. No original scientific finding exists. The old observation
    remains immutable rather than being silently relabeled current.
  support: supports
  snapshot_sha256: 2f261f4cc32831358b5f4ee4acecaabb66253d7bb02dcff457055b8ec368ff46
- evidence_id: plaque-current-5
  kind: record_content
  reference: data/structures/membrane_organelle/chloroplast_thylakoid_membrane.yaml
  locator: Complete maintained YAML at frozen source fa6c7f0034c57fac03d026ce0ddb8aaa4bd4b2e3;
    all fields, graphs, discussions and history
  accessed_at: '2026-11-03T10:14:14.575042Z'
  summary: Entire target independently inspected. Current target hash matches the
    original frozen target hash. Native PROPOSED status is unchanged; no target image
    is declared.
  support: supports
  snapshot_sha256: 16f50bd615bee75edd15004622bae49a9a25e71dd4b9573584ca1659139d0999
- evidence_id: plaque-original-5
  kind: prior_review
  reference: reviews/structured/20261021T110932Z-chloroplast-thylakoid-membrane-audit/review.yaml
  locator: Entire original authoritative YAML and Markdown; source hashes, findings,
    checks and assessments
  accessed_at: '2026-11-03T10:14:14.575042Z'
  summary: Original native validation and exact render passed; historical target bytes
    match the frozen hash. No original scientific finding exists. The old observation
    remains immutable rather than being silently relabeled current.
  support: supports
  snapshot_sha256: be8deef886b2ef883bd4c18f5079c12552a8bd1c4a985a15e7c69baf357a9fa2
- evidence_id: plaque-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Frozen native rules for evidence, component identity, assembly necessity,
    graph scope and structured-source applicability
  accessed_at: '2026-11-03T10:14:14.575042Z'
  summary: The native contract separates scientific curation from review, material
    constitution from molecular necessity, and exact parthood from subclass identity.
    Actual source coverage must be assessed when molecular pathways are named.
  support: context_only
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: plaque-rubric
  kind: authority
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Frozen native rules for evidence, component identity, assembly necessity,
    graph scope and structured-source applicability
  accessed_at: '2026-11-03T10:14:14.575042Z'
  summary: The native contract separates scientific curation from review, material
    constitution from molecular necessity, and exact parthood from subclass identity.
    Actual source coverage must be assessed when molecular pathways are named.
  support: context_only
  snapshot_sha256: e6b9e4b16a58c54402bed7bbee2c8b94a91d37562e8b0ee8b94ff0c829184a70
- evidence_id: plaque-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Frozen native rules for evidence, component identity, assembly necessity,
    graph scope and structured-source applicability
  accessed_at: '2026-11-03T10:14:14.575042Z'
  summary: The native contract separates scientific curation from review, material
    constitution from molecular necessity, and exact parthood from subclass identity.
    Actual source coverage must be assessed when molecular pathways are named.
  support: context_only
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: plaque-schema-policy
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Frozen native rules for evidence, component identity, assembly necessity,
    graph scope and structured-source applicability
  accessed_at: '2026-11-03T10:14:14.575042Z'
  summary: The native contract separates scientific curation from review, material
    constitution from molecular necessity, and exact parthood from subclass identity.
    Actual source coverage must be assessed when molecular pathways are named.
  support: context_only
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: plaque-thylakoid-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009534,GO:0009579,GO:0031976,GO:0009507,GO:0009535,GO:0009543,GO:0009570,GO:0009767,GO:0031978,GO:0042651,GO:0055035,GO:0019684
  locator: 'All12 requested GO terms: definitions, exact identifiers, comment and
    typed children; direct GO0009534 part_of children and GO0009507 whole-thylakoid
    partOf child inspected'
  accessed_at: '2026-11-03T10:10:37.402692Z'
  summary: Current terms separate whole thylakoid0009534, membrane0009535 and lumen0009543.
    GO0009534 directly lists membrane and lumen as part_of children. Definitions and
    biological-process entries support the bounded topology and photosynthetic functions;
    the thylakoid comment supplies the record’s explicit non-organelle interpretation.
  support: supports
  snapshot_sha256: 92d47639b6085622899587365a26395fab0c4e3b13fc1b06ad31f4a5032acc2c
- evidence_id: plaque-isa-0009534
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009534/ancestors?relations=is_a
  locator: Explicit relations=is_a endpoint and complete returned ancestor list
  accessed_at: '2026-11-03T10:10:38.915676Z'
  summary: The maintained broader plastid/generic thylakoid, lumen or membrane parents
    are in the is_a-only closure. Parthood is separately checked using typed relations;
    no partOf-to-isA substitution is made.
  support: supports
  snapshot_sha256: 824e5d91eed9b66cf761df5f0a79e90e674dc509417347b48bf246a2460d38ff
- evidence_id: plaque-isa-0009543
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009543/ancestors?relations=is_a
  locator: Explicit relations=is_a endpoint and complete returned ancestor list
  accessed_at: '2026-11-03T10:10:38.939404Z'
  summary: The maintained broader plastid/generic thylakoid, lumen or membrane parents
    are in the is_a-only closure. Parthood is separately checked using typed relations;
    no partOf-to-isA substitution is made.
  support: supports
  snapshot_sha256: 3a34ba6b8f2a48743a2fb6cfe59bcc70975ce9be9cc13e5dd83ea9cb92d59471
- evidence_id: plaque-isa-0009535
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009535/ancestors?relations=is_a
  locator: Explicit relations=is_a endpoint and complete returned ancestor list
  accessed_at: '2026-11-03T10:10:39.179233Z'
  summary: The maintained broader plastid/generic thylakoid, lumen or membrane parents
    are in the is_a-only closure. Parthood is separately checked using typed relations;
    no partOf-to-isA substitution is made.
  support: supports
  snapshot_sha256: b4b7ea337082bfbc851f0576406e9821ec7f1a0dec09984cab0b6325af5d08b0
- evidence_id: plaque-thylakoid-agent-SL-0056
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0056.json
  locator: Native definition, GO correspondence, immediate isA and partOf objects
    plus inherited hierarchy
  accessed_at: '2026-11-03T10:10:37.402905Z'
  summary: SL0056 identifies whole chloroplast thylakoid under plastid thylakoid and
    part of chloroplast. SL0057 and SL0058 directly name chloroplast thylakoid as
    partOf host, while their own isA parents are plastid lumen/membrane. The broader
    plastid-thylakoid relationship is inherited, not a different exact structure.
    The source’s single-lumen statement is explicitly qualified as thought, not proven
    here.
  support: supports
  snapshot_sha256: 180c1e15539e59f5cbe7f5c5539af13380b4d3010eef9ce3950e38615f478624
- evidence_id: plaque-thylakoid-agent-SL-0057
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0057.json
  locator: Native definition, GO correspondence, immediate isA and partOf objects
    plus inherited hierarchy
  accessed_at: '2026-11-03T10:10:37.402972Z'
  summary: SL0056 identifies whole chloroplast thylakoid under plastid thylakoid and
    part of chloroplast. SL0057 and SL0058 directly name chloroplast thylakoid as
    partOf host, while their own isA parents are plastid lumen/membrane. The broader
    plastid-thylakoid relationship is inherited, not a different exact structure.
    The source’s single-lumen statement is explicitly qualified as thought, not proven
    here.
  support: supports
  snapshot_sha256: 87f24980e13db67fbfb9fd757639366068a4af0424a21bbaf1ff5a2338e52f44
- evidence_id: plaque-thylakoid-agent-SL-0058
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0058.json
  locator: Native definition, GO correspondence, immediate isA and partOf objects
    plus inherited hierarchy
  accessed_at: '2026-11-03T10:10:37.403059Z'
  summary: SL0056 identifies whole chloroplast thylakoid under plastid thylakoid and
    part of chloroplast. SL0057 and SL0058 directly name chloroplast thylakoid as
    partOf host, while their own isA parents are plastid lumen/membrane. The broader
    plastid-thylakoid relationship is inherited, not a different exact structure.
    The source’s single-lumen statement is explicitly qualified as thought, not proven
    here.
  support: supports
  snapshot_sha256: 2f36a70ab825e0e0f5d2936a98e1938b3bc6dcf279d8cd017176b064a10588da
- evidence_id: plaque-thylakoid-agent-NCBITaxon-33090
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/33090
  locator: Native taxId, scientificName, rank and lineage; not prevalence or experimental
    stock
  accessed_at: '2026-11-03T10:10:37.403121Z'
  summary: ENA confirms Viridiplantae kingdom33090. Occurrence and culture context
    require the independently inspected literature.
  support: supports
  snapshot_sha256: b1394e36c6896d7ec64cdb301a239f2bc49bc435a22cc21fdba8fdc6217e2d11
- evidence_id: plaque-thylakoid-agent-NCBITaxon-3055
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3055
  locator: Native taxId, scientificName, rank and lineage; not prevalence or experimental
    stock
  accessed_at: '2026-11-03T10:10:37.403152Z'
  summary: ENA confirms Chlamydomonas reinhardtii species3055. Occurrence and culture
    context require the independently inspected literature.
  support: supports
  snapshot_sha256: e3861fe6706cefe2e079e15c0178a65e95efaad3890f548f25e721553eaa93a0
- evidence_id: plaque-thylakoid-agent-engel2015-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.7554%2FeLife.04889
  locator: 'Exact DOI query: title, authors, DOI/PMID/PMCID, publication type and
    complete abstract'
  accessed_at: '2026-11-03T10:10:38.011901Z'
  summary: Native bibliography identifies Native architecture of the Chlamydomonas
    chloroplast revealed by in situ cryo-electron tomography.; Engel BD, Schaffer
    M, Kuhn Cuellar L, Villa E, Plitzko JM, Baumeister W.. This is bibliographic/abstract
    evidence; body coverage is declared separately.
  support: supports
  snapshot_sha256: e871243bee6520756b75290d986d9df20b09b14d80b6ba888a5a1048eeb85e9d
- evidence_id: plaque-thylakoid-agent-perez2024-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1146%2Fannurev-cellbio-120823-022747&format=json&resultType=core
  locator: 'Exact DOI query: title, authors, DOI/PMID/PMCID, publication type and
    complete abstract'
  accessed_at: '2026-11-03T10:10:38.187008Z'
  summary: Native bibliography identifies Evolution of Thylakoid Structural Diversity.;
    Perez-Boerema A, Engel BD, Wietrzynski W.. This is bibliographic/abstract evidence;
    body coverage is declared separately.
  support: supports
  snapshot_sha256: f9df3427bb3b35764922628c9e89cc9378fa7875a4a103bde71a75b130d54926
- evidence_id: plaque-thylakoid-agent-doi-10.1007_s00294-011-0339-1
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1007/s00294-011-0339-1
  locator: 'Exact DOI query: title, authors, DOI/PMID/PMCID, publication type and
    complete abstract'
  accessed_at: '2026-11-03T10:10:38.258209Z'
  summary: 'Native bibliography identifies The chloroplast proteome: a survey from
    the Chlamydomonas reinhardtii perspective with a focus on distinctive features.;
    Terashima M, Specht M, Hippler M.. This is bibliographic/abstract evidence; body
    coverage is declared separately.'
  support: supports
  snapshot_sha256: aec76518f370734a76392741bffd319ac61df223c77fad628910ec04da56412e
- evidence_id: plaque-thylakoid-agent-doi-10.1098_rstb.2009.0103
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1098/rstb.2009.0103
  locator: 'Exact DOI query: title, authors, DOI/PMID/PMCID, publication type and
    complete abstract'
  accessed_at: '2026-11-03T10:10:38.555892Z'
  summary: Native bibliography identifies The endosymbiotic origin, diversification
    and fate of plastids.; Keeling PJ.. This is bibliographic/abstract evidence; body
    coverage is declared separately.
  support: supports
  snapshot_sha256: 63c6291480d57ca01d4eb770792f919c0e3128eeaae04894f1ed2f2f3fc0e886
- evidence_id: plaque-thylakoid-agent-engel2015-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4292175.1/PMC4292175.1.xml
  locator: 'Primary JATS: Introduction; Results s2-1,s2-2,s2-3; Discussion s3-1,s3-2;
    Methods s4-1 through s4-5. Included figure captions are text, not pixel or raw
    tomogram inspection.'
  accessed_at: '2026-11-03T10:10:38.043247Z'
  summary: Engel2015 examines native C.reinhardtii CC-124(137c), grown in TAP under
    constant light, using cryo-FIB and in situ cryo-ET. The body supports membrane/lumen
    separation and variable stacked/interconnecting architecture. Confined tomograms
    do not prove one globally continuous lumen; rare envelope connections and proposed
    exchange/biogenesis routes remain bounded interpretations, not universal formation
    necessities.
  support: supports
  snapshot_sha256: 16b5f264ce209350b41d8797dc53e59d7e3d2b1b8f14ca35ca21c0752e7bcb4e
- evidence_id: plaque-thylakoid-agent-engel2015-correction
  kind: primary_source
  reference: https://elifesciences.org/articles/11383
  locator: Complete publisher correction paragraph and linked original-paper identity
  accessed_at: '2026-11-03T10:10:38.177603Z'
  summary: The correction changes the Figure3 scale-bar unit from micrometres to nanometres,
    retaining200nm. None of the three records asserts that image or a numerical dimension,
    so no maintained claim requires correction.
  support: context_only
  snapshot_sha256: 0c2dd2f375bac649b4209c50e6d7593ca071e5931b423d01879abd231cb784f2
- evidence_id: plaque-thylakoid-agent-terashima2011-pdf
  kind: authority
  reference: https://link.springer.com/content/pdf/10.1007/s00294-011-0339-1.pdf
  locator: 'Actual %PDF body, printedpp151–156: Introduction and Photosynthesis section;
    extracted text through the section end before Chlorophyll biosynthesis. No figure-pixel,
    supplementary proteome or downstream metabolic-section audit.'
  accessed_at: '2026-11-03T10:10:38.518294Z'
  summary: Terashima/Specht/Hippler2011 is a secondary review. It supports thylakoid
    photosynthetic core complexes, electron transfer and the pH gradient, with distinct
    algal/vascular-plant antennae and regulatory responses. Localization, sequence
    comparison and qE/state-transition perturbations do not establish a universal
    membrane-formation requirement or a complete constituent inventory.
  support: supports
  snapshot_sha256: e42edb346d375e4e083e2eb79c6d9eff9fc217513e1ae9ecf808acb143129c6b
- evidence_id: plaque-thylakoid-agent-keeling2010-pmc
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2817223/
  locator: 'Actual secondary PMC HTML: abstract and §1 primary-plastid/green-lineage
    paragraphs; §6 distinction between loss of photosynthesis and plastid loss'
  accessed_at: '2026-11-03T10:10:38.582642Z'
  summary: Keeling2010 supports broad green-lineage plastid context while explicitly
    distinguishing retained nonphotosynthetic plastids from plastid loss. It does
    not independently measure thylakoid prevalence or universal photosynthetic status.
  support: supports
  snapshot_sha256: 7c0eea300c6d6a694668d62cda30305d8c92b42f72192c66518f1251414c9f95
- evidence_id: plaque-thylakoid-agent-perez2024-publisher
  kind: authority
  reference: https://www.annualreviews.org/content/journals/10.1146/annurev-cellbio-120823-022747
  locator: Actual unsuccessful native HTTP response; not scientific body content
  accessed_at: '2026-11-03T10:10:38.206422Z'
  summary: Fresh native request returnedHTTP403. Successful separately scoped alternatives
    do not convert this response into article evidence.
  support: context_only
  snapshot_sha256: 98f6c51430d1ec8a02651e1c8892e2f05ed0120f72983355b570e3366c064e06
- evidence_id: plaque-thylakoid-agent-keeling2010-jats
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2817223/fullTextXML
  locator: Actual unsuccessful native HTTP response; not scientific body content
  accessed_at: '2026-11-03T10:10:38.666265Z'
  summary: Fresh native request returnedHTTP500. Successful separately scoped alternatives
    do not convert this response into article evidence.
  support: context_only
  snapshot_sha256: 20adee96a05bcf94d4aab01be9624a9269e2af468301e30398059aa95b774f02
- evidence_id: plaque-perez-body-introduction
  kind: authority
  reference: https://doi.org/10.1146/annurev-cellbio-120823-022747
  locator: Cached browser-returned official publisher Introduction and evolutionary
    diversification paragraphs; unrelated hits excluded; packet hash below, not native
    body HTML
  accessed_at: '2026-11-03T09:37:31Z'
  summary: Perez2024 secondary body context supports thylakoid membrane/lumen compartmentalization
    and qualitative photosynthetic green-lineage occurrence, not every nonphotosynthetic
    plastid or quantitative prevalence. Reused snapshot independently reread; original09:34/09:37Z
    capture time is retained, not claimed fresh.
  support: supports
  snapshot_sha256: cbf836e7549f5d05b8b7fbbd2e975e1537dec5e4e051f22e74473117c8f73b7c
- evidence_id: plaque-perez-body-electron-transport
  kind: authority
  reference: https://doi.org/10.1146/annurev-cellbio-120823-022747
  locator: Cached browser-returned official publisher Electron Transport Chain Complexes
    subsection only; packet hash below, not native body HTML
  accessed_at: '2026-11-03T09:34:09Z'
  summary: The secondary review locates photosystems, quinone/soluble carriers and
    gradient-coupled ATP production at the membrane/lumen/stroma interfaces. It supports
    the broad functional claims without imposing a universal experimentally necessary
    protein inventory. Reused snapshot independently reread; original09:34/09:37Z
    capture time is retained, not claimed fresh.
  support: supports
  snapshot_sha256: 56c1f70a51fcbece7ecb33585c2ab81ad624de83df306e933f7556debff22110
- evidence_id: plaque-catalogue
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Entire current /api/datasets response, all returned organism/dataset rows;
    no pagination
  accessed_at: '2026-11-03T10:10:38.867300Z'
  summary: No current catalogue organism matches Chlamydomonas or the records’ green-lineage
    plastid hosts. The S.elongatus dataset is a different cyanobacterial organism
    and cannot supply chloroplast-thylakoid molecular evidence. Downstream gene/module
    queries are therefore not applicable; absence from the catalogue is not biological
    absence.
  support: supports
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: plaque-historical-runner
  kind: validation
  reference: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb datasets
  locator: Historical00:49Z receipt and stdout/stderr independently reread and hash-verified
  accessed_at: '2026-11-03T00:49:00.863225Z'
  summary: Historical runner exited1 before dataset execution due OS PermissionError
    reading pyvenv.cfg. No fresh runner invocation or success is claimed. Current
    source catalogue is the separately inspected permitted fallback.
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: plaque-native-chloroplast_thylakoid-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chloroplast_thylakoid.yaml
    --verify
  locator: Actual root-owned receipt and exact stdout independently read and hash-verified
  accessed_at: '2026-11-03T10:11:22.533331Z'
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  support: supports
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: plaque-native-chloroplast_thylakoid-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chloroplast_thylakoid.yaml
    --causal-graphs
  locator: Actual root-owned receipt and exact stdout independently read and hash-verified
  accessed_at: '2026-11-03T10:11:22.957770Z'
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
  support: supports
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
- evidence_id: plaque-native-chloroplast_thylakoid_lumen-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chloroplast_thylakoid_lumen.yaml
    --verify
  locator: Actual root-owned receipt and exact stdout independently read and hash-verified
  accessed_at: '2026-11-03T10:11:23.385712Z'
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  support: supports
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: plaque-native-chloroplast_thylakoid_lumen-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chloroplast_thylakoid_lumen.yaml
    --causal-graphs
  locator: Actual root-owned receipt and exact stdout independently read and hash-verified
  accessed_at: '2026-11-03T10:11:23.801841Z'
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
  support: supports
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
- evidence_id: plaque-native-chloroplast_thylakoid_membrane-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chloroplast_thylakoid_membrane.yaml
    --verify
  locator: Actual root-owned receipt and exact stdout independently read and hash-verified
  accessed_at: '2026-11-03T10:11:24.226174Z'
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  support: supports
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: plaque-native-chloroplast_thylakoid_membrane-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chloroplast_thylakoid_membrane.yaml
    --causal-graphs
  locator: Actual root-owned receipt and exact stdout independently read and hash-verified
  accessed_at: '2026-11-03T10:11:24.648488Z'
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
  support: supports
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
- evidence_id: micro-review-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Evidence Rules; Structured Source Cross-Checks; Missing Things; Workflow
  accessed_at: '2026-11-03T10:19:48.388792Z'
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
  summary: Native named-gene, protein and pathway claims trigger applicability assessment
    irrespective of transcriptomic assertions. Source absence must be bounded. No
    record or immutable review mutation is authorized for this independent pass.
  support: supports
- evidence_id: micro-review-config
  kind: authority
  reference: conf/record_review.yaml
  locator: Active skills and rubric routes
  accessed_at: '2026-11-03T10:19:48.388792Z'
  snapshot_sha256: d3334a12b8a616a7638f1195748085d2b543fba7df67ad4ff8fcc0ac18f2d3ee
  summary: Configuration, native review skill, review profile and output contract
    reread. Seventeen common policy/schema/verifier inputs are byte-identical to the
    previous reviewed cohort; their prior contract interpretation is retained with
    current critical rule checks.
  support: supports
- evidence_id: micro-review-profile
  kind: authority
  reference: docs/record-review-profile.md
  locator: Issue-only persistence; Native questions; Native checks
  accessed_at: '2026-11-03T10:19:48.388792Z'
  snapshot_sha256: 6a49c8d35f0a94082a9ad0b8bd8c6a929d85de8339141955f3779bd7ab0eb7e4
  summary: Issue-bearing successor may document clean refreshed claims alongside preserved
    unresolved findings. Native QC and source verification do not by themselves certify
    the scientific assertions.
  support: supports
- evidence_id: micro-schema-necessity
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: EssentialityEnum.ESSENTIAL; CausalNode.component_ref
  accessed_at: '2026-11-03T10:19:48.388792Z'
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
  summary: ESSENTIAL means the structure does not form without the component. A graph
    component_ref denotes the local own component; constituent identity, function,
    viability and organelle-formation necessity remain distinct.
  support: supports
- evidence_id: micro-graph-contract
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Node identity, component links and edge-level claim scope
  accessed_at: '2026-11-03T10:19:48.388792Z'
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
  summary: A multi-protein baseplate is a structure node. Coarse topological or energy-flow
    edges do not establish molecular completeness, direct universal contacts or formation
    necessity.
  support: supports
- evidence_id: micro-review-schema
  kind: authority
  reference: schema/record_review.yaml
  locator: EvidenceKind; Area; FindingReference; Action
  accessed_at: '2026-11-03T10:19:48.388792Z'
  snapshot_sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
  summary: Secondary review context uses authority with explicit scope, schema is
    a valid assessment area, and successor findings require exact repository/review/finding
    lineage.
  support: supports
- evidence_id: micro-original-validation-inputs
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/adversary-microtubule/original-validation-inputs.json
  locator: Three original validate commands, native render --content comparisons,
    original-source and current target blob hashes
  accessed_at: '2026-11-03T10:16:31.103557Z'
  snapshot_sha256: 311caab6996691f510a76cd538d4ce6cb07c96735e943385dbee1da8007d149a
  summary: All three original bundles validate and render byte-identically. Original
    target hashes match git source9c0446c4. Chlorosome and envelope are stale; cis-Golgi
    target is unchanged. These results do not convert old full-corpus checks into
    current checks.
  support: supports
- evidence_id: micro-record-chlorosome
  kind: record_content
  reference: data/structures/membrane_organelle/chlorosome.yaml
  locator: Complete current target YAML at fa6c7f0034c57fac03d026ce0ddb8aaa4bd4b2e3
  accessed_at: '2026-11-03T10:19:48.388792Z'
  snapshot_sha256: be2261521f06e087e2edd95af366813a289dba202239800a2c715033bd0105da
  summary: 'Entire record inspected: identity, definition, scope, components, protein
    examples, functions, taxon/canonical examples, graph, evidence, discussions and
    history. Current target differs from the original frozen record.'
  support: supports
- evidence_id: micro-prior-chlorosome
  kind: prior_review
  reference: reviews/structured/20261021T110934Z-chlorosome-audit/review.yaml
  locator: Entire immutable original YAML plus deterministic Markdown
  accessed_at: '2026-11-03T10:19:48.388792Z'
  snapshot_sha256: 5258ec88b9c9f6c87dae0507de4ed2f6ac9eedea0badd7bb1ef4f6edc8f5c644
  summary: Retained original 20261021T110934Z-chlorosome-audit; verdict needs_curation.
    Original source access dates and check provenance remain historical. Exact finding
    keys and occurrences are preserved in this report.
  support: supports
- evidence_id: micro-native-chlorosome-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/chlorosome-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chlorosome.yaml
    --verify; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/chlorosome-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T10:11:25.935969Z'
  snapshot_sha256: b26be661fa6eff24fabbd3376da078247b5a77fcc5301c0146df5493809b6df7
  summary: Actual exit0 at source fa6c7f0034c57fac03d026ce0ddb8aaa4bd4b2e3, 2026-11-03T10:11:24.680580+00:00
    to 2026-11-03T10:11:25.935969+00:00. Ten declared examples (seven reviewed, three
    unreviewed); causal graph has one PARTIAL_EXAMPLES accessory node (csmK lacks
    example) and one UNANCHORED_NO_UNIPROT generic reaction-center acceptor node.
    Corrected whole baseplate is STRUCTURE, not a missing protein example. Identity/coverage
    success does not establish localization or necessity.
  support: supports
- evidence_id: micro-native-chlorosome-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/chlorosome-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chlorosome.yaml
    --causal-graphs; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/chlorosome-uniprot-causal.log
    SHA256 c0b932b8875cdd028d1ca4ea4becedf1ee85d19859fdfcb5d5e0c7803d07df42
  accessed_at: '2026-11-03T10:11:26.357757Z'
  snapshot_sha256: cc82c0ec4b5861f7e19fda09fa0d14b169b6b0187bff7c12cf98ff0d8d2130df
  summary: Actual exit0 at source fa6c7f0034c57fac03d026ce0ddb8aaa4bd4b2e3, 2026-11-03T10:11:25.966660+00:00
    to 2026-11-03T10:11:26.357757+00:00. Ten declared examples (seven reviewed, three
    unreviewed); causal graph has one PARTIAL_EXAMPLES accessory node (csmK lacks
    example) and one UNANCHORED_NO_UNIPROT generic reaction-center acceptor node.
    Corrected whole baseplate is STRUCTURE, not a missing protein example. Identity/coverage
    success does not establish localization or necessity.
  support: supports
- evidence_id: micro-record-chlorosome_envelope
  kind: record_content
  reference: data/structures/membrane_organelle/chlorosome_envelope.yaml
  locator: Complete current target YAML at fa6c7f0034c57fac03d026ce0ddb8aaa4bd4b2e3
  accessed_at: '2026-11-03T10:19:48.388792Z'
  snapshot_sha256: d39583d641a4c6070008f52e29246d1659bf86b1158799b1c30caf2e272ef903
  summary: 'Entire record inspected: identity, definition, scope, components, protein
    examples, functions, taxon/canonical examples, graph, evidence, discussions and
    history. Current target differs from the original frozen record.'
  support: supports
- evidence_id: micro-prior-chlorosome_envelope
  kind: prior_review
  reference: reviews/structured/20261021T110935Z-chlorosome-envelope-audit/review.yaml
  locator: Entire immutable original YAML plus deterministic Markdown
  accessed_at: '2026-11-03T10:19:48.388792Z'
  snapshot_sha256: 71d6c9bad049169189915002337cab00a18684911c9d61043e8ca33ed476d65a
  summary: Retained original 20261021T110935Z-chlorosome-envelope-audit; verdict needs_curation.
    Original source access dates and check provenance remain historical. Exact finding
    keys and occurrences are preserved in this report.
  support: supports
- evidence_id: micro-native-chlorosome_envelope-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/chlorosome_envelope-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chlorosome_envelope.yaml
    --verify; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/chlorosome_envelope-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T10:11:27.380720Z'
  snapshot_sha256: f5023b4935c456d7804bef25a215dc146caf240b6a805458e54fdfa8b542f7b0
  summary: Actual exit0 at source fa6c7f0034c57fac03d026ce0ddb8aaa4bd4b2e3, 2026-11-03T10:11:26.389963+00:00
    to 2026-11-03T10:11:27.380720+00:00. Ten declared examples (seven reviewed, three
    unreviewed); causal graph has one PARTIAL_EXAMPLES node because csmK lacks an
    example. Corrected baseplate structure node is not a protein inventory failure.
    Identity/coverage success does not establish localization or necessity.
  support: supports
- evidence_id: micro-native-chlorosome_envelope-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/chlorosome_envelope-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chlorosome_envelope.yaml
    --causal-graphs; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/chlorosome_envelope-uniprot-causal.log
    SHA256 ce8445ca91d5abe4081756fe74beeb343e3acae44afb278945b3a29269f0f495
  accessed_at: '2026-11-03T10:11:27.794962Z'
  snapshot_sha256: 9110e211c3a9d8bf824cb95a03cd4ec666d6ec18a7100f44e37b7585e299f5e1
  summary: Actual exit0 at source fa6c7f0034c57fac03d026ce0ddb8aaa4bd4b2e3, 2026-11-03T10:11:27.412651+00:00
    to 2026-11-03T10:11:27.794962+00:00. Ten declared examples (seven reviewed, three
    unreviewed); causal graph has one PARTIAL_EXAMPLES node because csmK lacks an
    example. Corrected baseplate structure node is not a protein inventory failure.
    Identity/coverage success does not establish localization or necessity.
  support: supports
- evidence_id: micro-record-cis_golgi_network
  kind: record_content
  reference: data/structures/membrane_organelle/cis_golgi_network.yaml
  locator: Complete current target YAML at fa6c7f0034c57fac03d026ce0ddb8aaa4bd4b2e3
  accessed_at: '2026-11-03T10:19:48.388792Z'
  snapshot_sha256: 369cae5270aeacd25a94317be3b005167773bd89a5e4c2583061fa24cd79f31d
  summary: 'Entire record inspected: identity, definition, scope, components, protein
    examples, functions, taxon/canonical examples, graph, evidence, discussions and
    history. Target is byte-identical to the original frozen record.'
  support: supports
- evidence_id: micro-prior-cis_golgi_network
  kind: prior_review
  reference: reviews/structured/20261021T110938Z-cis-golgi-network-audit/review.yaml
  locator: Entire immutable original YAML plus deterministic Markdown
  accessed_at: '2026-11-03T10:19:48.388792Z'
  snapshot_sha256: c5490c5558528e3c04ac297eab3a35e5850a9f26d13fd543c248b26bd4416f12
  summary: Retained original 20261021T110938Z-cis-golgi-network-audit; verdict needs_curation.
    Original source access dates and check provenance remain historical. Exact finding
    keys and occurrences are preserved in this report.
  support: supports
- evidence_id: micro-native-cis_golgi_network-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/cis_golgi_network-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cis_golgi_network.yaml
    --verify; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/cis_golgi_network-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T10:11:28.977247Z'
  snapshot_sha256: 9695d51f4feda875a4fdc0c0742f19a9be8c5710a4c01250de49726b2ad3bdc8
  summary: Actual exit0 at source fa6c7f0034c57fac03d026ce0ddb8aaa4bd4b2e3, 2026-11-03T10:11:28.619985+00:00
    to 2026-11-03T10:11:28.977247+00:00. Empty protein-example inventory and zero
    GENE_OR_PROTEIN nodes; successful empty-scope command is not experimental molecular
    evidence. Identity/coverage success does not establish localization or necessity.
  support: supports
- evidence_id: micro-native-cis_golgi_network-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/cis_golgi_network-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cis_golgi_network.yaml
    --causal-graphs; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/cis_golgi_network-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-03T10:11:29.366997Z'
  snapshot_sha256: c91bca5f04a2fe3c74c16afdbb203b065ddb27819bc2d7010a95d377ba41fac1
  summary: Actual exit0 at source fa6c7f0034c57fac03d026ce0ddb8aaa4bd4b2e3, 2026-11-03T10:11:29.007528+00:00
    to 2026-11-03T10:11:29.366997+00:00. Empty protein-example inventory and zero
    GENE_OR_PROTEIN nodes; successful empty-scope command is not experimental molecular
    evidence. Identity/coverage success does not establish localization or necessity.
  support: supports
- evidence_id: micro-neighbor-baseplate
  kind: record_content
  reference: data/structures/energy_complex/chlorosome_baseplate_antenna_complex.yaml
  locator: Identity, definition, parentage, components, canonical example, graph and
    discussions
  accessed_at: '2026-11-03T10:19:48.388792Z'
  snapshot_sha256: 7ea00dedcd0998fc477737d6d2e8301e4e57a08e57378d19efe5e32a6ea8c92d
  summary: Frozen whole CsmA/BChl-a multi-protein baseplate identity supports corrected
    STRUCTURE nodes and internal grounding. This neighbor is boundary context only;
    its separately tracked mutant-preparation claim is not re-reviewed or resolved
    here.
  support: supports
- evidence_id: micro-neighbor-cgn-membrane
  kind: record_content
  reference: data/structures/membrane_organelle/cis_golgi_network_membrane.yaml
  locator: Identity, definition, hierarchy/parthood, synonyms and discussions
  accessed_at: '2026-11-03T10:19:48.388792Z'
  snapshot_sha256: c818f4de1c2fd8c36bc121d4389ce017c59526e083e6aefdf1b2a0041411da9c
  summary: Exact GO:0033106 boundary is distinct from the complete GO:0005801 network
    and generic lipid material; molecular residents are not inferred from the boundary.
  support: supports
- evidence_id: micro-neighbor-golgi
  kind: record_content
  reference: data/structures/membrane_organelle/golgi_apparatus.yaml
  locator: Identity, definition, hierarchy/parthood, has_part and discussions
  accessed_at: '2026-11-03T10:19:48.388792Z'
  snapshot_sha256: e3df76cd9d71ba04df9e5349475bd4191c31f93156acd422ef6b0223b88facca
  summary: Whole Golgi, stack and CGN are distinct structure scopes. Neighbor used
    only for boundary consistency, not a full scientific review or category-wide disposition.
  support: supports
- evidence_id: micro-chl-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0046858,GO:0043232,GO:0033105,GO:0015979
  locator: Exact QuickGO GO:0046858/0033105/0043232/0015979 definitions, names, synonyms,
    active flags and child relations
  accessed_at: '2026-11-03T10:11:00.710333Z'
  snapshot_sha256: 311aa9bdde571efbc2741945a2a4d73b13239ed30ec05c89398115367858b60a
  summary: Chlorosome is a pigment aggregate with monolayer envelope, correctly distinguished
    from a lipid bilayer-bounded organelle. Envelope is not an organelle membrane/envelope
    bilayer; photosynthesis is broader than antenna light harvesting.
  support: supports
- evidence_id: micro-chl-SL-0060
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0060.json
  locator: UniProt SL-0060 identity, definition, synonyms, GO mapping and chlorosome
    parthood
  accessed_at: '2026-11-03T10:11:00.710582Z'
  snapshot_sha256: 711bbfca86410598680bf45a126c4c9690dd7c71739ef68ab738259c18dff0c4
  summary: Chlorosomal envelope is an exact synonym; asymmetric glycolipid monolayer
    with pigment tails differs from a bilayer. Authority description is not proof
    of necessity for a particular lipid species.
  support: supports
- evidence_id: micro-chl-tax-2
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2
  locator: ENA taxonomy exact taxId/scientificName/rank/lineage/otherNames
  accessed_at: '2026-11-03T10:11:00.710671Z'
  snapshot_sha256: 314bd7723b8dea04f1840809fb74e06c514664fba9c6a0619e8f12e2a6dceef1
  summary: Current authority identifies 2 as Bacteria. Species and strain scope are
    retained; historical Pichia naming is not used as a current strain identity bridge.
  support: supports
- evidence_id: micro-chl-tax-1097
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1097
  locator: ENA taxonomy exact taxId/scientificName/rank/lineage/otherNames
  accessed_at: '2026-11-03T10:11:00.710731Z'
  snapshot_sha256: a8e843e290efea6a5a31d92ee3cdb32ee8bae331690d26d3c87955c375625c37
  summary: Current authority identifies 1097 as Chlorobaculum tepidum. Species and
    strain scope are retained; historical Pichia naming is not used as a current strain
    identity bridge.
  support: supports
- evidence_id: micro-chl-tax-1108
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1108
  locator: ENA taxonomy exact taxId/scientificName/rank/lineage/otherNames
  accessed_at: '2026-11-03T10:11:00.710790Z'
  snapshot_sha256: 715f90ba83134a7125e1978182c5242cf96eb6fb85f1a83cab48dc7daa063139
  summary: Current authority identifies 1108 as Chloroflexus aurantiacus. Species
    and strain scope are retained; historical Pichia naming is not used as a current
    strain identity bridge.
  support: supports
- evidence_id: micro-chl-tax-194439
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/194439
  locator: ENA taxonomy exact taxId/scientificName/rank/lineage/otherNames
  accessed_at: '2026-11-03T10:11:00.710853Z'
  snapshot_sha256: db206b8370769142a525002170c3e080b17cdb2493db598567586f1d4cae4eae
  summary: Current authority identifies 194439 as Chlorobaculum tepidum TLS. Species
    and strain scope are retained; historical Pichia naming is not used as a current
    strain identity bridge.
  support: supports
- evidence_id: micro-cis-tax-4922
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4922
  locator: ENA taxonomy exact taxId/scientificName/rank/lineage/otherNames
  accessed_at: '2026-11-03T10:11:09.052648Z'
  snapshot_sha256: 97a9231814c8f3647963f28cdbbdffca2dc1067a0136592a0f0d37babb846ee3
  summary: Current authority identifies 4922 as Komagataella pastoris. Species and
    strain scope are retained; historical Pichia naming is not used as a current strain
    identity bridge.
  support: supports
- evidence_id: micro-cis-tax-460519
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/460519
  locator: ENA taxonomy exact taxId/scientificName/rank/lineage/otherNames
  accessed_at: '2026-11-03T10:11:09.053105Z'
  snapshot_sha256: d7cb478e59011f67e93469d8e1b458585b0e2373435fdad6ffc5962069f62a31
  summary: Current authority identifies 460519 as Komagataella phaffii. Species and
    strain scope are retained; historical Pichia naming is not used as a current strain
    identity bridge.
  support: supports
- evidence_id: micro-chl-nielsen2016-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4992139.1/PMC4992139.1.xml
  locator: DOI10.1038/ncomms12454; complete Introduction, all Results, complete Discussion
    and Methods Sample preparation
  accessed_at: '2026-11-03T10:11:02.361749Z'
  snapshot_sha256: 0c5f33758e0ffea1a267cca08a1bcbb0da36023045ba7fcdc9189dfe9f6b3922
  summary: Genuine JATS. bchK-mutant carotenosomes retain an intact CsmA/BChl-a baseplate;
    wild-type/mutant comparison and NMR/cryo-EM/spectroscopy resolve organization.
    Introduction positively attributes structural integrity, attachment and energy-transfer
    roles. It does not remove the baseplate to test chlorosome formation. AFM dimensions
    are earlier-work comparisons; no raw data, figures or supplement reanalysis.
  support: supports
- evidence_id: micro-frigaard2004
  kind: primary_source
  reference: https://rcn.montana.edu/Publications/Pdf/2004/2004%20Frigaard%20et%20al.%20csm.%20J.%20Bacteriol.pdf
  locator: DOI10.1128/JB.186.3.646-653.2004; PDF pp646-652 Abstract, growth/construct
    Methods, Results Construction of csm mutants, biochemical characterizations and
    Discussion
  accessed_at: '2026-11-03T10:14:40.914564Z'
  snapshot_sha256: 61f617b1489615109b27d6b0b40167d3002831ddebca50ea0a13781dd03ef111
  summary: Fresh genuine primary PDF. csmA transformants remain merodiploid under
    tested conditions; author inference concerns essential light harvesting. Nine
    non-CsmA single mutants form functional chlorosomes with bounded morphology/pigment
    changes. This is neither a direct CsmA-loss formation assay nor universal cohort
    dispensability.
  support: supports
- evidence_id: micro-psencik2009-retained-body
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2795307/
  locator: DOI10.1128/JB.00690-09; Methods; Results Cryo-EM, Tomographic reconstruction
    and X-ray scattering; Discussion Overall shape, Parallel striation, Perpendicular
    striation and Summary
  accessed_at: '2026-11-03T04:31:37.620817Z'
  snapshot_sha256: 1a62f209794c33adbe5790b2797b9e93e8793d958f2e723bf19cf0fa556e8a80
  summary: Retained genuine PMC body fetched04:31:37Z, reread for this cohort. C.
    aurantiacus J-10-fl culture and chlorosome imaging/scattering support canonical
    occurrence, lamellar pigments and crystalline baseplate. Dimer assignment is a
    scoped inference; projection versus tomogram resolution and contaminating-bilayer
    scattering are distinguished. No fresh body-fetch success or pixel audit claimed.
  support: supports
- evidence_id: micro-chl-oostergetel2010-jats
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2882566.1/PMC2882566.1.xml
  locator: DOI10.1007/s11120-010-9533-0; secondary review abstract, Introduction Sec1,
    Chlorosomes Sec2 and Organization of the baseplate Sec5
  accessed_at: '2026-11-03T10:11:02.382507Z'
  snapshot_sha256: d555d33602f2946ad490d2d02be169d4f767093604c513edbf0d0753b347cea5
  summary: Secondary synthesis supplies limited phototroph distribution, self-assembled
    pigment and antenna/baseplate context. FMO coupling is green-sulfur-bacterial
    context, not universal acceptor identity. This is not a newly performed primary
    experiment.
  support: context_only
- evidence_id: micro-orf2013-browser
  kind: authority
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/adversary-microtubule/orf-browser-capture.json
  locator: Author-uploaded Orf2013 secondary article; Introduction and protein/baseplate
    section pp322-323, browser lines1200-1389; reference https://www.researchgate.net/publication/237199940_Chlorosome_Antenna_Complexes_from_Green_Photosynthetic_Bacteria
  accessed_at: '2026-11-03T10:12:05Z'
  snapshot_sha256: 476ad87504acd017f901e2a00a578c6cbed0a3b4345dc442abfe45971f287c1e
  summary: Actual browser-readable secondary body supports surface Csm localization,
    up-to-eleven proteins, distinct motif groups and lineage variability. Native direct
    body returned403 and publisher/PDF routes challenge HTML. The new edge is accepted
    only as surface localization, not universal protein membership, necessity or a
    complete assembly mechanism.
  support: context_only
- evidence_id: micro-chl-li2006-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1021%2Fbi060776y&format=json&resultType=core
  locator: DOI10.1021/bi060776y; exact metadata and complete abstract only
  accessed_at: '2026-11-03T10:11:01.610472Z'
  snapshot_sha256: 8073e85e672f077f1066a0641b6e01aaedde7170613240a3f52cd21de999c5d1
  summary: Complete primary abstract reports cross-linking in C. tepidum and mutant
    controls, CsmA oligomer/FMO interactions and a proposed envelope-contact model.
    It supports the named cohort/localization scope but is not a full Methods audit.
  support: partial
- evidence_id: micro-chl-frigaard2005-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1007/s11120-005-1331-8&format=json&resultType=core
  locator: DOI10.1007/s11120-005-1331-8; exact metadata and complete abstract only
  accessed_at: '2026-11-03T10:11:02.361626Z'
  snapshot_sha256: cf5293ba1393099a83929bb93937c5139e20b0f0f17ea7aa52fc213e5bd90ebd
  summary: Complete primary abstract distinguishes bchK-mutant vestigial carotenosomes
    from normal BChl-c chlorosomes; intact CsmA/BChl-a baseplate and flattened morphology
    do not establish baseplate-removal dispensability.
  support: partial
- evidence_id: micro-chl-orf2013-meta
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1007/s11120-013-9869-3
  locator: 'Exact DOI metadata and complete abstract: 10.1007/s11120-013-9869-3'
  accessed_at: '2026-11-03T10:11:01.609986Z'
  snapshot_sha256: fe8c53d3d2226385cd7e88b2bea020c3dc89afdcfb6fc8d6d5870e9090a56e42
  summary: 'Verified title/DOI/organism and abstract access: Chlorosome antenna complexes
    from green photosynthetic bacteria.. Claim-bearing primary body or secondary-context
    evidence is separately scoped above.'
  support: context_only
- evidence_id: micro-chl-oostergetel2010-meta
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1007/s11120-010-9533-0
  locator: 'Exact DOI metadata and complete abstract: 10.1007/s11120-010-9533-0'
  accessed_at: '2026-11-03T10:11:01.610154Z'
  snapshot_sha256: c4c3f4d084a63660114430edab8edd25a16b287d7de6f2b5c57a16f1452ca68b
  summary: 'Verified title/DOI/organism and abstract access: The chlorosome: a prototype
    for efficient light harvesting in photosynthesis.. Claim-bearing primary body
    or secondary-context evidence is separately scoped above.'
  support: context_only
- evidence_id: micro-chl-psencik2009-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1128/JB.00690-09
  locator: 'Exact DOI metadata and complete abstract: 10.1128/jb.00690-09'
  accessed_at: '2026-11-03T10:11:01.610302Z'
  snapshot_sha256: 202f2a3417932350d1493429648939255e642aee21d9a0d48b922102f0faa232
  summary: 'Verified title/DOI/organism and abstract access: Structure of chlorosomes
    from the green filamentous bacterium Chloroflexus aurantiacus.. Claim-bearing
    primary body or secondary-context evidence is separately scoped above.'
  support: context_only
- evidence_id: micro-chl-nielsen2016-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1038/ncomms12454
  locator: 'Exact DOI metadata and complete abstract: 10.1038/ncomms12454'
  accessed_at: '2026-11-03T10:11:01.610350Z'
  snapshot_sha256: 0040f396e49964974cf13f9586dbe914d0d51af62d0735571df420a194d9b999
  summary: 'Verified title/DOI/organism and abstract access: In situ high-resolution
    structure of the baseplate antenna complex in Chlorobaculum tepidum.. Claim-bearing
    primary body or secondary-context evidence is separately scoped above.'
  support: context_only
- evidence_id: micro-chl-frigaard2004-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128%2FJB.186.3.646-653.2004&format=json&resultType=core
  locator: 'Exact DOI metadata and complete abstract: 10.1128/jb.186.3.646-653.2004'
  accessed_at: '2026-11-03T10:11:01.610430Z'
  snapshot_sha256: 0142e808cc75ce236988195538136544013370342847498629c027f1e0dbc95a
  summary: 'Verified title/DOI/organism and abstract access: Nine mutants of Chlorobium
    tepidum each unable to synthesize a different chlorosome protein still assemble
    functional chlorosomes.. Claim-bearing primary body or secondary-context evidence
    is separately scoped above.'
  support: context_only
- evidence_id: micro-chl-P0A314
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0A314.json
  locator: UniProtKB exact accession; primaryAccession, entryType, organism, genes
    and proteinDescription
  accessed_at: '2026-11-03T10:11:02.446491Z'
  snapshot_sha256: 39dadbdc04fa6b4350a737e9894067b526bb041096c6a646b145818be2e1fdfa
  summary: P0A314 is UniProtKB reviewed (Swiss-Prot); gene csmA in taxon194439 C.
    tepidum TLS. Exact identity/status and locus support only; database names do not
    override experimental BChl-a baseplate specificity or establish universal localization/necessity.
  support: supports
- evidence_id: micro-chl-matches-P0A314
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/P0A314/
  locator: InterPro integrated/member entry matches for exact UniProt P0A314; entire
    returned page; next=None
  accessed_at: '2026-11-03T10:11:05.483186Z'
  snapshot_sha256: 54f4d65be0a9e9b2b9f0f132f009cff6bd1b7b844d423447f3e122b67fccd4e9
  summary: 'Bounded accession match inventory: G3DSA:1.20.5.950 homologous_superfamily
    bacteriochlorophyll c-binding protein; IPR001470 family Bacteriochlorophyll c-binding
    protein; IPR038387 homologous_superfamily Bacteriochlorophyll c-binding superfamily;
    PF02043 family Bacteriochlorophyll C binding protein; PIRSF002903 family Chlorosome
    protein, CsmA/CsmE types; PR00656 family BCHLROPHYLLC. Subgroup/domain matches
    do not denote the heterogeneous accessory Csm set or whole protein-pigment baseplate.
    Empty response is not proof of no family.'
  support: context_only
- evidence_id: micro-chl-Q46383
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q46383.json
  locator: UniProtKB exact accession; primaryAccession, entryType, organism, genes
    and proteinDescription
  accessed_at: '2026-11-03T10:11:02.551707Z'
  snapshot_sha256: f301bfe1e0c4af824862782ee615256c4dde780828a84695ae74d21562ef0beb
  summary: Q46383 is UniProtKB reviewed (Swiss-Prot); gene csmB in taxon194439 C.
    tepidum TLS. Exact identity/status and locus support only; database names do not
    override experimental BChl-a baseplate specificity or establish universal localization/necessity.
  support: supports
- evidence_id: micro-chl-matches-Q46383
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q46383/?page_size=200
  locator: InterPro integrated/member entry matches for exact UniProt Q46383; entire
    returned page; next=None
  accessed_at: '2026-11-03T10:11:05.485820Z'
  snapshot_sha256: 9d90c767f264a69a21098c3c83d3b39b5a1fe04146c9f05ab9d27d7a6f76b717
  summary: 'Bounded accession match inventory: IPR059980 family CsmB chlorosome envelope
    protein. Subgroup/domain matches do not denote the heterogeneous accessory Csm
    set or whole protein-pigment baseplate. Empty response is not proof of no family.'
  support: context_only
- evidence_id: micro-chl-Q46367
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q46367.json
  locator: UniProtKB exact accession; primaryAccession, entryType, organism, genes
    and proteinDescription
  accessed_at: '2026-11-03T10:11:02.650072Z'
  snapshot_sha256: 9f4fbc7b5b866d63bdd2fb45e49c2bc7890ec20343b17bb54c8e1de9cb76487b
  summary: Q46367 is UniProtKB reviewed (Swiss-Prot); gene csmC in taxon194439 C.
    tepidum TLS. Exact identity/status and locus support only; database names do not
    override experimental BChl-a baseplate specificity or establish universal localization/necessity.
  support: supports
- evidence_id: micro-chl-matches-Q46367
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q46367/?page_size=200
  locator: InterPro integrated/member entry matches for exact UniProt Q46367; entire
    returned page; next=None
  accessed_at: '2026-11-03T10:11:06.526876Z'
  snapshot_sha256: 13d35de84da180af3b491e5c7352138a475483eac3b3b83930119900eff1bb58
  summary: 'Bounded accession match inventory: IPR020995 family Chlorosome envelope
    protein C. Subgroup/domain matches do not denote the heterogeneous accessory Csm
    set or whole protein-pigment baseplate. Empty response is not proof of no family.'
  support: context_only
- evidence_id: micro-chl-Q46386
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q46386.json
  locator: UniProtKB exact accession; primaryAccession, entryType, organism, genes
    and proteinDescription
  accessed_at: '2026-11-03T10:11:02.836981Z'
  snapshot_sha256: 1bea7e1eeac590899a198949667c66f0871547966682307075b405c8affa2c98
  summary: Q46386 is UniProtKB reviewed (Swiss-Prot); gene csmE in taxon194439 C.
    tepidum TLS. Exact identity/status and locus support only; database names do not
    override experimental BChl-a baseplate specificity or establish universal localization/necessity.
  support: supports
- evidence_id: micro-chl-matches-Q46386
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q46386/?page_size=200
  locator: InterPro integrated/member entry matches for exact UniProt Q46386; entire
    returned page; next=None
  accessed_at: '2026-11-03T10:11:06.527371Z'
  snapshot_sha256: 1196fdb735bad1a728a046dac7eb015b2dcd257ee11380e2ac38aa9823f96f5b
  summary: 'Bounded accession match inventory: IPR001470 family Bacteriochlorophyll
    c-binding protein; IPR038387 homologous_superfamily Bacteriochlorophyll c-binding
    superfamily. Subgroup/domain matches do not denote the heterogeneous accessory
    Csm set or whole protein-pigment baseplate. Empty response is not proof of no
    family.'
  support: context_only
- evidence_id: micro-chl-O68986
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/O68986.json
  locator: UniProtKB exact accession; primaryAccession, entryType, organism, genes
    and proteinDescription
  accessed_at: '2026-11-03T10:11:02.923873Z'
  snapshot_sha256: 9281ae269128d5b54105a8605d129c917357da1399d7183edad995f522620a19
  summary: O68986 is UniProtKB reviewed (Swiss-Prot); gene csmF in taxon194439 C.
    tepidum TLS. Exact identity/status and locus support only; database names do not
    override experimental BChl-a baseplate specificity or establish universal localization/necessity.
  support: supports
- evidence_id: micro-chl-matches-O68986
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/O68986/?page_size=200
  locator: InterPro integrated/member entry matches for exact UniProt O68986; entire
    returned page; next=None
  accessed_at: '2026-11-03T10:11:06.805958Z'
  snapshot_sha256: f24e8d2e2362d57ce5607609a36cf37336a6b33537ee17404e33feba355fca4a
  summary: 'Bounded accession match inventory: IPR059980 family CsmB chlorosome envelope
    protein. Subgroup/domain matches do not denote the heterogeneous accessory Csm
    set or whole protein-pigment baseplate. Empty response is not proof of no family.'
  support: context_only
- evidence_id: micro-chl-O68988
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/O68988.json
  locator: UniProtKB exact accession; primaryAccession, entryType, organism, genes
    and proteinDescription
  accessed_at: '2026-11-03T10:11:03.034914Z'
  snapshot_sha256: 32f580bff31de222d3691dcbb480e4e92c4ae62a84ca939b61630f8c2bc3786c
  summary: O68988 is UniProtKB reviewed (Swiss-Prot); gene csmI in taxon194439 C.
    tepidum TLS. Exact identity/status and locus support only; database names do not
    override experimental BChl-a baseplate specificity or establish universal localization/necessity.
  support: supports
- evidence_id: micro-chl-matches-O68988
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/O68988/?page_size=200
  locator: InterPro integrated/member entry matches for exact UniProt O68988; entire
    returned page; next=None
  accessed_at: '2026-11-03T10:11:07.428620Z'
  snapshot_sha256: 4dc2781a1d1b61828609e12fdafb777740a4a7429809b0c70cd6c5da69c6f0fd
  summary: 'Bounded accession match inventory: IPR001041 domain 2Fe-2S ferredoxin-type
    iron-sulfur binding domain; IPR001055 family Adrenodoxin-like; IPR012675 homologous_superfamily
    Beta-grasp domain superfamily; IPR036010 homologous_superfamily 2Fe-2S ferredoxin-like
    superfamily. Subgroup/domain matches do not denote the heterogeneous accessory
    Csm set or whole protein-pigment baseplate. Empty response is not proof of no
    family.'
  support: context_only
- evidence_id: micro-chl-O68983
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/O68983.json
  locator: UniProtKB exact accession; primaryAccession, entryType, organism, genes
    and proteinDescription
  accessed_at: '2026-11-03T10:11:03.097580Z'
  snapshot_sha256: f5fd85c67d811dba67f0cb2ff35680d9098f8b9fe0739f5723b646ed0f62c854
  summary: O68983 is UniProtKB reviewed (Swiss-Prot); gene csmJ in taxon194439 C.
    tepidum TLS. Exact identity/status and locus support only; database names do not
    override experimental BChl-a baseplate specificity or establish universal localization/necessity.
  support: supports
- evidence_id: micro-chl-matches-O68983
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/O68983/?page_size=200
  locator: InterPro integrated/member entry matches for exact UniProt O68983; entire
    returned page; next=None
  accessed_at: '2026-11-03T10:11:07.653957Z'
  snapshot_sha256: c4e6d56c3e1f6740223bcf6d8703d55bfbb4ca56b9f26a162f89adce3ff257b9
  summary: 'Bounded accession match inventory: IPR001041 domain 2Fe-2S ferredoxin-type
    iron-sulfur binding domain; IPR001055 family Adrenodoxin-like; IPR012675 homologous_superfamily
    Beta-grasp domain superfamily; IPR036010 homologous_superfamily 2Fe-2S ferredoxin-like
    superfamily. Subgroup/domain matches do not denote the heterogeneous accessory
    Csm set or whole protein-pigment baseplate. Empty response is not proof of no
    family.'
  support: context_only
- evidence_id: micro-chl-H2VFJ4
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/H2VFJ4.json
  locator: UniProtKB exact accession; primaryAccession, entryType, organism, genes
    and proteinDescription
  accessed_at: '2026-11-03T10:11:03.236891Z'
  snapshot_sha256: 5c8e2854660c20e5a67f71093f44c2360ff76f83284f409937c1bfd8fa563e40
  summary: H2VFJ4 is UniProtKB unreviewed (TrEMBL); gene csmD in taxon194439 C. tepidum
    TLS. Exact identity/status and locus support only; database names do not override
    experimental BChl-a baseplate specificity or establish universal localization/necessity.
  support: supports
- evidence_id: micro-chl-matches-H2VFJ4
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/H2VFJ4/?page_size=200
  locator: InterPro integrated/member entry matches for exact UniProt H2VFJ4; entire
    returned page; next=None
  accessed_at: '2026-11-03T10:11:07.858448Z'
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
  summary: 'Bounded accession match inventory: HTTP204 empty response. Subgroup/domain
    matches do not denote the heterogeneous accessory Csm set or whole protein-pigment
    baseplate. Empty response is not proof of no family.'
  support: context_only
- evidence_id: micro-chl-H2VFJ1
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/H2VFJ1.json
  locator: UniProtKB exact accession; primaryAccession, entryType, organism, genes
    and proteinDescription
  accessed_at: '2026-11-03T10:11:03.425357Z'
  snapshot_sha256: f46eb2eea722743b474a6c6bb403702119f888e7a7081f82f49c3bc2d68271bc
  summary: H2VFJ1 is UniProtKB unreviewed (TrEMBL); gene csmH in taxon194439 C. tepidum
    TLS. Exact identity/status and locus support only; database names do not override
    experimental BChl-a baseplate specificity or establish universal localization/necessity.
  support: supports
- evidence_id: micro-chl-matches-H2VFJ1
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/H2VFJ1/?page_size=200
  locator: InterPro integrated/member entry matches for exact UniProt H2VFJ1; entire
    returned page; next=None
  accessed_at: '2026-11-03T10:11:07.932661Z'
  snapshot_sha256: a6962831d38490b34c5d8bbb2a94f8e6c982c06b32c42a32a8e5858c45a6490d
  summary: 'Bounded accession match inventory: IPR017845 repeat Chlorosome envelope
    protein H, CsmH; IPR040561 domain Large polyvalent protein associated domain 38.
    Subgroup/domain matches do not denote the heterogeneous accessory Csm set or whole
    protein-pigment baseplate. Empty response is not proof of no family.'
  support: context_only
- evidence_id: micro-chl-Q8KEN5
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q8KEN5.json
  locator: UniProtKB exact accession; primaryAccession, entryType, organism, genes
    and proteinDescription
  accessed_at: '2026-11-03T10:11:03.657820Z'
  snapshot_sha256: 3312354f0f178ad589517039088723dc7aae08f91af1ebdac65fa552cb5188ee
  summary: Q8KEN5 is UniProtKB unreviewed (TrEMBL); gene csmX in taxon194439 C. tepidum
    TLS. Exact identity/status and locus support only; database names do not override
    experimental BChl-a baseplate specificity or establish universal localization/necessity.
  support: supports
- evidence_id: micro-chl-matches-Q8KEN5
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q8KEN5/?page_size=200
  locator: InterPro integrated/member entry matches for exact UniProt Q8KEN5; entire
    returned page; next=None
  accessed_at: '2026-11-03T10:11:07.933119Z'
  snapshot_sha256: 903f92ae5457178d5dfb5387f4ff43b43dad57039a21b3b3f533cc4b0322333f
  summary: 'Bounded accession match inventory: IPR001041 domain 2Fe-2S ferredoxin-type
    iron-sulfur binding domain; IPR001055 family Adrenodoxin-like; IPR012675 homologous_superfamily
    Beta-grasp domain superfamily; IPR036010 homologous_superfamily 2Fe-2S ferredoxin-like
    superfamily. Subgroup/domain matches do not denote the heterogeneous accessory
    Csm set or whole protein-pigment baseplate. Empty response is not proof of no
    family.'
  support: context_only
- evidence_id: micro-chl-reviewed-csm-query
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A194439+AND+%28gene_exact%3AcsmA+OR+gene_exact%3AcsmB+OR+gene_exact%3AcsmC+OR+gene_exact%3AcsmD+OR+gene_exact%3AcsmE+OR+gene_exact%3AcsmF+OR+gene_exact%3AcsmH+OR+gene_exact%3AcsmI+OR+gene_exact%3AcsmJ+OR+gene_exact%3AcsmK+OR+gene_exact%3AcsmX%29&format=json&size=500
  locator: Exact UniProt search response and pagination headers
  accessed_at: '2026-11-03T10:11:04.408131Z'
  snapshot_sha256: 904b7429522795458886148bf17eed86c2b57d128f86e58f8286f778627757f8
  summary: Seven reviewed entries match the queried eleven symbols in TLS. Three declared
    unreviewed examples are separately verified; reviewed status is not invented for
    them.
  support: supports
  search_scope: Database UniProtKB; literal URL https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A194439+AND+%28gene_exact%3AcsmA+OR+gene_exact%3AcsmB+OR+gene_exact%3AcsmC+OR+gene_exact%3AcsmD+OR+gene_exact%3AcsmE+OR+gene_exact%3AcsmF+OR+gene_exact%3AcsmH+OR+gene_exact%3AcsmI+OR+gene_exact%3AcsmJ+OR+gene_exact%3AcsmK+OR+gene_exact%3AcsmX%29&format=json&size=500;
    accessed 2026-11-03T10:11:04.408131+00:00; requested size500; complete returned
    response, total_results=7; Link header=None. No alternate spelling, homology search
    or universal absence inference.
- evidence_id: micro-chl-csmK-query
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AcsmK&format=json&size=500
  locator: Exact UniProt search response and pagination headers
  accessed_at: '2026-11-03T10:11:04.439162Z'
  snapshot_sha256: a0273f3ee015db2d93e8b7003c9e14e76d24ea7b4fc43150f7816cd47fe11e4a
  summary: No entry returned for the literal csmK gene query. This is a bounded naming-query
    result, not evidence that CsmK or its family does not exist.
  support: supports
  search_scope: Database UniProtKB; literal URL https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AcsmK&format=json&size=500;
    accessed 2026-11-03T10:11:04.439162+00:00; requested size500; complete returned
    response, total_results=0; Link header=None. No alternate spelling, homology search
    or universal absence inference.
- evidence_id: micro-cis-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005783,GO:0005794,GO:0005801,GO:0033106,GO:0098791
  locator: QuickGO exact GO:0005801/0033106/0005794/0098791/0005783 active terms,
    definitions, synonyms, comments and children
  accessed_at: '2026-11-03T10:11:08.059163Z'
  snapshot_sha256: 1f64f46ea3228d75112cc4a7cd62683682181d7f56a4b695efb1f8f03db842e8
  summary: CGN is an ER-abutting network distinct from its membrane and whole Golgi;
    current GO explicitly says CGN is not part of the Golgi stack. Broader cis-face
    synonyms are not exact identities.
  support: supports
- evidence_id: micro-cis-jats-PMC2148216
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2148216.1/PMC2148216.1.xml
  locator: DOI10.1083/jcb.145.1.69; Methods Strains and Plasmids, complete Results
    and complete Discussion; text only
  accessed_at: '2026-11-03T10:11:09.799368Z'
  snapshot_sha256: e9eb8235003747a36696a90d27a3fd45f601b1e46dfb3bba5419d779b5fe9590
  summary: PPY1/PPY12 experiments establish coherent Golgi stacks adjacent to transitional
    ER. Sec13-positive tubulovesicular interface is interpreted as tER; Och1/late-marker
    apposition does not independently identify a distinct CGN. Whole primary narrative
    does not establish absence of CGN. No raw micrograph/pixel audit or full supplementary
    analysis.
  support: supports
- evidence_id: micro-cis-atcc-204163
  kind: authority
  reference: https://www.atcc.org/products/204163
  locator: ATCC204163 product identity, Strain designation PPY12, Genotype his4 arg4,
    Characteristics Comments
  accessed_at: '2026-11-03T10:11:09.799560Z'
  snapshot_sha256: 871a39203ad01dd26935f6aedb49c60d70abce7f7ac74977069748beb44e2ba6
  summary: PPY12 is K. phaffii; ATCC explicitly describes the change from K. pastoris
    based on in-house sequence analysis. This is a strain identity bridge, not evidence
    of organelle occurrence.
  support: supports
- evidence_id: micro-cis-ena-LC815816
  kind: authority
  reference: https://www.ebi.ac.uk/ena/browser/api/embl/LC815816.1?download=false
  locator: ENA LC815816.1 EMBL FT source qualifiers organism/strain/db_xref
  accessed_at: '2026-11-03T10:11:09.967152Z'
  snapshot_sha256: f02d748dce33d5c56b830ab9e96ccb14facd65a8a7621bdaa10c7711eb8d63b4
  summary: Source qualifiers identify Komagataella phaffii PPY12, taxon460519. Corroborates
    the strain bridge independently of historical name; ATG14 sequence is not evidence
    of CGN membership/function.
  support: supports
- evidence_id: micro-cis-cho2000-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1016/S0014-5793%2800%2901268-0%22
  locator: DOI10.1016/S0014-5793(00)01268-0; exact metadata and complete primary abstract
    only
  accessed_at: '2026-11-03T10:11:10.006407Z'
  snapshot_sha256: b0960521e38911bcc0523d02dcbc5d953440044fcace3d795af4bf575d3fd67f
  summary: S. cerevisiae Sed5 membrane immunoisolation enriches early-Golgi mannosyltransferases
    and excludes late-Golgi/ER markers. This limited abstract does not establish K.
    pastoris/phaffii CGN occurrence or universally essential resident proteins; both
    publisher body/PDF attempts403.
  support: partial
- evidence_id: micro-adapter-catalogue
  kind: search
  reference: https://imodulondb.org/api/datasets
  locator: Full iModulonDB API organism/dataset catalogue; all returned rows
  accessed_at: '2026-11-03T10:11:10.205824Z'
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  summary: No Chlorobaculum/Chlorobium, Chloroflexus, Komagataella/Pichia or Saccharomyces
    covered dataset was returned. Thus no matched target gene/module summary is justified;
    catalogue absence is not negative biological evidence.
  support: supports
  search_scope: iModulonDB GET https://imodulondb.org/api/datasets at 2026-11-03T10:11:10.205824+00:00;
    entire returned catalogue (20 organism rows,28 organism-dataset pairs), no pagination
    advertised. Compared organism names/keys for Chlorobaculum, Chlorobium, Chloroflexus,
    Komagataella, Pichia, Saccharomyces and their target species. No downstream query
    was run for an uncovered organism; no global database/biological absence inference.
- evidence_id: micro-historical-adapter-runner
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Retained earlier kg-microbe-sources imodulondb datasets invocation; actual
    stdout/stderr hashes and PermissionError
  accessed_at: '2026-11-03T00:49:00.863225Z'
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  summary: Historical00:49Z runner failed with PermissionError opening pyvenv.cfg;
    actual exit1 retained as historical unavailable evidence. It is not a new invocation
    or success. Current catalogue fallback was inspected separately.
  support: context_only
- evidence_id: septin-review-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Structured Source Cross-Checks and immutable review workflow
  summary: Actual named molecular or pathway assertions trigger applicability; absence
    of expression claims does not exempt them. Truly sparse topology scope need not
    invent a molecular query. Unmatched organisms permit bounded downstream non-applicability.
  accessed_at: '2026-11-03T10:15:35.444371Z'
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
  support: supports
- evidence_id: septin-curation-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Identity, components, source scope and necessity
  summary: Structure identity, material composition, proteins and empirical formation
    dependency are distinct; a spatial region need not assert a complete invariant
    molecular inventory.
  accessed_at: '2026-11-03T10:15:35.444371Z'
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
  support: supports
- evidence_id: septin-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: NONMECHANISTIC graph scope
  summary: Descriptive constitution, identity and spatial relations may be explicitly
    nonmechanistic; biological process endpoints are distinct from the containing
    compartment.
  accessed_at: '2026-11-03T10:15:35.444371Z'
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
  support: supports
- evidence_id: septin-record-chloroplast_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/chloroplast_membrane.yaml
  locator: Entire current maintained record at fa6c7f0034c57fac03d026ce0ddb8aaa4bd4b2e3
  summary: Full record identity, synonyms, history, boundaries, components where present,
    taxonomic examples, functions, evidence, graph and discussions read. No attached
    image or verbatim snippet is declared.
  accessed_at: '2026-11-03T10:15:35.444371Z'
  snapshot_sha256: 115d9369e1b84a54e66028f079a8d140e72d40ec2fb5877e64fb592b6a085905
  support: supports
- evidence_id: septin-original-chloroplast_membrane
  kind: prior_review
  reference: reviews/structured/20261021T110921Z-chloroplast-membrane-audit/review.yaml
  locator: Entire original YAML/Markdown pair; claims, checks, evidence tiers and
    verdict
  summary: Original pass_with_limitations has no findings or curation actions. Historical
    source access and checks remain historical, not newly executed.
  accessed_at: '2026-11-03T10:15:35.444371Z'
  snapshot_sha256: a76189a76a9dd5f2f9121ea2d9931a1eaa30242657b30eebd265187fbdeac676
  support: supports
- evidence_id: septin-original-validation-chloroplast_membrane
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/adversary-septin/original-checks.json
  locator: 20261021T110921Z-chloroplast-membrane-audit native validate/render and
    source/current hash comparison
  summary: Validation and render exit0; deterministic Markdown is byte-identical.
    Original source revision, original frozen target hash and current target bytes
    match.
  accessed_at: '2026-11-03T10:12:52.430674Z'
  snapshot_sha256: df3dafc20cd7efbac9a8dae8ca4555756c45b498f800201d420db51981eddaaf
  support: supports
- evidence_id: septin-native-chloroplast_membrane-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/chloroplast_membrane-uniprot-verify-receipt.json
  locator: Actual root-run receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/chloroplast_membrane-uniprot-verify.log
  summary: Exit0 at 2026-11-03T10:11:19.993371+00:00. No protein_examples, UniProtKB
    protein xrefs or GENE_OR_PROTEIN graph nodes are declared. The causal inventory
    has zero typed protein nodes; success does not validate molecules mentioned in
    prose, localization, mechanism or formation necessity.
  accessed_at: '2026-11-03T10:11:19.993371Z'
  snapshot_sha256: ff741861e52528673c2b3b442e263220a1cfa01eec6878ae9977f0c5f681d860
  support: supports
- evidence_id: septin-native-chloroplast_membrane-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/chloroplast_membrane-uniprot-causal-receipt.json
  locator: Actual root-run receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/chloroplast_membrane-uniprot-causal.log
  summary: Exit0 at 2026-11-03T10:11:20.413148+00:00. No protein_examples, UniProtKB
    protein xrefs or GENE_OR_PROTEIN graph nodes are declared. The causal inventory
    has zero typed protein nodes; success does not validate molecules mentioned in
    prose, localization, mechanism or formation necessity.
  accessed_at: '2026-11-03T10:11:20.413148Z'
  snapshot_sha256: 26658f08cf700c612339a7a4367eca404b93d3144d369109ae51ae288bdce791
  support: supports
- evidence_id: septin-record-chloroplast_outer_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/chloroplast_outer_membrane.yaml
  locator: Entire current maintained record at fa6c7f0034c57fac03d026ce0ddb8aaa4bd4b2e3
  summary: Full record identity, synonyms, history, boundaries, components where present,
    taxonomic examples, functions, evidence, graph and discussions read. No attached
    image or verbatim snippet is declared.
  accessed_at: '2026-11-03T10:15:35.444371Z'
  snapshot_sha256: f499d6317b1546cf0d578f54d04df76a8af3c54746f29db6b2d7af0244b0075d
  support: supports
- evidence_id: septin-original-chloroplast_outer_membrane
  kind: prior_review
  reference: reviews/structured/20261021T110923Z-chloroplast-outer-membrane-audit/review.yaml
  locator: Entire original YAML/Markdown pair; claims, checks, evidence tiers and
    verdict
  summary: Original pass_with_limitations has no findings or curation actions. Historical
    source access and checks remain historical, not newly executed.
  accessed_at: '2026-11-03T10:15:35.444371Z'
  snapshot_sha256: c8f22919f640db5735a0a8768eb75f73ab841bcc9dfc028c98d29c9bbfdd0b1d
  support: supports
- evidence_id: septin-original-validation-chloroplast_outer_membrane
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/adversary-septin/original-checks.json
  locator: 20261021T110923Z-chloroplast-outer-membrane-audit native validate/render
    and source/current hash comparison
  summary: Validation and render exit0; deterministic Markdown is byte-identical.
    Original source revision, original frozen target hash and current target bytes
    match.
  accessed_at: '2026-11-03T10:12:53.742010Z'
  snapshot_sha256: df3dafc20cd7efbac9a8dae8ca4555756c45b498f800201d420db51981eddaaf
  support: supports
- evidence_id: septin-native-chloroplast_outer_membrane-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/chloroplast_outer_membrane-uniprot-verify-receipt.json
  locator: Actual root-run receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/chloroplast_outer_membrane-uniprot-verify.log
  summary: Exit0 at 2026-11-03T10:11:20.823917+00:00. No protein_examples, UniProtKB
    protein xrefs or GENE_OR_PROTEIN graph nodes are declared. The causal inventory
    has zero typed protein nodes; success does not validate molecules mentioned in
    prose, localization, mechanism or formation necessity.
  accessed_at: '2026-11-03T10:11:20.823917Z'
  snapshot_sha256: acb911744c7005667ab1897e683794f99aa4aa572842d92ffda7501c9de4e52d
  support: supports
- evidence_id: septin-native-chloroplast_outer_membrane-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/chloroplast_outer_membrane-uniprot-causal-receipt.json
  locator: Actual root-run receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/chloroplast_outer_membrane-uniprot-causal.log
  summary: Exit0 at 2026-11-03T10:11:21.234089+00:00. No protein_examples, UniProtKB
    protein xrefs or GENE_OR_PROTEIN graph nodes are declared. The causal inventory
    has zero typed protein nodes; success does not validate molecules mentioned in
    prose, localization, mechanism or formation necessity.
  accessed_at: '2026-11-03T10:11:21.234089Z'
  snapshot_sha256: bff3abba48f82503ec4bb261334ff2478aa518ceefeb5103b0914249a75dd167
  support: supports
- evidence_id: septin-record-chloroplast_stroma
  kind: record_content
  reference: data/structures/membrane_organelle/chloroplast_stroma.yaml
  locator: Entire current maintained record at fa6c7f0034c57fac03d026ce0ddb8aaa4bd4b2e3
  summary: Full record identity, synonyms, history, boundaries, components where present,
    taxonomic examples, functions, evidence, graph and discussions read. No attached
    image or verbatim snippet is declared.
  accessed_at: '2026-11-03T10:15:35.444371Z'
  snapshot_sha256: cfdb0d3be9fba838d5288e478b39f922a4e11cbd240b689a2cbca7690c262b6a
  support: supports
- evidence_id: septin-original-chloroplast_stroma
  kind: prior_review
  reference: reviews/structured/20261021T110927Z-chloroplast-stroma-audit/review.yaml
  locator: Entire original YAML/Markdown pair; claims, checks, evidence tiers and
    verdict
  summary: Original pass_with_limitations has no findings or curation actions. Historical
    source access and checks remain historical, not newly executed.
  accessed_at: '2026-11-03T10:15:35.444371Z'
  snapshot_sha256: fad2c9ed334d31f3d23e9c207f85f54c2231b0f7167287251ce10ae9dfb80867
  support: supports
- evidence_id: septin-original-validation-chloroplast_stroma
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/adversary-septin/original-checks.json
  locator: 20261021T110927Z-chloroplast-stroma-audit native validate/render and source/current
    hash comparison
  summary: Validation and render exit0; deterministic Markdown is byte-identical.
    Original source revision, original frozen target hash and current target bytes
    match.
  accessed_at: '2026-11-03T10:12:54.920222Z'
  snapshot_sha256: df3dafc20cd7efbac9a8dae8ca4555756c45b498f800201d420db51981eddaaf
  support: supports
- evidence_id: septin-native-chloroplast_stroma-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/chloroplast_stroma-uniprot-verify-receipt.json
  locator: Actual root-run receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/chloroplast_stroma-uniprot-verify.log
  summary: Exit0 at 2026-11-03T10:11:21.659574+00:00. No protein_examples, UniProtKB
    protein xrefs or GENE_OR_PROTEIN graph nodes are declared. The causal inventory
    has zero typed protein nodes; success does not validate molecules mentioned in
    prose, localization, mechanism or formation necessity.
  accessed_at: '2026-11-03T10:11:21.659574Z'
  snapshot_sha256: d9e9a58322421a385514b8d49c9762ec0b5e9f61926eda6a45b75bce0e2831e9
  support: supports
- evidence_id: septin-native-chloroplast_stroma-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/chloroplast_stroma-uniprot-causal-receipt.json
  locator: Actual root-run receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/chloroplast_stroma-uniprot-causal.log
  summary: Exit0 at 2026-11-03T10:11:22.099143+00:00. No protein_examples, UniProtKB
    protein xrefs or GENE_OR_PROTEIN graph nodes are declared. The causal inventory
    has zero typed protein nodes; success does not validate molecules mentioned in
    prose, localization, mechanism or formation necessity.
  accessed_at: '2026-11-03T10:11:22.099143Z'
  snapshot_sha256: 62381f10f9088564b68e413a4e99d6fc3f4cf1d529d33069b3037eb980447d43
  support: supports
- evidence_id: septin-record-ciliary_pocket_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/ciliary_pocket_membrane.yaml
  locator: Entire current maintained record at fa6c7f0034c57fac03d026ce0ddb8aaa4bd4b2e3
  summary: Full record identity, synonyms, history, boundaries, components where present,
    taxonomic examples, functions, evidence, graph and discussions read. No attached
    image or verbatim snippet is declared.
  accessed_at: '2026-11-03T10:15:35.444371Z'
  snapshot_sha256: acdf228c05817a740e627e5885200d543b8cb91f6ac94aefa4f5bf954255b3e0
  support: supports
- evidence_id: septin-original-ciliary_pocket_membrane
  kind: prior_review
  reference: reviews/structured/20261021T110936Z-ciliary-pocket-membrane-audit/review.yaml
  locator: Entire original YAML/Markdown pair; claims, checks, evidence tiers and
    verdict
  summary: Original pass_with_limitations has no findings or curation actions. Historical
    source access and checks remain historical, not newly executed.
  accessed_at: '2026-11-03T10:15:35.444371Z'
  snapshot_sha256: 32694ec8da0b5a28df1fc31d0e85d4ec569f290f30ee42788653100d89bac2be
  support: supports
- evidence_id: septin-original-validation-ciliary_pocket_membrane
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/adversary-septin/original-checks.json
  locator: 20261021T110936Z-ciliary-pocket-membrane-audit native validate/render and
    source/current hash comparison
  summary: Validation and render exit0; deterministic Markdown is byte-identical.
    Original source revision, original frozen target hash and current target bytes
    match.
  accessed_at: '2026-11-03T10:12:56.102263Z'
  snapshot_sha256: df3dafc20cd7efbac9a8dae8ca4555756c45b498f800201d420db51981eddaaf
  support: supports
- evidence_id: septin-native-ciliary_pocket_membrane-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/ciliary_pocket_membrane-uniprot-verify-receipt.json
  locator: Actual root-run receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/ciliary_pocket_membrane-uniprot-verify.log
  summary: Exit0 at 2026-11-03T10:11:28.198402+00:00. No protein_examples, UniProtKB
    protein xrefs or GENE_OR_PROTEIN graph nodes are declared. The causal inventory
    has zero typed protein nodes; success does not validate molecules mentioned in
    prose, localization, mechanism or formation necessity.
  accessed_at: '2026-11-03T10:11:28.198402Z'
  snapshot_sha256: 6c7cb3e3f753370a39379307dc0a447596fbb0e6f6cba94cb7038910b0e4d9c9
  support: supports
- evidence_id: septin-native-ciliary_pocket_membrane-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/ciliary_pocket_membrane-uniprot-causal-receipt.json
  locator: Actual root-run receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/ciliary_pocket_membrane-uniprot-causal.log
  summary: Exit0 at 2026-11-03T10:11:28.589211+00:00. No protein_examples, UniProtKB
    protein xrefs or GENE_OR_PROTEIN graph nodes are declared. The causal inventory
    has zero typed protein nodes; success does not validate molecules mentioned in
    prose, localization, mechanism or formation necessity.
  accessed_at: '2026-11-03T10:11:28.589211Z'
  snapshot_sha256: 473a2f0ba8b1b644e5a4920546c9b88118f41aa6fcebe09f0c24d9fbeafae640
  support: supports
- evidence_id: septin-context-chloroplast
  kind: record_content
  reference: data/structures/membrane_organelle/chloroplast.yaml
  locator: Only identity, label, definition, parent_structures, part_of and has_part
  summary: Frozen before reading; used solely for membrane/space/whole-organelle or
    pocket/collar boundary consistency, not independent review of other claims or
    resolution of any historical finding.
  accessed_at: '2026-11-03T10:15:35.444371Z'
  snapshot_sha256: 4c13f5dadaeb23a88fabfc2b5ec65034ed0ac83cbca9d45143793618acf2e727
  support: supports
- evidence_id: septin-context-chloroplast_envelope
  kind: record_content
  reference: data/structures/membrane_organelle/chloroplast_envelope.yaml
  locator: Only identity, label, definition, parent_structures, part_of and has_part
  summary: Frozen before reading; used solely for membrane/space/whole-organelle or
    pocket/collar boundary consistency, not independent review of other claims or
    resolution of any historical finding.
  accessed_at: '2026-11-03T10:15:35.444371Z'
  snapshot_sha256: 29da363489107536342db1782001be534ea54605039b80c201cba0a46de9468e
  support: supports
- evidence_id: septin-context-chloroplast_inner_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/chloroplast_inner_membrane.yaml
  locator: Only identity, label, definition, parent_structures, part_of and has_part
  summary: Frozen before reading; used solely for membrane/space/whole-organelle or
    pocket/collar boundary consistency, not independent review of other claims or
    resolution of any historical finding.
  accessed_at: '2026-11-03T10:15:35.444371Z'
  snapshot_sha256: 05283f5252a6354d26bef1ff196b3a9e10fbd6e72e9a6ec17014330f7a28dbb3
  support: supports
- evidence_id: septin-context-chloroplast_intermembrane_space
  kind: record_content
  reference: data/structures/membrane_organelle/chloroplast_intermembrane_space.yaml
  locator: Only identity, label, definition, parent_structures, part_of and has_part
  summary: Frozen before reading; used solely for membrane/space/whole-organelle or
    pocket/collar boundary consistency, not independent review of other claims or
    resolution of any historical finding.
  accessed_at: '2026-11-03T10:15:35.444371Z'
  snapshot_sha256: 7ab90f4d2f4c41c466e100d589fb1f1d42bf90ded515dea6db5575d54119d43a
  support: supports
- evidence_id: septin-context-flagellar_pocket
  kind: record_content
  reference: data/structures/membrane_organelle/flagellar_pocket.yaml
  locator: Only identity, label, definition, parent_structures, part_of and has_part
  summary: Frozen before reading; used solely for membrane/space/whole-organelle or
    pocket/collar boundary consistency, not independent review of other claims or
    resolution of any historical finding.
  accessed_at: '2026-11-03T10:15:35.444371Z'
  snapshot_sha256: d67c465d104f21905f63ea994b6f4f526a51502cefccf79e9e732698f4971fa8
  support: supports
- evidence_id: septin-context-ciliary_pocket_collar
  kind: record_content
  reference: data/structures/cytoskeleton/ciliary_pocket_collar.yaml
  locator: Only identity, label, definition, parent_structures, part_of and has_part
  summary: Frozen before reading; used solely for membrane/space/whole-organelle or
    pocket/collar boundary consistency, not independent review of other claims or
    resolution of any historical finding.
  accessed_at: '2026-11-03T10:15:35.444371Z'
  snapshot_sha256: df0530c9582d0a40d8e0c646cdaa88cc0872d1e6e034cbdcd068b2a3f426ec3a
  support: supports
- evidence_id: septin-root22-sources-membrane-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009535,GO:0009706,GO:0009707,GO:0009941,GO:0031969,GO:0042170
  locator: 'Requested exact GO term records: identities, definitions, obsolete flags,
    synonyms and relevant typed child relations'
  summary: Exact envelope-bilayer definition, plastid-membrane is-a parent, envelope
    parthood and inner/outer is-a children. Internal thylakoid membrane has a distinct
    definition.
  accessed_at: '2026-11-03T10:10:42.906673Z'
  snapshot_sha256: e90cb719ebf63e14c398cecedb17dd8549200ed6147b4ddbe87ede063c2d0fca
  support: supports
- evidence_id: septin-root22-sources-outer-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005737,GO:0009527,GO:0009707,GO:0009941,GO:0031969,GO:0031972
  locator: 'Requested exact GO term records: identities, definitions, obsolete flags,
    synonyms and relevant typed child relations'
  summary: Exact cytoplasm-facing outer bilayer with both maintained is-a parents;
    intermembrane-space and envelope definitions support its topology.
  accessed_at: '2026-11-03T10:10:42.906957Z'
  snapshot_sha256: 35b70e77e3049a9f0a241d3c2f5a20cd21d865b1b34f81357ebe80cfd9824f02
  support: supports
- evidence_id: septin-root22-sources-stroma-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009507,GO:0009532,GO:0009543,GO:0009570,GO:0009941,GO:0010287,GO:0042644,GO:0045037
  locator: 'Requested exact GO term records: identities, definitions, obsolete flags,
    synonyms and relevant typed child relations'
  summary: Exact stroma region excludes thylakoid lumen; plastid-stroma parent and
    chloroplast whole are supported. Nucleoid and plastoglobule are explicit part_of
    children; protein-import process is distinct from its destination.
  accessed_at: '2026-11-03T10:10:42.907071Z'
  snapshot_sha256: 9c50463dde832ac17e3cc223fc764ffafb474ce21e31f3f00dabde8be8bc8f13
  support: supports
- evidence_id: septin-pocket-membrane-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0020016,GO:0020018,GO:0060170,GO:1990900
  locator: 'Requested exact GO term records: identities, definitions, obsolete flags,
    synonyms and relevant typed child relations'
  summary: Exact pocket-membrane identity and all three exact synonyms; ciliary-membrane
    is-a parent and pocket parthood. The collar is a separate structural identity.
  accessed_at: '2026-11-03T10:10:43.665593Z'
  snapshot_sha256: d86d3d966784eb15a91838b089711e2c7dce354317aa7a9d036376fb18b114d5
  support: supports
- evidence_id: septin-root22-sources-SL-0054-json
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0054.json
  locator: Exact native location id/name/definition/synonyms/GO mappings and relevant
    isA/partOf objects; no protein-list inference
  summary: SL-0054 maps to GO:0009707 with Chloroplastic outer membrane synonym and
    cytoplasm-facing definition. Immediate isA parents are SL-0053 and SL-0214. Envelope
    parthood occurs through hierarchy, not a direct top-level partOf field. The broader
    SL-0053 text also mentions thylakoids; it is not substituted for the more precise
    maintained GO:0031969 envelope-bilayer scope.
  accessed_at: '2026-11-03T10:10:42.907028Z'
  snapshot_sha256: e861edd355d24e6bdce007cce247ebd2830c8caf5a53e489525d8205d1c94aa9
  support: supports
- evidence_id: septin-root22-sources-SL-0055-json
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0055.json
  locator: Exact native location id/name/definition/synonyms/GO mappings and relevant
    isA/partOf objects; no protein-list inference
  summary: SL-0055 maps exactly to GO:0009570 with the chloroplastic stroma synonym;
    its definition excludes thylakoid space. Direct isA is plastid stroma and direct
    partOf is chloroplast.
  accessed_at: '2026-11-03T10:10:42.907110Z'
  snapshot_sha256: be546783dc42394dcb748cf88564ed2ed64faad14a4453c870f73df0949f93cf
  support: supports
- evidence_id: septin-root22-sources-SL-0217-json
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0217.json
  locator: Exact native location id/name/definition/synonyms/GO mappings and relevant
    isA/partOf objects; no protein-list inference
  summary: SL-0217 maps to plastoglobule GO:0010287. Its definition places lipid-containing
    plastoglobules in stroma; direct partOf is chloroplast, not a top-level stroma
    relation. Lipid-reservoir wording is explicitly qualified in the source.
  accessed_at: '2026-11-03T10:10:43.625075Z'
  snapshot_sha256: 48d64d27028d7a69b946a2f222adb8295a985b5b36233c6cd98732f615414b47
  support: supports
- evidence_id: septin-pocket-membrane-agent-tax-5691
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5691
  locator: Complete ENA taxonomy name, taxId, rank, lineage and aliases
  summary: Native taxon5691 is species Trypanosoma brucei. Taxonomy identity does
    not establish an experimental strain or quantitative occurrence.
  accessed_at: '2026-11-03T10:10:43.674306Z'
  snapshot_sha256: ba78ff6fe5de62b2654b61e249c2c87b239dca0208950b0e4ecf3ef2d81c99be
  support: supports
- evidence_id: septin-root22-sources-doi-10.1093_mp_ssp083
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1093%2Fmp%2Fssp083
  locator: 'Europe PMC exact DOI result: complete abstract, title, author list, identifiers,
    journal and date'
  summary: Karcher et al.2009 complete primary abstract identifies Chlamydomonas HLP
    chloroplast targeting/nucleoid association and RNAi effects on nucleoid organization/genome
    copy number. Current access is abstract-level; it does not establish that every
    stromal protein or constituent is necessary.
  accessed_at: '2026-11-03T10:10:43.627772Z'
  snapshot_sha256: 6aac755a607ed15ef4af27f54b3e8fd410f7301e9498d66fc356ad6f079019a3
  search_scope: Europe PMC search API exact DOI query encoded in reference; resultType=core
    and format=json, one returned response page, no date filter. Inspected exact matched
    record at 2026-11-03T10:10:43.627772Z; no broader literature-absence claim.
  support: supports
- evidence_id: septin-pocket-membrane-agent-doi-10.1073_pnas.0909289106
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1073/pnas.0909289106
  locator: 'Europe PMC exact DOI result: complete abstract, title, author list, identifiers,
    journal and date'
  summary: Gadelha et al.2009 primary abstract supports a distinct yet continuous
    T. brucei pocket membrane domain and associated cytoskeletal boundaries. Suggested
    channel functions remain hypotheses, not universal demonstrated mechanisms.
  accessed_at: '2026-11-03T10:10:43.686413Z'
  snapshot_sha256: 1e0d2e19103f1a6f98801b00012315427a396610d687351c10fecc37037093bb
  search_scope: Europe PMC search API exact DOI query encoded in reference; resultType=core
    and format=json, one returned response page, no date filter. Inspected exact matched
    record at 2026-11-03T10:10:43.686413Z; no broader literature-absence claim.
  support: supports
- evidence_id: septin-pocket-membrane-agent-doi-10.1242_jcs.045740
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1242/jcs.045740
  locator: 'Europe PMC exact DOI result: complete abstract, title, author list, identifiers,
    journal and date'
  summary: Lacomble et al.2009 primary abstract describes procyclic trypomastigote
    pocket geometry and associated boundaries; the membrane domain is distinguished
    from surrounding collar and other cytoskeleton.
  accessed_at: '2026-11-03T10:10:44.247548Z'
  snapshot_sha256: ab85e1b67afa139c3840f4cd1e58a0ecd9913aa645103352341a8824a397800b
  search_scope: Europe PMC search API exact DOI query encoded in reference; resultType=core
    and format=json, one returned response page, no date filter. Inspected exact matched
    record at 2026-11-03T10:10:44.247548Z; no broader literature-absence claim.
  support: supports
- evidence_id: septin-pocket-membrane-agent-doi-10.1038_nrmicro2221
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1038/nrmicro2221
  locator: 'Europe PMC exact DOI result: complete abstract, title, author list, identifiers,
    journal and date'
  summary: Field and Carrington2009 secondary review abstract describes a specialized
    plasma-membrane invagination and trafficking context. Current access is complete
    native abstract, not full review body or publisher Key Points.
  accessed_at: '2026-11-03T10:10:44.283445Z'
  snapshot_sha256: be8dc997977d04a433ac9e5ca5535e3a8d36c02bc0b6a4f1e044cab801811906
  search_scope: Europe PMC search API exact DOI query encoded in reference; resultType=core
    and format=json, one returned response page, no date filter. Inspected exact matched
    record at 2026-11-03T10:10:44.283445Z; no broader literature-absence claim.
  support: supports
- evidence_id: septin-pocket-membrane-agent-doi-10.1016_j.pt.2020.11.005
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.pt.2020.11.005
  locator: 'Europe PMC exact DOI result: complete abstract, title, author list, identifiers,
    journal and date'
  summary: Halliday et al.2021 secondary review abstract compares trypanosomatid pocket
    morphology/function with life-cycle and niche qualifications. Native bibliography
    includes Halliday, de Castro-Neto, Alcantara, Cunha-E-Silva, Vaughan and Sunter;
    the current record shorthand is not used as a full author list.
  accessed_at: '2026-11-03T10:10:44.312457Z'
  snapshot_sha256: 2a4a18b6628465221f28d38635b2102f5d1e05c4a635e4a18231d9d73dcdb3ad
  search_scope: Europe PMC search API exact DOI query encoded in reference; resultType=core
    and format=json, one returned response page, no date filter. Inspected exact matched
    record at 2026-11-03T10:10:44.312457Z; no broader literature-absence claim.
  support: supports
- evidence_id: septin-root21-sources-NCBITaxon-33090
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/33090
  locator: Native taxonomy exact record
  summary: Reused public-source snapshot originally fetched 2026-11-03T09:33:10.011310Z;
    no fresh retrieval claimed. Viridiplantae identity/rank/lineage and aliases.
  accessed_at: '2026-11-03T09:33:10.011310Z'
  snapshot_sha256: b1394e36c6896d7ec64cdb301a239f2bc49bc435a22cc21fdba8fdc6217e2d11
  support: supports
- evidence_id: septin-root21-sources-NCBITaxon-3055
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3055
  locator: Native taxonomy exact record
  summary: Reused public-source snapshot originally fetched 2026-11-03T09:33:10.011369Z;
    no fresh retrieval claimed. Chlamydomonas reinhardtii identity/rank/lineage and
    aliases.
  accessed_at: '2026-11-03T09:33:10.011369Z'
  snapshot_sha256: a24c8f85014097148d9e865ea324b01b8d04f6bae27e893834f8abb5bd8b6a1f
  support: supports
- evidence_id: septin-root21-sources-doi-10.1098_rstb.2009.0103
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1098/rstb.2009.0103
  locator: Complete exact Europe PMC bibliography and abstract
  summary: Reused public-source snapshot originally fetched 2026-11-03T09:33:10.767625Z;
    no fresh retrieval claimed. Keeling2010 is a secondary plastid-evolution synthesis,
    not primary experimental proof of every lineage or prevalence.
  accessed_at: '2026-11-03T09:33:10.767625Z'
  snapshot_sha256: 63c6291480d57ca01d4eb770792f919c0e3128eeaae04894f1ed2f2f3fc0e886
  search_scope: Europe PMC exact DOI core query from reference, one returned page,
    no date filter; only exact match metadata/full abstract inspected at original
    2026-11-03T09:33:10.767625Z.
  support: supports
- evidence_id: septin-root21-sources-doi-10.1016_j.cell.2022.10.030
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.cell.2022.10.030
  locator: Complete exact Europe PMC primary abstract and bibliography
  summary: Reused public-source snapshot originally fetched 2026-11-03T09:33:10.803490Z;
    no fresh retrieval claimed. Jin2022 resolves a Chlamydomonas14-component TOC–TIC
    assembly spanning two envelope membranes. Its inner route is potential Tic20/YlmG
    architecture; no complete Results or raw cryo-EM audit is claimed.
  accessed_at: '2026-11-03T09:33:10.803490Z'
  snapshot_sha256: f4fc2108c3825f4a38c42eb7d109ac334b6e4d413ff1216d0d013925a2780061
  search_scope: Europe PMC exact DOI core query from reference, one returned page,
    no date filter; only exact match metadata/full abstract inspected at original
    2026-11-03T09:33:10.803490Z.
  support: supports
- evidence_id: septin-root21-sources-doi-10.1007_s00294-011-0339-1
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1007/s00294-011-0339-1
  locator: Complete exact Europe PMC secondary-review abstract and bibliography
  summary: Reused public-source snapshot originally fetched 2026-11-03T09:33:11.481915Z;
    no fresh retrieval claimed. Terashima2011 compares Chlamydomonas chloroplast proteins/metabolism
    with plant chloroplasts; the whole-chloroplast survey is not a purified stromal
    proteome or direct assay of every nucleoid constituent.
  accessed_at: '2026-11-03T09:33:11.481915Z'
  snapshot_sha256: 703d897a8f74ddaa0e9e3866f4901c10269106f75ad66a847846cdcfd96883b0
  search_scope: Europe PMC exact DOI core query from reference, one returned page,
    no date filter; only exact match metadata/full abstract inspected at original
    2026-11-03T09:33:11.481915Z.
  support: supports
- evidence_id: septin-root21-sources-keeling2010-pmc
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2817223/
  locator: Genuine secondary-review PMC HTML Abstract and section1 primary-plastid
    origin/two-boundary-membrane body; no pixels
  summary: Reused public-source snapshot originally fetched 2026-11-03T09:33:10.806914Z;
    no fresh retrieval claimed. Selected body supports primary-plastid green-algal/plant
    context with lineage qualifications.
  accessed_at: '2026-11-03T09:33:10.806914Z'
  snapshot_sha256: 9b8d3133fe3b680c1f21e7bafc458416e28de352e38d165f186f79a288bd829c
  support: supports
- evidence_id: septin-root21-sources-jin2022-author-publications
  kind: primary_source
  reference: https://lifesciences.westlake.edu.cn/labs/zhen-yan/structural-biology-laboratory/publications/
  locator: Exact author-laboratory Jin2022 entry and complete abstract only
  summary: Reused public-source snapshot originally fetched 2026-11-03T09:33:11.441964Z;
    no fresh retrieval claimed. Author-hosted abstract corroborates envelope-spanning
    Chlamydomonas assembly and potential inner pathway; it is not full paper access.
  accessed_at: '2026-11-03T09:33:11.441964Z'
  snapshot_sha256: f634a6d488c6de60b0889cb28bb8d87e171e26c10293ad64223333d32bc18b03
  support: supports
- evidence_id: septin-root21-sources-terashima2011-pdf
  kind: validation
  reference: https://link.springer.com/content/pdf/10.1007/s00294-011-0339-1.pdf
  locator: Actual nominal publisher PDF response body
  summary: Reused public-source snapshot originally fetched 2026-11-03T09:33:11.567479Z;
    no fresh retrieval claimed. The nominal PDF returned3038-byte HTML challenge.
    No new full PDF read is claimed, and old original-review body access is not impersonated.
  accessed_at: '2026-11-03T09:33:11.567479Z'
  snapshot_sha256: 32ed63159c77e21ee19ca1b9aa3213ccf0218eb59539560b132a8e68ef0e18ea
  support: supports
- evidence_id: septin-current-adapter-catalogue
  kind: search
  reference: https://imodulondb.org/api/datasets
  locator: Complete official organism/dataset JSON response; all names, IDs and dataset
    lists inspected
  summary: The complete catalogue has20 organisms,28 organism/dataset pairs and22
    distinct dataset-key strings. None matches Viridiplantae, Chlamydomonas reinhardtii
    or Trypanosoma brucei. No mismatched organism is used for downstream gene/module
    inference, and noncoverage is not biological absence.
  accessed_at: '2026-11-03T10:10:44.588777Z'
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  search_scope: iModulonDB GET /api/datasets at 2026-11-03T10:10:44.588777Z; all20
    organism entries and every associated dataset key inspected for Viridiplantae/Chlamydomonas
    and T. brucei. No date filter or gene/module lookup in an unrelated taxon. Scope
    is this complete returned catalogue only.
  support: supports
- evidence_id: septin-historical-adapter-runner
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical canary runner invocation00:49:00.848907Z–00:49:00.863225Z
  summary: Actual historical datasets invocation exited1 with PermissionError reading
    pyvenv.cfg. Receipt is reused, not a fresh invocation; current source catalogue
    fallback is separately fetched.
  accessed_at: '2026-11-03T00:49:00.863225Z'
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  support: supports
- evidence_id: septin-access-source-receipts
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/adversary-septin/source-receipts.json
  locator: Actual source request outcomes/timestamps and saved response hashes
  summary: Direct and legacy PMC pocket routes returned challenge HTML; Europe PMC
    fullTextXML returned500. Karcher publisher/PDF routes and alternate article access
    failed. Field publisher returned challenge HTML and Halliday DOI route a redirect
    stub. These are not scientific body reads.
  accessed_at: '2026-11-03T10:15:35.444371Z'
  snapshot_sha256: b21cd250fa656aad7af876defde5a868c7269f2a230362947b44ed5f40617f04
  support: supports
- evidence_id: septin-access-extra-receipts
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/adversary-septin/extra-receipts.json
  locator: Actual source request outcomes/timestamps and saved response hashes
  summary: Direct and legacy PMC pocket routes returned challenge HTML; Europe PMC
    fullTextXML returned500. Karcher publisher/PDF routes and alternate article access
    failed. Field publisher returned challenge HTML and Halliday DOI route a redirect
    stub. These are not scientific body reads.
  accessed_at: '2026-11-03T10:15:35.444371Z'
  snapshot_sha256: 99a5bd30a67ba82f00e244cccf3c684227f5d5af56e803868bc10b25d473cbae
  support: supports
- evidence_id: septin-access-browser-alternatives-receipt
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/adversary-septin/browser-alternatives-receipt.json
  locator: Actual source request outcomes/timestamps and saved response hashes
  summary: Direct and legacy PMC pocket routes returned challenge HTML; Europe PMC
    fullTextXML returned500. Karcher publisher/PDF routes and alternate article access
    failed. Field publisher returned challenge HTML and Halliday DOI route a redirect
    stub. These are not scientific body reads.
  accessed_at: '2026-11-03T10:15:35.444371Z'
  snapshot_sha256: ee69db589ffe1a125cc8168272995d11b4edd9ea2355132becdf516736604393
  support: supports
- evidence_id: septin-gadelha-indexed-body
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2755463/
  locator: Only returned indexed Discussion subsections Surface Membrane Domains,
    Boundaries Between Continuous Surface Domains and No Endocytosis Regionalization
    in the FP
  summary: Primary discussion distinguishes membrane domains from the collar and keeps
    mechanisms qualified. This indexed excerpt is not a complete direct PMC body read.
  accessed_at: '2026-11-03T10:12:00Z'
  snapshot_sha256: 90a594d910d4dbb1eaf7286992a2bdd2da8026beb54728aace3e9181a8ba9990
  support: supports
- evidence_id: septin-lacomble-indexed-methods
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2714436/
  locator: 'Only returned indexed Materials and Methods: Cell culture, sample preparation,
    TEM and cellular tomography'
  summary: The methods identify procyclic T. brucei brucei strain427. This limited
    methods access does not make a full article or image audit.
  accessed_at: '2026-11-03T10:12:23Z'
  snapshot_sha256: bdbcd488b53c5d46399edd9548cf4a3f31a7ae60f224138ddaaa51a06f6244ca
  support: supports
- evidence_id: septin-pocket-source-search
  kind: search
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/adversary-septin/browser-source-receipts.json
  locator: Bounded web retrieval queries and only returned exact-primary results
  summary: Queries retrieved the specifically documented primary excerpts and possible
    access routes. Unrelated returned pages were discarded. Failed direct opens do
    not erase indexed excerpt access; no exhaustive absence finding is made.
  accessed_at: '2026-11-03T10:12:00Z'
  snapshot_sha256: dcb7e3e6ee266639f691ccb2baae445a6c7d9f951515576bfae49bc711d22847
  search_scope: 'Web search at 2026-11-03 10:12:00 UTC; exact queries [{"q": "\"Membrane
    domains and flagellar pocket boundaries\" pdf"}, {"q": "\"Three-dimensional cellular
    architecture\" \"045740\" full text"}]; response_length=long, first returned result
    set only, no recency filter. Only exact primary-article matches at PMC were used
    scientifically; unrelated results and unverified mirrored documents were excluded.'
  support: supports
- evidence_id: septin-pocket-stage-search
  kind: search
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/adversary-septin/browser-stage-search.json
  locator: Bounded web retrieval queries and only returned exact-primary results
  summary: Queries retrieved the specifically documented primary excerpts and possible
    access routes. Unrelated returned pages were discarded. Failed direct opens do
    not erase indexed excerpt access; no exhaustive absence finding is made.
  accessed_at: '2026-11-03T10:12:23Z'
  snapshot_sha256: b94ed98b7fb99b24b70c7dad7fab19730ea3239cb86cbcbc8b3fc2265d18eb7d
  search_scope: 'Web search at 2026-11-03 10:12:23 UTC; exact queries [{"q": "site:pmc.ncbi.nlm.nih.gov/articles/PMC2755463
    \"bloodstream\" \"Methods\""}, {"q": "site:pmc.ncbi.nlm.nih.gov/articles/PMC2714436
    \"Cell culture\" \"427\""}]; response_length=long, first returned result set only,
    no recency filter. Only exact primary-article matches at PMC were used scientifically;
    unrelated results and unverified mirrored documents were excluded.'
  support: supports
- evidence_id: check-qc
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/qc.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T10:16:47.222139Z'
  support: supports
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  snapshot_sha256: 20f7bad03e784220358c993ec3b3478410e64b748aaef1b1c6ae4065172a6c08
- evidence_id: check-labels
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/labels.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T10:11:48.985853Z'
  support: supports
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  snapshot_sha256: 6cdfb05df9a27194f05a5fd7f851783f817ac1523ca0bbfa54fe0e0d18775905
- evidence_id: check-trait-links
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/trait-links.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T10:11:23.258015Z'
  support: supports
  summary: Native TraitMech link check passed.
  snapshot_sha256: 8b336cdefbbd3daf6da8787990efdbe346c95e2c8361d50b7eb68a18f2d5a44a
- evidence_id: check-vendored
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/vendored.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T10:11:26.639781Z'
  support: supports
  summary: Pinned governed files match; native vendored check passed.
  snapshot_sha256: b1f169d103aaefa930745468bcca171e5867b9cc49e4e74311e458097e3252a6
- evidence_id: check-curies
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/curies.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T10:11:51.049067Z'
  support: supports
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  snapshot_sha256: fb3be251020aac118f6df680372ae7aaa32c2a1dd3366648cde95494f19d9dd2
- evidence_id: focused
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/focused-results.json
  locator: All twenty actual target schema/strict command outputs
  accessed_at: '2026-11-03T10:20:14Z'
  support: supports
  summary: Ten schema and ten strict commands returned exit zero.
  snapshot_sha256: 1ba661624d602ea73601028d5af00a1e7c2b02975f2fbd223596089c875af461
- evidence_id: supplemental-pmid
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2359/pmid-chunks-receipt.json
  locator: Complete native-report PMID set checked with unchanged resolver in batches
    of at most fifty
  accessed_at: '2026-11-03T10:12:49.848713Z'
  support: supports
  summary: 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers
    remain unverified.
  snapshot_sha256: ccbe272d86622a109a22031894f86ad84aadd18316c3cf0355487a847fa0391a
- evidence_id: historical-adapter-runner-availability
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical runner invocation receipt, cross-checked against exact stdout/stderr
    hashes; reread during PR2359 synthesis
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  summary: Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS
    PermissionError reading the configured runner pyvenv.cfg. This is a retained historical
    availability observation, not a fresh attempt or a scientific validation failure.
    Native policy permits inspected source-catalogue fallback.
assessments:
- assessment_id: plaque-t3-identity
  area: identity
  topic: Whole thylakoid, membrane and lumen are distinct
  outcome: supported
  target_ids:
  - GO:0009534
  summary: GO0009534 and SL0056 identify the whole chloroplast thylakoid, with plastid
    and broader thylakoid parents, chloroplast parthood and membrane/lumen parts.
    OTHER is consistent with GO’s explicit non-organelle comment and the absence of
    a closer non-organelle bounded-compartment kind. The membrane encloses the lumen
    rather than the complete membrane-plus-lumen structure.
  evidence_ids:
  - plaque-thylakoid-agent-go
  - plaque-thylakoid-agent-SL-0056
  - plaque-thylakoid-agent-SL-0057
  - plaque-thylakoid-agent-SL-0058
  - plaque-current-4
  - plaque-current-5
  - plaque-current-3
  - plaque-isa-0009534
- assessment_id: plaque-t3-composition
  area: grounding
  topic: The own membrane part is an appropriate structural component
  outcome: supported
  target_ids:
  - GO:0009534
  summary: The single membrane row identifies an actual own structural part with exact
    GO0009535 grounding and LIPID material type. It denotes the constituent pigmented
    membrane, not an individual lipid species or photosynthetic protein. No conflicting
    family assignment or universal inventory is asserted.
  evidence_ids:
  - plaque-thylakoid-agent-go
  - plaque-thylakoid-agent-SL-0056
  - plaque-thylakoid-agent-SL-0057
  - plaque-thylakoid-agent-SL-0058
  - plaque-thylakoid-agent-engel2015-jats
  - plaque-current-3
  - plaque-policy
- assessment_id: plaque-t3-necessity
  area: evidence
  topic: Constituting membrane versus molecular formation requirements
  outcome: unknown
  target_ids:
  - GO:0009534
  summary: A membrane is constitutive of the membrane-bounded thylakoid named by the
    ESSENTIAL row. The sources do not establish that each pigment, lipid species or
    photosynthetic complex is necessary for thylakoid formation. Proposed biogenesis
    routes and photosynthetic activity must remain separate from that experimental
    question.
  evidence_ids:
  - plaque-thylakoid-agent-engel2015-jats
  - plaque-thylakoid-agent-terashima2011-pdf
  - plaque-thylakoid-agent-go
  - plaque-current-3
  - plaque-policy
- assessment_id: plaque-t3-functions
  area: evidence
  topic: Electron transport and proton-gradient generation
  outcome: supported
  target_ids:
  - GO:0009534
  summary: GO0009767 precisely matches the maintained electron-transport function;
    native location authority and the inspected Terashima review support the membrane
    site and trans-thylakoid gradient. This does not transfer stromal carbon-fixation
    machinery into the thylakoid or claim all light reactions are a single protein
    complex.
  evidence_ids:
  - plaque-thylakoid-agent-go
  - plaque-thylakoid-agent-SL-0056
  - plaque-thylakoid-agent-SL-0057
  - plaque-thylakoid-agent-SL-0058
  - plaque-thylakoid-agent-terashima2011-pdf
  - plaque-thylakoid-agent-engel2015-jats
  - plaque-perez-body-electron-transport
  - plaque-current-3
- assessment_id: plaque-t3-graph
  area: graph
  topic: Explicitly nonmechanistic whole-thylakoid topology
  outcome: supported
  target_ids:
  - GO:0009534
  summary: 'All five current edges were assessed: original stroma embedding, membrane-encloses-lumen
    and photosynthetic-function relations, plus the two added membrane/lumen part_of
    whole-thylakoid edges. Fresh GO typed direct children and UniProt immediate partOf
    hosts support both additions. They do not reintroduce membrane-bounds-the-whole,
    assert complete carrier chemistry or terminally dispose of historical735/736.'
  evidence_ids:
  - plaque-thylakoid-agent-go
  - plaque-thylakoid-agent-SL-0056
  - plaque-thylakoid-agent-SL-0057
  - plaque-thylakoid-agent-SL-0058
  - plaque-thylakoid-agent-engel2015-jats
  - plaque-thylakoid-agent-terashima2011-pdf
  - plaque-current-3
  - plaque-policy
- assessment_id: plaque-t3-scope
  area: scope
  topic: Green-lineage occurrence with a direct Chlamydomonas example
  outcome: supported
  target_ids:
  - GO:0009534
  summary: Current taxonomy verifies Viridiplantae33090 and C.reinhardtii3055. Engel
    directly studies CC-124/137c in TAP under constant light; the primary body supports
    the native membrane/lumen species example while distinguishing algal organization
    from higher-plant grana. Perez/Terashima secondary context and the primary Introduction
    support qualitative photosynthetic green-lineage occurrence. Keeling selected
    secondary body preserves nonphotosynthetic-plastid limits. COMMON is not measured
    prevalence; no universal architecture or experimental stock transfer is inferred.
  evidence_ids:
  - plaque-thylakoid-agent-go
  - plaque-thylakoid-agent-NCBITaxon-33090
  - plaque-thylakoid-agent-NCBITaxon-3055
  - plaque-thylakoid-agent-engel2015-jats
  - plaque-perez-body-introduction
  - plaque-thylakoid-agent-terashima2011-pdf
  - plaque-thylakoid-agent-doi-10.1098_rstb.2009.0103
  - plaque-current-3
  - plaque-thylakoid-agent-keeling2010-pmc
- assessment_id: plaque-t3-coverage
  area: completeness
  topic: Bounded clean assessment
  outcome: supported
  target_ids:
  - GO:0009534
  summary: No scientific record-curation defect was established within the inspected
    claims. Optional protein inventories, images, numerical dimensions and expanded
    mechanisms are not mandatory. The Engel correction concerns a Figure3 scale unit
    absent from these records. Historical issue numbers in record history are preserved
    as history, not independently terminally resolved by this review. Bundle freshness/applicability
    corrections are separate.
  evidence_ids:
  - plaque-thylakoid-agent-go
  - plaque-thylakoid-agent-engel2015-jats
  - plaque-thylakoid-agent-engel2015-correction
  - plaque-perez-body-introduction
  - plaque-perez-body-electron-transport
  - plaque-thylakoid-agent-SL-0056
  - plaque-thylakoid-agent-SL-0057
  - plaque-thylakoid-agent-SL-0058
  - plaque-current-3
  - plaque-policy
- assessment_id: plaque-t3-native-protein
  area: schema
  topic: Native protein identity and graph checks
  outcome: supported
  summary: Both actual focused commands exited0. All three targets have empty protein-example
    inventories and zero GENE_OR_PROTEIN nodes. Exact material/structure nodes are
    not forced into protein coverage; these checks do not prove narrative molecular
    function, localization or assembly necessity.
  target_ids:
  - GO:0009534
  evidence_ids:
  - plaque-current-3
  - plaque-native-chloroplast_thylakoid-verify
  - plaque-native-chloroplast_thylakoid-causal
- assessment_id: plaque-t3-bundle-provenance
  area: provenance
  topic: Original native artifacts and frozen target comparison
  outcome: supported
  summary: Original YAML validates and Markdown is byte-identical to native render.
    Historical target bytes match its original frozen hash. Current whole-thylakoid
    differs by added history and two parthood edges; these are independently refreshed
    against current authorities. Immutable originals are preserved.
  target_ids:
  - GO:0009534
  evidence_ids:
  - plaque-current-3
  - plaque-original-3
- assessment_id: plaque-t3-adapter
  area: scope
  topic: Named photosynthetic pathways and covered-host assessment
  outcome: supported
  summary: Photosynthetic electron transport/light-reaction claims trigger applicability
    despite no transcriptomic assertion. The fresh complete source catalogue contains
    no matched Chlamydomonas/green-lineage host dataset; cyanobacterial S.elongatus
    cannot substitute for chloroplast evidence. No downstream gene/module search applies,
    and catalogue noncoverage is not biological absence. Historical runner unavailability
    remains separately dated.
  target_ids:
  - GO:0009534
  evidence_ids:
  - plaque-current-3
  - plaque-policy
  - plaque-catalogue
  - plaque-historical-runner
- assessment_id: plaque-t4-identity
  area: identity
  topic: Enclosed volume and plastid-lumen hierarchy
  outcome: supported
  target_ids:
  - GO:0009543
  summary: GO0009543 and SL0057 identify the lumen as the space inside chloroplast
    thylakoid membranes. Plastid-thylakoid-lumen parentage and whole-thylakoid parthood
    are supported. The maintained definition is a faithful paraphrase of the current
    cavity definition, not an identity change.
  evidence_ids:
  - plaque-thylakoid-agent-go
  - plaque-thylakoid-agent-SL-0057
  - plaque-thylakoid-agent-SL-0058
  - plaque-current-3
  - plaque-current-5
  - plaque-thylakoid-agent-engel2015-jats
  - plaque-current-4
  - plaque-isa-0009543
- assessment_id: plaque-t4-composition
  area: grounding
  topic: Boundary membrane is not a lumen constituent
  outcome: supported
  target_ids:
  - GO:0009543
  summary: The intentionally empty component inventory is coherent for a subcellular
    region. Its bounding membrane is a graph boundary, not a component located inside
    the lumen. No exact lumenal protein inventory, necessity, stoichiometry or family
    grounding is asserted, so no assembly-essentiality claim needs reinterpretation.
  evidence_ids:
  - plaque-thylakoid-agent-go
  - plaque-thylakoid-agent-SL-0057
  - plaque-thylakoid-agent-SL-0058
  - plaque-perez-body-introduction
  - plaque-thylakoid-agent-engel2015-jats
  - plaque-current-4
  - plaque-policy
- assessment_id: plaque-t4-graph
  area: graph
  topic: Minimal boundary relation with appropriate scope
  outcome: supported
  target_ids:
  - GO:0009543
  summary: The single encloses edge links the correct membrane and lumen authorities.
    NONMECHANISTIC accurately describes this topology and does not assert a proton-transfer
    or lumenal-protein mechanism. The absence of an optional function field is not
    a defect.
  evidence_ids:
  - plaque-thylakoid-agent-go
  - plaque-thylakoid-agent-SL-0057
  - plaque-thylakoid-agent-SL-0058
  - plaque-perez-body-introduction
  - plaque-thylakoid-agent-engel2015-jats
  - plaque-current-4
  - plaque-policy
- assessment_id: plaque-t4-scope
  area: scope
  topic: Green-lineage occurrence with a direct Chlamydomonas example
  outcome: supported
  target_ids:
  - GO:0009543
  summary: Current taxonomy verifies Viridiplantae33090 and C.reinhardtii3055. Engel
    directly studies CC-124/137c in TAP under constant light; the primary body supports
    the native membrane/lumen species example while distinguishing algal organization
    from higher-plant grana. Perez/Terashima secondary context and the primary Introduction
    support qualitative photosynthetic green-lineage occurrence. Keeling selected
    secondary body preserves nonphotosynthetic-plastid limits. COMMON is not measured
    prevalence; no universal architecture or experimental stock transfer is inferred.
  evidence_ids:
  - plaque-thylakoid-agent-go
  - plaque-thylakoid-agent-NCBITaxon-33090
  - plaque-thylakoid-agent-NCBITaxon-3055
  - plaque-thylakoid-agent-engel2015-jats
  - plaque-perez-body-introduction
  - plaque-current-4
  - plaque-thylakoid-agent-keeling2010-pmc
  - plaque-thylakoid-agent-terashima2011-pdf
- assessment_id: plaque-t4-coverage
  area: completeness
  topic: Bounded clean assessment
  outcome: supported
  target_ids:
  - GO:0009543
  summary: No scientific record-curation defect was established within the inspected
    claims. Optional protein inventories, images, numerical dimensions and expanded
    mechanisms are not mandatory. The Engel correction concerns a Figure3 scale unit
    absent from these records. Historical issue numbers in record history are preserved
    as history, not independently terminally resolved by this review. Bundle freshness/applicability
    corrections are separate.
  evidence_ids:
  - plaque-thylakoid-agent-go
  - plaque-thylakoid-agent-engel2015-jats
  - plaque-thylakoid-agent-engel2015-correction
  - plaque-perez-body-introduction
  - plaque-perez-body-electron-transport
  - plaque-thylakoid-agent-SL-0057
  - plaque-thylakoid-agent-SL-0058
  - plaque-current-4
  - plaque-policy
- assessment_id: plaque-t4-native-protein
  area: schema
  topic: Native protein identity and graph checks
  outcome: supported
  summary: Both actual focused commands exited0. All three targets have empty protein-example
    inventories and zero GENE_OR_PROTEIN nodes. Exact material/structure nodes are
    not forced into protein coverage; these checks do not prove narrative molecular
    function, localization or assembly necessity.
  target_ids:
  - GO:0009543
  evidence_ids:
  - plaque-current-4
  - plaque-native-chloroplast_thylakoid_lumen-verify
  - plaque-native-chloroplast_thylakoid_lumen-causal
- assessment_id: plaque-t4-bundle-provenance
  area: provenance
  topic: Original native artifacts and frozen target comparison
  outcome: supported
  summary: Original YAML validates and Markdown is byte-identical to native render.
    Historical target bytes match its original frozen hash. Current target bytes remain
    unchanged from the original frozen input. Immutable originals are preserved.
  target_ids:
  - GO:0009543
  evidence_ids:
  - plaque-current-4
  - plaque-original-4
- assessment_id: plaque-t4-adapter
  area: scope
  topic: Sparse lumen topology and actual applicability trigger
  outcome: not_applicable
  summary: The lumen record asserts an enclosed region, its boundary and occurrence;
    it explicitly refrains from lumenal proteins and proton-transport mechanisms.
    No represented gene, accession, regulator, molecular pathway or stress response
    requires module analysis. No molecular inventory is invented. The missing original
    adapter row is a genuine topology-only exclusion, not a bundle defect.
  target_ids:
  - GO:0009543
  evidence_ids:
  - plaque-current-4
  - plaque-policy
  - plaque-catalogue
- assessment_id: plaque-t5-identity
  area: identity
  topic: Chloroplast-specific membrane and broader parents
  outcome: supported
  target_ids:
  - GO:0009535
  summary: GO0009535 and SL0058 exactly identify the chloroplast thylakoid membrane.
    Direct plastid-thylakoid-membrane ancestry plus transitive generic thylakoid-membrane
    ancestry are coherent, and parthood in the whole chloroplast thylakoid is supported.
    Bacterial and cyanelle membranes remain broader-class context, not exact synonyms.
  evidence_ids:
  - plaque-thylakoid-agent-go
  - plaque-thylakoid-agent-SL-0056
  - plaque-thylakoid-agent-SL-0057
  - plaque-thylakoid-agent-SL-0058
  - plaque-current-3
  - plaque-current-4
  - plaque-current-5
  - plaque-isa-0009535
- assessment_id: plaque-t5-composition
  area: grounding
  topic: Collective lipid bilayer without forced molecular grounding
  outcome: supported
  target_ids:
  - GO:0009535
  summary: The component names collective thylakoid lipid material. Exact location
    authorities identify the complete membrane, not an individual source-neutral lipid
    class; reviewed-label-only representation and the open grounding discussion are
    appropriate. The source does not require a complete photosystem or antenna inventory
    in this membrane record.
  evidence_ids:
  - plaque-thylakoid-agent-go
  - plaque-thylakoid-agent-SL-0056
  - plaque-thylakoid-agent-SL-0057
  - plaque-thylakoid-agent-SL-0058
  - plaque-thylakoid-agent-engel2015-jats
  - plaque-thylakoid-agent-terashima2011-pdf
  - plaque-current-5
  - plaque-policy
- assessment_id: plaque-t5-necessity
  area: evidence
  topic: Material constitution and empirical formation requirements
  outcome: unknown
  target_ids:
  - GO:0009535
  summary: The ESSENTIAL row represents constituting membrane material. None of the
    reviewed photosynthetic proteins, pigments or lipid species is thereby demonstrated
    necessary for forming a thylakoid membrane. Activity, light acclimation, proteomic
    localization and proposed biogenesis do not resolve those individual assembly
    requirements.
  evidence_ids:
  - plaque-thylakoid-agent-engel2015-jats
  - plaque-thylakoid-agent-terashima2011-pdf
  - plaque-thylakoid-agent-go
  - plaque-current-5
  - plaque-policy
- assessment_id: plaque-t5-functions
  area: evidence
  topic: Light reactions at the membrane surface
  outcome: supported
  target_ids:
  - GO:0009535
  summary: GO0019684, SL0058 and the inspected Terashima/Perez review sections support
    the membrane’s light-reaction site, electron transfer and trans-thylakoid proton
    gradient. The function does not equate electron transport with carbon fixation
    or assert a complete source-neutral protein mechanism.
  evidence_ids:
  - plaque-thylakoid-agent-go
  - plaque-thylakoid-agent-SL-0056
  - plaque-thylakoid-agent-SL-0057
  - plaque-thylakoid-agent-SL-0058
  - plaque-thylakoid-agent-engel2015-jats
  - plaque-thylakoid-agent-terashima2011-pdf
  - plaque-perez-body-electron-transport
  - plaque-current-5
- assessment_id: plaque-t5-graph
  area: graph
  topic: Collective membrane node and boundary/function edges
  outcome: supported
  target_ids:
  - GO:0009535
  summary: The membrane node’s component_ref denotes its collective lipid-bilayer
    constituent, consistent with this membrane-only record; it does not identify the
    complete thylakoid compartment as lipid material. Encloses and supports edges
    correctly express boundary and general functional site. Explicit NONMECHANISTIC
    scope avoids unsupported complete carrier chemistry.
  evidence_ids:
  - plaque-thylakoid-agent-go
  - plaque-thylakoid-agent-SL-0056
  - plaque-thylakoid-agent-SL-0057
  - plaque-thylakoid-agent-SL-0058
  - plaque-thylakoid-agent-engel2015-jats
  - plaque-thylakoid-agent-terashima2011-pdf
  - plaque-perez-body-electron-transport
  - plaque-current-5
  - plaque-policy
- assessment_id: plaque-t5-scope
  area: scope
  topic: Green-lineage occurrence with a direct Chlamydomonas example
  outcome: supported
  target_ids:
  - GO:0009535
  summary: Current taxonomy verifies Viridiplantae33090 and C.reinhardtii3055. Engel
    directly studies CC-124/137c in TAP under constant light; the primary body supports
    the native membrane/lumen species example while distinguishing algal organization
    from higher-plant grana. Perez/Terashima secondary context and the primary Introduction
    support qualitative photosynthetic green-lineage occurrence. Keeling selected
    secondary body preserves nonphotosynthetic-plastid limits. COMMON is not measured
    prevalence; no universal architecture or experimental stock transfer is inferred.
  evidence_ids:
  - plaque-thylakoid-agent-go
  - plaque-thylakoid-agent-NCBITaxon-33090
  - plaque-thylakoid-agent-NCBITaxon-3055
  - plaque-thylakoid-agent-engel2015-jats
  - plaque-perez-body-introduction
  - plaque-thylakoid-agent-terashima2011-pdf
  - plaque-thylakoid-agent-doi-10.1098_rstb.2009.0103
  - plaque-current-5
  - plaque-thylakoid-agent-keeling2010-pmc
- assessment_id: plaque-t5-coverage
  area: completeness
  topic: Bounded clean assessment
  outcome: supported
  target_ids:
  - GO:0009535
  summary: No scientific record-curation defect was established within the inspected
    claims. Optional protein inventories, images, numerical dimensions and expanded
    mechanisms are not mandatory. The Engel correction concerns a Figure3 scale unit
    absent from these records. Historical issue numbers in record history are preserved
    as history, not independently terminally resolved by this review. Bundle freshness/applicability
    corrections are separate.
  evidence_ids:
  - plaque-thylakoid-agent-go
  - plaque-thylakoid-agent-engel2015-jats
  - plaque-thylakoid-agent-engel2015-correction
  - plaque-perez-body-introduction
  - plaque-perez-body-electron-transport
  - plaque-thylakoid-agent-SL-0056
  - plaque-thylakoid-agent-SL-0057
  - plaque-thylakoid-agent-SL-0058
  - plaque-current-5
  - plaque-policy
- assessment_id: plaque-t5-native-protein
  area: schema
  topic: Native protein identity and graph checks
  outcome: supported
  summary: Both actual focused commands exited0. All three targets have empty protein-example
    inventories and zero GENE_OR_PROTEIN nodes. Exact material/structure nodes are
    not forced into protein coverage; these checks do not prove narrative molecular
    function, localization or assembly necessity.
  target_ids:
  - GO:0009535
  evidence_ids:
  - plaque-current-5
  - plaque-native-chloroplast_thylakoid_membrane-verify
  - plaque-native-chloroplast_thylakoid_membrane-causal
- assessment_id: plaque-t5-bundle-provenance
  area: provenance
  topic: Original native artifacts and frozen target comparison
  outcome: supported
  summary: Original YAML validates and Markdown is byte-identical to native render.
    Historical target bytes match its original frozen hash. Current target bytes remain
    unchanged from the original frozen input. Immutable originals are preserved.
  target_ids:
  - GO:0009535
  evidence_ids:
  - plaque-current-5
  - plaque-original-5
- assessment_id: plaque-t5-adapter
  area: scope
  topic: Named photosynthetic pathways and covered-host assessment
  outcome: supported
  summary: Photosynthetic electron transport/light-reaction claims trigger applicability
    despite no transcriptomic assertion. The fresh complete source catalogue contains
    no matched Chlamydomonas/green-lineage host dataset; cyanobacterial S.elongatus
    cannot substitute for chloroplast evidence. No downstream gene/module search applies,
    and catalogue noncoverage is not biological absence. Historical runner unavailability
    remains separately dated.
  target_ids:
  - GO:0009535
  evidence_ids:
  - plaque-current-5
  - plaque-policy
  - plaque-catalogue
  - plaque-historical-runner
- assessment_id: plaque-t3-stale-refresh
  area: graph
  topic: Two newly added parthood edges
  outcome: supported
  summary: Current edges3 and4 add membrane0009535 and lumen0009543 as parts of whole
    thylakoid0009534. GO0009534 directly lists both typed part_of children; SL0057/0058
    directly name SL0056 as partOf, with broader plastid-thylakoid ancestry separately
    represented. These facts support both additions without confusing subclass identity,
    enclosing boundaries or mechanism. No stale delta remains unrefreshable.
  target_ids:
  - GO:0009534
  evidence_ids:
  - plaque-current-3
  - plaque-original-3
  - plaque-thylakoid-agent-go
  - plaque-thylakoid-agent-SL-0056
  - plaque-thylakoid-agent-SL-0057
  - plaque-thylakoid-agent-SL-0058
- assessment_id: micro-chlorosome-a1
  area: identity
  topic: Whole versus envelope identity and hierarchy
  outcome: supported
  summary: Exact active GO and UniProt definitions distinguish chlorosome, its monolayer
    envelope and lipid bilayers. The OTHER kind and intracellular membraneless-parent
    interpretation do not deny the glycolipid boundary; envelope and whole baseplate
    are separate scopes.
  target_ids:
  - GO:0046858
  evidence_ids:
  - micro-record-chlorosome
  - micro-chl-go
  - micro-chl-SL-0060
  - micro-neighbor-baseplate
- assessment_id: micro-chlorosome-a2
  area: grounding
  topic: Csm identities, reviewed status and bounded family coverage
  outcome: supported
  summary: 'All ten declared accessions match TLS genes: seven reviewed, three unreviewed.
    Accessory location cohort spans distinct families/domains; no single exact family
    should replace that set. The baseplate denotes the assembled CsmA/BChl-a complex,
    not the apoprotein family. csmK query miss and H2VFJ4 match204 do not prove absence.'
  target_ids:
  - GO:0046858
  evidence_ids:
  - micro-record-chlorosome
  - micro-chl-P0A314
  - micro-chl-Q46383
  - micro-chl-Q46367
  - micro-chl-Q46386
  - micro-chl-O68986
  - micro-chl-O68988
  - micro-chl-O68983
  - micro-chl-H2VFJ4
  - micro-chl-H2VFJ1
  - micro-chl-Q8KEN5
  - micro-chl-matches-P0A314
  - micro-chl-matches-Q46383
  - micro-chl-matches-Q46367
  - micro-chl-matches-Q46386
  - micro-chl-matches-O68986
  - micro-chl-matches-O68988
  - micro-chl-matches-O68983
  - micro-chl-matches-H2VFJ4
  - micro-chl-matches-H2VFJ1
  - micro-chl-matches-Q8KEN5
  - micro-chl-reviewed-csm-query
  - micro-chl-csmK-query
- assessment_id: micro-chlorosome-a3
  area: evidence
  topic: Constituents versus formation necessity
  outcome: concern
  summary: 'Inherited F1 remains confirmed: the ESSENTIAL baseplate annotation asserts
    target formation necessity beyond the cited experiments. Preserve positive structural
    integrity, antenna, attachment and viability roles. Frigaard2004 did not obtain
    segregated CsmA-loss mutants; Nielsen used bchK-mutant carotenosomes with a retained
    baseplate. Neither proves dispensability or universal failure of formation. Collective
    monolayer/pigment material is constitutional, not evidence that each molecular
    species is individually required.'
  target_ids:
  - GO:0046858
  evidence_ids:
  - micro-record-chlorosome
  - micro-schema-necessity
  - micro-chl-nielsen2016-jats
  - micro-frigaard2004
  - micro-chl-frigaard2005-meta
- assessment_id: micro-chlorosome-a4
  area: scope
  topic: Taxon examples and distribution
  outcome: supported
  summary: C. tepidum structural/genetic and C. aurantiacus J-10-fl imaging sources
    support the bounded examples. VARIABLE Bacteria and named phototrophic groups
    are secondary-context scope, not universal bacterial membership. Nielsen high-resolution
    preparation is mutant carotenosome; its wild-type comparisons and earlier AFM
    context are kept explicit.
  target_ids:
  - GO:0046858
  evidence_ids:
  - micro-record-chlorosome
  - micro-chl-tax-2
  - micro-chl-tax-1097
  - micro-chl-tax-1108
  - micro-chl-tax-194439
  - micro-chl-nielsen2016-jats
  - micro-frigaard2004
  - micro-psencik2009-retained-body
  - micro-chl-oostergetel2010-jats
  - micro-orf2013-browser
- assessment_id: micro-chlorosome-a5
  area: evidence
  topic: Light harvesting and component-localization roles
  outcome: supported
  summary: Pigment self-assembly, asymmetric envelope and baseplate energy transfer
    have authority/primary structural support. Secondary sources supply broader antenna
    context. Broad photosynthesis GO is not substituted for exact light harvesting,
    and heterogeneous accessory composition is not silently made universally essential.
  target_ids:
  - GO:0046858
  evidence_ids:
  - micro-record-chlorosome
  - micro-chl-go
  - micro-chl-nielsen2016-jats
  - micro-psencik2009-retained-body
  - micro-chl-oostergetel2010-jats
  - micro-orf2013-browser
  - micro-chl-li2006-meta
- assessment_id: micro-chlorosome-a6
  area: graph
  topic: 'Stale refresh: baseplate node identity'
  outcome: supported
  summary: Current csma_baseplate node is STRUCTURE and grounded to the frozen whole
    baseplate neighbor. This accurately denotes the assembled complex; the associated
    csmA example is not mistaken for the structure itself. This current-content assessment
    does not resolve an unfrozen multi-target category finding or all of closed issue2419.
  target_ids:
  - GO:0046858
  evidence_ids:
  - micro-record-chlorosome
  - micro-prior-chlorosome
  - micro-neighbor-baseplate
  - micro-chl-nielsen2016-jats
  - micro-graph-contract
  - micro-original-validation-inputs
- assessment_id: micro-chlorosome-a7
  area: graph
  topic: 'Stale refresh: new accessory Csm surface-localization edge'
  outcome: supported
  summary: The added component-linked accessory Csm node localizes to the monolayer
    surface, consistent with the explicitly secondary Orf protein section and primary
    envelope studies. Location is accepted at cohort/context scope, not as a new universal
    assembly mechanism or a direct-contact network. Gene-family heterogeneity and
    K example gap remain explicit.
  target_ids:
  - GO:0046858
  evidence_ids:
  - micro-record-chlorosome
  - micro-orf2013-browser
  - micro-chl-li2006-meta
  - micro-frigaard2004
  - micro-graph-contract
  - micro-native-chlorosome-causal
- assessment_id: micro-chlorosome-a8
  area: graph
  topic: Existing seven-edge pigment/baseplate energy-flow model
  outcome: supported
  summary: Existing self-assembly, monolayer enclosure, baseplate constituent, excitation
    transfer and acceptor/photochemistry edges are coarse supported organization.
    The MECHANISTIC label does not prove a complete molecular transfer mechanism;
    the generic unanchored acceptor and taxon-dependent downstream coupling remain
    bounded. The separate ESSENTIAL field remains F1, rather than treating a constituent
    forms edge as a direct deletion experiment.
  target_ids:
  - GO:0046858
  evidence_ids:
  - micro-record-chlorosome
  - micro-chl-go
  - micro-chl-nielsen2016-jats
  - micro-chl-oostergetel2010-jats
  - micro-native-chlorosome-causal
  - micro-graph-contract
- assessment_id: micro-chlorosome-a9
  area: scope
  topic: Missing original structured-source applicability assessment
  outcome: concern
  summary: Original review omits applicability despite explicit Csm genes/accessions
    and light-harvesting pathway context. Current bounded catalogue contains no matching
    chlorosome-bearing organism dataset. Historical runner unavailable result and
    current fallback are separately dated; no unmatched bacterial gene query is substituted.
  target_ids:
  - GO:0046858
  evidence_ids:
  - micro-record-chlorosome
  - micro-prior-chlorosome
  - micro-review-policy
  - micro-review-config
  - micro-adapter-catalogue
  - micro-historical-adapter-runner
- assessment_id: micro-chlorosome-a10
  area: schema
  topic: Original provenance, current checks and native limits
  outcome: supported
  summary: Original pair validates and deterministically renders; frozen old blob
    is verified and current delta substantively reassessed. Six current slice protein
    receipts are actual exit0. Coverage labels retain gaps rather than upgrading them
    to experimental membership/necessity or automatic scientific defects.
  target_ids:
  - GO:0046858
  evidence_ids:
  - micro-record-chlorosome
  - micro-original-validation-inputs
  - micro-native-chlorosome-verify
  - micro-native-chlorosome-causal
- assessment_id: micro-chlorosome-a11
  area: provenance
  topic: Exact finding lineage and current verdict
  outcome: concern
  summary: Retain exact original F1 occurrence and stable issue key as open confirmed
    major; current verdict needs_curation. Stale review refresh is feasible within
    a review-only successor; scientific record edits remain separately proposed.
  target_ids:
  - GO:0046858
  evidence_ids:
  - micro-record-chlorosome
  - micro-prior-chlorosome
  - micro-schema-necessity
  - micro-frigaard2004
  - micro-chl-nielsen2016-jats
- assessment_id: micro-chlorosome_envelope-a1
  area: identity
  topic: Whole versus envelope identity and hierarchy
  outcome: supported
  summary: Exact active GO and UniProt definitions distinguish chlorosome, its monolayer
    envelope and lipid bilayers. The OTHER kind and intracellular membraneless-parent
    interpretation do not deny the glycolipid boundary; envelope and whole baseplate
    are separate scopes.
  target_ids:
  - GO:0033105
  evidence_ids:
  - micro-record-chlorosome_envelope
  - micro-chl-go
  - micro-chl-SL-0060
  - micro-neighbor-baseplate
- assessment_id: micro-chlorosome_envelope-a2
  area: grounding
  topic: Csm identities, reviewed status and bounded family coverage
  outcome: supported
  summary: 'All ten declared accessions match TLS genes: seven reviewed, three unreviewed.
    Accessory location cohort spans distinct families/domains; no single exact family
    should replace that set. The baseplate denotes the assembled CsmA/BChl-a complex,
    not the apoprotein family. csmK query miss and H2VFJ4 match204 do not prove absence.'
  target_ids:
  - GO:0033105
  evidence_ids:
  - micro-record-chlorosome_envelope
  - micro-chl-P0A314
  - micro-chl-Q46383
  - micro-chl-Q46367
  - micro-chl-Q46386
  - micro-chl-O68986
  - micro-chl-O68988
  - micro-chl-O68983
  - micro-chl-H2VFJ4
  - micro-chl-H2VFJ1
  - micro-chl-Q8KEN5
  - micro-chl-matches-P0A314
  - micro-chl-matches-Q46383
  - micro-chl-matches-Q46367
  - micro-chl-matches-Q46386
  - micro-chl-matches-O68986
  - micro-chl-matches-O68988
  - micro-chl-matches-O68983
  - micro-chl-matches-H2VFJ4
  - micro-chl-matches-H2VFJ1
  - micro-chl-matches-Q8KEN5
  - micro-chl-reviewed-csm-query
  - micro-chl-csmK-query
- assessment_id: micro-chlorosome_envelope-a3
  area: evidence
  topic: Constituents versus formation necessity
  outcome: concern
  summary: 'Inherited F1 remains confirmed: the ESSENTIAL baseplate annotation asserts
    target formation necessity beyond the cited experiments. Preserve positive structural
    integrity, antenna, attachment and viability roles. Frigaard2004 did not obtain
    segregated CsmA-loss mutants; Nielsen used bchK-mutant carotenosomes with a retained
    baseplate. Neither proves dispensability or universal failure of formation. Collective
    monolayer/pigment material is constitutional, not evidence that each molecular
    species is individually required.'
  target_ids:
  - GO:0033105
  evidence_ids:
  - micro-record-chlorosome_envelope
  - micro-schema-necessity
  - micro-chl-nielsen2016-jats
  - micro-frigaard2004
  - micro-chl-frigaard2005-meta
- assessment_id: micro-chlorosome_envelope-a4
  area: scope
  topic: Taxon examples and distribution
  outcome: supported
  summary: C. tepidum structural/genetic and C. aurantiacus J-10-fl imaging sources
    support the bounded examples. VARIABLE Bacteria and named phototrophic groups
    are secondary-context scope, not universal bacterial membership. Nielsen high-resolution
    preparation is mutant carotenosome; its wild-type comparisons and earlier AFM
    context are kept explicit.
  target_ids:
  - GO:0033105
  evidence_ids:
  - micro-record-chlorosome_envelope
  - micro-chl-tax-2
  - micro-chl-tax-1097
  - micro-chl-tax-1108
  - micro-chl-tax-194439
  - micro-chl-nielsen2016-jats
  - micro-frigaard2004
  - micro-psencik2009-retained-body
  - micro-chl-oostergetel2010-jats
  - micro-orf2013-browser
- assessment_id: micro-chlorosome_envelope-a5
  area: evidence
  topic: Light harvesting and component-localization roles
  outcome: supported
  summary: Pigment self-assembly, asymmetric envelope and baseplate energy transfer
    have authority/primary structural support. Secondary sources supply broader antenna
    context. Broad photosynthesis GO is not substituted for exact light harvesting,
    and heterogeneous accessory composition is not silently made universally essential.
  target_ids:
  - GO:0033105
  evidence_ids:
  - micro-record-chlorosome_envelope
  - micro-chl-go
  - micro-chl-nielsen2016-jats
  - micro-psencik2009-retained-body
  - micro-chl-oostergetel2010-jats
  - micro-orf2013-browser
  - micro-chl-li2006-meta
- assessment_id: micro-chlorosome_envelope-a6
  area: graph
  topic: 'Stale refresh: baseplate node identity'
  outcome: supported
  summary: Current csma_baseplate node is STRUCTURE and grounded to the frozen whole
    baseplate neighbor. This accurately denotes the assembled complex; the associated
    csmA example is not mistaken for the structure itself. This current-content assessment
    does not resolve an unfrozen multi-target category finding or all of closed issue2419.
  target_ids:
  - GO:0033105
  evidence_ids:
  - micro-record-chlorosome_envelope
  - micro-prior-chlorosome_envelope
  - micro-neighbor-baseplate
  - micro-chl-nielsen2016-jats
  - micro-graph-contract
  - micro-original-validation-inputs
- assessment_id: micro-chlorosome_envelope-a7
  area: graph
  topic: Six-edge NONMECHANISTIC envelope topology
  outcome: supported
  summary: Envelope parthood, boundary material, embedded accessory group, pigment
    enclosure, baseplate position and antenna support agree with authority/structural
    source scopes. No residue-level contact network or complete biogenesis pathway
    is claimed.
  target_ids:
  - GO:0033105
  evidence_ids:
  - micro-record-chlorosome_envelope
  - micro-chl-go
  - micro-chl-SL-0060
  - micro-chl-nielsen2016-jats
  - micro-chl-li2006-meta
  - micro-graph-contract
- assessment_id: micro-chlorosome_envelope-a8
  area: scope
  topic: Missing original structured-source applicability assessment
  outcome: concern
  summary: Original review omits applicability despite explicit Csm genes/accessions
    and light-harvesting pathway context. Current bounded catalogue contains no matching
    chlorosome-bearing organism dataset. Historical runner unavailable result and
    current fallback are separately dated; no unmatched bacterial gene query is substituted.
  target_ids:
  - GO:0033105
  evidence_ids:
  - micro-record-chlorosome_envelope
  - micro-prior-chlorosome_envelope
  - micro-review-policy
  - micro-review-config
  - micro-adapter-catalogue
  - micro-historical-adapter-runner
- assessment_id: micro-chlorosome_envelope-a9
  area: schema
  topic: Original provenance, current checks and native limits
  outcome: supported
  summary: Original pair validates and deterministically renders; frozen old blob
    is verified and current delta substantively reassessed. Six current slice protein
    receipts are actual exit0. Coverage labels retain gaps rather than upgrading them
    to experimental membership/necessity or automatic scientific defects.
  target_ids:
  - GO:0033105
  evidence_ids:
  - micro-record-chlorosome_envelope
  - micro-original-validation-inputs
  - micro-native-chlorosome_envelope-verify
  - micro-native-chlorosome_envelope-causal
- assessment_id: micro-chlorosome_envelope-a10
  area: provenance
  topic: Exact finding lineage and current verdict
  outcome: concern
  summary: Retain exact original F1 occurrence and stable issue key as open confirmed
    major; current verdict needs_curation. Stale review refresh is feasible within
    a review-only successor; scientific record edits remain separately proposed.
  target_ids:
  - GO:0033105
  evidence_ids:
  - micro-record-chlorosome_envelope
  - micro-prior-chlorosome_envelope
  - micro-schema-necessity
  - micro-frigaard2004
  - micro-chl-nielsen2016-jats
- assessment_id: micro-cis_golgi_network-a1
  area: identity
  topic: Network, membrane, stack and whole Golgi boundaries
  outcome: supported
  summary: GO:0005801 denotes a distinct ER-facing network, not a protein, lipid constituent
    or whole stack. Exact synonyms and Golgi-subcompartment/whole-Golgi relations
    are semantically appropriate; current authority comment distinguishes CGN from
    the stack. Neighbor context is restricted to frozen boundary fields.
  target_ids:
  - GO:0005801
  evidence_ids:
  - micro-record-cis_golgi_network
  - micro-cis-go
  - micro-neighbor-cgn-membrane
  - micro-neighbor-golgi
- assessment_id: micro-cis_golgi_network-a2
  area: scope
  topic: 'Inherited F1: experimental strain/current taxon'
  outcome: concern
  summary: Rossanese uses PPY1 and isogenic PPY12. ATCC strain designation/reidentification
    and ENA source qualifiers identify PPY12 as K. phaffii460519, while the record
    assigns both occurrence and canonical example to K. pastoris4922. Historical species
    naming is insufficient; F1 remains confirmed major.
  target_ids:
  - GO:0005801
  evidence_ids:
  - micro-record-cis_golgi_network
  - micro-cis-jats-PMC2148216
  - micro-cis-atcc-204163
  - micro-cis-ena-LC815816
  - micro-cis-tax-4922
  - micro-cis-tax-460519
- assessment_id: micro-cis_golgi_network-a3
  area: evidence
  topic: 'Inherited F2: experiment-to-compartment scope'
  outcome: concern
  summary: Rossanese establishes ordered Golgi stacks and adjacent tER, with Sec13-positive
    tubulovesicular interface assigned to tER. That is not direct identification of
    distinct GO:0005801 CGN. Species correction alone does not repair compartment-specific
    occurrence/example support; Cho abstract concerns S. cerevisiae Sed5-enriched
    early-Golgi membranes and does not fill this gap. No biological absence is claimed.
  target_ids:
  - GO:0005801
  evidence_ids:
  - micro-record-cis_golgi_network
  - micro-cis-go
  - micro-cis-jats-PMC2148216
  - micro-cis-cho2000-meta
- assessment_id: micro-cis_golgi_network-a4
  area: graph
  topic: 'Inherited F3: whole-network component link'
  outcome: concern
  summary: The complete network node grounded GO:0005801 points through component_ref
    to cis_golgi_network_lipid_bilayer. The schema reserves this link for the own
    constituent; a generic lipid material cannot identify the complete compartment.
    Remove the link or give the material its own node; retain minor severity and the
    otherwise correct topology.
  target_ids:
  - GO:0005801
  evidence_ids:
  - micro-record-cis_golgi_network
  - micro-schema-necessity
  - micro-cis-go
  - micro-neighbor-cgn-membrane
- assessment_id: micro-cis_golgi_network-a5
  area: completeness
  topic: Lipid material, excluded residents and necessity
  outcome: supported
  summary: Generic lipid bilayer is a legitimate collective boundary constituent,
    not a second whole-organelle grounding. Sed5/COPII markers are explicitly excluded
    as universal constitutive components; immunoisolation/localization does not establish
    formation necessity or a complete taxon-neutral protein inventory.
  target_ids:
  - GO:0005801
  evidence_ids:
  - micro-record-cis_golgi_network
  - micro-cis-go
  - micro-cis-cho2000-meta
  - micro-cis-jats-PMC2148216
  - micro-schema-necessity
- assessment_id: micro-cis_golgi_network-a6
  area: graph
  topic: Three topology edges and source limits
  outcome: supported
  summary: Membrane bounds network, network part of Golgi, and network abuts ER are
    supported by authority definitions. NONMECHANISTIC scope is appropriate; the broad
    topology does not validate the particular occurrence/canonical example.
  target_ids:
  - GO:0005801
  evidence_ids:
  - micro-record-cis_golgi_network
  - micro-cis-go
  - micro-graph-contract
- assessment_id: micro-cis_golgi_network-a7
  area: scope
  topic: Missing original structured-source applicability assessment
  outcome: concern
  summary: Although the resident inventory is lipid-only, the record explicitly evaluates
    named Sed5-positive membrane compartments and COPII evidence. Native molecular-claim
    trigger warrants applicability review. The fresh complete catalogue has no Komagataella/Pichia/Saccharomyces
    dataset; no matched-organism downstream query is justified. This is not a sparse
    membrane-only exclusion.
  target_ids:
  - GO:0005801
  evidence_ids:
  - micro-record-cis_golgi_network
  - micro-prior-cis_golgi_network
  - micro-review-policy
  - micro-review-config
  - micro-adapter-catalogue
  - micro-historical-adapter-runner
- assessment_id: micro-cis_golgi_network-a8
  area: schema
  topic: Unchanged input and zero-protein native coverage
  outcome: supported
  summary: Original frozen target remains byte-identical; original pair validates
    and renders. Current native protein verification exits0 with empty example inventory
    and zero protein nodes. This is structural coverage only and does not repair the
    independent graph component-ref semantics.
  target_ids:
  - GO:0005801
  evidence_ids:
  - micro-record-cis_golgi_network
  - micro-original-validation-inputs
  - micro-native-cis_golgi_network-verify
  - micro-native-cis_golgi_network-causal
- assessment_id: micro-cis_golgi_network-a9
  area: provenance
  topic: Exact three-finding lineage/current verdict
  outcome: concern
  summary: Preserve original20261021T110938Z-cis-golgi-network-audit F1/F2/F3, keys
    and major/major/minor severity. All remain open; current needs_curation does not
    authorize record edits, close neighbor issues or resolve a category-wide finding.
  target_ids:
  - GO:0005801
  evidence_ids:
  - micro-record-cis_golgi_network
  - micro-prior-cis_golgi_network
  - micro-cis-jats-PMC2148216
  - micro-cis-atcc-204163
  - micro-cis-go
- assessment_id: septin-chloroplast_membrane-schema
  area: schema
  topic: Native schema, deterministic rendering and original input integrity
  outcome: supported
  summary: Original bundle validates and renders exactly. Its current target hash
    equals the frozen input and original source revision. Native protein checks pass
    at empty-inventory scope; scientific claims are assessed separately.
  target_ids:
  - GO:0031969
  evidence_ids:
  - septin-record-chloroplast_membrane
  - septin-original-validation-chloroplast_membrane
  - septin-native-chloroplast_membrane-verify
  - septin-native-chloroplast_membrane-causal
- assessment_id: septin-chloroplast_membrane-images
  area: scope
  topic: Images and verbatim source snippets
  outcome: not_applicable
  summary: No maintained image or verbatim snippet is declared by this target. Source
    text and metadata inspection does not claim image-pixel, tomography-volume or
    raw-data reanalysis.
  target_ids:
  - GO:0031969
  evidence_ids:
  - septin-record-chloroplast_membrane
- assessment_id: septin-chloroplast_membrane-native-limits
  area: provenance
  topic: Empty protein inventories and historical checks
  outcome: supported
  summary: The two fresh native commands report zero errors and zero typed protein
    graph nodes. Named proteins or pathways in narrative text are not covered by this
    empty inventory. Historical bundle checks retain their dates and are not portrayed
    as current runs.
  target_ids:
  - GO:0031969
  evidence_ids:
  - septin-record-chloroplast_membrane
  - septin-original-chloroplast_membrane
  - septin-native-chloroplast_membrane-verify
  - septin-native-chloroplast_membrane-causal
- assessment_id: septin-chloroplast_outer_membrane-schema
  area: schema
  topic: Native schema, deterministic rendering and original input integrity
  outcome: supported
  summary: Original bundle validates and renders exactly. Its current target hash
    equals the frozen input and original source revision. Native protein checks pass
    at empty-inventory scope; scientific claims are assessed separately.
  target_ids:
  - GO:0009707
  evidence_ids:
  - septin-record-chloroplast_outer_membrane
  - septin-original-validation-chloroplast_outer_membrane
  - septin-native-chloroplast_outer_membrane-verify
  - septin-native-chloroplast_outer_membrane-causal
- assessment_id: septin-chloroplast_outer_membrane-images
  area: scope
  topic: Images and verbatim source snippets
  outcome: not_applicable
  summary: No maintained image or verbatim snippet is declared by this target. Source
    text and metadata inspection does not claim image-pixel, tomography-volume or
    raw-data reanalysis.
  target_ids:
  - GO:0009707
  evidence_ids:
  - septin-record-chloroplast_outer_membrane
- assessment_id: septin-chloroplast_outer_membrane-native-limits
  area: provenance
  topic: Empty protein inventories and historical checks
  outcome: supported
  summary: The two fresh native commands report zero errors and zero typed protein
    graph nodes. Named proteins or pathways in narrative text are not covered by this
    empty inventory. Historical bundle checks retain their dates and are not portrayed
    as current runs.
  target_ids:
  - GO:0009707
  evidence_ids:
  - septin-record-chloroplast_outer_membrane
  - septin-original-chloroplast_outer_membrane
  - septin-native-chloroplast_outer_membrane-verify
  - septin-native-chloroplast_outer_membrane-causal
- assessment_id: septin-chloroplast_stroma-schema
  area: schema
  topic: Native schema, deterministic rendering and original input integrity
  outcome: supported
  summary: Original bundle validates and renders exactly. Its current target hash
    equals the frozen input and original source revision. Native protein checks pass
    at empty-inventory scope; scientific claims are assessed separately.
  target_ids:
  - GO:0009570
  evidence_ids:
  - septin-record-chloroplast_stroma
  - septin-original-validation-chloroplast_stroma
  - septin-native-chloroplast_stroma-verify
  - septin-native-chloroplast_stroma-causal
- assessment_id: septin-chloroplast_stroma-images
  area: scope
  topic: Images and verbatim source snippets
  outcome: not_applicable
  summary: No maintained image or verbatim snippet is declared by this target. Source
    text and metadata inspection does not claim image-pixel, tomography-volume or
    raw-data reanalysis.
  target_ids:
  - GO:0009570
  evidence_ids:
  - septin-record-chloroplast_stroma
- assessment_id: septin-chloroplast_stroma-native-limits
  area: provenance
  topic: Empty protein inventories and historical checks
  outcome: supported
  summary: The two fresh native commands report zero errors and zero typed protein
    graph nodes. Named proteins or pathways in narrative text are not covered by this
    empty inventory. Historical bundle checks retain their dates and are not portrayed
    as current runs.
  target_ids:
  - GO:0009570
  evidence_ids:
  - septin-record-chloroplast_stroma
  - septin-original-chloroplast_stroma
  - septin-native-chloroplast_stroma-verify
  - septin-native-chloroplast_stroma-causal
- assessment_id: septin-ciliary_pocket_membrane-schema
  area: schema
  topic: Native schema, deterministic rendering and original input integrity
  outcome: supported
  summary: Original bundle validates and renders exactly. Its current target hash
    equals the frozen input and original source revision. Native protein checks pass
    at empty-inventory scope; scientific claims are assessed separately.
  target_ids:
  - GO:0020018
  evidence_ids:
  - septin-record-ciliary_pocket_membrane
  - septin-original-validation-ciliary_pocket_membrane
  - septin-native-ciliary_pocket_membrane-verify
  - septin-native-ciliary_pocket_membrane-causal
- assessment_id: septin-ciliary_pocket_membrane-images
  area: scope
  topic: Images and verbatim source snippets
  outcome: not_applicable
  summary: No maintained image or verbatim snippet is declared by this target. Source
    text and metadata inspection does not claim image-pixel, tomography-volume or
    raw-data reanalysis.
  target_ids:
  - GO:0020018
  evidence_ids:
  - septin-record-ciliary_pocket_membrane
- assessment_id: septin-ciliary_pocket_membrane-native-limits
  area: provenance
  topic: Empty protein inventories and historical checks
  outcome: supported
  summary: The two fresh native commands report zero errors and zero typed protein
    graph nodes. Named proteins or pathways in narrative text are not covered by this
    empty inventory. Historical bundle checks retain their dates and are not portrayed
    as current runs.
  target_ids:
  - GO:0020018
  evidence_ids:
  - septin-record-ciliary_pocket_membrane
  - septin-original-ciliary_pocket_membrane
  - septin-native-ciliary_pocket_membrane-verify
  - septin-native-ciliary_pocket_membrane-causal
- assessment_id: septin-chloroplast_membrane-adapter
  area: scope
  topic: Molecular/pathway scope and current organism coverage
  outcome: not_applicable
  summary: TOC–TIC/import claims (and HLP/nucleoid context for stroma) trigger an
    applicability assessment despite an empty typed protein inventory. The complete
    current catalogue lacks a matching green-algal organism/dataset, so downstream
    gene/module lookup does not apply. Historical runner unavailability is separate;
    no expression-only exemption or cyanobacterial substitute is used.
  target_ids:
  - GO:0031969
  evidence_ids:
  - septin-record-chloroplast_membrane
  - septin-review-policy
  - septin-current-adapter-catalogue
  - septin-historical-adapter-runner
- assessment_id: septin-chloroplast_membrane-taxa
  area: scope
  topic: Qualified green-lineage distribution and exact algal example
  outcome: supported
  summary: Native taxonomy identifies Viridiplantae and Chlamydomonas reinhardtii.
    Occurrence is qualified to chloroplast-bearing/photosynthetic members, not every
    tissue or nonphotosynthetic descendant. Keeling secondary body supports that context;
    Jin primary abstract directly names Chlamydomonas without establishing a universal
    experimental strain.
  target_ids:
  - GO:0031969
  evidence_ids:
  - septin-record-chloroplast_membrane
  - septin-root21-sources-NCBITaxon-33090
  - septin-root21-sources-NCBITaxon-3055
  - septin-root21-sources-keeling2010-pmc
  - septin-root21-sources-doi-10.1016_j.cell.2022.10.030
- assessment_id: septin-chloroplast_membrane-source-scope
  area: evidence
  topic: Import structure and actual access tiers
  outcome: supported
  summary: Jin primary abstract and author entry support the envelope-spanning assembly
    at Chlamydomonas scope. They do not provide a complete Methods/Results or raw
    structural audit. Keeling is secondary body context. Reused snapshots retain original09:33Z
    times; current review does not claim a fresh full paper fetch.
  target_ids:
  - GO:0031969
  evidence_ids:
  - septin-record-chloroplast_membrane
  - septin-root21-sources-doi-10.1016_j.cell.2022.10.030
  - septin-root21-sources-jin2022-author-publications
  - septin-root21-sources-keeling2010-pmc
- assessment_id: septin-chloroplast_membrane-necessity
  area: scope
  topic: Formation requirements beyond current representation
  outcome: unknown
  summary: Collective membrane material can be constitutional, while stroma is a spatial
    region without component essentiality assertions. None of these records establishes
    necessity of each lipid, import protein or stromal occupant for forming the whole
    structure. Localization and function do not substitute for formation assays.
  target_ids:
  - GO:0031969
  evidence_ids:
  - septin-record-chloroplast_membrane
  - septin-curation-policy
- assessment_id: septin-chloroplast_membrane-verdict
  area: consistency
  topic: Positive qualified verdict with explicit limitations
  outcome: supported
  summary: 'pass_with_limitations remains supported: exact structural identity, boundaries
    and scoped occurrence/import claims have positive authority/primary support. Unknown
    molecular formation requirements, incomplete optional inventories and stated source-access
    limits remain explicit. No original scientific finding or curation action exists
    for this target, and no new concrete record defect was established.'
  target_ids:
  - GO:0031969
  evidence_ids:
  - septin-record-chloroplast_membrane
  - septin-original-chloroplast_membrane
  - septin-root21-sources-doi-10.1016_j.cell.2022.10.030
  - septin-root22-sources-membrane-go
- assessment_id: septin-chloroplast_outer_membrane-adapter
  area: scope
  topic: Molecular/pathway scope and current organism coverage
  outcome: not_applicable
  summary: TOC–TIC/import claims (and HLP/nucleoid context for stroma) trigger an
    applicability assessment despite an empty typed protein inventory. The complete
    current catalogue lacks a matching green-algal organism/dataset, so downstream
    gene/module lookup does not apply. Historical runner unavailability is separate;
    no expression-only exemption or cyanobacterial substitute is used.
  target_ids:
  - GO:0009707
  evidence_ids:
  - septin-record-chloroplast_outer_membrane
  - septin-review-policy
  - septin-current-adapter-catalogue
  - septin-historical-adapter-runner
- assessment_id: septin-chloroplast_outer_membrane-taxa
  area: scope
  topic: Qualified green-lineage distribution and exact algal example
  outcome: supported
  summary: Native taxonomy identifies Viridiplantae and Chlamydomonas reinhardtii.
    Occurrence is qualified to chloroplast-bearing/photosynthetic members, not every
    tissue or nonphotosynthetic descendant. Keeling secondary body supports that context;
    Jin primary abstract directly names Chlamydomonas without establishing a universal
    experimental strain.
  target_ids:
  - GO:0009707
  evidence_ids:
  - septin-record-chloroplast_outer_membrane
  - septin-root21-sources-NCBITaxon-33090
  - septin-root21-sources-NCBITaxon-3055
  - septin-root21-sources-keeling2010-pmc
  - septin-root21-sources-doi-10.1016_j.cell.2022.10.030
- assessment_id: septin-chloroplast_outer_membrane-source-scope
  area: evidence
  topic: Import structure and actual access tiers
  outcome: supported
  summary: Jin primary abstract and author entry support the envelope-spanning assembly
    at Chlamydomonas scope. They do not provide a complete Methods/Results or raw
    structural audit. Keeling is secondary body context. Reused snapshots retain original09:33Z
    times; current review does not claim a fresh full paper fetch.
  target_ids:
  - GO:0009707
  evidence_ids:
  - septin-record-chloroplast_outer_membrane
  - septin-root21-sources-doi-10.1016_j.cell.2022.10.030
  - septin-root21-sources-jin2022-author-publications
  - septin-root21-sources-keeling2010-pmc
- assessment_id: septin-chloroplast_outer_membrane-necessity
  area: scope
  topic: Formation requirements beyond current representation
  outcome: unknown
  summary: Collective membrane material can be constitutional, while stroma is a spatial
    region without component essentiality assertions. None of these records establishes
    necessity of each lipid, import protein or stromal occupant for forming the whole
    structure. Localization and function do not substitute for formation assays.
  target_ids:
  - GO:0009707
  evidence_ids:
  - septin-record-chloroplast_outer_membrane
  - septin-curation-policy
- assessment_id: septin-chloroplast_outer_membrane-verdict
  area: consistency
  topic: Positive qualified verdict with explicit limitations
  outcome: supported
  summary: 'pass_with_limitations remains supported: exact structural identity, boundaries
    and scoped occurrence/import claims have positive authority/primary support. Unknown
    molecular formation requirements, incomplete optional inventories and stated source-access
    limits remain explicit. No original scientific finding or curation action exists
    for this target, and no new concrete record defect was established.'
  target_ids:
  - GO:0009707
  evidence_ids:
  - septin-record-chloroplast_outer_membrane
  - septin-original-chloroplast_outer_membrane
  - septin-root21-sources-doi-10.1016_j.cell.2022.10.030
  - septin-root22-sources-outer-go
- assessment_id: septin-chloroplast_stroma-adapter
  area: scope
  topic: Molecular/pathway scope and current organism coverage
  outcome: not_applicable
  summary: TOC–TIC/import claims (and HLP/nucleoid context for stroma) trigger an
    applicability assessment despite an empty typed protein inventory. The complete
    current catalogue lacks a matching green-algal organism/dataset, so downstream
    gene/module lookup does not apply. Historical runner unavailability is separate;
    no expression-only exemption or cyanobacterial substitute is used.
  target_ids:
  - GO:0009570
  evidence_ids:
  - septin-record-chloroplast_stroma
  - septin-review-policy
  - septin-current-adapter-catalogue
  - septin-historical-adapter-runner
- assessment_id: septin-chloroplast_stroma-taxa
  area: scope
  topic: Qualified green-lineage distribution and exact algal example
  outcome: supported
  summary: Native taxonomy identifies Viridiplantae and Chlamydomonas reinhardtii.
    Occurrence is qualified to chloroplast-bearing/photosynthetic members, not every
    tissue or nonphotosynthetic descendant. Keeling secondary body supports that context;
    Jin primary abstract directly names Chlamydomonas without establishing a universal
    experimental strain.
  target_ids:
  - GO:0009570
  evidence_ids:
  - septin-record-chloroplast_stroma
  - septin-root21-sources-NCBITaxon-33090
  - septin-root21-sources-NCBITaxon-3055
  - septin-root21-sources-keeling2010-pmc
  - septin-root21-sources-doi-10.1016_j.cell.2022.10.030
- assessment_id: septin-chloroplast_stroma-source-scope
  area: evidence
  topic: Import structure and actual access tiers
  outcome: supported
  summary: Jin primary abstract and author entry support the envelope-spanning assembly
    at Chlamydomonas scope. They do not provide a complete Methods/Results or raw
    structural audit. Keeling is secondary body context. Reused snapshots retain original09:33Z
    times; current review does not claim a fresh full paper fetch.
  target_ids:
  - GO:0009570
  evidence_ids:
  - septin-record-chloroplast_stroma
  - septin-root21-sources-doi-10.1016_j.cell.2022.10.030
  - septin-root21-sources-jin2022-author-publications
  - septin-root21-sources-keeling2010-pmc
- assessment_id: septin-chloroplast_stroma-necessity
  area: scope
  topic: Formation requirements beyond current representation
  outcome: unknown
  summary: Collective membrane material can be constitutional, while stroma is a spatial
    region without component essentiality assertions. None of these records establishes
    necessity of each lipid, import protein or stromal occupant for forming the whole
    structure. Localization and function do not substitute for formation assays.
  target_ids:
  - GO:0009570
  evidence_ids:
  - septin-record-chloroplast_stroma
  - septin-curation-policy
- assessment_id: septin-chloroplast_stroma-verdict
  area: consistency
  topic: Positive qualified verdict with explicit limitations
  outcome: supported
  summary: 'pass_with_limitations remains supported: exact structural identity, boundaries
    and scoped occurrence/import claims have positive authority/primary support. Unknown
    molecular formation requirements, incomplete optional inventories and stated source-access
    limits remain explicit. No original scientific finding or curation action exists
    for this target, and no new concrete record defect was established.'
  target_ids:
  - GO:0009570
  evidence_ids:
  - septin-record-chloroplast_stroma
  - septin-original-chloroplast_stroma
  - septin-root21-sources-doi-10.1016_j.cell.2022.10.030
  - septin-root22-sources-stroma-go
- assessment_id: septin-chloroplast_membrane-identity
  area: identity
  topic: Generic chloroplast envelope membrane class
  outcome: supported
  summary: Current GO defines either envelope bilayer, with plastid membrane as is-a
    parent and envelope as whole. The inner/outer membranes are explicit is-a children.
    Internal thylakoid membrane is distinct; broader UniProt umbrella wording is not
    used to expand this GO identity.
  target_ids:
  - GO:0031969
  evidence_ids:
  - septin-record-chloroplast_membrane
  - septin-root22-sources-membrane-go
  - septin-context-chloroplast
  - septin-context-chloroplast_envelope
  - septin-context-chloroplast_inner_membrane
- assessment_id: septin-chloroplast_membrane-material
  area: grounding
  topic: Collective lipid constituent rather than chemical species
  outcome: supported
  summary: The reviewed-label-only row represents generic envelope-bilayer material,
    not the whole location as a chemical grounding. ESSENTIAL is constitutional at
    collective bilayer scale; no exact lipid species or molecular assembly factor
    is declared essential. The open grounding TODO is uncertainty, not evidence that
    no suitable term exists.
  target_ids:
  - GO:0031969
  evidence_ids:
  - septin-record-chloroplast_membrane
  - septin-root22-sources-membrane-go
  - septin-curation-policy
- assessment_id: septin-chloroplast_membrane-graph
  area: graph
  topic: Three nonmechanistic identity/parthood edges
  outcome: supported
  summary: All three edges retain membrane part_of envelope and inner/outer is_a generic
    membrane. Exact GO typed children and definitions support these relations without
    importing thylakoids, translocase subunits or a mechanism.
  target_ids:
  - GO:0031969
  evidence_ids:
  - septin-record-chloroplast_membrane
  - septin-root22-sources-membrane-go
  - septin-graph-policy
- assessment_id: septin-chloroplast_outer_membrane-identity
  area: identity
  topic: Exact outer-membrane orientation and dual parentage
  outcome: supported
  summary: GO0009707 and SL0054 agree on the cytoplasm-facing outer bilayer and exact
    location mapping. Both plastid outer membrane and chloroplast membrane parents
    are supported; the whole envelope and intermembrane space remain distinct.
  target_ids:
  - GO:0009707
  evidence_ids:
  - septin-record-chloroplast_outer_membrane
  - septin-root22-sources-outer-go
  - septin-root22-sources-SL-0054-json
  - septin-context-chloroplast_envelope
  - septin-context-chloroplast_intermembrane_space
- assessment_id: septin-chloroplast_outer_membrane-material
  area: grounding
  topic: Constitutional outer lipid bilayer
  outcome: supported
  summary: The generic lipid constituent is label-only and constitutionally essential
    at collective bilayer level. Whole-location identifiers are not claimed to identify
    a lipid species; no imported membrane protein inventory or individual necessity
    claim is implied.
  target_ids:
  - GO:0009707
  evidence_ids:
  - septin-record-chloroplast_outer_membrane
  - septin-root22-sources-outer-go
  - septin-root22-sources-SL-0054-json
  - septin-curation-policy
- assessment_id: septin-chloroplast_outer_membrane-graph
  area: graph
  topic: Three descriptive spatial relations
  outcome: supported
  summary: All three edges place the outer membrane in the envelope, facing cytoplasm
    and bounding intermembrane space. GO definitions support these directly; SL0054
    parent hierarchy corroborates context without inventing a direct top-level partOf
    field.
  target_ids:
  - GO:0009707
  evidence_ids:
  - septin-record-chloroplast_outer_membrane
  - septin-root22-sources-outer-go
  - septin-root22-sources-SL-0054-json
  - septin-context-chloroplast_intermembrane_space
  - septin-graph-policy
- assessment_id: septin-chloroplast_stroma-identity
  area: identity
  topic: Matrix compartment excluding thylakoid lumen
  outcome: supported
  summary: GO0009570 and SL0055 identify the stroma, plastid-stroma parent and chloroplast
    parthood. The explicit lumen exclusion is retained. A spatial region does not
    require an invariant list of every molecule residing in it.
  target_ids:
  - GO:0009570
  evidence_ids:
  - septin-record-chloroplast_stroma
  - septin-root22-sources-stroma-go
  - septin-root22-sources-SL-0055-json
  - septin-context-chloroplast
  - septin-context-chloroplast_inner_membrane
- assessment_id: septin-chloroplast_stroma-parts
  area: grounding
  topic: Nucleoids and plastoglobules within stromal scope
  outcome: supported
  summary: GO directly lists nucleoid and plastoglobule part_of children of stroma.
    SL0217 places plastoglobules in stroma in its definition, while direct partOf
    is chloroplast. Association with thylakoids does not move them into the thylakoid
    lumen.
  target_ids:
  - GO:0009570
  evidence_ids:
  - septin-record-chloroplast_stroma
  - septin-root22-sources-stroma-go
  - septin-root22-sources-SL-0217-json
- assessment_id: septin-chloroplast_stroma-nucleoid
  area: evidence
  topic: Primary nucleoid evidence versus secondary proteome context
  outcome: supported
  summary: The complete Karcher primary abstract supports Chlamydomonas HLP chloroplast
    targeting and nucleoid association, with RNAi organization/genome effects. Terashima
    secondary abstract supplies comparative metabolic/protein-biogenesis context;
    whole-chloroplast surveys are not treated as pure stromal inventories. Direct
    nucleoid evidence is separately cited on the maintained graph edge.
  target_ids:
  - GO:0009570
  evidence_ids:
  - septin-record-chloroplast_stroma
  - septin-root22-sources-doi-10.1093_mp_ssp083
  - septin-root21-sources-doi-10.1007_s00294-011-0339-1
  - septin-root21-sources-terashima2011-pdf
- assessment_id: septin-chloroplast_stroma-function-graph
  area: graph
  topic: Four boundary, parthood and import-destination edges
  outcome: supported
  summary: Envelope encloses stroma; nucleoid and plastoglobule occupy it; the biological
    process protein import terminates in stroma. The destination compartment is not
    made the transporting actor. NONMECHANISTIC scope excludes complete import, lipid-remodeling
    and nucleoid-maintenance mechanisms.
  target_ids:
  - GO:0009570
  evidence_ids:
  - septin-record-chloroplast_stroma
  - septin-root22-sources-stroma-go
  - septin-root22-sources-SL-0217-json
  - septin-root22-sources-doi-10.1093_mp_ssp083
  - septin-root21-sources-doi-10.1016_j.cell.2022.10.030
  - septin-graph-policy
- assessment_id: septin-ciliary_pocket_membrane-adapter
  area: scope
  topic: Sparse material/topology molecular-query exclusion
  outcome: not_applicable
  summary: The maintained pocket-membrane record asserts a collective lipid domain,
    boundaries and qualitative species occurrence. It names no resident protein, gene,
    regulator, exact lipid species or molecular pathway needing a matched query. The
    missing original adapter row is not a bundle defect. Independently inspected catalogue
    also has no T. brucei dataset; no biological absence follows.
  target_ids:
  - GO:0020018
  evidence_ids:
  - septin-record-ciliary_pocket_membrane
  - septin-review-policy
  - septin-current-adapter-catalogue
- assessment_id: septin-ciliary_pocket_membrane-identity
  area: identity
  topic: Exact membrane domain, synonyms and whole-pocket boundary
  outcome: supported
  summary: GO0020018 supports the membrane domain and three exact synonyms; ciliary
    membrane is the is-a parent and whole pocket the containing structure. The frozen
    collar and whole-pocket neighbors remain distinct identities.
  target_ids:
  - GO:0020018
  evidence_ids:
  - septin-record-ciliary_pocket_membrane
  - septin-pocket-membrane-agent-go
  - septin-context-flagellar_pocket
  - septin-context-ciliary_pocket_collar
- assessment_id: septin-ciliary_pocket_membrane-material
  area: grounding
  topic: Collective bilayer with unresolved molecular inventory
  outcome: supported
  summary: The label-only material row does not substitute the whole membrane location
    for an individual lipid. ESSENTIAL is constitutional for the collective bilayer.
    The inventory TODO does not justify importing every associated trafficking protein
    or cytoskeletal collar factor as a resident constituent.
  target_ids:
  - GO:0020018
  evidence_ids:
  - septin-record-ciliary_pocket_membrane
  - septin-pocket-membrane-agent-go
  - septin-curation-policy
- assessment_id: septin-ciliary_pocket_membrane-necessity
  area: scope
  topic: Individual formation dependencies
  outcome: unknown
  summary: No individual lipid or protein is shown necessary for formation of this
    complete membrane domain. The collective material identity does not supply such
    an experiment, and this review does not propose an exhaustive composition.
  target_ids:
  - GO:0020018
  evidence_ids:
  - septin-record-ciliary_pocket_membrane
  - septin-curation-policy
- assessment_id: septin-ciliary_pocket_membrane-taxa
  area: scope
  topic: T. brucei species and bounded experiment scope
  outcome: supported
  summary: Native taxonomy verifies the species. Exact primary abstracts support the
    qualitative example. Lacomble indexed Cell culture specifies procyclic T. brucei
    brucei strain427; that strain is not transferred to Gadelha or all life stages.
    COMMON is qualitative, not a measured population prevalence.
  target_ids:
  - GO:0020018
  evidence_ids:
  - septin-record-ciliary_pocket_membrane
  - septin-pocket-membrane-agent-tax-5691
  - septin-pocket-membrane-agent-doi-10.1073_pnas.0909289106
  - septin-pocket-membrane-agent-doi-10.1242_jcs.045740
  - septin-lacomble-indexed-methods
- assessment_id: septin-ciliary_pocket_membrane-boundary-evidence
  area: evidence
  topic: Direct membrane-domain evidence and secondary context
  outcome: supported
  summary: Gadelha primary abstract and indexed Discussion support distinct continuous
    membrane domains and their relationship to cytoskeletal boundaries. Field/Carrington
    secondary abstract supports the pocket as a membrane invagination. The maintained
    boundary function does not assert a universal filter/channel mechanism.
  target_ids:
  - GO:0020018
  evidence_ids:
  - septin-record-ciliary_pocket_membrane
  - septin-pocket-membrane-agent-doi-10.1073_pnas.0909289106
  - septin-gadelha-indexed-body
  - septin-pocket-membrane-agent-doi-10.1038_nrmicro2221
- assessment_id: septin-ciliary_pocket_membrane-graph
  area: graph
  topic: Two nonmechanistic constitution/topology edges
  outcome: supported
  summary: The contributes-to and bounds edges distinguish lipid material, complete
    membrane domain and whole pocket. They express constitution/topology, not molecular
    causation or the complete associated cytoskeleton.
  target_ids:
  - GO:0020018
  evidence_ids:
  - septin-record-ciliary_pocket_membrane
  - septin-pocket-membrane-agent-go
  - septin-graph-policy
- assessment_id: septin-ciliary_pocket_membrane-provenance
  area: provenance
  topic: Current abstract/indexed-body tiers differ from historical direct bodies
  outcome: supported
  summary: Current direct PMC routes supplied challenge pages; indexed primary Discussion/Methods
    excerpts and exact native abstracts were read instead. Field/Halliday current
    access is native review abstracts; publisher challenge/stub responses are not
    full papers. Original wider body-reading claims remain historical and are not
    copied as current observations.
  target_ids:
  - GO:0020018
  evidence_ids:
  - septin-original-ciliary_pocket_membrane
  - septin-access-source-receipts
  - septin-access-extra-receipts
  - septin-gadelha-indexed-body
  - septin-lacomble-indexed-methods
  - septin-pocket-membrane-agent-doi-10.1016_j.pt.2020.11.005
- assessment_id: septin-ciliary_pocket_membrane-verdict
  area: consistency
  topic: Positive qualified boundary review
  outcome: supported
  summary: pass_with_limitations remains supported for exact membrane identity, species
    example, collective material and boundary graph. Unresolved molecular inventory,
    unknown individual formation dependencies and current source-access tiers remain
    explicit. No original or new scientific correction is established.
  target_ids:
  - GO:0020018
  evidence_ids:
  - septin-record-ciliary_pocket_membrane
  - septin-original-ciliary_pocket_membrane
  - septin-pocket-membrane-agent-go
  - septin-pocket-membrane-agent-doi-10.1073_pnas.0909289106
  - septin-gadelha-indexed-body
- assessment_id: current-input-comparison
  area: provenance
  topic: Complete frozen-input comparison and bounded refresh
  outcome: supported
  summary: 3 of ten original target hashes differ from current main. The changed content
    is substantively reassessed in the target-specific assessments; original observations
    remain historical and unchanged. All current target and used context bytes are
    frozen.
  target_ids:
  - GO:0031969
  - GO:0009707
  - GO:0009570
  - GO:0009534
  - GO:0009543
  - GO:0009535
  - GO:0046858
  - GO:0033105
  - GO:0020018
  - GO:0005801
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
  issue_key: chlorosome-baseplate-assembly-necessity
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Separate CsmA baseplate function and viability from formation necessity
  description: The CsmA-baseplate component is marked ESSENTIAL, which the schema
    defines in terms of whether the target structure forms without it. Nielsen2016
    resolves a baseplate in bchK-mutant carotenosomes and compares wild-type/mutant
    structure; it does not remove the baseplate to test formation. Frigaard2004 reports
    failure of csmA transformants to segregate under its growth conditions and interprets
    possible essential light harvesting/viability, while the nine non-CsmA deletions
    retain chlorosomes. These results cannot by themselves assign an unqualified formation
    requirement to the baseplate across this bacterial structure class. Preserve the
    well-supported constituent and antenna roles, but qualify or withhold the assembly-necessity
    assertion unless a direct, appropriately scoped formation result is supplied.
    This finding does not say the baseplate is dispensable or treat vestigial pigment-free
    remnants as normal chlorosomes. Nielsen2016 explicitly assigns structural integrity
    as a baseplate function in its Introduction; retain this positive structural role
    while separating it from a tested universal requirement for formation.
  target_ids:
  - GO:0046858
  field_paths:
  - components[1].essentiality
  evidence_ids:
  - micro-record-chlorosome
  - micro-schema-necessity
  - micro-review-policy
  - micro-chl-nielsen2016-jats
  - micro-frigaard2004
  - micro-chl-frigaard2005-meta
  normalization_reason: 'Major unsupported scientific essentiality claim: a positive
    structure-formation requirement is represented using evidence of structure, antenna
    function and cell viability with different experimental endpoints.'
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/chlorosome.yaml
    role: maintained scientific record
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T110934Z-chlorosome-audit
    finding_id: F1
  native_severity: major
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2659
- finding_id: micro-F2
  issue_key: chlorosome_envelope-baseplate-assembly-necessity
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Separate CsmA baseplate function and viability from formation necessity
  description: The CsmA-baseplate component is marked ESSENTIAL, which the schema
    defines in terms of whether the target structure forms without it. Nielsen2016
    resolves a baseplate in bchK-mutant carotenosomes and compares wild-type/mutant
    structure; it does not remove the baseplate to test formation. Frigaard2004 reports
    failure of csmA transformants to segregate under its growth conditions and interprets
    possible essential light harvesting/viability, while the nine non-CsmA deletions
    retain chlorosomes. These results cannot by themselves assign an unqualified formation
    requirement to the baseplate across this bacterial structure class. Preserve the
    well-supported constituent and antenna roles, but qualify or withhold the assembly-necessity
    assertion unless a direct, appropriately scoped formation result is supplied.
    This finding does not say the baseplate is dispensable or treat vestigial pigment-free
    remnants as normal chlorosomes. Nielsen2016 explicitly assigns structural integrity
    as a baseplate function in its Introduction; retain this positive structural role
    while separating it from a tested universal requirement for formation.
  target_ids:
  - GO:0033105
  field_paths:
  - components[1].essentiality
  evidence_ids:
  - micro-record-chlorosome_envelope
  - micro-schema-necessity
  - micro-review-policy
  - micro-chl-nielsen2016-jats
  - micro-frigaard2004
  - micro-chl-frigaard2005-meta
  normalization_reason: 'Major unsupported scientific essentiality claim: a positive
    structure-formation requirement is represented using evidence of structure, antenna
    function and cell viability with different experimental endpoints.'
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/chlorosome_envelope.yaml
    role: maintained scientific record
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T110935Z-chlorosome-envelope-audit
    finding_id: F1
  native_severity: major
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2660
- finding_id: micro-F3
  issue_key: cis-golgi-network-ppy12-current-taxon
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: The cited PPY1/PPY12 study is assigned to the wrong current species
  description: Rossanese1999 used PPY1 and its isogenic PPY12 derivatives. ATCC explicitly
    identifies PPY12 as K. phaffii following sequence-based reidentification, independently
    corroborated by ENA LC815816.1 taxon460519. The maintained taxonomic_distribution
    and canonical_examples instead assign the experiment to K. pastoris4922. The historical
    Pichia pastoris name alone does not justify that current assignment.
  target_ids:
  - GO:0005801
  field_paths:
  - taxonomic_distribution[0].taxon_id
  - taxonomic_distribution[0].taxon_label
  - canonical_examples[0].taxon_id
  - canonical_examples[0].taxon_label
  evidence_ids:
  - micro-record-cis_golgi_network
  - micro-cis-jats-PMC2148216
  - micro-cis-atcc-204163
  - micro-cis-ena-LC815816
  - micro-cis-tax-4922
  - micro-cis-tax-460519
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/cis_golgi_network.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: major
  normalization_reason: Major because experimental species scope and the canonical
    example are materially misattributed, while the generic structure identity remains
    valid.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T110938Z-cis-golgi-network-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2661
- finding_id: micro-F4
  issue_key: cis-golgi-network-stack-study-evidence-scope
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: The cited stack study does not directly establish this CGN occurrence and
    example
  description: The occurrence and canonical-example slots belong to GO0005801, but
    their sole cited study directly resolves Golgi stacks and adjacent transitional
    ER. Native GO distinguishes CGN from the Golgi stack, and the source assigns its
    observed Sec13-positive tubulovesicular interface to tER. Neither early/late Golgi
    marker apposition nor ordered stacks alone demonstrates a distinct CGN. Correcting
    the species leaves this unsupported compartment-specific attribution intact.
  target_ids:
  - GO:0005801
  field_paths:
  - taxonomic_distribution[0]
  - canonical_examples[0]
  evidence_ids:
  - micro-record-cis_golgi_network
  - micro-cis-go
  - micro-cis-jats-PMC2148216
  - micro-cis-cho2000-meta
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/cis_golgi_network.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: major
  normalization_reason: Major because the only asserted species occurrence and canonical
    example overextend the cited observations to a different compartment scope; the
    ontology identity and generic topology remain supported.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T110938Z-cis-golgi-network-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2662
- finding_id: micro-F5
  issue_key: cis-golgi-network-node-lipid-component-link
  category: graph
  severity: minor
  status: open
  certainty: confirmed
  title: The whole-network graph node links to a lipid-material component
  description: The graph node grounded to GO0005801 denotes the complete membrane-bounded
    network, but its component_ref names cis_golgi_network_lipid_bilayer. The schema
    uses component_ref when the node is an own component; native GO separately identifies
    the complete network and its surrounding membrane. The link therefore collapses
    the compartment into its lipid constituent even though the graph otherwise keeps
    membrane and network nodes separate.
  target_ids:
  - GO:0005801
  field_paths:
  - causal_graphs#cis_golgi_network_entry_topology.nodes#cis_golgi_network.component_ref
  evidence_ids:
  - micro-record-cis_golgi_network
  - micro-schema-necessity
  - micro-cis-go
  - micro-neighbor-cgn-membrane
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/cis_golgi_network.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: minor
  normalization_reason: Minor because the graph identities and topology are otherwise
    valid; one local cross-link misrepresents material-versus-whole scope.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T110938Z-cis-golgi-network-audit
    finding_id: F3
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2663
actions:
- action_id: micro-A1
  description: Revise the CsmA-baseplate formation-necessity annotation or attach
    direct source evidence at the relevant taxon and experimental scope.
  finding_ids:
  - micro-F1
  target_ids:
  - GO:0046858
  acceptance_checks:
  - Keep the supported baseplate constituent identity, structural-integrity role and
    light-harvesting role.
  - Use UNKNOWN or an appropriately qualified necessity state unless inspected evidence
    tests target formation after the relevant component loss.
  - Do not substitute failed mutant segregation, viability or excitation-transfer
    loss for an assembly endpoint; retain the modified-carotenosome versus normal-chlorosome
    boundary.
  - Apply any scientific edit only in a separately authorized guarded-writer curation
    PR with event/history and native validation; this review-only PR leaves the record
    unchanged.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/chlorosome.yaml
    role: maintained scientific record
- action_id: micro-A2
  description: Revise the CsmA-baseplate formation-necessity annotation or attach
    direct source evidence at the relevant taxon and experimental scope.
  finding_ids:
  - micro-F2
  target_ids:
  - GO:0033105
  acceptance_checks:
  - Keep the supported baseplate constituent identity, structural-integrity role and
    light-harvesting role.
  - Use UNKNOWN or an appropriately qualified necessity state unless inspected evidence
    tests target formation after the relevant component loss.
  - Do not substitute failed mutant segregation, viability or excitation-transfer
    loss for an assembly endpoint; retain the modified-carotenosome versus normal-chlorosome
    boundary.
  - Apply any scientific edit only in a separately authorized guarded-writer curation
    PR with event/history and native validation; this review-only PR leaves the record
    unchanged.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/chlorosome_envelope.yaml
    role: maintained scientific record
- action_id: micro-A3
  finding_ids:
  - micro-F3
  target_ids:
  - GO:0005801
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/cis_golgi_network.yaml
    role: maintained scientific record
  description: Correct any retained PPY1/PPY12-based example and occurrence attribution
    to K. phaffii460519 with a documented strain bridge; retain the historical source
    name in notes. Address the separate CGN-specific evidence finding before retaining
    this as a confirmed CGN example.
  acceptance_checks:
  - Any retained Rossanese example uses the experimentally verified current taxon
    and preserves the historical name.
  - The species correction is not treated as proof of a CGN distinct from Golgi stacks.
  - Focused native validators pass.
  - Apply any scientific edit only in a separately authorized guarded-writer curation
    PR with event/history and native validation; this review-only PR leaves the record
    unchanged.
- action_id: micro-A4
  finding_ids:
  - micro-F4
  target_ids:
  - GO:0005801
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/cis_golgi_network.yaml
    role: maintained scientific record
  description: Supply direct evidence identifying the CGN in the asserted organism,
    or remove/defer the CGN-specific occurrence/example while retaining Rossanese
    as explicitly broader Golgi-stack/tER context. Do not replace the CGN identity
    with a whole-stack term or infer absence of CGN from this evidence gap.
  acceptance_checks:
  - Retained occurrence/example evidence distinguishes CGN from whole Golgi stacks
    and transitional ER.
  - The canonical example does not depend solely on whole-stack morphology or early-Golgi
    marker localization.
  - The independent current-species error is resolved for any retained experimental
    attribution.
  - Focused native validators pass.
  - Apply any scientific edit only in a separately authorized guarded-writer curation
    PR with event/history and native validation; this review-only PR leaves the record
    unchanged.
- action_id: micro-A5
  finding_ids:
  - micro-F5
  target_ids:
  - GO:0005801
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/cis_golgi_network.yaml
    role: maintained scientific record
  description: Remove the lipid component_ref from the whole-CGN node, or add a separate
    lipid-material node carrying that component_ref and an appropriate constituent
    relationship. Keep GO0005801 on the complete network and GO0033106 on its membrane.
  acceptance_checks:
  - No whole-CGN node is locally identified as the lipid-bilayer component.
  - Any added material node preserves membrane-versus-compartment scope.
  - Focused native validators pass.
  - Apply any scientific edit only in a separately authorized guarded-writer curation
    PR with event/history and native validation; this review-only PR leaves the record
    unchanged.
limitations:
- 'Chloroplast thylakoid, lumen and membrane independent subreview: Engel2015 is inspected
  primary JATS at the named Introduction/Results/Discussion/Methods sections; captions
  are text, not independent image-pixel or raw-tomogram analysis. CC-124/137c, TAP
  and constant light remain explicit. Limited tomogram volumes do not establish one
  globally continuous lumen or universal biogenesis routes.'
- 'Chloroplast thylakoid, lumen and membrane independent subreview: Terashima2011
  fresh source is an actual readable PDF, with printedpp151–156 Introduction/Photosynthesis
  text inspected. It is secondary synthesis; full supplementary proteomes, every cited
  primary experiment and later metabolic sections are outside this audit. The benign
  pdftotext hint-table warning did not prevent readable extraction.'
- 'Chloroplast thylakoid, lumen and membrane independent subreview: Perez2024 uses
  independently reread cached official-publisher browser body packets from09:34:09Z
  and09:37:31Z. Actual original capture times and hashes are retained. The new native
  request returned403; no new browser retrieval or complete native body is claimed.'
- 'Chloroplast thylakoid, lumen and membrane independent subreview: Keeling2010 selected
  fresh secondary PMC body was inspected; the failed EuropePMC JATS response remains
  separately disclosed. Broad plastid occurrence does not establish thylakoids in
  every nonphotosynthetic lineage.'
- 'Chloroplast thylakoid, lumen and membrane independent subreview: The ontology comment
  supports the maintained OTHER interpretation for whole thylakoid; no wholesale reconciliation
  of GO’s inherited organelle classification is claimed. Exact membrane/lumen parts
  and green-lineage scope are independently checked.'
- 'Chloroplast thylakoid, lumen and membrane independent subreview: Constitutional
  membrane material is distinct from necessary individual lipids, pigments or proteins.
  These targets intentionally contain no exact protein-example or family assertions,
  and no unsupported inventory is required.'
- 'Chloroplast thylakoid, lumen and membrane independent subreview: Current catalogue
  has no matched chloroplast host. S.elongatus photosynthetic dataset coverage is
  not Chlamydomonas coverage. The actual historical runner failed00:49Z; no fresh
  invocation or successful runner execution is claimed.'
- 'Chloroplast thylakoid, lumen and membrane independent subreview: Historical735/736/other
  curation numbers are read only as record history. No exact predecessor finding is
  newly resolved, rejected or superseded by this partial cohort.'
- 'Chloroplast thylakoid, lumen and membrane independent subreview: All three targets
  declare no images or numerical measurements; no target pixel inspection is claimed.
  Shared mutual targets provide all needed boundary context. Root owns global QC,
  issue deduplication/publication and repository/GitHub mutations.'
- 'Chlorosome, envelope and cis-Golgi network independent subreview: Assigned scope
  is exactly chlorosome, chlorosome envelope and cis-Golgi network. Three frozen neighbors
  were consulted only at declared boundary fields; no whole-category review or terminal
  disposition of closed grouped issue2419 is claimed.'
- 'Chlorosome, envelope and cis-Golgi network independent subreview: Nielsen2016 genuine
  current JATS was read at complete Introduction/Results/Discussion plus Sample preparation
  Methods. Its structure is bchK-mutant carotenosome baseplate with wild-type comparisons;
  AFM dimensions refer to earlier work. No NMR/raw microscopy pixels, supplements
  or full computational pipeline audit.'
- 'Chlorosome, envelope and cis-Golgi network independent subreview: Frigaard2004
  current institutional PDF was read as text at declared Methods/Results/Discussion
  scope. Native PMC challenge and guessed JATS404 are retained failures, not article
  bodies. CsmA nonsegregation tests viability/light harvesting under its conditions,
  not a direct universal assembly endpoint.'
- 'Chlorosome, envelope and cis-Golgi network independent subreview: Psencik2009 genuine
  PMC body snapshot was fetched2026-11-03T04:31:37.620817Z and reread now; current10:11Z
  PMC request returned challenge HTML and guessed JATS404. Declared Methods/structural
  Results/Discussion were inspected as text, not raw images or tomography/spectra
  reanalysis.'
- 'Chlorosome, envelope and cis-Golgi network independent subreview: Orf2013 author-uploaded
  body was inspected through the browser at its actual captured time, separately from
  direct403 and publisher/PDF challenge HTML. It and Oostergetel2010 are secondary
  context; neither is recast as a new primary experiment.'
- 'Chlorosome, envelope and cis-Golgi network independent subreview: Li2006 and Frigaard2005
  were assessed from exact primary abstracts only. Cho2000 primary abstract was accessible;
  both attempted publisher body/PDF routes returned403. No fresh complete Methods
  claims are made for these articles.'
- 'Chlorosome, envelope and cis-Golgi network independent subreview: Rossanese1999
  complete Results/Discussion and Strains and Plasmids Methods were inspected; no
  figure pixels, full remaining Methods or supplementary analysis. Its evidence gap
  does not establish absence of CGN. ATCC/ENA strain identity is not organelle-occurrence
  evidence.'
- 'Chlorosome, envelope and cis-Golgi network independent subreview: Ten declared
  chlorosome-family protein examples are verified in each record, seven reviewed and
  three unreviewed. InterPro match endpoints are bounded to these exact accessions;
  H2VFJ4 HTTP204 and exact-symbol csmK zero hits do not establish universal family/protein
  absence. Generic acceptor and missing csmK example remain explicitly bounded.'
- 'Chlorosome, envelope and cis-Golgi network independent subreview: iModulonDB no-match
  is limited to the complete catalogue fetched10:11:10Z and assigned taxa. Historical
  runner PermissionError is00:49Z, not a current invocation. No uncovered-organism
  downstream query or module membership was fabricated.'
- 'Chlorosome, envelope and cis-Golgi network independent subreview: Original review
  access and global-check dates remain historical and may have different scope. Current
  native six protein-command receipts were inspected; root owns current whole-corpus
  QC, label/identifier/trait/history gates, issue deduplication/publication and final
  integration.'
- 'Chloroplast membrane, outer membrane, stroma and ciliary pocket membrane independent
  subreview: Assigned four unchanged targets only; all four original bundles validate/render
  exactly and their original frozen record hashes remain current. No original scientific
  findings/actions exist and none is invented.'
- 'Chloroplast membrane, outer membrane, stroma and ciliary pocket membrane independent
  subreview: Public chloroplast source snapshots were reused with their original2026-11-03T09:33Z
  timestamps and verified hashes. Keeling body is secondary Abstract/section1 only;
  Jin is primary complete indexed abstract and exact author abstract entry, not full
  Results.'
- 'Chloroplast membrane, outer membrane, stroma and ciliary pocket membrane independent
  subreview: Terashima current usable scope is its complete secondary abstract; the
  retained nominal PDF response is HTML challenge. The historical October original
  review had a wider reported body scope, which this current review does not impersonate.
  Karcher primary support is complete abstract only; publisher/PDF routes returned403.'
- 'Chloroplast membrane, outer membrane, stroma and ciliary pocket membrane independent
  subreview: Current direct and legacy pocket PMC routes returned challenge HTML;
  Europe PMC fullTextXML returned500. Gadelha indexed primary Discussion and Lacomble
  indexed Methods were read at exact saved extents plus complete native abstracts.
  They are not complete direct full-body reads. Field and Halliday support is native
  secondary abstract only; current publisher responses are challenge/stub pages.'
- 'Chloroplast membrane, outer membrane, stroma and ciliary pocket membrane independent
  subreview: No figure pixels, raw tomography, supplementary proteome lists, kinetic
  datasets or full quantitative inventories were audited. No unobserved source body
  or unsupported life-stage/strain transfer is claimed.'
- 'Chloroplast membrane, outer membrane, stroma and ciliary pocket membrane independent
  subreview: The bounded web retrieval searches returned unrelated pages; only exact
  primary publication matches were used. Their absence of other results is not evidence
  of biological or bibliographic absence.'
- 'Chloroplast membrane, outer membrane, stroma and ciliary pocket membrane independent
  subreview: The complete source catalogue has no matched green-algal or T. brucei
  organism; coverage limits do not mean biological absence. No molecular query is
  invented for the sparse ciliary-pocket membrane. The00:49Z runner failure is historical,
  separate from current official source fallback.'
- 'Chloroplast membrane, outer membrane, stroma and ciliary pocket membrane independent
  subreview: All eight native protein commands pass empty inventories (zero typed
  protein nodes). They cannot establish TOC–TIC/HLP narrative identity, localization,
  protein function or assembly necessity.'
- 'Chloroplast membrane, outer membrane, stroma and ciliary pocket membrane independent
  subreview: Constitutional collective bilayer material is distinct from empirical
  requirement for each lipid species. The spatial stroma need not assert an invariant
  molecular inventory; individual formation necessity remains unknown.'
- 'Chloroplast membrane, outer membrane, stroma and ciliary pocket membrane independent
  subreview: The six additional frozen neighbors were read only for boundary fields.
  No other record, historical issue or category finding is terminally resolved. Global
  gates, issue dedup/publication, repository writes and merge decisions remain root-owned.'
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
- 'Issue #2657 tracks the thylakoid part_of edges and the chlorosome/baseplate node-typing
  and accessory-protein localization refreshes. Scientific record curation remains
  separately tracked and open. Existing validator #2514 remains open.'
- 'Issue #2658 tracks five omitted applicability assessments and three unsupported
  expression-only exclusions. Thylakoid lumen and ciliary pocket membrane are genuine
  sparse topology exclusions.'
- Source commit fa6c7f0034c57fac03d026ce0ddb8aaa4bd4b2e3 is retained by tag review-base/pr2359-current-record-followup-20261103.
- CLAUDE.md is an alias of AGENTS.md; canonical regular AGENTS.md bytes are frozen.
- All used local context was frozen before assessment, including nine neighbor records,
  native configuration, graph/protein policies and verifier source. Neighbors are
  context only, not additional targets or dispositions of their findings.
- Fresh and reused public-source snapshots retain actual access dates and inspection
  tiers. Native authority identity does not independently establish localization,
  mechanistic action or assembly necessity.
- Native checks with empty protein inventories or zero GENE_OR_PROTEIN nodes do not
  validate molecules appearing only in narrative prose.
- Thylakoid membrane/lumen part_of edges are assessed as anatomical containment. They
  do not reinstate the earlier bounds overclaim or establish one globally continuous
  lumen from local tomographic observations.
- 'Chlorosome baseplate complex typing and accessory protein localization are assessed
  separately from assembly necessity. Closed #2419 is history context for grouped
  node typing; this follow-up does not dispose of that grouped issue or category findings.
  Open #2537 concerns experimental-preparation wording in the separate baseplate-complex
  record.'
- 'All five inherited scientific findings remain open for separate record curation:
  chlorosome and envelope baseplate assembly necessity, cis-Golgi current PPY12 taxon
  and stack-versus-CGN study scope (major), and whole-network-to-lipid component_ref
  (minor). Seven targets retain qualified positive scientific assessments. No record
  is edited.'
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T110921Z-chloroplast-membrane-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T110923Z-chloroplast-outer-membrane-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T110927Z-chloroplast-stroma-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T110930Z-chloroplast-thylakoid-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T110931Z-chloroplast-thylakoid-lumen-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T110932Z-chloroplast-thylakoid-membrane-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T110934Z-chlorosome-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T110935Z-chlorosome-envelope-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T110936Z-ciliary-pocket-membrane-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T110938Z-cis-golgi-network-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
links:
- https://github.com/CultureBotAI/CellStructureMech/pull/2359
- https://github.com/CultureBotAI/CellStructureMech/issues/2514
- https://github.com/CultureBotAI/CellStructureMech/issues/2657
- https://github.com/CultureBotAI/CellStructureMech/issues/2658
- https://github.com/CultureBotAI/CellStructureMech/issues/2659
- https://github.com/CultureBotAI/CellStructureMech/issues/2660
- https://github.com/CultureBotAI/CellStructureMech/issues/2661
- https://github.com/CultureBotAI/CellStructureMech/issues/2662
- https://github.com/CultureBotAI/CellStructureMech/issues/2663
```
