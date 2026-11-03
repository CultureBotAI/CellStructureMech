# PR 2349: current-input review of ten records and adversarial follow-up

- Review: 20261103T040543Z-pr2349-current-record-followup
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-11-03T03:55:46.382715Z
- Finished UTC: 2026-11-03T04:05:43Z
- Reviewer: Codex root synthesis with three independent read-only adversarial reviewers (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Current-input reassessment of all ten records in PR2349. Stalk-spasmoneme causal descriptions and the telocentrosome gamma-tubulin-complex node type changed; both are substantively supported within their stated source scopes. Nine records have qualified supported assessments and split septin rings retain one minor confirmed generic-family grounding finding. The follow-up preserves exact finding lineage, refreshes both stale reviews and corrects structured-source applicability evidence for eight bundles; no scientific record is edited.

## Scope And Provenance

Exact ten-record PR cohort reassessed against current main de546d03939c0b16c12dcadb1472827e1468df7a. Changed inputs are substantively reassessed. Scientific records remain unchanged.

Selection: Complete cohort of ten maintained records reviewed in original PR head 4eddad83ec3549a0dd735f9868ce44981d6b2973.
Coverage: full; 10 reviewed / 10 in the declared population.
Source: working_tree at Git base 67d0dd66fe04472c58f4ad9c8b860df18a9f5f8a.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0032176 | data/structures/cytoskeleton/split_septin_rings.yaml | maintained | split septin rings |
| cellstructuremech:stalk_spasmoneme | data/structures/cytoskeleton/stalk_spasmoneme.yaml | maintained | Stalk spasmoneme |
| cellstructuremech:stentor_km_fiber | data/structures/cytoskeleton/stentor_km_fiber.yaml | maintained | Stentor Km fiber |
| cellstructuremech:stentor_perialgal_microtubule_meshwork | data/structures/cytoskeleton/stentor_perialgal_microtubule_meshwork.yaml | maintained | Stentor perialgal microtubule meshwork |
| GO:0070850 | data/structures/cytoskeleton/tacc_tog_complex.yaml | maintained | TACC/TOG complex |
| cellstructuremech:telocentrosome | data/structures/cytoskeleton/telocentrosome.yaml | maintained | telocentrosome |
| cellstructuremech:transition_zone_stellate_fiber_system | data/structures/cytoskeleton/transition_zone_stellate_fiber_system.yaml | maintained | transition zone stellate fiber system |
| cellstructuremech:tubulin_spool | data/structures/cytoskeleton/tubulin_spool.yaml | maintained | tubulin spool |
| GO:0097595 | data/structures/cytoskeleton/ventral_disc_crossbridge.yaml | maintained | ventral disc crossbridge |
| GO:0097594 | data/structures/cytoskeleton/ventral_disc_dorsal_microribbon.yaml | maintained | ventral disc dorsal microribbon |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full native QC | passed | True | GO:0032176, cellstructuremech:stalk_spasmoneme, cellstructuremech:stentor_km_fiber, cellstructuremech:stentor_perialgal_microtubule_meshwork, GO:0070850, cellstructuremech:telocentrosome, cellstructuremech:transition_zone_stellate_fiber_system, cellstructuremech:tubulin_spool, GO:0097595, GO:0097594 | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| Native label correspondence | passed | True | GO:0032176, cellstructuremech:stalk_spasmoneme, cellstructuremech:stentor_km_fiber, cellstructuremech:stentor_perialgal_microtubule_meshwork, GO:0070850, cellstructuremech:telocentrosome, cellstructuremech:transition_zone_stellate_fiber_system, cellstructuremech:tubulin_spool, GO:0097595, GO:0097594 | 4232 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| TraitMech references | passed | True | GO:0032176, cellstructuremech:stalk_spasmoneme, cellstructuremech:stentor_km_fiber, cellstructuremech:stentor_perialgal_microtubule_meshwork, GO:0070850, cellstructuremech:telocentrosome, cellstructuremech:transition_zone_stellate_fiber_system, cellstructuremech:tubulin_spool, GO:0097595, GO:0097594 | Native TraitMech link check passed. |
| Pinned governed files | passed | True | GO:0032176, cellstructuremech:stalk_spasmoneme, cellstructuremech:stentor_km_fiber, cellstructuremech:stentor_perialgal_microtubule_meshwork, GO:0070850, cellstructuremech:telocentrosome, cellstructuremech:transition_zone_stellate_fiber_system, cellstructuremech:tubulin_spool, GO:0097595, GO:0097594 | Pinned governed files match; native vendored check passed. |
| Native identifier resolver | passed | True | GO:0032176, cellstructuremech:stalk_spasmoneme, cellstructuremech:stentor_km_fiber, cellstructuremech:stentor_perialgal_microtubule_meshwork, GO:0070850, cellstructuremech:telocentrosome, cellstructuremech:transition_zone_stellate_fiber_system, cellstructuremech:tubulin_spool, GO:0097595, GO:0097594 | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| validate GO:0032176 | passed | True | GO:0032176 | Documented focused command passed. |
| validate-strict GO:0032176 | passed | True | GO:0032176 | Documented focused command passed. |
| validate cellstructuremech:stalk_spasmoneme | passed | True | cellstructuremech:stalk_spasmoneme | Documented focused command passed. |
| validate-strict cellstructuremech:stalk_spasmoneme | passed | True | cellstructuremech:stalk_spasmoneme | Documented focused command passed. |
| validate cellstructuremech:stentor_km_fiber | passed | True | cellstructuremech:stentor_km_fiber | Documented focused command passed. |
| validate-strict cellstructuremech:stentor_km_fiber | passed | True | cellstructuremech:stentor_km_fiber | Documented focused command passed. |
| validate cellstructuremech:stentor_perialgal_microtubule_meshwork | passed | True | cellstructuremech:stentor_perialgal_microtubule_meshwork | Documented focused command passed. |
| validate-strict cellstructuremech:stentor_perialgal_microtubule_meshwork | passed | True | cellstructuremech:stentor_perialgal_microtubule_meshwork | Documented focused command passed. |
| validate GO:0070850 | passed | True | GO:0070850 | Documented focused command passed. |
| validate-strict GO:0070850 | passed | True | GO:0070850 | Documented focused command passed. |
| validate cellstructuremech:telocentrosome | passed | True | cellstructuremech:telocentrosome | Documented focused command passed. |
| validate-strict cellstructuremech:telocentrosome | passed | True | cellstructuremech:telocentrosome | Documented focused command passed. |
| validate cellstructuremech:transition_zone_stellate_fiber_system | passed | True | cellstructuremech:transition_zone_stellate_fiber_system | Documented focused command passed. |
| validate-strict cellstructuremech:transition_zone_stellate_fiber_system | passed | True | cellstructuremech:transition_zone_stellate_fiber_system | Documented focused command passed. |
| validate cellstructuremech:tubulin_spool | passed | True | cellstructuremech:tubulin_spool | Documented focused command passed. |
| validate-strict cellstructuremech:tubulin_spool | passed | True | cellstructuremech:tubulin_spool | Documented focused command passed. |
| validate GO:0097595 | passed | True | GO:0097595 | Documented focused command passed. |
| validate-strict GO:0097595 | passed | True | GO:0097595 | Documented focused command passed. |
| validate GO:0097594 | passed | True | GO:0097594 | Documented focused command passed. |
| validate-strict GO:0097594 | passed | True | GO:0097594 | Documented focused command passed. |
| Supplemental bounded PMID authority checks | passed | True | GO:0032176, cellstructuremech:stalk_spasmoneme, cellstructuremech:stentor_km_fiber, cellstructuremech:stentor_perialgal_microtubule_meshwork, GO:0070850, cellstructuremech:telocentrosome, cellstructuremech:transition_zone_stellate_fiber_system, cellstructuremech:tubulin_spool, GO:0097595, GO:0097594 | 909 PMIDs all OK in bounded native requests; full-command limitations remain separate. |
| Official structured-source catalogue coverage | not_applicable | False | GO:0032176, cellstructuremech:stalk_spasmoneme, cellstructuremech:stentor_km_fiber, cellstructuremech:stentor_perialgal_microtubule_meshwork, GO:0070850, cellstructuremech:telocentrosome, cellstructuremech:transition_zone_stellate_fiber_system, cellstructuremech:tubulin_spool, GO:0097595, GO:0097594 | Official catalogue coverage contains 20 organisms and 28 datasets, all bacterial/archaeal; none matches this yeast/protist cohort. Fresh and independently reread cached catalogue responses retain actual access times and boundaries. The historical runner failure is documented separately; no new runner execution is claimed. |
| Independent claim-level source review | passed | True | GO:0032176, cellstructuremech:stalk_spasmoneme, cellstructuremech:stentor_km_fiber, cellstructuremech:stentor_perialgal_microtubule_meshwork, GO:0070850, cellstructuremech:telocentrosome, cellstructuremech:transition_zone_stellate_fiber_system, cellstructuremech:tubulin_spool, GO:0097595, GO:0097594 | Three read-only reviewers covered the complete ten-record cohort, including changed inputs, with explicit scientific findings and source-access limits. Final artifact/head acceptance occurs after saving. |
| Retained historical adapter runner availability | unavailable | False | cellstructuremech:stalk_spasmoneme, cellstructuremech:stentor_km_fiber, cellstructuremech:stentor_perialgal_microtubule_meshwork, GO:0070850, cellstructuremech:telocentrosome, cellstructuremech:transition_zone_stellate_fiber_system, cellstructuremech:tubulin_spool, GO:0097594 | Historical 00:49Z invocation unavailable due to OS access restriction. Official catalogue source fallback was inspected separately; no current invocation or successful adapter execution is claimed. The actual historical exit code 1 is retained in the evidence receipt, since the native unavailable-check model has no execution exit-code field. |

## Scientific And Domain Assessments

### Stalk organelle, family scope and preparation boundaries

identity: supported. Targets: cellstructuremech:stalk_spasmoneme.

The intracellular composite stalk organelle is distinct from sheath and continuous body myonemes. Spasmin-rich fractions and compartment immunolabeling support the combined centrin/spasmin class; broader IPR050145 is explicitly not an exact match. Native inventory, assembly essentiality and proposed spaconnectin/Sfi1 scaffold remain unresolved. Canonical V. convallaria and C. polypinum identities match authorities. Jiang2025 abstract places only CCDC specifically in sheath; EGF-like proteins remain stalk-level, with neither promoted into spasmoneme membership.

### Substantive refresh of three newly described response edges

graph: supported. Targets: cellstructuremech:stalk_spasmoneme.

The three added descriptions were reassessed: Routledge1978 supports calcium-responsive glycerinated preparations, with preparation/pH-dependent rates rather than a universal rapid kinetic constant; Ryu2012 supports Vorticella coiling/retraction and reduced excursion/prolonged contraction under imposed channel-flow resistance. The graph explicitly separates glycerinated calcium tests from live V. convallaria load experiments and remains FUNCTION/NONMECHANISTIC. No molecular motor, channel, serial force-additive architecture or ATP-independent live recovery is asserted. Staleness is refreshable without editing the record.

### Exact CIL preview and bounded image interpretation

provenance: supported. Targets: cellstructuremech:stalk_spasmoneme.

Native item identity, species, creator, public-domain status and preview match the record. Fresh JPEG exactly matches frozen tracked bytes and visually supports morphology only. The current catalogue date differs by one day from the original historical review; the record asserts only year2012, which remains supported. No raw-archive quality, exact stalk level, protein-specific signal or scale-derived dimensions are inferred.

### Overlapping cortical ribbon bundle and tubulin family identities

identity: supported. Targets: cellstructuremech:stentor_km_fiber.

Primary morphology supports a longitudinal overlapping ribbon bundle in S. coeruleus, distinct from a single microtubule, basal body, deeper myoneme and striated ciliary rootlet. The broad GO microtubule-bundle parent and cortical parthood are appropriate. IPR002452/IPR002453 identify alpha/beta families, not native paralog inventories, essential subunits or a bridge motor. Genus-qualified identity is not a claim of genus-wide prevalence.

### Fixed-state sliding inference versus broad tubulin intervention

graph: supported. Targets: cellstructuremech:stentor_km_fiber.

The record appropriately says implicated in re-extension and keeps bridge-driven sliding a model. Fixed-state overlap changes and opposing myoneme behavior do not identify a native ATPase or dynein; selective interventions were unsuccessful. Beta-tubulin RNAi does produce cortical-row breaks and disorientation, as the explicitly NONMECHANISTIC graph states. Mob1 diffuse cortical localization is not Km membership, and its perturbation phenotypes are not transferred to tubulin.

### Printed Figure8, page anchor and link-only licence

provenance: supported. Targets: cellstructuremech:stentor_km_fiber.

Complete PDF page8/printed711 visibly contains the described extended-cell transverse Km fiber, numbering diagram and0.1micrometer bar. Native package PDF/XML checksums match; JATS specifies CC BY-NC-SA4.0. The record links the printed figure and does not invent an XML figure identity or host/adapt a copy.

### Host irregular meshwork and directly stained beta-tubulin

identity: supported. Targets: cellstructuremech:stentor_perialgal_microtubule_meshwork.

Boudreau2025 supports an irregular host cortical meshwork with gaps occupied by algal vacuoles, distinct from regular individual cages, Km bundles, vacuole membranes and algal cells. Beta-tubulin T0198 staining supports the declared partial family inventory, not paralogs or linkers. S. pyriformis identity is supported by the source18S analysis and authority; host structure remains separate from independently culturable Chlorella.

### Proposed positioning without selective causal proof

evidence: supported. Targets: cellstructuremech:stentor_perialgal_microtubule_meshwork.

Spatial association and return after bulk centrifugation support a cortical-positioning hypothesis, not a selective requirement of the meshwork for anchoring, photosynthetic benefits, photoprotection, gas exchange or phototaxis. The qualified function, open discussion and absence of a mechanistic causal graph preserve that distinction; acknowledged unknown composition and linker identities are not new defects.

### Native Figure3 A/B and structured licence incompleteness

provenance: supported. Targets: cellstructuremech:stentor_perialgal_microtubule_meshwork.

The visually inspected native figure and PDF page6 caption agree with F3 and record A/B labels: chlorophyll/beta-tubulin images plus six sections through expanded mesh. Exact XML/PDF/JPEG MD5 values match metadata. Copyright explicitly grants CC BY4.0 while licence_code remains null; the record preserves link-only use and its hosting guard. Expanded distances are not native measurements.

### Organism/dataset coverage establishes source-adapter applicability

provenance: supported. Targets: cellstructuremech:stalk_spasmoneme, cellstructuremech:stentor_km_fiber, cellstructuremech:stentor_perialgal_microtubule_meshwork.

The original physical-structure/no-expression rationale was insufficient because these records name candidate proteins or regulators. The fresh complete returned catalogue lacks all assigned ciliate genera, so organism-specific iModulonDB queries are not applicable; coverage absence is not a biological negative. Root separately records runner availability and its actual historical attempt without claiming a new CLI run.

### Luminal assembly and distinct neighboring structures

identity: supported. Targets: cellstructuremech:transition_zone_stellate_fiber_system.

Local luminal-fiber identity, OTHER kind and broad parent/enclosing-transition-zone parthood are supported. Central cylinder, Y-links, external transition fibers, centrin arm and distal sleeve are distinct. The literal GO query is bounded, not an exhaustive absence proof.

### Centrin membership, sequence bridge and family scope

grounding: supported. Targets: cellstructuremech:transition_zone_stellate_fiber_system.

Reviewed P05434 identity, pCaBP4/source bridge and pleiotropic mutant/revertant evidence support centrin membership. The inspected families extend beyond the local constituent class; absence of a primary gene symbol is correctly preserved. No molecular sufficiency or universal essentiality is inferred.

### Extracted-cell response and unresolved excision disagreement

graph: supported. Targets: cellstructuremech:transition_zone_stellate_fiber_system.

The five graph edges preserve composition, A3 attachment and calcium-triggered condensation/inward doublet displacement. The1994 detergent-model experiment supports this bounded response. Jarvik abstract counterevidence, residual TableI excision and broader katanin preparations do not justify universal necessary/sufficient severing by centrin; the record explicitly retains that conflict.

### Strains, link-only Figure2 and licence

provenance: supported. Targets: cellstructuremech:transition_zone_stellate_fiber_system.

Species3055 is valid and137c/isolate416 are assay labels, not inferred culture accessions. Figure2 A–F and TableI were freshly visually checked. PDFpage3/0.2µm/extended-versus-condensed comparison and CC BY-NC-SA permissions agree. No tracked image or new clade-wide distribution is implied.

### Shape-bearing tubulin-positive assembly

identity: supported. Targets: cellstructuremech:tubulin_spool.

Primary U-ExM supports the local spool identity and generic Tubulin component. The broad GO relations and IPR000217 scope are appropriate without exact genes, fixed subtype stoichiometry, standard lattice topology or assumed centrin/DNA constituents.

### Culture and pinned specimen annotations

provenance: supported. Targets: cellstructuremech:tubulin_spool.

RCC10719/Takayama/P22-120, row1384 E7Ab/interphase/one-species/Yes and the exact pinned volume agree. Mixed RCC3511/RCC10719 filenames do not establish synonymy or spool occurrence in Biecheleriopsis. The volumes project, three channel sources, category annotations and archive link are verified without raw-volume reanalysis or prevalence inference.

### Observed morphology versus hypothesis and scale uncertainty

scope: supported. Targets: cellstructuremech:tubulin_spool.

Tracked image and fresh publisher bytes match; D–E alone supply spool panels. Fixed-cell expanded immunofluorescence does not establish live dynamics, desmose-mediated function, universal two-spool counts or exact lattice. The unresolved Figure2-versus-Methods scale conflict is explicit and no native dimensions are asserted. CC BY4.0 is supported by article and VOR metadata.

### Exact horizontal link and disc parthood

identity: supported. Targets: GO:0097595.

Exact GO crossbridge identity and part_of direction agree with primary lateral-link observations. The graph separates crossbridges from dorsal microribbons, microtubules, within-complex B bridge and whole disc.

### Bounded structural linkage with unresolved composition

scope: supported. Targets: GO:0097595.

WBC6 trophozoite cryo-ET of extracted flattened discs supports neighboring-ribbon linkage. Flexible crossbridge densities and discussion hypotheses do not demonstrate ATP/calcium-driven contraction, identify crossbridge proteins or establish sufficiency for attachment. Empty components and the explicit TODO are justified; qualitative COMMON is not measured prevalence.

### Trilaminar scaffold and four nonmechanistic relationships

graph: supported. Targets: GO:0097594.

Exact GO identity/synonym scopes, disc parthood and the four directed composition/topology edges are supported. Microribbons extend from microtubules and link laterally through crossbridges. The GO-derived mass range/tubulin exclusion is not relabeled as a new primary assay. No contractile mechanism, sheet-specific assignment or complete inventory is added.

### Primary localization versus family-cohort mapping

grounding: supported. Targets: GO:0097594.

Hagen directly supports beta-/delta-giardin and SALP-1 association, while Schwartz provides primary architecture and secondary composition context. IPR008374/PF06705 map beta/delta candidates; the inspected SALP-1 record and historical table do not establish the same full-cohort accession. Retaining an explicitly unresolved broad cohort is defensible; absent annotation does not disprove homology. Finer optional rows are not mandatory repairs.

### Species aliases, strain and preparation limits

scope: supported. Targets: GO:0097594.

Giardia intestinalis/lamblia are valid synonyms of species5741; WBC6 ATCC50803 is distinct strain evidence. Extracted-cytoskeleton tomography and tagged-protein immunolabeling establish architecture/association, not purified-protein reconstitution, exclusive composition, uniform turnover or all-stage/all-strain occurrence.

### Unchanged targets and empty original findings

provenance: supported. Targets: cellstructuremech:transition_zone_stellate_fiber_system, cellstructuremech:tubulin_spool, GO:0097595, GO:0097594.

All4 targets match original frozen hashes; original native validation/render passes. Every original verdict is pass_with_limitations with no findings, so no scientific issue lineage has been silently closed. Current assessments retain the original scientific boundaries.

### Corrected applicability for named constituents

scope: supported. Targets: cellstructuremech:transition_zone_stellate_fiber_system, cellstructuremech:tubulin_spool, GO:0097595, GO:0097594.

Stellate, spool and microribbon name proteins/accessions and need structured-source applicability documentation. The inspected complete catalogue has no matching organism/dataset; no module lookup or negative biological inference follows. Root runner evidence is separate. Crossbridge has no named molecular constituent or regulator and is excluded from the defect.

### Split-ring identity and hierarchy

identity: supported. Targets: GO:0032176.

GO:0032176 precisely denotes the paired rings, distinct from the single ring/collar and broader septin cytoskeleton; GO parent and part_of directions are retained.

### Generic Septin family

grounding: concern. Targets: GO:0032176.

The broad septin_proteins component remains incorrectly label-only for a local-cohort reason; IPR016491 is exactly the already-named generic Septin class. Preserve predecessor F1 and track through #2499.

### Split-ring morphology and bounded cytokinesis function

evidence: supported. Targets: GO:0032176.

The nonmechanistic assemble/split/flank graph and cautious thought-to-trap wording are supported by GO and the inspected secondary reviews. Collective structural necessity does not assert that every paralogue is essential; no exact paralogue membership or taxa are added.

### Split-ring adapter scope

scope: supported. Targets: GO:0032176.

This sparse record contains generic septin material without named genes or accessions. Do not allege the richer-record named-molecule exemption defect here; the current catalogue additionally lacks the eukaryotic context.

### TACC/TOG identity, products and family scope

identity: supported. Targets: GO:0070850.

GO:0070850 denotes the complex; Alp7 Q9URY2 and Alp14 O94534 are reviewed 972h- products and synonyms are verified. IPR045110 is XMAP215 family, whereas Alp7 IPR024312 is only a C-terminal domain and PF12709 coiled coil. Ndc80 Q10198 is graph context, not a third constituent; no universal 2:2 stoichiometry is claimed.

### Alp7/Alp14 polymerization and nucleation

evidence: supported. Targets: GO:0070850.

2016 purified association and tip occupancy support the first mechanism; 2018 Alp7-dependent MTOC recruitment/nucleation with retained plus-end tracking supports the second. The record correctly discloses conflicting deletion elongation observations and the engineered partial rescue; it does not universalize either context.

### Kinetochore attachment and transport graphs

graph: supported. Targets: GO:0070850.

Ndc80 F420S reduces Alp7/14 kinetochore signal by 30–40% and peptide/coIP/forced tethering experiments support bounded recruitment. Alp14 L615A export and Alp7 five-site phosphorylation/import phenotypes retain binding and residual import; Cut15 fragment two-hybrid is model support, and NLS growth rescue is not full spindle restoration.

### Dis1 and figure provenance

scope: supported. Targets: GO:0070850.

2019 forced targeting at endogenous expression fails reciprocal substitution while earlier overexpression compensation is explicitly retained. Figure 7 byte-matches the frozen image and depicts mixed-source purified TIRF material; CC BY 4.0 and caption scope match.

### Telocentrosome identity and exact accession boundaries

identity: supported. Targets: cellstructuremech:telocentrosome.

Local identity is appropriate for the telomere-associated MTOC, distinct from SPB, bouquet and narrower SUN/KASH tether. Eight molecular/example identities match native reviewed 972h- entries; Mto1 and Ssm4 homonyms are disambiguated. SUN1-5 and Tctex1 are exact family classes; Kms1, Kms2, Mto1, cytoplasmic Dhc1 and Ssm4 have honestly bounded label-only reasons.

### Substantive stale telocentrosome refresh

graph: supported. Targets: cellstructuremech:telocentrosome.

The sole scientific change is gamma_tuc node_type GENE_OR_PROTEIN to STRUCTURE, with its curation event. GO:0000930 is a multi-protein complex and Yoshida images Alp4 as a reporter, so current type STRUCTURE is supported. Reassessed all retained causal claims against primary sources; refresh must bind current SHA7eb101d9 rather than reuse old SHA05d5a42e or historical 4/4 protein-node coverage.

### Meiotic assembly and recruitment limits

evidence: supported. Targets: cellstructuremech:telocentrosome.

Primary imaging and perturbation establish cytoplasmic telomeric nucleation separate from Sid4-marked SPB. Kms1/Mto1 and Dlc1 contribute to Alp4 recruitment; Dhc1 dispensability is confined to that readout. Crosslinked-motor gathering is a proposed model. Upstream Bqt1/Bqt2/Rap1/Taz1 context is not a universal absence assertion, and no unsupported Mto2/all-gammaTuC/dynactin expansion is made.

### Ectopic 2025 assembly and image evidence

scope: supported. Targets: cellstructuremech:telocentrosome.

Ectopic Bqt1/Bqt2 in Rabl-deficient haploid mitotic cells yields partial Sad1/Kms1/Mto1/Alp4 recruitment without detected Dhc1 or complete bouquet, and Kms1 loss suppresses some phenotypes. Record avoids normal mitotic-generalization. Figure 2 pixel content, source hash and CC BY-NC-SA 3.0 licence agree; experimental stocks are not conflated with reference UniProt strain.

### Named-molecule structured-adapter applicability

scope: concern. Targets: GO:0070850.

The original non-transcriptomic exemption does not satisfy the current skill for named molecular cases. Fresh full official catalogue has 20 organisms/28 datasets and no S. pombe; this is the defensible downstream non-applicability basis. No new local runner execution is asserted; use the root historical runner receipt explicitly if needed.

### Named-molecule structured-adapter applicability

scope: concern. Targets: cellstructuremech:telocentrosome.

The original non-transcriptomic exemption does not satisfy the current skill for named molecular cases. Fresh full official catalogue has 20 organisms/28 datasets and no S. pombe; this is the defensible downstream non-applicability basis. No new local runner execution is asserted; use the root historical runner receipt explicitly if needed.

### Complete frozen-input comparison and bounded refresh

provenance: supported. Targets: GO:0032176, cellstructuremech:stalk_spasmoneme, cellstructuremech:stentor_km_fiber, cellstructuremech:stentor_perialgal_microtubule_meshwork, GO:0070850, cellstructuremech:telocentrosome, cellstructuremech:transition_zone_stellate_fiber_system, cellstructuremech:tubulin_spool, GO:0097595, GO:0097594.

2 of ten original target hashes differ from current main. The changed content is substantively reassessed in the target-specific assessments; original observations remain historical and unchanged. All current target and used context bytes are frozen.

## Findings

### septin-S2349-F1: The generic septin component has an exact family grounding

minor / open / confirmed; issue key: split-septin-rings-generic-family-withheld.

The septin_proteins row is REVIEWED_LABEL_ONLY because no family accession was assigned for the complete split-ring-forming cohort. Native IPR016491 directly represents the generic Septin family already named by the row. Assigning this class does not require determining which paralogues remain in a particular split pair or asserting that every family member forms this structure. Ground the generic row to InterPro:IPR016491 and retain exact membership as an open question.

## Recommended Actions And Acceptance Checks

### septin-S2349-AC1

In authorized curation, ground the septin-proteins row to InterPro:IPR016491 and align grounding status and notes. Preserve historical discussion rationale and record current progress in notes; retain unresolved localized cohort and individual essentiality limits.

- Compare component scope against native IPR016491 family description.
- Do not add unverified paralogue examples or universal assembly necessity.
- Run native schema, strict, label, history and generated-page checks after maintained-record changes.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| current-record-0 | data/structures/cytoskeleton/split_septin_rings.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 580abb6f00c144e871e1fded7fbb2dca8584ecf0d47a599f646558642c3027ff; current SHA256 580abb6f00c144e871e1fded7fbb2dca8584ecf0d47a599f646558642c3027ff. Record bytes unchanged since the original review. |
| original-review-0 | reviews/structured/20261021T084039Z-split-septin-rings-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-1 | data/structures/cytoskeleton/stalk_spasmoneme.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 42e090ec489b240c6b061368c7f44eba2267b46642bff54ef7c860e9e7eb7151; current SHA256 a3de4646f57551323b08c225176359cf3737eff71eaab9da598131d646920bdb. Changed record reassessed against current sources. |
| original-review-1 | reviews/structured/20261021T084039Z-stalk-spasmoneme-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-2 | data/structures/cytoskeleton/stentor_km_fiber.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 66b91b45477653bcafdf1f875b9820681ea1bdeddf36f9d37f74fabe9408cae6; current SHA256 66b91b45477653bcafdf1f875b9820681ea1bdeddf36f9d37f74fabe9408cae6. Record bytes unchanged since the original review. |
| original-review-2 | reviews/structured/20261021T084040Z-stentor-km-fiber-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-3 | data/structures/cytoskeleton/stentor_perialgal_microtubule_meshwork.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 3a0c8634cf4fca1f7d9253d399b2f6d343d806cd6e3b81e5d92ebf6ff9ab7daf; current SHA256 3a0c8634cf4fca1f7d9253d399b2f6d343d806cd6e3b81e5d92ebf6ff9ab7daf. Record bytes unchanged since the original review. |
| original-review-3 | reviews/structured/20261021T084040Z-stentor-perialgal-microtubule-meshwork-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-4 | data/structures/cytoskeleton/tacc_tog_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 7d2c57864f3928f8ab9bbc0d7e702aa142292ae00252b385f40a5a8dbcd7b787; current SHA256 7d2c57864f3928f8ab9bbc0d7e702aa142292ae00252b385f40a5a8dbcd7b787. Record bytes unchanged since the original review. |
| original-review-4 | reviews/structured/20261021T084040Z-tacc-tog-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-5 | data/structures/cytoskeleton/telocentrosome.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 05d5a42ee4b63bd62b3e8c6c0137e2268964980fcc00f27769e29498cf67dca7; current SHA256 7eb101d943b736d756d5ea90d304e6cc2b6dc59a11224203f2c5e7ea30cabc8b. Changed record reassessed against current sources. |
| original-review-5 | reviews/structured/20261021T084040Z-telocentrosome-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-6 | data/structures/cytoskeleton/transition_zone_stellate_fiber_system.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 ee5fc36bcda7810c550cfef29146f6b124f79703e6b73832b6f005583884ba36; current SHA256 ee5fc36bcda7810c550cfef29146f6b124f79703e6b73832b6f005583884ba36. Record bytes unchanged since the original review. |
| original-review-6 | reviews/structured/20261021T084040Z-transition-zone-stellate-fiber-system-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-7 | data/structures/cytoskeleton/tubulin_spool.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 1180c5c0b3a5c67f58a23b99913f7b78202beb8cf3e01c40ca5aac9c56dcf072; current SHA256 1180c5c0b3a5c67f58a23b99913f7b78202beb8cf3e01c40ca5aac9c56dcf072. Record bytes unchanged since the original review. |
| original-review-7 | reviews/structured/20261021T084041Z-tubulin-spool-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-8 | data/structures/cytoskeleton/ventral_disc_crossbridge.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 bb35ddad7c8b15916d19fa6e5ad334ca3476221330372020fdf4adc8565db67b; current SHA256 bb35ddad7c8b15916d19fa6e5ad334ca3476221330372020fdf4adc8565db67b. Record bytes unchanged since the original review. |
| original-review-8 | reviews/structured/20261021T084041Z-ventral-disc-crossbridge-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-9 | data/structures/cytoskeleton/ventral_disc_dorsal_microribbon.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 6bcdbfaaf84c4b6152147340dcbb6f5958d6dc6aca2288e034c3f2c357819425; current SHA256 6bcdbfaaf84c4b6152147340dcbb6f5958d6dc6aca2288e034c3f2c357819425. Record bytes unchanged since the original review. |
| original-review-9 | reviews/structured/20261021T084041Z-ventral-disc-dorsal-microribbon-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| plaque-stalk-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005622; results GO0005622 name, definition and isObsolete; freshly retrieved exact source bytes at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/stalk-agent-go.source | supports | GO0005622 is active intracellular anatomical structure. The broad is-a parent is compatible with the stalk-contained organelle; it is not an exact spasmoneme identifier. |
| plaque-stalk-agent-taxon-60850 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/60850; Native taxId, scientificName, species rank and lineage; freshly retrieved exact source bytes at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/stalk-agent-taxon-60850.source | supports | NCBITaxon60850 identifies Vorticella convallaria at species rank. |
| plaque-stalk-agent-taxon-168244 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/168244; Native taxId, scientificName, species rank and lineage; freshly retrieved exact source bytes at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/stalk-agent-taxon-168244.source | supports | NCBITaxon168244 identifies Carchesium polypinum at species rank. |
| plaque-stalk-agent-IPR050145 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050145/; Native metadata accession/name/type/description, including description provenance flags; fresh source snapshot in /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/stalk-agent-IPR050145.source | supports | IPR050145 is the broader Centrin/CML-like family, including caltractin, obelin and plant CML proteins. Its description is labelled llm=true, checked=true by InterPro. This authority check establishes entry scope, not exact native spasmin membership; the record appropriately leaves the narrower class REVIEWED_LABEL_ONLY and uses primary experiments for biology. |
| plaque-stalk-agent-literature-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=100&amp;query=DOI%3A%2210.1083/jcb.77.2.358%22%20OR%20DOI%3A%2210.1111/j.1550-7408.1999.tb04601.x%22%20OR%20DOI%3A%2210.1016/j.bpj.2012.07.038%22%20OR%20DOI%3A%2210.1111/j.1550-7408.1998.tb05066.x%22%20OR%20DOI%3A%2210.1111/jeu.70006%22; resultList.result DOI/title/authors/year/PMID/abstractText; abstract-tier scientific support for1999/2025; freshly retrieved exact source bytes at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/stalk-agent-literature-metadata.source | supports | Four exact DOI identities and abstracts recovered: Routledge1978 PMID418073, Maciejewski1999 PMID10361738, Ryu2012 PMID23009835, Jiang2025 PMID40059491. The 1999 abstract supports cloned/recombinant calcium-binding spasmin and 1F5 immunolocalization. The 2025 abstract supports CCDC and EGF-like stalk membership but specifically places only CCDC proteins in the sheath; neither demonstrates spasmoneme membership. The 1998 DOI was not returned by this bounded query, and is verified separately at the publisher. |
| plaque-stalk-primary-agent-routledge-native-pdf | https://pmc-oa-opendata.s3.amazonaws.com/PMC2110051.1/PMC2110051.1.pdf; PDF pp358-360 introduction and preparation/extraction Methods; pp361-364 extraction, protease-inhibitor control and calcium response Results; pp366-368 cross-genus morphology and limitations Discussion; fresh source snapshot in /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/stalk-primary-agent-routledge-native-pdf.source | supports | Primary article supports calcium-responsive glycerinated organelles and spasmin-rich extracted fractions, with unidentified proteins and incomplete reconstruction. The p363 Carchesium control responds normally to high/low calcium; p364 explicitly notes slow contraction at pH9. Rapid contraction is introductory context, not a preparation-independent measured rate. Genera differ in stalk coiling/folding; sheath and body continuity do not erase organelle boundaries. No absolute actin/tubulin absence is inferred. |
| plaque-stalk-primary-agent-konior-pdf | https://ilacadofsci.com/wp-content/uploads/2013/03/102-15MS2905-print.pdf; Main Methods pp163-165, Results/Discussion pp165-167, legends Figures2-8 pp170-174; no raw immunogold recount; fresh source snapshot in /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/stalk-primary-agent-konior-pdf.source | supports | Fresh primary PDF text supports distinct centrin/spasmin antibody patterns: N-termVcCentrin4 detects one Western band; 1F5 detects two. Both label fibrillar mass, with differing tubular localization and sheath-access requirements. Sfi1-like backbone, calcium-storage/structural roles and disassembly/reassembly remain a proposed model, not an identified native assembly or stoichiometry. |
| plaque-stalk-primary-agent-ryu-pdf | https://lab.prd.vanderbilt.edu/lang-lab/wp-content/uploads/sites/195/2023/01/MaximalForceCharacteristicsoftheCa2D-PoweredActuatorofVorticellaconvallaria2012.pdf; Primary main PDF pp860-866 introduction, channel-flow Methods, Results and Discussion; Figures1-5 captions; Supporting Material not read; fresh source snapshot in /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/stalk-primary-agent-ryu-pdf.source | supports | Live V. convallaria microfluidic channel experiments directly support slower contraction and less cell excursion as resistance rises (p862). Stalk coiling and retraction describe Vorticella, not universal folding behavior of all peritrich genera. Residual force is inferred hydrodynamically and maximal tension extrapolated; work omits terms, and serial force addition/motor-unit organization is hypothetical. These observations support the three newly added descriptions only within the graph's stated preparation/species and NONMECHANISTIC scope. |
| plaque-stalk-agent-cil39509-curl | https://www.cellimagelibrary.org/images/39509; Native landing-page JSON-LD, Description, Licensing, Biological Sources, Imaging and sample preparation; fresh source snapshot in /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/stalk-agent-cil39509-curl.source | supports | CIL39509 supports DOI10.7295/W9CIL39509, Richard Allen/Hawaii attribution, V. convallaria, TEM acquisition February15,1972, public-domain status and the exact preview URL. Current JSON-LD datePublished is January23,2012; the original review's January22 statement is a historical metadata observation. The record asserts only2012, so no current record correction follows. Physiological claims cited by image metadata are not demonstrated by this image. |
| plaque-stalk-agent-cil-preview | https://cildata.crbs.ucsd.edu/media/thumbnail_display/39509/39509_thumbnailx512.jpg; Entire source-served JPEG; visual inspection of identically hashed tracked image after native inspect added it; fresh source snapshot in /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/stalk-agent-cil-preview.source | supports | Fresh source JPEG exactly matches tracked cil_39509.jpg SHA2569055d5484ed8919c2a9f831c72eca12efd73abc294db7f017beb448ee45554c2. The inspected preview shows a spasmoneme profile with tubules and neighboring cortex. No protein-specific localization, calcium transport, calibrated dimensions or precise stalk level is inferred. |
| plaque-stentor-km-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097427,GO:0030863,GO:0035253; Exact three results, definition, name, isObsolete and synonyms; freshly retrieved exact source bytes at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/stentor-km-agent-go.source | supports | Active GO0097427 is the broader arrangement of closely apposed parallel microtubules. GO0030863 denotes cortical cytoskeleton. GO0035253 denotes a typically striated ciliary rootlet, not an exact identifier for the described overlapping ribbon bundle. Parthood of the local structure is supported by microscopy, not an asserted native GO link to a minted term. |
| plaque-stentor-km-agent-IPR002452 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002452/; metadata accession/name/type/description; family identity and alpha/beta microtubule composition; freshly retrieved exact source bytes at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/stentor-km-agent-IPR002452.source | supports | IPR002452 is the Alpha tubulin family and supports alpha/beta heterodimer composition of microtubules. |
| plaque-perialgal-prep-IPR002453 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002453/; metadata accession/name/type/description; family identity and alpha/beta microtubule composition; freshly retrieved exact source bytes at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/perialgal-prep-IPR002453.source | supports | IPR002453 is the Beta tubulin family. It is a family-class grounding, not a native Stentor paralogue census or bridge-motor identity. |
| plaque-stentor-km-agent-taxon-5963 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5963; taxId/scientificName/rank/lineage/otherNames; freshly retrieved exact source bytes at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/stentor-km-agent-taxon-5963.source | supports | NCBITaxon5963 is Stentor coeruleus at species rank; historical names and lineage are explicit. No experimental strain or genus-wide prevalence is inferred. |
| plaque-stentor-km-agent-literature-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=100&amp;query=DOI%3A%2210.1083/jcb.57.3.704%22%20OR%20DOI%3A%2210.1371/journal.pbio.1001861%22; Two native core result entries title/DOI/authors/year/PMID/PMCID; freshly retrieved exact source bytes at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/stentor-km-agent-literature-metadata.source | supports | Exact identities verified: Huang/Pitelka1973 DOI10.1083/jcb.57.3.704 PMID4633444 PMC2108994; Slabodnick et al.2014 DOI10.1371/journal.pbio.1001861 PMID24823688 PMC4019465. Both are primary studies; metadata abstracts do not replace the inspected bodies. |
| plaque-stentor-km-agent-huang1973-pdf | https://pmc-oa-opendata.s3.amazonaws.com/PMC2108994.1/PMC2108994.1.pdf; Primary PDF pp704-706 introduction/Methods; pp708-711 cortical organization; pp715-717 overlap Results; pp719-724 discussion through bridge-motor limits; complete PDF page8/printed711 Figure8 visually inspected; fresh source snapshot in /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/stentor-km-agent-huang1973-pdf.source | supports | Successive posterior-basal-body-associated microtubule ribbons overlap along cortical rows, distinct from deeper myonemes and transverse microtubules. Fixed extended cells have less overlap; active relative sliding is a model, selective disruptions were unsuccessful, and bridge ATPase/dynein identity lacks direct evidence. Figure8 is the extended-cell transverse Km bundle with numbering diagram and a printed0.1micrometer scale bar. |
| plaque-stentor-km-agent-huang1973-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC2108994.1/PMC2108994.1.xml; JATS article identity and permissions; PDF/XML MD5 values checked against current native package; fresh source snapshot in /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/stentor-km-agent-huang1973-jats.source | supports | Native JATS identifies Huang/Pitelka1973 and explicitly CC BY-NC-SA4.0. The image remains a link to printed Figure8 on PDF page8; no separately invented XML figure accession or repository hosting is asserted. |
| plaque-stentor-km-agent-huang1973-package | https://pmc-oa-opendata.s3.amazonaws.com/PMC2108994.1/PMC2108994.1.json; Version, DOI/PMID, retraction/licence flags, PDF/XML paths and MD5; fresh source snapshot in /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/stentor-km-agent-huang1973-package.source | supports | Version1 metadata identifies PMC2108994/PMID4633444 and DOI10.1083/jcb.57.3.704; is_retracted=false. Downloaded PDF MD5895cb427cb5cf8cc9afac7f76f59802d and XML MD580e819ecc2c76fdcf38709fe760b7d44 exactly match metadata. The precise4.0 licence is supplied by JATS. |
| plaque-stentor-km-agent-slabodnick2014 | https://journals.plos.org/plosbiology/article/file?id=10.1371/journal.pbio.1001861&amp;type=manuscript; Publisher XML Results s2b and s2c, Figures2/3 legends; culture/RNAi/qPCR/antibody/IF Methods s4a,s4d-s4g; fresh source snapshot in /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/stentor-km-agent-slabodnick2014.source | supports | Beta-tubulin RNAi reduces transcript and causes disoriented, broken/discontinuous cortical rows in S. coeruleus. The assay is broad tubulin depletion, not a selective Km-fiber intervention. Figure2 calls cortical staining anti-alpha-tubulin while Methods identify anti-acetylated-tubulin clone6-11B-1. Mob1 diffusely labels cortical rows; this does not identify it as a purified Km constituent. Unrelated later Mob1 morphogenesis experiments and supplements were not independently audited. |
| plaque-perialgal-prep-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005622,GO:0030863; Both term definitions and active flags; freshly retrieved exact source bytes at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/perialgal-prep-go.source | supports | Both terms are active: GO0005622 is intracellular anatomical structure and GO0030863 is the cortical cytoskeleton beneath the plasma membrane. They provide a broad parent and encompassing framework, respectively. |
| plaque-perialgal-prep-tax-2721102 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2721102; taxId, scientificName, rank and lineage; freshly retrieved exact source bytes at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/perialgal-prep-tax-2721102.source | supports | Taxon2721102 is Stentor pyriformis at species rank, in Stentoridae/Heterotrichida. |
| plaque-perialgal-prep-go-search | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=perialgal; numberOfHits, results and pageInfo; freshly retrieved exact source bytes at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/perialgal-prep-go-search.source | context_only | The current exact perialgal query returns zero hits. This is a bounded query result, not an exhaustive absence claim across ontology resources. |
| plaque-perialgal-prep-boudreau2025-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1091/mbc.E24-12-0571; Single DOI result bibliographic identity; freshly retrieved exact source bytes at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/perialgal-prep-boudreau2025-meta.source | supports | The exact DOI resolves to Boudreau et al.2025, PMID39937680/PMC12005096, on S.pyriformis cell biology and genome. |
| plaque-perialgal-prep-boudreau2025-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC12005096.1/PMC12005096.1.xml; JATS Cell anatomy, Host/symbiont phylogeny, Microtubule baskets Results; surface-association Discussion; culture, microscopy, expansion, algal-isolation and phylogeny Methods; F3 legend and permissions; fresh source snapshot in /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/perialgal-prep-boudreau2025-jats.source | supports | Primary text and anti-beta-tubulin T0198 Methods support an irregular host cortical mesh around algal vacuoles in S. pyriformis, distinct from longitudinal Km fibers. The algae can be cultured outside the host. Surface retention and physiological benefits remain proposed; centrifugation is not selective mesh disruption. Copyright explicitly grants CC BY4.0, while the licence element is a trademark notice. The Results reference to Figure3C is an internal source typo; native figure/legend show A/B and the record correctly uses B. |
| plaque-perialgal-prep-figure3 | https://pmc-oa-opendata.s3.amazonaws.com/PMC12005096.1/mbc-36-ar44-g003.jpg; Entire native Figure3 JPEG visually inspected; MD5 verified against version1 package; fresh source snapshot in /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/perialgal-prep-figure3.source | supports | PanelA shows chlorophyll and beta-tubulin signals; panelB contains six inward optical sections through expanded meshwork. No regular per-alga cage or native dimensions are inferred. Image MD5257bc762a3388119a79e88aed462a9fa matches the native package. |
| plaque-perialgal-prep-paper-pdf | https://pmc-oa-opendata.s3.amazonaws.com/PMC12005096.1/PMC12005096.1.pdf; PDF page6 caption and exact official file MD5; separate native figure visually inspected; fresh source snapshot in /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/perialgal-prep-paper-pdf.source | supports | Page6 is Figure3 with chlorophyll/beta-tubulin panelA and six-section expanded-mesh panelB. PDF MD5f078ec2af01c2da13f957c95b61640d5 matches version1 metadata. Expanded-image distances are not promoted to native measurements. |
| plaque-perialgal-prep-boudreau2025-package | https://pmc-oa-opendata.s3.amazonaws.com/metadata/PMC12005096.1.json; Version, DOI/PMID, is_retracted, licence_code and exact XML/PDF/Figure3 MD5 comparisons; fresh source snapshot in /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/perialgal-prep-boudreau2025-package.source | supports | Version1 metadata is not marked retracted and retains license_code:null. Fresh XML, PDF and Figure3 MD5 values match the package. The explicit JATS CC BY4.0 copyright grant and structured-code incompleteness are preserved; link-only use and hosting guard remain appropriate. |
| plaque-stalk-asai1998-publisher-abstract | https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1550-7408.1998.tb05066.x; Publisher browser-open extraction lines109-111 abstract and lines303-307/346 issue citation; exact serialized tool response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/asai-browser.json | supports | Asai et al.1998 volume45 pp33-39: chemical modification suggests a non-calcium-binding contributor in addition to spasmins; it does not resolve the native scaffold. Main Methods were not available. Initial curl403 and browser timeout were not used as source evidence; a subsequent publisher browser-open returned the abstract. First-online2007 differs from the1998 issue date. |
| plaque-adapter-datasets-current | https://imodulondb.org/api/datasets; Entire native /api/datasets response: all20 returned organism entries and their dataset keys; fresh response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/adapter-datasets-current.source | context_only | No returned organism/dataset key covers Vorticella, Carchesium, Zoothamnium or Stentor. Thus organism-specific iModulonDB gene/module queries are not applicable for these three ciliate records. This is coverage information, not evidence that a protein, localization or phenotype is absent. |
| plaque-record-stalk_spasmoneme | data/structures/cytoskeleton/stalk_spasmoneme.yaml; Entire current maintained YAML at67d0dd66fe04472c58f4ad9c8b860df18a9f5f8a; identity, components, taxa, evidence, graph, discussions and image metadata | context_only | Read-only current-input assessment; stale original input differs only in three added causal-edge descriptions plus a curation event; descriptions independently reassessed against actual primary text. |
| plaque-record-stentor_km_fiber | data/structures/cytoskeleton/stentor_km_fiber.yaml; Entire current maintained YAML at67d0dd66fe04472c58f4ad9c8b860df18a9f5f8a; identity, components, taxa, evidence, graph, discussions and image metadata | context_only | Read-only current-input assessment; maintained target bytes match the original frozen review input. No scientific fields or status changed. |
| plaque-record-stentor_perialgal_microtubule_meshwork | data/structures/cytoskeleton/stentor_perialgal_microtubule_meshwork.yaml; Entire current maintained YAML at67d0dd66fe04472c58f4ad9c8b860df18a9f5f8a; identity, components, taxa, evidence, graph, discussions and image metadata | context_only | Read-only current-input assessment; maintained target bytes match the original frozen review input. No scientific fields or status changed. |
| plaque-original-bundles-native-validation | scripts/record_review.py validate / render --content; git show historical source inputs; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/original-validation.json; three assigned originals only | supports | All three original bundles validate with exit0, render exact Markdown bytes and have all declared historical frozen input SHA256 values matching their source commit. These successful historical checks do not attest current content for the stale spasmoneme record. |
| micro-current-stellate-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0043232,GO:0035869,GO:0097539,GO:0120269; Four active terms: GO:0043232,0035869,0097539,0120269; definitions, names and status | supports | Broad intracellular membraneless parent and enclosing ciliary transition zone are distinct from external transition fibers and the trypanosome centrin arm. Native ontology does not itself contain the local record edge. |
| micro-current-stellate-agent-go-stellate-search | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=stellate&amp;limit=100; All24 returned names/definitions; page1/1, resultsPerPage100 | partial | No exact Chlamydomonas luminal-fiber identity appeared among the24 literal-query results; these concern stellate cells and related processes. This is not universal ontology absence. |
| micro-current-stellate-agent-tax-3055 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3055; ENA taxId/scientificName/rank/otherNames | supports | 3055 is Chlamydomonas reinhardtii; the species-level authority does not identify assay isolate416 or a culture-collection accession. |
| micro-current-stellate-agent-P05434 | https://rest.uniprot.org/uniprotkb/P05434.json; UniProt entryType, recommended/alternative names, organism, genes absence and EMBL cross-references | supports | Reviewed P05434 is Caltractin/Centrin, taxon3055, without a primary gene symbol. X12634/CAA31163.1 and X57973/CAA41039.1 establish sequence-source links. Identity alone does not confer fiber-specific localization. |
| micro-current-stellate-agent-IPR050145 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050145/; Native InterPro metadata.name/type and description including LLM flags | context_only | Centrin/CML-like includes caltractin, obelin and plant CML proteins; it is broader than stellate-fiber centrins. The description is flagged LLM-generated/checked by the authority; used only for authority family scope, not primary localization evidence. |
| micro-current-stellate-agent-IPR050230 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050230/; Native InterPro metadata.name/type and description including LLM flags | context_only | Calmodulin/Myosin light chain/Troponin C-like spans several distinct calcium-binding protein classes and is broader still. The description is flagged LLM-generated/checked by the authority; used only for authority family scope, not primary localization evidence. |
| micro-current-stellate-agent-sanders1994-pdf | https://pmc-oa-opendata.s3.amazonaws.com/PMC2119956.1/PMC2119956.1.pdf; Printed pp795–797 introduction/Methods and contraction Results; antibody/mutant Results and Discussion pp800–803; Figure2 PDFpage3 and TableI PDFpage6 visually inspected | supports | Detergent-extracted137c and vfl2 isolate416 experiments support calcium-triggered fiber condensation and inward doublet displacement. TableI retains residual excision after EDTA, anti-centrin antibodies and vfl2 perturbation. The authors propose shear/assay conditions to explain earlier disagreement; that interpretation does not resolve universal necessity. Figure2 panelsA–C versusD–F and0.2µm scale agree with the record; separate DIC Figure1 shares the page. |
| micro-current-stellate-agent-sanders1994-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC2119956.1/PMC2119956.1.xml; Article identifiers and permissions/license_ref | supports | Native PMC2119956.1 JATS supplies the article identity and CC BY-NC-SA4.0 licence. Its abstract/reference-format content does not replace the separately read primary PDF. |
| micro-current-stellate-agent-taillon1992-pdf | https://pmc-oa-opendata.s3.amazonaws.com/PMC2289752.1/PMC2289752.1.pdf; Abstract; pCaBP4/sequence-source and strain Methods pp1614–1615; mutation/revertant Results; class2 passages; TableII text and Discussion pp1622–1623 | supports | vfl2 centrin E101K and intragenic revertants link the protein to multiple centrin assemblies. Class2 Met/Ile revertants retain stellate fibers while distal striated fibers differ. vfl2-220 in this paper is not conflated with the separate1994 isolate416. The pCaBP4/sequence bridge supports protein identity; no selective stellate ablation, complete inventory or universal essentiality is demonstrated. |
| micro-current-jarvik1991-abstract | https://www.researchgate.net/publication/258112144_The_role_of_the_flagellar_transition_region_inferences_from_the_analysis_of_a_Chlamydomonas_mutant_with_defective_transition_region_structures; ResearchGate publisher preview primary abstract lines26–29 and summary47–107; browser artifact only | partial | The primary abstract reports effective vfl2 autotomy without organized stellate fibers or detectable axoneme narrowing; proposed central-pair exclusion concerns the broader transition-region structures. This supports retaining the conflict, not a fiber-only gating mechanism. Direct publisher access failed; no complete article body, Methods or figures were freshly read. |
| micro-current-stellate-agent-jarvik1991-browser | https://journals.biologists.com/jcs/article/99/4/731/60763/The-role-of-the-flagellar-transition-region; Native publisher retrieval HTTP403 challenge/error body | context_only | Direct publisher source was inaccessible in this request. A separate browser request timed out; readable primary abstract was obtained through publisher preview on ResearchGate. This response is not scientific full text. |
| micro-current-stellate-agent-lohret1998-html | https://pmc.ncbi.nlm.nih.gov/articles/PMC25341/?report=xml; PMC25341 actual HTML; abstract, Introduction paras17–18, purified-katanin/antibody Methods paras27–31 and relevant Results/Discussion | supports | Purified sea-urchin katanin and anti-human-p60 perturbations concern Chlamydomonas axonemes/whole flagellar-basal-body complexes. The centrin-necessity counterclaim partly cites explicitly unpublished observations. The work does not assign katanin, FA1 or FA2 to an isolated stellate-fiber inventory. |
| micro-current-stellate-agent-diener2015-html | https://pmc.ncbi.nlm.nih.gov/articles/PMC4318714/?report=xml; PMC4318714 actual HTML; isolation/ultrastructure paragraphs18,21–26 and proteomics paragraphs28,31–32 | supports | Isolated resorption-derived transition-zone material retains central cylinders after stellate fibers become unidentifiable. Whole-zone proteomics, centrin enrichment and severing proteins are not evidence that all identified proteins are constituents of intact stellate fibers. |
| micro-current-stellate-agent-hoek2022-pdf | https://push-zb.helmholtz-munich.de/deliver.php?id=34775; Institutional Science PDF page1 architecture Results and page2 Figure1 caption | supports | Native cryo-ET resolves a six-start stellate helix,49.2nm pitch and A3 attachment with about8.1nm repeat, distinct from Y-links and the distal sleeve. Architecture supports the attachment edge, not an exact molecular inventory or a resolved excision mechanism. Figure pixels, IFT-focused remainder and supplements were not inspected. |
| micro-current-spool-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005622,GO:0015630; GO:0005622 and GO:0015630 full active term definitions | supports | Broad intracellular anatomical parent and microtubule-cytoskeleton parthood are appropriate for a local spool identity, without asserting an exact spool GO term. |
| micro-current-spool-agent-go-spool-search | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=spool&amp;limit=100; Entire zero-hit response; resultsPerPage100,total0 | partial | Literal spool query returns no GO hits; local identity remains justified by primary morphology, not universal absence. |
| micro-current-spool-agent-tax-241424 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/241424; ENA taxId/scientificName/rank/lineage | supports | 241424 denotes Takayama helix in Kareniaceae; this verifies identity, not prevalence. |
| micro-current-spool-agent-IPR000217 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000217/; InterPro accession, family type/name, description and subtype context | supports | IPR000217 is the generic Tubulin family. It suits the broad component while neither identifying exact Takayama genes nor asserting every family subtype occurs in the spool. |
| micro-current-spool-agent-mikus2025-paper-pdf | https://www.roscoff-culture-collection.org/sites/default/files/rcc-papers/Mikus%20et%20al.%20-%202025%20-%20Charting%20the%20landscape%20of%20cytoskeletal%20diversity%20in%20microbial%20eukaryotes.pdf; Institutional article-in-press PDF reused from actual2026-11-03T03:20:54.167915Z fetch, newly read for Figure2 caption/Results pp4–5; Kareniaceae survey pp9–11; key-resource species entries; fixation/U-ExM/microscopy/Image analysis Methods e6–e8; CC BY statement | supports | Fixed-cell expansion immunofluorescence supports perinuclear/posterior tubulin-positive spools in Takayama and the sampled Kareniaceae. Apparent extension from a microtubule, desmose association and proposed physiological roles have distinct support levels. Figure2 scale statements conflict with Image analysis Methods; the record properly avoids deriving native dimensions. This new reading uses retained earlier bytes/time, not a fresh PDF download. |
| micro-current-spool-agent-table-s1 | https://www.dudinlab.com/s/Table-S1.xlsx; Workbook sheet relationships resolved natively; List of Species header/row46; Dataset Annotation header row3 and rows1375,1376,1384 | supports | RCC10719 is Takayama helix. Row1384 directly identifies P22-120, the exact s00 volume, E7Ab, interphase, one species in the gel and Spools=Yes. Rows1375–1376 are mixed-gel specimens and do not make RCC3511 a synonym or establish that other species has spools. Annotations are not independent cell-count/prevalence estimates. |
| micro-current-spool-agent-mikus2025-crossref | https://api.crossref.org/works/10.1016/j.cell.2025.09.027; message.DOI/title and complete licence array, content-version=vor | supports | Version-of-record licence is CC BY4.0, distinct from the text/data-mining agreements. It agrees with the article’s explicit CC BY statement. |
| micro-current-spool-agent-project | https://raw.githubusercontent.com/Dey-Lab-Team/culture-collections/2dc2f3dbae8fefe60cea3a2499a1a5f50fe4c98d/data/project.json; Complete pinned data/project.json at2dc2f3dbae8fefe60cea3a2499a1a5f50fe4c98d | supports | The project uses datasets=[volumes], defaultDataset=volumes, specVersion0.3.0. |
| micro-current-spool-agent-volumes-dataset | https://raw.githubusercontent.com/Dey-Lab-Team/culture-collections/2dc2f3dbae8fefe60cea3a2499a1a5f50fe4c98d/data/volumes/dataset.json; Top-level keys and exact rcc10719_pfa_dna-tub-nhs_20230802_od_s00 view plus ch0/ch1/ch2 sources | supports | The exact annotated volume has DNA/tubulin/NHS channels and belongs to spools. Legacy single_volumes substrings inside storage URLs do not override the project default. Other archive sources and raw volumes were not reanalyzed. |
| micro-current-spool-agent-categories | https://raw.githubusercontent.com/Dey-Lab-Team/culture-collections/2dc2f3dbae8fefe60cea3a2499a1a5f50fe4c98d/culture_collections/notebooks/categories.csv; Tab-delimited header; exact s00 row; RCC10719-containing rows and annotation value classes among1767 parsed rows | supports | Pinned annotation confirms the exact volume’s interphase/Yes/NE fields and Yes/No/Maybe/blank spool labels across RCC10719 samples. Those labels do not establish universal occurrence or independent biological replication. |
| micro-current-spool-agent-github-readme | https://raw.githubusercontent.com/Dey-Lab-Team/culture-collections/2dc2f3dbae8fefe60cea3a2499a1a5f50fe4c98d/README.md; Pinned README archive/access paragraph | context_only | The project links BioImage Archive S-BIAD2095. This verifies provenance only; raw volumes were not reanalyzed. |
| micro-current-spool-agent-publisher-figure2 | https://ars.els-cdn.com/content/image/1-s2.0-S0092867425011274-gr2_lrg.jpg; Fresh complete publisher Figure2 JPEG; compared with frozen tracked file and visually inspected all panels | supports | Publisher bytes and frozen tracked image are identical SHA256e979bacf2fad45501744aa5dbc2fd75c0fc2ab2b5e6a6be32be77aad0b1f9046. PanelsD–E show Takayama spools;D tubulin magenta/DNA blue;E closeups and diameter summaries. Other panels are other structures/taxa, not additional spool specimens. Caption preserves scale ambiguity. |
| micro-current-crossbridge-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097595,GO:0097594,GO:0097597; Active GO:0097595,0097594,0097597 definitions/synonyms; ventral-disc children relations | supports | Exact crossbridge and dorsal-microribbon identities and part_of relations are supported. The microribbon size/tubulin-exclusion definition is authority-backed, not a new biochemical measurement. Broader ventral-disc contractile-protein assertions are not imported into these targets. |
| micro-current-crossbridge-agent-tax-5741 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5741; ENA taxId/scientificName/rank/otherNames | supports | Giardia duodenalis species5741 explicitly includes G.intestinalis and G.lamblia synonyms; the target labels remain valid. |
| micro-current-crossbridge-agent-epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1371/journal.pone.0043783%22; Exact DOI result for10.1371/journal.pone.0043783 | supports | Resolves Schwartz, Heumann, Dawson and Hoenger2012, PMID22984443/PMC3439489. Citation identity only. |
| micro-current-crossbridge-agent-schwartz2012-jats | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3439489/fullTextXML; Fresh native JATS Results s2b/s2h; Discussion s3d/s3e; Methods s5a/s5d/s5e/s5f; associated main-text captions | supports | Primary tomography supports trilaminar dorsal microribbons with lateral crossbridges, distinct from the within-complex B bridge. WBC6 trophozoites and extracted flattened cytoskeletons, with five selected tomograms/four discs, bound interpretation. Crossbridge flexibility does not directly demonstrate active contraction or identify constituent proteins. Named giardin/SALP composition in Discussion is attributed earlier evidence, separately checked in Hagen2011. |
| micro-current-microribbon-agent-go-mt | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097593; GO:0097593 active definition and synonyms | supports | The spiral ventral-disc microtubule array supports near-perpendicular dorsal microribbons and is distinct from the microribbons themselves. |
| micro-current-microribbon-agent-tax-184922 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/184922; ENA taxon184922 scientificName/rank/synonyms | supports | ATCC50803 is a strain-level taxon. WBC6 identity is supplied by the primary Methods and native protein names, not inferred from the species taxon alone. |
| micro-current-microribbon-agent-epmc-hagen2011 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1371/journal.pntd.0001442%22; Exact DOI10.1371/journal.pntd.0001442 result | supports | Resolves Hagen2011 primary ventral-disc localization study, PMID22206034/PMC3243723. |
| micro-current-microribbon-agent-hagen2011-jats | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3243723/fullTextXML; Fresh native JATS Methods s2a/s2d/s2g; Results s3b; Discussion s4a; Table1 rowsGL50803_4812/86676/4410 | supports | Primary GFP and anti-GFP immunogold/negative-stain observations support beta-/delta-giardin and SALP-1 microribbon association. Structural sufficiency, timing, sheet-specific arrangement and universal turnover remain interpretations or unresolved. Table1 assigns PF06705 to beta/delta while SALP-1 has no domain entry; no negative homology inference follows. |
| micro-current-microribbon-agent-ipr-008374 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR008374/; Native metadata accession/name/type/description/integrated field | context_only | IPR008374 is the SF-assemblin/beta-giardin family; supports candidate mappings for beta/delta but the full named cohort needs scope reconciliation. |
| micro-current-microribbon-agent-ipr-038835 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR038835/; Native metadata accession/name/type/description/integrated field | context_only | IPR038835 is the Giardin subunit beta-like family; this does not automatically identify SALP-1 or every microribbon constituent. |
| micro-current-microribbon-agent-pfam-06705 | https://www.ebi.ac.uk/interpro/api/entry/pfam/PF06705/; Native metadata accession/name/type/description/integrated field | context_only | PF06705 is SF-assemblin/beta giardin integrated into IPR008374; its green-algal mitotic descriptions are not Giardia-specific evidence. |
| micro-current-microribbon-agent-uniprot-loci | https://rest.uniprot.org/uniprotkb/search?query=taxonomy_id%3A5741%20AND%20%28gene%3AGL50803_004812%20OR%20gene%3AGL50803_4812%20OR%20gene%3AGL50803_086676%20OR%20gene%3AGL50803_86676%20OR%20gene%3AGL50803_004410%20OR%20gene%3AGL50803_4410%29&amp;format=json&amp;size=100; Two returned reviewed-status/name/taxon/gene/cross-reference objects; X-Total-Results2; no continuation | context_only | Unreviewed E2RTU7 beta-giardin and E2RUA1 SALP-1 have WBC6 taxon184922 and expected locus aliases. Beta carries IPR008374/IPR038835/PF06705; the returned SALP-1 entry has none of those cross-references. That annotation gap does not disprove literature homology or establish universal family absence. |
| micro-current-microribbon-agent-uniprot-delta | https://rest.uniprot.org/uniprotkb/search?query=taxonomy_id%3A5741%20AND%20protein_name%3A%22Delta-giardin%22&amp;format=json&amp;size=100; Entire one-result response and family cross-references; X-Total-Results1; no continuation | context_only | Unreviewed A0A644FAT1 identifies WBC6 delta-giardin, locusGL50803_0086676, with IPR008374/PF06705 annotations. Native annotation supports identity/family candidates, not direct localization. |
| micro-current-current-adapter-catalogue | https://imodulondb.org/api/datasets; All20 organism entries/28 dataset names, cached raw catalogue independently reread | context_only | No catalogue organism/dataset matches Chlamydomonas, Takayama or Giardia. Named proteins justify applicability discovery for stellate, spool and microribbon; no target-specific search is available. Crossbridge has no named molecular target. This is dataset coverage, never biological negative evidence. |
| micro-record-stellate | data/structures/cytoskeleton/transition_zone_stellate_fiber_system.yaml; Complete target YAML | supports | Current bytes match the original frozen SHA256 ee5fc36bcda7810c550cfef29146f6b124f79703e6b73832b6f005583884ba36. No stale target or record edit. |
| micro-prior-stellate | reviews/structured/20261021T084040Z-transition-zone-stellate-fiber-system-audit/review.yaml; Original frozen inputs/checks/evidence/assessments/findings/verdict/limits | supports | Original pass_with_limitations has no scientific findings. Native validation/render and frozen-target comparison pass; old global receipts remain historical. |
| micro-record-spool | data/structures/cytoskeleton/tubulin_spool.yaml; Complete target YAML | supports | Current bytes match the original frozen SHA256 1180c5c0b3a5c67f58a23b99913f7b78202beb8cf3e01c40ca5aac9c56dcf072. No stale target or record edit. |
| micro-prior-spool | reviews/structured/20261021T084041Z-tubulin-spool-audit/review.yaml; Original frozen inputs/checks/evidence/assessments/findings/verdict/limits | supports | Original pass_with_limitations has no scientific findings. Native validation/render and frozen-target comparison pass; old global receipts remain historical. |
| micro-record-crossbridge | data/structures/cytoskeleton/ventral_disc_crossbridge.yaml; Complete target YAML | supports | Current bytes match the original frozen SHA256 bb35ddad7c8b15916d19fa6e5ad334ca3476221330372020fdf4adc8565db67b. No stale target or record edit. |
| micro-prior-crossbridge | reviews/structured/20261021T084041Z-ventral-disc-crossbridge-audit/review.yaml; Original frozen inputs/checks/evidence/assessments/findings/verdict/limits | supports | Original pass_with_limitations has no scientific findings. Native validation/render and frozen-target comparison pass; old global receipts remain historical. |
| micro-record-microribbon | data/structures/cytoskeleton/ventral_disc_dorsal_microribbon.yaml; Complete target YAML | supports | Current bytes match the original frozen SHA256 6bcdbfaaf84c4b6152147340dcbb6f5958d6dc6aca2288e034c3f2c357819425. No stale target or record edit. |
| micro-prior-microribbon | reviews/structured/20261021T084041Z-ventral-disc-dorsal-microribbon-audit/review.yaml; Original frozen inputs/checks/evidence/assessments/findings/verdict/limits | supports | Original pass_with_limitations has no scientific findings. Native validation/render and frozen-target comparison pass; old global receipts remain historical. |
| micro-original-native-checks | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-microtubule/original-checks.json; Four native validate/render commands and frozen-target comparison | supports | All4 validate with exit0 and render Markdown byte-exactly; all4 target hashes match. This is not a fresh whole-corpus QC claim. |
| micro-tracked-spool-image | data/images/cytoskeleton/tubulin_spool/mikus_2025_figure2.jpg; Complete frozen tracked Figure2 image; visually inspected after parent added to input manifest | supports | Frozen tracked image matches declared/publisher SHA256 and panel-specific caption. Image was explicitly frozen before this assessment. |
| micro-adapter-policy | .claude/skills/review-yaml-record/SKILL.md; structured-source-cross-checks block | supports | Named genes/proteins/accessions trigger consideration; runner/coverage checks precede module queries. Lack of an expression-module mechanism is not the stated exemption; absence of matching covered organisms supports downstream non-applicability. |
| septin-s2349-split-rings-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032176,GO:0032156,GO:0005856,GO:0032177,GO:0032153,GO:0005940,GO:0032173; Exact seven-term QuickGO responses: names, definitions, synonyms, parent children relations and referenced PMIDs. | supports | Authority supports paired split rings, parent and parthood distinctions, and cautiously phrased cytokinesis compartment function. |
| septin-s2349-split-rings-agent-family | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016491/; Native IPR016491 metadata.type, metadata.name, description and hierarchy. | supports | IPR016491 is the generic Septin family, matching the existing generic component independently of unresolved localized paralogue composition. |
| septin-s2349-split-rings-agent-douglas-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC1214204/; PMC1214204 secondary review: introductory budding cycle, ring-splitting and boundary-domain paragraphs; not a newly inspected primary experiment. | supports | Secondary review summarizes collar splitting and cytokinesis confinement; the record retains the cautious thought-to-trap claim. Native schema has no secondary_source evidence kind, so authority here identifies inspected secondary literature, not primary evidence. |
| septin-s2349-split-rings-agent-versele-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC1761124/?pdf=render; PMC1761124 secondary review: septin functions, collar scission and Figure 3 discussion. | supports | Secondary review supports bounded split-ring morphology and compartmentalization wording; no source-wide primary experiment audit claimed. authority kind denotes inspected secondary literature, not primary evidence. |
| septin-s2349-split-rings-agent-douglas-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1128/EC.4.9.1503-1512.2005&amp;format=json&amp;resultType=core; Complete returned result list for the exact URL query. | supports | Exact bounded identity/disambiguation lookup; results do not establish exhaustive absence from literature or biology. |
| septin-s2349-tacc-prep-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0007020,GO:0051315,GO:0061863,GO:0070850,GO:0090307,GO:0140535; Native issuing-authority response, exact accession/term or taxon and returned name/type/status. | supports | Checked native identity, label, taxon, accession crossreferences and the bounded family/domain scope relevant to the current record. |
| septin-s2349-tacc-prep-tax-4896 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4896; Native issuing-authority response, exact accession/term or taxon and returned name/type/status. | supports | Checked native identity, label, taxon, accession crossreferences and the bounded family/domain scope relevant to the current record. |
| septin-s2349-tacc-prep-tax-284812 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/284812; Native issuing-authority response, exact accession/term or taxon and returned name/type/status. | supports | Checked native identity, label, taxon, accession crossreferences and the bounded family/domain scope relevant to the current record. |
| septin-s2349-tacc-prep-IPR045110 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR045110/; Native issuing-authority response, exact accession/term or taxon and returned name/type/status. | supports | Checked native identity, label, taxon, accession crossreferences and the bounded family/domain scope relevant to the current record. |
| septin-s2349-tacc-prep-IPR024312 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR024312/; Native issuing-authority response, exact accession/term or taxon and returned name/type/status. | supports | Checked native identity, label, taxon, accession crossreferences and the bounded family/domain scope relevant to the current record. |
| septin-s2349-tacc-prep-matches-Q9URY2 | https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/Q9URY2/; Native issuing-authority response, exact accession/term or taxon and returned name/type/status. | supports | Checked native identity, label, taxon, accession crossreferences and the bounded family/domain scope relevant to the current record. |
| septin-s2349-tacc-prep-Q9URY2 | https://rest.uniprot.org/uniprotkb/Q9URY2.json; Native issuing-authority response, exact accession/term or taxon and returned name/type/status. | supports | Checked native identity, label, taxon, accession crossreferences and the bounded family/domain scope relevant to the current record. |
| septin-s2349-tacc-prep-O94534 | https://rest.uniprot.org/uniprotkb/O94534.json; Native issuing-authority response, exact accession/term or taxon and returned name/type/status. | supports | Checked native identity, label, taxon, accession crossreferences and the bounded family/domain scope relevant to the current record. |
| septin-s2349-tacc-prep-Q10198 | https://rest.uniprot.org/uniprotkb/Q10198.json; Native issuing-authority response, exact accession/term or taxon and returned name/type/status. | supports | Checked native identity, label, taxon, accession crossreferences and the bounded family/domain scope relevant to the current record. |
| septin-s2349-tacc-prep-query-alp7 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3Aalp7%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29; Complete returned result list for the exact URL query. | supports | Exact bounded identity/disambiguation lookup; results do not establish exhaustive absence from literature or biology. |
| septin-s2349-tacc-prep-query-mia1 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3Amia1%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29; Complete returned result list for the exact URL query. | supports | Exact bounded identity/disambiguation lookup; results do not establish exhaustive absence from literature or biology. |
| septin-s2349-tacc-prep-query-alp14 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3Aalp14%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29; Complete returned result list for the exact URL query. | supports | Exact bounded identity/disambiguation lookup; results do not establish exhaustive absence from literature or biology. |
| septin-s2349-tacc-prep-query-mtc1 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3Amtc1%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29; Complete returned result list for the exact URL query. | supports | Exact bounded identity/disambiguation lookup; results do not establish exhaustive absence from literature or biology. |
| septin-s2349-tacc-prep-hussmann2016-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1038/srep20653; Complete returned result list for the exact URL query. | supports | Exact bounded identity/disambiguation lookup; results do not establish exhaustive absence from literature or biology. |
| septin-s2349-tacc-prep-hussmann2016-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC4749977.1/PMC4749977.1.xml; PMC4749977 Results: in vivo deletions; purified Alp7/Alp14 binding; long MTs; tip-tracking; Figure 7 legend. Methods: tubulin purification and MT dynamics; Discussion occupancy subsection. | supports | Primary experiments show reduced elongation in alp7 deletion under these conditions, co-sedimentation of purified partners, no detectable Alp7-alone tubulin binding, and Alp7-enhanced Alp14 tip occupancy. Figure 7 is mixed-species purified TIRF material, not a whole-cell image or native universal stoichiometry. |
| septin-s2349-tacc-prep-nucleation2018-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.cub.2018.04.008; Complete returned result list for the exact URL query. | supports | Exact bounded identity/disambiguation lookup; results do not establish exhaustive absence from literature or biology. |
| septin-s2349-tacc-prep-nucleation2018-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC7263743.1/PMC7263743.1.xml; PMC7263743 sections S6, S8, S9, S13 and S14, with embedded Figure 6/7 experimental descriptions. | supports | Primary 2018 observations distinguish Alp7-dependent Alp14 MTOC loading/nucleation from retained plus-end tracking and normal elongation. The stated conflict with 2016 is real. Alp14-GBP/Mto1-bonsai rescue is engineered and partial. |
| septin-s2349-tacc-prep-attachment2013-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1091/mbc.E12-11-0817; Complete returned result list for the exact URL query. | supports | Exact bounded identity/disambiguation lookup; results do not establish exhaustive absence from literature or biology. |
| septin-s2349-tacc-prep-attachment2013-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC3623634.1/PMC3623634.1.xml; PMC3623634 Results on Ndc80-NH12/F420S, Alp7/14 localization, GST/coIP and loop peptide arrays, forced Nuf2-Alp7C rescue; corresponding biochemical Methods. | supports | Primary evidence supports reduced rather than abolished kinetochore recruitment, retained SPB context, peptide-defined direct association and forced-targeting rescue. It does not map a complete full-length interface or make Ndc80 a complex constituent. |
| septin-s2349-tacc-prep-transport2014-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1091/mbc.E13-11-0679; Complete returned result list for the exact URL query. | supports | Exact bounded identity/disambiguation lookup; results do not establish exhaustive absence from literature or biology. |
| septin-s2349-tacc-prep-transport2014-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC4072571.1/PMC4072571.1.xml; PMC4072571 Results L615, Alp7 deletion/5A kinase and localization experiments, Cut15 two-hybrid; Discussion CDK transport; kinase and two-hybrid Methods. | supports | L615A preserves Alp7 association while affecting export; Alp7 5A retains delayed import, reduces mitotic accumulation and has NLS-suppressible growth defects. Cut15 fragment interaction in budding-yeast two-hybrid supports a model, not measured native importin affinity or complete spindle rescue. |
| septin-s2349-tacc-prep-dis1_2019-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.3390/ijms20205108; Complete returned result list for the exact URL query. | supports | Exact bounded identity/disambiguation lookup; results do not establish exhaustive absence from literature or biology. |
| septin-s2349-tacc-prep-dis1_2019-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC6834199.1/PMC6834199.1.xml; PMC6834199 Results 2.6, Discussion 3.1, Methods 4.3. | supports | Reciprocal enforced targeting at endogenous expression fails to exchange Alp14 and Dis1 functions, whereas earlier overexpression rescue is explicitly retained. This does not exclude every conditional compensation or make Dis1 a TACC constituent. |
| septin-s2349-tacc-prep-figure7 | https://pmc-oa-opendata.s3.amazonaws.com/PMC4749977.1/srep20653-f7.jpg; Native source JPEG visually inspected via identical frozen local image; all panels A–D; bytes match the repository image exactly. | supports | Mixed S. pombe/brain-tubulin TIRF schematic, kymographs and growth histograms; 2 µm and 1 minute scales; CC BY 4.0 checked in primary JATS. |
| septin-s2349-telo-prep-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000930,GO:0000931,GO:0005815,GO:0008275,GO:0034993,GO:0045141,GO:0051418; Native issuing-authority response, exact accession/term or taxon and returned name/type/status. | supports | Checked native identity, label, taxon, accession crossreferences and the bounded family/domain scope relevant to the current record. |
| septin-s2349-telo-prep-IPR045119 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR045119/; Native issuing-authority response, exact accession/term or taxon and returned name/type/status. | supports | Checked native identity, label, taxon, accession crossreferences and the bounded family/domain scope relevant to the current record. |
| septin-s2349-telo-prep-IPR005334 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005334/; Native issuing-authority response, exact accession/term or taxon and returned name/type/status. | supports | Checked native identity, label, taxon, accession crossreferences and the bounded family/domain scope relevant to the current record. |
| septin-s2349-telo-prep-IPR030268 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR030268/; Native issuing-authority response, exact accession/term or taxon and returned name/type/status. | supports | Checked native identity, label, taxon, accession crossreferences and the bounded family/domain scope relevant to the current record. |
| septin-s2349-telo-prep-IPR026983 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR026983/; Native issuing-authority response, exact accession/term or taxon and returned name/type/status. | supports | Checked native identity, label, taxon, accession crossreferences and the bounded family/domain scope relevant to the current record. |
| septin-s2349-telo-prep-matches-P87245 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P87245/; Native issuing-authority response, exact accession/term or taxon and returned name/type/status. | supports | Checked native identity, label, taxon, accession crossreferences and the bounded family/domain scope relevant to the current record. |
| septin-s2349-telo-prep-matches-O43087 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/O43087/; Native issuing-authority response, exact accession/term or taxon and returned name/type/status. | supports | Checked native identity, label, taxon, accession crossreferences and the bounded family/domain scope relevant to the current record. |
| septin-s2349-telo-prep-matches-O94488 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/O94488/; Native issuing-authority response, exact accession/term or taxon and returned name/type/status. | supports | Checked native identity, label, taxon, accession crossreferences and the bounded family/domain scope relevant to the current record. |
| septin-s2349-telo-prep-matches-O13290 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/O13290/; Native issuing-authority response, exact accession/term or taxon and returned name/type/status. | supports | Checked native identity, label, taxon, accession crossreferences and the bounded family/domain scope relevant to the current record. |
| septin-s2349-telo-prep-matches-O42667 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/O42667/; Native issuing-authority response, exact accession/term or taxon and returned name/type/status. | supports | Checked native identity, label, taxon, accession crossreferences and the bounded family/domain scope relevant to the current record. |
| septin-s2349-telo-prep-Q09825 | https://rest.uniprot.org/uniprotkb/Q09825.json; Native issuing-authority response, exact accession/term or taxon and returned name/type/status. | supports | Checked native identity, label, taxon, accession crossreferences and the bounded family/domain scope relevant to the current record. |
| septin-s2349-telo-prep-P87245 | https://rest.uniprot.org/uniprotkb/P87245.json; Native issuing-authority response, exact accession/term or taxon and returned name/type/status. | supports | Checked native identity, label, taxon, accession crossreferences and the bounded family/domain scope relevant to the current record. |
| septin-s2349-telo-prep-O43087 | https://rest.uniprot.org/uniprotkb/O43087.json; Native issuing-authority response, exact accession/term or taxon and returned name/type/status. | supports | Checked native identity, label, taxon, accession crossreferences and the bounded family/domain scope relevant to the current record. |
| septin-s2349-telo-prep-O94488 | https://rest.uniprot.org/uniprotkb/O94488.json; Native issuing-authority response, exact accession/term or taxon and returned name/type/status. | supports | Checked native identity, label, taxon, accession crossreferences and the bounded family/domain scope relevant to the current record. |
| septin-s2349-telo-prep-Q9Y705 | https://rest.uniprot.org/uniprotkb/Q9Y705.json; Native issuing-authority response, exact accession/term or taxon and returned name/type/status. | supports | Checked native identity, label, taxon, accession crossreferences and the bounded family/domain scope relevant to the current record. |
| septin-s2349-telo-prep-Q9UTS6 | https://rest.uniprot.org/uniprotkb/Q9UTS6.json; Native issuing-authority response, exact accession/term or taxon and returned name/type/status. | supports | Checked native identity, label, taxon, accession crossreferences and the bounded family/domain scope relevant to the current record. |
| septin-s2349-telo-prep-O13290 | https://rest.uniprot.org/uniprotkb/O13290.json; Native issuing-authority response, exact accession/term or taxon and returned name/type/status. | supports | Checked native identity, label, taxon, accession crossreferences and the bounded family/domain scope relevant to the current record. |
| septin-s2349-telo-prep-O42667 | https://rest.uniprot.org/uniprotkb/O42667.json; Native issuing-authority response, exact accession/term or taxon and returned name/type/status. | supports | Checked native identity, label, taxon, accession crossreferences and the bounded family/domain scope relevant to the current record. |
| septin-s2349-telo-prep-query-mto1 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3Amto1%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29; Complete returned result list for the exact URL query. | supports | Exact bounded identity/disambiguation lookup; results do not establish exhaustive absence from literature or biology. |
| septin-s2349-telo-prep-query-ssm4 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3Assm4%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29; Complete returned result list for the exact URL query. | supports | Exact bounded identity/disambiguation lookup; results do not establish exhaustive absence from literature or biology. |
| septin-s2349-telo-prep-yoshida2013-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1083/jcb.201207168; Complete returned result list for the exact URL query. | supports | Exact bounded identity/disambiguation lookup; results do not establish exhaustive absence from literature or biology. |
| septin-s2349-telo-prep-jimenez2025-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1038/s41467-025-56049-9; Complete returned result list for the exact URL query. | supports | Exact bounded identity/disambiguation lookup; results do not establish exhaustive absence from literature or biology. |
| septin-s2349-telo-prep-yoshida2013-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC3575533.1/PMC3575533.1.xml; PMC3575533 main Results and figure legends 1–5, Discussion motor model, meiosis induction and microscopy Methods; Figure 5 Dlc1/Dhc1 paragraph and caption explicitly inspected. | supports | Primary imaging and perturbation support an SPB-distinct, telomere-associated meiotic MTOC. Kms1/Mto1 and Dlc1 support Alp4 recruitment; Dhc1 is dispensable narrowly for that recruitment, not efficient clustering. Figure 5C is a proposed motor model. Gamma-TuC is a multiprotein structure with Alp4 as reporter, supporting the current STRUCTURE node. |
| septin-s2349-telo-agent-yoshida2013-supp | https://pmc-oa-opendata.s3.amazonaws.com/PMC3575533.1/supp_jcb.201207168_JCB_201207168_sm.pdf; Native PDF text: Figures S1–S3 captions, six video legends and Table S1 relevant Figure 2 strains. PDF served as text/html but identified by %PDF magic; figures S2 pixels and videos not independently viewed. | supports | Captions support cytoplasmic regrowth, preconjugation Sad1 sites, independent Dlc1/Dhc1 localization and the multiple engineered experimental stocks; no identification of all experiments with the UniProt reference strain. |
| septin-s2349-telo-prep-jimenez2025-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC11747273.1/PMC11747273.1.xml; PMC11747273 sections Sec8, Sec9, Sec12, Sec14 and Sec17, Figure 6 caption; Sec10 context also inspected. | supports | Ectopic Bqt1/Bqt2 in Rabl-deficient haploid mitotic cells recruits Sad1/Kms1/Mto1/Alp4, without detected Dhc1 or complete bouquet. Kms1 deletion suppresses some growth/migration phenotypes. This is engineered partial assembly, not a normal constitutive mitotic telocentrosome. |
| septin-s2349-telo-agent-jimenez2025-supp | https://pmc-oa-opendata.s3.amazonaws.com/PMC11747273.1/41467_2025_56049_MOESM1_ESM.pdf; Native supplemental PDF text: Supplementary Figure 6 legend only, Rap1 localization and abundance context. | supports | Supplemental legend reports Rap1 localization/intensity assays and total-protein western blot replicates. This is caption-level supplementary coverage, not a complete supplement or underlying-image audit. |
| septin-s2349-telo-prep-figure2 | https://pmc-oa-opendata.s3.amazonaws.com/PMC3575533.1/JCB_201207168_Fig2.jpg; Native source JPEG visually inspected, panels A–E and 2 µm scale bars. | supports | Time-course fluorescence, haploid-meiosis schematic and DMSO/MBC plots correspond to record description; native SHA256 matches record link-only image, CC BY-NC-SA 3.0 checked in primary JATS. |
| septin-s2349-current-adapter-catalogue | https://imodulondb.org/api/datasets; Official iModulonDB API /api/datasets complete response, all 20 organism entries and 28 dataset keys. | supports | Inspected catalogue covers bacterial/archaeal organisms and no Schizosaccharomyces pombe or other eukaryotic target here. Target gene/module searches therefore do not apply. Catalogue absence is not evidence against biological structures; no new local runner invocation claimed. |
| septin-s2349-record-split_septin_rings | data/structures/cytoskeleton/split_septin_rings.yaml; Complete current YAML at head 67d0dd66fe04472c58f4ad9c8b860df18a9f5f8a. | supports | Whole maintained record inspected read-only, including components, graph edges, evidence, image/provenance, discussions and change history. |
| septin-s2349-record-tacc_tog_complex | data/structures/cytoskeleton/tacc_tog_complex.yaml; Complete current YAML at head 67d0dd66fe04472c58f4ad9c8b860df18a9f5f8a. | supports | Whole maintained record inspected read-only, including components, graph edges, evidence, image/provenance, discussions and change history. |
| septin-s2349-record-telocentrosome | data/structures/cytoskeleton/telocentrosome.yaml; Complete current YAML at head 67d0dd66fe04472c58f4ad9c8b860df18a9f5f8a. | supports | Whole maintained record inspected read-only, including components, graph edges, evidence, image/provenance, discussions and change history. |
| septin-s2349-policy | docs/CURATION.md; Components; scope and grounding requirements. | supports | Ground the existing generic family when an exact native family exists; do not substitute local cohort membership for family identity. |
| check-qc | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/qc.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| check-labels | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/labels.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | 4232 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| check-trait-links | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/trait-links.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Native TraitMech link check passed. |
| check-vendored | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/vendored.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Pinned governed files match; native vendored check passed. |
| check-curies | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/curies.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| focused | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/focused-results.json; All twenty actual target schema/strict command outputs | supports | Ten schema and ten strict commands returned exit zero. |
| supplemental-pmid | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/pmid-chunks-receipt.json; Complete native-report PMID set checked with unchanged resolver in batches of at most fifty | supports | 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers remain unverified. |
| historical-adapter-runner-availability | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical runner invocation receipt, cross-checked against exact stdout/stderr hashes; reread during PR2349 synthesis | context_only | Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS PermissionError reading the configured runner pyvenv.cfg. This is a retained historical availability observation, not a fresh attempt or a scientific validation failure. Native policy permits inspected source-catalogue fallback. |

## Limits And Additional Notes

- Stalk spasmoneme, Stentor Km fiber and perialgal meshwork independent subreview: Stalk spasmoneme: Routledge1978 claim-bearing preparation, extraction, calcium-response and Discussion sections were inspected; rates are preparation/pH dependent, and no universal fast kinetic constant is inferred from the word rapid. Underlying cited experiments were not independently reanalyzed.
- Stalk spasmoneme, Stentor Km fiber and perialgal meshwork independent subreview: Stalk spasmoneme: Konior2009 Methods/Results/Discussion and relevant legends were read, but no raw immunogold recount was performed. Ryu2012 main mechanical experiments and assumptions were read; Supporting Material and raw trajectories were not audited.
- Stalk spasmoneme, Stentor Km fiber and perialgal meshwork independent subreview: Stalk spasmoneme: Asai1998, Maciejewski1999 and Jiang2025 contributions remain abstract-tier. Asai direct curl returned403 and the first browser call timed out; a subsequent publisher browser extraction returned the abstract. The EPMC multi-DOI query omitted Asai, not evidence that the paper does not exist.
- Stalk spasmoneme, Stentor Km fiber and perialgal meshwork independent subreview: Stalk spasmoneme: CIL preview resolution supports qualitative morphology only. Current January23,2012 catalogue metadata differs from the older review's January22 historical observation; current record only claims2012. No raw archive, physiological calcium assay or calibrated dimension was reviewed.
- Stalk spasmoneme, Stentor Km fiber and perialgal meshwork independent subreview: Stentor Km fiber: Primary1973 introduction/Methods, cortical organization/overlap Results, Figure8 and bridge-motor Discussion were inspected. Later unrelated myoneme-contraction discussion and cited underlying studies were not independently audited.
- Stalk spasmoneme, Stentor Km fiber and perialgal meshwork independent subreview: Stentor Km fiber: Slabodnick2014 tubulin and Mob1 localization Results plus relevant Methods were inspected. Remaining Mob1 morphogenesis experiments and supplemental data were not fully audited. Fixed morphology and broad tubulin knockdown do not isolate Km-specific mechanics or identify the native bridge motor.
- Stalk spasmoneme, Stentor Km fiber and perialgal meshwork independent subreview: Stentor perialgal meshwork: Claim-bearing anatomy, phylogeny, meshwork, surface-association and microscopy/culture Methods were read; unrelated genomic, photosynthesis and phototaxis experiments, movies and raw data were not audited. No selective perturbation proves anchoring.
- Stalk spasmoneme, Stentor Km fiber and perialgal meshwork independent subreview: Stentor perialgal meshwork: Source Figure3 Results text mentions nonexistent panelC, but native figure/caption and record correctly use A/B. Structured PMC licence metadata remains incomplete; no hosting guard is changed and no expanded dimension is treated as native.
- Stalk spasmoneme, Stentor Km fiber and perialgal meshwork independent subreview: All three: Historical repository/ontology/taxon absence searches remain historical and were not comprehensively repeated. The fresh exact perialgal query and complete returned iModulonDB catalogue are bounded remote searches; neither implies exhaustive biological or ontology absence.
- Stalk spasmoneme, Stentor Km fiber and perialgal meshwork independent subreview: All three: This independent slice ran only original bundle validation/render/historical hash checks; root owns current corpus QC, focused record validation and final CI. No new adapter CLI run is claimed by this subreview.
- Stellate fiber system, tubulin spool, ventral-disc crossbridge and dorsal microribbon independent subreview: All4 assigned target hashes are unchanged. Native original-review validation/render ran independently; root owns whole-corpus QC, current focused record gates, final CI and merge checks.
- Stellate fiber system, tubulin spool, ventral-disc crossbridge and dorsal microribbon independent subreview: Stellate: Sanders claim-bearing Methods/Results/Discussion and Figure2/TableI were inspected; Taillon sequence/mutant/revertant/TableII text was inspected, but Taillon figure/table pixels and1988 sequence-source bodies were not independently reread. Strain labels and pleiotropic versus fiber-selective effects remain distinct.
- Stellate fiber system, tubulin spool, ventral-disc crossbridge and dorsal microribbon independent subreview: Stellate: direct Jarvik publisher HTTP access returned403 and browser access timed out; exact EuropePMC DOI search returned0 results. The full primary abstract/publisher preview summary was read on ResearchGate, not the full body, figures or Methods. These access limits do not contradict existence or the bounded counterclaim.
- Stellate fiber system, tubulin spool, ventral-disc crossbridge and dorsal microribbon independent subreview: Stellate: Lohret and Diener are limited to specified abstract/introduction/method/claim-bearing text passages. Their microscopy pixels, unlisted supplementary material and raw data were not reanalyzed. Hoek reading is confined to architecture Results and Figure1 caption; IFT remainder/supplements/figure pixels not inspected.
- Stellate fiber system, tubulin spool, ventral-disc crossbridge and dorsal microribbon independent subreview: Tubulin spool: institutionally hosted Mikus article-in-press PDF bytes were reused from the actual03:20:54Z fetch and newly read for the stated claim passages. Fresh workbook/native pinned metadata/publisher image and Crossref licence were inspected. No raw-volume-to-Figure2-panel mapping, raw volumes or videos were analyzed, and no full5479-source archive audit is claimed.
- Stellate fiber system, tubulin spool, ventral-disc crossbridge and dorsal microribbon independent subreview: Tubulin spool: workbook inspection was restricted to specified headers/rows; categories were parsed across1767 rows and RCC10719/exact-volume fields inspected. These annotations are not independent-cell counts, universal prevalence or proof of mixed-gel species identity. Unresolved expansion-scale wording prevents derived native dimensions.
- Stellate fiber system, tubulin spool, ventral-disc crossbridge and dorsal microribbon independent subreview: Crossbridge and microribbon: specified Schwartz architecture/Methods and Hagen localization/Methods/Table1 passages were read. Figure pixels, videos, raw tomography, full supplementary data and FRAP experiments were not independently reanalyzed. Proposed rigidity, contraction and dynamics are not imported as established mechanisms.
- Stellate fiber system, tubulin spool, ventral-disc crossbridge and dorsal microribbon independent subreview: Microribbon: inspected native protein/family records support candidate beta/delta mappings but do not establish exact full-cohort mapping. Missing SALP-1 family cross-references do not refute homology. GO-derived exclusion/size statements remain authority-backed rather than being attributed to tomography as biochemical proof.
- Stellate fiber system, tubulin spool, ventral-disc crossbridge and dorsal microribbon independent subreview: Structured sources: the complete iModulonDB catalogue was reused with its actual03:20:54Z fetch time and reread for these organisms. Runner availability is root-owned evidence. No matching covered target dataset means no downstream module query; it is never a biological-negative result.
- Stellate fiber system, tubulin spool, ventral-disc crossbridge and dorsal microribbon independent subreview: Bounded GO/UniProt searches explicitly retain literal queries, limits and result coverage. Historical ignored-inclusive record creation searches are not asserted as freshly rerun corpus-wide absence proofs.
- Split septin rings, TACC/TOG complex and telocentrosome independent subreview: Split-ring morphology/function corroboration uses current GO and explicitly secondary Douglas/Versele reviews; no new primary diffusion-barrier experiment audit or new paralogue-completeness claim.
- Split septin rings, TACC/TOG complex and telocentrosome independent subreview: TACC and telocentrosome primary full-text bodies were retrieved, but independent inspection is the named Results/Methods/caption scope above, not a claim to have reviewed every paragraph, image, supplement or cited reference. TACC supplementary figures/tables were not fetched independently; 2019 Alp14-NLS details beyond main Methods remain inherited scope.
- Split septin rings, TACC/TOG complex and telocentrosome independent subreview: Yoshida supplemental figures are caption/text scope and video legends only; supplemental pixels and movies were not independently inspected. Jimenez supplemental coverage is Figure6 legend only. The two record-linked main figures were visually inspected.
- Split septin rings, TACC/TOG complex and telocentrosome independent subreview: Two InterPro match requests initially returned HTTP429; bounded subsequent requests both succeeded and their later receipt times/hashes are used. Scratch conversion commands initially referenced response-extension filenames incorrectly and lacked optional image/PDF libraries; these are not repository validation failures. Native three-bundle validation and render each passed.
- Split septin rings, TACC/TOG complex and telocentrosome independent subreview: No new structured adapter runner call or all-corpus QC/CI is claimed by this subreview. Root owns current global checks. No records, bundles, GitHub state or branches were modified.
- Split septin rings, TACC/TOG complex and telocentrosome independent subreview: All external biological evidence cited here was freshly retrieved during this PR; no earlier cached scientific source body is passed off as current access. Broad literature completeness and absence beyond the exact authority/query scopes are not claimed.
- Historical observations remain immutable; their old checks are not represented as current-head execution.
- The adapter runner was not rerun after the canary established OS access failure. Catalogue-based coverage is assessed directly; fresh and reused responses retain actual access timestamps.
- Native label checks include 923 no-adapter skips. Native identifier checks include 909 PMID transport failures and 254 skipped identifiers; bounded supplemental checks independently resolve the 909 PMIDs.
- Scientific findings and native status are unchanged; proposed curation belongs in separate record PRs.
- Final trusted-base post-save review-check, exact-head independent acceptance, final-head CI and merge-group CI occur after saving this immutable observation and are not represented here as already completed.
- All ten original YAML/Markdown pairs are preserved unchanged. Current main was merged normally and pushed without force.
- One explicit issue-bearing ten-record cohort follows the repository persistence policy. Supported records are assessed within that cohort without fabricated findings.
- Bundle issues #2533 (two stale reviews) and #2534 (eight adapter coverage defects) are addressed here. Scientific curation remains in existing #2499; existing validator #2514 remains open.
- Source commit 67d0dd66fe04472c58f4ad9c8b860df18a9f5f8a is retained by tag review-base/pr2349-current-record-followup-20261103.
- CLAUDE.md is an alias of AGENTS.md; canonical regular AGENTS.md bytes are frozen.
- Every inherited source-access and check limitation is attributed to its independent subreview. Fresh fetches, cached response re-reading, abstract-only evidence and full-body passages retain distinct scopes.
- Six original adapter checks have unsupported exemption rationales, and two originals omit the check. Split septin rings and ventral-disc crossbridge are excluded from this defect; no unsupported defect is attributed to their sparse named molecular inventory.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T040543Z-pr2349-current-record-followup
kind: batch
repository: CultureBotAI/CellStructureMech
title: 'PR 2349: current-input review of ten records and adversarial follow-up'
started_at: '2026-11-03T03:55:46.382715Z'
finished_at: '2026-11-03T04:05:43Z'
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
summary: Current-input reassessment of all ten records in PR2349. Stalk-spasmoneme
  causal descriptions and the telocentrosome gamma-tubulin-complex node type changed;
  both are substantively supported within their stated source scopes. Nine records
  have qualified supported assessments and split septin rings retain one minor confirmed
  generic-family grounding finding. The follow-up preserves exact finding lineage,
  refreshes both stale reviews and corrects structured-source applicability evidence
  for eight bundles; no scientific record is edited.
source:
  git_revision: 67d0dd66fe04472c58f4ad9c8b860df18a9f5f8a
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
  - path: data/images/cytoskeleton/stalk_spasmoneme/cil_39509.jpg
    sha256: 9055d5484ed8919c2a9f831c72eca12efd73abc294db7f017beb448ee45554c2
    role: context
  - path: data/images/cytoskeleton/tacc_tog_complex/pmc4749977_f7.jpg
    sha256: 435c851418d002e2c49b2ccc3d39eac1f3bf5b30e5881c56f40c8876d81ef752
    role: context
  - path: data/images/cytoskeleton/tubulin_spool/mikus_2025_figure2.jpg
    sha256: e979bacf2fad45501744aa5dbc2fd75c0fc2ab2b5e6a6be32be77aad0b1f9046
    role: context
  - path: data/structures/cytoskeleton/split_septin_rings.yaml
    sha256: 580abb6f00c144e871e1fded7fbb2dca8584ecf0d47a599f646558642c3027ff
    role: target
  - path: data/structures/cytoskeleton/stalk_spasmoneme.yaml
    sha256: a3de4646f57551323b08c225176359cf3737eff71eaab9da598131d646920bdb
    role: target
  - path: data/structures/cytoskeleton/stentor_km_fiber.yaml
    sha256: 66b91b45477653bcafdf1f875b9820681ea1bdeddf36f9d37f74fabe9408cae6
    role: target
  - path: data/structures/cytoskeleton/stentor_perialgal_microtubule_meshwork.yaml
    sha256: 3a0c8634cf4fca1f7d9253d399b2f6d343d806cd6e3b81e5d92ebf6ff9ab7daf
    role: target
  - path: data/structures/cytoskeleton/tacc_tog_complex.yaml
    sha256: 7d2c57864f3928f8ab9bbc0d7e702aa142292ae00252b385f40a5a8dbcd7b787
    role: target
  - path: data/structures/cytoskeleton/telocentrosome.yaml
    sha256: 7eb101d943b736d756d5ea90d304e6cc2b6dc59a11224203f2c5e7ea30cabc8b
    role: target
  - path: data/structures/cytoskeleton/transition_zone_stellate_fiber_system.yaml
    sha256: ee5fc36bcda7810c550cfef29146f6b124f79703e6b73832b6f005583884ba36
    role: target
  - path: data/structures/cytoskeleton/tubulin_spool.yaml
    sha256: 1180c5c0b3a5c67f58a23b99913f7b78202beb8cf3e01c40ca5aac9c56dcf072
    role: target
  - path: data/structures/cytoskeleton/ventral_disc_crossbridge.yaml
    sha256: bb35ddad7c8b15916d19fa6e5ad334ca3476221330372020fdf4adc8565db67b
    role: target
  - path: data/structures/cytoskeleton/ventral_disc_dorsal_microribbon.yaml
    sha256: 6bcdbfaaf84c4b6152147340dcbb6f5958d6dc6aca2288e034c3f2c357819425
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
  - path: reviews/structured/20261021T084039Z-split-septin-rings-audit/review.md
    sha256: 481ea8845479e04c0d88a99f08adea9ec703821e9756fb23c1123f86a70d1f3a
    role: context
  - path: reviews/structured/20261021T084039Z-split-septin-rings-audit/review.yaml
    sha256: 676333aa87038764afd41f8148be5ab1e6450e9b780d1edac0a0049cb8180384
    role: context
  - path: reviews/structured/20261021T084039Z-stalk-spasmoneme-audit/review.md
    sha256: aa29f54964a1dc43fb5c91a9a008a27b9b761a57eda3ddbde42a5e34406edc61
    role: context
  - path: reviews/structured/20261021T084039Z-stalk-spasmoneme-audit/review.yaml
    sha256: 6b4c67707e1229ba18e42ff5b977762b31f2d3e2158f3c9b17ef6b735af14611
    role: context
  - path: reviews/structured/20261021T084040Z-stentor-km-fiber-audit/review.md
    sha256: df7c35305a1e70762bd02ec8a30ea54b49de9543ca634d063b4c4921b83457a8
    role: context
  - path: reviews/structured/20261021T084040Z-stentor-km-fiber-audit/review.yaml
    sha256: 77d4412c2b35ae63ebd1b559344b9b67d2e782e396fbb6f419f57236eb1e7726
    role: context
  - path: reviews/structured/20261021T084040Z-stentor-perialgal-microtubule-meshwork-audit/review.md
    sha256: 8ea931a66a9d077d981867d611ccce39b202ea38102779938acfa8c2ddd6160b
    role: context
  - path: reviews/structured/20261021T084040Z-stentor-perialgal-microtubule-meshwork-audit/review.yaml
    sha256: 95a1b960d4f8934b30ddd56720755798549ca729776beee9a8bb84cec377977f
    role: context
  - path: reviews/structured/20261021T084040Z-tacc-tog-complex-audit/review.md
    sha256: f6674baf70ab129d07952484a5132da915bda986dc95fa260cfd6fe9c111b88f
    role: context
  - path: reviews/structured/20261021T084040Z-tacc-tog-complex-audit/review.yaml
    sha256: 3e0467f53d2a528897dfaa7d32e5dd27e1933ca15978db6d20017c37c4cf0599
    role: context
  - path: reviews/structured/20261021T084040Z-telocentrosome-audit/review.md
    sha256: 757fa57a34c0489769c01ae1b8c38dabc17b0eecbc6eb8672b778e2c9d8f52b5
    role: context
  - path: reviews/structured/20261021T084040Z-telocentrosome-audit/review.yaml
    sha256: 670452ede8af481e1a3987ef7912162c882528f48e97910f7ea69efa0e89138e
    role: context
  - path: reviews/structured/20261021T084040Z-transition-zone-stellate-fiber-system-audit/review.md
    sha256: 39d0792c2f6a664f7a0aa507251ea2050461bb769e9874aed1b609129a8e24c1
    role: context
  - path: reviews/structured/20261021T084040Z-transition-zone-stellate-fiber-system-audit/review.yaml
    sha256: a78760668e36c695e3c4dc541dbdf6b68481a51b5c823770d6c58ca9c5fc4cc3
    role: context
  - path: reviews/structured/20261021T084041Z-tubulin-spool-audit/review.md
    sha256: dd2d6fa87b7fb05a19e97e2be1f3c2e4bce6ec46b916b3e5a438f0681716f378
    role: context
  - path: reviews/structured/20261021T084041Z-tubulin-spool-audit/review.yaml
    sha256: f1898ed88d87a03c14971c2cfaf87a1fcb9a02355bfa1d0ff58f8d3bf37a584e
    role: context
  - path: reviews/structured/20261021T084041Z-ventral-disc-crossbridge-audit/review.md
    sha256: 898664923a41f91420e9c0eff388c3a0a1e3375a7fc8243c1c15cf18dabed462
    role: context
  - path: reviews/structured/20261021T084041Z-ventral-disc-crossbridge-audit/review.yaml
    sha256: 76882ddb708ad4406c93480743ab7aa73be8c6f45b71323237bae8909f02257b
    role: context
  - path: reviews/structured/20261021T084041Z-ventral-disc-dorsal-microribbon-audit/review.md
    sha256: cd38d7a58c1ce2a2afc97030d1eb9e141441a9e4596636025f1ecec019cb3a4c
    role: context
  - path: reviews/structured/20261021T084041Z-ventral-disc-dorsal-microribbon-audit/review.yaml
    sha256: efee9bcedc3932f1894b0f018a4930a45538f1a4b287e8a9ed54a55b062fe982
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
- target_id: GO:0032176
  path: data/structures/cytoskeleton/split_septin_rings.yaml
  label: split septin rings
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/split_septin_rings.yaml
    role: maintained scientific record
- target_id: cellstructuremech:stalk_spasmoneme
  path: data/structures/cytoskeleton/stalk_spasmoneme.yaml
  label: Stalk spasmoneme
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/stalk_spasmoneme.yaml
    role: maintained scientific record
- target_id: cellstructuremech:stentor_km_fiber
  path: data/structures/cytoskeleton/stentor_km_fiber.yaml
  label: Stentor Km fiber
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/stentor_km_fiber.yaml
    role: maintained scientific record
- target_id: cellstructuremech:stentor_perialgal_microtubule_meshwork
  path: data/structures/cytoskeleton/stentor_perialgal_microtubule_meshwork.yaml
  label: Stentor perialgal microtubule meshwork
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/stentor_perialgal_microtubule_meshwork.yaml
    role: maintained scientific record
- target_id: GO:0070850
  path: data/structures/cytoskeleton/tacc_tog_complex.yaml
  label: TACC/TOG complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/tacc_tog_complex.yaml
    role: maintained scientific record
- target_id: cellstructuremech:telocentrosome
  path: data/structures/cytoskeleton/telocentrosome.yaml
  label: telocentrosome
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/telocentrosome.yaml
    role: maintained scientific record
- target_id: cellstructuremech:transition_zone_stellate_fiber_system
  path: data/structures/cytoskeleton/transition_zone_stellate_fiber_system.yaml
  label: transition zone stellate fiber system
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/transition_zone_stellate_fiber_system.yaml
    role: maintained scientific record
- target_id: cellstructuremech:tubulin_spool
  path: data/structures/cytoskeleton/tubulin_spool.yaml
  label: tubulin spool
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/tubulin_spool.yaml
    role: maintained scientific record
- target_id: GO:0097595
  path: data/structures/cytoskeleton/ventral_disc_crossbridge.yaml
  label: ventral disc crossbridge
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/ventral_disc_crossbridge.yaml
    role: maintained scientific record
- target_id: GO:0097594
  path: data/structures/cytoskeleton/ventral_disc_dorsal_microribbon.yaml
  label: ventral disc dorsal microribbon
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/ventral_disc_dorsal_microribbon.yaml
    role: maintained scientific record
scope:
  description: Exact ten-record PR cohort reassessed against current main de546d03939c0b16c12dcadb1472827e1468df7a.
    Changed inputs are substantively reassessed. Scientific records remain unchanged.
  selection: Complete cohort of ten maintained records reviewed in original PR head
    4eddad83ec3549a0dd735f9868ce44981d6b2973.
  coverage: full
  population_size: 10
  reviewed_target_ids:
  - GO:0032176
  - cellstructuremech:stalk_spasmoneme
  - cellstructuremech:stentor_km_fiber
  - cellstructuremech:stentor_perialgal_microtubule_meshwork
  - GO:0070850
  - cellstructuremech:telocentrosome
  - cellstructuremech:transition_zone_stellate_fiber_system
  - cellstructuremech:tubulin_spool
  - GO:0097595
  - GO:0097594
checks:
- check_id: qc
  name: Full native QC
  status: passed
  required: true
  target_ids:
  - GO:0032176
  - cellstructuremech:stalk_spasmoneme
  - cellstructuremech:stentor_km_fiber
  - cellstructuremech:stentor_perialgal_microtubule_meshwork
  - GO:0070850
  - cellstructuremech:telocentrosome
  - cellstructuremech:transition_zone_stellate_fiber_system
  - cellstructuremech:tubulin_spool
  - GO:0097595
  - GO:0097594
  command: just qc
  exit_code: 0
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  scope_note: Actual local execution at main-merge head 67d0dd66fe04472c58f4ad9c8b860df18a9f5f8a.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-qc
- check_id: labels
  name: Native label correspondence
  status: passed
  required: true
  target_ids:
  - GO:0032176
  - cellstructuremech:stalk_spasmoneme
  - cellstructuremech:stentor_km_fiber
  - cellstructuremech:stentor_perialgal_microtubule_meshwork
  - GO:0070850
  - cellstructuremech:telocentrosome
  - cellstructuremech:transition_zone_stellate_fiber_system
  - cellstructuremech:tubulin_spool
  - GO:0097595
  - GO:0097594
  command: just validate-products
  exit_code: 0
  summary: 4232 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  scope_note: Actual local execution at main-merge head 67d0dd66fe04472c58f4ad9c8b860df18a9f5f8a.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-labels
- check_id: trait-links
  name: TraitMech references
  status: passed
  required: true
  target_ids:
  - GO:0032176
  - cellstructuremech:stalk_spasmoneme
  - cellstructuremech:stentor_km_fiber
  - cellstructuremech:stentor_perialgal_microtubule_meshwork
  - GO:0070850
  - cellstructuremech:telocentrosome
  - cellstructuremech:transition_zone_stellate_fiber_system
  - cellstructuremech:tubulin_spool
  - GO:0097595
  - GO:0097594
  command: just check-trait-links --check
  exit_code: 0
  summary: Native TraitMech link check passed.
  scope_note: Actual local execution at main-merge head 67d0dd66fe04472c58f4ad9c8b860df18a9f5f8a.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-trait-links
- check_id: vendored
  name: Pinned governed files
  status: passed
  required: true
  target_ids:
  - GO:0032176
  - cellstructuremech:stalk_spasmoneme
  - cellstructuremech:stentor_km_fiber
  - cellstructuremech:stentor_perialgal_microtubule_meshwork
  - GO:0070850
  - cellstructuremech:telocentrosome
  - cellstructuremech:transition_zone_stellate_fiber_system
  - cellstructuremech:tubulin_spool
  - GO:0097595
  - GO:0097594
  command: just vendored-check
  exit_code: 0
  summary: Pinned governed files match; native vendored check passed.
  scope_note: Actual local execution at main-merge head 67d0dd66fe04472c58f4ad9c8b860df18a9f5f8a.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-vendored
- check_id: curies
  name: Native identifier resolver
  status: passed
  required: true
  target_ids:
  - GO:0032176
  - cellstructuremech:stalk_spasmoneme
  - cellstructuremech:stentor_km_fiber
  - cellstructuremech:stentor_perialgal_microtubule_meshwork
  - GO:0070850
  - cellstructuremech:telocentrosome
  - cellstructuremech:transition_zone_stellate_fiber_system
  - cellstructuremech:tubulin_spool
  - GO:0097595
  - GO:0097594
  command: just check-curies-strict
  exit_code: 0
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  scope_note: Actual local execution at main-merge head 67d0dd66fe04472c58f4ad9c8b860df18a9f5f8a.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-curies
- check_id: focused-0
  name: validate GO:0032176
  status: passed
  required: true
  target_ids:
  - GO:0032176
  command: just validate data/structures/cytoskeleton/split_septin_rings.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-1
  name: validate-strict GO:0032176
  status: passed
  required: true
  target_ids:
  - GO:0032176
  command: just validate-strict data/structures/cytoskeleton/split_septin_rings.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-2
  name: validate cellstructuremech:stalk_spasmoneme
  status: passed
  required: true
  target_ids:
  - cellstructuremech:stalk_spasmoneme
  command: just validate data/structures/cytoskeleton/stalk_spasmoneme.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-3
  name: validate-strict cellstructuremech:stalk_spasmoneme
  status: passed
  required: true
  target_ids:
  - cellstructuremech:stalk_spasmoneme
  command: just validate-strict data/structures/cytoskeleton/stalk_spasmoneme.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-4
  name: validate cellstructuremech:stentor_km_fiber
  status: passed
  required: true
  target_ids:
  - cellstructuremech:stentor_km_fiber
  command: just validate data/structures/cytoskeleton/stentor_km_fiber.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-5
  name: validate-strict cellstructuremech:stentor_km_fiber
  status: passed
  required: true
  target_ids:
  - cellstructuremech:stentor_km_fiber
  command: just validate-strict data/structures/cytoskeleton/stentor_km_fiber.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-6
  name: validate cellstructuremech:stentor_perialgal_microtubule_meshwork
  status: passed
  required: true
  target_ids:
  - cellstructuremech:stentor_perialgal_microtubule_meshwork
  command: just validate data/structures/cytoskeleton/stentor_perialgal_microtubule_meshwork.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-7
  name: validate-strict cellstructuremech:stentor_perialgal_microtubule_meshwork
  status: passed
  required: true
  target_ids:
  - cellstructuremech:stentor_perialgal_microtubule_meshwork
  command: just validate-strict data/structures/cytoskeleton/stentor_perialgal_microtubule_meshwork.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-8
  name: validate GO:0070850
  status: passed
  required: true
  target_ids:
  - GO:0070850
  command: just validate data/structures/cytoskeleton/tacc_tog_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-9
  name: validate-strict GO:0070850
  status: passed
  required: true
  target_ids:
  - GO:0070850
  command: just validate-strict data/structures/cytoskeleton/tacc_tog_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-10
  name: validate cellstructuremech:telocentrosome
  status: passed
  required: true
  target_ids:
  - cellstructuremech:telocentrosome
  command: just validate data/structures/cytoskeleton/telocentrosome.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-11
  name: validate-strict cellstructuremech:telocentrosome
  status: passed
  required: true
  target_ids:
  - cellstructuremech:telocentrosome
  command: just validate-strict data/structures/cytoskeleton/telocentrosome.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-12
  name: validate cellstructuremech:transition_zone_stellate_fiber_system
  status: passed
  required: true
  target_ids:
  - cellstructuremech:transition_zone_stellate_fiber_system
  command: just validate data/structures/cytoskeleton/transition_zone_stellate_fiber_system.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-13
  name: validate-strict cellstructuremech:transition_zone_stellate_fiber_system
  status: passed
  required: true
  target_ids:
  - cellstructuremech:transition_zone_stellate_fiber_system
  command: just validate-strict data/structures/cytoskeleton/transition_zone_stellate_fiber_system.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-14
  name: validate cellstructuremech:tubulin_spool
  status: passed
  required: true
  target_ids:
  - cellstructuremech:tubulin_spool
  command: just validate data/structures/cytoskeleton/tubulin_spool.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-15
  name: validate-strict cellstructuremech:tubulin_spool
  status: passed
  required: true
  target_ids:
  - cellstructuremech:tubulin_spool
  command: just validate-strict data/structures/cytoskeleton/tubulin_spool.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-16
  name: validate GO:0097595
  status: passed
  required: true
  target_ids:
  - GO:0097595
  command: just validate data/structures/cytoskeleton/ventral_disc_crossbridge.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-17
  name: validate-strict GO:0097595
  status: passed
  required: true
  target_ids:
  - GO:0097595
  command: just validate-strict data/structures/cytoskeleton/ventral_disc_crossbridge.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-18
  name: validate GO:0097594
  status: passed
  required: true
  target_ids:
  - GO:0097594
  command: just validate data/structures/cytoskeleton/ventral_disc_dorsal_microribbon.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-19
  name: validate-strict GO:0097594
  status: passed
  required: true
  target_ids:
  - GO:0097594
  command: just validate-strict data/structures/cytoskeleton/ventral_disc_dorsal_microribbon.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: supplemental-pmid
  name: Supplemental bounded PMID authority checks
  status: passed
  required: true
  target_ids:
  - GO:0032176
  - cellstructuremech:stalk_spasmoneme
  - cellstructuremech:stentor_km_fiber
  - cellstructuremech:stentor_perialgal_microtubule_meshwork
  - GO:0070850
  - cellstructuremech:telocentrosome
  - cellstructuremech:transition_zone_stellate_fiber_system
  - cellstructuremech:tubulin_spool
  - GO:0097595
  - GO:0097594
  command: .venv/bin/python /private/tmp/cellstructure-batches-2346-2397-20261103/check_pmid_chunks.py
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349
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
  - GO:0032176
  - cellstructuremech:stalk_spasmoneme
  - cellstructuremech:stentor_km_fiber
  - cellstructuremech:stentor_perialgal_microtubule_meshwork
  - GO:0070850
  - cellstructuremech:telocentrosome
  - cellstructuremech:transition_zone_stellate_fiber_system
  - cellstructuremech:tubulin_spool
  - GO:0097595
  - GO:0097594
  summary: Official catalogue coverage contains 20 organisms and 28 datasets, all
    bacterial/archaeal; none matches this yeast/protist cohort. Fresh and independently
    reread cached catalogue responses retain actual access times and boundaries. The
    historical runner failure is documented separately; no new runner execution is
    claimed.
  evidence_ids:
  - plaque-adapter-datasets-current
  - micro-current-current-adapter-catalogue
  - septin-s2349-current-adapter-catalogue
- check_id: independent-scientific-review
  name: Independent claim-level source review
  status: passed
  required: true
  target_ids:
  - GO:0032176
  - cellstructuremech:stalk_spasmoneme
  - cellstructuremech:stentor_km_fiber
  - cellstructuremech:stentor_perialgal_microtubule_meshwork
  - GO:0070850
  - cellstructuremech:telocentrosome
  - cellstructuremech:transition_zone_stellate_fiber_system
  - cellstructuremech:tubulin_spool
  - GO:0097595
  - GO:0097594
  summary: Three read-only reviewers covered the complete ten-record cohort, including
    changed inputs, with explicit scientific findings and source-access limits. Final
    artifact/head acceptance occurs after saving.
  evidence_ids:
  - plaque-stalk-agent-go
  - plaque-stalk-agent-taxon-60850
  - plaque-stalk-agent-taxon-168244
  - plaque-stalk-agent-IPR050145
  - plaque-stalk-agent-literature-metadata
  - plaque-stalk-primary-agent-routledge-native-pdf
  - plaque-stalk-primary-agent-konior-pdf
  - plaque-stalk-primary-agent-ryu-pdf
  - plaque-stalk-agent-cil39509-curl
  - plaque-stalk-agent-cil-preview
  - plaque-stentor-km-agent-go
  - plaque-stentor-km-agent-IPR002452
  - plaque-perialgal-prep-IPR002453
  - plaque-stentor-km-agent-taxon-5963
  - plaque-stentor-km-agent-literature-metadata
  - plaque-stentor-km-agent-huang1973-pdf
  - plaque-stentor-km-agent-huang1973-jats
  - plaque-stentor-km-agent-huang1973-package
  - plaque-stentor-km-agent-slabodnick2014
  - plaque-perialgal-prep-go
  - plaque-perialgal-prep-tax-2721102
  - plaque-perialgal-prep-boudreau2025-meta
  - plaque-perialgal-prep-boudreau2025-jats
  - plaque-perialgal-prep-figure3
  - plaque-perialgal-prep-paper-pdf
  - plaque-perialgal-prep-boudreau2025-package
  - plaque-stalk-asai1998-publisher-abstract
  - micro-current-stellate-agent-go
  - micro-current-stellate-agent-tax-3055
  - micro-current-stellate-agent-P05434
  - micro-current-stellate-agent-IPR050145
  - micro-current-stellate-agent-IPR050230
  - micro-current-stellate-agent-sanders1994-pdf
  - micro-current-stellate-agent-sanders1994-jats
  - micro-current-stellate-agent-taillon1992-pdf
  - micro-current-jarvik1991-abstract
  - micro-current-stellate-agent-lohret1998-html
  - micro-current-stellate-agent-diener2015-html
  - micro-current-stellate-agent-hoek2022-pdf
  - micro-current-spool-agent-go
  - micro-current-spool-agent-tax-241424
  - micro-current-spool-agent-IPR000217
  - micro-current-spool-agent-mikus2025-paper-pdf
  - micro-current-spool-agent-table-s1
  - micro-current-spool-agent-mikus2025-crossref
  - micro-current-spool-agent-project
  - micro-current-spool-agent-volumes-dataset
  - micro-current-spool-agent-categories
  - micro-current-spool-agent-github-readme
  - micro-current-spool-agent-publisher-figure2
  - micro-current-crossbridge-agent-go
  - micro-current-crossbridge-agent-tax-5741
  - micro-current-crossbridge-agent-epmc
  - micro-current-crossbridge-agent-schwartz2012-jats
  - micro-current-microribbon-agent-go-mt
  - micro-current-microribbon-agent-tax-184922
  - micro-current-microribbon-agent-epmc-hagen2011
  - micro-current-microribbon-agent-hagen2011-jats
  - micro-current-microribbon-agent-ipr-008374
  - micro-current-microribbon-agent-ipr-038835
  - micro-current-microribbon-agent-pfam-06705
  - septin-s2349-split-rings-agent-go
  - septin-s2349-split-rings-agent-family
  - septin-s2349-split-rings-agent-douglas-pmc
  - septin-s2349-split-rings-agent-versele-pmc
  - septin-s2349-tacc-prep-go
  - septin-s2349-tacc-prep-tax-4896
  - septin-s2349-tacc-prep-tax-284812
  - septin-s2349-tacc-prep-IPR045110
  - septin-s2349-tacc-prep-IPR024312
  - septin-s2349-tacc-prep-matches-Q9URY2
  - septin-s2349-tacc-prep-Q9URY2
  - septin-s2349-tacc-prep-O94534
  - septin-s2349-tacc-prep-Q10198
  - septin-s2349-tacc-prep-hussmann2016-jats
  - septin-s2349-tacc-prep-nucleation2018-jats
  - septin-s2349-tacc-prep-attachment2013-jats
  - septin-s2349-tacc-prep-transport2014-jats
  - septin-s2349-tacc-prep-dis1_2019-jats
  - septin-s2349-tacc-prep-figure7
  - septin-s2349-telo-prep-go
  - septin-s2349-telo-prep-IPR045119
  - septin-s2349-telo-prep-IPR005334
  - septin-s2349-telo-prep-IPR030268
  - septin-s2349-telo-prep-IPR026983
  - septin-s2349-telo-prep-matches-P87245
  - septin-s2349-telo-prep-matches-O43087
  - septin-s2349-telo-prep-matches-O94488
  - septin-s2349-telo-prep-matches-O13290
  - septin-s2349-telo-prep-matches-O42667
  - septin-s2349-telo-prep-Q09825
  - septin-s2349-telo-prep-P87245
  - septin-s2349-telo-prep-O43087
  - septin-s2349-telo-prep-O94488
  - septin-s2349-telo-prep-Q9Y705
  - septin-s2349-telo-prep-Q9UTS6
  - septin-s2349-telo-prep-O13290
  - septin-s2349-telo-prep-O42667
  - septin-s2349-telo-prep-yoshida2013-jats
  - septin-s2349-telo-agent-yoshida2013-supp
  - septin-s2349-telo-prep-jimenez2025-jats
  - septin-s2349-telo-agent-jimenez2025-supp
  - septin-s2349-telo-prep-figure2
  - septin-s2349-current-adapter-catalogue
  - septin-s2349-policy
- check_id: historical-adapter-runner
  name: Retained historical adapter runner availability
  status: unavailable
  required: false
  target_ids:
  - cellstructuremech:stalk_spasmoneme
  - cellstructuremech:stentor_km_fiber
  - cellstructuremech:stentor_perialgal_microtubule_meshwork
  - GO:0070850
  - cellstructuremech:telocentrosome
  - cellstructuremech:transition_zone_stellate_fiber_system
  - cellstructuremech:tubulin_spool
  - GO:0097594
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
  reference: data/structures/cytoskeleton/split_septin_rings.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T04:05:43Z'
  support: context_only
  summary: Original frozen SHA256 580abb6f00c144e871e1fded7fbb2dca8584ecf0d47a599f646558642c3027ff;
    current SHA256 580abb6f00c144e871e1fded7fbb2dca8584ecf0d47a599f646558642c3027ff.
    Record bytes unchanged since the original review.
  snapshot_sha256: 580abb6f00c144e871e1fded7fbb2dca8584ecf0d47a599f646558642c3027ff
- evidence_id: original-review-0
  kind: prior_review
  reference: reviews/structured/20261021T084039Z-split-septin-rings-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T04:05:43Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 676333aa87038764afd41f8148be5ab1e6450e9b780d1edac0a0049cb8180384
- evidence_id: current-record-1
  kind: record_content
  reference: data/structures/cytoskeleton/stalk_spasmoneme.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T04:05:43Z'
  support: context_only
  summary: Original frozen SHA256 42e090ec489b240c6b061368c7f44eba2267b46642bff54ef7c860e9e7eb7151;
    current SHA256 a3de4646f57551323b08c225176359cf3737eff71eaab9da598131d646920bdb.
    Changed record reassessed against current sources.
  snapshot_sha256: a3de4646f57551323b08c225176359cf3737eff71eaab9da598131d646920bdb
- evidence_id: original-review-1
  kind: prior_review
  reference: reviews/structured/20261021T084039Z-stalk-spasmoneme-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T04:05:43Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 6b4c67707e1229ba18e42ff5b977762b31f2d3e2158f3c9b17ef6b735af14611
- evidence_id: current-record-2
  kind: record_content
  reference: data/structures/cytoskeleton/stentor_km_fiber.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T04:05:43Z'
  support: context_only
  summary: Original frozen SHA256 66b91b45477653bcafdf1f875b9820681ea1bdeddf36f9d37f74fabe9408cae6;
    current SHA256 66b91b45477653bcafdf1f875b9820681ea1bdeddf36f9d37f74fabe9408cae6.
    Record bytes unchanged since the original review.
  snapshot_sha256: 66b91b45477653bcafdf1f875b9820681ea1bdeddf36f9d37f74fabe9408cae6
- evidence_id: original-review-2
  kind: prior_review
  reference: reviews/structured/20261021T084040Z-stentor-km-fiber-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T04:05:43Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 77d4412c2b35ae63ebd1b559344b9b67d2e782e396fbb6f419f57236eb1e7726
- evidence_id: current-record-3
  kind: record_content
  reference: data/structures/cytoskeleton/stentor_perialgal_microtubule_meshwork.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T04:05:43Z'
  support: context_only
  summary: Original frozen SHA256 3a0c8634cf4fca1f7d9253d399b2f6d343d806cd6e3b81e5d92ebf6ff9ab7daf;
    current SHA256 3a0c8634cf4fca1f7d9253d399b2f6d343d806cd6e3b81e5d92ebf6ff9ab7daf.
    Record bytes unchanged since the original review.
  snapshot_sha256: 3a0c8634cf4fca1f7d9253d399b2f6d343d806cd6e3b81e5d92ebf6ff9ab7daf
- evidence_id: original-review-3
  kind: prior_review
  reference: reviews/structured/20261021T084040Z-stentor-perialgal-microtubule-meshwork-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T04:05:43Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 95a1b960d4f8934b30ddd56720755798549ca729776beee9a8bb84cec377977f
- evidence_id: current-record-4
  kind: record_content
  reference: data/structures/cytoskeleton/tacc_tog_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T04:05:43Z'
  support: context_only
  summary: Original frozen SHA256 7d2c57864f3928f8ab9bbc0d7e702aa142292ae00252b385f40a5a8dbcd7b787;
    current SHA256 7d2c57864f3928f8ab9bbc0d7e702aa142292ae00252b385f40a5a8dbcd7b787.
    Record bytes unchanged since the original review.
  snapshot_sha256: 7d2c57864f3928f8ab9bbc0d7e702aa142292ae00252b385f40a5a8dbcd7b787
- evidence_id: original-review-4
  kind: prior_review
  reference: reviews/structured/20261021T084040Z-tacc-tog-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T04:05:43Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 3e0467f53d2a528897dfaa7d32e5dd27e1933ca15978db6d20017c37c4cf0599
- evidence_id: current-record-5
  kind: record_content
  reference: data/structures/cytoskeleton/telocentrosome.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T04:05:43Z'
  support: context_only
  summary: Original frozen SHA256 05d5a42ee4b63bd62b3e8c6c0137e2268964980fcc00f27769e29498cf67dca7;
    current SHA256 7eb101d943b736d756d5ea90d304e6cc2b6dc59a11224203f2c5e7ea30cabc8b.
    Changed record reassessed against current sources.
  snapshot_sha256: 7eb101d943b736d756d5ea90d304e6cc2b6dc59a11224203f2c5e7ea30cabc8b
- evidence_id: original-review-5
  kind: prior_review
  reference: reviews/structured/20261021T084040Z-telocentrosome-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T04:05:43Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 670452ede8af481e1a3987ef7912162c882528f48e97910f7ea69efa0e89138e
- evidence_id: current-record-6
  kind: record_content
  reference: data/structures/cytoskeleton/transition_zone_stellate_fiber_system.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T04:05:43Z'
  support: context_only
  summary: Original frozen SHA256 ee5fc36bcda7810c550cfef29146f6b124f79703e6b73832b6f005583884ba36;
    current SHA256 ee5fc36bcda7810c550cfef29146f6b124f79703e6b73832b6f005583884ba36.
    Record bytes unchanged since the original review.
  snapshot_sha256: ee5fc36bcda7810c550cfef29146f6b124f79703e6b73832b6f005583884ba36
- evidence_id: original-review-6
  kind: prior_review
  reference: reviews/structured/20261021T084040Z-transition-zone-stellate-fiber-system-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T04:05:43Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: a78760668e36c695e3c4dc541dbdf6b68481a51b5c823770d6c58ca9c5fc4cc3
- evidence_id: current-record-7
  kind: record_content
  reference: data/structures/cytoskeleton/tubulin_spool.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T04:05:43Z'
  support: context_only
  summary: Original frozen SHA256 1180c5c0b3a5c67f58a23b99913f7b78202beb8cf3e01c40ca5aac9c56dcf072;
    current SHA256 1180c5c0b3a5c67f58a23b99913f7b78202beb8cf3e01c40ca5aac9c56dcf072.
    Record bytes unchanged since the original review.
  snapshot_sha256: 1180c5c0b3a5c67f58a23b99913f7b78202beb8cf3e01c40ca5aac9c56dcf072
- evidence_id: original-review-7
  kind: prior_review
  reference: reviews/structured/20261021T084041Z-tubulin-spool-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T04:05:43Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: f1898ed88d87a03c14971c2cfaf87a1fcb9a02355bfa1d0ff58f8d3bf37a584e
- evidence_id: current-record-8
  kind: record_content
  reference: data/structures/cytoskeleton/ventral_disc_crossbridge.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T04:05:43Z'
  support: context_only
  summary: Original frozen SHA256 bb35ddad7c8b15916d19fa6e5ad334ca3476221330372020fdf4adc8565db67b;
    current SHA256 bb35ddad7c8b15916d19fa6e5ad334ca3476221330372020fdf4adc8565db67b.
    Record bytes unchanged since the original review.
  snapshot_sha256: bb35ddad7c8b15916d19fa6e5ad334ca3476221330372020fdf4adc8565db67b
- evidence_id: original-review-8
  kind: prior_review
  reference: reviews/structured/20261021T084041Z-ventral-disc-crossbridge-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T04:05:43Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 76882ddb708ad4406c93480743ab7aa73be8c6f45b71323237bae8909f02257b
- evidence_id: current-record-9
  kind: record_content
  reference: data/structures/cytoskeleton/ventral_disc_dorsal_microribbon.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T04:05:43Z'
  support: context_only
  summary: Original frozen SHA256 6bcdbfaaf84c4b6152147340dcbb6f5958d6dc6aca2288e034c3f2c357819425;
    current SHA256 6bcdbfaaf84c4b6152147340dcbb6f5958d6dc6aca2288e034c3f2c357819425.
    Record bytes unchanged since the original review.
  snapshot_sha256: 6bcdbfaaf84c4b6152147340dcbb6f5958d6dc6aca2288e034c3f2c357819425
- evidence_id: original-review-9
  kind: prior_review
  reference: reviews/structured/20261021T084041Z-ventral-disc-dorsal-microribbon-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T04:05:43Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: efee9bcedc3932f1894b0f018a4930a45538f1a4b287e8a9ed54a55b062fe982
- evidence_id: plaque-stalk-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005622
  locator: results GO0005622 name, definition and isObsolete; freshly retrieved exact
    source bytes at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/stalk-agent-go.source
  accessed_at: '2026-11-03T03:59:27.142667Z'
  support: supports
  summary: GO0005622 is active intracellular anatomical structure. The broad is-a
    parent is compatible with the stalk-contained organelle; it is not an exact spasmoneme
    identifier.
  snapshot_sha256: 41de7353f02b2b815b0dbbbab1cd36c29e08425722f02dc06e35d496275c83f6
- evidence_id: plaque-stalk-agent-taxon-60850
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/60850
  locator: Native taxId, scientificName, species rank and lineage; freshly retrieved
    exact source bytes at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/stalk-agent-taxon-60850.source
  accessed_at: '2026-11-03T03:59:27.142905Z'
  support: supports
  summary: NCBITaxon60850 identifies Vorticella convallaria at species rank.
  snapshot_sha256: 103212be547d5a2cd1015da6d262e4b9628edcaaa0a4f7394137c34e693c3212
- evidence_id: plaque-stalk-agent-taxon-168244
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/168244
  locator: Native taxId, scientificName, species rank and lineage; freshly retrieved
    exact source bytes at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/stalk-agent-taxon-168244.source
  accessed_at: '2026-11-03T03:59:27.142957Z'
  support: supports
  summary: NCBITaxon168244 identifies Carchesium polypinum at species rank.
  snapshot_sha256: 06bab3e9ac900e250a3007979438944936a13b9de1b2526d58a5231cb79200a6
- evidence_id: plaque-stalk-agent-IPR050145
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050145/
  locator: Native metadata accession/name/type/description, including description
    provenance flags; fresh source snapshot in /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/stalk-agent-IPR050145.source
  accessed_at: '2026-11-03T03:59:27.143017Z'
  support: supports
  summary: IPR050145 is the broader Centrin/CML-like family, including caltractin,
    obelin and plant CML proteins. Its description is labelled llm=true, checked=true
    by InterPro. This authority check establishes entry scope, not exact native spasmin
    membership; the record appropriately leaves the narrower class REVIEWED_LABEL_ONLY
    and uses primary experiments for biology.
  snapshot_sha256: 386371fb67a7de41d9f9a6ded2bbb77530d9a27411b46349d2ac050d45832910
- evidence_id: plaque-stalk-agent-literature-metadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=100&query=DOI%3A%2210.1083/jcb.77.2.358%22%20OR%20DOI%3A%2210.1111/j.1550-7408.1999.tb04601.x%22%20OR%20DOI%3A%2210.1016/j.bpj.2012.07.038%22%20OR%20DOI%3A%2210.1111/j.1550-7408.1998.tb05066.x%22%20OR%20DOI%3A%2210.1111/jeu.70006%22
  locator: resultList.result DOI/title/authors/year/PMID/abstractText; abstract-tier
    scientific support for1999/2025; freshly retrieved exact source bytes at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/stalk-agent-literature-metadata.source
  accessed_at: '2026-11-03T03:59:27.143396Z'
  support: supports
  summary: 'Four exact DOI identities and abstracts recovered: Routledge1978 PMID418073,
    Maciejewski1999 PMID10361738, Ryu2012 PMID23009835, Jiang2025 PMID40059491. The
    1999 abstract supports cloned/recombinant calcium-binding spasmin and 1F5 immunolocalization.
    The 2025 abstract supports CCDC and EGF-like stalk membership but specifically
    places only CCDC proteins in the sheath; neither demonstrates spasmoneme membership.
    The 1998 DOI was not returned by this bounded query, and is verified separately
    at the publisher.'
  snapshot_sha256: 3a3aa0ae410420ff18575d6c86fba1490a67dde8c9262178b57d5877c8301487
- evidence_id: plaque-stalk-primary-agent-routledge-native-pdf
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2110051.1/PMC2110051.1.pdf
  locator: PDF pp358-360 introduction and preparation/extraction Methods; pp361-364
    extraction, protease-inhibitor control and calcium response Results; pp366-368
    cross-genus morphology and limitations Discussion; fresh source snapshot in /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/stalk-primary-agent-routledge-native-pdf.source
  accessed_at: '2026-11-03T03:59:27.143444Z'
  support: supports
  summary: Primary article supports calcium-responsive glycerinated organelles and
    spasmin-rich extracted fractions, with unidentified proteins and incomplete reconstruction.
    The p363 Carchesium control responds normally to high/low calcium; p364 explicitly
    notes slow contraction at pH9. Rapid contraction is introductory context, not
    a preparation-independent measured rate. Genera differ in stalk coiling/folding;
    sheath and body continuity do not erase organelle boundaries. No absolute actin/tubulin
    absence is inferred.
  snapshot_sha256: 44178370ba3b2d378cc48b5b704246270c4ba67f3f2bba9fc13984d28eea42fe
- evidence_id: plaque-stalk-primary-agent-konior-pdf
  kind: primary_source
  reference: https://ilacadofsci.com/wp-content/uploads/2013/03/102-15MS2905-print.pdf
  locator: Main Methods pp163-165, Results/Discussion pp165-167, legends Figures2-8
    pp170-174; no raw immunogold recount; fresh source snapshot in /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/stalk-primary-agent-konior-pdf.source
  accessed_at: '2026-11-03T03:59:27.143494Z'
  support: supports
  summary: 'Fresh primary PDF text supports distinct centrin/spasmin antibody patterns:
    N-termVcCentrin4 detects one Western band; 1F5 detects two. Both label fibrillar
    mass, with differing tubular localization and sheath-access requirements. Sfi1-like
    backbone, calcium-storage/structural roles and disassembly/reassembly remain a
    proposed model, not an identified native assembly or stoichiometry.'
  snapshot_sha256: 2e671848682f3941d8897979290ebf7ef7704335692c2cf4dbd1af69286ca70b
- evidence_id: plaque-stalk-primary-agent-ryu-pdf
  kind: primary_source
  reference: https://lab.prd.vanderbilt.edu/lang-lab/wp-content/uploads/sites/195/2023/01/MaximalForceCharacteristicsoftheCa2D-PoweredActuatorofVorticellaconvallaria2012.pdf
  locator: Primary main PDF pp860-866 introduction, channel-flow Methods, Results
    and Discussion; Figures1-5 captions; Supporting Material not read; fresh source
    snapshot in /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/stalk-primary-agent-ryu-pdf.source
  accessed_at: '2026-11-03T03:59:27.143643Z'
  support: supports
  summary: Live V. convallaria microfluidic channel experiments directly support slower
    contraction and less cell excursion as resistance rises (p862). Stalk coiling
    and retraction describe Vorticella, not universal folding behavior of all peritrich
    genera. Residual force is inferred hydrodynamically and maximal tension extrapolated;
    work omits terms, and serial force addition/motor-unit organization is hypothetical.
    These observations support the three newly added descriptions only within the
    graph's stated preparation/species and NONMECHANISTIC scope.
  snapshot_sha256: ffcfac34712cef3a989f9f6f029ca49b73c396405100749e7908be3bc5c16570
- evidence_id: plaque-stalk-agent-cil39509-curl
  kind: database
  reference: https://www.cellimagelibrary.org/images/39509
  locator: Native landing-page JSON-LD, Description, Licensing, Biological Sources,
    Imaging and sample preparation; fresh source snapshot in /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/stalk-agent-cil39509-curl.source
  accessed_at: '2026-11-03T03:59:27.603101Z'
  support: supports
  summary: CIL39509 supports DOI10.7295/W9CIL39509, Richard Allen/Hawaii attribution,
    V. convallaria, TEM acquisition February15,1972, public-domain status and the
    exact preview URL. Current JSON-LD datePublished is January23,2012; the original
    review's January22 statement is a historical metadata observation. The record
    asserts only2012, so no current record correction follows. Physiological claims
    cited by image metadata are not demonstrated by this image.
  snapshot_sha256: 62180bb5a91d739a5ca78acc34f59e9ce4d5f92184da067e2f01eb675a33be9b
- evidence_id: plaque-stalk-agent-cil-preview
  kind: primary_source
  reference: https://cildata.crbs.ucsd.edu/media/thumbnail_display/39509/39509_thumbnailx512.jpg
  locator: Entire source-served JPEG; visual inspection of identically hashed tracked
    image after native inspect added it; fresh source snapshot in /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/stalk-agent-cil-preview.source
  accessed_at: '2026-11-03T03:59:27.779038Z'
  support: supports
  summary: Fresh source JPEG exactly matches tracked cil_39509.jpg SHA2569055d5484ed8919c2a9f831c72eca12efd73abc294db7f017beb448ee45554c2.
    The inspected preview shows a spasmoneme profile with tubules and neighboring
    cortex. No protein-specific localization, calcium transport, calibrated dimensions
    or precise stalk level is inferred.
  snapshot_sha256: 9055d5484ed8919c2a9f831c72eca12efd73abc294db7f017beb448ee45554c2
- evidence_id: plaque-stentor-km-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097427,GO:0030863,GO:0035253
  locator: Exact three results, definition, name, isObsolete and synonyms; freshly
    retrieved exact source bytes at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/stentor-km-agent-go.source
  accessed_at: '2026-11-03T03:59:27.796429Z'
  support: supports
  summary: Active GO0097427 is the broader arrangement of closely apposed parallel
    microtubules. GO0030863 denotes cortical cytoskeleton. GO0035253 denotes a typically
    striated ciliary rootlet, not an exact identifier for the described overlapping
    ribbon bundle. Parthood of the local structure is supported by microscopy, not
    an asserted native GO link to a minted term.
  snapshot_sha256: 45d23bce5337606a260e9596b5954b08f2e5872aa63388252921f8eea28bc485
- evidence_id: plaque-stentor-km-agent-IPR002452
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002452/
  locator: metadata accession/name/type/description; family identity and alpha/beta
    microtubule composition; freshly retrieved exact source bytes at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/stentor-km-agent-IPR002452.source
  accessed_at: '2026-11-03T03:59:27.806596Z'
  support: supports
  summary: IPR002452 is the Alpha tubulin family and supports alpha/beta heterodimer
    composition of microtubules.
  snapshot_sha256: ff28f4d004d8f82a804f7263ff1df3ab78d7bdbdeee755fa924a58e872602b5a
- evidence_id: plaque-perialgal-prep-IPR002453
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002453/
  locator: metadata accession/name/type/description; family identity and alpha/beta
    microtubule composition; freshly retrieved exact source bytes at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/perialgal-prep-IPR002453.source
  accessed_at: '2026-11-03T03:59:27.807776Z'
  support: supports
  summary: IPR002453 is the Beta tubulin family. It is a family-class grounding, not
    a native Stentor paralogue census or bridge-motor identity.
  snapshot_sha256: edbfe5509d6e568069c7105eacc2b7e296e84e0790a16a63d836c45a094d20ef
- evidence_id: plaque-stentor-km-agent-taxon-5963
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5963
  locator: taxId/scientificName/rank/lineage/otherNames; freshly retrieved exact source
    bytes at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/stentor-km-agent-taxon-5963.source
  accessed_at: '2026-11-03T03:59:27.886462Z'
  support: supports
  summary: NCBITaxon5963 is Stentor coeruleus at species rank; historical names and
    lineage are explicit. No experimental strain or genus-wide prevalence is inferred.
  snapshot_sha256: e66b4bd1362354340ef4683fab0f80bead40dfcfe41f4814c3b7283f96193813
- evidence_id: plaque-stentor-km-agent-literature-metadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=100&query=DOI%3A%2210.1083/jcb.57.3.704%22%20OR%20DOI%3A%2210.1371/journal.pbio.1001861%22
  locator: Two native core result entries title/DOI/authors/year/PMID/PMCID; freshly
    retrieved exact source bytes at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/stentor-km-agent-literature-metadata.source
  accessed_at: '2026-11-03T03:59:27.941427Z'
  support: supports
  summary: 'Exact identities verified: Huang/Pitelka1973 DOI10.1083/jcb.57.3.704 PMID4633444
    PMC2108994; Slabodnick et al.2014 DOI10.1371/journal.pbio.1001861 PMID24823688
    PMC4019465. Both are primary studies; metadata abstracts do not replace the inspected
    bodies.'
  snapshot_sha256: ab9edcabcad6510b5d3add01b9e099446672e642f2e752ad34fc3927182850a7
- evidence_id: plaque-stentor-km-agent-huang1973-pdf
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2108994.1/PMC2108994.1.pdf
  locator: Primary PDF pp704-706 introduction/Methods; pp708-711 cortical organization;
    pp715-717 overlap Results; pp719-724 discussion through bridge-motor limits; complete
    PDF page8/printed711 Figure8 visually inspected; fresh source snapshot in /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/stentor-km-agent-huang1973-pdf.source
  accessed_at: '2026-11-03T03:59:27.960099Z'
  support: supports
  summary: Successive posterior-basal-body-associated microtubule ribbons overlap
    along cortical rows, distinct from deeper myonemes and transverse microtubules.
    Fixed extended cells have less overlap; active relative sliding is a model, selective
    disruptions were unsuccessful, and bridge ATPase/dynein identity lacks direct
    evidence. Figure8 is the extended-cell transverse Km bundle with numbering diagram
    and a printed0.1micrometer scale bar.
  snapshot_sha256: 61e5f2ef7e22ef22f7e1d2b2e27ecf4f58195865867356261daadaf24fe17514
- evidence_id: plaque-stentor-km-agent-huang1973-jats
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2108994.1/PMC2108994.1.xml
  locator: JATS article identity and permissions; PDF/XML MD5 values checked against
    current native package; fresh source snapshot in /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/stentor-km-agent-huang1973-jats.source
  accessed_at: '2026-11-03T03:59:28.011162Z'
  support: supports
  summary: Native JATS identifies Huang/Pitelka1973 and explicitly CC BY-NC-SA4.0.
    The image remains a link to printed Figure8 on PDF page8; no separately invented
    XML figure accession or repository hosting is asserted.
  snapshot_sha256: d8e63c325a7d4af8fdcac7a0d20769bbd3790aaa272a34240702f030150c4499
- evidence_id: plaque-stentor-km-agent-huang1973-package
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2108994.1/PMC2108994.1.json
  locator: Version, DOI/PMID, retraction/licence flags, PDF/XML paths and MD5; fresh
    source snapshot in /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/stentor-km-agent-huang1973-package.source
  accessed_at: '2026-11-03T03:59:28.420966Z'
  support: supports
  summary: Version1 metadata identifies PMC2108994/PMID4633444 and DOI10.1083/jcb.57.3.704;
    is_retracted=false. Downloaded PDF MD5895cb427cb5cf8cc9afac7f76f59802d and XML
    MD580e819ecc2c76fdcf38709fe760b7d44 exactly match metadata. The precise4.0 licence
    is supplied by JATS.
  snapshot_sha256: 8a8fb5fd2065b9c3cdf0b1de373b3e8817e53945f308613d8a6989178a2b0e52
- evidence_id: plaque-stentor-km-agent-slabodnick2014
  kind: primary_source
  reference: https://journals.plos.org/plosbiology/article/file?id=10.1371/journal.pbio.1001861&type=manuscript
  locator: Publisher XML Results s2b and s2c, Figures2/3 legends; culture/RNAi/qPCR/antibody/IF
    Methods s4a,s4d-s4g; fresh source snapshot in /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/stentor-km-agent-slabodnick2014.source
  accessed_at: '2026-11-03T03:59:28.473596Z'
  support: supports
  summary: Beta-tubulin RNAi reduces transcript and causes disoriented, broken/discontinuous
    cortical rows in S. coeruleus. The assay is broad tubulin depletion, not a selective
    Km-fiber intervention. Figure2 calls cortical staining anti-alpha-tubulin while
    Methods identify anti-acetylated-tubulin clone6-11B-1. Mob1 diffusely labels cortical
    rows; this does not identify it as a purified Km constituent. Unrelated later
    Mob1 morphogenesis experiments and supplements were not independently audited.
  snapshot_sha256: ebaa941d4bafc7e757ab197bba170fcfc56ca05f8af7b3cef2b80f38b9e4aac0
- evidence_id: plaque-perialgal-prep-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005622,GO:0030863
  locator: Both term definitions and active flags; freshly retrieved exact source
    bytes at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/perialgal-prep-go.source
  accessed_at: '2026-11-03T03:59:28.480657Z'
  support: supports
  summary: 'Both terms are active: GO0005622 is intracellular anatomical structure
    and GO0030863 is the cortical cytoskeleton beneath the plasma membrane. They provide
    a broad parent and encompassing framework, respectively.'
  snapshot_sha256: a51dafa11e7eafbaa411cc1af78225229343863c98b30dd927d782676aff3bdd
- evidence_id: plaque-perialgal-prep-tax-2721102
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2721102
  locator: taxId, scientificName, rank and lineage; freshly retrieved exact source
    bytes at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/perialgal-prep-tax-2721102.source
  accessed_at: '2026-11-03T03:59:28.497617Z'
  support: supports
  summary: Taxon2721102 is Stentor pyriformis at species rank, in Stentoridae/Heterotrichida.
  snapshot_sha256: cd3ca9f2bf6dc5cac38dc284b5275956c14cec0141ffb8c951383c90db5bd928
- evidence_id: plaque-perialgal-prep-go-search
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=perialgal
  locator: numberOfHits, results and pageInfo; freshly retrieved exact source bytes
    at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/perialgal-prep-go-search.source
  accessed_at: '2026-11-03T03:59:28.506175Z'
  support: context_only
  summary: The current exact perialgal query returns zero hits. This is a bounded
    query result, not an exhaustive absence claim across ontology resources.
  snapshot_sha256: 4f0027cdf6df79bb6d4e90297666e971eb23ca7cfa19fc11fb9c9931fd5f1004
  search_scope: Remote QuickGO ontology search; exact query perialgal; default resultsPerPage25;
    returned numberOfHits0 with no results. Actual request 2026-11-03T03:59:28.506175Z.
    This single lexical query is not exhaustive ontology absence; ignored local files
    are inapplicable and no local absence is inferred.
- evidence_id: plaque-perialgal-prep-boudreau2025-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1091/mbc.E24-12-0571
  locator: Single DOI result bibliographic identity; freshly retrieved exact source
    bytes at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/perialgal-prep-boudreau2025-meta.source
  accessed_at: '2026-11-03T03:59:28.739172Z'
  support: supports
  summary: The exact DOI resolves to Boudreau et al.2025, PMID39937680/PMC12005096,
    on S.pyriformis cell biology and genome.
  snapshot_sha256: 351704f7987c7877759dd5b82d44e273b01097c0e967ba2d3b92b58d888f324f
- evidence_id: plaque-perialgal-prep-boudreau2025-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC12005096.1/PMC12005096.1.xml
  locator: JATS Cell anatomy, Host/symbiont phylogeny, Microtubule baskets Results;
    surface-association Discussion; culture, microscopy, expansion, algal-isolation
    and phylogeny Methods; F3 legend and permissions; fresh source snapshot in /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/perialgal-prep-boudreau2025-jats.source
  accessed_at: '2026-11-03T03:59:28.756936Z'
  support: supports
  summary: Primary text and anti-beta-tubulin T0198 Methods support an irregular host
    cortical mesh around algal vacuoles in S. pyriformis, distinct from longitudinal
    Km fibers. The algae can be cultured outside the host. Surface retention and physiological
    benefits remain proposed; centrifugation is not selective mesh disruption. Copyright
    explicitly grants CC BY4.0, while the licence element is a trademark notice. The
    Results reference to Figure3C is an internal source typo; native figure/legend
    show A/B and the record correctly uses B.
  snapshot_sha256: d574ab2e03930539e6b30484f81004a46dfbf06dbfe787fb6cc9e883fd419794
- evidence_id: plaque-perialgal-prep-figure3
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC12005096.1/mbc-36-ar44-g003.jpg
  locator: Entire native Figure3 JPEG visually inspected; MD5 verified against version1
    package; fresh source snapshot in /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/perialgal-prep-figure3.source
  accessed_at: '2026-11-03T03:59:28.767226Z'
  support: supports
  summary: PanelA shows chlorophyll and beta-tubulin signals; panelB contains six
    inward optical sections through expanded meshwork. No regular per-alga cage or
    native dimensions are inferred. Image MD5257bc762a3388119a79e88aed462a9fa matches
    the native package.
  snapshot_sha256: d58c093705a97648409f47c19bd5d6cfd819b9c93d724eeda3210c14aa8563fb
- evidence_id: plaque-perialgal-prep-paper-pdf
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC12005096.1/PMC12005096.1.pdf
  locator: PDF page6 caption and exact official file MD5; separate native figure visually
    inspected; fresh source snapshot in /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/perialgal-prep-paper-pdf.source
  accessed_at: '2026-11-03T03:59:28.861931Z'
  support: supports
  summary: Page6 is Figure3 with chlorophyll/beta-tubulin panelA and six-section expanded-mesh
    panelB. PDF MD5f078ec2af01c2da13f957c95b61640d5 matches version1 metadata. Expanded-image
    distances are not promoted to native measurements.
  snapshot_sha256: 815a397a1a03146c11d70c648df6d9acdb8b2471622f2e28627d18e111d17487
- evidence_id: plaque-perialgal-prep-boudreau2025-package
  kind: database
  reference: https://pmc-oa-opendata.s3.amazonaws.com/metadata/PMC12005096.1.json
  locator: Version, DOI/PMID, is_retracted, licence_code and exact XML/PDF/Figure3
    MD5 comparisons; fresh source snapshot in /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/perialgal-prep-boudreau2025-package.source
  accessed_at: '2026-11-03T03:59:28.956449Z'
  support: supports
  summary: Version1 metadata is not marked retracted and retains license_code:null.
    Fresh XML, PDF and Figure3 MD5 values match the package. The explicit JATS CC
    BY4.0 copyright grant and structured-code incompleteness are preserved; link-only
    use and hosting guard remain appropriate.
  snapshot_sha256: 66e981d2ab672ea0dc47fe7c2b8a51a743100a2554f0e46e3da0b9e921e9a63d
- evidence_id: plaque-stalk-asai1998-publisher-abstract
  kind: primary_source
  reference: https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1550-7408.1998.tb05066.x
  locator: Publisher browser-open extraction lines109-111 abstract and lines303-307/346
    issue citation; exact serialized tool response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/asai-browser.json
  accessed_at: '2026-11-03T04:01:19.862Z'
  snapshot_sha256: 80ef4a7dd017eebbe8ca9f451f30ed316af350bd806b1fa014184408daf6c884
  support: supports
  summary: 'Asai et al.1998 volume45 pp33-39: chemical modification suggests a non-calcium-binding
    contributor in addition to spasmins; it does not resolve the native scaffold.
    Main Methods were not available. Initial curl403 and browser timeout were not
    used as source evidence; a subsequent publisher browser-open returned the abstract.
    First-online2007 differs from the1998 issue date.'
- evidence_id: plaque-adapter-datasets-current
  kind: search
  reference: https://imodulondb.org/api/datasets
  locator: 'Entire native /api/datasets response: all20 returned organism entries
    and their dataset keys; fresh response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/adapter-datasets-current.source'
  accessed_at: '2026-11-03T04:02:02.453928Z'
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  support: context_only
  summary: No returned organism/dataset key covers Vorticella, Carchesium, Zoothamnium
    or Stentor. Thus organism-specific iModulonDB gene/module queries are not applicable
    for these three ciliate records. This is coverage information, not evidence that
    a protein, localization or phenotype is absent.
  search_scope: Remote iModulonDB /api/datasets, unfiltered GET, all20 organism objects
    in the returned array and every dataset key inspected; response has no pagination
    marker. Actual request 2026-11-03T04:02:02.453928Z. No claim about hidden/private/future
    datasets or biological absence. Ignored local files are not relevant to this remote
    catalogue. The earlier same-session cached catalogue was reread, then this independent
    fresh request obtained identical bytes.
- evidence_id: plaque-record-stalk_spasmoneme
  kind: record_content
  reference: data/structures/cytoskeleton/stalk_spasmoneme.yaml
  locator: Entire current maintained YAML at67d0dd66fe04472c58f4ad9c8b860df18a9f5f8a;
    identity, components, taxa, evidence, graph, discussions and image metadata
  accessed_at: '2026-11-03T04:03:35.803720Z'
  snapshot_sha256: a3de4646f57551323b08c225176359cf3737eff71eaab9da598131d646920bdb
  support: context_only
  summary: Read-only current-input assessment; stale original input differs only in
    three added causal-edge descriptions plus a curation event; descriptions independently
    reassessed against actual primary text.
- evidence_id: plaque-record-stentor_km_fiber
  kind: record_content
  reference: data/structures/cytoskeleton/stentor_km_fiber.yaml
  locator: Entire current maintained YAML at67d0dd66fe04472c58f4ad9c8b860df18a9f5f8a;
    identity, components, taxa, evidence, graph, discussions and image metadata
  accessed_at: '2026-11-03T04:03:35.803720Z'
  snapshot_sha256: 66b91b45477653bcafdf1f875b9820681ea1bdeddf36f9d37f74fabe9408cae6
  support: context_only
  summary: Read-only current-input assessment; maintained target bytes match the original
    frozen review input. No scientific fields or status changed.
- evidence_id: plaque-record-stentor_perialgal_microtubule_meshwork
  kind: record_content
  reference: data/structures/cytoskeleton/stentor_perialgal_microtubule_meshwork.yaml
  locator: Entire current maintained YAML at67d0dd66fe04472c58f4ad9c8b860df18a9f5f8a;
    identity, components, taxa, evidence, graph, discussions and image metadata
  accessed_at: '2026-11-03T04:03:35.803720Z'
  snapshot_sha256: 3a0c8634cf4fca1f7d9253d399b2f6d343d806cd6e3b81e5d92ebf6ff9ab7daf
  support: context_only
  summary: Read-only current-input assessment; maintained target bytes match the original
    frozen review input. No scientific fields or status changed.
- evidence_id: plaque-original-bundles-native-validation
  kind: validation
  reference: scripts/record_review.py validate / render --content; git show historical
    source inputs
  locator: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-plaque/original-validation.json;
    three assigned originals only
  accessed_at: '2026-11-03T03:59:39.553719Z'
  snapshot_sha256: 98add183458075607dfe7613e385f633a83f4de53625ed453725fa0c673b365d
  support: supports
  summary: All three original bundles validate with exit0, render exact Markdown bytes
    and have all declared historical frozen input SHA256 values matching their source
    commit. These successful historical checks do not attest current content for the
    stale spasmoneme record.
- evidence_id: micro-current-stellate-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0043232,GO:0035869,GO:0097539,GO:0120269
  locator: 'Four active terms: GO:0043232,0035869,0097539,0120269; definitions, names
    and status'
  accessed_at: '2026-11-03T03:58:33.536403Z'
  snapshot_sha256: 5c767264c75f85114d3e0539b27c36c95a01a43c295176037550a6ec482872f9
  support: supports
  summary: Broad intracellular membraneless parent and enclosing ciliary transition
    zone are distinct from external transition fibers and the trypanosome centrin
    arm. Native ontology does not itself contain the local record edge.
- evidence_id: micro-current-stellate-agent-go-stellate-search
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=stellate&limit=100
  locator: All24 returned names/definitions; page1/1, resultsPerPage100
  accessed_at: '2026-11-03T03:58:33.536665Z'
  snapshot_sha256: 4bd1242b6bdc81cc66d288960dfd0bf85d49542d7d93c2bb382c483542650e8b
  support: partial
  summary: No exact Chlamydomonas luminal-fiber identity appeared among the24 literal-query
    results; these concern stellate cells and related processes. This is not universal
    ontology absence.
  search_scope: QuickGO ontology/go/search query=stellate, limit=100, accessed2026-11-03UTC
    at the timestamp supplied; all24 returned terms inspected, pageInfo.current=1,total=1.
    Restricted to this literal text query, not all synonyms/ontologies or local corpus
    records.
- evidence_id: micro-current-stellate-agent-tax-3055
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3055
  locator: ENA taxId/scientificName/rank/otherNames
  accessed_at: '2026-11-03T03:58:33.536752Z'
  snapshot_sha256: e3861fe6706cefe2e079e15c0178a65e95efaad3890f548f25e721553eaa93a0
  support: supports
  summary: 3055 is Chlamydomonas reinhardtii; the species-level authority does not
    identify assay isolate416 or a culture-collection accession.
- evidence_id: micro-current-stellate-agent-P05434
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P05434.json
  locator: UniProt entryType, recommended/alternative names, organism, genes absence
    and EMBL cross-references
  accessed_at: '2026-11-03T03:58:33.536809Z'
  snapshot_sha256: dbc691271995563a38fd19896c92adfb1902cb79dde0e8d777c45effc2a05c79
  support: supports
  summary: Reviewed P05434 is Caltractin/Centrin, taxon3055, without a primary gene
    symbol. X12634/CAA31163.1 and X57973/CAA41039.1 establish sequence-source links.
    Identity alone does not confer fiber-specific localization.
- evidence_id: micro-current-stellate-agent-IPR050145
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050145/
  locator: Native InterPro metadata.name/type and description including LLM flags
  accessed_at: '2026-11-03T03:58:33.536858Z'
  snapshot_sha256: 386371fb67a7de41d9f9a6ded2bbb77530d9a27411b46349d2ac050d45832910
  support: context_only
  summary: Centrin/CML-like includes caltractin, obelin and plant CML proteins; it
    is broader than stellate-fiber centrins. The description is flagged LLM-generated/checked
    by the authority; used only for authority family scope, not primary localization
    evidence.
- evidence_id: micro-current-stellate-agent-IPR050230
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050230/
  locator: Native InterPro metadata.name/type and description including LLM flags
  accessed_at: '2026-11-03T03:58:33.536894Z'
  snapshot_sha256: 71caaab83a460a49f29a4c4bf6932354c77b07e1c9455f9c7521355e22c60bc0
  support: context_only
  summary: Calmodulin/Myosin light chain/Troponin C-like spans several distinct calcium-binding
    protein classes and is broader still. The description is flagged LLM-generated/checked
    by the authority; used only for authority family scope, not primary localization
    evidence.
- evidence_id: micro-current-stellate-agent-sanders1994-pdf
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2119956.1/PMC2119956.1.pdf
  locator: Printed pp795–797 introduction/Methods and contraction Results; antibody/mutant
    Results and Discussion pp800–803; Figure2 PDFpage3 and TableI PDFpage6 visually
    inspected
  accessed_at: '2026-11-03T03:58:34.174665Z'
  snapshot_sha256: a02b1259b713fc5928326c28e305e2b393a9f29ebc0bed89cbcfb8498a0833f6
  support: supports
  summary: Detergent-extracted137c and vfl2 isolate416 experiments support calcium-triggered
    fiber condensation and inward doublet displacement. TableI retains residual excision
    after EDTA, anti-centrin antibodies and vfl2 perturbation. The authors propose
    shear/assay conditions to explain earlier disagreement; that interpretation does
    not resolve universal necessity. Figure2 panelsA–C versusD–F and0.2µm scale agree
    with the record; separate DIC Figure1 shares the page.
- evidence_id: micro-current-stellate-agent-sanders1994-jats
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2119956.1/PMC2119956.1.xml
  locator: Article identifiers and permissions/license_ref
  accessed_at: '2026-11-03T03:58:34.175642Z'
  snapshot_sha256: b5b36e9e47f5d3581b29315791e40e214e85850fa3f1e8967e1eec0c66120a1e
  support: supports
  summary: Native PMC2119956.1 JATS supplies the article identity and CC BY-NC-SA4.0
    licence. Its abstract/reference-format content does not replace the separately
    read primary PDF.
- evidence_id: micro-current-stellate-agent-taillon1992-pdf
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2289752.1/PMC2289752.1.pdf
  locator: Abstract; pCaBP4/sequence-source and strain Methods pp1614–1615; mutation/revertant
    Results; class2 passages; TableII text and Discussion pp1622–1623
  accessed_at: '2026-11-03T03:58:34.187750Z'
  snapshot_sha256: dc06c2312e33688b48b18e0f93665b811d0a010055b929bcbea17cf62ec6e349
  support: supports
  summary: vfl2 centrin E101K and intragenic revertants link the protein to multiple
    centrin assemblies. Class2 Met/Ile revertants retain stellate fibers while distal
    striated fibers differ. vfl2-220 in this paper is not conflated with the separate1994
    isolate416. The pCaBP4/sequence bridge supports protein identity; no selective
    stellate ablation, complete inventory or universal essentiality is demonstrated.
- evidence_id: micro-current-jarvik1991-abstract
  kind: primary_source
  reference: https://www.researchgate.net/publication/258112144_The_role_of_the_flagellar_transition_region_inferences_from_the_analysis_of_a_Chlamydomonas_mutant_with_defective_transition_region_structures
  locator: ResearchGate publisher preview primary abstract lines26–29 and summary47–107;
    browser artifact only
  accessed_at: '2026-11-03T04:00:00.058Z'
  snapshot_sha256: b00b0af9bec13860033d798c587bbc0dcef300006d615eeddeb7a08f91d30ece
  support: partial
  summary: The primary abstract reports effective vfl2 autotomy without organized
    stellate fibers or detectable axoneme narrowing; proposed central-pair exclusion
    concerns the broader transition-region structures. This supports retaining the
    conflict, not a fiber-only gating mechanism. Direct publisher access failed; no
    complete article body, Methods or figures were freshly read.
- evidence_id: micro-current-stellate-agent-jarvik1991-browser
  kind: validation
  reference: https://journals.biologists.com/jcs/article/99/4/731/60763/The-role-of-the-flagellar-transition-region
  locator: Native publisher retrieval HTTP403 challenge/error body
  accessed_at: '2026-11-03T03:58:34.223146Z'
  snapshot_sha256: d5ed44e986bb717752629dfbb05644af21e59036e87966a26cdd8d1796f73874
  support: context_only
  summary: Direct publisher source was inaccessible in this request. A separate browser
    request timed out; readable primary abstract was obtained through publisher preview
    on ResearchGate. This response is not scientific full text.
- evidence_id: micro-current-stellate-agent-lohret1998-html
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC25341/?report=xml
  locator: PMC25341 actual HTML; abstract, Introduction paras17–18, purified-katanin/antibody
    Methods paras27–31 and relevant Results/Discussion
  accessed_at: '2026-11-03T03:58:34.250311Z'
  snapshot_sha256: f2e1870b21cf92562a5b2711d1bf5d773612375a1f8d50a4b93b34310fead38f
  support: supports
  summary: Purified sea-urchin katanin and anti-human-p60 perturbations concern Chlamydomonas
    axonemes/whole flagellar-basal-body complexes. The centrin-necessity counterclaim
    partly cites explicitly unpublished observations. The work does not assign katanin,
    FA1 or FA2 to an isolated stellate-fiber inventory.
- evidence_id: micro-current-stellate-agent-diener2015-html
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC4318714/?report=xml
  locator: PMC4318714 actual HTML; isolation/ultrastructure paragraphs18,21–26 and
    proteomics paragraphs28,31–32
  accessed_at: '2026-11-03T03:58:34.334715Z'
  snapshot_sha256: 5492f182dcb5155cd73e96b19a1bc33818c8927a4683df5142e225d00e4f8005
  support: supports
  summary: Isolated resorption-derived transition-zone material retains central cylinders
    after stellate fibers become unidentifiable. Whole-zone proteomics, centrin enrichment
    and severing proteins are not evidence that all identified proteins are constituents
    of intact stellate fibers.
- evidence_id: micro-current-stellate-agent-hoek2022-pdf
  kind: primary_source
  reference: https://push-zb.helmholtz-munich.de/deliver.php?id=34775
  locator: Institutional Science PDF page1 architecture Results and page2 Figure1
    caption
  accessed_at: '2026-11-03T03:58:34.371895Z'
  snapshot_sha256: 81730b4bf40849cb88917728dd26fc3a8936742fd109e4e46a700ee1e0615eba
  support: supports
  summary: Native cryo-ET resolves a six-start stellate helix,49.2nm pitch and A3
    attachment with about8.1nm repeat, distinct from Y-links and the distal sleeve.
    Architecture supports the attachment edge, not an exact molecular inventory or
    a resolved excision mechanism. Figure pixels, IFT-focused remainder and supplements
    were not inspected.
- evidence_id: micro-current-spool-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005622,GO:0015630
  locator: GO:0005622 and GO:0015630 full active term definitions
  accessed_at: '2026-11-03T03:58:34.679258Z'
  snapshot_sha256: 61990a834a77032f8a035de5072e94eafec06af437a1f1a8e9f0745584e75a9c
  support: supports
  summary: Broad intracellular anatomical parent and microtubule-cytoskeleton parthood
    are appropriate for a local spool identity, without asserting an exact spool GO
    term.
- evidence_id: micro-current-spool-agent-go-spool-search
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=spool&limit=100
  locator: Entire zero-hit response; resultsPerPage100,total0
  accessed_at: '2026-11-03T03:58:34.740758Z'
  snapshot_sha256: f3a7dae9b1e9335291e3940cdf0e5f8dadf9335da7b9547710606b5106c63f86
  support: partial
  summary: Literal spool query returns no GO hits; local identity remains justified
    by primary morphology, not universal absence.
  search_scope: QuickGO ontology/go/search query=spool, limit=100, accessed2026-11-03UTC
    at supplied timestamp; numberOfHits=0,pageInfo.total=0. No synonym expansion,
    other ontologies or fresh repository duplicate search was performed.
- evidence_id: micro-current-spool-agent-tax-241424
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/241424
  locator: ENA taxId/scientificName/rank/lineage
  accessed_at: '2026-11-03T03:58:34.810070Z'
  snapshot_sha256: d76ca812802b6c62059c2c10174a4b1f48a461391293dfd7bfd082eaeb86b665
  support: supports
  summary: 241424 denotes Takayama helix in Kareniaceae; this verifies identity, not
    prevalence.
- evidence_id: micro-current-spool-agent-IPR000217
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000217/
  locator: InterPro accession, family type/name, description and subtype context
  accessed_at: '2026-11-03T03:58:35.238660Z'
  snapshot_sha256: ddbf902c6495d576d69c82c85daf1bdf2bc9fea5894925a4efcd87dc45ea3170
  support: supports
  summary: IPR000217 is the generic Tubulin family. It suits the broad component while
    neither identifying exact Takayama genes nor asserting every family subtype occurs
    in the spool.
- evidence_id: micro-current-spool-agent-mikus2025-paper-pdf
  kind: primary_source
  reference: https://www.roscoff-culture-collection.org/sites/default/files/rcc-papers/Mikus%20et%20al.%20-%202025%20-%20Charting%20the%20landscape%20of%20cytoskeletal%20diversity%20in%20microbial%20eukaryotes.pdf
  locator: Institutional article-in-press PDF reused from actual2026-11-03T03:20:54.167915Z
    fetch, newly read for Figure2 caption/Results pp4–5; Kareniaceae survey pp9–11;
    key-resource species entries; fixation/U-ExM/microscopy/Image analysis Methods
    e6–e8; CC BY statement
  accessed_at: '2026-11-03T03:20:54.167915Z'
  snapshot_sha256: 117e1e97412645a193cfbb87664031ead725759d02dddce02be84ad7e3a14d16
  support: supports
  summary: Fixed-cell expansion immunofluorescence supports perinuclear/posterior
    tubulin-positive spools in Takayama and the sampled Kareniaceae. Apparent extension
    from a microtubule, desmose association and proposed physiological roles have
    distinct support levels. Figure2 scale statements conflict with Image analysis
    Methods; the record properly avoids deriving native dimensions. This new reading
    uses retained earlier bytes/time, not a fresh PDF download.
- evidence_id: micro-current-spool-agent-table-s1
  kind: primary_source
  reference: https://www.dudinlab.com/s/Table-S1.xlsx
  locator: Workbook sheet relationships resolved natively; List of Species header/row46;
    Dataset Annotation header row3 and rows1375,1376,1384
  accessed_at: '2026-11-03T03:58:35.298417Z'
  snapshot_sha256: bfeb51750c59a50005f2cc7d7efe28582b164d938ca76f7c795f0b26113e61fe
  support: supports
  summary: RCC10719 is Takayama helix. Row1384 directly identifies P22-120, the exact
    s00 volume, E7Ab, interphase, one species in the gel and Spools=Yes. Rows1375–1376
    are mixed-gel specimens and do not make RCC3511 a synonym or establish that other
    species has spools. Annotations are not independent cell-count/prevalence estimates.
- evidence_id: micro-current-spool-agent-mikus2025-crossref
  kind: database
  reference: https://api.crossref.org/works/10.1016/j.cell.2025.09.027
  locator: message.DOI/title and complete licence array, content-version=vor
  accessed_at: '2026-11-03T03:58:35.338680Z'
  snapshot_sha256: b65fcb4cb9a86a6eb0a78a0b4c7d31cf2e6bd995411774fa2e3d263d051b0730
  support: supports
  summary: Version-of-record licence is CC BY4.0, distinct from the text/data-mining
    agreements. It agrees with the article’s explicit CC BY statement.
- evidence_id: micro-current-spool-agent-project
  kind: database
  reference: https://raw.githubusercontent.com/Dey-Lab-Team/culture-collections/2dc2f3dbae8fefe60cea3a2499a1a5f50fe4c98d/data/project.json
  locator: Complete pinned data/project.json at2dc2f3dbae8fefe60cea3a2499a1a5f50fe4c98d
  accessed_at: '2026-11-03T03:58:35.409324Z'
  snapshot_sha256: 9b526fc72e078fdbd886c2be0c9e9b400e2f7e4aec3d0004bb53b4f1dc521fe6
  support: supports
  summary: The project uses datasets=[volumes], defaultDataset=volumes, specVersion0.3.0.
- evidence_id: micro-current-spool-agent-volumes-dataset
  kind: database
  reference: https://raw.githubusercontent.com/Dey-Lab-Team/culture-collections/2dc2f3dbae8fefe60cea3a2499a1a5f50fe4c98d/data/volumes/dataset.json
  locator: Top-level keys and exact rcc10719_pfa_dna-tub-nhs_20230802_od_s00 view
    plus ch0/ch1/ch2 sources
  accessed_at: '2026-11-03T03:58:35.423710Z'
  snapshot_sha256: 36d2f61fa50ac9ccd2a42050b50eb72ed8dabc09fc1df6fb05bbf12be5a5e2a3
  support: supports
  summary: The exact annotated volume has DNA/tubulin/NHS channels and belongs to
    spools. Legacy single_volumes substrings inside storage URLs do not override the
    project default. Other archive sources and raw volumes were not reanalyzed.
- evidence_id: micro-current-spool-agent-categories
  kind: database
  reference: https://raw.githubusercontent.com/Dey-Lab-Team/culture-collections/2dc2f3dbae8fefe60cea3a2499a1a5f50fe4c98d/culture_collections/notebooks/categories.csv
  locator: Tab-delimited header; exact s00 row; RCC10719-containing rows and annotation
    value classes among1767 parsed rows
  accessed_at: '2026-11-03T03:58:35.604686Z'
  snapshot_sha256: 29b0881b8a8a3e86fce753293ebbe3c94f3c27d4ac14804fed796296487b067d
  support: supports
  summary: Pinned annotation confirms the exact volume’s interphase/Yes/NE fields
    and Yes/No/Maybe/blank spool labels across RCC10719 samples. Those labels do not
    establish universal occurrence or independent biological replication.
- evidence_id: micro-current-spool-agent-github-readme
  kind: database
  reference: https://raw.githubusercontent.com/Dey-Lab-Team/culture-collections/2dc2f3dbae8fefe60cea3a2499a1a5f50fe4c98d/README.md
  locator: Pinned README archive/access paragraph
  accessed_at: '2026-11-03T03:58:35.745196Z'
  snapshot_sha256: 08257d90a998d18bd78e91066a8894d8e84b51dec08bf2a589dce1e3473252b7
  support: context_only
  summary: The project links BioImage Archive S-BIAD2095. This verifies provenance
    only; raw volumes were not reanalyzed.
- evidence_id: micro-current-spool-agent-publisher-figure2
  kind: primary_source
  reference: https://ars.els-cdn.com/content/image/1-s2.0-S0092867425011274-gr2_lrg.jpg
  locator: Fresh complete publisher Figure2 JPEG; compared with frozen tracked file
    and visually inspected all panels
  accessed_at: '2026-11-03T03:58:35.855915Z'
  snapshot_sha256: e979bacf2fad45501744aa5dbc2fd75c0fc2ab2b5e6a6be32be77aad0b1f9046
  support: supports
  summary: Publisher bytes and frozen tracked image are identical SHA256e979bacf2fad45501744aa5dbc2fd75c0fc2ab2b5e6a6be32be77aad0b1f9046.
    PanelsD–E show Takayama spools;D tubulin magenta/DNA blue;E closeups and diameter
    summaries. Other panels are other structures/taxa, not additional spool specimens.
    Caption preserves scale ambiguity.
- evidence_id: micro-current-crossbridge-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097595,GO:0097594,GO:0097597
  locator: Active GO:0097595,0097594,0097597 definitions/synonyms; ventral-disc children
    relations
  accessed_at: '2026-11-03T03:58:35.864313Z'
  snapshot_sha256: 10c107f8bf97e296423507c9b4fb6c16e1675974af8897652a382a3d35506abe
  support: supports
  summary: Exact crossbridge and dorsal-microribbon identities and part_of relations
    are supported. The microribbon size/tubulin-exclusion definition is authority-backed,
    not a new biochemical measurement. Broader ventral-disc contractile-protein assertions
    are not imported into these targets.
- evidence_id: micro-current-crossbridge-agent-tax-5741
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5741
  locator: ENA taxId/scientificName/rank/otherNames
  accessed_at: '2026-11-03T03:58:35.949174Z'
  snapshot_sha256: 1dcdc380972a71a0a24c80755d8bbacdcb0b6d9988bb5fb1e05ba43f50580dd3
  support: supports
  summary: Giardia duodenalis species5741 explicitly includes G.intestinalis and G.lamblia
    synonyms; the target labels remain valid.
- evidence_id: micro-current-crossbridge-agent-epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1371/journal.pone.0043783%22
  locator: Exact DOI result for10.1371/journal.pone.0043783
  accessed_at: '2026-11-03T03:58:35.953965Z'
  snapshot_sha256: e57aa4be2b4da0e8c2fd4082e5f08d1cd50239a932a5c403924d3a2618bac654
  support: supports
  summary: Resolves Schwartz, Heumann, Dawson and Hoenger2012, PMID22984443/PMC3439489.
    Citation identity only.
- evidence_id: micro-current-crossbridge-agent-schwartz2012-jats
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3439489/fullTextXML
  locator: Fresh native JATS Results s2b/s2h; Discussion s3d/s3e; Methods s5a/s5d/s5e/s5f;
    associated main-text captions
  accessed_at: '2026-11-03T03:58:35.967249Z'
  snapshot_sha256: df4cb13cb3b12c8be3df05f99f8b97cc44951dd61a2c00a168ed8e9aedb6f9d8
  support: supports
  summary: Primary tomography supports trilaminar dorsal microribbons with lateral
    crossbridges, distinct from the within-complex B bridge. WBC6 trophozoites and
    extracted flattened cytoskeletons, with five selected tomograms/four discs, bound
    interpretation. Crossbridge flexibility does not directly demonstrate active contraction
    or identify constituent proteins. Named giardin/SALP composition in Discussion
    is attributed earlier evidence, separately checked in Hagen2011.
- evidence_id: micro-current-microribbon-agent-go-mt
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097593
  locator: GO:0097593 active definition and synonyms
  accessed_at: '2026-11-03T03:58:36.277914Z'
  snapshot_sha256: 94ee5330346eb3c53b84ce94781809d3ba24d3999f3524cd2e763b8cce98fccd
  support: supports
  summary: The spiral ventral-disc microtubule array supports near-perpendicular dorsal
    microribbons and is distinct from the microribbons themselves.
- evidence_id: micro-current-microribbon-agent-tax-184922
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/184922
  locator: ENA taxon184922 scientificName/rank/synonyms
  accessed_at: '2026-11-03T03:58:36.399359Z'
  snapshot_sha256: 70613bfc0044d2eb3541655411f959c563106c7b5df29e88f6606f7d51b84928
  support: supports
  summary: ATCC50803 is a strain-level taxon. WBC6 identity is supplied by the primary
    Methods and native protein names, not inferred from the species taxon alone.
- evidence_id: micro-current-microribbon-agent-epmc-hagen2011
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1371/journal.pntd.0001442%22
  locator: Exact DOI10.1371/journal.pntd.0001442 result
  accessed_at: '2026-11-03T03:58:36.458190Z'
  snapshot_sha256: 4d697d3aa6da2c815796d4c04e3eb0574812dc2e23b494b4470d9af94946f1e4
  support: supports
  summary: Resolves Hagen2011 primary ventral-disc localization study, PMID22206034/PMC3243723.
- evidence_id: micro-current-microribbon-agent-hagen2011-jats
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3243723/fullTextXML
  locator: Fresh native JATS Methods s2a/s2d/s2g; Results s3b; Discussion s4a; Table1
    rowsGL50803_4812/86676/4410
  accessed_at: '2026-11-03T03:58:36.566295Z'
  snapshot_sha256: 4764e6ef8d323277737b63dbb374bbdb8011ff87153ed54603d74bd616b5e608
  support: supports
  summary: Primary GFP and anti-GFP immunogold/negative-stain observations support
    beta-/delta-giardin and SALP-1 microribbon association. Structural sufficiency,
    timing, sheet-specific arrangement and universal turnover remain interpretations
    or unresolved. Table1 assigns PF06705 to beta/delta while SALP-1 has no domain
    entry; no negative homology inference follows.
- evidence_id: micro-current-microribbon-agent-ipr-008374
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR008374/
  locator: Native metadata accession/name/type/description/integrated field
  accessed_at: '2026-11-03T03:58:36.595846Z'
  snapshot_sha256: 0d9ac5ff8dc1886c6b48d47528177aed2ce34400e0393f1129495cc68046fceb
  support: context_only
  summary: IPR008374 is the SF-assemblin/beta-giardin family; supports candidate mappings
    for beta/delta but the full named cohort needs scope reconciliation.
- evidence_id: micro-current-microribbon-agent-ipr-038835
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR038835/
  locator: Native metadata accession/name/type/description/integrated field
  accessed_at: '2026-11-03T03:58:36.875005Z'
  snapshot_sha256: 826d6306c2371f26731295978338f9f1f38acf7939b105c569aee13049c16b99
  support: context_only
  summary: IPR038835 is the Giardin subunit beta-like family; this does not automatically
    identify SALP-1 or every microribbon constituent.
- evidence_id: micro-current-microribbon-agent-pfam-06705
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF06705/
  locator: Native metadata accession/name/type/description/integrated field
  accessed_at: '2026-11-03T03:58:37.099384Z'
  snapshot_sha256: ff810d44cdf739fb2e1866f57bbdb9b5e7d0f2124f9fa8b128b58d5761ac42fb
  support: context_only
  summary: PF06705 is SF-assemblin/beta giardin integrated into IPR008374; its green-algal
    mitotic descriptions are not Giardia-specific evidence.
- evidence_id: micro-current-microribbon-agent-uniprot-loci
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=taxonomy_id%3A5741%20AND%20%28gene%3AGL50803_004812%20OR%20gene%3AGL50803_4812%20OR%20gene%3AGL50803_086676%20OR%20gene%3AGL50803_86676%20OR%20gene%3AGL50803_004410%20OR%20gene%3AGL50803_4410%29&format=json&size=100
  locator: Two returned reviewed-status/name/taxon/gene/cross-reference objects; X-Total-Results2;
    no continuation
  accessed_at: '2026-11-03T03:58:37.185445Z'
  snapshot_sha256: 37bbdc9a2c8c8ce4eeffd475820627ed023a7a655ecc774b78078e38c6c5f5be
  support: context_only
  summary: Unreviewed E2RTU7 beta-giardin and E2RUA1 SALP-1 have WBC6 taxon184922
    and expected locus aliases. Beta carries IPR008374/IPR038835/PF06705; the returned
    SALP-1 entry has none of those cross-references. That annotation gap does not
    disprove literature homology or establish universal family absence.
  search_scope: UniProtKB query taxonomy_id:5741 AND (gene:GL50803_004812 OR gene:GL50803_4812
    OR gene:GL50803_086676 OR gene:GL50803_86676 OR gene:GL50803_004410 OR gene:GL50803_4410),
    format=json,size100, accessed2026-11-03UTC. Entire2-result response inspected;
    X-Total-Results2,no Link continuation. Restricted to these locus spellings; does
    not include delta current GL50803_0086676 spelling or constitute an exhaustive
    family search.
- evidence_id: micro-current-microribbon-agent-uniprot-delta
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=taxonomy_id%3A5741%20AND%20protein_name%3A%22Delta-giardin%22&format=json&size=100
  locator: Entire one-result response and family cross-references; X-Total-Results1;
    no continuation
  accessed_at: '2026-11-03T03:58:37.207553Z'
  snapshot_sha256: 8907090f91024b4c024550b2d3b96d48b00fd71c7de7b21bdadf79787dd0bd11
  support: context_only
  summary: Unreviewed A0A644FAT1 identifies WBC6 delta-giardin, locusGL50803_0086676,
    with IPR008374/PF06705 annotations. Native annotation supports identity/family
    candidates, not direct localization.
  search_scope: UniProtKB query taxonomy_id:5741 AND protein_name:"Delta-giardin",format=json,size100,
    accessed2026-11-03UTC. All1 returned result inspected; X-Total-Results1,no Link
    continuation. Name/taxon-bounded query only, not complete organism proteome or
    homology search.
- evidence_id: micro-current-current-adapter-catalogue
  kind: search
  reference: https://imodulondb.org/api/datasets
  locator: All20 organism entries/28 dataset names, cached raw catalogue independently
    reread
  accessed_at: '2026-11-03T03:20:54.290965Z'
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  support: context_only
  summary: No catalogue organism/dataset matches Chlamydomonas, Takayama or Giardia.
    Named proteins justify applicability discovery for stellate, spool and microribbon;
    no target-specific search is available. Crossbridge has no named molecular target.
    This is dataset coverage, never biological negative evidence.
  search_scope: iModulonDB /api/datasets unfiltered complete endpoint, actual fetch2026-11-03T03:20:54.290965Z
    reused and reread for PR2349. No requested cap/pagination; all20 organism entries
    and28 dataset keys inspected for Chlamydomonas reinhardtii, Takayama helix and
    Giardia duodenalis/intestinalis/lamblia coverage. No match; no module/gene search
    performed. Root separately owns historical runner-availability evidence.
- evidence_id: micro-record-stellate
  kind: record_content
  reference: data/structures/cytoskeleton/transition_zone_stellate_fiber_system.yaml
  locator: Complete target YAML
  accessed_at: '2026-11-03T04:05:32.191708Z'
  snapshot_sha256: ee5fc36bcda7810c550cfef29146f6b124f79703e6b73832b6f005583884ba36
  support: supports
  summary: Current bytes match the original frozen SHA256 ee5fc36bcda7810c550cfef29146f6b124f79703e6b73832b6f005583884ba36.
    No stale target or record edit.
- evidence_id: micro-prior-stellate
  kind: prior_review
  reference: reviews/structured/20261021T084040Z-transition-zone-stellate-fiber-system-audit/review.yaml
  locator: Original frozen inputs/checks/evidence/assessments/findings/verdict/limits
  accessed_at: '2026-11-03T04:05:32.191708Z'
  snapshot_sha256: a78760668e36c695e3c4dc541dbdf6b68481a51b5c823770d6c58ca9c5fc4cc3
  support: supports
  summary: Original pass_with_limitations has no scientific findings. Native validation/render
    and frozen-target comparison pass; old global receipts remain historical.
- evidence_id: micro-record-spool
  kind: record_content
  reference: data/structures/cytoskeleton/tubulin_spool.yaml
  locator: Complete target YAML
  accessed_at: '2026-11-03T04:05:32.191708Z'
  snapshot_sha256: 1180c5c0b3a5c67f58a23b99913f7b78202beb8cf3e01c40ca5aac9c56dcf072
  support: supports
  summary: Current bytes match the original frozen SHA256 1180c5c0b3a5c67f58a23b99913f7b78202beb8cf3e01c40ca5aac9c56dcf072.
    No stale target or record edit.
- evidence_id: micro-prior-spool
  kind: prior_review
  reference: reviews/structured/20261021T084041Z-tubulin-spool-audit/review.yaml
  locator: Original frozen inputs/checks/evidence/assessments/findings/verdict/limits
  accessed_at: '2026-11-03T04:05:32.191708Z'
  snapshot_sha256: f1898ed88d87a03c14971c2cfaf87a1fcb9a02355bfa1d0ff58f8d3bf37a584e
  support: supports
  summary: Original pass_with_limitations has no scientific findings. Native validation/render
    and frozen-target comparison pass; old global receipts remain historical.
- evidence_id: micro-record-crossbridge
  kind: record_content
  reference: data/structures/cytoskeleton/ventral_disc_crossbridge.yaml
  locator: Complete target YAML
  accessed_at: '2026-11-03T04:05:32.191708Z'
  snapshot_sha256: bb35ddad7c8b15916d19fa6e5ad334ca3476221330372020fdf4adc8565db67b
  support: supports
  summary: Current bytes match the original frozen SHA256 bb35ddad7c8b15916d19fa6e5ad334ca3476221330372020fdf4adc8565db67b.
    No stale target or record edit.
- evidence_id: micro-prior-crossbridge
  kind: prior_review
  reference: reviews/structured/20261021T084041Z-ventral-disc-crossbridge-audit/review.yaml
  locator: Original frozen inputs/checks/evidence/assessments/findings/verdict/limits
  accessed_at: '2026-11-03T04:05:32.191708Z'
  snapshot_sha256: 76882ddb708ad4406c93480743ab7aa73be8c6f45b71323237bae8909f02257b
  support: supports
  summary: Original pass_with_limitations has no scientific findings. Native validation/render
    and frozen-target comparison pass; old global receipts remain historical.
- evidence_id: micro-record-microribbon
  kind: record_content
  reference: data/structures/cytoskeleton/ventral_disc_dorsal_microribbon.yaml
  locator: Complete target YAML
  accessed_at: '2026-11-03T04:05:32.191708Z'
  snapshot_sha256: 6bcdbfaaf84c4b6152147340dcbb6f5958d6dc6aca2288e034c3f2c357819425
  support: supports
  summary: Current bytes match the original frozen SHA256 6bcdbfaaf84c4b6152147340dcbb6f5958d6dc6aca2288e034c3f2c357819425.
    No stale target or record edit.
- evidence_id: micro-prior-microribbon
  kind: prior_review
  reference: reviews/structured/20261021T084041Z-ventral-disc-dorsal-microribbon-audit/review.yaml
  locator: Original frozen inputs/checks/evidence/assessments/findings/verdict/limits
  accessed_at: '2026-11-03T04:05:32.191708Z'
  snapshot_sha256: efee9bcedc3932f1894b0f018a4930a45538f1a4b287e8a9ed54a55b062fe982
  support: supports
  summary: Original pass_with_limitations has no scientific findings. Native validation/render
    and frozen-target comparison pass; old global receipts remain historical.
- evidence_id: micro-original-native-checks
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/adversary-microtubule/original-checks.json
  locator: Four native validate/render commands and frozen-target comparison
  accessed_at: '2026-11-03T03:58:32.822865Z'
  snapshot_sha256: bed13a8b3c1c27cce2745a294d487ed7bec1974d8f9a5cf6e41d80cab99ebb97
  support: supports
  summary: All4 validate with exit0 and render Markdown byte-exactly; all4 target
    hashes match. This is not a fresh whole-corpus QC claim.
- evidence_id: micro-tracked-spool-image
  kind: record_content
  reference: data/images/cytoskeleton/tubulin_spool/mikus_2025_figure2.jpg
  locator: Complete frozen tracked Figure2 image; visually inspected after parent
    added to input manifest
  accessed_at: '2026-11-03T04:05:32.191708Z'
  snapshot_sha256: e979bacf2fad45501744aa5dbc2fd75c0fc2ab2b5e6a6be32be77aad0b1f9046
  support: supports
  summary: Frozen tracked image matches declared/publisher SHA256 and panel-specific
    caption. Image was explicitly frozen before this assessment.
- evidence_id: micro-adapter-policy
  kind: record_content
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: structured-source-cross-checks block
  accessed_at: '2026-11-03T04:05:32.191708Z'
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
  support: supports
  summary: Named genes/proteins/accessions trigger consideration; runner/coverage
    checks precede module queries. Lack of an expression-module mechanism is not the
    stated exemption; absence of matching covered organisms supports downstream non-applicability.
- evidence_id: septin-s2349-split-rings-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032176,GO:0032156,GO:0005856,GO:0032177,GO:0032153,GO:0005940,GO:0032173
  locator: 'Exact seven-term QuickGO responses: names, definitions, synonyms, parent
    children relations and referenced PMIDs.'
  accessed_at: '2026-11-03T03:57:28.169497Z'
  support: supports
  summary: Authority supports paired split rings, parent and parthood distinctions,
    and cautiously phrased cytokinesis compartment function.
  snapshot_sha256: 063edda467c6a954eb7089a93e2953af863c6a9f8237d9d5eab53a1bbb7e07ea
- evidence_id: septin-s2349-split-rings-agent-family
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016491/
  locator: Native IPR016491 metadata.type, metadata.name, description and hierarchy.
  accessed_at: '2026-11-03T03:57:28.169834Z'
  support: supports
  summary: IPR016491 is the generic Septin family, matching the existing generic component
    independently of unresolved localized paralogue composition.
  snapshot_sha256: 5797c626d192b641ed5b4b2231e729f9f179bfd6bb18f911689fa08253688c4a
- evidence_id: septin-s2349-split-rings-agent-douglas-pmc
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1214204/
  locator: 'PMC1214204 secondary review: introductory budding cycle, ring-splitting
    and boundary-domain paragraphs; not a newly inspected primary experiment.'
  accessed_at: '2026-11-03T03:57:28.169916Z'
  support: supports
  summary: Secondary review summarizes collar splitting and cytokinesis confinement;
    the record retains the cautious thought-to-trap claim. Native schema has no secondary_source
    evidence kind, so authority here identifies inspected secondary literature, not
    primary evidence.
  snapshot_sha256: 35e80f8bd23920f2ea3125910c0927f1708af8bdf30599565f56d5df31c36ad8
- evidence_id: septin-s2349-split-rings-agent-versele-pmc
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1761124/?pdf=render
  locator: 'PMC1761124 secondary review: septin functions, collar scission and Figure
    3 discussion.'
  accessed_at: '2026-11-03T03:57:28.169972Z'
  support: supports
  summary: Secondary review supports bounded split-ring morphology and compartmentalization
    wording; no source-wide primary experiment audit claimed. authority kind denotes
    inspected secondary literature, not primary evidence.
  snapshot_sha256: 92c0d2dfff63cc4d0d3e90fda505fb1917484c5609796998796466173869c6ac
- evidence_id: septin-s2349-split-rings-agent-douglas-metadata
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1128/EC.4.9.1503-1512.2005&format=json&resultType=core
  locator: Complete returned result list for the exact URL query.
  accessed_at: '2026-11-03T03:57:28.170016Z'
  support: supports
  summary: Exact bounded identity/disambiguation lookup; results do not establish
    exhaustive absence from literature or biology.
  snapshot_sha256: 4237e9967b6dd7017a6ae6bb69002cb751bc337d98cc2f5d166b86d53bf2fc96
  search_scope: Database Europe PMC; exact request https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1128/EC.4.9.1503-1512.2005&format=json&resultType=core;
    query ['DOI:10.1128/EC.4.9.1503-1512.2005']; executed 2026-11-03T03:57:28.170016Z;
    only returned response inspected; no publication-date restriction or broad literature
    search, and no inferred universal absence.
- evidence_id: septin-s2349-tacc-prep-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0007020,GO:0051315,GO:0061863,GO:0070850,GO:0090307,GO:0140535
  locator: Native issuing-authority response, exact accession/term or taxon and returned
    name/type/status.
  accessed_at: '2026-11-03T03:57:28.170054Z'
  support: supports
  summary: Checked native identity, label, taxon, accession crossreferences and the
    bounded family/domain scope relevant to the current record.
  snapshot_sha256: cdf00b1e3e72e625e9dc0785a818930f660ce068dbf53a7503f22da8524fb27b
- evidence_id: septin-s2349-tacc-prep-tax-4896
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4896
  locator: Native issuing-authority response, exact accession/term or taxon and returned
    name/type/status.
  accessed_at: '2026-11-03T03:57:28.631768Z'
  support: supports
  summary: Checked native identity, label, taxon, accession crossreferences and the
    bounded family/domain scope relevant to the current record.
  snapshot_sha256: 42c5b7d3d99341137803612d6404cd3884e2d06ec8a740b1ad38163c678f6721
- evidence_id: septin-s2349-tacc-prep-tax-284812
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/284812
  locator: Native issuing-authority response, exact accession/term or taxon and returned
    name/type/status.
  accessed_at: '2026-11-03T03:57:28.662425Z'
  support: supports
  summary: Checked native identity, label, taxon, accession crossreferences and the
    bounded family/domain scope relevant to the current record.
  snapshot_sha256: 948c040cabf6c036dff451c7b6eac22605d0ed5d60a74f471e4431e63f82f721
- evidence_id: septin-s2349-tacc-prep-IPR045110
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR045110/
  locator: Native issuing-authority response, exact accession/term or taxon and returned
    name/type/status.
  accessed_at: '2026-11-03T03:57:28.784885Z'
  support: supports
  summary: Checked native identity, label, taxon, accession crossreferences and the
    bounded family/domain scope relevant to the current record.
  snapshot_sha256: e0ba89dab0b5c5383525985f74a81b6a5862a318c457d70882d37afa9b94017e
- evidence_id: septin-s2349-tacc-prep-IPR024312
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR024312/
  locator: Native issuing-authority response, exact accession/term or taxon and returned
    name/type/status.
  accessed_at: '2026-11-03T03:57:28.809954Z'
  support: supports
  summary: Checked native identity, label, taxon, accession crossreferences and the
    bounded family/domain scope relevant to the current record.
  snapshot_sha256: e605d3b7216ab19f4229b3206ce52b2e41631b14fd70741a8c821d50d642fb4e
- evidence_id: septin-s2349-tacc-prep-matches-Q9URY2
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/Q9URY2/
  locator: Native issuing-authority response, exact accession/term or taxon and returned
    name/type/status.
  accessed_at: '2026-11-03T03:57:28.810034Z'
  support: supports
  summary: Checked native identity, label, taxon, accession crossreferences and the
    bounded family/domain scope relevant to the current record.
  snapshot_sha256: 5c2231b4f665a8293114eb467b243f6ee50b206aed10efaaf73d8af44cae0748
- evidence_id: septin-s2349-tacc-prep-Q9URY2
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q9URY2.json
  locator: Native issuing-authority response, exact accession/term or taxon and returned
    name/type/status.
  accessed_at: '2026-11-03T03:57:28.855329Z'
  support: supports
  summary: Checked native identity, label, taxon, accession crossreferences and the
    bounded family/domain scope relevant to the current record.
  snapshot_sha256: 69a22093a5968e9a614a5170718632ab935b0628867cab263df68ad3bb240fe7
- evidence_id: septin-s2349-tacc-prep-O94534
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/O94534.json
  locator: Native issuing-authority response, exact accession/term or taxon and returned
    name/type/status.
  accessed_at: '2026-11-03T03:57:29.299199Z'
  support: supports
  summary: Checked native identity, label, taxon, accession crossreferences and the
    bounded family/domain scope relevant to the current record.
  snapshot_sha256: 257ba28d9d0e8203582177682405142bf2445317baad602e9f31a1171e13a722
- evidence_id: septin-s2349-tacc-prep-Q10198
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q10198.json
  locator: Native issuing-authority response, exact accession/term or taxon and returned
    name/type/status.
  accessed_at: '2026-11-03T03:57:29.321237Z'
  support: supports
  summary: Checked native identity, label, taxon, accession crossreferences and the
    bounded family/domain scope relevant to the current record.
  snapshot_sha256: 74dfc8ac8dfe5d6bb01ea8ef213bcfab5de60eaad94002910b2641df21ba3234
- evidence_id: septin-s2349-tacc-prep-query-alp7
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3Aalp7%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete returned result list for the exact URL query.
  accessed_at: '2026-11-03T03:57:29.420569Z'
  support: supports
  summary: Exact bounded identity/disambiguation lookup; results do not establish
    exhaustive absence from literature or biology.
  snapshot_sha256: 85a9ab6b3fa150223334efcf5eb54f2eb1f93a74afb8b0337782971b6a8741b0
  search_scope: Database UniProtKB; exact request https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3Aalp7%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29;
    query ['(gene_exact:alp7) AND (organism_id:284812) AND (reviewed:true)']; executed
    2026-11-03T03:57:29.420569Z; only returned response inspected; no publication-date
    restriction or broad literature search, and no inferred universal absence.
- evidence_id: septin-s2349-tacc-prep-query-mia1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3Amia1%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete returned result list for the exact URL query.
  accessed_at: '2026-11-03T03:57:29.473869Z'
  support: supports
  summary: Exact bounded identity/disambiguation lookup; results do not establish
    exhaustive absence from literature or biology.
  snapshot_sha256: 85a9ab6b3fa150223334efcf5eb54f2eb1f93a74afb8b0337782971b6a8741b0
  search_scope: Database UniProtKB; exact request https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3Amia1%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29;
    query ['(gene_exact:mia1) AND (organism_id:284812) AND (reviewed:true)']; executed
    2026-11-03T03:57:29.473869Z; only returned response inspected; no publication-date
    restriction or broad literature search, and no inferred universal absence.
- evidence_id: septin-s2349-tacc-prep-query-alp14
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3Aalp14%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete returned result list for the exact URL query.
  accessed_at: '2026-11-03T03:57:29.648961Z'
  support: supports
  summary: Exact bounded identity/disambiguation lookup; results do not establish
    exhaustive absence from literature or biology.
  snapshot_sha256: e23245d00978cff6a713e7e7a13dca05e5f49f13fe2ad5e7af6deb290cb48622
  search_scope: Database UniProtKB; exact request https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3Aalp14%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29;
    query ['(gene_exact:alp14) AND (organism_id:284812) AND (reviewed:true)']; executed
    2026-11-03T03:57:29.648961Z; only returned response inspected; no publication-date
    restriction or broad literature search, and no inferred universal absence.
- evidence_id: septin-s2349-tacc-prep-query-mtc1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3Amtc1%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete returned result list for the exact URL query.
  accessed_at: '2026-11-03T03:57:29.723569Z'
  support: supports
  summary: Exact bounded identity/disambiguation lookup; results do not establish
    exhaustive absence from literature or biology.
  snapshot_sha256: e23245d00978cff6a713e7e7a13dca05e5f49f13fe2ad5e7af6deb290cb48622
  search_scope: Database UniProtKB; exact request https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3Amtc1%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29;
    query ['(gene_exact:mtc1) AND (organism_id:284812) AND (reviewed:true)']; executed
    2026-11-03T03:57:29.723569Z; only returned response inspected; no publication-date
    restriction or broad literature search, and no inferred universal absence.
- evidence_id: septin-s2349-tacc-prep-hussmann2016-meta
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1038/srep20653
  locator: Complete returned result list for the exact URL query.
  accessed_at: '2026-11-03T03:57:30.029197Z'
  support: supports
  summary: Exact bounded identity/disambiguation lookup; results do not establish
    exhaustive absence from literature or biology.
  snapshot_sha256: 7fc23c662f4ad58c8057e22abf951687ebaeca2f262c19aa8a10ccbc296e1314
  search_scope: Database Europe PMC; exact request https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1038/srep20653;
    query ['DOI:10.1038/srep20653']; executed 2026-11-03T03:57:30.029197Z; only returned
    response inspected; no publication-date restriction or broad literature search,
    and no inferred universal absence.
- evidence_id: septin-s2349-tacc-prep-hussmann2016-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4749977.1/PMC4749977.1.xml
  locator: 'PMC4749977 Results: in vivo deletions; purified Alp7/Alp14 binding; long
    MTs; tip-tracking; Figure 7 legend. Methods: tubulin purification and MT dynamics;
    Discussion occupancy subsection.'
  accessed_at: '2026-11-03T03:57:30.104735Z'
  support: supports
  summary: Primary experiments show reduced elongation in alp7 deletion under these
    conditions, co-sedimentation of purified partners, no detectable Alp7-alone tubulin
    binding, and Alp7-enhanced Alp14 tip occupancy. Figure 7 is mixed-species purified
    TIRF material, not a whole-cell image or native universal stoichiometry.
  snapshot_sha256: 12a9df0a6cd70f2a6c93d068946c8bbe569417d91d70a49bc53da9564473c5b4
- evidence_id: septin-s2349-tacc-prep-nucleation2018-meta
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.cub.2018.04.008
  locator: Complete returned result list for the exact URL query.
  accessed_at: '2026-11-03T03:57:30.516960Z'
  support: supports
  summary: Exact bounded identity/disambiguation lookup; results do not establish
    exhaustive absence from literature or biology.
  snapshot_sha256: 0db1163e6786ca3c290707e471b43b6066087f405621c1c9d0bd30d517803579
  search_scope: Database Europe PMC; exact request https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.cub.2018.04.008;
    query ['DOI:10.1016/j.cub.2018.04.008']; executed 2026-11-03T03:57:30.516960Z;
    only returned response inspected; no publication-date restriction or broad literature
    search, and no inferred universal absence.
- evidence_id: septin-s2349-tacc-prep-nucleation2018-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC7263743.1/PMC7263743.1.xml
  locator: PMC7263743 sections S6, S8, S9, S13 and S14, with embedded Figure 6/7 experimental
    descriptions.
  accessed_at: '2026-11-03T03:57:30.591594Z'
  support: supports
  summary: Primary 2018 observations distinguish Alp7-dependent Alp14 MTOC loading/nucleation
    from retained plus-end tracking and normal elongation. The stated conflict with
    2016 is real. Alp14-GBP/Mto1-bonsai rescue is engineered and partial.
  snapshot_sha256: 5c6000e8b847fcdedb2b6d328d7a87e026432a1cb816daf6c5461f8cde76c9aa
- evidence_id: septin-s2349-tacc-prep-attachment2013-meta
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1091/mbc.E12-11-0817
  locator: Complete returned result list for the exact URL query.
  accessed_at: '2026-11-03T03:57:31.004154Z'
  support: supports
  summary: Exact bounded identity/disambiguation lookup; results do not establish
    exhaustive absence from literature or biology.
  snapshot_sha256: 7ff604c0c39886b038f3c5f758d4547372a8f363b55592038efd2f74cc6fe955
  search_scope: Database Europe PMC; exact request https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1091/mbc.E12-11-0817;
    query ['DOI:10.1091/mbc.E12-11-0817']; executed 2026-11-03T03:57:31.004154Z; only
    returned response inspected; no publication-date restriction or broad literature
    search, and no inferred universal absence.
- evidence_id: septin-s2349-tacc-prep-attachment2013-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3623634.1/PMC3623634.1.xml
  locator: PMC3623634 Results on Ndc80-NH12/F420S, Alp7/14 localization, GST/coIP
    and loop peptide arrays, forced Nuf2-Alp7C rescue; corresponding biochemical Methods.
  accessed_at: '2026-11-03T03:57:31.163181Z'
  support: supports
  summary: Primary evidence supports reduced rather than abolished kinetochore recruitment,
    retained SPB context, peptide-defined direct association and forced-targeting
    rescue. It does not map a complete full-length interface or make Ndc80 a complex
    constituent.
  snapshot_sha256: a175c7cb3756c9d5d46dde7bdac3d4badc4639f5a9e5cd40820da74b997e9c18
- evidence_id: septin-s2349-tacc-prep-transport2014-meta
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1091/mbc.E13-11-0679
  locator: Complete returned result list for the exact URL query.
  accessed_at: '2026-11-03T03:57:31.260744Z'
  support: supports
  summary: Exact bounded identity/disambiguation lookup; results do not establish
    exhaustive absence from literature or biology.
  snapshot_sha256: 81d21165b80bfb410cd1f437ffb0c94e7d07b330c8ca447308df323b4a9f4bd0
  search_scope: Database Europe PMC; exact request https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1091/mbc.E13-11-0679;
    query ['DOI:10.1091/mbc.E13-11-0679']; executed 2026-11-03T03:57:31.260744Z; only
    returned response inspected; no publication-date restriction or broad literature
    search, and no inferred universal absence.
- evidence_id: septin-s2349-tacc-prep-transport2014-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4072571.1/PMC4072571.1.xml
  locator: PMC4072571 Results L615, Alp7 deletion/5A kinase and localization experiments,
    Cut15 two-hybrid; Discussion CDK transport; kinase and two-hybrid Methods.
  accessed_at: '2026-11-03T03:57:31.406072Z'
  support: supports
  summary: L615A preserves Alp7 association while affecting export; Alp7 5A retains
    delayed import, reduces mitotic accumulation and has NLS-suppressible growth defects.
    Cut15 fragment interaction in budding-yeast two-hybrid supports a model, not measured
    native importin affinity or complete spindle rescue.
  snapshot_sha256: 7de093d110f396a921dcb99f1aae9c5280a88e1498a67496caa0c7f595c20398
- evidence_id: septin-s2349-tacc-prep-dis1_2019-meta
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.3390/ijms20205108
  locator: Complete returned result list for the exact URL query.
  accessed_at: '2026-11-03T03:57:31.615631Z'
  support: supports
  summary: Exact bounded identity/disambiguation lookup; results do not establish
    exhaustive absence from literature or biology.
  snapshot_sha256: a02668b811df46dd4c571f7e99afb718b981ad4d234ecb8fa486d70b2674760e
  search_scope: Database Europe PMC; exact request https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.3390/ijms20205108;
    query ['DOI:10.3390/ijms20205108']; executed 2026-11-03T03:57:31.615631Z; only
    returned response inspected; no publication-date restriction or broad literature
    search, and no inferred universal absence.
- evidence_id: septin-s2349-tacc-prep-dis1_2019-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC6834199.1/PMC6834199.1.xml
  locator: PMC6834199 Results 2.6, Discussion 3.1, Methods 4.3.
  accessed_at: '2026-11-03T03:57:31.641243Z'
  support: supports
  summary: Reciprocal enforced targeting at endogenous expression fails to exchange
    Alp14 and Dis1 functions, whereas earlier overexpression rescue is explicitly
    retained. This does not exclude every conditional compensation or make Dis1 a
    TACC constituent.
  snapshot_sha256: 308dd12b0a92c836d2337214dae7cede96eeab5b2fb45c2e866a6f03e46db690
- evidence_id: septin-s2349-tacc-prep-figure7
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4749977.1/srep20653-f7.jpg
  locator: Native source JPEG visually inspected via identical frozen local image;
    all panels A–D; bytes match the repository image exactly.
  accessed_at: '2026-11-03T03:57:31.880221Z'
  support: supports
  summary: Mixed S. pombe/brain-tubulin TIRF schematic, kymographs and growth histograms;
    2 µm and 1 minute scales; CC BY 4.0 checked in primary JATS.
  snapshot_sha256: 435c851418d002e2c49b2ccc3d39eac1f3bf5b30e5881c56f40c8876d81ef752
- evidence_id: septin-s2349-telo-prep-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000930,GO:0000931,GO:0005815,GO:0008275,GO:0034993,GO:0045141,GO:0051418
  locator: Native issuing-authority response, exact accession/term or taxon and returned
    name/type/status.
  accessed_at: '2026-11-03T03:57:31.939824Z'
  support: supports
  summary: Checked native identity, label, taxon, accession crossreferences and the
    bounded family/domain scope relevant to the current record.
  snapshot_sha256: 7b670c986f89d679995093f792fdaed38fad31db155cc58ec6543ec3726a70fb
- evidence_id: septin-s2349-telo-prep-IPR045119
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR045119/
  locator: Native issuing-authority response, exact accession/term or taxon and returned
    name/type/status.
  accessed_at: '2026-11-03T03:57:32.081755Z'
  support: supports
  summary: Checked native identity, label, taxon, accession crossreferences and the
    bounded family/domain scope relevant to the current record.
  snapshot_sha256: ebf2e470f10e591fe8475c39ac5142261438a51a9bba2571c0282d80a75d359e
- evidence_id: septin-s2349-telo-prep-IPR005334
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005334/
  locator: Native issuing-authority response, exact accession/term or taxon and returned
    name/type/status.
  accessed_at: '2026-11-03T03:57:32.116817Z'
  support: supports
  summary: Checked native identity, label, taxon, accession crossreferences and the
    bounded family/domain scope relevant to the current record.
  snapshot_sha256: 4b3892b04229e7d051837ff2dbe657906eae401d5545f4775f47dcd41a349eae
- evidence_id: septin-s2349-telo-prep-IPR030268
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR030268/
  locator: Native issuing-authority response, exact accession/term or taxon and returned
    name/type/status.
  accessed_at: '2026-11-03T03:57:32.244529Z'
  support: supports
  summary: Checked native identity, label, taxon, accession crossreferences and the
    bounded family/domain scope relevant to the current record.
  snapshot_sha256: dbb32dfc7393668c283edb648be9f69f26c050f891a4dad1e4af114825cd9850
- evidence_id: septin-s2349-telo-prep-IPR026983
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR026983/
  locator: Native issuing-authority response, exact accession/term or taxon and returned
    name/type/status.
  accessed_at: '2026-11-03T03:57:32.351739Z'
  support: supports
  summary: Checked native identity, label, taxon, accession crossreferences and the
    bounded family/domain scope relevant to the current record.
  snapshot_sha256: d857fa548bcd6eaa39e9d4297a84a47517b89e0e7fa84d0d4ff67fb5e330531e
- evidence_id: septin-s2349-telo-prep-matches-P87245
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P87245/
  locator: Native issuing-authority response, exact accession/term or taxon and returned
    name/type/status.
  accessed_at: '2026-11-03T03:57:32.492159Z'
  support: supports
  summary: Checked native identity, label, taxon, accession crossreferences and the
    bounded family/domain scope relevant to the current record.
  snapshot_sha256: fc2c3fa0cf4b315fd6bf85587320a1115d3db926b89531da051f9fd2c0f947b9
- evidence_id: septin-s2349-telo-prep-matches-O43087
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/O43087/
  locator: Native issuing-authority response, exact accession/term or taxon and returned
    name/type/status.
  accessed_at: '2026-11-03T03:57:32.531083Z'
  support: supports
  summary: Checked native identity, label, taxon, accession crossreferences and the
    bounded family/domain scope relevant to the current record.
  snapshot_sha256: 5a819c44321d8b1cc574c47d4a36edc32c92388cf4b7169d3c67ba2a1fbb87e3
- evidence_id: septin-s2349-telo-prep-matches-O94488
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/O94488/
  locator: Native issuing-authority response, exact accession/term or taxon and returned
    name/type/status.
  accessed_at: '2026-11-03T03:57:32.691017Z'
  support: supports
  summary: Checked native identity, label, taxon, accession crossreferences and the
    bounded family/domain scope relevant to the current record.
  snapshot_sha256: 475c2fa2c23696d5933a5f8278316b1d74bb8b282f9d954daa3b084e382dd7a9
- evidence_id: septin-s2349-telo-prep-matches-O13290
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/O13290/
  locator: Native issuing-authority response, exact accession/term or taxon and returned
    name/type/status.
  accessed_at: '2026-11-03T04:02:21.917162Z'
  support: supports
  summary: Checked native identity, label, taxon, accession crossreferences and the
    bounded family/domain scope relevant to the current record.
  snapshot_sha256: 8c4430fa06610326b682c69c7a7e98ff7a023355a89367bd91d4f2a598390e00
- evidence_id: septin-s2349-telo-prep-matches-O42667
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/O42667/
  locator: Native issuing-authority response, exact accession/term or taxon and returned
    name/type/status.
  accessed_at: '2026-11-03T04:02:25.621127Z'
  support: supports
  summary: Checked native identity, label, taxon, accession crossreferences and the
    bounded family/domain scope relevant to the current record.
  snapshot_sha256: 8fcdf617449beaa84533afde61bd15d1184f9ffc98d441d8bbd1c1fec22b0bdf
- evidence_id: septin-s2349-telo-prep-Q09825
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q09825.json
  locator: Native issuing-authority response, exact accession/term or taxon and returned
    name/type/status.
  accessed_at: '2026-11-03T03:57:32.956356Z'
  support: supports
  summary: Checked native identity, label, taxon, accession crossreferences and the
    bounded family/domain scope relevant to the current record.
  snapshot_sha256: af97b71167c7297318086add00ac1143a9ab78a2f714035f76ff4c31bf77993d
- evidence_id: septin-s2349-telo-prep-P87245
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P87245.json
  locator: Native issuing-authority response, exact accession/term or taxon and returned
    name/type/status.
  accessed_at: '2026-11-03T03:57:33.312449Z'
  support: supports
  summary: Checked native identity, label, taxon, accession crossreferences and the
    bounded family/domain scope relevant to the current record.
  snapshot_sha256: 84aa928d02abba093e6be0c791d5d9f775268e8701d7955ab7f7d7cbb36eb234
- evidence_id: septin-s2349-telo-prep-O43087
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/O43087.json
  locator: Native issuing-authority response, exact accession/term or taxon and returned
    name/type/status.
  accessed_at: '2026-11-03T03:57:33.365487Z'
  support: supports
  summary: Checked native identity, label, taxon, accession crossreferences and the
    bounded family/domain scope relevant to the current record.
  snapshot_sha256: 67d61fb0efd9d0200f7a6f6b30de9e9c2f96d8f0c61e3b61f6ab87999959a280
- evidence_id: septin-s2349-telo-prep-O94488
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/O94488.json
  locator: Native issuing-authority response, exact accession/term or taxon and returned
    name/type/status.
  accessed_at: '2026-11-03T03:57:33.390137Z'
  support: supports
  summary: Checked native identity, label, taxon, accession crossreferences and the
    bounded family/domain scope relevant to the current record.
  snapshot_sha256: 4903509b256bf5164ea7e5b80970bbb89056a71a4ea4a257e9feb8adcaf0e46b
- evidence_id: septin-s2349-telo-prep-Q9Y705
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q9Y705.json
  locator: Native issuing-authority response, exact accession/term or taxon and returned
    name/type/status.
  accessed_at: '2026-11-03T03:57:33.435469Z'
  support: supports
  summary: Checked native identity, label, taxon, accession crossreferences and the
    bounded family/domain scope relevant to the current record.
  snapshot_sha256: 1735b88bbff6bce84e252460f2f8e64bb72fbe3901bd81b9f1db63cba4d23682
- evidence_id: septin-s2349-telo-prep-Q9UTS6
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q9UTS6.json
  locator: Native issuing-authority response, exact accession/term or taxon and returned
    name/type/status.
  accessed_at: '2026-11-03T03:57:33.627097Z'
  support: supports
  summary: Checked native identity, label, taxon, accession crossreferences and the
    bounded family/domain scope relevant to the current record.
  snapshot_sha256: 82b57e907d15a5005acb377ac82a69302fe87dde3ecb479fad5c1b54cdd2ec5d
- evidence_id: septin-s2349-telo-prep-O13290
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/O13290.json
  locator: Native issuing-authority response, exact accession/term or taxon and returned
    name/type/status.
  accessed_at: '2026-11-03T03:57:33.674215Z'
  support: supports
  summary: Checked native identity, label, taxon, accession crossreferences and the
    bounded family/domain scope relevant to the current record.
  snapshot_sha256: 2888913ce8549c578a30bf4d77ce9dc77d3030e314862cd9b1b413f084831acd
- evidence_id: septin-s2349-telo-prep-O42667
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/O42667.json
  locator: Native issuing-authority response, exact accession/term or taxon and returned
    name/type/status.
  accessed_at: '2026-11-03T03:57:33.938349Z'
  support: supports
  summary: Checked native identity, label, taxon, accession crossreferences and the
    bounded family/domain scope relevant to the current record.
  snapshot_sha256: 257dc92e69587f9cd3e2909025585c2d3593ee46a795b9812dbcd313ebd2825f
- evidence_id: septin-s2349-telo-prep-query-mto1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3Amto1%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete returned result list for the exact URL query.
  accessed_at: '2026-11-03T03:57:34.089507Z'
  support: supports
  summary: Exact bounded identity/disambiguation lookup; results do not establish
    exhaustive absence from literature or biology.
  snapshot_sha256: 643ebc085c29c9b26ed5c571165c79adee2044c5a82cd66dc7e51a67879dc039
  search_scope: Database UniProtKB; exact request https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3Amto1%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29;
    query ['(gene_exact:mto1) AND (organism_id:284812) AND (reviewed:true)']; executed
    2026-11-03T03:57:34.089507Z; only returned response inspected; no publication-date
    restriction or broad literature search, and no inferred universal absence.
- evidence_id: septin-s2349-telo-prep-query-ssm4
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3Assm4%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete returned result list for the exact URL query.
  accessed_at: '2026-11-03T03:57:34.113645Z'
  support: supports
  summary: Exact bounded identity/disambiguation lookup; results do not establish
    exhaustive absence from literature or biology.
  snapshot_sha256: 0a8531c67b922b863beaa0de0b2d011c13809e5cbbdb2b06b9fe89ddbb708842
  search_scope: Database UniProtKB; exact request https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3Assm4%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29;
    query ['(gene_exact:ssm4) AND (organism_id:284812) AND (reviewed:true)']; executed
    2026-11-03T03:57:34.113645Z; only returned response inspected; no publication-date
    restriction or broad literature search, and no inferred universal absence.
- evidence_id: septin-s2349-telo-prep-yoshida2013-meta
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1083/jcb.201207168
  locator: Complete returned result list for the exact URL query.
  accessed_at: '2026-11-03T03:57:35.084654Z'
  support: supports
  summary: Exact bounded identity/disambiguation lookup; results do not establish
    exhaustive absence from literature or biology.
  snapshot_sha256: 168d1ee730cbd6b30d2b318eea329361ec7233caf231e800988afa15d62aacac
  search_scope: Database Europe PMC; exact request https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1083/jcb.201207168;
    query ['DOI:10.1083/jcb.201207168']; executed 2026-11-03T03:57:35.084654Z; only
    returned response inspected; no publication-date restriction or broad literature
    search, and no inferred universal absence.
- evidence_id: septin-s2349-telo-prep-jimenez2025-meta
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1038/s41467-025-56049-9
  locator: Complete returned result list for the exact URL query.
  accessed_at: '2026-11-03T03:57:35.204016Z'
  support: supports
  summary: Exact bounded identity/disambiguation lookup; results do not establish
    exhaustive absence from literature or biology.
  snapshot_sha256: 325789797eecd5b9eeed48935df51e17787ef0c6e6f55cbec5ce4ffebe708d6f
  search_scope: Database Europe PMC; exact request https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1038/s41467-025-56049-9;
    query ['DOI:10.1038/s41467-025-56049-9']; executed 2026-11-03T03:57:35.204016Z;
    only returned response inspected; no publication-date restriction or broad literature
    search, and no inferred universal absence.
- evidence_id: septin-s2349-telo-prep-yoshida2013-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3575533.1/PMC3575533.1.xml
  locator: PMC3575533 main Results and figure legends 1–5, Discussion motor model,
    meiosis induction and microscopy Methods; Figure 5 Dlc1/Dhc1 paragraph and caption
    explicitly inspected.
  accessed_at: '2026-11-03T03:57:35.712030Z'
  support: supports
  summary: Primary imaging and perturbation support an SPB-distinct, telomere-associated
    meiotic MTOC. Kms1/Mto1 and Dlc1 support Alp4 recruitment; Dhc1 is dispensable
    narrowly for that recruitment, not efficient clustering. Figure 5C is a proposed
    motor model. Gamma-TuC is a multiprotein structure with Alp4 as reporter, supporting
    the current STRUCTURE node.
  snapshot_sha256: 0f228ac437c8af6f3d9edc0552d70b3b15a670714423cd3d32e094ec0cc4e274
- evidence_id: septin-s2349-telo-agent-yoshida2013-supp
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3575533.1/supp_jcb.201207168_JCB_201207168_sm.pdf
  locator: 'Native PDF text: Figures S1–S3 captions, six video legends and Table S1
    relevant Figure 2 strains. PDF served as text/html but identified by %PDF magic;
    figures S2 pixels and videos not independently viewed.'
  accessed_at: '2026-11-03T03:57:35.846013Z'
  support: supports
  summary: Captions support cytoplasmic regrowth, preconjugation Sad1 sites, independent
    Dlc1/Dhc1 localization and the multiple engineered experimental stocks; no identification
    of all experiments with the UniProt reference strain.
  snapshot_sha256: d6e171a6afc45dfb5ac1e5cd7bed606d23fcd92bc34a69893ab1fae8a00d9291
- evidence_id: septin-s2349-telo-prep-jimenez2025-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC11747273.1/PMC11747273.1.xml
  locator: PMC11747273 sections Sec8, Sec9, Sec12, Sec14 and Sec17, Figure 6 caption;
    Sec10 context also inspected.
  accessed_at: '2026-11-03T03:57:36.166044Z'
  support: supports
  summary: Ectopic Bqt1/Bqt2 in Rabl-deficient haploid mitotic cells recruits Sad1/Kms1/Mto1/Alp4,
    without detected Dhc1 or complete bouquet. Kms1 deletion suppresses some growth/migration
    phenotypes. This is engineered partial assembly, not a normal constitutive mitotic
    telocentrosome.
  snapshot_sha256: 1e0470a799e49976e35584be8e8449af77c2e85fd1e11576a460227cd526e4ed
- evidence_id: septin-s2349-telo-agent-jimenez2025-supp
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC11747273.1/41467_2025_56049_MOESM1_ESM.pdf
  locator: 'Native supplemental PDF text: Supplementary Figure 6 legend only, Rap1
    localization and abundance context.'
  accessed_at: '2026-11-03T03:57:36.209591Z'
  support: supports
  summary: Supplemental legend reports Rap1 localization/intensity assays and total-protein
    western blot replicates. This is caption-level supplementary coverage, not a complete
    supplement or underlying-image audit.
  snapshot_sha256: adb86b58423a5e65ffdefe09b06fb17aba9d4acaa7f2c549197c9fd7e0c09221
- evidence_id: septin-s2349-telo-prep-figure2
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3575533.1/JCB_201207168_Fig2.jpg
  locator: Native source JPEG visually inspected, panels A–E and 2 µm scale bars.
  accessed_at: '2026-11-03T03:57:36.366499Z'
  support: supports
  summary: Time-course fluorescence, haploid-meiosis schematic and DMSO/MBC plots
    correspond to record description; native SHA256 matches record link-only image,
    CC BY-NC-SA 3.0 checked in primary JATS.
  snapshot_sha256: 8d3114614d32513832bc7e63ff308e1f8a4475724af6bf9c88e80f04a2dfb1ad
- evidence_id: septin-s2349-current-adapter-catalogue
  kind: authority
  reference: https://imodulondb.org/api/datasets
  locator: Official iModulonDB API /api/datasets complete response, all 20 organism
    entries and 28 dataset keys.
  accessed_at: '2026-11-03T03:57:36.948354Z'
  support: supports
  summary: Inspected catalogue covers bacterial/archaeal organisms and no Schizosaccharomyces
    pombe or other eukaryotic target here. Target gene/module searches therefore do
    not apply. Catalogue absence is not evidence against biological structures; no
    new local runner invocation claimed.
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: septin-s2349-record-split_septin_rings
  kind: record_content
  reference: data/structures/cytoskeleton/split_septin_rings.yaml
  locator: Complete current YAML at head 67d0dd66fe04472c58f4ad9c8b860df18a9f5f8a.
  accessed_at: '2026-11-03T04:04:51.926479Z'
  support: supports
  summary: Whole maintained record inspected read-only, including components, graph
    edges, evidence, image/provenance, discussions and change history.
  snapshot_sha256: 580abb6f00c144e871e1fded7fbb2dca8584ecf0d47a599f646558642c3027ff
- evidence_id: septin-s2349-record-tacc_tog_complex
  kind: record_content
  reference: data/structures/cytoskeleton/tacc_tog_complex.yaml
  locator: Complete current YAML at head 67d0dd66fe04472c58f4ad9c8b860df18a9f5f8a.
  accessed_at: '2026-11-03T04:04:51.926479Z'
  support: supports
  summary: Whole maintained record inspected read-only, including components, graph
    edges, evidence, image/provenance, discussions and change history.
  snapshot_sha256: 7d2c57864f3928f8ab9bbc0d7e702aa142292ae00252b385f40a5a8dbcd7b787
- evidence_id: septin-s2349-record-telocentrosome
  kind: record_content
  reference: data/structures/cytoskeleton/telocentrosome.yaml
  locator: Complete current YAML at head 67d0dd66fe04472c58f4ad9c8b860df18a9f5f8a.
  accessed_at: '2026-11-03T04:04:51.926479Z'
  support: supports
  summary: Whole maintained record inspected read-only, including components, graph
    edges, evidence, image/provenance, discussions and change history.
  snapshot_sha256: 7eb101d943b736d756d5ea90d304e6cc2b6dc59a11224203f2c5e7ea30cabc8b
- evidence_id: septin-s2349-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Components; scope and grounding requirements.
  accessed_at: '2026-11-03T04:04:51.926479Z'
  support: supports
  summary: Ground the existing generic family when an exact native family exists;
    do not substitute local cohort membership for family identity.
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
- evidence_id: check-qc
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/qc.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T04:01:56.430128Z'
  support: supports
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  snapshot_sha256: 65043448dd2644fc7cb6ade9797409762042201acec6e2b77e623eef55690183
- evidence_id: check-labels
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/labels.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T03:57:25.065615Z'
  support: supports
  summary: 4232 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  snapshot_sha256: d8200b370ec584f49336f01ed9035fbe21f0aa191ad0257a9a421938e9f17ecb
- evidence_id: check-trait-links
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/trait-links.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T03:57:00.382708Z'
  support: supports
  summary: Native TraitMech link check passed.
  snapshot_sha256: 8b336cdefbbd3daf6da8787990efdbe346c95e2c8361d50b7eb68a18f2d5a44a
- evidence_id: check-vendored
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/vendored.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T03:56:59.746433Z'
  support: supports
  summary: Pinned governed files match; native vendored check passed.
  snapshot_sha256: b1f169d103aaefa930745468bcca171e5867b9cc49e4e74311e458097e3252a6
- evidence_id: check-curies
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/curies.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T03:57:24.992134Z'
  support: supports
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  snapshot_sha256: fb3be251020aac118f6df680372ae7aaa32c2a1dd3366648cde95494f19d9dd2
- evidence_id: focused
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/focused-results.json
  locator: All twenty actual target schema/strict command outputs
  accessed_at: '2026-11-03T04:05:43Z'
  support: supports
  summary: Ten schema and ten strict commands returned exit zero.
  snapshot_sha256: d565064964531e606365294070434e20b9d8d6b36af4a549f0edcbbd7d85ae88
- evidence_id: supplemental-pmid
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2349/pmid-chunks-receipt.json
  locator: Complete native-report PMID set checked with unchanged resolver in batches
    of at most fifty
  accessed_at: '2026-11-03T03:59:15.147400Z'
  support: supports
  summary: 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers
    remain unverified.
  snapshot_sha256: 45f4c6a3bec358d1e1e32dcf973d0ed7b4108f6196546f1012fab68a33e542e3
- evidence_id: historical-adapter-runner-availability
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical runner invocation receipt, cross-checked against exact stdout/stderr
    hashes; reread during PR2349 synthesis
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  summary: Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS
    PermissionError reading the configured runner pyvenv.cfg. This is a retained historical
    availability observation, not a fresh attempt or a scientific validation failure.
    Native policy permits inspected source-catalogue fallback.
assessments:
- assessment_id: plaque-spasmoneme-identity-composition
  area: identity
  topic: Stalk organelle, family scope and preparation boundaries
  outcome: supported
  summary: The intracellular composite stalk organelle is distinct from sheath and
    continuous body myonemes. Spasmin-rich fractions and compartment immunolabeling
    support the combined centrin/spasmin class; broader IPR050145 is explicitly not
    an exact match. Native inventory, assembly essentiality and proposed spaconnectin/Sfi1
    scaffold remain unresolved. Canonical V. convallaria and C. polypinum identities
    match authorities. Jiang2025 abstract places only CCDC specifically in sheath;
    EGF-like proteins remain stalk-level, with neither promoted into spasmoneme membership.
  target_ids:
  - cellstructuremech:stalk_spasmoneme
  evidence_ids:
  - plaque-stalk-primary-agent-routledge-native-pdf
  - plaque-stalk-primary-agent-konior-pdf
  - plaque-stalk-agent-IPR050145
  - plaque-stalk-agent-go
  - plaque-stalk-agent-taxon-60850
  - plaque-stalk-agent-taxon-168244
  - plaque-stalk-agent-literature-metadata
  - plaque-stalk-asai1998-publisher-abstract
  - plaque-record-stalk_spasmoneme
- assessment_id: plaque-spasmoneme-stale-graph-refresh
  area: graph
  topic: Substantive refresh of three newly described response edges
  outcome: supported
  summary: 'The three added descriptions were reassessed: Routledge1978 supports calcium-responsive
    glycerinated preparations, with preparation/pH-dependent rates rather than a universal
    rapid kinetic constant; Ryu2012 supports Vorticella coiling/retraction and reduced
    excursion/prolonged contraction under imposed channel-flow resistance. The graph
    explicitly separates glycerinated calcium tests from live V. convallaria load
    experiments and remains FUNCTION/NONMECHANISTIC. No molecular motor, channel,
    serial force-additive architecture or ATP-independent live recovery is asserted.
    Staleness is refreshable without editing the record.'
  target_ids:
  - cellstructuremech:stalk_spasmoneme
  evidence_ids:
  - plaque-stalk-primary-agent-routledge-native-pdf
  - plaque-stalk-primary-agent-ryu-pdf
  - plaque-record-stalk_spasmoneme
- assessment_id: plaque-spasmoneme-image-provenance
  area: provenance
  topic: Exact CIL preview and bounded image interpretation
  outcome: supported
  summary: Native item identity, species, creator, public-domain status and preview
    match the record. Fresh JPEG exactly matches frozen tracked bytes and visually
    supports morphology only. The current catalogue date differs by one day from the
    original historical review; the record asserts only year2012, which remains supported.
    No raw-archive quality, exact stalk level, protein-specific signal or scale-derived
    dimensions are inferred.
  target_ids:
  - cellstructuremech:stalk_spasmoneme
  evidence_ids:
  - plaque-stalk-agent-cil39509-curl
  - plaque-stalk-agent-cil-preview
  - plaque-record-stalk_spasmoneme
- assessment_id: plaque-km-identity-composition
  area: identity
  topic: Overlapping cortical ribbon bundle and tubulin family identities
  outcome: supported
  summary: Primary morphology supports a longitudinal overlapping ribbon bundle in
    S. coeruleus, distinct from a single microtubule, basal body, deeper myoneme and
    striated ciliary rootlet. The broad GO microtubule-bundle parent and cortical
    parthood are appropriate. IPR002452/IPR002453 identify alpha/beta families, not
    native paralog inventories, essential subunits or a bridge motor. Genus-qualified
    identity is not a claim of genus-wide prevalence.
  target_ids:
  - cellstructuremech:stentor_km_fiber
  evidence_ids:
  - plaque-stentor-km-agent-huang1973-pdf
  - plaque-stentor-km-agent-go
  - plaque-stentor-km-agent-taxon-5963
  - plaque-stentor-km-agent-IPR002452
  - plaque-perialgal-prep-IPR002453
  - plaque-stentor-km-agent-slabodnick2014
  - plaque-record-stentor_km_fiber
- assessment_id: plaque-km-model-and-perturbation
  area: graph
  topic: Fixed-state sliding inference versus broad tubulin intervention
  outcome: supported
  summary: The record appropriately says implicated in re-extension and keeps bridge-driven
    sliding a model. Fixed-state overlap changes and opposing myoneme behavior do
    not identify a native ATPase or dynein; selective interventions were unsuccessful.
    Beta-tubulin RNAi does produce cortical-row breaks and disorientation, as the
    explicitly NONMECHANISTIC graph states. Mob1 diffuse cortical localization is
    not Km membership, and its perturbation phenotypes are not transferred to tubulin.
  target_ids:
  - cellstructuremech:stentor_km_fiber
  evidence_ids:
  - plaque-stentor-km-agent-huang1973-pdf
  - plaque-stentor-km-agent-slabodnick2014
  - plaque-record-stentor_km_fiber
- assessment_id: plaque-km-image-provenance
  area: provenance
  topic: Printed Figure8, page anchor and link-only licence
  outcome: supported
  summary: Complete PDF page8/printed711 visibly contains the described extended-cell
    transverse Km fiber, numbering diagram and0.1micrometer bar. Native package PDF/XML
    checksums match; JATS specifies CC BY-NC-SA4.0. The record links the printed figure
    and does not invent an XML figure identity or host/adapt a copy.
  target_ids:
  - cellstructuremech:stentor_km_fiber
  evidence_ids:
  - plaque-stentor-km-agent-huang1973-pdf
  - plaque-stentor-km-agent-huang1973-jats
  - plaque-stentor-km-agent-huang1973-package
  - plaque-record-stentor_km_fiber
- assessment_id: plaque-perialgal-identity-composition
  area: identity
  topic: Host irregular meshwork and directly stained beta-tubulin
  outcome: supported
  summary: Boudreau2025 supports an irregular host cortical meshwork with gaps occupied
    by algal vacuoles, distinct from regular individual cages, Km bundles, vacuole
    membranes and algal cells. Beta-tubulin T0198 staining supports the declared partial
    family inventory, not paralogs or linkers. S. pyriformis identity is supported
    by the source18S analysis and authority; host structure remains separate from
    independently culturable Chlorella.
  target_ids:
  - cellstructuremech:stentor_perialgal_microtubule_meshwork
  evidence_ids:
  - plaque-perialgal-prep-boudreau2025-jats
  - plaque-perialgal-prep-go
  - plaque-perialgal-prep-tax-2721102
  - plaque-perialgal-prep-IPR002453
  - plaque-record-stentor_perialgal_microtubule_meshwork
- assessment_id: plaque-perialgal-functional-limits
  area: evidence
  topic: Proposed positioning without selective causal proof
  outcome: supported
  summary: Spatial association and return after bulk centrifugation support a cortical-positioning
    hypothesis, not a selective requirement of the meshwork for anchoring, photosynthetic
    benefits, photoprotection, gas exchange or phototaxis. The qualified function,
    open discussion and absence of a mechanistic causal graph preserve that distinction;
    acknowledged unknown composition and linker identities are not new defects.
  target_ids:
  - cellstructuremech:stentor_perialgal_microtubule_meshwork
  evidence_ids:
  - plaque-perialgal-prep-boudreau2025-jats
  - plaque-perialgal-prep-go-search
  - plaque-record-stentor_perialgal_microtubule_meshwork
- assessment_id: plaque-perialgal-image-provenance
  area: provenance
  topic: Native Figure3 A/B and structured licence incompleteness
  outcome: supported
  summary: 'The visually inspected native figure and PDF page6 caption agree with
    F3 and record A/B labels: chlorophyll/beta-tubulin images plus six sections through
    expanded mesh. Exact XML/PDF/JPEG MD5 values match metadata. Copyright explicitly
    grants CC BY4.0 while licence_code remains null; the record preserves link-only
    use and its hosting guard. Expanded distances are not native measurements.'
  target_ids:
  - cellstructuremech:stentor_perialgal_microtubule_meshwork
  evidence_ids:
  - plaque-perialgal-prep-boudreau2025-jats
  - plaque-perialgal-prep-figure3
  - plaque-perialgal-prep-paper-pdf
  - plaque-perialgal-prep-boudreau2025-package
  - plaque-record-stentor_perialgal_microtubule_meshwork
- assessment_id: plaque-ciliate-adapter-coverage
  area: provenance
  topic: Organism/dataset coverage establishes source-adapter applicability
  outcome: supported
  target_ids:
  - cellstructuremech:stalk_spasmoneme
  - cellstructuremech:stentor_km_fiber
  - cellstructuremech:stentor_perialgal_microtubule_meshwork
  summary: The original physical-structure/no-expression rationale was insufficient
    because these records name candidate proteins or regulators. The fresh complete
    returned catalogue lacks all assigned ciliate genera, so organism-specific iModulonDB
    queries are not applicable; coverage absence is not a biological negative. Root
    separately records runner availability and its actual historical attempt without
    claiming a new CLI run.
  evidence_ids:
  - plaque-adapter-datasets-current
  - plaque-record-stalk_spasmoneme
  - plaque-record-stentor_km_fiber
  - plaque-record-stentor_perialgal_microtubule_meshwork
- assessment_id: micro-stellate-identity
  area: identity
  topic: Luminal assembly and distinct neighboring structures
  outcome: supported
  summary: Local luminal-fiber identity, OTHER kind and broad parent/enclosing-transition-zone
    parthood are supported. Central cylinder, Y-links, external transition fibers,
    centrin arm and distal sleeve are distinct. The literal GO query is bounded, not
    an exhaustive absence proof.
  target_ids:
  - cellstructuremech:transition_zone_stellate_fiber_system
  evidence_ids:
  - micro-record-stellate
  - micro-current-stellate-agent-go
  - micro-current-stellate-agent-go-stellate-search
  - micro-current-stellate-agent-diener2015-html
  - micro-current-stellate-agent-hoek2022-pdf
- assessment_id: micro-stellate-component
  area: grounding
  topic: Centrin membership, sequence bridge and family scope
  outcome: supported
  summary: Reviewed P05434 identity, pCaBP4/source bridge and pleiotropic mutant/revertant
    evidence support centrin membership. The inspected families extend beyond the
    local constituent class; absence of a primary gene symbol is correctly preserved.
    No molecular sufficiency or universal essentiality is inferred.
  target_ids:
  - cellstructuremech:transition_zone_stellate_fiber_system
  evidence_ids:
  - micro-record-stellate
  - micro-current-stellate-agent-P05434
  - micro-current-stellate-agent-taillon1992-pdf
  - micro-current-stellate-agent-IPR050145
  - micro-current-stellate-agent-IPR050230
- assessment_id: micro-stellate-mechanism
  area: graph
  topic: Extracted-cell response and unresolved excision disagreement
  outcome: supported
  summary: The five graph edges preserve composition, A3 attachment and calcium-triggered
    condensation/inward doublet displacement. The1994 detergent-model experiment supports
    this bounded response. Jarvik abstract counterevidence, residual TableI excision
    and broader katanin preparations do not justify universal necessary/sufficient
    severing by centrin; the record explicitly retains that conflict.
  target_ids:
  - cellstructuremech:transition_zone_stellate_fiber_system
  evidence_ids:
  - micro-record-stellate
  - micro-current-stellate-agent-sanders1994-pdf
  - micro-current-stellate-agent-hoek2022-pdf
  - micro-current-jarvik1991-abstract
  - micro-current-stellate-agent-lohret1998-html
- assessment_id: micro-stellate-image-scope
  area: provenance
  topic: Strains, link-only Figure2 and licence
  outcome: supported
  summary: Species3055 is valid and137c/isolate416 are assay labels, not inferred
    culture accessions. Figure2 A–F and TableI were freshly visually checked. PDFpage3/0.2µm/extended-versus-condensed
    comparison and CC BY-NC-SA permissions agree. No tracked image or new clade-wide
    distribution is implied.
  target_ids:
  - cellstructuremech:transition_zone_stellate_fiber_system
  evidence_ids:
  - micro-record-stellate
  - micro-current-stellate-agent-tax-3055
  - micro-current-stellate-agent-sanders1994-pdf
  - micro-current-stellate-agent-sanders1994-jats
- assessment_id: micro-spool-identity-composition
  area: identity
  topic: Shape-bearing tubulin-positive assembly
  outcome: supported
  summary: Primary U-ExM supports the local spool identity and generic Tubulin component.
    The broad GO relations and IPR000217 scope are appropriate without exact genes,
    fixed subtype stoichiometry, standard lattice topology or assumed centrin/DNA
    constituents.
  target_ids:
  - cellstructuremech:tubulin_spool
  evidence_ids:
  - micro-record-spool
  - micro-current-spool-agent-go
  - micro-current-spool-agent-go-spool-search
  - micro-current-spool-agent-IPR000217
  - micro-current-spool-agent-mikus2025-paper-pdf
  - micro-current-spool-agent-table-s1
- assessment_id: micro-spool-sample-dataset
  area: provenance
  topic: Culture and pinned specimen annotations
  outcome: supported
  summary: RCC10719/Takayama/P22-120, row1384 E7Ab/interphase/one-species/Yes and
    the exact pinned volume agree. Mixed RCC3511/RCC10719 filenames do not establish
    synonymy or spool occurrence in Biecheleriopsis. The volumes project, three channel
    sources, category annotations and archive link are verified without raw-volume
    reanalysis or prevalence inference.
  target_ids:
  - cellstructuremech:tubulin_spool
  evidence_ids:
  - micro-record-spool
  - micro-current-spool-agent-tax-241424
  - micro-current-spool-agent-table-s1
  - micro-current-spool-agent-project
  - micro-current-spool-agent-volumes-dataset
  - micro-current-spool-agent-categories
  - micro-current-spool-agent-github-readme
- assessment_id: micro-spool-image-function
  area: scope
  topic: Observed morphology versus hypothesis and scale uncertainty
  outcome: supported
  summary: Tracked image and fresh publisher bytes match; D–E alone supply spool panels.
    Fixed-cell expanded immunofluorescence does not establish live dynamics, desmose-mediated
    function, universal two-spool counts or exact lattice. The unresolved Figure2-versus-Methods
    scale conflict is explicit and no native dimensions are asserted. CC BY4.0 is
    supported by article and VOR metadata.
  target_ids:
  - cellstructuremech:tubulin_spool
  evidence_ids:
  - micro-record-spool
  - micro-tracked-spool-image
  - micro-current-spool-agent-publisher-figure2
  - micro-current-spool-agent-mikus2025-paper-pdf
  - micro-current-spool-agent-mikus2025-crossref
- assessment_id: micro-crossbridge-identity
  area: identity
  topic: Exact horizontal link and disc parthood
  outcome: supported
  summary: Exact GO crossbridge identity and part_of direction agree with primary
    lateral-link observations. The graph separates crossbridges from dorsal microribbons,
    microtubules, within-complex B bridge and whole disc.
  target_ids:
  - GO:0097595
  evidence_ids:
  - micro-record-crossbridge
  - micro-current-crossbridge-agent-go
  - micro-current-crossbridge-agent-schwartz2012-jats
- assessment_id: micro-crossbridge-function-scope
  area: scope
  topic: Bounded structural linkage with unresolved composition
  outcome: supported
  summary: WBC6 trophozoite cryo-ET of extracted flattened discs supports neighboring-ribbon
    linkage. Flexible crossbridge densities and discussion hypotheses do not demonstrate
    ATP/calcium-driven contraction, identify crossbridge proteins or establish sufficiency
    for attachment. Empty components and the explicit TODO are justified; qualitative
    COMMON is not measured prevalence.
  target_ids:
  - GO:0097595
  evidence_ids:
  - micro-record-crossbridge
  - micro-current-crossbridge-agent-tax-5741
  - micro-current-crossbridge-agent-schwartz2012-jats
  - micro-current-crossbridge-agent-epmc
- assessment_id: micro-microribbon-identity-graph
  area: graph
  topic: Trilaminar scaffold and four nonmechanistic relationships
  outcome: supported
  summary: Exact GO identity/synonym scopes, disc parthood and the four directed composition/topology
    edges are supported. Microribbons extend from microtubules and link laterally
    through crossbridges. The GO-derived mass range/tubulin exclusion is not relabeled
    as a new primary assay. No contractile mechanism, sheet-specific assignment or
    complete inventory is added.
  target_ids:
  - GO:0097594
  evidence_ids:
  - micro-record-microribbon
  - micro-current-crossbridge-agent-go
  - micro-current-microribbon-agent-go-mt
  - micro-current-crossbridge-agent-schwartz2012-jats
- assessment_id: micro-microribbon-components
  area: grounding
  topic: Primary localization versus family-cohort mapping
  outcome: supported
  summary: Hagen directly supports beta-/delta-giardin and SALP-1 association, while
    Schwartz provides primary architecture and secondary composition context. IPR008374/PF06705
    map beta/delta candidates; the inspected SALP-1 record and historical table do
    not establish the same full-cohort accession. Retaining an explicitly unresolved
    broad cohort is defensible; absent annotation does not disprove homology. Finer
    optional rows are not mandatory repairs.
  target_ids:
  - GO:0097594
  evidence_ids:
  - micro-record-microribbon
  - micro-current-microribbon-agent-hagen2011-jats
  - micro-current-crossbridge-agent-schwartz2012-jats
  - micro-current-microribbon-agent-ipr-008374
  - micro-current-microribbon-agent-ipr-038835
  - micro-current-microribbon-agent-pfam-06705
  - micro-current-microribbon-agent-uniprot-loci
  - micro-current-microribbon-agent-uniprot-delta
- assessment_id: micro-microribbon-taxonomy-methods
  area: scope
  topic: Species aliases, strain and preparation limits
  outcome: supported
  summary: Giardia intestinalis/lamblia are valid synonyms of species5741; WBC6 ATCC50803
    is distinct strain evidence. Extracted-cytoskeleton tomography and tagged-protein
    immunolabeling establish architecture/association, not purified-protein reconstitution,
    exclusive composition, uniform turnover or all-stage/all-strain occurrence.
  target_ids:
  - GO:0097594
  evidence_ids:
  - micro-record-microribbon
  - micro-current-crossbridge-agent-tax-5741
  - micro-current-microribbon-agent-tax-184922
  - micro-current-crossbridge-agent-schwartz2012-jats
  - micro-current-microribbon-agent-hagen2011-jats
- assessment_id: micro-input-lineage
  area: provenance
  topic: Unchanged targets and empty original findings
  outcome: supported
  summary: All4 targets match original frozen hashes; original native validation/render
    passes. Every original verdict is pass_with_limitations with no findings, so no
    scientific issue lineage has been silently closed. Current assessments retain
    the original scientific boundaries.
  target_ids:
  - cellstructuremech:transition_zone_stellate_fiber_system
  - cellstructuremech:tubulin_spool
  - GO:0097595
  - GO:0097594
  evidence_ids:
  - micro-original-native-checks
  - micro-prior-stellate
  - micro-prior-spool
  - micro-prior-crossbridge
  - micro-prior-microribbon
- assessment_id: micro-adapter-coverage
  area: scope
  topic: Corrected applicability for named constituents
  outcome: supported
  summary: Stellate, spool and microribbon name proteins/accessions and need structured-source
    applicability documentation. The inspected complete catalogue has no matching
    organism/dataset; no module lookup or negative biological inference follows. Root
    runner evidence is separate. Crossbridge has no named molecular constituent or
    regulator and is excluded from the defect.
  target_ids:
  - cellstructuremech:transition_zone_stellate_fiber_system
  - cellstructuremech:tubulin_spool
  - GO:0097595
  - GO:0097594
  evidence_ids:
  - micro-adapter-policy
  - micro-current-current-adapter-catalogue
  - micro-prior-stellate
  - micro-prior-spool
  - micro-prior-crossbridge
  - micro-prior-microribbon
- assessment_id: septin-S2349-A1
  area: identity
  topic: Split-ring identity and hierarchy
  outcome: supported
  summary: GO:0032176 precisely denotes the paired rings, distinct from the single
    ring/collar and broader septin cytoskeleton; GO parent and part_of directions
    are retained.
  target_ids:
  - GO:0032176
  evidence_ids:
  - septin-s2349-split-rings-agent-go
  - septin-s2349-record-split_septin_rings
- assessment_id: septin-S2349-A2
  area: grounding
  topic: Generic Septin family
  outcome: concern
  summary: 'The broad septin_proteins component remains incorrectly label-only for
    a local-cohort reason; IPR016491 is exactly the already-named generic Septin class.
    Preserve predecessor F1 and track through #2499.'
  target_ids:
  - GO:0032176
  evidence_ids:
  - septin-s2349-split-rings-agent-family
  - septin-s2349-record-split_septin_rings
  - septin-s2349-policy
- assessment_id: septin-S2349-A3
  area: evidence
  topic: Split-ring morphology and bounded cytokinesis function
  outcome: supported
  summary: The nonmechanistic assemble/split/flank graph and cautious thought-to-trap
    wording are supported by GO and the inspected secondary reviews. Collective structural
    necessity does not assert that every paralogue is essential; no exact paralogue
    membership or taxa are added.
  target_ids:
  - GO:0032176
  evidence_ids:
  - septin-s2349-split-rings-agent-go
  - septin-s2349-split-rings-agent-douglas-pmc
  - septin-s2349-split-rings-agent-versele-pmc
- assessment_id: septin-S2349-A4
  area: scope
  topic: Split-ring adapter scope
  outcome: supported
  summary: This sparse record contains generic septin material without named genes
    or accessions. Do not allege the richer-record named-molecule exemption defect
    here; the current catalogue additionally lacks the eukaryotic context.
  target_ids:
  - GO:0032176
  evidence_ids:
  - septin-s2349-record-split_septin_rings
  - septin-s2349-current-adapter-catalogue
- assessment_id: septin-S2349-A5
  area: identity
  topic: TACC/TOG identity, products and family scope
  outcome: supported
  summary: GO:0070850 denotes the complex; Alp7 Q9URY2 and Alp14 O94534 are reviewed
    972h- products and synonyms are verified. IPR045110 is XMAP215 family, whereas
    Alp7 IPR024312 is only a C-terminal domain and PF12709 coiled coil. Ndc80 Q10198
    is graph context, not a third constituent; no universal 2:2 stoichiometry is claimed.
  target_ids:
  - GO:0070850
  evidence_ids:
  - septin-s2349-tacc-prep-go
  - septin-s2349-tacc-prep-Q9URY2
  - septin-s2349-tacc-prep-O94534
  - septin-s2349-tacc-prep-Q10198
  - septin-s2349-tacc-prep-IPR045110
  - septin-s2349-tacc-prep-IPR024312
  - septin-s2349-tacc-prep-matches-Q9URY2
  - septin-s2349-tacc-prep-tax-4896
  - septin-s2349-tacc-prep-tax-284812
- assessment_id: septin-S2349-A6
  area: evidence
  topic: Alp7/Alp14 polymerization and nucleation
  outcome: supported
  summary: 2016 purified association and tip occupancy support the first mechanism;
    2018 Alp7-dependent MTOC recruitment/nucleation with retained plus-end tracking
    supports the second. The record correctly discloses conflicting deletion elongation
    observations and the engineered partial rescue; it does not universalize either
    context.
  target_ids:
  - GO:0070850
  evidence_ids:
  - septin-s2349-tacc-prep-hussmann2016-jats
  - septin-s2349-tacc-prep-nucleation2018-jats
  - septin-s2349-record-tacc_tog_complex
- assessment_id: septin-S2349-A7
  area: graph
  topic: Kinetochore attachment and transport graphs
  outcome: supported
  summary: Ndc80 F420S reduces Alp7/14 kinetochore signal by 30–40% and peptide/coIP/forced
    tethering experiments support bounded recruitment. Alp14 L615A export and Alp7
    five-site phosphorylation/import phenotypes retain binding and residual import;
    Cut15 fragment two-hybrid is model support, and NLS growth rescue is not full
    spindle restoration.
  target_ids:
  - GO:0070850
  evidence_ids:
  - septin-s2349-tacc-prep-attachment2013-jats
  - septin-s2349-tacc-prep-transport2014-jats
  - septin-s2349-record-tacc_tog_complex
- assessment_id: septin-S2349-A8
  area: scope
  topic: Dis1 and figure provenance
  outcome: supported
  summary: 2019 forced targeting at endogenous expression fails reciprocal substitution
    while earlier overexpression compensation is explicitly retained. Figure 7 byte-matches
    the frozen image and depicts mixed-source purified TIRF material; CC BY 4.0 and
    caption scope match.
  target_ids:
  - GO:0070850
  evidence_ids:
  - septin-s2349-tacc-prep-dis1_2019-jats
  - septin-s2349-tacc-prep-figure7
  - septin-s2349-tacc-prep-hussmann2016-jats
- assessment_id: septin-S2349-A9
  area: identity
  topic: Telocentrosome identity and exact accession boundaries
  outcome: supported
  summary: Local identity is appropriate for the telomere-associated MTOC, distinct
    from SPB, bouquet and narrower SUN/KASH tether. Eight molecular/example identities
    match native reviewed 972h- entries; Mto1 and Ssm4 homonyms are disambiguated.
    SUN1-5 and Tctex1 are exact family classes; Kms1, Kms2, Mto1, cytoplasmic Dhc1
    and Ssm4 have honestly bounded label-only reasons.
  target_ids:
  - cellstructuremech:telocentrosome
  evidence_ids:
  - septin-s2349-telo-prep-go
  - septin-s2349-telo-prep-Q09825
  - septin-s2349-telo-prep-P87245
  - septin-s2349-telo-prep-O43087
  - septin-s2349-telo-prep-O94488
  - septin-s2349-telo-prep-Q9Y705
  - septin-s2349-telo-prep-Q9UTS6
  - septin-s2349-telo-prep-O13290
  - septin-s2349-telo-prep-O42667
  - septin-s2349-telo-prep-query-mto1
  - septin-s2349-telo-prep-query-ssm4
  - septin-s2349-telo-prep-IPR045119
  - septin-s2349-telo-prep-IPR005334
  - septin-s2349-telo-prep-IPR030268
  - septin-s2349-telo-prep-IPR026983
  - septin-s2349-telo-prep-matches-P87245
  - septin-s2349-telo-prep-matches-O43087
  - septin-s2349-telo-prep-matches-O94488
  - septin-s2349-telo-prep-matches-O13290
  - septin-s2349-telo-prep-matches-O42667
- assessment_id: septin-S2349-A10
  area: graph
  topic: Substantive stale telocentrosome refresh
  outcome: supported
  summary: The sole scientific change is gamma_tuc node_type GENE_OR_PROTEIN to STRUCTURE,
    with its curation event. GO:0000930 is a multi-protein complex and Yoshida images
    Alp4 as a reporter, so current type STRUCTURE is supported. Reassessed all retained
    causal claims against primary sources; refresh must bind current SHA7eb101d9 rather
    than reuse old SHA05d5a42e or historical 4/4 protein-node coverage.
  target_ids:
  - cellstructuremech:telocentrosome
  evidence_ids:
  - septin-s2349-telo-prep-go
  - septin-s2349-telo-prep-yoshida2013-jats
  - septin-s2349-record-telocentrosome
- assessment_id: septin-S2349-A11
  area: evidence
  topic: Meiotic assembly and recruitment limits
  outcome: supported
  summary: Primary imaging and perturbation establish cytoplasmic telomeric nucleation
    separate from Sid4-marked SPB. Kms1/Mto1 and Dlc1 contribute to Alp4 recruitment;
    Dhc1 dispensability is confined to that readout. Crosslinked-motor gathering is
    a proposed model. Upstream Bqt1/Bqt2/Rap1/Taz1 context is not a universal absence
    assertion, and no unsupported Mto2/all-gammaTuC/dynactin expansion is made.
  target_ids:
  - cellstructuremech:telocentrosome
  evidence_ids:
  - septin-s2349-telo-prep-yoshida2013-jats
  - septin-s2349-telo-agent-yoshida2013-supp
  - septin-s2349-record-telocentrosome
- assessment_id: septin-S2349-A12
  area: scope
  topic: Ectopic 2025 assembly and image evidence
  outcome: supported
  summary: Ectopic Bqt1/Bqt2 in Rabl-deficient haploid mitotic cells yields partial
    Sad1/Kms1/Mto1/Alp4 recruitment without detected Dhc1 or complete bouquet, and
    Kms1 loss suppresses some phenotypes. Record avoids normal mitotic-generalization.
    Figure 2 pixel content, source hash and CC BY-NC-SA 3.0 licence agree; experimental
    stocks are not conflated with reference UniProt strain.
  target_ids:
  - cellstructuremech:telocentrosome
  evidence_ids:
  - septin-s2349-telo-prep-jimenez2025-jats
  - septin-s2349-telo-agent-jimenez2025-supp
  - septin-s2349-telo-prep-figure2
  - septin-s2349-telo-prep-yoshida2013-jats
- assessment_id: septin-S2349-A13
  area: scope
  topic: Named-molecule structured-adapter applicability
  outcome: concern
  summary: The original non-transcriptomic exemption does not satisfy the current
    skill for named molecular cases. Fresh full official catalogue has 20 organisms/28
    datasets and no S. pombe; this is the defensible downstream non-applicability
    basis. No new local runner execution is asserted; use the root historical runner
    receipt explicitly if needed.
  target_ids:
  - GO:0070850
  evidence_ids:
  - septin-s2349-current-adapter-catalogue
- assessment_id: septin-S2349-A14
  area: scope
  topic: Named-molecule structured-adapter applicability
  outcome: concern
  summary: The original non-transcriptomic exemption does not satisfy the current
    skill for named molecular cases. Fresh full official catalogue has 20 organisms/28
    datasets and no S. pombe; this is the defensible downstream non-applicability
    basis. No new local runner execution is asserted; use the root historical runner
    receipt explicitly if needed.
  target_ids:
  - cellstructuremech:telocentrosome
  evidence_ids:
  - septin-s2349-current-adapter-catalogue
- assessment_id: current-input-comparison
  area: provenance
  topic: Complete frozen-input comparison and bounded refresh
  outcome: supported
  summary: 2 of ten original target hashes differ from current main. The changed content
    is substantively reassessed in the target-specific assessments; original observations
    remain historical and unchanged. All current target and used context bytes are
    frozen.
  target_ids:
  - GO:0032176
  - cellstructuremech:stalk_spasmoneme
  - cellstructuremech:stentor_km_fiber
  - cellstructuremech:stentor_perialgal_microtubule_meshwork
  - GO:0070850
  - cellstructuremech:telocentrosome
  - cellstructuremech:transition_zone_stellate_fiber_system
  - cellstructuremech:tubulin_spool
  - GO:0097595
  - GO:0097594
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
- finding_id: septin-S2349-F1
  issue_key: split-septin-rings-generic-family-withheld
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: The generic septin component has an exact family grounding
  description: The septin_proteins row is REVIEWED_LABEL_ONLY because no family accession
    was assigned for the complete split-ring-forming cohort. Native IPR016491 directly
    represents the generic Septin family already named by the row. Assigning this
    class does not require determining which paralogues remain in a particular split
    pair or asserting that every family member forms this structure. Ground the generic
    row to InterPro:IPR016491 and retain exact membership as an open question.
  target_ids:
  - GO:0032176
  field_paths:
  - components[component_id=septin_proteins].grounding
  - components[component_id=septin_proteins].grounding_status
  - components[component_id=septin_proteins].grounding_notes
  - discussions[discussion_id=resolve_split_septin_rings_grounding]
  evidence_ids:
  - septin-s2349-split-rings-agent-family
  - septin-s2349-split-rings-agent-go
  - septin-s2349-record-split_septin_rings
  - septin-s2349-policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/split_septin_rings.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Components
  native_severity: minor
  normalization_reason: The structure and function remain supported; this is a resolvable
    family mapping for an existing generic component.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T084039Z-split-septin-rings-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2499
actions:
- action_id: septin-S2349-AC1
  finding_ids:
  - septin-S2349-F1
  target_ids:
  - GO:0032176
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/split_septin_rings.yaml
    role: maintained scientific record
  description: In authorized curation, ground the septin-proteins row to InterPro:IPR016491
    and align grounding status and notes. Preserve historical discussion rationale
    and record current progress in notes; retain unresolved localized cohort and individual
    essentiality limits.
  acceptance_checks:
  - Compare component scope against native IPR016491 family description.
  - Do not add unverified paralogue examples or universal assembly necessity.
  - Run native schema, strict, label, history and generated-page checks after maintained-record
    changes.
  generator: Maintained structure YAML; generated pages derive from it.
limitations:
- 'Stalk spasmoneme, Stentor Km fiber and perialgal meshwork independent subreview:
  Stalk spasmoneme: Routledge1978 claim-bearing preparation, extraction, calcium-response
  and Discussion sections were inspected; rates are preparation/pH dependent, and
  no universal fast kinetic constant is inferred from the word rapid. Underlying cited
  experiments were not independently reanalyzed.'
- 'Stalk spasmoneme, Stentor Km fiber and perialgal meshwork independent subreview:
  Stalk spasmoneme: Konior2009 Methods/Results/Discussion and relevant legends were
  read, but no raw immunogold recount was performed. Ryu2012 main mechanical experiments
  and assumptions were read; Supporting Material and raw trajectories were not audited.'
- 'Stalk spasmoneme, Stentor Km fiber and perialgal meshwork independent subreview:
  Stalk spasmoneme: Asai1998, Maciejewski1999 and Jiang2025 contributions remain abstract-tier.
  Asai direct curl returned403 and the first browser call timed out; a subsequent
  publisher browser extraction returned the abstract. The EPMC multi-DOI query omitted
  Asai, not evidence that the paper does not exist.'
- 'Stalk spasmoneme, Stentor Km fiber and perialgal meshwork independent subreview:
  Stalk spasmoneme: CIL preview resolution supports qualitative morphology only. Current
  January23,2012 catalogue metadata differs from the older review''s January22 historical
  observation; current record only claims2012. No raw archive, physiological calcium
  assay or calibrated dimension was reviewed.'
- 'Stalk spasmoneme, Stentor Km fiber and perialgal meshwork independent subreview:
  Stentor Km fiber: Primary1973 introduction/Methods, cortical organization/overlap
  Results, Figure8 and bridge-motor Discussion were inspected. Later unrelated myoneme-contraction
  discussion and cited underlying studies were not independently audited.'
- 'Stalk spasmoneme, Stentor Km fiber and perialgal meshwork independent subreview:
  Stentor Km fiber: Slabodnick2014 tubulin and Mob1 localization Results plus relevant
  Methods were inspected. Remaining Mob1 morphogenesis experiments and supplemental
  data were not fully audited. Fixed morphology and broad tubulin knockdown do not
  isolate Km-specific mechanics or identify the native bridge motor.'
- 'Stalk spasmoneme, Stentor Km fiber and perialgal meshwork independent subreview:
  Stentor perialgal meshwork: Claim-bearing anatomy, phylogeny, meshwork, surface-association
  and microscopy/culture Methods were read; unrelated genomic, photosynthesis and
  phototaxis experiments, movies and raw data were not audited. No selective perturbation
  proves anchoring.'
- 'Stalk spasmoneme, Stentor Km fiber and perialgal meshwork independent subreview:
  Stentor perialgal meshwork: Source Figure3 Results text mentions nonexistent panelC,
  but native figure/caption and record correctly use A/B. Structured PMC licence metadata
  remains incomplete; no hosting guard is changed and no expanded dimension is treated
  as native.'
- 'Stalk spasmoneme, Stentor Km fiber and perialgal meshwork independent subreview:
  All three: Historical repository/ontology/taxon absence searches remain historical
  and were not comprehensively repeated. The fresh exact perialgal query and complete
  returned iModulonDB catalogue are bounded remote searches; neither implies exhaustive
  biological or ontology absence.'
- 'Stalk spasmoneme, Stentor Km fiber and perialgal meshwork independent subreview:
  All three: This independent slice ran only original bundle validation/render/historical
  hash checks; root owns current corpus QC, focused record validation and final CI.
  No new adapter CLI run is claimed by this subreview.'
- 'Stellate fiber system, tubulin spool, ventral-disc crossbridge and dorsal microribbon
  independent subreview: All4 assigned target hashes are unchanged. Native original-review
  validation/render ran independently; root owns whole-corpus QC, current focused
  record gates, final CI and merge checks.'
- 'Stellate fiber system, tubulin spool, ventral-disc crossbridge and dorsal microribbon
  independent subreview: Stellate: Sanders claim-bearing Methods/Results/Discussion
  and Figure2/TableI were inspected; Taillon sequence/mutant/revertant/TableII text
  was inspected, but Taillon figure/table pixels and1988 sequence-source bodies were
  not independently reread. Strain labels and pleiotropic versus fiber-selective effects
  remain distinct.'
- 'Stellate fiber system, tubulin spool, ventral-disc crossbridge and dorsal microribbon
  independent subreview: Stellate: direct Jarvik publisher HTTP access returned403
  and browser access timed out; exact EuropePMC DOI search returned0 results. The
  full primary abstract/publisher preview summary was read on ResearchGate, not the
  full body, figures or Methods. These access limits do not contradict existence or
  the bounded counterclaim.'
- 'Stellate fiber system, tubulin spool, ventral-disc crossbridge and dorsal microribbon
  independent subreview: Stellate: Lohret and Diener are limited to specified abstract/introduction/method/claim-bearing
  text passages. Their microscopy pixels, unlisted supplementary material and raw
  data were not reanalyzed. Hoek reading is confined to architecture Results and Figure1
  caption; IFT remainder/supplements/figure pixels not inspected.'
- 'Stellate fiber system, tubulin spool, ventral-disc crossbridge and dorsal microribbon
  independent subreview: Tubulin spool: institutionally hosted Mikus article-in-press
  PDF bytes were reused from the actual03:20:54Z fetch and newly read for the stated
  claim passages. Fresh workbook/native pinned metadata/publisher image and Crossref
  licence were inspected. No raw-volume-to-Figure2-panel mapping, raw volumes or videos
  were analyzed, and no full5479-source archive audit is claimed.'
- 'Stellate fiber system, tubulin spool, ventral-disc crossbridge and dorsal microribbon
  independent subreview: Tubulin spool: workbook inspection was restricted to specified
  headers/rows; categories were parsed across1767 rows and RCC10719/exact-volume fields
  inspected. These annotations are not independent-cell counts, universal prevalence
  or proof of mixed-gel species identity. Unresolved expansion-scale wording prevents
  derived native dimensions.'
- 'Stellate fiber system, tubulin spool, ventral-disc crossbridge and dorsal microribbon
  independent subreview: Crossbridge and microribbon: specified Schwartz architecture/Methods
  and Hagen localization/Methods/Table1 passages were read. Figure pixels, videos,
  raw tomography, full supplementary data and FRAP experiments were not independently
  reanalyzed. Proposed rigidity, contraction and dynamics are not imported as established
  mechanisms.'
- 'Stellate fiber system, tubulin spool, ventral-disc crossbridge and dorsal microribbon
  independent subreview: Microribbon: inspected native protein/family records support
  candidate beta/delta mappings but do not establish exact full-cohort mapping. Missing
  SALP-1 family cross-references do not refute homology. GO-derived exclusion/size
  statements remain authority-backed rather than being attributed to tomography as
  biochemical proof.'
- 'Stellate fiber system, tubulin spool, ventral-disc crossbridge and dorsal microribbon
  independent subreview: Structured sources: the complete iModulonDB catalogue was
  reused with its actual03:20:54Z fetch time and reread for these organisms. Runner
  availability is root-owned evidence. No matching covered target dataset means no
  downstream module query; it is never a biological-negative result.'
- 'Stellate fiber system, tubulin spool, ventral-disc crossbridge and dorsal microribbon
  independent subreview: Bounded GO/UniProt searches explicitly retain literal queries,
  limits and result coverage. Historical ignored-inclusive record creation searches
  are not asserted as freshly rerun corpus-wide absence proofs.'
- 'Split septin rings, TACC/TOG complex and telocentrosome independent subreview:
  Split-ring morphology/function corroboration uses current GO and explicitly secondary
  Douglas/Versele reviews; no new primary diffusion-barrier experiment audit or new
  paralogue-completeness claim.'
- 'Split septin rings, TACC/TOG complex and telocentrosome independent subreview:
  TACC and telocentrosome primary full-text bodies were retrieved, but independent
  inspection is the named Results/Methods/caption scope above, not a claim to have
  reviewed every paragraph, image, supplement or cited reference. TACC supplementary
  figures/tables were not fetched independently; 2019 Alp14-NLS details beyond main
  Methods remain inherited scope.'
- 'Split septin rings, TACC/TOG complex and telocentrosome independent subreview:
  Yoshida supplemental figures are caption/text scope and video legends only; supplemental
  pixels and movies were not independently inspected. Jimenez supplemental coverage
  is Figure6 legend only. The two record-linked main figures were visually inspected.'
- 'Split septin rings, TACC/TOG complex and telocentrosome independent subreview:
  Two InterPro match requests initially returned HTTP429; bounded subsequent requests
  both succeeded and their later receipt times/hashes are used. Scratch conversion
  commands initially referenced response-extension filenames incorrectly and lacked
  optional image/PDF libraries; these are not repository validation failures. Native
  three-bundle validation and render each passed.'
- 'Split septin rings, TACC/TOG complex and telocentrosome independent subreview:
  No new structured adapter runner call or all-corpus QC/CI is claimed by this subreview.
  Root owns current global checks. No records, bundles, GitHub state or branches were
  modified.'
- 'Split septin rings, TACC/TOG complex and telocentrosome independent subreview:
  All external biological evidence cited here was freshly retrieved during this PR;
  no earlier cached scientific source body is passed off as current access. Broad
  literature completeness and absence beyond the exact authority/query scopes are
  not claimed.'
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
- 'Bundle issues #2533 (two stale reviews) and #2534 (eight adapter coverage defects)
  are addressed here. Scientific curation remains in existing #2499; existing validator
  #2514 remains open.'
- Source commit 67d0dd66fe04472c58f4ad9c8b860df18a9f5f8a is retained by tag review-base/pr2349-current-record-followup-20261103.
- CLAUDE.md is an alias of AGENTS.md; canonical regular AGENTS.md bytes are frozen.
- Every inherited source-access and check limitation is attributed to its independent
  subreview. Fresh fetches, cached response re-reading, abstract-only evidence and
  full-body passages retain distinct scopes.
- Six original adapter checks have unsupported exemption rationales, and two originals
  omit the check. Split septin rings and ventral-disc crossbridge are excluded from
  this defect; no unsupported defect is attributed to their sparse named molecular
  inventory.
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T084039Z-split-septin-rings-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T084039Z-stalk-spasmoneme-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T084040Z-stentor-km-fiber-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T084040Z-stentor-perialgal-microtubule-meshwork-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T084040Z-tacc-tog-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T084040Z-telocentrosome-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T084040Z-transition-zone-stellate-fiber-system-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T084041Z-tubulin-spool-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T084041Z-ventral-disc-crossbridge-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T084041Z-ventral-disc-dorsal-microribbon-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
links:
- https://github.com/CultureBotAI/CellStructureMech/pull/2349
- https://github.com/CultureBotAI/CellStructureMech/issues/2499
- https://github.com/CultureBotAI/CellStructureMech/issues/2514
- https://github.com/CultureBotAI/CellStructureMech/issues/2533
- https://github.com/CultureBotAI/CellStructureMech/issues/2534
```
