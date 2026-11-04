# PR 2382: current-input review of ten records and adversarial follow-up

- Review: 20261104T021428Z-pr2382-current-record-followup
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-11-04T01:57:28.444017Z
- Finished UTC: 2026-11-04T02:14:28Z
- Reviewer: Codex root synthesis with three independent read-only adversarial reviewers (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Independent current-input review of all ten structure records refreshes three stale observations (BAM, bindosome and CBF3), repairs ten unsupported structured-source applicability exclusions, and preserves nine independently confirmed inherited minor record-curation findings across eight targets. Apical complex and BAM pass with explicit source limits; the overall verdict remains needs_curation. Only immutable review successors are added.

## Scope And Provenance

Exact ten-record PR cohort reassessed against current main e715af32ff105343da446bc865a3adb2e3b5a2b3. Changed inputs are substantively reassessed. Scientific records remain unchanged.

Selection: Complete cohort of ten maintained records reviewed in original PR head 53645eea171f96d452504f427d3b33e21d15d586.
Coverage: full; 10 reviewed / 10 in the declared population.
Source: working_tree at Git base b82b8b5fcb02d90018a73c0d3d05ede8a2ab161f.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0044599 | data/structures/other/ap_5_adaptor_complex.yaml | maintained | AP-5 adaptor complex |
| GO:0030119 | data/structures/other/ap_type_membrane_coat_adaptor_complex.yaml | maintained | AP-type membrane coat adaptor complex |
| GO:0020007 | data/structures/other/apical_complex.yaml | maintained | apical complex |
| GO:0097691 | data/structures/other/bacterial_extracellular_vesicle.yaml | maintained | bacterial extracellular vesicle |
| GO:0061701 | data/structures/other/bacterial_outer_membrane_vesicle.yaml | maintained | bacterial outer membrane vesicle |
| GO:0036389 | data/structures/other/bacterial_pre_replicative_complex.yaml | maintained | bacterial pre-replicative complex |
| GO:1990063 | data/structures/other/bam_protein_complex.yaml | maintained | Bam protein complex |
| GO:7770042 | data/structures/other/bindosome_complex.yaml | maintained | bindosome complex |
| GO:0033186 | data/structures/other/caf_1_complex.yaml | maintained | CAF-1 complex |
| GO:0031518 | data/structures/other/cbf3_complex.yaml | maintained | CBF3 complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full native QC | passed | True | GO:0044599, GO:0030119, GO:0020007, GO:0097691, GO:0061701, GO:0036389, GO:1990063, GO:7770042, GO:0033186, GO:0031518 | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| Native label correspondence | passed | True | GO:0044599, GO:0030119, GO:0020007, GO:0097691, GO:0061701, GO:0036389, GO:1990063, GO:7770042, GO:0033186, GO:0031518 | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| TraitMech references | passed | True | GO:0044599, GO:0030119, GO:0020007, GO:0097691, GO:0061701, GO:0036389, GO:1990063, GO:7770042, GO:0033186, GO:0031518 | Native TraitMech link check passed. |
| Pinned governed files | passed | True | GO:0044599, GO:0030119, GO:0020007, GO:0097691, GO:0061701, GO:0036389, GO:1990063, GO:7770042, GO:0033186, GO:0031518 | Pinned governed files match; native vendored check passed. |
| Native identifier resolver | passed | True | GO:0044599, GO:0030119, GO:0020007, GO:0097691, GO:0061701, GO:0036389, GO:1990063, GO:7770042, GO:0033186, GO:0031518 | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| validate GO:0044599 | passed | True | GO:0044599 | Documented focused command passed. |
| validate-strict GO:0044599 | passed | True | GO:0044599 | Documented focused command passed. |
| validate GO:0030119 | passed | True | GO:0030119 | Documented focused command passed. |
| validate-strict GO:0030119 | passed | True | GO:0030119 | Documented focused command passed. |
| validate GO:0020007 | passed | True | GO:0020007 | Documented focused command passed. |
| validate-strict GO:0020007 | passed | True | GO:0020007 | Documented focused command passed. |
| validate GO:0097691 | passed | True | GO:0097691 | Documented focused command passed. |
| validate-strict GO:0097691 | passed | True | GO:0097691 | Documented focused command passed. |
| validate GO:0061701 | passed | True | GO:0061701 | Documented focused command passed. |
| validate-strict GO:0061701 | passed | True | GO:0061701 | Documented focused command passed. |
| validate GO:0036389 | passed | True | GO:0036389 | Documented focused command passed. |
| validate-strict GO:0036389 | passed | True | GO:0036389 | Documented focused command passed. |
| validate GO:1990063 | passed | True | GO:1990063 | Documented focused command passed. |
| validate-strict GO:1990063 | passed | True | GO:1990063 | Documented focused command passed. |
| validate GO:7770042 | passed | True | GO:7770042 | Documented focused command passed. |
| validate-strict GO:7770042 | passed | True | GO:7770042 | Documented focused command passed. |
| validate GO:0033186 | passed | True | GO:0033186 | Documented focused command passed. |
| validate-strict GO:0033186 | passed | True | GO:0033186 | Documented focused command passed. |
| validate GO:0031518 | passed | True | GO:0031518 | Documented focused command passed. |
| validate-strict GO:0031518 | passed | True | GO:0031518 | Documented focused command passed. |
| Supplemental bounded PMID authority checks | passed | True | GO:0044599, GO:0030119, GO:0020007, GO:0097691, GO:0061701, GO:0036389, GO:1990063, GO:7770042, GO:0033186, GO:0031518 | 909 PMIDs all OK in bounded native requests; full-command limitations remain separate. |
| Official structured-source applicability and covered-dataset cross-checks | passed | False | GO:0044599, GO:0030119, GO:0020007, GO:0097691, GO:0061701, GO:0036389, GO:1990063, GO:7770042, GO:0033186, GO:0031518 | All ten whole-record molecular or pathway narratives require an applicability assessment: seven formal and three prose-only exclusions are corrected. Fresh official catalogues and bounded E. coli precise1k and S. aureus dataset context were inspected; absent matched human, apicomplexan, yeast and solfataricus datasets do not imply biological absence. Experimental strain and reference-annotation identities remain distinct; expression modules do not establish physical membership, mechanism or necessity. The runner-unavailable receipt is historical, not a fresh invocation. |
| Independent claim-level source review | passed | True | GO:0044599, GO:0030119, GO:0020007, GO:0097691, GO:0061701, GO:0036389, GO:1990063, GO:7770042, GO:0033186, GO:0031518 | Three read-only reviewers covered the complete ten-record cohort, including changed inputs, with explicit scientific findings and source-access limits. Final artifact/head acceptance occurs after saving. |
| Retained historical adapter runner availability | unavailable | False | GO:0044599, GO:0030119, GO:0020007, GO:0097691, GO:0061701, GO:0036389, GO:1990063, GO:7770042, GO:0033186, GO:0031518 | Historical00:49Z invocation unavailable due to OS access restriction. Official catalogue fallback was inspected separately; no fresh invocation is claimed. Actual historical exit1 is retained in the evidence receipt; the native unavailable-check model has no execution exit-code field. |
| Native AP-5 adaptor complex UniProt verify check | passed | True | GO:0044599 | 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native AP-5 adaptor complex UniProt causal check | passed | True | GO:0044599 | 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native AP-type membrane coat adaptor complex UniProt verify check | passed | True | GO:0030119 | 0 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native AP-type membrane coat adaptor complex UniProt causal check | passed | True | GO:0030119 | 0 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native apical complex UniProt verify check | passed | True | GO:0020007 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native apical complex UniProt causal check | passed | True | GO:0020007 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native bacterial extracellular vesicle UniProt verify check | passed | True | GO:0097691 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native bacterial extracellular vesicle UniProt causal check | passed | True | GO:0097691 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native bacterial outer membrane vesicle UniProt verify check | passed | True | GO:0061701 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native bacterial outer membrane vesicle UniProt causal check | passed | True | GO:0061701 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native bacterial pre-replicative complex UniProt verify check | passed | True | GO:0036389 | 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native bacterial pre-replicative complex UniProt causal check | passed | True | GO:0036389 | 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native Bam protein complex UniProt verify check | passed | True | GO:1990063 | 5 represented protein examples; 8 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native Bam protein complex UniProt causal check | passed | True | GO:1990063 | 5 represented protein examples; 8 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native bindosome complex UniProt verify check | passed | True | GO:7770042 | 2 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native bindosome complex UniProt causal check | passed | True | GO:7770042 | 2 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native CAF-1 complex UniProt verify check | passed | True | GO:0033186 | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native CAF-1 complex UniProt causal check | passed | True | GO:0033186 | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native CBF3 complex UniProt verify check | passed | True | GO:0031518 | 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native CBF3 complex UniProt causal check | passed | True | GO:0031518 | 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |

## Scientific And Domain Assessments

### Exact structural identity and anatomical relations

identity: supported. Targets: GO:0044599.

Exact GO0044599 AP5 identity, parent GO0030119 and beta5/zeta/mu5/sigma5 architecture are supported. Late-endosome association does not establish universal clathrin coating.

### Family/class grounding semantics

grounding: concern. Targets: GO:0044599.

Four exact AP5 family mappings are independently verified and remain improperly deferred as REVIEWED_LABEL_ONLY. This is not optional representative coverage or substitution of broad domains.

### Source claims and actual access tiers

evidence: supported. Targets: GO:0044599.

AP5 endosomal-sorting implication is supported by HeLa knockdown redistribution/morphology plus tagged localization/co-IP evidence. Precise cargo route, full coat mechanism and individual formation necessity remain unproven. All metadata and actual body read extents are separately recorded. Secondary review abstracts and unsuccessful body routes do not certify unread experimental details.

### Complete coarse functional graph

graph: supported. Targets: GO:0044599.

Current FUNCTION/NONMECHANISTIC graph is constitutional/functional, not a complete assembly cycle. AP5 endosomal-sorting implication is supported by HeLa knockdown redistribution/morphology plus tagged localization/co-IP evidence. Precise cargo route, full coat mechanism and individual formation necessity remain unproven.

### Formation versus function and membership

evidence: supported. Targets: GO:0044599.

Constituent classes retain UNKNOWN formation essentiality. Protein membership, intervention effects on cargo/organelles or invasion, and localization do not by themselves prove every component universally necessary for structure formation.

### Canonical organism, strain and distribution scope

scope: supported. Targets: GO:0044599.

Human species9606 canonical HeLa context and native human accessions are separated from assay hosts; COMMON is qualitative, not a population census.

### Numerical scope

quantity: supported. Targets: GO:0044599.

No current experimental physical-size measurement is asserted. Protein sequence lengths/masses and source assay timing remain scoped to their evidence; no broad stoichiometric or prevalence measurement is inferred.

### Frozen inputs and deterministic original artifact

schema: supported. Targets: GO:0044599.

Actual native original validation/render exit0; derived Markdown exact and all historical inputs match. Current target unchanged from its frozen original input. These checks do not recertify historical global gates as fresh execution.

### Native protein inventory and coverage limits

completeness: supported. Targets: GO:0044599.

Four reviewed human examples and four COVERED typed core-subunit nodes; current exact queries return their intended primary genes. Native sequence/family identities and experimental localization scopes are verified separately. Neither empty optional coverage nor generic protein-class typing is a scientific defect by itself.

### Historical discussion and current assertion scope

provenance: supported. Targets: GO:0044599.

Dated rationale, retrieval events and curation history remain append-only. Current notes/prompts can be corrected in separate authorized curation, with appended clarification and events; no historical source observation is rewritten or guessed.

### Whole-record molecular-source applicability

evidence: supported. Targets: GO:0044599.

Positive molecular subunits, cargo/maturation or protein secretion/invasion assertions trigger actual applicability. Fresh complete official catalogue has no matching native human/Tetrahymena/Toxoplasma/Apicomplexa dataset. Downstream queries are bounded not_applicable after host coverage assessment, not because expression claims are absent. Historical runner unavailability is separate from fresh catalogue/native-source fallback; unrelated assay organisms are not substituted.

### Current target verdict

consistency: concern. Targets: GO:0044599.

Needs curation: one confirmed inherited minor finding, retaining positive qualified scientific assessments outside the precise grounding/gloss defect. No new finding or terminal disposition is invented.

### Exact structural identity and anatomical relations

identity: supported. Targets: GO:0030119.

Exact GO0030119 generic identity, is_a GO0098796 membrane protein complex and part_of GO0030117 membrane coat preserve distinct relation types. Parent definition needs the separately identified subtype/mass qualification; two-large/mu/sigma architecture remains valid.

### Family/class grounding semantics

grounding: supported. Targets: GO:0030119.

Generic AP subtype-spanning classes are not forced into partial AP1–3 families or unchecked LLM InterPro prose; exact pan-class coverage is not established by the bounded candidates.

### Source claims and actual access tiers

evidence: supported. Targets: GO:0030119.

AP-type class constitution and coat-linking description are supported as coarse generic scope. The Tetrahymena AP3 example establishes successful mature mucocyst maturation, not absence of all immature vesicles or stable mature-organelle membership. All metadata and actual body read extents are separately recorded. Secondary review abstracts and unsuccessful body routes do not certify unread experimental details.

### Complete coarse functional graph

graph: supported. Targets: GO:0030119.

Current FUNCTION/NONMECHANISTIC graph is constitutional/functional, not a complete assembly cycle. AP-type class constitution and coat-linking description are supported as coarse generic scope. The Tetrahymena AP3 example establishes successful mature mucocyst maturation, not absence of all immature vesicles or stable mature-organelle membership.

### Formation versus function and membership

evidence: supported. Targets: GO:0030119.

Constituent classes retain UNKNOWN formation essentiality. Protein membership, intervention effects on cargo/organelles or invasion, and localization do not by themselves prove every component universally necessary for structure formation.

### Canonical organism, strain and distribution scope

scope: supported. Targets: GO:0030119.

Tetrahymena species5911 canonical scope and CU428.1 experimental background are distinct; the generic AP class is not limited to AP3 or this organism.

### Numerical scope

quantity: concern. Targets: GO:0030119.

Generic exhaustive large-chain110–130kDa and sigma15–20kDa ranges fail AP5 counterexamples. Hirst predicts beta5~94kDa, and native canonical sequence masses independently show beta5~93.9kDa/zeta~88.6kDa/sigma5~22.5kDa. These are not assembled-complex experimental masses.

### Frozen inputs and deterministic original artifact

schema: supported. Targets: GO:0030119.

Actual native original validation/render exit0; derived Markdown exact and all historical inputs match. Current target unchanged from its frozen original input. These checks do not recertify historical global gates as fresh execution.

### Native protein inventory and coverage limits

completeness: supported. Targets: GO:0030119.

Zero examples and three NO_GENE_SYMBOLS typed protein-class nodes. Passing accession diagnostics do not establish missing optional examples or test an unpopulated inventory. Neither empty optional coverage nor generic protein-class typing is a scientific defect by itself.

### Historical discussion and current assertion scope

provenance: supported. Targets: GO:0030119.

Dated rationale, retrieval events and curation history remain append-only. Current notes/prompts can be corrected in separate authorized curation, with appended clarification and events; no historical source observation is rewritten or guessed.

### Whole-record molecular-source applicability

evidence: supported. Targets: GO:0030119.

Positive molecular subunits, cargo/maturation or protein secretion/invasion assertions trigger actual applicability. Fresh complete official catalogue has no matching native human/Tetrahymena/Toxoplasma/Apicomplexa dataset. Downstream queries are bounded not_applicable after host coverage assessment, not because expression claims are absent. Historical runner unavailability is separate from fresh catalogue/native-source fallback; unrelated assay organisms are not substituted.

### Current target verdict

consistency: concern. Targets: GO:0030119.

Needs curation: one confirmed inherited minor finding, retaining positive qualified scientific assessments outside the precise grounding/gloss defect. No new finding or terminal disposition is invented.

### Exact structural identity and anatomical relations

identity: supported. Targets: GO:0020007.

Exact GO0020007 composite anatomy and four named organelle/cytoskeletal parts are supported at coarse scope. Conoid presence varies by lineage/stage; named parts do not assert universal identical molecular inventory.

### Family/class grounding semantics

grounding: supported. Targets: GO:0020007.

Two broad cytoskeletal/secretory classes are acknowledged heterogeneous and label-only; no exact shared family is inferred. Named anatomical identities and permitted classes remain distinct.

### Source claims and actual access tiers

evidence: supported. Targets: GO:0020007.

Apical structure/invasion context is supported by partial cytoskeletal enrichment, APR perturbations and source-specific secretory sequence. Carruthers directly measures secretion order during RH/2F invasion of HFF; whole-apical coordination and moving-junction interpretation are not upgraded into a directly demonstrated cytoskeleton-to-secretion causal edge. All metadata and actual body read extents are separately recorded. Secondary review abstracts and unsuccessful body routes do not certify unread experimental details.

### Complete coarse functional graph

graph: supported. Targets: GO:0020007.

Current FUNCTION/NONMECHANISTIC graph is constitutional/functional, not a complete assembly cycle. Apical structure/invasion context is supported by partial cytoskeletal enrichment, APR perturbations and source-specific secretory sequence. Carruthers directly measures secretion order during RH/2F invasion of HFF; whole-apical coordination and moving-junction interpretation are not upgraded into a directly demonstrated cytoskeleton-to-secretion causal edge.

### Formation versus function and membership

evidence: supported. Targets: GO:0020007.

Constituent classes retain UNKNOWN formation essentiality. Protein membership, intervention effects on cargo/organelles or invasion, and localization do not by themselves prove every component universally necessary for structure formation.

### Canonical organism, strain and distribution scope

scope: supported. Targets: GO:0020007.

Apicomplexa phylum5794 and Toxoplasma species5811 are distinguished from RH/RH-derived tachyzoite experimental backgrounds. COMMON and stage/lineage variation are qualitative comparative scope, not measured prevalence or universal inventory.

### Numerical scope

quantity: supported. Targets: GO:0020007.

No current experimental physical-size measurement is asserted. Protein sequence lengths/masses and source assay timing remain scoped to their evidence; no broad stoichiometric or prevalence measurement is inferred.

### Frozen inputs and deterministic original artifact

schema: supported. Targets: GO:0020007.

Actual native original validation/render exit0; derived Markdown exact and all historical inputs match. Current target unchanged from its frozen original input. These checks do not recertify historical global gates as fresh execution.

### Native protein inventory and coverage limits

completeness: supported. Targets: GO:0020007.

Zero protein examples and zero GENE_OR_PROTEIN typed graph nodes. The two broad constituent cohorts are permitted classes; native pass is empty protein-xref coverage and does not independently establish their biology. Neither empty optional coverage nor generic protein-class typing is a scientific defect by itself.

### Historical discussion and current assertion scope

provenance: supported. Targets: GO:0020007.

Dated rationale, retrieval events and curation history remain append-only. Current notes/prompts can be corrected in separate authorized curation, with appended clarification and events; no historical source observation is rewritten or guessed.

### Whole-record molecular-source applicability

evidence: supported. Targets: GO:0020007.

Positive molecular subunits, cargo/maturation or protein secretion/invasion assertions trigger actual applicability. Fresh complete official catalogue has no matching native human/Tetrahymena/Toxoplasma/Apicomplexa dataset. Downstream queries are bounded not_applicable after host coverage assessment, not because expression claims are absent. Historical runner unavailability is separate from fresh catalogue/native-source fallback; unrelated assay organisms are not substituted.

### Current target verdict

consistency: supported. Targets: GO:0020007.

Pass with limitations: no confirmed record defect. Current GO polar-ring definition tension, inaccessible secondary bodies, partial primary-body read extents, heterogeneous classes and taxon/necessity limits are explicit. No generic-family or optional-example issue is manufactured.

### Polar-ring term versus source anatomical distinction

identity: unknown. Targets: GO:0020007.

GO0020031 label/aliases denote apical/anterior polar ring, but definition describes anterior conoid-fiber origin, conflicting with Hu preconoidal-ring versus APR distinction and Ren three-layer APR. The record uses the correct named APR/coarse parthood without repeating that conflicting definition. No guessed replacement or confident identity refutation is warranted; exact ontology-definition alignment remains unresolved.

### identity origin

identity: concern. Targets: GO:0097691.

GO0097691 and SL0489 are exact maintained authority identities, but their definition specifies plasma-membrane budding while current components/graph explicitly span outer-membrane/OIMV and Gram-positive routes. Retain inherited minor source-scope reconciliation; no assertion that the copied definition is fabricated.

### composition

representation: supported. Targets: GO:0097691.

Composite membrane is honestly OTHER with mixed lipids/proteins and no guessed single chemical CURIE; variable heterogeneous cargo is OTHER/UNKNOWN. Membrane constitutional ESSENTIAL does not imply a specific protein biogenesis requirement.

### taxon canonical

scope: supported. Targets: GO:0097691.

Bacteria VARIABLE is qualitative species/condition scope. S. aureus canonical example is supported by Lee2009 complete primary abstract reporting vesicles and90 proteins; no exact strain, all cargo topology or molecular delivery mechanism is inferred from that abstract.

### function graph

graph: supported. Targets: GO:0097691.

The explicitly NON_MECHANISTIC cargo-carriage graph distinguishes inner/surface association from universal luminal enclosure and acknowledges multiple release routes. It does not assert all proteins/cargo occupy the same topology or specify one required assembly mechanism.

### boundary history

consistency: supported. Targets: GO:0097691.

Broad bacterial extracellular vesicle is distinguished from generic microvesicle and narrow outer-membrane vesicle. Current typed mixed membrane and carries relation are evaluated directly; old issues663/664 are historical record context, not claimed newly resolved.

### identity boundary

identity: supported. Targets: GO:0061701.

GO0061701 specifies Gram-negative outer-membrane-derived spherical proteolipid vesicles; broader GO1903561 parent and outer-membrane topology are coherent. Gram-positive cytoplasmic vesicles and OIMVs are explicitly distinguished rather than silently included.

### composite type

representation: concern. Targets: GO:0061701.

Inherited F1 remains: the component label/notes/reference denote the entire mixed protein/LPS/phospholipid membrane while its type is LIPID. OTHER is available and used in the paired BEV record. This is bounded composite classification, not a false chemical grounding or wrong vesicle identity.

### canonical source

provenance: concern. Targets: GO:0061701.

Inherited F2 remains: the canonical note combines native OMV proteomes and inflammatory response under Park2010. Park body supports injection model and comparative Coomassie/LPS profiles, whereas Lee2007 complete abstract explicitly supplies141-protein global profiling. Keep these two source claims separated.

### host experimental scope

scope: supported. Targets: GO:0061701.

Park isolates intestinal E. coli from mouse CLP peritoneal fluid using16S identification and tests intraperitoneal purified OMV administration. These species-level evidence claims do not establish the precise1k K-12-related strains, natural infection equivalence or human clinical causation. Record species-level example remains supported within that scope.

### graph cargo necessity

graph: supported. Targets: GO:0061701.

Coarse NON_MECHANISTIC budding, bilayer enclosure and parthood are supported. The record does not claim all proteomic hits are luminal; heterogeneous cargo UNKNOWN is appropriate and membrane ESSENTIAL is constitutive. Empty optional protein examples are not a defect.

### identity composition

identity: supported. Targets: GO:0033186.

GO0033186 conserved heterotrimer and yeast Cac1/p90,Cac2/p60,Msi1/Cac3/p50 are supported by current authority and Kaufman primary purification/peptide-identification Results. Generic human p150/p60/p48/H3.1 definition is authority-scoped, not asserted as yeast subunit mass or histone variant.

### family grounding

grounding: concern. Targets: GO:0033186.

Inherited caf1-cac2-family remains: full family IPR045145 exactly matches the Cac2 class and current Q04199 crossreference, making that active REVIEWED_LABEL_ONLY/TODO gap actionable. Do not substitute Cac1 partial domains or broader MSI1/RBAP paralog class for narrow classes.

### native identities

nomenclature: supported. Targets: GO:0033186.

All3 accessions are reviewed S288c entries with exact gene/locus tokens: Q12495 primary RLF2 aliasCAC1/YPR018W; Q04199 CAC2/YML102W; P13712 MSI1 aliasCAC3/YBR195C. Their S288c identity examples do not recast BJ926 purification or W303 genetics as experiments in that strain.

### location evidence

evidence: supported. Targets: GO:0033186.

P13712 cytoplasm annotation is correctly tied to PMID11238915 in the native entry and the Johnston abstract distinguishes its CAF-independent RAS function. Identity/localization evidence is separated from Kaufman CAF membership; no claim the full CAF complex is necessarily cytoplasmic.

### graph necessity

graph: supported. Targets: GO:0033186.

NON_MECHANISTIC membership→CAF-I→nucleosome assembly is supported by purified-complex replication-preferential SV40 assay. UNKNOWN formation necessity remains appropriate: cell viability and UV/telomeric-silencing mutant phenotypes do not directly establish whether every subunit is required for physical complex assembly.

### taxon boundary

scope: supported. Targets: GO:0033186.

Saccharomyces canonical system and COMMON qualitative label are bounded to established study context, not a species-wide census. No lumping of adjacent chromatin remodelers or automatic resolution of unrelated histories is proposed.

### identity composition

identity: supported. Targets: GO:0031518.

Current GO0031518 and primary structures support Ctf13,Skp1,Cep3,Ndc10 protein classes in CBF3. Four classes do not mean four total monomers: the full structural preparation can contain Cep3 and Ndc10 dimers. Current record does not assert contrary stoichiometry.

### family grounding

grounding: concern. Targets: GO:0031518.

Inherited cbf3-skp1-family remains. IPR016897 is full Skp1 and maps P52286. Requiring a family uniquely separating CBF3-specific Skp1 from its SCF/RAVE roles confuses class identity with role context. Wider IPR001232 and other subunit domains are not forced into exact classes.

### native identities

nomenclature: supported. Targets: GO:0031518.

All4 reviewed S288c accessions and loci are correct: P35203 CTF13/YMR094W,P52286 SKP1/YDR328C,P40969 CEP3/YMR168C,P32504 primaryCBF2 aliasNDC10/YGR140W. The role explains native primary CBF2 while maintaining literature Ndc10; no arbitrary renaming is needed.

### location source joins

evidence: supported. Targets: GO:0031518.

Skp1 Huh2003 and Ndc10 Zeng1999 location references are checked against actual native SUBCELLULAR LOCATION annotations. Huh abstract alone is not a specific Skp1 image; Zeng Cbf2-GFP methods are a bounded control, not a wholesale reassignment of Slk19/Kar3 results to Ndc10.

### stale delta

graph: supported. Targets: GO:0031518.

Substantive stale refresh: Oct30 adds Ctf13→CBF3 and Skp1→CBF3 assembles_into edges and history. Leber body explicitly coexpresses full four-class complex, then separates Ndc10 and structures the Ctf13/Skp1/Cep3 core; Yan full CBF3–CEN3 body corroborates Ndc10/Ctf13 interface. Thus both new membership edges are supported with core/full distinctions preserved. Inherited Skp1 grounding gap is unchanged by these graph repairs.

### function necessity

scope: supported. Targets: GO:0031518.

NON_MECHANISTIC centromeric DNA/kinetochore initiation graph is appropriately bounded. Yan Cse4 deposition is proposed and not promoted to directly observed complete mechanism. UNKNOWN formation necessity is not invalidated by selected interface mutations, essential viability or purification alone.

### native validation

schema: supported. Targets: GO:0097691.

Current native verify/causal receipts both exit0. Independently counted 0 examples/0 GENE_OR_PROTEIN nodes, all reviewed/COVERED when nonempty. Four original YAML/Markdown pairs validate/render exactly;55 historical input occurrences match their original sources. No repository mutation was performed.

### completeness images

completeness: supported. Targets: GO:0097691.

Entire maintained record reviewed. No current image entry or separately curated physical-property measurement is present; definitional size language remains within the authority/source scope. No invented image/measurement obligation is imposed. Source text captions were used only within declared access tiers; no figure-pixel inspection is claimed. Existing source-neutral unresolved classes and generic cargo are not forced into unsupported exact identifiers.

### structured sources

evidence: supported. Targets: GO:0097691.

Positive molecular cargo-delivery/export and proteomic canonical narratives trigger the native adapter applicability assessment despite no named protein examples. The original prose exclusion expressly dismisses vesicle carriage and is unsupported. Fresh complete catalogue plus S. aureus108/165 and E. coli precise1k strain/annotation checks were performed; no yeast proxy or unverified experimental-strain match. Literal vesicle/cargo nonhits are not biological absence; selected OmpF expression contexts and OmpA below-threshold status do not prove OMV cargo.

### verdict lineage

provenance: concern. Targets: GO:0097691.

Current verdict remains needs_curation for the independently confirmed inherited minor finding(s). Exact predecessor identity is preserved; no original finding is silently dropped, no historical record repair is claimed as this PR work, and record curation remains outside this review-only branch.

### native validation

schema: supported. Targets: GO:0061701.

Current native verify/causal receipts both exit0. Independently counted 0 examples/0 GENE_OR_PROTEIN nodes, all reviewed/COVERED when nonempty. Four original YAML/Markdown pairs validate/render exactly;55 historical input occurrences match their original sources. No repository mutation was performed.

### completeness images

completeness: supported. Targets: GO:0061701.

Entire maintained record reviewed. No current image entry or separately curated physical-property measurement is present; definitional size language remains within the authority/source scope. No invented image/measurement obligation is imposed. Source text captions were used only within declared access tiers; no figure-pixel inspection is claimed. Existing source-neutral unresolved classes and generic cargo are not forced into unsupported exact identifiers.

### structured sources

evidence: supported. Targets: GO:0061701.

Positive molecular cargo-delivery/export and proteomic canonical narratives trigger the native adapter applicability assessment despite no named protein examples. The original prose exclusion expressly dismisses vesicle carriage and is unsupported. Fresh complete catalogue plus S. aureus108/165 and E. coli precise1k strain/annotation checks were performed; no yeast proxy or unverified experimental-strain match. Literal vesicle/cargo nonhits are not biological absence; selected OmpF expression contexts and OmpA below-threshold status do not prove OMV cargo.

### verdict lineage

provenance: concern. Targets: GO:0061701.

Current verdict remains needs_curation for the independently confirmed inherited minor finding(s). Exact predecessor identity is preserved; no original finding is silently dropped, no historical record repair is claimed as this PR work, and record curation remains outside this review-only branch.

### native validation

schema: supported. Targets: GO:0033186.

Current native verify/causal receipts both exit0. Independently counted 3 examples/3 GENE_OR_PROTEIN nodes, all reviewed/COVERED when nonempty. Four original YAML/Markdown pairs validate/render exactly;55 historical input occurrences match their original sources. No repository mutation was performed.

### completeness images

completeness: supported. Targets: GO:0033186.

Entire maintained record reviewed. No current image entry or separately curated physical-property measurement is present; definitional size language remains within the authority/source scope. No invented image/measurement obligation is imposed. Source text captions were used only within declared access tiers; no figure-pixel inspection is claimed. Existing source-neutral unresolved classes and generic cargo are not forced into unsupported exact identifiers.

### structured sources

evidence: supported. Targets: GO:0033186.

Named yeast genes/proteins and assembly/function pathways trigger an actual applicability assessment; the original formal no-expression-claim exemption is insufficient. Complete current official catalogue has no Saccharomyces dataset, so no organism-matched downstream module query applies. This scoped source result is not absence of the structure, pathway or gene.

### verdict lineage

provenance: concern. Targets: GO:0033186.

Current verdict remains needs_curation for the independently confirmed inherited minor finding(s). Exact predecessor identity is preserved; no original finding is silently dropped, no historical record repair is claimed as this PR work, and record curation remains outside this review-only branch.

### native validation

schema: supported. Targets: GO:0031518.

Current native verify/causal receipts both exit0. Independently counted 4 examples/4 GENE_OR_PROTEIN nodes, all reviewed/COVERED when nonempty. Four original YAML/Markdown pairs validate/render exactly;55 historical input occurrences match their original sources. No repository mutation was performed.

### completeness images

completeness: supported. Targets: GO:0031518.

Entire maintained record reviewed. No current image entry or separately curated physical-property measurement is present; definitional size language remains within the authority/source scope. No invented image/measurement obligation is imposed. Source text captions were used only within declared access tiers; no figure-pixel inspection is claimed. Existing source-neutral unresolved classes and generic cargo are not forced into unsupported exact identifiers.

### structured sources

evidence: supported. Targets: GO:0031518.

Named yeast genes/proteins and assembly/function pathways trigger an actual applicability assessment; the original formal no-expression-claim exemption is insufficient. Complete current official catalogue has no Saccharomyces dataset, so no organism-matched downstream module query applies. This scoped source result is not absence of the structure, pathway or gene.

### verdict lineage

provenance: concern. Targets: GO:0031518.

Current verdict remains needs_curation for the independently confirmed inherited minor finding(s). Exact predecessor identity is preserved; no original finding is silently dropped, no historical record repair is claimed as this PR work, and record curation remains outside this review-only branch.

### Generic bacterial pre-RC and restricted substates

identity: supported. Targets: GO:0036389.

Active GO0036389 and is-a pre-replicative/protein-DNA ancestry agree. The source distinguishes persistent high-affinity ORC from higher-order DnaA loading; current generic record does not silently identify every DiaA/HU/helicase substate as obligatory part.

### Exact DnaA family versus broader DnaA/Hda

grounding: concern. Targets: GO:0036389.

Current IPR001957 is the DnaA family and matches P03004. IPR020591 also includes Hda and is broader. This independently confirms the inherited minor actionable DnaA grounding gap; no exact SO term is invented for oriC and no historical search is called dishonest.

### Native DnaA identity and annotation joins

grounding: supported. Targets: GO:0036389.

P03004 reviewed dnaA/b3702 K-12 identity and exact name match. Regev2012, Schenk2017 and Garner1998 abstract scopes plus native annotation joins support the recorded source associations; E. coli/BL21 and Bacillus substudies are not silently treated as identical K-12 pre-RC experiments.

### Origin recognition and replication initiation

evidence: supported. Targets: GO:0036389.

Miller site substitutions, oligomerization mutant, footprints and binding assays support DnaA/oriC assembly and initiation competence. Licensing is generic biological language here; no eukaryotic licensing apparatus or sufficiency of binding for completed replication is asserted.

### Three coarse assembly/function edges

graph: supported. Targets: GO:0036389.

DnaA contributes, oriC scaffolds and the complex supports initiation. NONMECHANISTIC scope deliberately withholds lower-affinity loading dynamics, atomic oligomer details and later helicase transfer; the available primary source supports these bounded relations.

### Formation necessity and defined constituents

grounding: unknown. Targets: GO:0036389.

DnaA/oriC constitute the named complex and site/oligomerization experiments affect assembly. UNKNOWN flags are conservative; this review does not convert cell viability or individual site defects into a universal formation assay, nor demand optional depletion experiments.

### Canonical E. coli versus assay and module strains

scope: supported. Targets: GO:0036389.

Species562/K-12 identity and E. coli source system agree. COMMON remains qualitative ordinary initiation machinery, not a new prevalence census. W3110 is present in the selected dataset, but pooled five-strain module context is not the exact PC2/polA assay condition.

### Exact BAM complex and outer-membrane boundary

identity: supported. Targets: GO:1990063.

GO1990063 and primary sources denote bacterial BamABCDE assembly machinery, distinct from its external substrates or chaperones. GO0106234 biological broader class is supported by definition even though current is-a-only ancestry lacks that exact term; part_of outer membrane has native support.

### Five exact constituent families and examples

grounding: supported. Targets: GO:1990063.

BamA–E respective IPR023707/017687/014524/017689/026592 are full named families, each joined to the verified reviewed K-12 example. New family-grounded nodes correctly propagate those identities and component_refs. Generic BamB–E grouped actor is permitted, not falsely a new obligatory protein family.

### OmpT external substrate and product exemplars

grounding: supported. Targets: GO:1990063.

P09169 reviewed K-12 ompT/Protease7 is the correct protein identity. Hagan directly reconstitutes OmpT folding/insertion; the two actor xrefs give a concrete example and do not promote OmpT to a BAM constituent. Reference K-12 identity is kept distinct from expression hosts and the Hagan supplementary cloning details not read here.

### Four newly explicit lipoprotein parthood edges

graph: supported. Targets: GO:1990063.

Each new B/C/D/E node is a member of the group BamB–E actor, not a separately asserted stable four-protein isolated complex. Gu text supports BamB–POTRA2/3, BamC–BamD and BamE bridging BamD/POTRA4/5; Iadanza supports BamD/POTRA interactions. Parthood and source-grounded organization remain bounded; BamD essential wording concerns known bacterial function and is not imported into formal UNKNOWN formation flags.

### Reconstituted beta-barrel assembly

evidence: supported. Targets: GO:1990063.

Hagan supports purified BAM+SurA OmpT folding/insertion with LPS assay requirement, heat-modifiability and membrane integration readouts. This does not establish an ATP-driven mechanism or universal atomic sequence; current function is appropriately broad.

### Nonmechanistic state sampling retains distinct preparations

graph: supported. Targets: GO:1990063.

Gu captures intact inward-open and four-subunit lateral-open structures, Bakelar resolves BamACDE plus a modeled BamB, and Iadanza observes intact laterally open BAM. The record uses Iadanza for intact lateral opening and does not require every Gu state to contain all five subunits. Detergent/structural snapshots do not prove every catalytic transition.

### Approximate203kDa source-specific mass

quantity: supported. Targets: GO:1990063.

Iadanza native MS predominant203456±22Da agrees with approximate203kDa. Minor extra-BamE and reconstitution/detergent context prevent treating this as invariant across all bacteria. Units are exact kilodalton.

### Formation, viability and folding efficiency are distinct

grounding: unknown. Targets: GO:1990063.

All components retain UNKNOWN formation necessity. Essential BamA/D viability, nonessential B/C/E and maximum OmpT activity with all five do not independently settle every assembly condition or lineage. No optional depletion experiment is demanded and SurA remains upstream machinery, not a forced constituent.

### Diderm distribution and recombinant systems

scope: supported. Targets: GO:1990063.

Bacteria VARIABLE and explicit diderm/monoderm scope are compatible with the secondary overview and primary E. coli systems. BL21(DE3), HDB150 and DH5alpha contexts are distinct from reference K-12 annotations. No bacterial prevalence census or exact single-strain dataset equivalence is claimed.

### Surface sugar-binding assembly and Bas boundary

identity: supported. Targets: GO:7770042.

GO7770042 and parentGO0098796 agree with the mature surface sugar-binding assembly. Current Saccharolobus solfataricus identity accommodates historical Sulfolobus nomenclature. BasEF/ABC function in organization and uptake is not automatically mature400/600kDa constituent membership.

### Mixed class and exact available family limits

grounding: supported. Targets: GO:7770042.

Generic sugar-binding PROTEIN class is permitted; GlcS/AraS and uncertain SSO3043/1273 roles remain qualified. Native GlcS-like and broad solute-binding families do not establish an exact combined GlcS/AraS/TreS whole-class grounding; their LLM descriptions are not primary membership evidence. SlaA copurification remains an explicit boundary question.

### New unreviewed AraS/SSO3066 exemplar

grounding: supported. Targets: GO:7770042.

Native Q97UF5 is UNREVIEWED, ordered locusSSO3066, exact arabinose-binding product and P2tax273057. Albers2003 Table2 directly maps SSO3066 to AraS, so alias-query0 does not undermine the disclosed literature-to-locus mapping. The example remains identity-only; current2011 paper independently names AraS. No false reviewed status or exact native geneName assertion is inferred.

### Reviewed GlcS reference

grounding: supported. Targets: GO:7770042.

Q97UZ1 is reviewed glcS/SSO2847 in P2 and the exact reviewed query returns that accession. Identity is separate from source-backed binding-protein assembly; current native cross-references alone do not prove membership.

### Missing maintained claim-adjacent TreS constituent source

evidence: concern. Targets: GO:7770042.

The current gene_symbols includes treS but its cited GO/2011 source does not identify that named constituent. Newly inspected Albers2003 positively maps TreS toSSO0999 and discusses processing; this corrects any implication of biological absence, but is not yet a maintained citation or direct demonstration of TreS in the recovered400/600kDa complexes. Retain original minor as a bounded source-link curation gap, not a mandatory deletion or optional example gap.

### Organization and uptake versus extracted assembly

grounding: unknown. Targets: GO:7770042.

BasEF deletion preserves400/600kDa extracted complexes yet disrupts glucose uptake and surface morphology; this supports the recorded distinction between mature constituents and assembly/localization machinery. UNKNOWN for the broad binding-protein cohort does not imply dispensability.

### Coarse sugar uptake model with contact limits

graph: supported. Targets: GO:7770042.

Protein assemblies and sugar uptake support the two broad assembly/function edges. GO supplies the functional interaction interpretation, while the paper treats exact positioning/ABC handoff as inferred and fails to localize GlcS decisively. MECHANISTIC here remains a coarse model, not a directly resolved transporter contact or invariant native stoichiometry.

### PBL2025 experiments versus P2 examples

scope: supported. Targets: GO:7770042.

The paper tests PBL2025 andΔbasEF under defined media, whereas examples identify referenceP2. Species-level canonical identity is preserved without claiming P2 was the actual experimental strain. COMMON is qualitative and no universal high-mass composition/prevalence census is asserted.

### Claim-sensitive structured-source correction

scope: concern. Targets: GO:0036389.

Current positive DnaA/oriC initiation assertions require applicability; native explicit exclusion only says no expression-module claim. Fresh official E. coli precise1k actual gene/module context was inspected: all seven selected loci represented, no above-threshold dnaA/BAM membership, external OmpT in59/164. Neither membership nor nonmembership proves structure biology.

### Frozen observation and append-only history

provenance: supported. Targets: GO:0036389.

Original observation remains immutable; current source differences and historical edits are assessed independently. No category-wide or grouped historical issue resolution follows from source history. Dated discussion rationale/posed_date remain preserved; current notes/prompts may be updated only through later authorized curation.

### Actual validation and diagnostic scope

schema: supported. Targets: GO:0036389.

Original YAML and native Markdown pass exact validation/render;42historical inputs verified. Current root protein commands passed with independently checked actual inventory/classifications; no generic pass is equated to full scientific coverage.

### Whole-record scope with no forced optional fields

completeness: supported. Targets: GO:0036389.

Complete target reviewed; no maintained images or verbatim snippets occur. No figure pixels/raw data/supplements were reanalyzed and no optional image/example/chemical field was required merely because empty. Source-scoped limitations and open discussions remain explicit.

### Claim-sensitive structured-source correction

scope: concern. Targets: GO:1990063.

Current positive BamA–E/OmpT assembly assertions require applicability; original notes[1] excludes molecular complex claims in prose, without a formal adapter row. Fresh official E. coli precise1k actual gene/module context was inspected: all seven selected loci represented, no above-threshold dnaA/BAM membership, external OmpT in59/164. Neither membership nor nonmembership proves structure biology.

### Frozen observation and append-only history

provenance: supported. Targets: GO:1990063.

Original observation remains immutable; current source differences and historical edits are assessed independently. No category-wide or grouped historical issue resolution follows from source history. Dated discussion rationale/posed_date remain preserved; current notes/prompts may be updated only through later authorized curation.

### Actual validation and diagnostic scope

schema: supported. Targets: GO:1990063.

Original YAML and native Markdown pass exact validation/render;42historical inputs verified. Current root protein commands passed with independently checked actual inventory/classifications; no generic pass is equated to full scientific coverage.

### Whole-record scope with no forced optional fields

completeness: supported. Targets: GO:1990063.

Complete target reviewed; no maintained images or verbatim snippets occur. No figure pixels/raw data/supplements were reanalyzed and no optional image/example/chemical field was required merely because empty. Source-scoped limitations and open discussions remain explicit.

### Claim-sensitive structured-source correction

scope: concern. Targets: GO:7770042.

Current positive sugar-binding/ABC uptake assertions require applicability; native explicit exclusion only says no expression-module claim. Fresh catalogue lacks the exact solfataricus host; acidocaldarius is a different species and is not used as proxy. Applicability assessed, but no matched-host downstream dataset is asserted.

### Frozen observation and append-only history

provenance: supported. Targets: GO:7770042.

Original observation remains immutable; current source differences and historical edits are assessed independently. No category-wide or grouped historical issue resolution follows from source history. Dated discussion rationale/posed_date remain preserved; current notes/prompts may be updated only through later authorized curation.

### Actual validation and diagnostic scope

schema: supported. Targets: GO:7770042.

Original YAML and native Markdown pass exact validation/render;42historical inputs verified. Current root protein commands passed with independently checked actual inventory/classifications; no generic pass is equated to full scientific coverage.

### Whole-record scope with no forced optional fields

completeness: supported. Targets: GO:7770042.

Complete target reviewed; no maintained images or verbatim snippets occur. No figure pixels/raw data/supplements were reanalyzed and no optional image/example/chemical field was required merely because empty. Source-scoped limitations and open discussions remain explicit.

### Current scoped scientific disposition

other: concern. Targets: GO:0036389.

needs_curation: one independently confirmed inherited minor; exact lineage retained.

### Current scoped scientific disposition

other: supported. Targets: GO:1990063.

pass_with_limitations: BAM current substantive additions and complete record supported at declared tiers; no confirmed new scientific record defect. Historical adapter exclusion and staleness require successor repair.

### Current scoped scientific disposition

other: concern. Targets: GO:7770042.

needs_curation: one independently confirmed inherited minor; exact lineage retained.

### Complete frozen-input comparison and bounded refresh

provenance: supported. Targets: GO:0044599, GO:0030119, GO:0020007, GO:0097691, GO:0061701, GO:0036389, GO:1990063, GO:7770042, GO:0033186, GO:0031518.

3 of ten original target hashes differ from current main. The changed content is substantively reassessed in the target-specific assessments; original observations remain historical and unchanged. All current target and used context bytes are frozen.

## Findings

### septin-ap_5_adaptor_complex-F1: Ground the four verified AP5 subunit families

minor / open / confirmed; issue key: ap5-four-verified-family-groundings-label-only.

The native family identities ap5_beta5_subunit → InterPro:IPR038741, ap5_zeta_subunit → InterPro:IPR028222, ap5_mu5_subunit → InterPro:IPR039591, ap5_sigma5_subunit → InterPro:IPR029392 exactly match the four maintained AP5-specific subunit classes and their human examples. All four rows instead retain REVIEWED_LABEL_ONLY with notes saying no exact CURIE was curated in the earlier pass. The schema and CURATION define that status as inability to assert an exact class, not unfinished identifier curation. Current native authorities and actual primary-source scopes were independently re-read. Any discussion clarification preserves its dated rationale and appends rather than rewrites history.

### septin-ap_type_membrane_coat_adaptor_complex-F1: Qualify the exhaustive parent-class subunit description

minor / open / confirmed; issue key: ap-type-parent-gloss-excludes-ap5-zeta-mass.

The definition says each AP complex has beta plus alpha/gamma/delta/epsilon large chains of110–130kDa and sigma15–20kDa; the large-subunit row repeats the exhaustive chain list. Native GO0030119 repeats this text but also includes AP5 as a direct child. GO0044599 and Hirst2011 identify AP5 zeta, and Hirst predicts beta5 at94kDa. Native human sequence masses independently give beta5~93.9kDa, zeta~88.6kDa and sigma5~22.5kDa. These are subtype counterexamples to the generic exhaustive gloss, while the two-large/mu/sigma architecture remains correct. Current native authorities and actual primary-source scopes were independently re-read. Any discussion clarification preserves its dated rationale and appends rather than rewrites history.

### plaque-t3-F1: Distinguish the authority definition from the broader vesicle-origin scope

minor / open / confirmed; issue key: CellStructureMech-bacterial_extracellular_vesicle-authority-definition-origin-scope.

The definition, attributed solely to GO:0097691, describes plasma-membrane budding. It is faithfully copied from GO/SL, but the same record explicitly includes outer-membrane, outer-inner-membrane and Gram-positive vesicles and says several release pathways. Toyofuku2019 complete abstract expressly includes outer-membrane blebbing and lysis-derived routes. Readers need an explicit source-qualified scope note reconciling the narrow authority wording with the broader current record; this is not a claim that the copied GO definition or observed vesicle classes are fabricated.

### plaque-t4-F1: Type the complete proteolipid membrane as a composite constituent

minor / open / confirmed; issue key: CellStructureMech-bacterial_outer_membrane_vesicle-composite-proteolipid-type.

components[0] explicitly denotes the complete OMV bilayer mixture including outer-membrane proteins, LPS and phospholipids, yet component_type is LIPID. The label, role and graph refer to the whole composite membrane, not merely its lipid fraction. OTHER is available and the frozen BEV neighbor uses it for exactly this mixed-membrane distinction.

### plaque-t4-F2: Separate the OMV proteome source from the inflammatory-model source

minor / open / confirmed; issue key: CellStructureMech-bacterial_outer_membrane_vesicle-canonical-proteome-source-placement.

The canonical E. coli note attributes native OMV proteomes and host inflammatory responses to Park2010 alone. Park reports the injection model and comparative protein/LPS profiles; the already cited Lee2007 paper explicitly supplies global proteomic profiling (141 proteins in its complete abstract). The broader biological example is supported, but the two experimental claims need their respective sources.

### plaque-t8-F1: Resolve the exact Cac2 CAF-I subunit family

minor / open / confirmed; issue key: caf1-cac2-family.

IPR045145 is the full Cac2/CHAF1B/FAS2 protein family and is cross-referenced by the verified Cac2 accession Q04199. That exact available family makes the current Cac2 REVIEWED_LABEL_ONLY field and broad unresolved TODO actionable. This finding does not force Cac1 domains or the broader RBAP family onto narrower classes.

### plaque-t9-F1: Ground Skp1 independently of its complex-specific role

minor / open / confirmed; issue key: cbf3-skp1-family.

IPR016897 is the full Skp1 family and is cross-referenced by P52286. The current note withholds grounding because it seeks a CURIE separating CBF3-specific Skp1 from other complex contexts. Protein-class grounding and its source-backed role are separate fields, so that requirement need not prevent this exact identity grounding.

### micro-F1: Ground the DnaA constituent to its verified full family

minor / open / confirmed; issue key: bacterial-prerc-dnaa-family.

IPR001957 identifies the DnaA protein family and is cross-referenced by P03004. The current REVIEWED_LABEL_ONLY note says a family boundary was not curated in that pass; it does not reflect the now-verified exact available term. IPR020591 is broader DnaA/Hda and should not substitute for the exact family.

### micro-F2: Provide an exact source for the named TreS constituent link

minor / open / confirmed; issue key: bindosome-tres-source.

The maintained sugar-binding component names treS alongside glcS/araS, but its cited GO class and Zolghadr2011 article do not name that constituent. Fresh Albers2003 Table2 positively identifies TreS as SSO0999 and its Discussion addresses processing, so zero native symbol-query results cannot imply gene absence. That separately found source is not currently linked beside the claim and does not itself demonstrate TreS in the recovered 400/600 kDa assemblies. Preserve the inherited bounded claim-source gap; establish the specific constituent evidence or explicitly qualify its scope, without requiring deletion or a new optional protein example.

## Recommended Actions And Acceptance Checks

### septin-ap_5_adaptor_complex-A1

In separately authorized curation, assign ap5_beta5_subunit → InterPro:IPR038741, ap5_zeta_subunit → InterPro:IPR028222, ap5_mu5_subunit → InterPro:IPR039591, ap5_sigma5_subunit → InterPro:IPR029392, remove incompatible reviewed-label-only status/notes and close or update the exact-family TODO. Retain the four components, correct examples, UNKNOWN assembly necessity and qualified clathrin/sorting scope. Preserve dated rationale, posed dates, retrieval and curation events; append clarification rather than rewriting them. Record curation remains outside this review-only PR.

- Each mapped accession resolves to its stated AP5-specific family and matches the intended subtype class.
- The four current human identities and constituent roles remain unchanged; no domain or accessory factor replaces a core class.
- Focused schema/strict, protein and graph checks pass after the authorized scientific edit.
- Dated rationale and historical events remain preserved; any authorized record edit adds required history and does not force unsupported universal necessity or broader family identities.

### septin-ap_type_membrane_coat_adaptor_complex-A1

In separately authorized curation, describe the large-chain alternatives with AP5 zeta included and make molecular masses subtype-dependent examples rather than universal limits. Update the corresponding component evidence glosses, preserve the GO identifier and typed hierarchy, and cite the primary AP5 source alongside the ontology while recording the source-native mismatch. Preserve dated rationale, posed dates, retrieval and curation events; append clarification rather than rewriting them. Record curation remains outside this review-only PR.

- The generic description accommodates AP5 beta5/zeta/mu5/sigma5 without changing the supported two-large/mu/sigma architecture.
- Universal110–130kDa and15–20kDa limits are removed or explicitly limited to the appropriate subtype examples; predicted and measured masses are distinguished.
- GO identity, membrane-coat parthood, generic cohort boundaries and UNKNOWN necessity remain intact; focused schema/strict and graph checks pass.
- Dated rationale and historical events remain preserved; any authorized record edit adds required history and does not force unsupported universal necessity or broader family identities.

### plaque-t3-A1

Preserve the exact authority provenance, and qualify the definition or add a definition-adjacent literature-backed note explaining that the record covers multiple bacterial vesicle origins beyond plasma-membrane budding. Keep the nonmechanistic graph and cargo boundary.

- Preserve exact supported identity, experimental organism and native versus recombinant context.
- Attach source-specific evidence to each changed claim and retain historical provenance.
- Native schema, strict, CURIE, protein and graph checks pass as applicable.
- Preserve append-only dated rationale/history; append the current evidence and update active notes/TODO scope. This review PR does not edit records.

### plaque-t4-A1

Retype the explicitly whole proteolipid boundary as OTHER, or deliberately restrict the component to its lipid fraction and separately preserve the whole-membrane actor. Keep the correctly scoped OMV identity and cargo topology.

- Preserve exact supported identity, experimental organism and native versus recombinant context.
- Attach source-specific evidence to each changed claim and retain historical provenance.
- Native schema, strict, CURIE, protein and graph checks pass as applicable.
- Preserve append-only dated rationale/history; append the current evidence and update active notes/TODO scope. This review PR does not edit records.

### plaque-t4-A2

Attach Lee2007 to the proteomic clause using the supported schema/evidence placement, or narrow the Park-only canonical note to its OMV characterization and host-response experiment. Preserve the mouse-isolate/injection context.

- Preserve exact supported identity, experimental organism and native versus recombinant context.
- Attach source-specific evidence to each changed claim and retain historical provenance.
- Native schema, strict, CURIE, protein and graph checks pass as applicable.
- Preserve append-only dated rationale/history; append the current evidence and update active notes/TODO scope. This review PR does not edit records.

### plaque-t8-A1

Ground Cac2 to IPR045145 and reconcile its note/TODO; retain unresolved Cac1 and Msi1 family boundaries and supported complex membership.

- Verify exact family identity and reconcile affected label-only notes and TODO scope.
- Preserve supported examples and membership, with unresolved classes explicitly bounded.
- Use guarded curation and pass applicable schema, strict, protein and graph checks.
- Preserve append-only dated rationale/history; append the current evidence and update active notes/TODO scope. This review PR does not edit records.

### plaque-t9-A1

Ground Skp1 to IPR016897 and retain its CBF3-specific role/evidence separately. Narrow the TODO while leaving domain-only Ctf13/Cep3/Ndc10 candidates unresolved.

- Verify exact family identity and reconcile affected label-only notes and TODO scope.
- Preserve supported examples and membership, with unresolved classes explicitly bounded.
- Use guarded curation and pass applicable schema, strict, protein and graph checks.
- Preserve append-only dated rationale/history; append the current evidence and update active notes/TODO scope. This review PR does not edit records.

### micro-A1

In separately authorized curation, verify/add exact DnaA IPR001957 grounding and update current grounding status/notes; narrow the open prompt/current notes to unresolved oriC grounding. Preserve exact example and generic pre-RC boundary; append to dated rationale rather than replacing historical provenance.

- Verify exact family identity and reconcile affected label-only notes and TODO scope.
- Preserve supported examples and membership, with unresolved classes explicitly bounded.
- Use guarded curation and pass applicable schema, strict, protein and graph checks.
- Retain dated rationale and posed_date; append correction provenance and put current state in notes/prompt.
- This review-only PR edits no scientific records; use guarded writer/history and applicable native validation in separately authorized curation.

### micro-A2

In separately authorized curation, add a verified claim-adjacent source for the exact TreS constituent scope or explicitly qualify what remains uncertain. Consider the fresh positive SSO0999/TreS processing evidence without equating signal processing with mature-complex membership. Preserve GlcS/AraS support and SSO3043/1273/SlaA limitations; no automatic deletion or optional-example requirement follows from a zero-result query.

- Verify the exact gene/protein identity and source-specific bindosome membership; a zero-result query alone is insufficient.
- Place a verified supporting citation beside the exact symbol/component claim or explicitly qualify its bounded scope; removal is warranted only by affirmative curation evidence, not a zero-result query.
- Use guarded curation and pass applicable schema, strict, protein and graph checks.
- Retain dated rationale and posed_date; append correction provenance and put current state in notes/prompt.
- This review-only PR edits no scientific records; use guarded writer/history and applicable native validation in separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| current-record-0 | data/structures/other/ap_5_adaptor_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 d951b48b8f9fe05db066c722dd2dad8277f04eb4af1ac36bf4a5c03932ac82dc; current SHA256 d951b48b8f9fe05db066c722dd2dad8277f04eb4af1ac36bf4a5c03932ac82dc. Record bytes unchanged since the original review. |
| original-review-0 | reviews/structured/20261022T044318Z-ap-5-adaptor-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-1 | data/structures/other/ap_type_membrane_coat_adaptor_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 a16a52e7091df279f222b922baa48be321173ab9dc132e1c2be2384d48ca626b; current SHA256 a16a52e7091df279f222b922baa48be321173ab9dc132e1c2be2384d48ca626b. Record bytes unchanged since the original review. |
| original-review-1 | reviews/structured/20261022T044319Z-ap-type-membrane-coat-adaptor-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-2 | data/structures/other/apical_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 72b670707751292b450e4c8bccddb25a4a14e482fc0eaaa85975681694f55952; current SHA256 72b670707751292b450e4c8bccddb25a4a14e482fc0eaaa85975681694f55952. Record bytes unchanged since the original review. |
| original-review-2 | reviews/structured/20261022T044320Z-apical-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-3 | data/structures/other/bacterial_extracellular_vesicle.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 43f0f6e0dfef8fc8533bbbac4c5a1583adc6626873f52b92f2edbc32560137d2; current SHA256 43f0f6e0dfef8fc8533bbbac4c5a1583adc6626873f52b92f2edbc32560137d2. Record bytes unchanged since the original review. |
| original-review-3 | reviews/structured/20261022T044321Z-bacterial-extracellular-vesicle-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-4 | data/structures/other/bacterial_outer_membrane_vesicle.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 ae635da7dc9351f59de2b4283aa2d572b200cf9eba187147c027e5e86b445a34; current SHA256 ae635da7dc9351f59de2b4283aa2d572b200cf9eba187147c027e5e86b445a34. Record bytes unchanged since the original review. |
| original-review-4 | reviews/structured/20261022T044321Z-bacterial-outer-membrane-vesicle-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-5 | data/structures/other/bacterial_pre_replicative_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 a4a8871a963f0b0eb3e32d9a677f099afdf3f6246dc7964f1890b61b3f01b62a; current SHA256 a4a8871a963f0b0eb3e32d9a677f099afdf3f6246dc7964f1890b61b3f01b62a. Record bytes unchanged since the original review. |
| original-review-5 | reviews/structured/20261022T044322Z-bacterial-pre-replicative-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-6 | data/structures/other/bam_protein_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 caa3620dc7868afb69744609d3f28450d13ce822789d33224fab2e805a49a8dd; current SHA256 ac284bcf4e0ec8021b0f218143e2337a0845c36113edb097e79c950ac1688cde. Changed record reassessed against current sources. |
| original-review-6 | reviews/structured/20261022T044323Z-bam-protein-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-7 | data/structures/other/bindosome_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 b684ece5758180f8afba192ccad06e0938cbda33953c9390eadbbf7ce01fab91; current SHA256 360a186c82ed29ddaae42fdbcb445a37b8482be97bed64a6d077792b8fdce375. Changed record reassessed against current sources. |
| original-review-7 | reviews/structured/20261022T044323Z-bindosome-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-8 | data/structures/other/caf_1_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 9cfaf9ce52f019ddb3125428f3c6ce7cb17ae2e476fbd0fb9be2e0bcad652576; current SHA256 9cfaf9ce52f019ddb3125428f3c6ce7cb17ae2e476fbd0fb9be2e0bcad652576. Record bytes unchanged since the original review. |
| original-review-8 | reviews/structured/20261022T044324Z-caf-1-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-9 | data/structures/other/cbf3_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 8afa05438831e653a16909b6f127778342b1de47b324a3994c5f374937d9829a; current SHA256 9cf3d32f5094ac6a00417cb7b7c125b45a4329e364d8e721314f19349baf44f2. Changed record reassessed against current sources. |
| original-review-9 | reviews/structured/20261022T044325Z-cbf3-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| septin-review-policy | .claude/skills/review-yaml-record/SKILL.md; Complete scientific/source review; structured molecular source checks | supports | Positive molecular and pathway assertions anywhere in a record trigger actual structured-source applicability assessment; expression-only exclusions are insufficient. |
| septin-curation-policy | docs/CURATION.md; Family/class constituents, grounding status, formation necessity, append-only rationale | supports | Protein classes are permitted; exact assertable family grounding differs from reviewed-label-only status. Missing optional examples are not automatically defects. Dated rationale/history remain append-only. |
| septin-schema-policy | src/cellstructuremech/schema/cellstructuremech.yaml; Component grounding_status, formation essentiality, graph nodes and scope | supports | Family/class and complex representations are allowed. Verified identifiers must denote the stated class. UNKNOWN formation necessity and explicitly nonmechanistic functional graphs must not be inflated. |
| septin-protein-policy | .claude/skills/uniprot-protein-examples/SKILL.md; Primary/synonym identity, taxon/reviewed status, bounded queries, representative selection | supports | Native accession and gene-query coverage do not independently establish experimental localization or universal necessity. Queries are bounded observations, not reconstructed historical executions. |
| septin-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; FUNCTION/NONMECHANISTIC scope and evidence placement | supports | Coarse structural and functional summaries do not certify an experimentally resolved assembly cycle or individual subunit necessity. |
| septin-literature-policy | .claude/skills/literature-evidence/SKILL.md; Primary sources, abstract/body/pixel scope and source failure | supports | Access tier and actual read extents must be explicit; challenge pages and metadata cannot certify unread experimental details. |
| septin-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0044599,GO:0030119,GO:0098796,GO:0030117,GO:0020007,GO:0020010,GO:0020031,GO:0020008,GO:0020009; All nine requested term objects: exact identifiers, labels, complete definitions and relevant typed hierarchy relations | supports | GO0044599 is exact AP5 and child of GO0030119; the generic parent retains an outdated exhaustive subunit/mass gloss despite including AP5. GO0020007 is the apical composite with conoid, polar-ring, rhoptry and microneme relations. GO0020031 label/aliases and definition show the bounded preconoidal-ring versus APR tension discussed separately; no replacement identifier is guessed. |
| septin-catalogue | https://imodulondb.org/api/datasets; Complete returned official datasets catalogue; all organism/dataset rows inspected | supports | No native human, Tetrahymena or Toxoplasma/Apicomplexa host dataset occurs in this returned catalogue. Bacterial recombinant production or heterologous yeast assays are not substitutes. Downstream matched-module queries are not applicable after this bounded coverage assessment; lack of coverage is not biological absence. |
| septin-tax9606 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/9606; Complete ENA taxonomy object: taxonId, scientificName, rank and lineage | supports | Exact identities/ranks distinguish human species9606, Tetrahymena thermophila species5911, Apicomplexa phylum5794 and Toxoplasma gondii species5811. Taxonomy does not establish quantitative prevalence or the strain used in a particular experiment. |
| septin-tax5911 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5911; Complete ENA taxonomy object: taxonId, scientificName, rank and lineage | supports | Exact identities/ranks distinguish human species9606, Tetrahymena thermophila species5911, Apicomplexa phylum5794 and Toxoplasma gondii species5811. Taxonomy does not establish quantitative prevalence or the strain used in a particular experiment. |
| septin-tax5794 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5794; Complete ENA taxonomy object: taxonId, scientificName, rank and lineage | supports | Exact identities/ranks distinguish human species9606, Tetrahymena thermophila species5911, Apicomplexa phylum5794 and Toxoplasma gondii species5811. Taxonomy does not establish quantitative prevalence or the strain used in a particular experiment. |
| septin-tax5811 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5811; Complete ENA taxonomy object: taxonId, scientificName, rank and lineage | supports | Exact identities/ranks distinguish human species9606, Tetrahymena thermophila species5911, Apicomplexa phylum5794 and Toxoplasma gondii species5811. Taxonomy does not establish quantitative prevalence or the strain used in a particular experiment. |
| septin-protein-Q2VPB7 | https://rest.uniprot.org/uniprotkb/Q2VPB7.json; Native accession identity, recommended/alternative names, gene names, organism/reviewed entryType, sequence mass, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and InterPro cross-references | supports | Reviewed human AP5B1 beta5; primary AP5B1, ORF PP1030; length878 and canonical sequence mass93949Da; exact family IPR038741. Sequence mass is predicted for the canonical protein, not a measured assembled-complex mass; authority identity is not a new localization/necessity experiment. |
| septin-protein-O43299 | https://rest.uniprot.org/uniprotkb/O43299.json; Native accession identity, recommended/alternative names, gene names, organism/reviewed entryType, sequence mass, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and InterPro cross-references | supports | Reviewed human AP5Z1 zeta; primary AP5Z1, synonyms KIAA0415/SPG48; length807 and canonical sequence mass88605Da; exact family IPR028222. Slabicki isoform-specific cytoplasmic/nuclear localization is distinct from a universal AP5 localization claim. Sequence mass is predicted for the canonical protein, not a measured assembled-complex mass; authority identity is not a new localization/necessity experiment. |
| septin-protein-Q9H0R1 | https://rest.uniprot.org/uniprotkb/Q9H0R1.json; Native accession identity, recommended/alternative names, gene names, organism/reviewed entryType, sequence mass, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and InterPro cross-references | supports | Reviewed human AP5M1 mu5; primary AP5M1, synonyms C14orf108/MUDENG; length490 and sequence mass54767Da; exact family IPR039591. Experimental cytosol and inferred late-endosome membrane annotations are distinguished. Sequence mass is predicted for the canonical protein, not a measured assembled-complex mass; authority identity is not a new localization/necessity experiment. |
| septin-protein-Q9NUS5 | https://rest.uniprot.org/uniprotkb/Q9NUS5.json; Native accession identity, recommended/alternative names, gene names, organism/reviewed entryType, sequence mass, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and InterPro cross-references | supports | Reviewed human AP5S1 sigma5; primary AP5S1, synonym C20orf29; length200 and sequence mass22522Da; exact family IPR029392. Experimental cytosol and inferred endosome annotations are distinguished. Sequence mass is predicted for the canonical protein, not a measured assembled-complex mass; authority identity is not a new localization/necessity experiment. |
| septin-gene-AP5B1 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=100&amp;query=%28gene_exact%3AAP5B1%29%20AND%20%28organism_id%3A9606%29%20AND%20%28reviewed%3Atrue%29; Complete returned JSON and result-count/pagination headers | supports | One reviewed human intended primary-gene entry is returned by this current exact query. This supports bounded current identity/uniqueness, not reconstruction of the October retrieval. |
| septin-gene-AP5Z1 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=100&amp;query=%28gene_exact%3AAP5Z1%29%20AND%20%28organism_id%3A9606%29%20AND%20%28reviewed%3Atrue%29; Complete returned JSON and result-count/pagination headers | supports | One reviewed human intended primary-gene entry is returned by this current exact query. This supports bounded current identity/uniqueness, not reconstruction of the October retrieval. |
| septin-gene-AP5M1 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=100&amp;query=%28gene_exact%3AAP5M1%29%20AND%20%28organism_id%3A9606%29%20AND%20%28reviewed%3Atrue%29; Complete returned JSON and result-count/pagination headers | supports | One reviewed human intended primary-gene entry is returned by this current exact query. This supports bounded current identity/uniqueness, not reconstruction of the October retrieval. |
| septin-gene-AP5S1 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=100&amp;query=%28gene_exact%3AAP5S1%29%20AND%20%28organism_id%3A9606%29%20AND%20%28reviewed%3Atrue%29; Complete returned JSON and result-count/pagination headers | supports | One reviewed human intended primary-gene entry is returned by this current exact query. This supports bounded current identity/uniqueness, not reconstruction of the October retrieval. |
| septin-ipr-IPR038741 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR038741/; Complete native metadata accession/name/type, description, member databases, hierarchy and LLM flags | supports | Exact AP5 beta5 family. Relevant descriptions have false LLM flags. Broad parents/domains are not substituted for exact subtype or pan-adaptor classes. |
| septin-ipr-IPR028222 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR028222/; Complete native metadata accession/name/type, description, member databases, hierarchy and LLM flags | supports | Exact AP5 zeta family. Relevant descriptions have false LLM flags. Broad parents/domains are not substituted for exact subtype or pan-adaptor classes. |
| septin-ipr-IPR039591 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR039591/; Complete native metadata accession/name/type, description, member databases, hierarchy and LLM flags | supports | Exact AP5 mu5 family. Relevant descriptions have false LLM flags. Broad parents/domains are not substituted for exact subtype or pan-adaptor classes. |
| septin-ipr-IPR029392 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR029392/; Complete native metadata accession/name/type, description, member databases, hierarchy and LLM flags | supports | Exact AP5 sigma5 family. Relevant descriptions have false LLM flags. Broad parents/domains are not substituted for exact subtype or pan-adaptor classes. |
| septin-ipr-IPR001392 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001392/; Complete native metadata accession/name/type, description, member databases, hierarchy and LLM flags | supports | Broader AP1/2/3 mu family, not a demonstrated all-AP1–5 exact class. Relevant descriptions have false LLM flags. Broad parents/domains are not substituted for exact subtype or pan-adaptor classes. |
| septin-ipr-IPR016635 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016635/; Complete native metadata accession/name/type, description, member databases, hierarchy and LLM flags | supports | Broader sigma family with AP1/2/3 children, not a demonstrated all-AP1–5 exact class. Relevant descriptions have false LLM flags. Broad parents/domains are not substituted for exact subtype or pan-adaptor classes. |
| septin-ipr-IPR050431 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050431/; Native accession/name/type, member-database identity and description-generation flags | context_only | The entry is family type with PTHR10529 member identity; its description has llm=true, checked=false and is_reviewed_llm=false. Generated prose is not used as independent biological evidence or promoted to a verified pan-AP/stonin mapping. The original already disclosed this limitation. |
| septin-family-search-AP5 | https://www.ebi.ac.uk/interpro/api/entry/interpro/?search=AP-5&amp;page_size=200; All nine returned InterPro candidate objects; next=null | supports | The four exact AP5 families are distinguished from returned domain candidates. This is a bounded candidate search, not a claim that no other relevant entry exists anywhere. |
| septin-hirst2011-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1371/journal.pbio.1001170%22&amp;pageSize=100; Complete unique MED bibliographic metadata, authors, DOI/PMID/PMCID where present and returned abstract | supports | Hirst2011 identifies AP5 with endosomal localization and trafficking phenotypes; full fresh body is separately scoped. |
| septin-pmid-20613862 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A20613862%20AND%20SRC%3AMED&amp;pageSize=100; Complete unique MED bibliographic metadata, authors, DOI/PMID/PMCID where present and returned abstract | supports | Slabicki2010 identifies KIAA0415/SPG48 and interacting proteins; measured isoform localization and coimmunoprecipitation are distinct from its then-putative helicase interpretation, not adopted as a current AP5 mechanism. |
| septin-kaur2017-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1091%2Fmbc.e17-01-0018&amp;format=json&amp;resultType=core&amp;pageSize=100; Complete unique MED bibliographic metadata, authors, DOI/PMID/PMCID where present and returned abstract | supports | Kaur2017 tests Tetrahymena AP3-dependent mature mucocyst biogenesis; initial immature intermediates persist. |
| septin-hu2006-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1371/journal.ppat.0020013%22&amp;pageSize=100; Complete unique MED bibliographic metadata, authors, DOI/PMID/PMCID where present and returned abstract | supports | Hu2006 identifies candidate Toxoplasma cytoskeletal proteins using partial apical-complex enrichment; it is not a purified complete composite-organelle inventory. |
| septin-ren2024-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1073/pnas.2416602121%22&amp;pageSize=100; Complete unique MED bibliographic metadata, authors, DOI/PMID/PMCID where present and returned abstract | supports | Ren2024 experimentally distinguishes APR layers and their motility/invasion roles; it does not establish universal AP-complex-wide secretion coordination. |
| septin-pmid-9208224 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A9208224%20AND%20SRC%3AMED&amp;pageSize=100; Complete unique MED bibliographic metadata, authors, DOI/PMID/PMCID where present and returned abstract | supports | Carruthers/Sibley1997 measures ordered microneme/rhoptry/dense-granule secretion during Toxoplasma host-cell invasion; fresh genuine body scopes are recorded separately. |
| septin-boothroyd2008-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1038%2Fnrmicro1800&amp;pageSize=100; Complete unique MED bibliographic metadata, authors, DOI/PMID/PMCID where present and returned abstract | supports | Boothroyd/Dubremetz2008 is a secondary rhoptry review. Complete MED metadata and abstract only are verified in this pass; no current genuine full body or detailed Key Points is claimed. |
| septin-waller2024-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1128%2Fmmbr.00197-22&amp;pageSize=100; Complete unique MED bibliographic metadata, authors, DOI/PMID/PMCID where present and returned abstract | supports | Waller2024 is a secondary apical-complex review. Complete MED metadata/abstract support bounded comparative/evolutionary context, not a prevalence census or universal stage-specific inventory; current full-body access failed. |
| septin-hirst2011-xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3191125/fullTextXML; Fresh genuine JATS: Introduction s1; Results s2a,b,c,d,f including Figures1–4,8–9 captions and Table1 cells/explanation; Discussion s3 including Figure10 caption; Methods s4c,d,e | supports | HeLaM and tagged/co-IP experiments support AP5 heterotetramer and endosomal sorting implications. Corrected beta5 is878aa/predicted94kDa; zeta/sigma are fourth-complex-chain identities. Endogenous mu antibody was unsuitable for IF; controlled tagged constructs support LAMP1 association. CI-MPR/Vps26 redistribution and swollen MVB/tubules are phenotypes, not a fully resolved cargo route. Tested lack of CCV enrichment/clathrin association is not a universal no-coat theorem. Phylogeny sections, other methods, supplement and figure pixels were not inspected. |
| septin-slabicki2010-xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2893954/fullTextXML; Fresh genuine JATS: Results s2e,s2f with Figures3–6 captions; Methods s4j coimmunoprecipitation/MS and s4k fractionation | supports | Near-physiologic tagged KIAA0415/HeLa experiments distinguish shorter nuclear and longer cytoplasmic isoforms and interacting proteins. This supports the bounded AP5Z1 localization note, not universal cytoplasmic occupancy or a proven helicase mechanism. Other sections, supplements and figure pixels were not audited. |
| septin-kaur2017-xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5449153/fullTextXML; Fresh genuine JATS Results sec3–6 with Figures1–4 captions; Methods sec14/15 | supports | Tetrahymena CU428.1-background macronuclear APM3 knockout remains viable without growth defect but fails normal mature mucocyst biogenesis; immature cargo/protease-bearing intermediates and some docking persist. AP3 is a maturation pathway example, not a stable mature mucocyst subunit. Tagged Apm3 aggregation leaves endogenous localization unresolved; proposed delivery mechanism is hypothetical. No complete Discussion, supplements or figure pixels are claimed in this fresh read. |
| septin-hu2006-xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC1383488/fullTextXML; Fresh genuine JATS Introduction s1 and Figure1 caption; Results s2a/s2b with Figures2/3 captions and Table1/2 explanatory text, not table cells; Methods s4a/s4b | supports | RH tachyzoites cultured in HFF were partially detergent/sonication-fractionated to enrich conoid/apical cytoskeleton; contamination and incomplete recovery limit a whole-composite inventory. Preconoidal rings/conoid fibers are distinguished from APR anchoring subpellicular microtubules. Individual-protein sections, MudPIT methods, Discussion, supplements and figure pixels were not audited. |
| septin-ren2024-xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11573658/fullTextXML; Fresh genuine JATS Results s2–s6 and Figures1–5 captions/Table1 explanatory text; complete Discussion s7; Methods s9 culture and s10 transgenic lines | supports | RH-derived conditional Toxoplasma lines reveal three APR layers and distinguish the ring from the movable conoid. APR2 depletion impairs motility/invasion but leaves tested microneme secretion/rhoptry discharge intact; no blanket secretion-control mechanism follows. Methods are limited to cultures/transgenic construction; other assay methods, table cells, supplements and figure pixels were not inspected. |
| septin-carruthers1997-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC13475723/; Fresh genuine PMC HTML Methods S3–S6, Results S13–S17 with Figures1–6 captions, complete Discussion S19 including Figure8 caption | supports | RH/2F tachyzoites invading HFF, synchronous pulse invasion, selective permeabilization, immunolocalization and secretion assays measure MIC2 release before ROP1, then delayed GRA1/NTPase secretion. This supports source-specific ordered secretion and forming-PV association, not direct control by every apical cytoskeletal element or essentiality of every marker; Discussion explicitly notes ROP1-null in-vitro invasion. Moving-junction and all-Apicomplexa extensions remain broader interpretation/secondary context. Figure pixels, full remaining methods and supplements were not inspected. |
| septin-boothroyd2008-publisher | https://www.nature.com/articles/nrmicro1800; Complete failed-access response classified, 3038 bytes | context_only | HTTP200 publisher challenge rather than scientific body. Context only; no scientific claim derives from this response. Genuine available bodies and bounded native abstracts are identified separately. |
| septin-boothroyd2008-canonical | https://www.nature.com/articles/nrmicro1800?error=cookies_not_supported&amp;code=readonly; Complete failed-access response classified, 3038 bytes | context_only | HTTP200 publisher challenge rather than scientific body. Context only; no scientific claim derives from this response. Genuine available bodies and bounded native abstracts are identified separately. |
| septin-waller2024-xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11653781/fullTextXML; Complete failed-access response classified, 151 bytes | context_only | HTTP500 source retrieval failed. Context only; no scientific claim derives from this response. Genuine available bodies and bounded native abstracts are identified separately. |
| septin-adapter-runner-historical | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical attempted datasets runner receipt, 2026-11-03T00:49:00.848907Z–00:49:00.863225Z | context_only | Historical exit1 PermissionError reading runner pyvenv.cfg. No new runner execution is claimed; fresh official catalogue and native-source fallback are separate observations. |
| septin-original-validation | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-septin/original-checks.json; Actual native validate/render of three original pairs; all38 historical input occurrences | supports | All three original YAMLs validate, render exactly to committed Markdown and match every historical input occurrence at the original frozen revision. All three current target hashes equal their original target input. Historical source/gate observations are not represented as current execution. |
| septin-record-ap_5_adaptor_complex | data/structures/other/ap_5_adaptor_complex.yaml; Complete current record at b82b8b5fcb02d90018a73c0d3d05ede8a2ab161f | supports | All definitions, identifiers, typed relations, components, functions, source notes, examples, graph nodes/edges, discussions and history were read. Current target bytes are nonstale; no maintained image or experimental physical-size property is present. |
| septin-original-ap_5_adaptor_complex | reviews/structured/20261022T044318Z-ap-5-adaptor-complex-audit/review.yaml; Complete original YAML and paired Markdown; exact frozen inputs and original verdict/actions | supports | Original immutable review independently reassessed against current sources; exact historical inputs validated. Current verdict remains needs_curation for its inherited minor finding. |
| septin-native-ap_5_adaptor_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/ap_5_adaptor_complex-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/ap_5_adaptor_complex.yaml --verify; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/ap_5_adaptor_complex-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0. Four reviewed human examples and four COVERED typed core-subunit nodes; current exact queries return their intended primary genes. Native sequence/family identities and experimental localization scopes are verified separately. |
| septin-native-ap_5_adaptor_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/ap_5_adaptor_complex-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/ap_5_adaptor_complex.yaml --causal-graphs; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/ap_5_adaptor_complex-uniprot-causal.log SHA256 0ab5a9e877601b5e064d133c6e06c2d902f314b9c485fcf3447af02d79ff9db8 | supports | Exit0. Four reviewed human examples and four COVERED typed core-subunit nodes; current exact queries return their intended primary genes. Native sequence/family identities and experimental localization scopes are verified separately. |
| septin-record-ap_type_membrane_coat_adaptor_complex | data/structures/other/ap_type_membrane_coat_adaptor_complex.yaml; Complete current record at b82b8b5fcb02d90018a73c0d3d05ede8a2ab161f | supports | All definitions, identifiers, typed relations, components, functions, source notes, examples, graph nodes/edges, discussions and history were read. Current target bytes are nonstale; no maintained image or experimental physical-size property is present. |
| septin-original-ap_type_membrane_coat_adaptor_complex | reviews/structured/20261022T044319Z-ap-type-membrane-coat-adaptor-complex-audit/review.yaml; Complete original YAML and paired Markdown; exact frozen inputs and original verdict/actions | supports | Original immutable review independently reassessed against current sources; exact historical inputs validated. Current verdict remains needs_curation for its inherited minor finding. |
| septin-native-ap_type_membrane_coat_adaptor_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/ap_type_membrane_coat_adaptor_complex-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/ap_type_membrane_coat_adaptor_complex.yaml --verify; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/ap_type_membrane_coat_adaptor_complex-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0. Zero examples and three NO_GENE_SYMBOLS typed protein-class nodes. Passing accession diagnostics do not establish missing optional examples or test an unpopulated inventory. |
| septin-native-ap_type_membrane_coat_adaptor_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/ap_type_membrane_coat_adaptor_complex-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/ap_type_membrane_coat_adaptor_complex.yaml --causal-graphs; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/ap_type_membrane_coat_adaptor_complex-uniprot-causal.log SHA256 cfd777d9caf821e4e33d605f5651778539cefa8b4ee9e7a290e14a7776b4b7cd | supports | Exit0. Zero examples and three NO_GENE_SYMBOLS typed protein-class nodes. Passing accession diagnostics do not establish missing optional examples or test an unpopulated inventory. |
| septin-record-apical_complex | data/structures/other/apical_complex.yaml; Complete current record at b82b8b5fcb02d90018a73c0d3d05ede8a2ab161f | supports | All definitions, identifiers, typed relations, components, functions, source notes, examples, graph nodes/edges, discussions and history were read. Current target bytes are nonstale; no maintained image or experimental physical-size property is present. |
| septin-original-apical_complex | reviews/structured/20261022T044320Z-apical-complex-audit/review.yaml; Complete original YAML and paired Markdown; exact frozen inputs and original verdict/actions | supports | Original immutable review independently reassessed against current sources; exact historical inputs validated. Current verdict remains pass_with_limitations, with no scientific finding invented. |
| septin-native-apical_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/apical_complex-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/apical_complex.yaml --verify; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/apical_complex-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0. Zero protein examples and zero GENE_OR_PROTEIN typed graph nodes. The two broad constituent cohorts are permitted classes; native pass is empty protein-xref coverage and does not independently establish their biology. |
| septin-native-apical_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/apical_complex-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/apical_complex.yaml --causal-graphs; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/apical_complex-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Exit0. Zero protein examples and zero GENE_OR_PROTEIN typed graph nodes. The two broad constituent cohorts are permitted classes; native pass is empty protein-xref coverage and does not independently establish their biology. |
| plaque-current-3 | data/structures/other/bacterial_extracellular_vesicle.yaml; Entire current record at source b82b8b5fcb02d90018a73c0d3d05ede8a2ab161f | supports | Entire record independently read, including all definitions, evidence, components, examples, graph, taxonomic/canonical scopes, discussions and history; not just a protein inventory. |
| plaque-original-3-yaml | reviews/structured/20261022T044321Z-bacterial-extracellular-vesicle-audit/review.yaml; Entire immutable original paired review; historical assertions assessed at their own frozen revision | supports | Original findings, actions, source kinds, limitations, checks and exact historical input references inspected. Historical passed checks are not recast as current validation. |
| plaque-original-3-md | reviews/structured/20261022T044321Z-bacterial-extracellular-vesicle-audit/review.md; Entire immutable original paired review; historical assertions assessed at their own frozen revision | supports | Original findings, actions, source kinds, limitations, checks and exact historical input references inspected. Historical passed checks are not recast as current validation. |
| plaque-current-4 | data/structures/other/bacterial_outer_membrane_vesicle.yaml; Entire current record at source b82b8b5fcb02d90018a73c0d3d05ede8a2ab161f | supports | Entire record independently read, including all definitions, evidence, components, examples, graph, taxonomic/canonical scopes, discussions and history; not just a protein inventory. |
| plaque-original-4-yaml | reviews/structured/20261022T044321Z-bacterial-outer-membrane-vesicle-audit/review.yaml; Entire immutable original paired review; historical assertions assessed at their own frozen revision | supports | Original findings, actions, source kinds, limitations, checks and exact historical input references inspected. Historical passed checks are not recast as current validation. |
| plaque-original-4-md | reviews/structured/20261022T044321Z-bacterial-outer-membrane-vesicle-audit/review.md; Entire immutable original paired review; historical assertions assessed at their own frozen revision | supports | Original findings, actions, source kinds, limitations, checks and exact historical input references inspected. Historical passed checks are not recast as current validation. |
| plaque-current-8 | data/structures/other/caf_1_complex.yaml; Entire current record at source b82b8b5fcb02d90018a73c0d3d05ede8a2ab161f | supports | Entire record independently read, including all definitions, evidence, components, examples, graph, taxonomic/canonical scopes, discussions and history; not just a protein inventory. |
| plaque-original-8-yaml | reviews/structured/20261022T044324Z-caf-1-complex-audit/review.yaml; Entire immutable original paired review; historical assertions assessed at their own frozen revision | supports | Original findings, actions, source kinds, limitations, checks and exact historical input references inspected. Historical passed checks are not recast as current validation. |
| plaque-original-8-md | reviews/structured/20261022T044324Z-caf-1-complex-audit/review.md; Entire immutable original paired review; historical assertions assessed at their own frozen revision | supports | Original findings, actions, source kinds, limitations, checks and exact historical input references inspected. Historical passed checks are not recast as current validation. |
| plaque-current-9 | data/structures/other/cbf3_complex.yaml; Entire current record at source b82b8b5fcb02d90018a73c0d3d05ede8a2ab161f | supports | Entire record independently read, including all definitions, evidence, components, examples, graph, taxonomic/canonical scopes, discussions and history; not just a protein inventory. |
| plaque-original-9-yaml | reviews/structured/20261022T044325Z-cbf3-complex-audit/review.yaml; Entire immutable original paired review; historical assertions assessed at their own frozen revision | supports | Original findings, actions, source kinds, limitations, checks and exact historical input references inspected. Historical passed checks are not recast as current validation. |
| plaque-original-9-md | reviews/structured/20261022T044325Z-cbf3-complex-audit/review.md; Entire immutable original paired review; historical assertions assessed at their own frozen revision | supports | Original findings, actions, source kinds, limitations, checks and exact historical input references inspected. Historical passed checks are not recast as current validation. |
| plaque-policy | docs/CURATION.md; Frozen repository policy/schema, scoped portions independently inspected | supports | Source scope, evidence, component/family grounding, formation-specific necessity and append-only history rules. |
| plaque-review-skill | .claude/skills/review-yaml-record/SKILL.md; Frozen repository policy/schema, scoped portions independently inspected | supports | Whole-record scientific review and explicit structured-source applicability triggers; runner fallback and bounded interpretation. |
| plaque-protein-skill | .claude/skills/uniprot-protein-examples/SKILL.md; Frozen repository policy/schema, scoped portions independently inspected | supports | Exact native identity, gene/locus tokens, entry status, location evidence and graph inventory scope. |
| plaque-schema | src/cellstructuremech/schema/cellstructuremech.yaml; Frozen repository policy/schema, scoped portions independently inspected | supports | Closed native record contract including composite component types and graph component references. |
| plaque-review-schema | schema/record_review.yaml; Frozen repository policy/schema, scoped portions independently inspected | supports | Native evidence/assessment/finding/action enums, exact lineage and bounded search contract. |
| plaque-review-profile | docs/record-review-profile.md; Frozen repository policy/schema, scoped portions independently inspected | supports | Current local review profile and immutable native publication route. |
| plaque-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097691,GO:0061701,GO:1903561,GO:0009279,GO:0033186,GO:0032991,GO:0006334,GO:0031518,GO:0140513,GO:0000775,GO:0000776; GO0097691,0061701,1903561,0009279,0033186,0032991,0006334,0031518,0140513,0000775,0000776; definitions and relevant direct child relations; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/go.raw | supports | Current exact GO terms support four identities, relation scopes and source attribution; BEV definition still specifies plasma-membrane budding whereas OMV specifies outer-membrane-derived proteolipid vesicles. CAF-I heterotrimer and CBF3 four protein classes are explicit. |
| plaque-SL0489 | https://rest.uniprot.org/locations/SL-0489.json; Full location entry, definition, synonyms and GO links; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/SL0489.raw | supports | Native bacterial membrane vesicle location and synonyms were read; its plasma-membrane wording does not independently reconcile every broader vesicle-origin class. |
| plaque-tax-2 | https://rest.uniprot.org/taxonomy/2.json; taxonId/scientificName/rank/parent fields; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/tax-2.raw | supports | Current taxonomy identity/parent inspected: Bacteria domain. |
| plaque-tax-1280 | https://rest.uniprot.org/taxonomy/1280.json; taxonId/scientificName/rank/parent fields; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/tax-1280.raw | supports | Current taxonomy identity/parent inspected: Staphylococcus aureus species. |
| plaque-tax-562 | https://rest.uniprot.org/taxonomy/562.json; taxonId/scientificName/rank/parent fields; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/tax-562.raw | supports | Current taxonomy identity/parent inspected: Escherichia coli species. |
| plaque-tax-4932 | https://rest.uniprot.org/taxonomy/4932.json; taxonId/scientificName/rank/parent fields; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/tax-4932.raw | supports | Current taxonomy identity/parent inspected: Saccharomyces cerevisiae species. |
| plaque-tax-559292 | https://rest.uniprot.org/taxonomy/559292.json; taxonId/scientificName/rank/parent fields; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/tax-559292.raw | supports | Current taxonomy identity/parent inspected: S. cerevisiae S288c strain below species4932. |
| plaque-toyofuku2019-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038%2Fs41579-018-0112-2&amp;format=json&amp;resultType=core&amp;pageSize=1; Europe PMC exact DOI query, one matched MED record, complete abstract; secondary tier; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/toyofuku2019-meta.raw | supports | Complete indexed abstract and bibliographic identity inspected; this is a secondary review, not an independent experimental body. The abstract explicitly distinguishes outer-membrane blebbing and lysis-derived routes in Gram-negative and Gram-positive bacteria. |
| plaque-kim2015-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1016%2Fj.semcdb.2015.02.006&amp;format=json&amp;resultType=core&amp;pageSize=1; Europe PMC exact DOI query, one matched MED record, complete abstract; secondary tier; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/kim2015-meta.raw | supports | Complete indexed abstract and bibliographic identity inspected; this is a secondary review, not an independent experimental body. Broad bacterial-vesicle composition/cargo and interaction overview. |
| plaque-schwechheimer2015-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038%2Fnrmicro3525&amp;format=json&amp;resultType=core&amp;pageSize=1; Europe PMC exact DOI query, one matched MED record, complete abstract; secondary tier; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/schwechheimer2015-meta.raw | supports | Complete indexed abstract and bibliographic identity inspected; this is a secondary review, not an independent experimental body. OMV biogenesis, cargo and functions overview; separate genuine body inspected below. |
| plaque-lee2009-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1002%2Fpmic.200900338&amp;format=json&amp;resultType=core&amp;pageSize=1; Exact DOI query; complete primary abstract and bibliographic metadata, not an unread full body; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/lee2009-meta.raw | supports | Primary complete abstract reports S. aureus membrane vesicles and 90 identified proteins; the abstract does not establish a precise experimental strain here. |
| plaque-lee2007-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1002%2Fpmic.200700196&amp;format=json&amp;resultType=core&amp;pageSize=1; Exact DOI query; complete primary abstract and bibliographic metadata, not an unread full body; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/lee2007-meta.raw | supports | Primary complete abstract reports global E. coli OMV proteomics:141 proteins across two analyses, distinct from Park comparative gels. No full Methods or strain certification is claimed. |
| plaque-park2010-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1371%2Fjournal.pone.0011334&amp;format=json&amp;resultType=core&amp;pageSize=1; Exact DOI query; complete primary abstract and bibliographic metadata, not an unread full body; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/park2010-meta.raw | supports | Primary bibliographic identity and full abstract of intestinal E. coli OMV mouse injection model. |
| plaque-kaufman1997-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1101%2Fgad.11.3.345&amp;format=json&amp;resultType=core&amp;pageSize=1; Exact DOI query; complete primary abstract and bibliographic metadata, not an unread full body; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/kaufman1997-meta.raw | supports | Primary bibliographic identity and abstract of purified yeast CAF-I and nucleosome assembly; genuine PDF text separately inspected. |
| plaque-leber2018-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.15252%2Fembj.201798134&amp;format=json&amp;resultType=core&amp;pageSize=1; Exact DOI query; complete primary abstract and bibliographic metadata, not an unread full body; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/leber2018-meta.raw | supports | Primary bibliographic identity and abstract of the CBF3 core cryo-EM study. |
| plaque-yan2018-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038%2Fs41594-018-0154-1&amp;format=json&amp;resultType=core&amp;pageSize=1; Exact DOI query; complete primary abstract and bibliographic metadata, not an unread full body; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/yan2018-meta.raw | supports | Primary bibliographic identity and abstract of full CBF3–CEN3 structure; deposition claims remain model-scoped. |
| plaque-pmid-11238915 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11238915+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=1; Exact PMID query, complete primary abstract; one MED match; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/pmid-11238915.raw | supports | Johnston2001 abstract explicitly separates Msi1 cytoplasmic/RAS functions from CAF-I; native P13712 location joins inspected separately. |
| plaque-pmid-14562095 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=1; Exact PMID query, complete primary abstract; one MED match; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/pmid-14562095.raw | supports | Huh2003 full indexed abstract is a global localization screen; specific Skp1 location joined from native UniProt annotation, not inferred from the generic abstract. |
| plaque-pmid-10427094 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10427094+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=1; Exact PMID query, complete primary abstract; one MED match; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/pmid-10427094.raw | supports | Zeng1999 full abstract mainly concerns Slk19/Kar3; native Ndc10 location join and specific Cbf2-GFP body methods checked separately. |
| plaque-pmid-9030687 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9030687+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=1; Exact PMID query, complete primary abstract; one MED match; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/pmid-9030687.raw | supports | Kaufman1997 exact PMID bibliographic/abstract corroboration. |
| plaque-up-Q12495 | https://rest.uniprot.org/uniprotkb/Q12495.json; Complete native JSON; entryType/accession/name/genes/organism; relevant comments and crossreferences; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/up-Q12495.raw | supports | Full current reviewed entry identity, primary accession, recommended protein label, gene/alias/locus tokens, taxon559292, relevant FUNCTION/SUBUNIT/SUBCELLULAR LOCATION and InterPro crossreferences inspected. Primary token RLF2; localization/identity is not independent formation-necessity evidence. |
| plaque-up-Q04199 | https://rest.uniprot.org/uniprotkb/Q04199.json; Complete native JSON; entryType/accession/name/genes/organism; relevant comments and crossreferences; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/up-Q04199.raw | supports | Full current reviewed entry identity, primary accession, recommended protein label, gene/alias/locus tokens, taxon559292, relevant FUNCTION/SUBUNIT/SUBCELLULAR LOCATION and InterPro crossreferences inspected. Primary token CAC2; localization/identity is not independent formation-necessity evidence. |
| plaque-up-P13712 | https://rest.uniprot.org/uniprotkb/P13712.json; Complete native JSON; entryType/accession/name/genes/organism; relevant comments and crossreferences; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/up-P13712.raw | supports | Full current reviewed entry identity, primary accession, recommended protein label, gene/alias/locus tokens, taxon559292, relevant FUNCTION/SUBUNIT/SUBCELLULAR LOCATION and InterPro crossreferences inspected. Primary token MSI1; localization/identity is not independent formation-necessity evidence. |
| plaque-up-P35203 | https://rest.uniprot.org/uniprotkb/P35203.json; Complete native JSON; entryType/accession/name/genes/organism; relevant comments and crossreferences; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/up-P35203.raw | supports | Full current reviewed entry identity, primary accession, recommended protein label, gene/alias/locus tokens, taxon559292, relevant FUNCTION/SUBUNIT/SUBCELLULAR LOCATION and InterPro crossreferences inspected. Primary token CTF13; localization/identity is not independent formation-necessity evidence. |
| plaque-up-P52286 | https://rest.uniprot.org/uniprotkb/P52286.json; Complete native JSON; entryType/accession/name/genes/organism; relevant comments and crossreferences; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/up-P52286.raw | supports | Full current reviewed entry identity, primary accession, recommended protein label, gene/alias/locus tokens, taxon559292, relevant FUNCTION/SUBUNIT/SUBCELLULAR LOCATION and InterPro crossreferences inspected. Primary token SKP1; localization/identity is not independent formation-necessity evidence. |
| plaque-up-P40969 | https://rest.uniprot.org/uniprotkb/P40969.json; Complete native JSON; entryType/accession/name/genes/organism; relevant comments and crossreferences; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/up-P40969.raw | supports | Full current reviewed entry identity, primary accession, recommended protein label, gene/alias/locus tokens, taxon559292, relevant FUNCTION/SUBUNIT/SUBCELLULAR LOCATION and InterPro crossreferences inspected. Primary token CEP3; localization/identity is not independent formation-necessity evidence. |
| plaque-up-P32504 | https://rest.uniprot.org/uniprotkb/P32504.json; Complete native JSON; entryType/accession/name/genes/organism; relevant comments and crossreferences; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/up-P32504.raw | supports | Full current reviewed entry identity, primary accession, recommended protein label, gene/alias/locus tokens, taxon559292, relevant FUNCTION/SUBUNIT/SUBCELLULAR LOCATION and InterPro crossreferences inspected. Primary token CBF2; localization/identity is not independent formation-necessity evidence. |
| plaque-gene-CAC1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACAC1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=25; UniProt complete returned query result; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/gene-CAC1.raw | supports | Exactly one returned reviewed S288c entry; its actual primary/alias/locus tokens checked independently against the full entry, rather than trusting index retrieval. |
| plaque-gene-CAC2 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACAC2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=25; UniProt complete returned query result; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/gene-CAC2.raw | supports | Exactly one returned reviewed S288c entry; its actual primary/alias/locus tokens checked independently against the full entry, rather than trusting index retrieval. |
| plaque-gene-MSI1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AMSI1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=25; UniProt complete returned query result; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/gene-MSI1.raw | supports | Exactly one returned reviewed S288c entry; its actual primary/alias/locus tokens checked independently against the full entry, rather than trusting index retrieval. |
| plaque-gene-CTF13 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACTF13%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=25; UniProt complete returned query result; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/gene-CTF13.raw | supports | Exactly one returned reviewed S288c entry; its actual primary/alias/locus tokens checked independently against the full entry, rather than trusting index retrieval. |
| plaque-gene-SKP1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASKP1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=25; UniProt complete returned query result; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/gene-SKP1.raw | supports | Exactly one returned reviewed S288c entry; its actual primary/alias/locus tokens checked independently against the full entry, rather than trusting index retrieval. |
| plaque-gene-CEP3 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACEP3%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=25; UniProt complete returned query result; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/gene-CEP3.raw | supports | Exactly one returned reviewed S288c entry; its actual primary/alias/locus tokens checked independently against the full entry, rather than trusting index retrieval. |
| plaque-gene-NDC10 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ANDC10%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=25; UniProt complete returned query result; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/gene-NDC10.raw | supports | Exactly one returned reviewed S288c entry; its actual primary/alias/locus tokens checked independently against the full entry, rather than trusting index retrieval. |
| plaque-ipr-IPR045145 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR045145/; Exact InterPro entry metadata, hierarchy and type; bounds distinguish family/domain/general paralog class; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/ipr-IPR045145.raw | supports | Native accession, name and type inspected: {'name': 'Chromatin assembly factor 1 subunit Cac2/CHAF1B/FAS2', 'short': 'PTHR15271'} (family). IPR045145 is full Cac2/CHAF1B/FAS2 family, IPR016897 full Skp1; broader IPR001232 and domain-only candidates are not substituted. Generated descriptive prose is not treated as primary mechanism evidence. |
| plaque-ipr-IPR016897 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016897/; Exact InterPro entry metadata, hierarchy and type; bounds distinguish family/domain/general paralog class; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/ipr-IPR016897.raw | supports | Native accession, name and type inspected: {'name': 'S-phase kinase-associated protein 1', 'short': 'SKP1'} (family). IPR045145 is full Cac2/CHAF1B/FAS2 family, IPR016897 full Skp1; broader IPR001232 and domain-only candidates are not substituted. Generated descriptive prose is not treated as primary mechanism evidence. |
| plaque-ipr-IPR001232 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001232/; Exact InterPro entry metadata, hierarchy and type; bounds distinguish family/domain/general paralog class; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/ipr-IPR001232.raw | supports | Native accession, name and type inspected: {'name': 'S-phase kinase-associated protein 1-like', 'short': 'SKP1-like'} (family). IPR045145 is full Cac2/CHAF1B/FAS2 family, IPR016897 full Skp1; broader IPR001232 and domain-only candidates are not substituted. Generated descriptive prose is not treated as primary mechanism evidence. |
| plaque-ipr-IPR031760 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR031760/; Exact InterPro entry metadata, hierarchy and type; bounds distinguish family/domain/general paralog class; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/ipr-IPR031760.raw | supports | Native accession, name and type inspected: {'name': 'Centromere DNA-binding protein complex CBF3 subunit B, C-terminal', 'short': 'Cep3_C'} (domain). IPR045145 is full Cac2/CHAF1B/FAS2 family, IPR016897 full Skp1; broader IPR001232 and domain-only candidates are not substituted. Generated descriptive prose is not treated as primary mechanism evidence. |
| plaque-ipr-IPR022210 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR022210/; Exact InterPro entry metadata, hierarchy and type; bounds distinguish family/domain/general paralog class; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/ipr-IPR022210.raw | supports | Native accession, name and type inspected: {'name': 'Transcription activator GCR1-like domain', 'short': 'TF_GCR1-like'} (domain). IPR045145 is full Cac2/CHAF1B/FAS2 family, IPR016897 full Skp1; broader IPR001232 and domain-only candidates are not substituted. Generated descriptive prose is not treated as primary mechanism evidence. |
| plaque-ipr-IPR062588 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR062588/; Exact InterPro entry metadata, hierarchy and type; bounds distinguish family/domain/general paralog class; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/ipr-IPR062588.raw | supports | Native accession, name and type inspected: {'name': 'CTF13, N-terminal domain', 'short': 'CTF13_N'} (domain). IPR045145 is full Cac2/CHAF1B/FAS2 family, IPR016897 full Skp1; broader IPR001232 and domain-only candidates are not substituted. Generated descriptive prose is not treated as primary mechanism evidence. |
| plaque-ipr-IPR063542 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR063542/; Exact InterPro entry metadata, hierarchy and type; bounds distinguish family/domain/general paralog class; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/ipr-IPR063542.raw | supports | Native accession, name and type inspected: {'name': 'CTF13, C-terminal domain', 'short': 'CTF13_C'} (domain). IPR045145 is full Cac2/CHAF1B/FAS2 family, IPR016897 full Skp1; broader IPR001232 and domain-only candidates are not substituted. Generated descriptive prose is not treated as primary mechanism evidence. |
| plaque-ipr-IPR050459 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050459/; Exact InterPro entry metadata, hierarchy and type; bounds distinguish family/domain/general paralog class; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/ipr-IPR050459.raw | supports | Native accession, name and type inspected: {'name': 'WD repeat RBAP46/RBAP48/MSI1', 'short': 'WD_repeat_RBAP46/RBAP48/MSI1'} (family). IPR045145 is full Cac2/CHAF1B/FAS2 family, IPR016897 full Skp1; broader IPR001232 and domain-only candidates are not substituted. Generated descriptive prose is not treated as primary mechanism evidence. |
| plaque-ipr-IPR048800 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR048800/; Exact InterPro entry metadata, hierarchy and type; bounds distinguish family/domain/general paralog class; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/ipr-IPR048800.raw | supports | Native accession, name and type inspected: {'name': 'Chromatin assembly factor 1 subunit Cac1-like, C-terminal domain', 'short': 'Cac1-like_C'} (domain). IPR045145 is full Cac2/CHAF1B/FAS2 family, IPR016897 full Skp1; broader IPR001232 and domain-only candidates are not substituted. Generated descriptive prose is not treated as primary mechanism evidence. |
| plaque-ipr-IPR021644 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR021644/; Exact InterPro entry metadata, hierarchy and type; bounds distinguish family/domain/general paralog class; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/ipr-IPR021644.raw | supports | Native accession, name and type inspected: {'name': 'Chromatin assembly factor 1 p150 subunit, acidic region', 'short': 'CAF-1_p150_acidic'} (domain). IPR045145 is full Cac2/CHAF1B/FAS2 family, IPR016897 full Skp1; broader IPR001232 and domain-only candidates are not substituted. Generated descriptive prose is not treated as primary mechanism evidence. |
| plaque-ipr-IPR022043 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR022043/; Exact InterPro entry metadata, hierarchy and type; bounds distinguish family/domain/general paralog class; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/ipr-IPR022043.raw | supports | Native accession, name and type inspected: {'name': 'Chromatin assembly factor 1 subunit A, dimerization domain', 'short': 'CAF1A_DD'} (domain). IPR045145 is full Cac2/CHAF1B/FAS2 family, IPR016897 full Skp1; broader IPR001232 and domain-only candidates are not substituted. Generated descriptive prose is not treated as primary mechanism evidence. |
| plaque-PMC5771398-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC5771398.1/PMC5771398.1.xml; JATS secs0003,0005,0006,0007,0012: expression/core, Ctf13 fold, Skp1 interaction, intersubunit interfaces and purification; embedded text captions only, no pixel inspection; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/PMC5771398-jats.raw | supports | Leber primary body independently distinguishes coexpressed full Ndc10(2):Cep3(2):Ctf13(1):Skp1(1) preparation from the Ndc10-dissociated core used for cryo-EM. Ctf13/Skp1 heterodimer contacts Cep3 dimer. Source supports new membership edges without asserting core maps resolved Ndc10. |
| plaque-PMC6292502-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC6292502.1/PMC6292502.1.xml; JATS S2 overall architecture, S3 CEN3 dimer interaction, S7 cloning/expression/purification; no figure pixels or raw coordinate analysis; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/PMC6292502-jats.raw | supports | Yan full CBF3–CEN3 body and Methods support four-class complex, central Ndc10 dimer, Ctf13 interface and centromeric DNA recognition; Cse4 deposition is a proposed model. Yeast genes expressed in Hi5 cells; this is not an endogenous S288c localization or depletion assay. |
| plaque-PMC2893157-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC2893157.1/PMC2893157.1.xml; JATS s2 including embedded Fig1–6 text captions, s3a/b/c/e Methods; no image pixels, no K-12 strain equivalence; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/PMC2893157-jats.raw | supports | Park primary Results/Discussion and Methods show an intestinal mouse CLP E. coli isolate identified by16S, OMV preparations, injection-induced inflammation and comparative Coomassie protein/LPS profiles. No global141-protein identification experiment here; that belongs to Lee2007. |
| plaque-PMC5308417-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC5308417.1/PMC5308417.1.xml; Secondary review JATS S4 complete protein-cargo subsection and children,S9 bacterial communities,S14 virulence delivery; not primary evidence; no figures inspected; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/PMC5308417-jats.raw | supports | Genuine secondary review body distinguishes variable OMV proteome, cargo selection/purification limits, external versus luminal association and species-specific delivery/community examples. It contextualizes the broad nonmechanistic transport graph, not an independent assay for all bacteria. |
| plaque-PMC3206577-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC3206577.1/PMC3206577.1.xml; CBF2–GFP Fusion Plasmids Methods and Results section Slk19p Is Located...; no pixel inspection; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/PMC3206577-jats.raw | supports | Primary CBF2–GFP construct methods describe functional complementation; bounded localization Results concern Slk19/Kar3 and are not misattributed wholesale to Ndc10. Exact Ndc10 nucleus attribution is retained from native P32504 annotation. |
| plaque-kaufman1997-pdf-download | https://genesdev.cshlp.org/content/11/3/345.full.pdf?download=1; Official PDF bytes start %PDF; pdftotext text pages345–347 and354, text Fig1 caption; no figure pixels or exhaustive whole-PDF claim; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/kaufman1997-pdf-download.raw | supports | Genuine official PDF independently read: pages345–347 abstract/introduction and purification Results establish yeast p90/p60/p50 cosedimentation/peptide identification and replication-preferential nucleosome assembly; page354 Methods uses BJ926 purification, W303 genetic backgrounds, human histones and SV40 assay. Current S288c identity examples are not asserted to be those experimental strains. |
| plaque-kaufman1997-pdf | https://genesdev.cshlp.org/content/11/3/345.full.pdf; Exact attempted route and returned response; access context only; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/kaufman1997-pdf.raw | context_only | Initial official PDF route returned403 HTML challenge; later query-qualified official PDF succeeded, so no final unreadability claim. |
| plaque-kaufman1997-html | https://genesdev.cshlp.org/content/11/3/345.full; Exact attempted route and returned response; access context only; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/kaufman1997-html.raw | context_only | Publisher landing/citation shell lacks full article body; not body evidence. |
| plaque-kaufman1997-pdf-html | https://genesdev.cshlp.org/content/11/3/345.full.pdf+html; Exact attempted route and returned response; access context only; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/kaufman1997-pdf-html.raw | context_only | Wrapper route is not the independently inspected PDF. |
| plaque-PMC86735-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC86735.1/PMC86735.1.xml; Exact attempted route and returned response; access context only; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/PMC86735-jats.raw | context_only | Guessed official S3 revision returned404; PMID11238915 abstract and native annotation remain the declared tiers. |
| plaque-toyofuku2019-publisher | https://api.crossref.org/v1/works/10.1038%2Fs41579-018-0112-2/transform; Exact attempted route and returned response; access context only; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/toyofuku2019-publisher.raw | context_only | DOI route429; current scientific assessment uses complete indexed secondary abstract only. |
| plaque-adapter-sa-staph_precise108-genes | https://imodulondb.org/api/datasets/s_aureus/staph_precise108/genes; Exact attempted route and returned response; access context only; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/adapter-sa-staph_precise108-genes.raw | context_only | Path-style genes route returned915-byte frontend HTML, not a gene table; corrected query endpoint used separately. |
| plaque-adapter-sa-staph_precise165-genes | https://imodulondb.org/api/datasets/s_aureus/staph_precise165/genes; Exact attempted route and returned response; access context only; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/adapter-sa-staph_precise165-genes.raw | context_only | Path-style genes route returned915-byte frontend HTML, not a gene table; corrected query endpoint used separately. |
| plaque-kim2015-publisher | https://api.crossref.org/v1/works/10.1016%2Fj.semcdb.2015.02.006/transform; Exact Crossref transform response and bibliographic identity; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/kim2015-publisher.raw | context_only | DOI content negotiation yielded Crossref JSON metadata/abstract rather than publisher full text. No full-body claim is based on this response. |
| plaque-lee2009-publisher | https://api.crossref.org/v1/works/10.1002%2Fpmic.200900338/transform; Exact Crossref transform response and bibliographic identity; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/lee2009-publisher.raw | context_only | DOI content negotiation yielded Crossref JSON metadata/abstract rather than publisher full text. No full-body claim is based on this response. |
| plaque-lee2007-publisher | https://api.crossref.org/v1/works/10.1002%2Fpmic.200700196/transform; Exact Crossref transform response and bibliographic identity; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/lee2007-publisher.raw | context_only | DOI content negotiation yielded Crossref JSON metadata/abstract rather than publisher full text. No full-body claim is based on this response. |
| plaque-catalogue | https://imodulondb.org/api/datasets; Complete20-organism/28 organism-dataset-pair response; independently reread peer-fetched snapshot at its actual timestamp; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/catalogue.raw | supports | Complete current official catalogue has E. coli and S. aureus datasets, but no Saccharomyces row. Whole-record molecular/pathway triggers were assessed before the taxon-limited conclusion; lack of yeast coverage is not biological absence. |
| plaque-ecoli-meta | https://imodulondb.org/api/datasets/e_coli/precise1k/meta; Complete official metadata; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/ecoli-meta.raw | supports | precise1k metadata lists BW25113,DGF-298,GMOS,MG1655,W3110; no equivalence to the Park CLP intestinal isolate is asserted. |
| plaque-ecoli-genes | https://imodulondb.org/api/genes?organism=e_coli&amp;dataset=precise1k&amp;limit=10000; Complete requested table limit10000; exact gene_name/gene_product fields and selected loci; generated prose excluded; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/ecoli-genes.raw | supports | Full4257-row returned gene table inspected through bounded literal-query fields and selected ompA/b0957 and ompF/b0929 annotations; STRING511145 locus context retained. No vesicle localization is inferred. |
| plaque-ecoli-modules | https://imodulondb.org/api/datasets/e_coli/precise1k/imodulons; Complete module list metadata; no generated AI summaries; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/ecoli-modules.raw | supports | Complete201-module metadata queried only for bounded vesicle/outer membrane/cargo strings; module names/functions are expression context. |
| plaque-adapter-sa-staph_precise108-meta | https://imodulondb.org/api/datasets/s_aureus/staph_precise108/meta; Full official response; metadata strain list or bounded gene/module fields; generated prose excluded; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/adapter-sa-staph_precise108-meta.raw | supports | Current S. aureus staph_precise108 meta response independently inspected for exact strains and bounded vesicle/cargo context. USA300-related dataset strains are not substituted for the unverified strain of Lee2009; no absent biology is inferred. |
| plaque-adapter-sa-staph_precise108-imodulons | https://imodulondb.org/api/datasets/s_aureus/staph_precise108/imodulons; Full official response; metadata strain list or bounded gene/module fields; generated prose excluded; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/adapter-sa-staph_precise108-imodulons.raw | supports | Current S. aureus staph_precise108 imodulons response independently inspected for exact strains and bounded vesicle/cargo context. USA300-related dataset strains are not substituted for the unverified strain of Lee2009; no absent biology is inferred. |
| plaque-adapter-sa-staph_precise108-genes-query | https://imodulondb.org/api/genes?organism=s_aureus&amp;dataset=staph_precise108&amp;limit=10000; Full official response; metadata strain list or bounded gene/module fields; generated prose excluded; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/adapter-sa-staph_precise108-genes-query.raw | supports | Current S. aureus staph_precise108 genes-query response independently inspected for exact strains and bounded vesicle/cargo context. USA300-related dataset strains are not substituted for the unverified strain of Lee2009; no absent biology is inferred. |
| plaque-adapter-sa-staph_precise165-meta | https://imodulondb.org/api/datasets/s_aureus/staph_precise165/meta; Full official response; metadata strain list or bounded gene/module fields; generated prose excluded; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/adapter-sa-staph_precise165-meta.raw | supports | Current S. aureus staph_precise165 meta response independently inspected for exact strains and bounded vesicle/cargo context. USA300-related dataset strains are not substituted for the unverified strain of Lee2009; no absent biology is inferred. |
| plaque-adapter-sa-staph_precise165-imodulons | https://imodulondb.org/api/datasets/s_aureus/staph_precise165/imodulons; Full official response; metadata strain list or bounded gene/module fields; generated prose excluded; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/adapter-sa-staph_precise165-imodulons.raw | supports | Current S. aureus staph_precise165 imodulons response independently inspected for exact strains and bounded vesicle/cargo context. USA300-related dataset strains are not substituted for the unverified strain of Lee2009; no absent biology is inferred. |
| plaque-adapter-sa-staph_precise165-genes-query | https://imodulondb.org/api/genes?organism=s_aureus&amp;dataset=staph_precise165&amp;limit=10000; Full official response; metadata strain list or bounded gene/module fields; generated prose excluded; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/adapter-sa-staph_precise165-genes-query.raw | supports | Current S. aureus staph_precise165 genes-query response independently inspected for exact strains and bounded vesicle/cargo context. USA300-related dataset strains are not substituted for the unverified strain of Lee2009; no absent biology is inferred. |
| plaque-adapter-bounded-search | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/adapter-bounded-results.json; Complete selected gene and module responses bound by SHA; literal-query matches retained in scratch | context_only | Queries vesicle/outer membrane/cargo return no literal vesicle/cargo module hits;57 E. coli gene annotations match outer membrane. No S. aureus literal matches in these selected fields. These are bounded annotation results, not absence of vesicles or mechanisms. |
| plaque-adapter-ecoli-b0957-modules | https://imodulondb.org/api/genes/b0957/imodulons?organism=e_coli&amp;dataset=precise1k; Complete selected-locus membership response; weights,thresholds,flags; matched K-12 context only; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/adapter-ecoli-b0957-modules.raw | supports | All201 selected gene-module rows read. ompA has no true membership flags in this dataset; this is not protein absence. Selected because Park discusses OmpA/OmpF as contextual outer-membrane cargo, not because the maintained record asserts these exact genes. |
| plaque-adapter-ecoli-b0929-modules | https://imodulondb.org/api/genes/b0929/imodulons?organism=e_coli&amp;dataset=precise1k; Complete selected-locus membership response; weights,thresholds,flags; matched K-12 context only; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/adapter-ecoli-b0929-modules.raw | supports | All201 selected gene-module rows read. ompF passes thresholds in22SoxS,25Lrp,86UC-3,88Nitrogen; these are computational expression contexts only. Selected because Park discusses OmpA/OmpF as contextual outer-membrane cargo, not because the maintained record asserts these exact genes. |
| plaque-adapter-ecoli-module-22 | https://imodulondb.org/api/imodulons/e_coli/precise1k/22; Official full module response; only name/regulator/function/category/threshold and selected b0929 gene weight independently read; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/adapter-ecoli-module-22.raw | context_only | Native module metadata, threshold and b0929 membership inspected; generated AI summary excluded. Does not certify OMV cargo, secretion, localization, host inflammation or exact experimental strain. |
| plaque-adapter-ecoli-module-25 | https://imodulondb.org/api/imodulons/e_coli/precise1k/25; Official full module response; only name/regulator/function/category/threshold and selected b0929 gene weight independently read; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/adapter-ecoli-module-25.raw | context_only | Native module metadata, threshold and b0929 membership inspected; generated AI summary excluded. Does not certify OMV cargo, secretion, localization, host inflammation or exact experimental strain. |
| plaque-adapter-ecoli-module-86 | https://imodulondb.org/api/imodulons/e_coli/precise1k/86; Official full module response; only name/regulator/function/category/threshold and selected b0929 gene weight independently read; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/adapter-ecoli-module-86.raw | context_only | Native module metadata, threshold and b0929 membership inspected; generated AI summary excluded. Does not certify OMV cargo, secretion, localization, host inflammation or exact experimental strain. |
| plaque-adapter-ecoli-module-88 | https://imodulondb.org/api/imodulons/e_coli/precise1k/88; Official full module response; only name/regulator/function/category/threshold and selected b0929 gene weight independently read; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/adapter-ecoli-module-88.raw | context_only | Native module metadata, threshold and b0929 membership inspected; generated AI summary excluded. Does not certify OMV cargo, secretion, localization, host inflammation or exact experimental strain. |
| plaque-original-current-validation | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/originals-current-proof.json; Four original native validate/render executions,55 historical input occurrences,47 current frozen inputs | supports | All four immutable original YAMLs validate and render byte-identically to their Markdown;55 historical input occurrences match their own frozen Git source after symlink resolution. All47 current frozen inputs match source and worktree. Three own targets unchanged; CBF3 stale delta explicitly reassessed. |
| plaque-native-bacterial_extracellular_vesicle-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bacterial_extracellular_vesicle-uniprot-verify-receipt.json; Actual root command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/bacterial_extracellular_vesicle.yaml', '--verify']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bacterial_extracellular_vesicle-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0 on source head; independently read command/log and current record inventory: 0 reviewed protein examples and 0 typed GENE_OR_PROTEIN nodes (all COVERED when nonempty). Generic verify success alone does not certify scientific mechanism or family grounding. |
| plaque-native-bacterial_extracellular_vesicle-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bacterial_extracellular_vesicle-uniprot-causal-receipt.json; Actual root command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/bacterial_extracellular_vesicle.yaml', '--causal-graphs']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bacterial_extracellular_vesicle-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Actual exit0 on source head; independently read command/log and current record inventory: 0 reviewed protein examples and 0 typed GENE_OR_PROTEIN nodes (all COVERED when nonempty). Generic verify success alone does not certify scientific mechanism or family grounding. |
| plaque-native-bacterial_outer_membrane_vesicle-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bacterial_outer_membrane_vesicle-uniprot-verify-receipt.json; Actual root command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/bacterial_outer_membrane_vesicle.yaml', '--verify']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bacterial_outer_membrane_vesicle-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0 on source head; independently read command/log and current record inventory: 0 reviewed protein examples and 0 typed GENE_OR_PROTEIN nodes (all COVERED when nonempty). Generic verify success alone does not certify scientific mechanism or family grounding. |
| plaque-native-bacterial_outer_membrane_vesicle-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bacterial_outer_membrane_vesicle-uniprot-causal-receipt.json; Actual root command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/bacterial_outer_membrane_vesicle.yaml', '--causal-graphs']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bacterial_outer_membrane_vesicle-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Actual exit0 on source head; independently read command/log and current record inventory: 0 reviewed protein examples and 0 typed GENE_OR_PROTEIN nodes (all COVERED when nonempty). Generic verify success alone does not certify scientific mechanism or family grounding. |
| plaque-native-caf_1_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/caf_1_complex-uniprot-verify-receipt.json; Actual root command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/caf_1_complex.yaml', '--verify']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/caf_1_complex-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0 on source head; independently read command/log and current record inventory: 3 reviewed protein examples and 3 typed GENE_OR_PROTEIN nodes (all COVERED when nonempty). Generic verify success alone does not certify scientific mechanism or family grounding. |
| plaque-native-caf_1_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/caf_1_complex-uniprot-causal-receipt.json; Actual root command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/caf_1_complex.yaml', '--causal-graphs']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/caf_1_complex-uniprot-causal.log SHA256 7e39addd5c8162efa08ca6a788ad23af636459a2c7ddaaae5d6fcdbba13e0349 | supports | Actual exit0 on source head; independently read command/log and current record inventory: 3 reviewed protein examples and 3 typed GENE_OR_PROTEIN nodes (all COVERED when nonempty). Generic verify success alone does not certify scientific mechanism or family grounding. |
| plaque-native-cbf3_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/cbf3_complex-uniprot-verify-receipt.json; Actual root command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/cbf3_complex.yaml', '--verify']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/cbf3_complex-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0 on source head; independently read command/log and current record inventory: 4 reviewed protein examples and 4 typed GENE_OR_PROTEIN nodes (all COVERED when nonempty). Generic verify success alone does not certify scientific mechanism or family grounding. |
| plaque-native-cbf3_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/cbf3_complex-uniprot-causal-receipt.json; Actual root command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/cbf3_complex.yaml', '--causal-graphs']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/cbf3_complex-uniprot-causal.log SHA256 f028d171b3b55fd59304e552aebec98f3c543e05a312100bc617d82e1397131f | supports | Actual exit0 on source head; independently read command/log and current record inventory: 4 reviewed protein examples and 4 typed GENE_OR_PROTEIN nodes (all COVERED when nonempty). Generic verify success alone does not certify scientific mechanism or family grounding. |
| micro-record-0 | data/structures/other/bacterial_pre_replicative_complex.yaml; Complete current maintained YAML, all fields at exact source b82b8b5fcb02d90018a73c0d3d05ede8a2ab161f | supports | Whole target inspected including identity, history, components, protein examples, source placements, quantities, taxon scope, graph edges and discussions. |
| micro-prior-0 | reviews/structured/20261022T044322Z-bacterial-pre-replicative-complex-audit/review.yaml; Original authoritative YAML and native rendered Markdown; all checks, scientific dimensions, findings/actions/source tiers | supports | Immutable original observation remains historical; exact predecessor lineage and actual frozen-source hashes are retained. Historical validation metadata is not recast as a current run. |
| micro-delta-0 | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/5-stale.diff; Exact original frozen target revision to current main base | supports | BAM adds individual family-grounded lipoprotein nodes/parthood, BamA grounding, BamE xref and external OmpT substrate/product exemplars/K-12 context. Bindosome adds unreviewed AraS/SSO3066 example and history. Pre-RC is byte-identical. Each addition was substantively reassessed. |
| micro-record-1 | data/structures/other/bam_protein_complex.yaml; Complete current maintained YAML, all fields at exact source b82b8b5fcb02d90018a73c0d3d05ede8a2ab161f | supports | Whole target inspected including identity, history, components, protein examples, source placements, quantities, taxon scope, graph edges and discussions. |
| micro-prior-1 | reviews/structured/20261022T044323Z-bam-protein-complex-audit/review.yaml; Original authoritative YAML and native rendered Markdown; all checks, scientific dimensions, findings/actions/source tiers | supports | Immutable original observation remains historical; exact predecessor lineage and actual frozen-source hashes are retained. Historical validation metadata is not recast as a current run. |
| micro-delta-1 | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/6-stale.diff; Exact original frozen target revision to current main base | supports | BAM adds individual family-grounded lipoprotein nodes/parthood, BamA grounding, BamE xref and external OmpT substrate/product exemplars/K-12 context. Bindosome adds unreviewed AraS/SSO3066 example and history. Pre-RC is byte-identical. Each addition was substantively reassessed. |
| micro-record-2 | data/structures/other/bindosome_complex.yaml; Complete current maintained YAML, all fields at exact source b82b8b5fcb02d90018a73c0d3d05ede8a2ab161f | supports | Whole target inspected including identity, history, components, protein examples, source placements, quantities, taxon scope, graph edges and discussions. |
| micro-prior-2 | reviews/structured/20261022T044323Z-bindosome-complex-audit/review.yaml; Original authoritative YAML and native rendered Markdown; all checks, scientific dimensions, findings/actions/source tiers | supports | Immutable original observation remains historical; exact predecessor lineage and actual frozen-source hashes are retained. Historical validation metadata is not recast as a current run. |
| micro-delta-2 | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/7-stale.diff; Exact original frozen target revision to current main base | supports | BAM adds individual family-grounded lipoprotein nodes/parthood, BamA grounding, BamE xref and external OmpT substrate/product exemplars/K-12 context. Bindosome adds unreviewed AraS/SSO3066 example and history. Pre-RC is byte-identical. Each addition was substantively reassessed. |
| micro-policy | docs/CURATION.md; Evidence, Components/grounding/formation essentiality and Discussions append-only rules | supports | Component families/classes and organism examples are separate; exact verified family terms replace actionable label-only gaps. Essentiality concerns structure formation, not viability. Dated rationale/posed_date remain historical; current prompts/notes can be narrowed. |
| micro-native-policy | .claude/skills/review-yaml-record/SKILL.md; Complete native route, source adapter rules, active config/profile and checklist | supports | Positive protein/pathway assertions trigger source cross-checks even without expression claims; all actual scopes and validation limitations must remain explicit. Frozen common policy bytes equal the previously read PR2381 set, with relevant route/profile/CURATION/checklist/graph sections freshly reread. |
| micro-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Whole native graph skill plus frozen schema/component and external-actor rules | supports | Generic family/class and complex actors are permitted; external substrate xrefs are not forced into constituent membership. Coarse NONMECHANISTIC outlines need not invent atomic contacts. |
| micro-original-audit | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/original-audit.json; Six actual original validate/render commands;42 original source-input checks; six original artifacts immutable | supports | All three original YAMLs validate; paired Markdown is exact native render. All42 frozen source-input hashes match their original Git revisions; old target hashes and current staleness independently verified. |
| micro-up-P03004 | https://rest.uniprot.org/uniprotkb/P03004.json; Exact accession/status/name/gene and ordered loci/taxon; relevant FUNCTION/SUBUNIT/SUBCELLULAR LOCATION and evidence-code/citation joins; InterPro identifiers; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/up-P03004.raw | supports | P03004: UniProtKB reviewed (Swiss-Prot); taxon83333; name Chromosomal replication initiator protein DnaA; primary gene fields ['dnaA']; ordered loci ['b3702', 'JW3679']; InterPro ['IPR003593', 'IPR001957', 'IPR020591', 'IPR018312', 'IPR013159', 'IPR013317', 'IPR024633', 'IPR038454', 'IPR027417', 'IPR010921']. Q97UF5 has ordered locus SSO3066, no native araS geneName and is explicitly UNREVIEWED; the literature mapping is checked separately. Native annotations are not fresh primary-body experiments. |
| micro-up-P09169 | https://rest.uniprot.org/uniprotkb/P09169.json; Exact accession/status/name/gene and ordered loci/taxon; relevant FUNCTION/SUBUNIT/SUBCELLULAR LOCATION and evidence-code/citation joins; InterPro identifiers; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/up-P09169.raw | supports | P09169: UniProtKB reviewed (Swiss-Prot); taxon83333; name Protease 7; primary gene fields ['ompT']; ordered loci ['b0565', 'JW0554']; InterPro ['IPR020080', 'IPR020079', 'IPR000036']. Q97UF5 has ordered locus SSO3066, no native araS geneName and is explicitly UNREVIEWED; the literature mapping is checked separately. Native annotations are not fresh primary-body experiments. |
| micro-up-P0A903 | https://rest.uniprot.org/uniprotkb/P0A903.json; Exact accession/status/name/gene and ordered loci/taxon; relevant FUNCTION/SUBUNIT/SUBCELLULAR LOCATION and evidence-code/citation joins; InterPro identifiers; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/up-P0A903.raw | supports | P0A903: UniProtKB reviewed (Swiss-Prot); taxon83333; name Outer membrane protein assembly factor BamC; primary gene fields ['bamC']; ordered loci ['b2477', 'JW2462']; InterPro ['IPR014524', 'IPR010653', 'IPR064009', 'IPR042268']. Q97UF5 has ordered locus SSO3066, no native araS geneName and is explicitly UNREVIEWED; the literature mapping is checked separately. Native annotations are not fresh primary-body experiments. |
| micro-up-P0A937 | https://rest.uniprot.org/uniprotkb/P0A937.json; Exact accession/status/name/gene and ordered loci/taxon; relevant FUNCTION/SUBUNIT/SUBCELLULAR LOCATION and evidence-code/citation joins; InterPro identifiers; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/up-P0A937.raw | supports | P0A937: UniProtKB reviewed (Swiss-Prot); taxon83333; name Outer membrane protein assembly factor BamE; primary gene fields ['bamE']; ordered loci ['b2617', 'JW2598']; InterPro ['IPR026592', 'IPR037873', 'IPR007450']. Q97UF5 has ordered locus SSO3066, no native araS geneName and is explicitly UNREVIEWED; the literature mapping is checked separately. Native annotations are not fresh primary-body experiments. |
| micro-up-P0A940 | https://rest.uniprot.org/uniprotkb/P0A940.json; Exact accession/status/name/gene and ordered loci/taxon; relevant FUNCTION/SUBUNIT/SUBCELLULAR LOCATION and evidence-code/citation joins; InterPro identifiers; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/up-P0A940.raw | supports | P0A940: UniProtKB reviewed (Swiss-Prot); taxon83333; name Outer membrane protein assembly factor BamA; primary gene fields ['bamA']; ordered loci ['b0177', 'JW0172']; InterPro ['IPR000184', 'IPR010827', 'IPR039910', 'IPR023707', 'IPR034746']. Q97UF5 has ordered locus SSO3066, no native araS geneName and is explicitly UNREVIEWED; the literature mapping is checked separately. Native annotations are not fresh primary-body experiments. |
| micro-up-P0AC02 | https://rest.uniprot.org/uniprotkb/P0AC02.json; Exact accession/status/name/gene and ordered loci/taxon; relevant FUNCTION/SUBUNIT/SUBCELLULAR LOCATION and evidence-code/citation joins; InterPro identifiers; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/up-P0AC02.raw | supports | P0AC02: UniProtKB reviewed (Swiss-Prot); taxon83333; name Outer membrane protein assembly factor BamD; primary gene fields ['bamD']; ordered loci ['b2595', 'JW2577']; InterPro ['IPR017689', 'IPR039565', 'IPR011990']. Q97UF5 has ordered locus SSO3066, no native araS geneName and is explicitly UNREVIEWED; the literature mapping is checked separately. Native annotations are not fresh primary-body experiments. |
| micro-up-P77774 | https://rest.uniprot.org/uniprotkb/P77774.json; Exact accession/status/name/gene and ordered loci/taxon; relevant FUNCTION/SUBUNIT/SUBCELLULAR LOCATION and evidence-code/citation joins; InterPro identifiers; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/up-P77774.raw | supports | P77774: UniProtKB reviewed (Swiss-Prot); taxon83333; name Outer membrane protein assembly factor BamB; primary gene fields ['bamB']; ordered loci ['b2512', 'JW2496']; InterPro ['IPR017687', 'IPR018391', 'IPR002372', 'IPR011047', 'IPR015943']. Q97UF5 has ordered locus SSO3066, no native araS geneName and is explicitly UNREVIEWED; the literature mapping is checked separately. Native annotations are not fresh primary-body experiments. |
| micro-up-Q97UF5 | https://rest.uniprot.org/uniprotkb/Q97UF5.json; Exact accession/status/name/gene and ordered loci/taxon; relevant FUNCTION/SUBUNIT/SUBCELLULAR LOCATION and evidence-code/citation joins; InterPro identifiers; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/up-Q97UF5.raw | supports | Q97UF5: UniProtKB unreviewed (TrEMBL); taxon273057; name Arabinose ABC transporter, arabinose binding protein; primary gene fields [None]; ordered loci ['SSO3066']; InterPro ['IPR050490', 'IPR054925']. Q97UF5 has ordered locus SSO3066, no native araS geneName and is explicitly UNREVIEWED; the literature mapping is checked separately. Native annotations are not fresh primary-body experiments. |
| micro-up-Q97UZ1 | https://rest.uniprot.org/uniprotkb/Q97UZ1.json; Exact accession/status/name/gene and ordered loci/taxon; relevant FUNCTION/SUBUNIT/SUBCELLULAR LOCATION and evidence-code/citation joins; InterPro identifiers; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/up-Q97UZ1.raw | supports | Q97UZ1: UniProtKB reviewed (Swiss-Prot); taxon273057; name Glucose-binding protein GlcS; primary gene fields ['glcS']; ordered loci ['SSO2847']; InterPro ['IPR050490', 'IPR054925']. Q97UF5 has ordered locus SSO3066, no native araS geneName and is explicitly UNREVIEWED; the literature mapping is checked separately. Native annotations are not fresh primary-body experiments. |
| micro-query-SSO3066 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASSO3066%29+AND+%28organism_id%3A273057%29&amp;format=json&amp;size=100; Complete exact gene/taxon result page and accession identities; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/query-SSO3066.raw | supports | 1 returned accessions: ['Q97UF5']. Reviewed E. coli dnaA/BAM/OmpT and P2 glcS queries each return the intended unique entry. P2 araS/treS return0, while SSO3066 returns Q97UF5; absence of an alias in this index is not gene absence or refutation of a primary literature mapping. |
| micro-query-araS | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AaraS%29+AND+%28organism_id%3A273057%29&amp;format=json&amp;size=100; Complete exact gene/taxon result page and accession identities; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/query-araS.raw | supports | 0 returned accessions: []. Reviewed E. coli dnaA/BAM/OmpT and P2 glcS queries each return the intended unique entry. P2 araS/treS return0, while SSO3066 returns Q97UF5; absence of an alias in this index is not gene absence or refutation of a primary literature mapping. |
| micro-query-bamA | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AbamA%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete exact gene/taxon result page and accession identities; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/query-bamA.raw | supports | 1 returned accessions: ['P0A940']. Reviewed E. coli dnaA/BAM/OmpT and P2 glcS queries each return the intended unique entry. P2 araS/treS return0, while SSO3066 returns Q97UF5; absence of an alias in this index is not gene absence or refutation of a primary literature mapping. |
| micro-query-bamB | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AbamB%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete exact gene/taxon result page and accession identities; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/query-bamB.raw | supports | 1 returned accessions: ['P77774']. Reviewed E. coli dnaA/BAM/OmpT and P2 glcS queries each return the intended unique entry. P2 araS/treS return0, while SSO3066 returns Q97UF5; absence of an alias in this index is not gene absence or refutation of a primary literature mapping. |
| micro-query-bamC | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AbamC%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete exact gene/taxon result page and accession identities; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/query-bamC.raw | supports | 1 returned accessions: ['P0A903']. Reviewed E. coli dnaA/BAM/OmpT and P2 glcS queries each return the intended unique entry. P2 araS/treS return0, while SSO3066 returns Q97UF5; absence of an alias in this index is not gene absence or refutation of a primary literature mapping. |
| micro-query-bamD | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AbamD%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete exact gene/taxon result page and accession identities; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/query-bamD.raw | supports | 1 returned accessions: ['P0AC02']. Reviewed E. coli dnaA/BAM/OmpT and P2 glcS queries each return the intended unique entry. P2 araS/treS return0, while SSO3066 returns Q97UF5; absence of an alias in this index is not gene absence or refutation of a primary literature mapping. |
| micro-query-bamE | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AbamE%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete exact gene/taxon result page and accession identities; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/query-bamE.raw | supports | 1 returned accessions: ['P0A937']. Reviewed E. coli dnaA/BAM/OmpT and P2 glcS queries each return the intended unique entry. P2 araS/treS return0, while SSO3066 returns Q97UF5; absence of an alias in this index is not gene absence or refutation of a primary literature mapping. |
| micro-query-dnaA | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdnaA%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete exact gene/taxon result page and accession identities; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/query-dnaA.raw | supports | 1 returned accessions: ['P03004']. Reviewed E. coli dnaA/BAM/OmpT and P2 glcS queries each return the intended unique entry. P2 araS/treS return0, while SSO3066 returns Q97UF5; absence of an alias in this index is not gene absence or refutation of a primary literature mapping. |
| micro-query-glcS | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AglcS%29+AND+%28organism_id%3A273057%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete exact gene/taxon result page and accession identities; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/query-glcS.raw | supports | 1 returned accessions: ['Q97UZ1']. Reviewed E. coli dnaA/BAM/OmpT and P2 glcS queries each return the intended unique entry. P2 araS/treS return0, while SSO3066 returns Q97UF5; absence of an alias in this index is not gene absence or refutation of a primary literature mapping. |
| micro-query-ompT | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AompT%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete exact gene/taxon result page and accession identities; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/query-ompT.raw | supports | 1 returned accessions: ['P09169']. Reviewed E. coli dnaA/BAM/OmpT and P2 glcS queries each return the intended unique entry. P2 araS/treS return0, while SSO3066 returns Q97UF5; absence of an alias in this index is not gene absence or refutation of a primary literature mapping. |
| micro-query-treS | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AtreS%29+AND+%28organism_id%3A273057%29&amp;format=json&amp;size=100; Complete exact gene/taxon result page and accession identities; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/query-treS.raw | supports | 0 returned accessions: []. Reviewed E. coli dnaA/BAM/OmpT and P2 glcS queries each return the intended unique entry. P2 araS/treS return0, while SSO3066 returns Q97UF5; absence of an alias in this index is not gene absence or refutation of a primary literature mapping. |
| micro-ipr-IPR001957 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001957/; Exact name/type, complete description/flags, hierarchy and native example cross-reference; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/ipr-IPR001957.raw | supports | IPR001957: Chromosomal replication control, initiator DnaA; family. IPR001957 is DnaA-specific; IPR020591 explicitly also includes Hda. The five BAM terms match their full named families. IPR054925 has an unchecked LLM description and IPR050490 a checked LLM description; neither establishes the whole mixed bindosome cohort or primary membership. |
| micro-ipr-IPR014524 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR014524/; Exact name/type, complete description/flags, hierarchy and native example cross-reference; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/ipr-IPR014524.raw | supports | IPR014524: Outer membrane protein assembly factor BamC; family. IPR001957 is DnaA-specific; IPR020591 explicitly also includes Hda. The five BAM terms match their full named families. IPR054925 has an unchecked LLM description and IPR050490 a checked LLM description; neither establishes the whole mixed bindosome cohort or primary membership. |
| micro-ipr-IPR017687 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR017687/; Exact name/type, complete description/flags, hierarchy and native example cross-reference; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/ipr-IPR017687.raw | supports | IPR017687: Outer membrane protein assembly factor BamB; family. IPR001957 is DnaA-specific; IPR020591 explicitly also includes Hda. The five BAM terms match their full named families. IPR054925 has an unchecked LLM description and IPR050490 a checked LLM description; neither establishes the whole mixed bindosome cohort or primary membership. |
| micro-ipr-IPR017689 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR017689/; Exact name/type, complete description/flags, hierarchy and native example cross-reference; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/ipr-IPR017689.raw | supports | IPR017689: Outer membrane protein assembly factor BamD; family. IPR001957 is DnaA-specific; IPR020591 explicitly also includes Hda. The five BAM terms match their full named families. IPR054925 has an unchecked LLM description and IPR050490 a checked LLM description; neither establishes the whole mixed bindosome cohort or primary membership. |
| micro-ipr-IPR020591 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR020591/; Exact name/type, complete description/flags, hierarchy and native example cross-reference; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/ipr-IPR020591.raw | supports | IPR020591: Chromosomal replication control, initiator DnaA-like; family. IPR001957 is DnaA-specific; IPR020591 explicitly also includes Hda. The five BAM terms match their full named families. IPR054925 has an unchecked LLM description and IPR050490 a checked LLM description; neither establishes the whole mixed bindosome cohort or primary membership. |
| micro-ipr-IPR023707 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR023707/; Exact name/type, complete description/flags, hierarchy and native example cross-reference; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/ipr-IPR023707.raw | supports | IPR023707: Outer membrane protein assembly factor BamA; family. IPR001957 is DnaA-specific; IPR020591 explicitly also includes Hda. The five BAM terms match their full named families. IPR054925 has an unchecked LLM description and IPR050490 a checked LLM description; neither establishes the whole mixed bindosome cohort or primary membership. |
| micro-ipr-IPR026592 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR026592/; Exact name/type, complete description/flags, hierarchy and native example cross-reference; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/ipr-IPR026592.raw | supports | IPR026592: Outer membrane protein assembly factor BamE; family. IPR001957 is DnaA-specific; IPR020591 explicitly also includes Hda. The five BAM terms match their full named families. IPR054925 has an unchecked LLM description and IPR050490 a checked LLM description; neither establishes the whole mixed bindosome cohort or primary membership. |
| micro-ipr-IPR050490 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050490/; Exact name/type, complete description/flags, hierarchy and native example cross-reference; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/ipr-IPR050490.raw | supports | IPR050490: Bacterial solute-binding protein 1; family. IPR001957 is DnaA-specific; IPR020591 explicitly also includes Hda. The five BAM terms match their full named families. IPR054925 has an unchecked LLM description and IPR050490 a checked LLM description; neither establishes the whole mixed bindosome cohort or primary membership. |
| micro-ipr-IPR054925 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR054925/; Exact name/type, complete description/flags, hierarchy and native example cross-reference; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/ipr-IPR054925.raw | supports | IPR054925: Glucose-binding protein GlcS; family. IPR001957 is DnaA-specific; IPR020591 explicitly also includes Hda. The five BAM terms match their full named families. IPR054925 has an unchecked LLM description and IPR050490 a checked LLM description; neither establishes the whole mixed bindosome cohort or primary membership. |
| micro-go-0006270 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0006270; Exact active ID/name/definition and returned typed relationships or explicitly requested ancestor relation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/go-0006270.raw | supports | GO:0006270 DNA replication initiation; active=True. Ancestor results are transitive and relation-specific, not automatically direct edges. BAM is_a-only response does not include GO0106234, while part_of includes GO0009279; definition-based broader outer-membrane-complex classification is not thereby disproved. |
| micro-go-0009279 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0009279; Exact active ID/name/definition and returned typed relationships or explicitly requested ancestor relation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/go-0009279.raw | supports | GO:0009279 cell outer membrane; active=True. Ancestor results are transitive and relation-specific, not automatically direct edges. BAM is_a-only response does not include GO0106234, while part_of includes GO0009279; definition-based broader outer-membrane-complex classification is not thereby disproved. |
| micro-go-0032993 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0032993; Exact active ID/name/definition and returned typed relationships or explicitly requested ancestor relation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/go-0032993.raw | supports | GO:0032993 protein-DNA complex; active=True. Ancestor results are transitive and relation-specific, not automatically direct edges. BAM is_a-only response does not include GO0106234, while part_of includes GO0009279; definition-based broader outer-membrane-complex classification is not thereby disproved. |
| micro-go-0036387 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0036387; Exact active ID/name/definition and returned typed relationships or explicitly requested ancestor relation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/go-0036387.raw | supports | GO:0036387 pre-replicative complex; active=True. Ancestor results are transitive and relation-specific, not automatically direct edges. BAM is_a-only response does not include GO0106234, while part_of includes GO0009279; definition-based broader outer-membrane-complex classification is not thereby disproved. |
| micro-go-0036389-is_a | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0036389/ancestors?relations=is_a; Exact active ID/name/definition and returned typed relationships or explicitly requested ancestor relation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/go-0036389-is_a.raw | supports | GO:0036389 bacterial pre-replicative complex; active=True. Ancestor results are transitive and relation-specific, not automatically direct edges. BAM is_a-only response does not include GO0106234, while part_of includes GO0009279; definition-based broader outer-membrane-complex classification is not thereby disproved. |
| micro-go-0036389-part_of | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0036389/ancestors?relations=part_of; Exact active ID/name/definition and returned typed relationships or explicitly requested ancestor relation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/go-0036389-part_of.raw | supports | GO:0036389 bacterial pre-replicative complex; active=True. Ancestor results are transitive and relation-specific, not automatically direct edges. BAM is_a-only response does not include GO0106234, while part_of includes GO0009279; definition-based broader outer-membrane-complex classification is not thereby disproved. |
| micro-go-0036389 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0036389; Exact active ID/name/definition and returned typed relationships or explicitly requested ancestor relation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/go-0036389.raw | supports | GO:0036389 bacterial pre-replicative complex; active=True. Ancestor results are transitive and relation-specific, not automatically direct edges. BAM is_a-only response does not include GO0106234, while part_of includes GO0009279; definition-based broader outer-membrane-complex classification is not thereby disproved. |
| micro-go-0098796 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0098796; Exact active ID/name/definition and returned typed relationships or explicitly requested ancestor relation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/go-0098796.raw | supports | GO:0098796 membrane protein complex; active=True. Ancestor results are transitive and relation-specific, not automatically direct edges. BAM is_a-only response does not include GO0106234, while part_of includes GO0009279; definition-based broader outer-membrane-complex classification is not thereby disproved. |
| micro-go-0106234 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0106234; Exact active ID/name/definition and returned typed relationships or explicitly requested ancestor relation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/go-0106234.raw | supports | GO:0106234 outer membrane protein complex; active=True. Ancestor results are transitive and relation-specific, not automatically direct edges. BAM is_a-only response does not include GO0106234, while part_of includes GO0009279; definition-based broader outer-membrane-complex classification is not thereby disproved. |
| micro-go-1990063-is_a | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990063/ancestors?relations=is_a; Exact active ID/name/definition and returned typed relationships or explicitly requested ancestor relation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/go-1990063-is_a.raw | supports | GO:1990063 Bam protein complex; active=True. Ancestor results are transitive and relation-specific, not automatically direct edges. BAM is_a-only response does not include GO0106234, while part_of includes GO0009279; definition-based broader outer-membrane-complex classification is not thereby disproved. |
| micro-go-1990063-part_of | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990063/ancestors?relations=part_of; Exact active ID/name/definition and returned typed relationships or explicitly requested ancestor relation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/go-1990063-part_of.raw | supports | GO:1990063 Bam protein complex; active=True. Ancestor results are transitive and relation-specific, not automatically direct edges. BAM is_a-only response does not include GO0106234, while part_of includes GO0009279; definition-based broader outer-membrane-complex classification is not thereby disproved. |
| micro-go-1990063 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990063; Exact active ID/name/definition and returned typed relationships or explicitly requested ancestor relation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/go-1990063.raw | supports | GO:1990063 Bam protein complex; active=True. Ancestor results are transitive and relation-specific, not automatically direct edges. BAM is_a-only response does not include GO0106234, while part_of includes GO0009279; definition-based broader outer-membrane-complex classification is not thereby disproved. |
| micro-go-1990100 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990100; Exact active ID/name/definition and returned typed relationships or explicitly requested ancestor relation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/go-1990100.raw | supports | GO:1990100 DnaB-DnaC complex; active=True. Ancestor results are transitive and relation-specific, not automatically direct edges. BAM is_a-only response does not include GO0106234, while part_of includes GO0009279; definition-based broader outer-membrane-complex classification is not thereby disproved. |
| micro-go-1990101 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990101; Exact active ID/name/definition and returned typed relationships or explicitly requested ancestor relation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/go-1990101.raw | supports | GO:1990101 DnaA-oriC complex; active=True. Ancestor results are transitive and relation-specific, not automatically direct edges. BAM is_a-only response does not include GO0106234, while part_of includes GO0009279; definition-based broader outer-membrane-complex classification is not thereby disproved. |
| micro-go-1990102 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990102; Exact active ID/name/definition and returned typed relationships or explicitly requested ancestor relation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/go-1990102.raw | supports | GO:1990102 DnaA-DiaA complex; active=True. Ancestor results are transitive and relation-specific, not automatically direct edges. BAM is_a-only response does not include GO0106234, while part_of includes GO0009279; definition-based broader outer-membrane-complex classification is not thereby disproved. |
| micro-go-1990103 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990103; Exact active ID/name/definition and returned typed relationships or explicitly requested ancestor relation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/go-1990103.raw | supports | GO:1990103 DnaA-HU complex; active=True. Ancestor results are transitive and relation-specific, not automatically direct edges. BAM is_a-only response does not include GO0106234, while part_of includes GO0009279; definition-based broader outer-membrane-complex classification is not thereby disproved. |
| micro-go-7770042-is_a | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A7770042/ancestors?relations=is_a; Exact active ID/name/definition and returned typed relationships or explicitly requested ancestor relation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/go-7770042-is_a.raw | supports | GO:7770042 bindosome complex; active=True. Ancestor results are transitive and relation-specific, not automatically direct edges. BAM is_a-only response does not include GO0106234, while part_of includes GO0009279; definition-based broader outer-membrane-complex classification is not thereby disproved. |
| micro-go-7770042-part_of | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A7770042/ancestors?relations=part_of; Exact active ID/name/definition and returned typed relationships or explicitly requested ancestor relation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/go-7770042-part_of.raw | supports | GO:7770042 bindosome complex; active=True. Ancestor results are transitive and relation-specific, not automatically direct edges. BAM is_a-only response does not include GO0106234, while part_of includes GO0009279; definition-based broader outer-membrane-complex classification is not thereby disproved. |
| micro-go-7770042 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A7770042; Exact active ID/name/definition and returned typed relationships or explicitly requested ancestor relation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/go-7770042.raw | supports | GO:7770042 bindosome complex; active=True. Ancestor results are transitive and relation-specific, not automatically direct edges. BAM is_a-only response does not include GO0106234, while part_of includes GO0009279; definition-based broader outer-membrane-complex classification is not thereby disproved. |
| micro-tax-562 | https://rest.uniprot.org/taxonomy/562.json; Complete native taxon identifier/name/rank/lineage; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/tax-562.raw | supports | Exact taxonomy identity checked; historical Sulfolobus versus current Saccharolobus names do not change species/P2 identity. Reference accession strain, experimental host and dataset strains remain distinct. |
| micro-tax-83333 | https://rest.uniprot.org/taxonomy/83333.json; Complete native taxon identifier/name/rank/lineage; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/tax-83333.raw | supports | Exact taxonomy identity checked; historical Sulfolobus versus current Saccharolobus names do not change species/P2 identity. Reference accession strain, experimental host and dataset strains remain distinct. |
| micro-tax-2 | https://rest.uniprot.org/taxonomy/2.json; Complete native taxon identifier/name/rank/lineage; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/tax-2.raw | supports | Exact taxonomy identity checked; historical Sulfolobus versus current Saccharolobus names do not change species/P2 identity. Reference accession strain, experimental host and dataset strains remain distinct. |
| micro-tax-2287 | https://rest.uniprot.org/taxonomy/2287.json; Complete native taxon identifier/name/rank/lineage; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/tax-2287.raw | supports | Exact taxonomy identity checked; historical Sulfolobus versus current Saccharolobus names do not change species/P2 identity. Reference accession strain, experimental host and dataset strains remain distinct. |
| micro-tax-273057 | https://rest.uniprot.org/taxonomy/273057.json; Complete native taxon identifier/name/rank/lineage; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/tax-273057.raw | supports | Exact taxonomy identity checked; historical Sulfolobus versus current Saccharolobus names do not change species/P2 identity. Reference accession strain, experimental host and dataset strains remain distinct. |
| micro-uo-0000222 | https://www.ebi.ac.uk/ols4/api/ontologies/uo/terms?obo_id=UO:0000222; Exact OLS UO term name/identifier/definition; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/uo-0000222.raw | supports | UO0000222 kilodalton resolves; approximate203kDa measurement remains tied to the purified E. coli BAM preparation. |
| micro-miller2009-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A19833870+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact native bibliographic identity and complete deposited abstract; body scope separately enumerated; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/miller2009-meta.raw | partial | Bacterial origin recognition complexes direct assembly of higher-order DnaA oligomeric structures.; Miller DT, Grimwade JE, Betteridge T, Rozgaja T, Torgue JJ, Leonard AC.; DOI 10.1073/pnas.0909472106. Primary abstract tier only in this evidence row; no unread body is certified. |
| micro-leonard2010-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A21035377+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact native bibliographic identity and complete deposited abstract; body scope separately enumerated; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/leonard2010-meta.raw | context_only | Regulating DnaA complex assembly: it is time to fill the gaps.; Leonard AC, Grimwade JE.; DOI 10.1016/j.mib.2010.10.001. Secondary review context, not direct experimental evidence. |
| micro-hagan2010-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1126%2Fscience.1188919%22&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact native bibliographic identity and complete deposited abstract; body scope separately enumerated; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/hagan2010-meta.raw | partial | Reconstitution of outer membrane protein assembly from purified components.; Hagan CL, Kim S, Kahne D.; DOI 10.1126/science.1188919. Primary abstract tier only in this evidence row; no unread body is certified. |
| micro-hagan2011-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1146%2Fannurev-biochem-061408-144611%22&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact native bibliographic identity and complete deposited abstract; body scope separately enumerated; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/hagan2011-meta.raw | context_only | β-Barrel membrane protein assembly by the Bam complex.; Hagan CL, Silhavy TJ, Kahne D.; DOI 10.1146/annurev-biochem-061408-144611. Secondary review context, not direct experimental evidence. |
| micro-gu2016-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fnature17199%22&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact native bibliographic identity and complete deposited abstract; body scope separately enumerated; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/gu2016-meta.raw | partial | Structural basis of outer membrane protein insertion by the BAM complex.; Gu Y, Li H, Dong H, Zeng Y, Zhang Z, Paterson NG, Stansfeld PJ, Wang Z, Zhang Y, Wang W, Dong C.; DOI 10.1038/nature17199. Primary abstract tier only in this evidence row; no unread body is certified. |
| micro-iadanza2016-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fncomms12865%22&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact native bibliographic identity and complete deposited abstract; body scope separately enumerated; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/iadanza2016-meta.raw | partial | Lateral opening in the intact β-barrel assembly machinery captured by cryo-EM.; Iadanza MG, Higgins AJ, Schiffrin B, Calabrese AN, Brockwell DJ, Ashcroft AE, Radford SE, Ranson NA.; DOI 10.1038/ncomms12865. Primary abstract tier only in this evidence row; no unread body is certified. |
| micro-bakelar2016-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1126%2Fscience.aad3460%22&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact native bibliographic identity and complete deposited abstract; body scope separately enumerated; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/bakelar2016-meta.raw | partial | The structure of the β-barrel assembly machinery complex.; Bakelar J, Buchanan SK, Noinaj N.; DOI 10.1126/science.aad3460. Primary abstract tier only in this evidence row; no unread body is certified. |
| micro-zolghadr2011-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1007%2Fs00792-010-0353-0%22&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact native bibliographic identity and complete deposited abstract; body scope separately enumerated; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/zolghadr2011-meta.raw | partial | The bindosome is a structural component of the Sulfolobus solfataricus cell envelope.; Zolghadr B, Klingl A, Rachel R, Driessen AJ, Albers SV.; DOI 10.1007/s00792-010-0353-0. Primary abstract tier only in this evidence row; no unread body is certified. |
| micro-elferink2001-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11260467+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=100; Exact native bibliographic identity and complete deposited abstract; body scope separately enumerated; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/elferink2001-meta.raw | partial | Sugar transport in Sulfolobus solfataricus is mediated by two families of binding protein-dependent ABC transporters.; Elferink MG, Albers SV, Konings WN, Driessen AJ.; DOI 10.1046/j.1365-2958.2001.02336.x. Primary abstract tier only in this evidence row; no unread body is certified. |
| micro-go-bindosome-ref-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A38877064+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=100; Exact native bibliographic identity and complete deposited abstract; body scope separately enumerated; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/go-bindosome-ref-meta.raw | partial | Two distinct archaeal type IV pili structures formed by proteins with identical sequence.; Liu J, Eastep GN, Cvirkaite-Krupovic V, Rich-New ST, Kreutzberger MAB, Egelman EH, Krupovic M, Wang F.; DOI 10.1038/s41467-024-45062-z. Primary abstract tier only in this evidence row; no unread body is certified. |
| micro-pmid-15851030 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15851030+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact MED ID/title/authors/DOI and complete abstract, joined separately to native protein annotation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/pmid-15851030.raw | partial | Identification of a multicomponent complex required for outer membrane biogenesis in Escherichia coli.; Wu T, Malinverni J, Ruiz N, Kim S, Silhavy TJ, Kahne D.. Additional localization/complex annotation paper inspected at abstract tier only; no full body, all strains or unobserved measurements are certified. |
| micro-pmid-16079137 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A16079137+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact MED ID/title/authors/DOI and complete abstract, joined separately to native protein annotation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/pmid-16079137.raw | partial | Protein complexes of the Escherichia coli cell envelope.; Stenberg F, Chovanec P, Maslen SL, Robinson CV, Ilag LL, von Heijne G, Daley DO.. Additional localization/complex annotation paper inspected at abstract tier only; no full body, all strains or unobserved measurements are certified. |
| micro-pmid-17404237 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A17404237+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact MED ID/title/authors/DOI and complete abstract, joined separately to native protein annotation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/pmid-17404237.raw | partial | Lipoprotein SmpA is a component of the YaeT complex that assembles outer membrane proteins in Escherichia coli.; Sklar JG, Wu T, Gronenberg LS, Malinverni JC, Kahne D, Silhavy TJ.. Additional localization/complex annotation paper inspected at abstract tier only; no full body, all strains or unobserved measurements are certified. |
| micro-pmid-22574163 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A22574163+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact MED ID/title/authors/DOI and complete abstract, joined separately to native protein annotation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/pmid-22574163.raw | partial | Association of the chromosome replication initiator DnaA with the Escherichia coli inner membrane in vivo: quantity and mode of binding.; Regev T, Myers N, Zarivach R, Fishov I.. Additional localization/complex annotation paper inspected at abstract tier only; no full body, all strains or unobserved measurements are certified. |
| micro-pmid-23882017 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A23882017+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact MED ID/title/authors/DOI and complete abstract, joined separately to native protein annotation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/pmid-23882017.raw | partial | Receptor polymorphism restricts contact-dependent growth inhibition to members of the same species.; Ruhe ZC, Wallace AB, Low DA, Hayes CS.. Additional localization/complex annotation paper inspected at abstract tier only; no full body, all strains or unobserved measurements are certified. |
| micro-pmid-24619089 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A24619089+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact MED ID/title/authors/DOI and complete abstract, joined separately to native protein annotation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/pmid-24619089.raw | partial | Structural and functional analysis of the β-barrel domain of BamA from Escherichia coli.; Ni D, Wang Y, Yang X, Zhou H, Hou X, Cao B, Lu Z, Zhao X, Yang K, Huang Y.. Additional localization/complex annotation paper inspected at abstract tier only; no full body, all strains or unobserved measurements are certified. |
| micro-pmid-26900875 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A26900875+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact MED ID/title/authors/DOI and complete abstract, joined separately to native protein annotation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/pmid-26900875.raw | partial | Structure of the BAM complex and its implications for biogenesis of outer-membrane proteins.; Han L, Zheng J, Wang Y, Yang X, Liu Y, Sun C, Cao B, Zhou H, Ni D, Lou J, Zhao Y, Huang Y.. Additional localization/complex annotation paper inspected at abstract tier only; no full body, all strains or unobserved measurements are certified. |
| micro-pmid-28166228 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A28166228+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact MED ID/title/authors/DOI and complete abstract, joined separately to native protein annotation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/pmid-28166228.raw | partial | Rapid turnover of DnaA at replication origin regions contributes to initiation control of DNA replication.; Schenk K, Hervás AB, Rösch TC, Eisemann M, Schmitt BA, Dahlke S, Kleine-Borgmann L, Murray SM, Graumann PL.. Additional localization/complex annotation paper inspected at abstract tier only; no full body, all strains or unobserved measurements are certified. |
| micro-pmid-9478970 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9478970+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact MED ID/title/authors/DOI and complete abstract, joined separately to native protein annotation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/pmid-9478970.raw | partial | Membrane-mediated release of nucleotide from an initiator of chromosomal replication, Escherichia coli DnaA, occurs with insertion of a distinct region of the protein into the lipid bilayer.; Garner J, Durrer P, Kitchen J, Brunner J, Crooke E.. Additional localization/complex annotation paper inspected at abstract tier only; no full body, all strains or unobserved measurements are certified. |
| micro-miller2009-legacy | https://pmc.ncbi.nlm.nih.gov/articles/PMC2773971/?pdf=render; Complete Introduction, Results sec2–5, Discussion sec6 and Methods sec8–12; Fig1–6 captions, no pixels; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/miller2009-legacy.raw | supports | E. coli oriC high-affinity sites recruit oligomerization-proficient DnaA to lower-affinity sites; site mutants, DMS footprints, W6A, crosslinks and EMSA support this assembly stage. P3478/polA, W3110 and PC2/dnaC(ts) experiments and tagged purified proteins are explicit; generic pre-RC is not conflated with one restricted substate or every later helicase-loading step. |
| micro-leonard2010-body | https://pmc-oa-opendata.s3.amazonaws.com/PMC3005629.1/PMC3005629.1.xml; Secondary review Introduction S1, Extending the model S7 and Conclusions S8 only; no claim of complete body reading; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/leonard2010-body.raw | context_only | Review distinguishes DnaA/oriC pre-RC assembly and species-dependent origin architectures. Its proposed gap-filling model and optional regulatory factors are not direct experiments or mandatory components of every generic record. |
| micro-hagan2010-body | https://pmc-oa-opendata.s3.amazonaws.com/PMC2873164.1/PMC2873164.1.xml; Complete nine main-text paragraphs before Supplementary Material; embedded main text, no supplementary methods or figure pixels; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/hagan2010-body.raw | supports | Purified BamAB+BamCDE reconstructed complex with SurA folds and inserts OmpT in proteoliposomes; enzymatic fluorescence, heat-modifiability and carbonate resistance provide complementary evidence. Activity/viability necessity differs from formation;1:1:1:1 and ambiguous1or2BamE,7%yield and possible oligomers are contextual rather than universal composition. K-12 reference exemplar does not certify the uninspected exact experimental cloning strain. |
| micro-bakelar2016-body | https://pmc-oa-opendata.s3.amazonaws.com/PMC4883095.1/PMC4883095.1.xml; Main-text structure/interaction/conformation paragraphs; Methods S2–4 expression, purification/crystallization and modeling; no pixels/maps/supplementary tables; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/bakelar2016-body.raw | supports | Crystal material is BamACDE after BamB loss; modeled full BAM docks a separate BamAB structure. BamC/D/E interfaces, BamD TPR/POTRA and BamE bridge support organization; BL21(DE3) expression differs from native reference K-12. Structural observation is not a universal catalytic trajectory. |
| micro-iadanza2016-body | https://pmc-oa-opendata.s3.amazonaws.com/PMC5056442.1/PMC5056442.1.xml; Introduction, all seven Results subsections, Discussion; Methods expression/purification and proteoliposome reconstitution; no raw maps/pixels/supplemental tables; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/iadanza2016-body.raw | supports | Intact BamABCDE cryo-EM at4.9Å captures lateral opening with BamB present. Predominant native MS203456±22Da and minor additionalBamE distinguish approximate mass from invariant composition. OmpT activity/crosslink rescue supports bounded gating; detergent, BL21(DE3), reconstitution and substrate dependence remain explicit. |
| micro-gu2016-author | https://ueaeprints.uea.ac.uk/id/eprint/57584/1/BAM_Nature_Gu_29012016_2_change_Figure_legends_3_revised_accepted.pdf; Accepted manuscript printed pp1–8 through initial BamA–BamD interface discussion and Methods cloning/expression/purification pp27–29; text extraction only, no pixels; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/gu2016-author.raw | supports | Five-subunit inward-open and four-subunit lateral-open crystal complexes are distinct. BamB binds POTRA2/3; BamC engages BamD; BamE couples BamD with BamA POTRA4/5. HDB150/pJH114, additional bamB expression and DH5alpha plasmid preparation bound experimental scope; intact lateral-open observation is separately Iadanza, not attributed to Gu. |
| micro-zolghadr2011-body | https://pmc-oa-opendata.s3.amazonaws.com/PMC3047682.1/PMC3047682.1.xml; Entire Introduction, Methods and Results Sec1–15 plus Discussion Sec16 and captions; complete retained body literal TreS/trehalose check; no figure pixels; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/zolghadr2011-body.raw | supports | PBL2025/ΔbasEF envelope extraction/ConA/BN-PAGE and size exclusion recover400/600kDa complexes with GlcS/SSO3043 and SlaA/SSO1273. BasEF deletion preserves extracted complexes but impairs glucose uptake; localization/handoff and native assembly remain partly inferred. AraS appears in arabinose context; complete cited body does not name TreS. This is bounded source support, not biological absence. |
| micro-albers2003-legacy | https://pmc.ncbi.nlm.nih.gov/articles/PMC161584/; Exact Table2 whole ORF/signal/function inventory and adjacent Discussion on PibD specificity/processing; no pixels, other body sections not certified; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/albers2003-legacy.raw | supports | Table2 maps SSO3066 to AraS and SSO0999 to TreS; Discussion explicitly names GlcS/TreS/AraS processing. This supports AraS locus identity and positively establishes TreS identity/processing context, but does not itself show TreS in the mature400/600kDa complexes of the maintained2011 source. |
| micro-aras-locus-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%28SSO3066+OR+%22araS%22%29+AND+Sulfolobus&amp;format=json&amp;resultType=core&amp;pageSize=100; Complete bounded result metadata list; selected exact Albers2003 paper separately read; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/aras-locus-meta.raw | supports | Current query returns56 records. Broad araS query read as metadata/title-selection only, not56 full articles; exact SSO3066 query returns7 and identifies Albers2003. No all-literature absence conclusion. |
| micro-locus-exact-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%22SSO3066%22&amp;format=json&amp;resultType=core&amp;pageSize=100; Complete bounded result metadata list; selected exact Albers2003 paper separately read; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/locus-exact-meta.raw | supports | Current query returns7 records. Broad araS query read as metadata/title-selection only, not56 full articles; exact SSO3066 query returns7 and identifies Albers2003. No all-literature absence conclusion. |
| micro-access-miller2009-body | https://pmc-oa-opendata.s3.amazonaws.com/PMC2773971.1/PMC2773971.1.xml; Actual failed public source response; not scientific article content | context_only | HTTP404 body unavailable on this route; genuine alternatives for Miller/Albers were separately read. Elferink/Hagan2011 remain abstract-limited. |
| micro-access-albers2003-body | https://pmc-oa-opendata.s3.amazonaws.com/PMC161584.1/PMC161584.1.xml; Actual failed public source response; not scientific article content | context_only | HTTP404 body unavailable on this route; genuine alternatives for Miller/Albers were separately read. Elferink/Hagan2011 remain abstract-limited. |
| micro-access-elferink-publisher | https://onlinelibrary.wiley.com/doi/10.1046/j.1365-2958.2001.02336.x; Actual failed public source response; not scientific article content | context_only | HTTP403 body unavailable on this route; genuine alternatives for Miller/Albers were separately read. Elferink/Hagan2011 remain abstract-limited. |
| micro-access-hagan2011-publisher | https://www.annualreviews.org/content/journals/10.1146/annurev-biochem-061408-144611; Actual failed public source response; not scientific article content | context_only | HTTP403 body unavailable on this route; genuine alternatives for Miller/Albers were separately read. Elferink/Hagan2011 remain abstract-limited. |
| micro-access-wrong-article | https://pmc.ncbi.nlm.nih.gov/articles/PMC3209348/; Attempted PMC route title-identity check only | context_only | Candidate route returned an unrelated herpesvirus article; identity mismatch detected immediately, excluded from all scientific support. No Hagan2011 body claim. |
| micro-catalogue | https://imodulondb.org/api/datasets; Complete official organism/dataset catalogue; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/catalogue.raw | supports | Fresh catalogue covers E. coli; choose actual precise1k. It lists Sulfolobus acidocaldarius but not Saccharolobus/Sulfolobus solfataricus, so no unmatched archaeal proxy is used. Coverage is catalogue-specific, not biological absence. |
| micro-ecoli-meta | https://imodulondb.org/api/datasets/e_coli/precise1k/meta; Complete selected dataset metadata; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/ecoli-meta.raw | supports | precise1k comprises4257genes/201modules/1035samples/518conditions and BW25113,DGF-298,GMOS,MG1655,W3110. This mixed-strain dataset does not identify every HDB150/BL21/PBL2025 assay context. |
| micro-ecoli-genes | https://imodulondb.org/api/genes?organism=e_coli&amp;dataset=precise1k&amp;limit=10000; Complete4257-row gene inventory; exact selected locus/gene/UniProt joins; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/ecoli-genes.raw | supports | Current dnaA b3702, bamA b0177,bamB b2512,bamC b2477,bamD b2595,bamE b2617 and external ompT b0565 are represented. Presence in expression data does not establish membership or necessity. |
| micro-ecoli-modules | https://imodulondb.org/api/datasets/e_coli/precise1k/imodulons; Complete201-row module metadata list, numeric keys and labels; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/ecoli-modules.raw | supports | Module metadata checked independently of generated ai_summary; association is not assembly/catalysis/localization evidence. |
| micro-dataset-b3702 | https://imodulondb.org/api/genes/b3702/imodulons?organism=e_coli&amp;dataset=precise1k; Complete returned201-module table and actual flags/weights/thresholds; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/dataset-b3702.raw | supports | b3702: above-threshold entries []. No above-threshold result for dnaA/bamA–E is not gene absence or evidence against the structures. |
| micro-dataset-b0177 | https://imodulondb.org/api/genes/b0177/imodulons?organism=e_coli&amp;dataset=precise1k; Complete returned201-module table and actual flags/weights/thresholds; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/dataset-b0177.raw | supports | b0177: above-threshold entries []. No above-threshold result for dnaA/bamA–E is not gene absence or evidence against the structures. |
| micro-dataset-b2512 | https://imodulondb.org/api/genes/b2512/imodulons?organism=e_coli&amp;dataset=precise1k; Complete returned201-module table and actual flags/weights/thresholds; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/dataset-b2512.raw | supports | b2512: above-threshold entries []. No above-threshold result for dnaA/bamA–E is not gene absence or evidence against the structures. |
| micro-dataset-b2477 | https://imodulondb.org/api/genes/b2477/imodulons?organism=e_coli&amp;dataset=precise1k; Complete returned201-module table and actual flags/weights/thresholds; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/dataset-b2477.raw | supports | b2477: above-threshold entries []. No above-threshold result for dnaA/bamA–E is not gene absence or evidence against the structures. |
| micro-dataset-b2595 | https://imodulondb.org/api/genes/b2595/imodulons?organism=e_coli&amp;dataset=precise1k; Complete returned201-module table and actual flags/weights/thresholds; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/dataset-b2595.raw | supports | b2595: above-threshold entries []. No above-threshold result for dnaA/bamA–E is not gene absence or evidence against the structures. |
| micro-dataset-b2617 | https://imodulondb.org/api/genes/b2617/imodulons?organism=e_coli&amp;dataset=precise1k; Complete returned201-module table and actual flags/weights/thresholds; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/dataset-b2617.raw | supports | b2617: above-threshold entries []. No above-threshold result for dnaA/bamA–E is not gene absence or evidence against the structures. |
| micro-dataset-b0565 | https://imodulondb.org/api/genes/b0565/imodulons?organism=e_coli&amp;dataset=precise1k; Complete returned201-module table and actual flags/weights/thresholds; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/dataset-b0565.raw | supports | b0565: above-threshold entries [{'k': 59, 'name': 'Magnesium', 'weight': 0.100658384, 'threshold': 0.080711519}, {'k': 164, 'name': 'minicoli KOs', 'weight': 0.056150973, 'threshold': 0.042504139}]. No above-threshold result for dnaA/bamA–E is not gene absence or evidence against the structures. |
| micro-ecoli-module-59 | https://imodulondb.org/api/imodulons/e_coli/precise1k/59; Full actual module gene list and metadata; exact b0565 weight/threshold join; generated ai_summary and condition activities not used; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/ecoli-module-59.raw | supports | Magnesium/PhoP59:21genes, OmpT0.100658384 above0.080711519. This is regulatory context only, not proof of whole BAM coexpression, assembly or OmpT substrate processing. |
| micro-ecoli-module-164 | https://imodulondb.org/api/imodulons/e_coli/precise1k/164; Full actual module gene list and metadata; exact b0565 weight/threshold join; generated ai_summary and condition activities not used; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/ecoli-module-164.raw | supports | minicoli KOs164:115genes, OmpT0.056150973 above0.042504139. This is regulatory context only, not proof of whole BAM coexpression, assembly or OmpT substrate processing. |
| micro-historical-runner | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical00:49Z retained adapter invocation receipt; not rerun | context_only | Original optional runner was unavailable; fresh public official-source inspection supplies bounded applicability fallback. This is never counted as a current successful runner execution. |
| micro-native-bacterial_pre_replicative_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bacterial_pre_replicative_complex-uniprot-verify-receipt.json; Actual command receipt; full log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bacterial_pre_replicative_complex-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0; one reviewed example and one COVERED typed node. Generic verify success is not inventory count; diagnostics do not establish biological membership or absence. BAM external substrate/group nodes are allowed; partial TreS example coverage is not itself a missing-optional-example finding. |
| micro-native-bacterial_pre_replicative_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bacterial_pre_replicative_complex-uniprot-causal-receipt.json; Actual command receipt; full log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bacterial_pre_replicative_complex-uniprot-causal.log SHA256 f6e0e6b4b913d39e9ca812634ab0e75f1ff2e46eaf6d2e468133dbd2600c1019 | supports | Exit0; one reviewed example and one COVERED typed node. Generic verify success is not inventory count; diagnostics do not establish biological membership or absence. BAM external substrate/group nodes are allowed; partial TreS example coverage is not itself a missing-optional-example finding. |
| micro-native-bam_protein_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bam_protein_complex-uniprot-verify-receipt.json; Actual command receipt; full log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bam_protein_complex-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0; five reviewed component examples, five COVERED nodes and three UNANCHORED_WITH_UNIPROT external-substrate/group nodes. Generic verify success is not inventory count; diagnostics do not establish biological membership or absence. BAM external substrate/group nodes are allowed; partial TreS example coverage is not itself a missing-optional-example finding. |
| micro-native-bam_protein_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bam_protein_complex-uniprot-causal-receipt.json; Actual command receipt; full log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bam_protein_complex-uniprot-causal.log SHA256 c608f801dda01017c8f577c48d37c00d5189329ec184e1edfaa0c608734353ac | supports | Exit0; five reviewed component examples, five COVERED nodes and three UNANCHORED_WITH_UNIPROT external-substrate/group nodes. Generic verify success is not inventory count; diagnostics do not establish biological membership or absence. BAM external substrate/group nodes are allowed; partial TreS example coverage is not itself a missing-optional-example finding. |
| micro-native-bindosome_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bindosome_complex-uniprot-verify-receipt.json; Actual command receipt; full log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bindosome_complex-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0; two examples (one reviewed GlcS, one unreviewed SSO3066/AraS) and one PARTIAL_EXAMPLES node missing treS. Generic verify success is not inventory count; diagnostics do not establish biological membership or absence. BAM external substrate/group nodes are allowed; partial TreS example coverage is not itself a missing-optional-example finding. |
| micro-native-bindosome_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bindosome_complex-uniprot-causal-receipt.json; Actual command receipt; full log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bindosome_complex-uniprot-causal.log SHA256 c7712aeb5a9e9859a045011117f593a0b77378faa3ed724dcc110ecf06cbf0a6 | supports | Exit0; two examples (one reviewed GlcS, one unreviewed SSO3066/AraS) and one PARTIAL_EXAMPLES node missing treS. Generic verify success is not inventory count; diagnostics do not establish biological membership or absence. BAM external substrate/group nodes are allowed; partial TreS example coverage is not itself a missing-optional-example finding. |
| check-qc | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/qc.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| check-labels | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/labels.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| check-trait-links | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/trait-links.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Native TraitMech link check passed. |
| check-vendored | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/vendored.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Pinned governed files match; native vendored check passed. |
| check-curies | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/curies.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| focused | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/focused-results.json; All twenty actual target schema/strict command outputs | supports | Ten schema and ten strict commands returned exit zero. |
| supplemental-pmid | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/pmid-chunks-receipt.json; Complete native-report PMID set checked with unchanged resolver in batches of at most fifty | supports | 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers remain unverified. |
| historical-adapter-runner-availability | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical runner invocation receipt; exact retained SHA256 reverified during PR2382 synthesis | context_only | Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS PermissionError reading the configured runner pyvenv.cfg. This is retained historical availability evidence, not a fresh attempt or a scientific validation failure. Native policy permits inspected source-catalogue fallback. |
| root-native-ap_5_adaptor_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/ap_5_adaptor_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-ap_5_adaptor_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/ap_5_adaptor_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-ap_type_membrane_coat_adaptor_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/ap_type_membrane_coat_adaptor_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-ap_type_membrane_coat_adaptor_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/ap_type_membrane_coat_adaptor_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-apical_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/apical_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-apical_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/apical_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-bacterial_extracellular_vesicle-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bacterial_extracellular_vesicle-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-bacterial_extracellular_vesicle-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bacterial_extracellular_vesicle-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-bacterial_outer_membrane_vesicle-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bacterial_outer_membrane_vesicle-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-bacterial_outer_membrane_vesicle-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bacterial_outer_membrane_vesicle-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-bacterial_pre_replicative_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bacterial_pre_replicative_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-bacterial_pre_replicative_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bacterial_pre_replicative_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-bam_protein_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bam_protein_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 5 represented protein examples; 8 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-bam_protein_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bam_protein_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 5 represented protein examples; 8 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-bindosome_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bindosome_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 2 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-bindosome_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bindosome_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 2 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-caf_1_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/caf_1_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-caf_1_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/caf_1_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-cbf3_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/cbf3_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-cbf3_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/cbf3_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |

## Limits And Additional Notes

- AP-5, AP-type adaptor and apical-complex independent review: All three assigned current target hashes are unchanged. Two inherited minor findings are confirmed with exact predecessors; the apical target remains a qualified pass. No new finding, terminal disposition or unrelated-record issue resolution is invented.
- AP-5, AP-type adaptor and apical-complex independent review: Fresh genuine Hirst, Slabicki, Kaur, Hu, Ren and Carruthers bodies were read at the precise recorded sections/captions; no figure pixels or supplements were inspected and excluded sections are not certified. There are no maintained target images.
- AP-5, AP-type adaptor and apical-complex independent review: Boothroyd2008 and Waller2024 are secondary reviews at complete native MED metadata/abstract tier in this pass. Publisher challenge and Europe PMC500 bodies provide access context only; unread full-body claims and old Key Points are not represented as fresh observations.
- AP-5, AP-type adaptor and apical-complex independent review: Current GO0020031 polar-ring label/aliases versus definition has a bounded unresolved anatomical tension with primary sources. The maintained named APR/coarse parthood is not falsely refuted and no replacement identifier is guessed.
- AP-5, AP-type adaptor and apical-complex independent review: InterPro IPR050431 has unchecked LLM-generated prose; only native identity/flags are used as context. Exact AP5 families are supported independently by native family metadata and human example cross-references. Bounded candidate queries do not establish universal absence.
- AP-5, AP-type adaptor and apical-complex independent review: Native accession/query checks verify identity and populated or empty coverage, not universal necessity, endogenous localization or a complete assembly cycle. AP-type has three typed unpopulated classes; apical has zero typed protein nodes. Optional representatives/classes are not automatic defects.
- AP-5, AP-type adaptor and apical-complex independent review: Fresh catalogue coverage provides no matching native eukaryotic dataset for these assertions. No unrelated production/assay organism substitutes. Historical unavailable runner remains actual 2026-11-03T00:49Z observation, never a fresh invocation.
- AP-5, AP-type adaptor and apical-complex independent review: Record curation, final repository checks, CI, queue, merge and deletion remain parent-owned and are not certified by this scientific source review.
- Vesicle, CAF-1 and CBF3 independent review: Primary bodies directly inspected: Leber/Yan CBF3, Park OMV, scoped Zeng Cbf2-GFP Methods/Results, and Kaufman official PDF selected Results/Methods. Lee2007/Lee2009 and Huh/Johnston are bounded complete-primary-abstract/native-annotation tiers; no unread Methods, precise strain, cargo topology or mechanism is inferred.
- Vesicle, CAF-1 and CBF3 independent review: Toyofuku/Kim complete abstracts and Schwechheimer inspected body are secondary evidence. DOI content-negotiated Crossref JSON is metadata, not full publisher body. Initial403/429/404 and frontend-shell routes are preserved as access context; successful later Kaufman PDF access does not erase the initial failures.
- Vesicle, CAF-1 and CBF3 independent review: No current target image exists. PDF extraction and text captions are not figure-pixel inspection, and no image reproduction/licence clearance is asserted.
- Vesicle, CAF-1 and CBF3 independent review: The fresh current catalogue and official dataset tables were read directly as source fallback. No fresh kg-microbe-sources execution is claimed. Any root inclusion of the earlier00:49Z runner-unavailable receipt must retain its historical timestamp and failed-execution scope.
- Vesicle, CAF-1 and CBF3 independent review: Catalogue/annotation and selected module context are computational transcriptomics only. precise1k K-12-related strains do not establish Park intestinal CLP isolate equivalence; selected USA300-related datasets do not establish the unverified Lee2009 strain. No S. cerevisiae dataset matches. Query nonhits and below-threshold OmpA are not biological absence.
- Vesicle, CAF-1 and CBF3 independent review: Native verify/causal exit0 establishes declared identifier/inventory coverage, not current scientific correctness, exact family grounding, universal localization or necessity. Full QC/CI/merge queue are root-owned and not independently rerun or precertified here.
- Vesicle, CAF-1 and CBF3 independent review: Inherited scientific curation is reported only; records and original review bundles are unchanged. No unrelated category/neighbor issue is terminally resolved by this slice.
- Bacterial pre-RC, BAM and bindosome independent review: Scientific findings cover only three assigned whole records, not neighboring/category/grouped historical issue resolution.
- Bacterial pre-RC, BAM and bindosome independent review: Primary body scope is exact: Miller Introduction/Results/Discussion/Methods and captions; Hagan2010 main text only; Bakelar main text+MethodsS2–4; Iadanza Introduction/Results/Discussion and two declared Methods subsections; Gu accepted pp1–8 and27–29; Zolghadr entire main body/Methods/captions; Albers2003 Table2/adjacent Discussion only. No figure pixels, maps, raw data or supplements were inspected.
- Bacterial pre-RC, BAM and bindosome independent review: Hagan2011 and Elferink2001 publisher routes are blocked; these remain complete-abstract tiers. Leonard2010 is secondary and onlyS1/S7/S8 body sections were read. Additional protein annotation papers remain exact native metadata/complete abstracts and UniProt joins, not complete body certification.
- Bacterial pre-RC, BAM and bindosome independent review: A mistaken candidate PMC route for Hagan2011 returned an unrelated title and was immediately excluded; its receipt is access provenance only, not a source finding or scientific support.
- Bacterial pre-RC, BAM and bindosome independent review: BAM reference K-12 identity, HDB150/BL21(DE3)/DH5alpha experiments and pooled dataset strains are distinct. Predominant203kDa and specificOmpT assay cannot establish universal stoichiometry, atomic mechanism or formation necessity.
- Bacterial pre-RC, BAM and bindosome independent review: Bindosome referenceP2 is distinct from PBL2025 experiments. AraS=SSO3066 and TreS=SSO0999 primary mappings are positive evidence; alias query0 is not absence. TreS processing alone does not establish mature400/600kDa assembly membership.
- Bacterial pre-RC, BAM and bindosome independent review: No exact source-neutral family is forced onto the mixed bindosome cohort or unverified SO term onto oriC. Historical rationale is append-only; current unresolved tasks are not automatically completed by taxon-specific xrefs.
- Bacterial pre-RC, BAM and bindosome independent review: Official dataset fallback is bounded to full current catalogue, mixed-strain e_coli/precise1k, seven exact loci and201module rows per locus plus matching59/164 gene sets. Generated ai_summary and per-condition activity were not used as evidence. Above/below threshold is not physical membership, catalysis or necessity; acidocaldarius is not a solfataricus proxy.
- Bacterial pre-RC, BAM and bindosome independent review: Current native commands verify implemented identities and coverage diagnostics, not primary scientific validity. Bindosome PARTIAL_EXAMPLES missingTreS is not independently a scientific defect or proof of absence.
- Bacterial pre-RC, BAM and bindosome independent review: Historical runner receipt is2026-11-03T00:49:00.848907–00:49:00.863225Z, exit1/unavailable; no fresh execution claimed. Root owns corpus QC, saved-head CI/queue/publication. No repository/Git/GitHub changes were made.
- Historical observations remain immutable; their old checks are not represented as current-head execution.
- The adapter runner was not rerun after the canary established OS access failure. Catalogue-based coverage is assessed directly; fresh and reused responses retain actual access timestamps.
- Native label checks include 923 no-adapter skips. Native identifier checks include 909 PMID transport failures and 254 skipped identifiers; bounded supplemental checks independently resolve the 909 PMIDs.
- Scientific record-curation findings stay in separate issues; no record is edited by this review PR.
- Final trusted-base post-save review-check, exact-head independent acceptance, final-head CI and merge-group CI occur after saving this immutable observation and are not represented here as already completed.
- All ten original YAML/Markdown pairs remain unchanged. Three changed target hashes receive substantive source reassessment, not a mechanical hash update: BAM subunit/grounding/OmpT annotations, AraS/SSO3066 reference identity, and CBF3 Ctf13/Skp1 assembly edges.
- Nine inherited minor findings remain separately tracked: AP-5 exact families, AP-parent composition/mass gloss, BEV authority-definition scope, OMV composite typing and source placement, DnaA family, bounded TreS source support, Cac2 family and Skp1 family. Historical finding identities and dated rationale remain append-only.
- Positive Albers2003 evidence identifies AraS/SSO3066 and TreS/SSO0999 and discusses processing. The TreS finding concerns the maintained claim-adjacent constituent source, not biological absence, mandatory deletion or a required optional example.
- BAM reference K-12 OmpT identity and the purified folding/insertion assay are supported within inspected main-text scope. Exact supplementary construct provenance was not inspected; reference annotations are not treated as experiments performed in living K-12.
- CBF3 core versus full-complex preparations, CAF-1 BJ926 purification versus W303 genetics versus S288c identifiers, and Park OMV mouse-isolate/injection experiments versus pooled precise1k context remain distinct.
- The native protein inventory has 19 examples and 24 typed nodes. Current coverage diagnostics are 17 COVERED, one PARTIAL_EXAMPLES, three NO_GENE_SYMBOLS and three UNANCHORED_WITH_UNIPROT; these classifications alone are not scientific findings.
- Local corpus QC and focused gates passed before this observation. Post-save trusted-base review-check, exact-head re-review, final-head CI and merge-group CI remain subsequent external gates. Existing issue #2514 tracks the native bulk-PMID transport/reporting limitation; separately bounded resolution verified all 909 affected PMIDs.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261104T021428Z-pr2382-current-record-followup
kind: batch
repository: CultureBotAI/CellStructureMech
title: 'PR 2382: current-input review of ten records and adversarial follow-up'
started_at: '2026-11-04T01:57:28.444017Z'
finished_at: '2026-11-04T02:14:28Z'
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
summary: Independent current-input review of all ten structure records refreshes three
  stale observations (BAM, bindosome and CBF3), repairs ten unsupported structured-source
  applicability exclusions, and preserves nine independently confirmed inherited minor
  record-curation findings across eight targets. Apical complex and BAM pass with
  explicit source limits; the overall verdict remains needs_curation. Only immutable
  review successors are added.
source:
  git_revision: b82b8b5fcb02d90018a73c0d3d05ede8a2ab161f
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
  - path: data/structures/other/ap_5_adaptor_complex.yaml
    sha256: d951b48b8f9fe05db066c722dd2dad8277f04eb4af1ac36bf4a5c03932ac82dc
    role: target
  - path: data/structures/other/ap_type_membrane_coat_adaptor_complex.yaml
    sha256: a16a52e7091df279f222b922baa48be321173ab9dc132e1c2be2384d48ca626b
    role: target
  - path: data/structures/other/apical_complex.yaml
    sha256: 72b670707751292b450e4c8bccddb25a4a14e482fc0eaaa85975681694f55952
    role: target
  - path: data/structures/other/bacterial_extracellular_vesicle.yaml
    sha256: 43f0f6e0dfef8fc8533bbbac4c5a1583adc6626873f52b92f2edbc32560137d2
    role: target
  - path: data/structures/other/bacterial_outer_membrane_vesicle.yaml
    sha256: ae635da7dc9351f59de2b4283aa2d572b200cf9eba187147c027e5e86b445a34
    role: target
  - path: data/structures/other/bacterial_pre_replicative_complex.yaml
    sha256: a4a8871a963f0b0eb3e32d9a677f099afdf3f6246dc7964f1890b61b3f01b62a
    role: target
  - path: data/structures/other/bam_protein_complex.yaml
    sha256: ac284bcf4e0ec8021b0f218143e2337a0845c36113edb097e79c950ac1688cde
    role: target
  - path: data/structures/other/bindosome_complex.yaml
    sha256: 360a186c82ed29ddaae42fdbcb445a37b8482be97bed64a6d077792b8fdce375
    role: target
  - path: data/structures/other/caf_1_complex.yaml
    sha256: 9cfaf9ce52f019ddb3125428f3c6ce7cb17ae2e476fbd0fb9be2e0bcad652576
    role: target
  - path: data/structures/other/cbf3_complex.yaml
    sha256: 9cf3d32f5094ac6a00417cb7b7c125b45a4329e364d8e721314f19349baf44f2
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
  - path: reviews/structured/20261022T044318Z-ap-5-adaptor-complex-audit/review.md
    sha256: 55ce09c6671b2f931d1be3f25da51a642f6d520e79164905cb52f0d5d2f7d951
    role: context
  - path: reviews/structured/20261022T044318Z-ap-5-adaptor-complex-audit/review.yaml
    sha256: 202ed0adb6576cec2f53d0534cab118b16f81c35af955690259134befbf41b11
    role: context
  - path: reviews/structured/20261022T044319Z-ap-type-membrane-coat-adaptor-complex-audit/review.md
    sha256: fa2e9242144b1d03fb0c289641958a89f0a4296c754cb0724d4d5122d05f1681
    role: context
  - path: reviews/structured/20261022T044319Z-ap-type-membrane-coat-adaptor-complex-audit/review.yaml
    sha256: f9d5ddaf668a4d93b705ec4a49a37c5e2ca8aad1c0a85aa6dba40bd9d2fb681c
    role: context
  - path: reviews/structured/20261022T044320Z-apical-complex-audit/review.md
    sha256: 944f5047433f89f78a0c18d431352abbbf9f57a57292dffcd5536933303db790
    role: context
  - path: reviews/structured/20261022T044320Z-apical-complex-audit/review.yaml
    sha256: 6bb778c0edffbb843e663f1308b557e9098f56e563497650cba09816ab21964f
    role: context
  - path: reviews/structured/20261022T044321Z-bacterial-extracellular-vesicle-audit/review.md
    sha256: 0642d4d65e3e7b6534e98f7392d1bb067e568fb4cb709616f5e632dc33dd25b9
    role: context
  - path: reviews/structured/20261022T044321Z-bacterial-extracellular-vesicle-audit/review.yaml
    sha256: a07011482846bfeed4934761a86a5bbe024017036df6e25efb36babf13f972ed
    role: context
  - path: reviews/structured/20261022T044321Z-bacterial-outer-membrane-vesicle-audit/review.md
    sha256: c2e5c89d185bfd2a9c4e3e145a1f8c2cbf6fc98a9fce5037a0b3ad39a6e47830
    role: context
  - path: reviews/structured/20261022T044321Z-bacterial-outer-membrane-vesicle-audit/review.yaml
    sha256: 891ea995b50bff90b1e4817858ae96afba7ea596b2fdc92f7d2e3c74aa6198c0
    role: context
  - path: reviews/structured/20261022T044322Z-bacterial-pre-replicative-complex-audit/review.md
    sha256: 883bf8f7177222b24597854d7fca07d8604fb63a4c3fe7b272fe97a1796e6082
    role: context
  - path: reviews/structured/20261022T044322Z-bacterial-pre-replicative-complex-audit/review.yaml
    sha256: 0f46df59f2c24561a55cb0bcfca7d535e1c71e83a8407a5ff446e73dfcd548fe
    role: context
  - path: reviews/structured/20261022T044323Z-bam-protein-complex-audit/review.md
    sha256: f1c590a7e5bb5fb6c42ff61c851d57e9b5c7740caa9fa57530b8803756621144
    role: context
  - path: reviews/structured/20261022T044323Z-bam-protein-complex-audit/review.yaml
    sha256: 85a2536611ef781a45b0f5e986a05214590cfad7b7237a67e89ae26e8cec3772
    role: context
  - path: reviews/structured/20261022T044323Z-bindosome-complex-audit/review.md
    sha256: 534b5aacbcc05cc348c8a5b0e1da792a1088adf0c0df62c3cc983d567a4a732a
    role: context
  - path: reviews/structured/20261022T044323Z-bindosome-complex-audit/review.yaml
    sha256: 3c4e32c35bf0fd463a99f3c7c3a97043f9816189dd950b3fa5e227fd7e55abcd
    role: context
  - path: reviews/structured/20261022T044324Z-caf-1-complex-audit/review.md
    sha256: 1d644191dd2dbc83b3bd94a6852bc98aac5a2268ca1d7e0f01137e0429abdd22
    role: context
  - path: reviews/structured/20261022T044324Z-caf-1-complex-audit/review.yaml
    sha256: fb4dcdc6295e05feeb8a72463af97b1b7500ddf7271053658bcff165d5af253c
    role: context
  - path: reviews/structured/20261022T044325Z-cbf3-complex-audit/review.md
    sha256: c04bb3a746e87579620706b4b54dec08dd4101dcf22b934509613ba47be9bf1c
    role: context
  - path: reviews/structured/20261022T044325Z-cbf3-complex-audit/review.yaml
    sha256: 324587ca73380b88cc7da048e16d12ec28469bc06f28c7ff7b2f22bd00dda44f
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
- target_id: GO:0044599
  path: data/structures/other/ap_5_adaptor_complex.yaml
  label: AP-5 adaptor complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/ap_5_adaptor_complex.yaml
    role: maintained scientific record
- target_id: GO:0030119
  path: data/structures/other/ap_type_membrane_coat_adaptor_complex.yaml
  label: AP-type membrane coat adaptor complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/ap_type_membrane_coat_adaptor_complex.yaml
    role: maintained scientific record
- target_id: GO:0020007
  path: data/structures/other/apical_complex.yaml
  label: apical complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/apical_complex.yaml
    role: maintained scientific record
- target_id: GO:0097691
  path: data/structures/other/bacterial_extracellular_vesicle.yaml
  label: bacterial extracellular vesicle
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/bacterial_extracellular_vesicle.yaml
    role: maintained scientific record
- target_id: GO:0061701
  path: data/structures/other/bacterial_outer_membrane_vesicle.yaml
  label: bacterial outer membrane vesicle
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/bacterial_outer_membrane_vesicle.yaml
    role: maintained scientific record
- target_id: GO:0036389
  path: data/structures/other/bacterial_pre_replicative_complex.yaml
  label: bacterial pre-replicative complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/bacterial_pre_replicative_complex.yaml
    role: maintained scientific record
- target_id: GO:1990063
  path: data/structures/other/bam_protein_complex.yaml
  label: Bam protein complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/bam_protein_complex.yaml
    role: maintained scientific record
- target_id: GO:7770042
  path: data/structures/other/bindosome_complex.yaml
  label: bindosome complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/bindosome_complex.yaml
    role: maintained scientific record
- target_id: GO:0033186
  path: data/structures/other/caf_1_complex.yaml
  label: CAF-1 complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/caf_1_complex.yaml
    role: maintained scientific record
- target_id: GO:0031518
  path: data/structures/other/cbf3_complex.yaml
  label: CBF3 complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/cbf3_complex.yaml
    role: maintained scientific record
scope:
  description: Exact ten-record PR cohort reassessed against current main e715af32ff105343da446bc865a3adb2e3b5a2b3.
    Changed inputs are substantively reassessed. Scientific records remain unchanged.
  selection: Complete cohort of ten maintained records reviewed in original PR head
    53645eea171f96d452504f427d3b33e21d15d586.
  coverage: full
  population_size: 10
  reviewed_target_ids:
  - GO:0044599
  - GO:0030119
  - GO:0020007
  - GO:0097691
  - GO:0061701
  - GO:0036389
  - GO:1990063
  - GO:7770042
  - GO:0033186
  - GO:0031518
checks:
- check_id: qc
  name: Full native QC
  status: passed
  required: true
  target_ids:
  - GO:0044599
  - GO:0030119
  - GO:0020007
  - GO:0097691
  - GO:0061701
  - GO:0036389
  - GO:1990063
  - GO:7770042
  - GO:0033186
  - GO:0031518
  command: just qc
  exit_code: 0
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  scope_note: Actual local execution at main-merge head b82b8b5fcb02d90018a73c0d3d05ede8a2ab161f.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-qc
- check_id: labels
  name: Native label correspondence
  status: passed
  required: true
  target_ids:
  - GO:0044599
  - GO:0030119
  - GO:0020007
  - GO:0097691
  - GO:0061701
  - GO:0036389
  - GO:1990063
  - GO:7770042
  - GO:0033186
  - GO:0031518
  command: just validate-products
  exit_code: 0
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  scope_note: Actual local execution at main-merge head b82b8b5fcb02d90018a73c0d3d05ede8a2ab161f.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-labels
- check_id: trait-links
  name: TraitMech references
  status: passed
  required: true
  target_ids:
  - GO:0044599
  - GO:0030119
  - GO:0020007
  - GO:0097691
  - GO:0061701
  - GO:0036389
  - GO:1990063
  - GO:7770042
  - GO:0033186
  - GO:0031518
  command: just check-trait-links --check
  exit_code: 0
  summary: Native TraitMech link check passed.
  scope_note: Actual local execution at main-merge head b82b8b5fcb02d90018a73c0d3d05ede8a2ab161f.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-trait-links
- check_id: vendored
  name: Pinned governed files
  status: passed
  required: true
  target_ids:
  - GO:0044599
  - GO:0030119
  - GO:0020007
  - GO:0097691
  - GO:0061701
  - GO:0036389
  - GO:1990063
  - GO:7770042
  - GO:0033186
  - GO:0031518
  command: just vendored-check
  exit_code: 0
  summary: Pinned governed files match; native vendored check passed.
  scope_note: Actual local execution at main-merge head b82b8b5fcb02d90018a73c0d3d05ede8a2ab161f.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-vendored
- check_id: curies
  name: Native identifier resolver
  status: passed
  required: true
  target_ids:
  - GO:0044599
  - GO:0030119
  - GO:0020007
  - GO:0097691
  - GO:0061701
  - GO:0036389
  - GO:1990063
  - GO:7770042
  - GO:0033186
  - GO:0031518
  command: just check-curies
  exit_code: 0
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  scope_note: Actual local execution at main-merge head b82b8b5fcb02d90018a73c0d3d05ede8a2ab161f.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-curies
- check_id: focused-0
  name: validate GO:0044599
  status: passed
  required: true
  target_ids:
  - GO:0044599
  command: just validate data/structures/other/ap_5_adaptor_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-1
  name: validate-strict GO:0044599
  status: passed
  required: true
  target_ids:
  - GO:0044599
  command: just validate-strict data/structures/other/ap_5_adaptor_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-2
  name: validate GO:0030119
  status: passed
  required: true
  target_ids:
  - GO:0030119
  command: just validate data/structures/other/ap_type_membrane_coat_adaptor_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-3
  name: validate-strict GO:0030119
  status: passed
  required: true
  target_ids:
  - GO:0030119
  command: just validate-strict data/structures/other/ap_type_membrane_coat_adaptor_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-4
  name: validate GO:0020007
  status: passed
  required: true
  target_ids:
  - GO:0020007
  command: just validate data/structures/other/apical_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-5
  name: validate-strict GO:0020007
  status: passed
  required: true
  target_ids:
  - GO:0020007
  command: just validate-strict data/structures/other/apical_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-6
  name: validate GO:0097691
  status: passed
  required: true
  target_ids:
  - GO:0097691
  command: just validate data/structures/other/bacterial_extracellular_vesicle.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-7
  name: validate-strict GO:0097691
  status: passed
  required: true
  target_ids:
  - GO:0097691
  command: just validate-strict data/structures/other/bacterial_extracellular_vesicle.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-8
  name: validate GO:0061701
  status: passed
  required: true
  target_ids:
  - GO:0061701
  command: just validate data/structures/other/bacterial_outer_membrane_vesicle.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-9
  name: validate-strict GO:0061701
  status: passed
  required: true
  target_ids:
  - GO:0061701
  command: just validate-strict data/structures/other/bacterial_outer_membrane_vesicle.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-10
  name: validate GO:0036389
  status: passed
  required: true
  target_ids:
  - GO:0036389
  command: just validate data/structures/other/bacterial_pre_replicative_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-11
  name: validate-strict GO:0036389
  status: passed
  required: true
  target_ids:
  - GO:0036389
  command: just validate-strict data/structures/other/bacterial_pre_replicative_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-12
  name: validate GO:1990063
  status: passed
  required: true
  target_ids:
  - GO:1990063
  command: just validate data/structures/other/bam_protein_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-13
  name: validate-strict GO:1990063
  status: passed
  required: true
  target_ids:
  - GO:1990063
  command: just validate-strict data/structures/other/bam_protein_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-14
  name: validate GO:7770042
  status: passed
  required: true
  target_ids:
  - GO:7770042
  command: just validate data/structures/other/bindosome_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-15
  name: validate-strict GO:7770042
  status: passed
  required: true
  target_ids:
  - GO:7770042
  command: just validate-strict data/structures/other/bindosome_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-16
  name: validate GO:0033186
  status: passed
  required: true
  target_ids:
  - GO:0033186
  command: just validate data/structures/other/caf_1_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-17
  name: validate-strict GO:0033186
  status: passed
  required: true
  target_ids:
  - GO:0033186
  command: just validate-strict data/structures/other/caf_1_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-18
  name: validate GO:0031518
  status: passed
  required: true
  target_ids:
  - GO:0031518
  command: just validate data/structures/other/cbf3_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-19
  name: validate-strict GO:0031518
  status: passed
  required: true
  target_ids:
  - GO:0031518
  command: just validate-strict data/structures/other/cbf3_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: supplemental-pmid
  name: Supplemental bounded PMID authority checks
  status: passed
  required: true
  target_ids:
  - GO:0044599
  - GO:0030119
  - GO:0020007
  - GO:0097691
  - GO:0061701
  - GO:0036389
  - GO:1990063
  - GO:7770042
  - GO:0033186
  - GO:0031518
  command: .venv/bin/python /private/tmp/cellstructure-batches-2346-2397-20261103/check_pmid_chunks.py
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382
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
  - GO:0044599
  - GO:0030119
  - GO:0020007
  - GO:0097691
  - GO:0061701
  - GO:0036389
  - GO:1990063
  - GO:7770042
  - GO:0033186
  - GO:0031518
  summary: 'All ten whole-record molecular or pathway narratives require an applicability
    assessment: seven formal and three prose-only exclusions are corrected. Fresh
    official catalogues and bounded E. coli precise1k and S. aureus dataset context
    were inspected; absent matched human, apicomplexan, yeast and solfataricus datasets
    do not imply biological absence. Experimental strain and reference-annotation
    identities remain distinct; expression modules do not establish physical membership,
    mechanism or necessity. The runner-unavailable receipt is historical, not a fresh
    invocation.'
  evidence_ids:
  - septin-catalogue
  - plaque-adapter-sa-staph_precise108-genes
  - plaque-adapter-sa-staph_precise165-genes
  - plaque-catalogue
  - plaque-ecoli-meta
  - plaque-ecoli-genes
  - plaque-ecoli-modules
  - plaque-adapter-sa-staph_precise108-meta
  - plaque-adapter-sa-staph_precise108-imodulons
  - plaque-adapter-sa-staph_precise108-genes-query
  - plaque-adapter-sa-staph_precise165-meta
  - plaque-adapter-sa-staph_precise165-imodulons
  - plaque-adapter-sa-staph_precise165-genes-query
  - plaque-adapter-ecoli-b0957-modules
  - plaque-adapter-ecoli-b0929-modules
  - plaque-adapter-ecoli-module-22
  - plaque-adapter-ecoli-module-25
  - plaque-adapter-ecoli-module-86
  - plaque-adapter-ecoli-module-88
  - micro-catalogue
  - micro-ecoli-meta
  - micro-ecoli-genes
  - micro-ecoli-modules
  - micro-dataset-b3702
  - micro-dataset-b0177
  - micro-dataset-b2512
  - micro-dataset-b2477
  - micro-dataset-b2595
  - micro-dataset-b2617
  - micro-dataset-b0565
  - micro-ecoli-module-59
  - micro-ecoli-module-164
- check_id: independent-scientific-review
  name: Independent claim-level source review
  status: passed
  required: true
  target_ids:
  - GO:0044599
  - GO:0030119
  - GO:0020007
  - GO:0097691
  - GO:0061701
  - GO:0036389
  - GO:1990063
  - GO:7770042
  - GO:0033186
  - GO:0031518
  summary: Three read-only reviewers covered the complete ten-record cohort, including
    changed inputs, with explicit scientific findings and source-access limits. Final
    artifact/head acceptance occurs after saving.
  evidence_ids:
  - septin-review-policy
  - septin-curation-policy
  - septin-schema-policy
  - septin-protein-policy
  - septin-graph-policy
  - septin-literature-policy
  - septin-go
  - septin-catalogue
  - septin-tax9606
  - septin-tax5911
  - septin-tax5794
  - septin-tax5811
  - septin-protein-Q2VPB7
  - septin-protein-O43299
  - septin-protein-Q9H0R1
  - septin-protein-Q9NUS5
  - septin-ipr-IPR038741
  - septin-ipr-IPR028222
  - septin-ipr-IPR039591
  - septin-ipr-IPR029392
  - septin-ipr-IPR001392
  - septin-ipr-IPR016635
  - septin-ipr-IPR050431
  - septin-hirst2011-meta
  - septin-pmid-20613862
  - septin-kaur2017-meta
  - septin-hu2006-meta
  - septin-ren2024-meta
  - septin-pmid-9208224
  - septin-boothroyd2008-meta
  - septin-waller2024-meta
  - septin-hirst2011-xml
  - septin-slabicki2010-xml
  - septin-kaur2017-xml
  - septin-hu2006-xml
  - septin-ren2024-xml
  - septin-carruthers1997-pmc
  - plaque-policy
  - plaque-review-skill
  - plaque-protein-skill
  - plaque-schema
  - plaque-review-schema
  - plaque-review-profile
  - plaque-go
  - plaque-SL0489
  - plaque-tax-2
  - plaque-tax-1280
  - plaque-tax-562
  - plaque-tax-4932
  - plaque-tax-559292
  - plaque-toyofuku2019-meta
  - plaque-kim2015-meta
  - plaque-schwechheimer2015-meta
  - plaque-lee2009-meta
  - plaque-lee2007-meta
  - plaque-park2010-meta
  - plaque-kaufman1997-meta
  - plaque-leber2018-meta
  - plaque-yan2018-meta
  - plaque-pmid-11238915
  - plaque-pmid-14562095
  - plaque-pmid-10427094
  - plaque-pmid-9030687
  - plaque-up-Q12495
  - plaque-up-Q04199
  - plaque-up-P13712
  - plaque-up-P35203
  - plaque-up-P52286
  - plaque-up-P40969
  - plaque-up-P32504
  - plaque-ipr-IPR045145
  - plaque-ipr-IPR016897
  - plaque-ipr-IPR001232
  - plaque-ipr-IPR031760
  - plaque-ipr-IPR022210
  - plaque-ipr-IPR062588
  - plaque-ipr-IPR063542
  - plaque-ipr-IPR050459
  - plaque-ipr-IPR048800
  - plaque-ipr-IPR021644
  - plaque-ipr-IPR022043
  - plaque-PMC5771398-jats
  - plaque-PMC6292502-jats
  - plaque-PMC2893157-jats
  - plaque-PMC5308417-jats
  - plaque-PMC3206577-jats
  - plaque-kaufman1997-pdf-download
  - plaque-kim2015-publisher
  - plaque-lee2009-publisher
  - plaque-lee2007-publisher
  - plaque-catalogue
  - plaque-ecoli-meta
  - plaque-ecoli-genes
  - plaque-ecoli-modules
  - plaque-adapter-sa-staph_precise108-meta
  - plaque-adapter-sa-staph_precise108-imodulons
  - plaque-adapter-sa-staph_precise108-genes-query
  - plaque-adapter-sa-staph_precise165-meta
  - plaque-adapter-sa-staph_precise165-imodulons
  - plaque-adapter-sa-staph_precise165-genes-query
  - plaque-adapter-ecoli-b0957-modules
  - plaque-adapter-ecoli-b0929-modules
  - plaque-adapter-ecoli-module-22
  - plaque-adapter-ecoli-module-25
  - plaque-adapter-ecoli-module-86
  - plaque-adapter-ecoli-module-88
  - micro-policy
  - micro-native-policy
  - micro-graph-policy
  - micro-up-P03004
  - micro-up-P09169
  - micro-up-P0A903
  - micro-up-P0A937
  - micro-up-P0A940
  - micro-up-P0AC02
  - micro-up-P77774
  - micro-up-Q97UF5
  - micro-up-Q97UZ1
  - micro-ipr-IPR001957
  - micro-ipr-IPR014524
  - micro-ipr-IPR017687
  - micro-ipr-IPR017689
  - micro-ipr-IPR020591
  - micro-ipr-IPR023707
  - micro-ipr-IPR026592
  - micro-ipr-IPR050490
  - micro-ipr-IPR054925
  - micro-go-0006270
  - micro-go-0009279
  - micro-go-0032993
  - micro-go-0036387
  - micro-go-0036389-is_a
  - micro-go-0036389-part_of
  - micro-go-0036389
  - micro-go-0098796
  - micro-go-0106234
  - micro-go-1990063-is_a
  - micro-go-1990063-part_of
  - micro-go-1990063
  - micro-go-1990100
  - micro-go-1990101
  - micro-go-1990102
  - micro-go-1990103
  - micro-go-7770042-is_a
  - micro-go-7770042-part_of
  - micro-go-7770042
  - micro-tax-562
  - micro-tax-83333
  - micro-tax-2
  - micro-tax-2287
  - micro-tax-273057
  - micro-uo-0000222
  - micro-miller2009-meta
  - micro-leonard2010-meta
  - micro-hagan2010-meta
  - micro-hagan2011-meta
  - micro-gu2016-meta
  - micro-iadanza2016-meta
  - micro-bakelar2016-meta
  - micro-zolghadr2011-meta
  - micro-elferink2001-meta
  - micro-go-bindosome-ref-meta
  - micro-pmid-15851030
  - micro-pmid-16079137
  - micro-pmid-17404237
  - micro-pmid-22574163
  - micro-pmid-23882017
  - micro-pmid-24619089
  - micro-pmid-26900875
  - micro-pmid-28166228
  - micro-pmid-9478970
  - micro-miller2009-legacy
  - micro-leonard2010-body
  - micro-hagan2010-body
  - micro-bakelar2016-body
  - micro-iadanza2016-body
  - micro-gu2016-author
  - micro-zolghadr2011-body
  - micro-albers2003-legacy
  - micro-catalogue
  - micro-ecoli-meta
  - micro-ecoli-genes
  - micro-ecoli-modules
  - micro-ecoli-module-59
  - micro-ecoli-module-164
- check_id: historical-adapter-runner
  name: Retained historical adapter runner availability
  status: unavailable
  required: false
  target_ids:
  - GO:0044599
  - GO:0030119
  - GO:0020007
  - GO:0097691
  - GO:0061701
  - GO:0036389
  - GO:1990063
  - GO:7770042
  - GO:0033186
  - GO:0031518
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
- check_id: ap_5_adaptor_complex-uniprot-verify
  name: Native AP-5 adaptor complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0044599
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/ap_5_adaptor_complex.yaml
    --verify
  exit_code: 0
  summary: 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-ap_5_adaptor_complex-uniprot-verify
- check_id: ap_5_adaptor_complex-uniprot-causal
  name: Native AP-5 adaptor complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0044599
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/ap_5_adaptor_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-ap_5_adaptor_complex-uniprot-causal
- check_id: ap_type_membrane_coat_adaptor_complex-uniprot-verify
  name: Native AP-type membrane coat adaptor complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0030119
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/ap_type_membrane_coat_adaptor_complex.yaml
    --verify
  exit_code: 0
  summary: 0 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-ap_type_membrane_coat_adaptor_complex-uniprot-verify
- check_id: ap_type_membrane_coat_adaptor_complex-uniprot-causal
  name: Native AP-type membrane coat adaptor complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0030119
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/ap_type_membrane_coat_adaptor_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 0 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-ap_type_membrane_coat_adaptor_complex-uniprot-causal
- check_id: apical_complex-uniprot-verify
  name: Native apical complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0020007
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/apical_complex.yaml
    --verify
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-apical_complex-uniprot-verify
- check_id: apical_complex-uniprot-causal
  name: Native apical complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0020007
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/apical_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-apical_complex-uniprot-causal
- check_id: bacterial_extracellular_vesicle-uniprot-verify
  name: Native bacterial extracellular vesicle UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0097691
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/bacterial_extracellular_vesicle.yaml
    --verify
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-bacterial_extracellular_vesicle-uniprot-verify
- check_id: bacterial_extracellular_vesicle-uniprot-causal
  name: Native bacterial extracellular vesicle UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0097691
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/bacterial_extracellular_vesicle.yaml
    --causal-graphs
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-bacterial_extracellular_vesicle-uniprot-causal
- check_id: bacterial_outer_membrane_vesicle-uniprot-verify
  name: Native bacterial outer membrane vesicle UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0061701
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/bacterial_outer_membrane_vesicle.yaml
    --verify
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-bacterial_outer_membrane_vesicle-uniprot-verify
- check_id: bacterial_outer_membrane_vesicle-uniprot-causal
  name: Native bacterial outer membrane vesicle UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0061701
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/bacterial_outer_membrane_vesicle.yaml
    --causal-graphs
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-bacterial_outer_membrane_vesicle-uniprot-causal
- check_id: bacterial_pre_replicative_complex-uniprot-verify
  name: Native bacterial pre-replicative complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0036389
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/bacterial_pre_replicative_complex.yaml
    --verify
  exit_code: 0
  summary: 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-bacterial_pre_replicative_complex-uniprot-verify
- check_id: bacterial_pre_replicative_complex-uniprot-causal
  name: Native bacterial pre-replicative complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0036389
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/bacterial_pre_replicative_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-bacterial_pre_replicative_complex-uniprot-causal
- check_id: bam_protein_complex-uniprot-verify
  name: Native Bam protein complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:1990063
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/bam_protein_complex.yaml
    --verify
  exit_code: 0
  summary: 5 represented protein examples; 8 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-bam_protein_complex-uniprot-verify
- check_id: bam_protein_complex-uniprot-causal
  name: Native Bam protein complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:1990063
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/bam_protein_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 5 represented protein examples; 8 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-bam_protein_complex-uniprot-causal
- check_id: bindosome_complex-uniprot-verify
  name: Native bindosome complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:7770042
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/bindosome_complex.yaml
    --verify
  exit_code: 0
  summary: 2 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-bindosome_complex-uniprot-verify
- check_id: bindosome_complex-uniprot-causal
  name: Native bindosome complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:7770042
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/bindosome_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 2 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-bindosome_complex-uniprot-causal
- check_id: caf_1_complex-uniprot-verify
  name: Native CAF-1 complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0033186
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/caf_1_complex.yaml
    --verify
  exit_code: 0
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-caf_1_complex-uniprot-verify
- check_id: caf_1_complex-uniprot-causal
  name: Native CAF-1 complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0033186
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/caf_1_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-caf_1_complex-uniprot-causal
- check_id: cbf3_complex-uniprot-verify
  name: Native CBF3 complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0031518
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/cbf3_complex.yaml
    --verify
  exit_code: 0
  summary: 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-cbf3_complex-uniprot-verify
- check_id: cbf3_complex-uniprot-causal
  name: Native CBF3 complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0031518
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/cbf3_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-cbf3_complex-uniprot-causal
evidence:
- evidence_id: current-record-0
  kind: record_content
  reference: data/structures/other/ap_5_adaptor_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T02:14:28Z'
  support: context_only
  summary: Original frozen SHA256 d951b48b8f9fe05db066c722dd2dad8277f04eb4af1ac36bf4a5c03932ac82dc;
    current SHA256 d951b48b8f9fe05db066c722dd2dad8277f04eb4af1ac36bf4a5c03932ac82dc.
    Record bytes unchanged since the original review.
  snapshot_sha256: d951b48b8f9fe05db066c722dd2dad8277f04eb4af1ac36bf4a5c03932ac82dc
- evidence_id: original-review-0
  kind: prior_review
  reference: reviews/structured/20261022T044318Z-ap-5-adaptor-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T02:14:28Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 202ed0adb6576cec2f53d0534cab118b16f81c35af955690259134befbf41b11
- evidence_id: current-record-1
  kind: record_content
  reference: data/structures/other/ap_type_membrane_coat_adaptor_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T02:14:28Z'
  support: context_only
  summary: Original frozen SHA256 a16a52e7091df279f222b922baa48be321173ab9dc132e1c2be2384d48ca626b;
    current SHA256 a16a52e7091df279f222b922baa48be321173ab9dc132e1c2be2384d48ca626b.
    Record bytes unchanged since the original review.
  snapshot_sha256: a16a52e7091df279f222b922baa48be321173ab9dc132e1c2be2384d48ca626b
- evidence_id: original-review-1
  kind: prior_review
  reference: reviews/structured/20261022T044319Z-ap-type-membrane-coat-adaptor-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T02:14:28Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: f9d5ddaf668a4d93b705ec4a49a37c5e2ca8aad1c0a85aa6dba40bd9d2fb681c
- evidence_id: current-record-2
  kind: record_content
  reference: data/structures/other/apical_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T02:14:28Z'
  support: context_only
  summary: Original frozen SHA256 72b670707751292b450e4c8bccddb25a4a14e482fc0eaaa85975681694f55952;
    current SHA256 72b670707751292b450e4c8bccddb25a4a14e482fc0eaaa85975681694f55952.
    Record bytes unchanged since the original review.
  snapshot_sha256: 72b670707751292b450e4c8bccddb25a4a14e482fc0eaaa85975681694f55952
- evidence_id: original-review-2
  kind: prior_review
  reference: reviews/structured/20261022T044320Z-apical-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T02:14:28Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 6bb778c0edffbb843e663f1308b557e9098f56e563497650cba09816ab21964f
- evidence_id: current-record-3
  kind: record_content
  reference: data/structures/other/bacterial_extracellular_vesicle.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T02:14:28Z'
  support: context_only
  summary: Original frozen SHA256 43f0f6e0dfef8fc8533bbbac4c5a1583adc6626873f52b92f2edbc32560137d2;
    current SHA256 43f0f6e0dfef8fc8533bbbac4c5a1583adc6626873f52b92f2edbc32560137d2.
    Record bytes unchanged since the original review.
  snapshot_sha256: 43f0f6e0dfef8fc8533bbbac4c5a1583adc6626873f52b92f2edbc32560137d2
- evidence_id: original-review-3
  kind: prior_review
  reference: reviews/structured/20261022T044321Z-bacterial-extracellular-vesicle-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T02:14:28Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: a07011482846bfeed4934761a86a5bbe024017036df6e25efb36babf13f972ed
- evidence_id: current-record-4
  kind: record_content
  reference: data/structures/other/bacterial_outer_membrane_vesicle.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T02:14:28Z'
  support: context_only
  summary: Original frozen SHA256 ae635da7dc9351f59de2b4283aa2d572b200cf9eba187147c027e5e86b445a34;
    current SHA256 ae635da7dc9351f59de2b4283aa2d572b200cf9eba187147c027e5e86b445a34.
    Record bytes unchanged since the original review.
  snapshot_sha256: ae635da7dc9351f59de2b4283aa2d572b200cf9eba187147c027e5e86b445a34
- evidence_id: original-review-4
  kind: prior_review
  reference: reviews/structured/20261022T044321Z-bacterial-outer-membrane-vesicle-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T02:14:28Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 891ea995b50bff90b1e4817858ae96afba7ea596b2fdc92f7d2e3c74aa6198c0
- evidence_id: current-record-5
  kind: record_content
  reference: data/structures/other/bacterial_pre_replicative_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T02:14:28Z'
  support: context_only
  summary: Original frozen SHA256 a4a8871a963f0b0eb3e32d9a677f099afdf3f6246dc7964f1890b61b3f01b62a;
    current SHA256 a4a8871a963f0b0eb3e32d9a677f099afdf3f6246dc7964f1890b61b3f01b62a.
    Record bytes unchanged since the original review.
  snapshot_sha256: a4a8871a963f0b0eb3e32d9a677f099afdf3f6246dc7964f1890b61b3f01b62a
- evidence_id: original-review-5
  kind: prior_review
  reference: reviews/structured/20261022T044322Z-bacterial-pre-replicative-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T02:14:28Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 0f46df59f2c24561a55cb0bcfca7d535e1c71e83a8407a5ff446e73dfcd548fe
- evidence_id: current-record-6
  kind: record_content
  reference: data/structures/other/bam_protein_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T02:14:28Z'
  support: context_only
  summary: Original frozen SHA256 caa3620dc7868afb69744609d3f28450d13ce822789d33224fab2e805a49a8dd;
    current SHA256 ac284bcf4e0ec8021b0f218143e2337a0845c36113edb097e79c950ac1688cde.
    Changed record reassessed against current sources.
  snapshot_sha256: ac284bcf4e0ec8021b0f218143e2337a0845c36113edb097e79c950ac1688cde
- evidence_id: original-review-6
  kind: prior_review
  reference: reviews/structured/20261022T044323Z-bam-protein-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T02:14:28Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 85a2536611ef781a45b0f5e986a05214590cfad7b7237a67e89ae26e8cec3772
- evidence_id: current-record-7
  kind: record_content
  reference: data/structures/other/bindosome_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T02:14:28Z'
  support: context_only
  summary: Original frozen SHA256 b684ece5758180f8afba192ccad06e0938cbda33953c9390eadbbf7ce01fab91;
    current SHA256 360a186c82ed29ddaae42fdbcb445a37b8482be97bed64a6d077792b8fdce375.
    Changed record reassessed against current sources.
  snapshot_sha256: 360a186c82ed29ddaae42fdbcb445a37b8482be97bed64a6d077792b8fdce375
- evidence_id: original-review-7
  kind: prior_review
  reference: reviews/structured/20261022T044323Z-bindosome-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T02:14:28Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 3c4e32c35bf0fd463a99f3c7c3a97043f9816189dd950b3fa5e227fd7e55abcd
- evidence_id: current-record-8
  kind: record_content
  reference: data/structures/other/caf_1_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T02:14:28Z'
  support: context_only
  summary: Original frozen SHA256 9cfaf9ce52f019ddb3125428f3c6ce7cb17ae2e476fbd0fb9be2e0bcad652576;
    current SHA256 9cfaf9ce52f019ddb3125428f3c6ce7cb17ae2e476fbd0fb9be2e0bcad652576.
    Record bytes unchanged since the original review.
  snapshot_sha256: 9cfaf9ce52f019ddb3125428f3c6ce7cb17ae2e476fbd0fb9be2e0bcad652576
- evidence_id: original-review-8
  kind: prior_review
  reference: reviews/structured/20261022T044324Z-caf-1-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T02:14:28Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: fb4dcdc6295e05feeb8a72463af97b1b7500ddf7271053658bcff165d5af253c
- evidence_id: current-record-9
  kind: record_content
  reference: data/structures/other/cbf3_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T02:14:28Z'
  support: context_only
  summary: Original frozen SHA256 8afa05438831e653a16909b6f127778342b1de47b324a3994c5f374937d9829a;
    current SHA256 9cf3d32f5094ac6a00417cb7b7c125b45a4329e364d8e721314f19349baf44f2.
    Changed record reassessed against current sources.
  snapshot_sha256: 9cf3d32f5094ac6a00417cb7b7c125b45a4329e364d8e721314f19349baf44f2
- evidence_id: original-review-9
  kind: prior_review
  reference: reviews/structured/20261022T044325Z-cbf3-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T02:14:28Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 324587ca73380b88cc7da048e16d12ec28469bc06f28c7ff7b2f22bd00dda44f
- evidence_id: septin-review-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Complete scientific/source review; structured molecular source checks
  summary: Positive molecular and pathway assertions anywhere in a record trigger
    actual structured-source applicability assessment; expression-only exclusions
    are insufficient.
  accessed_at: '2026-11-04T02:05:50.546746Z'
  support: supports
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: septin-curation-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Family/class constituents, grounding status, formation necessity, append-only
    rationale
  summary: Protein classes are permitted; exact assertable family grounding differs
    from reviewed-label-only status. Missing optional examples are not automatically
    defects. Dated rationale/history remain append-only.
  accessed_at: '2026-11-04T02:05:50.546746Z'
  support: supports
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
- evidence_id: septin-schema-policy
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Component grounding_status, formation essentiality, graph nodes and scope
  summary: Family/class and complex representations are allowed. Verified identifiers
    must denote the stated class. UNKNOWN formation necessity and explicitly nonmechanistic
    functional graphs must not be inflated.
  accessed_at: '2026-11-04T02:05:50.546746Z'
  support: supports
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: septin-protein-policy
  kind: authority
  reference: .claude/skills/uniprot-protein-examples/SKILL.md
  locator: Primary/synonym identity, taxon/reviewed status, bounded queries, representative
    selection
  summary: Native accession and gene-query coverage do not independently establish
    experimental localization or universal necessity. Queries are bounded observations,
    not reconstructed historical executions.
  accessed_at: '2026-11-04T02:05:50.546746Z'
  support: supports
  snapshot_sha256: 6462894c8257823bae2b175c34693cd42f11ff9269a3829c15b9286ba6d7c876
- evidence_id: septin-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: FUNCTION/NONMECHANISTIC scope and evidence placement
  summary: Coarse structural and functional summaries do not certify an experimentally
    resolved assembly cycle or individual subunit necessity.
  accessed_at: '2026-11-04T02:05:50.546746Z'
  support: supports
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: septin-literature-policy
  kind: authority
  reference: .claude/skills/literature-evidence/SKILL.md
  locator: Primary sources, abstract/body/pixel scope and source failure
  summary: Access tier and actual read extents must be explicit; challenge pages and
    metadata cannot certify unread experimental details.
  accessed_at: '2026-11-04T02:05:50.546746Z'
  support: supports
  snapshot_sha256: f7c3c594b5fb2cd7d4d700844fce3b97c91cc382d4fdca8b2e2a96cf16abd41b
- evidence_id: septin-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0044599,GO:0030119,GO:0098796,GO:0030117,GO:0020007,GO:0020010,GO:0020031,GO:0020008,GO:0020009
  locator: 'All nine requested term objects: exact identifiers, labels, complete definitions
    and relevant typed hierarchy relations'
  summary: GO0044599 is exact AP5 and child of GO0030119; the generic parent retains
    an outdated exhaustive subunit/mass gloss despite including AP5. GO0020007 is
    the apical composite with conoid, polar-ring, rhoptry and microneme relations.
    GO0020031 label/aliases and definition show the bounded preconoidal-ring versus
    APR tension discussed separately; no replacement identifier is guessed.
  accessed_at: '2026-11-04T01:59:15.316969Z'
  support: supports
  snapshot_sha256: a713b4e9448e2e08e74e577c6dc7c355ca849d5fbbb7c1de1889f1efec199a1a
- evidence_id: septin-catalogue
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Complete returned official datasets catalogue; all organism/dataset rows
    inspected
  summary: No native human, Tetrahymena or Toxoplasma/Apicomplexa host dataset occurs
    in this returned catalogue. Bacterial recombinant production or heterologous yeast
    assays are not substitutes. Downstream matched-module queries are not applicable
    after this bounded coverage assessment; lack of coverage is not biological absence.
  accessed_at: '2026-11-04T01:59:20.124731Z'
  support: supports
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: septin-tax9606
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/9606
  locator: 'Complete ENA taxonomy object: taxonId, scientificName, rank and lineage'
  summary: Exact identities/ranks distinguish human species9606, Tetrahymena thermophila
    species5911, Apicomplexa phylum5794 and Toxoplasma gondii species5811. Taxonomy
    does not establish quantitative prevalence or the strain used in a particular
    experiment.
  accessed_at: '2026-11-04T01:59:15.306485Z'
  support: supports
  snapshot_sha256: ae6861231eabbe5c76a3e6240a9109a3163b77f2061b644c22bbdd1b01b15840
- evidence_id: septin-tax5911
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5911
  locator: 'Complete ENA taxonomy object: taxonId, scientificName, rank and lineage'
  summary: Exact identities/ranks distinguish human species9606, Tetrahymena thermophila
    species5911, Apicomplexa phylum5794 and Toxoplasma gondii species5811. Taxonomy
    does not establish quantitative prevalence or the strain used in a particular
    experiment.
  accessed_at: '2026-11-04T01:59:18.081136Z'
  support: supports
  snapshot_sha256: e848a1295088ad42e73c4c2c42d45869b4c9c2b10858e2c32086dc67b066a8c5
- evidence_id: septin-tax5794
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5794
  locator: 'Complete ENA taxonomy object: taxonId, scientificName, rank and lineage'
  summary: Exact identities/ranks distinguish human species9606, Tetrahymena thermophila
    species5911, Apicomplexa phylum5794 and Toxoplasma gondii species5811. Taxonomy
    does not establish quantitative prevalence or the strain used in a particular
    experiment.
  accessed_at: '2026-11-04T01:59:19.139845Z'
  support: supports
  snapshot_sha256: 617b42c27ae95a801b69abf63e1a545eff8565fd0af2f4a81be359d3fb6b3cbf
- evidence_id: septin-tax5811
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5811
  locator: 'Complete ENA taxonomy object: taxonId, scientificName, rank and lineage'
  summary: Exact identities/ranks distinguish human species9606, Tetrahymena thermophila
    species5911, Apicomplexa phylum5794 and Toxoplasma gondii species5811. Taxonomy
    does not establish quantitative prevalence or the strain used in a particular
    experiment.
  accessed_at: '2026-11-04T01:59:19.302940Z'
  support: supports
  snapshot_sha256: cbb209002c87051ce78d0a34bc169d2f6623f6bbfbb21edad170d43eb16d4032
- evidence_id: septin-protein-Q2VPB7
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q2VPB7.json
  locator: Native accession identity, recommended/alternative names, gene names, organism/reviewed
    entryType, sequence mass, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and InterPro
    cross-references
  summary: Reviewed human AP5B1 beta5; primary AP5B1, ORF PP1030; length878 and canonical
    sequence mass93949Da; exact family IPR038741. Sequence mass is predicted for the
    canonical protein, not a measured assembled-complex mass; authority identity is
    not a new localization/necessity experiment.
  accessed_at: '2026-11-04T01:59:16.146339Z'
  support: supports
  snapshot_sha256: 05e9ffb34a92f4558d354dc78b6e8dea7417623b9c890fc8dfd06db95aacd1aa
- evidence_id: septin-protein-O43299
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/O43299.json
  locator: Native accession identity, recommended/alternative names, gene names, organism/reviewed
    entryType, sequence mass, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and InterPro
    cross-references
  summary: Reviewed human AP5Z1 zeta; primary AP5Z1, synonyms KIAA0415/SPG48; length807
    and canonical sequence mass88605Da; exact family IPR028222. Slabicki isoform-specific
    cytoplasmic/nuclear localization is distinct from a universal AP5 localization
    claim. Sequence mass is predicted for the canonical protein, not a measured assembled-complex
    mass; authority identity is not a new localization/necessity experiment.
  accessed_at: '2026-11-04T01:59:16.911294Z'
  support: supports
  snapshot_sha256: bd057a0050e1996d438e5d681e2fa6e4880291b6d1cbb3131a526814cdfc75e6
- evidence_id: septin-protein-Q9H0R1
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q9H0R1.json
  locator: Native accession identity, recommended/alternative names, gene names, organism/reviewed
    entryType, sequence mass, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and InterPro
    cross-references
  summary: Reviewed human AP5M1 mu5; primary AP5M1, synonyms C14orf108/MUDENG; length490
    and sequence mass54767Da; exact family IPR039591. Experimental cytosol and inferred
    late-endosome membrane annotations are distinguished. Sequence mass is predicted
    for the canonical protein, not a measured assembled-complex mass; authority identity
    is not a new localization/necessity experiment.
  accessed_at: '2026-11-04T01:59:17.919548Z'
  support: supports
  snapshot_sha256: d600d7c33bdcca4c1527efcd998c894208cc86d259ce0b64158985fb8843000a
- evidence_id: septin-protein-Q9NUS5
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q9NUS5.json
  locator: Native accession identity, recommended/alternative names, gene names, organism/reviewed
    entryType, sequence mass, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and InterPro
    cross-references
  summary: Reviewed human AP5S1 sigma5; primary AP5S1, synonym C20orf29; length200
    and sequence mass22522Da; exact family IPR029392. Experimental cytosol and inferred
    endosome annotations are distinguished. Sequence mass is predicted for the canonical
    protein, not a measured assembled-complex mass; authority identity is not a new
    localization/necessity experiment.
  accessed_at: '2026-11-04T01:59:17.872314Z'
  support: supports
  snapshot_sha256: 66fd01cea60ce9fbd64f05f7870b05a0e4c1dadcf6110e97bf7174c332d1b5d3
- evidence_id: septin-gene-AP5B1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=100&query=%28gene_exact%3AAP5B1%29%20AND%20%28organism_id%3A9606%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete returned JSON and result-count/pagination headers
  summary: One reviewed human intended primary-gene entry is returned by this current
    exact query. This supports bounded current identity/uniqueness, not reconstruction
    of the October retrieval.
  accessed_at: '2026-11-04T01:59:17.060265Z'
  support: supports
  snapshot_sha256: 35ba81ef29bbebeb0ba091ca930351c9d1b6aca5c19eb646768f8be5de214139
  search_scope: UniProt REST query (gene_exact:AP5B1) AND (organism_id:9606) AND (reviewed:true),
    format=json,size=100,no date filter; complete returned single page inspected at
    2026-11-04T01:59:17.060265Z.
- evidence_id: septin-gene-AP5Z1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=100&query=%28gene_exact%3AAP5Z1%29%20AND%20%28organism_id%3A9606%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete returned JSON and result-count/pagination headers
  summary: One reviewed human intended primary-gene entry is returned by this current
    exact query. This supports bounded current identity/uniqueness, not reconstruction
    of the October retrieval.
  accessed_at: '2026-11-04T01:59:16.872110Z'
  support: supports
  snapshot_sha256: 0496b6b2fbc12203d00ad86cbd6af7cf0d05e5b2a7cd3b490c0e398df9a07234
  search_scope: UniProt REST query (gene_exact:AP5Z1) AND (organism_id:9606) AND (reviewed:true),
    format=json,size=100,no date filter; complete returned single page inspected at
    2026-11-04T01:59:16.872110Z.
- evidence_id: septin-gene-AP5M1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=100&query=%28gene_exact%3AAP5M1%29%20AND%20%28organism_id%3A9606%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete returned JSON and result-count/pagination headers
  summary: One reviewed human intended primary-gene entry is returned by this current
    exact query. This supports bounded current identity/uniqueness, not reconstruction
    of the October retrieval.
  accessed_at: '2026-11-04T01:59:18.893481Z'
  support: supports
  snapshot_sha256: 2dfaea9dbf6ef344272f604d7f62de6a27e145c91fe01a5a8f5433f63f474c78
  search_scope: UniProt REST query (gene_exact:AP5M1) AND (organism_id:9606) AND (reviewed:true),
    format=json,size=100,no date filter; complete returned single page inspected at
    2026-11-04T01:59:18.893481Z.
- evidence_id: septin-gene-AP5S1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=100&query=%28gene_exact%3AAP5S1%29%20AND%20%28organism_id%3A9606%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete returned JSON and result-count/pagination headers
  summary: One reviewed human intended primary-gene entry is returned by this current
    exact query. This supports bounded current identity/uniqueness, not reconstruction
    of the October retrieval.
  accessed_at: '2026-11-04T01:59:18.973536Z'
  support: supports
  snapshot_sha256: cff0f5c7bcdcdab9ec7b2441c9b85f18cc968db1dc05ebbe3e6b1fd6f26e555e
  search_scope: UniProt REST query (gene_exact:AP5S1) AND (organism_id:9606) AND (reviewed:true),
    format=json,size=100,no date filter; complete returned single page inspected at
    2026-11-04T01:59:18.973536Z.
- evidence_id: septin-ipr-IPR038741
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR038741/
  locator: Complete native metadata accession/name/type, description, member databases,
    hierarchy and LLM flags
  summary: Exact AP5 beta5 family. Relevant descriptions have false LLM flags. Broad
    parents/domains are not substituted for exact subtype or pan-adaptor classes.
  accessed_at: '2026-11-04T01:59:15.908661Z'
  support: supports
  snapshot_sha256: 9dcc8b54579b5d9162aded260904a30a25bc944333b8958eabb7014cfdd79869
- evidence_id: septin-ipr-IPR028222
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR028222/
  locator: Complete native metadata accession/name/type, description, member databases,
    hierarchy and LLM flags
  summary: Exact AP5 zeta family. Relevant descriptions have false LLM flags. Broad
    parents/domains are not substituted for exact subtype or pan-adaptor classes.
  accessed_at: '2026-11-04T01:59:16.535173Z'
  support: supports
  snapshot_sha256: 58606c459d23c3d8d20143f67c466f88cdb3e326282c429ace58956157d96681
- evidence_id: septin-ipr-IPR039591
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR039591/
  locator: Complete native metadata accession/name/type, description, member databases,
    hierarchy and LLM flags
  summary: Exact AP5 mu5 family. Relevant descriptions have false LLM flags. Broad
    parents/domains are not substituted for exact subtype or pan-adaptor classes.
  accessed_at: '2026-11-04T01:59:16.776031Z'
  support: supports
  snapshot_sha256: bc6b499374cb70c152fcb68597afe765a3bd0925d9508583ab1fb85cbcf5071f
- evidence_id: septin-ipr-IPR029392
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR029392/
  locator: Complete native metadata accession/name/type, description, member databases,
    hierarchy and LLM flags
  summary: Exact AP5 sigma5 family. Relevant descriptions have false LLM flags. Broad
    parents/domains are not substituted for exact subtype or pan-adaptor classes.
  accessed_at: '2026-11-04T01:59:17.395381Z'
  support: supports
  snapshot_sha256: 761eb11d006f3b3da7b2d822e6f90cfcd6ce3a6b5ee11dd15b848a7b68fe7649
- evidence_id: septin-ipr-IPR001392
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001392/
  locator: Complete native metadata accession/name/type, description, member databases,
    hierarchy and LLM flags
  summary: Broader AP1/2/3 mu family, not a demonstrated all-AP1–5 exact class. Relevant
    descriptions have false LLM flags. Broad parents/domains are not substituted for
    exact subtype or pan-adaptor classes.
  accessed_at: '2026-11-04T01:59:48.060516Z'
  support: supports
  snapshot_sha256: b514537350700a251483339024cec9ab501f94f7bcb632df44e9dcd5aa3415f4
- evidence_id: septin-ipr-IPR016635
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016635/
  locator: Complete native metadata accession/name/type, description, member databases,
    hierarchy and LLM flags
  summary: Broader sigma family with AP1/2/3 children, not a demonstrated all-AP1–5
    exact class. Relevant descriptions have false LLM flags. Broad parents/domains
    are not substituted for exact subtype or pan-adaptor classes.
  accessed_at: '2026-11-04T01:59:18.540974Z'
  support: supports
  snapshot_sha256: 597cc84578003af4a8f1b735aab9676edda62e82a0a06a4fa1422f1658b8aa8e
- evidence_id: septin-ipr-IPR050431
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050431/
  locator: Native accession/name/type, member-database identity and description-generation
    flags
  summary: The entry is family type with PTHR10529 member identity; its description
    has llm=true, checked=false and is_reviewed_llm=false. Generated prose is not
    used as independent biological evidence or promoted to a verified pan-AP/stonin
    mapping. The original already disclosed this limitation.
  accessed_at: '2026-11-04T01:59:18.706323Z'
  support: context_only
  snapshot_sha256: f6aa5a0da750163b88408d601261a89db56358b059b57f8ca55d50f83e6d07d8
- evidence_id: septin-family-search-AP5
  kind: search
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/?search=AP-5&page_size=200
  locator: All nine returned InterPro candidate objects; next=null
  summary: The four exact AP5 families are distinguished from returned domain candidates.
    This is a bounded candidate search, not a claim that no other relevant entry exists
    anywhere.
  accessed_at: '2026-11-04T01:59:16.733080Z'
  support: supports
  snapshot_sha256: 22f406bd1fcb40745c7db59270746fae6de5c3ed49599fbc7ff3d2635b3896ab
  search_scope: InterPro API entry/interpro search=AP-5,page_size=200,no date or taxon
    filter; complete returned page inspected at 2026-11-04T01:59:16.733080Z.
- evidence_id: septin-hirst2011-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1371/journal.pbio.1001170%22&pageSize=100
  locator: Complete unique MED bibliographic metadata, authors, DOI/PMID/PMCID where
    present and returned abstract
  summary: Hirst2011 identifies AP5 with endosomal localization and trafficking phenotypes;
    full fresh body is separately scoped.
  accessed_at: '2026-11-04T01:59:15.365387Z'
  support: supports
  snapshot_sha256: d54458b7bd72c67c1a5c45027f6c2a31f01aa78a9f67554d8bf916493d1cdd26
  search_scope: Europe PMC REST exact DOI or MED PMID query encoded in reference URL,resultType=core,format=json,pageSize=100,no
    date filter; complete unique hit/abstract read at 2026-11-04T01:59:15.365387Z.
- evidence_id: septin-pmid-20613862
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A20613862%20AND%20SRC%3AMED&pageSize=100
  locator: Complete unique MED bibliographic metadata, authors, DOI/PMID/PMCID where
    present and returned abstract
  summary: Slabicki2010 identifies KIAA0415/SPG48 and interacting proteins; measured
    isoform localization and coimmunoprecipitation are distinct from its then-putative
    helicase interpretation, not adopted as a current AP5 mechanism.
  accessed_at: '2026-11-04T01:59:15.356394Z'
  support: supports
  snapshot_sha256: 9ffa7061f42ab88cd567902f2c65ac66e9a3a7442d8111c288c559abb5a912f4
  search_scope: Europe PMC REST exact DOI or MED PMID query encoded in reference URL,resultType=core,format=json,pageSize=100,no
    date filter; complete unique hit/abstract read at 2026-11-04T01:59:15.356394Z.
- evidence_id: septin-kaur2017-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1091%2Fmbc.e17-01-0018&format=json&resultType=core&pageSize=100
  locator: Complete unique MED bibliographic metadata, authors, DOI/PMID/PMCID where
    present and returned abstract
  summary: Kaur2017 tests Tetrahymena AP3-dependent mature mucocyst biogenesis; initial
    immature intermediates persist.
  accessed_at: '2026-11-04T01:59:18.007430Z'
  support: supports
  snapshot_sha256: be3de304a895f5c2daa4e479813c3978f1ef42c9792718f5fcd61798643aaca2
  search_scope: Europe PMC REST exact DOI or MED PMID query encoded in reference URL,resultType=core,format=json,pageSize=100,no
    date filter; complete unique hit/abstract read at 2026-11-04T01:59:18.007430Z.
- evidence_id: septin-hu2006-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1371/journal.ppat.0020013%22&pageSize=100
  locator: Complete unique MED bibliographic metadata, authors, DOI/PMID/PMCID where
    present and returned abstract
  summary: Hu2006 identifies candidate Toxoplasma cytoskeletal proteins using partial
    apical-complex enrichment; it is not a purified complete composite-organelle inventory.
  accessed_at: '2026-11-04T01:59:19.567247Z'
  support: supports
  snapshot_sha256: ecd5428def487fe348ad21c7c99b13e2f596119dd903571eeed00da95137999a
  search_scope: Europe PMC REST exact DOI or MED PMID query encoded in reference URL,resultType=core,format=json,pageSize=100,no
    date filter; complete unique hit/abstract read at 2026-11-04T01:59:19.567247Z.
- evidence_id: septin-ren2024-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1073/pnas.2416602121%22&pageSize=100
  locator: Complete unique MED bibliographic metadata, authors, DOI/PMID/PMCID where
    present and returned abstract
  summary: Ren2024 experimentally distinguishes APR layers and their motility/invasion
    roles; it does not establish universal AP-complex-wide secretion coordination.
  accessed_at: '2026-11-04T01:59:19.737367Z'
  support: supports
  snapshot_sha256: 98344e0e55feaae5f05a7aeb94dda95cc371241c16f2ce5543ffca2f26d4b025
  search_scope: Europe PMC REST exact DOI or MED PMID query encoded in reference URL,resultType=core,format=json,pageSize=100,no
    date filter; complete unique hit/abstract read at 2026-11-04T01:59:19.737367Z.
- evidence_id: septin-pmid-9208224
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A9208224%20AND%20SRC%3AMED&pageSize=100
  locator: Complete unique MED bibliographic metadata, authors, DOI/PMID/PMCID where
    present and returned abstract
  summary: Carruthers/Sibley1997 measures ordered microneme/rhoptry/dense-granule
    secretion during Toxoplasma host-cell invasion; fresh genuine body scopes are
    recorded separately.
  accessed_at: '2026-11-04T01:59:19.915523Z'
  support: supports
  snapshot_sha256: a7efeec194d37ff52c350cb8d3358850a2abb6e41bbb2aa48c34ba4640ee1c25
  search_scope: Europe PMC REST exact DOI or MED PMID query encoded in reference URL,resultType=core,format=json,pageSize=100,no
    date filter; complete unique hit/abstract read at 2026-11-04T01:59:19.915523Z.
- evidence_id: septin-boothroyd2008-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1038%2Fnrmicro1800&pageSize=100
  locator: Complete unique MED bibliographic metadata, authors, DOI/PMID/PMCID where
    present and returned abstract
  summary: Boothroyd/Dubremetz2008 is a secondary rhoptry review. Complete MED metadata
    and abstract only are verified in this pass; no current genuine full body or detailed
    Key Points is claimed.
  accessed_at: '2026-11-04T01:59:20.342063Z'
  support: supports
  snapshot_sha256: e80d7f5a4a069f77b362f18ec6130955645891773c211a3f126e91aba73b9d56
  search_scope: Europe PMC REST exact DOI or MED PMID query encoded in reference URL,resultType=core,format=json,pageSize=100,no
    date filter; complete unique hit/abstract read at 2026-11-04T01:59:20.342063Z.
- evidence_id: septin-waller2024-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1128%2Fmmbr.00197-22&pageSize=100
  locator: Complete unique MED bibliographic metadata, authors, DOI/PMID/PMCID where
    present and returned abstract
  summary: Waller2024 is a secondary apical-complex review. Complete MED metadata/abstract
    support bounded comparative/evolutionary context, not a prevalence census or universal
    stage-specific inventory; current full-body access failed.
  accessed_at: '2026-11-04T01:59:21.252639Z'
  support: supports
  snapshot_sha256: 7c217d4a1f49296993947d8c0c581a8c7c1958f648aae3a83affa331a97437f1
  search_scope: Europe PMC REST exact DOI or MED PMID query encoded in reference URL,resultType=core,format=json,pageSize=100,no
    date filter; complete unique hit/abstract read at 2026-11-04T01:59:21.252639Z.
- evidence_id: septin-hirst2011-xml
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3191125/fullTextXML
  locator: 'Fresh genuine JATS: Introduction s1; Results s2a,b,c,d,f including Figures1–4,8–9
    captions and Table1 cells/explanation; Discussion s3 including Figure10 caption;
    Methods s4c,d,e'
  summary: HeLaM and tagged/co-IP experiments support AP5 heterotetramer and endosomal
    sorting implications. Corrected beta5 is878aa/predicted94kDa; zeta/sigma are fourth-complex-chain
    identities. Endogenous mu antibody was unsuitable for IF; controlled tagged constructs
    support LAMP1 association. CI-MPR/Vps26 redistribution and swollen MVB/tubules
    are phenotypes, not a fully resolved cargo route. Tested lack of CCV enrichment/clathrin
    association is not a universal no-coat theorem. Phylogeny sections, other methods,
    supplement and figure pixels were not inspected.
  accessed_at: '2026-11-04T01:59:16.038580Z'
  support: supports
  snapshot_sha256: 0768f8cbad56fcc2885542c578a4b656859fca5ba30ce216a85d16782e1f6571
- evidence_id: septin-slabicki2010-xml
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2893954/fullTextXML
  locator: 'Fresh genuine JATS: Results s2e,s2f with Figures3–6 captions; Methods
    s4j coimmunoprecipitation/MS and s4k fractionation'
  summary: Near-physiologic tagged KIAA0415/HeLa experiments distinguish shorter nuclear
    and longer cytoplasmic isoforms and interacting proteins. This supports the bounded
    AP5Z1 localization note, not universal cytoplasmic occupancy or a proven helicase
    mechanism. Other sections, supplements and figure pixels were not audited.
  accessed_at: '2026-11-04T01:59:15.994824Z'
  support: supports
  snapshot_sha256: fe7ac53d14ba2ca6fc0b911e4bb714161b8e1abec29b00277fcc8073e8cc5c32
- evidence_id: septin-kaur2017-xml
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5449153/fullTextXML
  locator: Fresh genuine JATS Results sec3–6 with Figures1–4 captions; Methods sec14/15
  summary: Tetrahymena CU428.1-background macronuclear APM3 knockout remains viable
    without growth defect but fails normal mature mucocyst biogenesis; immature cargo/protease-bearing
    intermediates and some docking persist. AP3 is a maturation pathway example, not
    a stable mature mucocyst subunit. Tagged Apm3 aggregation leaves endogenous localization
    unresolved; proposed delivery mechanism is hypothetical. No complete Discussion,
    supplements or figure pixels are claimed in this fresh read.
  accessed_at: '2026-11-04T01:59:19.065102Z'
  support: supports
  snapshot_sha256: 2c6942309cfe59ade8584e9ffc713ef9f5868b344b4ec89f16699a198eafcfc9
- evidence_id: septin-hu2006-xml
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC1383488/fullTextXML
  locator: Fresh genuine JATS Introduction s1 and Figure1 caption; Results s2a/s2b
    with Figures2/3 captions and Table1/2 explanatory text, not table cells; Methods
    s4a/s4b
  summary: RH tachyzoites cultured in HFF were partially detergent/sonication-fractionated
    to enrich conoid/apical cytoskeleton; contamination and incomplete recovery limit
    a whole-composite inventory. Preconoidal rings/conoid fibers are distinguished
    from APR anchoring subpellicular microtubules. Individual-protein sections, MudPIT
    methods, Discussion, supplements and figure pixels were not audited.
  accessed_at: '2026-11-04T01:59:21.058773Z'
  support: supports
  snapshot_sha256: dae4c4fe8cc077716338da2deccb2dea30a94147adc3fd3d81f778421cda256d
- evidence_id: septin-ren2024-xml
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11573658/fullTextXML
  locator: Fresh genuine JATS Results s2–s6 and Figures1–5 captions/Table1 explanatory
    text; complete Discussion s7; Methods s9 culture and s10 transgenic lines
  summary: RH-derived conditional Toxoplasma lines reveal three APR layers and distinguish
    the ring from the movable conoid. APR2 depletion impairs motility/invasion but
    leaves tested microneme secretion/rhoptry discharge intact; no blanket secretion-control
    mechanism follows. Methods are limited to cultures/transgenic construction; other
    assay methods, table cells, supplements and figure pixels were not inspected.
  accessed_at: '2026-11-04T01:59:20.558107Z'
  support: supports
  snapshot_sha256: 9f7353f01450d72ccf78f2cb80e610f64a58928d4e48f4d00393e012e82a7da6
- evidence_id: septin-carruthers1997-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC13475723/
  locator: Fresh genuine PMC HTML Methods S3–S6, Results S13–S17 with Figures1–6 captions,
    complete Discussion S19 including Figure8 caption
  summary: RH/2F tachyzoites invading HFF, synchronous pulse invasion, selective permeabilization,
    immunolocalization and secretion assays measure MIC2 release before ROP1, then
    delayed GRA1/NTPase secretion. This supports source-specific ordered secretion
    and forming-PV association, not direct control by every apical cytoskeletal element
    or essentiality of every marker; Discussion explicitly notes ROP1-null in-vitro
    invasion. Moving-junction and all-Apicomplexa extensions remain broader interpretation/secondary
    context. Figure pixels, full remaining methods and supplements were not inspected.
  accessed_at: '2026-11-04T01:59:19.947942Z'
  support: supports
  snapshot_sha256: 911bbf8edd2a405a8c9d2ab365b5dbce4256727f1ef666f2f5c4abc92a95be3c
- evidence_id: septin-boothroyd2008-publisher
  kind: validation
  reference: https://www.nature.com/articles/nrmicro1800
  locator: Complete failed-access response classified, 3038 bytes
  summary: HTTP200 publisher challenge rather than scientific body. Context only;
    no scientific claim derives from this response. Genuine available bodies and bounded
    native abstracts are identified separately.
  accessed_at: '2026-11-04T01:59:20.058470Z'
  support: context_only
  snapshot_sha256: 32ed63159c77e21ee19ca1b9aa3213ccf0218eb59539560b132a8e68ef0e18ea
- evidence_id: septin-boothroyd2008-canonical
  kind: validation
  reference: https://www.nature.com/articles/nrmicro1800?error=cookies_not_supported&code=readonly
  locator: Complete failed-access response classified, 3038 bytes
  summary: HTTP200 publisher challenge rather than scientific body. Context only;
    no scientific claim derives from this response. Genuine available bodies and bounded
    native abstracts are identified separately.
  accessed_at: '2026-11-04T02:00:47.240690Z'
  support: context_only
  snapshot_sha256: 32ed63159c77e21ee19ca1b9aa3213ccf0218eb59539560b132a8e68ef0e18ea
- evidence_id: septin-waller2024-xml
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11653781/fullTextXML
  locator: Complete failed-access response classified, 151 bytes
  summary: HTTP500 source retrieval failed. Context only; no scientific claim derives
    from this response. Genuine available bodies and bounded native abstracts are
    identified separately.
  accessed_at: '2026-11-04T02:00:47.952839Z'
  support: context_only
  snapshot_sha256: 329abd118a3d3b439bcd99672d9d7c5a871e5385c04198882d1cf0b9044cf8a3
- evidence_id: septin-adapter-runner-historical
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical attempted datasets runner receipt, 2026-11-03T00:49:00.848907Z–00:49:00.863225Z
  summary: Historical exit1 PermissionError reading runner pyvenv.cfg. No new runner
    execution is claimed; fresh official catalogue and native-source fallback are
    separate observations.
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: septin-original-validation
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-septin/original-checks.json
  locator: Actual native validate/render of three original pairs; all38 historical
    input occurrences
  summary: All three original YAMLs validate, render exactly to committed Markdown
    and match every historical input occurrence at the original frozen revision. All
    three current target hashes equal their original target input. Historical source/gate
    observations are not represented as current execution.
  accessed_at: '2026-11-04T02:05:50.546746Z'
  support: supports
  snapshot_sha256: 5c02259aedc778983faef0ea33e370aec2f424970c31826bf86fb399c524f3b8
- evidence_id: septin-record-ap_5_adaptor_complex
  kind: record_content
  reference: data/structures/other/ap_5_adaptor_complex.yaml
  locator: Complete current record at b82b8b5fcb02d90018a73c0d3d05ede8a2ab161f
  summary: All definitions, identifiers, typed relations, components, functions, source
    notes, examples, graph nodes/edges, discussions and history were read. Current
    target bytes are nonstale; no maintained image or experimental physical-size property
    is present.
  accessed_at: '2026-11-04T02:05:50.546746Z'
  support: supports
  snapshot_sha256: d951b48b8f9fe05db066c722dd2dad8277f04eb4af1ac36bf4a5c03932ac82dc
- evidence_id: septin-original-ap_5_adaptor_complex
  kind: record_content
  reference: reviews/structured/20261022T044318Z-ap-5-adaptor-complex-audit/review.yaml
  locator: Complete original YAML and paired Markdown; exact frozen inputs and original
    verdict/actions
  summary: Original immutable review independently reassessed against current sources;
    exact historical inputs validated. Current verdict remains needs_curation for
    its inherited minor finding.
  accessed_at: '2026-11-04T02:05:50.546746Z'
  support: supports
  snapshot_sha256: 202ed0adb6576cec2f53d0534cab118b16f81c35af955690259134befbf41b11
- evidence_id: septin-native-ap_5_adaptor_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/ap_5_adaptor_complex-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/ap_5_adaptor_complex.yaml
    --verify; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/ap_5_adaptor_complex-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: Exit0. Four reviewed human examples and four COVERED typed core-subunit
    nodes; current exact queries return their intended primary genes. Native sequence/family
    identities and experimental localization scopes are verified separately.
  accessed_at: '2026-11-04T01:59:45.098534Z'
  support: supports
  snapshot_sha256: 6bdf3915f60dd8f325cd495cfac0c11af14e1574497f1efdf57e4b31847cc4fa
- evidence_id: septin-native-ap_5_adaptor_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/ap_5_adaptor_complex-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/ap_5_adaptor_complex.yaml
    --causal-graphs; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/ap_5_adaptor_complex-uniprot-causal.log
    SHA256 0ab5a9e877601b5e064d133c6e06c2d902f314b9c485fcf3447af02d79ff9db8
  summary: Exit0. Four reviewed human examples and four COVERED typed core-subunit
    nodes; current exact queries return their intended primary genes. Native sequence/family
    identities and experimental localization scopes are verified separately.
  accessed_at: '2026-11-04T01:59:45.534281Z'
  support: supports
  snapshot_sha256: 5d25db9bb137e10ba4a9cdb48797fcac8ee5a53fe679a0c5f8cd1fe8e32b6b0f
- evidence_id: septin-record-ap_type_membrane_coat_adaptor_complex
  kind: record_content
  reference: data/structures/other/ap_type_membrane_coat_adaptor_complex.yaml
  locator: Complete current record at b82b8b5fcb02d90018a73c0d3d05ede8a2ab161f
  summary: All definitions, identifiers, typed relations, components, functions, source
    notes, examples, graph nodes/edges, discussions and history were read. Current
    target bytes are nonstale; no maintained image or experimental physical-size property
    is present.
  accessed_at: '2026-11-04T02:05:50.546746Z'
  support: supports
  snapshot_sha256: a16a52e7091df279f222b922baa48be321173ab9dc132e1c2be2384d48ca626b
- evidence_id: septin-original-ap_type_membrane_coat_adaptor_complex
  kind: record_content
  reference: reviews/structured/20261022T044319Z-ap-type-membrane-coat-adaptor-complex-audit/review.yaml
  locator: Complete original YAML and paired Markdown; exact frozen inputs and original
    verdict/actions
  summary: Original immutable review independently reassessed against current sources;
    exact historical inputs validated. Current verdict remains needs_curation for
    its inherited minor finding.
  accessed_at: '2026-11-04T02:05:50.546746Z'
  support: supports
  snapshot_sha256: f9d5ddaf668a4d93b705ec4a49a37c5e2ca8aad1c0a85aa6dba40bd9d2fb681c
- evidence_id: septin-native-ap_type_membrane_coat_adaptor_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/ap_type_membrane_coat_adaptor_complex-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/ap_type_membrane_coat_adaptor_complex.yaml
    --verify; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/ap_type_membrane_coat_adaptor_complex-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: Exit0. Zero examples and three NO_GENE_SYMBOLS typed protein-class nodes.
    Passing accession diagnostics do not establish missing optional examples or test
    an unpopulated inventory.
  accessed_at: '2026-11-04T01:59:45.981677Z'
  support: supports
  snapshot_sha256: c866c2b7293dacf77c67c9225415cfbc2a2ddf6c63ff1460b927e6650c6c60c9
- evidence_id: septin-native-ap_type_membrane_coat_adaptor_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/ap_type_membrane_coat_adaptor_complex-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/ap_type_membrane_coat_adaptor_complex.yaml
    --causal-graphs; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/ap_type_membrane_coat_adaptor_complex-uniprot-causal.log
    SHA256 cfd777d9caf821e4e33d605f5651778539cefa8b4ee9e7a290e14a7776b4b7cd
  summary: Exit0. Zero examples and three NO_GENE_SYMBOLS typed protein-class nodes.
    Passing accession diagnostics do not establish missing optional examples or test
    an unpopulated inventory.
  accessed_at: '2026-11-04T01:59:46.413581Z'
  support: supports
  snapshot_sha256: c81699b4844b7191c9616e9b44d728896534ce0fb9e7b116a5afb870f855e4de
- evidence_id: septin-record-apical_complex
  kind: record_content
  reference: data/structures/other/apical_complex.yaml
  locator: Complete current record at b82b8b5fcb02d90018a73c0d3d05ede8a2ab161f
  summary: All definitions, identifiers, typed relations, components, functions, source
    notes, examples, graph nodes/edges, discussions and history were read. Current
    target bytes are nonstale; no maintained image or experimental physical-size property
    is present.
  accessed_at: '2026-11-04T02:05:50.546746Z'
  support: supports
  snapshot_sha256: 72b670707751292b450e4c8bccddb25a4a14e482fc0eaaa85975681694f55952
- evidence_id: septin-original-apical_complex
  kind: record_content
  reference: reviews/structured/20261022T044320Z-apical-complex-audit/review.yaml
  locator: Complete original YAML and paired Markdown; exact frozen inputs and original
    verdict/actions
  summary: Original immutable review independently reassessed against current sources;
    exact historical inputs validated. Current verdict remains pass_with_limitations,
    with no scientific finding invented.
  accessed_at: '2026-11-04T02:05:50.546746Z'
  support: supports
  snapshot_sha256: 6bb778c0edffbb843e663f1308b557e9098f56e563497650cba09816ab21964f
- evidence_id: septin-native-apical_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/apical_complex-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/apical_complex.yaml
    --verify; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/apical_complex-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: Exit0. Zero protein examples and zero GENE_OR_PROTEIN typed graph nodes.
    The two broad constituent cohorts are permitted classes; native pass is empty
    protein-xref coverage and does not independently establish their biology.
  accessed_at: '2026-11-04T01:59:46.866057Z'
  support: supports
  snapshot_sha256: 042f5f81473748f1f5ab459dfbdbfbf1dce3f686e121686f2a3c6bf3809f09bd
- evidence_id: septin-native-apical_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/apical_complex-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/apical_complex.yaml
    --causal-graphs; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/apical_complex-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: Exit0. Zero protein examples and zero GENE_OR_PROTEIN typed graph nodes.
    The two broad constituent cohorts are permitted classes; native pass is empty
    protein-xref coverage and does not independently establish their biology.
  accessed_at: '2026-11-04T01:59:47.302524Z'
  support: supports
  snapshot_sha256: a0c03d2603383f700fa7070b55e56358a685ffdbabe3f3fe1b48195135e68fb2
- evidence_id: plaque-current-3
  kind: record_content
  reference: data/structures/other/bacterial_extracellular_vesicle.yaml
  locator: Entire current record at source b82b8b5fcb02d90018a73c0d3d05ede8a2ab161f
  accessed_at: '2026-11-04T02:11:03.460667Z'
  snapshot_sha256: 43f0f6e0dfef8fc8533bbbac4c5a1583adc6626873f52b92f2edbc32560137d2
  summary: Entire record independently read, including all definitions, evidence,
    components, examples, graph, taxonomic/canonical scopes, discussions and history;
    not just a protein inventory.
  support: supports
- evidence_id: plaque-original-3-yaml
  kind: prior_review
  reference: reviews/structured/20261022T044321Z-bacterial-extracellular-vesicle-audit/review.yaml
  locator: Entire immutable original paired review; historical assertions assessed
    at their own frozen revision
  accessed_at: '2026-11-04T02:11:03.460667Z'
  snapshot_sha256: a07011482846bfeed4934761a86a5bbe024017036df6e25efb36babf13f972ed
  summary: Original findings, actions, source kinds, limitations, checks and exact
    historical input references inspected. Historical passed checks are not recast
    as current validation.
  support: supports
- evidence_id: plaque-original-3-md
  kind: prior_review
  reference: reviews/structured/20261022T044321Z-bacterial-extracellular-vesicle-audit/review.md
  locator: Entire immutable original paired review; historical assertions assessed
    at their own frozen revision
  accessed_at: '2026-11-04T02:11:03.460667Z'
  snapshot_sha256: 0642d4d65e3e7b6534e98f7392d1bb067e568fb4cb709616f5e632dc33dd25b9
  summary: Original findings, actions, source kinds, limitations, checks and exact
    historical input references inspected. Historical passed checks are not recast
    as current validation.
  support: supports
- evidence_id: plaque-current-4
  kind: record_content
  reference: data/structures/other/bacterial_outer_membrane_vesicle.yaml
  locator: Entire current record at source b82b8b5fcb02d90018a73c0d3d05ede8a2ab161f
  accessed_at: '2026-11-04T02:11:03.460667Z'
  snapshot_sha256: ae635da7dc9351f59de2b4283aa2d572b200cf9eba187147c027e5e86b445a34
  summary: Entire record independently read, including all definitions, evidence,
    components, examples, graph, taxonomic/canonical scopes, discussions and history;
    not just a protein inventory.
  support: supports
- evidence_id: plaque-original-4-yaml
  kind: prior_review
  reference: reviews/structured/20261022T044321Z-bacterial-outer-membrane-vesicle-audit/review.yaml
  locator: Entire immutable original paired review; historical assertions assessed
    at their own frozen revision
  accessed_at: '2026-11-04T02:11:03.460667Z'
  snapshot_sha256: 891ea995b50bff90b1e4817858ae96afba7ea596b2fdc92f7d2e3c74aa6198c0
  summary: Original findings, actions, source kinds, limitations, checks and exact
    historical input references inspected. Historical passed checks are not recast
    as current validation.
  support: supports
- evidence_id: plaque-original-4-md
  kind: prior_review
  reference: reviews/structured/20261022T044321Z-bacterial-outer-membrane-vesicle-audit/review.md
  locator: Entire immutable original paired review; historical assertions assessed
    at their own frozen revision
  accessed_at: '2026-11-04T02:11:03.460667Z'
  snapshot_sha256: c2e5c89d185bfd2a9c4e3e145a1f8c2cbf6fc98a9fce5037a0b3ad39a6e47830
  summary: Original findings, actions, source kinds, limitations, checks and exact
    historical input references inspected. Historical passed checks are not recast
    as current validation.
  support: supports
- evidence_id: plaque-current-8
  kind: record_content
  reference: data/structures/other/caf_1_complex.yaml
  locator: Entire current record at source b82b8b5fcb02d90018a73c0d3d05ede8a2ab161f
  accessed_at: '2026-11-04T02:11:03.460667Z'
  snapshot_sha256: 9cfaf9ce52f019ddb3125428f3c6ce7cb17ae2e476fbd0fb9be2e0bcad652576
  summary: Entire record independently read, including all definitions, evidence,
    components, examples, graph, taxonomic/canonical scopes, discussions and history;
    not just a protein inventory.
  support: supports
- evidence_id: plaque-original-8-yaml
  kind: prior_review
  reference: reviews/structured/20261022T044324Z-caf-1-complex-audit/review.yaml
  locator: Entire immutable original paired review; historical assertions assessed
    at their own frozen revision
  accessed_at: '2026-11-04T02:11:03.460667Z'
  snapshot_sha256: fb4dcdc6295e05feeb8a72463af97b1b7500ddf7271053658bcff165d5af253c
  summary: Original findings, actions, source kinds, limitations, checks and exact
    historical input references inspected. Historical passed checks are not recast
    as current validation.
  support: supports
- evidence_id: plaque-original-8-md
  kind: prior_review
  reference: reviews/structured/20261022T044324Z-caf-1-complex-audit/review.md
  locator: Entire immutable original paired review; historical assertions assessed
    at their own frozen revision
  accessed_at: '2026-11-04T02:11:03.460667Z'
  snapshot_sha256: 1d644191dd2dbc83b3bd94a6852bc98aac5a2268ca1d7e0f01137e0429abdd22
  summary: Original findings, actions, source kinds, limitations, checks and exact
    historical input references inspected. Historical passed checks are not recast
    as current validation.
  support: supports
- evidence_id: plaque-current-9
  kind: record_content
  reference: data/structures/other/cbf3_complex.yaml
  locator: Entire current record at source b82b8b5fcb02d90018a73c0d3d05ede8a2ab161f
  accessed_at: '2026-11-04T02:11:03.460667Z'
  snapshot_sha256: 9cf3d32f5094ac6a00417cb7b7c125b45a4329e364d8e721314f19349baf44f2
  summary: Entire record independently read, including all definitions, evidence,
    components, examples, graph, taxonomic/canonical scopes, discussions and history;
    not just a protein inventory.
  support: supports
- evidence_id: plaque-original-9-yaml
  kind: prior_review
  reference: reviews/structured/20261022T044325Z-cbf3-complex-audit/review.yaml
  locator: Entire immutable original paired review; historical assertions assessed
    at their own frozen revision
  accessed_at: '2026-11-04T02:11:03.460667Z'
  snapshot_sha256: 324587ca73380b88cc7da048e16d12ec28469bc06f28c7ff7b2f22bd00dda44f
  summary: Original findings, actions, source kinds, limitations, checks and exact
    historical input references inspected. Historical passed checks are not recast
    as current validation.
  support: supports
- evidence_id: plaque-original-9-md
  kind: prior_review
  reference: reviews/structured/20261022T044325Z-cbf3-complex-audit/review.md
  locator: Entire immutable original paired review; historical assertions assessed
    at their own frozen revision
  accessed_at: '2026-11-04T02:11:03.460667Z'
  snapshot_sha256: c04bb3a746e87579620706b4b54dec08dd4101dcf22b934509613ba47be9bf1c
  summary: Original findings, actions, source kinds, limitations, checks and exact
    historical input references inspected. Historical passed checks are not recast
    as current validation.
  support: supports
- evidence_id: plaque-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Frozen repository policy/schema, scoped portions independently inspected
  accessed_at: '2026-11-04T02:11:03.460667Z'
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
  summary: Source scope, evidence, component/family grounding, formation-specific
    necessity and append-only history rules.
  support: supports
- evidence_id: plaque-review-skill
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Frozen repository policy/schema, scoped portions independently inspected
  accessed_at: '2026-11-04T02:11:03.460667Z'
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
  summary: Whole-record scientific review and explicit structured-source applicability
    triggers; runner fallback and bounded interpretation.
  support: supports
- evidence_id: plaque-protein-skill
  kind: authority
  reference: .claude/skills/uniprot-protein-examples/SKILL.md
  locator: Frozen repository policy/schema, scoped portions independently inspected
  accessed_at: '2026-11-04T02:11:03.460667Z'
  snapshot_sha256: 6462894c8257823bae2b175c34693cd42f11ff9269a3829c15b9286ba6d7c876
  summary: Exact native identity, gene/locus tokens, entry status, location evidence
    and graph inventory scope.
  support: supports
- evidence_id: plaque-schema
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Frozen repository policy/schema, scoped portions independently inspected
  accessed_at: '2026-11-04T02:11:03.460667Z'
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
  summary: Closed native record contract including composite component types and graph
    component references.
  support: supports
- evidence_id: plaque-review-schema
  kind: authority
  reference: schema/record_review.yaml
  locator: Frozen repository policy/schema, scoped portions independently inspected
  accessed_at: '2026-11-04T02:11:03.460667Z'
  snapshot_sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
  summary: Native evidence/assessment/finding/action enums, exact lineage and bounded
    search contract.
  support: supports
- evidence_id: plaque-review-profile
  kind: authority
  reference: docs/record-review-profile.md
  locator: Frozen repository policy/schema, scoped portions independently inspected
  accessed_at: '2026-11-04T02:11:03.460667Z'
  snapshot_sha256: 6a49c8d35f0a94082a9ad0b8bd8c6a929d85de8339141955f3779bd7ab0eb7e4
  summary: Current local review profile and immutable native publication route.
  support: supports
- evidence_id: plaque-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097691,GO:0061701,GO:1903561,GO:0009279,GO:0033186,GO:0032991,GO:0006334,GO:0031518,GO:0140513,GO:0000775,GO:0000776
  locator: GO0097691,0061701,1903561,0009279,0033186,0032991,0006334,0031518,0140513,0000775,0000776;
    definitions and relevant direct child relations; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/go.raw
  accessed_at: '2026-11-04T01:59:51.325665Z'
  snapshot_sha256: e596ea4e0041597938b727f6dfa225ff0a82a54007edf361f9b30f2d23ebd6d4
  summary: Current exact GO terms support four identities, relation scopes and source
    attribution; BEV definition still specifies plasma-membrane budding whereas OMV
    specifies outer-membrane-derived proteolipid vesicles. CAF-I heterotrimer and
    CBF3 four protein classes are explicit.
  support: supports
- evidence_id: plaque-SL0489
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0489.json
  locator: Full location entry, definition, synonyms and GO links; inspected response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/SL0489.raw
  accessed_at: '2026-11-04T01:59:51.187256Z'
  snapshot_sha256: df2cf06d3a65f961f93053c81b9fd2fd82b4ff7bf98ff407caed5cbe3f0b3939
  summary: Native bacterial membrane vesicle location and synonyms were read; its
    plasma-membrane wording does not independently reconcile every broader vesicle-origin
    class.
  support: supports
- evidence_id: plaque-tax-2
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/2.json
  locator: taxonId/scientificName/rank/parent fields; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/tax-2.raw
  accessed_at: '2026-11-04T01:59:51.628429Z'
  snapshot_sha256: 8074c9bcd59cd4da1da4bc9ec98c040bbecd52ef5c91c4c4bb9bed0f3a7cb5a9
  summary: 'Current taxonomy identity/parent inspected: Bacteria domain.'
  support: supports
- evidence_id: plaque-tax-1280
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/1280.json
  locator: taxonId/scientificName/rank/parent fields; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/tax-1280.raw
  accessed_at: '2026-11-04T01:59:51.768334Z'
  snapshot_sha256: faf940b385a99d02c1929991a8dd5cd3ba875441b30daf7d6b6504e8daef8cee
  summary: 'Current taxonomy identity/parent inspected: Staphylococcus aureus species.'
  support: supports
- evidence_id: plaque-tax-562
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/562.json
  locator: taxonId/scientificName/rank/parent fields; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/tax-562.raw
  accessed_at: '2026-11-04T01:59:56.707013Z'
  snapshot_sha256: 20aa358053d2fae1e2cd74636ed5aca1efbc372e5b8bcfdb10d3fa80be6789a1
  summary: 'Current taxonomy identity/parent inspected: Escherichia coli species.'
  support: supports
- evidence_id: plaque-tax-4932
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/4932.json
  locator: taxonId/scientificName/rank/parent fields; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/tax-4932.raw
  accessed_at: '2026-11-04T01:59:51.202661Z'
  snapshot_sha256: 963bbf3503fd0aa9e69dc25b64c5ae903f871991b37c4c593353b945c8e31688
  summary: 'Current taxonomy identity/parent inspected: Saccharomyces cerevisiae species.'
  support: supports
- evidence_id: plaque-tax-559292
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/559292.json
  locator: taxonId/scientificName/rank/parent fields; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/tax-559292.raw
  accessed_at: '2026-11-04T01:59:53.697646Z'
  snapshot_sha256: 9ebcfe8a317cc0c25c329a3a6a7cc9eaa863bb2dfebe5eaff9a34628c6684810
  summary: 'Current taxonomy identity/parent inspected: S. cerevisiae S288c strain
    below species4932.'
  support: supports
- evidence_id: plaque-toyofuku2019-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038%2Fs41579-018-0112-2&format=json&resultType=core&pageSize=1
  locator: Europe PMC exact DOI query, one matched MED record, complete abstract;
    secondary tier; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/toyofuku2019-meta.raw
  accessed_at: '2026-11-04T01:59:59.978331Z'
  snapshot_sha256: e2f495a5aeff04ca4a7a6c634260a5f7f5647c5f77eecea1a08186ab4a136c95
  summary: Complete indexed abstract and bibliographic identity inspected; this is
    a secondary review, not an independent experimental body. The abstract explicitly
    distinguishes outer-membrane blebbing and lysis-derived routes in Gram-negative
    and Gram-positive bacteria.
  support: supports
- evidence_id: plaque-kim2015-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1016%2Fj.semcdb.2015.02.006&format=json&resultType=core&pageSize=1
  locator: Europe PMC exact DOI query, one matched MED record, complete abstract;
    secondary tier; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/kim2015-meta.raw
  accessed_at: '2026-11-04T02:00:00.353890Z'
  snapshot_sha256: 899934b2fce6fcfe95d604ddefa784b9ef1d22fcf8a822e1b8ad2832d997454e
  summary: Complete indexed abstract and bibliographic identity inspected; this is
    a secondary review, not an independent experimental body. Broad bacterial-vesicle
    composition/cargo and interaction overview.
  support: supports
- evidence_id: plaque-schwechheimer2015-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038%2Fnrmicro3525&format=json&resultType=core&pageSize=1
  locator: Europe PMC exact DOI query, one matched MED record, complete abstract;
    secondary tier; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/schwechheimer2015-meta.raw
  accessed_at: '2026-11-04T02:00:00.504083Z'
  snapshot_sha256: cc3218ea9dbbefc94d87ec47ab4e37d4f39247b393057dab7ed691afd085cdf4
  summary: Complete indexed abstract and bibliographic identity inspected; this is
    a secondary review, not an independent experimental body. OMV biogenesis, cargo
    and functions overview; separate genuine body inspected below.
  support: supports
- evidence_id: plaque-lee2009-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1002%2Fpmic.200900338&format=json&resultType=core&pageSize=1
  locator: Exact DOI query; complete primary abstract and bibliographic metadata,
    not an unread full body; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/lee2009-meta.raw
  accessed_at: '2026-11-04T02:00:00.443339Z'
  snapshot_sha256: 284a85be040bfc408483c86198e1c333f6ee18998ed2d3fa761d31e1a99633ee
  summary: Primary complete abstract reports S. aureus membrane vesicles and 90 identified
    proteins; the abstract does not establish a precise experimental strain here.
  support: supports
- evidence_id: plaque-lee2007-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1002%2Fpmic.200700196&format=json&resultType=core&pageSize=1
  locator: Exact DOI query; complete primary abstract and bibliographic metadata,
    not an unread full body; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/lee2007-meta.raw
  accessed_at: '2026-11-04T02:00:00.602704Z'
  snapshot_sha256: 1c6d9dd589cb59178db3646f5e0cb657ccb78dd353e904e50d433a2d0eda844f
  summary: Primary complete abstract reports global E. coli OMV proteomics:141 proteins
    across two analyses, distinct from Park comparative gels. No full Methods or strain
    certification is claimed.
  support: supports
- evidence_id: plaque-park2010-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1371%2Fjournal.pone.0011334&format=json&resultType=core&pageSize=1
  locator: Exact DOI query; complete primary abstract and bibliographic metadata,
    not an unread full body; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/park2010-meta.raw
  accessed_at: '2026-11-04T02:00:00.520153Z'
  snapshot_sha256: 2d4ecb459ff8b962b5c25d8bfc230bddf3f0439bbfa7bd9820d85aecb4b7b33f
  summary: Primary bibliographic identity and full abstract of intestinal E. coli
    OMV mouse injection model.
  support: supports
- evidence_id: plaque-kaufman1997-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1101%2Fgad.11.3.345&format=json&resultType=core&pageSize=1
  locator: Exact DOI query; complete primary abstract and bibliographic metadata,
    not an unread full body; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/kaufman1997-meta.raw
  accessed_at: '2026-11-04T02:00:00.636876Z'
  snapshot_sha256: 5af6584ed8a27c277ed5fd120468fac4ea7c0ff9263d067ffb6985445aa3c3a8
  summary: Primary bibliographic identity and abstract of purified yeast CAF-I and
    nucleosome assembly; genuine PDF text separately inspected.
  support: supports
- evidence_id: plaque-leber2018-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.15252%2Fembj.201798134&format=json&resultType=core&pageSize=1
  locator: Exact DOI query; complete primary abstract and bibliographic metadata,
    not an unread full body; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/leber2018-meta.raw
  accessed_at: '2026-11-04T02:00:00.978523Z'
  snapshot_sha256: 8de8ac4d6870ee2f7fe031f949640709fb71087ac102cb8587403bc485982bbf
  summary: Primary bibliographic identity and abstract of the CBF3 core cryo-EM study.
  support: supports
- evidence_id: plaque-yan2018-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038%2Fs41594-018-0154-1&format=json&resultType=core&pageSize=1
  locator: Exact DOI query; complete primary abstract and bibliographic metadata,
    not an unread full body; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/yan2018-meta.raw
  accessed_at: '2026-11-04T02:00:01.093919Z'
  snapshot_sha256: 263d37a0f17e09b57dbd6efddc088862fe9c868e586f5a843c2f22a30b121d6c
  summary: Primary bibliographic identity and abstract of full CBF3–CEN3 structure;
    deposition claims remain model-scoped.
  support: supports
- evidence_id: plaque-pmid-11238915
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11238915+AND+SRC%3AMED&format=json&resultType=core&pageSize=1
  locator: Exact PMID query, complete primary abstract; one MED match; inspected response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/pmid-11238915.raw
  accessed_at: '2026-11-04T02:00:01.157439Z'
  snapshot_sha256: ec92f0f63c6e67566ec1d8059c59e18c7756fdba797ae30bd692422ea7de11da
  summary: Johnston2001 abstract explicitly separates Msi1 cytoplasmic/RAS functions
    from CAF-I; native P13712 location joins inspected separately.
  support: supports
- evidence_id: plaque-pmid-14562095
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&format=json&resultType=core&pageSize=1
  locator: Exact PMID query, complete primary abstract; one MED match; inspected response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/pmid-14562095.raw
  accessed_at: '2026-11-04T02:00:01.142419Z'
  snapshot_sha256: 29fa7e6d8ea5e645642a360565a0b71b2fb9041aab05012b6826702cf86793b1
  summary: Huh2003 full indexed abstract is a global localization screen; specific
    Skp1 location joined from native UniProt annotation, not inferred from the generic
    abstract.
  support: supports
- evidence_id: plaque-pmid-10427094
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10427094+AND+SRC%3AMED&format=json&resultType=core&pageSize=1
  locator: Exact PMID query, complete primary abstract; one MED match; inspected response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/pmid-10427094.raw
  accessed_at: '2026-11-04T02:00:01.245167Z'
  snapshot_sha256: 253984ace92f8e34917db61578e7bb4b82ab46ddea294b1c55aead3ca9939be3
  summary: Zeng1999 full abstract mainly concerns Slk19/Kar3; native Ndc10 location
    join and specific Cbf2-GFP body methods checked separately.
  support: supports
- evidence_id: plaque-pmid-9030687
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9030687+AND+SRC%3AMED&format=json&resultType=core&pageSize=1
  locator: Exact PMID query, complete primary abstract; one MED match; inspected response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/pmid-9030687.raw
  accessed_at: '2026-11-04T02:00:01.298875Z'
  snapshot_sha256: 4c31093a842f1e1e086b442a9ac2c18a59572e576043f15e8af42de9bdf58d27
  summary: Kaufman1997 exact PMID bibliographic/abstract corroboration.
  support: supports
- evidence_id: plaque-up-Q12495
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q12495.json
  locator: Complete native JSON; entryType/accession/name/genes/organism; relevant
    comments and crossreferences; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/up-Q12495.raw
  accessed_at: '2026-11-04T01:59:52.794347Z'
  snapshot_sha256: 7b72162a43e431763fcd598bcdeb70c2d2d84430771663f23a51bd9eeab70a5a
  summary: Full current reviewed entry identity, primary accession, recommended protein
    label, gene/alias/locus tokens, taxon559292, relevant FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION and InterPro crossreferences inspected. Primary token RLF2; localization/identity
    is not independent formation-necessity evidence.
  support: supports
- evidence_id: plaque-up-Q04199
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q04199.json
  locator: Complete native JSON; entryType/accession/name/genes/organism; relevant
    comments and crossreferences; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/up-Q04199.raw
  accessed_at: '2026-11-04T01:59:57.704036Z'
  snapshot_sha256: 29522b95b89beeff8e879bb26fc757f18eb99d9acd668b56c835420f34b355d5
  summary: Full current reviewed entry identity, primary accession, recommended protein
    label, gene/alias/locus tokens, taxon559292, relevant FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION and InterPro crossreferences inspected. Primary token CAC2; localization/identity
    is not independent formation-necessity evidence.
  support: supports
- evidence_id: plaque-up-P13712
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P13712.json
  locator: Complete native JSON; entryType/accession/name/genes/organism; relevant
    comments and crossreferences; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/up-P13712.raw
  accessed_at: '2026-11-04T01:59:52.699822Z'
  snapshot_sha256: 419b1e7a2f44ac14644c30d48929834f7b41e8a7d2da4b526c2a1d2eca06b740
  summary: Full current reviewed entry identity, primary accession, recommended protein
    label, gene/alias/locus tokens, taxon559292, relevant FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION and InterPro crossreferences inspected. Primary token MSI1; localization/identity
    is not independent formation-necessity evidence.
  support: supports
- evidence_id: plaque-up-P35203
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P35203.json
  locator: Complete native JSON; entryType/accession/name/genes/organism; relevant
    comments and crossreferences; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/up-P35203.raw
  accessed_at: '2026-11-04T01:59:59.152374Z'
  snapshot_sha256: b7ac0e2d1e660c8e882898f8d58c3decbcc9e23ce70b6fb2126ef523012fbc28
  summary: Full current reviewed entry identity, primary accession, recommended protein
    label, gene/alias/locus tokens, taxon559292, relevant FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION and InterPro crossreferences inspected. Primary token CTF13; localization/identity
    is not independent formation-necessity evidence.
  support: supports
- evidence_id: plaque-up-P52286
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P52286.json
  locator: Complete native JSON; entryType/accession/name/genes/organism; relevant
    comments and crossreferences; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/up-P52286.raw
  accessed_at: '2026-11-04T01:59:54.983384Z'
  snapshot_sha256: 384b52723af6931a974983b14bd8a4064b1b36dcb976ac07a81b8fbf8c309823
  summary: Full current reviewed entry identity, primary accession, recommended protein
    label, gene/alias/locus tokens, taxon559292, relevant FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION and InterPro crossreferences inspected. Primary token SKP1; localization/identity
    is not independent formation-necessity evidence.
  support: supports
- evidence_id: plaque-up-P40969
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P40969.json
  locator: Complete native JSON; entryType/accession/name/genes/organism; relevant
    comments and crossreferences; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/up-P40969.raw
  accessed_at: '2026-11-04T01:59:56.484594Z'
  snapshot_sha256: 75fb8c2b58c1436e83bfc12c58a4f95dead30bbea2b351fbfa2f4f7eb15bb1b6
  summary: Full current reviewed entry identity, primary accession, recommended protein
    label, gene/alias/locus tokens, taxon559292, relevant FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION and InterPro crossreferences inspected. Primary token CEP3; localization/identity
    is not independent formation-necessity evidence.
  support: supports
- evidence_id: plaque-up-P32504
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P32504.json
  locator: Complete native JSON; entryType/accession/name/genes/organism; relevant
    comments and crossreferences; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/up-P32504.raw
  accessed_at: '2026-11-04T01:59:59.885034Z'
  snapshot_sha256: b783ceedfc9758cde2f501520f0d344c49da696f9d1ef8b5d1ad609d041a291c
  summary: Full current reviewed entry identity, primary accession, recommended protein
    label, gene/alias/locus tokens, taxon559292, relevant FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION and InterPro crossreferences inspected. Primary token CBF2; localization/identity
    is not independent formation-necessity evidence.
  support: supports
- evidence_id: plaque-gene-CAC1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACAC1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=25
  locator: UniProt complete returned query result; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/gene-CAC1.raw
  accessed_at: '2026-11-04T01:59:54.092159Z'
  snapshot_sha256: 8edfe9fac64c7666767588c29b1ebf962c37b331fd216514c959ebb00fcd53f0
  summary: Exactly one returned reviewed S288c entry; its actual primary/alias/locus
    tokens checked independently against the full entry, rather than trusting index
    retrieval.
  support: supports
  search_scope: UniProt REST; actual URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACAC1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=25;
    gene_exact:CAC1, taxonomy_id:559292, reviewed:true; size25; first response only,
    one returned result; current retrieval date; no broader family absence claim.
- evidence_id: plaque-gene-CAC2
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACAC2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=25
  locator: UniProt complete returned query result; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/gene-CAC2.raw
  accessed_at: '2026-11-04T01:59:59.203933Z'
  snapshot_sha256: 25fcab8787502201dd94b57c366d728fd40a188716e30406d959a7d04f42b855
  summary: Exactly one returned reviewed S288c entry; its actual primary/alias/locus
    tokens checked independently against the full entry, rather than trusting index
    retrieval.
  support: supports
  search_scope: UniProt REST; actual URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACAC2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=25;
    gene_exact:CAC2, taxonomy_id:559292, reviewed:true; size25; first response only,
    one returned result; current retrieval date; no broader family absence claim.
- evidence_id: plaque-gene-MSI1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AMSI1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=25
  locator: UniProt complete returned query result; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/gene-MSI1.raw
  accessed_at: '2026-11-04T02:00:00.915842Z'
  snapshot_sha256: f6d3efa8e32ec46c9275bf251bc797eae7874b808484d523ca927fd598a9e966
  summary: Exactly one returned reviewed S288c entry; its actual primary/alias/locus
    tokens checked independently against the full entry, rather than trusting index
    retrieval.
  support: supports
  search_scope: UniProt REST; actual URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AMSI1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=25;
    gene_exact:MSI1, taxonomy_id:559292, reviewed:true; size25; first response only,
    one returned result; current retrieval date; no broader family absence claim.
- evidence_id: plaque-gene-CTF13
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACTF13%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=25
  locator: UniProt complete returned query result; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/gene-CTF13.raw
  accessed_at: '2026-11-04T01:59:58.095769Z'
  snapshot_sha256: 73fd0f00d38565ca289217eccf9b8265bb87c4ae463943d136d2c334f3f60730
  summary: Exactly one returned reviewed S288c entry; its actual primary/alias/locus
    tokens checked independently against the full entry, rather than trusting index
    retrieval.
  support: supports
  search_scope: UniProt REST; actual URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACTF13%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=25;
    gene_exact:CTF13, taxonomy_id:559292, reviewed:true; size25; first response only,
    one returned result; current retrieval date; no broader family absence claim.
- evidence_id: plaque-gene-SKP1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASKP1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=25
  locator: UniProt complete returned query result; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/gene-SKP1.raw
  accessed_at: '2026-11-04T01:59:58.045965Z'
  snapshot_sha256: d48806e41db085a4fc8c5d5c585b01bd3fcb3a7cbae52656786ef60352eae3ee
  summary: Exactly one returned reviewed S288c entry; its actual primary/alias/locus
    tokens checked independently against the full entry, rather than trusting index
    retrieval.
  support: supports
  search_scope: UniProt REST; actual URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASKP1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=25;
    gene_exact:SKP1, taxonomy_id:559292, reviewed:true; size25; first response only,
    one returned result; current retrieval date; no broader family absence claim.
- evidence_id: plaque-gene-CEP3
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACEP3%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=25
  locator: UniProt complete returned query result; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/gene-CEP3.raw
  accessed_at: '2026-11-04T02:00:02.092220Z'
  snapshot_sha256: 57f9c786d5411057e1ffdd23c9299304e76f268a3cd21520ae9891d77e59781f
  summary: Exactly one returned reviewed S288c entry; its actual primary/alias/locus
    tokens checked independently against the full entry, rather than trusting index
    retrieval.
  support: supports
  search_scope: UniProt REST; actual URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACEP3%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=25;
    gene_exact:CEP3, taxonomy_id:559292, reviewed:true; size25; first response only,
    one returned result; current retrieval date; no broader family absence claim.
- evidence_id: plaque-gene-NDC10
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ANDC10%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=25
  locator: UniProt complete returned query result; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/gene-NDC10.raw
  accessed_at: '2026-11-04T01:59:59.966875Z'
  snapshot_sha256: 32261bf36b3ce28be0eee85677906862da986cfa5af86dbf260ba75d60c31377
  summary: Exactly one returned reviewed S288c entry; its actual primary/alias/locus
    tokens checked independently against the full entry, rather than trusting index
    retrieval.
  support: supports
  search_scope: UniProt REST; actual URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ANDC10%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=25;
    gene_exact:NDC10, taxonomy_id:559292, reviewed:true; size25; first response only,
    one returned result; current retrieval date; no broader family absence claim.
- evidence_id: plaque-ipr-IPR045145
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR045145/
  locator: Exact InterPro entry metadata, hierarchy and type; bounds distinguish family/domain/general
    paralog class; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/ipr-IPR045145.raw
  accessed_at: '2026-11-04T01:59:58.656516Z'
  snapshot_sha256: 1e684451ec82c768404e39f55909bf93942b5e0f5076e5128e668c1146b2da7a
  summary: 'Native accession, name and type inspected: {''name'': ''Chromatin assembly
    factor 1 subunit Cac2/CHAF1B/FAS2'', ''short'': ''PTHR15271''} (family). IPR045145
    is full Cac2/CHAF1B/FAS2 family, IPR016897 full Skp1; broader IPR001232 and domain-only
    candidates are not substituted. Generated descriptive prose is not treated as
    primary mechanism evidence.'
  support: supports
- evidence_id: plaque-ipr-IPR016897
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016897/
  locator: Exact InterPro entry metadata, hierarchy and type; bounds distinguish family/domain/general
    paralog class; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/ipr-IPR016897.raw
  accessed_at: '2026-11-04T01:59:58.699104Z'
  snapshot_sha256: e47550d5dfd19baea033f543ef6823c3e10ca974faaae5d49d823b994c794df7
  summary: 'Native accession, name and type inspected: {''name'': ''S-phase kinase-associated
    protein 1'', ''short'': ''SKP1''} (family). IPR045145 is full Cac2/CHAF1B/FAS2
    family, IPR016897 full Skp1; broader IPR001232 and domain-only candidates are
    not substituted. Generated descriptive prose is not treated as primary mechanism
    evidence.'
  support: supports
- evidence_id: plaque-ipr-IPR001232
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001232/
  locator: Exact InterPro entry metadata, hierarchy and type; bounds distinguish family/domain/general
    paralog class; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/ipr-IPR001232.raw
  accessed_at: '2026-11-04T01:59:59.286452Z'
  snapshot_sha256: b53bf5571f84de756d3b93f4d5a19006dbf485dee5970c88249fdd202ec46c71
  summary: 'Native accession, name and type inspected: {''name'': ''S-phase kinase-associated
    protein 1-like'', ''short'': ''SKP1-like''} (family). IPR045145 is full Cac2/CHAF1B/FAS2
    family, IPR016897 full Skp1; broader IPR001232 and domain-only candidates are
    not substituted. Generated descriptive prose is not treated as primary mechanism
    evidence.'
  support: supports
- evidence_id: plaque-ipr-IPR031760
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR031760/
  locator: Exact InterPro entry metadata, hierarchy and type; bounds distinguish family/domain/general
    paralog class; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/ipr-IPR031760.raw
  accessed_at: '2026-11-04T01:59:59.340256Z'
  snapshot_sha256: f294c0cc3c83c69350fb0de39053a5afd42062cb6d865c21666bcef3134bb605
  summary: 'Native accession, name and type inspected: {''name'': ''Centromere DNA-binding
    protein complex CBF3 subunit B, C-terminal'', ''short'': ''Cep3_C''} (domain).
    IPR045145 is full Cac2/CHAF1B/FAS2 family, IPR016897 full Skp1; broader IPR001232
    and domain-only candidates are not substituted. Generated descriptive prose is
    not treated as primary mechanism evidence.'
  support: supports
- evidence_id: plaque-ipr-IPR022210
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR022210/
  locator: Exact InterPro entry metadata, hierarchy and type; bounds distinguish family/domain/general
    paralog class; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/ipr-IPR022210.raw
  accessed_at: '2026-11-04T01:59:59.751366Z'
  snapshot_sha256: fc37d61bd0c9c45b679494e572f472b578e22688948c3db9dd84ae2d9c9880a5
  summary: 'Native accession, name and type inspected: {''name'': ''Transcription
    activator GCR1-like domain'', ''short'': ''TF_GCR1-like''} (domain). IPR045145
    is full Cac2/CHAF1B/FAS2 family, IPR016897 full Skp1; broader IPR001232 and domain-only
    candidates are not substituted. Generated descriptive prose is not treated as
    primary mechanism evidence.'
  support: supports
- evidence_id: plaque-ipr-IPR062588
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR062588/
  locator: Exact InterPro entry metadata, hierarchy and type; bounds distinguish family/domain/general
    paralog class; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/ipr-IPR062588.raw
  accessed_at: '2026-11-04T01:59:59.818916Z'
  snapshot_sha256: 73f81b9f3346b9f4c7f8ae84099ca7e6c04f335c0fbba56a1de23dc19451eb24
  summary: 'Native accession, name and type inspected: {''name'': ''CTF13, N-terminal
    domain'', ''short'': ''CTF13_N''} (domain). IPR045145 is full Cac2/CHAF1B/FAS2
    family, IPR016897 full Skp1; broader IPR001232 and domain-only candidates are
    not substituted. Generated descriptive prose is not treated as primary mechanism
    evidence.'
  support: supports
- evidence_id: plaque-ipr-IPR063542
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR063542/
  locator: Exact InterPro entry metadata, hierarchy and type; bounds distinguish family/domain/general
    paralog class; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/ipr-IPR063542.raw
  accessed_at: '2026-11-04T01:59:59.905106Z'
  snapshot_sha256: f5d44ee4f75fc4b36cb680088f7705d6b94c4920884f925d2af1f3f3f247aa6d
  summary: 'Native accession, name and type inspected: {''name'': ''CTF13, C-terminal
    domain'', ''short'': ''CTF13_C''} (domain). IPR045145 is full Cac2/CHAF1B/FAS2
    family, IPR016897 full Skp1; broader IPR001232 and domain-only candidates are
    not substituted. Generated descriptive prose is not treated as primary mechanism
    evidence.'
  support: supports
- evidence_id: plaque-ipr-IPR050459
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050459/
  locator: Exact InterPro entry metadata, hierarchy and type; bounds distinguish family/domain/general
    paralog class; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/ipr-IPR050459.raw
  accessed_at: '2026-11-04T02:00:45.338384Z'
  snapshot_sha256: 667cffa52a61bb3569567d6151e8a6ff83dcb417f6acb273ce579cdbbfcbd05d
  summary: 'Native accession, name and type inspected: {''name'': ''WD repeat RBAP46/RBAP48/MSI1'',
    ''short'': ''WD_repeat_RBAP46/RBAP48/MSI1''} (family). IPR045145 is full Cac2/CHAF1B/FAS2
    family, IPR016897 full Skp1; broader IPR001232 and domain-only candidates are
    not substituted. Generated descriptive prose is not treated as primary mechanism
    evidence.'
  support: supports
- evidence_id: plaque-ipr-IPR048800
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR048800/
  locator: Exact InterPro entry metadata, hierarchy and type; bounds distinguish family/domain/general
    paralog class; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/ipr-IPR048800.raw
  accessed_at: '2026-11-04T02:00:45.463757Z'
  snapshot_sha256: 012ca68a98bc0fbb8b11958b2ab16a8239d555114bbcc354eea87866eee17846
  summary: 'Native accession, name and type inspected: {''name'': ''Chromatin assembly
    factor 1 subunit Cac1-like, C-terminal domain'', ''short'': ''Cac1-like_C''} (domain).
    IPR045145 is full Cac2/CHAF1B/FAS2 family, IPR016897 full Skp1; broader IPR001232
    and domain-only candidates are not substituted. Generated descriptive prose is
    not treated as primary mechanism evidence.'
  support: supports
- evidence_id: plaque-ipr-IPR021644
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR021644/
  locator: Exact InterPro entry metadata, hierarchy and type; bounds distinguish family/domain/general
    paralog class; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/ipr-IPR021644.raw
  accessed_at: '2026-11-04T02:00:45.503592Z'
  snapshot_sha256: d0eea548b9fd409da815a428c38431eda7456c5c5b2f25e798b3988f2a705ad1
  summary: 'Native accession, name and type inspected: {''name'': ''Chromatin assembly
    factor 1 p150 subunit, acidic region'', ''short'': ''CAF-1_p150_acidic''} (domain).
    IPR045145 is full Cac2/CHAF1B/FAS2 family, IPR016897 full Skp1; broader IPR001232
    and domain-only candidates are not substituted. Generated descriptive prose is
    not treated as primary mechanism evidence.'
  support: supports
- evidence_id: plaque-ipr-IPR022043
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR022043/
  locator: Exact InterPro entry metadata, hierarchy and type; bounds distinguish family/domain/general
    paralog class; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/ipr-IPR022043.raw
  accessed_at: '2026-11-04T02:00:45.540933Z'
  snapshot_sha256: 4ce4dceaf93c3d7af738076717af4a182435a1e2a2ff54198f4c5c1edef343a7
  summary: 'Native accession, name and type inspected: {''name'': ''Chromatin assembly
    factor 1 subunit A, dimerization domain'', ''short'': ''CAF1A_DD''} (domain).
    IPR045145 is full Cac2/CHAF1B/FAS2 family, IPR016897 full Skp1; broader IPR001232
    and domain-only candidates are not substituted. Generated descriptive prose is
    not treated as primary mechanism evidence.'
  support: supports
- evidence_id: plaque-PMC5771398-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5771398.1/PMC5771398.1.xml
  locator: 'JATS secs0003,0005,0006,0007,0012: expression/core, Ctf13 fold, Skp1 interaction,
    intersubunit interfaces and purification; embedded text captions only, no pixel
    inspection; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/PMC5771398-jats.raw'
  accessed_at: '2026-11-04T02:00:01.415531Z'
  snapshot_sha256: cd9f092ab07b42f0d1ca5fc9cd1ebe0d95a58c7cda17927472cd428178133c90
  summary: Leber primary body independently distinguishes coexpressed full Ndc10(2):Cep3(2):Ctf13(1):Skp1(1)
    preparation from the Ndc10-dissociated core used for cryo-EM. Ctf13/Skp1 heterodimer
    contacts Cep3 dimer. Source supports new membership edges without asserting core
    maps resolved Ndc10.
  support: supports
- evidence_id: plaque-PMC6292502-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC6292502.1/PMC6292502.1.xml
  locator: JATS S2 overall architecture, S3 CEN3 dimer interaction, S7 cloning/expression/purification;
    no figure pixels or raw coordinate analysis; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/PMC6292502-jats.raw
  accessed_at: '2026-11-04T02:00:01.453553Z'
  snapshot_sha256: 8f99737d72e41c9f45accbb4fc843476b68f4305d69fbde08af9b7b583d2a4b8
  summary: Yan full CBF3–CEN3 body and Methods support four-class complex, central
    Ndc10 dimer, Ctf13 interface and centromeric DNA recognition; Cse4 deposition
    is a proposed model. Yeast genes expressed in Hi5 cells; this is not an endogenous
    S288c localization or depletion assay.
  support: supports
- evidence_id: plaque-PMC2893157-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2893157.1/PMC2893157.1.xml
  locator: JATS s2 including embedded Fig1–6 text captions, s3a/b/c/e Methods; no
    image pixels, no K-12 strain equivalence; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/PMC2893157-jats.raw
  accessed_at: '2026-11-04T02:00:44.945581Z'
  snapshot_sha256: 73f4603e225d45d11528a69a8f19c0098626b63703a2b1de96627b83d648f180
  summary: Park primary Results/Discussion and Methods show an intestinal mouse CLP
    E. coli isolate identified by16S, OMV preparations, injection-induced inflammation
    and comparative Coomassie protein/LPS profiles. No global141-protein identification
    experiment here; that belongs to Lee2007.
  support: supports
- evidence_id: plaque-PMC5308417-jats
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5308417.1/PMC5308417.1.xml
  locator: Secondary review JATS S4 complete protein-cargo subsection and children,S9
    bacterial communities,S14 virulence delivery; not primary evidence; no figures
    inspected; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/PMC5308417-jats.raw
  accessed_at: '2026-11-04T02:00:45.087153Z'
  snapshot_sha256: 9030a328458b9c6724a4279038544af5a2752341b2a260677a853054991e8ead
  summary: Genuine secondary review body distinguishes variable OMV proteome, cargo
    selection/purification limits, external versus luminal association and species-specific
    delivery/community examples. It contextualizes the broad nonmechanistic transport
    graph, not an independent assay for all bacteria.
  support: supports
- evidence_id: plaque-PMC3206577-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3206577.1/PMC3206577.1.xml
  locator: CBF2–GFP Fusion Plasmids Methods and Results section Slk19p Is Located...;
    no pixel inspection; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/PMC3206577-jats.raw
  accessed_at: '2026-11-04T02:00:01.564315Z'
  snapshot_sha256: 5bcbfd5e7709fda64de08691ec05093d1ab8d50e5c19d97fbbc533f47c5592ec
  summary: Primary CBF2–GFP construct methods describe functional complementation;
    bounded localization Results concern Slk19/Kar3 and are not misattributed wholesale
    to Ndc10. Exact Ndc10 nucleus attribution is retained from native P32504 annotation.
  support: supports
- evidence_id: plaque-kaufman1997-pdf-download
  kind: primary_source
  reference: https://genesdev.cshlp.org/content/11/3/345.full.pdf?download=1
  locator: Official PDF bytes start %PDF; pdftotext text pages345–347 and354, text
    Fig1 caption; no figure pixels or exhaustive whole-PDF claim; inspected response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/kaufman1997-pdf-download.raw
  accessed_at: '2026-11-04T02:05:10.396468Z'
  snapshot_sha256: 80b005ca003a1cf32674e13202e84280beef17096bc10fc760b66841ba9d2080
  summary: 'Genuine official PDF independently read: pages345–347 abstract/introduction
    and purification Results establish yeast p90/p60/p50 cosedimentation/peptide identification
    and replication-preferential nucleosome assembly; page354 Methods uses BJ926 purification,
    W303 genetic backgrounds, human histones and SV40 assay. Current S288c identity
    examples are not asserted to be those experimental strains.'
  support: supports
- evidence_id: plaque-kaufman1997-pdf
  kind: validation
  reference: https://genesdev.cshlp.org/content/11/3/345.full.pdf
  locator: Exact attempted route and returned response; access context only; inspected
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/kaufman1997-pdf.raw
  accessed_at: '2026-11-04T02:00:44.586134Z'
  snapshot_sha256: 6808bccc13cb8e5e7c9ef03c2b2bd9efb8adcbcc2ce32bfed105b0ca338dd9ee
  summary: Initial official PDF route returned403 HTML challenge; later query-qualified
    official PDF succeeded, so no final unreadability claim.
  support: context_only
- evidence_id: plaque-kaufman1997-html
  kind: validation
  reference: https://genesdev.cshlp.org/content/11/3/345.full
  locator: Exact attempted route and returned response; access context only; inspected
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/kaufman1997-html.raw
  accessed_at: '2026-11-04T02:04:39.708717Z'
  snapshot_sha256: ccb88db897f098bbbd6c8e6a5b92d94835a4240aec0b5108112bc113076eac6b
  summary: Publisher landing/citation shell lacks full article body; not body evidence.
  support: context_only
- evidence_id: plaque-kaufman1997-pdf-html
  kind: validation
  reference: https://genesdev.cshlp.org/content/11/3/345.full.pdf+html
  locator: Exact attempted route and returned response; access context only; inspected
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/kaufman1997-pdf-html.raw
  accessed_at: '2026-11-04T02:05:08.910405Z'
  snapshot_sha256: 6e3d2f49091d2e839434767e21c778bb9e1667c30ccdc829a845fee976ad4b3b
  summary: Wrapper route is not the independently inspected PDF.
  support: context_only
- evidence_id: plaque-PMC86735-jats
  kind: validation
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC86735.1/PMC86735.1.xml
  locator: Exact attempted route and returned response; access context only; inspected
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/PMC86735-jats.raw
  accessed_at: '2026-11-04T02:00:44.869372Z'
  snapshot_sha256: 16fb1ad95944f43a5fdbb4303b11b788d15fb3c241a9ff10074642a1f8100be6
  summary: Guessed official S3 revision returned404; PMID11238915 abstract and native
    annotation remain the declared tiers.
  support: context_only
- evidence_id: plaque-toyofuku2019-publisher
  kind: validation
  reference: https://api.crossref.org/v1/works/10.1038%2Fs41579-018-0112-2/transform
  locator: Exact attempted route and returned response; access context only; inspected
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/toyofuku2019-publisher.raw
  accessed_at: '2026-11-04T02:00:44.903739Z'
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
  summary: DOI route429; current scientific assessment uses complete indexed secondary
    abstract only.
  support: context_only
- evidence_id: plaque-adapter-sa-staph_precise108-genes
  kind: validation
  reference: https://imodulondb.org/api/datasets/s_aureus/staph_precise108/genes
  locator: Exact attempted route and returned response; access context only; inspected
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/adapter-sa-staph_precise108-genes.raw
  accessed_at: '2026-11-04T02:04:39.027152Z'
  snapshot_sha256: 372db3e7392f2779f2d46aef5c4f7786399705355520de485f6c37ee92bf0478
  summary: Path-style genes route returned915-byte frontend HTML, not a gene table;
    corrected query endpoint used separately.
  support: context_only
- evidence_id: plaque-adapter-sa-staph_precise165-genes
  kind: validation
  reference: https://imodulondb.org/api/datasets/s_aureus/staph_precise165/genes
  locator: Exact attempted route and returned response; access context only; inspected
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/adapter-sa-staph_precise165-genes.raw
  accessed_at: '2026-11-04T02:04:39.027194Z'
  snapshot_sha256: 372db3e7392f2779f2d46aef5c4f7786399705355520de485f6c37ee92bf0478
  summary: Path-style genes route returned915-byte frontend HTML, not a gene table;
    corrected query endpoint used separately.
  support: context_only
- evidence_id: plaque-kim2015-publisher
  kind: database
  reference: https://api.crossref.org/v1/works/10.1016%2Fj.semcdb.2015.02.006/transform
  locator: Exact Crossref transform response and bibliographic identity; inspected
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/kim2015-publisher.raw
  accessed_at: '2026-11-04T02:00:45.488355Z'
  snapshot_sha256: 7c3790e7a789b201b1b11479c63432d1c47fbe9714bc3df7a4a00b438c088bc6
  summary: DOI content negotiation yielded Crossref JSON metadata/abstract rather
    than publisher full text. No full-body claim is based on this response.
  support: context_only
- evidence_id: plaque-lee2009-publisher
  kind: database
  reference: https://api.crossref.org/v1/works/10.1002%2Fpmic.200900338/transform
  locator: Exact Crossref transform response and bibliographic identity; inspected
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/lee2009-publisher.raw
  accessed_at: '2026-11-04T02:00:45.199441Z'
  snapshot_sha256: 7b83c1450c47f3e211593bae37ebcf11b2837d4613a4d2e728e052005f6fd4b4
  summary: DOI content negotiation yielded Crossref JSON metadata/abstract rather
    than publisher full text. No full-body claim is based on this response.
  support: context_only
- evidence_id: plaque-lee2007-publisher
  kind: database
  reference: https://api.crossref.org/v1/works/10.1002%2Fpmic.200700196/transform
  locator: Exact Crossref transform response and bibliographic identity; inspected
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/lee2007-publisher.raw
  accessed_at: '2026-11-04T02:00:45.463810Z'
  snapshot_sha256: 6d1f4dce9756dc1fd13c768b6a16b35fa1fd2e4c2faada02bc09affee8871a5d
  summary: DOI content negotiation yielded Crossref JSON metadata/abstract rather
    than publisher full text. No full-body claim is based on this response.
  support: context_only
- evidence_id: plaque-catalogue
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Complete20-organism/28 organism-dataset-pair response; independently reread
    peer-fetched snapshot at its actual timestamp; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/catalogue.raw
  accessed_at: '2026-11-04T02:01:13.129554Z'
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  summary: Complete current official catalogue has E. coli and S. aureus datasets,
    but no Saccharomyces row. Whole-record molecular/pathway triggers were assessed
    before the taxon-limited conclusion; lack of yeast coverage is not biological
    absence.
  support: supports
- evidence_id: plaque-ecoli-meta
  kind: database
  reference: https://imodulondb.org/api/datasets/e_coli/precise1k/meta
  locator: Complete official metadata; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/ecoli-meta.raw
  accessed_at: '2026-11-04T02:01:13.641479Z'
  snapshot_sha256: 6cd60b3e363a11c95c2b5b1d160fe360687c0a680a5b95c18c6c76e7c5d99865
  summary: precise1k metadata lists BW25113,DGF-298,GMOS,MG1655,W3110; no equivalence
    to the Park CLP intestinal isolate is asserted.
  support: supports
- evidence_id: plaque-ecoli-genes
  kind: database
  reference: https://imodulondb.org/api/genes?organism=e_coli&dataset=precise1k&limit=10000
  locator: Complete requested table limit10000; exact gene_name/gene_product fields
    and selected loci; generated prose excluded; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/ecoli-genes.raw
  accessed_at: '2026-11-04T02:01:13.335311Z'
  snapshot_sha256: db4db81a724c8bee753c68fa5fefdd34f3d89e2cd101ae52311088f7cb094d27
  summary: Full4257-row returned gene table inspected through bounded literal-query
    fields and selected ompA/b0957 and ompF/b0929 annotations; STRING511145 locus
    context retained. No vesicle localization is inferred.
  support: supports
- evidence_id: plaque-ecoli-modules
  kind: database
  reference: https://imodulondb.org/api/datasets/e_coli/precise1k/imodulons
  locator: Complete module list metadata; no generated AI summaries; inspected response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/ecoli-modules.raw
  accessed_at: '2026-11-04T02:01:12.943022Z'
  snapshot_sha256: c9f7564cc9fa212686b00f75d35b5438d9d8660066eada141b263e580634e26d
  summary: Complete201-module metadata queried only for bounded vesicle/outer membrane/cargo
    strings; module names/functions are expression context.
  support: supports
- evidence_id: plaque-adapter-sa-staph_precise108-meta
  kind: database
  reference: https://imodulondb.org/api/datasets/s_aureus/staph_precise108/meta
  locator: Full official response; metadata strain list or bounded gene/module fields;
    generated prose excluded; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/adapter-sa-staph_precise108-meta.raw
  accessed_at: '2026-11-04T02:04:39.144406Z'
  snapshot_sha256: 87ea7ae75ba7008e312e380160b25f4533163ee8962641b4e2d5a3c2389842b5
  summary: Current S. aureus staph_precise108 meta response independently inspected
    for exact strains and bounded vesicle/cargo context. USA300-related dataset strains
    are not substituted for the unverified strain of Lee2009; no absent biology is
    inferred.
  support: supports
- evidence_id: plaque-adapter-sa-staph_precise108-imodulons
  kind: database
  reference: https://imodulondb.org/api/datasets/s_aureus/staph_precise108/imodulons
  locator: Full official response; metadata strain list or bounded gene/module fields;
    generated prose excluded; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/adapter-sa-staph_precise108-imodulons.raw
  accessed_at: '2026-11-04T02:04:39.021528Z'
  snapshot_sha256: aaf4f463aa8f81d758b2899edd1acf32d567964f4f4341b534205a58d61b3ed4
  summary: Current S. aureus staph_precise108 imodulons response independently inspected
    for exact strains and bounded vesicle/cargo context. USA300-related dataset strains
    are not substituted for the unverified strain of Lee2009; no absent biology is
    inferred.
  support: supports
- evidence_id: plaque-adapter-sa-staph_precise108-genes-query
  kind: database
  reference: https://imodulondb.org/api/genes?organism=s_aureus&dataset=staph_precise108&limit=10000
  locator: Full official response; metadata strain list or bounded gene/module fields;
    generated prose excluded; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/adapter-sa-staph_precise108-genes-query.raw
  accessed_at: '2026-11-04T02:05:08.409011Z'
  snapshot_sha256: 29961e446530559303913da5fe7bbe94cee0df8575476d72ca67b6eb8572ccbd
  summary: Current S. aureus staph_precise108 genes-query response independently inspected
    for exact strains and bounded vesicle/cargo context. USA300-related dataset strains
    are not substituted for the unverified strain of Lee2009; no absent biology is
    inferred.
  support: supports
- evidence_id: plaque-adapter-sa-staph_precise165-meta
  kind: database
  reference: https://imodulondb.org/api/datasets/s_aureus/staph_precise165/meta
  locator: Full official response; metadata strain list or bounded gene/module fields;
    generated prose excluded; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/adapter-sa-staph_precise165-meta.raw
  accessed_at: '2026-11-04T02:04:39.265464Z'
  snapshot_sha256: e732e04d45161d2b8d3756e01ef513ad919572d25a3f877d4035f0fc57320f27
  summary: Current S. aureus staph_precise165 meta response independently inspected
    for exact strains and bounded vesicle/cargo context. USA300-related dataset strains
    are not substituted for the unverified strain of Lee2009; no absent biology is
    inferred.
  support: supports
- evidence_id: plaque-adapter-sa-staph_precise165-imodulons
  kind: database
  reference: https://imodulondb.org/api/datasets/s_aureus/staph_precise165/imodulons
  locator: Full official response; metadata strain list or bounded gene/module fields;
    generated prose excluded; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/adapter-sa-staph_precise165-imodulons.raw
  accessed_at: '2026-11-04T02:04:39.034256Z'
  snapshot_sha256: f3df2a552e914745c17f3609a237bd2ce3ca402ddb08b0f1d93375ca7b3a7e9c
  summary: Current S. aureus staph_precise165 imodulons response independently inspected
    for exact strains and bounded vesicle/cargo context. USA300-related dataset strains
    are not substituted for the unverified strain of Lee2009; no absent biology is
    inferred.
  support: supports
- evidence_id: plaque-adapter-sa-staph_precise165-genes-query
  kind: database
  reference: https://imodulondb.org/api/genes?organism=s_aureus&dataset=staph_precise165&limit=10000
  locator: Full official response; metadata strain list or bounded gene/module fields;
    generated prose excluded; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/adapter-sa-staph_precise165-genes-query.raw
  accessed_at: '2026-11-04T02:05:08.413966Z'
  snapshot_sha256: 221a852742a71c0110ace476ffd755b2d2f7b8b41a3de7687fccd279c3fdb7bd
  summary: Current S. aureus staph_precise165 genes-query response independently inspected
    for exact strains and bounded vesicle/cargo context. USA300-related dataset strains
    are not substituted for the unverified strain of Lee2009; no absent biology is
    inferred.
  support: supports
- evidence_id: plaque-adapter-bounded-search
  kind: search
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/adapter-bounded-results.json
  locator: Complete selected gene and module responses bound by SHA; literal-query
    matches retained in scratch
  accessed_at: '2026-11-04T02:06:09.314137Z'
  snapshot_sha256: d628cbf66ea2b3b19fe4db09f2415438f277866174d40c994facf7a176ca55b3
  summary: Queries vesicle/outer membrane/cargo return no literal vesicle/cargo module
    hits;57 E. coli gene annotations match outer membrane. No S. aureus literal matches
    in these selected fields. These are bounded annotation results, not absence of
    vesicles or mechanisms.
  support: context_only
  search_scope: Official iModulonDB datasets e_coli/precise1k (4257genes,201modules),
    s_aureus/staph_precise108 and staph_precise165 (all returned genes,29/76module
    rows); case-insensitive literal vesicle, outer membrane, cargo against gene_name/gene_product
    and module name/regulator/function/category only; all query results retained;
    no generated summaries, no other datasets or source organisms searched.
- evidence_id: plaque-adapter-ecoli-b0957-modules
  kind: database
  reference: https://imodulondb.org/api/genes/b0957/imodulons?organism=e_coli&dataset=precise1k
  locator: Complete selected-locus membership response; weights,thresholds,flags;
    matched K-12 context only; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/adapter-ecoli-b0957-modules.raw
  accessed_at: '2026-11-04T02:06:29.462081Z'
  snapshot_sha256: 26480475575b680bf13e7c6b1c5fe20dd657eb483c34a97f53b081ae40971c51
  summary: All201 selected gene-module rows read. ompA has no true membership flags
    in this dataset; this is not protein absence. Selected because Park discusses
    OmpA/OmpF as contextual outer-membrane cargo, not because the maintained record
    asserts these exact genes.
  support: supports
- evidence_id: plaque-adapter-ecoli-b0929-modules
  kind: database
  reference: https://imodulondb.org/api/genes/b0929/imodulons?organism=e_coli&dataset=precise1k
  locator: Complete selected-locus membership response; weights,thresholds,flags;
    matched K-12 context only; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/adapter-ecoli-b0929-modules.raw
  accessed_at: '2026-11-04T02:06:29.462061Z'
  snapshot_sha256: 28005163d210c91f8bfce0170e1ad178911893b90c38e6c62603e09ce67fcc8a
  summary: All201 selected gene-module rows read. ompF passes thresholds in22SoxS,25Lrp,86UC-3,88Nitrogen;
    these are computational expression contexts only. Selected because Park discusses
    OmpA/OmpF as contextual outer-membrane cargo, not because the maintained record
    asserts these exact genes.
  support: supports
- evidence_id: plaque-adapter-ecoli-module-22
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise1k/22
  locator: Official full module response; only name/regulator/function/category/threshold
    and selected b0929 gene weight independently read; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/adapter-ecoli-module-22.raw
  accessed_at: '2026-11-04T02:07:00.152399Z'
  snapshot_sha256: 75c93e893c864c0c0a515a7fb566fa97ed84141f008da563c9174b27e41e2703
  summary: Native module metadata, threshold and b0929 membership inspected; generated
    AI summary excluded. Does not certify OMV cargo, secretion, localization, host
    inflammation or exact experimental strain.
  support: context_only
- evidence_id: plaque-adapter-ecoli-module-25
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise1k/25
  locator: Official full module response; only name/regulator/function/category/threshold
    and selected b0929 gene weight independently read; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/adapter-ecoli-module-25.raw
  accessed_at: '2026-11-04T02:07:00.154315Z'
  snapshot_sha256: c9b5cb0e23bfd76f68f6d36d05f1e7b4e86c817963c523a440a5a01068f1f288
  summary: Native module metadata, threshold and b0929 membership inspected; generated
    AI summary excluded. Does not certify OMV cargo, secretion, localization, host
    inflammation or exact experimental strain.
  support: context_only
- evidence_id: plaque-adapter-ecoli-module-86
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise1k/86
  locator: Official full module response; only name/regulator/function/category/threshold
    and selected b0929 gene weight independently read; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/adapter-ecoli-module-86.raw
  accessed_at: '2026-11-04T02:07:00.158647Z'
  snapshot_sha256: dc010f69722e02c028497d05f252908be133ea75b0326156e53b8c3701ac8c8b
  summary: Native module metadata, threshold and b0929 membership inspected; generated
    AI summary excluded. Does not certify OMV cargo, secretion, localization, host
    inflammation or exact experimental strain.
  support: context_only
- evidence_id: plaque-adapter-ecoli-module-88
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise1k/88
  locator: Official full module response; only name/regulator/function/category/threshold
    and selected b0929 gene weight independently read; inspected response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/adapter-ecoli-module-88.raw
  accessed_at: '2026-11-04T02:07:00.158629Z'
  snapshot_sha256: 68d0e2ac5b8f540bcaa80ba7f5f49fc27cfc313ad5e57b194df6d57c14210c23
  summary: Native module metadata, threshold and b0929 membership inspected; generated
    AI summary excluded. Does not certify OMV cargo, secretion, localization, host
    inflammation or exact experimental strain.
  support: context_only
- evidence_id: plaque-original-current-validation
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-plaque/originals-current-proof.json
  locator: Four original native validate/render executions,55 historical input occurrences,47
    current frozen inputs
  accessed_at: '2026-11-04T02:11:03.460667Z'
  snapshot_sha256: 91b7e875d844569315897831e749a16b866557afbdb8bc0b2026456ca5a466ae
  summary: All four immutable original YAMLs validate and render byte-identically
    to their Markdown;55 historical input occurrences match their own frozen Git source
    after symlink resolution. All47 current frozen inputs match source and worktree.
    Three own targets unchanged; CBF3 stale delta explicitly reassessed.
  support: supports
- evidence_id: plaque-native-bacterial_extracellular_vesicle-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bacterial_extracellular_vesicle-uniprot-verify-receipt.json
  locator: Actual root command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record',
    'data/structures/other/bacterial_extracellular_vesicle.yaml', '--verify']; log
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bacterial_extracellular_vesicle-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T01:59:47.740332Z'
  snapshot_sha256: 1e130fa6a4516e813458e24cdc41181b6549377cf5b971f80c197b35b46988b6
  summary: 'Actual exit0 on source head; independently read command/log and current
    record inventory: 0 reviewed protein examples and 0 typed GENE_OR_PROTEIN nodes
    (all COVERED when nonempty). Generic verify success alone does not certify scientific
    mechanism or family grounding.'
  support: supports
- evidence_id: plaque-native-bacterial_extracellular_vesicle-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bacterial_extracellular_vesicle-uniprot-causal-receipt.json
  locator: Actual root command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record',
    'data/structures/other/bacterial_extracellular_vesicle.yaml', '--causal-graphs'];
    log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bacterial_extracellular_vesicle-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-04T01:59:48.226289Z'
  snapshot_sha256: c6d6c3e153a0dbe4c3f544c30868e893b3989665bc61604393d06e344e8dc832
  summary: 'Actual exit0 on source head; independently read command/log and current
    record inventory: 0 reviewed protein examples and 0 typed GENE_OR_PROTEIN nodes
    (all COVERED when nonempty). Generic verify success alone does not certify scientific
    mechanism or family grounding.'
  support: supports
- evidence_id: plaque-native-bacterial_outer_membrane_vesicle-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bacterial_outer_membrane_vesicle-uniprot-verify-receipt.json
  locator: Actual root command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record',
    'data/structures/other/bacterial_outer_membrane_vesicle.yaml', '--verify']; log
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bacterial_outer_membrane_vesicle-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T01:59:48.698445Z'
  snapshot_sha256: e6071fa3593f8ee26d36a92e652df9bb8593efb56a5b2d301fe763ff39c1f3cd
  summary: 'Actual exit0 on source head; independently read command/log and current
    record inventory: 0 reviewed protein examples and 0 typed GENE_OR_PROTEIN nodes
    (all COVERED when nonempty). Generic verify success alone does not certify scientific
    mechanism or family grounding.'
  support: supports
- evidence_id: plaque-native-bacterial_outer_membrane_vesicle-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bacterial_outer_membrane_vesicle-uniprot-causal-receipt.json
  locator: Actual root command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record',
    'data/structures/other/bacterial_outer_membrane_vesicle.yaml', '--causal-graphs'];
    log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bacterial_outer_membrane_vesicle-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-04T01:59:49.183136Z'
  snapshot_sha256: 2d99e99bfeecef438f6598277743ae1678d00dd2775b48d83074a34bd8471eb3
  summary: 'Actual exit0 on source head; independently read command/log and current
    record inventory: 0 reviewed protein examples and 0 typed GENE_OR_PROTEIN nodes
    (all COVERED when nonempty). Generic verify success alone does not certify scientific
    mechanism or family grounding.'
  support: supports
- evidence_id: plaque-native-caf_1_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/caf_1_complex-uniprot-verify-receipt.json
  locator: Actual root command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record',
    'data/structures/other/caf_1_complex.yaml', '--verify']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/caf_1_complex-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T02:00:00.809878Z'
  snapshot_sha256: 6ba871f24613640c702cdaf8be115a1faef7a07438ae58dd502a4f7f84dc44f5
  summary: 'Actual exit0 on source head; independently read command/log and current
    record inventory: 3 reviewed protein examples and 3 typed GENE_OR_PROTEIN nodes
    (all COVERED when nonempty). Generic verify success alone does not certify scientific
    mechanism or family grounding.'
  support: supports
- evidence_id: plaque-native-caf_1_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/caf_1_complex-uniprot-causal-receipt.json
  locator: Actual root command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record',
    'data/structures/other/caf_1_complex.yaml', '--causal-graphs']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/caf_1_complex-uniprot-causal.log
    SHA256 7e39addd5c8162efa08ca6a788ad23af636459a2c7ddaaae5d6fcdbba13e0349
  accessed_at: '2026-11-04T02:00:01.236947Z'
  snapshot_sha256: 8da62ff137d7c80fa72028f5f278ede0800d9bce95ff4f026dbfe70b26ba5bf6
  summary: 'Actual exit0 on source head; independently read command/log and current
    record inventory: 3 reviewed protein examples and 3 typed GENE_OR_PROTEIN nodes
    (all COVERED when nonempty). Generic verify success alone does not certify scientific
    mechanism or family grounding.'
  support: supports
- evidence_id: plaque-native-cbf3_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/cbf3_complex-uniprot-verify-receipt.json
  locator: Actual root command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record',
    'data/structures/other/cbf3_complex.yaml', '--verify']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/cbf3_complex-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T02:00:02.422686Z'
  snapshot_sha256: 8a17b0bdf4178eb4c8cc84765170a70c3baecb9300a75faccb01fb3a0ea2c80f
  summary: 'Actual exit0 on source head; independently read command/log and current
    record inventory: 4 reviewed protein examples and 4 typed GENE_OR_PROTEIN nodes
    (all COVERED when nonempty). Generic verify success alone does not certify scientific
    mechanism or family grounding.'
  support: supports
- evidence_id: plaque-native-cbf3_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/cbf3_complex-uniprot-causal-receipt.json
  locator: Actual root command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record',
    'data/structures/other/cbf3_complex.yaml', '--causal-graphs']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/cbf3_complex-uniprot-causal.log
    SHA256 f028d171b3b55fd59304e552aebec98f3c543e05a312100bc617d82e1397131f
  accessed_at: '2026-11-04T02:00:02.842842Z'
  snapshot_sha256: 60fe2f7eab1b8605ef7676987e4433ed00d630fdffc491d0047c5d9159d3ef4b
  summary: 'Actual exit0 on source head; independently read command/log and current
    record inventory: 4 reviewed protein examples and 4 typed GENE_OR_PROTEIN nodes
    (all COVERED when nonempty). Generic verify success alone does not certify scientific
    mechanism or family grounding.'
  support: supports
- evidence_id: micro-record-0
  kind: record_content
  reference: data/structures/other/bacterial_pre_replicative_complex.yaml
  locator: Complete current maintained YAML, all fields at exact source b82b8b5fcb02d90018a73c0d3d05ede8a2ab161f
  accessed_at: '2026-11-04T02:08:48.568645Z'
  support: supports
  summary: Whole target inspected including identity, history, components, protein
    examples, source placements, quantities, taxon scope, graph edges and discussions.
  snapshot_sha256: a4a8871a963f0b0eb3e32d9a677f099afdf3f6246dc7964f1890b61b3f01b62a
- evidence_id: micro-prior-0
  kind: prior_review
  reference: reviews/structured/20261022T044322Z-bacterial-pre-replicative-complex-audit/review.yaml
  locator: Original authoritative YAML and native rendered Markdown; all checks, scientific
    dimensions, findings/actions/source tiers
  accessed_at: '2026-11-04T02:08:48.568645Z'
  support: supports
  summary: Immutable original observation remains historical; exact predecessor lineage
    and actual frozen-source hashes are retained. Historical validation metadata is
    not recast as a current run.
  snapshot_sha256: 0f46df59f2c24561a55cb0bcfca7d535e1c71e83a8407a5ff446e73dfcd548fe
- evidence_id: micro-delta-0
  kind: record_content
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/5-stale.diff
  locator: Exact original frozen target revision to current main base
  accessed_at: '2026-11-04T02:08:48.568645Z'
  support: supports
  summary: BAM adds individual family-grounded lipoprotein nodes/parthood, BamA grounding,
    BamE xref and external OmpT substrate/product exemplars/K-12 context. Bindosome
    adds unreviewed AraS/SSO3066 example and history. Pre-RC is byte-identical. Each
    addition was substantively reassessed.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: micro-record-1
  kind: record_content
  reference: data/structures/other/bam_protein_complex.yaml
  locator: Complete current maintained YAML, all fields at exact source b82b8b5fcb02d90018a73c0d3d05ede8a2ab161f
  accessed_at: '2026-11-04T02:08:48.568645Z'
  support: supports
  summary: Whole target inspected including identity, history, components, protein
    examples, source placements, quantities, taxon scope, graph edges and discussions.
  snapshot_sha256: ac284bcf4e0ec8021b0f218143e2337a0845c36113edb097e79c950ac1688cde
- evidence_id: micro-prior-1
  kind: prior_review
  reference: reviews/structured/20261022T044323Z-bam-protein-complex-audit/review.yaml
  locator: Original authoritative YAML and native rendered Markdown; all checks, scientific
    dimensions, findings/actions/source tiers
  accessed_at: '2026-11-04T02:08:48.568645Z'
  support: supports
  summary: Immutable original observation remains historical; exact predecessor lineage
    and actual frozen-source hashes are retained. Historical validation metadata is
    not recast as a current run.
  snapshot_sha256: 85a2536611ef781a45b0f5e986a05214590cfad7b7237a67e89ae26e8cec3772
- evidence_id: micro-delta-1
  kind: record_content
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/6-stale.diff
  locator: Exact original frozen target revision to current main base
  accessed_at: '2026-11-04T02:08:48.568645Z'
  support: supports
  summary: BAM adds individual family-grounded lipoprotein nodes/parthood, BamA grounding,
    BamE xref and external OmpT substrate/product exemplars/K-12 context. Bindosome
    adds unreviewed AraS/SSO3066 example and history. Pre-RC is byte-identical. Each
    addition was substantively reassessed.
  snapshot_sha256: 43905b60ce8636cfa6b4733236970d435e448d8b88e925fc34ec48379c630951
- evidence_id: micro-record-2
  kind: record_content
  reference: data/structures/other/bindosome_complex.yaml
  locator: Complete current maintained YAML, all fields at exact source b82b8b5fcb02d90018a73c0d3d05ede8a2ab161f
  accessed_at: '2026-11-04T02:08:48.568645Z'
  support: supports
  summary: Whole target inspected including identity, history, components, protein
    examples, source placements, quantities, taxon scope, graph edges and discussions.
  snapshot_sha256: 360a186c82ed29ddaae42fdbcb445a37b8482be97bed64a6d077792b8fdce375
- evidence_id: micro-prior-2
  kind: prior_review
  reference: reviews/structured/20261022T044323Z-bindosome-complex-audit/review.yaml
  locator: Original authoritative YAML and native rendered Markdown; all checks, scientific
    dimensions, findings/actions/source tiers
  accessed_at: '2026-11-04T02:08:48.568645Z'
  support: supports
  summary: Immutable original observation remains historical; exact predecessor lineage
    and actual frozen-source hashes are retained. Historical validation metadata is
    not recast as a current run.
  snapshot_sha256: 3c4e32c35bf0fd463a99f3c7c3a97043f9816189dd950b3fa5e227fd7e55abcd
- evidence_id: micro-delta-2
  kind: record_content
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/7-stale.diff
  locator: Exact original frozen target revision to current main base
  accessed_at: '2026-11-04T02:08:48.568645Z'
  support: supports
  summary: BAM adds individual family-grounded lipoprotein nodes/parthood, BamA grounding,
    BamE xref and external OmpT substrate/product exemplars/K-12 context. Bindosome
    adds unreviewed AraS/SSO3066 example and history. Pre-RC is byte-identical. Each
    addition was substantively reassessed.
  snapshot_sha256: 36cb25a2158241e2d1e9af4cead306fa221001434db29ae6e3073826359ae337
- evidence_id: micro-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Evidence, Components/grounding/formation essentiality and Discussions append-only
    rules
  accessed_at: '2026-11-04T02:08:48.568645Z'
  support: supports
  summary: Component families/classes and organism examples are separate; exact verified
    family terms replace actionable label-only gaps. Essentiality concerns structure
    formation, not viability. Dated rationale/posed_date remain historical; current
    prompts/notes can be narrowed.
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
- evidence_id: micro-native-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Complete native route, source adapter rules, active config/profile and
    checklist
  accessed_at: '2026-11-04T02:08:48.568645Z'
  support: supports
  summary: Positive protein/pathway assertions trigger source cross-checks even without
    expression claims; all actual scopes and validation limitations must remain explicit.
    Frozen common policy bytes equal the previously read PR2381 set, with relevant
    route/profile/CURATION/checklist/graph sections freshly reread.
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: micro-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Whole native graph skill plus frozen schema/component and external-actor
    rules
  accessed_at: '2026-11-04T02:08:48.568645Z'
  support: supports
  summary: Generic family/class and complex actors are permitted; external substrate
    xrefs are not forced into constituent membership. Coarse NONMECHANISTIC outlines
    need not invent atomic contacts.
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: micro-original-audit
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/original-audit.json
  locator: Six actual original validate/render commands;42 original source-input checks;
    six original artifacts immutable
  accessed_at: '2026-11-04T02:08:48.568645Z'
  support: supports
  summary: All three original YAMLs validate; paired Markdown is exact native render.
    All42 frozen source-input hashes match their original Git revisions; old target
    hashes and current staleness independently verified.
  snapshot_sha256: b56292c0ee75e11d33d804b35861aff13ba1017f2dba1d17e024b39150699ceb
- evidence_id: micro-up-P03004
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P03004.json
  locator: Exact accession/status/name/gene and ordered loci/taxon; relevant FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION and evidence-code/citation joins; InterPro identifiers; exact retained
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/up-P03004.raw
  accessed_at: '2026-11-04T02:01:09.945440Z'
  support: supports
  summary: 'P03004: UniProtKB reviewed (Swiss-Prot); taxon83333; name Chromosomal
    replication initiator protein DnaA; primary gene fields [''dnaA'']; ordered loci
    [''b3702'', ''JW3679'']; InterPro [''IPR003593'', ''IPR001957'', ''IPR020591'',
    ''IPR018312'', ''IPR013159'', ''IPR013317'', ''IPR024633'', ''IPR038454'', ''IPR027417'',
    ''IPR010921'']. Q97UF5 has ordered locus SSO3066, no native araS geneName and
    is explicitly UNREVIEWED; the literature mapping is checked separately. Native
    annotations are not fresh primary-body experiments.'
  snapshot_sha256: 20b9ed0385942a0aebc3645f0f499a77e9aab0741218e2327ee80b6ae7590dca
- evidence_id: micro-up-P09169
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P09169.json
  locator: Exact accession/status/name/gene and ordered loci/taxon; relevant FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION and evidence-code/citation joins; InterPro identifiers; exact retained
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/up-P09169.raw
  accessed_at: '2026-11-04T02:01:08.318445Z'
  support: supports
  summary: 'P09169: UniProtKB reviewed (Swiss-Prot); taxon83333; name Protease 7;
    primary gene fields [''ompT'']; ordered loci [''b0565'', ''JW0554'']; InterPro
    [''IPR020080'', ''IPR020079'', ''IPR000036'']. Q97UF5 has ordered locus SSO3066,
    no native araS geneName and is explicitly UNREVIEWED; the literature mapping is
    checked separately. Native annotations are not fresh primary-body experiments.'
  snapshot_sha256: 56cb13b33704bd3201109b063b92bf3afa5eb6a57bbeaa48e433d6cec392711d
- evidence_id: micro-up-P0A903
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0A903.json
  locator: Exact accession/status/name/gene and ordered loci/taxon; relevant FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION and evidence-code/citation joins; InterPro identifiers; exact retained
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/up-P0A903.raw
  accessed_at: '2026-11-04T02:01:09.853779Z'
  support: supports
  summary: 'P0A903: UniProtKB reviewed (Swiss-Prot); taxon83333; name Outer membrane
    protein assembly factor BamC; primary gene fields [''bamC'']; ordered loci [''b2477'',
    ''JW2462'']; InterPro [''IPR014524'', ''IPR010653'', ''IPR064009'', ''IPR042268''].
    Q97UF5 has ordered locus SSO3066, no native araS geneName and is explicitly UNREVIEWED;
    the literature mapping is checked separately. Native annotations are not fresh
    primary-body experiments.'
  snapshot_sha256: 584c056225b866005264ce4b2288722d06ff5adf60d6f217a65b59e6b0c22c60
- evidence_id: micro-up-P0A937
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0A937.json
  locator: Exact accession/status/name/gene and ordered loci/taxon; relevant FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION and evidence-code/citation joins; InterPro identifiers; exact retained
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/up-P0A937.raw
  accessed_at: '2026-11-04T02:01:08.933171Z'
  support: supports
  summary: 'P0A937: UniProtKB reviewed (Swiss-Prot); taxon83333; name Outer membrane
    protein assembly factor BamE; primary gene fields [''bamE'']; ordered loci [''b2617'',
    ''JW2598'']; InterPro [''IPR026592'', ''IPR037873'', ''IPR007450'']. Q97UF5 has
    ordered locus SSO3066, no native araS geneName and is explicitly UNREVIEWED; the
    literature mapping is checked separately. Native annotations are not fresh primary-body
    experiments.'
  snapshot_sha256: 4a0d6c264c3eaa5fbb921ec2c0abd09825d2085e08bb12556cce6c15677e5d03
- evidence_id: micro-up-P0A940
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0A940.json
  locator: Exact accession/status/name/gene and ordered loci/taxon; relevant FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION and evidence-code/citation joins; InterPro identifiers; exact retained
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/up-P0A940.raw
  accessed_at: '2026-11-04T02:01:08.933208Z'
  support: supports
  summary: 'P0A940: UniProtKB reviewed (Swiss-Prot); taxon83333; name Outer membrane
    protein assembly factor BamA; primary gene fields [''bamA'']; ordered loci [''b0177'',
    ''JW0172'']; InterPro [''IPR000184'', ''IPR010827'', ''IPR039910'', ''IPR023707'',
    ''IPR034746'']. Q97UF5 has ordered locus SSO3066, no native araS geneName and
    is explicitly UNREVIEWED; the literature mapping is checked separately. Native
    annotations are not fresh primary-body experiments.'
  snapshot_sha256: 2ff846ae12669c4bab0ccd5ee26ee045bc2c77b2c49c18bfcf90adaee3a2296d
- evidence_id: micro-up-P0AC02
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0AC02.json
  locator: Exact accession/status/name/gene and ordered loci/taxon; relevant FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION and evidence-code/citation joins; InterPro identifiers; exact retained
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/up-P0AC02.raw
  accessed_at: '2026-11-04T02:01:10.913881Z'
  support: supports
  summary: 'P0AC02: UniProtKB reviewed (Swiss-Prot); taxon83333; name Outer membrane
    protein assembly factor BamD; primary gene fields [''bamD'']; ordered loci [''b2595'',
    ''JW2577'']; InterPro [''IPR017689'', ''IPR039565'', ''IPR011990'']. Q97UF5 has
    ordered locus SSO3066, no native araS geneName and is explicitly UNREVIEWED; the
    literature mapping is checked separately. Native annotations are not fresh primary-body
    experiments.'
  snapshot_sha256: 97262e786c9e1d055dd17acbcc26d085df95a8e0206f10d3ad247dc545a4902b
- evidence_id: micro-up-P77774
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P77774.json
  locator: Exact accession/status/name/gene and ordered loci/taxon; relevant FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION and evidence-code/citation joins; InterPro identifiers; exact retained
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/up-P77774.raw
  accessed_at: '2026-11-04T02:01:10.772778Z'
  support: supports
  summary: 'P77774: UniProtKB reviewed (Swiss-Prot); taxon83333; name Outer membrane
    protein assembly factor BamB; primary gene fields [''bamB'']; ordered loci [''b2512'',
    ''JW2496'']; InterPro [''IPR017687'', ''IPR018391'', ''IPR002372'', ''IPR011047'',
    ''IPR015943'']. Q97UF5 has ordered locus SSO3066, no native araS geneName and
    is explicitly UNREVIEWED; the literature mapping is checked separately. Native
    annotations are not fresh primary-body experiments.'
  snapshot_sha256: 2ef03b2f0a01756551013ff513ba85409096bdb8d13b57be1991bd465d1376e1
- evidence_id: micro-up-Q97UF5
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q97UF5.json
  locator: Exact accession/status/name/gene and ordered loci/taxon; relevant FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION and evidence-code/citation joins; InterPro identifiers; exact retained
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/up-Q97UF5.raw
  accessed_at: '2026-11-04T02:01:11.695113Z'
  support: supports
  summary: 'Q97UF5: UniProtKB unreviewed (TrEMBL); taxon273057; name Arabinose ABC
    transporter, arabinose binding protein; primary gene fields [None]; ordered loci
    [''SSO3066'']; InterPro [''IPR050490'', ''IPR054925'']. Q97UF5 has ordered locus
    SSO3066, no native araS geneName and is explicitly UNREVIEWED; the literature
    mapping is checked separately. Native annotations are not fresh primary-body experiments.'
  snapshot_sha256: 66a5b763eb2aef6bafe3c50c10c321790037a84cf704064442886107a07182b3
- evidence_id: micro-up-Q97UZ1
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q97UZ1.json
  locator: Exact accession/status/name/gene and ordered loci/taxon; relevant FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION and evidence-code/citation joins; InterPro identifiers; exact retained
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/up-Q97UZ1.raw
  accessed_at: '2026-11-04T02:01:08.318395Z'
  support: supports
  summary: 'Q97UZ1: UniProtKB reviewed (Swiss-Prot); taxon273057; name Glucose-binding
    protein GlcS; primary gene fields [''glcS'']; ordered loci [''SSO2847'']; InterPro
    [''IPR050490'', ''IPR054925'']. Q97UF5 has ordered locus SSO3066, no native araS
    geneName and is explicitly UNREVIEWED; the literature mapping is checked separately.
    Native annotations are not fresh primary-body experiments.'
  snapshot_sha256: ab20b08d6a5ca97a249809693768cb209dd925df6620275e9c03a874d7d79941
- evidence_id: micro-query-SSO3066
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASSO3066%29+AND+%28organism_id%3A273057%29&format=json&size=100
  locator: Complete exact gene/taxon result page and accession identities; exact retained
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/query-SSO3066.raw
  accessed_at: '2026-11-04T02:01:42.019079Z'
  support: supports
  summary: '1 returned accessions: [''Q97UF5'']. Reviewed E. coli dnaA/BAM/OmpT and
    P2 glcS queries each return the intended unique entry. P2 araS/treS return0, while
    SSO3066 returns Q97UF5; absence of an alias in this index is not gene absence
    or refutation of a primary literature mapping.'
  snapshot_sha256: 338a7e70b6d752f96c57fdbb8fc83286b214260c511d3a8bf87d49ec9bd11ce7
  search_scope: UniProtKB REST at 2026-11-04T02:01:42.019079Z; exact query in URL;
    organism83333 for dnaA/bamA–E/ompT with reviewed:true; organism273057 for glcS
    with reviewed:true and araS/treS/SSO3066 without reviewed filter; size100, complete
    returned first page, each0or1result. No inference beyond these specific current
    symbols/taxa.
- evidence_id: micro-query-araS
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AaraS%29+AND+%28organism_id%3A273057%29&format=json&size=100
  locator: Complete exact gene/taxon result page and accession identities; exact retained
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/query-araS.raw
  accessed_at: '2026-11-04T02:01:39.757100Z'
  support: supports
  summary: '0 returned accessions: []. Reviewed E. coli dnaA/BAM/OmpT and P2 glcS
    queries each return the intended unique entry. P2 araS/treS return0, while SSO3066
    returns Q97UF5; absence of an alias in this index is not gene absence or refutation
    of a primary literature mapping.'
  snapshot_sha256: 5021e624e752b001ce3e3846e8f158ed4aeb93a4c9a72fdb35a0c5b14a0eea84
  search_scope: UniProtKB REST at 2026-11-04T02:01:39.757100Z; exact query in URL;
    organism83333 for dnaA/bamA–E/ompT with reviewed:true; organism273057 for glcS
    with reviewed:true and araS/treS/SSO3066 without reviewed filter; size100, complete
    returned first page, each0or1result. No inference beyond these specific current
    symbols/taxa.
- evidence_id: micro-query-bamA
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AbamA%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete exact gene/taxon result page and accession identities; exact retained
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/query-bamA.raw
  accessed_at: '2026-11-04T02:01:38.155272Z'
  support: supports
  summary: '1 returned accessions: [''P0A940'']. Reviewed E. coli dnaA/BAM/OmpT and
    P2 glcS queries each return the intended unique entry. P2 araS/treS return0, while
    SSO3066 returns Q97UF5; absence of an alias in this index is not gene absence
    or refutation of a primary literature mapping.'
  snapshot_sha256: eedefca132b33d6adebab88357ec41c7c549af0160a80fe342ec9c5c2ed76809
  search_scope: UniProtKB REST at 2026-11-04T02:01:38.155272Z; exact query in URL;
    organism83333 for dnaA/bamA–E/ompT with reviewed:true; organism273057 for glcS
    with reviewed:true and araS/treS/SSO3066 without reviewed filter; size100, complete
    returned first page, each0or1result. No inference beyond these specific current
    symbols/taxa.
- evidence_id: micro-query-bamB
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AbamB%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete exact gene/taxon result page and accession identities; exact retained
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/query-bamB.raw
  accessed_at: '2026-11-04T02:01:38.581563Z'
  support: supports
  summary: '1 returned accessions: [''P77774'']. Reviewed E. coli dnaA/BAM/OmpT and
    P2 glcS queries each return the intended unique entry. P2 araS/treS return0, while
    SSO3066 returns Q97UF5; absence of an alias in this index is not gene absence
    or refutation of a primary literature mapping.'
  snapshot_sha256: a5fb6bdb8a6d22d3789192420f7891e4f381de850cf4cc724acdffe4383b890e
  search_scope: UniProtKB REST at 2026-11-04T02:01:38.581563Z; exact query in URL;
    organism83333 for dnaA/bamA–E/ompT with reviewed:true; organism273057 for glcS
    with reviewed:true and araS/treS/SSO3066 without reviewed filter; size100, complete
    returned first page, each0or1result. No inference beyond these specific current
    symbols/taxa.
- evidence_id: micro-query-bamC
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AbamC%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete exact gene/taxon result page and accession identities; exact retained
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/query-bamC.raw
  accessed_at: '2026-11-04T02:01:38.180962Z'
  support: supports
  summary: '1 returned accessions: [''P0A903'']. Reviewed E. coli dnaA/BAM/OmpT and
    P2 glcS queries each return the intended unique entry. P2 araS/treS return0, while
    SSO3066 returns Q97UF5; absence of an alias in this index is not gene absence
    or refutation of a primary literature mapping.'
  snapshot_sha256: 073444923c46fbd03e5e35ea4c1d56f51a2e76205a35aee6e9b0d426378fd5f4
  search_scope: UniProtKB REST at 2026-11-04T02:01:38.180962Z; exact query in URL;
    organism83333 for dnaA/bamA–E/ompT with reviewed:true; organism273057 for glcS
    with reviewed:true and araS/treS/SSO3066 without reviewed filter; size100, complete
    returned first page, each0or1result. No inference beyond these specific current
    symbols/taxa.
- evidence_id: micro-query-bamD
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AbamD%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete exact gene/taxon result page and accession identities; exact retained
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/query-bamD.raw
  accessed_at: '2026-11-04T02:01:39.869789Z'
  support: supports
  summary: '1 returned accessions: [''P0AC02'']. Reviewed E. coli dnaA/BAM/OmpT and
    P2 glcS queries each return the intended unique entry. P2 araS/treS return0, while
    SSO3066 returns Q97UF5; absence of an alias in this index is not gene absence
    or refutation of a primary literature mapping.'
  snapshot_sha256: 3863cd5db0a7c555cf2dba77d3a52ae3a8ebd3681a6821e8628e854c010497ca
  search_scope: UniProtKB REST at 2026-11-04T02:01:39.869789Z; exact query in URL;
    organism83333 for dnaA/bamA–E/ompT with reviewed:true; organism273057 for glcS
    with reviewed:true and araS/treS/SSO3066 without reviewed filter; size100, complete
    returned first page, each0or1result. No inference beyond these specific current
    symbols/taxa.
- evidence_id: micro-query-bamE
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AbamE%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete exact gene/taxon result page and accession identities; exact retained
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/query-bamE.raw
  accessed_at: '2026-11-04T02:01:40.940506Z'
  support: supports
  summary: '1 returned accessions: [''P0A937'']. Reviewed E. coli dnaA/BAM/OmpT and
    P2 glcS queries each return the intended unique entry. P2 araS/treS return0, while
    SSO3066 returns Q97UF5; absence of an alias in this index is not gene absence
    or refutation of a primary literature mapping.'
  snapshot_sha256: 2c3d1d8bec5ecedd19c04c83b35c47c779714bbbb1ffb76af766770cff82d765
  search_scope: UniProtKB REST at 2026-11-04T02:01:40.940506Z; exact query in URL;
    organism83333 for dnaA/bamA–E/ompT with reviewed:true; organism273057 for glcS
    with reviewed:true and araS/treS/SSO3066 without reviewed filter; size100, complete
    returned first page, each0or1result. No inference beyond these specific current
    symbols/taxa.
- evidence_id: micro-query-dnaA
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdnaA%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete exact gene/taxon result page and accession identities; exact retained
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/query-dnaA.raw
  accessed_at: '2026-11-04T02:01:37.991945Z'
  support: supports
  summary: '1 returned accessions: [''P03004'']. Reviewed E. coli dnaA/BAM/OmpT and
    P2 glcS queries each return the intended unique entry. P2 araS/treS return0, while
    SSO3066 returns Q97UF5; absence of an alias in this index is not gene absence
    or refutation of a primary literature mapping.'
  snapshot_sha256: 3db63cf0e2bda46f5e0d2292b32f98621aa2da23fba568a428d8ad2f1fb148a0
  search_scope: UniProtKB REST at 2026-11-04T02:01:37.991945Z; exact query in URL;
    organism83333 for dnaA/bamA–E/ompT with reviewed:true; organism273057 for glcS
    with reviewed:true and araS/treS/SSO3066 without reviewed filter; size100, complete
    returned first page, each0or1result. No inference beyond these specific current
    symbols/taxa.
- evidence_id: micro-query-glcS
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AglcS%29+AND+%28organism_id%3A273057%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete exact gene/taxon result page and accession identities; exact retained
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/query-glcS.raw
  accessed_at: '2026-11-04T02:01:40.945394Z'
  support: supports
  summary: '1 returned accessions: [''Q97UZ1'']. Reviewed E. coli dnaA/BAM/OmpT and
    P2 glcS queries each return the intended unique entry. P2 araS/treS return0, while
    SSO3066 returns Q97UF5; absence of an alias in this index is not gene absence
    or refutation of a primary literature mapping.'
  snapshot_sha256: 0f356de3c236cf57a55d69c15ea9b80fabfb8cbd596e620a0c2e384bcc1a4c4b
  search_scope: UniProtKB REST at 2026-11-04T02:01:40.945394Z; exact query in URL;
    organism83333 for dnaA/bamA–E/ompT with reviewed:true; organism273057 for glcS
    with reviewed:true and araS/treS/SSO3066 without reviewed filter; size100, complete
    returned first page, each0or1result. No inference beyond these specific current
    symbols/taxa.
- evidence_id: micro-query-ompT
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AompT%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete exact gene/taxon result page and accession identities; exact retained
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/query-ompT.raw
  accessed_at: '2026-11-04T02:01:38.814198Z'
  support: supports
  summary: '1 returned accessions: [''P09169'']. Reviewed E. coli dnaA/BAM/OmpT and
    P2 glcS queries each return the intended unique entry. P2 araS/treS return0, while
    SSO3066 returns Q97UF5; absence of an alias in this index is not gene absence
    or refutation of a primary literature mapping.'
  snapshot_sha256: 5909b2a14b5647e02a0b6d7c1522676e4f5c9d136c1a8babd772a79b921208bc
  search_scope: UniProtKB REST at 2026-11-04T02:01:38.814198Z; exact query in URL;
    organism83333 for dnaA/bamA–E/ompT with reviewed:true; organism273057 for glcS
    with reviewed:true and araS/treS/SSO3066 without reviewed filter; size100, complete
    returned first page, each0or1result. No inference beyond these specific current
    symbols/taxa.
- evidence_id: micro-query-treS
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AtreS%29+AND+%28organism_id%3A273057%29&format=json&size=100
  locator: Complete exact gene/taxon result page and accession identities; exact retained
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/query-treS.raw
  accessed_at: '2026-11-04T02:01:38.848113Z'
  support: supports
  summary: '0 returned accessions: []. Reviewed E. coli dnaA/BAM/OmpT and P2 glcS
    queries each return the intended unique entry. P2 araS/treS return0, while SSO3066
    returns Q97UF5; absence of an alias in this index is not gene absence or refutation
    of a primary literature mapping.'
  snapshot_sha256: 54399c680da725ef98caa870323f4ef32b3e1d1a89e6c039118d9f8148cf4bda
  search_scope: UniProtKB REST at 2026-11-04T02:01:38.848113Z; exact query in URL;
    organism83333 for dnaA/bamA–E/ompT with reviewed:true; organism273057 for glcS
    with reviewed:true and araS/treS/SSO3066 without reviewed filter; size100, complete
    returned first page, each0or1result. No inference beyond these specific current
    symbols/taxa.
- evidence_id: micro-ipr-IPR001957
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001957/
  locator: Exact name/type, complete description/flags, hierarchy and native example
    cross-reference; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/ipr-IPR001957.raw
  accessed_at: '2026-11-04T02:01:08.625160Z'
  support: supports
  summary: 'IPR001957: Chromosomal replication control, initiator DnaA; family. IPR001957
    is DnaA-specific; IPR020591 explicitly also includes Hda. The five BAM terms match
    their full named families. IPR054925 has an unchecked LLM description and IPR050490
    a checked LLM description; neither establishes the whole mixed bindosome cohort
    or primary membership.'
  snapshot_sha256: 364ea5ab4304d290b099574c7f9527e5577eefec2872f8fc2adde34de7eb2fc2
- evidence_id: micro-ipr-IPR014524
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR014524/
  locator: Exact name/type, complete description/flags, hierarchy and native example
    cross-reference; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/ipr-IPR014524.raw
  accessed_at: '2026-11-04T02:01:09.672680Z'
  support: supports
  summary: 'IPR014524: Outer membrane protein assembly factor BamC; family. IPR001957
    is DnaA-specific; IPR020591 explicitly also includes Hda. The five BAM terms match
    their full named families. IPR054925 has an unchecked LLM description and IPR050490
    a checked LLM description; neither establishes the whole mixed bindosome cohort
    or primary membership.'
  snapshot_sha256: e628a709adce13480ab5a3280fbffc7b8e8af5b546acd438be423992354b0164
- evidence_id: micro-ipr-IPR017687
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR017687/
  locator: Exact name/type, complete description/flags, hierarchy and native example
    cross-reference; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/ipr-IPR017687.raw
  accessed_at: '2026-11-04T02:01:09.546683Z'
  support: supports
  summary: 'IPR017687: Outer membrane protein assembly factor BamB; family. IPR001957
    is DnaA-specific; IPR020591 explicitly also includes Hda. The five BAM terms match
    their full named families. IPR054925 has an unchecked LLM description and IPR050490
    a checked LLM description; neither establishes the whole mixed bindosome cohort
    or primary membership.'
  snapshot_sha256: 4a1e68d606e1300e5d42418dc06954d330eea3f450edd6de5feb2edb0d8e091a
- evidence_id: micro-ipr-IPR017689
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR017689/
  locator: Exact name/type, complete description/flags, hierarchy and native example
    cross-reference; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/ipr-IPR017689.raw
  accessed_at: '2026-11-04T02:01:09.663419Z'
  support: supports
  summary: 'IPR017689: Outer membrane protein assembly factor BamD; family. IPR001957
    is DnaA-specific; IPR020591 explicitly also includes Hda. The five BAM terms match
    their full named families. IPR054925 has an unchecked LLM description and IPR050490
    a checked LLM description; neither establishes the whole mixed bindosome cohort
    or primary membership.'
  snapshot_sha256: 0f8fe8ba57b5271c42ba4a610111c9a46e8a0731f8c4fb661b1763d36939434e
- evidence_id: micro-ipr-IPR020591
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR020591/
  locator: Exact name/type, complete description/flags, hierarchy and native example
    cross-reference; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/ipr-IPR020591.raw
  accessed_at: '2026-11-04T02:01:09.342561Z'
  support: supports
  summary: 'IPR020591: Chromosomal replication control, initiator DnaA-like; family.
    IPR001957 is DnaA-specific; IPR020591 explicitly also includes Hda. The five BAM
    terms match their full named families. IPR054925 has an unchecked LLM description
    and IPR050490 a checked LLM description; neither establishes the whole mixed bindosome
    cohort or primary membership.'
  snapshot_sha256: 344ddf6a7a77fa3c9a45e8b2871365bab93b04f9b9f51c6b3139d559cb858dff
- evidence_id: micro-ipr-IPR023707
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR023707/
  locator: Exact name/type, complete description/flags, hierarchy and native example
    cross-reference; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/ipr-IPR023707.raw
  accessed_at: '2026-11-04T02:01:09.230477Z'
  support: supports
  summary: 'IPR023707: Outer membrane protein assembly factor BamA; family. IPR001957
    is DnaA-specific; IPR020591 explicitly also includes Hda. The five BAM terms match
    their full named families. IPR054925 has an unchecked LLM description and IPR050490
    a checked LLM description; neither establishes the whole mixed bindosome cohort
    or primary membership.'
  snapshot_sha256: 6332e23f488ba575c9b64f72ca33529ea7708cbc683ce6ea8c92d5be517ebda4
- evidence_id: micro-ipr-IPR026592
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR026592/
  locator: Exact name/type, complete description/flags, hierarchy and native example
    cross-reference; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/ipr-IPR026592.raw
  accessed_at: '2026-11-04T02:01:09.957099Z'
  support: supports
  summary: 'IPR026592: Outer membrane protein assembly factor BamE; family. IPR001957
    is DnaA-specific; IPR020591 explicitly also includes Hda. The five BAM terms match
    their full named families. IPR054925 has an unchecked LLM description and IPR050490
    a checked LLM description; neither establishes the whole mixed bindosome cohort
    or primary membership.'
  snapshot_sha256: 042bb194391df3d7402d2cce4e49dde1b549d3430d435dfa2a12b49e0b96239d
- evidence_id: micro-ipr-IPR050490
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050490/
  locator: Exact name/type, complete description/flags, hierarchy and native example
    cross-reference; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/ipr-IPR050490.raw
  accessed_at: '2026-11-04T02:03:03.996987Z'
  support: supports
  summary: 'IPR050490: Bacterial solute-binding protein 1; family. IPR001957 is DnaA-specific;
    IPR020591 explicitly also includes Hda. The five BAM terms match their full named
    families. IPR054925 has an unchecked LLM description and IPR050490 a checked LLM
    description; neither establishes the whole mixed bindosome cohort or primary membership.'
  snapshot_sha256: 019ee5f62494ea1df993c079c6fdfdda2c8f87773ca23adf4031363aaf218219
- evidence_id: micro-ipr-IPR054925
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR054925/
  locator: Exact name/type, complete description/flags, hierarchy and native example
    cross-reference; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/ipr-IPR054925.raw
  accessed_at: '2026-11-04T02:03:03.976398Z'
  support: supports
  summary: 'IPR054925: Glucose-binding protein GlcS; family. IPR001957 is DnaA-specific;
    IPR020591 explicitly also includes Hda. The five BAM terms match their full named
    families. IPR054925 has an unchecked LLM description and IPR050490 a checked LLM
    description; neither establishes the whole mixed bindosome cohort or primary membership.'
  snapshot_sha256: f0c2d4d1af8c3520d645f50e22eed82baaf522ccc6c8fdb22bd0f6527f37234c
- evidence_id: micro-go-0006270
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0006270
  locator: Exact active ID/name/definition and returned typed relationships or explicitly
    requested ancestor relation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/go-0006270.raw
  accessed_at: '2026-11-04T02:01:10.875976Z'
  support: supports
  summary: GO:0006270 DNA replication initiation; active=True. Ancestor results are
    transitive and relation-specific, not automatically direct edges. BAM is_a-only
    response does not include GO0106234, while part_of includes GO0009279; definition-based
    broader outer-membrane-complex classification is not thereby disproved.
  snapshot_sha256: e0ea96216a022971fca313127bdae0280af832afc23734001e734b67973c6601
- evidence_id: micro-go-0009279
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0009279
  locator: Exact active ID/name/definition and returned typed relationships or explicitly
    requested ancestor relation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/go-0009279.raw
  accessed_at: '2026-11-04T02:01:11.290830Z'
  support: supports
  summary: GO:0009279 cell outer membrane; active=True. Ancestor results are transitive
    and relation-specific, not automatically direct edges. BAM is_a-only response
    does not include GO0106234, while part_of includes GO0009279; definition-based
    broader outer-membrane-complex classification is not thereby disproved.
  snapshot_sha256: e409d4cc35ee2bc43ec4277998ff26a6d1b08138f2a7047601bc60d82f66ffa8
- evidence_id: micro-go-0032993
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0032993
  locator: Exact active ID/name/definition and returned typed relationships or explicitly
    requested ancestor relation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/go-0032993.raw
  accessed_at: '2026-11-04T02:01:10.283139Z'
  support: supports
  summary: GO:0032993 protein-DNA complex; active=True. Ancestor results are transitive
    and relation-specific, not automatically direct edges. BAM is_a-only response
    does not include GO0106234, while part_of includes GO0009279; definition-based
    broader outer-membrane-complex classification is not thereby disproved.
  snapshot_sha256: f25fd4bcd2b214be8f9ebe7538707984f53a6825554f7f18830819457512e0d6
- evidence_id: micro-go-0036387
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0036387
  locator: Exact active ID/name/definition and returned typed relationships or explicitly
    requested ancestor relation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/go-0036387.raw
  accessed_at: '2026-11-04T02:01:10.283180Z'
  support: supports
  summary: GO:0036387 pre-replicative complex; active=True. Ancestor results are transitive
    and relation-specific, not automatically direct edges. BAM is_a-only response
    does not include GO0106234, while part_of includes GO0009279; definition-based
    broader outer-membrane-complex classification is not thereby disproved.
  snapshot_sha256: 56e1671cb67c14e42ee288efb2a97440203f9fe2b81aafe71d4f8afe52c08183
- evidence_id: micro-go-0036389-is_a
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0036389/ancestors?relations=is_a
  locator: Exact active ID/name/definition and returned typed relationships or explicitly
    requested ancestor relation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/go-0036389-is_a.raw
  accessed_at: '2026-11-04T02:03:03.426640Z'
  support: supports
  summary: GO:0036389 bacterial pre-replicative complex; active=True. Ancestor results
    are transitive and relation-specific, not automatically direct edges. BAM is_a-only
    response does not include GO0106234, while part_of includes GO0009279; definition-based
    broader outer-membrane-complex classification is not thereby disproved.
  snapshot_sha256: 0896afcd2cf7273057c03fd123ec80e8bb5e715248c920bb5f62f356c2c551fb
- evidence_id: micro-go-0036389-part_of
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0036389/ancestors?relations=part_of
  locator: Exact active ID/name/definition and returned typed relationships or explicitly
    requested ancestor relation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/go-0036389-part_of.raw
  accessed_at: '2026-11-04T02:03:03.448666Z'
  support: supports
  summary: GO:0036389 bacterial pre-replicative complex; active=True. Ancestor results
    are transitive and relation-specific, not automatically direct edges. BAM is_a-only
    response does not include GO0106234, while part_of includes GO0009279; definition-based
    broader outer-membrane-complex classification is not thereby disproved.
  snapshot_sha256: 8da66f4ac447795b03dcb9e8d692dbb0275605c610c2c6040903db2fb4234306
- evidence_id: micro-go-0036389
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0036389
  locator: Exact active ID/name/definition and returned typed relationships or explicitly
    requested ancestor relation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/go-0036389.raw
  accessed_at: '2026-11-04T02:01:09.945399Z'
  support: supports
  summary: GO:0036389 bacterial pre-replicative complex; active=True. Ancestor results
    are transitive and relation-specific, not automatically direct edges. BAM is_a-only
    response does not include GO0106234, while part_of includes GO0009279; definition-based
    broader outer-membrane-complex classification is not thereby disproved.
  snapshot_sha256: 7460ed4ac9e03c1718d0159ac7201bd2e913e23951d120bbecf97767b570eb6a
- evidence_id: micro-go-0098796
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0098796
  locator: Exact active ID/name/definition and returned typed relationships or explicitly
    requested ancestor relation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/go-0098796.raw
  accessed_at: '2026-11-04T02:01:11.752678Z'
  support: supports
  summary: GO:0098796 membrane protein complex; active=True. Ancestor results are
    transitive and relation-specific, not automatically direct edges. BAM is_a-only
    response does not include GO0106234, while part_of includes GO0009279; definition-based
    broader outer-membrane-complex classification is not thereby disproved.
  snapshot_sha256: c0b9ee522071e5d1930dde6110f8ec3b3f939a2f12cdb77914e864b1fa04d5bb
- evidence_id: micro-go-0106234
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0106234
  locator: Exact active ID/name/definition and returned typed relationships or explicitly
    requested ancestor relation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/go-0106234.raw
  accessed_at: '2026-11-04T02:01:11.263203Z'
  support: supports
  summary: GO:0106234 outer membrane protein complex; active=True. Ancestor results
    are transitive and relation-specific, not automatically direct edges. BAM is_a-only
    response does not include GO0106234, while part_of includes GO0009279; definition-based
    broader outer-membrane-complex classification is not thereby disproved.
  snapshot_sha256: 8f8128ee2c0da85aa33a58499ccb0e6ece7ef9a30ca6dc92bf69b89f60fd713b
- evidence_id: micro-go-1990063-is_a
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990063/ancestors?relations=is_a
  locator: Exact active ID/name/definition and returned typed relationships or explicitly
    requested ancestor relation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/go-1990063-is_a.raw
  accessed_at: '2026-11-04T02:03:03.443057Z'
  support: supports
  summary: GO:1990063 Bam protein complex; active=True. Ancestor results are transitive
    and relation-specific, not automatically direct edges. BAM is_a-only response
    does not include GO0106234, while part_of includes GO0009279; definition-based
    broader outer-membrane-complex classification is not thereby disproved.
  snapshot_sha256: bd4dc08d6bd0f803e3f2eee8f0580914baf2237435a71fc14c81e05fafa5e80e
- evidence_id: micro-go-1990063-part_of
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990063/ancestors?relations=part_of
  locator: Exact active ID/name/definition and returned typed relationships or explicitly
    requested ancestor relation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/go-1990063-part_of.raw
  accessed_at: '2026-11-04T02:03:03.437127Z'
  support: supports
  summary: GO:1990063 Bam protein complex; active=True. Ancestor results are transitive
    and relation-specific, not automatically direct edges. BAM is_a-only response
    does not include GO0106234, while part_of includes GO0009279; definition-based
    broader outer-membrane-complex classification is not thereby disproved.
  snapshot_sha256: e33ff357e9e4e891ed09d7f96514fd289cd87e57fc4343acbff8406a1337d214
- evidence_id: micro-go-1990063
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990063
  locator: Exact active ID/name/definition and returned typed relationships or explicitly
    requested ancestor relation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/go-1990063.raw
  accessed_at: '2026-11-04T02:01:11.263243Z'
  support: supports
  summary: GO:1990063 Bam protein complex; active=True. Ancestor results are transitive
    and relation-specific, not automatically direct edges. BAM is_a-only response
    does not include GO0106234, while part_of includes GO0009279; definition-based
    broader outer-membrane-complex classification is not thereby disproved.
  snapshot_sha256: 1d1d101f4e2090e831ab4688539b417f47add12c6aa07c3adff2791542dc1004
- evidence_id: micro-go-1990100
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990100
  locator: Exact active ID/name/definition and returned typed relationships or explicitly
    requested ancestor relation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/go-1990100.raw
  accessed_at: '2026-11-04T02:01:10.876078Z'
  support: supports
  summary: GO:1990100 DnaB-DnaC complex; active=True. Ancestor results are transitive
    and relation-specific, not automatically direct edges. BAM is_a-only response
    does not include GO0106234, while part_of includes GO0009279; definition-based
    broader outer-membrane-complex classification is not thereby disproved.
  snapshot_sha256: 14aade75f1106c27c76f8328692e6163b9f5747df82f2666322cb2f7b668725d
- evidence_id: micro-go-1990101
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990101
  locator: Exact active ID/name/definition and returned typed relationships or explicitly
    requested ancestor relation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/go-1990101.raw
  accessed_at: '2026-11-04T02:01:10.468036Z'
  support: supports
  summary: GO:1990101 DnaA-oriC complex; active=True. Ancestor results are transitive
    and relation-specific, not automatically direct edges. BAM is_a-only response
    does not include GO0106234, while part_of includes GO0009279; definition-based
    broader outer-membrane-complex classification is not thereby disproved.
  snapshot_sha256: 0a23d28413a48d3195664bac9a2d0f0c0fd55fb4be3062eddcc3561867fc4342
- evidence_id: micro-go-1990102
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990102
  locator: Exact active ID/name/definition and returned typed relationships or explicitly
    requested ancestor relation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/go-1990102.raw
  accessed_at: '2026-11-04T02:01:10.876029Z'
  support: supports
  summary: GO:1990102 DnaA-DiaA complex; active=True. Ancestor results are transitive
    and relation-specific, not automatically direct edges. BAM is_a-only response
    does not include GO0106234, while part_of includes GO0009279; definition-based
    broader outer-membrane-complex classification is not thereby disproved.
  snapshot_sha256: dabec07dbf0f550e085d5eca8f679ec7c974d9f3b7d0c402c801e8ca02876715
- evidence_id: micro-go-1990103
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990103
  locator: Exact active ID/name/definition and returned typed relationships or explicitly
    requested ancestor relation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/go-1990103.raw
  accessed_at: '2026-11-04T02:01:10.875929Z'
  support: supports
  summary: GO:1990103 DnaA-HU complex; active=True. Ancestor results are transitive
    and relation-specific, not automatically direct edges. BAM is_a-only response
    does not include GO0106234, while part_of includes GO0009279; definition-based
    broader outer-membrane-complex classification is not thereby disproved.
  snapshot_sha256: 433297d5c7b21f84956999f2541404720751083b9bf905f22cd353f5bf4d6017
- evidence_id: micro-go-7770042-is_a
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A7770042/ancestors?relations=is_a
  locator: Exact active ID/name/definition and returned typed relationships or explicitly
    requested ancestor relation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/go-7770042-is_a.raw
  accessed_at: '2026-11-04T02:03:03.373164Z'
  support: supports
  summary: GO:7770042 bindosome complex; active=True. Ancestor results are transitive
    and relation-specific, not automatically direct edges. BAM is_a-only response
    does not include GO0106234, while part_of includes GO0009279; definition-based
    broader outer-membrane-complex classification is not thereby disproved.
  snapshot_sha256: 7e6fcd1a8e59e01bb4b059db912a904753196f76070d704046cdc841651079c0
- evidence_id: micro-go-7770042-part_of
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A7770042/ancestors?relations=part_of
  locator: Exact active ID/name/definition and returned typed relationships or explicitly
    requested ancestor relation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/go-7770042-part_of.raw
  accessed_at: '2026-11-04T02:03:03.445954Z'
  support: supports
  summary: GO:7770042 bindosome complex; active=True. Ancestor results are transitive
    and relation-specific, not automatically direct edges. BAM is_a-only response
    does not include GO0106234, while part_of includes GO0009279; definition-based
    broader outer-membrane-complex classification is not thereby disproved.
  snapshot_sha256: e5c20f5bf76b0364cb863a2642a50789833d40e11e97dfd9cd7fd697149251b8
- evidence_id: micro-go-7770042
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A7770042
  locator: Exact active ID/name/definition and returned typed relationships or explicitly
    requested ancestor relation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/go-7770042.raw
  accessed_at: '2026-11-04T02:01:11.437789Z'
  support: supports
  summary: GO:7770042 bindosome complex; active=True. Ancestor results are transitive
    and relation-specific, not automatically direct edges. BAM is_a-only response
    does not include GO0106234, while part_of includes GO0009279; definition-based
    broader outer-membrane-complex classification is not thereby disproved.
  snapshot_sha256: 459855847457771b6ce7d536092e383739d620a63aefd8ee39436f423e8c974b
- evidence_id: micro-tax-562
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/562.json
  locator: Complete native taxon identifier/name/rank/lineage; exact retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/tax-562.raw
  accessed_at: '2026-11-04T02:01:13.744866Z'
  support: supports
  summary: Exact taxonomy identity checked; historical Sulfolobus versus current Saccharolobus
    names do not change species/P2 identity. Reference accession strain, experimental
    host and dataset strains remain distinct.
  snapshot_sha256: 20aa358053d2fae1e2cd74636ed5aca1efbc372e5b8bcfdb10d3fa80be6789a1
- evidence_id: micro-tax-83333
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/83333.json
  locator: Complete native taxon identifier/name/rank/lineage; exact retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/tax-83333.raw
  accessed_at: '2026-11-04T02:01:12.729048Z'
  support: supports
  summary: Exact taxonomy identity checked; historical Sulfolobus versus current Saccharolobus
    names do not change species/P2 identity. Reference accession strain, experimental
    host and dataset strains remain distinct.
  snapshot_sha256: 83c59ae9694d1874b8a175d7ce7608f77f5688d35adf307a0859dbb20f9e1c17
- evidence_id: micro-tax-2
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/2.json
  locator: Complete native taxon identifier/name/rank/lineage; exact retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/tax-2.raw
  accessed_at: '2026-11-04T02:01:11.830267Z'
  support: supports
  summary: Exact taxonomy identity checked; historical Sulfolobus versus current Saccharolobus
    names do not change species/P2 identity. Reference accession strain, experimental
    host and dataset strains remain distinct.
  snapshot_sha256: 8074c9bcd59cd4da1da4bc9ec98c040bbecd52ef5c91c4c4bb9bed0f3a7cb5a9
- evidence_id: micro-tax-2287
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/2287.json
  locator: Complete native taxon identifier/name/rank/lineage; exact retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/tax-2287.raw
  accessed_at: '2026-11-04T02:01:13.744905Z'
  support: supports
  summary: Exact taxonomy identity checked; historical Sulfolobus versus current Saccharolobus
    names do not change species/P2 identity. Reference accession strain, experimental
    host and dataset strains remain distinct.
  snapshot_sha256: c9e15d8c665809a6d9a5a3b64b80ee3bc73847e381c0d535c5670b93011173f8
- evidence_id: micro-tax-273057
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/273057.json
  locator: Complete native taxon identifier/name/rank/lineage; exact retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/tax-273057.raw
  accessed_at: '2026-11-04T02:01:12.731272Z'
  support: supports
  summary: Exact taxonomy identity checked; historical Sulfolobus versus current Saccharolobus
    names do not change species/P2 identity. Reference accession strain, experimental
    host and dataset strains remain distinct.
  snapshot_sha256: a91261e09ed7539c4897f525c6aeb870cd2f486c79f617c0f62894efafef3954
- evidence_id: micro-uo-0000222
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uo/terms?obo_id=UO:0000222
  locator: Exact OLS UO term name/identifier/definition; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/uo-0000222.raw
  accessed_at: '2026-11-04T02:01:12.092253Z'
  support: supports
  summary: UO0000222 kilodalton resolves; approximate203kDa measurement remains tied
    to the purified E. coli BAM preparation.
  snapshot_sha256: 76b2847684bc23e048e4930291a2496762989586108c42140ecb256d72a1e74c
- evidence_id: micro-miller2009-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A19833870+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact native bibliographic identity and complete deposited abstract; body
    scope separately enumerated; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/miller2009-meta.raw
  accessed_at: '2026-11-04T02:01:12.099547Z'
  support: partial
  summary: Bacterial origin recognition complexes direct assembly of higher-order
    DnaA oligomeric structures.; Miller DT, Grimwade JE, Betteridge T, Rozgaja T,
    Torgue JJ, Leonard AC.; DOI 10.1073/pnas.0909472106. Primary abstract tier only
    in this evidence row; no unread body is certified.
  snapshot_sha256: f43be6d64081917dc470114814b4074f2218f98de054c1c371aec9ab1cd934de
- evidence_id: micro-leonard2010-meta
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A21035377+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact native bibliographic identity and complete deposited abstract; body
    scope separately enumerated; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/leonard2010-meta.raw
  accessed_at: '2026-11-04T02:01:12.098458Z'
  support: context_only
  summary: 'Regulating DnaA complex assembly: it is time to fill the gaps.; Leonard
    AC, Grimwade JE.; DOI 10.1016/j.mib.2010.10.001. Secondary review context, not
    direct experimental evidence.'
  snapshot_sha256: 3de30e5684dcf881f4843101623e0ffeb43e1f77c6a0aaf680408af38444dbf2
- evidence_id: micro-hagan2010-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1126%2Fscience.1188919%22&format=json&resultType=core&pageSize=10
  locator: Exact native bibliographic identity and complete deposited abstract; body
    scope separately enumerated; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/hagan2010-meta.raw
  accessed_at: '2026-11-04T02:01:12.573790Z'
  support: partial
  summary: Reconstitution of outer membrane protein assembly from purified components.;
    Hagan CL, Kim S, Kahne D.; DOI 10.1126/science.1188919. Primary abstract tier
    only in this evidence row; no unread body is certified.
  snapshot_sha256: f50465065f10aef344f386e9842bf22001c727e5739a2facd5142970da0f823b
- evidence_id: micro-hagan2011-meta
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1146%2Fannurev-biochem-061408-144611%22&format=json&resultType=core&pageSize=10
  locator: Exact native bibliographic identity and complete deposited abstract; body
    scope separately enumerated; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/hagan2011-meta.raw
  accessed_at: '2026-11-04T02:01:12.573879Z'
  support: context_only
  summary: β-Barrel membrane protein assembly by the Bam complex.; Hagan CL, Silhavy
    TJ, Kahne D.; DOI 10.1146/annurev-biochem-061408-144611. Secondary review context,
    not direct experimental evidence.
  snapshot_sha256: 0cc313f113346b1155ea63705084ddcfe3150f2ae71e6d2d4f521a2185117811
- evidence_id: micro-gu2016-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fnature17199%22&format=json&resultType=core&pageSize=10
  locator: Exact native bibliographic identity and complete deposited abstract; body
    scope separately enumerated; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/gu2016-meta.raw
  accessed_at: '2026-11-04T02:01:12.824441Z'
  support: partial
  summary: Structural basis of outer membrane protein insertion by the BAM complex.;
    Gu Y, Li H, Dong H, Zeng Y, Zhang Z, Paterson NG, Stansfeld PJ, Wang Z, Zhang
    Y, Wang W, Dong C.; DOI 10.1038/nature17199. Primary abstract tier only in this
    evidence row; no unread body is certified.
  snapshot_sha256: 874cef44b0cbb11766ad4e80e13e4c76dec4cc3fa5e786972cd4fc5bbbe9ee2e
- evidence_id: micro-iadanza2016-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fncomms12865%22&format=json&resultType=core&pageSize=10
  locator: Exact native bibliographic identity and complete deposited abstract; body
    scope separately enumerated; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/iadanza2016-meta.raw
  accessed_at: '2026-11-04T02:01:13.014506Z'
  support: partial
  summary: Lateral opening in the intact β-barrel assembly machinery captured by cryo-EM.;
    Iadanza MG, Higgins AJ, Schiffrin B, Calabrese AN, Brockwell DJ, Ashcroft AE,
    Radford SE, Ranson NA.; DOI 10.1038/ncomms12865. Primary abstract tier only in
    this evidence row; no unread body is certified.
  snapshot_sha256: be7a86b779fb8086825c1d306ca48645b4c0705c6d04b6b5bbf269eccb41e372
- evidence_id: micro-bakelar2016-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1126%2Fscience.aad3460%22&format=json&resultType=core&pageSize=10
  locator: Exact native bibliographic identity and complete deposited abstract; body
    scope separately enumerated; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/bakelar2016-meta.raw
  accessed_at: '2026-11-04T02:01:13.270070Z'
  support: partial
  summary: The structure of the β-barrel assembly machinery complex.; Bakelar J, Buchanan
    SK, Noinaj N.; DOI 10.1126/science.aad3460. Primary abstract tier only in this
    evidence row; no unread body is certified.
  snapshot_sha256: 459db605107caff0ce790a7e5a5066310d30040263a61aac81349a42b8ed9a16
- evidence_id: micro-zolghadr2011-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1007%2Fs00792-010-0353-0%22&format=json&resultType=core&pageSize=10
  locator: Exact native bibliographic identity and complete deposited abstract; body
    scope separately enumerated; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/zolghadr2011-meta.raw
  accessed_at: '2026-11-04T02:01:13.129610Z'
  support: partial
  summary: The bindosome is a structural component of the Sulfolobus solfataricus
    cell envelope.; Zolghadr B, Klingl A, Rachel R, Driessen AJ, Albers SV.; DOI 10.1007/s00792-010-0353-0.
    Primary abstract tier only in this evidence row; no unread body is certified.
  snapshot_sha256: 53ba84843400d6db7711a391911ba32be5baaf6e3a70c18caaa010a7608dcb79
- evidence_id: micro-elferink2001-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11260467+AND+SRC%3AMED&format=json&resultType=core&pageSize=100
  locator: Exact native bibliographic identity and complete deposited abstract; body
    scope separately enumerated; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/elferink2001-meta.raw
  accessed_at: '2026-11-04T02:03:03.397165Z'
  support: partial
  summary: Sugar transport in Sulfolobus solfataricus is mediated by two families
    of binding protein-dependent ABC transporters.; Elferink MG, Albers SV, Konings
    WN, Driessen AJ.; DOI 10.1046/j.1365-2958.2001.02336.x. Primary abstract tier
    only in this evidence row; no unread body is certified.
  snapshot_sha256: c97d4af6e6c565ac3e8520f9e526e9d5f8bd67bfac9a39bb28239ff304e400da
- evidence_id: micro-go-bindosome-ref-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A38877064+AND+SRC%3AMED&format=json&resultType=core&pageSize=100
  locator: Exact native bibliographic identity and complete deposited abstract; body
    scope separately enumerated; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/go-bindosome-ref-meta.raw
  accessed_at: '2026-11-04T02:03:03.464687Z'
  support: partial
  summary: Two distinct archaeal type IV pili structures formed by proteins with identical
    sequence.; Liu J, Eastep GN, Cvirkaite-Krupovic V, Rich-New ST, Kreutzberger MAB,
    Egelman EH, Krupovic M, Wang F.; DOI 10.1038/s41467-024-45062-z. Primary abstract
    tier only in this evidence row; no unread body is certified.
  snapshot_sha256: b770833a2c5fcb3a13fdcef9dd6c52a519cbaaf50da1c52ef69dfbf8eb7afaaf
- evidence_id: micro-pmid-15851030
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15851030+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact MED ID/title/authors/DOI and complete abstract, joined separately
    to native protein annotation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/pmid-15851030.raw
  accessed_at: '2026-11-04T02:02:09.025769Z'
  support: partial
  summary: Identification of a multicomponent complex required for outer membrane
    biogenesis in Escherichia coli.; Wu T, Malinverni J, Ruiz N, Kim S, Silhavy TJ,
    Kahne D.. Additional localization/complex annotation paper inspected at abstract
    tier only; no full body, all strains or unobserved measurements are certified.
  snapshot_sha256: 1e81ed1ea294da7ffe1bd820fc4e31f8bee8e314b947535dfa79a1f0d66c6236
- evidence_id: micro-pmid-16079137
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A16079137+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact MED ID/title/authors/DOI and complete abstract, joined separately
    to native protein annotation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/pmid-16079137.raw
  accessed_at: '2026-11-04T02:02:09.003034Z'
  support: partial
  summary: Protein complexes of the Escherichia coli cell envelope.; Stenberg F, Chovanec
    P, Maslen SL, Robinson CV, Ilag LL, von Heijne G, Daley DO.. Additional localization/complex
    annotation paper inspected at abstract tier only; no full body, all strains or
    unobserved measurements are certified.
  snapshot_sha256: d2b490fc521f56402549d0cc5d0134ebcbadf199e42ba992216b0504d51519ae
- evidence_id: micro-pmid-17404237
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A17404237+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact MED ID/title/authors/DOI and complete abstract, joined separately
    to native protein annotation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/pmid-17404237.raw
  accessed_at: '2026-11-04T02:02:09.105055Z'
  support: partial
  summary: Lipoprotein SmpA is a component of the YaeT complex that assembles outer
    membrane proteins in Escherichia coli.; Sklar JG, Wu T, Gronenberg LS, Malinverni
    JC, Kahne D, Silhavy TJ.. Additional localization/complex annotation paper inspected
    at abstract tier only; no full body, all strains or unobserved measurements are
    certified.
  snapshot_sha256: 62440605df5a4fafa575bed266b4a80dd3bbee85a4f1c4e84684ac58010e0a8e
- evidence_id: micro-pmid-22574163
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A22574163+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact MED ID/title/authors/DOI and complete abstract, joined separately
    to native protein annotation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/pmid-22574163.raw
  accessed_at: '2026-11-04T02:02:09.016262Z'
  support: partial
  summary: 'Association of the chromosome replication initiator DnaA with the Escherichia
    coli inner membrane in vivo: quantity and mode of binding.; Regev T, Myers N,
    Zarivach R, Fishov I.. Additional localization/complex annotation paper inspected
    at abstract tier only; no full body, all strains or unobserved measurements are
    certified.'
  snapshot_sha256: 3f8e6cf736bae4a359c4f0bdfbe99616714f9ddab7a4636d401c42a3edb7fa57
- evidence_id: micro-pmid-23882017
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A23882017+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact MED ID/title/authors/DOI and complete abstract, joined separately
    to native protein annotation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/pmid-23882017.raw
  accessed_at: '2026-11-04T02:02:09.043472Z'
  support: partial
  summary: Receptor polymorphism restricts contact-dependent growth inhibition to
    members of the same species.; Ruhe ZC, Wallace AB, Low DA, Hayes CS.. Additional
    localization/complex annotation paper inspected at abstract tier only; no full
    body, all strains or unobserved measurements are certified.
  snapshot_sha256: 389d0a7fafcaedc03727c8cd5e00191da277d979c5ba703d2ecfd717ee834150
- evidence_id: micro-pmid-24619089
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A24619089+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact MED ID/title/authors/DOI and complete abstract, joined separately
    to native protein annotation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/pmid-24619089.raw
  accessed_at: '2026-11-04T02:02:09.022574Z'
  support: partial
  summary: Structural and functional analysis of the β-barrel domain of BamA from
    Escherichia coli.; Ni D, Wang Y, Yang X, Zhou H, Hou X, Cao B, Lu Z, Zhao X, Yang
    K, Huang Y.. Additional localization/complex annotation paper inspected at abstract
    tier only; no full body, all strains or unobserved measurements are certified.
  snapshot_sha256: 7a56df382acf378c5ea8908cb69dd1d9c3a42f82ccc7a525011e233b921df222
- evidence_id: micro-pmid-26900875
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A26900875+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact MED ID/title/authors/DOI and complete abstract, joined separately
    to native protein annotation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/pmid-26900875.raw
  accessed_at: '2026-11-04T02:02:09.105014Z'
  support: partial
  summary: Structure of the BAM complex and its implications for biogenesis of outer-membrane
    proteins.; Han L, Zheng J, Wang Y, Yang X, Liu Y, Sun C, Cao B, Zhou H, Ni D,
    Lou J, Zhao Y, Huang Y.. Additional localization/complex annotation paper inspected
    at abstract tier only; no full body, all strains or unobserved measurements are
    certified.
  snapshot_sha256: b8e5b2a7997ae28b8188071724ad85cc3125f036171a0e8b7d4e8ed1f0e3b233
- evidence_id: micro-pmid-28166228
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A28166228+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact MED ID/title/authors/DOI and complete abstract, joined separately
    to native protein annotation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/pmid-28166228.raw
  accessed_at: '2026-11-04T02:02:09.009671Z'
  support: partial
  summary: Rapid turnover of DnaA at replication origin regions contributes to initiation
    control of DNA replication.; Schenk K, Hervás AB, Rösch TC, Eisemann M, Schmitt
    BA, Dahlke S, Kleine-Borgmann L, Murray SM, Graumann PL.. Additional localization/complex
    annotation paper inspected at abstract tier only; no full body, all strains or
    unobserved measurements are certified.
  snapshot_sha256: 655ae2c90f7be7bdc5e6458020e0a32225f6fd25650eaebc96141c04e441ef7e
- evidence_id: micro-pmid-9478970
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9478970+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact MED ID/title/authors/DOI and complete abstract, joined separately
    to native protein annotation; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/pmid-9478970.raw
  accessed_at: '2026-11-04T02:02:09.032915Z'
  support: partial
  summary: Membrane-mediated release of nucleotide from an initiator of chromosomal
    replication, Escherichia coli DnaA, occurs with insertion of a distinct region
    of the protein into the lipid bilayer.; Garner J, Durrer P, Kitchen J, Brunner
    J, Crooke E.. Additional localization/complex annotation paper inspected at abstract
    tier only; no full body, all strains or unobserved measurements are certified.
  snapshot_sha256: c0c1a51874e90d0ad3f50eeb075877994afe3963692d663f3d105c5b2089b29c
- evidence_id: micro-miller2009-legacy
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2773971/?pdf=render
  locator: Complete Introduction, Results sec2–5, Discussion sec6 and Methods sec8–12;
    Fig1–6 captions, no pixels; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/miller2009-legacy.raw
  accessed_at: '2026-11-04T02:02:08.485582Z'
  support: supports
  summary: E. coli oriC high-affinity sites recruit oligomerization-proficient DnaA
    to lower-affinity sites; site mutants, DMS footprints, W6A, crosslinks and EMSA
    support this assembly stage. P3478/polA, W3110 and PC2/dnaC(ts) experiments and
    tagged purified proteins are explicit; generic pre-RC is not conflated with one
    restricted substate or every later helicase-loading step.
  snapshot_sha256: c6b4c92a8d72dd2a0b23931dec903e3fd4427be0c0545d6bed1f13b710d99032
- evidence_id: micro-leonard2010-body
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3005629.1/PMC3005629.1.xml
  locator: Secondary review Introduction S1, Extending the model S7 and Conclusions
    S8 only; no claim of complete body reading; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/leonard2010-body.raw
  accessed_at: '2026-11-04T02:01:37.498189Z'
  support: context_only
  summary: Review distinguishes DnaA/oriC pre-RC assembly and species-dependent origin
    architectures. Its proposed gap-filling model and optional regulatory factors
    are not direct experiments or mandatory components of every generic record.
  snapshot_sha256: bf00c1242f9597caffd3b5adbc902433d7ef3b3bdfa22c2bf4ea0ad1ffcb24ca
- evidence_id: micro-hagan2010-body
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2873164.1/PMC2873164.1.xml
  locator: Complete nine main-text paragraphs before Supplementary Material; embedded
    main text, no supplementary methods or figure pixels; exact retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/hagan2010-body.raw
  accessed_at: '2026-11-04T02:01:37.450616Z'
  support: supports
  summary: Purified BamAB+BamCDE reconstructed complex with SurA folds and inserts
    OmpT in proteoliposomes; enzymatic fluorescence, heat-modifiability and carbonate
    resistance provide complementary evidence. Activity/viability necessity differs
    from formation;1:1:1:1 and ambiguous1or2BamE,7%yield and possible oligomers are
    contextual rather than universal composition. K-12 reference exemplar does not
    certify the uninspected exact experimental cloning strain.
  snapshot_sha256: b649cb255d47549aa7097c8d19cbe513a7a2e7e0ad8bca008896c9ba8bee5ebd
- evidence_id: micro-bakelar2016-body
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4883095.1/PMC4883095.1.xml
  locator: Main-text structure/interaction/conformation paragraphs; Methods S2–4 expression,
    purification/crystallization and modeling; no pixels/maps/supplementary tables;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/bakelar2016-body.raw
  accessed_at: '2026-11-04T02:01:37.483101Z'
  support: supports
  summary: Crystal material is BamACDE after BamB loss; modeled full BAM docks a separate
    BamAB structure. BamC/D/E interfaces, BamD TPR/POTRA and BamE bridge support organization;
    BL21(DE3) expression differs from native reference K-12. Structural observation
    is not a universal catalytic trajectory.
  snapshot_sha256: 65be5700ff853ad48e8186c21d980ecc8bbf77fe60f3e5ddf557cf78c9bf1b02
- evidence_id: micro-iadanza2016-body
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5056442.1/PMC5056442.1.xml
  locator: Introduction, all seven Results subsections, Discussion; Methods expression/purification
    and proteoliposome reconstitution; no raw maps/pixels/supplemental tables; exact
    retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/iadanza2016-body.raw
  accessed_at: '2026-11-04T02:01:37.524876Z'
  support: supports
  summary: Intact BamABCDE cryo-EM at4.9Å captures lateral opening with BamB present.
    Predominant native MS203456±22Da and minor additionalBamE distinguish approximate
    mass from invariant composition. OmpT activity/crosslink rescue supports bounded
    gating; detergent, BL21(DE3), reconstitution and substrate dependence remain explicit.
  snapshot_sha256: 0452f756a8c8fe0f727f589a4420643be71ca335f559b953c8c6bba9bae8b12a
- evidence_id: micro-gu2016-author
  kind: primary_source
  reference: https://ueaeprints.uea.ac.uk/id/eprint/57584/1/BAM_Nature_Gu_29012016_2_change_Figure_legends_3_revised_accepted.pdf
  locator: Accepted manuscript printed pp1–8 through initial BamA–BamD interface discussion
    and Methods cloning/expression/purification pp27–29; text extraction only, no
    pixels; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/gu2016-author.raw
  accessed_at: '2026-11-04T02:03:14.453634Z'
  support: supports
  summary: Five-subunit inward-open and four-subunit lateral-open crystal complexes
    are distinct. BamB binds POTRA2/3; BamC engages BamD; BamE couples BamD with BamA
    POTRA4/5. HDB150/pJH114, additional bamB expression and DH5alpha plasmid preparation
    bound experimental scope; intact lateral-open observation is separately Iadanza,
    not attributed to Gu.
  snapshot_sha256: e032a8e60fdd821e5e00f33268f9b232a0dc3970e6f65db4faa804bbbc71ec23
- evidence_id: micro-zolghadr2011-body
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3047682.1/PMC3047682.1.xml
  locator: Entire Introduction, Methods and Results Sec1–15 plus Discussion Sec16
    and captions; complete retained body literal TreS/trehalose check; no figure pixels;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/zolghadr2011-body.raw
  accessed_at: '2026-11-04T02:01:37.499402Z'
  support: supports
  summary: PBL2025/ΔbasEF envelope extraction/ConA/BN-PAGE and size exclusion recover400/600kDa
    complexes with GlcS/SSO3043 and SlaA/SSO1273. BasEF deletion preserves extracted
    complexes but impairs glucose uptake; localization/handoff and native assembly
    remain partly inferred. AraS appears in arabinose context; complete cited body
    does not name TreS. This is bounded source support, not biological absence.
  snapshot_sha256: ccd28c7cdd1fd7ca52ea4c17d6d43916a4e8a1d56610f7b64a5ac4d295703a06
- evidence_id: micro-albers2003-legacy
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC161584/
  locator: Exact Table2 whole ORF/signal/function inventory and adjacent Discussion
    on PibD specificity/processing; no pixels, other body sections not certified;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/albers2003-legacy.raw
  accessed_at: '2026-11-04T02:04:19.634436Z'
  support: supports
  summary: Table2 maps SSO3066 to AraS and SSO0999 to TreS; Discussion explicitly
    names GlcS/TreS/AraS processing. This supports AraS locus identity and positively
    establishes TreS identity/processing context, but does not itself show TreS in
    the mature400/600kDa complexes of the maintained2011 source.
  snapshot_sha256: df76171e8b5c9534199fb36843b0916d4dd4d9ecf0164125335f23009e8baa70
- evidence_id: micro-aras-locus-meta
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%28SSO3066+OR+%22araS%22%29+AND+Sulfolobus&format=json&resultType=core&pageSize=100
  locator: Complete bounded result metadata list; selected exact Albers2003 paper
    separately read; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/aras-locus-meta.raw
  accessed_at: '2026-11-04T02:03:04.644431Z'
  support: supports
  summary: Current query returns56 records. Broad araS query read as metadata/title-selection
    only, not56 full articles; exact SSO3066 query returns7 and identifies Albers2003.
    No all-literature absence conclusion.
  snapshot_sha256: 8275a71f599b7226cb39c363221eb975eaf26b18617d26bb7672f5d4da29de40
  search_scope: Europe PMC at2026-11-04T02:03:04.644431Z, exact query URL; resultTypecore,pageSize100;
    returned complete56-record metadata list. Bounds are these queries only; only
    separately cited bodies were read.
- evidence_id: micro-locus-exact-meta
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%22SSO3066%22&format=json&resultType=core&pageSize=100
  locator: Complete bounded result metadata list; selected exact Albers2003 paper
    separately read; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/locus-exact-meta.raw
  accessed_at: '2026-11-04T02:03:56.244888Z'
  support: supports
  summary: Current query returns7 records. Broad araS query read as metadata/title-selection
    only, not56 full articles; exact SSO3066 query returns7 and identifies Albers2003.
    No all-literature absence conclusion.
  snapshot_sha256: b684a7b1215c561060f1d891e3742664f23065c7da26d0527e45e369c71c9f81
  search_scope: Europe PMC at2026-11-04T02:03:56.244888Z, exact query URL; resultTypecore,pageSize100;
    returned complete7-record metadata list. Bounds are these queries only; only separately
    cited bodies were read.
- evidence_id: micro-access-miller2009-body
  kind: validation
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2773971.1/PMC2773971.1.xml
  locator: Actual failed public source response; not scientific article content
  accessed_at: '2026-11-04T02:01:37.304979Z'
  support: context_only
  summary: HTTP404 body unavailable on this route; genuine alternatives for Miller/Albers
    were separately read. Elferink/Hagan2011 remain abstract-limited.
  snapshot_sha256: e8716581e20f0919d3166d1bd76b2a80fa854dec2849f45e06f85edc65d2ef47
- evidence_id: micro-access-albers2003-body
  kind: validation
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC161584.1/PMC161584.1.xml
  locator: Actual failed public source response; not scientific article content
  accessed_at: '2026-11-04T02:04:19.623793Z'
  support: context_only
  summary: HTTP404 body unavailable on this route; genuine alternatives for Miller/Albers
    were separately read. Elferink/Hagan2011 remain abstract-limited.
  snapshot_sha256: b0d6d224ed4bbcb941c30a18e00c632880b1dbb8740189cea33382c08673d788
- evidence_id: micro-access-elferink-publisher
  kind: validation
  reference: https://onlinelibrary.wiley.com/doi/10.1046/j.1365-2958.2001.02336.x
  locator: Actual failed public source response; not scientific article content
  accessed_at: '2026-11-04T02:03:55.656715Z'
  support: context_only
  summary: HTTP403 body unavailable on this route; genuine alternatives for Miller/Albers
    were separately read. Elferink/Hagan2011 remain abstract-limited.
  snapshot_sha256: b23ccb6c3db57e822ded950264cbd5983fdefb020eb264f14fe5c3025104d1ca
- evidence_id: micro-access-hagan2011-publisher
  kind: validation
  reference: https://www.annualreviews.org/content/journals/10.1146/annurev-biochem-061408-144611
  locator: Actual failed public source response; not scientific article content
  accessed_at: '2026-11-04T02:03:55.647883Z'
  support: context_only
  summary: HTTP403 body unavailable on this route; genuine alternatives for Miller/Albers
    were separately read. Elferink/Hagan2011 remain abstract-limited.
  snapshot_sha256: e043d63cf19f87dd170bbfe04a4171d9ba89c393363a09199275d6981172d9d6
- evidence_id: micro-access-wrong-article
  kind: validation
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3209348/
  locator: Attempted PMC route title-identity check only
  accessed_at: '2026-11-04T02:02:08.510919Z'
  support: context_only
  summary: Candidate route returned an unrelated herpesvirus article; identity mismatch
    detected immediately, excluded from all scientific support. No Hagan2011 body
    claim.
  snapshot_sha256: 44b7982cb404e3d7bb472fb7dc0fd3ce936bf8cbcd0c06af3a797572498cd640
- evidence_id: micro-catalogue
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Complete official organism/dataset catalogue; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/catalogue.raw
  accessed_at: '2026-11-04T02:01:13.129554Z'
  support: supports
  summary: Fresh catalogue covers E. coli; choose actual precise1k. It lists Sulfolobus
    acidocaldarius but not Saccharolobus/Sulfolobus solfataricus, so no unmatched
    archaeal proxy is used. Coverage is catalogue-specific, not biological absence.
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: micro-ecoli-meta
  kind: database
  reference: https://imodulondb.org/api/datasets/e_coli/precise1k/meta
  locator: Complete selected dataset metadata; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/ecoli-meta.raw
  accessed_at: '2026-11-04T02:01:13.641479Z'
  support: supports
  summary: precise1k comprises4257genes/201modules/1035samples/518conditions and BW25113,DGF-298,GMOS,MG1655,W3110.
    This mixed-strain dataset does not identify every HDB150/BL21/PBL2025 assay context.
  snapshot_sha256: 6cd60b3e363a11c95c2b5b1d160fe360687c0a680a5b95c18c6c76e7c5d99865
- evidence_id: micro-ecoli-genes
  kind: database
  reference: https://imodulondb.org/api/genes?organism=e_coli&dataset=precise1k&limit=10000
  locator: Complete4257-row gene inventory; exact selected locus/gene/UniProt joins;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/ecoli-genes.raw
  accessed_at: '2026-11-04T02:01:13.335311Z'
  support: supports
  summary: Current dnaA b3702, bamA b0177,bamB b2512,bamC b2477,bamD b2595,bamE b2617
    and external ompT b0565 are represented. Presence in expression data does not
    establish membership or necessity.
  snapshot_sha256: db4db81a724c8bee753c68fa5fefdd34f3d89e2cd101ae52311088f7cb094d27
- evidence_id: micro-ecoli-modules
  kind: database
  reference: https://imodulondb.org/api/datasets/e_coli/precise1k/imodulons
  locator: Complete201-row module metadata list, numeric keys and labels; exact retained
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/ecoli-modules.raw
  accessed_at: '2026-11-04T02:01:12.943022Z'
  support: supports
  summary: Module metadata checked independently of generated ai_summary; association
    is not assembly/catalysis/localization evidence.
  snapshot_sha256: c9f7564cc9fa212686b00f75d35b5438d9d8660066eada141b263e580634e26d
- evidence_id: micro-dataset-b3702
  kind: search
  reference: https://imodulondb.org/api/genes/b3702/imodulons?organism=e_coli&dataset=precise1k
  locator: Complete returned201-module table and actual flags/weights/thresholds;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/dataset-b3702.raw
  accessed_at: '2026-11-04T02:02:08.290817Z'
  support: supports
  summary: 'b3702: above-threshold entries []. No above-threshold result for dnaA/bamA–E
    is not gene absence or evidence against the structures.'
  snapshot_sha256: f88e8e1cc78f58e88b8e2e1bce66d3b576f85ac167c41cad5b4030aaf2f333fb
  search_scope: Official iModulonDB e_coli/precise1k exact geneb3702, 2026-11-04T02:02:08.290817Z;
    complete returned201-module table, all flags checked, no other dataset/strain
    inferred.
- evidence_id: micro-dataset-b0177
  kind: search
  reference: https://imodulondb.org/api/genes/b0177/imodulons?organism=e_coli&dataset=precise1k
  locator: Complete returned201-module table and actual flags/weights/thresholds;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/dataset-b0177.raw
  accessed_at: '2026-11-04T02:02:08.288913Z'
  support: supports
  summary: 'b0177: above-threshold entries []. No above-threshold result for dnaA/bamA–E
    is not gene absence or evidence against the structures.'
  snapshot_sha256: 0ded141a62e2f09a3ecca56a47a3decf250c49dbd83628b5fdcd35e8f887cc43
  search_scope: Official iModulonDB e_coli/precise1k exact geneb0177, 2026-11-04T02:02:08.288913Z;
    complete returned201-module table, all flags checked, no other dataset/strain
    inferred.
- evidence_id: micro-dataset-b2512
  kind: search
  reference: https://imodulondb.org/api/genes/b2512/imodulons?organism=e_coli&dataset=precise1k
  locator: Complete returned201-module table and actual flags/weights/thresholds;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/dataset-b2512.raw
  accessed_at: '2026-11-04T02:02:08.278407Z'
  support: supports
  summary: 'b2512: above-threshold entries []. No above-threshold result for dnaA/bamA–E
    is not gene absence or evidence against the structures.'
  snapshot_sha256: 6f993b53f27eb1c00b1fc026a61f04bc46a8d5e8e984010875c5841325601ac6
  search_scope: Official iModulonDB e_coli/precise1k exact geneb2512, 2026-11-04T02:02:08.278407Z;
    complete returned201-module table, all flags checked, no other dataset/strain
    inferred.
- evidence_id: micro-dataset-b2477
  kind: search
  reference: https://imodulondb.org/api/genes/b2477/imodulons?organism=e_coli&dataset=precise1k
  locator: Complete returned201-module table and actual flags/weights/thresholds;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/dataset-b2477.raw
  accessed_at: '2026-11-04T02:02:08.272761Z'
  support: supports
  summary: 'b2477: above-threshold entries []. No above-threshold result for dnaA/bamA–E
    is not gene absence or evidence against the structures.'
  snapshot_sha256: c67ed160f01bbba337106c0839cd723d71c0de0fead44eac7ff66848da5a7ab4
  search_scope: Official iModulonDB e_coli/precise1k exact geneb2477, 2026-11-04T02:02:08.272761Z;
    complete returned201-module table, all flags checked, no other dataset/strain
    inferred.
- evidence_id: micro-dataset-b2595
  kind: search
  reference: https://imodulondb.org/api/genes/b2595/imodulons?organism=e_coli&dataset=precise1k
  locator: Complete returned201-module table and actual flags/weights/thresholds;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/dataset-b2595.raw
  accessed_at: '2026-11-04T02:02:08.269370Z'
  support: supports
  summary: 'b2595: above-threshold entries []. No above-threshold result for dnaA/bamA–E
    is not gene absence or evidence against the structures.'
  snapshot_sha256: 0b23d934ed740db4e64644640d9c44c81806223ee805a4632d0625fb830f5da7
  search_scope: Official iModulonDB e_coli/precise1k exact geneb2595, 2026-11-04T02:02:08.269370Z;
    complete returned201-module table, all flags checked, no other dataset/strain
    inferred.
- evidence_id: micro-dataset-b2617
  kind: search
  reference: https://imodulondb.org/api/genes/b2617/imodulons?organism=e_coli&dataset=precise1k
  locator: Complete returned201-module table and actual flags/weights/thresholds;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/dataset-b2617.raw
  accessed_at: '2026-11-04T02:02:08.288966Z'
  support: supports
  summary: 'b2617: above-threshold entries []. No above-threshold result for dnaA/bamA–E
    is not gene absence or evidence against the structures.'
  snapshot_sha256: af0c3327dfa03d7341f56b02b5a77c3ac4c1a7b303052118f0474bf4ec9ef236
  search_scope: Official iModulonDB e_coli/precise1k exact geneb2617, 2026-11-04T02:02:08.288966Z;
    complete returned201-module table, all flags checked, no other dataset/strain
    inferred.
- evidence_id: micro-dataset-b0565
  kind: search
  reference: https://imodulondb.org/api/genes/b0565/imodulons?organism=e_coli&dataset=precise1k
  locator: Complete returned201-module table and actual flags/weights/thresholds;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/dataset-b0565.raw
  accessed_at: '2026-11-04T02:02:08.276194Z'
  support: supports
  summary: 'b0565: above-threshold entries [{''k'': 59, ''name'': ''Magnesium'', ''weight'':
    0.100658384, ''threshold'': 0.080711519}, {''k'': 164, ''name'': ''minicoli KOs'',
    ''weight'': 0.056150973, ''threshold'': 0.042504139}]. No above-threshold result
    for dnaA/bamA–E is not gene absence or evidence against the structures.'
  snapshot_sha256: 314f38369b47093fc7db360031a4446a790bb2a0ac45ae48a9378158337dbe9f
  search_scope: Official iModulonDB e_coli/precise1k exact geneb0565, 2026-11-04T02:02:08.276194Z;
    complete returned201-module table, all flags checked, no other dataset/strain
    inferred.
- evidence_id: micro-ecoli-module-59
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise1k/59
  locator: Full actual module gene list and metadata; exact b0565 weight/threshold
    join; generated ai_summary and condition activities not used; exact retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/ecoli-module-59.raw
  accessed_at: '2026-11-04T02:03:02.561011Z'
  support: supports
  summary: Magnesium/PhoP59:21genes, OmpT0.100658384 above0.080711519. This is regulatory
    context only, not proof of whole BAM coexpression, assembly or OmpT substrate
    processing.
  snapshot_sha256: 7917e7eba317a7937cbd6ab943f44d6d53501fae3bae0a76dac8e588ac9f9461
- evidence_id: micro-ecoli-module-164
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise1k/164
  locator: Full actual module gene list and metadata; exact b0565 weight/threshold
    join; generated ai_summary and condition activities not used; exact retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/adversary-microtubule/ecoli-module-164.raw
  accessed_at: '2026-11-04T02:03:02.572133Z'
  support: supports
  summary: minicoli KOs164:115genes, OmpT0.056150973 above0.042504139. This is regulatory
    context only, not proof of whole BAM coexpression, assembly or OmpT substrate
    processing.
  snapshot_sha256: ca37e499656c78bcf779969c5b203a3db7b266ce721bc52164157e482ad9876a
- evidence_id: micro-historical-runner
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical00:49Z retained adapter invocation receipt; not rerun
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  summary: Original optional runner was unavailable; fresh public official-source
    inspection supplies bounded applicability fallback. This is never counted as a
    current successful runner execution.
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: micro-native-bacterial_pre_replicative_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bacterial_pre_replicative_complex-uniprot-verify-receipt.json
  locator: Actual command receipt; full log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bacterial_pre_replicative_complex-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T01:59:50.357288Z'
  support: supports
  summary: Exit0; one reviewed example and one COVERED typed node. Generic verify
    success is not inventory count; diagnostics do not establish biological membership
    or absence. BAM external substrate/group nodes are allowed; partial TreS example
    coverage is not itself a missing-optional-example finding.
  snapshot_sha256: ec8729f59daa9349ab820a8e106a8f0635dc5871c0cb46f1c0948c0cefc88285
- evidence_id: micro-native-bacterial_pre_replicative_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bacterial_pre_replicative_complex-uniprot-causal-receipt.json
  locator: Actual command receipt; full log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bacterial_pre_replicative_complex-uniprot-causal.log
    SHA256 f6e0e6b4b913d39e9ca812634ab0e75f1ff2e46eaf6d2e468133dbd2600c1019
  accessed_at: '2026-11-04T01:59:50.845053Z'
  support: supports
  summary: Exit0; one reviewed example and one COVERED typed node. Generic verify
    success is not inventory count; diagnostics do not establish biological membership
    or absence. BAM external substrate/group nodes are allowed; partial TreS example
    coverage is not itself a missing-optional-example finding.
  snapshot_sha256: 1f668b2334b363be865de530f18c6deaa584da3834cb0d00d7c131bc1041d217
- evidence_id: micro-native-bam_protein_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bam_protein_complex-uniprot-verify-receipt.json
  locator: Actual command receipt; full log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bam_protein_complex-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T01:59:54.900733Z'
  support: supports
  summary: Exit0; five reviewed component examples, five COVERED nodes and three UNANCHORED_WITH_UNIPROT
    external-substrate/group nodes. Generic verify success is not inventory count;
    diagnostics do not establish biological membership or absence. BAM external substrate/group
    nodes are allowed; partial TreS example coverage is not itself a missing-optional-example
    finding.
  snapshot_sha256: afaadd5a4e23cd22b68cff46f8e1cf3625122456e382a8508d9f5fcd18e3f1bb
- evidence_id: micro-native-bam_protein_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bam_protein_complex-uniprot-causal-receipt.json
  locator: Actual command receipt; full log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bam_protein_complex-uniprot-causal.log
    SHA256 c608f801dda01017c8f577c48d37c00d5189329ec184e1edfaa0c608734353ac
  accessed_at: '2026-11-04T01:59:55.395830Z'
  support: supports
  summary: Exit0; five reviewed component examples, five COVERED nodes and three UNANCHORED_WITH_UNIPROT
    external-substrate/group nodes. Generic verify success is not inventory count;
    diagnostics do not establish biological membership or absence. BAM external substrate/group
    nodes are allowed; partial TreS example coverage is not itself a missing-optional-example
    finding.
  snapshot_sha256: 35ebf86088d244e52637ee6c7636b87c4616393a0b8a39846dfbf041662388d3
- evidence_id: micro-native-bindosome_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bindosome_complex-uniprot-verify-receipt.json
  locator: Actual command receipt; full log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bindosome_complex-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T01:59:58.979246Z'
  support: supports
  summary: Exit0; two examples (one reviewed GlcS, one unreviewed SSO3066/AraS) and
    one PARTIAL_EXAMPLES node missing treS. Generic verify success is not inventory
    count; diagnostics do not establish biological membership or absence. BAM external
    substrate/group nodes are allowed; partial TreS example coverage is not itself
    a missing-optional-example finding.
  snapshot_sha256: 979d4bb415e0e8e9dfef25ee146d2d0e54b8fc09849b3953943a3cbb018d5ba6
- evidence_id: micro-native-bindosome_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bindosome_complex-uniprot-causal-receipt.json
  locator: Actual command receipt; full log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bindosome_complex-uniprot-causal.log
    SHA256 c7712aeb5a9e9859a045011117f593a0b77378faa3ed724dcc110ecf06cbf0a6
  accessed_at: '2026-11-04T01:59:59.428131Z'
  support: supports
  summary: Exit0; two examples (one reviewed GlcS, one unreviewed SSO3066/AraS) and
    one PARTIAL_EXAMPLES node missing treS. Generic verify success is not inventory
    count; diagnostics do not establish biological membership or absence. BAM external
    substrate/group nodes are allowed; partial TreS example coverage is not itself
    a missing-optional-example finding.
  snapshot_sha256: 53bd656619fd7002d79bb999a393c382e3269f1d0eea1a54750f4740e4c270f4
- evidence_id: check-qc
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/qc.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T02:04:18.780395Z'
  support: supports
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  snapshot_sha256: 949aabfde558c95bb342864f35562018e43569c988fd809d44636fb5c15a31b6
- evidence_id: check-labels
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/labels.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T02:00:16.795538Z'
  support: supports
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  snapshot_sha256: 6cdfb05df9a27194f05a5fd7f851783f817ac1523ca0bbfa54fe0e0d18775905
- evidence_id: check-trait-links
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/trait-links.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T01:59:52.350790Z'
  support: supports
  summary: Native TraitMech link check passed.
  snapshot_sha256: 8b336cdefbbd3daf6da8787990efdbe346c95e2c8361d50b7eb68a18f2d5a44a
- evidence_id: check-vendored
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/vendored.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T01:59:46.200275Z'
  support: supports
  summary: Pinned governed files match; native vendored check passed.
  snapshot_sha256: b1f169d103aaefa930745468bcca171e5867b9cc49e4e74311e458097e3252a6
- evidence_id: check-curies
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/curies.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T01:59:46.564011Z'
  support: supports
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  snapshot_sha256: bc12b1285f5747707643f7a98e03dbb3a6c88fb062ad49f99db9cb42ececf3d2
- evidence_id: focused
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/focused-results.json
  locator: All twenty actual target schema/strict command outputs
  accessed_at: '2026-11-04T02:14:28Z'
  support: supports
  summary: Ten schema and ten strict commands returned exit zero.
  snapshot_sha256: 64e092ff8385b1e8f0cefed4094a152c0b506d7f497d522ce03b480191c8d5b3
- evidence_id: supplemental-pmid
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/pmid-chunks-receipt.json
  locator: Complete native-report PMID set checked with unchanged resolver in batches
    of at most fifty
  accessed_at: '2026-11-04T02:01:16.918146Z'
  support: supports
  summary: 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers
    remain unverified.
  snapshot_sha256: 4bfd7e1dd4e4248abfd8394e612ce7c967c077ce057ed4bc3eff7eca8b7faa8e
- evidence_id: historical-adapter-runner-availability
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical runner invocation receipt; exact retained SHA256 reverified
    during PR2382 synthesis
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  summary: Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS
    PermissionError reading the configured runner pyvenv.cfg. This is retained historical
    availability evidence, not a fresh attempt or a scientific validation failure.
    Native policy permits inspected source-catalogue fallback.
- evidence_id: root-native-ap_5_adaptor_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/ap_5_adaptor_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T01:59:45.098534Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-ap_5_adaptor_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/ap_5_adaptor_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T01:59:45.534281Z'
  support: context_only
  snapshot_sha256: 0ab5a9e877601b5e064d133c6e06c2d902f314b9c485fcf3447af02d79ff9db8
  summary: 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-ap_type_membrane_coat_adaptor_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/ap_type_membrane_coat_adaptor_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T01:59:45.981677Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 0 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-ap_type_membrane_coat_adaptor_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/ap_type_membrane_coat_adaptor_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T01:59:46.413581Z'
  support: context_only
  snapshot_sha256: cfd777d9caf821e4e33d605f5651778539cefa8b4ee9e7a290e14a7776b4b7cd
  summary: 0 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-apical_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/apical_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T01:59:46.866057Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-apical_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/apical_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T01:59:47.302524Z'
  support: context_only
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-bacterial_extracellular_vesicle-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bacterial_extracellular_vesicle-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T01:59:47.740332Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-bacterial_extracellular_vesicle-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bacterial_extracellular_vesicle-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T01:59:48.226289Z'
  support: context_only
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-bacterial_outer_membrane_vesicle-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bacterial_outer_membrane_vesicle-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T01:59:48.698445Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-bacterial_outer_membrane_vesicle-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bacterial_outer_membrane_vesicle-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T01:59:49.183136Z'
  support: context_only
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-bacterial_pre_replicative_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bacterial_pre_replicative_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T01:59:50.357288Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-bacterial_pre_replicative_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bacterial_pre_replicative_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T01:59:50.845053Z'
  support: context_only
  snapshot_sha256: f6e0e6b4b913d39e9ca812634ab0e75f1ff2e46eaf6d2e468133dbd2600c1019
  summary: 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-bam_protein_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bam_protein_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T01:59:54.900733Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 5 represented protein examples; 8 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-bam_protein_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bam_protein_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T01:59:55.395830Z'
  support: context_only
  snapshot_sha256: c608f801dda01017c8f577c48d37c00d5189329ec184e1edfaa0c608734353ac
  summary: 5 represented protein examples; 8 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-bindosome_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bindosome_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T01:59:58.979246Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 2 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-bindosome_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/bindosome_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T01:59:59.428131Z'
  support: context_only
  snapshot_sha256: c7712aeb5a9e9859a045011117f593a0b77378faa3ed724dcc110ecf06cbf0a6
  summary: 2 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-caf_1_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/caf_1_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T02:00:00.809878Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-caf_1_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/caf_1_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T02:00:01.236947Z'
  support: context_only
  snapshot_sha256: 7e39addd5c8162efa08ca6a788ad23af636459a2c7ddaaae5d6fcdbba13e0349
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-cbf3_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/cbf3_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T02:00:02.422686Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-cbf3_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2382/cbf3_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T02:00:02.842842Z'
  support: context_only
  snapshot_sha256: f028d171b3b55fd59304e552aebec98f3c543e05a312100bc617d82e1397131f
  summary: 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
assessments:
- assessment_id: septin-ap_5_adaptor_complex-identity
  area: identity
  topic: Exact structural identity and anatomical relations
  outcome: supported
  summary: Exact GO0044599 AP5 identity, parent GO0030119 and beta5/zeta/mu5/sigma5
    architecture are supported. Late-endosome association does not establish universal
    clathrin coating.
  target_ids:
  - GO:0044599
  evidence_ids:
  - septin-record-ap_5_adaptor_complex
  - septin-original-ap_5_adaptor_complex
  - septin-go
  - septin-hirst2011-meta
  - septin-hirst2011-xml
  - septin-pmid-20613862
  - septin-slabicki2010-xml
  - septin-tax9606
- assessment_id: septin-ap_5_adaptor_complex-grounding
  area: grounding
  topic: Family/class grounding semantics
  outcome: concern
  summary: Four exact AP5 family mappings are independently verified and remain improperly
    deferred as REVIEWED_LABEL_ONLY. This is not optional representative coverage
    or substitution of broad domains.
  target_ids:
  - GO:0044599
  evidence_ids:
  - septin-record-ap_5_adaptor_complex
  - septin-original-ap_5_adaptor_complex
  - septin-go
  - septin-hirst2011-meta
  - septin-hirst2011-xml
  - septin-pmid-20613862
  - septin-slabicki2010-xml
  - septin-tax9606
  - septin-curation-policy
  - septin-schema-policy
  - septin-ipr-IPR038741
  - septin-ipr-IPR028222
  - septin-ipr-IPR039591
  - septin-ipr-IPR029392
- assessment_id: septin-ap_5_adaptor_complex-evidence
  area: evidence
  topic: Source claims and actual access tiers
  outcome: supported
  summary: AP5 endosomal-sorting implication is supported by HeLa knockdown redistribution/morphology
    plus tagged localization/co-IP evidence. Precise cargo route, full coat mechanism
    and individual formation necessity remain unproven. All metadata and actual body
    read extents are separately recorded. Secondary review abstracts and unsuccessful
    body routes do not certify unread experimental details.
  target_ids:
  - GO:0044599
  evidence_ids:
  - septin-record-ap_5_adaptor_complex
  - septin-original-ap_5_adaptor_complex
  - septin-go
  - septin-hirst2011-meta
  - septin-hirst2011-xml
  - septin-pmid-20613862
  - septin-slabicki2010-xml
  - septin-tax9606
  - septin-literature-policy
- assessment_id: septin-ap_5_adaptor_complex-graph
  area: graph
  topic: Complete coarse functional graph
  outcome: supported
  summary: Current FUNCTION/NONMECHANISTIC graph is constitutional/functional, not
    a complete assembly cycle. AP5 endosomal-sorting implication is supported by HeLa
    knockdown redistribution/morphology plus tagged localization/co-IP evidence. Precise
    cargo route, full coat mechanism and individual formation necessity remain unproven.
  target_ids:
  - GO:0044599
  evidence_ids:
  - septin-record-ap_5_adaptor_complex
  - septin-original-ap_5_adaptor_complex
  - septin-go
  - septin-hirst2011-meta
  - septin-hirst2011-xml
  - septin-pmid-20613862
  - septin-slabicki2010-xml
  - septin-tax9606
  - septin-graph-policy
  - septin-schema-policy
- assessment_id: septin-ap_5_adaptor_complex-formation
  area: evidence
  topic: Formation versus function and membership
  outcome: supported
  summary: Constituent classes retain UNKNOWN formation essentiality. Protein membership,
    intervention effects on cargo/organelles or invasion, and localization do not
    by themselves prove every component universally necessary for structure formation.
  target_ids:
  - GO:0044599
  evidence_ids:
  - septin-record-ap_5_adaptor_complex
  - septin-original-ap_5_adaptor_complex
  - septin-go
  - septin-hirst2011-meta
  - septin-hirst2011-xml
  - septin-pmid-20613862
  - septin-slabicki2010-xml
  - septin-tax9606
  - septin-curation-policy
- assessment_id: septin-ap_5_adaptor_complex-taxon
  area: scope
  topic: Canonical organism, strain and distribution scope
  outcome: supported
  summary: Human species9606 canonical HeLa context and native human accessions are
    separated from assay hosts; COMMON is qualitative, not a population census.
  target_ids:
  - GO:0044599
  evidence_ids:
  - septin-record-ap_5_adaptor_complex
  - septin-original-ap_5_adaptor_complex
  - septin-go
  - septin-hirst2011-meta
  - septin-hirst2011-xml
  - septin-pmid-20613862
  - septin-slabicki2010-xml
  - septin-tax9606
- assessment_id: septin-ap_5_adaptor_complex-quantity
  area: quantity
  topic: Numerical scope
  outcome: supported
  summary: No current experimental physical-size measurement is asserted. Protein
    sequence lengths/masses and source assay timing remain scoped to their evidence;
    no broad stoichiometric or prevalence measurement is inferred.
  target_ids:
  - GO:0044599
  evidence_ids:
  - septin-record-ap_5_adaptor_complex
  - septin-original-ap_5_adaptor_complex
  - septin-go
  - septin-hirst2011-meta
  - septin-hirst2011-xml
  - septin-pmid-20613862
  - septin-slabicki2010-xml
  - septin-tax9606
- assessment_id: septin-ap_5_adaptor_complex-schema
  area: schema
  topic: Frozen inputs and deterministic original artifact
  outcome: supported
  summary: Actual native original validation/render exit0; derived Markdown exact
    and all historical inputs match. Current target unchanged from its frozen original
    input. These checks do not recertify historical global gates as fresh execution.
  target_ids:
  - GO:0044599
  evidence_ids:
  - septin-record-ap_5_adaptor_complex
  - septin-original-ap_5_adaptor_complex
  - septin-go
  - septin-hirst2011-meta
  - septin-hirst2011-xml
  - septin-pmid-20613862
  - septin-slabicki2010-xml
  - septin-tax9606
  - septin-original-validation
- assessment_id: septin-ap_5_adaptor_complex-coverage
  area: completeness
  topic: Native protein inventory and coverage limits
  outcome: supported
  summary: Four reviewed human examples and four COVERED typed core-subunit nodes;
    current exact queries return their intended primary genes. Native sequence/family
    identities and experimental localization scopes are verified separately. Neither
    empty optional coverage nor generic protein-class typing is a scientific defect
    by itself.
  target_ids:
  - GO:0044599
  evidence_ids:
  - septin-record-ap_5_adaptor_complex
  - septin-original-ap_5_adaptor_complex
  - septin-go
  - septin-hirst2011-meta
  - septin-hirst2011-xml
  - septin-pmid-20613862
  - septin-slabicki2010-xml
  - septin-tax9606
  - septin-native-ap_5_adaptor_complex-verify
  - septin-native-ap_5_adaptor_complex-causal
  - septin-protein-policy
  - septin-protein-Q2VPB7
  - septin-protein-O43299
  - septin-protein-Q9H0R1
  - septin-protein-Q9NUS5
  - septin-gene-AP5B1
  - septin-gene-AP5Z1
  - septin-gene-AP5M1
  - septin-gene-AP5S1
- assessment_id: septin-ap_5_adaptor_complex-history
  area: provenance
  topic: Historical discussion and current assertion scope
  outcome: supported
  summary: Dated rationale, retrieval events and curation history remain append-only.
    Current notes/prompts can be corrected in separate authorized curation, with appended
    clarification and events; no historical source observation is rewritten or guessed.
  target_ids:
  - GO:0044599
  evidence_ids:
  - septin-record-ap_5_adaptor_complex
  - septin-original-ap_5_adaptor_complex
  - septin-go
  - septin-hirst2011-meta
  - septin-hirst2011-xml
  - septin-pmid-20613862
  - septin-slabicki2010-xml
  - septin-tax9606
  - septin-curation-policy
- assessment_id: septin-ap_5_adaptor_complex-adapter
  area: evidence
  topic: Whole-record molecular-source applicability
  outcome: supported
  summary: Positive molecular subunits, cargo/maturation or protein secretion/invasion
    assertions trigger actual applicability. Fresh complete official catalogue has
    no matching native human/Tetrahymena/Toxoplasma/Apicomplexa dataset. Downstream
    queries are bounded not_applicable after host coverage assessment, not because
    expression claims are absent. Historical runner unavailability is separate from
    fresh catalogue/native-source fallback; unrelated assay organisms are not substituted.
  target_ids:
  - GO:0044599
  evidence_ids:
  - septin-record-ap_5_adaptor_complex
  - septin-original-ap_5_adaptor_complex
  - septin-go
  - septin-hirst2011-meta
  - septin-hirst2011-xml
  - septin-pmid-20613862
  - septin-slabicki2010-xml
  - septin-tax9606
  - septin-review-policy
  - septin-catalogue
  - septin-adapter-runner-historical
- assessment_id: septin-ap_5_adaptor_complex-verdict
  area: consistency
  topic: Current target verdict
  outcome: concern
  summary: 'Needs curation: one confirmed inherited minor finding, retaining positive
    qualified scientific assessments outside the precise grounding/gloss defect. No
    new finding or terminal disposition is invented.'
  target_ids:
  - GO:0044599
  evidence_ids:
  - septin-record-ap_5_adaptor_complex
  - septin-original-ap_5_adaptor_complex
  - septin-go
  - septin-hirst2011-meta
  - septin-hirst2011-xml
  - septin-pmid-20613862
  - septin-slabicki2010-xml
  - septin-tax9606
  - septin-ipr-IPR038741
  - septin-ipr-IPR028222
  - septin-ipr-IPR039591
  - septin-ipr-IPR029392
- assessment_id: septin-ap_type_membrane_coat_adaptor_complex-identity
  area: identity
  topic: Exact structural identity and anatomical relations
  outcome: supported
  summary: Exact GO0030119 generic identity, is_a GO0098796 membrane protein complex
    and part_of GO0030117 membrane coat preserve distinct relation types. Parent definition
    needs the separately identified subtype/mass qualification; two-large/mu/sigma
    architecture remains valid.
  target_ids:
  - GO:0030119
  evidence_ids:
  - septin-record-ap_type_membrane_coat_adaptor_complex
  - septin-original-ap_type_membrane_coat_adaptor_complex
  - septin-go
  - septin-kaur2017-meta
  - septin-kaur2017-xml
  - septin-tax5911
  - septin-hirst2011-meta
  - septin-hirst2011-xml
- assessment_id: septin-ap_type_membrane_coat_adaptor_complex-grounding
  area: grounding
  topic: Family/class grounding semantics
  outcome: supported
  summary: Generic AP subtype-spanning classes are not forced into partial AP1–3 families
    or unchecked LLM InterPro prose; exact pan-class coverage is not established by
    the bounded candidates.
  target_ids:
  - GO:0030119
  evidence_ids:
  - septin-record-ap_type_membrane_coat_adaptor_complex
  - septin-original-ap_type_membrane_coat_adaptor_complex
  - septin-go
  - septin-kaur2017-meta
  - septin-kaur2017-xml
  - septin-tax5911
  - septin-hirst2011-meta
  - septin-hirst2011-xml
  - septin-curation-policy
  - septin-schema-policy
  - septin-ipr-IPR001392
  - septin-ipr-IPR016635
  - septin-ipr-IPR050431
- assessment_id: septin-ap_type_membrane_coat_adaptor_complex-evidence
  area: evidence
  topic: Source claims and actual access tiers
  outcome: supported
  summary: AP-type class constitution and coat-linking description are supported as
    coarse generic scope. The Tetrahymena AP3 example establishes successful mature
    mucocyst maturation, not absence of all immature vesicles or stable mature-organelle
    membership. All metadata and actual body read extents are separately recorded.
    Secondary review abstracts and unsuccessful body routes do not certify unread
    experimental details.
  target_ids:
  - GO:0030119
  evidence_ids:
  - septin-record-ap_type_membrane_coat_adaptor_complex
  - septin-original-ap_type_membrane_coat_adaptor_complex
  - septin-go
  - septin-kaur2017-meta
  - septin-kaur2017-xml
  - septin-tax5911
  - septin-hirst2011-meta
  - septin-hirst2011-xml
  - septin-literature-policy
- assessment_id: septin-ap_type_membrane_coat_adaptor_complex-graph
  area: graph
  topic: Complete coarse functional graph
  outcome: supported
  summary: Current FUNCTION/NONMECHANISTIC graph is constitutional/functional, not
    a complete assembly cycle. AP-type class constitution and coat-linking description
    are supported as coarse generic scope. The Tetrahymena AP3 example establishes
    successful mature mucocyst maturation, not absence of all immature vesicles or
    stable mature-organelle membership.
  target_ids:
  - GO:0030119
  evidence_ids:
  - septin-record-ap_type_membrane_coat_adaptor_complex
  - septin-original-ap_type_membrane_coat_adaptor_complex
  - septin-go
  - septin-kaur2017-meta
  - septin-kaur2017-xml
  - septin-tax5911
  - septin-hirst2011-meta
  - septin-hirst2011-xml
  - septin-graph-policy
  - septin-schema-policy
- assessment_id: septin-ap_type_membrane_coat_adaptor_complex-formation
  area: evidence
  topic: Formation versus function and membership
  outcome: supported
  summary: Constituent classes retain UNKNOWN formation essentiality. Protein membership,
    intervention effects on cargo/organelles or invasion, and localization do not
    by themselves prove every component universally necessary for structure formation.
  target_ids:
  - GO:0030119
  evidence_ids:
  - septin-record-ap_type_membrane_coat_adaptor_complex
  - septin-original-ap_type_membrane_coat_adaptor_complex
  - septin-go
  - septin-kaur2017-meta
  - septin-kaur2017-xml
  - septin-tax5911
  - septin-hirst2011-meta
  - septin-hirst2011-xml
  - septin-curation-policy
- assessment_id: septin-ap_type_membrane_coat_adaptor_complex-taxon
  area: scope
  topic: Canonical organism, strain and distribution scope
  outcome: supported
  summary: Tetrahymena species5911 canonical scope and CU428.1 experimental background
    are distinct; the generic AP class is not limited to AP3 or this organism.
  target_ids:
  - GO:0030119
  evidence_ids:
  - septin-record-ap_type_membrane_coat_adaptor_complex
  - septin-original-ap_type_membrane_coat_adaptor_complex
  - septin-go
  - septin-kaur2017-meta
  - septin-kaur2017-xml
  - septin-tax5911
  - septin-hirst2011-meta
  - septin-hirst2011-xml
- assessment_id: septin-ap_type_membrane_coat_adaptor_complex-quantity
  area: quantity
  topic: Numerical scope
  outcome: concern
  summary: Generic exhaustive large-chain110–130kDa and sigma15–20kDa ranges fail
    AP5 counterexamples. Hirst predicts beta5~94kDa, and native canonical sequence
    masses independently show beta5~93.9kDa/zeta~88.6kDa/sigma5~22.5kDa. These are
    not assembled-complex experimental masses.
  target_ids:
  - GO:0030119
  evidence_ids:
  - septin-record-ap_type_membrane_coat_adaptor_complex
  - septin-original-ap_type_membrane_coat_adaptor_complex
  - septin-go
  - septin-kaur2017-meta
  - septin-kaur2017-xml
  - septin-tax5911
  - septin-hirst2011-meta
  - septin-hirst2011-xml
  - septin-protein-Q2VPB7
  - septin-protein-O43299
  - septin-protein-Q9NUS5
  - septin-record-ap_5_adaptor_complex
- assessment_id: septin-ap_type_membrane_coat_adaptor_complex-schema
  area: schema
  topic: Frozen inputs and deterministic original artifact
  outcome: supported
  summary: Actual native original validation/render exit0; derived Markdown exact
    and all historical inputs match. Current target unchanged from its frozen original
    input. These checks do not recertify historical global gates as fresh execution.
  target_ids:
  - GO:0030119
  evidence_ids:
  - septin-record-ap_type_membrane_coat_adaptor_complex
  - septin-original-ap_type_membrane_coat_adaptor_complex
  - septin-go
  - septin-kaur2017-meta
  - septin-kaur2017-xml
  - septin-tax5911
  - septin-hirst2011-meta
  - septin-hirst2011-xml
  - septin-original-validation
- assessment_id: septin-ap_type_membrane_coat_adaptor_complex-coverage
  area: completeness
  topic: Native protein inventory and coverage limits
  outcome: supported
  summary: Zero examples and three NO_GENE_SYMBOLS typed protein-class nodes. Passing
    accession diagnostics do not establish missing optional examples or test an unpopulated
    inventory. Neither empty optional coverage nor generic protein-class typing is
    a scientific defect by itself.
  target_ids:
  - GO:0030119
  evidence_ids:
  - septin-record-ap_type_membrane_coat_adaptor_complex
  - septin-original-ap_type_membrane_coat_adaptor_complex
  - septin-go
  - septin-kaur2017-meta
  - septin-kaur2017-xml
  - septin-tax5911
  - septin-hirst2011-meta
  - septin-hirst2011-xml
  - septin-native-ap_type_membrane_coat_adaptor_complex-verify
  - septin-native-ap_type_membrane_coat_adaptor_complex-causal
  - septin-protein-policy
- assessment_id: septin-ap_type_membrane_coat_adaptor_complex-history
  area: provenance
  topic: Historical discussion and current assertion scope
  outcome: supported
  summary: Dated rationale, retrieval events and curation history remain append-only.
    Current notes/prompts can be corrected in separate authorized curation, with appended
    clarification and events; no historical source observation is rewritten or guessed.
  target_ids:
  - GO:0030119
  evidence_ids:
  - septin-record-ap_type_membrane_coat_adaptor_complex
  - septin-original-ap_type_membrane_coat_adaptor_complex
  - septin-go
  - septin-kaur2017-meta
  - septin-kaur2017-xml
  - septin-tax5911
  - septin-hirst2011-meta
  - septin-hirst2011-xml
  - septin-curation-policy
- assessment_id: septin-ap_type_membrane_coat_adaptor_complex-adapter
  area: evidence
  topic: Whole-record molecular-source applicability
  outcome: supported
  summary: Positive molecular subunits, cargo/maturation or protein secretion/invasion
    assertions trigger actual applicability. Fresh complete official catalogue has
    no matching native human/Tetrahymena/Toxoplasma/Apicomplexa dataset. Downstream
    queries are bounded not_applicable after host coverage assessment, not because
    expression claims are absent. Historical runner unavailability is separate from
    fresh catalogue/native-source fallback; unrelated assay organisms are not substituted.
  target_ids:
  - GO:0030119
  evidence_ids:
  - septin-record-ap_type_membrane_coat_adaptor_complex
  - septin-original-ap_type_membrane_coat_adaptor_complex
  - septin-go
  - septin-kaur2017-meta
  - septin-kaur2017-xml
  - septin-tax5911
  - septin-hirst2011-meta
  - septin-hirst2011-xml
  - septin-review-policy
  - septin-catalogue
  - septin-adapter-runner-historical
- assessment_id: septin-ap_type_membrane_coat_adaptor_complex-verdict
  area: consistency
  topic: Current target verdict
  outcome: concern
  summary: 'Needs curation: one confirmed inherited minor finding, retaining positive
    qualified scientific assessments outside the precise grounding/gloss defect. No
    new finding or terminal disposition is invented.'
  target_ids:
  - GO:0030119
  evidence_ids:
  - septin-record-ap_type_membrane_coat_adaptor_complex
  - septin-original-ap_type_membrane_coat_adaptor_complex
  - septin-go
  - septin-kaur2017-meta
  - septin-kaur2017-xml
  - septin-tax5911
  - septin-hirst2011-meta
  - septin-hirst2011-xml
- assessment_id: septin-apical_complex-identity
  area: identity
  topic: Exact structural identity and anatomical relations
  outcome: supported
  summary: Exact GO0020007 composite anatomy and four named organelle/cytoskeletal
    parts are supported at coarse scope. Conoid presence varies by lineage/stage;
    named parts do not assert universal identical molecular inventory.
  target_ids:
  - GO:0020007
  evidence_ids:
  - septin-record-apical_complex
  - septin-original-apical_complex
  - septin-go
  - septin-hu2006-meta
  - septin-hu2006-xml
  - septin-ren2024-meta
  - septin-ren2024-xml
  - septin-pmid-9208224
  - septin-carruthers1997-pmc
  - septin-boothroyd2008-meta
  - septin-waller2024-meta
  - septin-tax5794
  - septin-tax5811
- assessment_id: septin-apical_complex-grounding
  area: grounding
  topic: Family/class grounding semantics
  outcome: supported
  summary: Two broad cytoskeletal/secretory classes are acknowledged heterogeneous
    and label-only; no exact shared family is inferred. Named anatomical identities
    and permitted classes remain distinct.
  target_ids:
  - GO:0020007
  evidence_ids:
  - septin-record-apical_complex
  - septin-original-apical_complex
  - septin-go
  - septin-hu2006-meta
  - septin-hu2006-xml
  - septin-ren2024-meta
  - septin-ren2024-xml
  - septin-pmid-9208224
  - septin-carruthers1997-pmc
  - septin-boothroyd2008-meta
  - septin-waller2024-meta
  - septin-tax5794
  - septin-tax5811
  - septin-curation-policy
  - septin-schema-policy
- assessment_id: septin-apical_complex-evidence
  area: evidence
  topic: Source claims and actual access tiers
  outcome: supported
  summary: Apical structure/invasion context is supported by partial cytoskeletal
    enrichment, APR perturbations and source-specific secretory sequence. Carruthers
    directly measures secretion order during RH/2F invasion of HFF; whole-apical coordination
    and moving-junction interpretation are not upgraded into a directly demonstrated
    cytoskeleton-to-secretion causal edge. All metadata and actual body read extents
    are separately recorded. Secondary review abstracts and unsuccessful body routes
    do not certify unread experimental details.
  target_ids:
  - GO:0020007
  evidence_ids:
  - septin-record-apical_complex
  - septin-original-apical_complex
  - septin-go
  - septin-hu2006-meta
  - septin-hu2006-xml
  - septin-ren2024-meta
  - septin-ren2024-xml
  - septin-pmid-9208224
  - septin-carruthers1997-pmc
  - septin-boothroyd2008-meta
  - septin-waller2024-meta
  - septin-tax5794
  - septin-tax5811
  - septin-literature-policy
- assessment_id: septin-apical_complex-graph
  area: graph
  topic: Complete coarse functional graph
  outcome: supported
  summary: Current FUNCTION/NONMECHANISTIC graph is constitutional/functional, not
    a complete assembly cycle. Apical structure/invasion context is supported by partial
    cytoskeletal enrichment, APR perturbations and source-specific secretory sequence.
    Carruthers directly measures secretion order during RH/2F invasion of HFF; whole-apical
    coordination and moving-junction interpretation are not upgraded into a directly
    demonstrated cytoskeleton-to-secretion causal edge.
  target_ids:
  - GO:0020007
  evidence_ids:
  - septin-record-apical_complex
  - septin-original-apical_complex
  - septin-go
  - septin-hu2006-meta
  - septin-hu2006-xml
  - septin-ren2024-meta
  - septin-ren2024-xml
  - septin-pmid-9208224
  - septin-carruthers1997-pmc
  - septin-boothroyd2008-meta
  - septin-waller2024-meta
  - septin-tax5794
  - septin-tax5811
  - septin-graph-policy
  - septin-schema-policy
- assessment_id: septin-apical_complex-formation
  area: evidence
  topic: Formation versus function and membership
  outcome: supported
  summary: Constituent classes retain UNKNOWN formation essentiality. Protein membership,
    intervention effects on cargo/organelles or invasion, and localization do not
    by themselves prove every component universally necessary for structure formation.
  target_ids:
  - GO:0020007
  evidence_ids:
  - septin-record-apical_complex
  - septin-original-apical_complex
  - septin-go
  - septin-hu2006-meta
  - septin-hu2006-xml
  - septin-ren2024-meta
  - septin-ren2024-xml
  - septin-pmid-9208224
  - septin-carruthers1997-pmc
  - septin-boothroyd2008-meta
  - septin-waller2024-meta
  - septin-tax5794
  - septin-tax5811
  - septin-curation-policy
- assessment_id: septin-apical_complex-taxon
  area: scope
  topic: Canonical organism, strain and distribution scope
  outcome: supported
  summary: Apicomplexa phylum5794 and Toxoplasma species5811 are distinguished from
    RH/RH-derived tachyzoite experimental backgrounds. COMMON and stage/lineage variation
    are qualitative comparative scope, not measured prevalence or universal inventory.
  target_ids:
  - GO:0020007
  evidence_ids:
  - septin-record-apical_complex
  - septin-original-apical_complex
  - septin-go
  - septin-hu2006-meta
  - septin-hu2006-xml
  - septin-ren2024-meta
  - septin-ren2024-xml
  - septin-pmid-9208224
  - septin-carruthers1997-pmc
  - septin-boothroyd2008-meta
  - septin-waller2024-meta
  - septin-tax5794
  - septin-tax5811
- assessment_id: septin-apical_complex-quantity
  area: quantity
  topic: Numerical scope
  outcome: supported
  summary: No current experimental physical-size measurement is asserted. Protein
    sequence lengths/masses and source assay timing remain scoped to their evidence;
    no broad stoichiometric or prevalence measurement is inferred.
  target_ids:
  - GO:0020007
  evidence_ids:
  - septin-record-apical_complex
  - septin-original-apical_complex
  - septin-go
  - septin-hu2006-meta
  - septin-hu2006-xml
  - septin-ren2024-meta
  - septin-ren2024-xml
  - septin-pmid-9208224
  - septin-carruthers1997-pmc
  - septin-boothroyd2008-meta
  - septin-waller2024-meta
  - septin-tax5794
  - septin-tax5811
- assessment_id: septin-apical_complex-schema
  area: schema
  topic: Frozen inputs and deterministic original artifact
  outcome: supported
  summary: Actual native original validation/render exit0; derived Markdown exact
    and all historical inputs match. Current target unchanged from its frozen original
    input. These checks do not recertify historical global gates as fresh execution.
  target_ids:
  - GO:0020007
  evidence_ids:
  - septin-record-apical_complex
  - septin-original-apical_complex
  - septin-go
  - septin-hu2006-meta
  - septin-hu2006-xml
  - septin-ren2024-meta
  - septin-ren2024-xml
  - septin-pmid-9208224
  - septin-carruthers1997-pmc
  - septin-boothroyd2008-meta
  - septin-waller2024-meta
  - septin-tax5794
  - septin-tax5811
  - septin-original-validation
- assessment_id: septin-apical_complex-coverage
  area: completeness
  topic: Native protein inventory and coverage limits
  outcome: supported
  summary: Zero protein examples and zero GENE_OR_PROTEIN typed graph nodes. The two
    broad constituent cohorts are permitted classes; native pass is empty protein-xref
    coverage and does not independently establish their biology. Neither empty optional
    coverage nor generic protein-class typing is a scientific defect by itself.
  target_ids:
  - GO:0020007
  evidence_ids:
  - septin-record-apical_complex
  - septin-original-apical_complex
  - septin-go
  - septin-hu2006-meta
  - septin-hu2006-xml
  - septin-ren2024-meta
  - septin-ren2024-xml
  - septin-pmid-9208224
  - septin-carruthers1997-pmc
  - septin-boothroyd2008-meta
  - septin-waller2024-meta
  - septin-tax5794
  - septin-tax5811
  - septin-native-apical_complex-verify
  - septin-native-apical_complex-causal
  - septin-protein-policy
- assessment_id: septin-apical_complex-history
  area: provenance
  topic: Historical discussion and current assertion scope
  outcome: supported
  summary: Dated rationale, retrieval events and curation history remain append-only.
    Current notes/prompts can be corrected in separate authorized curation, with appended
    clarification and events; no historical source observation is rewritten or guessed.
  target_ids:
  - GO:0020007
  evidence_ids:
  - septin-record-apical_complex
  - septin-original-apical_complex
  - septin-go
  - septin-hu2006-meta
  - septin-hu2006-xml
  - septin-ren2024-meta
  - septin-ren2024-xml
  - septin-pmid-9208224
  - septin-carruthers1997-pmc
  - septin-boothroyd2008-meta
  - septin-waller2024-meta
  - septin-tax5794
  - septin-tax5811
  - septin-curation-policy
- assessment_id: septin-apical_complex-adapter
  area: evidence
  topic: Whole-record molecular-source applicability
  outcome: supported
  summary: Positive molecular subunits, cargo/maturation or protein secretion/invasion
    assertions trigger actual applicability. Fresh complete official catalogue has
    no matching native human/Tetrahymena/Toxoplasma/Apicomplexa dataset. Downstream
    queries are bounded not_applicable after host coverage assessment, not because
    expression claims are absent. Historical runner unavailability is separate from
    fresh catalogue/native-source fallback; unrelated assay organisms are not substituted.
  target_ids:
  - GO:0020007
  evidence_ids:
  - septin-record-apical_complex
  - septin-original-apical_complex
  - septin-go
  - septin-hu2006-meta
  - septin-hu2006-xml
  - septin-ren2024-meta
  - septin-ren2024-xml
  - septin-pmid-9208224
  - septin-carruthers1997-pmc
  - septin-boothroyd2008-meta
  - septin-waller2024-meta
  - septin-tax5794
  - septin-tax5811
  - septin-review-policy
  - septin-catalogue
  - septin-adapter-runner-historical
- assessment_id: septin-apical_complex-verdict
  area: consistency
  topic: Current target verdict
  outcome: supported
  summary: 'Pass with limitations: no confirmed record defect. Current GO polar-ring
    definition tension, inaccessible secondary bodies, partial primary-body read extents,
    heterogeneous classes and taxon/necessity limits are explicit. No generic-family
    or optional-example issue is manufactured.'
  target_ids:
  - GO:0020007
  evidence_ids:
  - septin-record-apical_complex
  - septin-original-apical_complex
  - septin-go
  - septin-hu2006-meta
  - septin-hu2006-xml
  - septin-ren2024-meta
  - septin-ren2024-xml
  - septin-pmid-9208224
  - septin-carruthers1997-pmc
  - septin-boothroyd2008-meta
  - septin-waller2024-meta
  - septin-tax5794
  - septin-tax5811
- assessment_id: septin-apical_complex-polar-ring
  area: identity
  topic: Polar-ring term versus source anatomical distinction
  outcome: unknown
  summary: GO0020031 label/aliases denote apical/anterior polar ring, but definition
    describes anterior conoid-fiber origin, conflicting with Hu preconoidal-ring versus
    APR distinction and Ren three-layer APR. The record uses the correct named APR/coarse
    parthood without repeating that conflicting definition. No guessed replacement
    or confident identity refutation is warranted; exact ontology-definition alignment
    remains unresolved.
  target_ids:
  - GO:0020007
  evidence_ids:
  - septin-record-apical_complex
  - septin-original-apical_complex
  - septin-go
  - septin-hu2006-meta
  - septin-hu2006-xml
  - septin-ren2024-meta
  - septin-ren2024-xml
  - septin-pmid-9208224
  - septin-carruthers1997-pmc
  - septin-boothroyd2008-meta
  - septin-waller2024-meta
  - septin-tax5794
  - septin-tax5811
- assessment_id: plaque-t3-identity-origin
  area: identity
  topic: identity origin
  outcome: concern
  summary: GO0097691 and SL0489 are exact maintained authority identities, but their
    definition specifies plasma-membrane budding while current components/graph explicitly
    span outer-membrane/OIMV and Gram-positive routes. Retain inherited minor source-scope
    reconciliation; no assertion that the copied definition is fabricated.
  target_ids:
  - GO:0097691
  evidence_ids:
  - plaque-current-3
  - plaque-go
  - plaque-SL0489
  - plaque-toyofuku2019-meta
- assessment_id: plaque-t3-composition
  area: representation
  topic: composition
  outcome: supported
  summary: Composite membrane is honestly OTHER with mixed lipids/proteins and no
    guessed single chemical CURIE; variable heterogeneous cargo is OTHER/UNKNOWN.
    Membrane constitutional ESSENTIAL does not imply a specific protein biogenesis
    requirement.
  target_ids:
  - GO:0097691
  evidence_ids:
  - plaque-current-3
  - plaque-go
  - plaque-kim2015-meta
  - plaque-policy
- assessment_id: plaque-t3-taxon-canonical
  area: scope
  topic: taxon canonical
  outcome: supported
  summary: Bacteria VARIABLE is qualitative species/condition scope. S. aureus canonical
    example is supported by Lee2009 complete primary abstract reporting vesicles and90
    proteins; no exact strain, all cargo topology or molecular delivery mechanism
    is inferred from that abstract.
  target_ids:
  - GO:0097691
  evidence_ids:
  - plaque-current-3
  - plaque-tax-2
  - plaque-tax-1280
  - plaque-lee2009-meta
- assessment_id: plaque-t3-function-graph
  area: graph
  topic: function graph
  outcome: supported
  summary: The explicitly NON_MECHANISTIC cargo-carriage graph distinguishes inner/surface
    association from universal luminal enclosure and acknowledges multiple release
    routes. It does not assert all proteins/cargo occupy the same topology or specify
    one required assembly mechanism.
  target_ids:
  - GO:0097691
  evidence_ids:
  - plaque-current-3
  - plaque-kim2015-meta
  - plaque-toyofuku2019-meta
  - plaque-PMC5308417-jats
- assessment_id: plaque-t3-boundary-history
  area: consistency
  topic: boundary history
  outcome: supported
  summary: Broad bacterial extracellular vesicle is distinguished from generic microvesicle
    and narrow outer-membrane vesicle. Current typed mixed membrane and carries relation
    are evaluated directly; old issues663/664 are historical record context, not claimed
    newly resolved.
  target_ids:
  - GO:0097691
  evidence_ids:
  - plaque-current-3
  - plaque-current-4
  - plaque-go
  - plaque-SL0489
  - plaque-policy
- assessment_id: plaque-t4-identity-boundary
  area: identity
  topic: identity boundary
  outcome: supported
  summary: GO0061701 specifies Gram-negative outer-membrane-derived spherical proteolipid
    vesicles; broader GO1903561 parent and outer-membrane topology are coherent. Gram-positive
    cytoplasmic vesicles and OIMVs are explicitly distinguished rather than silently
    included.
  target_ids:
  - GO:0061701
  evidence_ids:
  - plaque-current-4
  - plaque-go
  - plaque-current-3
  - plaque-PMC5308417-jats
- assessment_id: plaque-t4-composite-type
  area: representation
  topic: composite type
  outcome: concern
  summary: 'Inherited F1 remains: the component label/notes/reference denote the entire
    mixed protein/LPS/phospholipid membrane while its type is LIPID. OTHER is available
    and used in the paired BEV record. This is bounded composite classification, not
    a false chemical grounding or wrong vesicle identity.'
  target_ids:
  - GO:0061701
  evidence_ids:
  - plaque-current-4
  - plaque-current-3
  - plaque-schema
  - plaque-PMC2893157-jats
- assessment_id: plaque-t4-canonical-source
  area: provenance
  topic: canonical source
  outcome: concern
  summary: 'Inherited F2 remains: the canonical note combines native OMV proteomes
    and inflammatory response under Park2010. Park body supports injection model and
    comparative Coomassie/LPS profiles, whereas Lee2007 complete abstract explicitly
    supplies141-protein global profiling. Keep these two source claims separated.'
  target_ids:
  - GO:0061701
  evidence_ids:
  - plaque-current-4
  - plaque-PMC2893157-jats
  - plaque-lee2007-meta
- assessment_id: plaque-t4-host-experimental-scope
  area: scope
  topic: host experimental scope
  outcome: supported
  summary: Park isolates intestinal E. coli from mouse CLP peritoneal fluid using16S
    identification and tests intraperitoneal purified OMV administration. These species-level
    evidence claims do not establish the precise1k K-12-related strains, natural infection
    equivalence or human clinical causation. Record species-level example remains
    supported within that scope.
  target_ids:
  - GO:0061701
  evidence_ids:
  - plaque-current-4
  - plaque-tax-562
  - plaque-PMC2893157-jats
  - plaque-ecoli-meta
- assessment_id: plaque-t4-graph-cargo-necessity
  area: graph
  topic: graph cargo necessity
  outcome: supported
  summary: Coarse NON_MECHANISTIC budding, bilayer enclosure and parthood are supported.
    The record does not claim all proteomic hits are luminal; heterogeneous cargo
    UNKNOWN is appropriate and membrane ESSENTIAL is constitutive. Empty optional
    protein examples are not a defect.
  target_ids:
  - GO:0061701
  evidence_ids:
  - plaque-current-4
  - plaque-PMC2893157-jats
  - plaque-PMC5308417-jats
  - plaque-policy
- assessment_id: plaque-t8-identity-composition
  area: identity
  topic: identity composition
  outcome: supported
  summary: GO0033186 conserved heterotrimer and yeast Cac1/p90,Cac2/p60,Msi1/Cac3/p50
    are supported by current authority and Kaufman primary purification/peptide-identification
    Results. Generic human p150/p60/p48/H3.1 definition is authority-scoped, not asserted
    as yeast subunit mass or histone variant.
  target_ids:
  - GO:0033186
  evidence_ids:
  - plaque-current-8
  - plaque-go
  - plaque-kaufman1997-pdf-download
- assessment_id: plaque-t8-family-grounding
  area: grounding
  topic: family grounding
  outcome: concern
  summary: 'Inherited caf1-cac2-family remains: full family IPR045145 exactly matches
    the Cac2 class and current Q04199 crossreference, making that active REVIEWED_LABEL_ONLY/TODO
    gap actionable. Do not substitute Cac1 partial domains or broader MSI1/RBAP paralog
    class for narrow classes.'
  target_ids:
  - GO:0033186
  evidence_ids:
  - plaque-current-8
  - plaque-policy
  - plaque-ipr-IPR045145
  - plaque-up-Q04199
  - plaque-ipr-IPR048800
  - plaque-ipr-IPR021644
  - plaque-ipr-IPR022043
  - plaque-ipr-IPR050459
- assessment_id: plaque-t8-native-identities
  area: nomenclature
  topic: native identities
  outcome: supported
  summary: 'All3 accessions are reviewed S288c entries with exact gene/locus tokens:
    Q12495 primary RLF2 aliasCAC1/YPR018W; Q04199 CAC2/YML102W; P13712 MSI1 aliasCAC3/YBR195C.
    Their S288c identity examples do not recast BJ926 purification or W303 genetics
    as experiments in that strain.'
  target_ids:
  - GO:0033186
  evidence_ids:
  - plaque-current-8
  - plaque-up-Q12495
  - plaque-up-Q04199
  - plaque-up-P13712
  - plaque-gene-CAC1
  - plaque-gene-CAC2
  - plaque-gene-MSI1
  - plaque-tax-559292
  - plaque-kaufman1997-pdf-download
- assessment_id: plaque-t8-location-evidence
  area: evidence
  topic: location evidence
  outcome: supported
  summary: P13712 cytoplasm annotation is correctly tied to PMID11238915 in the native
    entry and the Johnston abstract distinguishes its CAF-independent RAS function.
    Identity/localization evidence is separated from Kaufman CAF membership; no claim
    the full CAF complex is necessarily cytoplasmic.
  target_ids:
  - GO:0033186
  evidence_ids:
  - plaque-current-8
  - plaque-up-P13712
  - plaque-pmid-11238915
  - plaque-kaufman1997-pdf-download
- assessment_id: plaque-t8-graph-necessity
  area: graph
  topic: graph necessity
  outcome: supported
  summary: 'NON_MECHANISTIC membership→CAF-I→nucleosome assembly is supported by purified-complex
    replication-preferential SV40 assay. UNKNOWN formation necessity remains appropriate:
    cell viability and UV/telomeric-silencing mutant phenotypes do not directly establish
    whether every subunit is required for physical complex assembly.'
  target_ids:
  - GO:0033186
  evidence_ids:
  - plaque-current-8
  - plaque-kaufman1997-pdf-download
  - plaque-policy
- assessment_id: plaque-t8-taxon-boundary
  area: scope
  topic: taxon boundary
  outcome: supported
  summary: Saccharomyces canonical system and COMMON qualitative label are bounded
    to established study context, not a species-wide census. No lumping of adjacent
    chromatin remodelers or automatic resolution of unrelated histories is proposed.
  target_ids:
  - GO:0033186
  evidence_ids:
  - plaque-current-8
  - plaque-tax-4932
  - plaque-go
  - plaque-kaufman1997-pdf-download
- assessment_id: plaque-t9-identity-composition
  area: identity
  topic: identity composition
  outcome: supported
  summary: 'Current GO0031518 and primary structures support Ctf13,Skp1,Cep3,Ndc10
    protein classes in CBF3. Four classes do not mean four total monomers: the full
    structural preparation can contain Cep3 and Ndc10 dimers. Current record does
    not assert contrary stoichiometry.'
  target_ids:
  - GO:0031518
  evidence_ids:
  - plaque-current-9
  - plaque-go
  - plaque-PMC5771398-jats
  - plaque-PMC6292502-jats
- assessment_id: plaque-t9-family-grounding
  area: grounding
  topic: family grounding
  outcome: concern
  summary: Inherited cbf3-skp1-family remains. IPR016897 is full Skp1 and maps P52286.
    Requiring a family uniquely separating CBF3-specific Skp1 from its SCF/RAVE roles
    confuses class identity with role context. Wider IPR001232 and other subunit domains
    are not forced into exact classes.
  target_ids:
  - GO:0031518
  evidence_ids:
  - plaque-current-9
  - plaque-policy
  - plaque-up-P52286
  - plaque-ipr-IPR016897
  - plaque-ipr-IPR001232
  - plaque-ipr-IPR031760
  - plaque-ipr-IPR022210
  - plaque-ipr-IPR062588
  - plaque-ipr-IPR063542
- assessment_id: plaque-t9-native-identities
  area: nomenclature
  topic: native identities
  outcome: supported
  summary: 'All4 reviewed S288c accessions and loci are correct: P35203 CTF13/YMR094W,P52286
    SKP1/YDR328C,P40969 CEP3/YMR168C,P32504 primaryCBF2 aliasNDC10/YGR140W. The role
    explains native primary CBF2 while maintaining literature Ndc10; no arbitrary
    renaming is needed.'
  target_ids:
  - GO:0031518
  evidence_ids:
  - plaque-current-9
  - plaque-up-P35203
  - plaque-up-P52286
  - plaque-up-P40969
  - plaque-up-P32504
  - plaque-gene-CTF13
  - plaque-gene-SKP1
  - plaque-gene-CEP3
  - plaque-gene-NDC10
  - plaque-tax-559292
- assessment_id: plaque-t9-location-source-joins
  area: evidence
  topic: location source joins
  outcome: supported
  summary: Skp1 Huh2003 and Ndc10 Zeng1999 location references are checked against
    actual native SUBCELLULAR LOCATION annotations. Huh abstract alone is not a specific
    Skp1 image; Zeng Cbf2-GFP methods are a bounded control, not a wholesale reassignment
    of Slk19/Kar3 results to Ndc10.
  target_ids:
  - GO:0031518
  evidence_ids:
  - plaque-current-9
  - plaque-up-P52286
  - plaque-up-P32504
  - plaque-pmid-14562095
  - plaque-pmid-10427094
  - plaque-PMC3206577-jats
- assessment_id: plaque-t9-stale-delta
  area: graph
  topic: stale delta
  outcome: supported
  summary: 'Substantive stale refresh: Oct30 adds Ctf13→CBF3 and Skp1→CBF3 assembles_into
    edges and history. Leber body explicitly coexpresses full four-class complex,
    then separates Ndc10 and structures the Ctf13/Skp1/Cep3 core; Yan full CBF3–CEN3
    body corroborates Ndc10/Ctf13 interface. Thus both new membership edges are supported
    with core/full distinctions preserved. Inherited Skp1 grounding gap is unchanged
    by these graph repairs.'
  target_ids:
  - GO:0031518
  evidence_ids:
  - plaque-current-9
  - plaque-original-9-yaml
  - plaque-PMC5771398-jats
  - plaque-PMC6292502-jats
  - plaque-go
  - plaque-original-current-validation
- assessment_id: plaque-t9-function-necessity
  area: scope
  topic: function necessity
  outcome: supported
  summary: NON_MECHANISTIC centromeric DNA/kinetochore initiation graph is appropriately
    bounded. Yan Cse4 deposition is proposed and not promoted to directly observed
    complete mechanism. UNKNOWN formation necessity is not invalidated by selected
    interface mutations, essential viability or purification alone.
  target_ids:
  - GO:0031518
  evidence_ids:
  - plaque-current-9
  - plaque-PMC5771398-jats
  - plaque-PMC6292502-jats
  - plaque-policy
- assessment_id: plaque-t3-native-validation
  area: schema
  topic: native validation
  outcome: supported
  summary: Current native verify/causal receipts both exit0. Independently counted
    0 examples/0 GENE_OR_PROTEIN nodes, all reviewed/COVERED when nonempty. Four original
    YAML/Markdown pairs validate/render exactly;55 historical input occurrences match
    their original sources. No repository mutation was performed.
  target_ids:
  - GO:0097691
  evidence_ids:
  - plaque-original-current-validation
  - plaque-native-bacterial_extracellular_vesicle-verify
  - plaque-native-bacterial_extracellular_vesicle-causal
  - plaque-review-schema
- assessment_id: plaque-t3-completeness-images
  area: completeness
  topic: completeness images
  outcome: supported
  summary: Entire maintained record reviewed. No current image entry or separately
    curated physical-property measurement is present; definitional size language remains
    within the authority/source scope. No invented image/measurement obligation is
    imposed. Source text captions were used only within declared access tiers; no
    figure-pixel inspection is claimed. Existing source-neutral unresolved classes
    and generic cargo are not forced into unsupported exact identifiers.
  target_ids:
  - GO:0097691
  evidence_ids:
  - plaque-current-3
  - plaque-policy
- assessment_id: plaque-t3-structured-sources
  area: evidence
  topic: structured sources
  outcome: supported
  summary: Positive molecular cargo-delivery/export and proteomic canonical narratives
    trigger the native adapter applicability assessment despite no named protein examples.
    The original prose exclusion expressly dismisses vesicle carriage and is unsupported.
    Fresh complete catalogue plus S. aureus108/165 and E. coli precise1k strain/annotation
    checks were performed; no yeast proxy or unverified experimental-strain match.
    Literal vesicle/cargo nonhits are not biological absence; selected OmpF expression
    contexts and OmpA below-threshold status do not prove OMV cargo.
  target_ids:
  - GO:0097691
  evidence_ids:
  - plaque-current-3
  - plaque-original-3-yaml
  - plaque-review-skill
  - plaque-catalogue
  - plaque-ecoli-meta
  - plaque-adapter-sa-staph_precise108-meta
  - plaque-adapter-sa-staph_precise165-meta
  - plaque-adapter-bounded-search
  - plaque-adapter-ecoli-b0957-modules
  - plaque-adapter-ecoli-b0929-modules
  - plaque-adapter-ecoli-module-22
  - plaque-adapter-ecoli-module-25
  - plaque-adapter-ecoli-module-86
  - plaque-adapter-ecoli-module-88
- assessment_id: plaque-t3-verdict-lineage
  area: provenance
  topic: verdict lineage
  outcome: concern
  summary: Current verdict remains needs_curation for the independently confirmed
    inherited minor finding(s). Exact predecessor identity is preserved; no original
    finding is silently dropped, no historical record repair is claimed as this PR
    work, and record curation remains outside this review-only branch.
  target_ids:
  - GO:0097691
  evidence_ids:
  - plaque-current-3
  - plaque-original-3-yaml
  - plaque-original-current-validation
- assessment_id: plaque-t4-native-validation
  area: schema
  topic: native validation
  outcome: supported
  summary: Current native verify/causal receipts both exit0. Independently counted
    0 examples/0 GENE_OR_PROTEIN nodes, all reviewed/COVERED when nonempty. Four original
    YAML/Markdown pairs validate/render exactly;55 historical input occurrences match
    their original sources. No repository mutation was performed.
  target_ids:
  - GO:0061701
  evidence_ids:
  - plaque-original-current-validation
  - plaque-native-bacterial_outer_membrane_vesicle-verify
  - plaque-native-bacterial_outer_membrane_vesicle-causal
  - plaque-review-schema
- assessment_id: plaque-t4-completeness-images
  area: completeness
  topic: completeness images
  outcome: supported
  summary: Entire maintained record reviewed. No current image entry or separately
    curated physical-property measurement is present; definitional size language remains
    within the authority/source scope. No invented image/measurement obligation is
    imposed. Source text captions were used only within declared access tiers; no
    figure-pixel inspection is claimed. Existing source-neutral unresolved classes
    and generic cargo are not forced into unsupported exact identifiers.
  target_ids:
  - GO:0061701
  evidence_ids:
  - plaque-current-4
  - plaque-policy
- assessment_id: plaque-t4-structured-sources
  area: evidence
  topic: structured sources
  outcome: supported
  summary: Positive molecular cargo-delivery/export and proteomic canonical narratives
    trigger the native adapter applicability assessment despite no named protein examples.
    The original prose exclusion expressly dismisses vesicle carriage and is unsupported.
    Fresh complete catalogue plus S. aureus108/165 and E. coli precise1k strain/annotation
    checks were performed; no yeast proxy or unverified experimental-strain match.
    Literal vesicle/cargo nonhits are not biological absence; selected OmpF expression
    contexts and OmpA below-threshold status do not prove OMV cargo.
  target_ids:
  - GO:0061701
  evidence_ids:
  - plaque-current-4
  - plaque-original-4-yaml
  - plaque-review-skill
  - plaque-catalogue
  - plaque-ecoli-meta
  - plaque-adapter-sa-staph_precise108-meta
  - plaque-adapter-sa-staph_precise165-meta
  - plaque-adapter-bounded-search
  - plaque-adapter-ecoli-b0957-modules
  - plaque-adapter-ecoli-b0929-modules
  - plaque-adapter-ecoli-module-22
  - plaque-adapter-ecoli-module-25
  - plaque-adapter-ecoli-module-86
  - plaque-adapter-ecoli-module-88
- assessment_id: plaque-t4-verdict-lineage
  area: provenance
  topic: verdict lineage
  outcome: concern
  summary: Current verdict remains needs_curation for the independently confirmed
    inherited minor finding(s). Exact predecessor identity is preserved; no original
    finding is silently dropped, no historical record repair is claimed as this PR
    work, and record curation remains outside this review-only branch.
  target_ids:
  - GO:0061701
  evidence_ids:
  - plaque-current-4
  - plaque-original-4-yaml
  - plaque-original-current-validation
- assessment_id: plaque-t8-native-validation
  area: schema
  topic: native validation
  outcome: supported
  summary: Current native verify/causal receipts both exit0. Independently counted
    3 examples/3 GENE_OR_PROTEIN nodes, all reviewed/COVERED when nonempty. Four original
    YAML/Markdown pairs validate/render exactly;55 historical input occurrences match
    their original sources. No repository mutation was performed.
  target_ids:
  - GO:0033186
  evidence_ids:
  - plaque-original-current-validation
  - plaque-native-caf_1_complex-verify
  - plaque-native-caf_1_complex-causal
  - plaque-review-schema
- assessment_id: plaque-t8-completeness-images
  area: completeness
  topic: completeness images
  outcome: supported
  summary: Entire maintained record reviewed. No current image entry or separately
    curated physical-property measurement is present; definitional size language remains
    within the authority/source scope. No invented image/measurement obligation is
    imposed. Source text captions were used only within declared access tiers; no
    figure-pixel inspection is claimed. Existing source-neutral unresolved classes
    and generic cargo are not forced into unsupported exact identifiers.
  target_ids:
  - GO:0033186
  evidence_ids:
  - plaque-current-8
  - plaque-policy
- assessment_id: plaque-t8-structured-sources
  area: evidence
  topic: structured sources
  outcome: supported
  summary: Named yeast genes/proteins and assembly/function pathways trigger an actual
    applicability assessment; the original formal no-expression-claim exemption is
    insufficient. Complete current official catalogue has no Saccharomyces dataset,
    so no organism-matched downstream module query applies. This scoped source result
    is not absence of the structure, pathway or gene.
  target_ids:
  - GO:0033186
  evidence_ids:
  - plaque-current-8
  - plaque-original-8-yaml
  - plaque-review-skill
  - plaque-catalogue
  - plaque-tax-4932
  - plaque-tax-559292
- assessment_id: plaque-t8-verdict-lineage
  area: provenance
  topic: verdict lineage
  outcome: concern
  summary: Current verdict remains needs_curation for the independently confirmed
    inherited minor finding(s). Exact predecessor identity is preserved; no original
    finding is silently dropped, no historical record repair is claimed as this PR
    work, and record curation remains outside this review-only branch.
  target_ids:
  - GO:0033186
  evidence_ids:
  - plaque-current-8
  - plaque-original-8-yaml
  - plaque-original-current-validation
- assessment_id: plaque-t9-native-validation
  area: schema
  topic: native validation
  outcome: supported
  summary: Current native verify/causal receipts both exit0. Independently counted
    4 examples/4 GENE_OR_PROTEIN nodes, all reviewed/COVERED when nonempty. Four original
    YAML/Markdown pairs validate/render exactly;55 historical input occurrences match
    their original sources. No repository mutation was performed.
  target_ids:
  - GO:0031518
  evidence_ids:
  - plaque-original-current-validation
  - plaque-native-cbf3_complex-verify
  - plaque-native-cbf3_complex-causal
  - plaque-review-schema
- assessment_id: plaque-t9-completeness-images
  area: completeness
  topic: completeness images
  outcome: supported
  summary: Entire maintained record reviewed. No current image entry or separately
    curated physical-property measurement is present; definitional size language remains
    within the authority/source scope. No invented image/measurement obligation is
    imposed. Source text captions were used only within declared access tiers; no
    figure-pixel inspection is claimed. Existing source-neutral unresolved classes
    and generic cargo are not forced into unsupported exact identifiers.
  target_ids:
  - GO:0031518
  evidence_ids:
  - plaque-current-9
  - plaque-policy
- assessment_id: plaque-t9-structured-sources
  area: evidence
  topic: structured sources
  outcome: supported
  summary: Named yeast genes/proteins and assembly/function pathways trigger an actual
    applicability assessment; the original formal no-expression-claim exemption is
    insufficient. Complete current official catalogue has no Saccharomyces dataset,
    so no organism-matched downstream module query applies. This scoped source result
    is not absence of the structure, pathway or gene.
  target_ids:
  - GO:0031518
  evidence_ids:
  - plaque-current-9
  - plaque-original-9-yaml
  - plaque-review-skill
  - plaque-catalogue
  - plaque-tax-4932
  - plaque-tax-559292
- assessment_id: plaque-t9-verdict-lineage
  area: provenance
  topic: verdict lineage
  outcome: concern
  summary: Current verdict remains needs_curation for the independently confirmed
    inherited minor finding(s). Exact predecessor identity is preserved; no original
    finding is silently dropped, no historical record repair is claimed as this PR
    work, and record curation remains outside this review-only branch.
  target_ids:
  - GO:0031518
  evidence_ids:
  - plaque-current-9
  - plaque-original-9-yaml
  - plaque-original-current-validation
- assessment_id: micro-prerc-identity
  area: identity
  topic: Generic bacterial pre-RC and restricted substates
  outcome: supported
  summary: Active GO0036389 and is-a pre-replicative/protein-DNA ancestry agree. The
    source distinguishes persistent high-affinity ORC from higher-order DnaA loading;
    current generic record does not silently identify every DiaA/HU/helicase substate
    as obligatory part.
  target_ids:
  - GO:0036389
  evidence_ids:
  - micro-record-0
  - micro-go-0036389
  - micro-go-0036389-is_a
  - micro-go-1990101
  - micro-go-1990102
  - micro-go-1990103
  - micro-go-1990100
  - micro-miller2009-legacy
  - micro-leonard2010-body
- assessment_id: micro-prerc-family
  area: grounding
  topic: Exact DnaA family versus broader DnaA/Hda
  outcome: concern
  summary: Current IPR001957 is the DnaA family and matches P03004. IPR020591 also
    includes Hda and is broader. This independently confirms the inherited minor actionable
    DnaA grounding gap; no exact SO term is invented for oriC and no historical search
    is called dishonest.
  target_ids:
  - GO:0036389
  evidence_ids:
  - micro-record-0
  - micro-ipr-IPR001957
  - micro-ipr-IPR020591
  - micro-up-P03004
  - micro-policy
- assessment_id: micro-prerc-example
  area: grounding
  topic: Native DnaA identity and annotation joins
  outcome: supported
  summary: P03004 reviewed dnaA/b3702 K-12 identity and exact name match. Regev2012,
    Schenk2017 and Garner1998 abstract scopes plus native annotation joins support
    the recorded source associations; E. coli/BL21 and Bacillus substudies are not
    silently treated as identical K-12 pre-RC experiments.
  target_ids:
  - GO:0036389
  evidence_ids:
  - micro-record-0
  - micro-up-P03004
  - micro-query-dnaA
  - micro-tax-83333
  - micro-pmid-22574163
  - micro-pmid-28166228
  - micro-pmid-9478970
- assessment_id: micro-prerc-function
  area: evidence
  topic: Origin recognition and replication initiation
  outcome: supported
  summary: Miller site substitutions, oligomerization mutant, footprints and binding
    assays support DnaA/oriC assembly and initiation competence. Licensing is generic
    biological language here; no eukaryotic licensing apparatus or sufficiency of
    binding for completed replication is asserted.
  target_ids:
  - GO:0036389
  evidence_ids:
  - micro-record-0
  - micro-miller2009-legacy
  - micro-go-0006270
  - micro-leonard2010-body
- assessment_id: micro-prerc-graph
  area: graph
  topic: Three coarse assembly/function edges
  outcome: supported
  summary: DnaA contributes, oriC scaffolds and the complex supports initiation. NONMECHANISTIC
    scope deliberately withholds lower-affinity loading dynamics, atomic oligomer
    details and later helicase transfer; the available primary source supports these
    bounded relations.
  target_ids:
  - GO:0036389
  evidence_ids:
  - micro-record-0
  - micro-graph-policy
  - micro-miller2009-legacy
  - micro-go-0036389
- assessment_id: micro-prerc-necessity
  area: grounding
  topic: Formation necessity and defined constituents
  outcome: unknown
  summary: DnaA/oriC constitute the named complex and site/oligomerization experiments
    affect assembly. UNKNOWN flags are conservative; this review does not convert
    cell viability or individual site defects into a universal formation assay, nor
    demand optional depletion experiments.
  target_ids:
  - GO:0036389
  evidence_ids:
  - micro-record-0
  - micro-miller2009-legacy
  - micro-policy
- assessment_id: micro-prerc-taxa
  area: scope
  topic: Canonical E. coli versus assay and module strains
  outcome: supported
  summary: Species562/K-12 identity and E. coli source system agree. COMMON remains
    qualitative ordinary initiation machinery, not a new prevalence census. W3110
    is present in the selected dataset, but pooled five-strain module context is not
    the exact PC2/polA assay condition.
  target_ids:
  - GO:0036389
  evidence_ids:
  - micro-record-0
  - micro-tax-562
  - micro-tax-83333
  - micro-miller2009-legacy
  - micro-ecoli-meta
- assessment_id: micro-bam-identity
  area: identity
  topic: Exact BAM complex and outer-membrane boundary
  outcome: supported
  summary: GO1990063 and primary sources denote bacterial BamABCDE assembly machinery,
    distinct from its external substrates or chaperones. GO0106234 biological broader
    class is supported by definition even though current is-a-only ancestry lacks
    that exact term; part_of outer membrane has native support.
  target_ids:
  - GO:1990063
  evidence_ids:
  - micro-record-1
  - micro-go-1990063
  - micro-go-0106234
  - micro-go-1990063-is_a
  - micro-go-1990063-part_of
  - micro-hagan2010-body
- assessment_id: micro-bam-families
  area: grounding
  topic: Five exact constituent families and examples
  outcome: supported
  summary: BamA–E respective IPR023707/017687/014524/017689/026592 are full named
    families, each joined to the verified reviewed K-12 example. New family-grounded
    nodes correctly propagate those identities and component_refs. Generic BamB–E
    grouped actor is permitted, not falsely a new obligatory protein family.
  target_ids:
  - GO:1990063
  evidence_ids:
  - micro-record-1
  - micro-ipr-IPR023707
  - micro-ipr-IPR017687
  - micro-ipr-IPR014524
  - micro-ipr-IPR017689
  - micro-ipr-IPR026592
  - micro-up-P0A940
  - micro-up-P77774
  - micro-up-P0A903
  - micro-up-P0AC02
  - micro-up-P0A937
  - micro-graph-policy
- assessment_id: micro-bam-substrate
  area: grounding
  topic: OmpT external substrate and product exemplars
  outcome: supported
  summary: P09169 reviewed K-12 ompT/Protease7 is the correct protein identity. Hagan
    directly reconstitutes OmpT folding/insertion; the two actor xrefs give a concrete
    example and do not promote OmpT to a BAM constituent. Reference K-12 identity
    is kept distinct from expression hosts and the Hagan supplementary cloning details
    not read here.
  target_ids:
  - GO:1990063
  evidence_ids:
  - micro-record-1
  - micro-delta-1
  - micro-up-P09169
  - micro-query-ompT
  - micro-hagan2010-body
  - micro-graph-policy
- assessment_id: micro-bam-stale-edges
  area: graph
  topic: Four newly explicit lipoprotein parthood edges
  outcome: supported
  summary: Each new B/C/D/E node is a member of the group BamB–E actor, not a separately
    asserted stable four-protein isolated complex. Gu text supports BamB–POTRA2/3,
    BamC–BamD and BamE bridging BamD/POTRA4/5; Iadanza supports BamD/POTRA interactions.
    Parthood and source-grounded organization remain bounded; BamD essential wording
    concerns known bacterial function and is not imported into formal UNKNOWN formation
    flags.
  target_ids:
  - GO:1990063
  evidence_ids:
  - micro-record-1
  - micro-delta-1
  - micro-gu2016-author
  - micro-iadanza2016-body
  - micro-bakelar2016-body
  - micro-policy
- assessment_id: micro-bam-function
  area: evidence
  topic: Reconstituted beta-barrel assembly
  outcome: supported
  summary: Hagan supports purified BAM+SurA OmpT folding/insertion with LPS assay
    requirement, heat-modifiability and membrane integration readouts. This does not
    establish an ATP-driven mechanism or universal atomic sequence; current function
    is appropriately broad.
  target_ids:
  - GO:1990063
  evidence_ids:
  - micro-record-1
  - micro-hagan2010-body
  - micro-hagan2011-meta
  - micro-iadanza2016-body
- assessment_id: micro-bam-conformation
  area: graph
  topic: Nonmechanistic state sampling retains distinct preparations
  outcome: supported
  summary: Gu captures intact inward-open and four-subunit lateral-open structures,
    Bakelar resolves BamACDE plus a modeled BamB, and Iadanza observes intact laterally
    open BAM. The record uses Iadanza for intact lateral opening and does not require
    every Gu state to contain all five subunits. Detergent/structural snapshots do
    not prove every catalytic transition.
  target_ids:
  - GO:1990063
  evidence_ids:
  - micro-record-1
  - micro-gu2016-author
  - micro-bakelar2016-body
  - micro-iadanza2016-body
- assessment_id: micro-bam-mass
  area: quantity
  topic: Approximate203kDa source-specific mass
  outcome: supported
  summary: Iadanza native MS predominant203456±22Da agrees with approximate203kDa.
    Minor extra-BamE and reconstitution/detergent context prevent treating this as
    invariant across all bacteria. Units are exact kilodalton.
  target_ids:
  - GO:1990063
  evidence_ids:
  - micro-record-1
  - micro-iadanza2016-body
  - micro-uo-0000222
- assessment_id: micro-bam-necessity
  area: grounding
  topic: Formation, viability and folding efficiency are distinct
  outcome: unknown
  summary: All components retain UNKNOWN formation necessity. Essential BamA/D viability,
    nonessential B/C/E and maximum OmpT activity with all five do not independently
    settle every assembly condition or lineage. No optional depletion experiment is
    demanded and SurA remains upstream machinery, not a forced constituent.
  target_ids:
  - GO:1990063
  evidence_ids:
  - micro-record-1
  - micro-hagan2010-body
  - micro-iadanza2016-body
  - micro-policy
- assessment_id: micro-bam-taxonomy
  area: scope
  topic: Diderm distribution and recombinant systems
  outcome: supported
  summary: Bacteria VARIABLE and explicit diderm/monoderm scope are compatible with
    the secondary overview and primary E. coli systems. BL21(DE3), HDB150 and DH5alpha
    contexts are distinct from reference K-12 annotations. No bacterial prevalence
    census or exact single-strain dataset equivalence is claimed.
  target_ids:
  - GO:1990063
  evidence_ids:
  - micro-record-1
  - micro-hagan2011-meta
  - micro-tax-2
  - micro-tax-562
  - micro-tax-83333
  - micro-gu2016-author
  - micro-iadanza2016-body
  - micro-bakelar2016-body
- assessment_id: micro-bindosome-identity
  area: identity
  topic: Surface sugar-binding assembly and Bas boundary
  outcome: supported
  summary: GO7770042 and parentGO0098796 agree with the mature surface sugar-binding
    assembly. Current Saccharolobus solfataricus identity accommodates historical
    Sulfolobus nomenclature. BasEF/ABC function in organization and uptake is not
    automatically mature400/600kDa constituent membership.
  target_ids:
  - GO:7770042
  evidence_ids:
  - micro-record-2
  - micro-go-7770042
  - micro-go-7770042-is_a
  - micro-tax-2287
  - micro-tax-273057
  - micro-zolghadr2011-body
- assessment_id: micro-bindosome-cohort
  area: grounding
  topic: Mixed class and exact available family limits
  outcome: supported
  summary: Generic sugar-binding PROTEIN class is permitted; GlcS/AraS and uncertain
    SSO3043/1273 roles remain qualified. Native GlcS-like and broad solute-binding
    families do not establish an exact combined GlcS/AraS/TreS whole-class grounding;
    their LLM descriptions are not primary membership evidence. SlaA copurification
    remains an explicit boundary question.
  target_ids:
  - GO:7770042
  evidence_ids:
  - micro-record-2
  - micro-policy
  - micro-zolghadr2011-body
  - micro-ipr-IPR054925
  - micro-ipr-IPR050490
- assessment_id: micro-bindosome-stale-aras
  area: grounding
  topic: New unreviewed AraS/SSO3066 exemplar
  outcome: supported
  summary: Native Q97UF5 is UNREVIEWED, ordered locusSSO3066, exact arabinose-binding
    product and P2tax273057. Albers2003 Table2 directly maps SSO3066 to AraS, so alias-query0
    does not undermine the disclosed literature-to-locus mapping. The example remains
    identity-only; current2011 paper independently names AraS. No false reviewed status
    or exact native geneName assertion is inferred.
  target_ids:
  - GO:7770042
  evidence_ids:
  - micro-record-2
  - micro-delta-2
  - micro-up-Q97UF5
  - micro-query-SSO3066
  - micro-query-araS
  - micro-albers2003-legacy
  - micro-zolghadr2011-body
- assessment_id: micro-bindosome-glcs
  area: grounding
  topic: Reviewed GlcS reference
  outcome: supported
  summary: Q97UZ1 is reviewed glcS/SSO2847 in P2 and the exact reviewed query returns
    that accession. Identity is separate from source-backed binding-protein assembly;
    current native cross-references alone do not prove membership.
  target_ids:
  - GO:7770042
  evidence_ids:
  - micro-record-2
  - micro-up-Q97UZ1
  - micro-query-glcS
  - micro-tax-273057
  - micro-zolghadr2011-body
- assessment_id: micro-bindosome-tres
  area: evidence
  topic: Missing maintained claim-adjacent TreS constituent source
  outcome: concern
  summary: The current gene_symbols includes treS but its cited GO/2011 source does
    not identify that named constituent. Newly inspected Albers2003 positively maps
    TreS toSSO0999 and discusses processing; this corrects any implication of biological
    absence, but is not yet a maintained citation or direct demonstration of TreS
    in the recovered400/600kDa complexes. Retain original minor as a bounded source-link
    curation gap, not a mandatory deletion or optional example gap.
  target_ids:
  - GO:7770042
  evidence_ids:
  - micro-record-2
  - micro-go-7770042
  - micro-zolghadr2011-body
  - micro-albers2003-legacy
  - micro-query-treS
  - micro-elferink2001-meta
- assessment_id: micro-bindosome-necessity
  area: grounding
  topic: Organization and uptake versus extracted assembly
  outcome: unknown
  summary: BasEF deletion preserves400/600kDa extracted complexes yet disrupts glucose
    uptake and surface morphology; this supports the recorded distinction between
    mature constituents and assembly/localization machinery. UNKNOWN for the broad
    binding-protein cohort does not imply dispensability.
  target_ids:
  - GO:7770042
  evidence_ids:
  - micro-record-2
  - micro-zolghadr2011-body
  - micro-policy
- assessment_id: micro-bindosome-function-graph
  area: graph
  topic: Coarse sugar uptake model with contact limits
  outcome: supported
  summary: Protein assemblies and sugar uptake support the two broad assembly/function
    edges. GO supplies the functional interaction interpretation, while the paper
    treats exact positioning/ABC handoff as inferred and fails to localize GlcS decisively.
    MECHANISTIC here remains a coarse model, not a directly resolved transporter contact
    or invariant native stoichiometry.
  target_ids:
  - GO:7770042
  evidence_ids:
  - micro-record-2
  - micro-zolghadr2011-body
  - micro-go-7770042
  - micro-graph-policy
- assessment_id: micro-bindosome-taxa
  area: scope
  topic: PBL2025 experiments versus P2 examples
  outcome: supported
  summary: The paper tests PBL2025 andΔbasEF under defined media, whereas examples
    identify referenceP2. Species-level canonical identity is preserved without claiming
    P2 was the actual experimental strain. COMMON is qualitative and no universal
    high-mass composition/prevalence census is asserted.
  target_ids:
  - GO:7770042
  evidence_ids:
  - micro-record-2
  - micro-zolghadr2011-body
  - micro-tax-2287
  - micro-tax-273057
- assessment_id: micro-adapter-0
  area: scope
  topic: Claim-sensitive structured-source correction
  outcome: concern
  summary: 'Current positive DnaA/oriC initiation assertions require applicability;
    native explicit exclusion only says no expression-module claim. Fresh official
    E. coli precise1k actual gene/module context was inspected: all seven selected
    loci represented, no above-threshold dnaA/BAM membership, external OmpT in59/164.
    Neither membership nor nonmembership proves structure biology.'
  target_ids:
  - GO:0036389
  evidence_ids:
  - micro-prior-0
  - micro-native-policy
  - micro-catalogue
  - micro-ecoli-meta
  - micro-ecoli-genes
  - micro-dataset-b3702
  - micro-dataset-b0177
  - micro-dataset-b2512
  - micro-dataset-b2477
  - micro-dataset-b2595
  - micro-dataset-b2617
  - micro-dataset-b0565
  - micro-ecoli-module-59
  - micro-ecoli-module-164
- assessment_id: micro-history-0
  area: provenance
  topic: Frozen observation and append-only history
  outcome: supported
  summary: Original observation remains immutable; current source differences and
    historical edits are assessed independently. No category-wide or grouped historical
    issue resolution follows from source history. Dated discussion rationale/posed_date
    remain preserved; current notes/prompts may be updated only through later authorized
    curation.
  target_ids:
  - GO:0036389
  evidence_ids:
  - micro-record-0
  - micro-prior-0
  - micro-delta-0
  - micro-policy
  - micro-original-audit
- assessment_id: micro-schema-0
  area: schema
  topic: Actual validation and diagnostic scope
  outcome: supported
  summary: Original YAML and native Markdown pass exact validation/render;42historical
    inputs verified. Current root protein commands passed with independently checked
    actual inventory/classifications; no generic pass is equated to full scientific
    coverage.
  target_ids:
  - GO:0036389
  evidence_ids:
  - micro-original-audit
  - micro-native-bacterial_pre_replicative_complex-verify
  - micro-native-bacterial_pre_replicative_complex-causal
- assessment_id: micro-coverage-0
  area: completeness
  topic: Whole-record scope with no forced optional fields
  outcome: supported
  summary: Complete target reviewed; no maintained images or verbatim snippets occur.
    No figure pixels/raw data/supplements were reanalyzed and no optional image/example/chemical
    field was required merely because empty. Source-scoped limitations and open discussions
    remain explicit.
  target_ids:
  - GO:0036389
  evidence_ids:
  - micro-record-0
  - micro-prior-0
- assessment_id: micro-adapter-1
  area: scope
  topic: Claim-sensitive structured-source correction
  outcome: concern
  summary: 'Current positive BamA–E/OmpT assembly assertions require applicability;
    original notes[1] excludes molecular complex claims in prose, without a formal
    adapter row. Fresh official E. coli precise1k actual gene/module context was inspected:
    all seven selected loci represented, no above-threshold dnaA/BAM membership, external
    OmpT in59/164. Neither membership nor nonmembership proves structure biology.'
  target_ids:
  - GO:1990063
  evidence_ids:
  - micro-prior-1
  - micro-native-policy
  - micro-catalogue
  - micro-ecoli-meta
  - micro-ecoli-genes
  - micro-dataset-b3702
  - micro-dataset-b0177
  - micro-dataset-b2512
  - micro-dataset-b2477
  - micro-dataset-b2595
  - micro-dataset-b2617
  - micro-dataset-b0565
  - micro-ecoli-module-59
  - micro-ecoli-module-164
- assessment_id: micro-history-1
  area: provenance
  topic: Frozen observation and append-only history
  outcome: supported
  summary: Original observation remains immutable; current source differences and
    historical edits are assessed independently. No category-wide or grouped historical
    issue resolution follows from source history. Dated discussion rationale/posed_date
    remain preserved; current notes/prompts may be updated only through later authorized
    curation.
  target_ids:
  - GO:1990063
  evidence_ids:
  - micro-record-1
  - micro-prior-1
  - micro-delta-1
  - micro-policy
  - micro-original-audit
- assessment_id: micro-schema-1
  area: schema
  topic: Actual validation and diagnostic scope
  outcome: supported
  summary: Original YAML and native Markdown pass exact validation/render;42historical
    inputs verified. Current root protein commands passed with independently checked
    actual inventory/classifications; no generic pass is equated to full scientific
    coverage.
  target_ids:
  - GO:1990063
  evidence_ids:
  - micro-original-audit
  - micro-native-bam_protein_complex-verify
  - micro-native-bam_protein_complex-causal
- assessment_id: micro-coverage-1
  area: completeness
  topic: Whole-record scope with no forced optional fields
  outcome: supported
  summary: Complete target reviewed; no maintained images or verbatim snippets occur.
    No figure pixels/raw data/supplements were reanalyzed and no optional image/example/chemical
    field was required merely because empty. Source-scoped limitations and open discussions
    remain explicit.
  target_ids:
  - GO:1990063
  evidence_ids:
  - micro-record-1
  - micro-prior-1
- assessment_id: micro-adapter-2
  area: scope
  topic: Claim-sensitive structured-source correction
  outcome: concern
  summary: Current positive sugar-binding/ABC uptake assertions require applicability;
    native explicit exclusion only says no expression-module claim. Fresh catalogue
    lacks the exact solfataricus host; acidocaldarius is a different species and is
    not used as proxy. Applicability assessed, but no matched-host downstream dataset
    is asserted.
  target_ids:
  - GO:7770042
  evidence_ids:
  - micro-prior-2
  - micro-native-policy
  - micro-catalogue
  - micro-ecoli-meta
- assessment_id: micro-history-2
  area: provenance
  topic: Frozen observation and append-only history
  outcome: supported
  summary: Original observation remains immutable; current source differences and
    historical edits are assessed independently. No category-wide or grouped historical
    issue resolution follows from source history. Dated discussion rationale/posed_date
    remain preserved; current notes/prompts may be updated only through later authorized
    curation.
  target_ids:
  - GO:7770042
  evidence_ids:
  - micro-record-2
  - micro-prior-2
  - micro-delta-2
  - micro-policy
  - micro-original-audit
- assessment_id: micro-schema-2
  area: schema
  topic: Actual validation and diagnostic scope
  outcome: supported
  summary: Original YAML and native Markdown pass exact validation/render;42historical
    inputs verified. Current root protein commands passed with independently checked
    actual inventory/classifications; no generic pass is equated to full scientific
    coverage.
  target_ids:
  - GO:7770042
  evidence_ids:
  - micro-original-audit
  - micro-native-bindosome_complex-verify
  - micro-native-bindosome_complex-causal
- assessment_id: micro-coverage-2
  area: completeness
  topic: Whole-record scope with no forced optional fields
  outcome: supported
  summary: Complete target reviewed; no maintained images or verbatim snippets occur.
    No figure pixels/raw data/supplements were reanalyzed and no optional image/example/chemical
    field was required merely because empty. Source-scoped limitations and open discussions
    remain explicit.
  target_ids:
  - GO:7770042
  evidence_ids:
  - micro-record-2
  - micro-prior-2
- assessment_id: micro-verdict-0
  area: other
  topic: Current scoped scientific disposition
  outcome: concern
  summary: 'needs_curation: one independently confirmed inherited minor; exact lineage
    retained.'
  target_ids:
  - GO:0036389
  evidence_ids:
  - micro-record-0
  - micro-prior-0
  - micro-ipr-IPR001957
  - micro-ipr-IPR020591
  - micro-up-P03004
  - micro-policy
- assessment_id: micro-verdict-1
  area: other
  topic: Current scoped scientific disposition
  outcome: supported
  summary: 'pass_with_limitations: BAM current substantive additions and complete
    record supported at declared tiers; no confirmed new scientific record defect.
    Historical adapter exclusion and staleness require successor repair.'
  target_ids:
  - GO:1990063
  evidence_ids:
  - micro-record-1
  - micro-prior-1
- assessment_id: micro-verdict-2
  area: other
  topic: Current scoped scientific disposition
  outcome: concern
  summary: 'needs_curation: one independently confirmed inherited minor; exact lineage
    retained.'
  target_ids:
  - GO:7770042
  evidence_ids:
  - micro-record-2
  - micro-prior-2
  - micro-go-7770042
  - micro-zolghadr2011-body
  - micro-albers2003-legacy
  - micro-query-treS
  - micro-elferink2001-meta
- assessment_id: current-input-comparison
  area: provenance
  topic: Complete frozen-input comparison and bounded refresh
  outcome: supported
  summary: 3 of ten original target hashes differ from current main. The changed content
    is substantively reassessed in the target-specific assessments; original observations
    remain historical and unchanged. All current target and used context bytes are
    frozen.
  target_ids:
  - GO:0044599
  - GO:0030119
  - GO:0020007
  - GO:0097691
  - GO:0061701
  - GO:0036389
  - GO:1990063
  - GO:7770042
  - GO:0033186
  - GO:0031518
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
- finding_id: septin-ap_5_adaptor_complex-F1
  issue_key: ap5-four-verified-family-groundings-label-only
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground the four verified AP5 subunit families
  description: The native family identities ap5_beta5_subunit → InterPro:IPR038741,
    ap5_zeta_subunit → InterPro:IPR028222, ap5_mu5_subunit → InterPro:IPR039591, ap5_sigma5_subunit
    → InterPro:IPR029392 exactly match the four maintained AP5-specific subunit classes
    and their human examples. All four rows instead retain REVIEWED_LABEL_ONLY with
    notes saying no exact CURIE was curated in the earlier pass. The schema and CURATION
    define that status as inability to assert an exact class, not unfinished identifier
    curation. Current native authorities and actual primary-source scopes were independently
    re-read. Any discussion clarification preserves its dated rationale and appends
    rather than rewrites history.
  target_ids:
  - GO:0044599
  field_paths:
  - components#ap5_beta5_subunit.grounding_status
  - components#ap5_zeta_subunit.grounding_status
  - components#ap5_mu5_subunit.grounding_status
  - components#ap5_sigma5_subunit.grounding_status
  - components#ap5_beta5_subunit.grounding_notes
  - components#ap5_zeta_subunit.grounding_notes
  - components#ap5_mu5_subunit.grounding_notes
  - components#ap5_sigma5_subunit.grounding_notes
  - discussions#resolve_ap5_subunit_groundings
  evidence_ids:
  - septin-record-ap_5_adaptor_complex
  - septin-original-ap_5_adaptor_complex
  - septin-curation-policy
  - septin-schema-policy
  - septin-ipr-IPR038741
  - septin-ipr-IPR028222
  - septin-ipr-IPR039591
  - septin-ipr-IPR029392
  - septin-protein-Q2VPB7
  - septin-protein-O43299
  - septin-protein-Q9H0R1
  - septin-protein-Q9NUS5
  - septin-family-search-AP5
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/ap_5_adaptor_complex.yaml
    role: maintained scientific record
  rule_id: Exact family grounding and reviewed-label-only contract
  native_severity: minor
  normalization_reason: Correct complex, subunit biology and protein examples remain
    intact. Four omitted exact family mappings are a bounded curation gap, not a wrong
    structure or an invitation to substitute partial domains.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T044318Z-ap-5-adaptor-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2857
- finding_id: septin-ap_type_membrane_coat_adaptor_complex-F1
  issue_key: ap-type-parent-gloss-excludes-ap5-zeta-mass
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Qualify the exhaustive parent-class subunit description
  description: The definition says each AP complex has beta plus alpha/gamma/delta/epsilon
    large chains of110–130kDa and sigma15–20kDa; the large-subunit row repeats the
    exhaustive chain list. Native GO0030119 repeats this text but also includes AP5
    as a direct child. GO0044599 and Hirst2011 identify AP5 zeta, and Hirst predicts
    beta5 at94kDa. Native human sequence masses independently give beta5~93.9kDa,
    zeta~88.6kDa and sigma5~22.5kDa. These are subtype counterexamples to the generic
    exhaustive gloss, while the two-large/mu/sigma architecture remains correct. Current
    native authorities and actual primary-source scopes were independently re-read.
    Any discussion clarification preserves its dated rationale and appends rather
    than rewrites history.
  target_ids:
  - GO:0030119
  field_paths:
  - definition
  - components#ap_large_subunits.role
  - components#ap_large_subunits.evidence[0].notes
  - components#ap_sigma_subunit.evidence[0].notes
  evidence_ids:
  - septin-record-ap_type_membrane_coat_adaptor_complex
  - septin-original-ap_type_membrane_coat_adaptor_complex
  - septin-curation-policy
  - septin-schema-policy
  - septin-record-ap_5_adaptor_complex
  - septin-go
  - septin-hirst2011-meta
  - septin-hirst2011-xml
  - septin-protein-Q2VPB7
  - septin-protein-O43299
  - septin-protein-Q9NUS5
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/ap_type_membrane_coat_adaptor_complex.yaml
    role: maintained scientific record
  rule_id: Generic-class scope and source-native conflicts
  native_severity: minor
  normalization_reason: The exact generic complex identity, hierarchy and heterotetrameric
    architecture remain supported. This is a localized outdated subtype list and size
    generalization copied from GO, not wrong whole-record identity or evidence that
    all AP biology is unsupported.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T044319Z-ap-type-membrane-coat-adaptor-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2858
- finding_id: plaque-t3-F1
  issue_key: CellStructureMech-bacterial_extracellular_vesicle-authority-definition-origin-scope
  category: scope
  severity: minor
  status: open
  certainty: confirmed
  title: Distinguish the authority definition from the broader vesicle-origin scope
  description: The definition, attributed solely to GO:0097691, describes plasma-membrane
    budding. It is faithfully copied from GO/SL, but the same record explicitly includes
    outer-membrane, outer-inner-membrane and Gram-positive vesicles and says several
    release pathways. Toyofuku2019 complete abstract expressly includes outer-membrane
    blebbing and lysis-derived routes. Readers need an explicit source-qualified scope
    note reconciling the narrow authority wording with the broader current record;
    this is not a claim that the copied GO definition or observed vesicle classes
    are fabricated.
  target_ids:
  - GO:0097691
  field_paths:
  - definition
  - definition_source
  - components[0].grounding_notes
  - causal_graphs[0].scope_notes
  evidence_ids:
  - plaque-current-3
  - plaque-go
  - plaque-SL0489
  - plaque-toyofuku2019-meta
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/bacterial_extracellular_vesicle.yaml
    role: maintained scientific record
  rule_id: Exact source scope, protein grounding and formation-specific essentiality
  native_severity: minor
  normalization_reason: Minor because exact identity, provenance and the multiple-origin
    biology are independently supported and current prose already states the broader
    scope; the required correction makes the authority/literature distinction explicit
    rather than reversing a mechanism or identity.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T044321Z-bacterial-extracellular-vesicle-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2859
- finding_id: plaque-t4-F1
  issue_key: CellStructureMech-bacterial_outer_membrane_vesicle-composite-proteolipid-type
  category: representation
  severity: minor
  status: open
  certainty: confirmed
  title: Type the complete proteolipid membrane as a composite constituent
  description: components[0] explicitly denotes the complete OMV bilayer mixture including
    outer-membrane proteins, LPS and phospholipids, yet component_type is LIPID. The
    label, role and graph refer to the whole composite membrane, not merely its lipid
    fraction. OTHER is available and the frozen BEV neighbor uses it for exactly this
    mixed-membrane distinction.
  target_ids:
  - GO:0061701
  field_paths:
  - components[0].component_type
  - components[0].grounding_notes
  - causal_graphs[0].nodes[1].component_ref
  evidence_ids:
  - plaque-current-4
  - plaque-current-3
  - plaque-schema
  - plaque-PMC2893157-jats
  - plaque-PMC5308417-jats
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/bacterial_outer_membrane_vesicle.yaml
    role: maintained scientific record
  rule_id: Exact source scope, protein grounding and formation-specific essentiality
  native_severity: minor
  normalization_reason: Minor because biological identity, label, composition and
    topology are correct and no wrong exact chemical CURIE is asserted; this is a
    bounded classification inconsistency rather than a membrane-location-as-lipid
    grounding error.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T044321Z-bacterial-outer-membrane-vesicle-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2860
- finding_id: plaque-t4-F2
  issue_key: CellStructureMech-bacterial_outer_membrane_vesicle-canonical-proteome-source-placement
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Separate the OMV proteome source from the inflammatory-model source
  description: The canonical E. coli note attributes native OMV proteomes and host
    inflammatory responses to Park2010 alone. Park reports the injection model and
    comparative protein/LPS profiles; the already cited Lee2007 paper explicitly supplies
    global proteomic profiling (141 proteins in its complete abstract). The broader
    biological example is supported, but the two experimental claims need their respective
    sources.
  target_ids:
  - GO:0061701
  field_paths:
  - canonical_examples[0].note
  - canonical_examples[0].reference
  evidence_ids:
  - plaque-current-4
  - plaque-PMC2893157-jats
  - plaque-lee2007-meta
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/bacterial_outer_membrane_vesicle.yaml
    role: maintained scientific record
  rule_id: Exact source scope, protein grounding and formation-specific essentiality
  native_severity: minor
  normalization_reason: Minor source placement because both claims are supported elsewhere
    in the existing cited literature; the fix neither changes organism identity nor
    rejects OMV inflammatory activity.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T044321Z-bacterial-outer-membrane-vesicle-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2861
- finding_id: plaque-t8-F1
  issue_key: caf1-cac2-family
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve the exact Cac2 CAF-I subunit family
  description: IPR045145 is the full Cac2/CHAF1B/FAS2 protein family and is cross-referenced
    by the verified Cac2 accession Q04199. That exact available family makes the current
    Cac2 REVIEWED_LABEL_ONLY field and broad unresolved TODO actionable. This finding
    does not force Cac1 domains or the broader RBAP family onto narrower classes.
  target_ids:
  - GO:0033186
  field_paths:
  - components[1].grounding_status
  - components[1].grounding_notes
  - discussions[0]
  evidence_ids:
  - plaque-current-8
  - plaque-policy
  - plaque-ipr-IPR045145
  - plaque-up-Q04199
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/caf_1_complex.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md REVIEWED_LABEL_ONLY
  native_severity: minor
  normalization_reason: Correct biological identity and membership; a verified exact
    family makes this bounded grounding gap actionable. Historical search honesty
    is not questioned.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T044324Z-caf-1-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2862
- finding_id: plaque-t9-F1
  issue_key: cbf3-skp1-family
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground Skp1 independently of its complex-specific role
  description: IPR016897 is the full Skp1 family and is cross-referenced by P52286.
    The current note withholds grounding because it seeks a CURIE separating CBF3-specific
    Skp1 from other complex contexts. Protein-class grounding and its source-backed
    role are separate fields, so that requirement need not prevent this exact identity
    grounding.
  target_ids:
  - GO:0031518
  field_paths:
  - components[1].grounding_status
  - components[1].grounding_notes
  - discussions[0]
  evidence_ids:
  - plaque-current-9
  - plaque-policy
  - plaque-ipr-IPR016897
  - plaque-up-P52286
  - plaque-PMC5771398-jats
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/cbf3_complex.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md REVIEWED_LABEL_ONLY
  native_severity: minor
  normalization_reason: Correct biological identity and membership; a verified exact
    family makes this bounded grounding gap actionable. Historical search honesty
    is not questioned.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T044325Z-cbf3-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2863
- finding_id: micro-F1
  issue_key: bacterial-prerc-dnaa-family
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground the DnaA constituent to its verified full family
  description: IPR001957 identifies the DnaA protein family and is cross-referenced
    by P03004. The current REVIEWED_LABEL_ONLY note says a family boundary was not
    curated in that pass; it does not reflect the now-verified exact available term.
    IPR020591 is broader DnaA/Hda and should not substitute for the exact family.
  target_ids:
  - GO:0036389
  field_paths:
  - components[0].grounding_status
  - components[0].grounding_notes
  - discussions[0]
  evidence_ids:
  - micro-record-0
  - micro-ipr-IPR001957
  - micro-ipr-IPR020591
  - micro-up-P03004
  - micro-policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/bacterial_pre_replicative_complex.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md REVIEWED_LABEL_ONLY
  native_severity: minor
  normalization_reason: Correct biological identity and membership; a verified exact
    family makes this bounded grounding gap actionable. Historical search honesty
    is not questioned.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T044322Z-bacterial-pre-replicative-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2864
- finding_id: micro-F2
  issue_key: bindosome-tres-source
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Provide an exact source for the named TreS constituent link
  description: The maintained sugar-binding component names treS alongside glcS/araS,
    but its cited GO class and Zolghadr2011 article do not name that constituent.
    Fresh Albers2003 Table2 positively identifies TreS as SSO0999 and its Discussion
    addresses processing, so zero native symbol-query results cannot imply gene absence.
    That separately found source is not currently linked beside the claim and does
    not itself demonstrate TreS in the recovered 400/600 kDa assemblies. Preserve
    the inherited bounded claim-source gap; establish the specific constituent evidence
    or explicitly qualify its scope, without requiring deletion or a new optional
    protein example.
  target_ids:
  - GO:7770042
  field_paths:
  - components[0].gene_symbols[2]
  - components[0].evidence
  evidence_ids:
  - micro-record-2
  - micro-go-7770042
  - micro-zolghadr2011-body
  - micro-albers2003-legacy
  - micro-query-treS
  - micro-elferink2001-meta
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/bindosome_complex.yaml
    role: maintained scientific record
  rule_id: Claim-specific source support
  native_severity: minor
  normalization_reason: The cited evidence does not support the exact constituent
    link, while an additional primary source positively identifies the protein and
    its processing. This is a bounded claim-source gap, not gene absence or a defect
    in the complex identity, supported GlcS/AraS cohort or principal function.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T044323Z-bindosome-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2865
actions:
- action_id: septin-ap_5_adaptor_complex-A1
  finding_ids:
  - septin-ap_5_adaptor_complex-F1
  target_ids:
  - GO:0044599
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/ap_5_adaptor_complex.yaml
    role: maintained scientific record
  description: In separately authorized curation, assign ap5_beta5_subunit → InterPro:IPR038741,
    ap5_zeta_subunit → InterPro:IPR028222, ap5_mu5_subunit → InterPro:IPR039591, ap5_sigma5_subunit
    → InterPro:IPR029392, remove incompatible reviewed-label-only status/notes and
    close or update the exact-family TODO. Retain the four components, correct examples,
    UNKNOWN assembly necessity and qualified clathrin/sorting scope. Preserve dated
    rationale, posed dates, retrieval and curation events; append clarification rather
    than rewriting them. Record curation remains outside this review-only PR.
  acceptance_checks:
  - Each mapped accession resolves to its stated AP5-specific family and matches the
    intended subtype class.
  - The four current human identities and constituent roles remain unchanged; no domain
    or accessory factor replaces a core class.
  - Focused schema/strict, protein and graph checks pass after the authorized scientific
    edit.
  - Dated rationale and historical events remain preserved; any authorized record
    edit adds required history and does not force unsupported universal necessity
    or broader family identities.
- action_id: septin-ap_type_membrane_coat_adaptor_complex-A1
  finding_ids:
  - septin-ap_type_membrane_coat_adaptor_complex-F1
  target_ids:
  - GO:0030119
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/ap_type_membrane_coat_adaptor_complex.yaml
    role: maintained scientific record
  description: In separately authorized curation, describe the large-chain alternatives
    with AP5 zeta included and make molecular masses subtype-dependent examples rather
    than universal limits. Update the corresponding component evidence glosses, preserve
    the GO identifier and typed hierarchy, and cite the primary AP5 source alongside
    the ontology while recording the source-native mismatch. Preserve dated rationale,
    posed dates, retrieval and curation events; append clarification rather than rewriting
    them. Record curation remains outside this review-only PR.
  acceptance_checks:
  - The generic description accommodates AP5 beta5/zeta/mu5/sigma5 without changing
    the supported two-large/mu/sigma architecture.
  - Universal110–130kDa and15–20kDa limits are removed or explicitly limited to the
    appropriate subtype examples; predicted and measured masses are distinguished.
  - GO identity, membrane-coat parthood, generic cohort boundaries and UNKNOWN necessity
    remain intact; focused schema/strict and graph checks pass.
  - Dated rationale and historical events remain preserved; any authorized record
    edit adds required history and does not force unsupported universal necessity
    or broader family identities.
- action_id: plaque-t3-A1
  finding_ids:
  - plaque-t3-F1
  target_ids:
  - GO:0097691
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/bacterial_extracellular_vesicle.yaml
    role: maintained scientific record
  description: Preserve the exact authority provenance, and qualify the definition
    or add a definition-adjacent literature-backed note explaining that the record
    covers multiple bacterial vesicle origins beyond plasma-membrane budding. Keep
    the nonmechanistic graph and cargo boundary.
  acceptance_checks:
  - Preserve exact supported identity, experimental organism and native versus recombinant
    context.
  - Attach source-specific evidence to each changed claim and retain historical provenance.
  - Native schema, strict, CURIE, protein and graph checks pass as applicable.
  - Preserve append-only dated rationale/history; append the current evidence and
    update active notes/TODO scope. This review PR does not edit records.
- action_id: plaque-t4-A1
  finding_ids:
  - plaque-t4-F1
  target_ids:
  - GO:0061701
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/bacterial_outer_membrane_vesicle.yaml
    role: maintained scientific record
  description: Retype the explicitly whole proteolipid boundary as OTHER, or deliberately
    restrict the component to its lipid fraction and separately preserve the whole-membrane
    actor. Keep the correctly scoped OMV identity and cargo topology.
  acceptance_checks:
  - Preserve exact supported identity, experimental organism and native versus recombinant
    context.
  - Attach source-specific evidence to each changed claim and retain historical provenance.
  - Native schema, strict, CURIE, protein and graph checks pass as applicable.
  - Preserve append-only dated rationale/history; append the current evidence and
    update active notes/TODO scope. This review PR does not edit records.
- action_id: plaque-t4-A2
  finding_ids:
  - plaque-t4-F2
  target_ids:
  - GO:0061701
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/bacterial_outer_membrane_vesicle.yaml
    role: maintained scientific record
  description: Attach Lee2007 to the proteomic clause using the supported schema/evidence
    placement, or narrow the Park-only canonical note to its OMV characterization
    and host-response experiment. Preserve the mouse-isolate/injection context.
  acceptance_checks:
  - Preserve exact supported identity, experimental organism and native versus recombinant
    context.
  - Attach source-specific evidence to each changed claim and retain historical provenance.
  - Native schema, strict, CURIE, protein and graph checks pass as applicable.
  - Preserve append-only dated rationale/history; append the current evidence and
    update active notes/TODO scope. This review PR does not edit records.
- action_id: plaque-t8-A1
  finding_ids:
  - plaque-t8-F1
  target_ids:
  - GO:0033186
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/caf_1_complex.yaml
    role: maintained scientific record
  description: Ground Cac2 to IPR045145 and reconcile its note/TODO; retain unresolved
    Cac1 and Msi1 family boundaries and supported complex membership.
  acceptance_checks:
  - Verify exact family identity and reconcile affected label-only notes and TODO
    scope.
  - Preserve supported examples and membership, with unresolved classes explicitly
    bounded.
  - Use guarded curation and pass applicable schema, strict, protein and graph checks.
  - Preserve append-only dated rationale/history; append the current evidence and
    update active notes/TODO scope. This review PR does not edit records.
- action_id: plaque-t9-A1
  finding_ids:
  - plaque-t9-F1
  target_ids:
  - GO:0031518
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/cbf3_complex.yaml
    role: maintained scientific record
  description: Ground Skp1 to IPR016897 and retain its CBF3-specific role/evidence
    separately. Narrow the TODO while leaving domain-only Ctf13/Cep3/Ndc10 candidates
    unresolved.
  acceptance_checks:
  - Verify exact family identity and reconcile affected label-only notes and TODO
    scope.
  - Preserve supported examples and membership, with unresolved classes explicitly
    bounded.
  - Use guarded curation and pass applicable schema, strict, protein and graph checks.
  - Preserve append-only dated rationale/history; append the current evidence and
    update active notes/TODO scope. This review PR does not edit records.
- action_id: micro-A1
  finding_ids:
  - micro-F1
  target_ids:
  - GO:0036389
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/bacterial_pre_replicative_complex.yaml
    role: maintained scientific record
  description: In separately authorized curation, verify/add exact DnaA IPR001957
    grounding and update current grounding status/notes; narrow the open prompt/current
    notes to unresolved oriC grounding. Preserve exact example and generic pre-RC
    boundary; append to dated rationale rather than replacing historical provenance.
  acceptance_checks:
  - Verify exact family identity and reconcile affected label-only notes and TODO
    scope.
  - Preserve supported examples and membership, with unresolved classes explicitly
    bounded.
  - Use guarded curation and pass applicable schema, strict, protein and graph checks.
  - Retain dated rationale and posed_date; append correction provenance and put current
    state in notes/prompt.
  - This review-only PR edits no scientific records; use guarded writer/history and
    applicable native validation in separately authorized curation.
- action_id: micro-A2
  finding_ids:
  - micro-F2
  target_ids:
  - GO:7770042
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/bindosome_complex.yaml
    role: maintained scientific record
  description: In separately authorized curation, add a verified claim-adjacent source
    for the exact TreS constituent scope or explicitly qualify what remains uncertain.
    Consider the fresh positive SSO0999/TreS processing evidence without equating
    signal processing with mature-complex membership. Preserve GlcS/AraS support and
    SSO3043/1273/SlaA limitations; no automatic deletion or optional-example requirement
    follows from a zero-result query.
  acceptance_checks:
  - Verify the exact gene/protein identity and source-specific bindosome membership;
    a zero-result query alone is insufficient.
  - Place a verified supporting citation beside the exact symbol/component claim or
    explicitly qualify its bounded scope; removal is warranted only by affirmative
    curation evidence, not a zero-result query.
  - Use guarded curation and pass applicable schema, strict, protein and graph checks.
  - Retain dated rationale and posed_date; append correction provenance and put current
    state in notes/prompt.
  - This review-only PR edits no scientific records; use guarded writer/history and
    applicable native validation in separately authorized curation.
limitations:
- 'AP-5, AP-type adaptor and apical-complex independent review: All three assigned
  current target hashes are unchanged. Two inherited minor findings are confirmed
  with exact predecessors; the apical target remains a qualified pass. No new finding,
  terminal disposition or unrelated-record issue resolution is invented.'
- 'AP-5, AP-type adaptor and apical-complex independent review: Fresh genuine Hirst,
  Slabicki, Kaur, Hu, Ren and Carruthers bodies were read at the precise recorded
  sections/captions; no figure pixels or supplements were inspected and excluded sections
  are not certified. There are no maintained target images.'
- 'AP-5, AP-type adaptor and apical-complex independent review: Boothroyd2008 and
  Waller2024 are secondary reviews at complete native MED metadata/abstract tier in
  this pass. Publisher challenge and Europe PMC500 bodies provide access context only;
  unread full-body claims and old Key Points are not represented as fresh observations.'
- 'AP-5, AP-type adaptor and apical-complex independent review: Current GO0020031
  polar-ring label/aliases versus definition has a bounded unresolved anatomical tension
  with primary sources. The maintained named APR/coarse parthood is not falsely refuted
  and no replacement identifier is guessed.'
- 'AP-5, AP-type adaptor and apical-complex independent review: InterPro IPR050431
  has unchecked LLM-generated prose; only native identity/flags are used as context.
  Exact AP5 families are supported independently by native family metadata and human
  example cross-references. Bounded candidate queries do not establish universal absence.'
- 'AP-5, AP-type adaptor and apical-complex independent review: Native accession/query
  checks verify identity and populated or empty coverage, not universal necessity,
  endogenous localization or a complete assembly cycle. AP-type has three typed unpopulated
  classes; apical has zero typed protein nodes. Optional representatives/classes are
  not automatic defects.'
- 'AP-5, AP-type adaptor and apical-complex independent review: Fresh catalogue coverage
  provides no matching native eukaryotic dataset for these assertions. No unrelated
  production/assay organism substitutes. Historical unavailable runner remains actual
  2026-11-03T00:49Z observation, never a fresh invocation.'
- 'AP-5, AP-type adaptor and apical-complex independent review: Record curation, final
  repository checks, CI, queue, merge and deletion remain parent-owned and are not
  certified by this scientific source review.'
- 'Vesicle, CAF-1 and CBF3 independent review: Primary bodies directly inspected:
  Leber/Yan CBF3, Park OMV, scoped Zeng Cbf2-GFP Methods/Results, and Kaufman official
  PDF selected Results/Methods. Lee2007/Lee2009 and Huh/Johnston are bounded complete-primary-abstract/native-annotation
  tiers; no unread Methods, precise strain, cargo topology or mechanism is inferred.'
- 'Vesicle, CAF-1 and CBF3 independent review: Toyofuku/Kim complete abstracts and
  Schwechheimer inspected body are secondary evidence. DOI content-negotiated Crossref
  JSON is metadata, not full publisher body. Initial403/429/404 and frontend-shell
  routes are preserved as access context; successful later Kaufman PDF access does
  not erase the initial failures.'
- 'Vesicle, CAF-1 and CBF3 independent review: No current target image exists. PDF
  extraction and text captions are not figure-pixel inspection, and no image reproduction/licence
  clearance is asserted.'
- 'Vesicle, CAF-1 and CBF3 independent review: The fresh current catalogue and official
  dataset tables were read directly as source fallback. No fresh kg-microbe-sources
  execution is claimed. Any root inclusion of the earlier00:49Z runner-unavailable
  receipt must retain its historical timestamp and failed-execution scope.'
- 'Vesicle, CAF-1 and CBF3 independent review: Catalogue/annotation and selected module
  context are computational transcriptomics only. precise1k K-12-related strains do
  not establish Park intestinal CLP isolate equivalence; selected USA300-related datasets
  do not establish the unverified Lee2009 strain. No S. cerevisiae dataset matches.
  Query nonhits and below-threshold OmpA are not biological absence.'
- 'Vesicle, CAF-1 and CBF3 independent review: Native verify/causal exit0 establishes
  declared identifier/inventory coverage, not current scientific correctness, exact
  family grounding, universal localization or necessity. Full QC/CI/merge queue are
  root-owned and not independently rerun or precertified here.'
- 'Vesicle, CAF-1 and CBF3 independent review: Inherited scientific curation is reported
  only; records and original review bundles are unchanged. No unrelated category/neighbor
  issue is terminally resolved by this slice.'
- 'Bacterial pre-RC, BAM and bindosome independent review: Scientific findings cover
  only three assigned whole records, not neighboring/category/grouped historical issue
  resolution.'
- 'Bacterial pre-RC, BAM and bindosome independent review: Primary body scope is exact:
  Miller Introduction/Results/Discussion/Methods and captions; Hagan2010 main text
  only; Bakelar main text+MethodsS2–4; Iadanza Introduction/Results/Discussion and
  two declared Methods subsections; Gu accepted pp1–8 and27–29; Zolghadr entire main
  body/Methods/captions; Albers2003 Table2/adjacent Discussion only. No figure pixels,
  maps, raw data or supplements were inspected.'
- 'Bacterial pre-RC, BAM and bindosome independent review: Hagan2011 and Elferink2001
  publisher routes are blocked; these remain complete-abstract tiers. Leonard2010
  is secondary and onlyS1/S7/S8 body sections were read. Additional protein annotation
  papers remain exact native metadata/complete abstracts and UniProt joins, not complete
  body certification.'
- 'Bacterial pre-RC, BAM and bindosome independent review: A mistaken candidate PMC
  route for Hagan2011 returned an unrelated title and was immediately excluded; its
  receipt is access provenance only, not a source finding or scientific support.'
- 'Bacterial pre-RC, BAM and bindosome independent review: BAM reference K-12 identity,
  HDB150/BL21(DE3)/DH5alpha experiments and pooled dataset strains are distinct. Predominant203kDa
  and specificOmpT assay cannot establish universal stoichiometry, atomic mechanism
  or formation necessity.'
- 'Bacterial pre-RC, BAM and bindosome independent review: Bindosome referenceP2 is
  distinct from PBL2025 experiments. AraS=SSO3066 and TreS=SSO0999 primary mappings
  are positive evidence; alias query0 is not absence. TreS processing alone does not
  establish mature400/600kDa assembly membership.'
- 'Bacterial pre-RC, BAM and bindosome independent review: No exact source-neutral
  family is forced onto the mixed bindosome cohort or unverified SO term onto oriC.
  Historical rationale is append-only; current unresolved tasks are not automatically
  completed by taxon-specific xrefs.'
- 'Bacterial pre-RC, BAM and bindosome independent review: Official dataset fallback
  is bounded to full current catalogue, mixed-strain e_coli/precise1k, seven exact
  loci and201module rows per locus plus matching59/164 gene sets. Generated ai_summary
  and per-condition activity were not used as evidence. Above/below threshold is not
  physical membership, catalysis or necessity; acidocaldarius is not a solfataricus
  proxy.'
- 'Bacterial pre-RC, BAM and bindosome independent review: Current native commands
  verify implemented identities and coverage diagnostics, not primary scientific validity.
  Bindosome PARTIAL_EXAMPLES missingTreS is not independently a scientific defect
  or proof of absence.'
- 'Bacterial pre-RC, BAM and bindosome independent review: Historical runner receipt
  is2026-11-03T00:49:00.848907–00:49:00.863225Z, exit1/unavailable; no fresh execution
  claimed. Root owns corpus QC, saved-head CI/queue/publication. No repository/Git/GitHub
  changes were made.'
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
- 'All ten original YAML/Markdown pairs remain unchanged. Three changed target hashes
  receive substantive source reassessment, not a mechanical hash update: BAM subunit/grounding/OmpT
  annotations, AraS/SSO3066 reference identity, and CBF3 Ctf13/Skp1 assembly edges.'
- 'Nine inherited minor findings remain separately tracked: AP-5 exact families, AP-parent
  composition/mass gloss, BEV authority-definition scope, OMV composite typing and
  source placement, DnaA family, bounded TreS source support, Cac2 family and Skp1
  family. Historical finding identities and dated rationale remain append-only.'
- Positive Albers2003 evidence identifies AraS/SSO3066 and TreS/SSO0999 and discusses
  processing. The TreS finding concerns the maintained claim-adjacent constituent
  source, not biological absence, mandatory deletion or a required optional example.
- BAM reference K-12 OmpT identity and the purified folding/insertion assay are supported
  within inspected main-text scope. Exact supplementary construct provenance was not
  inspected; reference annotations are not treated as experiments performed in living
  K-12.
- CBF3 core versus full-complex preparations, CAF-1 BJ926 purification versus W303
  genetics versus S288c identifiers, and Park OMV mouse-isolate/injection experiments
  versus pooled precise1k context remain distinct.
- The native protein inventory has 19 examples and 24 typed nodes. Current coverage
  diagnostics are 17 COVERED, one PARTIAL_EXAMPLES, three NO_GENE_SYMBOLS and three
  UNANCHORED_WITH_UNIPROT; these classifications alone are not scientific findings.
- 'Local corpus QC and focused gates passed before this observation. Post-save trusted-base
  review-check, exact-head re-review, final-head CI and merge-group CI remain subsequent
  external gates. Existing issue #2514 tracks the native bulk-PMID transport/reporting
  limitation; separately bounded resolution verified all 909 affected PMIDs.'
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T044318Z-ap-5-adaptor-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T044319Z-ap-type-membrane-coat-adaptor-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T044320Z-apical-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T044321Z-bacterial-extracellular-vesicle-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T044321Z-bacterial-outer-membrane-vesicle-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T044322Z-bacterial-pre-replicative-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T044323Z-bam-protein-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T044323Z-bindosome-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T044324Z-caf-1-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T044325Z-cbf3-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
links:
- https://github.com/CultureBotAI/CellStructureMech/pull/2382
- https://github.com/CultureBotAI/CellStructureMech/issues/2514
- https://github.com/CultureBotAI/CellStructureMech/issues/2855
- https://github.com/CultureBotAI/CellStructureMech/issues/2856
- https://github.com/CultureBotAI/CellStructureMech/issues/2857
- https://github.com/CultureBotAI/CellStructureMech/issues/2858
- https://github.com/CultureBotAI/CellStructureMech/issues/2859
- https://github.com/CultureBotAI/CellStructureMech/issues/2860
- https://github.com/CultureBotAI/CellStructureMech/issues/2861
- https://github.com/CultureBotAI/CellStructureMech/issues/2862
- https://github.com/CultureBotAI/CellStructureMech/issues/2863
- https://github.com/CultureBotAI/CellStructureMech/issues/2864
- https://github.com/CultureBotAI/CellStructureMech/issues/2865
```
