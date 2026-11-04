# PR 2376: current-input review of ten records and adversarial follow-up

- Review: 20261103T204939Z-pr2376-current-record-followup
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-11-03T20:41:43.388442Z
- Finished UTC: 2026-11-03T20:49:39Z
- Reviewer: Codex root synthesis with three independent read-only adversarial reviewers (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Current-input adversarial follow-up for the complete ten-record cohort after merging main. The stale polaroplast review is refreshed by reassessing newly added anatomical subregion nodes, component joins and two parthood edges. Seven unsupported source-applicability exclusions are corrected; thylakoid lumen, polaroplast and pusule retain justified physical-scope exclusions. Three original thylakoid observations misclassify secondary-review text and an access challenge as primary evidence; the successor corrects source tiers and access-only scope while leaving the originals unchanged. All scientific records remain unchanged. Two inherited major scientific findings remain open across two targets; eight other targets retain qualified positive assessments. Exact predecessor identities and separate curation issue links are preserved.

## Scope And Provenance

Exact ten-record PR cohort reassessed against current main a155c38220bee43550eac4ecff6ff2c0aee0823b. Changed inputs are substantively reassessed. Scientific records remain unchanged.

Selection: Complete cohort of ten maintained records reviewed in original PR head ee89490de10690a7dfadbad77ff2a331d4f24d42.
Coverage: full; 10 reviewed / 10 in the declared population.
Source: working_tree at Git base 55020000323f1344e65128992b35f6ef43c703a2.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0009527 | data/structures/membrane_organelle/plastid_outer_membrane.yaml | maintained | plastid outer membrane |
| GO:0009532 | data/structures/membrane_organelle/plastid_stroma.yaml | maintained | plastid stroma |
| GO:0031976 | data/structures/membrane_organelle/plastid_thylakoid.yaml | maintained | plastid thylakoid |
| GO:0031978 | data/structures/membrane_organelle/plastid_thylakoid_lumen.yaml | maintained | plastid thylakoid lumen |
| GO:0055035 | data/structures/membrane_organelle/plastid_thylakoid_membrane.yaml | maintained | plastid thylakoid membrane |
| GO:0160201 | data/structures/membrane_organelle/polaroplast.yaml | maintained | polaroplast |
| cellstructuremech:pusule | data/structures/membrane_organelle/pusule.yaml | maintained | pusule |
| GO:0160223 | data/structures/membrane_organelle/pyrenoid_tubule.yaml | maintained | pyrenoid tubule |
| GO:0055037 | data/structures/membrane_organelle/recycling_endosome.yaml | maintained | recycling endosome |
| GO:0034777 | data/structures/membrane_organelle/recycling_endosome_lumen.yaml | maintained | recycling endosome lumen |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full native QC | passed | True | GO:0009527, GO:0009532, GO:0031976, GO:0031978, GO:0055035, GO:0160201, cellstructuremech:pusule, GO:0160223, GO:0055037, GO:0034777 | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| Native label correspondence | passed | True | GO:0009527, GO:0009532, GO:0031976, GO:0031978, GO:0055035, GO:0160201, cellstructuremech:pusule, GO:0160223, GO:0055037, GO:0034777 | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| TraitMech references | passed | True | GO:0009527, GO:0009532, GO:0031976, GO:0031978, GO:0055035, GO:0160201, cellstructuremech:pusule, GO:0160223, GO:0055037, GO:0034777 | Native TraitMech link check passed. |
| Pinned governed files | passed | True | GO:0009527, GO:0009532, GO:0031976, GO:0031978, GO:0055035, GO:0160201, cellstructuremech:pusule, GO:0160223, GO:0055037, GO:0034777 | Pinned governed files match; native vendored check passed. |
| Native identifier resolver | passed | True | GO:0009527, GO:0009532, GO:0031976, GO:0031978, GO:0055035, GO:0160201, cellstructuremech:pusule, GO:0160223, GO:0055037, GO:0034777 | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| validate GO:0009527 | passed | True | GO:0009527 | Documented focused command passed. |
| validate-strict GO:0009527 | passed | True | GO:0009527 | Documented focused command passed. |
| validate GO:0009532 | passed | True | GO:0009532 | Documented focused command passed. |
| validate-strict GO:0009532 | passed | True | GO:0009532 | Documented focused command passed. |
| validate GO:0031976 | passed | True | GO:0031976 | Documented focused command passed. |
| validate-strict GO:0031976 | passed | True | GO:0031976 | Documented focused command passed. |
| validate GO:0031978 | passed | True | GO:0031978 | Documented focused command passed. |
| validate-strict GO:0031978 | passed | True | GO:0031978 | Documented focused command passed. |
| validate GO:0055035 | passed | True | GO:0055035 | Documented focused command passed. |
| validate-strict GO:0055035 | passed | True | GO:0055035 | Documented focused command passed. |
| validate GO:0160201 | passed | True | GO:0160201 | Documented focused command passed. |
| validate-strict GO:0160201 | passed | True | GO:0160201 | Documented focused command passed. |
| validate cellstructuremech:pusule | passed | True | cellstructuremech:pusule | Documented focused command passed. |
| validate-strict cellstructuremech:pusule | passed | True | cellstructuremech:pusule | Documented focused command passed. |
| validate GO:0160223 | passed | True | GO:0160223 | Documented focused command passed. |
| validate-strict GO:0160223 | passed | True | GO:0160223 | Documented focused command passed. |
| validate GO:0055037 | passed | True | GO:0055037 | Documented focused command passed. |
| validate-strict GO:0055037 | passed | True | GO:0055037 | Documented focused command passed. |
| validate GO:0034777 | passed | True | GO:0034777 | Documented focused command passed. |
| validate-strict GO:0034777 | passed | True | GO:0034777 | Documented focused command passed. |
| Supplemental bounded PMID authority checks | passed | True | GO:0009527, GO:0009532, GO:0031976, GO:0031978, GO:0055035, GO:0160201, cellstructuremech:pusule, GO:0160223, GO:0055037, GO:0034777 | 909 PMIDs all OK in bounded native requests; full-command limitations remain separate. |
| Official structured-source applicability and covered-dataset cross-checks | passed | False | GO:0009527, GO:0009532, GO:0031976, GO:0031978, GO:0055035, GO:0160201, cellstructuremech:pusule, GO:0160223, GO:0055037, GO:0034777 | Seven targets assert positive molecular/pathway claims: plastid outer membrane, stroma, whole thylakoid, thylakoid membrane, pyrenoid tubule and both recycling-endosome records. Five unsupported explicit check exclusions and two prose-only exclusions are corrected using actual catalogue coverage and bounded applicable source checks. Thylakoid lumen, polaroplast and pusule retain genuine physical/anatomical exclusions. Noncoverage is not biological absence and unrelated hosts are not substitutes. Historical runner unavailability remains historical; actual source fallback access scopes and timestamps are retained. |
| Independent claim-level source review | passed | True | GO:0009527, GO:0009532, GO:0031976, GO:0031978, GO:0055035, GO:0160201, cellstructuremech:pusule, GO:0160223, GO:0055037, GO:0034777 | Three read-only reviewers covered the complete ten-record cohort, including changed inputs, with explicit scientific findings and source-access limits. Final artifact/head acceptance occurs after saving. |
| Retained historical adapter runner availability | unavailable | False | GO:0009527, GO:0009532, GO:0031976, GO:0031978, GO:0055035, GO:0160201, cellstructuremech:pusule, GO:0160223, GO:0055037, GO:0034777 | Historical00:49Z invocation unavailable due to OS access restriction. Official catalogue fallback was inspected separately; no fresh invocation is claimed. Actual historical exit1 is retained in the evidence receipt; the native unavailable-check model has no execution exit-code field. |
| Native plastid outer membrane UniProt verify check | passed | True | GO:0009527 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native plastid outer membrane UniProt causal check | passed | True | GO:0009527 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native plastid stroma UniProt verify check | passed | True | GO:0009532 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native plastid stroma UniProt causal check | passed | True | GO:0009532 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native plastid thylakoid UniProt verify check | passed | True | GO:0031976 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native plastid thylakoid UniProt causal check | passed | True | GO:0031976 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native plastid thylakoid lumen UniProt verify check | passed | True | GO:0031978 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native plastid thylakoid lumen UniProt causal check | passed | True | GO:0031978 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native plastid thylakoid membrane UniProt verify check | passed | True | GO:0055035 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native plastid thylakoid membrane UniProt causal check | passed | True | GO:0055035 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native polaroplast UniProt verify check | passed | True | GO:0160201 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native polaroplast UniProt causal check | passed | True | GO:0160201 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native pusule UniProt verify check | passed | True | cellstructuremech:pusule | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native pusule UniProt causal check | passed | True | cellstructuremech:pusule | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native pyrenoid tubule UniProt verify check | passed | True | GO:0160223 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native pyrenoid tubule UniProt causal check | passed | True | GO:0160223 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native recycling endosome UniProt verify check | passed | True | GO:0055037 | 0 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native recycling endosome UniProt causal check | passed | True | GO:0055037 | 0 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native recycling endosome lumen UniProt verify check | passed | True | GO:0034777 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native recycling endosome lumen UniProt causal check | passed | True | GO:0034777 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |

## Scientific And Domain Assessments

### Original native validation/render and frozen inputs

schema: supported. Targets: GO:0160223.

Original validate/render pass and Markdown is exact. Every frozen historical input hash was checked; current target equals original frozen target. No staleness refresh is needed for these three targets.

### Exact identity and parent/part boundaries

identity: supported. Targets: GO:0160223.

GO0160223 exact specialized traversing membrane, GO1990732 parthood and GO0042651 continuity; membrane classification is supported by definition and primary anatomy. No direct full-ancestry query result is claimed.

### Definition and explicit biological scope

scope: supported. Targets: GO:0160223.

Definition is membrane topology; nonuniversality across pyrenoids is retained. Rubisco-matrix context does not turn the target into whole pyrenoid or a protein.

### Actual host/strain, life stage and occurrence

scope: supported. Targets: GO:0160223.

Chlamydomonas tax3055 matches Engel CC124(137c) and Franklin species context. Eukaryota RARE is qualitative lineage restriction, not a measured prevalence rate; He supports pyrenoid/tubule diversity and exceptions.

### Canonical experimental observation

evidence: supported. Targets: GO:0160223.

Engel primary cryoET resolves parallel minitubules and distinction of their stromal lumen from surrounding thylakoid-continuous tubule lumen. Source text captions read; pixels/tomograms not inspected.

### Material component versus whole structure

grounding: supported. Targets: GO:0160223.

Collective REVIEWED_LABEL_ONLY lipid material is explicit and no guessed chemical species or whole-structure GO is supplied as its chemical grounding. Generic constitutive bilayer is distinct from individual lipid necessity.

### Function, assay scope and molecular necessity

evidence: supported. Targets: GO:0160223.

Qualified thought-to-support CO2 delivery matches the explicitly secondary He model and Franklin Intro/Discussion. Proteomic fragment enrichment/localization is not direct interaction or every candidate being formation-essential.

### Complete graph scope and represented actors

graph: supported. Targets: GO:0160223.

NONMECHANISTIC three-edge graph captures parthood, thylakoid continuity and traversal. Omitted bicarbonate channels/carbonic anhydrase/diffusion actors are explicitly outside graph scope, not a hidden promised mechanism.

### Represented protein identity and class limits

grounding: not_applicable. Targets: GO:0160223.

No maintained individual protein accession or typed gene/protein actor exists. The positive Rubisco narrative is assessed within its source scope without inventing mandatory protein examples.

### Actual native protein checks and coverage

provenance: supported. Targets: GO:0160223.

Two actual native commands exit0. Zero examples and zero typed molecular nodes; generic verification stdout alone was not used to infer inventory counts. Native validity does not prove exhaustive membership, localization or necessity.

### Complete-record structured-source applicability

scope: supported. Targets: GO:0160223.

Positive Rubisco/CO2-delivery function triggers source applicability despite topological graph. Complete fresh catalogue lacks the actual eukaryotic hosts. Use scoped primary/authority fallback, without cyanobacterial proxy or unjustified downstream query. This corrects the old expression-only exemption; historical00:49Z runner failure is not a new run.

### Discussion/history and bounded neighbor context

provenance: supported. Targets: GO:0160223.

Open label-only lipid-grounding TODO remains open; resolved nonuniversality rationale is consistent with anatomical context. No mandatory universal whole-pyrenoid has_part is inferred. All records remain PROPOSED; no record mutation, whole-neighbor verdict or grouped-issue resolution is claimed.

### Unresolved formation and exhaustive molecular composition

completeness: unknown. Targets: GO:0160223.

Inspected sources establish scoped anatomy/localization and selected physiological effects. They do not establish an exhaustive formation machinery, invariant lipid composition or every molecular actor necessary across taxa. Optional protein examples are not mandatory solely because literature names proteins.

### Images, quantitative and other unasserted domains

scope: not_applicable. Targets: GO:0160223.

No maintained image/license claim, numerical measurement, associated-trait mapping or verbatim snippet in this target. Text captions are distinct from inspected image pixels, and no unseen source pixels/raw data/supplements are certified.

### Scientific verdict and exact lineage

completeness: supported. Targets: GO:0160223.

pass_with_limitations: no scientific finding established, within stated source-access and composition/necessity limits. No new scientific finding or terminal historical finding disposition is invented. Applicability bundle defect is separately corrected.

### Original native validation/render and frozen inputs

schema: supported. Targets: GO:0055037.

Original validate/render pass and Markdown is exact. Every frozen historical input hash was checked; current target equals original frozen target. No staleness refresh is needed for these three targets.

### Exact identity and parent/part boundaries

identity: supported. Targets: GO:0055037.

GO0055037 exact organelle identity, GO0005768 is-a and two distinct membrane/lumen parts remain supported; SL0232 is an exact xref with its own typed location relation.

### Definition and explicit biological scope

scope: supported. Targets: GO:0055037.

Ontology definition describes a recycling network rather than a fixed molecular complex. Rab11 marks and regulates studied host compartments without becoming a compulsory material constituent.

### Actual host/strain, life stage and occurrence

scope: supported. Targets: GO:0055037.

Trypanosoma tax5691 is valid. Jeffries complete abstract supports bloodstream/procyclic compartments and a more elaborate bloodstream compartment; VARIABLE is stage/context qualification rather than demonstrated all-strain prevalence. Umaer Methods specify bloodstream single-marker T. b. brucei; no extrapolation to all life stages.

### Canonical experimental observation

evidence: supported. Targets: GO:0055037.

Jeffries abstract directly reports Rab11 colocalization with transferrin receptor and internalized anti-VSG cargo. This supports the compartment example without reclassifying receptor as lumen cargo.

### Material component versus whole structure

grounding: concern. Targets: GO:0055037.

Inherited major F1 persists: LIPID component is grounded to GO0055038 whole membrane and linked by component_ref. Correct membrane topology does not turn a structural GO term into molecular lipid identity.

### Function, assay scope and molecular necessity

evidence: supported. Targets: GO:0055037.

Current coarse selective/Rab11-dependent recycling wording is compatible with source-specific observations. Pal abstract includes extensive degradation/product exocytosis, not intact ligand return; Umaer directly distinguishes affected ISG65 from largely unaffected VSG/TfR. No universal cargo or organelle-formation necessity is claimed.

### Complete graph scope and represented actors

graph: concern. Targets: GO:0055037.

NONMECHANISTIC six-edge graph contains subtype, membrane/lumen parthood, boundary, Rab11 localization and selective recycling support. External Rab11 actor is permitted; inherited F1 concerns only the membrane component linkage, not correct topology or complete-mechanism omission.

### Represented protein identity and class limits

grounding: supported. Targets: GO:0055037.

Q9NJE8 is current unreviewed T. brucei Rab11 with primary gene Rab11 and RAB11A synonym. Sequence-source references include Jeffries; inferred family annotations are not localization experiments. No sequence alignment to Umaer RNAi construct or universal strain correspondence was performed.

### Actual native protein checks and coverage

provenance: supported. Targets: GO:0055037.

Two actual native commands exit0. Zero examples and one UNANCHORED_WITH_UNIPROT external Rab11 node, not COVERED; absence of component_ref is intentional and no mandatory constituent inference follows. Native validity does not prove exhaustive membership, localization or necessity.

### Complete-record structured-source applicability

scope: supported. Targets: GO:0055037.

Positive Rab11 cargo-recycling biology triggers source applicability. Complete fresh catalogue lacks the actual eukaryotic hosts. Use scoped primary/authority fallback, without cyanobacterial proxy or unjustified downstream query. This corrects the old expression-only exemption; historical00:49Z runner failure is not a new run.

### Discussion/history and bounded neighbor context

provenance: supported. Targets: GO:0055037.

Historical Rab11 marker-not-component interpretation remains intact; correcting F1 does not require rewriting dated rationale or moving Rab11 into components. All records remain PROPOSED; no record mutation, whole-neighbor verdict or grouped-issue resolution is claimed.

### Unresolved formation and exhaustive molecular composition

completeness: unknown. Targets: GO:0055037.

Inspected sources establish scoped anatomy/localization and selected physiological effects. They do not establish an exhaustive formation machinery, invariant lipid composition or every molecular actor necessary across taxa. Optional protein examples are not mandatory solely because literature names proteins.

### Images, quantitative and other unasserted domains

scope: not_applicable. Targets: GO:0055037.

No maintained image/license claim, numerical measurement, associated-trait mapping or verbatim snippet in this target. Text captions are distinct from inspected image pixels, and no unseen source pixels/raw data/supplements are certified.

### Scientific verdict and exact lineage

completeness: concern. Targets: GO:0055037.

needs_curation: inherited major F1/key remains confirmed; record curation stays outside this PR. No new scientific finding or terminal historical finding disposition is invented. Applicability bundle defect is separately corrected.

### Original native validation/render and frozen inputs

schema: supported. Targets: GO:0034777.

Original validate/render pass and Markdown is exact. Every frozen historical input hash was checked; current target equals original frozen target. No staleness refresh is needed for these three targets.

### Exact identity and parent/part boundaries

identity: supported. Targets: GO:0034777.

GO0034777 exact enclosed volume, GO0031904 is-a, GO0055037 parthood and exact SL0345 synonym remain supported. Boundary membrane is not a lumen constituent.

### Definition and explicit biological scope

scope: supported. Targets: GO:0034777.

Definition/function is physical compartmentalization. Positive TbRAB11 compartment examples are contextual localization, not a claimed lumen-resident receptor or molecular routing mechanism.

### Actual host/strain, life stage and occurrence

scope: supported. Targets: GO:0034777.

Trypanosoma tax5691 is valid. Jeffries complete abstract supports bloodstream/procyclic compartments and a more elaborate bloodstream compartment; VARIABLE is stage/context qualification rather than demonstrated all-strain prevalence. No dedicated lumen proteome or exact experimental strain is inferred from the accessible Jeffries abstract.

### Canonical experimental observation

evidence: supported. Targets: GO:0034777.

Rab11-positive endosomal compartments instantiate a membrane-enclosed volume by anatomical inference; Jeffries is not claimed to have isolated and characterized a lumen-specific molecular inventory.

### Material component versus whole structure

grounding: supported. Targets: GO:0034777.

No constituent molecular inventory is asserted; surrounding membrane remains a separate boundary node. No obligatory protein or lipid example is invented.

### Function, assay scope and molecular necessity

evidence: supported. Targets: GO:0034777.

Physical lumen compartmentalization is supported by exact ontology definition. Current function does not assert that the lumen independently routes cargo or that transferrin receptor is a luminal soluble cargo.

### Complete graph scope and represented actors

graph: supported. Targets: GO:0034777.

NONMECHANISTIC three-edge graph captures lumen is-a, whole-organelle parthood and boundary. It expressly excludes Rab11/tether/coat/cargo-selection mechanisms; their absence is not an incomplete promised mechanism.

### Represented protein identity and class limits

grounding: not_applicable. Targets: GO:0034777.

No maintained individual protein accession or typed gene/protein actor exists. The positive Rab11 narrative is assessed within its source scope without inventing mandatory protein examples.

### Actual native protein checks and coverage

provenance: supported. Targets: GO:0034777.

Two actual native commands exit0. Zero examples and zero typed molecular nodes; generic verification stdout alone was not used to infer inventory counts. Native validity does not prove exhaustive membership, localization or necessity.

### Complete-record structured-source applicability

scope: supported. Targets: GO:0034777.

Positive TbRAB11-marked host-compartment narrative triggers applicability despite the physical lumen function and expressly excluded graph mechanism. Complete fresh catalogue lacks the actual eukaryotic hosts. Use scoped primary/authority fallback, without cyanobacterial proxy or unjustified downstream query. This corrects the old expression-only exemption; historical00:49Z runner failure is not a new run.

### Discussion/history and bounded neighbor context

provenance: supported. Targets: GO:0034777.

Current boundary-not-component interpretation and compartmentalization function preserve historical correction without claiming new disposal of prior issues. All records remain PROPOSED; no record mutation, whole-neighbor verdict or grouped-issue resolution is claimed.

### Unresolved formation and exhaustive molecular composition

completeness: unknown. Targets: GO:0034777.

Inspected sources establish scoped anatomy/localization and selected physiological effects. They do not establish an exhaustive formation machinery, invariant lipid composition or every molecular actor necessary across taxa. Optional protein examples are not mandatory solely because literature names proteins.

### Images, quantitative and other unasserted domains

scope: not_applicable. Targets: GO:0034777.

No maintained image/license claim, numerical measurement, associated-trait mapping or verbatim snippet in this target. Text captions are distinct from inspected image pixels, and no unseen source pixels/raw data/supplements are certified.

### Scientific verdict and exact lineage

completeness: supported. Targets: GO:0034777.

pass_with_limitations: no scientific finding established, within stated source-access and composition/necessity limits. No new scientific finding or terminal historical finding disposition is invented. Applicability bundle defect is separately corrected.

### Historical input integrity and native represented protein coverage

schema: supported. Targets: GO:0160201.

Both original pairs validate/render exactly and all27 historical inputs match. Current record has0examples/0typed protein nodes, so native protein success is an empty-inventory check. Root owns full current corpus/publication gates.

### Historical input integrity and native represented protein coverage

schema: supported. Targets: cellstructuremech:pusule.

Both original pairs validate/render exactly and all27 historical inputs match. Current record has0examples/0typed protein nodes, so native protein success is an empty-inventory check. Root owns full current corpus/publication gates.

### Polaroplast versus polar tube and nascent sporoplasm

identity: supported. Targets: GO:0160201.

Exact active GO0160201 denotes polaroplast. GO0044099 is a separate conduit, not record identity. Pressure phrasing follows the authority; sources qualify detailed firing mechanism.

### Aggregate membrane and anterior/posterior subregions

grounding: supported. Targets: GO:0160201.

Three LIPID rows explicitly denote aggregate membrane material/anatomical subregions and carry reviewed-label-only status; no whole-organelle CURIE is misrepresented as a lipid species. Han describes lamellar arrays, flattened tubules and posterior polaroplast, while Lv introduction describes lamellae/chambers/tubules. This is not an exhaustive molecular or stoichiometric inventory.

### Current added anatomical nodes and edges

graph: supported. Targets: GO:0160201.

Substantive refresh supports anterior_lamellar_polaroplast and posterior_tubular_polaroplast STRUCTURE component_refs and their part_of edges to the aggregate membrane system. They restate supported anatomical membership, not a new necessary molecular mechanism. Current graph has6nodes/5edges; old4nodes/3edges review remains historical.

### Microsporidia prevalence and Nosema example

scope: supported. Targets: GO:0160201.

COMMON is qualitative conserved-invasion-apparatus review scope, not measured prevalence. Direct membrane contribution study is N.bombycis CQ1, silkworm propagated with KOH-induced germination and BmE context. Species example does not generalize assay timing or marker distribution to all microsporidia.

### Physical membrane transfer and firing support

evidence: supported. Targets: GO:0160201.

Fixed-stage membrane and protein-marker distributions, cryo/TEM cargo and lipid analyses support coarse membrane movement/contribution to nascent sporoplasm. Current NONMECHANISTIC function graph and softened contribute_to edge do not identify force-generating molecules or prove exclusive origin. tracked/visualized is read as these bounded observational experiments, not continuous single-membrane tracing.

### Formation and molecular machinery

evidence: unknown. Targets: GO:0160201.

No exact protein/lipid inventory or essentiality is asserted. Surface-marker localization in Lv is not a necessary transport or formation mechanism. Open molecular-grounding TODO is appropriate; no mandatory optional-inventory finding.

### Structured-source applicability of a physical membrane graph

scope: not_applicable. Targets: GO:0160201.

Current positive assertions are membrane anatomy, physical discharge and material contribution; no named gene, molecular pathway/regulator, stress-response trait or transcriptomics dataset is asserted. Unassigned transporters/surface proteins are an explicit future TODO, not positive molecular membership. Thus genuine exclusion remains, clarified beyond original expression-only stock wording. Full current catalogue has no matched Microsporidia/Nosema host; no foreign proxy or biological absence claim.

### Primary versus secondary source tiers

provenance: supported. Targets: GO:0160201.

Exact DOI/title/author/year verified. Han and Chen are secondary scope; Lv primary methods/results are independently inspected in declared sections without figure-pixel/supplement audit. Existing historical resolution is not newly claimed work.

### Current polaroplast verdict

consistency: supported. Targets: GO:0160201.

Qualified pass remains warranted after source-grounded stale refresh; no scientific finding or request_curation action is established. Review-input staleness is a bundle defect fixed by linked current-input follow-up, not a record edit.

### Pusule identity and surface-connected topology

identity: supported. Targets: cellstructuremech:pusule.

Local identifier avoids adopting a broader term. Dodge publisher summary directly supports variable canal-connected sac/tubule/vesicle apparatus with apposed plasma/vacuolar membranes. GO membrane-bounded-organelle parent does not require sealed lumen; bounded QuickGO search returns0 exact name hits without asserting exhaustive nonexistence.

### Whole-membrane material and unknown necessity

grounding: supported. Targets: cellstructuremech:pusule.

OTHER membrane component with GO0016020 denotes the whole pusular wall, not a chemical lipid identity. UNKNOWN essentiality avoids inferring an assembly requirement from mature morphology. No protein named solely as a tracer is treated as an endogenous constituent.

### Three species and experimental contexts

scope: supported. Targets: cellstructuremech:pusule.

Exact taxa verified. Gavelis studies wild-collected P.kofoidii pseudocolonies; Klut deposited abstract identifies P.micans and A.carterae with tracer/serial TEM scope. Neither example establishes universal dinoflagellate prevalence, a laboratory strain, or same physiological mechanism.

### Tracer access versus molecular transport

evidence: supported. Targets: cellstructuremech:pusule.

HRP/ferritin/lectin entry through the flagellar canal supports lumen access only. Full-text controls were not independently available in the evidence used. Record explicitly keeps osmoregulation, secretion and collar/flagellum flow provisional and imports no transport function/causal graph or assimilation assertion.

### Pusule versus adjacent nuclear and vacuolar structures

identity: supported. Targets: cellstructuremech:pusule.

Pusule orange reconstruction is distinct from blue nucleus, green ribbon and flagellar rootlets. Frozen nuclear-net and contractile-vacuole identity fields provide bounded local context; they are not re-reviewed or resolved.

### Maintained figure pixels, caption, authors and license

provenance: supported. Targets: cellstructuremech:pusule.

Maintained Fig2 bytes equal fresh versioned PMC download and declared SHA/MD5. Actual pixels agree with TEM D, FIB-SEM E and contextual G/H; source caption supports bar values. Eight-author attribution and CC BY4.0 permissions are explicit with no separate exclusion. OTHER accurately represents mixed panels; no unsupported quantitative measurement.

### Structured-source genuine physical exclusion

scope: not_applicable. Targets: cellstructuremech:pusule.

Actual record remains anatomy/material/image scope; tracer proteins are assay reagents and proposed physiology is explicitly unresolved. No positive molecular/pathway/stress-response assertion triggers a required matched-gene analysis. Original stock expression wording is clarified but not counted as an unsupported-exclusion defect. Official catalogue has no named dinoflagellate host; no foreign proxy is used.

### Accurate bounded source access and immutable history

provenance: supported. Targets: cellstructuremech:pusule.

Dodge primary publisher Summary only; Klut primary deposited abstract only; Gavelis declared primary Results/Methods/caption/image/license. Past failed publisher accesses remain historical claims, not invented new failures. Current fresh successful summary/JATS access does not upgrade unread full sources.

### Current pusule verdict

consistency: supported. Targets: cellstructuremech:pusule.

Qualified pass remains warranted; no inherited or new scientific finding/request_curation action. Unresolved optional physiology and molecular details remain limitations. No neighbor/group disposition is inferred.

### Exact class and compartment boundaries

identity: supported. Targets: GO:0009527.

ExactGO9527 outer cytoplasm-facing bilayer, GO42170 is_a and envelope parthood/SL0214 synonyms; primary-green context bounded from extra membranes in complex plastids.

### Chemical material versus whole anatomical part

grounding: supported. Targets: GO:0009527.

Collective label-only bilayer explicitly avoids grounding chemical material to whole membrane. Corresponding STRUCTURE node denotes membrane; no erroneous chemical species/ratio asserted.

### Formation necessity at exact asserted level

evidence: unknown. Targets: GO:0009527.

Collective bilayer is defining material where asserted. Native anatomy, mature cryoET morphology and secondary synthesis do not establish necessity of each lipid species, photosystem, transporter or assembly protein. Matrix/lumen have no fixed necessary constituents.

### Every current graph edge and source scope

graph: supported. Targets: GO:0009527.

Three NONMECHANISTIC edges: envelope parthood, faces cytoplasm and bounds envelopeIMS. Descriptive GO/SL anatomy, not universal TOC–TIC machinery.

### Verified identities and bounded occurrence

scope: supported. Targets: GO:0009527.

Current Eukaryota/Viridiplantae/C.reinhardtii identities match; Keeling supports primary/secondary/reduced plastid distributions. Presence categories qualitative, not measured frequencies or universal import machinery.

### Canonical example and actual source access

evidence: supported. Targets: GO:0009527.

Current Jin primary abstract/indexed species supports C.reinhardtii TOC–TIC spanning envelope, not exact strain/full Methods/model or universal machinery.

### Whole-record structured-source applicability

evidence: concern. Targets: GO:0009527.

Original explicit expression-only N/A check is unsupported because whole record positively asserts TOC–TIC protein import. Fresh official catalogue has no matching green-algal/glaucophyte host; no unrelated cyanobacterial proxy or downstream query.

### Historical rationale/source-tier distinctions

provenance: supported. Targets: GO:0009527.

Historical rationale/status/grounding tasks retained; optional molecular-grounding TODOs not automatically resolved by whole-membrane identity. No broader/category/neighbor issue disposition.

### Frozen-input and native scope validation

schema: supported. Targets: GO:0009527.

All76 original frozen input hashes agree; five originalpairs validate and render exactly; assigned target unchanged. Actual ten native protein commands pass with zeroexamples/zeroGENE_OR_PROTEINnodes, not exhaustive biological coverage.

### Full record and qualified verdict

completeness: supported. Targets: GO:0009527.

Every maintained field/source placement/graph/history/discussion reviewed. No local images, physical-property measurements, verbatim snippets or individual accessions asserted. No confirmed scientific finding; qualified positive assessment retains stated access/experiment limits.

### Exact class and compartment boundaries

identity: supported. Targets: GO:0009532.

ExactGO9532 proteinaceous ground substance supports maintained paraphrase;SL0215 exact synonym and plastid parthood; matrix excludes thylakoid lumen and envelopeIMS.

### Chemical material versus whole anatomical part

grounding: supported. Targets: GO:0009532.

No fixed components on this volume/matrix record; variable cargo and optional proteins are not forced.

### Formation necessity at exact asserted level

evidence: unknown. Targets: GO:0009532.

Collective bilayer is defining material where asserted. Native anatomy, mature cryoET morphology and secondary synthesis do not establish necessity of each lipid species, photosystem, transporter or assembly protein. Matrix/lumen have no fixed necessary constituents.

### Every current graph edge and source scope

graph: supported. Targets: GO:0009532.

One NONMECHANISTIC plastid contains stroma relation; no fixed universal matrix-protein inventory.

### Verified identities and bounded occurrence

scope: supported. Targets: GO:0009532.

Current Eukaryota/Viridiplantae/C.reinhardtii identities match; Keeling supports primary/secondary/reduced plastid distributions. Presence categories qualitative, not measured frequencies or universal import machinery.

### Canonical example and actual source access

evidence: supported. Targets: GO:0009532.

Terashima secondary pages151–154 support broad Chlamydomonas chloroplast proteome/metabolic/protein-biogenesis context. No purified Chlamydomonas stromal proteome or individual cargo localization is inferred; Arabidopsis fraction results remain separate.

### Whole-record structured-source applicability

evidence: concern. Targets: GO:0009532.

Original explicit expression-only N/A check is unsupported because whole record positively asserts metabolic/protein-biogenesis proteins in Chlamydomonas stroma. Fresh official catalogue has no matching green-algal/glaucophyte host; no unrelated cyanobacterial proxy or downstream query.

### Historical rationale/source-tier distinctions

provenance: supported. Targets: GO:0009532.

Historical rationale/status/grounding tasks retained; optional molecular-grounding TODOs not automatically resolved by whole-membrane identity. No broader/category/neighbor issue disposition.

### Frozen-input and native scope validation

schema: supported. Targets: GO:0009532.

All76 original frozen input hashes agree; five originalpairs validate and render exactly; assigned target unchanged. Actual ten native protein commands pass with zeroexamples/zeroGENE_OR_PROTEINnodes, not exhaustive biological coverage.

### Full record and qualified verdict

completeness: supported. Targets: GO:0009532.

Every maintained field/source placement/graph/history/discussion reviewed. No local images, physical-property measurements, verbatim snippets or individual accessions asserted. No confirmed scientific finding; qualified positive assessment retains stated access/experiment limits.

### Exact class and compartment boundaries

identity: supported. Targets: GO:0031976.

ExactGO31976 whole thylakoid in plastid, parentGO9579/plastid parthood and distinct membrane/lumen parts. OTHER kind respects native non-organelle comment without conflating filesystem category.

### Chemical material versus whole anatomical part

grounding: concern. Targets: GO:0031976.

Inherited majorF1 confirmed: LIPID component identity is entireGO55035 membrane and graphcomponent_ref propagates mismatch. Preserve true boundary/has_part and accurate structural or label-only material alternatives.

### Formation necessity at exact asserted level

evidence: unknown. Targets: GO:0031976.

Collective bilayer is defining material where asserted. Native anatomy, mature cryoET morphology and secondary synthesis do not establish necessity of each lipid species, photosystem, transporter or assembly protein. Matrix/lumen have no fixed necessary constituents.

### Every current graph edge and source scope

graph: supported. Targets: GO:0031976.

Three NONMECHANISTIC edges: membrane bounds lumen, supports oxygenic light reactions and part_of whole thylakoid. Valid topology/function retained independently of F1 material/structure component_ref mismatch.

### Verified identities and bounded occurrence

scope: supported. Targets: GO:0031976.

Current Viridiplantae/Glaucocystophyceae/C.reinhardtii identities match. Native cyanelle classes plusSL0082 establish glaucophyte subtype; secondary review supports photosynthetic green lineages. COMMON remains qualitative rather than measured prevalence.

### Canonical example and actual source access

evidence: supported. Targets: GO:0031976.

Engel primary body directly supports native membrane/lumen cryoET example in CC124(137c), with TAP/constant light/air and43tomograms/27lamellae scoped. No quantitative property is copied to generic record; universal continuity and transport hypotheses not promoted.

### Whole-record structured-source applicability

evidence: concern. Targets: GO:0031976.

Original prose-only photosynthesis-versus-expression exclusion is unsupported because whole record positively asserts photosynthetic light-reaction complexes/pathway. Fresh official catalogue has no matching green-algal/glaucophyte host; no unrelated cyanobacterial proxy or downstream query.

### Historical rationale/source-tier distinctions

provenance: concern. Targets: GO:0031976.

Original Perez browser passages and HTTP403 route are mislabeled primary_source despite secondary/access-limit prose. Successor explicitly uses secondary authority/context and separates route failure from scientific primary evidence; historical observations retained.

### Frozen-input and native scope validation

schema: supported. Targets: GO:0031976.

All76 original frozen input hashes agree; five originalpairs validate and render exactly; assigned target unchanged. Actual ten native protein commands pass with zeroexamples/zeroGENE_OR_PROTEINnodes, not exhaustive biological coverage.

### Full record and qualified verdict

completeness: supported. Targets: GO:0031976.

Every maintained field/source placement/graph/history/discussion reviewed. No local images, physical-property measurements, verbatim snippets or individual accessions asserted. One inherited majorF1/action retained, no new scientific finding.

### Exact class and compartment boundaries

identity: supported. Targets: GO:0031978.

ExactGO31978 enclosed lumen with parentGO31977 and whole-thylakoid parthood; no boundary membrane misidentified as lumen component.

### Chemical material versus whole anatomical part

grounding: supported. Targets: GO:0031978.

No fixed components on this volume/matrix record; variable cargo and optional proteins are not forced.

### Formation necessity at exact asserted level

evidence: unknown. Targets: GO:0031978.

Collective bilayer is defining material where asserted. Native anatomy, mature cryoET morphology and secondary synthesis do not establish necessity of each lipid species, photosystem, transporter or assembly protein. Matrix/lumen have no fixed necessary constituents.

### Every current graph edge and source scope

graph: supported. Targets: GO:0031978.

Two NONMECHANISTIC edges: lumen part_of thylakoid and membrane encloses lumen. No proton concentration/transport machinery or cargo inventory is asserted.

### Verified identities and bounded occurrence

scope: supported. Targets: GO:0031978.

Current Viridiplantae/Glaucocystophyceae/C.reinhardtii identities match. Native cyanelle classes plusSL0082 establish glaucophyte subtype; secondary review supports photosynthetic green lineages. COMMON remains qualitative rather than measured prevalence.

### Canonical example and actual source access

evidence: supported. Targets: GO:0031978.

Engel primary body directly supports native membrane/lumen cryoET example in CC124(137c), with TAP/constant light/air and43tomograms/27lamellae scoped. No quantitative property is copied to generic record; universal continuity and transport hypotheses not promoted.

### Whole-record structured-source applicability

evidence: not_applicable. Targets: GO:0031978.

Genuine physical exclusion: maintained lumen is anatomical enclosed volume and cryoET morphology; explicit scope withholds lumenal proteins/proton transport. Cited paper background does not create a positive pathway claim on this record.

### Historical rationale/source-tier distinctions

provenance: concern. Targets: GO:0031978.

Original Perez browser passages and HTTP403 route are mislabeled primary_source despite secondary/access-limit prose. Successor explicitly uses secondary authority/context and separates route failure from scientific primary evidence; historical observations retained.

### Frozen-input and native scope validation

schema: supported. Targets: GO:0031978.

All76 original frozen input hashes agree; five originalpairs validate and render exactly; assigned target unchanged. Actual ten native protein commands pass with zeroexamples/zeroGENE_OR_PROTEINnodes, not exhaustive biological coverage.

### Full record and qualified verdict

completeness: supported. Targets: GO:0031978.

Every maintained field/source placement/graph/history/discussion reviewed. No local images, physical-property measurements, verbatim snippets or individual accessions asserted. No confirmed scientific finding; qualified positive assessment retains stated access/experiment limits.

### Exact class and compartment boundaries

identity: supported. Targets: GO:0055035.

ExactGO55035 lipid bilayer of a plastid thylakoid, parentGO42651 and whole-thylakoid parthood. Chloroplast/cyanelle native child relations; organellar chromatophore classification supported separately bySL0356, not invented GO edge.

### Chemical material versus whole anatomical part

grounding: supported. Targets: GO:0055035.

Collective label-only bilayer explicitly avoids grounding chemical material to whole membrane. Corresponding STRUCTURE node denotes membrane; no erroneous chemical species/ratio asserted.

### Formation necessity at exact asserted level

evidence: unknown. Targets: GO:0055035.

Collective bilayer is defining material where asserted. Native anatomy, mature cryoET morphology and secondary synthesis do not establish necessity of each lipid species, photosystem, transporter or assembly protein. Matrix/lumen have no fixed necessary constituents.

### Every current graph edge and source scope

graph: supported. Targets: GO:0055035.

Two NONMECHANISTIC edges: membrane bounds lumen and supports light reactions. Source secondary synthesis supports oxygenic electron transfer/proton gradient; not complete pathway stoichiometry or individual assembly requirements.

### Verified identities and bounded occurrence

scope: supported. Targets: GO:0055035.

Current Viridiplantae/Glaucocystophyceae/C.reinhardtii identities match. Native cyanelle classes plusSL0082 establish glaucophyte subtype; secondary review supports photosynthetic green lineages. COMMON remains qualitative rather than measured prevalence.

### Canonical example and actual source access

evidence: supported. Targets: GO:0055035.

Engel primary body directly supports native membrane/lumen cryoET example in CC124(137c), with TAP/constant light/air and43tomograms/27lamellae scoped. No quantitative property is copied to generic record; universal continuity and transport hypotheses not promoted.

### Whole-record structured-source applicability

evidence: concern. Targets: GO:0055035.

Original prose-only photosynthesis-versus-expression exclusion is unsupported because whole record positively asserts photosynthetic light-reaction complexes/pathway. Fresh official catalogue has no matching green-algal/glaucophyte host; no unrelated cyanobacterial proxy or downstream query.

### Historical rationale/source-tier distinctions

provenance: concern. Targets: GO:0055035.

Original Perez browser passages and HTTP403 route are mislabeled primary_source despite secondary/access-limit prose. Successor explicitly uses secondary authority/context and separates route failure from scientific primary evidence; historical observations retained.

### Frozen-input and native scope validation

schema: supported. Targets: GO:0055035.

All76 original frozen input hashes agree; five originalpairs validate and render exactly; assigned target unchanged. Actual ten native protein commands pass with zeroexamples/zeroGENE_OR_PROTEINnodes, not exhaustive biological coverage.

### Full record and qualified verdict

completeness: supported. Targets: GO:0055035.

Every maintained field/source placement/graph/history/discussion reviewed. No local images, physical-property measurements, verbatim snippets or individual accessions asserted. No confirmed scientific finding; qualified positive assessment retains stated access/experiment limits.

### Complete frozen-input comparison and bounded refresh

provenance: supported. Targets: GO:0009527, GO:0009532, GO:0031976, GO:0031978, GO:0055035, GO:0160201, cellstructuremech:pusule, GO:0160223, GO:0055037, GO:0034777.

1 of ten original target hashes differ from current main. The changed content is substantively reassessed in the target-specific assessments; original observations remain historical and unchanged. All current target and used context bytes are frozen.

## Findings

### septin-recycling_endosome-F1: Separate whole-membrane structure from molecular lipid grounding

major / open / confirmed; issue key: recycling-endosome-lipid-whole-membrane-grounding.

The LIPID component uses GO0055038 for the entire membrane and the graph links that node through component_ref. GO identifies the structural boundary, not a molecular lipid class. Valid membrane parthood does not repair this explicit type/grounding mismatch.

### micro-F1: Separate the whole membrane part from its lipid material identity

major / open / confirmed; issue key: plastid-thylakoid-membrane-lipid-identity.

components[0] is typed LIPID but grounded to GO0055035, which identifies the complete plastid thylakoid membrane. The exact GO definition includes a lipid bilayer as a structure; it is not an identifier for a molecular lipid constituent. The membrane graph node links back through component_ref. Preserve correct has_part and boundary topology while either representing this complete membrane as an accurately typed structural constituent or representing the collective lipid material without using the whole-membrane GO identity.

## Recommended Actions And Acceptance Checks

### septin-recycling_endosome-A1

Retain the valid membrane structural node and has_part. Represent collective lipid material with an honest label-only or justified chemical grounding, or explicitly represent the intended structural subpart with an appropriate type; align component_ref with that choice.

- No LIPID molecular row is grounded to the whole membrane GO identity.
- Correct membrane/lumen topology and Rab11 external-regulator distinction remain intact.
- No exact lipid species or obligatory protein inventory is invented.
- Focused native schema, strict, identifier, graph and history checks pass after separately authorized curation.

### micro-A1

In separately authorized curation, distinguish the whole membrane structural part from its collective lipid material, align component type/grounding and the component_ref join, and retain correct whole/part topology.

- The LIPID identity no longer denotes a whole membrane GO class; an accurate OTHER structural constituent remains permissible.
- Boundary, light-reaction and taxon claims remain supported at their existing scope.
- Native schema, strict, CURIE, graph and history checks pass.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| current-record-0 | data/structures/membrane_organelle/plastid_outer_membrane.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 59bd8548931d27f711233f542b5f927c0e7b0a68dd611eabb4777ee08003deaa; current SHA256 59bd8548931d27f711233f542b5f927c0e7b0a68dd611eabb4777ee08003deaa. Record bytes unchanged since the original review. |
| original-review-0 | reviews/structured/20261022T032956Z-plastid-outer-membrane-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-1 | data/structures/membrane_organelle/plastid_stroma.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 86d19307cbe21273498f0d7d6741e61f5ebf002cf78418c34b922d9d4963503b; current SHA256 86d19307cbe21273498f0d7d6741e61f5ebf002cf78418c34b922d9d4963503b. Record bytes unchanged since the original review. |
| original-review-1 | reviews/structured/20261022T032957Z-plastid-stroma-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-2 | data/structures/membrane_organelle/plastid_thylakoid.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 ec3c74ee89bf25eea6a3a5682b3f7f73e0837465dccf2a8f2c0cce1550a4e3c8; current SHA256 ec3c74ee89bf25eea6a3a5682b3f7f73e0837465dccf2a8f2c0cce1550a4e3c8. Record bytes unchanged since the original review. |
| original-review-2 | reviews/structured/20261022T032958Z-plastid-thylakoid-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-3 | data/structures/membrane_organelle/plastid_thylakoid_lumen.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 7a75c5aee47a20bbae7da6351e07fc7f2d1dc418e7ca34e253d08e3a531ff4ee; current SHA256 7a75c5aee47a20bbae7da6351e07fc7f2d1dc418e7ca34e253d08e3a531ff4ee. Record bytes unchanged since the original review. |
| original-review-3 | reviews/structured/20261022T032959Z-plastid-thylakoid-lumen-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-4 | data/structures/membrane_organelle/plastid_thylakoid_membrane.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 51a2ece521e1b5c0b3b589fc7cf665be1c9544299257e0fda7fcf8352e7401c2; current SHA256 51a2ece521e1b5c0b3b589fc7cf665be1c9544299257e0fda7fcf8352e7401c2. Record bytes unchanged since the original review. |
| original-review-4 | reviews/structured/20261022T033000Z-plastid-thylakoid-membrane-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-5 | data/structures/membrane_organelle/polaroplast.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 b755d59c2ad21e4b73e222a7d9979859a4d4b5c3c9f4543f9695dc3749beff69; current SHA256 33a7618c43eea5924263584a6faa84d6190ff1198bfdb1ca2903d49e726c2642. Changed record reassessed against current sources. |
| original-review-5 | reviews/structured/20261022T033000Z-polaroplast-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-6 | data/structures/membrane_organelle/pusule.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 3bc5082b5e3b721414b9b2d57c585c1a278de5053885f34f55b40ccd4b71a6ae; current SHA256 3bc5082b5e3b721414b9b2d57c585c1a278de5053885f34f55b40ccd4b71a6ae. Record bytes unchanged since the original review. |
| original-review-6 | reviews/structured/20261022T033001Z-pusule-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-7 | data/structures/membrane_organelle/pyrenoid_tubule.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 dd5c61f94612f6c30f259f029b7f4bc4daa8a7d4c0fa8111f6eb0715f78483d7; current SHA256 dd5c61f94612f6c30f259f029b7f4bc4daa8a7d4c0fa8111f6eb0715f78483d7. Record bytes unchanged since the original review. |
| original-review-7 | reviews/structured/20261022T033002Z-pyrenoid-tubule-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-8 | data/structures/membrane_organelle/recycling_endosome.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 7a806e4e4eaddd3578c517d587c4eaaf1c458e4f5cfc2e59065fc0f26594ac48; current SHA256 7a806e4e4eaddd3578c517d587c4eaaf1c458e4f5cfc2e59065fc0f26594ac48. Record bytes unchanged since the original review. |
| original-review-8 | reviews/structured/20261022T033003Z-recycling-endosome-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-9 | data/structures/membrane_organelle/recycling_endosome_lumen.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 69bc318299125a4de316f2ba3b7fc20e0655bca2d37fa6d43c12afcfa3fc3ce2; current SHA256 69bc318299125a4de316f2ba3b7fc20e0655bca2d37fa6d43c12afcfa3fc3ce2. Record bytes unchanged since the original review. |
| original-review-9 | reviews/structured/20261022T033003Z-recycling-endosome-lumen-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| septin-review-policy | .claude/skills/review-yaml-record/SKILL.md; Current molecular/pathway applicability and bounded fallback | supports | Positive molecular or pathway assertions trigger structured-source applicability even without an expression claim or individual examples. Use matched organism/strain evidence; source unavailability is not scientific absence. |
| septin-curation-policy | docs/CURATION.md; Identity, constituent evidence, generic classes and append-only discussion | supports | Exact structure identity, material identity, localization and formation necessity are distinct. Dated rationale is provenance, not a current inventory; optional examples and generic classes do not automatically require curation. |
| septin-schema-policy | src/cellstructuremech/schema/cellstructuremech.yaml; Structure, material, graph and evidence contract | supports | Whole-membrane GO identity is structural rather than a molecular lipid class. Collective label-only material and externally grounded regulatory graph nodes are valid scoped representations. |
| septin-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Mechanistic scope and graph actors/relations | supports | Descriptive topology and process association are assessed against their declared NONMECHANISTIC scope. No complete molecular causal chain or obligatory regulator-as-constituent representation is imposed. |
| septin-protein-policy | .claude/skills/uniprot-protein-examples/SKILL.md; Native examples and graph coverage | supports | Native accession and coverage checks certify represented inputs only; an empty example inventory is neither molecular completeness nor biological absence. |
| septin-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0160223,GO:0016020,GO:1990732,GO:0042651,GO:0055037,GO:0055038,GO:0034777,GO:0005768,GO:0031904; All nine exact current GO entries: complete definitions/synonyms and immediate typed child relations | supports | GO0160223 denotes pyrenoid-traversing membrane, distinct from whole GO1990732 and thylakoid membrane GO0042651. GO0055037 is the recycling organelle, GO0055038 its surrounding lipid bilayer and GO0034777 its enclosed volume; endosome/endosome-lumen parent entries expose the corresponding is-a children. Immediate pyrenoid part relations and recycling parts are distinguished from is-a. GO0016020 describes a whole membrane, not a source-neutral molecular lipid identity; no unqueried full-ancestry result is claimed. |
| septin-SL0232 | https://rest.uniprot.org/locations/SL-0232.json; Complete exact location entry and immediate typed isA/partOf fields; nested boundary text read | supports | Exact recycling-endosome location maps GO0055037 and describes Rab11 as a marker. Its relation to endosome is partOf in this response, while the record is-a claim is separately supported by GO; no conflation of these predicates. |
| septin-SL0345 | https://rest.uniprot.org/locations/SL-0345.json; Complete exact location entry and immediate typed isA/partOf fields; nested boundary text read | supports | Exact recycling-endosome-lumen maps GO0034777 and supplies recycling endosomal lumen synonym, endosome-lumen isA and recycling-endosome partOf. |
| septin-tax2759 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759; Complete current ENA/NCBI taxonomy response: identifier, rank, status and lineage | supports | Current Eukaryota domain identifier supports lineage identity, not a prevalence census. |
| septin-tax3055 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3055; Complete current ENA/NCBI taxonomy response: identifier, rank, status and lineage | supports | Current Chlamydomonas reinhardtii species identifier; actual Engel experiment uses CC124(137c), independently established from Methods. |
| septin-tax5691 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5691; Complete current ENA/NCBI taxonomy response: identifier, rank, status and lineage | supports | Current Trypanosoma brucei species identifier; Umaer independently specifies bloodstream T. b. brucei single-marker cells, not every strain or life stage. |
| septin-Q9NJE8 | https://rest.uniprot.org/uniprotkb/Q9NJE8.json; Complete current UniProt JSON: entry status, taxon, primary gene/synonym, submitted names, references, sequence and similarity evidence | supports | Unreviewed TrEMBL Q9NJE8 is T. brucei tax5691, primary gene Rab11, synonym RAB11A, with submitted RAB11A GTPase/small GTPase Rab11 names. Family similarity is inferred annotation, not a new localization experiment. Original sequence references include Jeffries/Field and PMID11683389. Identity is consistent with the graph marker, but no sequence alignment or strain-level equivalence to the Umaer Tb927.8.4330 RNAi construct was performed. |
| septin-engel2015-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.7554/eLife.04889&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact EuropePMC DOI or MED identifier query; complete single-hit metadata and abstract | supports | Engel2015 Native architecture of the Chlamydomonas chloroplast revealed by in situ cryo-electron tomography; primary study PMID25584625/PMC4292175. |
| septin-he2023-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1093/plcell/koad157&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact EuropePMC DOI or MED identifier query; complete single-hit metadata and abstract | supports | He, Crans and Jonikas2023 The pyrenoid: the eukaryotic CO2-concentrating organelle is a secondary review, PMID37279536/PMC10473226. |
| septin-franklin2026-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1111/nph.70669&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact EuropePMC DOI or MED identifier query; complete single-hit metadata and abstract | supports | Franklin et al. Proteomic analysis of the pyrenoid-traversing membranes of Chlamydomonas reinhardtii reveals novel components, PMID41116735/PMC12676092: online first2025-10-21 and journal publication year2026 are distinct valid dates; record2026 is not a demonstrated bibliographic error. |
| septin-jeffries2001-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11683389%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact EuropePMC DOI or MED identifier query; complete single-hit metadata and abstract | supports | Jeffries, Morgan and Field2001 PMID11683389/DOI10.1242/jcs.114.14.2617: complete abstract supports developmental differences and colocalization of TbRAB11 compartments with transferrin receptor and internalized anti-VSG cargo. Publisher body attempt403; exact strain/Methods/pixels not certified. |
| septin-pal2003-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12744719%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact EuropePMC DOI or MED identifier query; complete single-hit metadata and abstract | supports | Pal, Hall, Jeffries and Field2003 PMID12744719/DOI10.1042/bj20030469: complete abstract describes uptake, substantial degradation and exocytosed products after transferrin/anti-VSG antibody entry, with mutant-dependent kinetics. This is not proof of intact ligand recycling or a universal endogenous-cargo requirement. Genuine body unavailable in attempted endpoints. |
| septin-umaer2018-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A29582527%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact EuropePMC DOI or MED identifier query; complete single-hit metadata and abstract | supports | Umaer, Bush and Bangs2018 PMID29582527/DOI10.1111/tra.12565: selective recycling and endocytic trafficking. Complete metadata/abstract checked separately from genuine full scientific body. |
| septin-engel2015-jats | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4292175/fullTextXML; Genuine JATS Results s2-5, Discussion s3-3, Methods s4-1 through s4-4; Fig11 and Video6 text captions; no pixels/video/supplements/raw tomograms | supports | In situ cryo-FIB/cryoET of C. reinhardtii CC124(137c) grown in TAP under constant light resolves thylakoid sheets merging into pyrenoid-crossing tubules containing parallel minitubules. Tubule lumen is continuous with thylakoid lumen, whereas minitubule lumen connects interthylakoid stroma and matrix. Transport/CO2 mechanisms in Discussion are contextual proposals/prior work, not directly measured flux in these tomograms. Record retains coarse topology and qualified function. |
| septin-he2023-jats | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10473226/fullTextXML; Genuine secondary JATS Introduction koad157-s0, operating principles s1.1 and pyrenoid-associated membranes s2.2, embedded Fig1/2 text captions; no source pixels or reference-body audit | supports | Review supports structural diversity, absence of traversing membranes in some pyrenoids and qualified CO2-delivery models. Chlamydomonas carbonic-anhydrase/bestrophin model is not a demonstrated universal protein inventory. Matrix-independent tubules and uncertain minitubule function do not undermine the record topology. Secondary synthesis is explicitly distinguished from primary experimentation. |
| septin-franklin2026-jats | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12676092/fullTextXML; Genuine JATS Introduction sec0001, Methods sec0003/0004 including Table1/Fig2 text, Results sec0011/0012 including Fig1/Table2 text, Discussion sec0019/0020; no candidate-specific mutant results/pixels/supplements/raw MS | supports | RBMP1/2 baits enrich sonicated pyrenoid-associated membrane fragments relative to thylakoid controls, not detergent-solubilized direct interaction complexes. Proteomic enrichment is nonexhaustive localization context, not every candidate being essential. Intro/Discussion qualify CO2-supply function and support tubule traversal. CMJ030 context is used without certifying an internally inconsistent CC number across source Table1 and one Methods sentence. Record only claims species-level scope, coarse enrichment and qualified function. |
| septin-umaer2018-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC5948159/; Genuine PMC scientific body: complete Introduction/Results/Discussion and Methods (derived text lines86–177), Fig1–9 text captions; no image pixels/supplement/raw data | supports | Bloodstream T. b. brucei single-marker RNAi targets Tb927.8.4330; early assays precede terminal growth failure. Rab11 silencing reduces ISG65 recycling and increases its lysosomal turnover, while VSG and transferrin-receptor trafficking are largely unaffected. Surface flow assay does not distinguish every cargo; radioligand-product exocytosis in earlier Pal work is distinct from endogenous recycling. Current graph says selective/Rab11-dependent support, not universal dependence or organelle-formation necessity. Methods establish source conditions; authority accession identity is not claimed to be sequence-matched to this construct. |
| septin-catalogue | https://imodulondb.org/api/datasets; Complete fresh official organism/dataset catalogue; all returned organism rows and dataset strings read | supports | No Chlamydomonas/green-algal, Trypanosoma/Discoba or other eukaryotic host dataset is present in this bounded snapshot. Cyanobacterial s_elongatus coverage is not a proxy for a eukaryotic chloroplast or trypanosome. No matched downstream query is justified; primary/authority source fallback is used. Noncoverage is not biological absence. |
| septin-adapter-runner-historical | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical attempted runner; no fresh invocation | supports | Actual00:49:00.848907Z–00:49:00.863225Z exit1 PermissionError reading runner pyvenv.cfg is retained only as historical availability evidence. Fresh HTTP catalogue and source fallback are separate and are not a new runner success. |
| septin-retrieval-source-receipts | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/adversary-septin/source-receipts.json; Actual fresh HTTP attempt receipts and successful-body hashes | supports | Current genuine Engel/He/Franklin JATS and Umaer HTML are distinguished from Umaer/Pal XML500, Jeffries publisher403, and Pal HTTP200 proof-of-work preparation HTML at the apparent PDF URL. That1817-byte response is not a PDF. Complete Pal/Jeffries abstracts are used within their scope; unavailable Methods/pixels are not treated as evidence against the record. |
| septin-retrieval-additional-source-receipts | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/adversary-septin/additional-source-receipts.json; Actual fresh HTTP attempt receipts and successful-body hashes | supports | Current genuine Engel/He/Franklin JATS and Umaer HTML are distinguished from Umaer/Pal XML500, Jeffries publisher403, and Pal HTTP200 proof-of-work preparation HTML at the apparent PDF URL. That1817-byte response is not a PDF. Complete Pal/Jeffries abstracts are used within their scope; unavailable Methods/pixels are not treated as evidence against the record. |
| septin-context-pyrenoid | data/structures/other/pyrenoid.yaml; Frozen boundary-only context: identifier,label,definition,parent_structures,part_of,has_part,xrefs | supports | Read only after root froze the input. Whole pyrenoid does not impose universal tubules; recycling membrane remains a separate structural boundary. No neighbor scientific verdict or issue disposition is inferred. |
| septin-context-recycling_endosome_membrane | data/structures/membrane_organelle/recycling_endosome_membrane.yaml; Frozen boundary-only context: identifier,label,definition,parent_structures,part_of,has_part,xrefs | supports | Read only after root froze the input. Whole pyrenoid does not impose universal tubules; recycling membrane remains a separate structural boundary. No neighbor scientific verdict or issue disposition is inferred. |
| septin-record-pyrenoid_tubule | data/structures/membrane_organelle/pyrenoid_tubule.yaml; Complete current record at 55020000323f1344e65128992b35f6ef43c703a2 | supports | All identity, definition, components, taxa/examples, function/source notes, history/discussion and graph fields read. Zero individual examples; zero typed molecular nodes or protein accessions. No maintained image. |
| septin-original-pyrenoid_tubule | reviews/structured/20261022T033002Z-pyrenoid-tubule-audit/review.yaml; Complete immutable original YAML/Markdown pair and frozen-source metadata | supports | Original exact target bytes match current. Native schema/render and every historical input hash checked. Original has no scientific finding; qualified verdict is independently reassessed. Historical source access remains historical. |
| septin-original-validation-pyrenoid_tubule | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/adversary-septin/original-checks.json; Actual original native validation/render, exact Markdown and every historical frozen-input hash | supports | Validation and render exit0; exact original Markdown; all historical source inputs match their recorded hashes. Current target is unchanged. Schema validity is separate from scientific support. |
| septin-native-pyrenoid_tubule-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/pyrenoid_tubule-uniprot-verify-receipt.json; Actual command receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/pyrenoid_tubule-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0. Independently counted0 individual protein examples; zero GENE_OR_PROTEIN nodes and zero UniProtKB graph xrefs. This is empty represented protein scope, not complete molecular coverage or biological absence. |
| septin-native-pyrenoid_tubule-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/pyrenoid_tubule-uniprot-causal-receipt.json; Actual command receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/pyrenoid_tubule-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Exit0. Independently counted0 individual protein examples; zero GENE_OR_PROTEIN nodes and zero UniProtKB graph xrefs. This is empty represented protein scope, not complete molecular coverage or biological absence. |
| septin-record-recycling_endosome | data/structures/membrane_organelle/recycling_endosome.yaml; Complete current record at 55020000323f1344e65128992b35f6ef43c703a2 | supports | All identity, definition, components, taxa/examples, function/source notes, history/discussion and graph fields read. Zero individual examples; one typed external TbRAB11 node with Q9NJE8 xref. No maintained image. |
| septin-original-recycling_endosome | reviews/structured/20261022T033003Z-recycling-endosome-audit/review.yaml; Complete immutable original YAML/Markdown pair and frozen-source metadata | supports | Original exact target bytes match current. Native schema/render and every historical input hash checked. Inherited F1/key/action preserved with exact repository/review/finding predecessor. Historical source access remains historical. |
| septin-original-validation-recycling_endosome | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/adversary-septin/original-checks.json; Actual original native validation/render, exact Markdown and every historical frozen-input hash | supports | Validation and render exit0; exact original Markdown; all historical source inputs match their recorded hashes. Current target is unchanged. Schema validity is separate from scientific support. |
| septin-native-recycling_endosome-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/recycling_endosome-uniprot-verify-receipt.json; Actual command receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/recycling_endosome-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0. Independently counted0 individual protein examples; one GENE_OR_PROTEIN external TbRAB11 node is UNANCHORED_WITH_UNIPROT Q9NJE8, not COVERED. No component_ref is intentionally asserted; native identity/coverage does not establish experimental strain sequence equivalence, complete biology or necessary structural membership. |
| septin-native-recycling_endosome-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/recycling_endosome-uniprot-causal-receipt.json; Actual command receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/recycling_endosome-uniprot-causal.log SHA256 8ec13ce57264c182b589096a0cec398aeb141a38ec3be5d93c48ecc41174dcbe | supports | Exit0. Independently counted0 individual protein examples; one GENE_OR_PROTEIN external TbRAB11 node is UNANCHORED_WITH_UNIPROT Q9NJE8, not COVERED. No component_ref is intentionally asserted; native identity/coverage does not establish experimental strain sequence equivalence, complete biology or necessary structural membership. |
| septin-record-recycling_endosome_lumen | data/structures/membrane_organelle/recycling_endosome_lumen.yaml; Complete current record at 55020000323f1344e65128992b35f6ef43c703a2 | supports | All identity, definition, components, taxa/examples, function/source notes, history/discussion and graph fields read. Zero individual examples; zero typed molecular nodes or protein accessions. No maintained image. |
| septin-original-recycling_endosome_lumen | reviews/structured/20261022T033003Z-recycling-endosome-lumen-audit/review.yaml; Complete immutable original YAML/Markdown pair and frozen-source metadata | supports | Original exact target bytes match current. Native schema/render and every historical input hash checked. Original has no scientific finding; qualified verdict is independently reassessed. Historical source access remains historical. |
| septin-original-validation-recycling_endosome_lumen | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/adversary-septin/original-checks.json; Actual original native validation/render, exact Markdown and every historical frozen-input hash | supports | Validation and render exit0; exact original Markdown; all historical source inputs match their recorded hashes. Current target is unchanged. Schema validity is separate from scientific support. |
| septin-native-recycling_endosome_lumen-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/recycling_endosome_lumen-uniprot-verify-receipt.json; Actual command receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/recycling_endosome_lumen-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0. Independently counted0 individual protein examples; zero GENE_OR_PROTEIN nodes and zero UniProtKB graph xrefs. This is empty represented protein scope, not complete molecular coverage or biological absence. |
| septin-native-recycling_endosome_lumen-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/recycling_endosome_lumen-uniprot-causal-receipt.json; Actual command receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/recycling_endosome_lumen-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Exit0. Independently counted0 individual protein examples; zero GENE_OR_PROTEIN nodes and zero UniProtKB graph xrefs. This is empty represented protein scope, not complete molecular coverage or biological absence. |
| plaque-current-5 | data/structures/membrane_organelle/polaroplast.yaml; Entire current maintained record at 55020000323f1344e65128992b35f6ef43c703a2; all components, evidence, functions, graphs, discussions, image metadata and history | supports | Polaroplast is stale solely through two new subregion nodes, their anatomical part_of edges and matching history; pusule target bytes are unchanged. |
| plaque-original-5 | reviews/structured/20261022T033000Z-polaroplast-audit/review.yaml; Exact staleness-selected immutable YAML and native Markdown; source/evidence/assessments/checks/findings/actions/limits | supports | Original qualified pass has no scientific finding or request_curation action. Historical frozen inputs validate at original source; current reassessment is separate. |
| plaque-current-6 | data/structures/membrane_organelle/pusule.yaml; Entire current maintained record at 55020000323f1344e65128992b35f6ef43c703a2; all components, evidence, functions, graphs, discussions, image metadata and history | supports | Polaroplast is stale solely through two new subregion nodes, their anatomical part_of edges and matching history; pusule target bytes are unchanged. |
| plaque-original-6 | reviews/structured/20261022T033001Z-pusule-audit/review.yaml; Exact staleness-selected immutable YAML and native Markdown; source/evidence/assessments/checks/findings/actions/limits | supports | Original qualified pass has no scientific finding or request_curation action. Historical frozen inputs validate at original source; current reassessment is separate. |
| plaque-policy | .claude/skills/review-yaml-record/SKILL.md; Current skill Structured Source Cross-Checks/evidence rules reread; exact bytes unchanged from previous full read | context_only | Applicability follows positive gene/protein/pathway/stress/trait assertions. Physical membrane morphology or unresolved molecular machinery is not automatically a molecular-pathway assertion. |
| plaque-rubric | .claude/skills/curate-yaml-record/references/review-checklist.md; Previously read exact frozen checklist, unchanged | context_only | Identity, anatomical composition, function, mechanism and necessity assessed separately; optional unassigned proteins/lipids alone are not findings. |
| plaque-schema-policy | src/cellstructuremech/schema/cellstructuremech.yaml; Exact frozen component/causal schema previously read, unchanged | context_only | Label-only membrane materials differ from falsely grounding a chemical species to a whole membrane. STRUCTURE subregions and nonmechanistic FUNCTION graphs are permitted. |
| plaque-history-policy | docs/CURATION.md; Previously read exact discussion/history policy, unchanged | context_only | Historical rationale/events remain append-only. Current review does not close neighboring records or their issues. |
| plaque-context-contractile_vacuole | data/structures/membrane_organelle/contractile_vacuole.yaml; Identity/definition/component boundary and declared parthood only, read after exact source freeze; not a complete neighbor scientific audit | context_only | Distinct bounded vacuole versus nuclear-envelope network context; spatial adjacency does not assign ribbons, rootlets or nuclear membranes as pusule constituents. No neighbor finding disposition. |
| plaque-context-nuclear_net | data/structures/membrane_organelle/nuclear_net.yaml; Identity/definition/component boundary and declared parthood only, read after exact source freeze; not a complete neighbor scientific audit | context_only | Distinct bounded vacuole versus nuclear-envelope network context; spatial adjacency does not assign ribbons, rootlets or nuclear membranes as pusule constituents. No neighbor finding disposition. |
| plaque-go-polar | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0160201,GO:0044099; Fresh complete GO0160201 and0044099 id/name/definition/isObsolete response | supports | Exact polaroplast and distinct polar-tube identities. Water-swelling/pressure wording is issuing-authority definition, not a new experimentally proven force calculation. |
| plaque-go-pusule | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0043227,GO:0016020; Fresh complete GO0043227 and0016020 id/name/definition/isObsolete/typed children | supports | Whole membrane-bounded-organelle parent and whole-membrane material match the maintained OTHER membrane component. Surface-canal continuity is not denied by the parent; no exact GO pusule identity is fabricated. |
| plaque-go-pusule-search | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=pusule&amp;limit=100; Complete returned first page, zero results | supports | No exact pusule result in this bounded name query; not exhaustive ontology nonexistence proof. |
| plaque-tax-6029 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/6029; Fresh complete ENA taxId/scientificName/rank/lineage and alternate names | supports | Exact Microsporidia, Nosema bombycis, Polykrikos kofoidii, Prorocentrum micans or Amphidinium carterae identity verified. Taxonomy does not certify occurrence frequency or experimental strain. |
| plaque-tax-27978 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/27978; Fresh complete ENA taxId/scientificName/rank/lineage and alternate names | supports | Exact Microsporidia, Nosema bombycis, Polykrikos kofoidii, Prorocentrum micans or Amphidinium carterae identity verified. Taxonomy does not certify occurrence frequency or experimental strain. |
| plaque-tax-271679 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/271679; Fresh complete ENA taxId/scientificName/rank/lineage and alternate names | supports | Exact Microsporidia, Nosema bombycis, Polykrikos kofoidii, Prorocentrum micans or Amphidinium carterae identity verified. Taxonomy does not certify occurrence frequency or experimental strain. |
| plaque-tax-2945 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2945; Fresh complete ENA taxId/scientificName/rank/lineage and alternate names | supports | Exact Microsporidia, Nosema bombycis, Polykrikos kofoidii, Prorocentrum micans or Amphidinium carterae identity verified. Taxonomy does not certify occurrence frequency or experimental strain. |
| plaque-tax-2961 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2961; Fresh complete ENA taxId/scientificName/rank/lineage and alternate names | supports | Exact Microsporidia, Nosema bombycis, Polykrikos kofoidii, Prorocentrum micans or Amphidinium carterae identity verified. Taxonomy does not certify occurrence frequency or experimental strain. |
| plaque-han-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1007%2F978-3-030-93306-7_8&amp;format=json&amp;resultType=core&amp;pageSize=10; Fresh exact DOI bibliographic identity, title/authors/year/PMID/PMCID | supports | Cited attribution and year agree. Han chapter and Chen article provide secondary review context despite Han metadata research-article tag; Lv and Gavelis are primary experiments. |
| plaque-chen-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1186%2Fs13071-023-05908-9&amp;format=json&amp;resultType=core&amp;pageSize=10; Fresh exact DOI bibliographic identity, title/authors/year/PMID/PMCID | supports | Cited attribution and year agree. Han chapter and Chen article provide secondary review context despite Han metadata research-article tag; Lv and Gavelis are primary experiments. |
| plaque-lv-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1128%2Fmbio.02749-23&amp;format=json&amp;resultType=core&amp;pageSize=10; Fresh exact DOI bibliographic identity, title/authors/year/PMID/PMCID | supports | Cited attribution and year agree. Han chapter and Chen article provide secondary review context despite Han metadata research-article tag; Lv and Gavelis are primary experiments. |
| plaque-gavelis-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1038%2Fs41598-018-37065-w&amp;format=json&amp;resultType=core&amp;pageSize=10; Fresh exact DOI bibliographic identity, title/authors/year/PMID/PMCID | supports | Cited attribution and year agree. Han chapter and Chen article provide secondary review context despite Han metadata research-article tag; Lv and Gavelis are primary experiments. |
| plaque-han-body | https://pmc.ncbi.nlm.nih.gov/articles/PMC10037675/; Genuine SECONDARY chapter HTML: Introduction and Section8.2 selected membrane-array/germination paragraphs, Fig8.1/8.2/8.4/8.5/8.6 captions; no image pixels or complete later sections | supports | Lamellar/flattened-tubular membrane clusters and posterior polaroplast are described in the spore invasion apparatus. Anatomical subregions belong to the membrane system; conserved presence is qualitative and not a measured prevalence denominator. |
| plaque-chen-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC10468886.1/PMC10468886.1.xml; Genuine SECONDARY review JATS: life-cycle germination paragraph, structural polar-filament paragraph and concluding model/unknowns; no pixels or entire-paper certification | supports | Osmotic swelling/discharge is explicitly presented as a widely accepted hypothesis; polaroplast surrounds straight polar-filament region. This is context for physical firing support, not identified force-generation machinery or genetic necessity. |
| plaque-lv-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC10865828.1/PMC10865828.1.xml; Genuine primary JATS: Introduction; Results membrane cargo/transport, sporoplasm formation and localization-marker sections with Fig2–8 captions; Discussion; Methods cell culture/spore preparation/fluorescence/immunofluorescence/TEM/cryo-EM/lipidomics/controls/statistics. No figure pixels, supplements or rawdata independently inspected | supports | Nosema bombycis isolate CQ1 propagated in silkworms; 0.1M KOH induction and fixed-stage DiI/DAPI, TEM/cryo-EM, protein-marker distributions and lipidomics support transported membrane contribution to nascent sporoplasm. These are not continuous single-membrane lineage tracing, universal kinetics, exclusive origin or identified necessary transport proteins. New subregion edges are anatomical, not a mechanism inferred from antibody localization. |
| plaque-dodge-meta | https://api.crossref.org/works/10.1007/BF01279820; Fresh Crossref DOI/title/author/publication identity, no deposited full text | supports | Dodge1972 primary paper identity verified; readable publisher summary bound separately. |
| plaque-dodge-publisher | https://link.springer.com/article/10.1007/BF01279820; Fresh genuine Springer publisher Summary only; page explicitly labels subscription preview. No complete Methods/Results or PDF | supports | Survey summary describes seven pusular forms grouped by vesicle/tubule/sac topology and apposed invaginated plasma/vacuolar membranes with flagellar-canal connection. Excretion/osmoregulation is a proposed interpretation, not a measured molecular mechanism. |
| plaque-klut-meta | https://api.crossref.org/works/10.1139/b87-098; Fresh Crossref publisher-deposited PRIMARY abstract plus bibliographic identity; no full paper/figures/experimental-control audit | supports | Prorocentrum micans and Amphidinium carterae; salinity/temperature size changes and HRP/ferritin/lectin entry through flagellar canal. Fibrillar-collar flow, osmoregulation and secretion are suggestions. Entry into lumen is not demonstrated cytoplasmic delivery, nutrient assimilation or transmembrane transport. |
| plaque-gavelis-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC6351617.1/PMC6351617.1.xml; Fresh genuine JATS ResultsSec2/Par6 and neighboring nuclear-net distinction; MethodsCollection/TEM/FIB-SEM; Fig2 caption/graphic; author list and permissions. No whole-paper or other-figure pixel audit | supports | Wild-collected Polykrikos kofoidii pseudocolonies from Vancouver2015/FridayHarbor2016; four TEM specimens and one retained FIB-SEM specimen. Fig2D is transverse/longitudinal TEM duct/diverticula, E interior FIB-SEM reconstruction, G/H contextual orange pusule and blue nucleus. FIB-SEM uses high-pressure freezing/freeze substitution. Eight authors and CC BY4.0 match attribution; no contrary figure-specific credit restriction. |
| plaque-gavelis-fig2 | https://pmc-oa-opendata.s3.amazonaws.com/PMC6351617.1/41598_2018_37065_Fig2_HTML.jpg; Fresh exact PMC6351617.1 Fig2 JPEG compared bytewise with frozen maintained image; visual inspection of maintained identical pixels at2026-11-03T20:45:23Z | supports | All panels actually viewed. D shows duct/diverticula cross/longitudinal sections, E internal reconstructed pockets; orange G/H pusule is separate from blue nuclear and colored ribbon/rootlet structures. Caption supports D2micrometer andG/H5micrometer bars. No new morphometric measurement. Maintained/download bytes identical SHA6c37909f2a8a422f0625da79598171847c57a39ec9aad4587239482b31eaeb6a, MD5df1b5c4b4cb5d738f4042d41ce50521e. |
| plaque-local-pusule-image | data/images/membrane_organelle/pusule/pmc6351617_fig2.jpg; Frozen maintained image actually visually inspected at2026-11-03T20:45:23Z and matched to fresh source download | supports | Panel context, mixed modality and attribution remain source-bounded; nuclear panels do not become pusule components. |
| plaque-catalogue | https://imodulondb.org/api/datasets; Same-PR complete official JSON catalogue independently reread; actual first-fetch timestamp/hash retained, not a new request | supports | All20 organism rows/28 organism-dataset pairs are bacteria/archaea. No Microsporidia/Nosema or named dinoflagellate host. No matched gene/module query or foreign host proxy used; no biological absence inferred. |
| plaque-historical-runner | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Retained historical00:49Z runner failure with verified stdout/stderr hashes | context_only | PermissionError accessing pyvenv.cfg; no fresh invocation or runner success. Current official-source catalogue fallback is separately identified. |
| plaque-original-checks | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/adversary-plaque/original-checks.json; Actual original native validate/render and historical input hashes: polaroplast12,pusule15 | supports | Both originals validate and render byte-identical Markdown; all27 historical input rows match their originalsource. Polaroplast current hash differs and is substantively refreshed; pusule current target remains identical. |
| plaque-polaroplast-delta | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/adversary-plaque/5-stale.diff; Git diff original frozen revision to current source, exact assigned polaroplast path | supports | Only two anatomical STRUCTURE nodes/component_refs, two part_of edges and matching history were added. Existing component claims, functions and membrane-contribution edges are reassessed, not silently approved by hash replacement. |
| plaque-native-polaroplast-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/polaroplast.yaml --verify; Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/polaroplast-uniprot-verify-receipt.json; logSHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Direct current YAML inspection finds0 protein_examples and0 GENE_OR_PROTEIN nodes. Native command exits0 over an empty represented protein inventory; it does not verify absent proteins, organelle formation or physical mechanism. |
| plaque-native-polaroplast-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/polaroplast.yaml --causal-graphs; Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/polaroplast-uniprot-causal-receipt.json; logSHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Direct current YAML inspection finds0 protein_examples and0 GENE_OR_PROTEIN nodes. Native command exits0 over an empty represented protein inventory; it does not verify absent proteins, organelle formation or physical mechanism. |
| plaque-native-pusule-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/pusule.yaml --verify; Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/pusule-uniprot-verify-receipt.json; logSHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Direct current YAML inspection finds0 protein_examples and0 GENE_OR_PROTEIN nodes. Native command exits0 over an empty represented protein inventory; it does not verify absent proteins, organelle formation or physical mechanism. |
| plaque-native-pusule-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/pusule.yaml --causal-graphs; Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/pusule-uniprot-causal-receipt.json; logSHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Direct current YAML inspection finds0 protein_examples and0 GENE_OR_PROTEIN nodes. Native command exits0 over an empty represented protein inventory; it does not verify absent proteins, organelle formation or physical mechanism. |
| micro-policy | .claude/skills/review-yaml-record/SKILL.md; Current native skill/profile/config/checklist, structured-source applicability and optional-slot contract | context_only | Positive molecular/pathway claims anywhere in a record trigger source applicability. Explicitly withheld molecular scope and physical-only topology remain valid exclusions; source background does not create new record assertions. |
| micro-component-policy | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent/ComponentTypeEnum/EssentialityEnum and CURATION components | context_only | An anatomical membrane GO class is not a chemical LIPID identity; OTHER structural constituent or label-only collective material remains permissible. Optional molecular inventory and individual formation necessity are not inferred from topology. |
| micro-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Graph scope, source-specific edges, component join and allowed generic class semantics | context_only | NONMECHANISTIC descriptive anatomy and supported light-reaction site do not assert a complete assembly pathway or universal protein cohort. |
| micro-discussion-policy | docs/CURATION.md; Discussion305–324; components and evidence placement | context_only | Historical rationale remains append-only; optional chemical grounding and narrow compartment-boundary interpretations do not become defects merely because additional biology is known. |
| micro-record-plastid_outer_membrane | data/structures/membrane_organelle/plastid_outer_membrane.yaml; Entire current record: identity/definition, all source notes/taxa/examples, components/functions, every graph node/edge, status/history/discussions | supports | Complete unchanged target independently read. Original frozen target/current main hashes agree; no maintained record mutation. |
| micro-prior-plastid_outer_membrane | reviews/structured/20261022T032956Z-plastid-outer-membrane-audit/review.yaml; Authoritative original YAML all scientific claims/evidence/scopes/checks/assessments/findings/actions/limits and exact derived Markdown | context_only | Original pass_with_limitations; no scientific findings/actions. Explicit expression-only N/A check. Original observation/check times remain historical. |
| micro-native-plastid_outer_membrane-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_outer_membrane-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_outer_membrane.yaml --verify; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_outer_membrane-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0; complete target independently has zero protein_examples and zero GENE_OR_PROTEIN nodes. Generic verify-success does not certify exhaustive families/proteome, positive narrative machinery, or individual assembly necessity. |
| micro-native-plastid_outer_membrane-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_outer_membrane-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_outer_membrane.yaml --causal-graphs; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_outer_membrane-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Actual exit0; complete target independently has zero protein_examples and zero GENE_OR_PROTEIN nodes. Generic verify-success does not certify exhaustive families/proteome, positive narrative machinery, or individual assembly necessity. |
| micro-record-plastid_stroma | data/structures/membrane_organelle/plastid_stroma.yaml; Entire current record: identity/definition, all source notes/taxa/examples, components/functions, every graph node/edge, status/history/discussions | supports | Complete unchanged target independently read. Original frozen target/current main hashes agree; no maintained record mutation. |
| micro-prior-plastid_stroma | reviews/structured/20261022T032957Z-plastid-stroma-audit/review.yaml; Authoritative original YAML all scientific claims/evidence/scopes/checks/assessments/findings/actions/limits and exact derived Markdown | context_only | Original pass_with_limitations; no scientific findings/actions. Explicit expression-only N/A check. Original observation/check times remain historical. |
| micro-native-plastid_stroma-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_stroma-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_stroma.yaml --verify; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_stroma-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0; complete target independently has zero protein_examples and zero GENE_OR_PROTEIN nodes. Generic verify-success does not certify exhaustive families/proteome, positive narrative machinery, or individual assembly necessity. |
| micro-native-plastid_stroma-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_stroma-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_stroma.yaml --causal-graphs; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_stroma-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Actual exit0; complete target independently has zero protein_examples and zero GENE_OR_PROTEIN nodes. Generic verify-success does not certify exhaustive families/proteome, positive narrative machinery, or individual assembly necessity. |
| micro-record-plastid_thylakoid | data/structures/membrane_organelle/plastid_thylakoid.yaml; Entire current record: identity/definition, all source notes/taxa/examples, components/functions, every graph node/edge, status/history/discussions | supports | Complete unchanged target independently read. Original frozen target/current main hashes agree; no maintained record mutation. |
| micro-prior-plastid_thylakoid | reviews/structured/20261022T032958Z-plastid-thylakoid-audit/review.yaml; Authoritative original YAML all scientific claims/evidence/scopes/checks/assessments/findings/actions/limits and exact derived Markdown | context_only | Original needs_curation; one inherited majorF1. Prose-only expression-module exclusion; Perez secondary excerpts/challenge mislabeled primary_source. Original observation/check times remain historical. |
| micro-native-plastid_thylakoid-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_thylakoid-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_thylakoid.yaml --verify; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_thylakoid-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0; complete target independently has zero protein_examples and zero GENE_OR_PROTEIN nodes. Generic verify-success does not certify exhaustive families/proteome, positive narrative machinery, or individual assembly necessity. |
| micro-native-plastid_thylakoid-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_thylakoid-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_thylakoid.yaml --causal-graphs; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_thylakoid-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Actual exit0; complete target independently has zero protein_examples and zero GENE_OR_PROTEIN nodes. Generic verify-success does not certify exhaustive families/proteome, positive narrative machinery, or individual assembly necessity. |
| micro-record-plastid_thylakoid_lumen | data/structures/membrane_organelle/plastid_thylakoid_lumen.yaml; Entire current record: identity/definition, all source notes/taxa/examples, components/functions, every graph node/edge, status/history/discussions | supports | Complete unchanged target independently read. Original frozen target/current main hashes agree; no maintained record mutation. |
| micro-prior-plastid_thylakoid_lumen | reviews/structured/20261022T032959Z-plastid-thylakoid-lumen-audit/review.yaml; Authoritative original YAML all scientific claims/evidence/scopes/checks/assessments/findings/actions/limits and exact derived Markdown | context_only | Original pass_with_limitations; no scientific findings/actions. Prose-only expression-module exclusion; Perez secondary excerpts/challenge mislabeled primary_source. Original observation/check times remain historical. |
| micro-native-plastid_thylakoid_lumen-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_thylakoid_lumen-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_thylakoid_lumen.yaml --verify; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_thylakoid_lumen-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0; complete target independently has zero protein_examples and zero GENE_OR_PROTEIN nodes. Generic verify-success does not certify exhaustive families/proteome, positive narrative machinery, or individual assembly necessity. |
| micro-native-plastid_thylakoid_lumen-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_thylakoid_lumen-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_thylakoid_lumen.yaml --causal-graphs; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_thylakoid_lumen-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Actual exit0; complete target independently has zero protein_examples and zero GENE_OR_PROTEIN nodes. Generic verify-success does not certify exhaustive families/proteome, positive narrative machinery, or individual assembly necessity. |
| micro-record-plastid_thylakoid_membrane | data/structures/membrane_organelle/plastid_thylakoid_membrane.yaml; Entire current record: identity/definition, all source notes/taxa/examples, components/functions, every graph node/edge, status/history/discussions | supports | Complete unchanged target independently read. Original frozen target/current main hashes agree; no maintained record mutation. |
| micro-prior-plastid_thylakoid_membrane | reviews/structured/20261022T033000Z-plastid-thylakoid-membrane-audit/review.yaml; Authoritative original YAML all scientific claims/evidence/scopes/checks/assessments/findings/actions/limits and exact derived Markdown | context_only | Original pass_with_limitations; no scientific findings/actions. Prose-only expression-module exclusion; Perez secondary excerpts/challenge mislabeled primary_source. Original observation/check times remain historical. |
| micro-native-plastid_thylakoid_membrane-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_thylakoid_membrane-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_thylakoid_membrane.yaml --verify; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_thylakoid_membrane-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0; complete target independently has zero protein_examples and zero GENE_OR_PROTEIN nodes. Generic verify-success does not certify exhaustive families/proteome, positive narrative machinery, or individual assembly necessity. |
| micro-native-plastid_thylakoid_membrane-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_thylakoid_membrane-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_thylakoid_membrane.yaml --causal-graphs; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_thylakoid_membrane-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Actual exit0; complete target independently has zero protein_examples and zero GENE_OR_PROTEIN nodes. Generic verify-success does not certify exhaustive families/proteome, positive narrative machinery, or individual assembly necessity. |
| micro-original-pairs | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/adversary-microtubule/original-checks.json; Five actual native validates and five exact render --content comparisons | supports | All five original authoritative YAMLs validate and derive exact original Markdown bytes. |
| micro-original-inputs | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/adversary-microtubule/original-frozen-inputs.json; All76 original frozen input entries at retained original source | supports | All old hashes match. Own five targets unchanged; checking historical hashes does not constitute fresh scientific judgment of neighboring records. |
| micro-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005737,GO:0009526,GO:0009527,GO:0009529,GO:0009532,GO:0009535,GO:0009536,GO:0009579,GO:0009843,GO:0019684,GO:0031976,GO:0031977,GO:0031978,GO:0033114,GO:0033115,GO:0042170,GO:0042651,GO:0055035,GO:0070118; All19 requested native entries id/name/active/definition/synonyms/comments and relevant typed children; broad unrelated cytoplasm children not adopted | supports | Exact outer/stroma/thylakoid/lumen/membrane identities, parent classes and parthood verified. GO9532 proteinaceous ground substance supports current paraphrase; GO9579 comment explicitly distinguishes thylakoid from organelle. GO19684 is oxygenic PSI/PSII light reactions. Whole membraneGO55035 remains anatomical. GO70118 is under generic thylakoid membrane, not exposed as nativeGO55035 child. |
| micro-GO0009527-isa | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009527/ancestors?relations=is_a; Complete exact-term ancestors response with relations=is_a | supports | Exact transitive is_a ancestry read separately from parthood; GO0070118 lacks GO0055035 in this native ancestor response, while separate UniProt hierarchy supports the broader biological classification. |
| micro-GO0031976-isa | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031976/ancestors?relations=is_a; Complete exact-term ancestors response with relations=is_a | supports | Exact transitive is_a ancestry read separately from parthood; GO0070118 lacks GO0055035 in this native ancestor response, while separate UniProt hierarchy supports the broader biological classification. |
| micro-GO0031978-isa | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031978/ancestors?relations=is_a; Complete exact-term ancestors response with relations=is_a | supports | Exact transitive is_a ancestry read separately from parthood; GO0070118 lacks GO0055035 in this native ancestor response, while separate UniProt hierarchy supports the broader biological classification. |
| micro-GO0055035-isa | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0055035/ancestors?relations=is_a; Complete exact-term ancestors response with relations=is_a | supports | Exact transitive is_a ancestry read separately from parthood; GO0070118 lacks GO0055035 in this native ancestor response, while separate UniProt hierarchy supports the broader biological classification. |
| micro-GO0070118-isa | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0070118/ancestors?relations=is_a; Complete exact-term ancestors response with relations=is_a | supports | Exact transitive is_a ancestry read separately from parthood; GO0070118 lacks GO0055035 in this native ancestor response, while separate UniProt hierarchy supports the broader biological classification. |
| micro-SL-0214 | https://rest.uniprot.org/locations/SL-0214.json; Complete native location identity/definition/GO mappings/synonyms and nested is_a/part_of hierarchy; protein statistics not experimental census | supports | Exact GO9527 mapping/three synonyms, cytoplasm-facing orientation and nested generic membrane/envelope hierarchy. |
| micro-SL-0215 | https://rest.uniprot.org/locations/SL-0215.json; Complete native location identity/definition/GO mappings/synonyms and nested is_a/part_of hierarchy; protein statistics not experimental census | supports | Exact GO9532 mapping/synonym and internal hydrophilic matrix excluding thylakoid space; plastid parthood. |
| micro-SL-0278 | https://rest.uniprot.org/locations/SL-0278.json; Complete native location identity/definition/GO mappings/synonyms and nested is_a/part_of hierarchy; protein statistics not experimental census | supports | ExactGO31976 mapping, thylakoid is_a and plastid part_of. Identity/morphology source, not a measured protein stoichiometry or prevalence census. |
| micro-SL-0082 | https://rest.uniprot.org/locations/SL-0082.json; Complete native location identity/definition/GO mappings/synonyms and nested is_a/part_of hierarchy; protein statistics not experimental census | supports | Glaucocystophyte cyanelle identity and plastid hierarchy, cyanobacteria-like thylakoids and envelope/peptidoglycan context. |
| micro-SL-0356 | https://rest.uniprot.org/locations/SL-0356.json; Complete native location identity/definition/GO mappings/synonyms and nested is_a/part_of hierarchy; protein statistics not experimental census | supports | Exact organellar chromatophore membraneGO70118 with explicit is_aSL0216/GO55035 and whole-thylakoid parthood. Separate issuing-authority hierarchy, not a fabricated direct GO relation. |
| micro-tax2759 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759; Complete identity/rank/lineage/aliases; no taxon prevalence inferred | supports | Eukaryota domain. |
| micro-tax33090 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/33090; Complete identity/rank/lineage/aliases; no taxon prevalence inferred | supports | Viridiplantae kingdom/eukaryotic lineage. |
| micro-tax3055 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3055; Complete identity/rank/lineage/aliases; no taxon prevalence inferred | supports | C.reinhardtii species/green-algal lineage; strain aliases do not establish Jin experimental strain. |
| micro-tax38254 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/38254; Complete identity/rank/lineage/aliases; no taxon prevalence inferred | supports | Glaucocystophyceae class, Glaucophyceae/Glaucophyta synonyms. |
| micro-catalogue-api | https://imodulondb.org/api/datasets; Complete official unpaginated20 organism rows/28 organism-dataset pairs, id/name/description/datasets | supports | No Chlamydomonas, green-algal or glaucophyte host coverage. Four positive molecular/pathway records require applicability assessment; no matched source means no downstream gene/module query or unrelated bacterial proxy. Physical lumen exclusion remains independently justified. |
| micro-historical-runner | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical command /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources imodulondb datasets;00:49Z PermissionError reading pyvenv.cfg | context_only | Historical optional runner unavailable, not rerun now. Fresh native catalogue fallback used with host-noncoverage scope. |
| micro-keeling-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1098%2Frstb.2009.0103%22&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact quoted DOI query, unique MED record, complete title/authors/year/DOI/publication types/abstract and source routes | context_only | Keeling2010 PMID20124341 is secondary evolutionary review. |
| micro-terashima-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1007%2Fs00294-011-0339-1%22&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact quoted DOI query, unique MED record, complete title/authors/year/DOI/publication types/abstract and source routes | context_only | Terashima/Specht/Hippler2011 PMID21533645 is secondary chloroplast-proteome review. |
| micro-perez-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1146%2Fannurev-cellbio-120823-022747%22&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact quoted DOI query, unique MED record, complete title/authors/year/DOI/publication types/abstract and source routes | context_only | Perez-Boerema/Engel/Wietrzynski2024 PMID38950450 is explicitly publication type Review; oxygenic photosynthetic architecture and qualitative conservation. |
| micro-engel-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.7554%2FeLife.04889%22&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact quoted DOI query, unique MED record, complete title/authors/year/DOI/publication types/abstract and source routes | context_only | Engel2015 PMID25584625/PMC4292175 matches exact primary cryoET study; native abstract supports imaging context, body separately read. |
| micro-jin-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.cell.2022.10.030%22&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact DOI unique MED36413996 metadata, complete primary abstract and keywordList including C.reinhardtii; no full body | supports | Chlamydomonas TOC–TIC cryoEM supercomplex spans both envelope membranes and IMS scaffold; supports bounded outer-envelope example, not strain, full model/Methods, individual component necessity or every plastid lineage. |
| micro-keeling-retained | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2817223/; Retained genuine HTML10:10:38.582642Z, independently reread complete s1/s3/s6/s9 including embeddedFigures1–3 captions; no pixels/underlying studies | context_only | Secondary review supports green primary double envelopes and scattered/reduced plastids. Old universal mitochondrial claims, chromalveolate hypotheses and numerical census are not current assertions. |
| micro-terashima-retained | https://link.springer.com/content/pdf/10.1007/s00294-011-0339-1.pdf; Retained genuine PDF10:10:38.518294Z; independently reread pages151–154 including title/abstract/Introduction/proteome compilation/initial Photosynthesis and text captions; no later pages/pixels/supplementary inventories | context_only | Secondary review supports Chlamydomonas chloroplast metabolic/protein-biogenesis research. Chloroplast/mitochondrial enriched preparations and contamination/candidate caveats distinguish general stromal/proteome context from an independently purified Chlamydomonas stromal dataset; Arabidopsis subfraction data are not reassigned. |
| micro-perez-retained | https://www.annualreviews.org/docserver/ahah/fulltext/cellbio/40/1/annurev-cellbio-120823-022747.html?expires=1793737002&amp;id=id&amp;accname=guest&amp;checksum=47EAFDAB41E06430970416431EF37629; Retained genuine delivered publisherHTML20:02:23.441867Z; independently read complete Introduction/evolutionary overview, Building Blocks opening, Lipids and ETC sections, embeddedFigure1/2 captions. No pixels/complete later sections/underlying primary citations | context_only | Secondary review supports pigments/protein complexes and lipid membranes enclosing lumen, oxygenic electron transfer and proton gradient. No universal exact lipid ratios, per-protein formation necessity or exhaustive taxon-specific composition is imported. |
| micro-engel-primary | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4292175/fullTextXML; Fresh collaborating JATS20:43:24.342979Z independently read s1,s2-1/s2-2/s2-3 with embedded captions, s3-1/s3-2 and Methods s4-1 through s4-5; no pixels/videos/supplements/raw tomography | supports | Direct native thylakoid membrane/lumen cryoFIB/cryoET in C.reinhardtii WTCC124(137c), TAP/constant light/air conditions. Network morphology and rare envelope contacts observed; universal continuity and molecular transport/biogenesis remain hypotheses, not proved mechanisms. |
| micro-jin-retained-access | https://api.elsevier.com/content/article/PII:S0092867422013769?httpAccept=text/xml; Retained20:01:44.453877Z publisher XML1941bytes; exact coredata metadata inspected; no fresh body request | context_only | Full-text response wrapper contains only coredata, not scientific body. Current primary abstract remains the available assessed tier; no model/pixels/Methods claim. |
| check-qc | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/qc.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| check-labels | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/labels.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| check-trait-links | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/trait-links.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Native TraitMech link check passed. |
| check-vendored | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/vendored.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Pinned governed files match; native vendored check passed. |
| check-curies | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/curies.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| focused | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/focused-results.json; All twenty actual target schema/strict command outputs | supports | Ten schema and ten strict commands returned exit zero. |
| supplemental-pmid | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/pmid-chunks-receipt.json; Complete native-report PMID set checked with unchanged resolver in batches of at most fifty | supports | 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers remain unverified. |
| historical-adapter-runner-availability | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical runner invocation receipt, exact SHA256 reverified during PR2376 synthesis | context_only | Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS PermissionError reading the configured runner pyvenv.cfg. This is retained historical availability evidence, not a fresh attempt or a scientific validation failure. Native policy permits inspected source-catalogue fallback. |
| root-native-plastid_outer_membrane-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_outer_membrane-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-plastid_outer_membrane-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_outer_membrane-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-plastid_stroma-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_stroma-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-plastid_stroma-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_stroma-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-plastid_thylakoid-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_thylakoid-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-plastid_thylakoid-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_thylakoid-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-plastid_thylakoid_lumen-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_thylakoid_lumen-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-plastid_thylakoid_lumen-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_thylakoid_lumen-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-plastid_thylakoid_membrane-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_thylakoid_membrane-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-plastid_thylakoid_membrane-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_thylakoid_membrane-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-polaroplast-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/polaroplast-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-polaroplast-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/polaroplast-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-pusule-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/pusule-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-pusule-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/pusule-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-pyrenoid_tubule-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/pyrenoid_tubule-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-pyrenoid_tubule-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/pyrenoid_tubule-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-recycling_endosome-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/recycling_endosome-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-recycling_endosome-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/recycling_endosome-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-recycling_endosome_lumen-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/recycling_endosome_lumen-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-recycling_endosome_lumen-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/recycling_endosome_lumen-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |

## Limits And Additional Notes

- Pyrenoid tubule and two recycling-endosome records independent subreview: Independent read-only scope: three unchanged targets; one inherited confirmed major recycling-endosome lipid/whole-membrane grounding finding. Pyrenoid tubule and recycling lumen pass with limitations. Three explicit expression-only adapter exemptions require corrected applicability evidence. No new scientific finding or record mutation.
- Pyrenoid tubule and two recycling-endosome records independent subreview: All current authority/catalogue/metadata and genuine bodies were freshly fetched with recorded timestamps and SHA256. Engel scientific scope is Results s2-5, Discussion s3-3, Methods s4-1–4 and text captions; no source pixels/videos/raw tomograms. He is secondary review, inspected Introduction/operating-principles/membrane sections, not a primary experiment or reference-body audit.
- Pyrenoid tubule and two recycling-endosome records independent subreview: Franklin inspected Intro, strain/membrane-affinity Methods, membrane-isolation/relative-proteome Results and method/function Discussion with embedded tables/captions. Candidate-specific mutant results, raw MS and supplements were not independently audited. Membrane-fragment enrichment is not direct interaction, completeness or formation necessity. Online2025 versus publication2026 dates are distinguished. No exact contradictory source CC strain number is imported into a species-level record.
- Pyrenoid tubule and two recycling-endosome records independent subreview: Jeffries and Pal complete primary abstracts/metadata only: publisher403 and XML500/PDF preparation HTML prevented genuine full bodies in attempted endpoints. No exact strain/Methods/pixels are certified. Pal explicitly includes degradation/product exocytosis, so intact-ligand or universal endogenous-cargo dependence is not inferred. Access failure is not refutation.
- Pyrenoid tubule and two recycling-endosome records independent subreview: Umaer genuine scientific Introduction/Results/Discussion and Methods plus text captions were read. Bloodstream single-marker RNAi effects are selective for ISG65 versus largely unaffected VSG/TfR; source context does not generalize to every stage/cargo. No pixels/supplements/raw reanalysis or sequence alignment between Q9NJE8 and the RNAi locus was performed.
- Pyrenoid tubule and two recycling-endosome records independent subreview: Q9NJE8 current unreviewed identity/primary gene/taxon are compatible with external Rab11 marker. Inferred family annotation is not experimental localization. Native checks pass on zero examples and one UNANCHORED_WITH_UNIPROT node for whole recycling endosome; the other two targets have zero examples and zero typed nodes. These statuses are not complete molecular coverage or obligatory constituent claims.
- Pyrenoid tubule and two recycling-endosome records independent subreview: Fresh complete catalogue has no actual eukaryotic host match; no unmatched cyanobacterial proxy or downstream module query used. Catalogue noncoverage is not biological absence. Historical00:49Z runner PermissionError is retained only with its actual old timestamp, distinct from fresh HTTP/source fallback.
- Pyrenoid tubule and two recycling-endosome records independent subreview: All28 actually used repository inputs were frozen before reading:17 common inputs,3 targets,6 originals and2 bounded anatomy neighbors. Every historical source-input hash of the three originals was also checked without scientifically reauditing unrelated historical neighbors. No whole-neighbor/grouped-issue disposition or future saved-head/global-QC/CI/queue certification is claimed.
- Polaroplast and pusule independent subreview: Both assigned targets retain pass_with_limitations; no scientific finding or request_curation action established. Polaroplast stale graph is refreshable entirely in review-bundle scope; pusule unchanged. No record edits or new inventory mandatory requirements.
- Polaroplast and pusule independent subreview: Original native YAML validation and exact Markdown render pass for both; all12polaroplast+15pusule historical frozen inputs match. Current6nodes/5edges are independently reassessed rather than replacing a hash or treating historical4nodes/3edges as current.
- Polaroplast and pusule independent subreview: Han is a secondary book chapter, not primary experiment despite a metadata publication-type tag. Only declared Introduction/Section8.2 membrane paragraphs and Fig8.1/8.2/8.4–6 captions were read; no pixels or full underlying cited primary studies. Chen is secondary review; declared germination/structural/concluding paragraphs only.
- Polaroplast and pusule independent subreview: Lv primary JATS declared Introduction/Results/Discussion and relevant Methods read, but no figure pixels, supplementary files or rawdata reanalysis. N.bombycis CQ1/KOH/fixed-stage labeling and microscopy support contribution, not continuous membrane lineage tracing, an exclusive universal origin, measured force, or necessary protein machinery.
- Polaroplast and pusule independent subreview: Pusule Dodge access is genuine publisher Summary/subscription preview only; Klut is complete publisher-deposited primary abstract only. No fresh full-body/publisher-failure claim or experimental-control certification. Proposed functions remain proposed.
- Polaroplast and pusule independent subreview: Gavelis primary ResultsSec2/Par6, boundary paragraph, Collection/TEM/FIB-SEM, Fig2 caption and permissions were inspected; not whole-paper findings. Figure2 maintained/source pixels actually viewed and identical; no other figures, videos, supplements or morphometrics audited. Wild-collected pseudocolonies are not an invented laboratory strain.
- Polaroplast and pusule independent subreview: Both records have0protein_examples and0GENE_OR_PROTEIN nodes, verified directly and with four native root command receipts. An empty native inventory pass is not scientific proof of no proteins or mechanism.
- Polaroplast and pusule independent subreview: Both current whole-record claims support genuine structured-source exclusion: physical membrane movement/anatomy is not automatically a named molecular pathway; unresolved proteins and proposed physiology are not positive molecular assertions. Original stock expression-only wording is clarified. Same-PR catalogue independently reread at actual20:43:49.951558Z fetch time has no matched host; no foreign queries or absence inference. Historical00:49Z runner PermissionError remains historical, no new runner execution claimed.
- Polaroplast and pusule independent subreview: Two additional frozen neighbors used only for identity/definition/component/parthood boundary context; no entire-neighbor scientific review, disposition or issue resolution. Root owns global QC, issue handling, native persistence, CI/queue/merge; this report does not precertify future gates.
- Five plastid compartment records independent subreview: Five complete unchanged assigned records independently reviewed. One inherited major whole-thylakoid LIPID identity finding remains open with exact predecessor/action; four targets retain qualified positive assessments. Four adapter exclusions require correction; physical thylakoid lumen exclusion is genuine. No new scientific finding.
- Five plastid compartment records independent subreview: Current native authorities/catalogue/exact DOI metadata are fresh. Keeling genuineHTML10:10:38.582642Z, Terashima genuinePDF10:10:38.518294Z and Perez genuinepublisherHTML20:02:23.441867Z are retained with original hashes/timestamps and independently reread, not represented as new fetches.
- Five plastid compartment records independent subreview: Keeling secondary s1/s3/s6/s9 and embeddedFigure1–3 captions read. Outdated chromalveolate/universal mitochondrial statements, numerical census and underlying studies are not adopted; no pixels. Terashima secondary pp151–154 read, no later sections/supplementary lists/pixels; enriched wholechloroplast preparations are not purified Chlamydomonas stroma, and Arabidopsis fraction data remain distinct.
- Five plastid compartment records independent subreview: Jin2022 current primary abstract/species keyword only. Retained publisher1941byteXML coredata is metadata, not body. No exact strain, full Methods/atomic model/pixels/deletion-assay interpretation certified. Access limitation is not refutation.
- Five plastid compartment records independent subreview: Perez is secondary synthesis, not primary experimental evidence. Declared Introduction/evolutionary overview/BuildingBlocks/Lipids/ETC and embeddedFigure1/2 captions read; not whole later body, pixels or cited primary papers. No exact lipid ratios/universal protein inventory or individual assembly necessity inferred.
- Five plastid compartment records independent subreview: Engel primary fresh collaboratingJATS20:43:24.342979Z independently read s1,s2-1/s2-2/s2-3,s3-1/s3-2,Methods s4-1 through s4-5 and embedded captions; no figure/video pixels, supplements or raw tomography reanalysis. WTCC124(137c),TAP,constantlight/air context retained; observed connections do not prove universal continuity or proposed transport/biogenesis mechanisms.
- Five plastid compartment records independent subreview: GO0070118 native ancestry lacksGO0055035; UniProtSL0356 explicitly supplies plastid-thylakoid-membrane class mapping. No nativeGOedge is invented. COMMON/RARE distributions remain qualitative, not measured prevalence.
- Five plastid compartment records independent subreview: All five records have zero protein_examples and zero typed molecular nodes. Ten native passes certify only actual inputs; broad positive narrative protein/pathway claims still need applicability assessment. Full20organism/28pair catalogue lacks matched green/glaucophyte hosts; no proxy/downstream query. Historical00:49Z runner PermissionError is not a fresh invocation.
- Five plastid compartment records independent subreview: Original Perez evidence type defect affects three bundles, not scientific-record truth: secondary excerpt and failed access were structured as primary_source. New authority/context types and source access limits repair the successor assessment without altering historical bytes.
- Five plastid compartment records independent subreview: All32 actually used local inputs are frozen commonpolicy/config/schema/verifier plus five targets/ten original artifacts; no new neighbor scientific disposition. No record/history/generated/Git/GitHub edits. Root owns global gates, issues, final persistence/CI/queue/merge; this report does not precertify later results.
- Historical observations remain immutable; their old checks are not represented as current-head execution.
- The adapter runner was not rerun after the canary established OS access failure. Catalogue-based coverage is assessed directly; fresh and reused responses retain actual access timestamps.
- Native label checks include 923 no-adapter skips. Native identifier checks include 909 PMID transport failures and 254 skipped identifiers; bounded supplemental checks independently resolve the 909 PMIDs.
- Scientific record-curation findings stay in separate issues; no record is edited by this review PR.
- Final trusted-base post-save review-check, exact-head independent acceptance, final-head CI and merge-group CI occur after saving this immutable observation and are not represented here as already completed.
- All ten original YAML/Markdown pairs remain unchanged. Current main was merged normally and pushed without force. Only polaroplast differs from its original frozen target; the other nine target hashes still match.
- This explicit issue-bearing ten-record cohort follows native persistence policy. Inherited scientific findings preserve exact repository/review/finding lineage; newly observed findings, if any, have no invented predecessors.
- Issue2785 tracks the stale polaroplast review. The current record adds anterior lamellar and posterior tubular STRUCTURE nodes joined to existing components, two anatomical parthood edges and dated history. Their precise source support is reassessed without asserting new molecular machinery or formation necessity.
- Issue2786 tracks seven unsupported structured-source exclusions: five explicit check rows (outer membrane, stroma, pyrenoid tubule and both recycling records) and two prose notes (whole thylakoid and thylakoid membrane). Thylakoid lumen, polaroplast and pusule retain justified physical-scope exclusions.
- Issue2787 tracks three original thylakoid observations, each with three incorrectly primary-typed Perez2024 evidence items. Actual secondary-review text and HTTP403 access-only context remain distinct in the corrected successor; historical access times and limits are preserved.
- Source commit55020000323f1344e65128992b35f6ef43c703a2 is retained by tag review-base/pr2376-current-record-followup-20261103.
- CLAUDE.md aliases canonical regular AGENTS.md, whose exact bytes are frozen. All used local policy, schema, verifier, original observations, image and requested boundary inputs are frozen before assessment.
- All twenty native protein commands passed. There are no represented protein examples in this cohort. Recycling endosome has one typed TbRAB11 node with UniProtKB:Q9NJE8; the other nine records have zero typed molecular nodes. These scoped checks do not certify absence of narrative molecular claims or exhaustive biological inventories.
- Fresh and retained source snapshots preserve actual access times, source tiers and bounded inspected sections or pixels. Pusule image bytes, panel scope, caption, attribution and licence are assessed separately from physiological transport mechanisms.
- Native CausalNode schema permits families and complexes as GENE_OR_PROTEIN. Missing optional examples or unchanged label-only collective material do not automatically constitute scientific defects.
- No same-record/finding duplicate was found in all245 open issue bodies or25 bounded title/body/comment queries. Existing validator2514 remains reused. No scientific record, historical discussion or resolver is edited.
- Final trusted-base post-save review-check, exact-head independent acceptance, final-head CI and merge-group CI occur after this immutable observation and are not represented as already completed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T204939Z-pr2376-current-record-followup
kind: batch
repository: CultureBotAI/CellStructureMech
title: 'PR 2376: current-input review of ten records and adversarial follow-up'
started_at: '2026-11-03T20:41:43.388442Z'
finished_at: '2026-11-03T20:49:39Z'
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
  merging main. The stale polaroplast review is refreshed by reassessing newly added
  anatomical subregion nodes, component joins and two parthood edges. Seven unsupported
  source-applicability exclusions are corrected; thylakoid lumen, polaroplast and
  pusule retain justified physical-scope exclusions. Three original thylakoid observations
  misclassify secondary-review text and an access challenge as primary evidence; the
  successor corrects source tiers and access-only scope while leaving the originals
  unchanged. All scientific records remain unchanged. Two inherited major scientific
  findings remain open across two targets; eight other targets retain qualified positive
  assessments. Exact predecessor identities and separate curation issue links are
  preserved.
source:
  git_revision: 55020000323f1344e65128992b35f6ef43c703a2
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
  - path: data/images/membrane_organelle/pusule/pmc6351617_fig2.jpg
    sha256: 6c37909f2a8a422f0625da79598171847c57a39ec9aad4587239482b31eaeb6a
    role: context
  - path: data/structures/membrane_organelle/contractile_vacuole.yaml
    sha256: d1057e9c19ff100f054c73da52b597742dadde491f2a007cd7b648b8a7b626bb
    role: context
  - path: data/structures/membrane_organelle/nuclear_net.yaml
    sha256: 8b4a54d13a70cfb4fdce9bd18ae990793f9de9627fdca067573c033335d847ba
    role: context
  - path: data/structures/membrane_organelle/plastid_outer_membrane.yaml
    sha256: 59bd8548931d27f711233f542b5f927c0e7b0a68dd611eabb4777ee08003deaa
    role: target
  - path: data/structures/membrane_organelle/plastid_stroma.yaml
    sha256: 86d19307cbe21273498f0d7d6741e61f5ebf002cf78418c34b922d9d4963503b
    role: target
  - path: data/structures/membrane_organelle/plastid_thylakoid.yaml
    sha256: ec3c74ee89bf25eea6a3a5682b3f7f73e0837465dccf2a8f2c0cce1550a4e3c8
    role: target
  - path: data/structures/membrane_organelle/plastid_thylakoid_lumen.yaml
    sha256: 7a75c5aee47a20bbae7da6351e07fc7f2d1dc418e7ca34e253d08e3a531ff4ee
    role: target
  - path: data/structures/membrane_organelle/plastid_thylakoid_membrane.yaml
    sha256: 51a2ece521e1b5c0b3b589fc7cf665be1c9544299257e0fda7fcf8352e7401c2
    role: target
  - path: data/structures/membrane_organelle/polaroplast.yaml
    sha256: 33a7618c43eea5924263584a6faa84d6190ff1198bfdb1ca2903d49e726c2642
    role: target
  - path: data/structures/membrane_organelle/pusule.yaml
    sha256: 3bc5082b5e3b721414b9b2d57c585c1a278de5053885f34f55b40ccd4b71a6ae
    role: target
  - path: data/structures/membrane_organelle/pyrenoid_tubule.yaml
    sha256: dd5c61f94612f6c30f259f029b7f4bc4daa8a7d4c0fa8111f6eb0715f78483d7
    role: target
  - path: data/structures/membrane_organelle/recycling_endosome.yaml
    sha256: 7a806e4e4eaddd3578c517d587c4eaaf1c458e4f5cfc2e59065fc0f26594ac48
    role: target
  - path: data/structures/membrane_organelle/recycling_endosome_lumen.yaml
    sha256: 69bc318299125a4de316f2ba3b7fc20e0655bca2d37fa6d43c12afcfa3fc3ce2
    role: target
  - path: data/structures/membrane_organelle/recycling_endosome_membrane.yaml
    sha256: cc07cfcf4d3c8fcfac3594e3dec18791b1e5f40e13d867fcdb4ef355f07aebf0
    role: context
  - path: data/structures/other/pyrenoid.yaml
    sha256: bdaff3023422d77a8c9a8b8c5d45e254fa3ab2322076eb5aa27cb0e1e954bfc7
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
  - path: reviews/structured/20261022T032956Z-plastid-outer-membrane-audit/review.md
    sha256: b341c97d706eaf0e93ead18f268c3b7ebf77882bd5ef93edceedafa4de12a84c
    role: context
  - path: reviews/structured/20261022T032956Z-plastid-outer-membrane-audit/review.yaml
    sha256: 13834625be15bdee042f39f764b0f9557c5ea353bf9a718a3ee83cd8977afb99
    role: context
  - path: reviews/structured/20261022T032957Z-plastid-stroma-audit/review.md
    sha256: 40e9ef82553601e3108b6b25db73acde1888f06b92c8f16c87ebbe29015f5b52
    role: context
  - path: reviews/structured/20261022T032957Z-plastid-stroma-audit/review.yaml
    sha256: c720871647d0ee79fc341ae9122188743b57b0126deba5ced3346f04f37b4e17
    role: context
  - path: reviews/structured/20261022T032958Z-plastid-thylakoid-audit/review.md
    sha256: 10334897b0a3e0f998a01bf34ff25eeaf265f85ba9e16a749526185d1fb0e087
    role: context
  - path: reviews/structured/20261022T032958Z-plastid-thylakoid-audit/review.yaml
    sha256: 52d33d07dcc5220324e238d906c82c4e9c08bd3cf5a2ffc10dc0096fcc847fd5
    role: context
  - path: reviews/structured/20261022T032959Z-plastid-thylakoid-lumen-audit/review.md
    sha256: 7c6f9cf9501a06915e93f6c7c59549be57031b28a72ed3960322b2aceedc040e
    role: context
  - path: reviews/structured/20261022T032959Z-plastid-thylakoid-lumen-audit/review.yaml
    sha256: 6c6788f5b5bc7dbbd9d5e4fde20b0191a677dd93ff623ad95060f6a96f83d37b
    role: context
  - path: reviews/structured/20261022T033000Z-plastid-thylakoid-membrane-audit/review.md
    sha256: dedf7421a43e75d319345fb977be206db4d3c29622c3d7a962456dcf51d55d6b
    role: context
  - path: reviews/structured/20261022T033000Z-plastid-thylakoid-membrane-audit/review.yaml
    sha256: 36adab248fa393a33a16f6d364643e9d1c72ae8d8d8c78959c383c94aa883639
    role: context
  - path: reviews/structured/20261022T033000Z-polaroplast-audit/review.md
    sha256: 06a2ba92f7115d62b3b790624621a432a40db5c4903cb356196bd01a07229724
    role: context
  - path: reviews/structured/20261022T033000Z-polaroplast-audit/review.yaml
    sha256: 3ff3de0a207854971fcba962de9441e88400479b79261a7ac3f156e046410bde
    role: context
  - path: reviews/structured/20261022T033001Z-pusule-audit/review.md
    sha256: 693ce8b9c6c391f536ac1c9e22faf44b096c32d40d3d41a2cc56e2fb9ec4b999
    role: context
  - path: reviews/structured/20261022T033001Z-pusule-audit/review.yaml
    sha256: cabed5cf67f77e9ba0fbc42c52a5ca58f228bca641100969fdca23acdb7eb1aa
    role: context
  - path: reviews/structured/20261022T033002Z-pyrenoid-tubule-audit/review.md
    sha256: c6e6c61be9e689ec0d623e137fe4b0a181de376adb7b0eb373c59f589e2dca1a
    role: context
  - path: reviews/structured/20261022T033002Z-pyrenoid-tubule-audit/review.yaml
    sha256: 86891d8ba547b18479a840aedaf205aa3a18d4fbe16071a18a1a620a2afbe8c8
    role: context
  - path: reviews/structured/20261022T033003Z-recycling-endosome-audit/review.md
    sha256: 47a6713190213bbfcbfafc195882f3a1e7d5b8d5aaa525b7b72bc14bd9fea316
    role: context
  - path: reviews/structured/20261022T033003Z-recycling-endosome-audit/review.yaml
    sha256: 1f3826bc69bd0d47bd2ca0874f51a368f1db4841a507cf92e55a4a61557bd527
    role: context
  - path: reviews/structured/20261022T033003Z-recycling-endosome-lumen-audit/review.md
    sha256: 72994ed5fc0dd3330a8fd53373db8787a22fa3cbdd503eae78f5e8d5ff33083f
    role: context
  - path: reviews/structured/20261022T033003Z-recycling-endosome-lumen-audit/review.yaml
    sha256: 38cca0f4d52b044e8623cefb7a2d944e4ba7c5231523caba2cb616112c98ac7e
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
- target_id: GO:0009527
  path: data/structures/membrane_organelle/plastid_outer_membrane.yaml
  label: plastid outer membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/plastid_outer_membrane.yaml
    role: maintained scientific record
- target_id: GO:0009532
  path: data/structures/membrane_organelle/plastid_stroma.yaml
  label: plastid stroma
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/plastid_stroma.yaml
    role: maintained scientific record
- target_id: GO:0031976
  path: data/structures/membrane_organelle/plastid_thylakoid.yaml
  label: plastid thylakoid
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/plastid_thylakoid.yaml
    role: maintained scientific record
- target_id: GO:0031978
  path: data/structures/membrane_organelle/plastid_thylakoid_lumen.yaml
  label: plastid thylakoid lumen
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/plastid_thylakoid_lumen.yaml
    role: maintained scientific record
- target_id: GO:0055035
  path: data/structures/membrane_organelle/plastid_thylakoid_membrane.yaml
  label: plastid thylakoid membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/plastid_thylakoid_membrane.yaml
    role: maintained scientific record
- target_id: GO:0160201
  path: data/structures/membrane_organelle/polaroplast.yaml
  label: polaroplast
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/polaroplast.yaml
    role: maintained scientific record
- target_id: cellstructuremech:pusule
  path: data/structures/membrane_organelle/pusule.yaml
  label: pusule
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/pusule.yaml
    role: maintained scientific record
- target_id: GO:0160223
  path: data/structures/membrane_organelle/pyrenoid_tubule.yaml
  label: pyrenoid tubule
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/pyrenoid_tubule.yaml
    role: maintained scientific record
- target_id: GO:0055037
  path: data/structures/membrane_organelle/recycling_endosome.yaml
  label: recycling endosome
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/recycling_endosome.yaml
    role: maintained scientific record
- target_id: GO:0034777
  path: data/structures/membrane_organelle/recycling_endosome_lumen.yaml
  label: recycling endosome lumen
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/recycling_endosome_lumen.yaml
    role: maintained scientific record
scope:
  description: Exact ten-record PR cohort reassessed against current main a155c38220bee43550eac4ecff6ff2c0aee0823b.
    Changed inputs are substantively reassessed. Scientific records remain unchanged.
  selection: Complete cohort of ten maintained records reviewed in original PR head
    ee89490de10690a7dfadbad77ff2a331d4f24d42.
  coverage: full
  population_size: 10
  reviewed_target_ids:
  - GO:0009527
  - GO:0009532
  - GO:0031976
  - GO:0031978
  - GO:0055035
  - GO:0160201
  - cellstructuremech:pusule
  - GO:0160223
  - GO:0055037
  - GO:0034777
checks:
- check_id: qc
  name: Full native QC
  status: passed
  required: true
  target_ids:
  - GO:0009527
  - GO:0009532
  - GO:0031976
  - GO:0031978
  - GO:0055035
  - GO:0160201
  - cellstructuremech:pusule
  - GO:0160223
  - GO:0055037
  - GO:0034777
  command: just qc
  exit_code: 0
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  scope_note: Actual local execution at main-merge head 55020000323f1344e65128992b35f6ef43c703a2.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-qc
- check_id: labels
  name: Native label correspondence
  status: passed
  required: true
  target_ids:
  - GO:0009527
  - GO:0009532
  - GO:0031976
  - GO:0031978
  - GO:0055035
  - GO:0160201
  - cellstructuremech:pusule
  - GO:0160223
  - GO:0055037
  - GO:0034777
  command: just validate-products
  exit_code: 0
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  scope_note: Actual local execution at main-merge head 55020000323f1344e65128992b35f6ef43c703a2.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-labels
- check_id: trait-links
  name: TraitMech references
  status: passed
  required: true
  target_ids:
  - GO:0009527
  - GO:0009532
  - GO:0031976
  - GO:0031978
  - GO:0055035
  - GO:0160201
  - cellstructuremech:pusule
  - GO:0160223
  - GO:0055037
  - GO:0034777
  command: just check-trait-links --check
  exit_code: 0
  summary: Native TraitMech link check passed.
  scope_note: Actual local execution at main-merge head 55020000323f1344e65128992b35f6ef43c703a2.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-trait-links
- check_id: vendored
  name: Pinned governed files
  status: passed
  required: true
  target_ids:
  - GO:0009527
  - GO:0009532
  - GO:0031976
  - GO:0031978
  - GO:0055035
  - GO:0160201
  - cellstructuremech:pusule
  - GO:0160223
  - GO:0055037
  - GO:0034777
  command: just vendored-check
  exit_code: 0
  summary: Pinned governed files match; native vendored check passed.
  scope_note: Actual local execution at main-merge head 55020000323f1344e65128992b35f6ef43c703a2.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-vendored
- check_id: curies
  name: Native identifier resolver
  status: passed
  required: true
  target_ids:
  - GO:0009527
  - GO:0009532
  - GO:0031976
  - GO:0031978
  - GO:0055035
  - GO:0160201
  - cellstructuremech:pusule
  - GO:0160223
  - GO:0055037
  - GO:0034777
  command: just check-curies
  exit_code: 0
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  scope_note: Actual local execution at main-merge head 55020000323f1344e65128992b35f6ef43c703a2.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-curies
- check_id: focused-0
  name: validate GO:0009527
  status: passed
  required: true
  target_ids:
  - GO:0009527
  command: just validate data/structures/membrane_organelle/plastid_outer_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-1
  name: validate-strict GO:0009527
  status: passed
  required: true
  target_ids:
  - GO:0009527
  command: just validate-strict data/structures/membrane_organelle/plastid_outer_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-2
  name: validate GO:0009532
  status: passed
  required: true
  target_ids:
  - GO:0009532
  command: just validate data/structures/membrane_organelle/plastid_stroma.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-3
  name: validate-strict GO:0009532
  status: passed
  required: true
  target_ids:
  - GO:0009532
  command: just validate-strict data/structures/membrane_organelle/plastid_stroma.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-4
  name: validate GO:0031976
  status: passed
  required: true
  target_ids:
  - GO:0031976
  command: just validate data/structures/membrane_organelle/plastid_thylakoid.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-5
  name: validate-strict GO:0031976
  status: passed
  required: true
  target_ids:
  - GO:0031976
  command: just validate-strict data/structures/membrane_organelle/plastid_thylakoid.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-6
  name: validate GO:0031978
  status: passed
  required: true
  target_ids:
  - GO:0031978
  command: just validate data/structures/membrane_organelle/plastid_thylakoid_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-7
  name: validate-strict GO:0031978
  status: passed
  required: true
  target_ids:
  - GO:0031978
  command: just validate-strict data/structures/membrane_organelle/plastid_thylakoid_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-8
  name: validate GO:0055035
  status: passed
  required: true
  target_ids:
  - GO:0055035
  command: just validate data/structures/membrane_organelle/plastid_thylakoid_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-9
  name: validate-strict GO:0055035
  status: passed
  required: true
  target_ids:
  - GO:0055035
  command: just validate-strict data/structures/membrane_organelle/plastid_thylakoid_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-10
  name: validate GO:0160201
  status: passed
  required: true
  target_ids:
  - GO:0160201
  command: just validate data/structures/membrane_organelle/polaroplast.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-11
  name: validate-strict GO:0160201
  status: passed
  required: true
  target_ids:
  - GO:0160201
  command: just validate-strict data/structures/membrane_organelle/polaroplast.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-12
  name: validate cellstructuremech:pusule
  status: passed
  required: true
  target_ids:
  - cellstructuremech:pusule
  command: just validate data/structures/membrane_organelle/pusule.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-13
  name: validate-strict cellstructuremech:pusule
  status: passed
  required: true
  target_ids:
  - cellstructuremech:pusule
  command: just validate-strict data/structures/membrane_organelle/pusule.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-14
  name: validate GO:0160223
  status: passed
  required: true
  target_ids:
  - GO:0160223
  command: just validate data/structures/membrane_organelle/pyrenoid_tubule.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-15
  name: validate-strict GO:0160223
  status: passed
  required: true
  target_ids:
  - GO:0160223
  command: just validate-strict data/structures/membrane_organelle/pyrenoid_tubule.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-16
  name: validate GO:0055037
  status: passed
  required: true
  target_ids:
  - GO:0055037
  command: just validate data/structures/membrane_organelle/recycling_endosome.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-17
  name: validate-strict GO:0055037
  status: passed
  required: true
  target_ids:
  - GO:0055037
  command: just validate-strict data/structures/membrane_organelle/recycling_endosome.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-18
  name: validate GO:0034777
  status: passed
  required: true
  target_ids:
  - GO:0034777
  command: just validate data/structures/membrane_organelle/recycling_endosome_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-19
  name: validate-strict GO:0034777
  status: passed
  required: true
  target_ids:
  - GO:0034777
  command: just validate-strict data/structures/membrane_organelle/recycling_endosome_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: supplemental-pmid
  name: Supplemental bounded PMID authority checks
  status: passed
  required: true
  target_ids:
  - GO:0009527
  - GO:0009532
  - GO:0031976
  - GO:0031978
  - GO:0055035
  - GO:0160201
  - cellstructuremech:pusule
  - GO:0160223
  - GO:0055037
  - GO:0034777
  command: .venv/bin/python /private/tmp/cellstructure-batches-2346-2397-20261103/check_pmid_chunks.py
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376
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
  - GO:0009527
  - GO:0009532
  - GO:0031976
  - GO:0031978
  - GO:0055035
  - GO:0160201
  - cellstructuremech:pusule
  - GO:0160223
  - GO:0055037
  - GO:0034777
  summary: 'Seven targets assert positive molecular/pathway claims: plastid outer
    membrane, stroma, whole thylakoid, thylakoid membrane, pyrenoid tubule and both
    recycling-endosome records. Five unsupported explicit check exclusions and two
    prose-only exclusions are corrected using actual catalogue coverage and bounded
    applicable source checks. Thylakoid lumen, polaroplast and pusule retain genuine
    physical/anatomical exclusions. Noncoverage is not biological absence and unrelated
    hosts are not substitutes. Historical runner unavailability remains historical;
    actual source fallback access scopes and timestamps are retained.'
  evidence_ids:
  - septin-catalogue
  - plaque-catalogue
  - micro-catalogue-api
- check_id: independent-scientific-review
  name: Independent claim-level source review
  status: passed
  required: true
  target_ids:
  - GO:0009527
  - GO:0009532
  - GO:0031976
  - GO:0031978
  - GO:0055035
  - GO:0160201
  - cellstructuremech:pusule
  - GO:0160223
  - GO:0055037
  - GO:0034777
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
  - septin-SL0232
  - septin-SL0345
  - septin-tax2759
  - septin-tax3055
  - septin-tax5691
  - septin-Q9NJE8
  - septin-engel2015-jats
  - septin-he2023-jats
  - septin-franklin2026-jats
  - septin-umaer2018-pmc
  - plaque-policy
  - plaque-rubric
  - plaque-schema-policy
  - plaque-history-policy
  - plaque-go-polar
  - plaque-go-pusule
  - plaque-tax-6029
  - plaque-tax-27978
  - plaque-tax-271679
  - plaque-tax-2945
  - plaque-tax-2961
  - plaque-han-meta
  - plaque-chen-meta
  - plaque-lv-meta
  - plaque-gavelis-meta
  - plaque-han-body
  - plaque-chen-jats
  - plaque-lv-jats
  - plaque-dodge-meta
  - plaque-dodge-publisher
  - plaque-klut-meta
  - plaque-gavelis-jats
  - plaque-gavelis-fig2
  - plaque-catalogue
  - micro-policy
  - micro-component-policy
  - micro-graph-policy
  - micro-discussion-policy
  - micro-go
  - micro-GO0009527-isa
  - micro-GO0031976-isa
  - micro-GO0031978-isa
  - micro-GO0055035-isa
  - micro-GO0070118-isa
  - micro-SL-0214
  - micro-SL-0215
  - micro-SL-0278
  - micro-SL-0082
  - micro-SL-0356
  - micro-tax2759
  - micro-tax33090
  - micro-tax3055
  - micro-tax38254
  - micro-keeling-metadata
  - micro-terashima-metadata
  - micro-perez-metadata
  - micro-engel-metadata
  - micro-jin-metadata
  - micro-keeling-retained
  - micro-terashima-retained
  - micro-perez-retained
  - micro-engel-primary
- check_id: historical-adapter-runner
  name: Retained historical adapter runner availability
  status: unavailable
  required: false
  target_ids:
  - GO:0009527
  - GO:0009532
  - GO:0031976
  - GO:0031978
  - GO:0055035
  - GO:0160201
  - cellstructuremech:pusule
  - GO:0160223
  - GO:0055037
  - GO:0034777
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
- check_id: plastid_outer_membrane-uniprot-verify
  name: Native plastid outer membrane UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0009527
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_outer_membrane.yaml
    --verify
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-plastid_outer_membrane-uniprot-verify
- check_id: plastid_outer_membrane-uniprot-causal
  name: Native plastid outer membrane UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0009527
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_outer_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-plastid_outer_membrane-uniprot-causal
- check_id: plastid_stroma-uniprot-verify
  name: Native plastid stroma UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0009532
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_stroma.yaml
    --verify
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-plastid_stroma-uniprot-verify
- check_id: plastid_stroma-uniprot-causal
  name: Native plastid stroma UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0009532
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_stroma.yaml
    --causal-graphs
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-plastid_stroma-uniprot-causal
- check_id: plastid_thylakoid-uniprot-verify
  name: Native plastid thylakoid UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0031976
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_thylakoid.yaml
    --verify
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-plastid_thylakoid-uniprot-verify
- check_id: plastid_thylakoid-uniprot-causal
  name: Native plastid thylakoid UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0031976
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_thylakoid.yaml
    --causal-graphs
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-plastid_thylakoid-uniprot-causal
- check_id: plastid_thylakoid_lumen-uniprot-verify
  name: Native plastid thylakoid lumen UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0031978
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_thylakoid_lumen.yaml
    --verify
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-plastid_thylakoid_lumen-uniprot-verify
- check_id: plastid_thylakoid_lumen-uniprot-causal
  name: Native plastid thylakoid lumen UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0031978
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_thylakoid_lumen.yaml
    --causal-graphs
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-plastid_thylakoid_lumen-uniprot-causal
- check_id: plastid_thylakoid_membrane-uniprot-verify
  name: Native plastid thylakoid membrane UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0055035
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_thylakoid_membrane.yaml
    --verify
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-plastid_thylakoid_membrane-uniprot-verify
- check_id: plastid_thylakoid_membrane-uniprot-causal
  name: Native plastid thylakoid membrane UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0055035
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_thylakoid_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-plastid_thylakoid_membrane-uniprot-causal
- check_id: polaroplast-uniprot-verify
  name: Native polaroplast UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0160201
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/polaroplast.yaml
    --verify
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-polaroplast-uniprot-verify
- check_id: polaroplast-uniprot-causal
  name: Native polaroplast UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0160201
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/polaroplast.yaml
    --causal-graphs
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-polaroplast-uniprot-causal
- check_id: pusule-uniprot-verify
  name: Native pusule UniProt verify check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:pusule
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/pusule.yaml
    --verify
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-pusule-uniprot-verify
- check_id: pusule-uniprot-causal
  name: Native pusule UniProt causal check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:pusule
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/pusule.yaml
    --causal-graphs
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-pusule-uniprot-causal
- check_id: pyrenoid_tubule-uniprot-verify
  name: Native pyrenoid tubule UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0160223
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/pyrenoid_tubule.yaml
    --verify
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-pyrenoid_tubule-uniprot-verify
- check_id: pyrenoid_tubule-uniprot-causal
  name: Native pyrenoid tubule UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0160223
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/pyrenoid_tubule.yaml
    --causal-graphs
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-pyrenoid_tubule-uniprot-causal
- check_id: recycling_endosome-uniprot-verify
  name: Native recycling endosome UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0055037
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/recycling_endosome.yaml
    --verify
  exit_code: 0
  summary: 0 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-recycling_endosome-uniprot-verify
- check_id: recycling_endosome-uniprot-causal
  name: Native recycling endosome UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0055037
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/recycling_endosome.yaml
    --causal-graphs
  exit_code: 0
  summary: 0 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-recycling_endosome-uniprot-causal
- check_id: recycling_endosome_lumen-uniprot-verify
  name: Native recycling endosome lumen UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0034777
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/recycling_endosome_lumen.yaml
    --verify
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-recycling_endosome_lumen-uniprot-verify
- check_id: recycling_endosome_lumen-uniprot-causal
  name: Native recycling endosome lumen UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0034777
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/recycling_endosome_lumen.yaml
    --causal-graphs
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-recycling_endosome_lumen-uniprot-causal
evidence:
- evidence_id: current-record-0
  kind: record_content
  reference: data/structures/membrane_organelle/plastid_outer_membrane.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T20:49:39Z'
  support: context_only
  summary: Original frozen SHA256 59bd8548931d27f711233f542b5f927c0e7b0a68dd611eabb4777ee08003deaa;
    current SHA256 59bd8548931d27f711233f542b5f927c0e7b0a68dd611eabb4777ee08003deaa.
    Record bytes unchanged since the original review.
  snapshot_sha256: 59bd8548931d27f711233f542b5f927c0e7b0a68dd611eabb4777ee08003deaa
- evidence_id: original-review-0
  kind: prior_review
  reference: reviews/structured/20261022T032956Z-plastid-outer-membrane-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T20:49:39Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 13834625be15bdee042f39f764b0f9557c5ea353bf9a718a3ee83cd8977afb99
- evidence_id: current-record-1
  kind: record_content
  reference: data/structures/membrane_organelle/plastid_stroma.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T20:49:39Z'
  support: context_only
  summary: Original frozen SHA256 86d19307cbe21273498f0d7d6741e61f5ebf002cf78418c34b922d9d4963503b;
    current SHA256 86d19307cbe21273498f0d7d6741e61f5ebf002cf78418c34b922d9d4963503b.
    Record bytes unchanged since the original review.
  snapshot_sha256: 86d19307cbe21273498f0d7d6741e61f5ebf002cf78418c34b922d9d4963503b
- evidence_id: original-review-1
  kind: prior_review
  reference: reviews/structured/20261022T032957Z-plastid-stroma-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T20:49:39Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: c720871647d0ee79fc341ae9122188743b57b0126deba5ced3346f04f37b4e17
- evidence_id: current-record-2
  kind: record_content
  reference: data/structures/membrane_organelle/plastid_thylakoid.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T20:49:39Z'
  support: context_only
  summary: Original frozen SHA256 ec3c74ee89bf25eea6a3a5682b3f7f73e0837465dccf2a8f2c0cce1550a4e3c8;
    current SHA256 ec3c74ee89bf25eea6a3a5682b3f7f73e0837465dccf2a8f2c0cce1550a4e3c8.
    Record bytes unchanged since the original review.
  snapshot_sha256: ec3c74ee89bf25eea6a3a5682b3f7f73e0837465dccf2a8f2c0cce1550a4e3c8
- evidence_id: original-review-2
  kind: prior_review
  reference: reviews/structured/20261022T032958Z-plastid-thylakoid-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T20:49:39Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 52d33d07dcc5220324e238d906c82c4e9c08bd3cf5a2ffc10dc0096fcc847fd5
- evidence_id: current-record-3
  kind: record_content
  reference: data/structures/membrane_organelle/plastid_thylakoid_lumen.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T20:49:39Z'
  support: context_only
  summary: Original frozen SHA256 7a75c5aee47a20bbae7da6351e07fc7f2d1dc418e7ca34e253d08e3a531ff4ee;
    current SHA256 7a75c5aee47a20bbae7da6351e07fc7f2d1dc418e7ca34e253d08e3a531ff4ee.
    Record bytes unchanged since the original review.
  snapshot_sha256: 7a75c5aee47a20bbae7da6351e07fc7f2d1dc418e7ca34e253d08e3a531ff4ee
- evidence_id: original-review-3
  kind: prior_review
  reference: reviews/structured/20261022T032959Z-plastid-thylakoid-lumen-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T20:49:39Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 6c6788f5b5bc7dbbd9d5e4fde20b0191a677dd93ff623ad95060f6a96f83d37b
- evidence_id: current-record-4
  kind: record_content
  reference: data/structures/membrane_organelle/plastid_thylakoid_membrane.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T20:49:39Z'
  support: context_only
  summary: Original frozen SHA256 51a2ece521e1b5c0b3b589fc7cf665be1c9544299257e0fda7fcf8352e7401c2;
    current SHA256 51a2ece521e1b5c0b3b589fc7cf665be1c9544299257e0fda7fcf8352e7401c2.
    Record bytes unchanged since the original review.
  snapshot_sha256: 51a2ece521e1b5c0b3b589fc7cf665be1c9544299257e0fda7fcf8352e7401c2
- evidence_id: original-review-4
  kind: prior_review
  reference: reviews/structured/20261022T033000Z-plastid-thylakoid-membrane-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T20:49:39Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 36adab248fa393a33a16f6d364643e9d1c72ae8d8d8c78959c383c94aa883639
- evidence_id: current-record-5
  kind: record_content
  reference: data/structures/membrane_organelle/polaroplast.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T20:49:39Z'
  support: context_only
  summary: Original frozen SHA256 b755d59c2ad21e4b73e222a7d9979859a4d4b5c3c9f4543f9695dc3749beff69;
    current SHA256 33a7618c43eea5924263584a6faa84d6190ff1198bfdb1ca2903d49e726c2642.
    Changed record reassessed against current sources.
  snapshot_sha256: 33a7618c43eea5924263584a6faa84d6190ff1198bfdb1ca2903d49e726c2642
- evidence_id: original-review-5
  kind: prior_review
  reference: reviews/structured/20261022T033000Z-polaroplast-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T20:49:39Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 3ff3de0a207854971fcba962de9441e88400479b79261a7ac3f156e046410bde
- evidence_id: current-record-6
  kind: record_content
  reference: data/structures/membrane_organelle/pusule.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T20:49:39Z'
  support: context_only
  summary: Original frozen SHA256 3bc5082b5e3b721414b9b2d57c585c1a278de5053885f34f55b40ccd4b71a6ae;
    current SHA256 3bc5082b5e3b721414b9b2d57c585c1a278de5053885f34f55b40ccd4b71a6ae.
    Record bytes unchanged since the original review.
  snapshot_sha256: 3bc5082b5e3b721414b9b2d57c585c1a278de5053885f34f55b40ccd4b71a6ae
- evidence_id: original-review-6
  kind: prior_review
  reference: reviews/structured/20261022T033001Z-pusule-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T20:49:39Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: cabed5cf67f77e9ba0fbc42c52a5ca58f228bca641100969fdca23acdb7eb1aa
- evidence_id: current-record-7
  kind: record_content
  reference: data/structures/membrane_organelle/pyrenoid_tubule.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T20:49:39Z'
  support: context_only
  summary: Original frozen SHA256 dd5c61f94612f6c30f259f029b7f4bc4daa8a7d4c0fa8111f6eb0715f78483d7;
    current SHA256 dd5c61f94612f6c30f259f029b7f4bc4daa8a7d4c0fa8111f6eb0715f78483d7.
    Record bytes unchanged since the original review.
  snapshot_sha256: dd5c61f94612f6c30f259f029b7f4bc4daa8a7d4c0fa8111f6eb0715f78483d7
- evidence_id: original-review-7
  kind: prior_review
  reference: reviews/structured/20261022T033002Z-pyrenoid-tubule-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T20:49:39Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 86891d8ba547b18479a840aedaf205aa3a18d4fbe16071a18a1a620a2afbe8c8
- evidence_id: current-record-8
  kind: record_content
  reference: data/structures/membrane_organelle/recycling_endosome.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T20:49:39Z'
  support: context_only
  summary: Original frozen SHA256 7a806e4e4eaddd3578c517d587c4eaaf1c458e4f5cfc2e59065fc0f26594ac48;
    current SHA256 7a806e4e4eaddd3578c517d587c4eaaf1c458e4f5cfc2e59065fc0f26594ac48.
    Record bytes unchanged since the original review.
  snapshot_sha256: 7a806e4e4eaddd3578c517d587c4eaaf1c458e4f5cfc2e59065fc0f26594ac48
- evidence_id: original-review-8
  kind: prior_review
  reference: reviews/structured/20261022T033003Z-recycling-endosome-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T20:49:39Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 1f3826bc69bd0d47bd2ca0874f51a368f1db4841a507cf92e55a4a61557bd527
- evidence_id: current-record-9
  kind: record_content
  reference: data/structures/membrane_organelle/recycling_endosome_lumen.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T20:49:39Z'
  support: context_only
  summary: Original frozen SHA256 69bc318299125a4de316f2ba3b7fc20e0655bca2d37fa6d43c12afcfa3fc3ce2;
    current SHA256 69bc318299125a4de316f2ba3b7fc20e0655bca2d37fa6d43c12afcfa3fc3ce2.
    Record bytes unchanged since the original review.
  snapshot_sha256: 69bc318299125a4de316f2ba3b7fc20e0655bca2d37fa6d43c12afcfa3fc3ce2
- evidence_id: original-review-9
  kind: prior_review
  reference: reviews/structured/20261022T033003Z-recycling-endosome-lumen-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T20:49:39Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 38cca0f4d52b044e8623cefb7a2d944e4ba7c5231523caba2cb616112c98ac7e
- evidence_id: septin-review-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Current molecular/pathway applicability and bounded fallback
  summary: Positive molecular or pathway assertions trigger structured-source applicability
    even without an expression claim or individual examples. Use matched organism/strain
    evidence; source unavailability is not scientific absence.
  accessed_at: '2026-11-03T20:48:47.553933Z'
  support: supports
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: septin-curation-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Identity, constituent evidence, generic classes and append-only discussion
  summary: Exact structure identity, material identity, localization and formation
    necessity are distinct. Dated rationale is provenance, not a current inventory;
    optional examples and generic classes do not automatically require curation.
  accessed_at: '2026-11-03T20:48:47.553933Z'
  support: supports
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
- evidence_id: septin-schema-policy
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Structure, material, graph and evidence contract
  summary: Whole-membrane GO identity is structural rather than a molecular lipid
    class. Collective label-only material and externally grounded regulatory graph
    nodes are valid scoped representations.
  accessed_at: '2026-11-03T20:48:47.553933Z'
  support: supports
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: septin-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Mechanistic scope and graph actors/relations
  summary: Descriptive topology and process association are assessed against their
    declared NONMECHANISTIC scope. No complete molecular causal chain or obligatory
    regulator-as-constituent representation is imposed.
  accessed_at: '2026-11-03T20:48:47.553933Z'
  support: supports
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: septin-protein-policy
  kind: authority
  reference: .claude/skills/uniprot-protein-examples/SKILL.md
  locator: Native examples and graph coverage
  summary: Native accession and coverage checks certify represented inputs only; an
    empty example inventory is neither molecular completeness nor biological absence.
  accessed_at: '2026-11-03T20:48:47.553933Z'
  support: supports
  snapshot_sha256: 6462894c8257823bae2b175c34693cd42f11ff9269a3829c15b9286ba6d7c876
- evidence_id: septin-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0160223,GO:0016020,GO:1990732,GO:0042651,GO:0055037,GO:0055038,GO:0034777,GO:0005768,GO:0031904
  locator: 'All nine exact current GO entries: complete definitions/synonyms and immediate
    typed child relations'
  summary: GO0160223 denotes pyrenoid-traversing membrane, distinct from whole GO1990732
    and thylakoid membrane GO0042651. GO0055037 is the recycling organelle, GO0055038
    its surrounding lipid bilayer and GO0034777 its enclosed volume; endosome/endosome-lumen
    parent entries expose the corresponding is-a children. Immediate pyrenoid part
    relations and recycling parts are distinguished from is-a. GO0016020 describes
    a whole membrane, not a source-neutral molecular lipid identity; no unqueried
    full-ancestry result is claimed.
  accessed_at: '2026-11-03T20:43:22.937169Z'
  support: supports
  snapshot_sha256: 1fc7e4c66c46d6d6e4cbd4d010c33315e916514335c8639f65e6285a33833e87
- evidence_id: septin-SL0232
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0232.json
  locator: Complete exact location entry and immediate typed isA/partOf fields; nested
    boundary text read
  summary: Exact recycling-endosome location maps GO0055037 and describes Rab11 as
    a marker. Its relation to endosome is partOf in this response, while the record
    is-a claim is separately supported by GO; no conflation of these predicates.
  accessed_at: '2026-11-03T20:43:22.937438Z'
  support: supports
  snapshot_sha256: 0736135ed5a32ec69b72230194e431e0f6ea8eff90192e13e34594c7ce68163b
- evidence_id: septin-SL0345
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0345.json
  locator: Complete exact location entry and immediate typed isA/partOf fields; nested
    boundary text read
  summary: Exact recycling-endosome-lumen maps GO0034777 and supplies recycling endosomal
    lumen synonym, endosome-lumen isA and recycling-endosome partOf.
  accessed_at: '2026-11-03T20:43:22.937535Z'
  support: supports
  snapshot_sha256: c63ca9bd1055d1cb224612d7610c2451a92f253a07790db1a69dceafdf24501c
- evidence_id: septin-tax2759
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759
  locator: 'Complete current ENA/NCBI taxonomy response: identifier, rank, status
    and lineage'
  summary: Current Eukaryota domain identifier supports lineage identity, not a prevalence
    census.
  accessed_at: '2026-11-03T20:43:22.937598Z'
  support: supports
  snapshot_sha256: 61a68c76c70762c97e0b218568ab037d9a30c0207847247e9e055b5764a61634
- evidence_id: septin-tax3055
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3055
  locator: 'Complete current ENA/NCBI taxonomy response: identifier, rank, status
    and lineage'
  summary: Current Chlamydomonas reinhardtii species identifier; actual Engel experiment
    uses CC124(137c), independently established from Methods.
  accessed_at: '2026-11-03T20:43:22.937647Z'
  support: supports
  snapshot_sha256: e3861fe6706cefe2e079e15c0178a65e95efaad3890f548f25e721553eaa93a0
- evidence_id: septin-tax5691
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5691
  locator: 'Complete current ENA/NCBI taxonomy response: identifier, rank, status
    and lineage'
  summary: Current Trypanosoma brucei species identifier; Umaer independently specifies
    bloodstream T. b. brucei single-marker cells, not every strain or life stage.
  accessed_at: '2026-11-03T20:43:23.528349Z'
  support: supports
  snapshot_sha256: ba78ff6fe5de62b2654b61e249c2c87b239dca0208950b0e4ecf3ef2d81c99be
- evidence_id: septin-Q9NJE8
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q9NJE8.json
  locator: 'Complete current UniProt JSON: entry status, taxon, primary gene/synonym,
    submitted names, references, sequence and similarity evidence'
  summary: Unreviewed TrEMBL Q9NJE8 is T. brucei tax5691, primary gene Rab11, synonym
    RAB11A, with submitted RAB11A GTPase/small GTPase Rab11 names. Family similarity
    is inferred annotation, not a new localization experiment. Original sequence references
    include Jeffries/Field and PMID11683389. Identity is consistent with the graph
    marker, but no sequence alignment or strain-level equivalence to the Umaer Tb927.8.4330
    RNAi construct was performed.
  accessed_at: '2026-11-03T20:43:23.532961Z'
  support: supports
  snapshot_sha256: 69f602df124a0fc610ec0b6bfa97586217334d88d3a6ab4dd8c8f02840268343
- evidence_id: septin-engel2015-meta
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.7554/eLife.04889&format=json&resultType=core&pageSize=25
  locator: Exact EuropePMC DOI or MED identifier query; complete single-hit metadata
    and abstract
  summary: Engel2015 Native architecture of the Chlamydomonas chloroplast revealed
    by in situ cryo-electron tomography; primary study PMID25584625/PMC4292175.
  accessed_at: '2026-11-03T20:43:23.569732Z'
  support: supports
  snapshot_sha256: e871243bee6520756b75290d986d9df20b09b14d80b6ba888a5a1048eeb85e9d
  search_scope: EuropePMC REST exact query in reference URL, resultType=core,pageSize25,no
    date filter; one exact returned result completely inspected at 2026-11-03T20:43:23.569732Z.
    No broad literature-absence inference.
- evidence_id: septin-he2023-meta
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1093/plcell/koad157&format=json&resultType=core&pageSize=25
  locator: Exact EuropePMC DOI or MED identifier query; complete single-hit metadata
    and abstract
  summary: 'He, Crans and Jonikas2023 The pyrenoid: the eukaryotic CO2-concentrating
    organelle is a secondary review, PMID37279536/PMC10473226.'
  accessed_at: '2026-11-03T20:43:23.573112Z'
  support: supports
  snapshot_sha256: 18ea467621a67b89ceca80040bc93a17b15bdead3a98d6ebd6ee7a7e7fe32a40
  search_scope: EuropePMC REST exact query in reference URL, resultType=core,pageSize25,no
    date filter; one exact returned result completely inspected at 2026-11-03T20:43:23.573112Z.
    No broad literature-absence inference.
- evidence_id: septin-franklin2026-meta
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1111/nph.70669&format=json&resultType=core&pageSize=25
  locator: Exact EuropePMC DOI or MED identifier query; complete single-hit metadata
    and abstract
  summary: 'Franklin et al. Proteomic analysis of the pyrenoid-traversing membranes
    of Chlamydomonas reinhardtii reveals novel components, PMID41116735/PMC12676092:
    online first2025-10-21 and journal publication year2026 are distinct valid dates;
    record2026 is not a demonstrated bibliographic error.'
  accessed_at: '2026-11-03T20:43:23.598149Z'
  support: supports
  snapshot_sha256: 0b76189820a855de575171013c5471fe2925fa746aa260c2b87cb679e1783cfd
  search_scope: EuropePMC REST exact query in reference URL, resultType=core,pageSize25,no
    date filter; one exact returned result completely inspected at 2026-11-03T20:43:23.598149Z.
    No broad literature-absence inference.
- evidence_id: septin-jeffries2001-meta
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11683389%20AND%20SRC%3AMED&format=json&resultType=core&pageSize=25
  locator: Exact EuropePMC DOI or MED identifier query; complete single-hit metadata
    and abstract
  summary: 'Jeffries, Morgan and Field2001 PMID11683389/DOI10.1242/jcs.114.14.2617:
    complete abstract supports developmental differences and colocalization of TbRAB11
    compartments with transferrin receptor and internalized anti-VSG cargo. Publisher
    body attempt403; exact strain/Methods/pixels not certified.'
  accessed_at: '2026-11-03T20:43:24.122044Z'
  support: supports
  snapshot_sha256: 47119d081d8f1c7a80b63125de10f3688288733071805146639a1877e40653f0
  search_scope: EuropePMC REST exact query in reference URL, resultType=core,pageSize25,no
    date filter; one exact returned result completely inspected at 2026-11-03T20:43:24.122044Z.
    No broad literature-absence inference.
- evidence_id: septin-pal2003-meta
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12744719%20AND%20SRC%3AMED&format=json&resultType=core&pageSize=25
  locator: Exact EuropePMC DOI or MED identifier query; complete single-hit metadata
    and abstract
  summary: 'Pal, Hall, Jeffries and Field2003 PMID12744719/DOI10.1042/bj20030469:
    complete abstract describes uptake, substantial degradation and exocytosed products
    after transferrin/anti-VSG antibody entry, with mutant-dependent kinetics. This
    is not proof of intact ligand recycling or a universal endogenous-cargo requirement.
    Genuine body unavailable in attempted endpoints.'
  accessed_at: '2026-11-03T20:43:24.248346Z'
  support: supports
  snapshot_sha256: 8b3d1548e3eee9adec24dd5a22b5c3ba4928270b7b5bd973231c407adf093aa6
  search_scope: EuropePMC REST exact query in reference URL, resultType=core,pageSize25,no
    date filter; one exact returned result completely inspected at 2026-11-03T20:43:24.248346Z.
    No broad literature-absence inference.
- evidence_id: septin-umaer2018-meta
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A29582527%20AND%20SRC%3AMED&format=json&resultType=core&pageSize=25
  locator: Exact EuropePMC DOI or MED identifier query; complete single-hit metadata
    and abstract
  summary: 'Umaer, Bush and Bangs2018 PMID29582527/DOI10.1111/tra.12565: selective
    recycling and endocytic trafficking. Complete metadata/abstract checked separately
    from genuine full scientific body.'
  accessed_at: '2026-11-03T20:43:24.251391Z'
  support: supports
  snapshot_sha256: 6076e382a4d251e3158c62bb050d77172ba946f9c35b40e4514a82f1f72aa314
  search_scope: EuropePMC REST exact query in reference URL, resultType=core,pageSize25,no
    date filter; one exact returned result completely inspected at 2026-11-03T20:43:24.251391Z.
    No broad literature-absence inference.
- evidence_id: septin-engel2015-jats
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4292175/fullTextXML
  locator: Genuine JATS Results s2-5, Discussion s3-3, Methods s4-1 through s4-4;
    Fig11 and Video6 text captions; no pixels/video/supplements/raw tomograms
  summary: In situ cryo-FIB/cryoET of C. reinhardtii CC124(137c) grown in TAP under
    constant light resolves thylakoid sheets merging into pyrenoid-crossing tubules
    containing parallel minitubules. Tubule lumen is continuous with thylakoid lumen,
    whereas minitubule lumen connects interthylakoid stroma and matrix. Transport/CO2
    mechanisms in Discussion are contextual proposals/prior work, not directly measured
    flux in these tomograms. Record retains coarse topology and qualified function.
  accessed_at: '2026-11-03T20:43:24.342979Z'
  support: supports
  snapshot_sha256: 5d5e176465dc54f9a8b7a3b0faace8d7ccfa56ee57bece00723d4b451ff68026
- evidence_id: septin-he2023-jats
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10473226/fullTextXML
  locator: Genuine secondary JATS Introduction koad157-s0, operating principles s1.1
    and pyrenoid-associated membranes s2.2, embedded Fig1/2 text captions; no source
    pixels or reference-body audit
  summary: Review supports structural diversity, absence of traversing membranes in
    some pyrenoids and qualified CO2-delivery models. Chlamydomonas carbonic-anhydrase/bestrophin
    model is not a demonstrated universal protein inventory. Matrix-independent tubules
    and uncertain minitubule function do not undermine the record topology. Secondary
    synthesis is explicitly distinguished from primary experimentation.
  accessed_at: '2026-11-03T20:43:24.451127Z'
  support: supports
  snapshot_sha256: 2f3a9d60840a95a3417b319dd5d3c565ce0a78f1e917fe1cdf8f086739c027b9
- evidence_id: septin-franklin2026-jats
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12676092/fullTextXML
  locator: Genuine JATS Introduction sec0001, Methods sec0003/0004 including Table1/Fig2
    text, Results sec0011/0012 including Fig1/Table2 text, Discussion sec0019/0020;
    no candidate-specific mutant results/pixels/supplements/raw MS
  summary: RBMP1/2 baits enrich sonicated pyrenoid-associated membrane fragments relative
    to thylakoid controls, not detergent-solubilized direct interaction complexes.
    Proteomic enrichment is nonexhaustive localization context, not every candidate
    being essential. Intro/Discussion qualify CO2-supply function and support tubule
    traversal. CMJ030 context is used without certifying an internally inconsistent
    CC number across source Table1 and one Methods sentence. Record only claims species-level
    scope, coarse enrichment and qualified function.
  accessed_at: '2026-11-03T20:43:24.750447Z'
  support: supports
  snapshot_sha256: 845ba83cf3f615a9649b4e74e85788a8624e3f1aa2edb2006f429db4f055023f
- evidence_id: septin-umaer2018-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC5948159/
  locator: 'Genuine PMC scientific body: complete Introduction/Results/Discussion
    and Methods (derived text lines86–177), Fig1–9 text captions; no image pixels/supplement/raw
    data'
  summary: Bloodstream T. b. brucei single-marker RNAi targets Tb927.8.4330; early
    assays precede terminal growth failure. Rab11 silencing reduces ISG65 recycling
    and increases its lysosomal turnover, while VSG and transferrin-receptor trafficking
    are largely unaffected. Surface flow assay does not distinguish every cargo; radioligand-product
    exocytosis in earlier Pal work is distinct from endogenous recycling. Current
    graph says selective/Rab11-dependent support, not universal dependence or organelle-formation
    necessity. Methods establish source conditions; authority accession identity is
    not claimed to be sequence-matched to this construct.
  accessed_at: '2026-11-03T20:43:57.224744Z'
  support: supports
  snapshot_sha256: 53bb8925802d45bfb04f1853e842dcda8def3716f683c49264376ee725c12ee8
- evidence_id: septin-catalogue
  kind: search
  reference: https://imodulondb.org/api/datasets
  locator: Complete fresh official organism/dataset catalogue; all returned organism
    rows and dataset strings read
  summary: No Chlamydomonas/green-algal, Trypanosoma/Discoba or other eukaryotic host
    dataset is present in this bounded snapshot. Cyanobacterial s_elongatus coverage
    is not a proxy for a eukaryotic chloroplast or trypanosome. No matched downstream
    query is justified; primary/authority source fallback is used. Noncoverage is
    not biological absence.
  accessed_at: '2026-11-03T20:43:23.539462Z'
  support: supports
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  search_scope: GET https://imodulondb.org/api/datasets at 2026-11-03T20:43:23.539462Z;
    complete20 organism rows,28 organism-dataset pairs and22 unique dataset strings,
    no filters/date limit/truncation. All IDs/names/descriptions/keys inspected against
    actual named hosts; no broader database-absence claim.
- evidence_id: septin-adapter-runner-historical
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical attempted runner; no fresh invocation
  summary: Actual00:49:00.848907Z–00:49:00.863225Z exit1 PermissionError reading runner
    pyvenv.cfg is retained only as historical availability evidence. Fresh HTTP catalogue
    and source fallback are separate and are not a new runner success.
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: supports
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: septin-retrieval-source-receipts
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/adversary-septin/source-receipts.json
  locator: Actual fresh HTTP attempt receipts and successful-body hashes
  summary: Current genuine Engel/He/Franklin JATS and Umaer HTML are distinguished
    from Umaer/Pal XML500, Jeffries publisher403, and Pal HTTP200 proof-of-work preparation
    HTML at the apparent PDF URL. That1817-byte response is not a PDF. Complete Pal/Jeffries
    abstracts are used within their scope; unavailable Methods/pixels are not treated
    as evidence against the record.
  accessed_at: '2026-11-03T20:48:47.553933Z'
  support: supports
  snapshot_sha256: 6b0e4020dc7edb086bfe5e37ca7faa9d574ede4bce8c9e523d48081a8ba9380d
- evidence_id: septin-retrieval-additional-source-receipts
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/adversary-septin/additional-source-receipts.json
  locator: Actual fresh HTTP attempt receipts and successful-body hashes
  summary: Current genuine Engel/He/Franklin JATS and Umaer HTML are distinguished
    from Umaer/Pal XML500, Jeffries publisher403, and Pal HTTP200 proof-of-work preparation
    HTML at the apparent PDF URL. That1817-byte response is not a PDF. Complete Pal/Jeffries
    abstracts are used within their scope; unavailable Methods/pixels are not treated
    as evidence against the record.
  accessed_at: '2026-11-03T20:48:47.553933Z'
  support: supports
  snapshot_sha256: 92356bbc7a41941fa0a7533fe95676e4279ec42841c1183d2056be0e5b0df13f
- evidence_id: septin-context-pyrenoid
  kind: record_content
  reference: data/structures/other/pyrenoid.yaml
  locator: 'Frozen boundary-only context: identifier,label,definition,parent_structures,part_of,has_part,xrefs'
  summary: Read only after root froze the input. Whole pyrenoid does not impose universal
    tubules; recycling membrane remains a separate structural boundary. No neighbor
    scientific verdict or issue disposition is inferred.
  accessed_at: '2026-11-03T20:48:47.553933Z'
  support: supports
  snapshot_sha256: bdaff3023422d77a8c9a8b8c5d45e254fa3ab2322076eb5aa27cb0e1e954bfc7
- evidence_id: septin-context-recycling_endosome_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/recycling_endosome_membrane.yaml
  locator: 'Frozen boundary-only context: identifier,label,definition,parent_structures,part_of,has_part,xrefs'
  summary: Read only after root froze the input. Whole pyrenoid does not impose universal
    tubules; recycling membrane remains a separate structural boundary. No neighbor
    scientific verdict or issue disposition is inferred.
  accessed_at: '2026-11-03T20:48:47.553933Z'
  support: supports
  snapshot_sha256: cc07cfcf4d3c8fcfac3594e3dec18791b1e5f40e13d867fcdb4ef355f07aebf0
- evidence_id: septin-record-pyrenoid_tubule
  kind: record_content
  reference: data/structures/membrane_organelle/pyrenoid_tubule.yaml
  locator: Complete current record at 55020000323f1344e65128992b35f6ef43c703a2
  summary: All identity, definition, components, taxa/examples, function/source notes,
    history/discussion and graph fields read. Zero individual examples; zero typed
    molecular nodes or protein accessions. No maintained image.
  accessed_at: '2026-11-03T20:48:47.553933Z'
  support: supports
  snapshot_sha256: dd5c61f94612f6c30f259f029b7f4bc4daa8a7d4c0fa8111f6eb0715f78483d7
- evidence_id: septin-original-pyrenoid_tubule
  kind: prior_review
  reference: reviews/structured/20261022T033002Z-pyrenoid-tubule-audit/review.yaml
  locator: Complete immutable original YAML/Markdown pair and frozen-source metadata
  summary: Original exact target bytes match current. Native schema/render and every
    historical input hash checked. Original has no scientific finding; qualified verdict
    is independently reassessed. Historical source access remains historical.
  accessed_at: '2026-11-03T20:48:47.553933Z'
  support: supports
  snapshot_sha256: 86891d8ba547b18479a840aedaf205aa3a18d4fbe16071a18a1a620a2afbe8c8
- evidence_id: septin-original-validation-pyrenoid_tubule
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/adversary-septin/original-checks.json
  locator: Actual original native validation/render, exact Markdown and every historical
    frozen-input hash
  summary: Validation and render exit0; exact original Markdown; all historical source
    inputs match their recorded hashes. Current target is unchanged. Schema validity
    is separate from scientific support.
  accessed_at: '2026-11-03T20:42:59.761704Z'
  support: supports
  snapshot_sha256: 585963e8342d0bc305d784f0677f6471c04e76949ccb5f1b30200be0facc0b00
- evidence_id: septin-native-pyrenoid_tubule-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/pyrenoid_tubule-uniprot-verify-receipt.json
  locator: Actual command receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/pyrenoid_tubule-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: Exit0. Independently counted0 individual protein examples; zero GENE_OR_PROTEIN
    nodes and zero UniProtKB graph xrefs. This is empty represented protein scope,
    not complete molecular coverage or biological absence.
  accessed_at: '2026-11-03T20:42:59.023278Z'
  support: supports
  snapshot_sha256: b56ca3bb0f44ad83aa051a626092ca8dfaf1d7a4160e01c517fbafd2add1222c
- evidence_id: septin-native-pyrenoid_tubule-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/pyrenoid_tubule-uniprot-causal-receipt.json
  locator: Actual command receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/pyrenoid_tubule-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: Exit0. Independently counted0 individual protein examples; zero GENE_OR_PROTEIN
    nodes and zero UniProtKB graph xrefs. This is empty represented protein scope,
    not complete molecular coverage or biological absence.
  accessed_at: '2026-11-03T20:42:59.440482Z'
  support: supports
  snapshot_sha256: 15d7ce3aecf2c867def07c321638f8d22d5eb0b6651610a0bc9feb90ffff58c1
- evidence_id: septin-record-recycling_endosome
  kind: record_content
  reference: data/structures/membrane_organelle/recycling_endosome.yaml
  locator: Complete current record at 55020000323f1344e65128992b35f6ef43c703a2
  summary: All identity, definition, components, taxa/examples, function/source notes,
    history/discussion and graph fields read. Zero individual examples; one typed
    external TbRAB11 node with Q9NJE8 xref. No maintained image.
  accessed_at: '2026-11-03T20:48:47.553933Z'
  support: supports
  snapshot_sha256: 7a806e4e4eaddd3578c517d587c4eaaf1c458e4f5cfc2e59065fc0f26594ac48
- evidence_id: septin-original-recycling_endosome
  kind: prior_review
  reference: reviews/structured/20261022T033003Z-recycling-endosome-audit/review.yaml
  locator: Complete immutable original YAML/Markdown pair and frozen-source metadata
  summary: Original exact target bytes match current. Native schema/render and every
    historical input hash checked. Inherited F1/key/action preserved with exact repository/review/finding
    predecessor. Historical source access remains historical.
  accessed_at: '2026-11-03T20:48:47.553933Z'
  support: supports
  snapshot_sha256: 1f3826bc69bd0d47bd2ca0874f51a368f1db4841a507cf92e55a4a61557bd527
- evidence_id: septin-original-validation-recycling_endosome
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/adversary-septin/original-checks.json
  locator: Actual original native validation/render, exact Markdown and every historical
    frozen-input hash
  summary: Validation and render exit0; exact original Markdown; all historical source
    inputs match their recorded hashes. Current target is unchanged. Schema validity
    is separate from scientific support.
  accessed_at: '2026-11-03T20:43:01.037150Z'
  support: supports
  snapshot_sha256: 585963e8342d0bc305d784f0677f6471c04e76949ccb5f1b30200be0facc0b00
- evidence_id: septin-native-recycling_endosome-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/recycling_endosome-uniprot-verify-receipt.json
  locator: Actual command receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/recycling_endosome-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: Exit0. Independently counted0 individual protein examples; one GENE_OR_PROTEIN
    external TbRAB11 node is UNANCHORED_WITH_UNIPROT Q9NJE8, not COVERED. No component_ref
    is intentionally asserted; native identity/coverage does not establish experimental
    strain sequence equivalence, complete biology or necessary structural membership.
  accessed_at: '2026-11-03T20:43:00.740924Z'
  support: supports
  snapshot_sha256: ec654cde3004b1dd76efcb24a36c8067f3118dcc404d0fc1c1d77f555cfebe9b
- evidence_id: septin-native-recycling_endosome-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/recycling_endosome-uniprot-causal-receipt.json
  locator: Actual command receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/recycling_endosome-uniprot-causal.log
    SHA256 8ec13ce57264c182b589096a0cec398aeb141a38ec3be5d93c48ecc41174dcbe
  summary: Exit0. Independently counted0 individual protein examples; one GENE_OR_PROTEIN
    external TbRAB11 node is UNANCHORED_WITH_UNIPROT Q9NJE8, not COVERED. No component_ref
    is intentionally asserted; native identity/coverage does not establish experimental
    strain sequence equivalence, complete biology or necessary structural membership.
  accessed_at: '2026-11-03T20:43:01.174351Z'
  support: supports
  snapshot_sha256: 8eb3046f25968e8dff3def2fba4bbf93722f3ca9d8b3f76554ddd9a0c06f099b
- evidence_id: septin-record-recycling_endosome_lumen
  kind: record_content
  reference: data/structures/membrane_organelle/recycling_endosome_lumen.yaml
  locator: Complete current record at 55020000323f1344e65128992b35f6ef43c703a2
  summary: All identity, definition, components, taxa/examples, function/source notes,
    history/discussion and graph fields read. Zero individual examples; zero typed
    molecular nodes or protein accessions. No maintained image.
  accessed_at: '2026-11-03T20:48:47.553933Z'
  support: supports
  snapshot_sha256: 69bc318299125a4de316f2ba3b7fc20e0655bca2d37fa6d43c12afcfa3fc3ce2
- evidence_id: septin-original-recycling_endosome_lumen
  kind: prior_review
  reference: reviews/structured/20261022T033003Z-recycling-endosome-lumen-audit/review.yaml
  locator: Complete immutable original YAML/Markdown pair and frozen-source metadata
  summary: Original exact target bytes match current. Native schema/render and every
    historical input hash checked. Original has no scientific finding; qualified verdict
    is independently reassessed. Historical source access remains historical.
  accessed_at: '2026-11-03T20:48:47.553933Z'
  support: supports
  snapshot_sha256: 38cca0f4d52b044e8623cefb7a2d944e4ba7c5231523caba2cb616112c98ac7e
- evidence_id: septin-original-validation-recycling_endosome_lumen
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/adversary-septin/original-checks.json
  locator: Actual original native validation/render, exact Markdown and every historical
    frozen-input hash
  summary: Validation and render exit0; exact original Markdown; all historical source
    inputs match their recorded hashes. Current target is unchanged. Schema validity
    is separate from scientific support.
  accessed_at: '2026-11-03T20:43:02.343242Z'
  support: supports
  snapshot_sha256: 585963e8342d0bc305d784f0677f6471c04e76949ccb5f1b30200be0facc0b00
- evidence_id: septin-native-recycling_endosome_lumen-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/recycling_endosome_lumen-uniprot-verify-receipt.json
  locator: Actual command receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/recycling_endosome_lumen-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: Exit0. Independently counted0 individual protein examples; zero GENE_OR_PROTEIN
    nodes and zero UniProtKB graph xrefs. This is empty represented protein scope,
    not complete molecular coverage or biological absence.
  accessed_at: '2026-11-03T20:43:01.616988Z'
  support: supports
  snapshot_sha256: eec135089b64e2ef8b1a5fe8426848c9eb6624125b4cfe4587c6ddbe2e6533df
- evidence_id: septin-native-recycling_endosome_lumen-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/recycling_endosome_lumen-uniprot-causal-receipt.json
  locator: Actual command receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/recycling_endosome_lumen-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: Exit0. Independently counted0 individual protein examples; zero GENE_OR_PROTEIN
    nodes and zero UniProtKB graph xrefs. This is empty represented protein scope,
    not complete molecular coverage or biological absence.
  accessed_at: '2026-11-03T20:43:02.031057Z'
  support: supports
  snapshot_sha256: dd997e6987f284799ad245cf7dec528f8df9d0a71ad1ce04859ddb3fc1fc2a77
- evidence_id: plaque-current-5
  kind: record_content
  reference: data/structures/membrane_organelle/polaroplast.yaml
  locator: Entire current maintained record at 55020000323f1344e65128992b35f6ef43c703a2;
    all components, evidence, functions, graphs, discussions, image metadata and history
  summary: Polaroplast is stale solely through two new subregion nodes, their anatomical
    part_of edges and matching history; pusule target bytes are unchanged.
  accessed_at: '2026-11-03T20:47:42.896542Z'
  support: supports
  snapshot_sha256: 33a7618c43eea5924263584a6faa84d6190ff1198bfdb1ca2903d49e726c2642
- evidence_id: plaque-original-5
  kind: prior_review
  reference: reviews/structured/20261022T033000Z-polaroplast-audit/review.yaml
  locator: Exact staleness-selected immutable YAML and native Markdown; source/evidence/assessments/checks/findings/actions/limits
  summary: Original qualified pass has no scientific finding or request_curation action.
    Historical frozen inputs validate at original source; current reassessment is
    separate.
  accessed_at: '2026-11-03T20:47:42.896542Z'
  support: supports
  snapshot_sha256: 3ff3de0a207854971fcba962de9441e88400479b79261a7ac3f156e046410bde
- evidence_id: plaque-current-6
  kind: record_content
  reference: data/structures/membrane_organelle/pusule.yaml
  locator: Entire current maintained record at 55020000323f1344e65128992b35f6ef43c703a2;
    all components, evidence, functions, graphs, discussions, image metadata and history
  summary: Polaroplast is stale solely through two new subregion nodes, their anatomical
    part_of edges and matching history; pusule target bytes are unchanged.
  accessed_at: '2026-11-03T20:47:42.896542Z'
  support: supports
  snapshot_sha256: 3bc5082b5e3b721414b9b2d57c585c1a278de5053885f34f55b40ccd4b71a6ae
- evidence_id: plaque-original-6
  kind: prior_review
  reference: reviews/structured/20261022T033001Z-pusule-audit/review.yaml
  locator: Exact staleness-selected immutable YAML and native Markdown; source/evidence/assessments/checks/findings/actions/limits
  summary: Original qualified pass has no scientific finding or request_curation action.
    Historical frozen inputs validate at original source; current reassessment is
    separate.
  accessed_at: '2026-11-03T20:47:42.896542Z'
  support: supports
  snapshot_sha256: cabed5cf67f77e9ba0fbc42c52a5ca58f228bca641100969fdca23acdb7eb1aa
- evidence_id: plaque-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Current skill Structured Source Cross-Checks/evidence rules reread; exact
    bytes unchanged from previous full read
  summary: Applicability follows positive gene/protein/pathway/stress/trait assertions.
    Physical membrane morphology or unresolved molecular machinery is not automatically
    a molecular-pathway assertion.
  accessed_at: '2026-11-03T20:47:42.896542Z'
  support: context_only
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: plaque-rubric
  kind: authority
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Previously read exact frozen checklist, unchanged
  summary: Identity, anatomical composition, function, mechanism and necessity assessed
    separately; optional unassigned proteins/lipids alone are not findings.
  accessed_at: '2026-11-03T20:47:42.896542Z'
  support: context_only
  snapshot_sha256: e6b9e4b16a58c54402bed7bbee2c8b94a91d37562e8b0ee8b94ff0c829184a70
- evidence_id: plaque-schema-policy
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Exact frozen component/causal schema previously read, unchanged
  summary: Label-only membrane materials differ from falsely grounding a chemical
    species to a whole membrane. STRUCTURE subregions and nonmechanistic FUNCTION
    graphs are permitted.
  accessed_at: '2026-11-03T20:47:42.896542Z'
  support: context_only
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: plaque-history-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Previously read exact discussion/history policy, unchanged
  summary: Historical rationale/events remain append-only. Current review does not
    close neighboring records or their issues.
  accessed_at: '2026-11-03T20:47:42.896542Z'
  support: context_only
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
- evidence_id: plaque-context-contractile_vacuole
  kind: record_content
  reference: data/structures/membrane_organelle/contractile_vacuole.yaml
  locator: Identity/definition/component boundary and declared parthood only, read
    after exact source freeze; not a complete neighbor scientific audit
  summary: Distinct bounded vacuole versus nuclear-envelope network context; spatial
    adjacency does not assign ribbons, rootlets or nuclear membranes as pusule constituents.
    No neighbor finding disposition.
  accessed_at: '2026-11-03T20:47:42.896542Z'
  support: context_only
  snapshot_sha256: d1057e9c19ff100f054c73da52b597742dadde491f2a007cd7b648b8a7b626bb
- evidence_id: plaque-context-nuclear_net
  kind: record_content
  reference: data/structures/membrane_organelle/nuclear_net.yaml
  locator: Identity/definition/component boundary and declared parthood only, read
    after exact source freeze; not a complete neighbor scientific audit
  summary: Distinct bounded vacuole versus nuclear-envelope network context; spatial
    adjacency does not assign ribbons, rootlets or nuclear membranes as pusule constituents.
    No neighbor finding disposition.
  accessed_at: '2026-11-03T20:47:42.896542Z'
  support: context_only
  snapshot_sha256: 8b4a54d13a70cfb4fdce9bd18ae990793f9de9627fdca067573c033335d847ba
- evidence_id: plaque-go-polar
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0160201,GO:0044099
  locator: Fresh complete GO0160201 and0044099 id/name/definition/isObsolete response
  summary: Exact polaroplast and distinct polar-tube identities. Water-swelling/pressure
    wording is issuing-authority definition, not a new experimentally proven force
    calculation.
  accessed_at: '2026-11-03T20:44:20.705669Z'
  support: supports
  snapshot_sha256: 33880b6c13718a1e49c55ee674c90904b1ae7e406c9bdbc993da61f23951e8e0
- evidence_id: plaque-go-pusule
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0043227,GO:0016020
  locator: Fresh complete GO0043227 and0016020 id/name/definition/isObsolete/typed
    children
  summary: Whole membrane-bounded-organelle parent and whole-membrane material match
    the maintained OTHER membrane component. Surface-canal continuity is not denied
    by the parent; no exact GO pusule identity is fabricated.
  accessed_at: '2026-11-03T20:44:20.706602Z'
  support: supports
  snapshot_sha256: 1f9655bc19a55016646e5d2d9ac00ae67695c7d120efca5b4905fa33af04f763
- evidence_id: plaque-go-pusule-search
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=pusule&limit=100
  locator: Complete returned first page, zero results
  summary: No exact pusule result in this bounded name query; not exhaustive ontology
    nonexistence proof.
  accessed_at: '2026-11-03T20:44:20.707665Z'
  support: supports
  search_scope: QuickGO ontology/go/search query=pusule,limit=100 at 2026-11-03T20:44:20.707665Z;
    first returned page, numberOfHits0; no synonyms or all-ontology exhaustive absence
    claim.
  snapshot_sha256: f3a7dae9b1e9335291e3940cdf0e5f8dadf9335da7b9547710606b5106c63f86
- evidence_id: plaque-tax-6029
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/6029
  locator: Fresh complete ENA taxId/scientificName/rank/lineage and alternate names
  summary: Exact Microsporidia, Nosema bombycis, Polykrikos kofoidii, Prorocentrum
    micans or Amphidinium carterae identity verified. Taxonomy does not certify occurrence
    frequency or experimental strain.
  accessed_at: '2026-11-03T20:44:21.405270Z'
  support: supports
  snapshot_sha256: 5a4e56118a35563f14efbf594aef989903527ec8c8aea7e85d5a2ff21ea44243
- evidence_id: plaque-tax-27978
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/27978
  locator: Fresh complete ENA taxId/scientificName/rank/lineage and alternate names
  summary: Exact Microsporidia, Nosema bombycis, Polykrikos kofoidii, Prorocentrum
    micans or Amphidinium carterae identity verified. Taxonomy does not certify occurrence
    frequency or experimental strain.
  accessed_at: '2026-11-03T20:44:21.527980Z'
  support: supports
  snapshot_sha256: bd776284e072d75d566a4f14a4e4007db6c95e30f0b23fddef3d95e1763b3016
- evidence_id: plaque-tax-271679
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/271679
  locator: Fresh complete ENA taxId/scientificName/rank/lineage and alternate names
  summary: Exact Microsporidia, Nosema bombycis, Polykrikos kofoidii, Prorocentrum
    micans or Amphidinium carterae identity verified. Taxonomy does not certify occurrence
    frequency or experimental strain.
  accessed_at: '2026-11-03T20:44:21.586844Z'
  support: supports
  snapshot_sha256: 69cb7b45b417f8736d4242226f0b0b8b82fe08c8e4a9e82c667d7a8fa0b26f98
- evidence_id: plaque-tax-2945
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2945
  locator: Fresh complete ENA taxId/scientificName/rank/lineage and alternate names
  summary: Exact Microsporidia, Nosema bombycis, Polykrikos kofoidii, Prorocentrum
    micans or Amphidinium carterae identity verified. Taxonomy does not certify occurrence
    frequency or experimental strain.
  accessed_at: '2026-11-03T20:44:21.642916Z'
  support: supports
  snapshot_sha256: e0ac334f3b9b3bb07fa0e608b45d7fe6fa21c04fe5d188c012df3a0318fabe02
- evidence_id: plaque-tax-2961
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2961
  locator: Fresh complete ENA taxId/scientificName/rank/lineage and alternate names
  summary: Exact Microsporidia, Nosema bombycis, Polykrikos kofoidii, Prorocentrum
    micans or Amphidinium carterae identity verified. Taxonomy does not certify occurrence
    frequency or experimental strain.
  accessed_at: '2026-11-03T20:44:21.849751Z'
  support: supports
  snapshot_sha256: 0611f7d2024997ec72dd1ddacc0a14a79f14223c2800d75040f841378a22254d
- evidence_id: plaque-han-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1007%2F978-3-030-93306-7_8&format=json&resultType=core&pageSize=10
  locator: Fresh exact DOI bibliographic identity, title/authors/year/PMID/PMCID
  summary: Cited attribution and year agree. Han chapter and Chen article provide
    secondary review context despite Han metadata research-article tag; Lv and Gavelis
    are primary experiments.
  accessed_at: '2026-11-03T20:44:20.707815Z'
  support: supports
  search_scope: EuropePMC exact DOI query encoded in URL at 2026-11-03T20:44:20.707815Z;
    pageSize10, first returned page, 1 total hits; all returned bibliographic metadata
    inspected. Metadata does not certify full-body claims.
  snapshot_sha256: ece00d0653e1ae5478bcdb794c3298739432e8eba03c1966603a46a4e31a625b
- evidence_id: plaque-chen-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1186%2Fs13071-023-05908-9&format=json&resultType=core&pageSize=10
  locator: Fresh exact DOI bibliographic identity, title/authors/year/PMID/PMCID
  summary: Cited attribution and year agree. Han chapter and Chen article provide
    secondary review context despite Han metadata research-article tag; Lv and Gavelis
    are primary experiments.
  accessed_at: '2026-11-03T20:44:20.707894Z'
  support: supports
  search_scope: EuropePMC exact DOI query encoded in URL at 2026-11-03T20:44:20.707894Z;
    pageSize10, first returned page, 1 total hits; all returned bibliographic metadata
    inspected. Metadata does not certify full-body claims.
  snapshot_sha256: a8c1147f31c8c4591ac848ce52618bf04b481cec5f29289e9348e0049abdc313
- evidence_id: plaque-lv-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1128%2Fmbio.02749-23&format=json&resultType=core&pageSize=10
  locator: Fresh exact DOI bibliographic identity, title/authors/year/PMID/PMCID
  summary: Cited attribution and year agree. Han chapter and Chen article provide
    secondary review context despite Han metadata research-article tag; Lv and Gavelis
    are primary experiments.
  accessed_at: '2026-11-03T20:44:20.709279Z'
  support: supports
  search_scope: EuropePMC exact DOI query encoded in URL at 2026-11-03T20:44:20.709279Z;
    pageSize10, first returned page, 1 total hits; all returned bibliographic metadata
    inspected. Metadata does not certify full-body claims.
  snapshot_sha256: 7213b20e4455c152bf6918ebc7672c0456960983470389373ff6da3759097f09
- evidence_id: plaque-gavelis-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1038%2Fs41598-018-37065-w&format=json&resultType=core&pageSize=10
  locator: Fresh exact DOI bibliographic identity, title/authors/year/PMID/PMCID
  summary: Cited attribution and year agree. Han chapter and Chen article provide
    secondary review context despite Han metadata research-article tag; Lv and Gavelis
    are primary experiments.
  accessed_at: '2026-11-03T20:44:21.318160Z'
  support: supports
  search_scope: EuropePMC exact DOI query encoded in URL at 2026-11-03T20:44:21.318160Z;
    pageSize10, first returned page, 1 total hits; all returned bibliographic metadata
    inspected. Metadata does not certify full-body claims.
  snapshot_sha256: abe21fd631324427cf3fdaa1d64ea21153731f849322c523828e5aae2a715a87
- evidence_id: plaque-han-body
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC10037675/
  locator: 'Genuine SECONDARY chapter HTML: Introduction and Section8.2 selected membrane-array/germination
    paragraphs, Fig8.1/8.2/8.4/8.5/8.6 captions; no image pixels or complete later
    sections'
  summary: Lamellar/flattened-tubular membrane clusters and posterior polaroplast
    are described in the spore invasion apparatus. Anatomical subregions belong to
    the membrane system; conserved presence is qualitative and not a measured prevalence
    denominator.
  accessed_at: '2026-11-03T20:44:20.710233Z'
  support: supports
  snapshot_sha256: 2c5a2b94743f630553a422d8305df8814a408067b0152cc2afc2b169da0d826c
- evidence_id: plaque-chen-jats
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC10468886.1/PMC10468886.1.xml
  locator: 'Genuine SECONDARY review JATS: life-cycle germination paragraph, structural
    polar-filament paragraph and concluding model/unknowns; no pixels or entire-paper
    certification'
  summary: Osmotic swelling/discharge is explicitly presented as a widely accepted
    hypothesis; polaroplast surrounds straight polar-filament region. This is context
    for physical firing support, not identified force-generation machinery or genetic
    necessity.
  accessed_at: '2026-11-03T20:44:20.711803Z'
  support: supports
  snapshot_sha256: 5083a1d25970fc2b58e0d48e5c0b747caed5ea502f66e09c6d2217d449431e62
- evidence_id: plaque-lv-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC10865828.1/PMC10865828.1.xml
  locator: 'Genuine primary JATS: Introduction; Results membrane cargo/transport,
    sporoplasm formation and localization-marker sections with Fig2–8 captions; Discussion;
    Methods cell culture/spore preparation/fluorescence/immunofluorescence/TEM/cryo-EM/lipidomics/controls/statistics.
    No figure pixels, supplements or rawdata independently inspected'
  summary: Nosema bombycis isolate CQ1 propagated in silkworms; 0.1M KOH induction
    and fixed-stage DiI/DAPI, TEM/cryo-EM, protein-marker distributions and lipidomics
    support transported membrane contribution to nascent sporoplasm. These are not
    continuous single-membrane lineage tracing, universal kinetics, exclusive origin
    or identified necessary transport proteins. New subregion edges are anatomical,
    not a mechanism inferred from antibody localization.
  accessed_at: '2026-11-03T20:44:21.136732Z'
  support: supports
  snapshot_sha256: f1fd889f46a4988af03eeede4a5703c39ab8f9c2f2b5fbe30d03f44b87b96082
- evidence_id: plaque-dodge-meta
  kind: database
  reference: https://api.crossref.org/works/10.1007/BF01279820
  locator: Fresh Crossref DOI/title/author/publication identity, no deposited full
    text
  summary: Dodge1972 primary paper identity verified; readable publisher summary bound
    separately.
  accessed_at: '2026-11-03T20:44:21.184264Z'
  support: supports
  snapshot_sha256: 4f2645030cd70f46520080402c6b262016488091ead5bb2a6894a86021c38b23
- evidence_id: plaque-dodge-publisher
  kind: primary_source
  reference: https://link.springer.com/article/10.1007/BF01279820
  locator: Fresh genuine Springer publisher Summary only; page explicitly labels subscription
    preview. No complete Methods/Results or PDF
  summary: Survey summary describes seven pusular forms grouped by vesicle/tubule/sac
    topology and apposed invaginated plasma/vacuolar membranes with flagellar-canal
    connection. Excretion/osmoregulation is a proposed interpretation, not a measured
    molecular mechanism.
  accessed_at: '2026-11-03T20:44:21.313728Z'
  support: supports
  snapshot_sha256: 7cfdecce27fab7cf135dc937eeea3ac5a82091f0754848f63c30a001da0018c2
- evidence_id: plaque-klut-meta
  kind: primary_source
  reference: https://api.crossref.org/works/10.1139/b87-098
  locator: Fresh Crossref publisher-deposited PRIMARY abstract plus bibliographic
    identity; no full paper/figures/experimental-control audit
  summary: Prorocentrum micans and Amphidinium carterae; salinity/temperature size
    changes and HRP/ferritin/lectin entry through flagellar canal. Fibrillar-collar
    flow, osmoregulation and secretion are suggestions. Entry into lumen is not demonstrated
    cytoplasmic delivery, nutrient assimilation or transmembrane transport.
  accessed_at: '2026-11-03T20:44:21.314813Z'
  support: supports
  snapshot_sha256: d50606fb8d46c495b15621bbb3afc00a31f54b8572f6001efc22f0be63b0bf64
- evidence_id: plaque-gavelis-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC6351617.1/PMC6351617.1.xml
  locator: Fresh genuine JATS ResultsSec2/Par6 and neighboring nuclear-net distinction;
    MethodsCollection/TEM/FIB-SEM; Fig2 caption/graphic; author list and permissions.
    No whole-paper or other-figure pixel audit
  summary: Wild-collected Polykrikos kofoidii pseudocolonies from Vancouver2015/FridayHarbor2016;
    four TEM specimens and one retained FIB-SEM specimen. Fig2D is transverse/longitudinal
    TEM duct/diverticula, E interior FIB-SEM reconstruction, G/H contextual orange
    pusule and blue nucleus. FIB-SEM uses high-pressure freezing/freeze substitution.
    Eight authors and CC BY4.0 match attribution; no contrary figure-specific credit
    restriction.
  accessed_at: '2026-11-03T20:44:21.354541Z'
  support: supports
  snapshot_sha256: e9da1c1df53b0558143b645859b9cf77aa266778027d41a42b10d78502bad9f4
- evidence_id: plaque-gavelis-fig2
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC6351617.1/41598_2018_37065_Fig2_HTML.jpg
  locator: Fresh exact PMC6351617.1 Fig2 JPEG compared bytewise with frozen maintained
    image; visual inspection of maintained identical pixels at2026-11-03T20:45:23Z
  summary: All panels actually viewed. D shows duct/diverticula cross/longitudinal
    sections, E internal reconstructed pockets; orange G/H pusule is separate from
    blue nuclear and colored ribbon/rootlet structures. Caption supports D2micrometer
    andG/H5micrometer bars. No new morphometric measurement. Maintained/download bytes
    identical SHA6c37909f2a8a422f0625da79598171847c57a39ec9aad4587239482b31eaeb6a,
    MD5df1b5c4b4cb5d738f4042d41ce50521e.
  accessed_at: '2026-11-03T20:44:21.362272Z'
  support: supports
  snapshot_sha256: 6c37909f2a8a422f0625da79598171847c57a39ec9aad4587239482b31eaeb6a
- evidence_id: plaque-local-pusule-image
  kind: record_content
  reference: data/images/membrane_organelle/pusule/pmc6351617_fig2.jpg
  locator: Frozen maintained image actually visually inspected at2026-11-03T20:45:23Z
    and matched to fresh source download
  summary: Panel context, mixed modality and attribution remain source-bounded; nuclear
    panels do not become pusule components.
  accessed_at: '2026-11-03T20:45:23Z'
  support: supports
  snapshot_sha256: 6c37909f2a8a422f0625da79598171847c57a39ec9aad4587239482b31eaeb6a
- evidence_id: plaque-catalogue
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Same-PR complete official JSON catalogue independently reread; actual first-fetch
    timestamp/hash retained, not a new request
  summary: All20 organism rows/28 organism-dataset pairs are bacteria/archaea. No
    Microsporidia/Nosema or named dinoflagellate host. No matched gene/module query
    or foreign host proxy used; no biological absence inferred.
  accessed_at: '2026-11-03T20:43:49.951558Z'
  support: supports
  search_scope: Official /api/datasets complete response at 2026-11-03T20:43:49.951558Z;
    all20 rows/28pairs inspected against Microsporidia,Nosema,Polykrikos,Prorocentrum,Amphidinium
    exact/historical names; scope only this returned catalogue.
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: plaque-historical-runner
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Retained historical00:49Z runner failure with verified stdout/stderr hashes
  summary: PermissionError accessing pyvenv.cfg; no fresh invocation or runner success.
    Current official-source catalogue fallback is separately identified.
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: plaque-original-checks
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/adversary-plaque/original-checks.json
  locator: 'Actual original native validate/render and historical input hashes: polaroplast12,pusule15'
  summary: Both originals validate and render byte-identical Markdown; all27 historical
    input rows match their originalsource. Polaroplast current hash differs and is
    substantively refreshed; pusule current target remains identical.
  accessed_at: '2026-11-03T20:44:11.567910Z'
  support: supports
  snapshot_sha256: ee39d0076effc70629db096850c112b1bce7dea170600ba9a9315183b813c0b0
- evidence_id: plaque-polaroplast-delta
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/adversary-plaque/5-stale.diff
  locator: Git diff original frozen revision to current source, exact assigned polaroplast
    path
  summary: Only two anatomical STRUCTURE nodes/component_refs, two part_of edges and
    matching history were added. Existing component claims, functions and membrane-contribution
    edges are reassessed, not silently approved by hash replacement.
  accessed_at: '2026-11-03T20:47:42.896542Z'
  support: supports
  snapshot_sha256: fca11734bbc06173accfde8c5a4e7f496819184721636f1dc57d8a5e2cccfa59
- evidence_id: plaque-native-polaroplast-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/polaroplast.yaml
    --verify
  locator: Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/polaroplast-uniprot-verify-receipt.json;
    logSHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: Direct current YAML inspection finds0 protein_examples and0 GENE_OR_PROTEIN
    nodes. Native command exits0 over an empty represented protein inventory; it does
    not verify absent proteins, organelle formation or physical mechanism.
  accessed_at: '2026-11-03T20:42:57.359602Z'
  support: supports
  snapshot_sha256: bbf791dbcd3fddd3aafaa9a229f1223ea342c949d322c0b52e07a699d19d3388
- evidence_id: plaque-native-polaroplast-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/polaroplast.yaml
    --causal-graphs
  locator: Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/polaroplast-uniprot-causal-receipt.json;
    logSHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: Direct current YAML inspection finds0 protein_examples and0 GENE_OR_PROTEIN
    nodes. Native command exits0 over an empty represented protein inventory; it does
    not verify absent proteins, organelle formation or physical mechanism.
  accessed_at: '2026-11-03T20:42:57.765821Z'
  support: supports
  snapshot_sha256: 7bbb386fbe905d6bd93f5ec31f87647d0b1de6d321fa5ef9af6c56c600f1071c
- evidence_id: plaque-native-pusule-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/pusule.yaml
    --verify
  locator: Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/pusule-uniprot-verify-receipt.json;
    logSHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: Direct current YAML inspection finds0 protein_examples and0 GENE_OR_PROTEIN
    nodes. Native command exits0 over an empty represented protein inventory; it does
    not verify absent proteins, organelle formation or physical mechanism.
  accessed_at: '2026-11-03T20:42:58.197647Z'
  support: supports
  snapshot_sha256: 5a17166da819df485277b0cb2f0dc5c6176fff99f28aa73eda78c82d1271e01c
- evidence_id: plaque-native-pusule-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/pusule.yaml
    --causal-graphs
  locator: Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/pusule-uniprot-causal-receipt.json;
    logSHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: Direct current YAML inspection finds0 protein_examples and0 GENE_OR_PROTEIN
    nodes. Native command exits0 over an empty represented protein inventory; it does
    not verify absent proteins, organelle formation or physical mechanism.
  accessed_at: '2026-11-03T20:42:58.612492Z'
  support: supports
  snapshot_sha256: 4b822cc084f72bcc6255e0f362d960513a271cc9b20669f993a32f574c480a68
- evidence_id: micro-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Current native skill/profile/config/checklist, structured-source applicability
    and optional-slot contract
  accessed_at: '2026-11-03T20:47:44.492903Z'
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
  summary: Positive molecular/pathway claims anywhere in a record trigger source applicability.
    Explicitly withheld molecular scope and physical-only topology remain valid exclusions;
    source background does not create new record assertions.
  support: context_only
- evidence_id: micro-component-policy
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent/ComponentTypeEnum/EssentialityEnum and CURATION components
  accessed_at: '2026-11-03T20:47:44.492903Z'
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
  summary: An anatomical membrane GO class is not a chemical LIPID identity; OTHER
    structural constituent or label-only collective material remains permissible.
    Optional molecular inventory and individual formation necessity are not inferred
    from topology.
  support: context_only
- evidence_id: micro-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Graph scope, source-specific edges, component join and allowed generic
    class semantics
  accessed_at: '2026-11-03T20:47:44.492903Z'
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
  summary: NONMECHANISTIC descriptive anatomy and supported light-reaction site do
    not assert a complete assembly pathway or universal protein cohort.
  support: context_only
- evidence_id: micro-discussion-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Discussion305–324; components and evidence placement
  accessed_at: '2026-11-03T20:47:44.492903Z'
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
  summary: Historical rationale remains append-only; optional chemical grounding and
    narrow compartment-boundary interpretations do not become defects merely because
    additional biology is known.
  support: context_only
- evidence_id: micro-record-plastid_outer_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/plastid_outer_membrane.yaml
  locator: 'Entire current record: identity/definition, all source notes/taxa/examples,
    components/functions, every graph node/edge, status/history/discussions'
  accessed_at: '2026-11-03T20:47:44.492903Z'
  snapshot_sha256: 59bd8548931d27f711233f542b5f927c0e7b0a68dd611eabb4777ee08003deaa
  summary: Complete unchanged target independently read. Original frozen target/current
    main hashes agree; no maintained record mutation.
  support: supports
- evidence_id: micro-prior-plastid_outer_membrane
  kind: prior_review
  reference: reviews/structured/20261022T032956Z-plastid-outer-membrane-audit/review.yaml
  locator: Authoritative original YAML all scientific claims/evidence/scopes/checks/assessments/findings/actions/limits
    and exact derived Markdown
  accessed_at: '2026-11-03T20:47:44.492903Z'
  snapshot_sha256: 13834625be15bdee042f39f764b0f9557c5ea353bf9a718a3ee83cd8977afb99
  summary: Original pass_with_limitations; no scientific findings/actions. Explicit
    expression-only N/A check. Original observation/check times remain historical.
  support: context_only
- evidence_id: micro-native-plastid_outer_membrane-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_outer_membrane-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_outer_membrane.yaml
    --verify; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_outer_membrane-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T20:42:53.275440Z'
  snapshot_sha256: c348215abfd5fb1fa3ce7f168ecb670c0f2a23a988b4872a2af27faf7d3e3293
  summary: Actual exit0; complete target independently has zero protein_examples and
    zero GENE_OR_PROTEIN nodes. Generic verify-success does not certify exhaustive
    families/proteome, positive narrative machinery, or individual assembly necessity.
  support: supports
- evidence_id: micro-native-plastid_outer_membrane-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_outer_membrane-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_outer_membrane.yaml
    --causal-graphs; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_outer_membrane-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-03T20:42:53.690382Z'
  snapshot_sha256: 58ed19586858a947781445e57fe0c92e495a0a457eebaf312c5fdfd1f29dd5ef
  summary: Actual exit0; complete target independently has zero protein_examples and
    zero GENE_OR_PROTEIN nodes. Generic verify-success does not certify exhaustive
    families/proteome, positive narrative machinery, or individual assembly necessity.
  support: supports
- evidence_id: micro-record-plastid_stroma
  kind: record_content
  reference: data/structures/membrane_organelle/plastid_stroma.yaml
  locator: 'Entire current record: identity/definition, all source notes/taxa/examples,
    components/functions, every graph node/edge, status/history/discussions'
  accessed_at: '2026-11-03T20:47:44.492903Z'
  snapshot_sha256: 86d19307cbe21273498f0d7d6741e61f5ebf002cf78418c34b922d9d4963503b
  summary: Complete unchanged target independently read. Original frozen target/current
    main hashes agree; no maintained record mutation.
  support: supports
- evidence_id: micro-prior-plastid_stroma
  kind: prior_review
  reference: reviews/structured/20261022T032957Z-plastid-stroma-audit/review.yaml
  locator: Authoritative original YAML all scientific claims/evidence/scopes/checks/assessments/findings/actions/limits
    and exact derived Markdown
  accessed_at: '2026-11-03T20:47:44.492903Z'
  snapshot_sha256: c720871647d0ee79fc341ae9122188743b57b0126deba5ced3346f04f37b4e17
  summary: Original pass_with_limitations; no scientific findings/actions. Explicit
    expression-only N/A check. Original observation/check times remain historical.
  support: context_only
- evidence_id: micro-native-plastid_stroma-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_stroma-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_stroma.yaml
    --verify; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_stroma-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T20:42:54.092130Z'
  snapshot_sha256: 13439e819979762df2154d59bece7a1d732391d8eddd6d6cf29f122e9c869534
  summary: Actual exit0; complete target independently has zero protein_examples and
    zero GENE_OR_PROTEIN nodes. Generic verify-success does not certify exhaustive
    families/proteome, positive narrative machinery, or individual assembly necessity.
  support: supports
- evidence_id: micro-native-plastid_stroma-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_stroma-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_stroma.yaml
    --causal-graphs; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_stroma-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-03T20:42:54.492961Z'
  snapshot_sha256: 480b1290d0cc542d80394a094e7c3eb6fe15b3ee5aeab937db8e2cdc77038d03
  summary: Actual exit0; complete target independently has zero protein_examples and
    zero GENE_OR_PROTEIN nodes. Generic verify-success does not certify exhaustive
    families/proteome, positive narrative machinery, or individual assembly necessity.
  support: supports
- evidence_id: micro-record-plastid_thylakoid
  kind: record_content
  reference: data/structures/membrane_organelle/plastid_thylakoid.yaml
  locator: 'Entire current record: identity/definition, all source notes/taxa/examples,
    components/functions, every graph node/edge, status/history/discussions'
  accessed_at: '2026-11-03T20:47:44.492903Z'
  snapshot_sha256: ec3c74ee89bf25eea6a3a5682b3f7f73e0837465dccf2a8f2c0cce1550a4e3c8
  summary: Complete unchanged target independently read. Original frozen target/current
    main hashes agree; no maintained record mutation.
  support: supports
- evidence_id: micro-prior-plastid_thylakoid
  kind: prior_review
  reference: reviews/structured/20261022T032958Z-plastid-thylakoid-audit/review.yaml
  locator: Authoritative original YAML all scientific claims/evidence/scopes/checks/assessments/findings/actions/limits
    and exact derived Markdown
  accessed_at: '2026-11-03T20:47:44.492903Z'
  snapshot_sha256: 52d33d07dcc5220324e238d906c82c4e9c08bd3cf5a2ffc10dc0096fcc847fd5
  summary: Original needs_curation; one inherited majorF1. Prose-only expression-module
    exclusion; Perez secondary excerpts/challenge mislabeled primary_source. Original
    observation/check times remain historical.
  support: context_only
- evidence_id: micro-native-plastid_thylakoid-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_thylakoid-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_thylakoid.yaml
    --verify; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_thylakoid-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T20:42:54.889579Z'
  snapshot_sha256: d01c0856ebdc9570be0503e7d9fcfe7db35a6d82899d5ba8cc4e4b4c38ed5df4
  summary: Actual exit0; complete target independently has zero protein_examples and
    zero GENE_OR_PROTEIN nodes. Generic verify-success does not certify exhaustive
    families/proteome, positive narrative machinery, or individual assembly necessity.
  support: supports
- evidence_id: micro-native-plastid_thylakoid-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_thylakoid-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_thylakoid.yaml
    --causal-graphs; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_thylakoid-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-03T20:42:55.322542Z'
  snapshot_sha256: 8abee869989f99cc3c00e6dce9ac651d31302c8270b72815d02307b7baa698d9
  summary: Actual exit0; complete target independently has zero protein_examples and
    zero GENE_OR_PROTEIN nodes. Generic verify-success does not certify exhaustive
    families/proteome, positive narrative machinery, or individual assembly necessity.
  support: supports
- evidence_id: micro-record-plastid_thylakoid_lumen
  kind: record_content
  reference: data/structures/membrane_organelle/plastid_thylakoid_lumen.yaml
  locator: 'Entire current record: identity/definition, all source notes/taxa/examples,
    components/functions, every graph node/edge, status/history/discussions'
  accessed_at: '2026-11-03T20:47:44.492903Z'
  snapshot_sha256: 7a75c5aee47a20bbae7da6351e07fc7f2d1dc418e7ca34e253d08e3a531ff4ee
  summary: Complete unchanged target independently read. Original frozen target/current
    main hashes agree; no maintained record mutation.
  support: supports
- evidence_id: micro-prior-plastid_thylakoid_lumen
  kind: prior_review
  reference: reviews/structured/20261022T032959Z-plastid-thylakoid-lumen-audit/review.yaml
  locator: Authoritative original YAML all scientific claims/evidence/scopes/checks/assessments/findings/actions/limits
    and exact derived Markdown
  accessed_at: '2026-11-03T20:47:44.492903Z'
  snapshot_sha256: 6c6788f5b5bc7dbbd9d5e4fde20b0191a677dd93ff623ad95060f6a96f83d37b
  summary: Original pass_with_limitations; no scientific findings/actions. Prose-only
    expression-module exclusion; Perez secondary excerpts/challenge mislabeled primary_source.
    Original observation/check times remain historical.
  support: context_only
- evidence_id: micro-native-plastid_thylakoid_lumen-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_thylakoid_lumen-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_thylakoid_lumen.yaml
    --verify; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_thylakoid_lumen-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T20:42:55.734821Z'
  snapshot_sha256: 988c5b74db64437ad910528bb5d9a5b01407d4f56152c1c6265fe6272c9966ed
  summary: Actual exit0; complete target independently has zero protein_examples and
    zero GENE_OR_PROTEIN nodes. Generic verify-success does not certify exhaustive
    families/proteome, positive narrative machinery, or individual assembly necessity.
  support: supports
- evidence_id: micro-native-plastid_thylakoid_lumen-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_thylakoid_lumen-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_thylakoid_lumen.yaml
    --causal-graphs; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_thylakoid_lumen-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-03T20:42:56.143705Z'
  snapshot_sha256: efe0563fa73cce7e739b9f57fd704d30a84c69c99ce9ce399b042ba0b192c4d1
  summary: Actual exit0; complete target independently has zero protein_examples and
    zero GENE_OR_PROTEIN nodes. Generic verify-success does not certify exhaustive
    families/proteome, positive narrative machinery, or individual assembly necessity.
  support: supports
- evidence_id: micro-record-plastid_thylakoid_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/plastid_thylakoid_membrane.yaml
  locator: 'Entire current record: identity/definition, all source notes/taxa/examples,
    components/functions, every graph node/edge, status/history/discussions'
  accessed_at: '2026-11-03T20:47:44.492903Z'
  snapshot_sha256: 51a2ece521e1b5c0b3b589fc7cf665be1c9544299257e0fda7fcf8352e7401c2
  summary: Complete unchanged target independently read. Original frozen target/current
    main hashes agree; no maintained record mutation.
  support: supports
- evidence_id: micro-prior-plastid_thylakoid_membrane
  kind: prior_review
  reference: reviews/structured/20261022T033000Z-plastid-thylakoid-membrane-audit/review.yaml
  locator: Authoritative original YAML all scientific claims/evidence/scopes/checks/assessments/findings/actions/limits
    and exact derived Markdown
  accessed_at: '2026-11-03T20:47:44.492903Z'
  snapshot_sha256: 36adab248fa393a33a16f6d364643e9d1c72ae8d8d8c78959c383c94aa883639
  summary: Original pass_with_limitations; no scientific findings/actions. Prose-only
    expression-module exclusion; Perez secondary excerpts/challenge mislabeled primary_source.
    Original observation/check times remain historical.
  support: context_only
- evidence_id: micro-native-plastid_thylakoid_membrane-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_thylakoid_membrane-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_thylakoid_membrane.yaml
    --verify; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_thylakoid_membrane-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T20:42:56.552435Z'
  snapshot_sha256: f507ddcea0862c6b9870efdb1617041f306d19448827b01175d3ff7ea3ac4c63
  summary: Actual exit0; complete target independently has zero protein_examples and
    zero GENE_OR_PROTEIN nodes. Generic verify-success does not certify exhaustive
    families/proteome, positive narrative machinery, or individual assembly necessity.
  support: supports
- evidence_id: micro-native-plastid_thylakoid_membrane-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_thylakoid_membrane-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_thylakoid_membrane.yaml
    --causal-graphs; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_thylakoid_membrane-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-03T20:42:56.951807Z'
  snapshot_sha256: 47895d863af46ff1edd9a24f2d00853ae6daf2d2d7dc894ac39a00d3df66edf6
  summary: Actual exit0; complete target independently has zero protein_examples and
    zero GENE_OR_PROTEIN nodes. Generic verify-success does not certify exhaustive
    families/proteome, positive narrative machinery, or individual assembly necessity.
  support: supports
- evidence_id: micro-original-pairs
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/adversary-microtubule/original-checks.json
  locator: Five actual native validates and five exact render --content comparisons
  accessed_at: '2026-11-03T20:43:18.828646Z'
  snapshot_sha256: eebf273a47f418185d44a54c71cf6419e966c2e19b85873183d6055db3fdac4e
  summary: All five original authoritative YAMLs validate and derive exact original
    Markdown bytes.
  support: supports
- evidence_id: micro-original-inputs
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/adversary-microtubule/original-frozen-inputs.json
  locator: All76 original frozen input entries at retained original source
  accessed_at: '2026-11-03T20:47:44.492903Z'
  snapshot_sha256: 5d71b912791ab6dbb37d651869fb4cb4f5834555ba74cc28446c4a786f05ea57
  summary: All old hashes match. Own five targets unchanged; checking historical hashes
    does not constitute fresh scientific judgment of neighboring records.
  support: supports
- evidence_id: micro-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005737,GO:0009526,GO:0009527,GO:0009529,GO:0009532,GO:0009535,GO:0009536,GO:0009579,GO:0009843,GO:0019684,GO:0031976,GO:0031977,GO:0031978,GO:0033114,GO:0033115,GO:0042170,GO:0042651,GO:0055035,GO:0070118
  locator: All19 requested native entries id/name/active/definition/synonyms/comments
    and relevant typed children; broad unrelated cytoplasm children not adopted
  accessed_at: '2026-11-03T20:43:18.621567Z'
  snapshot_sha256: 382af7eb475e2bbea69917c424ee1931c201c2718f6eef148e1250630703ebf9
  summary: Exact outer/stroma/thylakoid/lumen/membrane identities, parent classes
    and parthood verified. GO9532 proteinaceous ground substance supports current
    paraphrase; GO9579 comment explicitly distinguishes thylakoid from organelle.
    GO19684 is oxygenic PSI/PSII light reactions. Whole membraneGO55035 remains anatomical.
    GO70118 is under generic thylakoid membrane, not exposed as nativeGO55035 child.
  support: supports
- evidence_id: micro-GO0009527-isa
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009527/ancestors?relations=is_a
  locator: Complete exact-term ancestors response with relations=is_a
  accessed_at: '2026-11-03T20:43:20.298708Z'
  snapshot_sha256: 973849fad45f274e222f032a2d4b55248c515ddaad9e1233a3ef6eb7640b5342
  summary: Exact transitive is_a ancestry read separately from parthood; GO0070118
    lacks GO0055035 in this native ancestor response, while separate UniProt hierarchy
    supports the broader biological classification.
  support: supports
- evidence_id: micro-GO0031976-isa
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031976/ancestors?relations=is_a
  locator: Complete exact-term ancestors response with relations=is_a
  accessed_at: '2026-11-03T20:43:20.476123Z'
  snapshot_sha256: d75c98f4d16e433aad2bfaf74456eb6a8df4be1e0bc7aa24b00b1234d31492ae
  summary: Exact transitive is_a ancestry read separately from parthood; GO0070118
    lacks GO0055035 in this native ancestor response, while separate UniProt hierarchy
    supports the broader biological classification.
  support: supports
- evidence_id: micro-GO0031978-isa
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031978/ancestors?relations=is_a
  locator: Complete exact-term ancestors response with relations=is_a
  accessed_at: '2026-11-03T20:43:20.580674Z'
  snapshot_sha256: 9c57575a4fce40dcc82790cf878d528f0a50d75230cb3fdacf390c2e94ee7ab2
  summary: Exact transitive is_a ancestry read separately from parthood; GO0070118
    lacks GO0055035 in this native ancestor response, while separate UniProt hierarchy
    supports the broader biological classification.
  support: supports
- evidence_id: micro-GO0055035-isa
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0055035/ancestors?relations=is_a
  locator: Complete exact-term ancestors response with relations=is_a
  accessed_at: '2026-11-03T20:43:20.665428Z'
  snapshot_sha256: 0db506be39ac69e975c0eff439b9e0e62a70654f938ef0fbb05a61bd8487e39b
  summary: Exact transitive is_a ancestry read separately from parthood; GO0070118
    lacks GO0055035 in this native ancestor response, while separate UniProt hierarchy
    supports the broader biological classification.
  support: supports
- evidence_id: micro-GO0070118-isa
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0070118/ancestors?relations=is_a
  locator: Complete exact-term ancestors response with relations=is_a
  accessed_at: '2026-11-03T20:43:20.697783Z'
  snapshot_sha256: 964663439387924de7f28043478cf2e40ffbc6a9f9516a5965227e537d1e92be
  summary: Exact transitive is_a ancestry read separately from parthood; GO0070118
    lacks GO0055035 in this native ancestor response, while separate UniProt hierarchy
    supports the broader biological classification.
  support: supports
- evidence_id: micro-SL-0214
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0214.json
  locator: Complete native location identity/definition/GO mappings/synonyms and nested
    is_a/part_of hierarchy; protein statistics not experimental census
  accessed_at: '2026-11-03T20:43:18.621844Z'
  snapshot_sha256: c849d1946fe23f77351fae5e9e4bcf0515e14578d37497cb0d320bc7ffb0dd93
  summary: Exact GO9527 mapping/three synonyms, cytoplasm-facing orientation and nested
    generic membrane/envelope hierarchy.
  support: supports
- evidence_id: micro-SL-0215
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0215.json
  locator: Complete native location identity/definition/GO mappings/synonyms and nested
    is_a/part_of hierarchy; protein statistics not experimental census
  accessed_at: '2026-11-03T20:43:18.621939Z'
  snapshot_sha256: 3cd370cb7778bb3c3211d864f856c9ee3af9163c78f780327e2e7413277f1b67
  summary: Exact GO9532 mapping/synonym and internal hydrophilic matrix excluding
    thylakoid space; plastid parthood.
  support: supports
- evidence_id: micro-SL-0278
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0278.json
  locator: Complete native location identity/definition/GO mappings/synonyms and nested
    is_a/part_of hierarchy; protein statistics not experimental census
  accessed_at: '2026-11-03T20:43:18.621998Z'
  snapshot_sha256: 45de8a98f24dded78cdf48ab6b0ca4812e1750b2ca31842e7dae26127d21c64e
  summary: ExactGO31976 mapping, thylakoid is_a and plastid part_of. Identity/morphology
    source, not a measured protein stoichiometry or prevalence census.
  support: supports
- evidence_id: micro-SL-0082
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0082.json
  locator: Complete native location identity/definition/GO mappings/synonyms and nested
    is_a/part_of hierarchy; protein statistics not experimental census
  accessed_at: '2026-11-03T20:43:18.622041Z'
  snapshot_sha256: ae0660e1e761b28504bbca0b97ea8b0cd6260df50fc514d37e4bcdb4afb2a3de
  summary: Glaucocystophyte cyanelle identity and plastid hierarchy, cyanobacteria-like
    thylakoids and envelope/peptidoglycan context.
  support: supports
- evidence_id: micro-SL-0356
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0356.json
  locator: Complete native location identity/definition/GO mappings/synonyms and nested
    is_a/part_of hierarchy; protein statistics not experimental census
  accessed_at: '2026-11-03T20:43:18.622077Z'
  snapshot_sha256: fd631a05c9cdbdd6ee8bc4fa220ede8d59ad460cdaecbc15e98f38709d644934
  summary: Exact organellar chromatophore membraneGO70118 with explicit is_aSL0216/GO55035
    and whole-thylakoid parthood. Separate issuing-authority hierarchy, not a fabricated
    direct GO relation.
  support: supports
- evidence_id: micro-tax2759
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759
  locator: Complete identity/rank/lineage/aliases; no taxon prevalence inferred
  accessed_at: '2026-11-03T20:43:19.370793Z'
  snapshot_sha256: 61a68c76c70762c97e0b218568ab037d9a30c0207847247e9e055b5764a61634
  summary: Eukaryota domain.
  support: supports
- evidence_id: micro-tax33090
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/33090
  locator: Complete identity/rank/lineage/aliases; no taxon prevalence inferred
  accessed_at: '2026-11-03T20:43:19.370891Z'
  snapshot_sha256: b1394e36c6896d7ec64cdb301a239f2bc49bc435a22cc21fdba8fdc6217e2d11
  summary: Viridiplantae kingdom/eukaryotic lineage.
  support: supports
- evidence_id: micro-tax3055
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3055
  locator: Complete identity/rank/lineage/aliases; no taxon prevalence inferred
  accessed_at: '2026-11-03T20:43:19.431409Z'
  snapshot_sha256: e3861fe6706cefe2e079e15c0178a65e95efaad3890f548f25e721553eaa93a0
  summary: C.reinhardtii species/green-algal lineage; strain aliases do not establish
    Jin experimental strain.
  support: supports
- evidence_id: micro-tax38254
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/38254
  locator: Complete identity/rank/lineage/aliases; no taxon prevalence inferred
  accessed_at: '2026-11-03T20:43:19.480186Z'
  snapshot_sha256: 4b487eb0e34bcb4941fbb315aae5214c96ea6f60255d71a2aca172cd35844009
  summary: Glaucocystophyceae class, Glaucophyceae/Glaucophyta synonyms.
  support: supports
- evidence_id: micro-catalogue-api
  kind: search
  reference: https://imodulondb.org/api/datasets
  locator: Complete official unpaginated20 organism rows/28 organism-dataset pairs,
    id/name/description/datasets
  accessed_at: '2026-11-03T20:43:49.951558Z'
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  summary: No Chlamydomonas, green-algal or glaucophyte host coverage. Four positive
    molecular/pathway records require applicability assessment; no matched source
    means no downstream gene/module query or unrelated bacterial proxy. Physical lumen
    exclusion remains independently justified.
  support: supports
  search_scope: Official iModulonDB /api/datasets accessed 2026-11-03T20:43:49.951558Z;
    full unpaginated20 organism rows/28 organism-dataset pairs, inspected id/name/description/dataset
    keys for Chlamydomonas/reinhardtii, Viridiplantae/green algae and Glaucocystophyceae/Glaucophyta.
    Bounded to returned catalogue and date, not universal absence.
- evidence_id: micro-historical-runner
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical command /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb datasets;00:49Z PermissionError reading pyvenv.cfg
  accessed_at: '2026-11-03T00:49:00.863225Z'
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  summary: Historical optional runner unavailable, not rerun now. Fresh native catalogue
    fallback used with host-noncoverage scope.
  support: context_only
- evidence_id: micro-keeling-metadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1098%2Frstb.2009.0103%22&format=json&resultType=core&pageSize=25
  locator: Exact quoted DOI query, unique MED record, complete title/authors/year/DOI/publication
    types/abstract and source routes
  accessed_at: '2026-11-03T20:43:19.525908Z'
  snapshot_sha256: 6c4c2d100f04d49ce5c123fd3f3296461de3cad0657279b56756d6bbe72b65a5
  summary: Keeling2010 PMID20124341 is secondary evolutionary review.
  support: context_only
- evidence_id: micro-terashima-metadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1007%2Fs00294-011-0339-1%22&format=json&resultType=core&pageSize=25
  locator: Exact quoted DOI query, unique MED record, complete title/authors/year/DOI/publication
    types/abstract and source routes
  accessed_at: '2026-11-03T20:43:19.978078Z'
  snapshot_sha256: d8e294a37b4aea4f3a848f0878f8bb017e2db164464c73cb3969dac1eb26dff9
  summary: Terashima/Specht/Hippler2011 PMID21533645 is secondary chloroplast-proteome
    review.
  support: context_only
- evidence_id: micro-perez-metadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1146%2Fannurev-cellbio-120823-022747%22&format=json&resultType=core&pageSize=25
  locator: Exact quoted DOI query, unique MED record, complete title/authors/year/DOI/publication
    types/abstract and source routes
  accessed_at: '2026-11-03T20:43:20.041521Z'
  snapshot_sha256: d2469ab1736b506b719d5c3ed200a00504885c61f22f4f60117405441d98ae72
  summary: Perez-Boerema/Engel/Wietrzynski2024 PMID38950450 is explicitly publication
    type Review; oxygenic photosynthetic architecture and qualitative conservation.
  support: context_only
- evidence_id: micro-engel-metadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.7554%2FeLife.04889%22&format=json&resultType=core&pageSize=25
  locator: Exact quoted DOI query, unique MED record, complete title/authors/year/DOI/publication
    types/abstract and source routes
  accessed_at: '2026-11-03T20:43:20.061681Z'
  snapshot_sha256: 1237b5ef0af468270986a2f304f59d4c06d4d40f7b2d5c7f78deec9410a5157f
  summary: Engel2015 PMID25584625/PMC4292175 matches exact primary cryoET study; native
    abstract supports imaging context, body separately read.
  support: context_only
- evidence_id: micro-jin-metadata
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.cell.2022.10.030%22&format=json&resultType=core&pageSize=25
  locator: Exact DOI unique MED36413996 metadata, complete primary abstract and keywordList
    including C.reinhardtii; no full body
  accessed_at: '2026-11-03T20:43:20.018579Z'
  snapshot_sha256: 6acdc39ef406f584db55a65552de51608adb06f87a950c923ed7a863bb58b76e
  summary: Chlamydomonas TOC–TIC cryoEM supercomplex spans both envelope membranes
    and IMS scaffold; supports bounded outer-envelope example, not strain, full model/Methods,
    individual component necessity or every plastid lineage.
  support: supports
- evidence_id: micro-keeling-retained
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2817223/
  locator: Retained genuine HTML10:10:38.582642Z, independently reread complete s1/s3/s6/s9
    including embeddedFigures1–3 captions; no pixels/underlying studies
  accessed_at: '2026-11-03T10:10:38.582642Z'
  snapshot_sha256: 7c0eea300c6d6a694668d62cda30305d8c92b42f72192c66518f1251414c9f95
  summary: Secondary review supports green primary double envelopes and scattered/reduced
    plastids. Old universal mitochondrial claims, chromalveolate hypotheses and numerical
    census are not current assertions.
  support: context_only
- evidence_id: micro-terashima-retained
  kind: authority
  reference: https://link.springer.com/content/pdf/10.1007/s00294-011-0339-1.pdf
  locator: Retained genuine PDF10:10:38.518294Z; independently reread pages151–154
    including title/abstract/Introduction/proteome compilation/initial Photosynthesis
    and text captions; no later pages/pixels/supplementary inventories
  accessed_at: '2026-11-03T10:10:38.518294Z'
  snapshot_sha256: e42edb346d375e4e083e2eb79c6d9eff9fc217513e1ae9ecf808acb143129c6b
  summary: Secondary review supports Chlamydomonas chloroplast metabolic/protein-biogenesis
    research. Chloroplast/mitochondrial enriched preparations and contamination/candidate
    caveats distinguish general stromal/proteome context from an independently purified
    Chlamydomonas stromal dataset; Arabidopsis subfraction data are not reassigned.
  support: context_only
- evidence_id: micro-perez-retained
  kind: authority
  reference: https://www.annualreviews.org/docserver/ahah/fulltext/cellbio/40/1/annurev-cellbio-120823-022747.html?expires=1793737002&id=id&accname=guest&checksum=47EAFDAB41E06430970416431EF37629
  locator: Retained genuine delivered publisherHTML20:02:23.441867Z; independently
    read complete Introduction/evolutionary overview, Building Blocks opening, Lipids
    and ETC sections, embeddedFigure1/2 captions. No pixels/complete later sections/underlying
    primary citations
  accessed_at: '2026-11-03T20:02:23.441867Z'
  snapshot_sha256: d4cb1bbd456fe36ec6dfcbcf218853b725e963929a7ae54588784df02577dd4a
  summary: Secondary review supports pigments/protein complexes and lipid membranes
    enclosing lumen, oxygenic electron transfer and proton gradient. No universal
    exact lipid ratios, per-protein formation necessity or exhaustive taxon-specific
    composition is imported.
  support: context_only
- evidence_id: micro-engel-primary
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4292175/fullTextXML
  locator: Fresh collaborating JATS20:43:24.342979Z independently read s1,s2-1/s2-2/s2-3
    with embedded captions, s3-1/s3-2 and Methods s4-1 through s4-5; no pixels/videos/supplements/raw
    tomography
  accessed_at: '2026-11-03T20:43:24.342979Z'
  snapshot_sha256: 5d5e176465dc54f9a8b7a3b0faace8d7ccfa56ee57bece00723d4b451ff68026
  summary: Direct native thylakoid membrane/lumen cryoFIB/cryoET in C.reinhardtii
    WTCC124(137c), TAP/constant light/air conditions. Network morphology and rare
    envelope contacts observed; universal continuity and molecular transport/biogenesis
    remain hypotheses, not proved mechanisms.
  support: supports
- evidence_id: micro-jin-retained-access
  kind: validation
  reference: https://api.elsevier.com/content/article/PII:S0092867422013769?httpAccept=text/xml
  locator: Retained20:01:44.453877Z publisher XML1941bytes; exact coredata metadata
    inspected; no fresh body request
  accessed_at: '2026-11-03T20:01:44.453877Z'
  snapshot_sha256: f89b1fa484e5f31c9142821a7352ba0906d288e01c84518b7d96822df5b6e2cb
  summary: Full-text response wrapper contains only coredata, not scientific body.
    Current primary abstract remains the available assessed tier; no model/pixels/Methods
    claim.
  support: context_only
- evidence_id: check-qc
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/qc.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T20:47:57.496872Z'
  support: supports
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  snapshot_sha256: 30dd0a0e3709716e352c0ec1aaaceb13f37636079e4035790477e66c6a55c4f2
- evidence_id: check-labels
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/labels.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T20:43:10.859965Z'
  support: supports
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  snapshot_sha256: 6cdfb05df9a27194f05a5fd7f851783f817ac1523ca0bbfa54fe0e0d18775905
- evidence_id: check-trait-links
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/trait-links.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T20:42:50.994465Z'
  support: supports
  summary: Native TraitMech link check passed.
  snapshot_sha256: 8b336cdefbbd3daf6da8787990efdbe346c95e2c8361d50b7eb68a18f2d5a44a
- evidence_id: check-vendored
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/vendored.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T20:42:46.057418Z'
  support: supports
  summary: Pinned governed files match; native vendored check passed.
  snapshot_sha256: b1f169d103aaefa930745468bcca171e5867b9cc49e4e74311e458097e3252a6
- evidence_id: check-curies
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/curies.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T20:42:53.304448Z'
  support: supports
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  snapshot_sha256: bc12b1285f5747707643f7a98e03dbb3a6c88fb062ad49f99db9cb42ececf3d2
- evidence_id: focused
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/focused-results.json
  locator: All twenty actual target schema/strict command outputs
  accessed_at: '2026-11-03T20:49:39Z'
  support: supports
  summary: Ten schema and ten strict commands returned exit zero.
  snapshot_sha256: 59cc4161d6366a4e6f305d02df6a911135847fb929bf7d38705b9bdcec890ab4
- evidence_id: supplemental-pmid
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/pmid-chunks-receipt.json
  locator: Complete native-report PMID set checked with unchanged resolver in batches
    of at most fifty
  accessed_at: '2026-11-03T20:44:18.083811Z'
  support: supports
  summary: 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers
    remain unverified.
  snapshot_sha256: 341ee37ebc1047d67c74d737ff5696d870b20a708894ce207171599c51f61cdb
- evidence_id: historical-adapter-runner-availability
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical runner invocation receipt, exact SHA256 reverified during PR2376
    synthesis
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  summary: Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS
    PermissionError reading the configured runner pyvenv.cfg. This is retained historical
    availability evidence, not a fresh attempt or a scientific validation failure.
    Native policy permits inspected source-catalogue fallback.
- evidence_id: root-native-plastid_outer_membrane-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_outer_membrane-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T20:42:53.275440Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-plastid_outer_membrane-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_outer_membrane-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T20:42:53.690382Z'
  support: context_only
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-plastid_stroma-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_stroma-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T20:42:54.092130Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-plastid_stroma-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_stroma-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T20:42:54.492961Z'
  support: context_only
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-plastid_thylakoid-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_thylakoid-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T20:42:54.889579Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-plastid_thylakoid-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_thylakoid-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T20:42:55.322542Z'
  support: context_only
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-plastid_thylakoid_lumen-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_thylakoid_lumen-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T20:42:55.734821Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-plastid_thylakoid_lumen-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_thylakoid_lumen-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T20:42:56.143705Z'
  support: context_only
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-plastid_thylakoid_membrane-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_thylakoid_membrane-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T20:42:56.552435Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-plastid_thylakoid_membrane-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/plastid_thylakoid_membrane-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T20:42:56.951807Z'
  support: context_only
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-polaroplast-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/polaroplast-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T20:42:57.359602Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-polaroplast-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/polaroplast-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T20:42:57.765821Z'
  support: context_only
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-pusule-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/pusule-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T20:42:58.197647Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-pusule-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/pusule-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T20:42:58.612492Z'
  support: context_only
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-pyrenoid_tubule-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/pyrenoid_tubule-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T20:42:59.023278Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-pyrenoid_tubule-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/pyrenoid_tubule-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T20:42:59.440482Z'
  support: context_only
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-recycling_endosome-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/recycling_endosome-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T20:43:00.740924Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 0 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-recycling_endosome-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/recycling_endosome-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T20:43:01.174351Z'
  support: context_only
  snapshot_sha256: 8ec13ce57264c182b589096a0cec398aeb141a38ec3be5d93c48ecc41174dcbe
  summary: 0 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-recycling_endosome_lumen-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/recycling_endosome_lumen-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T20:43:01.616988Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-recycling_endosome_lumen-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2376/recycling_endosome_lumen-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T20:43:02.031057Z'
  support: context_only
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
assessments:
- assessment_id: septin-pyrenoid_tubule-schema
  area: schema
  topic: Original native validation/render and frozen inputs
  outcome: supported
  summary: Original validate/render pass and Markdown is exact. Every frozen historical
    input hash was checked; current target equals original frozen target. No staleness
    refresh is needed for these three targets.
  target_ids:
  - GO:0160223
  evidence_ids:
  - septin-record-pyrenoid_tubule
  - septin-go
  - septin-engel2015-jats
  - septin-he2023-jats
  - septin-franklin2026-jats
  - septin-original-validation-pyrenoid_tubule
- assessment_id: septin-pyrenoid_tubule-identity
  area: identity
  topic: Exact identity and parent/part boundaries
  outcome: supported
  summary: GO0160223 exact specialized traversing membrane, GO1990732 parthood and
    GO0042651 continuity; membrane classification is supported by definition and primary
    anatomy. No direct full-ancestry query result is claimed.
  target_ids:
  - GO:0160223
  evidence_ids:
  - septin-record-pyrenoid_tubule
  - septin-go
  - septin-engel2015-jats
  - septin-he2023-jats
  - septin-franklin2026-jats
- assessment_id: septin-pyrenoid_tubule-definition
  area: scope
  topic: Definition and explicit biological scope
  outcome: supported
  summary: Definition is membrane topology; nonuniversality across pyrenoids is retained.
    Rubisco-matrix context does not turn the target into whole pyrenoid or a protein.
  target_ids:
  - GO:0160223
  evidence_ids:
  - septin-record-pyrenoid_tubule
  - septin-go
  - septin-engel2015-jats
  - septin-he2023-jats
  - septin-franklin2026-jats
- assessment_id: septin-pyrenoid_tubule-taxon
  area: scope
  topic: Actual host/strain, life stage and occurrence
  outcome: supported
  summary: Chlamydomonas tax3055 matches Engel CC124(137c) and Franklin species context.
    Eukaryota RARE is qualitative lineage restriction, not a measured prevalence rate;
    He supports pyrenoid/tubule diversity and exceptions.
  target_ids:
  - GO:0160223
  evidence_ids:
  - septin-record-pyrenoid_tubule
  - septin-go
  - septin-engel2015-jats
  - septin-he2023-jats
  - septin-franklin2026-jats
  - septin-tax2759
  - septin-tax3055
- assessment_id: septin-pyrenoid_tubule-canonical
  area: evidence
  topic: Canonical experimental observation
  outcome: supported
  summary: Engel primary cryoET resolves parallel minitubules and distinction of their
    stromal lumen from surrounding thylakoid-continuous tubule lumen. Source text
    captions read; pixels/tomograms not inspected.
  target_ids:
  - GO:0160223
  evidence_ids:
  - septin-record-pyrenoid_tubule
  - septin-go
  - septin-engel2015-jats
  - septin-he2023-jats
  - septin-franklin2026-jats
- assessment_id: septin-pyrenoid_tubule-material
  area: grounding
  topic: Material component versus whole structure
  outcome: supported
  summary: Collective REVIEWED_LABEL_ONLY lipid material is explicit and no guessed
    chemical species or whole-structure GO is supplied as its chemical grounding.
    Generic constitutive bilayer is distinct from individual lipid necessity.
  target_ids:
  - GO:0160223
  evidence_ids:
  - septin-record-pyrenoid_tubule
  - septin-go
  - septin-engel2015-jats
  - septin-he2023-jats
  - septin-franklin2026-jats
  - septin-curation-policy
  - septin-schema-policy
- assessment_id: septin-pyrenoid_tubule-function
  area: evidence
  topic: Function, assay scope and molecular necessity
  outcome: supported
  summary: Qualified thought-to-support CO2 delivery matches the explicitly secondary
    He model and Franklin Intro/Discussion. Proteomic fragment enrichment/localization
    is not direct interaction or every candidate being formation-essential.
  target_ids:
  - GO:0160223
  evidence_ids:
  - septin-record-pyrenoid_tubule
  - septin-go
  - septin-engel2015-jats
  - septin-he2023-jats
  - septin-franklin2026-jats
- assessment_id: septin-pyrenoid_tubule-graph
  area: graph
  topic: Complete graph scope and represented actors
  outcome: supported
  summary: NONMECHANISTIC three-edge graph captures parthood, thylakoid continuity
    and traversal. Omitted bicarbonate channels/carbonic anhydrase/diffusion actors
    are explicitly outside graph scope, not a hidden promised mechanism.
  target_ids:
  - GO:0160223
  evidence_ids:
  - septin-record-pyrenoid_tubule
  - septin-go
  - septin-engel2015-jats
  - septin-he2023-jats
  - septin-franklin2026-jats
  - septin-graph-policy
- assessment_id: septin-pyrenoid_tubule-identity-protein
  area: grounding
  topic: Represented protein identity and class limits
  outcome: not_applicable
  summary: No maintained individual protein accession or typed gene/protein actor
    exists. The positive Rubisco narrative is assessed within its source scope without
    inventing mandatory protein examples.
  target_ids:
  - GO:0160223
  evidence_ids:
  - septin-record-pyrenoid_tubule
  - septin-go
  - septin-engel2015-jats
  - septin-he2023-jats
  - septin-franklin2026-jats
  - septin-protein-policy
- assessment_id: septin-pyrenoid_tubule-native
  area: provenance
  topic: Actual native protein checks and coverage
  outcome: supported
  summary: Two actual native commands exit0. Zero examples and zero typed molecular
    nodes; generic verification stdout alone was not used to infer inventory counts.
    Native validity does not prove exhaustive membership, localization or necessity.
  target_ids:
  - GO:0160223
  evidence_ids:
  - septin-record-pyrenoid_tubule
  - septin-go
  - septin-engel2015-jats
  - septin-he2023-jats
  - septin-franklin2026-jats
  - septin-native-pyrenoid_tubule-verify
  - septin-native-pyrenoid_tubule-causal
  - septin-protein-policy
- assessment_id: septin-pyrenoid_tubule-adapter
  area: scope
  topic: Complete-record structured-source applicability
  outcome: supported
  summary: Positive Rubisco/CO2-delivery function triggers source applicability despite
    topological graph. Complete fresh catalogue lacks the actual eukaryotic hosts.
    Use scoped primary/authority fallback, without cyanobacterial proxy or unjustified
    downstream query. This corrects the old expression-only exemption; historical00:49Z
    runner failure is not a new run.
  target_ids:
  - GO:0160223
  evidence_ids:
  - septin-record-pyrenoid_tubule
  - septin-go
  - septin-engel2015-jats
  - septin-he2023-jats
  - septin-franklin2026-jats
  - septin-review-policy
  - septin-catalogue
  - septin-adapter-runner-historical
- assessment_id: septin-pyrenoid_tubule-history
  area: provenance
  topic: Discussion/history and bounded neighbor context
  outcome: supported
  summary: Open label-only lipid-grounding TODO remains open; resolved nonuniversality
    rationale is consistent with anatomical context. No mandatory universal whole-pyrenoid
    has_part is inferred. All records remain PROPOSED; no record mutation, whole-neighbor
    verdict or grouped-issue resolution is claimed.
  target_ids:
  - GO:0160223
  evidence_ids:
  - septin-record-pyrenoid_tubule
  - septin-go
  - septin-engel2015-jats
  - septin-he2023-jats
  - septin-franklin2026-jats
  - septin-curation-policy
- assessment_id: septin-pyrenoid_tubule-formation
  area: completeness
  topic: Unresolved formation and exhaustive molecular composition
  outcome: unknown
  summary: Inspected sources establish scoped anatomy/localization and selected physiological
    effects. They do not establish an exhaustive formation machinery, invariant lipid
    composition or every molecular actor necessary across taxa. Optional protein examples
    are not mandatory solely because literature names proteins.
  target_ids:
  - GO:0160223
  evidence_ids:
  - septin-record-pyrenoid_tubule
  - septin-go
  - septin-engel2015-jats
  - septin-he2023-jats
  - septin-franklin2026-jats
  - septin-protein-policy
- assessment_id: septin-pyrenoid_tubule-optional
  area: scope
  topic: Images, quantitative and other unasserted domains
  outcome: not_applicable
  summary: No maintained image/license claim, numerical measurement, associated-trait
    mapping or verbatim snippet in this target. Text captions are distinct from inspected
    image pixels, and no unseen source pixels/raw data/supplements are certified.
  target_ids:
  - GO:0160223
  evidence_ids:
  - septin-record-pyrenoid_tubule
  - septin-go
  - septin-engel2015-jats
  - septin-he2023-jats
  - septin-franklin2026-jats
- assessment_id: septin-pyrenoid_tubule-verdict
  area: completeness
  topic: Scientific verdict and exact lineage
  outcome: supported
  summary: 'pass_with_limitations: no scientific finding established, within stated
    source-access and composition/necessity limits. No new scientific finding or terminal
    historical finding disposition is invented. Applicability bundle defect is separately
    corrected.'
  target_ids:
  - GO:0160223
  evidence_ids:
  - septin-record-pyrenoid_tubule
  - septin-go
  - septin-engel2015-jats
  - septin-he2023-jats
  - septin-franklin2026-jats
  - septin-original-pyrenoid_tubule
- assessment_id: septin-recycling_endosome-schema
  area: schema
  topic: Original native validation/render and frozen inputs
  outcome: supported
  summary: Original validate/render pass and Markdown is exact. Every frozen historical
    input hash was checked; current target equals original frozen target. No staleness
    refresh is needed for these three targets.
  target_ids:
  - GO:0055037
  evidence_ids:
  - septin-record-recycling_endosome
  - septin-go
  - septin-jeffries2001-meta
  - septin-pal2003-meta
  - septin-umaer2018-pmc
  - septin-original-validation-recycling_endosome
- assessment_id: septin-recycling_endosome-identity
  area: identity
  topic: Exact identity and parent/part boundaries
  outcome: supported
  summary: GO0055037 exact organelle identity, GO0005768 is-a and two distinct membrane/lumen
    parts remain supported; SL0232 is an exact xref with its own typed location relation.
  target_ids:
  - GO:0055037
  evidence_ids:
  - septin-record-recycling_endosome
  - septin-go
  - septin-jeffries2001-meta
  - septin-pal2003-meta
  - septin-umaer2018-pmc
  - septin-SL0232
- assessment_id: septin-recycling_endosome-definition
  area: scope
  topic: Definition and explicit biological scope
  outcome: supported
  summary: Ontology definition describes a recycling network rather than a fixed molecular
    complex. Rab11 marks and regulates studied host compartments without becoming
    a compulsory material constituent.
  target_ids:
  - GO:0055037
  evidence_ids:
  - septin-record-recycling_endosome
  - septin-go
  - septin-jeffries2001-meta
  - septin-pal2003-meta
  - septin-umaer2018-pmc
- assessment_id: septin-recycling_endosome-taxon
  area: scope
  topic: Actual host/strain, life stage and occurrence
  outcome: supported
  summary: Trypanosoma tax5691 is valid. Jeffries complete abstract supports bloodstream/procyclic
    compartments and a more elaborate bloodstream compartment; VARIABLE is stage/context
    qualification rather than demonstrated all-strain prevalence. Umaer Methods specify
    bloodstream single-marker T. b. brucei; no extrapolation to all life stages.
  target_ids:
  - GO:0055037
  evidence_ids:
  - septin-record-recycling_endosome
  - septin-go
  - septin-jeffries2001-meta
  - septin-pal2003-meta
  - septin-umaer2018-pmc
  - septin-tax5691
- assessment_id: septin-recycling_endosome-canonical
  area: evidence
  topic: Canonical experimental observation
  outcome: supported
  summary: Jeffries abstract directly reports Rab11 colocalization with transferrin
    receptor and internalized anti-VSG cargo. This supports the compartment example
    without reclassifying receptor as lumen cargo.
  target_ids:
  - GO:0055037
  evidence_ids:
  - septin-record-recycling_endosome
  - septin-go
  - septin-jeffries2001-meta
  - septin-pal2003-meta
  - septin-umaer2018-pmc
- assessment_id: septin-recycling_endosome-material
  area: grounding
  topic: Material component versus whole structure
  outcome: concern
  summary: 'Inherited major F1 persists: LIPID component is grounded to GO0055038
    whole membrane and linked by component_ref. Correct membrane topology does not
    turn a structural GO term into molecular lipid identity.'
  target_ids:
  - GO:0055037
  evidence_ids:
  - septin-record-recycling_endosome
  - septin-go
  - septin-jeffries2001-meta
  - septin-pal2003-meta
  - septin-umaer2018-pmc
  - septin-curation-policy
  - septin-schema-policy
- assessment_id: septin-recycling_endosome-function
  area: evidence
  topic: Function, assay scope and molecular necessity
  outcome: supported
  summary: Current coarse selective/Rab11-dependent recycling wording is compatible
    with source-specific observations. Pal abstract includes extensive degradation/product
    exocytosis, not intact ligand return; Umaer directly distinguishes affected ISG65
    from largely unaffected VSG/TfR. No universal cargo or organelle-formation necessity
    is claimed.
  target_ids:
  - GO:0055037
  evidence_ids:
  - septin-record-recycling_endosome
  - septin-go
  - septin-jeffries2001-meta
  - septin-pal2003-meta
  - septin-umaer2018-pmc
- assessment_id: septin-recycling_endosome-graph
  area: graph
  topic: Complete graph scope and represented actors
  outcome: concern
  summary: NONMECHANISTIC six-edge graph contains subtype, membrane/lumen parthood,
    boundary, Rab11 localization and selective recycling support. External Rab11 actor
    is permitted; inherited F1 concerns only the membrane component linkage, not correct
    topology or complete-mechanism omission.
  target_ids:
  - GO:0055037
  evidence_ids:
  - septin-record-recycling_endosome
  - septin-go
  - septin-jeffries2001-meta
  - septin-pal2003-meta
  - septin-umaer2018-pmc
  - septin-graph-policy
- assessment_id: septin-recycling_endosome-identity-protein
  area: grounding
  topic: Represented protein identity and class limits
  outcome: supported
  summary: Q9NJE8 is current unreviewed T. brucei Rab11 with primary gene Rab11 and
    RAB11A synonym. Sequence-source references include Jeffries; inferred family annotations
    are not localization experiments. No sequence alignment to Umaer RNAi construct
    or universal strain correspondence was performed.
  target_ids:
  - GO:0055037
  evidence_ids:
  - septin-record-recycling_endosome
  - septin-go
  - septin-jeffries2001-meta
  - septin-pal2003-meta
  - septin-umaer2018-pmc
  - septin-Q9NJE8
  - septin-protein-policy
- assessment_id: septin-recycling_endosome-native
  area: provenance
  topic: Actual native protein checks and coverage
  outcome: supported
  summary: Two actual native commands exit0. Zero examples and one UNANCHORED_WITH_UNIPROT
    external Rab11 node, not COVERED; absence of component_ref is intentional and
    no mandatory constituent inference follows. Native validity does not prove exhaustive
    membership, localization or necessity.
  target_ids:
  - GO:0055037
  evidence_ids:
  - septin-record-recycling_endosome
  - septin-go
  - septin-jeffries2001-meta
  - septin-pal2003-meta
  - septin-umaer2018-pmc
  - septin-native-recycling_endosome-verify
  - septin-native-recycling_endosome-causal
  - septin-protein-policy
- assessment_id: septin-recycling_endosome-adapter
  area: scope
  topic: Complete-record structured-source applicability
  outcome: supported
  summary: Positive Rab11 cargo-recycling biology triggers source applicability. Complete
    fresh catalogue lacks the actual eukaryotic hosts. Use scoped primary/authority
    fallback, without cyanobacterial proxy or unjustified downstream query. This corrects
    the old expression-only exemption; historical00:49Z runner failure is not a new
    run.
  target_ids:
  - GO:0055037
  evidence_ids:
  - septin-record-recycling_endosome
  - septin-go
  - septin-jeffries2001-meta
  - septin-pal2003-meta
  - septin-umaer2018-pmc
  - septin-review-policy
  - septin-catalogue
  - septin-adapter-runner-historical
- assessment_id: septin-recycling_endosome-history
  area: provenance
  topic: Discussion/history and bounded neighbor context
  outcome: supported
  summary: Historical Rab11 marker-not-component interpretation remains intact; correcting
    F1 does not require rewriting dated rationale or moving Rab11 into components.
    All records remain PROPOSED; no record mutation, whole-neighbor verdict or grouped-issue
    resolution is claimed.
  target_ids:
  - GO:0055037
  evidence_ids:
  - septin-record-recycling_endosome
  - septin-go
  - septin-jeffries2001-meta
  - septin-pal2003-meta
  - septin-umaer2018-pmc
  - septin-curation-policy
- assessment_id: septin-recycling_endosome-formation
  area: completeness
  topic: Unresolved formation and exhaustive molecular composition
  outcome: unknown
  summary: Inspected sources establish scoped anatomy/localization and selected physiological
    effects. They do not establish an exhaustive formation machinery, invariant lipid
    composition or every molecular actor necessary across taxa. Optional protein examples
    are not mandatory solely because literature names proteins.
  target_ids:
  - GO:0055037
  evidence_ids:
  - septin-record-recycling_endosome
  - septin-go
  - septin-jeffries2001-meta
  - septin-pal2003-meta
  - septin-umaer2018-pmc
  - septin-protein-policy
- assessment_id: septin-recycling_endosome-optional
  area: scope
  topic: Images, quantitative and other unasserted domains
  outcome: not_applicable
  summary: No maintained image/license claim, numerical measurement, associated-trait
    mapping or verbatim snippet in this target. Text captions are distinct from inspected
    image pixels, and no unseen source pixels/raw data/supplements are certified.
  target_ids:
  - GO:0055037
  evidence_ids:
  - septin-record-recycling_endosome
  - septin-go
  - septin-jeffries2001-meta
  - septin-pal2003-meta
  - septin-umaer2018-pmc
- assessment_id: septin-recycling_endosome-verdict
  area: completeness
  topic: Scientific verdict and exact lineage
  outcome: concern
  summary: 'needs_curation: inherited major F1/key remains confirmed; record curation
    stays outside this PR. No new scientific finding or terminal historical finding
    disposition is invented. Applicability bundle defect is separately corrected.'
  target_ids:
  - GO:0055037
  evidence_ids:
  - septin-record-recycling_endosome
  - septin-go
  - septin-jeffries2001-meta
  - septin-pal2003-meta
  - septin-umaer2018-pmc
  - septin-original-recycling_endosome
- assessment_id: septin-recycling_endosome_lumen-schema
  area: schema
  topic: Original native validation/render and frozen inputs
  outcome: supported
  summary: Original validate/render pass and Markdown is exact. Every frozen historical
    input hash was checked; current target equals original frozen target. No staleness
    refresh is needed for these three targets.
  target_ids:
  - GO:0034777
  evidence_ids:
  - septin-record-recycling_endosome_lumen
  - septin-go
  - septin-jeffries2001-meta
  - septin-original-validation-recycling_endosome_lumen
- assessment_id: septin-recycling_endosome_lumen-identity
  area: identity
  topic: Exact identity and parent/part boundaries
  outcome: supported
  summary: GO0034777 exact enclosed volume, GO0031904 is-a, GO0055037 parthood and
    exact SL0345 synonym remain supported. Boundary membrane is not a lumen constituent.
  target_ids:
  - GO:0034777
  evidence_ids:
  - septin-record-recycling_endosome_lumen
  - septin-go
  - septin-jeffries2001-meta
  - septin-SL0345
- assessment_id: septin-recycling_endosome_lumen-definition
  area: scope
  topic: Definition and explicit biological scope
  outcome: supported
  summary: Definition/function is physical compartmentalization. Positive TbRAB11
    compartment examples are contextual localization, not a claimed lumen-resident
    receptor or molecular routing mechanism.
  target_ids:
  - GO:0034777
  evidence_ids:
  - septin-record-recycling_endosome_lumen
  - septin-go
  - septin-jeffries2001-meta
- assessment_id: septin-recycling_endosome_lumen-taxon
  area: scope
  topic: Actual host/strain, life stage and occurrence
  outcome: supported
  summary: Trypanosoma tax5691 is valid. Jeffries complete abstract supports bloodstream/procyclic
    compartments and a more elaborate bloodstream compartment; VARIABLE is stage/context
    qualification rather than demonstrated all-strain prevalence. No dedicated lumen
    proteome or exact experimental strain is inferred from the accessible Jeffries
    abstract.
  target_ids:
  - GO:0034777
  evidence_ids:
  - septin-record-recycling_endosome_lumen
  - septin-go
  - septin-jeffries2001-meta
  - septin-tax5691
- assessment_id: septin-recycling_endosome_lumen-canonical
  area: evidence
  topic: Canonical experimental observation
  outcome: supported
  summary: Rab11-positive endosomal compartments instantiate a membrane-enclosed volume
    by anatomical inference; Jeffries is not claimed to have isolated and characterized
    a lumen-specific molecular inventory.
  target_ids:
  - GO:0034777
  evidence_ids:
  - septin-record-recycling_endosome_lumen
  - septin-go
  - septin-jeffries2001-meta
- assessment_id: septin-recycling_endosome_lumen-material
  area: grounding
  topic: Material component versus whole structure
  outcome: supported
  summary: No constituent molecular inventory is asserted; surrounding membrane remains
    a separate boundary node. No obligatory protein or lipid example is invented.
  target_ids:
  - GO:0034777
  evidence_ids:
  - septin-record-recycling_endosome_lumen
  - septin-go
  - septin-jeffries2001-meta
  - septin-curation-policy
  - septin-schema-policy
- assessment_id: septin-recycling_endosome_lumen-function
  area: evidence
  topic: Function, assay scope and molecular necessity
  outcome: supported
  summary: Physical lumen compartmentalization is supported by exact ontology definition.
    Current function does not assert that the lumen independently routes cargo or
    that transferrin receptor is a luminal soluble cargo.
  target_ids:
  - GO:0034777
  evidence_ids:
  - septin-record-recycling_endosome_lumen
  - septin-go
  - septin-jeffries2001-meta
- assessment_id: septin-recycling_endosome_lumen-graph
  area: graph
  topic: Complete graph scope and represented actors
  outcome: supported
  summary: NONMECHANISTIC three-edge graph captures lumen is-a, whole-organelle parthood
    and boundary. It expressly excludes Rab11/tether/coat/cargo-selection mechanisms;
    their absence is not an incomplete promised mechanism.
  target_ids:
  - GO:0034777
  evidence_ids:
  - septin-record-recycling_endosome_lumen
  - septin-go
  - septin-jeffries2001-meta
  - septin-graph-policy
- assessment_id: septin-recycling_endosome_lumen-identity-protein
  area: grounding
  topic: Represented protein identity and class limits
  outcome: not_applicable
  summary: No maintained individual protein accession or typed gene/protein actor
    exists. The positive Rab11 narrative is assessed within its source scope without
    inventing mandatory protein examples.
  target_ids:
  - GO:0034777
  evidence_ids:
  - septin-record-recycling_endosome_lumen
  - septin-go
  - septin-jeffries2001-meta
  - septin-protein-policy
- assessment_id: septin-recycling_endosome_lumen-native
  area: provenance
  topic: Actual native protein checks and coverage
  outcome: supported
  summary: Two actual native commands exit0. Zero examples and zero typed molecular
    nodes; generic verification stdout alone was not used to infer inventory counts.
    Native validity does not prove exhaustive membership, localization or necessity.
  target_ids:
  - GO:0034777
  evidence_ids:
  - septin-record-recycling_endosome_lumen
  - septin-go
  - septin-jeffries2001-meta
  - septin-native-recycling_endosome_lumen-verify
  - septin-native-recycling_endosome_lumen-causal
  - septin-protein-policy
- assessment_id: septin-recycling_endosome_lumen-adapter
  area: scope
  topic: Complete-record structured-source applicability
  outcome: supported
  summary: Positive TbRAB11-marked host-compartment narrative triggers applicability
    despite the physical lumen function and expressly excluded graph mechanism. Complete
    fresh catalogue lacks the actual eukaryotic hosts. Use scoped primary/authority
    fallback, without cyanobacterial proxy or unjustified downstream query. This corrects
    the old expression-only exemption; historical00:49Z runner failure is not a new
    run.
  target_ids:
  - GO:0034777
  evidence_ids:
  - septin-record-recycling_endosome_lumen
  - septin-go
  - septin-jeffries2001-meta
  - septin-review-policy
  - septin-catalogue
  - septin-adapter-runner-historical
- assessment_id: septin-recycling_endosome_lumen-history
  area: provenance
  topic: Discussion/history and bounded neighbor context
  outcome: supported
  summary: Current boundary-not-component interpretation and compartmentalization
    function preserve historical correction without claiming new disposal of prior
    issues. All records remain PROPOSED; no record mutation, whole-neighbor verdict
    or grouped-issue resolution is claimed.
  target_ids:
  - GO:0034777
  evidence_ids:
  - septin-record-recycling_endosome_lumen
  - septin-go
  - septin-jeffries2001-meta
  - septin-curation-policy
- assessment_id: septin-recycling_endosome_lumen-formation
  area: completeness
  topic: Unresolved formation and exhaustive molecular composition
  outcome: unknown
  summary: Inspected sources establish scoped anatomy/localization and selected physiological
    effects. They do not establish an exhaustive formation machinery, invariant lipid
    composition or every molecular actor necessary across taxa. Optional protein examples
    are not mandatory solely because literature names proteins.
  target_ids:
  - GO:0034777
  evidence_ids:
  - septin-record-recycling_endosome_lumen
  - septin-go
  - septin-jeffries2001-meta
  - septin-protein-policy
- assessment_id: septin-recycling_endosome_lumen-optional
  area: scope
  topic: Images, quantitative and other unasserted domains
  outcome: not_applicable
  summary: No maintained image/license claim, numerical measurement, associated-trait
    mapping or verbatim snippet in this target. Text captions are distinct from inspected
    image pixels, and no unseen source pixels/raw data/supplements are certified.
  target_ids:
  - GO:0034777
  evidence_ids:
  - septin-record-recycling_endosome_lumen
  - septin-go
  - septin-jeffries2001-meta
- assessment_id: septin-recycling_endosome_lumen-verdict
  area: completeness
  topic: Scientific verdict and exact lineage
  outcome: supported
  summary: 'pass_with_limitations: no scientific finding established, within stated
    source-access and composition/necessity limits. No new scientific finding or terminal
    historical finding disposition is invented. Applicability bundle defect is separately
    corrected.'
  target_ids:
  - GO:0034777
  evidence_ids:
  - septin-record-recycling_endosome_lumen
  - septin-go
  - septin-jeffries2001-meta
  - septin-original-recycling_endosome_lumen
- assessment_id: plaque-t5-schema
  area: schema
  topic: Historical input integrity and native represented protein coverage
  outcome: supported
  summary: Both original pairs validate/render exactly and all27 historical inputs
    match. Current record has0examples/0typed protein nodes, so native protein success
    is an empty-inventory check. Root owns full current corpus/publication gates.
  target_ids:
  - GO:0160201
  evidence_ids:
  - plaque-current-5
  - plaque-original-5
  - plaque-original-checks
  - plaque-native-polaroplast-verify
  - plaque-native-polaroplast-causal
- assessment_id: plaque-t6-schema
  area: schema
  topic: Historical input integrity and native represented protein coverage
  outcome: supported
  summary: Both original pairs validate/render exactly and all27 historical inputs
    match. Current record has0examples/0typed protein nodes, so native protein success
    is an empty-inventory check. Root owns full current corpus/publication gates.
  target_ids:
  - cellstructuremech:pusule
  evidence_ids:
  - plaque-current-6
  - plaque-original-6
  - plaque-original-checks
  - plaque-native-pusule-verify
  - plaque-native-pusule-causal
- assessment_id: plaque-t5-identity
  area: identity
  topic: Polaroplast versus polar tube and nascent sporoplasm
  outcome: supported
  summary: Exact active GO0160201 denotes polaroplast. GO0044099 is a separate conduit,
    not record identity. Pressure phrasing follows the authority; sources qualify
    detailed firing mechanism.
  target_ids:
  - GO:0160201
  evidence_ids:
  - plaque-current-5
  - plaque-go-polar
  - plaque-chen-jats
- assessment_id: plaque-t5-material
  area: grounding
  topic: Aggregate membrane and anterior/posterior subregions
  outcome: supported
  summary: Three LIPID rows explicitly denote aggregate membrane material/anatomical
    subregions and carry reviewed-label-only status; no whole-organelle CURIE is misrepresented
    as a lipid species. Han describes lamellar arrays, flattened tubules and posterior
    polaroplast, while Lv introduction describes lamellae/chambers/tubules. This is
    not an exhaustive molecular or stoichiometric inventory.
  target_ids:
  - GO:0160201
  evidence_ids:
  - plaque-current-5
  - plaque-han-body
  - plaque-lv-jats
  - plaque-schema-policy
- assessment_id: plaque-t5-stale-refresh
  area: graph
  topic: Current added anatomical nodes and edges
  outcome: supported
  summary: Substantive refresh supports anterior_lamellar_polaroplast and posterior_tubular_polaroplast
    STRUCTURE component_refs and their part_of edges to the aggregate membrane system.
    They restate supported anatomical membership, not a new necessary molecular mechanism.
    Current graph has6nodes/5edges; old4nodes/3edges review remains historical.
  target_ids:
  - GO:0160201
  evidence_ids:
  - plaque-current-5
  - plaque-original-5
  - plaque-polaroplast-delta
  - plaque-han-body
  - plaque-lv-jats
- assessment_id: plaque-t5-scope
  area: scope
  topic: Microsporidia prevalence and Nosema example
  outcome: supported
  summary: COMMON is qualitative conserved-invasion-apparatus review scope, not measured
    prevalence. Direct membrane contribution study is N.bombycis CQ1, silkworm propagated
    with KOH-induced germination and BmE context. Species example does not generalize
    assay timing or marker distribution to all microsporidia.
  target_ids:
  - GO:0160201
  evidence_ids:
  - plaque-current-5
  - plaque-han-body
  - plaque-lv-jats
  - plaque-tax-6029
  - plaque-tax-27978
- assessment_id: plaque-t5-function
  area: evidence
  topic: Physical membrane transfer and firing support
  outcome: supported
  summary: Fixed-stage membrane and protein-marker distributions, cryo/TEM cargo and
    lipid analyses support coarse membrane movement/contribution to nascent sporoplasm.
    Current NONMECHANISTIC function graph and softened contribute_to edge do not identify
    force-generating molecules or prove exclusive origin. tracked/visualized is read
    as these bounded observational experiments, not continuous single-membrane tracing.
  target_ids:
  - GO:0160201
  evidence_ids:
  - plaque-current-5
  - plaque-lv-jats
  - plaque-chen-jats
  - plaque-han-body
- assessment_id: plaque-t5-necessity
  area: evidence
  topic: Formation and molecular machinery
  outcome: unknown
  summary: No exact protein/lipid inventory or essentiality is asserted. Surface-marker
    localization in Lv is not a necessary transport or formation mechanism. Open molecular-grounding
    TODO is appropriate; no mandatory optional-inventory finding.
  target_ids:
  - GO:0160201
  evidence_ids:
  - plaque-current-5
  - plaque-lv-jats
  - plaque-rubric
- assessment_id: plaque-t5-adapter
  area: scope
  topic: Structured-source applicability of a physical membrane graph
  outcome: not_applicable
  summary: Current positive assertions are membrane anatomy, physical discharge and
    material contribution; no named gene, molecular pathway/regulator, stress-response
    trait or transcriptomics dataset is asserted. Unassigned transporters/surface
    proteins are an explicit future TODO, not positive molecular membership. Thus
    genuine exclusion remains, clarified beyond original expression-only stock wording.
    Full current catalogue has no matched Microsporidia/Nosema host; no foreign proxy
    or biological absence claim.
  target_ids:
  - GO:0160201
  evidence_ids:
  - plaque-current-5
  - plaque-original-5
  - plaque-policy
  - plaque-catalogue
  - plaque-historical-runner
- assessment_id: plaque-t5-provenance
  area: provenance
  topic: Primary versus secondary source tiers
  outcome: supported
  summary: Exact DOI/title/author/year verified. Han and Chen are secondary scope;
    Lv primary methods/results are independently inspected in declared sections without
    figure-pixel/supplement audit. Existing historical resolution is not newly claimed
    work.
  target_ids:
  - GO:0160201
  evidence_ids:
  - plaque-current-5
  - plaque-han-meta
  - plaque-chen-meta
  - plaque-lv-meta
  - plaque-han-body
  - plaque-chen-jats
  - plaque-lv-jats
  - plaque-history-policy
- assessment_id: plaque-t5-verdict
  area: consistency
  topic: Current polaroplast verdict
  outcome: supported
  summary: Qualified pass remains warranted after source-grounded stale refresh; no
    scientific finding or request_curation action is established. Review-input staleness
    is a bundle defect fixed by linked current-input follow-up, not a record edit.
  target_ids:
  - GO:0160201
  evidence_ids:
  - plaque-current-5
  - plaque-polaroplast-delta
  - plaque-lv-jats
  - plaque-han-body
  - plaque-original-checks
- assessment_id: plaque-t6-identity
  area: identity
  topic: Pusule identity and surface-connected topology
  outcome: supported
  summary: Local identifier avoids adopting a broader term. Dodge publisher summary
    directly supports variable canal-connected sac/tubule/vesicle apparatus with apposed
    plasma/vacuolar membranes. GO membrane-bounded-organelle parent does not require
    sealed lumen; bounded QuickGO search returns0 exact name hits without asserting
    exhaustive nonexistence.
  target_ids:
  - cellstructuremech:pusule
  evidence_ids:
  - plaque-current-6
  - plaque-dodge-publisher
  - plaque-go-pusule
  - plaque-go-pusule-search
- assessment_id: plaque-t6-component
  area: grounding
  topic: Whole-membrane material and unknown necessity
  outcome: supported
  summary: OTHER membrane component with GO0016020 denotes the whole pusular wall,
    not a chemical lipid identity. UNKNOWN essentiality avoids inferring an assembly
    requirement from mature morphology. No protein named solely as a tracer is treated
    as an endogenous constituent.
  target_ids:
  - cellstructuremech:pusule
  evidence_ids:
  - plaque-current-6
  - plaque-go-pusule
  - plaque-dodge-publisher
  - plaque-klut-meta
  - plaque-schema-policy
- assessment_id: plaque-t6-examples
  area: scope
  topic: Three species and experimental contexts
  outcome: supported
  summary: Exact taxa verified. Gavelis studies wild-collected P.kofoidii pseudocolonies;
    Klut deposited abstract identifies P.micans and A.carterae with tracer/serial
    TEM scope. Neither example establishes universal dinoflagellate prevalence, a
    laboratory strain, or same physiological mechanism.
  target_ids:
  - cellstructuremech:pusule
  evidence_ids:
  - plaque-current-6
  - plaque-gavelis-jats
  - plaque-klut-meta
  - plaque-tax-271679
  - plaque-tax-2945
  - plaque-tax-2961
- assessment_id: plaque-t6-physiology
  area: evidence
  topic: Tracer access versus molecular transport
  outcome: supported
  summary: HRP/ferritin/lectin entry through the flagellar canal supports lumen access
    only. Full-text controls were not independently available in the evidence used.
    Record explicitly keeps osmoregulation, secretion and collar/flagellum flow provisional
    and imports no transport function/causal graph or assimilation assertion.
  target_ids:
  - cellstructuremech:pusule
  evidence_ids:
  - plaque-current-6
  - plaque-klut-meta
  - plaque-dodge-publisher
- assessment_id: plaque-t6-boundary
  area: identity
  topic: Pusule versus adjacent nuclear and vacuolar structures
  outcome: supported
  summary: Pusule orange reconstruction is distinct from blue nucleus, green ribbon
    and flagellar rootlets. Frozen nuclear-net and contractile-vacuole identity fields
    provide bounded local context; they are not re-reviewed or resolved.
  target_ids:
  - cellstructuremech:pusule
  evidence_ids:
  - plaque-current-6
  - plaque-gavelis-jats
  - plaque-gavelis-fig2
  - plaque-context-contractile_vacuole
  - plaque-context-nuclear_net
- assessment_id: plaque-t6-image
  area: provenance
  topic: Maintained figure pixels, caption, authors and license
  outcome: supported
  summary: Maintained Fig2 bytes equal fresh versioned PMC download and declared SHA/MD5.
    Actual pixels agree with TEM D, FIB-SEM E and contextual G/H; source caption supports
    bar values. Eight-author attribution and CC BY4.0 permissions are explicit with
    no separate exclusion. OTHER accurately represents mixed panels; no unsupported
    quantitative measurement.
  target_ids:
  - cellstructuremech:pusule
  evidence_ids:
  - plaque-current-6
  - plaque-local-pusule-image
  - plaque-gavelis-fig2
  - plaque-gavelis-jats
  - plaque-gavelis-meta
- assessment_id: plaque-t6-adapter
  area: scope
  topic: Structured-source genuine physical exclusion
  outcome: not_applicable
  summary: Actual record remains anatomy/material/image scope; tracer proteins are
    assay reagents and proposed physiology is explicitly unresolved. No positive molecular/pathway/stress-response
    assertion triggers a required matched-gene analysis. Original stock expression
    wording is clarified but not counted as an unsupported-exclusion defect. Official
    catalogue has no named dinoflagellate host; no foreign proxy is used.
  target_ids:
  - cellstructuremech:pusule
  evidence_ids:
  - plaque-current-6
  - plaque-original-6
  - plaque-policy
  - plaque-catalogue
  - plaque-klut-meta
  - plaque-historical-runner
- assessment_id: plaque-t6-provenance
  area: provenance
  topic: Accurate bounded source access and immutable history
  outcome: supported
  summary: Dodge primary publisher Summary only; Klut primary deposited abstract only;
    Gavelis declared primary Results/Methods/caption/image/license. Past failed publisher
    accesses remain historical claims, not invented new failures. Current fresh successful
    summary/JATS access does not upgrade unread full sources.
  target_ids:
  - cellstructuremech:pusule
  evidence_ids:
  - plaque-current-6
  - plaque-dodge-meta
  - plaque-dodge-publisher
  - plaque-klut-meta
  - plaque-gavelis-jats
  - plaque-history-policy
- assessment_id: plaque-t6-verdict
  area: consistency
  topic: Current pusule verdict
  outcome: supported
  summary: Qualified pass remains warranted; no inherited or new scientific finding/request_curation
    action. Unresolved optional physiology and molecular details remain limitations.
    No neighbor/group disposition is inferred.
  target_ids:
  - cellstructuremech:pusule
  evidence_ids:
  - plaque-current-6
  - plaque-dodge-publisher
  - plaque-klut-meta
  - plaque-gavelis-jats
  - plaque-original-checks
- assessment_id: micro-plastid_outer_membrane-identity
  area: identity
  topic: Exact class and compartment boundaries
  outcome: supported
  summary: ExactGO9527 outer cytoplasm-facing bilayer, GO42170 is_a and envelope parthood/SL0214
    synonyms; primary-green context bounded from extra membranes in complex plastids.
  target_ids:
  - GO:0009527
  evidence_ids:
  - micro-record-plastid_outer_membrane
  - micro-go
  - micro-SL-0214
  - micro-SL-0215
  - micro-SL-0278
  - micro-SL-0356
- assessment_id: micro-plastid_outer_membrane-material
  area: grounding
  topic: Chemical material versus whole anatomical part
  outcome: supported
  summary: Collective label-only bilayer explicitly avoids grounding chemical material
    to whole membrane. Corresponding STRUCTURE node denotes membrane; no erroneous
    chemical species/ratio asserted.
  target_ids:
  - GO:0009527
  evidence_ids:
  - micro-record-plastid_outer_membrane
  - micro-prior-plastid_outer_membrane
  - micro-go
  - micro-component-policy
- assessment_id: micro-plastid_outer_membrane-necessity
  area: evidence
  topic: Formation necessity at exact asserted level
  outcome: unknown
  summary: Collective bilayer is defining material where asserted. Native anatomy,
    mature cryoET morphology and secondary synthesis do not establish necessity of
    each lipid species, photosystem, transporter or assembly protein. Matrix/lumen
    have no fixed necessary constituents.
  target_ids:
  - GO:0009527
  evidence_ids:
  - micro-record-plastid_outer_membrane
  - micro-component-policy
  - micro-go
  - micro-jin-metadata
- assessment_id: micro-plastid_outer_membrane-graph
  area: graph
  topic: Every current graph edge and source scope
  outcome: supported
  summary: 'Three NONMECHANISTIC edges: envelope parthood, faces cytoplasm and bounds
    envelopeIMS. Descriptive GO/SL anatomy, not universal TOC–TIC machinery.'
  target_ids:
  - GO:0009527
  evidence_ids:
  - micro-record-plastid_outer_membrane
  - micro-graph-policy
  - micro-go
  - micro-jin-metadata
- assessment_id: micro-plastid_outer_membrane-taxon
  area: scope
  topic: Verified identities and bounded occurrence
  outcome: supported
  summary: Current Eukaryota/Viridiplantae/C.reinhardtii identities match; Keeling
    supports primary/secondary/reduced plastid distributions. Presence categories
    qualitative, not measured frequencies or universal import machinery.
  target_ids:
  - GO:0009527
  evidence_ids:
  - micro-record-plastid_outer_membrane
  - micro-tax2759
  - micro-tax33090
  - micro-tax3055
  - micro-tax38254
  - micro-go
  - micro-SL-0082
  - micro-keeling-retained
  - micro-perez-retained
- assessment_id: micro-plastid_outer_membrane-example
  area: evidence
  topic: Canonical example and actual source access
  outcome: supported
  summary: Current Jin primary abstract/indexed species supports C.reinhardtii TOC–TIC
    spanning envelope, not exact strain/full Methods/model or universal machinery.
  target_ids:
  - GO:0009527
  evidence_ids:
  - micro-record-plastid_outer_membrane
  - micro-jin-metadata
- assessment_id: micro-plastid_outer_membrane-adapter
  area: evidence
  topic: Whole-record structured-source applicability
  outcome: concern
  summary: Original explicit expression-only N/A check is unsupported because whole
    record positively asserts TOC–TIC protein import. Fresh official catalogue has
    no matching green-algal/glaucophyte host; no unrelated cyanobacterial proxy or
    downstream query.
  target_ids:
  - GO:0009527
  evidence_ids:
  - micro-record-plastid_outer_membrane
  - micro-prior-plastid_outer_membrane
  - micro-policy
  - micro-catalogue-api
  - micro-historical-runner
  - micro-jin-metadata
- assessment_id: micro-plastid_outer_membrane-history
  area: provenance
  topic: Historical rationale/source-tier distinctions
  outcome: supported
  summary: Historical rationale/status/grounding tasks retained; optional molecular-grounding
    TODOs not automatically resolved by whole-membrane identity. No broader/category/neighbor
    issue disposition.
  target_ids:
  - GO:0009527
  evidence_ids:
  - micro-record-plastid_outer_membrane
  - micro-prior-plastid_outer_membrane
  - micro-discussion-policy
  - micro-perez-metadata
  - micro-perez-retained
- assessment_id: micro-plastid_outer_membrane-native
  area: schema
  topic: Frozen-input and native scope validation
  outcome: supported
  summary: All76 original frozen input hashes agree; five originalpairs validate and
    render exactly; assigned target unchanged. Actual ten native protein commands
    pass with zeroexamples/zeroGENE_OR_PROTEINnodes, not exhaustive biological coverage.
  target_ids:
  - GO:0009527
  evidence_ids:
  - micro-record-plastid_outer_membrane
  - micro-original-pairs
  - micro-original-inputs
  - micro-native-plastid_outer_membrane-verify
  - micro-native-plastid_outer_membrane-causal
- assessment_id: micro-plastid_outer_membrane-coverage
  area: completeness
  topic: Full record and qualified verdict
  outcome: supported
  summary: Every maintained field/source placement/graph/history/discussion reviewed.
    No local images, physical-property measurements, verbatim snippets or individual
    accessions asserted. No confirmed scientific finding; qualified positive assessment
    retains stated access/experiment limits.
  target_ids:
  - GO:0009527
  evidence_ids:
  - micro-record-plastid_outer_membrane
  - micro-prior-plastid_outer_membrane
  - micro-policy
  - micro-go
  - micro-jin-metadata
- assessment_id: micro-plastid_stroma-identity
  area: identity
  topic: Exact class and compartment boundaries
  outcome: supported
  summary: ExactGO9532 proteinaceous ground substance supports maintained paraphrase;SL0215
    exact synonym and plastid parthood; matrix excludes thylakoid lumen and envelopeIMS.
  target_ids:
  - GO:0009532
  evidence_ids:
  - micro-record-plastid_stroma
  - micro-go
  - micro-SL-0214
  - micro-SL-0215
  - micro-SL-0278
  - micro-SL-0356
- assessment_id: micro-plastid_stroma-material
  area: grounding
  topic: Chemical material versus whole anatomical part
  outcome: supported
  summary: No fixed components on this volume/matrix record; variable cargo and optional
    proteins are not forced.
  target_ids:
  - GO:0009532
  evidence_ids:
  - micro-record-plastid_stroma
  - micro-prior-plastid_stroma
  - micro-go
  - micro-component-policy
- assessment_id: micro-plastid_stroma-necessity
  area: evidence
  topic: Formation necessity at exact asserted level
  outcome: unknown
  summary: Collective bilayer is defining material where asserted. Native anatomy,
    mature cryoET morphology and secondary synthesis do not establish necessity of
    each lipid species, photosystem, transporter or assembly protein. Matrix/lumen
    have no fixed necessary constituents.
  target_ids:
  - GO:0009532
  evidence_ids:
  - micro-record-plastid_stroma
  - micro-component-policy
  - micro-go
  - micro-terashima-retained
- assessment_id: micro-plastid_stroma-graph
  area: graph
  topic: Every current graph edge and source scope
  outcome: supported
  summary: One NONMECHANISTIC plastid contains stroma relation; no fixed universal
    matrix-protein inventory.
  target_ids:
  - GO:0009532
  evidence_ids:
  - micro-record-plastid_stroma
  - micro-graph-policy
  - micro-go
  - micro-terashima-retained
- assessment_id: micro-plastid_stroma-taxon
  area: scope
  topic: Verified identities and bounded occurrence
  outcome: supported
  summary: Current Eukaryota/Viridiplantae/C.reinhardtii identities match; Keeling
    supports primary/secondary/reduced plastid distributions. Presence categories
    qualitative, not measured frequencies or universal import machinery.
  target_ids:
  - GO:0009532
  evidence_ids:
  - micro-record-plastid_stroma
  - micro-tax2759
  - micro-tax33090
  - micro-tax3055
  - micro-tax38254
  - micro-go
  - micro-SL-0082
  - micro-keeling-retained
  - micro-perez-retained
- assessment_id: micro-plastid_stroma-example
  area: evidence
  topic: Canonical example and actual source access
  outcome: supported
  summary: Terashima secondary pages151–154 support broad Chlamydomonas chloroplast
    proteome/metabolic/protein-biogenesis context. No purified Chlamydomonas stromal
    proteome or individual cargo localization is inferred; Arabidopsis fraction results
    remain separate.
  target_ids:
  - GO:0009532
  evidence_ids:
  - micro-record-plastid_stroma
  - micro-terashima-retained
- assessment_id: micro-plastid_stroma-adapter
  area: evidence
  topic: Whole-record structured-source applicability
  outcome: concern
  summary: Original explicit expression-only N/A check is unsupported because whole
    record positively asserts metabolic/protein-biogenesis proteins in Chlamydomonas
    stroma. Fresh official catalogue has no matching green-algal/glaucophyte host;
    no unrelated cyanobacterial proxy or downstream query.
  target_ids:
  - GO:0009532
  evidence_ids:
  - micro-record-plastid_stroma
  - micro-prior-plastid_stroma
  - micro-policy
  - micro-catalogue-api
  - micro-historical-runner
  - micro-terashima-retained
- assessment_id: micro-plastid_stroma-history
  area: provenance
  topic: Historical rationale/source-tier distinctions
  outcome: supported
  summary: Historical rationale/status/grounding tasks retained; optional molecular-grounding
    TODOs not automatically resolved by whole-membrane identity. No broader/category/neighbor
    issue disposition.
  target_ids:
  - GO:0009532
  evidence_ids:
  - micro-record-plastid_stroma
  - micro-prior-plastid_stroma
  - micro-discussion-policy
  - micro-perez-metadata
  - micro-perez-retained
- assessment_id: micro-plastid_stroma-native
  area: schema
  topic: Frozen-input and native scope validation
  outcome: supported
  summary: All76 original frozen input hashes agree; five originalpairs validate and
    render exactly; assigned target unchanged. Actual ten native protein commands
    pass with zeroexamples/zeroGENE_OR_PROTEINnodes, not exhaustive biological coverage.
  target_ids:
  - GO:0009532
  evidence_ids:
  - micro-record-plastid_stroma
  - micro-original-pairs
  - micro-original-inputs
  - micro-native-plastid_stroma-verify
  - micro-native-plastid_stroma-causal
- assessment_id: micro-plastid_stroma-coverage
  area: completeness
  topic: Full record and qualified verdict
  outcome: supported
  summary: Every maintained field/source placement/graph/history/discussion reviewed.
    No local images, physical-property measurements, verbatim snippets or individual
    accessions asserted. No confirmed scientific finding; qualified positive assessment
    retains stated access/experiment limits.
  target_ids:
  - GO:0009532
  evidence_ids:
  - micro-record-plastid_stroma
  - micro-prior-plastid_stroma
  - micro-policy
  - micro-go
  - micro-terashima-retained
- assessment_id: micro-plastid_thylakoid-identity
  area: identity
  topic: Exact class and compartment boundaries
  outcome: supported
  summary: ExactGO31976 whole thylakoid in plastid, parentGO9579/plastid parthood
    and distinct membrane/lumen parts. OTHER kind respects native non-organelle comment
    without conflating filesystem category.
  target_ids:
  - GO:0031976
  evidence_ids:
  - micro-record-plastid_thylakoid
  - micro-go
  - micro-SL-0214
  - micro-SL-0215
  - micro-SL-0278
  - micro-SL-0356
- assessment_id: micro-plastid_thylakoid-material
  area: grounding
  topic: Chemical material versus whole anatomical part
  outcome: concern
  summary: 'Inherited majorF1 confirmed: LIPID component identity is entireGO55035
    membrane and graphcomponent_ref propagates mismatch. Preserve true boundary/has_part
    and accurate structural or label-only material alternatives.'
  target_ids:
  - GO:0031976
  evidence_ids:
  - micro-record-plastid_thylakoid
  - micro-prior-plastid_thylakoid
  - micro-go
  - micro-component-policy
- assessment_id: micro-plastid_thylakoid-necessity
  area: evidence
  topic: Formation necessity at exact asserted level
  outcome: unknown
  summary: Collective bilayer is defining material where asserted. Native anatomy,
    mature cryoET morphology and secondary synthesis do not establish necessity of
    each lipid species, photosystem, transporter or assembly protein. Matrix/lumen
    have no fixed necessary constituents.
  target_ids:
  - GO:0031976
  evidence_ids:
  - micro-record-plastid_thylakoid
  - micro-component-policy
  - micro-go
  - micro-engel-primary
  - micro-perez-retained
- assessment_id: micro-plastid_thylakoid-graph
  area: graph
  topic: Every current graph edge and source scope
  outcome: supported
  summary: 'Three NONMECHANISTIC edges: membrane bounds lumen, supports oxygenic light
    reactions and part_of whole thylakoid. Valid topology/function retained independently
    of F1 material/structure component_ref mismatch.'
  target_ids:
  - GO:0031976
  evidence_ids:
  - micro-record-plastid_thylakoid
  - micro-graph-policy
  - micro-go
  - micro-engel-primary
  - micro-perez-retained
- assessment_id: micro-plastid_thylakoid-taxon
  area: scope
  topic: Verified identities and bounded occurrence
  outcome: supported
  summary: Current Viridiplantae/Glaucocystophyceae/C.reinhardtii identities match.
    Native cyanelle classes plusSL0082 establish glaucophyte subtype; secondary review
    supports photosynthetic green lineages. COMMON remains qualitative rather than
    measured prevalence.
  target_ids:
  - GO:0031976
  evidence_ids:
  - micro-record-plastid_thylakoid
  - micro-tax2759
  - micro-tax33090
  - micro-tax3055
  - micro-tax38254
  - micro-go
  - micro-SL-0082
  - micro-keeling-retained
  - micro-perez-retained
- assessment_id: micro-plastid_thylakoid-example
  area: evidence
  topic: Canonical example and actual source access
  outcome: supported
  summary: Engel primary body directly supports native membrane/lumen cryoET example
    in CC124(137c), with TAP/constant light/air and43tomograms/27lamellae scoped.
    No quantitative property is copied to generic record; universal continuity and
    transport hypotheses not promoted.
  target_ids:
  - GO:0031976
  evidence_ids:
  - micro-record-plastid_thylakoid
  - micro-engel-primary
  - micro-perez-retained
- assessment_id: micro-plastid_thylakoid-adapter
  area: evidence
  topic: Whole-record structured-source applicability
  outcome: concern
  summary: Original prose-only photosynthesis-versus-expression exclusion is unsupported
    because whole record positively asserts photosynthetic light-reaction complexes/pathway.
    Fresh official catalogue has no matching green-algal/glaucophyte host; no unrelated
    cyanobacterial proxy or downstream query.
  target_ids:
  - GO:0031976
  evidence_ids:
  - micro-record-plastid_thylakoid
  - micro-prior-plastid_thylakoid
  - micro-policy
  - micro-catalogue-api
  - micro-historical-runner
  - micro-engel-primary
  - micro-perez-retained
- assessment_id: micro-plastid_thylakoid-history
  area: provenance
  topic: Historical rationale/source-tier distinctions
  outcome: concern
  summary: Original Perez browser passages and HTTP403 route are mislabeled primary_source
    despite secondary/access-limit prose. Successor explicitly uses secondary authority/context
    and separates route failure from scientific primary evidence; historical observations
    retained.
  target_ids:
  - GO:0031976
  evidence_ids:
  - micro-record-plastid_thylakoid
  - micro-prior-plastid_thylakoid
  - micro-discussion-policy
  - micro-perez-metadata
  - micro-perez-retained
- assessment_id: micro-plastid_thylakoid-native
  area: schema
  topic: Frozen-input and native scope validation
  outcome: supported
  summary: All76 original frozen input hashes agree; five originalpairs validate and
    render exactly; assigned target unchanged. Actual ten native protein commands
    pass with zeroexamples/zeroGENE_OR_PROTEINnodes, not exhaustive biological coverage.
  target_ids:
  - GO:0031976
  evidence_ids:
  - micro-record-plastid_thylakoid
  - micro-original-pairs
  - micro-original-inputs
  - micro-native-plastid_thylakoid-verify
  - micro-native-plastid_thylakoid-causal
- assessment_id: micro-plastid_thylakoid-coverage
  area: completeness
  topic: Full record and qualified verdict
  outcome: supported
  summary: Every maintained field/source placement/graph/history/discussion reviewed.
    No local images, physical-property measurements, verbatim snippets or individual
    accessions asserted. One inherited majorF1/action retained, no new scientific
    finding.
  target_ids:
  - GO:0031976
  evidence_ids:
  - micro-record-plastid_thylakoid
  - micro-prior-plastid_thylakoid
  - micro-policy
  - micro-go
  - micro-engel-primary
  - micro-perez-retained
- assessment_id: micro-plastid_thylakoid_lumen-identity
  area: identity
  topic: Exact class and compartment boundaries
  outcome: supported
  summary: ExactGO31978 enclosed lumen with parentGO31977 and whole-thylakoid parthood;
    no boundary membrane misidentified as lumen component.
  target_ids:
  - GO:0031978
  evidence_ids:
  - micro-record-plastid_thylakoid_lumen
  - micro-go
  - micro-SL-0214
  - micro-SL-0215
  - micro-SL-0278
  - micro-SL-0356
- assessment_id: micro-plastid_thylakoid_lumen-material
  area: grounding
  topic: Chemical material versus whole anatomical part
  outcome: supported
  summary: No fixed components on this volume/matrix record; variable cargo and optional
    proteins are not forced.
  target_ids:
  - GO:0031978
  evidence_ids:
  - micro-record-plastid_thylakoid_lumen
  - micro-prior-plastid_thylakoid_lumen
  - micro-go
  - micro-component-policy
- assessment_id: micro-plastid_thylakoid_lumen-necessity
  area: evidence
  topic: Formation necessity at exact asserted level
  outcome: unknown
  summary: Collective bilayer is defining material where asserted. Native anatomy,
    mature cryoET morphology and secondary synthesis do not establish necessity of
    each lipid species, photosystem, transporter or assembly protein. Matrix/lumen
    have no fixed necessary constituents.
  target_ids:
  - GO:0031978
  evidence_ids:
  - micro-record-plastid_thylakoid_lumen
  - micro-component-policy
  - micro-go
  - micro-engel-primary
  - micro-perez-retained
- assessment_id: micro-plastid_thylakoid_lumen-graph
  area: graph
  topic: Every current graph edge and source scope
  outcome: supported
  summary: 'Two NONMECHANISTIC edges: lumen part_of thylakoid and membrane encloses
    lumen. No proton concentration/transport machinery or cargo inventory is asserted.'
  target_ids:
  - GO:0031978
  evidence_ids:
  - micro-record-plastid_thylakoid_lumen
  - micro-graph-policy
  - micro-go
  - micro-engel-primary
  - micro-perez-retained
- assessment_id: micro-plastid_thylakoid_lumen-taxon
  area: scope
  topic: Verified identities and bounded occurrence
  outcome: supported
  summary: Current Viridiplantae/Glaucocystophyceae/C.reinhardtii identities match.
    Native cyanelle classes plusSL0082 establish glaucophyte subtype; secondary review
    supports photosynthetic green lineages. COMMON remains qualitative rather than
    measured prevalence.
  target_ids:
  - GO:0031978
  evidence_ids:
  - micro-record-plastid_thylakoid_lumen
  - micro-tax2759
  - micro-tax33090
  - micro-tax3055
  - micro-tax38254
  - micro-go
  - micro-SL-0082
  - micro-keeling-retained
  - micro-perez-retained
- assessment_id: micro-plastid_thylakoid_lumen-example
  area: evidence
  topic: Canonical example and actual source access
  outcome: supported
  summary: Engel primary body directly supports native membrane/lumen cryoET example
    in CC124(137c), with TAP/constant light/air and43tomograms/27lamellae scoped.
    No quantitative property is copied to generic record; universal continuity and
    transport hypotheses not promoted.
  target_ids:
  - GO:0031978
  evidence_ids:
  - micro-record-plastid_thylakoid_lumen
  - micro-engel-primary
  - micro-perez-retained
- assessment_id: micro-plastid_thylakoid_lumen-adapter
  area: evidence
  topic: Whole-record structured-source applicability
  outcome: not_applicable
  summary: 'Genuine physical exclusion: maintained lumen is anatomical enclosed volume
    and cryoET morphology; explicit scope withholds lumenal proteins/proton transport.
    Cited paper background does not create a positive pathway claim on this record.'
  target_ids:
  - GO:0031978
  evidence_ids:
  - micro-record-plastid_thylakoid_lumen
  - micro-prior-plastid_thylakoid_lumen
  - micro-policy
  - micro-catalogue-api
  - micro-historical-runner
  - micro-engel-primary
  - micro-perez-retained
- assessment_id: micro-plastid_thylakoid_lumen-history
  area: provenance
  topic: Historical rationale/source-tier distinctions
  outcome: concern
  summary: Original Perez browser passages and HTTP403 route are mislabeled primary_source
    despite secondary/access-limit prose. Successor explicitly uses secondary authority/context
    and separates route failure from scientific primary evidence; historical observations
    retained.
  target_ids:
  - GO:0031978
  evidence_ids:
  - micro-record-plastid_thylakoid_lumen
  - micro-prior-plastid_thylakoid_lumen
  - micro-discussion-policy
  - micro-perez-metadata
  - micro-perez-retained
- assessment_id: micro-plastid_thylakoid_lumen-native
  area: schema
  topic: Frozen-input and native scope validation
  outcome: supported
  summary: All76 original frozen input hashes agree; five originalpairs validate and
    render exactly; assigned target unchanged. Actual ten native protein commands
    pass with zeroexamples/zeroGENE_OR_PROTEINnodes, not exhaustive biological coverage.
  target_ids:
  - GO:0031978
  evidence_ids:
  - micro-record-plastid_thylakoid_lumen
  - micro-original-pairs
  - micro-original-inputs
  - micro-native-plastid_thylakoid_lumen-verify
  - micro-native-plastid_thylakoid_lumen-causal
- assessment_id: micro-plastid_thylakoid_lumen-coverage
  area: completeness
  topic: Full record and qualified verdict
  outcome: supported
  summary: Every maintained field/source placement/graph/history/discussion reviewed.
    No local images, physical-property measurements, verbatim snippets or individual
    accessions asserted. No confirmed scientific finding; qualified positive assessment
    retains stated access/experiment limits.
  target_ids:
  - GO:0031978
  evidence_ids:
  - micro-record-plastid_thylakoid_lumen
  - micro-prior-plastid_thylakoid_lumen
  - micro-policy
  - micro-go
  - micro-engel-primary
  - micro-perez-retained
- assessment_id: micro-plastid_thylakoid_membrane-identity
  area: identity
  topic: Exact class and compartment boundaries
  outcome: supported
  summary: ExactGO55035 lipid bilayer of a plastid thylakoid, parentGO42651 and whole-thylakoid
    parthood. Chloroplast/cyanelle native child relations; organellar chromatophore
    classification supported separately bySL0356, not invented GO edge.
  target_ids:
  - GO:0055035
  evidence_ids:
  - micro-record-plastid_thylakoid_membrane
  - micro-go
  - micro-SL-0214
  - micro-SL-0215
  - micro-SL-0278
  - micro-SL-0356
- assessment_id: micro-plastid_thylakoid_membrane-material
  area: grounding
  topic: Chemical material versus whole anatomical part
  outcome: supported
  summary: Collective label-only bilayer explicitly avoids grounding chemical material
    to whole membrane. Corresponding STRUCTURE node denotes membrane; no erroneous
    chemical species/ratio asserted.
  target_ids:
  - GO:0055035
  evidence_ids:
  - micro-record-plastid_thylakoid_membrane
  - micro-prior-plastid_thylakoid_membrane
  - micro-go
  - micro-component-policy
- assessment_id: micro-plastid_thylakoid_membrane-necessity
  area: evidence
  topic: Formation necessity at exact asserted level
  outcome: unknown
  summary: Collective bilayer is defining material where asserted. Native anatomy,
    mature cryoET morphology and secondary synthesis do not establish necessity of
    each lipid species, photosystem, transporter or assembly protein. Matrix/lumen
    have no fixed necessary constituents.
  target_ids:
  - GO:0055035
  evidence_ids:
  - micro-record-plastid_thylakoid_membrane
  - micro-component-policy
  - micro-go
  - micro-engel-primary
  - micro-perez-retained
- assessment_id: micro-plastid_thylakoid_membrane-graph
  area: graph
  topic: Every current graph edge and source scope
  outcome: supported
  summary: 'Two NONMECHANISTIC edges: membrane bounds lumen and supports light reactions.
    Source secondary synthesis supports oxygenic electron transfer/proton gradient;
    not complete pathway stoichiometry or individual assembly requirements.'
  target_ids:
  - GO:0055035
  evidence_ids:
  - micro-record-plastid_thylakoid_membrane
  - micro-graph-policy
  - micro-go
  - micro-engel-primary
  - micro-perez-retained
- assessment_id: micro-plastid_thylakoid_membrane-taxon
  area: scope
  topic: Verified identities and bounded occurrence
  outcome: supported
  summary: Current Viridiplantae/Glaucocystophyceae/C.reinhardtii identities match.
    Native cyanelle classes plusSL0082 establish glaucophyte subtype; secondary review
    supports photosynthetic green lineages. COMMON remains qualitative rather than
    measured prevalence.
  target_ids:
  - GO:0055035
  evidence_ids:
  - micro-record-plastid_thylakoid_membrane
  - micro-tax2759
  - micro-tax33090
  - micro-tax3055
  - micro-tax38254
  - micro-go
  - micro-SL-0082
  - micro-keeling-retained
  - micro-perez-retained
- assessment_id: micro-plastid_thylakoid_membrane-example
  area: evidence
  topic: Canonical example and actual source access
  outcome: supported
  summary: Engel primary body directly supports native membrane/lumen cryoET example
    in CC124(137c), with TAP/constant light/air and43tomograms/27lamellae scoped.
    No quantitative property is copied to generic record; universal continuity and
    transport hypotheses not promoted.
  target_ids:
  - GO:0055035
  evidence_ids:
  - micro-record-plastid_thylakoid_membrane
  - micro-engel-primary
  - micro-perez-retained
- assessment_id: micro-plastid_thylakoid_membrane-adapter
  area: evidence
  topic: Whole-record structured-source applicability
  outcome: concern
  summary: Original prose-only photosynthesis-versus-expression exclusion is unsupported
    because whole record positively asserts photosynthetic light-reaction complexes/pathway.
    Fresh official catalogue has no matching green-algal/glaucophyte host; no unrelated
    cyanobacterial proxy or downstream query.
  target_ids:
  - GO:0055035
  evidence_ids:
  - micro-record-plastid_thylakoid_membrane
  - micro-prior-plastid_thylakoid_membrane
  - micro-policy
  - micro-catalogue-api
  - micro-historical-runner
  - micro-engel-primary
  - micro-perez-retained
- assessment_id: micro-plastid_thylakoid_membrane-history
  area: provenance
  topic: Historical rationale/source-tier distinctions
  outcome: concern
  summary: Original Perez browser passages and HTTP403 route are mislabeled primary_source
    despite secondary/access-limit prose. Successor explicitly uses secondary authority/context
    and separates route failure from scientific primary evidence; historical observations
    retained.
  target_ids:
  - GO:0055035
  evidence_ids:
  - micro-record-plastid_thylakoid_membrane
  - micro-prior-plastid_thylakoid_membrane
  - micro-discussion-policy
  - micro-perez-metadata
  - micro-perez-retained
- assessment_id: micro-plastid_thylakoid_membrane-native
  area: schema
  topic: Frozen-input and native scope validation
  outcome: supported
  summary: All76 original frozen input hashes agree; five originalpairs validate and
    render exactly; assigned target unchanged. Actual ten native protein commands
    pass with zeroexamples/zeroGENE_OR_PROTEINnodes, not exhaustive biological coverage.
  target_ids:
  - GO:0055035
  evidence_ids:
  - micro-record-plastid_thylakoid_membrane
  - micro-original-pairs
  - micro-original-inputs
  - micro-native-plastid_thylakoid_membrane-verify
  - micro-native-plastid_thylakoid_membrane-causal
- assessment_id: micro-plastid_thylakoid_membrane-coverage
  area: completeness
  topic: Full record and qualified verdict
  outcome: supported
  summary: Every maintained field/source placement/graph/history/discussion reviewed.
    No local images, physical-property measurements, verbatim snippets or individual
    accessions asserted. No confirmed scientific finding; qualified positive assessment
    retains stated access/experiment limits.
  target_ids:
  - GO:0055035
  evidence_ids:
  - micro-record-plastid_thylakoid_membrane
  - micro-prior-plastid_thylakoid_membrane
  - micro-policy
  - micro-go
  - micro-engel-primary
  - micro-perez-retained
- assessment_id: current-input-comparison
  area: provenance
  topic: Complete frozen-input comparison and bounded refresh
  outcome: supported
  summary: 1 of ten original target hashes differ from current main. The changed content
    is substantively reassessed in the target-specific assessments; original observations
    remain historical and unchanged. All current target and used context bytes are
    frozen.
  target_ids:
  - GO:0009527
  - GO:0009532
  - GO:0031976
  - GO:0031978
  - GO:0055035
  - GO:0160201
  - cellstructuremech:pusule
  - GO:0160223
  - GO:0055037
  - GO:0034777
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
- finding_id: septin-recycling_endosome-F1
  issue_key: recycling-endosome-lipid-whole-membrane-grounding
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Separate whole-membrane structure from molecular lipid grounding
  description: The LIPID component uses GO0055038 for the entire membrane and the
    graph links that node through component_ref. GO identifies the structural boundary,
    not a molecular lipid class. Valid membrane parthood does not repair this explicit
    type/grounding mismatch.
  target_ids:
  - GO:0055037
  field_paths:
  - components[0].component_type
  - components[0].grounding
  - causal_graphs[0].nodes[2].component_ref
  evidence_ids:
  - septin-record-recycling_endosome
  - septin-go
  - septin-schema-policy
  - septin-curation-policy
  - septin-original-recycling_endosome
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/recycling_endosome.yaml
    role: maintained scientific record
  rule_id: StructuralComponent type and grounding contract
  native_severity: major
  normalization_reason: The molecular component category is materially misrepresented
    and propagated into the graph link; this is not merely an optional missing lipid
    identifier.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T033003Z-recycling-endosome-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2789
- finding_id: micro-F1
  issue_key: plastid-thylakoid-membrane-lipid-identity
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Separate the whole membrane part from its lipid material identity
  description: components[0] is typed LIPID but grounded to GO0055035, which identifies
    the complete plastid thylakoid membrane. The exact GO definition includes a lipid
    bilayer as a structure; it is not an identifier for a molecular lipid constituent.
    The membrane graph node links back through component_ref. Preserve correct has_part
    and boundary topology while either representing this complete membrane as an accurately
    typed structural constituent or representing the collective lipid material without
    using the whole-membrane GO identity.
  target_ids:
  - GO:0031976
  field_paths:
  - components[0].component_type
  - components[0].grounding
  - causal_graphs[0].nodes[1].component_ref
  evidence_ids:
  - micro-record-plastid_thylakoid
  - micro-prior-plastid_thylakoid
  - micro-go
  - micro-component-policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/plastid_thylakoid.yaml
    role: maintained scientific record
  rule_id: Typed constituent identity must match the exact grounding
  native_severity: major
  normalization_reason: The chemical material field identifies an entire cellular
    structure, materially changing the constituent identity and graph-to-component
    join. Accurate membrane existence/parthood is retained; this is not a demand for
    an optional detailed lipid inventory.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T032958Z-plastid-thylakoid-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2788
actions:
- action_id: septin-recycling_endosome-A1
  finding_ids:
  - septin-recycling_endosome-F1
  target_ids:
  - GO:0055037
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/recycling_endosome.yaml
    role: maintained scientific record
  description: Retain the valid membrane structural node and has_part. Represent collective
    lipid material with an honest label-only or justified chemical grounding, or explicitly
    represent the intended structural subpart with an appropriate type; align component_ref
    with that choice.
  acceptance_checks:
  - No LIPID molecular row is grounded to the whole membrane GO identity.
  - Correct membrane/lumen topology and Rab11 external-regulator distinction remain
    intact.
  - No exact lipid species or obligatory protein inventory is invented.
  - Focused native schema, strict, identifier, graph and history checks pass after
    separately authorized curation.
- action_id: micro-A1
  finding_ids:
  - micro-F1
  target_ids:
  - GO:0031976
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/plastid_thylakoid.yaml
    role: maintained scientific record
  description: In separately authorized curation, distinguish the whole membrane structural
    part from its collective lipid material, align component type/grounding and the
    component_ref join, and retain correct whole/part topology.
  acceptance_checks:
  - The LIPID identity no longer denotes a whole membrane GO class; an accurate OTHER
    structural constituent remains permissible.
  - Boundary, light-reaction and taxon claims remain supported at their existing scope.
  - Native schema, strict, CURIE, graph and history checks pass.
limitations:
- 'Pyrenoid tubule and two recycling-endosome records independent subreview: Independent
  read-only scope: three unchanged targets; one inherited confirmed major recycling-endosome
  lipid/whole-membrane grounding finding. Pyrenoid tubule and recycling lumen pass
  with limitations. Three explicit expression-only adapter exemptions require corrected
  applicability evidence. No new scientific finding or record mutation.'
- 'Pyrenoid tubule and two recycling-endosome records independent subreview: All current
  authority/catalogue/metadata and genuine bodies were freshly fetched with recorded
  timestamps and SHA256. Engel scientific scope is Results s2-5, Discussion s3-3,
  Methods s4-1–4 and text captions; no source pixels/videos/raw tomograms. He is secondary
  review, inspected Introduction/operating-principles/membrane sections, not a primary
  experiment or reference-body audit.'
- 'Pyrenoid tubule and two recycling-endosome records independent subreview: Franklin
  inspected Intro, strain/membrane-affinity Methods, membrane-isolation/relative-proteome
  Results and method/function Discussion with embedded tables/captions. Candidate-specific
  mutant results, raw MS and supplements were not independently audited. Membrane-fragment
  enrichment is not direct interaction, completeness or formation necessity. Online2025
  versus publication2026 dates are distinguished. No exact contradictory source CC
  strain number is imported into a species-level record.'
- 'Pyrenoid tubule and two recycling-endosome records independent subreview: Jeffries
  and Pal complete primary abstracts/metadata only: publisher403 and XML500/PDF preparation
  HTML prevented genuine full bodies in attempted endpoints. No exact strain/Methods/pixels
  are certified. Pal explicitly includes degradation/product exocytosis, so intact-ligand
  or universal endogenous-cargo dependence is not inferred. Access failure is not
  refutation.'
- 'Pyrenoid tubule and two recycling-endosome records independent subreview: Umaer
  genuine scientific Introduction/Results/Discussion and Methods plus text captions
  were read. Bloodstream single-marker RNAi effects are selective for ISG65 versus
  largely unaffected VSG/TfR; source context does not generalize to every stage/cargo.
  No pixels/supplements/raw reanalysis or sequence alignment between Q9NJE8 and the
  RNAi locus was performed.'
- 'Pyrenoid tubule and two recycling-endosome records independent subreview: Q9NJE8
  current unreviewed identity/primary gene/taxon are compatible with external Rab11
  marker. Inferred family annotation is not experimental localization. Native checks
  pass on zero examples and one UNANCHORED_WITH_UNIPROT node for whole recycling endosome;
  the other two targets have zero examples and zero typed nodes. These statuses are
  not complete molecular coverage or obligatory constituent claims.'
- 'Pyrenoid tubule and two recycling-endosome records independent subreview: Fresh
  complete catalogue has no actual eukaryotic host match; no unmatched cyanobacterial
  proxy or downstream module query used. Catalogue noncoverage is not biological absence.
  Historical00:49Z runner PermissionError is retained only with its actual old timestamp,
  distinct from fresh HTTP/source fallback.'
- 'Pyrenoid tubule and two recycling-endosome records independent subreview: All28
  actually used repository inputs were frozen before reading:17 common inputs,3 targets,6
  originals and2 bounded anatomy neighbors. Every historical source-input hash of
  the three originals was also checked without scientifically reauditing unrelated
  historical neighbors. No whole-neighbor/grouped-issue disposition or future saved-head/global-QC/CI/queue
  certification is claimed.'
- 'Polaroplast and pusule independent subreview: Both assigned targets retain pass_with_limitations;
  no scientific finding or request_curation action established. Polaroplast stale
  graph is refreshable entirely in review-bundle scope; pusule unchanged. No record
  edits or new inventory mandatory requirements.'
- 'Polaroplast and pusule independent subreview: Original native YAML validation and
  exact Markdown render pass for both; all12polaroplast+15pusule historical frozen
  inputs match. Current6nodes/5edges are independently reassessed rather than replacing
  a hash or treating historical4nodes/3edges as current.'
- 'Polaroplast and pusule independent subreview: Han is a secondary book chapter,
  not primary experiment despite a metadata publication-type tag. Only declared Introduction/Section8.2
  membrane paragraphs and Fig8.1/8.2/8.4–6 captions were read; no pixels or full underlying
  cited primary studies. Chen is secondary review; declared germination/structural/concluding
  paragraphs only.'
- 'Polaroplast and pusule independent subreview: Lv primary JATS declared Introduction/Results/Discussion
  and relevant Methods read, but no figure pixels, supplementary files or rawdata
  reanalysis. N.bombycis CQ1/KOH/fixed-stage labeling and microscopy support contribution,
  not continuous membrane lineage tracing, an exclusive universal origin, measured
  force, or necessary protein machinery.'
- 'Polaroplast and pusule independent subreview: Pusule Dodge access is genuine publisher
  Summary/subscription preview only; Klut is complete publisher-deposited primary
  abstract only. No fresh full-body/publisher-failure claim or experimental-control
  certification. Proposed functions remain proposed.'
- 'Polaroplast and pusule independent subreview: Gavelis primary ResultsSec2/Par6,
  boundary paragraph, Collection/TEM/FIB-SEM, Fig2 caption and permissions were inspected;
  not whole-paper findings. Figure2 maintained/source pixels actually viewed and identical;
  no other figures, videos, supplements or morphometrics audited. Wild-collected pseudocolonies
  are not an invented laboratory strain.'
- 'Polaroplast and pusule independent subreview: Both records have0protein_examples
  and0GENE_OR_PROTEIN nodes, verified directly and with four native root command receipts.
  An empty native inventory pass is not scientific proof of no proteins or mechanism.'
- 'Polaroplast and pusule independent subreview: Both current whole-record claims
  support genuine structured-source exclusion: physical membrane movement/anatomy
  is not automatically a named molecular pathway; unresolved proteins and proposed
  physiology are not positive molecular assertions. Original stock expression-only
  wording is clarified. Same-PR catalogue independently reread at actual20:43:49.951558Z
  fetch time has no matched host; no foreign queries or absence inference. Historical00:49Z
  runner PermissionError remains historical, no new runner execution claimed.'
- 'Polaroplast and pusule independent subreview: Two additional frozen neighbors used
  only for identity/definition/component/parthood boundary context; no entire-neighbor
  scientific review, disposition or issue resolution. Root owns global QC, issue handling,
  native persistence, CI/queue/merge; this report does not precertify future gates.'
- 'Five plastid compartment records independent subreview: Five complete unchanged
  assigned records independently reviewed. One inherited major whole-thylakoid LIPID
  identity finding remains open with exact predecessor/action; four targets retain
  qualified positive assessments. Four adapter exclusions require correction; physical
  thylakoid lumen exclusion is genuine. No new scientific finding.'
- 'Five plastid compartment records independent subreview: Current native authorities/catalogue/exact
  DOI metadata are fresh. Keeling genuineHTML10:10:38.582642Z, Terashima genuinePDF10:10:38.518294Z
  and Perez genuinepublisherHTML20:02:23.441867Z are retained with original hashes/timestamps
  and independently reread, not represented as new fetches.'
- 'Five plastid compartment records independent subreview: Keeling secondary s1/s3/s6/s9
  and embeddedFigure1–3 captions read. Outdated chromalveolate/universal mitochondrial
  statements, numerical census and underlying studies are not adopted; no pixels.
  Terashima secondary pp151–154 read, no later sections/supplementary lists/pixels;
  enriched wholechloroplast preparations are not purified Chlamydomonas stroma, and
  Arabidopsis fraction data remain distinct.'
- 'Five plastid compartment records independent subreview: Jin2022 current primary
  abstract/species keyword only. Retained publisher1941byteXML coredata is metadata,
  not body. No exact strain, full Methods/atomic model/pixels/deletion-assay interpretation
  certified. Access limitation is not refutation.'
- 'Five plastid compartment records independent subreview: Perez is secondary synthesis,
  not primary experimental evidence. Declared Introduction/evolutionary overview/BuildingBlocks/Lipids/ETC
  and embeddedFigure1/2 captions read; not whole later body, pixels or cited primary
  papers. No exact lipid ratios/universal protein inventory or individual assembly
  necessity inferred.'
- 'Five plastid compartment records independent subreview: Engel primary fresh collaboratingJATS20:43:24.342979Z
  independently read s1,s2-1/s2-2/s2-3,s3-1/s3-2,Methods s4-1 through s4-5 and embedded
  captions; no figure/video pixels, supplements or raw tomography reanalysis. WTCC124(137c),TAP,constantlight/air
  context retained; observed connections do not prove universal continuity or proposed
  transport/biogenesis mechanisms.'
- 'Five plastid compartment records independent subreview: GO0070118 native ancestry
  lacksGO0055035; UniProtSL0356 explicitly supplies plastid-thylakoid-membrane class
  mapping. No nativeGOedge is invented. COMMON/RARE distributions remain qualitative,
  not measured prevalence.'
- 'Five plastid compartment records independent subreview: All five records have zero
  protein_examples and zero typed molecular nodes. Ten native passes certify only
  actual inputs; broad positive narrative protein/pathway claims still need applicability
  assessment. Full20organism/28pair catalogue lacks matched green/glaucophyte hosts;
  no proxy/downstream query. Historical00:49Z runner PermissionError is not a fresh
  invocation.'
- 'Five plastid compartment records independent subreview: Original Perez evidence
  type defect affects three bundles, not scientific-record truth: secondary excerpt
  and failed access were structured as primary_source. New authority/context types
  and source access limits repair the successor assessment without altering historical
  bytes.'
- 'Five plastid compartment records independent subreview: All32 actually used local
  inputs are frozen commonpolicy/config/schema/verifier plus five targets/ten original
  artifacts; no new neighbor scientific disposition. No record/history/generated/Git/GitHub
  edits. Root owns global gates, issues, final persistence/CI/queue/merge; this report
  does not precertify later results.'
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
  and pushed without force. Only polaroplast differs from its original frozen target;
  the other nine target hashes still match.
- This explicit issue-bearing ten-record cohort follows native persistence policy.
  Inherited scientific findings preserve exact repository/review/finding lineage;
  newly observed findings, if any, have no invented predecessors.
- Issue2785 tracks the stale polaroplast review. The current record adds anterior
  lamellar and posterior tubular STRUCTURE nodes joined to existing components, two
  anatomical parthood edges and dated history. Their precise source support is reassessed
  without asserting new molecular machinery or formation necessity.
- 'Issue2786 tracks seven unsupported structured-source exclusions: five explicit
  check rows (outer membrane, stroma, pyrenoid tubule and both recycling records)
  and two prose notes (whole thylakoid and thylakoid membrane). Thylakoid lumen, polaroplast
  and pusule retain justified physical-scope exclusions.'
- Issue2787 tracks three original thylakoid observations, each with three incorrectly
  primary-typed Perez2024 evidence items. Actual secondary-review text and HTTP403
  access-only context remain distinct in the corrected successor; historical access
  times and limits are preserved.
- Source commit55020000323f1344e65128992b35f6ef43c703a2 is retained by tag review-base/pr2376-current-record-followup-20261103.
- CLAUDE.md aliases canonical regular AGENTS.md, whose exact bytes are frozen. All
  used local policy, schema, verifier, original observations, image and requested
  boundary inputs are frozen before assessment.
- All twenty native protein commands passed. There are no represented protein examples
  in this cohort. Recycling endosome has one typed TbRAB11 node with UniProtKB:Q9NJE8;
  the other nine records have zero typed molecular nodes. These scoped checks do not
  certify absence of narrative molecular claims or exhaustive biological inventories.
- Fresh and retained source snapshots preserve actual access times, source tiers and
  bounded inspected sections or pixels. Pusule image bytes, panel scope, caption,
  attribution and licence are assessed separately from physiological transport mechanisms.
- Native CausalNode schema permits families and complexes as GENE_OR_PROTEIN. Missing
  optional examples or unchanged label-only collective material do not automatically
  constitute scientific defects.
- No same-record/finding duplicate was found in all245 open issue bodies or25 bounded
  title/body/comment queries. Existing validator2514 remains reused. No scientific
  record, historical discussion or resolver is edited.
- Final trusted-base post-save review-check, exact-head independent acceptance, final-head
  CI and merge-group CI occur after this immutable observation and are not represented
  as already completed.
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T032956Z-plastid-outer-membrane-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T032957Z-plastid-stroma-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T032958Z-plastid-thylakoid-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T032959Z-plastid-thylakoid-lumen-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T033000Z-plastid-thylakoid-membrane-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T033000Z-polaroplast-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T033001Z-pusule-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T033002Z-pyrenoid-tubule-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T033003Z-recycling-endosome-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T033003Z-recycling-endosome-lumen-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
links:
- https://github.com/CultureBotAI/CellStructureMech/pull/2376
- https://github.com/CultureBotAI/CellStructureMech/issues/2514
- https://github.com/CultureBotAI/CellStructureMech/issues/2785
- https://github.com/CultureBotAI/CellStructureMech/issues/2786
- https://github.com/CultureBotAI/CellStructureMech/issues/2787
- https://github.com/CultureBotAI/CellStructureMech/issues/2788
- https://github.com/CultureBotAI/CellStructureMech/issues/2789
```
