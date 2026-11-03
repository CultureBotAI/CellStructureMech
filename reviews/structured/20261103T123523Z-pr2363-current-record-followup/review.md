# PR 2363: current-input review of ten records and adversarial follow-up

- Review: 20261103T123523Z-pr2363-current-record-followup
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-11-03T12:26:56.169916Z
- Finished UTC: 2026-11-03T12:35:23Z
- Reviewer: Codex root synthesis with three independent read-only adversarial reviewers (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Current-input reassessment of all ten records in PR2363. One stale diazoplast review is substantively refreshed and nine structured-source applicability assessments are corrected. Two inherited minor scientific findings remain open for separate curation; no records are edited.

## Scope And Provenance

Exact ten-record PR cohort reassessed against current main a961bb84a278a52cb08f9e5494240141ca8b1a76. Changed inputs are substantively reassessed. Scientific records remain unchanged.

Selection: Complete cohort of ten maintained records reviewed in original PR head 2282587034c1b0aa06edc6feeb558aca9e46f546.
Coverage: full; 10 reviewed / 10 in the declared population.
Source: working_tree at Git base cd5be11ad13304d75404a51d097635022d1bd091.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0009843 | data/structures/membrane_organelle/cyanelle_thylakoid.yaml | maintained | cyanelle thylakoid |
| GO:0033114 | data/structures/membrane_organelle/cyanelle_thylakoid_lumen.yaml | maintained | cyanelle thylakoid lumen |
| GO:0033115 | data/structures/membrane_organelle/cyanelle_thylakoid_membrane.yaml | maintained | cyanelle thylakoid membrane |
| GO:0031410 | data/structures/membrane_organelle/cytoplasmic_vesicle.yaml | maintained | cytoplasmic vesicle |
| GO:0060205 | data/structures/membrane_organelle/cytoplasmic_vesicle_lumen.yaml | maintained | cytoplasmic vesicle lumen |
| GO:0030659 | data/structures/membrane_organelle/cytoplasmic_vesicle_membrane.yaml | maintained | cytoplasmic vesicle membrane |
| cellstructuremech:diazoplast | data/structures/membrane_organelle/diazoplast.yaml | maintained | diazoplast |
| GO:0005769 | data/structures/membrane_organelle/early_endosome.yaml | maintained | early endosome |
| GO:0031905 | data/structures/membrane_organelle/early_endosome_lumen.yaml | maintained | early endosome lumen |
| GO:0031901 | data/structures/membrane_organelle/early_endosome_membrane.yaml | maintained | early endosome membrane |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full native QC | passed | True | GO:0009843, GO:0033114, GO:0033115, GO:0031410, GO:0060205, GO:0030659, cellstructuremech:diazoplast, GO:0005769, GO:0031905, GO:0031901 | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| Native label correspondence | passed | True | GO:0009843, GO:0033114, GO:0033115, GO:0031410, GO:0060205, GO:0030659, cellstructuremech:diazoplast, GO:0005769, GO:0031905, GO:0031901 | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| TraitMech references | passed | True | GO:0009843, GO:0033114, GO:0033115, GO:0031410, GO:0060205, GO:0030659, cellstructuremech:diazoplast, GO:0005769, GO:0031905, GO:0031901 | Native TraitMech link check passed. |
| Pinned governed files | passed | True | GO:0009843, GO:0033114, GO:0033115, GO:0031410, GO:0060205, GO:0030659, cellstructuremech:diazoplast, GO:0005769, GO:0031905, GO:0031901 | Pinned governed files match; native vendored check passed. |
| Native identifier resolver | passed | True | GO:0009843, GO:0033114, GO:0033115, GO:0031410, GO:0060205, GO:0030659, cellstructuremech:diazoplast, GO:0005769, GO:0031905, GO:0031901 | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| validate GO:0009843 | passed | True | GO:0009843 | Documented focused command passed. |
| validate-strict GO:0009843 | passed | True | GO:0009843 | Documented focused command passed. |
| validate GO:0033114 | passed | True | GO:0033114 | Documented focused command passed. |
| validate-strict GO:0033114 | passed | True | GO:0033114 | Documented focused command passed. |
| validate GO:0033115 | passed | True | GO:0033115 | Documented focused command passed. |
| validate-strict GO:0033115 | passed | True | GO:0033115 | Documented focused command passed. |
| validate GO:0031410 | passed | True | GO:0031410 | Documented focused command passed. |
| validate-strict GO:0031410 | passed | True | GO:0031410 | Documented focused command passed. |
| validate GO:0060205 | passed | True | GO:0060205 | Documented focused command passed. |
| validate-strict GO:0060205 | passed | True | GO:0060205 | Documented focused command passed. |
| validate GO:0030659 | passed | True | GO:0030659 | Documented focused command passed. |
| validate-strict GO:0030659 | passed | True | GO:0030659 | Documented focused command passed. |
| validate cellstructuremech:diazoplast | passed | True | cellstructuremech:diazoplast | Documented focused command passed. |
| validate-strict cellstructuremech:diazoplast | passed | True | cellstructuremech:diazoplast | Documented focused command passed. |
| validate GO:0005769 | passed | True | GO:0005769 | Documented focused command passed. |
| validate-strict GO:0005769 | passed | True | GO:0005769 | Documented focused command passed. |
| validate GO:0031905 | passed | True | GO:0031905 | Documented focused command passed. |
| validate-strict GO:0031905 | passed | True | GO:0031905 | Documented focused command passed. |
| validate GO:0031901 | passed | True | GO:0031901 | Documented focused command passed. |
| validate-strict GO:0031901 | passed | True | GO:0031901 | Documented focused command passed. |
| Supplemental bounded PMID authority checks | passed | True | GO:0009843, GO:0033114, GO:0033115, GO:0031410, GO:0060205, GO:0030659, cellstructuremech:diazoplast, GO:0005769, GO:0031905, GO:0031901 | 909 PMIDs all OK in bounded native requests; full-command limitations remain separate. |
| Official structured-source applicability and covered-dataset cross-checks | passed | False | GO:0009843, GO:0033114, GO:0033115, GO:0031410, GO:0060205, GO:0030659, cellstructuremech:diazoplast, GO:0005769, GO:0031905, GO:0031901 | Nine unsupported applicability exclusions are corrected: whole cyanelle thylakoid and membrane light-reaction context, the cytoplasmic-vesicle trio Cvt/early-secretory context, diazoplast nitrogen fixation/molecular examples, and the early-endosome trio endocytic cargo-routing context. Cyanelle thylakoid lumen remains a genuine topology-only exclusion with proton transport and lumen protein assertions withheld. Complete official catalogue coverage has no matching relevant Cyanophora, yeast, Epithemia, Crocosphaera, Azotobacter or Trypanosoma dataset. No unrelated organism proxy or downstream query substitutes for noncoverage. Resource noncoverage is not biological absence; the historical runner failure is not a fresh invocation. |
| Independent claim-level source review | passed | True | GO:0009843, GO:0033114, GO:0033115, GO:0031410, GO:0060205, GO:0030659, cellstructuremech:diazoplast, GO:0005769, GO:0031905, GO:0031901 | Three read-only reviewers covered the complete ten-record cohort, including changed inputs, with explicit scientific findings and source-access limits. Final artifact/head acceptance occurs after saving. |
| Retained historical adapter runner availability | unavailable | False | GO:0009843, GO:0033115, GO:0031410, GO:0060205, GO:0030659, cellstructuremech:diazoplast, GO:0005769, GO:0031905, GO:0031901 | Historical 00:49Z invocation unavailable due to OS access restriction. Official catalogue source fallback was inspected separately; no current invocation or successful adapter execution is claimed. The actual historical exit code 1 is retained in the evidence receipt, since the native unavailable-check model has no execution exit-code field. |
| Native cyanelle thylakoid UniProt verify check | passed | True | GO:0009843 | Read-only native command returned zero. Represented protein inventory and typed GENE_OR_PROTEIN graph coverage are empty. This does not validate narrative molecules, pathways or source scope. |
| Native cyanelle thylakoid UniProt causal check | passed | True | GO:0009843 | Read-only native command returned zero. Represented protein inventory and typed GENE_OR_PROTEIN graph coverage are empty. This does not validate narrative molecules, pathways or source scope. |
| Native cyanelle thylakoid lumen UniProt verify check | passed | True | GO:0033114 | Read-only native command returned zero. Represented protein inventory and typed GENE_OR_PROTEIN graph coverage are empty. This does not validate narrative molecules, pathways or source scope. |
| Native cyanelle thylakoid lumen UniProt causal check | passed | True | GO:0033114 | Read-only native command returned zero. Represented protein inventory and typed GENE_OR_PROTEIN graph coverage are empty. This does not validate narrative molecules, pathways or source scope. |
| Native cyanelle thylakoid membrane UniProt verify check | passed | True | GO:0033115 | Read-only native command returned zero. Represented protein inventory and typed GENE_OR_PROTEIN graph coverage are empty. This does not validate narrative molecules, pathways or source scope. |
| Native cyanelle thylakoid membrane UniProt causal check | passed | True | GO:0033115 | Read-only native command returned zero. Represented protein inventory and typed GENE_OR_PROTEIN graph coverage are empty. This does not validate narrative molecules, pathways or source scope. |
| Native cytoplasmic vesicle UniProt verify check | passed | True | GO:0031410 | Read-only native command returned zero. Represented protein inventory and typed GENE_OR_PROTEIN graph coverage are empty. This does not validate narrative molecules, pathways or source scope. |
| Native cytoplasmic vesicle UniProt causal check | passed | True | GO:0031410 | Read-only native command returned zero. Represented protein inventory and typed GENE_OR_PROTEIN graph coverage are empty. This does not validate narrative molecules, pathways or source scope. |
| Native cytoplasmic vesicle lumen UniProt verify check | passed | True | GO:0060205 | Read-only native command returned zero. Represented protein inventory and typed GENE_OR_PROTEIN graph coverage are empty. This does not validate narrative molecules, pathways or source scope. |
| Native cytoplasmic vesicle lumen UniProt causal check | passed | True | GO:0060205 | Read-only native command returned zero. Represented protein inventory and typed GENE_OR_PROTEIN graph coverage are empty. This does not validate narrative molecules, pathways or source scope. |
| Native cytoplasmic vesicle membrane UniProt verify check | passed | True | GO:0030659 | Read-only native command returned zero. Represented protein inventory and typed GENE_OR_PROTEIN graph coverage are empty. This does not validate narrative molecules, pathways or source scope. |
| Native cytoplasmic vesicle membrane UniProt causal check | passed | True | GO:0030659 | Read-only native command returned zero. Represented protein inventory and typed GENE_OR_PROTEIN graph coverage are empty. This does not validate narrative molecules, pathways or source scope. |
| Native diazoplast UniProt verify check | passed | True | cellstructuremech:diazoplast | Read-only native command returned zero. Three represented Azotobacter accessions are verified; typed GENE_OR_PROTEIN graph coverage is zero after complex retyping. Identity does not establish the proteins as Epithemia diazoplast members. |
| Native diazoplast UniProt causal check | passed | True | cellstructuremech:diazoplast | Read-only native command returned zero. Three represented Azotobacter accessions are verified; typed GENE_OR_PROTEIN graph coverage is zero after complex retyping. Identity does not establish the proteins as Epithemia diazoplast members. |
| Native early endosome UniProt verify check | passed | True | GO:0005769 | Read-only native command returned zero. Represented protein inventory and typed GENE_OR_PROTEIN graph coverage are empty. This does not validate narrative molecules, pathways or source scope. |
| Native early endosome UniProt causal check | passed | True | GO:0005769 | Read-only native command returned zero. Represented protein inventory and typed GENE_OR_PROTEIN graph coverage are empty. This does not validate narrative molecules, pathways or source scope. |
| Native early endosome lumen UniProt verify check | passed | True | GO:0031905 | Read-only native command returned zero. Represented protein inventory and typed GENE_OR_PROTEIN graph coverage are empty. This does not validate narrative molecules, pathways or source scope. |
| Native early endosome lumen UniProt causal check | passed | True | GO:0031905 | Read-only native command returned zero. Represented protein inventory and typed GENE_OR_PROTEIN graph coverage are empty. This does not validate narrative molecules, pathways or source scope. |
| Native early endosome membrane UniProt verify check | passed | True | GO:0031901 | Read-only native command returned zero. Represented protein inventory and typed GENE_OR_PROTEIN graph coverage are empty. This does not validate narrative molecules, pathways or source scope. |
| Native early endosome membrane UniProt causal check | passed | True | GO:0031901 | Read-only native command returned zero. Represented protein inventory and typed GENE_OR_PROTEIN graph coverage are empty. This does not validate narrative molecules, pathways or source scope. |

## Scientific And Domain Assessments

### Native protein and graph inventories

schema: supported. Targets: GO:0009843.

Both commands pass empty represented protein inventories and zero GENE_OR_PROTEIN nodes. Mechanical checks do not certify primary-source biology or establish a complete proteome.

### Original lineage and unchanged frozen record

provenance: supported. Targets: GO:0009843.

Original validates/renders exactly and all12 historical input hashes match. Current target unchanged; no stale input needs refresh. Original findings/actions empty. Historical record issues are context only, not reclosed or recertified.

### Entire maintained record and bounded science

completeness: supported. Targets: GO:0009843.

All maintained fields, histories, discussions and graph edges read. No target images, snippets, quantitative properties or named protein examples are represented. No optional molecular inventory is fabricated. No scientific curation defect established at declared evidence tiers.

### Exact organism/class and qualitative occurrence

scope: supported. Targets: GO:0009843.

ENA verifies C.paradoxa2762 and Glaucocystophyceae38254 including Glaucophyta synonym. COMMON is qualitative defining anatomy, not numerical sampled prevalence. Giddings observations are specifically C.paradoxa UTEX LB555 under stated conditions; no strain interchange or universal composition is inferred.

### Primary ultrastructure and photosynthetic context

evidence: supported. Targets: GO:0009843.

Independently viewed Giddings pages409–413 and416–418, including text, plots, gels, microscopy and the explicitly tentative Fig19 model. These support cyanelle thylakoid architecture in C.paradoxa. Precise PSI localization is expressly unresolved in the paper and is not asserted by this target. No complete-paper, raw-data or necessity reanalysis claimed.

### Native protein and graph inventories

schema: supported. Targets: GO:0033114.

Both commands pass empty represented protein inventories and zero GENE_OR_PROTEIN nodes. Mechanical checks do not certify primary-source biology or establish a complete proteome.

### Original lineage and unchanged frozen record

provenance: supported. Targets: GO:0033114.

Original validates/renders exactly and all12 historical input hashes match. Current target unchanged; no stale input needs refresh. Original findings/actions empty. Historical record issues are context only, not reclosed or recertified.

### Entire maintained record and bounded science

completeness: supported. Targets: GO:0033114.

All maintained fields, histories, discussions and graph edges read. No target images, snippets, quantitative properties or named protein examples are represented. No optional molecular inventory is fabricated. No scientific curation defect established at declared evidence tiers.

### Exact organism/class and qualitative occurrence

scope: supported. Targets: GO:0033114.

ENA verifies C.paradoxa2762 and Glaucocystophyceae38254 including Glaucophyta synonym. COMMON is qualitative defining anatomy, not numerical sampled prevalence. Giddings observations are specifically C.paradoxa UTEX LB555 under stated conditions; no strain interchange or universal composition is inferred.

### Primary ultrastructure and photosynthetic context

evidence: supported. Targets: GO:0033114.

Independently viewed Giddings pages409–413 and416–418, including text, plots, gels, microscopy and the explicitly tentative Fig19 model. These support cyanelle thylakoid architecture in C.paradoxa. Precise PSI localization is expressly unresolved in the paper and is not asserted by this target. No complete-paper, raw-data or necessity reanalysis claimed.

### Native protein and graph inventories

schema: supported. Targets: GO:0033115.

Both commands pass empty represented protein inventories and zero GENE_OR_PROTEIN nodes. Mechanical checks do not certify primary-source biology or establish a complete proteome.

### Original lineage and unchanged frozen record

provenance: supported. Targets: GO:0033115.

Original validates/renders exactly and all12 historical input hashes match. Current target unchanged; no stale input needs refresh. Original findings/actions empty. Historical record issues are context only, not reclosed or recertified.

### Entire maintained record and bounded science

completeness: supported. Targets: GO:0033115.

All maintained fields, histories, discussions and graph edges read. No target images, snippets, quantitative properties or named protein examples are represented. No optional molecular inventory is fabricated. No scientific curation defect established at declared evidence tiers.

### Exact organism/class and qualitative occurrence

scope: supported. Targets: GO:0033115.

ENA verifies C.paradoxa2762 and Glaucocystophyceae38254 including Glaucophyta synonym. COMMON is qualitative defining anatomy, not numerical sampled prevalence. Giddings observations are specifically C.paradoxa UTEX LB555 under stated conditions; no strain interchange or universal composition is inferred.

### Primary ultrastructure and photosynthetic context

evidence: supported. Targets: GO:0033115.

Independently viewed Giddings pages409–413 and416–418, including text, plots, gels, microscopy and the explicitly tentative Fig19 model. These support cyanelle thylakoid architecture in C.paradoxa. Precise PSI localization is expressly unresolved in the paper and is not asserted by this target. No complete-paper, raw-data or necessity reanalysis claimed.

### Exact identity, parentage and compartment boundaries

identity: supported. Targets: GO:0009843.

ExactGO0009843/SL0277 represent the whole internal thylakoid unit, containing membrane and lumen and part of cyanelle. Plastid-thylakoid and broader-thylakoid parentage are valid. Local coarse physical kind deliberately covers whole thylakoids; no GO is_a organelle assertion is added.

### Exact identity, parentage and compartment boundaries

identity: supported. Targets: GO:0033114.

ExactGO0033114/SL0084 represent the lumenal volume, part of whole cyanelle thylakoid and is_a plastid thylakoid lumen. It is not the bounding bilayer, whole thylakoid or a molecular cargo inventory.

### Exact identity, parentage and compartment boundaries

identity: supported. Targets: GO:0033115.

ExactGO0033115/SL0085 represent the lipid bilayer surrounding lumen. Plastid thylakoid membrane0055035 and broader0042651 parent classes are valid. It is part of whole thylakoid, distinct from cyanelle envelope membrane.

### Constituent membrane material

grounding: supported. Targets: GO:0009843.

The membrane constituent is correctly grounded toGO0033115 as the identified structural membrane, with LIPID material type. UNKNOWN formation essentiality avoids assigning measured assembly necessity. No individual lipid/protein identity is guessed.

### Intentional lack of lumen constituents

grounding: not_applicable. Targets: GO:0033114.

The record intentionally withholds lumen-localized proteins and proton transport pending source-specific evidence. An empty component inventory is not a defect in the bounded region record. A membrane boundary is not relabeled as soluble lumen cargo.

### Collective lipid bilayer and constitutional necessity

grounding: supported. Targets: GO:0033115.

Collective lipid bilayer is defining material, not a particular chemical species. ESSENTIAL is constitutional material necessity, not evidence that one lipid/protein is required to form the compartment. REVIEWED_LABEL_ONLY and existing material-grounding TODO correctly withhold an invented accession.

### Complete descriptive topology/function graph

graph: supported. Targets: GO:0009843.

Three NONMECHANISTIC edges describe membrane bounding lumen, membrane support of light reactions and membrane parthood in whole thylakoid. Typed GO/SL topology and inspected primary architecture support them without molecular assembly claims.

### Complete descriptive topology/function graph

graph: supported. Targets: GO:0033114.

Two NONMECHANISTIC edges describe lumen parthood in whole thylakoid and enclosing membrane. They assert geometry, not proton transport, cargo processing or complete photosynthetic mechanism.

### Complete descriptive topology/function graph

graph: supported. Targets: GO:0033115.

Two NONMECHANISTIC edges describe bounding lumen and providing the membrane site for light reactions. They do not assert precise PSI distribution, measured electron flow, protein assembly or loss-of-function necessity.

### Photosynthetic light-reaction site

evidence: supported. Targets: GO:0009843.

GO0009843/SL0277 explicitly support photosynthetic cyanelle thylakoids, and Giddings pigment/ultrastructure experiments corroborate this in C.paradoxa. The function is bounded to the membrane site of light reactions, not a complete protein inventory or a claim that the old paper resolves precise PSI placement.

### Pathway-triggered structured-source applicability

scope: supported. Targets: GO:0009843.

The current target explicitly asserts photosynthetic light-reaction functionGO0019684 and a membrane-supports-light-reactions graph edge, so the original no-gene/regulator/stress/transcriptomic rationale overlooks a real pathway trigger. Actual current catalogue inspection finds no Cyanophora/glaucophyte host. No matched downstream gene/module query applies, no cyanobacterial dataset is substituted, and noncoverage does not imply biological absence. Source-scoped primary/authority fallback completes the current assessment; historical runner remains unavailable at its actual earlier time.

### Photosynthetic light-reaction site

evidence: supported. Targets: GO:0033115.

GO0009843/SL0277 explicitly support photosynthetic cyanelle thylakoids, and Giddings pigment/ultrastructure experiments corroborate this in C.paradoxa. The function is bounded to the membrane site of light reactions, not a complete protein inventory or a claim that the old paper resolves precise PSI placement.

### Pathway-triggered structured-source applicability

scope: supported. Targets: GO:0033115.

The current target explicitly asserts photosynthetic light-reaction functionGO0019684 and a membrane-supports-light-reactions graph edge, so the original no-gene/regulator/stress/transcriptomic rationale overlooks a real pathway trigger. Actual current catalogue inspection finds no Cyanophora/glaucophyte host. No matched downstream gene/module query applies, no cyanobacterial dataset is substituted, and noncoverage does not imply biological absence. Source-scoped primary/authority fallback completes the current assessment; historical runner remains unavailable at its actual earlier time.

### Genuine topology-only applicability exclusion

scope: not_applicable. Targets: GO:0033114.

Complete record is geometry and qualitative occurrence only. It explicitly withholds lumen proteins and proton transport, and does not assert a named molecular actor, regulator, pathway, stress response, trait or expression/module inference. The old N/A wording does not create a defect absent a positive trigger. Catalogue has no glaucophyte host but that is contextual, not the sole reason for genuine exclusion.

### Frozen original and current inputs; immutable pair

provenance: supported. Targets: cellstructuremech:diazoplast.

Diazoplast original input7aabee1c3f14420665958c955451705d3c7ea115003ffd94060a2f1afd40d41f changed tofd3948e827eb4a9870bc4eccb09689dd5c82f5caef443f1e319daabbf21bb038: new history and complex-node retyping substantively assessed; original F1 persists. Original native validation/render passed; no artifact, record, status or historical finding rewritten.

### Actual current native verifier coverage

schema: supported. Targets: cellstructuremech:diazoplast.

Verify checks three declared Azotobacter accession examples and any xrefs; identity pass does not establish role in a diazoplast. Causal command counts zero GENE_OR_PROTEIN nodes; this is not validation of all graph biology, narrative proteins, membership or necessity.

### Actual pathway-triggered structured-source applicability

evidence: concern. Targets: cellstructuremech:diazoplast.

Named nifH/nifD/nifK/hupL, nitrogen fixation, photosynthesis and physiological perturbation trigger applicability. Original expression-only N/A rationale is insufficient. Current bounded catalogue contains no matching organism/dataset, so no downstream module query applies. Historical runner unavailability is separately dated; absence is not biological evidence.

### PROPOSED status and bounded curation ownership

provenance: supported. Targets: cellstructuremech:diazoplast.

Review preserves PROPOSED and append-only history. Source receipts describe inspected scopes; old reviewer access, prior issue/group/category dispositions and neighbor correctness are not recertified. Any scientific edit belongs to separately authorized guarded-writer curation; no record edited here.

### Frozen original and current inputs; immutable pair

provenance: supported. Targets: GO:0005769.

Current target bytes match the original input; original qualified pass had no findings/actions. Original native validation/render passed; no artifact, record, status or historical finding rewritten.

### Actual current native verifier coverage

schema: supported. Targets: GO:0005769.

Verify has an empty declared protein-example/xref inventory. Causal command counts zero GENE_OR_PROTEIN nodes; this is not validation of all graph biology, narrative proteins, membership or necessity.

### Actual pathway-triggered structured-source applicability

evidence: concern. Targets: GO:0005769.

Definition and function name clathrin-dependent/independent endocytosis and recycling/degradation cargo-sorting pathways. Original expression-only N/A rationale is insufficient. Current bounded catalogue contains no matching organism/dataset, so no downstream module query applies. Historical runner unavailability is separately dated; absence is not biological evidence.

### PROPOSED status and bounded curation ownership

provenance: supported. Targets: GO:0005769.

Review preserves PROPOSED and append-only history. Source receipts describe inspected scopes; old reviewer access, prior issue/group/category dispositions and neighbor correctness are not recertified. Any scientific edit belongs to separately authorized guarded-writer curation; no record edited here.

### Frozen original and current inputs; immutable pair

provenance: supported. Targets: GO:0031905.

Current target bytes match the original input; original qualified pass had no findings/actions. Original native validation/render passed; no artifact, record, status or historical finding rewritten.

### Actual current native verifier coverage

schema: supported. Targets: GO:0031905.

Verify has an empty declared protein-example/xref inventory. Causal command counts zero GENE_OR_PROTEIN nodes; this is not validation of all graph biology, narrative proteins, membership or necessity.

### Actual pathway-triggered structured-source applicability

evidence: concern. Targets: GO:0031905.

Function/evidence and canonical example explicitly assert cargo routing through the early-endocytic pathway; topology-only graph does not erase this trigger. Original expression-only N/A rationale is insufficient. Current bounded catalogue contains no matching organism/dataset, so no downstream module query applies. Historical runner unavailability is separately dated; absence is not biological evidence.

### PROPOSED status and bounded curation ownership

provenance: supported. Targets: GO:0031905.

Review preserves PROPOSED and append-only history. Source receipts describe inspected scopes; old reviewer access, prior issue/group/category dispositions and neighbor correctness are not recertified. Any scientific edit belongs to separately authorized guarded-writer curation; no record edited here.

### Frozen original and current inputs; immutable pair

provenance: supported. Targets: GO:0031901.

Current target bytes match the original input; original qualified pass had no findings/actions. Original native validation/render passed; no artifact, record, status or historical finding rewritten.

### Actual current native verifier coverage

schema: supported. Targets: GO:0031901.

Verify has an empty declared protein-example/xref inventory. Causal command counts zero GENE_OR_PROTEIN nodes; this is not validation of all graph biology, narrative proteins, membership or necessity.

### Actual pathway-triggered structured-source applicability

evidence: concern. Targets: GO:0031901.

Occurrence/canonical example and evidence explicitly place the membrane-bounded network in the T.cruzi endocytic pathway; a compartmentalization-only graph does not remove that asserted pathway context. Original expression-only N/A rationale is insufficient. Current bounded catalogue contains no matching organism/dataset, so no downstream module query applies. Historical runner unavailability is separately dated; absence is not biological evidence.

### PROPOSED status and bounded curation ownership

provenance: supported. Targets: GO:0031901.

Review preserves PROPOSED and append-only history. Source receipts describe inspected scopes; old reviewer access, prior issue/group/category dispositions and neighbor correctness are not recertified. Any scientific edit belongs to separately authorized guarded-writer curation; no record edited here.

### Structural proto-organelle boundary

identity: supported. Targets: cellstructuremech:diazoplast.

Minted compartment identity and intracellular-organelle parent are compatible with permanent Epithemia diazoplasts while genetic integration remains unresolved. Related spheroid-body synonym is source usage; diazoplast is not the UCYN-A/Braarudosphaera nitroplast. No exact match in the bounded current GO query is not universal absence.

### Genus occurrence and measured isolate

scope: supported. Targets: cellstructuremech:diazoplast.

Frail Introduction explicitly says all described Epithemia species; COMMON is qualitative, not a measured universal physiological pattern. Moulin/Gazos Creek Butano-area E.clementina strain and nonaxenic culture context are verified; ENA retains nom.ined. label. Frail later axenic cultures do not change the earlier experimental conditions.

### Nitrogenase, retained membranes and bounded HupL role

grounding: supported. Targets: cellstructuremech:diazoplast.

Moulin intact nif cluster, NifDK detection and nitrogenase activity support nitrogenase membership; retained internal thylakoids and boundary membranes do not imply photosynthesis. HupL detection supports the annotated recycling subunit at immunoblot/functional-assignment tier, not in-situ localization or measured H2 flux. Broad InterPro families and symbol-synonym collisions do not supply an exact uptake-specific equivalog; open grounding discussion remains appropriate.

### Accession identity, status and bounded query uniqueness

grounding: supported. Targets: cellstructuremech:diazoplast.

C1DK95 is unreviewed Azotobacter DJ with primary anfH and nifH synonym; reviewed P07328/P07329 map nifD/nifK and taxon354. Exact reviewed organism queries each return the stated single entry. These identities do not establish Epithemia membership, a native mixed-accession assembly or one protein as the whole complex.

### Identity-only examples versus structure-role field contract

grounding: concern. Targets: cellstructuremech:diazoplast.

Three examples explicitly disclaim structure membership, while ProteinExample requires the role in the structure to have been established for the named organism. The experiments concern Epithemia and the references are Azotobacter identities. Original minor F1 remains confirmed with exact lineage; accessions and nitrogenase component itself remain valid.

### Formation necessity distinct from activity

grounding: unknown. Targets: cellstructuremech:diazoplast.

All three components retain UNKNOWN. Detection, enzymatic function, material constitution and metabolic perturbations do not test whether the organelle forms without each molecule. No complete stoichiometry or exhaustive membrane inventory asserted.

### Substantive refresh of complex-node retyping

graph: supported. Targets: cellstructuremech:diazoplast.

The sole scientific delta changes nitrogenase from GENE_OR_PROTEIN to STRUCTURE while retaining GO0016610 and nitrogenase component_ref; native GO defines a multisubunit complex, so the new type fits the component/graph contract. Current zero typed gene nodes is expected, not evidence that the original ProteinExample placement was fixed. The added history mentioning grouped issue2404 does not terminally resolve that group or its unfrozen predecessor.

### Isotope exchange and physiological coupling

evidence: supported. Targets: cellstructuremech:diazoplast.

Moulin isotope data and culture ARA support compartment fixation, host nitrogen supply, photosynthetic carbon production and carbon transfer; transferred chemical species and transporters remain unidentified. NanoSIMS wash/dehydration effects preclude simple timing inference; IRMS distinguishes daytime host fixation. Nitrogen transfer not inferred from mere sequence annotation.

### All seven process-level mechanistic edges

graph: supported. Targets: cellstructuremech:diazoplast.

The seven edges retain nitrogenase catalysis, compartment fixation, nitrogen supply, host carbon production/transfer, photosynthetic support and partial inhibition. MECHANISTIC is defensible at the explicitly restricted E.clementina process/perturbation level: Results~60% reduction overrides stronger abstract abolition wording. No causal transporter identity, specific metabolite, respiration protection or division/import machinery asserted.

### Candidate proteins and hypotheses remain unresolved

evidence: supported. Targets: cellstructuremech:diazoplast.

Frail s5–7 and Discussion distinguish six enriched candidates from validated localization, undetected TusA from import evidence, and unsupported PFK import. Genetic-integration and host fission/confinement proposals remain hypotheses. Moulin species comparison and glycogen/respiration limitations prevent genus-wide physiology or universal glycogen absence.

### Figure2 pixels, native bytes, licence and taxon

evidence: supported. Targets: cellstructuremech:diazoplast.

Whole frozen A–C figure visually inspected; it matches native version1 asset SHA256 and MD5/size listing. Native caption supports12h/24h isotope panels, diazoplast arrows and quantified host/diazoplast regions. JATS author list and CC BY4.0 match record attribution; this is Moulin2024, not Frail2025 with a different licence. No quantitative reanalysis.

### Whole organelle, lumen and boundary remain distinct

identity: supported. Targets: GO:0005769.

Exact GO/UniProt identity and mappings match: whole organelle is an endosome; surrounding membrane and lumen are parts. Reservosome neighbor supplies identity context only as a separate downstream storage organelle.

### Epimastigote occurrence and source identification tier

scope: supported. Targets: GO:0005769.

Exact taxon5693 is T.cruzi. Porto complete primary abstract supports protein-gold cargo moving from principal cytostome/cytopharynx entry to interconnected vesicles/tubules and reservosomes. Authors propose early-endosome identity from pH and kinetics; no molecular marker or species-wide life-stage equivalence is invented. VARIABLE is qualitative; membrane/lumen existence follows the described bounded network plus exact authorities.

### Constitution versus optional molecular inventories

grounding: supported. Targets: GO:0005769.

Complete lipid bilayer constituting the membrane is supported; ESSENTIAL is collective constitution, not an experimentally demonstrated requirement for a particular lipid species. No full protein census or chemical stoichiometry claimed.

### Individual lipid requirements

grounding: unknown. Targets: GO:0005769.

The constitutional bilayer ESSENTIAL row does not identify necessity of particular molecular species, substitutes or concentrations. Those assembly requirements remain untested and should not be inferred from defining topology.

### Generic function separated from organism-specific route

evidence: supported. Targets: GO:0005769.

Generic incoming-vesicle sorting toward recycling/degradation follows GO/SL. Porto supplies only the stated T.cruzi protein-cargo route, not proof of every generic sorting branch or a full Rab/coat/tether mechanism.

### All NONMECHANISTIC edges scoped

graph: supported. Targets: GO:0005769.

Four classification/parthood/enclosure edges follow native authorities. Three cargo-route edges remain T.cruzi-epimastigote-specific and nonexclusive; abstract supports protein transit. The lipid-specific extension of final edge remains separately unknown.

### Entire record; source tier and omitted optional data

completeness: supported. Targets: GO:0005769.

Entire target read. No image, measured physical property, verbatim snippet or protein example is asserted. Porto source identity and abstract are current verified, while publisher403 and public API metadata stub leave body/methods/strain/figure pixels unverified. Neighbor records do not replace primary evidence. Unknown optional inventories are not invented findings.

### Whole organelle, lumen and boundary remain distinct

identity: supported. Targets: GO:0031905.

Exact GO/UniProt identity and mappings match: lumen is an endosome-lumen specialization inside the early endosome, bounded by its membrane. Reservosome neighbor supplies identity context only as a separate downstream storage organelle.

### Epimastigote occurrence and source identification tier

scope: supported. Targets: GO:0031905.

Exact taxon5693 is T.cruzi. Porto complete primary abstract supports protein-gold cargo moving from principal cytostome/cytopharynx entry to interconnected vesicles/tubules and reservosomes. Authors propose early-endosome identity from pH and kinetics; no molecular marker or species-wide life-stage equivalence is invented. VARIABLE is qualitative; membrane/lumen existence follows the described bounded network plus exact authorities.

### Constitution versus optional molecular inventories

grounding: supported. Targets: GO:0031905.

Lumen is an enclosed region, and the membrane is its boundary, not a lumen component; optional cargo inventory need not be populated.

### Generic function separated from organism-specific route

evidence: supported. Targets: GO:0031905.

The lumen is the volume through which cargo passes, supported by exact topology plus bounded protein-cargo uptake evidence; no lumen-localized enzyme, receptor or quantitative pH asserted.

### All NONMECHANISTIC edges scoped

graph: supported. Targets: GO:0031905.

Three edges preserve lumen is-a, organelle parthood and surrounding-membrane boundary; no molecular transition implied.

### Entire record; source tier and omitted optional data

completeness: supported. Targets: GO:0031905.

Entire target read. No image, measured physical property, verbatim snippet or protein example is asserted. Porto source identity and abstract are current verified, while publisher403 and public API metadata stub leave body/methods/strain/figure pixels unverified. Neighbor records do not replace primary evidence. Unknown optional inventories are not invented findings.

### Whole organelle, lumen and boundary remain distinct

identity: supported. Targets: GO:0031901.

Exact GO/UniProt identity and mappings match: surrounding bilayer is an endosome-membrane specialization and a part of early endosome. Reservosome neighbor supplies identity context only as a separate downstream storage organelle.

### Epimastigote occurrence and source identification tier

scope: supported. Targets: GO:0031901.

Exact taxon5693 is T.cruzi. Porto complete primary abstract supports protein-gold cargo moving from principal cytostome/cytopharynx entry to interconnected vesicles/tubules and reservosomes. Authors propose early-endosome identity from pH and kinetics; no molecular marker or species-wide life-stage equivalence is invented. VARIABLE is qualitative; membrane/lumen existence follows the described bounded network plus exact authorities.

### Constitution versus optional molecular inventories

grounding: supported. Targets: GO:0031901.

Complete lipid bilayer constituting the membrane is supported; ESSENTIAL is collective constitution, not an experimentally demonstrated requirement for a particular lipid species. No full protein census or chemical stoichiometry claimed.

### Individual lipid requirements

grounding: unknown. Targets: GO:0031901.

The constitutional bilayer ESSENTIAL row does not identify necessity of particular molecular species, substitutes or concentrations. Those assembly requirements remain untested and should not be inferred from defining topology.

### Generic function separated from organism-specific route

evidence: supported. Targets: GO:0031901.

Compartmentalization is a boundary function, supported by exact membrane/lumen definitions. It does not assign autonomous cargo sorting machinery or enzyme activity to lipid.

### All NONMECHANISTIC edges scoped

graph: supported. Targets: GO:0031901.

Three edges preserve membrane is-a, organelle parthood and lumen boundary, without inventing a Rab/coat mechanism.

### Entire record; source tier and omitted optional data

completeness: supported. Targets: GO:0031901.

Entire target read. No image, measured physical property, verbatim snippet or protein example is asserted. Porto source identity and abstract are current verified, while publisher403 and public API metadata stub leave body/methods/strain/figure pixels unverified. Neighbor records do not replace primary evidence. Unknown optional inventories are not invented findings.

### Lipid-specific transit remains unverified

evidence: unknown. Targets: GO:0005769.

The final whole-endosome graph description extends cargo transit to protein and lipid. Current primary abstract directly traces gold-protein conjugates and does not describe a lipid tracer. Full primary body remains inaccessible through checked routes, so neither confirmation nor contradiction of lipid-specific passage is established. Preserve the original explicit unknown; no new scientific finding solely from access limitation.

### Original schema/render and unchanged frozen targets

schema: supported. Targets: GO:0031410.

Original bundle validation and deterministic rendering pass. Original target hash matches its historical source and current bytes; no stale refresh is required for these three records.

### Empty represented protein inventory

provenance: supported. Targets: GO:0031410.

No protein examples or UniProtKB graph xrefs and zero GENE_OR_PROTEIN graph nodes. Native execution success covers only this empty represented inventory, not narrative pathway mechanisms, source-localized molecular actors or completeness.

### Images, physical measurements, traits and snippets

scope: not_applicable. Targets: GO:0031410.

No such surface is declared in the maintained target. A study caption or source description is not target image/pixel or raw-data validation.

### Original schema/render and unchanged frozen targets

schema: supported. Targets: GO:0060205.

Original bundle validation and deterministic rendering pass. Original target hash matches its historical source and current bytes; no stale refresh is required for these three records.

### Empty represented protein inventory

provenance: supported. Targets: GO:0060205.

No protein examples or UniProtKB graph xrefs and zero GENE_OR_PROTEIN graph nodes. Native execution success covers only this empty represented inventory, not narrative pathway mechanisms, source-localized molecular actors or completeness.

### Images, physical measurements, traits and snippets

scope: not_applicable. Targets: GO:0060205.

No such surface is declared in the maintained target. A study caption or source description is not target image/pixel or raw-data validation.

### Original schema/render and unchanged frozen targets

schema: supported. Targets: GO:0030659.

Original bundle validation and deterministic rendering pass. Original target hash matches its historical source and current bytes; no stale refresh is required for these three records.

### Empty represented protein inventory

provenance: supported. Targets: GO:0030659.

No protein examples or UniProtKB graph xrefs and zero GENE_OR_PROTEIN graph nodes. Native execution success covers only this empty represented inventory, not narrative pathway mechanisms, source-localized molecular actors or completeness.

### Images, physical measurements, traits and snippets

scope: not_applicable. Targets: GO:0030659.

No such surface is declared in the maintained target. A study caption or source description is not target image/pixel or raw-data validation.

### Yeast occurrence and condition-bounded subtype evidence

scope: supported. Targets: GO:0031410.

S.cerevisiae is correctly identified; Reggiori names BY4742/SEY6210 and conditional strains. The canonical note states a broad model and early-secretory assembly study, without an unsupported strain-specific microscopy claim. COMMON is qualitative, and the Cvt subtype is not a universal mechanism or membrane-origin model for all cytoplasmic vesicles.

### Actual pathway applicability and catalogue noncoverage

scope: not_applicable. Targets: GO:0031410.

The complete record affirms Cvt/early-secretory pathway context, so an expression-only exemption is insufficient. Current official catalogue inspection finds no matching yeast organism/dataset; downstream gene/module queries are not applicable. Historical unavailable runner remains separately timestamped and noncoverage does not imply biological absence.

### Current status and scope of historical statements

provenance: supported. Targets: GO:0031410.

PROPOSED status and historical curation text are unchanged. Current source review does not retrospectively certify old gate execution, authorship or searches and does not terminally resolve any neighbor/group/category issue.

### Yeast occurrence and condition-bounded subtype evidence

scope: supported. Targets: GO:0060205.

S.cerevisiae is correctly identified; Reggiori names BY4742/SEY6210 and conditional strains. The canonical note states a broad model and early-secretory assembly study, without an unsupported strain-specific microscopy claim. COMMON is qualitative, and the Cvt subtype is not a universal mechanism or membrane-origin model for all cytoplasmic vesicles.

### Actual pathway applicability and catalogue noncoverage

scope: not_applicable. Targets: GO:0060205.

The complete record affirms Cvt/early-secretory pathway context, so an expression-only exemption is insufficient. Current official catalogue inspection finds no matching yeast organism/dataset; downstream gene/module queries are not applicable. Historical unavailable runner remains separately timestamped and noncoverage does not imply biological absence.

### Current status and scope of historical statements

provenance: supported. Targets: GO:0060205.

PROPOSED status and historical curation text are unchanged. Current source review does not retrospectively certify old gate execution, authorship or searches and does not terminally resolve any neighbor/group/category issue.

### Yeast occurrence and condition-bounded subtype evidence

scope: supported. Targets: GO:0030659.

S.cerevisiae is correctly identified; Reggiori names BY4742/SEY6210 and conditional strains. The canonical note states a broad model and early-secretory assembly study, without an unsupported strain-specific microscopy claim. COMMON is qualitative, and the Cvt subtype is not a universal mechanism or membrane-origin model for all cytoplasmic vesicles.

### Actual pathway applicability and catalogue noncoverage

scope: not_applicable. Targets: GO:0030659.

The complete record affirms Cvt/early-secretory pathway context, so an expression-only exemption is insufficient. Current official catalogue inspection finds no matching yeast organism/dataset; downstream gene/module queries are not applicable. Historical unavailable runner remains separately timestamped and noncoverage does not imply biological absence.

### Current status and scope of historical statements

provenance: supported. Targets: GO:0030659.

PROPOSED status and historical curation text are unchanged. Current source review does not retrospectively certify old gate execution, authorship or searches and does not terminally resolve any neighbor/group/category issue.

### Whole cytoplasmic carrier class

identity: supported. Targets: GO:0031410.

GO0031410 definition, vesicle parentage, membrane/lumen parts and exact SL0088 mapping identify a complete membrane-bounded cytoplasmic vesicle. The generic record is distinct from Cvt or coat-defined subtypes, cargo proteins and transport processes.

### Collective defining membrane part

grounding: supported. Targets: GO:0031410.

The grounded LIPID row denotes the complete structural membrane part defined by GO0030659. ESSENTIAL is collective bilayer constitution, not a claimed necessity for each molecular lipid or protein. No full inventory or stoichiometry is asserted.

### Individual molecular formation requirements

grounding: unknown. Targets: GO:0031410.

The selected primary transport evidence does not establish individual lipid-species removal/substitution requirements. This uncertainty does not negate the membrane-bounded identity or create an unsupported knockout claim.

### Broad transport function and two nonmechanistic edges

graph: supported. Targets: GO:0031410.

SL0088 supports the broad secretory/endocytic carrier context. The two edges assert membrane parthood and carrier support of that transport class. They do not prescribe a universal coat, cargo, donor/acceptor pair or budding/fusion mechanism.

### Subtype coats and cargo are not universal components

completeness: supported. Targets: GO:0031410.

The resolved local discussion explicitly excludes subtype-specific clathrin/COPI/COPII, synaptic/secretory cargo and phagosome examples from generic constituents. Exact source scope supports this boundary. This reassessment does not newly resolve any earlier issue or certify a complete subtype inventory.

### Exact enclosed-volume identity and hierarchy

identity: supported. Targets: GO:0060205.

GO0060205 and SL0325 denote the cytoplasmic-vesicle enclosed volume. GO0031983 is its vesicle-lumen parent; cytoplasmic-vesicle parthood is supported. A lumen is a region, not its cargo or an independently operating pathway.

### Two boundary relations and no generic cargo function

graph: supported. Targets: GO:0060205.

Lumen part_of whole vesicle and membrane encloses lumen follow the exact GO/location descriptions. The Cvt model illustrates enclosed cargo volume without assigning universal cargo or molecular transport steps to every lumen. No removed generic-cargo function is silently restored.

### Optional lumen inventory remains unasserted

completeness: not_applicable. Targets: GO:0060205.

No material component, individual protein or molecular essentiality row is declared. A soluble inventory or independent process function is not required to define the bounded generic region; no absent optional field is called a defect.

### Exact surrounding-bilayer identity

identity: supported. Targets: GO:0030659.

GO0030659 definition, membrane parent, cytoplasmic-vesicle parthood and exact SL0089 mapping identify the surrounding membrane. These remain correct despite the localized Cvt example wording defect.

### Collective bilayer with limited chemical specificity

grounding: supported. Targets: GO:0030659.

REVIEWED_LABEL_ONLY applies to the generic lipid constituent, with an explicit chemical-grounding TODO. The membrane location is not falsely used as an individual lipid-species identity. This review does not establish exhaustive ontology absence or specific composition ratios.

### Constitution does not establish individual-lipid necessity

grounding: unknown. Targets: GO:0030659.

The ESSENTIAL material row is definitional membrane constitution. Reggiori transport experiments do not establish removal/substitution requirements for particular lipid species, and no such molecular assay is asserted.

### Two descriptive membrane relations

graph: supported. Targets: GO:0030659.

Membrane part_of and bounds whole cytoplasmic vesicle are supported surrounding-boundary relations. The nonmechanistic graph does not assert a coat, universal cargo or donor/acceptor mechanism and is not itself affected by the taxonomic-note error.

### Cvt carrier versus either constituent bilayer

scope: concern. Targets: GO:0030659.

The taxonomic note still calls Cvt vesicle membranes a double-membrane cytosolic carrier subtype. Current GO0033110 denotes either bilayer; GO0033107 and Reggiori identify the entire carrier as double-membrane. This reproduces the original minor F1 exactly and requires only separately authorized note curation.

### Qualified positive scientific assessment

evidence: supported. Targets: GO:0031410.

No concrete scientific correction was established in this complete assigned-record scope. Retain conditional subtype evidence, partial primary-body access, chemical necessity unknowns, empty native inventory and catalogue noncoverage. The review applicability defect is separately corrected by an immutable successor.

### Qualified positive scientific assessment

evidence: supported. Targets: GO:0060205.

No concrete scientific correction was established in this complete assigned-record scope. Retain conditional subtype evidence, partial primary-body access, chemical necessity unknowns, empty native inventory and catalogue noncoverage. The review applicability defect is separately corrected by an immutable successor.

### One inherited minor finding remains open

evidence: concern. Targets: GO:0030659.

Identity, component, hierarchy and graph remain sound. The one inherited carrier-versus-bilayer example note remains a minor request for separate record curation; a positive schema or native accession check does not resolve it.

### Complete frozen-input comparison and bounded refresh

provenance: supported. Targets: GO:0009843, GO:0033114, GO:0033115, GO:0031410, GO:0060205, GO:0030659, cellstructuremech:diazoplast, GO:0005769, GO:0031905, GO:0031901.

1 of ten original target hashes differ from current main. The changed content is substantively reassessed in the target-specific assessments; original observations remain historical and unchanged. All current target and used context bytes are frozen.

## Findings

### micro-F1: Identity-only Azotobacter references occupy a structure-specific protein-example field

minor / open / confirmed; issue key: diazoplast-cross-taxon-protein-example-placement.

ProteinExample is defined as an organism-specific instance where the protein role in the structure was established. The three Azotobacter examples explicitly establish accession/gene identity only and disclaim structure membership; the cited diazoplast experiments instead concern Epithemia. Their placement therefore exceeds the field contract despite appropriately cautious notes. The accessions, gene tokens, taxa and nitrogenase component itself are valid.

### septin-F1: Keep the Cvt membrane example distinct from its complete carrier

minor / open / confirmed; issue key: cytoplasmic-vesicle-membrane-cvt-example-carrier-wording.

The Saccharomyces distribution note describes Cvt vesicle membranes as a double-membrane cytosolic carrier subtype of the cytoplasmic vesicle membrane class. GO:0033110 denotes either constituent bilayer; GO:0033107 and Reggiori describe the whole carrier as double-membrane. Rewrite the local note to say that budding yeast has Cvt vesicles whose individual bilayers are cytoplasmic-vesicle-membrane subtypes. The record identity, taxon, membrane component and graph remain sound.

## Recommended Actions And Acceptance Checks

### micro-A1

In a separately authorized curation change, move cross-taxon identity-only references to discussion/context, or replace them with verified diazoplast/symbiont instances only when source-backed. If no such instances are established, omit protein_examples while preserving the supported nitrogenase component, gene-symbol metadata and primary evidence.

- Every retained protein_example has exact native identity metadata and evidence linking that instance/taxon to the diazoplast structure; identity-only references remain clearly contextual.
- Do not relabel Azotobacter accessions as Epithemia or infer an incorrect gene from the anfH/nifH synonym bridge.
- Preserve the supported nif cluster, nitrogenase membership and UNKNOWN formation necessity; run focused schema, strict and UniProt verification checks.
- Record curation remains a separate guarded-writer change; this review PR edits no scientific record.

### septin-A1

Under separately authorized curation, reword the yeast occurrence note to distinguish the whole double-membrane Cvt vesicle from either of its bilayers; keep the existing native IDs and taxon.

- The note assigns the double-membrane carrier description to the Cvt vesicle and the generic membrane subtype relation to either Cvt bilayer.
- Use the guarded writer and required history; run focused schema/strict and history checks, then render and qc.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| current-record-0 | data/structures/membrane_organelle/cyanelle_thylakoid.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 19838578792948bb527b33a0dd61374b6ee7a688eb2ee0406426c2e95639c7e3; current SHA256 19838578792948bb527b33a0dd61374b6ee7a688eb2ee0406426c2e95639c7e3. Record bytes unchanged since the original review. |
| original-review-0 | reviews/structured/20261022T013526Z-cyanelle-thylakoid-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-1 | data/structures/membrane_organelle/cyanelle_thylakoid_lumen.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 6dc48d3d810b7a63387502082d26502265a7f12eafec88058eb9e5d8be70a205; current SHA256 6dc48d3d810b7a63387502082d26502265a7f12eafec88058eb9e5d8be70a205. Record bytes unchanged since the original review. |
| original-review-1 | reviews/structured/20261022T013527Z-cyanelle-thylakoid-lumen-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-2 | data/structures/membrane_organelle/cyanelle_thylakoid_membrane.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 c1c3958038a4f3a20735ce33206475130078e9a12048dcbeff4bc0d04beb4178; current SHA256 c1c3958038a4f3a20735ce33206475130078e9a12048dcbeff4bc0d04beb4178. Record bytes unchanged since the original review. |
| original-review-2 | reviews/structured/20261022T013528Z-cyanelle-thylakoid-membrane-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-3 | data/structures/membrane_organelle/cytoplasmic_vesicle.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 f4704b74324c18cab955983a27173d6a98fae0153bc7a403cbbe3c865e4eba84; current SHA256 f4704b74324c18cab955983a27173d6a98fae0153bc7a403cbbe3c865e4eba84. Record bytes unchanged since the original review. |
| original-review-3 | reviews/structured/20261022T013529Z-cytoplasmic-vesicle-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-4 | data/structures/membrane_organelle/cytoplasmic_vesicle_lumen.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 87d5a5379cb643e40257e60c99a3308f2b6e6a49aa079856fb501fe6e3c738fe; current SHA256 87d5a5379cb643e40257e60c99a3308f2b6e6a49aa079856fb501fe6e3c738fe. Record bytes unchanged since the original review. |
| original-review-4 | reviews/structured/20261022T013530Z-cytoplasmic-vesicle-lumen-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-5 | data/structures/membrane_organelle/cytoplasmic_vesicle_membrane.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 112643d19f662095c8d81c907d5d6435fe93b612f8a037df2af0fe66af87d4aa; current SHA256 112643d19f662095c8d81c907d5d6435fe93b612f8a037df2af0fe66af87d4aa. Record bytes unchanged since the original review. |
| original-review-5 | reviews/structured/20261022T013531Z-cytoplasmic-vesicle-membrane-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-6 | data/structures/membrane_organelle/diazoplast.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 7aabee1c3f14420665958c955451705d3c7ea115003ffd94060a2f1afd40d41f; current SHA256 fd3948e827eb4a9870bc4eccb09689dd5c82f5caef443f1e319daabbf21bb038. Changed record reassessed against current sources. |
| original-review-6 | reviews/structured/20261022T013532Z-diazoplast-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-7 | data/structures/membrane_organelle/early_endosome.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 ed91f355f5faca2b5bd7af5036740c6d6034d783fcfa0252aeb533489c6a46a9; current SHA256 ed91f355f5faca2b5bd7af5036740c6d6034d783fcfa0252aeb533489c6a46a9. Record bytes unchanged since the original review. |
| original-review-7 | reviews/structured/20261022T013533Z-early-endosome-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-8 | data/structures/membrane_organelle/early_endosome_lumen.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 fe21c86defd34e34c5df67ec7bc0e7be16cc0342f2b10c6bae2ffd9569060290; current SHA256 fe21c86defd34e34c5df67ec7bc0e7be16cc0342f2b10c6bae2ffd9569060290. Record bytes unchanged since the original review. |
| original-review-8 | reviews/structured/20261022T013534Z-early-endosome-lumen-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-9 | data/structures/membrane_organelle/early_endosome_membrane.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 2d96c5c692f3e324e718d1fc2750703c41060a9ef56dd535cd55831da69354dc; current SHA256 2d96c5c692f3e324e718d1fc2750703c41060a9ef56dd535cd55831da69354dc. Record bytes unchanged since the original review. |
| original-review-9 | reviews/structured/20261022T013534Z-early-endosome-membrane-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| plaque-current-0 | data/structures/membrane_organelle/cyanelle_thylakoid.yaml; Entire maintained record at source cd5be11ad13304d75404a51d097635022d1bd091; all fields, histories, discussions and graphs | supports | Entire current target independently read. Hash remains unchanged from original frozen target; PROPOSED status unchanged and no record curation performed. |
| plaque-original-0 | reviews/structured/20261022T013526Z-cyanelle-thylakoid-audit/review.yaml; Original authoritative YAML/Markdown, source inputs, checks, assessments, findings/actions and limitations | supports | Original native validate/render passes and all original historical input hashes match. Verdict pass_with_limitations, no findings or actions. No original scientific finding exists to terminally dispose of. |
| plaque-current-1 | data/structures/membrane_organelle/cyanelle_thylakoid_lumen.yaml; Entire maintained record at source cd5be11ad13304d75404a51d097635022d1bd091; all fields, histories, discussions and graphs | supports | Entire current target independently read. Hash remains unchanged from original frozen target; PROPOSED status unchanged and no record curation performed. |
| plaque-original-1 | reviews/structured/20261022T013527Z-cyanelle-thylakoid-lumen-audit/review.yaml; Original authoritative YAML/Markdown, source inputs, checks, assessments, findings/actions and limitations | supports | Original native validate/render passes and all original historical input hashes match. Verdict pass_with_limitations, no findings or actions. No original scientific finding exists to terminally dispose of. |
| plaque-current-2 | data/structures/membrane_organelle/cyanelle_thylakoid_membrane.yaml; Entire maintained record at source cd5be11ad13304d75404a51d097635022d1bd091; all fields, histories, discussions and graphs | supports | Entire current target independently read. Hash remains unchanged from original frozen target; PROPOSED status unchanged and no record curation performed. |
| plaque-original-2 | reviews/structured/20261022T013528Z-cyanelle-thylakoid-membrane-audit/review.yaml; Original authoritative YAML/Markdown, source inputs, checks, assessments, findings/actions and limitations | supports | Original native validate/render passes and all original historical input hashes match. Verdict pass_with_limitations, no findings or actions. No original scientific finding exists to terminally dispose of. |
| plaque-policy | .claude/skills/review-yaml-record/SKILL.md; Frozen native policy/schema; complete applicable rules and taxonomy descriptions | context_only | Actual named genes/proteins/regulators/pathways/stress responses/traits trigger structured-source assessment. Generic material/topology or explicitly withheld molecular assignments are genuine exclusions. |
| plaque-rubric | .claude/skills/curate-yaml-record/references/review-checklist.md; Frozen native policy/schema; complete applicable rules and taxonomy descriptions | context_only | Source-scoped identity, component grounding, necessity, taxonomy and graph assessment; no compulsory protein inventory is fabricated for a material or topology record. |
| plaque-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Frozen native policy/schema; complete applicable rules and taxonomy descriptions | context_only | NONMECHANISTIC is a descriptive topology/function graph, not a demonstrated molecular formation mechanism. |
| plaque-schema-policy | src/cellstructuremech/schema/cellstructuremech.yaml; Frozen native policy/schema; complete applicable rules and taxonomy descriptions | context_only | Native schema introduction explicitly lists whole thylakoid as organelle-level granularity and MEMBRANE_ORGANELLE includes thylakoids. This coarse repository kind does not assert GO is_a organelle; GO0009579 comment about ontology organelle classification is not a contradiction in exact GO identity. |
| plaque-thylakoid-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009843,GO:0009842,GO:0009579,GO:0031976,GO:0033114,GO:0033115,GO:0031978,GO:0042651,GO:0055035,GO:0019684; Complete exact ten-term definitions, synonyms, obsolete status and typed child relations:0009843,0009842,0009579,0031976,0033114,0033115,0031978,0042651,0055035,0019684 | supports | GO0009843 is_a plastid thylakoid0031976, itself is_a thylakoid0009579; cyanelle0009842 contains0009843. Whole0009843 contains lumen0033114 and membrane0033115. Lumen is_a plastid lumen0031978; membrane is_a plastid thylakoid membrane0055035, itself is_a0042651. Both direct and broader parent classes are valid without claiming every parent direct. GO0019684 defines light reactions, not an experiment or particular protein necessity. |
| plaque-thylakoid-agent-SL-0277 | https://rest.uniprot.org/locations/SL-0277.json; Complete top-level definition, immediate isA/partOf and direct GO correspondence; nested objects distinguished | supports | SL0277 exactly mapsGO0009843, describing interconnected internal cyanelle membranes carrying out photosynthetic reactions; partOfSL0082 and parentSL0278. Protein counts are not structural prevalence or constituent necessity evidence. |
| plaque-thylakoid-agent-SL-0084 | https://rest.uniprot.org/locations/SL-0084.json; Complete top-level definition, immediate isA/partOf and direct GO correspondence; nested objects distinguished | supports | SL0084 exactly mapsGO0033114, the compartment bounded by cyanelle thylakoid membranes; parentSL0309 and partOfSL0277. Protein counts are not structural prevalence or constituent necessity evidence. |
| plaque-thylakoid-agent-SL-0085 | https://rest.uniprot.org/locations/SL-0085.json; Complete top-level definition, immediate isA/partOf and direct GO correspondence; nested objects distinguished | supports | SL0085 exactly mapsGO0033115, the lipid bilayer surrounding the thylakoid space within a glaucophyte photosynthetic organelle; parentSL0216 and partOfSL0277. Protein counts are not structural prevalence or constituent necessity evidence. |
| plaque-cached-tax2762 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2762; Complete native taxId/scientificName/rank/lineage/alternative names | supports | ENA verifies Cyanophora paradoxa 2762. Species belongs to Glaucocystophyceae. Identity does not establish experimental strain or numerical prevalence. Prior PR2362 snapshot independently reread; actual11:52Z fetch time retained, not a fresh request. |
| plaque-cached-tax38254 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/38254; Complete native taxId/scientificName/rank/lineage/alternative names | supports | ENA verifies Glaucocystophyceae 38254. Glaucophyta and Glaucophyceae are synonyms of class Glaucocystophyceae. Identity does not establish experimental strain or numerical prevalence. Prior PR2362 snapshot independently reread; actual11:52Z fetch time retained, not a fresh request. |
| plaque-cached-giddings1983-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1104%2Fpp.71.2.409; Complete primary abstract and exact title/authors/year/DOI10.1104/pp.71.2.409/PMID16662839 metadata | supports | Giddings/Wasmann/Staehelin1983 studies cyanelle thylakoids and envelope membranes in C.paradoxa by thin-section/freeze-fracture/etch microscopy and pigment/protein preparation. Presumptive PSII assignments and historical symbiont interpretation are not upgraded to modern molecular certainty. Prior PR2362 metadata snapshot independently reread with original fetch time; primary scan scopes are separately declared. |
| plaque-cached-giddings1983-page409 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/6ed041edd2c7/plntphys00558-0203.png; Scanned page409 visually inspected at original resolution: Title/authors, abstract, Introduction and initial culture/isolation Methods | supports | C.paradoxa UTEX LB555 grown at26C in modified CY-II medium under continuous illumination. Biological photosynthetic context and morphology are supported, without adopting historical endosymbiont language as modern ontology classification. Prior PR2362 scan independently viewed again with actual11:52Z retrieval retained. Only declared pages are claimed; no raw microscopy reanalysis. |
| plaque-cached-giddings1983-page410 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/8d99de19802c/plntphys00558-0204.png; Scanned page410 visually inspected at original resolution: Figures1–3 images/captions and continuing isolation Methods | supports | Whole cell and isolated cyanelle thin sections plus freeze-fracture thylakoid images show internal membranes and patterned surfaces. Isolated thylakoid preparations differ from intact cells; no new image measurements made. Prior PR2362 scan independently viewed again with actual11:52Z retrieval retained. Only declared pages are claimed; no raw microscopy reanalysis. |
| plaque-thylakoid-agent-giddings1983-page411 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/e0e22d1a8212/plntphys00558-0205.png; Scanned page411 visually inspected at original resolution: Figures4–5 plots/captions and spectrophotometry/electrophoresis/electron microscopy Methods | supports | Particle-size histograms and absorption spectra before/after phycobiliprotein removal support the experimental scope. These are not a complete protein inventory or live-cell flux assay. Fresh public scan fetched12:28Z and independently viewed. Only declared pages are claimed; no raw microscopy reanalysis. |
| plaque-cached-giddings1983-page412 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/392b5bf89308/plntphys00558-0206.png; Scanned page412 visually inspected at original resolution: Figure6 gel/caption, final preparation Methods and Thylakoids Results | supports | Protein preparations before/after pigment removal, thylakoid particle patterns and phycobilisome morphology distinguish supported material architecture from interpreted molecular identity. Prior PR2362 scan independently viewed again with actual11:52Z retrieval retained. Only declared pages are claimed; no raw microscopy reanalysis. |
| plaque-thylakoid-agent-giddings1983-page413 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/fa8191742d8c/plntphys00558-0207.png; Scanned page413 visually inspected at original resolution: Figures7–10 pixels and complete captions | supports | Thin-section and freeze-etch preparations show membrane sheets and surface phycobilisome rows; removed-pigment samples expose underlying particles. Interpreted particle identities remain qualified. Fresh public scan fetched12:28Z and independently viewed. Only declared pages are claimed; no raw microscopy reanalysis. |
| plaque-cached-giddings1983-page416 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/c329334d81e0/plntphys00558-0210.png; Scanned page416 visually inspected at original resolution: Figure15 histogram/caption, envelope Results continuation and Discussion opening | supports | Discussion relates thylakoid pigment, gel and microscopy observations to putative PSII centers. Proposed one-to-one structural association and reaction-center count are interpretations, not a complete verified proteome. Prior PR2362 scan independently viewed again with actual11:52Z retrieval retained. Only declared pages are claimed; no raw microscopy reanalysis. |
| plaque-cached-giddings1983-page417 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/7694ed6a7a74/plntphys00558-0211.png; Scanned page417 visually inspected at original resolution: Complete Discussion text and Figures16–18 pixels/captions | supports | Source explicitly states precise PSI localization is unknown and PSII-to-PSI versus direct energy transfer cannot be assessed. Envelope figures are not thylakoid evidence. Current target records do not assert the unsupported precise PSI arrangement. Prior PR2362 scan independently viewed again with actual11:52Z retrieval retained. Only declared pages are claimed; no raw microscopy reanalysis. |
| plaque-thylakoid-agent-giddings1983-page418 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/147bb64bab4f/plntphys00558-0212.png; Scanned page418 visually inspected at original resolution: Figure19 schematic pixels and full caption; no complete bibliography audit | supports | The thylakoid schematic distinguishes lipid bilayer, lumen-facing surface, phycobilisomes and presumptive PSII attachment sites. It is a model with probable/presumptive molecular assignments, not an independent experimental image or basis for complete molecular necessity. Fresh public scan fetched12:28Z and independently viewed. Only declared pages are claimed; no raw microscopy reanalysis. |
| plaque-catalogue | https://imodulondb.org/api/datasets; Complete fresh /api/datasets response: every returned organism and dataset entry inspected; no pagination | supports | No current organism row covers Cyanophora or another glaucophyte. A Synechococcus dataset is not substituted for a Cyanophora host context. Thus no matched downstream gene/module query applies. Catalogue noncoverage is not biological absence or a lack of photosynthetic machinery. |
| plaque-historical-runner | /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources imodulondb datasets; Original historical00:49Z receipt and stdout/stderr independently reread/hash-verified | context_only | Historical runner exited1 before datasets due OS PermissionError on pyvenv.cfg; not a new invocation or successful execution. Official current catalogue is the permitted source fallback. |
| plaque-original-checks | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/adversary-plaque/original-checks.json; Three read-only original native validate/render executions and every frozen input at historical source commit | supports | All three originals validate/render exactly. All12/12/12 historical input hashes match, and current targets remain unchanged. Original findings/actions empty. |
| plaque-native-cyanelle_thylakoid-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_thylakoid.yaml --verify; Actual root-owned native receipt and exact stdout independently read/hash-verified | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| plaque-native-cyanelle_thylakoid-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_thylakoid.yaml --causal-graphs; Actual root-owned native receipt and exact stdout independently read/hash-verified | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| plaque-native-cyanelle_thylakoid_lumen-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_thylakoid_lumen.yaml --verify; Actual root-owned native receipt and exact stdout independently read/hash-verified | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| plaque-native-cyanelle_thylakoid_lumen-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_thylakoid_lumen.yaml --causal-graphs; Actual root-owned native receipt and exact stdout independently read/hash-verified | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| plaque-native-cyanelle_thylakoid_membrane-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_thylakoid_membrane.yaml --verify; Actual root-owned native receipt and exact stdout independently read/hash-verified | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| plaque-native-cyanelle_thylakoid_membrane-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_thylakoid_membrane.yaml --causal-graphs; Actual root-owned native receipt and exact stdout independently read/hash-verified | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| micro-policy | .claude/skills/review-yaml-record/SKILL.md; Native source scopes, structured-adapter triggers, read-only ownership; profile/shared contract/config/checklist and graph/component schema retained as frozen context | context_only | All17 common policy/schema/verifier inputs hash-identical to prior reviewed set; native route and config reread, applicable protein and complex-field contracts rechecked. A named pathway can trigger applicability even in a topology graph; molecular identity alone does not establish membership. |
| micro-schema-protein-example | src/cellstructuremech/schema/cellstructuremech.yaml; Component.protein_examples lines448–454; ProteinExample description lines462–467; causal NodeType contract | supports | Protein examples require an organism-specific instance whose role in this structure was established. A single accession is not the whole multisubunit complex; STRUCTURE is appropriate for a GO-grounded nitrogenase complex. |
| micro-record-diazoplast | data/structures/membrane_organelle/diazoplast.yaml; Entire current maintained YAML including definition/history, components/examples, taxa, functions, all graph nodes/edges, discussions and any image | supports | Entire current target independently read at cd5be11ad13304d75404a51d097635022d1bd091. Diazoplast stale delta is new history plus nitrogenase node GENE_OR_PROTEIN→STRUCTURE; three protein examples remain unchanged. |
| micro-prior-diazoplast | reviews/structured/20261022T013532Z-diazoplast-audit/review.yaml; Original authoritative YAML and paired Markdown: frozen inputs, scientific assessments, findings/actions, limitations, native check claims and applicability rationale | context_only | Original observation preserved. Exact original F1 cross-taxon protein-example placement is re-evaluated with lineage retained. |
| micro-native-diazoplast-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/diazoplast-uniprot-verify-receipt.json; Actual .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/diazoplast.yaml --verify; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/diazoplast-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Root current-source execution exit0. Current verify covers the three represented Azotobacter accessions and any declared xrefs; it does not prove diazoplast membership. |
| micro-native-diazoplast-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/diazoplast-uniprot-causal-receipt.json; Actual .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/diazoplast.yaml --causal-graphs; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/diazoplast-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Root current-source execution exit0. All categories and total GENE_OR_PROTEIN causal nodes are zero; nitrogenase complex is now STRUCTURE. This check does not assess whole graph biology. |
| micro-record-early_endosome | data/structures/membrane_organelle/early_endosome.yaml; Entire current maintained YAML including definition/history, components/examples, taxa, functions, all graph nodes/edges, discussions and any image | supports | Entire current target independently read at cd5be11ad13304d75404a51d097635022d1bd091. Current bytes match original frozen record input. |
| micro-prior-early_endosome | reviews/structured/20261022T013533Z-early-endosome-audit/review.yaml; Original authoritative YAML and paired Markdown: frozen inputs, scientific assessments, findings/actions, limitations, native check claims and applicability rationale | context_only | Original observation preserved. Original findings/actions empty; qualified source limitations, including lipid-transit uncertainty for whole early endosome, are not silently upgraded. |
| micro-native-early_endosome-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/early_endosome-uniprot-verify-receipt.json; Actual .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/early_endosome.yaml --verify; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/early_endosome-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Root current-source execution exit0. Declared protein-example/xref inventory is empty; zero exit is not biological protein coverage. |
| micro-native-early_endosome-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/early_endosome-uniprot-causal-receipt.json; Actual .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/early_endosome.yaml --causal-graphs; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/early_endosome-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Root current-source execution exit0. All categories and total GENE_OR_PROTEIN causal nodes are zero; nitrogenase complex is now STRUCTURE. This check does not assess whole graph biology. |
| micro-record-early_endosome_lumen | data/structures/membrane_organelle/early_endosome_lumen.yaml; Entire current maintained YAML including definition/history, components/examples, taxa, functions, all graph nodes/edges, discussions and any image | supports | Entire current target independently read at cd5be11ad13304d75404a51d097635022d1bd091. Current bytes match original frozen record input. |
| micro-prior-early_endosome_lumen | reviews/structured/20261022T013534Z-early-endosome-lumen-audit/review.yaml; Original authoritative YAML and paired Markdown: frozen inputs, scientific assessments, findings/actions, limitations, native check claims and applicability rationale | context_only | Original observation preserved. Original findings/actions empty; qualified source limitations, including lipid-transit uncertainty for whole early endosome, are not silently upgraded. |
| micro-native-early_endosome_lumen-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/early_endosome_lumen-uniprot-verify-receipt.json; Actual .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/early_endosome_lumen.yaml --verify; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/early_endosome_lumen-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Root current-source execution exit0. Declared protein-example/xref inventory is empty; zero exit is not biological protein coverage. |
| micro-native-early_endosome_lumen-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/early_endosome_lumen-uniprot-causal-receipt.json; Actual .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/early_endosome_lumen.yaml --causal-graphs; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/early_endosome_lumen-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Root current-source execution exit0. All categories and total GENE_OR_PROTEIN causal nodes are zero; nitrogenase complex is now STRUCTURE. This check does not assess whole graph biology. |
| micro-record-early_endosome_membrane | data/structures/membrane_organelle/early_endosome_membrane.yaml; Entire current maintained YAML including definition/history, components/examples, taxa, functions, all graph nodes/edges, discussions and any image | supports | Entire current target independently read at cd5be11ad13304d75404a51d097635022d1bd091. Current bytes match original frozen record input. |
| micro-prior-early_endosome_membrane | reviews/structured/20261022T013534Z-early-endosome-membrane-audit/review.yaml; Original authoritative YAML and paired Markdown: frozen inputs, scientific assessments, findings/actions, limitations, native check claims and applicability rationale | context_only | Original observation preserved. Original findings/actions empty; qualified source limitations, including lipid-transit uncertainty for whole early endosome, are not silently upgraded. |
| micro-native-early_endosome_membrane-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/early_endosome_membrane-uniprot-verify-receipt.json; Actual .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/early_endosome_membrane.yaml --verify; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/early_endosome_membrane-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Root current-source execution exit0. Declared protein-example/xref inventory is empty; zero exit is not biological protein coverage. |
| micro-native-early_endosome_membrane-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/early_endosome_membrane-uniprot-causal-receipt.json; Actual .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/early_endosome_membrane.yaml --causal-graphs; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/early_endosome_membrane-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Root current-source execution exit0. All categories and total GENE_OR_PROTEIN causal nodes are zero; nitrogenase complex is now STRUCTURE. This check does not assess whole graph biology. |
| micro-context-nitroplast | data/structures/membrane_organelle/nitroplast.yaml; Bounded neighbor fields only: identifier,label,definition,parent/part fields,taxonomic/canonical example and discussions; frozen before reading | context_only | Boundary context only: UCYN-A-derived compartment in a Braarudosphaera host is distinct from Epithemia diazoplast. No full neighbor scientific audit or resolution of its findings. |
| micro-context-reservosome | data/structures/membrane_organelle/reservosome.yaml; Bounded neighbor fields only: identifier,label,definition,parent/part fields,taxonomic/canonical example and discussions; frozen before reading | context_only | Boundary context only: Posterior T.cruzi storage compartment is distinct from the upstream early-endosomal network. No full neighbor scientific audit or resolution of its findings. |
| micro-image-local | data/images/membrane_organelle/diazoplast/pmc11070190_f2.jpg; Entire frozen Figure2 A–C visually viewed in pixels, including12h/24h isotope panels, arrowheads, axes and lower quantification panels | supports | Complete multi-panel NanoSIMS figure matches record caption and native source asset. This is actual pixel inspection, not merely caption reading; no raw numerical data reanalysis. |
| micro-original-validation-inputs | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/adversary-microtubule/original-validation-inputs.json; Four native validate commands and four render --content comparisons; original Git-source and current input SHA checks | supports | All four original pairs validate and render byte-identically. Historical source f97b1abe2d78971b6f66b9083087d7a94cf3c0cc inputs verified. Diazoplast alone stale in this slice; no original artifact rewritten. |
| micro-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005769,GO:0005768,GO:0031901,GO:0031905,GO:0031910,GO:0031904,GO:0010008,GO:0043229,GO:0016020,GO:0016610,GO:0009399; Exact11-ID QuickGO response: definitions, active IDs and relevant typed child links; nitrogenaseGO0016610, fixationGO0009399, membrane/parent and all early-endosome terms | supports | Nitrogenase is a multisubunit complex with dinitrogenase and reductase, appropriate for STRUCTURE rather than a single gene/protein node. Early endosome, its lumen and surrounding bilayer have distinct exact identities; is-a and parthood links support topology. Broad intracellular organelle identity does not assert genetic integration. |
| micro-SL-0094 | https://rest.uniprot.org/locations/SL-0094.json; UniProt native location JSON top-level definition, GO mapping, synonyms and hierarchy, with nested parent context | supports | Exact early-endosome whole organelle and generic sorting scope agrees with GO; no imported universal pH, timing or specific receptor mechanism. |
| micro-SL-0093 | https://rest.uniprot.org/locations/SL-0093.json; UniProt native location JSON top-level definition, GO mapping, synonyms and hierarchy, with nested parent context | supports | Exact early-endosome membrane boundary and synonym scope agrees with GO; no imported universal pH, timing or specific receptor mechanism. |
| micro-SL-0337 | https://rest.uniprot.org/locations/SL-0337.json; UniProt native location JSON top-level definition, GO mapping, synonyms and hierarchy, with nested parent context | supports | Exact early-endosome lumen boundary and synonym scope agrees with GO; no imported universal pH, timing or specific receptor mechanism. |
| micro-tax5693 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5693; Exact ENA taxonomy tax-id response, scientific name, rank and alternate names | supports | Current identity verified: Trypanosoma cruzi species. Taxonomic identity alone is not evidence of compartment occurrence or protein membership. |
| micro-tax420972 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/420972; Exact ENA taxonomy tax-id response, scientific name, rank and alternate names | supports | Current identity verified: Epithemia genus. Taxonomic identity alone is not evidence of compartment occurrence or protein membership. |
| micro-tax3042617 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3042617; Exact ENA taxonomy tax-id response, scientific name, rank and alternate names | supports | Current identity verified: Epithemia clementina (nom. ined.) species. Taxonomic identity alone is not evidence of compartment occurrence or protein membership. |
| micro-tax354 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/354; Exact ENA taxonomy tax-id response, scientific name, rank and alternate names | supports | Current identity verified: Azotobacter vinelandii species. Taxonomic identity alone is not evidence of compartment occurrence or protein membership. |
| micro-tax322710 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/322710; Exact ENA taxonomy tax-id response, scientific name, rank and alternate names | supports | Current identity verified: Azotobacter vinelandii DJ strain. Taxonomic identity alone is not evidence of compartment occurrence or protein membership. |
| micro-protein-C1DK95 | https://rest.uniprot.org/uniprotkb/C1DK95.json; Current exact UniProtKB entry: accession, entry type, protein name, primary/synonym gene names, organism and taxon, cross-reference context | supports | Current accession tuple agrees with record. Unreviewed strain-DJ entry has primary anfH and native nifH synonym; this does not make it an Epithemia protein or prove all examples form one native complex. |
| micro-protein-P07328 | https://rest.uniprot.org/uniprotkb/P07328.json; Current exact UniProtKB entry: accession, entry type, protein name, primary/synonym gene names, organism and taxon, cross-reference context | supports | Current accession tuple agrees with record. Reviewed Azotobacter nifD alpha-chain identity, not an organelle-specific instance. |
| micro-protein-P07329 | https://rest.uniprot.org/uniprotkb/P07329.json; Current exact UniProtKB entry: accession, entry type, protein name, primary/synonym gene names, organism and taxon, cross-reference context | supports | Current accession tuple agrees with record. Reviewed Azotobacter nifK beta-chain identity, not an organelle-specific instance. |
| micro-query-nifD | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=100&amp;query=reviewed%3Atrue%20AND%20gene_exact%3AnifD%20AND%20organism_id%3A354; UniProt first and only response page, native total-results header and no next-page Link; accession/gene/taxon/InterPro fields inspected | supports | The bounded exact-symbol/taxon reviewed query returns the single stated accession, confirming present query uniqueness without broad family absence. |
| micro-query-nifK | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=100&amp;query=reviewed%3Atrue%20AND%20gene_exact%3AnifK%20AND%20organism_id%3A354; UniProt first and only response page, native total-results header and no next-page Link; accession/gene/taxon/InterPro fields inspected | supports | The bounded exact-symbol/taxon reviewed query returns the single stated accession, confirming present query uniqueness without broad family absence. |
| micro-query-hupL | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=100&amp;query=reviewed%3Atrue%20AND%20gene_exact%3AhupL; UniProt first and only response page, native total-results header and no next-page Link; accession/gene/taxon/InterPro fields inspected | supports | Eight reviewed exact-name/synonym hits: six large-subunit proteins carry IPR001501/IPR050867; two hits P26409/P28154 are HypA accessory proteins sharing hupL synonym and are excluded from large-subunit interpretation. Symbol search does not prove identity or exhaustive family specificity. |
| micro-IPR001501 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001501; InterPro exact entry name,type,member models and broad family metadata; descriptions distinguished from primary experimental evidence | supports | Entry covers a broad nickel-dependent/[NiFe]/[NiFeSe] hydrogenase large-subunit family rather than an exact uptake-specific Epithemia equivalog. Family identity supports the bounded grounding limitation, not a proof that no narrower family exists. |
| micro-IPR050867 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050867; InterPro exact entry name,type,member models and broad family metadata; descriptions distinguished from primary experimental evidence | supports | Entry covers a broad nickel-dependent/[NiFe]/[NiFeSe] hydrogenase large-subunit family rather than an exact uptake-specific Epithemia equivalog. IPR050867 description is explicitly marked LLM-generated and not reviewed; it is not used as primary mechanistic proof. |
| micro-moulin2024-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1093/ismeco/ycae055%22; Europe PMC exact DOI core metadata and complete primary abstract; body access separately scoped | supports | Exact bibliographic identity verified. Abstract stronger abolition wording is not substituted for the Results approximately60% reduction. |
| micro-frail2025-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1073/pnas.2507237122%22; Europe PMC exact DOI core metadata and complete primary abstract; body access separately scoped | supports | Exact bibliographic identity verified. Final2025 PNAS paper, not the differently titled2024 preprint. |
| micro-porto2000-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1078/0171-9335-00112%22; Europe PMC exact DOI core metadata and complete primary abstract; body access separately scoped | supports | Exact bibliographic identity verified. Primary abstract directly traces gold-protein cargo through cytostome/cytopharynx, vesicles/tubules and reservosomes; authors propose early-endosome identity from acidic staining and uptake kinetics. It does not establish equivalent lipid-tracer transit. |
| micro-moulin2024-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC11070190.1/PMC11070190.1.xml; Genuine PMC11070190.1 JATS: Introduction sec3, Methods pointer sec4, Results sec6–10, Discussion sec11–15, Figure2 full caption and front licence/author metadata; Fig1/3/4 captions/text only | supports | Primary E.clementina isotope/immunoblot/physiology results support nitrogenase membership, host nitrogen supply and carbon exchange, with nonaxenic model and process-level scope. Daytime darkness/DCMU reduces activity~60%; transport species, respiration mechanism and molecular division/import remain unresolved. CC BY4.0 and Figure2 provenance verified. No claim to inspect Fig1/3/4 pixels, cited studies, raw genomes or quantitative data. |
| micro-moulin2024-supp | https://pmc-oa-opendata.s3.amazonaws.com/PMC11070190.1/ismecomm-supplementals-submitted_ycae055.pdf; Supplementary PDF text: Strain isolation/cultivation (PDFpp1–2), sequencing/phylogeny/metagenomics (pp2–3), Isotope labeling/NanoSIMS and IRMS (pp3–5), TEM/activity assay (pp5–6), Protein extraction/immunoblot through antibody specification (pp6–7); text extraction, not supplement figure pixels | supports | Gazos Creek near Butano model and monoalgal-but-nonaxenic culture confirmed. Isotope workflow separates compartments with morphology/signal-based ROI and recognizes preparation limits; ARA measures culture activity, and immunoblots support NifDK/HupL detection with stated antibody scope. Does not establish localization by immunofluorescence or a hydrogen-flux assay. |
| micro-frail2025-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC12377750.1/PMC12377750.1.xml; Genuine PMC12377750.1 JATS: complete unheaded Introduction, Results s5–7, complete Discussion s8, Methods diazoplast isolation/proteomics s18–19; text/captions only | supports | All-described-Epithemia occurrence and independent diazoplast/nitroplast origins are stated, without genus-wide physiological uniformity. Six enriched host proteins remain localization candidates; TusA undetected and PFK import unsupported. Genetic integration and transport/division hypotheses remain bounded. Did not re-audit complete genome Results s2–4 or supplementary datasets; no image pixels from this paper reviewed. |
| micro-frail2025-supp | https://pmc-oa-opendata.s3.amazonaws.com/PMC12377750.1/pnas.2507237122.sapp.pdf; Supporting Information PDFp2, Generation of axenic culture paragraph; neighboring SEM paragraph read only as context | supports | Later axenic sequencing cultures were derived from initially clonal xenic E.clementina; this is a different study context from Moulin2024 nonaxenic physiology. Other supplement contents were not independently audited. |
| micro-moulin2024-f2 | https://pmc-oa-opendata.s3.amazonaws.com/PMC11070190.1/ycae055f2.jpg; Native PMC11070190.1/ycae055f2.jpg exact asset; SHA256 compared to frozen maintained image and pixels viewed through identical local file | supports | Native asset byte-identical to maintained Figure2: SHA256b8aae76bbe0c1d74896370bae92524c6764ea2795b1ddfa2309c5fc28dc74366; MD5 7141c250f82b9bd5c6a25e546aa7d444 agrees with source object listing. Complete A–C panel and taxon/context attribution preserved. |
| micro-moulin2024-package | https://pmc-oa-opendata.s3.amazonaws.com/?prefix=PMC11070190.1/&amp;max-keys=1000; PMC OA S3 prefix listing PMC11070190.1/, max-keys1000, IsTruncated=false; exact image key,size and ETag | context_only | Native version1 package lists ycae055f2.jpg size102607 and ETag matching computed MD5. Licence authority is article JATS CC BY4.0, not the different Frail2025 licence. |
| micro-porto2000-publisher | https://www.sciencedirect.com/science/article/pii/S0171933504700989; Actual ScienceDirect PII S0171933504700989 HTTP403 access response | context_only | Primary full body not recovered through this route; response is not scientific evidence. |
| micro-porto2000-api | https://api.elsevier.com/content/article/PII:S0171933504700989?httpAccept=text/xml; Actual public Elsevier API response XML, core metadata/openaccess flag; no article body | context_only | API returned HTTP200 bibliographic stub, not readable primary body. The current review remains complete-primary-abstract-only for Porto2000; no strain, methods or figure-pixel check claimed. |
| micro-diazoplast-go-search | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=diazoplast&amp;limit=100&amp;page=1; QuickGO literal query diazoplast, limit100,page1; complete zero-hit response | supports | Bounded current query has zero hits; supports retaining minted identity provisionally together with positive structural/source evidence, not universal ontology absence. |
| micro-catalogue | https://imodulondb.org/api/datasets; Complete official iModulonDB/api/datasets response; every organism ID/name and dataset-array row inspected | supports | No catalogue entry matches Epithemia/diazoplast, Crocosphaera/Cyanothece, Azotobacter or Trypanosoma. Other diazotrophs and Synechococcus are not organism proxies; no matching downstream gene/module query applies. No biological absence or lack-of-expression inference. |
| micro-historical-adapter-runner | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Retained actual00:49Z native datasets attempt, exit1 OS PermissionError reading runner pyvenv.cfg | context_only | Historical runner unavailability retained at its real earlier time; no fresh runner invocation claimed. Actual current catalogue source fallback inspected per native policy. |
| septin-review-policy | .claude/skills/review-yaml-record/SKILL.md; Structured Source Cross-Checks and immutable review contract | supports | Affirmative pathway context triggers applicability assessment even where molecular graph mechanisms are excluded. Expression-only non-inference is not an exemption; unmatched catalogue coverage is not negative biology. |
| septin-curation-policy | docs/CURATION.md; Identity, material components, source scope and evidence | supports | Whole carriers, their constituent membrane bilayers and enclosed regions are distinct. Generic constituent material, subtype-specific coat/cargo and formation machinery are not interchangeable. |
| septin-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; NONMECHANISTIC graphs and scoped evidence | supports | Topological relations and broad transport context may be nonmechanistic; a qualified source experiment does not establish a universal vesicle mechanism. |
| septin-record-cytoplasmic_vesicle | data/structures/membrane_organelle/cytoplasmic_vesicle.yaml; Entire current maintained record at cd5be11ad13304d75404a51d097635022d1bd091 | supports | Read all identity, definition, history, hierarchy, material component, taxon/canonical, function, evidence, graph edges and discussions. No target image, quantitative property, trait link, verbatim snippet or individual protein accession is declared. |
| septin-original-cytoplasmic_vesicle | reviews/structured/20261022T013529Z-cytoplasmic-vesicle-audit/review.yaml; Original YAML and deterministic Markdown; frozen inputs, checks, source tiers, assessments, findings/actions and limits | supports | Original membrane has one minor F1 carrier-versus-bilayer wording finding; whole and lumen have none. Historical global/source claims remain historical. The existing adapter row uses an unsupported expression-only exemption. |
| septin-original-validation-cytoplasmic_vesicle | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/adversary-septin/original-checks.json; 20261022T013529Z-cytoplasmic-vesicle-audit native validate/render and frozen historical/current target hashes | supports | Both native commands exited zero; Markdown matches exactly, and original-source/current hashes equal the frozen target input. |
| septin-native-cytoplasmic_vesicle-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/cytoplasmic_vesicle-uniprot-verify-receipt.json; Actual root command receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/cytoplasmic_vesicle-uniprot-verify.log | supports | Exit zero. No protein examples or UniProtKB graph xrefs and zero GENE_OR_PROTEIN graph nodes. Native execution success covers only this empty represented inventory, not narrative pathway mechanisms, source-localized molecular actors or completeness. |
| septin-native-cytoplasmic_vesicle-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/cytoplasmic_vesicle-uniprot-causal-receipt.json; Actual root command receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/cytoplasmic_vesicle-uniprot-causal.log | supports | Exit zero. No protein examples or UniProtKB graph xrefs and zero GENE_OR_PROTEIN graph nodes. Native execution success covers only this empty represented inventory, not narrative pathway mechanisms, source-localized molecular actors or completeness. |
| septin-record-cytoplasmic_vesicle_lumen | data/structures/membrane_organelle/cytoplasmic_vesicle_lumen.yaml; Entire current maintained record at cd5be11ad13304d75404a51d097635022d1bd091 | supports | Read all identity, definition, history, hierarchy, material component, taxon/canonical, function, evidence, graph edges and discussions. No target image, quantitative property, trait link, verbatim snippet or individual protein accession is declared. |
| septin-original-cytoplasmic_vesicle_lumen | reviews/structured/20261022T013530Z-cytoplasmic-vesicle-lumen-audit/review.yaml; Original YAML and deterministic Markdown; frozen inputs, checks, source tiers, assessments, findings/actions and limits | supports | Original membrane has one minor F1 carrier-versus-bilayer wording finding; whole and lumen have none. Historical global/source claims remain historical. The existing adapter row uses an unsupported expression-only exemption. |
| septin-original-validation-cytoplasmic_vesicle_lumen | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/adversary-septin/original-checks.json; 20261022T013530Z-cytoplasmic-vesicle-lumen-audit native validate/render and frozen historical/current target hashes | supports | Both native commands exited zero; Markdown matches exactly, and original-source/current hashes equal the frozen target input. |
| septin-native-cytoplasmic_vesicle_lumen-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/cytoplasmic_vesicle_lumen-uniprot-verify-receipt.json; Actual root command receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/cytoplasmic_vesicle_lumen-uniprot-verify.log | supports | Exit zero. No protein examples or UniProtKB graph xrefs and zero GENE_OR_PROTEIN graph nodes. Native execution success covers only this empty represented inventory, not narrative pathway mechanisms, source-localized molecular actors or completeness. |
| septin-native-cytoplasmic_vesicle_lumen-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/cytoplasmic_vesicle_lumen-uniprot-causal-receipt.json; Actual root command receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/cytoplasmic_vesicle_lumen-uniprot-causal.log | supports | Exit zero. No protein examples or UniProtKB graph xrefs and zero GENE_OR_PROTEIN graph nodes. Native execution success covers only this empty represented inventory, not narrative pathway mechanisms, source-localized molecular actors or completeness. |
| septin-record-cytoplasmic_vesicle_membrane | data/structures/membrane_organelle/cytoplasmic_vesicle_membrane.yaml; Entire current maintained record at cd5be11ad13304d75404a51d097635022d1bd091 | supports | Read all identity, definition, history, hierarchy, material component, taxon/canonical, function, evidence, graph edges and discussions. No target image, quantitative property, trait link, verbatim snippet or individual protein accession is declared. |
| septin-original-cytoplasmic_vesicle_membrane | reviews/structured/20261022T013531Z-cytoplasmic-vesicle-membrane-audit/review.yaml; Original YAML and deterministic Markdown; frozen inputs, checks, source tiers, assessments, findings/actions and limits | supports | Original membrane has one minor F1 carrier-versus-bilayer wording finding; whole and lumen have none. Historical global/source claims remain historical. The existing adapter row uses an unsupported expression-only exemption. |
| septin-original-validation-cytoplasmic_vesicle_membrane | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/adversary-septin/original-checks.json; 20261022T013531Z-cytoplasmic-vesicle-membrane-audit native validate/render and frozen historical/current target hashes | supports | Both native commands exited zero; Markdown matches exactly, and original-source/current hashes equal the frozen target input. |
| septin-native-cytoplasmic_vesicle_membrane-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/cytoplasmic_vesicle_membrane-uniprot-verify-receipt.json; Actual root command receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/cytoplasmic_vesicle_membrane-uniprot-verify.log | supports | Exit zero. No protein examples or UniProtKB graph xrefs and zero GENE_OR_PROTEIN graph nodes. Native execution success covers only this empty represented inventory, not narrative pathway mechanisms, source-localized molecular actors or completeness. |
| septin-native-cytoplasmic_vesicle_membrane-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/cytoplasmic_vesicle_membrane-uniprot-causal-receipt.json; Actual root command receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/cytoplasmic_vesicle_membrane-uniprot-causal.log | supports | Exit zero. No protein examples or UniProtKB graph xrefs and zero GENE_OR_PROTEIN graph nodes. Native execution success covers only this empty represented inventory, not narrative pathway mechanisms, source-localized molecular actors or completeness. |
| septin-context-cvt_vesicle | data/structures/membrane_organelle/cvt_vesicle.yaml; Boundary fields only: identifier, label, definition, structure_kind, parents, part_of and has_part | supports | Frozen before inspection. Whole Cvt carrier and either surrounding bilayer retain distinct exact identities and correct cytoplasmic-vesicle versus cytoplasmic-vesicle-membrane subtype relations. No whole-neighbor audit or disposition of its findings is asserted. |
| septin-context-cvt_vesicle_membrane | data/structures/membrane_organelle/cvt_vesicle_membrane.yaml; Boundary fields only: identifier, label, definition, structure_kind, parents, part_of and has_part | supports | Frozen before inspection. Whole Cvt carrier and either surrounding bilayer retain distinct exact identities and correct cytoplasmic-vesicle versus cytoplasmic-vesicle-membrane subtype relations. No whole-neighbor audit or disposition of its findings is asserted. |
| septin-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031410,GO:0031982,GO:0030659,GO:0060205,GO:0031983,GO:0016020,GO:0033107,GO:0033110; All eight exact terms: identity, definition, active status, synonyms and relevant typed child relations | supports | GO0031410 whole cytoplasmic vesicle, GO0030659 membrane and GO0060205 lumen are distinct. GO0031983 is the lumen is-a parent. GO0033107 is the whole double-membrane Cvt carrier and GO0033110 is either constituent bilayer; both are correctly subtyped under their corresponding generic classes. The membrane occurrence note conflates those levels. Broader membrane/vesicle definitions remain compatible with asserted hierarchy, without implying every listed parent is an immediate GO edge. |
| septin-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Exact taxId, scientificName, rank and lineage | supports | Taxon4932 is the species Saccharomyces cerevisiae. Species identity does not by itself verify strain, quantitative prevalence or every subtype mechanism. |
| septin-SL0088 | https://rest.uniprot.org/locations/SL-0088.json; Native entry id/name/definition, immediate isA/partOf and nested GO mappings | supports | SL0088 maps exactly to GO0031410, with broader vesicle parentage. Its native prose supports broad secretory/endocytic transport and lists clathrin/COPI/COPII, synaptic, secretory and phagosome subtypes. Such examples do not make all their coats or cargo universal constituents. |
| septin-SL0089 | https://rest.uniprot.org/locations/SL-0089.json; Native entry id/name/definition, immediate isA/partOf and nested GO mappings | supports | SL0089 maps exactly to GO0030659, is_a membrane and part_of cytoplasmic vesicle and endomembrane system. It describes a surrounding membrane, not the complete carrier or a single molecular lipid species. |
| septin-SL0325 | https://rest.uniprot.org/locations/SL-0325.json; Native entry id/name/definition, immediate isA/partOf and nested GO mappings | supports | SL0325 maps exactly to GO0060205 and part_of cytoplasmic vesicle. Its definition supports a membrane-bounded compartment, not a universal cargo list or independent transport function. |
| septin-reggiori2004-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A15004240%20AND%20SRC%3AMED; Complete primary abstract plus exact title/authors/year/DOI/PMID/PMCID and research article type | supports | Cached public-source snapshot fetched during PR2362 and independently reread for this review. Reggiori et al.2004 PMID15004240 DOI10.1091/mbc.e03-07-0479 supports budding-yeast double-membrane Cvt transport and condition-dependent early-secretory contributions, retaining membrane-origin uncertainty. |
| septin-reggiori2004-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC404015/; Cached genuine PMC404015 HTML independently reread: complete Introduction sec1, Methods Strains and Media sec3/Table1, Results sec14/Figure8 text caption, Discussion sec17 and sec18/Figure9 text caption. No full-paper, image-pixel or raw-data audit. | supports | Public body fetched during PR2362 at the retained timestamp; hash verified and reread for current claims. The paper distinguishes double-membrane cytosolic carriers from their bilayers, inner-body release after fusion and cargo delivery. Listed yeast strains and sec12 timing experiments support the canonical example while showing incomplete transport inhibition. ER/Golgi origin remains unresolved; maturation and assembly schemes are models, not universal demonstrated mechanisms. Introductory cited-study synthesis is not new direct evidence from every cited experiment. |
| septin-source-reuse-receipt | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/adversary-septin/reused-source-receipts.json; Retained actual fetch receipts, snapshot paths/hashes and PR2363 reread time | supports | Reggiori metadata actual fetch11:51:54.023844Z and body11:52:44.039650Z are retained; no new fetch is invented. Hashes of both public snapshots were rechecked before current reassessment. |
| septin-catalogue | https://imodulondb.org/api/datasets; Complete official organism list and all returned organism/dataset keys | supports | No matching Saccharomyces cerevisiae/yeast dataset is returned. All three records affirmatively cite Cvt/early-secretory pathway context, even when their graph omits molecular steps. Source applicability is assessed, but downstream unmatched-host gene/module queries are not justified. This is not biological absence. |
| septin-historical-adapter-runner | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Actual historical datasets invocation00:49:00.848907Z–00:49:00.863225Z | context_only | Retained canary invocation exited1 with PermissionError reading pyvenv.cfg. This is historical unavailable-runner evidence, not a new invocation or successful execution. Fresh official catalogue fallback was inspected separately. |
| septin-source-access | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/adversary-septin/source-receipts.json; Actual fresh source URLs, timestamps and hashes | supports | Current GO, three UniProt location entries, ENA taxon and official catalogue fetched successfully. Scientific paper metadata/body are explicitly cached and separately hash-verified/reread; fresh authority access does not imply fresh full-text access. |
| check-qc | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/qc.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| check-labels | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/labels.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| check-trait-links | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/trait-links.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Native TraitMech link check passed. |
| check-vendored | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/vendored.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Pinned governed files match; native vendored check passed. |
| check-curies | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/curies.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| focused | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/focused-results.json; All twenty actual target schema/strict command outputs | supports | Ten schema and ten strict commands returned exit zero. |
| supplemental-pmid | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/pmid-chunks-receipt.json; Complete native-report PMID set checked with unchanged resolver in batches of at most fifty | supports | 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers remain unverified. |
| historical-adapter-runner-availability | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical runner invocation receipt, cross-checked against exact stdout/stderr hashes; reread during PR2363 synthesis | context_only | Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS PermissionError reading the configured runner pyvenv.cfg. This is a retained historical availability observation, not a fresh attempt or a scientific validation failure. Native policy permits inspected source-catalogue fallback. |

## Limits And Additional Notes

- Cyanelle thylakoid, lumen and membrane independent subreview: Three assigned cyanelle thylakoid targets only, all unchanged from original inputs. No extra local neighbor record was used. Existing neighbor/group/category issues, including2675, are not resolved or recertified by this review.
- Cyanelle thylakoid, lumen and membrane independent subreview: Giddings source scope is independently viewed scanned pages409–413 and416–418, including declared text/figures. Pages409/410/412/416/417 and bibliography metadata reuse actual11:52Z PR2362 snapshots; pages411/413/418 were fetched12:28Z. No complete-paper or raw-data reanalysis. Fig19 is a model, not experimental proof; precise PSI localization is explicitly unknown in the paper.
- Cyanelle thylakoid, lumen and membrane independent subreview: Giddings cultured C.paradoxa UTEX LB555 at26C in modified CY-II with continuous illumination. Isolated cyanelles/thylakoids, pigment-removal preparations and thin-section/freeze-fracture/etch microscopy are distinct assays. No complete molecular inventory, universal strain composition, measured live-cell rate or individual formation requirement is inferred.
- Cyanelle thylakoid, lumen and membrane independent subreview: Fresh GO/UniProt sources establish exact structure identity, typed parthood and valid direct/broader parents. Native schema coarse whole-organelle granularity explicitly includes thylakoids; this is not a separate GO is_a organelle claim. COMMON describes qualitative occurrence, not a prevalence estimate.
- Cyanelle thylakoid, lumen and membrane independent subreview: Whole thylakoid and membrane assert light-reaction pathway context and require structured-source applicability correction. Lumen is genuinely topology-only and excluded; missing proteins are not fabricated as defects. Catalogue lacks a matching glaucophyte host; no matched downstream gene/module query or cyanobacterial substitution is justified.
- Cyanelle thylakoid, lumen and membrane independent subreview: Historical00:49Z PermissionError runner failure remains an earlier unavailable check, not a new invocation or success. Fresh official catalogue and source-scoped literature/authority checks are distinct fallback evidence.
- Cyanelle thylakoid, lumen and membrane independent subreview: All six native protein checks pass empty inventories and zero GENE_OR_PROTEIN nodes; this does not independently prove biological function or necessity. Root owns global gates, issue filing and all repository/GitHub mutations.
- Diazoplast and early-endosome trio independent subreview: Diazoplast/early-endosome independent slice: Four complete targets and original pairs reviewed; neighbors nitroplast/reservosome read only at frozen boundary/taxon/discussion fields. No neighbor/category/group issue resolved; #2404 history is not a disposition of its full predecessor.
- Diazoplast and early-endosome trio independent subreview: Diazoplast source scope: Moulin Introduction/Results/Discussion and stated supplementary methods inspected; only maintained Figure2 pixels viewed. Other figures were read as captions/text only. Frail body scope is Introduction,Results s5–7,Discussion s8,Methods s18–19; SI only axenic-culture paragraph plus neighboring context. No full genome/proteomics/raw-data audit or supplemental figure inspection.
- Diazoplast and early-endosome trio independent subreview: Diazoplast source scope: Imaging, biochemical detection, culture activity and enrichment do not establish every molecule necessity, exhaustive composition or host-protein import. HupL family search includes two synonym-collision accessory proteins, excluded from large-subunit interpretation; InterPro IPR050867 generated description is not primary evidence.
- Diazoplast and early-endosome trio independent subreview: Early-endosome source scope: Porto2000 complete primary abstract plus metadata only; ScienceDirect403 and public API metadata stub do not provide body/methods/strain/figure evidence. Protein routing supported; lipid-specific routing remains unknown, neither confirmed nor contradicted. Source authors proposed early-endosome identity using uptake kinetics and acidity, not a molecular marker.
- Diazoplast and early-endosome trio independent subreview: Diazoplast/early-endosome source scope: All four assert named molecular or pathway context requiring applicability assessment despite nonmolecular topology nodes. Fresh complete public catalogue has no matching organism/dataset; no downstream module query or biological absence conclusion. Actual native runner failure remains historical00:49Z, not a fresh attempt.
- Diazoplast and early-endosome trio independent subreview: Diazoplast/early-endosome native-check scope: Eight commands returned0; diazoplast verify checks three represented accession examples, other inventories empty; all causal typed-protein inventories zero after complex retyping. Schema/protein validators do not resolve membership or scientifically validate graph edges. Root owns full-corpus gates, issue dedup, final CI and queue; no future result borrowed.
- Cytoplasmic vesicle, lumen and membrane independent subreview: All three current targets match original frozen and historical-source hashes. Membrane F1 retains its exact original issue key and occurrence; whole/lumen original finding lists were empty. No newly invented predecessor or terminal disposition.
- Cytoplasmic vesicle, lumen and membrane independent subreview: Reggiori2004 public-source metadata and genuine HTML were fetched during PR2362 at actual11:51:54.023844Z and11:52:44.039650Z. Hashes were checked and bodies independently reread here. Current scope is complete abstract, Introduction sec1, Strains/Media sec3/Table1, Results sec14/Figure8 text, Discussion sec17 and18/Figure9 text only; no fresh paper fetch, complete article, figure pixels or raw-data reanalysis claimed.
- Cytoplasmic vesicle, lumen and membrane independent subreview: Primary intro/discussion includes prior-study synthesis and proposed models. Conditional sec12/sec7 experiments do not establish an exclusive ER/Golgi donor, universal vesicle formation mechanism or quantitative COMMON prevalence. Cvt subtype evidence is not a universal molecular census.
- Cytoplasmic vesicle, lumen and membrane independent subreview: Native six commands pass with no protein examples/xrefs and zero GENE_OR_PROTEIN nodes. This empty-inventory result does not independently validate narrative pathways, molecular actors, localization or composition. Collective bilayer constitution does not prove individual lipid necessity.
- Cytoplasmic vesicle, lumen and membrane independent subreview: All three records affirmatively cite Cvt/early-secretory pathway context despite geometry-focused graphs; their original expression-only exemptions need correction. Current complete catalogue lacks yeast coverage. No unmatched-host query or biological absence inference; runner failure remains actual historical00:49Z, not a new run.
- Cytoplasmic vesicle, lumen and membrane independent subreview: Two frozen Cvt neighbors were read at boundary fields only. No independent full-neighbor review, protein example audit or resolution of their findings is asserted. No target image, measurement, trait link or verbatim snippet is declared.
- Cytoplasmic vesicle, lumen and membrane independent subreview: Root owns full-cohort QC, issue deduplication/publication, repository/GitHub mutations and final-head/queue CI. The review-only scope leaves scientific record curation separate.
- Historical observations remain immutable; their old checks are not represented as current-head execution.
- The adapter runner was not rerun after the canary established OS access failure. Catalogue-based coverage is assessed directly; fresh and reused responses retain actual access timestamps.
- Native label checks include 923 no-adapter skips. Native identifier checks include 909 PMID transport failures and 254 skipped identifiers; bounded supplemental checks independently resolve the 909 PMIDs.
- Scientific record-curation findings stay in separate issues; no record is edited by this review PR.
- Final trusted-base post-save review-check, exact-head independent acceptance, final-head CI and merge-group CI occur after saving this immutable observation and are not represented here as already completed.
- All ten original YAML/Markdown pairs remain unchanged. Current main was merged normally and pushed without force.
- This explicit issue-bearing ten-record cohort follows the native persistence policy. Both inherited scientific findings retain their stable issue keys and exact predecessor repository/review/finding identities.
- Issue #2676 tracks the stale diazoplast target: a history entry and nitrogenase-complex node retyping from GENE_OR_PROTEIN to STRUCTURE. Current authority and native node-type policy support the complex-structure interpretation. The closed grouped #2404 is historical context; no other group target or finding is disposed of here.
- Issue #2677 tracks nine applicability defects: cyanelle thylakoid and its membrane assert light reactions; the three cytoplasmic-vesicle records assert Cvt/early-secretory context; diazoplast asserts nitrogen fixation and molecular examples; the early-endosome trio asserts endocytic cargo-routing context. Thylakoid lumen remains a genuine topology-only exclusion with molecular transport and lumen proteins withheld.
- Source commit cd5be11ad13304d75404a51d097635022d1bd091 is retained by tag review-base/pr2363-current-record-followup-20261103.
- CLAUDE.md is an alias of AGENTS.md; canonical regular AGENTS.md bytes are frozen.
- All 52 used local inputs were frozen before assessment, including four neighbor records, the actual diazoplast image, native configuration, graph/protein policies and verifier source. Neighbors are boundary context only, not additional targets or dispositions of their findings.
- Fresh and reused public-source snapshots retain actual access dates and inspection tiers. Authority identity does not independently establish structure membership, mechanistic action, species-wide generalization or assembly necessity.
- All twenty native protein commands returned zero. Diazoplast has three verified Azotobacter protein examples, while its retyped nitrogenase complex is no longer a GENE_OR_PROTEIN node; typed molecular graph coverage is therefore zero. The other nine targets have empty protein inventories and zero typed molecular nodes. Those results do not validate narrative molecules, pathway claims or Epithemia diazoplast membership.
- The inherited cytoplasmic-vesicle membrane finding distinguishes either Cvt bilayer from the complete double-membrane carrier. The inherited diazoplast finding distinguishes valid cross-taxon accession identities from the ProteinExample requirement for organism-specific structure membership. Retyping the complex does not resolve that placement defect.
- The actual frozen diazoplast Figure 2, its source, caption, taxon, NanoSIMS/quantification scope and CC BY 4.0 licence are assessed. Isotope enrichment supports the bounded exchange interpretation without establishing arbitrary protein membership.
- Current whole-cyanelle issue #2675 concerns an anatomical evidence note in a distinct record and is not resolved here. The source model uncertainty about precise photosystem localization is not converted into an asserted thylakoid mechanism.
- The two minor scientific findings remain open for separately authorized record curation: #2678 for the membrane wording and #2679 for diazoplast cross-taxon protein-example placement. Eight other targets retain qualified positive scientific assessments. No record is edited.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T123523Z-pr2363-current-record-followup
kind: batch
repository: CultureBotAI/CellStructureMech
title: 'PR 2363: current-input review of ten records and adversarial follow-up'
started_at: '2026-11-03T12:26:56.169916Z'
finished_at: '2026-11-03T12:35:23Z'
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
summary: Current-input reassessment of all ten records in PR2363. One stale diazoplast
  review is substantively refreshed and nine structured-source applicability assessments
  are corrected. Two inherited minor scientific findings remain open for separate
  curation; no records are edited.
source:
  git_revision: cd5be11ad13304d75404a51d097635022d1bd091
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
  - path: data/images/membrane_organelle/diazoplast/pmc11070190_f2.jpg
    sha256: b8aae76bbe0c1d74896370bae92524c6764ea2795b1ddfa2309c5fc28dc74366
    role: context
  - path: data/structures/membrane_organelle/cvt_vesicle.yaml
    sha256: cf6eb5075a057a0b8b104cbacb61cdf895298eb4b018945a08b46bcb939c8b0c
    role: context
  - path: data/structures/membrane_organelle/cvt_vesicle_membrane.yaml
    sha256: 679cdeb18f93b2ecf38916c132f8461121e7067f0db52e4b24842559b39dbb67
    role: context
  - path: data/structures/membrane_organelle/cyanelle_thylakoid.yaml
    sha256: 19838578792948bb527b33a0dd61374b6ee7a688eb2ee0406426c2e95639c7e3
    role: target
  - path: data/structures/membrane_organelle/cyanelle_thylakoid_lumen.yaml
    sha256: 6dc48d3d810b7a63387502082d26502265a7f12eafec88058eb9e5d8be70a205
    role: target
  - path: data/structures/membrane_organelle/cyanelle_thylakoid_membrane.yaml
    sha256: c1c3958038a4f3a20735ce33206475130078e9a12048dcbeff4bc0d04beb4178
    role: target
  - path: data/structures/membrane_organelle/cytoplasmic_vesicle.yaml
    sha256: f4704b74324c18cab955983a27173d6a98fae0153bc7a403cbbe3c865e4eba84
    role: target
  - path: data/structures/membrane_organelle/cytoplasmic_vesicle_lumen.yaml
    sha256: 87d5a5379cb643e40257e60c99a3308f2b6e6a49aa079856fb501fe6e3c738fe
    role: target
  - path: data/structures/membrane_organelle/cytoplasmic_vesicle_membrane.yaml
    sha256: 112643d19f662095c8d81c907d5d6435fe93b612f8a037df2af0fe66af87d4aa
    role: target
  - path: data/structures/membrane_organelle/diazoplast.yaml
    sha256: fd3948e827eb4a9870bc4eccb09689dd5c82f5caef443f1e319daabbf21bb038
    role: target
  - path: data/structures/membrane_organelle/early_endosome.yaml
    sha256: ed91f355f5faca2b5bd7af5036740c6d6034d783fcfa0252aeb533489c6a46a9
    role: target
  - path: data/structures/membrane_organelle/early_endosome_lumen.yaml
    sha256: fe21c86defd34e34c5df67ec7bc0e7be16cc0342f2b10c6bae2ffd9569060290
    role: target
  - path: data/structures/membrane_organelle/early_endosome_membrane.yaml
    sha256: 2d96c5c692f3e324e718d1fc2750703c41060a9ef56dd535cd55831da69354dc
    role: target
  - path: data/structures/membrane_organelle/nitroplast.yaml
    sha256: 3f7dc36b6c5e8389c881e64839227e1e5cdde49edb55277e245b180f0de8d6a8
    role: context
  - path: data/structures/membrane_organelle/reservosome.yaml
    sha256: c1a9daf798668ddf44d05a61e4ef589754275f4d385f1560ce38ccab0c07cdfa
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
  - path: reviews/structured/20261022T013526Z-cyanelle-thylakoid-audit/review.md
    sha256: ca21255fc10092759a32d3ff36337038b8711fabaf7e0b99e0a62013fb66b741
    role: context
  - path: reviews/structured/20261022T013526Z-cyanelle-thylakoid-audit/review.yaml
    sha256: 8d9f4f24970a0efde884021a112099b570e956b8cb1b64eb3d8e4d891e285ea2
    role: context
  - path: reviews/structured/20261022T013527Z-cyanelle-thylakoid-lumen-audit/review.md
    sha256: 281405740428e7ea502ef42fafc4fc9ef2cce65359083015ad834c67daeb43d5
    role: context
  - path: reviews/structured/20261022T013527Z-cyanelle-thylakoid-lumen-audit/review.yaml
    sha256: 13a7502831d4a4b2f9b06fc5530ef478c2ee33867988f2c8337a3bb55070b516
    role: context
  - path: reviews/structured/20261022T013528Z-cyanelle-thylakoid-membrane-audit/review.md
    sha256: f06de589260a3146491b7fdbdd014b6fcced862c5a9320732d9bb7ba27ecf2c5
    role: context
  - path: reviews/structured/20261022T013528Z-cyanelle-thylakoid-membrane-audit/review.yaml
    sha256: 76a0977412a28cf2baa50929fe1707f5749155f170bde412acca91e6ea49c286
    role: context
  - path: reviews/structured/20261022T013529Z-cytoplasmic-vesicle-audit/review.md
    sha256: d86b94d4a38fe9c1f07e44f6f3391c2c7268c8af59c11ba9aec020780bfc5f72
    role: context
  - path: reviews/structured/20261022T013529Z-cytoplasmic-vesicle-audit/review.yaml
    sha256: 28e7e5777617f9550a87a3e10115a2d76c6839cc0b1ea0d65968f27a1a747d27
    role: context
  - path: reviews/structured/20261022T013530Z-cytoplasmic-vesicle-lumen-audit/review.md
    sha256: 6d272bd0e13f06b94805ef9d3f6ca64c6b8888298337a41fb2301e9df98e8326
    role: context
  - path: reviews/structured/20261022T013530Z-cytoplasmic-vesicle-lumen-audit/review.yaml
    sha256: 7cd480b7fd9a364ecae7d01c4f95bb8a64fae0577c237fb847140ca506cd3297
    role: context
  - path: reviews/structured/20261022T013531Z-cytoplasmic-vesicle-membrane-audit/review.md
    sha256: b145b02468b675c23118e9b6c36729c9b04ce3a882dd74e81fde6bcd19d863d6
    role: context
  - path: reviews/structured/20261022T013531Z-cytoplasmic-vesicle-membrane-audit/review.yaml
    sha256: bca15f1dfaa8c49be3a41da7df6e1c09d0c6cf1b59979f21ea033d9be5756d39
    role: context
  - path: reviews/structured/20261022T013532Z-diazoplast-audit/review.md
    sha256: f2d9071238244ed3c582599f4403dcd6d7f548a5e73037bfb2fb6f3ecda6fd52
    role: context
  - path: reviews/structured/20261022T013532Z-diazoplast-audit/review.yaml
    sha256: a90cd1c474f3d57bc8a5676a03bbee5664c89152a0550821996989b8a381fe3c
    role: context
  - path: reviews/structured/20261022T013533Z-early-endosome-audit/review.md
    sha256: 0121d0e8b1059353aba7a85f7d1cecd0c146cddadfa410605f2ea8654f7e2b1e
    role: context
  - path: reviews/structured/20261022T013533Z-early-endosome-audit/review.yaml
    sha256: 0171636452cfeeec065d1c4502ab93239c402f667fa0fc2f841f8e633a97e7cc
    role: context
  - path: reviews/structured/20261022T013534Z-early-endosome-lumen-audit/review.md
    sha256: f25ece765f482af88d9d9f3a5f3cd6a8867221d9dbd63adbf8a1ce3bd62df7d5
    role: context
  - path: reviews/structured/20261022T013534Z-early-endosome-lumen-audit/review.yaml
    sha256: a7450853bc9a7f4640e2686af2e22fd1ee2ab5ceca83dd7fd1817efc039df898
    role: context
  - path: reviews/structured/20261022T013534Z-early-endosome-membrane-audit/review.md
    sha256: 52f0b62f0af0352cb4079d3f4a2f062dbef645f476ef4b48f5f7e0bad188105e
    role: context
  - path: reviews/structured/20261022T013534Z-early-endosome-membrane-audit/review.yaml
    sha256: ba11e4fd120f6d681e845a98d80bc970238961fef7caee92acbc98a1e5bbcb1d
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
- target_id: GO:0009843
  path: data/structures/membrane_organelle/cyanelle_thylakoid.yaml
  label: cyanelle thylakoid
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/cyanelle_thylakoid.yaml
    role: maintained scientific record
- target_id: GO:0033114
  path: data/structures/membrane_organelle/cyanelle_thylakoid_lumen.yaml
  label: cyanelle thylakoid lumen
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/cyanelle_thylakoid_lumen.yaml
    role: maintained scientific record
- target_id: GO:0033115
  path: data/structures/membrane_organelle/cyanelle_thylakoid_membrane.yaml
  label: cyanelle thylakoid membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/cyanelle_thylakoid_membrane.yaml
    role: maintained scientific record
- target_id: GO:0031410
  path: data/structures/membrane_organelle/cytoplasmic_vesicle.yaml
  label: cytoplasmic vesicle
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/cytoplasmic_vesicle.yaml
    role: maintained scientific record
- target_id: GO:0060205
  path: data/structures/membrane_organelle/cytoplasmic_vesicle_lumen.yaml
  label: cytoplasmic vesicle lumen
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/cytoplasmic_vesicle_lumen.yaml
    role: maintained scientific record
- target_id: GO:0030659
  path: data/structures/membrane_organelle/cytoplasmic_vesicle_membrane.yaml
  label: cytoplasmic vesicle membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/cytoplasmic_vesicle_membrane.yaml
    role: maintained scientific record
- target_id: cellstructuremech:diazoplast
  path: data/structures/membrane_organelle/diazoplast.yaml
  label: diazoplast
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/diazoplast.yaml
    role: maintained scientific record
- target_id: GO:0005769
  path: data/structures/membrane_organelle/early_endosome.yaml
  label: early endosome
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/early_endosome.yaml
    role: maintained scientific record
- target_id: GO:0031905
  path: data/structures/membrane_organelle/early_endosome_lumen.yaml
  label: early endosome lumen
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/early_endosome_lumen.yaml
    role: maintained scientific record
- target_id: GO:0031901
  path: data/structures/membrane_organelle/early_endosome_membrane.yaml
  label: early endosome membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/early_endosome_membrane.yaml
    role: maintained scientific record
scope:
  description: Exact ten-record PR cohort reassessed against current main a961bb84a278a52cb08f9e5494240141ca8b1a76.
    Changed inputs are substantively reassessed. Scientific records remain unchanged.
  selection: Complete cohort of ten maintained records reviewed in original PR head
    2282587034c1b0aa06edc6feeb558aca9e46f546.
  coverage: full
  population_size: 10
  reviewed_target_ids:
  - GO:0009843
  - GO:0033114
  - GO:0033115
  - GO:0031410
  - GO:0060205
  - GO:0030659
  - cellstructuremech:diazoplast
  - GO:0005769
  - GO:0031905
  - GO:0031901
checks:
- check_id: qc
  name: Full native QC
  status: passed
  required: true
  target_ids:
  - GO:0009843
  - GO:0033114
  - GO:0033115
  - GO:0031410
  - GO:0060205
  - GO:0030659
  - cellstructuremech:diazoplast
  - GO:0005769
  - GO:0031905
  - GO:0031901
  command: just qc
  exit_code: 0
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  scope_note: Actual local execution at main-merge head cd5be11ad13304d75404a51d097635022d1bd091.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-qc
- check_id: labels
  name: Native label correspondence
  status: passed
  required: true
  target_ids:
  - GO:0009843
  - GO:0033114
  - GO:0033115
  - GO:0031410
  - GO:0060205
  - GO:0030659
  - cellstructuremech:diazoplast
  - GO:0005769
  - GO:0031905
  - GO:0031901
  command: just validate-products
  exit_code: 0
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  scope_note: Actual local execution at main-merge head cd5be11ad13304d75404a51d097635022d1bd091.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-labels
- check_id: trait-links
  name: TraitMech references
  status: passed
  required: true
  target_ids:
  - GO:0009843
  - GO:0033114
  - GO:0033115
  - GO:0031410
  - GO:0060205
  - GO:0030659
  - cellstructuremech:diazoplast
  - GO:0005769
  - GO:0031905
  - GO:0031901
  command: just check-trait-links --check
  exit_code: 0
  summary: Native TraitMech link check passed.
  scope_note: Actual local execution at main-merge head cd5be11ad13304d75404a51d097635022d1bd091.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-trait-links
- check_id: vendored
  name: Pinned governed files
  status: passed
  required: true
  target_ids:
  - GO:0009843
  - GO:0033114
  - GO:0033115
  - GO:0031410
  - GO:0060205
  - GO:0030659
  - cellstructuremech:diazoplast
  - GO:0005769
  - GO:0031905
  - GO:0031901
  command: just vendored-check
  exit_code: 0
  summary: Pinned governed files match; native vendored check passed.
  scope_note: Actual local execution at main-merge head cd5be11ad13304d75404a51d097635022d1bd091.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-vendored
- check_id: curies
  name: Native identifier resolver
  status: passed
  required: true
  target_ids:
  - GO:0009843
  - GO:0033114
  - GO:0033115
  - GO:0031410
  - GO:0060205
  - GO:0030659
  - cellstructuremech:diazoplast
  - GO:0005769
  - GO:0031905
  - GO:0031901
  command: just check-curies
  exit_code: 0
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  scope_note: Actual local execution at main-merge head cd5be11ad13304d75404a51d097635022d1bd091.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-curies
- check_id: focused-0
  name: validate GO:0009843
  status: passed
  required: true
  target_ids:
  - GO:0009843
  command: just validate data/structures/membrane_organelle/cyanelle_thylakoid.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-1
  name: validate-strict GO:0009843
  status: passed
  required: true
  target_ids:
  - GO:0009843
  command: just validate-strict data/structures/membrane_organelle/cyanelle_thylakoid.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-2
  name: validate GO:0033114
  status: passed
  required: true
  target_ids:
  - GO:0033114
  command: just validate data/structures/membrane_organelle/cyanelle_thylakoid_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-3
  name: validate-strict GO:0033114
  status: passed
  required: true
  target_ids:
  - GO:0033114
  command: just validate-strict data/structures/membrane_organelle/cyanelle_thylakoid_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-4
  name: validate GO:0033115
  status: passed
  required: true
  target_ids:
  - GO:0033115
  command: just validate data/structures/membrane_organelle/cyanelle_thylakoid_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-5
  name: validate-strict GO:0033115
  status: passed
  required: true
  target_ids:
  - GO:0033115
  command: just validate-strict data/structures/membrane_organelle/cyanelle_thylakoid_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-6
  name: validate GO:0031410
  status: passed
  required: true
  target_ids:
  - GO:0031410
  command: just validate data/structures/membrane_organelle/cytoplasmic_vesicle.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-7
  name: validate-strict GO:0031410
  status: passed
  required: true
  target_ids:
  - GO:0031410
  command: just validate-strict data/structures/membrane_organelle/cytoplasmic_vesicle.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-8
  name: validate GO:0060205
  status: passed
  required: true
  target_ids:
  - GO:0060205
  command: just validate data/structures/membrane_organelle/cytoplasmic_vesicle_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-9
  name: validate-strict GO:0060205
  status: passed
  required: true
  target_ids:
  - GO:0060205
  command: just validate-strict data/structures/membrane_organelle/cytoplasmic_vesicle_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-10
  name: validate GO:0030659
  status: passed
  required: true
  target_ids:
  - GO:0030659
  command: just validate data/structures/membrane_organelle/cytoplasmic_vesicle_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-11
  name: validate-strict GO:0030659
  status: passed
  required: true
  target_ids:
  - GO:0030659
  command: just validate-strict data/structures/membrane_organelle/cytoplasmic_vesicle_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-12
  name: validate cellstructuremech:diazoplast
  status: passed
  required: true
  target_ids:
  - cellstructuremech:diazoplast
  command: just validate data/structures/membrane_organelle/diazoplast.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-13
  name: validate-strict cellstructuremech:diazoplast
  status: passed
  required: true
  target_ids:
  - cellstructuremech:diazoplast
  command: just validate-strict data/structures/membrane_organelle/diazoplast.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-14
  name: validate GO:0005769
  status: passed
  required: true
  target_ids:
  - GO:0005769
  command: just validate data/structures/membrane_organelle/early_endosome.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-15
  name: validate-strict GO:0005769
  status: passed
  required: true
  target_ids:
  - GO:0005769
  command: just validate-strict data/structures/membrane_organelle/early_endosome.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-16
  name: validate GO:0031905
  status: passed
  required: true
  target_ids:
  - GO:0031905
  command: just validate data/structures/membrane_organelle/early_endosome_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-17
  name: validate-strict GO:0031905
  status: passed
  required: true
  target_ids:
  - GO:0031905
  command: just validate-strict data/structures/membrane_organelle/early_endosome_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-18
  name: validate GO:0031901
  status: passed
  required: true
  target_ids:
  - GO:0031901
  command: just validate data/structures/membrane_organelle/early_endosome_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-19
  name: validate-strict GO:0031901
  status: passed
  required: true
  target_ids:
  - GO:0031901
  command: just validate-strict data/structures/membrane_organelle/early_endosome_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: supplemental-pmid
  name: Supplemental bounded PMID authority checks
  status: passed
  required: true
  target_ids:
  - GO:0009843
  - GO:0033114
  - GO:0033115
  - GO:0031410
  - GO:0060205
  - GO:0030659
  - cellstructuremech:diazoplast
  - GO:0005769
  - GO:0031905
  - GO:0031901
  command: .venv/bin/python /private/tmp/cellstructure-batches-2346-2397-20261103/check_pmid_chunks.py
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363
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
  - GO:0009843
  - GO:0033114
  - GO:0033115
  - GO:0031410
  - GO:0060205
  - GO:0030659
  - cellstructuremech:diazoplast
  - GO:0005769
  - GO:0031905
  - GO:0031901
  summary: 'Nine unsupported applicability exclusions are corrected: whole cyanelle
    thylakoid and membrane light-reaction context, the cytoplasmic-vesicle trio Cvt/early-secretory
    context, diazoplast nitrogen fixation/molecular examples, and the early-endosome
    trio endocytic cargo-routing context. Cyanelle thylakoid lumen remains a genuine
    topology-only exclusion with proton transport and lumen protein assertions withheld.
    Complete official catalogue coverage has no matching relevant Cyanophora, yeast,
    Epithemia, Crocosphaera, Azotobacter or Trypanosoma dataset. No unrelated organism
    proxy or downstream query substitutes for noncoverage. Resource noncoverage is
    not biological absence; the historical runner failure is not a fresh invocation.'
  evidence_ids:
  - plaque-catalogue
  - plaque-historical-runner
  - micro-catalogue
  - septin-catalogue
- check_id: independent-scientific-review
  name: Independent claim-level source review
  status: passed
  required: true
  target_ids:
  - GO:0009843
  - GO:0033114
  - GO:0033115
  - GO:0031410
  - GO:0060205
  - GO:0030659
  - cellstructuremech:diazoplast
  - GO:0005769
  - GO:0031905
  - GO:0031901
  summary: Three read-only reviewers covered the complete ten-record cohort, including
    changed inputs, with explicit scientific findings and source-access limits. Final
    artifact/head acceptance occurs after saving.
  evidence_ids:
  - plaque-policy
  - plaque-rubric
  - plaque-graph-policy
  - plaque-schema-policy
  - plaque-thylakoid-agent-go
  - plaque-thylakoid-agent-SL-0277
  - plaque-thylakoid-agent-SL-0084
  - plaque-thylakoid-agent-SL-0085
  - plaque-cached-tax2762
  - plaque-cached-tax38254
  - plaque-cached-giddings1983-meta
  - plaque-cached-giddings1983-page409
  - plaque-cached-giddings1983-page410
  - plaque-thylakoid-agent-giddings1983-page411
  - plaque-cached-giddings1983-page412
  - plaque-thylakoid-agent-giddings1983-page413
  - plaque-cached-giddings1983-page416
  - plaque-cached-giddings1983-page417
  - plaque-thylakoid-agent-giddings1983-page418
  - plaque-catalogue
  - micro-policy
  - micro-schema-protein-example
  - micro-go
  - micro-SL-0094
  - micro-SL-0093
  - micro-SL-0337
  - micro-tax5693
  - micro-tax420972
  - micro-tax3042617
  - micro-tax354
  - micro-tax322710
  - micro-protein-C1DK95
  - micro-protein-P07328
  - micro-protein-P07329
  - micro-IPR001501
  - micro-IPR050867
  - micro-moulin2024-meta
  - micro-frail2025-meta
  - micro-porto2000-meta
  - micro-moulin2024-jats
  - micro-moulin2024-supp
  - micro-frail2025-jats
  - micro-frail2025-supp
  - micro-moulin2024-f2
  - micro-moulin2024-package
  - micro-porto2000-publisher
  - micro-porto2000-api
  - septin-review-policy
  - septin-curation-policy
  - septin-graph-policy
  - septin-go
  - septin-tax4932
  - septin-SL0088
  - septin-SL0089
  - septin-SL0325
  - septin-reggiori2004-meta
  - septin-reggiori2004-pmc
- check_id: historical-adapter-runner
  name: Retained historical adapter runner availability
  status: unavailable
  required: false
  target_ids:
  - GO:0009843
  - GO:0033115
  - GO:0031410
  - GO:0060205
  - GO:0030659
  - cellstructuremech:diazoplast
  - GO:0005769
  - GO:0031905
  - GO:0031901
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
- check_id: cyanelle_thylakoid-uniprot-verify
  name: Native cyanelle thylakoid UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0009843
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_thylakoid.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Represented protein inventory and
    typed GENE_OR_PROTEIN graph coverage are empty. This does not validate narrative
    molecules, pathways or source scope.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-cyanelle_thylakoid-verify
- check_id: cyanelle_thylakoid-uniprot-causal
  name: Native cyanelle thylakoid UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0009843
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_thylakoid.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Represented protein inventory and
    typed GENE_OR_PROTEIN graph coverage are empty. This does not validate narrative
    molecules, pathways or source scope.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-cyanelle_thylakoid-causal
- check_id: cyanelle_thylakoid_lumen-uniprot-verify
  name: Native cyanelle thylakoid lumen UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0033114
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_thylakoid_lumen.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Represented protein inventory and
    typed GENE_OR_PROTEIN graph coverage are empty. This does not validate narrative
    molecules, pathways or source scope.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-cyanelle_thylakoid_lumen-verify
- check_id: cyanelle_thylakoid_lumen-uniprot-causal
  name: Native cyanelle thylakoid lumen UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0033114
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_thylakoid_lumen.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Represented protein inventory and
    typed GENE_OR_PROTEIN graph coverage are empty. This does not validate narrative
    molecules, pathways or source scope.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-cyanelle_thylakoid_lumen-causal
- check_id: cyanelle_thylakoid_membrane-uniprot-verify
  name: Native cyanelle thylakoid membrane UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0033115
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_thylakoid_membrane.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Represented protein inventory and
    typed GENE_OR_PROTEIN graph coverage are empty. This does not validate narrative
    molecules, pathways or source scope.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-cyanelle_thylakoid_membrane-verify
- check_id: cyanelle_thylakoid_membrane-uniprot-causal
  name: Native cyanelle thylakoid membrane UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0033115
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_thylakoid_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Represented protein inventory and
    typed GENE_OR_PROTEIN graph coverage are empty. This does not validate narrative
    molecules, pathways or source scope.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-cyanelle_thylakoid_membrane-causal
- check_id: cytoplasmic_vesicle-uniprot-verify
  name: Native cytoplasmic vesicle UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0031410
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cytoplasmic_vesicle.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Represented protein inventory and
    typed GENE_OR_PROTEIN graph coverage are empty. This does not validate narrative
    molecules, pathways or source scope.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-cytoplasmic_vesicle-verify
- check_id: cytoplasmic_vesicle-uniprot-causal
  name: Native cytoplasmic vesicle UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0031410
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cytoplasmic_vesicle.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Represented protein inventory and
    typed GENE_OR_PROTEIN graph coverage are empty. This does not validate narrative
    molecules, pathways or source scope.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-cytoplasmic_vesicle-causal
- check_id: cytoplasmic_vesicle_lumen-uniprot-verify
  name: Native cytoplasmic vesicle lumen UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0060205
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cytoplasmic_vesicle_lumen.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Represented protein inventory and
    typed GENE_OR_PROTEIN graph coverage are empty. This does not validate narrative
    molecules, pathways or source scope.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-cytoplasmic_vesicle_lumen-verify
- check_id: cytoplasmic_vesicle_lumen-uniprot-causal
  name: Native cytoplasmic vesicle lumen UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0060205
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cytoplasmic_vesicle_lumen.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Represented protein inventory and
    typed GENE_OR_PROTEIN graph coverage are empty. This does not validate narrative
    molecules, pathways or source scope.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-cytoplasmic_vesicle_lumen-causal
- check_id: cytoplasmic_vesicle_membrane-uniprot-verify
  name: Native cytoplasmic vesicle membrane UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0030659
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cytoplasmic_vesicle_membrane.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Represented protein inventory and
    typed GENE_OR_PROTEIN graph coverage are empty. This does not validate narrative
    molecules, pathways or source scope.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-cytoplasmic_vesicle_membrane-verify
- check_id: cytoplasmic_vesicle_membrane-uniprot-causal
  name: Native cytoplasmic vesicle membrane UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0030659
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cytoplasmic_vesicle_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Represented protein inventory and
    typed GENE_OR_PROTEIN graph coverage are empty. This does not validate narrative
    molecules, pathways or source scope.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-cytoplasmic_vesicle_membrane-causal
- check_id: diazoplast-uniprot-verify
  name: Native diazoplast UniProt verify check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:diazoplast
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/diazoplast.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Three represented Azotobacter accessions
    are verified; typed GENE_OR_PROTEIN graph coverage is zero after complex retyping.
    Identity does not establish the proteins as Epithemia diazoplast members.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-diazoplast-verify
- check_id: diazoplast-uniprot-causal
  name: Native diazoplast UniProt causal check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:diazoplast
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/diazoplast.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Three represented Azotobacter accessions
    are verified; typed GENE_OR_PROTEIN graph coverage is zero after complex retyping.
    Identity does not establish the proteins as Epithemia diazoplast members.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-diazoplast-causal
- check_id: early_endosome-uniprot-verify
  name: Native early endosome UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0005769
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/early_endosome.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Represented protein inventory and
    typed GENE_OR_PROTEIN graph coverage are empty. This does not validate narrative
    molecules, pathways or source scope.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-early_endosome-verify
- check_id: early_endosome-uniprot-causal
  name: Native early endosome UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0005769
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/early_endosome.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Represented protein inventory and
    typed GENE_OR_PROTEIN graph coverage are empty. This does not validate narrative
    molecules, pathways or source scope.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-early_endosome-causal
- check_id: early_endosome_lumen-uniprot-verify
  name: Native early endosome lumen UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0031905
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/early_endosome_lumen.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Represented protein inventory and
    typed GENE_OR_PROTEIN graph coverage are empty. This does not validate narrative
    molecules, pathways or source scope.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-early_endosome_lumen-verify
- check_id: early_endosome_lumen-uniprot-causal
  name: Native early endosome lumen UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0031905
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/early_endosome_lumen.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Represented protein inventory and
    typed GENE_OR_PROTEIN graph coverage are empty. This does not validate narrative
    molecules, pathways or source scope.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-early_endosome_lumen-causal
- check_id: early_endosome_membrane-uniprot-verify
  name: Native early endosome membrane UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0031901
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/early_endosome_membrane.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Represented protein inventory and
    typed GENE_OR_PROTEIN graph coverage are empty. This does not validate narrative
    molecules, pathways or source scope.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-early_endosome_membrane-verify
- check_id: early_endosome_membrane-uniprot-causal
  name: Native early endosome membrane UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0031901
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/early_endosome_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Represented protein inventory and
    typed GENE_OR_PROTEIN graph coverage are empty. This does not validate narrative
    molecules, pathways or source scope.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-early_endosome_membrane-causal
evidence:
- evidence_id: current-record-0
  kind: record_content
  reference: data/structures/membrane_organelle/cyanelle_thylakoid.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T12:35:23Z'
  support: context_only
  summary: Original frozen SHA256 19838578792948bb527b33a0dd61374b6ee7a688eb2ee0406426c2e95639c7e3;
    current SHA256 19838578792948bb527b33a0dd61374b6ee7a688eb2ee0406426c2e95639c7e3.
    Record bytes unchanged since the original review.
  snapshot_sha256: 19838578792948bb527b33a0dd61374b6ee7a688eb2ee0406426c2e95639c7e3
- evidence_id: original-review-0
  kind: prior_review
  reference: reviews/structured/20261022T013526Z-cyanelle-thylakoid-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T12:35:23Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 8d9f4f24970a0efde884021a112099b570e956b8cb1b64eb3d8e4d891e285ea2
- evidence_id: current-record-1
  kind: record_content
  reference: data/structures/membrane_organelle/cyanelle_thylakoid_lumen.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T12:35:23Z'
  support: context_only
  summary: Original frozen SHA256 6dc48d3d810b7a63387502082d26502265a7f12eafec88058eb9e5d8be70a205;
    current SHA256 6dc48d3d810b7a63387502082d26502265a7f12eafec88058eb9e5d8be70a205.
    Record bytes unchanged since the original review.
  snapshot_sha256: 6dc48d3d810b7a63387502082d26502265a7f12eafec88058eb9e5d8be70a205
- evidence_id: original-review-1
  kind: prior_review
  reference: reviews/structured/20261022T013527Z-cyanelle-thylakoid-lumen-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T12:35:23Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 13a7502831d4a4b2f9b06fc5530ef478c2ee33867988f2c8337a3bb55070b516
- evidence_id: current-record-2
  kind: record_content
  reference: data/structures/membrane_organelle/cyanelle_thylakoid_membrane.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T12:35:23Z'
  support: context_only
  summary: Original frozen SHA256 c1c3958038a4f3a20735ce33206475130078e9a12048dcbeff4bc0d04beb4178;
    current SHA256 c1c3958038a4f3a20735ce33206475130078e9a12048dcbeff4bc0d04beb4178.
    Record bytes unchanged since the original review.
  snapshot_sha256: c1c3958038a4f3a20735ce33206475130078e9a12048dcbeff4bc0d04beb4178
- evidence_id: original-review-2
  kind: prior_review
  reference: reviews/structured/20261022T013528Z-cyanelle-thylakoid-membrane-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T12:35:23Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 76a0977412a28cf2baa50929fe1707f5749155f170bde412acca91e6ea49c286
- evidence_id: current-record-3
  kind: record_content
  reference: data/structures/membrane_organelle/cytoplasmic_vesicle.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T12:35:23Z'
  support: context_only
  summary: Original frozen SHA256 f4704b74324c18cab955983a27173d6a98fae0153bc7a403cbbe3c865e4eba84;
    current SHA256 f4704b74324c18cab955983a27173d6a98fae0153bc7a403cbbe3c865e4eba84.
    Record bytes unchanged since the original review.
  snapshot_sha256: f4704b74324c18cab955983a27173d6a98fae0153bc7a403cbbe3c865e4eba84
- evidence_id: original-review-3
  kind: prior_review
  reference: reviews/structured/20261022T013529Z-cytoplasmic-vesicle-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T12:35:23Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 28e7e5777617f9550a87a3e10115a2d76c6839cc0b1ea0d65968f27a1a747d27
- evidence_id: current-record-4
  kind: record_content
  reference: data/structures/membrane_organelle/cytoplasmic_vesicle_lumen.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T12:35:23Z'
  support: context_only
  summary: Original frozen SHA256 87d5a5379cb643e40257e60c99a3308f2b6e6a49aa079856fb501fe6e3c738fe;
    current SHA256 87d5a5379cb643e40257e60c99a3308f2b6e6a49aa079856fb501fe6e3c738fe.
    Record bytes unchanged since the original review.
  snapshot_sha256: 87d5a5379cb643e40257e60c99a3308f2b6e6a49aa079856fb501fe6e3c738fe
- evidence_id: original-review-4
  kind: prior_review
  reference: reviews/structured/20261022T013530Z-cytoplasmic-vesicle-lumen-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T12:35:23Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 7cd480b7fd9a364ecae7d01c4f95bb8a64fae0577c237fb847140ca506cd3297
- evidence_id: current-record-5
  kind: record_content
  reference: data/structures/membrane_organelle/cytoplasmic_vesicle_membrane.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T12:35:23Z'
  support: context_only
  summary: Original frozen SHA256 112643d19f662095c8d81c907d5d6435fe93b612f8a037df2af0fe66af87d4aa;
    current SHA256 112643d19f662095c8d81c907d5d6435fe93b612f8a037df2af0fe66af87d4aa.
    Record bytes unchanged since the original review.
  snapshot_sha256: 112643d19f662095c8d81c907d5d6435fe93b612f8a037df2af0fe66af87d4aa
- evidence_id: original-review-5
  kind: prior_review
  reference: reviews/structured/20261022T013531Z-cytoplasmic-vesicle-membrane-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T12:35:23Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: bca15f1dfaa8c49be3a41da7df6e1c09d0c6cf1b59979f21ea033d9be5756d39
- evidence_id: current-record-6
  kind: record_content
  reference: data/structures/membrane_organelle/diazoplast.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T12:35:23Z'
  support: context_only
  summary: Original frozen SHA256 7aabee1c3f14420665958c955451705d3c7ea115003ffd94060a2f1afd40d41f;
    current SHA256 fd3948e827eb4a9870bc4eccb09689dd5c82f5caef443f1e319daabbf21bb038.
    Changed record reassessed against current sources.
  snapshot_sha256: fd3948e827eb4a9870bc4eccb09689dd5c82f5caef443f1e319daabbf21bb038
- evidence_id: original-review-6
  kind: prior_review
  reference: reviews/structured/20261022T013532Z-diazoplast-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T12:35:23Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: a90cd1c474f3d57bc8a5676a03bbee5664c89152a0550821996989b8a381fe3c
- evidence_id: current-record-7
  kind: record_content
  reference: data/structures/membrane_organelle/early_endosome.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T12:35:23Z'
  support: context_only
  summary: Original frozen SHA256 ed91f355f5faca2b5bd7af5036740c6d6034d783fcfa0252aeb533489c6a46a9;
    current SHA256 ed91f355f5faca2b5bd7af5036740c6d6034d783fcfa0252aeb533489c6a46a9.
    Record bytes unchanged since the original review.
  snapshot_sha256: ed91f355f5faca2b5bd7af5036740c6d6034d783fcfa0252aeb533489c6a46a9
- evidence_id: original-review-7
  kind: prior_review
  reference: reviews/structured/20261022T013533Z-early-endosome-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T12:35:23Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 0171636452cfeeec065d1c4502ab93239c402f667fa0fc2f841f8e633a97e7cc
- evidence_id: current-record-8
  kind: record_content
  reference: data/structures/membrane_organelle/early_endosome_lumen.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T12:35:23Z'
  support: context_only
  summary: Original frozen SHA256 fe21c86defd34e34c5df67ec7bc0e7be16cc0342f2b10c6bae2ffd9569060290;
    current SHA256 fe21c86defd34e34c5df67ec7bc0e7be16cc0342f2b10c6bae2ffd9569060290.
    Record bytes unchanged since the original review.
  snapshot_sha256: fe21c86defd34e34c5df67ec7bc0e7be16cc0342f2b10c6bae2ffd9569060290
- evidence_id: original-review-8
  kind: prior_review
  reference: reviews/structured/20261022T013534Z-early-endosome-lumen-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T12:35:23Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: a7450853bc9a7f4640e2686af2e22fd1ee2ab5ceca83dd7fd1817efc039df898
- evidence_id: current-record-9
  kind: record_content
  reference: data/structures/membrane_organelle/early_endosome_membrane.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T12:35:23Z'
  support: context_only
  summary: Original frozen SHA256 2d96c5c692f3e324e718d1fc2750703c41060a9ef56dd535cd55831da69354dc;
    current SHA256 2d96c5c692f3e324e718d1fc2750703c41060a9ef56dd535cd55831da69354dc.
    Record bytes unchanged since the original review.
  snapshot_sha256: 2d96c5c692f3e324e718d1fc2750703c41060a9ef56dd535cd55831da69354dc
- evidence_id: original-review-9
  kind: prior_review
  reference: reviews/structured/20261022T013534Z-early-endosome-membrane-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T12:35:23Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: ba11e4fd120f6d681e845a98d80bc970238961fef7caee92acbc98a1e5bbcb1d
- evidence_id: plaque-current-0
  kind: record_content
  reference: data/structures/membrane_organelle/cyanelle_thylakoid.yaml
  locator: Entire maintained record at source cd5be11ad13304d75404a51d097635022d1bd091;
    all fields, histories, discussions and graphs
  summary: Entire current target independently read. Hash remains unchanged from original
    frozen target; PROPOSED status unchanged and no record curation performed.
  accessed_at: '2026-11-03T12:31:55.499900Z'
  support: supports
  snapshot_sha256: 19838578792948bb527b33a0dd61374b6ee7a688eb2ee0406426c2e95639c7e3
- evidence_id: plaque-original-0
  kind: prior_review
  reference: reviews/structured/20261022T013526Z-cyanelle-thylakoid-audit/review.yaml
  locator: Original authoritative YAML/Markdown, source inputs, checks, assessments,
    findings/actions and limitations
  summary: Original native validate/render passes and all original historical input
    hashes match. Verdict pass_with_limitations, no findings or actions. No original
    scientific finding exists to terminally dispose of.
  accessed_at: '2026-11-03T12:31:55.499900Z'
  support: supports
  snapshot_sha256: 8d9f4f24970a0efde884021a112099b570e956b8cb1b64eb3d8e4d891e285ea2
- evidence_id: plaque-current-1
  kind: record_content
  reference: data/structures/membrane_organelle/cyanelle_thylakoid_lumen.yaml
  locator: Entire maintained record at source cd5be11ad13304d75404a51d097635022d1bd091;
    all fields, histories, discussions and graphs
  summary: Entire current target independently read. Hash remains unchanged from original
    frozen target; PROPOSED status unchanged and no record curation performed.
  accessed_at: '2026-11-03T12:31:55.499900Z'
  support: supports
  snapshot_sha256: 6dc48d3d810b7a63387502082d26502265a7f12eafec88058eb9e5d8be70a205
- evidence_id: plaque-original-1
  kind: prior_review
  reference: reviews/structured/20261022T013527Z-cyanelle-thylakoid-lumen-audit/review.yaml
  locator: Original authoritative YAML/Markdown, source inputs, checks, assessments,
    findings/actions and limitations
  summary: Original native validate/render passes and all original historical input
    hashes match. Verdict pass_with_limitations, no findings or actions. No original
    scientific finding exists to terminally dispose of.
  accessed_at: '2026-11-03T12:31:55.499900Z'
  support: supports
  snapshot_sha256: 13a7502831d4a4b2f9b06fc5530ef478c2ee33867988f2c8337a3bb55070b516
- evidence_id: plaque-current-2
  kind: record_content
  reference: data/structures/membrane_organelle/cyanelle_thylakoid_membrane.yaml
  locator: Entire maintained record at source cd5be11ad13304d75404a51d097635022d1bd091;
    all fields, histories, discussions and graphs
  summary: Entire current target independently read. Hash remains unchanged from original
    frozen target; PROPOSED status unchanged and no record curation performed.
  accessed_at: '2026-11-03T12:31:55.499900Z'
  support: supports
  snapshot_sha256: c1c3958038a4f3a20735ce33206475130078e9a12048dcbeff4bc0d04beb4178
- evidence_id: plaque-original-2
  kind: prior_review
  reference: reviews/structured/20261022T013528Z-cyanelle-thylakoid-membrane-audit/review.yaml
  locator: Original authoritative YAML/Markdown, source inputs, checks, assessments,
    findings/actions and limitations
  summary: Original native validate/render passes and all original historical input
    hashes match. Verdict pass_with_limitations, no findings or actions. No original
    scientific finding exists to terminally dispose of.
  accessed_at: '2026-11-03T12:31:55.499900Z'
  support: supports
  snapshot_sha256: 76a0977412a28cf2baa50929fe1707f5749155f170bde412acca91e6ea49c286
- evidence_id: plaque-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Frozen native policy/schema; complete applicable rules and taxonomy descriptions
  summary: Actual named genes/proteins/regulators/pathways/stress responses/traits
    trigger structured-source assessment. Generic material/topology or explicitly
    withheld molecular assignments are genuine exclusions.
  accessed_at: '2026-11-03T12:31:55.499900Z'
  support: context_only
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: plaque-rubric
  kind: authority
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Frozen native policy/schema; complete applicable rules and taxonomy descriptions
  summary: Source-scoped identity, component grounding, necessity, taxonomy and graph
    assessment; no compulsory protein inventory is fabricated for a material or topology
    record.
  accessed_at: '2026-11-03T12:31:55.499900Z'
  support: context_only
  snapshot_sha256: e6b9e4b16a58c54402bed7bbee2c8b94a91d37562e8b0ee8b94ff0c829184a70
- evidence_id: plaque-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Frozen native policy/schema; complete applicable rules and taxonomy descriptions
  summary: NONMECHANISTIC is a descriptive topology/function graph, not a demonstrated
    molecular formation mechanism.
  accessed_at: '2026-11-03T12:31:55.499900Z'
  support: context_only
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: plaque-schema-policy
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Frozen native policy/schema; complete applicable rules and taxonomy descriptions
  summary: Native schema introduction explicitly lists whole thylakoid as organelle-level
    granularity and MEMBRANE_ORGANELLE includes thylakoids. This coarse repository
    kind does not assert GO is_a organelle; GO0009579 comment about ontology organelle
    classification is not a contradiction in exact GO identity.
  accessed_at: '2026-11-03T12:31:55.499900Z'
  support: context_only
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: plaque-thylakoid-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009843,GO:0009842,GO:0009579,GO:0031976,GO:0033114,GO:0033115,GO:0031978,GO:0042651,GO:0055035,GO:0019684
  locator: Complete exact ten-term definitions, synonyms, obsolete status and typed
    child relations:0009843,0009842,0009579,0031976,0033114,0033115,0031978,0042651,0055035,0019684
  summary: GO0009843 is_a plastid thylakoid0031976, itself is_a thylakoid0009579;
    cyanelle0009842 contains0009843. Whole0009843 contains lumen0033114 and membrane0033115.
    Lumen is_a plastid lumen0031978; membrane is_a plastid thylakoid membrane0055035,
    itself is_a0042651. Both direct and broader parent classes are valid without claiming
    every parent direct. GO0019684 defines light reactions, not an experiment or particular
    protein necessity.
  accessed_at: '2026-11-03T12:28:15.159233Z'
  support: supports
  snapshot_sha256: 80a3716fe3cbefb29f0605ef8c411af5924fd206d86f2c0d0df65861ac476fbb
- evidence_id: plaque-thylakoid-agent-SL-0277
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0277.json
  locator: Complete top-level definition, immediate isA/partOf and direct GO correspondence;
    nested objects distinguished
  summary: SL0277 exactly mapsGO0009843, describing interconnected internal cyanelle
    membranes carrying out photosynthetic reactions; partOfSL0082 and parentSL0278.
    Protein counts are not structural prevalence or constituent necessity evidence.
  accessed_at: '2026-11-03T12:28:15.159473Z'
  support: supports
  snapshot_sha256: df24a25f56576fb322f032647d7a00c7e40087a5631bc78579f0392d613a66cf
- evidence_id: plaque-thylakoid-agent-SL-0084
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0084.json
  locator: Complete top-level definition, immediate isA/partOf and direct GO correspondence;
    nested objects distinguished
  summary: SL0084 exactly mapsGO0033114, the compartment bounded by cyanelle thylakoid
    membranes; parentSL0309 and partOfSL0277. Protein counts are not structural prevalence
    or constituent necessity evidence.
  accessed_at: '2026-11-03T12:28:15.159535Z'
  support: supports
  snapshot_sha256: 1d9d5a21592a2b0e9cc7199aeabcf70e6d0740dd5f390522ed6881f8c24a00f3
- evidence_id: plaque-thylakoid-agent-SL-0085
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0085.json
  locator: Complete top-level definition, immediate isA/partOf and direct GO correspondence;
    nested objects distinguished
  summary: SL0085 exactly mapsGO0033115, the lipid bilayer surrounding the thylakoid
    space within a glaucophyte photosynthetic organelle; parentSL0216 and partOfSL0277.
    Protein counts are not structural prevalence or constituent necessity evidence.
  accessed_at: '2026-11-03T12:28:15.161138Z'
  support: supports
  snapshot_sha256: 521b00e6f6978134d8516bb2234fc24c1ccc8e96da88735660076a3ef99ce4e4
- evidence_id: plaque-cached-tax2762
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2762
  locator: Complete native taxId/scientificName/rank/lineage/alternative names
  summary: ENA verifies Cyanophora paradoxa 2762. Species belongs to Glaucocystophyceae.
    Identity does not establish experimental strain or numerical prevalence. Prior
    PR2362 snapshot independently reread; actual11:52Z fetch time retained, not a
    fresh request.
  accessed_at: '2026-11-03T11:52:36.404873Z'
  support: supports
  snapshot_sha256: 8384800c0c30321c096fb48117051165d50982c461255fe65d738d523d60ed7a
- evidence_id: plaque-cached-tax38254
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/38254
  locator: Complete native taxId/scientificName/rank/lineage/alternative names
  summary: ENA verifies Glaucocystophyceae 38254. Glaucophyta and Glaucophyceae are
    synonyms of class Glaucocystophyceae. Identity does not establish experimental
    strain or numerical prevalence. Prior PR2362 snapshot independently reread; actual11:52Z
    fetch time retained, not a fresh request.
  accessed_at: '2026-11-03T11:52:36.404908Z'
  support: supports
  snapshot_sha256: 4b487eb0e34bcb4941fbb315aae5214c96ea6f60255d71a2aca172cd35844009
- evidence_id: plaque-cached-giddings1983-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1104%2Fpp.71.2.409
  locator: Complete primary abstract and exact title/authors/year/DOI10.1104/pp.71.2.409/PMID16662839
    metadata
  summary: Giddings/Wasmann/Staehelin1983 studies cyanelle thylakoids and envelope
    membranes in C.paradoxa by thin-section/freeze-fracture/etch microscopy and pigment/protein
    preparation. Presumptive PSII assignments and historical symbiont interpretation
    are not upgraded to modern molecular certainty. Prior PR2362 metadata snapshot
    independently reread with original fetch time; primary scan scopes are separately
    declared.
  accessed_at: '2026-11-03T11:52:37.145401Z'
  support: supports
  snapshot_sha256: e9050ae8f4efd4fb2d2362f165fcf9704d181bed10bd5e996a87e7ae85d79c02
- evidence_id: plaque-cached-giddings1983-page409
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/6ed041edd2c7/plntphys00558-0203.png
  locator: 'Scanned page409 visually inspected at original resolution: Title/authors,
    abstract, Introduction and initial culture/isolation Methods'
  summary: C.paradoxa UTEX LB555 grown at26C in modified CY-II medium under continuous
    illumination. Biological photosynthetic context and morphology are supported,
    without adopting historical endosymbiont language as modern ontology classification.
    Prior PR2362 scan independently viewed again with actual11:52Z retrieval retained.
    Only declared pages are claimed; no raw microscopy reanalysis.
  accessed_at: '2026-11-03T11:52:37.773780Z'
  support: supports
  snapshot_sha256: c0184058c66810b2544be1af57fac9acc2bbbfcdf71ee1186aade8232e5c9f61
- evidence_id: plaque-cached-giddings1983-page410
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/8d99de19802c/plntphys00558-0204.png
  locator: 'Scanned page410 visually inspected at original resolution: Figures1–3
    images/captions and continuing isolation Methods'
  summary: Whole cell and isolated cyanelle thin sections plus freeze-fracture thylakoid
    images show internal membranes and patterned surfaces. Isolated thylakoid preparations
    differ from intact cells; no new image measurements made. Prior PR2362 scan independently
    viewed again with actual11:52Z retrieval retained. Only declared pages are claimed;
    no raw microscopy reanalysis.
  accessed_at: '2026-11-03T11:52:37.785213Z'
  support: supports
  snapshot_sha256: ba0bd01ef58d44879c8f7b2689f79f5066039cef904b15a32330a611681812c0
- evidence_id: plaque-thylakoid-agent-giddings1983-page411
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/e0e22d1a8212/plntphys00558-0205.png
  locator: 'Scanned page411 visually inspected at original resolution: Figures4–5
    plots/captions and spectrophotometry/electrophoresis/electron microscopy Methods'
  summary: Particle-size histograms and absorption spectra before/after phycobiliprotein
    removal support the experimental scope. These are not a complete protein inventory
    or live-cell flux assay. Fresh public scan fetched12:28Z and independently viewed.
    Only declared pages are claimed; no raw microscopy reanalysis.
  accessed_at: '2026-11-03T12:28:15.164018Z'
  support: supports
  snapshot_sha256: 04c8112a5bdb0baf084cf2bbe18bdab02f401d99b64e56123a9408dcac13afc5
- evidence_id: plaque-cached-giddings1983-page412
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/392b5bf89308/plntphys00558-0206.png
  locator: 'Scanned page412 visually inspected at original resolution: Figure6 gel/caption,
    final preparation Methods and Thylakoids Results'
  summary: Protein preparations before/after pigment removal, thylakoid particle patterns
    and phycobilisome morphology distinguish supported material architecture from
    interpreted molecular identity. Prior PR2362 scan independently viewed again with
    actual11:52Z retrieval retained. Only declared pages are claimed; no raw microscopy
    reanalysis.
  accessed_at: '2026-11-03T11:52:37.796954Z'
  support: supports
  snapshot_sha256: 9c033e4b190ed1cd62006b88fa8961e80608056e79e1ec0fc45040e3bb19f47f
- evidence_id: plaque-thylakoid-agent-giddings1983-page413
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/fa8191742d8c/plntphys00558-0207.png
  locator: 'Scanned page413 visually inspected at original resolution: Figures7–10
    pixels and complete captions'
  summary: Thin-section and freeze-etch preparations show membrane sheets and surface
    phycobilisome rows; removed-pigment samples expose underlying particles. Interpreted
    particle identities remain qualified. Fresh public scan fetched12:28Z and independently
    viewed. Only declared pages are claimed; no raw microscopy reanalysis.
  accessed_at: '2026-11-03T12:28:15.166951Z'
  support: supports
  snapshot_sha256: 304f4c6eeb11b196e20f2e557df93393f410b032f1a7c1c5f62cf699ca9430d5
- evidence_id: plaque-cached-giddings1983-page416
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/c329334d81e0/plntphys00558-0210.png
  locator: 'Scanned page416 visually inspected at original resolution: Figure15 histogram/caption,
    envelope Results continuation and Discussion opening'
  summary: Discussion relates thylakoid pigment, gel and microscopy observations to
    putative PSII centers. Proposed one-to-one structural association and reaction-center
    count are interpretations, not a complete verified proteome. Prior PR2362 scan
    independently viewed again with actual11:52Z retrieval retained. Only declared
    pages are claimed; no raw microscopy reanalysis.
  accessed_at: '2026-11-03T11:52:38.068083Z'
  support: supports
  snapshot_sha256: 41f820c6bde6abc4318ac32baa45293634543bb4aceb0dc5129c3d25414e91ef
- evidence_id: plaque-cached-giddings1983-page417
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/7694ed6a7a74/plntphys00558-0211.png
  locator: 'Scanned page417 visually inspected at original resolution: Complete Discussion
    text and Figures16–18 pixels/captions'
  summary: Source explicitly states precise PSI localization is unknown and PSII-to-PSI
    versus direct energy transfer cannot be assessed. Envelope figures are not thylakoid
    evidence. Current target records do not assert the unsupported precise PSI arrangement.
    Prior PR2362 scan independently viewed again with actual11:52Z retrieval retained.
    Only declared pages are claimed; no raw microscopy reanalysis.
  accessed_at: '2026-11-03T11:52:38.074636Z'
  support: supports
  snapshot_sha256: 276c1cb60d1a909200199f8e24495840d2caa5f5131c8a896d3f97d70e5bcf6f
- evidence_id: plaque-thylakoid-agent-giddings1983-page418
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/147bb64bab4f/plntphys00558-0212.png
  locator: 'Scanned page418 visually inspected at original resolution: Figure19 schematic
    pixels and full caption; no complete bibliography audit'
  summary: The thylakoid schematic distinguishes lipid bilayer, lumen-facing surface,
    phycobilisomes and presumptive PSII attachment sites. It is a model with probable/presumptive
    molecular assignments, not an independent experimental image or basis for complete
    molecular necessity. Fresh public scan fetched12:28Z and independently viewed.
    Only declared pages are claimed; no raw microscopy reanalysis.
  accessed_at: '2026-11-03T12:28:15.168417Z'
  support: supports
  snapshot_sha256: 53bb97a831bd4188d8c67250adbeae16a40c0df97c26f61c6417debe30e83e53
- evidence_id: plaque-catalogue
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: 'Complete fresh /api/datasets response: every returned organism and dataset
    entry inspected; no pagination'
  summary: No current organism row covers Cyanophora or another glaucophyte. A Synechococcus
    dataset is not substituted for a Cyanophora host context. Thus no matched downstream
    gene/module query applies. Catalogue noncoverage is not biological absence or
    a lack of photosynthetic machinery.
  accessed_at: '2026-11-03T12:28:15.168686Z'
  support: supports
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: plaque-historical-runner
  kind: validation
  reference: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb datasets
  locator: Original historical00:49Z receipt and stdout/stderr independently reread/hash-verified
  summary: Historical runner exited1 before datasets due OS PermissionError on pyvenv.cfg;
    not a new invocation or successful execution. Official current catalogue is the
    permitted source fallback.
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: plaque-original-checks
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/adversary-plaque/original-checks.json
  locator: Three read-only original native validate/render executions and every frozen
    input at historical source commit
  summary: All three originals validate/render exactly. All12/12/12 historical input
    hashes match, and current targets remain unchanged. Original findings/actions
    empty.
  accessed_at: '2026-11-03T12:28:34.866383Z'
  support: supports
  snapshot_sha256: 4007b471051fbf7ff436e43654d961c09035d961cb1fbc544c2c4fe3ce2c2247
- evidence_id: plaque-native-cyanelle_thylakoid-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_thylakoid.yaml
    --verify
  locator: Actual root-owned native receipt and exact stdout independently read/hash-verified
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  accessed_at: '2026-11-03T12:28:23.045358Z'
  support: supports
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: plaque-native-cyanelle_thylakoid-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_thylakoid.yaml
    --causal-graphs
  locator: Actual root-owned native receipt and exact stdout independently read/hash-verified
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
  accessed_at: '2026-11-03T12:28:23.540854Z'
  support: supports
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
- evidence_id: plaque-native-cyanelle_thylakoid_lumen-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_thylakoid_lumen.yaml
    --verify
  locator: Actual root-owned native receipt and exact stdout independently read/hash-verified
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  accessed_at: '2026-11-03T12:28:24.030769Z'
  support: supports
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: plaque-native-cyanelle_thylakoid_lumen-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_thylakoid_lumen.yaml
    --causal-graphs
  locator: Actual root-owned native receipt and exact stdout independently read/hash-verified
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
  accessed_at: '2026-11-03T12:28:24.538209Z'
  support: supports
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
- evidence_id: plaque-native-cyanelle_thylakoid_membrane-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_thylakoid_membrane.yaml
    --verify
  locator: Actual root-owned native receipt and exact stdout independently read/hash-verified
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  accessed_at: '2026-11-03T12:28:25.010743Z'
  support: supports
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: plaque-native-cyanelle_thylakoid_membrane-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_thylakoid_membrane.yaml
    --causal-graphs
  locator: Actual root-owned native receipt and exact stdout independently read/hash-verified
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
  accessed_at: '2026-11-03T12:28:25.474567Z'
  support: supports
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
- evidence_id: micro-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Native source scopes, structured-adapter triggers, read-only ownership;
    profile/shared contract/config/checklist and graph/component schema retained as
    frozen context
  accessed_at: '2026-11-03T12:33:18.218593Z'
  support: context_only
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
  summary: All17 common policy/schema/verifier inputs hash-identical to prior reviewed
    set; native route and config reread, applicable protein and complex-field contracts
    rechecked. A named pathway can trigger applicability even in a topology graph;
    molecular identity alone does not establish membership.
- evidence_id: micro-schema-protein-example
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Component.protein_examples lines448–454; ProteinExample description lines462–467;
    causal NodeType contract
  accessed_at: '2026-11-03T12:33:18.218593Z'
  support: supports
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
  summary: Protein examples require an organism-specific instance whose role in this
    structure was established. A single accession is not the whole multisubunit complex;
    STRUCTURE is appropriate for a GO-grounded nitrogenase complex.
- evidence_id: micro-record-diazoplast
  kind: record_content
  reference: data/structures/membrane_organelle/diazoplast.yaml
  locator: Entire current maintained YAML including definition/history, components/examples,
    taxa, functions, all graph nodes/edges, discussions and any image
  accessed_at: '2026-11-03T12:33:18.218593Z'
  support: supports
  snapshot_sha256: fd3948e827eb4a9870bc4eccb09689dd5c82f5caef443f1e319daabbf21bb038
  summary: Entire current target independently read at cd5be11ad13304d75404a51d097635022d1bd091.
    Diazoplast stale delta is new history plus nitrogenase node GENE_OR_PROTEIN→STRUCTURE;
    three protein examples remain unchanged.
- evidence_id: micro-prior-diazoplast
  kind: prior_review
  reference: reviews/structured/20261022T013532Z-diazoplast-audit/review.yaml
  locator: 'Original authoritative YAML and paired Markdown: frozen inputs, scientific
    assessments, findings/actions, limitations, native check claims and applicability
    rationale'
  accessed_at: '2026-11-03T12:33:18.218593Z'
  support: context_only
  snapshot_sha256: a90cd1c474f3d57bc8a5676a03bbee5664c89152a0550821996989b8a381fe3c
  summary: Original observation preserved. Exact original F1 cross-taxon protein-example
    placement is re-evaluated with lineage retained.
- evidence_id: micro-native-diazoplast-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/diazoplast-uniprot-verify-receipt.json
  locator: Actual .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/diazoplast.yaml
    --verify; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/diazoplast-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T12:28:29.654838Z'
  support: supports
  snapshot_sha256: 0734eb70d9dcf5f104bf94ecdbb12f59cee0de95d46dabd3b1a18a727ee9dccb
  summary: Root current-source execution exit0. Current verify covers the three represented
    Azotobacter accessions and any declared xrefs; it does not prove diazoplast membership.
- evidence_id: micro-native-diazoplast-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/diazoplast-uniprot-causal-receipt.json
  locator: Actual .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/diazoplast.yaml
    --causal-graphs; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/diazoplast-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-03T12:28:30.078381Z'
  support: supports
  snapshot_sha256: 23440a8c02deec6349005d325316f634a21d7968f56d71698316b3c2bf99927e
  summary: Root current-source execution exit0. All categories and total GENE_OR_PROTEIN
    causal nodes are zero; nitrogenase complex is now STRUCTURE. This check does not
    assess whole graph biology.
- evidence_id: micro-record-early_endosome
  kind: record_content
  reference: data/structures/membrane_organelle/early_endosome.yaml
  locator: Entire current maintained YAML including definition/history, components/examples,
    taxa, functions, all graph nodes/edges, discussions and any image
  accessed_at: '2026-11-03T12:33:18.218593Z'
  support: supports
  snapshot_sha256: ed91f355f5faca2b5bd7af5036740c6d6034d783fcfa0252aeb533489c6a46a9
  summary: Entire current target independently read at cd5be11ad13304d75404a51d097635022d1bd091.
    Current bytes match original frozen record input.
- evidence_id: micro-prior-early_endosome
  kind: prior_review
  reference: reviews/structured/20261022T013533Z-early-endosome-audit/review.yaml
  locator: 'Original authoritative YAML and paired Markdown: frozen inputs, scientific
    assessments, findings/actions, limitations, native check claims and applicability
    rationale'
  accessed_at: '2026-11-03T12:33:18.218593Z'
  support: context_only
  snapshot_sha256: 0171636452cfeeec065d1c4502ab93239c402f667fa0fc2f841f8e633a97e7cc
  summary: Original observation preserved. Original findings/actions empty; qualified
    source limitations, including lipid-transit uncertainty for whole early endosome,
    are not silently upgraded.
- evidence_id: micro-native-early_endosome-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/early_endosome-uniprot-verify-receipt.json
  locator: Actual .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/early_endosome.yaml
    --verify; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/early_endosome-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T12:28:30.502705Z'
  support: supports
  snapshot_sha256: 74d3ed23feda225b7cbfd6c469bb0d24ea862e6ec0bdf4558cc948fa6fd05259
  summary: Root current-source execution exit0. Declared protein-example/xref inventory
    is empty; zero exit is not biological protein coverage.
- evidence_id: micro-native-early_endosome-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/early_endosome-uniprot-causal-receipt.json
  locator: Actual .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/early_endosome.yaml
    --causal-graphs; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/early_endosome-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-03T12:28:30.934314Z'
  support: supports
  snapshot_sha256: acea8ba17c64804f0d59c661e5747940405cdc31e78580b7a69205d4e7a9b905
  summary: Root current-source execution exit0. All categories and total GENE_OR_PROTEIN
    causal nodes are zero; nitrogenase complex is now STRUCTURE. This check does not
    assess whole graph biology.
- evidence_id: micro-record-early_endosome_lumen
  kind: record_content
  reference: data/structures/membrane_organelle/early_endosome_lumen.yaml
  locator: Entire current maintained YAML including definition/history, components/examples,
    taxa, functions, all graph nodes/edges, discussions and any image
  accessed_at: '2026-11-03T12:33:18.218593Z'
  support: supports
  snapshot_sha256: fe21c86defd34e34c5df67ec7bc0e7be16cc0342f2b10c6bae2ffd9569060290
  summary: Entire current target independently read at cd5be11ad13304d75404a51d097635022d1bd091.
    Current bytes match original frozen record input.
- evidence_id: micro-prior-early_endosome_lumen
  kind: prior_review
  reference: reviews/structured/20261022T013534Z-early-endosome-lumen-audit/review.yaml
  locator: 'Original authoritative YAML and paired Markdown: frozen inputs, scientific
    assessments, findings/actions, limitations, native check claims and applicability
    rationale'
  accessed_at: '2026-11-03T12:33:18.218593Z'
  support: context_only
  snapshot_sha256: a7450853bc9a7f4640e2686af2e22fd1ee2ab5ceca83dd7fd1817efc039df898
  summary: Original observation preserved. Original findings/actions empty; qualified
    source limitations, including lipid-transit uncertainty for whole early endosome,
    are not silently upgraded.
- evidence_id: micro-native-early_endosome_lumen-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/early_endosome_lumen-uniprot-verify-receipt.json
  locator: Actual .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/early_endosome_lumen.yaml
    --verify; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/early_endosome_lumen-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T12:28:31.363019Z'
  support: supports
  snapshot_sha256: 0142facd4e5c5af20c82c9cd1741832a7dee2b7202b35df6b3e4df1f5dfb5b25
  summary: Root current-source execution exit0. Declared protein-example/xref inventory
    is empty; zero exit is not biological protein coverage.
- evidence_id: micro-native-early_endosome_lumen-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/early_endosome_lumen-uniprot-causal-receipt.json
  locator: Actual .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/early_endosome_lumen.yaml
    --causal-graphs; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/early_endosome_lumen-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-03T12:28:31.802783Z'
  support: supports
  snapshot_sha256: c72ad3027978f6e6f0f136136376dfa117ae26da651f019e4d71313d39c1bd17
  summary: Root current-source execution exit0. All categories and total GENE_OR_PROTEIN
    causal nodes are zero; nitrogenase complex is now STRUCTURE. This check does not
    assess whole graph biology.
- evidence_id: micro-record-early_endosome_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/early_endosome_membrane.yaml
  locator: Entire current maintained YAML including definition/history, components/examples,
    taxa, functions, all graph nodes/edges, discussions and any image
  accessed_at: '2026-11-03T12:33:18.218593Z'
  support: supports
  snapshot_sha256: 2d96c5c692f3e324e718d1fc2750703c41060a9ef56dd535cd55831da69354dc
  summary: Entire current target independently read at cd5be11ad13304d75404a51d097635022d1bd091.
    Current bytes match original frozen record input.
- evidence_id: micro-prior-early_endosome_membrane
  kind: prior_review
  reference: reviews/structured/20261022T013534Z-early-endosome-membrane-audit/review.yaml
  locator: 'Original authoritative YAML and paired Markdown: frozen inputs, scientific
    assessments, findings/actions, limitations, native check claims and applicability
    rationale'
  accessed_at: '2026-11-03T12:33:18.218593Z'
  support: context_only
  snapshot_sha256: ba11e4fd120f6d681e845a98d80bc970238961fef7caee92acbc98a1e5bbcb1d
  summary: Original observation preserved. Original findings/actions empty; qualified
    source limitations, including lipid-transit uncertainty for whole early endosome,
    are not silently upgraded.
- evidence_id: micro-native-early_endosome_membrane-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/early_endosome_membrane-uniprot-verify-receipt.json
  locator: Actual .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/early_endosome_membrane.yaml
    --verify; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/early_endosome_membrane-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T12:28:32.252759Z'
  support: supports
  snapshot_sha256: 93c281358235e1f1907225efb155ed4f46dcff1bf0f6c095de6cbb63f0efc0b7
  summary: Root current-source execution exit0. Declared protein-example/xref inventory
    is empty; zero exit is not biological protein coverage.
- evidence_id: micro-native-early_endosome_membrane-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/early_endosome_membrane-uniprot-causal-receipt.json
  locator: Actual .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/early_endosome_membrane.yaml
    --causal-graphs; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/early_endosome_membrane-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-03T12:28:32.680990Z'
  support: supports
  snapshot_sha256: 056598ae71aac15d7da6a4190f4d6ea753dc6bf7a1b2ec74ec0e6ce66c96568a
  summary: Root current-source execution exit0. All categories and total GENE_OR_PROTEIN
    causal nodes are zero; nitrogenase complex is now STRUCTURE. This check does not
    assess whole graph biology.
- evidence_id: micro-context-nitroplast
  kind: record_content
  reference: data/structures/membrane_organelle/nitroplast.yaml
  locator: 'Bounded neighbor fields only: identifier,label,definition,parent/part
    fields,taxonomic/canonical example and discussions; frozen before reading'
  accessed_at: '2026-11-03T12:33:18.218593Z'
  support: context_only
  snapshot_sha256: 3f7dc36b6c5e8389c881e64839227e1e5cdde49edb55277e245b180f0de8d6a8
  summary: 'Boundary context only: UCYN-A-derived compartment in a Braarudosphaera
    host is distinct from Epithemia diazoplast. No full neighbor scientific audit
    or resolution of its findings.'
- evidence_id: micro-context-reservosome
  kind: record_content
  reference: data/structures/membrane_organelle/reservosome.yaml
  locator: 'Bounded neighbor fields only: identifier,label,definition,parent/part
    fields,taxonomic/canonical example and discussions; frozen before reading'
  accessed_at: '2026-11-03T12:33:18.218593Z'
  support: context_only
  snapshot_sha256: c1a9daf798668ddf44d05a61e4ef589754275f4d385f1560ce38ccab0c07cdfa
  summary: 'Boundary context only: Posterior T.cruzi storage compartment is distinct
    from the upstream early-endosomal network. No full neighbor scientific audit or
    resolution of its findings.'
- evidence_id: micro-image-local
  kind: record_content
  reference: data/images/membrane_organelle/diazoplast/pmc11070190_f2.jpg
  locator: Entire frozen Figure2 A–C visually viewed in pixels, including12h/24h isotope
    panels, arrowheads, axes and lower quantification panels
  accessed_at: '2026-11-03T12:33:18.218593Z'
  support: supports
  snapshot_sha256: b8aae76bbe0c1d74896370bae92524c6764ea2795b1ddfa2309c5fc28dc74366
  summary: Complete multi-panel NanoSIMS figure matches record caption and native
    source asset. This is actual pixel inspection, not merely caption reading; no
    raw numerical data reanalysis.
- evidence_id: micro-original-validation-inputs
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/adversary-microtubule/original-validation-inputs.json
  locator: Four native validate commands and four render --content comparisons; original
    Git-source and current input SHA checks
  accessed_at: '2026-11-03T12:29:55.995278Z'
  support: supports
  snapshot_sha256: 8ab5208194a6da96f3fb5d90f0538cac39a8a1dccc5a6b4a342eb530024edd0c
  summary: All four original pairs validate and render byte-identically. Historical
    source f97b1abe2d78971b6f66b9083087d7a94cf3c0cc inputs verified. Diazoplast alone
    stale in this slice; no original artifact rewritten.
- evidence_id: micro-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005769,GO:0005768,GO:0031901,GO:0031905,GO:0031910,GO:0031904,GO:0010008,GO:0043229,GO:0016020,GO:0016610,GO:0009399
  locator: 'Exact11-ID QuickGO response: definitions, active IDs and relevant typed
    child links; nitrogenaseGO0016610, fixationGO0009399, membrane/parent and all
    early-endosome terms'
  accessed_at: '2026-11-03T12:28:39.978039Z'
  support: supports
  snapshot_sha256: 2d3a411f06f5f0cadfabef628c420720c57625490d072af15c08150948c2d70a
  summary: Nitrogenase is a multisubunit complex with dinitrogenase and reductase,
    appropriate for STRUCTURE rather than a single gene/protein node. Early endosome,
    its lumen and surrounding bilayer have distinct exact identities; is-a and parthood
    links support topology. Broad intracellular organelle identity does not assert
    genetic integration.
- evidence_id: micro-SL-0094
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0094.json
  locator: UniProt native location JSON top-level definition, GO mapping, synonyms
    and hierarchy, with nested parent context
  accessed_at: '2026-11-03T12:28:39.978287Z'
  support: supports
  snapshot_sha256: eeac92a80301f62a58e7347189eb41dbfc07ad0a967e92ef381a322564f7dd6c
  summary: Exact early-endosome whole organelle and generic sorting scope agrees with
    GO; no imported universal pH, timing or specific receptor mechanism.
- evidence_id: micro-SL-0093
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0093.json
  locator: UniProt native location JSON top-level definition, GO mapping, synonyms
    and hierarchy, with nested parent context
  accessed_at: '2026-11-03T12:28:39.978375Z'
  support: supports
  snapshot_sha256: 392b6ec7be8069b5e4fd3aa57cda8eb78009fc21183689d7f90e8568637a3318
  summary: Exact early-endosome membrane boundary and synonym scope agrees with GO;
    no imported universal pH, timing or specific receptor mechanism.
- evidence_id: micro-SL-0337
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0337.json
  locator: UniProt native location JSON top-level definition, GO mapping, synonyms
    and hierarchy, with nested parent context
  accessed_at: '2026-11-03T12:28:39.978438Z'
  support: supports
  snapshot_sha256: fbb1b4b36e69fc7e4e876f50871e220533e9484041a2bda06d92581b945010bc
  summary: Exact early-endosome lumen boundary and synonym scope agrees with GO; no
    imported universal pH, timing or specific receptor mechanism.
- evidence_id: micro-tax5693
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5693
  locator: Exact ENA taxonomy tax-id response, scientific name, rank and alternate
    names
  accessed_at: '2026-11-03T12:28:39.978489Z'
  support: supports
  snapshot_sha256: 29ca5f9c41995471a462d22be4406f02aa99f2f23760f2ea91ac33282f22482f
  summary: 'Current identity verified: Trypanosoma cruzi species. Taxonomic identity
    alone is not evidence of compartment occurrence or protein membership.'
- evidence_id: micro-tax420972
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/420972
  locator: Exact ENA taxonomy tax-id response, scientific name, rank and alternate
    names
  accessed_at: '2026-11-03T12:28:39.978559Z'
  support: supports
  snapshot_sha256: 17b622fbd7860adee0cc4697b6d8b626a841ba1bb791324da3e2e10e1d5831cc
  summary: 'Current identity verified: Epithemia genus. Taxonomic identity alone is
    not evidence of compartment occurrence or protein membership.'
- evidence_id: micro-tax3042617
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3042617
  locator: Exact ENA taxonomy tax-id response, scientific name, rank and alternate
    names
  accessed_at: '2026-11-03T12:28:40.748676Z'
  support: supports
  snapshot_sha256: 889143154003a55cea05eb52d266b6a30a2b8d3f2d391f9fc975d5b5de643249
  summary: 'Current identity verified: Epithemia clementina (nom. ined.) species.
    Taxonomic identity alone is not evidence of compartment occurrence or protein
    membership.'
- evidence_id: micro-tax354
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/354
  locator: Exact ENA taxonomy tax-id response, scientific name, rank and alternate
    names
  accessed_at: '2026-11-03T12:28:40.750593Z'
  support: supports
  snapshot_sha256: 38679248614ff58289dae5e99ef4017b290943511d78cf2363f9e3bbfb759a33
  summary: 'Current identity verified: Azotobacter vinelandii species. Taxonomic identity
    alone is not evidence of compartment occurrence or protein membership.'
- evidence_id: micro-tax322710
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/322710
  locator: Exact ENA taxonomy tax-id response, scientific name, rank and alternate
    names
  accessed_at: '2026-11-03T12:28:40.772847Z'
  support: supports
  snapshot_sha256: 640e4da8d9e091562874f24c48830f375c806b9c6030617196a029b54d991a92
  summary: 'Current identity verified: Azotobacter vinelandii DJ strain. Taxonomic
    identity alone is not evidence of compartment occurrence or protein membership.'
- evidence_id: micro-protein-C1DK95
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/C1DK95.json
  locator: 'Current exact UniProtKB entry: accession, entry type, protein name, primary/synonym
    gene names, organism and taxon, cross-reference context'
  accessed_at: '2026-11-03T12:28:40.772929Z'
  support: supports
  snapshot_sha256: 5b56dc3bffa97f76f8ef0c68cff14396ac65857c7ad1e1753535e0cbcf10317a
  summary: Current accession tuple agrees with record. Unreviewed strain-DJ entry
    has primary anfH and native nifH synonym; this does not make it an Epithemia protein
    or prove all examples form one native complex.
- evidence_id: micro-protein-P07328
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P07328.json
  locator: 'Current exact UniProtKB entry: accession, entry type, protein name, primary/synonym
    gene names, organism and taxon, cross-reference context'
  accessed_at: '2026-11-03T12:28:40.844945Z'
  support: supports
  snapshot_sha256: 35fe0f5c7fb2778ad622cc32e76900ccd03e4d7c90bbfb808bd7cdabd4b36d60
  summary: Current accession tuple agrees with record. Reviewed Azotobacter nifD alpha-chain
    identity, not an organelle-specific instance.
- evidence_id: micro-protein-P07329
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P07329.json
  locator: 'Current exact UniProtKB entry: accession, entry type, protein name, primary/synonym
    gene names, organism and taxon, cross-reference context'
  accessed_at: '2026-11-03T12:28:41.260155Z'
  support: supports
  snapshot_sha256: a0bdaa2b7c5298dfd8d8dfb63cc01ebe8d7322f68d3692f13239a04e71cf062e
  summary: Current accession tuple agrees with record. Reviewed Azotobacter nifK beta-chain
    identity, not an organelle-specific instance.
- evidence_id: micro-query-nifD
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=100&query=reviewed%3Atrue%20AND%20gene_exact%3AnifD%20AND%20organism_id%3A354
  locator: UniProt first and only response page, native total-results header and no
    next-page Link; accession/gene/taxon/InterPro fields inspected
  accessed_at: '2026-11-03T12:29:29.343336Z'
  support: supports
  snapshot_sha256: 5b70d184c21e41b355b5d24c17705c69d02f01cde046d1fdd1a77c9deb3cf7b3
  summary: The bounded exact-symbol/taxon reviewed query returns the single stated
    accession, confirming present query uniqueness without broad family absence.
  search_scope: UniProtKB search on2026-11-03; literal query reviewed:true AND gene_exact:nifD
    AND organism_id:354; size100; returned 1 total results, no next-page Link. Scope
    is reviewed entries matching this literal query, including gene synonyms; no exhaustive
    unreviewed/family search.
- evidence_id: micro-query-nifK
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=100&query=reviewed%3Atrue%20AND%20gene_exact%3AnifK%20AND%20organism_id%3A354
  locator: UniProt first and only response page, native total-results header and no
    next-page Link; accession/gene/taxon/InterPro fields inspected
  accessed_at: '2026-11-03T12:29:29.343580Z'
  support: supports
  snapshot_sha256: 16514a2de65fca33146cab3fb0827c05ddddafe0d74150a7c8b5af1db7f42dab
  summary: The bounded exact-symbol/taxon reviewed query returns the single stated
    accession, confirming present query uniqueness without broad family absence.
  search_scope: UniProtKB search on2026-11-03; literal query reviewed:true AND gene_exact:nifK
    AND organism_id:354; size100; returned 1 total results, no next-page Link. Scope
    is reviewed entries matching this literal query, including gene synonyms; no exhaustive
    unreviewed/family search.
- evidence_id: micro-query-hupL
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=100&query=reviewed%3Atrue%20AND%20gene_exact%3AhupL
  locator: UniProt first and only response page, native total-results header and no
    next-page Link; accession/gene/taxon/InterPro fields inspected
  accessed_at: '2026-11-03T12:29:29.343669Z'
  support: supports
  snapshot_sha256: 3ce917f9bcc84499fcffa4b90649c089de78bf0b65b6a64f22803796198672ac
  summary: 'Eight reviewed exact-name/synonym hits: six large-subunit proteins carry
    IPR001501/IPR050867; two hits P26409/P28154 are HypA accessory proteins sharing
    hupL synonym and are excluded from large-subunit interpretation. Symbol search
    does not prove identity or exhaustive family specificity.'
  search_scope: UniProtKB search on2026-11-03; literal query reviewed:true AND gene_exact:hupL;
    size100; returned 8 total results, no next-page Link. Scope is reviewed entries
    matching this literal query, including gene synonyms; no exhaustive unreviewed/family
    search.
- evidence_id: micro-IPR001501
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001501
  locator: InterPro exact entry name,type,member models and broad family metadata;
    descriptions distinguished from primary experimental evidence
  accessed_at: '2026-11-03T12:28:41.357528Z'
  support: supports
  snapshot_sha256: b14fc4df0605b35be81443ab2df264375afe2fb9c9558620934c63bf323510da
  summary: Entry covers a broad nickel-dependent/[NiFe]/[NiFeSe] hydrogenase large-subunit
    family rather than an exact uptake-specific Epithemia equivalog. Family identity
    supports the bounded grounding limitation, not a proof that no narrower family
    exists.
- evidence_id: micro-IPR050867
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050867
  locator: InterPro exact entry name,type,member models and broad family metadata;
    descriptions distinguished from primary experimental evidence
  accessed_at: '2026-11-03T12:28:41.421457Z'
  support: supports
  snapshot_sha256: 0ed4967d74f420dc78de13398476e2561621e68bc750fcb0e074af464ed7e4ac
  summary: Entry covers a broad nickel-dependent/[NiFe]/[NiFeSe] hydrogenase large-subunit
    family rather than an exact uptake-specific Epithemia equivalog. IPR050867 description
    is explicitly marked LLM-generated and not reviewed; it is not used as primary
    mechanistic proof.
- evidence_id: micro-moulin2024-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1093/ismeco/ycae055%22
  locator: Europe PMC exact DOI core metadata and complete primary abstract; body
    access separately scoped
  accessed_at: '2026-11-03T12:28:41.452906Z'
  support: supports
  snapshot_sha256: 297c7065134d81815f4dfad2cd5f1adb065f558730078a50917a1a9d5fc42944
  summary: Exact bibliographic identity verified. Abstract stronger abolition wording
    is not substituted for the Results approximately60% reduction.
- evidence_id: micro-frail2025-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1073/pnas.2507237122%22
  locator: Europe PMC exact DOI core metadata and complete primary abstract; body
    access separately scoped
  accessed_at: '2026-11-03T12:28:41.518849Z'
  support: supports
  snapshot_sha256: 401422446b1d50c3378aa1a08f7cf3d7df2fa20b338457e61ea12a6a8c45eb08
  summary: Exact bibliographic identity verified. Final2025 PNAS paper, not the differently
    titled2024 preprint.
- evidence_id: micro-porto2000-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1078/0171-9335-00112%22
  locator: Europe PMC exact DOI core metadata and complete primary abstract; body
    access separately scoped
  accessed_at: '2026-11-03T12:28:41.966197Z'
  support: supports
  snapshot_sha256: 471a381dd60a54bed5d6a5e5e925aac4cf14d83489b0e01578ed4f5a64164bb5
  summary: Exact bibliographic identity verified. Primary abstract directly traces
    gold-protein cargo through cytostome/cytopharynx, vesicles/tubules and reservosomes;
    authors propose early-endosome identity from acidic staining and uptake kinetics.
    It does not establish equivalent lipid-tracer transit.
- evidence_id: micro-moulin2024-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC11070190.1/PMC11070190.1.xml
  locator: 'Genuine PMC11070190.1 JATS: Introduction sec3, Methods pointer sec4, Results
    sec6–10, Discussion sec11–15, Figure2 full caption and front licence/author metadata;
    Fig1/3/4 captions/text only'
  accessed_at: '2026-11-03T12:28:42.052068Z'
  support: supports
  snapshot_sha256: 157f4056917d22266a43cbdab6bd9b52b3c597ac2759382f9c576ecb349988b9
  summary: Primary E.clementina isotope/immunoblot/physiology results support nitrogenase
    membership, host nitrogen supply and carbon exchange, with nonaxenic model and
    process-level scope. Daytime darkness/DCMU reduces activity~60%; transport species,
    respiration mechanism and molecular division/import remain unresolved. CC BY4.0
    and Figure2 provenance verified. No claim to inspect Fig1/3/4 pixels, cited studies,
    raw genomes or quantitative data.
- evidence_id: micro-moulin2024-supp
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC11070190.1/ismecomm-supplementals-submitted_ycae055.pdf
  locator: 'Supplementary PDF text: Strain isolation/cultivation (PDFpp1–2), sequencing/phylogeny/metagenomics
    (pp2–3), Isotope labeling/NanoSIMS and IRMS (pp3–5), TEM/activity assay (pp5–6),
    Protein extraction/immunoblot through antibody specification (pp6–7); text extraction,
    not supplement figure pixels'
  accessed_at: '2026-11-03T12:29:29.343732Z'
  support: supports
  snapshot_sha256: ed5777cb68be7caa67a49e7b962e32fae126925823a701897e9f92b4fd90506f
  summary: Gazos Creek near Butano model and monoalgal-but-nonaxenic culture confirmed.
    Isotope workflow separates compartments with morphology/signal-based ROI and recognizes
    preparation limits; ARA measures culture activity, and immunoblots support NifDK/HupL
    detection with stated antibody scope. Does not establish localization by immunofluorescence
    or a hydrogen-flux assay.
- evidence_id: micro-frail2025-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC12377750.1/PMC12377750.1.xml
  locator: 'Genuine PMC12377750.1 JATS: complete unheaded Introduction, Results s5–7,
    complete Discussion s8, Methods diazoplast isolation/proteomics s18–19; text/captions
    only'
  accessed_at: '2026-11-03T12:28:42.069666Z'
  support: supports
  snapshot_sha256: bcde5c298db3fa11f7c070e5b593219287d6b58a8f11d880f114dd4a6073dff3
  summary: All-described-Epithemia occurrence and independent diazoplast/nitroplast
    origins are stated, without genus-wide physiological uniformity. Six enriched
    host proteins remain localization candidates; TusA undetected and PFK import unsupported.
    Genetic integration and transport/division hypotheses remain bounded. Did not
    re-audit complete genome Results s2–4 or supplementary datasets; no image pixels
    from this paper reviewed.
- evidence_id: micro-frail2025-supp
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC12377750.1/pnas.2507237122.sapp.pdf
  locator: Supporting Information PDFp2, Generation of axenic culture paragraph; neighboring
    SEM paragraph read only as context
  accessed_at: '2026-11-03T12:29:29.343789Z'
  support: supports
  snapshot_sha256: fa483be9c11980f38824bd74793d0aac11028a6885d156f694113c2365ab11d6
  summary: Later axenic sequencing cultures were derived from initially clonal xenic
    E.clementina; this is a different study context from Moulin2024 nonaxenic physiology.
    Other supplement contents were not independently audited.
- evidence_id: micro-moulin2024-f2
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC11070190.1/ycae055f2.jpg
  locator: Native PMC11070190.1/ycae055f2.jpg exact asset; SHA256 compared to frozen
    maintained image and pixels viewed through identical local file
  accessed_at: '2026-11-03T12:28:42.161145Z'
  support: supports
  snapshot_sha256: b8aae76bbe0c1d74896370bae92524c6764ea2795b1ddfa2309c5fc28dc74366
  summary: 'Native asset byte-identical to maintained Figure2: SHA256b8aae76bbe0c1d74896370bae92524c6764ea2795b1ddfa2309c5fc28dc74366;
    MD5 7141c250f82b9bd5c6a25e546aa7d444 agrees with source object listing. Complete
    A–C panel and taxon/context attribution preserved.'
- evidence_id: micro-moulin2024-package
  kind: database
  reference: https://pmc-oa-opendata.s3.amazonaws.com/?prefix=PMC11070190.1/&max-keys=1000
  locator: PMC OA S3 prefix listing PMC11070190.1/, max-keys1000, IsTruncated=false;
    exact image key,size and ETag
  accessed_at: '2026-11-03T12:28:42.523502Z'
  support: context_only
  snapshot_sha256: cf6bef003a03d9eb957216cd49a2a288bfc4a4a72b4ce5aa3a89006e0998c680
  summary: Native version1 package lists ycae055f2.jpg size102607 and ETag matching
    computed MD5. Licence authority is article JATS CC BY4.0, not the different Frail2025
    licence.
- evidence_id: micro-porto2000-publisher
  kind: authority
  reference: https://www.sciencedirect.com/science/article/pii/S0171933504700989
  locator: Actual ScienceDirect PII S0171933504700989 HTTP403 access response
  accessed_at: '2026-11-03T12:28:42.538555Z'
  support: context_only
  snapshot_sha256: fad5de279aeb11cfb4251f07eb46a756e5259e3991e7cc5ded7182d06ce28bee
  summary: Primary full body not recovered through this route; response is not scientific
    evidence.
- evidence_id: micro-porto2000-api
  kind: authority
  reference: https://api.elsevier.com/content/article/PII:S0171933504700989?httpAccept=text/xml
  locator: Actual public Elsevier API response XML, core metadata/openaccess flag;
    no article body
  accessed_at: '2026-11-03T12:28:42.549709Z'
  support: context_only
  snapshot_sha256: 0be172150cd46cead47bcf78fdc3c95acd836f8e1472969a4cc3d53e826be029
  summary: API returned HTTP200 bibliographic stub, not readable primary body. The
    current review remains complete-primary-abstract-only for Porto2000; no strain,
    methods or figure-pixel check claimed.
- evidence_id: micro-diazoplast-go-search
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=diazoplast&limit=100&page=1
  locator: QuickGO literal query diazoplast, limit100,page1; complete zero-hit response
  accessed_at: '2026-11-03T12:28:42.616642Z'
  support: supports
  snapshot_sha256: f3a7dae9b1e9335291e3940cdf0e5f8dadf9335da7b9547710606b5106c63f86
  summary: Bounded current query has zero hits; supports retaining minted identity
    provisionally together with positive structural/source evidence, not universal
    ontology absence.
  search_scope: QuickGO GO text search on2026-11-03, query=diazoplast, limit100,page1;
    response numberOfHits0 and empty results. This is one literal query, not an exhaustive
    search of synonyms, all ontologies or historical versions.
- evidence_id: micro-catalogue
  kind: search
  reference: https://imodulondb.org/api/datasets
  locator: Complete official iModulonDB/api/datasets response; every organism ID/name
    and dataset-array row inspected
  accessed_at: '2026-11-03T12:28:42.585058Z'
  support: supports
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  summary: No catalogue entry matches Epithemia/diazoplast, Crocosphaera/Cyanothece,
    Azotobacter or Trypanosoma. Other diazotrophs and Synechococcus are not organism
    proxies; no matching downstream gene/module query applies. No biological absence
    or lack-of-expression inference.
  search_scope: iModulonDB unfiltered public/api/datasets GET on2026-11-03; all20
    returned organism rows/28 organism-dataset pairs, no client truncation/pagination.
    Inspected names/IDs for Epithemia/clementina, diazoplast, Crocosphaera/Cyanothece,
    Azotobacter/vinelandii/DJ and Trypanosoma/cruzi. Scope limited to this catalogue.
- evidence_id: micro-historical-adapter-runner
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Retained actual00:49Z native datasets attempt, exit1 OS PermissionError
    reading runner pyvenv.cfg
  accessed_at: '2026-11-03T00:49:00.848907Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  summary: Historical runner unavailability retained at its real earlier time; no
    fresh runner invocation claimed. Actual current catalogue source fallback inspected
    per native policy.
- evidence_id: septin-review-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Structured Source Cross-Checks and immutable review contract
  summary: Affirmative pathway context triggers applicability assessment even where
    molecular graph mechanisms are excluded. Expression-only non-inference is not
    an exemption; unmatched catalogue coverage is not negative biology.
  accessed_at: '2026-11-03T12:30:29.048293Z'
  support: supports
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: septin-curation-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Identity, material components, source scope and evidence
  summary: Whole carriers, their constituent membrane bilayers and enclosed regions
    are distinct. Generic constituent material, subtype-specific coat/cargo and formation
    machinery are not interchangeable.
  accessed_at: '2026-11-03T12:30:29.048293Z'
  support: supports
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
- evidence_id: septin-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: NONMECHANISTIC graphs and scoped evidence
  summary: Topological relations and broad transport context may be nonmechanistic;
    a qualified source experiment does not establish a universal vesicle mechanism.
  accessed_at: '2026-11-03T12:30:29.048293Z'
  support: supports
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: septin-record-cytoplasmic_vesicle
  kind: record_content
  reference: data/structures/membrane_organelle/cytoplasmic_vesicle.yaml
  locator: Entire current maintained record at cd5be11ad13304d75404a51d097635022d1bd091
  summary: Read all identity, definition, history, hierarchy, material component,
    taxon/canonical, function, evidence, graph edges and discussions. No target image,
    quantitative property, trait link, verbatim snippet or individual protein accession
    is declared.
  accessed_at: '2026-11-03T12:30:29.048293Z'
  support: supports
  snapshot_sha256: f4704b74324c18cab955983a27173d6a98fae0153bc7a403cbbe3c865e4eba84
- evidence_id: septin-original-cytoplasmic_vesicle
  kind: prior_review
  reference: reviews/structured/20261022T013529Z-cytoplasmic-vesicle-audit/review.yaml
  locator: Original YAML and deterministic Markdown; frozen inputs, checks, source
    tiers, assessments, findings/actions and limits
  summary: Original membrane has one minor F1 carrier-versus-bilayer wording finding;
    whole and lumen have none. Historical global/source claims remain historical.
    The existing adapter row uses an unsupported expression-only exemption.
  accessed_at: '2026-11-03T12:30:29.048293Z'
  support: supports
  snapshot_sha256: 28e7e5777617f9550a87a3e10115a2d76c6839cc0b1ea0d65968f27a1a747d27
- evidence_id: septin-original-validation-cytoplasmic_vesicle
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/adversary-septin/original-checks.json
  locator: 20261022T013529Z-cytoplasmic-vesicle-audit native validate/render and frozen
    historical/current target hashes
  summary: Both native commands exited zero; Markdown matches exactly, and original-source/current
    hashes equal the frozen target input.
  accessed_at: '2026-11-03T12:28:23.463330Z'
  support: supports
  snapshot_sha256: 9379f0b2c3c1d3373fce7d7aab1a1b080d160cfee2cea1b910795c83c784162a
- evidence_id: septin-native-cytoplasmic_vesicle-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/cytoplasmic_vesicle-uniprot-verify-receipt.json
  locator: Actual root command receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/cytoplasmic_vesicle-uniprot-verify.log
  summary: Exit zero. No protein examples or UniProtKB graph xrefs and zero GENE_OR_PROTEIN
    graph nodes. Native execution success covers only this empty represented inventory,
    not narrative pathway mechanisms, source-localized molecular actors or completeness.
  accessed_at: '2026-11-03T12:28:25.941225Z'
  support: supports
  snapshot_sha256: 4e6d98ea217b91786eb6c5201c1536021a6ae0b3b5974827b481bf29bf09d744
- evidence_id: septin-native-cytoplasmic_vesicle-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/cytoplasmic_vesicle-uniprot-causal-receipt.json
  locator: Actual root command receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/cytoplasmic_vesicle-uniprot-causal.log
  summary: Exit zero. No protein examples or UniProtKB graph xrefs and zero GENE_OR_PROTEIN
    graph nodes. Native execution success covers only this empty represented inventory,
    not narrative pathway mechanisms, source-localized molecular actors or completeness.
  accessed_at: '2026-11-03T12:28:26.393990Z'
  support: supports
  snapshot_sha256: 8d18df7d3567d611ff84c45fa8f52b9e25020d19579b14d0c24c5fb8dd245d27
- evidence_id: septin-record-cytoplasmic_vesicle_lumen
  kind: record_content
  reference: data/structures/membrane_organelle/cytoplasmic_vesicle_lumen.yaml
  locator: Entire current maintained record at cd5be11ad13304d75404a51d097635022d1bd091
  summary: Read all identity, definition, history, hierarchy, material component,
    taxon/canonical, function, evidence, graph edges and discussions. No target image,
    quantitative property, trait link, verbatim snippet or individual protein accession
    is declared.
  accessed_at: '2026-11-03T12:30:29.048293Z'
  support: supports
  snapshot_sha256: 87d5a5379cb643e40257e60c99a3308f2b6e6a49aa079856fb501fe6e3c738fe
- evidence_id: septin-original-cytoplasmic_vesicle_lumen
  kind: prior_review
  reference: reviews/structured/20261022T013530Z-cytoplasmic-vesicle-lumen-audit/review.yaml
  locator: Original YAML and deterministic Markdown; frozen inputs, checks, source
    tiers, assessments, findings/actions and limits
  summary: Original membrane has one minor F1 carrier-versus-bilayer wording finding;
    whole and lumen have none. Historical global/source claims remain historical.
    The existing adapter row uses an unsupported expression-only exemption.
  accessed_at: '2026-11-03T12:30:29.048293Z'
  support: supports
  snapshot_sha256: 7cd480b7fd9a364ecae7d01c4f95bb8a64fae0577c237fb847140ca506cd3297
- evidence_id: septin-original-validation-cytoplasmic_vesicle_lumen
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/adversary-septin/original-checks.json
  locator: 20261022T013530Z-cytoplasmic-vesicle-lumen-audit native validate/render
    and frozen historical/current target hashes
  summary: Both native commands exited zero; Markdown matches exactly, and original-source/current
    hashes equal the frozen target input.
  accessed_at: '2026-11-03T12:28:24.828937Z'
  support: supports
  snapshot_sha256: 9379f0b2c3c1d3373fce7d7aab1a1b080d160cfee2cea1b910795c83c784162a
- evidence_id: septin-native-cytoplasmic_vesicle_lumen-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/cytoplasmic_vesicle_lumen-uniprot-verify-receipt.json
  locator: Actual root command receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/cytoplasmic_vesicle_lumen-uniprot-verify.log
  summary: Exit zero. No protein examples or UniProtKB graph xrefs and zero GENE_OR_PROTEIN
    graph nodes. Native execution success covers only this empty represented inventory,
    not narrative pathway mechanisms, source-localized molecular actors or completeness.
  accessed_at: '2026-11-03T12:28:26.842925Z'
  support: supports
  snapshot_sha256: 36a02298bc97caa4c86580dce82f36e9f8250793cee030c0a31ed61c331fca8b
- evidence_id: septin-native-cytoplasmic_vesicle_lumen-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/cytoplasmic_vesicle_lumen-uniprot-causal-receipt.json
  locator: Actual root command receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/cytoplasmic_vesicle_lumen-uniprot-causal.log
  summary: Exit zero. No protein examples or UniProtKB graph xrefs and zero GENE_OR_PROTEIN
    graph nodes. Native execution success covers only this empty represented inventory,
    not narrative pathway mechanisms, source-localized molecular actors or completeness.
  accessed_at: '2026-11-03T12:28:27.290563Z'
  support: supports
  snapshot_sha256: 59c4cd48c54df91d2e2882edae3bee1557ba22c469b20a8f14b6b374b3fcd429
- evidence_id: septin-record-cytoplasmic_vesicle_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/cytoplasmic_vesicle_membrane.yaml
  locator: Entire current maintained record at cd5be11ad13304d75404a51d097635022d1bd091
  summary: Read all identity, definition, history, hierarchy, material component,
    taxon/canonical, function, evidence, graph edges and discussions. No target image,
    quantitative property, trait link, verbatim snippet or individual protein accession
    is declared.
  accessed_at: '2026-11-03T12:30:29.048293Z'
  support: supports
  snapshot_sha256: 112643d19f662095c8d81c907d5d6435fe93b612f8a037df2af0fe66af87d4aa
- evidence_id: septin-original-cytoplasmic_vesicle_membrane
  kind: prior_review
  reference: reviews/structured/20261022T013531Z-cytoplasmic-vesicle-membrane-audit/review.yaml
  locator: Original YAML and deterministic Markdown; frozen inputs, checks, source
    tiers, assessments, findings/actions and limits
  summary: Original membrane has one minor F1 carrier-versus-bilayer wording finding;
    whole and lumen have none. Historical global/source claims remain historical.
    The existing adapter row uses an unsupported expression-only exemption.
  accessed_at: '2026-11-03T12:30:29.048293Z'
  support: supports
  snapshot_sha256: bca15f1dfaa8c49be3a41da7df6e1c09d0c6cf1b59979f21ea033d9be5756d39
- evidence_id: septin-original-validation-cytoplasmic_vesicle_membrane
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/adversary-septin/original-checks.json
  locator: 20261022T013531Z-cytoplasmic-vesicle-membrane-audit native validate/render
    and frozen historical/current target hashes
  summary: Both native commands exited zero; Markdown matches exactly, and original-source/current
    hashes equal the frozen target input.
  accessed_at: '2026-11-03T12:28:26.157810Z'
  support: supports
  snapshot_sha256: 9379f0b2c3c1d3373fce7d7aab1a1b080d160cfee2cea1b910795c83c784162a
- evidence_id: septin-native-cytoplasmic_vesicle_membrane-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/cytoplasmic_vesicle_membrane-uniprot-verify-receipt.json
  locator: Actual root command receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/cytoplasmic_vesicle_membrane-uniprot-verify.log
  summary: Exit zero. No protein examples or UniProtKB graph xrefs and zero GENE_OR_PROTEIN
    graph nodes. Native execution success covers only this empty represented inventory,
    not narrative pathway mechanisms, source-localized molecular actors or completeness.
  accessed_at: '2026-11-03T12:28:27.744854Z'
  support: supports
  snapshot_sha256: d75ceb65e537eb45047fd798a41390bb96b4048137c3f63d3e152a05fb93a386
- evidence_id: septin-native-cytoplasmic_vesicle_membrane-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/cytoplasmic_vesicle_membrane-uniprot-causal-receipt.json
  locator: Actual root command receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/cytoplasmic_vesicle_membrane-uniprot-causal.log
  summary: Exit zero. No protein examples or UniProtKB graph xrefs and zero GENE_OR_PROTEIN
    graph nodes. Native execution success covers only this empty represented inventory,
    not narrative pathway mechanisms, source-localized molecular actors or completeness.
  accessed_at: '2026-11-03T12:28:28.181229Z'
  support: supports
  snapshot_sha256: 1356fedf7c81910938700642670d7b750aea9e930ef59d97c9e75229d1a13bd3
- evidence_id: septin-context-cvt_vesicle
  kind: record_content
  reference: data/structures/membrane_organelle/cvt_vesicle.yaml
  locator: 'Boundary fields only: identifier, label, definition, structure_kind, parents,
    part_of and has_part'
  summary: Frozen before inspection. Whole Cvt carrier and either surrounding bilayer
    retain distinct exact identities and correct cytoplasmic-vesicle versus cytoplasmic-vesicle-membrane
    subtype relations. No whole-neighbor audit or disposition of its findings is asserted.
  accessed_at: '2026-11-03T12:30:29.048293Z'
  support: supports
  snapshot_sha256: cf6eb5075a057a0b8b104cbacb61cdf895298eb4b018945a08b46bcb939c8b0c
- evidence_id: septin-context-cvt_vesicle_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/cvt_vesicle_membrane.yaml
  locator: 'Boundary fields only: identifier, label, definition, structure_kind, parents,
    part_of and has_part'
  summary: Frozen before inspection. Whole Cvt carrier and either surrounding bilayer
    retain distinct exact identities and correct cytoplasmic-vesicle versus cytoplasmic-vesicle-membrane
    subtype relations. No whole-neighbor audit or disposition of its findings is asserted.
  accessed_at: '2026-11-03T12:30:29.048293Z'
  support: supports
  snapshot_sha256: 679cdeb18f93b2ecf38916c132f8461121e7067f0db52e4b24842559b39dbb67
- evidence_id: septin-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031410,GO:0031982,GO:0030659,GO:0060205,GO:0031983,GO:0016020,GO:0033107,GO:0033110
  locator: 'All eight exact terms: identity, definition, active status, synonyms and
    relevant typed child relations'
  summary: GO0031410 whole cytoplasmic vesicle, GO0030659 membrane and GO0060205 lumen
    are distinct. GO0031983 is the lumen is-a parent. GO0033107 is the whole double-membrane
    Cvt carrier and GO0033110 is either constituent bilayer; both are correctly subtyped
    under their corresponding generic classes. The membrane occurrence note conflates
    those levels. Broader membrane/vesicle definitions remain compatible with asserted
    hierarchy, without implying every listed parent is an immediate GO edge.
  accessed_at: '2026-11-03T12:28:10.742368Z'
  support: supports
  snapshot_sha256: 14fe6ad5b9c3ff039107f2dcfbbdf4804a68320e9f4a2e9b2935a0412a5ea28b
- evidence_id: septin-tax4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Exact taxId, scientificName, rank and lineage
  summary: Taxon4932 is the species Saccharomyces cerevisiae. Species identity does
    not by itself verify strain, quantitative prevalence or every subtype mechanism.
  accessed_at: '2026-11-03T12:28:10.742822Z'
  support: supports
  snapshot_sha256: 38f43dd1593a1d47416228ae385464f30aeb8302c3aadb45b3588d03744bc814
- evidence_id: septin-SL0088
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0088.json
  locator: Native entry id/name/definition, immediate isA/partOf and nested GO mappings
  summary: SL0088 maps exactly to GO0031410, with broader vesicle parentage. Its native
    prose supports broad secretory/endocytic transport and lists clathrin/COPI/COPII,
    synaptic, secretory and phagosome subtypes. Such examples do not make all their
    coats or cargo universal constituents.
  accessed_at: '2026-11-03T12:28:10.742648Z'
  support: supports
  snapshot_sha256: 00d81fd831a7300d9d7f3c1cb93f3da2f2ae88ba71a4424e42cb4a66a34c5756
- evidence_id: septin-SL0089
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0089.json
  locator: Native entry id/name/definition, immediate isA/partOf and nested GO mappings
  summary: SL0089 maps exactly to GO0030659, is_a membrane and part_of cytoplasmic
    vesicle and endomembrane system. It describes a surrounding membrane, not the
    complete carrier or a single molecular lipid species.
  accessed_at: '2026-11-03T12:28:10.742730Z'
  support: supports
  snapshot_sha256: 8835a54edcae28175c570b05842e2d000be27c06c058a6d778589e05af647e41
- evidence_id: septin-SL0325
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0325.json
  locator: Native entry id/name/definition, immediate isA/partOf and nested GO mappings
  summary: SL0325 maps exactly to GO0060205 and part_of cytoplasmic vesicle. Its definition
    supports a membrane-bounded compartment, not a universal cargo list or independent
    transport function.
  accessed_at: '2026-11-03T12:28:10.742782Z'
  support: supports
  snapshot_sha256: bc69c26c5fddf3a823c5587c17a17918b33094053f3311caa82f044acee4986e
- evidence_id: septin-reggiori2004-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A15004240%20AND%20SRC%3AMED
  locator: Complete primary abstract plus exact title/authors/year/DOI/PMID/PMCID
    and research article type
  summary: Cached public-source snapshot fetched during PR2362 and independently reread
    for this review. Reggiori et al.2004 PMID15004240 DOI10.1091/mbc.e03-07-0479 supports
    budding-yeast double-membrane Cvt transport and condition-dependent early-secretory
    contributions, retaining membrane-origin uncertainty.
  accessed_at: '2026-11-03T11:51:54.023844Z'
  support: supports
  snapshot_sha256: 923b0a91aaa2e0a2ecc4153f810d909c42f0129f6a71ea504c25908ef75af1a8
  search_scope: Europe PMC exact EXT_ID:15004240 AND SRC:MED, format=json/resultType=core,
    one matched result returned, no date filter. Original fetch 2026-11-03T11:51:54.023844Z
    retained; cached body reread for PR2363, no fresh API invocation or broad absence
    search claimed.
- evidence_id: septin-reggiori2004-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC404015/
  locator: 'Cached genuine PMC404015 HTML independently reread: complete Introduction
    sec1, Methods Strains and Media sec3/Table1, Results sec14/Figure8 text caption,
    Discussion sec17 and sec18/Figure9 text caption. No full-paper, image-pixel or
    raw-data audit.'
  summary: Public body fetched during PR2362 at the retained timestamp; hash verified
    and reread for current claims. The paper distinguishes double-membrane cytosolic
    carriers from their bilayers, inner-body release after fusion and cargo delivery.
    Listed yeast strains and sec12 timing experiments support the canonical example
    while showing incomplete transport inhibition. ER/Golgi origin remains unresolved;
    maturation and assembly schemes are models, not universal demonstrated mechanisms.
    Introductory cited-study synthesis is not new direct evidence from every cited
    experiment.
  accessed_at: '2026-11-03T11:52:44.039650Z'
  support: supports
  snapshot_sha256: c6e920f0e7dc866b10c1bdc179d4cc63604ffd4b349682f6d4243ba131254553
- evidence_id: septin-source-reuse-receipt
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/adversary-septin/reused-source-receipts.json
  locator: Retained actual fetch receipts, snapshot paths/hashes and PR2363 reread
    time
  summary: Reggiori metadata actual fetch11:51:54.023844Z and body11:52:44.039650Z
    are retained; no new fetch is invented. Hashes of both public snapshots were rechecked
    before current reassessment.
  accessed_at: '2026-11-03T12:28:34.508302Z'
  support: supports
  snapshot_sha256: dcfaf9006b6c7bc4c2195bcc67778afb2a8f517b9e19ae7328127e2036b3617c
- evidence_id: septin-catalogue
  kind: search
  reference: https://imodulondb.org/api/datasets
  locator: Complete official organism list and all returned organism/dataset keys
  summary: No matching Saccharomyces cerevisiae/yeast dataset is returned. All three
    records affirmatively cite Cvt/early-secretory pathway context, even when their
    graph omits molecular steps. Source applicability is assessed, but downstream
    unmatched-host gene/module queries are not justified. This is not biological absence.
  accessed_at: '2026-11-03T12:28:11.442991Z'
  support: supports
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  search_scope: Official GET /api/datasets at 2026-11-03T12:28:11.442991Z; complete
    returned organism/dataset catalogue inspected for Saccharomyces/cerevisiae/yeast,
    no date filter. No unrelated-organism substitution or downstream module query.
- evidence_id: septin-historical-adapter-runner
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Actual historical datasets invocation00:49:00.848907Z–00:49:00.863225Z
  summary: Retained canary invocation exited1 with PermissionError reading pyvenv.cfg.
    This is historical unavailable-runner evidence, not a new invocation or successful
    execution. Fresh official catalogue fallback was inspected separately.
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: septin-source-access
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/adversary-septin/source-receipts.json
  locator: Actual fresh source URLs, timestamps and hashes
  summary: Current GO, three UniProt location entries, ENA taxon and official catalogue
    fetched successfully. Scientific paper metadata/body are explicitly cached and
    separately hash-verified/reread; fresh authority access does not imply fresh full-text
    access.
  accessed_at: '2026-11-03T12:30:29.048293Z'
  support: supports
  snapshot_sha256: c17652175a8ba822ae1165125d457a76c44bbe457ec9047c1c7301f3f7f7f12d
- evidence_id: check-qc
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/qc.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T12:34:04.702448Z'
  support: supports
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  snapshot_sha256: 9e7cdfbf9e298fea36fd45a616df90126a03aa626a8adb9bc7c330e8b6c2fdeb
- evidence_id: check-labels
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/labels.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T12:28:51.641579Z'
  support: supports
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  snapshot_sha256: 6cdfb05df9a27194f05a5fd7f851783f817ac1523ca0bbfa54fe0e0d18775905
- evidence_id: check-trait-links
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/trait-links.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T12:28:28.797351Z'
  support: supports
  summary: Native TraitMech link check passed.
  snapshot_sha256: 8b336cdefbbd3daf6da8787990efdbe346c95e2c8361d50b7eb68a18f2d5a44a
- evidence_id: check-vendored
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/vendored.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T12:28:26.011818Z'
  support: supports
  summary: Pinned governed files match; native vendored check passed.
  snapshot_sha256: b1f169d103aaefa930745468bcca171e5867b9cc49e4e74311e458097e3252a6
- evidence_id: check-curies
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/curies.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T12:28:27.639423Z'
  support: supports
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  snapshot_sha256: bc12b1285f5747707643f7a98e03dbb3a6c88fb062ad49f99db9cb42ececf3d2
- evidence_id: focused
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/focused-results.json
  locator: All twenty actual target schema/strict command outputs
  accessed_at: '2026-11-03T12:35:23Z'
  support: supports
  summary: Ten schema and ten strict commands returned exit zero.
  snapshot_sha256: 42f3a28ce9031835ddaacad115a7dcc79c06fc24220526b1b64087a3d37f7786
- evidence_id: supplemental-pmid
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2363/pmid-chunks-receipt.json
  locator: Complete native-report PMID set checked with unchanged resolver in batches
    of at most fifty
  accessed_at: '2026-11-03T12:29:28.623524Z'
  support: supports
  summary: 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers
    remain unverified.
  snapshot_sha256: 1fbb9f27b404f95e246ae2ed0616294ce132001b0712d0592b9a246c164002e5
- evidence_id: historical-adapter-runner-availability
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical runner invocation receipt, cross-checked against exact stdout/stderr
    hashes; reread during PR2363 synthesis
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  summary: Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS
    PermissionError reading the configured runner pyvenv.cfg. This is a retained historical
    availability observation, not a fresh attempt or a scientific validation failure.
    Native policy permits inspected source-catalogue fallback.
assessments:
- assessment_id: plaque-t0-native
  area: schema
  topic: Native protein and graph inventories
  outcome: supported
  summary: Both commands pass empty represented protein inventories and zero GENE_OR_PROTEIN
    nodes. Mechanical checks do not certify primary-source biology or establish a
    complete proteome.
  target_ids:
  - GO:0009843
  evidence_ids:
  - plaque-current-0
  - plaque-native-cyanelle_thylakoid-verify
  - plaque-native-cyanelle_thylakoid-causal
- assessment_id: plaque-t0-provenance
  area: provenance
  topic: Original lineage and unchanged frozen record
  outcome: supported
  summary: Original validates/renders exactly and all12 historical input hashes match.
    Current target unchanged; no stale input needs refresh. Original findings/actions
    empty. Historical record issues are context only, not reclosed or recertified.
  target_ids:
  - GO:0009843
  evidence_ids:
  - plaque-current-0
  - plaque-original-0
  - plaque-original-checks
- assessment_id: plaque-t0-coverage
  area: completeness
  topic: Entire maintained record and bounded science
  outcome: supported
  summary: All maintained fields, histories, discussions and graph edges read. No
    target images, snippets, quantitative properties or named protein examples are
    represented. No optional molecular inventory is fabricated. No scientific curation
    defect established at declared evidence tiers.
  target_ids:
  - GO:0009843
  evidence_ids:
  - plaque-current-0
  - plaque-policy
  - plaque-rubric
- assessment_id: plaque-t0-taxonomy
  area: scope
  topic: Exact organism/class and qualitative occurrence
  outcome: supported
  summary: ENA verifies C.paradoxa2762 and Glaucocystophyceae38254 including Glaucophyta
    synonym. COMMON is qualitative defining anatomy, not numerical sampled prevalence.
    Giddings observations are specifically C.paradoxa UTEX LB555 under stated conditions;
    no strain interchange or universal composition is inferred.
  target_ids:
  - GO:0009843
  evidence_ids:
  - plaque-current-0
  - plaque-cached-tax2762
  - plaque-cached-tax38254
  - plaque-cached-giddings1983-page409
- assessment_id: plaque-t0-primary-scope
  area: evidence
  topic: Primary ultrastructure and photosynthetic context
  outcome: supported
  summary: Independently viewed Giddings pages409–413 and416–418, including text,
    plots, gels, microscopy and the explicitly tentative Fig19 model. These support
    cyanelle thylakoid architecture in C.paradoxa. Precise PSI localization is expressly
    unresolved in the paper and is not asserted by this target. No complete-paper,
    raw-data or necessity reanalysis claimed.
  target_ids:
  - GO:0009843
  evidence_ids:
  - plaque-current-0
  - plaque-cached-giddings1983-meta
  - plaque-cached-giddings1983-page409
  - plaque-cached-giddings1983-page410
  - plaque-thylakoid-agent-giddings1983-page411
  - plaque-cached-giddings1983-page412
  - plaque-thylakoid-agent-giddings1983-page413
  - plaque-cached-giddings1983-page416
  - plaque-cached-giddings1983-page417
  - plaque-thylakoid-agent-giddings1983-page418
- assessment_id: plaque-t1-native
  area: schema
  topic: Native protein and graph inventories
  outcome: supported
  summary: Both commands pass empty represented protein inventories and zero GENE_OR_PROTEIN
    nodes. Mechanical checks do not certify primary-source biology or establish a
    complete proteome.
  target_ids:
  - GO:0033114
  evidence_ids:
  - plaque-current-1
  - plaque-native-cyanelle_thylakoid_lumen-verify
  - plaque-native-cyanelle_thylakoid_lumen-causal
- assessment_id: plaque-t1-provenance
  area: provenance
  topic: Original lineage and unchanged frozen record
  outcome: supported
  summary: Original validates/renders exactly and all12 historical input hashes match.
    Current target unchanged; no stale input needs refresh. Original findings/actions
    empty. Historical record issues are context only, not reclosed or recertified.
  target_ids:
  - GO:0033114
  evidence_ids:
  - plaque-current-1
  - plaque-original-1
  - plaque-original-checks
- assessment_id: plaque-t1-coverage
  area: completeness
  topic: Entire maintained record and bounded science
  outcome: supported
  summary: All maintained fields, histories, discussions and graph edges read. No
    target images, snippets, quantitative properties or named protein examples are
    represented. No optional molecular inventory is fabricated. No scientific curation
    defect established at declared evidence tiers.
  target_ids:
  - GO:0033114
  evidence_ids:
  - plaque-current-1
  - plaque-policy
  - plaque-rubric
- assessment_id: plaque-t1-taxonomy
  area: scope
  topic: Exact organism/class and qualitative occurrence
  outcome: supported
  summary: ENA verifies C.paradoxa2762 and Glaucocystophyceae38254 including Glaucophyta
    synonym. COMMON is qualitative defining anatomy, not numerical sampled prevalence.
    Giddings observations are specifically C.paradoxa UTEX LB555 under stated conditions;
    no strain interchange or universal composition is inferred.
  target_ids:
  - GO:0033114
  evidence_ids:
  - plaque-current-1
  - plaque-cached-tax2762
  - plaque-cached-tax38254
  - plaque-cached-giddings1983-page409
- assessment_id: plaque-t1-primary-scope
  area: evidence
  topic: Primary ultrastructure and photosynthetic context
  outcome: supported
  summary: Independently viewed Giddings pages409–413 and416–418, including text,
    plots, gels, microscopy and the explicitly tentative Fig19 model. These support
    cyanelle thylakoid architecture in C.paradoxa. Precise PSI localization is expressly
    unresolved in the paper and is not asserted by this target. No complete-paper,
    raw-data or necessity reanalysis claimed.
  target_ids:
  - GO:0033114
  evidence_ids:
  - plaque-current-1
  - plaque-cached-giddings1983-meta
  - plaque-cached-giddings1983-page409
  - plaque-cached-giddings1983-page410
  - plaque-thylakoid-agent-giddings1983-page411
  - plaque-cached-giddings1983-page412
  - plaque-thylakoid-agent-giddings1983-page413
  - plaque-cached-giddings1983-page416
  - plaque-cached-giddings1983-page417
  - plaque-thylakoid-agent-giddings1983-page418
- assessment_id: plaque-t2-native
  area: schema
  topic: Native protein and graph inventories
  outcome: supported
  summary: Both commands pass empty represented protein inventories and zero GENE_OR_PROTEIN
    nodes. Mechanical checks do not certify primary-source biology or establish a
    complete proteome.
  target_ids:
  - GO:0033115
  evidence_ids:
  - plaque-current-2
  - plaque-native-cyanelle_thylakoid_membrane-verify
  - plaque-native-cyanelle_thylakoid_membrane-causal
- assessment_id: plaque-t2-provenance
  area: provenance
  topic: Original lineage and unchanged frozen record
  outcome: supported
  summary: Original validates/renders exactly and all12 historical input hashes match.
    Current target unchanged; no stale input needs refresh. Original findings/actions
    empty. Historical record issues are context only, not reclosed or recertified.
  target_ids:
  - GO:0033115
  evidence_ids:
  - plaque-current-2
  - plaque-original-2
  - plaque-original-checks
- assessment_id: plaque-t2-coverage
  area: completeness
  topic: Entire maintained record and bounded science
  outcome: supported
  summary: All maintained fields, histories, discussions and graph edges read. No
    target images, snippets, quantitative properties or named protein examples are
    represented. No optional molecular inventory is fabricated. No scientific curation
    defect established at declared evidence tiers.
  target_ids:
  - GO:0033115
  evidence_ids:
  - plaque-current-2
  - plaque-policy
  - plaque-rubric
- assessment_id: plaque-t2-taxonomy
  area: scope
  topic: Exact organism/class and qualitative occurrence
  outcome: supported
  summary: ENA verifies C.paradoxa2762 and Glaucocystophyceae38254 including Glaucophyta
    synonym. COMMON is qualitative defining anatomy, not numerical sampled prevalence.
    Giddings observations are specifically C.paradoxa UTEX LB555 under stated conditions;
    no strain interchange or universal composition is inferred.
  target_ids:
  - GO:0033115
  evidence_ids:
  - plaque-current-2
  - plaque-cached-tax2762
  - plaque-cached-tax38254
  - plaque-cached-giddings1983-page409
- assessment_id: plaque-t2-primary-scope
  area: evidence
  topic: Primary ultrastructure and photosynthetic context
  outcome: supported
  summary: Independently viewed Giddings pages409–413 and416–418, including text,
    plots, gels, microscopy and the explicitly tentative Fig19 model. These support
    cyanelle thylakoid architecture in C.paradoxa. Precise PSI localization is expressly
    unresolved in the paper and is not asserted by this target. No complete-paper,
    raw-data or necessity reanalysis claimed.
  target_ids:
  - GO:0033115
  evidence_ids:
  - plaque-current-2
  - plaque-cached-giddings1983-meta
  - plaque-cached-giddings1983-page409
  - plaque-cached-giddings1983-page410
  - plaque-thylakoid-agent-giddings1983-page411
  - plaque-cached-giddings1983-page412
  - plaque-thylakoid-agent-giddings1983-page413
  - plaque-cached-giddings1983-page416
  - plaque-cached-giddings1983-page417
  - plaque-thylakoid-agent-giddings1983-page418
- assessment_id: plaque-t0-identity
  area: identity
  topic: Exact identity, parentage and compartment boundaries
  outcome: supported
  summary: ExactGO0009843/SL0277 represent the whole internal thylakoid unit, containing
    membrane and lumen and part of cyanelle. Plastid-thylakoid and broader-thylakoid
    parentage are valid. Local coarse physical kind deliberately covers whole thylakoids;
    no GO is_a organelle assertion is added.
  target_ids:
  - GO:0009843
  evidence_ids:
  - plaque-current-0
  - plaque-thylakoid-agent-go
  - plaque-thylakoid-agent-SL-0277
  - plaque-schema-policy
- assessment_id: plaque-t1-identity
  area: identity
  topic: Exact identity, parentage and compartment boundaries
  outcome: supported
  summary: ExactGO0033114/SL0084 represent the lumenal volume, part of whole cyanelle
    thylakoid and is_a plastid thylakoid lumen. It is not the bounding bilayer, whole
    thylakoid or a molecular cargo inventory.
  target_ids:
  - GO:0033114
  evidence_ids:
  - plaque-current-1
  - plaque-thylakoid-agent-go
  - plaque-thylakoid-agent-SL-0084
  - plaque-schema-policy
- assessment_id: plaque-t2-identity
  area: identity
  topic: Exact identity, parentage and compartment boundaries
  outcome: supported
  summary: ExactGO0033115/SL0085 represent the lipid bilayer surrounding lumen. Plastid
    thylakoid membrane0055035 and broader0042651 parent classes are valid. It is part
    of whole thylakoid, distinct from cyanelle envelope membrane.
  target_ids:
  - GO:0033115
  evidence_ids:
  - plaque-current-2
  - plaque-thylakoid-agent-go
  - plaque-thylakoid-agent-SL-0085
  - plaque-schema-policy
- assessment_id: plaque-t0-composition
  area: grounding
  topic: Constituent membrane material
  outcome: supported
  summary: The membrane constituent is correctly grounded toGO0033115 as the identified
    structural membrane, with LIPID material type. UNKNOWN formation essentiality
    avoids assigning measured assembly necessity. No individual lipid/protein identity
    is guessed.
  target_ids:
  - GO:0009843
  evidence_ids:
  - plaque-current-0
  - plaque-thylakoid-agent-go
  - plaque-thylakoid-agent-SL-0085
  - plaque-rubric
- assessment_id: plaque-t1-composition
  area: grounding
  topic: Intentional lack of lumen constituents
  outcome: not_applicable
  summary: The record intentionally withholds lumen-localized proteins and proton
    transport pending source-specific evidence. An empty component inventory is not
    a defect in the bounded region record. A membrane boundary is not relabeled as
    soluble lumen cargo.
  target_ids:
  - GO:0033114
  evidence_ids:
  - plaque-current-1
  - plaque-thylakoid-agent-go
  - plaque-thylakoid-agent-SL-0084
  - plaque-rubric
- assessment_id: plaque-t2-composition
  area: grounding
  topic: Collective lipid bilayer and constitutional necessity
  outcome: supported
  summary: Collective lipid bilayer is defining material, not a particular chemical
    species. ESSENTIAL is constitutional material necessity, not evidence that one
    lipid/protein is required to form the compartment. REVIEWED_LABEL_ONLY and existing
    material-grounding TODO correctly withhold an invented accession.
  target_ids:
  - GO:0033115
  evidence_ids:
  - plaque-current-2
  - plaque-thylakoid-agent-go
  - plaque-thylakoid-agent-SL-0085
  - plaque-rubric
- assessment_id: plaque-t0-graph
  area: graph
  topic: Complete descriptive topology/function graph
  outcome: supported
  summary: Three NONMECHANISTIC edges describe membrane bounding lumen, membrane support
    of light reactions and membrane parthood in whole thylakoid. Typed GO/SL topology
    and inspected primary architecture support them without molecular assembly claims.
  target_ids:
  - GO:0009843
  evidence_ids:
  - plaque-current-0
  - plaque-thylakoid-agent-go
  - plaque-thylakoid-agent-SL-0277
  - plaque-thylakoid-agent-SL-0084
  - plaque-thylakoid-agent-SL-0085
  - plaque-graph-policy
  - plaque-cached-giddings1983-page417
- assessment_id: plaque-t1-graph
  area: graph
  topic: Complete descriptive topology/function graph
  outcome: supported
  summary: Two NONMECHANISTIC edges describe lumen parthood in whole thylakoid and
    enclosing membrane. They assert geometry, not proton transport, cargo processing
    or complete photosynthetic mechanism.
  target_ids:
  - GO:0033114
  evidence_ids:
  - plaque-current-1
  - plaque-thylakoid-agent-go
  - plaque-thylakoid-agent-SL-0277
  - plaque-thylakoid-agent-SL-0084
  - plaque-thylakoid-agent-SL-0085
  - plaque-graph-policy
  - plaque-cached-giddings1983-page417
- assessment_id: plaque-t2-graph
  area: graph
  topic: Complete descriptive topology/function graph
  outcome: supported
  summary: Two NONMECHANISTIC edges describe bounding lumen and providing the membrane
    site for light reactions. They do not assert precise PSI distribution, measured
    electron flow, protein assembly or loss-of-function necessity.
  target_ids:
  - GO:0033115
  evidence_ids:
  - plaque-current-2
  - plaque-thylakoid-agent-go
  - plaque-thylakoid-agent-SL-0277
  - plaque-thylakoid-agent-SL-0084
  - plaque-thylakoid-agent-SL-0085
  - plaque-graph-policy
  - plaque-cached-giddings1983-page417
- assessment_id: plaque-t0-function
  area: evidence
  topic: Photosynthetic light-reaction site
  outcome: supported
  summary: GO0009843/SL0277 explicitly support photosynthetic cyanelle thylakoids,
    and Giddings pigment/ultrastructure experiments corroborate this in C.paradoxa.
    The function is bounded to the membrane site of light reactions, not a complete
    protein inventory or a claim that the old paper resolves precise PSI placement.
  target_ids:
  - GO:0009843
  evidence_ids:
  - plaque-current-0
  - plaque-thylakoid-agent-go
  - plaque-thylakoid-agent-SL-0277
  - plaque-cached-giddings1983-page409
  - plaque-thylakoid-agent-giddings1983-page411
  - plaque-cached-giddings1983-page412
  - plaque-cached-giddings1983-page417
- assessment_id: plaque-t0-adapter
  area: scope
  topic: Pathway-triggered structured-source applicability
  outcome: supported
  summary: The current target explicitly asserts photosynthetic light-reaction functionGO0019684
    and a membrane-supports-light-reactions graph edge, so the original no-gene/regulator/stress/transcriptomic
    rationale overlooks a real pathway trigger. Actual current catalogue inspection
    finds no Cyanophora/glaucophyte host. No matched downstream gene/module query
    applies, no cyanobacterial dataset is substituted, and noncoverage does not imply
    biological absence. Source-scoped primary/authority fallback completes the current
    assessment; historical runner remains unavailable at its actual earlier time.
  target_ids:
  - GO:0009843
  evidence_ids:
  - plaque-current-0
  - plaque-original-0
  - plaque-policy
  - plaque-catalogue
  - plaque-historical-runner
  - plaque-thylakoid-agent-SL-0277
  - plaque-cached-giddings1983-page409
- assessment_id: plaque-t2-function
  area: evidence
  topic: Photosynthetic light-reaction site
  outcome: supported
  summary: GO0009843/SL0277 explicitly support photosynthetic cyanelle thylakoids,
    and Giddings pigment/ultrastructure experiments corroborate this in C.paradoxa.
    The function is bounded to the membrane site of light reactions, not a complete
    protein inventory or a claim that the old paper resolves precise PSI placement.
  target_ids:
  - GO:0033115
  evidence_ids:
  - plaque-current-2
  - plaque-thylakoid-agent-go
  - plaque-thylakoid-agent-SL-0277
  - plaque-cached-giddings1983-page409
  - plaque-thylakoid-agent-giddings1983-page411
  - plaque-cached-giddings1983-page412
  - plaque-cached-giddings1983-page417
- assessment_id: plaque-t2-adapter
  area: scope
  topic: Pathway-triggered structured-source applicability
  outcome: supported
  summary: The current target explicitly asserts photosynthetic light-reaction functionGO0019684
    and a membrane-supports-light-reactions graph edge, so the original no-gene/regulator/stress/transcriptomic
    rationale overlooks a real pathway trigger. Actual current catalogue inspection
    finds no Cyanophora/glaucophyte host. No matched downstream gene/module query
    applies, no cyanobacterial dataset is substituted, and noncoverage does not imply
    biological absence. Source-scoped primary/authority fallback completes the current
    assessment; historical runner remains unavailable at its actual earlier time.
  target_ids:
  - GO:0033115
  evidence_ids:
  - plaque-current-2
  - plaque-original-2
  - plaque-policy
  - plaque-catalogue
  - plaque-historical-runner
  - plaque-thylakoid-agent-SL-0277
  - plaque-cached-giddings1983-page409
- assessment_id: plaque-t1-adapter
  area: scope
  topic: Genuine topology-only applicability exclusion
  outcome: not_applicable
  summary: Complete record is geometry and qualitative occurrence only. It explicitly
    withholds lumen proteins and proton transport, and does not assert a named molecular
    actor, regulator, pathway, stress response, trait or expression/module inference.
    The old N/A wording does not create a defect absent a positive trigger. Catalogue
    has no glaucophyte host but that is contextual, not the sole reason for genuine
    exclusion.
  target_ids:
  - GO:0033114
  evidence_ids:
  - plaque-current-1
  - plaque-original-1
  - plaque-policy
  - plaque-catalogue
  - plaque-historical-runner
- assessment_id: micro-diazoplast-provenance
  area: provenance
  topic: Frozen original and current inputs; immutable pair
  outcome: supported
  summary: 'Diazoplast original input7aabee1c3f14420665958c955451705d3c7ea115003ffd94060a2f1afd40d41f
    changed tofd3948e827eb4a9870bc4eccb09689dd5c82f5caef443f1e319daabbf21bb038: new
    history and complex-node retyping substantively assessed; original F1 persists.
    Original native validation/render passed; no artifact, record, status or historical
    finding rewritten.'
  target_ids:
  - cellstructuremech:diazoplast
  evidence_ids:
  - micro-record-diazoplast
  - micro-prior-diazoplast
  - micro-original-validation-inputs
- assessment_id: micro-diazoplast-native
  area: schema
  topic: Actual current native verifier coverage
  outcome: supported
  summary: Verify checks three declared Azotobacter accession examples and any xrefs;
    identity pass does not establish role in a diazoplast. Causal command counts zero
    GENE_OR_PROTEIN nodes; this is not validation of all graph biology, narrative
    proteins, membership or necessity.
  target_ids:
  - cellstructuremech:diazoplast
  evidence_ids:
  - micro-record-diazoplast
  - micro-native-diazoplast-verify
  - micro-native-diazoplast-causal
- assessment_id: micro-diazoplast-adapter
  area: evidence
  topic: Actual pathway-triggered structured-source applicability
  outcome: concern
  summary: Named nifH/nifD/nifK/hupL, nitrogen fixation, photosynthesis and physiological
    perturbation trigger applicability. Original expression-only N/A rationale is
    insufficient. Current bounded catalogue contains no matching organism/dataset,
    so no downstream module query applies. Historical runner unavailability is separately
    dated; absence is not biological evidence.
  target_ids:
  - cellstructuremech:diazoplast
  evidence_ids:
  - micro-record-diazoplast
  - micro-prior-diazoplast
  - micro-policy
  - micro-catalogue
  - micro-historical-adapter-runner
- assessment_id: micro-diazoplast-status
  area: provenance
  topic: PROPOSED status and bounded curation ownership
  outcome: supported
  summary: Review preserves PROPOSED and append-only history. Source receipts describe
    inspected scopes; old reviewer access, prior issue/group/category dispositions
    and neighbor correctness are not recertified. Any scientific edit belongs to separately
    authorized guarded-writer curation; no record edited here.
  target_ids:
  - cellstructuremech:diazoplast
  evidence_ids:
  - micro-record-diazoplast
  - micro-prior-diazoplast
  - micro-policy
- assessment_id: micro-early_endosome-provenance
  area: provenance
  topic: Frozen original and current inputs; immutable pair
  outcome: supported
  summary: Current target bytes match the original input; original qualified pass
    had no findings/actions. Original native validation/render passed; no artifact,
    record, status or historical finding rewritten.
  target_ids:
  - GO:0005769
  evidence_ids:
  - micro-record-early_endosome
  - micro-prior-early_endosome
  - micro-original-validation-inputs
- assessment_id: micro-early_endosome-native
  area: schema
  topic: Actual current native verifier coverage
  outcome: supported
  summary: Verify has an empty declared protein-example/xref inventory. Causal command
    counts zero GENE_OR_PROTEIN nodes; this is not validation of all graph biology,
    narrative proteins, membership or necessity.
  target_ids:
  - GO:0005769
  evidence_ids:
  - micro-record-early_endosome
  - micro-native-early_endosome-verify
  - micro-native-early_endosome-causal
- assessment_id: micro-early_endosome-adapter
  area: evidence
  topic: Actual pathway-triggered structured-source applicability
  outcome: concern
  summary: Definition and function name clathrin-dependent/independent endocytosis
    and recycling/degradation cargo-sorting pathways. Original expression-only N/A
    rationale is insufficient. Current bounded catalogue contains no matching organism/dataset,
    so no downstream module query applies. Historical runner unavailability is separately
    dated; absence is not biological evidence.
  target_ids:
  - GO:0005769
  evidence_ids:
  - micro-record-early_endosome
  - micro-prior-early_endosome
  - micro-policy
  - micro-catalogue
  - micro-historical-adapter-runner
- assessment_id: micro-early_endosome-status
  area: provenance
  topic: PROPOSED status and bounded curation ownership
  outcome: supported
  summary: Review preserves PROPOSED and append-only history. Source receipts describe
    inspected scopes; old reviewer access, prior issue/group/category dispositions
    and neighbor correctness are not recertified. Any scientific edit belongs to separately
    authorized guarded-writer curation; no record edited here.
  target_ids:
  - GO:0005769
  evidence_ids:
  - micro-record-early_endosome
  - micro-prior-early_endosome
  - micro-policy
- assessment_id: micro-early_endosome_lumen-provenance
  area: provenance
  topic: Frozen original and current inputs; immutable pair
  outcome: supported
  summary: Current target bytes match the original input; original qualified pass
    had no findings/actions. Original native validation/render passed; no artifact,
    record, status or historical finding rewritten.
  target_ids:
  - GO:0031905
  evidence_ids:
  - micro-record-early_endosome_lumen
  - micro-prior-early_endosome_lumen
  - micro-original-validation-inputs
- assessment_id: micro-early_endosome_lumen-native
  area: schema
  topic: Actual current native verifier coverage
  outcome: supported
  summary: Verify has an empty declared protein-example/xref inventory. Causal command
    counts zero GENE_OR_PROTEIN nodes; this is not validation of all graph biology,
    narrative proteins, membership or necessity.
  target_ids:
  - GO:0031905
  evidence_ids:
  - micro-record-early_endosome_lumen
  - micro-native-early_endosome_lumen-verify
  - micro-native-early_endosome_lumen-causal
- assessment_id: micro-early_endosome_lumen-adapter
  area: evidence
  topic: Actual pathway-triggered structured-source applicability
  outcome: concern
  summary: Function/evidence and canonical example explicitly assert cargo routing
    through the early-endocytic pathway; topology-only graph does not erase this trigger.
    Original expression-only N/A rationale is insufficient. Current bounded catalogue
    contains no matching organism/dataset, so no downstream module query applies.
    Historical runner unavailability is separately dated; absence is not biological
    evidence.
  target_ids:
  - GO:0031905
  evidence_ids:
  - micro-record-early_endosome_lumen
  - micro-prior-early_endosome_lumen
  - micro-policy
  - micro-catalogue
  - micro-historical-adapter-runner
- assessment_id: micro-early_endosome_lumen-status
  area: provenance
  topic: PROPOSED status and bounded curation ownership
  outcome: supported
  summary: Review preserves PROPOSED and append-only history. Source receipts describe
    inspected scopes; old reviewer access, prior issue/group/category dispositions
    and neighbor correctness are not recertified. Any scientific edit belongs to separately
    authorized guarded-writer curation; no record edited here.
  target_ids:
  - GO:0031905
  evidence_ids:
  - micro-record-early_endosome_lumen
  - micro-prior-early_endosome_lumen
  - micro-policy
- assessment_id: micro-early_endosome_membrane-provenance
  area: provenance
  topic: Frozen original and current inputs; immutable pair
  outcome: supported
  summary: Current target bytes match the original input; original qualified pass
    had no findings/actions. Original native validation/render passed; no artifact,
    record, status or historical finding rewritten.
  target_ids:
  - GO:0031901
  evidence_ids:
  - micro-record-early_endosome_membrane
  - micro-prior-early_endosome_membrane
  - micro-original-validation-inputs
- assessment_id: micro-early_endosome_membrane-native
  area: schema
  topic: Actual current native verifier coverage
  outcome: supported
  summary: Verify has an empty declared protein-example/xref inventory. Causal command
    counts zero GENE_OR_PROTEIN nodes; this is not validation of all graph biology,
    narrative proteins, membership or necessity.
  target_ids:
  - GO:0031901
  evidence_ids:
  - micro-record-early_endosome_membrane
  - micro-native-early_endosome_membrane-verify
  - micro-native-early_endosome_membrane-causal
- assessment_id: micro-early_endosome_membrane-adapter
  area: evidence
  topic: Actual pathway-triggered structured-source applicability
  outcome: concern
  summary: Occurrence/canonical example and evidence explicitly place the membrane-bounded
    network in the T.cruzi endocytic pathway; a compartmentalization-only graph does
    not remove that asserted pathway context. Original expression-only N/A rationale
    is insufficient. Current bounded catalogue contains no matching organism/dataset,
    so no downstream module query applies. Historical runner unavailability is separately
    dated; absence is not biological evidence.
  target_ids:
  - GO:0031901
  evidence_ids:
  - micro-record-early_endosome_membrane
  - micro-prior-early_endosome_membrane
  - micro-policy
  - micro-catalogue
  - micro-historical-adapter-runner
- assessment_id: micro-early_endosome_membrane-status
  area: provenance
  topic: PROPOSED status and bounded curation ownership
  outcome: supported
  summary: Review preserves PROPOSED and append-only history. Source receipts describe
    inspected scopes; old reviewer access, prior issue/group/category dispositions
    and neighbor correctness are not recertified. Any scientific edit belongs to separately
    authorized guarded-writer curation; no record edited here.
  target_ids:
  - GO:0031901
  evidence_ids:
  - micro-record-early_endosome_membrane
  - micro-prior-early_endosome_membrane
  - micro-policy
- assessment_id: micro-diazoplast-identity
  area: identity
  topic: Structural proto-organelle boundary
  outcome: supported
  summary: Minted compartment identity and intracellular-organelle parent are compatible
    with permanent Epithemia diazoplasts while genetic integration remains unresolved.
    Related spheroid-body synonym is source usage; diazoplast is not the UCYN-A/Braarudosphaera
    nitroplast. No exact match in the bounded current GO query is not universal absence.
  target_ids:
  - cellstructuremech:diazoplast
  evidence_ids:
  - micro-record-diazoplast
  - micro-go
  - micro-diazoplast-go-search
  - micro-context-nitroplast
  - micro-moulin2024-jats
  - micro-moulin2024-supp
  - micro-frail2025-jats
  - micro-frail2025-supp
- assessment_id: micro-diazoplast-taxa
  area: scope
  topic: Genus occurrence and measured isolate
  outcome: supported
  summary: Frail Introduction explicitly says all described Epithemia species; COMMON
    is qualitative, not a measured universal physiological pattern. Moulin/Gazos Creek
    Butano-area E.clementina strain and nonaxenic culture context are verified; ENA
    retains nom.ined. label. Frail later axenic cultures do not change the earlier
    experimental conditions.
  target_ids:
  - cellstructuremech:diazoplast
  evidence_ids:
  - micro-record-diazoplast
  - micro-tax420972
  - micro-tax3042617
  - micro-moulin2024-jats
  - micro-moulin2024-supp
  - micro-frail2025-jats
  - micro-frail2025-supp
- assessment_id: micro-diazoplast-composition
  area: grounding
  topic: Nitrogenase, retained membranes and bounded HupL role
  outcome: supported
  summary: Moulin intact nif cluster, NifDK detection and nitrogenase activity support
    nitrogenase membership; retained internal thylakoids and boundary membranes do
    not imply photosynthesis. HupL detection supports the annotated recycling subunit
    at immunoblot/functional-assignment tier, not in-situ localization or measured
    H2 flux. Broad InterPro families and symbol-synonym collisions do not supply an
    exact uptake-specific equivalog; open grounding discussion remains appropriate.
  target_ids:
  - cellstructuremech:diazoplast
  evidence_ids:
  - micro-record-diazoplast
  - micro-go
  - micro-moulin2024-jats
  - micro-moulin2024-supp
  - micro-IPR001501
  - micro-IPR050867
  - micro-query-hupL
- assessment_id: micro-diazoplast-identities
  area: grounding
  topic: Accession identity, status and bounded query uniqueness
  outcome: supported
  summary: C1DK95 is unreviewed Azotobacter DJ with primary anfH and nifH synonym;
    reviewed P07328/P07329 map nifD/nifK and taxon354. Exact reviewed organism queries
    each return the stated single entry. These identities do not establish Epithemia
    membership, a native mixed-accession assembly or one protein as the whole complex.
  target_ids:
  - cellstructuremech:diazoplast
  evidence_ids:
  - micro-record-diazoplast
  - micro-tax354
  - micro-tax322710
  - micro-protein-C1DK95
  - micro-protein-P07328
  - micro-protein-P07329
  - micro-query-nifD
  - micro-query-nifK
- assessment_id: micro-diazoplast-placement
  area: grounding
  topic: Identity-only examples versus structure-role field contract
  outcome: concern
  summary: Three examples explicitly disclaim structure membership, while ProteinExample
    requires the role in the structure to have been established for the named organism.
    The experiments concern Epithemia and the references are Azotobacter identities.
    Original minor F1 remains confirmed with exact lineage; accessions and nitrogenase
    component itself remain valid.
  target_ids:
  - cellstructuremech:diazoplast
  evidence_ids:
  - micro-record-diazoplast
  - micro-prior-diazoplast
  - micro-schema-protein-example
  - micro-protein-C1DK95
  - micro-protein-P07328
  - micro-protein-P07329
  - micro-moulin2024-jats
  - micro-moulin2024-supp
  - micro-frail2025-jats
  - micro-frail2025-supp
- assessment_id: micro-diazoplast-necessity
  area: grounding
  topic: Formation necessity distinct from activity
  outcome: unknown
  summary: All three components retain UNKNOWN. Detection, enzymatic function, material
    constitution and metabolic perturbations do not test whether the organelle forms
    without each molecule. No complete stoichiometry or exhaustive membrane inventory
    asserted.
  target_ids:
  - cellstructuremech:diazoplast
  evidence_ids:
  - micro-record-diazoplast
  - micro-go
  - micro-moulin2024-jats
  - micro-moulin2024-supp
  - micro-frail2025-jats
  - micro-frail2025-supp
- assessment_id: micro-diazoplast-stale-node
  area: graph
  topic: Substantive refresh of complex-node retyping
  outcome: supported
  summary: The sole scientific delta changes nitrogenase from GENE_OR_PROTEIN to STRUCTURE
    while retaining GO0016610 and nitrogenase component_ref; native GO defines a multisubunit
    complex, so the new type fits the component/graph contract. Current zero typed
    gene nodes is expected, not evidence that the original ProteinExample placement
    was fixed. The added history mentioning grouped issue2404 does not terminally
    resolve that group or its unfrozen predecessor.
  target_ids:
  - cellstructuremech:diazoplast
  evidence_ids:
  - micro-record-diazoplast
  - micro-prior-diazoplast
  - micro-go
  - micro-schema-protein-example
  - micro-native-diazoplast-causal
- assessment_id: micro-diazoplast-functions
  area: evidence
  topic: Isotope exchange and physiological coupling
  outcome: supported
  summary: Moulin isotope data and culture ARA support compartment fixation, host
    nitrogen supply, photosynthetic carbon production and carbon transfer; transferred
    chemical species and transporters remain unidentified. NanoSIMS wash/dehydration
    effects preclude simple timing inference; IRMS distinguishes daytime host fixation.
    Nitrogen transfer not inferred from mere sequence annotation.
  target_ids:
  - cellstructuremech:diazoplast
  evidence_ids:
  - micro-record-diazoplast
  - micro-go
  - micro-moulin2024-jats
  - micro-moulin2024-supp
  - micro-moulin2024-f2
- assessment_id: micro-diazoplast-graph
  area: graph
  topic: All seven process-level mechanistic edges
  outcome: supported
  summary: 'The seven edges retain nitrogenase catalysis, compartment fixation, nitrogen
    supply, host carbon production/transfer, photosynthetic support and partial inhibition.
    MECHANISTIC is defensible at the explicitly restricted E.clementina process/perturbation
    level: Results~60% reduction overrides stronger abstract abolition wording. No
    causal transporter identity, specific metabolite, respiration protection or division/import
    machinery asserted.'
  target_ids:
  - cellstructuremech:diazoplast
  evidence_ids:
  - micro-record-diazoplast
  - micro-go
  - micro-moulin2024-jats
  - micro-moulin2024-supp
  - micro-moulin2024-f2
- assessment_id: micro-diazoplast-import-limits
  area: evidence
  topic: Candidate proteins and hypotheses remain unresolved
  outcome: supported
  summary: Frail s5–7 and Discussion distinguish six enriched candidates from validated
    localization, undetected TusA from import evidence, and unsupported PFK import.
    Genetic-integration and host fission/confinement proposals remain hypotheses.
    Moulin species comparison and glycogen/respiration limitations prevent genus-wide
    physiology or universal glycogen absence.
  target_ids:
  - cellstructuremech:diazoplast
  evidence_ids:
  - micro-record-diazoplast
  - micro-moulin2024-jats
  - micro-moulin2024-supp
  - micro-frail2025-jats
  - micro-frail2025-supp
- assessment_id: micro-diazoplast-image
  area: evidence
  topic: Figure2 pixels, native bytes, licence and taxon
  outcome: supported
  summary: Whole frozen A–C figure visually inspected; it matches native version1
    asset SHA256 and MD5/size listing. Native caption supports12h/24h isotope panels,
    diazoplast arrows and quantified host/diazoplast regions. JATS author list and
    CC BY4.0 match record attribution; this is Moulin2024, not Frail2025 with a different
    licence. No quantitative reanalysis.
  target_ids:
  - cellstructuremech:diazoplast
  evidence_ids:
  - micro-record-diazoplast
  - micro-image-local
  - micro-moulin2024-f2
  - micro-moulin2024-package
  - micro-moulin2024-jats
  - micro-moulin2024-meta
  - micro-tax3042617
- assessment_id: micro-early_endosome-identity
  area: identity
  topic: Whole organelle, lumen and boundary remain distinct
  outcome: supported
  summary: 'Exact GO/UniProt identity and mappings match: whole organelle is an endosome;
    surrounding membrane and lumen are parts. Reservosome neighbor supplies identity
    context only as a separate downstream storage organelle.'
  target_ids:
  - GO:0005769
  evidence_ids:
  - micro-record-early_endosome
  - micro-SL-0094
  - micro-go
  - micro-porto2000-meta
  - micro-tax5693
  - micro-context-reservosome
- assessment_id: micro-early_endosome-taxa
  area: scope
  topic: Epimastigote occurrence and source identification tier
  outcome: supported
  summary: Exact taxon5693 is T.cruzi. Porto complete primary abstract supports protein-gold
    cargo moving from principal cytostome/cytopharynx entry to interconnected vesicles/tubules
    and reservosomes. Authors propose early-endosome identity from pH and kinetics;
    no molecular marker or species-wide life-stage equivalence is invented. VARIABLE
    is qualitative; membrane/lumen existence follows the described bounded network
    plus exact authorities.
  target_ids:
  - GO:0005769
  evidence_ids:
  - micro-record-early_endosome
  - micro-SL-0094
  - micro-go
  - micro-porto2000-meta
  - micro-tax5693
  - micro-context-reservosome
- assessment_id: micro-early_endosome-composition
  area: grounding
  topic: Constitution versus optional molecular inventories
  outcome: supported
  summary: Complete lipid bilayer constituting the membrane is supported; ESSENTIAL
    is collective constitution, not an experimentally demonstrated requirement for
    a particular lipid species. No full protein census or chemical stoichiometry claimed.
  target_ids:
  - GO:0005769
  evidence_ids:
  - micro-record-early_endosome
  - micro-policy
  - micro-go
  - micro-SL-0094
- assessment_id: micro-early_endosome-necessity
  area: grounding
  topic: Individual lipid requirements
  outcome: unknown
  summary: The constitutional bilayer ESSENTIAL row does not identify necessity of
    particular molecular species, substitutes or concentrations. Those assembly requirements
    remain untested and should not be inferred from defining topology.
  target_ids:
  - GO:0005769
  evidence_ids:
  - micro-record-early_endosome
  - micro-go
- assessment_id: micro-early_endosome-function
  area: evidence
  topic: Generic function separated from organism-specific route
  outcome: supported
  summary: Generic incoming-vesicle sorting toward recycling/degradation follows GO/SL.
    Porto supplies only the stated T.cruzi protein-cargo route, not proof of every
    generic sorting branch or a full Rab/coat/tether mechanism.
  target_ids:
  - GO:0005769
  evidence_ids:
  - micro-record-early_endosome
  - micro-SL-0094
  - micro-go
  - micro-porto2000-meta
  - micro-tax5693
  - micro-context-reservosome
- assessment_id: micro-early_endosome-graph
  area: graph
  topic: All NONMECHANISTIC edges scoped
  outcome: supported
  summary: Four classification/parthood/enclosure edges follow native authorities.
    Three cargo-route edges remain T.cruzi-epimastigote-specific and nonexclusive;
    abstract supports protein transit. The lipid-specific extension of final edge
    remains separately unknown.
  target_ids:
  - GO:0005769
  evidence_ids:
  - micro-record-early_endosome
  - micro-SL-0094
  - micro-go
  - micro-porto2000-meta
  - micro-tax5693
  - micro-context-reservosome
- assessment_id: micro-early_endosome-coverage
  area: completeness
  topic: Entire record; source tier and omitted optional data
  outcome: supported
  summary: Entire target read. No image, measured physical property, verbatim snippet
    or protein example is asserted. Porto source identity and abstract are current
    verified, while publisher403 and public API metadata stub leave body/methods/strain/figure
    pixels unverified. Neighbor records do not replace primary evidence. Unknown optional
    inventories are not invented findings.
  target_ids:
  - GO:0005769
  evidence_ids:
  - micro-record-early_endosome
  - micro-SL-0094
  - micro-porto2000-meta
  - micro-porto2000-publisher
  - micro-porto2000-api
  - micro-context-reservosome
- assessment_id: micro-early_endosome_lumen-identity
  area: identity
  topic: Whole organelle, lumen and boundary remain distinct
  outcome: supported
  summary: 'Exact GO/UniProt identity and mappings match: lumen is an endosome-lumen
    specialization inside the early endosome, bounded by its membrane. Reservosome
    neighbor supplies identity context only as a separate downstream storage organelle.'
  target_ids:
  - GO:0031905
  evidence_ids:
  - micro-record-early_endosome_lumen
  - micro-SL-0337
  - micro-go
  - micro-porto2000-meta
  - micro-tax5693
  - micro-context-reservosome
- assessment_id: micro-early_endosome_lumen-taxa
  area: scope
  topic: Epimastigote occurrence and source identification tier
  outcome: supported
  summary: Exact taxon5693 is T.cruzi. Porto complete primary abstract supports protein-gold
    cargo moving from principal cytostome/cytopharynx entry to interconnected vesicles/tubules
    and reservosomes. Authors propose early-endosome identity from pH and kinetics;
    no molecular marker or species-wide life-stage equivalence is invented. VARIABLE
    is qualitative; membrane/lumen existence follows the described bounded network
    plus exact authorities.
  target_ids:
  - GO:0031905
  evidence_ids:
  - micro-record-early_endosome_lumen
  - micro-SL-0337
  - micro-go
  - micro-porto2000-meta
  - micro-tax5693
  - micro-context-reservosome
- assessment_id: micro-early_endosome_lumen-composition
  area: grounding
  topic: Constitution versus optional molecular inventories
  outcome: supported
  summary: Lumen is an enclosed region, and the membrane is its boundary, not a lumen
    component; optional cargo inventory need not be populated.
  target_ids:
  - GO:0031905
  evidence_ids:
  - micro-record-early_endosome_lumen
  - micro-policy
  - micro-go
  - micro-SL-0337
- assessment_id: micro-early_endosome_lumen-function
  area: evidence
  topic: Generic function separated from organism-specific route
  outcome: supported
  summary: The lumen is the volume through which cargo passes, supported by exact
    topology plus bounded protein-cargo uptake evidence; no lumen-localized enzyme,
    receptor or quantitative pH asserted.
  target_ids:
  - GO:0031905
  evidence_ids:
  - micro-record-early_endosome_lumen
  - micro-SL-0337
  - micro-go
  - micro-porto2000-meta
  - micro-tax5693
  - micro-context-reservosome
- assessment_id: micro-early_endosome_lumen-graph
  area: graph
  topic: All NONMECHANISTIC edges scoped
  outcome: supported
  summary: Three edges preserve lumen is-a, organelle parthood and surrounding-membrane
    boundary; no molecular transition implied.
  target_ids:
  - GO:0031905
  evidence_ids:
  - micro-record-early_endosome_lumen
  - micro-SL-0337
  - micro-go
  - micro-porto2000-meta
  - micro-tax5693
  - micro-context-reservosome
- assessment_id: micro-early_endosome_lumen-coverage
  area: completeness
  topic: Entire record; source tier and omitted optional data
  outcome: supported
  summary: Entire target read. No image, measured physical property, verbatim snippet
    or protein example is asserted. Porto source identity and abstract are current
    verified, while publisher403 and public API metadata stub leave body/methods/strain/figure
    pixels unverified. Neighbor records do not replace primary evidence. Unknown optional
    inventories are not invented findings.
  target_ids:
  - GO:0031905
  evidence_ids:
  - micro-record-early_endosome_lumen
  - micro-SL-0337
  - micro-porto2000-meta
  - micro-porto2000-publisher
  - micro-porto2000-api
  - micro-context-reservosome
- assessment_id: micro-early_endosome_membrane-identity
  area: identity
  topic: Whole organelle, lumen and boundary remain distinct
  outcome: supported
  summary: 'Exact GO/UniProt identity and mappings match: surrounding bilayer is an
    endosome-membrane specialization and a part of early endosome. Reservosome neighbor
    supplies identity context only as a separate downstream storage organelle.'
  target_ids:
  - GO:0031901
  evidence_ids:
  - micro-record-early_endosome_membrane
  - micro-SL-0093
  - micro-go
  - micro-porto2000-meta
  - micro-tax5693
  - micro-context-reservosome
- assessment_id: micro-early_endosome_membrane-taxa
  area: scope
  topic: Epimastigote occurrence and source identification tier
  outcome: supported
  summary: Exact taxon5693 is T.cruzi. Porto complete primary abstract supports protein-gold
    cargo moving from principal cytostome/cytopharynx entry to interconnected vesicles/tubules
    and reservosomes. Authors propose early-endosome identity from pH and kinetics;
    no molecular marker or species-wide life-stage equivalence is invented. VARIABLE
    is qualitative; membrane/lumen existence follows the described bounded network
    plus exact authorities.
  target_ids:
  - GO:0031901
  evidence_ids:
  - micro-record-early_endosome_membrane
  - micro-SL-0093
  - micro-go
  - micro-porto2000-meta
  - micro-tax5693
  - micro-context-reservosome
- assessment_id: micro-early_endosome_membrane-composition
  area: grounding
  topic: Constitution versus optional molecular inventories
  outcome: supported
  summary: Complete lipid bilayer constituting the membrane is supported; ESSENTIAL
    is collective constitution, not an experimentally demonstrated requirement for
    a particular lipid species. No full protein census or chemical stoichiometry claimed.
  target_ids:
  - GO:0031901
  evidence_ids:
  - micro-record-early_endosome_membrane
  - micro-policy
  - micro-go
  - micro-SL-0093
- assessment_id: micro-early_endosome_membrane-necessity
  area: grounding
  topic: Individual lipid requirements
  outcome: unknown
  summary: The constitutional bilayer ESSENTIAL row does not identify necessity of
    particular molecular species, substitutes or concentrations. Those assembly requirements
    remain untested and should not be inferred from defining topology.
  target_ids:
  - GO:0031901
  evidence_ids:
  - micro-record-early_endosome_membrane
  - micro-go
- assessment_id: micro-early_endosome_membrane-function
  area: evidence
  topic: Generic function separated from organism-specific route
  outcome: supported
  summary: Compartmentalization is a boundary function, supported by exact membrane/lumen
    definitions. It does not assign autonomous cargo sorting machinery or enzyme activity
    to lipid.
  target_ids:
  - GO:0031901
  evidence_ids:
  - micro-record-early_endosome_membrane
  - micro-SL-0093
  - micro-go
  - micro-porto2000-meta
  - micro-tax5693
  - micro-context-reservosome
- assessment_id: micro-early_endosome_membrane-graph
  area: graph
  topic: All NONMECHANISTIC edges scoped
  outcome: supported
  summary: Three edges preserve membrane is-a, organelle parthood and lumen boundary,
    without inventing a Rab/coat mechanism.
  target_ids:
  - GO:0031901
  evidence_ids:
  - micro-record-early_endosome_membrane
  - micro-SL-0093
  - micro-go
  - micro-porto2000-meta
  - micro-tax5693
  - micro-context-reservosome
- assessment_id: micro-early_endosome_membrane-coverage
  area: completeness
  topic: Entire record; source tier and omitted optional data
  outcome: supported
  summary: Entire target read. No image, measured physical property, verbatim snippet
    or protein example is asserted. Porto source identity and abstract are current
    verified, while publisher403 and public API metadata stub leave body/methods/strain/figure
    pixels unverified. Neighbor records do not replace primary evidence. Unknown optional
    inventories are not invented findings.
  target_ids:
  - GO:0031901
  evidence_ids:
  - micro-record-early_endosome_membrane
  - micro-SL-0093
  - micro-porto2000-meta
  - micro-porto2000-publisher
  - micro-porto2000-api
  - micro-context-reservosome
- assessment_id: micro-early-endosome-lipid-route
  area: evidence
  topic: Lipid-specific transit remains unverified
  outcome: unknown
  summary: The final whole-endosome graph description extends cargo transit to protein
    and lipid. Current primary abstract directly traces gold-protein conjugates and
    does not describe a lipid tracer. Full primary body remains inaccessible through
    checked routes, so neither confirmation nor contradiction of lipid-specific passage
    is established. Preserve the original explicit unknown; no new scientific finding
    solely from access limitation.
  target_ids:
  - GO:0005769
  evidence_ids:
  - micro-record-early_endosome
  - micro-prior-early_endosome
  - micro-porto2000-meta
  - micro-porto2000-publisher
  - micro-porto2000-api
- assessment_id: septin-cytoplasmic_vesicle-schema
  area: schema
  topic: Original schema/render and unchanged frozen targets
  outcome: supported
  summary: Original bundle validation and deterministic rendering pass. Original target
    hash matches its historical source and current bytes; no stale refresh is required
    for these three records.
  target_ids:
  - GO:0031410
  evidence_ids:
  - septin-record-cytoplasmic_vesicle
  - septin-original-validation-cytoplasmic_vesicle
- assessment_id: septin-cytoplasmic_vesicle-native-scope
  area: provenance
  topic: Empty represented protein inventory
  outcome: supported
  summary: No protein examples or UniProtKB graph xrefs and zero GENE_OR_PROTEIN graph
    nodes. Native execution success covers only this empty represented inventory,
    not narrative pathway mechanisms, source-localized molecular actors or completeness.
  target_ids:
  - GO:0031410
  evidence_ids:
  - septin-record-cytoplasmic_vesicle
  - septin-native-cytoplasmic_vesicle-verify
  - septin-native-cytoplasmic_vesicle-causal
- assessment_id: septin-cytoplasmic_vesicle-nonasserted-surfaces
  area: scope
  topic: Images, physical measurements, traits and snippets
  outcome: not_applicable
  summary: No such surface is declared in the maintained target. A study caption or
    source description is not target image/pixel or raw-data validation.
  target_ids:
  - GO:0031410
  evidence_ids:
  - septin-record-cytoplasmic_vesicle
- assessment_id: septin-cytoplasmic_vesicle_lumen-schema
  area: schema
  topic: Original schema/render and unchanged frozen targets
  outcome: supported
  summary: Original bundle validation and deterministic rendering pass. Original target
    hash matches its historical source and current bytes; no stale refresh is required
    for these three records.
  target_ids:
  - GO:0060205
  evidence_ids:
  - septin-record-cytoplasmic_vesicle_lumen
  - septin-original-validation-cytoplasmic_vesicle_lumen
- assessment_id: septin-cytoplasmic_vesicle_lumen-native-scope
  area: provenance
  topic: Empty represented protein inventory
  outcome: supported
  summary: No protein examples or UniProtKB graph xrefs and zero GENE_OR_PROTEIN graph
    nodes. Native execution success covers only this empty represented inventory,
    not narrative pathway mechanisms, source-localized molecular actors or completeness.
  target_ids:
  - GO:0060205
  evidence_ids:
  - septin-record-cytoplasmic_vesicle_lumen
  - septin-native-cytoplasmic_vesicle_lumen-verify
  - septin-native-cytoplasmic_vesicle_lumen-causal
- assessment_id: septin-cytoplasmic_vesicle_lumen-nonasserted-surfaces
  area: scope
  topic: Images, physical measurements, traits and snippets
  outcome: not_applicable
  summary: No such surface is declared in the maintained target. A study caption or
    source description is not target image/pixel or raw-data validation.
  target_ids:
  - GO:0060205
  evidence_ids:
  - septin-record-cytoplasmic_vesicle_lumen
- assessment_id: septin-cytoplasmic_vesicle_membrane-schema
  area: schema
  topic: Original schema/render and unchanged frozen targets
  outcome: supported
  summary: Original bundle validation and deterministic rendering pass. Original target
    hash matches its historical source and current bytes; no stale refresh is required
    for these three records.
  target_ids:
  - GO:0030659
  evidence_ids:
  - septin-record-cytoplasmic_vesicle_membrane
  - septin-original-validation-cytoplasmic_vesicle_membrane
- assessment_id: septin-cytoplasmic_vesicle_membrane-native-scope
  area: provenance
  topic: Empty represented protein inventory
  outcome: supported
  summary: No protein examples or UniProtKB graph xrefs and zero GENE_OR_PROTEIN graph
    nodes. Native execution success covers only this empty represented inventory,
    not narrative pathway mechanisms, source-localized molecular actors or completeness.
  target_ids:
  - GO:0030659
  evidence_ids:
  - septin-record-cytoplasmic_vesicle_membrane
  - septin-native-cytoplasmic_vesicle_membrane-verify
  - septin-native-cytoplasmic_vesicle_membrane-causal
- assessment_id: septin-cytoplasmic_vesicle_membrane-nonasserted-surfaces
  area: scope
  topic: Images, physical measurements, traits and snippets
  outcome: not_applicable
  summary: No such surface is declared in the maintained target. A study caption or
    source description is not target image/pixel or raw-data validation.
  target_ids:
  - GO:0030659
  evidence_ids:
  - septin-record-cytoplasmic_vesicle_membrane
- assessment_id: septin-cytoplasmic_vesicle-taxon
  area: scope
  topic: Yeast occurrence and condition-bounded subtype evidence
  outcome: supported
  summary: S.cerevisiae is correctly identified; Reggiori names BY4742/SEY6210 and
    conditional strains. The canonical note states a broad model and early-secretory
    assembly study, without an unsupported strain-specific microscopy claim. COMMON
    is qualitative, and the Cvt subtype is not a universal mechanism or membrane-origin
    model for all cytoplasmic vesicles.
  target_ids:
  - GO:0031410
  evidence_ids:
  - septin-record-cytoplasmic_vesicle
  - septin-tax4932
  - septin-reggiori2004-meta
  - septin-reggiori2004-pmc
  - septin-go
- assessment_id: septin-cytoplasmic_vesicle-adapter
  area: scope
  topic: Actual pathway applicability and catalogue noncoverage
  outcome: not_applicable
  summary: The complete record affirms Cvt/early-secretory pathway context, so an
    expression-only exemption is insufficient. Current official catalogue inspection
    finds no matching yeast organism/dataset; downstream gene/module queries are not
    applicable. Historical unavailable runner remains separately timestamped and noncoverage
    does not imply biological absence.
  target_ids:
  - GO:0031410
  evidence_ids:
  - septin-record-cytoplasmic_vesicle
  - septin-review-policy
  - septin-catalogue
  - septin-historical-adapter-runner
- assessment_id: septin-cytoplasmic_vesicle-history
  area: provenance
  topic: Current status and scope of historical statements
  outcome: supported
  summary: PROPOSED status and historical curation text are unchanged. Current source
    review does not retrospectively certify old gate execution, authorship or searches
    and does not terminally resolve any neighbor/group/category issue.
  target_ids:
  - GO:0031410
  evidence_ids:
  - septin-record-cytoplasmic_vesicle
  - septin-original-cytoplasmic_vesicle
  - septin-context-cvt_vesicle
  - septin-context-cvt_vesicle_membrane
- assessment_id: septin-cytoplasmic_vesicle_lumen-taxon
  area: scope
  topic: Yeast occurrence and condition-bounded subtype evidence
  outcome: supported
  summary: S.cerevisiae is correctly identified; Reggiori names BY4742/SEY6210 and
    conditional strains. The canonical note states a broad model and early-secretory
    assembly study, without an unsupported strain-specific microscopy claim. COMMON
    is qualitative, and the Cvt subtype is not a universal mechanism or membrane-origin
    model for all cytoplasmic vesicles.
  target_ids:
  - GO:0060205
  evidence_ids:
  - septin-record-cytoplasmic_vesicle_lumen
  - septin-tax4932
  - septin-reggiori2004-meta
  - septin-reggiori2004-pmc
  - septin-go
- assessment_id: septin-cytoplasmic_vesicle_lumen-adapter
  area: scope
  topic: Actual pathway applicability and catalogue noncoverage
  outcome: not_applicable
  summary: The complete record affirms Cvt/early-secretory pathway context, so an
    expression-only exemption is insufficient. Current official catalogue inspection
    finds no matching yeast organism/dataset; downstream gene/module queries are not
    applicable. Historical unavailable runner remains separately timestamped and noncoverage
    does not imply biological absence.
  target_ids:
  - GO:0060205
  evidence_ids:
  - septin-record-cytoplasmic_vesicle_lumen
  - septin-review-policy
  - septin-catalogue
  - septin-historical-adapter-runner
- assessment_id: septin-cytoplasmic_vesicle_lumen-history
  area: provenance
  topic: Current status and scope of historical statements
  outcome: supported
  summary: PROPOSED status and historical curation text are unchanged. Current source
    review does not retrospectively certify old gate execution, authorship or searches
    and does not terminally resolve any neighbor/group/category issue.
  target_ids:
  - GO:0060205
  evidence_ids:
  - septin-record-cytoplasmic_vesicle_lumen
  - septin-original-cytoplasmic_vesicle_lumen
  - septin-context-cvt_vesicle
  - septin-context-cvt_vesicle_membrane
- assessment_id: septin-cytoplasmic_vesicle_membrane-taxon
  area: scope
  topic: Yeast occurrence and condition-bounded subtype evidence
  outcome: supported
  summary: S.cerevisiae is correctly identified; Reggiori names BY4742/SEY6210 and
    conditional strains. The canonical note states a broad model and early-secretory
    assembly study, without an unsupported strain-specific microscopy claim. COMMON
    is qualitative, and the Cvt subtype is not a universal mechanism or membrane-origin
    model for all cytoplasmic vesicles.
  target_ids:
  - GO:0030659
  evidence_ids:
  - septin-record-cytoplasmic_vesicle_membrane
  - septin-tax4932
  - septin-reggiori2004-meta
  - septin-reggiori2004-pmc
  - septin-go
- assessment_id: septin-cytoplasmic_vesicle_membrane-adapter
  area: scope
  topic: Actual pathway applicability and catalogue noncoverage
  outcome: not_applicable
  summary: The complete record affirms Cvt/early-secretory pathway context, so an
    expression-only exemption is insufficient. Current official catalogue inspection
    finds no matching yeast organism/dataset; downstream gene/module queries are not
    applicable. Historical unavailable runner remains separately timestamped and noncoverage
    does not imply biological absence.
  target_ids:
  - GO:0030659
  evidence_ids:
  - septin-record-cytoplasmic_vesicle_membrane
  - septin-review-policy
  - septin-catalogue
  - septin-historical-adapter-runner
- assessment_id: septin-cytoplasmic_vesicle_membrane-history
  area: provenance
  topic: Current status and scope of historical statements
  outcome: supported
  summary: PROPOSED status and historical curation text are unchanged. Current source
    review does not retrospectively certify old gate execution, authorship or searches
    and does not terminally resolve any neighbor/group/category issue.
  target_ids:
  - GO:0030659
  evidence_ids:
  - septin-record-cytoplasmic_vesicle_membrane
  - septin-original-cytoplasmic_vesicle_membrane
  - septin-context-cvt_vesicle
  - septin-context-cvt_vesicle_membrane
- assessment_id: septin-cytoplasmic_vesicle-identity
  area: identity
  topic: Whole cytoplasmic carrier class
  outcome: supported
  summary: GO0031410 definition, vesicle parentage, membrane/lumen parts and exact
    SL0088 mapping identify a complete membrane-bounded cytoplasmic vesicle. The generic
    record is distinct from Cvt or coat-defined subtypes, cargo proteins and transport
    processes.
  target_ids:
  - GO:0031410
  evidence_ids:
  - septin-record-cytoplasmic_vesicle
  - septin-go
  - septin-SL0088
  - septin-SL0089
  - septin-SL0325
  - septin-context-cvt_vesicle
- assessment_id: septin-cytoplasmic_vesicle-material
  area: grounding
  topic: Collective defining membrane part
  outcome: supported
  summary: The grounded LIPID row denotes the complete structural membrane part defined
    by GO0030659. ESSENTIAL is collective bilayer constitution, not a claimed necessity
    for each molecular lipid or protein. No full inventory or stoichiometry is asserted.
  target_ids:
  - GO:0031410
  evidence_ids:
  - septin-record-cytoplasmic_vesicle
  - septin-curation-policy
  - septin-go
  - septin-SL0089
- assessment_id: septin-cytoplasmic_vesicle-necessity
  area: grounding
  topic: Individual molecular formation requirements
  outcome: unknown
  summary: The selected primary transport evidence does not establish individual lipid-species
    removal/substitution requirements. This uncertainty does not negate the membrane-bounded
    identity or create an unsupported knockout claim.
  target_ids:
  - GO:0031410
  evidence_ids:
  - septin-record-cytoplasmic_vesicle
  - septin-go
  - septin-reggiori2004-pmc
- assessment_id: septin-cytoplasmic_vesicle-function-graph
  area: graph
  topic: Broad transport function and two nonmechanistic edges
  outcome: supported
  summary: SL0088 supports the broad secretory/endocytic carrier context. The two
    edges assert membrane parthood and carrier support of that transport class. They
    do not prescribe a universal coat, cargo, donor/acceptor pair or budding/fusion
    mechanism.
  target_ids:
  - GO:0031410
  evidence_ids:
  - septin-record-cytoplasmic_vesicle
  - septin-go
  - septin-SL0088
  - septin-SL0089
  - septin-graph-policy
- assessment_id: septin-cytoplasmic_vesicle-subtype-boundary
  area: completeness
  topic: Subtype coats and cargo are not universal components
  outcome: supported
  summary: The resolved local discussion explicitly excludes subtype-specific clathrin/COPI/COPII,
    synaptic/secretory cargo and phagosome examples from generic constituents. Exact
    source scope supports this boundary. This reassessment does not newly resolve
    any earlier issue or certify a complete subtype inventory.
  target_ids:
  - GO:0031410
  evidence_ids:
  - septin-record-cytoplasmic_vesicle
  - septin-SL0088
  - septin-curation-policy
- assessment_id: septin-cytoplasmic_vesicle_lumen-identity
  area: identity
  topic: Exact enclosed-volume identity and hierarchy
  outcome: supported
  summary: GO0060205 and SL0325 denote the cytoplasmic-vesicle enclosed volume. GO0031983
    is its vesicle-lumen parent; cytoplasmic-vesicle parthood is supported. A lumen
    is a region, not its cargo or an independently operating pathway.
  target_ids:
  - GO:0060205
  evidence_ids:
  - septin-record-cytoplasmic_vesicle_lumen
  - septin-go
  - septin-SL0325
- assessment_id: septin-cytoplasmic_vesicle_lumen-graph
  area: graph
  topic: Two boundary relations and no generic cargo function
  outcome: supported
  summary: Lumen part_of whole vesicle and membrane encloses lumen follow the exact
    GO/location descriptions. The Cvt model illustrates enclosed cargo volume without
    assigning universal cargo or molecular transport steps to every lumen. No removed
    generic-cargo function is silently restored.
  target_ids:
  - GO:0060205
  evidence_ids:
  - septin-record-cytoplasmic_vesicle_lumen
  - septin-go
  - septin-SL0325
  - septin-SL0089
  - septin-reggiori2004-pmc
  - septin-graph-policy
- assessment_id: septin-cytoplasmic_vesicle_lumen-composition
  area: completeness
  topic: Optional lumen inventory remains unasserted
  outcome: not_applicable
  summary: No material component, individual protein or molecular essentiality row
    is declared. A soluble inventory or independent process function is not required
    to define the bounded generic region; no absent optional field is called a defect.
  target_ids:
  - GO:0060205
  evidence_ids:
  - septin-record-cytoplasmic_vesicle_lumen
  - septin-curation-policy
- assessment_id: septin-cytoplasmic_vesicle_membrane-identity
  area: identity
  topic: Exact surrounding-bilayer identity
  outcome: supported
  summary: GO0030659 definition, membrane parent, cytoplasmic-vesicle parthood and
    exact SL0089 mapping identify the surrounding membrane. These remain correct despite
    the localized Cvt example wording defect.
  target_ids:
  - GO:0030659
  evidence_ids:
  - septin-record-cytoplasmic_vesicle_membrane
  - septin-go
  - septin-SL0089
  - septin-context-cvt_vesicle_membrane
- assessment_id: septin-cytoplasmic_vesicle_membrane-material
  area: grounding
  topic: Collective bilayer with limited chemical specificity
  outcome: supported
  summary: REVIEWED_LABEL_ONLY applies to the generic lipid constituent, with an explicit
    chemical-grounding TODO. The membrane location is not falsely used as an individual
    lipid-species identity. This review does not establish exhaustive ontology absence
    or specific composition ratios.
  target_ids:
  - GO:0030659
  evidence_ids:
  - septin-record-cytoplasmic_vesicle_membrane
  - septin-go
  - septin-SL0089
  - septin-curation-policy
- assessment_id: septin-cytoplasmic_vesicle_membrane-necessity
  area: grounding
  topic: Constitution does not establish individual-lipid necessity
  outcome: unknown
  summary: The ESSENTIAL material row is definitional membrane constitution. Reggiori
    transport experiments do not establish removal/substitution requirements for particular
    lipid species, and no such molecular assay is asserted.
  target_ids:
  - GO:0030659
  evidence_ids:
  - septin-record-cytoplasmic_vesicle_membrane
  - septin-go
  - septin-reggiori2004-pmc
- assessment_id: septin-cytoplasmic_vesicle_membrane-graph
  area: graph
  topic: Two descriptive membrane relations
  outcome: supported
  summary: Membrane part_of and bounds whole cytoplasmic vesicle are supported surrounding-boundary
    relations. The nonmechanistic graph does not assert a coat, universal cargo or
    donor/acceptor mechanism and is not itself affected by the taxonomic-note error.
  target_ids:
  - GO:0030659
  evidence_ids:
  - septin-record-cytoplasmic_vesicle_membrane
  - septin-go
  - septin-SL0089
  - septin-graph-policy
- assessment_id: septin-cytoplasmic_vesicle_membrane-example-wording
  area: scope
  topic: Cvt carrier versus either constituent bilayer
  outcome: concern
  summary: The taxonomic note still calls Cvt vesicle membranes a double-membrane
    cytosolic carrier subtype. Current GO0033110 denotes either bilayer; GO0033107
    and Reggiori identify the entire carrier as double-membrane. This reproduces the
    original minor F1 exactly and requires only separately authorized note curation.
  target_ids:
  - GO:0030659
  evidence_ids:
  - septin-record-cytoplasmic_vesicle_membrane
  - septin-go
  - septin-reggiori2004-pmc
  - septin-context-cvt_vesicle
  - septin-context-cvt_vesicle_membrane
- assessment_id: septin-cytoplasmic_vesicle-verdict
  area: evidence
  topic: Qualified positive scientific assessment
  outcome: supported
  summary: No concrete scientific correction was established in this complete assigned-record
    scope. Retain conditional subtype evidence, partial primary-body access, chemical
    necessity unknowns, empty native inventory and catalogue noncoverage. The review
    applicability defect is separately corrected by an immutable successor.
  target_ids:
  - GO:0031410
  evidence_ids:
  - septin-record-cytoplasmic_vesicle
  - septin-go
  - septin-reggiori2004-pmc
  - septin-catalogue
- assessment_id: septin-cytoplasmic_vesicle_lumen-verdict
  area: evidence
  topic: Qualified positive scientific assessment
  outcome: supported
  summary: No concrete scientific correction was established in this complete assigned-record
    scope. Retain conditional subtype evidence, partial primary-body access, chemical
    necessity unknowns, empty native inventory and catalogue noncoverage. The review
    applicability defect is separately corrected by an immutable successor.
  target_ids:
  - GO:0060205
  evidence_ids:
  - septin-record-cytoplasmic_vesicle_lumen
  - septin-go
  - septin-reggiori2004-pmc
  - septin-catalogue
- assessment_id: septin-cytoplasmic_vesicle_membrane-verdict
  area: evidence
  topic: One inherited minor finding remains open
  outcome: concern
  summary: Identity, component, hierarchy and graph remain sound. The one inherited
    carrier-versus-bilayer example note remains a minor request for separate record
    curation; a positive schema or native accession check does not resolve it.
  target_ids:
  - GO:0030659
  evidence_ids:
  - septin-record-cytoplasmic_vesicle_membrane
  - septin-go
  - septin-reggiori2004-pmc
  - septin-original-cytoplasmic_vesicle_membrane
- assessment_id: current-input-comparison
  area: provenance
  topic: Complete frozen-input comparison and bounded refresh
  outcome: supported
  summary: 1 of ten original target hashes differ from current main. The changed content
    is substantively reassessed in the target-specific assessments; original observations
    remain historical and unchanged. All current target and used context bytes are
    frozen.
  target_ids:
  - GO:0009843
  - GO:0033114
  - GO:0033115
  - GO:0031410
  - GO:0060205
  - GO:0030659
  - cellstructuremech:diazoplast
  - GO:0005769
  - GO:0031905
  - GO:0031901
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
  issue_key: diazoplast-cross-taxon-protein-example-placement
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Identity-only Azotobacter references occupy a structure-specific protein-example
    field
  description: ProteinExample is defined as an organism-specific instance where the
    protein role in the structure was established. The three Azotobacter examples
    explicitly establish accession/gene identity only and disclaim structure membership;
    the cited diazoplast experiments instead concern Epithemia. Their placement therefore
    exceeds the field contract despite appropriately cautious notes. The accessions,
    gene tokens, taxa and nitrogenase component itself are valid.
  target_ids:
  - cellstructuremech:diazoplast
  field_paths:
  - components#nitrogenase.protein_examples
  evidence_ids:
  - micro-record-diazoplast
  - micro-schema-protein-example
  - micro-moulin2024-jats
  - micro-frail2025-jats
  - micro-protein-C1DK95
  - micro-protein-P07328
  - micro-protein-P07329
  - micro-tax354
  - micro-tax322710
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/diazoplast.yaml
    role: maintained scientific record
  rule_id: src/cellstructuremech/schema/cellstructuremech.yaml:Component.protein_examples
    and ProteinExample description
  native_severity: minor
  normalization_reason: Minor because explicit identity-only disclaimers preserve
    the scientific distinction and the underlying nitrogenase membership is supported;
    the correction concerns placement/provenance, not wrong identity or genus-wide
    nitrogenase scope.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T013532Z-diazoplast-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2679
- finding_id: septin-F1
  issue_key: cytoplasmic-vesicle-membrane-cvt-example-carrier-wording
  category: nomenclature
  severity: minor
  status: open
  certainty: confirmed
  title: Keep the Cvt membrane example distinct from its complete carrier
  description: The Saccharomyces distribution note describes Cvt vesicle membranes
    as a double-membrane cytosolic carrier subtype of the cytoplasmic vesicle membrane
    class. GO:0033110 denotes either constituent bilayer; GO:0033107 and Reggiori
    describe the whole carrier as double-membrane. Rewrite the local note to say that
    budding yeast has Cvt vesicles whose individual bilayers are cytoplasmic-vesicle-membrane
    subtypes. The record identity, taxon, membrane component and graph remain sound.
  target_ids:
  - GO:0030659
  field_paths:
  - taxonomic_distribution[taxon_id=NCBITaxon:4932].note
  evidence_ids:
  - septin-record-cytoplasmic_vesicle_membrane
  - septin-go
  - septin-reggiori2004-pmc
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/cytoplasmic_vesicle_membrane.yaml
    role: maintained scientific record
  rule_id: 'review-checklist:Identity; Taxonomic distribution; docs/CURATION.md: exact
    claim scope'
  native_severity: minor
  normalization_reason: Localized carrier-versus-bilayer wording in an example note;
    it does not change the correct target identity or hierarchy.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T013531Z-cytoplasmic-vesicle-membrane-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2678
actions:
- action_id: micro-A1
  finding_ids:
  - micro-F1
  target_ids:
  - cellstructuremech:diazoplast
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/diazoplast.yaml
    role: maintained scientific record
  description: In a separately authorized curation change, move cross-taxon identity-only
    references to discussion/context, or replace them with verified diazoplast/symbiont
    instances only when source-backed. If no such instances are established, omit
    protein_examples while preserving the supported nitrogenase component, gene-symbol
    metadata and primary evidence.
  acceptance_checks:
  - Every retained protein_example has exact native identity metadata and evidence
    linking that instance/taxon to the diazoplast structure; identity-only references
    remain clearly contextual.
  - Do not relabel Azotobacter accessions as Epithemia or infer an incorrect gene
    from the anfH/nifH synonym bridge.
  - Preserve the supported nif cluster, nitrogenase membership and UNKNOWN formation
    necessity; run focused schema, strict and UniProt verification checks.
  - Record curation remains a separate guarded-writer change; this review PR edits
    no scientific record.
- action_id: septin-A1
  finding_ids:
  - septin-F1
  target_ids:
  - GO:0030659
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/cytoplasmic_vesicle_membrane.yaml
    role: maintained scientific record
  description: Under separately authorized curation, reword the yeast occurrence note
    to distinguish the whole double-membrane Cvt vesicle from either of its bilayers;
    keep the existing native IDs and taxon.
  acceptance_checks:
  - The note assigns the double-membrane carrier description to the Cvt vesicle and
    the generic membrane subtype relation to either Cvt bilayer.
  - Use the guarded writer and required history; run focused schema/strict and history
    checks, then render and qc.
  generator: Maintained scientific YAML; just render derives pages.
limitations:
- 'Cyanelle thylakoid, lumen and membrane independent subreview: Three assigned cyanelle
  thylakoid targets only, all unchanged from original inputs. No extra local neighbor
  record was used. Existing neighbor/group/category issues, including2675, are not
  resolved or recertified by this review.'
- 'Cyanelle thylakoid, lumen and membrane independent subreview: Giddings source scope
  is independently viewed scanned pages409–413 and416–418, including declared text/figures.
  Pages409/410/412/416/417 and bibliography metadata reuse actual11:52Z PR2362 snapshots;
  pages411/413/418 were fetched12:28Z. No complete-paper or raw-data reanalysis. Fig19
  is a model, not experimental proof; precise PSI localization is explicitly unknown
  in the paper.'
- 'Cyanelle thylakoid, lumen and membrane independent subreview: Giddings cultured
  C.paradoxa UTEX LB555 at26C in modified CY-II with continuous illumination. Isolated
  cyanelles/thylakoids, pigment-removal preparations and thin-section/freeze-fracture/etch
  microscopy are distinct assays. No complete molecular inventory, universal strain
  composition, measured live-cell rate or individual formation requirement is inferred.'
- 'Cyanelle thylakoid, lumen and membrane independent subreview: Fresh GO/UniProt
  sources establish exact structure identity, typed parthood and valid direct/broader
  parents. Native schema coarse whole-organelle granularity explicitly includes thylakoids;
  this is not a separate GO is_a organelle claim. COMMON describes qualitative occurrence,
  not a prevalence estimate.'
- 'Cyanelle thylakoid, lumen and membrane independent subreview: Whole thylakoid and
  membrane assert light-reaction pathway context and require structured-source applicability
  correction. Lumen is genuinely topology-only and excluded; missing proteins are
  not fabricated as defects. Catalogue lacks a matching glaucophyte host; no matched
  downstream gene/module query or cyanobacterial substitution is justified.'
- 'Cyanelle thylakoid, lumen and membrane independent subreview: Historical00:49Z
  PermissionError runner failure remains an earlier unavailable check, not a new invocation
  or success. Fresh official catalogue and source-scoped literature/authority checks
  are distinct fallback evidence.'
- 'Cyanelle thylakoid, lumen and membrane independent subreview: All six native protein
  checks pass empty inventories and zero GENE_OR_PROTEIN nodes; this does not independently
  prove biological function or necessity. Root owns global gates, issue filing and
  all repository/GitHub mutations.'
- 'Diazoplast and early-endosome trio independent subreview: Diazoplast/early-endosome
  independent slice: Four complete targets and original pairs reviewed; neighbors
  nitroplast/reservosome read only at frozen boundary/taxon/discussion fields. No
  neighbor/category/group issue resolved; #2404 history is not a disposition of its
  full predecessor.'
- 'Diazoplast and early-endosome trio independent subreview: Diazoplast source scope:
  Moulin Introduction/Results/Discussion and stated supplementary methods inspected;
  only maintained Figure2 pixels viewed. Other figures were read as captions/text
  only. Frail body scope is Introduction,Results s5–7,Discussion s8,Methods s18–19;
  SI only axenic-culture paragraph plus neighboring context. No full genome/proteomics/raw-data
  audit or supplemental figure inspection.'
- 'Diazoplast and early-endosome trio independent subreview: Diazoplast source scope:
  Imaging, biochemical detection, culture activity and enrichment do not establish
  every molecule necessity, exhaustive composition or host-protein import. HupL family
  search includes two synonym-collision accessory proteins, excluded from large-subunit
  interpretation; InterPro IPR050867 generated description is not primary evidence.'
- 'Diazoplast and early-endosome trio independent subreview: Early-endosome source
  scope: Porto2000 complete primary abstract plus metadata only; ScienceDirect403
  and public API metadata stub do not provide body/methods/strain/figure evidence.
  Protein routing supported; lipid-specific routing remains unknown, neither confirmed
  nor contradicted. Source authors proposed early-endosome identity using uptake kinetics
  and acidity, not a molecular marker.'
- 'Diazoplast and early-endosome trio independent subreview: Diazoplast/early-endosome
  source scope: All four assert named molecular or pathway context requiring applicability
  assessment despite nonmolecular topology nodes. Fresh complete public catalogue
  has no matching organism/dataset; no downstream module query or biological absence
  conclusion. Actual native runner failure remains historical00:49Z, not a fresh attempt.'
- 'Diazoplast and early-endosome trio independent subreview: Diazoplast/early-endosome
  native-check scope: Eight commands returned0; diazoplast verify checks three represented
  accession examples, other inventories empty; all causal typed-protein inventories
  zero after complex retyping. Schema/protein validators do not resolve membership
  or scientifically validate graph edges. Root owns full-corpus gates, issue dedup,
  final CI and queue; no future result borrowed.'
- 'Cytoplasmic vesicle, lumen and membrane independent subreview: All three current
  targets match original frozen and historical-source hashes. Membrane F1 retains
  its exact original issue key and occurrence; whole/lumen original finding lists
  were empty. No newly invented predecessor or terminal disposition.'
- 'Cytoplasmic vesicle, lumen and membrane independent subreview: Reggiori2004 public-source
  metadata and genuine HTML were fetched during PR2362 at actual11:51:54.023844Z and11:52:44.039650Z.
  Hashes were checked and bodies independently reread here. Current scope is complete
  abstract, Introduction sec1, Strains/Media sec3/Table1, Results sec14/Figure8 text,
  Discussion sec17 and18/Figure9 text only; no fresh paper fetch, complete article,
  figure pixels or raw-data reanalysis claimed.'
- 'Cytoplasmic vesicle, lumen and membrane independent subreview: Primary intro/discussion
  includes prior-study synthesis and proposed models. Conditional sec12/sec7 experiments
  do not establish an exclusive ER/Golgi donor, universal vesicle formation mechanism
  or quantitative COMMON prevalence. Cvt subtype evidence is not a universal molecular
  census.'
- 'Cytoplasmic vesicle, lumen and membrane independent subreview: Native six commands
  pass with no protein examples/xrefs and zero GENE_OR_PROTEIN nodes. This empty-inventory
  result does not independently validate narrative pathways, molecular actors, localization
  or composition. Collective bilayer constitution does not prove individual lipid
  necessity.'
- 'Cytoplasmic vesicle, lumen and membrane independent subreview: All three records
  affirmatively cite Cvt/early-secretory pathway context despite geometry-focused
  graphs; their original expression-only exemptions need correction. Current complete
  catalogue lacks yeast coverage. No unmatched-host query or biological absence inference;
  runner failure remains actual historical00:49Z, not a new run.'
- 'Cytoplasmic vesicle, lumen and membrane independent subreview: Two frozen Cvt neighbors
  were read at boundary fields only. No independent full-neighbor review, protein
  example audit or resolution of their findings is asserted. No target image, measurement,
  trait link or verbatim snippet is declared.'
- 'Cytoplasmic vesicle, lumen and membrane independent subreview: Root owns full-cohort
  QC, issue deduplication/publication, repository/GitHub mutations and final-head/queue
  CI. The review-only scope leaves scientific record curation separate.'
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
  Both inherited scientific findings retain their stable issue keys and exact predecessor
  repository/review/finding identities.
- 'Issue #2676 tracks the stale diazoplast target: a history entry and nitrogenase-complex
  node retyping from GENE_OR_PROTEIN to STRUCTURE. Current authority and native node-type
  policy support the complex-structure interpretation. The closed grouped #2404 is
  historical context; no other group target or finding is disposed of here.'
- 'Issue #2677 tracks nine applicability defects: cyanelle thylakoid and its membrane
  assert light reactions; the three cytoplasmic-vesicle records assert Cvt/early-secretory
  context; diazoplast asserts nitrogen fixation and molecular examples; the early-endosome
  trio asserts endocytic cargo-routing context. Thylakoid lumen remains a genuine
  topology-only exclusion with molecular transport and lumen proteins withheld.'
- Source commit cd5be11ad13304d75404a51d097635022d1bd091 is retained by tag review-base/pr2363-current-record-followup-20261103.
- CLAUDE.md is an alias of AGENTS.md; canonical regular AGENTS.md bytes are frozen.
- All 52 used local inputs were frozen before assessment, including four neighbor
  records, the actual diazoplast image, native configuration, graph/protein policies
  and verifier source. Neighbors are boundary context only, not additional targets
  or dispositions of their findings.
- Fresh and reused public-source snapshots retain actual access dates and inspection
  tiers. Authority identity does not independently establish structure membership,
  mechanistic action, species-wide generalization or assembly necessity.
- All twenty native protein commands returned zero. Diazoplast has three verified
  Azotobacter protein examples, while its retyped nitrogenase complex is no longer
  a GENE_OR_PROTEIN node; typed molecular graph coverage is therefore zero. The other
  nine targets have empty protein inventories and zero typed molecular nodes. Those
  results do not validate narrative molecules, pathway claims or Epithemia diazoplast
  membership.
- The inherited cytoplasmic-vesicle membrane finding distinguishes either Cvt bilayer
  from the complete double-membrane carrier. The inherited diazoplast finding distinguishes
  valid cross-taxon accession identities from the ProteinExample requirement for organism-specific
  structure membership. Retyping the complex does not resolve that placement defect.
- The actual frozen diazoplast Figure 2, its source, caption, taxon, NanoSIMS/quantification
  scope and CC BY 4.0 licence are assessed. Isotope enrichment supports the bounded
  exchange interpretation without establishing arbitrary protein membership.
- 'Current whole-cyanelle issue #2675 concerns an anatomical evidence note in a distinct
  record and is not resolved here. The source model uncertainty about precise photosystem
  localization is not converted into an asserted thylakoid mechanism.'
- 'The two minor scientific findings remain open for separately authorized record
  curation: #2678 for the membrane wording and #2679 for diazoplast cross-taxon protein-example
  placement. Eight other targets retain qualified positive scientific assessments.
  No record is edited.'
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T013526Z-cyanelle-thylakoid-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T013527Z-cyanelle-thylakoid-lumen-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T013528Z-cyanelle-thylakoid-membrane-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T013529Z-cytoplasmic-vesicle-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T013530Z-cytoplasmic-vesicle-lumen-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T013531Z-cytoplasmic-vesicle-membrane-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T013532Z-diazoplast-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T013533Z-early-endosome-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T013534Z-early-endosome-lumen-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T013534Z-early-endosome-membrane-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
links:
- https://github.com/CultureBotAI/CellStructureMech/pull/2363
- https://github.com/CultureBotAI/CellStructureMech/issues/2514
- https://github.com/CultureBotAI/CellStructureMech/issues/2676
- https://github.com/CultureBotAI/CellStructureMech/issues/2677
- https://github.com/CultureBotAI/CellStructureMech/issues/2678
- https://github.com/CultureBotAI/CellStructureMech/issues/2679
```
