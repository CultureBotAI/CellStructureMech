# PR 2371: current-input review of ten records and adversarial follow-up

- Review: 20261103T173325Z-pr2371-current-record-followup
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-11-03T17:25:27.314718Z
- Finished UTC: 2026-11-03T17:33:25Z
- Reviewer: Codex root synthesis with three independent read-only adversarial reviewers (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Current-input adversarial follow-up for the complete ten-record cohort after merging main. All ten original target hashes still match; no stale review refresh is required. Six unsupported expression-only structured-source exclusions are corrected, while four mitosome compartments retain genuine physical/material-scope exclusions. Independent source review preserves seven inherited findings (three major and four minor) across seven records, with three qualified positive assessments. The MDL1 protein example, exact MVB compartment ontology identities and four citation titles remain separate record-curation tasks. All original review observations and scientific records remain unchanged.

## Scope And Provenance

Exact ten-record PR cohort reassessed against current main a56ca22a64ab01554d81d3188c47569d0fc9b162. Changed inputs are substantively reassessed. Scientific records remain unchanged.

Selection: Complete cohort of ten maintained records reviewed in original PR head eac6f6d992414efd884ca390ba15bcfe0a7ed730.
Coverage: full; 10 reviewed / 10 in the declared population.
Source: working_tree at Git base d6a41b5d3397c9d62944c9c21890ef47a097a0fa.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:mitosome_inner_membrane | data/structures/membrane_organelle/mitosome_inner_membrane.yaml | maintained | mitosome inner membrane |
| cellstructuremech:mitosome_intermembrane_space | data/structures/membrane_organelle/mitosome_intermembrane_space.yaml | maintained | mitosome intermembrane space |
| cellstructuremech:mitosome_matrix | data/structures/membrane_organelle/mitosome_matrix.yaml | maintained | mitosome matrix |
| cellstructuremech:mitosome_outer_membrane | data/structures/membrane_organelle/mitosome_outer_membrane.yaml | maintained | mitosome outer membrane |
| GO:0070074 | data/structures/membrane_organelle/mononeme.yaml | maintained | mononeme |
| GO:0036000 | data/structures/membrane_organelle/mucocyst.yaml | maintained | mucocyst |
| GO:0005771 | data/structures/membrane_organelle/multivesicular_body.yaml | maintained | multivesicular body |
| cellstructuremech:multivesicular_body_intraluminal_vesicle | data/structures/membrane_organelle/multivesicular_body_intraluminal_vesicle.yaml | maintained | multivesicular body intraluminal vesicle |
| cellstructuremech:multivesicular_body_lumen | data/structures/membrane_organelle/multivesicular_body_lumen.yaml | maintained | multivesicular body lumen |
| GO:0032585 | data/structures/membrane_organelle/multivesicular_body_membrane.yaml | maintained | multivesicular body membrane |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full native QC | passed | True | cellstructuremech:mitosome_inner_membrane, cellstructuremech:mitosome_intermembrane_space, cellstructuremech:mitosome_matrix, cellstructuremech:mitosome_outer_membrane, GO:0070074, GO:0036000, GO:0005771, cellstructuremech:multivesicular_body_intraluminal_vesicle, cellstructuremech:multivesicular_body_lumen, GO:0032585 | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| Native label correspondence | passed | True | cellstructuremech:mitosome_inner_membrane, cellstructuremech:mitosome_intermembrane_space, cellstructuremech:mitosome_matrix, cellstructuremech:mitosome_outer_membrane, GO:0070074, GO:0036000, GO:0005771, cellstructuremech:multivesicular_body_intraluminal_vesicle, cellstructuremech:multivesicular_body_lumen, GO:0032585 | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| TraitMech references | passed | True | cellstructuremech:mitosome_inner_membrane, cellstructuremech:mitosome_intermembrane_space, cellstructuremech:mitosome_matrix, cellstructuremech:mitosome_outer_membrane, GO:0070074, GO:0036000, GO:0005771, cellstructuremech:multivesicular_body_intraluminal_vesicle, cellstructuremech:multivesicular_body_lumen, GO:0032585 | Native TraitMech link check passed. |
| Pinned governed files | passed | True | cellstructuremech:mitosome_inner_membrane, cellstructuremech:mitosome_intermembrane_space, cellstructuremech:mitosome_matrix, cellstructuremech:mitosome_outer_membrane, GO:0070074, GO:0036000, GO:0005771, cellstructuremech:multivesicular_body_intraluminal_vesicle, cellstructuremech:multivesicular_body_lumen, GO:0032585 | Pinned governed files match; native vendored check passed. |
| Native identifier resolver | passed | True | cellstructuremech:mitosome_inner_membrane, cellstructuremech:mitosome_intermembrane_space, cellstructuremech:mitosome_matrix, cellstructuremech:mitosome_outer_membrane, GO:0070074, GO:0036000, GO:0005771, cellstructuremech:multivesicular_body_intraluminal_vesicle, cellstructuremech:multivesicular_body_lumen, GO:0032585 | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| validate cellstructuremech:mitosome_inner_membrane | passed | True | cellstructuremech:mitosome_inner_membrane | Documented focused command passed. |
| validate-strict cellstructuremech:mitosome_inner_membrane | passed | True | cellstructuremech:mitosome_inner_membrane | Documented focused command passed. |
| validate cellstructuremech:mitosome_intermembrane_space | passed | True | cellstructuremech:mitosome_intermembrane_space | Documented focused command passed. |
| validate-strict cellstructuremech:mitosome_intermembrane_space | passed | True | cellstructuremech:mitosome_intermembrane_space | Documented focused command passed. |
| validate cellstructuremech:mitosome_matrix | passed | True | cellstructuremech:mitosome_matrix | Documented focused command passed. |
| validate-strict cellstructuremech:mitosome_matrix | passed | True | cellstructuremech:mitosome_matrix | Documented focused command passed. |
| validate cellstructuremech:mitosome_outer_membrane | passed | True | cellstructuremech:mitosome_outer_membrane | Documented focused command passed. |
| validate-strict cellstructuremech:mitosome_outer_membrane | passed | True | cellstructuremech:mitosome_outer_membrane | Documented focused command passed. |
| validate GO:0070074 | passed | True | GO:0070074 | Documented focused command passed. |
| validate-strict GO:0070074 | passed | True | GO:0070074 | Documented focused command passed. |
| validate GO:0036000 | passed | True | GO:0036000 | Documented focused command passed. |
| validate-strict GO:0036000 | passed | True | GO:0036000 | Documented focused command passed. |
| validate GO:0005771 | passed | True | GO:0005771 | Documented focused command passed. |
| validate-strict GO:0005771 | passed | True | GO:0005771 | Documented focused command passed. |
| validate cellstructuremech:multivesicular_body_intraluminal_vesicle | passed | True | cellstructuremech:multivesicular_body_intraluminal_vesicle | Documented focused command passed. |
| validate-strict cellstructuremech:multivesicular_body_intraluminal_vesicle | passed | True | cellstructuremech:multivesicular_body_intraluminal_vesicle | Documented focused command passed. |
| validate cellstructuremech:multivesicular_body_lumen | passed | True | cellstructuremech:multivesicular_body_lumen | Documented focused command passed. |
| validate-strict cellstructuremech:multivesicular_body_lumen | passed | True | cellstructuremech:multivesicular_body_lumen | Documented focused command passed. |
| validate GO:0032585 | passed | True | GO:0032585 | Documented focused command passed. |
| validate-strict GO:0032585 | passed | True | GO:0032585 | Documented focused command passed. |
| Supplemental bounded PMID authority checks | passed | True | cellstructuremech:mitosome_inner_membrane, cellstructuremech:mitosome_intermembrane_space, cellstructuremech:mitosome_matrix, cellstructuremech:mitosome_outer_membrane, GO:0070074, GO:0036000, GO:0005771, cellstructuremech:multivesicular_body_intraluminal_vesicle, cellstructuremech:multivesicular_body_lumen, GO:0032585 | 909 PMIDs all OK in bounded native requests; full-command limitations remain separate. |
| Official structured-source applicability and covered-dataset cross-checks | passed | False | cellstructuremech:mitosome_inner_membrane, cellstructuremech:mitosome_intermembrane_space, cellstructuremech:mitosome_matrix, cellstructuremech:mitosome_outer_membrane, GO:0070074, GO:0036000, GO:0005771, cellstructuremech:multivesicular_body_intraluminal_vesicle, cellstructuremech:multivesicular_body_lumen, GO:0032585 | Six records make positive protein/pathway claims requiring source applicability assessment: mononeme, mucocyst and the four MVB records. Complete fresh official iModulonDB catalogue responses have no matching Plasmodium, Tetrahymena or Saccharomyces host. No unmatched host proxy or biological absence inference is used. All four mitosome compartments have genuine collective-material/spatial-topology scope, with protein/import machinery explicitly excluded; no artificial query requirement is imposed. Historical00:49Z runner unavailability remains historical, with actual current public-source fallback documented. |
| Independent claim-level source review | passed | True | cellstructuremech:mitosome_inner_membrane, cellstructuremech:mitosome_intermembrane_space, cellstructuremech:mitosome_matrix, cellstructuremech:mitosome_outer_membrane, GO:0070074, GO:0036000, GO:0005771, cellstructuremech:multivesicular_body_intraluminal_vesicle, cellstructuremech:multivesicular_body_lumen, GO:0032585 | Three read-only reviewers covered the complete ten-record cohort, including changed inputs, with explicit scientific findings and source-access limits. Final artifact/head acceptance occurs after saving. |
| Retained historical adapter runner availability | unavailable | False | cellstructuremech:mitosome_inner_membrane, cellstructuremech:mitosome_intermembrane_space, cellstructuremech:mitosome_matrix, cellstructuremech:mitosome_outer_membrane, GO:0070074, GO:0036000, GO:0005771, cellstructuremech:multivesicular_body_intraluminal_vesicle, cellstructuremech:multivesicular_body_lumen, GO:0032585 | Historical 00:49Z invocation unavailable due to OS access restriction. Official catalogue source fallback was inspected separately; no current invocation or successful adapter execution is claimed. The actual historical exit code 1 is retained in the evidence receipt, since the native unavailable-check model has no execution exit-code field. |
| Native mitosome inner membrane UniProt verify check | passed | True | cellstructuremech:mitosome_inner_membrane | Read-only native command returned zero. No protein examples or typed molecular nodes. Actual positive pathway assertions and justified physical-scope exclusions are assessed separately. |
| Native mitosome inner membrane UniProt causal check | passed | True | cellstructuremech:mitosome_inner_membrane | Read-only native command returned zero. No protein examples or typed molecular nodes. Actual positive pathway assertions and justified physical-scope exclusions are assessed separately. |
| Native mitosome intermembrane space UniProt verify check | passed | True | cellstructuremech:mitosome_intermembrane_space | Read-only native command returned zero. No protein examples or typed molecular nodes. Actual positive pathway assertions and justified physical-scope exclusions are assessed separately. |
| Native mitosome intermembrane space UniProt causal check | passed | True | cellstructuremech:mitosome_intermembrane_space | Read-only native command returned zero. No protein examples or typed molecular nodes. Actual positive pathway assertions and justified physical-scope exclusions are assessed separately. |
| Native mitosome matrix UniProt verify check | passed | True | cellstructuremech:mitosome_matrix | Read-only native command returned zero. No protein examples or typed molecular nodes. Actual positive pathway assertions and justified physical-scope exclusions are assessed separately. |
| Native mitosome matrix UniProt causal check | passed | True | cellstructuremech:mitosome_matrix | Read-only native command returned zero. No protein examples or typed molecular nodes. Actual positive pathway assertions and justified physical-scope exclusions are assessed separately. |
| Native mitosome outer membrane UniProt verify check | passed | True | cellstructuremech:mitosome_outer_membrane | Read-only native command returned zero. No protein examples or typed molecular nodes. Actual positive pathway assertions and justified physical-scope exclusions are assessed separately. |
| Native mitosome outer membrane UniProt causal check | passed | True | cellstructuremech:mitosome_outer_membrane | Read-only native command returned zero. No protein examples or typed molecular nodes. Actual positive pathway assertions and justified physical-scope exclusions are assessed separately. |
| Native mononeme UniProt verify check | passed | True | GO:0070074 | Read-only native command returned zero. One unreviewed A8IWX2/Rom1 example and one COVERED typed node. Native identity is separate from tagged-protein localization, secretion context and causal transport evidence. |
| Native mononeme UniProt causal check | passed | True | GO:0070074 | Read-only native command returned zero. One unreviewed A8IWX2/Rom1 example and one COVERED typed node. Native identity is separate from tagged-protein localization, secretion context and causal transport evidence. |
| Native mucocyst UniProt verify check | passed | True | GO:0036000 | Read-only native command returned zero. Six unreviewed examples and three COVERED typed nodes. Field correspondence does not establish the MDL1 literature-to-locus equivalence; that inherited scientific identity finding is assessed separately. |
| Native mucocyst UniProt causal check | passed | True | GO:0036000 | Read-only native command returned zero. Six unreviewed examples and three COVERED typed nodes. Field correspondence does not establish the MDL1 literature-to-locus equivalence; that inherited scientific identity finding is assessed separately. |
| Native multivesicular body UniProt verify check | passed | True | GO:0005771 | Read-only native command returned zero. No protein examples or typed molecular nodes. Actual positive pathway assertions and justified physical-scope exclusions are assessed separately. |
| Native multivesicular body UniProt causal check | passed | True | GO:0005771 | Read-only native command returned zero. No protein examples or typed molecular nodes. Actual positive pathway assertions and justified physical-scope exclusions are assessed separately. |
| Native multivesicular body intraluminal vesicle UniProt verify check | passed | True | cellstructuremech:multivesicular_body_intraluminal_vesicle | Read-only native command returned zero. No protein examples or typed molecular nodes. Actual positive pathway assertions and justified physical-scope exclusions are assessed separately. |
| Native multivesicular body intraluminal vesicle UniProt causal check | passed | True | cellstructuremech:multivesicular_body_intraluminal_vesicle | Read-only native command returned zero. No protein examples or typed molecular nodes. Actual positive pathway assertions and justified physical-scope exclusions are assessed separately. |
| Native multivesicular body lumen UniProt verify check | passed | True | cellstructuremech:multivesicular_body_lumen | Read-only native command returned zero. No protein examples or typed molecular nodes. Actual positive pathway assertions and justified physical-scope exclusions are assessed separately. |
| Native multivesicular body lumen UniProt causal check | passed | True | cellstructuremech:multivesicular_body_lumen | Read-only native command returned zero. No protein examples or typed molecular nodes. Actual positive pathway assertions and justified physical-scope exclusions are assessed separately. |
| Native multivesicular body membrane UniProt verify check | passed | True | GO:0032585 | Read-only native command returned zero. No protein examples or typed molecular nodes. Actual positive pathway assertions and justified physical-scope exclusions are assessed separately. |
| Native multivesicular body membrane UniProt causal check | passed | True | GO:0032585 | Read-only native command returned zero. No protein examples or typed molecular nodes. Actual positive pathway assertions and justified physical-scope exclusions are assessed separately. |

## Scientific And Domain Assessments

### Original native schema/render and unchanged frozen input

schema: supported. Targets: cellstructuremech:mitosome_inner_membrane.

Original validate/render pass, Markdown exact and historical target hash matches current bytes. None of these four targets is stale. A schema pass is not a biological verdict.

### Exact compartment identity, synonyms and broader classes

identity: supported. Targets: cellstructuremech:mitosome_inner_membrane.

Exact SL0439 definition and both synonyms match; GO0031090 is a suitable broader organelle membrane, while envelope is part_of. Bounded GO search returns whole mitosome only; exact local identities are retained without guessing chemical identifiers.

### Taxon identities and qualitative occurrence

scope: supported. Targets: cellstructuremech:mitosome_inner_membrane.

Eukaryota2759 and Entamoeba histolytica5759 match native authority. Tovar primary abstract establishes the mitochondrial remnant by localization/targeting; later Mi-ichi purification/IF supports organelle occurrence in HM-1:IMSScl6. Roger review supports qualitative patchy low-oxygen eukaryotic context, not numeric prevalence or every-strain coverage.

### Specific original ultrastructure and distribution access limits

evidence: unknown. Targets: cellstructuremech:mitosome_inner_membrane.

Tovar1999 complete abstract does not independently verify the specifically attributed double-membrane observation; its body/pixels were not read. Tachezy2022 complete secondary abstract does not establish the full body as a broad mitosome-distribution source. These limits are not biological refutations; current exact location authority supports compartment topology.

### Collective material versus optional compartment inventory

grounding: supported. Targets: cellstructuremech:mitosome_inner_membrane.

One reviewed-label-only LIPID row denotes the constitutive bilayer material, with no whole-membrane CURIE falsely used as a lipid identity. ESSENTIAL describes the collective bilayer constitution of this membrane, not a specific lipid/protein knockout result. The explicit grounding TODO stays accurate without a forced chemical identifier.

### Individual formation requirements are not measured

evidence: unknown. Targets: cellstructuremech:mitosome_inner_membrane.

Native anatomy defines the collective bilayer, but does not establish individual lipid species, stoichiometry, species-specific chemistry or experimental depletion/reconstitution requirements. Collective material constitution is not extrapolated to individual molecular essentiality.

### Complete descriptive topology graph

graph: supported. Targets: cellstructuremech:mitosome_inner_membrane.

Three NONMECHANISTIC edges: inner membrane part_of envelope, encloses matrix and delimits IMS. Exact authority boundaries and frozen local identities agree. Graph exclusions explicitly withhold protein import/transport machinery; no assembly mechanism, complete molecular inventory or causal intervention is asserted.

### Actual native protein-check coverage

provenance: supported. Targets: cellstructuremech:mitosome_inner_membrane.

Both commands exit0. Independent inventory confirms zero protein examples, zero typed molecular nodes and zero UniProtKB graph xrefs. Generic success text is not used alone to infer inventory emptiness or scientific completeness.

### Genuine material/topology exclusion

scope: not_applicable. Targets: cellstructuremech:mitosome_inner_membrane.

Complete record asserts only collective lipid material or spatial topology and qualitative occurrence. No positive named molecular/pathway/stress/trait/transcriptomic claim triggers a molecular query; protein/import mechanisms are explicitly excluded. Original N/A outcome is justified by this full scope, with wording clarified beyond the expression-only shorthand. No bundle defect is manufactured. Fresh catalogue also lacks Entamoeba; that absence is not biological evidence and no unrelated-host query is made.

### Confirmed DOI-title mismatch

provenance: concern. Targets: cellstructuremech:mitosome_inner_membrane.

DOI12922 resolves to The hydrogenosome of Trichomonas vaginalis by Tachezy,Makki,Hrdy2022; the record gives a different title. Preserve exact original minor F1 under this maintained record, without claiming unread full text lacks mitosome coverage.

### No image or unrepresented molecular requirement

scope: not_applicable. Targets: cellstructuremech:mitosome_inner_membrane.

No maintained image/pixel or licence assertion, physical measurement, associated trait, verbatim evidence snippet, individual gene/protein identity or protein example occurs. Optional inventory absence is not a failure. No source pixels or raw microscopy are independently inspected.

### Historical edits and neighbor context

provenance: supported. Targets: cellstructuremech:mitosome_inner_membrane.

PROPOSED status and recorded historical boundary-grounding changes remain intact. Open lipid-identity discussion, where present, documents intentional label-only material. Whole/envelope neighbors are frozen boundary context only; their scientific issues are neither adopted nor resolved.

### Current scientific verdict

completeness: concern. Targets: cellstructuremech:mitosome_inner_membrane.

needs_curation because one exact inherited minor bibliographic finding remains; no confirmed new scientific defect. Exact source tiers, prevalence/primary-attribution limits, empty native coverage and genuine physical applicability exclusion remain explicit.

### Original native schema/render and unchanged frozen input

schema: supported. Targets: cellstructuremech:mitosome_intermembrane_space.

Original validate/render pass, Markdown exact and historical target hash matches current bytes. None of these four targets is stale. A schema pass is not a biological verdict.

### Exact compartment identity, synonyms and broader classes

identity: supported. Targets: cellstructuremech:mitosome_intermembrane_space.

Exact SL0440 definition and all three synonyms match; part_of envelope is distinct from is_a. Bounded GO search returns whole mitosome only; exact local identities are retained without guessing chemical identifiers.

### Taxon identities and qualitative occurrence

scope: supported. Targets: cellstructuremech:mitosome_intermembrane_space.

Eukaryota2759 and Entamoeba histolytica5759 match native authority. Tovar primary abstract establishes the mitochondrial remnant by localization/targeting; later Mi-ichi purification/IF supports organelle occurrence in HM-1:IMSScl6. Roger review supports qualitative patchy low-oxygen eukaryotic context, not numeric prevalence or every-strain coverage.

### Specific original ultrastructure and distribution access limits

evidence: unknown. Targets: cellstructuremech:mitosome_intermembrane_space.

Tovar1999 complete abstract does not independently verify the specifically attributed double-membrane observation; its body/pixels were not read. Tachezy2022 complete secondary abstract does not establish the full body as a broad mitosome-distribution source. These limits are not biological refutations; current exact location authority supports compartment topology.

### Collective material versus optional compartment inventory

completeness: supported. Targets: cellstructuremech:mitosome_intermembrane_space.

This spatial compartment has no molecular component inventory or ESSENTIAL material assertion. Empty optional molecular slots do not establish a defect; no sibling metabolism or protein machinery is imported into the record.

### Complete descriptive topology graph

graph: supported. Targets: cellstructuremech:mitosome_intermembrane_space.

Three NONMECHANISTIC edges: IMS part_of envelope, outer and inner membranes delimit it. Exact authority boundaries and frozen local identities agree. Graph exclusions explicitly withhold protein import/transport machinery; no assembly mechanism, complete molecular inventory or causal intervention is asserted.

### Actual native protein-check coverage

provenance: supported. Targets: cellstructuremech:mitosome_intermembrane_space.

Both commands exit0. Independent inventory confirms zero protein examples, zero typed molecular nodes and zero UniProtKB graph xrefs. Generic success text is not used alone to infer inventory emptiness or scientific completeness.

### Genuine material/topology exclusion

scope: not_applicable. Targets: cellstructuremech:mitosome_intermembrane_space.

Complete record asserts only collective lipid material or spatial topology and qualitative occurrence. No positive named molecular/pathway/stress/trait/transcriptomic claim triggers a molecular query; protein/import mechanisms are explicitly excluded. Original N/A outcome is justified by this full scope, with wording clarified beyond the expression-only shorthand. No bundle defect is manufactured. Fresh catalogue also lacks Entamoeba; that absence is not biological evidence and no unrelated-host query is made.

### Confirmed DOI-title mismatch

provenance: concern. Targets: cellstructuremech:mitosome_intermembrane_space.

DOI12922 resolves to The hydrogenosome of Trichomonas vaginalis by Tachezy,Makki,Hrdy2022; the record gives a different title. Preserve exact original minor F1 under this maintained record, without claiming unread full text lacks mitosome coverage.

### No image or unrepresented molecular requirement

scope: not_applicable. Targets: cellstructuremech:mitosome_intermembrane_space.

No maintained image/pixel or licence assertion, physical measurement, associated trait, verbatim evidence snippet, individual gene/protein identity or protein example occurs. Optional inventory absence is not a failure. No source pixels or raw microscopy are independently inspected.

### Historical edits and neighbor context

provenance: supported. Targets: cellstructuremech:mitosome_intermembrane_space.

PROPOSED status and recorded historical boundary-grounding changes remain intact. Open lipid-identity discussion, where present, documents intentional label-only material. Whole/envelope neighbors are frozen boundary context only; their scientific issues are neither adopted nor resolved.

### Current scientific verdict

completeness: concern. Targets: cellstructuremech:mitosome_intermembrane_space.

needs_curation because one exact inherited minor bibliographic finding remains; no confirmed new scientific defect. Exact source tiers, prevalence/primary-attribution limits, empty native coverage and genuine physical applicability exclusion remain explicit.

### Original native schema/render and unchanged frozen input

schema: supported. Targets: cellstructuremech:mitosome_matrix.

Original validate/render pass, Markdown exact and historical target hash matches current bytes. None of these four targets is stale. A schema pass is not a biological verdict.

### Exact compartment identity, synonyms and broader classes

identity: supported. Targets: cellstructuremech:mitosome_matrix.

Exact SL0441 definition/synonym match; GO0043233 is an appropriate organelle-lumen parent by its innermost-volume definition, with whole mitosome part_of. Bounded GO search returns whole mitosome only; exact local identities are retained without guessing chemical identifiers.

### Taxon identities and qualitative occurrence

scope: supported. Targets: cellstructuremech:mitosome_matrix.

Eukaryota2759 and Entamoeba histolytica5759 match native authority. Tovar primary abstract establishes the mitochondrial remnant by localization/targeting; later Mi-ichi purification/IF supports organelle occurrence in HM-1:IMSScl6. Roger review supports qualitative patchy low-oxygen eukaryotic context, not numeric prevalence or every-strain coverage.

### Specific original ultrastructure and distribution access limits

evidence: unknown. Targets: cellstructuremech:mitosome_matrix.

Tovar1999 complete abstract does not independently verify the specifically attributed double-membrane observation; its body/pixels were not read. Tachezy2022 complete secondary abstract does not establish the full body as a broad mitosome-distribution source. These limits are not biological refutations; current exact location authority supports compartment topology.

### Collective material versus optional compartment inventory

completeness: supported. Targets: cellstructuremech:mitosome_matrix.

This spatial compartment has no molecular component inventory or ESSENTIAL material assertion. Empty optional molecular slots do not establish a defect; no sibling metabolism or protein machinery is imported into the record.

### Complete descriptive topology graph

graph: supported. Targets: cellstructuremech:mitosome_matrix.

Two NONMECHANISTIC edges: matrix part_of mitosome and inner membrane encloses matrix. Exact authority boundaries and frozen local identities agree. Graph exclusions explicitly withhold protein import/transport machinery; no assembly mechanism, complete molecular inventory or causal intervention is asserted.

### Actual native protein-check coverage

provenance: supported. Targets: cellstructuremech:mitosome_matrix.

Both commands exit0. Independent inventory confirms zero protein examples, zero typed molecular nodes and zero UniProtKB graph xrefs. Generic success text is not used alone to infer inventory emptiness or scientific completeness.

### Genuine material/topology exclusion

scope: not_applicable. Targets: cellstructuremech:mitosome_matrix.

Complete record asserts only collective lipid material or spatial topology and qualitative occurrence. No positive named molecular/pathway/stress/trait/transcriptomic claim triggers a molecular query; protein/import mechanisms are explicitly excluded. Original N/A outcome is justified by this full scope, with wording clarified beyond the expression-only shorthand. No bundle defect is manufactured. Fresh catalogue also lacks Entamoeba; that absence is not biological evidence and no unrelated-host query is made.

### Confirmed DOI-title mismatch

provenance: concern. Targets: cellstructuremech:mitosome_matrix.

DOI12922 resolves to The hydrogenosome of Trichomonas vaginalis by Tachezy,Makki,Hrdy2022; the record gives a different title. Preserve exact original minor F1 under this maintained record, without claiming unread full text lacks mitosome coverage.

### No image or unrepresented molecular requirement

scope: not_applicable. Targets: cellstructuremech:mitosome_matrix.

No maintained image/pixel or licence assertion, physical measurement, associated trait, verbatim evidence snippet, individual gene/protein identity or protein example occurs. Optional inventory absence is not a failure. No source pixels or raw microscopy are independently inspected.

### Historical edits and neighbor context

provenance: supported. Targets: cellstructuremech:mitosome_matrix.

PROPOSED status and recorded historical boundary-grounding changes remain intact. Open lipid-identity discussion, where present, documents intentional label-only material. Whole/envelope neighbors are frozen boundary context only; their scientific issues are neither adopted nor resolved.

### Current scientific verdict

completeness: concern. Targets: cellstructuremech:mitosome_matrix.

needs_curation because one exact inherited minor bibliographic finding remains; no confirmed new scientific defect. Exact source tiers, prevalence/primary-attribution limits, empty native coverage and genuine physical applicability exclusion remain explicit.

### Original native schema/render and unchanged frozen input

schema: supported. Targets: cellstructuremech:mitosome_outer_membrane.

Original validate/render pass, Markdown exact and historical target hash matches current bytes. None of these four targets is stale. A schema pass is not a biological verdict.

### Exact compartment identity, synonyms and broader classes

identity: supported. Targets: cellstructuremech:mitosome_outer_membrane.

Exact SL0443 definition and both synonyms match; GO0031090 broader organelle membrane is distinct from envelope part_of. Bounded GO search returns whole mitosome only; exact local identities are retained without guessing chemical identifiers.

### Taxon identities and qualitative occurrence

scope: supported. Targets: cellstructuremech:mitosome_outer_membrane.

Eukaryota2759 and Entamoeba histolytica5759 match native authority. Tovar primary abstract establishes the mitochondrial remnant by localization/targeting; later Mi-ichi purification/IF supports organelle occurrence in HM-1:IMSScl6. Roger review supports qualitative patchy low-oxygen eukaryotic context, not numeric prevalence or every-strain coverage.

### Specific original ultrastructure and distribution access limits

evidence: unknown. Targets: cellstructuremech:mitosome_outer_membrane.

Tovar1999 complete abstract does not independently verify the specifically attributed double-membrane observation; its body/pixels were not read. Tachezy2022 complete secondary abstract does not establish the full body as a broad mitosome-distribution source. These limits are not biological refutations; current exact location authority supports compartment topology.

### Collective material versus optional compartment inventory

grounding: supported. Targets: cellstructuremech:mitosome_outer_membrane.

One reviewed-label-only LIPID row denotes the constitutive bilayer material, with no whole-membrane CURIE falsely used as a lipid identity. ESSENTIAL describes the collective bilayer constitution of this membrane, not a specific lipid/protein knockout result. The explicit grounding TODO stays accurate without a forced chemical identifier.

### Individual formation requirements are not measured

evidence: unknown. Targets: cellstructuremech:mitosome_outer_membrane.

Native anatomy defines the collective bilayer, but does not establish individual lipid species, stoichiometry, species-specific chemistry or experimental depletion/reconstitution requirements. Collective material constitution is not extrapolated to individual molecular essentiality.

### Complete descriptive topology graph

graph: supported. Targets: cellstructuremech:mitosome_outer_membrane.

Three NONMECHANISTIC edges: outer membrane part_of envelope, faces cytoplasm and bounds IMS. Exact authority boundaries and frozen local identities agree. Graph exclusions explicitly withhold protein import/transport machinery; no assembly mechanism, complete molecular inventory or causal intervention is asserted.

### Actual native protein-check coverage

provenance: supported. Targets: cellstructuremech:mitosome_outer_membrane.

Both commands exit0. Independent inventory confirms zero protein examples, zero typed molecular nodes and zero UniProtKB graph xrefs. Generic success text is not used alone to infer inventory emptiness or scientific completeness.

### Genuine material/topology exclusion

scope: not_applicable. Targets: cellstructuremech:mitosome_outer_membrane.

Complete record asserts only collective lipid material or spatial topology and qualitative occurrence. No positive named molecular/pathway/stress/trait/transcriptomic claim triggers a molecular query; protein/import mechanisms are explicitly excluded. Original N/A outcome is justified by this full scope, with wording clarified beyond the expression-only shorthand. No bundle defect is manufactured. Fresh catalogue also lacks Entamoeba; that absence is not biological evidence and no unrelated-host query is made.

### Confirmed DOI-title mismatch

provenance: concern. Targets: cellstructuremech:mitosome_outer_membrane.

DOI12922 resolves to The hydrogenosome of Trichomonas vaginalis by Tachezy,Makki,Hrdy2022; the record gives a different title. Preserve exact original minor F1 under this maintained record, without claiming unread full text lacks mitosome coverage.

### No image or unrepresented molecular requirement

scope: not_applicable. Targets: cellstructuremech:mitosome_outer_membrane.

No maintained image/pixel or licence assertion, physical measurement, associated trait, verbatim evidence snippet, individual gene/protein identity or protein example occurs. Optional inventory absence is not a failure. No source pixels or raw microscopy are independently inspected.

### Historical edits and neighbor context

provenance: supported. Targets: cellstructuremech:mitosome_outer_membrane.

PROPOSED status and recorded historical boundary-grounding changes remain intact. Open lipid-identity discussion, where present, documents intentional label-only material. Whole/envelope neighbors are frozen boundary context only; their scientific issues are neither adopted nor resolved.

### Current scientific verdict

completeness: concern. Targets: cellstructuremech:mitosome_outer_membrane.

needs_curation because one exact inherited minor bibliographic finding remains; no confirmed new scientific defect. Exact source tiers, prevalence/primary-attribution limits, empty native coverage and genuine physical applicability exclusion remain explicit.

### Native inventory and actual coverage

schema: supported. Targets: GO:0070074.

One UNREVIEWED A8IWX2 example and one COVERED typed node. Native accession/field checks pass; they do not certify literature-symbol equivalence, localization or necessity.

### Historical source and exact rendering

schema: supported. Targets: GO:0070074.

Original native validate/render passes with14 matching frozen historical inputs. Current record bytes unchanged and PROPOSED status retained. No maintained image or quantitative property requires a pixel audit; no optional missing inventory finding invented.

### Molecular claims trigger bounded applicability assessment

evidence: supported. Targets: GO:0070074.

PfROM1/Rom1 localization and secretory redistribution are positive claims triggering native structured-source assessment. Original explicit expression-only exemption is inadequate. Fresh catalogue has no exact represented eukaryotic host; no downstream module query or negative biology conclusion. Historical runner failure remains historical.

### Native inventory and actual coverage

schema: supported. Targets: GO:0036000.

Six UNREVIEWED examples and three COVERED typed nodes; the MDD node is reported COVERED through I7M6L0, despite its independently confirmed wrong MDL1 attribution. Native accession/field checks pass; they do not certify literature-symbol equivalence, localization or necessity.

### Historical source and exact rendering

schema: supported. Targets: GO:0036000.

Original native validate/render passes with14 matching frozen historical inputs. Current record bytes unchanged and PROPOSED status retained. No maintained image or quantitative property requires a pixel audit; no optional missing inventory finding invented.

### Molecular claims trigger bounded applicability assessment

evidence: supported. Targets: GO:0036000.

GRL/GRT/MDL1/MDD and regulated exocytosis are positive claims triggering native structured-source assessment. Original explicit expression-only exemption is inadequate. Fresh catalogue has no exact represented eukaryotic host; no downstream module query or negative biology conclusion. Historical runner failure remains historical.

### Exact mononeme identity and apical anatomy

identity: supported. Targets: GO:0070074.

GO0070074 definition and direct apical-complex parthood agree;0043231 is the is_a parent. Micronemes, rhoptries and dense granules remain distinct comparator organelles.

### Mature-segmenter and release-stage limits

scope: supported. Targets: GO:0070074.

Species5833 and canonical P.falciparum agree. Primary experiments used tagged full-length PfROM1 in3D7; mature-segmenter discrete localization is separated from earlier schizonts and surface redistribution after release. No claim that a persistent separate mononeme is demonstrated in released merozoites.

### PfROM1 versus native Rom1 identity

grounding: supported. Targets: GO:0070074.

Native A8IWX2 is UNREVIEWED Rom1/Rhomboid-like protease,278aa,matching primary full-length PfROM1 sequence scope. Protein example is identity-only; primary microscopy supplies localization. Broad rhomboid family/domain hits do not establish an exact component family or necessity.

### Localized constituent and unknown formation necessity

evidence: supported. Targets: GO:0070074.

PfROM1 association with the assayed compartment is supported; UNKNOWN formation necessity is retained. Neither broad protease annotation nor prior heterologous cleavage evidence proves mononeme formation, a universal invasion requirement or endogenous substrate cleavage in this compartment.

### Six descriptive localization and redistribution edges

graph: supported. Targets: GO:0070074.

NONMECHANISTIC graph preserves association near subpellicular microtubules, separate marker compartments and post-release surface redistribution. Confocal proximity does not assert motor-mediated transport, physical binding, membrane fusion route or causal proteolysis.

### Primary body and access tier

provenance: supported. Targets: GO:0070074.

Singh title/DOI and genuine full HTML body inspected as specified; S3 guessed path404 was bypassed with a genuine matching PMC body. Main captions read but pixels and movies were not inspected. No image-copy or license claim appears in the maintained record.

### Existing stage corrections and optional completeness

consistency: supported. Targets: GO:0070074.

Present history/discussion limits are assessed as current content. Earlier issue1281/1282 mentions do not create a new terminal disposition of unfrozen predecessors; unresolved membrane/lumen/cargo/motor slots do not mandate invented structure or protein identities.

### Qualified mononeme support

evidence: unknown. Targets: GO:0070074.

Tagged localization is not an untagged endogenous atlas, electron-tomographic organelle census, causal transport mechanism or invasion knockout. No figure pixels, supplementary movies or modern all-stage prevalence survey assessed.

### Exact mucocyst secretory-granule identity

identity: supported. Targets: GO:0036000.

GO0036000 literal definition and secretory granule ancestor0030141 agree. Whole organelle, boundary membrane and lumen are distinct descriptive entities; no broader cellular component is adopted as exact identity.

### Tetrahymena species and strain boundaries

scope: supported. Targets: GO:0036000.

Native examples distinguish species5911 from SB210312017. Primary papers use stated laboratory wild-type/mutant/tagged strains and conditions, not a blanket SB210 experimental identity. COMMON is qualitative occurrence, not measured prevalence.

### Collective membrane and optional exact grounding

grounding: supported. Targets: GO:0036000.

Label-only collective bilayer constituent is a defensible membrane-bounded organelle building material. ESSENTIAL applies to the collective boundary, not every lipid species. No actual erroneous whole-membrane GO chemical grounding appears; unresolved exact lipid/complex grounding alone is not a finding.

### GRL cargo, lattice and representative identities

evidence: supported. Targets: GO:0036000.

P90618/O76218/O76219 match GRL1/3/4, all unreviewed. Primary work supports lattice cargo/coassembly, with proprotein processing and context-dependent associations. Domain hits for two examples do not ground the whole cohort; inconclusive GRL1 InterPro retrieval is not absence evidence. UNKNOWN formation necessity is not replaced by a universal claim.

### GRT identities and independent sorting scope

evidence: supported. Targets: GO:0036000.

Q3S4V5/Q2I2L7 match unreviewed GRT1/2; native gamma-crystallin-like context is broad. Primary sorting/biochemistry supports distinct cargo pathways under tested conditions; GRT double knockout retains gross core/secretion with subtler adhesion phenotype. No assertion that every interaction is absent in wild-type/TGN conditions or that family members are universally dispensable.

### Inherited wrong MDL1 concrete example

grounding: concern. Targets: GO:0036000.

I7M6L0 is TTHERM_00471830,392aa,PSMD4/S5A/Rpn10-family; the primary paper names MDL1 as TTHERM_00658810,346aa,which maps to distinct I7MM25. Maintained role/evidence notes assert the wrong literature-gene equivalence. Native correspondence success does not remove inherited major mucocyst-1.

### Putative MDD assembly and docking/discharge role

evidence: supported. Targets: GO:0036000.

Primary functional tagged Mdl1 polarizes before docking; deletion impairs docking/discharge despite mature crystal formation. Other associated subunits and biochemical/negative-stain data support putative MDD machinery. Unknown exact assembly and direct fusion mechanism remain limited. Mdl1 phenotype is not automatically necessity of every complex member or formation of the organelle.

### Seven nonmechanistic organization edges

graph: supported. Targets: GO:0036000.

Membrane boundary, lumen parthood, GRL crystal organization, GRT sorting, tip-associated MDD and secretion support descriptive scope. Exact Mdl1 localization supports the tip-associated machinery abstraction without claiming every associated subunit independently resolved at the tip. Component protein example remains the inherited identity defect. Complex-as-GENE_OR_PROTEIN is allowed natively.

### Biogenesis factors versus optional mature inventory

consistency: supported. Targets: GO:0036000.

Kontur supports Mma1 maturation role without significant mature localization in tested induced fusion. Kaur does show induced Stx7l1-GFP at mature and immature mucocysts; present conditional inventory notes do not deny this or require every supported protein added. Localization does not itself establish exocytic fusion necessity. No new optional-inventory or mandatory-enum finding.

### Primary experimental tiers and metadata

provenance: supported. Targets: GO:0036000.

Four independent mucocyst primary bodies were read in declared sections. Rahaman HTML matches DOI/title despite failed guessed S3 route; other three are genuine JATS. Kuppannan complex microscopy is negative-stain TEM, not cryoET. Main captions inspected only where declared; no actual figure pixels/supplements/raw proteomics audited.

### Exact inherited repair and scope

consistency: concern. Targets: GO:0036000.

Retain F1/A1 predecessor identity. Separately authorized curation should remove or replace the wrong example and attribution, verify paper locus plus native candidate identity/status/strain, and cite primary MDL1 membership. Do not replace entire MDD complex identity with one subunit or treat accession validation alone as scientific repair.

### Qualified scientific scope outside the confirmed finding

evidence: unknown. Targets: GO:0036000.

No exhaustive mature-protein inventory, raw mass-spectrometric reanalysis, exact MDD stoichiometry/assembly or direct membrane-fusion mechanism. Predicted helices/lipidation and broad family domains are not experimentally established necessities. P90618 InterPro retrieval and Q2I2L7 mapping remain inconclusive/unavailable.

### Exact entity, synonyms and boundaries

identity: supported. Targets: GO:0005771.

ActiveGO0005771 exactly matches whole-MVB definition. Typed GO relation and SL0174 support late-endosome ancestry; maintained membrane/lumen/ILV has_part boundaries distinguish three valid subentities. Existing local sibling links resolve uniquely despite their separately owned GO-first findings.

### Constituent material versus assembly machinery

grounding: supported. Targets: GO:0005771.

No molecular component inventory asserted; ESCRT machinery remains external assembly actors, not stable mature MVB constituents.

### Every coarse directed edge

graph: supported. Targets: GO:0005771.

All five NONMECHANISTIC edges checked: ESCRT-I sorting is supported by primary2001 abstract; ESCRT-II recruitment by direct Teo2004 purified Vps25/Vps20 and enhanced liposome association; ESCRT-III remodeling by primary2002 recruitment/sorting plus GO and secondary context; inward budding and ILV containment by defining ontology topology. No complete sequential scission mechanism or direct in-vivo reconstitution is asserted.

### Sorting and degradation destination

scope: supported. Targets: GO:0005771.

GO0071985 and inspected primary abstracts support ubiquitination as a cargo-sorting signal and ESCRT-associated entry into MVB vesicles; Henne secondary abstract supports vacuolar/lysosomal delivery. These are bounded yeast sorting assertions, not a universal claim that every ILV in every organism uses one obligatory mechanism.

### Budding-yeast experimental versus expression-host scope

scope: supported. Targets: GO:0005771.

Tax4932 confirms species. Primary abstracts and Teo S.cerevisiae source genes support qualitative yeast model/COMMON context, not a quantified prevalence census. Teo bacterial recombinant expression hosts and bovine-brain liposomes are assay materials, not organism exemplars for MVB identity.

### Original provenance and empty native protein coverage

schema: supported. Targets: GO:0005771.

All original hashes match retained source and target remains unchanged. Four original pairs validate/render exactly. Current verify/causal exit0, zero examples and zero GENE_OR_PROTEIN nodes; ESCRT STRUCTURE/GO identities were independently inspected. Generic success text is not populated protein verification.

### Present expression-only exclusion is unsupported

provenance: concern. Targets: GO:0005771.

Original imodulondb check exists; no omission. Positive ESCRT-dependent MVB sorting claims in functions/examples/graph require actual structured-source host applicability assessment even without transcriptomics claims. Lumen pathway statements remain positive assertions despite empty inventory.

### Fresh bounded catalogue host coverage

evidence: not_applicable. Targets: GO:0005771.

Actual official catalogue contains no matching Saccharomyces dataset. No downstream module search or summary is required for an unmatched host. Historical runner00:49Z limit and fresh successful catalogue fallback are distinct; no noncoverage-as-refutation or E.coli expression-host proxy.

### Exact access tiers and restricted inference

evidence: supported. Targets: GO:0005771.

Fresh primary2001/2002 complete abstracts and fresh secondaryHenne2011 abstract inspected. Exact DOI routes return redirect-only200, publisher routes403. Teo genuine primary PDF read p559/pp564-567 only; no image pixels, uninspected structural sections or supplements certified.

### Whole record and optional fields

completeness: supported. Targets: GO:0005771.

Complete maintained record read: identity/history, all claims/evidence, discussions, graph boundaries and status. No image, physical-number, verbatim snippet, trait or accession-bearing protein claim occurs. No optional lipid species, stoichiometry, full ESCRT inventory or category-wide disposition invented. PROPOSED and histories remain unchanged.

### Exact entity, synonyms and boundaries

identity: concern. Targets: cellstructuremech:multivesicular_body_intraluminal_vesicle.

Maintained internal membrane-bounded vesicle matches activeGO0097487 exactly, not broader vesicle0031982 or wholeMVB. GO definition, is_a-only ancestry and typed MVB part_of all agree. Local identifier is valid but misses required exact GO-first identity; preserve inherited majorF1 and identifier-preserving migration.

### Constituent material versus assembly machinery

grounding: supported. Targets: cellstructuremech:multivesicular_body_intraluminal_vesicle.

Collective lipid bilayer uses REVIEWED_LABEL_ONLY without a whole-membrane GO molecular grounding. ESCRT-III is assembly machinery, not forced into mature-vesicle or membrane components. Optional molecular lipid mapping TODO remains candid.

### Every coarse directed edge

graph: supported. Targets: cellstructuremech:multivesicular_body_intraluminal_vesicle.

All four NONMECHANISTIC edges checked: ESCRT-III acts on limiting membrane, limiting membrane buds inward, ILV is contained in the outerMVB lumen, limiting membrane bounds wholeMVB. The last actor is correctly the limiting membrane, not the ILV bilayer. Cargo reception describes sorting, not permanent ubiquitin retention on every completed vesicle.

### Sorting and degradation destination

scope: supported. Targets: cellstructuremech:multivesicular_body_intraluminal_vesicle.

GO0071985 and inspected primary abstracts support ubiquitination as a cargo-sorting signal and ESCRT-associated entry into MVB vesicles; Henne secondary abstract supports vacuolar/lysosomal delivery. These are bounded yeast sorting assertions, not a universal claim that every ILV in every organism uses one obligatory mechanism.

### Budding-yeast experimental versus expression-host scope

scope: supported. Targets: cellstructuremech:multivesicular_body_intraluminal_vesicle.

Tax4932 confirms species. Primary abstracts and Teo S.cerevisiae source genes support qualitative yeast model/COMMON context, not a quantified prevalence census. Teo bacterial recombinant expression hosts and bovine-brain liposomes are assay materials, not organism exemplars for MVB identity.

### Original provenance and empty native protein coverage

schema: supported. Targets: cellstructuremech:multivesicular_body_intraluminal_vesicle.

All original hashes match retained source and target remains unchanged. Four original pairs validate/render exactly. Current verify/causal exit0, zero examples and zero GENE_OR_PROTEIN nodes; ESCRT STRUCTURE/GO identities were independently inspected. Generic success text is not populated protein verification.

### Present expression-only exclusion is unsupported

provenance: concern. Targets: cellstructuremech:multivesicular_body_intraluminal_vesicle.

Original imodulondb check exists; no omission. Positive ESCRT-dependent MVB sorting claims in functions/examples/graph require actual structured-source host applicability assessment even without transcriptomics claims. Lumen pathway statements remain positive assertions despite empty inventory.

### Fresh bounded catalogue host coverage

evidence: not_applicable. Targets: cellstructuremech:multivesicular_body_intraluminal_vesicle.

Actual official catalogue contains no matching Saccharomyces dataset. No downstream module search or summary is required for an unmatched host. Historical runner00:49Z limit and fresh successful catalogue fallback are distinct; no noncoverage-as-refutation or E.coli expression-host proxy.

### Exact access tiers and restricted inference

evidence: supported. Targets: cellstructuremech:multivesicular_body_intraluminal_vesicle.

Fresh primary2001/2002 complete abstracts and fresh secondaryHenne2011 abstract inspected. Exact DOI routes return redirect-only200, publisher routes403. Teo genuine primary PDF read p559/pp564-567 only; no image pixels, uninspected structural sections or supplements certified.

### Whole record and optional fields

completeness: supported. Targets: cellstructuremech:multivesicular_body_intraluminal_vesicle.

Complete maintained record read: identity/history, all claims/evidence, discussions, graph boundaries and status. No image, physical-number, verbatim snippet, trait or accession-bearing protein claim occurs. No optional lipid species, stoichiometry, full ESCRT inventory or category-wide disposition invented. PROPOSED and histories remain unchanged.

### Constitutive bilayer versus molecular necessity

evidence: unknown. Targets: cellstructuremech:multivesicular_body_intraluminal_vesicle.

ESSENTIAL collective bilayer material is definitional for a membrane-bounded structure; it does not establish that an individual lipid species, ESCRT subunit or complete source-independent composition is required for formation. Inspected assay lipids are not the composition of the maintained yeast structure.

### Exact entity, synonyms and boundaries

identity: concern. Targets: cellstructuremech:multivesicular_body_lumen.

Outer-MVB lumen matches activeGO0097486 exactly, not the interior of one internal vesicle. SL0340 confirms all five maintained synonyms and endosome-lumen/MVB relations. Local identity remains valid but misses required exact GO identity; preserve inherited majorF1 with no destructive renaming.

### Constituent material versus assembly machinery

grounding: supported. Targets: cellstructuremech:multivesicular_body_lumen.

No molecular components or necessity asserted for this spatial lumen; membrane is boundary and ILVs are contents.

### Every coarse directed edge

graph: supported. Targets: cellstructuremech:multivesicular_body_lumen.

All four NONMECHANISTIC edges retain lumen isA endosome lumen, lumen partOf MVB, membrane bounds lumen, and ILV contained in lumen. Sorting function concerns destination of vesicles/cargo rather than autonomous catalysis by a volume.

### Sorting and degradation destination

scope: supported. Targets: cellstructuremech:multivesicular_body_lumen.

GO0071985 and inspected primary abstracts support ubiquitination as a cargo-sorting signal and ESCRT-associated entry into MVB vesicles; Henne secondary abstract supports vacuolar/lysosomal delivery. These are bounded yeast sorting assertions, not a universal claim that every ILV in every organism uses one obligatory mechanism.

### Budding-yeast experimental versus expression-host scope

scope: supported. Targets: cellstructuremech:multivesicular_body_lumen.

Tax4932 confirms species. Primary abstracts and Teo S.cerevisiae source genes support qualitative yeast model/COMMON context, not a quantified prevalence census. Teo bacterial recombinant expression hosts and bovine-brain liposomes are assay materials, not organism exemplars for MVB identity.

### Original provenance and empty native protein coverage

schema: supported. Targets: cellstructuremech:multivesicular_body_lumen.

All original hashes match retained source and target remains unchanged. Four original pairs validate/render exactly. Current verify/causal exit0, zero examples and zero GENE_OR_PROTEIN nodes; ESCRT STRUCTURE/GO identities were independently inspected. Generic success text is not populated protein verification.

### Present expression-only exclusion is unsupported

provenance: concern. Targets: cellstructuremech:multivesicular_body_lumen.

Original imodulondb check exists; no omission. Positive ESCRT-dependent MVB sorting claims in functions/examples/graph require actual structured-source host applicability assessment even without transcriptomics claims. Lumen pathway statements remain positive assertions despite empty inventory.

### Fresh bounded catalogue host coverage

evidence: not_applicable. Targets: cellstructuremech:multivesicular_body_lumen.

Actual official catalogue contains no matching Saccharomyces dataset. No downstream module search or summary is required for an unmatched host. Historical runner00:49Z limit and fresh successful catalogue fallback are distinct; no noncoverage-as-refutation or E.coli expression-host proxy.

### Exact access tiers and restricted inference

evidence: supported. Targets: cellstructuremech:multivesicular_body_lumen.

Fresh primary2001/2002 complete abstracts and fresh secondaryHenne2011 abstract inspected. Exact DOI routes return redirect-only200, publisher routes403. Teo genuine primary PDF read p559/pp564-567 only; no image pixels, uninspected structural sections or supplements certified.

### Whole record and optional fields

completeness: supported. Targets: cellstructuremech:multivesicular_body_lumen.

Complete maintained record read: identity/history, all claims/evidence, discussions, graph boundaries and status. No image, physical-number, verbatim snippet, trait or accession-bearing protein claim occurs. No optional lipid species, stoichiometry, full ESCRT inventory or category-wide disposition invented. PROPOSED and histories remain unchanged.

### Exact entity, synonyms and boundaries

identity: supported. Targets: GO:0032585.

GO0032585 exactly denotes the outer limiting MVB membrane. SL0175 confirms all five synonyms, endosome-membrane isA and wholeMVB partOf. This record is not every internal-vesicle membrane.

### Constituent material versus assembly machinery

grounding: supported. Targets: GO:0032585.

Collective lipid bilayer uses REVIEWED_LABEL_ONLY without a whole-membrane GO molecular grounding. ESCRT-III is assembly machinery, not forced into mature-vesicle or membrane components. Optional molecular lipid mapping TODO remains candid.

### Every coarse directed edge

graph: supported. Targets: GO:0032585.

All five NONMECHANISTIC edges retain membrane isA endosome membrane, membrane partOf MVB, ESCRT-III remodeling, inward ILV budding and ILV containment. Graph component_ref connects label-only constituent material; it does not assert a whole-membrane GO as a chemical molecular grounding.

### Sorting and degradation destination

scope: supported. Targets: GO:0032585.

GO0071985 and inspected primary abstracts support ubiquitination as a cargo-sorting signal and ESCRT-associated entry into MVB vesicles; Henne secondary abstract supports vacuolar/lysosomal delivery. These are bounded yeast sorting assertions, not a universal claim that every ILV in every organism uses one obligatory mechanism.

### Budding-yeast experimental versus expression-host scope

scope: supported. Targets: GO:0032585.

Tax4932 confirms species. Primary abstracts and Teo S.cerevisiae source genes support qualitative yeast model/COMMON context, not a quantified prevalence census. Teo bacterial recombinant expression hosts and bovine-brain liposomes are assay materials, not organism exemplars for MVB identity.

### Original provenance and empty native protein coverage

schema: supported. Targets: GO:0032585.

All original hashes match retained source and target remains unchanged. Four original pairs validate/render exactly. Current verify/causal exit0, zero examples and zero GENE_OR_PROTEIN nodes; ESCRT STRUCTURE/GO identities were independently inspected. Generic success text is not populated protein verification.

### Present expression-only exclusion is unsupported

provenance: concern. Targets: GO:0032585.

Original imodulondb check exists; no omission. Positive ESCRT-dependent MVB sorting claims in functions/examples/graph require actual structured-source host applicability assessment even without transcriptomics claims. Lumen pathway statements remain positive assertions despite empty inventory.

### Fresh bounded catalogue host coverage

evidence: not_applicable. Targets: GO:0032585.

Actual official catalogue contains no matching Saccharomyces dataset. No downstream module search or summary is required for an unmatched host. Historical runner00:49Z limit and fresh successful catalogue fallback are distinct; no noncoverage-as-refutation or E.coli expression-host proxy.

### Exact access tiers and restricted inference

evidence: supported. Targets: GO:0032585.

Fresh primary2001/2002 complete abstracts and fresh secondaryHenne2011 abstract inspected. Exact DOI routes return redirect-only200, publisher routes403. Teo genuine primary PDF read p559/pp564-567 only; no image pixels, uninspected structural sections or supplements certified.

### Whole record and optional fields

completeness: supported. Targets: GO:0032585.

Complete maintained record read: identity/history, all claims/evidence, discussions, graph boundaries and status. No image, physical-number, verbatim snippet, trait or accession-bearing protein claim occurs. No optional lipid species, stoichiometry, full ESCRT inventory or category-wide disposition invented. PROPOSED and histories remain unchanged.

### Constitutive bilayer versus molecular necessity

evidence: unknown. Targets: GO:0032585.

ESSENTIAL collective bilayer material is definitional for a membrane-bounded structure; it does not establish that an individual lipid species, ESCRT subunit or complete source-independent composition is required for formation. Inspected assay lipids are not the composition of the maintained yeast structure.

### Complete frozen-input comparison and bounded refresh

provenance: supported. Targets: cellstructuremech:mitosome_inner_membrane, cellstructuremech:mitosome_intermembrane_space, cellstructuremech:mitosome_matrix, cellstructuremech:mitosome_outer_membrane, GO:0070074, GO:0036000, GO:0005771, cellstructuremech:multivesicular_body_intraluminal_vesicle, cellstructuremech:multivesicular_body_lumen, GO:0032585.

0 of ten original target hashes differ from current main. The changed content is substantively reassessed in the target-specific assessments; original observations remain historical and unchanged. All current target and used context bytes are frozen.

## Findings

### septin-mitosome_inner_membrane-F1: Correct the title attached to DOI10.1111/jeu.12922

minor / open / confirmed; issue key: mitosome-inner-membrane-tachezy-title.

The evidence note calls this article Hydrogenosomes and mitosomes: Mitochondria of anaerobic eukaryotes. Exact native metadata identifies The hydrogenosome of Trichomonas vaginalis by Tachezy, Makki and Hrdy (2022). The DOI is valid; its unread full body is not presumed to lack a mitosome passage.

### septin-mitosome_intermembrane_space-F1: Correct the title attached to DOI10.1111/jeu.12922

minor / open / confirmed; issue key: mitosome-intermembrane-space-tachezy-title.

The evidence note calls this article Hydrogenosomes and mitosomes: Mitochondria of anaerobic eukaryotes. Exact native metadata identifies The hydrogenosome of Trichomonas vaginalis by Tachezy, Makki and Hrdy (2022). The DOI is valid; its unread full body is not presumed to lack a mitosome passage.

### septin-mitosome_matrix-F1: Correct the title attached to DOI10.1111/jeu.12922

minor / open / confirmed; issue key: mitosome-matrix-tachezy-title.

The evidence note calls this article Hydrogenosomes and mitosomes: Mitochondria of anaerobic eukaryotes. Exact native metadata identifies The hydrogenosome of Trichomonas vaginalis by Tachezy, Makki and Hrdy (2022). The DOI is valid; its unread full body is not presumed to lack a mitosome passage.

### septin-mitosome_outer_membrane-F1: Correct the title attached to DOI10.1111/jeu.12922

minor / open / confirmed; issue key: mitosome-outer-membrane-tachezy-title.

The evidence note calls this article Hydrogenosomes and mitosomes: Mitochondria of anaerobic eukaryotes. Exact native metadata identifies The hydrogenosome of Trichomonas vaginalis by Tachezy, Makki and Hrdy (2022). The DOI is valid; its unread full body is not presumed to lack a mitosome passage.

### plaque-t5-F1: Correct the MDL1 protein example

major / open / confirmed; issue key: mucocyst-1.

The MDD component names MDL1 but its protein example I7M6L0 carries TTHERM_00471830. Kuppannan explicitly names MDL1 as TTHERM_00658810,346aa; native UniProt resolves that locus to I7MM25. I7M6L0 is392aa and matches the S5A/Rpn10 proteasome family. Its role and evidence notes incorrectly assert a literature-gene equivalence despite passing native field correspondence.

### micro-F1: Reconcile the local identity with exact native GO:0097487

major / open / confirmed; issue key: multivesicular-body-intraluminal-vesicle-unused-exact-go-identity.

The maintained local identifier denotes the same biological entity as active GO:0097487. The candidate definition, ancestry and MVB parthood match; this is not a broader or merely label-similar term. An ignored-inclusive corpus search finds no existing use of the exact GO term. The record therefore misses the repository-required exact GO identity, while its biological boundary remains correct.

### micro-F2: Reconcile the local identity with exact native GO:0097486

major / open / confirmed; issue key: multivesicular-body-lumen-unused-exact-go-identity.

The maintained local identifier denotes the same biological entity as active GO:0097486. The candidate definition, ancestry and MVB parthood match; this is not a broader or merely label-similar term. An ignored-inclusive corpus search finds no existing use of the exact GO term. The record therefore misses the repository-required exact GO identity, while its biological boundary remains correct.

## Recommended Actions And Acceptance Checks

### septin-mitosome_inner_membrane-A1

Correct the bibliographic title/authorship for the retained DOI. Independently verify or replace its use for broad mitosome distribution without claiming unread full text proves absence.

- Confirm the retained DOI/title/author identity against native metadata.
- Run focused schema, strict and graph checks after separately authorized curation.

### septin-mitosome_intermembrane_space-A1

Correct the bibliographic title/authorship for the retained DOI. Independently verify or replace its use for broad mitosome distribution without claiming unread full text proves absence.

- Confirm the retained DOI/title/author identity against native metadata.
- Run focused schema, strict and graph checks after separately authorized curation.

### septin-mitosome_matrix-A1

Correct the bibliographic title/authorship for the retained DOI. Independently verify or replace its use for broad mitosome distribution without claiming unread full text proves absence.

- Confirm the retained DOI/title/author identity against native metadata.
- Run focused schema, strict and graph checks after separately authorized curation.

### septin-mitosome_outer_membrane-A1

Correct the bibliographic title/authorship for the retained DOI. Independently verify or replace its use for broad mitosome distribution without claiming unread full text proves absence.

- Confirm the retained DOI/title/author identity against native metadata.
- Run focused schema, strict and graph checks after separately authorized curation.

### plaque-t5-A1

Replace or remove the wrong protein example and its MDL1 attribution. If using the exact-locus I7MM25 candidate, retain its verified UNREVIEWED status, SB210 taxon, native protein name and locus; cite the primary paper for the MDL1 mapping and membership. Do not replace the complete MDD complex identity with one subunit.

- Verify exact paper locus, native identity and claim-specific source scope.
- After separately authorized curation, run focused schema/strict and native protein verification; native success alone does not validate literature-symbol attribution.

### micro-A1

In separately authorized curation, reconcile the entity with GO:0097487 using the documented identifier-preserving supersession process: retain the old local record as DEPRECATED and create or adopt the exact-GO successor with replaces. Coordinate references and evidence to the successor without silently reusing or renaming the old identifier. Preserve the verified lumen/vesicle boundary, species scope and optional lipid mapping limits.

- The adopted GO definition still exactly matches the maintained biological entity; no broader class is substituted.
- The old local identifier remains recoverable and the successor records replaces according to the curation contract.
- Ignored-inclusive corpus reference checks and native schema/strict/history/product/identifier gates pass after any separately authorized migration.

### micro-A2

In separately authorized curation, reconcile the entity with GO:0097486 using the documented identifier-preserving supersession process: retain the old local record as DEPRECATED and create or adopt the exact-GO successor with replaces. Coordinate references and evidence to the successor without silently reusing or renaming the old identifier. Preserve the verified lumen/vesicle boundary, species scope and optional lipid mapping limits.

- The adopted GO definition still exactly matches the maintained biological entity; no broader class is substituted.
- The old local identifier remains recoverable and the successor records replaces according to the curation contract.
- Ignored-inclusive corpus reference checks and native schema/strict/history/product/identifier gates pass after any separately authorized migration.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| current-record-0 | data/structures/membrane_organelle/mitosome_inner_membrane.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 758c67ff3788eef18a08b4b6720e1c3a96f135d4313cb3dc7777823599f6eb35; current SHA256 758c67ff3788eef18a08b4b6720e1c3a96f135d4313cb3dc7777823599f6eb35. Record bytes unchanged since the original review. |
| original-review-0 | reviews/structured/20261022T024026Z-mitosome-inner-membrane-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-1 | data/structures/membrane_organelle/mitosome_intermembrane_space.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 c961b013182d3ac6fb50a2fe4af7988c95d957237c78e904142cbb7e2f88df95; current SHA256 c961b013182d3ac6fb50a2fe4af7988c95d957237c78e904142cbb7e2f88df95. Record bytes unchanged since the original review. |
| original-review-1 | reviews/structured/20261022T024027Z-mitosome-intermembrane-space-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-2 | data/structures/membrane_organelle/mitosome_matrix.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 cc21e220c39e8210a84b7d15251fcb85474ec75f85eafab74c8df1d4a80c3bca; current SHA256 cc21e220c39e8210a84b7d15251fcb85474ec75f85eafab74c8df1d4a80c3bca. Record bytes unchanged since the original review. |
| original-review-2 | reviews/structured/20261022T024029Z-mitosome-matrix-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-3 | data/structures/membrane_organelle/mitosome_outer_membrane.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 8c9ed412d5d033717ea703db6c61c6960078608448a4cc6a57743a0ed37b7a58; current SHA256 8c9ed412d5d033717ea703db6c61c6960078608448a4cc6a57743a0ed37b7a58. Record bytes unchanged since the original review. |
| original-review-3 | reviews/structured/20261022T024030Z-mitosome-outer-membrane-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-4 | data/structures/membrane_organelle/mononeme.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 5e08d2090388a00b0883dd2253e8bd606d8c250a32406fb8492d6896c861a97b; current SHA256 5e08d2090388a00b0883dd2253e8bd606d8c250a32406fb8492d6896c861a97b. Record bytes unchanged since the original review. |
| original-review-4 | reviews/structured/20261022T024031Z-mononeme-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-5 | data/structures/membrane_organelle/mucocyst.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 5be0c727236d287685859cb323b9e0b109da3c26398bfe2d9adbe00f81f4b5bc; current SHA256 5be0c727236d287685859cb323b9e0b109da3c26398bfe2d9adbe00f81f4b5bc. Record bytes unchanged since the original review. |
| original-review-5 | reviews/structured/20261022T024032Z-mucocyst-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-6 | data/structures/membrane_organelle/multivesicular_body.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 cf6713b73e225eb2413a2a8b8a0fc9dfb6cf84a12f10133e3dcbec03791585a9; current SHA256 cf6713b73e225eb2413a2a8b8a0fc9dfb6cf84a12f10133e3dcbec03791585a9. Record bytes unchanged since the original review. |
| original-review-6 | reviews/structured/20261022T024033Z-multivesicular-body-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-7 | data/structures/membrane_organelle/multivesicular_body_intraluminal_vesicle.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 47e5f39198c321eb8e1df58ff20ac1a0a50ec731170ae0f9d07d22b299594916; current SHA256 47e5f39198c321eb8e1df58ff20ac1a0a50ec731170ae0f9d07d22b299594916. Record bytes unchanged since the original review. |
| original-review-7 | reviews/structured/20261022T024034Z-multivesicular-body-intraluminal-vesicle-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-8 | data/structures/membrane_organelle/multivesicular_body_lumen.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 6c67050e4fa82c1a03f0476a13be57741651c0ad9e1d4bfa241ca500525175f6; current SHA256 6c67050e4fa82c1a03f0476a13be57741651c0ad9e1d4bfa241ca500525175f6. Record bytes unchanged since the original review. |
| original-review-8 | reviews/structured/20261022T024034Z-multivesicular-body-lumen-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-9 | data/structures/membrane_organelle/multivesicular_body_membrane.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 f4b66123e8565c11507c55cd1184da62efd23de4b37e20995a6561bee8634db7; current SHA256 f4b66123e8565c11507c55cd1184da62efd23de4b37e20995a6561bee8634db7. Record bytes unchanged since the original review. |
| original-review-9 | reviews/structured/20261022T024035Z-multivesicular-body-membrane-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| septin-review-policy | .claude/skills/review-yaml-record/SKILL.md; Whole-record assertions, structured sources and severity rubric | supports | Positive molecular/pathway assertions require a real applicability assessment; absence of expression claims alone is not an exemption. Keep source scope, uncertainty and original finding identity; record curation is separate. |
| septin-curation-policy | docs/CURATION.md; Structural components, molecular grounding and family-or-class guidance | supports | Whole assembled membranes are structures; a LIPID component denotes molecular material and cannot use a complete membrane identity as exact chemical grounding. Taxon-agnostic protein families OR classes are permitted. An optional example inventory is not automatically required for every generic class. |
| septin-schema-policy | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, ComponentTypeEnum and grounding contract | supports | Molecular components and whole structures have different identities. Label-only supported lipid material is possible without inventing exact chemical composition. PROTEIN enum prose is interpreted with explicit CURATION generic-class permission; no automatic complex assertion follows from a heterogeneous class. |
| septin-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Graph nodes, component correspondence, source scope and necessity | supports | Descriptive boundary graphs can remain NONMECHANISTIC; source-specific localization, molecular identity and organelle-formation necessity must not be conflated. |
| septin-protein-policy | .claude/skills/uniprot-protein-examples/SKILL.md; Step2 generic classes and native coverage report | supports | Generic class components are explicitly recognized. A zero-example inventory or NO_GENE_SYMBOLS node is a stated coverage limit, not proof that the protein class does not exist or that its members form one stable complex. |
| septin-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031090,GO:0043233,GO:0032047,GO:0005737,GO:0016020; Exact five active GO identity/definition/synonym fields and selected membrane-parent relation | supports | GO0031090 describes an organelle-envelope bilayer; GO0043233 describes innermost enclosed organelle volume. GO0016020 defines collective membrane architecture. GO0032047 is whole mitosome and GO0005737 cytoplasm. These support broader class/containing structure, not exact child identity or a particular chemical lipid. |
| septin-go-mitosome-search | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=mitosome&amp;limit=100&amp;page=1; Complete one-page QuickGO search result, numberOfHits1 | supports | Only whole mitosome GO0032047 is returned. None of the four exact compartment identities is found in this bounded term search; exact UniProt locations support retained local identities. This is not a claim of exhaustive ontology absence. |
| septin-SL0438 | https://rest.uniprot.org/locations/SL-0438.json; Complete exact UniProt location JSON, including nested isA/partOf definitions and GO cross-references | supports | Envelope comprises inner/outer membranes and intermembrane space; partOf mitosome. Protein statistics are not used as evidence of absence or inventory completeness. Nested parent metabolic/import prose is not automatically asserted by these child records. |
| septin-SL0439 | https://rest.uniprot.org/locations/SL-0439.json; Complete exact UniProt location JSON, including nested isA/partOf definitions and GO cross-references | supports | Exact inner membrane separates matrix and IMS; exact synonyms match. Nested mitosome membrane and generic membrane define lipid-bilayer constitution. Protein statistics are not used as evidence of absence or inventory completeness. Nested parent metabolic/import prose is not automatically asserted by these child records. |
| septin-SL0440 | https://rest.uniprot.org/locations/SL-0440.json; Complete exact UniProt location JSON, including nested isA/partOf definitions and GO cross-references | supports | Exact IMS lies between inner/outer membranes, has all three target synonyms and is partOf envelope. Protein statistics are not used as evidence of absence or inventory completeness. Nested parent metabolic/import prose is not automatically asserted by these child records. |
| septin-SL0441 | https://rest.uniprot.org/locations/SL-0441.json; Complete exact UniProt location JSON, including nested isA/partOf definitions and GO cross-references | supports | Exact matrix is enclosed by the inner membrane, has mitosomal matrix synonym and is partOf mitosome. Protein statistics are not used as evidence of absence or inventory completeness. Nested parent metabolic/import prose is not automatically asserted by these child records. |
| septin-SL0443 | https://rest.uniprot.org/locations/SL-0443.json; Complete exact UniProt location JSON, including nested isA/partOf definitions and GO cross-references | supports | Exact outer membrane faces cytoplasm and both target synonyms match; nested generic membrane definition supplies collective material context. Protein statistics are not used as evidence of absence or inventory completeness. Nested parent metabolic/import prose is not automatically asserted by these child records. |
| septin-tax2759 | https://rest.uniprot.org/taxonomy/2759.json; Exact complete taxonomy identity/rank/active/lineage fields | supports | Active Eukaryota domain. Taxon identity does not establish quantitative prevalence, strain universality or organelle-formation experiments. |
| septin-tax5759 | https://rest.uniprot.org/taxonomy/5759.json; Exact complete taxonomy identity/rank/active/lineage fields | supports | Active Entamoeba histolytica species, Amoebozoa lineage. Taxon identity does not establish quantitative prevalence, strain universality or organelle-formation experiments. |
| septin-tovar1999-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1046%2Fj.1365-2958.1999.01414.x%22&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact MED PMID10361303, DOI, ordered authors/year and complete abstractText | supports | Tovar,Fischer,Clark1999 establishes Entamoeba CPN60 localization to a mitochondrial remnant and functional targeting-sequence deletion/replacement. The complete abstract does not itself demonstrate the specifically attributed double-membrane observation. This access limit is not refutation; full body/pixels are not claimed read. |
| septin-tachezy2022-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1111%2Fjeu.12922%22&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact MED PMID35567536, DOI, ordered authors/year and complete secondary abstractText | supports | DOI10.1111/jeu.12922 is The hydrogenosome of Trichomonas vaginalis by Tachezy,Makki,Hrdy2022. Complete abstract is hydrogenosome-focused; unread full body is not presumed to lack mitosome distribution discussion. Four target title mismatches are certain and retain separate exact lineage. |
| septin-catalogue | https://imodulondb.org/api/datasets; Complete official current organism/dataset catalogue | supports | All20 organism rows inspected; no matching Entamoeba/eukaryotic host is represented. More fundamentally these four records assert only collective lipid material or spatial topology and explicitly exclude molecular machinery. No downstream molecular query is required; no biological absence is inferred. |
| septin-miichi2009-pmc | https://pmc.ncbi.nlm.nih.gov/articles/2799805/; Previously fetched genuine PMC body re-read in this review at Results sec2,sec3 and Methods sec10,sec13; Fig1 caption text only | supports | Entamoeba HM-1:IMSScl6 mitosome fractions were purified and monitored by Cpn60, with partial proteome/contamination/heterogeneity qualifications and immunofluorescence methods. This supports later organelle occurrence and bounded experimental context, not a direct rereading of Tovar1999 ultrastructure. No proteins/pathways from this source are imported into child records. Cached public snapshot reused with its actual original access time; no fresh fetch of this body is claimed. |
| septin-roger2017-pdf | https://ecsolab.com/assets/pdf/roger_etal_2017.pdf; Previously fetched genuine secondary PDF re-read at R1184 opening Diversity paragraphs and R1186 reduction/mitosome comparison paragraphs; extracted text lines630–645,868–896 | supports | Review supports patchy low-oxygen eukaryotic organelle diversity and reductive continuum qualitatively. It is not a prevalence census or a primary formation experiment; unrelated lineage mechanisms are not assigned to these compartment records. Cached public snapshot reused with its actual original access time; no fresh fetch of this body is claimed. |
| septin-context-mitosome | data/structures/membrane_organelle/mitosome.yaml; Frozen identity/definition/source/parent/part_of/has_part/xrefs only | supports | Boundary context was frozen before read. Exact whole/envelope identity and reciprocal compartment relations support local references; unrelated functions/components/findings are not independently reviewed or resolved here. |
| septin-context-mitosome_envelope | data/structures/membrane_organelle/mitosome_envelope.yaml; Frozen identity/definition/source/parent/part_of/has_part/xrefs only | supports | Boundary context was frozen before read. Exact whole/envelope identity and reciprocal compartment relations support local references; unrelated functions/components/findings are not independently reviewed or resolved here. |
| septin-adapter-runner-historical | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical attempted runner only; no fresh invocation | supports | Actual00:49:00.848907Z–00:49:00.863225Z on2026-11-03 ended exit1 PermissionError reading pyvenv.cfg. This historical availability evidence is separate from fresh official catalogue and the four genuine scope exclusions. |
| septin-retrieval-source-receipts | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/adversary-septin/source-receipts.json; Actual retrieval or cached-body reinspection times and exact saved hashes | supports | Current authority requests are fresh; two previously fetched public bodies retain their original access timestamps and explicitly bounded reinspection scope. No historical failed retrieval is presented as current success. |
| septin-retrieval-additional-source-receipts | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/adversary-septin/additional-source-receipts.json; Actual retrieval or cached-body reinspection times and exact saved hashes | supports | Current authority requests are fresh; two previously fetched public bodies retain their original access timestamps and explicitly bounded reinspection scope. No historical failed retrieval is presented as current success. |
| septin-retrieval-reused-source-receipts | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/adversary-septin/reused-source-receipts.json; Actual retrieval or cached-body reinspection times and exact saved hashes | supports | Current authority requests are fresh; two previously fetched public bodies retain their original access timestamps and explicitly bounded reinspection scope. No historical failed retrieval is presented as current success. |
| septin-record-mitosome_inner_membrane | data/structures/membrane_organelle/mitosome_inner_membrane.yaml; Complete current record at d6a41b5d3397c9d62944c9c21890ef47a097a0fa | supports | Every identity,history,synonym,hierarchy,component,scope,canonical,evidence and complete graph field read. No protein example, gene symbol, UniProtKB xref, maintained image, numerical measurement, trait or verbatim snippet is asserted. |
| septin-original-mitosome_inner_membrane | reviews/structured/20261022T024026Z-mitosome-inner-membrane-audit/review.yaml; Original YAML/Markdown scientific scope, exact findings/actions, historical check disclosures and limitations | supports | Original remains immutable and its target frozen hash matches current bytes. Existing minor DOI-title finding is reassessed independently; historical checks retain historical scope. |
| septin-original-validation-mitosome_inner_membrane | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/adversary-septin/original-checks.json; Actual original native validation/render plus frozen historical source hash | supports | Native validate/render exit0 and Markdown byte equality; original source target hash agrees with frozen/current target. |
| septin-native-mitosome_inner_membrane-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/mitosome_inner_membrane-uniprot-verify-receipt.json; Actual receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/mitosome_inner_membrane-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0. Actual record has zero protein examples, zero GENE_OR_PROTEIN nodes and no UniProtKB graph xrefs. Native success validates an empty represented identifier scope, not all biological claims or a complete molecular inventory. |
| septin-native-mitosome_inner_membrane-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/mitosome_inner_membrane-uniprot-causal-receipt.json; Actual receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/mitosome_inner_membrane-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Exit0. Actual record has zero protein examples, zero GENE_OR_PROTEIN nodes and no UniProtKB graph xrefs. Native success validates an empty represented identifier scope, not all biological claims or a complete molecular inventory. |
| septin-record-mitosome_intermembrane_space | data/structures/membrane_organelle/mitosome_intermembrane_space.yaml; Complete current record at d6a41b5d3397c9d62944c9c21890ef47a097a0fa | supports | Every identity,history,synonym,hierarchy,component,scope,canonical,evidence and complete graph field read. No protein example, gene symbol, UniProtKB xref, maintained image, numerical measurement, trait or verbatim snippet is asserted. |
| septin-original-mitosome_intermembrane_space | reviews/structured/20261022T024027Z-mitosome-intermembrane-space-audit/review.yaml; Original YAML/Markdown scientific scope, exact findings/actions, historical check disclosures and limitations | supports | Original remains immutable and its target frozen hash matches current bytes. Existing minor DOI-title finding is reassessed independently; historical checks retain historical scope. |
| septin-original-validation-mitosome_intermembrane_space | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/adversary-septin/original-checks.json; Actual original native validation/render plus frozen historical source hash | supports | Native validate/render exit0 and Markdown byte equality; original source target hash agrees with frozen/current target. |
| septin-native-mitosome_intermembrane_space-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/mitosome_intermembrane_space-uniprot-verify-receipt.json; Actual receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/mitosome_intermembrane_space-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0. Actual record has zero protein examples, zero GENE_OR_PROTEIN nodes and no UniProtKB graph xrefs. Native success validates an empty represented identifier scope, not all biological claims or a complete molecular inventory. |
| septin-native-mitosome_intermembrane_space-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/mitosome_intermembrane_space-uniprot-causal-receipt.json; Actual receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/mitosome_intermembrane_space-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Exit0. Actual record has zero protein examples, zero GENE_OR_PROTEIN nodes and no UniProtKB graph xrefs. Native success validates an empty represented identifier scope, not all biological claims or a complete molecular inventory. |
| septin-record-mitosome_matrix | data/structures/membrane_organelle/mitosome_matrix.yaml; Complete current record at d6a41b5d3397c9d62944c9c21890ef47a097a0fa | supports | Every identity,history,synonym,hierarchy,component,scope,canonical,evidence and complete graph field read. No protein example, gene symbol, UniProtKB xref, maintained image, numerical measurement, trait or verbatim snippet is asserted. |
| septin-original-mitosome_matrix | reviews/structured/20261022T024029Z-mitosome-matrix-audit/review.yaml; Original YAML/Markdown scientific scope, exact findings/actions, historical check disclosures and limitations | supports | Original remains immutable and its target frozen hash matches current bytes. Existing minor DOI-title finding is reassessed independently; historical checks retain historical scope. |
| septin-original-validation-mitosome_matrix | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/adversary-septin/original-checks.json; Actual original native validation/render plus frozen historical source hash | supports | Native validate/render exit0 and Markdown byte equality; original source target hash agrees with frozen/current target. |
| septin-native-mitosome_matrix-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/mitosome_matrix-uniprot-verify-receipt.json; Actual receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/mitosome_matrix-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0. Actual record has zero protein examples, zero GENE_OR_PROTEIN nodes and no UniProtKB graph xrefs. Native success validates an empty represented identifier scope, not all biological claims or a complete molecular inventory. |
| septin-native-mitosome_matrix-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/mitosome_matrix-uniprot-causal-receipt.json; Actual receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/mitosome_matrix-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Exit0. Actual record has zero protein examples, zero GENE_OR_PROTEIN nodes and no UniProtKB graph xrefs. Native success validates an empty represented identifier scope, not all biological claims or a complete molecular inventory. |
| septin-record-mitosome_outer_membrane | data/structures/membrane_organelle/mitosome_outer_membrane.yaml; Complete current record at d6a41b5d3397c9d62944c9c21890ef47a097a0fa | supports | Every identity,history,synonym,hierarchy,component,scope,canonical,evidence and complete graph field read. No protein example, gene symbol, UniProtKB xref, maintained image, numerical measurement, trait or verbatim snippet is asserted. |
| septin-original-mitosome_outer_membrane | reviews/structured/20261022T024030Z-mitosome-outer-membrane-audit/review.yaml; Original YAML/Markdown scientific scope, exact findings/actions, historical check disclosures and limitations | supports | Original remains immutable and its target frozen hash matches current bytes. Existing minor DOI-title finding is reassessed independently; historical checks retain historical scope. |
| septin-original-validation-mitosome_outer_membrane | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/adversary-septin/original-checks.json; Actual original native validation/render plus frozen historical source hash | supports | Native validate/render exit0 and Markdown byte equality; original source target hash agrees with frozen/current target. |
| septin-native-mitosome_outer_membrane-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/mitosome_outer_membrane-uniprot-verify-receipt.json; Actual receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/mitosome_outer_membrane-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0. Actual record has zero protein examples, zero GENE_OR_PROTEIN nodes and no UniProtKB graph xrefs. Native success validates an empty represented identifier scope, not all biological claims or a complete molecular inventory. |
| septin-native-mitosome_outer_membrane-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/mitosome_outer_membrane-uniprot-causal-receipt.json; Actual receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/mitosome_outer_membrane-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Exit0. Actual record has zero protein examples, zero GENE_OR_PROTEIN nodes and no UniProtKB graph xrefs. Native success validates an empty represented identifier scope, not all biological claims or a complete molecular inventory. |
| plaque-current-4 | data/structures/membrane_organelle/mononeme.yaml; Entire current maintained record at d6a41b5d3397c9d62944c9c21890ef47a097a0fa, including components, all graphs, discussions and history | supports | Independently read current target; bytes match the original frozen target. Positive and explicitly excluded claims distinguished. |
| plaque-original-4 | reviews/structured/20261022T024031Z-mononeme-audit/review.yaml; Exact staleness-selected original YAML plus native-rendered Markdown; full source/check/assessment/finding/action fields | supports | Original pair native validation, exact Markdown rendering and all historical input hashes verified. Qualified pass; no original scientific finding or request-curation action. |
| plaque-current-5 | data/structures/membrane_organelle/mucocyst.yaml; Entire current maintained record at d6a41b5d3397c9d62944c9c21890ef47a097a0fa, including components, all graphs, discussions and history | supports | Independently read current target; bytes match the original frozen target. Positive and explicitly excluded claims distinguished. |
| plaque-original-5 | reviews/structured/20261022T024032Z-mucocyst-audit/review.yaml; Exact staleness-selected original YAML plus native-rendered Markdown; full source/check/assessment/finding/action fields | supports | Original pair native validation, exact Markdown rendering and all historical input hashes verified. One inherited major MDL1 identity finding remains. |
| plaque-policy | .claude/skills/review-yaml-record/SKILL.md; Frozen native policy, unchanged from previously read PR2370 set; structured-source paragraph and current enum contract reread | context_only | Native applicability includes genes, loci, accessions, proteins, pathways, stress and traits; expression-module absence is not sufficient exemption. |
| plaque-rubric | .claude/skills/curate-yaml-record/references/review-checklist.md; Frozen native policy, unchanged from previously read PR2370 set; structured-source paragraph and current enum contract reread | context_only | Exact identity, support, taxonomy, membership, necessity and mechanisms assessed separately; optional inventories alone are not findings. |
| plaque-graph-rubric | .claude/skills/curate-causal-graphs/SKILL.md; Frozen native policy, unchanged from previously read PR2370 set; structured-source paragraph and current enum contract reread | context_only | Descriptive association, localization and biochemical mechanism are distinct; preserve experimental-stage/preparation scope. |
| plaque-protein-contract | .claude/skills/uniprot-protein-examples/SKILL.md; Frozen native policy, unchanged from previously read PR2370 set; structured-source paragraph and current enum contract reread | context_only | Native accession/field correspondence and graph coverage cannot certify literature-symbol equivalence or complex membership. |
| plaque-schema-policy | src/cellstructuremech/schema/cellstructuremech.yaml; Frozen native policy, unchanged from previously read PR2370 set; structured-source paragraph and current enum contract reread | context_only | Native GENE_OR_PROTEIN permits protein families and complexes. Do not manufacture enum-only retyping or require every optional protein inventory. |
| plaque-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0070074,GO:0043231,GO:0020007,GO:0020025,GO:0020009,GO:0020008,GO:0020026,GO:0036000,GO:0030141; Complete exact nine-term response; definitions, synonyms, comments and typed children | supports | Mononeme GO0070074 and mucocyst GO0036000 identities agree. Apical complex has direct mononeme part_of child; intracellular membrane-bounded organelle has mononeme is_a child. Secretory granule has mucocyst is_a child. Distinct microneme/rhoptry/dense-granule identities are not conflated. |
| plaque-GO0070074-isa | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0070074/ancestors?relations=is_a; Complete current exact is_a ancestor response | supports | Mononeme has intracellular membrane-bounded organelle ancestor0043231. Parthood is assessed separately. |
| plaque-GO0036000-isa | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0036000/ancestors?relations=is_a; Complete current exact is_a ancestor response | supports | Mucocyst has secretory granule ancestor0030141. Parthood is assessed separately. |
| plaque-tax5833 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5833; Complete native ENA taxon identity, rank, lineage and aliases response | supports | 5833 resolves to Plasmodium falciparum species. Species and strain scopes are kept distinct; no proxy strain is silently substituted. |
| plaque-tax5911 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5911; Complete native ENA taxon identity, rank, lineage and aliases response | supports | 5911 resolves to Tetrahymena thermophila species. Species and strain scopes are kept distinct; no proxy strain is silently substituted. |
| plaque-tax312017 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/312017; Complete native ENA taxon identity, rank, lineage and aliases response | supports | 312017 resolves to Tetrahymena thermophila SB210 strain. Species and strain scopes are kept distinct; no proxy strain is silently substituted. |
| plaque-protein-A8IWX2 | https://rest.uniprot.org/uniprotkb/A8IWX2.json; Complete current UniProtKB JSON; accession, entry status, native protein/gene names, organism, sequence length, comments and cross-references | supports | UNREVIEWED Rhomboid-like protease, Rom1, P.falciparum5833,278 aa; native entry includes original sequence provenance. Rhomboid-family annotation is not primary evidence of mononeme localization or invasion necessity. |
| plaque-protein-P90618 | https://rest.uniprot.org/uniprotkb/P90618.json; Complete current UniProtKB JSON; accession, entry status, native protein/gene names, organism, sequence length, comments and cross-references | supports | UNREVIEWED Granule lattice protein1, GRL1, T.thermophila5911,402 aa. Correct species-level example; no fresh InterPro family annotation established. |
| plaque-protein-O76218 | https://rest.uniprot.org/uniprotkb/O76218.json; Complete current UniProtKB JSON; accession, entry status, native protein/gene names, organism, sequence length, comments and cross-references | supports | UNREVIEWED Granule lattice protein3, GRL3, T.thermophila5911,377 aa. Automated trichocyst/domain annotations do not replace primary mucocyst evidence. |
| plaque-protein-O76219 | https://rest.uniprot.org/uniprotkb/O76219.json; Complete current UniProtKB JSON; accession, entry status, native protein/gene names, organism, sequence length, comments and cross-references | supports | UNREVIEWED Granule lattice protein4, GRL4, T.thermophila5911,394 aa. Automated trichocyst/domain annotations do not replace primary mucocyst evidence. |
| plaque-protein-Q3S4V5 | https://rest.uniprot.org/uniprotkb/Q3S4V5.json; Complete current UniProtKB JSON; accession, entry status, native protein/gene names, organism, sequence length, comments and cross-references | supports | UNREVIEWED Granule tip protein1, GRT1, T.thermophila5911,765 aa; gamma-crystallin-like cross-reference. Primary cargo localization and transport are separate evidence. |
| plaque-protein-Q2I2L7 | https://rest.uniprot.org/uniprotkb/Q2I2L7.json; Complete current UniProtKB JSON; accession, entry status, native protein/gene names, organism, sequence length, comments and cross-references | supports | UNREVIEWED Granule tip protein2, GRT2, T.thermophila5911,765 aa; native gamma-crystallin-like cross-reference is available despite throttled separate InterPro endpoint. |
| plaque-protein-I7M6L0 | https://rest.uniprot.org/uniprotkb/I7M6L0.json; Complete current UniProtKB JSON; accession, entry status, native protein/gene names, organism, sequence length, comments and cross-references | supports | UNREVIEWED Ubiquitin interaction motif protein, ORF TTHERM_00471830, SB210312017,392 aa; no native primary MDL1 gene name. Automated S5A-family and PSMD4/UIM/vWFA cross-references conflict with its maintained MDL1 attribution. |
| plaque-protein-I7MM25 | https://rest.uniprot.org/uniprotkb/I7MM25.json; Complete current UniProtKB JSON; accession, entry status, native protein/gene names, organism, sequence length, comments and cross-references | supports | UNREVIEWED Concanavalin A-like lectin/glucanase family protein, ORF TTHERM_00658810, SB210312017,346 aa; exact paper-locus candidate. Native entry does not itself establish MDL1 nomenclature or mature-MDD membership. |
| plaque-family-A8IWX2 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/A8IWX2/?page_size=200; Complete InterPro protein-entry response, page_size200; all returned entries and their native types inspected | supports | Three entries: broad S54 rhomboid family IPR002610, rhomboid domain IPR022764 and rhomboid-like superfamily IPR035952; not an exact PfROM1-specific family or localization proof. |
| plaque-family-O76218 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/O76218/?page_size=200; Complete InterPro protein-entry response, page_size200; all returned entries and their native types inspected | supports | Only IPR059991 trichocyst matrix protein T1-F coiled-coil domain returned; a domain annotation is not whole-GRL-cohort identity. |
| plaque-family-O76219 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/O76219/?page_size=200; Complete InterPro protein-entry response, page_size200; all returned entries and their native types inspected | supports | Only IPR059991 trichocyst matrix protein T1-F coiled-coil domain returned; no whole-GRL-cohort grounding inferred. |
| plaque-family-Q3S4V5 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q3S4V5/?page_size=200; Complete InterPro protein-entry response, page_size200; all returned entries and their native types inspected | supports | IPR011024 gamma-crystallin-like homologous superfamily returned; broad support for declared GRT domain context, not exact family or transport evidence. |
| plaque-family-I7M6L0 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/I7M6L0/?page_size=200; Complete InterPro protein-entry response, page_size200; all returned entries and their native types inspected | supports | Four current entries include family IPR027040 PSMD4, UIM conserved site IPR003903 and vWFA domain/superfamily. Family assignment agrees with S5A/Rpn10 identity rather than the paper MDL1 locus. |
| plaque-family-I7MM25 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/I7MM25/?page_size=200; Complete InterPro protein-entry response, page_size200; all returned entries and their native types inspected | supports | Concanavalin-A-like superfamily IPR013320 plus DUF8019 IPR058332 returned; no exact complete MDD-complex grounding inferred. |
| plaque-IPR027040 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR027040/; Native entry metadata, family name, hierarchy and description | supports | IPR027040 explicitly denotes 26S proteasome non-ATPase regulatory subunit4, PSMD4/S5A/Rpn10. This corroborates wrong native protein identity; no claim that this abstract family annotation experimentally localizes the Tetrahymena protein. |
| plaque-family-P90618 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P90618/?page_size=200; HTTP204 with curl exit92 invalid HTTP/2 content-length; zero saved bytes and no body file | context_only | Inconclusive retrieval. Empty snapshot hash represents zero received body bytes, not evidence that GRL1 has no family annotation. |
| plaque-family-Q2I2L7 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q2I2L7/?page_size=200; HTTP429 JSON explicitly reports request throttling | context_only | Separate InterPro mapping was unavailable; successful current UniProt cross-reference is recorded separately. No negative family or biology conclusion. |
| plaque-query-MDL1 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AMDL1+AND+taxonomy_id%3A5911&amp;format=json&amp;size=25; Complete bounded UniProtKB search response, size25, taxonomy scope in query | supports | Exact MDL1 gene query returned zero; this does not refute MDL1 biology or imply an exhaustive alias search. |
| plaque-query-MDL1-locus | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ATTHERM_00658810+AND+taxonomy_id%3A5911&amp;format=json&amp;size=25; Complete bounded UniProtKB search response, size25, taxonomy scope in query | supports | Exact paper locus TTHERM_00658810 returned one I7MM25 match. |
| plaque-query-wrong-locus | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ATTHERM_00471830+AND+taxonomy_id%3A5911&amp;format=json&amp;size=25; Complete bounded UniProtKB search response, size25, taxonomy scope in query | supports | Exact maintained locus TTHERM_00471830 returned one I7M6L0 match. |
| plaque-query-Rom1 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ARom1+AND+organism_id%3A5833&amp;format=json&amp;size=25; Complete bounded UniProtKB search response, size25, taxonomy scope in query | supports | Exact Rom1 query returned one A8IWX2 match. |
| plaque-singh2007-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1073%2Fpnas.0709999104%22&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact DOI metadata title, authors, year, PMID and returned PMC identity; not a claim to inspect every abstract or source linked from metadata | supports | Citation identity matches the corresponding independently inspected primary body. Metadata is not mechanism evidence. |
| plaque-rahaman2009-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1128%2FEC.00151-09%22&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact DOI metadata title, authors, year, PMID and returned PMC identity; not a claim to inspect every abstract or source linked from metadata | supports | Citation identity matches the corresponding independently inspected primary body. Metadata is not mechanism evidence. |
| plaque-kontur2016-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1534%2Fg3.116.028878%22&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact DOI metadata title, authors, year, PMID and returned PMC identity; not a claim to inspect every abstract or source linked from metadata | supports | Citation identity matches the corresponding independently inspected primary body. Metadata is not mechanism evidence. |
| plaque-kuppannan2022-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1371%2Fjournal.pgen.1010194%22&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact DOI metadata title, authors, year, PMID and returned PMC identity; not a claim to inspect every abstract or source linked from metadata | supports | Citation identity matches the corresponding independently inspected primary body. Metadata is not mechanism evidence. |
| plaque-kaur2017-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1091%2Fmbc.e17-01-0018%22&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact DOI metadata title, authors, year, PMID and returned PMC identity; not a claim to inspect every abstract or source linked from metadata | supports | Citation identity matches the corresponding independently inspected primary body. Metadata is not mechanism evidence. |
| plaque-singh2007-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC2148419/; Genuine PMC2148419 HTML; title/DOI, complete Introduction, Results sections2–5, Discussion6, Methods8–12 and main Figure1–6 captions. No figure pixels or supplementary movies inspected. | supports | Full-length 278-aa PfROM1 was episomally triple-HA tagged under its promoter in P.falciparum3D7. Mature segmenters show thread-like apical localization distinct from assayed microneme/rhoptry/dense-granule markers and near subpellicular microtubules. Released merozoites show surface redistribution. Confocal proximity and endpoint redistribution are not evidence for a specific motor/transport route, cleavage mechanism or universal invasion requirement. Earlier schizonts differ; the record preserves mature-segmenter scope. |
| plaque-rahaman2009-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC2756869/; Genuine PMC2756869 HTML, verified title/DOI; text sections2,3,6,8,9,13,14,15,17,18,19 covering culture, knockout/sorting, biochemistry and Discussion. No figure pixels, supplementary material or caption-level microscopy audit claimed. | supports | CU428.1/SB281 experiments distinguish Grl proprotein heterooligomers from monomeric Grt cargo under the tested detergent/neutral-pH conditions. GRT1/2 double knockout preserves gross crystal morphology and stimulated secretion with subtler adhesion effects. Independent sorting is supported in the paper scope; authors explicitly cannot exclude other associations in wild-type/TGN conditions. No universal GRL/GRT formation necessity is inferred. |
| plaque-kontur2016-body | https://pmc-oa-opendata.s3.amazonaws.com/PMC4978903.1/PMC4978903.1.xml; Genuine PMC4978903.1 JATS; S2 culture/Table1 strains, S13 immunofluorescence, S15 fractionation, S30–33 Results and included captions. No pixels, raw fractions or uninspected mapping sections. | supports | MMA1 loss blocks normal mature mucocyst accumulation and cargo processing. Functional induced Mma1-CFP was predominantly cytosolic with a small pelletable fraction and no significant mature-mucocyst colocalization; endogenous3xGFP signal was below detection. Supports bounded maturation/canonical-example context, not mature resident inventory or all-strain equivalence. |
| plaque-kuppannan2022-body | https://pmc-oa-opendata.s3.amazonaws.com/PMC9159632.1/PMC9159632.1.xml; Genuine PMC9159632.1 JATS; Results sec003–009 including main captions, Methods sec011 culture, sec025 secretion assays, sec026 immunoprecipitation, sec027 LC-MS, sec029 negative-stain TEM. No actual figure pixels, S1/S2 tables, raw spectra or movies. | supports | Results sec004 explicitly defines MDL1 as TTHERM_00658810 encoding346 aa. Functional endogenous tagged Mdl1 polarizes before docking; loss impairs docking/secretion while mature crystals form. Immunoprecipitation/size fractionation and negative-stain EM support a putative MDD assembly with other mucocyst-associated subunits. Exact assembly dependencies, complete complex topology and direct fusion mechanism remain unresolved; predicted membrane/lipidation features are not universal biochemical necessities. |
| plaque-kaur2017-body | https://pmc-oa-opendata.s3.amazonaws.com/PMC5449153.1/PMC5449153.1.xml; Genuine PMC5449153.1 JATS; zero-based body//sec indices6,7,11,13,15,20,21,22: STX7L1 late-endosomal syntaxin, immature/mature localization including Fig6 caption, Discussion, culture, expression and imaging/colocalization Methods. No pixels, supplements or complete AP3 localization audit. | supports | Induced Stx7l1-GFP localizes to mature and immature mucocysts in the inspected contexts; localization does not establish exocytic fusion machinery. Current conditional component-selection discussion does not deny this localization or mandate an exhaustive protein inventory. AP3/Stx7l1 formation/maturation claims are distinguished from mature resident/late-fusion necessity; no new optional-inventory defect established. |
| plaque-catalogue | https://imodulondb.org/api/datasets; Complete fresh official /api/datasets response; every returned organism/dataset entry independently read | supports | Catalogue has no Plasmodium, Tetrahymena or other represented eukaryotic host. Both targets positively name genes/proteins and secretory behavior, so applicability must be assessed before the bounded no-matching-host outcome. No unrelated bacterial/archaeal strain is a proxy and no downstream matched module query applies. |
| plaque-historical-runner | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical00:49Z unavailable invocation and exact retained stdout/stderr hashes | context_only | Historical runner failed on OS PermissionError reading pyvenv.cfg. Fresh official catalogue and primary/authority fallback are current source checks; no fresh runner attempt/success claimed. |
| plaque-original-checks | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/adversary-plaque/original-checks.json; Two original native validate/render executions, historical input and current target comparisons | supports | Both original pairs validate and render exactly; each has14 matching historical frozen inputs and unchanged current target bytes. No original artifact edits. |
| plaque-native-mononeme-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/mononeme.yaml --verify; Actual root receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/mononeme-uniprot-verify-receipt.json; exact stdoutSHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | One UNREVIEWED A8IWX2 example and one COVERED typed node. Native accession/field checks pass; they do not certify literature-symbol equivalence, localization or necessity. |
| plaque-native-mononeme-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/mononeme.yaml --causal-graphs; Actual root receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/mononeme-uniprot-causal-receipt.json; exact stdoutSHA256 3781cd140b3497305c788818137907d8b5f1135ddf2cf03128e2348128267e99 | supports | One UNREVIEWED A8IWX2 example and one COVERED typed node. Native accession/field checks pass; they do not certify literature-symbol equivalence, localization or necessity. |
| plaque-native-mucocyst-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/mucocyst.yaml --verify; Actual root receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/mucocyst-uniprot-verify-receipt.json; exact stdoutSHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Six UNREVIEWED examples and three COVERED typed nodes; the MDD node is reported COVERED through I7M6L0, despite its independently confirmed wrong MDL1 attribution. Native accession/field checks pass; they do not certify literature-symbol equivalence, localization or necessity. |
| plaque-native-mucocyst-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/mucocyst.yaml --causal-graphs; Actual root receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/mucocyst-uniprot-causal-receipt.json; exact stdoutSHA256 0db45fdd11cde066b43f98876b7c74196880805dda60dc3b7b92d3944b636a3e | supports | Six UNREVIEWED examples and three COVERED typed nodes; the MDD node is reported COVERED through I7M6L0, despite its independently confirmed wrong MDL1 attribution. Native accession/field checks pass; they do not certify literature-symbol equivalence, localization or necessity. |
| micro-policy | .claude/skills/review-yaml-record/SKILL.md; Native review skill, profile/config/output contract/checklist and AGENTS GO-first rule | context_only | Actual named gene, complex and pathway claims trigger structured-source applicability assessment beyond expression assertions. Reviews retain original inputs and exact finding lineage; no record curation authorized. |
| micro-identifier-preservation | docs/CURATION.md; Identifiers rules1-3 and following local-slug paragraph; schema replaces field | context_only | An exact GO CC takes priority over a minted identifier. An existing identifier is not silently renamed: retain deprecated predecessor and successor replaces in separately authorized curation. |
| micro-component-policy | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent391-455, replaces350-357, CausalNode845-890; native class/essentiality guidance | context_only | Constituent lipid material differs from a whole membrane, assembly machinery and cargo; collective label-only material is permissible. Essentiality means structure formation, not physiological activity. Protein complexes can use STRUCTURE or GENE_OR_PROTEIN; no enum-only defect. |
| micro-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Complete graph contract; UniProt-example skill; verifier671-804; documented validate/render recipes | context_only | Check each edge at its claimed scope; do not force transient ESCRT machinery into mature structure components. Native protein pass with no examples/nodes does not verify GO complex identities or prove biological completeness. |
| micro-record-multivesicular_body | data/structures/membrane_organelle/multivesicular_body.yaml; Entire current record, including all history/evidence/components/functions/graphs/discussions | supports | Current target is byte-identical to the original frozen input; biological content was independently reassessed. |
| micro-prior-multivesicular_body | reviews/structured/20261022T024033Z-multivesicular-body-audit/review.yaml; Original review envelope, checks/evidence/assessments/findings/actions/limitations and exact native Markdown | context_only | Historical pass_with_limitations; 0 scientific findings. Explicit expression-only adapter exclusion is present, not omitted. Historical gates and source access are not current execution claims. |
| micro-native-multivesicular_body-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/multivesicular_body-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/multivesicular_body.yaml --verify; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/multivesicular_body-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0 at exact source. Zero component protein examples and zero GENE_OR_PROTEIN nodes; GO-grounded STRUCTURE actors checked separately at GO. No molecular identity, localization, stoichiometry or formation necessity inferred from empty native coverage. |
| micro-native-multivesicular_body-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/multivesicular_body-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/multivesicular_body.yaml --causal-graphs; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/multivesicular_body-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Exit0 at exact source. Zero component protein examples and zero GENE_OR_PROTEIN nodes; GO-grounded STRUCTURE actors checked separately at GO. No molecular identity, localization, stoichiometry or formation necessity inferred from empty native coverage. |
| micro-record-multivesicular_body_intraluminal_vesicle | data/structures/membrane_organelle/multivesicular_body_intraluminal_vesicle.yaml; Entire current record, including all history/evidence/components/functions/graphs/discussions | supports | Current target is byte-identical to the original frozen input; biological content was independently reassessed. |
| micro-prior-multivesicular_body_intraluminal_vesicle | reviews/structured/20261022T024034Z-multivesicular-body-intraluminal-vesicle-audit/review.yaml; Original review envelope, checks/evidence/assessments/findings/actions/limitations and exact native Markdown | context_only | Historical needs_curation; 1 scientific findings. Explicit expression-only adapter exclusion is present, not omitted. Historical gates and source access are not current execution claims. |
| micro-native-multivesicular_body_intraluminal_vesicle-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/multivesicular_body_intraluminal_vesicle-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/multivesicular_body_intraluminal_vesicle.yaml --verify; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/multivesicular_body_intraluminal_vesicle-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0 at exact source. Zero component protein examples and zero GENE_OR_PROTEIN nodes; GO-grounded STRUCTURE actors checked separately at GO. No molecular identity, localization, stoichiometry or formation necessity inferred from empty native coverage. |
| micro-native-multivesicular_body_intraluminal_vesicle-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/multivesicular_body_intraluminal_vesicle-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/multivesicular_body_intraluminal_vesicle.yaml --causal-graphs; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/multivesicular_body_intraluminal_vesicle-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Exit0 at exact source. Zero component protein examples and zero GENE_OR_PROTEIN nodes; GO-grounded STRUCTURE actors checked separately at GO. No molecular identity, localization, stoichiometry or formation necessity inferred from empty native coverage. |
| micro-record-multivesicular_body_lumen | data/structures/membrane_organelle/multivesicular_body_lumen.yaml; Entire current record, including all history/evidence/components/functions/graphs/discussions | supports | Current target is byte-identical to the original frozen input; biological content was independently reassessed. |
| micro-prior-multivesicular_body_lumen | reviews/structured/20261022T024034Z-multivesicular-body-lumen-audit/review.yaml; Original review envelope, checks/evidence/assessments/findings/actions/limitations and exact native Markdown | context_only | Historical needs_curation; 1 scientific findings. Explicit expression-only adapter exclusion is present, not omitted. Historical gates and source access are not current execution claims. |
| micro-native-multivesicular_body_lumen-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/multivesicular_body_lumen-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/multivesicular_body_lumen.yaml --verify; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/multivesicular_body_lumen-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0 at exact source. Zero component protein examples and zero GENE_OR_PROTEIN nodes; GO-grounded STRUCTURE actors checked separately at GO. No molecular identity, localization, stoichiometry or formation necessity inferred from empty native coverage. |
| micro-native-multivesicular_body_lumen-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/multivesicular_body_lumen-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/multivesicular_body_lumen.yaml --causal-graphs; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/multivesicular_body_lumen-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Exit0 at exact source. Zero component protein examples and zero GENE_OR_PROTEIN nodes; GO-grounded STRUCTURE actors checked separately at GO. No molecular identity, localization, stoichiometry or formation necessity inferred from empty native coverage. |
| micro-record-multivesicular_body_membrane | data/structures/membrane_organelle/multivesicular_body_membrane.yaml; Entire current record, including all history/evidence/components/functions/graphs/discussions | supports | Current target is byte-identical to the original frozen input; biological content was independently reassessed. |
| micro-prior-multivesicular_body_membrane | reviews/structured/20261022T024035Z-multivesicular-body-membrane-audit/review.yaml; Original review envelope, checks/evidence/assessments/findings/actions/limitations and exact native Markdown | context_only | Historical pass_with_limitations; 0 scientific findings. Explicit expression-only adapter exclusion is present, not omitted. Historical gates and source access are not current execution claims. |
| micro-native-multivesicular_body_membrane-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/multivesicular_body_membrane-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/multivesicular_body_membrane.yaml --verify; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/multivesicular_body_membrane-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0 at exact source. Zero component protein examples and zero GENE_OR_PROTEIN nodes; GO-grounded STRUCTURE actors checked separately at GO. No molecular identity, localization, stoichiometry or formation necessity inferred from empty native coverage. |
| micro-native-multivesicular_body_membrane-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/multivesicular_body_membrane-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/multivesicular_body_membrane.yaml --causal-graphs; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/multivesicular_body_membrane-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Exit0 at exact source. Zero component protein examples and zero GENE_OR_PROTEIN nodes; GO-grounded STRUCTURE actors checked separately at GO. No molecular identity, localization, stoichiometry or formation necessity inferred from empty native coverage. |
| micro-original-pairs | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/adversary-microtubule/original-checks.json; Actual four native validate and four render --content commands; all Markdown exact | supports | All original four pairs pass validation and exact deterministic rendering. |
| micro-original-inputs | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/adversary-microtubule/original-frozen-inputs.json; All76 original input entries checked against original retained source revisions | supports | Every original target and context hash verifies; all four current target hashes remain unchanged. Historical context hashing is provenance checking, not renewed scientific assessment of those unfrozen neighboring records. |
| micro-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005771,GO:0097487,GO:0097486,GO:0032585,GO:0031904,GO:0010008,GO:0031982,GO:0005770,GO:0071985,GO:0000813,GO:0000814,GO:0000815; All12 returned active term identities, definitions, synonyms and typed child relations | supports | Exact wholeMVB0005771, limiting membrane0032585, sorting0071985 and ESCRT0813/0814/0815 definitions agree. Active0097487 is a membrane-bounded vesicle wholly inside MVB;0097486 is the outermost-membrane enclosed lumen. WholeMVB lists both as part_of children; lateendosome5770 lists MVB as is_a child. |
| micro-go-0097486-isa | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097486/ancestors?relations=is_a; Complete relations=is_a ancestor list; not all listed ancestors are immediate parents | supports | The exact candidate has the declared broader ancestry:0097486 under endosome lumen0031904;0097487 under vesicle0031982. Combined with exact definition and typed MVB parthood this establishes biological equivalence, not a label-only match. |
| micro-go-0097487-isa | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097487/ancestors?relations=is_a; Complete relations=is_a ancestor list; not all listed ancestors are immediate parents | supports | The exact candidate has the declared broader ancestry:0097486 under endosome lumen0031904;0097487 under vesicle0031982. Combined with exact definition and typed MVB parthood this establishes biological equivalence, not a label-only match. |
| micro-go-0005771-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005771/ancestors?relations=is_a,part_of; Complete relations=is_a,part_of mixed ancestor list; relation types not inferred from flat results | supports | Mixed hierarchy/parthood response corroborates containing context; direct parent relation claims rely on separately typed GO child relations or SL isA/partOf objects, not untyped ancestor membership. |
| micro-go-0032585-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032585/ancestors?relations=is_a,part_of; Complete relations=is_a,part_of mixed ancestor list; relation types not inferred from flat results | supports | Mixed hierarchy/parthood response corroborates containing context; direct parent relation claims rely on separately typed GO child relations or SL isA/partOf objects, not untyped ancestor membership. |
| micro-sl0174 | https://rest.uniprot.org/locations/SL-0174.json; Complete exact location identity, five maintained synonyms, direct isA/partOf and GO links; nested entries read as boundary context | supports | SL0174 matches whole MVB and late-endosome classification. Protein counts are not complete component inventories or proof of stable membership. |
| micro-sl0175 | https://rest.uniprot.org/locations/SL-0175.json; Complete exact location identity, five maintained synonyms, direct isA/partOf and GO links; nested entries read as boundary context | supports | SL0175 matches limiting MVB membrane, endosome-membrane parent and wholeMVB parthood. Protein counts are not complete component inventories or proof of stable membership. |
| micro-sl0340 | https://rest.uniprot.org/locations/SL-0340.json; Complete exact location identity, five maintained synonyms, direct isA/partOf and GO links; nested entries read as boundary context | supports | SL0340 matches outer MVB lumen, endosome-lumen parent and wholeMVB parthood; not the inside of an individual ILV. Protein counts are not complete component inventories or proof of stable membership. |
| micro-tax4932 | https://rest.uniprot.org/taxonomy/4932.json; taxonId, scientificName, rank and complete lineage | supports | 4932 confirms Saccharomyces cerevisiae at species rank. Does not establish a particular experimental strain or frequency of MVBs in every culture. |
| micro-katzmann2001-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11511343%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=20; Exact PMID or quoted DOI core search, pageSize20; unique MED identity/title/authors/year and complete abstract | supports | Primary PMID11511343/DOI10.1016/S0092-8674(01)00434-2: ubiquitination as sorting signal and ESCRT-I cargo recognition/function in MVB sorting; yeast/mammalian conservation proposed. No unread Methods, exact strain or specific scission assay certified. |
| micro-babst2002-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12194857%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=20; Exact PMID or quoted DOI core search, pageSize20; unique MED identity/title/authors/year and complete abstract | supports | Primary PMID12194857/DOI10.1016/S1534-5807(02)00220-4: cytosolic ESCRT-III proteins recruit/oligomerize at endosomal membranes, Vps20-Snf7/Vps2-Vps24 functional organization and cargo sorting/concentration. Abstract is not a direct scission-reconstitution experiment. |
| micro-teo2004-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016/j.devcel.2004.09.003%22&amp;format=json&amp;resultType=core&amp;pageSize=20; Exact PMID or quoted DOI core search, pageSize20; unique MED identity/title/authors/year and complete abstract | supports | Primary PMID15469844/DOI10.1016/j.devcel.2004.09.003 matches genuine PDF: purified ESCRT-II directly binds Vps20 chiefly via Vps25 and increases both proteins membrane association in vitro. |
| micro-henne2011-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016/j.devcel.2011.05.015%22&amp;format=json&amp;resultType=core&amp;pageSize=20; Exact PMID or quoted DOI core search, pageSize20; unique MED identity/title/authors/year and complete abstract | context_only | Secondary review PMID21763610/DOI10.1016/j.devcel.2011.05.015: cargo-recognition/membrane-sculpting ESCRT pathway and MVB delivery to vacuole/lysosome. Abstract-only synthesis, not an independently read experimental body. |
| micro-teo2004-pdf | https://www2.mrc-lmb.cam.ac.uk/groups/rlw/download/publications/15469844.pdf; Printed p559 title/summary/Introduction; complete pp564-567 including Results, Conclusions, Figure4-6 captions and Experimental Procedures; no figure pixels, remaining structural Results or supplements | supports | Direct purified ESCRT-II/Vps20 binding chiefly through Vps25 and enhanced binding to bovine-brain-lipid liposomes support the coarse recruitment edge. S.cerevisiae genes cloned from ATCC9763D DNA and expressed in E.coli C41/B834; these expression hosts are not biological MVB exemplars or matching transcriptomic proxies. Figure6 is explicitly a model; this is not complete in-vivo ILV scission or a universal lipid-composition assay. |
| micro-katzmann2001-access | https://doi.org/10.1016/S0092-8674(01)00434-2; Exact DOI redirects to Elsevier Article Locator; inspected HTTP200 HTML has redirect metadata but no body | context_only | DOI resolves, but response is not full text. Cell fulltext route returned403. Complete native abstract remains the inspected tier. |
| micro-babst2002-access | https://doi.org/10.1016/S1534-5807(02)00220-4; Exact DOI redirects to Elsevier Article Locator; inspected HTTP200 HTML has redirect metadata but no body | context_only | DOI resolves, but response is not full text. Indexed Cell PDF route returned403. Complete native abstract remains the inspected tier. |
| micro-henne2011-access | https://doi.org/10.1016/j.devcel.2011.05.015; Exact DOI redirects to Elsevier Article Locator; inspected HTTP200 HTML has redirect metadata but no body | context_only | DOI resolves, but response is not full text. Exact Cell publisher https://www.cell.com/developmental-cell/retrieve/pii/S1534580711002073 returned403. Complete native abstract remains the inspected tier. |
| micro-local-identity-search | rg -n --no-ignore --hidden -g *.yaml GO:0097486&#124;GO:0097487&#124;^identifier: cellstructuremech:multivesicular_body_(lumen&#124;intraluminal_vesicle)$ data/structures; Complete ignored-inclusive maintained data/structures YAML search; output /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/adversary-microtubule/identity-search.log | supports | Each local target identifier occurs in its one maintained record; no GO0097486/0097487 occurrence in this bounded complete corpus search. Existing local links remain valid; no broken-reference finding assigned to sibling records. |
| micro-catalogue-api | https://imodulondb.org/api/datasets; Complete official array, all20 organism rows/28 organism-dataset pairs | supports | No Saccharomyces/yeast or ATCC9763D host dataset is represented. No matched downstream search/summary or bacterial-expression-host surrogate is warranted; noncoverage is not evidence against ESCRT biology. |
| micro-historical-runner | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical00:49Z attempted dataset command and PermissionError reading pyvenv.cfg | context_only | Actual historical optional runner exit1/unavailable. Not rerun or relabeled as current execution; current official catalogue is a separate successful fallback. |
| check-qc | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/qc.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| check-labels | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/labels.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| check-trait-links | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/trait-links.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Native TraitMech link check passed. |
| check-vendored | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/vendored.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Pinned governed files match; native vendored check passed. |
| check-curies | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/curies.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| focused | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/focused-results.json; All twenty actual target schema/strict command outputs | supports | Ten schema and ten strict commands returned exit zero. |
| supplemental-pmid | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/pmid-chunks-receipt.json; Complete native-report PMID set checked with unchanged resolver in batches of at most fifty | supports | 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers remain unverified. |
| historical-adapter-runner-availability | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical runner invocation receipt, exact SHA256 reverified during PR2371 synthesis | context_only | Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS PermissionError reading the configured runner pyvenv.cfg. This is a retained historical availability observation, not a fresh attempt or a scientific validation failure. Native policy permits inspected source-catalogue fallback. |

## Limits And Additional Notes

- Four mitosome compartment independent subreview: Read-only source review of four unchanged mitosome compartment targets. Root owns issue dedup/publication, repository writes and later gates. This report does not certify future saved-head, CI or queue outcomes.
- Four mitosome compartment independent subreview: Current fresh authority metadata and complete abstracts are distinguished from two explicitly reused genuine public bodies. Reused Roger/Mi-ichi snapshots retain their actual original fetch times and checked hashes, with bounded current reinspection locators.
- Four mitosome compartment independent subreview: Tovar1999 is complete primary abstract only; the exact attributed double-membrane observation remains unverified at original-body/pixel level. Current anatomical authority and later organelle research support topology/occurrence but do not silently substitute for that unread observation.
- Four mitosome compartment independent subreview: Tachezy2022 is a complete secondary abstract plus exact bibliographic identity. Four wrong titles are certain; unread full-body mitosome coverage is unknown, not refuted. Each maintained target retains its own exact predecessor finding and action.
- Four mitosome compartment independent subreview: Mi-ichi2009 reused body was re-read only at Results sec2/sec3 and Methods sec10/sec13, including Fig1 text caption. Partial enriched-fraction proteomics, contamination/heterogeneity and strain HM-1:IMSScl6 are explicit. No source pixels, supplements or full paper are newly claimed read.
- Four mitosome compartment independent subreview: Roger2017 reused secondary PDF was re-read at R1184 opening Diversity paragraphs and R1186 reduction/mitosome comparison paragraphs (text lines630–645 and868–896). This supports qualitative diversity, not numerical frequency or new primary experiments.
- Four mitosome compartment independent subreview: All eight native protein commands pass on empty represented scopes: zero protein examples, typed molecular nodes and UniProtKB graph xrefs in all four records. This is not universal molecular or scientific certification. No optional protein inventory, family grounding or complex enum finding is invented.
- Four mitosome compartment independent subreview: Inner/outer membrane ESSENTIAL applies to the collective lipid bilayer constituent. No exact lipid species, stoichiometry, lineage-specific composition or depletion/formation requirement is measured. Label-only chemical identity is intentionally retained; whole membranes are not used as lipid groundings.
- Four mitosome compartment independent subreview: All four original adapter outcomes are genuinely not applicable to the complete physical/material assertions; their rationale is clarified without a defect. Fresh catalogue noncoverage is supplemental scope evidence, not negative biology. Historical00:49Z runner failure is not a fresh execution.
- Four mitosome compartment independent subreview: All31 actually used repository inputs were frozen before use:17 common policies/schema/scripts,4 targets,8 original artifacts and2 boundary neighbors. Whole mitosome/envelope scientific findings and grouped historical issues are not disposed by this compartment review.
- Mononeme and mucocyst independent subreview: Both assigned records are unchanged. Mononeme remains pass_with_limitations; mucocyst needs_curation for exact inherited major mucocyst-1 only. No new scientific finding or unresolved stale refresh in this slice.
- Mononeme and mucocyst independent subreview: Both originals validate/render exactly and each14 historical inputs matches retained source. No records/original bundles modified; prior history mentions do not create terminal disposition of unfrozen older reviews.
- Mononeme and mucocyst independent subreview: All declared public snapshots are fresh at their individual recorded timestamps. Guessed Singh/Rahaman S3 paths returned404; genuine matching PMC HTML fallback was inspected. Other mucocyst bodies are genuine JATS. Source-tier locators state exactly read sections.
- Mononeme and mucocyst independent subreview: No figure pixels, supplementary movies/tables, raw spectra or quantitative image reanalysis. Captions were read only as specified. No maintained image-copy/license claim exists in these targets.
- Mononeme and mucocyst independent subreview: Singh uses tagged full-length PfROM1 in3D7 and supports mature-segmenter localization/post-release redistribution. Proximity is not motor causality or universal invasion necessity. Primary mucocyst findings retain laboratory strain, tag, stimulation and biochemical preparation limits.
- Mononeme and mucocyst independent subreview: Fresh UniProt examples retain UNREVIEWED status, native names, loci and species/strain distinctions. Exact MDL1 gene-name query returned zero but exact paper-locus query resolved I7MM25; no inference of absent MDL1 biology. Wrong native I7M6L0 attribution independently confirmed by paper locus/length and PSMD4 family.
- Mononeme and mucocyst independent subreview: P90618 InterPro request returned204 with curl92 invalid HTTP/2 header and zero received body bytes; no saved body. Q2I2L7 returned429 throttling. These are inconclusive, not negative family evidence. Successful UniProt cross-references and primary support are independently described.
- Mononeme and mucocyst independent subreview: Four root native commands pass with populated inventory: mononeme1example/1covered node, mucocyst6examples/3covered nodes. Native coverage does not certify literature-gene mapping; MDD remains COVERED syntactically despite scientific identity finding.
- Mononeme and mucocyst independent subreview: Both original explicit expression-only exclusions need review coverage correction. Fresh complete catalogue contains no exact eukaryotic hosts, so no matched downstream query applies. No foreign-strain proxy or inferred negative biology. Historical00:49Z runner PermissionError is not a fresh invocation.
- Mononeme and mucocyst independent subreview: Optional exact lipid/family/complex grounding and exhaustive mature-protein inventories are not automatically mandatory defects. Native graph schema allows protein complexes/families in GENE_OR_PROTEIN; no enum-only finding.
- Mononeme and mucocyst independent subreview: Root owns full QC, issue linkage, successor authoring, final CI and merge. This report binds independent current source review and scratch native preflight only; no premature final-head/queue certification.
- Multivesicular body and three boundary compartment independent subreview: All four assigned MVB records are unchanged and independently reassessed. Exactly two inherited major exact-GO identity findings remain open with full original repository/review/F1 lineage; no new scientific finding or terminal neighbor/category disposition.
- Multivesicular body and three boundary compartment independent subreview: Katzmann2001 and Babst2002 were inspected at complete primary-abstract tier, Henne2011 at complete secondary-review abstract tier. Exact DOI HTTP200 responses are Article Locator redirects without body; publisher routes return403. An exploratory wrong Henne PII route is not used as evidence; the exact publisher URL was subsequently obtained from the DOI and independently attempted. Bounded public-search leads did not add scientific body evidence. No unread Methods, precise strain, direct scission assay or universal mechanism certified.
- Multivesicular body and three boundary compartment independent subreview: Teo2004 fresh genuine PDF was read at p559 and complete pp564-567 including Figure4-6 captions and experimental procedures; no pixels, remaining structural Results or supplements. Direct recombinant-protein and bovine-brain-liposome binding is not complete in-vivo ILV scission; Figure6 is explicitly a model. E.coli expression hosts are not maintained MVB taxonomic exemplars.
- Multivesicular body and three boundary compartment independent subreview: GO/UniProt location definitions support exact entity/topology and coarse sorting scope. Mixed is_a/part_of ancestor lists were not used to invent direct relation types; candidate is_a-only responses and typed MVB child relations were checked separately. COMMON is qualitative and no source supplies a current exhaustive prevalence census.
- Multivesicular body and three boundary compartment independent subreview: All eight current native protein commands have zero protein examples and zero GENE_OR_PROTEIN nodes. GO-grounded ESCRT STRUCTURE actors are manually authority checked. No populated molecular inventory or experimental formation necessity is inferred from empty native verification.
- Multivesicular body and three boundary compartment independent subreview: All four original adapter rows are explicit expression-only exclusions requiring corrected rationale. Fresh official catalogue has no actual Saccharomyces host coverage; no matched downstream query, bacterial surrogate or negative biology inference. Runner00:49Z failed execution remains historical; it was not repeated here.
- Multivesicular body and three boundary compartment independent subreview: Constitutive collective lipid material remains separate from an exact molecular lipid identity, source-specific composition, protein membership and assembly necessity. Optional mapping TODOs and absent unasserted fields are not themselves findings.
- Multivesicular body and three boundary compartment independent subreview: Exact GO migrations belong to separate authorized curation, retaining old local identities as deprecated with successor replaces and coordinated references. Current local sibling links resolve correctly; they are not broken links or duplicate independent findings.
- Multivesicular body and three boundary compartment independent subreview: No record, original bundle, history, scientific status or generated product was edited. Root owns globalQC, GitHub issues, final-head CI, queue and merge; this source report does not precertify later gates. Scratch native validation/render verifies format/provenance, not automatic scientific truth.
- Historical observations remain immutable; their old checks are not represented as current-head execution.
- The adapter runner was not rerun after the canary established OS access failure. Catalogue-based coverage is assessed directly; fresh and reused responses retain actual access timestamps.
- Native label checks include 923 no-adapter skips. Native identifier checks include 909 PMID transport failures and 254 skipped identifiers; bounded supplemental checks independently resolve the 909 PMIDs.
- Scientific record-curation findings stay in separate issues; no record is edited by this review PR.
- Final trusted-base post-save review-check, exact-head independent acceptance, final-head CI and merge-group CI occur after saving this immutable observation and are not represented here as already completed.
- All ten original YAML/Markdown pairs remain unchanged. Current main was merged normally and pushed without force. None of the ten target hashes differs from its original frozen input; no stale-review issue is invented.
- This explicit issue-bearing ten-record cohort follows native persistence policy. Inherited scientific findings retain stable keys and exact predecessor repository/review/finding identities; any new finding has no invented predecessor.
- Bundle issue2740 tracks the six unsupported structured-source applicability exclusions. The immutable successor addresses them and clarifies the four genuine exclusions without record changes.
- Six expression-only structured-source exclusions require correction: mononeme, mucocyst and the four MVB records make positive protein/pathway claims. All four mitosome compartments have genuine collective-material/spatial-topology scope and explicitly exclude molecular machinery. No defect is invented for those four exclusions.
- Source commit d6a41b5d3397c9d62944c9c21890ef47a097a0fa is retained by tag review-base/pr2371-current-record-followup-20261103.
- CLAUDE.md aliases AGENTS.md; canonical regular AGENTS.md bytes are frozen. Every used local context input is frozen before its assessment.
- Fresh and reused source snapshots retain actual access times and inspection tiers. Native identifier identity does not independently establish structure membership, experimental intervention scope or assembly necessity.
- All twenty native protein commands returned zero. Mononeme has one unreviewed example and one COVERED typed node; mucocyst has six unreviewed examples and three COVERED typed nodes. The other eight records have zero examples and zero typed molecular nodes. Native field correspondence does not certify the MDL1 literature-to-locus equivalence.
- Exact MVB ontology-identity findings require separately authorized identifier-preserving migration. No identifier is silently replaced, neighbor record changed or current scientific record edited in this review-only PR.
- Current CausalNode schema permits protein families and complexes as GENE_OR_PROTEIN nodes. Complex or machinery typing alone is not a scientific defect. Optional protein/chemical slots and unread-source absence are not invented findings.
- Native-validator2514 remains open and reused. Related curation issues on whole mitosome/envelope and other records do not dispose of the present child-record findings.
- Final trusted-base review-check, exact-head independent acceptance, final-head CI and merge-group CI occur after this immutable observation and are not represented as already completed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T173325Z-pr2371-current-record-followup
kind: batch
repository: CultureBotAI/CellStructureMech
title: 'PR 2371: current-input review of ten records and adversarial follow-up'
started_at: '2026-11-03T17:25:27.314718Z'
finished_at: '2026-11-03T17:33:25Z'
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
  merging main. All ten original target hashes still match; no stale review refresh
  is required. Six unsupported expression-only structured-source exclusions are corrected,
  while four mitosome compartments retain genuine physical/material-scope exclusions.
  Independent source review preserves seven inherited findings (three major and four
  minor) across seven records, with three qualified positive assessments. The MDL1
  protein example, exact MVB compartment ontology identities and four citation titles
  remain separate record-curation tasks. All original review observations and scientific
  records remain unchanged.
source:
  git_revision: d6a41b5d3397c9d62944c9c21890ef47a097a0fa
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
  - path: data/structures/membrane_organelle/mitosome.yaml
    sha256: 6c663b4b22120c931071ef1b26da5d7859ec9b98cfbda7631cda2d2425ffd59f
    role: context
  - path: data/structures/membrane_organelle/mitosome_envelope.yaml
    sha256: 762b8bad522664b480655908ccd92a258624f836a99d3e78232fe1e30aea8fc9
    role: context
  - path: data/structures/membrane_organelle/mitosome_inner_membrane.yaml
    sha256: 758c67ff3788eef18a08b4b6720e1c3a96f135d4313cb3dc7777823599f6eb35
    role: target
  - path: data/structures/membrane_organelle/mitosome_intermembrane_space.yaml
    sha256: c961b013182d3ac6fb50a2fe4af7988c95d957237c78e904142cbb7e2f88df95
    role: target
  - path: data/structures/membrane_organelle/mitosome_matrix.yaml
    sha256: cc21e220c39e8210a84b7d15251fcb85474ec75f85eafab74c8df1d4a80c3bca
    role: target
  - path: data/structures/membrane_organelle/mitosome_outer_membrane.yaml
    sha256: 8c9ed412d5d033717ea703db6c61c6960078608448a4cc6a57743a0ed37b7a58
    role: target
  - path: data/structures/membrane_organelle/mononeme.yaml
    sha256: 5e08d2090388a00b0883dd2253e8bd606d8c250a32406fb8492d6896c861a97b
    role: target
  - path: data/structures/membrane_organelle/mucocyst.yaml
    sha256: 5be0c727236d287685859cb323b9e0b109da3c26398bfe2d9adbe00f81f4b5bc
    role: target
  - path: data/structures/membrane_organelle/multivesicular_body.yaml
    sha256: cf6713b73e225eb2413a2a8b8a0fc9dfb6cf84a12f10133e3dcbec03791585a9
    role: target
  - path: data/structures/membrane_organelle/multivesicular_body_intraluminal_vesicle.yaml
    sha256: 47e5f39198c321eb8e1df58ff20ac1a0a50ec731170ae0f9d07d22b299594916
    role: target
  - path: data/structures/membrane_organelle/multivesicular_body_lumen.yaml
    sha256: 6c67050e4fa82c1a03f0476a13be57741651c0ad9e1d4bfa241ca500525175f6
    role: target
  - path: data/structures/membrane_organelle/multivesicular_body_membrane.yaml
    sha256: f4b66123e8565c11507c55cd1184da62efd23de4b37e20995a6561bee8634db7
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
  - path: reviews/structured/20261022T024026Z-mitosome-inner-membrane-audit/review.md
    sha256: 102cc6d70f093ff6250f8397b0eda9f83cc47026a84cd506507618dfd06d93ab
    role: context
  - path: reviews/structured/20261022T024026Z-mitosome-inner-membrane-audit/review.yaml
    sha256: 2bd35df6350c65035d67ce6c2ad31e502f6ffb0a4980c4aeb32af69230d6b9d4
    role: context
  - path: reviews/structured/20261022T024027Z-mitosome-intermembrane-space-audit/review.md
    sha256: a99ac1d430da065dd8eabd57d1b18c2c30f27d8ce2eb45008641690c6db4b26b
    role: context
  - path: reviews/structured/20261022T024027Z-mitosome-intermembrane-space-audit/review.yaml
    sha256: 3e530773b54dd97080b3fb1a1f5806c58099a4cfc7acf0812a4a3901dbcb7faf
    role: context
  - path: reviews/structured/20261022T024029Z-mitosome-matrix-audit/review.md
    sha256: a703c77d741cfe54f7299744a2901967be7beae7f75badaf58db8856024c0a41
    role: context
  - path: reviews/structured/20261022T024029Z-mitosome-matrix-audit/review.yaml
    sha256: 3ecf271e54308c1661ed214adbaab67205f74d21faa1c5865aebce4ec4caa4ae
    role: context
  - path: reviews/structured/20261022T024030Z-mitosome-outer-membrane-audit/review.md
    sha256: 8b19a53bb9057286e6f6cdcdb7883cc5f35647db53d0fb6a21e4cd92b2a74275
    role: context
  - path: reviews/structured/20261022T024030Z-mitosome-outer-membrane-audit/review.yaml
    sha256: 55fb0381ac49bd7b7d70b37a261a275b8a80af1ec0098391d84d2eab0c64d0cd
    role: context
  - path: reviews/structured/20261022T024031Z-mononeme-audit/review.md
    sha256: 91a2ad3229ae07cc416eedde772f0766b4392ffa55854ff618b6bdd1df9fb4f4
    role: context
  - path: reviews/structured/20261022T024031Z-mononeme-audit/review.yaml
    sha256: e2a8548a358c4f9d2583ca5f1fb339c5e92f8fae29a7010330dbb0d647d67763
    role: context
  - path: reviews/structured/20261022T024032Z-mucocyst-audit/review.md
    sha256: b6c93bb82b8815bdfa32c73d4e92742d240b0bb73614ba2cd0ae61727a2932e2
    role: context
  - path: reviews/structured/20261022T024032Z-mucocyst-audit/review.yaml
    sha256: d128a0b104d5faeb41c207478606247d680b553e20348e42953263117da7c840
    role: context
  - path: reviews/structured/20261022T024033Z-multivesicular-body-audit/review.md
    sha256: 6014963639c3685894ffd0213593500dd9041c1273d05cc01cf2b9368c8e8861
    role: context
  - path: reviews/structured/20261022T024033Z-multivesicular-body-audit/review.yaml
    sha256: 96cdd54a167f32f2f29ed7a7ff1b0d78e8c34ecadb6d19f4b951e23432c44860
    role: context
  - path: reviews/structured/20261022T024034Z-multivesicular-body-intraluminal-vesicle-audit/review.md
    sha256: fd9c211d368041d2d21a508add385eb677933ec2ed7a67620dd5741c6e6e12c8
    role: context
  - path: reviews/structured/20261022T024034Z-multivesicular-body-intraluminal-vesicle-audit/review.yaml
    sha256: 11b8f7bd8d31ca2e16838b3c6733abe9bf46c49d8725fd1fbfbc1b5be4cf00d2
    role: context
  - path: reviews/structured/20261022T024034Z-multivesicular-body-lumen-audit/review.md
    sha256: 04801bb24f071167e66686fd5a3c67fa0daaf94bcb0c875428ee416a7b460d5e
    role: context
  - path: reviews/structured/20261022T024034Z-multivesicular-body-lumen-audit/review.yaml
    sha256: fd0883112cfc6489463787c14545243c6cada41d1c8bf43377553ec72f139501
    role: context
  - path: reviews/structured/20261022T024035Z-multivesicular-body-membrane-audit/review.md
    sha256: dbc3867ee645256497b24d11ae6bce47df97f0f3a9363841293448c3005480f0
    role: context
  - path: reviews/structured/20261022T024035Z-multivesicular-body-membrane-audit/review.yaml
    sha256: 4fba3266eb4d6138c7baf8fd9dfd4a73a7e940ae2c00cffa51a94c021e62df3c
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
- target_id: cellstructuremech:mitosome_inner_membrane
  path: data/structures/membrane_organelle/mitosome_inner_membrane.yaml
  label: mitosome inner membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/mitosome_inner_membrane.yaml
    role: maintained scientific record
- target_id: cellstructuremech:mitosome_intermembrane_space
  path: data/structures/membrane_organelle/mitosome_intermembrane_space.yaml
  label: mitosome intermembrane space
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/mitosome_intermembrane_space.yaml
    role: maintained scientific record
- target_id: cellstructuremech:mitosome_matrix
  path: data/structures/membrane_organelle/mitosome_matrix.yaml
  label: mitosome matrix
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/mitosome_matrix.yaml
    role: maintained scientific record
- target_id: cellstructuremech:mitosome_outer_membrane
  path: data/structures/membrane_organelle/mitosome_outer_membrane.yaml
  label: mitosome outer membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/mitosome_outer_membrane.yaml
    role: maintained scientific record
- target_id: GO:0070074
  path: data/structures/membrane_organelle/mononeme.yaml
  label: mononeme
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/mononeme.yaml
    role: maintained scientific record
- target_id: GO:0036000
  path: data/structures/membrane_organelle/mucocyst.yaml
  label: mucocyst
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/mucocyst.yaml
    role: maintained scientific record
- target_id: GO:0005771
  path: data/structures/membrane_organelle/multivesicular_body.yaml
  label: multivesicular body
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/multivesicular_body.yaml
    role: maintained scientific record
- target_id: cellstructuremech:multivesicular_body_intraluminal_vesicle
  path: data/structures/membrane_organelle/multivesicular_body_intraluminal_vesicle.yaml
  label: multivesicular body intraluminal vesicle
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/multivesicular_body_intraluminal_vesicle.yaml
    role: maintained scientific record
- target_id: cellstructuremech:multivesicular_body_lumen
  path: data/structures/membrane_organelle/multivesicular_body_lumen.yaml
  label: multivesicular body lumen
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/multivesicular_body_lumen.yaml
    role: maintained scientific record
- target_id: GO:0032585
  path: data/structures/membrane_organelle/multivesicular_body_membrane.yaml
  label: multivesicular body membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/multivesicular_body_membrane.yaml
    role: maintained scientific record
scope:
  description: Exact ten-record PR cohort reassessed against current main a56ca22a64ab01554d81d3188c47569d0fc9b162.
    Changed inputs are substantively reassessed. Scientific records remain unchanged.
  selection: Complete cohort of ten maintained records reviewed in original PR head
    eac6f6d992414efd884ca390ba15bcfe0a7ed730.
  coverage: full
  population_size: 10
  reviewed_target_ids:
  - cellstructuremech:mitosome_inner_membrane
  - cellstructuremech:mitosome_intermembrane_space
  - cellstructuremech:mitosome_matrix
  - cellstructuremech:mitosome_outer_membrane
  - GO:0070074
  - GO:0036000
  - GO:0005771
  - cellstructuremech:multivesicular_body_intraluminal_vesicle
  - cellstructuremech:multivesicular_body_lumen
  - GO:0032585
checks:
- check_id: qc
  name: Full native QC
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitosome_inner_membrane
  - cellstructuremech:mitosome_intermembrane_space
  - cellstructuremech:mitosome_matrix
  - cellstructuremech:mitosome_outer_membrane
  - GO:0070074
  - GO:0036000
  - GO:0005771
  - cellstructuremech:multivesicular_body_intraluminal_vesicle
  - cellstructuremech:multivesicular_body_lumen
  - GO:0032585
  command: just qc
  exit_code: 0
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  scope_note: Actual local execution at main-merge head d6a41b5d3397c9d62944c9c21890ef47a097a0fa.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-qc
- check_id: labels
  name: Native label correspondence
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitosome_inner_membrane
  - cellstructuremech:mitosome_intermembrane_space
  - cellstructuremech:mitosome_matrix
  - cellstructuremech:mitosome_outer_membrane
  - GO:0070074
  - GO:0036000
  - GO:0005771
  - cellstructuremech:multivesicular_body_intraluminal_vesicle
  - cellstructuremech:multivesicular_body_lumen
  - GO:0032585
  command: just validate-products
  exit_code: 0
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  scope_note: Actual local execution at main-merge head d6a41b5d3397c9d62944c9c21890ef47a097a0fa.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-labels
- check_id: trait-links
  name: TraitMech references
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitosome_inner_membrane
  - cellstructuremech:mitosome_intermembrane_space
  - cellstructuremech:mitosome_matrix
  - cellstructuremech:mitosome_outer_membrane
  - GO:0070074
  - GO:0036000
  - GO:0005771
  - cellstructuremech:multivesicular_body_intraluminal_vesicle
  - cellstructuremech:multivesicular_body_lumen
  - GO:0032585
  command: just check-trait-links --check
  exit_code: 0
  summary: Native TraitMech link check passed.
  scope_note: Actual local execution at main-merge head d6a41b5d3397c9d62944c9c21890ef47a097a0fa.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-trait-links
- check_id: vendored
  name: Pinned governed files
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitosome_inner_membrane
  - cellstructuremech:mitosome_intermembrane_space
  - cellstructuremech:mitosome_matrix
  - cellstructuremech:mitosome_outer_membrane
  - GO:0070074
  - GO:0036000
  - GO:0005771
  - cellstructuremech:multivesicular_body_intraluminal_vesicle
  - cellstructuremech:multivesicular_body_lumen
  - GO:0032585
  command: just vendored-check
  exit_code: 0
  summary: Pinned governed files match; native vendored check passed.
  scope_note: Actual local execution at main-merge head d6a41b5d3397c9d62944c9c21890ef47a097a0fa.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-vendored
- check_id: curies
  name: Native identifier resolver
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitosome_inner_membrane
  - cellstructuremech:mitosome_intermembrane_space
  - cellstructuremech:mitosome_matrix
  - cellstructuremech:mitosome_outer_membrane
  - GO:0070074
  - GO:0036000
  - GO:0005771
  - cellstructuremech:multivesicular_body_intraluminal_vesicle
  - cellstructuremech:multivesicular_body_lumen
  - GO:0032585
  command: just check-curies
  exit_code: 0
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  scope_note: Actual local execution at main-merge head d6a41b5d3397c9d62944c9c21890ef47a097a0fa.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-curies
- check_id: focused-0
  name: validate cellstructuremech:mitosome_inner_membrane
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitosome_inner_membrane
  command: just validate data/structures/membrane_organelle/mitosome_inner_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-1
  name: validate-strict cellstructuremech:mitosome_inner_membrane
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitosome_inner_membrane
  command: just validate-strict data/structures/membrane_organelle/mitosome_inner_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-2
  name: validate cellstructuremech:mitosome_intermembrane_space
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitosome_intermembrane_space
  command: just validate data/structures/membrane_organelle/mitosome_intermembrane_space.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-3
  name: validate-strict cellstructuremech:mitosome_intermembrane_space
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitosome_intermembrane_space
  command: just validate-strict data/structures/membrane_organelle/mitosome_intermembrane_space.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-4
  name: validate cellstructuremech:mitosome_matrix
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitosome_matrix
  command: just validate data/structures/membrane_organelle/mitosome_matrix.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-5
  name: validate-strict cellstructuremech:mitosome_matrix
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitosome_matrix
  command: just validate-strict data/structures/membrane_organelle/mitosome_matrix.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-6
  name: validate cellstructuremech:mitosome_outer_membrane
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitosome_outer_membrane
  command: just validate data/structures/membrane_organelle/mitosome_outer_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-7
  name: validate-strict cellstructuremech:mitosome_outer_membrane
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitosome_outer_membrane
  command: just validate-strict data/structures/membrane_organelle/mitosome_outer_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-8
  name: validate GO:0070074
  status: passed
  required: true
  target_ids:
  - GO:0070074
  command: just validate data/structures/membrane_organelle/mononeme.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-9
  name: validate-strict GO:0070074
  status: passed
  required: true
  target_ids:
  - GO:0070074
  command: just validate-strict data/structures/membrane_organelle/mononeme.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-10
  name: validate GO:0036000
  status: passed
  required: true
  target_ids:
  - GO:0036000
  command: just validate data/structures/membrane_organelle/mucocyst.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-11
  name: validate-strict GO:0036000
  status: passed
  required: true
  target_ids:
  - GO:0036000
  command: just validate-strict data/structures/membrane_organelle/mucocyst.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-12
  name: validate GO:0005771
  status: passed
  required: true
  target_ids:
  - GO:0005771
  command: just validate data/structures/membrane_organelle/multivesicular_body.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-13
  name: validate-strict GO:0005771
  status: passed
  required: true
  target_ids:
  - GO:0005771
  command: just validate-strict data/structures/membrane_organelle/multivesicular_body.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-14
  name: validate cellstructuremech:multivesicular_body_intraluminal_vesicle
  status: passed
  required: true
  target_ids:
  - cellstructuremech:multivesicular_body_intraluminal_vesicle
  command: just validate data/structures/membrane_organelle/multivesicular_body_intraluminal_vesicle.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-15
  name: validate-strict cellstructuremech:multivesicular_body_intraluminal_vesicle
  status: passed
  required: true
  target_ids:
  - cellstructuremech:multivesicular_body_intraluminal_vesicle
  command: just validate-strict data/structures/membrane_organelle/multivesicular_body_intraluminal_vesicle.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-16
  name: validate cellstructuremech:multivesicular_body_lumen
  status: passed
  required: true
  target_ids:
  - cellstructuremech:multivesicular_body_lumen
  command: just validate data/structures/membrane_organelle/multivesicular_body_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-17
  name: validate-strict cellstructuremech:multivesicular_body_lumen
  status: passed
  required: true
  target_ids:
  - cellstructuremech:multivesicular_body_lumen
  command: just validate-strict data/structures/membrane_organelle/multivesicular_body_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-18
  name: validate GO:0032585
  status: passed
  required: true
  target_ids:
  - GO:0032585
  command: just validate data/structures/membrane_organelle/multivesicular_body_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-19
  name: validate-strict GO:0032585
  status: passed
  required: true
  target_ids:
  - GO:0032585
  command: just validate-strict data/structures/membrane_organelle/multivesicular_body_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: supplemental-pmid
  name: Supplemental bounded PMID authority checks
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitosome_inner_membrane
  - cellstructuremech:mitosome_intermembrane_space
  - cellstructuremech:mitosome_matrix
  - cellstructuremech:mitosome_outer_membrane
  - GO:0070074
  - GO:0036000
  - GO:0005771
  - cellstructuremech:multivesicular_body_intraluminal_vesicle
  - cellstructuremech:multivesicular_body_lumen
  - GO:0032585
  command: .venv/bin/python /private/tmp/cellstructure-batches-2346-2397-20261103/check_pmid_chunks.py
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371
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
  - cellstructuremech:mitosome_inner_membrane
  - cellstructuremech:mitosome_intermembrane_space
  - cellstructuremech:mitosome_matrix
  - cellstructuremech:mitosome_outer_membrane
  - GO:0070074
  - GO:0036000
  - GO:0005771
  - cellstructuremech:multivesicular_body_intraluminal_vesicle
  - cellstructuremech:multivesicular_body_lumen
  - GO:0032585
  summary: 'Six records make positive protein/pathway claims requiring source applicability
    assessment: mononeme, mucocyst and the four MVB records. Complete fresh official
    iModulonDB catalogue responses have no matching Plasmodium, Tetrahymena or Saccharomyces
    host. No unmatched host proxy or biological absence inference is used. All four
    mitosome compartments have genuine collective-material/spatial-topology scope,
    with protein/import machinery explicitly excluded; no artificial query requirement
    is imposed. Historical00:49Z runner unavailability remains historical, with actual
    current public-source fallback documented.'
  evidence_ids:
  - septin-catalogue
  - plaque-catalogue
  - micro-catalogue-api
- check_id: independent-scientific-review
  name: Independent claim-level source review
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitosome_inner_membrane
  - cellstructuremech:mitosome_intermembrane_space
  - cellstructuremech:mitosome_matrix
  - cellstructuremech:mitosome_outer_membrane
  - GO:0070074
  - GO:0036000
  - GO:0005771
  - cellstructuremech:multivesicular_body_intraluminal_vesicle
  - cellstructuremech:multivesicular_body_lumen
  - GO:0032585
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
  - septin-SL0438
  - septin-SL0439
  - septin-SL0440
  - septin-SL0441
  - septin-SL0443
  - septin-tax2759
  - septin-tax5759
  - septin-tovar1999-meta
  - septin-tachezy2022-meta
  - septin-miichi2009-pmc
  - septin-roger2017-pdf
  - plaque-policy
  - plaque-rubric
  - plaque-graph-rubric
  - plaque-protein-contract
  - plaque-schema-policy
  - plaque-go
  - plaque-GO0070074-isa
  - plaque-GO0036000-isa
  - plaque-tax5833
  - plaque-tax5911
  - plaque-tax312017
  - plaque-protein-A8IWX2
  - plaque-protein-P90618
  - plaque-protein-O76218
  - plaque-protein-O76219
  - plaque-protein-Q3S4V5
  - plaque-protein-Q2I2L7
  - plaque-protein-I7M6L0
  - plaque-protein-I7MM25
  - plaque-family-A8IWX2
  - plaque-family-O76218
  - plaque-family-O76219
  - plaque-family-Q3S4V5
  - plaque-family-I7M6L0
  - plaque-family-I7MM25
  - plaque-IPR027040
  - plaque-singh2007-meta
  - plaque-rahaman2009-meta
  - plaque-kontur2016-meta
  - plaque-kuppannan2022-meta
  - plaque-kaur2017-meta
  - plaque-singh2007-pmc
  - plaque-rahaman2009-pmc
  - plaque-kontur2016-body
  - plaque-kuppannan2022-body
  - plaque-kaur2017-body
  - plaque-catalogue
  - micro-policy
  - micro-identifier-preservation
  - micro-component-policy
  - micro-graph-policy
  - micro-go
  - micro-go-0097486-isa
  - micro-go-0097487-isa
  - micro-go-0005771-ancestors
  - micro-go-0032585-ancestors
  - micro-sl0174
  - micro-sl0175
  - micro-sl0340
  - micro-tax4932
  - micro-katzmann2001-meta
  - micro-babst2002-meta
  - micro-teo2004-meta
  - micro-henne2011-meta
  - micro-teo2004-pdf
- check_id: historical-adapter-runner
  name: Retained historical adapter runner availability
  status: unavailable
  required: false
  target_ids:
  - cellstructuremech:mitosome_inner_membrane
  - cellstructuremech:mitosome_intermembrane_space
  - cellstructuremech:mitosome_matrix
  - cellstructuremech:mitosome_outer_membrane
  - GO:0070074
  - GO:0036000
  - GO:0005771
  - cellstructuremech:multivesicular_body_intraluminal_vesicle
  - cellstructuremech:multivesicular_body_lumen
  - GO:0032585
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
- check_id: mitosome_inner_membrane-uniprot-verify
  name: Native mitosome inner membrane UniProt verify check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitosome_inner_membrane
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/mitosome_inner_membrane.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples or typed molecular
    nodes. Actual positive pathway assertions and justified physical-scope exclusions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-mitosome_inner_membrane-verify
- check_id: mitosome_inner_membrane-uniprot-causal
  name: Native mitosome inner membrane UniProt causal check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitosome_inner_membrane
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/mitosome_inner_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples or typed molecular
    nodes. Actual positive pathway assertions and justified physical-scope exclusions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-mitosome_inner_membrane-causal
- check_id: mitosome_intermembrane_space-uniprot-verify
  name: Native mitosome intermembrane space UniProt verify check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitosome_intermembrane_space
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/mitosome_intermembrane_space.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples or typed molecular
    nodes. Actual positive pathway assertions and justified physical-scope exclusions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-mitosome_intermembrane_space-verify
- check_id: mitosome_intermembrane_space-uniprot-causal
  name: Native mitosome intermembrane space UniProt causal check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitosome_intermembrane_space
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/mitosome_intermembrane_space.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples or typed molecular
    nodes. Actual positive pathway assertions and justified physical-scope exclusions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-mitosome_intermembrane_space-causal
- check_id: mitosome_matrix-uniprot-verify
  name: Native mitosome matrix UniProt verify check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitosome_matrix
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/mitosome_matrix.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples or typed molecular
    nodes. Actual positive pathway assertions and justified physical-scope exclusions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-mitosome_matrix-verify
- check_id: mitosome_matrix-uniprot-causal
  name: Native mitosome matrix UniProt causal check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitosome_matrix
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/mitosome_matrix.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples or typed molecular
    nodes. Actual positive pathway assertions and justified physical-scope exclusions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-mitosome_matrix-causal
- check_id: mitosome_outer_membrane-uniprot-verify
  name: Native mitosome outer membrane UniProt verify check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitosome_outer_membrane
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/mitosome_outer_membrane.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples or typed molecular
    nodes. Actual positive pathway assertions and justified physical-scope exclusions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-mitosome_outer_membrane-verify
- check_id: mitosome_outer_membrane-uniprot-causal
  name: Native mitosome outer membrane UniProt causal check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:mitosome_outer_membrane
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/mitosome_outer_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples or typed molecular
    nodes. Actual positive pathway assertions and justified physical-scope exclusions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-mitosome_outer_membrane-causal
- check_id: mononeme-uniprot-verify
  name: Native mononeme UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0070074
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/mononeme.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. One unreviewed A8IWX2/Rom1 example
    and one COVERED typed node. Native identity is separate from tagged-protein localization,
    secretion context and causal transport evidence.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-mononeme-verify
- check_id: mononeme-uniprot-causal
  name: Native mononeme UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0070074
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/mononeme.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. One unreviewed A8IWX2/Rom1 example
    and one COVERED typed node. Native identity is separate from tagged-protein localization,
    secretion context and causal transport evidence.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-mononeme-causal
- check_id: mucocyst-uniprot-verify
  name: Native mucocyst UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0036000
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/mucocyst.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Six unreviewed examples and three
    COVERED typed nodes. Field correspondence does not establish the MDL1 literature-to-locus
    equivalence; that inherited scientific identity finding is assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-mucocyst-verify
- check_id: mucocyst-uniprot-causal
  name: Native mucocyst UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0036000
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/mucocyst.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Six unreviewed examples and three
    COVERED typed nodes. Field correspondence does not establish the MDL1 literature-to-locus
    equivalence; that inherited scientific identity finding is assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-mucocyst-causal
- check_id: multivesicular_body-uniprot-verify
  name: Native multivesicular body UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0005771
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/multivesicular_body.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples or typed molecular
    nodes. Actual positive pathway assertions and justified physical-scope exclusions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-multivesicular_body-verify
- check_id: multivesicular_body-uniprot-causal
  name: Native multivesicular body UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0005771
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/multivesicular_body.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples or typed molecular
    nodes. Actual positive pathway assertions and justified physical-scope exclusions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-multivesicular_body-causal
- check_id: multivesicular_body_intraluminal_vesicle-uniprot-verify
  name: Native multivesicular body intraluminal vesicle UniProt verify check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:multivesicular_body_intraluminal_vesicle
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/multivesicular_body_intraluminal_vesicle.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples or typed molecular
    nodes. Actual positive pathway assertions and justified physical-scope exclusions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-multivesicular_body_intraluminal_vesicle-verify
- check_id: multivesicular_body_intraluminal_vesicle-uniprot-causal
  name: Native multivesicular body intraluminal vesicle UniProt causal check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:multivesicular_body_intraluminal_vesicle
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/multivesicular_body_intraluminal_vesicle.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples or typed molecular
    nodes. Actual positive pathway assertions and justified physical-scope exclusions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-multivesicular_body_intraluminal_vesicle-causal
- check_id: multivesicular_body_lumen-uniprot-verify
  name: Native multivesicular body lumen UniProt verify check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:multivesicular_body_lumen
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/multivesicular_body_lumen.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples or typed molecular
    nodes. Actual positive pathway assertions and justified physical-scope exclusions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-multivesicular_body_lumen-verify
- check_id: multivesicular_body_lumen-uniprot-causal
  name: Native multivesicular body lumen UniProt causal check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:multivesicular_body_lumen
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/multivesicular_body_lumen.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples or typed molecular
    nodes. Actual positive pathway assertions and justified physical-scope exclusions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-multivesicular_body_lumen-causal
- check_id: multivesicular_body_membrane-uniprot-verify
  name: Native multivesicular body membrane UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0032585
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/multivesicular_body_membrane.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples or typed molecular
    nodes. Actual positive pathway assertions and justified physical-scope exclusions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-multivesicular_body_membrane-verify
- check_id: multivesicular_body_membrane-uniprot-causal
  name: Native multivesicular body membrane UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0032585
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/multivesicular_body_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples or typed molecular
    nodes. Actual positive pathway assertions and justified physical-scope exclusions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-multivesicular_body_membrane-causal
evidence:
- evidence_id: current-record-0
  kind: record_content
  reference: data/structures/membrane_organelle/mitosome_inner_membrane.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T17:33:25Z'
  support: context_only
  summary: Original frozen SHA256 758c67ff3788eef18a08b4b6720e1c3a96f135d4313cb3dc7777823599f6eb35;
    current SHA256 758c67ff3788eef18a08b4b6720e1c3a96f135d4313cb3dc7777823599f6eb35.
    Record bytes unchanged since the original review.
  snapshot_sha256: 758c67ff3788eef18a08b4b6720e1c3a96f135d4313cb3dc7777823599f6eb35
- evidence_id: original-review-0
  kind: prior_review
  reference: reviews/structured/20261022T024026Z-mitosome-inner-membrane-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T17:33:25Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 2bd35df6350c65035d67ce6c2ad31e502f6ffb0a4980c4aeb32af69230d6b9d4
- evidence_id: current-record-1
  kind: record_content
  reference: data/structures/membrane_organelle/mitosome_intermembrane_space.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T17:33:25Z'
  support: context_only
  summary: Original frozen SHA256 c961b013182d3ac6fb50a2fe4af7988c95d957237c78e904142cbb7e2f88df95;
    current SHA256 c961b013182d3ac6fb50a2fe4af7988c95d957237c78e904142cbb7e2f88df95.
    Record bytes unchanged since the original review.
  snapshot_sha256: c961b013182d3ac6fb50a2fe4af7988c95d957237c78e904142cbb7e2f88df95
- evidence_id: original-review-1
  kind: prior_review
  reference: reviews/structured/20261022T024027Z-mitosome-intermembrane-space-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T17:33:25Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 3e530773b54dd97080b3fb1a1f5806c58099a4cfc7acf0812a4a3901dbcb7faf
- evidence_id: current-record-2
  kind: record_content
  reference: data/structures/membrane_organelle/mitosome_matrix.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T17:33:25Z'
  support: context_only
  summary: Original frozen SHA256 cc21e220c39e8210a84b7d15251fcb85474ec75f85eafab74c8df1d4a80c3bca;
    current SHA256 cc21e220c39e8210a84b7d15251fcb85474ec75f85eafab74c8df1d4a80c3bca.
    Record bytes unchanged since the original review.
  snapshot_sha256: cc21e220c39e8210a84b7d15251fcb85474ec75f85eafab74c8df1d4a80c3bca
- evidence_id: original-review-2
  kind: prior_review
  reference: reviews/structured/20261022T024029Z-mitosome-matrix-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T17:33:25Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 3ecf271e54308c1661ed214adbaab67205f74d21faa1c5865aebce4ec4caa4ae
- evidence_id: current-record-3
  kind: record_content
  reference: data/structures/membrane_organelle/mitosome_outer_membrane.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T17:33:25Z'
  support: context_only
  summary: Original frozen SHA256 8c9ed412d5d033717ea703db6c61c6960078608448a4cc6a57743a0ed37b7a58;
    current SHA256 8c9ed412d5d033717ea703db6c61c6960078608448a4cc6a57743a0ed37b7a58.
    Record bytes unchanged since the original review.
  snapshot_sha256: 8c9ed412d5d033717ea703db6c61c6960078608448a4cc6a57743a0ed37b7a58
- evidence_id: original-review-3
  kind: prior_review
  reference: reviews/structured/20261022T024030Z-mitosome-outer-membrane-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T17:33:25Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 55fb0381ac49bd7b7d70b37a261a275b8a80af1ec0098391d84d2eab0c64d0cd
- evidence_id: current-record-4
  kind: record_content
  reference: data/structures/membrane_organelle/mononeme.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T17:33:25Z'
  support: context_only
  summary: Original frozen SHA256 5e08d2090388a00b0883dd2253e8bd606d8c250a32406fb8492d6896c861a97b;
    current SHA256 5e08d2090388a00b0883dd2253e8bd606d8c250a32406fb8492d6896c861a97b.
    Record bytes unchanged since the original review.
  snapshot_sha256: 5e08d2090388a00b0883dd2253e8bd606d8c250a32406fb8492d6896c861a97b
- evidence_id: original-review-4
  kind: prior_review
  reference: reviews/structured/20261022T024031Z-mononeme-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T17:33:25Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: e2a8548a358c4f9d2583ca5f1fb339c5e92f8fae29a7010330dbb0d647d67763
- evidence_id: current-record-5
  kind: record_content
  reference: data/structures/membrane_organelle/mucocyst.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T17:33:25Z'
  support: context_only
  summary: Original frozen SHA256 5be0c727236d287685859cb323b9e0b109da3c26398bfe2d9adbe00f81f4b5bc;
    current SHA256 5be0c727236d287685859cb323b9e0b109da3c26398bfe2d9adbe00f81f4b5bc.
    Record bytes unchanged since the original review.
  snapshot_sha256: 5be0c727236d287685859cb323b9e0b109da3c26398bfe2d9adbe00f81f4b5bc
- evidence_id: original-review-5
  kind: prior_review
  reference: reviews/structured/20261022T024032Z-mucocyst-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T17:33:25Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: d128a0b104d5faeb41c207478606247d680b553e20348e42953263117da7c840
- evidence_id: current-record-6
  kind: record_content
  reference: data/structures/membrane_organelle/multivesicular_body.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T17:33:25Z'
  support: context_only
  summary: Original frozen SHA256 cf6713b73e225eb2413a2a8b8a0fc9dfb6cf84a12f10133e3dcbec03791585a9;
    current SHA256 cf6713b73e225eb2413a2a8b8a0fc9dfb6cf84a12f10133e3dcbec03791585a9.
    Record bytes unchanged since the original review.
  snapshot_sha256: cf6713b73e225eb2413a2a8b8a0fc9dfb6cf84a12f10133e3dcbec03791585a9
- evidence_id: original-review-6
  kind: prior_review
  reference: reviews/structured/20261022T024033Z-multivesicular-body-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T17:33:25Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 96cdd54a167f32f2f29ed7a7ff1b0d78e8c34ecadb6d19f4b951e23432c44860
- evidence_id: current-record-7
  kind: record_content
  reference: data/structures/membrane_organelle/multivesicular_body_intraluminal_vesicle.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T17:33:25Z'
  support: context_only
  summary: Original frozen SHA256 47e5f39198c321eb8e1df58ff20ac1a0a50ec731170ae0f9d07d22b299594916;
    current SHA256 47e5f39198c321eb8e1df58ff20ac1a0a50ec731170ae0f9d07d22b299594916.
    Record bytes unchanged since the original review.
  snapshot_sha256: 47e5f39198c321eb8e1df58ff20ac1a0a50ec731170ae0f9d07d22b299594916
- evidence_id: original-review-7
  kind: prior_review
  reference: reviews/structured/20261022T024034Z-multivesicular-body-intraluminal-vesicle-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T17:33:25Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 11b8f7bd8d31ca2e16838b3c6733abe9bf46c49d8725fd1fbfbc1b5be4cf00d2
- evidence_id: current-record-8
  kind: record_content
  reference: data/structures/membrane_organelle/multivesicular_body_lumen.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T17:33:25Z'
  support: context_only
  summary: Original frozen SHA256 6c67050e4fa82c1a03f0476a13be57741651c0ad9e1d4bfa241ca500525175f6;
    current SHA256 6c67050e4fa82c1a03f0476a13be57741651c0ad9e1d4bfa241ca500525175f6.
    Record bytes unchanged since the original review.
  snapshot_sha256: 6c67050e4fa82c1a03f0476a13be57741651c0ad9e1d4bfa241ca500525175f6
- evidence_id: original-review-8
  kind: prior_review
  reference: reviews/structured/20261022T024034Z-multivesicular-body-lumen-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T17:33:25Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: fd0883112cfc6489463787c14545243c6cada41d1c8bf43377553ec72f139501
- evidence_id: current-record-9
  kind: record_content
  reference: data/structures/membrane_organelle/multivesicular_body_membrane.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T17:33:25Z'
  support: context_only
  summary: Original frozen SHA256 f4b66123e8565c11507c55cd1184da62efd23de4b37e20995a6561bee8634db7;
    current SHA256 f4b66123e8565c11507c55cd1184da62efd23de4b37e20995a6561bee8634db7.
    Record bytes unchanged since the original review.
  snapshot_sha256: f4b66123e8565c11507c55cd1184da62efd23de4b37e20995a6561bee8634db7
- evidence_id: original-review-9
  kind: prior_review
  reference: reviews/structured/20261022T024035Z-multivesicular-body-membrane-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T17:33:25Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 4fba3266eb4d6138c7baf8fd9dfd4a73a7e940ae2c00cffa51a94c021e62df3c
- evidence_id: septin-review-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Whole-record assertions, structured sources and severity rubric
  summary: Positive molecular/pathway assertions require a real applicability assessment;
    absence of expression claims alone is not an exemption. Keep source scope, uncertainty
    and original finding identity; record curation is separate.
  accessed_at: '2026-11-03T17:29:26.226460Z'
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
  accessed_at: '2026-11-03T17:29:26.226460Z'
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
  accessed_at: '2026-11-03T17:29:26.226460Z'
  support: supports
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: septin-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Graph nodes, component correspondence, source scope and necessity
  summary: Descriptive boundary graphs can remain NONMECHANISTIC; source-specific
    localization, molecular identity and organelle-formation necessity must not be
    conflated.
  accessed_at: '2026-11-03T17:29:26.226460Z'
  support: supports
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: septin-protein-policy
  kind: authority
  reference: .claude/skills/uniprot-protein-examples/SKILL.md
  locator: Step2 generic classes and native coverage report
  summary: Generic class components are explicitly recognized. A zero-example inventory
    or NO_GENE_SYMBOLS node is a stated coverage limit, not proof that the protein
    class does not exist or that its members form one stable complex.
  accessed_at: '2026-11-03T17:29:26.226460Z'
  support: supports
  snapshot_sha256: 6462894c8257823bae2b175c34693cd42f11ff9269a3829c15b9286ba6d7c876
- evidence_id: septin-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031090,GO:0043233,GO:0032047,GO:0005737,GO:0016020
  locator: Exact five active GO identity/definition/synonym fields and selected membrane-parent
    relation
  summary: GO0031090 describes an organelle-envelope bilayer; GO0043233 describes
    innermost enclosed organelle volume. GO0016020 defines collective membrane architecture.
    GO0032047 is whole mitosome and GO0005737 cytoplasm. These support broader class/containing
    structure, not exact child identity or a particular chemical lipid.
  accessed_at: '2026-11-03T17:26:52.392860Z'
  support: supports
  snapshot_sha256: 23138598699848330059546213f80700ebaa8c7c90531275c273a47c8ee02e16
- evidence_id: septin-go-mitosome-search
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=mitosome&limit=100&page=1
  locator: Complete one-page QuickGO search result, numberOfHits1
  summary: Only whole mitosome GO0032047 is returned. None of the four exact compartment
    identities is found in this bounded term search; exact UniProt locations support
    retained local identities. This is not a claim of exhaustive ontology absence.
  accessed_at: '2026-11-03T17:27:50.811451Z'
  support: supports
  snapshot_sha256: 3b413f2fefc581c2f0b5d1787702be27a31f84097a726900996db1b64fcd2d66
  search_scope: QuickGO ontology/go/search query=mitosome, limit100,page1,no date
    filter; actual fetch 2026-11-03T17:27:50.811451Z; response numberOfHits1,totalpages1.
    Exact substring search only.
- evidence_id: septin-SL0438
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0438.json
  locator: Complete exact UniProt location JSON, including nested isA/partOf definitions
    and GO cross-references
  summary: Envelope comprises inner/outer membranes and intermembrane space; partOf
    mitosome. Protein statistics are not used as evidence of absence or inventory
    completeness. Nested parent metabolic/import prose is not automatically asserted
    by these child records.
  accessed_at: '2026-11-03T17:26:52.393133Z'
  support: supports
  snapshot_sha256: a74bbec342759e1d7c209e2d408a5dac8b077776c4a482b83b5d128d4c942895
- evidence_id: septin-SL0439
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0439.json
  locator: Complete exact UniProt location JSON, including nested isA/partOf definitions
    and GO cross-references
  summary: Exact inner membrane separates matrix and IMS; exact synonyms match. Nested
    mitosome membrane and generic membrane define lipid-bilayer constitution. Protein
    statistics are not used as evidence of absence or inventory completeness. Nested
    parent metabolic/import prose is not automatically asserted by these child records.
  accessed_at: '2026-11-03T17:26:52.393222Z'
  support: supports
  snapshot_sha256: aa08a6ef2b2463cf77e08466169f334ff002b0ed4c1aa82f85d4ff285dcf922b
- evidence_id: septin-SL0440
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0440.json
  locator: Complete exact UniProt location JSON, including nested isA/partOf definitions
    and GO cross-references
  summary: Exact IMS lies between inner/outer membranes, has all three target synonyms
    and is partOf envelope. Protein statistics are not used as evidence of absence
    or inventory completeness. Nested parent metabolic/import prose is not automatically
    asserted by these child records.
  accessed_at: '2026-11-03T17:26:52.393282Z'
  support: supports
  snapshot_sha256: d6cdb2e1eda6f4ddf5e04ba1ad05c6105be6a430a606336ed682a6edbb1d452c
- evidence_id: septin-SL0441
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0441.json
  locator: Complete exact UniProt location JSON, including nested isA/partOf definitions
    and GO cross-references
  summary: Exact matrix is enclosed by the inner membrane, has mitosomal matrix synonym
    and is partOf mitosome. Protein statistics are not used as evidence of absence
    or inventory completeness. Nested parent metabolic/import prose is not automatically
    asserted by these child records.
  accessed_at: '2026-11-03T17:26:52.393328Z'
  support: supports
  snapshot_sha256: 2e9390220f484888b3f63b14693f749d5661543f53d983c65252ecd11dda86a7
- evidence_id: septin-SL0443
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0443.json
  locator: Complete exact UniProt location JSON, including nested isA/partOf definitions
    and GO cross-references
  summary: Exact outer membrane faces cytoplasm and both target synonyms match; nested
    generic membrane definition supplies collective material context. Protein statistics
    are not used as evidence of absence or inventory completeness. Nested parent metabolic/import
    prose is not automatically asserted by these child records.
  accessed_at: '2026-11-03T17:26:53.098495Z'
  support: supports
  snapshot_sha256: c3f24e9fa67fc04328b89defb79fb3ece008eb113320b4c4f7abc99703d0b204
- evidence_id: septin-tax2759
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/2759.json
  locator: Exact complete taxonomy identity/rank/active/lineage fields
  summary: Active Eukaryota domain. Taxon identity does not establish quantitative
    prevalence, strain universality or organelle-formation experiments.
  accessed_at: '2026-11-03T17:26:53.112706Z'
  support: supports
  snapshot_sha256: af5ba762219fdecb11d214126bb8184c0eb28fc6474d14777c4aaa7f7dd89369
- evidence_id: septin-tax5759
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/5759.json
  locator: Exact complete taxonomy identity/rank/active/lineage fields
  summary: Active Entamoeba histolytica species, Amoebozoa lineage. Taxon identity
    does not establish quantitative prevalence, strain universality or organelle-formation
    experiments.
  accessed_at: '2026-11-03T17:26:53.266647Z'
  support: supports
  snapshot_sha256: c3e1193b8db9c26e67399e29fe6c58a9fd849517b36f3fc3125cd2974d635b32
- evidence_id: septin-tovar1999-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1046%2Fj.1365-2958.1999.01414.x%22&format=json&resultType=core&pageSize=25
  locator: Exact MED PMID10361303, DOI, ordered authors/year and complete abstractText
  summary: Tovar,Fischer,Clark1999 establishes Entamoeba CPN60 localization to a mitochondrial
    remnant and functional targeting-sequence deletion/replacement. The complete abstract
    does not itself demonstrate the specifically attributed double-membrane observation.
    This access limit is not refutation; full body/pixels are not claimed read.
  accessed_at: '2026-11-03T17:26:53.295790Z'
  support: supports
  snapshot_sha256: 81975611f57d50aca0999277c7307407db73c6f3f881b6df610195f241b19bc2
  search_scope: Europe PMC exact DOI:"10.1046/j.1365-2958.1999.01414.x", resultType=core,pageSize25,no
    date filter; actual fetch 2026-11-03T17:26:53.295790Z; one exact MED hit. Bibliographic
    lookup, not exhaustive literature search.
- evidence_id: septin-tachezy2022-meta
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1111%2Fjeu.12922%22&format=json&resultType=core&pageSize=25
  locator: Exact MED PMID35567536, DOI, ordered authors/year and complete secondary
    abstractText
  summary: DOI10.1111/jeu.12922 is The hydrogenosome of Trichomonas vaginalis by Tachezy,Makki,Hrdy2022.
    Complete abstract is hydrogenosome-focused; unread full body is not presumed to
    lack mitosome distribution discussion. Four target title mismatches are certain
    and retain separate exact lineage.
  accessed_at: '2026-11-03T17:26:53.348819Z'
  support: supports
  snapshot_sha256: 098a59ef5bdfce263704b01b62d4f169cd48cd17f13264bc71c552fc0bfba4d9
  search_scope: Europe PMC exact DOI:"10.1111/jeu.12922", resultType=core,pageSize25,no
    date filter; actual fetch 2026-11-03T17:26:53.348819Z; one exact MED hit. Bibliographic
    lookup, not exhaustive literature search.
- evidence_id: septin-catalogue
  kind: search
  reference: https://imodulondb.org/api/datasets
  locator: Complete official current organism/dataset catalogue
  summary: All20 organism rows inspected; no matching Entamoeba/eukaryotic host is
    represented. More fundamentally these four records assert only collective lipid
    material or spatial topology and explicitly exclude molecular machinery. No downstream
    molecular query is required; no biological absence is inferred.
  accessed_at: '2026-11-03T17:26:53.950808Z'
  support: supports
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  search_scope: GET https://imodulondb.org/api/datasets at 2026-11-03T17:26:53.950808Z;
    all20rows,28organism-dataset pairs,22distinct dataset strings; no filters or truncation.
    Inspected organism id/name/description and dataset keys, bounded Entamoeba/histolytica
    and eukaryotic-host scope. No foreign-organism proxy.
- evidence_id: septin-miichi2009-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/2799805/
  locator: Previously fetched genuine PMC body re-read in this review at Results sec2,sec3
    and Methods sec10,sec13; Fig1 caption text only
  summary: Entamoeba HM-1:IMSScl6 mitosome fractions were purified and monitored by
    Cpn60, with partial proteome/contamination/heterogeneity qualifications and immunofluorescence
    methods. This supports later organelle occurrence and bounded experimental context,
    not a direct rereading of Tovar1999 ultrastructure. No proteins/pathways from
    this source are imported into child records. Cached public snapshot reused with
    its actual original access time; no fresh fetch of this body is claimed.
  accessed_at: '2026-11-03T16:49:41.281176Z'
  support: supports
  snapshot_sha256: a9663eae9f03ad66cfd611c321a3385036b4a95ef747fa0f6a83955415dd703f
- evidence_id: septin-roger2017-pdf
  kind: authority
  reference: https://ecsolab.com/assets/pdf/roger_etal_2017.pdf
  locator: Previously fetched genuine secondary PDF re-read at R1184 opening Diversity
    paragraphs and R1186 reduction/mitosome comparison paragraphs; extracted text
    lines630–645,868–896
  summary: Review supports patchy low-oxygen eukaryotic organelle diversity and reductive
    continuum qualitatively. It is not a prevalence census or a primary formation
    experiment; unrelated lineage mechanisms are not assigned to these compartment
    records. Cached public snapshot reused with its actual original access time; no
    fresh fetch of this body is claimed.
  accessed_at: '2026-11-03T16:48:57.629957Z'
  support: supports
  snapshot_sha256: b0ddb1d89fda3d1e929ef0d65c68b15864c0e602a5736305abbb08673010982e
- evidence_id: septin-context-mitosome
  kind: record_content
  reference: data/structures/membrane_organelle/mitosome.yaml
  locator: Frozen identity/definition/source/parent/part_of/has_part/xrefs only
  summary: Boundary context was frozen before read. Exact whole/envelope identity
    and reciprocal compartment relations support local references; unrelated functions/components/findings
    are not independently reviewed or resolved here.
  accessed_at: '2026-11-03T17:29:26.226460Z'
  support: supports
  snapshot_sha256: 6c663b4b22120c931071ef1b26da5d7859ec9b98cfbda7631cda2d2425ffd59f
- evidence_id: septin-context-mitosome_envelope
  kind: record_content
  reference: data/structures/membrane_organelle/mitosome_envelope.yaml
  locator: Frozen identity/definition/source/parent/part_of/has_part/xrefs only
  summary: Boundary context was frozen before read. Exact whole/envelope identity
    and reciprocal compartment relations support local references; unrelated functions/components/findings
    are not independently reviewed or resolved here.
  accessed_at: '2026-11-03T17:29:26.226460Z'
  support: supports
  snapshot_sha256: 762b8bad522664b480655908ccd92a258624f836a99d3e78232fe1e30aea8fc9
- evidence_id: septin-adapter-runner-historical
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical attempted runner only; no fresh invocation
  summary: Actual00:49:00.848907Z–00:49:00.863225Z on2026-11-03 ended exit1 PermissionError
    reading pyvenv.cfg. This historical availability evidence is separate from fresh
    official catalogue and the four genuine scope exclusions.
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: supports
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: septin-retrieval-source-receipts
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/adversary-septin/source-receipts.json
  locator: Actual retrieval or cached-body reinspection times and exact saved hashes
  summary: Current authority requests are fresh; two previously fetched public bodies
    retain their original access timestamps and explicitly bounded reinspection scope.
    No historical failed retrieval is presented as current success.
  accessed_at: '2026-11-03T17:29:26.226460Z'
  support: supports
  snapshot_sha256: 2625cf108071ceb1cdf495fbc8b0ec7c732f56b07a061a14eb2c86910126c864
- evidence_id: septin-retrieval-additional-source-receipts
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/adversary-septin/additional-source-receipts.json
  locator: Actual retrieval or cached-body reinspection times and exact saved hashes
  summary: Current authority requests are fresh; two previously fetched public bodies
    retain their original access timestamps and explicitly bounded reinspection scope.
    No historical failed retrieval is presented as current success.
  accessed_at: '2026-11-03T17:29:26.226460Z'
  support: supports
  snapshot_sha256: 147c2f79062b022f0f89f17cae2c9cfd205f51986918ccb639423180343c28e9
- evidence_id: septin-retrieval-reused-source-receipts
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/adversary-septin/reused-source-receipts.json
  locator: Actual retrieval or cached-body reinspection times and exact saved hashes
  summary: Current authority requests are fresh; two previously fetched public bodies
    retain their original access timestamps and explicitly bounded reinspection scope.
    No historical failed retrieval is presented as current success.
  accessed_at: '2026-11-03T17:29:26.226460Z'
  support: supports
  snapshot_sha256: 6480135c34b980877d86463117650b65b67aa8a02a51b7301f3502aecbd07e0b
- evidence_id: septin-record-mitosome_inner_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/mitosome_inner_membrane.yaml
  locator: Complete current record at d6a41b5d3397c9d62944c9c21890ef47a097a0fa
  summary: Every identity,history,synonym,hierarchy,component,scope,canonical,evidence
    and complete graph field read. No protein example, gene symbol, UniProtKB xref,
    maintained image, numerical measurement, trait or verbatim snippet is asserted.
  accessed_at: '2026-11-03T17:29:26.226460Z'
  support: supports
  snapshot_sha256: 758c67ff3788eef18a08b4b6720e1c3a96f135d4313cb3dc7777823599f6eb35
- evidence_id: septin-original-mitosome_inner_membrane
  kind: prior_review
  reference: reviews/structured/20261022T024026Z-mitosome-inner-membrane-audit/review.yaml
  locator: Original YAML/Markdown scientific scope, exact findings/actions, historical
    check disclosures and limitations
  summary: Original remains immutable and its target frozen hash matches current bytes.
    Existing minor DOI-title finding is reassessed independently; historical checks
    retain historical scope.
  accessed_at: '2026-11-03T17:29:26.226460Z'
  support: supports
  snapshot_sha256: 2bd35df6350c65035d67ce6c2ad31e502f6ffb0a4980c4aeb32af69230d6b9d4
- evidence_id: septin-original-validation-mitosome_inner_membrane
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/adversary-septin/original-checks.json
  locator: Actual original native validation/render plus frozen historical source
    hash
  summary: Native validate/render exit0 and Markdown byte equality; original source
    target hash agrees with frozen/current target.
  accessed_at: '2026-11-03T17:27:08.498744Z'
  support: supports
  snapshot_sha256: b53d99d3d39798ae7b79bfbebb89f02570930d21ac2cd6cdde39f986f774dafc
- evidence_id: septin-native-mitosome_inner_membrane-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/mitosome_inner_membrane-uniprot-verify-receipt.json
  locator: Actual receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/mitosome_inner_membrane-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: Exit0. Actual record has zero protein examples, zero GENE_OR_PROTEIN nodes
    and no UniProtKB graph xrefs. Native success validates an empty represented identifier
    scope, not all biological claims or a complete molecular inventory.
  accessed_at: '2026-11-03T17:26:39.066853Z'
  support: supports
  snapshot_sha256: 19740f02dcac9e31a2911cb3b89c8bc85b1b22cc16bb3bae2ae514a0f9da1a78
- evidence_id: septin-native-mitosome_inner_membrane-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/mitosome_inner_membrane-uniprot-causal-receipt.json
  locator: Actual receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/mitosome_inner_membrane-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: Exit0. Actual record has zero protein examples, zero GENE_OR_PROTEIN nodes
    and no UniProtKB graph xrefs. Native success validates an empty represented identifier
    scope, not all biological claims or a complete molecular inventory.
  accessed_at: '2026-11-03T17:26:39.472866Z'
  support: supports
  snapshot_sha256: 63f4b0219355259280c11f5f2460d3ede071d74bf6a722ddaf50cd63d2de0546
- evidence_id: septin-record-mitosome_intermembrane_space
  kind: record_content
  reference: data/structures/membrane_organelle/mitosome_intermembrane_space.yaml
  locator: Complete current record at d6a41b5d3397c9d62944c9c21890ef47a097a0fa
  summary: Every identity,history,synonym,hierarchy,component,scope,canonical,evidence
    and complete graph field read. No protein example, gene symbol, UniProtKB xref,
    maintained image, numerical measurement, trait or verbatim snippet is asserted.
  accessed_at: '2026-11-03T17:29:26.226460Z'
  support: supports
  snapshot_sha256: c961b013182d3ac6fb50a2fe4af7988c95d957237c78e904142cbb7e2f88df95
- evidence_id: septin-original-mitosome_intermembrane_space
  kind: prior_review
  reference: reviews/structured/20261022T024027Z-mitosome-intermembrane-space-audit/review.yaml
  locator: Original YAML/Markdown scientific scope, exact findings/actions, historical
    check disclosures and limitations
  summary: Original remains immutable and its target frozen hash matches current bytes.
    Existing minor DOI-title finding is reassessed independently; historical checks
    retain historical scope.
  accessed_at: '2026-11-03T17:29:26.226460Z'
  support: supports
  snapshot_sha256: 3e530773b54dd97080b3fb1a1f5806c58099a4cfc7acf0812a4a3901dbcb7faf
- evidence_id: septin-original-validation-mitosome_intermembrane_space
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/adversary-septin/original-checks.json
  locator: Actual original native validation/render plus frozen historical source
    hash
  summary: Native validate/render exit0 and Markdown byte equality; original source
    target hash agrees with frozen/current target.
  accessed_at: '2026-11-03T17:27:09.652447Z'
  support: supports
  snapshot_sha256: b53d99d3d39798ae7b79bfbebb89f02570930d21ac2cd6cdde39f986f774dafc
- evidence_id: septin-native-mitosome_intermembrane_space-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/mitosome_intermembrane_space-uniprot-verify-receipt.json
  locator: Actual receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/mitosome_intermembrane_space-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: Exit0. Actual record has zero protein examples, zero GENE_OR_PROTEIN nodes
    and no UniProtKB graph xrefs. Native success validates an empty represented identifier
    scope, not all biological claims or a complete molecular inventory.
  accessed_at: '2026-11-03T17:26:39.881593Z'
  support: supports
  snapshot_sha256: 079014927bf5a3439db0ff30b71387410a2e61786b97c8045db1dd6a40b4b4ad
- evidence_id: septin-native-mitosome_intermembrane_space-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/mitosome_intermembrane_space-uniprot-causal-receipt.json
  locator: Actual receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/mitosome_intermembrane_space-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: Exit0. Actual record has zero protein examples, zero GENE_OR_PROTEIN nodes
    and no UniProtKB graph xrefs. Native success validates an empty represented identifier
    scope, not all biological claims or a complete molecular inventory.
  accessed_at: '2026-11-03T17:26:40.287504Z'
  support: supports
  snapshot_sha256: 176da5545eba4d7eae0380276f2a3881d1528838e9919c99c4c62b987eaa8739
- evidence_id: septin-record-mitosome_matrix
  kind: record_content
  reference: data/structures/membrane_organelle/mitosome_matrix.yaml
  locator: Complete current record at d6a41b5d3397c9d62944c9c21890ef47a097a0fa
  summary: Every identity,history,synonym,hierarchy,component,scope,canonical,evidence
    and complete graph field read. No protein example, gene symbol, UniProtKB xref,
    maintained image, numerical measurement, trait or verbatim snippet is asserted.
  accessed_at: '2026-11-03T17:29:26.226460Z'
  support: supports
  snapshot_sha256: cc21e220c39e8210a84b7d15251fcb85474ec75f85eafab74c8df1d4a80c3bca
- evidence_id: septin-original-mitosome_matrix
  kind: prior_review
  reference: reviews/structured/20261022T024029Z-mitosome-matrix-audit/review.yaml
  locator: Original YAML/Markdown scientific scope, exact findings/actions, historical
    check disclosures and limitations
  summary: Original remains immutable and its target frozen hash matches current bytes.
    Existing minor DOI-title finding is reassessed independently; historical checks
    retain historical scope.
  accessed_at: '2026-11-03T17:29:26.226460Z'
  support: supports
  snapshot_sha256: 3ecf271e54308c1661ed214adbaab67205f74d21faa1c5865aebce4ec4caa4ae
- evidence_id: septin-original-validation-mitosome_matrix
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/adversary-septin/original-checks.json
  locator: Actual original native validation/render plus frozen historical source
    hash
  summary: Native validate/render exit0 and Markdown byte equality; original source
    target hash agrees with frozen/current target.
  accessed_at: '2026-11-03T17:27:10.781831Z'
  support: supports
  snapshot_sha256: b53d99d3d39798ae7b79bfbebb89f02570930d21ac2cd6cdde39f986f774dafc
- evidence_id: septin-native-mitosome_matrix-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/mitosome_matrix-uniprot-verify-receipt.json
  locator: Actual receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/mitosome_matrix-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: Exit0. Actual record has zero protein examples, zero GENE_OR_PROTEIN nodes
    and no UniProtKB graph xrefs. Native success validates an empty represented identifier
    scope, not all biological claims or a complete molecular inventory.
  accessed_at: '2026-11-03T17:26:40.685936Z'
  support: supports
  snapshot_sha256: f44df1e9cb21734878c09b6e27be5c548640e5b0071ce3230403ca4f526739f7
- evidence_id: septin-native-mitosome_matrix-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/mitosome_matrix-uniprot-causal-receipt.json
  locator: Actual receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/mitosome_matrix-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: Exit0. Actual record has zero protein examples, zero GENE_OR_PROTEIN nodes
    and no UniProtKB graph xrefs. Native success validates an empty represented identifier
    scope, not all biological claims or a complete molecular inventory.
  accessed_at: '2026-11-03T17:26:41.102506Z'
  support: supports
  snapshot_sha256: c70ae6ea034ad71c1052f93ef2655554ee2191bf110cf15bd8b85ce516fefefc
- evidence_id: septin-record-mitosome_outer_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/mitosome_outer_membrane.yaml
  locator: Complete current record at d6a41b5d3397c9d62944c9c21890ef47a097a0fa
  summary: Every identity,history,synonym,hierarchy,component,scope,canonical,evidence
    and complete graph field read. No protein example, gene symbol, UniProtKB xref,
    maintained image, numerical measurement, trait or verbatim snippet is asserted.
  accessed_at: '2026-11-03T17:29:26.226460Z'
  support: supports
  snapshot_sha256: 8c9ed412d5d033717ea703db6c61c6960078608448a4cc6a57743a0ed37b7a58
- evidence_id: septin-original-mitosome_outer_membrane
  kind: prior_review
  reference: reviews/structured/20261022T024030Z-mitosome-outer-membrane-audit/review.yaml
  locator: Original YAML/Markdown scientific scope, exact findings/actions, historical
    check disclosures and limitations
  summary: Original remains immutable and its target frozen hash matches current bytes.
    Existing minor DOI-title finding is reassessed independently; historical checks
    retain historical scope.
  accessed_at: '2026-11-03T17:29:26.226460Z'
  support: supports
  snapshot_sha256: 55fb0381ac49bd7b7d70b37a261a275b8a80af1ec0098391d84d2eab0c64d0cd
- evidence_id: septin-original-validation-mitosome_outer_membrane
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/adversary-septin/original-checks.json
  locator: Actual original native validation/render plus frozen historical source
    hash
  summary: Native validate/render exit0 and Markdown byte equality; original source
    target hash agrees with frozen/current target.
  accessed_at: '2026-11-03T17:27:11.914384Z'
  support: supports
  snapshot_sha256: b53d99d3d39798ae7b79bfbebb89f02570930d21ac2cd6cdde39f986f774dafc
- evidence_id: septin-native-mitosome_outer_membrane-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/mitosome_outer_membrane-uniprot-verify-receipt.json
  locator: Actual receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/mitosome_outer_membrane-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: Exit0. Actual record has zero protein examples, zero GENE_OR_PROTEIN nodes
    and no UniProtKB graph xrefs. Native success validates an empty represented identifier
    scope, not all biological claims or a complete molecular inventory.
  accessed_at: '2026-11-03T17:26:41.501740Z'
  support: supports
  snapshot_sha256: 74381cfe85b9e422e47b8eac35c3729debdfa8fe02090b1c105827b787536042
- evidence_id: septin-native-mitosome_outer_membrane-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/mitosome_outer_membrane-uniprot-causal-receipt.json
  locator: Actual receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/mitosome_outer_membrane-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: Exit0. Actual record has zero protein examples, zero GENE_OR_PROTEIN nodes
    and no UniProtKB graph xrefs. Native success validates an empty represented identifier
    scope, not all biological claims or a complete molecular inventory.
  accessed_at: '2026-11-03T17:26:41.912879Z'
  support: supports
  snapshot_sha256: ba40c755335ecc1dfc641021e6933e71ed0b6859b5292a4831bc7d68748c81d8
- evidence_id: plaque-current-4
  kind: record_content
  reference: data/structures/membrane_organelle/mononeme.yaml
  locator: Entire current maintained record at d6a41b5d3397c9d62944c9c21890ef47a097a0fa,
    including components, all graphs, discussions and history
  summary: Independently read current target; bytes match the original frozen target.
    Positive and explicitly excluded claims distinguished.
  accessed_at: '2026-11-03T17:32:39.629595Z'
  support: supports
  snapshot_sha256: 5e08d2090388a00b0883dd2253e8bd606d8c250a32406fb8492d6896c861a97b
- evidence_id: plaque-original-4
  kind: prior_review
  reference: reviews/structured/20261022T024031Z-mononeme-audit/review.yaml
  locator: Exact staleness-selected original YAML plus native-rendered Markdown; full
    source/check/assessment/finding/action fields
  summary: Original pair native validation, exact Markdown rendering and all historical
    input hashes verified. Qualified pass; no original scientific finding or request-curation
    action.
  accessed_at: '2026-11-03T17:32:39.629595Z'
  support: supports
  snapshot_sha256: e2a8548a358c4f9d2583ca5f1fb339c5e92f8fae29a7010330dbb0d647d67763
- evidence_id: plaque-current-5
  kind: record_content
  reference: data/structures/membrane_organelle/mucocyst.yaml
  locator: Entire current maintained record at d6a41b5d3397c9d62944c9c21890ef47a097a0fa,
    including components, all graphs, discussions and history
  summary: Independently read current target; bytes match the original frozen target.
    Positive and explicitly excluded claims distinguished.
  accessed_at: '2026-11-03T17:32:39.629595Z'
  support: supports
  snapshot_sha256: 5be0c727236d287685859cb323b9e0b109da3c26398bfe2d9adbe00f81f4b5bc
- evidence_id: plaque-original-5
  kind: prior_review
  reference: reviews/structured/20261022T024032Z-mucocyst-audit/review.yaml
  locator: Exact staleness-selected original YAML plus native-rendered Markdown; full
    source/check/assessment/finding/action fields
  summary: Original pair native validation, exact Markdown rendering and all historical
    input hashes verified. One inherited major MDL1 identity finding remains.
  accessed_at: '2026-11-03T17:32:39.629595Z'
  support: supports
  snapshot_sha256: d128a0b104d5faeb41c207478606247d680b553e20348e42953263117da7c840
- evidence_id: plaque-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Frozen native policy, unchanged from previously read PR2370 set; structured-source
    paragraph and current enum contract reread
  summary: Native applicability includes genes, loci, accessions, proteins, pathways,
    stress and traits; expression-module absence is not sufficient exemption.
  accessed_at: '2026-11-03T17:32:39.629595Z'
  support: context_only
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: plaque-rubric
  kind: authority
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Frozen native policy, unchanged from previously read PR2370 set; structured-source
    paragraph and current enum contract reread
  summary: Exact identity, support, taxonomy, membership, necessity and mechanisms
    assessed separately; optional inventories alone are not findings.
  accessed_at: '2026-11-03T17:32:39.629595Z'
  support: context_only
  snapshot_sha256: e6b9e4b16a58c54402bed7bbee2c8b94a91d37562e8b0ee8b94ff0c829184a70
- evidence_id: plaque-graph-rubric
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Frozen native policy, unchanged from previously read PR2370 set; structured-source
    paragraph and current enum contract reread
  summary: Descriptive association, localization and biochemical mechanism are distinct;
    preserve experimental-stage/preparation scope.
  accessed_at: '2026-11-03T17:32:39.629595Z'
  support: context_only
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: plaque-protein-contract
  kind: authority
  reference: .claude/skills/uniprot-protein-examples/SKILL.md
  locator: Frozen native policy, unchanged from previously read PR2370 set; structured-source
    paragraph and current enum contract reread
  summary: Native accession/field correspondence and graph coverage cannot certify
    literature-symbol equivalence or complex membership.
  accessed_at: '2026-11-03T17:32:39.629595Z'
  support: context_only
  snapshot_sha256: 6462894c8257823bae2b175c34693cd42f11ff9269a3829c15b9286ba6d7c876
- evidence_id: plaque-schema-policy
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Frozen native policy, unchanged from previously read PR2370 set; structured-source
    paragraph and current enum contract reread
  summary: Native GENE_OR_PROTEIN permits protein families and complexes. Do not manufacture
    enum-only retyping or require every optional protein inventory.
  accessed_at: '2026-11-03T17:32:39.629595Z'
  support: context_only
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: plaque-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0070074,GO:0043231,GO:0020007,GO:0020025,GO:0020009,GO:0020008,GO:0020026,GO:0036000,GO:0030141
  locator: Complete exact nine-term response; definitions, synonyms, comments and
    typed children
  summary: Mononeme GO0070074 and mucocyst GO0036000 identities agree. Apical complex
    has direct mononeme part_of child; intracellular membrane-bounded organelle has
    mononeme is_a child. Secretory granule has mucocyst is_a child. Distinct microneme/rhoptry/dense-granule
    identities are not conflated.
  accessed_at: '2026-11-03T17:27:03.601980Z'
  support: supports
  snapshot_sha256: a470c7c64f9e59ad7d74d5739486e255b66108c208cca0d3ee20bd009a48ddf7
- evidence_id: plaque-GO0070074-isa
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0070074/ancestors?relations=is_a
  locator: Complete current exact is_a ancestor response
  summary: Mononeme has intracellular membrane-bounded organelle ancestor0043231.
    Parthood is assessed separately.
  accessed_at: '2026-11-03T17:27:03.602204Z'
  support: supports
  snapshot_sha256: 4b5e34f21313f5f219c9cd414f95f51d09a8c71ab2ab776a6a94b158a28ddd7d
- evidence_id: plaque-GO0036000-isa
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0036000/ancestors?relations=is_a
  locator: Complete current exact is_a ancestor response
  summary: Mucocyst has secretory granule ancestor0030141. Parthood is assessed separately.
  accessed_at: '2026-11-03T17:27:03.602276Z'
  support: supports
  snapshot_sha256: 75c25e5fee44723072eefe65f20dbb0dbfe49316d796ae841aa40e79d342f6f8
- evidence_id: plaque-tax5833
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5833
  locator: Complete native ENA taxon identity, rank, lineage and aliases response
  summary: 5833 resolves to Plasmodium falciparum species. Species and strain scopes
    are kept distinct; no proxy strain is silently substituted.
  accessed_at: '2026-11-03T17:27:03.602328Z'
  support: supports
  snapshot_sha256: 47c9da135299ea0515b9cbddde80166e0e7256bcf1daac4cdf87f8ae3e0ecd11
- evidence_id: plaque-tax5911
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5911
  locator: Complete native ENA taxon identity, rank, lineage and aliases response
  summary: 5911 resolves to Tetrahymena thermophila species. Species and strain scopes
    are kept distinct; no proxy strain is silently substituted.
  accessed_at: '2026-11-03T17:27:03.602387Z'
  support: supports
  snapshot_sha256: 42cc1d612d8aa31ffc6e484dfb7b846348bea7e26ca272eb4b5f4e7739df4ce6
- evidence_id: plaque-tax312017
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/312017
  locator: Complete native ENA taxon identity, rank, lineage and aliases response
  summary: 312017 resolves to Tetrahymena thermophila SB210 strain. Species and strain
    scopes are kept distinct; no proxy strain is silently substituted.
  accessed_at: '2026-11-03T17:27:03.602445Z'
  support: supports
  snapshot_sha256: a8ac4ae3d8648260b642cf92df67703bb2ce7139b41cab8a25eac34c084c9124
- evidence_id: plaque-protein-A8IWX2
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/A8IWX2.json
  locator: Complete current UniProtKB JSON; accession, entry status, native protein/gene
    names, organism, sequence length, comments and cross-references
  summary: UNREVIEWED Rhomboid-like protease, Rom1, P.falciparum5833,278 aa; native
    entry includes original sequence provenance. Rhomboid-family annotation is not
    primary evidence of mononeme localization or invasion necessity.
  accessed_at: '2026-11-03T17:27:03.602514Z'
  support: supports
  snapshot_sha256: b026eba2d5cf47d55b60367cbcc216220c91c093d30f490edba04b83b0da942c
- evidence_id: plaque-protein-P90618
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P90618.json
  locator: Complete current UniProtKB JSON; accession, entry status, native protein/gene
    names, organism, sequence length, comments and cross-references
  summary: UNREVIEWED Granule lattice protein1, GRL1, T.thermophila5911,402 aa. Correct
    species-level example; no fresh InterPro family annotation established.
  accessed_at: '2026-11-03T17:27:04.201642Z'
  support: supports
  snapshot_sha256: a9b33c5cd31d0c1f7d192c8023d6fb857d8a0505ab029652cd111ebf917da77e
- evidence_id: plaque-protein-O76218
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/O76218.json
  locator: Complete current UniProtKB JSON; accession, entry status, native protein/gene
    names, organism, sequence length, comments and cross-references
  summary: UNREVIEWED Granule lattice protein3, GRL3, T.thermophila5911,377 aa. Automated
    trichocyst/domain annotations do not replace primary mucocyst evidence.
  accessed_at: '2026-11-03T17:27:04.219432Z'
  support: supports
  snapshot_sha256: d03b9f99065aa26eea69cfc6acce67d052c343d9bce4046cbb550467f17e9283
- evidence_id: plaque-protein-O76219
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/O76219.json
  locator: Complete current UniProtKB JSON; accession, entry status, native protein/gene
    names, organism, sequence length, comments and cross-references
  summary: UNREVIEWED Granule lattice protein4, GRL4, T.thermophila5911,394 aa. Automated
    trichocyst/domain annotations do not replace primary mucocyst evidence.
  accessed_at: '2026-11-03T17:27:04.233079Z'
  support: supports
  snapshot_sha256: db84c4bc8e9c3ae3a28ab3bafce2727007084e4c951038faaff08ca77c14e5b6
- evidence_id: plaque-protein-Q3S4V5
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q3S4V5.json
  locator: Complete current UniProtKB JSON; accession, entry status, native protein/gene
    names, organism, sequence length, comments and cross-references
  summary: UNREVIEWED Granule tip protein1, GRT1, T.thermophila5911,765 aa; gamma-crystallin-like
    cross-reference. Primary cargo localization and transport are separate evidence.
  accessed_at: '2026-11-03T17:27:04.248182Z'
  support: supports
  snapshot_sha256: b52c55cede92e392659e01447354fd3eba66efbeb946b0fb1bb943889b32feeb
- evidence_id: plaque-protein-Q2I2L7
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q2I2L7.json
  locator: Complete current UniProtKB JSON; accession, entry status, native protein/gene
    names, organism, sequence length, comments and cross-references
  summary: UNREVIEWED Granule tip protein2, GRT2, T.thermophila5911,765 aa; native
    gamma-crystallin-like cross-reference is available despite throttled separate
    InterPro endpoint.
  accessed_at: '2026-11-03T17:27:04.825197Z'
  support: supports
  snapshot_sha256: c23d156270aae950e0a742a0236af0294ff288058df74758de26d3f468949e54
- evidence_id: plaque-protein-I7M6L0
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/I7M6L0.json
  locator: Complete current UniProtKB JSON; accession, entry status, native protein/gene
    names, organism, sequence length, comments and cross-references
  summary: UNREVIEWED Ubiquitin interaction motif protein, ORF TTHERM_00471830, SB210312017,392
    aa; no native primary MDL1 gene name. Automated S5A-family and PSMD4/UIM/vWFA
    cross-references conflict with its maintained MDL1 attribution.
  accessed_at: '2026-11-03T17:27:05.170589Z'
  support: supports
  snapshot_sha256: d99aff9eb1b70657ca5b9c20051187374f0dc9ef9d1c35bb283ea35aa390cbc2
- evidence_id: plaque-protein-I7MM25
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/I7MM25.json
  locator: Complete current UniProtKB JSON; accession, entry status, native protein/gene
    names, organism, sequence length, comments and cross-references
  summary: UNREVIEWED Concanavalin A-like lectin/glucanase family protein, ORF TTHERM_00658810,
    SB210312017,346 aa; exact paper-locus candidate. Native entry does not itself
    establish MDL1 nomenclature or mature-MDD membership.
  accessed_at: '2026-11-03T17:27:05.360601Z'
  support: supports
  snapshot_sha256: b3b81ed8802ff08ff64b60172915a9a1efd7c26d0e412bc4134117c84be242de
- evidence_id: plaque-family-A8IWX2
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/A8IWX2/?page_size=200
  locator: Complete InterPro protein-entry response, page_size200; all returned entries
    and their native types inspected
  summary: 'Three entries: broad S54 rhomboid family IPR002610, rhomboid domain IPR022764
    and rhomboid-like superfamily IPR035952; not an exact PfROM1-specific family or
    localization proof.'
  accessed_at: '2026-11-03T17:27:03.602550Z'
  support: supports
  snapshot_sha256: 290eeed04ceacf22690889608fe8d4085ec1bd17984fd0381c55d554d3442b95
- evidence_id: plaque-family-O76218
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/O76218/?page_size=200
  locator: Complete InterPro protein-entry response, page_size200; all returned entries
    and their native types inspected
  summary: Only IPR059991 trichocyst matrix protein T1-F coiled-coil domain returned;
    a domain annotation is not whole-GRL-cohort identity.
  accessed_at: '2026-11-03T17:27:04.230018Z'
  support: supports
  snapshot_sha256: 855db98ba4eb1656d3be53b8d50234d819d9c3c9c68db416f1c493a4c244d4c1
- evidence_id: plaque-family-O76219
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/O76219/?page_size=200
  locator: Complete InterPro protein-entry response, page_size200; all returned entries
    and their native types inspected
  summary: Only IPR059991 trichocyst matrix protein T1-F coiled-coil domain returned;
    no whole-GRL-cohort grounding inferred.
  accessed_at: '2026-11-03T17:27:04.238343Z'
  support: supports
  snapshot_sha256: 9649ec3c6bdcaa4c142e16b6a631ca5683b1cda3750b975640ceb90f2862cee4
- evidence_id: plaque-family-Q3S4V5
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q3S4V5/?page_size=200
  locator: Complete InterPro protein-entry response, page_size200; all returned entries
    and their native types inspected
  summary: IPR011024 gamma-crystallin-like homologous superfamily returned; broad
    support for declared GRT domain context, not exact family or transport evidence.
  accessed_at: '2026-11-03T17:27:04.696221Z'
  support: supports
  snapshot_sha256: 34070432c38f0256f3976d465a23f045d7d05a9f7bcfa8f33546a1294d4ef287
- evidence_id: plaque-family-I7M6L0
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/I7M6L0/?page_size=200
  locator: Complete InterPro protein-entry response, page_size200; all returned entries
    and their native types inspected
  summary: Four current entries include family IPR027040 PSMD4, UIM conserved site
    IPR003903 and vWFA domain/superfamily. Family assignment agrees with S5A/Rpn10
    identity rather than the paper MDL1 locus.
  accessed_at: '2026-11-03T17:27:05.280666Z'
  support: supports
  snapshot_sha256: 6e8aaefcd2b84d69dba8b2d955ca989382aa620dbf47f3ea28873886a0461f67
- evidence_id: plaque-family-I7MM25
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/I7MM25/?page_size=200
  locator: Complete InterPro protein-entry response, page_size200; all returned entries
    and their native types inspected
  summary: Concanavalin-A-like superfamily IPR013320 plus DUF8019 IPR058332 returned;
    no exact complete MDD-complex grounding inferred.
  accessed_at: '2026-11-03T17:27:05.500839Z'
  support: supports
  snapshot_sha256: f370719949952deaae8ae8cfce53886f76c2415ec785e8146e59598968d034b0
- evidence_id: plaque-IPR027040
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR027040/
  locator: Native entry metadata, family name, hierarchy and description
  summary: IPR027040 explicitly denotes 26S proteasome non-ATPase regulatory subunit4,
    PSMD4/S5A/Rpn10. This corroborates wrong native protein identity; no claim that
    this abstract family annotation experimentally localizes the Tetrahymena protein.
  accessed_at: '2026-11-03T17:27:05.548130Z'
  support: supports
  snapshot_sha256: 6cb491ff1bb4926fd77f4421038e6354560908630bd8327129cfb3063f937133
- evidence_id: plaque-family-P90618
  kind: validation
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P90618/?page_size=200
  locator: HTTP204 with curl exit92 invalid HTTP/2 content-length; zero saved bytes
    and no body file
  summary: Inconclusive retrieval. Empty snapshot hash represents zero received body
    bytes, not evidence that GRL1 has no family annotation.
  accessed_at: '2026-11-03T17:27:04.204728Z'
  support: context_only
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: plaque-family-Q2I2L7
  kind: validation
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q2I2L7/?page_size=200
  locator: HTTP429 JSON explicitly reports request throttling
  summary: Separate InterPro mapping was unavailable; successful current UniProt cross-reference
    is recorded separately. No negative family or biology conclusion.
  accessed_at: '2026-11-03T17:27:04.938118Z'
  support: context_only
  snapshot_sha256: 9abf9cb941ee77b8e8a3348aa3517c7fbb81c7ae7cb580ff9d1b87961335b26f
- evidence_id: plaque-query-MDL1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AMDL1+AND+taxonomy_id%3A5911&format=json&size=25
  locator: Complete bounded UniProtKB search response, size25, taxonomy scope in query
  summary: Exact MDL1 gene query returned zero; this does not refute MDL1 biology
    or imply an exhaustive alias search.
  accessed_at: '2026-11-03T17:27:06.982104Z'
  support: supports
  search_scope: UniProtKB exact encoded query https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AMDL1+AND+taxonomy_id%3A5911&format=json&size=25;
    size25 at 2026-11-03T17:27:06.982104Z; all returned entries inspected. No unrelated-host
    search, unbounded absence or biological nonexistence inferred.
  snapshot_sha256: 5021e624e752b001ce3e3846e8f158ed4aeb93a4c9a72fdb35a0c5b14a0eea84
- evidence_id: plaque-query-MDL1-locus
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ATTHERM_00658810+AND+taxonomy_id%3A5911&format=json&size=25
  locator: Complete bounded UniProtKB search response, size25, taxonomy scope in query
  summary: Exact paper locus TTHERM_00658810 returned one I7MM25 match.
  accessed_at: '2026-11-03T17:27:07.140628Z'
  support: supports
  search_scope: UniProtKB exact encoded query https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ATTHERM_00658810+AND+taxonomy_id%3A5911&format=json&size=25;
    size25 at 2026-11-03T17:27:07.140628Z; all returned entries inspected. No unrelated-host
    search, unbounded absence or biological nonexistence inferred.
  snapshot_sha256: 4f31d5f7c6bb27e5bb2e2b04b64d1d97b5614db40f300cdeeff71fbc7e5a56d6
- evidence_id: plaque-query-wrong-locus
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ATTHERM_00471830+AND+taxonomy_id%3A5911&format=json&size=25
  locator: Complete bounded UniProtKB search response, size25, taxonomy scope in query
  summary: Exact maintained locus TTHERM_00471830 returned one I7M6L0 match.
  accessed_at: '2026-11-03T17:27:07.196716Z'
  support: supports
  search_scope: UniProtKB exact encoded query https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ATTHERM_00471830+AND+taxonomy_id%3A5911&format=json&size=25;
    size25 at 2026-11-03T17:27:07.196716Z; all returned entries inspected. No unrelated-host
    search, unbounded absence or biological nonexistence inferred.
  snapshot_sha256: 533d44b61e6aad83a21ca45bb462dcee91a682f2e89f40cca79d9d5c206166e0
- evidence_id: plaque-query-Rom1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ARom1+AND+organism_id%3A5833&format=json&size=25
  locator: Complete bounded UniProtKB search response, size25, taxonomy scope in query
  summary: Exact Rom1 query returned one A8IWX2 match.
  accessed_at: '2026-11-03T17:27:07.221834Z'
  support: supports
  search_scope: UniProtKB exact encoded query https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ARom1+AND+organism_id%3A5833&format=json&size=25;
    size25 at 2026-11-03T17:27:07.221834Z; all returned entries inspected. No unrelated-host
    search, unbounded absence or biological nonexistence inferred.
  snapshot_sha256: 9f70768bb624a53318923b3fed1e7e550932f23799717bfacf88e2e84de71dc1
- evidence_id: plaque-singh2007-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1073%2Fpnas.0709999104%22&format=json&resultType=core&pageSize=25
  locator: Exact DOI metadata title, authors, year, PMID and returned PMC identity;
    not a claim to inspect every abstract or source linked from metadata
  summary: Citation identity matches the corresponding independently inspected primary
    body. Metadata is not mechanism evidence.
  accessed_at: '2026-11-03T17:27:05.620631Z'
  support: supports
  search_scope: EuropePMC exact DOI query https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1073%2Fpnas.0709999104%22&format=json&resultType=core&pageSize=25;
    pageSize25 at 2026-11-03T17:27:05.620631Z; 1 returned metadata record inspected;
    no open-ended search or automatic full-text claim.
  snapshot_sha256: ee84925a6c1eeddf58bdefed06ebb40a583da9bf9409bb2b05ef304f1a9eb2d6
- evidence_id: plaque-rahaman2009-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1128%2FEC.00151-09%22&format=json&resultType=core&pageSize=25
  locator: Exact DOI metadata title, authors, year, PMID and returned PMC identity;
    not a claim to inspect every abstract or source linked from metadata
  summary: Citation identity matches the corresponding independently inspected primary
    body. Metadata is not mechanism evidence.
  accessed_at: '2026-11-03T17:27:06.462195Z'
  support: supports
  search_scope: EuropePMC exact DOI query https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1128%2FEC.00151-09%22&format=json&resultType=core&pageSize=25;
    pageSize25 at 2026-11-03T17:27:06.462195Z; 1 returned metadata record inspected;
    no open-ended search or automatic full-text claim.
  snapshot_sha256: 9c9f6964355a708ffe17981b76fcc56ba3a89be6190dfc2d0981fb4819977ed5
- evidence_id: plaque-kontur2016-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1534%2Fg3.116.028878%22&format=json&resultType=core&pageSize=25
  locator: Exact DOI metadata title, authors, year, PMID and returned PMC identity;
    not a claim to inspect every abstract or source linked from metadata
  summary: Citation identity matches the corresponding independently inspected primary
    body. Metadata is not mechanism evidence.
  accessed_at: '2026-11-03T17:27:06.252617Z'
  support: supports
  search_scope: EuropePMC exact DOI query https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1534%2Fg3.116.028878%22&format=json&resultType=core&pageSize=25;
    pageSize25 at 2026-11-03T17:27:06.252617Z; 1 returned metadata record inspected;
    no open-ended search or automatic full-text claim.
  snapshot_sha256: d5df0deb2d7afdf8ecadfa00f37c4e85648a64d5acb6409c8d04dcdb18984d14
- evidence_id: plaque-kuppannan2022-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1371%2Fjournal.pgen.1010194%22&format=json&resultType=core&pageSize=25
  locator: Exact DOI metadata title, authors, year, PMID and returned PMC identity;
    not a claim to inspect every abstract or source linked from metadata
  summary: Citation identity matches the corresponding independently inspected primary
    body. Metadata is not mechanism evidence.
  accessed_at: '2026-11-03T17:27:06.551493Z'
  support: supports
  search_scope: EuropePMC exact DOI query https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1371%2Fjournal.pgen.1010194%22&format=json&resultType=core&pageSize=25;
    pageSize25 at 2026-11-03T17:27:06.551493Z; 1 returned metadata record inspected;
    no open-ended search or automatic full-text claim.
  snapshot_sha256: ce837814eb65c37c822f721da0206353e5e4544bd4469058f113c838ac299166
- evidence_id: plaque-kaur2017-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1091%2Fmbc.e17-01-0018%22&format=json&resultType=core&pageSize=25
  locator: Exact DOI metadata title, authors, year, PMID and returned PMC identity;
    not a claim to inspect every abstract or source linked from metadata
  summary: Citation identity matches the corresponding independently inspected primary
    body. Metadata is not mechanism evidence.
  accessed_at: '2026-11-03T17:27:06.816086Z'
  support: supports
  search_scope: EuropePMC exact DOI query https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1091%2Fmbc.e17-01-0018%22&format=json&resultType=core&pageSize=25;
    pageSize25 at 2026-11-03T17:27:06.816086Z; 1 returned metadata record inspected;
    no open-ended search or automatic full-text claim.
  snapshot_sha256: 481de5607c74fdfb2e83103b40bcd078c739569e97035bd23d7a7a38d55c4041
- evidence_id: plaque-singh2007-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2148419/
  locator: Genuine PMC2148419 HTML; title/DOI, complete Introduction, Results sections2–5,
    Discussion6, Methods8–12 and main Figure1–6 captions. No figure pixels or supplementary
    movies inspected.
  summary: Full-length 278-aa PfROM1 was episomally triple-HA tagged under its promoter
    in P.falciparum3D7. Mature segmenters show thread-like apical localization distinct
    from assayed microneme/rhoptry/dense-granule markers and near subpellicular microtubules.
    Released merozoites show surface redistribution. Confocal proximity and endpoint
    redistribution are not evidence for a specific motor/transport route, cleavage
    mechanism or universal invasion requirement. Earlier schizonts differ; the record
    preserves mature-segmenter scope.
  accessed_at: '2026-11-03T17:27:06.250579Z'
  support: supports
  snapshot_sha256: 24a962f5a61ef505197eda2161cd30fadf69d14bae4d89c6ebadd86b83b358c5
- evidence_id: plaque-rahaman2009-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2756869/
  locator: Genuine PMC2756869 HTML, verified title/DOI; text sections2,3,6,8,9,13,14,15,17,18,19
    covering culture, knockout/sorting, biochemistry and Discussion. No figure pixels,
    supplementary material or caption-level microscopy audit claimed.
  summary: CU428.1/SB281 experiments distinguish Grl proprotein heterooligomers from
    monomeric Grt cargo under the tested detergent/neutral-pH conditions. GRT1/2 double
    knockout preserves gross crystal morphology and stimulated secretion with subtler
    adhesion effects. Independent sorting is supported in the paper scope; authors
    explicitly cannot exclude other associations in wild-type/TGN conditions. No universal
    GRL/GRT formation necessity is inferred.
  accessed_at: '2026-11-03T17:27:06.544548Z'
  support: supports
  snapshot_sha256: addae5fad06fb6b2cf250c411033028c1463b590dd580af6c47c8578454519cd
- evidence_id: plaque-kontur2016-body
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4978903.1/PMC4978903.1.xml
  locator: Genuine PMC4978903.1 JATS; S2 culture/Table1 strains, S13 immunofluorescence,
    S15 fractionation, S30–33 Results and included captions. No pixels, raw fractions
    or uninspected mapping sections.
  summary: MMA1 loss blocks normal mature mucocyst accumulation and cargo processing.
    Functional induced Mma1-CFP was predominantly cytosolic with a small pelletable
    fraction and no significant mature-mucocyst colocalization; endogenous3xGFP signal
    was below detection. Supports bounded maturation/canonical-example context, not
    mature resident inventory or all-strain equivalence.
  accessed_at: '2026-11-03T17:27:06.309378Z'
  support: supports
  snapshot_sha256: f28cee3ad277ee2e444a7ecbf1aa3a2f90b9f27f2add86084adec151818fdf1c
- evidence_id: plaque-kuppannan2022-body
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC9159632.1/PMC9159632.1.xml
  locator: Genuine PMC9159632.1 JATS; Results sec003–009 including main captions,
    Methods sec011 culture, sec025 secretion assays, sec026 immunoprecipitation, sec027
    LC-MS, sec029 negative-stain TEM. No actual figure pixels, S1/S2 tables, raw spectra
    or movies.
  summary: Results sec004 explicitly defines MDL1 as TTHERM_00658810 encoding346 aa.
    Functional endogenous tagged Mdl1 polarizes before docking; loss impairs docking/secretion
    while mature crystals form. Immunoprecipitation/size fractionation and negative-stain
    EM support a putative MDD assembly with other mucocyst-associated subunits. Exact
    assembly dependencies, complete complex topology and direct fusion mechanism remain
    unresolved; predicted membrane/lipidation features are not universal biochemical
    necessities.
  accessed_at: '2026-11-03T17:27:06.754538Z'
  support: supports
  snapshot_sha256: 92e1c8b000bf932f04e79f391a9db2260fff79935ada44033e521c30965077d2
- evidence_id: plaque-kaur2017-body
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5449153.1/PMC5449153.1.xml
  locator: 'Genuine PMC5449153.1 JATS; zero-based body//sec indices6,7,11,13,15,20,21,22:
    STX7L1 late-endosomal syntaxin, immature/mature localization including Fig6 caption,
    Discussion, culture, expression and imaging/colocalization Methods. No pixels,
    supplements or complete AP3 localization audit.'
  summary: Induced Stx7l1-GFP localizes to mature and immature mucocysts in the inspected
    contexts; localization does not establish exocytic fusion machinery. Current conditional
    component-selection discussion does not deny this localization or mandate an exhaustive
    protein inventory. AP3/Stx7l1 formation/maturation claims are distinguished from
    mature resident/late-fusion necessity; no new optional-inventory defect established.
  accessed_at: '2026-11-03T17:27:06.889347Z'
  support: supports
  snapshot_sha256: bee236ff4b518c27bee30d6f099fd7babefe41a6eabd676034bf62bbc6944aed
- evidence_id: plaque-catalogue
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Complete fresh official /api/datasets response; every returned organism/dataset
    entry independently read
  summary: Catalogue has no Plasmodium, Tetrahymena or other represented eukaryotic
    host. Both targets positively name genes/proteins and secretory behavior, so applicability
    must be assessed before the bounded no-matching-host outcome. No unrelated bacterial/archaeal
    strain is a proxy and no downstream matched module query applies.
  accessed_at: '2026-11-03T17:27:07.277044Z'
  support: supports
  search_scope: Official iModulonDB complete datasets response at 2026-11-03T17:27:07.277044Z;
    all returned organism/dataset pairs inspected for the two exact species/strain
    contexts. No module prose or unbounded biological absence inference.
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: plaque-historical-runner
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical00:49Z unavailable invocation and exact retained stdout/stderr
    hashes
  summary: Historical runner failed on OS PermissionError reading pyvenv.cfg. Fresh
    official catalogue and primary/authority fallback are current source checks; no
    fresh runner attempt/success claimed.
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: plaque-original-checks
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/adversary-plaque/original-checks.json
  locator: Two original native validate/render executions, historical input and current
    target comparisons
  summary: Both original pairs validate and render exactly; each has14 matching historical
    frozen inputs and unchanged current target bytes. No original artifact edits.
  accessed_at: '2026-11-03T17:26:54.956234Z'
  support: supports
  snapshot_sha256: 69c4f4e5c6264a1488bf276f3c380556c3b176c2b925c5c7cfa10d3ed755cee3
- evidence_id: plaque-native-mononeme-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/mononeme.yaml
    --verify
  locator: Actual root receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/mononeme-uniprot-verify-receipt.json;
    exact stdoutSHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: One UNREVIEWED A8IWX2 example and one COVERED typed node. Native accession/field
    checks pass; they do not certify literature-symbol equivalence, localization or
    necessity.
  accessed_at: '2026-11-03T17:26:43.040622Z'
  support: supports
  snapshot_sha256: ad91f813649c17fd63fc8a9a5d0bbadc3fd9bf01bc4ec6119b67c89f87704130
- evidence_id: plaque-native-mononeme-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/mononeme.yaml
    --causal-graphs
  locator: Actual root receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/mononeme-uniprot-causal-receipt.json;
    exact stdoutSHA256 3781cd140b3497305c788818137907d8b5f1135ddf2cf03128e2348128267e99
  summary: One UNREVIEWED A8IWX2 example and one COVERED typed node. Native accession/field
    checks pass; they do not certify literature-symbol equivalence, localization or
    necessity.
  accessed_at: '2026-11-03T17:26:43.439055Z'
  support: supports
  snapshot_sha256: 1922c5feb1dcea5ef465ce8900f9ca42cd5a5c8baa8e47d271b1ac17dfda113c
- evidence_id: plaque-native-mucocyst-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/mucocyst.yaml
    --verify
  locator: Actual root receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/mucocyst-uniprot-verify-receipt.json;
    exact stdoutSHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: Six UNREVIEWED examples and three COVERED typed nodes; the MDD node is
    reported COVERED through I7M6L0, despite its independently confirmed wrong MDL1
    attribution. Native accession/field checks pass; they do not certify literature-symbol
    equivalence, localization or necessity.
  accessed_at: '2026-11-03T17:26:44.828473Z'
  support: supports
  snapshot_sha256: 50c2adbf5002ddeeff86f5ee74529720799e30705bacd8791a5ccddc2f2f920c
- evidence_id: plaque-native-mucocyst-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/mucocyst.yaml
    --causal-graphs
  locator: Actual root receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/mucocyst-uniprot-causal-receipt.json;
    exact stdoutSHA256 0db45fdd11cde066b43f98876b7c74196880805dda60dc3b7b92d3944b636a3e
  summary: Six UNREVIEWED examples and three COVERED typed nodes; the MDD node is
    reported COVERED through I7M6L0, despite its independently confirmed wrong MDL1
    attribution. Native accession/field checks pass; they do not certify literature-symbol
    equivalence, localization or necessity.
  accessed_at: '2026-11-03T17:26:45.233628Z'
  support: supports
  snapshot_sha256: f88b6c5675a0d57be90ee989f4019603032647b91d2d7f1282c74445a6df1833
- evidence_id: micro-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Native review skill, profile/config/output contract/checklist and AGENTS
    GO-first rule
  accessed_at: '2026-11-03T17:31:50.623514Z'
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
  summary: Actual named gene, complex and pathway claims trigger structured-source
    applicability assessment beyond expression assertions. Reviews retain original
    inputs and exact finding lineage; no record curation authorized.
  support: context_only
- evidence_id: micro-identifier-preservation
  kind: authority
  reference: docs/CURATION.md
  locator: Identifiers rules1-3 and following local-slug paragraph; schema replaces
    field
  accessed_at: '2026-11-03T17:31:50.623514Z'
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
  summary: 'An exact GO CC takes priority over a minted identifier. An existing identifier
    is not silently renamed: retain deprecated predecessor and successor replaces
    in separately authorized curation.'
  support: context_only
- evidence_id: micro-component-policy
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent391-455, replaces350-357, CausalNode845-890; native
    class/essentiality guidance
  accessed_at: '2026-11-03T17:31:50.623514Z'
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
  summary: Constituent lipid material differs from a whole membrane, assembly machinery
    and cargo; collective label-only material is permissible. Essentiality means structure
    formation, not physiological activity. Protein complexes can use STRUCTURE or
    GENE_OR_PROTEIN; no enum-only defect.
  support: context_only
- evidence_id: micro-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Complete graph contract; UniProt-example skill; verifier671-804; documented
    validate/render recipes
  accessed_at: '2026-11-03T17:31:50.623514Z'
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
  summary: Check each edge at its claimed scope; do not force transient ESCRT machinery
    into mature structure components. Native protein pass with no examples/nodes does
    not verify GO complex identities or prove biological completeness.
  support: context_only
- evidence_id: micro-record-multivesicular_body
  kind: record_content
  reference: data/structures/membrane_organelle/multivesicular_body.yaml
  locator: Entire current record, including all history/evidence/components/functions/graphs/discussions
  accessed_at: '2026-11-03T17:31:50.623514Z'
  snapshot_sha256: cf6713b73e225eb2413a2a8b8a0fc9dfb6cf84a12f10133e3dcbec03791585a9
  summary: Current target is byte-identical to the original frozen input; biological
    content was independently reassessed.
  support: supports
- evidence_id: micro-prior-multivesicular_body
  kind: prior_review
  reference: reviews/structured/20261022T024033Z-multivesicular-body-audit/review.yaml
  locator: Original review envelope, checks/evidence/assessments/findings/actions/limitations
    and exact native Markdown
  accessed_at: '2026-11-03T17:31:50.623514Z'
  snapshot_sha256: 96cdd54a167f32f2f29ed7a7ff1b0d78e8c34ecadb6d19f4b951e23432c44860
  summary: Historical pass_with_limitations; 0 scientific findings. Explicit expression-only
    adapter exclusion is present, not omitted. Historical gates and source access
    are not current execution claims.
  support: context_only
- evidence_id: micro-native-multivesicular_body-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/multivesicular_body-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/multivesicular_body.yaml
    --verify; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/multivesicular_body-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T17:26:45.636539Z'
  snapshot_sha256: 8840cdd55ebc40a2b0648802b8159df39e7da1c88ef893ed186a63d5d4bba342
  summary: Exit0 at exact source. Zero component protein examples and zero GENE_OR_PROTEIN
    nodes; GO-grounded STRUCTURE actors checked separately at GO. No molecular identity,
    localization, stoichiometry or formation necessity inferred from empty native
    coverage.
  support: supports
- evidence_id: micro-native-multivesicular_body-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/multivesicular_body-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/multivesicular_body.yaml
    --causal-graphs; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/multivesicular_body-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-03T17:26:46.042674Z'
  snapshot_sha256: 14b0eec178b265c92a4ce2979d33e46e4cd2a4c272532304c986e27280b0c32c
  summary: Exit0 at exact source. Zero component protein examples and zero GENE_OR_PROTEIN
    nodes; GO-grounded STRUCTURE actors checked separately at GO. No molecular identity,
    localization, stoichiometry or formation necessity inferred from empty native
    coverage.
  support: supports
- evidence_id: micro-record-multivesicular_body_intraluminal_vesicle
  kind: record_content
  reference: data/structures/membrane_organelle/multivesicular_body_intraluminal_vesicle.yaml
  locator: Entire current record, including all history/evidence/components/functions/graphs/discussions
  accessed_at: '2026-11-03T17:31:50.623514Z'
  snapshot_sha256: 47e5f39198c321eb8e1df58ff20ac1a0a50ec731170ae0f9d07d22b299594916
  summary: Current target is byte-identical to the original frozen input; biological
    content was independently reassessed.
  support: supports
- evidence_id: micro-prior-multivesicular_body_intraluminal_vesicle
  kind: prior_review
  reference: reviews/structured/20261022T024034Z-multivesicular-body-intraluminal-vesicle-audit/review.yaml
  locator: Original review envelope, checks/evidence/assessments/findings/actions/limitations
    and exact native Markdown
  accessed_at: '2026-11-03T17:31:50.623514Z'
  snapshot_sha256: 11b8f7bd8d31ca2e16838b3c6733abe9bf46c49d8725fd1fbfbc1b5be4cf00d2
  summary: Historical needs_curation; 1 scientific findings. Explicit expression-only
    adapter exclusion is present, not omitted. Historical gates and source access
    are not current execution claims.
  support: context_only
- evidence_id: micro-native-multivesicular_body_intraluminal_vesicle-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/multivesicular_body_intraluminal_vesicle-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/multivesicular_body_intraluminal_vesicle.yaml
    --verify; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/multivesicular_body_intraluminal_vesicle-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T17:26:46.444099Z'
  snapshot_sha256: 44fec24a6c6db224491fbbc61be8884fcc6d1f10a670c10ed24f308a0ac996ee
  summary: Exit0 at exact source. Zero component protein examples and zero GENE_OR_PROTEIN
    nodes; GO-grounded STRUCTURE actors checked separately at GO. No molecular identity,
    localization, stoichiometry or formation necessity inferred from empty native
    coverage.
  support: supports
- evidence_id: micro-native-multivesicular_body_intraluminal_vesicle-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/multivesicular_body_intraluminal_vesicle-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/multivesicular_body_intraluminal_vesicle.yaml
    --causal-graphs; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/multivesicular_body_intraluminal_vesicle-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-03T17:26:46.847843Z'
  snapshot_sha256: 27aab87fbf66545a02d1e009dfaadff5531b7579d8335255cfc8472ec225f066
  summary: Exit0 at exact source. Zero component protein examples and zero GENE_OR_PROTEIN
    nodes; GO-grounded STRUCTURE actors checked separately at GO. No molecular identity,
    localization, stoichiometry or formation necessity inferred from empty native
    coverage.
  support: supports
- evidence_id: micro-record-multivesicular_body_lumen
  kind: record_content
  reference: data/structures/membrane_organelle/multivesicular_body_lumen.yaml
  locator: Entire current record, including all history/evidence/components/functions/graphs/discussions
  accessed_at: '2026-11-03T17:31:50.623514Z'
  snapshot_sha256: 6c67050e4fa82c1a03f0476a13be57741651c0ad9e1d4bfa241ca500525175f6
  summary: Current target is byte-identical to the original frozen input; biological
    content was independently reassessed.
  support: supports
- evidence_id: micro-prior-multivesicular_body_lumen
  kind: prior_review
  reference: reviews/structured/20261022T024034Z-multivesicular-body-lumen-audit/review.yaml
  locator: Original review envelope, checks/evidence/assessments/findings/actions/limitations
    and exact native Markdown
  accessed_at: '2026-11-03T17:31:50.623514Z'
  snapshot_sha256: fd0883112cfc6489463787c14545243c6cada41d1c8bf43377553ec72f139501
  summary: Historical needs_curation; 1 scientific findings. Explicit expression-only
    adapter exclusion is present, not omitted. Historical gates and source access
    are not current execution claims.
  support: context_only
- evidence_id: micro-native-multivesicular_body_lumen-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/multivesicular_body_lumen-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/multivesicular_body_lumen.yaml
    --verify; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/multivesicular_body_lumen-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T17:26:47.246178Z'
  snapshot_sha256: 99af0cb88cdda90b8925d621048a908665a81f154f9b06efba34b38ab15a55bb
  summary: Exit0 at exact source. Zero component protein examples and zero GENE_OR_PROTEIN
    nodes; GO-grounded STRUCTURE actors checked separately at GO. No molecular identity,
    localization, stoichiometry or formation necessity inferred from empty native
    coverage.
  support: supports
- evidence_id: micro-native-multivesicular_body_lumen-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/multivesicular_body_lumen-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/multivesicular_body_lumen.yaml
    --causal-graphs; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/multivesicular_body_lumen-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-03T17:26:47.650839Z'
  snapshot_sha256: df87b40a22667d331358fe2590389b5057bed2444bc73c4cc9cc18647c2d7dab
  summary: Exit0 at exact source. Zero component protein examples and zero GENE_OR_PROTEIN
    nodes; GO-grounded STRUCTURE actors checked separately at GO. No molecular identity,
    localization, stoichiometry or formation necessity inferred from empty native
    coverage.
  support: supports
- evidence_id: micro-record-multivesicular_body_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/multivesicular_body_membrane.yaml
  locator: Entire current record, including all history/evidence/components/functions/graphs/discussions
  accessed_at: '2026-11-03T17:31:50.623514Z'
  snapshot_sha256: f4b66123e8565c11507c55cd1184da62efd23de4b37e20995a6561bee8634db7
  summary: Current target is byte-identical to the original frozen input; biological
    content was independently reassessed.
  support: supports
- evidence_id: micro-prior-multivesicular_body_membrane
  kind: prior_review
  reference: reviews/structured/20261022T024035Z-multivesicular-body-membrane-audit/review.yaml
  locator: Original review envelope, checks/evidence/assessments/findings/actions/limitations
    and exact native Markdown
  accessed_at: '2026-11-03T17:31:50.623514Z'
  snapshot_sha256: 4fba3266eb4d6138c7baf8fd9dfd4a73a7e940ae2c00cffa51a94c021e62df3c
  summary: Historical pass_with_limitations; 0 scientific findings. Explicit expression-only
    adapter exclusion is present, not omitted. Historical gates and source access
    are not current execution claims.
  support: context_only
- evidence_id: micro-native-multivesicular_body_membrane-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/multivesicular_body_membrane-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/multivesicular_body_membrane.yaml
    --verify; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/multivesicular_body_membrane-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T17:26:48.046807Z'
  snapshot_sha256: 6fa17628b3f9fb6a024d395d2319b1c4b97e4e44f1f6d731c0778224fb88f54b
  summary: Exit0 at exact source. Zero component protein examples and zero GENE_OR_PROTEIN
    nodes; GO-grounded STRUCTURE actors checked separately at GO. No molecular identity,
    localization, stoichiometry or formation necessity inferred from empty native
    coverage.
  support: supports
- evidence_id: micro-native-multivesicular_body_membrane-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/multivesicular_body_membrane-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/multivesicular_body_membrane.yaml
    --causal-graphs; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/multivesicular_body_membrane-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-03T17:26:48.438810Z'
  snapshot_sha256: f84dc399c613f8c4c4e4b3fd70963b06141aaceb60e7f8039b9833ff7a757e8f
  summary: Exit0 at exact source. Zero component protein examples and zero GENE_OR_PROTEIN
    nodes; GO-grounded STRUCTURE actors checked separately at GO. No molecular identity,
    localization, stoichiometry or formation necessity inferred from empty native
    coverage.
  support: supports
- evidence_id: micro-original-pairs
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/adversary-microtubule/original-checks.json
  locator: Actual four native validate and four render --content commands; all Markdown
    exact
  accessed_at: '2026-11-03T17:28:34.531924Z'
  snapshot_sha256: e659679643d1515e9ed171eac8d82d72c76439acdc517aede18530e1e1d38e55
  summary: All original four pairs pass validation and exact deterministic rendering.
  support: supports
- evidence_id: micro-original-inputs
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/adversary-microtubule/original-frozen-inputs.json
  locator: All76 original input entries checked against original retained source revisions
  accessed_at: '2026-11-03T17:31:50.623514Z'
  snapshot_sha256: aa2755c937363e80e41f9cd364930dd5c5e12ce6993d9895daa3ddd90a8ae06f
  summary: Every original target and context hash verifies; all four current target
    hashes remain unchanged. Historical context hashing is provenance checking, not
    renewed scientific assessment of those unfrozen neighboring records.
  support: supports
- evidence_id: micro-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005771,GO:0097487,GO:0097486,GO:0032585,GO:0031904,GO:0010008,GO:0031982,GO:0005770,GO:0071985,GO:0000813,GO:0000814,GO:0000815
  locator: All12 returned active term identities, definitions, synonyms and typed
    child relations
  accessed_at: '2026-11-03T17:27:21.184690Z'
  snapshot_sha256: f6d4b3b3b12ee285881cdb3343cd2d4a2a8198622db50d848a551104577d24d4
  summary: Exact wholeMVB0005771, limiting membrane0032585, sorting0071985 and ESCRT0813/0814/0815
    definitions agree. Active0097487 is a membrane-bounded vesicle wholly inside MVB;0097486
    is the outermost-membrane enclosed lumen. WholeMVB lists both as part_of children;
    lateendosome5770 lists MVB as is_a child.
  support: supports
- evidence_id: micro-go-0097486-isa
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097486/ancestors?relations=is_a
  locator: Complete relations=is_a ancestor list; not all listed ancestors are immediate
    parents
  accessed_at: '2026-11-03T17:28:03.281265Z'
  snapshot_sha256: 9b3762e8a4119f40aa8d5fbc8358250b835e8b5ff846bbcc30c7bad1f0b5a619
  summary: The exact candidate has the declared broader ancestry:0097486 under endosome
    lumen0031904;0097487 under vesicle0031982. Combined with exact definition and
    typed MVB parthood this establishes biological equivalence, not a label-only match.
  support: supports
- evidence_id: micro-go-0097487-isa
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097487/ancestors?relations=is_a
  locator: Complete relations=is_a ancestor list; not all listed ancestors are immediate
    parents
  accessed_at: '2026-11-03T17:28:03.349112Z'
  snapshot_sha256: 0f0753c1eebce7ee85ab62017314041b224e5b9a0a20b72c71c9eada7a69b40c
  summary: The exact candidate has the declared broader ancestry:0097486 under endosome
    lumen0031904;0097487 under vesicle0031982. Combined with exact definition and
    typed MVB parthood this establishes biological equivalence, not a label-only match.
  support: supports
- evidence_id: micro-go-0005771-ancestors
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005771/ancestors?relations=is_a,part_of
  locator: Complete relations=is_a,part_of mixed ancestor list; relation types not
    inferred from flat results
  accessed_at: '2026-11-03T17:27:21.185175Z'
  snapshot_sha256: a75abdfd308e4b4067ac3b9cd6cede7a0a8c77f534cef57fdb6dc7f95367e35e
  summary: Mixed hierarchy/parthood response corroborates containing context; direct
    parent relation claims rely on separately typed GO child relations or SL isA/partOf
    objects, not untyped ancestor membership.
  support: supports
- evidence_id: micro-go-0032585-ancestors
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032585/ancestors?relations=is_a,part_of
  locator: Complete relations=is_a,part_of mixed ancestor list; relation types not
    inferred from flat results
  accessed_at: '2026-11-03T17:27:21.185108Z'
  snapshot_sha256: a41ba8e11ba380963dbdfb01bbef09685b257eddf9b1d7f3dbd3b926cd649183
  summary: Mixed hierarchy/parthood response corroborates containing context; direct
    parent relation claims rely on separately typed GO child relations or SL isA/partOf
    objects, not untyped ancestor membership.
  support: supports
- evidence_id: micro-sl0174
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0174.json
  locator: Complete exact location identity, five maintained synonyms, direct isA/partOf
    and GO links; nested entries read as boundary context
  accessed_at: '2026-11-03T17:27:21.185225Z'
  snapshot_sha256: 8052073d7abddf51eeec63cfcb269be2bd66c8811719dddbcce96da3ae469329
  summary: SL0174 matches whole MVB and late-endosome classification. Protein counts
    are not complete component inventories or proof of stable membership.
  support: supports
- evidence_id: micro-sl0175
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0175.json
  locator: Complete exact location identity, five maintained synonyms, direct isA/partOf
    and GO links; nested entries read as boundary context
  accessed_at: '2026-11-03T17:27:21.778764Z'
  snapshot_sha256: edbdb71c1abf69e1d5b60336733b967a335566cc9dedc94608bc600aa0ebea31
  summary: SL0175 matches limiting MVB membrane, endosome-membrane parent and wholeMVB
    parthood. Protein counts are not complete component inventories or proof of stable
    membership.
  support: supports
- evidence_id: micro-sl0340
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0340.json
  locator: Complete exact location identity, five maintained synonyms, direct isA/partOf
    and GO links; nested entries read as boundary context
  accessed_at: '2026-11-03T17:27:21.778873Z'
  snapshot_sha256: 8e50a2ed2c762cf87ee99c3fdc6742225f4e9669f81b50640f776066000860ad
  summary: SL0340 matches outer MVB lumen, endosome-lumen parent and wholeMVB parthood;
    not the inside of an individual ILV. Protein counts are not complete component
    inventories or proof of stable membership.
  support: supports
- evidence_id: micro-tax4932
  kind: database
  reference: https://rest.uniprot.org/taxonomy/4932.json
  locator: taxonId, scientificName, rank and complete lineage
  accessed_at: '2026-11-03T17:27:21.787511Z'
  snapshot_sha256: 963bbf3503fd0aa9e69dc25b64c5ae903f871991b37c4c593353b945c8e31688
  summary: 4932 confirms Saccharomyces cerevisiae at species rank. Does not establish
    a particular experimental strain or frequency of MVBs in every culture.
  support: supports
- evidence_id: micro-katzmann2001-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11511343%20AND%20SRC%3AMED&format=json&resultType=core&pageSize=20
  locator: Exact PMID or quoted DOI core search, pageSize20; unique MED identity/title/authors/year
    and complete abstract
  accessed_at: '2026-11-03T17:27:21.863917Z'
  snapshot_sha256: 398c67b9988fa63427850773ae65a85abcced545d9852ed30a3c64d75bdf7681
  summary: 'Primary PMID11511343/DOI10.1016/S0092-8674(01)00434-2: ubiquitination
    as sorting signal and ESCRT-I cargo recognition/function in MVB sorting; yeast/mammalian
    conservation proposed. No unread Methods, exact strain or specific scission assay
    certified.'
  support: supports
- evidence_id: micro-babst2002-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12194857%20AND%20SRC%3AMED&format=json&resultType=core&pageSize=20
  locator: Exact PMID or quoted DOI core search, pageSize20; unique MED identity/title/authors/year
    and complete abstract
  accessed_at: '2026-11-03T17:27:21.920510Z'
  snapshot_sha256: 1d01a7e0647138f52d40caf229ae7c36c02fd517f23c0f39e2e4fce2cd5d5634
  summary: 'Primary PMID12194857/DOI10.1016/S1534-5807(02)00220-4: cytosolic ESCRT-III
    proteins recruit/oligomerize at endosomal membranes, Vps20-Snf7/Vps2-Vps24 functional
    organization and cargo sorting/concentration. Abstract is not a direct scission-reconstitution
    experiment.'
  support: supports
- evidence_id: micro-teo2004-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016/j.devcel.2004.09.003%22&format=json&resultType=core&pageSize=20
  locator: Exact PMID or quoted DOI core search, pageSize20; unique MED identity/title/authors/year
    and complete abstract
  accessed_at: '2026-11-03T17:27:21.986751Z'
  snapshot_sha256: 3f2e7bda38e7a96c2d75ad53d38ae5edb50927881f8c0863b2e88628e249d9ed
  summary: 'Primary PMID15469844/DOI10.1016/j.devcel.2004.09.003 matches genuine PDF:
    purified ESCRT-II directly binds Vps20 chiefly via Vps25 and increases both proteins
    membrane association in vitro.'
  support: supports
- evidence_id: micro-henne2011-meta
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016/j.devcel.2011.05.015%22&format=json&resultType=core&pageSize=20
  locator: Exact PMID or quoted DOI core search, pageSize20; unique MED identity/title/authors/year
    and complete abstract
  accessed_at: '2026-11-03T17:27:22.357299Z'
  snapshot_sha256: ee8364cd8d7b246bf132110d25b53170783d004d9714e9d8e634bd696a5b80e9
  summary: 'Secondary review PMID21763610/DOI10.1016/j.devcel.2011.05.015: cargo-recognition/membrane-sculpting
    ESCRT pathway and MVB delivery to vacuole/lysosome. Abstract-only synthesis, not
    an independently read experimental body.'
  support: context_only
- evidence_id: micro-teo2004-pdf
  kind: primary_source
  reference: https://www2.mrc-lmb.cam.ac.uk/groups/rlw/download/publications/15469844.pdf
  locator: Printed p559 title/summary/Introduction; complete pp564-567 including Results,
    Conclusions, Figure4-6 captions and Experimental Procedures; no figure pixels,
    remaining structural Results or supplements
  accessed_at: '2026-11-03T17:28:03.281040Z'
  snapshot_sha256: 9a62830da92c7a92939524b134a277cf6381382e5539dfdfb47ab58e22817dce
  summary: Direct purified ESCRT-II/Vps20 binding chiefly through Vps25 and enhanced
    binding to bovine-brain-lipid liposomes support the coarse recruitment edge. S.cerevisiae
    genes cloned from ATCC9763D DNA and expressed in E.coli C41/B834; these expression
    hosts are not biological MVB exemplars or matching transcriptomic proxies. Figure6
    is explicitly a model; this is not complete in-vivo ILV scission or a universal
    lipid-composition assay.
  support: supports
- evidence_id: micro-katzmann2001-access
  kind: validation
  reference: https://doi.org/10.1016/S0092-8674(01)00434-2
  locator: Exact DOI redirects to Elsevier Article Locator; inspected HTTP200 HTML
    has redirect metadata but no body
  accessed_at: '2026-11-03T17:29:39.117014Z'
  snapshot_sha256: 224144c18b49b032d4f0bed0f44a6c4e0c8e138cc9ac6eb705fcce976f4c8dab
  summary: DOI resolves, but response is not full text. Cell fulltext route returned403.
    Complete native abstract remains the inspected tier.
  support: context_only
- evidence_id: micro-babst2002-access
  kind: validation
  reference: https://doi.org/10.1016/S1534-5807(02)00220-4
  locator: Exact DOI redirects to Elsevier Article Locator; inspected HTTP200 HTML
    has redirect metadata but no body
  accessed_at: '2026-11-03T17:29:39.117104Z'
  snapshot_sha256: 9682cc6c46ab54a0d0722013ee2980e469623e649887249044d76a0bf9a68c55
  summary: DOI resolves, but response is not full text. Indexed Cell PDF route returned403.
    Complete native abstract remains the inspected tier.
  support: context_only
- evidence_id: micro-henne2011-access
  kind: validation
  reference: https://doi.org/10.1016/j.devcel.2011.05.015
  locator: Exact DOI redirects to Elsevier Article Locator; inspected HTTP200 HTML
    has redirect metadata but no body
  accessed_at: '2026-11-03T17:29:39.116710Z'
  snapshot_sha256: 7183966d5c99dad16300bd3a39e3b777bf88d697c00663b59deb2959b84ce7d6
  summary: DOI resolves, but response is not full text. Exact Cell publisher https://www.cell.com/developmental-cell/retrieve/pii/S1534580711002073
    returned403. Complete native abstract remains the inspected tier.
  support: context_only
- evidence_id: micro-local-identity-search
  kind: search
  reference: 'rg -n --no-ignore --hidden -g *.yaml GO:0097486|GO:0097487|^identifier:
    cellstructuremech:multivesicular_body_(lumen|intraluminal_vesicle)$ data/structures'
  locator: Complete ignored-inclusive maintained data/structures YAML search; output
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/adversary-microtubule/identity-search.log
  accessed_at: '2026-11-03T17:28:29.279558Z'
  snapshot_sha256: 62eddb42d43b6e8586b6a0d38448c9edd1272be0f78e0af65026828ba94b83d2
  summary: Each local target identifier occurs in its one maintained record; no GO0097486/0097487
    occurrence in this bounded complete corpus search. Existing local links remain
    valid; no broken-reference finding assigned to sibling records.
  support: supports
  search_scope: 'At 2026-11-03T17:28:29.279558Z, rg -n --no-ignore --hidden -g *.yaml
    over data/structures; regex GO:0097486|GO:0097487|^identifier: cellstructuremech:multivesicular_body_(lumen|intraluminal_vesicle)$.
    Includes ignored and hidden files; complete output with no truncation/pagination;
    maintained corpus only, not entire Git history or internet.'
- evidence_id: micro-catalogue-api
  kind: search
  reference: https://imodulondb.org/api/datasets
  locator: Complete official array, all20 organism rows/28 organism-dataset pairs
  accessed_at: '2026-11-03T17:28:03.280729Z'
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  summary: No Saccharomyces/yeast or ATCC9763D host dataset is represented. No matched
    downstream search/summary or bacterial-expression-host surrogate is warranted;
    noncoverage is not evidence against ESCRT biology.
  support: supports
  search_scope: Official iModulonDB /api/datasets at 2026-11-03T17:28:03.280729Z;
    complete20 organism rows/28 organism-dataset pairs, no pagination. Inspected all
    names/keys/dataset keys and exact Saccharomyces/cerevisiae/yeast/ATCC9763D strings.
    No genome-wide or expression-negative conclusion.
- evidence_id: micro-historical-runner
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical00:49Z attempted dataset command and PermissionError reading
    pyvenv.cfg
  accessed_at: '2026-11-03T00:49:00.863225Z'
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  summary: Actual historical optional runner exit1/unavailable. Not rerun or relabeled
    as current execution; current official catalogue is a separate successful fallback.
  support: context_only
- evidence_id: check-qc
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/qc.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T17:31:38.196313Z'
  support: supports
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  snapshot_sha256: bccaf322fcc95de8a56a058118900233cddf32185c3bd237d3e04fac1a54231a
- evidence_id: check-labels
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/labels.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T17:27:30.704532Z'
  support: supports
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  snapshot_sha256: 6cdfb05df9a27194f05a5fd7f851783f817ac1523ca0bbfa54fe0e0d18775905
- evidence_id: check-trait-links
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/trait-links.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T17:27:11.522119Z'
  support: supports
  summary: Native TraitMech link check passed.
  snapshot_sha256: 8b336cdefbbd3daf6da8787990efdbe346c95e2c8361d50b7eb68a18f2d5a44a
- evidence_id: check-vendored
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/vendored.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T17:27:13.377476Z'
  support: supports
  summary: Pinned governed files match; native vendored check passed.
  snapshot_sha256: b1f169d103aaefa930745468bcca171e5867b9cc49e4e74311e458097e3252a6
- evidence_id: check-curies
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/curies.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T17:26:42.951816Z'
  support: supports
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  snapshot_sha256: bc12b1285f5747707643f7a98e03dbb3a6c88fb062ad49f99db9cb42ececf3d2
- evidence_id: focused
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/focused-results.json
  locator: All twenty actual target schema/strict command outputs
  accessed_at: '2026-11-03T17:33:25Z'
  support: supports
  summary: Ten schema and ten strict commands returned exit zero.
  snapshot_sha256: 779ca7c6b5e013614b0a379b1ba9d1c5ed8030ab88a412e664f460ba4f078a5e
- evidence_id: supplemental-pmid
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2371/pmid-chunks-receipt.json
  locator: Complete native-report PMID set checked with unchanged resolver in batches
    of at most fifty
  accessed_at: '2026-11-03T17:28:08.562045Z'
  support: supports
  summary: 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers
    remain unverified.
  snapshot_sha256: 78d3203bfec3282cb457dab67854dd6031740f9cc7f6e87a284ba34477dacb28
- evidence_id: historical-adapter-runner-availability
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical runner invocation receipt, exact SHA256 reverified during PR2371
    synthesis
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  summary: Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS
    PermissionError reading the configured runner pyvenv.cfg. This is a retained historical
    availability observation, not a fresh attempt or a scientific validation failure.
    Native policy permits inspected source-catalogue fallback.
assessments:
- assessment_id: septin-mitosome_inner_membrane-schema
  area: schema
  topic: Original native schema/render and unchanged frozen input
  outcome: supported
  summary: Original validate/render pass, Markdown exact and historical target hash
    matches current bytes. None of these four targets is stale. A schema pass is not
    a biological verdict.
  target_ids:
  - cellstructuremech:mitosome_inner_membrane
  evidence_ids:
  - septin-record-mitosome_inner_membrane
  - septin-original-validation-mitosome_inner_membrane
- assessment_id: septin-mitosome_inner_membrane-identity
  area: identity
  topic: Exact compartment identity, synonyms and broader classes
  outcome: supported
  summary: Exact SL0439 definition and both synonyms match; GO0031090 is a suitable
    broader organelle membrane, while envelope is part_of. Bounded GO search returns
    whole mitosome only; exact local identities are retained without guessing chemical
    identifiers.
  target_ids:
  - cellstructuremech:mitosome_inner_membrane
  evidence_ids:
  - septin-record-mitosome_inner_membrane
  - septin-SL0439
  - septin-go
  - septin-go-mitosome-search
  - septin-context-mitosome
  - septin-context-mitosome_envelope
- assessment_id: septin-mitosome_inner_membrane-taxa
  area: scope
  topic: Taxon identities and qualitative occurrence
  outcome: supported
  summary: Eukaryota2759 and Entamoeba histolytica5759 match native authority. Tovar
    primary abstract establishes the mitochondrial remnant by localization/targeting;
    later Mi-ichi purification/IF supports organelle occurrence in HM-1:IMSScl6. Roger
    review supports qualitative patchy low-oxygen eukaryotic context, not numeric
    prevalence or every-strain coverage.
  target_ids:
  - cellstructuremech:mitosome_inner_membrane
  evidence_ids:
  - septin-record-mitosome_inner_membrane
  - septin-tax2759
  - septin-tax5759
  - septin-tovar1999-meta
  - septin-miichi2009-pmc
  - septin-roger2017-pdf
- assessment_id: septin-mitosome_inner_membrane-attribution-limits
  area: evidence
  topic: Specific original ultrastructure and distribution access limits
  outcome: unknown
  summary: Tovar1999 complete abstract does not independently verify the specifically
    attributed double-membrane observation; its body/pixels were not read. Tachezy2022
    complete secondary abstract does not establish the full body as a broad mitosome-distribution
    source. These limits are not biological refutations; current exact location authority
    supports compartment topology.
  target_ids:
  - cellstructuremech:mitosome_inner_membrane
  evidence_ids:
  - septin-record-mitosome_inner_membrane
  - septin-tovar1999-meta
  - septin-tachezy2022-meta
  - septin-SL0439
  - septin-SL0438
- assessment_id: septin-mitosome_inner_membrane-materials
  area: grounding
  topic: Collective material versus optional compartment inventory
  outcome: supported
  summary: One reviewed-label-only LIPID row denotes the constitutive bilayer material,
    with no whole-membrane CURIE falsely used as a lipid identity. ESSENTIAL describes
    the collective bilayer constitution of this membrane, not a specific lipid/protein
    knockout result. The explicit grounding TODO stays accurate without a forced chemical
    identifier.
  target_ids:
  - cellstructuremech:mitosome_inner_membrane
  evidence_ids:
  - septin-record-mitosome_inner_membrane
  - septin-SL0439
  - septin-go
  - septin-curation-policy
  - septin-schema-policy
- assessment_id: septin-mitosome_inner_membrane-necessity
  area: evidence
  topic: Individual formation requirements are not measured
  outcome: unknown
  summary: Native anatomy defines the collective bilayer, but does not establish individual
    lipid species, stoichiometry, species-specific chemistry or experimental depletion/reconstitution
    requirements. Collective material constitution is not extrapolated to individual
    molecular essentiality.
  target_ids:
  - cellstructuremech:mitosome_inner_membrane
  evidence_ids:
  - septin-record-mitosome_inner_membrane
  - septin-SL0439
  - septin-schema-policy
- assessment_id: septin-mitosome_inner_membrane-graph
  area: graph
  topic: Complete descriptive topology graph
  outcome: supported
  summary: 'Three NONMECHANISTIC edges: inner membrane part_of envelope, encloses
    matrix and delimits IMS. Exact authority boundaries and frozen local identities
    agree. Graph exclusions explicitly withhold protein import/transport machinery;
    no assembly mechanism, complete molecular inventory or causal intervention is
    asserted.'
  target_ids:
  - cellstructuremech:mitosome_inner_membrane
  evidence_ids:
  - septin-record-mitosome_inner_membrane
  - septin-graph-policy
  - septin-SL0438
  - septin-SL0439
  - septin-SL0440
  - septin-SL0441
  - septin-SL0443
  - septin-go
  - septin-context-mitosome
  - septin-context-mitosome_envelope
- assessment_id: septin-mitosome_inner_membrane-native
  area: provenance
  topic: Actual native protein-check coverage
  outcome: supported
  summary: Both commands exit0. Independent inventory confirms zero protein examples,
    zero typed molecular nodes and zero UniProtKB graph xrefs. Generic success text
    is not used alone to infer inventory emptiness or scientific completeness.
  target_ids:
  - cellstructuremech:mitosome_inner_membrane
  evidence_ids:
  - septin-record-mitosome_inner_membrane
  - septin-native-mitosome_inner_membrane-verify
  - septin-native-mitosome_inner_membrane-causal
- assessment_id: septin-mitosome_inner_membrane-adapter
  area: scope
  topic: Genuine material/topology exclusion
  outcome: not_applicable
  summary: Complete record asserts only collective lipid material or spatial topology
    and qualitative occurrence. No positive named molecular/pathway/stress/trait/transcriptomic
    claim triggers a molecular query; protein/import mechanisms are explicitly excluded.
    Original N/A outcome is justified by this full scope, with wording clarified beyond
    the expression-only shorthand. No bundle defect is manufactured. Fresh catalogue
    also lacks Entamoeba; that absence is not biological evidence and no unrelated-host
    query is made.
  target_ids:
  - cellstructuremech:mitosome_inner_membrane
  evidence_ids:
  - septin-record-mitosome_inner_membrane
  - septin-original-mitosome_inner_membrane
  - septin-review-policy
  - septin-catalogue
  - septin-adapter-runner-historical
- assessment_id: septin-mitosome_inner_membrane-bibliography
  area: provenance
  topic: Confirmed DOI-title mismatch
  outcome: concern
  summary: DOI12922 resolves to The hydrogenosome of Trichomonas vaginalis by Tachezy,Makki,Hrdy2022;
    the record gives a different title. Preserve exact original minor F1 under this
    maintained record, without claiming unread full text lacks mitosome coverage.
  target_ids:
  - cellstructuremech:mitosome_inner_membrane
  evidence_ids:
  - septin-record-mitosome_inner_membrane
  - septin-original-mitosome_inner_membrane
  - septin-tachezy2022-meta
- assessment_id: septin-mitosome_inner_membrane-scope
  area: scope
  topic: No image or unrepresented molecular requirement
  outcome: not_applicable
  summary: No maintained image/pixel or licence assertion, physical measurement, associated
    trait, verbatim evidence snippet, individual gene/protein identity or protein
    example occurs. Optional inventory absence is not a failure. No source pixels
    or raw microscopy are independently inspected.
  target_ids:
  - cellstructuremech:mitosome_inner_membrane
  evidence_ids:
  - septin-record-mitosome_inner_membrane
  - septin-protein-policy
- assessment_id: septin-mitosome_inner_membrane-history
  area: provenance
  topic: Historical edits and neighbor context
  outcome: supported
  summary: PROPOSED status and recorded historical boundary-grounding changes remain
    intact. Open lipid-identity discussion, where present, documents intentional label-only
    material. Whole/envelope neighbors are frozen boundary context only; their scientific
    issues are neither adopted nor resolved.
  target_ids:
  - cellstructuremech:mitosome_inner_membrane
  evidence_ids:
  - septin-record-mitosome_inner_membrane
  - septin-context-mitosome
  - septin-context-mitosome_envelope
- assessment_id: septin-mitosome_inner_membrane-verdict
  area: completeness
  topic: Current scientific verdict
  outcome: concern
  summary: needs_curation because one exact inherited minor bibliographic finding
    remains; no confirmed new scientific defect. Exact source tiers, prevalence/primary-attribution
    limits, empty native coverage and genuine physical applicability exclusion remain
    explicit.
  target_ids:
  - cellstructuremech:mitosome_inner_membrane
  evidence_ids:
  - septin-record-mitosome_inner_membrane
  - septin-original-mitosome_inner_membrane
  - septin-tachezy2022-meta
  - septin-SL0439
- assessment_id: septin-mitosome_intermembrane_space-schema
  area: schema
  topic: Original native schema/render and unchanged frozen input
  outcome: supported
  summary: Original validate/render pass, Markdown exact and historical target hash
    matches current bytes. None of these four targets is stale. A schema pass is not
    a biological verdict.
  target_ids:
  - cellstructuremech:mitosome_intermembrane_space
  evidence_ids:
  - septin-record-mitosome_intermembrane_space
  - septin-original-validation-mitosome_intermembrane_space
- assessment_id: septin-mitosome_intermembrane_space-identity
  area: identity
  topic: Exact compartment identity, synonyms and broader classes
  outcome: supported
  summary: Exact SL0440 definition and all three synonyms match; part_of envelope
    is distinct from is_a. Bounded GO search returns whole mitosome only; exact local
    identities are retained without guessing chemical identifiers.
  target_ids:
  - cellstructuremech:mitosome_intermembrane_space
  evidence_ids:
  - septin-record-mitosome_intermembrane_space
  - septin-SL0440
  - septin-go
  - septin-go-mitosome-search
  - septin-context-mitosome
  - septin-context-mitosome_envelope
- assessment_id: septin-mitosome_intermembrane_space-taxa
  area: scope
  topic: Taxon identities and qualitative occurrence
  outcome: supported
  summary: Eukaryota2759 and Entamoeba histolytica5759 match native authority. Tovar
    primary abstract establishes the mitochondrial remnant by localization/targeting;
    later Mi-ichi purification/IF supports organelle occurrence in HM-1:IMSScl6. Roger
    review supports qualitative patchy low-oxygen eukaryotic context, not numeric
    prevalence or every-strain coverage.
  target_ids:
  - cellstructuremech:mitosome_intermembrane_space
  evidence_ids:
  - septin-record-mitosome_intermembrane_space
  - septin-tax2759
  - septin-tax5759
  - septin-tovar1999-meta
  - septin-miichi2009-pmc
  - septin-roger2017-pdf
- assessment_id: septin-mitosome_intermembrane_space-attribution-limits
  area: evidence
  topic: Specific original ultrastructure and distribution access limits
  outcome: unknown
  summary: Tovar1999 complete abstract does not independently verify the specifically
    attributed double-membrane observation; its body/pixels were not read. Tachezy2022
    complete secondary abstract does not establish the full body as a broad mitosome-distribution
    source. These limits are not biological refutations; current exact location authority
    supports compartment topology.
  target_ids:
  - cellstructuremech:mitosome_intermembrane_space
  evidence_ids:
  - septin-record-mitosome_intermembrane_space
  - septin-tovar1999-meta
  - septin-tachezy2022-meta
  - septin-SL0440
  - septin-SL0438
- assessment_id: septin-mitosome_intermembrane_space-materials
  area: completeness
  topic: Collective material versus optional compartment inventory
  outcome: supported
  summary: This spatial compartment has no molecular component inventory or ESSENTIAL
    material assertion. Empty optional molecular slots do not establish a defect;
    no sibling metabolism or protein machinery is imported into the record.
  target_ids:
  - cellstructuremech:mitosome_intermembrane_space
  evidence_ids:
  - septin-record-mitosome_intermembrane_space
  - septin-SL0440
  - septin-go
  - septin-curation-policy
  - septin-schema-policy
- assessment_id: septin-mitosome_intermembrane_space-graph
  area: graph
  topic: Complete descriptive topology graph
  outcome: supported
  summary: 'Three NONMECHANISTIC edges: IMS part_of envelope, outer and inner membranes
    delimit it. Exact authority boundaries and frozen local identities agree. Graph
    exclusions explicitly withhold protein import/transport machinery; no assembly
    mechanism, complete molecular inventory or causal intervention is asserted.'
  target_ids:
  - cellstructuremech:mitosome_intermembrane_space
  evidence_ids:
  - septin-record-mitosome_intermembrane_space
  - septin-graph-policy
  - septin-SL0438
  - septin-SL0439
  - septin-SL0440
  - septin-SL0441
  - septin-SL0443
  - septin-go
  - septin-context-mitosome
  - septin-context-mitosome_envelope
- assessment_id: septin-mitosome_intermembrane_space-native
  area: provenance
  topic: Actual native protein-check coverage
  outcome: supported
  summary: Both commands exit0. Independent inventory confirms zero protein examples,
    zero typed molecular nodes and zero UniProtKB graph xrefs. Generic success text
    is not used alone to infer inventory emptiness or scientific completeness.
  target_ids:
  - cellstructuremech:mitosome_intermembrane_space
  evidence_ids:
  - septin-record-mitosome_intermembrane_space
  - septin-native-mitosome_intermembrane_space-verify
  - septin-native-mitosome_intermembrane_space-causal
- assessment_id: septin-mitosome_intermembrane_space-adapter
  area: scope
  topic: Genuine material/topology exclusion
  outcome: not_applicable
  summary: Complete record asserts only collective lipid material or spatial topology
    and qualitative occurrence. No positive named molecular/pathway/stress/trait/transcriptomic
    claim triggers a molecular query; protein/import mechanisms are explicitly excluded.
    Original N/A outcome is justified by this full scope, with wording clarified beyond
    the expression-only shorthand. No bundle defect is manufactured. Fresh catalogue
    also lacks Entamoeba; that absence is not biological evidence and no unrelated-host
    query is made.
  target_ids:
  - cellstructuremech:mitosome_intermembrane_space
  evidence_ids:
  - septin-record-mitosome_intermembrane_space
  - septin-original-mitosome_intermembrane_space
  - septin-review-policy
  - septin-catalogue
  - septin-adapter-runner-historical
- assessment_id: septin-mitosome_intermembrane_space-bibliography
  area: provenance
  topic: Confirmed DOI-title mismatch
  outcome: concern
  summary: DOI12922 resolves to The hydrogenosome of Trichomonas vaginalis by Tachezy,Makki,Hrdy2022;
    the record gives a different title. Preserve exact original minor F1 under this
    maintained record, without claiming unread full text lacks mitosome coverage.
  target_ids:
  - cellstructuremech:mitosome_intermembrane_space
  evidence_ids:
  - septin-record-mitosome_intermembrane_space
  - septin-original-mitosome_intermembrane_space
  - septin-tachezy2022-meta
- assessment_id: septin-mitosome_intermembrane_space-scope
  area: scope
  topic: No image or unrepresented molecular requirement
  outcome: not_applicable
  summary: No maintained image/pixel or licence assertion, physical measurement, associated
    trait, verbatim evidence snippet, individual gene/protein identity or protein
    example occurs. Optional inventory absence is not a failure. No source pixels
    or raw microscopy are independently inspected.
  target_ids:
  - cellstructuremech:mitosome_intermembrane_space
  evidence_ids:
  - septin-record-mitosome_intermembrane_space
  - septin-protein-policy
- assessment_id: septin-mitosome_intermembrane_space-history
  area: provenance
  topic: Historical edits and neighbor context
  outcome: supported
  summary: PROPOSED status and recorded historical boundary-grounding changes remain
    intact. Open lipid-identity discussion, where present, documents intentional label-only
    material. Whole/envelope neighbors are frozen boundary context only; their scientific
    issues are neither adopted nor resolved.
  target_ids:
  - cellstructuremech:mitosome_intermembrane_space
  evidence_ids:
  - septin-record-mitosome_intermembrane_space
  - septin-context-mitosome
  - septin-context-mitosome_envelope
- assessment_id: septin-mitosome_intermembrane_space-verdict
  area: completeness
  topic: Current scientific verdict
  outcome: concern
  summary: needs_curation because one exact inherited minor bibliographic finding
    remains; no confirmed new scientific defect. Exact source tiers, prevalence/primary-attribution
    limits, empty native coverage and genuine physical applicability exclusion remain
    explicit.
  target_ids:
  - cellstructuremech:mitosome_intermembrane_space
  evidence_ids:
  - septin-record-mitosome_intermembrane_space
  - septin-original-mitosome_intermembrane_space
  - septin-tachezy2022-meta
  - septin-SL0440
- assessment_id: septin-mitosome_matrix-schema
  area: schema
  topic: Original native schema/render and unchanged frozen input
  outcome: supported
  summary: Original validate/render pass, Markdown exact and historical target hash
    matches current bytes. None of these four targets is stale. A schema pass is not
    a biological verdict.
  target_ids:
  - cellstructuremech:mitosome_matrix
  evidence_ids:
  - septin-record-mitosome_matrix
  - septin-original-validation-mitosome_matrix
- assessment_id: septin-mitosome_matrix-identity
  area: identity
  topic: Exact compartment identity, synonyms and broader classes
  outcome: supported
  summary: Exact SL0441 definition/synonym match; GO0043233 is an appropriate organelle-lumen
    parent by its innermost-volume definition, with whole mitosome part_of. Bounded
    GO search returns whole mitosome only; exact local identities are retained without
    guessing chemical identifiers.
  target_ids:
  - cellstructuremech:mitosome_matrix
  evidence_ids:
  - septin-record-mitosome_matrix
  - septin-SL0441
  - septin-go
  - septin-go-mitosome-search
  - septin-context-mitosome
  - septin-context-mitosome_envelope
- assessment_id: septin-mitosome_matrix-taxa
  area: scope
  topic: Taxon identities and qualitative occurrence
  outcome: supported
  summary: Eukaryota2759 and Entamoeba histolytica5759 match native authority. Tovar
    primary abstract establishes the mitochondrial remnant by localization/targeting;
    later Mi-ichi purification/IF supports organelle occurrence in HM-1:IMSScl6. Roger
    review supports qualitative patchy low-oxygen eukaryotic context, not numeric
    prevalence or every-strain coverage.
  target_ids:
  - cellstructuremech:mitosome_matrix
  evidence_ids:
  - septin-record-mitosome_matrix
  - septin-tax2759
  - septin-tax5759
  - septin-tovar1999-meta
  - septin-miichi2009-pmc
  - septin-roger2017-pdf
- assessment_id: septin-mitosome_matrix-attribution-limits
  area: evidence
  topic: Specific original ultrastructure and distribution access limits
  outcome: unknown
  summary: Tovar1999 complete abstract does not independently verify the specifically
    attributed double-membrane observation; its body/pixels were not read. Tachezy2022
    complete secondary abstract does not establish the full body as a broad mitosome-distribution
    source. These limits are not biological refutations; current exact location authority
    supports compartment topology.
  target_ids:
  - cellstructuremech:mitosome_matrix
  evidence_ids:
  - septin-record-mitosome_matrix
  - septin-tovar1999-meta
  - septin-tachezy2022-meta
  - septin-SL0441
  - septin-SL0438
- assessment_id: septin-mitosome_matrix-materials
  area: completeness
  topic: Collective material versus optional compartment inventory
  outcome: supported
  summary: This spatial compartment has no molecular component inventory or ESSENTIAL
    material assertion. Empty optional molecular slots do not establish a defect;
    no sibling metabolism or protein machinery is imported into the record.
  target_ids:
  - cellstructuremech:mitosome_matrix
  evidence_ids:
  - septin-record-mitosome_matrix
  - septin-SL0441
  - septin-go
  - septin-curation-policy
  - septin-schema-policy
- assessment_id: septin-mitosome_matrix-graph
  area: graph
  topic: Complete descriptive topology graph
  outcome: supported
  summary: 'Two NONMECHANISTIC edges: matrix part_of mitosome and inner membrane encloses
    matrix. Exact authority boundaries and frozen local identities agree. Graph exclusions
    explicitly withhold protein import/transport machinery; no assembly mechanism,
    complete molecular inventory or causal intervention is asserted.'
  target_ids:
  - cellstructuremech:mitosome_matrix
  evidence_ids:
  - septin-record-mitosome_matrix
  - septin-graph-policy
  - septin-SL0438
  - septin-SL0439
  - septin-SL0440
  - septin-SL0441
  - septin-SL0443
  - septin-go
  - septin-context-mitosome
  - septin-context-mitosome_envelope
- assessment_id: septin-mitosome_matrix-native
  area: provenance
  topic: Actual native protein-check coverage
  outcome: supported
  summary: Both commands exit0. Independent inventory confirms zero protein examples,
    zero typed molecular nodes and zero UniProtKB graph xrefs. Generic success text
    is not used alone to infer inventory emptiness or scientific completeness.
  target_ids:
  - cellstructuremech:mitosome_matrix
  evidence_ids:
  - septin-record-mitosome_matrix
  - septin-native-mitosome_matrix-verify
  - septin-native-mitosome_matrix-causal
- assessment_id: septin-mitosome_matrix-adapter
  area: scope
  topic: Genuine material/topology exclusion
  outcome: not_applicable
  summary: Complete record asserts only collective lipid material or spatial topology
    and qualitative occurrence. No positive named molecular/pathway/stress/trait/transcriptomic
    claim triggers a molecular query; protein/import mechanisms are explicitly excluded.
    Original N/A outcome is justified by this full scope, with wording clarified beyond
    the expression-only shorthand. No bundle defect is manufactured. Fresh catalogue
    also lacks Entamoeba; that absence is not biological evidence and no unrelated-host
    query is made.
  target_ids:
  - cellstructuremech:mitosome_matrix
  evidence_ids:
  - septin-record-mitosome_matrix
  - septin-original-mitosome_matrix
  - septin-review-policy
  - septin-catalogue
  - septin-adapter-runner-historical
- assessment_id: septin-mitosome_matrix-bibliography
  area: provenance
  topic: Confirmed DOI-title mismatch
  outcome: concern
  summary: DOI12922 resolves to The hydrogenosome of Trichomonas vaginalis by Tachezy,Makki,Hrdy2022;
    the record gives a different title. Preserve exact original minor F1 under this
    maintained record, without claiming unread full text lacks mitosome coverage.
  target_ids:
  - cellstructuremech:mitosome_matrix
  evidence_ids:
  - septin-record-mitosome_matrix
  - septin-original-mitosome_matrix
  - septin-tachezy2022-meta
- assessment_id: septin-mitosome_matrix-scope
  area: scope
  topic: No image or unrepresented molecular requirement
  outcome: not_applicable
  summary: No maintained image/pixel or licence assertion, physical measurement, associated
    trait, verbatim evidence snippet, individual gene/protein identity or protein
    example occurs. Optional inventory absence is not a failure. No source pixels
    or raw microscopy are independently inspected.
  target_ids:
  - cellstructuremech:mitosome_matrix
  evidence_ids:
  - septin-record-mitosome_matrix
  - septin-protein-policy
- assessment_id: septin-mitosome_matrix-history
  area: provenance
  topic: Historical edits and neighbor context
  outcome: supported
  summary: PROPOSED status and recorded historical boundary-grounding changes remain
    intact. Open lipid-identity discussion, where present, documents intentional label-only
    material. Whole/envelope neighbors are frozen boundary context only; their scientific
    issues are neither adopted nor resolved.
  target_ids:
  - cellstructuremech:mitosome_matrix
  evidence_ids:
  - septin-record-mitosome_matrix
  - septin-context-mitosome
  - septin-context-mitosome_envelope
- assessment_id: septin-mitosome_matrix-verdict
  area: completeness
  topic: Current scientific verdict
  outcome: concern
  summary: needs_curation because one exact inherited minor bibliographic finding
    remains; no confirmed new scientific defect. Exact source tiers, prevalence/primary-attribution
    limits, empty native coverage and genuine physical applicability exclusion remain
    explicit.
  target_ids:
  - cellstructuremech:mitosome_matrix
  evidence_ids:
  - septin-record-mitosome_matrix
  - septin-original-mitosome_matrix
  - septin-tachezy2022-meta
  - septin-SL0441
- assessment_id: septin-mitosome_outer_membrane-schema
  area: schema
  topic: Original native schema/render and unchanged frozen input
  outcome: supported
  summary: Original validate/render pass, Markdown exact and historical target hash
    matches current bytes. None of these four targets is stale. A schema pass is not
    a biological verdict.
  target_ids:
  - cellstructuremech:mitosome_outer_membrane
  evidence_ids:
  - septin-record-mitosome_outer_membrane
  - septin-original-validation-mitosome_outer_membrane
- assessment_id: septin-mitosome_outer_membrane-identity
  area: identity
  topic: Exact compartment identity, synonyms and broader classes
  outcome: supported
  summary: Exact SL0443 definition and both synonyms match; GO0031090 broader organelle
    membrane is distinct from envelope part_of. Bounded GO search returns whole mitosome
    only; exact local identities are retained without guessing chemical identifiers.
  target_ids:
  - cellstructuremech:mitosome_outer_membrane
  evidence_ids:
  - septin-record-mitosome_outer_membrane
  - septin-SL0443
  - septin-go
  - septin-go-mitosome-search
  - septin-context-mitosome
  - septin-context-mitosome_envelope
- assessment_id: septin-mitosome_outer_membrane-taxa
  area: scope
  topic: Taxon identities and qualitative occurrence
  outcome: supported
  summary: Eukaryota2759 and Entamoeba histolytica5759 match native authority. Tovar
    primary abstract establishes the mitochondrial remnant by localization/targeting;
    later Mi-ichi purification/IF supports organelle occurrence in HM-1:IMSScl6. Roger
    review supports qualitative patchy low-oxygen eukaryotic context, not numeric
    prevalence or every-strain coverage.
  target_ids:
  - cellstructuremech:mitosome_outer_membrane
  evidence_ids:
  - septin-record-mitosome_outer_membrane
  - septin-tax2759
  - septin-tax5759
  - septin-tovar1999-meta
  - septin-miichi2009-pmc
  - septin-roger2017-pdf
- assessment_id: septin-mitosome_outer_membrane-attribution-limits
  area: evidence
  topic: Specific original ultrastructure and distribution access limits
  outcome: unknown
  summary: Tovar1999 complete abstract does not independently verify the specifically
    attributed double-membrane observation; its body/pixels were not read. Tachezy2022
    complete secondary abstract does not establish the full body as a broad mitosome-distribution
    source. These limits are not biological refutations; current exact location authority
    supports compartment topology.
  target_ids:
  - cellstructuremech:mitosome_outer_membrane
  evidence_ids:
  - septin-record-mitosome_outer_membrane
  - septin-tovar1999-meta
  - septin-tachezy2022-meta
  - septin-SL0443
  - septin-SL0438
- assessment_id: septin-mitosome_outer_membrane-materials
  area: grounding
  topic: Collective material versus optional compartment inventory
  outcome: supported
  summary: One reviewed-label-only LIPID row denotes the constitutive bilayer material,
    with no whole-membrane CURIE falsely used as a lipid identity. ESSENTIAL describes
    the collective bilayer constitution of this membrane, not a specific lipid/protein
    knockout result. The explicit grounding TODO stays accurate without a forced chemical
    identifier.
  target_ids:
  - cellstructuremech:mitosome_outer_membrane
  evidence_ids:
  - septin-record-mitosome_outer_membrane
  - septin-SL0443
  - septin-go
  - septin-curation-policy
  - septin-schema-policy
- assessment_id: septin-mitosome_outer_membrane-necessity
  area: evidence
  topic: Individual formation requirements are not measured
  outcome: unknown
  summary: Native anatomy defines the collective bilayer, but does not establish individual
    lipid species, stoichiometry, species-specific chemistry or experimental depletion/reconstitution
    requirements. Collective material constitution is not extrapolated to individual
    molecular essentiality.
  target_ids:
  - cellstructuremech:mitosome_outer_membrane
  evidence_ids:
  - septin-record-mitosome_outer_membrane
  - septin-SL0443
  - septin-schema-policy
- assessment_id: septin-mitosome_outer_membrane-graph
  area: graph
  topic: Complete descriptive topology graph
  outcome: supported
  summary: 'Three NONMECHANISTIC edges: outer membrane part_of envelope, faces cytoplasm
    and bounds IMS. Exact authority boundaries and frozen local identities agree.
    Graph exclusions explicitly withhold protein import/transport machinery; no assembly
    mechanism, complete molecular inventory or causal intervention is asserted.'
  target_ids:
  - cellstructuremech:mitosome_outer_membrane
  evidence_ids:
  - septin-record-mitosome_outer_membrane
  - septin-graph-policy
  - septin-SL0438
  - septin-SL0439
  - septin-SL0440
  - septin-SL0441
  - septin-SL0443
  - septin-go
  - septin-context-mitosome
  - septin-context-mitosome_envelope
- assessment_id: septin-mitosome_outer_membrane-native
  area: provenance
  topic: Actual native protein-check coverage
  outcome: supported
  summary: Both commands exit0. Independent inventory confirms zero protein examples,
    zero typed molecular nodes and zero UniProtKB graph xrefs. Generic success text
    is not used alone to infer inventory emptiness or scientific completeness.
  target_ids:
  - cellstructuremech:mitosome_outer_membrane
  evidence_ids:
  - septin-record-mitosome_outer_membrane
  - septin-native-mitosome_outer_membrane-verify
  - septin-native-mitosome_outer_membrane-causal
- assessment_id: septin-mitosome_outer_membrane-adapter
  area: scope
  topic: Genuine material/topology exclusion
  outcome: not_applicable
  summary: Complete record asserts only collective lipid material or spatial topology
    and qualitative occurrence. No positive named molecular/pathway/stress/trait/transcriptomic
    claim triggers a molecular query; protein/import mechanisms are explicitly excluded.
    Original N/A outcome is justified by this full scope, with wording clarified beyond
    the expression-only shorthand. No bundle defect is manufactured. Fresh catalogue
    also lacks Entamoeba; that absence is not biological evidence and no unrelated-host
    query is made.
  target_ids:
  - cellstructuremech:mitosome_outer_membrane
  evidence_ids:
  - septin-record-mitosome_outer_membrane
  - septin-original-mitosome_outer_membrane
  - septin-review-policy
  - septin-catalogue
  - septin-adapter-runner-historical
- assessment_id: septin-mitosome_outer_membrane-bibliography
  area: provenance
  topic: Confirmed DOI-title mismatch
  outcome: concern
  summary: DOI12922 resolves to The hydrogenosome of Trichomonas vaginalis by Tachezy,Makki,Hrdy2022;
    the record gives a different title. Preserve exact original minor F1 under this
    maintained record, without claiming unread full text lacks mitosome coverage.
  target_ids:
  - cellstructuremech:mitosome_outer_membrane
  evidence_ids:
  - septin-record-mitosome_outer_membrane
  - septin-original-mitosome_outer_membrane
  - septin-tachezy2022-meta
- assessment_id: septin-mitosome_outer_membrane-scope
  area: scope
  topic: No image or unrepresented molecular requirement
  outcome: not_applicable
  summary: No maintained image/pixel or licence assertion, physical measurement, associated
    trait, verbatim evidence snippet, individual gene/protein identity or protein
    example occurs. Optional inventory absence is not a failure. No source pixels
    or raw microscopy are independently inspected.
  target_ids:
  - cellstructuremech:mitosome_outer_membrane
  evidence_ids:
  - septin-record-mitosome_outer_membrane
  - septin-protein-policy
- assessment_id: septin-mitosome_outer_membrane-history
  area: provenance
  topic: Historical edits and neighbor context
  outcome: supported
  summary: PROPOSED status and recorded historical boundary-grounding changes remain
    intact. Open lipid-identity discussion, where present, documents intentional label-only
    material. Whole/envelope neighbors are frozen boundary context only; their scientific
    issues are neither adopted nor resolved.
  target_ids:
  - cellstructuremech:mitosome_outer_membrane
  evidence_ids:
  - septin-record-mitosome_outer_membrane
  - septin-context-mitosome
  - septin-context-mitosome_envelope
- assessment_id: septin-mitosome_outer_membrane-verdict
  area: completeness
  topic: Current scientific verdict
  outcome: concern
  summary: needs_curation because one exact inherited minor bibliographic finding
    remains; no confirmed new scientific defect. Exact source tiers, prevalence/primary-attribution
    limits, empty native coverage and genuine physical applicability exclusion remain
    explicit.
  target_ids:
  - cellstructuremech:mitosome_outer_membrane
  evidence_ids:
  - septin-record-mitosome_outer_membrane
  - septin-original-mitosome_outer_membrane
  - septin-tachezy2022-meta
  - septin-SL0443
- assessment_id: plaque-t4-native
  area: schema
  topic: Native inventory and actual coverage
  outcome: supported
  summary: One UNREVIEWED A8IWX2 example and one COVERED typed node. Native accession/field
    checks pass; they do not certify literature-symbol equivalence, localization or
    necessity.
  target_ids:
  - GO:0070074
  evidence_ids:
  - plaque-current-4
  - plaque-native-mononeme-verify
  - plaque-native-mononeme-causal
  - plaque-protein-contract
- assessment_id: plaque-t4-schema
  area: schema
  topic: Historical source and exact rendering
  outcome: supported
  summary: Original native validate/render passes with14 matching frozen historical
    inputs. Current record bytes unchanged and PROPOSED status retained. No maintained
    image or quantitative property requires a pixel audit; no optional missing inventory
    finding invented.
  target_ids:
  - GO:0070074
  evidence_ids:
  - plaque-current-4
  - plaque-original-4
  - plaque-original-checks
  - plaque-rubric
- assessment_id: plaque-t4-adapter
  area: evidence
  topic: Molecular claims trigger bounded applicability assessment
  outcome: supported
  summary: PfROM1/Rom1 localization and secretory redistribution are positive claims
    triggering native structured-source assessment. Original explicit expression-only
    exemption is inadequate. Fresh catalogue has no exact represented eukaryotic host;
    no downstream module query or negative biology conclusion. Historical runner failure
    remains historical.
  target_ids:
  - GO:0070074
  evidence_ids:
  - plaque-current-4
  - plaque-original-4
  - plaque-policy
  - plaque-catalogue
  - plaque-historical-runner
- assessment_id: plaque-t5-native
  area: schema
  topic: Native inventory and actual coverage
  outcome: supported
  summary: Six UNREVIEWED examples and three COVERED typed nodes; the MDD node is
    reported COVERED through I7M6L0, despite its independently confirmed wrong MDL1
    attribution. Native accession/field checks pass; they do not certify literature-symbol
    equivalence, localization or necessity.
  target_ids:
  - GO:0036000
  evidence_ids:
  - plaque-current-5
  - plaque-native-mucocyst-verify
  - plaque-native-mucocyst-causal
  - plaque-protein-contract
- assessment_id: plaque-t5-schema
  area: schema
  topic: Historical source and exact rendering
  outcome: supported
  summary: Original native validate/render passes with14 matching frozen historical
    inputs. Current record bytes unchanged and PROPOSED status retained. No maintained
    image or quantitative property requires a pixel audit; no optional missing inventory
    finding invented.
  target_ids:
  - GO:0036000
  evidence_ids:
  - plaque-current-5
  - plaque-original-5
  - plaque-original-checks
  - plaque-rubric
- assessment_id: plaque-t5-adapter
  area: evidence
  topic: Molecular claims trigger bounded applicability assessment
  outcome: supported
  summary: GRL/GRT/MDL1/MDD and regulated exocytosis are positive claims triggering
    native structured-source assessment. Original explicit expression-only exemption
    is inadequate. Fresh catalogue has no exact represented eukaryotic host; no downstream
    module query or negative biology conclusion. Historical runner failure remains
    historical.
  target_ids:
  - GO:0036000
  evidence_ids:
  - plaque-current-5
  - plaque-original-5
  - plaque-policy
  - plaque-catalogue
  - plaque-historical-runner
- assessment_id: plaque-t4-identity
  area: identity
  topic: Exact mononeme identity and apical anatomy
  outcome: supported
  summary: GO0070074 definition and direct apical-complex parthood agree;0043231 is
    the is_a parent. Micronemes, rhoptries and dense granules remain distinct comparator
    organelles.
  target_ids:
  - GO:0070074
  evidence_ids:
  - plaque-current-4
  - plaque-go
  - plaque-GO0070074-isa
  - plaque-singh2007-pmc
- assessment_id: plaque-t4-taxa
  area: scope
  topic: Mature-segmenter and release-stage limits
  outcome: supported
  summary: Species5833 and canonical P.falciparum agree. Primary experiments used
    tagged full-length PfROM1 in3D7; mature-segmenter discrete localization is separated
    from earlier schizonts and surface redistribution after release. No claim that
    a persistent separate mononeme is demonstrated in released merozoites.
  target_ids:
  - GO:0070074
  evidence_ids:
  - plaque-current-4
  - plaque-tax5833
  - plaque-singh2007-pmc
- assessment_id: plaque-t4-protein
  area: grounding
  topic: PfROM1 versus native Rom1 identity
  outcome: supported
  summary: Native A8IWX2 is UNREVIEWED Rom1/Rhomboid-like protease,278aa,matching
    primary full-length PfROM1 sequence scope. Protein example is identity-only; primary
    microscopy supplies localization. Broad rhomboid family/domain hits do not establish
    an exact component family or necessity.
  target_ids:
  - GO:0070074
  evidence_ids:
  - plaque-current-4
  - plaque-protein-A8IWX2
  - plaque-query-Rom1
  - plaque-family-A8IWX2
  - plaque-singh2007-pmc
- assessment_id: plaque-t4-component
  area: evidence
  topic: Localized constituent and unknown formation necessity
  outcome: supported
  summary: PfROM1 association with the assayed compartment is supported; UNKNOWN formation
    necessity is retained. Neither broad protease annotation nor prior heterologous
    cleavage evidence proves mononeme formation, a universal invasion requirement
    or endogenous substrate cleavage in this compartment.
  target_ids:
  - GO:0070074
  evidence_ids:
  - plaque-current-4
  - plaque-singh2007-pmc
  - plaque-protein-A8IWX2
- assessment_id: plaque-t4-graph
  area: graph
  topic: Six descriptive localization and redistribution edges
  outcome: supported
  summary: NONMECHANISTIC graph preserves association near subpellicular microtubules,
    separate marker compartments and post-release surface redistribution. Confocal
    proximity does not assert motor-mediated transport, physical binding, membrane
    fusion route or causal proteolysis.
  target_ids:
  - GO:0070074
  evidence_ids:
  - plaque-current-4
  - plaque-singh2007-pmc
  - plaque-go
  - plaque-graph-rubric
- assessment_id: plaque-t4-sources
  area: provenance
  topic: Primary body and access tier
  outcome: supported
  summary: Singh title/DOI and genuine full HTML body inspected as specified; S3 guessed
    path404 was bypassed with a genuine matching PMC body. Main captions read but
    pixels and movies were not inspected. No image-copy or license claim appears in
    the maintained record.
  target_ids:
  - GO:0070074
  evidence_ids:
  - plaque-current-4
  - plaque-singh2007-meta
  - plaque-singh2007-pmc
- assessment_id: plaque-t4-history
  area: consistency
  topic: Existing stage corrections and optional completeness
  outcome: supported
  summary: Present history/discussion limits are assessed as current content. Earlier
    issue1281/1282 mentions do not create a new terminal disposition of unfrozen predecessors;
    unresolved membrane/lumen/cargo/motor slots do not mandate invented structure
    or protein identities.
  target_ids:
  - GO:0070074
  evidence_ids:
  - plaque-current-4
  - plaque-rubric
  - plaque-singh2007-pmc
- assessment_id: plaque-t4-limits
  area: evidence
  topic: Qualified mononeme support
  outcome: unknown
  summary: Tagged localization is not an untagged endogenous atlas, electron-tomographic
    organelle census, causal transport mechanism or invasion knockout. No figure pixels,
    supplementary movies or modern all-stage prevalence survey assessed.
  target_ids:
  - GO:0070074
  evidence_ids:
  - plaque-current-4
  - plaque-singh2007-pmc
- assessment_id: plaque-t5-identity
  area: identity
  topic: Exact mucocyst secretory-granule identity
  outcome: supported
  summary: GO0036000 literal definition and secretory granule ancestor0030141 agree.
    Whole organelle, boundary membrane and lumen are distinct descriptive entities;
    no broader cellular component is adopted as exact identity.
  target_ids:
  - GO:0036000
  evidence_ids:
  - plaque-current-5
  - plaque-go
  - plaque-GO0036000-isa
- assessment_id: plaque-t5-taxa
  area: scope
  topic: Tetrahymena species and strain boundaries
  outcome: supported
  summary: Native examples distinguish species5911 from SB210312017. Primary papers
    use stated laboratory wild-type/mutant/tagged strains and conditions, not a blanket
    SB210 experimental identity. COMMON is qualitative occurrence, not measured prevalence.
  target_ids:
  - GO:0036000
  evidence_ids:
  - plaque-current-5
  - plaque-tax5911
  - plaque-tax312017
  - plaque-kontur2016-body
  - plaque-rahaman2009-pmc
  - plaque-kuppannan2022-body
- assessment_id: plaque-t5-material
  area: grounding
  topic: Collective membrane and optional exact grounding
  outcome: supported
  summary: Label-only collective bilayer constituent is a defensible membrane-bounded
    organelle building material. ESSENTIAL applies to the collective boundary, not
    every lipid species. No actual erroneous whole-membrane GO chemical grounding
    appears; unresolved exact lipid/complex grounding alone is not a finding.
  target_ids:
  - GO:0036000
  evidence_ids:
  - plaque-current-5
  - plaque-go
  - plaque-schema-policy
  - plaque-rubric
- assessment_id: plaque-t5-grl
  area: evidence
  topic: GRL cargo, lattice and representative identities
  outcome: supported
  summary: P90618/O76218/O76219 match GRL1/3/4, all unreviewed. Primary work supports
    lattice cargo/coassembly, with proprotein processing and context-dependent associations.
    Domain hits for two examples do not ground the whole cohort; inconclusive GRL1
    InterPro retrieval is not absence evidence. UNKNOWN formation necessity is not
    replaced by a universal claim.
  target_ids:
  - GO:0036000
  evidence_ids:
  - plaque-current-5
  - plaque-protein-P90618
  - plaque-protein-O76218
  - plaque-protein-O76219
  - plaque-family-O76218
  - plaque-family-O76219
  - plaque-family-P90618
  - plaque-rahaman2009-pmc
  - plaque-kontur2016-body
  - plaque-kuppannan2022-body
- assessment_id: plaque-t5-grt
  area: evidence
  topic: GRT identities and independent sorting scope
  outcome: supported
  summary: Q3S4V5/Q2I2L7 match unreviewed GRT1/2; native gamma-crystallin-like context
    is broad. Primary sorting/biochemistry supports distinct cargo pathways under
    tested conditions; GRT double knockout retains gross core/secretion with subtler
    adhesion phenotype. No assertion that every interaction is absent in wild-type/TGN
    conditions or that family members are universally dispensable.
  target_ids:
  - GO:0036000
  evidence_ids:
  - plaque-current-5
  - plaque-protein-Q3S4V5
  - plaque-protein-Q2I2L7
  - plaque-family-Q3S4V5
  - plaque-family-Q2I2L7
  - plaque-rahaman2009-pmc
- assessment_id: plaque-t5-F1
  area: grounding
  topic: Inherited wrong MDL1 concrete example
  outcome: concern
  summary: I7M6L0 is TTHERM_00471830,392aa,PSMD4/S5A/Rpn10-family; the primary paper
    names MDL1 as TTHERM_00658810,346aa,which maps to distinct I7MM25. Maintained
    role/evidence notes assert the wrong literature-gene equivalence. Native correspondence
    success does not remove inherited major mucocyst-1.
  target_ids:
  - GO:0036000
  evidence_ids:
  - plaque-current-5
  - plaque-original-5
  - plaque-protein-I7M6L0
  - plaque-family-I7M6L0
  - plaque-IPR027040
  - plaque-kuppannan2022-body
  - plaque-query-MDL1-locus
  - plaque-protein-I7MM25
  - plaque-query-wrong-locus
- assessment_id: plaque-t5-mdd
  area: evidence
  topic: Putative MDD assembly and docking/discharge role
  outcome: supported
  summary: Primary functional tagged Mdl1 polarizes before docking; deletion impairs
    docking/discharge despite mature crystal formation. Other associated subunits
    and biochemical/negative-stain data support putative MDD machinery. Unknown exact
    assembly and direct fusion mechanism remain limited. Mdl1 phenotype is not automatically
    necessity of every complex member or formation of the organelle.
  target_ids:
  - GO:0036000
  evidence_ids:
  - plaque-current-5
  - plaque-kuppannan2022-body
  - plaque-schema-policy
- assessment_id: plaque-t5-graph
  area: graph
  topic: Seven nonmechanistic organization edges
  outcome: supported
  summary: Membrane boundary, lumen parthood, GRL crystal organization, GRT sorting,
    tip-associated MDD and secretion support descriptive scope. Exact Mdl1 localization
    supports the tip-associated machinery abstraction without claiming every associated
    subunit independently resolved at the tip. Component protein example remains the
    inherited identity defect. Complex-as-GENE_OR_PROTEIN is allowed natively.
  target_ids:
  - GO:0036000
  evidence_ids:
  - plaque-current-5
  - plaque-kuppannan2022-body
  - plaque-rahaman2009-pmc
  - plaque-graph-rubric
  - plaque-schema-policy
- assessment_id: plaque-t5-inventory
  area: consistency
  topic: Biogenesis factors versus optional mature inventory
  outcome: supported
  summary: Kontur supports Mma1 maturation role without significant mature localization
    in tested induced fusion. Kaur does show induced Stx7l1-GFP at mature and immature
    mucocysts; present conditional inventory notes do not deny this or require every
    supported protein added. Localization does not itself establish exocytic fusion
    necessity. No new optional-inventory or mandatory-enum finding.
  target_ids:
  - GO:0036000
  evidence_ids:
  - plaque-current-5
  - plaque-kontur2016-body
  - plaque-kaur2017-body
  - plaque-rubric
  - plaque-schema-policy
- assessment_id: plaque-t5-sources
  area: provenance
  topic: Primary experimental tiers and metadata
  outcome: supported
  summary: Four independent mucocyst primary bodies were read in declared sections.
    Rahaman HTML matches DOI/title despite failed guessed S3 route; other three are
    genuine JATS. Kuppannan complex microscopy is negative-stain TEM, not cryoET.
    Main captions inspected only where declared; no actual figure pixels/supplements/raw
    proteomics audited.
  target_ids:
  - GO:0036000
  evidence_ids:
  - plaque-current-5
  - plaque-rahaman2009-meta
  - plaque-kontur2016-meta
  - plaque-kuppannan2022-meta
  - plaque-kaur2017-meta
  - plaque-rahaman2009-pmc
  - plaque-kontur2016-body
  - plaque-kuppannan2022-body
  - plaque-kaur2017-body
- assessment_id: plaque-t5-action
  area: consistency
  topic: Exact inherited repair and scope
  outcome: concern
  summary: Retain F1/A1 predecessor identity. Separately authorized curation should
    remove or replace the wrong example and attribution, verify paper locus plus native
    candidate identity/status/strain, and cite primary MDL1 membership. Do not replace
    entire MDD complex identity with one subunit or treat accession validation alone
    as scientific repair.
  target_ids:
  - GO:0036000
  evidence_ids:
  - plaque-current-5
  - plaque-original-5
  - plaque-protein-I7MM25
  - plaque-kuppannan2022-body
  - plaque-protein-contract
- assessment_id: plaque-t5-limits
  area: evidence
  topic: Qualified scientific scope outside the confirmed finding
  outcome: unknown
  summary: No exhaustive mature-protein inventory, raw mass-spectrometric reanalysis,
    exact MDD stoichiometry/assembly or direct membrane-fusion mechanism. Predicted
    helices/lipidation and broad family domains are not experimentally established
    necessities. P90618 InterPro retrieval and Q2I2L7 mapping remain inconclusive/unavailable.
  target_ids:
  - GO:0036000
  evidence_ids:
  - plaque-current-5
  - plaque-kuppannan2022-body
  - plaque-family-P90618
  - plaque-family-Q2I2L7
  - plaque-rubric
- assessment_id: micro-multivesicular_body-identity
  area: identity
  topic: Exact entity, synonyms and boundaries
  outcome: supported
  summary: ActiveGO0005771 exactly matches whole-MVB definition. Typed GO relation
    and SL0174 support late-endosome ancestry; maintained membrane/lumen/ILV has_part
    boundaries distinguish three valid subentities. Existing local sibling links resolve
    uniquely despite their separately owned GO-first findings.
  target_ids:
  - GO:0005771
  evidence_ids:
  - micro-record-multivesicular_body
  - micro-go
  - micro-identifier-preservation
  - micro-local-identity-search
  - micro-sl0174
- assessment_id: micro-multivesicular_body-components
  area: grounding
  topic: Constituent material versus assembly machinery
  outcome: supported
  summary: No molecular component inventory asserted; ESCRT machinery remains external
    assembly actors, not stable mature MVB constituents.
  target_ids:
  - GO:0005771
  evidence_ids:
  - micro-record-multivesicular_body
  - micro-component-policy
  - micro-go
  - micro-babst2002-meta
- assessment_id: micro-multivesicular_body-graph
  area: graph
  topic: Every coarse directed edge
  outcome: supported
  summary: 'All five NONMECHANISTIC edges checked: ESCRT-I sorting is supported by
    primary2001 abstract; ESCRT-II recruitment by direct Teo2004 purified Vps25/Vps20
    and enhanced liposome association; ESCRT-III remodeling by primary2002 recruitment/sorting
    plus GO and secondary context; inward budding and ILV containment by defining
    ontology topology. No complete sequential scission mechanism or direct in-vivo
    reconstitution is asserted.'
  target_ids:
  - GO:0005771
  evidence_ids:
  - micro-record-multivesicular_body
  - micro-go
  - micro-sl0340
  - micro-katzmann2001-meta
  - micro-babst2002-meta
  - micro-henne2011-meta
  - micro-teo2004-pdf
  - micro-graph-policy
- assessment_id: micro-multivesicular_body-function
  area: scope
  topic: Sorting and degradation destination
  outcome: supported
  summary: GO0071985 and inspected primary abstracts support ubiquitination as a cargo-sorting
    signal and ESCRT-associated entry into MVB vesicles; Henne secondary abstract
    supports vacuolar/lysosomal delivery. These are bounded yeast sorting assertions,
    not a universal claim that every ILV in every organism uses one obligatory mechanism.
  target_ids:
  - GO:0005771
  evidence_ids:
  - micro-record-multivesicular_body
  - micro-go
  - micro-katzmann2001-meta
  - micro-babst2002-meta
  - micro-henne2011-meta
- assessment_id: micro-multivesicular_body-taxon
  area: scope
  topic: Budding-yeast experimental versus expression-host scope
  outcome: supported
  summary: Tax4932 confirms species. Primary abstracts and Teo S.cerevisiae source
    genes support qualitative yeast model/COMMON context, not a quantified prevalence
    census. Teo bacterial recombinant expression hosts and bovine-brain liposomes
    are assay materials, not organism exemplars for MVB identity.
  target_ids:
  - GO:0005771
  evidence_ids:
  - micro-record-multivesicular_body
  - micro-tax4932
  - micro-katzmann2001-meta
  - micro-babst2002-meta
  - micro-teo2004-pdf
- assessment_id: micro-multivesicular_body-native
  area: schema
  topic: Original provenance and empty native protein coverage
  outcome: supported
  summary: All original hashes match retained source and target remains unchanged.
    Four original pairs validate/render exactly. Current verify/causal exit0, zero
    examples and zero GENE_OR_PROTEIN nodes; ESCRT STRUCTURE/GO identities were independently
    inspected. Generic success text is not populated protein verification.
  target_ids:
  - GO:0005771
  evidence_ids:
  - micro-prior-multivesicular_body
  - micro-original-inputs
  - micro-original-pairs
  - micro-native-multivesicular_body-verify
  - micro-native-multivesicular_body-causal
  - micro-go
  - micro-graph-policy
- assessment_id: micro-multivesicular_body-adapter-original
  area: provenance
  topic: Present expression-only exclusion is unsupported
  outcome: concern
  summary: Original imodulondb check exists; no omission. Positive ESCRT-dependent
    MVB sorting claims in functions/examples/graph require actual structured-source
    host applicability assessment even without transcriptomics claims. Lumen pathway
    statements remain positive assertions despite empty inventory.
  target_ids:
  - GO:0005771
  evidence_ids:
  - micro-record-multivesicular_body
  - micro-prior-multivesicular_body
  - micro-policy
- assessment_id: micro-multivesicular_body-adapter-current
  area: evidence
  topic: Fresh bounded catalogue host coverage
  outcome: not_applicable
  summary: Actual official catalogue contains no matching Saccharomyces dataset. No
    downstream module search or summary is required for an unmatched host. Historical
    runner00:49Z limit and fresh successful catalogue fallback are distinct; no noncoverage-as-refutation
    or E.coli expression-host proxy.
  target_ids:
  - GO:0005771
  evidence_ids:
  - micro-record-multivesicular_body
  - micro-catalogue-api
  - micro-historical-runner
  - micro-policy
- assessment_id: micro-multivesicular_body-access
  area: evidence
  topic: Exact access tiers and restricted inference
  outcome: supported
  summary: Fresh primary2001/2002 complete abstracts and fresh secondaryHenne2011
    abstract inspected. Exact DOI routes return redirect-only200, publisher routes403.
    Teo genuine primary PDF read p559/pp564-567 only; no image pixels, uninspected
    structural sections or supplements certified.
  target_ids:
  - GO:0005771
  evidence_ids:
  - micro-record-multivesicular_body
  - micro-katzmann2001-meta
  - micro-babst2002-meta
  - micro-henne2011-meta
  - micro-teo2004-pdf
  - micro-katzmann2001-access
  - micro-babst2002-access
  - micro-henne2011-access
- assessment_id: micro-multivesicular_body-coverage
  area: completeness
  topic: Whole record and optional fields
  outcome: supported
  summary: 'Complete maintained record read: identity/history, all claims/evidence,
    discussions, graph boundaries and status. No image, physical-number, verbatim
    snippet, trait or accession-bearing protein claim occurs. No optional lipid species,
    stoichiometry, full ESCRT inventory or category-wide disposition invented. PROPOSED
    and histories remain unchanged.'
  target_ids:
  - GO:0005771
  evidence_ids:
  - micro-record-multivesicular_body
  - micro-prior-multivesicular_body
  - micro-component-policy
  - micro-policy
- assessment_id: micro-multivesicular_body_intraluminal_vesicle-identity
  area: identity
  topic: Exact entity, synonyms and boundaries
  outcome: concern
  summary: Maintained internal membrane-bounded vesicle matches activeGO0097487 exactly,
    not broader vesicle0031982 or wholeMVB. GO definition, is_a-only ancestry and
    typed MVB part_of all agree. Local identifier is valid but misses required exact
    GO-first identity; preserve inherited majorF1 and identifier-preserving migration.
  target_ids:
  - cellstructuremech:multivesicular_body_intraluminal_vesicle
  evidence_ids:
  - micro-record-multivesicular_body_intraluminal_vesicle
  - micro-go
  - micro-identifier-preservation
  - micro-local-identity-search
  - micro-go-0097487-isa
- assessment_id: micro-multivesicular_body_intraluminal_vesicle-components
  area: grounding
  topic: Constituent material versus assembly machinery
  outcome: supported
  summary: Collective lipid bilayer uses REVIEWED_LABEL_ONLY without a whole-membrane
    GO molecular grounding. ESCRT-III is assembly machinery, not forced into mature-vesicle
    or membrane components. Optional molecular lipid mapping TODO remains candid.
  target_ids:
  - cellstructuremech:multivesicular_body_intraluminal_vesicle
  evidence_ids:
  - micro-record-multivesicular_body_intraluminal_vesicle
  - micro-component-policy
  - micro-go
  - micro-babst2002-meta
- assessment_id: micro-multivesicular_body_intraluminal_vesicle-graph
  area: graph
  topic: Every coarse directed edge
  outcome: supported
  summary: 'All four NONMECHANISTIC edges checked: ESCRT-III acts on limiting membrane,
    limiting membrane buds inward, ILV is contained in the outerMVB lumen, limiting
    membrane bounds wholeMVB. The last actor is correctly the limiting membrane, not
    the ILV bilayer. Cargo reception describes sorting, not permanent ubiquitin retention
    on every completed vesicle.'
  target_ids:
  - cellstructuremech:multivesicular_body_intraluminal_vesicle
  evidence_ids:
  - micro-record-multivesicular_body_intraluminal_vesicle
  - micro-go
  - micro-sl0340
  - micro-katzmann2001-meta
  - micro-babst2002-meta
  - micro-henne2011-meta
  - micro-teo2004-pdf
  - micro-graph-policy
- assessment_id: micro-multivesicular_body_intraluminal_vesicle-function
  area: scope
  topic: Sorting and degradation destination
  outcome: supported
  summary: GO0071985 and inspected primary abstracts support ubiquitination as a cargo-sorting
    signal and ESCRT-associated entry into MVB vesicles; Henne secondary abstract
    supports vacuolar/lysosomal delivery. These are bounded yeast sorting assertions,
    not a universal claim that every ILV in every organism uses one obligatory mechanism.
  target_ids:
  - cellstructuremech:multivesicular_body_intraluminal_vesicle
  evidence_ids:
  - micro-record-multivesicular_body_intraluminal_vesicle
  - micro-go
  - micro-katzmann2001-meta
  - micro-babst2002-meta
  - micro-henne2011-meta
- assessment_id: micro-multivesicular_body_intraluminal_vesicle-taxon
  area: scope
  topic: Budding-yeast experimental versus expression-host scope
  outcome: supported
  summary: Tax4932 confirms species. Primary abstracts and Teo S.cerevisiae source
    genes support qualitative yeast model/COMMON context, not a quantified prevalence
    census. Teo bacterial recombinant expression hosts and bovine-brain liposomes
    are assay materials, not organism exemplars for MVB identity.
  target_ids:
  - cellstructuremech:multivesicular_body_intraluminal_vesicle
  evidence_ids:
  - micro-record-multivesicular_body_intraluminal_vesicle
  - micro-tax4932
  - micro-katzmann2001-meta
  - micro-babst2002-meta
  - micro-teo2004-pdf
- assessment_id: micro-multivesicular_body_intraluminal_vesicle-native
  area: schema
  topic: Original provenance and empty native protein coverage
  outcome: supported
  summary: All original hashes match retained source and target remains unchanged.
    Four original pairs validate/render exactly. Current verify/causal exit0, zero
    examples and zero GENE_OR_PROTEIN nodes; ESCRT STRUCTURE/GO identities were independently
    inspected. Generic success text is not populated protein verification.
  target_ids:
  - cellstructuremech:multivesicular_body_intraluminal_vesicle
  evidence_ids:
  - micro-prior-multivesicular_body_intraluminal_vesicle
  - micro-original-inputs
  - micro-original-pairs
  - micro-native-multivesicular_body_intraluminal_vesicle-verify
  - micro-native-multivesicular_body_intraluminal_vesicle-causal
  - micro-go
  - micro-graph-policy
- assessment_id: micro-multivesicular_body_intraluminal_vesicle-adapter-original
  area: provenance
  topic: Present expression-only exclusion is unsupported
  outcome: concern
  summary: Original imodulondb check exists; no omission. Positive ESCRT-dependent
    MVB sorting claims in functions/examples/graph require actual structured-source
    host applicability assessment even without transcriptomics claims. Lumen pathway
    statements remain positive assertions despite empty inventory.
  target_ids:
  - cellstructuremech:multivesicular_body_intraluminal_vesicle
  evidence_ids:
  - micro-record-multivesicular_body_intraluminal_vesicle
  - micro-prior-multivesicular_body_intraluminal_vesicle
  - micro-policy
- assessment_id: micro-multivesicular_body_intraluminal_vesicle-adapter-current
  area: evidence
  topic: Fresh bounded catalogue host coverage
  outcome: not_applicable
  summary: Actual official catalogue contains no matching Saccharomyces dataset. No
    downstream module search or summary is required for an unmatched host. Historical
    runner00:49Z limit and fresh successful catalogue fallback are distinct; no noncoverage-as-refutation
    or E.coli expression-host proxy.
  target_ids:
  - cellstructuremech:multivesicular_body_intraluminal_vesicle
  evidence_ids:
  - micro-record-multivesicular_body_intraluminal_vesicle
  - micro-catalogue-api
  - micro-historical-runner
  - micro-policy
- assessment_id: micro-multivesicular_body_intraluminal_vesicle-access
  area: evidence
  topic: Exact access tiers and restricted inference
  outcome: supported
  summary: Fresh primary2001/2002 complete abstracts and fresh secondaryHenne2011
    abstract inspected. Exact DOI routes return redirect-only200, publisher routes403.
    Teo genuine primary PDF read p559/pp564-567 only; no image pixels, uninspected
    structural sections or supplements certified.
  target_ids:
  - cellstructuremech:multivesicular_body_intraluminal_vesicle
  evidence_ids:
  - micro-record-multivesicular_body_intraluminal_vesicle
  - micro-katzmann2001-meta
  - micro-babst2002-meta
  - micro-henne2011-meta
  - micro-teo2004-pdf
  - micro-katzmann2001-access
  - micro-babst2002-access
  - micro-henne2011-access
- assessment_id: micro-multivesicular_body_intraluminal_vesicle-coverage
  area: completeness
  topic: Whole record and optional fields
  outcome: supported
  summary: 'Complete maintained record read: identity/history, all claims/evidence,
    discussions, graph boundaries and status. No image, physical-number, verbatim
    snippet, trait or accession-bearing protein claim occurs. No optional lipid species,
    stoichiometry, full ESCRT inventory or category-wide disposition invented. PROPOSED
    and histories remain unchanged.'
  target_ids:
  - cellstructuremech:multivesicular_body_intraluminal_vesicle
  evidence_ids:
  - micro-record-multivesicular_body_intraluminal_vesicle
  - micro-prior-multivesicular_body_intraluminal_vesicle
  - micro-component-policy
  - micro-policy
- assessment_id: micro-multivesicular_body_intraluminal_vesicle-necessity
  area: evidence
  topic: Constitutive bilayer versus molecular necessity
  outcome: unknown
  summary: ESSENTIAL collective bilayer material is definitional for a membrane-bounded
    structure; it does not establish that an individual lipid species, ESCRT subunit
    or complete source-independent composition is required for formation. Inspected
    assay lipids are not the composition of the maintained yeast structure.
  target_ids:
  - cellstructuremech:multivesicular_body_intraluminal_vesicle
  evidence_ids:
  - micro-record-multivesicular_body_intraluminal_vesicle
  - micro-component-policy
  - micro-teo2004-pdf
  - micro-go
- assessment_id: micro-multivesicular_body_lumen-identity
  area: identity
  topic: Exact entity, synonyms and boundaries
  outcome: concern
  summary: Outer-MVB lumen matches activeGO0097486 exactly, not the interior of one
    internal vesicle. SL0340 confirms all five maintained synonyms and endosome-lumen/MVB
    relations. Local identity remains valid but misses required exact GO identity;
    preserve inherited majorF1 with no destructive renaming.
  target_ids:
  - cellstructuremech:multivesicular_body_lumen
  evidence_ids:
  - micro-record-multivesicular_body_lumen
  - micro-go
  - micro-identifier-preservation
  - micro-local-identity-search
  - micro-go-0097486-isa
  - micro-sl0340
- assessment_id: micro-multivesicular_body_lumen-components
  area: grounding
  topic: Constituent material versus assembly machinery
  outcome: supported
  summary: No molecular components or necessity asserted for this spatial lumen; membrane
    is boundary and ILVs are contents.
  target_ids:
  - cellstructuremech:multivesicular_body_lumen
  evidence_ids:
  - micro-record-multivesicular_body_lumen
  - micro-component-policy
  - micro-go
  - micro-babst2002-meta
- assessment_id: micro-multivesicular_body_lumen-graph
  area: graph
  topic: Every coarse directed edge
  outcome: supported
  summary: All four NONMECHANISTIC edges retain lumen isA endosome lumen, lumen partOf
    MVB, membrane bounds lumen, and ILV contained in lumen. Sorting function concerns
    destination of vesicles/cargo rather than autonomous catalysis by a volume.
  target_ids:
  - cellstructuremech:multivesicular_body_lumen
  evidence_ids:
  - micro-record-multivesicular_body_lumen
  - micro-go
  - micro-sl0340
  - micro-katzmann2001-meta
  - micro-babst2002-meta
  - micro-henne2011-meta
  - micro-teo2004-pdf
  - micro-graph-policy
- assessment_id: micro-multivesicular_body_lumen-function
  area: scope
  topic: Sorting and degradation destination
  outcome: supported
  summary: GO0071985 and inspected primary abstracts support ubiquitination as a cargo-sorting
    signal and ESCRT-associated entry into MVB vesicles; Henne secondary abstract
    supports vacuolar/lysosomal delivery. These are bounded yeast sorting assertions,
    not a universal claim that every ILV in every organism uses one obligatory mechanism.
  target_ids:
  - cellstructuremech:multivesicular_body_lumen
  evidence_ids:
  - micro-record-multivesicular_body_lumen
  - micro-go
  - micro-katzmann2001-meta
  - micro-babst2002-meta
  - micro-henne2011-meta
- assessment_id: micro-multivesicular_body_lumen-taxon
  area: scope
  topic: Budding-yeast experimental versus expression-host scope
  outcome: supported
  summary: Tax4932 confirms species. Primary abstracts and Teo S.cerevisiae source
    genes support qualitative yeast model/COMMON context, not a quantified prevalence
    census. Teo bacterial recombinant expression hosts and bovine-brain liposomes
    are assay materials, not organism exemplars for MVB identity.
  target_ids:
  - cellstructuremech:multivesicular_body_lumen
  evidence_ids:
  - micro-record-multivesicular_body_lumen
  - micro-tax4932
  - micro-katzmann2001-meta
  - micro-babst2002-meta
  - micro-teo2004-pdf
- assessment_id: micro-multivesicular_body_lumen-native
  area: schema
  topic: Original provenance and empty native protein coverage
  outcome: supported
  summary: All original hashes match retained source and target remains unchanged.
    Four original pairs validate/render exactly. Current verify/causal exit0, zero
    examples and zero GENE_OR_PROTEIN nodes; ESCRT STRUCTURE/GO identities were independently
    inspected. Generic success text is not populated protein verification.
  target_ids:
  - cellstructuremech:multivesicular_body_lumen
  evidence_ids:
  - micro-prior-multivesicular_body_lumen
  - micro-original-inputs
  - micro-original-pairs
  - micro-native-multivesicular_body_lumen-verify
  - micro-native-multivesicular_body_lumen-causal
  - micro-go
  - micro-graph-policy
- assessment_id: micro-multivesicular_body_lumen-adapter-original
  area: provenance
  topic: Present expression-only exclusion is unsupported
  outcome: concern
  summary: Original imodulondb check exists; no omission. Positive ESCRT-dependent
    MVB sorting claims in functions/examples/graph require actual structured-source
    host applicability assessment even without transcriptomics claims. Lumen pathway
    statements remain positive assertions despite empty inventory.
  target_ids:
  - cellstructuremech:multivesicular_body_lumen
  evidence_ids:
  - micro-record-multivesicular_body_lumen
  - micro-prior-multivesicular_body_lumen
  - micro-policy
- assessment_id: micro-multivesicular_body_lumen-adapter-current
  area: evidence
  topic: Fresh bounded catalogue host coverage
  outcome: not_applicable
  summary: Actual official catalogue contains no matching Saccharomyces dataset. No
    downstream module search or summary is required for an unmatched host. Historical
    runner00:49Z limit and fresh successful catalogue fallback are distinct; no noncoverage-as-refutation
    or E.coli expression-host proxy.
  target_ids:
  - cellstructuremech:multivesicular_body_lumen
  evidence_ids:
  - micro-record-multivesicular_body_lumen
  - micro-catalogue-api
  - micro-historical-runner
  - micro-policy
- assessment_id: micro-multivesicular_body_lumen-access
  area: evidence
  topic: Exact access tiers and restricted inference
  outcome: supported
  summary: Fresh primary2001/2002 complete abstracts and fresh secondaryHenne2011
    abstract inspected. Exact DOI routes return redirect-only200, publisher routes403.
    Teo genuine primary PDF read p559/pp564-567 only; no image pixels, uninspected
    structural sections or supplements certified.
  target_ids:
  - cellstructuremech:multivesicular_body_lumen
  evidence_ids:
  - micro-record-multivesicular_body_lumen
  - micro-katzmann2001-meta
  - micro-babst2002-meta
  - micro-henne2011-meta
  - micro-teo2004-pdf
  - micro-katzmann2001-access
  - micro-babst2002-access
  - micro-henne2011-access
- assessment_id: micro-multivesicular_body_lumen-coverage
  area: completeness
  topic: Whole record and optional fields
  outcome: supported
  summary: 'Complete maintained record read: identity/history, all claims/evidence,
    discussions, graph boundaries and status. No image, physical-number, verbatim
    snippet, trait or accession-bearing protein claim occurs. No optional lipid species,
    stoichiometry, full ESCRT inventory or category-wide disposition invented. PROPOSED
    and histories remain unchanged.'
  target_ids:
  - cellstructuremech:multivesicular_body_lumen
  evidence_ids:
  - micro-record-multivesicular_body_lumen
  - micro-prior-multivesicular_body_lumen
  - micro-component-policy
  - micro-policy
- assessment_id: micro-multivesicular_body_membrane-identity
  area: identity
  topic: Exact entity, synonyms and boundaries
  outcome: supported
  summary: GO0032585 exactly denotes the outer limiting MVB membrane. SL0175 confirms
    all five synonyms, endosome-membrane isA and wholeMVB partOf. This record is not
    every internal-vesicle membrane.
  target_ids:
  - GO:0032585
  evidence_ids:
  - micro-record-multivesicular_body_membrane
  - micro-go
  - micro-identifier-preservation
  - micro-local-identity-search
  - micro-sl0175
- assessment_id: micro-multivesicular_body_membrane-components
  area: grounding
  topic: Constituent material versus assembly machinery
  outcome: supported
  summary: Collective lipid bilayer uses REVIEWED_LABEL_ONLY without a whole-membrane
    GO molecular grounding. ESCRT-III is assembly machinery, not forced into mature-vesicle
    or membrane components. Optional molecular lipid mapping TODO remains candid.
  target_ids:
  - GO:0032585
  evidence_ids:
  - micro-record-multivesicular_body_membrane
  - micro-component-policy
  - micro-go
  - micro-babst2002-meta
- assessment_id: micro-multivesicular_body_membrane-graph
  area: graph
  topic: Every coarse directed edge
  outcome: supported
  summary: All five NONMECHANISTIC edges retain membrane isA endosome membrane, membrane
    partOf MVB, ESCRT-III remodeling, inward ILV budding and ILV containment. Graph
    component_ref connects label-only constituent material; it does not assert a whole-membrane
    GO as a chemical molecular grounding.
  target_ids:
  - GO:0032585
  evidence_ids:
  - micro-record-multivesicular_body_membrane
  - micro-go
  - micro-sl0340
  - micro-katzmann2001-meta
  - micro-babst2002-meta
  - micro-henne2011-meta
  - micro-teo2004-pdf
  - micro-graph-policy
- assessment_id: micro-multivesicular_body_membrane-function
  area: scope
  topic: Sorting and degradation destination
  outcome: supported
  summary: GO0071985 and inspected primary abstracts support ubiquitination as a cargo-sorting
    signal and ESCRT-associated entry into MVB vesicles; Henne secondary abstract
    supports vacuolar/lysosomal delivery. These are bounded yeast sorting assertions,
    not a universal claim that every ILV in every organism uses one obligatory mechanism.
  target_ids:
  - GO:0032585
  evidence_ids:
  - micro-record-multivesicular_body_membrane
  - micro-go
  - micro-katzmann2001-meta
  - micro-babst2002-meta
  - micro-henne2011-meta
- assessment_id: micro-multivesicular_body_membrane-taxon
  area: scope
  topic: Budding-yeast experimental versus expression-host scope
  outcome: supported
  summary: Tax4932 confirms species. Primary abstracts and Teo S.cerevisiae source
    genes support qualitative yeast model/COMMON context, not a quantified prevalence
    census. Teo bacterial recombinant expression hosts and bovine-brain liposomes
    are assay materials, not organism exemplars for MVB identity.
  target_ids:
  - GO:0032585
  evidence_ids:
  - micro-record-multivesicular_body_membrane
  - micro-tax4932
  - micro-katzmann2001-meta
  - micro-babst2002-meta
  - micro-teo2004-pdf
- assessment_id: micro-multivesicular_body_membrane-native
  area: schema
  topic: Original provenance and empty native protein coverage
  outcome: supported
  summary: All original hashes match retained source and target remains unchanged.
    Four original pairs validate/render exactly. Current verify/causal exit0, zero
    examples and zero GENE_OR_PROTEIN nodes; ESCRT STRUCTURE/GO identities were independently
    inspected. Generic success text is not populated protein verification.
  target_ids:
  - GO:0032585
  evidence_ids:
  - micro-prior-multivesicular_body_membrane
  - micro-original-inputs
  - micro-original-pairs
  - micro-native-multivesicular_body_membrane-verify
  - micro-native-multivesicular_body_membrane-causal
  - micro-go
  - micro-graph-policy
- assessment_id: micro-multivesicular_body_membrane-adapter-original
  area: provenance
  topic: Present expression-only exclusion is unsupported
  outcome: concern
  summary: Original imodulondb check exists; no omission. Positive ESCRT-dependent
    MVB sorting claims in functions/examples/graph require actual structured-source
    host applicability assessment even without transcriptomics claims. Lumen pathway
    statements remain positive assertions despite empty inventory.
  target_ids:
  - GO:0032585
  evidence_ids:
  - micro-record-multivesicular_body_membrane
  - micro-prior-multivesicular_body_membrane
  - micro-policy
- assessment_id: micro-multivesicular_body_membrane-adapter-current
  area: evidence
  topic: Fresh bounded catalogue host coverage
  outcome: not_applicable
  summary: Actual official catalogue contains no matching Saccharomyces dataset. No
    downstream module search or summary is required for an unmatched host. Historical
    runner00:49Z limit and fresh successful catalogue fallback are distinct; no noncoverage-as-refutation
    or E.coli expression-host proxy.
  target_ids:
  - GO:0032585
  evidence_ids:
  - micro-record-multivesicular_body_membrane
  - micro-catalogue-api
  - micro-historical-runner
  - micro-policy
- assessment_id: micro-multivesicular_body_membrane-access
  area: evidence
  topic: Exact access tiers and restricted inference
  outcome: supported
  summary: Fresh primary2001/2002 complete abstracts and fresh secondaryHenne2011
    abstract inspected. Exact DOI routes return redirect-only200, publisher routes403.
    Teo genuine primary PDF read p559/pp564-567 only; no image pixels, uninspected
    structural sections or supplements certified.
  target_ids:
  - GO:0032585
  evidence_ids:
  - micro-record-multivesicular_body_membrane
  - micro-katzmann2001-meta
  - micro-babst2002-meta
  - micro-henne2011-meta
  - micro-teo2004-pdf
  - micro-katzmann2001-access
  - micro-babst2002-access
  - micro-henne2011-access
- assessment_id: micro-multivesicular_body_membrane-coverage
  area: completeness
  topic: Whole record and optional fields
  outcome: supported
  summary: 'Complete maintained record read: identity/history, all claims/evidence,
    discussions, graph boundaries and status. No image, physical-number, verbatim
    snippet, trait or accession-bearing protein claim occurs. No optional lipid species,
    stoichiometry, full ESCRT inventory or category-wide disposition invented. PROPOSED
    and histories remain unchanged.'
  target_ids:
  - GO:0032585
  evidence_ids:
  - micro-record-multivesicular_body_membrane
  - micro-prior-multivesicular_body_membrane
  - micro-component-policy
  - micro-policy
- assessment_id: micro-multivesicular_body_membrane-necessity
  area: evidence
  topic: Constitutive bilayer versus molecular necessity
  outcome: unknown
  summary: ESSENTIAL collective bilayer material is definitional for a membrane-bounded
    structure; it does not establish that an individual lipid species, ESCRT subunit
    or complete source-independent composition is required for formation. Inspected
    assay lipids are not the composition of the maintained yeast structure.
  target_ids:
  - GO:0032585
  evidence_ids:
  - micro-record-multivesicular_body_membrane
  - micro-component-policy
  - micro-teo2004-pdf
  - micro-go
- assessment_id: current-input-comparison
  area: provenance
  topic: Complete frozen-input comparison and bounded refresh
  outcome: supported
  summary: 0 of ten original target hashes differ from current main. The changed content
    is substantively reassessed in the target-specific assessments; original observations
    remain historical and unchanged. All current target and used context bytes are
    frozen.
  target_ids:
  - cellstructuremech:mitosome_inner_membrane
  - cellstructuremech:mitosome_intermembrane_space
  - cellstructuremech:mitosome_matrix
  - cellstructuremech:mitosome_outer_membrane
  - GO:0070074
  - GO:0036000
  - GO:0005771
  - cellstructuremech:multivesicular_body_intraluminal_vesicle
  - cellstructuremech:multivesicular_body_lumen
  - GO:0032585
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
- finding_id: septin-mitosome_inner_membrane-F1
  issue_key: mitosome-inner-membrane-tachezy-title
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Correct the title attached to DOI10.1111/jeu.12922
  description: 'The evidence note calls this article Hydrogenosomes and mitosomes:
    Mitochondria of anaerobic eukaryotes. Exact native metadata identifies The hydrogenosome
    of Trichomonas vaginalis by Tachezy, Makki and Hrdy (2022). The DOI is valid;
    its unread full body is not presumed to lack a mitosome passage.'
  target_ids:
  - cellstructuremech:mitosome_inner_membrane
  field_paths:
  - evidence[6].notes
  evidence_ids:
  - septin-record-mitosome_inner_membrane
  - septin-original-mitosome_inner_membrane
  - septin-tachezy2022-meta
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/mitosome_inner_membrane.yaml
    role: maintained scientific record
  rule_id: .claude/skills/review-yaml-record/SKILL.md:exact source identity
  native_severity: minor
  normalization_reason: Minor bibliographic title/attribution error; no wrong compartment
    identity or demonstrated false distribution follows from the access limitation.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T024026Z-mitosome-inner-membrane-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2741
- finding_id: septin-mitosome_intermembrane_space-F1
  issue_key: mitosome-intermembrane-space-tachezy-title
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Correct the title attached to DOI10.1111/jeu.12922
  description: 'The evidence note calls this article Hydrogenosomes and mitosomes:
    Mitochondria of anaerobic eukaryotes. Exact native metadata identifies The hydrogenosome
    of Trichomonas vaginalis by Tachezy, Makki and Hrdy (2022). The DOI is valid;
    its unread full body is not presumed to lack a mitosome passage.'
  target_ids:
  - cellstructuremech:mitosome_intermembrane_space
  field_paths:
  - evidence[5].notes
  evidence_ids:
  - septin-record-mitosome_intermembrane_space
  - septin-original-mitosome_intermembrane_space
  - septin-tachezy2022-meta
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/mitosome_intermembrane_space.yaml
    role: maintained scientific record
  rule_id: .claude/skills/review-yaml-record/SKILL.md:exact source identity
  native_severity: minor
  normalization_reason: Minor bibliographic title/attribution error; no wrong compartment
    identity or demonstrated false distribution follows from the access limitation.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T024027Z-mitosome-intermembrane-space-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2742
- finding_id: septin-mitosome_matrix-F1
  issue_key: mitosome-matrix-tachezy-title
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Correct the title attached to DOI10.1111/jeu.12922
  description: 'The evidence note calls this article Hydrogenosomes and mitosomes:
    Mitochondria of anaerobic eukaryotes. Exact native metadata identifies The hydrogenosome
    of Trichomonas vaginalis by Tachezy, Makki and Hrdy (2022). The DOI is valid;
    its unread full body is not presumed to lack a mitosome passage.'
  target_ids:
  - cellstructuremech:mitosome_matrix
  field_paths:
  - evidence[5].notes
  evidence_ids:
  - septin-record-mitosome_matrix
  - septin-original-mitosome_matrix
  - septin-tachezy2022-meta
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/mitosome_matrix.yaml
    role: maintained scientific record
  rule_id: .claude/skills/review-yaml-record/SKILL.md:exact source identity
  native_severity: minor
  normalization_reason: Minor bibliographic title/attribution error; no wrong compartment
    identity or demonstrated false distribution follows from the access limitation.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T024029Z-mitosome-matrix-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2743
- finding_id: septin-mitosome_outer_membrane-F1
  issue_key: mitosome-outer-membrane-tachezy-title
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Correct the title attached to DOI10.1111/jeu.12922
  description: 'The evidence note calls this article Hydrogenosomes and mitosomes:
    Mitochondria of anaerobic eukaryotes. Exact native metadata identifies The hydrogenosome
    of Trichomonas vaginalis by Tachezy, Makki and Hrdy (2022). The DOI is valid;
    its unread full body is not presumed to lack a mitosome passage.'
  target_ids:
  - cellstructuremech:mitosome_outer_membrane
  field_paths:
  - evidence[6].notes
  evidence_ids:
  - septin-record-mitosome_outer_membrane
  - septin-original-mitosome_outer_membrane
  - septin-tachezy2022-meta
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/mitosome_outer_membrane.yaml
    role: maintained scientific record
  rule_id: .claude/skills/review-yaml-record/SKILL.md:exact source identity
  native_severity: minor
  normalization_reason: Minor bibliographic title/attribution error; no wrong compartment
    identity or demonstrated false distribution follows from the access limitation.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T024030Z-mitosome-outer-membrane-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2744
- finding_id: plaque-t5-F1
  issue_key: mucocyst-1
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Correct the MDL1 protein example
  description: The MDD component names MDL1 but its protein example I7M6L0 carries
    TTHERM_00471830. Kuppannan explicitly names MDL1 as TTHERM_00658810,346aa; native
    UniProt resolves that locus to I7MM25. I7M6L0 is392aa and matches the S5A/Rpn10
    proteasome family. Its role and evidence notes incorrectly assert a literature-gene
    equivalence despite passing native field correspondence.
  target_ids:
  - GO:0036000
  field_paths:
  - components[3].protein_examples[0]
  evidence_ids:
  - plaque-current-5
  - plaque-original-5
  - plaque-protein-I7M6L0
  - plaque-family-I7M6L0
  - plaque-IPR027040
  - plaque-kuppannan2022-body
  - plaque-query-MDL1-locus
  - plaque-protein-I7MM25
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/mucocyst.yaml
    role: maintained scientific record
  rule_id: .claude/skills/review-yaml-record/SKILL.md:exact identity and claim-level
    support
  native_severity: major
  normalization_reason: Major wrong concrete protein identity.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T024032Z-mucocyst-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2747
- finding_id: micro-F1
  issue_key: multivesicular-body-intraluminal-vesicle-unused-exact-go-identity
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Reconcile the local identity with exact native GO:0097487
  description: The maintained local identifier denotes the same biological entity
    as active GO:0097487. The candidate definition, ancestry and MVB parthood match;
    this is not a broader or merely label-similar term. An ignored-inclusive corpus
    search finds no existing use of the exact GO term. The record therefore misses
    the repository-required exact GO identity, while its biological boundary remains
    correct.
  target_ids:
  - cellstructuremech:multivesicular_body_intraluminal_vesicle
  field_paths:
  - identifier
  - definition_source
  - causal_graphs[0].nodes
  evidence_ids:
  - micro-record-multivesicular_body_intraluminal_vesicle
  - micro-go
  - micro-go-0097487-isa
  - micro-local-identity-search
  - micro-policy
  - micro-identifier-preservation
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/multivesicular_body_intraluminal_vesicle.yaml
    role: maintained scientific record
  rule_id: CLAUDE.md:GO cellular component first; docs/CURATION.md:Identifiers rules1–3
  native_severity: major
  normalization_reason: This is a concrete exact ontology-identity grounding defect
    under the native GO-first rule, not an empty optional component slot or wrong
    biological boundary. It is not a blocker because the existing local identity is
    valid and resolves uniquely.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T024034Z-multivesicular-body-intraluminal-vesicle-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2745
- finding_id: micro-F2
  issue_key: multivesicular-body-lumen-unused-exact-go-identity
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Reconcile the local identity with exact native GO:0097486
  description: The maintained local identifier denotes the same biological entity
    as active GO:0097486. The candidate definition, ancestry and MVB parthood match;
    this is not a broader or merely label-similar term. An ignored-inclusive corpus
    search finds no existing use of the exact GO term. The record therefore misses
    the repository-required exact GO identity, while its biological boundary remains
    correct.
  target_ids:
  - cellstructuremech:multivesicular_body_lumen
  field_paths:
  - identifier
  - definition_source
  - causal_graphs[0].nodes
  evidence_ids:
  - micro-record-multivesicular_body_lumen
  - micro-go
  - micro-go-0097486-isa
  - micro-local-identity-search
  - micro-policy
  - micro-identifier-preservation
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/multivesicular_body_lumen.yaml
    role: maintained scientific record
  rule_id: CLAUDE.md:GO cellular component first; docs/CURATION.md:Identifiers rules1–3
  native_severity: major
  normalization_reason: This is a concrete exact ontology-identity grounding defect
    under the native GO-first rule, not an empty optional component slot or wrong
    biological boundary. It is not a blocker because the existing local identity is
    valid and resolves uniquely.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T024034Z-multivesicular-body-lumen-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2746
actions:
- action_id: septin-mitosome_inner_membrane-A1
  finding_ids:
  - septin-mitosome_inner_membrane-F1
  target_ids:
  - cellstructuremech:mitosome_inner_membrane
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/mitosome_inner_membrane.yaml
    role: maintained scientific record
  description: Correct the bibliographic title/authorship for the retained DOI. Independently
    verify or replace its use for broad mitosome distribution without claiming unread
    full text proves absence.
  acceptance_checks:
  - Confirm the retained DOI/title/author identity against native metadata.
  - Run focused schema, strict and graph checks after separately authorized curation.
- action_id: septin-mitosome_intermembrane_space-A1
  finding_ids:
  - septin-mitosome_intermembrane_space-F1
  target_ids:
  - cellstructuremech:mitosome_intermembrane_space
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/mitosome_intermembrane_space.yaml
    role: maintained scientific record
  description: Correct the bibliographic title/authorship for the retained DOI. Independently
    verify or replace its use for broad mitosome distribution without claiming unread
    full text proves absence.
  acceptance_checks:
  - Confirm the retained DOI/title/author identity against native metadata.
  - Run focused schema, strict and graph checks after separately authorized curation.
- action_id: septin-mitosome_matrix-A1
  finding_ids:
  - septin-mitosome_matrix-F1
  target_ids:
  - cellstructuremech:mitosome_matrix
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/mitosome_matrix.yaml
    role: maintained scientific record
  description: Correct the bibliographic title/authorship for the retained DOI. Independently
    verify or replace its use for broad mitosome distribution without claiming unread
    full text proves absence.
  acceptance_checks:
  - Confirm the retained DOI/title/author identity against native metadata.
  - Run focused schema, strict and graph checks after separately authorized curation.
- action_id: septin-mitosome_outer_membrane-A1
  finding_ids:
  - septin-mitosome_outer_membrane-F1
  target_ids:
  - cellstructuremech:mitosome_outer_membrane
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/mitosome_outer_membrane.yaml
    role: maintained scientific record
  description: Correct the bibliographic title/authorship for the retained DOI. Independently
    verify or replace its use for broad mitosome distribution without claiming unread
    full text proves absence.
  acceptance_checks:
  - Confirm the retained DOI/title/author identity against native metadata.
  - Run focused schema, strict and graph checks after separately authorized curation.
- action_id: plaque-t5-A1
  finding_ids:
  - plaque-t5-F1
  target_ids:
  - GO:0036000
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/mucocyst.yaml
    role: maintained scientific record
  description: Replace or remove the wrong protein example and its MDL1 attribution.
    If using the exact-locus I7MM25 candidate, retain its verified UNREVIEWED status,
    SB210 taxon, native protein name and locus; cite the primary paper for the MDL1
    mapping and membership. Do not replace the complete MDD complex identity with
    one subunit.
  acceptance_checks:
  - Verify exact paper locus, native identity and claim-specific source scope.
  - After separately authorized curation, run focused schema/strict and native protein
    verification; native success alone does not validate literature-symbol attribution.
- action_id: micro-A1
  finding_ids:
  - micro-F1
  target_ids:
  - cellstructuremech:multivesicular_body_intraluminal_vesicle
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/multivesicular_body_intraluminal_vesicle.yaml
    role: maintained scientific record
  description: 'In separately authorized curation, reconcile the entity with GO:0097487
    using the documented identifier-preserving supersession process: retain the old
    local record as DEPRECATED and create or adopt the exact-GO successor with replaces.
    Coordinate references and evidence to the successor without silently reusing or
    renaming the old identifier. Preserve the verified lumen/vesicle boundary, species
    scope and optional lipid mapping limits.'
  acceptance_checks:
  - The adopted GO definition still exactly matches the maintained biological entity;
    no broader class is substituted.
  - The old local identifier remains recoverable and the successor records replaces
    according to the curation contract.
  - Ignored-inclusive corpus reference checks and native schema/strict/history/product/identifier
    gates pass after any separately authorized migration.
- action_id: micro-A2
  finding_ids:
  - micro-F2
  target_ids:
  - cellstructuremech:multivesicular_body_lumen
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/multivesicular_body_lumen.yaml
    role: maintained scientific record
  description: 'In separately authorized curation, reconcile the entity with GO:0097486
    using the documented identifier-preserving supersession process: retain the old
    local record as DEPRECATED and create or adopt the exact-GO successor with replaces.
    Coordinate references and evidence to the successor without silently reusing or
    renaming the old identifier. Preserve the verified lumen/vesicle boundary, species
    scope and optional lipid mapping limits.'
  acceptance_checks:
  - The adopted GO definition still exactly matches the maintained biological entity;
    no broader class is substituted.
  - The old local identifier remains recoverable and the successor records replaces
    according to the curation contract.
  - Ignored-inclusive corpus reference checks and native schema/strict/history/product/identifier
    gates pass after any separately authorized migration.
limitations:
- 'Four mitosome compartment independent subreview: Read-only source review of four
  unchanged mitosome compartment targets. Root owns issue dedup/publication, repository
  writes and later gates. This report does not certify future saved-head, CI or queue
  outcomes.'
- 'Four mitosome compartment independent subreview: Current fresh authority metadata
  and complete abstracts are distinguished from two explicitly reused genuine public
  bodies. Reused Roger/Mi-ichi snapshots retain their actual original fetch times
  and checked hashes, with bounded current reinspection locators.'
- 'Four mitosome compartment independent subreview: Tovar1999 is complete primary
  abstract only; the exact attributed double-membrane observation remains unverified
  at original-body/pixel level. Current anatomical authority and later organelle research
  support topology/occurrence but do not silently substitute for that unread observation.'
- 'Four mitosome compartment independent subreview: Tachezy2022 is a complete secondary
  abstract plus exact bibliographic identity. Four wrong titles are certain; unread
  full-body mitosome coverage is unknown, not refuted. Each maintained target retains
  its own exact predecessor finding and action.'
- 'Four mitosome compartment independent subreview: Mi-ichi2009 reused body was re-read
  only at Results sec2/sec3 and Methods sec10/sec13, including Fig1 text caption.
  Partial enriched-fraction proteomics, contamination/heterogeneity and strain HM-1:IMSScl6
  are explicit. No source pixels, supplements or full paper are newly claimed read.'
- 'Four mitosome compartment independent subreview: Roger2017 reused secondary PDF
  was re-read at R1184 opening Diversity paragraphs and R1186 reduction/mitosome comparison
  paragraphs (text lines630–645 and868–896). This supports qualitative diversity,
  not numerical frequency or new primary experiments.'
- 'Four mitosome compartment independent subreview: All eight native protein commands
  pass on empty represented scopes: zero protein examples, typed molecular nodes and
  UniProtKB graph xrefs in all four records. This is not universal molecular or scientific
  certification. No optional protein inventory, family grounding or complex enum finding
  is invented.'
- 'Four mitosome compartment independent subreview: Inner/outer membrane ESSENTIAL
  applies to the collective lipid bilayer constituent. No exact lipid species, stoichiometry,
  lineage-specific composition or depletion/formation requirement is measured. Label-only
  chemical identity is intentionally retained; whole membranes are not used as lipid
  groundings.'
- 'Four mitosome compartment independent subreview: All four original adapter outcomes
  are genuinely not applicable to the complete physical/material assertions; their
  rationale is clarified without a defect. Fresh catalogue noncoverage is supplemental
  scope evidence, not negative biology. Historical00:49Z runner failure is not a fresh
  execution.'
- 'Four mitosome compartment independent subreview: All31 actually used repository
  inputs were frozen before use:17 common policies/schema/scripts,4 targets,8 original
  artifacts and2 boundary neighbors. Whole mitosome/envelope scientific findings and
  grouped historical issues are not disposed by this compartment review.'
- 'Mononeme and mucocyst independent subreview: Both assigned records are unchanged.
  Mononeme remains pass_with_limitations; mucocyst needs_curation for exact inherited
  major mucocyst-1 only. No new scientific finding or unresolved stale refresh in
  this slice.'
- 'Mononeme and mucocyst independent subreview: Both originals validate/render exactly
  and each14 historical inputs matches retained source. No records/original bundles
  modified; prior history mentions do not create terminal disposition of unfrozen
  older reviews.'
- 'Mononeme and mucocyst independent subreview: All declared public snapshots are
  fresh at their individual recorded timestamps. Guessed Singh/Rahaman S3 paths returned404;
  genuine matching PMC HTML fallback was inspected. Other mucocyst bodies are genuine
  JATS. Source-tier locators state exactly read sections.'
- 'Mononeme and mucocyst independent subreview: No figure pixels, supplementary movies/tables,
  raw spectra or quantitative image reanalysis. Captions were read only as specified.
  No maintained image-copy/license claim exists in these targets.'
- 'Mononeme and mucocyst independent subreview: Singh uses tagged full-length PfROM1
  in3D7 and supports mature-segmenter localization/post-release redistribution. Proximity
  is not motor causality or universal invasion necessity. Primary mucocyst findings
  retain laboratory strain, tag, stimulation and biochemical preparation limits.'
- 'Mononeme and mucocyst independent subreview: Fresh UniProt examples retain UNREVIEWED
  status, native names, loci and species/strain distinctions. Exact MDL1 gene-name
  query returned zero but exact paper-locus query resolved I7MM25; no inference of
  absent MDL1 biology. Wrong native I7M6L0 attribution independently confirmed by
  paper locus/length and PSMD4 family.'
- 'Mononeme and mucocyst independent subreview: P90618 InterPro request returned204
  with curl92 invalid HTTP/2 header and zero received body bytes; no saved body. Q2I2L7
  returned429 throttling. These are inconclusive, not negative family evidence. Successful
  UniProt cross-references and primary support are independently described.'
- 'Mononeme and mucocyst independent subreview: Four root native commands pass with
  populated inventory: mononeme1example/1covered node, mucocyst6examples/3covered
  nodes. Native coverage does not certify literature-gene mapping; MDD remains COVERED
  syntactically despite scientific identity finding.'
- 'Mononeme and mucocyst independent subreview: Both original explicit expression-only
  exclusions need review coverage correction. Fresh complete catalogue contains no
  exact eukaryotic hosts, so no matched downstream query applies. No foreign-strain
  proxy or inferred negative biology. Historical00:49Z runner PermissionError is not
  a fresh invocation.'
- 'Mononeme and mucocyst independent subreview: Optional exact lipid/family/complex
  grounding and exhaustive mature-protein inventories are not automatically mandatory
  defects. Native graph schema allows protein complexes/families in GENE_OR_PROTEIN;
  no enum-only finding.'
- 'Mononeme and mucocyst independent subreview: Root owns full QC, issue linkage,
  successor authoring, final CI and merge. This report binds independent current source
  review and scratch native preflight only; no premature final-head/queue certification.'
- 'Multivesicular body and three boundary compartment independent subreview: All four
  assigned MVB records are unchanged and independently reassessed. Exactly two inherited
  major exact-GO identity findings remain open with full original repository/review/F1
  lineage; no new scientific finding or terminal neighbor/category disposition.'
- 'Multivesicular body and three boundary compartment independent subreview: Katzmann2001
  and Babst2002 were inspected at complete primary-abstract tier, Henne2011 at complete
  secondary-review abstract tier. Exact DOI HTTP200 responses are Article Locator
  redirects without body; publisher routes return403. An exploratory wrong Henne PII
  route is not used as evidence; the exact publisher URL was subsequently obtained
  from the DOI and independently attempted. Bounded public-search leads did not add
  scientific body evidence. No unread Methods, precise strain, direct scission assay
  or universal mechanism certified.'
- 'Multivesicular body and three boundary compartment independent subreview: Teo2004
  fresh genuine PDF was read at p559 and complete pp564-567 including Figure4-6 captions
  and experimental procedures; no pixels, remaining structural Results or supplements.
  Direct recombinant-protein and bovine-brain-liposome binding is not complete in-vivo
  ILV scission; Figure6 is explicitly a model. E.coli expression hosts are not maintained
  MVB taxonomic exemplars.'
- 'Multivesicular body and three boundary compartment independent subreview: GO/UniProt
  location definitions support exact entity/topology and coarse sorting scope. Mixed
  is_a/part_of ancestor lists were not used to invent direct relation types; candidate
  is_a-only responses and typed MVB child relations were checked separately. COMMON
  is qualitative and no source supplies a current exhaustive prevalence census.'
- 'Multivesicular body and three boundary compartment independent subreview: All eight
  current native protein commands have zero protein examples and zero GENE_OR_PROTEIN
  nodes. GO-grounded ESCRT STRUCTURE actors are manually authority checked. No populated
  molecular inventory or experimental formation necessity is inferred from empty native
  verification.'
- 'Multivesicular body and three boundary compartment independent subreview: All four
  original adapter rows are explicit expression-only exclusions requiring corrected
  rationale. Fresh official catalogue has no actual Saccharomyces host coverage; no
  matched downstream query, bacterial surrogate or negative biology inference. Runner00:49Z
  failed execution remains historical; it was not repeated here.'
- 'Multivesicular body and three boundary compartment independent subreview: Constitutive
  collective lipid material remains separate from an exact molecular lipid identity,
  source-specific composition, protein membership and assembly necessity. Optional
  mapping TODOs and absent unasserted fields are not themselves findings.'
- 'Multivesicular body and three boundary compartment independent subreview: Exact
  GO migrations belong to separate authorized curation, retaining old local identities
  as deprecated with successor replaces and coordinated references. Current local
  sibling links resolve correctly; they are not broken links or duplicate independent
  findings.'
- 'Multivesicular body and three boundary compartment independent subreview: No record,
  original bundle, history, scientific status or generated product was edited. Root
  owns globalQC, GitHub issues, final-head CI, queue and merge; this source report
  does not precertify later gates. Scratch native validation/render verifies format/provenance,
  not automatic scientific truth.'
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
  and pushed without force. None of the ten target hashes differs from its original
  frozen input; no stale-review issue is invented.
- This explicit issue-bearing ten-record cohort follows native persistence policy.
  Inherited scientific findings retain stable keys and exact predecessor repository/review/finding
  identities; any new finding has no invented predecessor.
- Bundle issue2740 tracks the six unsupported structured-source applicability exclusions.
  The immutable successor addresses them and clarifies the four genuine exclusions
  without record changes.
- 'Six expression-only structured-source exclusions require correction: mononeme,
  mucocyst and the four MVB records make positive protein/pathway claims. All four
  mitosome compartments have genuine collective-material/spatial-topology scope and
  explicitly exclude molecular machinery. No defect is invented for those four exclusions.'
- Source commit d6a41b5d3397c9d62944c9c21890ef47a097a0fa is retained by tag review-base/pr2371-current-record-followup-20261103.
- CLAUDE.md aliases AGENTS.md; canonical regular AGENTS.md bytes are frozen. Every
  used local context input is frozen before its assessment.
- Fresh and reused source snapshots retain actual access times and inspection tiers.
  Native identifier identity does not independently establish structure membership,
  experimental intervention scope or assembly necessity.
- All twenty native protein commands returned zero. Mononeme has one unreviewed example
  and one COVERED typed node; mucocyst has six unreviewed examples and three COVERED
  typed nodes. The other eight records have zero examples and zero typed molecular
  nodes. Native field correspondence does not certify the MDL1 literature-to-locus
  equivalence.
- Exact MVB ontology-identity findings require separately authorized identifier-preserving
  migration. No identifier is silently replaced, neighbor record changed or current
  scientific record edited in this review-only PR.
- Current CausalNode schema permits protein families and complexes as GENE_OR_PROTEIN
  nodes. Complex or machinery typing alone is not a scientific defect. Optional protein/chemical
  slots and unread-source absence are not invented findings.
- Native-validator2514 remains open and reused. Related curation issues on whole mitosome/envelope
  and other records do not dispose of the present child-record findings.
- Final trusted-base review-check, exact-head independent acceptance, final-head CI
  and merge-group CI occur after this immutable observation and are not represented
  as already completed.
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T024026Z-mitosome-inner-membrane-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T024027Z-mitosome-intermembrane-space-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T024029Z-mitosome-matrix-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T024030Z-mitosome-outer-membrane-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T024031Z-mononeme-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T024032Z-mucocyst-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T024033Z-multivesicular-body-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T024034Z-multivesicular-body-intraluminal-vesicle-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T024034Z-multivesicular-body-lumen-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T024035Z-multivesicular-body-membrane-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
links:
- https://github.com/CultureBotAI/CellStructureMech/pull/2371
- https://github.com/CultureBotAI/CellStructureMech/issues/2514
- https://github.com/CultureBotAI/CellStructureMech/issues/2740
- https://github.com/CultureBotAI/CellStructureMech/issues/2741
- https://github.com/CultureBotAI/CellStructureMech/issues/2742
- https://github.com/CultureBotAI/CellStructureMech/issues/2743
- https://github.com/CultureBotAI/CellStructureMech/issues/2744
- https://github.com/CultureBotAI/CellStructureMech/issues/2745
- https://github.com/CultureBotAI/CellStructureMech/issues/2746
- https://github.com/CultureBotAI/CellStructureMech/issues/2747
```
