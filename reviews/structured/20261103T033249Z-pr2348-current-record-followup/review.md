# PR 2348: current-input review of ten records and adversarial follow-up

- Review: 20261103T033249Z-pr2348-current-record-followup
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-11-03T03:18:37.622806Z
- Finished UTC: 2026-11-03T03:32:49Z
- Reviewer: Codex root synthesis with three independent read-only adversarial reviewers (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Current-input reassessment of all ten records in PR2348. The septin-ring input changed through an added filaments-to-ring/hourglass-collar edge and curation event; its new claim is substantively supported within the stated Saccharomyces descriptive scope. Six records have qualified supported assessments and four need curation. Five original scientific findings remain: four minor confirmed grounding gaps and one major confirmed sporulation-array membership conflict. The follow-up preserves exact finding lineage, refreshes the stale review and corrects structured-source applicability evidence for seven bundles; no scientific record is edited.

## Scope And Provenance

Exact ten-record PR cohort reassessed against current main d69b72e8b4ea6626144a1eddc245e73ee90f4227. Changed inputs are substantively reassessed. Scientific records remain unchanged.

Selection: Complete cohort of ten maintained records reviewed in original PR head b8d549b9b6ddb3fd81ed4a9d7f45ecfef3ccf48d.
Coverage: full; 10 reviewed / 10 in the declared population.
Source: working_tree at Git base c5d2d7e40e573b342332ef2b1203de1089602637.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0032173 | data/structures/cytoskeleton/septin_collar.yaml | maintained | septin collar |
| GO:0032160 | data/structures/cytoskeleton/septin_filament_array.yaml | maintained | septin filament array |
| GO:0005940 | data/structures/cytoskeleton/septin_ring.yaml | maintained | septin ring |
| GO:1990334 | data/structures/cytoskeleton/sin_men_two_component_gap_complex.yaml | maintained | SIN/MEN two-component GAP complex |
| cellstructuremech:sinister_fiber | data/structures/cytoskeleton/sinister_fiber.yaml | maintained | sinister fiber |
| GO:0005876 | data/structures/cytoskeleton/spindle_microtubule.yaml | maintained | spindle microtubule |
| GO:0005816 | data/structures/cytoskeleton/spindle_pole_body.yaml | maintained | spindle pole body |
| cellstructuremech:spindle_pole_body_duplication_plaque | data/structures/cytoskeleton/spindle_pole_body_duplication_plaque.yaml | maintained | spindle pole body duplication plaque |
| cellstructuremech:spindle_pole_body_satellite | data/structures/cytoskeleton/spindle_pole_body_satellite.yaml | maintained | spindle pole body satellite |
| cellstructuremech:spirostomum_myoneme_fishnet | data/structures/cytoskeleton/spirostomum_myoneme_fishnet.yaml | maintained | Spirostomum myoneme fishnet |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full native QC | passed | True | GO:0032173, GO:0032160, GO:0005940, GO:1990334, cellstructuremech:sinister_fiber, GO:0005876, GO:0005816, cellstructuremech:spindle_pole_body_duplication_plaque, cellstructuremech:spindle_pole_body_satellite, cellstructuremech:spirostomum_myoneme_fishnet | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| Native label correspondence | passed | True | GO:0032173, GO:0032160, GO:0005940, GO:1990334, cellstructuremech:sinister_fiber, GO:0005876, GO:0005816, cellstructuremech:spindle_pole_body_duplication_plaque, cellstructuremech:spindle_pole_body_satellite, cellstructuremech:spirostomum_myoneme_fishnet | 4232 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| TraitMech references | passed | True | GO:0032173, GO:0032160, GO:0005940, GO:1990334, cellstructuremech:sinister_fiber, GO:0005876, GO:0005816, cellstructuremech:spindle_pole_body_duplication_plaque, cellstructuremech:spindle_pole_body_satellite, cellstructuremech:spirostomum_myoneme_fishnet | Native TraitMech link check passed. |
| Pinned governed files | passed | True | GO:0032173, GO:0032160, GO:0005940, GO:1990334, cellstructuremech:sinister_fiber, GO:0005876, GO:0005816, cellstructuremech:spindle_pole_body_duplication_plaque, cellstructuremech:spindle_pole_body_satellite, cellstructuremech:spirostomum_myoneme_fishnet | Pinned governed files match; native vendored check passed. |
| Native identifier resolver | passed | True | GO:0032173, GO:0032160, GO:0005940, GO:1990334, cellstructuremech:sinister_fiber, GO:0005876, GO:0005816, cellstructuremech:spindle_pole_body_duplication_plaque, cellstructuremech:spindle_pole_body_satellite, cellstructuremech:spirostomum_myoneme_fishnet | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| validate GO:0032173 | passed | True | GO:0032173 | Documented focused command passed. |
| validate-strict GO:0032173 | passed | True | GO:0032173 | Documented focused command passed. |
| validate GO:0032160 | passed | True | GO:0032160 | Documented focused command passed. |
| validate-strict GO:0032160 | passed | True | GO:0032160 | Documented focused command passed. |
| validate GO:0005940 | passed | True | GO:0005940 | Documented focused command passed. |
| validate-strict GO:0005940 | passed | True | GO:0005940 | Documented focused command passed. |
| validate GO:1990334 | passed | True | GO:1990334 | Documented focused command passed. |
| validate-strict GO:1990334 | passed | True | GO:1990334 | Documented focused command passed. |
| validate cellstructuremech:sinister_fiber | passed | True | cellstructuremech:sinister_fiber | Documented focused command passed. |
| validate-strict cellstructuremech:sinister_fiber | passed | True | cellstructuremech:sinister_fiber | Documented focused command passed. |
| validate GO:0005876 | passed | True | GO:0005876 | Documented focused command passed. |
| validate-strict GO:0005876 | passed | True | GO:0005876 | Documented focused command passed. |
| validate GO:0005816 | passed | True | GO:0005816 | Documented focused command passed. |
| validate-strict GO:0005816 | passed | True | GO:0005816 | Documented focused command passed. |
| validate cellstructuremech:spindle_pole_body_duplication_plaque | passed | True | cellstructuremech:spindle_pole_body_duplication_plaque | Documented focused command passed. |
| validate-strict cellstructuremech:spindle_pole_body_duplication_plaque | passed | True | cellstructuremech:spindle_pole_body_duplication_plaque | Documented focused command passed. |
| validate cellstructuremech:spindle_pole_body_satellite | passed | True | cellstructuremech:spindle_pole_body_satellite | Documented focused command passed. |
| validate-strict cellstructuremech:spindle_pole_body_satellite | passed | True | cellstructuremech:spindle_pole_body_satellite | Documented focused command passed. |
| validate cellstructuremech:spirostomum_myoneme_fishnet | passed | True | cellstructuremech:spirostomum_myoneme_fishnet | Documented focused command passed. |
| validate-strict cellstructuremech:spirostomum_myoneme_fishnet | passed | True | cellstructuremech:spirostomum_myoneme_fishnet | Documented focused command passed. |
| Supplemental bounded PMID authority checks | passed | True | GO:0032173, GO:0032160, GO:0005940, GO:1990334, cellstructuremech:sinister_fiber, GO:0005876, GO:0005816, cellstructuremech:spindle_pole_body_duplication_plaque, cellstructuremech:spindle_pole_body_satellite, cellstructuremech:spirostomum_myoneme_fishnet | 909 PMIDs all OK in bounded native requests; full-command limitations remain separate. |
| Official structured-source catalogue coverage | not_applicable | False | GO:0032173, GO:0032160, GO:0005940, GO:1990334, cellstructuremech:sinister_fiber, GO:0005876, GO:0005816, cellstructuremech:spindle_pole_body_duplication_plaque, cellstructuremech:spindle_pole_body_satellite, cellstructuremech:spirostomum_myoneme_fishnet | Official catalogue coverage contains 20 organisms and 28 datasets, all bacterial/archaeal; none matches this yeast/protist cohort. Fresh and independently reread cached catalogue responses retain actual access times and boundaries. The historical runner failure is documented separately; no new runner execution is claimed. |
| Independent claim-level source review | passed | True | GO:0032173, GO:0032160, GO:0005940, GO:1990334, cellstructuremech:sinister_fiber, GO:0005876, GO:0005816, cellstructuremech:spindle_pole_body_duplication_plaque, cellstructuremech:spindle_pole_body_satellite, cellstructuremech:spirostomum_myoneme_fishnet | Three read-only reviewers covered the complete ten-record cohort, including changed inputs, with explicit scientific findings and source-access limits. Final artifact/head acceptance occurs after saving. |
| Retained historical adapter runner availability | unavailable | False | GO:0032173, GO:0032160, GO:0005940, GO:1990334, cellstructuremech:sinister_fiber, GO:0005876, cellstructuremech:spirostomum_myoneme_fishnet | Historical 00:49Z invocation unavailable due to OS access restriction. Official catalogue source fallback was inspected separately; no current invocation or successful adapter execution is claimed. The actual historical exit code 1 is retained in the evidence receipt, since the native unavailable-check model has no execution exit-code field. |

## Scientific And Domain Assessments

### Whole fungal MTOC and bounded budding-yeast example

identity: supported. Targets: GO:0005816.

GO:0005816 exactly matches the whole SPB definition and SPB synonym. Species-specific evidence for budding yeast does not assert universal occurrence in every fungal cell. The whole organelle is distinct from its heterogeneous core, plaques and gamma-tubulin nucleators. CPX-1420 denotes only IL2 and CPX-1198 a species-specific small complex; neither is equivalent to the whole SPB.

### Nuclear/cytoplasmic nucleation and duplication topology

evidence: supported. Targets: GO:0005816.

The scaffold connects both faces of the SPB to microtubule-nucleating complexes. Duplication and separation provide the two poles of a bipolar spindle. The old-to-new templates-assembly edge is explicitly NONMECHANISTIC and denotes neighboring assembly at the half bridge, without asserting exact protein transfer, a strictly conservative process, purified nucleation sufficiency or a complete molecular insertion mechanism.

### Persistent exact general gamma-tubulin complex grounding gap

grounding: concern. Targets: GO:0005816.

The existing gamma_tubulin_complexes row is a broad multiprotein class, exactly covered by active GO:0000930. Deferring a narrower fungal small/ring or plaque-bound identifier does not justify withholding that general grounding. Original F1 remains confirmed/minor. Preserve the separately justified heterogeneous core and do not impose species-specific CPX composition or fixed stoichiometry.

### Primary integrative-model scope

scope: supported. Targets: GO:0005816.

Viswanath models CP/IL2 using structural, fluorescence and EM restraints, not the entire SPB at atomic resolution. The crystal constraint uses K. lactis calmodulin; tagged tomography rejects the initial two-layer Spc29 configuration. Revised core stoichiometry and proposed domain-swap/assembly mechanisms are explicitly interpretive. The record uses this source only for the layered core architecture and adds no quantitative or direct-binding claim.

### Expanded plaque intermediate and local satellite precursor

identity: supported. Targets: cellstructuremech:spindle_pole_body_duplication_plaque.

The local record denotes the transient cytoplasmic plaque formed after satellite expansion and before completed daughter-SPB maturation. It is distinct from the satellite, half bridge and whole SPB. The explicitly referenced satellite is an independently read current target with a frozen hash. Both NONMECHANISTIC graph edges preserve precursor direction; expansion can overlap insertion, so the three-stage narrative is not a strict ban on partial insertion during growth. No competing exact GO identity was established in the bounded first100 search.

### Early distal half-bridge precursor

identity: supported. Targets: cellstructuremech:spindle_pole_body_satellite.

The locally identified satellite is the early cytoplasmic precursor at the distal half-bridge tip, distinct from the mature SPB and bridge itself. Normal cycling-cell occurrence and budding-yeast scope are supported; COMMON is qualitative occurrence rather than a prevalence measurement. Its seeding function and two NONMECHANISTIC edges describe assembly topology without asserting autonomous microtubule nucleation or skipping the intervening plaque stage. No exact competing GO identity was established among the first100 query results.

### Primary localization, stage inference and optional components

scope: supported. Targets: cellstructuremech:spindle_pole_body_duplication_plaque, cellstructuremech:spindle_pole_body_satellite.

Adams serial EM/localization supports the precursor model, but shared composition and morphology do not directly trace an individual satellite into a plaque. Direct satellite Spc29, inferred plaque Spc29, tentative plaque Tub4, half-bridge Spc72/Tub4 and post-insertion Spc110 remain distinct evidence scopes. Tagged K699/K842 derivatives, alpha-factor enrichment, fixation and altered-NLS overexpression do not establish universal composition or purified binding. The records deliberately leave optional component inventories unfilled; no consequential omission was found.

### Native organism/dataset applicability

scope: not_applicable. Targets: GO:0005816, cellstructuremech:spindle_pole_body_duplication_plaque, cellstructuremech:spindle_pole_body_satellite.

Fresh complete iModulonDB catalogue has no Saccharomyces dataset. These three records contain no gene symbols, protein accession examples, regulators or expression-module assertions; a gene/strain-specific expression-module search is not available. The old physical-subject rationale can be clarified with coverage evidence, but is not treated as a confirmed actionable bundle omission for these exact sparse targets. Catalogue absence is not biological evidence.

### Frozen inputs, source tiers and native artifacts

provenance: supported. Targets: GO:0005816, cellstructuremech:spindle_pole_body_duplication_plaque, cellstructuremech:spindle_pole_body_satellite.

All three target hashes are unchanged. Native original YAML validation, Markdown roundtrip and historical source hashes pass. Adams1999 and Viswanath2017 are primary evidence; Jaspersen2004 and Winey2012 are secondary syntheses. Fresh responses and one re-read cached browser passage preserve their real retrieval times and bytes. No tracked images or additional scientific neighbor beyond the assigned satellite were used.

### Exact complex and separation from signaling states

identity: supported. Targets: GO:1990334.

GO:1990334 is exact; narrow Bfa1-Bub2 and Byr4-Cdc16 synonyms, GAP-complex parent and SPB parthood are bounded correctly. The broader SIN/MEN complex and its active/inhibited states are not substituted for the two-component GAP identity.

### Tem1 inhibition and experimental scope

evidence: supported. Targets: GO:1990334.

The primary study supports budding-yeast inhibition and orientation/checkpoint context without requiring the oversimplified claim that all checkpoint effects are exclusively GAP hydrolysis. W303-derived mutant/localization and in vitro assays do not independently demonstrate all fission-yeast details. The optional unresolved component-grounding TODO is disclosed, not fabricated as a complete molecular inventory.

### Native linker, taxon and protein identity

identity: supported. Targets: cellstructuremech:sinister_fiber.

The observed basal-body-to-five-microtubule-root linker is distinct from neighboring fibers and mother-centriole-specific GO appendages. S. similis taxon, SAG culture bridge and unreviewed O49944/AJ001438 identity agree. Historical culture-label spelling is not overextended to the exact AJ001438 row.

### Native constituent versus in vitro reassembly

evidence: supported. Targets: cellstructuremech:sinister_fiber.

Antibody specificity and native immunogold support BAp95 membership. Purified recombinant reassembly under the documented dialysis conditions supports the experimental graph; proposed rod/ladder intermediates and physiological roles remain hypotheses, and no native essentiality is inferred. Figures5/7/8 were visually inspected and captions agree.

### Bounded exact-family search and image provenance

grounding: supported. Targets: cellstructuremech:sinister_fiber.

Exact accession and three literal InterPro text requests returned empty204 responses. This supports a bounded unresolved exact-family mapping, not universal family absence; predicted coiled-coil similarity is not an exact family assignment. Link-only Figure7 attribution/licence and checksum agree with the inspected source.

### Exact filament and nonmechanistic topology

identity: supported. Targets: GO:0005876.

The record is the spindle microtubule filament, with microtubule parent and spindle parthood. Its four nonmechanistic relationships separate SPB, kinetochore and mitotic spindle from tubulin constituents and preserve presumptive kinetochore interpretation.

### Combined tubulin material and exact examples

grounding: supported. Targets: GO:0005876.

Reviewed S288c TUB1/P09733, TUB2/P02557 and TUB3/P09734 identities are independently confirmed, including bounded exact-gene searches. Combined alpha/beta lattice material can be essential without making the minor TUB3 paralog individually essential. No forced single-family accession or exhaustive MAP/motor inventory is required for the explicitly bounded combined component.

### Fixed-cell reconstruction, live imaging and annotation provenance

scope: supported. Targets: GO:0005876.

Winey reconstruction used high-pressure freezing/freeze substitution, not live imaging or cryo-ET; Straight live GFP chromosome/spindle claims are verified only at abstract scope. Anders supports tubulin mutant/cytoskeleton claims; Cederquist tests G1 astral MT/Kip3 behavior and is retained only as native annotation provenance. Secondary Jaspersen context is labeled as such. Species and S288c strain remain distinct.

### Extended cortical network and broad relations

identity: supported. Targets: cellstructuremech:spirostomum_myoneme_fishnet.

Primary studies support a distinct Spirostomum extended myoneme mesh with broad intracellular-structure parent and cortical-cytoskeleton parthood. The literal QuickGO query does not establish exhaustive ontology absence. Mikus comparative passages remain secondary context and do not equate all centrin-rich cortical networks.

### Spasmins, giant backbones and antibody boundaries

grounding: supported. Targets: cellstructuremech:spirostomum_myoneme_fishnet.

Evidence supports the two component classes and their carefully stated limits: anti-GSBP2 cross-reacts, anti-GSBP1 is specific, centrin antibodies do not resolve all paralogs, and IP is not a direct-contact map. Broader Centrin/CML and SFI1-like families are not exact mappings for the local component cohorts. No exact unverified accession or native stoichiometry is invented.

### Perturbation and versioned mechanism evidence

scope: supported. Targets: cellstructuremech:spirostomum_myoneme_fishnet.

S. minus rare type-E RNAi-associated observations do not establish uniform depletion or essentiality. S. ambiguum preprint geometry/model and antibody evidence is kept distinct from the final2026 abstract’s qualitative purified-repeat observations. No final-paper numeric, Methods or full-figure claim is independently verified here. The record appropriately avoids a resolved force/recovery graph.

### Figure5 distinction and immutable source versions

provenance: supported. Targets: cellstructuremech:spirostomum_myoneme_fishnet.

Fresh visual inspection distinguishes predicted complex, localization and Western specificity panels. Link-only permissions and record MD5s match fresh versioned XML/image package metadata. The fixed2024 preprint is not silently replaced by the updated Europe PMC preprint abstract.

### No stale targets or inherited scientific findings

provenance: supported. Targets: GO:1990334, cellstructuremech:sinister_fiber, GO:0005876, cellstructuremech:spirostomum_myoneme_fishnet.

All four current target byte hashes match the original frozen inputs. Each original verdict is pass_with_limitations with no findings. No scientific lineage is silently resolved or lost, and no stale scientific refresh is needed for these four.

### Current structured-source coverage

scope: supported. Targets: GO:1990334, cellstructuremech:sinister_fiber, GO:0005876, cellstructuremech:spirostomum_myoneme_fishnet.

Named proteins/genes trigger adapter consideration, even without expression-module claims. Fresh complete catalogue lacks matching target organisms/datasets, so target-specific module search is not_applicable without biological-negative inference. Root must pair this with its separately documented runner-availability check. Original exemption summaries need correction in the successor.

### Generic hourglass collar and localized subtypes

identity: supported. Targets: GO:0032173.

GO0032173, exact hourglass synonym and septin-cytoskeleton parent agree. Bud-neck and invasive-hyphal collar terms are retained as narrower classes; the Saccharomyces example does not redefine the generic class or impose its filament arrangement on every subtype.

### Five verified mitotic septin examples

grounding: supported. Targets: GO:0032173.

All five accession identities, reviewed statuses, recommended labels, symbols and S288C taxon match native sources. Independent primary Introduction and review synthesis support the named mitotic collar cohort; the accession-only qualifiers are appropriate. ESSENTIAL denotes collective septin material, not a requirement for every paralog or universal cell viability.

### Species example and strain identifiers

scope: supported. Targets: GO:0032173.

The S. cerevisiae occurrence and reporter example are supported by the cited primary paper. COMMON is qualitative occurrence in the named budding-cell context, not measured prevalence or a claim that every cell-cycle state contains a collar. S288C protein identities are sequence examples, not assertions that the JC482 experiments used S288C.

### Ring-to-collar descriptive topology

graph: supported. Targets: GO:0032173.

Both edges retain GO-backed septin material and budding-yeast ring expansion. NONMECHANISTIC scope does not claim an ordered recruitment pathway, direct Bni4/Kcc4 binding or that collar formation initiates their asymmetry.

### Generic Septin family versus localized cohort

grounding: concern. Targets: GO:0032173.

The component is named septin proteins but its rationale withholds grounding until a family denotes the complete assembly-forming cohort. IPR016491 supplies the generic family identity; localized composition remains a separate scientific question.

### Source tier and exact imported annotations

provenance: supported. Targets: GO:0032173.

Independent PR #2348 review inspected the current record and genuine primary body prose at the listed locators. GO/InterPro/UniProt are identifier authorities. Douglas, Versele, Glomb, Bridges and Vargas are secondary syntheses where used. Huh/Mino/Finnigan were inspected here only via metadata/abstract and exact native UniProt citation attribution. Earlier cached bodies carry their original retrieval timestamps. Successful report=xml PMC responses contained article prose; Europe PMC HTTP 500 and PMC challenge responses were not used as scientific evidence.

### Bounded record without invented inventory requirements

completeness: supported. Targets: GO:0032173.

No complete accessory inventory, stoichiometry, dimensions, image license or recruitment mechanism is claimed. These absent optional details do not create additional findings; current scientific status is retained.

### Generic array and localized children

identity: supported. Targets: GO:0032160.

GO0032160 exactly matches the bar/filament-array definition, septin-cytoskeleton parent and cytoskeleton parthood. Prospore and chlamydospore terms remain narrower array classes; ring, collar and cap are distinguished rather than merged.

### Developmental species contexts

scope: supported. Targets: GO:0032160.

The GO-backed S. cerevisiae sporulation and C. albicans chlamydospore examples are accurately attributed, and VARIABLE preserves growth-stage dependence. Species identities and the S288C sequence-example strain are correct. Native GO does not constitute a primary experiment or a universal quantitative prevalence estimate.

### Composition and membrane-localization topology

graph: supported. Targets: GO:0032160.

The three NONMECHANISTIC edges are supported at the generic-family and stated membrane-context levels. Bars are not assigned molecular thickness or treated as directly resolved single filaments; optical-sheet interpretation is retained. Neither Don1 rings nor a complete recruitment/force-generation mechanism is imported.

### Accurate accession identity and imported compartment notes

grounding: supported. Targets: GO:0032160.

All five reviewed identities, labels, primary symbols, S288C taxon and exact-query uniqueness checks pass. Native UniProt supports the imported general membrane/bud-neck citations exactly. Those notes deliberately do not establish sporulation-array membership, and identity correctness is retained independently of the membership finding.

### Generic Septin family versus localized cohort

grounding: concern. Targets: GO:0032160.

The component is named septin proteins but its rationale withholds grounding until a family denotes the complete assembly-forming cohort. IPR016491 supplies the generic family identity; localized composition remains a separate scientific question.

### Mitotic examples versus the stated sporulation array

evidence: concern. Targets: GO:0032160.

The current Saccharomyces example is specifically a prospore-membrane array, yet its component declares the full mitotic five-gene set. Primary imaging contradicts unqualified Cdc12/Shs1 assignment in that context. This does not establish their absence from every conceivable filament array or invalidate the three other accurate identities; Cdc11 detection in the PSM literature is retained.

### Ontology source chain and independent primary falsification

provenance: supported. Targets: GO:0032160.

Independent PR #2348 review inspected the current record and genuine primary body prose at the listed locators. GO/InterPro/UniProt are identifier authorities. Douglas, Versele, Glomb, Bridges and Vargas are secondary syntheses where used. Huh/Mino/Finnigan were inspected here only via metadata/abstract and exact native UniProt citation attribution. Earlier cached bodies carry their original retrieval timestamps. Successful report=xml PMC responses contained article prose; Europe PMC HTTP 500 and PMC challenge responses were not used as scientific evidence.

### Higher-order cortical ring versus smaller septin complexes

identity: supported. Targets: GO:0005940.

GO0005940 matches the defined higher-order ring, its septin-cytoskeleton parent and cell-cortex parthood. GO0031105 is a smaller oligomeric complex, appropriately retained as a distinct assembly level. The microbial record uses fungal examples without claiming that the GO class excludes animal rings.

### Five identity examples and mitotic structural cohort

grounding: supported. Targets: GO:0005940.

All sequence identities, primary symbols, reviewed statuses, S288C taxon labels and uniqueness checks pass. Primary and review evidence supports the five mitotic bud-neck septins. General membrane/bud-neck annotations are not silently promoted to a different localization. Collective ESSENTIAL is not a claim that each paralog is individually necessary for every ring.

### Fungal occurrence and Saccharomyces model

scope: supported. Targets: GO:0005940.

Native Fungi/species/strain identities agree. COMMON is a qualitative fungal occurrence statement with explicit variation by lineage and morphogenetic context, not universal occurrence, numerical prevalence or universal essentiality. The named Saccharomyces example is supported by Iwase; tested backgrounds are not equated to every S288C-derived strain.

### Division-site scaffold and cytokinesis factors

evidence: supported. Targets: GO:0005940.

Budding-yeast recruitment and cytokinesis-site organization have direct experimental support, while broader fungal scaffolding rests on reviews. The record does not claim direct binding for every cytokinesis factor or that septins generate constriction force or determine every fungal cleavage plane.

### Scoped oligomer-to-filament-to-ring hierarchy

graph: supported. Targets: GO:0005940.

The NONMECHANISTIC graph is explicitly a Saccharomyces assembly hierarchy, supported by the reconstituted Cdc11-capped core and budding-cell localization. It does not specify all five paralogs in one octamer or a universal fungal rod order. Shs1-capped rods and viable alternative hexamers limit universal reading of the generic rod-to-filament edge; these documented exceptions are retained in this assessment.

### Generic Septin family versus localized cohort

grounding: concern. Targets: GO:0005940.

The component is named septin proteins but its rationale withholds grounding until a family denotes the complete assembly-forming cohort. IPR016491 supplies the generic family identity; localized composition remains a separate scientific question.

### Primary experiments versus literature reviews

provenance: supported. Targets: GO:0005940.

Independent PR #2348 review inspected the current record and genuine primary body prose at the listed locators. GO/InterPro/UniProt are identifier authorities. Douglas, Versele, Glomb, Bridges and Vargas are secondary syntheses where used. Huh/Mino/Finnigan were inspected here only via metadata/abstract and exact native UniProt citation attribution. Earlier cached bodies carry their original retrieval timestamps. Successful report=xml PMC responses contained article prose; Europe PMC HTTP 500 and PMC challenge responses were not used as scientific evidence.

### Optional detailed composition and mechanism

completeness: supported. Targets: GO:0005940.

No exhaustive accessory-protein list, molecular dimensions, image license or full ordered recruitment mechanism is asserted. Optional unresolved details and distinct localized ring subtypes do not create additional findings.

### Substantive reassessment of the 2026-10-31 filaments-to-ring edge

graph: supported. Targets: GO:0005940.

The original ring input a29add3311f4b53bf4b50c2ec527d5ef450cfff625eadd312324d625b8790b93 differs from current f536dd5b190f0cba77de3b14131a2bd5b9d12369a96c81014cc6b0c2ebf1361d by a curation event and the organize-into edge. Its explicitly Saccharomyces NONMECHANISTIC hierarchy is supported: Glomb describes cortical ring organization and ring expansion to the hourglass; Bertin reconstitutes paired core filaments; Bridges summarizes paired/gauze cortical arrays and membrane annealing. This is descriptive assembly/remodeling, not proof of one universal filament orientation, oligomer size, all-five-in-one rod or molecular recruitment mechanism. No additional scientific defect observed in the changed claim.

### Organism-coverage basis for downstream iModulonDB applicability

provenance: supported. Targets: GO:0032173, GO:0032160, GO:0005940.

All three records declare named septin genes and require the structured-source discovery step. The independently reread cached official catalogue has no fungal dataset matching the records. Downstream gene/module queries therefore are not applicable for this scoped catalogue, with the original fetch time and separate historical runner limitation retained.

### Complete frozen-input comparison and bounded refresh

provenance: supported. Targets: GO:0032173, GO:0032160, GO:0005940, GO:1990334, cellstructuremech:sinister_fiber, GO:0005876, GO:0005816, cellstructuremech:spindle_pole_body_duplication_plaque, cellstructuremech:spindle_pole_body_satellite, cellstructuremech:spirostomum_myoneme_fishnet.

1 of ten original target hashes differ from current main. The changed content is substantively reassessed in the target-specific assessments; original observations remain historical and unchanged. All current target and used context bytes are frozen.

## Findings

### plaque-F1: The existing gamma-tubulin complex class has an exact GO grounding

minor / open / confirmed; issue key: spindle-pole-body-gamma-tubulin-complex-grounding.

The component gamma_tubulin_complexes is REVIEWED_LABEL_ONLY, with notes deferring exact fungal small-complex or plaque-bound ring-complex identifiers. Native GO0000930 directly denotes the general multiprotein gamma-tubulin complex class already asserted by this component; its definition includes MTOC localization and nucleation, and its children distinguish small and ring complexes. Ground this existing broad row to GO:0000930, or document a concrete narrower scope mismatch if the intended row changes. This does not require species-specific CPX composition, an exhaustive inventory, or replacement of the heterogeneous core component.

### septin-septin-collar-F1: Localized-cohort criterion leaves the generic Septin family ungrounded

minor / open / confirmed; issue key: septin-collar-generic-family-withheld.

The generic septin-proteins component is REVIEWED_LABEL_ONLY because its rationale asks for an accession matching the complete localized cohort. Verified IPR016491 identifies the named Septin family without requiring a localization-specific family. Reconcile grounding, status and rationale while preserving separate uncertainty about exact paralogs and associated proteins.

### septin-septin-filament-array-F1: Localized-cohort criterion leaves the generic Septin family ungrounded

minor / open / confirmed; issue key: septin-filament-array-generic-family-withheld.

The generic septin-proteins component is REVIEWED_LABEL_ONLY because its rationale asks for an accession matching the complete localized cohort. Verified IPR016491 identifies the named Septin family without requiring a localization-specific family. Reconcile grounding, status and rationale while preserving separate uncertainty about exact paralogs and associated proteins.

### septin-septin-filament-array-F2: Cdc12 and Shs1 examples are not supported in the stated Saccharomyces array context

major / open / confirmed; issue key: septin-filament-array-mitotic-examples-in-sporulation-context.

The only S. cerevisiae array context declared by this record is the prospore membrane during sporulation. Its septin component nevertheless includes CDC12/P32468 and SHS1/Q07657 as unqualified structural examples alongside the mitotic set. Their identities are correct, but primary dual-color localization finds little or no Cdc12 and no Shs1 in the Cdc10-marked sporulation structures; later work independently distinguishes the development-specific assembly. Restrict these assignments or provide direct evidence for an explicitly stated alternative array context. This is not an assertion that Cdc12/Shs1 cannot occur in any structure described loosely as an array, nor that the accessions are wrong.

### septin-septin-ring-F1: Localized-cohort criterion leaves the generic Septin family ungrounded

minor / open / confirmed; issue key: septin-ring-generic-family-withheld.

The generic septin-proteins component is REVIEWED_LABEL_ONLY because its rationale asks for an accession matching the complete localized cohort. Verified IPR016491 identifies the named Septin family without requiring a localization-specific family. Reconcile grounding, status and rationale while preserving separate uncertainty about exact paralogs and associated proteins.

## Recommended Actions And Acceptance Checks

### plaque-A1

In later authorized curation, add GO:0000930 to the existing gamma-tubulin-complex component and align grounding_status/notes with the verified general class. Preserve the specific small/ring and plaque-assembly limitations; do not equate a species-specific CPX entry with the whole SPB. Preserve historical discussion rationale and record any current progress in notes.

- Compare the revised component scope against the active GO0000930 definition and its small/ring subtypes.
- Retain the supported nuclear/cytoplasmic nucleation-site role without adding autonomous nucleation sufficiency or universal stoichiometry.
- Run native schema, strict, label, history and generated-page checks after maintained-record curation.

### septin-septin-collar-A1

Under separately authorized curation, ground the generic Septin component to verified IPR016491 and reconcile the cohort-based rationale.

- Retain separate membership evidence; do not infer universal paralog usage or stoichiometry from a family match.
- Retain structure-level rather than individual-protein viability essentiality.
- Use guarded curation/history and run native schema, strict, identifier-label, protein-example and rendered-page checks.

### septin-septin-filament-array-A1

Under separately authorized curation, ground the generic Septin component to verified IPR016491 and reconcile the cohort-based rationale.

- Retain separate membership evidence; do not infer universal paralog usage or stoichiometry from a family match.
- Retain structure-level rather than individual-protein viability essentiality.
- Use guarded curation/history and run native schema, strict, identifier-label, protein-example and rendered-page checks.

### septin-septin-filament-array-A2

Under separately authorized curation, reconcile the CDC12 and SHS1 symbols/examples with the stated S. cerevisiae sporulation-array scope: restrict/remove these structural assignments, or document a distinct source-supported context that actually fits this GO array class.

- Preserve correct accession identity and taxon information separately from structural membership.
- Do not infer absence from every array architecture or remove Cdc11 solely from a modern core-rod model; published PSM detection is distinct from integral rod composition.
- If adding Spr3/Spr28 as better-supported sporulation examples, verify their own exact native accession/taxon and localization evidence before editing.
- Do not infer Candida paralog membership from Saccharomyces or impose an exhaustive inventory requirement.
- Use guarded curation/history and run focused schema, strict, UniProt identity, label and generated-page checks.

### septin-septin-ring-A1

Under separately authorized curation, ground the generic Septin component to verified IPR016491 and reconcile the cohort-based rationale.

- Retain separate membership evidence; do not infer universal paralog usage or stoichiometry from a family match.
- Retain structure-level rather than individual-protein viability essentiality.
- Use guarded curation/history and run native schema, strict, identifier-label, protein-example and rendered-page checks.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| current-record-0 | data/structures/cytoskeleton/septin_collar.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 c16f869099afaf1a608e229fb19f217583156684f4a7311549af622691b556d9; current SHA256 c16f869099afaf1a608e229fb19f217583156684f4a7311549af622691b556d9. Record bytes unchanged since the original review. |
| original-review-0 | reviews/structured/20261021T082244Z-septin-collar-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-1 | data/structures/cytoskeleton/septin_filament_array.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 8413e81f4ac3c0daf46af8a81bbc0c819380242af370486f07865114e2edc1a0; current SHA256 8413e81f4ac3c0daf46af8a81bbc0c819380242af370486f07865114e2edc1a0. Record bytes unchanged since the original review. |
| original-review-1 | reviews/structured/20261021T082244Z-septin-filament-array-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-2 | data/structures/cytoskeleton/septin_ring.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 a29add3311f4b53bf4b50c2ec527d5ef450cfff625eadd312324d625b8790b93; current SHA256 f536dd5b190f0cba77de3b14131a2bd5b9d12369a96c81014cc6b0c2ebf1361d. Changed record reassessed against current sources. |
| original-review-2 | reviews/structured/20261021T082244Z-septin-ring-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-3 | data/structures/cytoskeleton/sin_men_two_component_gap_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 922665d09fdb8ddf24c904aefc3ccd0ec99a36f92d4d33f71a42c732036ecbdd; current SHA256 922665d09fdb8ddf24c904aefc3ccd0ec99a36f92d4d33f71a42c732036ecbdd. Record bytes unchanged since the original review. |
| original-review-3 | reviews/structured/20261021T082245Z-sin-men-two-component-gap-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-4 | data/structures/cytoskeleton/sinister_fiber.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 9227477d7ba7b31e708bd60156ccb5d24f7051d3e0451b9138e6b3380d3664e5; current SHA256 9227477d7ba7b31e708bd60156ccb5d24f7051d3e0451b9138e6b3380d3664e5. Record bytes unchanged since the original review. |
| original-review-4 | reviews/structured/20261021T082245Z-sinister-fiber-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-5 | data/structures/cytoskeleton/spindle_microtubule.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 bd8d435d59b948878bdcc978f015029ba6f6cc236b43eab0a5a5fe8b1a350fb9; current SHA256 bd8d435d59b948878bdcc978f015029ba6f6cc236b43eab0a5a5fe8b1a350fb9. Record bytes unchanged since the original review. |
| original-review-5 | reviews/structured/20261021T082245Z-spindle-microtubule-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-6 | data/structures/cytoskeleton/spindle_pole_body.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 50885e021c246e17e29beb27f7dc98e37ee4d34878648fea4fd8b565bbb2fc78; current SHA256 50885e021c246e17e29beb27f7dc98e37ee4d34878648fea4fd8b565bbb2fc78. Record bytes unchanged since the original review. |
| original-review-6 | reviews/structured/20261021T082245Z-spindle-pole-body-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-7 | data/structures/cytoskeleton/spindle_pole_body_duplication_plaque.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 e321abc96c81de9d3b524b7a68e2cefc4f28aaf72df105b42c96e1c6b8e994c3; current SHA256 e321abc96c81de9d3b524b7a68e2cefc4f28aaf72df105b42c96e1c6b8e994c3. Record bytes unchanged since the original review. |
| original-review-7 | reviews/structured/20261021T082245Z-spindle-pole-body-duplication-plaque-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-8 | data/structures/cytoskeleton/spindle_pole_body_satellite.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 a6a16f2dc3c09895fb7f4af93e1cad023c01b75dd424b99a1177ce93b516acb3; current SHA256 a6a16f2dc3c09895fb7f4af93e1cad023c01b75dd424b99a1177ce93b516acb3. Record bytes unchanged since the original review. |
| original-review-8 | reviews/structured/20261021T082245Z-spindle-pole-body-satellite-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-9 | data/structures/cytoskeleton/spirostomum_myoneme_fishnet.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 23c2668330bc68a88153d7ed54feb0a5626a88d4ae53a8da6e250d2dda8d71af; current SHA256 23c2668330bc68a88153d7ed54feb0a5626a88d4ae53a8da6e250d2dda8d71af. Record bytes unchanged since the original review. |
| original-review-9 | reviews/structured/20261021T082245Z-spirostomum-myoneme-fishnet-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| plaque-spb-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005816,GO:0032991,GO:0005825,GO:0008274,GO:0008275,GO:0000930; results selected by exact IDs; definition, isObsolete, synonyms and child relations; only the explicitly described returned definitions inform this review; fresh source bytes at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2348/adversary-plaque/spb-agent-go.source | supports | Active GO:0005816 exactly identifies the fungal MTOC and has SPB as an exact synonym. GO:0005825 denotes the distinct half bridge and is a part_of child of SPB. GO:0032991 denotes protein-containing complex. GO:0000930 directly identifies the broad gamma-tubulin complex class, with small and ring subtype children GO:0008275 and GO:0000931; narrower subtype uncertainty does not prevent grounding the existing broad row. |
| plaque-spb-agent-taxon | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; taxId, scientificName, rank and lineage; fresh source bytes at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2348/adversary-plaque/spb-agent-taxon.source | supports | NCBITaxon4932 is Saccharomyces cerevisiae at species rank. The record does not assert a particular experimental strain or quantitative prevalence. |
| plaque-spb-agent-epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1146/annurev.cellbio.20.022003.114106%22%20OR%20DOI%3A%2210.1091/mbc.E17-06-0397%22%20OR%20DOI%3A%2210.1083/jcb.145.4.809%22%20OR%20DOI%3A%2210.1534/genetics.111.128710%22; Four native resultList.result entries: DOI, title, authorString, pubYear, PMID, PMCID, abstractText and pubTypeList; fresh source bytes at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2348/adversary-plaque/spb-agent-epmc.source | supports | Exact citation identities are verified: Jaspersen/Winey2004 PMID15473833; Viswanath2017 PMID28814505/PMC5687031; Adams/Kilmartin1999 PMID10330408/PMC2133189; Winey/Bloom2012 PMID22491889/PMC3316638. The 2004 and 2012 bodies synthesize previous work; generic database publication-type tags do not make the 2012 review a new experiment. |
| plaque-spb-agent-viswanath2017 | https://pmc-oa-opendata.s3.amazonaws.com/PMC5687031.1/PMC5687031.1.xml; Native JATS: Introduction/Figure1 caption; Results Gathering of data, Representations and restraints, Initial models, single-layer Spc29 test, reduced-Spc29 architecture; Discussion; Methods Composition and stoichiometry, In vivo FRET and System representation. Selected claim-bearing main-text sections read, not all Methods/supplements. /private/tmp/cellstructure-batches-2346-2397-20261103/pr2348/adversary-plaque/spb-agent-viswanath2017.source | supports | Primary integrative modeling concerns the CP/IL2 core and portions of Spc42, Spc29, Spc110, Cmd1 and Cnm67, combining crystallography, SAXS, FRET and EM information. K. lactis calmodulin supplied the crystal constraint; in vivo FRET concerns S. cerevisiae. Tagged EM rejected the initial two-layer Spc29 model. Reduced core Spc29 stoichiometry, a possible peripheral pool and proposed calmodulin domain swaps remain model interpretations. The current record makes no fixed copy-count, whole-SPB atomic-structure or purified-assembly-sufficiency claim. |
| plaque-spb-agent-CPX-1198 | https://www.ebi.ac.uk/intact/complex-ws/complex/CPX-1198; complexAc, name, species, systematicName, participants, functions and properties; original receipt; fresh source bytes at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2348/adversary-plaque/spb-agent-CPX-1198.source | context_only | Native CPX1198 denotes the Saccharomyces cerevisiae gamma-tubulin small complex (taxon559292), a species-specific assembly with Tub4/Spc97/Spc98 and nucleotide participants. It is a candidate subassembly rather than identity for the whole SPB or every gamma-tubulin complex. Its narrower scope is not needed to establish the GO0000930 match. |
| plaque-spb-agent-CPX-1420 | https://www.ebi.ac.uk/intact/complex-ws/complex/CPX-1420; complexAc, name, species, systematicName and properties; fresh source bytes at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2348/adversary-plaque/spb-agent-CPX-1420.source | context_only | CPX1420 denotes the Saccharomyces cerevisiae intermediate-layer-2 complex (taxon559292) with Spc42/Cnm67. Its scope does not identify the entire CP/IL2 core or whole SPB. |
| plaque-spb-agent-adams1999 | https://pmc-oa-opendata.s3.amazonaws.com/PMC2133189.1/PMC2133189.1.xml; Native PMC OA JATS: Methods Yeast Strains and ImmunoEM; Results EM of SPB Duplication, Main Components of the SPB Core, Approximate Arrangement, Components of Satellite/Duplication Plaque/Half-Bridge, and altered-NLS Spc110 overexpression; Discussion. Main-text source descriptions of Figures1/3/4/6/8/9 read; no pixel reanalysis. /private/tmp/cellstructure-batches-2346-2397-20261103/pr2348/adversary-plaque/spb-agent-adams1999.source | supports | Primary serial EM of alpha-factor-released budding yeast identifies cytoplasmic duplication plaques, partial insertion and later paired SPBs. ImmunoEM directly localizes Spc42/Nud1 to both satellite and plaque, Cnm67 less consistently to satellite, and Spc29 directly to satellite; plaque Spc29 is inferred with mps2-1 fluorescence support. Spc72/Tub4 half-bridge localization is not uniform satellite incorporation. Spc110 is detected after insertion. Shared composition/morphology suggest a precursor-product relationship rather than direct lineage tracing. K699/K842 derivatives, fixation sensitivity, tagging and multiple Spc42-GFP copies bound interpretation. Delta-NLS Spc110 perturbation supports disrupted attachment; retraction/binding mechanisms remain models. |
| plaque-spb-agent-go-duplication-search | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=spindle%20pole%20body%20duplication%20plaque&amp;limit=100; Native results page1; 100 candidates read by ID and name; numberOfHits=551 with six total pages; exact query is retained in reference.; fresh source bytes at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2348/adversary-plaque/spb-agent-go-duplication-search.source | context_only | No exact SPB duplication plaque cellular-component label occurs among the first100 returned native search candidates. Mature SPB, its named plaques, half bridge and duplication processes have distinct meanings. This supports retaining the local identity within the bounded search, not an exhaustive assertion of ontology absence. |
| plaque-spb-agent-go-satellite-search | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=spindle%20pole%20body%20satellite&amp;limit=100; Native results page1; 100 candidates read by ID and name; numberOfHits=564 with six total pages; exact query is retained in reference.; fresh source bytes at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2348/adversary-plaque/spb-agent-go-satellite-search.source | context_only | No exact SPB satellite cellular-component label occurs among the first100 returned native search candidates. Mature SPB, its named plaques, half bridge and duplication processes have distinct meanings. This supports retaining the local identity within the bounded search, not an exhaustive assertion of ontology absence. |
| plaque-spb-adapter-catalogue | https://imodulondb.org/api/datasets; Complete native organism/dataset catalogue; fresh source bytes at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2348/adversary-plaque/spb-adapter-catalogue.source | supports | Complete fresh native catalogue contains 20 organism entries and 28 datasets, all bacterial or archaeal; no Saccharomyces dataset is available. Organism-specific searches are not applicable. This is catalogue coverage evidence, not negative biological evidence; no new adapter CLI execution is claimed. |
| plaque-spb-agent-winey2012 | https://pmc.ncbi.nlm.nih.gov/articles/PMC3316638/?report=xml; Native PMC HTML section Spindle pole duplication and separation, Figure7 caption and adjacent insertion/maturation/bridge-separation paragraphs; this is a secondary review. /private/tmp/cellstructure-batches-2346-2397-20261103/pr2348/adversary-plaque/winey2012-pmc.source | supports | The literature synthesis identifies satellite-bearing SPBs in cycling cells as a normal intermediate; duplication-plaque growth and nuclear-envelope insertion can overlap. Nuclear-face maturation and later bridge separation yield the two spindle poles. Mechanism of membrane fenestration remains unresolved in this synthesis. This is a successfully inspected native HTML alternative after the PMC OA S3 route returned404, not a claim that the 2012 review reports a new experiment. |
| plaque-spb-jaspersen-structure-cached | https://www.researchgate.net/publication/8241691_THE_BUDDING_YEAST_SPINDLE_POLE_BODY_Structure_Duplication_and_Function; Re-read retained browser extraction lines187-487 (author-manuscript pp5-12), structural layers/core/half-bridge sections. Serialized browser receipt /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-plaque/paper2004-browser.json | supports | Secondary review describes the layered SPB scaffold and distinct half bridge. Cached browser text was re-read for these exact records; the original 00:47:42Z access time is retained. Hash binds the serialized browser receipt, not publisher PDF or native HTTP response bytes. |
| plaque-spb-jaspersen-duplication-fresh | https://www.researchgate.net/publication/8241691_THE_BUDDING_YEAST_SPINDLE_POLE_BODY_Structure_Duplication_and_Function; Author-manuscript pp15-20, browser lines619-800: Duplication Pathway, Separation and conservative/semi-conservative discussion. Fresh serialized browser response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2348/adversary-plaque/jaspersen-duplication-browser.json; not native HTTP/PDF bytes. | supports | Secondary synthesis describes distal satellite formation, expanded duplication plaque, envelope insertion and nuclear-component recruitment, followed by bridge severing/separation. Molecular fusion/retraction and strict conservative inheritance are not established by the descriptive sequence. |
| plaque-spb-jaspersen-nucleation-fresh | https://www.researchgate.net/publication/8241691_THE_BUDDING_YEAST_SPINDLE_POLE_BODY_Structure_Duplication_and_Function; Author-manuscript pp24-26, browser lines978-1073: Microtubule Nucleation and spindle assembly. Fresh serialized browser response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2348/adversary-plaque/jaspersen-nucleation-browser.json; not native HTTP/PDF bytes. | supports | Secondary synthesis places gamma-tubulin complexes on both SPB faces through Spc110/Spc72 and distinguishes associated nucleators from alpha/beta polymers. Low nucleation by isolated soluble complexes does not establish autonomous scaffold or universal isolated-complex sufficiency. |
| plaque-current-0 | data/structures/cytoskeleton/spindle_pole_body.yaml; Entire maintained current YAML at c5d2d7e40e573b342332ef2b1203de1089602637; unchanged from historical review target input | context_only | Complete target was read. Definitions, components, functions, graph edges, discussions and history assessed. No maintained content was changed. |
| plaque-current-1 | data/structures/cytoskeleton/spindle_pole_body_duplication_plaque.yaml; Entire maintained current YAML at c5d2d7e40e573b342332ef2b1203de1089602637; unchanged from historical review target input | context_only | Complete target was read. Definitions, components, functions, graph edges, discussions and history assessed. No maintained content was changed. |
| plaque-current-2 | data/structures/cytoskeleton/spindle_pole_body_satellite.yaml; Entire maintained current YAML at c5d2d7e40e573b342332ef2b1203de1089602637; unchanged from historical review target input | context_only | Complete target was read. Definitions, components, functions, graph edges, discussions and history assessed. No maintained content was changed. |
| plaque-curation-policy | docs/CURATION.md; Identity, Components, Evidence and scientific-status requirements | context_only | Use exact GO structural identity when available, justify label-only grounding, preserve experimental scope and keep review separate from curation. Empty optional inventory alone is not a defect. |
| plaque-native-original-checks | scripts/record_review.py; Independent validate/render commands and source input git-show comparisons; actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2348/adversary-plaque/native-original-checks.json | supports | All three original bundles validate; their Markdown is byte-identical to native render --content. Every frozen historical input matches its recorded source revision. Target hashes are unchanged on current main-merge head. |
| micro-current-gap-prep-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005816,GO:0160065,GO:0160066,GO:0160067,GO:1902773,GO:1990334; results for GO:0005816, GO:0160065, GO:0160066, GO:0160067, GO:1902773 and GO:1990334; id/name/isObsolete/definition/synonyms/children | supports | Active exact GAP identity and narrow Bfa1-Bub2/Byr4-Cdc16 synonyms; appropriate GAP-complex is-a and spindle-pole-body parthood. Broader SIN/MEN complex and its inhibited/active state terms remain distinct. |
| micro-current-gap-prep-tax-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; ENA scientificName and taxonId for NCBITaxon:4932 | supports | Saccharomyces cerevisiae is the species-level example. |
| micro-current-gap-prep-fraschini-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1083/jcb.200507162; Single DOI-matched Europe PMC result: title, DOI, PMID, PMCID | supports | DOI 10.1083/jcb.200507162 resolves to Fraschini et al., PMID 16449187 / PMC2063644; citation identity only. |
| micro-current-gap-prep-fraschini-jats | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2063644/fullTextXML; Introduction sec1; GAP assays and Fig5 in sec6; Discussion sec9–11 and Fig7 model; strains sec13; GTPase assay Methods sec16 | supports | Budding-yeast Bfa1-Bub2 restrains Tem1-dependent mitotic exit. Bfa1 stabilizes Tem1-bound GTP and supports Bub2 hydrolysis; checkpoint and localization phenotypes show that checkpoint control is not reducible to a single exclusive hydrolysis mechanism. W303-derived strains, in vitro assays and mutant/localization experiments support the record’s bounded claim; this is not direct experimental evidence for the fission-yeast branch. |
| micro-current-sinister-prep-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005856,GO:0043232,GO:0120103; GO:0005856, GO:0043232 and GO:0120103 definitions and active status | supports | Cytoskeleton parthood and broad intracellular non-membrane-bounded organelle parent are compatible. Mother-centriole subdistal appendage is not an exact identity for the two differently placed sinister fibers. |
| micro-current-sinister-prep-tax-3192 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3192; ENA taxonId and scientificName | supports | NCBITaxon:3192 identifies Spermatozopsis similis. |
| micro-current-sinister-prep-O49944 | https://rest.uniprot.org/uniprotkb/O49944.json; entryType, proteinDescription, organism, sequence length, EMBL cross-reference | supports | O49944 is an unreviewed 834-aa S. similis 95 kD basal apparatus-protein entry with AJ001438 / CAA04763.1 correspondence. Sequence identity does not prove all members of a broad coiled-coil family are sinister-fiber constituents. |
| micro-current-sinister-prep-strain | https://sagdb.uni-goettingen.de/detailedList.php?str_number=1.85; SAG culture 1.85; species and sequence-reference table | supports | Current SAG 1.85 culture entry identifies S. similis and lists AJ001438; historical B1.85 spelling occurs in other sequence metadata on this culture page. The AJ001438 row itself is not claimed to contain the historical spelling. |
| micro-current-sinister-prep-geimer-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1083/jcb.140.5.1149; DOI-matched Europe PMC result identity | supports | 10.1083/jcb.140.5.1149 identifies the Geimer et al. 1998 primary study and PMC2132688. |
| micro-current-sinister-prep-geimer-s3 | https://pmc-oa-opendata.s3.amazonaws.com/PMC2132688.1/PMC2132688.1.xml; Claim-bearing Results on cloning, recombinant reassembly and immunogold/native architecture; Discussion; relevant culture, recombinant purification, dialysis, antibody and microscopy Methods; figure captions and permissions | supports | Anti-rec95 specificity and controls support BAp95 as a sinister-fiber constituent. Recombinant BAp95 assembles patterned fibers after the stated urea-removal protocol; larger/high-concentration aggregates differ. Native older- and younger-basal-body linkers attach to a five-microtubule root. Proposed physiological and assembly-intermediate interpretations remain hypotheses, and native essentiality is untested. JATS carries CC BY-NC-SA 4.0 permissions. |
| micro-current-sinister-prep-figure5 | https://pmc-oa-opendata.s3.amazonaws.com/PMC2132688.1/JCB15053.f5.jpg; Figure5 panels a–g, visually inspected | supports | Reassembled banded fibers in panels a–e differ from the larger spindle-shaped aggregates in f–g; supports the explicitly bounded in vitro reassembly claim. |
| micro-current-sinister-prep-figure7 | https://pmc-oa-opendata.s3.amazonaws.com/PMC2132688.1/JCB15053.f7.jpg; Figure7 panels a–i, visually inspected with JATS caption | supports | Anti-rec95 labeling panels a,c–f,h,i and preimmune panels b,g support sinister-fiber localization; open arrow in a denotes the distal connecting fiber, not the labeled sinister fiber. The caption’s control and scale interpretations agree. Fresh image MD5 f23cd3d26f582cd37401dc00e89ddccb matches the record. |
| micro-current-sinister-prep-figure8 | https://pmc-oa-opendata.s3.amazonaws.com/PMC2132688.1/JCB15053.f8.jpg; Figure8 native architecture panels, visually inspected | supports | Native basal-apparatus views support the differently positioned older/younger-basal-body fibers and root attachment; they do not establish proposed physiological roles. |
| micro-current-interpro-family | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/O49944/; Exact InterPro protein-to-entry endpoint /entry/interpro/protein/uniprot/O49944/; HTTP204 empty body | partial | The specific protein-entry lookup returned no entries at access time. It does not prove global absence of any applicable family. |
| micro-current-interpro-family-search | https://www.ebi.ac.uk/interpro/api/entry/interpro/?search=BAp95&amp;page_size=200; InterPro /entry/interpro/ literal search parameter; page_size=200; HTTP204 empty response | partial | The bounded InterPro text query 'BAp95' returned no result body; this is not an exhaustive homology search. |
| micro-current-interpro-family-search-sinister | https://www.ebi.ac.uk/interpro/api/entry/interpro/?search=sinister%20fiber&amp;page_size=200; InterPro /entry/interpro/ literal search parameter; page_size=200; HTTP204 empty response | partial | The bounded InterPro text query 'sinister fiber' returned no result body; this is not an exhaustive homology search. |
| micro-current-interpro-family-search-basal | https://www.ebi.ac.uk/interpro/api/entry/interpro/?search=basal%20apparatus%20protein&amp;page_size=200; InterPro /entry/interpro/ literal search parameter; page_size=200; HTTP204 empty response | partial | The bounded InterPro text query 'basal apparatus protein' returned no result body; this is not an exhaustive homology search. |
| micro-current-spindle-mt-prep-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000776,GO:0005816,GO:0005819,GO:0005874,GO:0005876,GO:0007059,GO:0072686; Seven queried GO definitions/status/hierarchy: 0000776,0005816,0005819,0005874,0005876,0007059,0072686 | supports | Exact spindle-microtubule identity, microtubule parent, spindle parthood, chromosome-segregation function and distinct SPB/kinetochore/mitotic-spindle neighbors are supported by active terms. |
| micro-current-spindle-mt-prep-tax-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; ENA taxon identity | supports | Saccharomyces cerevisiae species identity. |
| micro-current-spindle-mt-prep-tax-559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; ENA taxon identity | supports | S. cerevisiae S288c strain-level taxon; distinct from species 4932. |
| micro-current-spindle-mt-prep-winey-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1083/jcb.129.6.1601; DOI 10.1083/jcb.129.6.1601 exact result | supports | Winey et al. 1995 spindle reconstruction citation resolves to PMC2291174. |
| micro-current-spindle-mt-prep-winey-s3 | https://pmc-oa-opendata.s3.amazonaws.com/PMC2291174.1/PMC2291174.1.pdf; PDF abstract/introduction and Methods pp1601–1602; reconstruction Results; core/noncore interpretation p1609; text extracted with pdftotext | supports | High-pressure-frozen, freeze-substituted yeast serial sections support three-dimensional spindle reconstruction and core/noncore organization. D8Bx5Ca is S288c-derived. The kinetochore class is presumptive rather than direct visualization of kinetochore contacts, as the record acknowledges. These are not live-cell or cryo-electron-tomography observations. |
| micro-current-spindle-mt-prep-straight-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1126/science.277.5325.574; Complete Europe PMC abstract for DOI10.1126/science.277.5325.574 / PMID9228009 | partial | The primary abstract describes GFP-Lac-repressor-marked chromosome loci and GFP-Tub1 spindle imaging in living yeast, supporting bounded chromosome-movement/anaphase-A claims. Full text and supplementary material were not freshly inspected. |
| micro-current-spindle-mt-prep-P09733 | https://rest.uniprot.org/uniprotkb/P09733.json; UniProt entryType, primaryAccession, geneName, organism, protein name and relevant subcellular-location evidence | supports | Reviewed S288c entry P09733 identifies TUB1. Major alpha-tubulin; native experimental cytoskeleton citation PMID11739794. Accession identity and native annotations are distinguished from direct spindle-membership experiments. |
| micro-current-spindle-mt-prep-query-TUB1 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3ATUB1%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&amp;size=500; UniProt gene_exact AND organism_id:559292 AND reviewed:true; size500; X-Total-Results=1; no Link continuation | supports | Exactly one reviewed S288c result for TUB1: P09733. This checks the supplied gene-accession identity, not an exhaustive spindle proteome. |
| micro-current-spindle-mt-prep-P02557 | https://rest.uniprot.org/uniprotkb/P02557.json; UniProt entryType, primaryAccession, geneName, organism, protein name and relevant subcellular-location evidence | supports | Reviewed S288c entry P02557 identifies TUB2. Beta-tubulin; native cytoskeleton/Kip3 annotation citation PMID23001566. Accession identity and native annotations are distinguished from direct spindle-membership experiments. |
| micro-current-spindle-mt-prep-query-TUB2 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3ATUB2%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&amp;size=500; UniProt gene_exact AND organism_id:559292 AND reviewed:true; size500; X-Total-Results=1; no Link continuation | supports | Exactly one reviewed S288c result for TUB2: P02557. This checks the supplied gene-accession identity, not an exhaustive spindle proteome. |
| micro-current-spindle-mt-prep-P09734 | https://rest.uniprot.org/uniprotkb/P09734.json; UniProt entryType, primaryAccession, geneName, organism, protein name and relevant subcellular-location evidence | supports | Reviewed S288c entry P09734 identifies TUB3. Minor alpha-tubulin; no unsupported claim that this paralog is individually essential. Accession identity and native annotations are distinguished from direct spindle-membership experiments. |
| micro-current-spindle-mt-prep-query-TUB3 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3ATUB3%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&amp;size=500; UniProt gene_exact AND organism_id:559292 AND reviewed:true; size500; X-Total-Results=1; no Link continuation | supports | Exactly one reviewed S288c result for TUB3: P09734. This checks the supplied gene-accession identity, not an exhaustive spindle proteome. |
| micro-current-spindle-mt-prep-anders-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A11739794%20AND%20SRC%3AMED; Europe PMC exact PMID11739794 result | supports | Citation identity for the native TUB1 annotation source. |
| micro-current-spindle-mt-prep-cederquist-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A23001566%20AND%20SRC%3AMED; Europe PMC exact PMID23001566 result | supports | Citation identity for the native TUB2 annotation source. |
| micro-current-spindle-mt-agent-anders2001 | https://pmc.ncbi.nlm.nih.gov/articles/PMC60769/?report=xml; PMC60769 HTML; selected paragraphs 11,17,21,25,26,31,35 in retained paragraph index; abstract and relevant Results/Methods | supports | TUB1 is the major essential alpha-tubulin while TUB3 deletion is viable; GFP/mutant experiments describe abnormal cytoplasmic and spindle microtubules. Supports native annotation provenance and the record’s combined alpha/beta-material essentiality rather than essentiality of every paralog. |
| micro-current-spindle-mt-agent-cederquist2012 | https://pmc.ncbi.nlm.nih.gov/articles/PMC3516133/?report=xml; PMC3516133 HTML; abstract and Results paragraphs44,45,48,49,51 in retained paragraph index | supports | The human mutation is modeled in yeast Tub2; heterozygous diploids and GFP-TUB1 G1 astral-microtubule/Kip3 behavior are the actual assay scope. This supports the native cytoskeleton annotation provenance, not a claim that this paper directly demonstrates all spindle localization. |
| micro-current-jaspersen-secondary-context | https://www.researchgate.net/publication/8241691_THE_BUDDING_YEAST_SPINDLE_POLE_BODY_Structure_Duplication_and_Function; Retained browser text of Jaspersen and Winey 2004; microtubule-nucleation section, especially lines976–1073 | context_only | Secondary review context for the nuclear inner plaque / cytoplasmic outer plaque and gamma-tubulin nucleation. Browser response is cached text crawled three weeks earlier, freshly accessed here; no original experiment or fresh publisher PDF is claimed. Native cited papers, not this review alone, support the record’s primary structural claims. |
| micro-current-spirostomum-agent-zhang2023-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC9946354.1/PMC9946354.1.xml; Claim-bearing Results on spasmins, GSBP1/2, RNAi and adjacent cortical organization; Discussion; relevant culture, MS/IP, IF, Western and RNAi Methods; Fig5 caption/permissions | supports | S. minus myoneme composition, giant Sfi1-like backbones, antibody specificity and the bounded perturbation observations support the record. Anti-GSBP2 cross-reacts with both backbones; anti-GSBP1 is specific; anti-centrin is not paralog-specific. IP associations are not direct-contact maps. Rare type-E effects and dsRNA-bacterial checks do not establish uniform target depletion, essentiality or motor stoichiometry. JATS MD5 3e94476b75520b5f351c6f4fd97e95c4 matches the package and record. |
| micro-current-spirostomum-agent-zhang2023-package | https://pmc-oa-opendata.s3.amazonaws.com/PMC9946354.1/PMC9946354.1.json; Versioned PMC9946354.1 file manifest, licence and retraction metadata | supports | Versioned PMC9946354.1 manifest identifies Zhang2023 XML/image checksums and CC BY-NC licence; no retraction indicated. Fresh JATS and Figure5 MD5s match manifest and record. |
| micro-current-spirostomum-agent-figure5 | https://pmc-oa-opendata.s3.amazonaws.com/PMC9946354.1/sciadv.add6550-f5.jpg; Figure5 A,B,C, visually inspected against caption | supports | A is an AlphaFold prediction; B combines centrin/GSBP2 staining across cortical layers; C contrasts GSBP1 versus GSBP2 staining and one-versus-two Western bands. The image does not prove an atomic native complex. Image MD5 4d4c13d6219f5b468c531d2def3df883 matches package and record. |
| micro-current-spirostomum-agent-lannan2024-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC11581044.2/PMC11581044.2.xml; Versioned PMC11581044.2 preprint, Results sections S3,S4,S5,S7 and claim-relevant Discussion S8 | supports | The inspected 2024 version supports the S. ambiguum mesh geometry, calcium-linked observations and bounded repeat-complex predictions. Volume conservation is a model assumption; cross-species antibody labeling is not paralog identification; predicted compact/extended conformations are not direct proof of the final force-generating mechanism. Old future-work statements do not imply the final 2026 work lacks experiments. JATS MD5 9546d004a0e44d93c64fded2bff97443 matches manifest and record. |
| micro-current-spirostomum-agent-lannan2024-package | https://pmc-oa-opendata.s3.amazonaws.com/PMC11581044.2/PMC11581044.2.json; Versioned PMC11581044.2 manifest: XML checksum/licence | supports | The fixed versioned preprint XML checksum is verified and its CC BY-NC-ND 4.0 scope retained; this is distinct from subsequently updated Europe PMC preprint metadata. |
| micro-current-spirostomum-agent-epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=100&amp;query=DOI%3A10.1126%2Fsciadv.add6550%20OR%20DOI%3A10.1073%2Fpnas.2601408123%20OR%20DOI%3A10.1101%2F2024.11.07.622534%20OR%20DOI%3A10.1016%2Fj.cell.2025.09.027; Exact four-DOI Europe PMC result metadata | supports | Resolves Zhang2023, the Lannan preprint, Lannan2026 final PNAS and Mikus2025 identifiers/titles. The current preprint metadata can describe an updated version and is not silently substituted for PMC11581044.2. |
| micro-current-spirostomum-final2026-abstract | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=100&amp;query=DOI%3A10.1126%2Fsciadv.add6550%20OR%20DOI%3A10.1073%2Fpnas.2601408123%20OR%20DOI%3A10.1101%2F2024.11.07.622534%20OR%20DOI%3A10.1016%2Fj.cell.2025.09.027; Only DOI10.1073/pnas.2601408123 / PMID42213749 result abstractText | partial | The final primary abstract reports centrin/Sfi1 myoneme evidence, deformation modeling and purified repeat-complex calcium-dependent compaction/self-association. Supports only these qualitative abstract-level imports; final Methods, numerical conditions, figures and supplementary data were not available here. |
| micro-current-spirostomum-agent-lannan2026-epmcfull | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13229174/fullTextXML; Europe PMC PMC13229174/fullTextXML HTTP500 receipt | context_only | Fresh final-paper full-text request failed with HTTP500; no final full-text inspection claimed. |
| micro-current-spirostomum-agent-lannan2026-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC13229174/; PMC13229174 HTTP200 response body | context_only | HTTP200 body is a browser/recaptcha challenge, not readable scientific full text. No final-paper body, embargo date or figures were verified through this response. |
| micro-current-spirostomum-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005622,GO:0030863; GO:0005622 and GO:0030863 active definitions | supports | Broad intracellular-anatomical-structure parent and cortical-cytoskeleton parthood are compatible with the local fishnet identity. |
| micro-current-spirostomum-agent-go-myoneme-search | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=myoneme; QuickGO text search for literal myoneme; zero results | partial | This bounded GO text query supplies no exact identity term. Primary evidence and explicit local identity carry the structure; a zero-result text query is not universal ontology absence. |
| micro-current-spirostomum-agent-taxon-402029 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/402029; ENA taxonId/scientificName | supports | Exact species identity: Spirostomum minus. |
| micro-current-spirostomum-agent-taxon-37688 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/37688; ENA taxonId/scientificName | supports | Exact species identity: Spirostomum ambiguum. |
| micro-current-spirostomum-agent-IPR050145 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050145/; Native InterPro accession/name/type and family description | context_only | Centrin/CML-like is a broader family than myonemal spasmins and includes other calcium-binding proteins; it is not exact structure-specific grounding. Description text is authority-provided context, not independent primary localization evidence. |
| micro-current-spirostomum-agent-IPR052270 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR052270/; Native InterPro accession/name/type and family description | context_only | Centrin-binding protein SFI1-like covers a broader class including other proteins such as CCDC191; it is not demonstrated to map exactly the giant Spirostomum backbone pair. No invented exact GSBP accession. |
| micro-current-spirostomum-agent-mikus2025-paper-pdf | https://www.roscoff-culture-collection.org/sites/default/files/rcc-papers/Mikus%20et%20al.%20-%202025%20-%20Charting%20the%20landscape%20of%20cytoskeletal%20diversity%20in%20microbial%20eukaryotes.pdf; Fresh institutional PDF, printed pp7 and13; text lines425–450 and765–790 in retained pdftotext output | context_only | Spirostomum fishnet and Paramecium ICL are comparative context citing earlier studies. Lacrymaria fishnet/oral-ring discussion concerns a different taxon. These passages do not supply new primary Spirostomum evidence or establish identity of all centrin-rich networks. |
| micro-current-current-adapter-catalogue | https://imodulondb.org/api/datasets; Complete /api/datasets JSON list: 20 organism entries / 28 datasets; no pagination advertised | context_only | The complete returned catalogue contains no S. cerevisiae, S. similis or Spirostomum organism/dataset. A target-specific module search is therefore not applicable. This is dataset coverage, not negative biological evidence. |
| micro-current-record-gap | data/structures/cytoskeleton/sin_men_two_component_gap_complex.yaml; Complete unchanged target YAML | supports | Current target bytes match the original review frozen SHA256 922665d09fdb8ddf24c904aefc3ccd0ec99a36f92d4d33f71a42c732036ecbdd. Full target read; no record edit or stale refresh required. |
| micro-original-review-gap | reviews/structured/20261021T082245Z-sin-men-two-component-gap-complex-audit/review.yaml; Original source inputs/checks/evidence/assessments/findings/verdict/limitations | supports | Original verdict pass_with_limitations with no findings. Its target hash remains current and native validation/render passes; its iModulonDB exemption relies on absence of expression-module claims rather than establishing actual organism/dataset applicability. |
| micro-current-record-sinister | data/structures/cytoskeleton/sinister_fiber.yaml; Complete unchanged target YAML | supports | Current target bytes match the original review frozen SHA256 9227477d7ba7b31e708bd60156ccb5d24f7051d3e0451b9138e6b3380d3664e5. Full target read; no record edit or stale refresh required. |
| micro-original-review-sinister | reviews/structured/20261021T082245Z-sinister-fiber-audit/review.yaml; Original source inputs/checks/evidence/assessments/findings/verdict/limitations | supports | Original verdict pass_with_limitations with no findings. Its target hash remains current and native validation/render passes; its iModulonDB exemption relies on absence of expression-module claims rather than establishing actual organism/dataset applicability. |
| micro-current-record-spindle | data/structures/cytoskeleton/spindle_microtubule.yaml; Complete unchanged target YAML | supports | Current target bytes match the original review frozen SHA256 bd8d435d59b948878bdcc978f015029ba6f6cc236b43eab0a5a5fe8b1a350fb9. Full target read; no record edit or stale refresh required. |
| micro-original-review-spindle | reviews/structured/20261021T082245Z-spindle-microtubule-audit/review.yaml; Original source inputs/checks/evidence/assessments/findings/verdict/limitations | supports | Original verdict pass_with_limitations with no findings. Its target hash remains current and native validation/render passes; its iModulonDB exemption relies on absence of expression-module claims rather than establishing actual organism/dataset applicability. |
| micro-current-record-spirostomum | data/structures/cytoskeleton/spirostomum_myoneme_fishnet.yaml; Complete unchanged target YAML | supports | Current target bytes match the original review frozen SHA256 23c2668330bc68a88153d7ed54feb0a5626a88d4ae53a8da6e250d2dda8d71af. Full target read; no record edit or stale refresh required. |
| micro-original-review-spirostomum | reviews/structured/20261021T082245Z-spirostomum-myoneme-fishnet-audit/review.yaml; Original source inputs/checks/evidence/assessments/findings/verdict/limitations | supports | Original verdict pass_with_limitations with no findings. Its target hash remains current and native validation/render passes; its iModulonDB exemption relies on absence of expression-module claims rather than establishing actual organism/dataset applicability. |
| micro-current-original-validation | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2348/adversary-microtubule/original-checks.json; Four native validate results, renderer byte equality and frozen-target comparison | supports | All four original reviews validate with exit0, rendered Markdown matches exactly, and target hashes match. This receipt does not represent full corpus QC. |
| micro-current-adapter-policy | .claude/skills/review-yaml-record/SKILL.md; structured-source-cross-checks block, lines91–123 | supports | Named genes/proteins/accessions trigger structured-source consideration. For iModulonDB candidates, resolve runner and coverage first; lack of matching organism/dataset supports not_applicable. Absence of an expression-module assertion is not the stated exemption. |
| septin-p2348-collar-record | data/structures/cytoskeleton/septin_collar.yaml; Entire target, all components/protein examples, taxonomy, graph edges, evidence and discussions | context_only | Complete target read after native inspection. Maintained record and mapping status remain PROPOSED; no scientific promotion or content change. |
| septin-p2348-policy | docs/CURATION.md; Components: family grounding, composition and structure-formation essentiality | context_only | A generic family identifier is distinct from an exact localized cohort; ESSENTIAL refers to formation of the named structure, not viability or each named paralog. |
| septin-p2348-example-policy | .claude/skills/uniprot-protein-examples/SKILL.md; Non-negotiable rules1–5; captured as expanded native inspect input | context_only | Correct accession, gene, taxon and entry status do not independently establish structure membership. Native subcellular-location evidence is retained only for the actual compartment named. |
| septin-p2348-septin-collar-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032173,GO:0032156,GO:0032174,GO:0062140,GO:0005940,GO:0032160,GO:0005856,GO:0032165,GO:0032166,GO:0032159,GO:0005938,GO:0031105; Returned exact terms and isObsolete flags; definitions, synonyms and children with is_a versus part_of relations | supports | Exact active GO definitions, generic structure classes, named parents/children and structural parthood were checked. The returned broader terms expose the relevant child relations. |
| septin-p2348-septin-collar-agent-family | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016491/; metadata accession/name/type=family, description and hierarchy; cached response independently reread at this review | supports | Cached native response independently reread for PR #2348; accessed_at retains the actual earlier fetch time. IPR016491 is the Septin family, appropriate to the generic septin-proteins label. It does not delimit one localized cohort, specify stoichiometry or prove membership of an individual example. |
| septin-p2348-septin-collar-agent-paper-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=25&amp;query=%28DOI%3A%2210.1091/mbc.E04-09-0764%22%29%20OR%20%28DOI%3A%2210.1534/genetics.107.073007%22%29%20OR%20%28DOI%3A%2210.1073/pnas.0803330105%22%29%20OR%20%28DOI%3A%2210.1016/j.devcel.2011.02.004%22%29%20OR%20%28DOI%3A%2210.3389/fcell.2016.00123%22%29%20OR%20%28DOI%3A%2210.1016/j.mib.2014.04.004%22%29%20OR%20%28DOI%3A%2210.1099/mic.0.000359%22%29%20OR%20%28EXT_ID%3A14562095%20AND%20SRC%3AMED%29%20OR%20%28EXT_ID%3A25971666%20AND%20SRC%3AMED%29%20OR%20%28EXT_ID%3A9790978%20AND%20SRC%3AMED%29; Relevant exact DOI/PMID result objects; publication metadata and abstracts | supports | Fresh native metadata verifies the ten exact DOI/PMID identities, titles and publication types. Huh 2003, Finnigan 2015 and Mino 1998 were read at abstract/metadata tier here; their imported localization citations were checked against native UniProt. Their primary bodies were not independently audited in this assigned slice. |
| septin-p2348-septin-collar-agent-P32457 | https://rest.uniprot.org/uniprotkb/P32457.json; primaryAccession, entryType, proteinDescription, genes, organism and SUBCELLULAR LOCATION evidence | supports | The reviewed accession, recommended protein label, primary CDC3 symbol and organism taxon559292 match the record. Native subcellular-location annotations and their experimental PubMed citations were inspected without treating general membrane/bud-neck evidence as another morphogenetic localization. |
| septin-p2348-septin-collar-agent-symbol-CDC3 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=100&amp;query=%28gene_exact%3ACDC3%29%20AND%20%28taxonomy_id%3A4932%29%20AND%20%28reviewed%3Atrue%29; Exact query in receipt, results cardinality, primaryAccession and gene token | context_only | Exact reviewed CDC3 query in S. cerevisiae returns one entry, P32457. The gene token and taxon were checked directly; this is an identity/uniqueness result, not membership evidence. |
| septin-p2348-septin-collar-agent-P25342 | https://rest.uniprot.org/uniprotkb/P25342.json; primaryAccession, entryType, proteinDescription, genes, organism and SUBCELLULAR LOCATION evidence | supports | The reviewed accession, recommended protein label, primary CDC10 symbol and organism taxon559292 match the record. Native subcellular-location annotations and their experimental PubMed citations were inspected without treating general membrane/bud-neck evidence as another morphogenetic localization. |
| septin-p2348-septin-collar-agent-symbol-CDC10 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=100&amp;query=%28gene_exact%3ACDC10%29%20AND%20%28taxonomy_id%3A4932%29%20AND%20%28reviewed%3Atrue%29; Exact query in receipt, results cardinality, primaryAccession and gene token | context_only | Exact reviewed CDC10 query in S. cerevisiae returns one entry, P25342. The gene token and taxon were checked directly; this is an identity/uniqueness result, not membership evidence. |
| septin-p2348-septin-collar-agent-P32458 | https://rest.uniprot.org/uniprotkb/P32458.json; primaryAccession, entryType, proteinDescription, genes, organism and SUBCELLULAR LOCATION evidence | supports | The reviewed accession, recommended protein label, primary CDC11 symbol and organism taxon559292 match the record. Native subcellular-location annotations and their experimental PubMed citations were inspected without treating general membrane/bud-neck evidence as another morphogenetic localization. |
| septin-p2348-septin-collar-agent-symbol-CDC11 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=100&amp;query=%28gene_exact%3ACDC11%29%20AND%20%28taxonomy_id%3A4932%29%20AND%20%28reviewed%3Atrue%29; Exact query in receipt, results cardinality, primaryAccession and gene token | context_only | Exact reviewed CDC11 query in S. cerevisiae returns one entry, P32458. The gene token and taxon were checked directly; this is an identity/uniqueness result, not membership evidence. |
| septin-p2348-septin-collar-agent-P32468 | https://rest.uniprot.org/uniprotkb/P32468.json; primaryAccession, entryType, proteinDescription, genes, organism and SUBCELLULAR LOCATION evidence | supports | The reviewed accession, recommended protein label, primary CDC12 symbol and organism taxon559292 match the record. Native subcellular-location annotations and their experimental PubMed citations were inspected without treating general membrane/bud-neck evidence as another morphogenetic localization. |
| septin-p2348-septin-collar-agent-symbol-CDC12 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=100&amp;query=%28gene_exact%3ACDC12%29%20AND%20%28taxonomy_id%3A4932%29%20AND%20%28reviewed%3Atrue%29; Exact query in receipt, results cardinality, primaryAccession and gene token | context_only | Exact reviewed CDC12 query in S. cerevisiae returns one entry, P32468. The gene token and taxon were checked directly; this is an identity/uniqueness result, not membership evidence. |
| septin-p2348-septin-collar-agent-Q07657 | https://rest.uniprot.org/uniprotkb/Q07657.json; primaryAccession, entryType, proteinDescription, genes, organism and SUBCELLULAR LOCATION evidence | supports | The reviewed accession, recommended protein label, primary SHS1 symbol and organism taxon559292 match the record. Native subcellular-location annotations and their experimental PubMed citations were inspected without treating general membrane/bud-neck evidence as another morphogenetic localization. |
| septin-p2348-septin-collar-agent-symbol-SHS1 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=100&amp;query=%28gene_exact%3ASHS1%29%20AND%20%28taxonomy_id%3A4932%29%20AND%20%28reviewed%3Atrue%29; Exact query in receipt, results cardinality, primaryAccession and gene token | context_only | Exact reviewed SHS1 query in S. cerevisiae returns one entry, Q07657. The gene token and taxon were checked directly; this is an identity/uniqueness result, not membership evidence. |
| septin-p2348-septin-collar-agent-taxon-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; taxId, scientificName, rank and lineage | supports | Native taxonomy confirms the exact taxon identifier, scientific name and rank; species scope is distinguished from the S288C sequence-example strain. |
| septin-p2348-septin-collar-agent-taxon-559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; taxId, scientificName, rank and lineage | supports | Native taxonomy confirms the exact taxon identifier, scientific name and rank; species scope is distinguished from the S288C sequence-example strain. |
| septin-p2348-septin-collar-agent-kozubowski2005-xml | https://pmc.ncbi.nlm.nih.gov/articles/PMC1182288/?report=xml; PMC1182288 native full HTML despite report=xml parameter: Introduction, Methods sec3–4/Table1, Results sec6/Figure1 legend and Discussion sec9 | supports | Primary source identity and body support the S. cerevisiae ring-to-collar context and Bni4/Kcc4 reporters. Intro identifies the five vegetative septins; Results sec6/Fig1 tracks reporter asymmetry already before budding and during collar formation. Methods specify JC482-congenic backgrounds and tagged reporters. The paper does not establish that the ring-to-collar transition initiates reporter asymmetry. |
| septin-p2348-septin-collar-agent-versele-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC1761124/?pdf=render; PMC1761124 S2 paragraphP4 and Figure3 context; review tier, original retrieval retained | supports | Cached native response independently reread for PR #2348; accessed_at retains the actual earlier fetch time. Review synthesis explicitly describes Cdc3/Cdc10/Cdc11/Cdc12/Shs1 complexes in the mitotic mother-bud-neck collar, distinguishing the meiotic cohort. The older molecular assembly model is not adopted as a current universal subunit-order claim. |
| septin-p2348-filament-array-record | data/structures/cytoskeleton/septin_filament_array.yaml; Entire target, all components/protein examples, taxonomy, graph edges, evidence and discussions | context_only | Complete target read after native inspection. Maintained record and mapping status remain PROPOSED; no scientific promotion or content change. |
| septin-p2348-septin-array-agent-taxon-5476 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5476; taxId, scientificName, rank and lineage | supports | Native taxonomy confirms the exact taxon identifier, scientific name and rank; species scope is distinguished from the S288C sequence-example strain. |
| septin-p2348-septin-array-agent-douglas-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC1214204/?pdf=render; PMC1214204 sec14 and sec17; cached response independently reread at this review; review-tier synthesis | supports | Cached native response independently reread for PR #2348; accessed_at retains the actual earlier fetch time. The GO definition source is a literature review. It describes prospore septin sheets appearing as bars in optical sections and Candida chlamydospore peripheral filament arrays after septation. These stage-dependent localizations are not a single universal mitotic paralog set. |
| septin-p2348-septin-array-agent-tachikawa2001 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2150859/fullTextXML; PMC2150859 Results sec7–10 and Figures5–9 legends; cached response independently reread at this review | supports | Cached native response independently reread for PR #2348; accessed_at retains the actual earlier fetch time. Primary Spr28/Gip1/Glc7 imaging supports a dynamic prospore-membrane array. Optical bars can represent parallel sheets; the Don1 leading-edge ring is distinct. Disrupted septin localization in gip1 mutants does not by itself establish that every membrane process requires every septin. |
| septin-p2348-septin-array-agent-mcmurray2008 | https://pmc.ncbi.nlm.nih.gov/articles/PMC2562167/?report=xml; PMC2562167 Results and Discussion S1: sporulation paragraphs beginning Two septins required / Like Cdc10 / Unlike CDC3; Figure3A,C,E,F,G and caption; DOI10.1016/j.cub.2008.07.020, PMID18701287 | refutes | Primary dual-color imaging finds little or no Cdc12-GFP in Cdc10-mCherry-marked spore-associated structures and no Shs1-GFP colocalization there; Shs1 remains in ascal cytoplasm. Cdc12 persists by immunoblot, so failure to detect it in the array is not attributed simply to degradation. Cdc10 is reused through the developmental transition. This directly challenges the unqualified Cdc12/Shs1 examples in the record's S. cerevisiae sporulation context. |
| septin-p2348-septin-array-agent-mcmurray2008-figure3 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/502c/2562167/a3850b2cb250/nihms67754f3.jpg; Native Figure 3 panels A-G visually inspected in this review, with the freshly fetched full-text caption and Results; particular comparisons C/F and persistence blot E. | refutes | Native Figure3 was visually inspected: panelsC/F compare Cdc10-mCherry-marked spore structures with Cdc12-GFP/Shs1-GFP; panelE shows Cdc12 persistence. Interpretation follows the primary caption and Results, without extracting new quantitative intensity values. |
| septin-p2348-septin-array-agent-garcia2016 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4772501/fullTextXML; PMC4772501 native JATS: Abstract; Introduction; Results Higher-order assembly and Behavior of sporulation-specific septin complexes in vivo; Figure 4 caption; Discussion. Text and legends, no pixel reanalysis. | refutes | Later primary study tests development-specific complexes. Results s08 uses FRAP and BiFC: Cdc3–Cdc10 and Cdc3–Spr3 mark PSM structures, whereas forced Cdc3–Cdc12 interaction is predominantly peripheral ascal puncta. The Introduction explicitly preserves detectable Cdc11 at the PSM while the bulk of Cdc12/Shs1 is excluded. These observations are scoped to tested sporulating backgrounds. |
| septin-p2348-ring-record | data/structures/cytoskeleton/septin_ring.yaml; Entire target, all components/protein examples, taxonomy, graph edges, evidence and discussions | context_only | Complete target read after native inspection. Maintained record and mapping status remain PROPOSED; no scientific promotion or content change. |
| septin-p2348-septin-ring-agent-taxon-4751 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4751; taxId, scientificName, rank and lineage | supports | Native taxonomy confirms the exact taxon identifier, scientific name and rank; species scope is distinguished from the S288C sequence-example strain. |
| septin-p2348-septin-ring-agent-iwase2007-xml | https://pmc.ncbi.nlm.nih.gov/articles/PMC2013704/?report=xml; PMC2013704 genuine full HTML: Abstract, Introduction, Materials/strain Table 1, Results and Figure 1-5 legends on Shs1 localization, Cdc3/10/11/12 rings without Shs1, and Iqg1/Myo1/Cyk3 localization; no pixel reanalysis. | supports | Primary S. cerevisiae experiments verify Shs1 bud-neck localization and distinguish septin ring assembly from recruitment of cytokinesis factors. Shs1 deletion can leave Cdc3/Cdc10/Cdc11/Cdc12 rings assembled while Iqg1/Myo1/Cyk3 localization and cytokinesis are impaired; requirement depends on background and conditions. |
| septin-p2348-septin-ring-agent-bertin2008-xml | https://pmc.ncbi.nlm.nih.gov/articles/PMC2426963/?report=xml; PMC2426963 Results sec2–6, especially sec2 and sec4/Figures1 and4 legends; exact DOI10.1073/pnas.0803330105 | supports | Purified recombinant Cdc3/Cdc10/Cdc11/Cdc12 complexes form nonpolar octameric rods; lowering salt yields end-to-end paired filaments. The direct reconstitution establishes a four-paralog core with two copies each, not simultaneous incorporation of all five listed mitotic paralogs. Shs1 replacement was a proposal in this paper. |
| septin-p2348-septin-ring-agent-mcmurray2011-xml | https://pmc.ncbi.nlm.nih.gov/articles/PMC3079881/?report=xml; PMC3079881 genuine full HTML: Summary; Results Cdc12 and Cdc3 homodimerization, Blocking Filament Assembly is Lethal and Prevents Cortical Septin Localization; Figure 3 legend and genotype/condition context. Text/legend inspection, no raw EM or fluorescence reanalysis. | supports | Primary interface-mutant and microscopy experiments connect filament polymerization to cortical organization and viability in the tested yeast conditions. Cdc10- or Cdc11-deficient cells can survive via alternative hexameric assemblies, so neither individual necessity nor one oligomer size is universal. |
| septin-p2348-septin-ring-agent-glomb2016-xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5093138/fullTextXML; PMC5093138 native JATS full text: paragraphs The mitotic yeast, Septin octamers containing Shs1, In the living yeast cell, After bud formation and Taken together; Figure 2 caption; secondary minireview. | supports | Review synthesis supports the five mitotic septins, bud-site recruitment, ring-to-collar/split-ring transitions and scaffold functions. It explicitly distinguishes Cdc11-capped rods that assemble end-to-end from Shs1-capped rods that preferentially form curved/lateral assemblies. |
| septin-p2348-septin-ring-agent-bridges2014-xml | https://pmc.ncbi.nlm.nih.gov/articles/PMC4266239/?report=xml; PMC4266239 S1–S3 and Figure1 textual legend; review tier, DOI10.1016/j.mib.2014.04.004 | supports | Review of fungal pathogens supports septin scaffolding at division sites and species-specific higher-order localization, including bud-neck and hyphal septation contexts. It cautions that many mechanistic explanations remain unresolved and mutant phenotypes can be indirect. |
| septin-p2348-septin-ring-agent-vargas2016-xml | https://pmc.ncbi.nlm.nih.gov/articles/PMC5068138/?report=xml; PMC5068138 s1-3, s1-5 and s1-6, Figure1 textual legend; review tier, DOI10.1099/mic.0.000359 | supports | Review supports broad fungal septin occurrence and functions in morphology, septation and development, while distinguishing species-dependent rod composition and Shs1-dependent assembly. Septin deletion often reduces rather than abolishes septation. |
| septin-p2348-septin-adapter-catalogue | https://imodulondb.org/api/datasets; Complete 20-organism / 28-dataset catalogue response; all organism names and dataset keys independently reread | context_only | Cached native catalogue has bacterial and archaeal organisms only; no organism/dataset key matches these fungal targets. Named genes make adapter discovery relevant under the rubric, but downstream organism-specific searches are not applicable after this bounded coverage check. Earlier runner PermissionError is a separate availability limitation, not the non-applicability basis. |
| check-qc | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2348/qc.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| check-labels | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2348/labels.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | 4232 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| check-trait-links | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2348/trait-links.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Native TraitMech link check passed. |
| check-vendored | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2348/vendored.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Pinned governed files match; native vendored check passed. |
| check-curies | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2348/curies.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| focused | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2348/focused-results.json; All twenty actual target schema/strict command outputs | supports | Ten schema and ten strict commands returned exit zero. |
| supplemental-pmid | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2348/pmid-chunks-receipt.json; Complete native-report PMID set checked with unchanged resolver in batches of at most fifty | supports | 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers remain unverified. |
| historical-adapter-runner-availability | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical runner invocation receipt, cross-checked against exact stdout/stderr hashes; reread during PR2348 synthesis | context_only | Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS PermissionError reading the configured runner pyvenv.cfg. This is a retained historical availability observation, not a fresh attempt or a scientific validation failure. Native policy permits inspected source-catalogue fallback. |

## Limits And Additional Notes

- Spindle pole body, duplication plaque and satellite independent subreview: Assigned SPB/duplication-plaque/satellite subreview only. Global QC, strict/identifier/label gates and CI are parent-owned; this report attests only the original-bundle native checks it executed.
- Spindle pole body, duplication plaque and satellite independent subreview: Adams1999 claim-bearing main-text Methods/Results/Discussion were read. Microscopy pixels, raw serial-section data, every temperature-sensitive mutant experiment and all historical antecedents were not independently reanalyzed. Stage inference is not single-structure lineage tracing.
- Spindle pole body, duplication plaque and satellite independent subreview: Viswanath2017 Introduction, selected modeling Results, Discussion and specified Methods were read. Raw models, microscopy pixels, all validation equations and full supplementary datasets were not independently rerun or reaudited.
- Spindle pole body, duplication plaque and satellite independent subreview: Jaspersen2004 is a secondary author manuscript read through browser extraction. The structure passage is reused from the actual 2026-11-03T00:47:42Z fetch and was re-read; duplication and nucleation passages were freshly retrieved. Browser receipt hashes are not publisher-PDF hashes or native HTTP status evidence.
- Spindle pole body, duplication plaque and satellite independent subreview: Winey2012 PMC OA S3 returned404. The alternate native PMC HTML route succeeded and its claim-bearing duplication/separation section was read. This access limit is resolved for the reviewed claims, not hidden or called a successful S3 retrieval.
- Spindle pole body, duplication plaque and satellite independent subreview: GO searches covered the first100 ID/name candidates for each exact query, on page1 of6. Remaining pages and every synonym were not exhaustively searched. No universal ontology-absence claim is made.
- Spindle pole body, duplication plaque and satellite independent subreview: Complex Portal entries are narrowly scoped contextual candidates. Their participant lists are not transplanted into the record as universal SPB composition; no individual protein example is asserted by any of these three target records.
- Spindle pole body, duplication plaque and satellite independent subreview: No new iModulonDB adapter CLI execution is claimed. The complete native catalogue was freshly retrieved and inspected; parent owns runner availability disclosure.
- Spindle pole body, duplication plaque and satellite independent subreview: No tracked images were present in the fully read targets, and no scientific neighbor beyond the assigned satellite target was used. All local input paths are enumerated; cached external-response bytes are evidence snapshots, not maintained repository inputs.
- SIN/MEN GAP complex, sinister fiber, spindle microtubule and Spirostomum myoneme independent subreview: All four assigned record inputs are unchanged. Fresh source retrieval receipts record actual UTC access and native bytes; no historical primary retrieval time is reused as a fresh download.
- SIN/MEN GAP complex, sinister fiber, spindle microtubule and Spirostomum myoneme independent subreview: GAP: inspected Fraschini claim-relevant sections and Methods listed in evidence, not all raw experimental data. Budding-yeast study does not directly verify every fission-yeast branch detail. No complete constituent inventory is asserted.
- SIN/MEN GAP complex, sinister fiber, spindle microtubule and Spirostomum myoneme independent subreview: Sinister: complete claim-bearing primary Results/Discussion and relevant Methods plus Figure5/7/8 pixels inspected. No raw microscopy data or unlisted supplement was inspected. Exact-family checks are bounded to one protein endpoint and three literal text queries; they are not exhaustive homology coverage.
- SIN/MEN GAP complex, sinister fiber, spindle microtubule and Spirostomum myoneme independent subreview: Spindle: Winey PDF selected claim-bearing sections were text-inspected; its figure pixels/raw tomography were not independently reinspected. Straight1997 is fresh abstract-only verification, not a new full-text read. Anders and Cederquist were inspected in the specified abstract/Results/Methods passages, not exhaustively. Jaspersen is secondary cached browser text, not fresh publisher full text or primary evidence.
- SIN/MEN GAP complex, sinister fiber, spindle microtubule and Spirostomum myoneme independent subreview: Spirostomum: Zhang2023 claim-bearing Results/Discussion/relevant Methods and Figure5 pixels were inspected. Versioned Lannan2024 main-text claim-relevant sections were inspected, but supplementary Methods/raw data and its figure pixels were not freshly inspected.
- SIN/MEN GAP complex, sinister fiber, spindle microtubule and Spirostomum myoneme independent subreview: Spirostomum final2026: the fresh native Europe PMC abstract supports only qualitative abstract-level claims. Europe PMC final fullTextXML returned500; PMC returned a200 browser challenge; publisher browsing returned403. No fresh embargo date, final Methods, final figures/supplement or quantitative condition was verified. The original reported embargo remains historical, not independently reproduced.
- SIN/MEN GAP complex, sinister fiber, spindle microtubule and Spirostomum myoneme independent subreview: Spirostomum: Mikus2025 PDF passages are secondary comparative context for Spirostomum, not new primary local evidence; the broader InterPro family descriptions do not establish exact local-component identities.
- SIN/MEN GAP complex, sinister fiber, spindle microtubule and Spirostomum myoneme independent subreview: Structured sources: fresh complete iModulonDB catalogue coverage was inspected; no matching organisms/datasets exist within that returned list. Runner availability is root-owned evidence. Lack of dataset coverage is not evidence against the biological assemblies.
- SIN/MEN GAP complex, sinister fiber, spindle microtubule and Spirostomum myoneme independent subreview: Original bundles: native validation and exact rendering were independently checked. Full corpus QC/identifier/label/history gates are run by root; this report does not relabel historical check results as fresh global checks.
- Septin collar, filament array and ring independent subreview: This independent slice covers only septin collar, septin filament array and septin ring; all source-access and image limitations below are scoped to those three targets.
- Septin collar, filament array and ring independent subreview: Three generic-family findings and the confirmed major sporulation-array composition finding remain open record curation; no record was edited and no historical scientific issue was closed.
- Septin collar, filament array and ring independent subreview: The filament-array finding concerns the stated S. cerevisiae sporulation/prospore context. It is not an exclusion of Cdc12 or Shs1 from every possible septin array. Cdc11 detection at PSM and membership of the reconstituted meiotic core are distinct and were not conflated.
- Septin collar, filament array and ring independent subreview: Primary McMurray 2008 Figure 3 was visually inspected with its caption and Results. Other article bodies and selected legends were inspected, but microscopy pixels, raw movies, supplements and quantitative analyses were not independently reanalyzed.
- Septin collar, filament array and ring independent subreview: The C. albicans chlamydospore array is corroborated at exact GO and Douglas secondary-review tiers. Its original microscopy was not reanalyzed. Tachikawa sheet geometry is measured on Gip1 with Spr28 colocalization, not direct single-filament resolution.
- Septin collar, filament array and ring independent subreview: Huh 2003, Finnigan 2015 and Mino 1998 were accessed at metadata/abstract and native-UniProt-attribution tier in this slice; no claim that their full primary bodies were reread.
- Septin collar, filament array and ring independent subreview: The changed septin-ring edge is accepted within its expressly budding-yeast descriptive hierarchy. Pairing and cortical architecture are corroborated by reconstitution plus secondary synthesis, without claiming new in-vivo imaging analysis, universal architecture or every paralog being individually essential.
- Septin collar, filament array and ring independent subreview: IPR016491, Douglas, Versele, Tachikawa and the official iModulonDB catalogue use independently reread cached native responses with actual earlier fetch times and hashes, not fresh retrieval claims.
- Septin collar, filament array and ring independent subreview: Seven Europe PMC XML requests returned HTTP 500 and alternate pdf=render routes returned browser-challenge HTML. Genuine PMC report=xml HTML provided all seven full bodies; failed/challenged bytes are not scientific evidence. A scratch HTML parser dependency was absent, so standard-library HTML parsing was used; no repository check failed.
- Septin collar, filament array and ring independent subreview: No new structured runner invocation was performed: root retains the canary runner PermissionError receipt. Downstream non-applicability rests on the bounded organism catalogue rather than lack of transcriptomic claims.
- Septin collar, filament array and ring independent subreview: Corpus QC, strict corpus resolvers and final-head CI are root-owned gates, not claimed as executed by this independent subreview. Original three bundle validation/render checks passed; historical check receipts are not relabeled as current.
- Historical observations remain immutable; their old checks are not represented as current-head execution.
- The adapter runner was not rerun after the canary established OS access failure. Catalogue-based coverage is assessed directly; fresh and reused responses retain actual access timestamps.
- Native label checks include 923 no-adapter skips. Native identifier checks include 909 PMID transport failures and 254 skipped identifiers; bounded supplemental checks independently resolve the 909 PMIDs.
- Scientific findings and native status are unchanged; proposed curation belongs in separate record PRs.
- Final trusted-base post-save review-check, exact-head independent acceptance, final-head CI and merge-group CI occur after saving this immutable observation and are not represented here as already completed.
- All ten original YAML/Markdown pairs are preserved unchanged. Current main was merged normally and pushed without force.
- One explicit issue-bearing ten-record cohort follows the repository persistence policy. Supported records are assessed within that cohort without fabricated findings.
- Bundle issues #2529 (stale septin-ring review) and #2532 (seven unsupported adapter exemption rationales) are addressed here. Scientific curation remains in #2499 (three same-class findings consolidated), #2530 and #2531; existing validator #2514 remains open.
- Source commit c5d2d7e40e573b342332ef2b1203de1089602637 is retained by tag review-base/pr2348-current-record-followup-20261103.
- CLAUDE.md is an alias of AGENTS.md; canonical regular AGENTS.md bytes are frozen.
- Every inherited source-access and check limitation is attributed to its independent subreview. Fresh fetches, cached response re-reading, abstract-only evidence and full-body passages retain distinct scopes.
- The seven original adapter checks exist; the repaired defect is their unsupported exemption rationale. The three sparse spindle-pole/plaque/satellite records are excluded from that defect.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T033249Z-pr2348-current-record-followup
kind: batch
repository: CultureBotAI/CellStructureMech
title: 'PR 2348: current-input review of ten records and adversarial follow-up'
started_at: '2026-11-03T03:18:37.622806Z'
finished_at: '2026-11-03T03:32:49Z'
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
summary: 'Current-input reassessment of all ten records in PR2348. The septin-ring
  input changed through an added filaments-to-ring/hourglass-collar edge and curation
  event; its new claim is substantively supported within the stated Saccharomyces
  descriptive scope. Six records have qualified supported assessments and four need
  curation. Five original scientific findings remain: four minor confirmed grounding
  gaps and one major confirmed sporulation-array membership conflict. The follow-up
  preserves exact finding lineage, refreshes the stale review and corrects structured-source
  applicability evidence for seven bundles; no scientific record is edited.'
source:
  git_revision: c5d2d7e40e573b342332ef2b1203de1089602637
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
  - path: data/structures/cytoskeleton/septin_collar.yaml
    sha256: c16f869099afaf1a608e229fb19f217583156684f4a7311549af622691b556d9
    role: target
  - path: data/structures/cytoskeleton/septin_filament_array.yaml
    sha256: 8413e81f4ac3c0daf46af8a81bbc0c819380242af370486f07865114e2edc1a0
    role: target
  - path: data/structures/cytoskeleton/septin_ring.yaml
    sha256: f536dd5b190f0cba77de3b14131a2bd5b9d12369a96c81014cc6b0c2ebf1361d
    role: target
  - path: data/structures/cytoskeleton/sin_men_two_component_gap_complex.yaml
    sha256: 922665d09fdb8ddf24c904aefc3ccd0ec99a36f92d4d33f71a42c732036ecbdd
    role: target
  - path: data/structures/cytoskeleton/sinister_fiber.yaml
    sha256: 9227477d7ba7b31e708bd60156ccb5d24f7051d3e0451b9138e6b3380d3664e5
    role: target
  - path: data/structures/cytoskeleton/spindle_microtubule.yaml
    sha256: bd8d435d59b948878bdcc978f015029ba6f6cc236b43eab0a5a5fe8b1a350fb9
    role: target
  - path: data/structures/cytoskeleton/spindle_pole_body.yaml
    sha256: 50885e021c246e17e29beb27f7dc98e37ee4d34878648fea4fd8b565bbb2fc78
    role: target
  - path: data/structures/cytoskeleton/spindle_pole_body_duplication_plaque.yaml
    sha256: e321abc96c81de9d3b524b7a68e2cefc4f28aaf72df105b42c96e1c6b8e994c3
    role: target
  - path: data/structures/cytoskeleton/spindle_pole_body_satellite.yaml
    sha256: a6a16f2dc3c09895fb7f4af93e1cad023c01b75dd424b99a1177ce93b516acb3
    role: target
  - path: data/structures/cytoskeleton/spirostomum_myoneme_fishnet.yaml
    sha256: 23c2668330bc68a88153d7ed54feb0a5626a88d4ae53a8da6e250d2dda8d71af
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
  - path: reviews/structured/20261021T082244Z-septin-collar-audit/review.md
    sha256: 9725685fd1df20ed9d00272dea2818c6719e51752c66cc1ad1f12d8b10ed77a3
    role: context
  - path: reviews/structured/20261021T082244Z-septin-collar-audit/review.yaml
    sha256: 715088fc531ecbabe37bb99faf0e951cfaaef8fcfb3fe6548f52d3d3e320d598
    role: context
  - path: reviews/structured/20261021T082244Z-septin-filament-array-audit/review.md
    sha256: 2bc970b8bd0289bb9e9005128e8dd9c7db0089736e07a684a8633951e917e5a8
    role: context
  - path: reviews/structured/20261021T082244Z-septin-filament-array-audit/review.yaml
    sha256: 3922fc327258cb43604cddcd327f130a6ddd281d3c6f3f7921561352546277a0
    role: context
  - path: reviews/structured/20261021T082244Z-septin-ring-audit/review.md
    sha256: 8e6828b38cc42360adba6547595c20c1f907c75646cd802cdef850b633bb275c
    role: context
  - path: reviews/structured/20261021T082244Z-septin-ring-audit/review.yaml
    sha256: 5fc821b506798ee2d9af059234dad7e4bbb57654c60b1849ee2f6f49cb8c1a09
    role: context
  - path: reviews/structured/20261021T082245Z-sin-men-two-component-gap-complex-audit/review.md
    sha256: 6eb5664e1f4d73ff9e79a92dc538ea0bb8b72ffe4645f43346d958fcd9ab24da
    role: context
  - path: reviews/structured/20261021T082245Z-sin-men-two-component-gap-complex-audit/review.yaml
    sha256: 6860dfe506571b094c545df1e9788141e3a9beab7a37e9399dc33fdb0b7c1d0a
    role: context
  - path: reviews/structured/20261021T082245Z-sinister-fiber-audit/review.md
    sha256: ef6d6fd08df34d9ac11eeed80aba5af0e05ff9006dff99de84db034d67a3fb47
    role: context
  - path: reviews/structured/20261021T082245Z-sinister-fiber-audit/review.yaml
    sha256: 5f0b624c9840228af1cb1478aecdb410f1b273d37dca272df12451f7fd7b52aa
    role: context
  - path: reviews/structured/20261021T082245Z-spindle-microtubule-audit/review.md
    sha256: ec3662417528cb3e57bda1d4d6146dbe5c2fa0a323ca3c9d1116ac846af9e310
    role: context
  - path: reviews/structured/20261021T082245Z-spindle-microtubule-audit/review.yaml
    sha256: ae4c7d5dcc6ab23b2804ff1ac023995cc0fb3de62f50272069de12b7371a979c
    role: context
  - path: reviews/structured/20261021T082245Z-spindle-pole-body-audit/review.md
    sha256: d68e9da58353b651dde9c8fbc882bd4bcf2717294fba796672a4ce9bdefa11e9
    role: context
  - path: reviews/structured/20261021T082245Z-spindle-pole-body-audit/review.yaml
    sha256: 7d7f26a2aeb08c643c27ca128ea45a0e2dd1d7a3b3582e9767865f7b88456947
    role: context
  - path: reviews/structured/20261021T082245Z-spindle-pole-body-duplication-plaque-audit/review.md
    sha256: 3d9f991f34d59d4bd1db9d7a13454fa17630c67fd85d7059ec95fd39db7f98c0
    role: context
  - path: reviews/structured/20261021T082245Z-spindle-pole-body-duplication-plaque-audit/review.yaml
    sha256: da1c1bdd413daa3e64a894c99dda9231da7d1bf98a5c560ea5c5ad2f9ff83e20
    role: context
  - path: reviews/structured/20261021T082245Z-spindle-pole-body-satellite-audit/review.md
    sha256: d37d7a5d3105a0eea4a8861a337b71f2098a928abea859e19998f4509abf06c1
    role: context
  - path: reviews/structured/20261021T082245Z-spindle-pole-body-satellite-audit/review.yaml
    sha256: ef4a65cacb87173863db0217fa05e9149da7a89cb6dbfadea9b70c2fa002773d
    role: context
  - path: reviews/structured/20261021T082245Z-spirostomum-myoneme-fishnet-audit/review.md
    sha256: 308e6433a745efbac51d52487a57465ec250a0377c82e2bb7ebbe3ff3b818344
    role: context
  - path: reviews/structured/20261021T082245Z-spirostomum-myoneme-fishnet-audit/review.yaml
    sha256: 53bbd7643fac6e1f80fdb8a31e2f00f0cf8ab87a385ff878cc9c82e00309d79b
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
targets:
- target_id: GO:0032173
  path: data/structures/cytoskeleton/septin_collar.yaml
  label: septin collar
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/septin_collar.yaml
    role: maintained scientific record
- target_id: GO:0032160
  path: data/structures/cytoskeleton/septin_filament_array.yaml
  label: septin filament array
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/septin_filament_array.yaml
    role: maintained scientific record
- target_id: GO:0005940
  path: data/structures/cytoskeleton/septin_ring.yaml
  label: septin ring
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/septin_ring.yaml
    role: maintained scientific record
- target_id: GO:1990334
  path: data/structures/cytoskeleton/sin_men_two_component_gap_complex.yaml
  label: SIN/MEN two-component GAP complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/sin_men_two_component_gap_complex.yaml
    role: maintained scientific record
- target_id: cellstructuremech:sinister_fiber
  path: data/structures/cytoskeleton/sinister_fiber.yaml
  label: sinister fiber
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/sinister_fiber.yaml
    role: maintained scientific record
- target_id: GO:0005876
  path: data/structures/cytoskeleton/spindle_microtubule.yaml
  label: spindle microtubule
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/spindle_microtubule.yaml
    role: maintained scientific record
- target_id: GO:0005816
  path: data/structures/cytoskeleton/spindle_pole_body.yaml
  label: spindle pole body
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/spindle_pole_body.yaml
    role: maintained scientific record
- target_id: cellstructuremech:spindle_pole_body_duplication_plaque
  path: data/structures/cytoskeleton/spindle_pole_body_duplication_plaque.yaml
  label: spindle pole body duplication plaque
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/spindle_pole_body_duplication_plaque.yaml
    role: maintained scientific record
- target_id: cellstructuremech:spindle_pole_body_satellite
  path: data/structures/cytoskeleton/spindle_pole_body_satellite.yaml
  label: spindle pole body satellite
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/spindle_pole_body_satellite.yaml
    role: maintained scientific record
- target_id: cellstructuremech:spirostomum_myoneme_fishnet
  path: data/structures/cytoskeleton/spirostomum_myoneme_fishnet.yaml
  label: Spirostomum myoneme fishnet
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/spirostomum_myoneme_fishnet.yaml
    role: maintained scientific record
scope:
  description: Exact ten-record PR cohort reassessed against current main d69b72e8b4ea6626144a1eddc245e73ee90f4227.
    Changed inputs are substantively reassessed. Scientific records remain unchanged.
  selection: Complete cohort of ten maintained records reviewed in original PR head
    b8d549b9b6ddb3fd81ed4a9d7f45ecfef3ccf48d.
  coverage: full
  population_size: 10
  reviewed_target_ids:
  - GO:0032173
  - GO:0032160
  - GO:0005940
  - GO:1990334
  - cellstructuremech:sinister_fiber
  - GO:0005876
  - GO:0005816
  - cellstructuremech:spindle_pole_body_duplication_plaque
  - cellstructuremech:spindle_pole_body_satellite
  - cellstructuremech:spirostomum_myoneme_fishnet
checks:
- check_id: qc
  name: Full native QC
  status: passed
  required: true
  target_ids:
  - GO:0032173
  - GO:0032160
  - GO:0005940
  - GO:1990334
  - cellstructuremech:sinister_fiber
  - GO:0005876
  - GO:0005816
  - cellstructuremech:spindle_pole_body_duplication_plaque
  - cellstructuremech:spindle_pole_body_satellite
  - cellstructuremech:spirostomum_myoneme_fishnet
  command: just qc
  exit_code: 0
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  scope_note: Actual local execution at main-merge head c5d2d7e40e573b342332ef2b1203de1089602637.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-qc
- check_id: labels
  name: Native label correspondence
  status: passed
  required: true
  target_ids:
  - GO:0032173
  - GO:0032160
  - GO:0005940
  - GO:1990334
  - cellstructuremech:sinister_fiber
  - GO:0005876
  - GO:0005816
  - cellstructuremech:spindle_pole_body_duplication_plaque
  - cellstructuremech:spindle_pole_body_satellite
  - cellstructuremech:spirostomum_myoneme_fishnet
  command: just validate-products
  exit_code: 0
  summary: 4232 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  scope_note: Actual local execution at main-merge head c5d2d7e40e573b342332ef2b1203de1089602637.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-labels
- check_id: trait-links
  name: TraitMech references
  status: passed
  required: true
  target_ids:
  - GO:0032173
  - GO:0032160
  - GO:0005940
  - GO:1990334
  - cellstructuremech:sinister_fiber
  - GO:0005876
  - GO:0005816
  - cellstructuremech:spindle_pole_body_duplication_plaque
  - cellstructuremech:spindle_pole_body_satellite
  - cellstructuremech:spirostomum_myoneme_fishnet
  command: just check-trait-links --check
  exit_code: 0
  summary: Native TraitMech link check passed.
  scope_note: Actual local execution at main-merge head c5d2d7e40e573b342332ef2b1203de1089602637.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-trait-links
- check_id: vendored
  name: Pinned governed files
  status: passed
  required: true
  target_ids:
  - GO:0032173
  - GO:0032160
  - GO:0005940
  - GO:1990334
  - cellstructuremech:sinister_fiber
  - GO:0005876
  - GO:0005816
  - cellstructuremech:spindle_pole_body_duplication_plaque
  - cellstructuremech:spindle_pole_body_satellite
  - cellstructuremech:spirostomum_myoneme_fishnet
  command: just vendored-check
  exit_code: 0
  summary: Pinned governed files match; native vendored check passed.
  scope_note: Actual local execution at main-merge head c5d2d7e40e573b342332ef2b1203de1089602637.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-vendored
- check_id: curies
  name: Native identifier resolver
  status: passed
  required: true
  target_ids:
  - GO:0032173
  - GO:0032160
  - GO:0005940
  - GO:1990334
  - cellstructuremech:sinister_fiber
  - GO:0005876
  - GO:0005816
  - cellstructuremech:spindle_pole_body_duplication_plaque
  - cellstructuremech:spindle_pole_body_satellite
  - cellstructuremech:spirostomum_myoneme_fishnet
  command: just check-curies-strict
  exit_code: 0
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  scope_note: Actual local execution at main-merge head c5d2d7e40e573b342332ef2b1203de1089602637.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-curies
- check_id: focused-0
  name: validate GO:0032173
  status: passed
  required: true
  target_ids:
  - GO:0032173
  command: just validate data/structures/cytoskeleton/septin_collar.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-1
  name: validate-strict GO:0032173
  status: passed
  required: true
  target_ids:
  - GO:0032173
  command: just validate-strict data/structures/cytoskeleton/septin_collar.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-2
  name: validate GO:0032160
  status: passed
  required: true
  target_ids:
  - GO:0032160
  command: just validate data/structures/cytoskeleton/septin_filament_array.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-3
  name: validate-strict GO:0032160
  status: passed
  required: true
  target_ids:
  - GO:0032160
  command: just validate-strict data/structures/cytoskeleton/septin_filament_array.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-4
  name: validate GO:0005940
  status: passed
  required: true
  target_ids:
  - GO:0005940
  command: just validate data/structures/cytoskeleton/septin_ring.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-5
  name: validate-strict GO:0005940
  status: passed
  required: true
  target_ids:
  - GO:0005940
  command: just validate-strict data/structures/cytoskeleton/septin_ring.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-6
  name: validate GO:1990334
  status: passed
  required: true
  target_ids:
  - GO:1990334
  command: just validate data/structures/cytoskeleton/sin_men_two_component_gap_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-7
  name: validate-strict GO:1990334
  status: passed
  required: true
  target_ids:
  - GO:1990334
  command: just validate-strict data/structures/cytoskeleton/sin_men_two_component_gap_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-8
  name: validate cellstructuremech:sinister_fiber
  status: passed
  required: true
  target_ids:
  - cellstructuremech:sinister_fiber
  command: just validate data/structures/cytoskeleton/sinister_fiber.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-9
  name: validate-strict cellstructuremech:sinister_fiber
  status: passed
  required: true
  target_ids:
  - cellstructuremech:sinister_fiber
  command: just validate-strict data/structures/cytoskeleton/sinister_fiber.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-10
  name: validate GO:0005876
  status: passed
  required: true
  target_ids:
  - GO:0005876
  command: just validate data/structures/cytoskeleton/spindle_microtubule.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-11
  name: validate-strict GO:0005876
  status: passed
  required: true
  target_ids:
  - GO:0005876
  command: just validate-strict data/structures/cytoskeleton/spindle_microtubule.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-12
  name: validate GO:0005816
  status: passed
  required: true
  target_ids:
  - GO:0005816
  command: just validate data/structures/cytoskeleton/spindle_pole_body.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-13
  name: validate-strict GO:0005816
  status: passed
  required: true
  target_ids:
  - GO:0005816
  command: just validate-strict data/structures/cytoskeleton/spindle_pole_body.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-14
  name: validate cellstructuremech:spindle_pole_body_duplication_plaque
  status: passed
  required: true
  target_ids:
  - cellstructuremech:spindle_pole_body_duplication_plaque
  command: just validate data/structures/cytoskeleton/spindle_pole_body_duplication_plaque.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-15
  name: validate-strict cellstructuremech:spindle_pole_body_duplication_plaque
  status: passed
  required: true
  target_ids:
  - cellstructuremech:spindle_pole_body_duplication_plaque
  command: just validate-strict data/structures/cytoskeleton/spindle_pole_body_duplication_plaque.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-16
  name: validate cellstructuremech:spindle_pole_body_satellite
  status: passed
  required: true
  target_ids:
  - cellstructuremech:spindle_pole_body_satellite
  command: just validate data/structures/cytoskeleton/spindle_pole_body_satellite.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-17
  name: validate-strict cellstructuremech:spindle_pole_body_satellite
  status: passed
  required: true
  target_ids:
  - cellstructuremech:spindle_pole_body_satellite
  command: just validate-strict data/structures/cytoskeleton/spindle_pole_body_satellite.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-18
  name: validate cellstructuremech:spirostomum_myoneme_fishnet
  status: passed
  required: true
  target_ids:
  - cellstructuremech:spirostomum_myoneme_fishnet
  command: just validate data/structures/cytoskeleton/spirostomum_myoneme_fishnet.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-19
  name: validate-strict cellstructuremech:spirostomum_myoneme_fishnet
  status: passed
  required: true
  target_ids:
  - cellstructuremech:spirostomum_myoneme_fishnet
  command: just validate-strict data/structures/cytoskeleton/spirostomum_myoneme_fishnet.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: supplemental-pmid
  name: Supplemental bounded PMID authority checks
  status: passed
  required: true
  target_ids:
  - GO:0032173
  - GO:0032160
  - GO:0005940
  - GO:1990334
  - cellstructuremech:sinister_fiber
  - GO:0005876
  - GO:0005816
  - cellstructuremech:spindle_pole_body_duplication_plaque
  - cellstructuremech:spindle_pole_body_satellite
  - cellstructuremech:spirostomum_myoneme_fishnet
  command: .venv/bin/python /private/tmp/cellstructure-batches-2346-2397-20261103/check_pmid_chunks.py
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2348
  exit_code: 0
  summary: 909 PMIDs all OK in bounded native requests; full-command limitations remain
    separate.
  evidence_ids:
  - supplemental-pmid
- check_id: structured-source-applicability
  name: Official structured-source catalogue coverage
  status: not_applicable
  required: false
  target_ids:
  - GO:0032173
  - GO:0032160
  - GO:0005940
  - GO:1990334
  - cellstructuremech:sinister_fiber
  - GO:0005876
  - GO:0005816
  - cellstructuremech:spindle_pole_body_duplication_plaque
  - cellstructuremech:spindle_pole_body_satellite
  - cellstructuremech:spirostomum_myoneme_fishnet
  summary: Official catalogue coverage contains 20 organisms and 28 datasets, all
    bacterial/archaeal; none matches this yeast/protist cohort. Fresh and independently
    reread cached catalogue responses retain actual access times and boundaries. The
    historical runner failure is documented separately; no new runner execution is
    claimed.
  evidence_ids:
  - plaque-spb-adapter-catalogue
  - micro-current-current-adapter-catalogue
  - septin-p2348-septin-adapter-catalogue
- check_id: independent-scientific-review
  name: Independent claim-level source review
  status: passed
  required: true
  target_ids:
  - GO:0032173
  - GO:0032160
  - GO:0005940
  - GO:1990334
  - cellstructuremech:sinister_fiber
  - GO:0005876
  - GO:0005816
  - cellstructuremech:spindle_pole_body_duplication_plaque
  - cellstructuremech:spindle_pole_body_satellite
  - cellstructuremech:spirostomum_myoneme_fishnet
  summary: Three read-only reviewers covered the complete ten-record cohort, including
    changed inputs, with explicit scientific findings and source-access limits. Final
    artifact/head acceptance occurs after saving.
  evidence_ids:
  - plaque-spb-agent-go
  - plaque-spb-agent-taxon
  - plaque-spb-agent-epmc
  - plaque-spb-agent-viswanath2017
  - plaque-spb-agent-CPX-1198
  - plaque-spb-agent-CPX-1420
  - plaque-spb-agent-adams1999
  - plaque-spb-adapter-catalogue
  - plaque-spb-agent-winey2012
  - plaque-spb-jaspersen-structure-cached
  - plaque-spb-jaspersen-duplication-fresh
  - plaque-spb-jaspersen-nucleation-fresh
  - plaque-curation-policy
  - micro-current-gap-prep-go
  - micro-current-gap-prep-tax-4932
  - micro-current-gap-prep-fraschini-meta
  - micro-current-gap-prep-fraschini-jats
  - micro-current-sinister-prep-go
  - micro-current-sinister-prep-tax-3192
  - micro-current-sinister-prep-O49944
  - micro-current-sinister-prep-strain
  - micro-current-sinister-prep-geimer-meta
  - micro-current-sinister-prep-geimer-s3
  - micro-current-sinister-prep-figure5
  - micro-current-sinister-prep-figure7
  - micro-current-sinister-prep-figure8
  - micro-current-interpro-family
  - micro-current-spindle-mt-prep-go
  - micro-current-spindle-mt-prep-tax-4932
  - micro-current-spindle-mt-prep-tax-559292
  - micro-current-spindle-mt-prep-winey-meta
  - micro-current-spindle-mt-prep-winey-s3
  - micro-current-spindle-mt-prep-straight-meta
  - micro-current-spindle-mt-prep-P09733
  - micro-current-spindle-mt-prep-P02557
  - micro-current-spindle-mt-prep-P09734
  - micro-current-spindle-mt-prep-anders-meta
  - micro-current-spindle-mt-prep-cederquist-meta
  - micro-current-spindle-mt-agent-anders2001
  - micro-current-spindle-mt-agent-cederquist2012
  - micro-current-jaspersen-secondary-context
  - micro-current-spirostomum-agent-zhang2023-jats
  - micro-current-spirostomum-agent-zhang2023-package
  - micro-current-spirostomum-agent-figure5
  - micro-current-spirostomum-agent-lannan2024-jats
  - micro-current-spirostomum-agent-lannan2024-package
  - micro-current-spirostomum-agent-epmc
  - micro-current-spirostomum-final2026-abstract
  - micro-current-spirostomum-agent-go
  - micro-current-spirostomum-agent-taxon-402029
  - micro-current-spirostomum-agent-taxon-37688
  - micro-current-spirostomum-agent-IPR050145
  - micro-current-spirostomum-agent-IPR052270
  - micro-current-spirostomum-agent-mikus2025-paper-pdf
  - septin-p2348-septin-collar-agent-go
  - septin-p2348-septin-collar-agent-family
  - septin-p2348-septin-collar-agent-paper-metadata
  - septin-p2348-septin-collar-agent-P32457
  - septin-p2348-septin-collar-agent-symbol-CDC3
  - septin-p2348-septin-collar-agent-P25342
  - septin-p2348-septin-collar-agent-symbol-CDC10
  - septin-p2348-septin-collar-agent-P32458
  - septin-p2348-septin-collar-agent-symbol-CDC11
  - septin-p2348-septin-collar-agent-P32468
  - septin-p2348-septin-collar-agent-symbol-CDC12
  - septin-p2348-septin-collar-agent-Q07657
  - septin-p2348-septin-collar-agent-symbol-SHS1
  - septin-p2348-septin-collar-agent-taxon-4932
  - septin-p2348-septin-collar-agent-taxon-559292
  - septin-p2348-septin-collar-agent-kozubowski2005-xml
  - septin-p2348-septin-collar-agent-versele-pmc
  - septin-p2348-septin-array-agent-taxon-5476
  - septin-p2348-septin-array-agent-douglas-pmc
  - septin-p2348-septin-array-agent-tachikawa2001
  - septin-p2348-septin-array-agent-mcmurray2008
  - septin-p2348-septin-array-agent-mcmurray2008-figure3
  - septin-p2348-septin-array-agent-garcia2016
  - septin-p2348-septin-ring-agent-taxon-4751
  - septin-p2348-septin-ring-agent-iwase2007-xml
  - septin-p2348-septin-ring-agent-bertin2008-xml
  - septin-p2348-septin-ring-agent-mcmurray2011-xml
  - septin-p2348-septin-ring-agent-glomb2016-xml
  - septin-p2348-septin-ring-agent-bridges2014-xml
  - septin-p2348-septin-ring-agent-vargas2016-xml
  - septin-p2348-septin-adapter-catalogue
- check_id: historical-adapter-runner
  name: Retained historical adapter runner availability
  status: unavailable
  required: false
  target_ids:
  - GO:0032173
  - GO:0032160
  - GO:0005940
  - GO:1990334
  - cellstructuremech:sinister_fiber
  - GO:0005876
  - cellstructuremech:spirostomum_myoneme_fishnet
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
evidence:
- evidence_id: current-record-0
  kind: record_content
  reference: data/structures/cytoskeleton/septin_collar.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T03:32:49Z'
  support: context_only
  summary: Original frozen SHA256 c16f869099afaf1a608e229fb19f217583156684f4a7311549af622691b556d9;
    current SHA256 c16f869099afaf1a608e229fb19f217583156684f4a7311549af622691b556d9.
    Record bytes unchanged since the original review.
  snapshot_sha256: c16f869099afaf1a608e229fb19f217583156684f4a7311549af622691b556d9
- evidence_id: original-review-0
  kind: prior_review
  reference: reviews/structured/20261021T082244Z-septin-collar-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T03:32:49Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 715088fc531ecbabe37bb99faf0e951cfaaef8fcfb3fe6548f52d3d3e320d598
- evidence_id: current-record-1
  kind: record_content
  reference: data/structures/cytoskeleton/septin_filament_array.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T03:32:49Z'
  support: context_only
  summary: Original frozen SHA256 8413e81f4ac3c0daf46af8a81bbc0c819380242af370486f07865114e2edc1a0;
    current SHA256 8413e81f4ac3c0daf46af8a81bbc0c819380242af370486f07865114e2edc1a0.
    Record bytes unchanged since the original review.
  snapshot_sha256: 8413e81f4ac3c0daf46af8a81bbc0c819380242af370486f07865114e2edc1a0
- evidence_id: original-review-1
  kind: prior_review
  reference: reviews/structured/20261021T082244Z-septin-filament-array-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T03:32:49Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 3922fc327258cb43604cddcd327f130a6ddd281d3c6f3f7921561352546277a0
- evidence_id: current-record-2
  kind: record_content
  reference: data/structures/cytoskeleton/septin_ring.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T03:32:49Z'
  support: context_only
  summary: Original frozen SHA256 a29add3311f4b53bf4b50c2ec527d5ef450cfff625eadd312324d625b8790b93;
    current SHA256 f536dd5b190f0cba77de3b14131a2bd5b9d12369a96c81014cc6b0c2ebf1361d.
    Changed record reassessed against current sources.
  snapshot_sha256: f536dd5b190f0cba77de3b14131a2bd5b9d12369a96c81014cc6b0c2ebf1361d
- evidence_id: original-review-2
  kind: prior_review
  reference: reviews/structured/20261021T082244Z-septin-ring-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T03:32:49Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 5fc821b506798ee2d9af059234dad7e4bbb57654c60b1849ee2f6f49cb8c1a09
- evidence_id: current-record-3
  kind: record_content
  reference: data/structures/cytoskeleton/sin_men_two_component_gap_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T03:32:49Z'
  support: context_only
  summary: Original frozen SHA256 922665d09fdb8ddf24c904aefc3ccd0ec99a36f92d4d33f71a42c732036ecbdd;
    current SHA256 922665d09fdb8ddf24c904aefc3ccd0ec99a36f92d4d33f71a42c732036ecbdd.
    Record bytes unchanged since the original review.
  snapshot_sha256: 922665d09fdb8ddf24c904aefc3ccd0ec99a36f92d4d33f71a42c732036ecbdd
- evidence_id: original-review-3
  kind: prior_review
  reference: reviews/structured/20261021T082245Z-sin-men-two-component-gap-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T03:32:49Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 6860dfe506571b094c545df1e9788141e3a9beab7a37e9399dc33fdb0b7c1d0a
- evidence_id: current-record-4
  kind: record_content
  reference: data/structures/cytoskeleton/sinister_fiber.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T03:32:49Z'
  support: context_only
  summary: Original frozen SHA256 9227477d7ba7b31e708bd60156ccb5d24f7051d3e0451b9138e6b3380d3664e5;
    current SHA256 9227477d7ba7b31e708bd60156ccb5d24f7051d3e0451b9138e6b3380d3664e5.
    Record bytes unchanged since the original review.
  snapshot_sha256: 9227477d7ba7b31e708bd60156ccb5d24f7051d3e0451b9138e6b3380d3664e5
- evidence_id: original-review-4
  kind: prior_review
  reference: reviews/structured/20261021T082245Z-sinister-fiber-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T03:32:49Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 5f0b624c9840228af1cb1478aecdb410f1b273d37dca272df12451f7fd7b52aa
- evidence_id: current-record-5
  kind: record_content
  reference: data/structures/cytoskeleton/spindle_microtubule.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T03:32:49Z'
  support: context_only
  summary: Original frozen SHA256 bd8d435d59b948878bdcc978f015029ba6f6cc236b43eab0a5a5fe8b1a350fb9;
    current SHA256 bd8d435d59b948878bdcc978f015029ba6f6cc236b43eab0a5a5fe8b1a350fb9.
    Record bytes unchanged since the original review.
  snapshot_sha256: bd8d435d59b948878bdcc978f015029ba6f6cc236b43eab0a5a5fe8b1a350fb9
- evidence_id: original-review-5
  kind: prior_review
  reference: reviews/structured/20261021T082245Z-spindle-microtubule-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T03:32:49Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: ae4c7d5dcc6ab23b2804ff1ac023995cc0fb3de62f50272069de12b7371a979c
- evidence_id: current-record-6
  kind: record_content
  reference: data/structures/cytoskeleton/spindle_pole_body.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T03:32:49Z'
  support: context_only
  summary: Original frozen SHA256 50885e021c246e17e29beb27f7dc98e37ee4d34878648fea4fd8b565bbb2fc78;
    current SHA256 50885e021c246e17e29beb27f7dc98e37ee4d34878648fea4fd8b565bbb2fc78.
    Record bytes unchanged since the original review.
  snapshot_sha256: 50885e021c246e17e29beb27f7dc98e37ee4d34878648fea4fd8b565bbb2fc78
- evidence_id: original-review-6
  kind: prior_review
  reference: reviews/structured/20261021T082245Z-spindle-pole-body-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T03:32:49Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 7d7f26a2aeb08c643c27ca128ea45a0e2dd1d7a3b3582e9767865f7b88456947
- evidence_id: current-record-7
  kind: record_content
  reference: data/structures/cytoskeleton/spindle_pole_body_duplication_plaque.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T03:32:49Z'
  support: context_only
  summary: Original frozen SHA256 e321abc96c81de9d3b524b7a68e2cefc4f28aaf72df105b42c96e1c6b8e994c3;
    current SHA256 e321abc96c81de9d3b524b7a68e2cefc4f28aaf72df105b42c96e1c6b8e994c3.
    Record bytes unchanged since the original review.
  snapshot_sha256: e321abc96c81de9d3b524b7a68e2cefc4f28aaf72df105b42c96e1c6b8e994c3
- evidence_id: original-review-7
  kind: prior_review
  reference: reviews/structured/20261021T082245Z-spindle-pole-body-duplication-plaque-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T03:32:49Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: da1c1bdd413daa3e64a894c99dda9231da7d1bf98a5c560ea5c5ad2f9ff83e20
- evidence_id: current-record-8
  kind: record_content
  reference: data/structures/cytoskeleton/spindle_pole_body_satellite.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T03:32:49Z'
  support: context_only
  summary: Original frozen SHA256 a6a16f2dc3c09895fb7f4af93e1cad023c01b75dd424b99a1177ce93b516acb3;
    current SHA256 a6a16f2dc3c09895fb7f4af93e1cad023c01b75dd424b99a1177ce93b516acb3.
    Record bytes unchanged since the original review.
  snapshot_sha256: a6a16f2dc3c09895fb7f4af93e1cad023c01b75dd424b99a1177ce93b516acb3
- evidence_id: original-review-8
  kind: prior_review
  reference: reviews/structured/20261021T082245Z-spindle-pole-body-satellite-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T03:32:49Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: ef4a65cacb87173863db0217fa05e9149da7a89cb6dbfadea9b70c2fa002773d
- evidence_id: current-record-9
  kind: record_content
  reference: data/structures/cytoskeleton/spirostomum_myoneme_fishnet.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T03:32:49Z'
  support: context_only
  summary: Original frozen SHA256 23c2668330bc68a88153d7ed54feb0a5626a88d4ae53a8da6e250d2dda8d71af;
    current SHA256 23c2668330bc68a88153d7ed54feb0a5626a88d4ae53a8da6e250d2dda8d71af.
    Record bytes unchanged since the original review.
  snapshot_sha256: 23c2668330bc68a88153d7ed54feb0a5626a88d4ae53a8da6e250d2dda8d71af
- evidence_id: original-review-9
  kind: prior_review
  reference: reviews/structured/20261021T082245Z-spirostomum-myoneme-fishnet-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T03:32:49Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 53bbd7643fac6e1f80fdb8a31e2f00f0cf8ab87a385ff878cc9c82e00309d79b
- evidence_id: plaque-spb-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005816,GO:0032991,GO:0005825,GO:0008274,GO:0008275,GO:0000930
  locator: results selected by exact IDs; definition, isObsolete, synonyms and child
    relations; only the explicitly described returned definitions inform this review;
    fresh source bytes at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2348/adversary-plaque/spb-agent-go.source
  accessed_at: '2026-11-03T03:21:00.970776Z'
  support: supports
  summary: Active GO:0005816 exactly identifies the fungal MTOC and has SPB as an
    exact synonym. GO:0005825 denotes the distinct half bridge and is a part_of child
    of SPB. GO:0032991 denotes protein-containing complex. GO:0000930 directly identifies
    the broad gamma-tubulin complex class, with small and ring subtype children GO:0008275
    and GO:0000931; narrower subtype uncertainty does not prevent grounding the existing
    broad row.
  snapshot_sha256: 0351bb754bafd4c13ddd0abfa8da47ccb2146941d3c3457e7f28ce368ed12bc8
- evidence_id: plaque-spb-agent-taxon
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: taxId, scientificName, rank and lineage; fresh source bytes at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2348/adversary-plaque/spb-agent-taxon.source
  accessed_at: '2026-11-03T03:21:00.971025Z'
  support: supports
  summary: NCBITaxon4932 is Saccharomyces cerevisiae at species rank. The record does
    not assert a particular experimental strain or quantitative prevalence.
  snapshot_sha256: 38f43dd1593a1d47416228ae385464f30aeb8302c3aadb45b3588d03744bc814
- evidence_id: plaque-spb-agent-epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1146/annurev.cellbio.20.022003.114106%22%20OR%20DOI%3A%2210.1091/mbc.E17-06-0397%22%20OR%20DOI%3A%2210.1083/jcb.145.4.809%22%20OR%20DOI%3A%2210.1534/genetics.111.128710%22
  locator: 'Four native resultList.result entries: DOI, title, authorString, pubYear,
    PMID, PMCID, abstractText and pubTypeList; fresh source bytes at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2348/adversary-plaque/spb-agent-epmc.source'
  accessed_at: '2026-11-03T03:21:00.971089Z'
  support: supports
  summary: 'Exact citation identities are verified: Jaspersen/Winey2004 PMID15473833;
    Viswanath2017 PMID28814505/PMC5687031; Adams/Kilmartin1999 PMID10330408/PMC2133189;
    Winey/Bloom2012 PMID22491889/PMC3316638. The 2004 and 2012 bodies synthesize previous
    work; generic database publication-type tags do not make the 2012 review a new
    experiment.'
  snapshot_sha256: b5f8b5ee728d7d86a38409b23183ea83856839834ed5f3d9658d4390873ae906
- evidence_id: plaque-spb-agent-viswanath2017
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5687031.1/PMC5687031.1.xml
  locator: 'Native JATS: Introduction/Figure1 caption; Results Gathering of data,
    Representations and restraints, Initial models, single-layer Spc29 test, reduced-Spc29
    architecture; Discussion; Methods Composition and stoichiometry, In vivo FRET
    and System representation. Selected claim-bearing main-text sections read, not
    all Methods/supplements. /private/tmp/cellstructure-batches-2346-2397-20261103/pr2348/adversary-plaque/spb-agent-viswanath2017.source'
  accessed_at: '2026-11-03T03:21:00.971515Z'
  support: supports
  summary: Primary integrative modeling concerns the CP/IL2 core and portions of Spc42,
    Spc29, Spc110, Cmd1 and Cnm67, combining crystallography, SAXS, FRET and EM information.
    K. lactis calmodulin supplied the crystal constraint; in vivo FRET concerns S.
    cerevisiae. Tagged EM rejected the initial two-layer Spc29 model. Reduced core
    Spc29 stoichiometry, a possible peripheral pool and proposed calmodulin domain
    swaps remain model interpretations. The current record makes no fixed copy-count,
    whole-SPB atomic-structure or purified-assembly-sufficiency claim.
  snapshot_sha256: 004836a027b7fad21def4f6e9eebc94ec5f1e07679d123407a062241f6edb580
- evidence_id: plaque-spb-agent-CPX-1198
  kind: database
  reference: https://www.ebi.ac.uk/intact/complex-ws/complex/CPX-1198
  locator: complexAc, name, species, systematicName, participants, functions and properties;
    original receipt; fresh source bytes at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2348/adversary-plaque/spb-agent-CPX-1198.source
  accessed_at: '2026-11-03T03:21:00.971650Z'
  support: context_only
  summary: Native CPX1198 denotes the Saccharomyces cerevisiae gamma-tubulin small
    complex (taxon559292), a species-specific assembly with Tub4/Spc97/Spc98 and nucleotide
    participants. It is a candidate subassembly rather than identity for the whole
    SPB or every gamma-tubulin complex. Its narrower scope is not needed to establish
    the GO0000930 match.
  snapshot_sha256: 6ad8b7dadcc915c04c213a08278cb1695d5f089b126afc38b2817a1aa56ca860
- evidence_id: plaque-spb-agent-CPX-1420
  kind: database
  reference: https://www.ebi.ac.uk/intact/complex-ws/complex/CPX-1420
  locator: complexAc, name, species, systematicName and properties; fresh source bytes
    at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2348/adversary-plaque/spb-agent-CPX-1420.source
  accessed_at: '2026-11-03T03:21:00.978418Z'
  support: context_only
  summary: CPX1420 denotes the Saccharomyces cerevisiae intermediate-layer-2 complex
    (taxon559292) with Spc42/Cnm67. Its scope does not identify the entire CP/IL2
    core or whole SPB.
  snapshot_sha256: f323ad1b133af230458960bed57f117f466742411055b27524379ba1f070cf29
- evidence_id: plaque-spb-agent-adams1999
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2133189.1/PMC2133189.1.xml
  locator: 'Native PMC OA JATS: Methods Yeast Strains and ImmunoEM; Results EM of
    SPB Duplication, Main Components of the SPB Core, Approximate Arrangement, Components
    of Satellite/Duplication Plaque/Half-Bridge, and altered-NLS Spc110 overexpression;
    Discussion. Main-text source descriptions of Figures1/3/4/6/8/9 read; no pixel
    reanalysis. /private/tmp/cellstructure-batches-2346-2397-20261103/pr2348/adversary-plaque/spb-agent-adams1999.source'
  accessed_at: '2026-11-03T03:21:01.979410Z'
  support: supports
  summary: Primary serial EM of alpha-factor-released budding yeast identifies cytoplasmic
    duplication plaques, partial insertion and later paired SPBs. ImmunoEM directly
    localizes Spc42/Nud1 to both satellite and plaque, Cnm67 less consistently to
    satellite, and Spc29 directly to satellite; plaque Spc29 is inferred with mps2-1
    fluorescence support. Spc72/Tub4 half-bridge localization is not uniform satellite
    incorporation. Spc110 is detected after insertion. Shared composition/morphology
    suggest a precursor-product relationship rather than direct lineage tracing. K699/K842
    derivatives, fixation sensitivity, tagging and multiple Spc42-GFP copies bound
    interpretation. Delta-NLS Spc110 perturbation supports disrupted attachment; retraction/binding
    mechanisms remain models.
  snapshot_sha256: 792c1ee51beceedd27bea97a3811215d102430f55ca147e7f051e9a0eb315c34
- evidence_id: plaque-spb-agent-go-duplication-search
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=spindle%20pole%20body%20duplication%20plaque&limit=100
  locator: Native results page1; 100 candidates read by ID and name; numberOfHits=551
    with six total pages; exact query is retained in reference.; fresh source bytes
    at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2348/adversary-plaque/spb-agent-go-duplication-search.source
  accessed_at: '2026-11-03T03:21:02.065197Z'
  support: context_only
  summary: No exact SPB duplication plaque cellular-component label occurs among the
    first100 returned native search candidates. Mature SPB, its named plaques, half
    bridge and duplication processes have distinct meanings. This supports retaining
    the local identity within the bounded search, not an exhaustive assertion of ontology
    absence.
  snapshot_sha256: f53739175547a6be6e3db9a2ea0f87f2d3e1653604eb3e8ec92f5f78ab06c883
  search_scope: Remote QuickGO query spindle pole body duplication plaque, page1 with
    limit100; first100 result names/IDs and relevant native definitions inspected.
    Remaining pages not exhaustively searched. Ignored-file inclusion is not applicable
    to this remote query; no local-file absence is inferred. Actual fresh request
    date 2026-11-03 UTC, exact request timestamp 2026-11-03T03:21:02.065197Z.
- evidence_id: plaque-spb-agent-go-satellite-search
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=spindle%20pole%20body%20satellite&limit=100
  locator: Native results page1; 100 candidates read by ID and name; numberOfHits=564
    with six total pages; exact query is retained in reference.; fresh source bytes
    at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2348/adversary-plaque/spb-agent-go-satellite-search.source
  accessed_at: '2026-11-03T03:21:02.174770Z'
  support: context_only
  summary: No exact SPB satellite cellular-component label occurs among the first100
    returned native search candidates. Mature SPB, its named plaques, half bridge
    and duplication processes have distinct meanings. This supports retaining the
    local identity within the bounded search, not an exhaustive assertion of ontology
    absence.
  snapshot_sha256: d9e24b9ec9b93913380a942eb15dcd8c920f109b97cd91f4483e82c39f581f71
  search_scope: Remote QuickGO query spindle pole body satellite, page1 with limit100;
    first100 result names/IDs and relevant native definitions inspected. Remaining
    pages not exhaustively searched. Ignored-file inclusion is not applicable to this
    remote query; no local-file absence is inferred. Actual fresh request date 2026-11-03
    UTC, exact request timestamp 2026-11-03T03:21:02.174770Z.
- evidence_id: plaque-spb-adapter-catalogue
  kind: database
  reference: https://imodulondb.org/api/datasets
  accessed_at: '2026-11-03T03:21:02.287813Z'
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  locator: Complete native organism/dataset catalogue; fresh source bytes at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2348/adversary-plaque/spb-adapter-catalogue.source
  support: supports
  summary: Complete fresh native catalogue contains 20 organism entries and 28 datasets,
    all bacterial or archaeal; no Saccharomyces dataset is available. Organism-specific
    searches are not applicable. This is catalogue coverage evidence, not negative
    biological evidence; no new adapter CLI execution is claimed.
- evidence_id: plaque-spb-agent-winey2012
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3316638/?report=xml
  locator: Native PMC HTML section Spindle pole duplication and separation, Figure7
    caption and adjacent insertion/maturation/bridge-separation paragraphs; this is
    a secondary review. /private/tmp/cellstructure-batches-2346-2397-20261103/pr2348/adversary-plaque/winey2012-pmc.source
  accessed_at: '2026-11-03T03:22:25.729732Z'
  snapshot_sha256: d2033eadfad2dd4a9391af9d79d55c3671f61ddf3c56e600e54bb05ece228034
  support: supports
  summary: The literature synthesis identifies satellite-bearing SPBs in cycling cells
    as a normal intermediate; duplication-plaque growth and nuclear-envelope insertion
    can overlap. Nuclear-face maturation and later bridge separation yield the two
    spindle poles. Mechanism of membrane fenestration remains unresolved in this synthesis.
    This is a successfully inspected native HTML alternative after the PMC OA S3 route
    returned404, not a claim that the 2012 review reports a new experiment.
- evidence_id: plaque-spb-jaspersen-structure-cached
  kind: authority
  reference: https://www.researchgate.net/publication/8241691_THE_BUDDING_YEAST_SPINDLE_POLE_BODY_Structure_Duplication_and_Function
  locator: Re-read retained browser extraction lines187-487 (author-manuscript pp5-12),
    structural layers/core/half-bridge sections. Serialized browser receipt /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-plaque/paper2004-browser.json
  accessed_at: '2026-11-03T00:47:42Z'
  snapshot_sha256: e027d82955a859cb483e7800eefbf4424e4e27a4f4cc538fdfc7156388bb3f35
  support: supports
  summary: Secondary review describes the layered SPB scaffold and distinct half bridge.
    Cached browser text was re-read for these exact records; the original 00:47:42Z
    access time is retained. Hash binds the serialized browser receipt, not publisher
    PDF or native HTTP response bytes.
- evidence_id: plaque-spb-jaspersen-duplication-fresh
  kind: authority
  reference: https://www.researchgate.net/publication/8241691_THE_BUDDING_YEAST_SPINDLE_POLE_BODY_Structure_Duplication_and_Function
  locator: 'Author-manuscript pp15-20, browser lines619-800: Duplication Pathway,
    Separation and conservative/semi-conservative discussion. Fresh serialized browser
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2348/adversary-plaque/jaspersen-duplication-browser.json;
    not native HTTP/PDF bytes.'
  accessed_at: '2026-11-03T03:21:26Z'
  snapshot_sha256: 23b9123df392c877d66ffe268f5ef28ab1c96489ef0d94a32dfe3dccd96cc8bb
  support: supports
  summary: Secondary synthesis describes distal satellite formation, expanded duplication
    plaque, envelope insertion and nuclear-component recruitment, followed by bridge
    severing/separation. Molecular fusion/retraction and strict conservative inheritance
    are not established by the descriptive sequence.
- evidence_id: plaque-spb-jaspersen-nucleation-fresh
  kind: authority
  reference: https://www.researchgate.net/publication/8241691_THE_BUDDING_YEAST_SPINDLE_POLE_BODY_Structure_Duplication_and_Function
  locator: 'Author-manuscript pp24-26, browser lines978-1073: Microtubule Nucleation
    and spindle assembly. Fresh serialized browser response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2348/adversary-plaque/jaspersen-nucleation-browser.json;
    not native HTTP/PDF bytes.'
  accessed_at: '2026-11-03T03:21:32Z'
  snapshot_sha256: ad795ab14e979592b4ee453d8ed177591fe26cb81983611d48dc74be2f78cc53
  support: supports
  summary: Secondary synthesis places gamma-tubulin complexes on both SPB faces through
    Spc110/Spc72 and distinguishes associated nucleators from alpha/beta polymers.
    Low nucleation by isolated soluble complexes does not establish autonomous scaffold
    or universal isolated-complex sufficiency.
- evidence_id: plaque-current-0
  kind: record_content
  reference: data/structures/cytoskeleton/spindle_pole_body.yaml
  locator: Entire maintained current YAML at c5d2d7e40e573b342332ef2b1203de1089602637;
    unchanged from historical review target input
  accessed_at: '2026-11-03T03:26:12.090291Z'
  snapshot_sha256: 50885e021c246e17e29beb27f7dc98e37ee4d34878648fea4fd8b565bbb2fc78
  support: context_only
  summary: Complete target was read. Definitions, components, functions, graph edges,
    discussions and history assessed. No maintained content was changed.
- evidence_id: plaque-current-1
  kind: record_content
  reference: data/structures/cytoskeleton/spindle_pole_body_duplication_plaque.yaml
  locator: Entire maintained current YAML at c5d2d7e40e573b342332ef2b1203de1089602637;
    unchanged from historical review target input
  accessed_at: '2026-11-03T03:26:12.090291Z'
  snapshot_sha256: e321abc96c81de9d3b524b7a68e2cefc4f28aaf72df105b42c96e1c6b8e994c3
  support: context_only
  summary: Complete target was read. Definitions, components, functions, graph edges,
    discussions and history assessed. No maintained content was changed.
- evidence_id: plaque-current-2
  kind: record_content
  reference: data/structures/cytoskeleton/spindle_pole_body_satellite.yaml
  locator: Entire maintained current YAML at c5d2d7e40e573b342332ef2b1203de1089602637;
    unchanged from historical review target input
  accessed_at: '2026-11-03T03:26:12.090291Z'
  snapshot_sha256: a6a16f2dc3c09895fb7f4af93e1cad023c01b75dd424b99a1177ce93b516acb3
  support: context_only
  summary: Complete target was read. Definitions, components, functions, graph edges,
    discussions and history assessed. No maintained content was changed.
- evidence_id: plaque-curation-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Identity, Components, Evidence and scientific-status requirements
  accessed_at: '2026-11-03T03:26:12.090291Z'
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
  support: context_only
  summary: Use exact GO structural identity when available, justify label-only grounding,
    preserve experimental scope and keep review separate from curation. Empty optional
    inventory alone is not a defect.
- evidence_id: plaque-native-original-checks
  kind: validation
  reference: scripts/record_review.py
  locator: Independent validate/render commands and source input git-show comparisons;
    actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2348/adversary-plaque/native-original-checks.json
  accessed_at: '2026-11-03T03:26:12.090291Z'
  snapshot_sha256: eb587be7f98993dc771b38e9e2e2f0206bb7e616882bf2a3b46605d49d1dfffb
  support: supports
  summary: All three original bundles validate; their Markdown is byte-identical to
    native render --content. Every frozen historical input matches its recorded source
    revision. Target hashes are unchanged on current main-merge head.
- evidence_id: micro-current-gap-prep-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005816,GO:0160065,GO:0160066,GO:0160067,GO:1902773,GO:1990334
  locator: results for GO:0005816, GO:0160065, GO:0160066, GO:0160067, GO:1902773
    and GO:1990334; id/name/isObsolete/definition/synonyms/children
  accessed_at: '2026-11-03T03:20:47.346418Z'
  snapshot_sha256: 3133574ce154c8126caa7b82bc59568161c6f40a112272c815a096bee1649b49
  support: supports
  summary: Active exact GAP identity and narrow Bfa1-Bub2/Byr4-Cdc16 synonyms; appropriate
    GAP-complex is-a and spindle-pole-body parthood. Broader SIN/MEN complex and its
    inhibited/active state terms remain distinct.
- evidence_id: micro-current-gap-prep-tax-4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: ENA scientificName and taxonId for NCBITaxon:4932
  accessed_at: '2026-11-03T03:20:47.346783Z'
  snapshot_sha256: 38f43dd1593a1d47416228ae385464f30aeb8302c3aadb45b3588d03744bc814
  support: supports
  summary: Saccharomyces cerevisiae is the species-level example.
- evidence_id: micro-current-gap-prep-fraschini-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1083/jcb.200507162
  locator: 'Single DOI-matched Europe PMC result: title, DOI, PMID, PMCID'
  accessed_at: '2026-11-03T03:20:47.346884Z'
  snapshot_sha256: aea83395478966ebf4f2213466cc9fe1675c98063826c6c43a496cc52c87e63b
  support: supports
  summary: DOI 10.1083/jcb.200507162 resolves to Fraschini et al., PMID 16449187 /
    PMC2063644; citation identity only.
- evidence_id: micro-current-gap-prep-fraschini-jats
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2063644/fullTextXML
  locator: Introduction sec1; GAP assays and Fig5 in sec6; Discussion sec9–11 and
    Fig7 model; strains sec13; GTPase assay Methods sec16
  accessed_at: '2026-11-03T03:20:47.346993Z'
  snapshot_sha256: fc4658c387e9fb9fe12f46b3bf8bb6679cdc3ab33ad9b816e4f0992274e2e18b
  support: supports
  summary: Budding-yeast Bfa1-Bub2 restrains Tem1-dependent mitotic exit. Bfa1 stabilizes
    Tem1-bound GTP and supports Bub2 hydrolysis; checkpoint and localization phenotypes
    show that checkpoint control is not reducible to a single exclusive hydrolysis
    mechanism. W303-derived strains, in vitro assays and mutant/localization experiments
    support the record’s bounded claim; this is not direct experimental evidence for
    the fission-yeast branch.
- evidence_id: micro-current-sinister-prep-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005856,GO:0043232,GO:0120103
  locator: GO:0005856, GO:0043232 and GO:0120103 definitions and active status
  accessed_at: '2026-11-03T03:20:47.347078Z'
  snapshot_sha256: f31472cddab5dd37195121f9c780e76e466b7bade1da5116487beb7e51b629bd
  support: supports
  summary: Cytoskeleton parthood and broad intracellular non-membrane-bounded organelle
    parent are compatible. Mother-centriole subdistal appendage is not an exact identity
    for the two differently placed sinister fibers.
- evidence_id: micro-current-sinister-prep-tax-3192
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3192
  locator: ENA taxonId and scientificName
  accessed_at: '2026-11-03T03:20:47.347135Z'
  snapshot_sha256: a4a0ba510059ca136c43e8c2d1bc99b8e3e92102e5ad9deadbaaf1454b56e64b
  support: supports
  summary: NCBITaxon:3192 identifies Spermatozopsis similis.
- evidence_id: micro-current-sinister-prep-O49944
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/O49944.json
  locator: entryType, proteinDescription, organism, sequence length, EMBL cross-reference
  accessed_at: '2026-11-03T03:20:48.133940Z'
  snapshot_sha256: db6df16bdb9d2c0b88a960c7791bfbfd5e5ce4597ffa61ad825f1abb2a145554
  support: supports
  summary: O49944 is an unreviewed 834-aa S. similis 95 kD basal apparatus-protein
    entry with AJ001438 / CAA04763.1 correspondence. Sequence identity does not prove
    all members of a broad coiled-coil family are sinister-fiber constituents.
- evidence_id: micro-current-sinister-prep-strain
  kind: authority
  reference: https://sagdb.uni-goettingen.de/detailedList.php?str_number=1.85
  locator: SAG culture 1.85; species and sequence-reference table
  accessed_at: '2026-11-03T03:20:48.139996Z'
  snapshot_sha256: 917c9376c21f51f4c5f9fddd81df2456311452dfe38e4b89aab4df25d6c10cc8
  support: supports
  summary: Current SAG 1.85 culture entry identifies S. similis and lists AJ001438;
    historical B1.85 spelling occurs in other sequence metadata on this culture page.
    The AJ001438 row itself is not claimed to contain the historical spelling.
- evidence_id: micro-current-sinister-prep-geimer-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1083/jcb.140.5.1149
  locator: DOI-matched Europe PMC result identity
  accessed_at: '2026-11-03T03:20:48.210832Z'
  snapshot_sha256: 8d2dde383931e9b916fc3f1f0faab47b719c1b11659180ba42156f50e974b830
  support: supports
  summary: 10.1083/jcb.140.5.1149 identifies the Geimer et al. 1998 primary study
    and PMC2132688.
- evidence_id: micro-current-sinister-prep-geimer-s3
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2132688.1/PMC2132688.1.xml
  locator: Claim-bearing Results on cloning, recombinant reassembly and immunogold/native
    architecture; Discussion; relevant culture, recombinant purification, dialysis,
    antibody and microscopy Methods; figure captions and permissions
  accessed_at: '2026-11-03T03:20:48.262681Z'
  snapshot_sha256: 08fbbc9f099d1f64182b5dcb8cb683299836f01dc2300a093c290ed0156bcf41
  support: supports
  summary: Anti-rec95 specificity and controls support BAp95 as a sinister-fiber constituent.
    Recombinant BAp95 assembles patterned fibers after the stated urea-removal protocol;
    larger/high-concentration aggregates differ. Native older- and younger-basal-body
    linkers attach to a five-microtubule root. Proposed physiological and assembly-intermediate
    interpretations remain hypotheses, and native essentiality is untested. JATS carries
    CC BY-NC-SA 4.0 permissions.
- evidence_id: micro-current-sinister-prep-figure5
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2132688.1/JCB15053.f5.jpg
  locator: Figure5 panels a–g, visually inspected
  accessed_at: '2026-11-03T03:20:48.688460Z'
  snapshot_sha256: 1317f6975ea6f44f192719fcfae14f692b1caa24c902389bc369f7815284a640
  support: supports
  summary: Reassembled banded fibers in panels a–e differ from the larger spindle-shaped
    aggregates in f–g; supports the explicitly bounded in vitro reassembly claim.
- evidence_id: micro-current-sinister-prep-figure7
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2132688.1/JCB15053.f7.jpg
  locator: Figure7 panels a–i, visually inspected with JATS caption
  accessed_at: '2026-11-03T03:20:48.301406Z'
  snapshot_sha256: 363e493a65cb47436d260ffdeb373dd9f8ed7b77e4d3c4e48e16c773e338bd8a
  support: supports
  summary: Anti-rec95 labeling panels a,c–f,h,i and preimmune panels b,g support sinister-fiber
    localization; open arrow in a denotes the distal connecting fiber, not the labeled
    sinister fiber. The caption’s control and scale interpretations agree. Fresh image
    MD5 f23cd3d26f582cd37401dc00e89ddccb matches the record.
- evidence_id: micro-current-sinister-prep-figure8
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2132688.1/JCB15053.f8.jpg
  locator: Figure8 native architecture panels, visually inspected
  accessed_at: '2026-11-03T03:20:48.740258Z'
  snapshot_sha256: 619df5c2da94e208089aa551df462aeae46dca28e8bc30c63217348d551d17b3
  support: supports
  summary: Native basal-apparatus views support the differently positioned older/younger-basal-body
    fibers and root attachment; they do not establish proposed physiological roles.
- evidence_id: micro-current-interpro-family
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/O49944/
  locator: Exact InterPro protein-to-entry endpoint /entry/interpro/protein/uniprot/O49944/;
    HTTP204 empty body
  accessed_at: '2026-11-03T03:20:48.751288Z'
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
  support: partial
  summary: The specific protein-entry lookup returned no entries at access time. It
    does not prove global absence of any applicable family.
- evidence_id: micro-current-interpro-family-search
  kind: search
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/?search=BAp95&page_size=200
  locator: InterPro /entry/interpro/ literal search parameter; page_size=200; HTTP204
    empty response
  accessed_at: '2026-11-03T03:20:48.835850Z'
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
  support: partial
  summary: The bounded InterPro text query 'BAp95' returned no result body; this is
    not an exhaustive homology search.
  search_scope: InterPro entry API /entry/interpro/, literal search parameter 'BAp95',
    accessed 2026-11-03 UTC; first request page_size=200 returned HTTP204 with empty
    body and no next-page link. Only this text query was tested; no sequence-profile
    search, unreviewed terminology expansion or universal absence inference.
- evidence_id: micro-current-interpro-family-search-sinister
  kind: search
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/?search=sinister%20fiber&page_size=200
  locator: InterPro /entry/interpro/ literal search parameter; page_size=200; HTTP204
    empty response
  accessed_at: '2026-11-03T03:20:48.863651Z'
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
  support: partial
  summary: The bounded InterPro text query 'sinister fiber' returned no result body;
    this is not an exhaustive homology search.
  search_scope: InterPro entry API /entry/interpro/, literal search parameter 'sinister
    fiber', accessed 2026-11-03 UTC; first request page_size=200 returned HTTP204
    with empty body and no next-page link. Only this text query was tested; no sequence-profile
    search, unreviewed terminology expansion or universal absence inference.
- evidence_id: micro-current-interpro-family-search-basal
  kind: search
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/?search=basal%20apparatus%20protein&page_size=200
  locator: InterPro /entry/interpro/ literal search parameter; page_size=200; HTTP204
    empty response
  accessed_at: '2026-11-03T03:20:49.118247Z'
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
  support: partial
  summary: The bounded InterPro text query 'basal apparatus protein' returned no result
    body; this is not an exhaustive homology search.
  search_scope: InterPro entry API /entry/interpro/, literal search parameter 'basal
    apparatus protein', accessed 2026-11-03 UTC; first request page_size=200 returned
    HTTP204 with empty body and no next-page link. Only this text query was tested;
    no sequence-profile search, unreviewed terminology expansion or universal absence
    inference.
- evidence_id: micro-current-spindle-mt-prep-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000776,GO:0005816,GO:0005819,GO:0005874,GO:0005876,GO:0007059,GO:0072686
  locator: 'Seven queried GO definitions/status/hierarchy: 0000776,0005816,0005819,0005874,0005876,0007059,0072686'
  accessed_at: '2026-11-03T03:20:49.267510Z'
  snapshot_sha256: 099e0c8241d476fc601a0c6627fdb424559378cc77635c64c57f949f695fa785
  support: supports
  summary: Exact spindle-microtubule identity, microtubule parent, spindle parthood,
    chromosome-segregation function and distinct SPB/kinetochore/mitotic-spindle neighbors
    are supported by active terms.
- evidence_id: micro-current-spindle-mt-prep-tax-4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: ENA taxon identity
  accessed_at: '2026-11-03T03:20:49.365730Z'
  snapshot_sha256: 38f43dd1593a1d47416228ae385464f30aeb8302c3aadb45b3588d03744bc814
  support: supports
  summary: Saccharomyces cerevisiae species identity.
- evidence_id: micro-current-spindle-mt-prep-tax-559292
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: ENA taxon identity
  accessed_at: '2026-11-03T03:20:49.568979Z'
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
  support: supports
  summary: S. cerevisiae S288c strain-level taxon; distinct from species 4932.
- evidence_id: micro-current-spindle-mt-prep-winey-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1083/jcb.129.6.1601
  locator: DOI 10.1083/jcb.129.6.1601 exact result
  accessed_at: '2026-11-03T03:20:49.912561Z'
  snapshot_sha256: 313adbe1b330fba0e7502cfe978a583511f5c53e92c76fcedbb16f6f28d65de4
  support: supports
  summary: Winey et al. 1995 spindle reconstruction citation resolves to PMC2291174.
- evidence_id: micro-current-spindle-mt-prep-winey-s3
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2291174.1/PMC2291174.1.pdf
  locator: PDF abstract/introduction and Methods pp1601–1602; reconstruction Results;
    core/noncore interpretation p1609; text extracted with pdftotext
  accessed_at: '2026-11-03T03:20:49.926215Z'
  snapshot_sha256: b25472f54aa259fba263345f6665f398654801c4574c60673c242a2c1f96630c
  support: supports
  summary: High-pressure-frozen, freeze-substituted yeast serial sections support
    three-dimensional spindle reconstruction and core/noncore organization. D8Bx5Ca
    is S288c-derived. The kinetochore class is presumptive rather than direct visualization
    of kinetochore contacts, as the record acknowledges. These are not live-cell or
    cryo-electron-tomography observations.
- evidence_id: micro-current-spindle-mt-prep-straight-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1126/science.277.5325.574
  locator: Complete Europe PMC abstract for DOI10.1126/science.277.5325.574 / PMID9228009
  accessed_at: '2026-11-03T03:20:50.070484Z'
  snapshot_sha256: 85e5bb2644f5eb8b678b868051d04585c6585435bc1a03ca4913aaadce2fa9ae
  support: partial
  summary: The primary abstract describes GFP-Lac-repressor-marked chromosome loci
    and GFP-Tub1 spindle imaging in living yeast, supporting bounded chromosome-movement/anaphase-A
    claims. Full text and supplementary material were not freshly inspected.
- evidence_id: micro-current-spindle-mt-prep-P09733
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P09733.json
  locator: UniProt entryType, primaryAccession, geneName, organism, protein name and
    relevant subcellular-location evidence
  accessed_at: '2026-11-03T03:20:50.070770Z'
  snapshot_sha256: aed535980dd8ac2307085497de3917488ff4f5da0252812d09d17d17c739b426
  support: supports
  summary: Reviewed S288c entry P09733 identifies TUB1. Major alpha-tubulin; native
    experimental cytoskeleton citation PMID11739794. Accession identity and native
    annotations are distinguished from direct spindle-membership experiments.
- evidence_id: micro-current-spindle-mt-prep-query-TUB1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3ATUB1%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&size=500
  locator: UniProt gene_exact AND organism_id:559292 AND reviewed:true; size500; X-Total-Results=1;
    no Link continuation
  accessed_at: '2026-11-03T03:20:50.168292Z'
  snapshot_sha256: ab3ef6eb4aba30b014094695c817ac553dcd2c55c6f8feda6c32fae65e55e16c
  support: supports
  summary: 'Exactly one reviewed S288c result for TUB1: P09733. This checks the supplied
    gene-accession identity, not an exhaustive spindle proteome.'
  search_scope: 'UniProtKB search on 2026-11-03 UTC: (gene_exact:TUB1) AND (organism_id:559292)
    AND (reviewed:true), format=json, size=500. One result, X-Total-Results=1 and
    no pagination Link. Restricted to reviewed S288c exact-gene entries; excludes
    other taxa, strains, aliases and unreviewed entries.'
- evidence_id: micro-current-spindle-mt-prep-P02557
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P02557.json
  locator: UniProt entryType, primaryAccession, geneName, organism, protein name and
    relevant subcellular-location evidence
  accessed_at: '2026-11-03T03:20:50.313239Z'
  snapshot_sha256: d22cba0cfbb4aaa448114cc4356c81a4f7116a79ee7359a05b69dfd659d6b646
  support: supports
  summary: Reviewed S288c entry P02557 identifies TUB2. Beta-tubulin; native cytoskeleton/Kip3
    annotation citation PMID23001566. Accession identity and native annotations are
    distinguished from direct spindle-membership experiments.
- evidence_id: micro-current-spindle-mt-prep-query-TUB2
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3ATUB2%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&size=500
  locator: UniProt gene_exact AND organism_id:559292 AND reviewed:true; size500; X-Total-Results=1;
    no Link continuation
  accessed_at: '2026-11-03T03:20:50.556502Z'
  snapshot_sha256: 4d1049116e3e865676ca2a31ed8f01bdd757d3cad4b28b84933b5903876ea148
  support: supports
  summary: 'Exactly one reviewed S288c result for TUB2: P02557. This checks the supplied
    gene-accession identity, not an exhaustive spindle proteome.'
  search_scope: 'UniProtKB search on 2026-11-03 UTC: (gene_exact:TUB2) AND (organism_id:559292)
    AND (reviewed:true), format=json, size=500. One result, X-Total-Results=1 and
    no pagination Link. Restricted to reviewed S288c exact-gene entries; excludes
    other taxa, strains, aliases and unreviewed entries.'
- evidence_id: micro-current-spindle-mt-prep-P09734
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P09734.json
  locator: UniProt entryType, primaryAccession, geneName, organism, protein name and
    relevant subcellular-location evidence
  accessed_at: '2026-11-03T03:20:50.735485Z'
  snapshot_sha256: 0a6865ddaa8955d9ccdc57056008255b39a4ab55d5b75e640a37a0206c197b67
  support: supports
  summary: Reviewed S288c entry P09734 identifies TUB3. Minor alpha-tubulin; no unsupported
    claim that this paralog is individually essential. Accession identity and native
    annotations are distinguished from direct spindle-membership experiments.
- evidence_id: micro-current-spindle-mt-prep-query-TUB3
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3ATUB3%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&size=500
  locator: UniProt gene_exact AND organism_id:559292 AND reviewed:true; size500; X-Total-Results=1;
    no Link continuation
  accessed_at: '2026-11-03T03:20:50.987736Z'
  snapshot_sha256: 1e154b62a419986ae1256476fa07411bfb9f6cc39e678a36cd482cc505e8e62e
  support: supports
  summary: 'Exactly one reviewed S288c result for TUB3: P09734. This checks the supplied
    gene-accession identity, not an exhaustive spindle proteome.'
  search_scope: 'UniProtKB search on 2026-11-03 UTC: (gene_exact:TUB3) AND (organism_id:559292)
    AND (reviewed:true), format=json, size=500. One result, X-Total-Results=1 and
    no pagination Link. Restricted to reviewed S288c exact-gene entries; excludes
    other taxa, strains, aliases and unreviewed entries.'
- evidence_id: micro-current-spindle-mt-prep-anders-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A11739794%20AND%20SRC%3AMED
  locator: Europe PMC exact PMID11739794 result
  accessed_at: '2026-11-03T03:20:51.293056Z'
  snapshot_sha256: 09d880b0260ec19f9866a41868cb276dd1a1e6ee374c042df5ab39b5d2ee4b57
  support: supports
  summary: Citation identity for the native TUB1 annotation source.
- evidence_id: micro-current-spindle-mt-prep-cederquist-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A23001566%20AND%20SRC%3AMED
  locator: Europe PMC exact PMID23001566 result
  accessed_at: '2026-11-03T03:20:51.809336Z'
  snapshot_sha256: 11012dca34504a5eb2b11d689f0a93e4ce4338b23cc03fb67b1d2289c64726c1
  support: supports
  summary: Citation identity for the native TUB2 annotation source.
- evidence_id: micro-current-spindle-mt-agent-anders2001
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC60769/?report=xml
  locator: PMC60769 HTML; selected paragraphs 11,17,21,25,26,31,35 in retained paragraph
    index; abstract and relevant Results/Methods
  accessed_at: '2026-11-03T03:20:52.016451Z'
  snapshot_sha256: 80dd36650cf86a732efac4d4c96d779bc4835b67ee9178189c98c007e409c37e
  support: supports
  summary: TUB1 is the major essential alpha-tubulin while TUB3 deletion is viable;
    GFP/mutant experiments describe abnormal cytoplasmic and spindle microtubules.
    Supports native annotation provenance and the record’s combined alpha/beta-material
    essentiality rather than essentiality of every paralog.
- evidence_id: micro-current-spindle-mt-agent-cederquist2012
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3516133/?report=xml
  locator: PMC3516133 HTML; abstract and Results paragraphs44,45,48,49,51 in retained
    paragraph index
  accessed_at: '2026-11-03T03:20:52.096906Z'
  snapshot_sha256: 27fcdd010d8f9a84cc9245cdf35bc1c4351ee38e848d86e855e3b341da0e873a
  support: supports
  summary: The human mutation is modeled in yeast Tub2; heterozygous diploids and
    GFP-TUB1 G1 astral-microtubule/Kip3 behavior are the actual assay scope. This
    supports the native cytoskeleton annotation provenance, not a claim that this
    paper directly demonstrates all spindle localization.
- evidence_id: micro-current-jaspersen-secondary-context
  kind: authority
  reference: https://www.researchgate.net/publication/8241691_THE_BUDDING_YEAST_SPINDLE_POLE_BODY_Structure_Duplication_and_Function
  locator: Retained browser text of Jaspersen and Winey 2004; microtubule-nucleation
    section, especially lines976–1073
  accessed_at: '2026-11-03T03:26:34.810Z'
  snapshot_sha256: 373ac9ea3523aac94fdb0a12f2821d73d46bdd0e40413e31026554c7fa2aa55f
  support: context_only
  summary: Secondary review context for the nuclear inner plaque / cytoplasmic outer
    plaque and gamma-tubulin nucleation. Browser response is cached text crawled three
    weeks earlier, freshly accessed here; no original experiment or fresh publisher
    PDF is claimed. Native cited papers, not this review alone, support the record’s
    primary structural claims.
- evidence_id: micro-current-spirostomum-agent-zhang2023-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC9946354.1/PMC9946354.1.xml
  locator: Claim-bearing Results on spasmins, GSBP1/2, RNAi and adjacent cortical
    organization; Discussion; relevant culture, MS/IP, IF, Western and RNAi Methods;
    Fig5 caption/permissions
  accessed_at: '2026-11-03T03:20:52.319178Z'
  snapshot_sha256: c3d482565da44fe649e92200485a628b8b2881507c999565525126430bf8b8c0
  support: supports
  summary: S. minus myoneme composition, giant Sfi1-like backbones, antibody specificity
    and the bounded perturbation observations support the record. Anti-GSBP2 cross-reacts
    with both backbones; anti-GSBP1 is specific; anti-centrin is not paralog-specific.
    IP associations are not direct-contact maps. Rare type-E effects and dsRNA-bacterial
    checks do not establish uniform target depletion, essentiality or motor stoichiometry.
    JATS MD5 3e94476b75520b5f351c6f4fd97e95c4 matches the package and record.
- evidence_id: micro-current-spirostomum-agent-zhang2023-package
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC9946354.1/PMC9946354.1.json
  locator: Versioned PMC9946354.1 file manifest, licence and retraction metadata
  accessed_at: '2026-11-03T03:20:52.420373Z'
  snapshot_sha256: 2d6d0e0d92190e68f7bcaffb8336d17e37d0260554d582ab558d1a38eeff1391
  support: supports
  summary: Versioned PMC9946354.1 manifest identifies Zhang2023 XML/image checksums
    and CC BY-NC licence; no retraction indicated. Fresh JATS and Figure5 MD5s match
    manifest and record.
- evidence_id: micro-current-spirostomum-agent-figure5
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC9946354.1/sciadv.add6550-f5.jpg
  locator: Figure5 A,B,C, visually inspected against caption
  accessed_at: '2026-11-03T03:20:52.726712Z'
  snapshot_sha256: 185ff236ea1c9456b74815889be6d4d6d2828158715ef02228d9dd9c6a3debc6
  support: supports
  summary: A is an AlphaFold prediction; B combines centrin/GSBP2 staining across
    cortical layers; C contrasts GSBP1 versus GSBP2 staining and one-versus-two Western
    bands. The image does not prove an atomic native complex. Image MD5 4d4c13d6219f5b468c531d2def3df883
    matches package and record.
- evidence_id: micro-current-spirostomum-agent-lannan2024-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC11581044.2/PMC11581044.2.xml
  locator: Versioned PMC11581044.2 preprint, Results sections S3,S4,S5,S7 and claim-relevant
    Discussion S8
  accessed_at: '2026-11-03T03:20:52.830530Z'
  snapshot_sha256: 1825d2e752183254de63b70203c6e723f51266aff5bef48b1c01fa4800823d14
  support: supports
  summary: The inspected 2024 version supports the S. ambiguum mesh geometry, calcium-linked
    observations and bounded repeat-complex predictions. Volume conservation is a
    model assumption; cross-species antibody labeling is not paralog identification;
    predicted compact/extended conformations are not direct proof of the final force-generating
    mechanism. Old future-work statements do not imply the final 2026 work lacks experiments.
    JATS MD5 9546d004a0e44d93c64fded2bff97443 matches manifest and record.
- evidence_id: micro-current-spirostomum-agent-lannan2024-package
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC11581044.2/PMC11581044.2.json
  locator: 'Versioned PMC11581044.2 manifest: XML checksum/licence'
  accessed_at: '2026-11-03T03:20:52.830727Z'
  snapshot_sha256: b54f2570fd40f71b2a10641c13311be821c6d376bf6cbfa11ef383318a5c8aaa
  support: supports
  summary: The fixed versioned preprint XML checksum is verified and its CC BY-NC-ND
    4.0 scope retained; this is distinct from subsequently updated Europe PMC preprint
    metadata.
- evidence_id: micro-current-spirostomum-agent-epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=100&query=DOI%3A10.1126%2Fsciadv.add6550%20OR%20DOI%3A10.1073%2Fpnas.2601408123%20OR%20DOI%3A10.1101%2F2024.11.07.622534%20OR%20DOI%3A10.1016%2Fj.cell.2025.09.027
  locator: Exact four-DOI Europe PMC result metadata
  accessed_at: '2026-11-03T03:20:52.892412Z'
  snapshot_sha256: 87d6ae7739c1ff43129d11dfa593663735641e3a67c31561aa07f280f82b6549
  support: supports
  summary: Resolves Zhang2023, the Lannan preprint, Lannan2026 final PNAS and Mikus2025
    identifiers/titles. The current preprint metadata can describe an updated version
    and is not silently substituted for PMC11581044.2.
- evidence_id: micro-current-spirostomum-final2026-abstract
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=100&query=DOI%3A10.1126%2Fsciadv.add6550%20OR%20DOI%3A10.1073%2Fpnas.2601408123%20OR%20DOI%3A10.1101%2F2024.11.07.622534%20OR%20DOI%3A10.1016%2Fj.cell.2025.09.027
  locator: Only DOI10.1073/pnas.2601408123 / PMID42213749 result abstractText
  accessed_at: '2026-11-03T03:20:52.892412Z'
  snapshot_sha256: 87d6ae7739c1ff43129d11dfa593663735641e3a67c31561aa07f280f82b6549
  support: partial
  summary: The final primary abstract reports centrin/Sfi1 myoneme evidence, deformation
    modeling and purified repeat-complex calcium-dependent compaction/self-association.
    Supports only these qualitative abstract-level imports; final Methods, numerical
    conditions, figures and supplementary data were not available here.
- evidence_id: micro-current-spirostomum-agent-lannan2026-epmcfull
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13229174/fullTextXML
  locator: Europe PMC PMC13229174/fullTextXML HTTP500 receipt
  accessed_at: '2026-11-03T03:20:53.204363Z'
  snapshot_sha256: 2fafba58e46ba2b7c19d0437d22d8a39baf02ad2d024cd69c98d885a8e2908d4
  support: context_only
  summary: Fresh final-paper full-text request failed with HTTP500; no final full-text
    inspection claimed.
- evidence_id: micro-current-spirostomum-agent-lannan2026-pmc
  kind: validation
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC13229174/
  locator: PMC13229174 HTTP200 response body
  accessed_at: '2026-11-03T03:20:53.343083Z'
  snapshot_sha256: d241da564da406b903552f84fe01a428464a14912073d8e6f7a306c13909c606
  support: context_only
  summary: HTTP200 body is a browser/recaptcha challenge, not readable scientific
    full text. No final-paper body, embargo date or figures were verified through
    this response.
- evidence_id: micro-current-spirostomum-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005622,GO:0030863
  locator: GO:0005622 and GO:0030863 active definitions
  accessed_at: '2026-11-03T03:20:53.512562Z'
  snapshot_sha256: a51dafa11e7eafbaa411cc1af78225229343863c98b30dd927d782676aff3bdd
  support: supports
  summary: Broad intracellular-anatomical-structure parent and cortical-cytoskeleton
    parthood are compatible with the local fishnet identity.
- evidence_id: micro-current-spirostomum-agent-go-myoneme-search
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=myoneme
  locator: QuickGO text search for literal myoneme; zero results
  accessed_at: '2026-11-03T03:20:53.607374Z'
  snapshot_sha256: 4f0027cdf6df79bb6d4e90297666e971eb23ca7cfa19fc11fb9c9931fd5f1004
  support: partial
  summary: This bounded GO text query supplies no exact identity term. Primary evidence
    and explicit local identity carry the structure; a zero-result text query is not
    universal ontology absence.
  search_scope: QuickGO ontology/go/search query=myoneme on 2026-11-03 UTC, using
    the exact request URL recorded here and default limit25 confirmed by pageInfo.resultsPerPage=25;
    response numberOfHits=0, pageInfo.total=0 and no result pages. Restricted to this
    literal term; not a synonym expansion, exhaustive GO graph or other-ontology search.
- evidence_id: micro-current-spirostomum-agent-taxon-402029
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/402029
  locator: ENA taxonId/scientificName
  accessed_at: '2026-11-03T03:20:53.607639Z'
  snapshot_sha256: 3daf11b5278aa464c33f69834f17328a4c6ef63002f883b3a7022420448f9a71
  support: supports
  summary: 'Exact species identity: Spirostomum minus.'
- evidence_id: micro-current-spirostomum-agent-taxon-37688
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/37688
  locator: ENA taxonId/scientificName
  accessed_at: '2026-11-03T03:20:53.640854Z'
  snapshot_sha256: 93ad54c57e3ac8594ed009581a653643745bee76296eb997692f4c2af60204af
  support: supports
  summary: 'Exact species identity: Spirostomum ambiguum.'
- evidence_id: micro-current-spirostomum-agent-IPR050145
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050145/
  locator: Native InterPro accession/name/type and family description
  accessed_at: '2026-11-03T03:20:53.824299Z'
  snapshot_sha256: 386371fb67a7de41d9f9a6ded2bbb77530d9a27411b46349d2ac050d45832910
  support: context_only
  summary: Centrin/CML-like is a broader family than myonemal spasmins and includes
    other calcium-binding proteins; it is not exact structure-specific grounding.
    Description text is authority-provided context, not independent primary localization
    evidence.
- evidence_id: micro-current-spirostomum-agent-IPR052270
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR052270/
  locator: Native InterPro accession/name/type and family description
  accessed_at: '2026-11-03T03:20:53.978226Z'
  snapshot_sha256: 1b31c05d82a1ef155a91ee9b419e70a5e28f9414358e858d34f79e55ea5b54bb
  support: context_only
  summary: Centrin-binding protein SFI1-like covers a broader class including other
    proteins such as CCDC191; it is not demonstrated to map exactly the giant Spirostomum
    backbone pair. No invented exact GSBP accession.
- evidence_id: micro-current-spirostomum-agent-mikus2025-paper-pdf
  kind: authority
  reference: https://www.roscoff-culture-collection.org/sites/default/files/rcc-papers/Mikus%20et%20al.%20-%202025%20-%20Charting%20the%20landscape%20of%20cytoskeletal%20diversity%20in%20microbial%20eukaryotes.pdf
  locator: Fresh institutional PDF, printed pp7 and13; text lines425–450 and765–790
    in retained pdftotext output
  accessed_at: '2026-11-03T03:20:54.167915Z'
  snapshot_sha256: 117e1e97412645a193cfbb87664031ead725759d02dddce02be84ad7e3a14d16
  support: context_only
  summary: Spirostomum fishnet and Paramecium ICL are comparative context citing earlier
    studies. Lacrymaria fishnet/oral-ring discussion concerns a different taxon. These
    passages do not supply new primary Spirostomum evidence or establish identity
    of all centrin-rich networks.
- evidence_id: micro-current-current-adapter-catalogue
  kind: search
  reference: https://imodulondb.org/api/datasets
  locator: 'Complete /api/datasets JSON list: 20 organism entries / 28 datasets; no
    pagination advertised'
  accessed_at: '2026-11-03T03:20:54.290965Z'
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  support: context_only
  summary: The complete returned catalogue contains no S. cerevisiae, S. similis or
    Spirostomum organism/dataset. A target-specific module search is therefore not
    applicable. This is dataset coverage, not negative biological evidence.
  search_scope: iModulonDB /api/datasets, accessed 2026-11-03 UTC, unfiltered complete
    catalogue endpoint with no requested result cap or pagination; inspected all 20
    returned organism entries and all 28 dataset names. Compared the four targets’
    declared S. cerevisiae, Spermatozopsis similis, S. minus and S. ambiguum contexts.
    No matching organism/dataset returned; no gene/module search performed and no
    biological absence inferred. Runner availability is independently documented by
    the root reviewer, not established by this HTTP request.
- evidence_id: micro-current-record-gap
  kind: record_content
  reference: data/structures/cytoskeleton/sin_men_two_component_gap_complex.yaml
  locator: Complete unchanged target YAML
  accessed_at: '2026-11-03T03:31:47.193751Z'
  snapshot_sha256: 922665d09fdb8ddf24c904aefc3ccd0ec99a36f92d4d33f71a42c732036ecbdd
  support: supports
  summary: Current target bytes match the original review frozen SHA256 922665d09fdb8ddf24c904aefc3ccd0ec99a36f92d4d33f71a42c732036ecbdd.
    Full target read; no record edit or stale refresh required.
- evidence_id: micro-original-review-gap
  kind: prior_review
  reference: reviews/structured/20261021T082245Z-sin-men-two-component-gap-complex-audit/review.yaml
  locator: Original source inputs/checks/evidence/assessments/findings/verdict/limitations
  accessed_at: '2026-11-03T03:31:47.193751Z'
  snapshot_sha256: 6860dfe506571b094c545df1e9788141e3a9beab7a37e9399dc33fdb0b7c1d0a
  support: supports
  summary: Original verdict pass_with_limitations with no findings. Its target hash
    remains current and native validation/render passes; its iModulonDB exemption
    relies on absence of expression-module claims rather than establishing actual
    organism/dataset applicability.
- evidence_id: micro-current-record-sinister
  kind: record_content
  reference: data/structures/cytoskeleton/sinister_fiber.yaml
  locator: Complete unchanged target YAML
  accessed_at: '2026-11-03T03:31:47.193751Z'
  snapshot_sha256: 9227477d7ba7b31e708bd60156ccb5d24f7051d3e0451b9138e6b3380d3664e5
  support: supports
  summary: Current target bytes match the original review frozen SHA256 9227477d7ba7b31e708bd60156ccb5d24f7051d3e0451b9138e6b3380d3664e5.
    Full target read; no record edit or stale refresh required.
- evidence_id: micro-original-review-sinister
  kind: prior_review
  reference: reviews/structured/20261021T082245Z-sinister-fiber-audit/review.yaml
  locator: Original source inputs/checks/evidence/assessments/findings/verdict/limitations
  accessed_at: '2026-11-03T03:31:47.193751Z'
  snapshot_sha256: 5f0b624c9840228af1cb1478aecdb410f1b273d37dca272df12451f7fd7b52aa
  support: supports
  summary: Original verdict pass_with_limitations with no findings. Its target hash
    remains current and native validation/render passes; its iModulonDB exemption
    relies on absence of expression-module claims rather than establishing actual
    organism/dataset applicability.
- evidence_id: micro-current-record-spindle
  kind: record_content
  reference: data/structures/cytoskeleton/spindle_microtubule.yaml
  locator: Complete unchanged target YAML
  accessed_at: '2026-11-03T03:31:47.193751Z'
  snapshot_sha256: bd8d435d59b948878bdcc978f015029ba6f6cc236b43eab0a5a5fe8b1a350fb9
  support: supports
  summary: Current target bytes match the original review frozen SHA256 bd8d435d59b948878bdcc978f015029ba6f6cc236b43eab0a5a5fe8b1a350fb9.
    Full target read; no record edit or stale refresh required.
- evidence_id: micro-original-review-spindle
  kind: prior_review
  reference: reviews/structured/20261021T082245Z-spindle-microtubule-audit/review.yaml
  locator: Original source inputs/checks/evidence/assessments/findings/verdict/limitations
  accessed_at: '2026-11-03T03:31:47.193751Z'
  snapshot_sha256: ae4c7d5dcc6ab23b2804ff1ac023995cc0fb3de62f50272069de12b7371a979c
  support: supports
  summary: Original verdict pass_with_limitations with no findings. Its target hash
    remains current and native validation/render passes; its iModulonDB exemption
    relies on absence of expression-module claims rather than establishing actual
    organism/dataset applicability.
- evidence_id: micro-current-record-spirostomum
  kind: record_content
  reference: data/structures/cytoskeleton/spirostomum_myoneme_fishnet.yaml
  locator: Complete unchanged target YAML
  accessed_at: '2026-11-03T03:31:47.193751Z'
  snapshot_sha256: 23c2668330bc68a88153d7ed54feb0a5626a88d4ae53a8da6e250d2dda8d71af
  support: supports
  summary: Current target bytes match the original review frozen SHA256 23c2668330bc68a88153d7ed54feb0a5626a88d4ae53a8da6e250d2dda8d71af.
    Full target read; no record edit or stale refresh required.
- evidence_id: micro-original-review-spirostomum
  kind: prior_review
  reference: reviews/structured/20261021T082245Z-spirostomum-myoneme-fishnet-audit/review.yaml
  locator: Original source inputs/checks/evidence/assessments/findings/verdict/limitations
  accessed_at: '2026-11-03T03:31:47.193751Z'
  snapshot_sha256: 53bbd7643fac6e1f80fdb8a31e2f00f0cf8ab87a385ff878cc9c82e00309d79b
  support: supports
  summary: Original verdict pass_with_limitations with no findings. Its target hash
    remains current and native validation/render passes; its iModulonDB exemption
    relies on absence of expression-module claims rather than establishing actual
    organism/dataset applicability.
- evidence_id: micro-current-original-validation
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2348/adversary-microtubule/original-checks.json
  locator: Four native validate results, renderer byte equality and frozen-target
    comparison
  accessed_at: '2026-11-03T03:20:53.477650Z'
  snapshot_sha256: 31e191745d9dc3a5c994e5263a4a3c3ec11a92a54a1d0bc94aeb22cb65eaa217
  support: supports
  summary: All four original reviews validate with exit0, rendered Markdown matches
    exactly, and target hashes match. This receipt does not represent full corpus
    QC.
- evidence_id: micro-current-adapter-policy
  kind: record_content
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: structured-source-cross-checks block, lines91–123
  accessed_at: '2026-11-03T03:31:47.193751Z'
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
  support: supports
  summary: Named genes/proteins/accessions trigger structured-source consideration.
    For iModulonDB candidates, resolve runner and coverage first; lack of matching
    organism/dataset supports not_applicable. Absence of an expression-module assertion
    is not the stated exemption.
- evidence_id: septin-p2348-collar-record
  kind: record_content
  reference: data/structures/cytoskeleton/septin_collar.yaml
  locator: Entire target, all components/protein examples, taxonomy, graph edges,
    evidence and discussions
  accessed_at: '2026-11-03T03:28:43.476054Z'
  support: context_only
  summary: Complete target read after native inspection. Maintained record and mapping
    status remain PROPOSED; no scientific promotion or content change.
  snapshot_sha256: c16f869099afaf1a608e229fb19f217583156684f4a7311549af622691b556d9
- evidence_id: septin-p2348-policy
  kind: record_content
  reference: docs/CURATION.md
  locator: 'Components: family grounding, composition and structure-formation essentiality'
  accessed_at: '2026-11-03T03:28:43.476054Z'
  support: context_only
  summary: A generic family identifier is distinct from an exact localized cohort;
    ESSENTIAL refers to formation of the named structure, not viability or each named
    paralog.
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
- evidence_id: septin-p2348-example-policy
  kind: record_content
  reference: .claude/skills/uniprot-protein-examples/SKILL.md
  locator: Non-negotiable rules1–5; captured as expanded native inspect input
  accessed_at: '2026-11-03T03:28:43.476054Z'
  support: context_only
  summary: Correct accession, gene, taxon and entry status do not independently establish
    structure membership. Native subcellular-location evidence is retained only for
    the actual compartment named.
  snapshot_sha256: 6462894c8257823bae2b175c34693cd42f11ff9269a3829c15b9286ba6d7c876
- evidence_id: septin-p2348-septin-collar-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032173,GO:0032156,GO:0032174,GO:0062140,GO:0005940,GO:0032160,GO:0005856,GO:0032165,GO:0032166,GO:0032159,GO:0005938,GO:0031105
  locator: Returned exact terms and isObsolete flags; definitions, synonyms and children
    with is_a versus part_of relations
  accessed_at: '2026-11-03T03:22:26.138977Z'
  support: supports
  summary: Exact active GO definitions, generic structure classes, named parents/children
    and structural parthood were checked. The returned broader terms expose the relevant
    child relations.
  snapshot_sha256: c354da8bddce6953db86b6ed705e054d4600415453e594bf8fa3eca70b56e47e
- evidence_id: septin-p2348-septin-collar-agent-family
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016491/
  locator: metadata accession/name/type=family, description and hierarchy; cached
    response independently reread at this review
  accessed_at: '2026-11-03T01:54:20.570567Z'
  support: supports
  summary: 'Cached native response independently reread for PR #2348; accessed_at
    retains the actual earlier fetch time. IPR016491 is the Septin family, appropriate
    to the generic septin-proteins label. It does not delimit one localized cohort,
    specify stoichiometry or prove membership of an individual example.'
  snapshot_sha256: 5797c626d192b641ed5b4b2231e729f9f179bfd6bb18f911689fa08253688c4a
- evidence_id: septin-p2348-septin-collar-agent-paper-metadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=25&query=%28DOI%3A%2210.1091/mbc.E04-09-0764%22%29%20OR%20%28DOI%3A%2210.1534/genetics.107.073007%22%29%20OR%20%28DOI%3A%2210.1073/pnas.0803330105%22%29%20OR%20%28DOI%3A%2210.1016/j.devcel.2011.02.004%22%29%20OR%20%28DOI%3A%2210.3389/fcell.2016.00123%22%29%20OR%20%28DOI%3A%2210.1016/j.mib.2014.04.004%22%29%20OR%20%28DOI%3A%2210.1099/mic.0.000359%22%29%20OR%20%28EXT_ID%3A14562095%20AND%20SRC%3AMED%29%20OR%20%28EXT_ID%3A25971666%20AND%20SRC%3AMED%29%20OR%20%28EXT_ID%3A9790978%20AND%20SRC%3AMED%29
  locator: Relevant exact DOI/PMID result objects; publication metadata and abstracts
  accessed_at: '2026-11-03T03:22:26.139281Z'
  support: supports
  summary: Fresh native metadata verifies the ten exact DOI/PMID identities, titles
    and publication types. Huh 2003, Finnigan 2015 and Mino 1998 were read at abstract/metadata
    tier here; their imported localization citations were checked against native UniProt.
    Their primary bodies were not independently audited in this assigned slice.
  snapshot_sha256: 308f19aa28a0c4667f0e9c7f01796686289255238b64f4e7e39706e69ae04e42
  search_scope: Europe PMC native exact query (DOI:"10.1091/mbc.E04-09-0764") OR (DOI:"10.1534/genetics.107.073007")
    OR (DOI:"10.1073/pnas.0803330105") OR (DOI:"10.1016/j.devcel.2011.02.004") OR
    (DOI:"10.3389/fcell.2016.00123") OR (DOI:"10.1016/j.mib.2014.04.004") OR (DOI:"10.1099/mic.0.000359")
    OR (EXT_ID:14562095 AND SRC:MED) OR (EXT_ID:25971666 AND SRC:MED) OR (EXT_ID:9790978
    AND SRC:MED); queried 2026-11-03T03:22:26.139281Z; no publication-date restriction;
    resultType=core, pageSize=25; all ten returned exact-identifier objects inspected;
    metadata and abstracts only for Huh 2003, Finnigan 2015 and Mino 1998. No global
    literature-absence conclusion.
- evidence_id: septin-p2348-septin-collar-agent-P32457
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P32457.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism and SUBCELLULAR
    LOCATION evidence
  accessed_at: '2026-11-03T03:22:26.139388Z'
  support: supports
  summary: The reviewed accession, recommended protein label, primary CDC3 symbol
    and organism taxon559292 match the record. Native subcellular-location annotations
    and their experimental PubMed citations were inspected without treating general
    membrane/bud-neck evidence as another morphogenetic localization.
  snapshot_sha256: 7fc581a719d6b12f8611b58bfc0c11fc057c73e673b217485a3379b8330b6efe
- evidence_id: septin-p2348-septin-collar-agent-symbol-CDC3
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=100&query=%28gene_exact%3ACDC3%29%20AND%20%28taxonomy_id%3A4932%29%20AND%20%28reviewed%3Atrue%29
  locator: Exact query in receipt, results cardinality, primaryAccession and gene
    token
  accessed_at: '2026-11-03T03:22:26.139463Z'
  support: context_only
  summary: Exact reviewed CDC3 query in S. cerevisiae returns one entry, P32457. The
    gene token and taxon were checked directly; this is an identity/uniqueness result,
    not membership evidence.
  snapshot_sha256: d15bf1b00b3f29538132111c0a6ab994f6bf134478224348f6857db31c1f4aee
  search_scope: UniProtKB native exact query (gene_exact:CDC3) AND (taxonomy_id:4932)
    AND (reviewed:true); queried 2026-11-03T03:22:26.139463Z; no publication-date
    restriction; reviewed entries restricted to taxonomy_id:4932, size=100, exactly
    one returned record inspected; primary gene token also checked.
- evidence_id: septin-p2348-septin-collar-agent-P25342
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P25342.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism and SUBCELLULAR
    LOCATION evidence
  accessed_at: '2026-11-03T03:22:26.139528Z'
  support: supports
  summary: The reviewed accession, recommended protein label, primary CDC10 symbol
    and organism taxon559292 match the record. Native subcellular-location annotations
    and their experimental PubMed citations were inspected without treating general
    membrane/bud-neck evidence as another morphogenetic localization.
  snapshot_sha256: 5a5194945989f266f18122a50805faa45f7bc00a599dcefcf7cf6592d753174d
- evidence_id: septin-p2348-septin-collar-agent-symbol-CDC10
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=100&query=%28gene_exact%3ACDC10%29%20AND%20%28taxonomy_id%3A4932%29%20AND%20%28reviewed%3Atrue%29
  locator: Exact query in receipt, results cardinality, primaryAccession and gene
    token
  accessed_at: '2026-11-03T03:22:26.139637Z'
  support: context_only
  summary: Exact reviewed CDC10 query in S. cerevisiae returns one entry, P25342.
    The gene token and taxon were checked directly; this is an identity/uniqueness
    result, not membership evidence.
  snapshot_sha256: f9b9dc13ffea60b8a6bfb9d653d7a4ede1157e95cf417161793bf122b409fa8c
  search_scope: UniProtKB native exact query (gene_exact:CDC10) AND (taxonomy_id:4932)
    AND (reviewed:true); queried 2026-11-03T03:22:26.139637Z; no publication-date
    restriction; reviewed entries restricted to taxonomy_id:4932, size=100, exactly
    one returned record inspected; primary gene token also checked.
- evidence_id: septin-p2348-septin-collar-agent-P32458
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P32458.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism and SUBCELLULAR
    LOCATION evidence
  accessed_at: '2026-11-03T03:22:26.947075Z'
  support: supports
  summary: The reviewed accession, recommended protein label, primary CDC11 symbol
    and organism taxon559292 match the record. Native subcellular-location annotations
    and their experimental PubMed citations were inspected without treating general
    membrane/bud-neck evidence as another morphogenetic localization.
  snapshot_sha256: 839db168d3ac73f1e1718845d2d92024c8bd535a96081c789ff55a1a0e98c922
- evidence_id: septin-p2348-septin-collar-agent-symbol-CDC11
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=100&query=%28gene_exact%3ACDC11%29%20AND%20%28taxonomy_id%3A4932%29%20AND%20%28reviewed%3Atrue%29
  locator: Exact query in receipt, results cardinality, primaryAccession and gene
    token
  accessed_at: '2026-11-03T03:22:26.960034Z'
  support: context_only
  summary: Exact reviewed CDC11 query in S. cerevisiae returns one entry, P32458.
    The gene token and taxon were checked directly; this is an identity/uniqueness
    result, not membership evidence.
  snapshot_sha256: 384fe6c570f5d6549a3469d520685905279ff9f0303a7f72da1f0d9399322fc5
  search_scope: UniProtKB native exact query (gene_exact:CDC11) AND (taxonomy_id:4932)
    AND (reviewed:true); queried 2026-11-03T03:22:26.960034Z; no publication-date
    restriction; reviewed entries restricted to taxonomy_id:4932, size=100, exactly
    one returned record inspected; primary gene token also checked.
- evidence_id: septin-p2348-septin-collar-agent-P32468
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P32468.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism and SUBCELLULAR
    LOCATION evidence
  accessed_at: '2026-11-03T03:22:26.985855Z'
  support: supports
  summary: The reviewed accession, recommended protein label, primary CDC12 symbol
    and organism taxon559292 match the record. Native subcellular-location annotations
    and their experimental PubMed citations were inspected without treating general
    membrane/bud-neck evidence as another morphogenetic localization.
  snapshot_sha256: 3a96072071fa02a2e65a0d5d80ebcf82c631ff8f674fc6ce5ae642b8b273619e
- evidence_id: septin-p2348-septin-collar-agent-symbol-CDC12
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=100&query=%28gene_exact%3ACDC12%29%20AND%20%28taxonomy_id%3A4932%29%20AND%20%28reviewed%3Atrue%29
  locator: Exact query in receipt, results cardinality, primaryAccession and gene
    token
  accessed_at: '2026-11-03T03:22:27.179239Z'
  support: context_only
  summary: Exact reviewed CDC12 query in S. cerevisiae returns one entry, P32468.
    The gene token and taxon were checked directly; this is an identity/uniqueness
    result, not membership evidence.
  snapshot_sha256: 0096f0d783694af4a97eabab1e461dba9433f5de30a034cd6f25b0b667097721
  search_scope: UniProtKB native exact query (gene_exact:CDC12) AND (taxonomy_id:4932)
    AND (reviewed:true); queried 2026-11-03T03:22:27.179239Z; no publication-date
    restriction; reviewed entries restricted to taxonomy_id:4932, size=100, exactly
    one returned record inspected; primary gene token also checked.
- evidence_id: septin-p2348-septin-collar-agent-Q07657
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q07657.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism and SUBCELLULAR
    LOCATION evidence
  accessed_at: '2026-11-03T03:22:27.215900Z'
  support: supports
  summary: The reviewed accession, recommended protein label, primary SHS1 symbol
    and organism taxon559292 match the record. Native subcellular-location annotations
    and their experimental PubMed citations were inspected without treating general
    membrane/bud-neck evidence as another morphogenetic localization.
  snapshot_sha256: 4b3fa80abaa9782dee6cb8412786a5eed43b5df173dd4a150079a04064ec2627
- evidence_id: septin-p2348-septin-collar-agent-symbol-SHS1
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=100&query=%28gene_exact%3ASHS1%29%20AND%20%28taxonomy_id%3A4932%29%20AND%20%28reviewed%3Atrue%29
  locator: Exact query in receipt, results cardinality, primaryAccession and gene
    token
  accessed_at: '2026-11-03T03:22:27.321467Z'
  support: context_only
  summary: Exact reviewed SHS1 query in S. cerevisiae returns one entry, Q07657. The
    gene token and taxon were checked directly; this is an identity/uniqueness result,
    not membership evidence.
  snapshot_sha256: 0a077959f8d07e4292e2a3362dd78fb89992cf62800d84b1ad922eca984fd0c2
  search_scope: UniProtKB native exact query (gene_exact:SHS1) AND (taxonomy_id:4932)
    AND (reviewed:true); queried 2026-11-03T03:22:27.321467Z; no publication-date
    restriction; reviewed entries restricted to taxonomy_id:4932, size=100, exactly
    one returned record inspected; primary gene token also checked.
- evidence_id: septin-p2348-septin-collar-agent-taxon-4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: taxId, scientificName, rank and lineage
  accessed_at: '2026-11-03T03:22:28.049930Z'
  support: supports
  summary: Native taxonomy confirms the exact taxon identifier, scientific name and
    rank; species scope is distinguished from the S288C sequence-example strain.
  snapshot_sha256: 38f43dd1593a1d47416228ae385464f30aeb8302c3aadb45b3588d03744bc814
- evidence_id: septin-p2348-septin-collar-agent-taxon-559292
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: taxId, scientificName, rank and lineage
  accessed_at: '2026-11-03T03:22:28.123209Z'
  support: supports
  summary: Native taxonomy confirms the exact taxon identifier, scientific name and
    rank; species scope is distinguished from the S288C sequence-example strain.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: septin-p2348-septin-collar-agent-kozubowski2005-xml
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1182288/?report=xml
  locator: 'PMC1182288 native full HTML despite report=xml parameter: Introduction,
    Methods sec3–4/Table1, Results sec6/Figure1 legend and Discussion sec9'
  accessed_at: '2026-11-03T03:23:24.803720Z'
  support: supports
  summary: Primary source identity and body support the S. cerevisiae ring-to-collar
    context and Bni4/Kcc4 reporters. Intro identifies the five vegetative septins;
    Results sec6/Fig1 tracks reporter asymmetry already before budding and during
    collar formation. Methods specify JC482-congenic backgrounds and tagged reporters.
    The paper does not establish that the ring-to-collar transition initiates reporter
    asymmetry.
  snapshot_sha256: cf05e624c14722be1c3a95b97a633a629ff62fa97dacc8393e435e2076299216
- evidence_id: septin-p2348-septin-collar-agent-versele-pmc
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1761124/?pdf=render
  locator: PMC1761124 S2 paragraphP4 and Figure3 context; review tier, original retrieval
    retained
  accessed_at: '2026-11-03T01:54:20.386810Z'
  support: supports
  summary: 'Cached native response independently reread for PR #2348; accessed_at
    retains the actual earlier fetch time. Review synthesis explicitly describes Cdc3/Cdc10/Cdc11/Cdc12/Shs1
    complexes in the mitotic mother-bud-neck collar, distinguishing the meiotic cohort.
    The older molecular assembly model is not adopted as a current universal subunit-order
    claim.'
  snapshot_sha256: f397cf97bc67fb2894de8f8d4d3a5f3d6dda395ed00c87a9723bd7a38cfa020d
- evidence_id: septin-p2348-filament-array-record
  kind: record_content
  reference: data/structures/cytoskeleton/septin_filament_array.yaml
  locator: Entire target, all components/protein examples, taxonomy, graph edges,
    evidence and discussions
  accessed_at: '2026-11-03T03:28:43.476054Z'
  support: context_only
  summary: Complete target read after native inspection. Maintained record and mapping
    status remain PROPOSED; no scientific promotion or content change.
  snapshot_sha256: 8413e81f4ac3c0daf46af8a81bbc0c819380242af370486f07865114e2edc1a0
- evidence_id: septin-p2348-septin-array-agent-taxon-5476
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5476
  locator: taxId, scientificName, rank and lineage
  accessed_at: '2026-11-03T03:22:28.837947Z'
  support: supports
  summary: Native taxonomy confirms the exact taxon identifier, scientific name and
    rank; species scope is distinguished from the S288C sequence-example strain.
  snapshot_sha256: fdba428d1e1abf55ec666204b7320749e8f16f798a55b771ec0f5af932e6ab71
- evidence_id: septin-p2348-septin-array-agent-douglas-pmc
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1214204/?pdf=render
  locator: PMC1214204 sec14 and sec17; cached response independently reread at this
    review; review-tier synthesis
  accessed_at: '2026-11-03T00:45:07.048036Z'
  support: supports
  summary: 'Cached native response independently reread for PR #2348; accessed_at
    retains the actual earlier fetch time. The GO definition source is a literature
    review. It describes prospore septin sheets appearing as bars in optical sections
    and Candida chlamydospore peripheral filament arrays after septation. These stage-dependent
    localizations are not a single universal mitotic paralog set.'
  snapshot_sha256: 1f416e43bc154bdee2274b49bcb018582fbe2663eca2f62668d543e369bc9e1e
- evidence_id: septin-p2348-septin-array-agent-tachikawa2001
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2150859/fullTextXML
  locator: PMC2150859 Results sec7–10 and Figures5–9 legends; cached response independently
    reread at this review
  accessed_at: '2026-11-03T02:32:42.186808Z'
  support: supports
  summary: 'Cached native response independently reread for PR #2348; accessed_at
    retains the actual earlier fetch time. Primary Spr28/Gip1/Glc7 imaging supports
    a dynamic prospore-membrane array. Optical bars can represent parallel sheets;
    the Don1 leading-edge ring is distinct. Disrupted septin localization in gip1
    mutants does not by itself establish that every membrane process requires every
    septin.'
  snapshot_sha256: f15d65a734c0bb2a02dd5f2b31eed6f557164bc648994906c2072e5a9802ecfa
- evidence_id: septin-p2348-septin-array-agent-mcmurray2008
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2562167/?report=xml
  locator: 'PMC2562167 Results and Discussion S1: sporulation paragraphs beginning
    Two septins required / Like Cdc10 / Unlike CDC3; Figure3A,C,E,F,G and caption;
    DOI10.1016/j.cub.2008.07.020, PMID18701287'
  accessed_at: '2026-11-03T03:23:24.804050Z'
  support: refutes
  summary: Primary dual-color imaging finds little or no Cdc12-GFP in Cdc10-mCherry-marked
    spore-associated structures and no Shs1-GFP colocalization there; Shs1 remains
    in ascal cytoplasm. Cdc12 persists by immunoblot, so failure to detect it in the
    array is not attributed simply to degradation. Cdc10 is reused through the developmental
    transition. This directly challenges the unqualified Cdc12/Shs1 examples in the
    record's S. cerevisiae sporulation context.
  snapshot_sha256: 0301c9c812d9c939ffdac75f3ff31a6ced890787207082b549beeca56b60c8d2
- evidence_id: septin-p2348-septin-array-agent-mcmurray2008-figure3
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/502c/2562167/a3850b2cb250/nihms67754f3.jpg
  locator: Native Figure 3 panels A-G visually inspected in this review, with the
    freshly fetched full-text caption and Results; particular comparisons C/F and
    persistence blot E.
  accessed_at: '2026-11-03T03:22:30.428054Z'
  support: refutes
  summary: 'Native Figure3 was visually inspected: panelsC/F compare Cdc10-mCherry-marked
    spore structures with Cdc12-GFP/Shs1-GFP; panelE shows Cdc12 persistence. Interpretation
    follows the primary caption and Results, without extracting new quantitative intensity
    values.'
  snapshot_sha256: 09d4e5f7c061be87831d7ce567a851b3b48c639ae4d9b234dd80564e0a86260b
- evidence_id: septin-p2348-septin-array-agent-garcia2016
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4772501/fullTextXML
  locator: 'PMC4772501 native JATS: Abstract; Introduction; Results Higher-order assembly
    and Behavior of sporulation-specific septin complexes in vivo; Figure 4 caption;
    Discussion. Text and legends, no pixel reanalysis.'
  accessed_at: '2026-11-03T03:22:29.162582Z'
  support: refutes
  summary: 'Later primary study tests development-specific complexes. Results s08
    uses FRAP and BiFC: Cdc3–Cdc10 and Cdc3–Spr3 mark PSM structures, whereas forced
    Cdc3–Cdc12 interaction is predominantly peripheral ascal puncta. The Introduction
    explicitly preserves detectable Cdc11 at the PSM while the bulk of Cdc12/Shs1
    is excluded. These observations are scoped to tested sporulating backgrounds.'
  snapshot_sha256: af0698aed6e2e3c9db0ad0b768f3c5e8e2d1083abb530b84b703c60e41effa2c
- evidence_id: septin-p2348-ring-record
  kind: record_content
  reference: data/structures/cytoskeleton/septin_ring.yaml
  locator: Entire target, all components/protein examples, taxonomy, graph edges,
    evidence and discussions
  accessed_at: '2026-11-03T03:28:43.476054Z'
  support: context_only
  summary: Complete target read after native inspection. Maintained record and mapping
    status remain PROPOSED; no scientific promotion or content change.
  snapshot_sha256: f536dd5b190f0cba77de3b14131a2bd5b9d12369a96c81014cc6b0c2ebf1361d
- evidence_id: septin-p2348-septin-ring-agent-taxon-4751
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4751
  locator: taxId, scientificName, rank and lineage
  accessed_at: '2026-11-03T03:22:29.442892Z'
  support: supports
  summary: Native taxonomy confirms the exact taxon identifier, scientific name and
    rank; species scope is distinguished from the S288C sequence-example strain.
  snapshot_sha256: a7bab59bce650c0d29732327d4e7e342f1b648747f7f9635958f923b4a6089e6
- evidence_id: septin-p2348-septin-ring-agent-iwase2007-xml
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2013704/?report=xml
  locator: 'PMC2013704 genuine full HTML: Abstract, Introduction, Materials/strain
    Table 1, Results and Figure 1-5 legends on Shs1 localization, Cdc3/10/11/12 rings
    without Shs1, and Iqg1/Myo1/Cyk3 localization; no pixel reanalysis.'
  accessed_at: '2026-11-03T03:23:24.804134Z'
  support: supports
  summary: Primary S. cerevisiae experiments verify Shs1 bud-neck localization and
    distinguish septin ring assembly from recruitment of cytokinesis factors. Shs1
    deletion can leave Cdc3/Cdc10/Cdc11/Cdc12 rings assembled while Iqg1/Myo1/Cyk3
    localization and cytokinesis are impaired; requirement depends on background and
    conditions.
  snapshot_sha256: e600e8d1a3be8d9d61fdc9205f9a0a1a611890802b08a09393138e5c803d82ce
- evidence_id: septin-p2348-septin-ring-agent-bertin2008-xml
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2426963/?report=xml
  locator: PMC2426963 Results sec2–6, especially sec2 and sec4/Figures1 and4 legends;
    exact DOI10.1073/pnas.0803330105
  accessed_at: '2026-11-03T03:23:24.804182Z'
  support: supports
  summary: Purified recombinant Cdc3/Cdc10/Cdc11/Cdc12 complexes form nonpolar octameric
    rods; lowering salt yields end-to-end paired filaments. The direct reconstitution
    establishes a four-paralog core with two copies each, not simultaneous incorporation
    of all five listed mitotic paralogs. Shs1 replacement was a proposal in this paper.
  snapshot_sha256: b796870609eac0d30ae756de3969af24690c1a1891581137d54cc4f039d1b8dd
- evidence_id: septin-p2348-septin-ring-agent-mcmurray2011-xml
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3079881/?report=xml
  locator: 'PMC3079881 genuine full HTML: Summary; Results Cdc12 and Cdc3 homodimerization,
    Blocking Filament Assembly is Lethal and Prevents Cortical Septin Localization;
    Figure 3 legend and genotype/condition context. Text/legend inspection, no raw
    EM or fluorescence reanalysis.'
  accessed_at: '2026-11-03T03:23:24.804223Z'
  support: supports
  summary: Primary interface-mutant and microscopy experiments connect filament polymerization
    to cortical organization and viability in the tested yeast conditions. Cdc10-
    or Cdc11-deficient cells can survive via alternative hexameric assemblies, so
    neither individual necessity nor one oligomer size is universal.
  snapshot_sha256: 38ebb9244d3703dd3fb3fc7db098453b60975a2f4a7939cf07de27179a6da8df
- evidence_id: septin-p2348-septin-ring-agent-glomb2016-xml
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5093138/fullTextXML
  locator: 'PMC5093138 native JATS full text: paragraphs The mitotic yeast, Septin
    octamers containing Shs1, In the living yeast cell, After bud formation and Taken
    together; Figure 2 caption; secondary minireview.'
  accessed_at: '2026-11-03T03:22:30.113043Z'
  support: supports
  summary: Review synthesis supports the five mitotic septins, bud-site recruitment,
    ring-to-collar/split-ring transitions and scaffold functions. It explicitly distinguishes
    Cdc11-capped rods that assemble end-to-end from Shs1-capped rods that preferentially
    form curved/lateral assemblies.
  snapshot_sha256: edb83019065ba205c7ccd3de8634086ae00febfce3850bb22998601791d14bce
- evidence_id: septin-p2348-septin-ring-agent-bridges2014-xml
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC4266239/?report=xml
  locator: PMC4266239 S1–S3 and Figure1 textual legend; review tier, DOI10.1016/j.mib.2014.04.004
  accessed_at: '2026-11-03T03:23:24.804263Z'
  support: supports
  summary: Review of fungal pathogens supports septin scaffolding at division sites
    and species-specific higher-order localization, including bud-neck and hyphal
    septation contexts. It cautions that many mechanistic explanations remain unresolved
    and mutant phenotypes can be indirect.
  snapshot_sha256: e9a44359c5f74a9b1b417efef7502257711c6123f6000dbacfc5a6d6fb490a4a
- evidence_id: septin-p2348-septin-ring-agent-vargas2016-xml
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC5068138/?report=xml
  locator: PMC5068138 s1-3, s1-5 and s1-6, Figure1 textual legend; review tier, DOI10.1099/mic.0.000359
  accessed_at: '2026-11-03T03:23:25.152900Z'
  support: supports
  summary: Review supports broad fungal septin occurrence and functions in morphology,
    septation and development, while distinguishing species-dependent rod composition
    and Shs1-dependent assembly. Septin deletion often reduces rather than abolishes
    septation.
  snapshot_sha256: 0ea7d12c66842b8f1a2df75f121b17564b4eb283444a5d521c26fa184b8ff993
- evidence_id: septin-p2348-septin-adapter-catalogue
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Complete 20-organism / 28-dataset catalogue response; all organism names
    and dataset keys independently reread
  accessed_at: '2026-11-03T01:54:20.056965Z'
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  support: context_only
  search_scope: Official iModulonDB /api/datasets complete catalogue fetched 2026-11-03T01:54:20.056965Z
    and reused from this session; no query term, date filter or pagination limit;
    all 20 organism entries and 28 dataset keys inspected for Fungi, Saccharomyces
    cerevisiae/S288C and Candida albicans coverage. This is catalogue coverage only,
    never gene absence or structural-localization evidence.
  summary: Cached native catalogue has bacterial and archaeal organisms only; no organism/dataset
    key matches these fungal targets. Named genes make adapter discovery relevant
    under the rubric, but downstream organism-specific searches are not applicable
    after this bounded coverage check. Earlier runner PermissionError is a separate
    availability limitation, not the non-applicability basis.
- evidence_id: check-qc
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2348/qc.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T03:25:33.917006Z'
  support: supports
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  snapshot_sha256: f99f043c55cd066e876228d550e2e1e24ccca2bf6d3c02dafc2a2732ff08fbbe
- evidence_id: check-labels
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2348/labels.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T03:20:25.724101Z'
  support: supports
  summary: 4232 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  snapshot_sha256: d8200b370ec584f49336f01ed9035fbe21f0aa191ad0257a9a421938e9f17ecb
- evidence_id: check-trait-links
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2348/trait-links.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T03:20:03.158046Z'
  support: supports
  summary: Native TraitMech link check passed.
  snapshot_sha256: 8b336cdefbbd3daf6da8787990efdbe346c95e2c8361d50b7eb68a18f2d5a44a
- evidence_id: check-vendored
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2348/vendored.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T03:20:01.919183Z'
  support: supports
  summary: Pinned governed files match; native vendored check passed.
  snapshot_sha256: b1f169d103aaefa930745468bcca171e5867b9cc49e4e74311e458097e3252a6
- evidence_id: check-curies
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2348/curies.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T03:20:31.541909Z'
  support: supports
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  snapshot_sha256: fb3be251020aac118f6df680372ae7aaa32c2a1dd3366648cde95494f19d9dd2
- evidence_id: focused
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2348/focused-results.json
  locator: All twenty actual target schema/strict command outputs
  accessed_at: '2026-11-03T03:32:49Z'
  support: supports
  summary: Ten schema and ten strict commands returned exit zero.
  snapshot_sha256: 8aff133db75224ecadd5513c06af0c20739c2b2121f0ed506a226b8cd661df71
- evidence_id: supplemental-pmid
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2348/pmid-chunks-receipt.json
  locator: Complete native-report PMID set checked with unchanged resolver in batches
    of at most fifty
  accessed_at: '2026-11-03T03:21:18.719375Z'
  support: supports
  summary: 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers
    remain unverified.
  snapshot_sha256: 997a5c5812f2c0ca3e71b4f4407fc4497c0772d081abe204a687b72539ef09f4
- evidence_id: historical-adapter-runner-availability
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical runner invocation receipt, cross-checked against exact stdout/stderr
    hashes; reread during PR2348 synthesis
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  summary: Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS
    PermissionError reading the configured runner pyvenv.cfg. This is a retained historical
    availability observation, not a fresh attempt or a scientific validation failure.
    Native policy permits inspected source-catalogue fallback.
assessments:
- assessment_id: plaque-spb-current-identity
  area: identity
  topic: Whole fungal MTOC and bounded budding-yeast example
  outcome: supported
  summary: GO:0005816 exactly matches the whole SPB definition and SPB synonym. Species-specific
    evidence for budding yeast does not assert universal occurrence in every fungal
    cell. The whole organelle is distinct from its heterogeneous core, plaques and
    gamma-tubulin nucleators. CPX-1420 denotes only IL2 and CPX-1198 a species-specific
    small complex; neither is equivalent to the whole SPB.
  target_ids:
  - GO:0005816
  evidence_ids:
  - plaque-current-0
  - plaque-spb-agent-go
  - plaque-spb-agent-taxon
  - plaque-spb-agent-CPX-1198
  - plaque-spb-agent-CPX-1420
  - plaque-spb-agent-viswanath2017
- assessment_id: plaque-spb-current-function
  area: evidence
  topic: Nuclear/cytoplasmic nucleation and duplication topology
  outcome: supported
  summary: The scaffold connects both faces of the SPB to microtubule-nucleating complexes.
    Duplication and separation provide the two poles of a bipolar spindle. The old-to-new
    templates-assembly edge is explicitly NONMECHANISTIC and denotes neighboring assembly
    at the half bridge, without asserting exact protein transfer, a strictly conservative
    process, purified nucleation sufficiency or a complete molecular insertion mechanism.
  target_ids:
  - GO:0005816
  evidence_ids:
  - plaque-current-0
  - plaque-spb-agent-viswanath2017
  - plaque-spb-agent-adams1999
  - plaque-spb-agent-winey2012
  - plaque-spb-jaspersen-structure-cached
  - plaque-spb-jaspersen-duplication-fresh
  - plaque-spb-jaspersen-nucleation-fresh
- assessment_id: plaque-spb-current-grounding
  area: grounding
  topic: Persistent exact general gamma-tubulin complex grounding gap
  outcome: concern
  summary: The existing gamma_tubulin_complexes row is a broad multiprotein class,
    exactly covered by active GO:0000930. Deferring a narrower fungal small/ring or
    plaque-bound identifier does not justify withholding that general grounding. Original
    F1 remains confirmed/minor. Preserve the separately justified heterogeneous core
    and do not impose species-specific CPX composition or fixed stoichiometry.
  target_ids:
  - GO:0005816
  evidence_ids:
  - plaque-current-0
  - plaque-spb-agent-go
  - plaque-spb-agent-CPX-1198
  - plaque-curation-policy
- assessment_id: plaque-spb-core-model-scope
  area: scope
  topic: Primary integrative-model scope
  outcome: supported
  summary: Viswanath models CP/IL2 using structural, fluorescence and EM restraints,
    not the entire SPB at atomic resolution. The crystal constraint uses K. lactis
    calmodulin; tagged tomography rejects the initial two-layer Spc29 configuration.
    Revised core stoichiometry and proposed domain-swap/assembly mechanisms are explicitly
    interpretive. The record uses this source only for the layered core architecture
    and adds no quantitative or direct-binding claim.
  target_ids:
  - GO:0005816
  evidence_ids:
  - plaque-current-0
  - plaque-spb-agent-viswanath2017
- assessment_id: plaque-duplication-plaque-current
  area: identity
  topic: Expanded plaque intermediate and local satellite precursor
  outcome: supported
  summary: The local record denotes the transient cytoplasmic plaque formed after
    satellite expansion and before completed daughter-SPB maturation. It is distinct
    from the satellite, half bridge and whole SPB. The explicitly referenced satellite
    is an independently read current target with a frozen hash. Both NONMECHANISTIC
    graph edges preserve precursor direction; expansion can overlap insertion, so
    the three-stage narrative is not a strict ban on partial insertion during growth.
    No competing exact GO identity was established in the bounded first100 search.
  target_ids:
  - cellstructuremech:spindle_pole_body_duplication_plaque
  evidence_ids:
  - plaque-current-1
  - plaque-current-2
  - plaque-spb-agent-go
  - plaque-spb-agent-adams1999
  - plaque-spb-agent-winey2012
  - plaque-spb-jaspersen-duplication-fresh
  - plaque-spb-agent-go-duplication-search
- assessment_id: plaque-satellite-current
  area: identity
  topic: Early distal half-bridge precursor
  outcome: supported
  summary: The locally identified satellite is the early cytoplasmic precursor at
    the distal half-bridge tip, distinct from the mature SPB and bridge itself. Normal
    cycling-cell occurrence and budding-yeast scope are supported; COMMON is qualitative
    occurrence rather than a prevalence measurement. Its seeding function and two
    NONMECHANISTIC edges describe assembly topology without asserting autonomous microtubule
    nucleation or skipping the intervening plaque stage. No exact competing GO identity
    was established among the first100 query results.
  target_ids:
  - cellstructuremech:spindle_pole_body_satellite
  evidence_ids:
  - plaque-current-2
  - plaque-spb-agent-go
  - plaque-spb-agent-adams1999
  - plaque-spb-agent-winey2012
  - plaque-spb-jaspersen-duplication-fresh
  - plaque-spb-agent-go-satellite-search
  - plaque-spb-agent-taxon
- assessment_id: plaque-precursor-evidence-limits
  area: scope
  topic: Primary localization, stage inference and optional components
  outcome: supported
  summary: Adams serial EM/localization supports the precursor model, but shared composition
    and morphology do not directly trace an individual satellite into a plaque. Direct
    satellite Spc29, inferred plaque Spc29, tentative plaque Tub4, half-bridge Spc72/Tub4
    and post-insertion Spc110 remain distinct evidence scopes. Tagged K699/K842 derivatives,
    alpha-factor enrichment, fixation and altered-NLS overexpression do not establish
    universal composition or purified binding. The records deliberately leave optional
    component inventories unfilled; no consequential omission was found.
  target_ids:
  - cellstructuremech:spindle_pole_body_duplication_plaque
  - cellstructuremech:spindle_pole_body_satellite
  evidence_ids:
  - plaque-current-1
  - plaque-current-2
  - plaque-spb-agent-adams1999
  - plaque-spb-agent-winey2012
  - plaque-curation-policy
- assessment_id: plaque-source-adapter-coverage
  area: scope
  topic: Native organism/dataset applicability
  outcome: not_applicable
  summary: Fresh complete iModulonDB catalogue has no Saccharomyces dataset. These
    three records contain no gene symbols, protein accession examples, regulators
    or expression-module assertions; a gene/strain-specific expression-module search
    is not available. The old physical-subject rationale can be clarified with coverage
    evidence, but is not treated as a confirmed actionable bundle omission for these
    exact sparse targets. Catalogue absence is not biological evidence.
  target_ids:
  - GO:0005816
  - cellstructuremech:spindle_pole_body_duplication_plaque
  - cellstructuremech:spindle_pole_body_satellite
  evidence_ids:
  - plaque-current-0
  - plaque-current-1
  - plaque-current-2
  - plaque-spb-adapter-catalogue
- assessment_id: plaque-review-provenance
  area: provenance
  topic: Frozen inputs, source tiers and native artifacts
  outcome: supported
  summary: All three target hashes are unchanged. Native original YAML validation,
    Markdown roundtrip and historical source hashes pass. Adams1999 and Viswanath2017
    are primary evidence; Jaspersen2004 and Winey2012 are secondary syntheses. Fresh
    responses and one re-read cached browser passage preserve their real retrieval
    times and bytes. No tracked images or additional scientific neighbor beyond the
    assigned satellite were used.
  target_ids:
  - GO:0005816
  - cellstructuremech:spindle_pole_body_duplication_plaque
  - cellstructuremech:spindle_pole_body_satellite
  evidence_ids:
  - plaque-native-original-checks
  - plaque-spb-agent-epmc
  - plaque-spb-agent-adams1999
  - plaque-spb-agent-viswanath2017
  - plaque-spb-agent-winey2012
  - plaque-spb-jaspersen-structure-cached
- assessment_id: micro-gap-identity
  area: identity
  topic: Exact complex and separation from signaling states
  outcome: supported
  summary: GO:1990334 is exact; narrow Bfa1-Bub2 and Byr4-Cdc16 synonyms, GAP-complex
    parent and SPB parthood are bounded correctly. The broader SIN/MEN complex and
    its active/inhibited states are not substituted for the two-component GAP identity.
  target_ids:
  - GO:1990334
  evidence_ids:
  - micro-current-record-gap
  - micro-current-gap-prep-go
- assessment_id: micro-gap-function
  area: evidence
  topic: Tem1 inhibition and experimental scope
  outcome: supported
  summary: The primary study supports budding-yeast inhibition and orientation/checkpoint
    context without requiring the oversimplified claim that all checkpoint effects
    are exclusively GAP hydrolysis. W303-derived mutant/localization and in vitro
    assays do not independently demonstrate all fission-yeast details. The optional
    unresolved component-grounding TODO is disclosed, not fabricated as a complete
    molecular inventory.
  target_ids:
  - GO:1990334
  evidence_ids:
  - micro-current-record-gap
  - micro-current-gap-prep-fraschini-jats
  - micro-current-gap-prep-fraschini-meta
  - micro-current-gap-prep-tax-4932
- assessment_id: micro-sinister-identity
  area: identity
  topic: Native linker, taxon and protein identity
  outcome: supported
  summary: The observed basal-body-to-five-microtubule-root linker is distinct from
    neighboring fibers and mother-centriole-specific GO appendages. S. similis taxon,
    SAG culture bridge and unreviewed O49944/AJ001438 identity agree. Historical culture-label
    spelling is not overextended to the exact AJ001438 row.
  target_ids:
  - cellstructuremech:sinister_fiber
  evidence_ids:
  - micro-current-record-sinister
  - micro-current-sinister-prep-go
  - micro-current-sinister-prep-tax-3192
  - micro-current-sinister-prep-strain
  - micro-current-sinister-prep-O49944
- assessment_id: micro-sinister-assembly
  area: evidence
  topic: Native constituent versus in vitro reassembly
  outcome: supported
  summary: Antibody specificity and native immunogold support BAp95 membership. Purified
    recombinant reassembly under the documented dialysis conditions supports the experimental
    graph; proposed rod/ladder intermediates and physiological roles remain hypotheses,
    and no native essentiality is inferred. Figures5/7/8 were visually inspected and
    captions agree.
  target_ids:
  - cellstructuremech:sinister_fiber
  evidence_ids:
  - micro-current-record-sinister
  - micro-current-sinister-prep-geimer-s3
  - micro-current-sinister-prep-figure5
  - micro-current-sinister-prep-figure7
  - micro-current-sinister-prep-figure8
- assessment_id: micro-sinister-family
  area: grounding
  topic: Bounded exact-family search and image provenance
  outcome: supported
  summary: Exact accession and three literal InterPro text requests returned empty204
    responses. This supports a bounded unresolved exact-family mapping, not universal
    family absence; predicted coiled-coil similarity is not an exact family assignment.
    Link-only Figure7 attribution/licence and checksum agree with the inspected source.
  target_ids:
  - cellstructuremech:sinister_fiber
  evidence_ids:
  - micro-current-record-sinister
  - micro-current-interpro-family
  - micro-current-interpro-family-search
  - micro-current-interpro-family-search-sinister
  - micro-current-interpro-family-search-basal
  - micro-current-sinister-prep-geimer-s3
  - micro-current-sinister-prep-figure7
- assessment_id: micro-spindle-identity
  area: identity
  topic: Exact filament and nonmechanistic topology
  outcome: supported
  summary: The record is the spindle microtubule filament, with microtubule parent
    and spindle parthood. Its four nonmechanistic relationships separate SPB, kinetochore
    and mitotic spindle from tubulin constituents and preserve presumptive kinetochore
    interpretation.
  target_ids:
  - GO:0005876
  evidence_ids:
  - micro-current-record-spindle
  - micro-current-spindle-mt-prep-go
  - micro-current-spindle-mt-prep-winey-s3
- assessment_id: micro-spindle-components
  area: grounding
  topic: Combined tubulin material and exact examples
  outcome: supported
  summary: Reviewed S288c TUB1/P09733, TUB2/P02557 and TUB3/P09734 identities are
    independently confirmed, including bounded exact-gene searches. Combined alpha/beta
    lattice material can be essential without making the minor TUB3 paralog individually
    essential. No forced single-family accession or exhaustive MAP/motor inventory
    is required for the explicitly bounded combined component.
  target_ids:
  - GO:0005876
  evidence_ids:
  - micro-current-record-spindle
  - micro-current-spindle-mt-prep-P09733
  - micro-current-spindle-mt-prep-P02557
  - micro-current-spindle-mt-prep-P09734
  - micro-current-spindle-mt-prep-query-TUB1
  - micro-current-spindle-mt-prep-query-TUB2
  - micro-current-spindle-mt-prep-query-TUB3
  - micro-current-spindle-mt-agent-anders2001
- assessment_id: micro-spindle-scope
  area: scope
  topic: Fixed-cell reconstruction, live imaging and annotation provenance
  outcome: supported
  summary: Winey reconstruction used high-pressure freezing/freeze substitution, not
    live imaging or cryo-ET; Straight live GFP chromosome/spindle claims are verified
    only at abstract scope. Anders supports tubulin mutant/cytoskeleton claims; Cederquist
    tests G1 astral MT/Kip3 behavior and is retained only as native annotation provenance.
    Secondary Jaspersen context is labeled as such. Species and S288c strain remain
    distinct.
  target_ids:
  - GO:0005876
  evidence_ids:
  - micro-current-record-spindle
  - micro-current-spindle-mt-prep-winey-s3
  - micro-current-spindle-mt-prep-straight-meta
  - micro-current-spindle-mt-agent-anders2001
  - micro-current-spindle-mt-agent-cederquist2012
  - micro-current-jaspersen-secondary-context
  - micro-current-spindle-mt-prep-tax-4932
  - micro-current-spindle-mt-prep-tax-559292
- assessment_id: micro-spirostomum-identity
  area: identity
  topic: Extended cortical network and broad relations
  outcome: supported
  summary: Primary studies support a distinct Spirostomum extended myoneme mesh with
    broad intracellular-structure parent and cortical-cytoskeleton parthood. The literal
    QuickGO query does not establish exhaustive ontology absence. Mikus comparative
    passages remain secondary context and do not equate all centrin-rich cortical
    networks.
  target_ids:
  - cellstructuremech:spirostomum_myoneme_fishnet
  evidence_ids:
  - micro-current-record-spirostomum
  - micro-current-spirostomum-agent-zhang2023-jats
  - micro-current-spirostomum-agent-lannan2024-jats
  - micro-current-spirostomum-agent-go
  - micro-current-spirostomum-agent-go-myoneme-search
  - micro-current-spirostomum-agent-mikus2025-paper-pdf
- assessment_id: micro-spirostomum-components
  area: grounding
  topic: Spasmins, giant backbones and antibody boundaries
  outcome: supported
  summary: 'Evidence supports the two component classes and their carefully stated
    limits: anti-GSBP2 cross-reacts, anti-GSBP1 is specific, centrin antibodies do
    not resolve all paralogs, and IP is not a direct-contact map. Broader Centrin/CML
    and SFI1-like families are not exact mappings for the local component cohorts.
    No exact unverified accession or native stoichiometry is invented.'
  target_ids:
  - cellstructuremech:spirostomum_myoneme_fishnet
  evidence_ids:
  - micro-current-record-spirostomum
  - micro-current-spirostomum-agent-zhang2023-jats
  - micro-current-spirostomum-agent-lannan2024-jats
  - micro-current-spirostomum-agent-IPR050145
  - micro-current-spirostomum-agent-IPR052270
- assessment_id: micro-spirostomum-mechanism
  area: scope
  topic: Perturbation and versioned mechanism evidence
  outcome: supported
  summary: S. minus rare type-E RNAi-associated observations do not establish uniform
    depletion or essentiality. S. ambiguum preprint geometry/model and antibody evidence
    is kept distinct from the final2026 abstract’s qualitative purified-repeat observations.
    No final-paper numeric, Methods or full-figure claim is independently verified
    here. The record appropriately avoids a resolved force/recovery graph.
  target_ids:
  - cellstructuremech:spirostomum_myoneme_fishnet
  evidence_ids:
  - micro-current-record-spirostomum
  - micro-current-spirostomum-agent-zhang2023-jats
  - micro-current-spirostomum-agent-lannan2024-jats
  - micro-current-spirostomum-final2026-abstract
  - micro-current-spirostomum-agent-taxon-402029
  - micro-current-spirostomum-agent-taxon-37688
- assessment_id: micro-spirostomum-image
  area: provenance
  topic: Figure5 distinction and immutable source versions
  outcome: supported
  summary: Fresh visual inspection distinguishes predicted complex, localization and
    Western specificity panels. Link-only permissions and record MD5s match fresh
    versioned XML/image package metadata. The fixed2024 preprint is not silently replaced
    by the updated Europe PMC preprint abstract.
  target_ids:
  - cellstructuremech:spirostomum_myoneme_fishnet
  evidence_ids:
  - micro-current-record-spirostomum
  - micro-current-spirostomum-agent-figure5
  - micro-current-spirostomum-agent-zhang2023-package
  - micro-current-spirostomum-agent-lannan2024-package
  - micro-current-spirostomum-agent-epmc
- assessment_id: micro-four-target-frozen-inputs
  area: provenance
  topic: No stale targets or inherited scientific findings
  outcome: supported
  summary: All four current target byte hashes match the original frozen inputs. Each
    original verdict is pass_with_limitations with no findings. No scientific lineage
    is silently resolved or lost, and no stale scientific refresh is needed for these
    four.
  target_ids:
  - GO:1990334
  - cellstructuremech:sinister_fiber
  - GO:0005876
  - cellstructuremech:spirostomum_myoneme_fishnet
  evidence_ids:
  - micro-current-original-validation
  - micro-original-review-gap
  - micro-original-review-sinister
  - micro-original-review-spindle
  - micro-original-review-spirostomum
- assessment_id: micro-four-target-adapter-current-scope
  area: scope
  topic: Current structured-source coverage
  outcome: supported
  summary: Named proteins/genes trigger adapter consideration, even without expression-module
    claims. Fresh complete catalogue lacks matching target organisms/datasets, so
    target-specific module search is not_applicable without biological-negative inference.
    Root must pair this with its separately documented runner-availability check.
    Original exemption summaries need correction in the successor.
  target_ids:
  - GO:1990334
  - cellstructuremech:sinister_fiber
  - GO:0005876
  - cellstructuremech:spirostomum_myoneme_fishnet
  evidence_ids:
  - micro-current-adapter-policy
  - micro-current-current-adapter-catalogue
  - micro-original-review-gap
  - micro-original-review-sinister
  - micro-original-review-spindle
  - micro-original-review-spirostomum
- assessment_id: septin-septin-collar-identity
  area: identity
  topic: Generic hourglass collar and localized subtypes
  outcome: supported
  target_ids:
  - GO:0032173
  summary: GO0032173, exact hourglass synonym and septin-cytoskeleton parent agree.
    Bud-neck and invasive-hyphal collar terms are retained as narrower classes; the
    Saccharomyces example does not redefine the generic class or impose its filament
    arrangement on every subtype.
  evidence_ids:
  - septin-p2348-septin-collar-agent-go
  - septin-p2348-septin-collar-agent-kozubowski2005-xml
  - septin-p2348-collar-record
- assessment_id: septin-septin-collar-composition
  area: grounding
  topic: Five verified mitotic septin examples
  outcome: supported
  target_ids:
  - GO:0032173
  summary: All five accession identities, reviewed statuses, recommended labels, symbols
    and S288C taxon match native sources. Independent primary Introduction and review
    synthesis support the named mitotic collar cohort; the accession-only qualifiers
    are appropriate. ESSENTIAL denotes collective septin material, not a requirement
    for every paralog or universal cell viability.
  evidence_ids:
  - septin-p2348-septin-collar-agent-kozubowski2005-xml
  - septin-p2348-septin-collar-agent-versele-pmc
  - septin-p2348-septin-collar-agent-P32457
  - septin-p2348-septin-collar-agent-symbol-CDC3
  - septin-p2348-septin-collar-agent-P25342
  - septin-p2348-septin-collar-agent-symbol-CDC10
  - septin-p2348-septin-collar-agent-P32458
  - septin-p2348-septin-collar-agent-symbol-CDC11
  - septin-p2348-septin-collar-agent-P32468
  - septin-p2348-septin-collar-agent-symbol-CDC12
  - septin-p2348-septin-collar-agent-Q07657
  - septin-p2348-septin-collar-agent-symbol-SHS1
  - septin-p2348-collar-record
  - septin-p2348-policy
  - septin-p2348-example-policy
- assessment_id: septin-septin-collar-scope
  area: scope
  topic: Species example and strain identifiers
  outcome: supported
  target_ids:
  - GO:0032173
  summary: The S. cerevisiae occurrence and reporter example are supported by the
    cited primary paper. COMMON is qualitative occurrence in the named budding-cell
    context, not measured prevalence or a claim that every cell-cycle state contains
    a collar. S288C protein identities are sequence examples, not assertions that
    the JC482 experiments used S288C.
  evidence_ids:
  - septin-p2348-septin-collar-agent-kozubowski2005-xml
  - septin-p2348-septin-collar-agent-taxon-4932
  - septin-p2348-septin-collar-agent-taxon-559292
  - septin-p2348-collar-record
- assessment_id: septin-septin-collar-graph
  area: graph
  topic: Ring-to-collar descriptive topology
  outcome: supported
  target_ids:
  - GO:0032173
  summary: Both edges retain GO-backed septin material and budding-yeast ring expansion.
    NONMECHANISTIC scope does not claim an ordered recruitment pathway, direct Bni4/Kcc4
    binding or that collar formation initiates their asymmetry.
  evidence_ids:
  - septin-p2348-septin-collar-agent-go
  - septin-p2348-septin-collar-agent-kozubowski2005-xml
  - septin-p2348-septin-collar-agent-versele-pmc
  - septin-p2348-collar-record
- assessment_id: septin-septin-collar-family
  area: grounding
  topic: Generic Septin family versus localized cohort
  outcome: concern
  target_ids:
  - GO:0032173
  summary: The component is named septin proteins but its rationale withholds grounding
    until a family denotes the complete assembly-forming cohort. IPR016491 supplies
    the generic family identity; localized composition remains a separate scientific
    question.
  evidence_ids:
  - septin-p2348-septin-collar-agent-family
  - septin-p2348-collar-record
  - septin-p2348-policy
- assessment_id: septin-septin-collar-provenance
  area: provenance
  topic: Source tier and exact imported annotations
  outcome: supported
  target_ids:
  - GO:0032173
  summary: 'Independent PR #2348 review inspected the current record and genuine primary
    body prose at the listed locators. GO/InterPro/UniProt are identifier authorities.
    Douglas, Versele, Glomb, Bridges and Vargas are secondary syntheses where used.
    Huh/Mino/Finnigan were inspected here only via metadata/abstract and exact native
    UniProt citation attribution. Earlier cached bodies carry their original retrieval
    timestamps. Successful report=xml PMC responses contained article prose; Europe
    PMC HTTP 500 and PMC challenge responses were not used as scientific evidence.'
  evidence_ids:
  - septin-p2348-septin-collar-agent-paper-metadata
  - septin-p2348-septin-collar-agent-kozubowski2005-xml
  - septin-p2348-septin-collar-agent-versele-pmc
  - septin-p2348-septin-collar-agent-P32457
  - septin-p2348-septin-collar-agent-symbol-CDC3
  - septin-p2348-septin-collar-agent-P25342
  - septin-p2348-septin-collar-agent-symbol-CDC10
  - septin-p2348-septin-collar-agent-P32458
  - septin-p2348-septin-collar-agent-symbol-CDC11
  - septin-p2348-septin-collar-agent-P32468
  - septin-p2348-septin-collar-agent-symbol-CDC12
  - septin-p2348-septin-collar-agent-Q07657
  - septin-p2348-septin-collar-agent-symbol-SHS1
- assessment_id: septin-septin-collar-completeness
  area: completeness
  topic: Bounded record without invented inventory requirements
  outcome: supported
  target_ids:
  - GO:0032173
  summary: No complete accessory inventory, stoichiometry, dimensions, image license
    or recruitment mechanism is claimed. These absent optional details do not create
    additional findings; current scientific status is retained.
  evidence_ids:
  - septin-p2348-septin-collar-agent-go
  - septin-p2348-septin-collar-agent-kozubowski2005-xml
  - septin-p2348-collar-record
- assessment_id: septin-septin-filament-array-identity
  area: identity
  topic: Generic array and localized children
  outcome: supported
  target_ids:
  - GO:0032160
  summary: GO0032160 exactly matches the bar/filament-array definition, septin-cytoskeleton
    parent and cytoskeleton parthood. Prospore and chlamydospore terms remain narrower
    array classes; ring, collar and cap are distinguished rather than merged.
  evidence_ids:
  - septin-p2348-septin-collar-agent-go
  - septin-p2348-septin-array-agent-douglas-pmc
  - septin-p2348-filament-array-record
- assessment_id: septin-septin-filament-array-scope
  area: scope
  topic: Developmental species contexts
  outcome: supported
  target_ids:
  - GO:0032160
  summary: The GO-backed S. cerevisiae sporulation and C. albicans chlamydospore examples
    are accurately attributed, and VARIABLE preserves growth-stage dependence. Species
    identities and the S288C sequence-example strain are correct. Native GO does not
    constitute a primary experiment or a universal quantitative prevalence estimate.
  evidence_ids:
  - septin-p2348-septin-collar-agent-go
  - septin-p2348-septin-array-agent-douglas-pmc
  - septin-p2348-septin-array-agent-tachikawa2001
  - septin-p2348-septin-collar-agent-taxon-4932
  - septin-p2348-septin-collar-agent-taxon-559292
  - septin-p2348-septin-array-agent-taxon-5476
  - septin-p2348-filament-array-record
- assessment_id: septin-septin-filament-array-graph
  area: graph
  topic: Composition and membrane-localization topology
  outcome: supported
  target_ids:
  - GO:0032160
  summary: The three NONMECHANISTIC edges are supported at the generic-family and
    stated membrane-context levels. Bars are not assigned molecular thickness or treated
    as directly resolved single filaments; optical-sheet interpretation is retained.
    Neither Don1 rings nor a complete recruitment/force-generation mechanism is imported.
  evidence_ids:
  - septin-p2348-septin-collar-agent-go
  - septin-p2348-septin-array-agent-douglas-pmc
  - septin-p2348-septin-array-agent-tachikawa2001
  - septin-p2348-filament-array-record
- assessment_id: septin-septin-filament-array-sequence-identities
  area: grounding
  topic: Accurate accession identity and imported compartment notes
  outcome: supported
  target_ids:
  - GO:0032160
  summary: All five reviewed identities, labels, primary symbols, S288C taxon and
    exact-query uniqueness checks pass. Native UniProt supports the imported general
    membrane/bud-neck citations exactly. Those notes deliberately do not establish
    sporulation-array membership, and identity correctness is retained independently
    of the membership finding.
  evidence_ids:
  - septin-p2348-septin-collar-agent-P32457
  - septin-p2348-septin-collar-agent-symbol-CDC3
  - septin-p2348-septin-collar-agent-P25342
  - septin-p2348-septin-collar-agent-symbol-CDC10
  - septin-p2348-septin-collar-agent-P32458
  - septin-p2348-septin-collar-agent-symbol-CDC11
  - septin-p2348-septin-collar-agent-P32468
  - septin-p2348-septin-collar-agent-symbol-CDC12
  - septin-p2348-septin-collar-agent-Q07657
  - septin-p2348-septin-collar-agent-symbol-SHS1
  - septin-p2348-filament-array-record
  - septin-p2348-example-policy
- assessment_id: septin-septin-filament-array-family
  area: grounding
  topic: Generic Septin family versus localized cohort
  outcome: concern
  target_ids:
  - GO:0032160
  summary: The component is named septin proteins but its rationale withholds grounding
    until a family denotes the complete assembly-forming cohort. IPR016491 supplies
    the generic family identity; localized composition remains a separate scientific
    question.
  evidence_ids:
  - septin-p2348-septin-collar-agent-family
  - septin-p2348-filament-array-record
  - septin-p2348-policy
- assessment_id: septin-septin-filament-array-array-membership
  area: evidence
  topic: Mitotic examples versus the stated sporulation array
  outcome: concern
  target_ids:
  - GO:0032160
  summary: The current Saccharomyces example is specifically a prospore-membrane array,
    yet its component declares the full mitotic five-gene set. Primary imaging contradicts
    unqualified Cdc12/Shs1 assignment in that context. This does not establish their
    absence from every conceivable filament array or invalidate the three other accurate
    identities; Cdc11 detection in the PSM literature is retained.
  evidence_ids:
  - septin-p2348-septin-array-agent-mcmurray2008
  - septin-p2348-septin-array-agent-mcmurray2008-figure3
  - septin-p2348-septin-array-agent-garcia2016
  - septin-p2348-septin-collar-agent-versele-pmc
  - septin-p2348-septin-array-agent-douglas-pmc
  - septin-p2348-filament-array-record
  - septin-p2348-example-policy
- assessment_id: septin-septin-filament-array-provenance
  area: provenance
  topic: Ontology source chain and independent primary falsification
  outcome: supported
  target_ids:
  - GO:0032160
  summary: 'Independent PR #2348 review inspected the current record and genuine primary
    body prose at the listed locators. GO/InterPro/UniProt are identifier authorities.
    Douglas, Versele, Glomb, Bridges and Vargas are secondary syntheses where used.
    Huh/Mino/Finnigan were inspected here only via metadata/abstract and exact native
    UniProt citation attribution. Earlier cached bodies carry their original retrieval
    timestamps. Successful report=xml PMC responses contained article prose; Europe
    PMC HTTP 500 and PMC challenge responses were not used as scientific evidence.'
  evidence_ids:
  - septin-p2348-septin-collar-agent-go
  - septin-p2348-septin-array-agent-douglas-pmc
  - septin-p2348-septin-array-agent-tachikawa2001
  - septin-p2348-septin-array-agent-mcmurray2008
  - septin-p2348-septin-array-agent-garcia2016
  - septin-p2348-septin-collar-agent-paper-metadata
  - septin-p2348-filament-array-record
- assessment_id: septin-septin-ring-identity
  area: identity
  topic: Higher-order cortical ring versus smaller septin complexes
  outcome: supported
  target_ids:
  - GO:0005940
  summary: GO0005940 matches the defined higher-order ring, its septin-cytoskeleton
    parent and cell-cortex parthood. GO0031105 is a smaller oligomeric complex, appropriately
    retained as a distinct assembly level. The microbial record uses fungal examples
    without claiming that the GO class excludes animal rings.
  evidence_ids:
  - septin-p2348-septin-collar-agent-go
  - septin-p2348-septin-ring-agent-iwase2007-xml
  - septin-p2348-septin-ring-agent-glomb2016-xml
  - septin-p2348-ring-record
- assessment_id: septin-septin-ring-composition
  area: grounding
  topic: Five identity examples and mitotic structural cohort
  outcome: supported
  target_ids:
  - GO:0005940
  summary: All sequence identities, primary symbols, reviewed statuses, S288C taxon
    labels and uniqueness checks pass. Primary and review evidence supports the five
    mitotic bud-neck septins. General membrane/bud-neck annotations are not silently
    promoted to a different localization. Collective ESSENTIAL is not a claim that
    each paralog is individually necessary for every ring.
  evidence_ids:
  - septin-p2348-septin-ring-agent-iwase2007-xml
  - septin-p2348-septin-ring-agent-glomb2016-xml
  - septin-p2348-septin-collar-agent-P32457
  - septin-p2348-septin-collar-agent-symbol-CDC3
  - septin-p2348-septin-collar-agent-P25342
  - septin-p2348-septin-collar-agent-symbol-CDC10
  - septin-p2348-septin-collar-agent-P32458
  - septin-p2348-septin-collar-agent-symbol-CDC11
  - septin-p2348-septin-collar-agent-P32468
  - septin-p2348-septin-collar-agent-symbol-CDC12
  - septin-p2348-septin-collar-agent-Q07657
  - septin-p2348-septin-collar-agent-symbol-SHS1
  - septin-p2348-ring-record
  - septin-p2348-policy
  - septin-p2348-example-policy
- assessment_id: septin-septin-ring-scope
  area: scope
  topic: Fungal occurrence and Saccharomyces model
  outcome: supported
  target_ids:
  - GO:0005940
  summary: Native Fungi/species/strain identities agree. COMMON is a qualitative fungal
    occurrence statement with explicit variation by lineage and morphogenetic context,
    not universal occurrence, numerical prevalence or universal essentiality. The
    named Saccharomyces example is supported by Iwase; tested backgrounds are not
    equated to every S288C-derived strain.
  evidence_ids:
  - septin-p2348-septin-ring-agent-iwase2007-xml
  - septin-p2348-septin-ring-agent-bridges2014-xml
  - septin-p2348-septin-ring-agent-vargas2016-xml
  - septin-p2348-septin-collar-agent-taxon-4932
  - septin-p2348-septin-collar-agent-taxon-559292
  - septin-p2348-septin-ring-agent-taxon-4751
  - septin-p2348-ring-record
- assessment_id: septin-septin-ring-function
  area: evidence
  topic: Division-site scaffold and cytokinesis factors
  outcome: supported
  target_ids:
  - GO:0005940
  summary: Budding-yeast recruitment and cytokinesis-site organization have direct
    experimental support, while broader fungal scaffolding rests on reviews. The record
    does not claim direct binding for every cytokinesis factor or that septins generate
    constriction force or determine every fungal cleavage plane.
  evidence_ids:
  - septin-p2348-septin-ring-agent-iwase2007-xml
  - septin-p2348-septin-ring-agent-glomb2016-xml
  - septin-p2348-septin-ring-agent-bridges2014-xml
  - septin-p2348-septin-ring-agent-vargas2016-xml
  - septin-p2348-ring-record
- assessment_id: septin-septin-ring-graph
  area: graph
  topic: Scoped oligomer-to-filament-to-ring hierarchy
  outcome: supported
  target_ids:
  - GO:0005940
  summary: The NONMECHANISTIC graph is explicitly a Saccharomyces assembly hierarchy,
    supported by the reconstituted Cdc11-capped core and budding-cell localization.
    It does not specify all five paralogs in one octamer or a universal fungal rod
    order. Shs1-capped rods and viable alternative hexamers limit universal reading
    of the generic rod-to-filament edge; these documented exceptions are retained
    in this assessment.
  evidence_ids:
  - septin-p2348-septin-ring-agent-bertin2008-xml
  - septin-p2348-septin-ring-agent-mcmurray2011-xml
  - septin-p2348-septin-ring-agent-glomb2016-xml
  - septin-p2348-septin-ring-agent-vargas2016-xml
  - septin-p2348-septin-collar-agent-go
  - septin-p2348-ring-record
- assessment_id: septin-septin-ring-family
  area: grounding
  topic: Generic Septin family versus localized cohort
  outcome: concern
  target_ids:
  - GO:0005940
  summary: The component is named septin proteins but its rationale withholds grounding
    until a family denotes the complete assembly-forming cohort. IPR016491 supplies
    the generic family identity; localized composition remains a separate scientific
    question.
  evidence_ids:
  - septin-p2348-septin-collar-agent-family
  - septin-p2348-ring-record
  - septin-p2348-policy
- assessment_id: septin-septin-ring-provenance
  area: provenance
  topic: Primary experiments versus literature reviews
  outcome: supported
  target_ids:
  - GO:0005940
  summary: 'Independent PR #2348 review inspected the current record and genuine primary
    body prose at the listed locators. GO/InterPro/UniProt are identifier authorities.
    Douglas, Versele, Glomb, Bridges and Vargas are secondary syntheses where used.
    Huh/Mino/Finnigan were inspected here only via metadata/abstract and exact native
    UniProt citation attribution. Earlier cached bodies carry their original retrieval
    timestamps. Successful report=xml PMC responses contained article prose; Europe
    PMC HTTP 500 and PMC challenge responses were not used as scientific evidence.'
  evidence_ids:
  - septin-p2348-septin-collar-agent-paper-metadata
  - septin-p2348-septin-ring-agent-iwase2007-xml
  - septin-p2348-septin-ring-agent-bertin2008-xml
  - septin-p2348-septin-ring-agent-mcmurray2011-xml
  - septin-p2348-septin-ring-agent-glomb2016-xml
  - septin-p2348-septin-ring-agent-bridges2014-xml
  - septin-p2348-septin-ring-agent-vargas2016-xml
  - septin-p2348-septin-collar-agent-P32457
  - septin-p2348-septin-collar-agent-symbol-CDC3
  - septin-p2348-septin-collar-agent-P25342
  - septin-p2348-septin-collar-agent-symbol-CDC10
  - septin-p2348-septin-collar-agent-P32458
  - septin-p2348-septin-collar-agent-symbol-CDC11
  - septin-p2348-septin-collar-agent-P32468
  - septin-p2348-septin-collar-agent-symbol-CDC12
  - septin-p2348-septin-collar-agent-Q07657
  - septin-p2348-septin-collar-agent-symbol-SHS1
- assessment_id: septin-septin-ring-completeness
  area: completeness
  topic: Optional detailed composition and mechanism
  outcome: supported
  target_ids:
  - GO:0005940
  summary: No exhaustive accessory-protein list, molecular dimensions, image license
    or full ordered recruitment mechanism is asserted. Optional unresolved details
    and distinct localized ring subtypes do not create additional findings.
  evidence_ids:
  - septin-p2348-septin-collar-agent-go
  - septin-p2348-septin-ring-agent-iwase2007-xml
  - septin-p2348-septin-ring-agent-bertin2008-xml
  - septin-p2348-ring-record
- assessment_id: septin-septin-ring-staleness-refresh
  area: graph
  topic: Substantive reassessment of the 2026-10-31 filaments-to-ring edge
  outcome: supported
  target_ids:
  - GO:0005940
  evidence_ids:
  - septin-p2348-ring-record
  - septin-p2348-septin-collar-agent-go
  - septin-p2348-septin-ring-agent-glomb2016-xml
  - septin-p2348-septin-ring-agent-bridges2014-xml
  - septin-p2348-septin-ring-agent-bertin2008-xml
  - septin-p2348-septin-ring-agent-mcmurray2011-xml
  summary: 'The original ring input a29add3311f4b53bf4b50c2ec527d5ef450cfff625eadd312324d625b8790b93
    differs from current f536dd5b190f0cba77de3b14131a2bd5b9d12369a96c81014cc6b0c2ebf1361d
    by a curation event and the organize-into edge. Its explicitly Saccharomyces NONMECHANISTIC
    hierarchy is supported: Glomb describes cortical ring organization and ring expansion
    to the hourglass; Bertin reconstitutes paired core filaments; Bridges summarizes
    paired/gauze cortical arrays and membrane annealing. This is descriptive assembly/remodeling,
    not proof of one universal filament orientation, oligomer size, all-five-in-one
    rod or molecular recruitment mechanism. No additional scientific defect observed
    in the changed claim.'
- assessment_id: septin-septin-adapter-coverage
  area: provenance
  topic: Organism-coverage basis for downstream iModulonDB applicability
  outcome: supported
  target_ids:
  - GO:0032173
  - GO:0032160
  - GO:0005940
  evidence_ids:
  - septin-p2348-septin-adapter-catalogue
  summary: All three records declare named septin genes and require the structured-source
    discovery step. The independently reread cached official catalogue has no fungal
    dataset matching the records. Downstream gene/module queries therefore are not
    applicable for this scoped catalogue, with the original fetch time and separate
    historical runner limitation retained.
- assessment_id: current-input-comparison
  area: provenance
  topic: Complete frozen-input comparison and bounded refresh
  outcome: supported
  summary: 1 of ten original target hashes differ from current main. The changed content
    is substantively reassessed in the target-specific assessments; original observations
    remain historical and unchanged. All current target and used context bytes are
    frozen.
  target_ids:
  - GO:0032173
  - GO:0032160
  - GO:0005940
  - GO:1990334
  - cellstructuremech:sinister_fiber
  - GO:0005876
  - GO:0005816
  - cellstructuremech:spindle_pole_body_duplication_plaque
  - cellstructuremech:spindle_pole_body_satellite
  - cellstructuremech:spirostomum_myoneme_fishnet
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
- finding_id: plaque-F1
  issue_key: spindle-pole-body-gamma-tubulin-complex-grounding
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: The existing gamma-tubulin complex class has an exact GO grounding
  description: The component gamma_tubulin_complexes is REVIEWED_LABEL_ONLY, with
    notes deferring exact fungal small-complex or plaque-bound ring-complex identifiers.
    Native GO0000930 directly denotes the general multiprotein gamma-tubulin complex
    class already asserted by this component; its definition includes MTOC localization
    and nucleation, and its children distinguish small and ring complexes. Ground
    this existing broad row to GO:0000930, or document a concrete narrower scope mismatch
    if the intended row changes. This does not require species-specific CPX composition,
    an exhaustive inventory, or replacement of the heterogeneous core component.
  target_ids:
  - GO:0005816
  field_paths:
  - components[component_id=gamma_tubulin_complexes].grounding
  - components[component_id=gamma_tubulin_complexes].grounding_status
  - components[component_id=gamma_tubulin_complexes].grounding_notes
  evidence_ids:
  - plaque-spb-agent-go
  - plaque-spb-jaspersen-nucleation-fresh
  - plaque-current-0
  - plaque-curation-policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/spindle_pole_body.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Components
  native_severity: minor
  normalization_reason: The scientific identity and function remain supported; the
    defect is a resolvable exact grounding for an existing component class.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T082245Z-spindle-pole-body-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2531
- finding_id: septin-septin-collar-F1
  issue_key: septin-collar-generic-family-withheld
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Localized-cohort criterion leaves the generic Septin family ungrounded
  description: The generic septin-proteins component is REVIEWED_LABEL_ONLY because
    its rationale asks for an accession matching the complete localized cohort. Verified
    IPR016491 identifies the named Septin family without requiring a localization-specific
    family. Reconcile grounding, status and rationale while preserving separate uncertainty
    about exact paralogs and associated proteins.
  target_ids:
  - GO:0032173
  field_paths:
  - components[component_id=septin_proteins].grounding_status
  - components[component_id=septin_proteins].grounding_notes
  - discussions
  evidence_ids:
  - septin-p2348-septin-collar-agent-family
  - septin-p2348-collar-record
  - septin-p2348-policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/septin_collar.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Components
  native_severity: minor
  normalization_reason: A bounded generic-family mapping gap; exact structure identity
    and species-specific composition are separate.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T082244Z-septin-collar-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2499
- finding_id: septin-septin-filament-array-F1
  issue_key: septin-filament-array-generic-family-withheld
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Localized-cohort criterion leaves the generic Septin family ungrounded
  description: The generic septin-proteins component is REVIEWED_LABEL_ONLY because
    its rationale asks for an accession matching the complete localized cohort. Verified
    IPR016491 identifies the named Septin family without requiring a localization-specific
    family. Reconcile grounding, status and rationale while preserving separate uncertainty
    about exact paralogs and associated proteins.
  target_ids:
  - GO:0032160
  field_paths:
  - components[component_id=septin_proteins].grounding_status
  - components[component_id=septin_proteins].grounding_notes
  - discussions
  evidence_ids:
  - septin-p2348-septin-collar-agent-family
  - septin-p2348-filament-array-record
  - septin-p2348-policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/septin_filament_array.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Components
  native_severity: minor
  normalization_reason: A bounded generic-family mapping gap; exact structure identity
    and species-specific composition are separate.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T082244Z-septin-filament-array-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2499
- finding_id: septin-septin-filament-array-F2
  issue_key: septin-filament-array-mitotic-examples-in-sporulation-context
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Cdc12 and Shs1 examples are not supported in the stated Saccharomyces array
    context
  description: The only S. cerevisiae array context declared by this record is the
    prospore membrane during sporulation. Its septin component nevertheless includes
    CDC12/P32468 and SHS1/Q07657 as unqualified structural examples alongside the
    mitotic set. Their identities are correct, but primary dual-color localization
    finds little or no Cdc12 and no Shs1 in the Cdc10-marked sporulation structures;
    later work independently distinguishes the development-specific assembly. Restrict
    these assignments or provide direct evidence for an explicitly stated alternative
    array context. This is not an assertion that Cdc12/Shs1 cannot occur in any structure
    described loosely as an array, nor that the accessions are wrong.
  target_ids:
  - GO:0032160
  field_paths:
  - components[component_id=septin_proteins].gene_symbols
  - components[component_id=septin_proteins].protein_examples
  evidence_ids:
  - septin-p2348-septin-array-agent-mcmurray2008
  - septin-p2348-septin-array-agent-mcmurray2008-figure3
  - septin-p2348-septin-array-agent-garcia2016
  - septin-p2348-septin-collar-agent-versele-pmc
  - septin-p2348-septin-collar-agent-P32457
  - septin-p2348-septin-collar-agent-symbol-CDC3
  - septin-p2348-septin-collar-agent-P25342
  - septin-p2348-septin-collar-agent-symbol-CDC10
  - septin-p2348-septin-collar-agent-P32458
  - septin-p2348-septin-collar-agent-symbol-CDC11
  - septin-p2348-septin-collar-agent-P32468
  - septin-p2348-septin-collar-agent-symbol-CDC12
  - septin-p2348-septin-collar-agent-Q07657
  - septin-p2348-septin-collar-agent-symbol-SHS1
  - septin-p2348-filament-array-record
  - septin-p2348-example-policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/septin_filament_array.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Components
  native_severity: major
  normalization_reason: A material localized-component assignment conflicts with direct
    primary evidence in the specific developmental context that the record supplies;
    generic family membership does not resolve it.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T082244Z-septin-filament-array-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2530
- finding_id: septin-septin-ring-F1
  issue_key: septin-ring-generic-family-withheld
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Localized-cohort criterion leaves the generic Septin family ungrounded
  description: The generic septin-proteins component is REVIEWED_LABEL_ONLY because
    its rationale asks for an accession matching the complete localized cohort. Verified
    IPR016491 identifies the named Septin family without requiring a localization-specific
    family. Reconcile grounding, status and rationale while preserving separate uncertainty
    about exact paralogs and associated proteins.
  target_ids:
  - GO:0005940
  field_paths:
  - components[component_id=septin_proteins].grounding_status
  - components[component_id=septin_proteins].grounding_notes
  - discussions
  evidence_ids:
  - septin-p2348-septin-collar-agent-family
  - septin-p2348-ring-record
  - septin-p2348-policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/septin_ring.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Components
  native_severity: minor
  normalization_reason: A bounded generic-family mapping gap; exact structure identity
    and species-specific composition are separate.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T082244Z-septin-ring-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2499
actions:
- action_id: plaque-A1
  finding_ids:
  - plaque-F1
  target_ids:
  - GO:0005816
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/spindle_pole_body.yaml
    role: maintained scientific record
  description: In later authorized curation, add GO:0000930 to the existing gamma-tubulin-complex
    component and align grounding_status/notes with the verified general class. Preserve
    the specific small/ring and plaque-assembly limitations; do not equate a species-specific
    CPX entry with the whole SPB. Preserve historical discussion rationale and record
    any current progress in notes.
  acceptance_checks:
  - Compare the revised component scope against the active GO0000930 definition and
    its small/ring subtypes.
  - Retain the supported nuclear/cytoplasmic nucleation-site role without adding autonomous
    nucleation sufficiency or universal stoichiometry.
  - Run native schema, strict, label, history and generated-page checks after maintained-record
    curation.
  generator: Maintained structure YAML; just render derives pages.
- action_id: septin-septin-collar-A1
  finding_ids:
  - septin-septin-collar-F1
  target_ids:
  - GO:0032173
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/septin_collar.yaml
    role: maintained scientific record
  description: Under separately authorized curation, ground the generic Septin component
    to verified IPR016491 and reconcile the cohort-based rationale.
  acceptance_checks:
  - Retain separate membership evidence; do not infer universal paralog usage or stoichiometry
    from a family match.
  - Retain structure-level rather than individual-protein viability essentiality.
  - Use guarded curation/history and run native schema, strict, identifier-label,
    protein-example and rendered-page checks.
  generator: Maintained scientific YAML; generated pages derive through just render.
- action_id: septin-septin-filament-array-A1
  finding_ids:
  - septin-septin-filament-array-F1
  target_ids:
  - GO:0032160
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/septin_filament_array.yaml
    role: maintained scientific record
  description: Under separately authorized curation, ground the generic Septin component
    to verified IPR016491 and reconcile the cohort-based rationale.
  acceptance_checks:
  - Retain separate membership evidence; do not infer universal paralog usage or stoichiometry
    from a family match.
  - Retain structure-level rather than individual-protein viability essentiality.
  - Use guarded curation/history and run native schema, strict, identifier-label,
    protein-example and rendered-page checks.
  generator: Maintained scientific YAML; generated pages derive through just render.
- action_id: septin-septin-filament-array-A2
  finding_ids:
  - septin-septin-filament-array-F2
  target_ids:
  - GO:0032160
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/septin_filament_array.yaml
    role: maintained scientific record
  description: 'Under separately authorized curation, reconcile the CDC12 and SHS1
    symbols/examples with the stated S. cerevisiae sporulation-array scope: restrict/remove
    these structural assignments, or document a distinct source-supported context
    that actually fits this GO array class.'
  acceptance_checks:
  - Preserve correct accession identity and taxon information separately from structural
    membership.
  - Do not infer absence from every array architecture or remove Cdc11 solely from
    a modern core-rod model; published PSM detection is distinct from integral rod
    composition.
  - If adding Spr3/Spr28 as better-supported sporulation examples, verify their own
    exact native accession/taxon and localization evidence before editing.
  - Do not infer Candida paralog membership from Saccharomyces or impose an exhaustive
    inventory requirement.
  - Use guarded curation/history and run focused schema, strict, UniProt identity,
    label and generated-page checks.
  generator: Maintained scientific YAML; generated pages derive through just render.
- action_id: septin-septin-ring-A1
  finding_ids:
  - septin-septin-ring-F1
  target_ids:
  - GO:0005940
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/septin_ring.yaml
    role: maintained scientific record
  description: Under separately authorized curation, ground the generic Septin component
    to verified IPR016491 and reconcile the cohort-based rationale.
  acceptance_checks:
  - Retain separate membership evidence; do not infer universal paralog usage or stoichiometry
    from a family match.
  - Retain structure-level rather than individual-protein viability essentiality.
  - Use guarded curation/history and run native schema, strict, identifier-label,
    protein-example and rendered-page checks.
  generator: Maintained scientific YAML; generated pages derive through just render.
limitations:
- 'Spindle pole body, duplication plaque and satellite independent subreview: Assigned
  SPB/duplication-plaque/satellite subreview only. Global QC, strict/identifier/label
  gates and CI are parent-owned; this report attests only the original-bundle native
  checks it executed.'
- 'Spindle pole body, duplication plaque and satellite independent subreview: Adams1999
  claim-bearing main-text Methods/Results/Discussion were read. Microscopy pixels,
  raw serial-section data, every temperature-sensitive mutant experiment and all historical
  antecedents were not independently reanalyzed. Stage inference is not single-structure
  lineage tracing.'
- 'Spindle pole body, duplication plaque and satellite independent subreview: Viswanath2017
  Introduction, selected modeling Results, Discussion and specified Methods were read.
  Raw models, microscopy pixels, all validation equations and full supplementary datasets
  were not independently rerun or reaudited.'
- 'Spindle pole body, duplication plaque and satellite independent subreview: Jaspersen2004
  is a secondary author manuscript read through browser extraction. The structure
  passage is reused from the actual 2026-11-03T00:47:42Z fetch and was re-read; duplication
  and nucleation passages were freshly retrieved. Browser receipt hashes are not publisher-PDF
  hashes or native HTTP status evidence.'
- 'Spindle pole body, duplication plaque and satellite independent subreview: Winey2012
  PMC OA S3 returned404. The alternate native PMC HTML route succeeded and its claim-bearing
  duplication/separation section was read. This access limit is resolved for the reviewed
  claims, not hidden or called a successful S3 retrieval.'
- 'Spindle pole body, duplication plaque and satellite independent subreview: GO searches
  covered the first100 ID/name candidates for each exact query, on page1 of6. Remaining
  pages and every synonym were not exhaustively searched. No universal ontology-absence
  claim is made.'
- 'Spindle pole body, duplication plaque and satellite independent subreview: Complex
  Portal entries are narrowly scoped contextual candidates. Their participant lists
  are not transplanted into the record as universal SPB composition; no individual
  protein example is asserted by any of these three target records.'
- 'Spindle pole body, duplication plaque and satellite independent subreview: No new
  iModulonDB adapter CLI execution is claimed. The complete native catalogue was freshly
  retrieved and inspected; parent owns runner availability disclosure.'
- 'Spindle pole body, duplication plaque and satellite independent subreview: No tracked
  images were present in the fully read targets, and no scientific neighbor beyond
  the assigned satellite target was used. All local input paths are enumerated; cached
  external-response bytes are evidence snapshots, not maintained repository inputs.'
- 'SIN/MEN GAP complex, sinister fiber, spindle microtubule and Spirostomum myoneme
  independent subreview: All four assigned record inputs are unchanged. Fresh source
  retrieval receipts record actual UTC access and native bytes; no historical primary
  retrieval time is reused as a fresh download.'
- 'SIN/MEN GAP complex, sinister fiber, spindle microtubule and Spirostomum myoneme
  independent subreview: GAP: inspected Fraschini claim-relevant sections and Methods
  listed in evidence, not all raw experimental data. Budding-yeast study does not
  directly verify every fission-yeast branch detail. No complete constituent inventory
  is asserted.'
- 'SIN/MEN GAP complex, sinister fiber, spindle microtubule and Spirostomum myoneme
  independent subreview: Sinister: complete claim-bearing primary Results/Discussion
  and relevant Methods plus Figure5/7/8 pixels inspected. No raw microscopy data or
  unlisted supplement was inspected. Exact-family checks are bounded to one protein
  endpoint and three literal text queries; they are not exhaustive homology coverage.'
- 'SIN/MEN GAP complex, sinister fiber, spindle microtubule and Spirostomum myoneme
  independent subreview: Spindle: Winey PDF selected claim-bearing sections were text-inspected;
  its figure pixels/raw tomography were not independently reinspected. Straight1997
  is fresh abstract-only verification, not a new full-text read. Anders and Cederquist
  were inspected in the specified abstract/Results/Methods passages, not exhaustively.
  Jaspersen is secondary cached browser text, not fresh publisher full text or primary
  evidence.'
- 'SIN/MEN GAP complex, sinister fiber, spindle microtubule and Spirostomum myoneme
  independent subreview: Spirostomum: Zhang2023 claim-bearing Results/Discussion/relevant
  Methods and Figure5 pixels were inspected. Versioned Lannan2024 main-text claim-relevant
  sections were inspected, but supplementary Methods/raw data and its figure pixels
  were not freshly inspected.'
- 'SIN/MEN GAP complex, sinister fiber, spindle microtubule and Spirostomum myoneme
  independent subreview: Spirostomum final2026: the fresh native Europe PMC abstract
  supports only qualitative abstract-level claims. Europe PMC final fullTextXML returned500;
  PMC returned a200 browser challenge; publisher browsing returned403. No fresh embargo
  date, final Methods, final figures/supplement or quantitative condition was verified.
  The original reported embargo remains historical, not independently reproduced.'
- 'SIN/MEN GAP complex, sinister fiber, spindle microtubule and Spirostomum myoneme
  independent subreview: Spirostomum: Mikus2025 PDF passages are secondary comparative
  context for Spirostomum, not new primary local evidence; the broader InterPro family
  descriptions do not establish exact local-component identities.'
- 'SIN/MEN GAP complex, sinister fiber, spindle microtubule and Spirostomum myoneme
  independent subreview: Structured sources: fresh complete iModulonDB catalogue coverage
  was inspected; no matching organisms/datasets exist within that returned list. Runner
  availability is root-owned evidence. Lack of dataset coverage is not evidence against
  the biological assemblies.'
- 'SIN/MEN GAP complex, sinister fiber, spindle microtubule and Spirostomum myoneme
  independent subreview: Original bundles: native validation and exact rendering were
  independently checked. Full corpus QC/identifier/label/history gates are run by
  root; this report does not relabel historical check results as fresh global checks.'
- 'Septin collar, filament array and ring independent subreview: This independent
  slice covers only septin collar, septin filament array and septin ring; all source-access
  and image limitations below are scoped to those three targets.'
- 'Septin collar, filament array and ring independent subreview: Three generic-family
  findings and the confirmed major sporulation-array composition finding remain open
  record curation; no record was edited and no historical scientific issue was closed.'
- 'Septin collar, filament array and ring independent subreview: The filament-array
  finding concerns the stated S. cerevisiae sporulation/prospore context. It is not
  an exclusion of Cdc12 or Shs1 from every possible septin array. Cdc11 detection
  at PSM and membership of the reconstituted meiotic core are distinct and were not
  conflated.'
- 'Septin collar, filament array and ring independent subreview: Primary McMurray
  2008 Figure 3 was visually inspected with its caption and Results. Other article
  bodies and selected legends were inspected, but microscopy pixels, raw movies, supplements
  and quantitative analyses were not independently reanalyzed.'
- 'Septin collar, filament array and ring independent subreview: The C. albicans chlamydospore
  array is corroborated at exact GO and Douglas secondary-review tiers. Its original
  microscopy was not reanalyzed. Tachikawa sheet geometry is measured on Gip1 with
  Spr28 colocalization, not direct single-filament resolution.'
- 'Septin collar, filament array and ring independent subreview: Huh 2003, Finnigan
  2015 and Mino 1998 were accessed at metadata/abstract and native-UniProt-attribution
  tier in this slice; no claim that their full primary bodies were reread.'
- 'Septin collar, filament array and ring independent subreview: The changed septin-ring
  edge is accepted within its expressly budding-yeast descriptive hierarchy. Pairing
  and cortical architecture are corroborated by reconstitution plus secondary synthesis,
  without claiming new in-vivo imaging analysis, universal architecture or every paralog
  being individually essential.'
- 'Septin collar, filament array and ring independent subreview: IPR016491, Douglas,
  Versele, Tachikawa and the official iModulonDB catalogue use independently reread
  cached native responses with actual earlier fetch times and hashes, not fresh retrieval
  claims.'
- 'Septin collar, filament array and ring independent subreview: Seven Europe PMC
  XML requests returned HTTP 500 and alternate pdf=render routes returned browser-challenge
  HTML. Genuine PMC report=xml HTML provided all seven full bodies; failed/challenged
  bytes are not scientific evidence. A scratch HTML parser dependency was absent,
  so standard-library HTML parsing was used; no repository check failed.'
- 'Septin collar, filament array and ring independent subreview: No new structured
  runner invocation was performed: root retains the canary runner PermissionError
  receipt. Downstream non-applicability rests on the bounded organism catalogue rather
  than lack of transcriptomic claims.'
- 'Septin collar, filament array and ring independent subreview: Corpus QC, strict
  corpus resolvers and final-head CI are root-owned gates, not claimed as executed
  by this independent subreview. Original three bundle validation/render checks passed;
  historical check receipts are not relabeled as current.'
- Historical observations remain immutable; their old checks are not represented as
  current-head execution.
- The adapter runner was not rerun after the canary established OS access failure.
  Catalogue-based coverage is assessed directly; fresh and reused responses retain
  actual access timestamps.
- Native label checks include 923 no-adapter skips. Native identifier checks include
  909 PMID transport failures and 254 skipped identifiers; bounded supplemental checks
  independently resolve the 909 PMIDs.
- Scientific findings and native status are unchanged; proposed curation belongs in
  separate record PRs.
- Final trusted-base post-save review-check, exact-head independent acceptance, final-head
  CI and merge-group CI occur after saving this immutable observation and are not
  represented here as already completed.
notes:
- All ten original YAML/Markdown pairs are preserved unchanged. Current main was merged
  normally and pushed without force.
- One explicit issue-bearing ten-record cohort follows the repository persistence
  policy. Supported records are assessed within that cohort without fabricated findings.
- 'Bundle issues #2529 (stale septin-ring review) and #2532 (seven unsupported adapter
  exemption rationales) are addressed here. Scientific curation remains in #2499 (three
  same-class findings consolidated), #2530 and #2531; existing validator #2514 remains
  open.'
- Source commit c5d2d7e40e573b342332ef2b1203de1089602637 is retained by tag review-base/pr2348-current-record-followup-20261103.
- CLAUDE.md is an alias of AGENTS.md; canonical regular AGENTS.md bytes are frozen.
- Every inherited source-access and check limitation is attributed to its independent
  subreview. Fresh fetches, cached response re-reading, abstract-only evidence and
  full-body passages retain distinct scopes.
- The seven original adapter checks exist; the repaired defect is their unsupported
  exemption rationale. The three sparse spindle-pole/plaque/satellite records are
  excluded from that defect.
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T082244Z-septin-collar-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T082244Z-septin-filament-array-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T082244Z-septin-ring-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T082245Z-sin-men-two-component-gap-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T082245Z-sinister-fiber-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T082245Z-spindle-microtubule-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T082245Z-spindle-pole-body-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T082245Z-spindle-pole-body-duplication-plaque-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T082245Z-spindle-pole-body-satellite-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T082245Z-spirostomum-myoneme-fishnet-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
links:
- https://github.com/CultureBotAI/CellStructureMech/pull/2348
- https://github.com/CultureBotAI/CellStructureMech/issues/2499
- https://github.com/CultureBotAI/CellStructureMech/issues/2514
- https://github.com/CultureBotAI/CellStructureMech/issues/2529
- https://github.com/CultureBotAI/CellStructureMech/issues/2530
- https://github.com/CultureBotAI/CellStructureMech/issues/2531
- https://github.com/CultureBotAI/CellStructureMech/issues/2532
```
