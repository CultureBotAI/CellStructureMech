# PR 2375: current-input review of ten records and adversarial follow-up

- Review: 20261103T201029Z-pr2375-current-record-followup
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-11-03T19:58:46.015890Z
- Finished UTC: 2026-11-03T20:10:29Z
- Reviewer: Codex root synthesis with three independent read-only adversarial reviewers (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Current-input adversarial follow-up for the complete ten-record cohort after merging main. Two stale reviews are refreshed through substantive reassessment of changed chromatophore and thylakoid membrane content, including added graph nodes, groundings and edges. Eight unsupported source-applicability exclusions are corrected, including four prose-only exclusions and four explicit check rows; whole plastid and generic plastid membrane retain genuine physical/material-topology exclusions. Inherited findings retain exact predecessor identities. All original observations and scientific records remain unchanged. Ten inherited scientific findings remain open (six major and four minor) across seven targets; three other targets retain qualified positive assessments. Separate curation issues preserve exact predecessor lineage.

## Scope And Provenance

Exact ten-record PR cohort reassessed against current main 2b971e43fc3fad85009d3cd036695b33f0fcaf5c. Changed inputs are substantively reassessed. Scientific records remain unchanged.

Selection: Complete cohort of ten maintained records reviewed in original PR head 048dab0c30cba35f96656b45bac93d33d19a1908.
Coverage: full; 10 reviewed / 10 in the declared population.
Source: working_tree at Git base 659d5d9ce7e16c8607002bf1655db2f3c652e6e1.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0106174 | data/structures/membrane_organelle/phagolysosome_vesicle_lumen.yaml | maintained | phagolysosome vesicle lumen |
| GO:0034357 | data/structures/membrane_organelle/photosynthetic_membrane.yaml | maintained | photosynthetic membrane |
| GO:0042717 | data/structures/membrane_organelle/plasma_membrane_derived_chromatophore_membrane.yaml | maintained | plasma membrane-derived chromatophore membrane |
| GO:0031979 | data/structures/membrane_organelle/plasma_membrane_derived_thylakoid_lumen.yaml | maintained | plasma membrane-derived thylakoid lumen |
| GO:0031676 | data/structures/membrane_organelle/plasma_membrane_derived_thylakoid_membrane.yaml | maintained | plasma membrane-derived thylakoid membrane |
| GO:0009536 | data/structures/membrane_organelle/plastid.yaml | maintained | plastid |
| GO:0009526 | data/structures/membrane_organelle/plastid_envelope.yaml | maintained | plastid envelope |
| GO:0009528 | data/structures/membrane_organelle/plastid_inner_membrane.yaml | maintained | plastid inner membrane |
| GO:0009529 | data/structures/membrane_organelle/plastid_intermembrane_space.yaml | maintained | plastid intermembrane space |
| GO:0042170 | data/structures/membrane_organelle/plastid_membrane.yaml | maintained | plastid membrane |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full native QC | passed | True | GO:0106174, GO:0034357, GO:0042717, GO:0031979, GO:0031676, GO:0009536, GO:0009526, GO:0009528, GO:0009529, GO:0042170 | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| Native label correspondence | passed | True | GO:0106174, GO:0034357, GO:0042717, GO:0031979, GO:0031676, GO:0009536, GO:0009526, GO:0009528, GO:0009529, GO:0042170 | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| TraitMech references | passed | True | GO:0106174, GO:0034357, GO:0042717, GO:0031979, GO:0031676, GO:0009536, GO:0009526, GO:0009528, GO:0009529, GO:0042170 | Native TraitMech link check passed. |
| Pinned governed files | passed | True | GO:0106174, GO:0034357, GO:0042717, GO:0031979, GO:0031676, GO:0009536, GO:0009526, GO:0009528, GO:0009529, GO:0042170 | Pinned governed files match; native vendored check passed. |
| Native identifier resolver | passed | True | GO:0106174, GO:0034357, GO:0042717, GO:0031979, GO:0031676, GO:0009536, GO:0009526, GO:0009528, GO:0009529, GO:0042170 | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| validate GO:0106174 | passed | True | GO:0106174 | Documented focused command passed. |
| validate-strict GO:0106174 | passed | True | GO:0106174 | Documented focused command passed. |
| validate GO:0034357 | passed | True | GO:0034357 | Documented focused command passed. |
| validate-strict GO:0034357 | passed | True | GO:0034357 | Documented focused command passed. |
| validate GO:0042717 | passed | True | GO:0042717 | Documented focused command passed. |
| validate-strict GO:0042717 | passed | True | GO:0042717 | Documented focused command passed. |
| validate GO:0031979 | passed | True | GO:0031979 | Documented focused command passed. |
| validate-strict GO:0031979 | passed | True | GO:0031979 | Documented focused command passed. |
| validate GO:0031676 | passed | True | GO:0031676 | Documented focused command passed. |
| validate-strict GO:0031676 | passed | True | GO:0031676 | Documented focused command passed. |
| validate GO:0009536 | passed | True | GO:0009536 | Documented focused command passed. |
| validate-strict GO:0009536 | passed | True | GO:0009536 | Documented focused command passed. |
| validate GO:0009526 | passed | True | GO:0009526 | Documented focused command passed. |
| validate-strict GO:0009526 | passed | True | GO:0009526 | Documented focused command passed. |
| validate GO:0009528 | passed | True | GO:0009528 | Documented focused command passed. |
| validate-strict GO:0009528 | passed | True | GO:0009528 | Documented focused command passed. |
| validate GO:0009529 | passed | True | GO:0009529 | Documented focused command passed. |
| validate-strict GO:0009529 | passed | True | GO:0009529 | Documented focused command passed. |
| validate GO:0042170 | passed | True | GO:0042170 | Documented focused command passed. |
| validate-strict GO:0042170 | passed | True | GO:0042170 | Documented focused command passed. |
| Supplemental bounded PMID authority checks | passed | True | GO:0106174, GO:0034357, GO:0042717, GO:0031979, GO:0031676, GO:0009536, GO:0009526, GO:0009528, GO:0009529, GO:0042170 | 909 PMIDs all OK in bounded native requests; full-command limitations remain separate. |
| Official structured-source applicability and covered-dataset cross-checks | passed | False | GO:0106174, GO:0034357, GO:0042717, GO:0031979, GO:0031676, GO:0009536, GO:0009526, GO:0009528, GO:0009529, GO:0042170 | Eight records assert positive molecular/pathway claims: phagolysosome lumen, photosynthetic membrane, bacterial chromatophore membrane, two bacterial thylakoid compartments, plastid envelope, inner membrane and intermembrane space. Four unsupported prose-only exclusions and four unsupported explicit check rows are corrected with actual host/strain catalogue coverage and applicable downstream checks. Whole plastid and generic plastid membrane retain genuine physical/material-topology exclusions. A study-model mention alone is not an asserted protein inventory. Noncoverage is not biological absence; unrelated organisms are not proxies. Historical runner unavailability stays historical with actual public-source fallback scopes and timestamps. |
| Independent claim-level source review | passed | True | GO:0106174, GO:0034357, GO:0042717, GO:0031979, GO:0031676, GO:0009536, GO:0009526, GO:0009528, GO:0009529, GO:0042170 | Three read-only reviewers covered the complete ten-record cohort, including changed inputs, with explicit scientific findings and source-access limits. Final artifact/head acceptance occurs after saving. |
| Retained historical adapter runner availability | unavailable | False | GO:0106174, GO:0034357, GO:0042717, GO:0031979, GO:0031676, GO:0009536, GO:0009526, GO:0009528, GO:0009529, GO:0042170 | Historical00:49Z invocation unavailable due to OS access restriction. Official catalogue fallback was inspected separately; no fresh invocation is claimed. Actual historical exit1 is retained in the evidence receipt; the native unavailable-check model has no execution exit-code field. |
| Native phagolysosome vesicle lumen UniProt verify check | passed | True | GO:0106174 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native phagolysosome vesicle lumen UniProt causal check | passed | True | GO:0106174 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native photosynthetic membrane UniProt verify check | passed | True | GO:0034357 | 8 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native photosynthetic membrane UniProt causal check | passed | True | GO:0034357 | 8 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native plasma membrane-derived chromatophore membrane UniProt verify check | passed | True | GO:0042717 | 6 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native plasma membrane-derived chromatophore membrane UniProt causal check | passed | True | GO:0042717 | 6 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native plasma membrane-derived thylakoid lumen UniProt verify check | passed | True | GO:0031979 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native plasma membrane-derived thylakoid lumen UniProt causal check | passed | True | GO:0031979 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native plasma membrane-derived thylakoid membrane UniProt verify check | passed | True | GO:0031676 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native plasma membrane-derived thylakoid membrane UniProt causal check | passed | True | GO:0031676 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native plastid UniProt verify check | passed | True | GO:0009536 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native plastid UniProt causal check | passed | True | GO:0009536 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native plastid envelope UniProt verify check | passed | True | GO:0009526 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native plastid envelope UniProt causal check | passed | True | GO:0009526 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native plastid inner membrane UniProt verify check | passed | True | GO:0009528 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native plastid inner membrane UniProt causal check | passed | True | GO:0009528 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native plastid intermembrane space UniProt verify check | passed | True | GO:0009529 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native plastid intermembrane space UniProt causal check | passed | True | GO:0009529 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native plastid membrane UniProt verify check | passed | True | GO:0042170 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native plastid membrane UniProt causal check | passed | True | GO:0042170 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |

## Scientific And Domain Assessments

### Original native validation/render and frozen input

schema: supported. Targets: GO:0106174.

Actual original native validation/render pass with exact Markdown. Historical frozen target hash verified. Current target is byte-identical to its original frozen input.

### Exact identity, synonym and structural boundary

identity: supported. Targets: GO:0106174.

GO0106174 volume, GO0097013 parent and GO0032010 parthood remain exact. Ordinary phagolysosome-lumen wording is compatible even if not a current GO exact-synonym string; SL0342 supplies broader lumen context only.

### Definition source and expanded biological scope

scope: concern. Targets: GO:0106174.

Inherited major F1 persists: exact ontology volume clause is followed by cross-taxon enzyme/ROS/microbial-killing program not supplied by GO or established in full by the Ax2 source. This does not refute any individual mechanism or require replacing the correct identity.

### Actual source organism, strain and occurrence

scope: supported. Targets: GO:0106174.

D. discoideum/Ax2 is the actual primary host. COMMON is qualitative model-system occurrence and does not certify all strains/taxa/stages. Added Entamoeba/ciliate generalization is addressed by F1.

### Constituent/material scope

grounding: supported. Targets: GO:0106174.

No component inventory is asserted for this lumen; enclosing membrane remains a separate STRUCTURE. Variable luminal cargo or proton-gradient function is not a mandatory stable protein inventory.

### Direct experimental result versus context

evidence: concern. Targets: GO:0106174.

Inherited minor F3 persists: source directly dissects trafficking/composition, while acidification is discussed from prior work. Current canonical/function notes blur that distinction; retain qualitative maturation while qualifying assay attribution.

### Biological function and necessity

evidence: concern. Targets: GO:0106174.

GO0090383 acidification association is biologically coherent but does not make the2002 source a direct pH experiment. Full cross-taxon digestive-program support remains bounded by F1/F3.

### Graph scope and complete edge inventory

graph: concern. Targets: GO:0106174.

Inherited minor F2 persists: MECHANISTIC/assembly-functional-mechanism wording exceeds two actual descriptive edges, lumen parthood and whole-volume association with acidification. No explanatory proton transport transition is represented.

### Actual native coverage versus molecular completeness

provenance: supported. Targets: GO:0106174.

Actual two native commands pass. Independent count is0 examples,0 typed molecular nodes,0 UniProtKB graph xrefs. This empty inventory does not erase the positive narrative pathway scope.

### Whole-record structured-source applicability

scope: supported. Targets: GO:0106174.

Positive acidification and digestive molecular narrative trigger policy. Fresh complete catalogue lacks the actual Dictyostelium/Ax2 and other named host groups; use scoped primary/authority fallback, not prey or another host. Historical00:49Z unavailable runner is separate from these completed fresh HTTP/source checks.

### Append-only provenance and boundary contexts

provenance: supported. Targets: GO:0106174.

PROPOSED state and dated history/discussion remain unchanged. Historical resolved topology/material discussions are not rewritten as current inventories. Bounded frozen neighbor anatomy does not dispose another record or grouped issue. 

### Unresolved formation/assembly detail

completeness: unknown. Targets: GO:0106174.

Source anatomy and measured trafficking/localization do not establish exhaustive formation machinery, invariant molecular composition or individual necessary subunits across taxa. Optional protein examples are not mandatory solely because sources identify proteins.

### Absent image/measurement/protein domains

scope: not_applicable. Targets: GO:0106174.

No maintained image/license claim, individual protein accession, quantitative measurement, associated-trait mapping or verbatim snippet occurs in these three records. Source text captions were read without image pixels/raw datasets/supplements. Those unseen domains are not certified.

### Current scientific verdict and exact lineage

completeness: concern. Targets: GO:0106174.

needs_curation: inherited F1 major definition scope plus F2/F3 minor graph/acidification attribution remain open. No new scientific finding; maintained-record fixes stay outside this review-only PR. Original exact keys, severity normalization and predecessor references are preserved.

### Original native validation/render and frozen input

schema: supported. Targets: GO:0031979.

Actual original native validation/render pass with exact Markdown. Historical frozen target hash verified. Current target is byte-identical to its original frozen input.

### Exact identity, synonym and structural boundary

identity: supported. Targets: GO:0031979.

GO0031979 and SL0044 identify the enclosed cellular thylakoid lumen with GO0030075 parthood. Boundary membrane is a separate structure. GO non-organelle commentary and qualified lack of obligatory continuity are retained.

### Definition source and expanded biological scope

scope: supported. Targets: GO:0031979.

Definition remains topological rather than a fixed cross-taxon protein inventory. Plasma-membrane-derived terminology does not require a continuing physical bridge; actual7942 cryoET reports no apparent direct connection.

### Actual source organism, strain and occurrence

scope: concern. Targets: GO:0031979.

Inherited major F1 persists: current canonical example attributes Huokko2021 to Synechocystis6803, but Methods/Results specify Synechococcus elongatus7942. The explicit Huokko evidence note also repeats the incorrect host. PCC6803 presence itself is not refuted. Cyanobacteriota COMMON with Gloeobacter exception is qualitative, not a census.

### Constituent/material scope

grounding: supported. Targets: GO:0031979.

No component inventory is asserted for this lumen; enclosing membrane remains a separate STRUCTURE. Variable luminal cargo or proton-gradient function is not a mandatory stable protein inventory.

### Direct experimental result versus context

evidence: supported. Targets: GO:0031979.

Casella uses native7942 thylakoid preparations and functional fluorescent tags; AFM b6f shape assignment is tentative and distinct from tagged localization. Huokko uses HL-to-LL recovery and cryoET in7942; no direct membrane continuity is assumed. Perez is secondary synthesis, not a new primary assay.

### Biological function and necessity

evidence: supported. Targets: GO:0031979.

Positive trans-thylakoid proton-gradient narrative is supported by the inspected secondary review; the lumen graph intentionally remains descriptive anatomy rather than a complete proton-transport mechanism.

### Graph scope and complete edge inventory

graph: supported. Targets: GO:0031979.

NONMECHANISTIC graph has2 anatomical edges: lumen parthood and membrane boundary. It does not promise an omitted molecular causal sequence.

### Actual native coverage versus molecular completeness

provenance: supported. Targets: GO:0031979.

Actual two native commands pass. Independent count is0 examples,0 typed molecular nodes,0 UniProtKB graph xrefs. This empty inventory does not erase the positive narrative pathway scope.

### Whole-record structured-source applicability

scope: supported. Targets: GO:0031979.

Positive photochemistry/proton-gradient and complex/pathway assertions trigger policy. Fresh catalogue and bounded s_elongatus/elprecise300 gene/module checks cover actual cited7942 experiments and broad cyanobacterial context. They do not substitute for unmatched6803 or repair its source attribution. psaA/petB pass module38 thresholds; psbA1/atpA all-false flags do not establish biological absence. Historical00:49Z unavailable runner is separate from these completed fresh HTTP/source checks.

### Append-only provenance and boundary contexts

provenance: supported. Targets: GO:0031979.

PROPOSED state and dated history/discussion remain unchanged. Historical resolved topology/material discussions are not rewritten as current inventories. Bounded frozen neighbor anatomy does not dispose another record or grouped issue. 

### Unresolved formation/assembly detail

completeness: unknown. Targets: GO:0031979.

Source anatomy, measured trafficking/localization and secondary photochemical synthesis do not establish exhaustive formation machinery, invariant molecular composition or individual necessary subunits across taxa. Optional protein examples are not mandatory solely because sources identify proteins.

### Absent image/measurement/protein domains

scope: not_applicable. Targets: GO:0031979.

No maintained image/license claim, individual protein accession, quantitative measurement, associated-trait mapping or verbatim snippet occurs in these three records. Source text captions were read without image pixels/raw datasets/supplements. Those unseen domains are not certified.

### Current scientific verdict and exact lineage

completeness: concern. Targets: GO:0031979.

needs_curation: inherited major F1 experimental-organism attribution remains open. No new scientific finding; maintained-record fixes stay outside this review-only PR. Original exact keys, severity normalization and predecessor references are preserved.

### Original native validation/render and frozen input

schema: supported. Targets: GO:0031676.

Actual original native validation/render pass with exact Markdown. Historical frozen target hash verified. Current membrane input is stale and is substantively refreshed against primary and secondary sources; historical evidence is not reauthored.

### Exact identity, synonym and structural boundary

identity: supported. Targets: GO:0031676.

GO0031676 and SL0045 identify cellular thylakoid membrane, with GO0042651 is-a and GO0030075 parthood. Whole-thylakoid ontology part assertions are not falsely stated as direct membrane axioms; primary residence evidence supports the membrane representation.

### Definition source and expanded biological scope

scope: supported. Targets: GO:0031676.

Definition remains topological rather than a fixed cross-taxon protein inventory. Plasma-membrane-derived terminology does not require a continuing physical bridge; actual7942 cryoET reports no apparent direct connection.

### Actual source organism, strain and occurrence

scope: concern. Targets: GO:0031676.

Inherited major F1 persists: current canonical example attributes Huokko2021 to Synechocystis6803, but Methods/Results specify Synechococcus elongatus7942. Casella2017 mapping/FRAP notes in the PSI component and graph likewise misattribute the host. PCC6803 presence itself is not refuted. Cyanobacteriota COMMON with Gloeobacter exception is qualitative, not a census.

### Constituent/material scope

grounding: supported. Targets: GO:0031676.

Collective label-only lipid matrix denotes constitutive bilayer material, not a guessed chemical species or a whole-membrane GO substituted as chemical identity. Four GO-grounded complexes are distinct physical assemblies; UNKNOWN formation necessity is retained. No exact lipid percentage is imported from a review.

### Direct experimental result versus context

evidence: supported. Targets: GO:0031676.

Casella uses native7942 thylakoid preparations and functional fluorescent tags; AFM b6f shape assignment is tentative and distinct from tagged localization. Huokko uses HL-to-LL recovery and cryoET in7942; no direct membrane continuity is assumed. Perez is secondary synthesis, not a new primary assay.

### Biological function and necessity

evidence: supported. Targets: GO:0031676.

PSII, b6f and PSI electron transport and proton-gradient-driven ATP synthesis are supported at complex/pathway level. Individual subunit necessity, invariant stoichiometry and universal membrane composition are not demonstrated here.

### Graph scope and complete edge inventory

graph: supported. Targets: GO:0031676.

Current NONMECHANISTIC graph has6 descriptive edges: boundary, PSII/b6f/PSI residence, electron-transport association and newly added ATP-synthase residence. The old frozen graph had5 and lacked the ATP edge, despite the original review saying it was already there.

### Actual native coverage versus molecular completeness

provenance: supported. Targets: GO:0031676.

Actual two native commands pass. Independent count is0 examples,0 typed molecular nodes,0 UniProtKB graph xrefs. Existing GO protein-complex components and STRUCTURE nodes remain valid; no automatic enum or mandatory representative finding is invented.

### Whole-record structured-source applicability

scope: supported. Targets: GO:0031676.

Positive photochemistry/proton-gradient and complex/pathway assertions trigger policy. Fresh catalogue and bounded s_elongatus/elprecise300 gene/module checks cover actual cited7942 experiments and broad cyanobacterial context. They do not substitute for unmatched6803 or repair its source attribution. psaA/petB pass module38 thresholds; psbA1/atpA all-false flags do not establish biological absence. Historical00:49Z unavailable runner is separate from these completed fresh HTTP/source checks.

### Append-only provenance and boundary contexts

provenance: supported. Targets: GO:0031676.

PROPOSED state and dated history/discussion remain unchanged. Historical resolved topology/material discussions are not rewritten as current inventories. Bounded frozen neighbor anatomy does not dispose another record or grouped issue. Added ATP-edge history is current-source context; no claim that old review had actually inspected it.

### Unresolved formation/assembly detail

completeness: unknown. Targets: GO:0031676.

Source anatomy, measured trafficking/localization and secondary photochemical synthesis do not establish exhaustive formation machinery, invariant molecular composition or individual necessary subunits across taxa. Optional protein examples are not mandatory solely because sources identify proteins.

### Absent image/measurement/protein domains

scope: not_applicable. Targets: GO:0031676.

No maintained image/license claim, individual protein accession, quantitative measurement, associated-trait mapping or verbatim snippet occurs in these three records. Source text captions were read without image pixels/raw datasets/supplements. Those unseen domains are not certified.

### Current scientific verdict and exact lineage

completeness: concern. Targets: GO:0031676.

needs_curation: inherited major F1 experimental-organism attribution remains open. No new scientific finding; maintained-record fixes stay outside this review-only PR. Original exact keys, severity normalization and predecessor references are preserved.

### Historical originals and current represented molecular coverage

schema: supported. Targets: GO:0034357.

Both original pairs validate/render exactly with20 historical inputs each. Current native examples/node counts are separately bound; original graph coverage does not certify later changes. Root owns current corpus/publication gates.

### Historical originals and current represented molecular coverage

schema: supported. Targets: GO:0042717.

Both original pairs validate/render exactly with20 historical inputs each. Current native examples/node counts are separately bound; original graph coverage does not certify later changes. Root owns current corpus/publication gates.

### Generic photosynthetic membrane boundary

identity: supported. Targets: GO:0034357.

GO0034357 exactly matches broad photosynthetic membrane and membrane parent. Oxygenic and purple-bacterial subclasses coexist; broad reaction-center/carrier classes are not one exact narrow protein family.

### Declared lipid, pigment and protein classes

grounding: supported. Targets: GO:0034357.

Collective lipid matrix is label-only without whole-membrane chemical misgrounding. Broad pigments/carriers and reaction-center or cytochrome classes are explicitly heterogeneous. Component examples do not define exhaustive stoichiometry or identical incorporation across lineages.

### Constitutional classes versus individual assembly requirements

evidence: unknown. Targets: GO:0034357.

Bilayer and broad photochemical classes are constitutional to this generic structure. Specific gene/protein/pigment depletion requirements do not follow from mature localization or activity; UNKNOWN specific-complex necessity remains appropriate.

### Eight reviewed examples and exact taxa

grounding: supported. Targets: GO:0034357.

PsaA/PSII D1, PufL/M, cytochromef/b6 andpurplepetB/fbcB,petC/fbcC identities agree. P16033 includes psbA2 andpsbA3; tax1111708 is Kazusa, separate fromsourcePCC7942. Annotation evidence codes and abstract-only experimental cross-checks retain limits.

### Qualitative distribution and actual canonical hosts

scope: concern. Targets: GO:0034357.

Perez secondaryIntroduction supports widespread cyanobacterial thylakoids withGloeobacter exception; broadBacteria prevalence is qualitative, not a census. Casella source isPCC7942, whereas canonicalexample0/onegraphsource note namePCC6803. Independent PCC6803 protein examples remain valid.

### Seven descriptive photochemistry edges

graph: supported. Targets: GO:0034357.

Current seven NONMECHANISTIC edges summarize pigment binding/excitation, residence, carrier andcytochrome routing, PMF andelectron transport. They are illustrative oxygenic/purple contexts, not one universally conserved stoichiometric mechanism. Casella source attribution remains a separate finding.

### Oxygenic process scope

grounding: concern. Targets: GO:0034357.

GO0019684 defines oxygenic PSI/PSII wateroxidation/NADPreduction; current broad description also cites purple architecture without oxygenic-subset qualification. Retain broadGO0009767context and delimit this narrower function rather than excluding valid anoxygenic membranes.

### Integral versus peripheral antenna and optional inventory

scope: supported. Targets: GO:0034357.

Bahatyrova supports integral LH2; Sui secondaryabstract and Nielsen primaryabstract give bounded peripheral antenna/baseplate context. Open discussion appropriately avoids projecting every antenna as an integral membrane part. Optional complete subtype inventory or generic ATPase enrichment is not automatically mandatory.

### Positive molecular/pathway claims and matched source organism

evidence: supported. Targets: GO:0034357.

Whole record asserts genes, proteins and photochemical pathways, so expression-only narrative exclusion is invalid. Fresh catalogue permits bounded PCC7942 source-context checks; selectedgene/module results agree with pathway context. No dataset is substituted for canonicalPCC6803 or purplehosts.

### Purple bacterial membrane versus organellar chromatophore

identity: supported. Targets: GO:0042717.

GO0042717/SL0042 are exact purple-bacterial plasma-derived membrane; GO0070112 is separate organellar membrane. Generic photosynthetic parent and related broad chromatophore synonym preserve that boundary.

### Existing whole-complex constituents and exact groundings

grounding: concern. Targets: GO:0042717.

RC-LH1-PufX andbc1 local identities match current grounded components/nodes. Existing LH2 andF0F1 remain label-only despite exact maintainedLH2 andactiveGO0045259F1-F0 identity; this inherited bounded mapping defect is not an optional new inventory demand.

### Specific complex formation requirements

evidence: unknown. Targets: GO:0042717.

The bilayer is constitutional; every listed specific complex remains UNKNOWN for formation necessity. AFM architecture, photochemical activity, inferred annotations and isolated-vesicle coupling do not establish each complex is indispensable for building all chromatophores.

### Six reviewed examples with strain-specific identity

grounding: supported. Targets: GO:0042717.

LH2pucA/B andATPaseatpA/B/D/E examples match reviewed identities and exacttaxa. atpD usesATCC17025 whereasatpA/B/E use2.4.1; individual examples are not represented as one experimentally measured complete complex in one strain. Native graph count is nowzero typedmolecular nodes.

### Source strains and bounded prevalence

scope: supported. Targets: GO:0042717.

BahatyrovaNCIB8253, ComayrasGa andFenioukR.capsulatusB10 are separate contexts. They support illustrative purple-bacterial architecture/coupling, not universalc2 use, invariantdimer geometry or quantifiedBacteria prevalence.

### Substantive refresh of two added edges

graph: supported. Targets: GO:0042717.

Eight current NONMECHANISTIC edges include newbc1→PMF andRC-LH1-PufX→membrane. Feniouk supports bc1-associated voltage contribution/coupling andBahatyrova actualRC/LH2 membrane residence. Comayras inhibited-pool assay is not unperturbed PMF measurement. No unsupported universal mechanism or necessity is added.

### Substantive current-input refresh without category-wide disposition

provenance: supported. Targets: GO:0042717.

Current addedlocalRC/bc1groundings andSTRUCTURE retypings are coherent, but do not resolve independentLH2/F0F1 constituent mapping. Original20inputhashes remain historical. Current eightedges/sixexamples/zero typednodes replace old sixedge/typednode account. No disposition of all#2432 category records is inferred.

### Applicability assessed before actual purple-host noncoverage

evidence: supported. Targets: GO:0042717.

NamedLH2/ATPasegenes andcyclic photophosphorylation trigger required source assessment even without expression-module claims. Complete current catalogue has noCereibacter/Rhodobacter matching host. PCC7942 results are not a purple-host proxy; no unmatched downstreamquery or negativebiology inferred.

### Complete current scope without optional enrichment

completeness: supported. Targets: GO:0034357.

Every current field and graph/source placement assessed; no maintained image, direct quotation or quantitative physical-property claim requires pixel/measurement validation. No newprotein/chemical inventory mandated. Historical rationale remains append-only; curation actions stay separate from review refresh.

### Complete current scope without optional enrichment

completeness: supported. Targets: GO:0042717.

Every current field and graph/source placement assessed; no maintained image, direct quotation or quantitative physical-property claim requires pixel/measurement validation. No newprotein/chemical inventory mandated. Historical rationale remains append-only; curation actions stay separate from review refresh.

### Exact identity and hierarchy

identity: supported. Targets: GO:0009536.

ExactGO9536 broad cytoplasmic organelle with GO43231 parent, cytoplasm parthood andSL0209 mapping. No universal photosynthesis or fixed membrane count asserted.

### Anatomical component identity versus chemical material

grounding: concern. Targets: GO:0009536.

Inherited major F1 confirmed: LIPID rows ground complete GO membrane structures; component_ref inherits mismatch. Keep valid structural nodes/parts and use accurate structural or label-only material representation.

### Individual formation necessity

evidence: unknown. Targets: GO:0009536.

UNKNOWN on whole/envelope retained; ESSENTIAL on inner/generic bilayer denotes defining collective material only. Neither anatomy nor TOC–TIC cryoEM observation establishes individual lipid/protein necessity for formation. IMS has no such constituent requirement.

### Every descriptive edge and source scope

graph: supported. Targets: GO:0009536.

Three NONMECHANISTIC relations: plastid in cytoplasm, membrane boundary, stroma contained. Membrane node remains correct despite F1 component join mismatch.

### Qualitative occurrence and lineage bounds

scope: supported. Targets: GO:0009536.

Current2759/33090/3055 identities verified. Keeling s1/s3/s6 supports green-primary and scattered secondary/reduced contexts; RARE/COMMON are qualitative, not measured frequencies or all-isolate claims. Historical phylogenetic models are not presented as current complete consensus.

### Exact canonical example and experimental extent

evidence: supported. Targets: GO:0009536.

Terashima secondary abstract and retained pp151–152 support a C.reinhardtii chloroplast used for proteome/protein-biogenesis research. The record does not claim a specific protein cohort, experimental membrane-only proteome or detailed pathway merely by naming the model.

### Whole-record structured-source applicability

evidence: not_applicable. Targets: GO:0009536.

Genuine physical/material/class scope: canonical model use for proteome/protein-biogenesis studies is research context, not a positive specified molecular cohort/pathway. Graph/discussion withhold specialized machinery. Background source biology is not imported as a record assertion; no mandatory dataset query defect.

### Historical boundary decisions and grounding discussions

provenance: supported. Targets: GO:0009536.

Original observations and current PROPOSED status remain unchanged; no closed historical or neighbor issue/category resolved. Source-neutral chemical TODOs remain valid; label-only constituents and append-only rationale do not require fabricated corrections.

### Frozen inputs/native original pairs/current coverage

schema: supported. Targets: GO:0009536.

All75 old frozen hashes verify; five original YAML/Markdown pairs validate/render exactly. Own target unchanged. Ten actual native protein commands pass with zero examples/typed nodes; positive narrative machinery still needs applicability assessment.

### Complete record and bounded verdict

completeness: supported. Targets: GO:0009536.

Full current record reviewed: no maintained images, verbatim snippets, quantitative physical properties or individual protein accessions require extra claims. Exact inherited major finding/action retained; no new scientific finding.

### Exact identity and hierarchy

identity: supported. Targets: GO:0009526.

ExactGO9526 double envelope including IMS, organelle-envelope parent/plastid parthood andSL0210 synonym. Scope is primary double envelope distinct from extra surrounding complex-plastid membranes.

### Anatomical component identity versus chemical material

grounding: concern. Targets: GO:0009526.

Inherited major F2 confirmed: LIPID rows ground complete GO membrane structures; component_ref inherits mismatch. Keep valid structural nodes/parts and use accurate structural or label-only material representation.

### Individual formation necessity

evidence: unknown. Targets: GO:0009526.

UNKNOWN on whole/envelope retained; ESSENTIAL on inner/generic bilayer denotes defining collective material only. Neither anatomy nor TOC–TIC cryoEM observation establishes individual lipid/protein necessity for formation. IMS has no such constituent requirement.

### Every descriptive edge and source scope

graph: supported. Targets: GO:0009526.

Five NONMECHANISTIC edges: envelope encloses plastid, outer/inner part_of envelope, envelope containsIMS, inner boundsstroma. True topology retained independently from F1 typed-component mismatch.

### Qualitative occurrence and lineage bounds

scope: supported. Targets: GO:0009526.

Current2759/33090/3055 identities verified. Keeling s1/s3/s6 supports green-primary and scattered secondary/reduced contexts; RARE/COMMON are qualitative, not measured frequencies or all-isolate claims. Historical phylogenetic models are not presented as current complete consensus.

### Exact canonical example and experimental extent

evidence: supported. Targets: GO:0009526.

Jin primary abstract+indexed species keyword supports C.reinhardtii TOC–TIC bridge/IMS or Tic-side context. No full Methods, strain, raw structure/pixels or individual formation necessity certified.

### Whole-record structured-source applicability

evidence: concern. Targets: GO:0009526.

Original expression-only exclusion is unsupported: taxonomy/canonical prose positively asserts TOC–TIC import supercomplex at this boundary. Fresh official catalogue lacks matching Chlamydomonas host; no proxy/downstream unmatched query.

### Historical boundary decisions and grounding discussions

provenance: supported. Targets: GO:0009526.

Original observations and current PROPOSED status remain unchanged; no closed historical or neighbor issue/category resolved. Source-neutral chemical TODOs remain valid; label-only constituents and append-only rationale do not require fabricated corrections.

### Frozen inputs/native original pairs/current coverage

schema: supported. Targets: GO:0009526.

All75 old frozen hashes verify; five original YAML/Markdown pairs validate/render exactly. Own target unchanged. Ten actual native protein commands pass with zero examples/typed nodes; positive narrative machinery still needs applicability assessment.

### Complete record and bounded verdict

completeness: supported. Targets: GO:0009526.

Full current record reviewed: no maintained images, verbatim snippets, quantitative physical properties or individual protein accessions require extra claims. Exact inherited major finding/action retained; no new scientific finding.

### Exact identity and hierarchy

identity: supported. Targets: GO:0009528.

ExactGO9528 stroma-facing bilayer, generic membrane parent/envelope part and threeSL0211 synonyms; IMS remains distinct.

### Anatomical component identity versus chemical material

grounding: supported. Targets: GO:0009528.

Reviewed-label-only collective bilayer material has no erroneous whole-membrane chemical grounding. Defining collective material remains distinct from exact lipid species.

### Individual formation necessity

evidence: unknown. Targets: GO:0009528.

UNKNOWN on whole/envelope retained; ESSENTIAL on inner/generic bilayer denotes defining collective material only. Neither anatomy nor TOC–TIC cryoEM observation establishes individual lipid/protein necessity for formation. IMS has no such constituent requirement.

### Every descriptive edge and source scope

graph: supported. Targets: GO:0009528.

Three NONMECHANISTIC edges correctly state envelope parthood, stroma boundary andIMS delimitation; no universal translocon inventory asserted.

### Qualitative occurrence and lineage bounds

scope: supported. Targets: GO:0009528.

Current2759/33090/3055 identities verified. Keeling s1/s3/s6 supports green-primary and scattered secondary/reduced contexts; RARE/COMMON are qualitative, not measured frequencies or all-isolate claims. Historical phylogenetic models are not presented as current complete consensus.

### Exact canonical example and experimental extent

evidence: supported. Targets: GO:0009528.

Jin primary abstract+indexed species keyword supports C.reinhardtii TOC–TIC bridge/IMS or Tic-side context. No full Methods, strain, raw structure/pixels or individual formation necessity certified.

### Whole-record structured-source applicability

evidence: concern. Targets: GO:0009528.

Original expression-only exclusion is unsupported: taxonomy/canonical prose positively asserts TOC–TIC import supercomplex at this boundary. Fresh official catalogue lacks matching Chlamydomonas host; no proxy/downstream unmatched query.

### Historical boundary decisions and grounding discussions

provenance: supported. Targets: GO:0009528.

Original observations and current PROPOSED status remain unchanged; no closed historical or neighbor issue/category resolved. Source-neutral chemical TODOs remain valid; label-only constituents and append-only rationale do not require fabricated corrections.

### Frozen inputs/native original pairs/current coverage

schema: supported. Targets: GO:0009528.

All75 old frozen hashes verify; five original YAML/Markdown pairs validate/render exactly. Own target unchanged. Ten actual native protein commands pass with zero examples/typed nodes; positive narrative machinery still needs applicability assessment.

### Complete record and bounded verdict

completeness: supported. Targets: GO:0009528.

Full current record reviewed: no maintained images, verbatim snippets, quantitative physical properties or individual protein accessions require extra claims. No supported scientific finding; qualified pass preserves molecular/experimental/access limits.

### Exact identity and hierarchy

identity: supported. Targets: GO:0009529.

ExactGO9529 between-bilayer region withSL0212 synonym/envelope parthood; neither stroma nor membrane.

### Anatomical component identity versus chemical material

grounding: supported. Targets: GO:0009529.

No components on the spatial IMS record; no invented molecular inventory.

### Individual formation necessity

evidence: unknown. Targets: GO:0009529.

UNKNOWN on whole/envelope retained; ESSENTIAL on inner/generic bilayer denotes defining collective material only. Neither anatomy nor TOC–TIC cryoEM observation establishes individual lipid/protein necessity for formation. IMS has no such constituent requirement.

### Every descriptive edge and source scope

graph: supported. Targets: GO:0009529.

Three NONMECHANISTIC edges correctly state envelope parthood and two bilayer boundaries; positive speciesTOC–TIC example separately bounded.

### Qualitative occurrence and lineage bounds

scope: supported. Targets: GO:0009529.

Current2759/33090/3055 identities verified. Keeling s1/s3/s6 supports green-primary and scattered secondary/reduced contexts; RARE/COMMON are qualitative, not measured frequencies or all-isolate claims. Historical phylogenetic models are not presented as current complete consensus.

### Exact canonical example and experimental extent

evidence: supported. Targets: GO:0009529.

Jin primary abstract+indexed species keyword supports C.reinhardtii TOC–TIC bridge/IMS or Tic-side context. No full Methods, strain, raw structure/pixels or individual formation necessity certified.

### Whole-record structured-source applicability

evidence: concern. Targets: GO:0009529.

Original expression-only exclusion is unsupported: taxonomy/canonical prose positively asserts TOC–TIC import supercomplex at this boundary. Fresh official catalogue lacks matching Chlamydomonas host; no proxy/downstream unmatched query.

### Historical boundary decisions and grounding discussions

provenance: supported. Targets: GO:0009529.

Original observations and current PROPOSED status remain unchanged; no closed historical or neighbor issue/category resolved. Source-neutral chemical TODOs remain valid; label-only constituents and append-only rationale do not require fabricated corrections.

### Frozen inputs/native original pairs/current coverage

schema: supported. Targets: GO:0009529.

All75 old frozen hashes verify; five original YAML/Markdown pairs validate/render exactly. Own target unchanged. Ten actual native protein commands pass with zero examples/typed nodes; positive narrative machinery still needs applicability assessment.

### Complete record and bounded verdict

completeness: supported. Targets: GO:0009529.

Full current record reviewed: no maintained images, verbatim snippets, quantitative physical properties or individual protein accessions require extra claims. No supported scientific finding; qualified pass preserves molecular/experimental/access limits.

### Exact identity and hierarchy

identity: supported. Targets: GO:0042170.

ExactGO42170 definition plusGO16020 ancestry; explicit GO is_a children andSL0213 nested fallback support internal thylakoid class despite envelope-focused definition prose.

### Anatomical component identity versus chemical material

grounding: supported. Targets: GO:0042170.

Reviewed-label-only collective bilayer material has no erroneous whole-membrane chemical grounding. Defining collective material remains distinct from exact lipid species.

### Individual formation necessity

evidence: unknown. Targets: GO:0042170.

UNKNOWN on whole/envelope retained; ESSENTIAL on inner/generic bilayer denotes defining collective material only. Neither anatomy nor TOC–TIC cryoEM observation establishes individual lipid/protein necessity for formation. IMS has no such constituent requirement.

### Every descriptive edge and source scope

graph: supported. Targets: GO:0042170.

Three NONMECHANISTIC is_a edges outer,inner,thylakoid→generic membrane verified directly in GO children; no universal membrane count/protein composition inferred.

### Qualitative occurrence and lineage bounds

scope: supported. Targets: GO:0042170.

Current2759/33090/3055 identities verified. Keeling s1/s3/s6 supports green-primary and scattered secondary/reduced contexts; RARE/COMMON are qualitative, not measured frequencies or all-isolate claims. Historical phylogenetic models are not presented as current complete consensus.

### Exact canonical example and experimental extent

evidence: supported. Targets: GO:0042170.

Terashima secondary abstract and retained pp151–152 support a C.reinhardtii chloroplast used for proteome/protein-biogenesis research. The record does not claim a specific protein cohort, experimental membrane-only proteome or detailed pathway merely by naming the model.

### Whole-record structured-source applicability

evidence: not_applicable. Targets: GO:0042170.

Genuine physical/material/class scope: canonical model use for proteome/protein-biogenesis studies is research context, not a positive specified molecular cohort/pathway. Graph/discussion withhold specialized machinery. Background source biology is not imported as a record assertion; no mandatory dataset query defect.

### Historical boundary decisions and grounding discussions

provenance: supported. Targets: GO:0042170.

Original observations and current PROPOSED status remain unchanged; no closed historical or neighbor issue/category resolved. Source-neutral chemical TODOs remain valid; label-only constituents and append-only rationale do not require fabricated corrections.

### Frozen inputs/native original pairs/current coverage

schema: supported. Targets: GO:0042170.

All75 old frozen hashes verify; five original YAML/Markdown pairs validate/render exactly. Own target unchanged. Ten actual native protein commands pass with zero examples/typed nodes; positive narrative machinery still needs applicability assessment.

### Complete record and bounded verdict

completeness: supported. Targets: GO:0042170.

Full current record reviewed: no maintained images, verbatim snippets, quantitative physical properties or individual protein accessions require extra claims. No supported scientific finding; qualified pass preserves molecular/experimental/access limits.

### Complete frozen-input comparison and bounded refresh

provenance: supported. Targets: GO:0106174, GO:0034357, GO:0042717, GO:0031979, GO:0031676, GO:0009536, GO:0009526, GO:0009528, GO:0009529, GO:0042170.

2 of ten original target hashes differ from current main. The changed content is substantively reassessed in the target-specific assessments; original observations remain historical and unchanged. All current target and used context bytes are frozen.

## Findings

### septin-phagolysosome_vesicle_lumen-F1: Bound the expanded definition to demonstrated biology

major / open / confirmed; issue key: phagolysosome-vesicle-lumen-expanded-definition-scope.

The appended definition makes a cross-taxon molecular inventory and microbial-killing claim under a GO definition source that specifies only enclosed volume. The cited primary study directly resolves Dictyostelium trafficking and constituent profiles, not the entire stated enzymatic/ROS program across all named lineages.

### septin-phagolysosome_vesicle_lumen-F2: Align graph scope with its descriptive edges

minor / open / confirmed; issue key: phagolysosome-vesicle-lumen-graph-scope.

The MECHANISTIC scope and assembly/functional-mechanism title overstate the two descriptive edges: parthood and whole-volume association with acidification. No proton transport or other explanatory transition is represented.

### septin-phagolysosome_vesicle_lumen-F3: Qualify the acidification assay attribution

minor / open / confirmed; issue key: phagolysosome-vesicle-lumen-acidification-source-scope.

The canonical example and function evidence note blend directly dissected membrane/luminal trafficking phases with acidification behavior. Gotthardt2002 discusses acidification from prior work rather than presenting a direct luminal-pH assay in its Methods/Results.

### septin-plasma_membrane_derived_thylakoid_lumen-F1: Correct the experimental organism attributed to the thylakoid studies

major / open / confirmed; issue key: plasma-membrane-derived-thylakoid-lumen-1.

The cited Huokko2021 de novo-thylakoid study is assigned to Synechocystis PCC6803. The inspected primary Methods/Results identify Synechococcus elongatus PCC7942. These are distinct genera and taxon nodes. Correct the experiment/example and the explicit source notes together; do not change separately supported Synechocystis protein examples or imply that PCC6803 lacks thylakoids.

### septin-plasma_membrane_derived_thylakoid_membrane-F1: Correct the experimental organism attributed to the thylakoid studies

major / open / confirmed; issue key: plasma-membrane-derived-thylakoid-membrane-1.

The cited Huokko2021 de novo-thylakoid study and Casella2017 mapping/FRAP notes is assigned to Synechocystis PCC6803. The inspected primary Methods/Results identify Synechococcus elongatus PCC7942. These are distinct genera and taxon nodes. Correct the experiment/example and the explicit source notes together; do not change separately supported Synechocystis protein examples or imply that PCC6803 lacks thylakoids.

### plaque-t1-F1: Correct the experimental organism attributed to the thylakoid studies

major / open / confirmed; issue key: photosynthetic-membrane-1.

The cited Casella2017 native-architecture/FRAP study is assigned to Synechocystis PCC6803. The inspected primary Methods/Results identify Synechococcus elongatus PCC7942. These are distinct genera and taxon nodes. Correct the experiment/example and the explicit source notes together; do not change separately supported Synechocystis protein examples or imply that PCC6803 lacks thylakoids.

### plaque-t1-F2: Qualify the oxygenic scope of the GO-grounded light-reaction function

minor / open / confirmed; issue key: photosynthetic-membrane-2.

GO0019684 explicitly defines oxygenic PSI/PSII light reactions involving water oxidation and NADP reduction. The function description is broad and its evidence combines an oxygenic thylakoid review with anoxygenic purple-bacterial architecture, without stating that the GO-grounded function applies to the oxygenic subset. Preserve the broad membrane class but delimit the GO claim and move the purple-specific support to the broader electron-transport/energy-conversion account.

### plaque-t2-F1: Ground the two existing complexes with verified whole-complex identifiers

minor / open / confirmed; issue key: plasma-membrane-derived-chromatophore-membrane-1.

The existing LH2 constituent remains REVIEWED_LABEL_ONLY while the frozen maintained record cellstructuremech:lh2_peripheral_light_harvesting_antenna_complex supplies the exact whole-complex identity in the same chromatophore context. The existing F0F1 constituent also remains label-only solely pending a chromatophore-localized accession, although active GO0045259 exactly names the F1-F0 ATP synthase complex; location belongs in its role/context. This is a bounded gap in two already asserted constituents, not a demand for an optional new inventory or a claim that the historical pass had access to future records.

### micro-F1: Separate membrane structures from molecular lipid grounding

major / open / confirmed; issue key: plastid-lipid-whole-membrane-grounding.

The maintained LIPID component row uses GO0042170 for the complete generic plastid membrane class. These are structural cellular-component identities, not the molecular lipid material identity required by the declared component type. Linked graph component_ref fields perpetuate that typing mismatch even though the structural nodes and topology are sound.

### micro-F2: Separate membrane structures from molecular lipid grounding

major / open / confirmed; issue key: plastid-envelope-lipid-whole-membrane-grounding.

The maintained LIPID component rows use GO0009527 and GO0009528 for complete outer and inner membranes. These are structural cellular-component identities, not the molecular lipid material identity required by the declared component type. Linked graph component_ref fields perpetuate that typing mismatch even though the structural nodes and topology are sound.

## Recommended Actions And Acceptance Checks

### septin-phagolysosome_vesicle_lumen-A1

Retain the ontology volume definition and place supported extra biology in source-, taxon- and stage-qualified fields, or provide directly inspected evidence for each retained extension.

- Ontology text and added interpretation are distinguished.
- No complete cross-taxon digestive program is inferred solely from Dictyostelium time profiles.
- Correct lumen hierarchy and supported maturation are preserved.
- Native schema, strict, identifier, graph and history checks pass after separately authorized curation.

### septin-phagolysosome_vesicle_lumen-A2

Use NONMECHANISTIC with a precise scope note and title, or separately curate a source-backed mechanistic path.

- Scope and title match actual graph resolution.
- No unsupported obligatory component is introduced to make the graph mechanistic.
- Native schema, strict, identifier, graph and history checks pass after separately authorized curation.

### septin-phagolysosome_vesicle_lumen-A3

Distinguish measured trafficking profiles from acidification context synthesized from earlier studies, or cite inspected direct pH evidence.

- The note accurately identifies which measurements the cited study performed.
- Supported qualitative maturation and acidification are retained.
- Native schema, strict, identifier, graph and history checks pass after separately authorized curation.

### septin-plasma_membrane_derived_thylakoid_lumen-A1

In separately authorized curation, use Synechococcus elongatus PCC7942 for these exact studies and verify the taxon pairing, or supply a genuinely matching PCC6803 study for a retained PCC6803 example; align every explicit source note.

- Each changed field matches the exact source organism, process or whole-complex identity.
- Correct structure boundaries, protein identities and original history remain intact.
- Native schema, strict, CURIE, graph and history gates pass.

### septin-plasma_membrane_derived_thylakoid_membrane-A1

In separately authorized curation, use Synechococcus elongatus PCC7942 for these exact studies and verify the taxon pairing, or supply a genuinely matching PCC6803 study for a retained PCC6803 example; align every explicit source note.

- Each changed field matches the exact source organism, process or whole-complex identity.
- Correct structure boundaries, protein identities and original history remain intact.
- Native schema, strict, CURIE, graph and history gates pass.

### plaque-t1-A1

In separately authorized curation, use Synechococcus elongatus PCC7942 for these exact studies and verify the taxon pairing, or supply a genuinely matching PCC6803 study for a retained PCC6803 example; align every explicit source note.

- Each changed field matches the exact source organism, process or whole-complex identity.
- Correct structure boundaries, protein identities and original history remain intact.
- Native schema, strict, CURIE, graph and history gates pass.
- Preserve append-only historical rationale/events; amend current fields or append a scoped resolution. Do not resolve unrelated category or neighbor findings.

### plaque-t1-A2

In separately authorized curation, state explicitly that GO0019684 applies to the oxygenic subset and attach only matching support there; retain purple photochemistry under the already broader function or another exactly verified process.

- Each changed field matches the exact source organism, process or whole-complex identity.
- Correct structure boundaries, protein identities and original history remain intact.
- Native schema, strict, CURIE, graph and history gates pass.
- Preserve append-only historical rationale/events; amend current fields or append a scoped resolution. Do not resolve unrelated category or neighbor findings.

### plaque-t2-A1

In separately authorized curation, ground LH2 to the exact maintained local complex and F0F1 to GO0045259, retain source-specific localization and UNKNOWN formation necessity, and resolve the current grounding task without rewriting historical events.

- Each changed field matches the exact source organism, process or whole-complex identity.
- Correct structure boundaries, protein identities and original history remain intact.
- Native schema, strict, CURIE, graph and history gates pass.
- Preserve append-only historical rationale/events; amend current fields or append a scoped resolution. Do not resolve unrelated category or neighbor findings.

### micro-A1

Keep correct GO membrane entities as structural nodes/parts. If the rows mean collective lipid material, relabel and use honest reviewed-label-only grounding pending a justified chemical identifier; if they mean structural subparts, represent them with an appropriate explicit structural type rather than LIPID. Align component_ref links with the chosen model.

- No LIPID molecular row uses a complete membrane GO identity as its chemical grounding.
- Valid membrane identities, has_part topology and boundaries remain intact.
- No specific lipid species or obligatory protein inventory is invented.
- Native schema, strict, identifier, graph and history checks pass after separately authorized curation.

### micro-A2

Keep correct GO membrane entities as structural nodes/parts. If the rows mean collective lipid material, relabel and use honest reviewed-label-only grounding pending a justified chemical identifier; if they mean structural subparts, represent them with an appropriate explicit structural type rather than LIPID. Align component_ref links with the chosen model.

- No LIPID molecular row uses a complete membrane GO identity as its chemical grounding.
- Valid membrane identities, has_part topology and boundaries remain intact.
- No specific lipid species or obligatory protein inventory is invented.
- Native schema, strict, identifier, graph and history checks pass after separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| current-record-0 | data/structures/membrane_organelle/phagolysosome_vesicle_lumen.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 096069e6ecc9f33d640dfb9621fa69dedfab50cb9a9f08e6186e9583a823c319; current SHA256 096069e6ecc9f33d640dfb9621fa69dedfab50cb9a9f08e6186e9583a823c319. Record bytes unchanged since the original review. |
| original-review-0 | reviews/structured/20261022T032300Z-phagolysosome-vesicle-lumen-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-1 | data/structures/membrane_organelle/photosynthetic_membrane.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 5fe446aae99635ba843cf22d1144ab1312a2c30224367c49efd0bedcbd06db97; current SHA256 5fe446aae99635ba843cf22d1144ab1312a2c30224367c49efd0bedcbd06db97. Record bytes unchanged since the original review. |
| original-review-1 | reviews/structured/20261022T032301Z-photosynthetic-membrane-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-2 | data/structures/membrane_organelle/plasma_membrane_derived_chromatophore_membrane.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 f3130fc795ff500febb7d273c6a7b281ec7d2cc230d6e44fb5363c6c9256b064; current SHA256 e2622df75241a3d18a0c08f64d1e59fc10f49da8ee8ed7843cf6f08df2020195. Changed record reassessed against current sources. |
| original-review-2 | reviews/structured/20261022T032301Z-plasma-membrane-derived-chromatophore-membrane-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-3 | data/structures/membrane_organelle/plasma_membrane_derived_thylakoid_lumen.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 4b4fbe694529235b322625d85f5c210eddea0cc03e5e1a684d5bff2d698bca82; current SHA256 4b4fbe694529235b322625d85f5c210eddea0cc03e5e1a684d5bff2d698bca82. Record bytes unchanged since the original review. |
| original-review-3 | reviews/structured/20261022T032302Z-plasma-membrane-derived-thylakoid-lumen-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-4 | data/structures/membrane_organelle/plasma_membrane_derived_thylakoid_membrane.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 66205b2d304df6e2b425730f885ccf46de08dc94c99c60636eab667d3bf68410; current SHA256 50b81e60972c1a3c89a73cf685b98887a221a3b0ba379b10fee8be1765d167e0. Changed record reassessed against current sources. |
| original-review-4 | reviews/structured/20261022T032303Z-plasma-membrane-derived-thylakoid-membrane-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-5 | data/structures/membrane_organelle/plastid.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 1be30ab06bc2fbae9294930ceaf74b20a2d43d8af60986aa9ed0e07b9645ae81; current SHA256 1be30ab06bc2fbae9294930ceaf74b20a2d43d8af60986aa9ed0e07b9645ae81. Record bytes unchanged since the original review. |
| original-review-5 | reviews/structured/20261022T032303Z-plastid-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-6 | data/structures/membrane_organelle/plastid_envelope.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 9033a6955c21d6043019061509c7ca1bf470bec884e7f4e1a5edc0080b680968; current SHA256 9033a6955c21d6043019061509c7ca1bf470bec884e7f4e1a5edc0080b680968. Record bytes unchanged since the original review. |
| original-review-6 | reviews/structured/20261022T032304Z-plastid-envelope-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-7 | data/structures/membrane_organelle/plastid_inner_membrane.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 ceb12c6ee4451216ae406f17f68ea2d3730a6da302b38e8bb8fcabc532a6a4fa; current SHA256 ceb12c6ee4451216ae406f17f68ea2d3730a6da302b38e8bb8fcabc532a6a4fa. Record bytes unchanged since the original review. |
| original-review-7 | reviews/structured/20261022T032305Z-plastid-inner-membrane-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-8 | data/structures/membrane_organelle/plastid_intermembrane_space.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 2ef21406931fb90ec3aead7f57ee12a4376ad3d95276c7db3c2a7ab324c73c5d; current SHA256 2ef21406931fb90ec3aead7f57ee12a4376ad3d95276c7db3c2a7ab324c73c5d. Record bytes unchanged since the original review. |
| original-review-8 | reviews/structured/20261022T032305Z-plastid-intermembrane-space-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-9 | data/structures/membrane_organelle/plastid_membrane.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 ae09183c12ecb85ac2135b3615b9a613985285039f5730126227fde982e55bef; current SHA256 ae09183c12ecb85ac2135b3615b9a613985285039f5730126227fde982e55bef. Record bytes unchanged since the original review. |
| original-review-9 | reviews/structured/20261022T032306Z-plastid-membrane-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| septin-review-policy | .claude/skills/review-yaml-record/SKILL.md; Current molecular/pathway applicability and bounded fallback | supports | Positive molecular or pathway assertions trigger structured-source applicability even without an expression claim or individual examples. Use matched organism/strain evidence and distinguish source unavailability from scientific absence. |
| septin-curation-policy | docs/CURATION.md; Identity, source-specific evidence, generic classes and append-only discussion | supports | Exact structure identity, constituent identity, localization and formation necessity are distinct. Dated rationale is provenance, not current inventory; optional examples and generic classes do not automatically require curation. |
| septin-schema-policy | src/cellstructuremech/schema/cellstructuremech.yaml; Current structure, material, graph and evidence contract | supports | Collective material, molecular complexes and structure nodes are distinct native representations. No enum-only complex defect or guessed chemical/protein CURIE is introduced. |
| septin-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Mechanistic scope and graph actors/relations | supports | Parthood and broad process associations must not be presented as a represented explanatory actor/transition mechanism. Graph source observations must match the actual frozen version. |
| septin-protein-policy | .claude/skills/uniprot-protein-examples/SKILL.md; Native examples and graph coverage | supports | Native accession/coverage checks certify the represented scope; an empty inventory is neither molecular completeness nor biological absence. |
| septin-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0106174,GO:0032010,GO:0097013,GO:0060205,GO:0045335,GO:0030670,GO:0090383,GO:0031979,GO:0031676,GO:0030075,GO:0009579,GO:0042651,GO:0030094,GO:0030096,GO:0009512,GO:0045259,GO:0009767; All17 exact current GO entries: definitions, identifiers, synonyms and immediate typed relations | supports | GO0106174 supplies the phagolysosome lumen volume definition, with broader phagocytic-lumen and whole-organelle boundaries; it does not supply the appended cross-taxon enzyme/ROS program. GO0031979 and GO0031676 identify bacterial thylakoid lumen/membrane. GO0030075 allows derivation/association without obligatory physical continuity with plasma membrane; GO0009579 explicitly excludes organelle classification. GO complex/process definitions support PSII, PSI, b6f, F-type ATP synthase and electron transport, without proving individual formation necessity. Direct whole-thylakoid part relations are not silently treated as direct membrane-part ontology axioms. |
| septin-SL0044 | https://rest.uniprot.org/locations/SL-0044.json; Exact location definition, synonyms/GO mapping and immediate isA/partOf fields; nested boundary text read | supports | Exact cellular-thylakoid lumen maps GO0031979; immediate partOf cellular thylakoid supports boundary. Nested Synechocystis discontinuity description is background, not the organism of Huokko2021. |
| septin-SL0045 | https://rest.uniprot.org/locations/SL-0045.json; Exact location definition, synonyms/GO mapping and immediate isA/partOf fields; nested boundary text read | supports | Exact cellular-thylakoid membrane maps GO0031676 and partOf cellular thylakoid. Nested SL0043 calls discontinuous Synechocystis membranes organelles whereas GO0009579 says thylakoids are not organelles; target native MEMBRANE/SUBCELLULAR_REGION classification is retained without inventing an enum defect. |
| septin-SL0342 | https://rest.uniprot.org/locations/SL-0342.json; Exact location definition, synonyms/GO mapping and immediate isA/partOf fields; nested boundary text read | supports | Broader phagosome lumen has phagocytic/phagosomal synonyms, cytoplasmic-vesicle-lumen parent and phagosome parthood. It is not exact phagolysosome-lumen identity or a molecular-program source. |
| septin-tax1117 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1117; Complete current ENA/NCBI taxonomy response: identifier, rank, status, lineage and supplied aliases | supports | Active Cyanobacteriota phylum, used for broad occurrence rather than experiment identity. Qualitative COMMON occurrence is not a census or every-strain guarantee. |
| septin-tax1148 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1148; Complete current ENA/NCBI taxonomy response: identifier, rank, status, lineage and supplied aliases | supports | Synechocystis sp. PCC6803 species taxon; distinct from the experimental Synechococcus lineage. Qualitative COMMON occurrence is not a census or every-strain guarantee. |
| septin-tax1140 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1140; Complete current ENA/NCBI taxonomy response: identifier, rank, status, lineage and supplied aliases | supports | Synechococcus elongatus PCC7942 strain, including FACHB805 synonym. This is the host used by Casella2017 and Huokko2021, not PCC6803. Qualitative COMMON occurrence is not a census or every-strain guarantee. |
| septin-tax44689 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/44689; Complete current ENA/NCBI taxonomy response: identifier, rank, status, lineage and supplied aliases | supports | Active Dictyostelium discoideum species; the primary study independently specifies Ax2 in HL5c at22C. Qualitative COMMON occurrence is not a census or every-strain guarantee. |
| septin-perez2024-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1146%2Fannurev-cellbio-120823-022747&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact DOI EuropePMC result; complete metadata and abstract | supports | Perez Boerema, Engel and Wietrzynski2024 Evolution of Thylakoid Structural Diversity is a secondary review, PMID38950450. Metadata/abstract do not substitute for the separately read genuine body. |
| septin-huokko2021-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038%2Fs41467-021-23680-1&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact DOI EuropePMC result; complete metadata and abstract | supports | Huokko2021 Probing the biogenesis pathway and dynamics of thylakoid membranes, PMID34108457/PMC8190092, explicitly studies Synechococcus elongatus7942. |
| septin-casella2017-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1016%2Fj.molp.2017.09.019&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact DOI EuropePMC result; complete metadata and abstract | supports | Casella2017 Dissecting the Native Architecture and Dynamics of Cyanobacterial Photosynthetic Machinery, PMID29017828/PMC5683893, explicitly studies Synechococcus elongatus7942. |
| septin-casella2017-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC5683893.1/PMC5683893.1.xml; Published JATS Results2.1/2.2/2.3 and Methods4.1/4.8, Fig1–5 text captions and Table1 text; no image pixels/supplements/raw data | supports | Actual native organism is Synechococcus elongatus7942. Detergent-free thylakoid preparations, immunoblot/BN-PAGE and functional fluorescent tags support PSII, PSI, b6f and ATP-synthase thylakoid residence and conditional mobility. AFM b6f assignment is explicitly tentative; native-tag/confocal evidence is separate. BG11 at30C/50 microeinstein light is the experimental context. Synechocystis6803 appears as comparison, not the studied FRAP host. Paper ATP-beta nomenclature is not silently converted to the unrelated database Fo-subunit-atpB name. |
| septin-huokko2021-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC8190092.1/PMC8190092.1.xml; Published JATS ResultsSec3/4 and MethodsSec9/12/13, Fig1/2 text captions; no pixels/supplements/raw data | supports | Actual organism is Synechococcus elongatus7942. HL300 treatment followed by LL20 recovery at30C in BG11 was used to study thylakoid biogenesis with TEM/cryoET. New membrane fragments occur near plasma membrane/preexisting thylakoids, but no apparent direct plasma-membrane connection/fusion was observed. Tentative VIPP1-like objects remain tentative. Synechocystis6803 is comparative background, not the canonical experiment. No universal continuity or causal formation necessity is inferred. |
| septin-perez2024-delivered | https://www.annualreviews.org/docserver/ahah/fulltext/cellbio/40/1/annurev-cellbio-120823-022747.html?expires=1793737002&amp;id=id&amp;accname=guest&amp;checksum=47EAFDAB41E06430970416431EF37629; Genuine publisher-delivered secondary full-text HTML fragment: Introduction, Building Blocks/Lipids and Electron Transport Chain Complexes, Fig1/2 text captions; no pixels or reference-body audit | supports | Secondary review explicitly describes lumen separation/proton gradients, Gloeobacter exception, collective galactolipid-rich membrane and four major ETC/ATP-synthesis complexes. PSII water oxidation, b6f proton transfer, PSI electron transfer and proton-gradient-driven ATP synthase are contextual synthesis. Supports the newly added ATP-synthase residence edge; no new exact subunit stoichiometry, universal lipid percentage or individual formation-necessity claim is inferred. Publisher landing page alone was a loading shell; the actual body was retrieved through its public delivery link. |
| septin-PMID12388753 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12388753+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=25; Cached exact EuropePMC MED record: complete metadata/abstract reread now | supports | Gotthardt2002 High-resolution dissection of phagosome maturation reveals distinct membrane trafficking phases, PMID12388753/PMC129962/DOI10.1091/mbc.e02-04-0206. Abstract describes Ax2 pulse-chase trafficking, two hydrolase-delivery phases and recycling; direct pH measurement is not the reported assay. Cached source was retrieved at 2026-11-03T19:21:29.422467Z; current reinspection is not a fresh HTTP access. |
| septin-gotthardt2002-unige-pdf | https://access.archive-ouverte.unige.ch/access/metadata/7ba3d74f-e1a5-4cae-8646-670a6fd9a236/download; Cached published primary PDF pp3508–3518 inspected in PR2374; current reread Methods pp3509–3510 and Discussion/Fig7 text pp3517–3518; complete abstract also reread. No new pixel/raw/supplement audit | supports | Actual Ax2 latex-bead pulse/chase purification, immunoblot/protein-lipid analyses and microscopy resolve trafficking/composition. Current Methods reread confirms no direct luminal-pH assay; Discussion combines own and prior work, citing Maniak1999/2001 for acidification. CatD/CPp34 delivery/recycling does not establish the entire asserted cross-taxon protease/lysozyme/phospholipase/ROS program. This is an attribution/scope limit, not denial of qualitative acidification or any particular organism biology. Cached source was retrieved at 2026-11-03T19:23:10.499151Z; current reinspection is not a fresh HTTP access. |
| septin-catalogue | https://imodulondb.org/api/datasets; Complete fresh official organism/dataset catalogue; all rows/dataset strings inspected | supports | s_elongatus/elprecise300 is available; selected gene identities explicitly carry Synpcc7942 and tax1140 string IDs. No Synechocystis6803, Dictyostelium/Ax2, Entamoeba or ciliate host dataset occurs. PCC7942 evidence is relevant to the actual cited experiments and broad cyanobacterial pathway, never a substitute for the incorrect PCC6803 attribution. Catalogue noncoverage is not biological absence. |
| septin-adapter-search-photosystem | https://imodulondb.org/api/search?organism=s_elongatus&amp;dataset=elprecise300&amp;query=photosystem&amp;limit=50; Official matched-host dataset search response, complete returned structured hits | supports | 36 gene hits and modules38 Photosystems/1 PSII. These queries corroborate relevant source coverage, not molecular necessity or completeness. |
| septin-adapter-search-cytochrome-b6 | https://imodulondb.org/api/search?organism=s_elongatus&amp;dataset=elprecise300&amp;query=cytochrome+b6&amp;limit=50; Official matched-host dataset search response, complete returned structured hits | supports | Seven gene hits, including petB Synpcc7942_2331; no module hit in this bounded text search. These queries corroborate relevant source coverage, not molecular necessity or completeness. |
| septin-adapter-search-ATP-synthase | https://imodulondb.org/api/search?organism=s_elongatus&amp;dataset=elprecise300&amp;query=ATP+synthase&amp;limit=50; Official matched-host dataset search response, complete returned structured hits | supports | Nine gene hits including atpA Synpcc7942_0336; no module hit in this bounded text search. Function labels are database annotations, not a new experimental validation. These queries corroborate relevant source coverage, not molecular necessity or completeness. |
| septin-adapter-search-thylakoid | https://imodulondb.org/api/search?organism=s_elongatus&amp;dataset=elprecise300&amp;query=thylakoid&amp;limit=50; Official matched-host dataset search response, complete returned structured hits | supports | Two gene hits including lepB1; no module hit in this bounded text search. These queries corroborate relevant source coverage, not molecular necessity or completeness. |
| septin-adapter-gene-Synpcc7942_2049 | https://imodulondb.org/api/genes/s_elongatus/elprecise300/Synpcc7942_2049; Exact matched-host gene response: gene/locus, product, source tax1140 string identifier and database accession | supports | Selected psaA identity corroborates PCC7942 scope. Unrecorded dataset accessions are contextual and are not proposed as new maintained protein examples or independent localization/causality evidence. |
| septin-adapter-gene-Synpcc7942_2049-modules | https://imodulondb.org/api/genes/s_elongatus/elprecise300/Synpcc7942_2049/imodulons; All57 returned module-association rows; is_in_imodulon flags and relevant thresholds inspected | supports | Single positive flag is module38 Photosystems. Threshold membership is dataset-specific and does not prove structural presence/absence, gene expression absence, regulation, causality or formation necessity. |
| septin-adapter-gene-Synpcc7942_0424 | https://imodulondb.org/api/genes/s_elongatus/elprecise300/Synpcc7942_0424; Exact matched-host gene response: gene/locus, product, source tax1140 string identifier and database accession | supports | Selected psbA1 identity corroborates PCC7942 scope. Unrecorded dataset accessions are contextual and are not proposed as new maintained protein examples or independent localization/causality evidence. |
| septin-adapter-gene-Synpcc7942_0424-modules | https://imodulondb.org/api/genes/s_elongatus/elprecise300/Synpcc7942_0424/imodulons; All57 returned module-association rows; is_in_imodulon flags and relevant thresholds inspected | supports | No true module-membership flag among the57 returned rows. Threshold membership is dataset-specific and does not prove structural presence/absence, gene expression absence, regulation, causality or formation necessity. |
| septin-adapter-gene-Synpcc7942_2331 | https://imodulondb.org/api/genes/s_elongatus/elprecise300/Synpcc7942_2331; Exact matched-host gene response: gene/locus, product, source tax1140 string identifier and database accession | supports | Selected petB identity corroborates PCC7942 scope. Unrecorded dataset accessions are contextual and are not proposed as new maintained protein examples or independent localization/causality evidence. |
| septin-adapter-gene-Synpcc7942_2331-modules | https://imodulondb.org/api/genes/s_elongatus/elprecise300/Synpcc7942_2331/imodulons; All57 returned module-association rows; is_in_imodulon flags and relevant thresholds inspected | supports | Single positive flag is module38 Photosystems. Threshold membership is dataset-specific and does not prove structural presence/absence, gene expression absence, regulation, causality or formation necessity. |
| septin-adapter-gene-Synpcc7942_0336 | https://imodulondb.org/api/genes/s_elongatus/elprecise300/Synpcc7942_0336; Exact matched-host gene response: gene/locus, product, source tax1140 string identifier and database accession | supports | Selected atpA ATP-synthase alpha identity corroborates PCC7942 scope. Unrecorded dataset accessions are contextual and are not proposed as new maintained protein examples or independent localization/causality evidence. |
| septin-adapter-gene-Synpcc7942_0336-modules | https://imodulondb.org/api/genes/s_elongatus/elprecise300/Synpcc7942_0336/imodulons; All57 returned module-association rows; is_in_imodulon flags and relevant thresholds inspected | supports | No true module-membership flag among the57 returned rows. Threshold membership is dataset-specific and does not prove structural presence/absence, gene expression absence, regulation, causality or formation necessity. |
| septin-adapter-module-1 | https://imodulondb.org/api/imodulons/s_elongatus/elprecise300/1; Exact module metadata and returned gene IDs/weights; generated prose and activities excluded | supports | Module1 PSII has21 listed genes and does not include the four selected loci. Reported n_conditions=0 is endpoint metadata, not proof of a biologically conditionless experiment. No AI-generated summary is treated as scientific evidence. |
| septin-adapter-module-38 | https://imodulondb.org/api/imodulons/s_elongatus/elprecise300/38; Exact module metadata and returned gene IDs/weights; generated prose and activities excluded | supports | Module38 Photosystems has44 listed genes and includes psaA2049/petB2331, consistent with their positive gene-response flags. Reported n_conditions=0 is endpoint metadata, not proof of a biologically conditionless experiment. No AI-generated summary is treated as scientific evidence. |
| septin-adapter-runner-historical | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical attempted runner; no fresh invocation | supports | Actual00:49:00.848907Z–00:49:00.863225Z exit1 PermissionError reading pyvenv.cfg remains historical. Fresh HTTP catalogue/downstream/source fallback is separate and is not a new runner success. |
| septin-retrieval-source-receipts | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/adversary-septin/source-receipts.json; Actual fresh HTTP receipts and byte hashes | supports | Successful genuine body and official source endpoints are distinguished from publisher loading shell, intermediate delivery URL, dataset SPA shell and application script used only to locate public endpoints. Cached Gotthardt bytes and independently reread collaborating primary snapshots preserve their actual original timestamps. |
| septin-retrieval-additional-source-receipts | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/adversary-septin/additional-source-receipts.json; Actual fresh HTTP receipts and byte hashes | supports | Successful genuine body and official source endpoints are distinguished from publisher loading shell, intermediate delivery URL, dataset SPA shell and application script used only to locate public endpoints. Cached Gotthardt bytes and independently reread collaborating primary snapshots preserve their actual original timestamps. |
| septin-retrieval-downstream-source-receipts | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/adversary-septin/downstream-source-receipts.json; Actual fresh HTTP receipts and byte hashes | supports | Successful genuine body and official source endpoints are distinguished from publisher loading shell, intermediate delivery URL, dataset SPA shell and application script used only to locate public endpoints. Cached Gotthardt bytes and independently reread collaborating primary snapshots preserve their actual original timestamps. |
| septin-context-phagolysosome | data/structures/membrane_organelle/phagolysosome.yaml; Frozen boundary context only: identifier, label, definition, parent_structures, part_of, has_part and xrefs | supports | Bounded context read after root froze this exact input. No complete neighbor mechanism/verdict or existing issue disposition is inferred. |
| septin-context-phagolysosome_membrane | data/structures/membrane_organelle/phagolysosome_membrane.yaml; Frozen boundary context only: identifier, label, definition, parent_structures, part_of, has_part and xrefs | supports | Bounded context read after root froze this exact input. No complete neighbor mechanism/verdict or existing issue disposition is inferred. |
| septin-context-bacterial_thylakoid | data/structures/membrane_organelle/bacterial_thylakoid.yaml; Frozen boundary context only: identifier, label, definition, parent_structures, part_of, has_part and xrefs | supports | Bounded context read after root froze this exact input. No complete neighbor mechanism/verdict or existing issue disposition is inferred. |
| septin-context-proton_transporting_atp_synthase_complex | data/structures/energy_complex/proton_transporting_atp_synthase_complex.yaml; Frozen boundary context only: identifier, label, definition, parent_structures, part_of, has_part and xrefs | supports | Bounded context read after root froze this exact input. No complete neighbor mechanism/verdict or existing issue disposition is inferred. |
| septin-record-phagolysosome_vesicle_lumen | data/structures/membrane_organelle/phagolysosome_vesicle_lumen.yaml; Complete current record at 659d5d9ce7e16c8607002bf1655db2f3c652e6e1 | supports | All identity, definition, components, taxa/examples, function/source notes, discussion/history and graph fields read. Independently counted0 individual examples,0 GENE_OR_PROTEIN nodes,0 UniProtKB graph xrefs and no maintained images.  |
| septin-original-phagolysosome_vesicle_lumen | reviews/structured/20261022T032300Z-phagolysosome-vesicle-lumen-audit/review.yaml; Complete immutable original YAML/Markdown pair, original findings/actions/verdict and source snapshot | supports | Old source access/checks remain historical. Every inherited finding is retained with exact predecessor. Original frozen target bytes match current target. |
| septin-original-validation-phagolysosome_vesicle_lumen | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/adversary-septin/original-checks.json; Actual native validate/render, exact Markdown equality and original frozen/current target hash comparison | supports | Native original validation/render exit0 and exact Markdown. Historical source target matches frozen input; current target matches. Schema validity does not certify scientific support. |
| septin-native-phagolysosome_vesicle_lumen-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/phagolysosome_vesicle_lumen-uniprot-verify-receipt.json; Actual native receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/phagolysosome_vesicle_lumen-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0. Independently counted0 individual protein examples,0 GENE_OR_PROTEIN nodes and0 UniProtKB graph xrefs. Exit0 covers this empty represented scope, not complete molecular coverage or scientific validity. Positive narrative pathway assertions remain separately assessed. |
| septin-native-phagolysosome_vesicle_lumen-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/phagolysosome_vesicle_lumen-uniprot-causal-receipt.json; Actual native receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/phagolysosome_vesicle_lumen-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Exit0. Independently counted0 individual protein examples,0 GENE_OR_PROTEIN nodes and0 UniProtKB graph xrefs. Exit0 covers this empty represented scope, not complete molecular coverage or scientific validity. Positive narrative pathway assertions remain separately assessed. |
| septin-record-plasma_membrane_derived_thylakoid_lumen | data/structures/membrane_organelle/plasma_membrane_derived_thylakoid_lumen.yaml; Complete current record at 659d5d9ce7e16c8607002bf1655db2f3c652e6e1 | supports | All identity, definition, components, taxa/examples, function/source notes, discussion/history and graph fields read. Independently counted0 individual examples,0 GENE_OR_PROTEIN nodes,0 UniProtKB graph xrefs and no maintained images.  |
| septin-original-plasma_membrane_derived_thylakoid_lumen | reviews/structured/20261022T032302Z-plasma-membrane-derived-thylakoid-lumen-audit/review.yaml; Complete immutable original YAML/Markdown pair, original findings/actions/verdict and source snapshot | supports | Old source access/checks remain historical. Every inherited finding is retained with exact predecessor. Original frozen target bytes match current target. |
| septin-original-validation-plasma_membrane_derived_thylakoid_lumen | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/adversary-septin/original-checks.json; Actual native validate/render, exact Markdown equality and original frozen/current target hash comparison | supports | Native original validation/render exit0 and exact Markdown. Historical source target matches frozen input; current target matches. Schema validity does not certify scientific support. |
| septin-native-plasma_membrane_derived_thylakoid_lumen-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plasma_membrane_derived_thylakoid_lumen-uniprot-verify-receipt.json; Actual native receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plasma_membrane_derived_thylakoid_lumen-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0. Independently counted0 individual protein examples,0 GENE_OR_PROTEIN nodes and0 UniProtKB graph xrefs. Exit0 covers this empty represented scope, not complete molecular coverage or scientific validity. Positive narrative pathway assertions remain separately assessed. |
| septin-native-plasma_membrane_derived_thylakoid_lumen-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plasma_membrane_derived_thylakoid_lumen-uniprot-causal-receipt.json; Actual native receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plasma_membrane_derived_thylakoid_lumen-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Exit0. Independently counted0 individual protein examples,0 GENE_OR_PROTEIN nodes and0 UniProtKB graph xrefs. Exit0 covers this empty represented scope, not complete molecular coverage or scientific validity. Positive narrative pathway assertions remain separately assessed. |
| septin-record-plasma_membrane_derived_thylakoid_membrane | data/structures/membrane_organelle/plasma_membrane_derived_thylakoid_membrane.yaml; Complete current record at 659d5d9ce7e16c8607002bf1655db2f3c652e6e1 | supports | All identity, definition, components, taxa/examples, function/source notes, discussion/history and graph fields read. Independently counted0 individual examples,0 GENE_OR_PROTEIN nodes,0 UniProtKB graph xrefs and no maintained images. Current6-edge descriptive graph adds ATP-synthase structure residence. |
| septin-original-plasma_membrane_derived_thylakoid_membrane | reviews/structured/20261022T032303Z-plasma-membrane-derived-thylakoid-membrane-audit/review.yaml; Complete immutable original YAML/Markdown pair, original findings/actions/verdict and source snapshot | supports | Old source access/checks remain historical. Every inherited finding is retained with exact predecessor. Target input changed; original graph assessment also misdescribed the old5-edge graph as including ATP residence. |
| septin-original-validation-plasma_membrane_derived_thylakoid_membrane | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/adversary-septin/original-checks.json; Actual native validate/render, exact Markdown equality and original frozen/current target hash comparison | supports | Native original validation/render exit0 and exact Markdown. Historical source target matches frozen input; current differs and is substantively refreshed. Schema validity does not certify scientific support. |
| septin-native-plasma_membrane_derived_thylakoid_membrane-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plasma_membrane_derived_thylakoid_membrane-uniprot-verify-receipt.json; Actual native receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plasma_membrane_derived_thylakoid_membrane-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0. Independently counted0 individual protein examples,0 GENE_OR_PROTEIN nodes and0 UniProtKB graph xrefs. Exit0 covers this empty represented scope, not complete molecular coverage or scientific validity. Four GO-grounded protein-complex components and their STRUCTURE graph nodes remain real molecular assertions. |
| septin-native-plasma_membrane_derived_thylakoid_membrane-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plasma_membrane_derived_thylakoid_membrane-uniprot-causal-receipt.json; Actual native receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plasma_membrane_derived_thylakoid_membrane-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Exit0. Independently counted0 individual protein examples,0 GENE_OR_PROTEIN nodes and0 UniProtKB graph xrefs. Exit0 covers this empty represented scope, not complete molecular coverage or scientific validity. Four GO-grounded protein-complex components and their STRUCTURE graph nodes remain real molecular assertions. |
| plaque-current-1 | data/structures/membrane_organelle/photosynthetic_membrane.yaml; Entire current maintained record at 659d5d9ce7e16c8607002bf1655db2f3c652e6e1; all fields, graph edges, discussions and history | supports | Photosynthetic membrane remains byte-identical to original freeze; chromatophore is stale and receives substantive current reassessment of retyped/grounded nodes and two new edges. |
| plaque-original-1 | reviews/structured/20261022T032301Z-photosynthetic-membrane-audit/review.yaml; Exact staleness-selected original YAML and deterministic native Markdown; source/evidence, assessments, checks, findings/actions and notes | supports | Immutable original natively validates/renders; all20 historical frozen inputs match its source. Historical six-edge chromatophore assessment is not a current eight-edge certification. |
| plaque-current-2 | data/structures/membrane_organelle/plasma_membrane_derived_chromatophore_membrane.yaml; Entire current maintained record at 659d5d9ce7e16c8607002bf1655db2f3c652e6e1; all fields, graph edges, discussions and history | supports | Photosynthetic membrane remains byte-identical to original freeze; chromatophore is stale and receives substantive current reassessment of retyped/grounded nodes and two new edges. |
| plaque-original-2 | reviews/structured/20261022T032301Z-plasma-membrane-derived-chromatophore-membrane-audit/review.yaml; Exact staleness-selected original YAML and deterministic native Markdown; source/evidence, assessments, checks, findings/actions and notes | supports | Immutable original natively validates/renders; all20 historical frozen inputs match its source. Historical six-edge chromatophore assessment is not a current eight-edge certification. |
| plaque-policy | .claude/skills/review-yaml-record/SKILL.md; Current skill Structured Source Cross-Checks and evidence rules reread | context_only | Positive protein and pathway assertions trigger applicability even without expression-module assertions. |
| plaque-rubric | .claude/skills/curate-yaml-record/references/review-checklist.md; Previously read exact frozen checklist, unchanged | context_only | Identity, source scope, material, mechanism and necessity evaluated separately; optional inventory gaps alone are not findings. |
| plaque-graph-rubric | .claude/skills/curate-causal-graphs/SKILL.md; Previously read exact graph contract, unchanged | context_only | Native schema permits families and protein complexes under GENE_OR_PROTEIN; retyping to STRUCTURE is not automatically a correction of an invalid prior enum. |
| plaque-schema-policy | src/cellstructuremech/schema/cellstructuremech.yaml; Exact frozen component, necessity and graph schema, unchanged | context_only | Label-only collective lipids differ from misgrounded whole membranes; local and GO whole-complex identity differs from a subunit accession. |
| plaque-history-policy | docs/CURATION.md; Previously read exact discussion/history policy, unchanged | context_only | Rationale/history are append-only; update current grounding and future-facing notes or append a resolution without erasing historical explanations. |
| plaque-context-chromatophore_cytochrome_bc1_complex | data/structures/energy_complex/chromatophore_cytochrome_bc1_complex.yaml; Identity, definition, taxonomic/function/source fields and node inventory read after exact input freeze; not an exhaustive neighbor review | context_only | Exact local whole-complex context for RC-LH1-PufX, bc1 or peripheral LH2. Neighbor histories/issues and entire mechanisms are not adjudicated or resolved. |
| plaque-context-lh2_peripheral_light_harvesting_antenna_complex | data/structures/energy_complex/lh2_peripheral_light_harvesting_antenna_complex.yaml; Identity, definition, taxonomic/function/source fields and node inventory read after exact input freeze; not an exhaustive neighbor review | context_only | Exact local whole-complex context for RC-LH1-PufX, bc1 or peripheral LH2. Neighbor histories/issues and entire mechanisms are not adjudicated or resolved. |
| plaque-context-rc_lh1_pufx_core_complex | data/structures/energy_complex/rc_lh1_pufx_core_complex.yaml; Identity, definition, taxonomic/function/source fields and node inventory read after exact input freeze; not an exhaustive neighbor review | context_only | Exact local whole-complex context for RC-LH1-PufX, bc1 or peripheral LH2. Neighbor histories/issues and entire mechanisms are not adjudicated or resolved. |
| plaque-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0034357,GO:0042717,GO:0070112,GO:0030076,GO:0009767,GO:0019684,GO:0045259,GO:0016020; Complete fresh8-term response: id/name/definition/isObsolete/synonyms/typed children | supports | GO0034357 and0042717 match generic and purple-bacterial membranes;0070112 is distinct organellar chromatophore.0019684 specifically defines oxygenic PSI/PSII light reactions.0045259 is active with exact F1-F0 complex synonym; location does not require a new whole-complex identity. |
| plaque-SL0042 | https://rest.uniprot.org/locations/SL-0042.json; Complete native location JSON definition/synonym/GO mapping | supports | Explicit plasma-derived purple-bacterial photosynthetic membrane, RC/antenna/bc1/F0F1 scope. This is localization authority, not a direct measurement of universal stoichiometry or formation necessity. |
| plaque-tax2 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2; Complete ENA taxId/scientificName/rank/lineage/alternate names | supports | Verified exact maintained taxon identity and strain hierarchy. PCC6803/Kazusa, PCC7942, Cereibacter species and2.4.1/ATCC17025 strains remain distinct; taxonomy alone does not establish experimental localization or prevalence. |
| plaque-tax1063 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1063; Complete ENA taxId/scientificName/rank/lineage/alternate names | supports | Verified exact maintained taxon identity and strain hierarchy. PCC6803/Kazusa, PCC7942, Cereibacter species and2.4.1/ATCC17025 strains remain distinct; taxonomy alone does not establish experimental localization or prevalence. |
| plaque-tax272943 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/272943; Complete ENA taxId/scientificName/rank/lineage/alternate names | supports | Verified exact maintained taxon identity and strain hierarchy. PCC6803/Kazusa, PCC7942, Cereibacter species and2.4.1/ATCC17025 strains remain distinct; taxonomy alone does not establish experimental localization or prevalence. |
| plaque-tax349102 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/349102; Complete ENA taxId/scientificName/rank/lineage/alternate names | supports | Verified exact maintained taxon identity and strain hierarchy. PCC6803/Kazusa, PCC7942, Cereibacter species and2.4.1/ATCC17025 strains remain distinct; taxonomy alone does not establish experimental localization or prevalence. |
| plaque-tax1111708 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1111708; Complete ENA taxId/scientificName/rank/lineage/alternate names | supports | Verified exact maintained taxon identity and strain hierarchy. PCC6803/Kazusa, PCC7942, Cereibacter species and2.4.1/ATCC17025 strains remain distinct; taxonomy alone does not establish experimental localization or prevalence. |
| plaque-tax1117 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1117; Complete ENA taxId/scientificName/rank/lineage/alternate names Same-PR public snapshot independently reread; actual initial fetch timestamp/hash retained, not a new request. | supports | Verified exact maintained taxon identity and strain hierarchy. PCC6803/Kazusa, PCC7942, Cereibacter species and2.4.1/ATCC17025 strains remain distinct; taxonomy alone does not establish experimental localization or prevalence. |
| plaque-tax1148 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1148; Complete ENA taxId/scientificName/rank/lineage/alternate names Same-PR public snapshot independently reread; actual initial fetch timestamp/hash retained, not a new request. | supports | Verified exact maintained taxon identity and strain hierarchy. PCC6803/Kazusa, PCC7942, Cereibacter species and2.4.1/ATCC17025 strains remain distinct; taxonomy alone does not establish experimental localization or prevalence. |
| plaque-tax1140 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1140; Complete ENA taxId/scientificName/rank/lineage/alternate names Same-PR public snapshot independently reread; actual initial fetch timestamp/hash retained, not a new request. | supports | Verified exact maintained taxon identity and strain hierarchy. PCC6803/Kazusa, PCC7942, Cereibacter species and2.4.1/ATCC17025 strains remain distinct; taxonomy alone does not establish experimental localization or prevalence. |
| plaque-casella2017-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1016%2Fj.molp.2017.09.019&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact bibliographic metadata and complete deposited PRIMARY abstract | supports | Exact title/year/DOI/PMID and declared experimental context verified. Nielsen is abstract-only here; other detailed scopes are bound to separately inspected source bodies. |
| plaque-bahatyrova2004-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038%2Fnature02823&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact bibliographic metadata and complete deposited PRIMARY abstract | supports | Exact title/year/DOI/PMID and declared experimental context verified. Nielsen is abstract-only here; other detailed scopes are bound to separately inspected source bodies. |
| plaque-comayras2005-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1074%2Fjbc.M412088200&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact bibliographic metadata and complete deposited PRIMARY abstract | supports | Exact title/year/DOI/PMID and declared experimental context verified. Nielsen is abstract-only here; other detailed scopes are bound to separately inspected source bodies. |
| plaque-feniouk2002-pmid | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11867431+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact bibliographic metadata and complete deposited PRIMARY abstract | supports | Exact title/year/DOI/PMID and declared experimental context verified. Nielsen is abstract-only here; other detailed scopes are bound to separately inspected source bodies. |
| plaque-nielsen2016-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038%2Fncomms12454&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact bibliographic metadata and complete deposited PRIMARY abstract | supports | Exact title/year/DOI/PMID and declared experimental context verified. Nielsen is abstract-only here; other detailed scopes are bound to separately inspected source bodies. |
| plaque-sui2021-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1146%2Fannurev-biophys-062920-063657&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact metadata and complete deposited SECONDARY REVIEW abstract | supports | Phycobilisome pigment-protein/linker organization and energy transfer provide boundary context only; no full Sui body or universal integral-membrane antenna assertion. |
| plaque-feniouk2002-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1016%2FS0006-3495%2802%2975470-2&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact DOI first-page search returned0; no body evidence | context_only | Initial exact DOI search produced no indexed hit in this request. Later exact PMID11867431 uniquely resolves the cited paper; zero search hits are not source nonexistence. |
| plaque-casella2017-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC5683893.1/PMC5683893.1.xml; Genuine PMC5683893 JATS Results2.1–2.4 including embeddedFig1–8 captions; Methods4.1/4.5/4.7/4.8. No figure pixels, supplements, rawdata, remaining Methods or Discussion audited | supports | Actual S.elongatus PCC7942 wild type and tagged PsaE/CP47/PetA/ATPbeta; BG11,30C and stated illumination. Native-membrane AFM and live microscopy/FRAP do not establish PCC6803 experiments. Some b6f particle assignment is tentative; no blanket particle identity claim. |
| plaque-bahatyrova2004-pdf | https://eprints.whiterose.ac.uk/id/eprint/102/1/huntercn1.pdf; Genuine university-hosted PDF pp1058–1061 complete scientific main text/Methods/Fig1–3 captions; adjacent unrelated article matter excluded. No pixels/supplements | supports | R.sphaeroides NCIB8253 native isolated membranes show RC-LH1-PufX arrays and LH2 contacts/clusters. Preparation/AFM context is retained. bc1 and ATPase positions were not localized by this AFM; PufX is not directly resolved. Illustrative organization is not universal architecture or an assembly-necessity test. |
| plaque-feniouk2002-author-pdf | https://www.home.uni-osnabrueck.de/wjunge/public/230.pdf; Genuine author-hosted PDF pp1115–1121 scientific main text, Methods, Results/Discussion, Fig1–6 captions/Table1; no figure pixels/rawdata | supports | R.capsulatus B10 malate/photoheterotrophic cultures30C; isolated chromatophores. Flash-induced522nm electrochromic voltage shows RC and slower bc1 charge-transfer phases and inhibitor-sensitive ATPase proton flux. Coupling supports PMF use; direct luciferase ATP-product measurements cited from earlier work are not certified as new measurements in this paper. |
| plaque-comayras-browser-initial | https://www.researchgate.net/publication/8099149_Functional_consequences_of_the_organization_of_the_photosynthetic_apparatus_in_Rhodobacter_sphaeroides_I_Quinone_domains_and_excitation_transfer_in_chromatophores_and_reaction_centerantenna_complexes; Retained browser author-upload primary excerpt; initial lines0–626 and overlapping410–1241 include Introduction, Methods and initialResults; no complete body or pixels. Timestamp is immediately-after-access receipt time; native HTTP status not supplied. | supports | Ga-strain excitation/quinone-pool work. Pool assay inhibits bc1 and removes voltage/pH gradients; normal cyclic routing is contextual, not a directly measured unperturbed PMF result. |
| plaque-comayras-browser-methods | https://www.researchgate.net/publication/8099149_Functional_consequences_of_the_organization_of_the_photosynthetic_apparatus_in_Rhodobacter_sphaeroides_I_Quinone_domains_and_excitation_transfer_in_chromatophores_and_reaction_centerantenna_complexes; Retained browser author-upload primary excerpt; initial lines0–626 and overlapping410–1241 include Introduction, Methods and initialResults; no complete body or pixels. Timestamp is immediately-after-access receipt time; native HTTP status not supplied. | supports | Ga-strain excitation/quinone-pool work. Pool assay inhibits bc1 and removes voltage/pH gradients; normal cyclic routing is contextual, not a directly measured unperturbed PMF result. |
| plaque-perez2024-delivered | https://www.annualreviews.org/docserver/ahah/fulltext/cellbio/40/1/annurev-cellbio-120823-022747.html?expires=1793737002&amp;id=id&amp;accname=guest&amp;checksum=47EAFDAB41E06430970416431EF37629; SECONDARY REVIEW publisher-delivered body: Introduction, evolutionary overview, Building Blocks, Lipids and Electron Transport Chain Complexes plus embeddedFig1/2 captions; not remaining body or pixels Same-PR public snapshot independently reread; actual initial fetch timestamp/hash retained, not a new request. | supports | Supports broad oxygenic membrane/lipid/photosystem/electron-carrier context and Gloeobacter exception. Its oxygenic pathway is not purple-bacterial photochemistry or experimental depletion/formation proof. |
| plaque-protein-P29254 | https://rest.uniprot.org/uniprotkb/P29254.json; Fresh native accession: primary name, gene/aliases/loci, exact organism/reviewed status, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY and InterPro cross-references | supports | Reviewed identity agrees with declared example. Native annotations distinguish experimental citations from HAMAP/by-similarity inference; family cross-references are contextual and not substitutes for whole-complex grounding. No formation necessity or exhaustive stoichiometry is inferred. |
| plaque-protein-P0C0Y8 | https://rest.uniprot.org/uniprotkb/P0C0Y8.json; Fresh native accession: primary name, gene/aliases/loci, exact organism/reviewed status, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY and InterPro cross-references | supports | Reviewed identity agrees with declared example. Native annotations distinguish experimental citations from HAMAP/by-similarity inference; family cross-references are contextual and not substitutes for whole-complex grounding. No formation necessity or exhaustive stoichiometry is inferred. |
| plaque-protein-P0C0Y9 | https://rest.uniprot.org/uniprotkb/P0C0Y9.json; Fresh native accession: primary name, gene/aliases/loci, exact organism/reviewed status, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY and InterPro cross-references | supports | Reviewed identity agrees with declared example. Native annotations distinguish experimental citations from HAMAP/by-similarity inference; family cross-references are contextual and not substitutes for whole-complex grounding. No formation necessity or exhaustive stoichiometry is inferred. |
| plaque-protein-P16033 | https://rest.uniprot.org/uniprotkb/P16033.json; Fresh native accession: primary name, gene/aliases/loci, exact organism/reviewed status, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY and InterPro cross-references | supports | Reviewed identity agrees with declared example. Native annotations distinguish experimental citations from HAMAP/by-similarity inference; family cross-references are contextual and not substitutes for whole-complex grounding. No formation necessity or exhaustive stoichiometry is inferred. |
| plaque-protein-P26287 | https://rest.uniprot.org/uniprotkb/P26287.json; Fresh native accession: primary name, gene/aliases/loci, exact organism/reviewed status, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY and InterPro cross-references | supports | Reviewed identity agrees with declared example. Native annotations distinguish experimental citations from HAMAP/by-similarity inference; family cross-references are contextual and not substitutes for whole-complex grounding. No formation necessity or exhaustive stoichiometry is inferred. |
| plaque-protein-Q57038 | https://rest.uniprot.org/uniprotkb/Q57038.json; Fresh native accession: primary name, gene/aliases/loci, exact organism/reviewed status, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY and InterPro cross-references | supports | Reviewed identity agrees with declared example. Native annotations distinguish experimental citations from HAMAP/by-similarity inference; family cross-references are contextual and not substitutes for whole-complex grounding. No formation necessity or exhaustive stoichiometry is inferred. |
| plaque-protein-Q02761 | https://rest.uniprot.org/uniprotkb/Q02761.json; Fresh native accession: primary name, gene/aliases/loci, exact organism/reviewed status, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY and InterPro cross-references | supports | Reviewed identity agrees with declared example. Native annotations distinguish experimental citations from HAMAP/by-similarity inference; family cross-references are contextual and not substitutes for whole-complex grounding. No formation necessity or exhaustive stoichiometry is inferred. |
| plaque-protein-Q02760 | https://rest.uniprot.org/uniprotkb/Q02760.json; Fresh native accession: primary name, gene/aliases/loci, exact organism/reviewed status, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY and InterPro cross-references | supports | Reviewed identity agrees with declared example. Native annotations distinguish experimental citations from HAMAP/by-similarity inference; family cross-references are contextual and not substitutes for whole-complex grounding. No formation necessity or exhaustive stoichiometry is inferred. |
| plaque-protein-P0C0Y0 | https://rest.uniprot.org/uniprotkb/P0C0Y0.json; Fresh native accession: primary name, gene/aliases/loci, exact organism/reviewed status, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY and InterPro cross-references | supports | Reviewed identity agrees with declared example. Native annotations distinguish experimental citations from HAMAP/by-similarity inference; family cross-references are contextual and not substitutes for whole-complex grounding. No formation necessity or exhaustive stoichiometry is inferred. |
| plaque-protein-P0C0Y2 | https://rest.uniprot.org/uniprotkb/P0C0Y2.json; Fresh native accession: primary name, gene/aliases/loci, exact organism/reviewed status, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY and InterPro cross-references | supports | Reviewed identity agrees with declared example. Native annotations distinguish experimental citations from HAMAP/by-similarity inference; family cross-references are contextual and not substitutes for whole-complex grounding. No formation necessity or exhaustive stoichiometry is inferred. |
| plaque-protein-A4WUM7 | https://rest.uniprot.org/uniprotkb/A4WUM7.json; Fresh native accession: primary name, gene/aliases/loci, exact organism/reviewed status, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY and InterPro cross-references | supports | Reviewed identity agrees with declared example. Native annotations distinguish experimental citations from HAMAP/by-similarity inference; family cross-references are contextual and not substitutes for whole-complex grounding. No formation necessity or exhaustive stoichiometry is inferred. |
| plaque-protein-Q3J433 | https://rest.uniprot.org/uniprotkb/Q3J433.json; Fresh native accession: primary name, gene/aliases/loci, exact organism/reviewed status, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY and InterPro cross-references | supports | Reviewed identity agrees with declared example. Native annotations distinguish experimental citations from HAMAP/by-similarity inference; family cross-references are contextual and not substitutes for whole-complex grounding. No formation necessity or exhaustive stoichiometry is inferred. |
| plaque-protein-Q3IZ12 | https://rest.uniprot.org/uniprotkb/Q3IZ12.json; Fresh native accession: primary name, gene/aliases/loci, exact organism/reviewed status, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY and InterPro cross-references | supports | Reviewed identity agrees with declared example. Native annotations distinguish experimental citations from HAMAP/by-similarity inference; family cross-references are contextual and not substitutes for whole-complex grounding. No formation necessity or exhaustive stoichiometry is inferred. |
| plaque-protein-Q3IZ13 | https://rest.uniprot.org/uniprotkb/Q3IZ13.json; Fresh native accession: primary name, gene/aliases/loci, exact organism/reviewed status, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY and InterPro cross-references | supports | Reviewed identity agrees with declared example. Native annotations distinguish experimental citations from HAMAP/by-similarity inference; family cross-references are contextual and not substitutes for whole-complex grounding. No formation necessity or exhaustive stoichiometry is inferred. |
| plaque-reviewed-genes-1111708 | https://rest.uniprot.org/uniprotkb/search?query=%28reviewed%3Atrue%29+AND+%28taxonomy_id%3A1111708%29+AND+%28gene_exact%3ApsaA+OR+gene_exact%3ApsbA+OR+gene_exact%3ApsbA2+OR+gene_exact%3ApsbA3+OR+gene_exact%3ApetA+OR+gene_exact%3ApetB%29&amp;format=json&amp;size=500; All returned accession/gene/taxon rows inspected; exact organism filtering after taxonomic-descendant query | supports | Four Kazusa and19 Cereibacter-descendant rows. Current examples remain unique under each exact asserted gene/taxon pairing; descendants are not collapsed into species-level duplicates. P16033 covers psbA2 andpsbA3 loci, not a claim that the genome contains only one psbA locus. |
| plaque-reviewed-genes-1063 | https://rest.uniprot.org/uniprotkb/search?query=%28reviewed%3Atrue%29+AND+%28taxonomy_id%3A1063%29+AND+%28gene_exact%3ApufL+OR+gene_exact%3ApufM+OR+gene_exact%3ApucA+OR+gene_exact%3ApucB+OR+gene_exact%3ApetB+OR+gene_exact%3AfbcB+OR+gene_exact%3ApetC+OR+gene_exact%3AfbcC+OR+gene_exact%3AatpA+OR+gene_exact%3AatpB+OR+gene_exact%3AatpD+OR+gene_exact%3AatpE%29&amp;format=json&amp;size=500; All returned accession/gene/taxon rows inspected; exact organism filtering after taxonomic-descendant query | supports | Four Kazusa and19 Cereibacter-descendant rows. Current examples remain unique under each exact asserted gene/taxon pairing; descendants are not collapsed into species-level duplicates. P16033 covers psbA2 andpsbA3 loci, not a claim that the genome contains only one psbA locus. |
| plaque-PMID11788579 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11788579+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact MED metadata and complete deposited PRIMARY abstract; no full paper/pixels | supports | Cited PCC6803 PSII or b6f composition/localization experiment matches bounded native annotation context. Tagging, isolated complexes and mutants remain study-specific; abstracts do not certify every full-paper mechanism or strain-general necessity. |
| plaque-PMID12069591 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12069591+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact MED metadata and complete deposited PRIMARY abstract; no full paper/pixels | supports | Cited PCC6803 PSII or b6f composition/localization experiment matches bounded native annotation context. Tagging, isolated complexes and mutants remain study-specific; abstracts do not certify every full-paper mechanism or strain-general necessity. |
| plaque-PMID19577535 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A19577535+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact MED metadata and complete deposited PRIMARY abstract; no full paper/pixels | supports | Cited PCC6803 PSII or b6f composition/localization experiment matches bounded native annotation context. Tagging, isolated complexes and mutants remain study-specific; abstracts do not certify every full-paper mechanism or strain-general necessity. |
| plaque-PMID34937700 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A34937700+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact MED metadata and complete deposited PRIMARY abstract; no full paper/pixels | supports | Cited PCC6803 PSII or b6f composition/localization experiment matches bounded native annotation context. Tagging, isolated complexes and mutants remain study-specific; abstracts do not certify every full-paper mechanism or strain-general necessity. |
| plaque-PMID35726684 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A35726684+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact MED metadata and complete deposited PRIMARY abstract; no full paper/pixels | supports | Cited PCC6803 PSII or b6f composition/localization experiment matches bounded native annotation context. Tagging, isolated complexes and mutants remain study-specific; abstracts do not certify every full-paper mechanism or strain-general necessity. |
| plaque-catalogue | https://imodulondb.org/api/datasets; Complete official catalogue independently inspected across every returned organism/dataset pair Same-PR public snapshot independently reread; actual initial fetch timestamp/hash retained, not a new request. | supports | S.elongatus/elprecise300 is available, but no Synechocystis6803, Cereibacter/Rhodobacter sphaeroides or R.capsulatus dataset. PCC7942 context is relevant only to that source organism, not a replacement for canonicalPCC6803 or purple-host evidence. |
| plaque-adapter-search-photosystem | https://imodulondb.org/api/search?organism=s_elongatus&amp;dataset=elprecise300&amp;query=photosystem&amp;limit=50; Complete bounded official gene/module search response independently reread Same-PR public snapshot independently reread; actual initial fetch timestamp/hash retained, not a new request. | supports | Matching molecular pathway context in PCC7942 source dataset only. Search hits are not structural membership, assembly requirements or cross-species evidence. |
| plaque-adapter-search-cytochrome-b6 | https://imodulondb.org/api/search?organism=s_elongatus&amp;dataset=elprecise300&amp;query=cytochrome+b6&amp;limit=50; Complete bounded official gene/module search response independently reread Same-PR public snapshot independently reread; actual initial fetch timestamp/hash retained, not a new request. | supports | Matching molecular pathway context in PCC7942 source dataset only. Search hits are not structural membership, assembly requirements or cross-species evidence. |
| plaque-adapter-search-ATP-synthase | https://imodulondb.org/api/search?organism=s_elongatus&amp;dataset=elprecise300&amp;query=ATP+synthase&amp;limit=50; Complete bounded official gene/module search response independently reread Same-PR public snapshot independently reread; actual initial fetch timestamp/hash retained, not a new request. | supports | Matching molecular pathway context in PCC7942 source dataset only. Search hits are not structural membership, assembly requirements or cross-species evidence. |
| plaque-adapter-search-thylakoid | https://imodulondb.org/api/search?organism=s_elongatus&amp;dataset=elprecise300&amp;query=thylakoid&amp;limit=50; Complete bounded official gene/module search response independently reread Same-PR public snapshot independently reread; actual initial fetch timestamp/hash retained, not a new request. | supports | Matching molecular pathway context in PCC7942 source dataset only. Search hits are not structural membership, assembly requirements or cross-species evidence. |
| plaque-adapter-gene-Synpcc7942_2049 | https://imodulondb.org/api/genes/s_elongatus/elprecise300/Synpcc7942_2049; Complete selected native gene identity/product/string taxon metadata, no inferred interaction Same-PR public snapshot independently reread; actual initial fetch timestamp/hash retained, not a new request. | supports | Synpcc7942 identifiers and STRING tax1140 establish exact PCC7942 context; selectedpsaA/psbA1/petB/atpA are not PCC6803 or purple-bacterial accession replacements. |
| plaque-adapter-gene-Synpcc7942_2049-modules | https://imodulondb.org/api/genes/s_elongatus/elprecise300/Synpcc7942_2049/imodulons; All57 selected-gene module rows and threshold flags inspected Same-PR public snapshot independently reread; actual initial fetch timestamp/hash retained, not a new request. | supports | psaA2049 andpetB2331 each pass only module38 threshold. psbA1_0424 andatpA0336 have no true flags among these57rows. Below-threshold membership is not biological absence or lack of a photosystem/ATPase. |
| plaque-adapter-gene-Synpcc7942_0424 | https://imodulondb.org/api/genes/s_elongatus/elprecise300/Synpcc7942_0424; Complete selected native gene identity/product/string taxon metadata, no inferred interaction Same-PR public snapshot independently reread; actual initial fetch timestamp/hash retained, not a new request. | supports | Synpcc7942 identifiers and STRING tax1140 establish exact PCC7942 context; selectedpsaA/psbA1/petB/atpA are not PCC6803 or purple-bacterial accession replacements. |
| plaque-adapter-gene-Synpcc7942_0424-modules | https://imodulondb.org/api/genes/s_elongatus/elprecise300/Synpcc7942_0424/imodulons; All57 selected-gene module rows and threshold flags inspected Same-PR public snapshot independently reread; actual initial fetch timestamp/hash retained, not a new request. | supports | psaA2049 andpetB2331 each pass only module38 threshold. psbA1_0424 andatpA0336 have no true flags among these57rows. Below-threshold membership is not biological absence or lack of a photosystem/ATPase. |
| plaque-adapter-gene-Synpcc7942_2331 | https://imodulondb.org/api/genes/s_elongatus/elprecise300/Synpcc7942_2331; Complete selected native gene identity/product/string taxon metadata, no inferred interaction Same-PR public snapshot independently reread; actual initial fetch timestamp/hash retained, not a new request. | supports | Synpcc7942 identifiers and STRING tax1140 establish exact PCC7942 context; selectedpsaA/psbA1/petB/atpA are not PCC6803 or purple-bacterial accession replacements. |
| plaque-adapter-gene-Synpcc7942_2331-modules | https://imodulondb.org/api/genes/s_elongatus/elprecise300/Synpcc7942_2331/imodulons; All57 selected-gene module rows and threshold flags inspected Same-PR public snapshot independently reread; actual initial fetch timestamp/hash retained, not a new request. | supports | psaA2049 andpetB2331 each pass only module38 threshold. psbA1_0424 andatpA0336 have no true flags among these57rows. Below-threshold membership is not biological absence or lack of a photosystem/ATPase. |
| plaque-adapter-gene-Synpcc7942_0336 | https://imodulondb.org/api/genes/s_elongatus/elprecise300/Synpcc7942_0336; Complete selected native gene identity/product/string taxon metadata, no inferred interaction Same-PR public snapshot independently reread; actual initial fetch timestamp/hash retained, not a new request. | supports | Synpcc7942 identifiers and STRING tax1140 establish exact PCC7942 context; selectedpsaA/psbA1/petB/atpA are not PCC6803 or purple-bacterial accession replacements. |
| plaque-adapter-gene-Synpcc7942_0336-modules | https://imodulondb.org/api/genes/s_elongatus/elprecise300/Synpcc7942_0336/imodulons; All57 selected-gene module rows and threshold flags inspected Same-PR public snapshot independently reread; actual initial fetch timestamp/hash retained, not a new request. | supports | psaA2049 andpetB2331 each pass only module38 threshold. psbA1_0424 andatpA0336 have no true flags among these57rows. Below-threshold membership is not biological absence or lack of a photosystem/ATPase. |
| plaque-adapter-module-1 | https://imodulondb.org/api/imodulons/s_elongatus/elprecise300/1; Native module identity/category/threshold and complete21/44 member ID lists inspected; activity arrays counted but condition effects not analyzed; AI summaries excluded Same-PR public snapshot independently reread; actual initial fetch timestamp/hash retained, not a new request. | supports | PSII module1 andPhotosystems38 are dataset expression components. They cross-check pathway context without certifying physical complexes, direct regulation, universality or necessity. |
| plaque-adapter-module-38 | https://imodulondb.org/api/imodulons/s_elongatus/elprecise300/38; Native module identity/category/threshold and complete21/44 member ID lists inspected; activity arrays counted but condition effects not analyzed; AI summaries excluded Same-PR public snapshot independently reread; actual initial fetch timestamp/hash retained, not a new request. | supports | PSII module1 andPhotosystems38 are dataset expression components. They cross-check pathway context without certifying physical complexes, direct regulation, universality or necessity. |
| plaque-historical-runner | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Retained historical00:49Z failed runner and verified stdout/stderr | context_only | PermissionError accessing pyvenv.cfg; no new runner invocation or success. Current official-source fallback and actual dataset checks are separate. |
| plaque-original-checks | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/adversary-plaque/original-checks.json; Actual native original validate/render commands and historical40 input hashes | supports | Both immutable pairs validate/render exactly and20 historical inputs each match. Photosynthetic target unchanged; chromatophore target stale, refreshed separately. |
| plaque-native-photosynthetic_membrane-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/photosynthetic_membrane.yaml --verify; Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/photosynthetic_membrane-uniprot-verify-receipt.json and logSHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Eight reviewed examples and2COVERED typed nodes. Native coverage checks do not certify every scientific claim, formation necessity or current source attribution. |
| plaque-native-photosynthetic_membrane-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/photosynthetic_membrane.yaml --causal-graphs; Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/photosynthetic_membrane-uniprot-causal-receipt.json and logSHA256 4cdd749f721d4255905a1b805650377d703f536b2323e1a71e2fd7dd809ccd34 | supports | Eight reviewed examples and2COVERED typed nodes. Native coverage checks do not certify every scientific claim, formation necessity or current source attribution. |
| plaque-native-plasma_membrane_derived_chromatophore_membrane-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plasma_membrane_derived_chromatophore_membrane.yaml --verify; Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plasma_membrane_derived_chromatophore_membrane-uniprot-verify-receipt.json and logSHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Six reviewed examples but0GENE_OR_PROTEIN nodes after current retyping; this is not an empty accession inventory. Native coverage checks do not certify every scientific claim, formation necessity or current source attribution. |
| plaque-native-plasma_membrane_derived_chromatophore_membrane-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plasma_membrane_derived_chromatophore_membrane.yaml --causal-graphs; Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plasma_membrane_derived_chromatophore_membrane-uniprot-causal-receipt.json and logSHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Six reviewed examples but0GENE_OR_PROTEIN nodes after current retyping; this is not an empty accession inventory. Native coverage checks do not certify every scientific claim, formation necessity or current source attribution. |
| micro-policy | .claude/skills/review-yaml-record/SKILL.md; Native skill/profile/config/checklist and structured-source contract | context_only | Whole positive molecular/pathway claims trigger applicability, regardless of empty inventories; mere paper/model context and explicitly withheld mechanisms do not create a claim. |
| micro-component-policy | src/cellstructuremech/schema/cellstructuremech.yaml; ComponentTypeEnum/StructuralComponent plus native CURATION component identity guidance | context_only | Whole anatomical membrane is distinct from molecular lipid material. Reviewed-label-only collective bilayer is valid; structural-subpart representation is not categorically forbidden. Formation necessity of individual molecules is not inferred from topology. |
| micro-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Source-specific edge, class identity/component join and graph-scope contract | context_only | Descriptive topology/class relationships are NONMECHANISTIC; lineage-specific protein mechanisms and optional inventories are not required on generic records. |
| micro-discussion-policy | docs/CURATION.md; Discussion305–324 and component/taxon guidance | context_only | Rationale is append-only provenance. Source-neutral material TODOs remain open; exact whole-membrane GO does not supply a chemical lipid identity. |
| micro-record-plastid | data/structures/membrane_organelle/plastid.yaml; Entire current record including all history/discussions, evidence, taxon/canonical context, material rows and every graph node/edge | supports | Complete independently read unchanged record; original frozen target matches. No record mutation. |
| micro-prior-plastid | reviews/structured/20261022T032303Z-plastid-audit/review.yaml; Original identity/source inputs/checks/evidence/read scopes/assessments/findings/actions/limits and deterministic Markdown | context_only | Original needs_curation; one inherited major F1. Explicit expression-only adapter exclusion present. Historical accesses/checks remain historical. |
| micro-native-plastid-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid.yaml --verify; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0; independently counted zero protein_examples and zero typed GENE_OR_PROTEIN nodes. Generic verify-success does not establish complete proteome/family coverage, translocon identity or biological necessity. |
| micro-native-plastid-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid.yaml --causal-graphs; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Actual exit0; independently counted zero protein_examples and zero typed GENE_OR_PROTEIN nodes. Generic verify-success does not establish complete proteome/family coverage, translocon identity or biological necessity. |
| micro-record-plastid_envelope | data/structures/membrane_organelle/plastid_envelope.yaml; Entire current record including all history/discussions, evidence, taxon/canonical context, material rows and every graph node/edge | supports | Complete independently read unchanged record; original frozen target matches. No record mutation. |
| micro-prior-plastid_envelope | reviews/structured/20261022T032304Z-plastid-envelope-audit/review.yaml; Original identity/source inputs/checks/evidence/read scopes/assessments/findings/actions/limits and deterministic Markdown | context_only | Original needs_curation; one inherited major F1. Explicit expression-only adapter exclusion present. Historical accesses/checks remain historical. |
| micro-native-plastid_envelope-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid_envelope-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_envelope.yaml --verify; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid_envelope-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0; independently counted zero protein_examples and zero typed GENE_OR_PROTEIN nodes. Generic verify-success does not establish complete proteome/family coverage, translocon identity or biological necessity. |
| micro-native-plastid_envelope-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid_envelope-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_envelope.yaml --causal-graphs; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid_envelope-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Actual exit0; independently counted zero protein_examples and zero typed GENE_OR_PROTEIN nodes. Generic verify-success does not establish complete proteome/family coverage, translocon identity or biological necessity. |
| micro-record-plastid_inner_membrane | data/structures/membrane_organelle/plastid_inner_membrane.yaml; Entire current record including all history/discussions, evidence, taxon/canonical context, material rows and every graph node/edge | supports | Complete independently read unchanged record; original frozen target matches. No record mutation. |
| micro-prior-plastid_inner_membrane | reviews/structured/20261022T032305Z-plastid-inner-membrane-audit/review.yaml; Original identity/source inputs/checks/evidence/read scopes/assessments/findings/actions/limits and deterministic Markdown | context_only | Original pass_with_limitations; no findings/actions. Explicit expression-only adapter exclusion present. Historical accesses/checks remain historical. |
| micro-native-plastid_inner_membrane-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid_inner_membrane-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_inner_membrane.yaml --verify; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid_inner_membrane-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0; independently counted zero protein_examples and zero typed GENE_OR_PROTEIN nodes. Generic verify-success does not establish complete proteome/family coverage, translocon identity or biological necessity. |
| micro-native-plastid_inner_membrane-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid_inner_membrane-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_inner_membrane.yaml --causal-graphs; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid_inner_membrane-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Actual exit0; independently counted zero protein_examples and zero typed GENE_OR_PROTEIN nodes. Generic verify-success does not establish complete proteome/family coverage, translocon identity or biological necessity. |
| micro-record-plastid_intermembrane_space | data/structures/membrane_organelle/plastid_intermembrane_space.yaml; Entire current record including all history/discussions, evidence, taxon/canonical context, material rows and every graph node/edge | supports | Complete independently read unchanged record; original frozen target matches. No record mutation. |
| micro-prior-plastid_intermembrane_space | reviews/structured/20261022T032305Z-plastid-intermembrane-space-audit/review.yaml; Original identity/source inputs/checks/evidence/read scopes/assessments/findings/actions/limits and deterministic Markdown | context_only | Original pass_with_limitations; no findings/actions. Explicit expression-only adapter exclusion present. Historical accesses/checks remain historical. |
| micro-native-plastid_intermembrane_space-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid_intermembrane_space-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_intermembrane_space.yaml --verify; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid_intermembrane_space-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0; independently counted zero protein_examples and zero typed GENE_OR_PROTEIN nodes. Generic verify-success does not establish complete proteome/family coverage, translocon identity or biological necessity. |
| micro-native-plastid_intermembrane_space-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid_intermembrane_space-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_intermembrane_space.yaml --causal-graphs; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid_intermembrane_space-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Actual exit0; independently counted zero protein_examples and zero typed GENE_OR_PROTEIN nodes. Generic verify-success does not establish complete proteome/family coverage, translocon identity or biological necessity. |
| micro-record-plastid_membrane | data/structures/membrane_organelle/plastid_membrane.yaml; Entire current record including all history/discussions, evidence, taxon/canonical context, material rows and every graph node/edge | supports | Complete independently read unchanged record; original frozen target matches. No record mutation. |
| micro-prior-plastid_membrane | reviews/structured/20261022T032306Z-plastid-membrane-audit/review.yaml; Original identity/source inputs/checks/evidence/read scopes/assessments/findings/actions/limits and deterministic Markdown | context_only | Original pass_with_limitations; no findings/actions. Explicit expression-only adapter exclusion present. Historical accesses/checks remain historical. |
| micro-native-plastid_membrane-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid_membrane-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_membrane.yaml --verify; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid_membrane-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0; independently counted zero protein_examples and zero typed GENE_OR_PROTEIN nodes. Generic verify-success does not establish complete proteome/family coverage, translocon identity or biological necessity. |
| micro-native-plastid_membrane-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid_membrane-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_membrane.yaml --causal-graphs; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid_membrane-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Actual exit0; independently counted zero protein_examples and zero typed GENE_OR_PROTEIN nodes. Generic verify-success does not establish complete proteome/family coverage, translocon identity or biological necessity. |
| micro-neighbor-plastid_stroma | data/structures/membrane_organelle/plastid_stroma.yaml; Complete frozen boundary neighbor, only compartment distinction assessed | context_only | Stroma is matrix/ground substance distinct from IMS; outer membrane is cytoplasm-facing bilayer. Neighbor biological findings, applicability and history/issues are not terminally disposed. |
| micro-neighbor-plastid_outer_membrane | data/structures/membrane_organelle/plastid_outer_membrane.yaml; Complete frozen boundary neighbor, only compartment distinction assessed | context_only | Stroma is matrix/ground substance distinct from IMS; outer membrane is cytoplasm-facing bilayer. Neighbor biological findings, applicability and history/issues are not terminally disposed. |
| micro-original-pairs | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/adversary-microtubule/original-checks.json; Five actual native validates and five render --content exact comparisons | supports | All five original YAMLs validate and Markdown render exactly. |
| micro-original-inputs | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/adversary-microtubule/original-frozen-inputs.json; All75 historical frozen input entries at original retained source | supports | All historical hashes verify; own five current target hashes unchanged. Historical hashing does not constitute new scientific judgments of unfrozen neighbors. |
| micro-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009536,GO:0009526,GO:0043231,GO:0005737,GO:0042170,GO:0009532,GO:0031967,GO:0009527,GO:0009528,GO:0009529,GO:0016020,GO:0055035,GO:0033113,GO:0160211; All14 exact requested entries: active id/name/definition/synonyms and typed children; unrelated broad-cytoplasm children not treated as evidence | supports | Exact whole/envelope/inner/IMS/generic identities verified. GO0043231 is_a plastid and cytoplasm part_of plastid typed children; plastid stroma/envelope/membrane parts explicit. Envelope includes IMS/generic membrane; GO0042170 explicitly has outer,inner,thylakoid,cyanelle,apicoplast is_a children despite envelope-focused definition. No is_a/parthood conflation. Whole membrane GO remains anatomical, not chemical lipid. |
| micro-go0042170-isa | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0042170/ancestors?relations=is_a; Complete exact-term ancestors request relations=is_a | supports | GO0042170 has GO0016020 membrane ancestry; direct typed children separately support exact membrane classes. No direct parthood inferred from transitive is_a. |
| micro-SL0209 | https://rest.uniprot.org/locations/SL-0209.json; Full native location identity/definition/synonyms/GO mapping and immediate/nested hierarchy; statistics not biological census | supports | Exact plastidGO9536 mapping and photosynthetic/nonphotosynthetic context; no universal photosynthetic function or membrane count. |
| micro-SL0210 | https://rest.uniprot.org/locations/SL-0210.json; Full native location identity/definition/synonyms/GO mapping and immediate/nested hierarchy; statistics not biological census | supports | Exact envelopeGO9526/synonym and inner+outer+IMS definition; plastid parthood. |
| micro-SL0211 | https://rest.uniprot.org/locations/SL-0211.json; Full native location identity/definition/synonyms/GO mapping and immediate/nested hierarchy; statistics not biological census | supports | Exact innerGO9528/three synonyms; stroma/IMS separation, generic-membrane hierarchy; nestedSL0213 includes outer/inner/thylakoid fallback scope. |
| micro-SL0212 | https://rest.uniprot.org/locations/SL-0212.json; Full native location identity/definition/synonyms/GO mapping and immediate/nested hierarchy; statistics not biological census | supports | Exact IMSGO9529/synonym, envelope parthood and between-inner/outer definition; not stroma or bilayer. |
| micro-SL0214 | https://rest.uniprot.org/locations/SL-0214.json; Full native location identity/definition/synonyms/GO mapping and immediate/nested hierarchy; statistics not biological census | supports | Exact outerGO9527/three synonyms and cytoplasm-facing definition; generic-membrane hierarchy. |
| micro-tax2759 | https://rest.uniprot.org/taxonomy/2759.json; Native identity/rank/active/parent/lineage; species strain list not experiment provenance | supports | Eukaryota active domain. |
| micro-tax33090 | https://rest.uniprot.org/taxonomy/33090.json; Native identity/rank/active/parent/lineage; species strain list not experiment provenance | supports | Viridiplantae active kingdom within Eukaryota. |
| micro-tax3055 | https://rest.uniprot.org/taxonomy/3055.json; Native identity/rank/active/parent/lineage; species strain list not experiment provenance | supports | Chlamydomonas reinhardtii active species within green-algal lineage. Listed strain aliases do not identify which experimental strain Jin used. |
| micro-catalogue | https://imodulondb.org/api/datasets; Full unpaginated official catalogue,20 organisms/28 organism-dataset pairs | supports | No Chlamydomonas/reinhardtii, Viridiplantae/green-algal host entry. Three TOC–TIC-bearing targets require coverage assessment; no matching host means no downstream module/gene query. Whole/generic physical scope remains excluded independently of catalogue noncoverage. |
| micro-historical-runner | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical command /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources imodulondb datasets; actual00:49Z exit1 PermissionError reading pyvenv.cfg | context_only | Historical unavailable optional runner, not fresh invocation. Fresh official catalogue fallback completed; no matched-host downstream query. |
| micro-keeling2010-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1098%2Frstb.2009.0103%22&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact DOI core unique MED record identity/authors/publication types and complete abstract | context_only | Keeling2010 PMID20124341/PMC2817223 is secondary evolutionary review. Plastid diversity/loss context is not current universal phylogenetic consensus or numerical census. |
| micro-terashima2011-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1007%2Fs00294-011-0339-1%22&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact DOI core unique MED record identity/authors/publication types and complete abstract | context_only | Terashima/Specht/Hippler2011 PMID21533645 is secondary review. Supports C.reinhardtii chloroplast model context; compiled996 proteins are not all independently experimentally proven membrane residents or mandatory inventory. |
| micro-jin2022-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.cell.2022.10.030%22&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact DOI unique MED36413996 identity/authors, complete primary abstract, keywordList/meshHeadingList/fullTextUrlList; no body | supports | Jin2022 reports Chlamydomonas TOC–TIC cryoEM assembly spanning two envelope membranes and IMS scaffold; indexed keyword explicitly names C.reinhardtii. This supports species-bounded example and inner/IMS placement, not exact strain/Methods/model validation, per-protein necessity or every plastid lineage. |
| micro-jin2022-crossref | https://api.crossref.org/works/10.1016/j.cell.2022.10.030; Exact DOI title/authors/date/resource/link metadata; publisher route discovery only | context_only | Exact primary title/DOI and PII S0092867422013769 verified. Crossref metadata is not full article access. |
| micro-keeling2010-retained | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2817223/; Retained genuine HTML fetched10:10:38.582642Z; independently reread complete sections s1,s3,s6,s9 with embedded Figure1–3 captions; no pixels/other sections/underlying experiments | context_only | Secondary review supports primary double boundaries, secondary3/4 membranes and retained nonphotosynthetic plastids. Outdated universal mitochondrial-loss/old chromalveolate hypotheses are not adopted; no new current census. |
| micro-terashima2011-retained | https://link.springer.com/content/pdf/10.1007/s00294-011-0339-1.pdf; Retained genuine PDF fetched10:10:38.518294Z; fresh pdftotext pages151–152, complete title/abstract/Introduction and initial proteome-compilation discussion; no later pages/pixels/supplements | context_only | Secondary review supports chloroplast model/proteome research context and explains enriched-fraction contamination and compilation. No generic whole/membrane record claims996 residents, a specific pathway or membrane-only proteome; broad canonical model wording remains supported. |
| micro-access-keeling2010-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC2817223.1/PMC2817223.1.xml; Actual route response content inspected; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/adversary-microtubule/keeling2010-jats.receipt.json | context_only | S3 candidate404; no body. |
| micro-access-keeling2010-canonical | https://pmc.ncbi.nlm.nih.gov/articles/PMC2817223/; Actual route response content inspected; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/adversary-microtubule/keeling2010-canonical.receipt.json | context_only | HTTP200 recaptcha, not article. |
| micro-access-keeling2010-legacy | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2817223/; Actual route response content inspected; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/adversary-microtubule/keeling2010-legacy.receipt.json | context_only | HTTP200 recaptcha, not article; earlier genuine retained body separately read. |
| micro-access-terashima2011-pdf | https://link.springer.com/content/pdf/10.1007/s00294-011-0339-1.pdf; Actual route response content inspected; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/adversary-microtubule/terashima2011-pdf.receipt.json | context_only | HTTP2003038-byte HTML challenge, not PDF; genuine earlier retained PDF separately read. |
| micro-access-terashima2011-crossref | https://api.crossref.org/works/10.1007/s00294-011-0339-1; Actual route response content inspected; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/adversary-microtubule/terashima2011-crossref.receipt.json | context_only | HTTP429 zero-byte response; metadata elsewhere separately verified. |
| micro-access-jin2022-publisher | https://api.elsevier.com/content/article/PII:S0092867422013769?httpAccept=text/xml; Actual route response content inspected; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/adversary-microtubule/jin2022-publisher.receipt.json | context_only | HTTP2001941-byte XML contains core metadata only, despite full-text-retrieval-response name; no article body. |
| micro-access-jin2022-pdf | https://www.cell.com/cell/pdf/S0092-8674(22)01376-9.pdf; Actual route response content inspected; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/adversary-microtubule/jin2022-pdf.receipt.json | context_only | HTTP403 publisher challenge; no body/pixels. |
| check-qc | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/qc.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| check-labels | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/labels.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| check-trait-links | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/trait-links.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Native TraitMech link check passed. |
| check-vendored | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/vendored.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Pinned governed files match; native vendored check passed. |
| check-curies | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/curies.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| focused | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/focused-results.json; All twenty actual target schema/strict command outputs | supports | Ten schema and ten strict commands returned exit zero. |
| supplemental-pmid | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/pmid-chunks-receipt.json; Complete native-report PMID set checked with unchanged resolver in batches of at most fifty | supports | 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers remain unverified. |
| historical-adapter-runner-availability | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical runner invocation receipt, exact SHA256 reverified during PR2375 synthesis | context_only | Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS PermissionError reading the configured runner pyvenv.cfg. This is retained historical availability evidence, not a fresh attempt or a scientific validation failure. Native policy permits inspected source-catalogue fallback. |
| root-native-phagolysosome_vesicle_lumen-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/phagolysosome_vesicle_lumen-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-phagolysosome_vesicle_lumen-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/phagolysosome_vesicle_lumen-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-photosynthetic_membrane-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/photosynthetic_membrane-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 8 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-photosynthetic_membrane-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/photosynthetic_membrane-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 8 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-plasma_membrane_derived_chromatophore_membrane-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plasma_membrane_derived_chromatophore_membrane-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 6 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-plasma_membrane_derived_chromatophore_membrane-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plasma_membrane_derived_chromatophore_membrane-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 6 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-plasma_membrane_derived_thylakoid_lumen-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plasma_membrane_derived_thylakoid_lumen-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-plasma_membrane_derived_thylakoid_lumen-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plasma_membrane_derived_thylakoid_lumen-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-plasma_membrane_derived_thylakoid_membrane-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plasma_membrane_derived_thylakoid_membrane-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-plasma_membrane_derived_thylakoid_membrane-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plasma_membrane_derived_thylakoid_membrane-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-plastid-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-plastid-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-plastid_envelope-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid_envelope-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-plastid_envelope-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid_envelope-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-plastid_inner_membrane-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid_inner_membrane-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-plastid_inner_membrane-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid_inner_membrane-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-plastid_intermembrane_space-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid_intermembrane_space-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-plastid_intermembrane_space-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid_intermembrane_space-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-plastid_membrane-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid_membrane-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-plastid_membrane-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid_membrane-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |

## Limits And Additional Notes

- Phagolysosome lumen and bacterial thylakoid compartments independent subreview: Independent read-only review of three assigned targets. Five inherited scientific findings remain open:3major2minor. No new scientific finding or rejected predecessor; all three verdicts need curation. One assigned target is stale and substantively refreshed, while its old graph-inventory misdescription is separately corrected in review scope. No maintained records changed.
- Phagolysosome lumen and bacterial thylakoid compartments independent subreview: Current ontology/SL/taxonomy/catalogue and bounded matched-host HTTP queries are fresh. Gotthardt2002 PDF/metadata are cached from PR2374 with exact original access times and byte hashes; current reread is explicitly bounded. Casella/Huokko fresh collaborating-source snapshots were independently read at the stated sections and retain actual fetch times.
- Phagolysosome lumen and bacterial thylakoid compartments independent subreview: Casella Results2.1–2.3/Methods4.1/4.8, Fig1–5 text captions and Table1 text were read. Huokko ResultsSec3/4 and MethodsSec9/12/13 plus Fig1/2 captions were read. No image pixels, supplemental tables/movies or raw quantitative reanalysis. AFM b6f identification remains tentative; no source-condition generalization to all hosts.
- Phagolysosome lumen and bacterial thylakoid compartments independent subreview: Perez2024 is a secondary review. Actual publisher-delivered body Introduction/Lipids/ETC sections and text captions support qualitative mechanism/residence; initial landing/loading page alone did not. No exact universal lipid percentages, necessity claims or cited reference-body audit is inferred.
- Phagolysosome lumen and bacterial thylakoid compartments independent subreview: Gotthardt2002 original main body pp3508–3518 was inspected previously; Methods pp3509–3510 and Discussion/Fig7 pp3517–3518 were reread now. Trafficking/composition experiments are distinguished from prior-work acidification discussion and from the expanded cross-taxon enzymatic/ROS definition.
- Phagolysosome lumen and bacterial thylakoid compartments independent subreview: Catalogue has matched PCC7942 scope, not Synechocystis6803 or Dictyostelium/Entamoeba/ciliate hosts. Four bounded searches, four selected gene identities/57-row association responses and module1/38 structured data are contextual. Generated AI prose, expression matrices and conditions were not assessed. All-false threshold flags do not mean biological absence or failed localization; no unmatched organism proxy is used.
- Phagolysosome lumen and bacterial thylakoid compartments independent subreview: Historical runner PermissionError at00:49Z is retained only as historical availability evidence. Actual six native protein checks pass on independently confirmed0 examples/0 typed nodes/0 UniProtKB graph xrefs. Existing GO complexes/STRUCTURE nodes remain molecular assertions; empty native scope does not certify completeness.
- Phagolysosome lumen and bacterial thylakoid compartments independent subreview: All30 actually used repository inputs were frozen before reading:17 common policy/schema/script inputs,3 targets,6 originals and4 bounded anatomy neighbors. No whole-neighbor verdict, rationale rewrite, grouped-issue resolution, future saved-head/CI/merge certification or record mutation is claimed.
- Photosynthetic and bacterial chromatophore membranes independent subreview: Both assigned records still need curation for three inherited findings: one major source-organism attribution, one minor oxygenic-function scope and one minor existing-complex grounding. No newly confirmed scientific finding. Stale chromatophore is refreshable entirely in review-bundle scope; no record changes.
- Photosynthetic and bacterial chromatophore membranes independent subreview: Both original native pairs validate/render byte-for-byte;20 historical inputs each match originalsource. Photosynthetic target unchanged; chromatophore adds coherent currentgroundings/retypings/twoedges and is substantively refreshed. Historical graph/protein counts are not current counts. No category-wide#2432 resolution inferred.
- Photosynthetic and bacterial chromatophore membranes independent subreview: Fresh native GO,SL,taxon and14accession responses plus bounded reviewedgene searches verify identities/aliases/loci/status. P16033 includes two psbA loci. Nativeannotation inference/experimental citations are distinct; InterPro cross-references are not independently expanded family-page assertions or whole-complex groundings.
- Photosynthetic and bacterial chromatophore membranes independent subreview: Casella genuineJATS onlyResults2.1–2.4/captions andMethods4.1/4.5/4.7/4.8 read. PCC7942 notPCC6803; no pixels,supplements,rawdata or completeothersections audit. Huokko was fetched/shared but not relied on for this assigned current assessment.
- Photosynthetic and bacterial chromatophore membranes independent subreview: Bahatyrova genuinePDF scientificpp1058–1061/Methods/captions read; no pixels/supplements. NativeNCIB8253 isolatedmembranes have preparation-specific architecture; AFM did not localizebc1/ATPase or directlyresolvePufX. Feniouk genuinePDF scientificpp1115–1121/Methods/Results/Discussion/captions read; R.capsulatusB10 electrochromic/inhibitor coupling, not a newly audited directATP-product experiment.
- Photosynthetic and bacterial chromatophore membranes independent subreview: Comayras public author-upload browser excerpts only0–1241 with overlappingcaptures; no fullbody/pixels or nativeHTTPsuccess claim. Ga-strain quinone-pool assay suppressesbc1 and gradients; context doesnot establish unperturbed cyclicPMF measurement. Initial ScienceDirect access403 and DOI-query failure are access/search limits, not scientific refutations.
- Photosynthetic and bacterial chromatophore membranes independent subreview: Perez is SECONDARY REVIEW body, not primaryexperiment: inspectedIntroduction/evolutionaryoverview/BuildingBlocks/Lipids/ETC andembeddedFig1/2captions only. Sui secondaryabstract andNielsen primaryabstract only. Five PCC6803 annotation-linked primaryabstracts inspected; their full bodies/pixels not claimed.
- Photosynthetic and bacterial chromatophore membranes independent subreview: Same-PR shared source receipts retain actual20:00–20:02Zfetch dates andhashes; independently reread, not represented as fresh requests. Bothtargets lack maintainedimages/quantitativephysicalproperties/directquotes; no pixel or rawquantitative reanalysis claimed.
- Photosynthetic and bacterial chromatophore membranes independent subreview: Actual native checks cover8reviewedexamples/2COVEREDnodes forphotosynthetic and6reviewedexamples/0GENE_OR_PROTEINnodes forchromatophore. Zero typednodes is not an emptyprotein inventory. Enum permits complexes/families, so no automatic oldtyping defect.
- Photosynthetic and bacterial chromatophore membranes independent subreview: Both actual protein/pathway narratives trigger applicability. Catalogue hasPCC7942matchedsourcecontext, noPCC6803 orpurplehost. Bounded4queries/selected4genes/module1and38 independently reread. Belowthreshold is not absence; activity arrays notcondition-analyzed andAIgeneratedprose excluded. Historical00:49Zrunner remains unavailable; no newrunnerinvocation claimed.
- Photosynthetic and bacterial chromatophore membranes independent subreview: Three frozenenergycomplexneighbors used only for exact identity/definition/taxon/function/source andnodeinventory context; no complete neighbor scientificreview or issueclosure. No additionallocalinputs used beforefreeze. Root owns current globalQC,issues,persistence,CI/queue/merge; thissource report doesnot certify futuregates.
- Five plastid compartment records independent subreview: Five unchanged complete records independently reviewed: two inherited major whole-membrane LIPID findings preserve exact predecessor/action; three other targets remain qualified. Three unsupported explicit adapter exclusions corrected in assessment; two genuine physical exclusions preserved. No new scientific finding.
- Five plastid compartment records independent subreview: Fresh current GO/SL/taxonomy/catalogue and exact literature metadata are distinct from retained genuine Keeling HTML10:10:38.582642Z and Terashima PDF10:10:38.518294Z. Retained source bytes/hash verified and declared sections independently reread now; not new fetches.
- Five plastid compartment records independent subreview: Keeling secondary review read complete s1/s3/s6/s9 with embedded Figures1–3 captions only. Old chromalveolate models, universal mitochondrial-loss statements, numerical species estimates and underlying cited primary studies are not adopted or independently audited. No source pixels/supplements.
- Five plastid compartment records independent subreview: Terashima secondary PDF title/abstract/Introduction and initial proteome discussion onpp151–152 read. No later sections/protein tables/supplements/pixels audited; fraction contamination/compiled candidates are not treated as a generic membrane molecular inventory.
- Five plastid compartment records independent subreview: Jin2022 primary access is complete abstract, indexed C.reinhardtii keyword and bibliographic/publisher metadata only. PublisherXML returns coredata, not article body; PDF route403. No exact strain, full Methods/coordinate model/pixels/functional deletion experiments certified. Access limits are not refutations.
- Five plastid compartment records independent subreview: Five records have zero protein_examples and zero typed molecular nodes; current native passes do not imply complete protein-family coverage. Three positiveTOC–TIC narrative claims trigger adapter coverage despite empty graph; whole/generic model-use context does not assert a specified pathway.
- Five plastid compartment records independent subreview: Fresh full20-organism/28-pair official catalogue has no matching Chlamydomonas/green-algal host. No unmatched cyanobacterial proxy/downstream module query; noncoverage is not negative biology. Historical00:49Z runner failure remains historical unavailable, not rerun.
- Five plastid compartment records independent subreview: GO generic membrane definition focuses on envelope while explicit child hierarchy includes thylakoid/cyanelle/apicoplast membranes; class evidence supports this broader fallback without inventing a direct GO relation. Two frozen neighbors are boundary context only; their issues/verdicts are not adjudicated.
- Five plastid compartment records independent subreview: No records/originals/history/generated files/Git/GitHub changed; root owns current global gates,issue dedup/publication/successor and later CI/queue/merge. This report does not precertify future results.
- Historical observations remain immutable; their old checks are not represented as current-head execution.
- The adapter runner was not rerun after the canary established OS access failure. Catalogue-based coverage is assessed directly; fresh and reused responses retain actual access timestamps.
- Native label checks include 923 no-adapter skips. Native identifier checks include 909 PMID transport failures and 254 skipped identifiers; bounded supplemental checks independently resolve the 909 PMIDs.
- Scientific record-curation findings stay in separate issues; no record is edited by this review PR.
- Final trusted-base post-save review-check, exact-head independent acceptance, final-head CI and merge-group CI occur after saving this immutable observation and are not represented here as already completed.
- All ten original YAML/Markdown pairs remain unchanged. Current main was merged normally and pushed without force. Two original target hashes differ: plasma-membrane-derived chromatophore membrane and thylakoid membrane. Their changed claims are substantively reassessed; the other eight inputs still match.
- This explicit issue-bearing ten-record cohort follows native persistence policy. Inherited scientific findings retain stable keys and exact predecessor repository/review/finding identities; any newly observed finding has no invented predecessor.
- Issue2773 tracks the two stale reviews and the original thylakoid assessment that prematurely described ATP-synthase residence among the old five edges. The successor distinguishes historical assessment error from the newly present node/edge instead of claiming the original review saw future content.
- Issue2774 tracks eight unsupported source-applicability exclusions: four prose notes without a formal check (photosynthetic membrane, bacterial chromatophore membrane, bacterial thylakoid lumen/membrane) and four explicit check rows (phagolysosome lumen, plastid envelope, inner membrane and IMS). Whole plastid and generic plastid membrane retain genuine material/topology exclusions.
- Source commit659d5d9ce7e16c8607002bf1655db2f3c652e6e1 is retained by tag review-base/pr2375-current-record-followup-20261103.
- CLAUDE.md aliases AGENTS.md; canonical regular AGENTS.md bytes are frozen. All used local policy, schema, verifier, original artifacts and boundary/complex context inputs are frozen before assessment.
- Chromatophore newly propagated node groundings concern RC-LH1-PufX and bc1, not the separate original LH2/F0F1 component-grounding finding. Closed issue2432 is narrow historical propagation context, not proof of broader issue resolution.
- Fresh and retained literature snapshots preserve their actual access times and declared body/abstract/pixel limits. Identity and family/domain checks are distinct from experimental structure membership, strain provenance or assembly necessity.
- All twenty native protein commands passed. Photosynthetic membrane has eight reviewed examples and two COVERED typed nodes; bacterial chromatophore membrane has six reviewed examples and zero current GENE_OR_PROTEIN nodes after complex-node retyping. The other eight records have zero examples and zero typed molecular nodes. Positive narrative pathway claims still require applicability assessment.
- Native CausalNode schema permits families and complexes as GENE_OR_PROTEIN. Subsequent STRUCTURE retyping alone is not evidence that original generic typing was invalid. Source-neutral group/complex grounding questions are not automatically resolved by taxon-specific subunit accessions.
- Five related open issue matches concern different maintained records; no same-record/finding duplicate was found. Validator2514 remains reused and open. No scientific records, historical discussions or resolver are edited.
- Final trusted-base review-check, exact-head independent acceptance, final-head CI and merge-group CI occur after this immutable observation and are not represented as already complete.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T201029Z-pr2375-current-record-followup
kind: batch
repository: CultureBotAI/CellStructureMech
title: 'PR 2375: current-input review of ten records and adversarial follow-up'
started_at: '2026-11-03T19:58:46.015890Z'
finished_at: '2026-11-03T20:10:29Z'
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
  merging main. Two stale reviews are refreshed through substantive reassessment of
  changed chromatophore and thylakoid membrane content, including added graph nodes,
  groundings and edges. Eight unsupported source-applicability exclusions are corrected,
  including four prose-only exclusions and four explicit check rows; whole plastid
  and generic plastid membrane retain genuine physical/material-topology exclusions.
  Inherited findings retain exact predecessor identities. All original observations
  and scientific records remain unchanged. Ten inherited scientific findings remain
  open (six major and four minor) across seven targets; three other targets retain
  qualified positive assessments. Separate curation issues preserve exact predecessor
  lineage.
source:
  git_revision: 659d5d9ce7e16c8607002bf1655db2f3c652e6e1
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
  - path: data/structures/energy_complex/chromatophore_cytochrome_bc1_complex.yaml
    sha256: 7f6582722d2f5376262287856929ec073f8550493eee88c6cb92dfc7624ec7ed
    role: context
  - path: data/structures/energy_complex/lh2_peripheral_light_harvesting_antenna_complex.yaml
    sha256: 4bb84c48c2bb27f1a8dded06f479771b494070977ef26e0b14f0708bc446a7ce
    role: context
  - path: data/structures/energy_complex/proton_transporting_atp_synthase_complex.yaml
    sha256: ab93b5ffa055615dfc9de1edfb137773e1098b4f7e9eefdda9d0ea00961af4fb
    role: context
  - path: data/structures/energy_complex/rc_lh1_pufx_core_complex.yaml
    sha256: 0a3a6fcfe54b7a355fd2903992f521fb2fc293ce984d4ede356dbc8460071824
    role: context
  - path: data/structures/membrane_organelle/bacterial_thylakoid.yaml
    sha256: a134c6cf6fd6069f0a0ddc37f1e99ded9a32994b3b1fa16d2f9938e3e46b8c40
    role: context
  - path: data/structures/membrane_organelle/phagolysosome.yaml
    sha256: 1aa7bcc22c4b8a9bb65c69fad0c276e2446d28534b72a8abf930ed0e64c70e1e
    role: context
  - path: data/structures/membrane_organelle/phagolysosome_membrane.yaml
    sha256: 7f7e638a499bf7a56376a0f51d9de765fe0e3b9f7563bdb2ee13e9d332306b32
    role: context
  - path: data/structures/membrane_organelle/phagolysosome_vesicle_lumen.yaml
    sha256: 096069e6ecc9f33d640dfb9621fa69dedfab50cb9a9f08e6186e9583a823c319
    role: target
  - path: data/structures/membrane_organelle/photosynthetic_membrane.yaml
    sha256: 5fe446aae99635ba843cf22d1144ab1312a2c30224367c49efd0bedcbd06db97
    role: target
  - path: data/structures/membrane_organelle/plasma_membrane_derived_chromatophore_membrane.yaml
    sha256: e2622df75241a3d18a0c08f64d1e59fc10f49da8ee8ed7843cf6f08df2020195
    role: target
  - path: data/structures/membrane_organelle/plasma_membrane_derived_thylakoid_lumen.yaml
    sha256: 4b4fbe694529235b322625d85f5c210eddea0cc03e5e1a684d5bff2d698bca82
    role: target
  - path: data/structures/membrane_organelle/plasma_membrane_derived_thylakoid_membrane.yaml
    sha256: 50b81e60972c1a3c89a73cf685b98887a221a3b0ba379b10fee8be1765d167e0
    role: target
  - path: data/structures/membrane_organelle/plastid.yaml
    sha256: 1be30ab06bc2fbae9294930ceaf74b20a2d43d8af60986aa9ed0e07b9645ae81
    role: target
  - path: data/structures/membrane_organelle/plastid_envelope.yaml
    sha256: 9033a6955c21d6043019061509c7ca1bf470bec884e7f4e1a5edc0080b680968
    role: target
  - path: data/structures/membrane_organelle/plastid_inner_membrane.yaml
    sha256: ceb12c6ee4451216ae406f17f68ea2d3730a6da302b38e8bb8fcabc532a6a4fa
    role: target
  - path: data/structures/membrane_organelle/plastid_intermembrane_space.yaml
    sha256: 2ef21406931fb90ec3aead7f57ee12a4376ad3d95276c7db3c2a7ab324c73c5d
    role: target
  - path: data/structures/membrane_organelle/plastid_membrane.yaml
    sha256: ae09183c12ecb85ac2135b3615b9a613985285039f5730126227fde982e55bef
    role: target
  - path: data/structures/membrane_organelle/plastid_outer_membrane.yaml
    sha256: 59bd8548931d27f711233f542b5f927c0e7b0a68dd611eabb4777ee08003deaa
    role: context
  - path: data/structures/membrane_organelle/plastid_stroma.yaml
    sha256: 86d19307cbe21273498f0d7d6741e61f5ebf002cf78418c34b922d9d4963503b
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
  - path: reviews/structured/20261022T032300Z-phagolysosome-vesicle-lumen-audit/review.md
    sha256: 62a6ecfacdaa7b697b9a823b18f9b11e17c86217249338f5ee0c42467f47147c
    role: context
  - path: reviews/structured/20261022T032300Z-phagolysosome-vesicle-lumen-audit/review.yaml
    sha256: 9db7f19b1526966a1a2435120db2c562c33ebd62fe8b4799ee87d388564bb901
    role: context
  - path: reviews/structured/20261022T032301Z-photosynthetic-membrane-audit/review.md
    sha256: aa65e696931ca51e26818f8fb5dfef0818f0f0f422709ac790a90609ba4ecaa9
    role: context
  - path: reviews/structured/20261022T032301Z-photosynthetic-membrane-audit/review.yaml
    sha256: 77366c398da4f6db5027b57932a0d70eb2fa789ea9ff11045430d2dda257fe93
    role: context
  - path: reviews/structured/20261022T032301Z-plasma-membrane-derived-chromatophore-membrane-audit/review.md
    sha256: c15ea80c57b6fb59030638716096cab66e07c960d4fffbba68aa3a789aa40f1f
    role: context
  - path: reviews/structured/20261022T032301Z-plasma-membrane-derived-chromatophore-membrane-audit/review.yaml
    sha256: 0f187b643ca8c6237cb1a59d3cb021732cb8d620f31f8004c7b5ac6db67d1ace
    role: context
  - path: reviews/structured/20261022T032302Z-plasma-membrane-derived-thylakoid-lumen-audit/review.md
    sha256: 467387512b6001c3cbe3ca952a6d8d2d1e812f8ba4e55f0e12f536b5e795740b
    role: context
  - path: reviews/structured/20261022T032302Z-plasma-membrane-derived-thylakoid-lumen-audit/review.yaml
    sha256: 7b0dd6c4c520177c2718ab94847ac8f1118eddcdf70d7fdab66344de65432ad5
    role: context
  - path: reviews/structured/20261022T032303Z-plasma-membrane-derived-thylakoid-membrane-audit/review.md
    sha256: 88884be022779abd63db5e0605256e35491cfe84354e6b754a2b694934f8bd60
    role: context
  - path: reviews/structured/20261022T032303Z-plasma-membrane-derived-thylakoid-membrane-audit/review.yaml
    sha256: 199e73c73eaeb5c2f6b712174de004dc5937b00e4a13d2b7b3448ccb5c096b3e
    role: context
  - path: reviews/structured/20261022T032303Z-plastid-audit/review.md
    sha256: f4ade985f3fc9b4d05004f3f121188c435775c63bfb93fa17e0b6ac3404a4d2e
    role: context
  - path: reviews/structured/20261022T032303Z-plastid-audit/review.yaml
    sha256: 1c42de1dc8e88cd7fff7a11e033c2a4955c21115be4c933cbd0398e4a39e7ec9
    role: context
  - path: reviews/structured/20261022T032304Z-plastid-envelope-audit/review.md
    sha256: 552355aedb83cfe6f0a20b78b4c49b6945a73a28b09edb517de3c9434a163ebc
    role: context
  - path: reviews/structured/20261022T032304Z-plastid-envelope-audit/review.yaml
    sha256: 5fe2d0c23c716174f5967a19662fd0158f7b411d6af5d623ff086c6750999a81
    role: context
  - path: reviews/structured/20261022T032305Z-plastid-inner-membrane-audit/review.md
    sha256: 49fa0fd92e317c19483d2bf342a30ed2793508a33e14afc966bac7fcdd64010f
    role: context
  - path: reviews/structured/20261022T032305Z-plastid-inner-membrane-audit/review.yaml
    sha256: 7beb0aff217f2f0917394a45e58ed3d40d8f40f5671418a934aebb05b4c7af66
    role: context
  - path: reviews/structured/20261022T032305Z-plastid-intermembrane-space-audit/review.md
    sha256: 989c6d2eb5f675410c58ad2d5029c5d02e28efc80d8fc682c857270176006ed8
    role: context
  - path: reviews/structured/20261022T032305Z-plastid-intermembrane-space-audit/review.yaml
    sha256: e582df2870c77ec17e21f8395ff224db0e6ddcb17a6ed2bf3341b2e7eb1570de
    role: context
  - path: reviews/structured/20261022T032306Z-plastid-membrane-audit/review.md
    sha256: e6417997437437568095d8a695764bc9154b289b7bb4f5ac8b548c08df02e0ab
    role: context
  - path: reviews/structured/20261022T032306Z-plastid-membrane-audit/review.yaml
    sha256: 876aef10c0601ebfb1e46596c4090506f360e0d84cda4dbbf822b0cd38d67ff2
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
- target_id: GO:0106174
  path: data/structures/membrane_organelle/phagolysosome_vesicle_lumen.yaml
  label: phagolysosome vesicle lumen
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/phagolysosome_vesicle_lumen.yaml
    role: maintained scientific record
- target_id: GO:0034357
  path: data/structures/membrane_organelle/photosynthetic_membrane.yaml
  label: photosynthetic membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/photosynthetic_membrane.yaml
    role: maintained scientific record
- target_id: GO:0042717
  path: data/structures/membrane_organelle/plasma_membrane_derived_chromatophore_membrane.yaml
  label: plasma membrane-derived chromatophore membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/plasma_membrane_derived_chromatophore_membrane.yaml
    role: maintained scientific record
- target_id: GO:0031979
  path: data/structures/membrane_organelle/plasma_membrane_derived_thylakoid_lumen.yaml
  label: plasma membrane-derived thylakoid lumen
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/plasma_membrane_derived_thylakoid_lumen.yaml
    role: maintained scientific record
- target_id: GO:0031676
  path: data/structures/membrane_organelle/plasma_membrane_derived_thylakoid_membrane.yaml
  label: plasma membrane-derived thylakoid membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/plasma_membrane_derived_thylakoid_membrane.yaml
    role: maintained scientific record
- target_id: GO:0009536
  path: data/structures/membrane_organelle/plastid.yaml
  label: plastid
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/plastid.yaml
    role: maintained scientific record
- target_id: GO:0009526
  path: data/structures/membrane_organelle/plastid_envelope.yaml
  label: plastid envelope
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/plastid_envelope.yaml
    role: maintained scientific record
- target_id: GO:0009528
  path: data/structures/membrane_organelle/plastid_inner_membrane.yaml
  label: plastid inner membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/plastid_inner_membrane.yaml
    role: maintained scientific record
- target_id: GO:0009529
  path: data/structures/membrane_organelle/plastid_intermembrane_space.yaml
  label: plastid intermembrane space
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/plastid_intermembrane_space.yaml
    role: maintained scientific record
- target_id: GO:0042170
  path: data/structures/membrane_organelle/plastid_membrane.yaml
  label: plastid membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/plastid_membrane.yaml
    role: maintained scientific record
scope:
  description: Exact ten-record PR cohort reassessed against current main 2b971e43fc3fad85009d3cd036695b33f0fcaf5c.
    Changed inputs are substantively reassessed. Scientific records remain unchanged.
  selection: Complete cohort of ten maintained records reviewed in original PR head
    048dab0c30cba35f96656b45bac93d33d19a1908.
  coverage: full
  population_size: 10
  reviewed_target_ids:
  - GO:0106174
  - GO:0034357
  - GO:0042717
  - GO:0031979
  - GO:0031676
  - GO:0009536
  - GO:0009526
  - GO:0009528
  - GO:0009529
  - GO:0042170
checks:
- check_id: qc
  name: Full native QC
  status: passed
  required: true
  target_ids:
  - GO:0106174
  - GO:0034357
  - GO:0042717
  - GO:0031979
  - GO:0031676
  - GO:0009536
  - GO:0009526
  - GO:0009528
  - GO:0009529
  - GO:0042170
  command: just qc
  exit_code: 0
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  scope_note: Actual local execution at main-merge head 659d5d9ce7e16c8607002bf1655db2f3c652e6e1.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-qc
- check_id: labels
  name: Native label correspondence
  status: passed
  required: true
  target_ids:
  - GO:0106174
  - GO:0034357
  - GO:0042717
  - GO:0031979
  - GO:0031676
  - GO:0009536
  - GO:0009526
  - GO:0009528
  - GO:0009529
  - GO:0042170
  command: just validate-products
  exit_code: 0
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  scope_note: Actual local execution at main-merge head 659d5d9ce7e16c8607002bf1655db2f3c652e6e1.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-labels
- check_id: trait-links
  name: TraitMech references
  status: passed
  required: true
  target_ids:
  - GO:0106174
  - GO:0034357
  - GO:0042717
  - GO:0031979
  - GO:0031676
  - GO:0009536
  - GO:0009526
  - GO:0009528
  - GO:0009529
  - GO:0042170
  command: just check-trait-links --check
  exit_code: 0
  summary: Native TraitMech link check passed.
  scope_note: Actual local execution at main-merge head 659d5d9ce7e16c8607002bf1655db2f3c652e6e1.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-trait-links
- check_id: vendored
  name: Pinned governed files
  status: passed
  required: true
  target_ids:
  - GO:0106174
  - GO:0034357
  - GO:0042717
  - GO:0031979
  - GO:0031676
  - GO:0009536
  - GO:0009526
  - GO:0009528
  - GO:0009529
  - GO:0042170
  command: just vendored-check
  exit_code: 0
  summary: Pinned governed files match; native vendored check passed.
  scope_note: Actual local execution at main-merge head 659d5d9ce7e16c8607002bf1655db2f3c652e6e1.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-vendored
- check_id: curies
  name: Native identifier resolver
  status: passed
  required: true
  target_ids:
  - GO:0106174
  - GO:0034357
  - GO:0042717
  - GO:0031979
  - GO:0031676
  - GO:0009536
  - GO:0009526
  - GO:0009528
  - GO:0009529
  - GO:0042170
  command: just check-curies
  exit_code: 0
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  scope_note: Actual local execution at main-merge head 659d5d9ce7e16c8607002bf1655db2f3c652e6e1.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-curies
- check_id: focused-0
  name: validate GO:0106174
  status: passed
  required: true
  target_ids:
  - GO:0106174
  command: just validate data/structures/membrane_organelle/phagolysosome_vesicle_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-1
  name: validate-strict GO:0106174
  status: passed
  required: true
  target_ids:
  - GO:0106174
  command: just validate-strict data/structures/membrane_organelle/phagolysosome_vesicle_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-2
  name: validate GO:0034357
  status: passed
  required: true
  target_ids:
  - GO:0034357
  command: just validate data/structures/membrane_organelle/photosynthetic_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-3
  name: validate-strict GO:0034357
  status: passed
  required: true
  target_ids:
  - GO:0034357
  command: just validate-strict data/structures/membrane_organelle/photosynthetic_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-4
  name: validate GO:0042717
  status: passed
  required: true
  target_ids:
  - GO:0042717
  command: just validate data/structures/membrane_organelle/plasma_membrane_derived_chromatophore_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-5
  name: validate-strict GO:0042717
  status: passed
  required: true
  target_ids:
  - GO:0042717
  command: just validate-strict data/structures/membrane_organelle/plasma_membrane_derived_chromatophore_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-6
  name: validate GO:0031979
  status: passed
  required: true
  target_ids:
  - GO:0031979
  command: just validate data/structures/membrane_organelle/plasma_membrane_derived_thylakoid_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-7
  name: validate-strict GO:0031979
  status: passed
  required: true
  target_ids:
  - GO:0031979
  command: just validate-strict data/structures/membrane_organelle/plasma_membrane_derived_thylakoid_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-8
  name: validate GO:0031676
  status: passed
  required: true
  target_ids:
  - GO:0031676
  command: just validate data/structures/membrane_organelle/plasma_membrane_derived_thylakoid_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-9
  name: validate-strict GO:0031676
  status: passed
  required: true
  target_ids:
  - GO:0031676
  command: just validate-strict data/structures/membrane_organelle/plasma_membrane_derived_thylakoid_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-10
  name: validate GO:0009536
  status: passed
  required: true
  target_ids:
  - GO:0009536
  command: just validate data/structures/membrane_organelle/plastid.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-11
  name: validate-strict GO:0009536
  status: passed
  required: true
  target_ids:
  - GO:0009536
  command: just validate-strict data/structures/membrane_organelle/plastid.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-12
  name: validate GO:0009526
  status: passed
  required: true
  target_ids:
  - GO:0009526
  command: just validate data/structures/membrane_organelle/plastid_envelope.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-13
  name: validate-strict GO:0009526
  status: passed
  required: true
  target_ids:
  - GO:0009526
  command: just validate-strict data/structures/membrane_organelle/plastid_envelope.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-14
  name: validate GO:0009528
  status: passed
  required: true
  target_ids:
  - GO:0009528
  command: just validate data/structures/membrane_organelle/plastid_inner_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-15
  name: validate-strict GO:0009528
  status: passed
  required: true
  target_ids:
  - GO:0009528
  command: just validate-strict data/structures/membrane_organelle/plastid_inner_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-16
  name: validate GO:0009529
  status: passed
  required: true
  target_ids:
  - GO:0009529
  command: just validate data/structures/membrane_organelle/plastid_intermembrane_space.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-17
  name: validate-strict GO:0009529
  status: passed
  required: true
  target_ids:
  - GO:0009529
  command: just validate-strict data/structures/membrane_organelle/plastid_intermembrane_space.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-18
  name: validate GO:0042170
  status: passed
  required: true
  target_ids:
  - GO:0042170
  command: just validate data/structures/membrane_organelle/plastid_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-19
  name: validate-strict GO:0042170
  status: passed
  required: true
  target_ids:
  - GO:0042170
  command: just validate-strict data/structures/membrane_organelle/plastid_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: supplemental-pmid
  name: Supplemental bounded PMID authority checks
  status: passed
  required: true
  target_ids:
  - GO:0106174
  - GO:0034357
  - GO:0042717
  - GO:0031979
  - GO:0031676
  - GO:0009536
  - GO:0009526
  - GO:0009528
  - GO:0009529
  - GO:0042170
  command: .venv/bin/python /private/tmp/cellstructure-batches-2346-2397-20261103/check_pmid_chunks.py
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375
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
  - GO:0106174
  - GO:0034357
  - GO:0042717
  - GO:0031979
  - GO:0031676
  - GO:0009536
  - GO:0009526
  - GO:0009528
  - GO:0009529
  - GO:0042170
  summary: 'Eight records assert positive molecular/pathway claims: phagolysosome
    lumen, photosynthetic membrane, bacterial chromatophore membrane, two bacterial
    thylakoid compartments, plastid envelope, inner membrane and intermembrane space.
    Four unsupported prose-only exclusions and four unsupported explicit check rows
    are corrected with actual host/strain catalogue coverage and applicable downstream
    checks. Whole plastid and generic plastid membrane retain genuine physical/material-topology
    exclusions. A study-model mention alone is not an asserted protein inventory.
    Noncoverage is not biological absence; unrelated organisms are not proxies. Historical
    runner unavailability stays historical with actual public-source fallback scopes
    and timestamps.'
  evidence_ids:
  - septin-catalogue
  - septin-adapter-search-photosystem
  - septin-adapter-search-cytochrome-b6
  - septin-adapter-search-ATP-synthase
  - septin-adapter-search-thylakoid
  - septin-adapter-gene-Synpcc7942_2049
  - septin-adapter-gene-Synpcc7942_2049-modules
  - septin-adapter-gene-Synpcc7942_0424
  - septin-adapter-gene-Synpcc7942_0424-modules
  - septin-adapter-gene-Synpcc7942_2331
  - septin-adapter-gene-Synpcc7942_2331-modules
  - septin-adapter-gene-Synpcc7942_0336
  - septin-adapter-gene-Synpcc7942_0336-modules
  - septin-adapter-module-1
  - septin-adapter-module-38
  - plaque-catalogue
  - plaque-adapter-search-photosystem
  - plaque-adapter-search-cytochrome-b6
  - plaque-adapter-search-ATP-synthase
  - plaque-adapter-search-thylakoid
  - plaque-adapter-gene-Synpcc7942_2049
  - plaque-adapter-gene-Synpcc7942_2049-modules
  - plaque-adapter-gene-Synpcc7942_0424
  - plaque-adapter-gene-Synpcc7942_0424-modules
  - plaque-adapter-gene-Synpcc7942_2331
  - plaque-adapter-gene-Synpcc7942_2331-modules
  - plaque-adapter-gene-Synpcc7942_0336
  - plaque-adapter-gene-Synpcc7942_0336-modules
  - plaque-adapter-module-1
  - plaque-adapter-module-38
  - micro-catalogue
- check_id: independent-scientific-review
  name: Independent claim-level source review
  status: passed
  required: true
  target_ids:
  - GO:0106174
  - GO:0034357
  - GO:0042717
  - GO:0031979
  - GO:0031676
  - GO:0009536
  - GO:0009526
  - GO:0009528
  - GO:0009529
  - GO:0042170
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
  - septin-SL0044
  - septin-SL0045
  - septin-SL0342
  - septin-tax1117
  - septin-tax1148
  - septin-tax1140
  - septin-tax44689
  - septin-casella2017-jats
  - septin-huokko2021-jats
  - septin-perez2024-delivered
  - septin-gotthardt2002-unige-pdf
  - septin-adapter-gene-Synpcc7942_2049
  - septin-adapter-gene-Synpcc7942_0424
  - septin-adapter-gene-Synpcc7942_2331
  - septin-adapter-gene-Synpcc7942_0336
  - septin-adapter-module-1
  - septin-adapter-module-38
  - plaque-policy
  - plaque-rubric
  - plaque-graph-rubric
  - plaque-schema-policy
  - plaque-history-policy
  - plaque-go
  - plaque-SL0042
  - plaque-tax2
  - plaque-tax1063
  - plaque-tax272943
  - plaque-tax349102
  - plaque-tax1111708
  - plaque-tax1117
  - plaque-tax1148
  - plaque-tax1140
  - plaque-casella2017-meta
  - plaque-bahatyrova2004-meta
  - plaque-comayras2005-meta
  - plaque-feniouk2002-pmid
  - plaque-nielsen2016-meta
  - plaque-sui2021-meta
  - plaque-feniouk2002-meta
  - plaque-casella2017-jats
  - plaque-bahatyrova2004-pdf
  - plaque-feniouk2002-author-pdf
  - plaque-comayras-browser-initial
  - plaque-comayras-browser-methods
  - plaque-perez2024-delivered
  - plaque-protein-P29254
  - plaque-protein-P0C0Y8
  - plaque-protein-P0C0Y9
  - plaque-protein-P16033
  - plaque-protein-P26287
  - plaque-protein-Q57038
  - plaque-protein-Q02761
  - plaque-protein-Q02760
  - plaque-protein-P0C0Y0
  - plaque-protein-P0C0Y2
  - plaque-protein-A4WUM7
  - plaque-protein-Q3J433
  - plaque-protein-Q3IZ12
  - plaque-protein-Q3IZ13
  - plaque-PMID11788579
  - plaque-PMID12069591
  - plaque-PMID19577535
  - plaque-PMID34937700
  - plaque-PMID35726684
  - plaque-catalogue
  - plaque-adapter-gene-Synpcc7942_2049
  - plaque-adapter-gene-Synpcc7942_2049-modules
  - plaque-adapter-gene-Synpcc7942_0424
  - plaque-adapter-gene-Synpcc7942_0424-modules
  - plaque-adapter-gene-Synpcc7942_2331
  - plaque-adapter-gene-Synpcc7942_2331-modules
  - plaque-adapter-gene-Synpcc7942_0336
  - plaque-adapter-gene-Synpcc7942_0336-modules
  - plaque-adapter-module-1
  - plaque-adapter-module-38
  - micro-policy
  - micro-component-policy
  - micro-graph-policy
  - micro-discussion-policy
  - micro-go
  - micro-go0042170-isa
  - micro-SL0209
  - micro-SL0210
  - micro-SL0211
  - micro-SL0212
  - micro-SL0214
  - micro-tax2759
  - micro-tax33090
  - micro-tax3055
  - micro-keeling2010-meta
  - micro-terashima2011-meta
  - micro-jin2022-meta
  - micro-jin2022-crossref
  - micro-keeling2010-retained
  - micro-terashima2011-retained
- check_id: historical-adapter-runner
  name: Retained historical adapter runner availability
  status: unavailable
  required: false
  target_ids:
  - GO:0106174
  - GO:0034357
  - GO:0042717
  - GO:0031979
  - GO:0031676
  - GO:0009536
  - GO:0009526
  - GO:0009528
  - GO:0009529
  - GO:0042170
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
- check_id: phagolysosome_vesicle_lumen-uniprot-verify
  name: Native phagolysosome vesicle lumen UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0106174
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/phagolysosome_vesicle_lumen.yaml
    --verify
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-phagolysosome_vesicle_lumen-uniprot-verify
- check_id: phagolysosome_vesicle_lumen-uniprot-causal
  name: Native phagolysosome vesicle lumen UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0106174
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/phagolysosome_vesicle_lumen.yaml
    --causal-graphs
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-phagolysosome_vesicle_lumen-uniprot-causal
- check_id: photosynthetic_membrane-uniprot-verify
  name: Native photosynthetic membrane UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0034357
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/photosynthetic_membrane.yaml
    --verify
  exit_code: 0
  summary: 8 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-photosynthetic_membrane-uniprot-verify
- check_id: photosynthetic_membrane-uniprot-causal
  name: Native photosynthetic membrane UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0034357
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/photosynthetic_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: 8 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-photosynthetic_membrane-uniprot-causal
- check_id: plasma_membrane_derived_chromatophore_membrane-uniprot-verify
  name: Native plasma membrane-derived chromatophore membrane UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0042717
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plasma_membrane_derived_chromatophore_membrane.yaml
    --verify
  exit_code: 0
  summary: 6 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-plasma_membrane_derived_chromatophore_membrane-uniprot-verify
- check_id: plasma_membrane_derived_chromatophore_membrane-uniprot-causal
  name: Native plasma membrane-derived chromatophore membrane UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0042717
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plasma_membrane_derived_chromatophore_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: 6 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-plasma_membrane_derived_chromatophore_membrane-uniprot-causal
- check_id: plasma_membrane_derived_thylakoid_lumen-uniprot-verify
  name: Native plasma membrane-derived thylakoid lumen UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0031979
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plasma_membrane_derived_thylakoid_lumen.yaml
    --verify
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-plasma_membrane_derived_thylakoid_lumen-uniprot-verify
- check_id: plasma_membrane_derived_thylakoid_lumen-uniprot-causal
  name: Native plasma membrane-derived thylakoid lumen UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0031979
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plasma_membrane_derived_thylakoid_lumen.yaml
    --causal-graphs
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-plasma_membrane_derived_thylakoid_lumen-uniprot-causal
- check_id: plasma_membrane_derived_thylakoid_membrane-uniprot-verify
  name: Native plasma membrane-derived thylakoid membrane UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0031676
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plasma_membrane_derived_thylakoid_membrane.yaml
    --verify
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-plasma_membrane_derived_thylakoid_membrane-uniprot-verify
- check_id: plasma_membrane_derived_thylakoid_membrane-uniprot-causal
  name: Native plasma membrane-derived thylakoid membrane UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0031676
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plasma_membrane_derived_thylakoid_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-plasma_membrane_derived_thylakoid_membrane-uniprot-causal
- check_id: plastid-uniprot-verify
  name: Native plastid UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0009536
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid.yaml
    --verify
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-plastid-uniprot-verify
- check_id: plastid-uniprot-causal
  name: Native plastid UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0009536
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid.yaml
    --causal-graphs
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-plastid-uniprot-causal
- check_id: plastid_envelope-uniprot-verify
  name: Native plastid envelope UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0009526
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_envelope.yaml
    --verify
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-plastid_envelope-uniprot-verify
- check_id: plastid_envelope-uniprot-causal
  name: Native plastid envelope UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0009526
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_envelope.yaml
    --causal-graphs
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-plastid_envelope-uniprot-causal
- check_id: plastid_inner_membrane-uniprot-verify
  name: Native plastid inner membrane UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0009528
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_inner_membrane.yaml
    --verify
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-plastid_inner_membrane-uniprot-verify
- check_id: plastid_inner_membrane-uniprot-causal
  name: Native plastid inner membrane UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0009528
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_inner_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-plastid_inner_membrane-uniprot-causal
- check_id: plastid_intermembrane_space-uniprot-verify
  name: Native plastid intermembrane space UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0009529
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_intermembrane_space.yaml
    --verify
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-plastid_intermembrane_space-uniprot-verify
- check_id: plastid_intermembrane_space-uniprot-causal
  name: Native plastid intermembrane space UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0009529
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_intermembrane_space.yaml
    --causal-graphs
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-plastid_intermembrane_space-uniprot-causal
- check_id: plastid_membrane-uniprot-verify
  name: Native plastid membrane UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0042170
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_membrane.yaml
    --verify
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-plastid_membrane-uniprot-verify
- check_id: plastid_membrane-uniprot-causal
  name: Native plastid membrane UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0042170
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-plastid_membrane-uniprot-causal
evidence:
- evidence_id: current-record-0
  kind: record_content
  reference: data/structures/membrane_organelle/phagolysosome_vesicle_lumen.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T20:10:29Z'
  support: context_only
  summary: Original frozen SHA256 096069e6ecc9f33d640dfb9621fa69dedfab50cb9a9f08e6186e9583a823c319;
    current SHA256 096069e6ecc9f33d640dfb9621fa69dedfab50cb9a9f08e6186e9583a823c319.
    Record bytes unchanged since the original review.
  snapshot_sha256: 096069e6ecc9f33d640dfb9621fa69dedfab50cb9a9f08e6186e9583a823c319
- evidence_id: original-review-0
  kind: prior_review
  reference: reviews/structured/20261022T032300Z-phagolysosome-vesicle-lumen-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T20:10:29Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 9db7f19b1526966a1a2435120db2c562c33ebd62fe8b4799ee87d388564bb901
- evidence_id: current-record-1
  kind: record_content
  reference: data/structures/membrane_organelle/photosynthetic_membrane.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T20:10:29Z'
  support: context_only
  summary: Original frozen SHA256 5fe446aae99635ba843cf22d1144ab1312a2c30224367c49efd0bedcbd06db97;
    current SHA256 5fe446aae99635ba843cf22d1144ab1312a2c30224367c49efd0bedcbd06db97.
    Record bytes unchanged since the original review.
  snapshot_sha256: 5fe446aae99635ba843cf22d1144ab1312a2c30224367c49efd0bedcbd06db97
- evidence_id: original-review-1
  kind: prior_review
  reference: reviews/structured/20261022T032301Z-photosynthetic-membrane-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T20:10:29Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 77366c398da4f6db5027b57932a0d70eb2fa789ea9ff11045430d2dda257fe93
- evidence_id: current-record-2
  kind: record_content
  reference: data/structures/membrane_organelle/plasma_membrane_derived_chromatophore_membrane.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T20:10:29Z'
  support: context_only
  summary: Original frozen SHA256 f3130fc795ff500febb7d273c6a7b281ec7d2cc230d6e44fb5363c6c9256b064;
    current SHA256 e2622df75241a3d18a0c08f64d1e59fc10f49da8ee8ed7843cf6f08df2020195.
    Changed record reassessed against current sources.
  snapshot_sha256: e2622df75241a3d18a0c08f64d1e59fc10f49da8ee8ed7843cf6f08df2020195
- evidence_id: original-review-2
  kind: prior_review
  reference: reviews/structured/20261022T032301Z-plasma-membrane-derived-chromatophore-membrane-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T20:10:29Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 0f187b643ca8c6237cb1a59d3cb021732cb8d620f31f8004c7b5ac6db67d1ace
- evidence_id: current-record-3
  kind: record_content
  reference: data/structures/membrane_organelle/plasma_membrane_derived_thylakoid_lumen.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T20:10:29Z'
  support: context_only
  summary: Original frozen SHA256 4b4fbe694529235b322625d85f5c210eddea0cc03e5e1a684d5bff2d698bca82;
    current SHA256 4b4fbe694529235b322625d85f5c210eddea0cc03e5e1a684d5bff2d698bca82.
    Record bytes unchanged since the original review.
  snapshot_sha256: 4b4fbe694529235b322625d85f5c210eddea0cc03e5e1a684d5bff2d698bca82
- evidence_id: original-review-3
  kind: prior_review
  reference: reviews/structured/20261022T032302Z-plasma-membrane-derived-thylakoid-lumen-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T20:10:29Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 7b0dd6c4c520177c2718ab94847ac8f1118eddcdf70d7fdab66344de65432ad5
- evidence_id: current-record-4
  kind: record_content
  reference: data/structures/membrane_organelle/plasma_membrane_derived_thylakoid_membrane.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T20:10:29Z'
  support: context_only
  summary: Original frozen SHA256 66205b2d304df6e2b425730f885ccf46de08dc94c99c60636eab667d3bf68410;
    current SHA256 50b81e60972c1a3c89a73cf685b98887a221a3b0ba379b10fee8be1765d167e0.
    Changed record reassessed against current sources.
  snapshot_sha256: 50b81e60972c1a3c89a73cf685b98887a221a3b0ba379b10fee8be1765d167e0
- evidence_id: original-review-4
  kind: prior_review
  reference: reviews/structured/20261022T032303Z-plasma-membrane-derived-thylakoid-membrane-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T20:10:29Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 199e73c73eaeb5c2f6b712174de004dc5937b00e4a13d2b7b3448ccb5c096b3e
- evidence_id: current-record-5
  kind: record_content
  reference: data/structures/membrane_organelle/plastid.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T20:10:29Z'
  support: context_only
  summary: Original frozen SHA256 1be30ab06bc2fbae9294930ceaf74b20a2d43d8af60986aa9ed0e07b9645ae81;
    current SHA256 1be30ab06bc2fbae9294930ceaf74b20a2d43d8af60986aa9ed0e07b9645ae81.
    Record bytes unchanged since the original review.
  snapshot_sha256: 1be30ab06bc2fbae9294930ceaf74b20a2d43d8af60986aa9ed0e07b9645ae81
- evidence_id: original-review-5
  kind: prior_review
  reference: reviews/structured/20261022T032303Z-plastid-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T20:10:29Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 1c42de1dc8e88cd7fff7a11e033c2a4955c21115be4c933cbd0398e4a39e7ec9
- evidence_id: current-record-6
  kind: record_content
  reference: data/structures/membrane_organelle/plastid_envelope.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T20:10:29Z'
  support: context_only
  summary: Original frozen SHA256 9033a6955c21d6043019061509c7ca1bf470bec884e7f4e1a5edc0080b680968;
    current SHA256 9033a6955c21d6043019061509c7ca1bf470bec884e7f4e1a5edc0080b680968.
    Record bytes unchanged since the original review.
  snapshot_sha256: 9033a6955c21d6043019061509c7ca1bf470bec884e7f4e1a5edc0080b680968
- evidence_id: original-review-6
  kind: prior_review
  reference: reviews/structured/20261022T032304Z-plastid-envelope-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T20:10:29Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 5fe2d0c23c716174f5967a19662fd0158f7b411d6af5d623ff086c6750999a81
- evidence_id: current-record-7
  kind: record_content
  reference: data/structures/membrane_organelle/plastid_inner_membrane.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T20:10:29Z'
  support: context_only
  summary: Original frozen SHA256 ceb12c6ee4451216ae406f17f68ea2d3730a6da302b38e8bb8fcabc532a6a4fa;
    current SHA256 ceb12c6ee4451216ae406f17f68ea2d3730a6da302b38e8bb8fcabc532a6a4fa.
    Record bytes unchanged since the original review.
  snapshot_sha256: ceb12c6ee4451216ae406f17f68ea2d3730a6da302b38e8bb8fcabc532a6a4fa
- evidence_id: original-review-7
  kind: prior_review
  reference: reviews/structured/20261022T032305Z-plastid-inner-membrane-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T20:10:29Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 7beb0aff217f2f0917394a45e58ed3d40d8f40f5671418a934aebb05b4c7af66
- evidence_id: current-record-8
  kind: record_content
  reference: data/structures/membrane_organelle/plastid_intermembrane_space.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T20:10:29Z'
  support: context_only
  summary: Original frozen SHA256 2ef21406931fb90ec3aead7f57ee12a4376ad3d95276c7db3c2a7ab324c73c5d;
    current SHA256 2ef21406931fb90ec3aead7f57ee12a4376ad3d95276c7db3c2a7ab324c73c5d.
    Record bytes unchanged since the original review.
  snapshot_sha256: 2ef21406931fb90ec3aead7f57ee12a4376ad3d95276c7db3c2a7ab324c73c5d
- evidence_id: original-review-8
  kind: prior_review
  reference: reviews/structured/20261022T032305Z-plastid-intermembrane-space-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T20:10:29Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: e582df2870c77ec17e21f8395ff224db0e6ddcb17a6ed2bf3341b2e7eb1570de
- evidence_id: current-record-9
  kind: record_content
  reference: data/structures/membrane_organelle/plastid_membrane.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T20:10:29Z'
  support: context_only
  summary: Original frozen SHA256 ae09183c12ecb85ac2135b3615b9a613985285039f5730126227fde982e55bef;
    current SHA256 ae09183c12ecb85ac2135b3615b9a613985285039f5730126227fde982e55bef.
    Record bytes unchanged since the original review.
  snapshot_sha256: ae09183c12ecb85ac2135b3615b9a613985285039f5730126227fde982e55bef
- evidence_id: original-review-9
  kind: prior_review
  reference: reviews/structured/20261022T032306Z-plastid-membrane-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T20:10:29Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 876aef10c0601ebfb1e46596c4090506f360e0d84cda4dbbf822b0cd38d67ff2
- evidence_id: septin-review-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Current molecular/pathway applicability and bounded fallback
  summary: Positive molecular or pathway assertions trigger structured-source applicability
    even without an expression claim or individual examples. Use matched organism/strain
    evidence and distinguish source unavailability from scientific absence.
  accessed_at: '2026-11-03T20:08:14.850367Z'
  support: supports
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: septin-curation-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Identity, source-specific evidence, generic classes and append-only discussion
  summary: Exact structure identity, constituent identity, localization and formation
    necessity are distinct. Dated rationale is provenance, not current inventory;
    optional examples and generic classes do not automatically require curation.
  accessed_at: '2026-11-03T20:08:14.850367Z'
  support: supports
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
- evidence_id: septin-schema-policy
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Current structure, material, graph and evidence contract
  summary: Collective material, molecular complexes and structure nodes are distinct
    native representations. No enum-only complex defect or guessed chemical/protein
    CURIE is introduced.
  accessed_at: '2026-11-03T20:08:14.850367Z'
  support: supports
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: septin-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Mechanistic scope and graph actors/relations
  summary: Parthood and broad process associations must not be presented as a represented
    explanatory actor/transition mechanism. Graph source observations must match the
    actual frozen version.
  accessed_at: '2026-11-03T20:08:14.850367Z'
  support: supports
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: septin-protein-policy
  kind: authority
  reference: .claude/skills/uniprot-protein-examples/SKILL.md
  locator: Native examples and graph coverage
  summary: Native accession/coverage checks certify the represented scope; an empty
    inventory is neither molecular completeness nor biological absence.
  accessed_at: '2026-11-03T20:08:14.850367Z'
  support: supports
  snapshot_sha256: 6462894c8257823bae2b175c34693cd42f11ff9269a3829c15b9286ba6d7c876
- evidence_id: septin-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0106174,GO:0032010,GO:0097013,GO:0060205,GO:0045335,GO:0030670,GO:0090383,GO:0031979,GO:0031676,GO:0030075,GO:0009579,GO:0042651,GO:0030094,GO:0030096,GO:0009512,GO:0045259,GO:0009767
  locator: 'All17 exact current GO entries: definitions, identifiers, synonyms and
    immediate typed relations'
  summary: GO0106174 supplies the phagolysosome lumen volume definition, with broader
    phagocytic-lumen and whole-organelle boundaries; it does not supply the appended
    cross-taxon enzyme/ROS program. GO0031979 and GO0031676 identify bacterial thylakoid
    lumen/membrane. GO0030075 allows derivation/association without obligatory physical
    continuity with plasma membrane; GO0009579 explicitly excludes organelle classification.
    GO complex/process definitions support PSII, PSI, b6f, F-type ATP synthase and
    electron transport, without proving individual formation necessity. Direct whole-thylakoid
    part relations are not silently treated as direct membrane-part ontology axioms.
  accessed_at: '2026-11-03T20:00:23.058739Z'
  support: supports
  snapshot_sha256: 47cdc2b5191002c767e3a06ebd7660e7a170bc9190e22c7876de8666b480d3e2
- evidence_id: septin-SL0044
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0044.json
  locator: Exact location definition, synonyms/GO mapping and immediate isA/partOf
    fields; nested boundary text read
  summary: Exact cellular-thylakoid lumen maps GO0031979; immediate partOf cellular
    thylakoid supports boundary. Nested Synechocystis discontinuity description is
    background, not the organism of Huokko2021.
  accessed_at: '2026-11-03T20:00:23.059030Z'
  support: supports
  snapshot_sha256: ac9afb75436945fe5aa2b05c693b8eb87cb6511b9907d3bc922b43d81ad136a8
- evidence_id: septin-SL0045
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0045.json
  locator: Exact location definition, synonyms/GO mapping and immediate isA/partOf
    fields; nested boundary text read
  summary: Exact cellular-thylakoid membrane maps GO0031676 and partOf cellular thylakoid.
    Nested SL0043 calls discontinuous Synechocystis membranes organelles whereas GO0009579
    says thylakoids are not organelles; target native MEMBRANE/SUBCELLULAR_REGION
    classification is retained without inventing an enum defect.
  accessed_at: '2026-11-03T20:00:23.059137Z'
  support: supports
  snapshot_sha256: ef7ca37f3d79b995c2c2f4d5f47200aa88b6166b17c66bf4792a5dfc1cf77af6
- evidence_id: septin-SL0342
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0342.json
  locator: Exact location definition, synonyms/GO mapping and immediate isA/partOf
    fields; nested boundary text read
  summary: Broader phagosome lumen has phagocytic/phagosomal synonyms, cytoplasmic-vesicle-lumen
    parent and phagosome parthood. It is not exact phagolysosome-lumen identity or
    a molecular-program source.
  accessed_at: '2026-11-03T20:00:23.059184Z'
  support: supports
  snapshot_sha256: b241eb5f4701f414d2e4911c8d661922bd28e3523f6082c25a73e56375a18dd8
- evidence_id: septin-tax1117
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1117
  locator: 'Complete current ENA/NCBI taxonomy response: identifier, rank, status,
    lineage and supplied aliases'
  summary: Active Cyanobacteriota phylum, used for broad occurrence rather than experiment
    identity. Qualitative COMMON occurrence is not a census or every-strain guarantee.
  accessed_at: '2026-11-03T20:00:23.059224Z'
  support: supports
  snapshot_sha256: 5f4919ad6f362a82291b587d27134147f277ffc5fa593f6076f1983a704cd985
- evidence_id: septin-tax1148
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1148
  locator: 'Complete current ENA/NCBI taxonomy response: identifier, rank, status,
    lineage and supplied aliases'
  summary: Synechocystis sp. PCC6803 species taxon; distinct from the experimental
    Synechococcus lineage. Qualitative COMMON occurrence is not a census or every-strain
    guarantee.
  accessed_at: '2026-11-03T20:00:23.650521Z'
  support: supports
  snapshot_sha256: 84c0a354189f6b736c57eb3886dc08090cd6edba80c6e35c1b92909c26f35ab4
- evidence_id: septin-tax1140
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1140
  locator: 'Complete current ENA/NCBI taxonomy response: identifier, rank, status,
    lineage and supplied aliases'
  summary: Synechococcus elongatus PCC7942 strain, including FACHB805 synonym. This
    is the host used by Casella2017 and Huokko2021, not PCC6803. Qualitative COMMON
    occurrence is not a census or every-strain guarantee.
  accessed_at: '2026-11-03T20:00:23.660737Z'
  support: supports
  snapshot_sha256: 70bf02b8ca783e9afbd060d6c098a79cec71954ea2d64a270fc130481a63cb2b
- evidence_id: septin-tax44689
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/44689
  locator: 'Complete current ENA/NCBI taxonomy response: identifier, rank, status,
    lineage and supplied aliases'
  summary: Active Dictyostelium discoideum species; the primary study independently
    specifies Ax2 in HL5c at22C. Qualitative COMMON occurrence is not a census or
    every-strain guarantee.
  accessed_at: '2026-11-03T20:00:23.666326Z'
  support: supports
  snapshot_sha256: f7bfea542a721125d862d08a5f8dd0986c1c19034b45f1fb92adf8c8d045efca
- evidence_id: septin-perez2024-meta
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1146%2Fannurev-cellbio-120823-022747&format=json&resultType=core&pageSize=25
  locator: Exact DOI EuropePMC result; complete metadata and abstract
  summary: Perez Boerema, Engel and Wietrzynski2024 Evolution of Thylakoid Structural
    Diversity is a secondary review, PMID38950450. Metadata/abstract do not substitute
    for the separately read genuine body.
  accessed_at: '2026-11-03T20:00:23.684517Z'
  support: supports
  snapshot_sha256: f9df3427bb3b35764922628c9e89cc9378fa7875a4a103bde71a75b130d54926
  search_scope: EuropePMC REST exact DOI query as in reference URL, resultType=core,
    pageSize25, no date filter; one exact result and full abstract inspected at 2026-11-03T20:00:23.684517Z.
    No broad literature absence claim.
- evidence_id: septin-huokko2021-meta
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038%2Fs41467-021-23680-1&format=json&resultType=core&pageSize=25
  locator: Exact DOI EuropePMC result; complete metadata and abstract
  summary: Huokko2021 Probing the biogenesis pathway and dynamics of thylakoid membranes,
    PMID34108457/PMC8190092, explicitly studies Synechococcus elongatus7942.
  accessed_at: '2026-11-03T20:00:24.178914Z'
  support: supports
  snapshot_sha256: af3189fba6c317b70a180f0f879e06319c38aa25d407906fa3a9c9e4628f1ab5
  search_scope: EuropePMC REST exact DOI query as in reference URL, resultType=core,
    pageSize25, no date filter; one exact result and full abstract inspected at 2026-11-03T20:00:24.178914Z.
    No broad literature absence claim.
- evidence_id: septin-casella2017-meta
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1016%2Fj.molp.2017.09.019&format=json&resultType=core&pageSize=25
  locator: Exact DOI EuropePMC result; complete metadata and abstract
  summary: Casella2017 Dissecting the Native Architecture and Dynamics of Cyanobacterial
    Photosynthetic Machinery, PMID29017828/PMC5683893, explicitly studies Synechococcus
    elongatus7942.
  accessed_at: '2026-11-03T20:00:24.244880Z'
  support: supports
  snapshot_sha256: 1c47c2e672d5f9c2bc828bcd7f7112bfa00418cb7a683c5677e18e365e6acdf4
  search_scope: EuropePMC REST exact DOI query as in reference URL, resultType=core,
    pageSize25, no date filter; one exact result and full abstract inspected at 2026-11-03T20:00:24.244880Z.
    No broad literature absence claim.
- evidence_id: septin-casella2017-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5683893.1/PMC5683893.1.xml
  locator: Published JATS Results2.1/2.2/2.3 and Methods4.1/4.8, Fig1–5 text captions
    and Table1 text; no image pixels/supplements/raw data
  summary: Actual native organism is Synechococcus elongatus7942. Detergent-free thylakoid
    preparations, immunoblot/BN-PAGE and functional fluorescent tags support PSII,
    PSI, b6f and ATP-synthase thylakoid residence and conditional mobility. AFM b6f
    assignment is explicitly tentative; native-tag/confocal evidence is separate.
    BG11 at30C/50 microeinstein light is the experimental context. Synechocystis6803
    appears as comparison, not the studied FRAP host. Paper ATP-beta nomenclature
    is not silently converted to the unrelated database Fo-subunit-atpB name.
  accessed_at: '2026-11-03T20:01:07.430727Z'
  support: supports
  snapshot_sha256: 6e3c04f52b15e4ce163579c9c0c3a44b1946bded6fe47e1299e3ef6dc2ce18d7
- evidence_id: septin-huokko2021-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC8190092.1/PMC8190092.1.xml
  locator: Published JATS ResultsSec3/4 and MethodsSec9/12/13, Fig1/2 text captions;
    no pixels/supplements/raw data
  summary: Actual organism is Synechococcus elongatus7942. HL300 treatment followed
    by LL20 recovery at30C in BG11 was used to study thylakoid biogenesis with TEM/cryoET.
    New membrane fragments occur near plasma membrane/preexisting thylakoids, but
    no apparent direct plasma-membrane connection/fusion was observed. Tentative VIPP1-like
    objects remain tentative. Synechocystis6803 is comparative background, not the
    canonical experiment. No universal continuity or causal formation necessity is
    inferred.
  accessed_at: '2026-11-03T20:01:07.431996Z'
  support: supports
  snapshot_sha256: 0140e3b1a9fbb1fe170d186f153c24e08fb32c4cc91754a49facf09cdc67ff21
- evidence_id: septin-perez2024-delivered
  kind: authority
  reference: https://www.annualreviews.org/docserver/ahah/fulltext/cellbio/40/1/annurev-cellbio-120823-022747.html?expires=1793737002&id=id&accname=guest&checksum=47EAFDAB41E06430970416431EF37629
  locator: 'Genuine publisher-delivered secondary full-text HTML fragment: Introduction,
    Building Blocks/Lipids and Electron Transport Chain Complexes, Fig1/2 text captions;
    no pixels or reference-body audit'
  summary: Secondary review explicitly describes lumen separation/proton gradients,
    Gloeobacter exception, collective galactolipid-rich membrane and four major ETC/ATP-synthesis
    complexes. PSII water oxidation, b6f proton transfer, PSI electron transfer and
    proton-gradient-driven ATP synthase are contextual synthesis. Supports the newly
    added ATP-synthase residence edge; no new exact subunit stoichiometry, universal
    lipid percentage or individual formation-necessity claim is inferred. Publisher
    landing page alone was a loading shell; the actual body was retrieved through
    its public delivery link.
  accessed_at: '2026-11-03T20:02:23.441867Z'
  support: supports
  snapshot_sha256: d4cb1bbd456fe36ec6dfcbcf218853b725e963929a7ae54588784df02577dd4a
- evidence_id: septin-PMID12388753
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12388753+AND+SRC%3AMED&format=json&resultType=core&pageSize=25
  locator: 'Cached exact EuropePMC MED record: complete metadata/abstract reread now'
  summary: Gotthardt2002 High-resolution dissection of phagosome maturation reveals
    distinct membrane trafficking phases, PMID12388753/PMC129962/DOI10.1091/mbc.e02-04-0206.
    Abstract describes Ax2 pulse-chase trafficking, two hydrolase-delivery phases
    and recycling; direct pH measurement is not the reported assay. Cached source
    was retrieved at 2026-11-03T19:21:29.422467Z; current reinspection is not a fresh
    HTTP access.
  accessed_at: '2026-11-03T19:21:29.422467Z'
  support: supports
  snapshot_sha256: 7ba1845e0950b4eb8287d04190a939a374cb06b9baee8d880bbd3829a813c22c
  search_scope: Original EuropePMC EXT_ID:12388753 AND SRC:MED, resultType=core, pageSize25,
    no date filter; one exact hit; cached bytes reread now, retaining actual original
    access time.
- evidence_id: septin-gotthardt2002-unige-pdf
  kind: primary_source
  reference: https://access.archive-ouverte.unige.ch/access/metadata/7ba3d74f-e1a5-4cae-8646-670a6fd9a236/download
  locator: Cached published primary PDF pp3508–3518 inspected in PR2374; current reread
    Methods pp3509–3510 and Discussion/Fig7 text pp3517–3518; complete abstract also
    reread. No new pixel/raw/supplement audit
  summary: Actual Ax2 latex-bead pulse/chase purification, immunoblot/protein-lipid
    analyses and microscopy resolve trafficking/composition. Current Methods reread
    confirms no direct luminal-pH assay; Discussion combines own and prior work, citing
    Maniak1999/2001 for acidification. CatD/CPp34 delivery/recycling does not establish
    the entire asserted cross-taxon protease/lysozyme/phospholipase/ROS program. This
    is an attribution/scope limit, not denial of qualitative acidification or any
    particular organism biology. Cached source was retrieved at 2026-11-03T19:23:10.499151Z;
    current reinspection is not a fresh HTTP access.
  accessed_at: '2026-11-03T19:23:10.499151Z'
  support: supports
  snapshot_sha256: b04b33f2e5723103549505bc97a1c300da11fa3f6fc279ed8315c18e1c8e1602
- evidence_id: septin-catalogue
  kind: search
  reference: https://imodulondb.org/api/datasets
  locator: Complete fresh official organism/dataset catalogue; all rows/dataset strings
    inspected
  summary: s_elongatus/elprecise300 is available; selected gene identities explicitly
    carry Synpcc7942 and tax1140 string IDs. No Synechocystis6803, Dictyostelium/Ax2,
    Entamoeba or ciliate host dataset occurs. PCC7942 evidence is relevant to the
    actual cited experiments and broad cyanobacterial pathway, never a substitute
    for the incorrect PCC6803 attribution. Catalogue noncoverage is not biological
    absence.
  accessed_at: '2026-11-03T20:00:24.254005Z'
  support: supports
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  search_scope: GET https://imodulondb.org/api/datasets at 2026-11-03T20:00:24.254005Z;
    complete20 organism rows,28 organism-dataset pairs,22 distinct dataset strings,
    no filters/date restriction/truncation. Inspected all names, IDs, descriptions
    and keys for the named hosts and actual primary-study strain.
- evidence_id: septin-adapter-search-photosystem
  kind: search
  reference: https://imodulondb.org/api/search?organism=s_elongatus&dataset=elprecise300&query=photosystem&limit=50
  locator: Official matched-host dataset search response, complete returned structured
    hits
  summary: 36 gene hits and modules38 Photosystems/1 PSII. These queries corroborate
    relevant source coverage, not molecular necessity or completeness.
  accessed_at: '2026-11-03T20:01:40.929615Z'
  support: supports
  snapshot_sha256: 72f73baf5ddd33b5afb9073db878e46cc3dca85f09ad8cc87e46c5014e472878
  search_scope: GET https://imodulondb.org/api/search?organism=s_elongatus&dataset=elprecise300&query=photosystem&limit=50
    at 2026-11-03T20:01:40.929615Z; organism=s_elongatus,dataset=elprecise300, exact
    query in URL, limit50, no date filter. All returned structured hits inspected;
    no absence inferred beyond returned search.
- evidence_id: septin-adapter-search-cytochrome-b6
  kind: search
  reference: https://imodulondb.org/api/search?organism=s_elongatus&dataset=elprecise300&query=cytochrome+b6&limit=50
  locator: Official matched-host dataset search response, complete returned structured
    hits
  summary: Seven gene hits, including petB Synpcc7942_2331; no module hit in this
    bounded text search. These queries corroborate relevant source coverage, not molecular
    necessity or completeness.
  accessed_at: '2026-11-03T20:01:40.929706Z'
  support: supports
  snapshot_sha256: da117375554693bbcb4301ca4e817c01b3ffe032762cd9851d2409ae2c74d2b5
  search_scope: GET https://imodulondb.org/api/search?organism=s_elongatus&dataset=elprecise300&query=cytochrome+b6&limit=50
    at 2026-11-03T20:01:40.929706Z; organism=s_elongatus,dataset=elprecise300, exact
    query in URL, limit50, no date filter. All returned structured hits inspected;
    no absence inferred beyond returned search.
- evidence_id: septin-adapter-search-ATP-synthase
  kind: search
  reference: https://imodulondb.org/api/search?organism=s_elongatus&dataset=elprecise300&query=ATP+synthase&limit=50
  locator: Official matched-host dataset search response, complete returned structured
    hits
  summary: Nine gene hits including atpA Synpcc7942_0336; no module hit in this bounded
    text search. Function labels are database annotations, not a new experimental
    validation. These queries corroborate relevant source coverage, not molecular
    necessity or completeness.
  accessed_at: '2026-11-03T20:01:40.929763Z'
  support: supports
  snapshot_sha256: 18a5d8f23d18d048b25f6d5ba9819772537fc1b613130cb0c8d0b5df8215254a
  search_scope: GET https://imodulondb.org/api/search?organism=s_elongatus&dataset=elprecise300&query=ATP+synthase&limit=50
    at 2026-11-03T20:01:40.929763Z; organism=s_elongatus,dataset=elprecise300, exact
    query in URL, limit50, no date filter. All returned structured hits inspected;
    no absence inferred beyond returned search.
- evidence_id: septin-adapter-search-thylakoid
  kind: search
  reference: https://imodulondb.org/api/search?organism=s_elongatus&dataset=elprecise300&query=thylakoid&limit=50
  locator: Official matched-host dataset search response, complete returned structured
    hits
  summary: Two gene hits including lepB1; no module hit in this bounded text search.
    These queries corroborate relevant source coverage, not molecular necessity or
    completeness.
  accessed_at: '2026-11-03T20:01:40.929810Z'
  support: supports
  snapshot_sha256: de2e39cd5b191d1fc60d4b1d6c0727738b4c24f02c88cfb21ea0ed836b9ab9e2
  search_scope: GET https://imodulondb.org/api/search?organism=s_elongatus&dataset=elprecise300&query=thylakoid&limit=50
    at 2026-11-03T20:01:40.929810Z; organism=s_elongatus,dataset=elprecise300, exact
    query in URL, limit50, no date filter. All returned structured hits inspected;
    no absence inferred beyond returned search.
- evidence_id: septin-adapter-gene-Synpcc7942_2049
  kind: authority
  reference: https://imodulondb.org/api/genes/s_elongatus/elprecise300/Synpcc7942_2049
  locator: 'Exact matched-host gene response: gene/locus, product, source tax1140
    string identifier and database accession'
  summary: Selected psaA identity corroborates PCC7942 scope. Unrecorded dataset accessions
    are contextual and are not proposed as new maintained protein examples or independent
    localization/causality evidence.
  accessed_at: '2026-11-03T20:02:23.443522Z'
  support: supports
  snapshot_sha256: dc7ed67b6ed59f60fab6caa30b381847e8870b54503570af4724cba694642cef
- evidence_id: septin-adapter-gene-Synpcc7942_2049-modules
  kind: search
  reference: https://imodulondb.org/api/genes/s_elongatus/elprecise300/Synpcc7942_2049/imodulons
  locator: All57 returned module-association rows; is_in_imodulon flags and relevant
    thresholds inspected
  summary: Single positive flag is module38 Photosystems. Threshold membership is
    dataset-specific and does not prove structural presence/absence, gene expression
    absence, regulation, causality or formation necessity.
  accessed_at: '2026-11-03T20:02:23.443849Z'
  support: supports
  snapshot_sha256: 0f0efec038067d4c2e41f6b6d825f909f836e06a77cb16d460c866e76aac4073
  search_scope: Exact GET https://imodulondb.org/api/genes/s_elongatus/elprecise300/Synpcc7942_2049/imodulons
    at 2026-11-03T20:02:23.443849Z for s_elongatus/elprecise300 and this one gene,
    full57 returned rows, no date filter or broader search. No raw expression matrix
    or condition reanalysis.
- evidence_id: septin-adapter-gene-Synpcc7942_0424
  kind: authority
  reference: https://imodulondb.org/api/genes/s_elongatus/elprecise300/Synpcc7942_0424
  locator: 'Exact matched-host gene response: gene/locus, product, source tax1140
    string identifier and database accession'
  summary: Selected psbA1 identity corroborates PCC7942 scope. Unrecorded dataset
    accessions are contextual and are not proposed as new maintained protein examples
    or independent localization/causality evidence.
  accessed_at: '2026-11-03T20:02:23.444237Z'
  support: supports
  snapshot_sha256: 3ae80dbc5a6ab3ad960f25fb963e20887269854fc3a3da1cbff004c1bf5ce50a
- evidence_id: septin-adapter-gene-Synpcc7942_0424-modules
  kind: search
  reference: https://imodulondb.org/api/genes/s_elongatus/elprecise300/Synpcc7942_0424/imodulons
  locator: All57 returned module-association rows; is_in_imodulon flags and relevant
    thresholds inspected
  summary: No true module-membership flag among the57 returned rows. Threshold membership
    is dataset-specific and does not prove structural presence/absence, gene expression
    absence, regulation, causality or formation necessity.
  accessed_at: '2026-11-03T20:02:23.497459Z'
  support: supports
  snapshot_sha256: e242213845e64fc758b1fec9479d3bb60d501b50df461f5f57f482c563aef45e
  search_scope: Exact GET https://imodulondb.org/api/genes/s_elongatus/elprecise300/Synpcc7942_0424/imodulons
    at 2026-11-03T20:02:23.497459Z for s_elongatus/elprecise300 and this one gene,
    full57 returned rows, no date filter or broader search. No raw expression matrix
    or condition reanalysis.
- evidence_id: septin-adapter-gene-Synpcc7942_2331
  kind: authority
  reference: https://imodulondb.org/api/genes/s_elongatus/elprecise300/Synpcc7942_2331
  locator: 'Exact matched-host gene response: gene/locus, product, source tax1140
    string identifier and database accession'
  summary: Selected petB identity corroborates PCC7942 scope. Unrecorded dataset accessions
    are contextual and are not proposed as new maintained protein examples or independent
    localization/causality evidence.
  accessed_at: '2026-11-03T20:02:23.500457Z'
  support: supports
  snapshot_sha256: 8fc2418671e788c8aeba8880cb283a02dffd648b256ad34898ddf6439267434a
- evidence_id: septin-adapter-gene-Synpcc7942_2331-modules
  kind: search
  reference: https://imodulondb.org/api/genes/s_elongatus/elprecise300/Synpcc7942_2331/imodulons
  locator: All57 returned module-association rows; is_in_imodulon flags and relevant
    thresholds inspected
  summary: Single positive flag is module38 Photosystems. Threshold membership is
    dataset-specific and does not prove structural presence/absence, gene expression
    absence, regulation, causality or formation necessity.
  accessed_at: '2026-11-03T20:02:23.506749Z'
  support: supports
  snapshot_sha256: c8b7521e1ac670fe08764cec2de07d8f54150eac10984f2a6cbf689830937e4b
  search_scope: Exact GET https://imodulondb.org/api/genes/s_elongatus/elprecise300/Synpcc7942_2331/imodulons
    at 2026-11-03T20:02:23.506749Z for s_elongatus/elprecise300 and this one gene,
    full57 returned rows, no date filter or broader search. No raw expression matrix
    or condition reanalysis.
- evidence_id: septin-adapter-gene-Synpcc7942_0336
  kind: authority
  reference: https://imodulondb.org/api/genes/s_elongatus/elprecise300/Synpcc7942_0336
  locator: 'Exact matched-host gene response: gene/locus, product, source tax1140
    string identifier and database accession'
  summary: Selected atpA ATP-synthase alpha identity corroborates PCC7942 scope. Unrecorded
    dataset accessions are contextual and are not proposed as new maintained protein
    examples or independent localization/causality evidence.
  accessed_at: '2026-11-03T20:02:23.534758Z'
  support: supports
  snapshot_sha256: 17c5019212c898cd0554bda946e02c85cd8f11682fe7935db501a50e3fd70712
- evidence_id: septin-adapter-gene-Synpcc7942_0336-modules
  kind: search
  reference: https://imodulondb.org/api/genes/s_elongatus/elprecise300/Synpcc7942_0336/imodulons
  locator: All57 returned module-association rows; is_in_imodulon flags and relevant
    thresholds inspected
  summary: No true module-membership flag among the57 returned rows. Threshold membership
    is dataset-specific and does not prove structural presence/absence, gene expression
    absence, regulation, causality or formation necessity.
  accessed_at: '2026-11-03T20:02:23.534828Z'
  support: supports
  snapshot_sha256: 2794d7d93899d2454920f1ccb4906dd7936bc98718aa79580032f4b8140e7fb5
  search_scope: Exact GET https://imodulondb.org/api/genes/s_elongatus/elprecise300/Synpcc7942_0336/imodulons
    at 2026-11-03T20:02:23.534828Z for s_elongatus/elprecise300 and this one gene,
    full57 returned rows, no date filter or broader search. No raw expression matrix
    or condition reanalysis.
- evidence_id: septin-adapter-module-1
  kind: authority
  reference: https://imodulondb.org/api/imodulons/s_elongatus/elprecise300/1
  locator: Exact module metadata and returned gene IDs/weights; generated prose and
    activities excluded
  summary: Module1 PSII has21 listed genes and does not include the four selected
    loci. Reported n_conditions=0 is endpoint metadata, not proof of a biologically
    conditionless experiment. No AI-generated summary is treated as scientific evidence.
  accessed_at: '2026-11-03T20:02:23.553512Z'
  support: supports
  snapshot_sha256: fe180c45de0f7400ffc349de6340de2a5f2fa1530e48f7995d8adcb60c9f0c59
- evidence_id: septin-adapter-module-38
  kind: authority
  reference: https://imodulondb.org/api/imodulons/s_elongatus/elprecise300/38
  locator: Exact module metadata and returned gene IDs/weights; generated prose and
    activities excluded
  summary: Module38 Photosystems has44 listed genes and includes psaA2049/petB2331,
    consistent with their positive gene-response flags. Reported n_conditions=0 is
    endpoint metadata, not proof of a biologically conditionless experiment. No AI-generated
    summary is treated as scientific evidence.
  accessed_at: '2026-11-03T20:02:23.564078Z'
  support: supports
  snapshot_sha256: 7236e5234640b6a379fa25dc2ac44375ba96a07d69f7a020e06741bcd94c0965
- evidence_id: septin-adapter-runner-historical
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical attempted runner; no fresh invocation
  summary: Actual00:49:00.848907Z–00:49:00.863225Z exit1 PermissionError reading pyvenv.cfg
    remains historical. Fresh HTTP catalogue/downstream/source fallback is separate
    and is not a new runner success.
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: supports
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: septin-retrieval-source-receipts
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/adversary-septin/source-receipts.json
  locator: Actual fresh HTTP receipts and byte hashes
  summary: Successful genuine body and official source endpoints are distinguished
    from publisher loading shell, intermediate delivery URL, dataset SPA shell and
    application script used only to locate public endpoints. Cached Gotthardt bytes
    and independently reread collaborating primary snapshots preserve their actual
    original timestamps.
  accessed_at: '2026-11-03T20:08:14.850367Z'
  support: supports
  snapshot_sha256: d46da46475fa2bbf3df7aea86d73d5d47dea0392abf1f14793ea7fc028fe6e04
- evidence_id: septin-retrieval-additional-source-receipts
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/adversary-septin/additional-source-receipts.json
  locator: Actual fresh HTTP receipts and byte hashes
  summary: Successful genuine body and official source endpoints are distinguished
    from publisher loading shell, intermediate delivery URL, dataset SPA shell and
    application script used only to locate public endpoints. Cached Gotthardt bytes
    and independently reread collaborating primary snapshots preserve their actual
    original timestamps.
  accessed_at: '2026-11-03T20:08:14.850367Z'
  support: supports
  snapshot_sha256: 06e8308d02198198a9151fc58ab616fb5762ec1140175019f609a7c56d1c654b
- evidence_id: septin-retrieval-downstream-source-receipts
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/adversary-septin/downstream-source-receipts.json
  locator: Actual fresh HTTP receipts and byte hashes
  summary: Successful genuine body and official source endpoints are distinguished
    from publisher loading shell, intermediate delivery URL, dataset SPA shell and
    application script used only to locate public endpoints. Cached Gotthardt bytes
    and independently reread collaborating primary snapshots preserve their actual
    original timestamps.
  accessed_at: '2026-11-03T20:08:14.850367Z'
  support: supports
  snapshot_sha256: ff8d60a7faba2b41d0402ac7ef15a516daf86a493d7569edcbdb6a8c391ed477
- evidence_id: septin-context-phagolysosome
  kind: record_content
  reference: data/structures/membrane_organelle/phagolysosome.yaml
  locator: 'Frozen boundary context only: identifier, label, definition, parent_structures,
    part_of, has_part and xrefs'
  summary: Bounded context read after root froze this exact input. No complete neighbor
    mechanism/verdict or existing issue disposition is inferred.
  accessed_at: '2026-11-03T20:08:14.850367Z'
  support: supports
  snapshot_sha256: 1aa7bcc22c4b8a9bb65c69fad0c276e2446d28534b72a8abf930ed0e64c70e1e
- evidence_id: septin-context-phagolysosome_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/phagolysosome_membrane.yaml
  locator: 'Frozen boundary context only: identifier, label, definition, parent_structures,
    part_of, has_part and xrefs'
  summary: Bounded context read after root froze this exact input. No complete neighbor
    mechanism/verdict or existing issue disposition is inferred.
  accessed_at: '2026-11-03T20:08:14.850367Z'
  support: supports
  snapshot_sha256: 7f7e638a499bf7a56376a0f51d9de765fe0e3b9f7563bdb2ee13e9d332306b32
- evidence_id: septin-context-bacterial_thylakoid
  kind: record_content
  reference: data/structures/membrane_organelle/bacterial_thylakoid.yaml
  locator: 'Frozen boundary context only: identifier, label, definition, parent_structures,
    part_of, has_part and xrefs'
  summary: Bounded context read after root froze this exact input. No complete neighbor
    mechanism/verdict or existing issue disposition is inferred.
  accessed_at: '2026-11-03T20:08:14.850367Z'
  support: supports
  snapshot_sha256: a134c6cf6fd6069f0a0ddc37f1e99ded9a32994b3b1fa16d2f9938e3e46b8c40
- evidence_id: septin-context-proton_transporting_atp_synthase_complex
  kind: record_content
  reference: data/structures/energy_complex/proton_transporting_atp_synthase_complex.yaml
  locator: 'Frozen boundary context only: identifier, label, definition, parent_structures,
    part_of, has_part and xrefs'
  summary: Bounded context read after root froze this exact input. No complete neighbor
    mechanism/verdict or existing issue disposition is inferred.
  accessed_at: '2026-11-03T20:08:14.850367Z'
  support: supports
  snapshot_sha256: ab93b5ffa055615dfc9de1edfb137773e1098b4f7e9eefdda9d0ea00961af4fb
- evidence_id: septin-record-phagolysosome_vesicle_lumen
  kind: record_content
  reference: data/structures/membrane_organelle/phagolysosome_vesicle_lumen.yaml
  locator: Complete current record at 659d5d9ce7e16c8607002bf1655db2f3c652e6e1
  summary: 'All identity, definition, components, taxa/examples, function/source notes,
    discussion/history and graph fields read. Independently counted0 individual examples,0
    GENE_OR_PROTEIN nodes,0 UniProtKB graph xrefs and no maintained images. '
  accessed_at: '2026-11-03T20:08:14.850367Z'
  support: supports
  snapshot_sha256: 096069e6ecc9f33d640dfb9621fa69dedfab50cb9a9f08e6186e9583a823c319
- evidence_id: septin-original-phagolysosome_vesicle_lumen
  kind: prior_review
  reference: reviews/structured/20261022T032300Z-phagolysosome-vesicle-lumen-audit/review.yaml
  locator: Complete immutable original YAML/Markdown pair, original findings/actions/verdict
    and source snapshot
  summary: Old source access/checks remain historical. Every inherited finding is
    retained with exact predecessor. Original frozen target bytes match current target.
  accessed_at: '2026-11-03T20:08:14.850367Z'
  support: supports
  snapshot_sha256: 9db7f19b1526966a1a2435120db2c562c33ebd62fe8b4799ee87d388564bb901
- evidence_id: septin-original-validation-phagolysosome_vesicle_lumen
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/adversary-septin/original-checks.json
  locator: Actual native validate/render, exact Markdown equality and original frozen/current
    target hash comparison
  summary: Native original validation/render exit0 and exact Markdown. Historical
    source target matches frozen input; current target matches. Schema validity does
    not certify scientific support.
  accessed_at: '2026-11-03T20:00:42.036332Z'
  support: supports
  snapshot_sha256: 0c9534050e3fc555d996ecc1471b9a84a36fccd40396a92ff7b586dc2748da59
- evidence_id: septin-native-phagolysosome_vesicle_lumen-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/phagolysosome_vesicle_lumen-uniprot-verify-receipt.json
  locator: Actual native receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/phagolysosome_vesicle_lumen-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: Exit0. Independently counted0 individual protein examples,0 GENE_OR_PROTEIN
    nodes and0 UniProtKB graph xrefs. Exit0 covers this empty represented scope, not
    complete molecular coverage or scientific validity. Positive narrative pathway
    assertions remain separately assessed.
  accessed_at: '2026-11-03T19:59:31.812655Z'
  support: supports
  snapshot_sha256: 9a635dac0ab7f599718692920a582536f52886f159e8baf5caa9171ff7c28bdc
- evidence_id: septin-native-phagolysosome_vesicle_lumen-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/phagolysosome_vesicle_lumen-uniprot-causal-receipt.json
  locator: Actual native receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/phagolysosome_vesicle_lumen-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: Exit0. Independently counted0 individual protein examples,0 GENE_OR_PROTEIN
    nodes and0 UniProtKB graph xrefs. Exit0 covers this empty represented scope, not
    complete molecular coverage or scientific validity. Positive narrative pathway
    assertions remain separately assessed.
  accessed_at: '2026-11-03T19:59:32.303614Z'
  support: supports
  snapshot_sha256: 04f4c1cae73d492e2f564ea469515497f52f3e5b040185a1a1fb553bf9c75583
- evidence_id: septin-record-plasma_membrane_derived_thylakoid_lumen
  kind: record_content
  reference: data/structures/membrane_organelle/plasma_membrane_derived_thylakoid_lumen.yaml
  locator: Complete current record at 659d5d9ce7e16c8607002bf1655db2f3c652e6e1
  summary: 'All identity, definition, components, taxa/examples, function/source notes,
    discussion/history and graph fields read. Independently counted0 individual examples,0
    GENE_OR_PROTEIN nodes,0 UniProtKB graph xrefs and no maintained images. '
  accessed_at: '2026-11-03T20:08:14.850367Z'
  support: supports
  snapshot_sha256: 4b4fbe694529235b322625d85f5c210eddea0cc03e5e1a684d5bff2d698bca82
- evidence_id: septin-original-plasma_membrane_derived_thylakoid_lumen
  kind: prior_review
  reference: reviews/structured/20261022T032302Z-plasma-membrane-derived-thylakoid-lumen-audit/review.yaml
  locator: Complete immutable original YAML/Markdown pair, original findings/actions/verdict
    and source snapshot
  summary: Old source access/checks remain historical. Every inherited finding is
    retained with exact predecessor. Original frozen target bytes match current target.
  accessed_at: '2026-11-03T20:08:14.850367Z'
  support: supports
  snapshot_sha256: 7b0dd6c4c520177c2718ab94847ac8f1118eddcdf70d7fdab66344de65432ad5
- evidence_id: septin-original-validation-plasma_membrane_derived_thylakoid_lumen
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/adversary-septin/original-checks.json
  locator: Actual native validate/render, exact Markdown equality and original frozen/current
    target hash comparison
  summary: Native original validation/render exit0 and exact Markdown. Historical
    source target matches frozen input; current target matches. Schema validity does
    not certify scientific support.
  accessed_at: '2026-11-03T20:00:43.227458Z'
  support: supports
  snapshot_sha256: 0c9534050e3fc555d996ecc1471b9a84a36fccd40396a92ff7b586dc2748da59
- evidence_id: septin-native-plasma_membrane_derived_thylakoid_lumen-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plasma_membrane_derived_thylakoid_lumen-uniprot-verify-receipt.json
  locator: Actual native receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plasma_membrane_derived_thylakoid_lumen-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: Exit0. Independently counted0 individual protein examples,0 GENE_OR_PROTEIN
    nodes and0 UniProtKB graph xrefs. Exit0 covers this empty represented scope, not
    complete molecular coverage or scientific validity. Positive narrative pathway
    assertions remain separately assessed.
  accessed_at: '2026-11-03T19:59:37.169586Z'
  support: supports
  snapshot_sha256: 43e70df07b94ee48071a9f8b8eea88e5e3c7447b0f3466e7c9241fde66bdac4e
- evidence_id: septin-native-plasma_membrane_derived_thylakoid_lumen-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plasma_membrane_derived_thylakoid_lumen-uniprot-causal-receipt.json
  locator: Actual native receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plasma_membrane_derived_thylakoid_lumen-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: Exit0. Independently counted0 individual protein examples,0 GENE_OR_PROTEIN
    nodes and0 UniProtKB graph xrefs. Exit0 covers this empty represented scope, not
    complete molecular coverage or scientific validity. Positive narrative pathway
    assertions remain separately assessed.
  accessed_at: '2026-11-03T19:59:37.666291Z'
  support: supports
  snapshot_sha256: 6b9b35f5b1e0bf9a595a4ad696d246345abb725e61e31615d692216097a8e6a7
- evidence_id: septin-record-plasma_membrane_derived_thylakoid_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/plasma_membrane_derived_thylakoid_membrane.yaml
  locator: Complete current record at 659d5d9ce7e16c8607002bf1655db2f3c652e6e1
  summary: All identity, definition, components, taxa/examples, function/source notes,
    discussion/history and graph fields read. Independently counted0 individual examples,0
    GENE_OR_PROTEIN nodes,0 UniProtKB graph xrefs and no maintained images. Current6-edge
    descriptive graph adds ATP-synthase structure residence.
  accessed_at: '2026-11-03T20:08:14.850367Z'
  support: supports
  snapshot_sha256: 50b81e60972c1a3c89a73cf685b98887a221a3b0ba379b10fee8be1765d167e0
- evidence_id: septin-original-plasma_membrane_derived_thylakoid_membrane
  kind: prior_review
  reference: reviews/structured/20261022T032303Z-plasma-membrane-derived-thylakoid-membrane-audit/review.yaml
  locator: Complete immutable original YAML/Markdown pair, original findings/actions/verdict
    and source snapshot
  summary: Old source access/checks remain historical. Every inherited finding is
    retained with exact predecessor. Target input changed; original graph assessment
    also misdescribed the old5-edge graph as including ATP residence.
  accessed_at: '2026-11-03T20:08:14.850367Z'
  support: supports
  snapshot_sha256: 199e73c73eaeb5c2f6b712174de004dc5937b00e4a13d2b7b3448ccb5c096b3e
- evidence_id: septin-original-validation-plasma_membrane_derived_thylakoid_membrane
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/adversary-septin/original-checks.json
  locator: Actual native validate/render, exact Markdown equality and original frozen/current
    target hash comparison
  summary: Native original validation/render exit0 and exact Markdown. Historical
    source target matches frozen input; current differs and is substantively refreshed.
    Schema validity does not certify scientific support.
  accessed_at: '2026-11-03T20:00:44.419767Z'
  support: supports
  snapshot_sha256: 0c9534050e3fc555d996ecc1471b9a84a36fccd40396a92ff7b586dc2748da59
- evidence_id: septin-native-plasma_membrane_derived_thylakoid_membrane-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plasma_membrane_derived_thylakoid_membrane-uniprot-verify-receipt.json
  locator: Actual native receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plasma_membrane_derived_thylakoid_membrane-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: Exit0. Independently counted0 individual protein examples,0 GENE_OR_PROTEIN
    nodes and0 UniProtKB graph xrefs. Exit0 covers this empty represented scope, not
    complete molecular coverage or scientific validity. Four GO-grounded protein-complex
    components and their STRUCTURE graph nodes remain real molecular assertions.
  accessed_at: '2026-11-03T19:59:38.148654Z'
  support: supports
  snapshot_sha256: 8bb506bc483a141bd2906f19b6e8d2d0167f1d2016ec2ec2158da95a5460369b
- evidence_id: septin-native-plasma_membrane_derived_thylakoid_membrane-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plasma_membrane_derived_thylakoid_membrane-uniprot-causal-receipt.json
  locator: Actual native receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plasma_membrane_derived_thylakoid_membrane-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: Exit0. Independently counted0 individual protein examples,0 GENE_OR_PROTEIN
    nodes and0 UniProtKB graph xrefs. Exit0 covers this empty represented scope, not
    complete molecular coverage or scientific validity. Four GO-grounded protein-complex
    components and their STRUCTURE graph nodes remain real molecular assertions.
  accessed_at: '2026-11-03T19:59:38.623974Z'
  support: supports
  snapshot_sha256: 1aa2062691d54683a2f27cf2a107d4bb60b6565260e44eb63f84053aee2530a9
- evidence_id: plaque-current-1
  kind: record_content
  reference: data/structures/membrane_organelle/photosynthetic_membrane.yaml
  locator: Entire current maintained record at 659d5d9ce7e16c8607002bf1655db2f3c652e6e1;
    all fields, graph edges, discussions and history
  summary: Photosynthetic membrane remains byte-identical to original freeze; chromatophore
    is stale and receives substantive current reassessment of retyped/grounded nodes
    and two new edges.
  accessed_at: '2026-11-03T20:09:38.622910Z'
  support: supports
  snapshot_sha256: 5fe446aae99635ba843cf22d1144ab1312a2c30224367c49efd0bedcbd06db97
- evidence_id: plaque-original-1
  kind: prior_review
  reference: reviews/structured/20261022T032301Z-photosynthetic-membrane-audit/review.yaml
  locator: Exact staleness-selected original YAML and deterministic native Markdown;
    source/evidence, assessments, checks, findings/actions and notes
  summary: Immutable original natively validates/renders; all20 historical frozen
    inputs match its source. Historical six-edge chromatophore assessment is not a
    current eight-edge certification.
  accessed_at: '2026-11-03T20:09:38.622910Z'
  support: supports
  snapshot_sha256: 77366c398da4f6db5027b57932a0d70eb2fa789ea9ff11045430d2dda257fe93
- evidence_id: plaque-current-2
  kind: record_content
  reference: data/structures/membrane_organelle/plasma_membrane_derived_chromatophore_membrane.yaml
  locator: Entire current maintained record at 659d5d9ce7e16c8607002bf1655db2f3c652e6e1;
    all fields, graph edges, discussions and history
  summary: Photosynthetic membrane remains byte-identical to original freeze; chromatophore
    is stale and receives substantive current reassessment of retyped/grounded nodes
    and two new edges.
  accessed_at: '2026-11-03T20:09:38.622910Z'
  support: supports
  snapshot_sha256: e2622df75241a3d18a0c08f64d1e59fc10f49da8ee8ed7843cf6f08df2020195
- evidence_id: plaque-original-2
  kind: prior_review
  reference: reviews/structured/20261022T032301Z-plasma-membrane-derived-chromatophore-membrane-audit/review.yaml
  locator: Exact staleness-selected original YAML and deterministic native Markdown;
    source/evidence, assessments, checks, findings/actions and notes
  summary: Immutable original natively validates/renders; all20 historical frozen
    inputs match its source. Historical six-edge chromatophore assessment is not a
    current eight-edge certification.
  accessed_at: '2026-11-03T20:09:38.622910Z'
  support: supports
  snapshot_sha256: 0f187b643ca8c6237cb1a59d3cb021732cb8d620f31f8004c7b5ac6db67d1ace
- evidence_id: plaque-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Current skill Structured Source Cross-Checks and evidence rules reread
  summary: Positive protein and pathway assertions trigger applicability even without
    expression-module assertions.
  accessed_at: '2026-11-03T20:09:38.622910Z'
  support: context_only
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: plaque-rubric
  kind: authority
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Previously read exact frozen checklist, unchanged
  summary: Identity, source scope, material, mechanism and necessity evaluated separately;
    optional inventory gaps alone are not findings.
  accessed_at: '2026-11-03T20:09:38.622910Z'
  support: context_only
  snapshot_sha256: e6b9e4b16a58c54402bed7bbee2c8b94a91d37562e8b0ee8b94ff0c829184a70
- evidence_id: plaque-graph-rubric
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Previously read exact graph contract, unchanged
  summary: Native schema permits families and protein complexes under GENE_OR_PROTEIN;
    retyping to STRUCTURE is not automatically a correction of an invalid prior enum.
  accessed_at: '2026-11-03T20:09:38.622910Z'
  support: context_only
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: plaque-schema-policy
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Exact frozen component, necessity and graph schema, unchanged
  summary: Label-only collective lipids differ from misgrounded whole membranes; local
    and GO whole-complex identity differs from a subunit accession.
  accessed_at: '2026-11-03T20:09:38.622910Z'
  support: context_only
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: plaque-history-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Previously read exact discussion/history policy, unchanged
  summary: Rationale/history are append-only; update current grounding and future-facing
    notes or append a resolution without erasing historical explanations.
  accessed_at: '2026-11-03T20:09:38.622910Z'
  support: context_only
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
- evidence_id: plaque-context-chromatophore_cytochrome_bc1_complex
  kind: record_content
  reference: data/structures/energy_complex/chromatophore_cytochrome_bc1_complex.yaml
  locator: Identity, definition, taxonomic/function/source fields and node inventory
    read after exact input freeze; not an exhaustive neighbor review
  summary: Exact local whole-complex context for RC-LH1-PufX, bc1 or peripheral LH2.
    Neighbor histories/issues and entire mechanisms are not adjudicated or resolved.
  accessed_at: '2026-11-03T20:09:38.622910Z'
  support: context_only
  snapshot_sha256: 7f6582722d2f5376262287856929ec073f8550493eee88c6cb92dfc7624ec7ed
- evidence_id: plaque-context-lh2_peripheral_light_harvesting_antenna_complex
  kind: record_content
  reference: data/structures/energy_complex/lh2_peripheral_light_harvesting_antenna_complex.yaml
  locator: Identity, definition, taxonomic/function/source fields and node inventory
    read after exact input freeze; not an exhaustive neighbor review
  summary: Exact local whole-complex context for RC-LH1-PufX, bc1 or peripheral LH2.
    Neighbor histories/issues and entire mechanisms are not adjudicated or resolved.
  accessed_at: '2026-11-03T20:09:38.622910Z'
  support: context_only
  snapshot_sha256: 4bb84c48c2bb27f1a8dded06f479771b494070977ef26e0b14f0708bc446a7ce
- evidence_id: plaque-context-rc_lh1_pufx_core_complex
  kind: record_content
  reference: data/structures/energy_complex/rc_lh1_pufx_core_complex.yaml
  locator: Identity, definition, taxonomic/function/source fields and node inventory
    read after exact input freeze; not an exhaustive neighbor review
  summary: Exact local whole-complex context for RC-LH1-PufX, bc1 or peripheral LH2.
    Neighbor histories/issues and entire mechanisms are not adjudicated or resolved.
  accessed_at: '2026-11-03T20:09:38.622910Z'
  support: context_only
  snapshot_sha256: 0a3a6fcfe54b7a355fd2903992f521fb2fc293ce984d4ede356dbc8460071824
- evidence_id: plaque-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0034357,GO:0042717,GO:0070112,GO:0030076,GO:0009767,GO:0019684,GO:0045259,GO:0016020
  locator: 'Complete fresh8-term response: id/name/definition/isObsolete/synonyms/typed
    children'
  summary: GO0034357 and0042717 match generic and purple-bacterial membranes;0070112
    is distinct organellar chromatophore.0019684 specifically defines oxygenic PSI/PSII
    light reactions.0045259 is active with exact F1-F0 complex synonym; location does
    not require a new whole-complex identity.
  accessed_at: '2026-11-03T20:01:00.848173Z'
  support: supports
  snapshot_sha256: 89ff19c82b09aca0d818d56ba07ccda3aae3b301bfad1fe9a62bd3ecefd86f05
- evidence_id: plaque-SL0042
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0042.json
  locator: Complete native location JSON definition/synonym/GO mapping
  summary: Explicit plasma-derived purple-bacterial photosynthetic membrane, RC/antenna/bc1/F0F1
    scope. This is localization authority, not a direct measurement of universal stoichiometry
    or formation necessity.
  accessed_at: '2026-11-03T20:01:00.848415Z'
  support: supports
  snapshot_sha256: f16f40b6a8cfdb7911506598df2106649cf2e49643691a2077726a4384262ead
- evidence_id: plaque-tax2
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2
  locator: Complete ENA taxId/scientificName/rank/lineage/alternate names
  summary: Verified exact maintained taxon identity and strain hierarchy. PCC6803/Kazusa,
    PCC7942, Cereibacter species and2.4.1/ATCC17025 strains remain distinct; taxonomy
    alone does not establish experimental localization or prevalence.
  accessed_at: '2026-11-03T20:01:00.848502Z'
  support: supports
  snapshot_sha256: 314bd7723b8dea04f1840809fb74e06c514664fba9c6a0619e8f12e2a6dceef1
- evidence_id: plaque-tax1063
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1063
  locator: Complete ENA taxId/scientificName/rank/lineage/alternate names
  summary: Verified exact maintained taxon identity and strain hierarchy. PCC6803/Kazusa,
    PCC7942, Cereibacter species and2.4.1/ATCC17025 strains remain distinct; taxonomy
    alone does not establish experimental localization or prevalence.
  accessed_at: '2026-11-03T20:01:00.848950Z'
  support: supports
  snapshot_sha256: ba4a84dcb70c81bb2219c9d1d1d48961fa88ddae6b9718624baeaac55e4a7edf
- evidence_id: plaque-tax272943
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/272943
  locator: Complete ENA taxId/scientificName/rank/lineage/alternate names
  summary: Verified exact maintained taxon identity and strain hierarchy. PCC6803/Kazusa,
    PCC7942, Cereibacter species and2.4.1/ATCC17025 strains remain distinct; taxonomy
    alone does not establish experimental localization or prevalence.
  accessed_at: '2026-11-03T20:01:00.849041Z'
  support: supports
  snapshot_sha256: d049cb77bc4090d3737dda669b8a5b0e418737c098f7bb33bb059334c96bb3b0
- evidence_id: plaque-tax349102
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/349102
  locator: Complete ENA taxId/scientificName/rank/lineage/alternate names
  summary: Verified exact maintained taxon identity and strain hierarchy. PCC6803/Kazusa,
    PCC7942, Cereibacter species and2.4.1/ATCC17025 strains remain distinct; taxonomy
    alone does not establish experimental localization or prevalence.
  accessed_at: '2026-11-03T20:01:00.853483Z'
  support: supports
  snapshot_sha256: 59d8f35326317c9ea5184e8e59b87685eb800002554d2ba3d08b813046ca7f9a
- evidence_id: plaque-tax1111708
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1111708
  locator: Complete ENA taxId/scientificName/rank/lineage/alternate names
  summary: Verified exact maintained taxon identity and strain hierarchy. PCC6803/Kazusa,
    PCC7942, Cereibacter species and2.4.1/ATCC17025 strains remain distinct; taxonomy
    alone does not establish experimental localization or prevalence.
  accessed_at: '2026-11-03T20:01:00.856517Z'
  support: supports
  snapshot_sha256: a059d5c8b13212e336d88e33ebf02c638ad3840710b5228abfff6fa8d5c065a0
- evidence_id: plaque-tax1117
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1117
  locator: Complete ENA taxId/scientificName/rank/lineage/alternate names Same-PR
    public snapshot independently reread; actual initial fetch timestamp/hash retained,
    not a new request.
  summary: Verified exact maintained taxon identity and strain hierarchy. PCC6803/Kazusa,
    PCC7942, Cereibacter species and2.4.1/ATCC17025 strains remain distinct; taxonomy
    alone does not establish experimental localization or prevalence.
  accessed_at: '2026-11-03T20:00:23.059224Z'
  support: supports
  snapshot_sha256: 5f4919ad6f362a82291b587d27134147f277ffc5fa593f6076f1983a704cd985
- evidence_id: plaque-tax1148
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1148
  locator: Complete ENA taxId/scientificName/rank/lineage/alternate names Same-PR
    public snapshot independently reread; actual initial fetch timestamp/hash retained,
    not a new request.
  summary: Verified exact maintained taxon identity and strain hierarchy. PCC6803/Kazusa,
    PCC7942, Cereibacter species and2.4.1/ATCC17025 strains remain distinct; taxonomy
    alone does not establish experimental localization or prevalence.
  accessed_at: '2026-11-03T20:00:23.650521Z'
  support: supports
  snapshot_sha256: 84c0a354189f6b736c57eb3886dc08090cd6edba80c6e35c1b92909c26f35ab4
- evidence_id: plaque-tax1140
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1140
  locator: Complete ENA taxId/scientificName/rank/lineage/alternate names Same-PR
    public snapshot independently reread; actual initial fetch timestamp/hash retained,
    not a new request.
  summary: Verified exact maintained taxon identity and strain hierarchy. PCC6803/Kazusa,
    PCC7942, Cereibacter species and2.4.1/ATCC17025 strains remain distinct; taxonomy
    alone does not establish experimental localization or prevalence.
  accessed_at: '2026-11-03T20:00:23.660737Z'
  support: supports
  snapshot_sha256: 70bf02b8ca783e9afbd060d6c098a79cec71954ea2d64a270fc130481a63cb2b
- evidence_id: plaque-casella2017-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1016%2Fj.molp.2017.09.019&format=json&resultType=core&pageSize=25
  locator: Exact bibliographic metadata and complete deposited PRIMARY abstract
  summary: Exact title/year/DOI/PMID and declared experimental context verified. Nielsen
    is abstract-only here; other detailed scopes are bound to separately inspected
    source bodies.
  accessed_at: '2026-11-03T20:01:04.451776Z'
  support: supports
  search_scope: EuropePMC exact DOI or PMID query encoded in URL at 2026-11-03T20:01:04.451776Z;
    pageSize25, first returned page, 1 total hits; inspected every returned metadata
    row and complete deposited abstract. No full-body claim from this response.
  snapshot_sha256: f9ab8e3e0ee2994d6ad8e8c4ba544e08a13d0874a6734e084db4cb03c97fecbe
- evidence_id: plaque-bahatyrova2004-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038%2Fnature02823&format=json&resultType=core&pageSize=25
  locator: Exact bibliographic metadata and complete deposited PRIMARY abstract
  summary: Exact title/year/DOI/PMID and declared experimental context verified. Nielsen
    is abstract-only here; other detailed scopes are bound to separately inspected
    source bodies.
  accessed_at: '2026-11-03T20:01:05.232006Z'
  support: supports
  search_scope: EuropePMC exact DOI or PMID query encoded in URL at 2026-11-03T20:01:05.232006Z;
    pageSize25, first returned page, 1 total hits; inspected every returned metadata
    row and complete deposited abstract. No full-body claim from this response.
  snapshot_sha256: cdd0a3a0fab5cf8136a8c5e9e2246441b2cbf420c78c71eaf28cf9620293f722
- evidence_id: plaque-comayras2005-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1074%2Fjbc.M412088200&format=json&resultType=core&pageSize=25
  locator: Exact bibliographic metadata and complete deposited PRIMARY abstract
  summary: Exact title/year/DOI/PMID and declared experimental context verified. Nielsen
    is abstract-only here; other detailed scopes are bound to separately inspected
    source bodies.
  accessed_at: '2026-11-03T20:01:05.485889Z'
  support: supports
  search_scope: EuropePMC exact DOI or PMID query encoded in URL at 2026-11-03T20:01:05.485889Z;
    pageSize25, first returned page, 1 total hits; inspected every returned metadata
    row and complete deposited abstract. No full-body claim from this response.
  snapshot_sha256: c7e1f7dc8ecab121f7081d005e200962fedb179219b51d1f04bef3272903be9e
- evidence_id: plaque-feniouk2002-pmid
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11867431+AND+SRC%3AMED&format=json&resultType=core&pageSize=25
  locator: Exact bibliographic metadata and complete deposited PRIMARY abstract
  summary: Exact title/year/DOI/PMID and declared experimental context verified. Nielsen
    is abstract-only here; other detailed scopes are bound to separately inspected
    source bodies.
  accessed_at: '2026-11-03T20:06:22.422767Z'
  support: supports
  search_scope: EuropePMC exact DOI or PMID query encoded in URL at 2026-11-03T20:06:22.422767Z;
    pageSize25, first returned page, 1 total hits; inspected every returned metadata
    row and complete deposited abstract. No full-body claim from this response.
  snapshot_sha256: da8fdb8afe6b2200561ca5fc42c6506b86ad032be65a87bbb5a538bc65bfb770
- evidence_id: plaque-nielsen2016-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038%2Fncomms12454&format=json&resultType=core&pageSize=25
  locator: Exact bibliographic metadata and complete deposited PRIMARY abstract
  summary: Exact title/year/DOI/PMID and declared experimental context verified. Nielsen
    is abstract-only here; other detailed scopes are bound to separately inspected
    source bodies.
  accessed_at: '2026-11-03T20:01:06.407695Z'
  support: supports
  search_scope: EuropePMC exact DOI or PMID query encoded in URL at 2026-11-03T20:01:06.407695Z;
    pageSize25, first returned page, 1 total hits; inspected every returned metadata
    row and complete deposited abstract. No full-body claim from this response.
  snapshot_sha256: 945d9435e2d307dae357550e7e5c2ffed58b79561880240a1ef0cee894253ad8
- evidence_id: plaque-sui2021-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1146%2Fannurev-biophys-062920-063657&format=json&resultType=core&pageSize=25
  locator: Exact metadata and complete deposited SECONDARY REVIEW abstract
  summary: Phycobilisome pigment-protein/linker organization and energy transfer provide
    boundary context only; no full Sui body or universal integral-membrane antenna
    assertion.
  accessed_at: '2026-11-03T20:01:06.308270Z'
  support: supports
  search_scope: EuropePMC exact DOI or PMID query encoded in URL at 2026-11-03T20:01:06.308270Z;
    pageSize25, first returned page, 1 total hits; inspected every returned metadata
    row and complete deposited abstract. No full-body claim from this response.
  snapshot_sha256: 89c1f01375e5e3f1a9745b339c91f1addde69ae97b688a91007b2d80b8894f80
- evidence_id: plaque-feniouk2002-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1016%2FS0006-3495%2802%2975470-2&format=json&resultType=core&pageSize=25
  locator: Exact DOI first-page search returned0; no body evidence
  summary: Initial exact DOI search produced no indexed hit in this request. Later
    exact PMID11867431 uniquely resolves the cited paper; zero search hits are not
    source nonexistence.
  accessed_at: '2026-11-03T20:01:06.065676Z'
  support: context_only
  search_scope: EuropePMC exact DOI or PMID query encoded in URL at 2026-11-03T20:01:06.065676Z;
    pageSize25, first returned page, 0 total hits; inspected every returned metadata
    row and complete deposited abstract. No full-body claim from this response.
  snapshot_sha256: 77a0835ccb1671554365ba2cfe01766a0867ae6ec013256d89cb9382144f61de
- evidence_id: plaque-casella2017-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5683893.1/PMC5683893.1.xml
  locator: Genuine PMC5683893 JATS Results2.1–2.4 including embeddedFig1–8 captions;
    Methods4.1/4.5/4.7/4.8. No figure pixels, supplements, rawdata, remaining Methods
    or Discussion audited
  summary: Actual S.elongatus PCC7942 wild type and tagged PsaE/CP47/PetA/ATPbeta;
    BG11,30C and stated illumination. Native-membrane AFM and live microscopy/FRAP
    do not establish PCC6803 experiments. Some b6f particle assignment is tentative;
    no blanket particle identity claim.
  accessed_at: '2026-11-03T20:01:07.430727Z'
  support: supports
  snapshot_sha256: 6e3c04f52b15e4ce163579c9c0c3a44b1946bded6fe47e1299e3ef6dc2ce18d7
- evidence_id: plaque-bahatyrova2004-pdf
  kind: primary_source
  reference: https://eprints.whiterose.ac.uk/id/eprint/102/1/huntercn1.pdf
  locator: Genuine university-hosted PDF pp1058–1061 complete scientific main text/Methods/Fig1–3
    captions; adjacent unrelated article matter excluded. No pixels/supplements
  summary: R.sphaeroides NCIB8253 native isolated membranes show RC-LH1-PufX arrays
    and LH2 contacts/clusters. Preparation/AFM context is retained. bc1 and ATPase
    positions were not localized by this AFM; PufX is not directly resolved. Illustrative
    organization is not universal architecture or an assembly-necessity test.
  accessed_at: '2026-11-03T20:01:07.474607Z'
  support: supports
  snapshot_sha256: 18b555872af69d3ebed8f51dcfab485e048eaa892d83e9ac71cb998564f3bd25
- evidence_id: plaque-feniouk2002-author-pdf
  kind: primary_source
  reference: https://www.home.uni-osnabrueck.de/wjunge/public/230.pdf
  locator: Genuine author-hosted PDF pp1115–1121 scientific main text, Methods, Results/Discussion,
    Fig1–6 captions/Table1; no figure pixels/rawdata
  summary: R.capsulatus B10 malate/photoheterotrophic cultures30C; isolated chromatophores.
    Flash-induced522nm electrochromic voltage shows RC and slower bc1 charge-transfer
    phases and inhibitor-sensitive ATPase proton flux. Coupling supports PMF use;
    direct luciferase ATP-product measurements cited from earlier work are not certified
    as new measurements in this paper.
  accessed_at: '2026-11-03T20:01:08.250369Z'
  support: supports
  snapshot_sha256: 3c82e4f25ab7e2e369b48c517184c91bb4670921722aa18f85c64adcc2a858df
- evidence_id: plaque-comayras-browser-initial
  kind: primary_source
  reference: https://www.researchgate.net/publication/8099149_Functional_consequences_of_the_organization_of_the_photosynthetic_apparatus_in_Rhodobacter_sphaeroides_I_Quinone_domains_and_excitation_transfer_in_chromatophores_and_reaction_centerantenna_complexes
  locator: Retained browser author-upload primary excerpt; initial lines0–626 and
    overlapping410–1241 include Introduction, Methods and initialResults; no complete
    body or pixels. Timestamp is immediately-after-access receipt time; native HTTP
    status not supplied.
  summary: Ga-strain excitation/quinone-pool work. Pool assay inhibits bc1 and removes
    voltage/pH gradients; normal cyclic routing is contextual, not a directly measured
    unperturbed PMF result.
  accessed_at: '2026-11-03T20:02:48Z'
  support: supports
  snapshot_sha256: a9a6903527d7ede3cff1bdc642e75c2e1b4591e198ecbd76867eae44dfd956ec
- evidence_id: plaque-comayras-browser-methods
  kind: primary_source
  reference: https://www.researchgate.net/publication/8099149_Functional_consequences_of_the_organization_of_the_photosynthetic_apparatus_in_Rhodobacter_sphaeroides_I_Quinone_domains_and_excitation_transfer_in_chromatophores_and_reaction_centerantenna_complexes
  locator: Retained browser author-upload primary excerpt; initial lines0–626 and
    overlapping410–1241 include Introduction, Methods and initialResults; no complete
    body or pixels. Timestamp is immediately-after-access receipt time; native HTTP
    status not supplied.
  summary: Ga-strain excitation/quinone-pool work. Pool assay inhibits bc1 and removes
    voltage/pH gradients; normal cyclic routing is contextual, not a directly measured
    unperturbed PMF result.
  accessed_at: '2026-11-03T20:05:21Z'
  support: supports
  snapshot_sha256: fdc1704ac2f196f93e09c9cfebaf1a2bcb8bc4055300028aa1b5b172429d0618
- evidence_id: plaque-perez2024-delivered
  kind: authority
  reference: https://www.annualreviews.org/docserver/ahah/fulltext/cellbio/40/1/annurev-cellbio-120823-022747.html?expires=1793737002&id=id&accname=guest&checksum=47EAFDAB41E06430970416431EF37629
  locator: 'SECONDARY REVIEW publisher-delivered body: Introduction, evolutionary
    overview, Building Blocks, Lipids and Electron Transport Chain Complexes plus
    embeddedFig1/2 captions; not remaining body or pixels Same-PR public snapshot
    independently reread; actual initial fetch timestamp/hash retained, not a new
    request.'
  summary: Supports broad oxygenic membrane/lipid/photosystem/electron-carrier context
    and Gloeobacter exception. Its oxygenic pathway is not purple-bacterial photochemistry
    or experimental depletion/formation proof.
  accessed_at: '2026-11-03T20:02:23.441867Z'
  support: supports
  snapshot_sha256: d4cb1bbd456fe36ec6dfcbcf218853b725e963929a7ae54588784df02577dd4a
- evidence_id: plaque-protein-P29254
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P29254.json
  locator: 'Fresh native accession: primary name, gene/aliases/loci, exact organism/reviewed
    status, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY and InterPro cross-references'
  summary: Reviewed identity agrees with declared example. Native annotations distinguish
    experimental citations from HAMAP/by-similarity inference; family cross-references
    are contextual and not substitutes for whole-complex grounding. No formation necessity
    or exhaustive stoichiometry is inferred.
  accessed_at: '2026-11-03T20:01:00.856678Z'
  support: supports
  snapshot_sha256: 65acbde0deb06ea9ee1de6253044fdb57586f51af927c6ce6f2ddbc9c4050da3
- evidence_id: plaque-protein-P0C0Y8
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0C0Y8.json
  locator: 'Fresh native accession: primary name, gene/aliases/loci, exact organism/reviewed
    status, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY and InterPro cross-references'
  summary: Reviewed identity agrees with declared example. Native annotations distinguish
    experimental citations from HAMAP/by-similarity inference; family cross-references
    are contextual and not substitutes for whole-complex grounding. No formation necessity
    or exhaustive stoichiometry is inferred.
  accessed_at: '2026-11-03T20:01:01.520376Z'
  support: supports
  snapshot_sha256: fabd2b773ae1798d4d3b5bf03c09acba532309994d37002f3364f29b37a9e653
- evidence_id: plaque-protein-P0C0Y9
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0C0Y9.json
  locator: 'Fresh native accession: primary name, gene/aliases/loci, exact organism/reviewed
    status, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY and InterPro cross-references'
  summary: Reviewed identity agrees with declared example. Native annotations distinguish
    experimental citations from HAMAP/by-similarity inference; family cross-references
    are contextual and not substitutes for whole-complex grounding. No formation necessity
    or exhaustive stoichiometry is inferred.
  accessed_at: '2026-11-03T20:01:01.536651Z'
  support: supports
  snapshot_sha256: 3ffa18b43567cf4e99789ee683b4d2b00c4690760b99d99ba228d454ed783954
- evidence_id: plaque-protein-P16033
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P16033.json
  locator: 'Fresh native accession: primary name, gene/aliases/loci, exact organism/reviewed
    status, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY and InterPro cross-references'
  summary: Reviewed identity agrees with declared example. Native annotations distinguish
    experimental citations from HAMAP/by-similarity inference; family cross-references
    are contextual and not substitutes for whole-complex grounding. No formation necessity
    or exhaustive stoichiometry is inferred.
  accessed_at: '2026-11-03T20:01:01.537711Z'
  support: supports
  snapshot_sha256: 48d78d515a73f40f08b776f610f7f71eda49a822f898a908422cf293e0e6dc36
- evidence_id: plaque-protein-P26287
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P26287.json
  locator: 'Fresh native accession: primary name, gene/aliases/loci, exact organism/reviewed
    status, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY and InterPro cross-references'
  summary: Reviewed identity agrees with declared example. Native annotations distinguish
    experimental citations from HAMAP/by-similarity inference; family cross-references
    are contextual and not substitutes for whole-complex grounding. No formation necessity
    or exhaustive stoichiometry is inferred.
  accessed_at: '2026-11-03T20:01:01.545091Z'
  support: supports
  snapshot_sha256: 7ecc1c0fdc4daf1b6eac9fa350ffdf0cf196dca48197b6a590cb932a4dc2f9b1
- evidence_id: plaque-protein-Q57038
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q57038.json
  locator: 'Fresh native accession: primary name, gene/aliases/loci, exact organism/reviewed
    status, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY and InterPro cross-references'
  summary: Reviewed identity agrees with declared example. Native annotations distinguish
    experimental citations from HAMAP/by-similarity inference; family cross-references
    are contextual and not substitutes for whole-complex grounding. No formation necessity
    or exhaustive stoichiometry is inferred.
  accessed_at: '2026-11-03T20:01:01.550672Z'
  support: supports
  snapshot_sha256: 9df75bf783fb681317fb03ac9307134b92f54ede4d16a551abbc31aa24387a0a
- evidence_id: plaque-protein-Q02761
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q02761.json
  locator: 'Fresh native accession: primary name, gene/aliases/loci, exact organism/reviewed
    status, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY and InterPro cross-references'
  summary: Reviewed identity agrees with declared example. Native annotations distinguish
    experimental citations from HAMAP/by-similarity inference; family cross-references
    are contextual and not substitutes for whole-complex grounding. No formation necessity
    or exhaustive stoichiometry is inferred.
  accessed_at: '2026-11-03T20:01:01.572367Z'
  support: supports
  snapshot_sha256: e7735cdabb97caf68b9c821f79c7795a0bad1e1b1294c3e4e2b640df9d934141
- evidence_id: plaque-protein-Q02760
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q02760.json
  locator: 'Fresh native accession: primary name, gene/aliases/loci, exact organism/reviewed
    status, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY and InterPro cross-references'
  summary: Reviewed identity agrees with declared example. Native annotations distinguish
    experimental citations from HAMAP/by-similarity inference; family cross-references
    are contextual and not substitutes for whole-complex grounding. No formation necessity
    or exhaustive stoichiometry is inferred.
  accessed_at: '2026-11-03T20:01:01.574689Z'
  support: supports
  snapshot_sha256: db0c0729b8e3750330653a16dfd5fdd41380e00a93018d1f201df8286905e95f
- evidence_id: plaque-protein-P0C0Y0
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0C0Y0.json
  locator: 'Fresh native accession: primary name, gene/aliases/loci, exact organism/reviewed
    status, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY and InterPro cross-references'
  summary: Reviewed identity agrees with declared example. Native annotations distinguish
    experimental citations from HAMAP/by-similarity inference; family cross-references
    are contextual and not substitutes for whole-complex grounding. No formation necessity
    or exhaustive stoichiometry is inferred.
  accessed_at: '2026-11-03T20:01:01.780041Z'
  support: supports
  snapshot_sha256: 400956bf4478dd3351939ef06edeea0b6b5076faf74ac7d306bbe8a485d365d8
- evidence_id: plaque-protein-P0C0Y2
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0C0Y2.json
  locator: 'Fresh native accession: primary name, gene/aliases/loci, exact organism/reviewed
    status, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY and InterPro cross-references'
  summary: Reviewed identity agrees with declared example. Native annotations distinguish
    experimental citations from HAMAP/by-similarity inference; family cross-references
    are contextual and not substitutes for whole-complex grounding. No formation necessity
    or exhaustive stoichiometry is inferred.
  accessed_at: '2026-11-03T20:01:02.241350Z'
  support: supports
  snapshot_sha256: 87f9dfdbccde25c9a9258efeaba7ce4d1a173827f52e0902b7f4efabac1d354b
- evidence_id: plaque-protein-A4WUM7
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/A4WUM7.json
  locator: 'Fresh native accession: primary name, gene/aliases/loci, exact organism/reviewed
    status, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY and InterPro cross-references'
  summary: Reviewed identity agrees with declared example. Native annotations distinguish
    experimental citations from HAMAP/by-similarity inference; family cross-references
    are contextual and not substitutes for whole-complex grounding. No formation necessity
    or exhaustive stoichiometry is inferred.
  accessed_at: '2026-11-03T20:01:02.350238Z'
  support: supports
  snapshot_sha256: 5c3aae23062a2df4d944cb0bdd71f3bdb0172e4d1d7b3ebaa37a3e8b13338c36
- evidence_id: plaque-protein-Q3J433
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q3J433.json
  locator: 'Fresh native accession: primary name, gene/aliases/loci, exact organism/reviewed
    status, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY and InterPro cross-references'
  summary: Reviewed identity agrees with declared example. Native annotations distinguish
    experimental citations from HAMAP/by-similarity inference; family cross-references
    are contextual and not substitutes for whole-complex grounding. No formation necessity
    or exhaustive stoichiometry is inferred.
  accessed_at: '2026-11-03T20:01:03.231557Z'
  support: supports
  snapshot_sha256: 32297fbd8e0d7ea8b1a198aa3e9ea6a1a173c47ff5d741c300ee174a12a475f1
- evidence_id: plaque-protein-Q3IZ12
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q3IZ12.json
  locator: 'Fresh native accession: primary name, gene/aliases/loci, exact organism/reviewed
    status, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY and InterPro cross-references'
  summary: Reviewed identity agrees with declared example. Native annotations distinguish
    experimental citations from HAMAP/by-similarity inference; family cross-references
    are contextual and not substitutes for whole-complex grounding. No formation necessity
    or exhaustive stoichiometry is inferred.
  accessed_at: '2026-11-03T20:01:03.335065Z'
  support: supports
  snapshot_sha256: adeb72617b0c8e6929af69eb2f91d4bf3663d2d9e0247456abda566ad90020e9
- evidence_id: plaque-protein-Q3IZ13
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q3IZ13.json
  locator: 'Fresh native accession: primary name, gene/aliases/loci, exact organism/reviewed
    status, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY and InterPro cross-references'
  summary: Reviewed identity agrees with declared example. Native annotations distinguish
    experimental citations from HAMAP/by-similarity inference; family cross-references
    are contextual and not substitutes for whole-complex grounding. No formation necessity
    or exhaustive stoichiometry is inferred.
  accessed_at: '2026-11-03T20:01:04.223408Z'
  support: supports
  snapshot_sha256: 9ef24a139908492f9978f6f81f757064dd2eea71ba8952a91afb5522a22c68d9
- evidence_id: plaque-reviewed-genes-1111708
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28reviewed%3Atrue%29+AND+%28taxonomy_id%3A1111708%29+AND+%28gene_exact%3ApsaA+OR+gene_exact%3ApsbA+OR+gene_exact%3ApsbA2+OR+gene_exact%3ApsbA3+OR+gene_exact%3ApetA+OR+gene_exact%3ApetB%29&format=json&size=500
  locator: All returned accession/gene/taxon rows inspected; exact organism filtering
    after taxonomic-descendant query
  summary: Four Kazusa and19 Cereibacter-descendant rows. Current examples remain
    unique under each exact asserted gene/taxon pairing; descendants are not collapsed
    into species-level duplicates. P16033 covers psbA2 andpsbA3 loci, not a claim
    that the genome contains only one psbA locus.
  accessed_at: '2026-11-03T20:06:22.422942Z'
  support: supports
  search_scope: UniProtKB reviewed:true AND taxonomy_id filter AND finite gene_exact
    OR list encoded in URL; 2026-11-03T20:06:22.422942Z; size500 first page; 4 rows
    returned/inspected. No unreviewed or genome-wide copy-number absence claim.
  snapshot_sha256: 285166640d6f8a36ab6eff1221eeaa85fce2af4c8d54edd4cd743238a279e7e8
- evidence_id: plaque-reviewed-genes-1063
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28reviewed%3Atrue%29+AND+%28taxonomy_id%3A1063%29+AND+%28gene_exact%3ApufL+OR+gene_exact%3ApufM+OR+gene_exact%3ApucA+OR+gene_exact%3ApucB+OR+gene_exact%3ApetB+OR+gene_exact%3AfbcB+OR+gene_exact%3ApetC+OR+gene_exact%3AfbcC+OR+gene_exact%3AatpA+OR+gene_exact%3AatpB+OR+gene_exact%3AatpD+OR+gene_exact%3AatpE%29&format=json&size=500
  locator: All returned accession/gene/taxon rows inspected; exact organism filtering
    after taxonomic-descendant query
  summary: Four Kazusa and19 Cereibacter-descendant rows. Current examples remain
    unique under each exact asserted gene/taxon pairing; descendants are not collapsed
    into species-level duplicates. P16033 covers psbA2 andpsbA3 loci, not a claim
    that the genome contains only one psbA locus.
  accessed_at: '2026-11-03T20:06:22.423061Z'
  support: supports
  search_scope: UniProtKB reviewed:true AND taxonomy_id filter AND finite gene_exact
    OR list encoded in URL; 2026-11-03T20:06:22.423061Z; size500 first page; 19 rows
    returned/inspected. No unreviewed or genome-wide copy-number absence claim.
  snapshot_sha256: 069f96b26978d4bf33cc19a694b4f5b0f218c7eb0aeee4eea5c077593f8c72e6
- evidence_id: plaque-PMID11788579
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11788579+AND+SRC%3AMED&format=json&resultType=core&pageSize=25
  locator: Exact MED metadata and complete deposited PRIMARY abstract; no full paper/pixels
  summary: Cited PCC6803 PSII or b6f composition/localization experiment matches bounded
    native annotation context. Tagging, isolated complexes and mutants remain study-specific;
    abstracts do not certify every full-paper mechanism or strain-general necessity.
  accessed_at: '2026-11-03T20:01:06.409173Z'
  support: supports
  search_scope: EuropePMC exact DOI or PMID query encoded in URL at 2026-11-03T20:01:06.409173Z;
    pageSize25, first returned page, 1 total hits; inspected every returned metadata
    row and complete deposited abstract. No full-body claim from this response.
  snapshot_sha256: 1e575e9dfa1c06162ecbf725b8a4504323eb0c4b86236ce2eed95a144e0ccd57
- evidence_id: plaque-PMID12069591
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12069591+AND+SRC%3AMED&format=json&resultType=core&pageSize=25
  locator: Exact MED metadata and complete deposited PRIMARY abstract; no full paper/pixels
  summary: Cited PCC6803 PSII or b6f composition/localization experiment matches bounded
    native annotation context. Tagging, isolated complexes and mutants remain study-specific;
    abstracts do not certify every full-paper mechanism or strain-general necessity.
  accessed_at: '2026-11-03T20:01:06.470916Z'
  support: supports
  search_scope: EuropePMC exact DOI or PMID query encoded in URL at 2026-11-03T20:01:06.470916Z;
    pageSize25, first returned page, 1 total hits; inspected every returned metadata
    row and complete deposited abstract. No full-body claim from this response.
  snapshot_sha256: 162bffe5a51b9eea811b8bf469328d23cfd017b6330323722425ec533a5c875f
- evidence_id: plaque-PMID19577535
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A19577535+AND+SRC%3AMED&format=json&resultType=core&pageSize=25
  locator: Exact MED metadata and complete deposited PRIMARY abstract; no full paper/pixels
  summary: Cited PCC6803 PSII or b6f composition/localization experiment matches bounded
    native annotation context. Tagging, isolated complexes and mutants remain study-specific;
    abstracts do not certify every full-paper mechanism or strain-general necessity.
  accessed_at: '2026-11-03T20:01:07.219206Z'
  support: supports
  search_scope: EuropePMC exact DOI or PMID query encoded in URL at 2026-11-03T20:01:07.219206Z;
    pageSize25, first returned page, 1 total hits; inspected every returned metadata
    row and complete deposited abstract. No full-body claim from this response.
  snapshot_sha256: f6d6524080c3f45f47769fb2f4b5f8f078b143372fa39ef2a397a4148df04abc
- evidence_id: plaque-PMID34937700
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A34937700+AND+SRC%3AMED&format=json&resultType=core&pageSize=25
  locator: Exact MED metadata and complete deposited PRIMARY abstract; no full paper/pixels
  summary: Cited PCC6803 PSII or b6f composition/localization experiment matches bounded
    native annotation context. Tagging, isolated complexes and mutants remain study-specific;
    abstracts do not certify every full-paper mechanism or strain-general necessity.
  accessed_at: '2026-11-03T20:01:07.220595Z'
  support: supports
  search_scope: EuropePMC exact DOI or PMID query encoded in URL at 2026-11-03T20:01:07.220595Z;
    pageSize25, first returned page, 1 total hits; inspected every returned metadata
    row and complete deposited abstract. No full-body claim from this response.
  snapshot_sha256: d06cc93240a16bf28e353a7111d581f6679bb469aad7b4e271414a5bc3fdc3cc
- evidence_id: plaque-PMID35726684
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A35726684+AND+SRC%3AMED&format=json&resultType=core&pageSize=25
  locator: Exact MED metadata and complete deposited PRIMARY abstract; no full paper/pixels
  summary: Cited PCC6803 PSII or b6f composition/localization experiment matches bounded
    native annotation context. Tagging, isolated complexes and mutants remain study-specific;
    abstracts do not certify every full-paper mechanism or strain-general necessity.
  accessed_at: '2026-11-03T20:01:07.430608Z'
  support: supports
  search_scope: EuropePMC exact DOI or PMID query encoded in URL at 2026-11-03T20:01:07.430608Z;
    pageSize25, first returned page, 1 total hits; inspected every returned metadata
    row and complete deposited abstract. No full-body claim from this response.
  snapshot_sha256: a957f42881e5ff086ca1393bfa530c4013d52d9f11ff9a80fac336692b816e98
- evidence_id: plaque-catalogue
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Complete official catalogue independently inspected across every returned
    organism/dataset pair Same-PR public snapshot independently reread; actual initial
    fetch timestamp/hash retained, not a new request.
  summary: S.elongatus/elprecise300 is available, but no Synechocystis6803, Cereibacter/Rhodobacter
    sphaeroides or R.capsulatus dataset. PCC7942 context is relevant only to that
    source organism, not a replacement for canonicalPCC6803 or purple-host evidence.
  accessed_at: '2026-11-03T20:00:24.254005Z'
  support: supports
  search_scope: Official /api/datasets full returned catalogue at 2026-11-03T20:00:24.254005Z;
    all20organism rows/28organism-dataset pairs, exact scientific/historical host
    names checked. No other catalogue or unlisted host coverage inferred.
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: plaque-adapter-search-photosystem
  kind: search
  reference: https://imodulondb.org/api/search?organism=s_elongatus&dataset=elprecise300&query=photosystem&limit=50
  locator: Complete bounded official gene/module search response independently reread
    Same-PR public snapshot independently reread; actual initial fetch timestamp/hash
    retained, not a new request.
  summary: Matching molecular pathway context in PCC7942 source dataset only. Search
    hits are not structural membership, assembly requirements or cross-species evidence.
  accessed_at: '2026-11-03T20:01:40.929615Z'
  support: supports
  search_scope: iModulonDB s_elongatus/elprecise300; query and limit50 explicitly
    encoded in URL at 2026-11-03T20:01:40.929615Z; one response inspected, no unobserved
    pagination. Generated prose excluded.
  snapshot_sha256: 72f73baf5ddd33b5afb9073db878e46cc3dca85f09ad8cc87e46c5014e472878
- evidence_id: plaque-adapter-search-cytochrome-b6
  kind: search
  reference: https://imodulondb.org/api/search?organism=s_elongatus&dataset=elprecise300&query=cytochrome+b6&limit=50
  locator: Complete bounded official gene/module search response independently reread
    Same-PR public snapshot independently reread; actual initial fetch timestamp/hash
    retained, not a new request.
  summary: Matching molecular pathway context in PCC7942 source dataset only. Search
    hits are not structural membership, assembly requirements or cross-species evidence.
  accessed_at: '2026-11-03T20:01:40.929706Z'
  support: supports
  search_scope: iModulonDB s_elongatus/elprecise300; query and limit50 explicitly
    encoded in URL at 2026-11-03T20:01:40.929706Z; one response inspected, no unobserved
    pagination. Generated prose excluded.
  snapshot_sha256: da117375554693bbcb4301ca4e817c01b3ffe032762cd9851d2409ae2c74d2b5
- evidence_id: plaque-adapter-search-ATP-synthase
  kind: search
  reference: https://imodulondb.org/api/search?organism=s_elongatus&dataset=elprecise300&query=ATP+synthase&limit=50
  locator: Complete bounded official gene/module search response independently reread
    Same-PR public snapshot independently reread; actual initial fetch timestamp/hash
    retained, not a new request.
  summary: Matching molecular pathway context in PCC7942 source dataset only. Search
    hits are not structural membership, assembly requirements or cross-species evidence.
  accessed_at: '2026-11-03T20:01:40.929763Z'
  support: supports
  search_scope: iModulonDB s_elongatus/elprecise300; query and limit50 explicitly
    encoded in URL at 2026-11-03T20:01:40.929763Z; one response inspected, no unobserved
    pagination. Generated prose excluded.
  snapshot_sha256: 18a5d8f23d18d048b25f6d5ba9819772537fc1b613130cb0c8d0b5df8215254a
- evidence_id: plaque-adapter-search-thylakoid
  kind: search
  reference: https://imodulondb.org/api/search?organism=s_elongatus&dataset=elprecise300&query=thylakoid&limit=50
  locator: Complete bounded official gene/module search response independently reread
    Same-PR public snapshot independently reread; actual initial fetch timestamp/hash
    retained, not a new request.
  summary: Matching molecular pathway context in PCC7942 source dataset only. Search
    hits are not structural membership, assembly requirements or cross-species evidence.
  accessed_at: '2026-11-03T20:01:40.929810Z'
  support: supports
  search_scope: iModulonDB s_elongatus/elprecise300; query and limit50 explicitly
    encoded in URL at 2026-11-03T20:01:40.929810Z; one response inspected, no unobserved
    pagination. Generated prose excluded.
  snapshot_sha256: de2e39cd5b191d1fc60d4b1d6c0727738b4c24f02c88cfb21ea0ed836b9ab9e2
- evidence_id: plaque-adapter-gene-Synpcc7942_2049
  kind: database
  reference: https://imodulondb.org/api/genes/s_elongatus/elprecise300/Synpcc7942_2049
  locator: Complete selected native gene identity/product/string taxon metadata, no
    inferred interaction Same-PR public snapshot independently reread; actual initial
    fetch timestamp/hash retained, not a new request.
  summary: Synpcc7942 identifiers and STRING tax1140 establish exact PCC7942 context;
    selectedpsaA/psbA1/petB/atpA are not PCC6803 or purple-bacterial accession replacements.
  accessed_at: '2026-11-03T20:02:23.443522Z'
  support: supports
  snapshot_sha256: dc7ed67b6ed59f60fab6caa30b381847e8870b54503570af4724cba694642cef
- evidence_id: plaque-adapter-gene-Synpcc7942_2049-modules
  kind: database
  reference: https://imodulondb.org/api/genes/s_elongatus/elprecise300/Synpcc7942_2049/imodulons
  locator: All57 selected-gene module rows and threshold flags inspected Same-PR public
    snapshot independently reread; actual initial fetch timestamp/hash retained, not
    a new request.
  summary: psaA2049 andpetB2331 each pass only module38 threshold. psbA1_0424 andatpA0336
    have no true flags among these57rows. Below-threshold membership is not biological
    absence or lack of a photosystem/ATPase.
  accessed_at: '2026-11-03T20:02:23.443849Z'
  support: supports
  snapshot_sha256: 0f0efec038067d4c2e41f6b6d825f909f836e06a77cb16d460c866e76aac4073
- evidence_id: plaque-adapter-gene-Synpcc7942_0424
  kind: database
  reference: https://imodulondb.org/api/genes/s_elongatus/elprecise300/Synpcc7942_0424
  locator: Complete selected native gene identity/product/string taxon metadata, no
    inferred interaction Same-PR public snapshot independently reread; actual initial
    fetch timestamp/hash retained, not a new request.
  summary: Synpcc7942 identifiers and STRING tax1140 establish exact PCC7942 context;
    selectedpsaA/psbA1/petB/atpA are not PCC6803 or purple-bacterial accession replacements.
  accessed_at: '2026-11-03T20:02:23.444237Z'
  support: supports
  snapshot_sha256: 3ae80dbc5a6ab3ad960f25fb963e20887269854fc3a3da1cbff004c1bf5ce50a
- evidence_id: plaque-adapter-gene-Synpcc7942_0424-modules
  kind: database
  reference: https://imodulondb.org/api/genes/s_elongatus/elprecise300/Synpcc7942_0424/imodulons
  locator: All57 selected-gene module rows and threshold flags inspected Same-PR public
    snapshot independently reread; actual initial fetch timestamp/hash retained, not
    a new request.
  summary: psaA2049 andpetB2331 each pass only module38 threshold. psbA1_0424 andatpA0336
    have no true flags among these57rows. Below-threshold membership is not biological
    absence or lack of a photosystem/ATPase.
  accessed_at: '2026-11-03T20:02:23.497459Z'
  support: supports
  snapshot_sha256: e242213845e64fc758b1fec9479d3bb60d501b50df461f5f57f482c563aef45e
- evidence_id: plaque-adapter-gene-Synpcc7942_2331
  kind: database
  reference: https://imodulondb.org/api/genes/s_elongatus/elprecise300/Synpcc7942_2331
  locator: Complete selected native gene identity/product/string taxon metadata, no
    inferred interaction Same-PR public snapshot independently reread; actual initial
    fetch timestamp/hash retained, not a new request.
  summary: Synpcc7942 identifiers and STRING tax1140 establish exact PCC7942 context;
    selectedpsaA/psbA1/petB/atpA are not PCC6803 or purple-bacterial accession replacements.
  accessed_at: '2026-11-03T20:02:23.500457Z'
  support: supports
  snapshot_sha256: 8fc2418671e788c8aeba8880cb283a02dffd648b256ad34898ddf6439267434a
- evidence_id: plaque-adapter-gene-Synpcc7942_2331-modules
  kind: database
  reference: https://imodulondb.org/api/genes/s_elongatus/elprecise300/Synpcc7942_2331/imodulons
  locator: All57 selected-gene module rows and threshold flags inspected Same-PR public
    snapshot independently reread; actual initial fetch timestamp/hash retained, not
    a new request.
  summary: psaA2049 andpetB2331 each pass only module38 threshold. psbA1_0424 andatpA0336
    have no true flags among these57rows. Below-threshold membership is not biological
    absence or lack of a photosystem/ATPase.
  accessed_at: '2026-11-03T20:02:23.506749Z'
  support: supports
  snapshot_sha256: c8b7521e1ac670fe08764cec2de07d8f54150eac10984f2a6cbf689830937e4b
- evidence_id: plaque-adapter-gene-Synpcc7942_0336
  kind: database
  reference: https://imodulondb.org/api/genes/s_elongatus/elprecise300/Synpcc7942_0336
  locator: Complete selected native gene identity/product/string taxon metadata, no
    inferred interaction Same-PR public snapshot independently reread; actual initial
    fetch timestamp/hash retained, not a new request.
  summary: Synpcc7942 identifiers and STRING tax1140 establish exact PCC7942 context;
    selectedpsaA/psbA1/petB/atpA are not PCC6803 or purple-bacterial accession replacements.
  accessed_at: '2026-11-03T20:02:23.534758Z'
  support: supports
  snapshot_sha256: 17c5019212c898cd0554bda946e02c85cd8f11682fe7935db501a50e3fd70712
- evidence_id: plaque-adapter-gene-Synpcc7942_0336-modules
  kind: database
  reference: https://imodulondb.org/api/genes/s_elongatus/elprecise300/Synpcc7942_0336/imodulons
  locator: All57 selected-gene module rows and threshold flags inspected Same-PR public
    snapshot independently reread; actual initial fetch timestamp/hash retained, not
    a new request.
  summary: psaA2049 andpetB2331 each pass only module38 threshold. psbA1_0424 andatpA0336
    have no true flags among these57rows. Below-threshold membership is not biological
    absence or lack of a photosystem/ATPase.
  accessed_at: '2026-11-03T20:02:23.534828Z'
  support: supports
  snapshot_sha256: 2794d7d93899d2454920f1ccb4906dd7936bc98718aa79580032f4b8140e7fb5
- evidence_id: plaque-adapter-module-1
  kind: database
  reference: https://imodulondb.org/api/imodulons/s_elongatus/elprecise300/1
  locator: Native module identity/category/threshold and complete21/44 member ID lists
    inspected; activity arrays counted but condition effects not analyzed; AI summaries
    excluded Same-PR public snapshot independently reread; actual initial fetch timestamp/hash
    retained, not a new request.
  summary: PSII module1 andPhotosystems38 are dataset expression components. They
    cross-check pathway context without certifying physical complexes, direct regulation,
    universality or necessity.
  accessed_at: '2026-11-03T20:02:23.553512Z'
  support: supports
  snapshot_sha256: fe180c45de0f7400ffc349de6340de2a5f2fa1530e48f7995d8adcb60c9f0c59
- evidence_id: plaque-adapter-module-38
  kind: database
  reference: https://imodulondb.org/api/imodulons/s_elongatus/elprecise300/38
  locator: Native module identity/category/threshold and complete21/44 member ID lists
    inspected; activity arrays counted but condition effects not analyzed; AI summaries
    excluded Same-PR public snapshot independently reread; actual initial fetch timestamp/hash
    retained, not a new request.
  summary: PSII module1 andPhotosystems38 are dataset expression components. They
    cross-check pathway context without certifying physical complexes, direct regulation,
    universality or necessity.
  accessed_at: '2026-11-03T20:02:23.564078Z'
  support: supports
  snapshot_sha256: 7236e5234640b6a379fa25dc2ac44375ba96a07d69f7a020e06741bcd94c0965
- evidence_id: plaque-historical-runner
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Retained historical00:49Z failed runner and verified stdout/stderr
  summary: PermissionError accessing pyvenv.cfg; no new runner invocation or success.
    Current official-source fallback and actual dataset checks are separate.
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: plaque-original-checks
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/adversary-plaque/original-checks.json
  locator: Actual native original validate/render commands and historical40 input
    hashes
  summary: Both immutable pairs validate/render exactly and20 historical inputs each
    match. Photosynthetic target unchanged; chromatophore target stale, refreshed
    separately.
  accessed_at: '2026-11-03T20:01:36.958482Z'
  support: supports
  snapshot_sha256: 1411114c1bb2dc95e35dcc41a633b2293f7c904eeca7f430e0f7607a76251b3d
- evidence_id: plaque-native-photosynthetic_membrane-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/photosynthetic_membrane.yaml
    --verify
  locator: Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/photosynthetic_membrane-uniprot-verify-receipt.json
    and logSHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: Eight reviewed examples and2COVERED typed nodes. Native coverage checks
    do not certify every scientific claim, formation necessity or current source attribution.
  accessed_at: '2026-11-03T19:59:33.961237Z'
  support: supports
  snapshot_sha256: bf420602304023dcb926002aec236bf1af470f613e16cb50f97fb2932ccea213
- evidence_id: plaque-native-photosynthetic_membrane-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/photosynthetic_membrane.yaml
    --causal-graphs
  locator: Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/photosynthetic_membrane-uniprot-causal-receipt.json
    and logSHA256 4cdd749f721d4255905a1b805650377d703f536b2323e1a71e2fd7dd809ccd34
  summary: Eight reviewed examples and2COVERED typed nodes. Native coverage checks
    do not certify every scientific claim, formation necessity or current source attribution.
  accessed_at: '2026-11-03T19:59:34.502252Z'
  support: supports
  snapshot_sha256: e8f954793cd6561ac846c1c5d4dcc5ac6373abe677f690a9adc31dceb90365e1
- evidence_id: plaque-native-plasma_membrane_derived_chromatophore_membrane-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plasma_membrane_derived_chromatophore_membrane.yaml
    --verify
  locator: Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plasma_membrane_derived_chromatophore_membrane-uniprot-verify-receipt.json
    and logSHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: Six reviewed examples but0GENE_OR_PROTEIN nodes after current retyping;
    this is not an empty accession inventory. Native coverage checks do not certify
    every scientific claim, formation necessity or current source attribution.
  accessed_at: '2026-11-03T19:59:36.149801Z'
  support: supports
  snapshot_sha256: e8662602f234827ff747051f4800ca87db9dff2dfe92c7f78defdb540c387594
- evidence_id: plaque-native-plasma_membrane_derived_chromatophore_membrane-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plasma_membrane_derived_chromatophore_membrane.yaml
    --causal-graphs
  locator: Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plasma_membrane_derived_chromatophore_membrane-uniprot-causal-receipt.json
    and logSHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: Six reviewed examples but0GENE_OR_PROTEIN nodes after current retyping;
    this is not an empty accession inventory. Native coverage checks do not certify
    every scientific claim, formation necessity or current source attribution.
  accessed_at: '2026-11-03T19:59:36.676000Z'
  support: supports
  snapshot_sha256: 34dff06a8fcc71b45ebacd1bce269c13a3c1323d278458845d3a6a86621ecbdc
- evidence_id: micro-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Native skill/profile/config/checklist and structured-source contract
  accessed_at: '2026-11-03T20:03:48.886790Z'
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
  summary: Whole positive molecular/pathway claims trigger applicability, regardless
    of empty inventories; mere paper/model context and explicitly withheld mechanisms
    do not create a claim.
  support: context_only
- evidence_id: micro-component-policy
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: ComponentTypeEnum/StructuralComponent plus native CURATION component identity
    guidance
  accessed_at: '2026-11-03T20:03:48.886790Z'
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
  summary: Whole anatomical membrane is distinct from molecular lipid material. Reviewed-label-only
    collective bilayer is valid; structural-subpart representation is not categorically
    forbidden. Formation necessity of individual molecules is not inferred from topology.
  support: context_only
- evidence_id: micro-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Source-specific edge, class identity/component join and graph-scope contract
  accessed_at: '2026-11-03T20:03:48.886790Z'
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
  summary: Descriptive topology/class relationships are NONMECHANISTIC; lineage-specific
    protein mechanisms and optional inventories are not required on generic records.
  support: context_only
- evidence_id: micro-discussion-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Discussion305–324 and component/taxon guidance
  accessed_at: '2026-11-03T20:03:48.886790Z'
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
  summary: Rationale is append-only provenance. Source-neutral material TODOs remain
    open; exact whole-membrane GO does not supply a chemical lipid identity.
  support: context_only
- evidence_id: micro-record-plastid
  kind: record_content
  reference: data/structures/membrane_organelle/plastid.yaml
  locator: Entire current record including all history/discussions, evidence, taxon/canonical
    context, material rows and every graph node/edge
  accessed_at: '2026-11-03T20:03:48.886790Z'
  snapshot_sha256: 1be30ab06bc2fbae9294930ceaf74b20a2d43d8af60986aa9ed0e07b9645ae81
  summary: Complete independently read unchanged record; original frozen target matches.
    No record mutation.
  support: supports
- evidence_id: micro-prior-plastid
  kind: prior_review
  reference: reviews/structured/20261022T032303Z-plastid-audit/review.yaml
  locator: Original identity/source inputs/checks/evidence/read scopes/assessments/findings/actions/limits
    and deterministic Markdown
  accessed_at: '2026-11-03T20:03:48.886790Z'
  snapshot_sha256: 1c42de1dc8e88cd7fff7a11e033c2a4955c21115be4c933cbd0398e4a39e7ec9
  summary: Original needs_curation; one inherited major F1. Explicit expression-only
    adapter exclusion present. Historical accesses/checks remain historical.
  support: context_only
- evidence_id: micro-native-plastid-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid.yaml
    --verify; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T19:59:39.117227Z'
  snapshot_sha256: 7fc030d5cb2dbe017ecc5378dfd784acf54b76573f90accb7e3855eb193078c0
  summary: Actual exit0; independently counted zero protein_examples and zero typed
    GENE_OR_PROTEIN nodes. Generic verify-success does not establish complete proteome/family
    coverage, translocon identity or biological necessity.
  support: supports
- evidence_id: micro-native-plastid-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid.yaml
    --causal-graphs; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-03T19:59:39.604324Z'
  snapshot_sha256: 0bc17e0803e35c03479b927d8bd0bd8508063d275f251e76b24c1ce8c907485e
  summary: Actual exit0; independently counted zero protein_examples and zero typed
    GENE_OR_PROTEIN nodes. Generic verify-success does not establish complete proteome/family
    coverage, translocon identity or biological necessity.
  support: supports
- evidence_id: micro-record-plastid_envelope
  kind: record_content
  reference: data/structures/membrane_organelle/plastid_envelope.yaml
  locator: Entire current record including all history/discussions, evidence, taxon/canonical
    context, material rows and every graph node/edge
  accessed_at: '2026-11-03T20:03:48.886790Z'
  snapshot_sha256: 9033a6955c21d6043019061509c7ca1bf470bec884e7f4e1a5edc0080b680968
  summary: Complete independently read unchanged record; original frozen target matches.
    No record mutation.
  support: supports
- evidence_id: micro-prior-plastid_envelope
  kind: prior_review
  reference: reviews/structured/20261022T032304Z-plastid-envelope-audit/review.yaml
  locator: Original identity/source inputs/checks/evidence/read scopes/assessments/findings/actions/limits
    and deterministic Markdown
  accessed_at: '2026-11-03T20:03:48.886790Z'
  snapshot_sha256: 5fe2d0c23c716174f5967a19662fd0158f7b411d6af5d623ff086c6750999a81
  summary: Original needs_curation; one inherited major F1. Explicit expression-only
    adapter exclusion present. Historical accesses/checks remain historical.
  support: context_only
- evidence_id: micro-native-plastid_envelope-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid_envelope-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_envelope.yaml
    --verify; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid_envelope-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T19:59:40.115268Z'
  snapshot_sha256: 9c908954deff67a518868dfe0cec17cafb95c4d38bdd5a1b5d30c1ba9d180e63
  summary: Actual exit0; independently counted zero protein_examples and zero typed
    GENE_OR_PROTEIN nodes. Generic verify-success does not establish complete proteome/family
    coverage, translocon identity or biological necessity.
  support: supports
- evidence_id: micro-native-plastid_envelope-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid_envelope-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_envelope.yaml
    --causal-graphs; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid_envelope-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-03T19:59:40.588174Z'
  snapshot_sha256: 5fd2a7e43fa9bdbc922f7a5073fed252fc8b66c9a8511ff18688349f5027eef5
  summary: Actual exit0; independently counted zero protein_examples and zero typed
    GENE_OR_PROTEIN nodes. Generic verify-success does not establish complete proteome/family
    coverage, translocon identity or biological necessity.
  support: supports
- evidence_id: micro-record-plastid_inner_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/plastid_inner_membrane.yaml
  locator: Entire current record including all history/discussions, evidence, taxon/canonical
    context, material rows and every graph node/edge
  accessed_at: '2026-11-03T20:03:48.886790Z'
  snapshot_sha256: ceb12c6ee4451216ae406f17f68ea2d3730a6da302b38e8bb8fcabc532a6a4fa
  summary: Complete independently read unchanged record; original frozen target matches.
    No record mutation.
  support: supports
- evidence_id: micro-prior-plastid_inner_membrane
  kind: prior_review
  reference: reviews/structured/20261022T032305Z-plastid-inner-membrane-audit/review.yaml
  locator: Original identity/source inputs/checks/evidence/read scopes/assessments/findings/actions/limits
    and deterministic Markdown
  accessed_at: '2026-11-03T20:03:48.886790Z'
  snapshot_sha256: 7beb0aff217f2f0917394a45e58ed3d40d8f40f5671418a934aebb05b4c7af66
  summary: Original pass_with_limitations; no findings/actions. Explicit expression-only
    adapter exclusion present. Historical accesses/checks remain historical.
  support: context_only
- evidence_id: micro-native-plastid_inner_membrane-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid_inner_membrane-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_inner_membrane.yaml
    --verify; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid_inner_membrane-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T19:59:41.059982Z'
  snapshot_sha256: b3c6db6b23eefcb6085e3bf6fcc83521d6c9d32f9a08e6d7bb62ff7701538964
  summary: Actual exit0; independently counted zero protein_examples and zero typed
    GENE_OR_PROTEIN nodes. Generic verify-success does not establish complete proteome/family
    coverage, translocon identity or biological necessity.
  support: supports
- evidence_id: micro-native-plastid_inner_membrane-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid_inner_membrane-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_inner_membrane.yaml
    --causal-graphs; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid_inner_membrane-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-03T19:59:41.530301Z'
  snapshot_sha256: 59917efbe62690e34e982f63f06a4eb133de247cf417355fddbe096bae484fd8
  summary: Actual exit0; independently counted zero protein_examples and zero typed
    GENE_OR_PROTEIN nodes. Generic verify-success does not establish complete proteome/family
    coverage, translocon identity or biological necessity.
  support: supports
- evidence_id: micro-record-plastid_intermembrane_space
  kind: record_content
  reference: data/structures/membrane_organelle/plastid_intermembrane_space.yaml
  locator: Entire current record including all history/discussions, evidence, taxon/canonical
    context, material rows and every graph node/edge
  accessed_at: '2026-11-03T20:03:48.886790Z'
  snapshot_sha256: 2ef21406931fb90ec3aead7f57ee12a4376ad3d95276c7db3c2a7ab324c73c5d
  summary: Complete independently read unchanged record; original frozen target matches.
    No record mutation.
  support: supports
- evidence_id: micro-prior-plastid_intermembrane_space
  kind: prior_review
  reference: reviews/structured/20261022T032305Z-plastid-intermembrane-space-audit/review.yaml
  locator: Original identity/source inputs/checks/evidence/read scopes/assessments/findings/actions/limits
    and deterministic Markdown
  accessed_at: '2026-11-03T20:03:48.886790Z'
  snapshot_sha256: e582df2870c77ec17e21f8395ff224db0e6ddcb17a6ed2bf3341b2e7eb1570de
  summary: Original pass_with_limitations; no findings/actions. Explicit expression-only
    adapter exclusion present. Historical accesses/checks remain historical.
  support: context_only
- evidence_id: micro-native-plastid_intermembrane_space-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid_intermembrane_space-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_intermembrane_space.yaml
    --verify; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid_intermembrane_space-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T19:59:42.015179Z'
  snapshot_sha256: 1315be6cf310c3e6b0fe73392948e7058142f9248103dd292b60dcb4554121e2
  summary: Actual exit0; independently counted zero protein_examples and zero typed
    GENE_OR_PROTEIN nodes. Generic verify-success does not establish complete proteome/family
    coverage, translocon identity or biological necessity.
  support: supports
- evidence_id: micro-native-plastid_intermembrane_space-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid_intermembrane_space-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_intermembrane_space.yaml
    --causal-graphs; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid_intermembrane_space-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-03T19:59:42.492490Z'
  snapshot_sha256: 13329871691fd557e6d49868b7a31fa84ca254354feb2a4bb8c47bb9dda4d0f0
  summary: Actual exit0; independently counted zero protein_examples and zero typed
    GENE_OR_PROTEIN nodes. Generic verify-success does not establish complete proteome/family
    coverage, translocon identity or biological necessity.
  support: supports
- evidence_id: micro-record-plastid_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/plastid_membrane.yaml
  locator: Entire current record including all history/discussions, evidence, taxon/canonical
    context, material rows and every graph node/edge
  accessed_at: '2026-11-03T20:03:48.886790Z'
  snapshot_sha256: ae09183c12ecb85ac2135b3615b9a613985285039f5730126227fde982e55bef
  summary: Complete independently read unchanged record; original frozen target matches.
    No record mutation.
  support: supports
- evidence_id: micro-prior-plastid_membrane
  kind: prior_review
  reference: reviews/structured/20261022T032306Z-plastid-membrane-audit/review.yaml
  locator: Original identity/source inputs/checks/evidence/read scopes/assessments/findings/actions/limits
    and deterministic Markdown
  accessed_at: '2026-11-03T20:03:48.886790Z'
  snapshot_sha256: 876aef10c0601ebfb1e46596c4090506f360e0d84cda4dbbf822b0cd38d67ff2
  summary: Original pass_with_limitations; no findings/actions. Explicit expression-only
    adapter exclusion present. Historical accesses/checks remain historical.
  support: context_only
- evidence_id: micro-native-plastid_membrane-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid_membrane-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_membrane.yaml
    --verify; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid_membrane-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T19:59:42.977951Z'
  snapshot_sha256: f94c775a9d03e3ca3f16ff98de7913fb4fb4570eb8b06e82c81fc7d10defb964
  summary: Actual exit0; independently counted zero protein_examples and zero typed
    GENE_OR_PROTEIN nodes. Generic verify-success does not establish complete proteome/family
    coverage, translocon identity or biological necessity.
  support: supports
- evidence_id: micro-native-plastid_membrane-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid_membrane-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/plastid_membrane.yaml
    --causal-graphs; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid_membrane-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-03T19:59:43.473333Z'
  snapshot_sha256: 744297029f8a2916013672de24a5893148b32f49d68712eddbd9be586f61e602
  summary: Actual exit0; independently counted zero protein_examples and zero typed
    GENE_OR_PROTEIN nodes. Generic verify-success does not establish complete proteome/family
    coverage, translocon identity or biological necessity.
  support: supports
- evidence_id: micro-neighbor-plastid_stroma
  kind: record_content
  reference: data/structures/membrane_organelle/plastid_stroma.yaml
  locator: Complete frozen boundary neighbor, only compartment distinction assessed
  accessed_at: '2026-11-03T20:03:48.886790Z'
  snapshot_sha256: 86d19307cbe21273498f0d7d6741e61f5ebf002cf78418c34b922d9d4963503b
  summary: Stroma is matrix/ground substance distinct from IMS; outer membrane is
    cytoplasm-facing bilayer. Neighbor biological findings, applicability and history/issues
    are not terminally disposed.
  support: context_only
- evidence_id: micro-neighbor-plastid_outer_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/plastid_outer_membrane.yaml
  locator: Complete frozen boundary neighbor, only compartment distinction assessed
  accessed_at: '2026-11-03T20:03:48.886790Z'
  snapshot_sha256: 59bd8548931d27f711233f542b5f927c0e7b0a68dd611eabb4777ee08003deaa
  summary: Stroma is matrix/ground substance distinct from IMS; outer membrane is
    cytoplasm-facing bilayer. Neighbor biological findings, applicability and history/issues
    are not terminally disposed.
  support: context_only
- evidence_id: micro-original-pairs
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/adversary-microtubule/original-checks.json
  locator: Five actual native validates and five render --content exact comparisons
  accessed_at: '2026-11-03T20:00:08.449616Z'
  snapshot_sha256: 7e6778972a0336e701bde9014f90a4ca25ea5b307cf6f2d841f40e6cfd992949
  summary: All five original YAMLs validate and Markdown render exactly.
  support: supports
- evidence_id: micro-original-inputs
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/adversary-microtubule/original-frozen-inputs.json
  locator: All75 historical frozen input entries at original retained source
  accessed_at: '2026-11-03T20:03:48.886790Z'
  snapshot_sha256: 1fbdfbbbc9c54b64cc2be5d8dcd1787865e79fb7493ba53ee67879ee70c0d471
  summary: All historical hashes verify; own five current target hashes unchanged.
    Historical hashing does not constitute new scientific judgments of unfrozen neighbors.
  support: supports
- evidence_id: micro-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009536,GO:0009526,GO:0043231,GO:0005737,GO:0042170,GO:0009532,GO:0031967,GO:0009527,GO:0009528,GO:0009529,GO:0016020,GO:0055035,GO:0033113,GO:0160211
  locator: 'All14 exact requested entries: active id/name/definition/synonyms and
    typed children; unrelated broad-cytoplasm children not treated as evidence'
  accessed_at: '2026-11-03T20:00:11.084499Z'
  snapshot_sha256: 99fdd058846ea33d210fbd051a4200c72e782f088a219129708fe8675dac76d9
  summary: Exact whole/envelope/inner/IMS/generic identities verified. GO0043231 is_a
    plastid and cytoplasm part_of plastid typed children; plastid stroma/envelope/membrane
    parts explicit. Envelope includes IMS/generic membrane; GO0042170 explicitly has
    outer,inner,thylakoid,cyanelle,apicoplast is_a children despite envelope-focused
    definition. No is_a/parthood conflation. Whole membrane GO remains anatomical,
    not chemical lipid.
  support: supports
- evidence_id: micro-go0042170-isa
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0042170/ancestors?relations=is_a
  locator: Complete exact-term ancestors request relations=is_a
  accessed_at: '2026-11-03T20:01:44.454142Z'
  snapshot_sha256: 78421c8762cdc337a932eacc0725479566a99847cb661a763ae43a5251b2fb53
  summary: GO0042170 has GO0016020 membrane ancestry; direct typed children separately
    support exact membrane classes. No direct parthood inferred from transitive is_a.
  support: supports
- evidence_id: micro-SL0209
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0209.json
  locator: Full native location identity/definition/synonyms/GO mapping and immediate/nested
    hierarchy; statistics not biological census
  accessed_at: '2026-11-03T20:00:11.084782Z'
  snapshot_sha256: 857c3318daeb72c42cf4c273a21fc9e99243ad68301147a01a796a906c371b58
  summary: Exact plastidGO9536 mapping and photosynthetic/nonphotosynthetic context;
    no universal photosynthetic function or membrane count.
  support: supports
- evidence_id: micro-SL0210
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0210.json
  locator: Full native location identity/definition/synonyms/GO mapping and immediate/nested
    hierarchy; statistics not biological census
  accessed_at: '2026-11-03T20:00:11.084869Z'
  snapshot_sha256: 0716e583e23a85c025ba7164c6efa6647276d47f68ede54d0fac20ac968b6664
  summary: Exact envelopeGO9526/synonym and inner+outer+IMS definition; plastid parthood.
  support: supports
- evidence_id: micro-SL0211
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0211.json
  locator: Full native location identity/definition/synonyms/GO mapping and immediate/nested
    hierarchy; statistics not biological census
  accessed_at: '2026-11-03T20:00:11.084944Z'
  snapshot_sha256: a1d5aada6f9ece1571ec375df8c0ab1e2a3dbab0398a46de53ab9957199147d8
  summary: Exact innerGO9528/three synonyms; stroma/IMS separation, generic-membrane
    hierarchy; nestedSL0213 includes outer/inner/thylakoid fallback scope.
  support: supports
- evidence_id: micro-SL0212
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0212.json
  locator: Full native location identity/definition/synonyms/GO mapping and immediate/nested
    hierarchy; statistics not biological census
  accessed_at: '2026-11-03T20:00:11.085006Z'
  snapshot_sha256: e45d81d88e3d6f167d665d42f1721da6eb6a2c6e69821dee5c9d2740afb514aa
  summary: Exact IMSGO9529/synonym, envelope parthood and between-inner/outer definition;
    not stroma or bilayer.
  support: supports
- evidence_id: micro-SL0214
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0214.json
  locator: Full native location identity/definition/synonyms/GO mapping and immediate/nested
    hierarchy; statistics not biological census
  accessed_at: '2026-11-03T20:00:11.085055Z'
  snapshot_sha256: c849d1946fe23f77351fae5e9e4bcf0515e14578d37497cb0d320bc7ffb0dd93
  summary: Exact outerGO9527/three synonyms and cytoplasm-facing definition; generic-membrane
    hierarchy.
  support: supports
- evidence_id: micro-tax2759
  kind: database
  reference: https://rest.uniprot.org/taxonomy/2759.json
  locator: Native identity/rank/active/parent/lineage; species strain list not experiment
    provenance
  accessed_at: '2026-11-03T20:00:11.841045Z'
  snapshot_sha256: af5ba762219fdecb11d214126bb8184c0eb28fc6474d14777c4aaa7f7dd89369
  summary: Eukaryota active domain.
  support: supports
- evidence_id: micro-tax33090
  kind: database
  reference: https://rest.uniprot.org/taxonomy/33090.json
  locator: Native identity/rank/active/parent/lineage; species strain list not experiment
    provenance
  accessed_at: '2026-11-03T20:00:11.841159Z'
  snapshot_sha256: b982424d27b194ce13071e5e2b9ab27613390e37b23e735be0aad29a9156047e
  summary: Viridiplantae active kingdom within Eukaryota.
  support: supports
- evidence_id: micro-tax3055
  kind: database
  reference: https://rest.uniprot.org/taxonomy/3055.json
  locator: Native identity/rank/active/parent/lineage; species strain list not experiment
    provenance
  accessed_at: '2026-11-03T20:00:12.217034Z'
  snapshot_sha256: 31e68163918c110c000e261d4edc5ae389b11e9992f43540ba3b89a9471ce850
  summary: Chlamydomonas reinhardtii active species within green-algal lineage. Listed
    strain aliases do not identify which experimental strain Jin used.
  support: supports
- evidence_id: micro-catalogue
  kind: search
  reference: https://imodulondb.org/api/datasets
  locator: Full unpaginated official catalogue,20 organisms/28 organism-dataset pairs
  accessed_at: '2026-11-03T20:00:12.220224Z'
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  summary: No Chlamydomonas/reinhardtii, Viridiplantae/green-algal host entry. Three
    TOC–TIC-bearing targets require coverage assessment; no matching host means no
    downstream module/gene query. Whole/generic physical scope remains excluded independently
    of catalogue noncoverage.
  support: supports
  search_scope: Official iModulonDB /api/datasets at 2026-11-03T20:00:12.220224Z;
    HTTP200 complete unpaginated20 organism rows/28 organism-dataset pairs, inspect
    id/name/description/datasets for Chlamydomonas,reinhardtii,green algae and Viridiplantae.
    Coverage limited to returned catalogue/date; no universal absence or unrelated
    cyanobacterial proxy.
- evidence_id: micro-historical-runner
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical command /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb datasets; actual00:49Z exit1 PermissionError reading pyvenv.cfg
  accessed_at: '2026-11-03T00:49:00.863225Z'
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  summary: Historical unavailable optional runner, not fresh invocation. Fresh official
    catalogue fallback completed; no matched-host downstream query.
  support: context_only
- evidence_id: micro-keeling2010-meta
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1098%2Frstb.2009.0103%22&format=json&resultType=core&pageSize=25
  locator: Exact DOI core unique MED record identity/authors/publication types and
    complete abstract
  accessed_at: '2026-11-03T20:00:12.281228Z'
  snapshot_sha256: 6c4c2d100f04d49ce5c123fd3f3296461de3cad0657279b56756d6bbe72b65a5
  summary: Keeling2010 PMID20124341/PMC2817223 is secondary evolutionary review. Plastid
    diversity/loss context is not current universal phylogenetic consensus or numerical
    census.
  support: context_only
- evidence_id: micro-terashima2011-meta
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1007%2Fs00294-011-0339-1%22&format=json&resultType=core&pageSize=25
  locator: Exact DOI core unique MED record identity/authors/publication types and
    complete abstract
  accessed_at: '2026-11-03T20:00:12.371119Z'
  snapshot_sha256: a0d671dcbfe1f2bb63903f3fbdfd8bed3c7002db90a9f949a4dc8e8e9f18fb12
  summary: Terashima/Specht/Hippler2011 PMID21533645 is secondary review. Supports
    C.reinhardtii chloroplast model context; compiled996 proteins are not all independently
    experimentally proven membrane residents or mandatory inventory.
  support: context_only
- evidence_id: micro-jin2022-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.cell.2022.10.030%22&format=json&resultType=core&pageSize=25
  locator: Exact DOI unique MED36413996 identity/authors, complete primary abstract,
    keywordList/meshHeadingList/fullTextUrlList; no body
  accessed_at: '2026-11-03T20:00:12.954495Z'
  snapshot_sha256: 6acdc39ef406f584db55a65552de51608adb06f87a950c923ed7a863bb58b76e
  summary: Jin2022 reports Chlamydomonas TOC–TIC cryoEM assembly spanning two envelope
    membranes and IMS scaffold; indexed keyword explicitly names C.reinhardtii. This
    supports species-bounded example and inner/IMS placement, not exact strain/Methods/model
    validation, per-protein necessity or every plastid lineage.
  support: supports
- evidence_id: micro-jin2022-crossref
  kind: database
  reference: https://api.crossref.org/works/10.1016/j.cell.2022.10.030
  locator: Exact DOI title/authors/date/resource/link metadata; publisher route discovery
    only
  accessed_at: '2026-11-03T20:00:45.534265Z'
  snapshot_sha256: c2b1b871dd0053f897196e2513abe10910ae5f13c1567435645202d05ead8ba7
  summary: Exact primary title/DOI and PII S0092867422013769 verified. Crossref metadata
    is not full article access.
  support: context_only
- evidence_id: micro-keeling2010-retained
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2817223/
  locator: Retained genuine HTML fetched10:10:38.582642Z; independently reread complete
    sections s1,s3,s6,s9 with embedded Figure1–3 captions; no pixels/other sections/underlying
    experiments
  accessed_at: '2026-11-03T10:10:38.582642Z'
  snapshot_sha256: 7c0eea300c6d6a694668d62cda30305d8c92b42f72192c66518f1251414c9f95
  summary: Secondary review supports primary double boundaries, secondary3/4 membranes
    and retained nonphotosynthetic plastids. Outdated universal mitochondrial-loss/old
    chromalveolate hypotheses are not adopted; no new current census.
  support: context_only
- evidence_id: micro-terashima2011-retained
  kind: authority
  reference: https://link.springer.com/content/pdf/10.1007/s00294-011-0339-1.pdf
  locator: Retained genuine PDF fetched10:10:38.518294Z; fresh pdftotext pages151–152,
    complete title/abstract/Introduction and initial proteome-compilation discussion;
    no later pages/pixels/supplements
  accessed_at: '2026-11-03T10:10:38.518294Z'
  snapshot_sha256: e42edb346d375e4e083e2eb79c6d9eff9fc217513e1ae9ecf808acb143129c6b
  summary: Secondary review supports chloroplast model/proteome research context and
    explains enriched-fraction contamination and compilation. No generic whole/membrane
    record claims996 residents, a specific pathway or membrane-only proteome; broad
    canonical model wording remains supported.
  support: context_only
- evidence_id: micro-access-keeling2010-jats
  kind: validation
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2817223.1/PMC2817223.1.xml
  locator: Actual route response content inspected; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/adversary-microtubule/keeling2010-jats.receipt.json
  accessed_at: '2026-11-03T20:00:12.999933Z'
  snapshot_sha256: 0759254eb6aa7e80607a5adfeb120cc90f777373bacd09d8295bd6bfe6e0ba41
  summary: S3 candidate404; no body.
  support: context_only
- evidence_id: micro-access-keeling2010-canonical
  kind: validation
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2817223/
  locator: Actual route response content inspected; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/adversary-microtubule/keeling2010-canonical.receipt.json
  accessed_at: '2026-11-03T20:00:45.533896Z'
  snapshot_sha256: f2e5f75e6deefae4792232dad3b107b658ef69a61a7dbfdacf321d3d5252fb0f
  summary: HTTP200 recaptcha, not article.
  support: context_only
- evidence_id: micro-access-keeling2010-legacy
  kind: validation
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2817223/
  locator: Actual route response content inspected; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/adversary-microtubule/keeling2010-legacy.receipt.json
  accessed_at: '2026-11-03T20:00:45.534152Z'
  snapshot_sha256: 450ecb3a90388d76b4003c4daed9f4b4d0d27f8c27ecdc3be1dfa93b63e721a5
  summary: HTTP200 recaptcha, not article; earlier genuine retained body separately
    read.
  support: context_only
- evidence_id: micro-access-terashima2011-pdf
  kind: validation
  reference: https://link.springer.com/content/pdf/10.1007/s00294-011-0339-1.pdf
  locator: Actual route response content inspected; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/adversary-microtubule/terashima2011-pdf.receipt.json
  accessed_at: '2026-11-03T20:00:13.140767Z'
  snapshot_sha256: 32ed63159c77e21ee19ca1b9aa3213ccf0218eb59539560b132a8e68ef0e18ea
  summary: HTTP2003038-byte HTML challenge, not PDF; genuine earlier retained PDF
    separately read.
  support: context_only
- evidence_id: micro-access-terashima2011-crossref
  kind: validation
  reference: https://api.crossref.org/works/10.1007/s00294-011-0339-1
  locator: Actual route response content inspected; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/adversary-microtubule/terashima2011-crossref.receipt.json
  accessed_at: '2026-11-03T20:00:45.534333Z'
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
  summary: HTTP429 zero-byte response; metadata elsewhere separately verified.
  support: context_only
- evidence_id: micro-access-jin2022-publisher
  kind: validation
  reference: https://api.elsevier.com/content/article/PII:S0092867422013769?httpAccept=text/xml
  locator: Actual route response content inspected; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/adversary-microtubule/jin2022-publisher.receipt.json
  accessed_at: '2026-11-03T20:01:44.453877Z'
  snapshot_sha256: f89b1fa484e5f31c9142821a7352ba0906d288e01c84518b7d96822df5b6e2cb
  summary: HTTP2001941-byte XML contains core metadata only, despite full-text-retrieval-response
    name; no article body.
  support: context_only
- evidence_id: micro-access-jin2022-pdf
  kind: validation
  reference: https://www.cell.com/cell/pdf/S0092-8674(22)01376-9.pdf
  locator: Actual route response content inspected; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/adversary-microtubule/jin2022-pdf.receipt.json
  accessed_at: '2026-11-03T20:01:44.454214Z'
  snapshot_sha256: 4b240ef044c03a30c29223b4cc5bdff71c68c10a914ed7544df83aba5a84e48d
  summary: HTTP403 publisher challenge; no body/pixels.
  support: context_only
- evidence_id: check-qc
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/qc.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T20:04:57.140538Z'
  support: supports
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  snapshot_sha256: 8a911635cfdd35af331f5b5ca5a84a34414ed5fe48d8ace2372c90fd82c0978a
- evidence_id: check-labels
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/labels.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T20:00:08.319126Z'
  support: supports
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  snapshot_sha256: 6cdfb05df9a27194f05a5fd7f851783f817ac1523ca0bbfa54fe0e0d18775905
- evidence_id: check-trait-links
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/trait-links.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T19:59:38.060518Z'
  support: supports
  summary: Native TraitMech link check passed.
  snapshot_sha256: 8b336cdefbbd3daf6da8787990efdbe346c95e2c8361d50b7eb68a18f2d5a44a
- evidence_id: check-vendored
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/vendored.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T19:59:35.122795Z'
  support: supports
  summary: Pinned governed files match; native vendored check passed.
  snapshot_sha256: b1f169d103aaefa930745468bcca171e5867b9cc49e4e74311e458097e3252a6
- evidence_id: check-curies
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/curies.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T19:59:37.979968Z'
  support: supports
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  snapshot_sha256: bc12b1285f5747707643f7a98e03dbb3a6c88fb062ad49f99db9cb42ececf3d2
- evidence_id: focused
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/focused-results.json
  locator: All twenty actual target schema/strict command outputs
  accessed_at: '2026-11-03T20:10:29Z'
  support: supports
  summary: Ten schema and ten strict commands returned exit zero.
  snapshot_sha256: b7bce8b5444893dbca8cc5d03aaa7239278ebff836f7c55ee87cda84731e615e
- evidence_id: supplemental-pmid
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/pmid-chunks-receipt.json
  locator: Complete native-report PMID set checked with unchanged resolver in batches
    of at most fifty
  accessed_at: '2026-11-03T20:01:22.063255Z'
  support: supports
  summary: 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers
    remain unverified.
  snapshot_sha256: d8c551b24870ce10b000faba163b629f194fd211285f9294ea40bbf577581882
- evidence_id: historical-adapter-runner-availability
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical runner invocation receipt, exact SHA256 reverified during PR2375
    synthesis
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  summary: Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS
    PermissionError reading the configured runner pyvenv.cfg. This is retained historical
    availability evidence, not a fresh attempt or a scientific validation failure.
    Native policy permits inspected source-catalogue fallback.
- evidence_id: root-native-phagolysosome_vesicle_lumen-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/phagolysosome_vesicle_lumen-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T19:59:31.812655Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-phagolysosome_vesicle_lumen-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/phagolysosome_vesicle_lumen-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T19:59:32.303614Z'
  support: context_only
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-photosynthetic_membrane-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/photosynthetic_membrane-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T19:59:33.961237Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 8 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-photosynthetic_membrane-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/photosynthetic_membrane-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T19:59:34.502252Z'
  support: context_only
  snapshot_sha256: 4cdd749f721d4255905a1b805650377d703f536b2323e1a71e2fd7dd809ccd34
  summary: 8 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-plasma_membrane_derived_chromatophore_membrane-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plasma_membrane_derived_chromatophore_membrane-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T19:59:36.149801Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 6 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-plasma_membrane_derived_chromatophore_membrane-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plasma_membrane_derived_chromatophore_membrane-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T19:59:36.676000Z'
  support: context_only
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: 6 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-plasma_membrane_derived_thylakoid_lumen-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plasma_membrane_derived_thylakoid_lumen-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T19:59:37.169586Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-plasma_membrane_derived_thylakoid_lumen-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plasma_membrane_derived_thylakoid_lumen-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T19:59:37.666291Z'
  support: context_only
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-plasma_membrane_derived_thylakoid_membrane-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plasma_membrane_derived_thylakoid_membrane-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T19:59:38.148654Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-plasma_membrane_derived_thylakoid_membrane-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plasma_membrane_derived_thylakoid_membrane-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T19:59:38.623974Z'
  support: context_only
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-plastid-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T19:59:39.117227Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-plastid-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T19:59:39.604324Z'
  support: context_only
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-plastid_envelope-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid_envelope-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T19:59:40.115268Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-plastid_envelope-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid_envelope-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T19:59:40.588174Z'
  support: context_only
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-plastid_inner_membrane-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid_inner_membrane-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T19:59:41.059982Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-plastid_inner_membrane-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid_inner_membrane-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T19:59:41.530301Z'
  support: context_only
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-plastid_intermembrane_space-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid_intermembrane_space-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T19:59:42.015179Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-plastid_intermembrane_space-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid_intermembrane_space-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T19:59:42.492490Z'
  support: context_only
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-plastid_membrane-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid_membrane-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T19:59:42.977951Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-plastid_membrane-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2375/plastid_membrane-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T19:59:43.473333Z'
  support: context_only
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
assessments:
- assessment_id: septin-phagolysosome_vesicle_lumen-schema
  area: schema
  topic: Original native validation/render and frozen input
  outcome: supported
  summary: Actual original native validation/render pass with exact Markdown. Historical
    frozen target hash verified. Current target is byte-identical to its original
    frozen input.
  target_ids:
  - GO:0106174
  evidence_ids:
  - septin-record-phagolysosome_vesicle_lumen
  - septin-original-validation-phagolysosome_vesicle_lumen
- assessment_id: septin-phagolysosome_vesicle_lumen-identity
  area: identity
  topic: Exact identity, synonym and structural boundary
  outcome: supported
  summary: GO0106174 volume, GO0097013 parent and GO0032010 parthood remain exact.
    Ordinary phagolysosome-lumen wording is compatible even if not a current GO exact-synonym
    string; SL0342 supplies broader lumen context only.
  target_ids:
  - GO:0106174
  evidence_ids:
  - septin-record-phagolysosome_vesicle_lumen
  - septin-go
  - septin-gotthardt2002-unige-pdf
  - septin-PMID12388753
  - septin-SL0342
- assessment_id: septin-phagolysosome_vesicle_lumen-definition
  area: scope
  topic: Definition source and expanded biological scope
  outcome: concern
  summary: 'Inherited major F1 persists: exact ontology volume clause is followed
    by cross-taxon enzyme/ROS/microbial-killing program not supplied by GO or established
    in full by the Ax2 source. This does not refute any individual mechanism or require
    replacing the correct identity.'
  target_ids:
  - GO:0106174
  evidence_ids:
  - septin-record-phagolysosome_vesicle_lumen
  - septin-go
  - septin-gotthardt2002-unige-pdf
  - septin-PMID12388753
- assessment_id: septin-phagolysosome_vesicle_lumen-taxon
  area: scope
  topic: Actual source organism, strain and occurrence
  outcome: supported
  summary: D. discoideum/Ax2 is the actual primary host. COMMON is qualitative model-system
    occurrence and does not certify all strains/taxa/stages. Added Entamoeba/ciliate
    generalization is addressed by F1.
  target_ids:
  - GO:0106174
  evidence_ids:
  - septin-record-phagolysosome_vesicle_lumen
  - septin-go
  - septin-gotthardt2002-unige-pdf
  - septin-PMID12388753
  - septin-tax44689
- assessment_id: septin-phagolysosome_vesicle_lumen-material
  area: grounding
  topic: Constituent/material scope
  outcome: supported
  summary: No component inventory is asserted for this lumen; enclosing membrane remains
    a separate STRUCTURE. Variable luminal cargo or proton-gradient function is not
    a mandatory stable protein inventory.
  target_ids:
  - GO:0106174
  evidence_ids:
  - septin-record-phagolysosome_vesicle_lumen
  - septin-go
  - septin-gotthardt2002-unige-pdf
  - septin-PMID12388753
  - septin-curation-policy
  - septin-schema-policy
- assessment_id: septin-phagolysosome_vesicle_lumen-experimental
  area: evidence
  topic: Direct experimental result versus context
  outcome: concern
  summary: 'Inherited minor F3 persists: source directly dissects trafficking/composition,
    while acidification is discussed from prior work. Current canonical/function notes
    blur that distinction; retain qualitative maturation while qualifying assay attribution.'
  target_ids:
  - GO:0106174
  evidence_ids:
  - septin-record-phagolysosome_vesicle_lumen
  - septin-go
  - septin-gotthardt2002-unige-pdf
  - septin-PMID12388753
- assessment_id: septin-phagolysosome_vesicle_lumen-function
  area: evidence
  topic: Biological function and necessity
  outcome: concern
  summary: GO0090383 acidification association is biologically coherent but does not
    make the2002 source a direct pH experiment. Full cross-taxon digestive-program
    support remains bounded by F1/F3.
  target_ids:
  - GO:0106174
  evidence_ids:
  - septin-record-phagolysosome_vesicle_lumen
  - septin-go
  - septin-gotthardt2002-unige-pdf
  - septin-PMID12388753
- assessment_id: septin-phagolysosome_vesicle_lumen-graph
  area: graph
  topic: Graph scope and complete edge inventory
  outcome: concern
  summary: 'Inherited minor F2 persists: MECHANISTIC/assembly-functional-mechanism
    wording exceeds two actual descriptive edges, lumen parthood and whole-volume
    association with acidification. No explanatory proton transport transition is
    represented.'
  target_ids:
  - GO:0106174
  evidence_ids:
  - septin-record-phagolysosome_vesicle_lumen
  - septin-go
  - septin-gotthardt2002-unige-pdf
  - septin-PMID12388753
  - septin-graph-policy
  - septin-schema-policy
  - septin-original-phagolysosome_vesicle_lumen
- assessment_id: septin-phagolysosome_vesicle_lumen-native
  area: provenance
  topic: Actual native coverage versus molecular completeness
  outcome: supported
  summary: Actual two native commands pass. Independent count is0 examples,0 typed
    molecular nodes,0 UniProtKB graph xrefs. This empty inventory does not erase the
    positive narrative pathway scope.
  target_ids:
  - GO:0106174
  evidence_ids:
  - septin-record-phagolysosome_vesicle_lumen
  - septin-native-phagolysosome_vesicle_lumen-verify
  - septin-native-phagolysosome_vesicle_lumen-causal
  - septin-protein-policy
- assessment_id: septin-phagolysosome_vesicle_lumen-adapter
  area: scope
  topic: Whole-record structured-source applicability
  outcome: supported
  summary: Positive acidification and digestive molecular narrative trigger policy.
    Fresh complete catalogue lacks the actual Dictyostelium/Ax2 and other named host
    groups; use scoped primary/authority fallback, not prey or another host. Historical00:49Z
    unavailable runner is separate from these completed fresh HTTP/source checks.
  target_ids:
  - GO:0106174
  evidence_ids:
  - septin-record-phagolysosome_vesicle_lumen
  - septin-go
  - septin-gotthardt2002-unige-pdf
  - septin-PMID12388753
  - septin-review-policy
  - septin-catalogue
  - septin-adapter-runner-historical
- assessment_id: septin-phagolysosome_vesicle_lumen-history
  area: provenance
  topic: Append-only provenance and boundary contexts
  outcome: supported
  summary: 'PROPOSED state and dated history/discussion remain unchanged. Historical
    resolved topology/material discussions are not rewritten as current inventories.
    Bounded frozen neighbor anatomy does not dispose another record or grouped issue. '
  target_ids:
  - GO:0106174
  evidence_ids:
  - septin-record-phagolysosome_vesicle_lumen
  - septin-curation-policy
  - septin-original-phagolysosome_vesicle_lumen
- assessment_id: septin-phagolysosome_vesicle_lumen-formation
  area: completeness
  topic: Unresolved formation/assembly detail
  outcome: unknown
  summary: Source anatomy and measured trafficking/localization do not establish exhaustive
    formation machinery, invariant molecular composition or individual necessary subunits
    across taxa. Optional protein examples are not mandatory solely because sources
    identify proteins.
  target_ids:
  - GO:0106174
  evidence_ids:
  - septin-record-phagolysosome_vesicle_lumen
  - septin-go
  - septin-gotthardt2002-unige-pdf
  - septin-PMID12388753
  - septin-protein-policy
- assessment_id: septin-phagolysosome_vesicle_lumen-optional
  area: scope
  topic: Absent image/measurement/protein domains
  outcome: not_applicable
  summary: No maintained image/license claim, individual protein accession, quantitative
    measurement, associated-trait mapping or verbatim snippet occurs in these three
    records. Source text captions were read without image pixels/raw datasets/supplements.
    Those unseen domains are not certified.
  target_ids:
  - GO:0106174
  evidence_ids:
  - septin-record-phagolysosome_vesicle_lumen
  - septin-go
  - septin-gotthardt2002-unige-pdf
  - septin-PMID12388753
- assessment_id: septin-phagolysosome_vesicle_lumen-verdict
  area: completeness
  topic: Current scientific verdict and exact lineage
  outcome: concern
  summary: 'needs_curation: inherited F1 major definition scope plus F2/F3 minor graph/acidification
    attribution remain open. No new scientific finding; maintained-record fixes stay
    outside this review-only PR. Original exact keys, severity normalization and predecessor
    references are preserved.'
  target_ids:
  - GO:0106174
  evidence_ids:
  - septin-record-phagolysosome_vesicle_lumen
  - septin-go
  - septin-gotthardt2002-unige-pdf
  - septin-PMID12388753
  - septin-original-phagolysosome_vesicle_lumen
- assessment_id: septin-plasma_membrane_derived_thylakoid_lumen-schema
  area: schema
  topic: Original native validation/render and frozen input
  outcome: supported
  summary: Actual original native validation/render pass with exact Markdown. Historical
    frozen target hash verified. Current target is byte-identical to its original
    frozen input.
  target_ids:
  - GO:0031979
  evidence_ids:
  - septin-record-plasma_membrane_derived_thylakoid_lumen
  - septin-original-validation-plasma_membrane_derived_thylakoid_lumen
- assessment_id: septin-plasma_membrane_derived_thylakoid_lumen-identity
  area: identity
  topic: Exact identity, synonym and structural boundary
  outcome: supported
  summary: GO0031979 and SL0044 identify the enclosed cellular thylakoid lumen with
    GO0030075 parthood. Boundary membrane is a separate structure. GO non-organelle
    commentary and qualified lack of obligatory continuity are retained.
  target_ids:
  - GO:0031979
  evidence_ids:
  - septin-record-plasma_membrane_derived_thylakoid_lumen
  - septin-go
  - septin-huokko2021-jats
  - septin-casella2017-jats
  - septin-perez2024-delivered
  - septin-SL0044
- assessment_id: septin-plasma_membrane_derived_thylakoid_lumen-definition
  area: scope
  topic: Definition source and expanded biological scope
  outcome: supported
  summary: Definition remains topological rather than a fixed cross-taxon protein
    inventory. Plasma-membrane-derived terminology does not require a continuing physical
    bridge; actual7942 cryoET reports no apparent direct connection.
  target_ids:
  - GO:0031979
  evidence_ids:
  - septin-record-plasma_membrane_derived_thylakoid_lumen
  - septin-go
  - septin-huokko2021-jats
  - septin-casella2017-jats
  - septin-perez2024-delivered
- assessment_id: septin-plasma_membrane_derived_thylakoid_lumen-taxon
  area: scope
  topic: Actual source organism, strain and occurrence
  outcome: concern
  summary: 'Inherited major F1 persists: current canonical example attributes Huokko2021
    to Synechocystis6803, but Methods/Results specify Synechococcus elongatus7942.
    The explicit Huokko evidence note also repeats the incorrect host. PCC6803 presence
    itself is not refuted. Cyanobacteriota COMMON with Gloeobacter exception is qualitative,
    not a census.'
  target_ids:
  - GO:0031979
  evidence_ids:
  - septin-record-plasma_membrane_derived_thylakoid_lumen
  - septin-go
  - septin-huokko2021-jats
  - septin-casella2017-jats
  - septin-perez2024-delivered
  - septin-tax1117
  - septin-tax1148
  - septin-tax1140
- assessment_id: septin-plasma_membrane_derived_thylakoid_lumen-material
  area: grounding
  topic: Constituent/material scope
  outcome: supported
  summary: No component inventory is asserted for this lumen; enclosing membrane remains
    a separate STRUCTURE. Variable luminal cargo or proton-gradient function is not
    a mandatory stable protein inventory.
  target_ids:
  - GO:0031979
  evidence_ids:
  - septin-record-plasma_membrane_derived_thylakoid_lumen
  - septin-go
  - septin-huokko2021-jats
  - septin-casella2017-jats
  - septin-perez2024-delivered
  - septin-curation-policy
  - septin-schema-policy
- assessment_id: septin-plasma_membrane_derived_thylakoid_lumen-experimental
  area: evidence
  topic: Direct experimental result versus context
  outcome: supported
  summary: Casella uses native7942 thylakoid preparations and functional fluorescent
    tags; AFM b6f shape assignment is tentative and distinct from tagged localization.
    Huokko uses HL-to-LL recovery and cryoET in7942; no direct membrane continuity
    is assumed. Perez is secondary synthesis, not a new primary assay.
  target_ids:
  - GO:0031979
  evidence_ids:
  - septin-record-plasma_membrane_derived_thylakoid_lumen
  - septin-go
  - septin-huokko2021-jats
  - septin-casella2017-jats
  - septin-perez2024-delivered
- assessment_id: septin-plasma_membrane_derived_thylakoid_lumen-function
  area: evidence
  topic: Biological function and necessity
  outcome: supported
  summary: Positive trans-thylakoid proton-gradient narrative is supported by the
    inspected secondary review; the lumen graph intentionally remains descriptive
    anatomy rather than a complete proton-transport mechanism.
  target_ids:
  - GO:0031979
  evidence_ids:
  - septin-record-plasma_membrane_derived_thylakoid_lumen
  - septin-go
  - septin-huokko2021-jats
  - septin-casella2017-jats
  - septin-perez2024-delivered
- assessment_id: septin-plasma_membrane_derived_thylakoid_lumen-graph
  area: graph
  topic: Graph scope and complete edge inventory
  outcome: supported
  summary: 'NONMECHANISTIC graph has2 anatomical edges: lumen parthood and membrane
    boundary. It does not promise an omitted molecular causal sequence.'
  target_ids:
  - GO:0031979
  evidence_ids:
  - septin-record-plasma_membrane_derived_thylakoid_lumen
  - septin-go
  - septin-huokko2021-jats
  - septin-casella2017-jats
  - septin-perez2024-delivered
  - septin-graph-policy
  - septin-schema-policy
  - septin-original-plasma_membrane_derived_thylakoid_lumen
- assessment_id: septin-plasma_membrane_derived_thylakoid_lumen-native
  area: provenance
  topic: Actual native coverage versus molecular completeness
  outcome: supported
  summary: Actual two native commands pass. Independent count is0 examples,0 typed
    molecular nodes,0 UniProtKB graph xrefs. This empty inventory does not erase the
    positive narrative pathway scope.
  target_ids:
  - GO:0031979
  evidence_ids:
  - septin-record-plasma_membrane_derived_thylakoid_lumen
  - septin-native-plasma_membrane_derived_thylakoid_lumen-verify
  - septin-native-plasma_membrane_derived_thylakoid_lumen-causal
  - septin-protein-policy
- assessment_id: septin-plasma_membrane_derived_thylakoid_lumen-adapter
  area: scope
  topic: Whole-record structured-source applicability
  outcome: supported
  summary: Positive photochemistry/proton-gradient and complex/pathway assertions
    trigger policy. Fresh catalogue and bounded s_elongatus/elprecise300 gene/module
    checks cover actual cited7942 experiments and broad cyanobacterial context. They
    do not substitute for unmatched6803 or repair its source attribution. psaA/petB
    pass module38 thresholds; psbA1/atpA all-false flags do not establish biological
    absence. Historical00:49Z unavailable runner is separate from these completed
    fresh HTTP/source checks.
  target_ids:
  - GO:0031979
  evidence_ids:
  - septin-record-plasma_membrane_derived_thylakoid_lumen
  - septin-go
  - septin-huokko2021-jats
  - septin-casella2017-jats
  - septin-perez2024-delivered
  - septin-review-policy
  - septin-catalogue
  - septin-adapter-runner-historical
  - septin-adapter-gene-Synpcc7942_2049-modules
  - septin-adapter-gene-Synpcc7942_0424-modules
  - septin-adapter-gene-Synpcc7942_2331-modules
  - septin-adapter-gene-Synpcc7942_0336-modules
  - septin-adapter-module-38
- assessment_id: septin-plasma_membrane_derived_thylakoid_lumen-history
  area: provenance
  topic: Append-only provenance and boundary contexts
  outcome: supported
  summary: 'PROPOSED state and dated history/discussion remain unchanged. Historical
    resolved topology/material discussions are not rewritten as current inventories.
    Bounded frozen neighbor anatomy does not dispose another record or grouped issue. '
  target_ids:
  - GO:0031979
  evidence_ids:
  - septin-record-plasma_membrane_derived_thylakoid_lumen
  - septin-curation-policy
  - septin-original-plasma_membrane_derived_thylakoid_lumen
- assessment_id: septin-plasma_membrane_derived_thylakoid_lumen-formation
  area: completeness
  topic: Unresolved formation/assembly detail
  outcome: unknown
  summary: Source anatomy, measured trafficking/localization and secondary photochemical
    synthesis do not establish exhaustive formation machinery, invariant molecular
    composition or individual necessary subunits across taxa. Optional protein examples
    are not mandatory solely because sources identify proteins.
  target_ids:
  - GO:0031979
  evidence_ids:
  - septin-record-plasma_membrane_derived_thylakoid_lumen
  - septin-go
  - septin-huokko2021-jats
  - septin-casella2017-jats
  - septin-perez2024-delivered
  - septin-protein-policy
- assessment_id: septin-plasma_membrane_derived_thylakoid_lumen-optional
  area: scope
  topic: Absent image/measurement/protein domains
  outcome: not_applicable
  summary: No maintained image/license claim, individual protein accession, quantitative
    measurement, associated-trait mapping or verbatim snippet occurs in these three
    records. Source text captions were read without image pixels/raw datasets/supplements.
    Those unseen domains are not certified.
  target_ids:
  - GO:0031979
  evidence_ids:
  - septin-record-plasma_membrane_derived_thylakoid_lumen
  - septin-go
  - septin-huokko2021-jats
  - septin-casella2017-jats
  - septin-perez2024-delivered
- assessment_id: septin-plasma_membrane_derived_thylakoid_lumen-verdict
  area: completeness
  topic: Current scientific verdict and exact lineage
  outcome: concern
  summary: 'needs_curation: inherited major F1 experimental-organism attribution remains
    open. No new scientific finding; maintained-record fixes stay outside this review-only
    PR. Original exact keys, severity normalization and predecessor references are
    preserved.'
  target_ids:
  - GO:0031979
  evidence_ids:
  - septin-record-plasma_membrane_derived_thylakoid_lumen
  - septin-go
  - septin-huokko2021-jats
  - septin-casella2017-jats
  - septin-perez2024-delivered
  - septin-original-plasma_membrane_derived_thylakoid_lumen
- assessment_id: septin-plasma_membrane_derived_thylakoid_membrane-schema
  area: schema
  topic: Original native validation/render and frozen input
  outcome: supported
  summary: Actual original native validation/render pass with exact Markdown. Historical
    frozen target hash verified. Current membrane input is stale and is substantively
    refreshed against primary and secondary sources; historical evidence is not reauthored.
  target_ids:
  - GO:0031676
  evidence_ids:
  - septin-record-plasma_membrane_derived_thylakoid_membrane
  - septin-original-validation-plasma_membrane_derived_thylakoid_membrane
- assessment_id: septin-plasma_membrane_derived_thylakoid_membrane-identity
  area: identity
  topic: Exact identity, synonym and structural boundary
  outcome: supported
  summary: GO0031676 and SL0045 identify cellular thylakoid membrane, with GO0042651
    is-a and GO0030075 parthood. Whole-thylakoid ontology part assertions are not
    falsely stated as direct membrane axioms; primary residence evidence supports
    the membrane representation.
  target_ids:
  - GO:0031676
  evidence_ids:
  - septin-record-plasma_membrane_derived_thylakoid_membrane
  - septin-go
  - septin-huokko2021-jats
  - septin-casella2017-jats
  - septin-perez2024-delivered
  - septin-SL0045
- assessment_id: septin-plasma_membrane_derived_thylakoid_membrane-definition
  area: scope
  topic: Definition source and expanded biological scope
  outcome: supported
  summary: Definition remains topological rather than a fixed cross-taxon protein
    inventory. Plasma-membrane-derived terminology does not require a continuing physical
    bridge; actual7942 cryoET reports no apparent direct connection.
  target_ids:
  - GO:0031676
  evidence_ids:
  - septin-record-plasma_membrane_derived_thylakoid_membrane
  - septin-go
  - septin-huokko2021-jats
  - septin-casella2017-jats
  - septin-perez2024-delivered
- assessment_id: septin-plasma_membrane_derived_thylakoid_membrane-taxon
  area: scope
  topic: Actual source organism, strain and occurrence
  outcome: concern
  summary: 'Inherited major F1 persists: current canonical example attributes Huokko2021
    to Synechocystis6803, but Methods/Results specify Synechococcus elongatus7942.
    Casella2017 mapping/FRAP notes in the PSI component and graph likewise misattribute
    the host. PCC6803 presence itself is not refuted. Cyanobacteriota COMMON with
    Gloeobacter exception is qualitative, not a census.'
  target_ids:
  - GO:0031676
  evidence_ids:
  - septin-record-plasma_membrane_derived_thylakoid_membrane
  - septin-go
  - septin-huokko2021-jats
  - septin-casella2017-jats
  - septin-perez2024-delivered
  - septin-tax1117
  - septin-tax1148
  - septin-tax1140
- assessment_id: septin-plasma_membrane_derived_thylakoid_membrane-material
  area: grounding
  topic: Constituent/material scope
  outcome: supported
  summary: Collective label-only lipid matrix denotes constitutive bilayer material,
    not a guessed chemical species or a whole-membrane GO substituted as chemical
    identity. Four GO-grounded complexes are distinct physical assemblies; UNKNOWN
    formation necessity is retained. No exact lipid percentage is imported from a
    review.
  target_ids:
  - GO:0031676
  evidence_ids:
  - septin-record-plasma_membrane_derived_thylakoid_membrane
  - septin-go
  - septin-huokko2021-jats
  - septin-casella2017-jats
  - septin-perez2024-delivered
  - septin-curation-policy
  - septin-schema-policy
- assessment_id: septin-plasma_membrane_derived_thylakoid_membrane-experimental
  area: evidence
  topic: Direct experimental result versus context
  outcome: supported
  summary: Casella uses native7942 thylakoid preparations and functional fluorescent
    tags; AFM b6f shape assignment is tentative and distinct from tagged localization.
    Huokko uses HL-to-LL recovery and cryoET in7942; no direct membrane continuity
    is assumed. Perez is secondary synthesis, not a new primary assay.
  target_ids:
  - GO:0031676
  evidence_ids:
  - septin-record-plasma_membrane_derived_thylakoid_membrane
  - septin-go
  - septin-huokko2021-jats
  - septin-casella2017-jats
  - septin-perez2024-delivered
- assessment_id: septin-plasma_membrane_derived_thylakoid_membrane-function
  area: evidence
  topic: Biological function and necessity
  outcome: supported
  summary: PSII, b6f and PSI electron transport and proton-gradient-driven ATP synthesis
    are supported at complex/pathway level. Individual subunit necessity, invariant
    stoichiometry and universal membrane composition are not demonstrated here.
  target_ids:
  - GO:0031676
  evidence_ids:
  - septin-record-plasma_membrane_derived_thylakoid_membrane
  - septin-go
  - septin-huokko2021-jats
  - septin-casella2017-jats
  - septin-perez2024-delivered
- assessment_id: septin-plasma_membrane_derived_thylakoid_membrane-graph
  area: graph
  topic: Graph scope and complete edge inventory
  outcome: supported
  summary: 'Current NONMECHANISTIC graph has6 descriptive edges: boundary, PSII/b6f/PSI
    residence, electron-transport association and newly added ATP-synthase residence.
    The old frozen graph had5 and lacked the ATP edge, despite the original review
    saying it was already there.'
  target_ids:
  - GO:0031676
  evidence_ids:
  - septin-record-plasma_membrane_derived_thylakoid_membrane
  - septin-go
  - septin-huokko2021-jats
  - septin-casella2017-jats
  - septin-perez2024-delivered
  - septin-graph-policy
  - septin-schema-policy
  - septin-original-plasma_membrane_derived_thylakoid_membrane
- assessment_id: septin-plasma_membrane_derived_thylakoid_membrane-native
  area: provenance
  topic: Actual native coverage versus molecular completeness
  outcome: supported
  summary: Actual two native commands pass. Independent count is0 examples,0 typed
    molecular nodes,0 UniProtKB graph xrefs. Existing GO protein-complex components
    and STRUCTURE nodes remain valid; no automatic enum or mandatory representative
    finding is invented.
  target_ids:
  - GO:0031676
  evidence_ids:
  - septin-record-plasma_membrane_derived_thylakoid_membrane
  - septin-native-plasma_membrane_derived_thylakoid_membrane-verify
  - septin-native-plasma_membrane_derived_thylakoid_membrane-causal
  - septin-protein-policy
- assessment_id: septin-plasma_membrane_derived_thylakoid_membrane-adapter
  area: scope
  topic: Whole-record structured-source applicability
  outcome: supported
  summary: Positive photochemistry/proton-gradient and complex/pathway assertions
    trigger policy. Fresh catalogue and bounded s_elongatus/elprecise300 gene/module
    checks cover actual cited7942 experiments and broad cyanobacterial context. They
    do not substitute for unmatched6803 or repair its source attribution. psaA/petB
    pass module38 thresholds; psbA1/atpA all-false flags do not establish biological
    absence. Historical00:49Z unavailable runner is separate from these completed
    fresh HTTP/source checks.
  target_ids:
  - GO:0031676
  evidence_ids:
  - septin-record-plasma_membrane_derived_thylakoid_membrane
  - septin-go
  - septin-huokko2021-jats
  - septin-casella2017-jats
  - septin-perez2024-delivered
  - septin-review-policy
  - septin-catalogue
  - septin-adapter-runner-historical
  - septin-adapter-gene-Synpcc7942_2049-modules
  - septin-adapter-gene-Synpcc7942_0424-modules
  - septin-adapter-gene-Synpcc7942_2331-modules
  - septin-adapter-gene-Synpcc7942_0336-modules
  - septin-adapter-module-38
- assessment_id: septin-plasma_membrane_derived_thylakoid_membrane-history
  area: provenance
  topic: Append-only provenance and boundary contexts
  outcome: supported
  summary: PROPOSED state and dated history/discussion remain unchanged. Historical
    resolved topology/material discussions are not rewritten as current inventories.
    Bounded frozen neighbor anatomy does not dispose another record or grouped issue.
    Added ATP-edge history is current-source context; no claim that old review had
    actually inspected it.
  target_ids:
  - GO:0031676
  evidence_ids:
  - septin-record-plasma_membrane_derived_thylakoid_membrane
  - septin-curation-policy
  - septin-original-plasma_membrane_derived_thylakoid_membrane
- assessment_id: septin-plasma_membrane_derived_thylakoid_membrane-formation
  area: completeness
  topic: Unresolved formation/assembly detail
  outcome: unknown
  summary: Source anatomy, measured trafficking/localization and secondary photochemical
    synthesis do not establish exhaustive formation machinery, invariant molecular
    composition or individual necessary subunits across taxa. Optional protein examples
    are not mandatory solely because sources identify proteins.
  target_ids:
  - GO:0031676
  evidence_ids:
  - septin-record-plasma_membrane_derived_thylakoid_membrane
  - septin-go
  - septin-huokko2021-jats
  - septin-casella2017-jats
  - septin-perez2024-delivered
  - septin-protein-policy
- assessment_id: septin-plasma_membrane_derived_thylakoid_membrane-optional
  area: scope
  topic: Absent image/measurement/protein domains
  outcome: not_applicable
  summary: No maintained image/license claim, individual protein accession, quantitative
    measurement, associated-trait mapping or verbatim snippet occurs in these three
    records. Source text captions were read without image pixels/raw datasets/supplements.
    Those unseen domains are not certified.
  target_ids:
  - GO:0031676
  evidence_ids:
  - septin-record-plasma_membrane_derived_thylakoid_membrane
  - septin-go
  - septin-huokko2021-jats
  - septin-casella2017-jats
  - septin-perez2024-delivered
- assessment_id: septin-plasma_membrane_derived_thylakoid_membrane-verdict
  area: completeness
  topic: Current scientific verdict and exact lineage
  outcome: concern
  summary: 'needs_curation: inherited major F1 experimental-organism attribution remains
    open. No new scientific finding; maintained-record fixes stay outside this review-only
    PR. Original exact keys, severity normalization and predecessor references are
    preserved.'
  target_ids:
  - GO:0031676
  evidence_ids:
  - septin-record-plasma_membrane_derived_thylakoid_membrane
  - septin-go
  - septin-huokko2021-jats
  - septin-casella2017-jats
  - septin-perez2024-delivered
  - septin-original-plasma_membrane_derived_thylakoid_membrane
- assessment_id: plaque-t1-schema
  area: schema
  topic: Historical originals and current represented molecular coverage
  outcome: supported
  summary: Both original pairs validate/render exactly with20 historical inputs each.
    Current native examples/node counts are separately bound; original graph coverage
    does not certify later changes. Root owns current corpus/publication gates.
  target_ids:
  - GO:0034357
  evidence_ids:
  - plaque-current-1
  - plaque-original-1
  - plaque-original-checks
  - plaque-native-photosynthetic_membrane-verify
  - plaque-native-photosynthetic_membrane-causal
- assessment_id: plaque-t2-schema
  area: schema
  topic: Historical originals and current represented molecular coverage
  outcome: supported
  summary: Both original pairs validate/render exactly with20 historical inputs each.
    Current native examples/node counts are separately bound; original graph coverage
    does not certify later changes. Root owns current corpus/publication gates.
  target_ids:
  - GO:0042717
  evidence_ids:
  - plaque-current-2
  - plaque-original-2
  - plaque-original-checks
  - plaque-native-plasma_membrane_derived_chromatophore_membrane-verify
  - plaque-native-plasma_membrane_derived_chromatophore_membrane-causal
- assessment_id: plaque-t1-identity
  area: identity
  topic: Generic photosynthetic membrane boundary
  outcome: supported
  summary: GO0034357 exactly matches broad photosynthetic membrane and membrane parent.
    Oxygenic and purple-bacterial subclasses coexist; broad reaction-center/carrier
    classes are not one exact narrow protein family.
  target_ids:
  - GO:0034357
  evidence_ids:
  - plaque-current-1
  - plaque-go
  - plaque-SL0042
- assessment_id: plaque-t1-material
  area: grounding
  topic: Declared lipid, pigment and protein classes
  outcome: supported
  summary: Collective lipid matrix is label-only without whole-membrane chemical misgrounding.
    Broad pigments/carriers and reaction-center or cytochrome classes are explicitly
    heterogeneous. Component examples do not define exhaustive stoichiometry or identical
    incorporation across lineages.
  target_ids:
  - GO:0034357
  evidence_ids:
  - plaque-current-1
  - plaque-schema-policy
  - plaque-casella2017-jats
  - plaque-perez2024-delivered
  - plaque-bahatyrova2004-pdf
- assessment_id: plaque-t1-necessity
  area: evidence
  topic: Constitutional classes versus individual assembly requirements
  outcome: unknown
  summary: Bilayer and broad photochemical classes are constitutional to this generic
    structure. Specific gene/protein/pigment depletion requirements do not follow
    from mature localization or activity; UNKNOWN specific-complex necessity remains
    appropriate.
  target_ids:
  - GO:0034357
  evidence_ids:
  - plaque-current-1
  - plaque-rubric
  - plaque-schema-policy
  - plaque-casella2017-jats
- assessment_id: plaque-t1-proteins
  area: grounding
  topic: Eight reviewed examples and exact taxa
  outcome: supported
  summary: PsaA/PSII D1, PufL/M, cytochromef/b6 andpurplepetB/fbcB,petC/fbcC identities
    agree. P16033 includes psbA2 andpsbA3; tax1111708 is Kazusa, separate fromsourcePCC7942.
    Annotation evidence codes and abstract-only experimental cross-checks retain limits.
  target_ids:
  - GO:0034357
  evidence_ids:
  - plaque-current-1
  - plaque-reviewed-genes-1111708
  - plaque-reviewed-genes-1063
  - plaque-protein-P29254
  - plaque-protein-P0C0Y8
  - plaque-protein-P0C0Y9
  - plaque-protein-P16033
  - plaque-protein-P26287
  - plaque-protein-Q57038
  - plaque-protein-Q02761
  - plaque-protein-Q02760
  - plaque-PMID11788579
  - plaque-PMID12069591
  - plaque-PMID19577535
  - plaque-PMID34937700
  - plaque-PMID35726684
- assessment_id: plaque-t1-scope
  area: scope
  topic: Qualitative distribution and actual canonical hosts
  outcome: concern
  summary: Perez secondaryIntroduction supports widespread cyanobacterial thylakoids
    withGloeobacter exception; broadBacteria prevalence is qualitative, not a census.
    Casella source isPCC7942, whereas canonicalexample0/onegraphsource note namePCC6803.
    Independent PCC6803 protein examples remain valid.
  target_ids:
  - GO:0034357
  evidence_ids:
  - plaque-current-1
  - plaque-perez2024-delivered
  - plaque-casella2017-jats
  - plaque-tax1117
  - plaque-tax1148
  - plaque-tax1140
  - plaque-tax1111708
- assessment_id: plaque-t1-graph
  area: graph
  topic: Seven descriptive photochemistry edges
  outcome: supported
  summary: Current seven NONMECHANISTIC edges summarize pigment binding/excitation,
    residence, carrier andcytochrome routing, PMF andelectron transport. They are
    illustrative oxygenic/purple contexts, not one universally conserved stoichiometric
    mechanism. Casella source attribution remains a separate finding.
  target_ids:
  - GO:0034357
  evidence_ids:
  - plaque-current-1
  - plaque-graph-rubric
  - plaque-casella2017-jats
  - plaque-bahatyrova2004-pdf
  - plaque-feniouk2002-author-pdf
  - plaque-perez2024-delivered
- assessment_id: plaque-t1-function
  area: grounding
  topic: Oxygenic process scope
  outcome: concern
  summary: GO0019684 defines oxygenic PSI/PSII wateroxidation/NADPreduction; current
    broad description also cites purple architecture without oxygenic-subset qualification.
    Retain broadGO0009767context and delimit this narrower function rather than excluding
    valid anoxygenic membranes.
  target_ids:
  - GO:0034357
  evidence_ids:
  - plaque-current-1
  - plaque-go
  - plaque-perez2024-delivered
  - plaque-bahatyrova2004-pdf
- assessment_id: plaque-t1-boundaries
  area: scope
  topic: Integral versus peripheral antenna and optional inventory
  outcome: supported
  summary: Bahatyrova supports integral LH2; Sui secondaryabstract and Nielsen primaryabstract
    give bounded peripheral antenna/baseplate context. Open discussion appropriately
    avoids projecting every antenna as an integral membrane part. Optional complete
    subtype inventory or generic ATPase enrichment is not automatically mandatory.
  target_ids:
  - GO:0034357
  evidence_ids:
  - plaque-current-1
  - plaque-bahatyrova2004-pdf
  - plaque-sui2021-meta
  - plaque-nielsen2016-meta
  - plaque-go
  - plaque-history-policy
- assessment_id: plaque-t1-adapter
  area: evidence
  topic: Positive molecular/pathway claims and matched source organism
  outcome: supported
  summary: Whole record asserts genes, proteins and photochemical pathways, so expression-only
    narrative exclusion is invalid. Fresh catalogue permits bounded PCC7942 source-context
    checks; selectedgene/module results agree with pathway context. No dataset is
    substituted for canonicalPCC6803 or purplehosts.
  target_ids:
  - GO:0034357
  evidence_ids:
  - plaque-current-1
  - plaque-original-1
  - plaque-policy
  - plaque-catalogue
  - plaque-adapter-search-photosystem
  - plaque-adapter-search-cytochrome-b6
  - plaque-adapter-gene-Synpcc7942_2049-modules
  - plaque-adapter-gene-Synpcc7942_0424-modules
  - plaque-adapter-gene-Synpcc7942_2331-modules
  - plaque-adapter-module-38
  - plaque-historical-runner
- assessment_id: plaque-t2-identity
  area: identity
  topic: Purple bacterial membrane versus organellar chromatophore
  outcome: supported
  summary: GO0042717/SL0042 are exact purple-bacterial plasma-derived membrane; GO0070112
    is separate organellar membrane. Generic photosynthetic parent and related broad
    chromatophore synonym preserve that boundary.
  target_ids:
  - GO:0042717
  evidence_ids:
  - plaque-current-2
  - plaque-go
  - plaque-SL0042
- assessment_id: plaque-t2-composition
  area: grounding
  topic: Existing whole-complex constituents and exact groundings
  outcome: concern
  summary: RC-LH1-PufX andbc1 local identities match current grounded components/nodes.
    Existing LH2 andF0F1 remain label-only despite exact maintainedLH2 andactiveGO0045259F1-F0
    identity; this inherited bounded mapping defect is not an optional new inventory
    demand.
  target_ids:
  - GO:0042717
  evidence_ids:
  - plaque-current-2
  - plaque-go
  - plaque-SL0042
  - plaque-context-lh2_peripheral_light_harvesting_antenna_complex
  - plaque-context-rc_lh1_pufx_core_complex
  - plaque-context-chromatophore_cytochrome_bc1_complex
- assessment_id: plaque-t2-necessity
  area: evidence
  topic: Specific complex formation requirements
  outcome: unknown
  summary: The bilayer is constitutional; every listed specific complex remains UNKNOWN
    for formation necessity. AFM architecture, photochemical activity, inferred annotations
    and isolated-vesicle coupling do not establish each complex is indispensable for
    building all chromatophores.
  target_ids:
  - GO:0042717
  evidence_ids:
  - plaque-current-2
  - plaque-rubric
  - plaque-bahatyrova2004-pdf
  - plaque-feniouk2002-author-pdf
- assessment_id: plaque-t2-proteins
  area: grounding
  topic: Six reviewed examples with strain-specific identity
  outcome: supported
  summary: LH2pucA/B andATPaseatpA/B/D/E examples match reviewed identities and exacttaxa.
    atpD usesATCC17025 whereasatpA/B/E use2.4.1; individual examples are not represented
    as one experimentally measured complete complex in one strain. Native graph count
    is nowzero typedmolecular nodes.
  target_ids:
  - GO:0042717
  evidence_ids:
  - plaque-current-2
  - plaque-reviewed-genes-1063
  - plaque-tax1063
  - plaque-tax272943
  - plaque-tax349102
  - plaque-protein-P0C0Y0
  - plaque-protein-P0C0Y2
  - plaque-protein-A4WUM7
  - plaque-protein-Q3J433
  - plaque-protein-Q3IZ12
  - plaque-protein-Q3IZ13
- assessment_id: plaque-t2-scope
  area: scope
  topic: Source strains and bounded prevalence
  outcome: supported
  summary: BahatyrovaNCIB8253, ComayrasGa andFenioukR.capsulatusB10 are separate contexts.
    They support illustrative purple-bacterial architecture/coupling, not universalc2
    use, invariantdimer geometry or quantifiedBacteria prevalence.
  target_ids:
  - GO:0042717
  evidence_ids:
  - plaque-current-2
  - plaque-bahatyrova2004-pdf
  - plaque-comayras-browser-methods
  - plaque-feniouk2002-author-pdf
  - plaque-tax1063
  - plaque-tax272943
- assessment_id: plaque-t2-graph
  area: graph
  topic: Substantive refresh of two added edges
  outcome: supported
  summary: Eight current NONMECHANISTIC edges include newbc1→PMF andRC-LH1-PufX→membrane.
    Feniouk supports bc1-associated voltage contribution/coupling andBahatyrova actualRC/LH2
    membrane residence. Comayras inhibited-pool assay is not unperturbed PMF measurement.
    No unsupported universal mechanism or necessity is added.
  target_ids:
  - GO:0042717
  evidence_ids:
  - plaque-current-2
  - plaque-original-2
  - plaque-feniouk2002-author-pdf
  - plaque-bahatyrova2004-pdf
  - plaque-comayras-browser-methods
  - plaque-graph-rubric
- assessment_id: plaque-t2-stale
  area: provenance
  topic: Substantive current-input refresh without category-wide disposition
  outcome: supported
  summary: Current addedlocalRC/bc1groundings andSTRUCTURE retypings are coherent,
    but do not resolve independentLH2/F0F1 constituent mapping. Original20inputhashes
    remain historical. Current eightedges/sixexamples/zero typednodes replace old
    sixedge/typednode account. No disposition of all#2432 category records is inferred.
  target_ids:
  - GO:0042717
  evidence_ids:
  - plaque-current-2
  - plaque-original-2
  - plaque-original-checks
  - plaque-context-rc_lh1_pufx_core_complex
  - plaque-context-chromatophore_cytochrome_bc1_complex
  - plaque-graph-rubric
  - plaque-history-policy
- assessment_id: plaque-t2-adapter
  area: evidence
  topic: Applicability assessed before actual purple-host noncoverage
  outcome: supported
  summary: NamedLH2/ATPasegenes andcyclic photophosphorylation trigger required source
    assessment even without expression-module claims. Complete current catalogue has
    noCereibacter/Rhodobacter matching host. PCC7942 results are not a purple-host
    proxy; no unmatched downstreamquery or negativebiology inferred.
  target_ids:
  - GO:0042717
  evidence_ids:
  - plaque-current-2
  - plaque-original-2
  - plaque-policy
  - plaque-catalogue
  - plaque-historical-runner
- assessment_id: plaque-t1-coverage
  area: completeness
  topic: Complete current scope without optional enrichment
  outcome: supported
  summary: Every current field and graph/source placement assessed; no maintained
    image, direct quotation or quantitative physical-property claim requires pixel/measurement
    validation. No newprotein/chemical inventory mandated. Historical rationale remains
    append-only; curation actions stay separate from review refresh.
  target_ids:
  - GO:0034357
  evidence_ids:
  - plaque-current-1
  - plaque-rubric
  - plaque-history-policy
  - plaque-schema-policy
- assessment_id: plaque-t2-coverage
  area: completeness
  topic: Complete current scope without optional enrichment
  outcome: supported
  summary: Every current field and graph/source placement assessed; no maintained
    image, direct quotation or quantitative physical-property claim requires pixel/measurement
    validation. No newprotein/chemical inventory mandated. Historical rationale remains
    append-only; curation actions stay separate from review refresh.
  target_ids:
  - GO:0042717
  evidence_ids:
  - plaque-current-2
  - plaque-rubric
  - plaque-history-policy
  - plaque-schema-policy
- assessment_id: micro-plastid-identity
  area: identity
  topic: Exact identity and hierarchy
  outcome: supported
  summary: ExactGO9536 broad cytoplasmic organelle with GO43231 parent, cytoplasm
    parthood andSL0209 mapping. No universal photosynthesis or fixed membrane count
    asserted.
  target_ids:
  - GO:0009536
  evidence_ids:
  - micro-record-plastid
  - micro-go
  - micro-go0042170-isa
  - micro-SL0209
  - micro-SL0210
  - micro-SL0211
  - micro-SL0212
  - micro-SL0214
- assessment_id: micro-plastid-material
  area: grounding
  topic: Anatomical component identity versus chemical material
  outcome: concern
  summary: 'Inherited major F1 confirmed: LIPID rows ground complete GO membrane structures;
    component_ref inherits mismatch. Keep valid structural nodes/parts and use accurate
    structural or label-only material representation.'
  target_ids:
  - GO:0009536
  evidence_ids:
  - micro-record-plastid
  - micro-prior-plastid
  - micro-component-policy
  - micro-go
- assessment_id: micro-plastid-necessity
  area: evidence
  topic: Individual formation necessity
  outcome: unknown
  summary: UNKNOWN on whole/envelope retained; ESSENTIAL on inner/generic bilayer
    denotes defining collective material only. Neither anatomy nor TOC–TIC cryoEM
    observation establishes individual lipid/protein necessity for formation. IMS
    has no such constituent requirement.
  target_ids:
  - GO:0009536
  evidence_ids:
  - micro-record-plastid
  - micro-component-policy
  - micro-jin2022-meta
  - micro-go
- assessment_id: micro-plastid-graph
  area: graph
  topic: Every descriptive edge and source scope
  outcome: supported
  summary: 'Three NONMECHANISTIC relations: plastid in cytoplasm, membrane boundary,
    stroma contained. Membrane node remains correct despite F1 component join mismatch.'
  target_ids:
  - GO:0009536
  evidence_ids:
  - micro-record-plastid
  - micro-graph-policy
  - micro-go
  - micro-SL0209
  - micro-SL0210
  - micro-SL0211
  - micro-SL0212
  - micro-SL0214
  - micro-neighbor-plastid_stroma
  - micro-neighbor-plastid_outer_membrane
- assessment_id: micro-plastid-taxon
  area: scope
  topic: Qualitative occurrence and lineage bounds
  outcome: supported
  summary: Current2759/33090/3055 identities verified. Keeling s1/s3/s6 supports green-primary
    and scattered secondary/reduced contexts; RARE/COMMON are qualitative, not measured
    frequencies or all-isolate claims. Historical phylogenetic models are not presented
    as current complete consensus.
  target_ids:
  - GO:0009536
  evidence_ids:
  - micro-record-plastid
  - micro-tax2759
  - micro-tax33090
  - micro-tax3055
  - micro-keeling2010-meta
  - micro-keeling2010-retained
- assessment_id: micro-plastid-example
  area: evidence
  topic: Exact canonical example and experimental extent
  outcome: supported
  summary: Terashima secondary abstract and retained pp151–152 support a C.reinhardtii
    chloroplast used for proteome/protein-biogenesis research. The record does not
    claim a specific protein cohort, experimental membrane-only proteome or detailed
    pathway merely by naming the model.
  target_ids:
  - GO:0009536
  evidence_ids:
  - micro-record-plastid
  - micro-terashima2011-meta
  - micro-terashima2011-retained
- assessment_id: micro-plastid-adapter
  area: evidence
  topic: Whole-record structured-source applicability
  outcome: not_applicable
  summary: 'Genuine physical/material/class scope: canonical model use for proteome/protein-biogenesis
    studies is research context, not a positive specified molecular cohort/pathway.
    Graph/discussion withhold specialized machinery. Background source biology is
    not imported as a record assertion; no mandatory dataset query defect.'
  target_ids:
  - GO:0009536
  evidence_ids:
  - micro-record-plastid
  - micro-prior-plastid
  - micro-policy
  - micro-catalogue
  - micro-historical-runner
- assessment_id: micro-plastid-history
  area: provenance
  topic: Historical boundary decisions and grounding discussions
  outcome: supported
  summary: Original observations and current PROPOSED status remain unchanged; no
    closed historical or neighbor issue/category resolved. Source-neutral chemical
    TODOs remain valid; label-only constituents and append-only rationale do not require
    fabricated corrections.
  target_ids:
  - GO:0009536
  evidence_ids:
  - micro-record-plastid
  - micro-prior-plastid
  - micro-discussion-policy
  - micro-component-policy
- assessment_id: micro-plastid-native
  area: schema
  topic: Frozen inputs/native original pairs/current coverage
  outcome: supported
  summary: All75 old frozen hashes verify; five original YAML/Markdown pairs validate/render
    exactly. Own target unchanged. Ten actual native protein commands pass with zero
    examples/typed nodes; positive narrative machinery still needs applicability assessment.
  target_ids:
  - GO:0009536
  evidence_ids:
  - micro-prior-plastid
  - micro-original-pairs
  - micro-original-inputs
  - micro-native-plastid-verify
  - micro-native-plastid-causal
- assessment_id: micro-plastid-coverage
  area: completeness
  topic: Complete record and bounded verdict
  outcome: supported
  summary: 'Full current record reviewed: no maintained images, verbatim snippets,
    quantitative physical properties or individual protein accessions require extra
    claims. Exact inherited major finding/action retained; no new scientific finding.'
  target_ids:
  - GO:0009536
  evidence_ids:
  - micro-record-plastid
  - micro-prior-plastid
  - micro-policy
  - micro-go
  - micro-original-pairs
- assessment_id: micro-plastid_envelope-identity
  area: identity
  topic: Exact identity and hierarchy
  outcome: supported
  summary: ExactGO9526 double envelope including IMS, organelle-envelope parent/plastid
    parthood andSL0210 synonym. Scope is primary double envelope distinct from extra
    surrounding complex-plastid membranes.
  target_ids:
  - GO:0009526
  evidence_ids:
  - micro-record-plastid_envelope
  - micro-go
  - micro-go0042170-isa
  - micro-SL0209
  - micro-SL0210
  - micro-SL0211
  - micro-SL0212
  - micro-SL0214
- assessment_id: micro-plastid_envelope-material
  area: grounding
  topic: Anatomical component identity versus chemical material
  outcome: concern
  summary: 'Inherited major F2 confirmed: LIPID rows ground complete GO membrane structures;
    component_ref inherits mismatch. Keep valid structural nodes/parts and use accurate
    structural or label-only material representation.'
  target_ids:
  - GO:0009526
  evidence_ids:
  - micro-record-plastid_envelope
  - micro-prior-plastid_envelope
  - micro-component-policy
  - micro-go
- assessment_id: micro-plastid_envelope-necessity
  area: evidence
  topic: Individual formation necessity
  outcome: unknown
  summary: UNKNOWN on whole/envelope retained; ESSENTIAL on inner/generic bilayer
    denotes defining collective material only. Neither anatomy nor TOC–TIC cryoEM
    observation establishes individual lipid/protein necessity for formation. IMS
    has no such constituent requirement.
  target_ids:
  - GO:0009526
  evidence_ids:
  - micro-record-plastid_envelope
  - micro-component-policy
  - micro-jin2022-meta
  - micro-go
- assessment_id: micro-plastid_envelope-graph
  area: graph
  topic: Every descriptive edge and source scope
  outcome: supported
  summary: 'Five NONMECHANISTIC edges: envelope encloses plastid, outer/inner part_of
    envelope, envelope containsIMS, inner boundsstroma. True topology retained independently
    from F1 typed-component mismatch.'
  target_ids:
  - GO:0009526
  evidence_ids:
  - micro-record-plastid_envelope
  - micro-graph-policy
  - micro-go
  - micro-SL0209
  - micro-SL0210
  - micro-SL0211
  - micro-SL0212
  - micro-SL0214
  - micro-neighbor-plastid_stroma
  - micro-neighbor-plastid_outer_membrane
- assessment_id: micro-plastid_envelope-taxon
  area: scope
  topic: Qualitative occurrence and lineage bounds
  outcome: supported
  summary: Current2759/33090/3055 identities verified. Keeling s1/s3/s6 supports green-primary
    and scattered secondary/reduced contexts; RARE/COMMON are qualitative, not measured
    frequencies or all-isolate claims. Historical phylogenetic models are not presented
    as current complete consensus.
  target_ids:
  - GO:0009526
  evidence_ids:
  - micro-record-plastid_envelope
  - micro-tax2759
  - micro-tax33090
  - micro-tax3055
  - micro-keeling2010-meta
  - micro-keeling2010-retained
- assessment_id: micro-plastid_envelope-example
  area: evidence
  topic: Exact canonical example and experimental extent
  outcome: supported
  summary: Jin primary abstract+indexed species keyword supports C.reinhardtii TOC–TIC
    bridge/IMS or Tic-side context. No full Methods, strain, raw structure/pixels
    or individual formation necessity certified.
  target_ids:
  - GO:0009526
  evidence_ids:
  - micro-record-plastid_envelope
  - micro-jin2022-meta
- assessment_id: micro-plastid_envelope-adapter
  area: evidence
  topic: Whole-record structured-source applicability
  outcome: concern
  summary: 'Original expression-only exclusion is unsupported: taxonomy/canonical
    prose positively asserts TOC–TIC import supercomplex at this boundary. Fresh official
    catalogue lacks matching Chlamydomonas host; no proxy/downstream unmatched query.'
  target_ids:
  - GO:0009526
  evidence_ids:
  - micro-record-plastid_envelope
  - micro-prior-plastid_envelope
  - micro-policy
  - micro-catalogue
  - micro-historical-runner
- assessment_id: micro-plastid_envelope-history
  area: provenance
  topic: Historical boundary decisions and grounding discussions
  outcome: supported
  summary: Original observations and current PROPOSED status remain unchanged; no
    closed historical or neighbor issue/category resolved. Source-neutral chemical
    TODOs remain valid; label-only constituents and append-only rationale do not require
    fabricated corrections.
  target_ids:
  - GO:0009526
  evidence_ids:
  - micro-record-plastid_envelope
  - micro-prior-plastid_envelope
  - micro-discussion-policy
  - micro-component-policy
- assessment_id: micro-plastid_envelope-native
  area: schema
  topic: Frozen inputs/native original pairs/current coverage
  outcome: supported
  summary: All75 old frozen hashes verify; five original YAML/Markdown pairs validate/render
    exactly. Own target unchanged. Ten actual native protein commands pass with zero
    examples/typed nodes; positive narrative machinery still needs applicability assessment.
  target_ids:
  - GO:0009526
  evidence_ids:
  - micro-prior-plastid_envelope
  - micro-original-pairs
  - micro-original-inputs
  - micro-native-plastid_envelope-verify
  - micro-native-plastid_envelope-causal
- assessment_id: micro-plastid_envelope-coverage
  area: completeness
  topic: Complete record and bounded verdict
  outcome: supported
  summary: 'Full current record reviewed: no maintained images, verbatim snippets,
    quantitative physical properties or individual protein accessions require extra
    claims. Exact inherited major finding/action retained; no new scientific finding.'
  target_ids:
  - GO:0009526
  evidence_ids:
  - micro-record-plastid_envelope
  - micro-prior-plastid_envelope
  - micro-policy
  - micro-go
  - micro-original-pairs
- assessment_id: micro-plastid_inner_membrane-identity
  area: identity
  topic: Exact identity and hierarchy
  outcome: supported
  summary: ExactGO9528 stroma-facing bilayer, generic membrane parent/envelope part
    and threeSL0211 synonyms; IMS remains distinct.
  target_ids:
  - GO:0009528
  evidence_ids:
  - micro-record-plastid_inner_membrane
  - micro-go
  - micro-go0042170-isa
  - micro-SL0209
  - micro-SL0210
  - micro-SL0211
  - micro-SL0212
  - micro-SL0214
- assessment_id: micro-plastid_inner_membrane-material
  area: grounding
  topic: Anatomical component identity versus chemical material
  outcome: supported
  summary: Reviewed-label-only collective bilayer material has no erroneous whole-membrane
    chemical grounding. Defining collective material remains distinct from exact lipid
    species.
  target_ids:
  - GO:0009528
  evidence_ids:
  - micro-record-plastid_inner_membrane
  - micro-prior-plastid_inner_membrane
  - micro-component-policy
  - micro-go
- assessment_id: micro-plastid_inner_membrane-necessity
  area: evidence
  topic: Individual formation necessity
  outcome: unknown
  summary: UNKNOWN on whole/envelope retained; ESSENTIAL on inner/generic bilayer
    denotes defining collective material only. Neither anatomy nor TOC–TIC cryoEM
    observation establishes individual lipid/protein necessity for formation. IMS
    has no such constituent requirement.
  target_ids:
  - GO:0009528
  evidence_ids:
  - micro-record-plastid_inner_membrane
  - micro-component-policy
  - micro-jin2022-meta
  - micro-go
- assessment_id: micro-plastid_inner_membrane-graph
  area: graph
  topic: Every descriptive edge and source scope
  outcome: supported
  summary: Three NONMECHANISTIC edges correctly state envelope parthood, stroma boundary
    andIMS delimitation; no universal translocon inventory asserted.
  target_ids:
  - GO:0009528
  evidence_ids:
  - micro-record-plastid_inner_membrane
  - micro-graph-policy
  - micro-go
  - micro-SL0209
  - micro-SL0210
  - micro-SL0211
  - micro-SL0212
  - micro-SL0214
  - micro-neighbor-plastid_stroma
  - micro-neighbor-plastid_outer_membrane
- assessment_id: micro-plastid_inner_membrane-taxon
  area: scope
  topic: Qualitative occurrence and lineage bounds
  outcome: supported
  summary: Current2759/33090/3055 identities verified. Keeling s1/s3/s6 supports green-primary
    and scattered secondary/reduced contexts; RARE/COMMON are qualitative, not measured
    frequencies or all-isolate claims. Historical phylogenetic models are not presented
    as current complete consensus.
  target_ids:
  - GO:0009528
  evidence_ids:
  - micro-record-plastid_inner_membrane
  - micro-tax2759
  - micro-tax33090
  - micro-tax3055
  - micro-keeling2010-meta
  - micro-keeling2010-retained
- assessment_id: micro-plastid_inner_membrane-example
  area: evidence
  topic: Exact canonical example and experimental extent
  outcome: supported
  summary: Jin primary abstract+indexed species keyword supports C.reinhardtii TOC–TIC
    bridge/IMS or Tic-side context. No full Methods, strain, raw structure/pixels
    or individual formation necessity certified.
  target_ids:
  - GO:0009528
  evidence_ids:
  - micro-record-plastid_inner_membrane
  - micro-jin2022-meta
- assessment_id: micro-plastid_inner_membrane-adapter
  area: evidence
  topic: Whole-record structured-source applicability
  outcome: concern
  summary: 'Original expression-only exclusion is unsupported: taxonomy/canonical
    prose positively asserts TOC–TIC import supercomplex at this boundary. Fresh official
    catalogue lacks matching Chlamydomonas host; no proxy/downstream unmatched query.'
  target_ids:
  - GO:0009528
  evidence_ids:
  - micro-record-plastid_inner_membrane
  - micro-prior-plastid_inner_membrane
  - micro-policy
  - micro-catalogue
  - micro-historical-runner
- assessment_id: micro-plastid_inner_membrane-history
  area: provenance
  topic: Historical boundary decisions and grounding discussions
  outcome: supported
  summary: Original observations and current PROPOSED status remain unchanged; no
    closed historical or neighbor issue/category resolved. Source-neutral chemical
    TODOs remain valid; label-only constituents and append-only rationale do not require
    fabricated corrections.
  target_ids:
  - GO:0009528
  evidence_ids:
  - micro-record-plastid_inner_membrane
  - micro-prior-plastid_inner_membrane
  - micro-discussion-policy
  - micro-component-policy
- assessment_id: micro-plastid_inner_membrane-native
  area: schema
  topic: Frozen inputs/native original pairs/current coverage
  outcome: supported
  summary: All75 old frozen hashes verify; five original YAML/Markdown pairs validate/render
    exactly. Own target unchanged. Ten actual native protein commands pass with zero
    examples/typed nodes; positive narrative machinery still needs applicability assessment.
  target_ids:
  - GO:0009528
  evidence_ids:
  - micro-prior-plastid_inner_membrane
  - micro-original-pairs
  - micro-original-inputs
  - micro-native-plastid_inner_membrane-verify
  - micro-native-plastid_inner_membrane-causal
- assessment_id: micro-plastid_inner_membrane-coverage
  area: completeness
  topic: Complete record and bounded verdict
  outcome: supported
  summary: 'Full current record reviewed: no maintained images, verbatim snippets,
    quantitative physical properties or individual protein accessions require extra
    claims. No supported scientific finding; qualified pass preserves molecular/experimental/access
    limits.'
  target_ids:
  - GO:0009528
  evidence_ids:
  - micro-record-plastid_inner_membrane
  - micro-prior-plastid_inner_membrane
  - micro-policy
  - micro-go
  - micro-original-pairs
- assessment_id: micro-plastid_intermembrane_space-identity
  area: identity
  topic: Exact identity and hierarchy
  outcome: supported
  summary: ExactGO9529 between-bilayer region withSL0212 synonym/envelope parthood;
    neither stroma nor membrane.
  target_ids:
  - GO:0009529
  evidence_ids:
  - micro-record-plastid_intermembrane_space
  - micro-go
  - micro-go0042170-isa
  - micro-SL0209
  - micro-SL0210
  - micro-SL0211
  - micro-SL0212
  - micro-SL0214
- assessment_id: micro-plastid_intermembrane_space-material
  area: grounding
  topic: Anatomical component identity versus chemical material
  outcome: supported
  summary: No components on the spatial IMS record; no invented molecular inventory.
  target_ids:
  - GO:0009529
  evidence_ids:
  - micro-record-plastid_intermembrane_space
  - micro-prior-plastid_intermembrane_space
  - micro-component-policy
  - micro-go
- assessment_id: micro-plastid_intermembrane_space-necessity
  area: evidence
  topic: Individual formation necessity
  outcome: unknown
  summary: UNKNOWN on whole/envelope retained; ESSENTIAL on inner/generic bilayer
    denotes defining collective material only. Neither anatomy nor TOC–TIC cryoEM
    observation establishes individual lipid/protein necessity for formation. IMS
    has no such constituent requirement.
  target_ids:
  - GO:0009529
  evidence_ids:
  - micro-record-plastid_intermembrane_space
  - micro-component-policy
  - micro-jin2022-meta
  - micro-go
- assessment_id: micro-plastid_intermembrane_space-graph
  area: graph
  topic: Every descriptive edge and source scope
  outcome: supported
  summary: Three NONMECHANISTIC edges correctly state envelope parthood and two bilayer
    boundaries; positive speciesTOC–TIC example separately bounded.
  target_ids:
  - GO:0009529
  evidence_ids:
  - micro-record-plastid_intermembrane_space
  - micro-graph-policy
  - micro-go
  - micro-SL0209
  - micro-SL0210
  - micro-SL0211
  - micro-SL0212
  - micro-SL0214
  - micro-neighbor-plastid_stroma
  - micro-neighbor-plastid_outer_membrane
- assessment_id: micro-plastid_intermembrane_space-taxon
  area: scope
  topic: Qualitative occurrence and lineage bounds
  outcome: supported
  summary: Current2759/33090/3055 identities verified. Keeling s1/s3/s6 supports green-primary
    and scattered secondary/reduced contexts; RARE/COMMON are qualitative, not measured
    frequencies or all-isolate claims. Historical phylogenetic models are not presented
    as current complete consensus.
  target_ids:
  - GO:0009529
  evidence_ids:
  - micro-record-plastid_intermembrane_space
  - micro-tax2759
  - micro-tax33090
  - micro-tax3055
  - micro-keeling2010-meta
  - micro-keeling2010-retained
- assessment_id: micro-plastid_intermembrane_space-example
  area: evidence
  topic: Exact canonical example and experimental extent
  outcome: supported
  summary: Jin primary abstract+indexed species keyword supports C.reinhardtii TOC–TIC
    bridge/IMS or Tic-side context. No full Methods, strain, raw structure/pixels
    or individual formation necessity certified.
  target_ids:
  - GO:0009529
  evidence_ids:
  - micro-record-plastid_intermembrane_space
  - micro-jin2022-meta
- assessment_id: micro-plastid_intermembrane_space-adapter
  area: evidence
  topic: Whole-record structured-source applicability
  outcome: concern
  summary: 'Original expression-only exclusion is unsupported: taxonomy/canonical
    prose positively asserts TOC–TIC import supercomplex at this boundary. Fresh official
    catalogue lacks matching Chlamydomonas host; no proxy/downstream unmatched query.'
  target_ids:
  - GO:0009529
  evidence_ids:
  - micro-record-plastid_intermembrane_space
  - micro-prior-plastid_intermembrane_space
  - micro-policy
  - micro-catalogue
  - micro-historical-runner
- assessment_id: micro-plastid_intermembrane_space-history
  area: provenance
  topic: Historical boundary decisions and grounding discussions
  outcome: supported
  summary: Original observations and current PROPOSED status remain unchanged; no
    closed historical or neighbor issue/category resolved. Source-neutral chemical
    TODOs remain valid; label-only constituents and append-only rationale do not require
    fabricated corrections.
  target_ids:
  - GO:0009529
  evidence_ids:
  - micro-record-plastid_intermembrane_space
  - micro-prior-plastid_intermembrane_space
  - micro-discussion-policy
  - micro-component-policy
- assessment_id: micro-plastid_intermembrane_space-native
  area: schema
  topic: Frozen inputs/native original pairs/current coverage
  outcome: supported
  summary: All75 old frozen hashes verify; five original YAML/Markdown pairs validate/render
    exactly. Own target unchanged. Ten actual native protein commands pass with zero
    examples/typed nodes; positive narrative machinery still needs applicability assessment.
  target_ids:
  - GO:0009529
  evidence_ids:
  - micro-prior-plastid_intermembrane_space
  - micro-original-pairs
  - micro-original-inputs
  - micro-native-plastid_intermembrane_space-verify
  - micro-native-plastid_intermembrane_space-causal
- assessment_id: micro-plastid_intermembrane_space-coverage
  area: completeness
  topic: Complete record and bounded verdict
  outcome: supported
  summary: 'Full current record reviewed: no maintained images, verbatim snippets,
    quantitative physical properties or individual protein accessions require extra
    claims. No supported scientific finding; qualified pass preserves molecular/experimental/access
    limits.'
  target_ids:
  - GO:0009529
  evidence_ids:
  - micro-record-plastid_intermembrane_space
  - micro-prior-plastid_intermembrane_space
  - micro-policy
  - micro-go
  - micro-original-pairs
- assessment_id: micro-plastid_membrane-identity
  area: identity
  topic: Exact identity and hierarchy
  outcome: supported
  summary: ExactGO42170 definition plusGO16020 ancestry; explicit GO is_a children
    andSL0213 nested fallback support internal thylakoid class despite envelope-focused
    definition prose.
  target_ids:
  - GO:0042170
  evidence_ids:
  - micro-record-plastid_membrane
  - micro-go
  - micro-go0042170-isa
  - micro-SL0209
  - micro-SL0210
  - micro-SL0211
  - micro-SL0212
  - micro-SL0214
- assessment_id: micro-plastid_membrane-material
  area: grounding
  topic: Anatomical component identity versus chemical material
  outcome: supported
  summary: Reviewed-label-only collective bilayer material has no erroneous whole-membrane
    chemical grounding. Defining collective material remains distinct from exact lipid
    species.
  target_ids:
  - GO:0042170
  evidence_ids:
  - micro-record-plastid_membrane
  - micro-prior-plastid_membrane
  - micro-component-policy
  - micro-go
- assessment_id: micro-plastid_membrane-necessity
  area: evidence
  topic: Individual formation necessity
  outcome: unknown
  summary: UNKNOWN on whole/envelope retained; ESSENTIAL on inner/generic bilayer
    denotes defining collective material only. Neither anatomy nor TOC–TIC cryoEM
    observation establishes individual lipid/protein necessity for formation. IMS
    has no such constituent requirement.
  target_ids:
  - GO:0042170
  evidence_ids:
  - micro-record-plastid_membrane
  - micro-component-policy
  - micro-jin2022-meta
  - micro-go
- assessment_id: micro-plastid_membrane-graph
  area: graph
  topic: Every descriptive edge and source scope
  outcome: supported
  summary: Three NONMECHANISTIC is_a edges outer,inner,thylakoid→generic membrane
    verified directly in GO children; no universal membrane count/protein composition
    inferred.
  target_ids:
  - GO:0042170
  evidence_ids:
  - micro-record-plastid_membrane
  - micro-graph-policy
  - micro-go
  - micro-SL0209
  - micro-SL0210
  - micro-SL0211
  - micro-SL0212
  - micro-SL0214
  - micro-neighbor-plastid_stroma
  - micro-neighbor-plastid_outer_membrane
- assessment_id: micro-plastid_membrane-taxon
  area: scope
  topic: Qualitative occurrence and lineage bounds
  outcome: supported
  summary: Current2759/33090/3055 identities verified. Keeling s1/s3/s6 supports green-primary
    and scattered secondary/reduced contexts; RARE/COMMON are qualitative, not measured
    frequencies or all-isolate claims. Historical phylogenetic models are not presented
    as current complete consensus.
  target_ids:
  - GO:0042170
  evidence_ids:
  - micro-record-plastid_membrane
  - micro-tax2759
  - micro-tax33090
  - micro-tax3055
  - micro-keeling2010-meta
  - micro-keeling2010-retained
- assessment_id: micro-plastid_membrane-example
  area: evidence
  topic: Exact canonical example and experimental extent
  outcome: supported
  summary: Terashima secondary abstract and retained pp151–152 support a C.reinhardtii
    chloroplast used for proteome/protein-biogenesis research. The record does not
    claim a specific protein cohort, experimental membrane-only proteome or detailed
    pathway merely by naming the model.
  target_ids:
  - GO:0042170
  evidence_ids:
  - micro-record-plastid_membrane
  - micro-terashima2011-meta
  - micro-terashima2011-retained
- assessment_id: micro-plastid_membrane-adapter
  area: evidence
  topic: Whole-record structured-source applicability
  outcome: not_applicable
  summary: 'Genuine physical/material/class scope: canonical model use for proteome/protein-biogenesis
    studies is research context, not a positive specified molecular cohort/pathway.
    Graph/discussion withhold specialized machinery. Background source biology is
    not imported as a record assertion; no mandatory dataset query defect.'
  target_ids:
  - GO:0042170
  evidence_ids:
  - micro-record-plastid_membrane
  - micro-prior-plastid_membrane
  - micro-policy
  - micro-catalogue
  - micro-historical-runner
- assessment_id: micro-plastid_membrane-history
  area: provenance
  topic: Historical boundary decisions and grounding discussions
  outcome: supported
  summary: Original observations and current PROPOSED status remain unchanged; no
    closed historical or neighbor issue/category resolved. Source-neutral chemical
    TODOs remain valid; label-only constituents and append-only rationale do not require
    fabricated corrections.
  target_ids:
  - GO:0042170
  evidence_ids:
  - micro-record-plastid_membrane
  - micro-prior-plastid_membrane
  - micro-discussion-policy
  - micro-component-policy
- assessment_id: micro-plastid_membrane-native
  area: schema
  topic: Frozen inputs/native original pairs/current coverage
  outcome: supported
  summary: All75 old frozen hashes verify; five original YAML/Markdown pairs validate/render
    exactly. Own target unchanged. Ten actual native protein commands pass with zero
    examples/typed nodes; positive narrative machinery still needs applicability assessment.
  target_ids:
  - GO:0042170
  evidence_ids:
  - micro-prior-plastid_membrane
  - micro-original-pairs
  - micro-original-inputs
  - micro-native-plastid_membrane-verify
  - micro-native-plastid_membrane-causal
- assessment_id: micro-plastid_membrane-coverage
  area: completeness
  topic: Complete record and bounded verdict
  outcome: supported
  summary: 'Full current record reviewed: no maintained images, verbatim snippets,
    quantitative physical properties or individual protein accessions require extra
    claims. No supported scientific finding; qualified pass preserves molecular/experimental/access
    limits.'
  target_ids:
  - GO:0042170
  evidence_ids:
  - micro-record-plastid_membrane
  - micro-prior-plastid_membrane
  - micro-policy
  - micro-go
  - micro-original-pairs
- assessment_id: current-input-comparison
  area: provenance
  topic: Complete frozen-input comparison and bounded refresh
  outcome: supported
  summary: 2 of ten original target hashes differ from current main. The changed content
    is substantively reassessed in the target-specific assessments; original observations
    remain historical and unchanged. All current target and used context bytes are
    frozen.
  target_ids:
  - GO:0106174
  - GO:0034357
  - GO:0042717
  - GO:0031979
  - GO:0031676
  - GO:0009536
  - GO:0009526
  - GO:0009528
  - GO:0009529
  - GO:0042170
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
- finding_id: septin-phagolysosome_vesicle_lumen-F1
  issue_key: phagolysosome-vesicle-lumen-expanded-definition-scope
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Bound the expanded definition to demonstrated biology
  description: The appended definition makes a cross-taxon molecular inventory and
    microbial-killing claim under a GO definition source that specifies only enclosed
    volume. The cited primary study directly resolves Dictyostelium trafficking and
    constituent profiles, not the entire stated enzymatic/ROS program across all named
    lineages.
  target_ids:
  - GO:0106174
  field_paths:
  - definition
  - definition_source
  evidence_ids:
  - septin-record-phagolysosome_vesicle_lumen
  - septin-go
  - septin-gotthardt2002-unige-pdf
  - septin-PMID12388753
  - septin-original-phagolysosome_vesicle_lumen
  - septin-curation-policy
  - septin-graph-policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/phagolysosome_vesicle_lumen.yaml
    role: maintained scientific record
  rule_id: Source-specific support and molecular/structural grounding contract
  native_severity: major
  normalization_reason: This is a material defining-function and biological-scope
    extension, not merely a missing citation; the exact lumen identity remains correct.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T032300Z-phagolysosome-vesicle-lumen-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2777
- finding_id: septin-phagolysosome_vesicle_lumen-F2
  issue_key: phagolysosome-vesicle-lumen-graph-scope
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Align graph scope with its descriptive edges
  description: 'The MECHANISTIC scope and assembly/functional-mechanism title overstate
    the two descriptive edges: parthood and whole-volume association with acidification.
    No proton transport or other explanatory transition is represented.'
  target_ids:
  - GO:0106174
  field_paths:
  - causal_graphs[0].scope_status
  - causal_graphs[0].title
  - causal_graphs[0].description
  evidence_ids:
  - septin-record-phagolysosome_vesicle_lumen
  - septin-go
  - septin-gotthardt2002-unige-pdf
  - septin-PMID12388753
  - septin-original-phagolysosome_vesicle_lumen
  - septin-curation-policy
  - septin-graph-policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/phagolysosome_vesicle_lumen.yaml
    role: maintained scientific record
  rule_id: Source-specific support and molecular/structural grounding contract
  native_severity: minor
  normalization_reason: The underlying identities and broad process association are
    retained; the bounded problem is the graph scope promise.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T032300Z-phagolysosome-vesicle-lumen-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2778
- finding_id: septin-phagolysosome_vesicle_lumen-F3
  issue_key: phagolysosome-vesicle-lumen-acidification-source-scope
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Qualify the acidification assay attribution
  description: The canonical example and function evidence note blend directly dissected
    membrane/luminal trafficking phases with acidification behavior. Gotthardt2002
    discusses acidification from prior work rather than presenting a direct luminal-pH
    assay in its Methods/Results.
  target_ids:
  - GO:0106174
  field_paths:
  - canonical_examples[0].note
  - functions[0].evidence[1].notes
  evidence_ids:
  - septin-record-phagolysosome_vesicle_lumen
  - septin-go
  - septin-gotthardt2002-unige-pdf
  - septin-PMID12388753
  - septin-original-phagolysosome_vesicle_lumen
  - septin-curation-policy
  - septin-graph-policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/phagolysosome_vesicle_lumen.yaml
    role: maintained scientific record
  rule_id: Source-specific support and molecular/structural grounding contract
  native_severity: minor
  normalization_reason: This is bounded experimental-source precision independent
    of the broader definition problem; qualitative acidification remains supported.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T032300Z-phagolysosome-vesicle-lumen-audit
    finding_id: F3
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2779
- finding_id: septin-plasma_membrane_derived_thylakoid_lumen-F1
  issue_key: plasma-membrane-derived-thylakoid-lumen-1
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Correct the experimental organism attributed to the thylakoid studies
  description: The cited Huokko2021 de novo-thylakoid study is assigned to Synechocystis
    PCC6803. The inspected primary Methods/Results identify Synechococcus elongatus
    PCC7942. These are distinct genera and taxon nodes. Correct the experiment/example
    and the explicit source notes together; do not change separately supported Synechocystis
    protein examples or imply that PCC6803 lacks thylakoids.
  target_ids:
  - GO:0031979
  field_paths:
  - canonical_examples[0]
  - evidence[6].notes
  evidence_ids:
  - septin-record-plasma_membrane_derived_thylakoid_lumen
  - septin-go
  - septin-huokko2021-jats
  - septin-casella2017-jats
  - septin-perez2024-delivered
  - septin-original-plasma_membrane_derived_thylakoid_lumen
  - septin-curation-policy
  - septin-graph-policy
  - septin-tax1140
  - septin-tax1148
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/plasma_membrane_derived_thylakoid_lumen.yaml
    role: maintained scientific record
  rule_id: Exact source identity, claim scope and grounded constituent identity
  native_severity: major
  normalization_reason: The experiment is concretely transferred between distinct
    organisms, materially changing provenance and the canonical biological example.
    This exceeds a spelling or historical-title defect, although the broad membrane/lumen
    identity remains valid.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T032302Z-plasma-membrane-derived-thylakoid-lumen-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2780
- finding_id: septin-plasma_membrane_derived_thylakoid_membrane-F1
  issue_key: plasma-membrane-derived-thylakoid-membrane-1
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Correct the experimental organism attributed to the thylakoid studies
  description: The cited Huokko2021 de novo-thylakoid study and Casella2017 mapping/FRAP
    notes is assigned to Synechocystis PCC6803. The inspected primary Methods/Results
    identify Synechococcus elongatus PCC7942. These are distinct genera and taxon
    nodes. Correct the experiment/example and the explicit source notes together;
    do not change separately supported Synechocystis protein examples or imply that
    PCC6803 lacks thylakoids.
  target_ids:
  - GO:0031676
  field_paths:
  - canonical_examples[0]
  - components[3].evidence[1].notes
  - causal_graphs[0].edges[1].evidence[0].notes
  - causal_graphs[0].edges[3].evidence[0].notes
  evidence_ids:
  - septin-record-plasma_membrane_derived_thylakoid_membrane
  - septin-go
  - septin-huokko2021-jats
  - septin-casella2017-jats
  - septin-perez2024-delivered
  - septin-original-plasma_membrane_derived_thylakoid_membrane
  - septin-curation-policy
  - septin-graph-policy
  - septin-tax1140
  - septin-tax1148
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/plasma_membrane_derived_thylakoid_membrane.yaml
    role: maintained scientific record
  rule_id: Exact source identity, claim scope and grounded constituent identity
  native_severity: major
  normalization_reason: The experiment is concretely transferred between distinct
    organisms, materially changing provenance and the canonical biological example.
    This exceeds a spelling or historical-title defect, although the broad membrane/lumen
    identity remains valid.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T032303Z-plasma-membrane-derived-thylakoid-membrane-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2781
- finding_id: plaque-t1-F1
  issue_key: photosynthetic-membrane-1
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Correct the experimental organism attributed to the thylakoid studies
  description: The cited Casella2017 native-architecture/FRAP study is assigned to
    Synechocystis PCC6803. The inspected primary Methods/Results identify Synechococcus
    elongatus PCC7942. These are distinct genera and taxon nodes. Correct the experiment/example
    and the explicit source notes together; do not change separately supported Synechocystis
    protein examples or imply that PCC6803 lacks thylakoids.
  target_ids:
  - GO:0034357
  field_paths:
  - canonical_examples[0]
  - causal_graphs[0].edges[2].evidence[1].notes
  evidence_ids:
  - plaque-current-1
  - plaque-original-1
  - plaque-casella2017-jats
  - plaque-tax1148
  - plaque-tax1140
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/photosynthetic_membrane.yaml
    role: maintained scientific record
  rule_id: Exact source identity, claim scope and grounded constituent identity
  native_severity: major
  normalization_reason: The experiment is concretely transferred between distinct
    organisms, materially changing provenance and the canonical biological example.
    This exceeds a spelling or historical-title defect, although the broad membrane/lumen
    identity remains valid.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T032301Z-photosynthetic-membrane-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2782
- finding_id: plaque-t1-F2
  issue_key: photosynthetic-membrane-2
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Qualify the oxygenic scope of the GO-grounded light-reaction function
  description: GO0019684 explicitly defines oxygenic PSI/PSII light reactions involving
    water oxidation and NADP reduction. The function description is broad and its
    evidence combines an oxygenic thylakoid review with anoxygenic purple-bacterial
    architecture, without stating that the GO-grounded function applies to the oxygenic
    subset. Preserve the broad membrane class but delimit the GO claim and move the
    purple-specific support to the broader electron-transport/energy-conversion account.
  target_ids:
  - GO:0034357
  field_paths:
  - functions[1].grounding
  - functions[1].description
  - functions[1].evidence[1]
  evidence_ids:
  - plaque-current-1
  - plaque-original-1
  - plaque-go
  - plaque-perez2024-delivered
  - plaque-bahatyrova2004-pdf
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/photosynthetic_membrane.yaml
    role: maintained scientific record
  rule_id: Exact source identity, claim scope and grounded constituent identity
  native_severity: minor
  normalization_reason: The generic structure can legitimately have an oxygenic-subset
    function. The bounded defect is ambiguous scope and evidence placement under a
    narrower process term, not rejection of purple photochemistry or of the membrane
    identity.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T032301Z-photosynthetic-membrane-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2783
- finding_id: plaque-t2-F1
  issue_key: plasma-membrane-derived-chromatophore-membrane-1
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground the two existing complexes with verified whole-complex identifiers
  description: The existing LH2 constituent remains REVIEWED_LABEL_ONLY while the
    frozen maintained record cellstructuremech:lh2_peripheral_light_harvesting_antenna_complex
    supplies the exact whole-complex identity in the same chromatophore context. The
    existing F0F1 constituent also remains label-only solely pending a chromatophore-localized
    accession, although active GO0045259 exactly names the F1-F0 ATP synthase complex;
    location belongs in its role/context. This is a bounded gap in two already asserted
    constituents, not a demand for an optional new inventory or a claim that the historical
    pass had access to future records.
  target_ids:
  - GO:0042717
  field_paths:
  - components[2].grounding_status
  - components[2].grounding_notes
  - components[4].grounding_status
  - components[4].grounding_notes
  - discussions[1]
  evidence_ids:
  - plaque-current-2
  - plaque-original-2
  - plaque-go
  - plaque-context-lh2_peripheral_light_harvesting_antenna_complex
  - plaque-SL0042
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/plasma_membrane_derived_chromatophore_membrane.yaml
    role: maintained scientific record
  rule_id: Exact source identity, claim scope and grounded constituent identity
  native_severity: minor
  normalization_reason: Both constituents are already correctly described and supported;
    the available exact mappings improve interoperability without changing biology.
    A localization-specific new term is not required for the already named whole-complex
    identity.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T032301Z-plasma-membrane-derived-chromatophore-membrane-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2784
- finding_id: micro-F1
  issue_key: plastid-lipid-whole-membrane-grounding
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Separate membrane structures from molecular lipid grounding
  description: The maintained LIPID component row uses GO0042170 for the complete
    generic plastid membrane class. These are structural cellular-component identities,
    not the molecular lipid material identity required by the declared component type.
    Linked graph component_ref fields perpetuate that typing mismatch even though
    the structural nodes and topology are sound.
  target_ids:
  - GO:0009536
  field_paths:
  - components[0].component_type
  - components[0].grounding
  - causal_graphs[0].nodes[1].component_ref
  evidence_ids:
  - micro-record-plastid
  - micro-prior-plastid
  - micro-go
  - micro-component-policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/plastid.yaml
    role: maintained scientific record
  rule_id: Source-specific support and molecular/structural grounding contract
  native_severity: major
  normalization_reason: This materially misrepresents the component category/grounding
    and contaminates its graph association; it is not merely an optional missing lipid
    identifier or an argument against valid structural parthood.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T032303Z-plastid-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2775
- finding_id: micro-F2
  issue_key: plastid-envelope-lipid-whole-membrane-grounding
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Separate membrane structures from molecular lipid grounding
  description: The maintained LIPID component rows use GO0009527 and GO0009528 for
    complete outer and inner membranes. These are structural cellular-component identities,
    not the molecular lipid material identity required by the declared component type.
    Linked graph component_ref fields perpetuate that typing mismatch even though
    the structural nodes and topology are sound.
  target_ids:
  - GO:0009526
  field_paths:
  - components[0].component_type
  - components[0].grounding
  - components[1].component_type
  - components[1].grounding
  - causal_graphs[0].nodes[2].component_ref
  - causal_graphs[0].nodes[3].component_ref
  evidence_ids:
  - micro-record-plastid_envelope
  - micro-prior-plastid_envelope
  - micro-go
  - micro-component-policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/plastid_envelope.yaml
    role: maintained scientific record
  rule_id: Source-specific support and molecular/structural grounding contract
  native_severity: major
  normalization_reason: This materially misrepresents the component category/grounding
    and contaminates its graph association; it is not merely an optional missing lipid
    identifier or an argument against valid structural parthood.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T032304Z-plastid-envelope-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2776
actions:
- action_id: septin-phagolysosome_vesicle_lumen-A1
  finding_ids:
  - septin-phagolysosome_vesicle_lumen-F1
  target_ids:
  - GO:0106174
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/phagolysosome_vesicle_lumen.yaml
    role: maintained scientific record
  description: Retain the ontology volume definition and place supported extra biology
    in source-, taxon- and stage-qualified fields, or provide directly inspected evidence
    for each retained extension.
  acceptance_checks:
  - Ontology text and added interpretation are distinguished.
  - No complete cross-taxon digestive program is inferred solely from Dictyostelium
    time profiles.
  - Correct lumen hierarchy and supported maturation are preserved.
  - Native schema, strict, identifier, graph and history checks pass after separately
    authorized curation.
- action_id: septin-phagolysosome_vesicle_lumen-A2
  finding_ids:
  - septin-phagolysosome_vesicle_lumen-F2
  target_ids:
  - GO:0106174
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/phagolysosome_vesicle_lumen.yaml
    role: maintained scientific record
  description: Use NONMECHANISTIC with a precise scope note and title, or separately
    curate a source-backed mechanistic path.
  acceptance_checks:
  - Scope and title match actual graph resolution.
  - No unsupported obligatory component is introduced to make the graph mechanistic.
  - Native schema, strict, identifier, graph and history checks pass after separately
    authorized curation.
- action_id: septin-phagolysosome_vesicle_lumen-A3
  finding_ids:
  - septin-phagolysosome_vesicle_lumen-F3
  target_ids:
  - GO:0106174
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/phagolysosome_vesicle_lumen.yaml
    role: maintained scientific record
  description: Distinguish measured trafficking profiles from acidification context
    synthesized from earlier studies, or cite inspected direct pH evidence.
  acceptance_checks:
  - The note accurately identifies which measurements the cited study performed.
  - Supported qualitative maturation and acidification are retained.
  - Native schema, strict, identifier, graph and history checks pass after separately
    authorized curation.
- action_id: septin-plasma_membrane_derived_thylakoid_lumen-A1
  finding_ids:
  - septin-plasma_membrane_derived_thylakoid_lumen-F1
  target_ids:
  - GO:0031979
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/plasma_membrane_derived_thylakoid_lumen.yaml
    role: maintained scientific record
  description: In separately authorized curation, use Synechococcus elongatus PCC7942
    for these exact studies and verify the taxon pairing, or supply a genuinely matching
    PCC6803 study for a retained PCC6803 example; align every explicit source note.
  acceptance_checks:
  - Each changed field matches the exact source organism, process or whole-complex
    identity.
  - Correct structure boundaries, protein identities and original history remain intact.
  - Native schema, strict, CURIE, graph and history gates pass.
- action_id: septin-plasma_membrane_derived_thylakoid_membrane-A1
  finding_ids:
  - septin-plasma_membrane_derived_thylakoid_membrane-F1
  target_ids:
  - GO:0031676
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/plasma_membrane_derived_thylakoid_membrane.yaml
    role: maintained scientific record
  description: In separately authorized curation, use Synechococcus elongatus PCC7942
    for these exact studies and verify the taxon pairing, or supply a genuinely matching
    PCC6803 study for a retained PCC6803 example; align every explicit source note.
  acceptance_checks:
  - Each changed field matches the exact source organism, process or whole-complex
    identity.
  - Correct structure boundaries, protein identities and original history remain intact.
  - Native schema, strict, CURIE, graph and history gates pass.
- action_id: plaque-t1-A1
  finding_ids:
  - plaque-t1-F1
  target_ids:
  - GO:0034357
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/photosynthetic_membrane.yaml
    role: maintained scientific record
  description: In separately authorized curation, use Synechococcus elongatus PCC7942
    for these exact studies and verify the taxon pairing, or supply a genuinely matching
    PCC6803 study for a retained PCC6803 example; align every explicit source note.
  acceptance_checks:
  - Each changed field matches the exact source organism, process or whole-complex
    identity.
  - Correct structure boundaries, protein identities and original history remain intact.
  - Native schema, strict, CURIE, graph and history gates pass.
  - Preserve append-only historical rationale/events; amend current fields or append
    a scoped resolution. Do not resolve unrelated category or neighbor findings.
- action_id: plaque-t1-A2
  finding_ids:
  - plaque-t1-F2
  target_ids:
  - GO:0034357
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/photosynthetic_membrane.yaml
    role: maintained scientific record
  description: In separately authorized curation, state explicitly that GO0019684
    applies to the oxygenic subset and attach only matching support there; retain
    purple photochemistry under the already broader function or another exactly verified
    process.
  acceptance_checks:
  - Each changed field matches the exact source organism, process or whole-complex
    identity.
  - Correct structure boundaries, protein identities and original history remain intact.
  - Native schema, strict, CURIE, graph and history gates pass.
  - Preserve append-only historical rationale/events; amend current fields or append
    a scoped resolution. Do not resolve unrelated category or neighbor findings.
- action_id: plaque-t2-A1
  finding_ids:
  - plaque-t2-F1
  target_ids:
  - GO:0042717
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/plasma_membrane_derived_chromatophore_membrane.yaml
    role: maintained scientific record
  description: In separately authorized curation, ground LH2 to the exact maintained
    local complex and F0F1 to GO0045259, retain source-specific localization and UNKNOWN
    formation necessity, and resolve the current grounding task without rewriting
    historical events.
  acceptance_checks:
  - Each changed field matches the exact source organism, process or whole-complex
    identity.
  - Correct structure boundaries, protein identities and original history remain intact.
  - Native schema, strict, CURIE, graph and history gates pass.
  - Preserve append-only historical rationale/events; amend current fields or append
    a scoped resolution. Do not resolve unrelated category or neighbor findings.
- action_id: micro-A1
  finding_ids:
  - micro-F1
  target_ids:
  - GO:0009536
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/plastid.yaml
    role: maintained scientific record
  description: Keep correct GO membrane entities as structural nodes/parts. If the
    rows mean collective lipid material, relabel and use honest reviewed-label-only
    grounding pending a justified chemical identifier; if they mean structural subparts,
    represent them with an appropriate explicit structural type rather than LIPID.
    Align component_ref links with the chosen model.
  acceptance_checks:
  - No LIPID molecular row uses a complete membrane GO identity as its chemical grounding.
  - Valid membrane identities, has_part topology and boundaries remain intact.
  - No specific lipid species or obligatory protein inventory is invented.
  - Native schema, strict, identifier, graph and history checks pass after separately
    authorized curation.
- action_id: micro-A2
  finding_ids:
  - micro-F2
  target_ids:
  - GO:0009526
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/plastid_envelope.yaml
    role: maintained scientific record
  description: Keep correct GO membrane entities as structural nodes/parts. If the
    rows mean collective lipid material, relabel and use honest reviewed-label-only
    grounding pending a justified chemical identifier; if they mean structural subparts,
    represent them with an appropriate explicit structural type rather than LIPID.
    Align component_ref links with the chosen model.
  acceptance_checks:
  - No LIPID molecular row uses a complete membrane GO identity as its chemical grounding.
  - Valid membrane identities, has_part topology and boundaries remain intact.
  - No specific lipid species or obligatory protein inventory is invented.
  - Native schema, strict, identifier, graph and history checks pass after separately
    authorized curation.
limitations:
- 'Phagolysosome lumen and bacterial thylakoid compartments independent subreview:
  Independent read-only review of three assigned targets. Five inherited scientific
  findings remain open:3major2minor. No new scientific finding or rejected predecessor;
  all three verdicts need curation. One assigned target is stale and substantively
  refreshed, while its old graph-inventory misdescription is separately corrected
  in review scope. No maintained records changed.'
- 'Phagolysosome lumen and bacterial thylakoid compartments independent subreview:
  Current ontology/SL/taxonomy/catalogue and bounded matched-host HTTP queries are
  fresh. Gotthardt2002 PDF/metadata are cached from PR2374 with exact original access
  times and byte hashes; current reread is explicitly bounded. Casella/Huokko fresh
  collaborating-source snapshots were independently read at the stated sections and
  retain actual fetch times.'
- 'Phagolysosome lumen and bacterial thylakoid compartments independent subreview:
  Casella Results2.1–2.3/Methods4.1/4.8, Fig1–5 text captions and Table1 text were
  read. Huokko ResultsSec3/4 and MethodsSec9/12/13 plus Fig1/2 captions were read.
  No image pixels, supplemental tables/movies or raw quantitative reanalysis. AFM
  b6f identification remains tentative; no source-condition generalization to all
  hosts.'
- 'Phagolysosome lumen and bacterial thylakoid compartments independent subreview:
  Perez2024 is a secondary review. Actual publisher-delivered body Introduction/Lipids/ETC
  sections and text captions support qualitative mechanism/residence; initial landing/loading
  page alone did not. No exact universal lipid percentages, necessity claims or cited
  reference-body audit is inferred.'
- 'Phagolysosome lumen and bacterial thylakoid compartments independent subreview:
  Gotthardt2002 original main body pp3508–3518 was inspected previously; Methods pp3509–3510
  and Discussion/Fig7 pp3517–3518 were reread now. Trafficking/composition experiments
  are distinguished from prior-work acidification discussion and from the expanded
  cross-taxon enzymatic/ROS definition.'
- 'Phagolysosome lumen and bacterial thylakoid compartments independent subreview:
  Catalogue has matched PCC7942 scope, not Synechocystis6803 or Dictyostelium/Entamoeba/ciliate
  hosts. Four bounded searches, four selected gene identities/57-row association responses
  and module1/38 structured data are contextual. Generated AI prose, expression matrices
  and conditions were not assessed. All-false threshold flags do not mean biological
  absence or failed localization; no unmatched organism proxy is used.'
- 'Phagolysosome lumen and bacterial thylakoid compartments independent subreview:
  Historical runner PermissionError at00:49Z is retained only as historical availability
  evidence. Actual six native protein checks pass on independently confirmed0 examples/0
  typed nodes/0 UniProtKB graph xrefs. Existing GO complexes/STRUCTURE nodes remain
  molecular assertions; empty native scope does not certify completeness.'
- 'Phagolysosome lumen and bacterial thylakoid compartments independent subreview:
  All30 actually used repository inputs were frozen before reading:17 common policy/schema/script
  inputs,3 targets,6 originals and4 bounded anatomy neighbors. No whole-neighbor verdict,
  rationale rewrite, grouped-issue resolution, future saved-head/CI/merge certification
  or record mutation is claimed.'
- 'Photosynthetic and bacterial chromatophore membranes independent subreview: Both
  assigned records still need curation for three inherited findings: one major source-organism
  attribution, one minor oxygenic-function scope and one minor existing-complex grounding.
  No newly confirmed scientific finding. Stale chromatophore is refreshable entirely
  in review-bundle scope; no record changes.'
- 'Photosynthetic and bacterial chromatophore membranes independent subreview: Both
  original native pairs validate/render byte-for-byte;20 historical inputs each match
  originalsource. Photosynthetic target unchanged; chromatophore adds coherent currentgroundings/retypings/twoedges
  and is substantively refreshed. Historical graph/protein counts are not current
  counts. No category-wide#2432 resolution inferred.'
- 'Photosynthetic and bacterial chromatophore membranes independent subreview: Fresh
  native GO,SL,taxon and14accession responses plus bounded reviewedgene searches verify
  identities/aliases/loci/status. P16033 includes two psbA loci. Nativeannotation
  inference/experimental citations are distinct; InterPro cross-references are not
  independently expanded family-page assertions or whole-complex groundings.'
- 'Photosynthetic and bacterial chromatophore membranes independent subreview: Casella
  genuineJATS onlyResults2.1–2.4/captions andMethods4.1/4.5/4.7/4.8 read. PCC7942
  notPCC6803; no pixels,supplements,rawdata or completeothersections audit. Huokko
  was fetched/shared but not relied on for this assigned current assessment.'
- 'Photosynthetic and bacterial chromatophore membranes independent subreview: Bahatyrova
  genuinePDF scientificpp1058–1061/Methods/captions read; no pixels/supplements. NativeNCIB8253
  isolatedmembranes have preparation-specific architecture; AFM did not localizebc1/ATPase
  or directlyresolvePufX. Feniouk genuinePDF scientificpp1115–1121/Methods/Results/Discussion/captions
  read; R.capsulatusB10 electrochromic/inhibitor coupling, not a newly audited directATP-product
  experiment.'
- 'Photosynthetic and bacterial chromatophore membranes independent subreview: Comayras
  public author-upload browser excerpts only0–1241 with overlappingcaptures; no fullbody/pixels
  or nativeHTTPsuccess claim. Ga-strain quinone-pool assay suppressesbc1 and gradients;
  context doesnot establish unperturbed cyclicPMF measurement. Initial ScienceDirect
  access403 and DOI-query failure are access/search limits, not scientific refutations.'
- 'Photosynthetic and bacterial chromatophore membranes independent subreview: Perez
  is SECONDARY REVIEW body, not primaryexperiment: inspectedIntroduction/evolutionaryoverview/BuildingBlocks/Lipids/ETC
  andembeddedFig1/2captions only. Sui secondaryabstract andNielsen primaryabstract
  only. Five PCC6803 annotation-linked primaryabstracts inspected; their full bodies/pixels
  not claimed.'
- 'Photosynthetic and bacterial chromatophore membranes independent subreview: Same-PR
  shared source receipts retain actual20:00–20:02Zfetch dates andhashes; independently
  reread, not represented as fresh requests. Bothtargets lack maintainedimages/quantitativephysicalproperties/directquotes;
  no pixel or rawquantitative reanalysis claimed.'
- 'Photosynthetic and bacterial chromatophore membranes independent subreview: Actual
  native checks cover8reviewedexamples/2COVEREDnodes forphotosynthetic and6reviewedexamples/0GENE_OR_PROTEINnodes
  forchromatophore. Zero typednodes is not an emptyprotein inventory. Enum permits
  complexes/families, so no automatic oldtyping defect.'
- 'Photosynthetic and bacterial chromatophore membranes independent subreview: Both
  actual protein/pathway narratives trigger applicability. Catalogue hasPCC7942matchedsourcecontext,
  noPCC6803 orpurplehost. Bounded4queries/selected4genes/module1and38 independently
  reread. Belowthreshold is not absence; activity arrays notcondition-analyzed andAIgeneratedprose
  excluded. Historical00:49Zrunner remains unavailable; no newrunnerinvocation claimed.'
- 'Photosynthetic and bacterial chromatophore membranes independent subreview: Three
  frozenenergycomplexneighbors used only for exact identity/definition/taxon/function/source
  andnodeinventory context; no complete neighbor scientificreview or issueclosure.
  No additionallocalinputs used beforefreeze. Root owns current globalQC,issues,persistence,CI/queue/merge;
  thissource report doesnot certify futuregates.'
- 'Five plastid compartment records independent subreview: Five unchanged complete
  records independently reviewed: two inherited major whole-membrane LIPID findings
  preserve exact predecessor/action; three other targets remain qualified. Three unsupported
  explicit adapter exclusions corrected in assessment; two genuine physical exclusions
  preserved. No new scientific finding.'
- 'Five plastid compartment records independent subreview: Fresh current GO/SL/taxonomy/catalogue
  and exact literature metadata are distinct from retained genuine Keeling HTML10:10:38.582642Z
  and Terashima PDF10:10:38.518294Z. Retained source bytes/hash verified and declared
  sections independently reread now; not new fetches.'
- 'Five plastid compartment records independent subreview: Keeling secondary review
  read complete s1/s3/s6/s9 with embedded Figures1–3 captions only. Old chromalveolate
  models, universal mitochondrial-loss statements, numerical species estimates and
  underlying cited primary studies are not adopted or independently audited. No source
  pixels/supplements.'
- 'Five plastid compartment records independent subreview: Terashima secondary PDF
  title/abstract/Introduction and initial proteome discussion onpp151–152 read. No
  later sections/protein tables/supplements/pixels audited; fraction contamination/compiled
  candidates are not treated as a generic membrane molecular inventory.'
- 'Five plastid compartment records independent subreview: Jin2022 primary access
  is complete abstract, indexed C.reinhardtii keyword and bibliographic/publisher
  metadata only. PublisherXML returns coredata, not article body; PDF route403. No
  exact strain, full Methods/coordinate model/pixels/functional deletion experiments
  certified. Access limits are not refutations.'
- 'Five plastid compartment records independent subreview: Five records have zero
  protein_examples and zero typed molecular nodes; current native passes do not imply
  complete protein-family coverage. Three positiveTOC–TIC narrative claims trigger
  adapter coverage despite empty graph; whole/generic model-use context does not assert
  a specified pathway.'
- 'Five plastid compartment records independent subreview: Fresh full20-organism/28-pair
  official catalogue has no matching Chlamydomonas/green-algal host. No unmatched
  cyanobacterial proxy/downstream module query; noncoverage is not negative biology.
  Historical00:49Z runner failure remains historical unavailable, not rerun.'
- 'Five plastid compartment records independent subreview: GO generic membrane definition
  focuses on envelope while explicit child hierarchy includes thylakoid/cyanelle/apicoplast
  membranes; class evidence supports this broader fallback without inventing a direct
  GO relation. Two frozen neighbors are boundary context only; their issues/verdicts
  are not adjudicated.'
- 'Five plastid compartment records independent subreview: No records/originals/history/generated
  files/Git/GitHub changed; root owns current global gates,issue dedup/publication/successor
  and later CI/queue/merge. This report does not precertify future results.'
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
- 'All ten original YAML/Markdown pairs remain unchanged. Current main was merged
  normally and pushed without force. Two original target hashes differ: plasma-membrane-derived
  chromatophore membrane and thylakoid membrane. Their changed claims are substantively
  reassessed; the other eight inputs still match.'
- This explicit issue-bearing ten-record cohort follows native persistence policy.
  Inherited scientific findings retain stable keys and exact predecessor repository/review/finding
  identities; any newly observed finding has no invented predecessor.
- Issue2773 tracks the two stale reviews and the original thylakoid assessment that
  prematurely described ATP-synthase residence among the old five edges. The successor
  distinguishes historical assessment error from the newly present node/edge instead
  of claiming the original review saw future content.
- 'Issue2774 tracks eight unsupported source-applicability exclusions: four prose
  notes without a formal check (photosynthetic membrane, bacterial chromatophore membrane,
  bacterial thylakoid lumen/membrane) and four explicit check rows (phagolysosome
  lumen, plastid envelope, inner membrane and IMS). Whole plastid and generic plastid
  membrane retain genuine material/topology exclusions.'
- Source commit659d5d9ce7e16c8607002bf1655db2f3c652e6e1 is retained by tag review-base/pr2375-current-record-followup-20261103.
- CLAUDE.md aliases AGENTS.md; canonical regular AGENTS.md bytes are frozen. All used
  local policy, schema, verifier, original artifacts and boundary/complex context
  inputs are frozen before assessment.
- Chromatophore newly propagated node groundings concern RC-LH1-PufX and bc1, not
  the separate original LH2/F0F1 component-grounding finding. Closed issue2432 is
  narrow historical propagation context, not proof of broader issue resolution.
- Fresh and retained literature snapshots preserve their actual access times and declared
  body/abstract/pixel limits. Identity and family/domain checks are distinct from
  experimental structure membership, strain provenance or assembly necessity.
- All twenty native protein commands passed. Photosynthetic membrane has eight reviewed
  examples and two COVERED typed nodes; bacterial chromatophore membrane has six reviewed
  examples and zero current GENE_OR_PROTEIN nodes after complex-node retyping. The
  other eight records have zero examples and zero typed molecular nodes. Positive
  narrative pathway claims still require applicability assessment.
- Native CausalNode schema permits families and complexes as GENE_OR_PROTEIN. Subsequent
  STRUCTURE retyping alone is not evidence that original generic typing was invalid.
  Source-neutral group/complex grounding questions are not automatically resolved
  by taxon-specific subunit accessions.
- Five related open issue matches concern different maintained records; no same-record/finding
  duplicate was found. Validator2514 remains reused and open. No scientific records,
  historical discussions or resolver are edited.
- Final trusted-base review-check, exact-head independent acceptance, final-head CI
  and merge-group CI occur after this immutable observation and are not represented
  as already complete.
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T032300Z-phagolysosome-vesicle-lumen-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T032301Z-photosynthetic-membrane-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T032301Z-plasma-membrane-derived-chromatophore-membrane-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T032302Z-plasma-membrane-derived-thylakoid-lumen-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T032303Z-plasma-membrane-derived-thylakoid-membrane-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T032303Z-plastid-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T032304Z-plastid-envelope-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T032305Z-plastid-inner-membrane-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T032305Z-plastid-intermembrane-space-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T032306Z-plastid-membrane-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
links:
- https://github.com/CultureBotAI/CellStructureMech/pull/2375
- https://github.com/CultureBotAI/CellStructureMech/issues/2514
- https://github.com/CultureBotAI/CellStructureMech/issues/2773
- https://github.com/CultureBotAI/CellStructureMech/issues/2774
- https://github.com/CultureBotAI/CellStructureMech/issues/2775
- https://github.com/CultureBotAI/CellStructureMech/issues/2776
- https://github.com/CultureBotAI/CellStructureMech/issues/2777
- https://github.com/CultureBotAI/CellStructureMech/issues/2778
- https://github.com/CultureBotAI/CellStructureMech/issues/2779
- https://github.com/CultureBotAI/CellStructureMech/issues/2780
- https://github.com/CultureBotAI/CellStructureMech/issues/2781
- https://github.com/CultureBotAI/CellStructureMech/issues/2782
- https://github.com/CultureBotAI/CellStructureMech/issues/2783
- https://github.com/CultureBotAI/CellStructureMech/issues/2784
```
