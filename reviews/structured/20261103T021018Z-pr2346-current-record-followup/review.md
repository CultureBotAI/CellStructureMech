# PR 2346: current-input review of ten cytoskeletal records and adversarial follow-up

- Review: 20261103T021018Z-pr2346-current-record-followup
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-11-03T01:50:31Z
- Finished UTC: 2026-11-03T02:10:18Z
- Reviewer: Codex root synthesis with three independent read-only adversarial reviewers (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Current-input reassessment of the exact ten records in PR2346. Only microtubule changed since its frozen input: two reviewed protein examples and history were added. Three minor scientific curation findings remain: mitotic septin family grounding, outer mitotic plaque cell-cycle wording, and distinct beta-tubulin genes mislabeled as synonyms. Seven records have qualified supported assessments; three need curation. This issue-bearing batch repairs stale-currentness, the omitted phase-wording finding and adapter-coverage reasoning while preserving all original reviews and all scientific records.

## Scope And Provenance

Entire ten-record PR2346 cohort, assessed against current main 0ca1cafbc4841d27447043385df4b0ec0717820c. Exact original frozen hashes were compared with current maintained bytes. Current schema/source/claim scopes are reassessed; no scientific record, status or history mutation.

Selection: Exactly the ten record paths reviewed in original PR2346 head de122cf47c47daf8299d72b2be4a778003fef85b. Deterministic complete cohort, not a sample from the1022-record corpus.
Coverage: full; 10 reviewed / 10 in the declared population.
Source: working_tree at Git base 9d7ce4c503b68329385b8c73999c721c00deef34.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0035974 | data/structures/cytoskeleton/meiotic_spindle_pole_body.yaml | maintained | meiotic spindle pole body |
| GO:0044732 | data/structures/cytoskeleton/mitotic_spindle_pole_body.yaml | maintained | mitotic spindle pole body |
| GO:0071958 | data/structures/cytoskeleton/new_mitotic_spindle_pole_body.yaml | maintained | new mitotic spindle pole body |
| GO:0032151 | data/structures/cytoskeleton/mitotic_septin_complex.yaml | maintained | mitotic septin complex |
| GO:0160067 | data/structures/cytoskeleton/new_spindle_pole_body_sin_signaling_complex.yaml | maintained | new spindle pole body SIN signaling complex |
| GO:0005874 | data/structures/cytoskeleton/microtubule.yaml | maintained | microtubule |
| GO:0005880 | data/structures/cytoskeleton/nuclear_microtubule.yaml | maintained | nuclear microtubule |
| GO:0061499 | data/structures/cytoskeleton/outer_plaque_of_mitotic_spindle_pole_body.yaml | maintained | outer plaque of mitotic spindle pole body |
| GO:0005824 | data/structures/cytoskeleton/outer_plaque_of_spindle_pole_body.yaml | maintained | outer plaque of spindle pole body |
| cellstructuremech:nucleus_basal_body_connector | data/structures/cytoskeleton/nucleus_basal_body_connector.yaml | maintained | nucleus-basal body connector |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full native QC | passed | True | GO:0035974, GO:0044732, GO:0071958, GO:0032151, GO:0160067, GO:0005874, GO:0005880, GO:0061499, GO:0005824, cellstructuremech:nucleus_basal_body_connector | Full QC passed:1054 tests passed,3 skipped; strict schema, history, generated products and other native gates passed. |
| Native label correspondence | passed | True | GO:0035974, GO:0044732, GO:0071958, GO:0032151, GO:0160067, GO:0005874, GO:0005880, GO:0061499, GO:0005824, cellstructuremech:nucleus_basal_body_connector | 4232 canonical,50 synonym and9 exception matches;923 SKIPPED_NO_ADAPTER pairs are not authority verification. |
| TraitMech references | passed | True | GO:0035974, GO:0044732, GO:0071958, GO:0032151, GO:0160067, GO:0005874, GO:0005880, GO:0061499, GO:0005824, cellstructuremech:nucleus_basal_body_connector | TraitMech references returned exit0; see exact receipt. |
| Pinned governed files | passed | True | GO:0035974, GO:0044732, GO:0071958, GO:0032151, GO:0160067, GO:0005874, GO:0005880, GO:0061499, GO:0005824, cellstructuremech:nucleus_basal_body_connector | Pinned governed files returned exit0; see exact receipt. |
| Native identifier resolver | passed | True | GO:0035974, GO:0044732, GO:0071958, GO:0032151, GO:0160067, GO:0005874, GO:0005880, GO:0061499, GO:0005824, cellstructuremech:nucleus_basal_body_connector | Exit0 with5264 OK,909 UNREACHABLE PMIDs (oversized GET HTTP414),254 SKIPPED. Existing issue2514 tracks batching and the misleading terminal universal-success text. Target authority evidence and supplemental PMID checks are separate. |
| validate meiotic spindle pole body | passed | True | GO:0035974 | Documented focused command returned exit0. |
| validate-strict meiotic spindle pole body | passed | True | GO:0035974 | Documented focused command returned exit0. |
| validate mitotic spindle pole body | passed | True | GO:0044732 | Documented focused command returned exit0. |
| validate-strict mitotic spindle pole body | passed | True | GO:0044732 | Documented focused command returned exit0. |
| validate new mitotic spindle pole body | passed | True | GO:0071958 | Documented focused command returned exit0. |
| validate-strict new mitotic spindle pole body | passed | True | GO:0071958 | Documented focused command returned exit0. |
| validate mitotic septin complex | passed | True | GO:0032151 | Documented focused command returned exit0. |
| validate-strict mitotic septin complex | passed | True | GO:0032151 | Documented focused command returned exit0. |
| validate new spindle pole body SIN signaling complex | passed | True | GO:0160067 | Documented focused command returned exit0. |
| validate-strict new spindle pole body SIN signaling complex | passed | True | GO:0160067 | Documented focused command returned exit0. |
| validate microtubule | passed | True | GO:0005874 | Documented focused command returned exit0. |
| validate-strict microtubule | passed | True | GO:0005874 | Documented focused command returned exit0. |
| validate nuclear microtubule | passed | True | GO:0005880 | Documented focused command returned exit0. |
| validate-strict nuclear microtubule | passed | True | GO:0005880 | Documented focused command returned exit0. |
| validate outer plaque of mitotic spindle pole body | passed | True | GO:0061499 | Documented focused command returned exit0. |
| validate-strict outer plaque of mitotic spindle pole body | passed | True | GO:0061499 | Documented focused command returned exit0. |
| validate outer plaque of spindle pole body | passed | True | GO:0005824 | Documented focused command returned exit0. |
| validate-strict outer plaque of spindle pole body | passed | True | GO:0005824 | Documented focused command returned exit0. |
| validate nucleus-basal body connector | passed | True | cellstructuremech:nucleus_basal_body_connector | Documented focused command returned exit0. |
| validate-strict nucleus-basal body connector | passed | True | cellstructuremech:nucleus_basal_body_connector | Documented focused command returned exit0. |
| Supplemental bounded PMID authority checks | passed | True | GO:0035974, GO:0044732, GO:0071958, GO:0032151, GO:0160067, GO:0005874, GO:0005880, GO:0061499, GO:0005824, cellstructuremech:nucleus_basal_body_connector | 909/909 PMIDs OK in19 bounded requests. Native full-command coverage remains separately disclosed. |
| Official iModulonDB catalogue applicability | not_applicable | False | GO:0035974, GO:0044732, GO:0071958, GO:0032151, GO:0160067, GO:0005874, GO:0005880, GO:0061499, GO:0005824, cellstructuremech:nucleus_basal_body_connector | Official catalogue fallback contains20 organisms/28 datasets and no matching target yeast/protist. No new CLI runner execution is claimed; prior canary OS unavailability remains explicit. |
| Independent claim-level source review | passed | True | GO:0035974, GO:0044732, GO:0071958, GO:0032151, GO:0160067, GO:0005874, GO:0005880, GO:0061499, GO:0005824, cellstructuremech:nucleus_basal_body_connector | Three independent read-only reviewers covered all ten current records and their original bundles. This records source-review completion with explicit limitations and findings; final artifact/head acceptance is a separate publication gate. |

## Scientific And Domain Assessments

### meiotic spindle pole body current scientific assessment

evidence: supported. Targets: GO:0035974.

The exact whole meiotic-SPB identity, GO parent and S. cerevisiae example are supported. The graph correctly scopes the MOP substructure and normal prospore-membrane initiation site to budding-yeast meiosis II. Knop/Strasser, Bajgier and Mathieson distinguish normal membrane initiation/docking from precursor targeting and mutant untethered membranes; the target asserts neither autonomous fusion catalysis nor absolute mature-plaque dependence in every mutant. Optional composition remains a documented limitation, with no asserted erroneous family accessions or copy counts.

### mitotic spindle pole body current scientific assessment

evidence: supported. Targets: GO:0044732.

GO supports the exact mitotic-cell-cycle subtype and half-bridge/intermediate-layer parthood. G1 duplication is compatible with this scope; the half-bridge edge is a bounded assembly-site statement, not a complete molecular recruitment order. Primary core-architecture context and the cited review support nuclear/cytoplasmic microtubule organization. Optional database candidates remain bounded by strain, family/domain, subcomplex and stoichiometry scope; no erroneous composition is asserted.

### new mitotic spindle pole body current scientific assessment

evidence: supported. Targets: GO:0071958.

The exact GO identity, new-SPB synonym, mitotic-SPB parent and S. pombe example are supported. Grallert Results sec4/sec5/sec8 and Discussion sec13 demonstrate conservative age labeling, active SIN on the new SPB in anaphase B/G1, and history-dependent Fin1 recruitment. The target avoids equating Fin1 with an exclusive or permanent new-pole constituent and keeps local generic duplication placeholders distinct from the exact age/asymmetry class. Optional protein-family composition remains unresolved without an asserted mapping error.

### outer plaque of mitotic spindle pole body current scientific assessment

evidence: concern. Targets: GO:0061499.

Exact GO identity, generic-outer-plaque is-a and mitotic-SPB parthood, cytoplasmic orientation and bounded microtubule-organizing function are supported. The meiotic remodeling boundary and optional composition limitations are sound. Three mitosis-specific phrases can imply M-phase restriction; the source supports a mitotic-cell-cycle subtype instead. This is a minor ambiguity requiring wording curation, not rejection of the identity or topology.

### outer plaque of spindle pole body current scientific assessment

evidence: supported. Targets: GO:0005824.

The cytoplasmic plaque identity, whole-SPB parthood, budding-yeast example and bounded cytoplasmic microtubule organization are supported. Three named plaques plus intermediate layers are compatible descriptions. The plaque remains distinct from associated gamma-TuSC, the meiotic remodeling product and the separate prospore-membrane attachment region. No phase-only claim, fixed stoichiometry or exact erroneous protein-family mapping is asserted; optional composition stays a limitation.

### microtubule current scientific assessment

evidence: concern. Targets: GO:0005874.

Exact GO generic alpha/beta microtubule identity, topology and bounded specialized-array examples are supported. InterPro collective class remains honestly label-only. New P09204 and P04690 reviewed accession/name/taxon identities and canonical-query uniqueness are verified. Q6SPP7 remains an unreviewed22aa fragment used only as identity. The new P04690 TUB2 synonym wording is a minor scientific curation request; all record edits stay outside this PR.

### nuclear microtubule current scientific assessment

evidence: supported. Targets: GO:0005880.

Unchanged nuclear microtubule is exact location-defined GO subtype, part of nucleus, with one bounded budding-yeast inner-plaque organization example. Graph is NONMECHANISTIC and does not conflate nuclear location with spindle membership. Optional molecular inventory is explicitly deferred, not falsely asserted. Secondary literature remains identified as secondary.

### nucleus-basal body connector current scientific assessment

evidence: supported. Targets: cellstructuremech:nucleus_basal_body_connector.

Unchanged connector identity, centrin species example, broader rootlet parent, conditional calcium/EGTA/ATP graph, and Figure2 provenance are supported. Living-gamete versus extracted-model context is preserved; ATP potentiation is not contraction or established phosphorylation. Mutant segregation inference is not selective connector ablation; Sfi1/CBP1.1 is a proposal, not imported constituent. Chrysomonad examples and negative gene-induction claim remain abstract-bounded. No new scientific defect found.

### mitotic septin complex current scientific assessment

evidence: concern. Targets: GO:0032151.

Exact generic mitotic heterooligomer and nonmechanistic oligomerization remain supported. Generic Septin family grounding can be resolved independently of full species-specific subunit set. Existing minorF1 remains open.

### new spindle pole body SIN signaling complex current scientific assessment

evidence: supported. Targets: GO:0160067.

Exact new-SPB anaphase signaling complex identity, parentage and narrow S.pombe example/function supported. Source correctly separates prior asymmetry background, newly measured scaffold regulation and proposed Fig8 mechanism. No additional scientific curation defect observed; no compulsory inventory or graph invented.

### Changed microtubule input and accession-versus-gene boundary

grounding: concern. Targets: GO:0005874.

The original microtubule observation predates P09204/P04690 and cannot certify those additions. Both current reviewed accessions, taxon and canonical-name query uniqueness are supported. P04690 represents products of two distinct beta-tubulin genes, so TUB2-as-synonym wording needs a bounded correction. The valid accession and identity-only membership disclaimer remain intact.

### Structured-source organism coverage and physical-mechanism boundary

scope: supported. Targets: GO:0035974, GO:0044732, GO:0071958, GO:0032151, GO:0160067, GO:0005874, GO:0005880, GO:0061499, GO:0005824, cellstructuremech:nucleus_basal_body_connector.

Fresh official catalogue inspection shows no relevant yeast or protist dataset. Downstream organism-specific expression-module searches are not applicable. The original rationales in the named-molecule cases excluded the adapter solely by physical/nontranscriptomic subject matter; this follow-up supplies the missing coverage basis. The nuclear-microtubule record has no named molecular-gene/accession trigger, so no omission is invented there. The prior canary runner failure is historical OS-access evidence, not a newly executed check.

## Findings

### F1: Assembly-cohort criterion leaves generic Septin family ungrounded

minor / open / confirmed; issue key: mitotic-septin-complex-family-grounding-scope.

The generic septin-proteins component remains REVIEWED_LABEL_ONLY while its rationale waits for a mapping for the full mitotic cohort. Native IPR016491 identifies the named family. Reconcile the family mapping, status and notes while retaining the separate unresolved species-specific and accessory inventory.

### F2: Outer mitotic plaque wording can imply unsupported M-phase restriction

minor / open / confirmed; issue key: outer-plaque-mitotic-cell-cycle-wording.

Three mitosis-specific phrases can imply existence restricted to M phase. GO0044732 defines the mitotic-cell-cycle SPB; the cited review describes persistent SPBs and G1 activity. The record provides no evidence for M-phase-only existence. The original review recognized the source limitation but omitted the corresponding curation finding.

### F3: One beta-tubulin protein entry does not make two genes synonyms

minor / open / confirmed; issue key: microtubule-beta-genes-not-synonyms.

The new reviewed beta-tubulin example calls TUB2 a synonym. TUB1 and TUB2 are distinct genes encoding the same amino-acid sequence, and P04690 has separate TUBB1 and TUBB2 gene objects. Shared product/accession does not make these genes aliases.

## Recommended Actions And Acceptance Checks

### A1

Separately ground the generic mitotic septin class to the verified Septin family and reconcile status, notes and TODO while retaining unresolved species/paralogue/accessory membership. Existing consolidated issue2499 tracks this record alongside distinct medial and meiotic targets.

- Verify native IPR016491 name/type and preserve independent assembly-localization evidence.
- Do not infer universal copy counts, paralog essentiality, occurrence or a complete complex from family grounding.
- Use guarded record writing, curation/history and native validation in a separate scientific curation PR.

### A2

Curate the three phrases to of the mitotic-cell-cycle SPB or equivalent, preserving the exact GO identity and relations. Do not edit the record in this review-only PR.

- All three affected fields retain mitotic-cell-cycle subtype scope without unsupported M-phase exclusivity.
- Preserve exact identity/topology and use guarded scientific curation, history and native validation in a separate PR.

### A3

Retain P04690 and its reviewed label/status; replace synonym wording with an explicit statement that one protein entry represents products of the two distinct beta-tubulin genes. Keep accession identity separate from membership.

- Describe two distinct beta-tubulin genes sharing the protein entry/product; preserve valid accession/status/taxon.
- Maintain identity-versus-membership distinction; perform record/history/native validation changes in a separate curation PR.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record-0 | data/structures/cytoskeleton/meiotic_spindle_pole_body.yaml; Entire current maintained YAML; native inspect freezes exact bytes | context_only | Current SHA256 2a99651652ccaa1b26dd8149e44976824366dbe2157a708fb1df0560323b8a75; original frozen SHA256 2a99651652ccaa1b26dd8149e44976824366dbe2157a708fb1df0560323b8a75. Record bytes remain identical to the original frozen input. |
| prior-0 | reviews/structured/20261021T074511Z-meiotic-spindle-pole-body-audit/review.yaml; Original immutable source, evidence, assessments, verdict, findings, actions and limitations | context_only | Historical observation retained; its old checks and source access are not represented as current-head execution. |
| record-1 | data/structures/cytoskeleton/mitotic_spindle_pole_body.yaml; Entire current maintained YAML; native inspect freezes exact bytes | context_only | Current SHA256 6f26eef2c9a8c923eb0c851b4d65b90a696322095208e731be170b6b0c9f0329; original frozen SHA256 6f26eef2c9a8c923eb0c851b4d65b90a696322095208e731be170b6b0c9f0329. Record bytes remain identical to the original frozen input. |
| prior-1 | reviews/structured/20261021T074637Z-mitotic-spindle-pole-body-audit/review.yaml; Original immutable source, evidence, assessments, verdict, findings, actions and limitations | context_only | Historical observation retained; its old checks and source access are not represented as current-head execution. |
| record-2 | data/structures/cytoskeleton/new_mitotic_spindle_pole_body.yaml; Entire current maintained YAML; native inspect freezes exact bytes | context_only | Current SHA256 33ac955370a7476c7bb3f3fca4cfc9464120890e6a3e57fcb3b32d5e2504fb82; original frozen SHA256 33ac955370a7476c7bb3f3fca4cfc9464120890e6a3e57fcb3b32d5e2504fb82. Record bytes remain identical to the original frozen input. |
| prior-2 | reviews/structured/20261021T074637Z-new-mitotic-spindle-pole-body-audit/review.yaml; Original immutable source, evidence, assessments, verdict, findings, actions and limitations | context_only | Historical observation retained; its old checks and source access are not represented as current-head execution. |
| record-3 | data/structures/cytoskeleton/mitotic_septin_complex.yaml; Entire current maintained YAML; native inspect freezes exact bytes | context_only | Current SHA256 99bf85740532379d8f9d88a2f07563cf9853a42e00a367fc5453d598ad308d1e; original frozen SHA256 99bf85740532379d8f9d88a2f07563cf9853a42e00a367fc5453d598ad308d1e. Record bytes remain identical to the original frozen input. |
| prior-3 | reviews/structured/20261021T074638Z-mitotic-septin-complex-audit/review.yaml; Original immutable source, evidence, assessments, verdict, findings, actions and limitations | context_only | Historical observation retained; its old checks and source access are not represented as current-head execution. |
| record-4 | data/structures/cytoskeleton/new_spindle_pole_body_sin_signaling_complex.yaml; Entire current maintained YAML; native inspect freezes exact bytes | context_only | Current SHA256 84ade1d5217bae8fa401f096724d0892e76378469bec45c6ea25e961a0e28cae; original frozen SHA256 84ade1d5217bae8fa401f096724d0892e76378469bec45c6ea25e961a0e28cae. Record bytes remain identical to the original frozen input. |
| prior-4 | reviews/structured/20261021T074638Z-new-spindle-pole-body-sin-signaling-complex-audit/review.yaml; Original immutable source, evidence, assessments, verdict, findings, actions and limitations | context_only | Historical observation retained; its old checks and source access are not represented as current-head execution. |
| record-5 | data/structures/cytoskeleton/microtubule.yaml; Entire current maintained YAML; native inspect freezes exact bytes | context_only | Current SHA256 170483f42c69e1b91f2e11ace0483b30aa3beeba791119a77c644c99da1decc6; original frozen SHA256 06773fdcef54b61e7ed2a8a4c1066dfed8ba71dce8050eb39a879fab702b7498. Changed input reassessed against current primary and authority sources. |
| prior-5 | reviews/structured/20261021T074814Z-microtubule-audit/review.yaml; Original immutable source, evidence, assessments, verdict, findings, actions and limitations | context_only | Historical observation retained; its old checks and source access are not represented as current-head execution. |
| record-6 | data/structures/cytoskeleton/nuclear_microtubule.yaml; Entire current maintained YAML; native inspect freezes exact bytes | context_only | Current SHA256 09096977c74bdb36271d09b2a8aa1ac4c269ff8f3adbc854beae8b348f8aa252; original frozen SHA256 09096977c74bdb36271d09b2a8aa1ac4c269ff8f3adbc854beae8b348f8aa252. Record bytes remain identical to the original frozen input. |
| prior-6 | reviews/structured/20261021T074814Z-nuclear-microtubule-audit/review.yaml; Original immutable source, evidence, assessments, verdict, findings, actions and limitations | context_only | Historical observation retained; its old checks and source access are not represented as current-head execution. |
| record-7 | data/structures/cytoskeleton/outer_plaque_of_mitotic_spindle_pole_body.yaml; Entire current maintained YAML; native inspect freezes exact bytes | context_only | Current SHA256 9197bc8f9b1fed339d56314bb682274576fa41bb94b26e2d09823e14a26ec226; original frozen SHA256 9197bc8f9b1fed339d56314bb682274576fa41bb94b26e2d09823e14a26ec226. Record bytes remain identical to the original frozen input. |
| prior-7 | reviews/structured/20261021T074815Z-outer-plaque-of-mitotic-spindle-pole-body-audit/review.yaml; Original immutable source, evidence, assessments, verdict, findings, actions and limitations | context_only | Historical observation retained; its old checks and source access are not represented as current-head execution. |
| record-8 | data/structures/cytoskeleton/outer_plaque_of_spindle_pole_body.yaml; Entire current maintained YAML; native inspect freezes exact bytes | context_only | Current SHA256 2aa7db5e2c632a9934dda8fbc3c57a85d1742c6aa7322e769f6f162103f17142; original frozen SHA256 2aa7db5e2c632a9934dda8fbc3c57a85d1742c6aa7322e769f6f162103f17142. Record bytes remain identical to the original frozen input. |
| prior-8 | reviews/structured/20261021T074815Z-outer-plaque-of-spindle-pole-body-audit/review.yaml; Original immutable source, evidence, assessments, verdict, findings, actions and limitations | context_only | Historical observation retained; its old checks and source access are not represented as current-head execution. |
| record-9 | data/structures/cytoskeleton/nucleus_basal_body_connector.yaml; Entire current maintained YAML; native inspect freezes exact bytes | context_only | Current SHA256 89e5e96440535f65493ee4b2928b835f415f79358200f32d877ec59487300f0d; original frozen SHA256 89e5e96440535f65493ee4b2928b835f415f79358200f32d877ec59487300f0d. Record bytes remain identical to the original frozen input. |
| prior-9 | reviews/structured/20261021T075001Z-nucleus-basal-body-connector-audit/review.yaml; Original immutable source, evidence, assessments, verdict, findings, actions and limitations | context_only | Historical observation retained; its old checks and source access are not represented as current-head execution. |
| context-mop | data/structures/cytoskeleton/meiotic_outer_plaque.yaml; Entire maintained context YAML; native inspect freezes exact bytes | context_only | Context only: whole meiotic outer-plaque boundary used in the meiotic spindle-pole assessment; not an additional reviewed target. |
| context-spb | data/structures/cytoskeleton/spindle_pole_body.yaml; Entire maintained context YAML; native inspect freezes exact bytes | context_only | Context only: generic spindle-pole old/new role placeholders used in the new mitotic spindle-pole assessment; not an additional reviewed target. |
| meiotic-spb-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0035974%2CGO%3A0005816%2CGO%3A0031322%2CGO%3A0005628%2CGO%3A0005824%2CGO%3A0070057; All six returned definitions, active flags and parent child relations | supports | GO0035974 is the active meiotic SPB class under GO0005816. GO0031322 denotes the remodeling process; GO0005628 the prospore membrane; GO0005824 the outer plaque; GO0070057 the membrane attachment region. These are distinct entities. |
| meiotic-spb-agent-taxon | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; taxId, scientificName, rank and lineage | supports | ENA confirms NCBITaxon4932 is Saccharomyces cerevisiae at species rank. |
| meiotic-spb-agent-knop2000-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1093/emboj/19.14.3657&amp;format=json&amp;resultType=core; Exact native EuropePMC result: DOI, PMID, title, authors, year, journal and availability fields | supports | Knop and Strasser2000: DOI10.1093/emboj/19.14.3657, PMID10899120, PMC313968, exact title and authors. |
| meiotic-spb-agent-bajgier2001-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1091/mbc.12.6.1611&amp;format=json&amp;resultType=core; Exact native EuropePMC result: DOI, PMID, title, authors, year, journal and availability fields | supports | Bajgier et al.2001: DOI10.1091/mbc.12.6.1611, PMID11408572, PMC37328, exact title and authors. |
| meiotic-spb-agent-mathieson2010-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1091/mbc.E10-07-0563&amp;format=json&amp;resultType=core; Exact native EuropePMC result: DOI, PMID, title, authors, year, journal and availability fields | supports | Mathieson et al.2010: DOI10.1091/mbc.E10-07-0563, PMID20826607, exact title and authors. This metadata response omits its PMCID; the separately inspected native PMC2965686 article resolves full-text availability. |
| meiotic-spb-agent-knop2000 | https://pmc.ncbi.nlm.nih.gov/articles/PMC313968/?pdf=render; Native PMC313968 HTML, Results sections sec4 and sec7-sec9; Discussion sec11-sec12; figure legends as text. Actual article body, not a PDF or challenge response. | supports | Budding-yeast primary experiments connect Mpc54/Mpc70-dependent meiotic outer-plaque assembly to normal prospore-membrane formation. Precursor targeting can persist without mature plaque assembly. The body distinguishes the whole SPB, its meiosis-II plaque and the growing membrane; fusion-machinery recruitment in Discussion is a model. |
| meiotic-spb-agent-bajgier2001 | https://pmc.ncbi.nlm.nih.gov/articles/PMC37328/?pdf=render; Native PMC37328 HTML, Results sec8, sec11-sec12 and sec15; Discussion sec17; source-specific mutant and meiotic-stage context | supports | Spo21/Mpc70 contributes to meiosis-specific SPB modification. spo21 deletion disrupts plaque and membrane formation while meiotic divisions proceed. cnm67 mutants can form untethered prospore membranes, limiting any claim that attachment to an intact SPB is universally indispensable. |
| meiotic-spb-agent-mathieson2010-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC2965686/?pdf=render; Native PMC2965686 HTML, Results sec11 and sec14-sec18; Discussion sec20-sec23; article identity/DOI in header and text figure legends | supports | Selected Mpc54 point mutants retain meiotic-plaque composition and ultrastructure while impairing vesicle docking and recruitment of Sec4/exocyst factors. The FRET-based model places Mpc54/Spo21 N termini toward the membrane-facing surface; Ady4 is not a stable component, and Spo74 placement is unresolved. Proposed direct binding or exchange mechanisms remain interpretation. |
| mitotic-spb-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0044732%2CGO%3A0005816%2CGO%3A0061496%2CGO%3A0061498; All four returned term definitions, active flags and parent-term child relations | supports | Native GO confirms active GO0044732 under GO0005816, with GO0061496 half bridge and GO0061498 intermediate layer as mitotic-SPB substructures. The exact cell-cycle identity and graph relations are retained. |
| mitotic-spb-agent-strain | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; taxId, scientificName and strain rank | context_only | Candidate sequence and complex entries concern S. cerevisiae S288C, NCBITaxon559292; the record declares the species-level example. |
| mitotic-spb-agent-epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1146/annurev.cellbio.20.022003.114106%20OR%20DOI:10.1091/mbc.E17-06-0397&amp;format=json&amp;resultType=core; Both returned title, author, DOI, PMID, year and journal records | supports | Native metadata confirms Jaspersen and Winey2004 DOI10.1146/annurev.cellbio.20.022003.114106 / PMID15473833 and corroborating Viswanath2017 DOI10.1091/mbc.E17-06-0397 / PMID28814505. |
| mitotic-spb-agent-viswanath2017 | https://pmc-oa-opendata.s3.amazonaws.com/PMC5687031.1/PMC5687031.1.xml; Native JATS Introduction, Figure1 caption and relevant layer-localization Results/Methods | supports | The Introduction and Figure1 distinguish plaques, IL1/IL2 and nuclear/cytoplasmic nucleation sites. Its integrative model concerns the core rather than a complete reconstruction of every SPB constituent or duplication stage. |
| mitotic-spb-agent-candidate-proteins | https://rest.uniprot.org/uniprotkb/search?query=organism_id%3A559292%20AND%20%28gene_exact%3ASPC110%20OR%20gene_exact%3ATUB4%20OR%20gene_exact%3ASPC97%20OR%20gene_exact%3ASPC98%20OR%20gene_exact%3ACMD1%20OR%20gene_exact%3ASPC42%20OR%20gene_exact%3ACNM67%20OR%20gene_exact%3ASPC29%20OR%20gene_exact%3ANUD1%20OR%20gene_exact%3ASPC72%29&amp;format=json&amp;size=50; Relevant accession, reviewed status, name, genes, organism and native family/complex cross-references; optional candidates, not currently asserted examples | context_only | Reviewed S288C entries resolve Spc110 P32380, Spc97 P38863, Spc98 P53540, Tub4 P53378, Spc42 P36094, Cnm67 P53865, Spc29 P33419, Cmd1 P06787, Nud1 P32336 and Spc72 P39723 as possible inventory material. The historical TRM2/NUD1 alias hit is not adopted as Nud1. |
| mitotic-spb-agent-CPX-1198 | https://www.ebi.ac.uk/intact/complex-ws/complex/CPX-1198; complexAc, name, species, participants, systematicName, properties and evidenceType | context_only | CPX1198 is the S288C gamma-tubulin small complex, with Spc97, Spc98 and two Tub4 subunits. It is an associated constituent complex, not an identifier or copy count for the whole SPB. |
| mitotic-spb-agent-CPX-1420 | https://www.ebi.ac.uk/intact/complex-ws/complex/CPX-1420; complexAc, name, species, participants, properties and GO0005823 cross-reference | context_only | CPX1420 is the Spc42/Cnm67 intermediate-layer2 complex. Its narrower complex scope and its central-plaque GO cross-reference must not be collapsed into the whole SPB or all intermediate layers. |
| mitotic-spb-agent-IPR002454 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002454/; Native metadata accession, name, type, description and relevant member/hierarchy fields | context_only | Gamma tubulin is a family-level candidate for Tub4; source localization remains a separate claim. |
| mitotic-spb-agent-IPR007259 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007259/; Native metadata accession, name, type, description and relevant member/hierarchy fields | context_only | Gamma-tubulin complex component protein is a broader family covering several GCP paralogues, not an exact individual Spc97/Spc98 identity. |
| mitotic-spb-agent-IPR021611 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR021611/; Native metadata accession, name, type, description and relevant member/hierarchy fields | context_only | Spindle pole body component Spc42 is an exact named-family candidate. |
| mitotic-spb-agent-IPR040593 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR040593/; Native metadata accession, name, type, description and relevant member/hierarchy fields | context_only | Spc110 C-terminal is a domain, not a whole-protein family; it cannot replace exact whole-component grounding. |
| new-mitotic-spb-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0071958%2CGO%3A0071957%2CGO%3A0044732; All three exact definitions, synonym scopes, active flags and parent-term child relations | supports | GO0071958 is the active new mitotic SPB class, with exact synonym new SPB and parent GO0044732. GO0071957 denotes the distinct old, pre-existing sibling. |
| new-mitotic-spb-agent-taxon | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4896; taxId, scientificName, rank and lineage | supports | ENA confirms Schizosaccharomyces pombe, NCBITaxon4896, at species rank. |
| new-mitotic-spb-agent-grallert2004-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1101/gad.296204&amp;format=json&amp;resultType=core; Exact EuropePMC core result: citation identity and availability fields | supports | Native metadata verifies Grallert et al.2004, DOI10.1101/gad.296204, PMID15132994, PMC406291, exact title, authors and journal. |
| new-mitotic-spb-agent-grallert2004 | https://pmc.ncbi.nlm.nih.gov/articles/PMC406291/?pdf=render; Native PMC406291 HTML: Results sec4-sec5 and sec8-sec9; Discussion sec12-sec14; Methods sec19-sec20; Figure2, Figure5 and Figure8 legends as text | supports | Primary S. pombe lineage labeling identifies active SIN on the new SPB in late anaphase B/G1. Fin1 instead always associates with the old SPB and with only half of new SPBs, depending on parental history. Early localization to both poles and age-dependent maturation delimit the signaling claim. |
| mitotic-outer-plaque-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0061499%2CGO%3A0005824%2CGO%3A0044732%2CGO%3A0005881; All four returned definitions, active flags, synonyms where relevant and parent-term child relations | supports | GO0061499 is the active mitotic outer-plaque class, with is-a parent GO0005824 and parthood in GO0044732. GO0005881 is the exact cytoplasmic-microtubule identity used in the graph. |
| mitotic-outer-plaque-agent-epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:10899120%20OR%20EXT_ID:15473833%20OR%20EXT_ID:28814505&amp;format=json&amp;resultType=core; All three returned title, author, DOI, PMID, year and journal records | supports | Native metadata verifies Jaspersen/Winey2004 DOI10.1146/annurev.cellbio.20.022003.114106 / PMID15473833; Knop/Strasser2000 DOI10.1093/emboj/19.14.3657 / PMID10899120; and corroborating Viswanath2017 DOI10.1091/mbc.E17-06-0397 / PMID28814505. |
| outer-plaque-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0005824%2CGO%3A0005816%2CGO%3A0005881%2CGO%3A0070057; All four returned definitions, active flags, synonyms where relevant and parent-term child relations | supports | GO0005824 is the active cytoplasmic outer-plaque class with SPB parthood in GO0005816. GO0005881 is the exact cytoplasmic-microtubule identity, and GO0070057 denotes a region of the prospore membrane rather than the plaque. |
| spb-ipr021750-cached | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR021750/; Native InterPro metadata accession/name/type/description; reused independently inspected cached response; fresh request at 2026-11-03T01:54:20.713748Z returned HTTP 429 and was not retried | context_only | The Septation initiation Sid4-like family includes Sid4, Ady3 and Cnm67, so it is broader than Cnm67 alone. No new successful retrieval is claimed. |
| spb-jaspersen2004-author-manuscript | https://www.researchgate.net/publication/8241691_THE_BUDDING_YEAST_SPINDLE_POLE_BODY_Structure_Duplication_and_Function; Public author-manuscript pp5-6, pp9-12 and meiotic-SPB pp12-13; browser-extracted text previously retrieved 2026-11-03T00:47:42Z to00:47:43Z and reread for these targets. Snapshot is serialized browser extraction, not native PDF bytes. Secondary literature-review context, corroborated by primary/GO sources. | supports | SPBs persist through the budding-yeast life cycle; G1 growth/duplication is within the mitotic cell cycle. The half bridge is a new-SPB assembly site. Outer-plaque Nud1/Spc72 and associated gamma-tubulin machinery face the cytoplasm; Cnm67 connects layers. Meiotic remodeling replaces Spc72 with Mpc54/Spo21. The source does not imply M-phase-only existence of the mitotic SPB or plaque. |
| current-microtubule-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005874,GO:0099513,GO:0015630; results GO:0005874, GO:0099513, GO:0015630, active names, definitions, synonyms, explicit children relation fields; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/microtubule-agent-go.raw | supports | Exact generic microtubule identity and both parent/parthood relationships verified; usual thirteen protofilaments and dimensions are GO wording, not new universal measurements. |
| current-nuclear-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005880,GO:0005874,GO:0005634,GO:0005822,GO:0005881,GO:0005876; results GO:0005880, GO:0005874, GO:0005634, GO:0005822, GO:0005881, GO:0005876; definitions and children relation fields; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/nuclear-agent-go.raw | supports | Exact location-defined nuclear microtubule and is_a microtubule / part_of nucleus relations verified. Inner plaque is nuclear; spindle membership and nuclear location can overlap. |
| current-connector-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0035253,GO:0051647,GO:0120118,GO:0120269; results GO:0035253, GO:0051647, GO:0120118, GO:0120269; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/connector-agent-go.raw | supports | Rootlet broader-class placement and nucleus-localization function match. Kinetoplastid flagella connector and ciliary centrin arm are separate structures, not aliases of the algal NBBC. |
| current-microtubule-agent-taxon-chlamy | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3055; taxId, scientificName, rank, otherNames; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/microtubule-agent-taxon-chlamy.raw | supports | Species identity verified: 3055 Chlamydomonas reinhardtii. Taxonomy alone does not establish biological occurrence or tested strain. |
| current-microtubule-agent-taxon-giardia | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5741; taxId, scientificName, rank, otherNames; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/microtubule-agent-taxon-giardia.raw | supports | Species identity verified: 5741 Giardia duodenalis. Taxonomy alone does not establish biological occurrence or tested strain. |
| current-nuclear-agent-taxon | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; taxId, scientificName, rank, otherNames; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/nuclear-agent-taxon.raw | supports | Species identity verified: 4932 Saccharomyces cerevisiae. Taxonomy alone does not establish biological occurrence or tested strain. |
| current-connector-agent-taxon-420600 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/420600; taxId, scientificName, rank, otherNames; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/connector-agent-taxon-420600.raw | supports | Species identity verified: 420600 Mallomonas insignis. Taxonomy alone does not establish biological occurrence or tested strain. |
| current-connector-agent-taxon-52555 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/52555; taxId, scientificName, rank, otherNames; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/connector-agent-taxon-52555.raw | supports | Species identity verified: 52555 Synura petersenii. Taxonomy alone does not establish biological occurrence or tested strain. |
| current-microtubule-agent-uniprot | https://rest.uniprot.org/uniprotkb/Q6SPP7.json; entryType, genes, organism, sequence, proteinDescription.flag; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/microtubule-agent-uniprot.raw | supports | Q6SPP7 remains unreviewed TUA2 in taxon3055, a22-residue fragment. Supports accession identity only, not full-length or experimental-strain incorporation. |
| current-new-uniprot-P09204 | https://rest.uniprot.org/uniprotkb/P09204.json; entryType, proteinDescription.recommendedName, genes, organism, cross-references; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/new-uniprot-P09204.raw | supports | P09204 is reviewed Tubulin alpha-1 chain, taxon3055, primary gene TUBA1. Correct accession/status/name in new example; native entry does not itself list historical TUA1 as a synonym. |
| current-new-uniprot-P04690 | https://rest.uniprot.org/uniprotkb/P04690.json; entryType, proteinDescription.recommendedName, genes[0].geneName and genes[1].geneName, organism; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/new-uniprot-P04690.raw | supports | P04690 is reviewed Tubulin beta-1/beta-2 chain, taxon3055. Native genes array contains two separate gene objects TUBB1 and TUBB2, not one gene with synonym TUB2. Accession is valid; alias wording is not. |
| current-canonical-search-TUBA1 | https://rest.uniprot.org/uniprotkb/search?query=%28organism_id%3A3055%29+AND+%28reviewed%3Atrue%29+AND+%28gene%3ATUBA1%29&amp;format=json&amp;size=500; complete results array for reviewed:true AND organism_id:3055 AND gene:TUBA1, size500; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/canonical-search-TUBA1.raw | supports | One reviewed result for canonical gene TUBA1: P09204. This confirms current canonical-query uniqueness; historical-symbol queries TUA1/TUB1 return zero and are not used as proof of wrong accession. |
| current-canonical-search-TUBB1 | https://rest.uniprot.org/uniprotkb/search?query=%28organism_id%3A3055%29+AND+%28reviewed%3Atrue%29+AND+%28gene%3ATUBB1%29&amp;format=json&amp;size=500; complete results array for reviewed:true AND organism_id:3055 AND gene:TUBB1, size500; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/canonical-search-TUBB1.raw | supports | One reviewed result for canonical gene TUBB1: P04690. This confirms current canonical-query uniqueness; historical-symbol queries TUA1/TUB1 return zero and are not used as proof of wrong accession. |
| current-canonical-search-TUBB2 | https://rest.uniprot.org/uniprotkb/search?query=%28organism_id%3A3055%29+AND+%28reviewed%3Atrue%29+AND+%28gene%3ATUBB2%29&amp;format=json&amp;size=500; complete results array for reviewed:true AND organism_id:3055 AND gene:TUBB2, size500; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/canonical-search-TUBB2.raw | supports | One reviewed result for canonical gene TUBB2: P04690. This confirms current canonical-query uniqueness; historical-symbol queries TUA1/TUB1 return zero and are not used as proof of wrong accession. |
| current-microtubule-agent-kato2020-full | https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0242694; Abstract; Introduction first two paragraphs; Methods insertional mutants; Results Isolation of tubulin-gene disruptants, Figures1-4 captions; Discussion first paragraph; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/microtubule-agent-kato2020-full.raw | supports | Kato2020 directly treats tua1/tua2 and tub1/tub2 as distinct gene pairs encoding identical proteins, and creates gene-specific disruptants. This refutes TUB2 as merely a synonym of TUB1; the native accession can still represent the shared product. Most single-gene disruptants retain tubulin level and flagellar regeneration, so generic constituent essentiality must not imply every paralog is essential. |
| current-microtubule-agent-interpro-alpha | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002452/; metadata.accession/type/name/description; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/microtubule-agent-interpro-alpha.raw | supports | IPR002452 represents alpha tubulin, not the combined alpha/beta constituent class. |
| current-microtubule-agent-interpro-beta | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002453/; metadata.accession/type/name/description; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/microtubule-agent-interpro-beta.raw | supports | IPR002453 represents beta tubulin, not the combined alpha/beta constituent class. |
| current-microtubule-agent-interpro-tubulin | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000217/; metadata.accession/type/name/description; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/microtubule-agent-interpro-tubulin.raw | supports | IPR000217 includes other eukaryotic tubulin classes and bacterial homologues; no exact combined alpha/beta class substitution is justified. |
| current-connector-agent-ipr050145 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050145/; metadata.accession/type/name/description; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/connector-agent-ipr050145.raw | supports | IPR050145 Centrin/CML-like explicitly includes obelin and plant CML proteins, broader than connector centrins. |
| current-connector-agent-ipr050230 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050230/; metadata.accession/type/name/description; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/connector-agent-ipr050230.raw | supports | IPR050230 is broad Calmodulin/Myosin light chain/Troponin C-like family, not an exact connector-centrin class. |
| current-microtubule-agent-schwartz-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC3439489.1/PMC3439489.1.xml; Sections s2a,s2b,s2e,s5a,s5d,s5e; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/microtubule-agent-schwartz-jats.raw | supports | WBC6 Giardia disc scaffold is a spiral microtubule array with dorsal microribbons;13protofilaments and4nm/8nm repeats. Detergent-isolated discs flatten;2.8nm resolution cannot distinguish alpha/beta or every accessory density. Supports array example and scaffold, not exact isoform or measured attachment force. |
| current-microtubule-agent-nomura-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC6398456.1/PMC6398456.1.xml; Sections s2a,s2c,s2d,s4a; Figures2-5 captions; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/microtubule-agent-nomura-jats.raw | supports | Chrysochromulina sp.NIES4122 extended haptonema has seven microtubules; fixed thin-section and demembranated negative-stain observations support specialized array context. Taxol20uM60min inhibits induced coiling. No identified complete MAP inventory or purified contraction mechanism. |
| current-microtubule-agent-pilhofer-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC3232192.1/PMC3232192.1.xml; Section s2 Results and Discussion all direct paragraphs; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/microtubule-agent-pilhofer-jats.raw | supports | BtubAB forms bacterial tubes in Prosthecobacter; native cryotomography/model analysis supports five-protofilament interpretation. Evolution and seam interpretation remain proposals. Different tubulin system from canonical eukaryotic alpha/beta microtubule. |
| current-microtubule-agent-erb-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC4244570.1/PMC4244570.1.xml; Abstract, s2-1 and s2-2 opening assay context, complete s2-5 infection spindle subsection and captions; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/microtubule-agent-erb-jats.raw | supports | Phage201phi2-1 PhuZ in P.chlororaphis forms a dynamic bipolar spindle-like system during infection; purified dynamics and GFP live-cell observations do not make it a canonical eukaryotic alpha/beta microtubule. Anchor identity remains unresolved. |
| current-microtubule-agent-duggin-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC4369195.1/PMC4369195.1.xml; Main-body direct paragraphs: CetZ structures, deletions, rod development, localization, dynamics and concluding interpretation; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/microtubule-agent-duggin-jats.raw | supports | H.volcaniiH98 CetZ1 is a cell-shape/motility system distinct from FtsZ division; CetZ2 crystal protofilaments/sheets and CetZ1 patches/filaments do not establish canonical alpha/beta tubes. GFP partial function and mutant hyperstability are explicit. |
| current-microtubule-agent-dutcher-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC4888484.1/PMC4888484.1.xml; Abstract and Sec2 Basal body structure; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/microtubule-agent-dutcher-jats.raw | context_only | Secondary review supplies basal-body triplet and transition-zone doublet context and specialized tubulin classes; no primary experiment is claimed and these associated proteins are not imported as universal microtubule components. |
| current-microtubule-agent-mcquillen-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC8610174.1/PMC8610174.1.xml; Abstract and S2 Overview of FtsZ and the Divisome; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/microtubule-agent-mcquillen-jats.raw | context_only | Secondary review supplies FtsZ cytokinetic polymer-class context; no claim of canonical eukaryotic microtubule identity or independently audited primary mechanism. |
| current-microtubule-agent-epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=100&amp;query=DOI%3A%2210.1126/science.1128618%22%20OR%20DOI%3A%2210.1371/journal.pone.0043783%22%20OR%20DOI%3A%2210.1186/s13630-016-0039-z%22%20OR%20DOI%3A%2210.1242/bio.036590%22%20OR%20DOI%3A%2210.1371/journal.pbio.1001213%22%20OR%20DOI%3A%2210.1073/pnas.1705062114%22%20OR%20DOI%3A%2210.1101/gad.1546107%22%20OR%20DOI%3A%2210.7554/eLife.03197%22%20OR%20DOI%3A%2210.1038/nature13983%22%20OR%20DOI%3A%2210.1146/annurev-biophys-121219-081703%22; All10 exact DOI metadata; full primary abstracts for Deng2017 and Larsen2007; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/microtubule-agent-epmc.raw | supports | All cited identities match. Fresh primary abstracts support four-stranded BtubAB mini-microtubules with in-vitro dynamics, and TubZ treadmilling/plasmid maintenance. Current legacy full-text fetches returned challenge pages, so their detailed historical body readings are not independently freshly reproduced. |
| current-nuclear-agent-epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1146/annurev.cellbio.20.022003.114106%22; Exact DOI result PMID15473833; full abstract and publication metadata; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/nuclear-agent-epmc.raw | supports | Jaspersen/Winey2004 citation identity matches and is explicitly a review, not a primary experiment. Abstract is consistent with bounded SPB microtubule-organizing context. |
| current-connector-agent-1985-pdf | https://pmc-oa-opendata.s3.amazonaws.com/PMC2113967.1/PMC2113967.1.pdf; Abstract; printed1904-1906 isolation/immunoreactivity/calcium paragraphs; printed1908-1911 identity, artifact caveats and systemII boundary; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/connector-agent-1985-pdf.raw | supports | Primary text supports fibrous nucleus-basal-body connection, acidic20kDa antibody-reactive protein and calcium shortening. Whole-cell staining limits preparation artifact concern. Approximately6nm filaments were tentatively assigned; no definitive diameter or universal essentiality inferred. Figure pixels not fully audited. |
| current-connector-agent-1987-pdf | https://pmc-oa-opendata.s3.amazonaws.com/PMC2114663.1/PMC2114663.1.pdf; All seven pages extracted text; printed1799 gamete Methods,1800 reactivation,1801-1804 results,Figure2 andTableI; Figure2 on PDFpage4 independently visually inspected; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/connector-agent-1987-pdf.raw | supports | 137c derivativeNOmt+ gametes: living deflagellation snapshots and extracted NP40 models support root contraction/anterior nucleus and EGTA reextension. Refractory models need ATP potentiation before renewed calcium response; ATP alone is not contraction. Phosphorylation is proposed, not established. Figure2 has9panels in3rows and5umbar as record describes. |
| current-connector-agent-1987-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC2114663.1/PMC2114663.1.xml; front/article-meta/permissions/license and explicit license_ref/license-p; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/connector-agent-1987-jats.raw | context_only | Native JATS explicitly grants CC BY-NC-SA4.0; validates record link-only Figure2 licensing. Text is PDF-preformat; scientific experiment support is independently tied to the PDF row. |
| current-connector-agent-1992-pdf | https://pmc-oa-opendata.s3.amazonaws.com/PMC2289752.1/PMC2289752.1.pdf; Abstract; printed1617 class1/class2 and immunolocalization;1618-1619 contracted extracted models;1622-1623 Discussion andTableII; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/connector-agent-1992-pdf.raw | supports | vfl2E101K and intragenic revertants link tested centrin to NBBC/striated-fiber/transition-region assembly. Class2Met/Ile restore apparently normal NBBC despite abnormal distal fibers. Segregation claim is authors inference by exclusion, not selective NBBC ablation; record preserves this limitation. |
| current-connector-agent-2005-legacy | https://pmc.ncbi.nlm.nih.gov/articles/PMC1168961/?report=xml; Methods strain/cytoskeleton preparation; Results paragraphs on NBBC and continuity; Discussion Sfi1/CBP1.1 scaffold proposal; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/connector-agent-2005-legacy.raw | supports | cw15+SAG83.81 isolated interphase cytoskeleton immunogold supports broader scaffold association. NBBC continuity with neighboring fibers cannot all be directly proven; Sfi1/CBP1.1 is an imported candidate hypothesis, not established Chlamydomonas NBBC constituent. |
| current-connector-agent-epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=100&amp;query=DOI%3A%2210.1083/jcb.101.5.1903%22%20OR%20DOI%3A%2210.1083/jcb.105.4.1799%22%20OR%20DOI%3A%2210.1002/cm.970140409%22%20OR%20DOI%3A%2210.1083/jcb.119.6.1613%22%20OR%20DOI%3A%2210.1007/s00709-003-0016-4%22%20OR%20DOI%3A%2210.1128/EC.4.7.1253-1263.2005%22; Exact six DOI results and all returned primary abstracts, especially1989 and2003; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/connector-agent-epmc.raw | supports | 1989 directly tests preserved post-deflagellation gene induction in connector-defective vfl2.2003 compares Synura petersenii and Mallomonas species; strong20-22kDa immunoblot and mitotic description are Synura-specific. Current Springer fetch is challenge content, so fresh2003 support is primary-abstract-bounded;1989 full text remains unread. |
| current-connector-agent-uniprot | https://rest.uniprot.org/uniprotkb/P05434.json; primaryAccession, entryType, recommended name, organism, absent genes field, sequence, sequence-source references; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/connector-agent-uniprot.raw | supports | P05434 is reviewed Caltractin/Centrin,taxon3055,169aa, no primary gene supplied. Species-level example and references fit tested centrin; does not prove cross-taxon connector-specific paralog or full inventory. |
| current-micro-nicastro-browser | https://www.researchgate.net/publication/6871150_The_Molecular_Architecture_of_Axonemes_Revealed_by_Cryoelectron_Tomography; Initial abstract/body lines112-136 and Figure1 captions lines40-43; shared captured browser response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/nicastro-jaspersen-browser.json; SHA256 is entire JSON receipt, not native publisher bytes | supports | Author-uploaded primary manuscript supports Chlamydomonas/sea-urchin axoneme arrays, with Chlamydomonas panelsF-H. No exact isoform assignment or independent PDF/movies/pixels audit. |
| current-micro-jaspersen-browser | https://www.researchgate.net/publication/8241691_THE_BUDDING_YEAST_SPINDLE_POLE_BODY_Structure_Duplication_and_Function; Fresh browser extraction manuscript pp24-26 Microtubule Nucleation and Microtubule-Dependent Functions, lines978-1073; earlier current-session paper2004-browser.json p5 read independently; shared captured browser response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/nicastro-jaspersen-browser.json; SHA256 is entire JSON receipt, not native publisher bytes | supports | Secondary author manuscript explicitly locates nuclear microtubule origins at inner plaque and describes alpha/beta arrays extending into nucleoplasm. Supports bounded yeast example without universal site, composition or strain claims. |
| current-record-microtubule | data/structures/cytoskeleton/microtubule.yaml; Entire current record; original bundle compared to this input | context_only | Current record independently read at PR head9d7ce4c503b68329385b8c73999c721c00deef34; stale delta consists of two reviewed UniProt examples and curation history. |
| current-record-nuclear_microtubule | data/structures/cytoskeleton/nuclear_microtubule.yaml; Entire current record; original bundle compared to this input | context_only | Current record independently read at PR head9d7ce4c503b68329385b8c73999c721c00deef34; bytes match original frozen review input. |
| current-record-nucleus_basal_body_connector | data/structures/cytoskeleton/nucleus_basal_body_connector.yaml; Entire current record; original bundle compared to this input | context_only | Current record independently read at PR head9d7ce4c503b68329385b8c73999c721c00deef34; bytes match original frozen review input. |
| ipr016491 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016491/; Native accession/name/type/hierarchy and generic family description | supports | IPR016491 is the Septin family; class grounding does not require complete mitotic assembly composition. |
| mitotic-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005940,GO:0031105,GO:0032151,GO:0032152; Four complete active GO terms and direct parent child list | supports | GO0032151 is the mitotic heterooligomer; parentGO0031105, meiotic siblingGO0032152, ringGO0005940 distinct. |
| sin-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0071958,GO:0160065,GO:0160066,GO:0160067,GO:1990334; Five complete GO terms, synonyms and parent child lists | supports | GO0160067 exact identity/synonym and parentGO0160065 confirmed; active Spg1 at newSPB during anaphase; association is not asserted parthood. |
| versele | https://pmc.ncbi.nlm.nih.gov/articles/PMC1761124/?pdf=render; Secondary review S2,S3,S4 and Table1 context | supports | Review distinguishes mitotic from meiotic cohorts, oligomers from higher polymers and species-specific paralogs. No primary experiment repetition or universal copy-count inference. |
| johnson | https://pmc.ncbi.nlm.nih.gov/articles/PMC3025462/?pdf=render; PMC3025462 Introduction; Resultssec3,5–9 with captions; Discussionsec11–14/Fig8caption; Methodssec16,17,20,22 | supports | Introduction synthesizes prior pole-age asymmetry work. Actual experiments examine Dma1-dependent Sid4 ubiquitination, Plo1 localization and Byr4 phosphorylation/localization during defined arrests. Fig8 is a model, not whole-SIN reconstitution. |
| sin-species | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4896; taxId,scientificName,rank | supports | NCBITaxon4896 is Schizosaccharomyces pombe, species rank. |
| sin-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1038/emboj.2010.317&amp;format=json&amp;resultType=core; Exact DOI result title,authors,PMID,PMCID and abstract | supports | DOI10.1038/emboj.2010.317 is Johnson/Gould2011, PMID21131906, PMC3025462. |
| adapter-catalogue | https://imodulondb.org/api/datasets; Entire official public organism/dataset catalogue | supports | Complete official catalogue contains20 organisms and28 datasets, all bacterial/archaeal. No dataset covers the target yeast or protist examples (Saccharomyces, Schizosaccharomyces, Chlamydomonas, Giardia, Mallomonas or Synura). This establishes coverage-based non-applicability, not absence of the structures or genes. |
| check-qc | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/qc.log; Actual stdout/stderr and command receipt | supports | Full native QC returned exit0. |
| check-labels | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/labels.log; Actual stdout/stderr and command receipt | supports | Native label correspondence returned exit0. |
| check-trait-links | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/trait-links.log; Actual stdout/stderr and command receipt | supports | TraitMech references returned exit0. |
| check-vendored | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/vendored.log; Actual stdout/stderr and command receipt | supports | Pinned governed files returned exit0. |
| check-curies | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/curies.log; Actual stdout/stderr and command receipt | supports | Native identifier resolver returned exit0. |
| focused | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/focused-results.json; All20 actual schema/strict command outputs | supports | Ten target schema and ten target strict checks passed. |
| supplemental-pmid | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/pmid-chunks-receipt.json; Exact909-PMID set checked by unchanged native resolver in19 requests of at most50 | supports | All909 PMIDs returned OK. Original full-command report/cache remain unchanged;254 skipped identifiers are not claimed resolved. |

## Limits And Additional Notes

- The 2004 literature-review source is author-manuscript browser extraction, not verified publisher PDF bytes; its underlying primary literature was not exhaustively reread.
- Primary article text and claim-relevant figure legends were read; raw data, microscopy pixels, movies, model inputs and all supplements were not independently reanalyzed.
- IPR021750 returned HTTP429 at 2026-11-03T01:54:20.713748Z; no retry was made. The independently inspected response from00:45:04.724098Z is reused with that earlier timestamp, not represented as fresh successful access.
- Family/domain candidates and S288C complex entries do not establish complete plaque/SPB inventories, universal fungal/strain composition or whole-organelle stoichiometry.
- Current Deng/Larsen legacy HTML and Springer2003 fetches returned HTTP200 challenge pages, not literature. Fresh exact primary abstracts are the inspected ceiling for those routes; original historical full-body attestations are not represented as freshly reproduced.
- Nicastro and Jaspersen read through author-uploaded browser extraction; recorded hash is JSON browser receipt, not publisher PDF. No native HTTP status attestation. Jaspersen is secondary review.
- Connector1989/2003 full texts not read.1987Figure2 visually inspected; other source image panels/movies were not exhaustively audited.
- Historic TUA1/TUB1 exact native search strings yield no result while canonical TUBA1/TUBB1 searches verify one reviewed accession each. This is not proof of wrong accession; no separate mapping finding is made.
- Versele is secondary context. Underlying primary experiments were not independently reanalyzed.
- Johnson figure captions and relevant prose/methods were read; figure pixels, movies, supplements, strain table and raw data not independently evaluated.
- Earlier primary pole-age studies cited in JohnsonIntroduction were not all reread.
- No exhaustive modern component-family search for every SIN protein was conducted.
- Adapter CLI was not rerun because its OS-level unavailability was already established in canary; fresh source-native catalogue inspection supplies current applicability basis.
- Old observations and their command receipts remain historical and immutable; changed record inputs are reassessed here, not merely assigned replacement hashes.
- The adapter runner was not rerun after the canary established OS access failure. Current coverage is established by the freshly inspected source-native catalogue, not by a successful CLI call.
- Label correspondence has923 no-adapter skips. The native identifier command has909 HTTP414 transport failures and254 skipped identifiers; supplemental bounded requests resolve the909 PMIDs separately.
- Current scientific curation remains open; this observation neither edits records nor promotes native status.
- Final post-save trusted-base review-check and final-head/merge-group CI are publication gates performed after this immutable observation; no pending outcome is represented as passed.
- Original ten YAML/Markdown pairs remain byte-identical; main was merged normally without a force push. All changed tracked files in this PR are review bundles.
- One explicit issue-bearing cohort follows the repository persistence gate. No artificial issues or standalone clean bundles were created.
- Bundle fixes are tracked by issues2517(stale currentness),2518(omitted outer-plaque finding),2519(adapter applicability and draft count precision),2520(missing frozen context inputs). Scientific issues2499(reused),2515 and2516 stay open. Existing tooling issue2514 is reused with complete coverage disclosure.
- The source commit9d7ce4c503b68329385b8c73999c721c00deef34 is retained by additive tag review-base/pr2346-current-record-followup-20261103 so squash and branch deletion preserve native provenance validation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T021018Z-pr2346-current-record-followup
kind: batch
repository: CultureBotAI/CellStructureMech
title: 'PR 2346: current-input review of ten cytoskeletal records and adversarial
  follow-up'
started_at: '2026-11-03T01:50:31Z'
finished_at: '2026-11-03T02:10:18Z'
reviewer:
  identity: Codex root synthesis with three independent read-only adversarial reviewers
  kind: agent
  independence: self_review
  independence_basis: Root authors this follow-up. Three separate read-only agents
    independently inspected the original bundles, current records and primary/authority
    sources in five-record plaque, three-record microtubule/connector and two-record
    septin/SIN scopes. They did not author or modify repository files and will independently
    re-review the final head. This is not human scientific sign-off.
skill: .claude/skills/review-yaml-record/SKILL.md; explicit batch route in docs/record-review-profile.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'Current-input reassessment of the exact ten records in PR2346. Only microtubule
  changed since its frozen input: two reviewed protein examples and history were added.
  Three minor scientific curation findings remain: mitotic septin family grounding,
  outer mitotic plaque cell-cycle wording, and distinct beta-tubulin genes mislabeled
  as synonyms. Seven records have qualified supported assessments; three need curation.
  This issue-bearing batch repairs stale-currentness, the omitted phase-wording finding
  and adapter-coverage reasoning while preserving all original reviews and all scientific
  records.'
source:
  git_revision: 9d7ce4c503b68329385b8c73999c721c00deef34
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
  - path: data/structures/cytoskeleton/meiotic_outer_plaque.yaml
    sha256: 5482b05be175efef27e7e2acd73c2a7fb6cddbd69ebe7c430ed0adc3f858bfe9
    role: context
  - path: data/structures/cytoskeleton/meiotic_spindle_pole_body.yaml
    sha256: 2a99651652ccaa1b26dd8149e44976824366dbe2157a708fb1df0560323b8a75
    role: target
  - path: data/structures/cytoskeleton/microtubule.yaml
    sha256: 170483f42c69e1b91f2e11ace0483b30aa3beeba791119a77c644c99da1decc6
    role: target
  - path: data/structures/cytoskeleton/mitotic_septin_complex.yaml
    sha256: 99bf85740532379d8f9d88a2f07563cf9853a42e00a367fc5453d598ad308d1e
    role: target
  - path: data/structures/cytoskeleton/mitotic_spindle_pole_body.yaml
    sha256: 6f26eef2c9a8c923eb0c851b4d65b90a696322095208e731be170b6b0c9f0329
    role: target
  - path: data/structures/cytoskeleton/new_mitotic_spindle_pole_body.yaml
    sha256: 33ac955370a7476c7bb3f3fca4cfc9464120890e6a3e57fcb3b32d5e2504fb82
    role: target
  - path: data/structures/cytoskeleton/new_spindle_pole_body_sin_signaling_complex.yaml
    sha256: 84ade1d5217bae8fa401f096724d0892e76378469bec45c6ea25e961a0e28cae
    role: target
  - path: data/structures/cytoskeleton/nuclear_microtubule.yaml
    sha256: 09096977c74bdb36271d09b2a8aa1ac4c269ff8f3adbc854beae8b348f8aa252
    role: target
  - path: data/structures/cytoskeleton/nucleus_basal_body_connector.yaml
    sha256: 89e5e96440535f65493ee4b2928b835f415f79358200f32d877ec59487300f0d
    role: target
  - path: data/structures/cytoskeleton/outer_plaque_of_mitotic_spindle_pole_body.yaml
    sha256: 9197bc8f9b1fed339d56314bb682274576fa41bb94b26e2d09823e14a26ec226
    role: target
  - path: data/structures/cytoskeleton/outer_plaque_of_spindle_pole_body.yaml
    sha256: 2aa7db5e2c632a9934dda8fbc3c57a85d1742c6aa7322e769f6f162103f17142
    role: target
  - path: data/structures/cytoskeleton/spindle_pole_body.yaml
    sha256: 50885e021c246e17e29beb27f7dc98e37ee4d34878648fea4fd8b565bbb2fc78
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
  - path: reviews/structured/20261021T074511Z-meiotic-spindle-pole-body-audit/review.yaml
    sha256: b38455b795f651e445a087ea061447b4bddb9bd1ab1271b407da1e56e8b3028e
    role: context
  - path: reviews/structured/20261021T074637Z-mitotic-spindle-pole-body-audit/review.yaml
    sha256: 2e17a91197125460cc972e8c1176fb9b37c55e49cb23dd6b4b87381fbae8dc20
    role: context
  - path: reviews/structured/20261021T074637Z-new-mitotic-spindle-pole-body-audit/review.yaml
    sha256: 3be9788da2cdcf783a1cf436b11aa96e3ff2828e08f75b87ea67bb4eb81c6078
    role: context
  - path: reviews/structured/20261021T074638Z-mitotic-septin-complex-audit/review.yaml
    sha256: ea81871d561be4a8719b951fe9b6e0f74d2d244288c357a7675b013bf666c6aa
    role: context
  - path: reviews/structured/20261021T074638Z-new-spindle-pole-body-sin-signaling-complex-audit/review.yaml
    sha256: 25ed8eb25e51118e93d0bad5435ea18808112eb336e37fbba551322e6a6c0aef
    role: context
  - path: reviews/structured/20261021T074814Z-microtubule-audit/review.yaml
    sha256: f435bc1bccc74295c18f3e6aeec09568936815f806add79b4656ff1bce205667
    role: context
  - path: reviews/structured/20261021T074814Z-nuclear-microtubule-audit/review.yaml
    sha256: b959d65c7902e071560aa93b6f4c0f026cc0cc4204de151898105f411ae517fd
    role: context
  - path: reviews/structured/20261021T074815Z-outer-plaque-of-mitotic-spindle-pole-body-audit/review.yaml
    sha256: ae81ce5693237e3b5f6a86c0fc87baf6f9156c2fcd256455328050ca4df3357a
    role: context
  - path: reviews/structured/20261021T074815Z-outer-plaque-of-spindle-pole-body-audit/review.yaml
    sha256: 3facd8fe706ec1f1546b3c41470518e3cb5697b7bec67203e61f2a16ce529c20
    role: context
  - path: reviews/structured/20261021T075001Z-nucleus-basal-body-connector-audit/review.yaml
    sha256: 84f515365a2de98a9b8348bbeae4956eefbd2cc84e41ab9b17000f38252051cf
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
targets:
- target_id: GO:0035974
  path: data/structures/cytoskeleton/meiotic_spindle_pole_body.yaml
  label: meiotic spindle pole body
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/meiotic_spindle_pole_body.yaml
    role: maintained scientific record
- target_id: GO:0044732
  path: data/structures/cytoskeleton/mitotic_spindle_pole_body.yaml
  label: mitotic spindle pole body
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/mitotic_spindle_pole_body.yaml
    role: maintained scientific record
- target_id: GO:0071958
  path: data/structures/cytoskeleton/new_mitotic_spindle_pole_body.yaml
  label: new mitotic spindle pole body
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/new_mitotic_spindle_pole_body.yaml
    role: maintained scientific record
- target_id: GO:0032151
  path: data/structures/cytoskeleton/mitotic_septin_complex.yaml
  label: mitotic septin complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/mitotic_septin_complex.yaml
    role: maintained scientific record
- target_id: GO:0160067
  path: data/structures/cytoskeleton/new_spindle_pole_body_sin_signaling_complex.yaml
  label: new spindle pole body SIN signaling complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/new_spindle_pole_body_sin_signaling_complex.yaml
    role: maintained scientific record
- target_id: GO:0005874
  path: data/structures/cytoskeleton/microtubule.yaml
  label: microtubule
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/microtubule.yaml
    role: maintained scientific record
- target_id: GO:0005880
  path: data/structures/cytoskeleton/nuclear_microtubule.yaml
  label: nuclear microtubule
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/nuclear_microtubule.yaml
    role: maintained scientific record
- target_id: GO:0061499
  path: data/structures/cytoskeleton/outer_plaque_of_mitotic_spindle_pole_body.yaml
  label: outer plaque of mitotic spindle pole body
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/outer_plaque_of_mitotic_spindle_pole_body.yaml
    role: maintained scientific record
- target_id: GO:0005824
  path: data/structures/cytoskeleton/outer_plaque_of_spindle_pole_body.yaml
  label: outer plaque of spindle pole body
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/outer_plaque_of_spindle_pole_body.yaml
    role: maintained scientific record
- target_id: cellstructuremech:nucleus_basal_body_connector
  path: data/structures/cytoskeleton/nucleus_basal_body_connector.yaml
  label: nucleus-basal body connector
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/nucleus_basal_body_connector.yaml
    role: maintained scientific record
scope:
  description: Entire ten-record PR2346 cohort, assessed against current main 0ca1cafbc4841d27447043385df4b0ec0717820c.
    Exact original frozen hashes were compared with current maintained bytes. Current
    schema/source/claim scopes are reassessed; no scientific record, status or history
    mutation.
  selection: Exactly the ten record paths reviewed in original PR2346 head de122cf47c47daf8299d72b2be4a778003fef85b.
    Deterministic complete cohort, not a sample from the1022-record corpus.
  coverage: full
  population_size: 10
  reviewed_target_ids:
  - GO:0035974
  - GO:0044732
  - GO:0071958
  - GO:0032151
  - GO:0160067
  - GO:0005874
  - GO:0005880
  - GO:0061499
  - GO:0005824
  - cellstructuremech:nucleus_basal_body_connector
checks:
- check_id: qc
  name: Full native QC
  status: passed
  required: true
  target_ids:
  - GO:0035974
  - GO:0044732
  - GO:0071958
  - GO:0032151
  - GO:0160067
  - GO:0005874
  - GO:0005880
  - GO:0061499
  - GO:0005824
  - cellstructuremech:nucleus_basal_body_connector
  command: just qc
  exit_code: 0
  summary: Full QC passed:1054 tests passed,3 skipped; strict schema, history, generated
    products and other native gates passed.
  scope_note: Actual local execution at main-merge head9d7ce4c50; no later final-head
    CI or post-save check is claimed here.
  evidence_ids:
  - check-qc
- check_id: labels
  name: Native label correspondence
  status: passed
  required: true
  target_ids:
  - GO:0035974
  - GO:0044732
  - GO:0071958
  - GO:0032151
  - GO:0160067
  - GO:0005874
  - GO:0005880
  - GO:0061499
  - GO:0005824
  - cellstructuremech:nucleus_basal_body_connector
  command: just validate-products
  exit_code: 0
  summary: 4232 canonical,50 synonym and9 exception matches;923 SKIPPED_NO_ADAPTER
    pairs are not authority verification.
  scope_note: Actual local execution at main-merge head9d7ce4c50; no later final-head
    CI or post-save check is claimed here.
  evidence_ids:
  - check-labels
- check_id: trait-links
  name: TraitMech references
  status: passed
  required: true
  target_ids:
  - GO:0035974
  - GO:0044732
  - GO:0071958
  - GO:0032151
  - GO:0160067
  - GO:0005874
  - GO:0005880
  - GO:0061499
  - GO:0005824
  - cellstructuremech:nucleus_basal_body_connector
  command: just check-trait-links --check
  exit_code: 0
  summary: TraitMech references returned exit0; see exact receipt.
  scope_note: Actual local execution at main-merge head9d7ce4c50; no later final-head
    CI or post-save check is claimed here.
  evidence_ids:
  - check-trait-links
- check_id: vendored
  name: Pinned governed files
  status: passed
  required: true
  target_ids:
  - GO:0035974
  - GO:0044732
  - GO:0071958
  - GO:0032151
  - GO:0160067
  - GO:0005874
  - GO:0005880
  - GO:0061499
  - GO:0005824
  - cellstructuremech:nucleus_basal_body_connector
  command: just vendored-check
  exit_code: 0
  summary: Pinned governed files returned exit0; see exact receipt.
  scope_note: Actual local execution at main-merge head9d7ce4c50; no later final-head
    CI or post-save check is claimed here.
  evidence_ids:
  - check-vendored
- check_id: curies
  name: Native identifier resolver
  status: passed
  required: true
  target_ids:
  - GO:0035974
  - GO:0044732
  - GO:0071958
  - GO:0032151
  - GO:0160067
  - GO:0005874
  - GO:0005880
  - GO:0061499
  - GO:0005824
  - cellstructuremech:nucleus_basal_body_connector
  command: just check-curies-strict
  exit_code: 0
  summary: Exit0 with5264 OK,909 UNREACHABLE PMIDs (oversized GET HTTP414),254 SKIPPED.
    Existing issue2514 tracks batching and the misleading terminal universal-success
    text. Target authority evidence and supplemental PMID checks are separate.
  scope_note: Actual local execution at main-merge head9d7ce4c50; no later final-head
    CI or post-save check is claimed here.
  evidence_ids:
  - check-curies
- check_id: focused-0
  name: validate meiotic spindle pole body
  status: passed
  required: true
  target_ids:
  - GO:0035974
  command: just validate data/structures/cytoskeleton/meiotic_spindle_pole_body.yaml
  exit_code: 0
  summary: Documented focused command returned exit0.
  evidence_ids:
  - focused
- check_id: focused-1
  name: validate-strict meiotic spindle pole body
  status: passed
  required: true
  target_ids:
  - GO:0035974
  command: just validate-strict data/structures/cytoskeleton/meiotic_spindle_pole_body.yaml
  exit_code: 0
  summary: Documented focused command returned exit0.
  evidence_ids:
  - focused
- check_id: focused-2
  name: validate mitotic spindle pole body
  status: passed
  required: true
  target_ids:
  - GO:0044732
  command: just validate data/structures/cytoskeleton/mitotic_spindle_pole_body.yaml
  exit_code: 0
  summary: Documented focused command returned exit0.
  evidence_ids:
  - focused
- check_id: focused-3
  name: validate-strict mitotic spindle pole body
  status: passed
  required: true
  target_ids:
  - GO:0044732
  command: just validate-strict data/structures/cytoskeleton/mitotic_spindle_pole_body.yaml
  exit_code: 0
  summary: Documented focused command returned exit0.
  evidence_ids:
  - focused
- check_id: focused-4
  name: validate new mitotic spindle pole body
  status: passed
  required: true
  target_ids:
  - GO:0071958
  command: just validate data/structures/cytoskeleton/new_mitotic_spindle_pole_body.yaml
  exit_code: 0
  summary: Documented focused command returned exit0.
  evidence_ids:
  - focused
- check_id: focused-5
  name: validate-strict new mitotic spindle pole body
  status: passed
  required: true
  target_ids:
  - GO:0071958
  command: just validate-strict data/structures/cytoskeleton/new_mitotic_spindle_pole_body.yaml
  exit_code: 0
  summary: Documented focused command returned exit0.
  evidence_ids:
  - focused
- check_id: focused-6
  name: validate mitotic septin complex
  status: passed
  required: true
  target_ids:
  - GO:0032151
  command: just validate data/structures/cytoskeleton/mitotic_septin_complex.yaml
  exit_code: 0
  summary: Documented focused command returned exit0.
  evidence_ids:
  - focused
- check_id: focused-7
  name: validate-strict mitotic septin complex
  status: passed
  required: true
  target_ids:
  - GO:0032151
  command: just validate-strict data/structures/cytoskeleton/mitotic_septin_complex.yaml
  exit_code: 0
  summary: Documented focused command returned exit0.
  evidence_ids:
  - focused
- check_id: focused-8
  name: validate new spindle pole body SIN signaling complex
  status: passed
  required: true
  target_ids:
  - GO:0160067
  command: just validate data/structures/cytoskeleton/new_spindle_pole_body_sin_signaling_complex.yaml
  exit_code: 0
  summary: Documented focused command returned exit0.
  evidence_ids:
  - focused
- check_id: focused-9
  name: validate-strict new spindle pole body SIN signaling complex
  status: passed
  required: true
  target_ids:
  - GO:0160067
  command: just validate-strict data/structures/cytoskeleton/new_spindle_pole_body_sin_signaling_complex.yaml
  exit_code: 0
  summary: Documented focused command returned exit0.
  evidence_ids:
  - focused
- check_id: focused-10
  name: validate microtubule
  status: passed
  required: true
  target_ids:
  - GO:0005874
  command: just validate data/structures/cytoskeleton/microtubule.yaml
  exit_code: 0
  summary: Documented focused command returned exit0.
  evidence_ids:
  - focused
- check_id: focused-11
  name: validate-strict microtubule
  status: passed
  required: true
  target_ids:
  - GO:0005874
  command: just validate-strict data/structures/cytoskeleton/microtubule.yaml
  exit_code: 0
  summary: Documented focused command returned exit0.
  evidence_ids:
  - focused
- check_id: focused-12
  name: validate nuclear microtubule
  status: passed
  required: true
  target_ids:
  - GO:0005880
  command: just validate data/structures/cytoskeleton/nuclear_microtubule.yaml
  exit_code: 0
  summary: Documented focused command returned exit0.
  evidence_ids:
  - focused
- check_id: focused-13
  name: validate-strict nuclear microtubule
  status: passed
  required: true
  target_ids:
  - GO:0005880
  command: just validate-strict data/structures/cytoskeleton/nuclear_microtubule.yaml
  exit_code: 0
  summary: Documented focused command returned exit0.
  evidence_ids:
  - focused
- check_id: focused-14
  name: validate outer plaque of mitotic spindle pole body
  status: passed
  required: true
  target_ids:
  - GO:0061499
  command: just validate data/structures/cytoskeleton/outer_plaque_of_mitotic_spindle_pole_body.yaml
  exit_code: 0
  summary: Documented focused command returned exit0.
  evidence_ids:
  - focused
- check_id: focused-15
  name: validate-strict outer plaque of mitotic spindle pole body
  status: passed
  required: true
  target_ids:
  - GO:0061499
  command: just validate-strict data/structures/cytoskeleton/outer_plaque_of_mitotic_spindle_pole_body.yaml
  exit_code: 0
  summary: Documented focused command returned exit0.
  evidence_ids:
  - focused
- check_id: focused-16
  name: validate outer plaque of spindle pole body
  status: passed
  required: true
  target_ids:
  - GO:0005824
  command: just validate data/structures/cytoskeleton/outer_plaque_of_spindle_pole_body.yaml
  exit_code: 0
  summary: Documented focused command returned exit0.
  evidence_ids:
  - focused
- check_id: focused-17
  name: validate-strict outer plaque of spindle pole body
  status: passed
  required: true
  target_ids:
  - GO:0005824
  command: just validate-strict data/structures/cytoskeleton/outer_plaque_of_spindle_pole_body.yaml
  exit_code: 0
  summary: Documented focused command returned exit0.
  evidence_ids:
  - focused
- check_id: focused-18
  name: validate nucleus-basal body connector
  status: passed
  required: true
  target_ids:
  - cellstructuremech:nucleus_basal_body_connector
  command: just validate data/structures/cytoskeleton/nucleus_basal_body_connector.yaml
  exit_code: 0
  summary: Documented focused command returned exit0.
  evidence_ids:
  - focused
- check_id: focused-19
  name: validate-strict nucleus-basal body connector
  status: passed
  required: true
  target_ids:
  - cellstructuremech:nucleus_basal_body_connector
  command: just validate-strict data/structures/cytoskeleton/nucleus_basal_body_connector.yaml
  exit_code: 0
  summary: Documented focused command returned exit0.
  evidence_ids:
  - focused
- check_id: supplemental-pmid
  name: Supplemental bounded PMID authority checks
  status: passed
  required: true
  target_ids:
  - GO:0035974
  - GO:0044732
  - GO:0071958
  - GO:0032151
  - GO:0160067
  - GO:0005874
  - GO:0005880
  - GO:0061499
  - GO:0005824
  - cellstructuremech:nucleus_basal_body_connector
  command: .venv/bin/python /private/tmp/cellstructure-batches-2346-2397-20261103/check_pmid_chunks.py
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346
  exit_code: 0
  summary: 909/909 PMIDs OK in19 bounded requests. Native full-command coverage remains
    separately disclosed.
  evidence_ids:
  - supplemental-pmid
- check_id: structured-source-applicability
  name: Official iModulonDB catalogue applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0035974
  - GO:0044732
  - GO:0071958
  - GO:0032151
  - GO:0160067
  - GO:0005874
  - GO:0005880
  - GO:0061499
  - GO:0005824
  - cellstructuremech:nucleus_basal_body_connector
  summary: Official catalogue fallback contains20 organisms/28 datasets and no matching
    target yeast/protist. No new CLI runner execution is claimed; prior canary OS
    unavailability remains explicit.
  evidence_ids:
  - adapter-catalogue
- check_id: independent-scientific-review
  name: Independent claim-level source review
  status: passed
  required: true
  target_ids:
  - GO:0035974
  - GO:0044732
  - GO:0071958
  - GO:0032151
  - GO:0160067
  - GO:0005874
  - GO:0005880
  - GO:0061499
  - GO:0005824
  - cellstructuremech:nucleus_basal_body_connector
  summary: Three independent read-only reviewers covered all ten current records and
    their original bundles. This records source-review completion with explicit limitations
    and findings; final artifact/head acceptance is a separate publication gate.
  evidence_ids:
  - meiotic-spb-agent-go
  - meiotic-spb-agent-taxon
  - meiotic-spb-agent-knop2000-metadata
  - meiotic-spb-agent-bajgier2001-metadata
  - meiotic-spb-agent-mathieson2010-metadata
  - meiotic-spb-agent-knop2000
  - meiotic-spb-agent-bajgier2001
  - meiotic-spb-agent-mathieson2010-pmc
  - mitotic-spb-agent-go
  - mitotic-spb-agent-strain
  - mitotic-spb-agent-epmc
  - mitotic-spb-agent-viswanath2017
  - mitotic-spb-agent-candidate-proteins
  - mitotic-spb-agent-CPX-1198
  - mitotic-spb-agent-CPX-1420
  - mitotic-spb-agent-IPR002454
  - mitotic-spb-agent-IPR007259
  - mitotic-spb-agent-IPR021611
  - mitotic-spb-agent-IPR040593
  - new-mitotic-spb-agent-go
  - new-mitotic-spb-agent-taxon
  - new-mitotic-spb-agent-grallert2004-metadata
  - new-mitotic-spb-agent-grallert2004
  - mitotic-outer-plaque-agent-go
  - mitotic-outer-plaque-agent-epmc
  - outer-plaque-agent-go
  - spb-ipr021750-cached
  - spb-jaspersen2004-author-manuscript
  - current-microtubule-agent-go
  - current-nuclear-agent-go
  - current-connector-agent-go
  - current-microtubule-agent-taxon-chlamy
  - current-microtubule-agent-taxon-giardia
  - current-nuclear-agent-taxon
  - current-connector-agent-taxon-420600
  - current-connector-agent-taxon-52555
  - current-microtubule-agent-uniprot
  - current-new-uniprot-P09204
  - current-new-uniprot-P04690
  - current-canonical-search-TUBA1
  - current-canonical-search-TUBB1
  - current-canonical-search-TUBB2
  - current-microtubule-agent-kato2020-full
  - current-microtubule-agent-interpro-alpha
  - current-microtubule-agent-interpro-beta
  - current-microtubule-agent-interpro-tubulin
  - current-connector-agent-ipr050145
  - current-connector-agent-ipr050230
  - current-microtubule-agent-schwartz-jats
  - current-microtubule-agent-nomura-jats
  - current-microtubule-agent-pilhofer-jats
  - current-microtubule-agent-erb-jats
  - current-microtubule-agent-duggin-jats
  - current-microtubule-agent-dutcher-jats
  - current-microtubule-agent-mcquillen-jats
  - current-microtubule-agent-epmc
  - current-nuclear-agent-epmc
  - current-connector-agent-1985-pdf
  - current-connector-agent-1987-pdf
  - current-connector-agent-1987-jats
  - current-connector-agent-1992-pdf
  - current-connector-agent-2005-legacy
  - current-connector-agent-epmc
  - current-connector-agent-uniprot
  - current-micro-nicastro-browser
  - current-micro-jaspersen-browser
  - ipr016491
  - mitotic-go
  - sin-go
  - versele
  - johnson
  - sin-species
  - sin-metadata
  - adapter-catalogue
evidence:
- evidence_id: record-0
  kind: record_content
  reference: data/structures/cytoskeleton/meiotic_spindle_pole_body.yaml
  locator: Entire current maintained YAML; native inspect freezes exact bytes
  accessed_at: '2026-11-03T02:10:18Z'
  support: context_only
  summary: Current SHA256 2a99651652ccaa1b26dd8149e44976824366dbe2157a708fb1df0560323b8a75;
    original frozen SHA256 2a99651652ccaa1b26dd8149e44976824366dbe2157a708fb1df0560323b8a75.
    Record bytes remain identical to the original frozen input.
  snapshot_sha256: 2a99651652ccaa1b26dd8149e44976824366dbe2157a708fb1df0560323b8a75
- evidence_id: prior-0
  kind: prior_review
  reference: reviews/structured/20261021T074511Z-meiotic-spindle-pole-body-audit/review.yaml
  locator: Original immutable source, evidence, assessments, verdict, findings, actions
    and limitations
  accessed_at: '2026-11-03T02:10:18Z'
  support: context_only
  summary: Historical observation retained; its old checks and source access are not
    represented as current-head execution.
  snapshot_sha256: b38455b795f651e445a087ea061447b4bddb9bd1ab1271b407da1e56e8b3028e
- evidence_id: record-1
  kind: record_content
  reference: data/structures/cytoskeleton/mitotic_spindle_pole_body.yaml
  locator: Entire current maintained YAML; native inspect freezes exact bytes
  accessed_at: '2026-11-03T02:10:18Z'
  support: context_only
  summary: Current SHA256 6f26eef2c9a8c923eb0c851b4d65b90a696322095208e731be170b6b0c9f0329;
    original frozen SHA256 6f26eef2c9a8c923eb0c851b4d65b90a696322095208e731be170b6b0c9f0329.
    Record bytes remain identical to the original frozen input.
  snapshot_sha256: 6f26eef2c9a8c923eb0c851b4d65b90a696322095208e731be170b6b0c9f0329
- evidence_id: prior-1
  kind: prior_review
  reference: reviews/structured/20261021T074637Z-mitotic-spindle-pole-body-audit/review.yaml
  locator: Original immutable source, evidence, assessments, verdict, findings, actions
    and limitations
  accessed_at: '2026-11-03T02:10:18Z'
  support: context_only
  summary: Historical observation retained; its old checks and source access are not
    represented as current-head execution.
  snapshot_sha256: 2e17a91197125460cc972e8c1176fb9b37c55e49cb23dd6b4b87381fbae8dc20
- evidence_id: record-2
  kind: record_content
  reference: data/structures/cytoskeleton/new_mitotic_spindle_pole_body.yaml
  locator: Entire current maintained YAML; native inspect freezes exact bytes
  accessed_at: '2026-11-03T02:10:18Z'
  support: context_only
  summary: Current SHA256 33ac955370a7476c7bb3f3fca4cfc9464120890e6a3e57fcb3b32d5e2504fb82;
    original frozen SHA256 33ac955370a7476c7bb3f3fca4cfc9464120890e6a3e57fcb3b32d5e2504fb82.
    Record bytes remain identical to the original frozen input.
  snapshot_sha256: 33ac955370a7476c7bb3f3fca4cfc9464120890e6a3e57fcb3b32d5e2504fb82
- evidence_id: prior-2
  kind: prior_review
  reference: reviews/structured/20261021T074637Z-new-mitotic-spindle-pole-body-audit/review.yaml
  locator: Original immutable source, evidence, assessments, verdict, findings, actions
    and limitations
  accessed_at: '2026-11-03T02:10:18Z'
  support: context_only
  summary: Historical observation retained; its old checks and source access are not
    represented as current-head execution.
  snapshot_sha256: 3be9788da2cdcf783a1cf436b11aa96e3ff2828e08f75b87ea67bb4eb81c6078
- evidence_id: record-3
  kind: record_content
  reference: data/structures/cytoskeleton/mitotic_septin_complex.yaml
  locator: Entire current maintained YAML; native inspect freezes exact bytes
  accessed_at: '2026-11-03T02:10:18Z'
  support: context_only
  summary: Current SHA256 99bf85740532379d8f9d88a2f07563cf9853a42e00a367fc5453d598ad308d1e;
    original frozen SHA256 99bf85740532379d8f9d88a2f07563cf9853a42e00a367fc5453d598ad308d1e.
    Record bytes remain identical to the original frozen input.
  snapshot_sha256: 99bf85740532379d8f9d88a2f07563cf9853a42e00a367fc5453d598ad308d1e
- evidence_id: prior-3
  kind: prior_review
  reference: reviews/structured/20261021T074638Z-mitotic-septin-complex-audit/review.yaml
  locator: Original immutable source, evidence, assessments, verdict, findings, actions
    and limitations
  accessed_at: '2026-11-03T02:10:18Z'
  support: context_only
  summary: Historical observation retained; its old checks and source access are not
    represented as current-head execution.
  snapshot_sha256: ea81871d561be4a8719b951fe9b6e0f74d2d244288c357a7675b013bf666c6aa
- evidence_id: record-4
  kind: record_content
  reference: data/structures/cytoskeleton/new_spindle_pole_body_sin_signaling_complex.yaml
  locator: Entire current maintained YAML; native inspect freezes exact bytes
  accessed_at: '2026-11-03T02:10:18Z'
  support: context_only
  summary: Current SHA256 84ade1d5217bae8fa401f096724d0892e76378469bec45c6ea25e961a0e28cae;
    original frozen SHA256 84ade1d5217bae8fa401f096724d0892e76378469bec45c6ea25e961a0e28cae.
    Record bytes remain identical to the original frozen input.
  snapshot_sha256: 84ade1d5217bae8fa401f096724d0892e76378469bec45c6ea25e961a0e28cae
- evidence_id: prior-4
  kind: prior_review
  reference: reviews/structured/20261021T074638Z-new-spindle-pole-body-sin-signaling-complex-audit/review.yaml
  locator: Original immutable source, evidence, assessments, verdict, findings, actions
    and limitations
  accessed_at: '2026-11-03T02:10:18Z'
  support: context_only
  summary: Historical observation retained; its old checks and source access are not
    represented as current-head execution.
  snapshot_sha256: 25ed8eb25e51118e93d0bad5435ea18808112eb336e37fbba551322e6a6c0aef
- evidence_id: record-5
  kind: record_content
  reference: data/structures/cytoskeleton/microtubule.yaml
  locator: Entire current maintained YAML; native inspect freezes exact bytes
  accessed_at: '2026-11-03T02:10:18Z'
  support: context_only
  summary: Current SHA256 170483f42c69e1b91f2e11ace0483b30aa3beeba791119a77c644c99da1decc6;
    original frozen SHA256 06773fdcef54b61e7ed2a8a4c1066dfed8ba71dce8050eb39a879fab702b7498.
    Changed input reassessed against current primary and authority sources.
  snapshot_sha256: 170483f42c69e1b91f2e11ace0483b30aa3beeba791119a77c644c99da1decc6
- evidence_id: prior-5
  kind: prior_review
  reference: reviews/structured/20261021T074814Z-microtubule-audit/review.yaml
  locator: Original immutable source, evidence, assessments, verdict, findings, actions
    and limitations
  accessed_at: '2026-11-03T02:10:18Z'
  support: context_only
  summary: Historical observation retained; its old checks and source access are not
    represented as current-head execution.
  snapshot_sha256: f435bc1bccc74295c18f3e6aeec09568936815f806add79b4656ff1bce205667
- evidence_id: record-6
  kind: record_content
  reference: data/structures/cytoskeleton/nuclear_microtubule.yaml
  locator: Entire current maintained YAML; native inspect freezes exact bytes
  accessed_at: '2026-11-03T02:10:18Z'
  support: context_only
  summary: Current SHA256 09096977c74bdb36271d09b2a8aa1ac4c269ff8f3adbc854beae8b348f8aa252;
    original frozen SHA256 09096977c74bdb36271d09b2a8aa1ac4c269ff8f3adbc854beae8b348f8aa252.
    Record bytes remain identical to the original frozen input.
  snapshot_sha256: 09096977c74bdb36271d09b2a8aa1ac4c269ff8f3adbc854beae8b348f8aa252
- evidence_id: prior-6
  kind: prior_review
  reference: reviews/structured/20261021T074814Z-nuclear-microtubule-audit/review.yaml
  locator: Original immutable source, evidence, assessments, verdict, findings, actions
    and limitations
  accessed_at: '2026-11-03T02:10:18Z'
  support: context_only
  summary: Historical observation retained; its old checks and source access are not
    represented as current-head execution.
  snapshot_sha256: b959d65c7902e071560aa93b6f4c0f026cc0cc4204de151898105f411ae517fd
- evidence_id: record-7
  kind: record_content
  reference: data/structures/cytoskeleton/outer_plaque_of_mitotic_spindle_pole_body.yaml
  locator: Entire current maintained YAML; native inspect freezes exact bytes
  accessed_at: '2026-11-03T02:10:18Z'
  support: context_only
  summary: Current SHA256 9197bc8f9b1fed339d56314bb682274576fa41bb94b26e2d09823e14a26ec226;
    original frozen SHA256 9197bc8f9b1fed339d56314bb682274576fa41bb94b26e2d09823e14a26ec226.
    Record bytes remain identical to the original frozen input.
  snapshot_sha256: 9197bc8f9b1fed339d56314bb682274576fa41bb94b26e2d09823e14a26ec226
- evidence_id: prior-7
  kind: prior_review
  reference: reviews/structured/20261021T074815Z-outer-plaque-of-mitotic-spindle-pole-body-audit/review.yaml
  locator: Original immutable source, evidence, assessments, verdict, findings, actions
    and limitations
  accessed_at: '2026-11-03T02:10:18Z'
  support: context_only
  summary: Historical observation retained; its old checks and source access are not
    represented as current-head execution.
  snapshot_sha256: ae81ce5693237e3b5f6a86c0fc87baf6f9156c2fcd256455328050ca4df3357a
- evidence_id: record-8
  kind: record_content
  reference: data/structures/cytoskeleton/outer_plaque_of_spindle_pole_body.yaml
  locator: Entire current maintained YAML; native inspect freezes exact bytes
  accessed_at: '2026-11-03T02:10:18Z'
  support: context_only
  summary: Current SHA256 2aa7db5e2c632a9934dda8fbc3c57a85d1742c6aa7322e769f6f162103f17142;
    original frozen SHA256 2aa7db5e2c632a9934dda8fbc3c57a85d1742c6aa7322e769f6f162103f17142.
    Record bytes remain identical to the original frozen input.
  snapshot_sha256: 2aa7db5e2c632a9934dda8fbc3c57a85d1742c6aa7322e769f6f162103f17142
- evidence_id: prior-8
  kind: prior_review
  reference: reviews/structured/20261021T074815Z-outer-plaque-of-spindle-pole-body-audit/review.yaml
  locator: Original immutable source, evidence, assessments, verdict, findings, actions
    and limitations
  accessed_at: '2026-11-03T02:10:18Z'
  support: context_only
  summary: Historical observation retained; its old checks and source access are not
    represented as current-head execution.
  snapshot_sha256: 3facd8fe706ec1f1546b3c41470518e3cb5697b7bec67203e61f2a16ce529c20
- evidence_id: record-9
  kind: record_content
  reference: data/structures/cytoskeleton/nucleus_basal_body_connector.yaml
  locator: Entire current maintained YAML; native inspect freezes exact bytes
  accessed_at: '2026-11-03T02:10:18Z'
  support: context_only
  summary: Current SHA256 89e5e96440535f65493ee4b2928b835f415f79358200f32d877ec59487300f0d;
    original frozen SHA256 89e5e96440535f65493ee4b2928b835f415f79358200f32d877ec59487300f0d.
    Record bytes remain identical to the original frozen input.
  snapshot_sha256: 89e5e96440535f65493ee4b2928b835f415f79358200f32d877ec59487300f0d
- evidence_id: prior-9
  kind: prior_review
  reference: reviews/structured/20261021T075001Z-nucleus-basal-body-connector-audit/review.yaml
  locator: Original immutable source, evidence, assessments, verdict, findings, actions
    and limitations
  accessed_at: '2026-11-03T02:10:18Z'
  support: context_only
  summary: Historical observation retained; its old checks and source access are not
    represented as current-head execution.
  snapshot_sha256: 84f515365a2de98a9b8348bbeae4956eefbd2cc84e41ab9b17000f38252051cf
- evidence_id: context-mop
  kind: record_content
  reference: data/structures/cytoskeleton/meiotic_outer_plaque.yaml
  locator: Entire maintained context YAML; native inspect freezes exact bytes
  accessed_at: '2026-11-03T02:10:18Z'
  support: context_only
  summary: 'Context only: whole meiotic outer-plaque boundary used in the meiotic
    spindle-pole assessment; not an additional reviewed target.'
  snapshot_sha256: 5482b05be175efef27e7e2acd73c2a7fb6cddbd69ebe7c430ed0adc3f858bfe9
- evidence_id: context-spb
  kind: record_content
  reference: data/structures/cytoskeleton/spindle_pole_body.yaml
  locator: Entire maintained context YAML; native inspect freezes exact bytes
  accessed_at: '2026-11-03T02:10:18Z'
  support: context_only
  summary: 'Context only: generic spindle-pole old/new role placeholders used in the
    new mitotic spindle-pole assessment; not an additional reviewed target.'
  snapshot_sha256: 50885e021c246e17e29beb27f7dc98e37ee4d34878648fea4fd8b565bbb2fc78
- evidence_id: meiotic-spb-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0035974%2CGO%3A0005816%2CGO%3A0031322%2CGO%3A0005628%2CGO%3A0005824%2CGO%3A0070057
  locator: All six returned definitions, active flags and parent child relations
  accessed_at: '2026-11-03T01:54:19.809870Z'
  support: supports
  summary: GO0035974 is the active meiotic SPB class under GO0005816. GO0031322 denotes
    the remodeling process; GO0005628 the prospore membrane; GO0005824 the outer plaque;
    GO0070057 the membrane attachment region. These are distinct entities.
  snapshot_sha256: cf3f57c87019a739f5f8ec0b5ee1fb0d71dd2e65fd7dd9c2a8a866da5eef70a6
- evidence_id: meiotic-spb-agent-taxon
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: taxId, scientificName, rank and lineage
  accessed_at: '2026-11-03T01:54:19.810185Z'
  support: supports
  summary: ENA confirms NCBITaxon4932 is Saccharomyces cerevisiae at species rank.
  snapshot_sha256: 38f43dd1593a1d47416228ae385464f30aeb8302c3aadb45b3588d03744bc814
- evidence_id: meiotic-spb-agent-knop2000-metadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1093/emboj/19.14.3657&format=json&resultType=core
  locator: 'Exact native EuropePMC result: DOI, PMID, title, authors, year, journal
    and availability fields'
  accessed_at: '2026-11-03T01:54:19.810258Z'
  support: supports
  summary: 'Knop and Strasser2000: DOI10.1093/emboj/19.14.3657, PMID10899120, PMC313968,
    exact title and authors.'
  snapshot_sha256: 7754934e18b9b1c64aca54f5657dfb2ca1b71c1ccbc90d93f538e41e513ef7e1
- evidence_id: meiotic-spb-agent-bajgier2001-metadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1091/mbc.12.6.1611&format=json&resultType=core
  locator: 'Exact native EuropePMC result: DOI, PMID, title, authors, year, journal
    and availability fields'
  accessed_at: '2026-11-03T01:54:19.810311Z'
  support: supports
  summary: 'Bajgier et al.2001: DOI10.1091/mbc.12.6.1611, PMID11408572, PMC37328,
    exact title and authors.'
  snapshot_sha256: 83c5dfbd96f2d5da321735d88518341c2c7f34d2dbf885fcb3ca8689efff53e6
- evidence_id: meiotic-spb-agent-mathieson2010-metadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1091/mbc.E10-07-0563&format=json&resultType=core
  locator: 'Exact native EuropePMC result: DOI, PMID, title, authors, year, journal
    and availability fields'
  accessed_at: '2026-11-03T01:54:19.810351Z'
  support: supports
  summary: 'Mathieson et al.2010: DOI10.1091/mbc.E10-07-0563, PMID20826607, exact
    title and authors. This metadata response omits its PMCID; the separately inspected
    native PMC2965686 article resolves full-text availability.'
  snapshot_sha256: 46b51685624d697a96eb3c4009d4fb59778d6b0a0fe8ed5a3dcc48cc0b5b1d6d
- evidence_id: meiotic-spb-agent-knop2000
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC313968/?pdf=render
  locator: Native PMC313968 HTML, Results sections sec4 and sec7-sec9; Discussion
    sec11-sec12; figure legends as text. Actual article body, not a PDF or challenge
    response.
  accessed_at: '2026-11-03T01:54:19.810387Z'
  support: supports
  summary: Budding-yeast primary experiments connect Mpc54/Mpc70-dependent meiotic
    outer-plaque assembly to normal prospore-membrane formation. Precursor targeting
    can persist without mature plaque assembly. The body distinguishes the whole SPB,
    its meiosis-II plaque and the growing membrane; fusion-machinery recruitment in
    Discussion is a model.
  snapshot_sha256: d1bbb5ffbbd3cc6314a0c47a13d49c54506224ad674cbfbf6e029df0cb743ce9
- evidence_id: meiotic-spb-agent-bajgier2001
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC37328/?pdf=render
  locator: Native PMC37328 HTML, Results sec8, sec11-sec12 and sec15; Discussion sec17;
    source-specific mutant and meiotic-stage context
  accessed_at: '2026-11-03T01:54:19.810419Z'
  support: supports
  summary: Spo21/Mpc70 contributes to meiosis-specific SPB modification. spo21 deletion
    disrupts plaque and membrane formation while meiotic divisions proceed. cnm67
    mutants can form untethered prospore membranes, limiting any claim that attachment
    to an intact SPB is universally indispensable.
  snapshot_sha256: 4304028cc5e77ef451daf3048b5a0961145c28a4a9b2b621140a63f0df7bbdcb
- evidence_id: meiotic-spb-agent-mathieson2010-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2965686/?pdf=render
  locator: Native PMC2965686 HTML, Results sec11 and sec14-sec18; Discussion sec20-sec23;
    article identity/DOI in header and text figure legends
  accessed_at: '2026-11-03T01:54:19.810447Z'
  support: supports
  summary: Selected Mpc54 point mutants retain meiotic-plaque composition and ultrastructure
    while impairing vesicle docking and recruitment of Sec4/exocyst factors. The FRET-based
    model places Mpc54/Spo21 N termini toward the membrane-facing surface; Ady4 is
    not a stable component, and Spo74 placement is unresolved. Proposed direct binding
    or exchange mechanisms remain interpretation.
  snapshot_sha256: 2c23e8184823196aea82ceff0ce31d522ee91876d148adb77ffdb0e69ef6ba82
- evidence_id: mitotic-spb-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0044732%2CGO%3A0005816%2CGO%3A0061496%2CGO%3A0061498
  locator: All four returned term definitions, active flags and parent-term child
    relations
  accessed_at: '2026-11-03T01:54:19.810476Z'
  support: supports
  summary: Native GO confirms active GO0044732 under GO0005816, with GO0061496 half
    bridge and GO0061498 intermediate layer as mitotic-SPB substructures. The exact
    cell-cycle identity and graph relations are retained.
  snapshot_sha256: 72afd525fe6e749fbdc185149e7c36d970a1eb78461b32b5a7011f042c10014d
- evidence_id: mitotic-spb-agent-strain
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: taxId, scientificName and strain rank
  accessed_at: '2026-11-03T01:54:19.810504Z'
  support: context_only
  summary: Candidate sequence and complex entries concern S. cerevisiae S288C, NCBITaxon559292;
    the record declares the species-level example.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: mitotic-spb-agent-epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1146/annurev.cellbio.20.022003.114106%20OR%20DOI:10.1091/mbc.E17-06-0397&format=json&resultType=core
  locator: Both returned title, author, DOI, PMID, year and journal records
  accessed_at: '2026-11-03T01:54:20.458129Z'
  support: supports
  summary: Native metadata confirms Jaspersen and Winey2004 DOI10.1146/annurev.cellbio.20.022003.114106
    / PMID15473833 and corroborating Viswanath2017 DOI10.1091/mbc.E17-06-0397 / PMID28814505.
  snapshot_sha256: c03e88f13293f0e6a1c03a44e0c1aa2cf7fd5b4fc1ca21bcf036afe44015f741
- evidence_id: mitotic-spb-agent-viswanath2017
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5687031.1/PMC5687031.1.xml
  locator: Native JATS Introduction, Figure1 caption and relevant layer-localization
    Results/Methods
  accessed_at: '2026-11-03T01:54:20.500530Z'
  support: supports
  summary: The Introduction and Figure1 distinguish plaques, IL1/IL2 and nuclear/cytoplasmic
    nucleation sites. Its integrative model concerns the core rather than a complete
    reconstruction of every SPB constituent or duplication stage.
  snapshot_sha256: 004836a027b7fad21def4f6e9eebc94ec5f1e07679d123407a062241f6edb580
- evidence_id: mitotic-spb-agent-candidate-proteins
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/search?query=organism_id%3A559292%20AND%20%28gene_exact%3ASPC110%20OR%20gene_exact%3ATUB4%20OR%20gene_exact%3ASPC97%20OR%20gene_exact%3ASPC98%20OR%20gene_exact%3ACMD1%20OR%20gene_exact%3ASPC42%20OR%20gene_exact%3ACNM67%20OR%20gene_exact%3ASPC29%20OR%20gene_exact%3ANUD1%20OR%20gene_exact%3ASPC72%29&format=json&size=50
  locator: Relevant accession, reviewed status, name, genes, organism and native family/complex
    cross-references; optional candidates, not currently asserted examples
  accessed_at: '2026-11-03T01:54:20.570008Z'
  support: context_only
  summary: Reviewed S288C entries resolve Spc110 P32380, Spc97 P38863, Spc98 P53540,
    Tub4 P53378, Spc42 P36094, Cnm67 P53865, Spc29 P33419, Cmd1 P06787, Nud1 P32336
    and Spc72 P39723 as possible inventory material. The historical TRM2/NUD1 alias
    hit is not adopted as Nud1.
  snapshot_sha256: 773c38e1acac076de463c8ca995c32fde95d19a569acc8605352db6fa2134126
- evidence_id: mitotic-spb-agent-CPX-1198
  kind: database
  reference: https://www.ebi.ac.uk/intact/complex-ws/complex/CPX-1198
  locator: complexAc, name, species, participants, systematicName, properties and
    evidenceType
  accessed_at: '2026-11-03T01:54:20.669739Z'
  support: context_only
  summary: CPX1198 is the S288C gamma-tubulin small complex, with Spc97, Spc98 and
    two Tub4 subunits. It is an associated constituent complex, not an identifier
    or copy count for the whole SPB.
  snapshot_sha256: 6ad8b7dadcc915c04c213a08278cb1695d5f089b126afc38b2817a1aa56ca860
- evidence_id: mitotic-spb-agent-CPX-1420
  kind: database
  reference: https://www.ebi.ac.uk/intact/complex-ws/complex/CPX-1420
  locator: complexAc, name, species, participants, properties and GO0005823 cross-reference
  accessed_at: '2026-11-03T01:54:20.684236Z'
  support: context_only
  summary: CPX1420 is the Spc42/Cnm67 intermediate-layer2 complex. Its narrower complex
    scope and its central-plaque GO cross-reference must not be collapsed into the
    whole SPB or all intermediate layers.
  snapshot_sha256: f323ad1b133af230458960bed57f117f466742411055b27524379ba1f070cf29
- evidence_id: mitotic-spb-agent-IPR002454
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002454/
  locator: Native metadata accession, name, type, description and relevant member/hierarchy
    fields
  accessed_at: '2026-11-03T01:54:20.687457Z'
  support: context_only
  summary: Gamma tubulin is a family-level candidate for Tub4; source localization
    remains a separate claim.
  snapshot_sha256: 0cc07ff810e7acb2b8d24c24597c1bcabf177adb7e06ae6ddfabbb352fe0c668
- evidence_id: mitotic-spb-agent-IPR007259
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007259/
  locator: Native metadata accession, name, type, description and relevant member/hierarchy
    fields
  accessed_at: '2026-11-03T01:54:20.700609Z'
  support: context_only
  summary: Gamma-tubulin complex component protein is a broader family covering several
    GCP paralogues, not an exact individual Spc97/Spc98 identity.
  snapshot_sha256: 35abdb19f33d76f750dba5e51b97017071754f6c4def2ee06df37f41b461a389
- evidence_id: mitotic-spb-agent-IPR021611
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR021611/
  locator: Native metadata accession, name, type, description and relevant member/hierarchy
    fields
  accessed_at: '2026-11-03T01:54:20.706289Z'
  support: context_only
  summary: Spindle pole body component Spc42 is an exact named-family candidate.
  snapshot_sha256: aef911d443ea6bf22900e5ff3818f2d89f7d431d884a0cbb4c89b816e1175f34
- evidence_id: mitotic-spb-agent-IPR040593
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR040593/
  locator: Native metadata accession, name, type, description and relevant member/hierarchy
    fields
  accessed_at: '2026-11-03T01:54:20.721909Z'
  support: context_only
  summary: Spc110 C-terminal is a domain, not a whole-protein family; it cannot replace
    exact whole-component grounding.
  snapshot_sha256: ca33c3d4e076b45e58a018b0f87b2a26fa2b3292d0da42d0f16a82f76946092f
- evidence_id: new-mitotic-spb-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0071958%2CGO%3A0071957%2CGO%3A0044732
  locator: All three exact definitions, synonym scopes, active flags and parent-term
    child relations
  accessed_at: '2026-11-03T01:54:21.056194Z'
  support: supports
  summary: GO0071958 is the active new mitotic SPB class, with exact synonym new SPB
    and parent GO0044732. GO0071957 denotes the distinct old, pre-existing sibling.
  snapshot_sha256: 74dfb3320a1e69bc33faae1ffb5c0351bd84650b4e86f798ae5bf92f26d18f62
- evidence_id: new-mitotic-spb-agent-taxon
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4896
  locator: taxId, scientificName, rank and lineage
  accessed_at: '2026-11-03T01:54:21.116804Z'
  support: supports
  summary: ENA confirms Schizosaccharomyces pombe, NCBITaxon4896, at species rank.
  snapshot_sha256: cdb53b3f4ab5e6bb4476de3bf0db333ae647e307a9fa8f98108827f98fe7f4d3
- evidence_id: new-mitotic-spb-agent-grallert2004-metadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1101/gad.296204&format=json&resultType=core
  locator: 'Exact EuropePMC core result: citation identity and availability fields'
  accessed_at: '2026-11-03T01:54:21.293169Z'
  support: supports
  summary: Native metadata verifies Grallert et al.2004, DOI10.1101/gad.296204, PMID15132994,
    PMC406291, exact title, authors and journal.
  snapshot_sha256: c64265cb102adbe7e47950968adbe885a01ff480f027d6a79adbe472465f5488
- evidence_id: new-mitotic-spb-agent-grallert2004
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC406291/?pdf=render
  locator: 'Native PMC406291 HTML: Results sec4-sec5 and sec8-sec9; Discussion sec12-sec14;
    Methods sec19-sec20; Figure2, Figure5 and Figure8 legends as text'
  accessed_at: '2026-11-03T01:54:21.296478Z'
  support: supports
  summary: Primary S. pombe lineage labeling identifies active SIN on the new SPB
    in late anaphase B/G1. Fin1 instead always associates with the old SPB and with
    only half of new SPBs, depending on parental history. Early localization to both
    poles and age-dependent maturation delimit the signaling claim.
  snapshot_sha256: a08d20b46fed8f91fce808a7e0d94878cf8465fc842a280b5dddfacfe454105e
- evidence_id: mitotic-outer-plaque-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0061499%2CGO%3A0005824%2CGO%3A0044732%2CGO%3A0005881
  locator: All four returned definitions, active flags, synonyms where relevant and
    parent-term child relations
  accessed_at: '2026-11-03T01:54:21.314509Z'
  support: supports
  summary: GO0061499 is the active mitotic outer-plaque class, with is-a parent GO0005824
    and parthood in GO0044732. GO0005881 is the exact cytoplasmic-microtubule identity
    used in the graph.
  snapshot_sha256: e417bee78c2a7bc5fa54be56cebb82a642f00cd4441d64e7af28d92542755837
- evidence_id: mitotic-outer-plaque-agent-epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:10899120%20OR%20EXT_ID:15473833%20OR%20EXT_ID:28814505&format=json&resultType=core
  locator: All three returned title, author, DOI, PMID, year and journal records
  accessed_at: '2026-11-03T01:54:21.329292Z'
  support: supports
  summary: Native metadata verifies Jaspersen/Winey2004 DOI10.1146/annurev.cellbio.20.022003.114106
    / PMID15473833; Knop/Strasser2000 DOI10.1093/emboj/19.14.3657 / PMID10899120;
    and corroborating Viswanath2017 DOI10.1091/mbc.E17-06-0397 / PMID28814505.
  snapshot_sha256: d8451cfa735aa130f693d2d93444379ba1c0c27eae64b0f627a7648d332089ab
- evidence_id: outer-plaque-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0005824%2CGO%3A0005816%2CGO%3A0005881%2CGO%3A0070057
  locator: All four returned definitions, active flags, synonyms where relevant and
    parent-term child relations
  accessed_at: '2026-11-03T01:54:21.397177Z'
  support: supports
  summary: GO0005824 is the active cytoplasmic outer-plaque class with SPB parthood
    in GO0005816. GO0005881 is the exact cytoplasmic-microtubule identity, and GO0070057
    denotes a region of the prospore membrane rather than the plaque.
  snapshot_sha256: 22b29d52971eddcd363eab03ca0e05464816947bb49bbeac5f8678d9be2dff05
- evidence_id: spb-ipr021750-cached
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR021750/
  locator: Native InterPro metadata accession/name/type/description; reused independently
    inspected cached response; fresh request at 2026-11-03T01:54:20.713748Z returned
    HTTP 429 and was not retried
  accessed_at: '2026-11-03T00:45:04.724098Z'
  snapshot_sha256: f1fe20d4b8df21ce0b199b723bafd32ae02fce926221a25124470b9b93f07def
  support: context_only
  summary: The Septation initiation Sid4-like family includes Sid4, Ady3 and Cnm67,
    so it is broader than Cnm67 alone. No new successful retrieval is claimed.
- evidence_id: spb-jaspersen2004-author-manuscript
  kind: authority
  reference: https://www.researchgate.net/publication/8241691_THE_BUDDING_YEAST_SPINDLE_POLE_BODY_Structure_Duplication_and_Function
  locator: Public author-manuscript pp5-6, pp9-12 and meiotic-SPB pp12-13; browser-extracted
    text previously retrieved 2026-11-03T00:47:42Z to00:47:43Z and reread for these
    targets. Snapshot is serialized browser extraction, not native PDF bytes. Secondary
    literature-review context, corroborated by primary/GO sources.
  accessed_at: '2026-11-03T00:47:43Z'
  snapshot_sha256: e027d82955a859cb483e7800eefbf4424e4e27a4f4cc538fdfc7156388bb3f35
  support: supports
  summary: SPBs persist through the budding-yeast life cycle; G1 growth/duplication
    is within the mitotic cell cycle. The half bridge is a new-SPB assembly site.
    Outer-plaque Nud1/Spc72 and associated gamma-tubulin machinery face the cytoplasm;
    Cnm67 connects layers. Meiotic remodeling replaces Spc72 with Mpc54/Spo21. The
    source does not imply M-phase-only existence of the mitotic SPB or plaque.
- evidence_id: current-microtubule-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005874,GO:0099513,GO:0015630
  locator: results GO:0005874, GO:0099513, GO:0015630, active names, definitions,
    synonyms, explicit children relation fields; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/microtubule-agent-go.raw
  accessed_at: '2026-11-03T01:56:16.765872Z'
  snapshot_sha256: 79b21dcd052ab58971af90217665f9cee4a2cc63ec01c29ee158afc2e197df0f
  summary: Exact generic microtubule identity and both parent/parthood relationships
    verified; usual thirteen protofilaments and dimensions are GO wording, not new
    universal measurements.
  support: supports
- evidence_id: current-nuclear-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005880,GO:0005874,GO:0005634,GO:0005822,GO:0005881,GO:0005876
  locator: results GO:0005880, GO:0005874, GO:0005634, GO:0005822, GO:0005881, GO:0005876;
    definitions and children relation fields; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/nuclear-agent-go.raw
  accessed_at: '2026-11-03T01:56:18.291857Z'
  snapshot_sha256: b38984db5ca7c25b8713102f88d7a26e1ea0a9c1ca9c312095f1f425ad84401d
  summary: Exact location-defined nuclear microtubule and is_a microtubule / part_of
    nucleus relations verified. Inner plaque is nuclear; spindle membership and nuclear
    location can overlap.
  support: supports
- evidence_id: current-connector-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0035253,GO:0051647,GO:0120118,GO:0120269
  locator: results GO:0035253, GO:0051647, GO:0120118, GO:0120269; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/connector-agent-go.raw
  accessed_at: '2026-11-03T01:56:19.192203Z'
  snapshot_sha256: c80e002ece3cf027c45da5015ee8a76b88f69628dde761788719af66ed915f31
  summary: Rootlet broader-class placement and nucleus-localization function match.
    Kinetoplastid flagella connector and ciliary centrin arm are separate structures,
    not aliases of the algal NBBC.
  support: supports
- evidence_id: current-microtubule-agent-taxon-chlamy
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3055
  locator: taxId, scientificName, rank, otherNames; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/microtubule-agent-taxon-chlamy.raw
  accessed_at: '2026-11-03T01:56:16.766236Z'
  snapshot_sha256: e3861fe6706cefe2e079e15c0178a65e95efaad3890f548f25e721553eaa93a0
  summary: 'Species identity verified: 3055 Chlamydomonas reinhardtii. Taxonomy alone
    does not establish biological occurrence or tested strain.'
  support: supports
- evidence_id: current-microtubule-agent-taxon-giardia
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5741
  locator: taxId, scientificName, rank, otherNames; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/microtubule-agent-taxon-giardia.raw
  accessed_at: '2026-11-03T01:56:16.766296Z'
  snapshot_sha256: 1dcdc380972a71a0a24c80755d8bbacdcb0b6d9988bb5fb1e05ba43f50580dd3
  summary: 'Species identity verified: 5741 Giardia duodenalis. Taxonomy alone does
    not establish biological occurrence or tested strain.'
  support: supports
- evidence_id: current-nuclear-agent-taxon
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: taxId, scientificName, rank, otherNames; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/nuclear-agent-taxon.raw
  accessed_at: '2026-11-03T01:56:18.490842Z'
  snapshot_sha256: 38f43dd1593a1d47416228ae385464f30aeb8302c3aadb45b3588d03744bc814
  summary: 'Species identity verified: 4932 Saccharomyces cerevisiae. Taxonomy alone
    does not establish biological occurrence or tested strain.'
  support: supports
- evidence_id: current-connector-agent-taxon-420600
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/420600
  locator: taxId, scientificName, rank, otherNames; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/connector-agent-taxon-420600.raw
  accessed_at: '2026-11-03T01:56:19.781631Z'
  snapshot_sha256: 0413529cae9c8c88bf35f50dbfb27ad54979a0e5fc1da9a7b181dd6542674c07
  summary: 'Species identity verified: 420600 Mallomonas insignis. Taxonomy alone
    does not establish biological occurrence or tested strain.'
  support: supports
- evidence_id: current-connector-agent-taxon-52555
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/52555
  locator: taxId, scientificName, rank, otherNames; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/connector-agent-taxon-52555.raw
  accessed_at: '2026-11-03T01:56:20.001278Z'
  snapshot_sha256: 4047ec7ff222e3547d878e27d7b4945e79eaa3cfeebf5852902f63258e105f4d
  summary: 'Species identity verified: 52555 Synura petersenii. Taxonomy alone does
    not establish biological occurrence or tested strain.'
  support: supports
- evidence_id: current-microtubule-agent-uniprot
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q6SPP7.json
  locator: entryType, genes, organism, sequence, proteinDescription.flag; native bytes
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/microtubule-agent-uniprot.raw
  accessed_at: '2026-11-03T01:56:16.766151Z'
  snapshot_sha256: c871d3efc50e072fcc1f3bfdb20b419a68c14693c7ef3b245ffd2bdceeace77d
  summary: Q6SPP7 remains unreviewed TUA2 in taxon3055, a22-residue fragment. Supports
    accession identity only, not full-length or experimental-strain incorporation.
  support: supports
- evidence_id: current-new-uniprot-P09204
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P09204.json
  locator: entryType, proteinDescription.recommendedName, genes, organism, cross-references;
    native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/new-uniprot-P09204.raw
  accessed_at: '2026-11-03T01:56:20.037700Z'
  snapshot_sha256: 092609b91d1bea9759e0894997be7ee8f1b50238b2c235759b12eea9230d57cd
  summary: P09204 is reviewed Tubulin alpha-1 chain, taxon3055, primary gene TUBA1.
    Correct accession/status/name in new example; native entry does not itself list
    historical TUA1 as a synonym.
  support: supports
- evidence_id: current-new-uniprot-P04690
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P04690.json
  locator: entryType, proteinDescription.recommendedName, genes[0].geneName and genes[1].geneName,
    organism; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/new-uniprot-P04690.raw
  accessed_at: '2026-11-03T01:56:20.208693Z'
  snapshot_sha256: c69ad46d36f683e79190ba96368918cb4acf3d8729ff6666511e22ae79267613
  summary: P04690 is reviewed Tubulin beta-1/beta-2 chain, taxon3055. Native genes
    array contains two separate gene objects TUBB1 and TUBB2, not one gene with synonym
    TUB2. Accession is valid; alias wording is not.
  support: supports
- evidence_id: current-canonical-search-TUBA1
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28organism_id%3A3055%29+AND+%28reviewed%3Atrue%29+AND+%28gene%3ATUBA1%29&format=json&size=500
  locator: complete results array for reviewed:true AND organism_id:3055 AND gene:TUBA1,
    size500; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/canonical-search-TUBA1.raw
  accessed_at: '2026-11-03T01:59:05.056257Z'
  snapshot_sha256: 45d2fadbb365e2e7b632c704f31f09d9bb2d829418c4c698a9bf4dfa2ba26264
  summary: 'One reviewed result for canonical gene TUBA1: P09204. This confirms current
    canonical-query uniqueness; historical-symbol queries TUA1/TUB1 return zero and
    are not used as proof of wrong accession.'
  support: supports
- evidence_id: current-canonical-search-TUBB1
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28organism_id%3A3055%29+AND+%28reviewed%3Atrue%29+AND+%28gene%3ATUBB1%29&format=json&size=500
  locator: complete results array for reviewed:true AND organism_id:3055 AND gene:TUBB1,
    size500; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/canonical-search-TUBB1.raw
  accessed_at: '2026-11-03T01:59:05.056434Z'
  snapshot_sha256: 416573c7cd58f197540434e075c49f579fc0a64d4d9f5e8648129199864a2305
  summary: 'One reviewed result for canonical gene TUBB1: P04690. This confirms current
    canonical-query uniqueness; historical-symbol queries TUA1/TUB1 return zero and
    are not used as proof of wrong accession.'
  support: supports
- evidence_id: current-canonical-search-TUBB2
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28organism_id%3A3055%29+AND+%28reviewed%3Atrue%29+AND+%28gene%3ATUBB2%29&format=json&size=500
  locator: complete results array for reviewed:true AND organism_id:3055 AND gene:TUBB2,
    size500; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/canonical-search-TUBB2.raw
  accessed_at: '2026-11-03T01:59:05.056497Z'
  snapshot_sha256: 416573c7cd58f197540434e075c49f579fc0a64d4d9f5e8648129199864a2305
  summary: 'One reviewed result for canonical gene TUBB2: P04690. This confirms current
    canonical-query uniqueness; historical-symbol queries TUA1/TUB1 return zero and
    are not used as proof of wrong accession.'
  support: supports
- evidence_id: current-microtubule-agent-kato2020-full
  kind: primary_source
  reference: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0242694
  locator: Abstract; Introduction first two paragraphs; Methods insertional mutants;
    Results Isolation of tubulin-gene disruptants, Figures1-4 captions; Discussion
    first paragraph; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/microtubule-agent-kato2020-full.raw
  accessed_at: '2026-11-03T01:56:18.269997Z'
  snapshot_sha256: 5c6141f91e92c12fa696b5ac2525db2ccf629cf038b2b72b00d3fcd43724b987
  summary: Kato2020 directly treats tua1/tua2 and tub1/tub2 as distinct gene pairs
    encoding identical proteins, and creates gene-specific disruptants. This refutes
    TUB2 as merely a synonym of TUB1; the native accession can still represent the
    shared product. Most single-gene disruptants retain tubulin level and flagellar
    regeneration, so generic constituent essentiality must not imply every paralog
    is essential.
  support: supports
- evidence_id: current-microtubule-agent-interpro-alpha
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002452/
  locator: metadata.accession/type/name/description; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/microtubule-agent-interpro-alpha.raw
  accessed_at: '2026-11-03T01:56:17.892199Z'
  snapshot_sha256: ff28f4d004d8f82a804f7263ff1df3ab78d7bdbdeee755fa924a58e872602b5a
  summary: IPR002452 represents alpha tubulin, not the combined alpha/beta constituent
    class.
  support: supports
- evidence_id: current-microtubule-agent-interpro-beta
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002453/
  locator: metadata.accession/type/name/description; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/microtubule-agent-interpro-beta.raw
  accessed_at: '2026-11-03T01:56:17.941502Z'
  snapshot_sha256: edbfe5509d6e568069c7105eacc2b7e296e84e0790a16a63d836c45a094d20ef
  summary: IPR002453 represents beta tubulin, not the combined alpha/beta constituent
    class.
  support: supports
- evidence_id: current-microtubule-agent-interpro-tubulin
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000217/
  locator: metadata.accession/type/name/description; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/microtubule-agent-interpro-tubulin.raw
  accessed_at: '2026-11-03T01:56:17.972662Z'
  snapshot_sha256: ddbf902c6495d576d69c82c85daf1bdf2bc9fea5894925a4efcd87dc45ea3170
  summary: IPR000217 includes other eukaryotic tubulin classes and bacterial homologues;
    no exact combined alpha/beta class substitution is justified.
  support: supports
- evidence_id: current-connector-agent-ipr050145
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050145/
  locator: metadata.accession/type/name/description; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/connector-agent-ipr050145.raw
  accessed_at: '2026-11-03T01:56:19.379838Z'
  snapshot_sha256: 386371fb67a7de41d9f9a6ded2bbb77530d9a27411b46349d2ac050d45832910
  summary: IPR050145 Centrin/CML-like explicitly includes obelin and plant CML proteins,
    broader than connector centrins.
  support: supports
- evidence_id: current-connector-agent-ipr050230
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050230/
  locator: metadata.accession/type/name/description; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/connector-agent-ipr050230.raw
  accessed_at: '2026-11-03T01:56:19.577230Z'
  snapshot_sha256: 71caaab83a460a49f29a4c4bf6932354c77b07e1c9455f9c7521355e22c60bc0
  summary: IPR050230 is broad Calmodulin/Myosin light chain/Troponin C-like family,
    not an exact connector-centrin class.
  support: supports
- evidence_id: current-microtubule-agent-schwartz-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3439489.1/PMC3439489.1.xml
  locator: Sections s2a,s2b,s2e,s5a,s5d,s5e; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/microtubule-agent-schwartz-jats.raw
  accessed_at: '2026-11-03T01:56:16.766405Z'
  snapshot_sha256: bc72cef07174c775a057ac4b2c2edc09c5b5963774f9694bc2c69dac03fe566d
  summary: WBC6 Giardia disc scaffold is a spiral microtubule array with dorsal microribbons;13protofilaments
    and4nm/8nm repeats. Detergent-isolated discs flatten;2.8nm resolution cannot distinguish
    alpha/beta or every accessory density. Supports array example and scaffold, not
    exact isoform or measured attachment force.
  support: supports
- evidence_id: current-microtubule-agent-nomura-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC6398456.1/PMC6398456.1.xml
  locator: Sections s2a,s2c,s2d,s4a; Figures2-5 captions; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/microtubule-agent-nomura-jats.raw
  accessed_at: '2026-11-03T01:56:17.511425Z'
  snapshot_sha256: c6ec46d3df555cb74f3bcda13e9219c08f328673c0b1e0be1f868a6078c8f3a8
  summary: Chrysochromulina sp.NIES4122 extended haptonema has seven microtubules;
    fixed thin-section and demembranated negative-stain observations support specialized
    array context. Taxol20uM60min inhibits induced coiling. No identified complete
    MAP inventory or purified contraction mechanism.
  support: supports
- evidence_id: current-microtubule-agent-pilhofer-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3232192.1/PMC3232192.1.xml
  locator: Section s2 Results and Discussion all direct paragraphs; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/microtubule-agent-pilhofer-jats.raw
  accessed_at: '2026-11-03T01:56:17.511518Z'
  snapshot_sha256: d9e5918b4045ba6ca61f88df63bef425fe72bd14e24c6f730e69d349ee5709b2
  summary: BtubAB forms bacterial tubes in Prosthecobacter; native cryotomography/model
    analysis supports five-protofilament interpretation. Evolution and seam interpretation
    remain proposals. Different tubulin system from canonical eukaryotic alpha/beta
    microtubule.
  support: supports
- evidence_id: current-microtubule-agent-erb-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4244570.1/PMC4244570.1.xml
  locator: Abstract, s2-1 and s2-2 opening assay context, complete s2-5 infection
    spindle subsection and captions; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/microtubule-agent-erb-jats.raw
  accessed_at: '2026-11-03T01:56:17.787274Z'
  snapshot_sha256: af2c840c44ca7f9cee56ac8b4333fe4d7814d7011771f971810787f65a15f985
  summary: Phage201phi2-1 PhuZ in P.chlororaphis forms a dynamic bipolar spindle-like
    system during infection; purified dynamics and GFP live-cell observations do not
    make it a canonical eukaryotic alpha/beta microtubule. Anchor identity remains
    unresolved.
  support: supports
- evidence_id: current-microtubule-agent-duggin-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4369195.1/PMC4369195.1.xml
  locator: 'Main-body direct paragraphs: CetZ structures, deletions, rod development,
    localization, dynamics and concluding interpretation; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/microtubule-agent-duggin-jats.raw'
  accessed_at: '2026-11-03T01:56:17.848475Z'
  snapshot_sha256: 54e1fd62d5322677f3ba4eed48dcf33fbe2c423156dd2b5e166e87b3986bcf72
  summary: H.volcaniiH98 CetZ1 is a cell-shape/motility system distinct from FtsZ
    division; CetZ2 crystal protofilaments/sheets and CetZ1 patches/filaments do not
    establish canonical alpha/beta tubes. GFP partial function and mutant hyperstability
    are explicit.
  support: supports
- evidence_id: current-microtubule-agent-dutcher-jats
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4888484.1/PMC4888484.1.xml
  locator: Abstract and Sec2 Basal body structure; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/microtubule-agent-dutcher-jats.raw
  accessed_at: '2026-11-03T01:56:17.409424Z'
  snapshot_sha256: 429c24022ba00944721b09a7837e0e2c78fb2a041648a150915bd5a658ac188d
  summary: Secondary review supplies basal-body triplet and transition-zone doublet
    context and specialized tubulin classes; no primary experiment is claimed and
    these associated proteins are not imported as universal microtubule components.
  support: context_only
- evidence_id: current-microtubule-agent-mcquillen-jats
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC8610174.1/PMC8610174.1.xml
  locator: Abstract and S2 Overview of FtsZ and the Divisome; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/microtubule-agent-mcquillen-jats.raw
  accessed_at: '2026-11-03T01:56:17.883364Z'
  snapshot_sha256: 8a76b9af3fed1226ad5e9e6f00452499f9541ace397318b6d6ff1635dd0ca45d
  summary: Secondary review supplies FtsZ cytokinetic polymer-class context; no claim
    of canonical eukaryotic microtubule identity or independently audited primary
    mechanism.
  support: context_only
- evidence_id: current-microtubule-agent-epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=100&query=DOI%3A%2210.1126/science.1128618%22%20OR%20DOI%3A%2210.1371/journal.pone.0043783%22%20OR%20DOI%3A%2210.1186/s13630-016-0039-z%22%20OR%20DOI%3A%2210.1242/bio.036590%22%20OR%20DOI%3A%2210.1371/journal.pbio.1001213%22%20OR%20DOI%3A%2210.1073/pnas.1705062114%22%20OR%20DOI%3A%2210.1101/gad.1546107%22%20OR%20DOI%3A%2210.7554/eLife.03197%22%20OR%20DOI%3A%2210.1038/nature13983%22%20OR%20DOI%3A%2210.1146/annurev-biophys-121219-081703%22
  locator: All10 exact DOI metadata; full primary abstracts for Deng2017 and Larsen2007;
    native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/microtubule-agent-epmc.raw
  accessed_at: '2026-11-03T01:56:16.766353Z'
  snapshot_sha256: b77bc99862348bf58fef8064fd6b7c590a0809bf3a3ab39d045a2fdea19df326
  summary: All cited identities match. Fresh primary abstracts support four-stranded
    BtubAB mini-microtubules with in-vitro dynamics, and TubZ treadmilling/plasmid
    maintenance. Current legacy full-text fetches returned challenge pages, so their
    detailed historical body readings are not independently freshly reproduced.
  support: supports
- evidence_id: current-nuclear-agent-epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1146/annurev.cellbio.20.022003.114106%22
  locator: Exact DOI result PMID15473833; full abstract and publication metadata;
    native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/nuclear-agent-epmc.raw
  accessed_at: '2026-11-03T01:56:18.543163Z'
  snapshot_sha256: 54b1400b7916632fc27591244775377c825e7a504eafffc648737970d0d796f8
  summary: Jaspersen/Winey2004 citation identity matches and is explicitly a review,
    not a primary experiment. Abstract is consistent with bounded SPB microtubule-organizing
    context.
  support: supports
- evidence_id: current-connector-agent-1985-pdf
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2113967.1/PMC2113967.1.pdf
  locator: Abstract; printed1904-1906 isolation/immunoreactivity/calcium paragraphs;
    printed1908-1911 identity, artifact caveats and systemII boundary; native bytes
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/connector-agent-1985-pdf.raw
  accessed_at: '2026-11-03T01:56:18.555682Z'
  snapshot_sha256: 1ec9c7409a6e7191df1a37c2f7efb610282b3c43cefa8e3600f4d0af0ecff1b3
  summary: Primary text supports fibrous nucleus-basal-body connection, acidic20kDa
    antibody-reactive protein and calcium shortening. Whole-cell staining limits preparation
    artifact concern. Approximately6nm filaments were tentatively assigned; no definitive
    diameter or universal essentiality inferred. Figure pixels not fully audited.
  support: supports
- evidence_id: current-connector-agent-1987-pdf
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2114663.1/PMC2114663.1.pdf
  locator: All seven pages extracted text; printed1799 gamete Methods,1800 reactivation,1801-1804
    results,Figure2 andTableI; Figure2 on PDFpage4 independently visually inspected;
    native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/connector-agent-1987-pdf.raw
  accessed_at: '2026-11-03T01:56:18.874431Z'
  snapshot_sha256: a742c84cb85915321404f0c531f1bb1e851a64dd7ad608e24449b8a8488ab619
  summary: '137c derivativeNOmt+ gametes: living deflagellation snapshots and extracted
    NP40 models support root contraction/anterior nucleus and EGTA reextension. Refractory
    models need ATP potentiation before renewed calcium response; ATP alone is not
    contraction. Phosphorylation is proposed, not established. Figure2 has9panels
    in3rows and5umbar as record describes.'
  support: supports
- evidence_id: current-connector-agent-1987-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2114663.1/PMC2114663.1.xml
  locator: front/article-meta/permissions/license and explicit license_ref/license-p;
    native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/connector-agent-1987-jats.raw
  accessed_at: '2026-11-03T01:56:18.605100Z'
  snapshot_sha256: 226ef7af3a1147f68912bad8960dc9fc8bfd8f90341263c04f3b020458fd5b67
  summary: Native JATS explicitly grants CC BY-NC-SA4.0; validates record link-only
    Figure2 licensing. Text is PDF-preformat; scientific experiment support is independently
    tied to the PDF row.
  support: context_only
- evidence_id: current-connector-agent-1992-pdf
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2289752.1/PMC2289752.1.pdf
  locator: Abstract; printed1617 class1/class2 and immunolocalization;1618-1619 contracted
    extracted models;1622-1623 Discussion andTableII; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/connector-agent-1992-pdf.raw
  accessed_at: '2026-11-03T01:56:18.977965Z'
  snapshot_sha256: dc06c2312e33688b48b18e0f93665b811d0a010055b929bcbea17cf62ec6e349
  summary: vfl2E101K and intragenic revertants link tested centrin to NBBC/striated-fiber/transition-region
    assembly. Class2Met/Ile restore apparently normal NBBC despite abnormal distal
    fibers. Segregation claim is authors inference by exclusion, not selective NBBC
    ablation; record preserves this limitation.
  support: supports
- evidence_id: current-connector-agent-2005-legacy
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1168961/?report=xml
  locator: Methods strain/cytoskeleton preparation; Results paragraphs on NBBC and
    continuity; Discussion Sfi1/CBP1.1 scaffold proposal; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/connector-agent-2005-legacy.raw
  accessed_at: '2026-11-03T01:56:19.128125Z'
  snapshot_sha256: 5531276dc889b394f6867dc817fe1977a6336ef73e9834a276609a598a6d6d15
  summary: cw15+SAG83.81 isolated interphase cytoskeleton immunogold supports broader
    scaffold association. NBBC continuity with neighboring fibers cannot all be directly
    proven; Sfi1/CBP1.1 is an imported candidate hypothesis, not established Chlamydomonas
    NBBC constituent.
  support: supports
- evidence_id: current-connector-agent-epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=100&query=DOI%3A%2210.1083/jcb.101.5.1903%22%20OR%20DOI%3A%2210.1083/jcb.105.4.1799%22%20OR%20DOI%3A%2210.1002/cm.970140409%22%20OR%20DOI%3A%2210.1083/jcb.119.6.1613%22%20OR%20DOI%3A%2210.1007/s00709-003-0016-4%22%20OR%20DOI%3A%2210.1128/EC.4.7.1253-1263.2005%22
  locator: Exact six DOI results and all returned primary abstracts, especially1989
    and2003; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/connector-agent-epmc.raw
  accessed_at: '2026-11-03T01:56:19.132399Z'
  snapshot_sha256: 4a29776f419ce2829602aecddda59b8a476333db3ed6a5ac363e399c0349c7f4
  summary: 1989 directly tests preserved post-deflagellation gene induction in connector-defective
    vfl2.2003 compares Synura petersenii and Mallomonas species; strong20-22kDa immunoblot
    and mitotic description are Synura-specific. Current Springer fetch is challenge
    content, so fresh2003 support is primary-abstract-bounded;1989 full text remains
    unread.
  support: supports
- evidence_id: current-connector-agent-uniprot
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P05434.json
  locator: primaryAccession, entryType, recommended name, organism, absent genes field,
    sequence, sequence-source references; native bytes /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/connector-agent-uniprot.raw
  accessed_at: '2026-11-03T01:56:20.005703Z'
  snapshot_sha256: dbc691271995563a38fd19896c92adfb1902cb79dde0e8d777c45effc2a05c79
  summary: P05434 is reviewed Caltractin/Centrin,taxon3055,169aa, no primary gene
    supplied. Species-level example and references fit tested centrin; does not prove
    cross-taxon connector-specific paralog or full inventory.
  support: supports
- evidence_id: current-micro-nicastro-browser
  kind: primary_source
  reference: https://www.researchgate.net/publication/6871150_The_Molecular_Architecture_of_Axonemes_Revealed_by_Cryoelectron_Tomography
  locator: Initial abstract/body lines112-136 and Figure1 captions lines40-43; shared
    captured browser response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/nicastro-jaspersen-browser.json;
    SHA256 is entire JSON receipt, not native publisher bytes
  accessed_at: '2026-11-03T01:57:22.231Z'
  snapshot_sha256: 3e099904c6bfa7b06b1054425088f401660eb77bcab988c2ac489b0a3901d4b0
  support: supports
  summary: Author-uploaded primary manuscript supports Chlamydomonas/sea-urchin axoneme
    arrays, with Chlamydomonas panelsF-H. No exact isoform assignment or independent
    PDF/movies/pixels audit.
- evidence_id: current-micro-jaspersen-browser
  kind: authority
  reference: https://www.researchgate.net/publication/8241691_THE_BUDDING_YEAST_SPINDLE_POLE_BODY_Structure_Duplication_and_Function
  locator: Fresh browser extraction manuscript pp24-26 Microtubule Nucleation and
    Microtubule-Dependent Functions, lines978-1073; earlier current-session paper2004-browser.json
    p5 read independently; shared captured browser response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/adversary-microtubule/nicastro-jaspersen-browser.json;
    SHA256 is entire JSON receipt, not native publisher bytes
  accessed_at: '2026-11-03T01:57:22.231Z'
  snapshot_sha256: 3e099904c6bfa7b06b1054425088f401660eb77bcab988c2ac489b0a3901d4b0
  support: supports
  summary: Secondary author manuscript explicitly locates nuclear microtubule origins
    at inner plaque and describes alpha/beta arrays extending into nucleoplasm. Supports
    bounded yeast example without universal site, composition or strain claims.
- evidence_id: current-record-microtubule
  kind: record_content
  reference: data/structures/cytoskeleton/microtubule.yaml
  locator: Entire current record; original bundle compared to this input
  accessed_at: '2026-11-03T02:01:21.698922Z'
  snapshot_sha256: 170483f42c69e1b91f2e11ace0483b30aa3beeba791119a77c644c99da1decc6
  support: context_only
  summary: Current record independently read at PR head9d7ce4c503b68329385b8c73999c721c00deef34;
    stale delta consists of two reviewed UniProt examples and curation history.
- evidence_id: current-record-nuclear_microtubule
  kind: record_content
  reference: data/structures/cytoskeleton/nuclear_microtubule.yaml
  locator: Entire current record; original bundle compared to this input
  accessed_at: '2026-11-03T02:01:21.698922Z'
  snapshot_sha256: 09096977c74bdb36271d09b2a8aa1ac4c269ff8f3adbc854beae8b348f8aa252
  support: context_only
  summary: Current record independently read at PR head9d7ce4c503b68329385b8c73999c721c00deef34;
    bytes match original frozen review input.
- evidence_id: current-record-nucleus_basal_body_connector
  kind: record_content
  reference: data/structures/cytoskeleton/nucleus_basal_body_connector.yaml
  locator: Entire current record; original bundle compared to this input
  accessed_at: '2026-11-03T02:01:21.698922Z'
  snapshot_sha256: 89e5e96440535f65493ee4b2928b835f415f79358200f32d877ec59487300f0d
  support: context_only
  summary: Current record independently read at PR head9d7ce4c503b68329385b8c73999c721c00deef34;
    bytes match original frozen review input.
- evidence_id: ipr016491
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016491/
  locator: Native accession/name/type/hierarchy and generic family description
  accessed_at: '2026-11-03T01:54:20.570567Z'
  snapshot_sha256: 5797c626d192b641ed5b4b2231e729f9f179bfd6bb18f911689fa08253688c4a
  summary: IPR016491 is the Septin family; class grounding does not require complete
    mitotic assembly composition.
  support: supports
- evidence_id: mitotic-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005940,GO:0031105,GO:0032151,GO:0032152
  locator: Four complete active GO terms and direct parent child list
  accessed_at: '2026-11-03T01:54:20.528268Z'
  snapshot_sha256: 45ba4b66451232f3765af5f098ab85b8d45464136fdd237fb6250c19ee29480c
  summary: GO0032151 is the mitotic heterooligomer; parentGO0031105, meiotic siblingGO0032152,
    ringGO0005940 distinct.
  support: supports
- evidence_id: sin-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0071958,GO:0160065,GO:0160066,GO:0160067,GO:1990334
  locator: Five complete GO terms, synonyms and parent child lists
  accessed_at: '2026-11-03T01:54:20.526289Z'
  snapshot_sha256: 06fba1d1f2ef39145692a64bda546596ecbc1315c90fd314e689ab0d58852e6c
  summary: GO0160067 exact identity/synonym and parentGO0160065 confirmed; active
    Spg1 at newSPB during anaphase; association is not asserted parthood.
  support: supports
- evidence_id: versele
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1761124/?pdf=render
  locator: Secondary review S2,S3,S4 and Table1 context
  accessed_at: '2026-11-03T01:54:20.386810Z'
  snapshot_sha256: f397cf97bc67fb2894de8f8d4d3a5f3d6dda395ed00c87a9723bd7a38cfa020d
  summary: Review distinguishes mitotic from meiotic cohorts, oligomers from higher
    polymers and species-specific paralogs. No primary experiment repetition or universal
    copy-count inference.
  support: supports
- evidence_id: johnson
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3025462/?pdf=render
  locator: PMC3025462 Introduction; Resultssec3,5–9 with captions; Discussionsec11–14/Fig8caption;
    Methodssec16,17,20,22
  accessed_at: '2026-11-03T01:54:20.397031Z'
  snapshot_sha256: 334f7a294a448d8fa64599e7ccc5abbbb6dcc548c30885c92ad7b07880457365
  summary: Introduction synthesizes prior pole-age asymmetry work. Actual experiments
    examine Dma1-dependent Sid4 ubiquitination, Plo1 localization and Byr4 phosphorylation/localization
    during defined arrests. Fig8 is a model, not whole-SIN reconstitution.
  support: supports
- evidence_id: sin-species
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4896
  locator: taxId,scientificName,rank
  accessed_at: '2026-11-03T01:54:20.633023Z'
  snapshot_sha256: 42c5b7d3d99341137803612d6404cd3884e2d06ec8a740b1ad38163c678f6721
  summary: NCBITaxon4896 is Schizosaccharomyces pombe, species rank.
  support: supports
- evidence_id: sin-metadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1038/emboj.2010.317&format=json&resultType=core
  locator: Exact DOI result title,authors,PMID,PMCID and abstract
  accessed_at: '2026-11-03T01:54:20.657313Z'
  snapshot_sha256: aee80cef63e67f5a3d0babbad6f40b588d62fae282f1cf628f45f5bc6e15144f
  summary: DOI10.1038/emboj.2010.317 is Johnson/Gould2011, PMID21131906, PMC3025462.
  support: supports
- evidence_id: adapter-catalogue
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Entire official public organism/dataset catalogue
  accessed_at: '2026-11-03T01:54:20.056965Z'
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  summary: Complete official catalogue contains20 organisms and28 datasets, all bacterial/archaeal.
    No dataset covers the target yeast or protist examples (Saccharomyces, Schizosaccharomyces,
    Chlamydomonas, Giardia, Mallomonas or Synura). This establishes coverage-based
    non-applicability, not absence of the structures or genes.
  support: supports
- evidence_id: check-qc
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/qc.log
  locator: Actual stdout/stderr and command receipt
  accessed_at: '2026-11-03T01:59:40.937170Z'
  support: supports
  summary: Full native QC returned exit0.
  snapshot_sha256: 633afb11a7c643fe7ea61d4f888ecf59aa9304d8ffc1206c61fa15d1dd85f187
- evidence_id: check-labels
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/labels.log
  locator: Actual stdout/stderr and command receipt
  accessed_at: '2026-11-03T01:55:06.829930Z'
  support: supports
  summary: Native label correspondence returned exit0.
  snapshot_sha256: d8200b370ec584f49336f01ed9035fbe21f0aa191ad0257a9a421938e9f17ecb
- evidence_id: check-trait-links
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/trait-links.log
  locator: Actual stdout/stderr and command receipt
  accessed_at: '2026-11-03T01:58:06.886529Z'
  support: supports
  summary: TraitMech references returned exit0.
  snapshot_sha256: 8b336cdefbbd3daf6da8787990efdbe346c95e2c8361d50b7eb68a18f2d5a44a
- evidence_id: check-vendored
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/vendored.log
  locator: Actual stdout/stderr and command receipt
  accessed_at: '2026-11-03T01:58:03.655188Z'
  support: supports
  summary: Pinned governed files returned exit0.
  snapshot_sha256: b1f169d103aaefa930745468bcca171e5867b9cc49e4e74311e458097e3252a6
- evidence_id: check-curies
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/curies.log
  locator: Actual stdout/stderr and command receipt
  accessed_at: '2026-11-03T01:55:12.217119Z'
  support: supports
  summary: Native identifier resolver returned exit0.
  snapshot_sha256: fb3be251020aac118f6df680372ae7aaa32c2a1dd3366648cde95494f19d9dd2
- evidence_id: focused
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/focused-results.json
  locator: All20 actual schema/strict command outputs
  accessed_at: '2026-11-03T02:10:18Z'
  support: supports
  summary: Ten target schema and ten target strict checks passed.
  snapshot_sha256: f837e7dd22cb36d1b5beb01053673f964c9908dab42b95798a90e7090081fbe3
- evidence_id: supplemental-pmid
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2346/pmid-chunks-receipt.json
  locator: Exact909-PMID set checked by unchanged native resolver in19 requests of
    at most50
  accessed_at: '2026-11-03T01:58:21.883947Z'
  support: supports
  summary: All909 PMIDs returned OK. Original full-command report/cache remain unchanged;254
    skipped identifiers are not claimed resolved.
  snapshot_sha256: 3218ac7e64d2465b52c023efbcf98797c715f3782c2ad6cfd1a1697d8cafddca
assessments:
- assessment_id: current-0
  area: evidence
  topic: meiotic spindle pole body current scientific assessment
  outcome: supported
  summary: The exact whole meiotic-SPB identity, GO parent and S. cerevisiae example
    are supported. The graph correctly scopes the MOP substructure and normal prospore-membrane
    initiation site to budding-yeast meiosis II. Knop/Strasser, Bajgier and Mathieson
    distinguish normal membrane initiation/docking from precursor targeting and mutant
    untethered membranes; the target asserts neither autonomous fusion catalysis nor
    absolute mature-plaque dependence in every mutant. Optional composition remains
    a documented limitation, with no asserted erroneous family accessions or copy
    counts.
  target_ids:
  - GO:0035974
  evidence_ids:
  - record-0
  - prior-0
  - meiotic-spb-agent-go
  - meiotic-spb-agent-taxon
  - meiotic-spb-agent-knop2000
  - meiotic-spb-agent-bajgier2001
  - meiotic-spb-agent-mathieson2010-pmc
  - context-mop
- assessment_id: current-1
  area: evidence
  topic: mitotic spindle pole body current scientific assessment
  outcome: supported
  summary: GO supports the exact mitotic-cell-cycle subtype and half-bridge/intermediate-layer
    parthood. G1 duplication is compatible with this scope; the half-bridge edge is
    a bounded assembly-site statement, not a complete molecular recruitment order.
    Primary core-architecture context and the cited review support nuclear/cytoplasmic
    microtubule organization. Optional database candidates remain bounded by strain,
    family/domain, subcomplex and stoichiometry scope; no erroneous composition is
    asserted.
  target_ids:
  - GO:0044732
  evidence_ids:
  - record-1
  - prior-1
  - mitotic-spb-agent-go
  - meiotic-spb-agent-taxon
  - mitotic-spb-agent-strain
  - spb-jaspersen2004-author-manuscript
  - mitotic-spb-agent-viswanath2017
  - mitotic-spb-agent-candidate-proteins
  - mitotic-spb-agent-CPX-1198
  - mitotic-spb-agent-CPX-1420
  - mitotic-spb-agent-IPR002454
  - mitotic-spb-agent-IPR007259
  - mitotic-spb-agent-IPR021611
  - mitotic-spb-agent-IPR040593
  - spb-ipr021750-cached
- assessment_id: current-2
  area: evidence
  topic: new mitotic spindle pole body current scientific assessment
  outcome: supported
  summary: The exact GO identity, new-SPB synonym, mitotic-SPB parent and S. pombe
    example are supported. Grallert Results sec4/sec5/sec8 and Discussion sec13 demonstrate
    conservative age labeling, active SIN on the new SPB in anaphase B/G1, and history-dependent
    Fin1 recruitment. The target avoids equating Fin1 with an exclusive or permanent
    new-pole constituent and keeps local generic duplication placeholders distinct
    from the exact age/asymmetry class. Optional protein-family composition remains
    unresolved without an asserted mapping error.
  target_ids:
  - GO:0071958
  evidence_ids:
  - record-2
  - prior-2
  - new-mitotic-spb-agent-go
  - new-mitotic-spb-agent-taxon
  - new-mitotic-spb-agent-grallert2004-metadata
  - new-mitotic-spb-agent-grallert2004
  - context-spb
- assessment_id: current-7
  area: evidence
  topic: outer plaque of mitotic spindle pole body current scientific assessment
  outcome: concern
  summary: Exact GO identity, generic-outer-plaque is-a and mitotic-SPB parthood,
    cytoplasmic orientation and bounded microtubule-organizing function are supported.
    The meiotic remodeling boundary and optional composition limitations are sound.
    Three mitosis-specific phrases can imply M-phase restriction; the source supports
    a mitotic-cell-cycle subtype instead. This is a minor ambiguity requiring wording
    curation, not rejection of the identity or topology.
  target_ids:
  - GO:0061499
  evidence_ids:
  - record-7
  - prior-7
  - mitotic-outer-plaque-agent-go
  - meiotic-spb-agent-taxon
  - spb-jaspersen2004-author-manuscript
  - mitotic-spb-agent-viswanath2017
  - meiotic-spb-agent-knop2000
  - mitotic-spb-agent-candidate-proteins
  - mitotic-spb-agent-IPR002454
  - mitotic-spb-agent-IPR007259
  - spb-ipr021750-cached
- assessment_id: current-8
  area: evidence
  topic: outer plaque of spindle pole body current scientific assessment
  outcome: supported
  summary: The cytoplasmic plaque identity, whole-SPB parthood, budding-yeast example
    and bounded cytoplasmic microtubule organization are supported. Three named plaques
    plus intermediate layers are compatible descriptions. The plaque remains distinct
    from associated gamma-TuSC, the meiotic remodeling product and the separate prospore-membrane
    attachment region. No phase-only claim, fixed stoichiometry or exact erroneous
    protein-family mapping is asserted; optional composition stays a limitation.
  target_ids:
  - GO:0005824
  evidence_ids:
  - record-8
  - prior-8
  - outer-plaque-agent-go
  - meiotic-spb-agent-taxon
  - spb-jaspersen2004-author-manuscript
  - mitotic-spb-agent-viswanath2017
  - meiotic-spb-agent-knop2000
  - mitotic-spb-agent-candidate-proteins
  - mitotic-spb-agent-IPR002454
  - mitotic-spb-agent-IPR007259
  - spb-ipr021750-cached
- assessment_id: current-5
  area: evidence
  topic: microtubule current scientific assessment
  outcome: concern
  summary: Exact GO generic alpha/beta microtubule identity, topology and bounded
    specialized-array examples are supported. InterPro collective class remains honestly
    label-only. New P09204 and P04690 reviewed accession/name/taxon identities and
    canonical-query uniqueness are verified. Q6SPP7 remains an unreviewed22aa fragment
    used only as identity. The new P04690 TUB2 synonym wording is a minor scientific
    curation request; all record edits stay outside this PR.
  target_ids:
  - GO:0005874
  evidence_ids:
  - record-5
  - prior-5
  - current-microtubule-agent-go
  - current-new-uniprot-P09204
  - current-new-uniprot-P04690
  - current-microtubule-agent-kato2020-full
  - current-microtubule-agent-schwartz-jats
  - current-micro-nicastro-browser
  - current-microtubule-agent-interpro-tubulin
  - current-record-microtubule
- assessment_id: current-6
  area: evidence
  topic: nuclear microtubule current scientific assessment
  outcome: supported
  summary: Unchanged nuclear microtubule is exact location-defined GO subtype, part
    of nucleus, with one bounded budding-yeast inner-plaque organization example.
    Graph is NONMECHANISTIC and does not conflate nuclear location with spindle membership.
    Optional molecular inventory is explicitly deferred, not falsely asserted. Secondary
    literature remains identified as secondary.
  target_ids:
  - GO:0005880
  evidence_ids:
  - record-6
  - prior-6
  - current-nuclear-agent-go
  - current-nuclear-agent-taxon
  - current-micro-jaspersen-browser
  - current-nuclear-agent-epmc
  - current-record-nuclear_microtubule
- assessment_id: current-9
  area: evidence
  topic: nucleus-basal body connector current scientific assessment
  outcome: supported
  summary: Unchanged connector identity, centrin species example, broader rootlet
    parent, conditional calcium/EGTA/ATP graph, and Figure2 provenance are supported.
    Living-gamete versus extracted-model context is preserved; ATP potentiation is
    not contraction or established phosphorylation. Mutant segregation inference is
    not selective connector ablation; Sfi1/CBP1.1 is a proposal, not imported constituent.
    Chrysomonad examples and negative gene-induction claim remain abstract-bounded.
    No new scientific defect found.
  target_ids:
  - cellstructuremech:nucleus_basal_body_connector
  evidence_ids:
  - record-9
  - prior-9
  - current-connector-agent-go
  - current-connector-agent-uniprot
  - current-connector-agent-1985-pdf
  - current-connector-agent-1987-pdf
  - current-connector-agent-1987-jats
  - current-connector-agent-1992-pdf
  - current-connector-agent-2005-legacy
  - current-connector-agent-epmc
  - current-record-nucleus_basal_body_connector
- assessment_id: current-3
  area: evidence
  topic: mitotic septin complex current scientific assessment
  outcome: concern
  summary: Exact generic mitotic heterooligomer and nonmechanistic oligomerization
    remain supported. Generic Septin family grounding can be resolved independently
    of full species-specific subunit set. Existing minorF1 remains open.
  target_ids:
  - GO:0032151
  evidence_ids:
  - record-3
  - prior-3
  - ipr016491
  - mitotic-go
  - versele
- assessment_id: current-4
  area: evidence
  topic: new spindle pole body SIN signaling complex current scientific assessment
  outcome: supported
  summary: Exact new-SPB anaphase signaling complex identity, parentage and narrow
    S.pombe example/function supported. Source correctly separates prior asymmetry
    background, newly measured scaffold regulation and proposed Fig8 mechanism. No
    additional scientific curation defect observed; no compulsory inventory or graph
    invented.
  target_ids:
  - GO:0160067
  evidence_ids:
  - record-4
  - prior-4
  - sin-go
  - johnson
  - sin-species
  - sin-metadata
- assessment_id: stale-protein-examples
  area: grounding
  topic: Changed microtubule input and accession-versus-gene boundary
  outcome: concern
  summary: The original microtubule observation predates P09204/P04690 and cannot
    certify those additions. Both current reviewed accessions, taxon and canonical-name
    query uniqueness are supported. P04690 represents products of two distinct beta-tubulin
    genes, so TUB2-as-synonym wording needs a bounded correction. The valid accession
    and identity-only membership disclaimer remain intact.
  target_ids:
  - GO:0005874
  evidence_ids:
  - record-5
  - prior-5
  - current-new-uniprot-P09204
  - current-new-uniprot-P04690
  - current-canonical-search-TUBA1
  - current-canonical-search-TUBB1
  - current-canonical-search-TUBB2
  - current-microtubule-agent-kato2020-full
- assessment_id: adapter-coverage
  area: scope
  topic: Structured-source organism coverage and physical-mechanism boundary
  outcome: supported
  summary: Fresh official catalogue inspection shows no relevant yeast or protist
    dataset. Downstream organism-specific expression-module searches are not applicable.
    The original rationales in the named-molecule cases excluded the adapter solely
    by physical/nontranscriptomic subject matter; this follow-up supplies the missing
    coverage basis. The nuclear-microtubule record has no named molecular-gene/accession
    trigger, so no omission is invented there. The prior canary runner failure is
    historical OS-access evidence, not a newly executed check.
  target_ids:
  - GO:0035974
  - GO:0044732
  - GO:0071958
  - GO:0032151
  - GO:0160067
  - GO:0005874
  - GO:0005880
  - GO:0061499
  - GO:0005824
  - cellstructuremech:nucleus_basal_body_connector
  evidence_ids:
  - adapter-catalogue
findings:
- finding_id: F1
  issue_key: mitotic-septin-complex-family-grounding-scope
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Assembly-cohort criterion leaves generic Septin family ungrounded
  description: The generic septin-proteins component remains REVIEWED_LABEL_ONLY while
    its rationale waits for a mapping for the full mitotic cohort. Native IPR016491
    identifies the named family. Reconcile the family mapping, status and notes while
    retaining the separate unresolved species-specific and accessory inventory.
  target_ids:
  - GO:0032151
  field_paths:
  - components[component_id=septin_proteins].grounding_status
  - components[component_id=septin_proteins].grounding_notes
  - discussions[discussion_id=resolve_mitotic_septin_complex_components]
  evidence_ids:
  - record-3
  - prior-3
  - ipr016491
  - mitotic-go
  - versele
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/mitotic_septin_complex.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Components
  native_severity: minor
  normalization_reason: Bounded resolvable mapping gap; exact structure identity and
    descriptive oligomerization remain supported.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T074638Z-mitotic-septin-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2499
- finding_id: F2
  issue_key: outer-plaque-mitotic-cell-cycle-wording
  category: scope
  severity: minor
  status: open
  certainty: confirmed
  title: Outer mitotic plaque wording can imply unsupported M-phase restriction
  description: Three mitosis-specific phrases can imply existence restricted to M
    phase. GO0044732 defines the mitotic-cell-cycle SPB; the cited review describes
    persistent SPBs and G1 activity. The record provides no evidence for M-phase-only
    existence. The original review recognized the source limitation but omitted the
    corresponding curation finding.
  target_ids:
  - GO:0061499
  field_paths:
  - causal_graphs[0].description
  - causal_graphs[0].edges[0].description
  - discussions[0].resolution_note
  evidence_ids:
  - record-7
  - prior-7
  - mitotic-outer-plaque-agent-go
  - spb-jaspersen2004-author-manuscript
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/outer_plaque_of_mitotic_spindle_pole_body.yaml
    role: maintained scientific record
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2515
- finding_id: F3
  issue_key: microtubule-beta-genes-not-synonyms
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: One beta-tubulin protein entry does not make two genes synonyms
  description: The new reviewed beta-tubulin example calls TUB2 a synonym. TUB1 and
    TUB2 are distinct genes encoding the same amino-acid sequence, and P04690 has
    separate TUBB1 and TUBB2 gene objects. Shared product/accession does not make
    these genes aliases.
  target_ids:
  - GO:0005874
  field_paths:
  - components[component_id=alpha_beta_tubulins].protein_examples[uniprot_id=UniProtKB:P04690].role
  evidence_ids:
  - record-5
  - prior-5
  - current-new-uniprot-P04690
  - current-microtubule-agent-kato2020-full
  - current-canonical-search-TUBB1
  - current-canonical-search-TUBB2
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/microtubule.yaml
    role: maintained scientific record
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2516
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0032151
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/mitotic_septin_complex.yaml
    role: maintained scientific record
  description: Separately ground the generic mitotic septin class to the verified
    Septin family and reconcile status, notes and TODO while retaining unresolved
    species/paralogue/accessory membership. Existing consolidated issue2499 tracks
    this record alongside distinct medial and meiotic targets.
  acceptance_checks:
  - Verify native IPR016491 name/type and preserve independent assembly-localization
    evidence.
  - Do not infer universal copy counts, paralog essentiality, occurrence or a complete
    complex from family grounding.
  - Use guarded record writing, curation/history and native validation in a separate
    scientific curation PR.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - GO:0061499
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/outer_plaque_of_mitotic_spindle_pole_body.yaml
    role: maintained scientific record
  description: Curate the three phrases to of the mitotic-cell-cycle SPB or equivalent,
    preserving the exact GO identity and relations. Do not edit the record in this
    review-only PR.
  acceptance_checks:
  - All three affected fields retain mitotic-cell-cycle subtype scope without unsupported
    M-phase exclusivity.
  - Preserve exact identity/topology and use guarded scientific curation, history
    and native validation in a separate PR.
- action_id: A3
  finding_ids:
  - F3
  target_ids:
  - GO:0005874
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/microtubule.yaml
    role: maintained scientific record
  description: Retain P04690 and its reviewed label/status; replace synonym wording
    with an explicit statement that one protein entry represents products of the two
    distinct beta-tubulin genes. Keep accession identity separate from membership.
  acceptance_checks:
  - Describe two distinct beta-tubulin genes sharing the protein entry/product; preserve
    valid accession/status/taxon.
  - Maintain identity-versus-membership distinction; perform record/history/native
    validation changes in a separate curation PR.
limitations:
- The 2004 literature-review source is author-manuscript browser extraction, not verified
  publisher PDF bytes; its underlying primary literature was not exhaustively reread.
- Primary article text and claim-relevant figure legends were read; raw data, microscopy
  pixels, movies, model inputs and all supplements were not independently reanalyzed.
- IPR021750 returned HTTP429 at 2026-11-03T01:54:20.713748Z; no retry was made. The
  independently inspected response from00:45:04.724098Z is reused with that earlier
  timestamp, not represented as fresh successful access.
- Family/domain candidates and S288C complex entries do not establish complete plaque/SPB
  inventories, universal fungal/strain composition or whole-organelle stoichiometry.
- Current Deng/Larsen legacy HTML and Springer2003 fetches returned HTTP200 challenge
  pages, not literature. Fresh exact primary abstracts are the inspected ceiling for
  those routes; original historical full-body attestations are not represented as
  freshly reproduced.
- Nicastro and Jaspersen read through author-uploaded browser extraction; recorded
  hash is JSON browser receipt, not publisher PDF. No native HTTP status attestation.
  Jaspersen is secondary review.
- Connector1989/2003 full texts not read.1987Figure2 visually inspected; other source
  image panels/movies were not exhaustively audited.
- Historic TUA1/TUB1 exact native search strings yield no result while canonical TUBA1/TUBB1
  searches verify one reviewed accession each. This is not proof of wrong accession;
  no separate mapping finding is made.
- Versele is secondary context. Underlying primary experiments were not independently
  reanalyzed.
- Johnson figure captions and relevant prose/methods were read; figure pixels, movies,
  supplements, strain table and raw data not independently evaluated.
- Earlier primary pole-age studies cited in JohnsonIntroduction were not all reread.
- No exhaustive modern component-family search for every SIN protein was conducted.
- Adapter CLI was not rerun because its OS-level unavailability was already established
  in canary; fresh source-native catalogue inspection supplies current applicability
  basis.
- Old observations and their command receipts remain historical and immutable; changed
  record inputs are reassessed here, not merely assigned replacement hashes.
- The adapter runner was not rerun after the canary established OS access failure.
  Current coverage is established by the freshly inspected source-native catalogue,
  not by a successful CLI call.
- Label correspondence has923 no-adapter skips. The native identifier command has909
  HTTP414 transport failures and254 skipped identifiers; supplemental bounded requests
  resolve the909 PMIDs separately.
- Current scientific curation remains open; this observation neither edits records
  nor promotes native status.
- Final post-save trusted-base review-check and final-head/merge-group CI are publication
  gates performed after this immutable observation; no pending outcome is represented
  as passed.
notes:
- Original ten YAML/Markdown pairs remain byte-identical; main was merged normally
  without a force push. All changed tracked files in this PR are review bundles.
- One explicit issue-bearing cohort follows the repository persistence gate. No artificial
  issues or standalone clean bundles were created.
- Bundle fixes are tracked by issues2517(stale currentness),2518(omitted outer-plaque
  finding),2519(adapter applicability and draft count precision),2520(missing frozen
  context inputs). Scientific issues2499(reused),2515 and2516 stay open. Existing
  tooling issue2514 is reused with complete coverage disclosure.
- The source commit9d7ce4c503b68329385b8c73999c721c00deef34 is retained by additive
  tag review-base/pr2346-current-record-followup-20261103 so squash and branch deletion
  preserve native provenance validation.
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T074511Z-meiotic-spindle-pole-body-audit
  relationship: Current-input follow-up; original immutable observation retained.
    Existing finding lineage is preserved explicitly.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T074637Z-mitotic-spindle-pole-body-audit
  relationship: Current-input follow-up; original immutable observation retained.
    Existing finding lineage is preserved explicitly.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T074637Z-new-mitotic-spindle-pole-body-audit
  relationship: Current-input follow-up; original immutable observation retained.
    Existing finding lineage is preserved explicitly.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T074638Z-mitotic-septin-complex-audit
  relationship: Current-input follow-up; original immutable observation retained.
    Existing finding lineage is preserved explicitly.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T074638Z-new-spindle-pole-body-sin-signaling-complex-audit
  relationship: Current-input follow-up; original immutable observation retained.
    Existing finding lineage is preserved explicitly.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T074814Z-microtubule-audit
  relationship: Current-input follow-up; original immutable observation retained.
    Existing finding lineage is preserved explicitly.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T074814Z-nuclear-microtubule-audit
  relationship: Current-input follow-up; original immutable observation retained.
    Existing finding lineage is preserved explicitly.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T074815Z-outer-plaque-of-mitotic-spindle-pole-body-audit
  relationship: Current-input follow-up; original immutable observation retained.
    Existing finding lineage is preserved explicitly.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T074815Z-outer-plaque-of-spindle-pole-body-audit
  relationship: Current-input follow-up; original immutable observation retained.
    Existing finding lineage is preserved explicitly.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T075001Z-nucleus-basal-body-connector-audit
  relationship: Current-input follow-up; original immutable observation retained.
    Existing finding lineage is preserved explicitly.
links:
- https://github.com/CultureBotAI/CellStructureMech/pull/2346
- https://github.com/CultureBotAI/CellStructureMech/issues/2499
- https://github.com/CultureBotAI/CellStructureMech/issues/2514
- https://github.com/CultureBotAI/CellStructureMech/issues/2515
- https://github.com/CultureBotAI/CellStructureMech/issues/2516
- https://github.com/CultureBotAI/CellStructureMech/issues/2517
- https://github.com/CultureBotAI/CellStructureMech/issues/2518
- https://github.com/CultureBotAI/CellStructureMech/issues/2519
- https://github.com/CultureBotAI/CellStructureMech/issues/2520
```
