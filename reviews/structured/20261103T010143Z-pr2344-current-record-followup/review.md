# PR 2344: current review of ten cytoskeletal records and adversarial follow-up

- Review: 20261103T010143Z-pr2344-current-record-followup
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-11-03T00:42:43Z
- Finished UTC: 2026-11-03T01:01:43Z
- Reviewer: Codex root synthesis with three independent read-only adversarial reviewers (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Current-input reassessment of all ten records in PR 2344, including three changed since their frozen reviews. Seven scientific curation findings remain: one major unsupported vesicular hydrolase export mechanism, two minor mitotic-cell-cycle wording ambiguities, and four minor septin findings retained with exact lineage. Four records have supported qualified current assessments; six require curation. The original ten immutable bundles remain historical observations. This issue-bearing batch supplies the refreshed assessment, acknowledges missed historical defects, and corrects the adapter-coverage rationale without changing scientific records.

## Scope And Provenance

Entire ten-record PR cohort, not a corpus sample. The original frozen records and review claims are compared with current main 4efb30b376d650109f5df154cf95fc382e714ca2; every changed scientific assertion is reassessed. Full records, original assessments and current source scope are inspected. No curation or native status promotion.

Selection: Exactly the ten target paths in PR 2344 original head 5b50c32ef35f6ef410dd16a3819d71b9f08b970c; deterministic path order. Current main contains 1022 records; only these ten are in scope.
Coverage: full; 10 reviewed / 10 in the declared population.
Source: working_tree at Git base dab5276568439756fa032e736df085fc75e0e271.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0061497 | data/structures/cytoskeleton/inner_plaque_of_mitotic_spindle_pole_body.yaml | maintained | inner plaque of mitotic spindle pole body |
| GO:0005822 | data/structures/cytoskeleton/inner_plaque_of_spindle_pole_body.yaml | maintained | inner plaque of spindle pole body |
| GO:0061498 | data/structures/cytoskeleton/intermediate_layer_of_mitotic_spindle_pole_body.yaml | maintained | intermediate layer of mitotic spindle pole body |
| GO:0005821 | data/structures/cytoskeleton/intermediate_layer_of_spindle_pole_body.yaml | maintained | intermediate layer of spindle pole body |
| GO:0031021 | data/structures/cytoskeleton/interphase_microtubule_organizing_center.yaml | maintained | interphase microtubule organizing center |
| GO:1990819 | data/structures/cytoskeleton/mating_projection_actin_fusion_focus.yaml | maintained | mating projection actin fusion focus |
| GO:0032175 | data/structures/cytoskeleton/mating_projection_septin_ring.yaml | maintained | mating projection septin ring |
| GO:0036391 | data/structures/cytoskeleton/medial_cortex_septin_ring.yaml | maintained | medial cortex septin ring |
| GO:0097568 | data/structures/cytoskeleton/median_body.yaml | maintained | median body |
| GO:0032152 | data/structures/cytoskeleton/meiotic_septin_complex.yaml | maintained | meiotic septin complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Structured adapter runner | failed | False | GO:0061497, GO:0005822, GO:0061498, GO:0005821, GO:0031021, GO:1990819, GO:0032175, GO:0036391, GO:0097568, GO:0032152 | Actual installed runner unavailable because OS denied pyvenv.cfg; direct source-native catalogue fallback inspected. |
| Organism-specific expression-module applicability | not_applicable | False | GO:0061497, GO:0005822, GO:0061498, GO:0005821, GO:0031021, GO:1990819, GO:0032175, GO:0036391, GO:0097568, GO:0032152 | The inspected native catalogue has no matching yeast or Giardia dataset. Downstream organism/component searches were not run; no phenotype or mechanism absence is inferred. |
| Frozen input comparison and reassessment | passed | True | GO:0061497, GO:0005822, GO:0061498, GO:0005821, GO:0031021, GO:1990819, GO:0032175, GO:0036391, GO:0097568, GO:0032152 | Ten exact hashes compared with fetched main; three changed targets reassessed against source-specific evidence and all ten receive current assessments. |
| Full native QC after complete historical-object hydration | passed | True | GO:0061497, GO:0005822, GO:0061498, GO:0005821, GO:0031021, GO:1990819, GO:0032175, GO:0036391, GO:0097568, GO:0032152 | Full native QC after complete historical-object hydration exit 0. See exact logged result and limitations; native zero is not universal source or identifier coverage. |
| Ontology label correspondence | passed | True | GO:0061497, GO:0005822, GO:0061498, GO:0005821, GO:0031021, GO:1990819, GO:0032175, GO:0036391, GO:0097568, GO:0032152 | Exit0: 4232 canonical, 50 synonym and 9 exception matches; 923 pairs skipped because no adapter. Native success does not mean every identifier was checked. |
| TraitMech cross-references | passed | True | GO:0061497, GO:0005822, GO:0061498, GO:0005821, GO:0031021, GO:1990819, GO:0032175, GO:0036391, GO:0097568, GO:0032152 | TraitMech cross-references exit 0. See exact logged result and limitations; native zero is not universal source or identifier coverage. |
| Pinned governed-file sync | passed | True | GO:0061497, GO:0005822, GO:0061498, GO:0005821, GO:0031021, GO:1990819, GO:0032175, GO:0036391, GO:0097568, GO:0032152 | Pinned governed-file sync exit 0. See exact logged result and limitations; native zero is not universal source or identifier coverage. |
| Supplemental full-corpus identifier scan result pending | unavailable | False | GO:0061497, GO:0005822, GO:0061498, GO:0005821, GO:0031021, GO:1990819, GO:0032175, GO:0036391, GO:0097568, GO:0032152 | Started 2026-11-03T00:45:51+00:00; running without a final result at finished_at. Target-specific authority responses were separately inspected. Final publication waits for the scan and records its result in the PR. |
| Identifier CI on merged-main head | passed | False | GO:0061497, GO:0005822, GO:0061498, GO:0005821, GO:0031021, GO:1990819, GO:0032175, GO:0036391, GO:0097568, GO:0032152 | Exact main-merge head dab52765 workflow completed successfully;6173 OK and254 SKIPPED in native report. This is not the final amended-head CI or a completed local cold-cache result. |
| validate inner plaque of mitotic spindle pole body | passed | True | GO:0061497 | Native focused check exit 0. |
| validate-strict inner plaque of mitotic spindle pole body | passed | True | GO:0061497 | Native focused check exit 0. |
| validate inner plaque of spindle pole body | passed | True | GO:0005822 | Native focused check exit 0. |
| validate-strict inner plaque of spindle pole body | passed | True | GO:0005822 | Native focused check exit 0. |
| validate intermediate layer of mitotic spindle pole body | passed | True | GO:0061498 | Native focused check exit 0. |
| validate-strict intermediate layer of mitotic spindle pole body | passed | True | GO:0061498 | Native focused check exit 0. |
| validate intermediate layer of spindle pole body | passed | True | GO:0005821 | Native focused check exit 0. |
| validate-strict intermediate layer of spindle pole body | passed | True | GO:0005821 | Native focused check exit 0. |
| validate interphase microtubule organizing center | passed | True | GO:0031021 | Native focused check exit 0. |
| validate-strict interphase microtubule organizing center | passed | True | GO:0031021 | Native focused check exit 0. |
| validate mating projection actin fusion focus | passed | True | GO:1990819 | Native focused check exit 0. |
| validate-strict mating projection actin fusion focus | passed | True | GO:1990819 | Native focused check exit 0. |
| validate mating projection septin ring | passed | True | GO:0032175 | Native focused check exit 0. |
| validate-strict mating projection septin ring | passed | True | GO:0032175 | Native focused check exit 0. |
| validate medial cortex septin ring | passed | True | GO:0036391 | Native focused check exit 0. |
| validate-strict medial cortex septin ring | passed | True | GO:0036391 | Native focused check exit 0. |
| validate median body | passed | True | GO:0097568 | Native focused check exit 0. |
| validate-strict median body | passed | True | GO:0097568 | Native focused check exit 0. |
| validate meiotic septin complex | passed | True | GO:0032152 | Native focused check exit 0. |
| validate-strict meiotic septin complex | passed | True | GO:0032152 | Native focused check exit 0. |

## Scientific And Domain Assessments

### inner plaque of mitotic spindle pole body current assessment

scope: concern. Targets: GO:0061497.

Exact identity and is-a/parthood remain supported by native GO. S. cerevisiae is an example; S288C candidate-protein identity is not generalized. Inner-plaque anchoring and intermediate-layer CP/IL2 model boundaries are preserved; InterPro domains/families and generic gamma-TuSC counts do not establish plaque-wide stoichiometry. Minor ambiguity remains: mitosis-specific wording can imply M-phase restriction although the subtype denotes the mitotic cell cycle; request separate wording curation.

### inner plaque of spindle pole body current assessment

scope: supported. Targets: GO:0005822.

Exact identity and is-a/parthood remain supported by native GO. S. cerevisiae is an example; S288C candidate-protein identity is not generalized. Inner-plaque anchoring and intermediate-layer CP/IL2 model boundaries are preserved; InterPro domains/families and generic gamma-TuSC counts do not establish plaque-wide stoichiometry. No new issue observed within these source and access limits; qualified support retained.

### intermediate layer of mitotic spindle pole body current assessment

scope: concern. Targets: GO:0061498.

Exact identity and is-a/parthood remain supported by native GO. S. cerevisiae is an example; S288C candidate-protein identity is not generalized. Inner-plaque anchoring and intermediate-layer CP/IL2 model boundaries are preserved; InterPro domains/families and generic gamma-TuSC counts do not establish plaque-wide stoichiometry. Minor ambiguity remains: mitosis-specific wording can imply M-phase restriction although the subtype denotes the mitotic cell cycle; request separate wording curation.

### intermediate layer of spindle pole body current assessment

scope: supported. Targets: GO:0005821.

Exact identity and is-a/parthood remain supported by native GO. S. cerevisiae is an example; S288C candidate-protein identity is not generalized. Inner-plaque anchoring and intermediate-layer CP/IL2 model boundaries are preserved; InterPro domains/families and generic gamma-TuSC counts do not establish plaque-wide stoichiometry. No new issue observed within these source and access limits; qualified support retained.

### interphase microtubule organizing center current full-record reassessment

graph: supported. Targets: GO:0031021.

Current STRUCTURE node for gamma_tuc agrees with complex identity and component type. Historical GO definition remains bounded to S. pombe/example context. Bao supports distinct inactive 9A1-NE docking, active Mto1[NE] nucleation and full-length cold regrowth; Liu supports reciprocal Alp7/Mto1 and Alp14 localization under MBC recovery with residual stubs and partial rescue; Lynch supports engineered bonsai CM1/Mto2-dependent activation and bounded copy estimates; Shen and Nie support dynamic Rsp1 site/dose effects and distinguish whole-cell deletion from Klp2-dependent lattice recruitment. All eight current UniProt reference identities are reviewed entries in taxon284812. IPR045110 is XMAP215 family; IPR024312 is a domain; IPR051964 is broad and its description LLM-generated. Tracked Figure6 visually inspected; panel contexts agree.

### mating projection actin fusion focus current full-record reassessment

graph: concern. Targets: GO:1990819.

Original frozen-input assessment is scientifically sound within stated limits. Current record retains exact GO focus identity, part_of topology, actin and motor identities, Fus1-dependent aster and myosin focalization. The newly added hydrolase-to-dissolution edge overstates the known export route (F7). Joint Myo51/Myo52 focalization remains distinct from tested Myo52-tail cargo localization; no equivalent direct transport by both motors is established.

### median body current full-record reassessment

graph: supported. Targets: GO:0097568.

Current Q969B0 addition is a verified reviewed kin-13 exemplar in species5741, preserving distinction between protein identifier and membership evidence. UniProt labels it Fragment and identifies Polish sequence source; Park2022 WB/ATCC30957 localization supports the current citation without claiming that the exemplar sequence is the experimental strain. Dawson2007 demonstrates GFP Kin13/EB1 median-body localization and 48h S280N volume reduction while early-mitotic arrays can elongate/persist. Giardia synonyms remain accepted; GO identity and topology agree. The later review retains an enigmatic function and labels reservoir support as a hypothesis; a definite physiological function need not be invented.

### mating projection septin ring current scope and grounding

grounding: concern. Targets: GO:0032175.

Exact localized identity and hierarchy are supported and unchanged. Generic septin proteins can be grounded at family level without resolving complete assembly membership; retain the original minor finding and its separate unresolved species/paralogue/accessory boundary. The proposed mating-barrier qualification is still needed; primary interaction/localization results do not demonstrate diffusion exclusion.

### medial cortex septin ring current scope and grounding

grounding: concern. Targets: GO:0036391.

Exact localized identity and hierarchy are supported and unchanged. Generic septin proteins can be grounded at family level without resolving complete assembly membership; retain the original minor finding and its separate unresolved species/paralogue/accessory boundary. Secondary literature supplies bounded contextual support, not proof of a universal mechanism or inventory.

### meiotic septin complex current scope and grounding

grounding: concern. Targets: GO:0032152.

Exact localized identity and hierarchy are supported and unchanged. Generic septin proteins can be grounded at family level without resolving complete assembly membership; retain the original minor finding and its separate unresolved species/paralogue/accessory boundary. Secondary literature supplies bounded contextual support, not proof of a universal mechanism or inventory.

### Historical iMTOC oversight and current correction

representation: supported. Targets: GO:0031021.

The original iMTOC clean assessment missed the frozen gamma_tuc GENE_OR_PROTEIN mismatch. Current main has already corrected that PROTEIN_COMPLEX/GO:0000930 node to STRUCTURE under issue2404. This follow-up explicitly assesses the corrected bytes; it neither retroactively changes the old verdict nor reopens completed scientific curation.

## Findings

### F1: Generic septin family grounding is withheld for an unresolved localized cohort

minor / open / confirmed; issue key: mating-projection-septin-ring-generic-family-withheld.

The component is declared as septin proteins, but its grounding rationale requires resolving all ring-forming fungal paralogues before assigning a family. Native IPR016491 already identifies this generic class. Localized membership, exact paralogues and accessory boundaries remain separate questions and do not prevent class-level grounding.

### F2: The function wording upgrades a proposed barrier role

minor / open / confirmed; issue key: mating-projection-septin-ring-barrier-qualification.

The function says the ring can act as a barrier and its GO evidence note states the barrier role without qualification. Native GO says may, Douglas presents this as a model, and the target definition itself retains that uncertainty. The inspected 1997 interaction/localization experiments do not establish diffusion exclusion. Restore the same uncertainty at the function assertion; this does not reject the proposed role.

### F3: Assembly-cohort criterion leaves generic Septin family ungrounded

minor / open / confirmed; issue key: medial-cortex-septin-ring-family-grounding-scope.

The generic septin-proteins row is REVIEWED_LABEL_ONLY while the rationale waits for an exact accession for its complete developmental or localized cohort. Native IPR016491 identifies the named generic Septin family. Reconcile that mapping with the status, notes and TODO, retaining the separate unresolved species-specific and accessory inventory.

### F4: Assembly-cohort criterion leaves generic Septin family ungrounded

minor / open / confirmed; issue key: meiotic-septin-complex-family-grounding-scope.

The generic septin-proteins row is REVIEWED_LABEL_ONLY while the rationale waits for an exact accession for its complete developmental or localized cohort. Native IPR016491 identifies the named generic Septin family. Reconcile that mapping with the status, notes and TODO, retaining the separate unresolved species-specific and accessory inventory.

### F5: Mitotic-cell-cycle subtype wording can imply M-phase restriction

minor / open / confirmed; issue key: inner-plaque-of-mitotic-spindle-pole-body-phase-wording.

The graph description, first edge description and boundary resolution say mitosis-specific. GO denotes the mitotic-cell-cycle SPB subtype. This bounded wording ambiguity can imply narrower M-phase restriction; it is not proof the author intended exclusivity. The original review explained correct scope but did not make the discrepancy actionable.

### F6: Mitotic-cell-cycle subtype wording can imply M-phase restriction

minor / open / confirmed; issue key: intermediate-layer-of-mitotic-spindle-pole-body-phase-wording.

The graph description, first edge description and boundary resolution say mitosis-specific. GO denotes the mitotic-cell-cycle SPB subtype. This bounded wording ambiguity can imply narrower M-phase restriction; it is not proof the author intended exclusivity. The original review explained correct scope but did not make the discrepancy actionable.

### F7: Hydrolase edge overstates a demonstrated vesicular export mechanism

major / open / confirmed; issue key: mating-focus-unproven-vesicular-hydrolase-export.

The added hydrolase-to-wall-dissolution edge says glucanase-containing secretory vesicles release hydrolases. Dudin2015 supports focal enrichment, Myo52-tail dependence and wall erosion, but Agn2, Eng2 and Exg3 lack signal sequences/transmembrane domains and their route outside the cell is unknown. The reviewed record must not upgrade likely cargo localization into established vesicle-mediated secretion.

## Recommended Actions And Acceptance Checks

### A1

Ground the generic septin-proteins component to verified IPR016491 using an appropriate native grounding status, and rewrite its rationale to preserve the unresolved localized cohort and accessory questions.

- The component label and family scope correspond to Septin.
- Do not infer taxon examples, paralogue membership, essentiality, stoichiometry or Afr1 inclusion from this family assignment.
- Preserve the GO:0032175 versus GO:0032162 boundary discussion.
- Run documented native schema, strict, label, history and generated-product checks after separately authorized curation.

### A2

Use may act or equivalent proposed-role wording in the function description and GO evidence note, retaining the specific shmoo-neck location and the proposed localization of mating factors.

- Definition, function description and evidence notes consistently identify the barrier as proposed.
- Do not add a demonstrated barrier edge, direct-binding assertion or obligatory Afr1 constituent claim.
- Keep ring-versus-band and experimental-example uncertainty explicit.
- Run documented native schema, strict, label, history and generated-product checks after separately authorized curation.

### A3

Under separately authorized curation, map the generic septin class to verified IPR016491 and reconcile status/notes/TODO while preserving unresolved assembly membership.

- Verify native Septin family name/type and retain independent structure-localization evidence.
- Do not infer a universal subunit set, copy count, taxonomic distribution or individual-paralog essentiality.
- Use the guarded scientific writer and append curation/history records; run native schema, strict, label, history and generated-page checks.

### A4

Under separately authorized curation, map the generic septin class to verified IPR016491 and reconcile status/notes/TODO while preserving unresolved assembly membership.

- Verify native Septin family name/type and retain independent structure-localization evidence.
- Do not infer a universal subunit set, copy count, taxonomic distribution or individual-paralog essentiality.
- Use the guarded scientific writer and append curation/history records; run native schema, strict, label, history and generated-page checks.

### A5

Separately curate the three fields to consistently say of the mitotic-cell-cycle SPB, retaining exact identity and topology.

- All three fields preserve whole mitotic-cell-cycle scope without unsupported M-phase exclusivity.
- Use guarded writer, append curation/history, regenerate products and run documented schema, strict, labels and QC gates in separate curation work.

### A6

Separately curate the three fields to consistently say of the mitotic-cell-cycle SPB, retaining exact identity and topology.

- All three fields preserve whole mitotic-cell-cycle scope without unsupported M-phase exclusivity.
- Use guarded writer, append curation/history, regenerate products and run documented schema, strict, labels and QC gates in separate curation work.

### A7

Separately restrict the edge and evidence note to demonstrated focal glucanase enrichment and local wall erosion; retain the unknown export route.

- No established vesicle-mediated export is asserted for Agn2/Eng2/Exg3.
- Preserve distinction between joint myosin focalization and Myo52-tail cargo experiments.
- Guarded writer, curation/history, native validation and regenerated products in separate curation PR.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record-0 | data/structures/cytoskeleton/inner_plaque_of_mitotic_spindle_pole_body.yaml; Entire current maintained YAML; exact input captured by native inspect | supports | Current record read in full. SHA-256 c7d1f6c1fa0f5928a0d3bc67d245eb0d3e655798fc62e719990248707765aff8. Original frozen hash c7d1f6c1fa0f5928a0d3bc67d245eb0d3e655798fc62e719990248707765aff8. Unchanged from original reviewed target bytes. |
| prior-0 | reviews/structured/20261021T073051Z-inner-plaque-of-mitotic-spindle-pole-body-audit/review.yaml; Original immutable YAML and derived Markdown; source, assessments, findings, actions, limitations | context_only | Original review is a historical observation, not evidence that current bytes or current validators were checked. |
| record-1 | data/structures/cytoskeleton/inner_plaque_of_spindle_pole_body.yaml; Entire current maintained YAML; exact input captured by native inspect | supports | Current record read in full. SHA-256 663b2ccb7bf2a427807d0156bb33feb5c96ce978649f091ed5a9a2b4723a0dba. Original frozen hash 663b2ccb7bf2a427807d0156bb33feb5c96ce978649f091ed5a9a2b4723a0dba. Unchanged from original reviewed target bytes. |
| prior-1 | reviews/structured/20261021T073051Z-inner-plaque-of-spindle-pole-body-audit/review.yaml; Original immutable YAML and derived Markdown; source, assessments, findings, actions, limitations | context_only | Original review is a historical observation, not evidence that current bytes or current validators were checked. |
| record-2 | data/structures/cytoskeleton/intermediate_layer_of_mitotic_spindle_pole_body.yaml; Entire current maintained YAML; exact input captured by native inspect | supports | Current record read in full. SHA-256 6babc40661cf4080adb6b1c5e18c42a78c7b1cffddae612a3288fee4926c98e5. Original frozen hash 6babc40661cf4080adb6b1c5e18c42a78c7b1cffddae612a3288fee4926c98e5. Unchanged from original reviewed target bytes. |
| prior-2 | reviews/structured/20261021T073051Z-intermediate-layer-of-mitotic-spindle-pole-body-audit/review.yaml; Original immutable YAML and derived Markdown; source, assessments, findings, actions, limitations | context_only | Original review is a historical observation, not evidence that current bytes or current validators were checked. |
| record-3 | data/structures/cytoskeleton/intermediate_layer_of_spindle_pole_body.yaml; Entire current maintained YAML; exact input captured by native inspect | supports | Current record read in full. SHA-256 3c889767d96b20dae86ccb3327892d5d33a5892591133cd4dcea4ad17a4b07c0. Original frozen hash 3c889767d96b20dae86ccb3327892d5d33a5892591133cd4dcea4ad17a4b07c0. Unchanged from original reviewed target bytes. |
| prior-3 | reviews/structured/20261021T073051Z-intermediate-layer-of-spindle-pole-body-audit/review.yaml; Original immutable YAML and derived Markdown; source, assessments, findings, actions, limitations | context_only | Original review is a historical observation, not evidence that current bytes or current validators were checked. |
| record-4 | data/structures/cytoskeleton/interphase_microtubule_organizing_center.yaml; Entire current maintained YAML; exact input captured by native inspect | supports | Current record read in full. SHA-256 5ef265cc6fcc3c2c281479cd4aeacaa5d770d1f3a4a682a37a2d897e1562ba75. Original frozen hash e16c54c5053f30b3da52fae3a7b2eeb0afb18d2580bff4e95d3b69071160b7ca. Changed: reassessed current delta against primary sources. |
| prior-4 | reviews/structured/20261021T073259Z-interphase-microtubule-organizing-center-audit/review.yaml; Original immutable YAML and derived Markdown; source, assessments, findings, actions, limitations | context_only | Original review is a historical observation, not evidence that current bytes or current validators were checked. |
| record-5 | data/structures/cytoskeleton/mating_projection_actin_fusion_focus.yaml; Entire current maintained YAML; exact input captured by native inspect | supports | Current record read in full. SHA-256 7cb7ba894d0912377f74951bc82404b93d14333ff28363d0e2082e7f65f1f6bf. Original frozen hash e0b5696c74beabb751e5334fd04492a057d4b3fceeedf87f7b1c59978e172b1e. Changed: reassessed current delta against primary sources. |
| prior-5 | reviews/structured/20261021T073259Z-mating-projection-actin-fusion-focus-audit/review.yaml; Original immutable YAML and derived Markdown; source, assessments, findings, actions, limitations | context_only | Original review is a historical observation, not evidence that current bytes or current validators were checked. |
| record-6 | data/structures/cytoskeleton/mating_projection_septin_ring.yaml; Entire current maintained YAML; exact input captured by native inspect | supports | Current record read in full. SHA-256 1829e9907009f5d72966b7b14936288c5bb5d141ea0fb043058a6e1939a078b6. Original frozen hash 1829e9907009f5d72966b7b14936288c5bb5d141ea0fb043058a6e1939a078b6. Unchanged from original reviewed target bytes. |
| prior-6 | reviews/structured/20261021T073357Z-mating-projection-septin-ring-audit/review.yaml; Original immutable YAML and derived Markdown; source, assessments, findings, actions, limitations | context_only | Original review is a historical observation, not evidence that current bytes or current validators were checked. |
| record-7 | data/structures/cytoskeleton/medial_cortex_septin_ring.yaml; Entire current maintained YAML; exact input captured by native inspect | supports | Current record read in full. SHA-256 9286b6cd14a1d4ee846f71768e3e2c167d3254af72efc0e9437738dd16caddb6. Original frozen hash 9286b6cd14a1d4ee846f71768e3e2c167d3254af72efc0e9437738dd16caddb6. Unchanged from original reviewed target bytes. |
| prior-7 | reviews/structured/20261021T073422Z-medial-cortex-septin-ring-audit/review.yaml; Original immutable YAML and derived Markdown; source, assessments, findings, actions, limitations | context_only | Original review is a historical observation, not evidence that current bytes or current validators were checked. |
| record-8 | data/structures/cytoskeleton/median_body.yaml; Entire current maintained YAML; exact input captured by native inspect | supports | Current record read in full. SHA-256 0db987ccc4976e3045c1d47b7aa74591aeee8e1c92c1b3b991d4498410ab5e42. Original frozen hash d8acb0b396e2f02d12854bfcef95a7a2bc67b6be648058230971e38d1b7e757f. Changed: reassessed current delta against primary sources. |
| prior-8 | reviews/structured/20261021T073648Z-median-body-audit/review.yaml; Original immutable YAML and derived Markdown; source, assessments, findings, actions, limitations | context_only | Original review is a historical observation, not evidence that current bytes or current validators were checked. |
| record-9 | data/structures/cytoskeleton/meiotic_septin_complex.yaml; Entire current maintained YAML; exact input captured by native inspect | supports | Current record read in full. SHA-256 4f10be6c6b32a3c71f43f28570d1eefac729c757657a1a28d29ff41f890aebe9. Original frozen hash 4f10be6c6b32a3c71f43f28570d1eefac729c757657a1a28d29ff41f890aebe9. Unchanged from original reviewed target bytes. |
| prior-9 | reviews/structured/20261021T073648Z-meiotic-septin-complex-audit/review.yaml; Original immutable YAML and derived Markdown; source, assessments, findings, actions, limitations | context_only | Original review is a historical observation, not evidence that current bytes or current validators were checked. |
| staleness | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/staleness.json; All ten target hashes against exact fetched main commit | supports | Three changed target inputs: iMTOC node type/history, fusion-focus two edges/history, median-body protein exemplar/history. Seven match exactly. |
| plaque-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0061497%2CGO%3A0061498%2CGO%3A0044732%2CGO%3A0005821%2CGO%3A0005822%2CGO%3A0005816%2CGO%3A0005823%2CGO%3A0005824%2CGO%3A0005880; Nine native GO definitions and direct hierarchy links; GO:0044732 mitotic cell cycle scope | supports | Exact inner/intermediate generic and mitotic subtype identities and parent/parthood agree. Mitotic-cell-cycle subtype does not establish restriction to M phase. |
| plaque2017 | https://pmc-oa-opendata.s3.amazonaws.com/PMC5687031.1/PMC5687031.1.xml; Viswanath2017 DOI10.1091/mbc.E17-06-0397; Fig1A, Results and Methods Stage1 construction | supports | S. cerevisiae plaque geometry and nuclear gamma-TuSC anchoring are distinguished from modeled CP/IL2 boundaries, not universal species-independent assembly counts. |
| plaque-CPX-1420 | https://www.ebi.ac.uk/intact/complex-ws/complex/CPX-1420; Complete named native entry; identity, scope and native type | supports | Accession-specific authority check. CPX-1420 IL2 name and central-plaque GO cross-reference discrepancy is preserved; domain/family and species/strain distinctions are not collapsed. |
| plaque-CPX-1198 | https://www.ebi.ac.uk/intact/complex-ws/complex/CPX-1198; Complete named native entry; identity, scope and native type | supports | Native identity/type read; a protein family, domain or taxon entry is not assembly membership or universal stoichiometry evidence. |
| plaque-IPR021611 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR021611/; Complete named native entry; identity, scope and native type | supports | Native identity/type read; a protein family, domain or taxon entry is not assembly membership or universal stoichiometry evidence. |
| plaque-IPR021750 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR021750/; Complete named native entry; identity, scope and native type | supports | Native identity/type read; a protein family, domain or taxon entry is not assembly membership or universal stoichiometry evidence. |
| plaque-IPR002454 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002454/; Complete named native entry; identity, scope and native type | supports | Native identity/type read; a protein family, domain or taxon entry is not assembly membership or universal stoichiometry evidence. |
| plaque-IPR007259 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007259/; Complete named native entry; identity, scope and native type | supports | Native identity/type read; a protein family, domain or taxon entry is not assembly membership or universal stoichiometry evidence. |
| plaque-IPR040593 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR040593/; Complete named native entry; identity, scope and native type | supports | Native identity/type read; a protein family, domain or taxon entry is not assembly membership or universal stoichiometry evidence. |
| plaque-taxon4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete named native entry; identity, scope and native type | supports | Native identity/type read; a protein family, domain or taxon entry is not assembly membership or universal stoichiometry evidence. |
| plaque-taxon559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Complete named native entry; identity, scope and native type | supports | Native identity/type read; a protein family, domain or taxon entry is not assembly membership or universal stoichiometry evidence. |
| plaque2004 | https://www.researchgate.net/publication/8241691_THE_BUDDING_YEAST_SPINDLE_POLE_BODY_Structure_Duplication_and_Function; Jaspersen/Winey2004 author-manuscript browser extraction, pp5-6 | supports | Secondary literature review context: yeast SPBs persist through the life cycle and change size from G1 to mitosis. This is not independently repeated primary experimentation. Browser extraction, not native publisher PDF. |
| septin-family | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016491/; IPR016491 complete response metadata/type/description | supports | Native Septin family denotes generic septin proteins; does not settle localized paralog membership or accessories. |
| septin-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000144,GO:0005937,GO:0005940,GO:0031105,GO:0032151,GO:0032152,GO:0032162,GO:0032168,GO:0032169,GO:0032170,GO:0032172,GO:0032175,GO:0032177,GO:0036391; Fourteen GO identity/definition and hierarchy records | supports | Distinct localized rings, band and meiotic complex retain exact identities; mating barrier is qualified as proposed. |
| douglas | https://pmc.ncbi.nlm.nih.gov/articles/PMC1214204/?pdf=render; Douglas2005 secondary review, sections13/14/16 | supports | Secondary literature context for septin developmental locations and proposed mating barrier; no direct barrier measurement is inferred. |
| versele | https://pmc.ncbi.nlm.nih.gov/articles/PMC1761124/?pdf=render; Versele/Thorner2005 secondary review, S2/S3/S4/S11 | supports | Secondary literature context for localized septin structures, meiotic composition and unknowns; not a substitute for source-specific primary proof. |
| giot990 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/29b7/305708/32aaf5d2b359/mbc00110-0052.png; Giot/Konopka1997 primary scanned page 990; visually read | supports | Figure1 two-hybrid interaction and Table2 deletion mapping; co-immunoprecipitation unsuccessful because Afr1 insoluble. No purified direct interaction established. |
| giot992 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/29b7/305708/473cc467f993/mbc00110-0054.png; Giot/Konopka1997 primary scanned page 992; visually read | supports | Figure4 projection morphology; deleting the Cdc12-binding domain retains projection formation at reduced efficiency. Does not establish necessity for every Afr1 function. |
| giot993 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/29b7/305708/8cb325b6c446/mbc00110-0055.png; Giot/Konopka1997 primary scanned page 993; visually read | supports | Figure6 Afr1 immunolocalization and mutant localization; surrounding text compares expected Cdc12 position and infers possible membrane/ring association from focal planes. |
| giot995 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/29b7/305708/0adefab85f30/mbc00110-0057.png; Giot/Konopka1997 primary scanned page 995; visually read | supports | Figure9 and Discussion: Cdc12 interaction concentrates Afr1 at projection base; binding is not essential for all Afr1 functions. These experiments do not demonstrate diffusion exclusion. |
| bao | https://pmc-oa-opendata.s3.amazonaws.com/PMC6008054.1/PMC6008054.1.xml; Results s2-2 through s2-9; Discussion s3-1; Methods s4-2 through s4-5-6; Fig6 | supports | Distinct inactive 9A1-NE docking, active NE nucleation and full-length cold-regrowth assays; no invariant NPC membership or native stoichiometry. |
| liu | https://pmc-oa-opendata.s3.amazonaws.com/PMC6927237.1/PMC6927237.1.xml; Results sec3 through sec8; Discussion sec9; Methods sec12 through sec14 | supports | MBC-recovery reciprocal Alp7/Mto1 recruitment and Alp14-associated elongation; residual stubs, SPB regrowth and partial rescue preserved. |
| lynch | https://pmc-oa-opendata.s3.amazonaws.com/PMC3989768.1/PMC3989768.1.xml; Results/Discussion engineered NE/bonsai localization, gamma-TuRC-specific protein requirement, copy-number and multimerization subsections; brief Experimental Procedures | supports | Engineered Mto1 bonsai/NE localization and activation are distinct; CM1/Mto2 dependency and construct-specific copy counts are not universal native geometry. |
| shen | https://pmc-oa-opendata.s3.amazonaws.com/PMC6589567.1/PMC6589567.1.xml; Results non-SPB formation, Mto1 localization, Rsp1 interaction and overexpression; Discussion paragraphs1-2 and5 | supports | Rsp1 deletion, truncation, overexpression and dynamic colocalization distinguish redistribution from complete loss of nucleation. |
| nie | https://pmc-oa-opendata.s3.amazonaws.com/PMC11698074.1/PMC11698074.1.xml; Results Klp2/Rsp1 localization, Ase1/nucleation, transport, purified-complex interactions and competition; Discussion paragraphs1-5 | supports | Klp2-dependent lattice delivery and Rsp1/Ssa1 effects support site-specific regulation; no universal resident membership or whole-cell depletion equivalence. |
| micro-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031021,GO:0000930,GO:1990819,GO:0097568,GO:0005874,GO:0015629,GO:0043332,GO:0005856; Eight exact native GO records | supports | Current gamma-tubulin complex identity supports STRUCTURE type; target identities and parthood match named structures. |
| dawson | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2168246/; Methods fixation/48h doxycycline repression withdrawal and volume measurements; Results Figs2/3 and6/Table2; Discussion Kinesin-13 regulates microtubule dynamics in the median body | supports | Tagged Kin13/EB1 localize to median body; 48h rigor-mutant condition reduces median-body volume, distinct from earlier mitotic-array observations. |
| kin13 | https://rest.uniprot.org/uniprotkb/Q969B0.json; Q969B0 native reviewed status, label, gene, taxon, fragment flag and source strain; annotated experimental citation | supports | Reviewed kin-13 species5741 exemplar; fragment/Polish sequence source is not equated to Park experimental WB stock. Identity evidence is not localization by itself. |
| hagen | https://pmc-oa-opendata.s3.amazonaws.com/PMC8086724.1/PMC8086724.1.xml; Hagen2020 secondary review, sectionS5 paragraphs1-2 | supports | Secondary review describes enigmatic median-body function and reservoir hypothesis, not settled physiology. |
| scott | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3192862/fullTextXML; Relevant direct formin nucleation Results and bacterial recombinant fragment/heterologous actin methods | supports | Direct recombinant Fus1 fragment/heterologous actin experiments support nucleation; not a native full-focus composition inventory. |
| dudin | https://pmc-oa-opendata.s3.amazonaws.com/PMC4384723.1/PMC4384723.1.xml; Entire main Introduction, Results, Discussion; main captions; Methods strains/media. Especially Results final subsection and Discussion Function of the fusion focus paragraph2 | supports | Fus1/typeV myosin focalization and glucanase enrichment support wall erosion; export of Agn2/Eng2/Exg3 remains unknown. This refutes a demonstrated vesicular-export assertion. |
| park | https://pmc-oa-opendata.s3.amazonaws.com/PMC9256289.1/PMC9256289.1.xml; Materials and Methods Giardia lamblia cultivation; Results Localization of GlKin-13 in Giardia trophozoite cytoskeletal structures paragraphs1-2; Fig1; Discussion study limited to interphase | supports | WB/ATCC30957 Kin13 immunolocalization includes median body, axonemes, basal bodies and flagellar tips; no identity of experimental stock with Polish sequence source is asserted. |
| imtocs-agent-family-IPR024312 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR024312/; Native accession-specific identity/type/gene/taxon fields | supports | Source scope is the named accession. Family versus domain, species versus reference stock and identity versus experimental membership remain distinct. |
| imtocs-agent-family-IPR045110 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR045110/; Native accession-specific identity/type/gene/taxon fields | supports | Source scope is the named accession. Family versus domain, species versus reference stock and identity versus experimental membership remain distinct. |
| imtocs-agent-family-IPR051964 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR051964/; Native accession-specific identity/type/gene/taxon fields | supports | Source scope is the named accession. Family versus domain, species versus reference stock and identity versus experimental membership remain distinct. |
| imtocs-agent-taxon-species | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4896; Native accession-specific identity/type/gene/taxon fields | supports | Source scope is the named accession. Family versus domain, species versus reference stock and identity versus experimental membership remain distinct. |
| imtocs-agent-taxon-stock | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/284812; Native accession-specific identity/type/gene/taxon fields | supports | Source scope is the named accession. Family versus domain, species versus reference stock and identity versus experimental membership remain distinct. |
| fusion-focus-agent-act1 | https://rest.uniprot.org/uniprotkb/P10989.json; Native accession-specific identity/type/gene/taxon fields | supports | Source scope is the named accession. Family versus domain, species versus reference stock and identity versus experimental membership remain distinct. |
| fusion-focus-agent-fus1 | https://rest.uniprot.org/uniprotkb/Q10719.json; Native accession-specific identity/type/gene/taxon fields | supports | Source scope is the named accession. Family versus domain, species versus reference stock and identity versus experimental membership remain distinct. |
| fusion-focus-agent-myo51 | https://rest.uniprot.org/uniprotkb/O74805.json; Native accession-specific identity/type/gene/taxon fields | supports | Source scope is the named accession. Family versus domain, species versus reference stock and identity versus experimental membership remain distinct. |
| fusion-focus-agent-myo52 | https://rest.uniprot.org/uniprotkb/O94477.json; Native accession-specific identity/type/gene/taxon fields | supports | Source scope is the named accession. Family versus domain, species versus reference stock and identity versus experimental membership remain distinct. |
| fusion-focus-agent-species | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4896; Native accession-specific identity/type/gene/taxon fields | supports | Source scope is the named accession. Family versus domain, species versus reference stock and identity versus experimental membership remain distinct. |
| fusion-focus-agent-strain | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/284812; Native accession-specific identity/type/gene/taxon fields | supports | Source scope is the named accession. Family versus domain, species versus reference stock and identity versus experimental membership remain distinct. |
| median-body-agent-species | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5741; Native accession-specific identity/type/gene/taxon fields | supports | Source scope is the named accession. Family versus domain, species versus reference stock and identity versus experimental membership remain distinct. |
| imtoc-uniprot | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=accession%3AO94488%20OR%20accession%3AQ9USP7%20OR%20accession%3AQ9Y705%20OR%20accession%3AQ9URY2%20OR%20accession%3AO94534%20OR%20accession%3AO13601%20OR%20accession%3AP14068%20OR%20accession%3AQ09847; Eight named accessions; reviewed status, gene, label and taxon284812 | supports | Eight reference-sequence identities verified; reference stock does not denote every experimental strain. |
| median-topology | https://www.ebi.ac.uk/ols4/api/ontologies/go/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FGO_0097568/graph; GO_0097568 graph part_of GO_0005856 and has_part GO_0005874 | supports | Exact directed median-body cytoskeleton parthood and microtubule has_part links are present; no direction reversal. |
| bao-figure6 | data/images/cytoskeleton/interphase_microtubule_organizing_center/pmc6008054_fig6.jpg; Tracked Figure6 pixels, visually inspected by independent reviewer | supports | A deletion diagram; B inactive9A1-NE reporter; C full-length wild-type Mto1 cold-regrowth; D/E active Mto1[NE] nucleation; F crosslink-MS. These assay contexts are not interchangeable. |
| adapter-catalogue | https://imodulondb.org/api/datasets; Complete native public dataset catalogue; organism and dataset keys | supports | 20 organisms and 28 datasets; no Saccharomyces cerevisiae, Schizosaccharomyces pombe or Giardia dataset. No downstream covered-organism query applies; this is not negative evidence about structure biology. |
| adapter-execution | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Actual installed runner invocation and OS exception | supports | Exit1: OS denied reading pyvenv.cfg. Runner unavailable; direct native catalogue fallback succeeded. No successful CLI execution is claimed. |
| check-qc-final | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/qc-final.log; Actual command stdout/stderr and receipt | supports | Full native QC after complete historical-object hydration returned 0. |
| check-label-correspondence | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/label-correspondence.log; Actual command stdout/stderr and receipt | supports | Ontology label correspondence returned 0. |
| check-trait-links | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/trait-links.log; Actual command stdout/stderr and receipt | supports | TraitMech cross-references returned 0. |
| check-vendored | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/vendored.log; Actual command stdout/stderr and receipt | supports | Pinned governed-file sync returned 0. |
| curies-pending | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/curies-pending-receipt.json; Actual process start and observed running state | supports | Supplemental full-corpus resolver command launched 2026-11-03T00:45:51+00:00; final result still pending at review finish. No exit code or passing verdict is claimed. |
| ci-liveness | https://github.com/CultureBotAI/CellStructureMech/actions/runs/41554972151; Completed exact merged-main-head identifier workflow and downloaded native TSV | supports | CI report on dab52765 has6173 OK and254 SKIPPED identifiers, with no missing/obsolete or unreachable rows. This is CI evidence; the independent cold-cache local scan is separately reported and may still be pending. |
| focused | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/focused-checks.json; 20 actual documented schema/strict commands | supports | Ten schema and ten closed-schema validations; actual per-command exits retained. |

## Limits And Additional Notes

- All original saved reviews remain historical observations against their frozen bytes. Their old validation receipts are not current CI or QC evidence.
- Current primary papers and relevant result/method/caption sections were inspected by independent agents; raw microscopy, movies and every supplementary protocol were not independently reconstructed.
- Bao Figure6 was visually inspected; other microtubule/fusion microscopy was checked through text/captions, not new image analysis.
- Zimmerman2004 and Piva2004 full-text details were not newly independently recovered. Hardin2017 primary PDF was not reread in this pass; the current Hagen secondary review preserves the reservoir hypothesis as unresolved.
- Jaspersen/Winey2004 was read through an author-manuscript browser extraction, not an authenticated publisher PDF. Douglas, Versele and Hagen are secondary context and do not establish uninspected primary mechanisms.
- Four Giot primary page scans990/992/993/995 were visually read; this pass does not claim rereading all original pages988-996.
- The installed structured-source adapter could not run because of OS access restrictions. Native catalogue fallback supports coverage-based non-applicability; physical subject matter alone is not that criterion.
- Review completion does not promote any scientific record status or authorize curation. Seven scientific findings stay open for separate record work.
- The optional full-corpus identifier scan was still running when this immutable observation finished; it supplies no completed verdict here. The separate PR publication receipt will report its actual final exit and unresolved coverage before merge.
- Label correspondence skipped923 pairs without an adapter. Two early QC attempts stopped on incomplete local Git provenance objects; missing blobs and37 source commits were fetched before successful current QC. No retained bundle was changed to bypass provenance checks.
- The canary is PR2344 only. No other batch PR or Intel-session branch is modified.
- One explicit issue-bearing batch follows the repository issue-only gate. Clean current iMTOC, median-body and generic plaque assessments are included as members of this same requested cohort; no issues are fabricated to force standalone clean bundles.
- Original ten YAML/Markdown pairs are preserved byte-for-byte. Current main was merged normally; no rebase or force push.
- Review-artifact remediation issues2504-2507 concern the missed historical node type, omitted phase findings, stale currentness, and adapter rationale. The current assessments and actual check results above supply their corrections. Scientific issues2497-2503 remain separate.
- Independent draft re-review additionally corrected evidence links, frozen Figure6 input, dangling scratch finding ID, page-specific Giot summaries and secondary-literature typing, tracked by issues2508-2512. Those are review-artifact corrections, not scientific curation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T010143Z-pr2344-current-record-followup
kind: batch
repository: CultureBotAI/CellStructureMech
title: 'PR 2344: current review of ten cytoskeletal records and adversarial follow-up'
started_at: '2026-11-03T00:42:43Z'
finished_at: '2026-11-03T01:01:43Z'
reviewer:
  identity: Codex root synthesis with three independent read-only adversarial reviewers
  kind: agent
  independence: self_review
  independence_basis: Root authored this follow-up; independent agents pr2344_plaque_adversary,
    pr2344_microtubule_adversary and pr2344_septin_adversary inspected the original
    ten bundles, current records and actual sources without authoring or changing
    repository files. Their reports supplied findings; they separately re-review this
    new artifact. This is not human scientific sign-off.
skill: .claude/skills/review-yaml-record/SKILL.md; explicit batch route in docs/record-review-profile.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'Current-input reassessment of all ten records in PR 2344, including three
  changed since their frozen reviews. Seven scientific curation findings remain: one
  major unsupported vesicular hydrolase export mechanism, two minor mitotic-cell-cycle
  wording ambiguities, and four minor septin findings retained with exact lineage.
  Four records have supported qualified current assessments; six require curation.
  The original ten immutable bundles remain historical observations. This issue-bearing
  batch supplies the refreshed assessment, acknowledges missed historical defects,
  and corrects the adapter-coverage rationale without changing scientific records.'
source:
  git_revision: dab5276568439756fa032e736df085fc75e0e271
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: e6b9e4b16a58c54402bed7bbee2c8b94a91d37562e8b0ee8b94ff0c829184a70
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
    role: context
  - path: AGENTS.md
    sha256: ef74a980161b55cd24f1851e38d1c0b2e004fcf8837f1bc70da1874e4e8380f0
    role: context
  - path: data/images/cytoskeleton/interphase_microtubule_organizing_center/pmc6008054_fig6.jpg
    sha256: 198bb4cc3881692720e29c525187f21ada7a25145c0f29d3f6eb82ae15070e7f
    role: context
  - path: data/structures/cytoskeleton/inner_plaque_of_mitotic_spindle_pole_body.yaml
    sha256: c7d1f6c1fa0f5928a0d3bc67d245eb0d3e655798fc62e719990248707765aff8
    role: target
  - path: data/structures/cytoskeleton/inner_plaque_of_spindle_pole_body.yaml
    sha256: 663b2ccb7bf2a427807d0156bb33feb5c96ce978649f091ed5a9a2b4723a0dba
    role: target
  - path: data/structures/cytoskeleton/intermediate_layer_of_mitotic_spindle_pole_body.yaml
    sha256: 6babc40661cf4080adb6b1c5e18c42a78c7b1cffddae612a3288fee4926c98e5
    role: target
  - path: data/structures/cytoskeleton/intermediate_layer_of_spindle_pole_body.yaml
    sha256: 3c889767d96b20dae86ccb3327892d5d33a5892591133cd4dcea4ad17a4b07c0
    role: target
  - path: data/structures/cytoskeleton/interphase_microtubule_organizing_center.yaml
    sha256: 5ef265cc6fcc3c2c281479cd4aeacaa5d770d1f3a4a682a37a2d897e1562ba75
    role: target
  - path: data/structures/cytoskeleton/mating_projection_actin_fusion_focus.yaml
    sha256: 7cb7ba894d0912377f74951bc82404b93d14333ff28363d0e2082e7f65f1f6bf
    role: target
  - path: data/structures/cytoskeleton/mating_projection_septin_ring.yaml
    sha256: 1829e9907009f5d72966b7b14936288c5bb5d141ea0fb043058a6e1939a078b6
    role: target
  - path: data/structures/cytoskeleton/medial_cortex_septin_ring.yaml
    sha256: 9286b6cd14a1d4ee846f71768e3e2c167d3254af72efc0e9437738dd16caddb6
    role: target
  - path: data/structures/cytoskeleton/median_body.yaml
    sha256: 0db987ccc4976e3045c1d47b7aa74591aeee8e1c92c1b3b991d4498410ab5e42
    role: target
  - path: data/structures/cytoskeleton/meiotic_septin_complex.yaml
    sha256: 4f10be6c6b32a3c71f43f28570d1eefac729c757657a1a28d29ff41f890aebe9
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
  - path: reviews/structured/20261021T073051Z-inner-plaque-of-mitotic-spindle-pole-body-audit/review.yaml
    sha256: dd10a30e00ab515c4be273f923ad679da175aec59a6fb6242912414bb971cea5
    role: context
  - path: reviews/structured/20261021T073051Z-inner-plaque-of-spindle-pole-body-audit/review.yaml
    sha256: 0d8cc558580e9ec8e14b4e42c03ddeedf750b3c7d18ed5554535b8e70c43afdf
    role: context
  - path: reviews/structured/20261021T073051Z-intermediate-layer-of-mitotic-spindle-pole-body-audit/review.yaml
    sha256: 27137456a538cc6a2a59f364333bc9617261f1c0e4a511a22129500dc67fe47b
    role: context
  - path: reviews/structured/20261021T073051Z-intermediate-layer-of-spindle-pole-body-audit/review.yaml
    sha256: ea88afd275592bf84b0d0693d9c76bd0cd517230737b42ea8e0f8f66dc2cd23c
    role: context
  - path: reviews/structured/20261021T073259Z-interphase-microtubule-organizing-center-audit/review.yaml
    sha256: 93651d00b8e9097e4c432ffc28c63d6818666fe72e80a84769fe3977c475a209
    role: context
  - path: reviews/structured/20261021T073259Z-mating-projection-actin-fusion-focus-audit/review.yaml
    sha256: 19f053d847f934381b1645431020f9e165655f08e96df820354c903758b6f88e
    role: context
  - path: reviews/structured/20261021T073357Z-mating-projection-septin-ring-audit/review.yaml
    sha256: 2663b0e31195c3964e82686b79e54a3b5cc0bd384862693cfa8b0e9331354617
    role: context
  - path: reviews/structured/20261021T073422Z-medial-cortex-septin-ring-audit/review.yaml
    sha256: 382cfab75ca573f5fd135477cce4a2dce516808fc7759610704cc1ec62bdbb78
    role: context
  - path: reviews/structured/20261021T073648Z-median-body-audit/review.yaml
    sha256: 7aa15ce259a11e1e0bb872bf39b008d6beb109d142af08323d1a592045dbd286
    role: context
  - path: reviews/structured/20261021T073648Z-meiotic-septin-complex-audit/review.yaml
    sha256: 0a38a51ddc1deb703d1d764509c46522d96ea6c84da8371226e94709412b1cd2
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
targets:
- target_id: GO:0061497
  path: data/structures/cytoskeleton/inner_plaque_of_mitotic_spindle_pole_body.yaml
  label: inner plaque of mitotic spindle pole body
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/inner_plaque_of_mitotic_spindle_pole_body.yaml
    role: maintained scientific record
- target_id: GO:0005822
  path: data/structures/cytoskeleton/inner_plaque_of_spindle_pole_body.yaml
  label: inner plaque of spindle pole body
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/inner_plaque_of_spindle_pole_body.yaml
    role: maintained scientific record
- target_id: GO:0061498
  path: data/structures/cytoskeleton/intermediate_layer_of_mitotic_spindle_pole_body.yaml
  label: intermediate layer of mitotic spindle pole body
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/intermediate_layer_of_mitotic_spindle_pole_body.yaml
    role: maintained scientific record
- target_id: GO:0005821
  path: data/structures/cytoskeleton/intermediate_layer_of_spindle_pole_body.yaml
  label: intermediate layer of spindle pole body
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/intermediate_layer_of_spindle_pole_body.yaml
    role: maintained scientific record
- target_id: GO:0031021
  path: data/structures/cytoskeleton/interphase_microtubule_organizing_center.yaml
  label: interphase microtubule organizing center
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/interphase_microtubule_organizing_center.yaml
    role: maintained scientific record
- target_id: GO:1990819
  path: data/structures/cytoskeleton/mating_projection_actin_fusion_focus.yaml
  label: mating projection actin fusion focus
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/mating_projection_actin_fusion_focus.yaml
    role: maintained scientific record
- target_id: GO:0032175
  path: data/structures/cytoskeleton/mating_projection_septin_ring.yaml
  label: mating projection septin ring
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/mating_projection_septin_ring.yaml
    role: maintained scientific record
- target_id: GO:0036391
  path: data/structures/cytoskeleton/medial_cortex_septin_ring.yaml
  label: medial cortex septin ring
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/medial_cortex_septin_ring.yaml
    role: maintained scientific record
- target_id: GO:0097568
  path: data/structures/cytoskeleton/median_body.yaml
  label: median body
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/median_body.yaml
    role: maintained scientific record
- target_id: GO:0032152
  path: data/structures/cytoskeleton/meiotic_septin_complex.yaml
  label: meiotic septin complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/meiotic_septin_complex.yaml
    role: maintained scientific record
scope:
  description: Entire ten-record PR cohort, not a corpus sample. The original frozen
    records and review claims are compared with current main 4efb30b376d650109f5df154cf95fc382e714ca2;
    every changed scientific assertion is reassessed. Full records, original assessments
    and current source scope are inspected. No curation or native status promotion.
  selection: Exactly the ten target paths in PR 2344 original head 5b50c32ef35f6ef410dd16a3819d71b9f08b970c;
    deterministic path order. Current main contains 1022 records; only these ten are
    in scope.
  coverage: full
  population_size: 10
  reviewed_target_ids:
  - GO:0061497
  - GO:0005822
  - GO:0061498
  - GO:0005821
  - GO:0031021
  - GO:1990819
  - GO:0032175
  - GO:0036391
  - GO:0097568
  - GO:0032152
checks:
- check_id: adapter-runner
  name: Structured adapter runner
  status: failed
  required: false
  target_ids:
  - GO:0061497
  - GO:0005822
  - GO:0061498
  - GO:0005821
  - GO:0031021
  - GO:1990819
  - GO:0032175
  - GO:0036391
  - GO:0097568
  - GO:0032152
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb datasets
  exit_code: 1
  summary: Actual installed runner unavailable because OS denied pyvenv.cfg; direct
    source-native catalogue fallback inspected.
  evidence_ids:
  - adapter-execution
  - adapter-catalogue
- check_id: adapter-applicability
  name: Organism-specific expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0061497
  - GO:0005822
  - GO:0061498
  - GO:0005821
  - GO:0031021
  - GO:1990819
  - GO:0032175
  - GO:0036391
  - GO:0097568
  - GO:0032152
  summary: The inspected native catalogue has no matching yeast or Giardia dataset.
    Downstream organism/component searches were not run; no phenotype or mechanism
    absence is inferred.
  evidence_ids:
  - adapter-catalogue
- check_id: staleness
  name: Frozen input comparison and reassessment
  status: passed
  required: true
  target_ids:
  - GO:0061497
  - GO:0005822
  - GO:0061498
  - GO:0005821
  - GO:0031021
  - GO:1990819
  - GO:0032175
  - GO:0036391
  - GO:0097568
  - GO:0032152
  summary: Ten exact hashes compared with fetched main; three changed targets reassessed
    against source-specific evidence and all ten receive current assessments.
  evidence_ids:
  - staleness
- check_id: qc-final
  name: Full native QC after complete historical-object hydration
  status: passed
  required: true
  target_ids:
  - GO:0061497
  - GO:0005822
  - GO:0061498
  - GO:0005821
  - GO:0031021
  - GO:1990819
  - GO:0032175
  - GO:0036391
  - GO:0097568
  - GO:0032152
  command: just qc
  exit_code: 0
  summary: Full native QC after complete historical-object hydration exit 0. See exact
    logged result and limitations; native zero is not universal source or identifier
    coverage.
  evidence_ids:
  - check-qc-final
- check_id: label-correspondence
  name: Ontology label correspondence
  status: passed
  required: true
  target_ids:
  - GO:0061497
  - GO:0005822
  - GO:0061498
  - GO:0005821
  - GO:0031021
  - GO:1990819
  - GO:0032175
  - GO:0036391
  - GO:0097568
  - GO:0032152
  command: just validate-products
  exit_code: 0
  summary: 'Exit0: 4232 canonical, 50 synonym and 9 exception matches; 923 pairs skipped
    because no adapter. Native success does not mean every identifier was checked.'
  evidence_ids:
  - check-label-correspondence
- check_id: trait-links
  name: TraitMech cross-references
  status: passed
  required: true
  target_ids:
  - GO:0061497
  - GO:0005822
  - GO:0061498
  - GO:0005821
  - GO:0031021
  - GO:1990819
  - GO:0032175
  - GO:0036391
  - GO:0097568
  - GO:0032152
  command: just check-trait-links --check
  exit_code: 0
  summary: TraitMech cross-references exit 0. See exact logged result and limitations;
    native zero is not universal source or identifier coverage.
  evidence_ids:
  - check-trait-links
- check_id: vendored
  name: Pinned governed-file sync
  status: passed
  required: true
  target_ids:
  - GO:0061497
  - GO:0005822
  - GO:0061498
  - GO:0005821
  - GO:0031021
  - GO:1990819
  - GO:0032175
  - GO:0036391
  - GO:0097568
  - GO:0032152
  command: just vendored-check
  exit_code: 0
  summary: Pinned governed-file sync exit 0. See exact logged result and limitations;
    native zero is not universal source or identifier coverage.
  evidence_ids:
  - check-vendored
- check_id: curies-pending
  name: Supplemental full-corpus identifier scan result pending
  status: unavailable
  required: false
  target_ids:
  - GO:0061497
  - GO:0005822
  - GO:0061498
  - GO:0005821
  - GO:0031021
  - GO:1990819
  - GO:0032175
  - GO:0036391
  - GO:0097568
  - GO:0032152
  command: just check-curies-strict
  summary: Started 2026-11-03T00:45:51+00:00; running without a final result at finished_at.
    Target-specific authority responses were separately inspected. Final publication
    waits for the scan and records its result in the PR.
  evidence_ids:
  - curies-pending
- check_id: ci-liveness-main-merge
  name: Identifier CI on merged-main head
  status: passed
  required: false
  target_ids:
  - GO:0061497
  - GO:0005822
  - GO:0061498
  - GO:0005821
  - GO:0031021
  - GO:1990819
  - GO:0032175
  - GO:0036391
  - GO:0097568
  - GO:0032152
  summary: Exact main-merge head dab52765 workflow completed successfully;6173 OK
    and254 SKIPPED in native report. This is not the final amended-head CI or a completed
    local cold-cache result.
  evidence_ids:
  - ci-liveness
- check_id: validate-0
  name: validate inner plaque of mitotic spindle pole body
  status: passed
  required: true
  target_ids:
  - GO:0061497
  command: just validate data/structures/cytoskeleton/inner_plaque_of_mitotic_spindle_pole_body.yaml
  exit_code: 0
  summary: Native focused check exit 0.
  evidence_ids:
  - focused
- check_id: validate-strict-0
  name: validate-strict inner plaque of mitotic spindle pole body
  status: passed
  required: true
  target_ids:
  - GO:0061497
  command: just validate-strict data/structures/cytoskeleton/inner_plaque_of_mitotic_spindle_pole_body.yaml
    --out /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/inner_plaque_of_mitotic_spindle_pole_body-strict.tsv
  exit_code: 0
  summary: Native focused check exit 0.
  evidence_ids:
  - focused
- check_id: validate-1
  name: validate inner plaque of spindle pole body
  status: passed
  required: true
  target_ids:
  - GO:0005822
  command: just validate data/structures/cytoskeleton/inner_plaque_of_spindle_pole_body.yaml
  exit_code: 0
  summary: Native focused check exit 0.
  evidence_ids:
  - focused
- check_id: validate-strict-1
  name: validate-strict inner plaque of spindle pole body
  status: passed
  required: true
  target_ids:
  - GO:0005822
  command: just validate-strict data/structures/cytoskeleton/inner_plaque_of_spindle_pole_body.yaml
    --out /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/inner_plaque_of_spindle_pole_body-strict.tsv
  exit_code: 0
  summary: Native focused check exit 0.
  evidence_ids:
  - focused
- check_id: validate-2
  name: validate intermediate layer of mitotic spindle pole body
  status: passed
  required: true
  target_ids:
  - GO:0061498
  command: just validate data/structures/cytoskeleton/intermediate_layer_of_mitotic_spindle_pole_body.yaml
  exit_code: 0
  summary: Native focused check exit 0.
  evidence_ids:
  - focused
- check_id: validate-strict-2
  name: validate-strict intermediate layer of mitotic spindle pole body
  status: passed
  required: true
  target_ids:
  - GO:0061498
  command: just validate-strict data/structures/cytoskeleton/intermediate_layer_of_mitotic_spindle_pole_body.yaml
    --out /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/intermediate_layer_of_mitotic_spindle_pole_body-strict.tsv
  exit_code: 0
  summary: Native focused check exit 0.
  evidence_ids:
  - focused
- check_id: validate-3
  name: validate intermediate layer of spindle pole body
  status: passed
  required: true
  target_ids:
  - GO:0005821
  command: just validate data/structures/cytoskeleton/intermediate_layer_of_spindle_pole_body.yaml
  exit_code: 0
  summary: Native focused check exit 0.
  evidence_ids:
  - focused
- check_id: validate-strict-3
  name: validate-strict intermediate layer of spindle pole body
  status: passed
  required: true
  target_ids:
  - GO:0005821
  command: just validate-strict data/structures/cytoskeleton/intermediate_layer_of_spindle_pole_body.yaml
    --out /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/intermediate_layer_of_spindle_pole_body-strict.tsv
  exit_code: 0
  summary: Native focused check exit 0.
  evidence_ids:
  - focused
- check_id: validate-4
  name: validate interphase microtubule organizing center
  status: passed
  required: true
  target_ids:
  - GO:0031021
  command: just validate data/structures/cytoskeleton/interphase_microtubule_organizing_center.yaml
  exit_code: 0
  summary: Native focused check exit 0.
  evidence_ids:
  - focused
- check_id: validate-strict-4
  name: validate-strict interphase microtubule organizing center
  status: passed
  required: true
  target_ids:
  - GO:0031021
  command: just validate-strict data/structures/cytoskeleton/interphase_microtubule_organizing_center.yaml
    --out /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/interphase_microtubule_organizing_center-strict.tsv
  exit_code: 0
  summary: Native focused check exit 0.
  evidence_ids:
  - focused
- check_id: validate-5
  name: validate mating projection actin fusion focus
  status: passed
  required: true
  target_ids:
  - GO:1990819
  command: just validate data/structures/cytoskeleton/mating_projection_actin_fusion_focus.yaml
  exit_code: 0
  summary: Native focused check exit 0.
  evidence_ids:
  - focused
- check_id: validate-strict-5
  name: validate-strict mating projection actin fusion focus
  status: passed
  required: true
  target_ids:
  - GO:1990819
  command: just validate-strict data/structures/cytoskeleton/mating_projection_actin_fusion_focus.yaml
    --out /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/mating_projection_actin_fusion_focus-strict.tsv
  exit_code: 0
  summary: Native focused check exit 0.
  evidence_ids:
  - focused
- check_id: validate-6
  name: validate mating projection septin ring
  status: passed
  required: true
  target_ids:
  - GO:0032175
  command: just validate data/structures/cytoskeleton/mating_projection_septin_ring.yaml
  exit_code: 0
  summary: Native focused check exit 0.
  evidence_ids:
  - focused
- check_id: validate-strict-6
  name: validate-strict mating projection septin ring
  status: passed
  required: true
  target_ids:
  - GO:0032175
  command: just validate-strict data/structures/cytoskeleton/mating_projection_septin_ring.yaml
    --out /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/mating_projection_septin_ring-strict.tsv
  exit_code: 0
  summary: Native focused check exit 0.
  evidence_ids:
  - focused
- check_id: validate-7
  name: validate medial cortex septin ring
  status: passed
  required: true
  target_ids:
  - GO:0036391
  command: just validate data/structures/cytoskeleton/medial_cortex_septin_ring.yaml
  exit_code: 0
  summary: Native focused check exit 0.
  evidence_ids:
  - focused
- check_id: validate-strict-7
  name: validate-strict medial cortex septin ring
  status: passed
  required: true
  target_ids:
  - GO:0036391
  command: just validate-strict data/structures/cytoskeleton/medial_cortex_septin_ring.yaml
    --out /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/medial_cortex_septin_ring-strict.tsv
  exit_code: 0
  summary: Native focused check exit 0.
  evidence_ids:
  - focused
- check_id: validate-8
  name: validate median body
  status: passed
  required: true
  target_ids:
  - GO:0097568
  command: just validate data/structures/cytoskeleton/median_body.yaml
  exit_code: 0
  summary: Native focused check exit 0.
  evidence_ids:
  - focused
- check_id: validate-strict-8
  name: validate-strict median body
  status: passed
  required: true
  target_ids:
  - GO:0097568
  command: just validate-strict data/structures/cytoskeleton/median_body.yaml --out
    /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/median_body-strict.tsv
  exit_code: 0
  summary: Native focused check exit 0.
  evidence_ids:
  - focused
- check_id: validate-9
  name: validate meiotic septin complex
  status: passed
  required: true
  target_ids:
  - GO:0032152
  command: just validate data/structures/cytoskeleton/meiotic_septin_complex.yaml
  exit_code: 0
  summary: Native focused check exit 0.
  evidence_ids:
  - focused
- check_id: validate-strict-9
  name: validate-strict meiotic septin complex
  status: passed
  required: true
  target_ids:
  - GO:0032152
  command: just validate-strict data/structures/cytoskeleton/meiotic_septin_complex.yaml
    --out /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/meiotic_septin_complex-strict.tsv
  exit_code: 0
  summary: Native focused check exit 0.
  evidence_ids:
  - focused
evidence:
- evidence_id: record-0
  kind: record_content
  reference: data/structures/cytoskeleton/inner_plaque_of_mitotic_spindle_pole_body.yaml
  locator: Entire current maintained YAML; exact input captured by native inspect
  accessed_at: '2026-11-03T01:01:43Z'
  support: supports
  summary: Current record read in full. SHA-256 c7d1f6c1fa0f5928a0d3bc67d245eb0d3e655798fc62e719990248707765aff8.
    Original frozen hash c7d1f6c1fa0f5928a0d3bc67d245eb0d3e655798fc62e719990248707765aff8.
    Unchanged from original reviewed target bytes.
  snapshot_sha256: c7d1f6c1fa0f5928a0d3bc67d245eb0d3e655798fc62e719990248707765aff8
- evidence_id: prior-0
  kind: prior_review
  reference: reviews/structured/20261021T073051Z-inner-plaque-of-mitotic-spindle-pole-body-audit/review.yaml
  locator: Original immutable YAML and derived Markdown; source, assessments, findings,
    actions, limitations
  accessed_at: '2026-11-03T01:01:43Z'
  support: context_only
  summary: Original review is a historical observation, not evidence that current
    bytes or current validators were checked.
  snapshot_sha256: dd10a30e00ab515c4be273f923ad679da175aec59a6fb6242912414bb971cea5
- evidence_id: record-1
  kind: record_content
  reference: data/structures/cytoskeleton/inner_plaque_of_spindle_pole_body.yaml
  locator: Entire current maintained YAML; exact input captured by native inspect
  accessed_at: '2026-11-03T01:01:43Z'
  support: supports
  summary: Current record read in full. SHA-256 663b2ccb7bf2a427807d0156bb33feb5c96ce978649f091ed5a9a2b4723a0dba.
    Original frozen hash 663b2ccb7bf2a427807d0156bb33feb5c96ce978649f091ed5a9a2b4723a0dba.
    Unchanged from original reviewed target bytes.
  snapshot_sha256: 663b2ccb7bf2a427807d0156bb33feb5c96ce978649f091ed5a9a2b4723a0dba
- evidence_id: prior-1
  kind: prior_review
  reference: reviews/structured/20261021T073051Z-inner-plaque-of-spindle-pole-body-audit/review.yaml
  locator: Original immutable YAML and derived Markdown; source, assessments, findings,
    actions, limitations
  accessed_at: '2026-11-03T01:01:43Z'
  support: context_only
  summary: Original review is a historical observation, not evidence that current
    bytes or current validators were checked.
  snapshot_sha256: 0d8cc558580e9ec8e14b4e42c03ddeedf750b3c7d18ed5554535b8e70c43afdf
- evidence_id: record-2
  kind: record_content
  reference: data/structures/cytoskeleton/intermediate_layer_of_mitotic_spindle_pole_body.yaml
  locator: Entire current maintained YAML; exact input captured by native inspect
  accessed_at: '2026-11-03T01:01:43Z'
  support: supports
  summary: Current record read in full. SHA-256 6babc40661cf4080adb6b1c5e18c42a78c7b1cffddae612a3288fee4926c98e5.
    Original frozen hash 6babc40661cf4080adb6b1c5e18c42a78c7b1cffddae612a3288fee4926c98e5.
    Unchanged from original reviewed target bytes.
  snapshot_sha256: 6babc40661cf4080adb6b1c5e18c42a78c7b1cffddae612a3288fee4926c98e5
- evidence_id: prior-2
  kind: prior_review
  reference: reviews/structured/20261021T073051Z-intermediate-layer-of-mitotic-spindle-pole-body-audit/review.yaml
  locator: Original immutable YAML and derived Markdown; source, assessments, findings,
    actions, limitations
  accessed_at: '2026-11-03T01:01:43Z'
  support: context_only
  summary: Original review is a historical observation, not evidence that current
    bytes or current validators were checked.
  snapshot_sha256: 27137456a538cc6a2a59f364333bc9617261f1c0e4a511a22129500dc67fe47b
- evidence_id: record-3
  kind: record_content
  reference: data/structures/cytoskeleton/intermediate_layer_of_spindle_pole_body.yaml
  locator: Entire current maintained YAML; exact input captured by native inspect
  accessed_at: '2026-11-03T01:01:43Z'
  support: supports
  summary: Current record read in full. SHA-256 3c889767d96b20dae86ccb3327892d5d33a5892591133cd4dcea4ad17a4b07c0.
    Original frozen hash 3c889767d96b20dae86ccb3327892d5d33a5892591133cd4dcea4ad17a4b07c0.
    Unchanged from original reviewed target bytes.
  snapshot_sha256: 3c889767d96b20dae86ccb3327892d5d33a5892591133cd4dcea4ad17a4b07c0
- evidence_id: prior-3
  kind: prior_review
  reference: reviews/structured/20261021T073051Z-intermediate-layer-of-spindle-pole-body-audit/review.yaml
  locator: Original immutable YAML and derived Markdown; source, assessments, findings,
    actions, limitations
  accessed_at: '2026-11-03T01:01:43Z'
  support: context_only
  summary: Original review is a historical observation, not evidence that current
    bytes or current validators were checked.
  snapshot_sha256: ea88afd275592bf84b0d0693d9c76bd0cd517230737b42ea8e0f8f66dc2cd23c
- evidence_id: record-4
  kind: record_content
  reference: data/structures/cytoskeleton/interphase_microtubule_organizing_center.yaml
  locator: Entire current maintained YAML; exact input captured by native inspect
  accessed_at: '2026-11-03T01:01:43Z'
  support: supports
  summary: 'Current record read in full. SHA-256 5ef265cc6fcc3c2c281479cd4aeacaa5d770d1f3a4a682a37a2d897e1562ba75.
    Original frozen hash e16c54c5053f30b3da52fae3a7b2eeb0afb18d2580bff4e95d3b69071160b7ca.
    Changed: reassessed current delta against primary sources.'
  snapshot_sha256: 5ef265cc6fcc3c2c281479cd4aeacaa5d770d1f3a4a682a37a2d897e1562ba75
- evidence_id: prior-4
  kind: prior_review
  reference: reviews/structured/20261021T073259Z-interphase-microtubule-organizing-center-audit/review.yaml
  locator: Original immutable YAML and derived Markdown; source, assessments, findings,
    actions, limitations
  accessed_at: '2026-11-03T01:01:43Z'
  support: context_only
  summary: Original review is a historical observation, not evidence that current
    bytes or current validators were checked.
  snapshot_sha256: 93651d00b8e9097e4c432ffc28c63d6818666fe72e80a84769fe3977c475a209
- evidence_id: record-5
  kind: record_content
  reference: data/structures/cytoskeleton/mating_projection_actin_fusion_focus.yaml
  locator: Entire current maintained YAML; exact input captured by native inspect
  accessed_at: '2026-11-03T01:01:43Z'
  support: supports
  summary: 'Current record read in full. SHA-256 7cb7ba894d0912377f74951bc82404b93d14333ff28363d0e2082e7f65f1f6bf.
    Original frozen hash e0b5696c74beabb751e5334fd04492a057d4b3fceeedf87f7b1c59978e172b1e.
    Changed: reassessed current delta against primary sources.'
  snapshot_sha256: 7cb7ba894d0912377f74951bc82404b93d14333ff28363d0e2082e7f65f1f6bf
- evidence_id: prior-5
  kind: prior_review
  reference: reviews/structured/20261021T073259Z-mating-projection-actin-fusion-focus-audit/review.yaml
  locator: Original immutable YAML and derived Markdown; source, assessments, findings,
    actions, limitations
  accessed_at: '2026-11-03T01:01:43Z'
  support: context_only
  summary: Original review is a historical observation, not evidence that current
    bytes or current validators were checked.
  snapshot_sha256: 19f053d847f934381b1645431020f9e165655f08e96df820354c903758b6f88e
- evidence_id: record-6
  kind: record_content
  reference: data/structures/cytoskeleton/mating_projection_septin_ring.yaml
  locator: Entire current maintained YAML; exact input captured by native inspect
  accessed_at: '2026-11-03T01:01:43Z'
  support: supports
  summary: Current record read in full. SHA-256 1829e9907009f5d72966b7b14936288c5bb5d141ea0fb043058a6e1939a078b6.
    Original frozen hash 1829e9907009f5d72966b7b14936288c5bb5d141ea0fb043058a6e1939a078b6.
    Unchanged from original reviewed target bytes.
  snapshot_sha256: 1829e9907009f5d72966b7b14936288c5bb5d141ea0fb043058a6e1939a078b6
- evidence_id: prior-6
  kind: prior_review
  reference: reviews/structured/20261021T073357Z-mating-projection-septin-ring-audit/review.yaml
  locator: Original immutable YAML and derived Markdown; source, assessments, findings,
    actions, limitations
  accessed_at: '2026-11-03T01:01:43Z'
  support: context_only
  summary: Original review is a historical observation, not evidence that current
    bytes or current validators were checked.
  snapshot_sha256: 2663b0e31195c3964e82686b79e54a3b5cc0bd384862693cfa8b0e9331354617
- evidence_id: record-7
  kind: record_content
  reference: data/structures/cytoskeleton/medial_cortex_septin_ring.yaml
  locator: Entire current maintained YAML; exact input captured by native inspect
  accessed_at: '2026-11-03T01:01:43Z'
  support: supports
  summary: Current record read in full. SHA-256 9286b6cd14a1d4ee846f71768e3e2c167d3254af72efc0e9437738dd16caddb6.
    Original frozen hash 9286b6cd14a1d4ee846f71768e3e2c167d3254af72efc0e9437738dd16caddb6.
    Unchanged from original reviewed target bytes.
  snapshot_sha256: 9286b6cd14a1d4ee846f71768e3e2c167d3254af72efc0e9437738dd16caddb6
- evidence_id: prior-7
  kind: prior_review
  reference: reviews/structured/20261021T073422Z-medial-cortex-septin-ring-audit/review.yaml
  locator: Original immutable YAML and derived Markdown; source, assessments, findings,
    actions, limitations
  accessed_at: '2026-11-03T01:01:43Z'
  support: context_only
  summary: Original review is a historical observation, not evidence that current
    bytes or current validators were checked.
  snapshot_sha256: 382cfab75ca573f5fd135477cce4a2dce516808fc7759610704cc1ec62bdbb78
- evidence_id: record-8
  kind: record_content
  reference: data/structures/cytoskeleton/median_body.yaml
  locator: Entire current maintained YAML; exact input captured by native inspect
  accessed_at: '2026-11-03T01:01:43Z'
  support: supports
  summary: 'Current record read in full. SHA-256 0db987ccc4976e3045c1d47b7aa74591aeee8e1c92c1b3b991d4498410ab5e42.
    Original frozen hash d8acb0b396e2f02d12854bfcef95a7a2bc67b6be648058230971e38d1b7e757f.
    Changed: reassessed current delta against primary sources.'
  snapshot_sha256: 0db987ccc4976e3045c1d47b7aa74591aeee8e1c92c1b3b991d4498410ab5e42
- evidence_id: prior-8
  kind: prior_review
  reference: reviews/structured/20261021T073648Z-median-body-audit/review.yaml
  locator: Original immutable YAML and derived Markdown; source, assessments, findings,
    actions, limitations
  accessed_at: '2026-11-03T01:01:43Z'
  support: context_only
  summary: Original review is a historical observation, not evidence that current
    bytes or current validators were checked.
  snapshot_sha256: 7aa15ce259a11e1e0bb872bf39b008d6beb109d142af08323d1a592045dbd286
- evidence_id: record-9
  kind: record_content
  reference: data/structures/cytoskeleton/meiotic_septin_complex.yaml
  locator: Entire current maintained YAML; exact input captured by native inspect
  accessed_at: '2026-11-03T01:01:43Z'
  support: supports
  summary: Current record read in full. SHA-256 4f10be6c6b32a3c71f43f28570d1eefac729c757657a1a28d29ff41f890aebe9.
    Original frozen hash 4f10be6c6b32a3c71f43f28570d1eefac729c757657a1a28d29ff41f890aebe9.
    Unchanged from original reviewed target bytes.
  snapshot_sha256: 4f10be6c6b32a3c71f43f28570d1eefac729c757657a1a28d29ff41f890aebe9
- evidence_id: prior-9
  kind: prior_review
  reference: reviews/structured/20261021T073648Z-meiotic-septin-complex-audit/review.yaml
  locator: Original immutable YAML and derived Markdown; source, assessments, findings,
    actions, limitations
  accessed_at: '2026-11-03T01:01:43Z'
  support: context_only
  summary: Original review is a historical observation, not evidence that current
    bytes or current validators were checked.
  snapshot_sha256: 0a38a51ddc1deb703d1d764509c46522d96ea6c84da8371226e94709412b1cd2
- evidence_id: staleness
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/staleness.json
  locator: All ten target hashes against exact fetched main commit
  accessed_at: '2026-11-03T01:01:43Z'
  support: supports
  summary: 'Three changed target inputs: iMTOC node type/history, fusion-focus two
    edges/history, median-body protein exemplar/history. Seven match exactly.'
  snapshot_sha256: de698366daae54b2ac65526e05227f567f7d703166d1ea15be9f275c12fda5ce
- evidence_id: plaque-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0061497%2CGO%3A0061498%2CGO%3A0044732%2CGO%3A0005821%2CGO%3A0005822%2CGO%3A0005816%2CGO%3A0005823%2CGO%3A0005824%2CGO%3A0005880
  locator: Nine native GO definitions and direct hierarchy links; GO:0044732 mitotic
    cell cycle scope
  accessed_at: '2026-11-03T00:45:04.723589Z'
  support: supports
  summary: Exact inner/intermediate generic and mitotic subtype identities and parent/parthood
    agree. Mitotic-cell-cycle subtype does not establish restriction to M phase.
  snapshot_sha256: 866610768e560f653df9e4111f29a5c2cba0b5b6a922fc4492ec3e5ebfc93e1f
- evidence_id: plaque2017
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5687031.1/PMC5687031.1.xml
  locator: Viswanath2017 DOI10.1091/mbc.E17-06-0397; Fig1A, Results and Methods Stage1
    construction
  accessed_at: '2026-11-03T00:45:04.723878Z'
  support: supports
  summary: S. cerevisiae plaque geometry and nuclear gamma-TuSC anchoring are distinguished
    from modeled CP/IL2 boundaries, not universal species-independent assembly counts.
  snapshot_sha256: 004836a027b7fad21def4f6e9eebc94ec5f1e07679d123407a062241f6edb580
- evidence_id: plaque-CPX-1420
  kind: authority
  reference: https://www.ebi.ac.uk/intact/complex-ws/complex/CPX-1420
  locator: Complete named native entry; identity, scope and native type
  accessed_at: '2026-11-03T00:45:04.723962Z'
  support: supports
  summary: Accession-specific authority check. CPX-1420 IL2 name and central-plaque
    GO cross-reference discrepancy is preserved; domain/family and species/strain
    distinctions are not collapsed.
  snapshot_sha256: f323ad1b133af230458960bed57f117f466742411055b27524379ba1f070cf29
- evidence_id: plaque-CPX-1198
  kind: authority
  reference: https://www.ebi.ac.uk/intact/complex-ws/complex/CPX-1198
  locator: Complete named native entry; identity, scope and native type
  accessed_at: '2026-11-03T00:45:04.724018Z'
  support: supports
  summary: Native identity/type read; a protein family, domain or taxon entry is not
    assembly membership or universal stoichiometry evidence.
  snapshot_sha256: 6ad8b7dadcc915c04c213a08278cb1695d5f089b126afc38b2817a1aa56ca860
- evidence_id: plaque-IPR021611
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR021611/
  locator: Complete named native entry; identity, scope and native type
  accessed_at: '2026-11-03T00:45:04.724060Z'
  support: supports
  summary: Native identity/type read; a protein family, domain or taxon entry is not
    assembly membership or universal stoichiometry evidence.
  snapshot_sha256: aef911d443ea6bf22900e5ff3818f2d89f7d431d884a0cbb4c89b816e1175f34
- evidence_id: plaque-IPR021750
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR021750/
  locator: Complete named native entry; identity, scope and native type
  accessed_at: '2026-11-03T00:45:04.724098Z'
  support: supports
  summary: Native identity/type read; a protein family, domain or taxon entry is not
    assembly membership or universal stoichiometry evidence.
  snapshot_sha256: f1fe20d4b8df21ce0b199b723bafd32ae02fce926221a25124470b9b93f07def
- evidence_id: plaque-IPR002454
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002454/
  locator: Complete named native entry; identity, scope and native type
  accessed_at: '2026-11-03T00:45:04.724130Z'
  support: supports
  summary: Native identity/type read; a protein family, domain or taxon entry is not
    assembly membership or universal stoichiometry evidence.
  snapshot_sha256: 0cc07ff810e7acb2b8d24c24597c1bcabf177adb7e06ae6ddfabbb352fe0c668
- evidence_id: plaque-IPR007259
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007259/
  locator: Complete named native entry; identity, scope and native type
  accessed_at: '2026-11-03T00:45:04.724157Z'
  support: supports
  summary: Native identity/type read; a protein family, domain or taxon entry is not
    assembly membership or universal stoichiometry evidence.
  snapshot_sha256: 35abdb19f33d76f750dba5e51b97017071754f6c4def2ee06df37f41b461a389
- evidence_id: plaque-IPR040593
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR040593/
  locator: Complete named native entry; identity, scope and native type
  accessed_at: '2026-11-03T00:45:05.498280Z'
  support: supports
  summary: Native identity/type read; a protein family, domain or taxon entry is not
    assembly membership or universal stoichiometry evidence.
  snapshot_sha256: ca33c3d4e076b45e58a018b0f87b2a26fa2b3292d0da42d0f16a82f76946092f
- evidence_id: plaque-taxon4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete named native entry; identity, scope and native type
  accessed_at: '2026-11-03T00:45:05.671185Z'
  support: supports
  summary: Native identity/type read; a protein family, domain or taxon entry is not
    assembly membership or universal stoichiometry evidence.
  snapshot_sha256: 38f43dd1593a1d47416228ae385464f30aeb8302c3aadb45b3588d03744bc814
- evidence_id: plaque-taxon559292
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Complete named native entry; identity, scope and native type
  accessed_at: '2026-11-03T00:45:05.677686Z'
  support: supports
  summary: Native identity/type read; a protein family, domain or taxon entry is not
    assembly membership or universal stoichiometry evidence.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: plaque2004
  kind: authority
  reference: https://www.researchgate.net/publication/8241691_THE_BUDDING_YEAST_SPINDLE_POLE_BODY_Structure_Duplication_and_Function
  locator: Jaspersen/Winey2004 author-manuscript browser extraction, pp5-6
  accessed_at: '2026-11-03T00:47:43Z'
  support: supports
  summary: 'Secondary literature review context: yeast SPBs persist through the life
    cycle and change size from G1 to mitosis. This is not independently repeated primary
    experimentation. Browser extraction, not native publisher PDF.'
  snapshot_sha256: e027d82955a859cb483e7800eefbf4424e4e27a4f4cc538fdfc7156388bb3f35
- evidence_id: septin-family
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016491/
  locator: IPR016491 complete response metadata/type/description
  accessed_at: '2026-11-03T00:45:07.205913Z'
  support: supports
  summary: Native Septin family denotes generic septin proteins; does not settle localized
    paralog membership or accessories.
  snapshot_sha256: 5797c626d192b641ed5b4b2231e729f9f179bfd6bb18f911689fa08253688c4a
- evidence_id: septin-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000144,GO:0005937,GO:0005940,GO:0031105,GO:0032151,GO:0032152,GO:0032162,GO:0032168,GO:0032169,GO:0032170,GO:0032172,GO:0032175,GO:0032177,GO:0036391
  locator: Fourteen GO identity/definition and hierarchy records
  accessed_at: '2026-11-03T00:45:07.221599Z'
  support: supports
  summary: Distinct localized rings, band and meiotic complex retain exact identities;
    mating barrier is qualified as proposed.
  snapshot_sha256: 195b505509afb86ac5e36fdcd2f642c41229a6518723caa82f769e3a4f62c734
- evidence_id: douglas
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1214204/?pdf=render
  locator: Douglas2005 secondary review, sections13/14/16
  accessed_at: '2026-11-03T00:45:07.048036Z'
  support: supports
  summary: Secondary literature context for septin developmental locations and proposed
    mating barrier; no direct barrier measurement is inferred.
  snapshot_sha256: 1f416e43bc154bdee2274b49bcb018582fbe2663eca2f62668d543e369bc9e1e
- evidence_id: versele
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1761124/?pdf=render
  locator: Versele/Thorner2005 secondary review, S2/S3/S4/S11
  accessed_at: '2026-11-03T00:45:07.002956Z'
  support: supports
  summary: Secondary literature context for localized septin structures, meiotic composition
    and unknowns; not a substitute for source-specific primary proof.
  snapshot_sha256: 376aadf65f0a2dd0bc00cd61927783c234cc7509529808f83f956ccf8891c0dc
- evidence_id: giot990
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/29b7/305708/32aaf5d2b359/mbc00110-0052.png
  locator: Giot/Konopka1997 primary scanned page 990; visually read
  accessed_at: '2026-11-03T00:45:06.830133Z'
  support: supports
  summary: Figure1 two-hybrid interaction and Table2 deletion mapping; co-immunoprecipitation
    unsuccessful because Afr1 insoluble. No purified direct interaction established.
  snapshot_sha256: 4ab3ff07929caed92402b60cedf10732953b69b8a0440e27cc0bf911641d46bb
- evidence_id: giot992
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/29b7/305708/473cc467f993/mbc00110-0054.png
  locator: Giot/Konopka1997 primary scanned page 992; visually read
  accessed_at: '2026-11-03T00:45:06.910771Z'
  support: supports
  summary: Figure4 projection morphology; deleting the Cdc12-binding domain retains
    projection formation at reduced efficiency. Does not establish necessity for every
    Afr1 function.
  snapshot_sha256: f46ba6a90f06c6ce78c6491b14b9d23b4c76b38d2b46eb5f5f826b1f664342e4
- evidence_id: giot993
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/29b7/305708/8cb325b6c446/mbc00110-0055.png
  locator: Giot/Konopka1997 primary scanned page 993; visually read
  accessed_at: '2026-11-03T00:45:06.892934Z'
  support: supports
  summary: Figure6 Afr1 immunolocalization and mutant localization; surrounding text
    compares expected Cdc12 position and infers possible membrane/ring association
    from focal planes.
  snapshot_sha256: 0cc46617e50550c0a9a0eaa67789ba2303cd528d562477e59a2464f69180f6ac
- evidence_id: giot995
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/29b7/305708/0adefab85f30/mbc00110-0057.png
  locator: Giot/Konopka1997 primary scanned page 995; visually read
  accessed_at: '2026-11-03T00:45:06.878122Z'
  support: supports
  summary: 'Figure9 and Discussion: Cdc12 interaction concentrates Afr1 at projection
    base; binding is not essential for all Afr1 functions. These experiments do not
    demonstrate diffusion exclusion.'
  snapshot_sha256: d8de806cb6d2650d5053f1d42a7d44e8fa08fa7bab9202ea05202ac69f8c49d5
- evidence_id: bao
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC6008054.1/PMC6008054.1.xml
  locator: Results s2-2 through s2-9; Discussion s3-1; Methods s4-2 through s4-5-6;
    Fig6
  accessed_at: '2026-11-03T00:45:33.587676Z'
  support: supports
  summary: Distinct inactive 9A1-NE docking, active NE nucleation and full-length
    cold-regrowth assays; no invariant NPC membership or native stoichiometry.
  snapshot_sha256: 98922bf7afa92f51893d04754fc68faff701ed6e202ebbbdc21f6140ffa215ba
- evidence_id: liu
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC6927237.1/PMC6927237.1.xml
  locator: Results sec3 through sec8; Discussion sec9; Methods sec12 through sec14
  accessed_at: '2026-11-03T00:45:33.588737Z'
  support: supports
  summary: MBC-recovery reciprocal Alp7/Mto1 recruitment and Alp14-associated elongation;
    residual stubs, SPB regrowth and partial rescue preserved.
  snapshot_sha256: 7b17884b81acbfccea7e1f7edc63e74e7de43321e6d72ab47150ea2d28be5917
- evidence_id: lynch
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3989768.1/PMC3989768.1.xml
  locator: Results/Discussion engineered NE/bonsai localization, gamma-TuRC-specific
    protein requirement, copy-number and multimerization subsections; brief Experimental
    Procedures
  accessed_at: '2026-11-03T00:45:33.589555Z'
  support: supports
  summary: Engineered Mto1 bonsai/NE localization and activation are distinct; CM1/Mto2
    dependency and construct-specific copy counts are not universal native geometry.
  snapshot_sha256: c79f01751fe2552986d4dc8ff9523ebf86ad6349f546520563c06c3bf32a323b
- evidence_id: shen
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC6589567.1/PMC6589567.1.xml
  locator: Results non-SPB formation, Mto1 localization, Rsp1 interaction and overexpression;
    Discussion paragraphs1-2 and5
  accessed_at: '2026-11-03T00:45:33.589886Z'
  support: supports
  summary: Rsp1 deletion, truncation, overexpression and dynamic colocalization distinguish
    redistribution from complete loss of nucleation.
  snapshot_sha256: ba8abf01a2f32bdfba0bc693b7a229a578f72415fdf7228fc5ab3d9f1dcad489
- evidence_id: nie
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC11698074.1/PMC11698074.1.xml
  locator: Results Klp2/Rsp1 localization, Ase1/nucleation, transport, purified-complex
    interactions and competition; Discussion paragraphs1-5
  accessed_at: '2026-11-03T00:45:33.590230Z'
  support: supports
  summary: Klp2-dependent lattice delivery and Rsp1/Ssa1 effects support site-specific
    regulation; no universal resident membership or whole-cell depletion equivalence.
  snapshot_sha256: fe10addd128129687b7a78e7b85d14a37823bb3185cca39c0b6a4485d649ec16
- evidence_id: micro-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031021,GO:0000930,GO:1990819,GO:0097568,GO:0005874,GO:0015629,GO:0043332,GO:0005856
  locator: Eight exact native GO records
  accessed_at: '2026-11-03T00:45:34.307761Z'
  support: supports
  summary: Current gamma-tubulin complex identity supports STRUCTURE type; target
    identities and parthood match named structures.
  snapshot_sha256: 7cc1a08103361c4d8be275873db4545285fad485a35042adeed4ab63886352af
- evidence_id: dawson
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2168246/
  locator: Methods fixation/48h doxycycline repression withdrawal and volume measurements;
    Results Figs2/3 and6/Table2; Discussion Kinesin-13 regulates microtubule dynamics
    in the median body
  accessed_at: '2026-11-03T00:45:33.590953Z'
  support: supports
  summary: Tagged Kin13/EB1 localize to median body; 48h rigor-mutant condition reduces
    median-body volume, distinct from earlier mitotic-array observations.
  snapshot_sha256: dfe7559d605da38cde3001c203d2d2d1ee1016c91b73dd3b09e1b4f0e9f46202
- evidence_id: kin13
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q969B0.json
  locator: Q969B0 native reviewed status, label, gene, taxon, fragment flag and source
    strain; annotated experimental citation
  accessed_at: '2026-11-03T00:45:34.232481Z'
  support: supports
  summary: Reviewed kin-13 species5741 exemplar; fragment/Polish sequence source is
    not equated to Park experimental WB stock. Identity evidence is not localization
    by itself.
  snapshot_sha256: cd8813c16c223f08f81201cb48439da873b82123a4595ab90f5d84068439363a
- evidence_id: hagen
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC8086724.1/PMC8086724.1.xml
  locator: Hagen2020 secondary review, sectionS5 paragraphs1-2
  accessed_at: '2026-11-03T00:45:33.590798Z'
  support: supports
  summary: Secondary review describes enigmatic median-body function and reservoir
    hypothesis, not settled physiology.
  snapshot_sha256: e94a97234e02daf25a3a3de12b4f6f86f8bcacd85629b39202fd195c4b7c8894
- evidence_id: scott
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3192862/fullTextXML
  locator: Relevant direct formin nucleation Results and bacterial recombinant fragment/heterologous
    actin methods
  accessed_at: '2026-11-03T00:45:34.296544Z'
  support: supports
  summary: Direct recombinant Fus1 fragment/heterologous actin experiments support
    nucleation; not a native full-focus composition inventory.
  snapshot_sha256: 98843adf024e7b2f678e270ef38aec76d874e2a5fe0a3cdf48a63a2869da5f26
- evidence_id: dudin
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4384723.1/PMC4384723.1.xml
  locator: Entire main Introduction, Results, Discussion; main captions; Methods strains/media.
    Especially Results final subsection and Discussion Function of the fusion focus
    paragraph2
  accessed_at: '2026-11-03T00:45:14.236757Z'
  support: supports
  summary: Fus1/typeV myosin focalization and glucanase enrichment support wall erosion;
    export of Agn2/Eng2/Exg3 remains unknown. This refutes a demonstrated vesicular-export
    assertion.
  snapshot_sha256: f633bda509aa2aa9c09133ca13cf16c3f0a12105b484946bd5f80a1abe76ff52
- evidence_id: park
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC9256289.1/PMC9256289.1.xml
  locator: Materials and Methods Giardia lamblia cultivation; Results Localization
    of GlKin-13 in Giardia trophozoite cytoskeletal structures paragraphs1-2; Fig1;
    Discussion study limited to interphase
  accessed_at: '2026-11-03T00:47:05.442196Z'
  support: supports
  summary: WB/ATCC30957 Kin13 immunolocalization includes median body, axonemes, basal
    bodies and flagellar tips; no identity of experimental stock with Polish sequence
    source is asserted.
  snapshot_sha256: ab4af1261e94b06844a2dd8a07de1bab4c4f2d3d9e4a28518972bcc623371054
- evidence_id: imtocs-agent-family-IPR024312
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR024312/
  locator: Native accession-specific identity/type/gene/taxon fields
  accessed_at: '2026-11-03T00:47:51.210932Z'
  support: supports
  summary: Source scope is the named accession. Family versus domain, species versus
    reference stock and identity versus experimental membership remain distinct.
  snapshot_sha256: e605d3b7216ab19f4229b3206ce52b2e41631b14fd70741a8c821d50d642fb4e
- evidence_id: imtocs-agent-family-IPR045110
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR045110/
  locator: Native accession-specific identity/type/gene/taxon fields
  accessed_at: '2026-11-03T00:47:51.211124Z'
  support: supports
  summary: Source scope is the named accession. Family versus domain, species versus
    reference stock and identity versus experimental membership remain distinct.
  snapshot_sha256: e0ba89dab0b5c5383525985f74a81b6a5862a318c457d70882d37afa9b94017e
- evidence_id: imtocs-agent-family-IPR051964
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR051964/
  locator: Native accession-specific identity/type/gene/taxon fields
  accessed_at: '2026-11-03T00:47:51.211186Z'
  support: supports
  summary: Source scope is the named accession. Family versus domain, species versus
    reference stock and identity versus experimental membership remain distinct.
  snapshot_sha256: 780b169a39295dc553a828dd8044e3cfe23343d0474b5769e33b9a506fa068d6
- evidence_id: imtocs-agent-taxon-species
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4896
  locator: Native accession-specific identity/type/gene/taxon fields
  accessed_at: '2026-11-03T00:47:51.211228Z'
  support: supports
  summary: Source scope is the named accession. Family versus domain, species versus
    reference stock and identity versus experimental membership remain distinct.
  snapshot_sha256: 42c5b7d3d99341137803612d6404cd3884e2d06ec8a740b1ad38163c678f6721
- evidence_id: imtocs-agent-taxon-stock
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/284812
  locator: Native accession-specific identity/type/gene/taxon fields
  accessed_at: '2026-11-03T00:47:51.211260Z'
  support: supports
  summary: Source scope is the named accession. Family versus domain, species versus
    reference stock and identity versus experimental membership remain distinct.
  snapshot_sha256: 948c040cabf6c036dff451c7b6eac22605d0ed5d60a74f471e4431e63f82f721
- evidence_id: fusion-focus-agent-act1
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P10989.json
  locator: Native accession-specific identity/type/gene/taxon fields
  accessed_at: '2026-11-03T00:47:51.211286Z'
  support: supports
  summary: Source scope is the named accession. Family versus domain, species versus
    reference stock and identity versus experimental membership remain distinct.
  snapshot_sha256: 1ac2a412f7ed0e84b486b80ce65faceb178201a11785fe0cd70900d034a42a5b
- evidence_id: fusion-focus-agent-fus1
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q10719.json
  locator: Native accession-specific identity/type/gene/taxon fields
  accessed_at: '2026-11-03T00:47:51.211312Z'
  support: supports
  summary: Source scope is the named accession. Family versus domain, species versus
    reference stock and identity versus experimental membership remain distinct.
  snapshot_sha256: 10bcb4aece3b932ceef5486cdcee441eb4a67dcca0bdf1e01da16aa56b3c6799
- evidence_id: fusion-focus-agent-myo51
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/O74805.json
  locator: Native accession-specific identity/type/gene/taxon fields
  accessed_at: '2026-11-03T00:47:51.211336Z'
  support: supports
  summary: Source scope is the named accession. Family versus domain, species versus
    reference stock and identity versus experimental membership remain distinct.
  snapshot_sha256: 5a36b454db41da070ea82a6e50eeed38692dc45741d4406c3a1a0713eb5ede6b
- evidence_id: fusion-focus-agent-myo52
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/O94477.json
  locator: Native accession-specific identity/type/gene/taxon fields
  accessed_at: '2026-11-03T00:47:52.070400Z'
  support: supports
  summary: Source scope is the named accession. Family versus domain, species versus
    reference stock and identity versus experimental membership remain distinct.
  snapshot_sha256: b5b5dab12baf409d538d03d3a1cac93474dd4df9fd88d7adecb0a32f9ead5e27
- evidence_id: fusion-focus-agent-species
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4896
  locator: Native accession-specific identity/type/gene/taxon fields
  accessed_at: '2026-11-03T00:47:52.149236Z'
  support: supports
  summary: Source scope is the named accession. Family versus domain, species versus
    reference stock and identity versus experimental membership remain distinct.
  snapshot_sha256: 42c5b7d3d99341137803612d6404cd3884e2d06ec8a740b1ad38163c678f6721
- evidence_id: fusion-focus-agent-strain
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/284812
  locator: Native accession-specific identity/type/gene/taxon fields
  accessed_at: '2026-11-03T00:47:52.166415Z'
  support: supports
  summary: Source scope is the named accession. Family versus domain, species versus
    reference stock and identity versus experimental membership remain distinct.
  snapshot_sha256: 948c040cabf6c036dff451c7b6eac22605d0ed5d60a74f471e4431e63f82f721
- evidence_id: median-body-agent-species
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5741
  locator: Native accession-specific identity/type/gene/taxon fields
  accessed_at: '2026-11-03T00:47:52.181114Z'
  support: supports
  summary: Source scope is the named accession. Family versus domain, species versus
    reference stock and identity versus experimental membership remain distinct.
  snapshot_sha256: 1dcdc380972a71a0a24c80755d8bbacdcb0b6d9988bb5fb1e05ba43f50580dd3
- evidence_id: imtoc-uniprot
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=accession%3AO94488%20OR%20accession%3AQ9USP7%20OR%20accession%3AQ9Y705%20OR%20accession%3AQ9URY2%20OR%20accession%3AO94534%20OR%20accession%3AO13601%20OR%20accession%3AP14068%20OR%20accession%3AQ09847
  locator: Eight named accessions; reviewed status, gene, label and taxon284812
  accessed_at: '2026-11-03T00:48:23.922758Z'
  support: supports
  summary: Eight reference-sequence identities verified; reference stock does not
    denote every experimental strain.
  snapshot_sha256: cf3148d9acc0524650ba739433ee780ea710d5c8e6a333444a83905196c8f471
- evidence_id: median-topology
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/go/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FGO_0097568/graph
  locator: GO_0097568 graph part_of GO_0005856 and has_part GO_0005874
  accessed_at: '2026-11-03T00:53:26.021446Z'
  support: supports
  summary: Exact directed median-body cytoskeleton parthood and microtubule has_part
    links are present; no direction reversal.
  snapshot_sha256: add88681db421767de0a28dd9e4c8f77d708e7173f029b7c88c4947b2cd1d529
- evidence_id: bao-figure6
  kind: record_content
  reference: data/images/cytoskeleton/interphase_microtubule_organizing_center/pmc6008054_fig6.jpg
  locator: Tracked Figure6 pixels, visually inspected by independent reviewer
  accessed_at: '2026-11-03T01:01:43Z'
  support: supports
  summary: A deletion diagram; B inactive9A1-NE reporter; C full-length wild-type
    Mto1 cold-regrowth; D/E active Mto1[NE] nucleation; F crosslink-MS. These assay
    contexts are not interchangeable.
  snapshot_sha256: 198bb4cc3881692720e29c525187f21ada7a25145c0f29d3f6eb82ae15070e7f
- evidence_id: adapter-catalogue
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Complete native public dataset catalogue; organism and dataset keys
  accessed_at: '2026-11-03T00:48:48.702947Z'
  support: supports
  summary: 20 organisms and 28 datasets; no Saccharomyces cerevisiae, Schizosaccharomyces
    pombe or Giardia dataset. No downstream covered-organism query applies; this is
    not negative evidence about structure biology.
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: adapter-execution
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Actual installed runner invocation and OS exception
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: supports
  summary: 'Exit1: OS denied reading pyvenv.cfg. Runner unavailable; direct native
    catalogue fallback succeeded. No successful CLI execution is claimed.'
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: check-qc-final
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/qc-final.log
  locator: Actual command stdout/stderr and receipt
  accessed_at: '2026-11-03T01:00:26.432334Z'
  support: supports
  summary: Full native QC after complete historical-object hydration returned 0.
  snapshot_sha256: dca0be953a95e2536929c17d09e1bd4d2040a5f9c0f664a2937851adf9dbe833
- evidence_id: check-label-correspondence
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/label-correspondence.log
  locator: Actual command stdout/stderr and receipt
  accessed_at: '2026-11-03T00:46:25.132243Z'
  support: supports
  summary: Ontology label correspondence returned 0.
  snapshot_sha256: d8200b370ec584f49336f01ed9035fbe21f0aa191ad0257a9a421938e9f17ecb
- evidence_id: check-trait-links
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/trait-links.log
  locator: Actual command stdout/stderr and receipt
  accessed_at: '2026-11-03T00:45:54.151930Z'
  support: supports
  summary: TraitMech cross-references returned 0.
  snapshot_sha256: 8b336cdefbbd3daf6da8787990efdbe346c95e2c8361d50b7eb68a18f2d5a44a
- evidence_id: check-vendored
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/vendored.log
  locator: Actual command stdout/stderr and receipt
  accessed_at: '2026-11-03T00:45:54.632700Z'
  support: supports
  summary: Pinned governed-file sync returned 0.
  snapshot_sha256: b1f169d103aaefa930745468bcca171e5867b9cc49e4e74311e458097e3252a6
- evidence_id: curies-pending
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/curies-pending-receipt.json
  locator: Actual process start and observed running state
  accessed_at: '2026-11-03T00:58:46.173925Z'
  support: supports
  summary: Supplemental full-corpus resolver command launched 2026-11-03T00:45:51+00:00;
    final result still pending at review finish. No exit code or passing verdict is
    claimed.
  snapshot_sha256: 9f1fdbe84dd03e689e106bef8d82db5cd1467605782fee8a4cb8b3fcf049ca53
- evidence_id: ci-liveness
  kind: validation
  reference: https://github.com/CultureBotAI/CellStructureMech/actions/runs/41554972151
  locator: Completed exact merged-main-head identifier workflow and downloaded native
    TSV
  accessed_at: '2026-11-03T00:47:40Z'
  support: supports
  summary: CI report on dab52765 has6173 OK and254 SKIPPED identifiers, with no missing/obsolete
    or unreachable rows. This is CI evidence; the independent cold-cache local scan
    is separately reported and may still be pending.
  snapshot_sha256: dd4ae6a8e245c4b060ef6277d25a9f111c8b13d2e7e3b01bb24ef1e114bd64ee
- evidence_id: focused
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/focused-checks.json
  locator: 20 actual documented schema/strict commands
  accessed_at: '2026-11-03T01:01:43Z'
  support: supports
  summary: Ten schema and ten closed-schema validations; actual per-command exits
    retained.
  snapshot_sha256: 9d3fac09947054777bff647c8d4a96d6d14b32dc262860a1c2d4f518594b1234
assessments:
- assessment_id: current-0
  area: scope
  topic: inner plaque of mitotic spindle pole body current assessment
  outcome: concern
  summary: 'Exact identity and is-a/parthood remain supported by native GO. S. cerevisiae
    is an example; S288C candidate-protein identity is not generalized. Inner-plaque
    anchoring and intermediate-layer CP/IL2 model boundaries are preserved; InterPro
    domains/families and generic gamma-TuSC counts do not establish plaque-wide stoichiometry.
    Minor ambiguity remains: mitosis-specific wording can imply M-phase restriction
    although the subtype denotes the mitotic cell cycle; request separate wording
    curation.'
  target_ids:
  - GO:0061497
  evidence_ids:
  - record-0
  - prior-0
  - plaque-go
  - plaque2017
  - plaque2004
  - plaque-CPX-1420
  - plaque-CPX-1198
  - plaque-IPR021611
  - plaque-IPR021750
  - plaque-IPR002454
  - plaque-IPR007259
  - plaque-IPR040593
  - plaque-taxon4932
  - plaque-taxon559292
- assessment_id: current-1
  area: scope
  topic: inner plaque of spindle pole body current assessment
  outcome: supported
  summary: Exact identity and is-a/parthood remain supported by native GO. S. cerevisiae
    is an example; S288C candidate-protein identity is not generalized. Inner-plaque
    anchoring and intermediate-layer CP/IL2 model boundaries are preserved; InterPro
    domains/families and generic gamma-TuSC counts do not establish plaque-wide stoichiometry.
    No new issue observed within these source and access limits; qualified support
    retained.
  target_ids:
  - GO:0005822
  evidence_ids:
  - record-1
  - prior-1
  - plaque-go
  - plaque2017
  - plaque2004
  - plaque-CPX-1420
  - plaque-CPX-1198
  - plaque-IPR021611
  - plaque-IPR021750
  - plaque-IPR002454
  - plaque-IPR007259
  - plaque-IPR040593
  - plaque-taxon4932
  - plaque-taxon559292
- assessment_id: current-2
  area: scope
  topic: intermediate layer of mitotic spindle pole body current assessment
  outcome: concern
  summary: 'Exact identity and is-a/parthood remain supported by native GO. S. cerevisiae
    is an example; S288C candidate-protein identity is not generalized. Inner-plaque
    anchoring and intermediate-layer CP/IL2 model boundaries are preserved; InterPro
    domains/families and generic gamma-TuSC counts do not establish plaque-wide stoichiometry.
    Minor ambiguity remains: mitosis-specific wording can imply M-phase restriction
    although the subtype denotes the mitotic cell cycle; request separate wording
    curation.'
  target_ids:
  - GO:0061498
  evidence_ids:
  - record-2
  - prior-2
  - plaque-go
  - plaque2017
  - plaque2004
  - plaque-CPX-1420
  - plaque-CPX-1198
  - plaque-IPR021611
  - plaque-IPR021750
  - plaque-IPR002454
  - plaque-IPR007259
  - plaque-IPR040593
  - plaque-taxon4932
  - plaque-taxon559292
- assessment_id: current-3
  area: scope
  topic: intermediate layer of spindle pole body current assessment
  outcome: supported
  summary: Exact identity and is-a/parthood remain supported by native GO. S. cerevisiae
    is an example; S288C candidate-protein identity is not generalized. Inner-plaque
    anchoring and intermediate-layer CP/IL2 model boundaries are preserved; InterPro
    domains/families and generic gamma-TuSC counts do not establish plaque-wide stoichiometry.
    No new issue observed within these source and access limits; qualified support
    retained.
  target_ids:
  - GO:0005821
  evidence_ids:
  - record-3
  - prior-3
  - plaque-go
  - plaque2017
  - plaque2004
  - plaque-CPX-1420
  - plaque-CPX-1198
  - plaque-IPR021611
  - plaque-IPR021750
  - plaque-IPR002454
  - plaque-IPR007259
  - plaque-IPR040593
  - plaque-taxon4932
  - plaque-taxon559292
- assessment_id: current-4
  area: graph
  topic: interphase microtubule organizing center current full-record reassessment
  outcome: supported
  summary: Current STRUCTURE node for gamma_tuc agrees with complex identity and component
    type. Historical GO definition remains bounded to S. pombe/example context. Bao
    supports distinct inactive 9A1-NE docking, active Mto1[NE] nucleation and full-length
    cold regrowth; Liu supports reciprocal Alp7/Mto1 and Alp14 localization under
    MBC recovery with residual stubs and partial rescue; Lynch supports engineered
    bonsai CM1/Mto2-dependent activation and bounded copy estimates; Shen and Nie
    support dynamic Rsp1 site/dose effects and distinguish whole-cell deletion from
    Klp2-dependent lattice recruitment. All eight current UniProt reference identities
    are reviewed entries in taxon284812. IPR045110 is XMAP215 family; IPR024312 is
    a domain; IPR051964 is broad and its description LLM-generated. Tracked Figure6
    visually inspected; panel contexts agree.
  target_ids:
  - GO:0031021
  evidence_ids:
  - record-4
  - prior-4
  - bao
  - liu
  - lynch
  - shen
  - nie
  - micro-go
  - imtoc-uniprot
  - bao-figure6
  - imtocs-agent-family-IPR024312
  - imtocs-agent-family-IPR045110
  - imtocs-agent-family-IPR051964
  - imtocs-agent-taxon-species
  - imtocs-agent-taxon-stock
- assessment_id: current-5
  area: graph
  topic: mating projection actin fusion focus current full-record reassessment
  outcome: concern
  summary: Original frozen-input assessment is scientifically sound within stated
    limits. Current record retains exact GO focus identity, part_of topology, actin
    and motor identities, Fus1-dependent aster and myosin focalization. The newly
    added hydrolase-to-dissolution edge overstates the known export route (F7). Joint
    Myo51/Myo52 focalization remains distinct from tested Myo52-tail cargo localization;
    no equivalent direct transport by both motors is established.
  target_ids:
  - GO:1990819
  evidence_ids:
  - record-5
  - prior-5
  - dudin
  - scott
  - micro-go
  - fusion-focus-agent-act1
  - fusion-focus-agent-fus1
  - fusion-focus-agent-myo51
  - fusion-focus-agent-myo52
- assessment_id: current-8
  area: graph
  topic: median body current full-record reassessment
  outcome: supported
  summary: Current Q969B0 addition is a verified reviewed kin-13 exemplar in species5741,
    preserving distinction between protein identifier and membership evidence. UniProt
    labels it Fragment and identifies Polish sequence source; Park2022 WB/ATCC30957
    localization supports the current citation without claiming that the exemplar
    sequence is the experimental strain. Dawson2007 demonstrates GFP Kin13/EB1 median-body
    localization and 48h S280N volume reduction while early-mitotic arrays can elongate/persist.
    Giardia synonyms remain accepted; GO identity and topology agree. The later review
    retains an enigmatic function and labels reservoir support as a hypothesis; a
    definite physiological function need not be invented.
  target_ids:
  - GO:0097568
  evidence_ids:
  - record-8
  - prior-8
  - dawson
  - kin13
  - park
  - hagen
  - micro-go
  - median-topology
  - median-body-agent-species
- assessment_id: current-6
  area: grounding
  topic: mating projection septin ring current scope and grounding
  outcome: concern
  summary: Exact localized identity and hierarchy are supported and unchanged. Generic
    septin proteins can be grounded at family level without resolving complete assembly
    membership; retain the original minor finding and its separate unresolved species/paralogue/accessory
    boundary. The proposed mating-barrier qualification is still needed; primary interaction/localization
    results do not demonstrate diffusion exclusion.
  target_ids:
  - GO:0032175
  evidence_ids:
  - record-6
  - prior-6
  - septin-family
  - septin-go
  - douglas
  - versele
  - giot990
  - giot992
  - giot993
  - giot995
- assessment_id: current-7
  area: grounding
  topic: medial cortex septin ring current scope and grounding
  outcome: concern
  summary: Exact localized identity and hierarchy are supported and unchanged. Generic
    septin proteins can be grounded at family level without resolving complete assembly
    membership; retain the original minor finding and its separate unresolved species/paralogue/accessory
    boundary. Secondary literature supplies bounded contextual support, not proof
    of a universal mechanism or inventory.
  target_ids:
  - GO:0036391
  evidence_ids:
  - record-7
  - prior-7
  - septin-family
  - septin-go
  - douglas
  - versele
- assessment_id: current-9
  area: grounding
  topic: meiotic septin complex current scope and grounding
  outcome: concern
  summary: Exact localized identity and hierarchy are supported and unchanged. Generic
    septin proteins can be grounded at family level without resolving complete assembly
    membership; retain the original minor finding and its separate unresolved species/paralogue/accessory
    boundary. Secondary literature supplies bounded contextual support, not proof
    of a universal mechanism or inventory.
  target_ids:
  - GO:0032152
  evidence_ids:
  - record-9
  - prior-9
  - septin-family
  - septin-go
  - douglas
  - versele
- assessment_id: history-correction
  area: representation
  topic: Historical iMTOC oversight and current correction
  outcome: supported
  summary: The original iMTOC clean assessment missed the frozen gamma_tuc GENE_OR_PROTEIN
    mismatch. Current main has already corrected that PROTEIN_COMPLEX/GO:0000930 node
    to STRUCTURE under issue2404. This follow-up explicitly assesses the corrected
    bytes; it neither retroactively changes the old verdict nor reopens completed
    scientific curation.
  target_ids:
  - GO:0031021
  evidence_ids:
  - record-4
  - prior-4
  - micro-go
  - staleness
findings:
- finding_id: F1
  issue_key: mating-projection-septin-ring-generic-family-withheld
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Generic septin family grounding is withheld for an unresolved localized cohort
  description: The component is declared as septin proteins, but its grounding rationale
    requires resolving all ring-forming fungal paralogues before assigning a family.
    Native IPR016491 already identifies this generic class. Localized membership,
    exact paralogues and accessory boundaries remain separate questions and do not
    prevent class-level grounding.
  target_ids:
  - GO:0032175
  field_paths:
  - components[component_id=septin_proteins].grounding
  - components[component_id=septin_proteins].grounding_status
  - components[component_id=septin_proteins].grounding_notes
  evidence_ids:
  - record-6
  - prior-6
  - septin-family
  - septin-go
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/mating_projection_septin_ring.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Components
  native_severity: minor
  normalization_reason: Bounded curation inconsistency; the assembly identity, cautious
    example boundary and existing nonmechanistic graph remain supported.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T073357Z-mating-projection-septin-ring-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2498
- finding_id: F2
  issue_key: mating-projection-septin-ring-barrier-qualification
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: The function wording upgrades a proposed barrier role
  description: The function says the ring can act as a barrier and its GO evidence
    note states the barrier role without qualification. Native GO says may, Douglas
    presents this as a model, and the target definition itself retains that uncertainty.
    The inspected 1997 interaction/localization experiments do not establish diffusion
    exclusion. Restore the same uncertainty at the function assertion; this does not
    reject the proposed role.
  target_ids:
  - GO:0032175
  field_paths:
  - functions[function_id=shmoo_neck_mating_factor_barrier].description
  - functions[function_id=shmoo_neck_mating_factor_barrier].evidence
  evidence_ids:
  - record-6
  - prior-6
  - septin-family
  - septin-go
  - douglas
  - giot995
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/mating_projection_septin_ring.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Evidence
  native_severity: minor
  normalization_reason: Bounded curation inconsistency; the assembly identity, cautious
    example boundary and existing nonmechanistic graph remain supported.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T073357Z-mating-projection-septin-ring-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2497
- finding_id: F3
  issue_key: medial-cortex-septin-ring-family-grounding-scope
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Assembly-cohort criterion leaves generic Septin family ungrounded
  description: The generic septin-proteins row is REVIEWED_LABEL_ONLY while the rationale
    waits for an exact accession for its complete developmental or localized cohort.
    Native IPR016491 identifies the named generic Septin family. Reconcile that mapping
    with the status, notes and TODO, retaining the separate unresolved species-specific
    and accessory inventory.
  target_ids:
  - GO:0036391
  field_paths:
  - components[component_id=septin_proteins].grounding_status
  - components[component_id=septin_proteins].grounding_notes
  - discussions[discussion_id=resolve_medial_cortex_septin_ring_components]
  evidence_ids:
  - record-7
  - prior-7
  - septin-family
  - septin-go
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/medial_cortex_septin_ring.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Components
  native_severity: minor
  normalization_reason: Bounded resolvable family mapping; exact structure identity,
    hierarchy and descriptive graph remain supported.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T073422Z-medial-cortex-septin-ring-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2499
- finding_id: F4
  issue_key: meiotic-septin-complex-family-grounding-scope
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Assembly-cohort criterion leaves generic Septin family ungrounded
  description: The generic septin-proteins row is REVIEWED_LABEL_ONLY while the rationale
    waits for an exact accession for its complete developmental or localized cohort.
    Native IPR016491 identifies the named generic Septin family. Reconcile that mapping
    with the status, notes and TODO, retaining the separate unresolved species-specific
    and accessory inventory.
  target_ids:
  - GO:0032152
  field_paths:
  - components[component_id=septin_proteins].grounding_status
  - components[component_id=septin_proteins].grounding_notes
  - discussions[discussion_id=resolve_meiotic_septin_complex_components]
  evidence_ids:
  - record-9
  - prior-9
  - septin-family
  - septin-go
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/meiotic_septin_complex.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Components
  native_severity: minor
  normalization_reason: Bounded resolvable family mapping; exact structure identity,
    hierarchy and descriptive graph remain supported.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T073648Z-meiotic-septin-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2500
- finding_id: F5
  issue_key: inner-plaque-of-mitotic-spindle-pole-body-phase-wording
  category: scope
  severity: minor
  status: open
  certainty: confirmed
  title: Mitotic-cell-cycle subtype wording can imply M-phase restriction
  description: The graph description, first edge description and boundary resolution
    say mitosis-specific. GO denotes the mitotic-cell-cycle SPB subtype. This bounded
    wording ambiguity can imply narrower M-phase restriction; it is not proof the
    author intended exclusivity. The original review explained correct scope but did
    not make the discrepancy actionable.
  target_ids:
  - GO:0061497
  field_paths:
  - causal_graphs[0].description
  - causal_graphs[0].edges[0].description
  - discussions[0].resolution_note
  evidence_ids:
  - record-0
  - prior-0
  - plaque-go
  - plaque2004
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/inner_plaque_of_mitotic_spindle_pole_body.yaml
    role: maintained scientific record
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2501
- finding_id: F6
  issue_key: intermediate-layer-of-mitotic-spindle-pole-body-phase-wording
  category: scope
  severity: minor
  status: open
  certainty: confirmed
  title: Mitotic-cell-cycle subtype wording can imply M-phase restriction
  description: The graph description, first edge description and boundary resolution
    say mitosis-specific. GO denotes the mitotic-cell-cycle SPB subtype. This bounded
    wording ambiguity can imply narrower M-phase restriction; it is not proof the
    author intended exclusivity. The original review explained correct scope but did
    not make the discrepancy actionable.
  target_ids:
  - GO:0061498
  field_paths:
  - causal_graphs[0].description
  - causal_graphs[0].edges[0].description
  - discussions[0].resolution_note
  evidence_ids:
  - record-2
  - prior-2
  - plaque-go
  - plaque2004
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/intermediate_layer_of_mitotic_spindle_pole_body.yaml
    role: maintained scientific record
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2502
- finding_id: F7
  issue_key: mating-focus-unproven-vesicular-hydrolase-export
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Hydrolase edge overstates a demonstrated vesicular export mechanism
  description: The added hydrolase-to-wall-dissolution edge says glucanase-containing
    secretory vesicles release hydrolases. Dudin2015 supports focal enrichment, Myo52-tail
    dependence and wall erosion, but Agn2, Eng2 and Exg3 lack signal sequences/transmembrane
    domains and their route outside the cell is unknown. The reviewed record must
    not upgrade likely cargo localization into established vesicle-mediated secretion.
  target_ids:
  - GO:1990819
  field_paths:
  - causal_graphs[graph_id=fus1_actin_focus_wall_dissolution].edges[subject=cell_wall_hydrolases,object=cell_wall_dissolution].description
  - causal_graphs[graph_id=fus1_actin_focus_wall_dissolution].edges[subject=cell_wall_hydrolases,object=cell_wall_dissolution].evidence
  evidence_ids:
  - record-5
  - prior-5
  - dudin
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/mating_projection_actin_fusion_focus.yaml
    role: maintained scientific record
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2503
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0032175
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/mating_projection_septin_ring.yaml
    role: maintained scientific record
  description: Ground the generic septin-proteins component to verified IPR016491
    using an appropriate native grounding status, and rewrite its rationale to preserve
    the unresolved localized cohort and accessory questions.
  acceptance_checks:
  - The component label and family scope correspond to Septin.
  - Do not infer taxon examples, paralogue membership, essentiality, stoichiometry
    or Afr1 inclusion from this family assignment.
  - Preserve the GO:0032175 versus GO:0032162 boundary discussion.
  - Run documented native schema, strict, label, history and generated-product checks
    after separately authorized curation.
  generator: Maintained structure YAML; just render derives pages.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - GO:0032175
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/mating_projection_septin_ring.yaml
    role: maintained scientific record
  description: Use may act or equivalent proposed-role wording in the function description
    and GO evidence note, retaining the specific shmoo-neck location and the proposed
    localization of mating factors.
  acceptance_checks:
  - Definition, function description and evidence notes consistently identify the
    barrier as proposed.
  - Do not add a demonstrated barrier edge, direct-binding assertion or obligatory
    Afr1 constituent claim.
  - Keep ring-versus-band and experimental-example uncertainty explicit.
  - Run documented native schema, strict, label, history and generated-product checks
    after separately authorized curation.
  generator: Maintained structure YAML; just render derives pages.
- action_id: A3
  finding_ids:
  - F3
  target_ids:
  - GO:0036391
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/medial_cortex_septin_ring.yaml
    role: maintained scientific record
  description: Under separately authorized curation, map the generic septin class
    to verified IPR016491 and reconcile status/notes/TODO while preserving unresolved
    assembly membership.
  acceptance_checks:
  - Verify native Septin family name/type and retain independent structure-localization
    evidence.
  - Do not infer a universal subunit set, copy count, taxonomic distribution or individual-paralog
    essentiality.
  - Use the guarded scientific writer and append curation/history records; run native
    schema, strict, label, history and generated-page checks.
  generator: Maintained structure YAML; just render derives pages.
- action_id: A4
  finding_ids:
  - F4
  target_ids:
  - GO:0032152
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/meiotic_septin_complex.yaml
    role: maintained scientific record
  description: Under separately authorized curation, map the generic septin class
    to verified IPR016491 and reconcile status/notes/TODO while preserving unresolved
    assembly membership.
  acceptance_checks:
  - Verify native Septin family name/type and retain independent structure-localization
    evidence.
  - Do not infer a universal subunit set, copy count, taxonomic distribution or individual-paralog
    essentiality.
  - Use the guarded scientific writer and append curation/history records; run native
    schema, strict, label, history and generated-page checks.
  generator: Maintained structure YAML; just render derives pages.
- action_id: A5
  finding_ids:
  - F5
  target_ids:
  - GO:0061497
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/inner_plaque_of_mitotic_spindle_pole_body.yaml
    role: maintained scientific record
  description: Separately curate the three fields to consistently say of the mitotic-cell-cycle
    SPB, retaining exact identity and topology.
  acceptance_checks:
  - All three fields preserve whole mitotic-cell-cycle scope without unsupported M-phase
    exclusivity.
  - Use guarded writer, append curation/history, regenerate products and run documented
    schema, strict, labels and QC gates in separate curation work.
- action_id: A6
  finding_ids:
  - F6
  target_ids:
  - GO:0061498
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/intermediate_layer_of_mitotic_spindle_pole_body.yaml
    role: maintained scientific record
  description: Separately curate the three fields to consistently say of the mitotic-cell-cycle
    SPB, retaining exact identity and topology.
  acceptance_checks:
  - All three fields preserve whole mitotic-cell-cycle scope without unsupported M-phase
    exclusivity.
  - Use guarded writer, append curation/history, regenerate products and run documented
    schema, strict, labels and QC gates in separate curation work.
- action_id: A7
  finding_ids:
  - F7
  target_ids:
  - GO:1990819
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/mating_projection_actin_fusion_focus.yaml
    role: maintained scientific record
  description: Separately restrict the edge and evidence note to demonstrated focal
    glucanase enrichment and local wall erosion; retain the unknown export route.
  acceptance_checks:
  - No established vesicle-mediated export is asserted for Agn2/Eng2/Exg3.
  - Preserve distinction between joint myosin focalization and Myo52-tail cargo experiments.
  - Guarded writer, curation/history, native validation and regenerated products in
    separate curation PR.
limitations:
- All original saved reviews remain historical observations against their frozen bytes.
  Their old validation receipts are not current CI or QC evidence.
- Current primary papers and relevant result/method/caption sections were inspected
  by independent agents; raw microscopy, movies and every supplementary protocol were
  not independently reconstructed.
- Bao Figure6 was visually inspected; other microtubule/fusion microscopy was checked
  through text/captions, not new image analysis.
- Zimmerman2004 and Piva2004 full-text details were not newly independently recovered.
  Hardin2017 primary PDF was not reread in this pass; the current Hagen secondary
  review preserves the reservoir hypothesis as unresolved.
- Jaspersen/Winey2004 was read through an author-manuscript browser extraction, not
  an authenticated publisher PDF. Douglas, Versele and Hagen are secondary context
  and do not establish uninspected primary mechanisms.
- Four Giot primary page scans990/992/993/995 were visually read; this pass does not
  claim rereading all original pages988-996.
- The installed structured-source adapter could not run because of OS access restrictions.
  Native catalogue fallback supports coverage-based non-applicability; physical subject
  matter alone is not that criterion.
- Review completion does not promote any scientific record status or authorize curation.
  Seven scientific findings stay open for separate record work.
- The optional full-corpus identifier scan was still running when this immutable observation
  finished; it supplies no completed verdict here. The separate PR publication receipt
  will report its actual final exit and unresolved coverage before merge.
- Label correspondence skipped923 pairs without an adapter. Two early QC attempts
  stopped on incomplete local Git provenance objects; missing blobs and37 source commits
  were fetched before successful current QC. No retained bundle was changed to bypass
  provenance checks.
notes:
- The canary is PR2344 only. No other batch PR or Intel-session branch is modified.
- One explicit issue-bearing batch follows the repository issue-only gate. Clean current
  iMTOC, median-body and generic plaque assessments are included as members of this
  same requested cohort; no issues are fabricated to force standalone clean bundles.
- Original ten YAML/Markdown pairs are preserved byte-for-byte. Current main was merged
  normally; no rebase or force push.
- Review-artifact remediation issues2504-2507 concern the missed historical node type,
  omitted phase findings, stale currentness, and adapter rationale. The current assessments
  and actual check results above supply their corrections. Scientific issues2497-2503
  remain separate.
- Independent draft re-review additionally corrected evidence links, frozen Figure6
  input, dangling scratch finding ID, page-specific Giot summaries and secondary-literature
  typing, tracked by issues2508-2512. Those are review-artifact corrections, not scientific
  curation.
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T073051Z-inner-plaque-of-mitotic-spindle-pole-body-audit
  relationship: Current-input follow-up; original immutable observation retained.
    Stable existing finding keys retain exact previous occurrences.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T073051Z-inner-plaque-of-spindle-pole-body-audit
  relationship: Current-input follow-up; original immutable observation retained.
    Stable existing finding keys retain exact previous occurrences.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T073051Z-intermediate-layer-of-mitotic-spindle-pole-body-audit
  relationship: Current-input follow-up; original immutable observation retained.
    Stable existing finding keys retain exact previous occurrences.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T073051Z-intermediate-layer-of-spindle-pole-body-audit
  relationship: Current-input follow-up; original immutable observation retained.
    Stable existing finding keys retain exact previous occurrences.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T073259Z-interphase-microtubule-organizing-center-audit
  relationship: Current-input follow-up; original immutable observation retained.
    Stable existing finding keys retain exact previous occurrences.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T073259Z-mating-projection-actin-fusion-focus-audit
  relationship: Current-input follow-up; original immutable observation retained.
    Stable existing finding keys retain exact previous occurrences.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T073357Z-mating-projection-septin-ring-audit
  relationship: Current-input follow-up; original immutable observation retained.
    Stable existing finding keys retain exact previous occurrences.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T073422Z-medial-cortex-septin-ring-audit
  relationship: Current-input follow-up; original immutable observation retained.
    Stable existing finding keys retain exact previous occurrences.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T073648Z-median-body-audit
  relationship: Current-input follow-up; original immutable observation retained.
    Stable existing finding keys retain exact previous occurrences.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T073648Z-meiotic-septin-complex-audit
  relationship: Current-input follow-up; original immutable observation retained.
    Stable existing finding keys retain exact previous occurrences.
links:
- https://github.com/CultureBotAI/CellStructureMech/pull/2344
- https://github.com/CultureBotAI/CellStructureMech/issues/2497
- https://github.com/CultureBotAI/CellStructureMech/issues/2498
- https://github.com/CultureBotAI/CellStructureMech/issues/2499
- https://github.com/CultureBotAI/CellStructureMech/issues/2500
- https://github.com/CultureBotAI/CellStructureMech/issues/2501
- https://github.com/CultureBotAI/CellStructureMech/issues/2502
- https://github.com/CultureBotAI/CellStructureMech/issues/2503
- https://github.com/CultureBotAI/CellStructureMech/issues/2504
- https://github.com/CultureBotAI/CellStructureMech/issues/2505
- https://github.com/CultureBotAI/CellStructureMech/issues/2506
- https://github.com/CultureBotAI/CellStructureMech/issues/2507
- https://github.com/CultureBotAI/CellStructureMech/issues/2508
- https://github.com/CultureBotAI/CellStructureMech/issues/2509
- https://github.com/CultureBotAI/CellStructureMech/issues/2510
- https://github.com/CultureBotAI/CellStructureMech/issues/2511
- https://github.com/CultureBotAI/CellStructureMech/issues/2512
```
