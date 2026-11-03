# PR 2358: current-input review of ten records and adversarial follow-up

- Review: 20261103T094445Z-pr2358-current-record-followup
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-11-03T09:31:38.879464Z
- Finished UTC: 2026-11-03T09:44:45Z
- Reviewer: Codex root synthesis with three independent read-only adversarial reviewers (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Current-input reassessment of all ten records in PR2358. Two stale reviews are substantively refreshed. Independent source assessments retain the three inherited scientific findings and correct nine structured-source applicability assessments without editing records.

## Scope And Provenance

Exact ten-record PR cohort reassessed against current main 463315caf9231f00781fef74e7d9b8ef8c44a502. Changed inputs are substantively reassessed. Scientific records remain unchanged.

Selection: Complete cohort of ten maintained records reviewed in original PR head 998dda812da7bd6e3740c579ee8ff24669b62a9c.
Coverage: full; 10 reviewed / 10 in the declared population.
Source: working_tree at Git base e721920f30c72a6c35cecb9913c6780e18a460ed.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0160211 | data/structures/membrane_organelle/apicoplast_membrane.yaml | maintained | apicoplast membrane |
| GO:0005776 | data/structures/membrane_organelle/autophagosome.yaml | maintained | autophagosome |
| GO:0034423 | data/structures/membrane_organelle/autophagosome_lumen.yaml | maintained | autophagosome lumen |
| GO:0000421 | data/structures/membrane_organelle/autophagosome_membrane.yaml | maintained | autophagosome membrane |
| GO:0030075 | data/structures/membrane_organelle/bacterial_thylakoid.yaml | maintained | bacterial thylakoid |
| GO:0045009 | data/structures/membrane_organelle/chitosome.yaml | maintained | chitosome |
| GO:0009507 | data/structures/membrane_organelle/chloroplast.yaml | maintained | chloroplast |
| GO:0009941 | data/structures/membrane_organelle/chloroplast_envelope.yaml | maintained | chloroplast envelope |
| GO:0009706 | data/structures/membrane_organelle/chloroplast_inner_membrane.yaml | maintained | chloroplast inner membrane |
| GO:0031972 | data/structures/membrane_organelle/chloroplast_intermembrane_space.yaml | maintained | chloroplast intermembrane space |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full native QC | passed | True | GO:0160211, GO:0005776, GO:0034423, GO:0000421, GO:0030075, GO:0045009, GO:0009507, GO:0009941, GO:0009706, GO:0031972 | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| Native label correspondence | passed | True | GO:0160211, GO:0005776, GO:0034423, GO:0000421, GO:0030075, GO:0045009, GO:0009507, GO:0009941, GO:0009706, GO:0031972 | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| TraitMech references | passed | True | GO:0160211, GO:0005776, GO:0034423, GO:0000421, GO:0030075, GO:0045009, GO:0009507, GO:0009941, GO:0009706, GO:0031972 | Native TraitMech link check passed. |
| Pinned governed files | passed | True | GO:0160211, GO:0005776, GO:0034423, GO:0000421, GO:0030075, GO:0045009, GO:0009507, GO:0009941, GO:0009706, GO:0031972 | Pinned governed files match; native vendored check passed. |
| Native identifier resolver | passed | True | GO:0160211, GO:0005776, GO:0034423, GO:0000421, GO:0030075, GO:0045009, GO:0009507, GO:0009941, GO:0009706, GO:0031972 | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| validate GO:0160211 | passed | True | GO:0160211 | Documented focused command passed. |
| validate-strict GO:0160211 | passed | True | GO:0160211 | Documented focused command passed. |
| validate GO:0005776 | passed | True | GO:0005776 | Documented focused command passed. |
| validate-strict GO:0005776 | passed | True | GO:0005776 | Documented focused command passed. |
| validate GO:0034423 | passed | True | GO:0034423 | Documented focused command passed. |
| validate-strict GO:0034423 | passed | True | GO:0034423 | Documented focused command passed. |
| validate GO:0000421 | passed | True | GO:0000421 | Documented focused command passed. |
| validate-strict GO:0000421 | passed | True | GO:0000421 | Documented focused command passed. |
| validate GO:0030075 | passed | True | GO:0030075 | Documented focused command passed. |
| validate-strict GO:0030075 | passed | True | GO:0030075 | Documented focused command passed. |
| validate GO:0045009 | passed | True | GO:0045009 | Documented focused command passed. |
| validate-strict GO:0045009 | passed | True | GO:0045009 | Documented focused command passed. |
| validate GO:0009507 | passed | True | GO:0009507 | Documented focused command passed. |
| validate-strict GO:0009507 | passed | True | GO:0009507 | Documented focused command passed. |
| validate GO:0009941 | passed | True | GO:0009941 | Documented focused command passed. |
| validate-strict GO:0009941 | passed | True | GO:0009941 | Documented focused command passed. |
| validate GO:0009706 | passed | True | GO:0009706 | Documented focused command passed. |
| validate-strict GO:0009706 | passed | True | GO:0009706 | Documented focused command passed. |
| validate GO:0031972 | passed | True | GO:0031972 | Documented focused command passed. |
| validate-strict GO:0031972 | passed | True | GO:0031972 | Documented focused command passed. |
| Supplemental bounded PMID authority checks | passed | True | GO:0160211, GO:0005776, GO:0034423, GO:0000421, GO:0030075, GO:0045009, GO:0009507, GO:0009941, GO:0009706, GO:0031972 | 909 PMIDs all OK in bounded native requests; full-command limitations remain separate. |
| Official structured-source applicability and covered-dataset cross-checks | passed | False | GO:0160211, GO:0005776, GO:0034423, GO:0000421, GO:0030075, GO:0045009, GO:0009507, GO:0009941, GO:0009706, GO:0031972 | Nine applicability defects are corrected: three omissions (apicoplast membrane, bacterial thylakoid and chitosome), and six unsupported expression-only exclusions (autophagosome, autophagosome membrane, chloroplast, envelope, inner membrane and intermembrane space). Autophagosome lumen is a genuine sparse topology exclusion. Actual catalogue coverage, bounded molecular searches and experimental strain contexts are assessed separately. PCC7942 dataset context cannot support the maintained PCC6803 example or repair its curation finding. No covered fungal, apicomplexan or green-algal dataset is substituted with another organism. Resource noncoverage is not biological absence; retained historical runner failure is not a fresh invocation. |
| Independent claim-level source review | passed | True | GO:0160211, GO:0005776, GO:0034423, GO:0000421, GO:0030075, GO:0045009, GO:0009507, GO:0009941, GO:0009706, GO:0031972 | Three read-only reviewers covered the complete ten-record cohort, including changed inputs, with explicit scientific findings and source-access limits. Final artifact/head acceptance occurs after saving. |
| Retained historical adapter runner availability | unavailable | False | GO:0160211, GO:0005776, GO:0000421, GO:0030075, GO:0045009, GO:0009507, GO:0009941, GO:0009706, GO:0031972 | Historical 00:49Z invocation unavailable due to OS access restriction. Official catalogue source fallback was inspected separately; no current invocation or successful adapter execution is claimed. The actual historical exit code 1 is retained in the evidence receipt, since the native unavailable-check model has no execution exit-code field. |
| Native apicoplast membrane UniProt verify check | passed | True | GO:0160211 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native apicoplast membrane UniProt causal check | passed | True | GO:0160211 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native autophagosome UniProt verify check | passed | True | GO:0005776 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native autophagosome UniProt causal check | passed | True | GO:0005776 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native autophagosome lumen UniProt verify check | passed | True | GO:0034423 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native autophagosome lumen UniProt causal check | passed | True | GO:0034423 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native autophagosome membrane UniProt verify check | passed | True | GO:0000421 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native autophagosome membrane UniProt causal check | passed | True | GO:0000421 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native bacterial thylakoid UniProt verify check | passed | True | GO:0030075 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native bacterial thylakoid UniProt causal check | passed | True | GO:0030075 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native chitosome UniProt verify check | passed | True | GO:0045009 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native chitosome UniProt causal check | passed | True | GO:0045009 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native chloroplast UniProt verify check | passed | True | GO:0009507 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native chloroplast UniProt causal check | passed | True | GO:0009507 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native chloroplast envelope UniProt verify check | passed | True | GO:0009941 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native chloroplast envelope UniProt causal check | passed | True | GO:0009941 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native chloroplast inner membrane UniProt verify check | passed | True | GO:0009706 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native chloroplast inner membrane UniProt causal check | passed | True | GO:0009706 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native chloroplast intermembrane space UniProt verify check | passed | True | GO:0031972 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native chloroplast intermembrane space UniProt causal check | passed | True | GO:0031972 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories, zero molecular graph nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |

## Scientific And Domain Assessments

### Whole thylakoid identity and part boundaries

identity: supported. Targets: GO:0030075.

The exact GO identity, synonym, parent and four asserted parts are supported; OTHER follows the explicit GO comment that a thylakoid is not an organelle. The filesystem category does not redefine its kind. No local sibling record is used as scientific evidence.

### Collective bilayer and photosynthetic complex membership

evidence: supported. Targets: GO:0030075.

A membrane boundary is constitutional to this compartment, supporting ESSENTIAL at the collective bilayer level. The four known photosynthetic complexes are correctly represented by complex identifiers rather than forced single-protein families. Native authority and the primary assays establish broad membership; their incorrect organism attributions are separately addressed by F1.

### Individual molecular assembly requirements

evidence: unknown. Targets: GO:0030075.

The four complex rows correctly retain UNKNOWN. Membrane residence, photosynthetic function, changing abundance and the study of biogenesis do not alone establish which complex or individual lipid is necessary to form every bacterial thylakoid.

### Taxonomic distribution versus exact experimental model

scope: concern. Targets: GO:0030075.

Cyanobacterial COMMON presence with a named thylakoid-lacking exception is supported. Both source papers study Synechococcus elongatus PCC7942; the target transfers this work to Synechocystis PCC6803 and repeats Synechocystis in Casella evidence notes (F1). This is a source-organism mismatch, not evidence that Synechocystis lacks thylakoids.

### Both functions and all ten coarse graph edges

graph: supported. Targets: GO:0030075.

The membrane/lumen topology and PSII–quinone–b6f–PSI/ATP synthesis roles are supported at the declared NONMECHANISTIC scale. The b6f-to-PSI edge explicitly allows a downstream soluble carrier. No fixed stoichiometry, exhaustive respiratory inventory or direct b6f–PSI physical transfer is asserted. Correct the organism scope of the two Casella localization edges with F1.

### Ontology-derived attachment wording versus observed membrane development

evidence: unknown. Targets: GO:0030075.

The target reproduces current GO wording accurately. Huokko distinguishes proximity/thylapse-like contacts from direct membrane connection or fusion and leaves origin models unresolved. This review does not infer obligatory membrane continuity, universal plasma-membrane budding, or validated membrane tethers in every cyanobacterium from that wording.

### Evidence identity, discussion scope and bounded inventory

completeness: supported. Targets: GO:0030075.

All cited DOIs resolve to the intended works. The native ontology supports the resolved whole-compartment versus membrane and non-organelle decisions. The record has no image or protein-example assertions. Additional respiratory complexes, lipid species and detailed biogenesis machinery are not mandatory solely because the sources describe them. Historical notes remain historical.

### Native protein identity and graph coverage

schema: supported. Targets: GO:0030075.

Both actual checks exited0. These records have no protein examples and no GENE_OR_PROTEIN causal nodes; complex/structure or spatial nodes are not forced into individual protein coverage. Empty inventory does not prove molecular membership or assembly necessity.

### Frozen historical input and deterministic bundle validation

provenance: supported. Targets: GO:0030075.

Original YAML validates and exact native Markdown render agrees. Historical target hash and current hash match; no stale delta requires refresh. New assessments correct bundle applicability without rewriting originals or claiming scientific record edits.

### Photosynthetic pathways and bounded matched PCC7942 source context

scope: supported. Targets: GO:0030075.

The photosynthetic complexes/pathway trigger applicability. Fresh catalogue/meta identify PCC7942 elprecise300, matching the cited experimental context but not maintained PCC6803. Bounded searches and representative psaA/psbA1/petB/atpA membership checks plus module38/1 metadata/lists provide computational context only. Below-threshold psbA1/atpA results are not absence; generated summaries are excluded. The inherited organism mismatch remains open.

### Exact identity and adjacent structure boundaries

identity: supported. Targets: GO:0009706.

Native identifiers and source descriptions distinguish the complete organelle, its double-membrane envelope including the intervening space, individual inner bilayer, and enclosed intermembrane region. Asserted is_a parents and physical parts are coherent. The source-neutral GO definition is not silently expanded to make every plastid photosynthetic.

### Green lineage and model-organism context

scope: supported. Targets: GO:0009706.

Native taxonomy confirms Viridiplantae and C.reinhardtii. Keeling selected review text supports photosynthetic green-lineage plastids while acknowledging loss/nonphotosynthetic forms. Jin primary abstract supplies envelope-spanning TOC–TIC/IMS context; linked7VCF deposited entity metadata confirms species3055. No strain, quantitative prevalence or universal translocon composition is inferred.

### The collective bounding bilayer

grounding: supported. Targets: GO:0009706.

The component is the inner bilayer itself and its ESSENTIAL value is constitutional at that collective level. The label-only rationale correctly avoids using the whole location term as a chemical identifier for a particular lipid. The record does not assert one invariant lipid composition.

### Molecular assembly requirements are not supplied

evidence: unknown. Targets: GO:0009706.

Constitutional existence of a bilayer does not establish necessity of each lipid molecule or membrane protein. Those individual requirements remain unresolved, and the record does not import translocon perturbation claims as membrane-formation assays.

### Three descriptive membrane boundaries

graph: supported. Targets: GO:0009706.

The NONMECHANISTIC graph separates envelope parthood from the two spatial boundaries. Exact GO definitions and UniProtSL0051 support stroma-facing topology and separation from the intermembrane region. Lumen-facing in the GO definition means the organelle interior here; the maintained role/graph explicitly specifies stroma and does not confuse it with thylakoid lumen.

### Accurate citation identities and bounded access

provenance: supported. Targets: GO:0009706.

Citation identities match native bibliography. Keeling selected secondary body was accessible through PMC despite failed alternative routes. Jin biology remains primary-abstract scope with separate deposit organism metadata; publisher403 is not full-body access. Historical reviews/status are unchanged.

### Bounded record-level coverage

completeness: supported. Targets: GO:0009706.

The entire maintained record and cited claim contexts were inspected at the stated source scopes. Additional exhaustive component inventories, numerical properties, images, traits and expanded mechanisms are optional. No verbatim quotation requires repair, and no status or history rewrite is proposed. This bounded review does not assert exhaustive literature completeness.

### Native protein identity and graph coverage

schema: supported. Targets: GO:0009706.

Both actual checks exited0. These records have no protein examples and no GENE_OR_PROTEIN causal nodes; complex/structure or spatial nodes are not forced into individual protein coverage. Empty inventory does not prove molecular membership or assembly necessity.

### Frozen historical input and deterministic bundle validation

provenance: supported. Targets: GO:0009706.

Original YAML validates and exact native Markdown render agrees. Historical target hash and current hash match; no stale delta requires refresh. New assessments correct bundle applicability without rewriting originals or claiming scientific record edits.

### TOC–TIC prose triggers real covered-organism assessment

scope: supported. Targets: GO:0009706.

Although the inventory is sparse, taxon/example prose explicitly names the TOC–TIC protein-import pathway. It triggers applicability independently of transcriptomics claims. The fresh full catalogue has no Chlamydomonas dataset or matching green-lineage host; downstream modules from cyanobacteria cannot validate chloroplast import. Current bounded outcome is no matching dataset, not a no-expression exemption. Historical runner failure remains separately dated.

### Exact identity and adjacent structure boundaries

identity: supported. Targets: GO:0031972.

Native identifiers and source descriptions distinguish the complete organelle, its double-membrane envelope including the intervening space, individual inner bilayer, and enclosed intermembrane region. Asserted is_a parents and physical parts are coherent. The source-neutral GO definition is not silently expanded to make every plastid photosynthetic.

### Green lineage and model-organism context

scope: supported. Targets: GO:0031972.

Native taxonomy confirms Viridiplantae and C.reinhardtii. Keeling selected review text supports photosynthetic green-lineage plastids while acknowledging loss/nonphotosynthetic forms. Jin primary abstract supplies envelope-spanning TOC–TIC/IMS context; linked7VCF deposited entity metadata confirms species3055. No strain, quantitative prevalence or universal translocon composition is inferred.

### A spatial region with no asserted fixed molecular inventory

completeness: supported. Targets: GO:0031972.

This record denotes the volume between bilayers. Omitting a molecular component list is appropriate: the IMS scaffold described by Jin is part of an import complex, not a universal material identity of the entire region. No optional inventory or protein example is required to make the topology record complete at its stated scope.

### No molecular assembly dependency is encoded

evidence: unknown. Targets: GO:0031972.

The target has no component essentiality assertions. Defining a region between membranes does not identify a particular molecule as necessary for its formation.

### Two spatial delimitation edges

graph: supported. Targets: GO:0031972.

Both NONMECHANISTIC edges identify the outer and inner bilayers as the two boundaries. Native GO and UniProt definitions support this topology. The exact synonym, plastid-intermembrane is_a parent and chloroplast-envelope part_of relation are separately verified.

### Accurate citation identities and bounded access

provenance: supported. Targets: GO:0031972.

Citation identities match native bibliography. Keeling selected secondary body was accessible through PMC despite failed alternative routes. Jin biology remains primary-abstract scope with separate deposit organism metadata; publisher403 is not full-body access. Historical reviews/status are unchanged.

### Bounded record-level coverage

completeness: supported. Targets: GO:0031972.

The entire maintained record and cited claim contexts were inspected at the stated source scopes. Additional exhaustive component inventories, numerical properties, images, traits and expanded mechanisms are optional. No verbatim quotation requires repair, and no status or history rewrite is proposed. This bounded review does not assert exhaustive literature completeness.

### Native protein identity and graph coverage

schema: supported. Targets: GO:0031972.

Both actual checks exited0. These records have no protein examples and no GENE_OR_PROTEIN causal nodes; complex/structure or spatial nodes are not forced into individual protein coverage. Empty inventory does not prove molecular membership or assembly necessity.

### Frozen historical input and deterministic bundle validation

provenance: supported. Targets: GO:0031972.

Original YAML validates and exact native Markdown render agrees. Historical target hash and current hash match; no stale delta requires refresh. New assessments correct bundle applicability without rewriting originals or claiming scientific record edits.

### TOC–TIC prose triggers real covered-organism assessment

scope: supported. Targets: GO:0031972.

Although the inventory is sparse, taxon/example prose explicitly names the TOC–TIC protein-import pathway. It triggers applicability independently of transcriptomics claims. The fresh full catalogue has no Chlamydomonas dataset or matching green-lineage host; downstream modules from cyanobacteria cannot validate chloroplast import. Current bounded outcome is no matching dataset, not a no-expression exemption. Historical runner failure remains separately dated.

### Immutable original validation and input comparison

schema: supported. Targets: GO:0005776.

Original validate/render succeeds and frozen source blob matches. Current record changed and receives substantive source reassessment below; original files remain immutable.

### Native current protein verifier and graph inventory

schema: supported. Targets: GO:0005776.

Both current native commands return0, with zero protein examples and zero GENE_OR_PROTEIN nodes. Empty-inventory success is not experimental completeness.

### Immutable original validation and input comparison

schema: supported. Targets: GO:0034423.

Original validate/render succeeds and frozen source blob matches. Current record equals the original frozen target; source and scope are independently reassessed.

### Native current protein verifier and graph inventory

schema: supported. Targets: GO:0034423.

Both current native commands return0, with zero protein examples and zero GENE_OR_PROTEIN nodes. Empty-inventory success is not experimental completeness.

### Immutable original validation and input comparison

schema: supported. Targets: GO:0000421.

Original validate/render succeeds and frozen source blob matches. Current record equals the original frozen target; source and scope are independently reassessed.

### Native current protein verifier and graph inventory

schema: supported. Targets: GO:0000421.

Both current native commands return0, with zero protein examples and zero GENE_OR_PROTEIN nodes. Empty-inventory success is not experimental completeness.

### Immutable original validation and input comparison

schema: supported. Targets: GO:0045009.

Original validate/render succeeds and frozen source blob matches. Current record changed and receives substantive source reassessment below; original files remain immutable.

### Native current protein verifier and graph inventory

schema: supported. Targets: GO:0045009.

The current verifier passes for two reviewed CHS examples; graph coverage is one COVERED protein node. These checks do not establish localization, essentiality, or a complete fungal protein cohort.

### Whole organelle identity and part boundaries

identity: supported. Targets: GO:0005776.

GO exact identity, organelle kind, double-membrane definition and two synonym scopes agree. Membrane and lumen are parts, not is-a equivalents; invading-microorganism wording derives from the authority definition, not the yeast experiments.

### Stale refresh: macroautophagy function grounding

grounding: supported. Targets: GO:0005776.

The changed function now explicitly uses GO:0016236, which exactly denotes macroautophagy through autophagosome formation. Existing graph grounding already used that term; no new mechanistic or taxonomic claim is introduced.

### Yeast starvation and canonical model source scope

evidence: supported. Targets: GO:0005776.

Starvation-conditioned yeast autophagy and the genetic/fluorescence model are supported. COMMON is read with the explicit induction condition, not constitutive presence in every cell. PAS organization is distinguished from a mature autophagosome.

### Constituent boundary and deferred Atg cohorts

completeness: supported. Targets: GO:0005776.

The collective membrane boundary is essential by organelle identity; this does not assign essentiality to an individual lipid or Atg protein. The existing TODO explicitly defers exact taxon-neutral machinery while the graph is NONMECHANISTIC. No false absent-family assertion or fabricated universal protein inventory is added.

### All four boundary/function/fusion edges

graph: supported. Targets: GO:0005776.

Bounds, parthood and macroautophagy support are authority-aligned. The yeast vacuole-fusion endpoint is explicitly supported by GO:0061909; Takeshige establishes vacuolar bodies but does not independently dissect the fusion mechanism. The graph preserves that coarse scope.

### Structured-source applicability correction

scope: concern. Targets: GO:0005776.

Original expression-only N/A rationale is inadequate for named macroautophagy and ATG context. Fresh full-catalogue assessment finds no fungal dataset, so matched-organism search/module summary is unavailable; absence is not negative science.

### Current assessment and original clean verdict

provenance: supported. Targets: GO:0005776.

The original clean scientific outcome is retained after refreshing changed grounding. Source-access limitations remain explicit; no current scientific finding or prior terminal category-finding resolution is asserted.

### Volume identity, synonyms and hierarchy

identity: supported. Targets: GO:0034423.

The lumen is a subcellular volume, not a protein complex or membrane. GO exact definition and UniProt synonyms, vesicle-lumen is-a and autophagosome parthood agree; the model is not claimed to reproduce current GO direct parent edges.

### Yeast occurrence and experimental exemplar

evidence: supported. Targets: GO:0034423.

The inherited conditional yeast context and formation-model citation are supported by the same bounded starvation and PAS experiments. Neither is used to infer resident lumen components from transient degradative cargo.

### Two topology edges and omitted cargo inventory

graph: supported. Targets: GO:0034423.

Lumen parthood and membrane bounds agree with GO/UniProt. No resident protein, enzymatic function or complete Atg mechanism is asserted; omission of transient cargo from components is appropriate.

### Sparse topology applicability exclusion

scope: not_applicable. Targets: GO:0034423.

This record asserts a compartment and two topology edges; macroautophagy supplies enclosing-organelle context and Atg wording expressly excludes mechanism. It has no named resident-protein/function/pathway inventory needing a matched molecular query. It is not counted as an additional adapter defect; the same catalogue also has no yeast match.

### Unchanged original clean verdict

provenance: supported. Targets: GO:0034423.

The exact frozen record is unchanged; independent current source inspection identifies no scientific correction. Original source/validation dates and limited access remain historical rather than silently renewed.

### Boundary identity, synonyms and hierarchy

identity: supported. Targets: GO:0000421.

Active GO:0000421 and UniProt SL-0022 agree on membrane identity, synonyms, cytoplasmic-vesicle-membrane is-a and autophagosome parthood. This is distinct from both the organelle and its lumen.

### Generic lipid material and essentiality

completeness: supported. Targets: GO:0000421.

The ungrounded constituent is generic lipid-bilayer material, not a second whole-membrane identity. The explicit rationale correctly avoids substituting the whole-structure GO term for a chemical constituent; essentiality attaches to the collective boundary. No exact chemical was invented.

### Function and yeast exemplar

evidence: supported. Targets: GO:0000421.

Macroautophagy grounding is exact and the membrane function is coarse. Yeast induction and PAS/formation model remain condition-scoped. Xie is secondary abstract context; it is not treated as a newly inspected full experimental body.

### Three boundary and support edges

graph: supported. Targets: GO:0000421.

Bounds, parthood and macroautophagy support are consistent with authority definitions. The stated NONMECHANISTIC scope does not assert molecular initiation, closure or fusion mechanisms.

### Structured-source applicability correction

scope: concern. Targets: GO:0000421.

The original expression-only N/A rationale is inadequate for the explicit macroautophagy function/pathway assertion. Current catalogue has no fungal match, so no target-specific downstream module query can be grounded; this is a bounded coverage conclusion.

### Unchanged original clean verdict

provenance: supported. Targets: GO:0000421.

Independent inspection retains the clean scientific verdict for the unchanged record; adapter rationale is a bundle repair, not a reason to mutate scientific record content.

### Fungal vesicle identity, definition and taxon scope

identity: supported. Targets: GO:0045009.

Exact GO identity and cytoplasmic-vesicle parent are appropriate. The multi-lineage secondary review is retained as bounded fungal context, not evidence of universality; the Saccharomyces example has primary trafficking support.

### Inherited exact membrane grounding F1

grounding: concern. Targets: GO:0045009.

Current component and active discussion still assert that no exact chitosome membrane term exists. Active GO:0030661 is the exact match; preserve the original finding key and minor severity while leaving record curation outside this PR.

### CHS examples, families and identity limits

grounding: supported. Targets: GO:0045009.

Both declared S288C examples are reviewed exact gene identities, and the bounded reviewed-symbol query confirms one entry per gene. Both match broad IPR004835; that does not establish every family member as resident cargo or erase the unresolved heterogeneous fungal-cohort TODO.

### Protein source annotations and necessity scope

evidence: supported. Targets: GO:0045009.

The three P29465 PMIDs are genuine experimental Cell membrane annotations and are labeled accordingly. Native graph coverage is complete for the two declared symbols, not all fungal isoenzymes. UNKNOWN protein essentiality avoids inferring universal necessity from yeast transport mutations.

### Stale refresh: plasma-membrane cargo-delivery edge

graph: supported. Targets: GO:0045009.

The new edge is supported for delivery by primary Chs3 trafficking experiments. Its stated purpose of cell-surface activation is read within explicit NONMECHANISTIC scope, not as proof that transport is sufficient for activation or that all isoenzymes share Chs6 dependence. The primary Discussion leaves activation alternatives unresolved.

### Existing storage, membrane, septum and product edges

graph: supported. Targets: GO:0045009.

The boundary and latent-cargo pool have authority/fractionation support; polarized delivery has yeast primary evidence. Septum delivery remains proposed, chitin is chemical output rather than resident cargo, and secondary review disagreements about ontogeny are not promoted into settled mechanism.

### Pinned PathwayMech relation

consistency: supported. Targets: GO:0045009.

The exact pinned S288C model contains CHS3 and its chitin-synthesis activity. The record correctly states enzyme delivery to cell surface and preserves species-experiment versus narrower pathway-strain scope; it does not relocate catalysis into the chitosome.

### Missing structured-source applicability assessment

scope: concern. Targets: GO:0045009.

Original check list omits applicability despite CHS1/CHS3 and declared pathway delivery. Fresh catalogue inspection supplies a bounded no-fungal-dataset conclusion; no unmatched bacterial gene/module query is substituted.

### Exact inherited finding lineage and verdict

provenance: concern. Targets: GO:0045009.

Original20261021T110752Z-chitosome-audit/F1 remains open with its stable key and minor confirmed severity. Current needs_curation is solely the exact membrane-grounding defect found here; the refresh itself can be completed in a review-only successor.

### Native schema, deterministic rendering and unchanged frozen input

schema: supported. Targets: GO:0160211.

Original review validates and renders byte-identically. Its target hash equals the original source bytes and current source-head bytes. Root-run native protein gates pass within their explicit inventory limits.

### Native schema, deterministic rendering and unchanged frozen input

schema: supported. Targets: GO:0009507.

Original review validates and renders byte-identically. Its target hash equals the original source bytes and current source-head bytes. Root-run native protein gates pass within their explicit inventory limits.

### Native schema, deterministic rendering and unchanged frozen input

schema: supported. Targets: GO:0009941.

Original review validates and renders byte-identically. Its target hash equals the original source bytes and current source-head bytes. Root-run native protein gates pass within their explicit inventory limits.

### Structured-source applicability and actual organism coverage

scope: not_applicable. Targets: GO:0160211.

Named molecular actors/import pathways trigger applicability assessment. The current complete official catalogue has no matched organism/dataset for this target; downstream gene/module lookups therefore do not apply. Runner unavailability is historical and separate. No bacterial/cyanobacterial dataset is substituted for a eukaryotic plastid.

### Images, snippets and unobserved measurements

scope: not_applicable. Targets: GO:0160211.

The current record has no attached image or verbatim snippet requiring image/snippet validation. Source caption/text inspection is not pixel or raw-data reanalysis.

### Structured-source applicability and actual organism coverage

scope: not_applicable. Targets: GO:0009507.

Named molecular actors/import pathways trigger applicability assessment. The current complete official catalogue has no matched organism/dataset for this target; downstream gene/module lookups therefore do not apply. Runner unavailability is historical and separate. No bacterial/cyanobacterial dataset is substituted for a eukaryotic plastid.

### Images, snippets and unobserved measurements

scope: not_applicable. Targets: GO:0009507.

The current record has no attached image or verbatim snippet requiring image/snippet validation. Source caption/text inspection is not pixel or raw-data reanalysis.

### Structured-source applicability and actual organism coverage

scope: not_applicable. Targets: GO:0009941.

Named molecular actors/import pathways trigger applicability assessment. The current complete official catalogue has no matched organism/dataset for this target; downstream gene/module lookups therefore do not apply. Runner unavailability is historical and separate. No bacterial/cyanobacterial dataset is substituted for a eukaryotic plastid.

### Images, snippets and unobserved measurements

scope: not_applicable. Targets: GO:0009941.

The current record has no attached image or verbatim snippet requiring image/snippet validation. Source caption/text inspection is not pixel or raw-data reanalysis.

### Exact membrane identity and whole-organelle boundary

identity: supported. Targets: GO:0160211.

GO:0160211 identifies an apicoplast lipid bilayer, GO:0016020 its broad membrane parent, and GO:0020011 the containing organelle. Frozen whole-apicoplast neighbor gives compatible parthood; identity is not broadened to the whole organelle.

### Collective lipid constituent and necessity

grounding: supported. Targets: GO:0160211.

The label-only lipid-bilayer constituent is a collective matrix of the membrane structure; its essentiality is definitional at this collective scale. No individual lipid species, unique class CURIE or specific biosynthetic gene is inferred essential. The whole-membrane GO identity is not reused as the chemical matrix.

### Variable apicomplexan presence and exact example taxa

scope: supported. Targets: GO:0160211.

Exact native taxonomy supports Apicomplexa, Toxoplasma and Plasmodium identities. Secondary review context supports VARIABLE presence rather than universality; experimental membrane architecture and Tic20 claims retain their stated organism scope.

### Direct membrane-architecture evidence

evidence: supported. Targets: GO:0160211.

Lemgruber primary cryo-electron tomography resolves four membranes in Plasmodium merozoites, matching the scoped canonical example and membrane-boundary claim. Captions/Results were inspected; no new image-pixel or reconstruction analysis is claimed.

### S8GBF3 identity, family and experimental scope

grounding: supported. Targets: GO:0160211.

S8GBF3 is unreviewed T. gondii ME49 TIC20/TGME49_255370 with native Tic20-family match. The institutional copy of van Dooren primary study supports innermost-membrane placement and import dependency. Metadata/family matches alone do not prove location, essentiality or pore formation.

### Tic20 topology versus direct channel mechanism

graph: supported. Targets: GO:0160211.

The actual edge is resides in and the graph explicitly excludes a full import reaction. It is supported at localization/import-step scope. Early residual import and delayed near-complete block are retained; neither the node label nor this acceptance is treated as direct proof that Tic20 is a pore. A different whole-organelle translocates edge is outside this target.

### B9PY98 ER versus apicoplast Der1 identity

identity: concern. Targets: GO:0160211.

Original F1 remains: the SELMA node includes B9PY98, whose native ENA bridge is Der1ER1 FJ976521/ACU32856.1. Primary-study deposit mapping distinguishes apicoplast Der1Ap FJ976520/ACU32855.1/C9WWW6. Identifier validity and shared family membership cannot cure a wrong cellular paralog.

### O97275/PfsDer1-2 evidence bridge

evidence: supported. Targets: GO:0160211.

Native O97275/CAB38986.4/PF3D7_0314300 metadata and NCBI Gene support the locus bridge; the Kalanon published Der1-2 antibody peptide matches O97275. Der1-2 antibody experiments are kept distinct from full-length Der1-1 localization. This bounded representative identity does not validate every SELMA constituent.

### Protein-import boundary and outer-envelope system

evidence: supported. Targets: GO:0160211.

Agrawal2013 primary localization/ablation/complementation and the Tic20 study support an apicoplast protein-import system. The SELMA outer-membrane position retains source-model scope; the membrane record does not claim an identified endogenous ubiquitin modifier or a complete import mechanism.

### Native identifier checks are not localization checks

provenance: supported. Targets: GO:0160211.

Both native commands pass: three graph UniProt xrefs resolve and two nodes are UNANCHORED_WITH_UNIPROT. This establishes limited identifier inventory coverage; it does not contradict or resolve the ER-paralog finding.

### Current target verdict and exact finding continuity

consistency: concern. Targets: GO:0160211.

needs_curation remains appropriate for the unchanged record because the original major wrong-paralog xref is still present. Preserve its original issue key and F1 occurrence; file separate membrane-target curation rather than claiming a whole-apicoplast issue resolves this record.

### Exact organelle/envelope identity, parentage and parthood

identity: supported. Targets: GO:0009507.

The chlorophyll-containing plastid identity is GO:0009507, with GO:0009536 as is-a parent. Exact component GO definitions and typed child relations distinguish envelope, bilayers, stroma and thylakoids.

### Taxonomic identities, prevalence qualification and experimental organism

scope: supported. Targets: GO:0009507.

ENA verifies Viridiplantae and Chlamydomonas reinhardtii; Keeling secondary body supports primary-plastid green-algal/plant context. COMMON is qualified to photosynthetic members, not all Viridiplantae. The Jin architecture is explicitly Chlamydomonas and is not universalized to every plastid.

### Membrane and import-complex boundaries

grounding: supported. Targets: GO:0009507.

Three membrane components have exact GO identities. The divergent Chlamydomonas TOC-TIC aggregate is explicitly label-only; current GO:0061927 contains classical Tic110/Toc159/Toc34 requirements, so withholding that specific identity is justified rather than generic family-grounding deferral.

### Unknown formation dependencies

scope: unknown. Targets: GO:0009507.

Component necessity remains UNKNOWN. Ontological identity, proteome localization and a resolved import assembly do not by themselves establish whether removal of each constituent prevents formation of this complete maintained structure. No formation-dependency claim is added.

### Chlamydomonas envelope-spanning import architecture

evidence: supported. Targets: GO:0009507.

Jin primary abstract and author-hosted abstract support the 14-component envelope-spanning TOC-TIC assembly, with a potential Tic20/YlmG inner route and intermembrane scaffold. The record states compartment-level import function; this review does not claim to have reanalysed transport kinetics, full Results or raw cryo-EM data.

### Nonmechanistic topology and import relations

graph: supported. Targets: GO:0009507.

All eight graph edges were read: envelope enclosing organelle/bounding stroma, bilayer parthood, thylakoid stromal placement and membrane boundary, and TOC-TIC spanning/mediating import. GO definitions support topology; Jin supplies Chlamydomonas assembly scope. This does not establish every subunit, pore mechanism or biogenesis pathway.

### Empty native protein inventory

provenance: supported. Targets: GO:0009507.

Verify and causal audit exit 0, but there are zero protein_examples and zero GENE_OR_PROTEIN nodes. This is an empty typed inventory, not experimental validation of named proteins in prose or generic TOC/TIC function.

### Positive target assessment with explicit access and completeness limits

consistency: supported. Targets: GO:0009507.

pass_with_limitations remains supported: exact identity, compartment topology and bounded Chlamydomonas import claims have positive source support. Unknown formation necessity, incomplete constituent enumeration and abstract-level Jin access remain explicit. Original review has no request_curation finding for this target; open descriptive TODOs are not automatically converted into a defect.

### Exact organelle/envelope identity, parentage and parthood

identity: supported. Targets: GO:0009941.

GO:0009941 denotes the double-bilayer envelope including intermembrane space, with GO:0009526 as is-a parent and GO:0009507 as containing organelle. It is distinct from either single membrane or either adjoining space.

### Taxonomic identities, prevalence qualification and experimental organism

scope: supported. Targets: GO:0009941.

ENA verifies Viridiplantae and Chlamydomonas reinhardtii; Keeling secondary body supports primary-plastid green-algal/plant context. COMMON is qualified to photosynthetic members, not all Viridiplantae. The Jin architecture is explicitly Chlamydomonas and is not universalized to every plastid.

### Membrane and import-complex boundaries

grounding: supported. Targets: GO:0009941.

Separate Toc and Tic complexes have exact GO identities and outer/inner-envelope placement. They are represented as complexes/STRUCTURE nodes, without pretending that one individual protein is equivalent to the complete assembly.

### Unknown formation dependencies

scope: unknown. Targets: GO:0009941.

Component necessity remains UNKNOWN. Ontological identity, proteome localization and a resolved import assembly do not by themselves establish whether removal of each constituent prevents formation of this complete maintained structure. No formation-dependency claim is added.

### Chlamydomonas envelope-spanning import architecture

evidence: supported. Targets: GO:0009941.

Jin primary abstract and author-hosted abstract support the 14-component envelope-spanning TOC-TIC assembly, with a potential Tic20/YlmG inner route and intermembrane scaffold. The record states compartment-level import function; this review does not claim to have reanalysed transport kinetics, full Results or raw cryo-EM data.

### Nonmechanistic topology and import relations

graph: supported. Targets: GO:0009941.

All ten graph edges were read: envelope/organellar and space boundaries, bilayer parthood, Toc/Tic membrane placement, coupling and compartment-level precursor routing. GO definitions support topology; Jin supplies Chlamydomonas assembly scope. This does not establish every subunit, pore mechanism or biogenesis pathway.

### Empty native protein inventory

provenance: supported. Targets: GO:0009941.

Verify and causal audit exit 0, but there are zero protein_examples and zero GENE_OR_PROTEIN nodes. This is an empty typed inventory, not experimental validation of named proteins in prose or generic TOC/TIC function.

### Positive target assessment with explicit access and completeness limits

consistency: supported. Targets: GO:0009941.

pass_with_limitations remains supported: exact identity, compartment topology and bounded Chlamydomonas import claims have positive source support. Unknown formation necessity, incomplete constituent enumeration and abstract-level Jin access remain explicit. Original review has no request_curation finding for this target; open descriptive TODOs are not automatically converted into a defect.

### Photosynthesis and comparative chloroplast proteome

evidence: supported. Targets: GO:0009507.

GO supports the photosynthesis process identity. Terashima secondary review complete abstract supports the Chlamydomonas chloroplast proteome/metabolic comparison and photosynthetic context. The nominal PDF response is challenge HTML, so the current review does not claim new full-body inspection or exhaustive localization coverage.

### Complete frozen-input comparison and bounded refresh

provenance: supported. Targets: GO:0160211, GO:0005776, GO:0034423, GO:0000421, GO:0030075, GO:0045009, GO:0009507, GO:0009941, GO:0009706, GO:0031972.

2 of ten original target hashes differ from current main. The changed content is substantively reassessed in the target-specific assessments; original observations remain historical and unchanged. All current target and used context bytes are frozen.

## Findings

### plaque-t4-F1: The cited primary thylakoid studies used Synechococcus PCC7942, not Synechocystis PCC6803

major / open / confirmed; issue key: bacterial_thylakoid-experimental-organism-mismatch.

Huokko2021 explicitly performs light-regulated thylakoid biogenesis experiments in Synechococcus elongatus PCC7942, whereas canonical_examples[0] assigns that experiment to tax1148 Synechocystis PCC6803. Casella2017 likewise performs its native membrane organization and mobility experiments in PCC7942, but four maintained component/graph source notes call the assayed organism Synechocystis. Both papers discuss earlier Synechocystis work, which is not a substitute for their own Methods. Reconcile the exemplar taxon, label, note and reference together, and correct the repeated Casella organism attributions. The evidence does not imply that Synechocystis lacks thylakoids.

### micro-F1: Ground the chitosome membrane to its exact active GO term

minor / open / confirmed; issue key: chitosome-exact-membrane-grounding.

The current component remains REVIEWED_LABEL_ONLY and the open grounding discussion says GO has no exact chitosome-membrane child. Native GO0045009 explicitly lists GO0030661 part_of, and native GO0030661 is chitosome membrane, defined as the lipid bilayer surrounding a chitosome. This is an exact match to the existing constituent, not a new optional inventory row. Ground the membrane component and update the active discussion accordingly while preserving historical curation notes and the separately unresolved fungal protein-cohort question.

### septin-S2358-F1: The SELMA node links to an ER Der1 paralog

major / open / confirmed; issue key: apicoplast-membrane-selma-er-paralog-xref.

The membrane SELMA/ERAD-derived import-machinery node retains B9PY98. Native UniProt/ENA cross-references identify Der1ER1 FJ976521/ACU32856.1. The author primary-study Methods and Table3.1 separately map apicoplast Der1Ap FJ976520/ACU32855.1, now C9WWW6. Shared family and successful accession resolution do not make this ER paralog an appropriate apicoplast-machinery xref.

## Recommended Actions And Acceptance Checks

### plaque-t4-A1

Reconcile the canonical taxon, label, note and source to the actual PCC7942 experiment, or supply genuinely PCC6803-specific evidence; correct the four repeated Casella organism attributions together. Preserve general bacterial-thylakoid identity and do not infer PCC6803 lacks thylakoids.

- Preserve stable issue key and exact previous occurrence.
- Separately authorized guarded record curation and append-only history; this review PR makes no scientific record changes.
- Recheck every cited experimental organism and native taxonomy, then native schema/strict, labels, references, history and QC after later curation.

### micro-A1

In separately authorized record curation, ground the existing chitosome membrane constituent to active GO:0030661 and update only the false membrane portion of the active grounding discussion. Preserve history and the independently unresolved fungal cargo-class scope.

- The existing membrane component uses exact GO:0030661 with source-backed label correspondence and grounding status.
- The active discussion no longer asserts that an exact chitosome membrane term does not exist; historical curation text is preserved.
- Do not substitute the broad chitin-synthase family for a demonstrated universal fungal cargo cohort or infer constituent necessity from identity.
- Use the guarded writer and curation/history protocol with applicable native checks in a separate record-curation PR.

### septin-S2358-C1

In a separate record-curation change, remove the ER-paralog B9PY98 from the membrane SELMA node or replace it with independently verified apicoplast Der1Ap/C9WWW6 and its primary-source sequence bridge. Preserve unreviewed status, exact taxon, missing native gene-name field and bounded representative scope; do not claim that the whole complex equals one protein.

- Exact graph xrefs identify the represented apicoplast actors rather than ER paralogs.
- Any C9WWW6 replacement retains FJ976520/ACU32855.1 primary-source mapping and exact taxon/status metadata.
- Run focused schema, strict CURIE and native UniProt checks.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| current-record-0 | data/structures/membrane_organelle/apicoplast_membrane.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 fb3e343e0ed2a8711dff2305abea2166c589cb0a7b169d291c67fed81990ca58; current SHA256 fb3e343e0ed2a8711dff2305abea2166c589cb0a7b169d291c67fed81990ca58. Record bytes unchanged since the original review. |
| original-review-0 | reviews/structured/20261021T110736Z-apicoplast-membrane-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-1 | data/structures/membrane_organelle/autophagosome.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 9d18c1f34ce5e4da65546eccf8f4ffc9a2273fcca1cd6db4efbb770f8591c3ba; current SHA256 08c1df95826ee2cb8b86b66592876f324eae999c7cafdc619d1ffad1607f6232. Changed record reassessed against current sources. |
| original-review-1 | reviews/structured/20261021T110741Z-autophagosome-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-2 | data/structures/membrane_organelle/autophagosome_lumen.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 33fbf9f3ae1591081dd1e113d0fd7476c64bdafaa238ec35c7705fb89bb0f98d; current SHA256 33fbf9f3ae1591081dd1e113d0fd7476c64bdafaa238ec35c7705fb89bb0f98d. Record bytes unchanged since the original review. |
| original-review-2 | reviews/structured/20261021T110744Z-autophagosome-lumen-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-3 | data/structures/membrane_organelle/autophagosome_membrane.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 aa651db3a9b5a208ae7a4deef9d3595d79c0296cda8ebdc9a1c524a11b948254; current SHA256 aa651db3a9b5a208ae7a4deef9d3595d79c0296cda8ebdc9a1c524a11b948254. Record bytes unchanged since the original review. |
| original-review-3 | reviews/structured/20261021T110747Z-autophagosome-membrane-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-4 | data/structures/membrane_organelle/bacterial_thylakoid.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 a134c6cf6fd6069f0a0ddc37f1e99ded9a32994b3b1fa16d2f9938e3e46b8c40; current SHA256 a134c6cf6fd6069f0a0ddc37f1e99ded9a32994b3b1fa16d2f9938e3e46b8c40. Record bytes unchanged since the original review. |
| original-review-4 | reviews/structured/20261021T110749Z-bacterial-thylakoid-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-5 | data/structures/membrane_organelle/chitosome.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 7233ef84787e4a164a1388fbb12643f34bfc28bf12272f6c0898868975376938; current SHA256 ec564f818b649f3c4c8a56de6d6bea798eded59e73f1c4b840325eb83b9d5493. Changed record reassessed against current sources. |
| original-review-5 | reviews/structured/20261021T110752Z-chitosome-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-6 | data/structures/membrane_organelle/chloroplast.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 4c13f5dadaeb23a88fabfc2b5ec65034ed0ac83cbca9d45143793618acf2e727; current SHA256 4c13f5dadaeb23a88fabfc2b5ec65034ed0ac83cbca9d45143793618acf2e727. Record bytes unchanged since the original review. |
| original-review-6 | reviews/structured/20261021T110755Z-chloroplast-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-7 | data/structures/membrane_organelle/chloroplast_envelope.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 29da363489107536342db1782001be534ea54605039b80c201cba0a46de9468e; current SHA256 29da363489107536342db1782001be534ea54605039b80c201cba0a46de9468e. Record bytes unchanged since the original review. |
| original-review-7 | reviews/structured/20261021T110757Z-chloroplast-envelope-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-8 | data/structures/membrane_organelle/chloroplast_inner_membrane.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 05283f5252a6354d26bef1ff196b3a9e10fbd6e72e9a6ec17014330f7a28dbb3; current SHA256 05283f5252a6354d26bef1ff196b3a9e10fbd6e72e9a6ec17014330f7a28dbb3. Record bytes unchanged since the original review. |
| original-review-8 | reviews/structured/20261021T110759Z-chloroplast-inner-membrane-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-9 | data/structures/membrane_organelle/chloroplast_intermembrane_space.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 7ab90f4d2f4c41c466e100d589fb1f1d42bf90ded515dea6db5575d54119d43a; current SHA256 7ab90f4d2f4c41c466e100d589fb1f1d42bf90ded515dea6db5575d54119d43a. Record bytes unchanged since the original review. |
| original-review-9 | reviews/structured/20261021T110802Z-chloroplast-intermembrane-space-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| plaque-current-4 | data/structures/membrane_organelle/bacterial_thylakoid.yaml; Complete current YAML at source e721920f30c72a6c35cecb9913c6780e18a460ed; every field, graph edge and history entry | context_only | Current bytes match the historical frozen target hash. Entire maintained record independently reassessed; status remains PROPOSED and no target image is declared. |
| plaque-original-4 | reviews/structured/20261021T110749Z-bacterial-thylakoid-audit/review.yaml; Complete original YAML and Markdown; actual native validate and exact render --content | context_only | Native validation and deterministic Markdown equality passed; historical target bytes match the original frozen hash. Original finding and check scopes were independently read. |
| plaque-current-8 | data/structures/membrane_organelle/chloroplast_inner_membrane.yaml; Complete current YAML at source e721920f30c72a6c35cecb9913c6780e18a460ed; every field, graph edge and history entry | context_only | Current bytes match the historical frozen target hash. Entire maintained record independently reassessed; status remains PROPOSED and no target image is declared. |
| plaque-original-8 | reviews/structured/20261021T110759Z-chloroplast-inner-membrane-audit/review.yaml; Complete original YAML and Markdown; actual native validate and exact render --content | context_only | Native validation and deterministic Markdown equality passed; historical target bytes match the original frozen hash. Original finding and check scopes were independently read. |
| plaque-current-9 | data/structures/membrane_organelle/chloroplast_intermembrane_space.yaml; Complete current YAML at source e721920f30c72a6c35cecb9913c6780e18a460ed; every field, graph edge and history entry | context_only | Current bytes match the historical frozen target hash. Entire maintained record independently reassessed; status remains PROPOSED and no target image is declared. |
| plaque-original-9 | reviews/structured/20261021T110802Z-chloroplast-intermembrane-space-audit/review.yaml; Complete original YAML and Markdown; actual native validate and exact render --content | context_only | Native validation and deterministic Markdown equality passed; historical target bytes match the original frozen hash. Original finding and check scopes were independently read. |
| plaque-neighbor-chloroplast | data/structures/membrane_organelle/chloroplast.yaml; Frozen local boundary context or native review rule | context_only | Neighbor identity, definition, hierarchy, parthood and discussions only; no whole-record scientific judgment. |
| plaque-neighbor-chloroplast_envelope | data/structures/membrane_organelle/chloroplast_envelope.yaml; Frozen local boundary context or native review rule | context_only | Neighbor identity, definition, hierarchy, parthood and discussions only; no whole-record scientific judgment. |
| plaque-policy | .claude/skills/review-yaml-record/SKILL.md; Frozen local boundary context or native review rule | context_only | Native rules distinguish structure identity, molecular grounding, membership and assembly necessity; require claim-level source scopes, actual adapter applicability and immutable evidence-bearing reviews. |
| plaque-rubric | .claude/skills/curate-yaml-record/references/review-checklist.md; Frozen local boundary context or native review rule | context_only | Native rules distinguish structure identity, molecular grounding, membership and assembly necessity; require claim-level source scopes, actual adapter applicability and immutable evidence-bearing reviews. |
| plaque-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Frozen local boundary context or native review rule | context_only | Native rules distinguish structure identity, molecular grounding, membership and assembly necessity; require claim-level source scopes, actual adapter applicability and immutable evidence-bearing reviews. |
| plaque-schema-policy | src/cellstructuremech/schema/cellstructuremech.yaml; Frozen local boundary context or native review rule | context_only | Native rules distinguish structure identity, molecular grounding, membership and assembly necessity; require claim-level source scopes, actual adapter applicability and immutable evidence-bearing reviews. |
| plaque-thylakoid-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030075,GO:0009579,GO:0031676,GO:0031979,GO:0030094,GO:0030096,GO:0009512,GO:0045259,GO:0009767,GO:0042651; Exact returned term IDs, definitions, synonyms, comment and typed child relations | supports | Current GO terms support the stated identities and distinguish whole structures, membranes and enclosed regions. Typed is_a versus part_of relations are inspected separately; ontology-derived wording is not experimental evidence of universal biogenesis. |
| plaque-root21-sources-inner-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009528,GO:0009570,GO:0009706,GO:0009941,GO:0031969,GO:0031972; Exact returned term IDs, definitions, synonyms, comment and typed child relations | supports | Current GO terms support the stated identities and distinguish whole structures, membranes and enclosed regions. Typed is_a versus part_of relations are inspected separately; ontology-derived wording is not experimental evidence of universal biogenesis. |
| plaque-root21-sources-ims-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009529,GO:0009706,GO:0009707,GO:0009941,GO:0031972; Exact returned term IDs, definitions, synonyms, comment and typed child relations | supports | Current GO terms support the stated identities and distinguish whole structures, membranes and enclosed regions. Typed is_a versus part_of relations are inspected separately; ontology-derived wording is not experimental evidence of universal biogenesis. |
| plaque-inner-isa | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009706/ancestors?relations=is_a; Explicit relations=is_a ancestor response; complete returned ancestor list | supports | The asserted is_a parents occur in the is_a-only closure. This does not substitute a parthood relation for subclass identity. |
| plaque-ims-isa | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031972/ancestors?relations=is_a; Explicit relations=is_a ancestor response; complete returned ancestor list | supports | The asserted is_a parents occur in the is_a-only closure. This does not substitute a parthood relation for subclass identity. |
| plaque-thylakoid-agent-tax-1117 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1117; Native taxId, scientificName, rank and lineage; identity only | supports | Exact authority identity: 1117 Cyanobacteriota. Taxonomic identity does not establish prevalence, experimental stock or localization. |
| plaque-thylakoid-agent-tax-1148 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1148; Native taxId, scientificName, rank and lineage; identity only | supports | Exact authority identity: 1148 Synechocystis sp. PCC 6803. Taxonomic identity does not establish prevalence, experimental stock or localization. |
| plaque-thylakoid-agent-tax-1140 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1140; Native taxId, scientificName, rank and lineage; identity only | supports | Exact authority identity: 1140 Synechococcus elongatus PCC 7942 = FACHB-805. Taxonomic identity does not establish prevalence, experimental stock or localization. |
| plaque-root21-sources-NCBITaxon-33090 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/33090; Native taxId, scientificName, rank and lineage; identity only | supports | Exact authority identity: 33090 Viridiplantae. Taxonomic identity does not establish prevalence, experimental stock or localization. |
| plaque-root21-sources-NCBITaxon-3055 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3055; Native taxId, scientificName, rank and lineage; identity only | supports | Exact authority identity: 3055 Chlamydomonas reinhardtii. Taxonomic identity does not establish prevalence, experimental stock or localization. |
| plaque-thylakoid-agent-perez2024-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1146%2Fannurev-cellbio-120823-022747&amp;format=json&amp;resultType=core; Exact DOI query: authors, title, DOI/PMID/PMCID and complete returned abstract; no body inference | supports | Native bibliography resolves to Evolution of Thylakoid Structural Diversity.; Perez-Boerema A, Engel BD, Wietrzynski W.. The abstract was read, but full-body support is claimed only by separately scoped rows. |
| plaque-thylakoid-agent-casella2017-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1016%2Fj.molp.2017.09.019&amp;format=json&amp;resultType=core; Exact DOI query: authors, title, DOI/PMID/PMCID and complete returned abstract; no body inference | supports | Native bibliography resolves to Dissecting the Native Architecture and Dynamics of Cyanobacterial Photosynthetic Machinery.; Casella S, Huang F, Mason D, Zhao GY, Johnson GN, Mullineaux CW, Liu LN.. The abstract was read, but full-body support is claimed only by separately scoped rows. |
| plaque-thylakoid-agent-huokko2021-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038%2Fs41467-021-23680-1&amp;format=json&amp;resultType=core; Exact DOI query: authors, title, DOI/PMID/PMCID and complete returned abstract; no body inference | supports | Native bibliography resolves to Probing the biogenesis pathway and dynamics of thylakoid membranes.; Huokko T, Ni T, Dykes GF, Simpson DM, Brownridge P, Conradi FD, Beynon RJ, Nixon PJ, Mullineaux CW, Zhang P, Liu LN.. The abstract was read, but full-body support is claimed only by separately scoped rows. |
| plaque-root21-sources-doi-10.1098_rstb.2009.0103 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1098/rstb.2009.0103; Exact DOI query: authors, title, DOI/PMID/PMCID and complete returned abstract; no body inference | supports | Native bibliography resolves to The endosymbiotic origin, diversification and fate of plastids.; Keeling PJ.. The abstract was read, but full-body support is claimed only by separately scoped rows. |
| plaque-root21-sources-doi-10.1016_j.cell.2022.10.030 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.cell.2022.10.030; Exact DOI query: authors, title, DOI/PMID/PMCID and complete returned abstract; no body inference | supports | Jin2022 primary abstract reports a Chlamydomonas TOC–TIC supercomplex spanning both chloroplast envelope membranes with an IMS scaffold. This supports the bounded topology/import example; species is independently checked against deposited 7VCF entity metadata, and no strain is inferred. |
| plaque-thylakoid-agent-jats-PMC5683893 | https://pmc-oa-opendata.s3.amazonaws.com/PMC5683893.1/PMC5683893.1.xml; Primary JATS: Introduction, Results §§2.1–2.3 and selected §2.4/Discussion text; Methods §4.1 Strains and Growth Conditions. Figure captions within those sections, not independent pixels or supplements. | supports | Casella2017 explicitly assays Synechococcus elongatus PCC7942 grown in BG11 at30C. Native membrane isolation/BN-PAGE, AFM and tagged-complex TIRF/confocal/FRAP support photosystem, b6f and ATPase residence, heterogeneous organization and mobility in that strain. AFM b6f identification is explicitly tentative; earlier Synechocystis work is background, not the experimental organism. No universal assembly necessity is established. |
| plaque-thylakoid-agent-jats-PMC8190092 | https://pmc-oa-opendata.s3.amazonaws.com/PMC8190092.1/PMC8190092.1.xml; Primary JATS: Introduction; selected Results §§Sec4–Sec6 and Discussion Sec7; Methods Sec9 Strains and Culture, Sec12 TEM, Sec13 cryo-ET. Text and captions only; no independent image-pixel or raw-data audit. | supports | Huokko2021 uses Synechococcus elongatus PCC7942 for light-regulated thylakoid biogenesis. Source Methods distinguish that strain from cited Synechocystis literature. Observed membrane proximity and thylapse-like sites do not establish direct plasma-membrane fusion. Complex assembly/insertion and abundance vary with light and time; these results do not establish universal individual assembly requirements. |
| plaque-root21-sources-keeling2010-pmc | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2817223/; Secondary review HTML: abstract and §1 plastid origins, two bounding membranes, green algae/plants and TOC/TIC paragraphs; selected §3 secondary-plastid membrane/trafficking context. No figure-pixel audit. | supports | Keeling2010 secondary synthesis supports the primary plastid envelope and green-lineage context while recognizing nonphotosynthetic plastids and loss. Its evolutionary review is not a measured prevalence estimate or new primary membrane experiment. |
| plaque-root21-sources-SL-0051-json | https://rest.uniprot.org/locations/SL-0051.json; Native definition, GO correspondence, exact synonym, immediate isA and partOf objects with inherited hierarchy distinguished | supports | SL0051 defines the stroma–IMS boundary and has separate chloroplast-membrane and plastid-inner-membrane isA parents. SL0052 defines the volume between bilayers and has plastid-IMS isA plus chloroplast-envelope partOf. The location identifiers do not identify a particular lipid species. |
| plaque-root21-sources-SL-0052-json | https://rest.uniprot.org/locations/SL-0052.json; Native definition, GO correspondence, exact synonym, immediate isA and partOf objects with inherited hierarchy distinguished | supports | SL0051 defines the stroma–IMS boundary and has separate chloroplast-membrane and plastid-inner-membrane isA parents. SL0052 defines the volume between bilayers and has plastid-IMS isA plus chloroplast-envelope partOf. The location identifiers do not identify a particular lipid species. |
| plaque-jin2022-pdb-entry | https://data.rcsb.org/rest/v1/core/entry/7VCF; 7VCF struct.title and primary citation DOI, PMID, authors, year | supports | The deposited TOC–TIC structure is linked directly to Jin2022 DOI10.1016/j.cell.2022.10.030 and PMID36413996. This is source linkage, not an independent coordinate reanalysis. |
| plaque-jin2022-pdb-entity1 | https://data.rcsb.org/rest/v1/core/polymer_entity/7VCF/1; 7VCF polymer entity1 entity_src_gen and rcsb_entity_source_organism; no coordinate interpretation | supports | The primary deposition identifies source/host Chlamydomonas reinhardtii tax3055 for entity1, independently narrowing the abstract’s genus-level name to the maintained species. No strain, universal complex composition or essentiality is inferred. |
| plaque-perez-body-electron-transport | https://doi.org/10.1146/annurev-cellbio-120823-022747; Browser-returned indexed publisher body: Electron Transport Chain Complexes subsection and selected contact-site paragraphs; packet hash, not native HTML body | supports | Secondary review supports the PSII–quinone–b6f–soluble carrier–PSI sequence and proton-gradient use by ATP synthase. Only those returned body sections were used; indexed content is explicitly a browser fallback after native403 responses. |
| plaque-perez-body-introduction | https://doi.org/10.1146/annurev-cellbio-120823-022747; Browser-returned indexed official publisher Introduction and selected membrane-architecture/contact-site paragraphs; unrelated search hits excluded | supports | The publisher review explicitly identifies Gloeobacter as a thylakoid-lacking exception and separates cyanobacterial cytoplasm from plastid stroma. This supports qualitative distribution and topology, not quantitative prevalence or universal continuity. |
| plaque-perez2024-publisher | https://www.annualreviews.org/content/journals/10.1146/annurev-cellbio-120823-022747; Actual unsuccessful HTTP source-access response; not scientific article content | context_only | Fresh native route returned HTTP403. No body evidence is inferred from this response. Successful body/abstract/database fallbacks are separately scoped. |
| plaque-perez2024-body | https://www.annualreviews.org/deliver/fulltext/cellbio/40/1/annurev-cellbio-120823-022747.html?itemId=/content/journals/10.1146/annurev-cellbio-120823-022747&amp;mimeType=html&amp;fmt=ahah; Actual unsuccessful HTTP source-access response; not scientific article content | context_only | Fresh native route returned HTTP403. No body evidence is inferred from this response. Successful body/abstract/database fallbacks are separately scoped. |
| plaque-root21-sources-keeling2010-jats | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2817223/fullTextXML; Actual unsuccessful HTTP source-access response; not scientific article content | context_only | Fresh native route returned HTTP500. No body evidence is inferred from this response. Successful body/abstract/database fallbacks are separately scoped. |
| plaque-root21-sources-keeling2010-s3 | https://pmc-oa-opendata.s3.amazonaws.com/PMC2817223.1/PMC2817223.1.xml; Actual unsuccessful HTTP source-access response; not scientific article content | context_only | Fresh native route returned HTTP404. No body evidence is inferred from this response. Successful body/abstract/database fallbacks are separately scoped. |
| plaque-root21-sources-keeling2010-repository | https://marinebiology.pt/beu/files/bib/Keeling2010.pdf; Actual unsuccessful HTTP source-access response; not scientific article content | context_only | Fresh native route returned HTTP401. No body evidence is inferred from this response. Successful body/abstract/database fallbacks are separately scoped. |
| plaque-root21-sources-keeling2010-bioc | https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_xml/PMC2817223/unicode; Actual unsuccessful HTTP source-access response; not scientific article content | context_only | Fresh native route returned HTTP429. No body evidence is inferred from this response. Successful body/abstract/database fallbacks are separately scoped. |
| plaque-root21-sources-jin2022-publisher | https://www.sciencedirect.com/science/article/pii/S0092867422013769; Actual unsuccessful HTTP source-access response; not scientific article content | context_only | Fresh native route returned HTTP403. No body evidence is inferred from this response. Successful body/abstract/database fallbacks are separately scoped. |
| plaque-root21-sources-jin2022-author-publications | https://lifesciences.westlake.edu.cn/labs/zhen-yan/structural-biology-laboratory/publications/; Author laboratory publication listing HTML/embedded metadata; bounded inspection for Jin2022 source access | context_only | The listing was readable but was not used as primary-paper body evidence. No full Jin paper or experimental strain is inferred from it. |
| plaque-catalogue | https://imodulondb.org/api/datasets; Entire fresh /api/datasets response, every returned organism/dataset entry; no pagination | supports | The catalogue includes Synechococcus elongatus elprecise300 but no Synechocystis or Chlamydomonas dataset. PCC7942 is relevant to the cited thylakoid experiments only; it cannot be silently substituted for the maintained PCC6803 example. No unmatched chloroplast species is substituted and catalogue absence is not biological absence. |
| plaque-adapter-meta | https://imodulondb.org/api/datasets/s_elongatus/elprecise300/meta; Dataset organism, strains, publication DOI, module/sample/gene counts | supports | elprecise300 explicitly names S.elongatus PCC7942 and DOI10.1073/pnas.2410492121. It is a computational expression dataset, not a membrane-localization or organelle-assembly experiment. |
| plaque-adapter-search-thylakoid | https://imodulondb.org/api/search?organism=s_elongatus&amp;dataset=elprecise300&amp;query=thylakoid&amp;limit=50; Actual bounded native search response; relevant gene IDs and module names only | supports | Bounded thylakoid search provides leads for representative PCC7942 photosynthetic gene/module cross-checks. A broad cytochrome-oxidase hit is not evidence about b6f; text-hit absence is not biological absence. |
| plaque-adapter-search-photosystem | https://imodulondb.org/api/search?organism=s_elongatus&amp;dataset=elprecise300&amp;query=photosystem&amp;limit=50; Actual bounded native search response; relevant gene IDs and module names only | supports | Bounded photosystem search provides leads for representative PCC7942 photosynthetic gene/module cross-checks. A broad cytochrome-oxidase hit is not evidence about b6f; text-hit absence is not biological absence. |
| plaque-adapter-search-cytochrome | https://imodulondb.org/api/search?organism=s_elongatus&amp;dataset=elprecise300&amp;query=cytochrome&amp;limit=50; Actual bounded native search response; relevant gene IDs and module names only | supports | Bounded cytochrome search provides leads for representative PCC7942 photosynthetic gene/module cross-checks. A broad cytochrome-oxidase hit is not evidence about b6f; text-hit absence is not biological absence. |
| plaque-adapter-search-ATP-synthase | https://imodulondb.org/api/search?organism=s_elongatus&amp;dataset=elprecise300&amp;query=ATP+synthase&amp;limit=50; Actual bounded native search response; relevant gene IDs and module names only | supports | Bounded ATP-synthase search provides leads for representative PCC7942 photosynthetic gene/module cross-checks. A broad cytochrome-oxidase hit is not evidence about b6f; text-hit absence is not biological absence. |
| plaque-adapter-gene-Synpcc7942_2049 | https://imodulondb.org/api/genes/s_elongatus/elprecise300/Synpcc7942_2049/imodulons; Exact gene-to-module endpoint; all57 returned membership flags, thresholds and selected weights | supports | psaA is above threshold only in module38 Photosystems: weight0.076674881 versus threshold0.063088206. These are bounded computational context results; no localization, essentiality or cross-strain inference follows. |
| plaque-adapter-gene-Synpcc7942_0424 | https://imodulondb.org/api/genes/s_elongatus/elprecise300/Synpcc7942_0424/imodulons; Exact gene-to-module endpoint; all57 returned membership flags, thresholds and selected weights | supports | psbA1 has no above-threshold membership among the57 returned modules; this is not absence of the gene, PSII or function. These are bounded computational context results; no localization, essentiality or cross-strain inference follows. |
| plaque-adapter-gene-Synpcc7942_2331 | https://imodulondb.org/api/genes/s_elongatus/elprecise300/Synpcc7942_2331/imodulons; Exact gene-to-module endpoint; all57 returned membership flags, thresholds and selected weights | supports | petB is above threshold only in module38 Photosystems: weight0.071675474 versus threshold0.063088206. These are bounded computational context results; no localization, essentiality or cross-strain inference follows. |
| plaque-adapter-gene-Synpcc7942_0336 | https://imodulondb.org/api/genes/s_elongatus/elprecise300/Synpcc7942_0336/imodulons; Exact gene-to-module endpoint; all57 returned membership flags, thresholds and selected weights | supports | atpA has no above-threshold membership among the57 returned modules; this does not refute ATP synthase membership or function. These are bounded computational context results; no localization, essentiality or cross-strain inference follows. |
| plaque-adapter-module-38 | https://imodulondb.org/api/imodulons/s_elongatus/elprecise300/38; Native module metadata: name, function_description, threshold, n_genes and regulator; generated summaries excluded | supports | Module38 provides bounded photosynthetic-expression context with 44 members. Labels are computational annotations, not evidence that every member resides in a thylakoid or forms a physical complex. |
| plaque-adapter-module-38-genes | https://imodulondb.org/api/imodulons/s_elongatus/elprecise300/38/genes?limit=50; Native member list requested limit50; all returned gene IDs, names, weights and in_imodulon flags; no generated prose | supports | All 44 returned rows are above-threshold members. Module38 includes psaA/psaB, several PSII genes and petB/petD; module1 includes selected PSII and b6f genes. This validates specific computational membership only, not complete complex inventories. |
| plaque-adapter-module-1 | https://imodulondb.org/api/imodulons/s_elongatus/elprecise300/1; Native module metadata: name, function_description, threshold, n_genes and regulator; generated summaries excluded | supports | Module1 provides bounded photosynthetic-expression context with 21 members. Labels are computational annotations, not evidence that every member resides in a thylakoid or forms a physical complex. |
| plaque-adapter-module-1-genes | https://imodulondb.org/api/imodulons/s_elongatus/elprecise300/1/genes?limit=50; Native member list requested limit50; all returned gene IDs, names, weights and in_imodulon flags; no generated prose | supports | All 21 returned rows are above-threshold members. Module38 includes psaA/psaB, several PSII genes and petB/petD; module1 includes selected PSII and b6f genes. This validates specific computational membership only, not complete complex inventories. |
| plaque-adapter-publication | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1073/pnas.2410492121&amp;format=json&amp;resultType=core&amp;pageSize=5; Exact DOI query; primary abstract and bibliographic identity only | supports | The cited elprecise300 paper decomposes300 PCC7942 RNA-seq datasets into57 independently modulated gene sets. Its abstract supports the computational provenance and photosynthesis context, not membrane localization, growth essentiality or biological absence. |
| plaque-historical-runner | /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources imodulondb datasets; Historical00:49Z receipt and stdout/stderr independently reread and hash-verified; no fresh invocation | context_only | The historical runner exited1 before dataset execution due OS PermissionError reading pyvenv.cfg. Current independently fetched source endpoints are the permitted fallback; source success is not runner execution. |
| plaque-native-bacterial_thylakoid-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/bacterial_thylakoid.yaml --verify; Actual root-owned receipt and exact stdout log independently read and hash-verified | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| plaque-native-bacterial_thylakoid-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/bacterial_thylakoid.yaml --causal-graphs; Actual root-owned receipt and exact stdout log independently read and hash-verified | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| plaque-native-chloroplast_inner_membrane-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chloroplast_inner_membrane.yaml --verify; Actual root-owned receipt and exact stdout log independently read and hash-verified | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| plaque-native-chloroplast_inner_membrane-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chloroplast_inner_membrane.yaml --causal-graphs; Actual root-owned receipt and exact stdout log independently read and hash-verified | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| plaque-native-chloroplast_intermembrane_space-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chloroplast_intermembrane_space.yaml --verify; Actual root-owned receipt and exact stdout log independently read and hash-verified | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| plaque-native-chloroplast_intermembrane_space-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chloroplast_intermembrane_space.yaml --causal-graphs; Actual root-owned receipt and exact stdout log independently read and hash-verified | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| micro-review-policy | .claude/skills/review-yaml-record/SKILL.md; Evidence Rules; Structured Source Cross-Checks; Missing Things; Workflow | supports | Native read-only source review. Named genes/proteins/pathways/stress responses trigger applicability assessment, independent of an expression claim. Catalogue absence is not negative biological evidence. |
| micro-review-config | conf/record_review.yaml; version1 review skills, rubrics and repository routing | supports | The current frozen configuration, skill and profile were reread; the seventeen common policy/schema/verifier inputs are unchanged from the prior independently reviewed cohort. No additional local scientific record was used outside the four assigned frozen targets. |
| micro-review-profile | docs/record-review-profile.md; Required scientific coverage; verdict and native validation profile | supports | Separate scientific curation from review-bundle repairs; retain immutable observations and native scope/severity. A new issue-bearing batch may contain supported clean target assessments. |
| micro-graph-contract | .claude/skills/curate-causal-graphs/SKILL.md; Graph scope, evidence and necessity contract | supports | Coarse NONMECHANISTIC functional/topological graphs must not be treated as complete mechanistic models. Protein identity, localization, functional dependency and constituent essentiality are different claims. |
| micro-review-schema | schema/record_review.yaml; EvidenceKind; Support; Area; AssessmentOutcome; FindingReference | supports | Secondary literature is explicitly labeled and encoded authority/context_only; schema is the permitted assessment area; every predecessor identifies repository, review and finding. |
| micro-original-validation-inputs | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/adversary-microtubule/original-validation-inputs.json; Four exact original native validate/render runs and original-source git blob hashes | supports | All four original bundles validate; native render --content equals original Markdown byte for byte. Original frozen target hashes match original source revision9c0446c4. Current autophagosome and chitosome hashes differ; lumen and membrane match. Historical commands are not recast as current-head whole-corpus tests. |
| micro-record-autophagosome | data/structures/membrane_organelle/autophagosome.yaml; Entire current YAML at e721920f30c72a6c35cecb9913c6780e18a460ed | supports | Current complete record inspected, including identity, components, functions, graph nodes/edges, scope notes, taxon examples, discussions, citations and curation history; changed from frozen original input. |
| micro-prior-autophagosome | reviews/structured/20261021T110741Z-autophagosome-audit/review.yaml; Entire immutable YAML and deterministic Markdown; findings, actions, checks and frozen source | supports | Original 20261021T110741Z-autophagosome-audit retained without mutation. Original verdict pass_with_limitations; 0 original scientific finding(s). Current reassessment does not rewrite original access dates or global-check provenance. |
| micro-native-autophagosome-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/autophagosome-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/autophagosome.yaml --verify; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/autophagosome-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0 at source e721920f30c72a6c35cecb9913c6780e18a460ed, 2026-11-03T09:32:44.624086+00:00 to 2026-11-03T09:32:45.016091+00:00. Empty protein-example inventory and zero GENE_OR_PROTEIN nodes; this is a successful empty-scope structural check, not experimental protein evidence. Identity/coverage success does not establish membership or necessity. |
| micro-native-autophagosome-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/autophagosome-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/autophagosome.yaml --causal-graphs; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/autophagosome-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Actual exit0 at source e721920f30c72a6c35cecb9913c6780e18a460ed, 2026-11-03T09:32:45.045818+00:00 to 2026-11-03T09:32:45.428758+00:00. Empty protein-example inventory and zero GENE_OR_PROTEIN nodes; this is a successful empty-scope structural check, not experimental protein evidence. Identity/coverage success does not establish membership or necessity. |
| micro-record-autophagosome_lumen | data/structures/membrane_organelle/autophagosome_lumen.yaml; Entire current YAML at e721920f30c72a6c35cecb9913c6780e18a460ed | supports | Current complete record inspected, including identity, components, functions, graph nodes/edges, scope notes, taxon examples, discussions, citations and curation history; identical to frozen original input. |
| micro-prior-autophagosome_lumen | reviews/structured/20261021T110744Z-autophagosome-lumen-audit/review.yaml; Entire immutable YAML and deterministic Markdown; findings, actions, checks and frozen source | supports | Original 20261021T110744Z-autophagosome-lumen-audit retained without mutation. Original verdict pass_with_limitations; 0 original scientific finding(s). Current reassessment does not rewrite original access dates or global-check provenance. |
| micro-native-autophagosome_lumen-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/autophagosome_lumen-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/autophagosome_lumen.yaml --verify; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/autophagosome_lumen-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0 at source e721920f30c72a6c35cecb9913c6780e18a460ed, 2026-11-03T09:32:45.458837+00:00 to 2026-11-03T09:32:45.851535+00:00. Empty protein-example inventory and zero GENE_OR_PROTEIN nodes; this is a successful empty-scope structural check, not experimental protein evidence. Identity/coverage success does not establish membership or necessity. |
| micro-native-autophagosome_lumen-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/autophagosome_lumen-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/autophagosome_lumen.yaml --causal-graphs; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/autophagosome_lumen-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Actual exit0 at source e721920f30c72a6c35cecb9913c6780e18a460ed, 2026-11-03T09:32:45.882420+00:00 to 2026-11-03T09:32:46.264565+00:00. Empty protein-example inventory and zero GENE_OR_PROTEIN nodes; this is a successful empty-scope structural check, not experimental protein evidence. Identity/coverage success does not establish membership or necessity. |
| micro-record-autophagosome_membrane | data/structures/membrane_organelle/autophagosome_membrane.yaml; Entire current YAML at e721920f30c72a6c35cecb9913c6780e18a460ed | supports | Current complete record inspected, including identity, components, functions, graph nodes/edges, scope notes, taxon examples, discussions, citations and curation history; identical to frozen original input. |
| micro-prior-autophagosome_membrane | reviews/structured/20261021T110747Z-autophagosome-membrane-audit/review.yaml; Entire immutable YAML and deterministic Markdown; findings, actions, checks and frozen source | supports | Original 20261021T110747Z-autophagosome-membrane-audit retained without mutation. Original verdict pass_with_limitations; 0 original scientific finding(s). Current reassessment does not rewrite original access dates or global-check provenance. |
| micro-native-autophagosome_membrane-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/autophagosome_membrane-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/autophagosome_membrane.yaml --verify; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/autophagosome_membrane-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0 at source e721920f30c72a6c35cecb9913c6780e18a460ed, 2026-11-03T09:32:46.295572+00:00 to 2026-11-03T09:32:46.690900+00:00. Empty protein-example inventory and zero GENE_OR_PROTEIN nodes; this is a successful empty-scope structural check, not experimental protein evidence. Identity/coverage success does not establish membership or necessity. |
| micro-native-autophagosome_membrane-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/autophagosome_membrane-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/autophagosome_membrane.yaml --causal-graphs; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/autophagosome_membrane-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Actual exit0 at source e721920f30c72a6c35cecb9913c6780e18a460ed, 2026-11-03T09:32:46.720855+00:00 to 2026-11-03T09:32:47.107463+00:00. Empty protein-example inventory and zero GENE_OR_PROTEIN nodes; this is a successful empty-scope structural check, not experimental protein evidence. Identity/coverage success does not establish membership or necessity. |
| micro-record-chitosome | data/structures/membrane_organelle/chitosome.yaml; Entire current YAML at e721920f30c72a6c35cecb9913c6780e18a460ed | supports | Current complete record inspected, including identity, components, functions, graph nodes/edges, scope notes, taxon examples, discussions, citations and curation history; changed from frozen original input. |
| micro-prior-chitosome | reviews/structured/20261021T110752Z-chitosome-audit/review.yaml; Entire immutable YAML and deterministic Markdown; findings, actions, checks and frozen source | supports | Original 20261021T110752Z-chitosome-audit retained without mutation. Original verdict needs_curation; 1 original scientific finding(s). Current reassessment does not rewrite original access dates or global-check provenance. |
| micro-native-chitosome-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/chitosome-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chitosome.yaml --verify; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/chitosome-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0 at source e721920f30c72a6c35cecb9913c6780e18a460ed, 2026-11-03T09:32:47.989875+00:00 to 2026-11-03T09:32:49.169761+00:00. Two reviewed protein examples CHS1/P08004 and CHS3/P29465; one GENE_OR_PROTEIN node COVERED by the same component examples. Identity/coverage success does not establish membership or necessity. |
| micro-native-chitosome-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/chitosome-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chitosome.yaml --causal-graphs; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/chitosome-uniprot-causal.log SHA256 4e39579edbac102eb474e951a3f5210ea7d1bbe4ce137cc84e38915fca388d63 | supports | Actual exit0 at source e721920f30c72a6c35cecb9913c6780e18a460ed, 2026-11-03T09:32:49.201704+00:00 to 2026-11-03T09:32:49.595030+00:00. Two reviewed protein examples CHS1/P08004 and CHS3/P29465; one GENE_OR_PROTEIN node COVERED by the same component examples. Identity/coverage success does not establish membership or necessity. |
| micro-auto-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005776,GO:0000421,GO:0034423,GO:0060205,GO:0030659,GO:0016236,GO:0061909,GO:0000324; Exact QuickGO term records GO:0005776/0000421/0034423/0060205/0030659/0016236/0061909/0000324; names, definitions, synonyms, active status and children | supports | Active exact terms distinguish autophagosome, its membrane and lumen, macroautophagy, fusion and fungal vacuole. GO:0016236 proceeds through autophagosome formation. GO:0061909 explicitly includes the yeast vacuole endpoint. Synonym scopes and resident-lumen annotation caution are retained. |
| micro-auto-SL-0022-json | https://rest.uniprot.org/locations/SL-0022.json; UniProt subcellular location SL-0022 definition, synonyms, geneOntologies, isA and partOf | supports | Autophagosome membrane maps to GO:0000421; the three record synonyms are supplied; isA cytoplasmic vesicle membrane and partOf autophagosome support the modeled relations. These are UniProt assertions, not claims about current direct GO parentage. |
| micro-auto-SL-0318-json | https://rest.uniprot.org/locations/SL-0318.json; UniProt subcellular location SL-0318 definition, synonyms, geneOntologies, isA and partOf | supports | Autophagosome lumen maps to GO:0034423; its three synonyms, isA cytoplasmic vesicle lumen and partOf autophagosome are explicit. Degradation cargo is not inferred to be a constitutive lumen component. |
| micro-auto-taxon-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; ENA taxonomy exact4932 scientificName/rank/lineage | supports | NCBITaxon:4932 is Saccharomyces cerevisiae at species rank, within Fungi. It is distinct from the narrower S288C strain identifier. |
| micro-auto-takeshige1992-xml | https://pmc-oa-opendata.s3.amazonaws.com/PMC2289660.1/PMC2289660.1.xml; DOI10.1083/jcb.119.2.301; JATS abstract; OCR Introduction, Methods, initial Results on body appearance and starvation conditions; complete Discussion | supports | Yeast proteinase-deficient and PMSF-treated wild-type experiments support starvation-associated vacuolar autophagic bodies and cytoplasmic cargo delivery. The Discussion explicitly leaves body-formation mechanism unresolved; this paper alone is not a direct molecular fusion assay. OCR text inspected; no figure pixels or raw data inspected. |
| micro-auto-suzuki2001-publisher | https://www.embopress.org/doi/full/10.1093/emboj/20.21.5971; DOI10.1093/emboj/20.21.5971; publisher Abstract, Introduction, Results PAS/localization and genetic grouping, Discussion Sec8, Methods Sec11 | supports | Physiological fluorescent fusions, mutant localization and autophagy assays support budding yeast as a genetic/fluorescence model and distinguish PAS organization from mature autophagosomes. APG protein participation is not a universal mature-organelle membership or stoichiometry claim. Selected Results narratives and complete Discussion/Methods inspected; no figure pixels. |
| micro-auto-xie2007-publisher | https://www.nature.com/articles/ncb1007-1102; DOI10.1038/ncb1007-1102; publisher title and complete abstract only | context_only | Secondary review abstract supplies context for double-membrane autophagosome formation and core machinery. No current full-body or PDF access is claimed; broad context is not independent experimental validation. |
| micro-auto-ichimura2000-publisher | https://www.nature.com/articles/35044114; DOI10.1038/35044114; publisher title and complete abstract only | partial | Primary abstract establishes Apg8 conjugation to phosphatidylethanolamine through a ubiquitin-like system. Supports the bounded lipidation TODO context, not a complete current protein inventory or inspected full methods. |
| micro-chito-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0045009,GO:0031410,GO:0005886,GO:0030428; QuickGO exact GO:0045009/0031410/0005886/0030428 active records, definitions and children | supports | Chitosome is a membrane-bounded fungal chitin-synthase particle/cytoplasmic vesicle with a proposed reservoir-to-septum role. Plasma membrane and cell septum graph endpoints are active correctly named terms; regulated septum delivery remains proposed. |
| micro-chito-go-parts | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030661,GO:0033162; QuickGO exact GO:0030661 name/definition/isObsolete and GO:0045009 child relation in paired chito-go response | supports | GO:0030661 is the active exact chitosome membrane term, defined as the lipid bilayer surrounding a chitosome. GO:0045009 lists it through part_of. This contradicts the current no-exact-membrane-term rationale; unrelated queried GO:0033162 is not used for a record inference. |
| micro-chito-chebi17029 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17029; OLS ChEBI exact17029 embedded term, label, definition, ontology identifier and obsolete flag | supports | CHEBI:17029 denotes chitin, a beta(1→4)-linked N-acetyl-D-glucosamine polymer. The graph represents a synthesis product, not a resident chitosome constituent. |
| micro-chito-tax-4751 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4751; ENA exact4751 scientificName/rank/lineage | supports | NCBITaxon:4751 denotes Fungi; authority identity does not establish universal structure occurrence. |
| micro-chito-tax-559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; ENA exact559292 scientificName/rank/lineage | supports | NCBITaxon:559292 denotes Saccharomyces cerevisiae S288C at strain rank; the related pathway and protein examples use this narrower scope. |
| micro-chito-leal1988-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1073%2Fpnas.85.22.8516&amp;format=json&amp;resultType=core; DOI10.1073/pnas.85.22.8516 exact Europe PMC core result: title and complete abstract | partial | Primary abstract resolves low-density chitosome and plasma-membrane populations from yeast homogenates, with mostly zymogenic synthase and unresolved ultimate active-enzyme location. Supports vesicle distinction, not a demonstrated universal delivery/activation mechanism. Full primary body and figure pixels not inspected. |
| micro-chito-jats-PMC2132460 | https://pmc-oa-opendata.s3.amazonaws.com/PMC2132460.1/PMC2132460.1.xml; DOI10.1083/jcb.136.1.95; JATS abstract, Methods yeast strains/tagging/immunofluorescence, Results Chs3 glycosylation/polarization/Chs5/mating and all five Discussion subsections | supports | Functional tagged Chs3 localization and chs5/myo2 perturbations support polarized yeast cell-surface targeting. The discussion treats late/post-Golgi patch identities and detailed transport models as hypotheses. Read claim-bearing text; no figure pixels, raw images or supplemental data examined. |
| micro-chito-ziman1998-browser-discussion | https://pmc.ncbi.nlm.nih.gov/articles/PMC25385/; DOI10.1091/mbc.9.6.1565; complete PMC primary abstract, Introduction, Methods, Results narratives and Discussion | supports | Chs6-dependent Chs3 anterograde transport supports the new plasma-membrane delivery endpoint. Chs1 traffic differs; activation alternatives remain unresolved in Discussion. The new NONMECHANISTIC edge is accepted for delivery purpose, not as proof transport alone activates every fungal synthase. No figure-pixel inspection. |
| micro-chito-bartnicki2006-pdf | https://www.davidmoore.org.uk/21st_Century_Guidebook_to_Fungi_PLATINUM/REPRINT_collection/Bartnicki-Garcia_chitosomes2006.pdf; DOI10.1111/j.1567-1364.2006.00158.x; genuine downloaded PDF, extracted text pp957–964 through Conclusion; captions text only | context_only | Secondary minireview covers fungal chitosome evidence, zymogenicity, delivery, opposing interpretations of endocytic origin and unresolved ontogeny/activation. It supports bounded multi-lineage context, not a universal fungal frequency or settled biogenesis mechanism. PDF text read; embedded pixels not inspected. |
| micro-chito-P08004 | https://rest.uniprot.org/uniprotkb/P08004.json; UniProtKB complete entry: accession/status/gene/taxon; function and subcellular-location comments and evidence references | supports | P08004 is the reviewed S288C entry for CHS1. Identity is distinct from chitosome membership or essentiality. CHS1 is distinct from CHS3 and does not inherit its Chs6-dependent trafficking result. |
| micro-chito-P29465 | https://rest.uniprot.org/uniprotkb/P29465.json; UniProtKB complete entry: accession/status/gene/taxon; function and subcellular-location comments and evidence references | supports | P29465 is the reviewed S288C entry for CHS3. Identity is distinct from chitosome membership or essentiality. P29465 Cell membrane annotations cite all three record PMIDs; these are not relabeled as chitosome-localization experiments. |
| micro-chito-reviewed-uniqueness | https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A559292+AND+%28gene_exact%3ACHS1+OR+gene_exact%3ACHS3%29&amp;format=json&amp;size=500; UniProt REST reviewed S288C exact gene-symbol query, two results and response pagination metadata | supports | The bounded reviewed S288C query returns one CHS1/P08004 and one CHS3/P29465 entry. This verifies uniqueness within that query, not across all fungi or unreviewed entries. |
| micro-chito-PMID-12928491 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12928491+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact cited PMID Europe PMC core record; title, author/year and complete abstract | partial | Primary abstract reports stress-responsive Rho1/Pkc1-dependent Chs3 mobilization from internal stores to plasma membrane. The actual UniProt Cell membrane reference matches; body, methods and image data were not inspected. |
| micro-chito-PMID-17519287 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A17519287+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact cited PMID Europe PMC core record; title, author/year and complete abstract | partial | Primary abstract separates Chs3 delivery from productive Chs4-associated plasma-membrane activity and rapid endocytosis. The actual UniProt Cell membrane reference matches; body, methods and image data were not inspected. |
| micro-chito-PMID-28346351 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A28346351+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact cited PMID Europe PMC core record; title, author/year and complete abstract | partial | Primary abstract supports Chs3 membrane organization and oligomeric/localization study scope. The actual UniProt Cell membrane reference matches; body, methods and image data were not inspected. |
| micro-chito-IPR004835 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004835/; InterPro entry metadata, family description and cross-family scope | supports | IPR004835 Chitin synthase is a broad family across fungi and animals; its existence does not itself prove every chitosome biochemical cargo class is one exact curated fungal family. |
| micro-chito-ipr-matches-P08004 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P08004/?page_size=200; InterPro protein-entry match list, count3, next=null, type and accession for each result | supports | The declared example maps to IPR004835 Chitin synthase, with additional domain/superfamily matches. This confirms example-family membership; it neither localizes all family members to chitosomes nor determines a universal isoenzyme cohort. |
| micro-chito-ipr-matches-P29465 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P29465/?page_size=200; InterPro protein-entry match list, count3, next=null, type and accession for each result | supports | The declared example maps to IPR004835 Chitin synthase, with additional domain/superfamily matches. This confirms example-family membership; it neither localizes all family members to chitosomes nor determines a universal isoenzyme cohort. |
| micro-pathway-commit | https://raw.githubusercontent.com/CultureBotAI/PathwayMech/d8ec2b69f7a4c615aecddff80498fef1e1fab0ce/data/pathways/chitin-biosynthesis.yaml; Exact remote PathwayMech commit d8ec2b69f7a4c615aecddff80498fef1e1fab0ce; pathway id/taxon/participants and CHS3 enables edge003 | supports | The declared chitin-biosynthesis model exists at the pinned public commit, taxon559292; CHS3 SGD:S000000227 is an explicit participant enabling a chitin-synthase reaction. The link is enzyme delivery, not catalysis inside chitosomes. Remote model bytes inspected; no local sibling-repository input was used. |
| micro-adapter-catalogue | https://imodulondb.org/api/datasets; Complete iModulonDB /api/datasets response, all20 organism rows/28 organism-dataset pairs | supports | Fresh catalogue inspection finds no Saccharomyces or other fungal organism/dataset match. No supported organism key is available for a target-specific downstream gene/module query; this is database coverage only, not absence of the proteins/pathways. |
| micro-historical-adapter-runner | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Retained actual imodulondb datasets runner receipt from 00:49Z; command, timestamps, exit1 and PermissionError reason | context_only | Historical runner attempt 2026-11-03T00:49:00.848907Z–00:49:00.863225Z failed because pyvenv.cfg could not be read. This retained receipt is not a new run or evidence of current service failure; the fresh inspected source catalogue is the present fallback. |
| septin-native-review-policy | .claude/skills/review-yaml-record/SKILL.md; Structured Source Cross-Checks and native immutable review workflow | supports | Named genes, accessions and pathways require applicability assessment; lack of expression claims does not exempt a target. Unmatched organism coverage permits bounded downstream non-applicability. Review-only source capture and append-only successor workflow apply. |
| septin-native-curation-policy | docs/CURATION.md; Identity, component boundaries, evidence and necessity | supports | Exact structure identity, class-level components, representative proteins, localizations, functions and structure-formation dependencies require distinct evidence. |
| septin-native-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Graph kinds, NONMECHANISTIC scope and protein evidence contract | supports | Topology graphs may retain stated coarse scope; a protein xref still must identify the represented actor. Identifier success does not prove localization or mechanism. |
| septin-record-apicoplast_membrane | data/structures/membrane_organelle/apicoplast_membrane.yaml; Entire current maintained record at e721920f30c72a6c35cecb9913c6780e18a460ed | supports | Full identity, history, components, necessity, taxonomy, functions, evidence, graph and discussions inspected. No attached image exists in this record. |
| septin-original-apicoplast_membrane | reviews/structured/20261021T110736Z-apicoplast-membrane-audit/review.yaml; Entire original YAML and paired deterministic Markdown | supports | Original findings, curation requests, verdict, evidence scopes, frozen input and check disclosures inspected without changing the original artifact. |
| septin-original-validation-apicoplast_membrane | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/adversary-septin/original-checks.json; 20261021T110736Z-apicoplast-membrane-audit validate and render --content; original/source/current target hashes | supports | Native validation and render exit 0; rendered Markdown byte-identical. Current record equals original frozen target hash, which also matches the original source revision. Schema validity does not certify scientific claims. |
| septin-native-apicoplast_membrane-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/apicoplast_membrane-uniprot-verify-receipt.json; Exact root-run command, timestamps, source head and stdout hash; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/apicoplast_membrane-uniprot-verify.log | supports | Command exited 0 at 2026-11-03T09:32:44.174280+00:00. No protein_examples are declared; three graph UniProt xrefs resolve. Causal audit reports exactly two UNANCHORED_WITH_UNIPROT nodes and zero covered component_ref nodes. It does not validate the Der1 paralog localization. |
| septin-native-apicoplast_membrane-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/apicoplast_membrane-uniprot-causal-receipt.json; Exact root-run command, timestamps, source head and stdout hash; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/apicoplast_membrane-uniprot-causal.log | supports | Command exited 0 at 2026-11-03T09:32:44.594381+00:00. No protein_examples are declared; three graph UniProt xrefs resolve. Causal audit reports exactly two UNANCHORED_WITH_UNIPROT nodes and zero covered component_ref nodes. It does not validate the Der1 paralog localization. |
| septin-record-chloroplast | data/structures/membrane_organelle/chloroplast.yaml; Entire current maintained record at e721920f30c72a6c35cecb9913c6780e18a460ed | supports | Full identity, history, components, necessity, taxonomy, functions, evidence, graph and discussions inspected. No attached image exists in this record. |
| septin-original-chloroplast | reviews/structured/20261021T110755Z-chloroplast-audit/review.yaml; Entire original YAML and paired deterministic Markdown | supports | Original findings, curation requests, verdict, evidence scopes, frozen input and check disclosures inspected without changing the original artifact. |
| septin-original-validation-chloroplast | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/adversary-septin/original-checks.json; 20261021T110755Z-chloroplast-audit validate and render --content; original/source/current target hashes | supports | Native validation and render exit 0; rendered Markdown byte-identical. Current record equals original frozen target hash, which also matches the original source revision. Schema validity does not certify scientific claims. |
| septin-native-chloroplast-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/chloroplast-uniprot-verify-receipt.json; Exact root-run command, timestamps, source head and stdout hash; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/chloroplast-uniprot-verify.log | supports | Command exited 0 at 2026-11-03T09:32:50.019609+00:00. No protein_examples, UniProt protein xrefs or GENE_OR_PROTEIN graph nodes are declared. The causal inventory is empty (zero typed protein nodes); success does not validate molecular prose or TOC/TIC composition. |
| septin-native-chloroplast-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/chloroplast-uniprot-causal-receipt.json; Exact root-run command, timestamps, source head and stdout hash; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/chloroplast-uniprot-causal.log | supports | Command exited 0 at 2026-11-03T09:32:50.458099+00:00. No protein_examples, UniProt protein xrefs or GENE_OR_PROTEIN graph nodes are declared. The causal inventory is empty (zero typed protein nodes); success does not validate molecular prose or TOC/TIC composition. |
| septin-record-chloroplast_envelope | data/structures/membrane_organelle/chloroplast_envelope.yaml; Entire current maintained record at e721920f30c72a6c35cecb9913c6780e18a460ed | supports | Full identity, history, components, necessity, taxonomy, functions, evidence, graph and discussions inspected. No attached image exists in this record. |
| septin-original-chloroplast_envelope | reviews/structured/20261021T110757Z-chloroplast-envelope-audit/review.yaml; Entire original YAML and paired deterministic Markdown | supports | Original findings, curation requests, verdict, evidence scopes, frozen input and check disclosures inspected without changing the original artifact. |
| septin-original-validation-chloroplast_envelope | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/adversary-septin/original-checks.json; 20261021T110757Z-chloroplast-envelope-audit validate and render --content; original/source/current target hashes | supports | Native validation and render exit 0; rendered Markdown byte-identical. Current record equals original frozen target hash, which also matches the original source revision. Schema validity does not certify scientific claims. |
| septin-native-chloroplast_envelope-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/chloroplast_envelope-uniprot-verify-receipt.json; Exact root-run command, timestamps, source head and stdout hash; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/chloroplast_envelope-uniprot-verify.log | supports | Command exited 0 at 2026-11-03T09:32:50.909232+00:00. No protein_examples, UniProt protein xrefs or GENE_OR_PROTEIN graph nodes are declared. The causal inventory is empty (zero typed protein nodes); success does not validate molecular prose or TOC/TIC composition. |
| septin-native-chloroplast_envelope-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/chloroplast_envelope-uniprot-causal-receipt.json; Exact root-run command, timestamps, source head and stdout hash; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/chloroplast_envelope-uniprot-causal.log | supports | Command exited 0 at 2026-11-03T09:32:51.346119+00:00. No protein_examples, UniProt protein xrefs or GENE_OR_PROTEIN graph nodes are declared. The causal inventory is empty (zero typed protein nodes); success does not validate molecular prose or TOC/TIC composition. |
| septin-context-apicoplast | data/structures/membrane_organelle/apicoplast.yaml; Identity, membrane has_part and shared SELMA component only | supports | Whole-organelle boundary and shared B9PY98 context inspected. This is a distinct maintained target; no prior whole-organelle finding is closed or transferred wholesale. |
| septin-context-chloroplast_inner_membrane | data/structures/membrane_organelle/chloroplast_inner_membrane.yaml; Identity, definition, parent_structures and part_of only | supports | Frozen neighbor distinguishes the stroma-facing inner bilayer from the complete envelope and its intermembrane space. |
| septin-context-chloroplast_intermembrane_space | data/structures/membrane_organelle/chloroplast_intermembrane_space.yaml; Identity, definition, parent_structures and part_of only | supports | Frozen neighbor denotes the region between bilayers, not either bilayer or the stroma. |
| septin-apicoplast-membrane-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0160211,GO:0016020,GO:0020011; Exact QuickGO records GO:0160211, GO:0016020 and GO:0020011; definitions and typed child relations | supports | Exact apicoplast-membrane identity and broad membrane parent are distinct from the whole apicoplast; GO:0020011 explicitly has apicoplast membrane as part. |
| septin-root21-sources-chloroplast-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009507,GO:0009534,GO:0009535,GO:0009536,GO:0009570,GO:0009706,GO:0009707,GO:0009941,GO:0010006,GO:0015979,GO:0031897,GO:0045037,GO:0061927; Complete thirteen requested GO term records; names, definitions, obsolete flags and typed child relations | supports | Supports exact chloroplast/plastid identity, envelope/stroma/thylakoid topology, Toc/Tic and photosynthesis/import process identities; preserves part_of versus is_a relations. |
| septin-root21-sources-envelope-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009507,GO:0009526,GO:0009570,GO:0009706,GO:0009707,GO:0009941,GO:0010006,GO:0031897,GO:0031972,GO:0045037; Complete ten requested GO term records; definitions and typed child relations | supports | Envelope includes both bilayers and intermembrane space; plastid envelope is its parent, chloroplast its whole. Toc and Tic have exact outer/inner-envelope translocon identities. |
| septin-root21-sources-GO0061927 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0061927; GO:0061927 complete exact term definition | supports | TOC-TIC supercomplex I explicitly includes Toc75, Toc159, Toc34 and Tic110; it is not automatically exact for the divergent Jin Chlamydomonas assembly. |
| septin-root21-sources-ancestors-0009507 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009507/ancestors?relations=is_a,part_of; Complete requested ancestor closure with relations=is_a,part_of | supports | Ancestor closure is contextual support only; direct typed relations and definitions are separately inspected so is-a and parthood are not conflated. |
| septin-root21-sources-ancestors-0009941 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009941/ancestors?relations=is_a,part_of; Complete requested ancestor closure with relations=is_a,part_of | supports | Ancestor closure is contextual support only; direct typed relations and definitions are separately inspected so is-a and parthood are not conflated. |
| septin-root21-sources-NCBITaxon-33090 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/33090; Exact ENA taxonomy identity/rank/lineage and aliases | supports | Taxon 33090 resolves to Viridiplantae; the native lineage is Eukaryota; . Metadata supports identity, not universal presence. |
| septin-root21-sources-NCBITaxon-3055 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3055; Exact ENA taxonomy identity/rank/lineage and aliases | supports | Taxon 3055 resolves to Chlamydomonas reinhardtii; the native lineage is Eukaryota; Viridiplantae; Chlorophyta; core chlorophytes; Chlorophyceae; CS clade; Chlamydomonadales; Chlamydomonadaceae; Chlamydomonas; . Metadata supports identity, not universal presence. |
| septin-root21-sources-doi-10.1098_rstb.2009.0103 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1098/rstb.2009.0103; Europe PMC exact DOI core result: complete abstract, title, authors, journal, date and identifier fields | supports | Keeling 2010 is a secondary review; complete indexed abstract and bibliographic metadata support primary-plastid evolutionary context, with lineage/loss caveats. |
| septin-root21-sources-doi-10.1016_j.cell.2022.10.030 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.cell.2022.10.030; Europe PMC exact DOI core result: complete abstract, title, authors, journal, date and identifier fields | supports | Jin et al. 2022 primary study complete indexed abstract: Chlamydomonas 14-component complex spans both envelope membranes; Toc120/Toc75 hybrid barrel and a potential Tic20/YlmG path are connected across the intermembrane space. Abstract-level access is not a full Results or raw cryo-EM audit. |
| septin-root21-sources-doi-10.1007_s00294-011-0339-1 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1007/s00294-011-0339-1; Europe PMC exact DOI core result: complete abstract, title, authors, journal, date and identifier fields | supports | Terashima, Specht and Hippler 2011 secondary proteome review, complete indexed abstract and metadata: experimentally localized chloroplast protein set, comparative photosynthetic/metabolic context and Chlamydomonas/plant comparison. No fresh full PDF read is claimed. |
| septin-root21-sources-keeling2010-pmc | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2817223/; Genuine PMC secondary-review HTML: Abstract and section 1 origin/primary plastids, including two bounding membranes and green-algal/plant context; no image pixels | supports | Fresh body access confirms cyanobacterial primary-plastid origin and two-membrane topology in the explicitly discussed lineages. Historical broader evolutionary hypotheses elsewhere in this review are not recast as current experimental proof. |
| septin-root21-sources-jin2022-author-publications | https://lifesciences.westlake.edu.cn/labs/zhen-yan/structural-biology-laboratory/publications/; Author laboratory publication-list entry for Jin et al. 2022: title, author list, journal/DOI and complete study abstract only | supports | The author-hosted abstract corroborates the exact assembly, Chlamydomonas scope and potential inner-channel wording. This is neither a complete paper nor independent raw structural reanalysis. |
| septin-root21-sources-terashima2011-pdf | https://link.springer.com/content/pdf/10.1007/s00294-011-0339-1.pdf; HTTP 200 response body inspected: 3,038-byte HTML challenge, not PDF | supports | Publisher PDF route returned HTML rather than scientific content; the current review uses the complete native indexed abstract instead of claiming a successful full-body read. |
| septin-current-source-access-receipts | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/adversary-septin/source-receipts.json; Actual fresh requests, timestamps, HTTP status/content-type/hash; includes failed routes | supports | Jin publisher returned HTTP 403; Terashima nominal PDF returned challenge HTML. Keeling PMC body succeeded, though alternate API routes failed. These outcomes limit access claims and are not biological findings. |
| septin-current-adapter-catalogue | https://imodulondb.org/api/datasets; Complete official datasets response; every organism name/id and dataset list inspected | supports | Twenty listed organisms comprise 28 organism/dataset pairs and 22 distinct dataset-key strings. No listed organism matches Apicomplexa, Toxoplasma gondii, Plasmodium falciparum or their represented strains, Viridiplantae, or Chlamydomonas reinhardtii. Thus no target-matched downstream gene/module lookup applies. This is a database-coverage statement, not biological absence. |
| septin-historical-adapter-runner-unavailable | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical canary invocation at 2026-11-03T00:49:00.848907Z–00:49:00.863225Z | supports | Actual historical datasets runner exited 1 with PermissionError reading pyvenv.cfg. Receipt is reused; no fresh invocation is claimed. Current official-source fallback is separately fetched. |
| septin-apicoplast-agent-tax-5794 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5794; ENA taxonomy exact tax-id response: current name, aliases, rank and lineage | supports | Reused public-source snapshot, originally fetched at 2026-11-03T08:55:13.959999Z; no fresh network retrieval claimed. Native taxon 5794 is Apicomplexa; inspected name, rank, aliases and lineage. This establishes identity and strain/species context, not universal organelle presence. |
| septin-apicoplast-agent-tax-5811 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5811; ENA taxonomy exact tax-id response: current name, aliases, rank and lineage | supports | Reused public-source snapshot, originally fetched at 2026-11-03T08:55:14.075206Z; no fresh network retrieval claimed. Native taxon 5811 is Toxoplasma gondii; inspected name, rank, aliases and lineage. This establishes identity and strain/species context, not universal organelle presence. |
| septin-apicoplast-agent-tax-5833 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5833; ENA taxonomy exact tax-id response: current name, aliases, rank and lineage | supports | Reused public-source snapshot, originally fetched at 2026-11-03T08:55:14.170990Z; no fresh network retrieval claimed. Native taxon 5833 is Plasmodium falciparum; inspected name, rank, aliases and lineage. This establishes identity and strain/species context, not universal organelle presence. |
| septin-apicoplast-agent-tax-508771 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/508771; ENA taxonomy exact tax-id response: current name, aliases, rank and lineage | supports | Reused public-source snapshot, originally fetched at 2026-11-03T08:55:14.482604Z; no fresh network retrieval claimed. Native taxon 508771 is Toxoplasma gondii ME49; inspected name, rank, aliases and lineage. This establishes identity and strain/species context, not universal organelle presence. |
| septin-apicoplast-agent-tax-36329 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/36329; ENA taxonomy exact tax-id response: current name, aliases, rank and lineage | supports | Reused public-source snapshot, originally fetched at 2026-11-03T08:55:14.671962Z; no fresh network retrieval claimed. Native taxon 36329 is Plasmodium falciparum 3D7; inspected name, rank, aliases and lineage. This establishes identity and strain/species context, not universal organelle presence. |
| septin-apicoplast-agent-S8GBF3 | https://rest.uniprot.org/uniprotkb/S8GBF3.json; Native accession, entry status, organism/taxon, gene/ORF names, protein name, sequence and cross-reference fields | supports | Reused public-source snapshot, originally fetched at 2026-11-03T08:55:14.763108Z; no fresh network retrieval claimed. S8GBF3: UniProtKB unreviewed (TrEMBL); taxon 508771; native gene/ORF values TIC20, TGME49_255370. Identity/status metadata does not alone establish organelle membership. |
| septin-apicoplast-agent-O97275 | https://rest.uniprot.org/uniprotkb/O97275.json; Native accession, entry status, organism/taxon, gene/ORF names, protein name, sequence and cross-reference fields | supports | Reused public-source snapshot, originally fetched at 2026-11-03T08:55:14.979966Z; no fresh network retrieval claimed. O97275: UniProtKB unreviewed (TrEMBL); taxon 36329; native gene/ORF values PF3D7_0314300. Identity/status metadata does not alone establish organelle membership. |
| septin-apicoplast-agent-B9PY98 | https://rest.uniprot.org/uniprotkb/B9PY98.json; Native accession, entry status, organism/taxon, gene/ORF names, protein name, sequence and cross-reference fields | supports | Reused public-source snapshot, originally fetched at 2026-11-03T08:55:15.188599Z; no fresh network retrieval claimed. B9PY98: UniProtKB unreviewed (TrEMBL); taxon 5811; native gene/ORF values no native gene-name field. Identity/status metadata does not alone establish organelle membership. EMBL cross-reference is FJ976521/ACU32856.1, independently deposited as Der1ER1. |
| septin-apicoplast-agent-C9WWW6 | https://rest.uniprot.org/uniprotkb/C9WWW6.json; Native accession, entry status, organism/taxon, gene/ORF names, protein name, sequence and cross-reference fields | supports | Reused public-source snapshot, originally fetched at 2026-11-03T08:55:16.014524Z; no fresh network retrieval claimed. C9WWW6: UniProtKB unreviewed (TrEMBL); taxon 5811; native gene/ORF values no native gene-name field. Identity/status metadata does not alone establish organelle membership. EMBL cross-reference is FJ976520/ACU32855.1, independently deposited as apicoplast Der1; automated ER wording is not accepted as a replacement for primary localization. |
| septin-apicoplast-agent-matches-S8GBF3 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/S8GBF3/?page_size=200; Complete example-specific native InterPro matches response; accession/type/match positions and pagination inspected | supports | Reused public-source snapshot, originally fetched at 2026-11-03T08:55:18.399340Z; no fresh network retrieval claimed. Native example matches: IPR005691:family. Protein family, domain and homologous-superfamily types remain distinct; generated biological descriptions are not used. |
| septin-apicoplast-agent-matches-O97275 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/O97275/?page_size=200; Complete example-specific native InterPro matches response; accession/type/match positions and pagination inspected | supports | Reused public-source snapshot, originally fetched at 2026-11-03T08:55:19.035669Z; no fresh network retrieval claimed. Native example matches: IPR007599:family, IPR035952:homologous_superfamily. Protein family, domain and homologous-superfamily types remain distinct; generated biological descriptions are not used. |
| septin-apicoplast-agent-matches-B9PY98 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/B9PY98/?page_size=200; Complete example-specific native InterPro matches response; accession/type/match positions and pagination inspected | supports | Reused public-source snapshot, originally fetched at 2026-11-03T08:55:19.293895Z; no fresh network retrieval claimed. Native example matches: IPR007599:family, IPR035952:homologous_superfamily. Protein family, domain and homologous-superfamily types remain distinct; generated biological descriptions are not used. |
| septin-apicoplast-agent-jats-PMC3681736 | https://pmc-oa-opendata.s3.amazonaws.com/PMC3681736.1/PMC3681736.1.xml; Agrawal et al. 2013 JATS: Abstract, apicoplast enzyme localization/import experiments, Discussion including unresolved endogenous modifier paragraphs | supports | Reused public-source snapshot, originally fetched at 2026-11-03T08:55:23.487064Z; no fresh network retrieval claimed. Supports an apicoplast ubiquitylation-system import role and tested enzyme activity, while explicitly leaving endogenous ubiquitin versus ubiquitin-like modifier unresolved. Recombinant human ubiquitin is the tested in-vitro substrate. |
| septin-apicoplast-agent-jats-PMC3662607 | https://pmc-oa-opendata.s3.amazonaws.com/PMC3662607.1/PMC3662607.1.xml; Lemgruber et al. 2013 JATS: Abstract, Results four-membrane reconstructions, figure captions and Conclusions; no new pixel audit | supports | Reused public-source snapshot, originally fetched at 2026-11-03T08:55:23.544521Z; no fresh network retrieval claimed. Cryo-electron tomography of P. falciparum merozoites resolves four envelope membranes; local apposition explains slices apparently showing three. Supports the scoped membrane-boundary claim, not protein identities. |
| septin-apicoplast-agent-jats-PMC2817234 | https://pmc-oa-opendata.s3.amazonaws.com/PMC2817234.1/PMC2817234.1.xml; Lim and McFadden 2010 secondary review JATS: origin/envelope, targeting and metabolic pathway sections | supports | Reused public-source snapshot, originally fetched at 2026-11-03T08:55:23.770969Z; no fresh network retrieval claimed. Secondary review body supports four-membrane envelope and bipartite signal/transit targeting context. It is not a new primary localization or assembly experiment. |
| septin-apicoplast-agent-jats-PMC5406208 | https://pmc-oa-opendata.s3.amazonaws.com/PMC5406208.1/PMC5406208.1.xml; McFadden and Yeh 2017 secondary review JATS: apicoplast loss and stage-specific metabolic function sections | supports | Reused public-source snapshot, originally fetched at 2026-11-03T08:55:23.938665Z; no fresh network retrieval claimed. Secondary context supports variable apicomplexan presence including Cryptosporidium loss and life-stage distinctions. No universal family or life-stage metabolic requirement is inferred. |
| septin-apicoplast-agent-ena-FJ976521 | https://www.ebi.ac.uk/ena/browser/api/embl/FJ976521?download=false; ENA native flatfile DE/CDS product/protein_id and translation | supports | Reused public-source snapshot, originally fetched at 2026-11-03T08:55:24.022634Z; no fresh network retrieval claimed. FJ976521 explicitly names Der1ER1 and ACU32856.1; exact accession bridge to unreviewed B9PY98, the ER paralog. |
| septin-apicoplast-agent-ena-FJ976520 | https://www.ebi.ac.uk/ena/browser/api/embl/FJ976520?download=false; ENA native flatfile DE/CDS product/note/protein_id and translation | supports | Reused public-source snapshot, originally fetched at 2026-11-03T08:55:24.218558Z; no fresh network retrieval claimed. FJ976520 explicitly names apicoplast Der1/Der1Ap and ACU32855.1; exact accession bridge to unreviewed C9WWW6. Automated generic ER location in that UniProt entry is not substituted for the primary paralog evidence. |
| septin-apicoplast-agent-ena-CAB38986 | https://www.ebi.ac.uk/ena/browser/api/embl/CAB38986.4?download=false; Native sequence/locus metadata; exact gene and old-locus bridge only | supports | Reused public-source snapshot, originally fetched at 2026-11-03T08:55:24.473949Z; no fresh network retrieval claimed. Supports current O97275/CAB38986.4/PF3D7_0314300 and older PFC0590c identity bridge; the old identifier string and new locus name are not treated as identical literal strings. |
| septin-apicoplast-agent-gene-814456 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=gene&amp;id=814456&amp;retmode=json; Native sequence/locus metadata; exact gene and old-locus bridge only | supports | Reused public-source snapshot, originally fetched at 2026-11-03T08:55:24.497062Z; no fresh network retrieval claimed. Supports current O97275/CAB38986.4/PF3D7_0314300 and older PFC0590c identity bridge; the old identifier string and new locus name are not treated as identical literal strings. |
| septin-apicoplast-agent-kalanon2009-pdf | https://fad.webmate.me/McFadden_Lab/Mcfadden_Papers/2009/Kalanon_Euk_Cell_2009.pdf; Author-hosted Kalanon et al. 2009 PDF: Methods antibody peptide printed p.1148; PfsDer1 paralog Results/Table1/Fig.4 caption printed pp.1149–1152 | supports | Reused public-source snapshot, originally fetched at 2026-11-03T08:55:24.648334Z; no fresh network retrieval claimed. Separates PfsDer1-1 from PfsDer1-2/PFC0590c. Published anti-Der1-2 peptide IKDCVSKYTSRSSTNN occurs at residues303–318 of current O97275. Full-length Der1-1 localization experiments are not transferred to Der1-2. |
| septin-agrawal2011-thesis | https://openscholar.uga.edu/record/21126/files/agrawal_swati_201105_phd.pdf; Institutional author dissertation: Chapter 3 Methods printed p.46/PDF59 and Table3.1 p.81/PDF94; Appendix2 reprinted Tic20 primary study pp.176–188, especially pp.187–188/PDF200–201 | supports | Reused public-source snapshot, originally fetched at 2026-11-03T09:00:17.320297Z; no fresh network retrieval claimed. Author-reproduced primary studies distinguish ER Der1 FJ976521 from apicoplast Der1 FJ976520. Tic20 depletion leaves 65–77% wild-type import at day 2 but essentially completely inhibits import by day 4; the study explicitly considers accessory/regulatory alternatives to direct channel action. This supports localized import dependency without proving a pore mechanism. |
| check-qc | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/qc.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| check-labels | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/labels.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| check-trait-links | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/trait-links.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Native TraitMech link check passed. |
| check-vendored | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/vendored.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Pinned governed files match; native vendored check passed. |
| check-curies | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/curies.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| focused | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/focused-results.json; All twenty actual target schema/strict command outputs | supports | Ten schema and ten strict commands returned exit zero. |
| supplemental-pmid | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/pmid-chunks-receipt.json; Complete native-report PMID set checked with unchanged resolver in batches of at most fifty | supports | 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers remain unverified. |
| historical-adapter-runner-availability | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical runner invocation receipt, cross-checked against exact stdout/stderr hashes; reread during PR2358 synthesis | context_only | Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS PermissionError reading the configured runner pyvenv.cfg. This is a retained historical availability observation, not a fresh attempt or a scientific validation failure. Native policy permits inspected source-catalogue fallback. |

## Limits And Additional Notes

- Bacterial thylakoid, chloroplast inner membrane and intermembrane space independent subreview: All three target bytes are unchanged from the original reviews. Their source-grounded reassessment does not rewrite originals or record history.
- Bacterial thylakoid, chloroplast inner membrane and intermembrane space independent subreview: Casella2017 and Huokko2021 are inspected primary body text/selected captions at the explicit locators; figure pixels, supplementary raw data and exhaustive perturbation literature were not independently audited. AFM b6f assignment remains tentative.
- Bacterial thylakoid, chloroplast inner membrane and intermembrane space independent subreview: Perez2024 is secondary synthesis accessed through browser-returned indexed official publisher body; native landing/delivery attempts returned403. Only named returned sections are treated as read; no complete native-body retrieval is claimed.
- Bacterial thylakoid, chloroplast inner membrane and intermembrane space independent subreview: Keeling2010 selected secondary HTML body is accessible through PMC; failed JATS/S3/PDF/BioC routes do not negate that bounded fallback. Jin2022 biology is primary abstract only;7VCF metadata verifies linked species, not an experimental strain or complete paper inspection.
- Bacterial thylakoid, chloroplast inner membrane and intermembrane space independent subreview: Ontology-derived plasma-membrane attachment wording is not evidence of obligatory physical fusion or a universal cyanobacterial biogenesis mechanism. Individual assembly necessity remains unknown; collective bilayer identity is distinct.
- Bacterial thylakoid, chloroplast inner membrane and intermembrane space independent subreview: Historical adapter runner failure occurred00:49Z, not during this subreview. Fresh source endpoints are independently accessed fallback, not a new runner success. Catalogue coverage is exact organism/dataset context.
- Bacterial thylakoid, chloroplast inner membrane and intermembrane space independent subreview: Matched elprecise300 is PCC7942 experimental-source context, not maintained PCC6803 or chloroplast evidence. Four representative gene queries and two module summaries/member lists are bounded computational checks; below-threshold results do not show absence. Generated module prose is excluded.
- Bacterial thylakoid, chloroplast inner membrane and intermembrane space independent subreview: Sparse inner-membrane/IMS inventories do not require invented proteins. TOC–TIC prose nevertheless triggers a coverage assessment. Empty native protein inventories pass validity checks without proving membership or essentiality.
- Bacterial thylakoid, chloroplast inner membrane and intermembrane space independent subreview: All three targets declare no images; no target pixel assessment is claimed. Neighbor chloroplast/envelope records are used for boundaries only. Root owns corpus gates, issue deduplication/publication, repository writes and merge decisions.
- Autophagosome, lumen, membrane and chitosome independent subreview: Assigned scope only: four autophagy/chitosome records and their original review pairs. No whole-category finding resolution or scientific assessment of the other six targets is made by this report.
- Autophagosome, lumen, membrane and chitosome independent subreview: Source-specific current access: Takeshige1992 is OCR JATS abstract/selected body/Discussion; Suzuki2001 publisher selected Results and complete Discussion/Methods; Santos1997 selected claim-bearing primary Methods/Results/Discussion; Ziman1998 primary text narratives. No primary figure pixels, raw data or supplements were inspected.
- Autophagosome, lumen, membrane and chitosome independent subreview: Leal-Morales1988, Ichimura2000 and three CHS3 annotation PMIDs were assessed from exact primary abstracts only. Xie2007 was assessed from its secondary review abstract only. Bartnicki2006 was read as secondary PDF text through Conclusion, not an independent primary experiment.
- Autophagosome, lumen, membrane and chitosome independent subreview: Historical original-review evidence may have wider or narrower access than this fresh pass. Its dates and access tiers are not rewritten. Current source evidence rows retain their actual09:33Z fetch times, even when interpreted later.
- Autophagosome, lumen, membrane and chitosome independent subreview: The chitosome new delivery edge is accepted within its explicit NONMECHANISTIC scope; Chs3 transport experiments do not demonstrate activation of every fungal isoenzyme, sufficient activation by delivery alone, universal Chs6 dependence or a complete biogenesis route.
- Autophagosome, lumen, membrane and chitosome independent subreview: InterPro broad family membership of the two examples is not universal fungal cargo coverage. Native protein commands are empty-scope for all three autophagy records and cover only the two declared chitosome examples/one graph protein node.
- Autophagosome, lumen, membrane and chitosome independent subreview: iModulonDB no-match concerns only the complete dataset catalogue fetched2026-11-03T09:33:07Z and these fungal taxa. The retained runner failure was00:49Z, not a new invocation. No unsupported matched-organism gene or module search was invented.
- Autophagosome, lumen, membrane and chitosome independent subreview: Initial sandbox DNS failures were preserved under initial-dns-unavailable; permitted public-network retrieval then succeeded. Two guessed JATS routes returned404, while actual publisher/PMC alternatives supplied the documented primary text. These access failures are not successful source checks.
- Autophagosome, lumen, membrane and chitosome independent subreview: Root owns current whole-corpus QC, identifier/label/trait checks, issue deduplication, issue publication and final integration. This independent report inspected its eight actual focused native protein receipts and original-bundle validation; it does not claim to have rerun global gates.
- Apicoplast membrane, chloroplast and envelope independent subreview: Public apicoplast source snapshots are explicitly reused with their original 08:55Z or 09:00Z access timestamps and verified hashes; the source evidence is not represented as newly fetched. No prior immutable review bundle beyond these assigned original reviews was used.
- Apicoplast membrane, chloroplast and envelope independent subreview: Jin2022 current access is complete native indexed abstract and exact author-laboratory abstract entry; publisher body request returned403. No complete Results, supplementary material, raw cryo-EM data or experimental images were audited. The potential inner route remains source-model scope.
- Apicoplast membrane, chloroplast and envelope independent subreview: Terashima2011 current access is complete native abstract/bibliographic metadata. Its nominal PDF route returned HTML challenge, not a PDF. Keeling2010 was genuinely read at fresh PMC Abstract/section1 body scope and is a secondary review.
- Apicoplast membrane, chloroplast and envelope independent subreview: Tic20/Der1 primary support uses the institutional author dissertation reprints and exact deposited sequences; prior PMC challenge responses are not represented as successful full-body reads. TgTic20 import impairment is temporally resolved and does not prove direct pore action.
- Apicoplast membrane, chloroplast and envelope independent subreview: Kalanon2009 inspected Methods/selected Results/Table1/Fig4 caption; O97275/Der1-2 is not assigned the full-length Der1-1 experiments. No image pixels were reanalysed.
- Apicoplast membrane, chloroplast and envelope independent subreview: No claim of exhaustive constituent inventory, every import-machine class grounding, quantitative lipid composition or universal organelle formation dependency. Component necessity remains UNKNOWN in the chloroplast targets.
- Apicoplast membrane, chloroplast and envelope independent subreview: The official catalogue coverage assessment is bounded to its current complete response. No covered organism matches these targets; this is not biological absence. Historical runner failure at00:49Z is not a fresh run and is distinct from successful fresh source fallback.
- Apicoplast membrane, chloroplast and envelope independent subreview: Native checks validate exact declared identifiers and typed inventory only: two membrane UNANCHORED_WITH_UNIPROT nodes and empty chloroplast/envelope protein inventories. They do not resolve the wrong-paralog scientific finding.
- Apicoplast membrane, chloroplast and envelope independent subreview: The additional frozen apicoplast and inner-membrane/intermembrane-space records are boundary/identity context only. No whole-organelle or multi-target historical finding is marked resolved.
- Apicoplast membrane, chloroplast and envelope independent subreview: Root owns global QC/CI, issue deduplication/publication and final repository checks; this report performs no repository or GitHub mutation.
- Historical observations remain immutable; their old checks are not represented as current-head execution.
- The adapter runner was not rerun after the canary established OS access failure. Catalogue-based coverage is assessed directly; fresh and reused responses retain actual access timestamps.
- Native label checks include 923 no-adapter skips. Native identifier checks include 909 PMID transport failures and 254 skipped identifiers; bounded supplemental checks independently resolve the 909 PMIDs.
- Scientific record-curation findings stay in separate issues; no record is edited by this review PR.
- Final trusted-base post-save review-check, exact-head independent acceptance, final-head CI and merge-group CI occur after saving this immutable observation and are not represented here as already completed.
- All ten original YAML/Markdown pairs remain unchanged. Current main was merged normally and pushed without force.
- This explicit issue-bearing ten-record cohort follows the native persistence policy. Each inherited scientific finding retains exact predecessor identity.
- Issue #2652 tracks the autophagosome function grounding and chitosome cargo-delivery edge refreshes. Scientific record curation remains separately tracked and open. Existing validator #2514 remains open.
- Issue #2653 tracks three omitted applicability assessments and six unsupported expression-only exclusions. The sparse autophagosome lumen is a genuine topology exclusion.
- Source commit e721920f30c72a6c35cecb9913c6780e18a460ed is retained by tag review-base/pr2358-current-record-followup-20261103.
- CLAUDE.md is an alias of AGENTS.md; canonical regular AGENTS.md bytes are frozen.
- All used local context was frozen before assessment, including native configuration, graph/protein policies and verifier source. The whole-apicoplast neighbor is context only, not an additional target or a disposition of its findings.
- Fresh and reused public-source snapshots retain actual access dates and inspection tiers. Native authority identity does not independently establish localization, mechanistic action or assembly necessity.
- Native checks with empty protein inventories or zero GENE_OR_PROTEIN nodes do not validate molecules appearing only in narrative prose.
- The autophagosome macroautophagy identifier and chitosome cargo delivery are reassessed within their stated scopes. Chs3 transport evidence does not establish universal isoenzyme activation.
- All three original scientific findings remain open for separate record curation; no scientific finding is terminally resolved.
- Two major findings (apicoplast membrane Der1 paralog and bacterial thylakoid organism attribution) remain open as #2654 and #2655. The minor chitosome membrane grounding finding remains open as #2656. The seven targets without scientific findings retain qualified positive assessments; no record is edited.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T094445Z-pr2358-current-record-followup
kind: batch
repository: CultureBotAI/CellStructureMech
title: 'PR 2358: current-input review of ten records and adversarial follow-up'
started_at: '2026-11-03T09:31:38.879464Z'
finished_at: '2026-11-03T09:44:45Z'
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
summary: Current-input reassessment of all ten records in PR2358. Two stale reviews
  are substantively refreshed. Independent source assessments retain the three inherited
  scientific findings and correct nine structured-source applicability assessments
  without editing records.
source:
  git_revision: e721920f30c72a6c35cecb9913c6780e18a460ed
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
  - path: data/structures/membrane_organelle/apicoplast.yaml
    sha256: 00971d8425f63fc5d490907a43c00b6760c2d88c5413fce6bdbc2dd09919410e
    role: context
  - path: data/structures/membrane_organelle/apicoplast_membrane.yaml
    sha256: fb3e343e0ed2a8711dff2305abea2166c589cb0a7b169d291c67fed81990ca58
    role: target
  - path: data/structures/membrane_organelle/autophagosome.yaml
    sha256: 08c1df95826ee2cb8b86b66592876f324eae999c7cafdc619d1ffad1607f6232
    role: target
  - path: data/structures/membrane_organelle/autophagosome_lumen.yaml
    sha256: 33fbf9f3ae1591081dd1e113d0fd7476c64bdafaa238ec35c7705fb89bb0f98d
    role: target
  - path: data/structures/membrane_organelle/autophagosome_membrane.yaml
    sha256: aa651db3a9b5a208ae7a4deef9d3595d79c0296cda8ebdc9a1c524a11b948254
    role: target
  - path: data/structures/membrane_organelle/bacterial_thylakoid.yaml
    sha256: a134c6cf6fd6069f0a0ddc37f1e99ded9a32994b3b1fa16d2f9938e3e46b8c40
    role: target
  - path: data/structures/membrane_organelle/chitosome.yaml
    sha256: ec564f818b649f3c4c8a56de6d6bea798eded59e73f1c4b840325eb83b9d5493
    role: target
  - path: data/structures/membrane_organelle/chloroplast.yaml
    sha256: 4c13f5dadaeb23a88fabfc2b5ec65034ed0ac83cbca9d45143793618acf2e727
    role: target
  - path: data/structures/membrane_organelle/chloroplast_envelope.yaml
    sha256: 29da363489107536342db1782001be534ea54605039b80c201cba0a46de9468e
    role: target
  - path: data/structures/membrane_organelle/chloroplast_inner_membrane.yaml
    sha256: 05283f5252a6354d26bef1ff196b3a9e10fbd6e72e9a6ec17014330f7a28dbb3
    role: target
  - path: data/structures/membrane_organelle/chloroplast_intermembrane_space.yaml
    sha256: 7ab90f4d2f4c41c466e100d589fb1f1d42bf90ded515dea6db5575d54119d43a
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
  - path: reviews/structured/20261021T110736Z-apicoplast-membrane-audit/review.md
    sha256: edd10dc498383b5244d5cbe3667c522e7fc5bc73282412092691cf399ba48d0c
    role: context
  - path: reviews/structured/20261021T110736Z-apicoplast-membrane-audit/review.yaml
    sha256: 327d4a503051b00002667d41e48c0fea69c8f330e639efe0880099fa13c6d5c4
    role: context
  - path: reviews/structured/20261021T110741Z-autophagosome-audit/review.md
    sha256: 68583afd2e4eb6c932ed5a24eb7d9469959ae262832f710c70a229bfc7b5dca2
    role: context
  - path: reviews/structured/20261021T110741Z-autophagosome-audit/review.yaml
    sha256: 18417b1f2d56272090dd09e3eb52dab6c976ec104e8cfce11319408847dccbb4
    role: context
  - path: reviews/structured/20261021T110744Z-autophagosome-lumen-audit/review.md
    sha256: bfcf0a25f0264d5de15c61446bd336e0d86c9f6f9faa11e2de4c0e01eb1b43fc
    role: context
  - path: reviews/structured/20261021T110744Z-autophagosome-lumen-audit/review.yaml
    sha256: 6f417e89968139de6fc68836753c3ed68851e18f30bd98b3211ed692400e51ad
    role: context
  - path: reviews/structured/20261021T110747Z-autophagosome-membrane-audit/review.md
    sha256: b81862bfa5f937731b3d342ba894502d5d906e255b59bca1c17be9e4029c43b1
    role: context
  - path: reviews/structured/20261021T110747Z-autophagosome-membrane-audit/review.yaml
    sha256: 64f2d8ab01bf1550f71fcbf450bee87417f10e5edc36d6532f097e4098ad8ab0
    role: context
  - path: reviews/structured/20261021T110749Z-bacterial-thylakoid-audit/review.md
    sha256: 8a411eb0087b471d41bf81eb7922f60bb62b85a838da0acbcdbca093e0bd3eb2
    role: context
  - path: reviews/structured/20261021T110749Z-bacterial-thylakoid-audit/review.yaml
    sha256: 98df4b4d629ecb3e169f2739cdb7b78e032ea2c6db5b728666c57e3ab9a612fe
    role: context
  - path: reviews/structured/20261021T110752Z-chitosome-audit/review.md
    sha256: 4ebd1797103664092948fa50ed46069c61d452dcfbc8edab5d003949223ff94e
    role: context
  - path: reviews/structured/20261021T110752Z-chitosome-audit/review.yaml
    sha256: 99af0b9628e6b9af0c5713c89658610c7e2cc5a3a7c947993210b4da76a51b53
    role: context
  - path: reviews/structured/20261021T110755Z-chloroplast-audit/review.md
    sha256: 0543e854022b2b4e70d9e81cba788e986c6efd8cc6db507a139f9979666fa4fd
    role: context
  - path: reviews/structured/20261021T110755Z-chloroplast-audit/review.yaml
    sha256: f3c3ddbd2da9a91bb230a8acf49262a9a1d045b1902b91552b7edec02f1ac0b7
    role: context
  - path: reviews/structured/20261021T110757Z-chloroplast-envelope-audit/review.md
    sha256: 42d07619240f082849e553906f0aef38f600081d27b7fc54d5e1f86321999f4b
    role: context
  - path: reviews/structured/20261021T110757Z-chloroplast-envelope-audit/review.yaml
    sha256: 2be9beedd1b70a7c4947df25bebb9141cbe4997eed76a41a94db1bdb5da0b9fc
    role: context
  - path: reviews/structured/20261021T110759Z-chloroplast-inner-membrane-audit/review.md
    sha256: 04cc4f7c61ea8e82e5c3040ddf6c3365892a2fc42241879d3dae9f850c3a3102
    role: context
  - path: reviews/structured/20261021T110759Z-chloroplast-inner-membrane-audit/review.yaml
    sha256: 6c0e37df007c7583d7699f3394d389b525487bfaaadd3345e1cc62e1d1a06672
    role: context
  - path: reviews/structured/20261021T110802Z-chloroplast-intermembrane-space-audit/review.md
    sha256: d03e6e30e49e5da429b3d8394557217ae6b1cf20cb4e613a2b2a452bcc647d7d
    role: context
  - path: reviews/structured/20261021T110802Z-chloroplast-intermembrane-space-audit/review.yaml
    sha256: 26b83275375d9f3a36a937e7d24a4b79fc5198364f742aa2f23f3476dd497b2f
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
- target_id: GO:0160211
  path: data/structures/membrane_organelle/apicoplast_membrane.yaml
  label: apicoplast membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/apicoplast_membrane.yaml
    role: maintained scientific record
- target_id: GO:0005776
  path: data/structures/membrane_organelle/autophagosome.yaml
  label: autophagosome
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/autophagosome.yaml
    role: maintained scientific record
- target_id: GO:0034423
  path: data/structures/membrane_organelle/autophagosome_lumen.yaml
  label: autophagosome lumen
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/autophagosome_lumen.yaml
    role: maintained scientific record
- target_id: GO:0000421
  path: data/structures/membrane_organelle/autophagosome_membrane.yaml
  label: autophagosome membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/autophagosome_membrane.yaml
    role: maintained scientific record
- target_id: GO:0030075
  path: data/structures/membrane_organelle/bacterial_thylakoid.yaml
  label: bacterial thylakoid
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/bacterial_thylakoid.yaml
    role: maintained scientific record
- target_id: GO:0045009
  path: data/structures/membrane_organelle/chitosome.yaml
  label: chitosome
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/chitosome.yaml
    role: maintained scientific record
- target_id: GO:0009507
  path: data/structures/membrane_organelle/chloroplast.yaml
  label: chloroplast
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/chloroplast.yaml
    role: maintained scientific record
- target_id: GO:0009941
  path: data/structures/membrane_organelle/chloroplast_envelope.yaml
  label: chloroplast envelope
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/chloroplast_envelope.yaml
    role: maintained scientific record
- target_id: GO:0009706
  path: data/structures/membrane_organelle/chloroplast_inner_membrane.yaml
  label: chloroplast inner membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/chloroplast_inner_membrane.yaml
    role: maintained scientific record
- target_id: GO:0031972
  path: data/structures/membrane_organelle/chloroplast_intermembrane_space.yaml
  label: chloroplast intermembrane space
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/chloroplast_intermembrane_space.yaml
    role: maintained scientific record
scope:
  description: Exact ten-record PR cohort reassessed against current main 463315caf9231f00781fef74e7d9b8ef8c44a502.
    Changed inputs are substantively reassessed. Scientific records remain unchanged.
  selection: Complete cohort of ten maintained records reviewed in original PR head
    998dda812da7bd6e3740c579ee8ff24669b62a9c.
  coverage: full
  population_size: 10
  reviewed_target_ids:
  - GO:0160211
  - GO:0005776
  - GO:0034423
  - GO:0000421
  - GO:0030075
  - GO:0045009
  - GO:0009507
  - GO:0009941
  - GO:0009706
  - GO:0031972
checks:
- check_id: qc
  name: Full native QC
  status: passed
  required: true
  target_ids:
  - GO:0160211
  - GO:0005776
  - GO:0034423
  - GO:0000421
  - GO:0030075
  - GO:0045009
  - GO:0009507
  - GO:0009941
  - GO:0009706
  - GO:0031972
  command: just qc
  exit_code: 0
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  scope_note: Actual local execution at main-merge head e721920f30c72a6c35cecb9913c6780e18a460ed.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-qc
- check_id: labels
  name: Native label correspondence
  status: passed
  required: true
  target_ids:
  - GO:0160211
  - GO:0005776
  - GO:0034423
  - GO:0000421
  - GO:0030075
  - GO:0045009
  - GO:0009507
  - GO:0009941
  - GO:0009706
  - GO:0031972
  command: just validate-products
  exit_code: 0
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  scope_note: Actual local execution at main-merge head e721920f30c72a6c35cecb9913c6780e18a460ed.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-labels
- check_id: trait-links
  name: TraitMech references
  status: passed
  required: true
  target_ids:
  - GO:0160211
  - GO:0005776
  - GO:0034423
  - GO:0000421
  - GO:0030075
  - GO:0045009
  - GO:0009507
  - GO:0009941
  - GO:0009706
  - GO:0031972
  command: just check-trait-links --check
  exit_code: 0
  summary: Native TraitMech link check passed.
  scope_note: Actual local execution at main-merge head e721920f30c72a6c35cecb9913c6780e18a460ed.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-trait-links
- check_id: vendored
  name: Pinned governed files
  status: passed
  required: true
  target_ids:
  - GO:0160211
  - GO:0005776
  - GO:0034423
  - GO:0000421
  - GO:0030075
  - GO:0045009
  - GO:0009507
  - GO:0009941
  - GO:0009706
  - GO:0031972
  command: just vendored-check
  exit_code: 0
  summary: Pinned governed files match; native vendored check passed.
  scope_note: Actual local execution at main-merge head e721920f30c72a6c35cecb9913c6780e18a460ed.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-vendored
- check_id: curies
  name: Native identifier resolver
  status: passed
  required: true
  target_ids:
  - GO:0160211
  - GO:0005776
  - GO:0034423
  - GO:0000421
  - GO:0030075
  - GO:0045009
  - GO:0009507
  - GO:0009941
  - GO:0009706
  - GO:0031972
  command: just check-curies-strict
  exit_code: 0
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  scope_note: Actual local execution at main-merge head e721920f30c72a6c35cecb9913c6780e18a460ed.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-curies
- check_id: focused-0
  name: validate GO:0160211
  status: passed
  required: true
  target_ids:
  - GO:0160211
  command: just validate data/structures/membrane_organelle/apicoplast_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-1
  name: validate-strict GO:0160211
  status: passed
  required: true
  target_ids:
  - GO:0160211
  command: just validate-strict data/structures/membrane_organelle/apicoplast_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-2
  name: validate GO:0005776
  status: passed
  required: true
  target_ids:
  - GO:0005776
  command: just validate data/structures/membrane_organelle/autophagosome.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-3
  name: validate-strict GO:0005776
  status: passed
  required: true
  target_ids:
  - GO:0005776
  command: just validate-strict data/structures/membrane_organelle/autophagosome.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-4
  name: validate GO:0034423
  status: passed
  required: true
  target_ids:
  - GO:0034423
  command: just validate data/structures/membrane_organelle/autophagosome_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-5
  name: validate-strict GO:0034423
  status: passed
  required: true
  target_ids:
  - GO:0034423
  command: just validate-strict data/structures/membrane_organelle/autophagosome_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-6
  name: validate GO:0000421
  status: passed
  required: true
  target_ids:
  - GO:0000421
  command: just validate data/structures/membrane_organelle/autophagosome_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-7
  name: validate-strict GO:0000421
  status: passed
  required: true
  target_ids:
  - GO:0000421
  command: just validate-strict data/structures/membrane_organelle/autophagosome_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-8
  name: validate GO:0030075
  status: passed
  required: true
  target_ids:
  - GO:0030075
  command: just validate data/structures/membrane_organelle/bacterial_thylakoid.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-9
  name: validate-strict GO:0030075
  status: passed
  required: true
  target_ids:
  - GO:0030075
  command: just validate-strict data/structures/membrane_organelle/bacterial_thylakoid.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-10
  name: validate GO:0045009
  status: passed
  required: true
  target_ids:
  - GO:0045009
  command: just validate data/structures/membrane_organelle/chitosome.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-11
  name: validate-strict GO:0045009
  status: passed
  required: true
  target_ids:
  - GO:0045009
  command: just validate-strict data/structures/membrane_organelle/chitosome.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-12
  name: validate GO:0009507
  status: passed
  required: true
  target_ids:
  - GO:0009507
  command: just validate data/structures/membrane_organelle/chloroplast.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-13
  name: validate-strict GO:0009507
  status: passed
  required: true
  target_ids:
  - GO:0009507
  command: just validate-strict data/structures/membrane_organelle/chloroplast.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-14
  name: validate GO:0009941
  status: passed
  required: true
  target_ids:
  - GO:0009941
  command: just validate data/structures/membrane_organelle/chloroplast_envelope.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-15
  name: validate-strict GO:0009941
  status: passed
  required: true
  target_ids:
  - GO:0009941
  command: just validate-strict data/structures/membrane_organelle/chloroplast_envelope.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-16
  name: validate GO:0009706
  status: passed
  required: true
  target_ids:
  - GO:0009706
  command: just validate data/structures/membrane_organelle/chloroplast_inner_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-17
  name: validate-strict GO:0009706
  status: passed
  required: true
  target_ids:
  - GO:0009706
  command: just validate-strict data/structures/membrane_organelle/chloroplast_inner_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-18
  name: validate GO:0031972
  status: passed
  required: true
  target_ids:
  - GO:0031972
  command: just validate data/structures/membrane_organelle/chloroplast_intermembrane_space.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-19
  name: validate-strict GO:0031972
  status: passed
  required: true
  target_ids:
  - GO:0031972
  command: just validate-strict data/structures/membrane_organelle/chloroplast_intermembrane_space.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: supplemental-pmid
  name: Supplemental bounded PMID authority checks
  status: passed
  required: true
  target_ids:
  - GO:0160211
  - GO:0005776
  - GO:0034423
  - GO:0000421
  - GO:0030075
  - GO:0045009
  - GO:0009507
  - GO:0009941
  - GO:0009706
  - GO:0031972
  command: .venv/bin/python /private/tmp/cellstructure-batches-2346-2397-20261103/check_pmid_chunks.py
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358
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
  - GO:0160211
  - GO:0005776
  - GO:0034423
  - GO:0000421
  - GO:0030075
  - GO:0045009
  - GO:0009507
  - GO:0009941
  - GO:0009706
  - GO:0031972
  summary: 'Nine applicability defects are corrected: three omissions (apicoplast
    membrane, bacterial thylakoid and chitosome), and six unsupported expression-only
    exclusions (autophagosome, autophagosome membrane, chloroplast, envelope, inner
    membrane and intermembrane space). Autophagosome lumen is a genuine sparse topology
    exclusion. Actual catalogue coverage, bounded molecular searches and experimental
    strain contexts are assessed separately. PCC7942 dataset context cannot support
    the maintained PCC6803 example or repair its curation finding. No covered fungal,
    apicomplexan or green-algal dataset is substituted with another organism. Resource
    noncoverage is not biological absence; retained historical runner failure is not
    a fresh invocation.'
  evidence_ids:
  - plaque-catalogue
  - plaque-adapter-meta
  - plaque-adapter-search-thylakoid
  - plaque-adapter-search-photosystem
  - plaque-adapter-search-cytochrome
  - plaque-adapter-search-ATP-synthase
  - plaque-adapter-gene-Synpcc7942_2049
  - plaque-adapter-gene-Synpcc7942_0424
  - plaque-adapter-gene-Synpcc7942_2331
  - plaque-adapter-gene-Synpcc7942_0336
  - plaque-adapter-module-38
  - plaque-adapter-module-38-genes
  - plaque-adapter-module-1
  - plaque-adapter-module-1-genes
  - plaque-historical-runner
  - micro-adapter-catalogue
  - septin-current-adapter-catalogue
- check_id: independent-scientific-review
  name: Independent claim-level source review
  status: passed
  required: true
  target_ids:
  - GO:0160211
  - GO:0005776
  - GO:0034423
  - GO:0000421
  - GO:0030075
  - GO:0045009
  - GO:0009507
  - GO:0009941
  - GO:0009706
  - GO:0031972
  summary: Three read-only reviewers covered the complete ten-record cohort, including
    changed inputs, with explicit scientific findings and source-access limits. Final
    artifact/head acceptance occurs after saving.
  evidence_ids:
  - plaque-policy
  - plaque-rubric
  - plaque-graph-policy
  - plaque-schema-policy
  - plaque-thylakoid-agent-go
  - plaque-root21-sources-inner-go
  - plaque-root21-sources-ims-go
  - plaque-inner-isa
  - plaque-ims-isa
  - plaque-thylakoid-agent-tax-1117
  - plaque-thylakoid-agent-tax-1148
  - plaque-thylakoid-agent-tax-1140
  - plaque-root21-sources-NCBITaxon-33090
  - plaque-root21-sources-NCBITaxon-3055
  - plaque-thylakoid-agent-perez2024-meta
  - plaque-thylakoid-agent-casella2017-meta
  - plaque-thylakoid-agent-huokko2021-meta
  - plaque-root21-sources-doi-10.1098_rstb.2009.0103
  - plaque-root21-sources-doi-10.1016_j.cell.2022.10.030
  - plaque-thylakoid-agent-jats-PMC5683893
  - plaque-thylakoid-agent-jats-PMC8190092
  - plaque-root21-sources-keeling2010-pmc
  - plaque-root21-sources-SL-0051-json
  - plaque-root21-sources-SL-0052-json
  - plaque-jin2022-pdb-entry
  - plaque-jin2022-pdb-entity1
  - plaque-perez-body-electron-transport
  - plaque-perez-body-introduction
  - plaque-perez2024-publisher
  - plaque-perez2024-body
  - plaque-root21-sources-keeling2010-jats
  - plaque-root21-sources-keeling2010-s3
  - plaque-root21-sources-keeling2010-repository
  - plaque-root21-sources-keeling2010-bioc
  - plaque-root21-sources-jin2022-publisher
  - plaque-root21-sources-jin2022-author-publications
  - plaque-catalogue
  - plaque-adapter-meta
  - plaque-adapter-gene-Synpcc7942_2049
  - plaque-adapter-gene-Synpcc7942_0424
  - plaque-adapter-gene-Synpcc7942_2331
  - plaque-adapter-gene-Synpcc7942_0336
  - plaque-adapter-module-38
  - plaque-adapter-module-38-genes
  - plaque-adapter-module-1
  - plaque-adapter-module-1-genes
  - plaque-adapter-publication
  - micro-review-policy
  - micro-review-config
  - micro-review-profile
  - micro-graph-contract
  - micro-review-schema
  - micro-auto-go
  - micro-auto-SL-0022-json
  - micro-auto-SL-0318-json
  - micro-auto-taxon-4932
  - micro-auto-takeshige1992-xml
  - micro-auto-suzuki2001-publisher
  - micro-auto-xie2007-publisher
  - micro-auto-ichimura2000-publisher
  - micro-chito-go
  - micro-chito-go-parts
  - micro-chito-chebi17029
  - micro-chito-tax-4751
  - micro-chito-tax-559292
  - micro-chito-leal1988-meta
  - micro-chito-jats-PMC2132460
  - micro-chito-ziman1998-browser-discussion
  - micro-chito-bartnicki2006-pdf
  - micro-chito-P08004
  - micro-chito-P29465
  - micro-chito-PMID-12928491
  - micro-chito-PMID-17519287
  - micro-chito-PMID-28346351
  - micro-chito-IPR004835
  - micro-chito-ipr-matches-P08004
  - micro-chito-ipr-matches-P29465
  - micro-adapter-catalogue
  - septin-native-review-policy
  - septin-native-curation-policy
  - septin-native-graph-policy
  - septin-apicoplast-membrane-agent-go
  - septin-root21-sources-chloroplast-go
  - septin-root21-sources-envelope-go
  - septin-root21-sources-GO0061927
  - septin-root21-sources-ancestors-0009507
  - septin-root21-sources-ancestors-0009941
  - septin-root21-sources-NCBITaxon-33090
  - septin-root21-sources-NCBITaxon-3055
  - septin-root21-sources-doi-10.1098_rstb.2009.0103
  - septin-root21-sources-doi-10.1016_j.cell.2022.10.030
  - septin-root21-sources-doi-10.1007_s00294-011-0339-1
  - septin-root21-sources-keeling2010-pmc
  - septin-root21-sources-jin2022-author-publications
  - septin-apicoplast-agent-tax-5794
  - septin-apicoplast-agent-tax-5811
  - septin-apicoplast-agent-tax-5833
  - septin-apicoplast-agent-tax-508771
  - septin-apicoplast-agent-tax-36329
  - septin-apicoplast-agent-S8GBF3
  - septin-apicoplast-agent-O97275
  - septin-apicoplast-agent-B9PY98
  - septin-apicoplast-agent-C9WWW6
  - septin-apicoplast-agent-matches-S8GBF3
  - septin-apicoplast-agent-matches-O97275
  - septin-apicoplast-agent-matches-B9PY98
  - septin-apicoplast-agent-jats-PMC3681736
  - septin-apicoplast-agent-jats-PMC3662607
  - septin-apicoplast-agent-jats-PMC2817234
  - septin-apicoplast-agent-jats-PMC5406208
  - septin-apicoplast-agent-ena-FJ976521
  - septin-apicoplast-agent-ena-FJ976520
  - septin-apicoplast-agent-ena-CAB38986
  - septin-apicoplast-agent-gene-814456
  - septin-apicoplast-agent-kalanon2009-pdf
  - septin-agrawal2011-thesis
- check_id: historical-adapter-runner
  name: Retained historical adapter runner availability
  status: unavailable
  required: false
  target_ids:
  - GO:0160211
  - GO:0005776
  - GO:0000421
  - GO:0030075
  - GO:0045009
  - GO:0009507
  - GO:0009941
  - GO:0009706
  - GO:0031972
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
- check_id: apicoplast_membrane-uniprot-verify
  name: Native apicoplast membrane UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0160211
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/apicoplast_membrane.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-apicoplast_membrane-verify
- check_id: apicoplast_membrane-uniprot-causal
  name: Native apicoplast membrane UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0160211
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/apicoplast_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-apicoplast_membrane-causal
- check_id: autophagosome-uniprot-verify
  name: Native autophagosome UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0005776
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/autophagosome.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-autophagosome-verify
- check_id: autophagosome-uniprot-causal
  name: Native autophagosome UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0005776
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/autophagosome.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-autophagosome-causal
- check_id: autophagosome_lumen-uniprot-verify
  name: Native autophagosome lumen UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0034423
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/autophagosome_lumen.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-autophagosome_lumen-verify
- check_id: autophagosome_lumen-uniprot-causal
  name: Native autophagosome lumen UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0034423
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/autophagosome_lumen.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-autophagosome_lumen-causal
- check_id: autophagosome_membrane-uniprot-verify
  name: Native autophagosome membrane UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0000421
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/autophagosome_membrane.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-autophagosome_membrane-verify
- check_id: autophagosome_membrane-uniprot-causal
  name: Native autophagosome membrane UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0000421
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/autophagosome_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-autophagosome_membrane-causal
- check_id: bacterial_thylakoid-uniprot-verify
  name: Native bacterial thylakoid UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0030075
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/bacterial_thylakoid.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-bacterial_thylakoid-verify
- check_id: bacterial_thylakoid-uniprot-causal
  name: Native bacterial thylakoid UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0030075
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/bacterial_thylakoid.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-bacterial_thylakoid-causal
- check_id: chitosome-uniprot-verify
  name: Native chitosome UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0045009
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chitosome.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-chitosome-verify
- check_id: chitosome-uniprot-causal
  name: Native chitosome UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0045009
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chitosome.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-chitosome-causal
- check_id: chloroplast-uniprot-verify
  name: Native chloroplast UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0009507
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chloroplast.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-chloroplast-verify
- check_id: chloroplast-uniprot-causal
  name: Native chloroplast UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0009507
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chloroplast.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-chloroplast-causal
- check_id: chloroplast_envelope-uniprot-verify
  name: Native chloroplast envelope UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0009941
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chloroplast_envelope.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-chloroplast_envelope-verify
- check_id: chloroplast_envelope-uniprot-causal
  name: Native chloroplast envelope UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0009941
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chloroplast_envelope.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-chloroplast_envelope-causal
- check_id: chloroplast_inner_membrane-uniprot-verify
  name: Native chloroplast inner membrane UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0009706
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chloroplast_inner_membrane.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-chloroplast_inner_membrane-verify
- check_id: chloroplast_inner_membrane-uniprot-causal
  name: Native chloroplast inner membrane UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0009706
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chloroplast_inner_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-chloroplast_inner_membrane-causal
- check_id: chloroplast_intermembrane_space-uniprot-verify
  name: Native chloroplast intermembrane space UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0031972
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chloroplast_intermembrane_space.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-chloroplast_intermembrane_space-verify
- check_id: chloroplast_intermembrane_space-uniprot-causal
  name: Native chloroplast intermembrane space UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0031972
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chloroplast_intermembrane_space.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories, zero molecular graph
    nodes or unanchored xrefs do not validate narrative molecules, mechanism, taxon
    transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-chloroplast_intermembrane_space-causal
evidence:
- evidence_id: current-record-0
  kind: record_content
  reference: data/structures/membrane_organelle/apicoplast_membrane.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T09:44:45Z'
  support: context_only
  summary: Original frozen SHA256 fb3e343e0ed2a8711dff2305abea2166c589cb0a7b169d291c67fed81990ca58;
    current SHA256 fb3e343e0ed2a8711dff2305abea2166c589cb0a7b169d291c67fed81990ca58.
    Record bytes unchanged since the original review.
  snapshot_sha256: fb3e343e0ed2a8711dff2305abea2166c589cb0a7b169d291c67fed81990ca58
- evidence_id: original-review-0
  kind: prior_review
  reference: reviews/structured/20261021T110736Z-apicoplast-membrane-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T09:44:45Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 327d4a503051b00002667d41e48c0fea69c8f330e639efe0880099fa13c6d5c4
- evidence_id: current-record-1
  kind: record_content
  reference: data/structures/membrane_organelle/autophagosome.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T09:44:45Z'
  support: context_only
  summary: Original frozen SHA256 9d18c1f34ce5e4da65546eccf8f4ffc9a2273fcca1cd6db4efbb770f8591c3ba;
    current SHA256 08c1df95826ee2cb8b86b66592876f324eae999c7cafdc619d1ffad1607f6232.
    Changed record reassessed against current sources.
  snapshot_sha256: 08c1df95826ee2cb8b86b66592876f324eae999c7cafdc619d1ffad1607f6232
- evidence_id: original-review-1
  kind: prior_review
  reference: reviews/structured/20261021T110741Z-autophagosome-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T09:44:45Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 18417b1f2d56272090dd09e3eb52dab6c976ec104e8cfce11319408847dccbb4
- evidence_id: current-record-2
  kind: record_content
  reference: data/structures/membrane_organelle/autophagosome_lumen.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T09:44:45Z'
  support: context_only
  summary: Original frozen SHA256 33fbf9f3ae1591081dd1e113d0fd7476c64bdafaa238ec35c7705fb89bb0f98d;
    current SHA256 33fbf9f3ae1591081dd1e113d0fd7476c64bdafaa238ec35c7705fb89bb0f98d.
    Record bytes unchanged since the original review.
  snapshot_sha256: 33fbf9f3ae1591081dd1e113d0fd7476c64bdafaa238ec35c7705fb89bb0f98d
- evidence_id: original-review-2
  kind: prior_review
  reference: reviews/structured/20261021T110744Z-autophagosome-lumen-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T09:44:45Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 6f417e89968139de6fc68836753c3ed68851e18f30bd98b3211ed692400e51ad
- evidence_id: current-record-3
  kind: record_content
  reference: data/structures/membrane_organelle/autophagosome_membrane.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T09:44:45Z'
  support: context_only
  summary: Original frozen SHA256 aa651db3a9b5a208ae7a4deef9d3595d79c0296cda8ebdc9a1c524a11b948254;
    current SHA256 aa651db3a9b5a208ae7a4deef9d3595d79c0296cda8ebdc9a1c524a11b948254.
    Record bytes unchanged since the original review.
  snapshot_sha256: aa651db3a9b5a208ae7a4deef9d3595d79c0296cda8ebdc9a1c524a11b948254
- evidence_id: original-review-3
  kind: prior_review
  reference: reviews/structured/20261021T110747Z-autophagosome-membrane-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T09:44:45Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 64f2d8ab01bf1550f71fcbf450bee87417f10e5edc36d6532f097e4098ad8ab0
- evidence_id: current-record-4
  kind: record_content
  reference: data/structures/membrane_organelle/bacterial_thylakoid.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T09:44:45Z'
  support: context_only
  summary: Original frozen SHA256 a134c6cf6fd6069f0a0ddc37f1e99ded9a32994b3b1fa16d2f9938e3e46b8c40;
    current SHA256 a134c6cf6fd6069f0a0ddc37f1e99ded9a32994b3b1fa16d2f9938e3e46b8c40.
    Record bytes unchanged since the original review.
  snapshot_sha256: a134c6cf6fd6069f0a0ddc37f1e99ded9a32994b3b1fa16d2f9938e3e46b8c40
- evidence_id: original-review-4
  kind: prior_review
  reference: reviews/structured/20261021T110749Z-bacterial-thylakoid-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T09:44:45Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 98df4b4d629ecb3e169f2739cdb7b78e032ea2c6db5b728666c57e3ab9a612fe
- evidence_id: current-record-5
  kind: record_content
  reference: data/structures/membrane_organelle/chitosome.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T09:44:45Z'
  support: context_only
  summary: Original frozen SHA256 7233ef84787e4a164a1388fbb12643f34bfc28bf12272f6c0898868975376938;
    current SHA256 ec564f818b649f3c4c8a56de6d6bea798eded59e73f1c4b840325eb83b9d5493.
    Changed record reassessed against current sources.
  snapshot_sha256: ec564f818b649f3c4c8a56de6d6bea798eded59e73f1c4b840325eb83b9d5493
- evidence_id: original-review-5
  kind: prior_review
  reference: reviews/structured/20261021T110752Z-chitosome-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T09:44:45Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 99af0b9628e6b9af0c5713c89658610c7e2cc5a3a7c947993210b4da76a51b53
- evidence_id: current-record-6
  kind: record_content
  reference: data/structures/membrane_organelle/chloroplast.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T09:44:45Z'
  support: context_only
  summary: Original frozen SHA256 4c13f5dadaeb23a88fabfc2b5ec65034ed0ac83cbca9d45143793618acf2e727;
    current SHA256 4c13f5dadaeb23a88fabfc2b5ec65034ed0ac83cbca9d45143793618acf2e727.
    Record bytes unchanged since the original review.
  snapshot_sha256: 4c13f5dadaeb23a88fabfc2b5ec65034ed0ac83cbca9d45143793618acf2e727
- evidence_id: original-review-6
  kind: prior_review
  reference: reviews/structured/20261021T110755Z-chloroplast-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T09:44:45Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: f3c3ddbd2da9a91bb230a8acf49262a9a1d045b1902b91552b7edec02f1ac0b7
- evidence_id: current-record-7
  kind: record_content
  reference: data/structures/membrane_organelle/chloroplast_envelope.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T09:44:45Z'
  support: context_only
  summary: Original frozen SHA256 29da363489107536342db1782001be534ea54605039b80c201cba0a46de9468e;
    current SHA256 29da363489107536342db1782001be534ea54605039b80c201cba0a46de9468e.
    Record bytes unchanged since the original review.
  snapshot_sha256: 29da363489107536342db1782001be534ea54605039b80c201cba0a46de9468e
- evidence_id: original-review-7
  kind: prior_review
  reference: reviews/structured/20261021T110757Z-chloroplast-envelope-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T09:44:45Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 2be9beedd1b70a7c4947df25bebb9141cbe4997eed76a41a94db1bdb5da0b9fc
- evidence_id: current-record-8
  kind: record_content
  reference: data/structures/membrane_organelle/chloroplast_inner_membrane.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T09:44:45Z'
  support: context_only
  summary: Original frozen SHA256 05283f5252a6354d26bef1ff196b3a9e10fbd6e72e9a6ec17014330f7a28dbb3;
    current SHA256 05283f5252a6354d26bef1ff196b3a9e10fbd6e72e9a6ec17014330f7a28dbb3.
    Record bytes unchanged since the original review.
  snapshot_sha256: 05283f5252a6354d26bef1ff196b3a9e10fbd6e72e9a6ec17014330f7a28dbb3
- evidence_id: original-review-8
  kind: prior_review
  reference: reviews/structured/20261021T110759Z-chloroplast-inner-membrane-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T09:44:45Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 6c0e37df007c7583d7699f3394d389b525487bfaaadd3345e1cc62e1d1a06672
- evidence_id: current-record-9
  kind: record_content
  reference: data/structures/membrane_organelle/chloroplast_intermembrane_space.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T09:44:45Z'
  support: context_only
  summary: Original frozen SHA256 7ab90f4d2f4c41c466e100d589fb1f1d42bf90ded515dea6db5575d54119d43a;
    current SHA256 7ab90f4d2f4c41c466e100d589fb1f1d42bf90ded515dea6db5575d54119d43a.
    Record bytes unchanged since the original review.
  snapshot_sha256: 7ab90f4d2f4c41c466e100d589fb1f1d42bf90ded515dea6db5575d54119d43a
- evidence_id: original-review-9
  kind: prior_review
  reference: reviews/structured/20261021T110802Z-chloroplast-intermembrane-space-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T09:44:45Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 26b83275375d9f3a36a937e7d24a4b79fc5198364f742aa2f23f3476dd497b2f
- evidence_id: plaque-current-4
  kind: record_content
  reference: data/structures/membrane_organelle/bacterial_thylakoid.yaml
  locator: Complete current YAML at source e721920f30c72a6c35cecb9913c6780e18a460ed;
    every field, graph edge and history entry
  accessed_at: '2026-11-03T09:40:48.212813Z'
  support: context_only
  summary: Current bytes match the historical frozen target hash. Entire maintained
    record independently reassessed; status remains PROPOSED and no target image is
    declared.
  snapshot_sha256: a134c6cf6fd6069f0a0ddc37f1e99ded9a32994b3b1fa16d2f9938e3e46b8c40
- evidence_id: plaque-original-4
  kind: prior_review
  reference: reviews/structured/20261021T110749Z-bacterial-thylakoid-audit/review.yaml
  locator: Complete original YAML and Markdown; actual native validate and exact render
    --content
  accessed_at: '2026-11-03T09:40:48.212813Z'
  support: context_only
  summary: Native validation and deterministic Markdown equality passed; historical
    target bytes match the original frozen hash. Original finding and check scopes
    were independently read.
  snapshot_sha256: 98df4b4d629ecb3e169f2739cdb7b78e032ea2c6db5b728666c57e3ab9a612fe
- evidence_id: plaque-current-8
  kind: record_content
  reference: data/structures/membrane_organelle/chloroplast_inner_membrane.yaml
  locator: Complete current YAML at source e721920f30c72a6c35cecb9913c6780e18a460ed;
    every field, graph edge and history entry
  accessed_at: '2026-11-03T09:40:48.212813Z'
  support: context_only
  summary: Current bytes match the historical frozen target hash. Entire maintained
    record independently reassessed; status remains PROPOSED and no target image is
    declared.
  snapshot_sha256: 05283f5252a6354d26bef1ff196b3a9e10fbd6e72e9a6ec17014330f7a28dbb3
- evidence_id: plaque-original-8
  kind: prior_review
  reference: reviews/structured/20261021T110759Z-chloroplast-inner-membrane-audit/review.yaml
  locator: Complete original YAML and Markdown; actual native validate and exact render
    --content
  accessed_at: '2026-11-03T09:40:48.212813Z'
  support: context_only
  summary: Native validation and deterministic Markdown equality passed; historical
    target bytes match the original frozen hash. Original finding and check scopes
    were independently read.
  snapshot_sha256: 6c0e37df007c7583d7699f3394d389b525487bfaaadd3345e1cc62e1d1a06672
- evidence_id: plaque-current-9
  kind: record_content
  reference: data/structures/membrane_organelle/chloroplast_intermembrane_space.yaml
  locator: Complete current YAML at source e721920f30c72a6c35cecb9913c6780e18a460ed;
    every field, graph edge and history entry
  accessed_at: '2026-11-03T09:40:48.212813Z'
  support: context_only
  summary: Current bytes match the historical frozen target hash. Entire maintained
    record independently reassessed; status remains PROPOSED and no target image is
    declared.
  snapshot_sha256: 7ab90f4d2f4c41c466e100d589fb1f1d42bf90ded515dea6db5575d54119d43a
- evidence_id: plaque-original-9
  kind: prior_review
  reference: reviews/structured/20261021T110802Z-chloroplast-intermembrane-space-audit/review.yaml
  locator: Complete original YAML and Markdown; actual native validate and exact render
    --content
  accessed_at: '2026-11-03T09:40:48.212813Z'
  support: context_only
  summary: Native validation and deterministic Markdown equality passed; historical
    target bytes match the original frozen hash. Original finding and check scopes
    were independently read.
  snapshot_sha256: 26b83275375d9f3a36a937e7d24a4b79fc5198364f742aa2f23f3476dd497b2f
- evidence_id: plaque-neighbor-chloroplast
  kind: record_content
  reference: data/structures/membrane_organelle/chloroplast.yaml
  locator: Frozen local boundary context or native review rule
  accessed_at: '2026-11-03T09:40:48.212813Z'
  support: context_only
  summary: Neighbor identity, definition, hierarchy, parthood and discussions only;
    no whole-record scientific judgment.
  snapshot_sha256: 4c13f5dadaeb23a88fabfc2b5ec65034ed0ac83cbca9d45143793618acf2e727
- evidence_id: plaque-neighbor-chloroplast_envelope
  kind: record_content
  reference: data/structures/membrane_organelle/chloroplast_envelope.yaml
  locator: Frozen local boundary context or native review rule
  accessed_at: '2026-11-03T09:40:48.212813Z'
  support: context_only
  summary: Neighbor identity, definition, hierarchy, parthood and discussions only;
    no whole-record scientific judgment.
  snapshot_sha256: 29da363489107536342db1782001be534ea54605039b80c201cba0a46de9468e
- evidence_id: plaque-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Frozen local boundary context or native review rule
  accessed_at: '2026-11-03T09:40:48.212813Z'
  support: context_only
  summary: Native rules distinguish structure identity, molecular grounding, membership
    and assembly necessity; require claim-level source scopes, actual adapter applicability
    and immutable evidence-bearing reviews.
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: plaque-rubric
  kind: authority
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Frozen local boundary context or native review rule
  accessed_at: '2026-11-03T09:40:48.212813Z'
  support: context_only
  summary: Native rules distinguish structure identity, molecular grounding, membership
    and assembly necessity; require claim-level source scopes, actual adapter applicability
    and immutable evidence-bearing reviews.
  snapshot_sha256: e6b9e4b16a58c54402bed7bbee2c8b94a91d37562e8b0ee8b94ff0c829184a70
- evidence_id: plaque-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Frozen local boundary context or native review rule
  accessed_at: '2026-11-03T09:40:48.212813Z'
  support: context_only
  summary: Native rules distinguish structure identity, molecular grounding, membership
    and assembly necessity; require claim-level source scopes, actual adapter applicability
    and immutable evidence-bearing reviews.
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: plaque-schema-policy
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Frozen local boundary context or native review rule
  accessed_at: '2026-11-03T09:40:48.212813Z'
  support: context_only
  summary: Native rules distinguish structure identity, molecular grounding, membership
    and assembly necessity; require claim-level source scopes, actual adapter applicability
    and immutable evidence-bearing reviews.
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: plaque-thylakoid-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030075,GO:0009579,GO:0031676,GO:0031979,GO:0030094,GO:0030096,GO:0009512,GO:0045259,GO:0009767,GO:0042651
  locator: Exact returned term IDs, definitions, synonyms, comment and typed child
    relations
  accessed_at: '2026-11-03T09:33:23.661904Z'
  support: supports
  summary: Current GO terms support the stated identities and distinguish whole structures,
    membranes and enclosed regions. Typed is_a versus part_of relations are inspected
    separately; ontology-derived wording is not experimental evidence of universal
    biogenesis.
  snapshot_sha256: a318cc333a4ce72ef86dbc2671fef779dc2ad9fc744e8d3404ca11b9911e9954
- evidence_id: plaque-root21-sources-inner-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009528,GO:0009570,GO:0009706,GO:0009941,GO:0031969,GO:0031972
  locator: Exact returned term IDs, definitions, synonyms, comment and typed child
    relations
  accessed_at: '2026-11-03T09:33:24.173853Z'
  support: supports
  summary: Current GO terms support the stated identities and distinguish whole structures,
    membranes and enclosed regions. Typed is_a versus part_of relations are inspected
    separately; ontology-derived wording is not experimental evidence of universal
    biogenesis.
  snapshot_sha256: 087d62f1a0c168cf3eff51e5cf85c2a0673d8bb5050d69a062e4a20a43982e31
- evidence_id: plaque-root21-sources-ims-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009529,GO:0009706,GO:0009707,GO:0009941,GO:0031972
  locator: Exact returned term IDs, definitions, synonyms, comment and typed child
    relations
  accessed_at: '2026-11-03T09:33:24.926171Z'
  support: supports
  summary: Current GO terms support the stated identities and distinguish whole structures,
    membranes and enclosed regions. Typed is_a versus part_of relations are inspected
    separately; ontology-derived wording is not experimental evidence of universal
    biogenesis.
  snapshot_sha256: 3bcbf4bf02b601fc560d59f0858f836994308023b6ad2ff18c443f5479eb29ab
- evidence_id: plaque-inner-isa
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009706/ancestors?relations=is_a
  locator: Explicit relations=is_a ancestor response; complete returned ancestor list
  accessed_at: '2026-11-03T09:33:25.058731Z'
  support: supports
  summary: The asserted is_a parents occur in the is_a-only closure. This does not
    substitute a parthood relation for subclass identity.
  snapshot_sha256: 4df588daca6407a428606e8dbcf1e990cdf34a154db1e5ac8f2a1b07459105b7
- evidence_id: plaque-ims-isa
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031972/ancestors?relations=is_a
  locator: Explicit relations=is_a ancestor response; complete returned ancestor list
  accessed_at: '2026-11-03T09:33:25.123642Z'
  support: supports
  summary: The asserted is_a parents occur in the is_a-only closure. This does not
    substitute a parthood relation for subclass identity.
  snapshot_sha256: 621861d3b17c4e573d29adbbc43601bf7580a77551c6af1b6ec4e12ab7996637
- evidence_id: plaque-thylakoid-agent-tax-1117
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1117
  locator: Native taxId, scientificName, rank and lineage; identity only
  accessed_at: '2026-11-03T09:33:23.662134Z'
  support: supports
  summary: 'Exact authority identity: 1117 Cyanobacteriota. Taxonomic identity does
    not establish prevalence, experimental stock or localization.'
  snapshot_sha256: 5f4919ad6f362a82291b587d27134147f277ffc5fa593f6076f1983a704cd985
- evidence_id: plaque-thylakoid-agent-tax-1148
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1148
  locator: Native taxId, scientificName, rank and lineage; identity only
  accessed_at: '2026-11-03T09:33:23.662266Z'
  support: supports
  summary: 'Exact authority identity: 1148 Synechocystis sp. PCC 6803. Taxonomic identity
    does not establish prevalence, experimental stock or localization.'
  snapshot_sha256: 84c0a354189f6b736c57eb3886dc08090cd6edba80c6e35c1b92909c26f35ab4
- evidence_id: plaque-thylakoid-agent-tax-1140
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1140
  locator: Native taxId, scientificName, rank and lineage; identity only
  accessed_at: '2026-11-03T09:33:23.662679Z'
  support: supports
  summary: 'Exact authority identity: 1140 Synechococcus elongatus PCC 7942 = FACHB-805.
    Taxonomic identity does not establish prevalence, experimental stock or localization.'
  snapshot_sha256: 70bf02b8ca783e9afbd060d6c098a79cec71954ea2d64a270fc130481a63cb2b
- evidence_id: plaque-root21-sources-NCBITaxon-33090
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/33090
  locator: Native taxId, scientificName, rank and lineage; identity only
  accessed_at: '2026-11-03T09:33:24.260252Z'
  support: supports
  summary: 'Exact authority identity: 33090 Viridiplantae. Taxonomic identity does
    not establish prevalence, experimental stock or localization.'
  snapshot_sha256: b1394e36c6896d7ec64cdb301a239f2bc49bc435a22cc21fdba8fdc6217e2d11
- evidence_id: plaque-root21-sources-NCBITaxon-3055
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3055
  locator: Native taxId, scientificName, rank and lineage; identity only
  accessed_at: '2026-11-03T09:33:24.278123Z'
  support: supports
  summary: 'Exact authority identity: 3055 Chlamydomonas reinhardtii. Taxonomic identity
    does not establish prevalence, experimental stock or localization.'
  snapshot_sha256: e3861fe6706cefe2e079e15c0178a65e95efaad3890f548f25e721553eaa93a0
- evidence_id: plaque-thylakoid-agent-perez2024-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1146%2Fannurev-cellbio-120823-022747&format=json&resultType=core
  locator: 'Exact DOI query: authors, title, DOI/PMID/PMCID and complete returned
    abstract; no body inference'
  accessed_at: '2026-11-03T09:33:23.664405Z'
  support: supports
  summary: Native bibliography resolves to Evolution of Thylakoid Structural Diversity.;
    Perez-Boerema A, Engel BD, Wietrzynski W.. The abstract was read, but full-body
    support is claimed only by separately scoped rows.
  snapshot_sha256: f9df3427bb3b35764922628c9e89cc9378fa7875a4a103bde71a75b130d54926
- evidence_id: plaque-thylakoid-agent-casella2017-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1016%2Fj.molp.2017.09.019&format=json&resultType=core
  locator: 'Exact DOI query: authors, title, DOI/PMID/PMCID and complete returned
    abstract; no body inference'
  accessed_at: '2026-11-03T09:33:23.668516Z'
  support: supports
  summary: Native bibliography resolves to Dissecting the Native Architecture and
    Dynamics of Cyanobacterial Photosynthetic Machinery.; Casella S, Huang F, Mason
    D, Zhao GY, Johnson GN, Mullineaux CW, Liu LN.. The abstract was read, but full-body
    support is claimed only by separately scoped rows.
  snapshot_sha256: f9ab8e3e0ee2994d6ad8e8c4ba544e08a13d0874a6734e084db4cb03c97fecbe
- evidence_id: plaque-thylakoid-agent-huokko2021-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038%2Fs41467-021-23680-1&format=json&resultType=core
  locator: 'Exact DOI query: authors, title, DOI/PMID/PMCID and complete returned
    abstract; no body inference'
  accessed_at: '2026-11-03T09:33:23.668876Z'
  support: supports
  summary: Native bibliography resolves to Probing the biogenesis pathway and dynamics
    of thylakoid membranes.; Huokko T, Ni T, Dykes GF, Simpson DM, Brownridge P, Conradi
    FD, Beynon RJ, Nixon PJ, Mullineaux CW, Zhang P, Liu LN.. The abstract was read,
    but full-body support is claimed only by separately scoped rows.
  snapshot_sha256: af3189fba6c317b70a180f0f879e06319c38aa25d407906fa3a9c9e4628f1ab5
- evidence_id: plaque-root21-sources-doi-10.1098_rstb.2009.0103
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1098/rstb.2009.0103
  locator: 'Exact DOI query: authors, title, DOI/PMID/PMCID and complete returned
    abstract; no body inference'
  accessed_at: '2026-11-03T09:33:24.288972Z'
  support: supports
  summary: Native bibliography resolves to The endosymbiotic origin, diversification
    and fate of plastids.; Keeling PJ.. The abstract was read, but full-body support
    is claimed only by separately scoped rows.
  snapshot_sha256: 63c6291480d57ca01d4eb770792f919c0e3128eeaae04894f1ed2f2f3fc0e886
- evidence_id: plaque-root21-sources-doi-10.1016_j.cell.2022.10.030
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.cell.2022.10.030
  locator: 'Exact DOI query: authors, title, DOI/PMID/PMCID and complete returned
    abstract; no body inference'
  accessed_at: '2026-11-03T09:33:24.291196Z'
  support: supports
  summary: Jin2022 primary abstract reports a Chlamydomonas TOC–TIC supercomplex spanning
    both chloroplast envelope membranes with an IMS scaffold. This supports the bounded
    topology/import example; species is independently checked against deposited 7VCF
    entity metadata, and no strain is inferred.
  snapshot_sha256: b99888266af111ada3766e17870e706ab2a7c1da4ee0568626bedbfe5b000cb4
- evidence_id: plaque-thylakoid-agent-jats-PMC5683893
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5683893.1/PMC5683893.1.xml
  locator: 'Primary JATS: Introduction, Results §§2.1–2.3 and selected §2.4/Discussion
    text; Methods §4.1 Strains and Growth Conditions. Figure captions within those
    sections, not independent pixels or supplements.'
  accessed_at: '2026-11-03T09:33:23.672558Z'
  support: supports
  summary: Casella2017 explicitly assays Synechococcus elongatus PCC7942 grown in
    BG11 at30C. Native membrane isolation/BN-PAGE, AFM and tagged-complex TIRF/confocal/FRAP
    support photosystem, b6f and ATPase residence, heterogeneous organization and
    mobility in that strain. AFM b6f identification is explicitly tentative; earlier
    Synechocystis work is background, not the experimental organism. No universal
    assembly necessity is established.
  snapshot_sha256: 6e3c04f52b15e4ce163579c9c0c3a44b1946bded6fe47e1299e3ef6dc2ce18d7
- evidence_id: plaque-thylakoid-agent-jats-PMC8190092
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC8190092.1/PMC8190092.1.xml
  locator: 'Primary JATS: Introduction; selected Results §§Sec4–Sec6 and Discussion
    Sec7; Methods Sec9 Strains and Culture, Sec12 TEM, Sec13 cryo-ET. Text and captions
    only; no independent image-pixel or raw-data audit.'
  accessed_at: '2026-11-03T09:33:23.673011Z'
  support: supports
  summary: Huokko2021 uses Synechococcus elongatus PCC7942 for light-regulated thylakoid
    biogenesis. Source Methods distinguish that strain from cited Synechocystis literature.
    Observed membrane proximity and thylapse-like sites do not establish direct plasma-membrane
    fusion. Complex assembly/insertion and abundance vary with light and time; these
    results do not establish universal individual assembly requirements.
  snapshot_sha256: 0140e3b1a9fbb1fe170d186f153c24e08fb32c4cc91754a49facf09cdc67ff21
- evidence_id: plaque-root21-sources-keeling2010-pmc
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2817223/
  locator: 'Secondary review HTML: abstract and §1 plastid origins, two bounding membranes,
    green algae/plants and TOC/TIC paragraphs; selected §3 secondary-plastid membrane/trafficking
    context. No figure-pixel audit.'
  accessed_at: '2026-11-03T09:33:24.294643Z'
  support: supports
  summary: Keeling2010 secondary synthesis supports the primary plastid envelope and
    green-lineage context while recognizing nonphotosynthetic plastids and loss. Its
    evolutionary review is not a measured prevalence estimate or new primary membrane
    experiment.
  snapshot_sha256: decbb826d3fd9122491839b2f4de5ba646f9a2014c02fdf963feb6eca1e5800f
- evidence_id: plaque-root21-sources-SL-0051-json
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0051.json
  locator: Native definition, GO correspondence, exact synonym, immediate isA and
    partOf objects with inherited hierarchy distinguished
  accessed_at: '2026-11-03T09:33:24.884710Z'
  support: supports
  summary: SL0051 defines the stroma–IMS boundary and has separate chloroplast-membrane
    and plastid-inner-membrane isA parents. SL0052 defines the volume between bilayers
    and has plastid-IMS isA plus chloroplast-envelope partOf. The location identifiers
    do not identify a particular lipid species.
  snapshot_sha256: 297e41f26610b99820c4cc766411026cbc6b5b53f5551bce9b51d4be67c19454
- evidence_id: plaque-root21-sources-SL-0052-json
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0052.json
  locator: Native definition, GO correspondence, exact synonym, immediate isA and
    partOf objects with inherited hierarchy distinguished
  accessed_at: '2026-11-03T09:33:24.952147Z'
  support: supports
  summary: SL0051 defines the stroma–IMS boundary and has separate chloroplast-membrane
    and plastid-inner-membrane isA parents. SL0052 defines the volume between bilayers
    and has plastid-IMS isA plus chloroplast-envelope partOf. The location identifiers
    do not identify a particular lipid species.
  snapshot_sha256: 86926cc4e68d0232f615a03ad85bdb5676bdda61cdb70b011d034f751f440f81
- evidence_id: plaque-jin2022-pdb-entry
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/entry/7VCF
  locator: 7VCF struct.title and primary citation DOI, PMID, authors, year
  accessed_at: '2026-11-03T09:37:37.829066Z'
  support: supports
  summary: The deposited TOC–TIC structure is linked directly to Jin2022 DOI10.1016/j.cell.2022.10.030
    and PMID36413996. This is source linkage, not an independent coordinate reanalysis.
  snapshot_sha256: 61b96cb1867bf3de51e21afd2438309aadc8abf36de941a4cc3f2b1227628e31
- evidence_id: plaque-jin2022-pdb-entity1
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/7VCF/1
  locator: 7VCF polymer entity1 entity_src_gen and rcsb_entity_source_organism; no
    coordinate interpretation
  accessed_at: '2026-11-03T09:37:37.829278Z'
  support: supports
  summary: The primary deposition identifies source/host Chlamydomonas reinhardtii
    tax3055 for entity1, independently narrowing the abstract’s genus-level name to
    the maintained species. No strain, universal complex composition or essentiality
    is inferred.
  snapshot_sha256: 13a5bacc3b24e7813f5aaa1f767cf2f5ecadb100622d2a8fab8469458545b516
- evidence_id: plaque-perez-body-electron-transport
  kind: authority
  reference: https://doi.org/10.1146/annurev-cellbio-120823-022747
  locator: 'Browser-returned indexed publisher body: Electron Transport Chain Complexes
    subsection and selected contact-site paragraphs; packet hash, not native HTML
    body'
  accessed_at: '2026-11-03T09:34:09Z'
  support: supports
  summary: Secondary review supports the PSII–quinone–b6f–soluble carrier–PSI sequence
    and proton-gradient use by ATP synthase. Only those returned body sections were
    used; indexed content is explicitly a browser fallback after native403 responses.
  snapshot_sha256: 56c1f70a51fcbece7ecb33585c2ab81ad624de83df306e933f7556debff22110
- evidence_id: plaque-perez-body-introduction
  kind: authority
  reference: https://doi.org/10.1146/annurev-cellbio-120823-022747
  locator: Browser-returned indexed official publisher Introduction and selected membrane-architecture/contact-site
    paragraphs; unrelated search hits excluded
  accessed_at: '2026-11-03T09:37:31Z'
  support: supports
  summary: The publisher review explicitly identifies Gloeobacter as a thylakoid-lacking
    exception and separates cyanobacterial cytoplasm from plastid stroma. This supports
    qualitative distribution and topology, not quantitative prevalence or universal
    continuity.
  snapshot_sha256: cbf836e7549f5d05b8b7fbbd2e975e1537dec5e4e051f22e74473117c8f73b7c
- evidence_id: plaque-perez2024-publisher
  kind: authority
  reference: https://www.annualreviews.org/content/journals/10.1146/annurev-cellbio-120823-022747
  locator: Actual unsuccessful HTTP source-access response; not scientific article
    content
  accessed_at: '2026-11-03T09:33:25.044081Z'
  support: context_only
  summary: Fresh native route returned HTTP403. No body evidence is inferred from
    this response. Successful body/abstract/database fallbacks are separately scoped.
  snapshot_sha256: 2698fc638c96fe960aa00aad656412ce52e88cffca821ab4f25f91052e495ca7
- evidence_id: plaque-perez2024-body
  kind: authority
  reference: https://www.annualreviews.org/deliver/fulltext/cellbio/40/1/annurev-cellbio-120823-022747.html?itemId=/content/journals/10.1146/annurev-cellbio-120823-022747&mimeType=html&fmt=ahah
  locator: Actual unsuccessful HTTP source-access response; not scientific article
    content
  accessed_at: '2026-11-03T09:33:49.140996Z'
  support: context_only
  summary: Fresh native route returned HTTP403. No body evidence is inferred from
    this response. Successful body/abstract/database fallbacks are separately scoped.
  snapshot_sha256: 89e0b1c448354654f856afb85a9198710c51db0293b6bf6b38581cf1a95f1cd4
- evidence_id: plaque-root21-sources-keeling2010-jats
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2817223/fullTextXML
  locator: Actual unsuccessful HTTP source-access response; not scientific article
    content
  accessed_at: '2026-11-03T09:33:24.331394Z'
  support: context_only
  summary: Fresh native route returned HTTP500. No body evidence is inferred from
    this response. Successful body/abstract/database fallbacks are separately scoped.
  snapshot_sha256: 5e961c51da999dace26d3bfbbf225f4b09b14fbafd734ff0b042105ddd2ac8f6
- evidence_id: plaque-root21-sources-keeling2010-s3
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2817223.1/PMC2817223.1.xml
  locator: Actual unsuccessful HTTP source-access response; not scientific article
    content
  accessed_at: '2026-11-03T09:33:24.338353Z'
  support: context_only
  summary: Fresh native route returned HTTP404. No body evidence is inferred from
    this response. Successful body/abstract/database fallbacks are separately scoped.
  snapshot_sha256: 7a10bf14e4619c984f91294b5a0e66df2111df20bf8c0debf57f6a89550bf241
- evidence_id: plaque-root21-sources-keeling2010-repository
  kind: authority
  reference: https://marinebiology.pt/beu/files/bib/Keeling2010.pdf
  locator: Actual unsuccessful HTTP source-access response; not scientific article
    content
  accessed_at: '2026-11-03T09:33:24.613871Z'
  support: context_only
  summary: Fresh native route returned HTTP401. No body evidence is inferred from
    this response. Successful body/abstract/database fallbacks are separately scoped.
  snapshot_sha256: 30fe9c4a1ab18b051b0fa152bfca786e5101d182c14d3ffed4969738d9ec60ca
- evidence_id: plaque-root21-sources-keeling2010-bioc
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_xml/PMC2817223/unicode
  locator: Actual unsuccessful HTTP source-access response; not scientific article
    content
  accessed_at: '2026-11-03T09:33:24.770064Z'
  support: context_only
  summary: Fresh native route returned HTTP429. No body evidence is inferred from
    this response. Successful body/abstract/database fallbacks are separately scoped.
  snapshot_sha256: 037c2dbe610ab2a6516d0f0916f7ad3cdfe016739186de59e5eaecd7043d00ba
- evidence_id: plaque-root21-sources-jin2022-publisher
  kind: authority
  reference: https://www.sciencedirect.com/science/article/pii/S0092867422013769
  locator: Actual unsuccessful HTTP source-access response; not scientific article
    content
  accessed_at: '2026-11-03T09:33:24.830448Z'
  support: context_only
  summary: Fresh native route returned HTTP403. No body evidence is inferred from
    this response. Successful body/abstract/database fallbacks are separately scoped.
  snapshot_sha256: 3735308f13c16e5b84c866b5f1a5f0a294cad7f5b1870908a45d6cb3aa66e7ee
- evidence_id: plaque-root21-sources-jin2022-author-publications
  kind: authority
  reference: https://lifesciences.westlake.edu.cn/labs/zhen-yan/structural-biology-laboratory/publications/
  locator: Author laboratory publication listing HTML/embedded metadata; bounded inspection
    for Jin2022 source access
  accessed_at: '2026-11-03T09:33:24.860844Z'
  support: context_only
  summary: The listing was readable but was not used as primary-paper body evidence.
    No full Jin paper or experimental strain is inferred from it.
  snapshot_sha256: f634a6d488c6de60b0889cb28bb8d87e171e26c10293ad64223333d32bc18b03
- evidence_id: plaque-catalogue
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Entire fresh /api/datasets response, every returned organism/dataset entry;
    no pagination
  accessed_at: '2026-11-03T09:33:24.962327Z'
  support: supports
  summary: The catalogue includes Synechococcus elongatus elprecise300 but no Synechocystis
    or Chlamydomonas dataset. PCC7942 is relevant to the cited thylakoid experiments
    only; it cannot be silently substituted for the maintained PCC6803 example. No
    unmatched chloroplast species is substituted and catalogue absence is not biological
    absence.
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: plaque-adapter-meta
  kind: database
  reference: https://imodulondb.org/api/datasets/s_elongatus/elprecise300/meta
  locator: Dataset organism, strains, publication DOI, module/sample/gene counts
  accessed_at: '2026-11-03T09:33:49.141174Z'
  support: supports
  summary: elprecise300 explicitly names S.elongatus PCC7942 and DOI10.1073/pnas.2410492121.
    It is a computational expression dataset, not a membrane-localization or organelle-assembly
    experiment.
  snapshot_sha256: ab1cea70cad9bdb6214c6350d7a8bf92ddddf13bdc928620cbc5ba76badc947f
- evidence_id: plaque-adapter-search-thylakoid
  kind: search
  reference: https://imodulondb.org/api/search?organism=s_elongatus&dataset=elprecise300&query=thylakoid&limit=50
  locator: Actual bounded native search response; relevant gene IDs and module names
    only
  accessed_at: '2026-11-03T09:33:49.141235Z'
  support: supports
  summary: Bounded thylakoid search provides leads for representative PCC7942 photosynthetic
    gene/module cross-checks. A broad cytochrome-oxidase hit is not evidence about
    b6f; text-hit absence is not biological absence.
  search_scope: iModulonDB /api/search organism=s_elongatus dataset=elprecise300 query=thylakoid
    limit=50; executed 2026-11-03T09:33:49.141235+00:00; only returned genes/modules
    inspected, no whole-genome completeness claim.
  snapshot_sha256: de2e39cd5b191d1fc60d4b1d6c0727738b4c24f02c88cfb21ea0ed836b9ab9e2
- evidence_id: plaque-adapter-search-photosystem
  kind: search
  reference: https://imodulondb.org/api/search?organism=s_elongatus&dataset=elprecise300&query=photosystem&limit=50
  locator: Actual bounded native search response; relevant gene IDs and module names
    only
  accessed_at: '2026-11-03T09:33:49.141310Z'
  support: supports
  summary: Bounded photosystem search provides leads for representative PCC7942 photosynthetic
    gene/module cross-checks. A broad cytochrome-oxidase hit is not evidence about
    b6f; text-hit absence is not biological absence.
  search_scope: iModulonDB /api/search organism=s_elongatus dataset=elprecise300 query=photosystem
    limit=50; executed 2026-11-03T09:33:49.141310+00:00; only returned genes/modules
    inspected, no whole-genome completeness claim.
  snapshot_sha256: 72f73baf5ddd33b5afb9073db878e46cc3dca85f09ad8cc87e46c5014e472878
- evidence_id: plaque-adapter-search-cytochrome
  kind: search
  reference: https://imodulondb.org/api/search?organism=s_elongatus&dataset=elprecise300&query=cytochrome&limit=50
  locator: Actual bounded native search response; relevant gene IDs and module names
    only
  accessed_at: '2026-11-03T09:33:49.141403Z'
  support: supports
  summary: Bounded cytochrome search provides leads for representative PCC7942 photosynthetic
    gene/module cross-checks. A broad cytochrome-oxidase hit is not evidence about
    b6f; text-hit absence is not biological absence.
  search_scope: iModulonDB /api/search organism=s_elongatus dataset=elprecise300 query=cytochrome
    limit=50; executed 2026-11-03T09:33:49.141403+00:00; only returned genes/modules
    inspected, no whole-genome completeness claim.
  snapshot_sha256: df5272b019d95a68c635bbfad2dc44353dda0e0e672bcd94b59466c6f2a7760f
- evidence_id: plaque-adapter-search-ATP-synthase
  kind: search
  reference: https://imodulondb.org/api/search?organism=s_elongatus&dataset=elprecise300&query=ATP+synthase&limit=50
  locator: Actual bounded native search response; relevant gene IDs and module names
    only
  accessed_at: '2026-11-03T09:33:49.141458Z'
  support: supports
  summary: Bounded ATP-synthase search provides leads for representative PCC7942 photosynthetic
    gene/module cross-checks. A broad cytochrome-oxidase hit is not evidence about
    b6f; text-hit absence is not biological absence.
  search_scope: iModulonDB /api/search organism=s_elongatus dataset=elprecise300 query=ATP
    synthase limit=50; executed 2026-11-03T09:33:49.141458+00:00; only returned genes/modules
    inspected, no whole-genome completeness claim.
  snapshot_sha256: 18a5d8f23d18d048b25f6d5ba9819772537fc1b613130cb0c8d0b5df8215254a
- evidence_id: plaque-adapter-gene-Synpcc7942_2049
  kind: database
  reference: https://imodulondb.org/api/genes/s_elongatus/elprecise300/Synpcc7942_2049/imodulons
  locator: Exact gene-to-module endpoint; all57 returned membership flags, thresholds
    and selected weights
  accessed_at: '2026-11-03T09:36:37.632385Z'
  support: supports
  summary: 'psaA is above threshold only in module38 Photosystems: weight0.076674881
    versus threshold0.063088206. These are bounded computational context results;
    no localization, essentiality or cross-strain inference follows.'
  snapshot_sha256: 0f0efec038067d4c2e41f6b6d825f909f836e06a77cb16d460c866e76aac4073
- evidence_id: plaque-adapter-gene-Synpcc7942_0424
  kind: database
  reference: https://imodulondb.org/api/genes/s_elongatus/elprecise300/Synpcc7942_0424/imodulons
  locator: Exact gene-to-module endpoint; all57 returned membership flags, thresholds
    and selected weights
  accessed_at: '2026-11-03T09:36:37.632642Z'
  support: supports
  summary: psbA1 has no above-threshold membership among the57 returned modules; this
    is not absence of the gene, PSII or function. These are bounded computational
    context results; no localization, essentiality or cross-strain inference follows.
  snapshot_sha256: e242213845e64fc758b1fec9479d3bb60d501b50df461f5f57f482c563aef45e
- evidence_id: plaque-adapter-gene-Synpcc7942_2331
  kind: database
  reference: https://imodulondb.org/api/genes/s_elongatus/elprecise300/Synpcc7942_2331/imodulons
  locator: Exact gene-to-module endpoint; all57 returned membership flags, thresholds
    and selected weights
  accessed_at: '2026-11-03T09:36:37.632731Z'
  support: supports
  summary: 'petB is above threshold only in module38 Photosystems: weight0.071675474
    versus threshold0.063088206. These are bounded computational context results;
    no localization, essentiality or cross-strain inference follows.'
  snapshot_sha256: c8b7521e1ac670fe08764cec2de07d8f54150eac10984f2a6cbf689830937e4b
- evidence_id: plaque-adapter-gene-Synpcc7942_0336
  kind: database
  reference: https://imodulondb.org/api/genes/s_elongatus/elprecise300/Synpcc7942_0336/imodulons
  locator: Exact gene-to-module endpoint; all57 returned membership flags, thresholds
    and selected weights
  accessed_at: '2026-11-03T09:36:37.632815Z'
  support: supports
  summary: atpA has no above-threshold membership among the57 returned modules; this
    does not refute ATP synthase membership or function. These are bounded computational
    context results; no localization, essentiality or cross-strain inference follows.
  snapshot_sha256: 2794d7d93899d2454920f1ccb4906dd7936bc98718aa79580032f4b8140e7fb5
- evidence_id: plaque-adapter-module-38
  kind: database
  reference: https://imodulondb.org/api/imodulons/s_elongatus/elprecise300/38
  locator: 'Native module metadata: name, function_description, threshold, n_genes
    and regulator; generated summaries excluded'
  accessed_at: '2026-11-03T09:36:37.638022Z'
  support: supports
  summary: Module38 provides bounded photosynthetic-expression context with 44 members.
    Labels are computational annotations, not evidence that every member resides in
    a thylakoid or forms a physical complex.
  snapshot_sha256: 7236e5234640b6a379fa25dc2ac44375ba96a07d69f7a020e06741bcd94c0965
- evidence_id: plaque-adapter-module-38-genes
  kind: database
  reference: https://imodulondb.org/api/imodulons/s_elongatus/elprecise300/38/genes?limit=50
  locator: Native member list requested limit50; all returned gene IDs, names, weights
    and in_imodulon flags; no generated prose
  accessed_at: '2026-11-03T09:36:37.689131Z'
  support: supports
  summary: All 44 returned rows are above-threshold members. Module38 includes psaA/psaB,
    several PSII genes and petB/petD; module1 includes selected PSII and b6f genes.
    This validates specific computational membership only, not complete complex inventories.
  snapshot_sha256: 4c8790c372c142c3fb6c0b72582164af9b1d29e1bb180245ce2b49c493b8b9dd
- evidence_id: plaque-adapter-module-1
  kind: database
  reference: https://imodulondb.org/api/imodulons/s_elongatus/elprecise300/1
  locator: 'Native module metadata: name, function_description, threshold, n_genes
    and regulator; generated summaries excluded'
  accessed_at: '2026-11-03T09:36:37.691184Z'
  support: supports
  summary: Module1 provides bounded photosynthetic-expression context with 21 members.
    Labels are computational annotations, not evidence that every member resides in
    a thylakoid or forms a physical complex.
  snapshot_sha256: fe180c45de0f7400ffc349de6340de2a5f2fa1530e48f7995d8adcb60c9f0c59
- evidence_id: plaque-adapter-module-1-genes
  kind: database
  reference: https://imodulondb.org/api/imodulons/s_elongatus/elprecise300/1/genes?limit=50
  locator: Native member list requested limit50; all returned gene IDs, names, weights
    and in_imodulon flags; no generated prose
  accessed_at: '2026-11-03T09:36:37.693502Z'
  support: supports
  summary: All 21 returned rows are above-threshold members. Module38 includes psaA/psaB,
    several PSII genes and petB/petD; module1 includes selected PSII and b6f genes.
    This validates specific computational membership only, not complete complex inventories.
  snapshot_sha256: 5e609cf72cb90d203f4621ef96ca31187d551d8ff327a7052cc48c763d470539
- evidence_id: plaque-adapter-publication
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1073/pnas.2410492121&format=json&resultType=core&pageSize=5
  locator: Exact DOI query; primary abstract and bibliographic identity only
  accessed_at: '2026-11-03T09:36:37.695062Z'
  support: supports
  summary: The cited elprecise300 paper decomposes300 PCC7942 RNA-seq datasets into57
    independently modulated gene sets. Its abstract supports the computational provenance
    and photosynthesis context, not membrane localization, growth essentiality or
    biological absence.
  snapshot_sha256: 55d03cba0ef7bd21e6b3695663b6ae4a237f024df909a0ee9bc2ff0c6cf33299
- evidence_id: plaque-historical-runner
  kind: validation
  reference: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb datasets
  locator: Historical00:49Z receipt and stdout/stderr independently reread and hash-verified;
    no fresh invocation
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  summary: The historical runner exited1 before dataset execution due OS PermissionError
    reading pyvenv.cfg. Current independently fetched source endpoints are the permitted
    fallback; source success is not runner execution.
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: plaque-native-bacterial_thylakoid-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/bacterial_thylakoid.yaml
    --verify
  locator: Actual root-owned receipt and exact stdout log independently read and hash-verified
  accessed_at: '2026-11-03T09:32:47.532598Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: plaque-native-bacterial_thylakoid-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/bacterial_thylakoid.yaml
    --causal-graphs
  locator: Actual root-owned receipt and exact stdout log independently read and hash-verified
  accessed_at: '2026-11-03T09:32:47.959780Z'
  support: supports
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
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
- evidence_id: plaque-native-chloroplast_inner_membrane-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chloroplast_inner_membrane.yaml
    --verify
  locator: Actual root-owned receipt and exact stdout log independently read and hash-verified
  accessed_at: '2026-11-03T09:32:51.786683Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: plaque-native-chloroplast_inner_membrane-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chloroplast_inner_membrane.yaml
    --causal-graphs
  locator: Actual root-owned receipt and exact stdout log independently read and hash-verified
  accessed_at: '2026-11-03T09:32:52.232345Z'
  support: supports
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
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
- evidence_id: plaque-native-chloroplast_intermembrane_space-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chloroplast_intermembrane_space.yaml
    --verify
  locator: Actual root-owned receipt and exact stdout log independently read and hash-verified
  accessed_at: '2026-11-03T09:32:52.677694Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: plaque-native-chloroplast_intermembrane_space-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chloroplast_intermembrane_space.yaml
    --causal-graphs
  locator: Actual root-owned receipt and exact stdout log independently read and hash-verified
  accessed_at: '2026-11-03T09:32:53.120917Z'
  support: supports
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
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
- evidence_id: micro-review-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Evidence Rules; Structured Source Cross-Checks; Missing Things; Workflow
  accessed_at: '2026-11-03T09:42:05.676895Z'
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
  summary: Native read-only source review. Named genes/proteins/pathways/stress responses
    trigger applicability assessment, independent of an expression claim. Catalogue
    absence is not negative biological evidence.
  support: supports
- evidence_id: micro-review-config
  kind: authority
  reference: conf/record_review.yaml
  locator: version1 review skills, rubrics and repository routing
  accessed_at: '2026-11-03T09:42:05.676895Z'
  snapshot_sha256: d3334a12b8a616a7638f1195748085d2b543fba7df67ad4ff8fcc0ac18f2d3ee
  summary: The current frozen configuration, skill and profile were reread; the seventeen
    common policy/schema/verifier inputs are unchanged from the prior independently
    reviewed cohort. No additional local scientific record was used outside the four
    assigned frozen targets.
  support: supports
- evidence_id: micro-review-profile
  kind: authority
  reference: docs/record-review-profile.md
  locator: Required scientific coverage; verdict and native validation profile
  accessed_at: '2026-11-03T09:42:05.676895Z'
  snapshot_sha256: 6a49c8d35f0a94082a9ad0b8bd8c6a929d85de8339141955f3779bd7ab0eb7e4
  summary: Separate scientific curation from review-bundle repairs; retain immutable
    observations and native scope/severity. A new issue-bearing batch may contain
    supported clean target assessments.
  support: supports
- evidence_id: micro-graph-contract
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Graph scope, evidence and necessity contract
  accessed_at: '2026-11-03T09:42:05.676895Z'
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
  summary: Coarse NONMECHANISTIC functional/topological graphs must not be treated
    as complete mechanistic models. Protein identity, localization, functional dependency
    and constituent essentiality are different claims.
  support: supports
- evidence_id: micro-review-schema
  kind: authority
  reference: schema/record_review.yaml
  locator: EvidenceKind; Support; Area; AssessmentOutcome; FindingReference
  accessed_at: '2026-11-03T09:42:05.676895Z'
  snapshot_sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
  summary: Secondary literature is explicitly labeled and encoded authority/context_only;
    schema is the permitted assessment area; every predecessor identifies repository,
    review and finding.
  support: supports
- evidence_id: micro-original-validation-inputs
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/adversary-microtubule/original-validation-inputs.json
  locator: Four exact original native validate/render runs and original-source git
    blob hashes
  accessed_at: '2026-11-03T09:33:33.412186Z'
  snapshot_sha256: 0924d04dcc47688cd52e4a15a26b6b147c955162dfaa63f4394fc77e5f03d739
  summary: All four original bundles validate; native render --content equals original
    Markdown byte for byte. Original frozen target hashes match original source revision9c0446c4.
    Current autophagosome and chitosome hashes differ; lumen and membrane match. Historical
    commands are not recast as current-head whole-corpus tests.
  support: supports
- evidence_id: micro-record-autophagosome
  kind: record_content
  reference: data/structures/membrane_organelle/autophagosome.yaml
  locator: Entire current YAML at e721920f30c72a6c35cecb9913c6780e18a460ed
  accessed_at: '2026-11-03T09:42:05.676895Z'
  snapshot_sha256: 08c1df95826ee2cb8b86b66592876f324eae999c7cafdc619d1ffad1607f6232
  summary: Current complete record inspected, including identity, components, functions,
    graph nodes/edges, scope notes, taxon examples, discussions, citations and curation
    history; changed from frozen original input.
  support: supports
- evidence_id: micro-prior-autophagosome
  kind: prior_review
  reference: reviews/structured/20261021T110741Z-autophagosome-audit/review.yaml
  locator: Entire immutable YAML and deterministic Markdown; findings, actions, checks
    and frozen source
  accessed_at: '2026-11-03T09:42:05.676895Z'
  snapshot_sha256: 18417b1f2d56272090dd09e3eb52dab6c976ec104e8cfce11319408847dccbb4
  summary: Original 20261021T110741Z-autophagosome-audit retained without mutation.
    Original verdict pass_with_limitations; 0 original scientific finding(s). Current
    reassessment does not rewrite original access dates or global-check provenance.
  support: supports
- evidence_id: micro-native-autophagosome-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/autophagosome-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/autophagosome.yaml
    --verify; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/autophagosome-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T09:32:45.016091Z'
  snapshot_sha256: f72a66871efce1f717dfa44438e5a617bc497ec3f9cdaeb508f1e1001a93c5f9
  summary: Actual exit0 at source e721920f30c72a6c35cecb9913c6780e18a460ed, 2026-11-03T09:32:44.624086+00:00
    to 2026-11-03T09:32:45.016091+00:00. Empty protein-example inventory and zero
    GENE_OR_PROTEIN nodes; this is a successful empty-scope structural check, not
    experimental protein evidence. Identity/coverage success does not establish membership
    or necessity.
  support: supports
- evidence_id: micro-native-autophagosome-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/autophagosome-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/autophagosome.yaml
    --causal-graphs; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/autophagosome-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-03T09:32:45.428758Z'
  snapshot_sha256: 78d352bdf3fa58c84353be07cb8ea88e7c15b03dc93e9c806bb5b1524e2059bd
  summary: Actual exit0 at source e721920f30c72a6c35cecb9913c6780e18a460ed, 2026-11-03T09:32:45.045818+00:00
    to 2026-11-03T09:32:45.428758+00:00. Empty protein-example inventory and zero
    GENE_OR_PROTEIN nodes; this is a successful empty-scope structural check, not
    experimental protein evidence. Identity/coverage success does not establish membership
    or necessity.
  support: supports
- evidence_id: micro-record-autophagosome_lumen
  kind: record_content
  reference: data/structures/membrane_organelle/autophagosome_lumen.yaml
  locator: Entire current YAML at e721920f30c72a6c35cecb9913c6780e18a460ed
  accessed_at: '2026-11-03T09:42:05.676895Z'
  snapshot_sha256: 33fbf9f3ae1591081dd1e113d0fd7476c64bdafaa238ec35c7705fb89bb0f98d
  summary: Current complete record inspected, including identity, components, functions,
    graph nodes/edges, scope notes, taxon examples, discussions, citations and curation
    history; identical to frozen original input.
  support: supports
- evidence_id: micro-prior-autophagosome_lumen
  kind: prior_review
  reference: reviews/structured/20261021T110744Z-autophagosome-lumen-audit/review.yaml
  locator: Entire immutable YAML and deterministic Markdown; findings, actions, checks
    and frozen source
  accessed_at: '2026-11-03T09:42:05.676895Z'
  snapshot_sha256: 6f417e89968139de6fc68836753c3ed68851e18f30bd98b3211ed692400e51ad
  summary: Original 20261021T110744Z-autophagosome-lumen-audit retained without mutation.
    Original verdict pass_with_limitations; 0 original scientific finding(s). Current
    reassessment does not rewrite original access dates or global-check provenance.
  support: supports
- evidence_id: micro-native-autophagosome_lumen-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/autophagosome_lumen-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/autophagosome_lumen.yaml
    --verify; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/autophagosome_lumen-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T09:32:45.851535Z'
  snapshot_sha256: a56f1e4bccadaca8ed170ad8afd8e54641d6d9bdeb8449a094838ff9573d07dd
  summary: Actual exit0 at source e721920f30c72a6c35cecb9913c6780e18a460ed, 2026-11-03T09:32:45.458837+00:00
    to 2026-11-03T09:32:45.851535+00:00. Empty protein-example inventory and zero
    GENE_OR_PROTEIN nodes; this is a successful empty-scope structural check, not
    experimental protein evidence. Identity/coverage success does not establish membership
    or necessity.
  support: supports
- evidence_id: micro-native-autophagosome_lumen-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/autophagosome_lumen-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/autophagosome_lumen.yaml
    --causal-graphs; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/autophagosome_lumen-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-03T09:32:46.264565Z'
  snapshot_sha256: 18e50222e7f50346bd77423b722dc7adf1f4d903ff33d47521eeb2480dc8866a
  summary: Actual exit0 at source e721920f30c72a6c35cecb9913c6780e18a460ed, 2026-11-03T09:32:45.882420+00:00
    to 2026-11-03T09:32:46.264565+00:00. Empty protein-example inventory and zero
    GENE_OR_PROTEIN nodes; this is a successful empty-scope structural check, not
    experimental protein evidence. Identity/coverage success does not establish membership
    or necessity.
  support: supports
- evidence_id: micro-record-autophagosome_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/autophagosome_membrane.yaml
  locator: Entire current YAML at e721920f30c72a6c35cecb9913c6780e18a460ed
  accessed_at: '2026-11-03T09:42:05.676895Z'
  snapshot_sha256: aa651db3a9b5a208ae7a4deef9d3595d79c0296cda8ebdc9a1c524a11b948254
  summary: Current complete record inspected, including identity, components, functions,
    graph nodes/edges, scope notes, taxon examples, discussions, citations and curation
    history; identical to frozen original input.
  support: supports
- evidence_id: micro-prior-autophagosome_membrane
  kind: prior_review
  reference: reviews/structured/20261021T110747Z-autophagosome-membrane-audit/review.yaml
  locator: Entire immutable YAML and deterministic Markdown; findings, actions, checks
    and frozen source
  accessed_at: '2026-11-03T09:42:05.676895Z'
  snapshot_sha256: 64f2d8ab01bf1550f71fcbf450bee87417f10e5edc36d6532f097e4098ad8ab0
  summary: Original 20261021T110747Z-autophagosome-membrane-audit retained without
    mutation. Original verdict pass_with_limitations; 0 original scientific finding(s).
    Current reassessment does not rewrite original access dates or global-check provenance.
  support: supports
- evidence_id: micro-native-autophagosome_membrane-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/autophagosome_membrane-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/autophagosome_membrane.yaml
    --verify; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/autophagosome_membrane-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T09:32:46.690900Z'
  snapshot_sha256: f9dd1fb0bb98809fa07c356a7f479ebac48e4a1d30956547064be70b11f1fcd8
  summary: Actual exit0 at source e721920f30c72a6c35cecb9913c6780e18a460ed, 2026-11-03T09:32:46.295572+00:00
    to 2026-11-03T09:32:46.690900+00:00. Empty protein-example inventory and zero
    GENE_OR_PROTEIN nodes; this is a successful empty-scope structural check, not
    experimental protein evidence. Identity/coverage success does not establish membership
    or necessity.
  support: supports
- evidence_id: micro-native-autophagosome_membrane-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/autophagosome_membrane-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/autophagosome_membrane.yaml
    --causal-graphs; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/autophagosome_membrane-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-03T09:32:47.107463Z'
  snapshot_sha256: 64d5054a1f37d8373bc0613f7b8d1f87da5407bad5420d2fd1ff24fd17b93808
  summary: Actual exit0 at source e721920f30c72a6c35cecb9913c6780e18a460ed, 2026-11-03T09:32:46.720855+00:00
    to 2026-11-03T09:32:47.107463+00:00. Empty protein-example inventory and zero
    GENE_OR_PROTEIN nodes; this is a successful empty-scope structural check, not
    experimental protein evidence. Identity/coverage success does not establish membership
    or necessity.
  support: supports
- evidence_id: micro-record-chitosome
  kind: record_content
  reference: data/structures/membrane_organelle/chitosome.yaml
  locator: Entire current YAML at e721920f30c72a6c35cecb9913c6780e18a460ed
  accessed_at: '2026-11-03T09:42:05.676895Z'
  snapshot_sha256: ec564f818b649f3c4c8a56de6d6bea798eded59e73f1c4b840325eb83b9d5493
  summary: Current complete record inspected, including identity, components, functions,
    graph nodes/edges, scope notes, taxon examples, discussions, citations and curation
    history; changed from frozen original input.
  support: supports
- evidence_id: micro-prior-chitosome
  kind: prior_review
  reference: reviews/structured/20261021T110752Z-chitosome-audit/review.yaml
  locator: Entire immutable YAML and deterministic Markdown; findings, actions, checks
    and frozen source
  accessed_at: '2026-11-03T09:42:05.676895Z'
  snapshot_sha256: 99af0b9628e6b9af0c5713c89658610c7e2cc5a3a7c947993210b4da76a51b53
  summary: Original 20261021T110752Z-chitosome-audit retained without mutation. Original
    verdict needs_curation; 1 original scientific finding(s). Current reassessment
    does not rewrite original access dates or global-check provenance.
  support: supports
- evidence_id: micro-native-chitosome-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/chitosome-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chitosome.yaml
    --verify; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/chitosome-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T09:32:49.169761Z'
  snapshot_sha256: 595c55944255cd6c8d597f6c98611b581066851dca6518be56081f67740a4c70
  summary: Actual exit0 at source e721920f30c72a6c35cecb9913c6780e18a460ed, 2026-11-03T09:32:47.989875+00:00
    to 2026-11-03T09:32:49.169761+00:00. Two reviewed protein examples CHS1/P08004
    and CHS3/P29465; one GENE_OR_PROTEIN node COVERED by the same component examples.
    Identity/coverage success does not establish membership or necessity.
  support: supports
- evidence_id: micro-native-chitosome-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/chitosome-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/chitosome.yaml
    --causal-graphs; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/chitosome-uniprot-causal.log
    SHA256 4e39579edbac102eb474e951a3f5210ea7d1bbe4ce137cc84e38915fca388d63
  accessed_at: '2026-11-03T09:32:49.595030Z'
  snapshot_sha256: 49f54385bfd74c6d5ad5f347f96ef6de17510ebbd63e989933f1f9a88c433fbc
  summary: Actual exit0 at source e721920f30c72a6c35cecb9913c6780e18a460ed, 2026-11-03T09:32:49.201704+00:00
    to 2026-11-03T09:32:49.595030+00:00. Two reviewed protein examples CHS1/P08004
    and CHS3/P29465; one GENE_OR_PROTEIN node COVERED by the same component examples.
    Identity/coverage success does not establish membership or necessity.
  support: supports
- evidence_id: micro-auto-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005776,GO:0000421,GO:0034423,GO:0060205,GO:0030659,GO:0016236,GO:0061909,GO:0000324
  locator: Exact QuickGO term records GO:0005776/0000421/0034423/0060205/0030659/0016236/0061909/0000324;
    names, definitions, synonyms, active status and children
  accessed_at: '2026-11-03T09:33:03.428217Z'
  snapshot_sha256: fe74c39bb2d12700df800c03833e04ab0657e0ce6e25675ee35f98fe8b2d5a85
  summary: Active exact terms distinguish autophagosome, its membrane and lumen, macroautophagy,
    fusion and fungal vacuole. GO:0016236 proceeds through autophagosome formation.
    GO:0061909 explicitly includes the yeast vacuole endpoint. Synonym scopes and
    resident-lumen annotation caution are retained.
  support: supports
- evidence_id: micro-auto-SL-0022-json
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0022.json
  locator: UniProt subcellular location SL-0022 definition, synonyms, geneOntologies,
    isA and partOf
  accessed_at: '2026-11-03T09:33:03.428551Z'
  snapshot_sha256: eabd5326015a1e721e992120feec2b465d2137e7df7110ec6bcc3600fae87726
  summary: Autophagosome membrane maps to GO:0000421; the three record synonyms are
    supplied; isA cytoplasmic vesicle membrane and partOf autophagosome support the
    modeled relations. These are UniProt assertions, not claims about current direct
    GO parentage.
  support: supports
- evidence_id: micro-auto-SL-0318-json
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0318.json
  locator: UniProt subcellular location SL-0318 definition, synonyms, geneOntologies,
    isA and partOf
  accessed_at: '2026-11-03T09:33:03.428608Z'
  snapshot_sha256: ebef9b962bb00a5283ab0b9c024255499af7ceb9ebd05dec11e14fa5c9ded695
  summary: Autophagosome lumen maps to GO:0034423; its three synonyms, isA cytoplasmic
    vesicle lumen and partOf autophagosome are explicit. Degradation cargo is not
    inferred to be a constitutive lumen component.
  support: supports
- evidence_id: micro-auto-taxon-4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: ENA taxonomy exact4932 scientificName/rank/lineage
  accessed_at: '2026-11-03T09:33:03.428652Z'
  snapshot_sha256: 38f43dd1593a1d47416228ae385464f30aeb8302c3aadb45b3588d03744bc814
  summary: NCBITaxon:4932 is Saccharomyces cerevisiae at species rank, within Fungi.
    It is distinct from the narrower S288C strain identifier.
  support: supports
- evidence_id: micro-auto-takeshige1992-xml
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2289660.1/PMC2289660.1.xml
  locator: DOI10.1083/jcb.119.2.301; JATS abstract; OCR Introduction, Methods, initial
    Results on body appearance and starvation conditions; complete Discussion
  accessed_at: '2026-11-03T09:33:04.028243Z'
  snapshot_sha256: d9234befa5757085ce8dd6be2333dbe0c6a49f3ae59c87f8904818a0f51ceec2
  summary: Yeast proteinase-deficient and PMSF-treated wild-type experiments support
    starvation-associated vacuolar autophagic bodies and cytoplasmic cargo delivery.
    The Discussion explicitly leaves body-formation mechanism unresolved; this paper
    alone is not a direct molecular fusion assay. OCR text inspected; no figure pixels
    or raw data inspected.
  support: supports
- evidence_id: micro-auto-suzuki2001-publisher
  kind: primary_source
  reference: https://www.embopress.org/doi/full/10.1093/emboj/20.21.5971
  locator: DOI10.1093/emboj/20.21.5971; publisher Abstract, Introduction, Results
    PAS/localization and genetic grouping, Discussion Sec8, Methods Sec11
  accessed_at: '2026-11-03T09:33:04.032273Z'
  snapshot_sha256: d67a9129af86f3d815f722baaf1e311c43d1725e7b69678f9625af493de0009b
  summary: Physiological fluorescent fusions, mutant localization and autophagy assays
    support budding yeast as a genetic/fluorescence model and distinguish PAS organization
    from mature autophagosomes. APG protein participation is not a universal mature-organelle
    membership or stoichiometry claim. Selected Results narratives and complete Discussion/Methods
    inspected; no figure pixels.
  support: supports
- evidence_id: micro-auto-xie2007-publisher
  kind: authority
  reference: https://www.nature.com/articles/ncb1007-1102
  locator: DOI10.1038/ncb1007-1102; publisher title and complete abstract only
  accessed_at: '2026-11-03T09:33:04.041778Z'
  snapshot_sha256: 203ae18301d5f8048ade90842370a221dd9e864a1eb59d0ff2d72dfdc336a9ba
  summary: Secondary review abstract supplies context for double-membrane autophagosome
    formation and core machinery. No current full-body or PDF access is claimed; broad
    context is not independent experimental validation.
  support: context_only
- evidence_id: micro-auto-ichimura2000-publisher
  kind: primary_source
  reference: https://www.nature.com/articles/35044114
  locator: DOI10.1038/35044114; publisher title and complete abstract only
  accessed_at: '2026-11-03T09:33:04.066112Z'
  snapshot_sha256: 01864bb746b194966692cc3c2dbc764644adea514e774995a052338218c41c12
  summary: Primary abstract establishes Apg8 conjugation to phosphatidylethanolamine
    through a ubiquitin-like system. Supports the bounded lipidation TODO context,
    not a complete current protein inventory or inspected full methods.
  support: partial
- evidence_id: micro-chito-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0045009,GO:0031410,GO:0005886,GO:0030428
  locator: QuickGO exact GO:0045009/0031410/0005886/0030428 active records, definitions
    and children
  accessed_at: '2026-11-03T09:33:04.073036Z'
  snapshot_sha256: 3a8c2319d7dcd662445edde2e22b70808dbe684e52a6c61eb52b0902fea873f9
  summary: Chitosome is a membrane-bounded fungal chitin-synthase particle/cytoplasmic
    vesicle with a proposed reservoir-to-septum role. Plasma membrane and cell septum
    graph endpoints are active correctly named terms; regulated septum delivery remains
    proposed.
  support: supports
- evidence_id: micro-chito-go-parts
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030661,GO:0033162
  locator: QuickGO exact GO:0030661 name/definition/isObsolete and GO:0045009 child
    relation in paired chito-go response
  accessed_at: '2026-11-03T09:33:04.294174Z'
  snapshot_sha256: e8c2ee2e0b71c77ecf3017af483e57a2825907545636b5502e65a05465b8e2df
  summary: GO:0030661 is the active exact chitosome membrane term, defined as the
    lipid bilayer surrounding a chitosome. GO:0045009 lists it through part_of. This
    contradicts the current no-exact-membrane-term rationale; unrelated queried GO:0033162
    is not used for a record inference.
  support: supports
- evidence_id: micro-chito-chebi17029
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17029
  locator: OLS ChEBI exact17029 embedded term, label, definition, ontology identifier
    and obsolete flag
  accessed_at: '2026-11-03T09:33:04.413216Z'
  snapshot_sha256: a246bef2108be925e56d8768f8c27c89aaede533a7fe4ba246aeed52355e658c
  summary: CHEBI:17029 denotes chitin, a beta(1→4)-linked N-acetyl-D-glucosamine polymer.
    The graph represents a synthesis product, not a resident chitosome constituent.
  support: supports
- evidence_id: micro-chito-tax-4751
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4751
  locator: ENA exact4751 scientificName/rank/lineage
  accessed_at: '2026-11-03T09:33:04.670807Z'
  snapshot_sha256: a7bab59bce650c0d29732327d4e7e342f1b648747f7f9635958f923b4a6089e6
  summary: NCBITaxon:4751 denotes Fungi; authority identity does not establish universal
    structure occurrence.
  support: supports
- evidence_id: micro-chito-tax-559292
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: ENA exact559292 scientificName/rank/lineage
  accessed_at: '2026-11-03T09:33:05.018133Z'
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
  summary: NCBITaxon:559292 denotes Saccharomyces cerevisiae S288C at strain rank;
    the related pathway and protein examples use this narrower scope.
  support: supports
- evidence_id: micro-chito-leal1988-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1073%2Fpnas.85.22.8516&format=json&resultType=core
  locator: 'DOI10.1073/pnas.85.22.8516 exact Europe PMC core result: title and complete
    abstract'
  accessed_at: '2026-11-03T09:33:05.537243Z'
  snapshot_sha256: 878b2f0e97931b07893d402419f3a588adc10a86dc788dec9d8a7cf6ebdd1b02
  summary: Primary abstract resolves low-density chitosome and plasma-membrane populations
    from yeast homogenates, with mostly zymogenic synthase and unresolved ultimate
    active-enzyme location. Supports vesicle distinction, not a demonstrated universal
    delivery/activation mechanism. Full primary body and figure pixels not inspected.
  support: partial
- evidence_id: micro-chito-jats-PMC2132460
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2132460.1/PMC2132460.1.xml
  locator: DOI10.1083/jcb.136.1.95; JATS abstract, Methods yeast strains/tagging/immunofluorescence,
    Results Chs3 glycosylation/polarization/Chs5/mating and all five Discussion subsections
  accessed_at: '2026-11-03T09:33:05.907626Z'
  snapshot_sha256: ac284c0c2cf5124a2fa5947b7405732415ed0d657f35be8a943f3eb2211a0112
  summary: Functional tagged Chs3 localization and chs5/myo2 perturbations support
    polarized yeast cell-surface targeting. The discussion treats late/post-Golgi
    patch identities and detailed transport models as hypotheses. Read claim-bearing
    text; no figure pixels, raw images or supplemental data examined.
  support: supports
- evidence_id: micro-chito-ziman1998-browser-discussion
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC25385/
  locator: DOI10.1091/mbc.9.6.1565; complete PMC primary abstract, Introduction, Methods,
    Results narratives and Discussion
  accessed_at: '2026-11-03T09:33:06.177429Z'
  snapshot_sha256: 8a190e0192c526e1f09ad1bad3d6884ee1df116d92d8d518065e8b37d4a8ad59
  summary: Chs6-dependent Chs3 anterograde transport supports the new plasma-membrane
    delivery endpoint. Chs1 traffic differs; activation alternatives remain unresolved
    in Discussion. The new NONMECHANISTIC edge is accepted for delivery purpose, not
    as proof transport alone activates every fungal synthase. No figure-pixel inspection.
  support: supports
- evidence_id: micro-chito-bartnicki2006-pdf
  kind: authority
  reference: https://www.davidmoore.org.uk/21st_Century_Guidebook_to_Fungi_PLATINUM/REPRINT_collection/Bartnicki-Garcia_chitosomes2006.pdf
  locator: DOI10.1111/j.1567-1364.2006.00158.x; genuine downloaded PDF, extracted
    text pp957–964 through Conclusion; captions text only
  accessed_at: '2026-11-03T09:33:05.905156Z'
  snapshot_sha256: e8071dd556203864ae1d31963e73c344a2bf9f3f210d8bf8bb6f3a958def993d
  summary: Secondary minireview covers fungal chitosome evidence, zymogenicity, delivery,
    opposing interpretations of endocytic origin and unresolved ontogeny/activation.
    It supports bounded multi-lineage context, not a universal fungal frequency or
    settled biogenesis mechanism. PDF text read; embedded pixels not inspected.
  support: context_only
- evidence_id: micro-chito-P08004
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P08004.json
  locator: 'UniProtKB complete entry: accession/status/gene/taxon; function and subcellular-location
    comments and evidence references'
  accessed_at: '2026-11-03T09:33:06.252275Z'
  snapshot_sha256: a2d134e2e1ca0e5fa1e6ffcc0cbabfd557544af36d14a885afde32238ed3e763
  summary: P08004 is the reviewed S288C entry for CHS1. Identity is distinct from
    chitosome membership or essentiality. CHS1 is distinct from CHS3 and does not
    inherit its Chs6-dependent trafficking result.
  support: supports
- evidence_id: micro-chito-P29465
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P29465.json
  locator: 'UniProtKB complete entry: accession/status/gene/taxon; function and subcellular-location
    comments and evidence references'
  accessed_at: '2026-11-03T09:33:06.378057Z'
  snapshot_sha256: 63f91ca6bb09dd735b34f1430f55a85d5a0ba4c48ba7d2b31e76e02187dda1a0
  summary: P29465 is the reviewed S288C entry for CHS3. Identity is distinct from
    chitosome membership or essentiality. P29465 Cell membrane annotations cite all
    three record PMIDs; these are not relabeled as chitosome-localization experiments.
  support: supports
- evidence_id: micro-chito-reviewed-uniqueness
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A559292+AND+%28gene_exact%3ACHS1+OR+gene_exact%3ACHS3%29&format=json&size=500
  locator: UniProt REST reviewed S288C exact gene-symbol query, two results and response
    pagination metadata
  accessed_at: '2026-11-03T09:33:06.426663Z'
  snapshot_sha256: 576c4d50fc66040e399deb527cd60a1693c1897e7b3a511d05d5b697beffdf94
  summary: The bounded reviewed S288C query returns one CHS1/P08004 and one CHS3/P29465
    entry. This verifies uniqueness within that query, not across all fungi or unreviewed
    entries.
  support: supports
  search_scope: UniProtKB REST search on 2026-11-03 at 09:33:06Z; query reviewed:true
    AND organism_id:559292 AND (gene_exact:CHS1 OR gene_exact:CHS3); format=json,
    size=500; returned2 reviewed entries and no next-page link. Restricted to two
    exact symbols and S288C; no global fungal absence or paralog-exhaustiveness claim.
- evidence_id: micro-chito-PMID-12928491
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12928491+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact cited PMID Europe PMC core record; title, author/year and complete
    abstract
  accessed_at: '2026-11-03T09:33:06.571963Z'
  snapshot_sha256: f33d7af399148a938819b3e9c9f41c0726f91f2c5ac1356041e3e828acb8d9e0
  summary: Primary abstract reports stress-responsive Rho1/Pkc1-dependent Chs3 mobilization
    from internal stores to plasma membrane. The actual UniProt Cell membrane reference
    matches; body, methods and image data were not inspected.
  support: partial
- evidence_id: micro-chito-PMID-17519287
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A17519287+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact cited PMID Europe PMC core record; title, author/year and complete
    abstract
  accessed_at: '2026-11-03T09:33:06.607393Z'
  snapshot_sha256: 834e16478cb586a2df18db7e9f98107748bf37246cbda12ed08a833d17e44cac
  summary: Primary abstract separates Chs3 delivery from productive Chs4-associated
    plasma-membrane activity and rapid endocytosis. The actual UniProt Cell membrane
    reference matches; body, methods and image data were not inspected.
  support: partial
- evidence_id: micro-chito-PMID-28346351
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A28346351+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact cited PMID Europe PMC core record; title, author/year and complete
    abstract
  accessed_at: '2026-11-03T09:33:07.063359Z'
  snapshot_sha256: aae352bcf07ffcfdb03439f01792585eee8e883cc2c942c8d9128bae4c0055ca
  summary: Primary abstract supports Chs3 membrane organization and oligomeric/localization
    study scope. The actual UniProt Cell membrane reference matches; body, methods
    and image data were not inspected.
  support: partial
- evidence_id: micro-chito-IPR004835
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004835/
  locator: InterPro entry metadata, family description and cross-family scope
  accessed_at: '2026-11-03T09:33:07.184536Z'
  snapshot_sha256: 4ea95627f5806df27f8e91b2a42796b48fa75c88915491138530003e40425061
  summary: IPR004835 Chitin synthase is a broad family across fungi and animals; its
    existence does not itself prove every chitosome biochemical cargo class is one
    exact curated fungal family.
  support: supports
- evidence_id: micro-chito-ipr-matches-P08004
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P08004/?page_size=200
  locator: InterPro protein-entry match list, count3, next=null, type and accession
    for each result
  accessed_at: '2026-11-03T09:33:07.193916Z'
  snapshot_sha256: 2fb845200fde3b061a28ed9a023cf60beab2e1a47a3228f2c6e64122dd147b8e
  summary: The declared example maps to IPR004835 Chitin synthase, with additional
    domain/superfamily matches. This confirms example-family membership; it neither
    localizes all family members to chitosomes nor determines a universal isoenzyme
    cohort.
  support: supports
- evidence_id: micro-chito-ipr-matches-P29465
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P29465/?page_size=200
  locator: InterPro protein-entry match list, count3, next=null, type and accession
    for each result
  accessed_at: '2026-11-03T09:33:07.211126Z'
  snapshot_sha256: 1851ce85abaea603ab3695517705aaebded413c0df291bd74c1b6b461427616c
  summary: The declared example maps to IPR004835 Chitin synthase, with additional
    domain/superfamily matches. This confirms example-family membership; it neither
    localizes all family members to chitosomes nor determines a universal isoenzyme
    cohort.
  support: supports
- evidence_id: micro-pathway-commit
  kind: record_content
  reference: https://raw.githubusercontent.com/CultureBotAI/PathwayMech/d8ec2b69f7a4c615aecddff80498fef1e1fab0ce/data/pathways/chitin-biosynthesis.yaml
  locator: Exact remote PathwayMech commit d8ec2b69f7a4c615aecddff80498fef1e1fab0ce;
    pathway id/taxon/participants and CHS3 enables edge003
  accessed_at: '2026-11-03T09:33:07.726762Z'
  snapshot_sha256: d02205589a895098dc0a361cd0134f3075895103db2db82f21a1e36d56572a1a
  summary: The declared chitin-biosynthesis model exists at the pinned public commit,
    taxon559292; CHS3 SGD:S000000227 is an explicit participant enabling a chitin-synthase
    reaction. The link is enzyme delivery, not catalysis inside chitosomes. Remote
    model bytes inspected; no local sibling-repository input was used.
  support: supports
- evidence_id: micro-adapter-catalogue
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Complete iModulonDB /api/datasets response, all20 organism rows/28 organism-dataset
    pairs
  accessed_at: '2026-11-03T09:33:07.339002Z'
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  summary: Fresh catalogue inspection finds no Saccharomyces or other fungal organism/dataset
    match. No supported organism key is available for a target-specific downstream
    gene/module query; this is database coverage only, not absence of the proteins/pathways.
  support: supports
- evidence_id: micro-historical-adapter-runner
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Retained actual imodulondb datasets runner receipt from 00:49Z; command,
    timestamps, exit1 and PermissionError reason
  accessed_at: '2026-11-03T00:49:00.863225Z'
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  summary: Historical runner attempt 2026-11-03T00:49:00.848907Z–00:49:00.863225Z
    failed because pyvenv.cfg could not be read. This retained receipt is not a new
    run or evidence of current service failure; the fresh inspected source catalogue
    is the present fallback.
  support: context_only
- evidence_id: septin-native-review-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Structured Source Cross-Checks and native immutable review workflow
  summary: Named genes, accessions and pathways require applicability assessment;
    lack of expression claims does not exempt a target. Unmatched organism coverage
    permits bounded downstream non-applicability. Review-only source capture and append-only
    successor workflow apply.
  accessed_at: '2026-11-03T09:40:10.095108Z'
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
  support: supports
- evidence_id: septin-native-curation-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Identity, component boundaries, evidence and necessity
  summary: Exact structure identity, class-level components, representative proteins,
    localizations, functions and structure-formation dependencies require distinct
    evidence.
  accessed_at: '2026-11-03T09:40:10.095108Z'
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
  support: supports
- evidence_id: septin-native-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Graph kinds, NONMECHANISTIC scope and protein evidence contract
  summary: Topology graphs may retain stated coarse scope; a protein xref still must
    identify the represented actor. Identifier success does not prove localization
    or mechanism.
  accessed_at: '2026-11-03T09:40:10.095108Z'
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
  support: supports
- evidence_id: septin-record-apicoplast_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/apicoplast_membrane.yaml
  locator: Entire current maintained record at e721920f30c72a6c35cecb9913c6780e18a460ed
  summary: Full identity, history, components, necessity, taxonomy, functions, evidence,
    graph and discussions inspected. No attached image exists in this record.
  accessed_at: '2026-11-03T09:40:10.095108Z'
  snapshot_sha256: fb3e343e0ed2a8711dff2305abea2166c589cb0a7b169d291c67fed81990ca58
  support: supports
- evidence_id: septin-original-apicoplast_membrane
  kind: prior_review
  reference: reviews/structured/20261021T110736Z-apicoplast-membrane-audit/review.yaml
  locator: Entire original YAML and paired deterministic Markdown
  summary: Original findings, curation requests, verdict, evidence scopes, frozen
    input and check disclosures inspected without changing the original artifact.
  accessed_at: '2026-11-03T09:40:10.095108Z'
  snapshot_sha256: 327d4a503051b00002667d41e48c0fea69c8f330e639efe0880099fa13c6d5c4
  support: supports
- evidence_id: septin-original-validation-apicoplast_membrane
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/adversary-septin/original-checks.json
  locator: 20261021T110736Z-apicoplast-membrane-audit validate and render --content;
    original/source/current target hashes
  summary: Native validation and render exit 0; rendered Markdown byte-identical.
    Current record equals original frozen target hash, which also matches the original
    source revision. Schema validity does not certify scientific claims.
  accessed_at: '2026-11-03T09:36:24.619016Z'
  snapshot_sha256: 3a278d9c91f9f63337a1bdb72781586ef8d5b589dcd7531fe789eb902691c33b
  support: supports
- evidence_id: septin-native-apicoplast_membrane-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/apicoplast_membrane-uniprot-verify-receipt.json
  locator: Exact root-run command, timestamps, source head and stdout hash; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/apicoplast_membrane-uniprot-verify.log
  summary: Command exited 0 at 2026-11-03T09:32:44.174280+00:00. No protein_examples
    are declared; three graph UniProt xrefs resolve. Causal audit reports exactly
    two UNANCHORED_WITH_UNIPROT nodes and zero covered component_ref nodes. It does
    not validate the Der1 paralog localization.
  accessed_at: '2026-11-03T09:32:44.174280Z'
  snapshot_sha256: 23333e8c5be057c8cfe1d6f3a34a47fb52d50bcf77987feb4ca4f4fd2a1c35e6
  support: supports
- evidence_id: septin-native-apicoplast_membrane-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/apicoplast_membrane-uniprot-causal-receipt.json
  locator: Exact root-run command, timestamps, source head and stdout hash; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/apicoplast_membrane-uniprot-causal.log
  summary: Command exited 0 at 2026-11-03T09:32:44.594381+00:00. No protein_examples
    are declared; three graph UniProt xrefs resolve. Causal audit reports exactly
    two UNANCHORED_WITH_UNIPROT nodes and zero covered component_ref nodes. It does
    not validate the Der1 paralog localization.
  accessed_at: '2026-11-03T09:32:44.594381Z'
  snapshot_sha256: b482716ac656c5ccdc5c9f56b83394bd8673c72c7b4ed271a1078248a76cbe88
  support: supports
- evidence_id: septin-record-chloroplast
  kind: record_content
  reference: data/structures/membrane_organelle/chloroplast.yaml
  locator: Entire current maintained record at e721920f30c72a6c35cecb9913c6780e18a460ed
  summary: Full identity, history, components, necessity, taxonomy, functions, evidence,
    graph and discussions inspected. No attached image exists in this record.
  accessed_at: '2026-11-03T09:40:10.095108Z'
  snapshot_sha256: 4c13f5dadaeb23a88fabfc2b5ec65034ed0ac83cbca9d45143793618acf2e727
  support: supports
- evidence_id: septin-original-chloroplast
  kind: prior_review
  reference: reviews/structured/20261021T110755Z-chloroplast-audit/review.yaml
  locator: Entire original YAML and paired deterministic Markdown
  summary: Original findings, curation requests, verdict, evidence scopes, frozen
    input and check disclosures inspected without changing the original artifact.
  accessed_at: '2026-11-03T09:40:10.095108Z'
  snapshot_sha256: f3c3ddbd2da9a91bb230a8acf49262a9a1d045b1902b91552b7edec02f1ac0b7
  support: supports
- evidence_id: septin-original-validation-chloroplast
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/adversary-septin/original-checks.json
  locator: 20261021T110755Z-chloroplast-audit validate and render --content; original/source/current
    target hashes
  summary: Native validation and render exit 0; rendered Markdown byte-identical.
    Current record equals original frozen target hash, which also matches the original
    source revision. Schema validity does not certify scientific claims.
  accessed_at: '2026-11-03T09:36:25.948177Z'
  snapshot_sha256: 3a278d9c91f9f63337a1bdb72781586ef8d5b589dcd7531fe789eb902691c33b
  support: supports
- evidence_id: septin-native-chloroplast-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/chloroplast-uniprot-verify-receipt.json
  locator: Exact root-run command, timestamps, source head and stdout hash; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/chloroplast-uniprot-verify.log
  summary: Command exited 0 at 2026-11-03T09:32:50.019609+00:00. No protein_examples,
    UniProt protein xrefs or GENE_OR_PROTEIN graph nodes are declared. The causal
    inventory is empty (zero typed protein nodes); success does not validate molecular
    prose or TOC/TIC composition.
  accessed_at: '2026-11-03T09:32:50.019609Z'
  snapshot_sha256: 29fd68e33afe3d9479a891e453e781b5c3d0d9f06b8f88d051c1b6c5b8c07401
  support: supports
- evidence_id: septin-native-chloroplast-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/chloroplast-uniprot-causal-receipt.json
  locator: Exact root-run command, timestamps, source head and stdout hash; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/chloroplast-uniprot-causal.log
  summary: Command exited 0 at 2026-11-03T09:32:50.458099+00:00. No protein_examples,
    UniProt protein xrefs or GENE_OR_PROTEIN graph nodes are declared. The causal
    inventory is empty (zero typed protein nodes); success does not validate molecular
    prose or TOC/TIC composition.
  accessed_at: '2026-11-03T09:32:50.458099Z'
  snapshot_sha256: 040cb233c721586e2b2fa543362cc74b3cf583947de17ff11146a698f8dd7d5a
  support: supports
- evidence_id: septin-record-chloroplast_envelope
  kind: record_content
  reference: data/structures/membrane_organelle/chloroplast_envelope.yaml
  locator: Entire current maintained record at e721920f30c72a6c35cecb9913c6780e18a460ed
  summary: Full identity, history, components, necessity, taxonomy, functions, evidence,
    graph and discussions inspected. No attached image exists in this record.
  accessed_at: '2026-11-03T09:40:10.095108Z'
  snapshot_sha256: 29da363489107536342db1782001be534ea54605039b80c201cba0a46de9468e
  support: supports
- evidence_id: septin-original-chloroplast_envelope
  kind: prior_review
  reference: reviews/structured/20261021T110757Z-chloroplast-envelope-audit/review.yaml
  locator: Entire original YAML and paired deterministic Markdown
  summary: Original findings, curation requests, verdict, evidence scopes, frozen
    input and check disclosures inspected without changing the original artifact.
  accessed_at: '2026-11-03T09:40:10.095108Z'
  snapshot_sha256: 2be9beedd1b70a7c4947df25bebb9141cbe4997eed76a41a94db1bdb5da0b9fc
  support: supports
- evidence_id: septin-original-validation-chloroplast_envelope
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/adversary-septin/original-checks.json
  locator: 20261021T110757Z-chloroplast-envelope-audit validate and render --content;
    original/source/current target hashes
  summary: Native validation and render exit 0; rendered Markdown byte-identical.
    Current record equals original frozen target hash, which also matches the original
    source revision. Schema validity does not certify scientific claims.
  accessed_at: '2026-11-03T09:36:27.278139Z'
  snapshot_sha256: 3a278d9c91f9f63337a1bdb72781586ef8d5b589dcd7531fe789eb902691c33b
  support: supports
- evidence_id: septin-native-chloroplast_envelope-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/chloroplast_envelope-uniprot-verify-receipt.json
  locator: Exact root-run command, timestamps, source head and stdout hash; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/chloroplast_envelope-uniprot-verify.log
  summary: Command exited 0 at 2026-11-03T09:32:50.909232+00:00. No protein_examples,
    UniProt protein xrefs or GENE_OR_PROTEIN graph nodes are declared. The causal
    inventory is empty (zero typed protein nodes); success does not validate molecular
    prose or TOC/TIC composition.
  accessed_at: '2026-11-03T09:32:50.909232Z'
  snapshot_sha256: 845b6611a6ae8d17100cbce9b1e35efbaa3f2a3d00893f0bc45d2dde8e223fc2
  support: supports
- evidence_id: septin-native-chloroplast_envelope-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/chloroplast_envelope-uniprot-causal-receipt.json
  locator: Exact root-run command, timestamps, source head and stdout hash; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/chloroplast_envelope-uniprot-causal.log
  summary: Command exited 0 at 2026-11-03T09:32:51.346119+00:00. No protein_examples,
    UniProt protein xrefs or GENE_OR_PROTEIN graph nodes are declared. The causal
    inventory is empty (zero typed protein nodes); success does not validate molecular
    prose or TOC/TIC composition.
  accessed_at: '2026-11-03T09:32:51.346119Z'
  snapshot_sha256: 0d096514ea497b5505c80be7dfc7f67d45123e66374f294bd5d1c0dda0cff51c
  support: supports
- evidence_id: septin-context-apicoplast
  kind: record_content
  reference: data/structures/membrane_organelle/apicoplast.yaml
  locator: Identity, membrane has_part and shared SELMA component only
  summary: Whole-organelle boundary and shared B9PY98 context inspected. This is a
    distinct maintained target; no prior whole-organelle finding is closed or transferred
    wholesale.
  accessed_at: '2026-11-03T09:40:10.095108Z'
  snapshot_sha256: 00971d8425f63fc5d490907a43c00b6760c2d88c5413fce6bdbc2dd09919410e
  support: supports
- evidence_id: septin-context-chloroplast_inner_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/chloroplast_inner_membrane.yaml
  locator: Identity, definition, parent_structures and part_of only
  summary: Frozen neighbor distinguishes the stroma-facing inner bilayer from the
    complete envelope and its intermembrane space.
  accessed_at: '2026-11-03T09:40:10.095108Z'
  snapshot_sha256: 05283f5252a6354d26bef1ff196b3a9e10fbd6e72e9a6ec17014330f7a28dbb3
  support: supports
- evidence_id: septin-context-chloroplast_intermembrane_space
  kind: record_content
  reference: data/structures/membrane_organelle/chloroplast_intermembrane_space.yaml
  locator: Identity, definition, parent_structures and part_of only
  summary: Frozen neighbor denotes the region between bilayers, not either bilayer
    or the stroma.
  accessed_at: '2026-11-03T09:40:10.095108Z'
  snapshot_sha256: 7ab90f4d2f4c41c466e100d589fb1f1d42bf90ded515dea6db5575d54119d43a
  support: supports
- evidence_id: septin-apicoplast-membrane-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0160211,GO:0016020,GO:0020011
  locator: Exact QuickGO records GO:0160211, GO:0016020 and GO:0020011; definitions
    and typed child relations
  summary: Exact apicoplast-membrane identity and broad membrane parent are distinct
    from the whole apicoplast; GO:0020011 explicitly has apicoplast membrane as part.
  accessed_at: '2026-11-03T09:33:10.010723Z'
  snapshot_sha256: b8bf19850eeb9acf37d2a2184e92e65b4ddd0bdddf25d071cade34f89c966748
  support: supports
- evidence_id: septin-root21-sources-chloroplast-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009507,GO:0009534,GO:0009535,GO:0009536,GO:0009570,GO:0009706,GO:0009707,GO:0009941,GO:0010006,GO:0015979,GO:0031897,GO:0045037,GO:0061927
  locator: Complete thirteen requested GO term records; names, definitions, obsolete
    flags and typed child relations
  summary: Supports exact chloroplast/plastid identity, envelope/stroma/thylakoid
    topology, Toc/Tic and photosynthesis/import process identities; preserves part_of
    versus is_a relations.
  accessed_at: '2026-11-03T09:33:10.011107Z'
  snapshot_sha256: d3e445f547c0b77756cd784b474abddbcef716d647264ff4e3ffcad643ff4ed8
  support: supports
- evidence_id: septin-root21-sources-envelope-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009507,GO:0009526,GO:0009570,GO:0009706,GO:0009707,GO:0009941,GO:0010006,GO:0031897,GO:0031972,GO:0045037
  locator: Complete ten requested GO term records; definitions and typed child relations
  summary: Envelope includes both bilayers and intermembrane space; plastid envelope
    is its parent, chloroplast its whole. Toc and Tic have exact outer/inner-envelope
    translocon identities.
  accessed_at: '2026-11-03T09:33:11.800585Z'
  snapshot_sha256: 260213873d2fb05f3956a9c1255b23363d75aa5dba6a8c110f39cc2d8ca8f624
  support: supports
- evidence_id: septin-root21-sources-GO0061927
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0061927
  locator: GO:0061927 complete exact term definition
  summary: TOC-TIC supercomplex I explicitly includes Toc75, Toc159, Toc34 and Tic110;
    it is not automatically exact for the divergent Jin Chlamydomonas assembly.
  accessed_at: '2026-11-03T09:33:11.665050Z'
  snapshot_sha256: c396141ec6b3ee096330ffd7050a629e09efdbb06839c03e0ea67a546cf389d2
  support: supports
- evidence_id: septin-root21-sources-ancestors-0009507
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009507/ancestors?relations=is_a,part_of
  locator: Complete requested ancestor closure with relations=is_a,part_of
  summary: Ancestor closure is contextual support only; direct typed relations and
    definitions are separately inspected so is-a and parthood are not conflated.
  accessed_at: '2026-11-03T09:33:10.011232Z'
  snapshot_sha256: cbdf5fc49c2b7c9425aece03659961b04336046658ec04870b356ee0ef3a97cf
  support: supports
- evidence_id: septin-root21-sources-ancestors-0009941
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009941/ancestors?relations=is_a,part_of
  locator: Complete requested ancestor closure with relations=is_a,part_of
  summary: Ancestor closure is contextual support only; direct typed relations and
    definitions are separately inspected so is-a and parthood are not conflated.
  accessed_at: '2026-11-03T09:33:12.086897Z'
  snapshot_sha256: c66d5423aab8006aeeabf213bca3cabd1193b860a59550b35b397b9ac1b2dc30
  support: supports
- evidence_id: septin-root21-sources-NCBITaxon-33090
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/33090
  locator: Exact ENA taxonomy identity/rank/lineage and aliases
  summary: Taxon 33090 resolves to Viridiplantae; the native lineage is Eukaryota;
    . Metadata supports identity, not universal presence.
  accessed_at: '2026-11-03T09:33:10.011310Z'
  snapshot_sha256: b1394e36c6896d7ec64cdb301a239f2bc49bc435a22cc21fdba8fdc6217e2d11
  support: supports
- evidence_id: septin-root21-sources-NCBITaxon-3055
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3055
  locator: Exact ENA taxonomy identity/rank/lineage and aliases
  summary: Taxon 3055 resolves to Chlamydomonas reinhardtii; the native lineage is
    Eukaryota; Viridiplantae; Chlorophyta; core chlorophytes; Chlorophyceae; CS clade;
    Chlamydomonadales; Chlamydomonadaceae; Chlamydomonas; . Metadata supports identity,
    not universal presence.
  accessed_at: '2026-11-03T09:33:10.011369Z'
  snapshot_sha256: a24c8f85014097148d9e865ea324b01b8d04f6bae27e893834f8abb5bd8b6a1f
  support: supports
- evidence_id: septin-root21-sources-doi-10.1098_rstb.2009.0103
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1098/rstb.2009.0103
  locator: 'Europe PMC exact DOI core result: complete abstract, title, authors, journal,
    date and identifier fields'
  summary: Keeling 2010 is a secondary review; complete indexed abstract and bibliographic
    metadata support primary-plastid evolutionary context, with lineage/loss caveats.
  accessed_at: '2026-11-03T09:33:10.767625Z'
  snapshot_sha256: 63c6291480d57ca01d4eb770792f919c0e3128eeaae04894f1ed2f2f3fc0e886
  search_scope: Europe PMC search API; query DOI:10.1098/rstb.2009.0103; resultType=core,
    format=json, default one response page; inspected exact returned bibliographic
    match and full abstract at 2026-11-03T09:33:10.767625Z; no publication-date filter
    and no broader literature-absence claim.
  support: supports
- evidence_id: septin-root21-sources-doi-10.1016_j.cell.2022.10.030
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.cell.2022.10.030
  locator: 'Europe PMC exact DOI core result: complete abstract, title, authors, journal,
    date and identifier fields'
  summary: 'Jin et al. 2022 primary study complete indexed abstract: Chlamydomonas
    14-component complex spans both envelope membranes; Toc120/Toc75 hybrid barrel
    and a potential Tic20/YlmG path are connected across the intermembrane space.
    Abstract-level access is not a full Results or raw cryo-EM audit.'
  accessed_at: '2026-11-03T09:33:10.803490Z'
  snapshot_sha256: f4fc2108c3825f4a38c42eb7d109ac334b6e4d413ff1216d0d013925a2780061
  search_scope: Europe PMC search API; query DOI:10.1016/j.cell.2022.10.030; resultType=core,
    format=json, default one response page; inspected exact returned bibliographic
    match and full abstract at 2026-11-03T09:33:10.803490Z; no publication-date filter
    and no broader literature-absence claim.
  support: supports
- evidence_id: septin-root21-sources-doi-10.1007_s00294-011-0339-1
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1007/s00294-011-0339-1
  locator: 'Europe PMC exact DOI core result: complete abstract, title, authors, journal,
    date and identifier fields'
  summary: 'Terashima, Specht and Hippler 2011 secondary proteome review, complete
    indexed abstract and metadata: experimentally localized chloroplast protein set,
    comparative photosynthetic/metabolic context and Chlamydomonas/plant comparison.
    No fresh full PDF read is claimed.'
  accessed_at: '2026-11-03T09:33:11.481915Z'
  snapshot_sha256: 703d897a8f74ddaa0e9e3866f4901c10269106f75ad66a847846cdcfd96883b0
  search_scope: Europe PMC search API; query DOI:10.1007/s00294-011-0339-1; resultType=core,
    format=json, default one response page; inspected exact returned bibliographic
    match and full abstract at 2026-11-03T09:33:11.481915Z; no publication-date filter
    and no broader literature-absence claim.
  support: supports
- evidence_id: septin-root21-sources-keeling2010-pmc
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2817223/
  locator: 'Genuine PMC secondary-review HTML: Abstract and section 1 origin/primary
    plastids, including two bounding membranes and green-algal/plant context; no image
    pixels'
  summary: Fresh body access confirms cyanobacterial primary-plastid origin and two-membrane
    topology in the explicitly discussed lineages. Historical broader evolutionary
    hypotheses elsewhere in this review are not recast as current experimental proof.
  accessed_at: '2026-11-03T09:33:10.806914Z'
  snapshot_sha256: 9b8d3133fe3b680c1f21e7bafc458416e28de352e38d165f186f79a288bd829c
  support: supports
- evidence_id: septin-root21-sources-jin2022-author-publications
  kind: primary_source
  reference: https://lifesciences.westlake.edu.cn/labs/zhen-yan/structural-biology-laboratory/publications/
  locator: 'Author laboratory publication-list entry for Jin et al. 2022: title, author
    list, journal/DOI and complete study abstract only'
  summary: The author-hosted abstract corroborates the exact assembly, Chlamydomonas
    scope and potential inner-channel wording. This is neither a complete paper nor
    independent raw structural reanalysis.
  accessed_at: '2026-11-03T09:33:11.441964Z'
  snapshot_sha256: f634a6d488c6de60b0889cb28bb8d87e171e26c10293ad64223333d32bc18b03
  support: supports
- evidence_id: septin-root21-sources-terashima2011-pdf
  kind: validation
  reference: https://link.springer.com/content/pdf/10.1007/s00294-011-0339-1.pdf
  locator: 'HTTP 200 response body inspected: 3,038-byte HTML challenge, not PDF'
  summary: Publisher PDF route returned HTML rather than scientific content; the current
    review uses the complete native indexed abstract instead of claiming a successful
    full-body read.
  accessed_at: '2026-11-03T09:33:11.567479Z'
  snapshot_sha256: 32ed63159c77e21ee19ca1b9aa3213ccf0218eb59539560b132a8e68ef0e18ea
  support: supports
- evidence_id: septin-current-source-access-receipts
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/adversary-septin/source-receipts.json
  locator: Actual fresh requests, timestamps, HTTP status/content-type/hash; includes
    failed routes
  summary: Jin publisher returned HTTP 403; Terashima nominal PDF returned challenge
    HTML. Keeling PMC body succeeded, though alternate API routes failed. These outcomes
    limit access claims and are not biological findings.
  accessed_at: '2026-11-03T09:40:10.095108Z'
  snapshot_sha256: 36a3b761bf9121251df41ae90faafa922d13bee4dee56a3a318179ed92432c02
  support: supports
- evidence_id: septin-current-adapter-catalogue
  kind: search
  reference: https://imodulondb.org/api/datasets
  locator: Complete official datasets response; every organism name/id and dataset
    list inspected
  summary: Twenty listed organisms comprise 28 organism/dataset pairs and 22 distinct
    dataset-key strings. No listed organism matches Apicomplexa, Toxoplasma gondii,
    Plasmodium falciparum or their represented strains, Viridiplantae, or Chlamydomonas
    reinhardtii. Thus no target-matched downstream gene/module lookup applies. This
    is a database-coverage statement, not biological absence.
  accessed_at: '2026-11-03T09:33:12.275564Z'
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  search_scope: iModulonDB official GET /api/datasets; complete 20-organism JSON response
    fetched 2026-11-03T09:33:12.275564Z; inspected all names, IDs and dataset lists
    for Apicomplexa/Toxoplasma/Plasmodium and Viridiplantae/Chlamydomonas, including
    current example strain taxa 508771 and 36329. No date filter; no gene/module query
    in an unrelated organism; no inferred absence outside this catalogue.
  support: supports
- evidence_id: septin-historical-adapter-runner-unavailable
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical canary invocation at 2026-11-03T00:49:00.848907Z–00:49:00.863225Z
  summary: Actual historical datasets runner exited 1 with PermissionError reading
    pyvenv.cfg. Receipt is reused; no fresh invocation is claimed. Current official-source
    fallback is separately fetched.
  accessed_at: '2026-11-03T00:49:00.863225Z'
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  support: supports
- evidence_id: septin-apicoplast-agent-tax-5794
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5794
  locator: 'ENA taxonomy exact tax-id response: current name, aliases, rank and lineage'
  summary: Reused public-source snapshot, originally fetched at 2026-11-03T08:55:13.959999Z;
    no fresh network retrieval claimed. Native taxon 5794 is Apicomplexa; inspected
    name, rank, aliases and lineage. This establishes identity and strain/species
    context, not universal organelle presence.
  accessed_at: '2026-11-03T08:55:13.959999Z'
  snapshot_sha256: 617b42c27ae95a801b69abf63e1a545eff8565fd0af2f4a81be359d3fb6b3cbf
  support: supports
- evidence_id: septin-apicoplast-agent-tax-5811
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5811
  locator: 'ENA taxonomy exact tax-id response: current name, aliases, rank and lineage'
  summary: Reused public-source snapshot, originally fetched at 2026-11-03T08:55:14.075206Z;
    no fresh network retrieval claimed. Native taxon 5811 is Toxoplasma gondii; inspected
    name, rank, aliases and lineage. This establishes identity and strain/species
    context, not universal organelle presence.
  accessed_at: '2026-11-03T08:55:14.075206Z'
  snapshot_sha256: cbb209002c87051ce78d0a34bc169d2f6623f6bbfbb21edad170d43eb16d4032
  support: supports
- evidence_id: septin-apicoplast-agent-tax-5833
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5833
  locator: 'ENA taxonomy exact tax-id response: current name, aliases, rank and lineage'
  summary: Reused public-source snapshot, originally fetched at 2026-11-03T08:55:14.170990Z;
    no fresh network retrieval claimed. Native taxon 5833 is Plasmodium falciparum;
    inspected name, rank, aliases and lineage. This establishes identity and strain/species
    context, not universal organelle presence.
  accessed_at: '2026-11-03T08:55:14.170990Z'
  snapshot_sha256: 47c9da135299ea0515b9cbddde80166e0e7256bcf1daac4cdf87f8ae3e0ecd11
  support: supports
- evidence_id: septin-apicoplast-agent-tax-508771
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/508771
  locator: 'ENA taxonomy exact tax-id response: current name, aliases, rank and lineage'
  summary: Reused public-source snapshot, originally fetched at 2026-11-03T08:55:14.482604Z;
    no fresh network retrieval claimed. Native taxon 508771 is Toxoplasma gondii ME49;
    inspected name, rank, aliases and lineage. This establishes identity and strain/species
    context, not universal organelle presence.
  accessed_at: '2026-11-03T08:55:14.482604Z'
  snapshot_sha256: d1622dee69e1fe2abfea4351893585852f4200cfff6eac3b42e5a014283cd0b0
  support: supports
- evidence_id: septin-apicoplast-agent-tax-36329
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/36329
  locator: 'ENA taxonomy exact tax-id response: current name, aliases, rank and lineage'
  summary: Reused public-source snapshot, originally fetched at 2026-11-03T08:55:14.671962Z;
    no fresh network retrieval claimed. Native taxon 36329 is Plasmodium falciparum
    3D7; inspected name, rank, aliases and lineage. This establishes identity and
    strain/species context, not universal organelle presence.
  accessed_at: '2026-11-03T08:55:14.671962Z'
  snapshot_sha256: 6d1389e6a3af3a09ef4bf23157b95ec8d94dac9b395b8f8ccf0d1952beddc306
  support: supports
- evidence_id: septin-apicoplast-agent-S8GBF3
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/S8GBF3.json
  locator: Native accession, entry status, organism/taxon, gene/ORF names, protein
    name, sequence and cross-reference fields
  summary: 'Reused public-source snapshot, originally fetched at 2026-11-03T08:55:14.763108Z;
    no fresh network retrieval claimed. S8GBF3: UniProtKB unreviewed (TrEMBL); taxon
    508771; native gene/ORF values TIC20, TGME49_255370. Identity/status metadata
    does not alone establish organelle membership.'
  accessed_at: '2026-11-03T08:55:14.763108Z'
  snapshot_sha256: 6f8ee8170f0800a4b6cc9e8c5cea4930f69f83c3d0d4392d8cfc6c3eee95ebd4
  support: supports
- evidence_id: septin-apicoplast-agent-O97275
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/O97275.json
  locator: Native accession, entry status, organism/taxon, gene/ORF names, protein
    name, sequence and cross-reference fields
  summary: 'Reused public-source snapshot, originally fetched at 2026-11-03T08:55:14.979966Z;
    no fresh network retrieval claimed. O97275: UniProtKB unreviewed (TrEMBL); taxon
    36329; native gene/ORF values PF3D7_0314300. Identity/status metadata does not
    alone establish organelle membership.'
  accessed_at: '2026-11-03T08:55:14.979966Z'
  snapshot_sha256: aa2a0c336bb23dcf2519f28ca86594f604bde1109843da9c2009d44459e0d241
  support: supports
- evidence_id: septin-apicoplast-agent-B9PY98
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/B9PY98.json
  locator: Native accession, entry status, organism/taxon, gene/ORF names, protein
    name, sequence and cross-reference fields
  summary: 'Reused public-source snapshot, originally fetched at 2026-11-03T08:55:15.188599Z;
    no fresh network retrieval claimed. B9PY98: UniProtKB unreviewed (TrEMBL); taxon
    5811; native gene/ORF values no native gene-name field. Identity/status metadata
    does not alone establish organelle membership. EMBL cross-reference is FJ976521/ACU32856.1,
    independently deposited as Der1ER1.'
  accessed_at: '2026-11-03T08:55:15.188599Z'
  snapshot_sha256: 5e769e2158976bdd00e8f8faedecee43ff930efff08515488ea2e999900edb70
  support: supports
- evidence_id: septin-apicoplast-agent-C9WWW6
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/C9WWW6.json
  locator: Native accession, entry status, organism/taxon, gene/ORF names, protein
    name, sequence and cross-reference fields
  summary: 'Reused public-source snapshot, originally fetched at 2026-11-03T08:55:16.014524Z;
    no fresh network retrieval claimed. C9WWW6: UniProtKB unreviewed (TrEMBL); taxon
    5811; native gene/ORF values no native gene-name field. Identity/status metadata
    does not alone establish organelle membership. EMBL cross-reference is FJ976520/ACU32855.1,
    independently deposited as apicoplast Der1; automated ER wording is not accepted
    as a replacement for primary localization.'
  accessed_at: '2026-11-03T08:55:16.014524Z'
  snapshot_sha256: 322c5fb4f1e71820ed84f3e03f57edeb35c06f1e671641702a129d00c727cf0e
  support: supports
- evidence_id: septin-apicoplast-agent-matches-S8GBF3
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/S8GBF3/?page_size=200
  locator: Complete example-specific native InterPro matches response; accession/type/match
    positions and pagination inspected
  summary: 'Reused public-source snapshot, originally fetched at 2026-11-03T08:55:18.399340Z;
    no fresh network retrieval claimed. Native example matches: IPR005691:family.
    Protein family, domain and homologous-superfamily types remain distinct; generated
    biological descriptions are not used.'
  accessed_at: '2026-11-03T08:55:18.399340Z'
  snapshot_sha256: 43cd8b9d7fde94abf9038d7fc9785aae46b79d52245b9672587e64cac9020ceb
  support: supports
- evidence_id: septin-apicoplast-agent-matches-O97275
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/O97275/?page_size=200
  locator: Complete example-specific native InterPro matches response; accession/type/match
    positions and pagination inspected
  summary: 'Reused public-source snapshot, originally fetched at 2026-11-03T08:55:19.035669Z;
    no fresh network retrieval claimed. Native example matches: IPR007599:family,
    IPR035952:homologous_superfamily. Protein family, domain and homologous-superfamily
    types remain distinct; generated biological descriptions are not used.'
  accessed_at: '2026-11-03T08:55:19.035669Z'
  snapshot_sha256: 751500a2527a56fd64a534a58d8cb850d8fbe6010609087cf75b459243cc1eaa
  support: supports
- evidence_id: septin-apicoplast-agent-matches-B9PY98
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/B9PY98/?page_size=200
  locator: Complete example-specific native InterPro matches response; accession/type/match
    positions and pagination inspected
  summary: 'Reused public-source snapshot, originally fetched at 2026-11-03T08:55:19.293895Z;
    no fresh network retrieval claimed. Native example matches: IPR007599:family,
    IPR035952:homologous_superfamily. Protein family, domain and homologous-superfamily
    types remain distinct; generated biological descriptions are not used.'
  accessed_at: '2026-11-03T08:55:19.293895Z'
  snapshot_sha256: e3f9e802aee474bbb0bddc4c7e9fb7007c014b7ee37fe22382c8deca667ae831
  support: supports
- evidence_id: septin-apicoplast-agent-jats-PMC3681736
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3681736.1/PMC3681736.1.xml
  locator: 'Agrawal et al. 2013 JATS: Abstract, apicoplast enzyme localization/import
    experiments, Discussion including unresolved endogenous modifier paragraphs'
  summary: Reused public-source snapshot, originally fetched at 2026-11-03T08:55:23.487064Z;
    no fresh network retrieval claimed. Supports an apicoplast ubiquitylation-system
    import role and tested enzyme activity, while explicitly leaving endogenous ubiquitin
    versus ubiquitin-like modifier unresolved. Recombinant human ubiquitin is the
    tested in-vitro substrate.
  accessed_at: '2026-11-03T08:55:23.487064Z'
  snapshot_sha256: 8e546449838569e9d2d6a7d89bffc348f344d421df0c04c833ca170916a26897
  support: supports
- evidence_id: septin-apicoplast-agent-jats-PMC3662607
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3662607.1/PMC3662607.1.xml
  locator: 'Lemgruber et al. 2013 JATS: Abstract, Results four-membrane reconstructions,
    figure captions and Conclusions; no new pixel audit'
  summary: Reused public-source snapshot, originally fetched at 2026-11-03T08:55:23.544521Z;
    no fresh network retrieval claimed. Cryo-electron tomography of P. falciparum
    merozoites resolves four envelope membranes; local apposition explains slices
    apparently showing three. Supports the scoped membrane-boundary claim, not protein
    identities.
  accessed_at: '2026-11-03T08:55:23.544521Z'
  snapshot_sha256: 6a8d19405baff6d46f39c9c039da72718883c8b15c1850da7249c229af07f642
  support: supports
- evidence_id: septin-apicoplast-agent-jats-PMC2817234
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2817234.1/PMC2817234.1.xml
  locator: 'Lim and McFadden 2010 secondary review JATS: origin/envelope, targeting
    and metabolic pathway sections'
  summary: Reused public-source snapshot, originally fetched at 2026-11-03T08:55:23.770969Z;
    no fresh network retrieval claimed. Secondary review body supports four-membrane
    envelope and bipartite signal/transit targeting context. It is not a new primary
    localization or assembly experiment.
  accessed_at: '2026-11-03T08:55:23.770969Z'
  snapshot_sha256: 600962f47c1fa8ce333826e38b6df45e8fd8e4c252cabbb68c723d849fbe0352
  support: supports
- evidence_id: septin-apicoplast-agent-jats-PMC5406208
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5406208.1/PMC5406208.1.xml
  locator: 'McFadden and Yeh 2017 secondary review JATS: apicoplast loss and stage-specific
    metabolic function sections'
  summary: Reused public-source snapshot, originally fetched at 2026-11-03T08:55:23.938665Z;
    no fresh network retrieval claimed. Secondary context supports variable apicomplexan
    presence including Cryptosporidium loss and life-stage distinctions. No universal
    family or life-stage metabolic requirement is inferred.
  accessed_at: '2026-11-03T08:55:23.938665Z'
  snapshot_sha256: 3bd5749b77dc8ad8c1f12559b31e1c8f18780cd68b53430e021e1191ac3457b3
  support: supports
- evidence_id: septin-apicoplast-agent-ena-FJ976521
  kind: database
  reference: https://www.ebi.ac.uk/ena/browser/api/embl/FJ976521?download=false
  locator: ENA native flatfile DE/CDS product/protein_id and translation
  summary: Reused public-source snapshot, originally fetched at 2026-11-03T08:55:24.022634Z;
    no fresh network retrieval claimed. FJ976521 explicitly names Der1ER1 and ACU32856.1;
    exact accession bridge to unreviewed B9PY98, the ER paralog.
  accessed_at: '2026-11-03T08:55:24.022634Z'
  snapshot_sha256: c828fa0bcfedada7e3f1681cf850c2171324afdb4832e582f84733fd96c20831
  support: supports
- evidence_id: septin-apicoplast-agent-ena-FJ976520
  kind: database
  reference: https://www.ebi.ac.uk/ena/browser/api/embl/FJ976520?download=false
  locator: ENA native flatfile DE/CDS product/note/protein_id and translation
  summary: Reused public-source snapshot, originally fetched at 2026-11-03T08:55:24.218558Z;
    no fresh network retrieval claimed. FJ976520 explicitly names apicoplast Der1/Der1Ap
    and ACU32855.1; exact accession bridge to unreviewed C9WWW6. Automated generic
    ER location in that UniProt entry is not substituted for the primary paralog evidence.
  accessed_at: '2026-11-03T08:55:24.218558Z'
  snapshot_sha256: 47671e2466a074e673610363f3c8e7d8429c5063b2dbba1cf947b0212e32bfd2
  support: supports
- evidence_id: septin-apicoplast-agent-ena-CAB38986
  kind: database
  reference: https://www.ebi.ac.uk/ena/browser/api/embl/CAB38986.4?download=false
  locator: Native sequence/locus metadata; exact gene and old-locus bridge only
  summary: Reused public-source snapshot, originally fetched at 2026-11-03T08:55:24.473949Z;
    no fresh network retrieval claimed. Supports current O97275/CAB38986.4/PF3D7_0314300
    and older PFC0590c identity bridge; the old identifier string and new locus name
    are not treated as identical literal strings.
  accessed_at: '2026-11-03T08:55:24.473949Z'
  snapshot_sha256: a30a4b80383caa9e201851e7e8e9ed3edc23a763419f786e1df7926037f532ef
  support: supports
- evidence_id: septin-apicoplast-agent-gene-814456
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=gene&id=814456&retmode=json
  locator: Native sequence/locus metadata; exact gene and old-locus bridge only
  summary: Reused public-source snapshot, originally fetched at 2026-11-03T08:55:24.497062Z;
    no fresh network retrieval claimed. Supports current O97275/CAB38986.4/PF3D7_0314300
    and older PFC0590c identity bridge; the old identifier string and new locus name
    are not treated as identical literal strings.
  accessed_at: '2026-11-03T08:55:24.497062Z'
  snapshot_sha256: 95978f67da120777d7cd6b2f19bab33265c5ed897b6a435c3981275833603ed7
  support: supports
- evidence_id: septin-apicoplast-agent-kalanon2009-pdf
  kind: primary_source
  reference: https://fad.webmate.me/McFadden_Lab/Mcfadden_Papers/2009/Kalanon_Euk_Cell_2009.pdf
  locator: 'Author-hosted Kalanon et al. 2009 PDF: Methods antibody peptide printed
    p.1148; PfsDer1 paralog Results/Table1/Fig.4 caption printed pp.1149–1152'
  summary: Reused public-source snapshot, originally fetched at 2026-11-03T08:55:24.648334Z;
    no fresh network retrieval claimed. Separates PfsDer1-1 from PfsDer1-2/PFC0590c.
    Published anti-Der1-2 peptide IKDCVSKYTSRSSTNN occurs at residues303–318 of current
    O97275. Full-length Der1-1 localization experiments are not transferred to Der1-2.
  accessed_at: '2026-11-03T08:55:24.648334Z'
  snapshot_sha256: b38fbf7d4b2afc6cc5b36f4797f94c46a25f859d093d64b031f656485bc12add
  support: supports
- evidence_id: septin-agrawal2011-thesis
  kind: primary_source
  reference: https://openscholar.uga.edu/record/21126/files/agrawal_swati_201105_phd.pdf
  locator: 'Institutional author dissertation: Chapter 3 Methods printed p.46/PDF59
    and Table3.1 p.81/PDF94; Appendix2 reprinted Tic20 primary study pp.176–188, especially
    pp.187–188/PDF200–201'
  summary: Reused public-source snapshot, originally fetched at 2026-11-03T09:00:17.320297Z;
    no fresh network retrieval claimed. Author-reproduced primary studies distinguish
    ER Der1 FJ976521 from apicoplast Der1 FJ976520. Tic20 depletion leaves 65–77%
    wild-type import at day 2 but essentially completely inhibits import by day 4;
    the study explicitly considers accessory/regulatory alternatives to direct channel
    action. This supports localized import dependency without proving a pore mechanism.
  accessed_at: '2026-11-03T09:00:17.320297Z'
  snapshot_sha256: f0a1550c929a23dbcd8a50bb95a4e4a7042aff6d1acfa0cbbc50d990c2cc6a36
  support: supports
- evidence_id: check-qc
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/qc.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T09:38:13.427387Z'
  support: supports
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  snapshot_sha256: 483e49a58115af930b9d80d1f32c8b8f6fe29f1b519f7f8ae1ff7fe5190f7fc5
- evidence_id: check-labels
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/labels.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T09:33:34.489541Z'
  support: supports
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  snapshot_sha256: 6cdfb05df9a27194f05a5fd7f851783f817ac1523ca0bbfa54fe0e0d18775905
- evidence_id: check-trait-links
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/trait-links.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T09:33:11.471306Z'
  support: supports
  summary: Native TraitMech link check passed.
  snapshot_sha256: 8b336cdefbbd3daf6da8787990efdbe346c95e2c8361d50b7eb68a18f2d5a44a
- evidence_id: check-vendored
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/vendored.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T09:33:12.323999Z'
  support: supports
  summary: Pinned governed files match; native vendored check passed.
  snapshot_sha256: b1f169d103aaefa930745468bcca171e5867b9cc49e4e74311e458097e3252a6
- evidence_id: check-curies
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/curies.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T09:33:38.432825Z'
  support: supports
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  snapshot_sha256: fb3be251020aac118f6df680372ae7aaa32c2a1dd3366648cde95494f19d9dd2
- evidence_id: focused
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/focused-results.json
  locator: All twenty actual target schema/strict command outputs
  accessed_at: '2026-11-03T09:44:45Z'
  support: supports
  summary: Ten schema and ten strict commands returned exit zero.
  snapshot_sha256: ce40899211318ea2a91f752598c234083f9b2f7f9e0a49ab2ea0b66e9f165df2
- evidence_id: supplemental-pmid
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2358/pmid-chunks-receipt.json
  locator: Complete native-report PMID set checked with unchanged resolver in batches
    of at most fifty
  accessed_at: '2026-11-03T09:34:49.179102Z'
  support: supports
  summary: 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers
    remain unverified.
  snapshot_sha256: 2a1db8ffa4a416f4ec8f3824824a205f48fa1ab716ae21bbb706c59c879ff27f
- evidence_id: historical-adapter-runner-availability
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical runner invocation receipt, cross-checked against exact stdout/stderr
    hashes; reread during PR2358 synthesis
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  summary: Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS
    PermissionError reading the configured runner pyvenv.cfg. This is a retained historical
    availability observation, not a fresh attempt or a scientific validation failure.
    Native policy permits inspected source-catalogue fallback.
assessments:
- assessment_id: plaque-t4-identity
  area: identity
  topic: Whole thylakoid identity and part boundaries
  outcome: supported
  target_ids:
  - GO:0030075
  summary: The exact GO identity, synonym, parent and four asserted parts are supported;
    OTHER follows the explicit GO comment that a thylakoid is not an organelle. The
    filesystem category does not redefine its kind. No local sibling record is used
    as scientific evidence.
  evidence_ids:
  - plaque-current-4
  - plaque-thylakoid-agent-go
- assessment_id: plaque-t4-composition
  area: evidence
  topic: Collective bilayer and photosynthetic complex membership
  outcome: supported
  target_ids:
  - GO:0030075
  summary: A membrane boundary is constitutional to this compartment, supporting ESSENTIAL
    at the collective bilayer level. The four known photosynthetic complexes are correctly
    represented by complex identifiers rather than forced single-protein families.
    Native authority and the primary assays establish broad membership; their incorrect
    organism attributions are separately addressed by F1.
  evidence_ids:
  - plaque-current-4
  - plaque-thylakoid-agent-go
  - plaque-thylakoid-agent-jats-PMC5683893
  - plaque-thylakoid-agent-jats-PMC8190092
- assessment_id: plaque-t4-necessity
  area: evidence
  topic: Individual molecular assembly requirements
  outcome: unknown
  target_ids:
  - GO:0030075
  summary: The four complex rows correctly retain UNKNOWN. Membrane residence, photosynthetic
    function, changing abundance and the study of biogenesis do not alone establish
    which complex or individual lipid is necessary to form every bacterial thylakoid.
  evidence_ids:
  - plaque-current-4
  - plaque-policy
  - plaque-thylakoid-agent-jats-PMC5683893
  - plaque-thylakoid-agent-jats-PMC8190092
- assessment_id: plaque-t4-taxon-example
  area: scope
  topic: Taxonomic distribution versus exact experimental model
  outcome: concern
  target_ids:
  - GO:0030075
  summary: Cyanobacterial COMMON presence with a named thylakoid-lacking exception
    is supported. Both source papers study Synechococcus elongatus PCC7942; the target
    transfers this work to Synechocystis PCC6803 and repeats Synechocystis in Casella
    evidence notes (F1). This is a source-organism mismatch, not evidence that Synechocystis
    lacks thylakoids.
  evidence_ids:
  - plaque-current-4
  - plaque-perez-body-introduction
  - plaque-thylakoid-agent-jats-PMC5683893
  - plaque-thylakoid-agent-jats-PMC8190092
  - plaque-thylakoid-agent-tax-1117
  - plaque-thylakoid-agent-tax-1148
  - plaque-thylakoid-agent-tax-1140
- assessment_id: plaque-t4-functions-graph
  area: graph
  topic: Both functions and all ten coarse graph edges
  outcome: supported
  target_ids:
  - GO:0030075
  summary: The membrane/lumen topology and PSII–quinone–b6f–PSI/ATP synthesis roles
    are supported at the declared NONMECHANISTIC scale. The b6f-to-PSI edge explicitly
    allows a downstream soluble carrier. No fixed stoichiometry, exhaustive respiratory
    inventory or direct b6f–PSI physical transfer is asserted. Correct the organism
    scope of the two Casella localization edges with F1.
  evidence_ids:
  - plaque-current-4
  - plaque-graph-policy
  - plaque-thylakoid-agent-go
  - plaque-perez-body-electron-transport
  - plaque-thylakoid-agent-jats-PMC5683893
- assessment_id: plaque-t4-biogenesis-limit
  area: evidence
  topic: Ontology-derived attachment wording versus observed membrane development
  outcome: unknown
  target_ids:
  - GO:0030075
  summary: The target reproduces current GO wording accurately. Huokko distinguishes
    proximity/thylapse-like contacts from direct membrane connection or fusion and
    leaves origin models unresolved. This review does not infer obligatory membrane
    continuity, universal plasma-membrane budding, or validated membrane tethers in
    every cyanobacterium from that wording.
  evidence_ids:
  - plaque-current-4
  - plaque-thylakoid-agent-go
  - plaque-thylakoid-agent-jats-PMC8190092
  - plaque-perez-body-introduction
- assessment_id: plaque-t4-provenance-completeness
  area: completeness
  topic: Evidence identity, discussion scope and bounded inventory
  outcome: supported
  target_ids:
  - GO:0030075
  summary: All cited DOIs resolve to the intended works. The native ontology supports
    the resolved whole-compartment versus membrane and non-organelle decisions. The
    record has no image or protein-example assertions. Additional respiratory complexes,
    lipid species and detailed biogenesis machinery are not mandatory solely because
    the sources describe them. Historical notes remain historical.
  evidence_ids:
  - plaque-current-4
  - plaque-thylakoid-agent-go
  - plaque-thylakoid-agent-perez2024-meta
  - plaque-thylakoid-agent-casella2017-meta
  - plaque-thylakoid-agent-huokko2021-meta
- assessment_id: plaque-t4-native-protein
  area: schema
  topic: Native protein identity and graph coverage
  outcome: supported
  summary: Both actual checks exited0. These records have no protein examples and
    no GENE_OR_PROTEIN causal nodes; complex/structure or spatial nodes are not forced
    into individual protein coverage. Empty inventory does not prove molecular membership
    or assembly necessity.
  target_ids:
  - GO:0030075
  evidence_ids:
  - plaque-current-4
  - plaque-native-bacterial_thylakoid-verify
  - plaque-native-bacterial_thylakoid-causal
- assessment_id: plaque-t4-bundle-provenance
  area: provenance
  topic: Frozen historical input and deterministic bundle validation
  outcome: supported
  summary: Original YAML validates and exact native Markdown render agrees. Historical
    target hash and current hash match; no stale delta requires refresh. New assessments
    correct bundle applicability without rewriting originals or claiming scientific
    record edits.
  target_ids:
  - GO:0030075
  evidence_ids:
  - plaque-current-4
  - plaque-original-4
- assessment_id: plaque-t4-adapter
  area: scope
  topic: Photosynthetic pathways and bounded matched PCC7942 source context
  outcome: supported
  summary: The photosynthetic complexes/pathway trigger applicability. Fresh catalogue/meta
    identify PCC7942 elprecise300, matching the cited experimental context but not
    maintained PCC6803. Bounded searches and representative psaA/psbA1/petB/atpA membership
    checks plus module38/1 metadata/lists provide computational context only. Below-threshold
    psbA1/atpA results are not absence; generated summaries are excluded. The inherited
    organism mismatch remains open.
  target_ids:
  - GO:0030075
  evidence_ids:
  - plaque-current-4
  - plaque-policy
  - plaque-historical-runner
  - plaque-catalogue
  - plaque-adapter-meta
  - plaque-adapter-search-photosystem
  - plaque-adapter-search-cytochrome
  - plaque-adapter-search-ATP-synthase
  - plaque-adapter-gene-Synpcc7942_2049
  - plaque-adapter-gene-Synpcc7942_0424
  - plaque-adapter-gene-Synpcc7942_2331
  - plaque-adapter-gene-Synpcc7942_0336
  - plaque-adapter-module-38
  - plaque-adapter-module-38-genes
  - plaque-adapter-module-1
  - plaque-adapter-module-1-genes
  - plaque-adapter-publication
- assessment_id: plaque-t8-identity
  area: identity
  topic: Exact identity and adjacent structure boundaries
  outcome: supported
  target_ids:
  - GO:0009706
  summary: Native identifiers and source descriptions distinguish the complete organelle,
    its double-membrane envelope including the intervening space, individual inner
    bilayer, and enclosed intermembrane region. Asserted is_a parents and physical
    parts are coherent. The source-neutral GO definition is not silently expanded
    to make every plastid photosynthetic.
  evidence_ids:
  - plaque-current-8
  - plaque-root21-sources-inner-go
  - plaque-inner-isa
  - plaque-root21-sources-SL-0051-json
- assessment_id: plaque-t8-scope
  area: scope
  topic: Green lineage and model-organism context
  outcome: supported
  target_ids:
  - GO:0009706
  summary: Native taxonomy confirms Viridiplantae and C.reinhardtii. Keeling selected
    review text supports photosynthetic green-lineage plastids while acknowledging
    loss/nonphotosynthetic forms. Jin primary abstract supplies envelope-spanning
    TOC–TIC/IMS context; linked7VCF deposited entity metadata confirms species3055.
    No strain, quantitative prevalence or universal translocon composition is inferred.
  evidence_ids:
  - plaque-current-8
  - plaque-root21-sources-inner-go
  - plaque-inner-isa
  - plaque-root21-sources-SL-0051-json
  - plaque-root21-sources-NCBITaxon-33090
  - plaque-root21-sources-NCBITaxon-3055
  - plaque-root21-sources-keeling2010-pmc
  - plaque-root21-sources-doi-10.1016_j.cell.2022.10.030
  - plaque-jin2022-pdb-entry
  - plaque-jin2022-pdb-entity1
- assessment_id: plaque-t8-composition
  area: grounding
  topic: The collective bounding bilayer
  outcome: supported
  target_ids:
  - GO:0009706
  summary: The component is the inner bilayer itself and its ESSENTIAL value is constitutional
    at that collective level. The label-only rationale correctly avoids using the
    whole location term as a chemical identifier for a particular lipid. The record
    does not assert one invariant lipid composition.
  evidence_ids:
  - plaque-current-8
  - plaque-root21-sources-inner-go
  - plaque-inner-isa
  - plaque-root21-sources-SL-0051-json
  - plaque-policy
- assessment_id: plaque-t8-necessity
  area: evidence
  topic: Molecular assembly requirements are not supplied
  outcome: unknown
  target_ids:
  - GO:0009706
  summary: Constitutional existence of a bilayer does not establish necessity of each
    lipid molecule or membrane protein. Those individual requirements remain unresolved,
    and the record does not import translocon perturbation claims as membrane-formation
    assays.
  evidence_ids:
  - plaque-current-8
  - plaque-root21-sources-inner-go
  - plaque-inner-isa
  - plaque-root21-sources-SL-0051-json
  - plaque-policy
- assessment_id: plaque-t8-graph
  area: graph
  topic: Three descriptive membrane boundaries
  outcome: supported
  target_ids:
  - GO:0009706
  summary: The NONMECHANISTIC graph separates envelope parthood from the two spatial
    boundaries. Exact GO definitions and UniProtSL0051 support stroma-facing topology
    and separation from the intermembrane region. Lumen-facing in the GO definition
    means the organelle interior here; the maintained role/graph explicitly specifies
    stroma and does not confuse it with thylakoid lumen.
  evidence_ids:
  - plaque-current-8
  - plaque-root21-sources-inner-go
  - plaque-inner-isa
  - plaque-root21-sources-SL-0051-json
- assessment_id: plaque-t8-provenance
  area: provenance
  topic: Accurate citation identities and bounded access
  outcome: supported
  target_ids:
  - GO:0009706
  summary: Citation identities match native bibliography. Keeling selected secondary
    body was accessible through PMC despite failed alternative routes. Jin biology
    remains primary-abstract scope with separate deposit organism metadata; publisher403
    is not full-body access. Historical reviews/status are unchanged.
  evidence_ids:
  - plaque-current-8
  - plaque-root21-sources-doi-10.1098_rstb.2009.0103
  - plaque-root21-sources-doi-10.1016_j.cell.2022.10.030
  - plaque-root21-sources-keeling2010-pmc
  - plaque-root21-sources-jin2022-publisher
  - plaque-jin2022-pdb-entry
  - plaque-jin2022-pdb-entity1
- assessment_id: plaque-t8-coverage
  area: completeness
  topic: Bounded record-level coverage
  outcome: supported
  target_ids:
  - GO:0009706
  summary: The entire maintained record and cited claim contexts were inspected at
    the stated source scopes. Additional exhaustive component inventories, numerical
    properties, images, traits and expanded mechanisms are optional. No verbatim quotation
    requires repair, and no status or history rewrite is proposed. This bounded review
    does not assert exhaustive literature completeness.
  evidence_ids:
  - plaque-current-8
  - plaque-policy
  - plaque-neighbor-chloroplast
  - plaque-neighbor-chloroplast_envelope
  - plaque-current-9
  - plaque-root21-sources-inner-go
  - plaque-inner-isa
  - plaque-root21-sources-SL-0051-json
- assessment_id: plaque-t8-native-protein
  area: schema
  topic: Native protein identity and graph coverage
  outcome: supported
  summary: Both actual checks exited0. These records have no protein examples and
    no GENE_OR_PROTEIN causal nodes; complex/structure or spatial nodes are not forced
    into individual protein coverage. Empty inventory does not prove molecular membership
    or assembly necessity.
  target_ids:
  - GO:0009706
  evidence_ids:
  - plaque-current-8
  - plaque-native-chloroplast_inner_membrane-verify
  - plaque-native-chloroplast_inner_membrane-causal
- assessment_id: plaque-t8-bundle-provenance
  area: provenance
  topic: Frozen historical input and deterministic bundle validation
  outcome: supported
  summary: Original YAML validates and exact native Markdown render agrees. Historical
    target hash and current hash match; no stale delta requires refresh. New assessments
    correct bundle applicability without rewriting originals or claiming scientific
    record edits.
  target_ids:
  - GO:0009706
  evidence_ids:
  - plaque-current-8
  - plaque-original-8
- assessment_id: plaque-t8-adapter
  area: scope
  topic: TOC–TIC prose triggers real covered-organism assessment
  outcome: supported
  summary: Although the inventory is sparse, taxon/example prose explicitly names
    the TOC–TIC protein-import pathway. It triggers applicability independently of
    transcriptomics claims. The fresh full catalogue has no Chlamydomonas dataset
    or matching green-lineage host; downstream modules from cyanobacteria cannot validate
    chloroplast import. Current bounded outcome is no matching dataset, not a no-expression
    exemption. Historical runner failure remains separately dated.
  target_ids:
  - GO:0009706
  evidence_ids:
  - plaque-current-8
  - plaque-policy
  - plaque-historical-runner
  - plaque-catalogue
  - plaque-root21-sources-doi-10.1016_j.cell.2022.10.030
  - plaque-jin2022-pdb-entity1
- assessment_id: plaque-t9-identity
  area: identity
  topic: Exact identity and adjacent structure boundaries
  outcome: supported
  target_ids:
  - GO:0031972
  summary: Native identifiers and source descriptions distinguish the complete organelle,
    its double-membrane envelope including the intervening space, individual inner
    bilayer, and enclosed intermembrane region. Asserted is_a parents and physical
    parts are coherent. The source-neutral GO definition is not silently expanded
    to make every plastid photosynthetic.
  evidence_ids:
  - plaque-current-9
  - plaque-root21-sources-ims-go
  - plaque-ims-isa
  - plaque-root21-sources-SL-0051-json
  - plaque-root21-sources-SL-0052-json
- assessment_id: plaque-t9-scope
  area: scope
  topic: Green lineage and model-organism context
  outcome: supported
  target_ids:
  - GO:0031972
  summary: Native taxonomy confirms Viridiplantae and C.reinhardtii. Keeling selected
    review text supports photosynthetic green-lineage plastids while acknowledging
    loss/nonphotosynthetic forms. Jin primary abstract supplies envelope-spanning
    TOC–TIC/IMS context; linked7VCF deposited entity metadata confirms species3055.
    No strain, quantitative prevalence or universal translocon composition is inferred.
  evidence_ids:
  - plaque-current-9
  - plaque-root21-sources-ims-go
  - plaque-ims-isa
  - plaque-root21-sources-SL-0051-json
  - plaque-root21-sources-SL-0052-json
  - plaque-root21-sources-NCBITaxon-33090
  - plaque-root21-sources-NCBITaxon-3055
  - plaque-root21-sources-keeling2010-pmc
  - plaque-root21-sources-doi-10.1016_j.cell.2022.10.030
  - plaque-jin2022-pdb-entry
  - plaque-jin2022-pdb-entity1
- assessment_id: plaque-t9-composition
  area: completeness
  topic: A spatial region with no asserted fixed molecular inventory
  outcome: supported
  target_ids:
  - GO:0031972
  summary: 'This record denotes the volume between bilayers. Omitting a molecular
    component list is appropriate: the IMS scaffold described by Jin is part of an
    import complex, not a universal material identity of the entire region. No optional
    inventory or protein example is required to make the topology record complete
    at its stated scope.'
  evidence_ids:
  - plaque-current-9
  - plaque-root21-sources-ims-go
  - plaque-ims-isa
  - plaque-root21-sources-SL-0051-json
  - plaque-root21-sources-SL-0052-json
  - plaque-policy
- assessment_id: plaque-t9-necessity
  area: evidence
  topic: No molecular assembly dependency is encoded
  outcome: unknown
  target_ids:
  - GO:0031972
  summary: The target has no component essentiality assertions. Defining a region
    between membranes does not identify a particular molecule as necessary for its
    formation.
  evidence_ids:
  - plaque-current-9
  - plaque-root21-sources-ims-go
  - plaque-ims-isa
  - plaque-root21-sources-SL-0051-json
  - plaque-root21-sources-SL-0052-json
  - plaque-policy
- assessment_id: plaque-t9-graph
  area: graph
  topic: Two spatial delimitation edges
  outcome: supported
  target_ids:
  - GO:0031972
  summary: Both NONMECHANISTIC edges identify the outer and inner bilayers as the
    two boundaries. Native GO and UniProt definitions support this topology. The exact
    synonym, plastid-intermembrane is_a parent and chloroplast-envelope part_of relation
    are separately verified.
  evidence_ids:
  - plaque-current-9
  - plaque-root21-sources-ims-go
  - plaque-ims-isa
  - plaque-root21-sources-SL-0051-json
  - plaque-root21-sources-SL-0052-json
- assessment_id: plaque-t9-provenance
  area: provenance
  topic: Accurate citation identities and bounded access
  outcome: supported
  target_ids:
  - GO:0031972
  summary: Citation identities match native bibliography. Keeling selected secondary
    body was accessible through PMC despite failed alternative routes. Jin biology
    remains primary-abstract scope with separate deposit organism metadata; publisher403
    is not full-body access. Historical reviews/status are unchanged.
  evidence_ids:
  - plaque-current-9
  - plaque-root21-sources-doi-10.1098_rstb.2009.0103
  - plaque-root21-sources-doi-10.1016_j.cell.2022.10.030
  - plaque-root21-sources-keeling2010-pmc
  - plaque-root21-sources-jin2022-publisher
  - plaque-jin2022-pdb-entry
  - plaque-jin2022-pdb-entity1
- assessment_id: plaque-t9-coverage
  area: completeness
  topic: Bounded record-level coverage
  outcome: supported
  target_ids:
  - GO:0031972
  summary: The entire maintained record and cited claim contexts were inspected at
    the stated source scopes. Additional exhaustive component inventories, numerical
    properties, images, traits and expanded mechanisms are optional. No verbatim quotation
    requires repair, and no status or history rewrite is proposed. This bounded review
    does not assert exhaustive literature completeness.
  evidence_ids:
  - plaque-current-9
  - plaque-policy
  - plaque-neighbor-chloroplast
  - plaque-neighbor-chloroplast_envelope
  - plaque-current-8
  - plaque-root21-sources-ims-go
  - plaque-ims-isa
  - plaque-root21-sources-SL-0051-json
  - plaque-root21-sources-SL-0052-json
- assessment_id: plaque-t9-native-protein
  area: schema
  topic: Native protein identity and graph coverage
  outcome: supported
  summary: Both actual checks exited0. These records have no protein examples and
    no GENE_OR_PROTEIN causal nodes; complex/structure or spatial nodes are not forced
    into individual protein coverage. Empty inventory does not prove molecular membership
    or assembly necessity.
  target_ids:
  - GO:0031972
  evidence_ids:
  - plaque-current-9
  - plaque-native-chloroplast_intermembrane_space-verify
  - plaque-native-chloroplast_intermembrane_space-causal
- assessment_id: plaque-t9-bundle-provenance
  area: provenance
  topic: Frozen historical input and deterministic bundle validation
  outcome: supported
  summary: Original YAML validates and exact native Markdown render agrees. Historical
    target hash and current hash match; no stale delta requires refresh. New assessments
    correct bundle applicability without rewriting originals or claiming scientific
    record edits.
  target_ids:
  - GO:0031972
  evidence_ids:
  - plaque-current-9
  - plaque-original-9
- assessment_id: plaque-t9-adapter
  area: scope
  topic: TOC–TIC prose triggers real covered-organism assessment
  outcome: supported
  summary: Although the inventory is sparse, taxon/example prose explicitly names
    the TOC–TIC protein-import pathway. It triggers applicability independently of
    transcriptomics claims. The fresh full catalogue has no Chlamydomonas dataset
    or matching green-lineage host; downstream modules from cyanobacteria cannot validate
    chloroplast import. Current bounded outcome is no matching dataset, not a no-expression
    exemption. Historical runner failure remains separately dated.
  target_ids:
  - GO:0031972
  evidence_ids:
  - plaque-current-9
  - plaque-policy
  - plaque-historical-runner
  - plaque-catalogue
  - plaque-root21-sources-doi-10.1016_j.cell.2022.10.030
  - plaque-jin2022-pdb-entity1
- assessment_id: micro-autophagosome-a1
  area: schema
  topic: Immutable original validation and input comparison
  outcome: supported
  summary: Original validate/render succeeds and frozen source blob matches. Current
    record changed and receives substantive source reassessment below; original files
    remain immutable.
  target_ids:
  - GO:0005776
  evidence_ids:
  - micro-record-autophagosome
  - micro-prior-autophagosome
  - micro-original-validation-inputs
- assessment_id: micro-autophagosome-a2
  area: schema
  topic: Native current protein verifier and graph inventory
  outcome: supported
  summary: Both current native commands return0, with zero protein examples and zero
    GENE_OR_PROTEIN nodes. Empty-inventory success is not experimental completeness.
  target_ids:
  - GO:0005776
  evidence_ids:
  - micro-record-autophagosome
  - micro-native-autophagosome-verify
  - micro-native-autophagosome-causal
- assessment_id: micro-autophagosome_lumen-a1
  area: schema
  topic: Immutable original validation and input comparison
  outcome: supported
  summary: Original validate/render succeeds and frozen source blob matches. Current
    record equals the original frozen target; source and scope are independently reassessed.
  target_ids:
  - GO:0034423
  evidence_ids:
  - micro-record-autophagosome_lumen
  - micro-prior-autophagosome_lumen
  - micro-original-validation-inputs
- assessment_id: micro-autophagosome_lumen-a2
  area: schema
  topic: Native current protein verifier and graph inventory
  outcome: supported
  summary: Both current native commands return0, with zero protein examples and zero
    GENE_OR_PROTEIN nodes. Empty-inventory success is not experimental completeness.
  target_ids:
  - GO:0034423
  evidence_ids:
  - micro-record-autophagosome_lumen
  - micro-native-autophagosome_lumen-verify
  - micro-native-autophagosome_lumen-causal
- assessment_id: micro-autophagosome_membrane-a1
  area: schema
  topic: Immutable original validation and input comparison
  outcome: supported
  summary: Original validate/render succeeds and frozen source blob matches. Current
    record equals the original frozen target; source and scope are independently reassessed.
  target_ids:
  - GO:0000421
  evidence_ids:
  - micro-record-autophagosome_membrane
  - micro-prior-autophagosome_membrane
  - micro-original-validation-inputs
- assessment_id: micro-autophagosome_membrane-a2
  area: schema
  topic: Native current protein verifier and graph inventory
  outcome: supported
  summary: Both current native commands return0, with zero protein examples and zero
    GENE_OR_PROTEIN nodes. Empty-inventory success is not experimental completeness.
  target_ids:
  - GO:0000421
  evidence_ids:
  - micro-record-autophagosome_membrane
  - micro-native-autophagosome_membrane-verify
  - micro-native-autophagosome_membrane-causal
- assessment_id: micro-chitosome-a1
  area: schema
  topic: Immutable original validation and input comparison
  outcome: supported
  summary: Original validate/render succeeds and frozen source blob matches. Current
    record changed and receives substantive source reassessment below; original files
    remain immutable.
  target_ids:
  - GO:0045009
  evidence_ids:
  - micro-record-chitosome
  - micro-prior-chitosome
  - micro-original-validation-inputs
- assessment_id: micro-chitosome-a2
  area: schema
  topic: Native current protein verifier and graph inventory
  outcome: supported
  summary: The current verifier passes for two reviewed CHS examples; graph coverage
    is one COVERED protein node. These checks do not establish localization, essentiality,
    or a complete fungal protein cohort.
  target_ids:
  - GO:0045009
  evidence_ids:
  - micro-record-chitosome
  - micro-native-chitosome-verify
  - micro-native-chitosome-causal
- assessment_id: micro-autophagosome-a3
  area: identity
  topic: Whole organelle identity and part boundaries
  outcome: supported
  summary: GO exact identity, organelle kind, double-membrane definition and two synonym
    scopes agree. Membrane and lumen are parts, not is-a equivalents; invading-microorganism
    wording derives from the authority definition, not the yeast experiments.
  target_ids:
  - GO:0005776
  evidence_ids:
  - micro-record-autophagosome
  - micro-auto-go
- assessment_id: micro-autophagosome-a4
  area: grounding
  topic: 'Stale refresh: macroautophagy function grounding'
  outcome: supported
  summary: The changed function now explicitly uses GO:0016236, which exactly denotes
    macroautophagy through autophagosome formation. Existing graph grounding already
    used that term; no new mechanistic or taxonomic claim is introduced.
  target_ids:
  - GO:0005776
  evidence_ids:
  - micro-record-autophagosome
  - micro-prior-autophagosome
  - micro-auto-go
  - micro-original-validation-inputs
- assessment_id: micro-autophagosome-a5
  area: evidence
  topic: Yeast starvation and canonical model source scope
  outcome: supported
  summary: Starvation-conditioned yeast autophagy and the genetic/fluorescence model
    are supported. COMMON is read with the explicit induction condition, not constitutive
    presence in every cell. PAS organization is distinguished from a mature autophagosome.
  target_ids:
  - GO:0005776
  evidence_ids:
  - micro-record-autophagosome
  - micro-auto-taxon-4932
  - micro-auto-takeshige1992-xml
  - micro-auto-suzuki2001-publisher
- assessment_id: micro-autophagosome-a6
  area: completeness
  topic: Constituent boundary and deferred Atg cohorts
  outcome: supported
  summary: The collective membrane boundary is essential by organelle identity; this
    does not assign essentiality to an individual lipid or Atg protein. The existing
    TODO explicitly defers exact taxon-neutral machinery while the graph is NONMECHANISTIC.
    No false absent-family assertion or fabricated universal protein inventory is
    added.
  target_ids:
  - GO:0005776
  evidence_ids:
  - micro-record-autophagosome
  - micro-auto-go
  - micro-auto-ichimura2000-publisher
  - micro-auto-suzuki2001-publisher
  - micro-graph-contract
- assessment_id: micro-autophagosome-a7
  area: graph
  topic: All four boundary/function/fusion edges
  outcome: supported
  summary: Bounds, parthood and macroautophagy support are authority-aligned. The
    yeast vacuole-fusion endpoint is explicitly supported by GO:0061909; Takeshige
    establishes vacuolar bodies but does not independently dissect the fusion mechanism.
    The graph preserves that coarse scope.
  target_ids:
  - GO:0005776
  evidence_ids:
  - micro-record-autophagosome
  - micro-auto-go
  - micro-auto-takeshige1992-xml
  - micro-graph-contract
- assessment_id: micro-autophagosome-a8
  area: scope
  topic: Structured-source applicability correction
  outcome: concern
  summary: Original expression-only N/A rationale is inadequate for named macroautophagy
    and ATG context. Fresh full-catalogue assessment finds no fungal dataset, so matched-organism
    search/module summary is unavailable; absence is not negative science.
  target_ids:
  - GO:0005776
  evidence_ids:
  - micro-prior-autophagosome
  - micro-record-autophagosome
  - micro-review-policy
  - micro-review-config
  - micro-adapter-catalogue
  - micro-historical-adapter-runner
- assessment_id: micro-autophagosome-a9
  area: provenance
  topic: Current assessment and original clean verdict
  outcome: supported
  summary: The original clean scientific outcome is retained after refreshing changed
    grounding. Source-access limitations remain explicit; no current scientific finding
    or prior terminal category-finding resolution is asserted.
  target_ids:
  - GO:0005776
  evidence_ids:
  - micro-prior-autophagosome
  - micro-record-autophagosome
  - micro-auto-xie2007-publisher
  - micro-auto-ichimura2000-publisher
- assessment_id: micro-autophagosome_lumen-a3
  area: identity
  topic: Volume identity, synonyms and hierarchy
  outcome: supported
  summary: The lumen is a subcellular volume, not a protein complex or membrane. GO
    exact definition and UniProt synonyms, vesicle-lumen is-a and autophagosome parthood
    agree; the model is not claimed to reproduce current GO direct parent edges.
  target_ids:
  - GO:0034423
  evidence_ids:
  - micro-record-autophagosome_lumen
  - micro-auto-go
  - micro-auto-SL-0318-json
- assessment_id: micro-autophagosome_lumen-a4
  area: evidence
  topic: Yeast occurrence and experimental exemplar
  outcome: supported
  summary: The inherited conditional yeast context and formation-model citation are
    supported by the same bounded starvation and PAS experiments. Neither is used
    to infer resident lumen components from transient degradative cargo.
  target_ids:
  - GO:0034423
  evidence_ids:
  - micro-record-autophagosome_lumen
  - micro-auto-taxon-4932
  - micro-auto-takeshige1992-xml
  - micro-auto-suzuki2001-publisher
- assessment_id: micro-autophagosome_lumen-a5
  area: graph
  topic: Two topology edges and omitted cargo inventory
  outcome: supported
  summary: Lumen parthood and membrane bounds agree with GO/UniProt. No resident protein,
    enzymatic function or complete Atg mechanism is asserted; omission of transient
    cargo from components is appropriate.
  target_ids:
  - GO:0034423
  evidence_ids:
  - micro-record-autophagosome_lumen
  - micro-auto-go
  - micro-auto-SL-0318-json
  - micro-graph-contract
- assessment_id: micro-autophagosome_lumen-a6
  area: scope
  topic: Sparse topology applicability exclusion
  outcome: not_applicable
  summary: This record asserts a compartment and two topology edges; macroautophagy
    supplies enclosing-organelle context and Atg wording expressly excludes mechanism.
    It has no named resident-protein/function/pathway inventory needing a matched
    molecular query. It is not counted as an additional adapter defect; the same catalogue
    also has no yeast match.
  target_ids:
  - GO:0034423
  evidence_ids:
  - micro-record-autophagosome_lumen
  - micro-review-policy
  - micro-review-config
  - micro-adapter-catalogue
- assessment_id: micro-autophagosome_lumen-a7
  area: provenance
  topic: Unchanged original clean verdict
  outcome: supported
  summary: The exact frozen record is unchanged; independent current source inspection
    identifies no scientific correction. Original source/validation dates and limited
    access remain historical rather than silently renewed.
  target_ids:
  - GO:0034423
  evidence_ids:
  - micro-record-autophagosome_lumen
  - micro-prior-autophagosome_lumen
  - micro-original-validation-inputs
- assessment_id: micro-autophagosome_membrane-a3
  area: identity
  topic: Boundary identity, synonyms and hierarchy
  outcome: supported
  summary: Active GO:0000421 and UniProt SL-0022 agree on membrane identity, synonyms,
    cytoplasmic-vesicle-membrane is-a and autophagosome parthood. This is distinct
    from both the organelle and its lumen.
  target_ids:
  - GO:0000421
  evidence_ids:
  - micro-record-autophagosome_membrane
  - micro-auto-go
  - micro-auto-SL-0022-json
- assessment_id: micro-autophagosome_membrane-a4
  area: completeness
  topic: Generic lipid material and essentiality
  outcome: supported
  summary: The ungrounded constituent is generic lipid-bilayer material, not a second
    whole-membrane identity. The explicit rationale correctly avoids substituting
    the whole-structure GO term for a chemical constituent; essentiality attaches
    to the collective boundary. No exact chemical was invented.
  target_ids:
  - GO:0000421
  evidence_ids:
  - micro-record-autophagosome_membrane
  - micro-auto-go
  - micro-auto-SL-0022-json
  - micro-auto-xie2007-publisher
- assessment_id: micro-autophagosome_membrane-a5
  area: evidence
  topic: Function and yeast exemplar
  outcome: supported
  summary: Macroautophagy grounding is exact and the membrane function is coarse.
    Yeast induction and PAS/formation model remain condition-scoped. Xie is secondary
    abstract context; it is not treated as a newly inspected full experimental body.
  target_ids:
  - GO:0000421
  evidence_ids:
  - micro-record-autophagosome_membrane
  - micro-auto-go
  - micro-auto-takeshige1992-xml
  - micro-auto-suzuki2001-publisher
  - micro-auto-xie2007-publisher
  - micro-auto-taxon-4932
- assessment_id: micro-autophagosome_membrane-a6
  area: graph
  topic: Three boundary and support edges
  outcome: supported
  summary: Bounds, parthood and macroautophagy support are consistent with authority
    definitions. The stated NONMECHANISTIC scope does not assert molecular initiation,
    closure or fusion mechanisms.
  target_ids:
  - GO:0000421
  evidence_ids:
  - micro-record-autophagosome_membrane
  - micro-auto-go
  - micro-auto-SL-0022-json
  - micro-graph-contract
- assessment_id: micro-autophagosome_membrane-a7
  area: scope
  topic: Structured-source applicability correction
  outcome: concern
  summary: The original expression-only N/A rationale is inadequate for the explicit
    macroautophagy function/pathway assertion. Current catalogue has no fungal match,
    so no target-specific downstream module query can be grounded; this is a bounded
    coverage conclusion.
  target_ids:
  - GO:0000421
  evidence_ids:
  - micro-record-autophagosome_membrane
  - micro-prior-autophagosome_membrane
  - micro-review-policy
  - micro-review-config
  - micro-adapter-catalogue
  - micro-historical-adapter-runner
- assessment_id: micro-autophagosome_membrane-a8
  area: provenance
  topic: Unchanged original clean verdict
  outcome: supported
  summary: Independent inspection retains the clean scientific verdict for the unchanged
    record; adapter rationale is a bundle repair, not a reason to mutate scientific
    record content.
  target_ids:
  - GO:0000421
  evidence_ids:
  - micro-record-autophagosome_membrane
  - micro-prior-autophagosome_membrane
  - micro-original-validation-inputs
- assessment_id: micro-chitosome-a3
  area: identity
  topic: Fungal vesicle identity, definition and taxon scope
  outcome: supported
  summary: Exact GO identity and cytoplasmic-vesicle parent are appropriate. The multi-lineage
    secondary review is retained as bounded fungal context, not evidence of universality;
    the Saccharomyces example has primary trafficking support.
  target_ids:
  - GO:0045009
  evidence_ids:
  - micro-record-chitosome
  - micro-chito-go
  - micro-chito-tax-4751
  - micro-auto-taxon-4932
  - micro-chito-bartnicki2006-pdf
  - micro-chito-ziman1998-browser-discussion
- assessment_id: micro-chitosome-a4
  area: grounding
  topic: Inherited exact membrane grounding F1
  outcome: concern
  summary: Current component and active discussion still assert that no exact chitosome
    membrane term exists. Active GO:0030661 is the exact match; preserve the original
    finding key and minor severity while leaving record curation outside this PR.
  target_ids:
  - GO:0045009
  evidence_ids:
  - micro-record-chitosome
  - micro-prior-chitosome
  - micro-chito-go
  - micro-chito-go-parts
- assessment_id: micro-chitosome-a5
  area: grounding
  topic: CHS examples, families and identity limits
  outcome: supported
  summary: Both declared S288C examples are reviewed exact gene identities, and the
    bounded reviewed-symbol query confirms one entry per gene. Both match broad IPR004835;
    that does not establish every family member as resident cargo or erase the unresolved
    heterogeneous fungal-cohort TODO.
  target_ids:
  - GO:0045009
  evidence_ids:
  - micro-record-chitosome
  - micro-chito-P08004
  - micro-chito-P29465
  - micro-chito-reviewed-uniqueness
  - micro-chito-tax-559292
  - micro-chito-IPR004835
  - micro-chito-ipr-matches-P08004
  - micro-chito-ipr-matches-P29465
- assessment_id: micro-chitosome-a6
  area: evidence
  topic: Protein source annotations and necessity scope
  outcome: supported
  summary: The three P29465 PMIDs are genuine experimental Cell membrane annotations
    and are labeled accordingly. Native graph coverage is complete for the two declared
    symbols, not all fungal isoenzymes. UNKNOWN protein essentiality avoids inferring
    universal necessity from yeast transport mutations.
  target_ids:
  - GO:0045009
  evidence_ids:
  - micro-record-chitosome
  - micro-chito-P29465
  - micro-chito-PMID-12928491
  - micro-chito-PMID-17519287
  - micro-chito-PMID-28346351
  - micro-native-chitosome-verify
  - micro-native-chitosome-causal
- assessment_id: micro-chitosome-a7
  area: graph
  topic: 'Stale refresh: plasma-membrane cargo-delivery edge'
  outcome: supported
  summary: The new edge is supported for delivery by primary Chs3 trafficking experiments.
    Its stated purpose of cell-surface activation is read within explicit NONMECHANISTIC
    scope, not as proof that transport is sufficient for activation or that all isoenzymes
    share Chs6 dependence. The primary Discussion leaves activation alternatives unresolved.
  target_ids:
  - GO:0045009
  evidence_ids:
  - micro-record-chitosome
  - micro-prior-chitosome
  - micro-chito-ziman1998-browser-discussion
  - micro-chito-PMID-17519287
  - micro-graph-contract
- assessment_id: micro-chitosome-a8
  area: graph
  topic: Existing storage, membrane, septum and product edges
  outcome: supported
  summary: The boundary and latent-cargo pool have authority/fractionation support;
    polarized delivery has yeast primary evidence. Septum delivery remains proposed,
    chitin is chemical output rather than resident cargo, and secondary review disagreements
    about ontogeny are not promoted into settled mechanism.
  target_ids:
  - GO:0045009
  evidence_ids:
  - micro-record-chitosome
  - micro-chito-go
  - micro-chito-chebi17029
  - micro-chito-leal1988-meta
  - micro-chito-jats-PMC2132460
  - micro-chito-bartnicki2006-pdf
- assessment_id: micro-chitosome-a9
  area: consistency
  topic: Pinned PathwayMech relation
  outcome: supported
  summary: The exact pinned S288C model contains CHS3 and its chitin-synthesis activity.
    The record correctly states enzyme delivery to cell surface and preserves species-experiment
    versus narrower pathway-strain scope; it does not relocate catalysis into the
    chitosome.
  target_ids:
  - GO:0045009
  evidence_ids:
  - micro-record-chitosome
  - micro-pathway-commit
  - micro-chito-tax-559292
  - micro-chito-ziman1998-browser-discussion
- assessment_id: micro-chitosome-a10
  area: scope
  topic: Missing structured-source applicability assessment
  outcome: concern
  summary: Original check list omits applicability despite CHS1/CHS3 and declared
    pathway delivery. Fresh catalogue inspection supplies a bounded no-fungal-dataset
    conclusion; no unmatched bacterial gene/module query is substituted.
  target_ids:
  - GO:0045009
  evidence_ids:
  - micro-record-chitosome
  - micro-prior-chitosome
  - micro-review-policy
  - micro-review-config
  - micro-adapter-catalogue
  - micro-historical-adapter-runner
- assessment_id: micro-chitosome-a11
  area: provenance
  topic: Exact inherited finding lineage and verdict
  outcome: concern
  summary: Original20261021T110752Z-chitosome-audit/F1 remains open with its stable
    key and minor confirmed severity. Current needs_curation is solely the exact membrane-grounding
    defect found here; the refresh itself can be completed in a review-only successor.
  target_ids:
  - GO:0045009
  evidence_ids:
  - micro-record-chitosome
  - micro-prior-chitosome
  - micro-chito-go-parts
  - micro-original-validation-inputs
- assessment_id: septin-apicoplast_membrane-schema
  area: schema
  topic: Native schema, deterministic rendering and unchanged frozen input
  outcome: supported
  summary: Original review validates and renders byte-identically. Its target hash
    equals the original source bytes and current source-head bytes. Root-run native
    protein gates pass within their explicit inventory limits.
  target_ids:
  - GO:0160211
  evidence_ids:
  - septin-record-apicoplast_membrane
  - septin-original-apicoplast_membrane
  - septin-original-validation-apicoplast_membrane
  - septin-native-apicoplast_membrane-verify
  - septin-native-apicoplast_membrane-causal
- assessment_id: septin-chloroplast-schema
  area: schema
  topic: Native schema, deterministic rendering and unchanged frozen input
  outcome: supported
  summary: Original review validates and renders byte-identically. Its target hash
    equals the original source bytes and current source-head bytes. Root-run native
    protein gates pass within their explicit inventory limits.
  target_ids:
  - GO:0009507
  evidence_ids:
  - septin-record-chloroplast
  - septin-original-chloroplast
  - septin-original-validation-chloroplast
  - septin-native-chloroplast-verify
  - septin-native-chloroplast-causal
- assessment_id: septin-chloroplast_envelope-schema
  area: schema
  topic: Native schema, deterministic rendering and unchanged frozen input
  outcome: supported
  summary: Original review validates and renders byte-identically. Its target hash
    equals the original source bytes and current source-head bytes. Root-run native
    protein gates pass within their explicit inventory limits.
  target_ids:
  - GO:0009941
  evidence_ids:
  - septin-record-chloroplast_envelope
  - septin-original-chloroplast_envelope
  - septin-original-validation-chloroplast_envelope
  - septin-native-chloroplast_envelope-verify
  - septin-native-chloroplast_envelope-causal
- assessment_id: septin-apicoplast_membrane-adapter
  area: scope
  topic: Structured-source applicability and actual organism coverage
  outcome: not_applicable
  summary: Named molecular actors/import pathways trigger applicability assessment.
    The current complete official catalogue has no matched organism/dataset for this
    target; downstream gene/module lookups therefore do not apply. Runner unavailability
    is historical and separate. No bacterial/cyanobacterial dataset is substituted
    for a eukaryotic plastid.
  target_ids:
  - GO:0160211
  evidence_ids:
  - septin-record-apicoplast_membrane
  - septin-native-review-policy
  - septin-current-adapter-catalogue
  - septin-historical-adapter-runner-unavailable
- assessment_id: septin-apicoplast_membrane-image-scope
  area: scope
  topic: Images, snippets and unobserved measurements
  outcome: not_applicable
  summary: The current record has no attached image or verbatim snippet requiring
    image/snippet validation. Source caption/text inspection is not pixel or raw-data
    reanalysis.
  target_ids:
  - GO:0160211
  evidence_ids:
  - septin-record-apicoplast_membrane
- assessment_id: septin-chloroplast-adapter
  area: scope
  topic: Structured-source applicability and actual organism coverage
  outcome: not_applicable
  summary: Named molecular actors/import pathways trigger applicability assessment.
    The current complete official catalogue has no matched organism/dataset for this
    target; downstream gene/module lookups therefore do not apply. Runner unavailability
    is historical and separate. No bacterial/cyanobacterial dataset is substituted
    for a eukaryotic plastid.
  target_ids:
  - GO:0009507
  evidence_ids:
  - septin-record-chloroplast
  - septin-native-review-policy
  - septin-current-adapter-catalogue
  - septin-historical-adapter-runner-unavailable
- assessment_id: septin-chloroplast-image-scope
  area: scope
  topic: Images, snippets and unobserved measurements
  outcome: not_applicable
  summary: The current record has no attached image or verbatim snippet requiring
    image/snippet validation. Source caption/text inspection is not pixel or raw-data
    reanalysis.
  target_ids:
  - GO:0009507
  evidence_ids:
  - septin-record-chloroplast
- assessment_id: septin-chloroplast_envelope-adapter
  area: scope
  topic: Structured-source applicability and actual organism coverage
  outcome: not_applicable
  summary: Named molecular actors/import pathways trigger applicability assessment.
    The current complete official catalogue has no matched organism/dataset for this
    target; downstream gene/module lookups therefore do not apply. Runner unavailability
    is historical and separate. No bacterial/cyanobacterial dataset is substituted
    for a eukaryotic plastid.
  target_ids:
  - GO:0009941
  evidence_ids:
  - septin-record-chloroplast_envelope
  - septin-native-review-policy
  - septin-current-adapter-catalogue
  - septin-historical-adapter-runner-unavailable
- assessment_id: septin-chloroplast_envelope-image-scope
  area: scope
  topic: Images, snippets and unobserved measurements
  outcome: not_applicable
  summary: The current record has no attached image or verbatim snippet requiring
    image/snippet validation. Source caption/text inspection is not pixel or raw-data
    reanalysis.
  target_ids:
  - GO:0009941
  evidence_ids:
  - septin-record-chloroplast_envelope
- assessment_id: septin-apicoplast_membrane-identity
  area: identity
  topic: Exact membrane identity and whole-organelle boundary
  outcome: supported
  summary: GO:0160211 identifies an apicoplast lipid bilayer, GO:0016020 its broad
    membrane parent, and GO:0020011 the containing organelle. Frozen whole-apicoplast
    neighbor gives compatible parthood; identity is not broadened to the whole organelle.
  target_ids:
  - GO:0160211
  evidence_ids:
  - septin-record-apicoplast_membrane
  - septin-apicoplast-membrane-agent-go
  - septin-context-apicoplast
- assessment_id: septin-apicoplast_membrane-lipid-component
  area: grounding
  topic: Collective lipid constituent and necessity
  outcome: supported
  summary: The label-only lipid-bilayer constituent is a collective matrix of the
    membrane structure; its essentiality is definitional at this collective scale.
    No individual lipid species, unique class CURIE or specific biosynthetic gene
    is inferred essential. The whole-membrane GO identity is not reused as the chemical
    matrix.
  target_ids:
  - GO:0160211
  evidence_ids:
  - septin-record-apicoplast_membrane
  - septin-apicoplast-membrane-agent-go
  - septin-apicoplast-agent-jats-PMC3662607
  - septin-native-curation-policy
- assessment_id: septin-apicoplast_membrane-taxa
  area: scope
  topic: Variable apicomplexan presence and exact example taxa
  outcome: supported
  summary: Exact native taxonomy supports Apicomplexa, Toxoplasma and Plasmodium identities.
    Secondary review context supports VARIABLE presence rather than universality;
    experimental membrane architecture and Tic20 claims retain their stated organism
    scope.
  target_ids:
  - GO:0160211
  evidence_ids:
  - septin-record-apicoplast_membrane
  - septin-apicoplast-agent-tax-5794
  - septin-apicoplast-agent-tax-5811
  - septin-apicoplast-agent-tax-5833
  - septin-apicoplast-agent-tax-508771
  - septin-apicoplast-agent-tax-36329
  - septin-apicoplast-agent-jats-PMC5406208
- assessment_id: septin-apicoplast_membrane-four-membranes
  area: evidence
  topic: Direct membrane-architecture evidence
  outcome: supported
  summary: Lemgruber primary cryo-electron tomography resolves four membranes in Plasmodium
    merozoites, matching the scoped canonical example and membrane-boundary claim.
    Captions/Results were inspected; no new image-pixel or reconstruction analysis
    is claimed.
  target_ids:
  - GO:0160211
  evidence_ids:
  - septin-record-apicoplast_membrane
  - septin-apicoplast-agent-jats-PMC3662607
- assessment_id: septin-apicoplast_membrane-tic20-identity
  area: grounding
  topic: S8GBF3 identity, family and experimental scope
  outcome: supported
  summary: S8GBF3 is unreviewed T. gondii ME49 TIC20/TGME49_255370 with native Tic20-family
    match. The institutional copy of van Dooren primary study supports innermost-membrane
    placement and import dependency. Metadata/family matches alone do not prove location,
    essentiality or pore formation.
  target_ids:
  - GO:0160211
  evidence_ids:
  - septin-record-apicoplast_membrane
  - septin-apicoplast-agent-S8GBF3
  - septin-apicoplast-agent-matches-S8GBF3
  - septin-agrawal2011-thesis
- assessment_id: septin-apicoplast_membrane-tic20-graph
  area: graph
  topic: Tic20 topology versus direct channel mechanism
  outcome: supported
  summary: The actual edge is resides in and the graph explicitly excludes a full
    import reaction. It is supported at localization/import-step scope. Early residual
    import and delayed near-complete block are retained; neither the node label nor
    this acceptance is treated as direct proof that Tic20 is a pore. A different whole-organelle
    translocates edge is outside this target.
  target_ids:
  - GO:0160211
  evidence_ids:
  - septin-record-apicoplast_membrane
  - septin-agrawal2011-thesis
  - septin-native-graph-policy
- assessment_id: septin-apicoplast_membrane-selma-paralog
  area: identity
  topic: B9PY98 ER versus apicoplast Der1 identity
  outcome: concern
  summary: 'Original F1 remains: the SELMA node includes B9PY98, whose native ENA
    bridge is Der1ER1 FJ976521/ACU32856.1. Primary-study deposit mapping distinguishes
    apicoplast Der1Ap FJ976520/ACU32855.1/C9WWW6. Identifier validity and shared family
    membership cannot cure a wrong cellular paralog.'
  target_ids:
  - GO:0160211
  evidence_ids:
  - septin-record-apicoplast_membrane
  - septin-original-apicoplast_membrane
  - septin-apicoplast-agent-B9PY98
  - septin-apicoplast-agent-C9WWW6
  - septin-apicoplast-agent-ena-FJ976521
  - septin-apicoplast-agent-ena-FJ976520
  - septin-agrawal2011-thesis
- assessment_id: septin-apicoplast_membrane-selma-pf-identity
  area: evidence
  topic: O97275/PfsDer1-2 evidence bridge
  outcome: supported
  summary: Native O97275/CAB38986.4/PF3D7_0314300 metadata and NCBI Gene support the
    locus bridge; the Kalanon published Der1-2 antibody peptide matches O97275. Der1-2
    antibody experiments are kept distinct from full-length Der1-1 localization. This
    bounded representative identity does not validate every SELMA constituent.
  target_ids:
  - GO:0160211
  evidence_ids:
  - septin-record-apicoplast_membrane
  - septin-apicoplast-agent-O97275
  - septin-apicoplast-agent-ena-CAB38986
  - septin-apicoplast-agent-gene-814456
  - septin-apicoplast-agent-kalanon2009-pdf
- assessment_id: septin-apicoplast_membrane-import-function
  area: evidence
  topic: Protein-import boundary and outer-envelope system
  outcome: supported
  summary: Agrawal2013 primary localization/ablation/complementation and the Tic20
    study support an apicoplast protein-import system. The SELMA outer-membrane position
    retains source-model scope; the membrane record does not claim an identified endogenous
    ubiquitin modifier or a complete import mechanism.
  target_ids:
  - GO:0160211
  evidence_ids:
  - septin-record-apicoplast_membrane
  - septin-apicoplast-agent-jats-PMC3681736
  - septin-apicoplast-agent-jats-PMC2817234
  - septin-agrawal2011-thesis
- assessment_id: septin-apicoplast_membrane-native-limits
  area: provenance
  topic: Native identifier checks are not localization checks
  outcome: supported
  summary: 'Both native commands pass: three graph UniProt xrefs resolve and two nodes
    are UNANCHORED_WITH_UNIPROT. This establishes limited identifier inventory coverage;
    it does not contradict or resolve the ER-paralog finding.'
  target_ids:
  - GO:0160211
  evidence_ids:
  - septin-native-apicoplast_membrane-verify
  - septin-native-apicoplast_membrane-causal
  - septin-apicoplast-agent-ena-FJ976521
- assessment_id: septin-apicoplast_membrane-verdict
  area: consistency
  topic: Current target verdict and exact finding continuity
  outcome: concern
  summary: needs_curation remains appropriate for the unchanged record because the
    original major wrong-paralog xref is still present. Preserve its original issue
    key and F1 occurrence; file separate membrane-target curation rather than claiming
    a whole-apicoplast issue resolves this record.
  target_ids:
  - GO:0160211
  evidence_ids:
  - septin-record-apicoplast_membrane
  - septin-original-apicoplast_membrane
  - septin-apicoplast-agent-ena-FJ976521
  - septin-agrawal2011-thesis
- assessment_id: septin-chloroplast-identity
  area: identity
  topic: Exact organelle/envelope identity, parentage and parthood
  outcome: supported
  summary: The chlorophyll-containing plastid identity is GO:0009507, with GO:0009536
    as is-a parent. Exact component GO definitions and typed child relations distinguish
    envelope, bilayers, stroma and thylakoids.
  target_ids:
  - GO:0009507
  evidence_ids:
  - septin-record-chloroplast
  - septin-root21-sources-chloroplast-go
  - septin-root21-sources-ancestors-0009507
  - septin-context-chloroplast_inner_membrane
  - septin-context-chloroplast_intermembrane_space
- assessment_id: septin-chloroplast-taxa
  area: scope
  topic: Taxonomic identities, prevalence qualification and experimental organism
  outcome: supported
  summary: ENA verifies Viridiplantae and Chlamydomonas reinhardtii; Keeling secondary
    body supports primary-plastid green-algal/plant context. COMMON is qualified to
    photosynthetic members, not all Viridiplantae. The Jin architecture is explicitly
    Chlamydomonas and is not universalized to every plastid.
  target_ids:
  - GO:0009507
  evidence_ids:
  - septin-record-chloroplast
  - septin-root21-sources-NCBITaxon-33090
  - septin-root21-sources-NCBITaxon-3055
  - septin-root21-sources-keeling2010-pmc
  - septin-root21-sources-doi-10.1016_j.cell.2022.10.030
- assessment_id: septin-chloroplast-components
  area: grounding
  topic: Membrane and import-complex boundaries
  outcome: supported
  summary: Three membrane components have exact GO identities. The divergent Chlamydomonas
    TOC-TIC aggregate is explicitly label-only; current GO:0061927 contains classical
    Tic110/Toc159/Toc34 requirements, so withholding that specific identity is justified
    rather than generic family-grounding deferral.
  target_ids:
  - GO:0009507
  evidence_ids:
  - septin-record-chloroplast
  - septin-root21-sources-chloroplast-go
  - septin-root21-sources-GO0061927
  - septin-root21-sources-doi-10.1016_j.cell.2022.10.030
- assessment_id: septin-chloroplast-necessity
  area: scope
  topic: Unknown formation dependencies
  outcome: unknown
  summary: Component necessity remains UNKNOWN. Ontological identity, proteome localization
    and a resolved import assembly do not by themselves establish whether removal
    of each constituent prevents formation of this complete maintained structure.
    No formation-dependency claim is added.
  target_ids:
  - GO:0009507
  evidence_ids:
  - septin-record-chloroplast
  - septin-native-curation-policy
  - septin-root21-sources-doi-10.1016_j.cell.2022.10.030
- assessment_id: septin-chloroplast-import
  area: evidence
  topic: Chlamydomonas envelope-spanning import architecture
  outcome: supported
  summary: Jin primary abstract and author-hosted abstract support the 14-component
    envelope-spanning TOC-TIC assembly, with a potential Tic20/YlmG inner route and
    intermembrane scaffold. The record states compartment-level import function; this
    review does not claim to have reanalysed transport kinetics, full Results or raw
    cryo-EM data.
  target_ids:
  - GO:0009507
  evidence_ids:
  - septin-record-chloroplast
  - septin-root21-sources-chloroplast-go
  - septin-root21-sources-doi-10.1016_j.cell.2022.10.030
  - septin-root21-sources-jin2022-author-publications
- assessment_id: septin-chloroplast-graph
  area: graph
  topic: Nonmechanistic topology and import relations
  outcome: supported
  summary: 'All eight graph edges were read: envelope enclosing organelle/bounding
    stroma, bilayer parthood, thylakoid stromal placement and membrane boundary, and
    TOC-TIC spanning/mediating import. GO definitions support topology; Jin supplies
    Chlamydomonas assembly scope. This does not establish every subunit, pore mechanism
    or biogenesis pathway.'
  target_ids:
  - GO:0009507
  evidence_ids:
  - septin-record-chloroplast
  - septin-root21-sources-chloroplast-go
  - septin-root21-sources-doi-10.1016_j.cell.2022.10.030
  - septin-native-graph-policy
- assessment_id: septin-chloroplast-native-limits
  area: provenance
  topic: Empty native protein inventory
  outcome: supported
  summary: Verify and causal audit exit 0, but there are zero protein_examples and
    zero GENE_OR_PROTEIN nodes. This is an empty typed inventory, not experimental
    validation of named proteins in prose or generic TOC/TIC function.
  target_ids:
  - GO:0009507
  evidence_ids:
  - septin-record-chloroplast
  - septin-native-chloroplast-verify
  - septin-native-chloroplast-causal
- assessment_id: septin-chloroplast-verdict
  area: consistency
  topic: Positive target assessment with explicit access and completeness limits
  outcome: supported
  summary: 'pass_with_limitations remains supported: exact identity, compartment topology
    and bounded Chlamydomonas import claims have positive source support. Unknown
    formation necessity, incomplete constituent enumeration and abstract-level Jin
    access remain explicit. Original review has no request_curation finding for this
    target; open descriptive TODOs are not automatically converted into a defect.'
  target_ids:
  - GO:0009507
  evidence_ids:
  - septin-record-chloroplast
  - septin-original-chloroplast
  - septin-root21-sources-chloroplast-go
  - septin-root21-sources-doi-10.1016_j.cell.2022.10.030
  - septin-current-source-access-receipts
- assessment_id: septin-chloroplast_envelope-identity
  area: identity
  topic: Exact organelle/envelope identity, parentage and parthood
  outcome: supported
  summary: GO:0009941 denotes the double-bilayer envelope including intermembrane
    space, with GO:0009526 as is-a parent and GO:0009507 as containing organelle.
    It is distinct from either single membrane or either adjoining space.
  target_ids:
  - GO:0009941
  evidence_ids:
  - septin-record-chloroplast_envelope
  - septin-root21-sources-envelope-go
  - septin-root21-sources-ancestors-0009941
  - septin-context-chloroplast_inner_membrane
  - septin-context-chloroplast_intermembrane_space
- assessment_id: septin-chloroplast_envelope-taxa
  area: scope
  topic: Taxonomic identities, prevalence qualification and experimental organism
  outcome: supported
  summary: ENA verifies Viridiplantae and Chlamydomonas reinhardtii; Keeling secondary
    body supports primary-plastid green-algal/plant context. COMMON is qualified to
    photosynthetic members, not all Viridiplantae. The Jin architecture is explicitly
    Chlamydomonas and is not universalized to every plastid.
  target_ids:
  - GO:0009941
  evidence_ids:
  - septin-record-chloroplast_envelope
  - septin-root21-sources-NCBITaxon-33090
  - septin-root21-sources-NCBITaxon-3055
  - septin-root21-sources-keeling2010-pmc
  - septin-root21-sources-doi-10.1016_j.cell.2022.10.030
- assessment_id: septin-chloroplast_envelope-components
  area: grounding
  topic: Membrane and import-complex boundaries
  outcome: supported
  summary: Separate Toc and Tic complexes have exact GO identities and outer/inner-envelope
    placement. They are represented as complexes/STRUCTURE nodes, without pretending
    that one individual protein is equivalent to the complete assembly.
  target_ids:
  - GO:0009941
  evidence_ids:
  - septin-record-chloroplast_envelope
  - septin-root21-sources-envelope-go
  - septin-root21-sources-GO0061927
  - septin-root21-sources-doi-10.1016_j.cell.2022.10.030
- assessment_id: septin-chloroplast_envelope-necessity
  area: scope
  topic: Unknown formation dependencies
  outcome: unknown
  summary: Component necessity remains UNKNOWN. Ontological identity, proteome localization
    and a resolved import assembly do not by themselves establish whether removal
    of each constituent prevents formation of this complete maintained structure.
    No formation-dependency claim is added.
  target_ids:
  - GO:0009941
  evidence_ids:
  - septin-record-chloroplast_envelope
  - septin-native-curation-policy
  - septin-root21-sources-doi-10.1016_j.cell.2022.10.030
- assessment_id: septin-chloroplast_envelope-import
  area: evidence
  topic: Chlamydomonas envelope-spanning import architecture
  outcome: supported
  summary: Jin primary abstract and author-hosted abstract support the 14-component
    envelope-spanning TOC-TIC assembly, with a potential Tic20/YlmG inner route and
    intermembrane scaffold. The record states compartment-level import function; this
    review does not claim to have reanalysed transport kinetics, full Results or raw
    cryo-EM data.
  target_ids:
  - GO:0009941
  evidence_ids:
  - septin-record-chloroplast_envelope
  - septin-root21-sources-envelope-go
  - septin-root21-sources-doi-10.1016_j.cell.2022.10.030
  - septin-root21-sources-jin2022-author-publications
- assessment_id: septin-chloroplast_envelope-graph
  area: graph
  topic: Nonmechanistic topology and import relations
  outcome: supported
  summary: 'All ten graph edges were read: envelope/organellar and space boundaries,
    bilayer parthood, Toc/Tic membrane placement, coupling and compartment-level precursor
    routing. GO definitions support topology; Jin supplies Chlamydomonas assembly
    scope. This does not establish every subunit, pore mechanism or biogenesis pathway.'
  target_ids:
  - GO:0009941
  evidence_ids:
  - septin-record-chloroplast_envelope
  - septin-root21-sources-envelope-go
  - septin-root21-sources-doi-10.1016_j.cell.2022.10.030
  - septin-native-graph-policy
- assessment_id: septin-chloroplast_envelope-native-limits
  area: provenance
  topic: Empty native protein inventory
  outcome: supported
  summary: Verify and causal audit exit 0, but there are zero protein_examples and
    zero GENE_OR_PROTEIN nodes. This is an empty typed inventory, not experimental
    validation of named proteins in prose or generic TOC/TIC function.
  target_ids:
  - GO:0009941
  evidence_ids:
  - septin-record-chloroplast_envelope
  - septin-native-chloroplast_envelope-verify
  - septin-native-chloroplast_envelope-causal
- assessment_id: septin-chloroplast_envelope-verdict
  area: consistency
  topic: Positive target assessment with explicit access and completeness limits
  outcome: supported
  summary: 'pass_with_limitations remains supported: exact identity, compartment topology
    and bounded Chlamydomonas import claims have positive source support. Unknown
    formation necessity, incomplete constituent enumeration and abstract-level Jin
    access remain explicit. Original review has no request_curation finding for this
    target; open descriptive TODOs are not automatically converted into a defect.'
  target_ids:
  - GO:0009941
  evidence_ids:
  - septin-record-chloroplast_envelope
  - septin-original-chloroplast_envelope
  - septin-root21-sources-envelope-go
  - septin-root21-sources-doi-10.1016_j.cell.2022.10.030
  - septin-current-source-access-receipts
- assessment_id: septin-chloroplast-photosynthesis
  area: evidence
  topic: Photosynthesis and comparative chloroplast proteome
  outcome: supported
  summary: GO supports the photosynthesis process identity. Terashima secondary review
    complete abstract supports the Chlamydomonas chloroplast proteome/metabolic comparison
    and photosynthetic context. The nominal PDF response is challenge HTML, so the
    current review does not claim new full-body inspection or exhaustive localization
    coverage.
  target_ids:
  - GO:0009507
  evidence_ids:
  - septin-record-chloroplast
  - septin-root21-sources-chloroplast-go
  - septin-root21-sources-doi-10.1007_s00294-011-0339-1
  - septin-root21-sources-terashima2011-pdf
- assessment_id: current-input-comparison
  area: provenance
  topic: Complete frozen-input comparison and bounded refresh
  outcome: supported
  summary: 2 of ten original target hashes differ from current main. The changed content
    is substantively reassessed in the target-specific assessments; original observations
    remain historical and unchanged. All current target and used context bytes are
    frozen.
  target_ids:
  - GO:0160211
  - GO:0005776
  - GO:0034423
  - GO:0000421
  - GO:0030075
  - GO:0045009
  - GO:0009507
  - GO:0009941
  - GO:0009706
  - GO:0031972
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
- finding_id: plaque-t4-F1
  issue_key: bacterial_thylakoid-experimental-organism-mismatch
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: The cited primary thylakoid studies used Synechococcus PCC7942, not Synechocystis
    PCC6803
  description: Huokko2021 explicitly performs light-regulated thylakoid biogenesis
    experiments in Synechococcus elongatus PCC7942, whereas canonical_examples[0]
    assigns that experiment to tax1148 Synechocystis PCC6803. Casella2017 likewise
    performs its native membrane organization and mobility experiments in PCC7942,
    but four maintained component/graph source notes call the assayed organism Synechocystis.
    Both papers discuss earlier Synechocystis work, which is not a substitute for
    their own Methods. Reconcile the exemplar taxon, label, note and reference together,
    and correct the repeated Casella organism attributions. The evidence does not
    imply that Synechocystis lacks thylakoids.
  target_ids:
  - GO:0030075
  field_paths:
  - canonical_examples[0]
  - components[0].evidence[1].notes
  - components[3].evidence[1].notes
  - causal_graphs[0].edges[2].evidence[0].notes
  - causal_graphs[0].edges[3].evidence[0].notes
  evidence_ids:
  - plaque-current-4
  - plaque-thylakoid-agent-jats-PMC5683893
  - plaque-thylakoid-agent-jats-PMC8190092
  - plaque-thylakoid-agent-tax-1117
  - plaque-thylakoid-agent-tax-1148
  - plaque-thylakoid-agent-tax-1140
  normalization_reason: Major because the only canonical experimental example and
    repeated source-specific localization claims transfer evidence between distinct
    genera and strains; the general thylakoid identity remains correct.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/bacterial_thylakoid.yaml
    role: maintained scientific record
  native_severity: major
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T110749Z-bacterial-thylakoid-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2655
- finding_id: micro-F1
  issue_key: chitosome-exact-membrane-grounding
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Ground the chitosome membrane to its exact active GO term
  description: The current component remains REVIEWED_LABEL_ONLY and the open grounding
    discussion says GO has no exact chitosome-membrane child. Native GO0045009 explicitly
    lists GO0030661 part_of, and native GO0030661 is chitosome membrane, defined as
    the lipid bilayer surrounding a chitosome. This is an exact match to the existing
    constituent, not a new optional inventory row. Ground the membrane component and
    update the active discussion accordingly while preserving historical curation
    notes and the separately unresolved fungal protein-cohort question.
  target_ids:
  - GO:0045009
  field_paths:
  - components[0].grounding_status
  - components[0].grounding_notes
  - components[0].grounding
  - discussions[0].prompt
  - discussions[0].rationale
  evidence_ids:
  - micro-record-chitosome
  - micro-review-policy
  - micro-chito-go
  - micro-chito-go-parts
  - micro-prior-chitosome
  normalization_reason: 'Minor: the membrane identity and scientific role are already
    correct; the concrete defect is avoidable missing exact grounding and a stale
    open no-term rationale.'
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/chitosome.yaml
    role: maintained scientific record
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T110752Z-chitosome-audit
    finding_id: F1
  native_severity: minor
  rule_id: docs/CURATION.md:Identifiers; docs/record-reviews.md:Verdict And Severity
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2656
- finding_id: septin-S2358-F1
  issue_key: apicoplast-membrane-selma-er-paralog-xref
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: The SELMA node links to an ER Der1 paralog
  description: The membrane SELMA/ERAD-derived import-machinery node retains B9PY98.
    Native UniProt/ENA cross-references identify Der1ER1 FJ976521/ACU32856.1. The
    author primary-study Methods and Table3.1 separately map apicoplast Der1Ap FJ976520/ACU32855.1,
    now C9WWW6. Shared family and successful accession resolution do not make this
    ER paralog an appropriate apicoplast-machinery xref.
  target_ids:
  - GO:0160211
  field_paths:
  - causal_graphs#apicoplast_membrane_envelope.nodes#selma_import_system.xrefs
  evidence_ids:
  - septin-record-apicoplast_membrane
  - septin-original-apicoplast_membrane
  - septin-apicoplast-agent-B9PY98
  - septin-apicoplast-agent-C9WWW6
  - septin-apicoplast-agent-ena-FJ976521
  - septin-apicoplast-agent-ena-FJ976520
  - septin-agrawal2011-thesis
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/apicoplast_membrane.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: major
  normalization_reason: Major because an explicit graph protein reference identifies
    a different cellular paralog from the represented import machinery.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T110736Z-apicoplast-membrane-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2654
actions:
- action_id: plaque-t4-A1
  finding_ids:
  - plaque-t4-F1
  target_ids:
  - GO:0030075
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/bacterial_thylakoid.yaml
    role: maintained scientific record
  description: Reconcile the canonical taxon, label, note and source to the actual
    PCC7942 experiment, or supply genuinely PCC6803-specific evidence; correct the
    four repeated Casella organism attributions together. Preserve general bacterial-thylakoid
    identity and do not infer PCC6803 lacks thylakoids.
  acceptance_checks:
  - Preserve stable issue key and exact previous occurrence.
  - Separately authorized guarded record curation and append-only history; this review
    PR makes no scientific record changes.
  - Recheck every cited experimental organism and native taxonomy, then native schema/strict,
    labels, references, history and QC after later curation.
- action_id: micro-A1
  finding_ids:
  - micro-F1
  target_ids:
  - GO:0045009
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/chitosome.yaml
    role: maintained scientific record
  description: In separately authorized record curation, ground the existing chitosome
    membrane constituent to active GO:0030661 and update only the false membrane portion
    of the active grounding discussion. Preserve history and the independently unresolved
    fungal cargo-class scope.
  acceptance_checks:
  - The existing membrane component uses exact GO:0030661 with source-backed label
    correspondence and grounding status.
  - The active discussion no longer asserts that an exact chitosome membrane term
    does not exist; historical curation text is preserved.
  - Do not substitute the broad chitin-synthase family for a demonstrated universal
    fungal cargo cohort or infer constituent necessity from identity.
  - Use the guarded writer and curation/history protocol with applicable native checks
    in a separate record-curation PR.
- action_id: septin-S2358-C1
  finding_ids:
  - septin-S2358-F1
  target_ids:
  - GO:0160211
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/apicoplast_membrane.yaml
    role: maintained scientific record
  description: In a separate record-curation change, remove the ER-paralog B9PY98
    from the membrane SELMA node or replace it with independently verified apicoplast
    Der1Ap/C9WWW6 and its primary-source sequence bridge. Preserve unreviewed status,
    exact taxon, missing native gene-name field and bounded representative scope;
    do not claim that the whole complex equals one protein.
  acceptance_checks:
  - Exact graph xrefs identify the represented apicoplast actors rather than ER paralogs.
  - Any C9WWW6 replacement retains FJ976520/ACU32855.1 primary-source mapping and
    exact taxon/status metadata.
  - Run focused schema, strict CURIE and native UniProt checks.
limitations:
- 'Bacterial thylakoid, chloroplast inner membrane and intermembrane space independent
  subreview: All three target bytes are unchanged from the original reviews. Their
  source-grounded reassessment does not rewrite originals or record history.'
- 'Bacterial thylakoid, chloroplast inner membrane and intermembrane space independent
  subreview: Casella2017 and Huokko2021 are inspected primary body text/selected captions
  at the explicit locators; figure pixels, supplementary raw data and exhaustive perturbation
  literature were not independently audited. AFM b6f assignment remains tentative.'
- 'Bacterial thylakoid, chloroplast inner membrane and intermembrane space independent
  subreview: Perez2024 is secondary synthesis accessed through browser-returned indexed
  official publisher body; native landing/delivery attempts returned403. Only named
  returned sections are treated as read; no complete native-body retrieval is claimed.'
- 'Bacterial thylakoid, chloroplast inner membrane and intermembrane space independent
  subreview: Keeling2010 selected secondary HTML body is accessible through PMC; failed
  JATS/S3/PDF/BioC routes do not negate that bounded fallback. Jin2022 biology is
  primary abstract only;7VCF metadata verifies linked species, not an experimental
  strain or complete paper inspection.'
- 'Bacterial thylakoid, chloroplast inner membrane and intermembrane space independent
  subreview: Ontology-derived plasma-membrane attachment wording is not evidence of
  obligatory physical fusion or a universal cyanobacterial biogenesis mechanism. Individual
  assembly necessity remains unknown; collective bilayer identity is distinct.'
- 'Bacterial thylakoid, chloroplast inner membrane and intermembrane space independent
  subreview: Historical adapter runner failure occurred00:49Z, not during this subreview.
  Fresh source endpoints are independently accessed fallback, not a new runner success.
  Catalogue coverage is exact organism/dataset context.'
- 'Bacterial thylakoid, chloroplast inner membrane and intermembrane space independent
  subreview: Matched elprecise300 is PCC7942 experimental-source context, not maintained
  PCC6803 or chloroplast evidence. Four representative gene queries and two module
  summaries/member lists are bounded computational checks; below-threshold results
  do not show absence. Generated module prose is excluded.'
- 'Bacterial thylakoid, chloroplast inner membrane and intermembrane space independent
  subreview: Sparse inner-membrane/IMS inventories do not require invented proteins.
  TOC–TIC prose nevertheless triggers a coverage assessment. Empty native protein
  inventories pass validity checks without proving membership or essentiality.'
- 'Bacterial thylakoid, chloroplast inner membrane and intermembrane space independent
  subreview: All three targets declare no images; no target pixel assessment is claimed.
  Neighbor chloroplast/envelope records are used for boundaries only. Root owns corpus
  gates, issue deduplication/publication, repository writes and merge decisions.'
- 'Autophagosome, lumen, membrane and chitosome independent subreview: Assigned scope
  only: four autophagy/chitosome records and their original review pairs. No whole-category
  finding resolution or scientific assessment of the other six targets is made by
  this report.'
- 'Autophagosome, lumen, membrane and chitosome independent subreview: Source-specific
  current access: Takeshige1992 is OCR JATS abstract/selected body/Discussion; Suzuki2001
  publisher selected Results and complete Discussion/Methods; Santos1997 selected
  claim-bearing primary Methods/Results/Discussion; Ziman1998 primary text narratives.
  No primary figure pixels, raw data or supplements were inspected.'
- 'Autophagosome, lumen, membrane and chitosome independent subreview: Leal-Morales1988,
  Ichimura2000 and three CHS3 annotation PMIDs were assessed from exact primary abstracts
  only. Xie2007 was assessed from its secondary review abstract only. Bartnicki2006
  was read as secondary PDF text through Conclusion, not an independent primary experiment.'
- 'Autophagosome, lumen, membrane and chitosome independent subreview: Historical
  original-review evidence may have wider or narrower access than this fresh pass.
  Its dates and access tiers are not rewritten. Current source evidence rows retain
  their actual09:33Z fetch times, even when interpreted later.'
- 'Autophagosome, lumen, membrane and chitosome independent subreview: The chitosome
  new delivery edge is accepted within its explicit NONMECHANISTIC scope; Chs3 transport
  experiments do not demonstrate activation of every fungal isoenzyme, sufficient
  activation by delivery alone, universal Chs6 dependence or a complete biogenesis
  route.'
- 'Autophagosome, lumen, membrane and chitosome independent subreview: InterPro broad
  family membership of the two examples is not universal fungal cargo coverage. Native
  protein commands are empty-scope for all three autophagy records and cover only
  the two declared chitosome examples/one graph protein node.'
- 'Autophagosome, lumen, membrane and chitosome independent subreview: iModulonDB
  no-match concerns only the complete dataset catalogue fetched2026-11-03T09:33:07Z
  and these fungal taxa. The retained runner failure was00:49Z, not a new invocation.
  No unsupported matched-organism gene or module search was invented.'
- 'Autophagosome, lumen, membrane and chitosome independent subreview: Initial sandbox
  DNS failures were preserved under initial-dns-unavailable; permitted public-network
  retrieval then succeeded. Two guessed JATS routes returned404, while actual publisher/PMC
  alternatives supplied the documented primary text. These access failures are not
  successful source checks.'
- 'Autophagosome, lumen, membrane and chitosome independent subreview: Root owns current
  whole-corpus QC, identifier/label/trait checks, issue deduplication, issue publication
  and final integration. This independent report inspected its eight actual focused
  native protein receipts and original-bundle validation; it does not claim to have
  rerun global gates.'
- 'Apicoplast membrane, chloroplast and envelope independent subreview: Public apicoplast
  source snapshots are explicitly reused with their original 08:55Z or 09:00Z access
  timestamps and verified hashes; the source evidence is not represented as newly
  fetched. No prior immutable review bundle beyond these assigned original reviews
  was used.'
- 'Apicoplast membrane, chloroplast and envelope independent subreview: Jin2022 current
  access is complete native indexed abstract and exact author-laboratory abstract
  entry; publisher body request returned403. No complete Results, supplementary material,
  raw cryo-EM data or experimental images were audited. The potential inner route
  remains source-model scope.'
- 'Apicoplast membrane, chloroplast and envelope independent subreview: Terashima2011
  current access is complete native abstract/bibliographic metadata. Its nominal PDF
  route returned HTML challenge, not a PDF. Keeling2010 was genuinely read at fresh
  PMC Abstract/section1 body scope and is a secondary review.'
- 'Apicoplast membrane, chloroplast and envelope independent subreview: Tic20/Der1
  primary support uses the institutional author dissertation reprints and exact deposited
  sequences; prior PMC challenge responses are not represented as successful full-body
  reads. TgTic20 import impairment is temporally resolved and does not prove direct
  pore action.'
- 'Apicoplast membrane, chloroplast and envelope independent subreview: Kalanon2009
  inspected Methods/selected Results/Table1/Fig4 caption; O97275/Der1-2 is not assigned
  the full-length Der1-1 experiments. No image pixels were reanalysed.'
- 'Apicoplast membrane, chloroplast and envelope independent subreview: No claim of
  exhaustive constituent inventory, every import-machine class grounding, quantitative
  lipid composition or universal organelle formation dependency. Component necessity
  remains UNKNOWN in the chloroplast targets.'
- 'Apicoplast membrane, chloroplast and envelope independent subreview: The official
  catalogue coverage assessment is bounded to its current complete response. No covered
  organism matches these targets; this is not biological absence. Historical runner
  failure at00:49Z is not a fresh run and is distinct from successful fresh source
  fallback.'
- 'Apicoplast membrane, chloroplast and envelope independent subreview: Native checks
  validate exact declared identifiers and typed inventory only: two membrane UNANCHORED_WITH_UNIPROT
  nodes and empty chloroplast/envelope protein inventories. They do not resolve the
  wrong-paralog scientific finding.'
- 'Apicoplast membrane, chloroplast and envelope independent subreview: The additional
  frozen apicoplast and inner-membrane/intermembrane-space records are boundary/identity
  context only. No whole-organelle or multi-target historical finding is marked resolved.'
- 'Apicoplast membrane, chloroplast and envelope independent subreview: Root owns
  global QC/CI, issue deduplication/publication and final repository checks; this
  report performs no repository or GitHub mutation.'
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
- 'Issue #2652 tracks the autophagosome function grounding and chitosome cargo-delivery
  edge refreshes. Scientific record curation remains separately tracked and open.
  Existing validator #2514 remains open.'
- 'Issue #2653 tracks three omitted applicability assessments and six unsupported
  expression-only exclusions. The sparse autophagosome lumen is a genuine topology
  exclusion.'
- Source commit e721920f30c72a6c35cecb9913c6780e18a460ed is retained by tag review-base/pr2358-current-record-followup-20261103.
- CLAUDE.md is an alias of AGENTS.md; canonical regular AGENTS.md bytes are frozen.
- All used local context was frozen before assessment, including native configuration,
  graph/protein policies and verifier source. The whole-apicoplast neighbor is context
  only, not an additional target or a disposition of its findings.
- Fresh and reused public-source snapshots retain actual access dates and inspection
  tiers. Native authority identity does not independently establish localization,
  mechanistic action or assembly necessity.
- Native checks with empty protein inventories or zero GENE_OR_PROTEIN nodes do not
  validate molecules appearing only in narrative prose.
- The autophagosome macroautophagy identifier and chitosome cargo delivery are reassessed
  within their stated scopes. Chs3 transport evidence does not establish universal
  isoenzyme activation.
- All three original scientific findings remain open for separate record curation;
  no scientific finding is terminally resolved.
- 'Two major findings (apicoplast membrane Der1 paralog and bacterial thylakoid organism
  attribution) remain open as #2654 and #2655. The minor chitosome membrane grounding
  finding remains open as #2656. The seven targets without scientific findings retain
  qualified positive assessments; no record is edited.'
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T110736Z-apicoplast-membrane-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T110741Z-autophagosome-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T110744Z-autophagosome-lumen-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T110747Z-autophagosome-membrane-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T110749Z-bacterial-thylakoid-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T110752Z-chitosome-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T110755Z-chloroplast-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T110757Z-chloroplast-envelope-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T110759Z-chloroplast-inner-membrane-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T110802Z-chloroplast-intermembrane-space-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
links:
- https://github.com/CultureBotAI/CellStructureMech/pull/2358
- https://github.com/CultureBotAI/CellStructureMech/issues/2514
- https://github.com/CultureBotAI/CellStructureMech/issues/2652
- https://github.com/CultureBotAI/CellStructureMech/issues/2653
- https://github.com/CultureBotAI/CellStructureMech/issues/2654
- https://github.com/CultureBotAI/CellStructureMech/issues/2655
- https://github.com/CultureBotAI/CellStructureMech/issues/2656
```
