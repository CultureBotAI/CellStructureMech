# PR 2373: current-input review of ten records and adversarial follow-up

- Review: 20261103T184731Z-pr2373-current-record-followup
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-11-03T18:39:37.063967Z
- Finished UTC: 2026-11-03T18:47:31Z
- Reviewer: Codex root synthesis with three independent read-only adversarial reviewers (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Current-input adversarial follow-up for the complete ten-record cohort after merging main. All ten original target hashes still match, so no stale refresh is required. Four unsupported expression-only structured-source exclusions are corrected; six genuine physical/material-topology exclusions are preserved. Four inherited findings remain open (three major and one minor) across three records: thylakoid membrane-component identity and source attribution, osmiophilic-body egress counterevidence, and parasitophorous-vacuole canonical-example species attribution. Seven targets retain qualified positive assessments. All original review observations and scientific records remain unchanged.

## Scope And Provenance

Exact ten-record PR cohort reassessed against current main fa4d81142ca76aa4b656afbbf0ac2caa3e16c952. Changed inputs are substantively reassessed. Scientific records remain unchanged.

Selection: Complete cohort of ten maintained records reviewed in original PR head 36e49e748537472bbfdb4ac0fa6b864a40ecd661.
Coverage: full; 10 reviewed / 10 in the declared population.
Source: working_tree at Git base bdd5beb85634420b1d99c91138a9121631087f89.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0070113 | data/structures/membrane_organelle/organellar_chromatophore_inner_membrane.yaml | maintained | organellar chromatophore inner membrane |
| GO:0070115 | data/structures/membrane_organelle/organellar_chromatophore_intermembrane_space.yaml | maintained | organellar chromatophore intermembrane space |
| GO:0070112 | data/structures/membrane_organelle/organellar_chromatophore_membrane.yaml | maintained | organellar chromatophore membrane |
| GO:0070114 | data/structures/membrane_organelle/organellar_chromatophore_outer_membrane.yaml | maintained | organellar chromatophore outer membrane |
| GO:0070116 | data/structures/membrane_organelle/organellar_chromatophore_thylakoid.yaml | maintained | organellar chromatophore thylakoid |
| GO:0070117 | data/structures/membrane_organelle/organellar_chromatophore_thylakoid_lumen.yaml | maintained | organellar chromatophore thylakoid lumen |
| GO:0070118 | data/structures/membrane_organelle/organellar_chromatophore_thylakoid_membrane.yaml | maintained | organellar chromatophore thylakoid membrane |
| GO:0044310 | data/structures/membrane_organelle/osmiophilic_body.yaml | maintained | osmiophilic body |
| cellstructuremech:parasitophorous_vacuole | data/structures/membrane_organelle/parasitophorous_vacuole.yaml | maintained | parasitophorous vacuole |
| cellstructuremech:parasitophorous_vacuole_lumen | data/structures/membrane_organelle/parasitophorous_vacuole_lumen.yaml | maintained | parasitophorous vacuole lumen |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full native QC | passed | True | GO:0070113, GO:0070115, GO:0070112, GO:0070114, GO:0070116, GO:0070117, GO:0070118, GO:0044310, cellstructuremech:parasitophorous_vacuole, cellstructuremech:parasitophorous_vacuole_lumen | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| Native label correspondence | passed | True | GO:0070113, GO:0070115, GO:0070112, GO:0070114, GO:0070116, GO:0070117, GO:0070118, GO:0044310, cellstructuremech:parasitophorous_vacuole, cellstructuremech:parasitophorous_vacuole_lumen | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| TraitMech references | passed | True | GO:0070113, GO:0070115, GO:0070112, GO:0070114, GO:0070116, GO:0070117, GO:0070118, GO:0044310, cellstructuremech:parasitophorous_vacuole, cellstructuremech:parasitophorous_vacuole_lumen | Native TraitMech link check passed. |
| Pinned governed files | passed | True | GO:0070113, GO:0070115, GO:0070112, GO:0070114, GO:0070116, GO:0070117, GO:0070118, GO:0044310, cellstructuremech:parasitophorous_vacuole, cellstructuremech:parasitophorous_vacuole_lumen | Pinned governed files match; native vendored check passed. |
| Native identifier resolver | passed | True | GO:0070113, GO:0070115, GO:0070112, GO:0070114, GO:0070116, GO:0070117, GO:0070118, GO:0044310, cellstructuremech:parasitophorous_vacuole, cellstructuremech:parasitophorous_vacuole_lumen | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| validate GO:0070113 | passed | True | GO:0070113 | Documented focused command passed. |
| validate-strict GO:0070113 | passed | True | GO:0070113 | Documented focused command passed. |
| validate GO:0070115 | passed | True | GO:0070115 | Documented focused command passed. |
| validate-strict GO:0070115 | passed | True | GO:0070115 | Documented focused command passed. |
| validate GO:0070112 | passed | True | GO:0070112 | Documented focused command passed. |
| validate-strict GO:0070112 | passed | True | GO:0070112 | Documented focused command passed. |
| validate GO:0070114 | passed | True | GO:0070114 | Documented focused command passed. |
| validate-strict GO:0070114 | passed | True | GO:0070114 | Documented focused command passed. |
| validate GO:0070116 | passed | True | GO:0070116 | Documented focused command passed. |
| validate-strict GO:0070116 | passed | True | GO:0070116 | Documented focused command passed. |
| validate GO:0070117 | passed | True | GO:0070117 | Documented focused command passed. |
| validate-strict GO:0070117 | passed | True | GO:0070117 | Documented focused command passed. |
| validate GO:0070118 | passed | True | GO:0070118 | Documented focused command passed. |
| validate-strict GO:0070118 | passed | True | GO:0070118 | Documented focused command passed. |
| validate GO:0044310 | passed | True | GO:0044310 | Documented focused command passed. |
| validate-strict GO:0044310 | passed | True | GO:0044310 | Documented focused command passed. |
| validate cellstructuremech:parasitophorous_vacuole | passed | True | cellstructuremech:parasitophorous_vacuole | Documented focused command passed. |
| validate-strict cellstructuremech:parasitophorous_vacuole | passed | True | cellstructuremech:parasitophorous_vacuole | Documented focused command passed. |
| validate cellstructuremech:parasitophorous_vacuole_lumen | passed | True | cellstructuremech:parasitophorous_vacuole_lumen | Documented focused command passed. |
| validate-strict cellstructuremech:parasitophorous_vacuole_lumen | passed | True | cellstructuremech:parasitophorous_vacuole_lumen | Documented focused command passed. |
| Supplemental bounded PMID authority checks | passed | True | GO:0070113, GO:0070115, GO:0070112, GO:0070114, GO:0070116, GO:0070117, GO:0070118, GO:0044310, cellstructuremech:parasitophorous_vacuole, cellstructuremech:parasitophorous_vacuole_lumen | 909 PMIDs all OK in bounded native requests; full-command limitations remain separate. |
| Official structured-source applicability and covered-dataset cross-checks | passed | False | GO:0070113, GO:0070115, GO:0070112, GO:0070114, GO:0070116, GO:0070117, GO:0070118, GO:0044310, cellstructuremech:parasitophorous_vacuole, cellstructuremech:parasitophorous_vacuole_lumen | Four records make positive molecular claims and require source applicability assessment: chromatophore thylakoid and thylakoid membrane assert photosynthetic light-reaction complexes; osmiophilic body asserts Pfg377 and emergence/egress; whole parasitophorous vacuole makes a positive BioID/PVM-associated protein assertion. Current official iModulonDB catalogue coverage is checked for the relevant hosts/strains; unmatched datasets are not proxies and noncoverage is not biological absence. Four chromatophore envelope-boundary records plus thylakoid lumen and PV lumen retain genuine physical/topology exclusions. Historical00:49Z runner unavailability stays historical, with actual public-source fallback coverage and access limits recorded. |
| Independent claim-level source review | passed | True | GO:0070113, GO:0070115, GO:0070112, GO:0070114, GO:0070116, GO:0070117, GO:0070118, GO:0044310, cellstructuremech:parasitophorous_vacuole, cellstructuremech:parasitophorous_vacuole_lumen | Three read-only reviewers covered the complete ten-record cohort, including changed inputs, with explicit scientific findings and source-access limits. Final artifact/head acceptance occurs after saving. |
| Retained historical adapter runner availability | unavailable | False | GO:0070113, GO:0070115, GO:0070112, GO:0070114, GO:0070116, GO:0070117, GO:0070118, GO:0044310, cellstructuremech:parasitophorous_vacuole, cellstructuremech:parasitophorous_vacuole_lumen | Historical 00:49Z invocation unavailable due to OS access restriction. Official catalogue source fallback was inspected separately; no current invocation or successful adapter execution is claimed. The actual historical exit code 1 is retained in the evidence receipt, since the native unavailable-check model has no execution exit-code field. |
| Native organellar chromatophore inner membrane UniProt verify check | passed | True | GO:0070113 | Read-only native command returned zero. No protein examples or typed molecular nodes. Positive molecular/pathway assertions and justified physical-scope exclusions are assessed separately. |
| Native organellar chromatophore inner membrane UniProt causal check | passed | True | GO:0070113 | Read-only native command returned zero. No protein examples or typed molecular nodes. Positive molecular/pathway assertions and justified physical-scope exclusions are assessed separately. |
| Native organellar chromatophore intermembrane space UniProt verify check | passed | True | GO:0070115 | Read-only native command returned zero. No protein examples or typed molecular nodes. Positive molecular/pathway assertions and justified physical-scope exclusions are assessed separately. |
| Native organellar chromatophore intermembrane space UniProt causal check | passed | True | GO:0070115 | Read-only native command returned zero. No protein examples or typed molecular nodes. Positive molecular/pathway assertions and justified physical-scope exclusions are assessed separately. |
| Native organellar chromatophore membrane UniProt verify check | passed | True | GO:0070112 | Read-only native command returned zero. No protein examples or typed molecular nodes. Positive molecular/pathway assertions and justified physical-scope exclusions are assessed separately. |
| Native organellar chromatophore membrane UniProt causal check | passed | True | GO:0070112 | Read-only native command returned zero. No protein examples or typed molecular nodes. Positive molecular/pathway assertions and justified physical-scope exclusions are assessed separately. |
| Native organellar chromatophore outer membrane UniProt verify check | passed | True | GO:0070114 | Read-only native command returned zero. No protein examples or typed molecular nodes. Positive molecular/pathway assertions and justified physical-scope exclusions are assessed separately. |
| Native organellar chromatophore outer membrane UniProt causal check | passed | True | GO:0070114 | Read-only native command returned zero. No protein examples or typed molecular nodes. Positive molecular/pathway assertions and justified physical-scope exclusions are assessed separately. |
| Native organellar chromatophore thylakoid UniProt verify check | passed | True | GO:0070116 | Read-only native command returned zero. No protein examples or typed molecular nodes. Positive molecular/pathway assertions and justified physical-scope exclusions are assessed separately. |
| Native organellar chromatophore thylakoid UniProt causal check | passed | True | GO:0070116 | Read-only native command returned zero. No protein examples or typed molecular nodes. Positive molecular/pathway assertions and justified physical-scope exclusions are assessed separately. |
| Native organellar chromatophore thylakoid lumen UniProt verify check | passed | True | GO:0070117 | Read-only native command returned zero. No protein examples or typed molecular nodes. Positive molecular/pathway assertions and justified physical-scope exclusions are assessed separately. |
| Native organellar chromatophore thylakoid lumen UniProt causal check | passed | True | GO:0070117 | Read-only native command returned zero. No protein examples or typed molecular nodes. Positive molecular/pathway assertions and justified physical-scope exclusions are assessed separately. |
| Native organellar chromatophore thylakoid membrane UniProt verify check | passed | True | GO:0070118 | Read-only native command returned zero. No protein examples or typed molecular nodes. Positive molecular/pathway assertions and justified physical-scope exclusions are assessed separately. |
| Native organellar chromatophore thylakoid membrane UniProt causal check | passed | True | GO:0070118 | Read-only native command returned zero. No protein examples or typed molecular nodes. Positive molecular/pathway assertions and justified physical-scope exclusions are assessed separately. |
| Native osmiophilic body UniProt verify check | passed | True | GO:0044310 | Read-only native command returned zero. One unreviewed A0A059WIJ2/Pfg377 example and one COVERED typed node. Native identifier correspondence is separate from fragment scope, localization, source-specific genetic phenotypes and contradictory egress evidence. |
| Native osmiophilic body UniProt causal check | passed | True | GO:0044310 | Read-only native command returned zero. One unreviewed A0A059WIJ2/Pfg377 example and one COVERED typed node. Native identifier correspondence is separate from fragment scope, localization, source-specific genetic phenotypes and contradictory egress evidence. |
| Native parasitophorous vacuole UniProt verify check | passed | True | cellstructuremech:parasitophorous_vacuole | Read-only native command returned zero. No protein examples or typed molecular nodes. Positive molecular/pathway assertions and justified physical-scope exclusions are assessed separately. |
| Native parasitophorous vacuole UniProt causal check | passed | True | cellstructuremech:parasitophorous_vacuole | Read-only native command returned zero. No protein examples or typed molecular nodes. Positive molecular/pathway assertions and justified physical-scope exclusions are assessed separately. |
| Native parasitophorous vacuole lumen UniProt verify check | passed | True | cellstructuremech:parasitophorous_vacuole_lumen | Read-only native command returned zero. No protein examples or typed molecular nodes. Positive molecular/pathway assertions and justified physical-scope exclusions are assessed separately. |
| Native parasitophorous vacuole lumen UniProt causal check | passed | True | cellstructuremech:parasitophorous_vacuole_lumen | Read-only native command returned zero. No protein examples or typed molecular nodes. Positive molecular/pathway assertions and justified physical-scope exclusions are assessed separately. |

## Scientific And Domain Assessments

### Original native schema/render and unchanged input

schema: supported. Targets: GO:0070116.

Original validate/render exit0 and Markdown exact; current record matches the review frozen hash. No assigned target is stale. Schema validity is distinct from the scientific judgment.

### Exact identity, synonyms and anatomy

identity: supported. Targets: GO:0070116.

Exact GO0070116 definition matches; thylakoid GO0009579 is an is_a ancestor, whole chromatophore GO0070111 is part_of, lumen/membrane are constituent parts, and SL0354 is the exact location xref.

### Ontology versus native classification scope

scope: supported. Targets: GO:0070116.

Source hierarchy and textual definitions need separate attribution. GO generic thylakoid comment says it is not considered an organelle, whereas the repository native category explicitly includes thylakoids. The physical membrane-bounded lumen and native model support the retained structure_kind without an enum-only finding. GO0070112 definition emphasizes enclosing bilayers while its hierarchy also includes internal thylakoid membranes; current explicit hierarchy/SL support is retained without silently rewriting the source.

### Taxon identity and qualitative presence

scope: supported. Targets: GO:0070116.

P. chromatophora39717 species and canonical model identity agree with authority. Nowack2014 is secondary deposited-abstract context; Nowack2012 directly studies thylakoids/PSI in CCAC0185 M0880/a. COMMON is read qualitatively, not as a measured prevalence percentage or every-strain guarantee.

### Whole structure and collective lipid material

grounding: concern. Targets: GO:0070116.

A LIPID component is exactly grounded to whole membrane GO0070118 and linked from a STRUCTURE graph node. This is inherited F1, a confirmed whole-structure versus molecular-material identity mismatch. UNKNOWN essentiality does not cure the typing/grounding error.

### Positive photosynthetic light-complex evidence

evidence: supported. Targets: GO:0070116.

SL0354/SL0356 explicitly describe light-reaction complexes. Re-read Nowack2012 primary Results support PsaE thylakoid association and selected imported PSI subunits associating with purified PSI in one cultured P. chromatophora subisolate. These observations support the modest light-reaction-site claim without enumerating the complete photosystem/electron-transport chain.

### Exact source placement

evidence: concern. Targets: GO:0070116.

Inherited F2 persists at the component evidence and supports-edge evidence: GO0070118 defines a bilayer but does not state that it carries light-reaction complexes. Keep the true biology and cite SL0354/SL0356 or the scoped primary PSI result for that clause.

### Formation and complete composition remain unknown

evidence: unknown. Targets: GO:0070116.

Neither exact location authority nor the bounded primary localization/purification experiment establishes every lipid/protein identity, stoichiometry, cross-strain conservation or individual necessity for thylakoid formation. No missing optional protein examples or automatic protein-complex type defect is inferred.

### Complete descriptive graph and declared limits

graph: concern. Targets: GO:0070116.

Three NONMECHANISTIC edges: membrane bounds lumen, supports light reactions and is part of thylakoid. Topology and modest functional relation are supported; F1 component correspondence and F2 source note remain the two explicit corrections.

### Actual native protein verification coverage

provenance: supported. Targets: GO:0070116.

Both actual commands exit0 and independent full-record inventory confirms zero examples, zero typed molecular nodes and zero UniProtKB graph xrefs. Generic verify text alone is not treated as inventory evidence; empty native coverage is not biological completeness.

### Corrected positive pathway applicability assessment

scope: supported. Targets: GO:0070116.

Record positively asserts photosynthetic light-reaction complexes in component/function/graph narrative despite no individual protein inventory. Original absence-of-expression rationale is insufficient. Fresh full official catalogue contains no matched Paulinella host/strain, so source-specific SL/primary checks are the bounded fallback; no free-living cyanobacterial proxy or gene/module query is substituted. This completes applicability assessment, not a new native runner execution.

### No unrepresented image, measurement or protein assertion

scope: not_applicable. Targets: GO:0070116.

No maintained image or licence claim, numeric measurement, associated trait, verbatim snippet, individual gene/protein identity or representative protein example occurs. Current source read includes text captions only, not pixels, raw data or supplements. These optional domains are not filled by inference.

### History and context are not new issue dispositions

provenance: supported. Targets: GO:0070116.

Record retains PROPOSED status and historical curation events. Existing boundary/grounding discussion is read in its exact field scope. Frozen whole chromatophore is boundary context only; distinct whole-record issues or previous historical closures are not newly resolved by this review.

### Current scientific verdict

completeness: concern. Targets: GO:0070116.

needs_curation: retain exact inherited F1 major grounding and F2 minor source attribution, with two separately authorized curation actions. No new scientific finding.

### Original native schema/render and unchanged input

schema: supported. Targets: GO:0070117.

Original validate/render exit0 and Markdown exact; current record matches the review frozen hash. No assigned target is stale. Schema validity is distinct from the scientific judgment.

### Exact identity, synonyms and anatomy

identity: supported. Targets: GO:0070117.

Exact GO0070117 definition and Paulinella-type synonym match. GO0031978 plastid lumen parent is positively supported by SL0355 isA, even though it is absent from current GO is_a ancestry. Whole thylakoid parthood is separate from class membership.

### Ontology versus native classification scope

scope: supported. Targets: GO:0070117.

Source hierarchy and textual definitions need separate attribution. GO generic thylakoid comment says it is not considered an organelle, whereas the repository native category explicitly includes thylakoids. The physical membrane-bounded lumen and native model support the retained structure_kind without an enum-only finding. GO0070112 definition emphasizes enclosing bilayers while its hierarchy also includes internal thylakoid membranes; current explicit hierarchy/SL support is retained without silently rewriting the source.

### Taxon identity and qualitative presence

scope: supported. Targets: GO:0070117.

Paulinella39716 is a genus. Exact SL range supports the bounded organism context, and VARIABLE notes explicitly avoid asserting every genus member carries chromatophores. No numerical prevalence or all-species universal claim is introduced.

### Whole structure and collective lipid material

grounding: supported. Targets: GO:0070117.

No component inventory is asserted. Boundary membrane remains a STRUCTURE node without component_ref; it is not misrepresented as lumen material. Historical resolved boundary interpretation is consistent with current fields.

### Complete descriptive graph and declared limits

graph: supported. Targets: GO:0070117.

One NONMECHANISTIC edge: membrane encloses lumen. GO0070117 andSL0355 support the exact boundary; scope explicitly withholds lumenal proteins and photosynthetic proton-transport mechanisms. No source is silently promoted into a transport pathway.

### Actual native protein verification coverage

provenance: supported. Targets: GO:0070117.

Both actual commands exit0 and independent full-record inventory confirms zero examples, zero typed molecular nodes and zero UniProtKB graph xrefs. Generic verify text alone is not treated as inventory evidence; empty native coverage is not biological completeness.

### Genuine spatial-only applicability exclusion

scope: not_applicable. Targets: GO:0070117.

Full record asserts identity, spatial enclosure and qualitative occurrence only; it explicitly excludes lumenal proteins and photosynthetic proton transport. Therefore its original N/A outcome is genuine, clarified with actual scope instead of expression-only shorthand. Nested SL parent molecular prose is not an asserted child-record mechanism. No applicability defect or irrelevant gene query is manufactured.

### No unrepresented image, measurement or protein assertion

scope: not_applicable. Targets: GO:0070117.

No maintained image or licence claim, numeric measurement, associated trait, verbatim snippet, individual gene/protein identity or representative protein example occurs. Current source read includes text captions only, not pixels, raw data or supplements. These optional domains are not filled by inference.

### History and context are not new issue dispositions

provenance: supported. Targets: GO:0070117.

Record retains PROPOSED status and historical curation events. Existing boundary/grounding discussion is read in its exact field scope. Frozen whole chromatophore is boundary context only; distinct whole-record issues or previous historical closures are not newly resolved by this review.

### Current scientific verdict

completeness: supported. Targets: GO:0070117.

pass_with_limitations: current identity, topology and explicitly bounded assertions are supported; no inherited or new scientific finding. Retain source-tier, occurrence, native-empty-inventory and optional composition limits.

### Original native schema/render and unchanged input

schema: supported. Targets: GO:0070118.

Original validate/render exit0 and Markdown exact; current record matches the review frozen hash. No assigned target is stale. Schema validity is distinct from the scientific judgment.

### Exact identity, synonyms and anatomy

identity: supported. Targets: GO:0070118.

Exact GO0070118 definition and Paulinella-type synonym match. GO0042651 andGO0070112 are present in GO is_a ancestry; additional GO0055035 plastid membrane parent is explicitly supported by SL0356 isA. Whole thylakoid parthood is distinct.

### Ontology versus native classification scope

scope: supported. Targets: GO:0070118.

Source hierarchy and textual definitions need separate attribution. GO generic thylakoid comment says it is not considered an organelle, whereas the repository native category explicitly includes thylakoids. The physical membrane-bounded lumen and native model support the retained structure_kind without an enum-only finding. GO0070112 definition emphasizes enclosing bilayers while its hierarchy also includes internal thylakoid membranes; current explicit hierarchy/SL support is retained without silently rewriting the source.

### Taxon identity and qualitative presence

scope: supported. Targets: GO:0070118.

Paulinella39716 is a genus. Exact SL range supports the bounded organism context, and VARIABLE notes explicitly avoid asserting every genus member carries chromatophores. No numerical prevalence or all-species universal claim is introduced.

### Whole structure and collective lipid material

grounding: supported. Targets: GO:0070118.

One REVIEWED_LABEL_ONLY LIPID row explicitly denotes collective bilayer material and does not use whole-membrane GO as chemical grounding. ESSENTIAL refers to constitutive collective membrane material, not individual lipid/protein depletion or formation necessity. Exact chemical identity remains an explicit TODO without a fabricated CURIE.

### Positive photosynthetic light-complex evidence

evidence: supported. Targets: GO:0070118.

SL0354/SL0356 explicitly describe light-reaction complexes. Re-read Nowack2012 primary Results support PsaE thylakoid association and selected imported PSI subunits associating with purified PSI in one cultured P. chromatophora subisolate. These observations support the modest light-reaction-site claim without enumerating the complete photosystem/electron-transport chain.

### Exact source placement

evidence: supported. Targets: GO:0070118.

Component and supports-edge use GO0070118 only for the bilayer definition and explicitly cite SL0356 for light-reaction complexes. This exact source distinction avoids the separate whole-thylakoid record finding.

### Formation and complete composition remain unknown

evidence: unknown. Targets: GO:0070118.

Neither exact location authority nor the bounded primary localization/purification experiment establishes every lipid/protein identity, stoichiometry, cross-strain conservation or individual necessity for thylakoid formation. No missing optional protein examples or automatic protein-complex type defect is inferred.

### Complete descriptive graph and declared limits

graph: supported. Targets: GO:0070118.

Two NONMECHANISTIC edges: membrane bounds lumen and supports light reactions. GO supports topology andSL0356 the functional clause. The scope explicitly withholds a complete photosystem/electron-transport inventory.

### Actual native protein verification coverage

provenance: supported. Targets: GO:0070118.

Both actual commands exit0 and independent full-record inventory confirms zero examples, zero typed molecular nodes and zero UniProtKB graph xrefs. Generic verify text alone is not treated as inventory evidence; empty native coverage is not biological completeness.

### Corrected positive pathway applicability assessment

scope: supported. Targets: GO:0070118.

Record positively asserts photosynthetic light-reaction complexes in component/function/graph narrative despite no individual protein inventory. Original absence-of-expression rationale is insufficient. Fresh full official catalogue contains no matched Paulinella host/strain, so source-specific SL/primary checks are the bounded fallback; no free-living cyanobacterial proxy or gene/module query is substituted. This completes applicability assessment, not a new native runner execution.

### No unrepresented image, measurement or protein assertion

scope: not_applicable. Targets: GO:0070118.

No maintained image or licence claim, numeric measurement, associated trait, verbatim snippet, individual gene/protein identity or representative protein example occurs. Current source read includes text captions only, not pixels, raw data or supplements. These optional domains are not filled by inference.

### History and context are not new issue dispositions

provenance: supported. Targets: GO:0070118.

Record retains PROPOSED status and historical curation events. Existing boundary/grounding discussion is read in its exact field scope. Frozen whole chromatophore is boundary context only; distinct whole-record issues or previous historical closures are not newly resolved by this review.

### Current scientific verdict

completeness: supported. Targets: GO:0070118.

pass_with_limitations: current identity, topology and explicitly bounded assertions are supported; no inherited or new scientific finding. Retain source-tier, occurrence, native-empty-inventory and optional composition limits.

### Immutable original and current source checks

schema: supported. Targets: GO:0044310.

Exact target unchanged. Original pair passes native validation/deterministic rendering and15historical hashes; current accession coverage retains actual empty/populated scope. Root owns full local gates and publication.

### Immutable original and current source checks

schema: supported. Targets: cellstructuremech:parasitophorous_vacuole.

Exact target unchanged. Original pair passes native validation/deterministic rendering and15historical hashes; current accession coverage retains actual empty/populated scope. Root owns full local gates and publication.

### Immutable original and current source checks

schema: supported. Targets: cellstructuremech:parasitophorous_vacuole_lumen.

Exact target unchanged. Original pair passes native validation/deterministic rendering and15historical hashes; current accession coverage retains actual empty/populated scope. Root owns full local gates and publication.

### Exact osmiophilic secretory vesicle

identity: supported. Targets: GO:0044310.

GO0044310 exact current definition and direct0031410 parent agree. Record denotes organelle, not protein or phenotype. The definition explicitly calls content-release aid postulated; this historical ontology wording is not itself a demonstrated-mechanism claim.

### Boundary material and protein component

grounding: supported. Targets: GO:0044310.

Label-only collective membrane has no incorrectly applied whole-membrane chemical CURIE. Pfg377 association is supported by1995 primary abstract immunoelectron localization and2016 body. No precise lipid species or complete protein inventory is claimed.

### Actual Pfg377 accession identity and limits

grounding: supported. Targets: GO:0044310.

A0A059WIJ2 matches pfg377/taxon5833/UNREVIEWED.193-aa G1 fragment is not full-length experimental3D7 protein, but maintained example explicitly only establishes gene identity. No mandatory replacement or new instance defect follows.

### Family mapping remains bounded unknown

grounding: unknown. Targets: GO:0044310.

Exact InterPro association request204 provides no usable family list; reviewed-gene query returns0. PANTHER crossreferences are not verified here as exact source-neutral class. No guessed grounding or exhaustive family-absence claim.

### Normal complement versus absolute formation

scope: supported. Targets: GO:0044310.

Membrane ESSENTIAL is definitional boundary, not experimentally demonstrated particular lipid necessity. Protein UNKNOWN essentiality remains conservative: depleted bodies and residual abnormal granules distinguish normal complement from absolute no-organelle formation.

### Female-gametocyte and experimental strain context

scope: supported. Targets: GO:0044310.

Species5833 correct; COMMON explicitly scoped mature female gametocytes, not all cells.1995/2016 experiments are3D7 context; native sequenceG1 is separately labeled representative identity.2008 historical canonical example is tied to its specific source.

### Inherited unqualified egress explanation conflicts with cited evidence

graph: concern. Targets: GO:0044310.

Record functions0/general graph description/edge3 and emergence explanation for oocyst defect do not reconcile its cited2016 normal-egress finding in independent OB-depleted clones. NONMECHANISTIC label avoids physical secretion proof but not this material functional overstatement. Preserve exact inheritedmajor key,2008 observation and qualified2016 timing.

### Supported edges and infection association survive

graph: supported. Targets: GO:0044310.

Membrane bounds organelle, Pfg377 associates with it and supports normal-body complement; these edges remain supported. Both studies report strong mosquito infection impairment.2016 does not prove an alternative direct post-egress mechanism or refute all possible kinetic/strain-dependent contributions.

### Positive protein and transmission pathway triggers

evidence: supported. Targets: GO:0044310.

Pfg377 gene/accession, knockout phenotype and egress/transmission claims trigger native structured-source assessment. Current catalogue has no matched Plasmodium host; downstream queries not applicable after real coverage check. Original no-expression exemption needs linked-review correction.

### Primary access and phenotype bounds

evidence: unknown. Targets: GO:0044310.

Alano/deKoning full bodies not obtained, complete primary abstracts read. Suarez declared Methods/Results/Discussion plusFig1caption only; no pixels/supplements/raw proteomics.15-minute assay does not resolve every transient kinetic effect. Additional OB proteins are optional, not invented completeness findings.

### Exact apicomplexan PV versus broad GO

identity: supported. Targets: cellstructuremech:parasitophorous_vacuole.

SL0194 specifically scopes host-cell vacuole to most apicomplexans. Broader GO0020003 definition includes general symbionts despite exact lexical PV synonym, so local narrow identity plus GO parent remains defensible.

### Whole vacuole membrane and lumen boundaries

graph: supported. Targets: cellstructuremech:parasitophorous_vacuole.

Local PVM and lumen identifiers resolve in frozen contexts. Single NONMECHANISTIC bounds edge and has_part links agree with exact SL0193/0341; no secretory mechanism or molecular component essentiality is asserted by graph.

### Qualitative niche and Toxoplasma example

scope: supported. Targets: cellstructuremech:parasitophorous_vacuole.

Apicomplexa COMMON is expressly most-parasite qualitative scope, not universal every stage. Clough secondary abstract supports Toxoplasma interface/replication niche; Lingelbach secondary abstract supports invasion-associated surrounding membrane. No complete primary nutrient/permeability mechanism is certified.

### Inherited BioID experimental taxon mismatch

evidence: concern. Targets: cellstructuremech:parasitophorous_vacuole.

Canonical example1 says P.falciparum BioID with Schnider2018. Exact primary abstract/JATS identify P.berghei ANKA mCherryHsp70 blood-stage experiment. P.falciparum orthologs and earlier literature are separate comparisons, not experiment provenance; preserve inheritedmajor key.

### Proximity candidates are not complete composition or necessity

evidence: supported. Targets: cellstructuremech:parasitophorous_vacuole.

Schnider lists61candidates; off-target PV/PPM labeling and secretion transit are explicit. This validates bounded survey provenance, not membership/necessity of all candidates in whole PV or every species. Correcting taxon does not entail importing61components or new causal mechanisms.

### Positive BioID PVM protein assertion triggers coverage

evidence: supported. Targets: cellstructuremech:parasitophorous_vacuole.

Although no molecular component inventory exists and graph is topology-only, canonical example positively asserts a PVM protein survey and replication niche. Whole-record molecular assertion triggers applicability. Official catalogue has no Plasmodium/Toxoplasma match; no foreign-host query/negative inference.

### Historical fixes and neighboring evidence remain separate

provenance: supported. Targets: cellstructuremech:parasitophorous_vacuole.

Historical820–822 and resolved membrane-identity TODO are not terminally re-adjudicated. Frozen neighbor used for exact boundary context only; this successor fixes no neighbor record or broader issue. Original scientific observations remain immutable.

### Primary versus secondary source coverage

evidence: unknown. Targets: cellstructuremech:parasitophorous_vacuole.

Schnider only declared Results/Discussion/Methods and embedded captions read; no pixels/supplementary files or quantitative reanalysis. Lingelbach/Clough are complete secondary abstracts only; blocked/redirect pages do not certify full text.

### Exact PV lumen with broader vacuolar-space parent

identity: supported. Targets: cellstructuremech:parasitophorous_vacuole_lumen.

SL0341 exact definition/synonym and partOfPV agree. GO0020004 broadly denotes space between symbiont plasma membrane and enclosing vacuole membrane. Neither broad synonym nor definition warrants collapsing narrow local apicomplexan lumen identity.

### One descriptive lumen parthood edge

graph: supported. Targets: cellstructuremech:parasitophorous_vacuole_lumen.

Internal compartment and local PV parthood are explicit in native location authority; bounded region is not the whole membrane or parasite. Graph specifically excludes residence, nutrient access and remodeling mechanisms.

### Qualitative apicomplexan context

scope: supported. Targets: cellstructuremech:parasitophorous_vacuole_lumen.

ENA verifies phylum5794. COMMON explicitly inherits most-apicomplexan location definition; not every stage/cell or a quantitative frequency. No canonical strain, protein essentiality or dimensions asserted.

### Genuine physical and topology exclusion

evidence: not_applicable. Targets: cellstructuremech:parasitophorous_vacuole_lumen.

Whole positive content concerns exact region, boundaries and qualitative host context. Molecular mechanisms/functions were explicitly removed/excluded; neighboring protein survey is not inherited as lumen content. Original exclusion remains appropriate with precise scope rationale, no bundle defect.

### No mandatory molecular contents or mechanism

evidence: supported. Targets: cellstructuremech:parasitophorous_vacuole_lumen.

Empty optional components/functions/examples are not material defects in deliberately limited region record. Historical824/825 mentions are provenance, not current blanket closure or re-adjudication. Lumen has no inherited scientific finding.

### Exact identity, synonyms, subtype and parthood

identity: supported. Targets: GO:0070113.

GO0070113 and SL0359 exactly identify the inner stroma-facing bilayer. GO supports chromatophore-membrane subclass; UniProt explicitly supplies plastid-inner-membrane parent and chromatophore parthood. No absent GO plastid edge is fabricated.

### Material constituent distinct from complete anatomical identity

grounding: supported. Targets: GO:0070113.

Single LIPID/CONSTITUENT is the collective bilayer material, REVIEWED_LABEL_ONLY with notes and no whole-membrane GO chemical grounding. Anatomical GO identities remain on the record/structure nodes. No precise lipid complement is invented.

### Constitutive material versus experimental formation necessity

evidence: unknown. Targets: GO:0070113.

ESSENTIAL is supported only for the defining collective bilayer, not an individual lipid species or protein. No particular molecular formation requirement is asserted or established by these sources.

### Every edge, node and scope

graph: supported. Targets: GO:0070113.

Two NONMECHANISTIC edges: inner membrane bounds stroma and delimits intermembrane space. SL0359 expressly describes the separation. Label-only stroma node is coherent; current SL0353 is optional enrichment, not a new source claim or historical correction.

### Verified genus and qualitative variable occurrence

scope: supported. Targets: GO:0070113.

Paulinella39716 genus is correct. Explicit VARIABLE avoids claiming every species has chromatophores; secondary Gabr S2 distinguishes photosynthetic and heterotrophic lineages. Primary Nowack culture is CCAC0185/subisolateM0880/a, not a genus-wide sample. No frequency estimate or experimental strain substitution.

### Whole-record structured-source applicability

evidence: not_applicable. Targets: GO:0070113.

Full target asserts material anatomy and localization scope, with no named protein/regulator/pathway/stress-response claim. Inner/outer explicitly withhold import and photosynthetic machinery; generic fallback scope is not an asserted protein inventory. The original exclusion is genuine despite its generic expression-only explanation.

### Exact authorities and bounded primary/secondary context

evidence: supported. Targets: GO:0070113.

All maintained citations are GO/UniProt-location authorities for anatomical identity/topology. Current primary Nowack body reread is only the declared sections/captions, with actual earlier retrieval time; Gabr fresh S2 body is secondary context. No source pixels, unlisted sections, molecular assembly assay or compulsory protein completeness claimed.

### Original hashes, native validation/render and current protein coverage

schema: supported. Targets: GO:0070113.

All68 old input entries verify at retained source, all4 old pairs validate/render exactly and target hash remains unchanged. Current verify/causal commands exit0 with zero examples and zero typed protein nodes; not evidence of molecular completeness.

### Historical rationale and scientific status

provenance: supported. Targets: GO:0070113.

Full record history/discussions retained; PROPOSED status unchanged. Label-only material grounding TODOs remain bounded optional identity questions; no empty-slot defect or whole-issue resolution inferred. Historical removal of unavailableSL0353 is not retroactively false because it resolves now.

### Complete record, absent optional claim surfaces and verdict

completeness: supported. Targets: GO:0070113.

Entire current record read: no images, physical-measurement objects, individual protein accessions, gene symbols, complex-composition inventory or verbatim quotations require extra checks. No supported scientific or review-bundle defect observed. Qualified pass retains chemical, assembly, prevalence and source-access limits; no inherited findings exist.

### Exact identity, synonyms, subtype and parthood

identity: supported. Targets: GO:0070115.

GO0070115 and SL0360 exactly identify the region between two envelope bilayers. UniProt supplies plastid-intermembrane-space parent; GO and UniProt support chromatophore containment. Stroma and thylakoid lumen remain distinct.

### Material constituent distinct from complete anatomical identity

grounding: supported. Targets: GO:0070115.

Residual wall is PEPTIDOGLYCAN/CONSTITUENT, REVIEWED_LABEL_ONLY with explicit rationale and no guessed chemical or whole-space CURIE. Source places residual peptidoglycan between membranes; exact layer chemistry remains unasserted.

### Constitutive material versus experimental formation necessity

evidence: unknown. Targets: GO:0070115.

UNKNOWN essentiality is retained for the residual wall: placement does not establish whether the intermembrane space forms without it.

### Every edge, node and scope

graph: supported. Targets: GO:0070115.

Three NONMECHANISTIC edges: outer/inner membranes delimit the space and residual peptidoglycan resides there. SL0351 supports the layer placement, SL0359/0360 and GO0070115 support boundaries. Component_ref points to the labeled wall material, not to the entire compartment as chemistry.

### Verified genus and qualitative variable occurrence

scope: supported. Targets: GO:0070115.

Paulinella39716 genus is correct. Explicit VARIABLE avoids claiming every species has chromatophores; secondary Gabr S2 distinguishes photosynthetic and heterotrophic lineages. Primary Nowack culture is CCAC0185/subisolateM0880/a, not a genus-wide sample. No frequency estimate or experimental strain substitution.

### Whole-record structured-source applicability

evidence: not_applicable. Targets: GO:0070115.

Full target asserts only physical boundaries and residual-wall placement; positively withholds import/remodeling/protein inventories. SL0351 background description of the parent photosynthetic organelle does not convert this compartment-topology record into a pathway assertion.

### Exact authorities and bounded primary/secondary context

evidence: supported. Targets: GO:0070115.

All maintained citations are GO/UniProt-location authorities for anatomical identity/topology. Current primary Nowack body reread is only the declared sections/captions, with actual earlier retrieval time; Gabr fresh S2 body is secondary context. No source pixels, unlisted sections, molecular assembly assay or compulsory protein completeness claimed.

### Original hashes, native validation/render and current protein coverage

schema: supported. Targets: GO:0070115.

All68 old input entries verify at retained source, all4 old pairs validate/render exactly and target hash remains unchanged. Current verify/causal commands exit0 with zero examples and zero typed protein nodes; not evidence of molecular completeness.

### Historical rationale and scientific status

provenance: supported. Targets: GO:0070115.

Full record history/discussions retained; PROPOSED status unchanged. Label-only material grounding TODOs remain bounded optional identity questions; no empty-slot defect or whole-issue resolution inferred. No historical closed issue is terminally disposed by this review.

### Complete record, absent optional claim surfaces and verdict

completeness: supported. Targets: GO:0070115.

Entire current record read: no images, physical-measurement objects, individual protein accessions, gene symbols, complex-composition inventory or verbatim quotations require extra checks. No supported scientific or review-bundle defect observed. Qualified pass retains chemical, assembly, prevalence and source-access limits; no inherited findings exist.

### Exact identity, synonyms, subtype and parthood

identity: supported. Targets: GO:0070112.

GO0070112 and SL0352 exactly identify generic membrane localization. GO definition says surrounding bilayers but its own explicit is_a children and SL0352 include thylakoid membrane in the fallback class; this is not a new unsupported biological generalization. GO0030659 parent and chromatophore parthood verified.

### Material constituent distinct from complete anatomical identity

grounding: supported. Targets: GO:0070112.

Single LIPID/CONSTITUENT is the collective bilayer material, REVIEWED_LABEL_ONLY with notes and no whole-membrane GO chemical grounding. Anatomical GO identities remain on the record/structure nodes. No precise lipid complement is invented.

### Constitutive material versus experimental formation necessity

evidence: unknown. Targets: GO:0070112.

ESSENTIAL is supported only for the defining collective bilayer, not an individual lipid species or protein. No particular molecular formation requirement is asserted or established by these sources.

### Every edge, node and scope

graph: supported. Targets: GO:0070112.

Four NONMECHANISTIC edges: generic membrane part_of chromatophore, with inner, outer and thylakoid membranes as is_a subclasses. Exact GO typed children and SL0352 support the scope; no unknown protein localization is assigned to a specific membrane.

### Verified genus and qualitative variable occurrence

scope: supported. Targets: GO:0070112.

Paulinella39716 genus is correct. Explicit VARIABLE avoids claiming every species has chromatophores; secondary Gabr S2 distinguishes photosynthetic and heterotrophic lineages. Primary Nowack culture is CCAC0185/subisolateM0880/a, not a genus-wide sample. No frequency estimate or experimental strain substitution.

### Whole-record structured-source applicability

evidence: not_applicable. Targets: GO:0070112.

Full target asserts material anatomy and localization scope, with no named protein/regulator/pathway/stress-response claim. Inner/outer explicitly withhold import and photosynthetic machinery; generic fallback scope is not an asserted protein inventory. The original exclusion is genuine despite its generic expression-only explanation.

### Exact authorities and bounded primary/secondary context

evidence: supported. Targets: GO:0070112.

All maintained citations are GO/UniProt-location authorities for anatomical identity/topology. Current primary Nowack body reread is only the declared sections/captions, with actual earlier retrieval time; Gabr fresh S2 body is secondary context. No source pixels, unlisted sections, molecular assembly assay or compulsory protein completeness claimed.

### Original hashes, native validation/render and current protein coverage

schema: supported. Targets: GO:0070112.

All68 old input entries verify at retained source, all4 old pairs validate/render exactly and target hash remains unchanged. Current verify/causal commands exit0 with zero examples and zero typed protein nodes; not evidence of molecular completeness.

### Historical rationale and scientific status

provenance: supported. Targets: GO:0070112.

Full record history/discussions retained; PROPOSED status unchanged. Label-only material grounding TODOs remain bounded optional identity questions; no empty-slot defect or whole-issue resolution inferred. Generic scope resolution remains separate from open material grounding.

### Complete record, absent optional claim surfaces and verdict

completeness: supported. Targets: GO:0070112.

Entire current record read: no images, physical-measurement objects, individual protein accessions, gene symbols, complex-composition inventory or verbatim quotations require extra checks. No supported scientific or review-bundle defect observed. Qualified pass retains chemical, assembly, prevalence and source-access limits; no inherited findings exist.

### Exact identity, synonyms, subtype and parthood

identity: supported. Targets: GO:0070114.

GO0070114 and SL0361 exactly identify cytoplasm-facing outer bilayer. GO chromatophore-membrane subclass and UniProt plastid-outer-membrane parent/parthood are distinct verified relationships.

### Material constituent distinct from complete anatomical identity

grounding: supported. Targets: GO:0070114.

Single LIPID/CONSTITUENT is the collective bilayer material, REVIEWED_LABEL_ONLY with notes and no whole-membrane GO chemical grounding. Anatomical GO identities remain on the record/structure nodes. No precise lipid complement is invented.

### Constitutive material versus experimental formation necessity

evidence: unknown. Targets: GO:0070114.

ESSENTIAL is supported only for the defining collective bilayer, not an individual lipid species or protein. No particular molecular formation requirement is asserted or established by these sources.

### Every edge, node and scope

graph: supported. Targets: GO:0070114.

One NONMECHANISTIC bounds edge locates the outer host-cytoplasm-facing bilayer as chromatophore outer boundary. It does not equate the inner or thylakoid membrane with the exterior boundary or posit transport machinery.

### Verified genus and qualitative variable occurrence

scope: supported. Targets: GO:0070114.

Paulinella39716 genus is correct. Explicit VARIABLE avoids claiming every species has chromatophores; secondary Gabr S2 distinguishes photosynthetic and heterotrophic lineages. Primary Nowack culture is CCAC0185/subisolateM0880/a, not a genus-wide sample. No frequency estimate or experimental strain substitution.

### Whole-record structured-source applicability

evidence: not_applicable. Targets: GO:0070114.

Full target asserts material anatomy and localization scope, with no named protein/regulator/pathway/stress-response claim. Inner/outer explicitly withhold import and photosynthetic machinery; generic fallback scope is not an asserted protein inventory. The original exclusion is genuine despite its generic expression-only explanation.

### Exact authorities and bounded primary/secondary context

evidence: supported. Targets: GO:0070114.

All maintained citations are GO/UniProt-location authorities for anatomical identity/topology. Current primary Nowack body reread is only the declared sections/captions, with actual earlier retrieval time; Gabr fresh S2 body is secondary context. No source pixels, unlisted sections, molecular assembly assay or compulsory protein completeness claimed.

### Original hashes, native validation/render and current protein coverage

schema: supported. Targets: GO:0070114.

All68 old input entries verify at retained source, all4 old pairs validate/render exactly and target hash remains unchanged. Current verify/causal commands exit0 with zero examples and zero typed protein nodes; not evidence of molecular completeness.

### Historical rationale and scientific status

provenance: supported. Targets: GO:0070114.

Full record history/discussions retained; PROPOSED status unchanged. Label-only material grounding TODOs remain bounded optional identity questions; no empty-slot defect or whole-issue resolution inferred. No historical closed issue is terminally disposed by this review.

### Complete record, absent optional claim surfaces and verdict

completeness: supported. Targets: GO:0070114.

Entire current record read: no images, physical-measurement objects, individual protein accessions, gene symbols, complex-composition inventory or verbatim quotations require extra checks. No supported scientific or review-bundle defect observed. Qualified pass retains chemical, assembly, prevalence and source-access limits; no inherited findings exist.

### Complete frozen-input comparison and bounded refresh

provenance: supported. Targets: GO:0070113, GO:0070115, GO:0070112, GO:0070114, GO:0070116, GO:0070117, GO:0070118, GO:0044310, cellstructuremech:parasitophorous_vacuole, cellstructuremech:parasitophorous_vacuole_lumen.

0 of ten original target hashes differ from current main. The changed content is substantively reassessed in the target-specific assessments; original observations remain historical and unchanged. All current target and used context bytes are frozen.

## Findings

### septin-organellar_chromatophore_thylakoid-F1: Separate whole membrane identity from lipid material

major / open / confirmed; issue key: chromatophore-thylakoid-whole-membrane-lipid.

The LIPID component is labelled and grounded to the entire organellar chromatophore thylakoid membrane GO0070118. The graph structural node carries a component_ref to this row. GO identifies a whole anatomical membrane, not a lipid entity.

### septin-organellar_chromatophore_thylakoid-F2: Use the source that establishes the light-complex claim

minor / open / confirmed; issue key: chromatophore-thylakoid-go-light-complex-attribution.

The component and photosynthesis edge say GO0070118 defines a membrane carrying light-reaction complexes. Its native definition identifies only the bilayer compartment. SL0354 already cited by the function, and the independently inspected Nowack2012 primary study, support the biological statement.

### plaque-t7-F1: Reconcile the emergence pathway with the cited2016 counterevidence

major / open / confirmed; issue key: osmiophilic-body-unreconciled-pfg377-egress-counterevidence.

The record presents reduced emergence as a general consequence of Pfg377-dependent body depletion and as the route to poor mosquito infection. Its own cited2016 study generated new pfg377 knockouts with depleted bodies, observed normal measured egress, and retained severe mosquito infection defects. That study explicitly reports failure to reproduce the earlier egress phenotype. The record therefore needs source- and condition-specific qualification rather than the current unqualified functional pathway. This does not refute Pfg377 localization, normal-body biogenesis, mosquito infection support or the explicitly postulated GO definition.

### plaque-t8-F1: Correct the species attached to the cited BioID canonical example

major / open / confirmed; issue key: parasitophorous-vacuole-bioid-canonical-species-misattribution.

canonical_examples[1] assigns the Schnider2018 BioID survey to Plasmodium falciparum5833. The cited primary paper performed that survey in P. berghei blood stages and states the ANKA mCherryHsp70 experimental background. Its comparisons with P. falciparum orthologs and previous studies do not support the maintained claim that this survey used P. falciparum.

## Recommended Actions And Acceptance Checks

### septin-organellar_chromatophore_thylakoid-A1

Preserve supported membrane topology. Retain a whole structural constituent with an appropriate type, or describe supported lipid material separately with exact chemical grounding or justified reviewed-label-only status; align the component_ref accordingly.

- Verify each amended type and source note against the exact native definition or primary passage.
- After separately authorized curation, run focused schema, strict, graph and label validation.

### septin-organellar_chromatophore_thylakoid-A2

Restrict the GO note to its membrane definition and attach the light-complex claim to SL0354 and/or the relevant primary thylakoid photosystem evidence.

- Verify each amended type and source note against the exact native definition or primary passage.
- After separately authorized curation, run focused schema, strict, graph and label validation.

### plaque-t7-A1

In separately authorized curation, explicitly distinguish the2008 emergence result from the2016 non-reproduction in defined3D7 knockout clones. Qualify or remove the general body-abundance-to-emergence assertion and its explanation of the oocyst defect. Preserve supported Pfg377/body biogenesis and mosquito infection association, and retain uncertainty about the post-egress causal step without inventing a replacement mechanism.

- Both cited studies and their differing assay/context results are represented honestly.
- No unqualified graph/function assertion treats poor egress as the established explanation of the Pfg377-associated mosquito defect.
- Correct GO identity, membrane topology, Pfg377 membership and qualified transmission association remain intact.
- Native schema, strict, identifier, protein, graph and history gates pass after authorized curation.

### plaque-t8-A1

In separately authorized curation, align this canonical example with the actual P. berghei study, using verified taxon5821 and the appropriate experimental background, or replace the citation and note with independently inspected P. falciparum-specific experimental evidence. Preserve the broader apicomplexan identity and valid Toxoplasma example.

- The taxon, note and cited experiment identify the same parasite species.
- P. berghei ANKA study data are not relabeled as P. falciparum data; orthology is distinguished from experimental provenance.
- PV identity, PVM/lumen boundary links and valid niche claims remain unchanged.
- Native schema, strict, taxon/identifier and history checks pass after authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| current-record-0 | data/structures/membrane_organelle/organellar_chromatophore_inner_membrane.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 e3c244a36b1484e5d3ca95aa114de0a719660aa4d76ae1811ed12584b3d72b1e; current SHA256 e3c244a36b1484e5d3ca95aa114de0a719660aa4d76ae1811ed12584b3d72b1e. Record bytes unchanged since the original review. |
| original-review-0 | reviews/structured/20261022T030049Z-organellar-chromatophore-inner-membrane-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-1 | data/structures/membrane_organelle/organellar_chromatophore_intermembrane_space.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 f67ae10cda248a93eba761943f430c0ea5e6d4550dcf9514611822866d2c98ed; current SHA256 f67ae10cda248a93eba761943f430c0ea5e6d4550dcf9514611822866d2c98ed. Record bytes unchanged since the original review. |
| original-review-1 | reviews/structured/20261022T030050Z-organellar-chromatophore-intermembrane-space-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-2 | data/structures/membrane_organelle/organellar_chromatophore_membrane.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 179b7a8a2519cb216889baed1305e54b1de332688cbb7bac1c24857f1209a794; current SHA256 179b7a8a2519cb216889baed1305e54b1de332688cbb7bac1c24857f1209a794. Record bytes unchanged since the original review. |
| original-review-2 | reviews/structured/20261022T030051Z-organellar-chromatophore-membrane-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-3 | data/structures/membrane_organelle/organellar_chromatophore_outer_membrane.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 f7d415a8e211d48ef9ecf5f0bb1b96a0ac3336c1ce6498d78d9bf0033bce3c11; current SHA256 f7d415a8e211d48ef9ecf5f0bb1b96a0ac3336c1ce6498d78d9bf0033bce3c11. Record bytes unchanged since the original review. |
| original-review-3 | reviews/structured/20261022T030052Z-organellar-chromatophore-outer-membrane-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-4 | data/structures/membrane_organelle/organellar_chromatophore_thylakoid.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 6ce01ac746d2a475719c41e8eea903b510d96648cff04a1338248feb3558731a; current SHA256 6ce01ac746d2a475719c41e8eea903b510d96648cff04a1338248feb3558731a. Record bytes unchanged since the original review. |
| original-review-4 | reviews/structured/20261022T030053Z-organellar-chromatophore-thylakoid-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-5 | data/structures/membrane_organelle/organellar_chromatophore_thylakoid_lumen.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 6d012bda5b45cabee640a9a066a9ceb0f0a61e1b26d13214370ad299b185c2fa; current SHA256 6d012bda5b45cabee640a9a066a9ceb0f0a61e1b26d13214370ad299b185c2fa. Record bytes unchanged since the original review. |
| original-review-5 | reviews/structured/20261022T030054Z-organellar-chromatophore-thylakoid-lumen-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-6 | data/structures/membrane_organelle/organellar_chromatophore_thylakoid_membrane.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 67a0433476fdb5ca77a1a30bb921d4d80603a5ae1c61869162edf87f07d6364b; current SHA256 67a0433476fdb5ca77a1a30bb921d4d80603a5ae1c61869162edf87f07d6364b. Record bytes unchanged since the original review. |
| original-review-6 | reviews/structured/20261022T030055Z-organellar-chromatophore-thylakoid-membrane-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-7 | data/structures/membrane_organelle/osmiophilic_body.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 12985dc29b3e81008d138f3de6e0e10b93090ff200e538a105f24a7c171bfafc; current SHA256 12985dc29b3e81008d138f3de6e0e10b93090ff200e538a105f24a7c171bfafc. Record bytes unchanged since the original review. |
| original-review-7 | reviews/structured/20261022T030055Z-osmiophilic-body-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-8 | data/structures/membrane_organelle/parasitophorous_vacuole.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 bc5b288dc20d549717192249a6d0889856bdaf66fe33b61cd213b503f4d6f610; current SHA256 bc5b288dc20d549717192249a6d0889856bdaf66fe33b61cd213b503f4d6f610. Record bytes unchanged since the original review. |
| original-review-8 | reviews/structured/20261022T030057Z-parasitophorous-vacuole-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-9 | data/structures/membrane_organelle/parasitophorous_vacuole_lumen.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 4a2a0820584215f4a76152f44d66e365ed67a663527da333d2e6c00d24bc244f; current SHA256 4a2a0820584215f4a76152f44d66e365ed67a663527da333d2e6c00d24bc244f. Record bytes unchanged since the original review. |
| original-review-9 | reviews/structured/20261022T030057Z-parasitophorous-vacuole-lumen-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| septin-review-policy | .claude/skills/review-yaml-record/SKILL.md; Whole-record assertions, structured sources and severity rubric | supports | Positive molecular/pathway assertions require a real applicability assessment; absence of expression claims alone is not an exemption. Keep source scope, uncertainty and original finding identity; record curation is separate. |
| septin-curation-policy | docs/CURATION.md; Structural components, molecular grounding and family-or-class guidance | supports | Whole assembled membranes are structures; a LIPID component denotes molecular material and cannot use a complete membrane identity as exact chemical grounding. Taxon-agnostic protein families OR classes are permitted. An optional example inventory is not automatically required for every generic class. |
| septin-schema-policy | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, ComponentTypeEnum and grounding contract | supports | Molecular components and whole structures have different identities. Label-only supported lipid material is possible without inventing exact chemical composition. PROTEIN enum prose is interpreted with explicit CURATION generic-class permission; no automatic complex assertion follows from a heterogeneous class. |
| septin-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Graph nodes, component correspondence, source scope and necessity | supports | Descriptive boundary graphs can remain NONMECHANISTIC; source-specific localization, molecular identity and organelle-formation necessity must not be conflated. |
| septin-protein-policy | .claude/skills/uniprot-protein-examples/SKILL.md; Step2 generic classes and native coverage report | supports | Generic class components are explicitly recognized. A zero-example inventory or NO_GENE_SYMBOLS node is a stated coverage limit, not proof that the protein class does not exist or that its members form one stable complex. |
| septin-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0070116,GO:0070117,GO:0070118,GO:0009579,GO:0031977,GO:0031978,GO:0042651,GO:0055035,GO:0070112,GO:0019684,GO:0070111; All eleven exact GO entries: identifiers, definitions, synonyms, comments and immediate child relations | supports | GO0070116 is a thylakoid in an organellar chromatophore; GO0070117 is its enclosed volume and GO0070118 its lipid-bilayer membrane. GO0070118 does not itself say that the membrane carries light-reaction complexes. GO0019684 is the light-reaction process. Whole anatomical membrane identifiers are not exact chemical lipid identities. Generic GO0009579 comment excludes the word organelle while native repository category guidance explicitly includes thylakoids; this vocabulary tension is retained without inventing a type error. |
| septin-SL0354 | https://rest.uniprot.org/locations/SL-0354.json; Complete exact UniProt location JSON, including nested isA/partOf fields and GO cross-references | supports | Exact thylakoid definition explicitly describes internal interconnected membranes carrying complexes for photosynthetic light reactions; its identity, Paulinella range and whole-chromatophore parthood match. Nested parent molecular prose is not automatically assigned to a child spatial compartment; location protein statistics do not establish biological absence. |
| septin-SL0355 | https://rest.uniprot.org/locations/SL-0355.json; Complete exact UniProt location JSON, including nested isA/partOf fields and GO cross-references | supports | Exact lumen is bounded by thylakoid membrane, maps GO0070117, isA plastid thylakoid lumen SL0309/GO0031978 and partOf thylakoid; Paulinella range does not imply every genus member has chromatophores. Nested parent molecular prose is not automatically assigned to a child spatial compartment; location protein statistics do not establish biological absence. |
| septin-SL0356 | https://rest.uniprot.org/locations/SL-0356.json; Complete exact UniProt location JSON, including nested isA/partOf fields and GO cross-references | supports | Exact membrane maps GO0070118, describes light-reaction complexes, isA plastid thylakoid membrane SL0216/GO0055035 and partOf thylakoid; Paulinella range is qualitative. Nested parent molecular prose is not automatically assigned to a child spatial compartment; location protein statistics do not establish biological absence. |
| septin-tax39716 | https://rest.uniprot.org/taxonomy/39716.json; Complete current taxonomy identity, active status, rank and lineage | supports | NCBITaxon39716 is active Paulinella at genus rank. Taxon identity alone does not establish numerical frequency or universal organelle presence. |
| septin-GO0070116-isa | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0070116/ancestors?relations=is_a; Complete exact QuickGO ancestors response with relations=is_a | supports | GO0009579 is among thylakoid is_a ancestors. This response is a bounded ontology hierarchy observation, not an experimental mechanism or exhaustive source consensus. |
| septin-GO0070117-isa | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0070117/ancestors?relations=is_a; Complete exact QuickGO ancestors response with relations=is_a | supports | GO0031977 generic thylakoid lumen occurs, but GO0031978 plastid thylakoid lumen is not among the returned is_a ancestors; the latter parent has separate positive support in SL0355. This response is a bounded ontology hierarchy observation, not an experimental mechanism or exhaustive source consensus. |
| septin-GO0070118-isa | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0070118/ancestors?relations=is_a; Complete exact QuickGO ancestors response with relations=is_a | supports | GO0042651 generic thylakoid membrane and GO0070112 chromatophore membrane occur; GO0055035 plastid thylakoid membrane is not among returned is_a ancestors, but SL0356 explicitly supplies that classification. This response is a bounded ontology hierarchy observation, not an experimental mechanism or exhaustive source consensus. |
| septin-catalogue | https://imodulondb.org/api/datasets; Complete current official organism/dataset catalogue | supports | No Paulinella, P. chromatophora or CCAC0185 host/strain appears in the inspected catalogue. Molecular light-reaction assertions in thylakoid and membrane require this applicability assessment; the lumen independently excludes molecular mechanisms. No matching host dataset warrants downstream gene/module checks, and Synechococcus or another free-living cyanobacterium is not substituted for a Paulinella organelle. Catalogue noncoverage is not negative biological evidence. |
| septin-tax39717 | https://rest.uniprot.org/taxonomy/39717.json; Previously fetched exact taxonomy JSON independently re-read: identity, rank and Paulinella parent | supports | NCBITaxon39717 is Paulinella chromatophora species. Identity does not by itself establish species-wide frequency. Cached public snapshot retains its actual original fetch timestamp; no fresh body retrieval is claimed. |
| septin-nowack2014-crossref | https://api.crossref.org/works/10.5586/asbp.2014.049; Previously fetched Crossref exact DOI metadata and complete deposited abstract re-read; full secondary body not read | supports | DOI10.5586/asbp.2014.049 is Eva C. M. Nowack2014 Paulinella chromatophora - rethinking the transition from endosymbiont to organelle. Deposited secondary abstract supports photosynthetic chromatophore evolutionary context; it is not a numerical prevalence census or direct new structural experiment. Cached public snapshot retains its actual original fetch timestamp; no fresh body retrieval is claimed. |
| septin-nowack2012-prefixed | https://pmc.ncbi.nlm.nih.gov/articles/PMC3325729/; Previously fetched genuine PMC3325729 HTML independently re-read at Results first two sections (PsaE localization and PsaE/PsaK1/PsaK2 association with PSI), Fig1/2 text captions and Methods Strain and Growth Conditions paragraph | supports | Immunogold localization associates PsaE with thylakoids; PSI purification with immunoblot, mass-spectrometric/Edman characterization supports selected PSI subunit association. Study uses P. chromatophora CCAC0185 subisolate M0880/a, grown at17C in Waris-H medium under14h light/10h dark. Bounded positive molecular/localization evidence does not enumerate all light complexes or demonstrate each constituent necessary for thylakoid formation. Figure captions were read, not source pixels/supplements/raw data. Cached public snapshot retains its actual original fetch timestamp; no fresh body retrieval is claimed. |
| septin-context-organellar_chromatophore | data/structures/membrane_organelle/organellar_chromatophore.yaml; Frozen identity, label, definition, parent_structures, part_of, has_part and xrefs only | supports | Whole chromatophore boundary context was frozen before read. Reciprocal thylakoid identity/parthood supports local structural relations. No independent whole-record verdict or disposition of its distinct scientific issues is claimed. |
| septin-adapter-runner-historical | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical attempted runner only; no fresh invocation | supports | Actual2026-11-03T00:49:00.848907Z–00:49:00.863225Z attempt ended exit1 PermissionError reading pyvenv.cfg. This availability receipt is historical and separate from the fresh successful official catalogue fetch and record-specific applicability judgment. |
| septin-retrieval-source-receipts | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/adversary-septin/source-receipts.json; Actual retrieval or cached-source reinspection times and exact saved hashes | supports | Nine current official requests succeeded. Three previously fetched public snapshots retain original access timestamps and explicit bounded reinspection scope. No metadata, secondary abstract or text caption is represented as a fresh complete primary-body or pixel audit. |
| septin-retrieval-reused-source-receipts | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/adversary-septin/reused-source-receipts.json; Actual retrieval or cached-source reinspection times and exact saved hashes | supports | Nine current official requests succeeded. Three previously fetched public snapshots retain original access timestamps and explicit bounded reinspection scope. No metadata, secondary abstract or text caption is represented as a fresh complete primary-body or pixel audit. |
| septin-record-organellar_chromatophore_thylakoid | data/structures/membrane_organelle/organellar_chromatophore_thylakoid.yaml; Complete current record at bdd5beb85634420b1d99c91138a9121631087f89 | supports | Every identity, history, synonym, hierarchy, component, scope, canonical example, evidence, discussion and complete graph field read. No individual protein example/gene-symbol inventory, typed molecular node, UniProtKB graph xref, maintained image, numerical measurement, associated trait or verbatim snippet occurs. |
| septin-original-organellar_chromatophore_thylakoid | reviews/structured/20261022T030053Z-organellar-chromatophore-thylakoid-audit/review.yaml; Original YAML/Markdown scope, exact findings/actions, historical checks and limitations | supports | Original pair remains immutable; frozen target hash matches current bytes. Original verdict and finding lineage were independently reassessed; old check disclosures are not recast as current executions. |
| septin-original-validation-organellar_chromatophore_thylakoid | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/adversary-septin/original-checks.json; Actual original native validation/render plus frozen/current target hash | supports | Native validate/render exit0 and Markdown byte equality; frozen target hash agrees with current target. |
| septin-native-organellar_chromatophore_thylakoid-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_thylakoid-uniprot-verify-receipt.json; Actual receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_thylakoid-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0. Actual record has zero protein examples, zero GENE_OR_PROTEIN nodes and no UniProtKB graph xrefs. Native success validates the empty represented identifier scope; it does not prove molecular inventory completeness or all biological claims. |
| septin-native-organellar_chromatophore_thylakoid-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_thylakoid-uniprot-causal-receipt.json; Actual receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_thylakoid-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Exit0. Actual record has zero protein examples, zero GENE_OR_PROTEIN nodes and no UniProtKB graph xrefs. Native success validates the empty represented identifier scope; it does not prove molecular inventory completeness or all biological claims. |
| septin-record-organellar_chromatophore_thylakoid_lumen | data/structures/membrane_organelle/organellar_chromatophore_thylakoid_lumen.yaml; Complete current record at bdd5beb85634420b1d99c91138a9121631087f89 | supports | Every identity, history, synonym, hierarchy, component, scope, canonical example, evidence, discussion and complete graph field read. No individual protein example/gene-symbol inventory, typed molecular node, UniProtKB graph xref, maintained image, numerical measurement, associated trait or verbatim snippet occurs. |
| septin-original-organellar_chromatophore_thylakoid_lumen | reviews/structured/20261022T030054Z-organellar-chromatophore-thylakoid-lumen-audit/review.yaml; Original YAML/Markdown scope, exact findings/actions, historical checks and limitations | supports | Original pair remains immutable; frozen target hash matches current bytes. Original verdict and finding lineage were independently reassessed; old check disclosures are not recast as current executions. |
| septin-original-validation-organellar_chromatophore_thylakoid_lumen | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/adversary-septin/original-checks.json; Actual original native validation/render plus frozen/current target hash | supports | Native validate/render exit0 and Markdown byte equality; frozen target hash agrees with current target. |
| septin-native-organellar_chromatophore_thylakoid_lumen-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_thylakoid_lumen-uniprot-verify-receipt.json; Actual receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_thylakoid_lumen-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0. Actual record has zero protein examples, zero GENE_OR_PROTEIN nodes and no UniProtKB graph xrefs. Native success validates the empty represented identifier scope; it does not prove molecular inventory completeness or all biological claims. |
| septin-native-organellar_chromatophore_thylakoid_lumen-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_thylakoid_lumen-uniprot-causal-receipt.json; Actual receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_thylakoid_lumen-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Exit0. Actual record has zero protein examples, zero GENE_OR_PROTEIN nodes and no UniProtKB graph xrefs. Native success validates the empty represented identifier scope; it does not prove molecular inventory completeness or all biological claims. |
| septin-record-organellar_chromatophore_thylakoid_membrane | data/structures/membrane_organelle/organellar_chromatophore_thylakoid_membrane.yaml; Complete current record at bdd5beb85634420b1d99c91138a9121631087f89 | supports | Every identity, history, synonym, hierarchy, component, scope, canonical example, evidence, discussion and complete graph field read. No individual protein example/gene-symbol inventory, typed molecular node, UniProtKB graph xref, maintained image, numerical measurement, associated trait or verbatim snippet occurs. |
| septin-original-organellar_chromatophore_thylakoid_membrane | reviews/structured/20261022T030055Z-organellar-chromatophore-thylakoid-membrane-audit/review.yaml; Original YAML/Markdown scope, exact findings/actions, historical checks and limitations | supports | Original pair remains immutable; frozen target hash matches current bytes. Original verdict and finding lineage were independently reassessed; old check disclosures are not recast as current executions. |
| septin-original-validation-organellar_chromatophore_thylakoid_membrane | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/adversary-septin/original-checks.json; Actual original native validation/render plus frozen/current target hash | supports | Native validate/render exit0 and Markdown byte equality; frozen target hash agrees with current target. |
| septin-native-organellar_chromatophore_thylakoid_membrane-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_thylakoid_membrane-uniprot-verify-receipt.json; Actual receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_thylakoid_membrane-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0. Actual record has zero protein examples, zero GENE_OR_PROTEIN nodes and no UniProtKB graph xrefs. Native success validates the empty represented identifier scope; it does not prove molecular inventory completeness or all biological claims. |
| septin-native-organellar_chromatophore_thylakoid_membrane-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_thylakoid_membrane-uniprot-causal-receipt.json; Actual receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_thylakoid_membrane-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Exit0. Actual record has zero protein examples, zero GENE_OR_PROTEIN nodes and no UniProtKB graph xrefs. Native success validates the empty represented identifier scope; it does not prove molecular inventory completeness or all biological claims. |
| plaque-current-7 | data/structures/membrane_organelle/osmiophilic_body.yaml; Entire current maintained record at bdd5beb85634420b1d99c91138a9121631087f89; all fields, graphs, discussions and history | supports | Read complete exact target. Current bytes equal original target freeze; scientific reassessment is current, not a stale-input refresh. |
| plaque-original-7 | reviews/structured/20261022T030055Z-osmiophilic-body-audit/review.yaml; Exact staleness-selected original YAML and native Markdown; all evidence, assessments, checks, finding/action and source fields | supports | Original observations remain immutable. Native validation/render and all15 original frozen input hashes verified separately for this target. |
| plaque-current-8 | data/structures/membrane_organelle/parasitophorous_vacuole.yaml; Entire current maintained record at bdd5beb85634420b1d99c91138a9121631087f89; all fields, graphs, discussions and history | supports | Read complete exact target. Current bytes equal original target freeze; scientific reassessment is current, not a stale-input refresh. |
| plaque-original-8 | reviews/structured/20261022T030057Z-parasitophorous-vacuole-audit/review.yaml; Exact staleness-selected original YAML and native Markdown; all evidence, assessments, checks, finding/action and source fields | supports | Original observations remain immutable. Native validation/render and all15 original frozen input hashes verified separately for this target. |
| plaque-current-9 | data/structures/membrane_organelle/parasitophorous_vacuole_lumen.yaml; Entire current maintained record at bdd5beb85634420b1d99c91138a9121631087f89; all fields, graphs, discussions and history | supports | Read complete exact target. Current bytes equal original target freeze; scientific reassessment is current, not a stale-input refresh. |
| plaque-original-9 | reviews/structured/20261022T030057Z-parasitophorous-vacuole-lumen-audit/review.yaml; Exact staleness-selected original YAML and native Markdown; all evidence, assessments, checks, finding/action and source fields | supports | Original observations remain immutable. Native validation/render and all15 original frozen input hashes verified separately for this target. |
| plaque-policy | .claude/skills/review-yaml-record/SKILL.md; Fresh current Structured Source Cross-Checks and evidence rules; unchanged native instructions | context_only | Full positive protein/pathway claims trigger applicability; no expression assertion is not a sufficient exemption. Actual morphology-only targets can remain excluded. |
| plaque-rubric | .claude/skills/curate-yaml-record/references/review-checklist.md; Previously read exact frozen checklist bytes unchanged | context_only | Identity, source-specific science, taxon, model granularity, necessity and accessibility are separate assessments; no optional inventory finding. |
| plaque-graph-rubric | .claude/skills/curate-causal-graphs/SKILL.md; Previously read frozen graph policy unchanged | context_only | Nonmechanistic designation does not excuse a material unqualified functional conflict. Localization and constitutive material are distinct from formation necessity. |
| plaque-protein-contract | .claude/skills/uniprot-protein-examples/SKILL.md; Previously read frozen native example contract unchanged | context_only | Examples identify specific instances; a fragment/unreviewed example need not supply a full protein mechanism. COVERED means represented identifier coverage, not scientific completeness. |
| plaque-schema-policy | src/cellstructuremech/schema/cellstructuremech.yaml; Current StructuralComponent and CausalNode enums/contract bytes unchanged | context_only | LIPID label-only generic membrane material is distinct from using a whole-membrane GO identity as a molecular chemical grounding. Protein complexes/families are permitted GENE_OR_PROTEIN nodes. |
| plaque-context-pvm | data/structures/membrane_organelle/parasitophorous_vacuole_membrane.yaml; Whole frozen neighbor read after root expanded inspect; bounded local boundary identity/topology context only | context_only | Exact local PVM identifier and PV parthood resolve. Neighbor canonical-example evidence is not adjudicated or resolved by this assigned-target review. |
| plaque-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0044310,GO:0031410,GO:0020003,GO:0020004,GO:0020005; Complete exact5-term QuickGO response, all definitions/synonyms/comments/typed children | supports | GO0044310 exact osmiophilic body/postulated-release definition and direct0031410 is_a are supported. GO0020003/4/5 are broader symbiont vacuole/space/membrane identities with direct typed part children. Lexical exact PV synonyms do not override broader native biological definitions. |
| plaque-SL-0193 | https://rest.uniprot.org/locations/SL-0193.json; Complete current UniProt location JSON; exact definition, synonyms, mappings and typed isA/partOf | supports | Native locations support narrower apicomplexan PV, exact surrounding PVM and exact lumen; lumen/PVM partOf is distinct from broad GO parentage and molecular composition. |
| plaque-SL-0194 | https://rest.uniprot.org/locations/SL-0194.json; Complete current UniProt location JSON; exact definition, synonyms, mappings and typed isA/partOf | supports | Native locations support narrower apicomplexan PV, exact surrounding PVM and exact lumen; lumen/PVM partOf is distinct from broad GO parentage and molecular composition. |
| plaque-SL-0341 | https://rest.uniprot.org/locations/SL-0341.json; Complete current UniProt location JSON; exact definition, synonyms, mappings and typed isA/partOf | supports | Native locations support narrower apicomplexan PV, exact surrounding PVM and exact lumen; lumen/PVM partOf is distinct from broad GO parentage and molecular composition. |
| plaque-tax5794 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5794; Complete current ENA taxon identity/rank/lineage/alternate names | supports | Exact Apicomplexa, Toxoplasma gondii, Plasmodium falciparum or Plasmodium berghei identity verified; neither taxonomic identity nor orthology substitutes for the experimental organism/strain. |
| plaque-tax5811 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5811; Complete current ENA taxon identity/rank/lineage/alternate names | supports | Exact Apicomplexa, Toxoplasma gondii, Plasmodium falciparum or Plasmodium berghei identity verified; neither taxonomic identity nor orthology substitutes for the experimental organism/strain. |
| plaque-tax5833 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5833; Complete current ENA taxon identity/rank/lineage/alternate names | supports | Exact Apicomplexa, Toxoplasma gondii, Plasmodium falciparum or Plasmodium berghei identity verified; neither taxonomic identity nor orthology substitutes for the experimental organism/strain. |
| plaque-tax5821 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5821; Complete current ENA taxon identity/rank/lineage/alternate names | supports | Exact Apicomplexa, Toxoplasma gondii, Plasmodium falciparum or Plasmodium berghei identity verified; neither taxonomic identity nor orthology substitutes for the experimental organism/strain. |
| plaque-pfg377 | https://rest.uniprot.org/uniprotkb/A0A059WIJ2.json; Complete current A0A059WIJ2 JSON including entry status, protein description, gene, sequence, reference strain and crossreferences | supports | UNREVIEWED TrEMBL Pfg377/pfg377, taxon5833,193-aa Fragment, predicted protein evidence, G1 sequence background. Partial gene example remains identity-only, not the full377-kDa experimental protein or the3D7 knockout strain. Native PANTHER annotations are not automatically adopted as exact source-neutral grounding. |
| plaque-pfg377-interpro | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/A0A059WIJ2/?page_size=200; Exact accession association request page_size200; HTTP204 zero bytes | context_only | This response supplies no inspectable family list; it does not establish absence of a Pfg377 family or justify guessing a grounding. |
| plaque-pfg377-reviewed-search | https://rest.uniprot.org/uniprotkb/search?query=%28gene%3Apfg377%29%20AND%20%28organism_id%3A5833%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Exact native gene:pfg377 AND organism_id:5833 AND reviewed:true; size100 | context_only | Zero returned reviewed entries within this exact query. Does not refute unreviewed accession identity or prove absence under other aliases/family namespaces. |
| plaque-alano1995-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1016%2F0166-6851%2895%2902491-3&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact DOI query with punctuation; pageSize25; zero hits | context_only | No result from this DOI search surface is not a missing-paper finding. Exact PMID8719156 subsequently returns the valid DOI/title and complete primary abstract. |
| plaque-alano1995-pmid | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8719156%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact native bibliographic identity and complete primary abstract inspected | supports | Title/authors/year/DOI/PMID checked. Alano supports3D7 cDNA, full377-kDa gene product and immunoelectron localization;2008 reports reduced emergence and infection;2016 reports contrary egress result;2018 explicitly reports P.berghei BioID. Abstract scope is distinct from separately read bodies. |
| plaque-dekoning2008-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1111%2Fj.1365-2958.2007.06039.x&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact native bibliographic identity and complete primary abstract inspected | supports | Title/authors/year/DOI/PMID checked. Alano supports3D7 cDNA, full377-kDa gene product and immunoelectron localization;2008 reports reduced emergence and infection;2016 reports contrary egress result;2018 explicitly reports P.berghei BioID. Abstract scope is distinct from separately read bodies. |
| plaque-suarez2016-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1074%2Fmcp.M116.060681&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact native bibliographic identity and complete primary abstract inspected | supports | Title/authors/year/DOI/PMID checked. Alano supports3D7 cDNA, full377-kDa gene product and immunoelectron localization;2008 reports reduced emergence and infection;2016 reports contrary egress result;2018 explicitly reports P.berghei BioID. Abstract scope is distinct from separately read bodies. |
| plaque-schnider2018-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128%2FmSphere.00522-17&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact native bibliographic identity and complete primary abstract inspected | supports | Title/authors/year/DOI/PMID checked. Alano supports3D7 cDNA, full377-kDa gene product and immunoelectron localization;2008 reports reduced emergence and infection;2016 reports contrary egress result;2018 explicitly reports P.berghei BioID. Abstract scope is distinct from separately read bodies. |
| plaque-lingelbach1998-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1242%2Fjcs.111.11.1467&amp;format=json&amp;resultType=core&amp;pageSize=25; Complete native bibliographic metadata and abstract; SECONDARY REVIEW | supports | Lingelbach describes invasion-associated PVM formation around Plasmodium/Toxoplasma. Clough supports the Toxoplasma replicative niche/interface. These are secondary syntheses, not newly inspected primary mechanism experiments or full review bodies. |
| plaque-clough2017-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1016%2Fj.pt.2017.02.007&amp;format=json&amp;resultType=core&amp;pageSize=25; Complete native bibliographic metadata and abstract; SECONDARY REVIEW | supports | Lingelbach describes invasion-associated PVM formation around Plasmodium/Toxoplasma. Clough supports the Toxoplasma replicative niche/interface. These are secondary syntheses, not newly inspected primary mechanism experiments or full review bodies. |
| plaque-dekoning2008-repository | https://eprints.gla.ac.uk/4379/; University Glasgow repository metadata and complete abstract; explicit full-text availability statement | supports | Matches2008 authors/title/DOI/claim scope; full text explicitly unavailable from repository. Wiley PDF403 is not read as article body. The reported historical emergence phenotype remains genuine evidence, requiring reconciliation rather than erasure. |
| plaque-suarez2016-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC5054347/; Genuine PMC5054347 HTML; Methods sec5–9, Results sec19 with Figure1 caption, complete Discussion sec24 read. Additional parent-section output is not claimed as complete analysis of other Methods/Results. No figure pixels, supplements or raw proteomics. | supports | New3D7 pfg377KO clones5-2/8-20 are OB-depleted with abnormal residual granules. WGA/XA assay at15min, at least4experiments/200gametes each, finds no egress difference; clone5-2 has severe Ngousso A.gambiae infection/oocyst defect. Authors explicitly fail to reproduce2008 egress result and leave post-egress arrest unknown. Normal-body biogenesis and transmission association survive; a universal no-egress-role conclusion across all timing/strains does not follow. |
| plaque-schnider2018-body | https://pmc-oa-opendata.s3.amazonaws.com/PMC5784244.1/PMC5784244.1.xml; Genuine PMC5784244.1 JATS; title/DOI, Results s1.1/s1.2 including embedded captions, complete Discussion s2, Methods s3.6/s3.9. No source figure pixels, supplemental files, or quantitative reanalysis. | supports | EXP1-BirA*-V5 BioID uses P.berghei ANKA mCherryHsp70 blood-stage schizonts,18h150µM biotin.61candidate list is not61proven PVM residents; source notes off-target labeling and7follow-up candidates with3novel PVM localizations. P.falciparum references are ortholog/prior-study comparisons, not the performed survey organism. |
| plaque-catalogue | https://imodulondb.org/api/datasets; Same-PR fresh complete official catalogue, all20organism rows/28organism-dataset pairs independently read; original retrieval time retained | supports | All represented hosts are bacteria/archaea, no Plasmodium/Toxoplasma/apicomplexan dataset. Osmiophilic protein/egress/transmission and whole-PV BioID/PVM-protein assertions require applicability followed by bounded host noncoverage. PV lumen is genuinely topology-only. No foreign-host downstream module proxy or negative biology. |
| plaque-access-routes | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/adversary-plaque/additional-receipts.json; Actual additional request statuses and snapshot hashes | context_only | Alano publisher403, Wiley PDF403, Suarez S3 JATS404, Lingelbach publisher403, Clough DOI route200 redirect shell are not full texts. Genuine Suarez PMC HTML/Schnider JATS are separately scoped successful bodies. Alano DOI0hits is resolved through exact PMID, not an absence claim. |
| plaque-historical-runner | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical00:49Z unavailable runner receipt and retained stdout/stderr | context_only | Historical PermissionError accessing pyvenv.cfg; not rerun or represented as successful. Current public catalogue source fallback is independently inspected. |
| plaque-original-checks | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/adversary-plaque/original-checks.json; Actual three original native validation/render pairs and retained source/current hashes | supports | All3 originals validate/render exactly;15 historical inputs each match retained source; all3 current target hashes unchanged. |
| plaque-native-osmiophilic_body-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/osmiophilic_body.yaml --verify; Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/osmiophilic_body-uniprot-verify-receipt.json and stdoutSHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual osmiophilic inventory has1UNREVIEWED Pfg377 fragment example and1COVERED typed node; native coverage is identifier representation, not reconciliation of egress evidence. |
| plaque-native-osmiophilic_body-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/osmiophilic_body.yaml --causal-graphs; Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/osmiophilic_body-uniprot-causal-receipt.json and stdoutSHA256 8bdeb0fe45330c8ed5561de769ee40e4812f9112e072ee6467a5a2d6ba734b2f | supports | Actual osmiophilic inventory has1UNREVIEWED Pfg377 fragment example and1COVERED typed node; native coverage is identifier representation, not reconciliation of egress evidence. |
| plaque-native-parasitophorous_vacuole-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/parasitophorous_vacuole.yaml --verify; Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/parasitophorous_vacuole-uniprot-verify-receipt.json and stdoutSHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual inventory has0examples and0GENE_OR_PROTEINnodes; native pass is empty represented accession/node coverage, not validation of narrative BioID or all molecular claims. |
| plaque-native-parasitophorous_vacuole-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/parasitophorous_vacuole.yaml --causal-graphs; Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/parasitophorous_vacuole-uniprot-causal-receipt.json and stdoutSHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Actual inventory has0examples and0GENE_OR_PROTEINnodes; native pass is empty represented accession/node coverage, not validation of narrative BioID or all molecular claims. |
| plaque-native-parasitophorous_vacuole_lumen-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/parasitophorous_vacuole_lumen.yaml --verify; Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/parasitophorous_vacuole_lumen-uniprot-verify-receipt.json and stdoutSHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual inventory has0examples and0GENE_OR_PROTEINnodes; native pass is empty represented accession/node coverage, not validation of narrative BioID or all molecular claims. |
| plaque-native-parasitophorous_vacuole_lumen-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/parasitophorous_vacuole_lumen.yaml --causal-graphs; Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/parasitophorous_vacuole_lumen-uniprot-causal-receipt.json and stdoutSHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Actual inventory has0examples and0GENE_OR_PROTEINnodes; native pass is empty represented accession/node coverage, not validation of narrative BioID or all molecular claims. |
| micro-policy | .claude/skills/review-yaml-record/SKILL.md; Native skill/profile/config/checklist and structured-source cross-check contract | context_only | Actual protein/pathway assertions trigger host applicability assessment; material/topology-only records with molecular mechanisms withheld are genuine exclusions. Optional slots and historical clean bundles do not justify invented findings. |
| micro-component-policy | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent391-460, ComponentTypeEnum, EssentialityEnum and native CURATION components guidance | context_only | Label-only collective bilayer or residual peptidoglycan material is distinct from using a whole anatomical GO membrane as chemical grounding. Exact molecular identities must not be guessed. Essentiality concerns structure formation, not cell viability. |
| micro-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Whole graph scope, source-specific evidence and node/component-reference contract; add-cell-structure guidance | context_only | NONMECHANISTIC topology is not an experimentally established assembly or transport pathway. Every asserted edge is assessed at its actual source scope. No unsupported complete protein inventory is inferred from native empty passes. |
| micro-record-organellar_chromatophore_inner_membrane | data/structures/membrane_organelle/organellar_chromatophore_inner_membrane.yaml; Entire record including history, definitions, taxonomy, all components/evidence, every graph node/edge and discussions | supports | Complete current target independently reviewed; exact original frozen target hash unchanged. No scientific record mutation. |
| micro-prior-organellar_chromatophore_inner_membrane | reviews/structured/20261022T030049Z-organellar-chromatophore-inner-membrane-audit/review.yaml; Original native identity/provenance/checks/evidence/assessments/limitations; original Markdown checked by actual deterministic renderer | context_only | Original pass_with_limitations, no findings or request-curation actions. Explicit expression-only applicability row is present; complete current physical scope independently supports genuine exclusion. Historical accesses and commands are not current executions. |
| micro-native-organellar_chromatophore_inner_membrane-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_inner_membrane-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/organellar_chromatophore_inner_membrane.yaml --verify; full log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_inner_membrane-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0 at source head. Independently read record has zero protein_examples and zero GENE_OR_PROTEIN nodes; causal report explicitly counts zero. Generic verification success text is not proof of a populated molecular inventory, family grounding or biochemical completeness. |
| micro-native-organellar_chromatophore_inner_membrane-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_inner_membrane-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/organellar_chromatophore_inner_membrane.yaml --causal-graphs; full log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_inner_membrane-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Exit0 at source head. Independently read record has zero protein_examples and zero GENE_OR_PROTEIN nodes; causal report explicitly counts zero. Generic verification success text is not proof of a populated molecular inventory, family grounding or biochemical completeness. |
| micro-record-organellar_chromatophore_intermembrane_space | data/structures/membrane_organelle/organellar_chromatophore_intermembrane_space.yaml; Entire record including history, definitions, taxonomy, all components/evidence, every graph node/edge and discussions | supports | Complete current target independently reviewed; exact original frozen target hash unchanged. No scientific record mutation. |
| micro-prior-organellar_chromatophore_intermembrane_space | reviews/structured/20261022T030050Z-organellar-chromatophore-intermembrane-space-audit/review.yaml; Original native identity/provenance/checks/evidence/assessments/limitations; original Markdown checked by actual deterministic renderer | context_only | Original pass_with_limitations, no findings or request-curation actions. Explicit expression-only applicability row is present; complete current physical scope independently supports genuine exclusion. Historical accesses and commands are not current executions. |
| micro-native-organellar_chromatophore_intermembrane_space-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_intermembrane_space-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/organellar_chromatophore_intermembrane_space.yaml --verify; full log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_intermembrane_space-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0 at source head. Independently read record has zero protein_examples and zero GENE_OR_PROTEIN nodes; causal report explicitly counts zero. Generic verification success text is not proof of a populated molecular inventory, family grounding or biochemical completeness. |
| micro-native-organellar_chromatophore_intermembrane_space-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_intermembrane_space-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/organellar_chromatophore_intermembrane_space.yaml --causal-graphs; full log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_intermembrane_space-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Exit0 at source head. Independently read record has zero protein_examples and zero GENE_OR_PROTEIN nodes; causal report explicitly counts zero. Generic verification success text is not proof of a populated molecular inventory, family grounding or biochemical completeness. |
| micro-record-organellar_chromatophore_membrane | data/structures/membrane_organelle/organellar_chromatophore_membrane.yaml; Entire record including history, definitions, taxonomy, all components/evidence, every graph node/edge and discussions | supports | Complete current target independently reviewed; exact original frozen target hash unchanged. No scientific record mutation. |
| micro-prior-organellar_chromatophore_membrane | reviews/structured/20261022T030051Z-organellar-chromatophore-membrane-audit/review.yaml; Original native identity/provenance/checks/evidence/assessments/limitations; original Markdown checked by actual deterministic renderer | context_only | Original pass_with_limitations, no findings or request-curation actions. Explicit expression-only applicability row is present; complete current physical scope independently supports genuine exclusion. Historical accesses and commands are not current executions. |
| micro-native-organellar_chromatophore_membrane-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_membrane-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/organellar_chromatophore_membrane.yaml --verify; full log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_membrane-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0 at source head. Independently read record has zero protein_examples and zero GENE_OR_PROTEIN nodes; causal report explicitly counts zero. Generic verification success text is not proof of a populated molecular inventory, family grounding or biochemical completeness. |
| micro-native-organellar_chromatophore_membrane-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_membrane-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/organellar_chromatophore_membrane.yaml --causal-graphs; full log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_membrane-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Exit0 at source head. Independently read record has zero protein_examples and zero GENE_OR_PROTEIN nodes; causal report explicitly counts zero. Generic verification success text is not proof of a populated molecular inventory, family grounding or biochemical completeness. |
| micro-record-organellar_chromatophore_outer_membrane | data/structures/membrane_organelle/organellar_chromatophore_outer_membrane.yaml; Entire record including history, definitions, taxonomy, all components/evidence, every graph node/edge and discussions | supports | Complete current target independently reviewed; exact original frozen target hash unchanged. No scientific record mutation. |
| micro-prior-organellar_chromatophore_outer_membrane | reviews/structured/20261022T030052Z-organellar-chromatophore-outer-membrane-audit/review.yaml; Original native identity/provenance/checks/evidence/assessments/limitations; original Markdown checked by actual deterministic renderer | context_only | Original pass_with_limitations, no findings or request-curation actions. Explicit expression-only applicability row is present; complete current physical scope independently supports genuine exclusion. Historical accesses and commands are not current executions. |
| micro-native-organellar_chromatophore_outer_membrane-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_outer_membrane-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/organellar_chromatophore_outer_membrane.yaml --verify; full log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_outer_membrane-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0 at source head. Independently read record has zero protein_examples and zero GENE_OR_PROTEIN nodes; causal report explicitly counts zero. Generic verification success text is not proof of a populated molecular inventory, family grounding or biochemical completeness. |
| micro-native-organellar_chromatophore_outer_membrane-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_outer_membrane-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/organellar_chromatophore_outer_membrane.yaml --causal-graphs; full log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_outer_membrane-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Exit0 at source head. Independently read record has zero protein_examples and zero GENE_OR_PROTEIN nodes; causal report explicitly counts zero. Generic verification success text is not proof of a populated molecular inventory, family grounding or biochemical completeness. |
| micro-original-pairs | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/adversary-microtubule/original-checks.json; Four actual native validate calls and four render --content calls with exact Markdown comparison | supports | All four original YAML documents validate and all four committed Markdown artifacts exactly match their deterministic render. |
| micro-original-inputs | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/adversary-microtubule/original-frozen-inputs.json; All68 historical frozen input entries at original retained source revision | supports | All original source hashes verify; current four target hashes unchanged. Historical context hashing is provenance validation, not a new scientific judgment of unfrozen neighboring records. |
| micro-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0070111,GO:0070112,GO:0070113,GO:0070114,GO:0070115,GO:0070116,GO:0070117,GO:0070118,GO:0009527,GO:0009528,GO:0009529,GO:0030659; Complete12 requested active terms: id/name/definition/synonyms/isObsolete and typed children; exact queried list in URL | supports | GO0070112/13/14/15 identify generic membrane, inner membrane, outer membrane and intermembrane space. GO0070112 directly has0070113/14/18 is_a children; GO0030659 directly has0070112 is_a child. GO0070111 directly has0070112/14/15 part_of children; no direct inner relation fabricated. Parent plastid anatomy terms are active; differing hierarchy claims are attributed to UniProt, not invented GO edges. |
| micro-go-0070112-isa | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0070112/ancestors?relations=is_a; Complete exact-term ancestors request with relations=is_a; transitive ancestry not immediate-parent or parthood proof | supports | Native is_a ancestors for GO:0070112 are GO:0030659, GO:0070112, GO:0012506, GO:0016020, GO:0110165, GO:0005575, GO:0031090. Broader plastid parents absent from this exact response are not asserted as GO edges; native UniProt immediate relationships are separately inspected. |
| micro-go-0070113-isa | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0070113/ancestors?relations=is_a; Complete exact-term ancestors request with relations=is_a; transitive ancestry not immediate-parent or parthood proof | supports | Native is_a ancestors for GO:0070113 are GO:0030659, GO:0070112, GO:0012506, GO:0016020, GO:0070113, GO:0110165, GO:0005575, GO:0031090. Broader plastid parents absent from this exact response are not asserted as GO edges; native UniProt immediate relationships are separately inspected. |
| micro-go-0070114-isa | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0070114/ancestors?relations=is_a; Complete exact-term ancestors request with relations=is_a; transitive ancestry not immediate-parent or parthood proof | supports | Native is_a ancestors for GO:0070114 are GO:0030659, GO:0070112, GO:0098588, GO:0012506, GO:0016020, GO:0043661, GO:0070114, GO:0110165, GO:0005575, GO:0031090, GO:0030666. Broader plastid parents absent from this exact response are not asserted as GO edges; native UniProt immediate relationships are separately inspected. |
| micro-go-0070115-isa | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0070115/ancestors?relations=is_a; Complete exact-term ancestors request with relations=is_a; transitive ancestry not immediate-parent or parthood proof | supports | Native is_a ancestors for GO:0070115 are GO:0070115, GO:0110165, GO:0005575. Broader plastid parents absent from this exact response are not asserted as GO edges; native UniProt immediate relationships are separately inspected. |
| micro-SL0351 | https://rest.uniprot.org/locations/SL-0351.json; Top-level native id/name/definition/category/GO mappings, immediate isA/partOf entries and corresponding parent GO cross-references; statistics not evidence of biological absence | supports | Exact GO0070111 mapping and definition explicitly state two surrounding membranes, residual peptidoglycan between them and internal thylakoids. This authority supports anatomical context; its broader biosynthetic discussion is not imported as a pathway assertion into the four physical records. |
| micro-SL0352 | https://rest.uniprot.org/locations/SL-0352.json; Top-level native id/name/definition/category/GO mappings, immediate isA/partOf entries and corresponding parent GO cross-references; statistics not evidence of biological absence | supports | Exact GO0070112 mapping, definition explicitly covers unspecified outer/inner/thylakoid localization, immediate isA plastid membrane and partOf organellar chromatophore. Its generic fallback scope is distinct from identifying any particular membrane or protein. |
| micro-SL0359 | https://rest.uniprot.org/locations/SL-0359.json; Top-level native id/name/definition/category/GO mappings, immediate isA/partOf entries and corresponding parent GO cross-references; statistics not evidence of biological absence | supports | Exact GO0070113 mapping and definition of stroma/intermembrane-space separation; immediate isA plastid inner membraneGO0009528 and chromatophore membraneGO0070112, partOf chromatophoreGO0070111. Paulinella-specific description is not a prevalence census. |
| micro-SL0360 | https://rest.uniprot.org/locations/SL-0360.json; Top-level native id/name/definition/category/GO mappings, immediate isA/partOf entries and corresponding parent GO cross-references; statistics not evidence of biological absence | supports | Exact GO0070115 mapping and region between inner/outer membranes; immediate isA plastid intermembrane spaceGO0009529 and partOf chromatophoreGO0070111. It denotes neither stroma nor thylakoid lumen. |
| micro-SL0361 | https://rest.uniprot.org/locations/SL-0361.json; Top-level native id/name/definition/category/GO mappings, immediate isA/partOf entries and corresponding parent GO cross-references; statistics not evidence of biological absence | supports | Exact GO0070114 mapping and cytoplasm-facing membrane definition; immediate isA plastid outer membraneGO0009527 and chromatophore membraneGO0070112, partOf chromatophoreGO0070111. |
| micro-SL0353 | https://rest.uniprot.org/locations/SL-0353.json; Top-level native id/name/definition/category/GO mappings, immediate isA/partOf entries and corresponding parent GO cross-references; statistics not evidence of biological absence | supports | Current exact location identifies chromatophore stroma excluding thylakoid space; immediate isA plastid stroma, partOf chromatophore, no top-level GO mapping. Optional enrichment does not refute the dated historical unresolved-accession removal or require rewriting append-only history. |
| micro-tax39716 | https://rest.uniprot.org/taxonomy/39716.json; Complete scientificName/taxonId/rank/active and parent/lineage fields | supports | Current authority identifies Paulinella39716 at genus rank within Eukaryota/Rhizaria/Cercozoa. This verifies identity, not universal occurrence or quantitative prevalence. |
| micro-catalogue | https://imodulondb.org/api/datasets; Complete official /api/datasets response; all20 organism rows and28 organism/dataset pairs inspected | supports | No Paulinella, chromatophora, micropora, longichromatophora or matching eukaryotic-host entry is present. The four targets already have genuine physical exclusions; this supplemental catalogue check does not invent pathway claims or justify a bacterial proxy. Noncoverage is not biological negative evidence. |
| micro-historical-runner | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical command /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources imodulondb datasets; actual00:49Z exit1/PermissionError reading pyvenv.cfg | context_only | Historical optional runner unavailable receipt retained as historical context, not rerun or current success. Current official catalogue fallback was freshly read; no necessary matched-host downstream query exists for these physical targets. |
| micro-gabr2020-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1111%2Fjpy.13003%22&amp;format=json&amp;resultType=core&amp;pageSize=25; Retained actual PR2372 retrieval; independently reread exact DOI core result identity/authors/publication type and complete abstract; pageSize25 unique MED result | context_only | Paulinella, a model for understanding plastid primary endosymbiosis. DOI10.1111/jpy.13003 PMID32289879. Secondary review, context only; abstract does not replace full-body scope. |
| micro-nowack2012-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1073%2Fpnas.1118800109%22&amp;format=json&amp;resultType=core&amp;pageSize=25; Retained actual PR2372 retrieval; independently reread exact DOI core result identity/authors/publication type and complete abstract; pageSize25 unique MED result | context_only | Trafficking of protein into the recently established photosynthetic organelles of Paulinella chromatophora. DOI10.1073/pnas.1118800109 PMID22371600. Primary import study; metadata/abstract distinct from bounded body reread. |
| micro-nowack2012-body | https://pmc.ncbi.nlm.nih.gov/articles/PMC3325729/; Retained genuine canonicalPMC HTML fetched18:08:44Z in PR2372, independently reread now: Resultssec2/3 with Fig1/2 captions and Methodssec14 Strain and Growth Conditions; no pixels or supplementary data | context_only | Primary P.chromatophora CCAC0185, a subisolate of M0880/a, shows chromatophores/thylakoids and localized PsaE plus PSI association in stated experiments. This corroborates organism/organelle context, not specific envelope lipid composition, residual-wall chemistry or individual formation necessity. No boundary protein imported from thylakoid localization. |
| micro-gabr2020-canonical | https://pmc.ncbi.nlm.nih.gov/articles/PMC7734844/; Genuine canonicalPMC secondary-review body, complete S2 The Paulinella Model and embedded Figure1 caption only; no figure pixels | context_only | Secondary context distinguishes photosynthetic Paulinella lineages from heterotrophic relatives lacking chromatophores. Supports qualitative VARIABLE within the genus, not a numerical prevalence census or current exhaustive species list. Fresh body retrieval distinguished from reused earlier metadata. |
| check-qc | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/qc.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| check-labels | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/labels.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| check-trait-links | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/trait-links.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Native TraitMech link check passed. |
| check-vendored | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/vendored.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Pinned governed files match; native vendored check passed. |
| check-curies | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/curies.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| focused | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/focused-results.json; All twenty actual target schema/strict command outputs | supports | Ten schema and ten strict commands returned exit zero. |
| supplemental-pmid | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/pmid-chunks-receipt.json; Complete native-report PMID set checked with unchanged resolver in batches of at most fifty | supports | 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers remain unverified. |
| historical-adapter-runner-availability | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical runner invocation receipt, exact SHA256 reverified during PR2373 synthesis | context_only | Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS PermissionError reading the configured runner pyvenv.cfg. This is a retained historical availability observation, not a fresh attempt or a scientific validation failure. Native policy permits inspected source-catalogue fallback. |

## Limits And Additional Notes

- Chromatophore thylakoid and two compartments independent subreview: Read-only source review of three unchanged thylakoid records at the exact source head. Root owns issue dedup/publication and repository/global/CI/queue actions. No future saved-head or CI attestation is made here.
- Chromatophore thylakoid and two compartments independent subreview: Nine fresh official-source requests are distinguished from three public snapshots reused with verified hashes and original access times: species taxonomy, Crossref secondary metadata/abstract and genuine Nowack2012 PMC body. No false fresh-access or full-paper claim is made.
- Chromatophore thylakoid and two compartments independent subreview: Nowack2012 reinspection is bounded to the first two Results sections, Fig1/2 text captions and Methods Strain and Growth Conditions. It establishes selected PsaE localization and PSI subunit association in CCAC0185 M0880/a under recorded culture conditions, not the full photosystem inventory or experimental requirements for thylakoid formation. No source pixels, raw data or supplements were examined.
- Chromatophore thylakoid and two compartments independent subreview: Nowack2014 is exact metadata and complete deposited secondary abstract only. COMMON species presence is qualitative, not numerically measured; genus VARIABLE notes do not assert universal chromatophore occurrence. Original reviewers other broader literature access remains historical, not adopted as current full-body evidence.
- Chromatophore thylakoid and two compartments independent subreview: GO and UniProt hierarchy/text attribution are kept distinct: plastid-specific lumen/membrane parents have explicit SL isA support even where current GO is_a ancestry does not contain them. Generic GO thylakoid organelle terminology and native category wording differ; no unsupported enum-only finding is manufactured.
- Chromatophore thylakoid and two compartments independent subreview: The membrane record intentionally uses REVIEWED_LABEL_ONLY collective lipid material; ESSENTIAL denotes constitutive bilayer material, not individual lipid/protein necessity. Optional exact chemistry, stoichiometry and protein inventory remain unestablished without forcing a CURIE. The whole-thylakoid LIPID-to-whole-membrane grounding is a distinct confirmed inherited error.
- Chromatophore thylakoid and two compartments independent subreview: All six native protein commands pass on independently confirmed empty represented scopes: zero protein examples, typed molecular nodes and UniProtKB graph xrefs. This is not universal molecular or scientific validation.
- Chromatophore thylakoid and two compartments independent subreview: Two actual positive light-reaction narratives trigger corrected structured-source applicability. Fresh catalogue has no Paulinella host match; unrelated cyanobacteria are not proxies. The lumen genuinely excludes molecular mechanisms. Historical00:49Z runner failure is never represented as a fresh invocation or biological noncoverage test.
- Chromatophore thylakoid and two compartments independent subreview: All27 actually used repository inputs were frozen before use:17 common rules/schema/scripts,3 targets,6 original artifacts and1 whole-chromatophore boundary neighbor. No new closure or whole-record/neighbor/group issue disposition is inferred.
- Osmiophilic body and parasitophorous vacuole boundary independent subreview: All3 targets unchanged. Two exact inheritedmajor findings/actions retained with original keys/severities and repository/review/finding predecessors; no new scientific finding. Lumen remains qualified.
- Osmiophilic body and parasitophorous vacuole boundary independent subreview: Original3 pairs natively validate and render byte-for-byte;15 historical frozen inputs each match. All actual used current local inputs are frozen. No scientific promotion, record/original edit or terminal neighbor/group/history disposition.
- Osmiophilic body and parasitophorous vacuole boundary independent subreview: Alano exact DOI query returned0 but exact PMID8719156 verified DOI/title/year/authors and complete primary abstract. Publisher403; full body unread. deKoning complete primary abstract and Glasgow metadata read; Wiley403 and repository explicitly no full text.2008 phenotype remains genuine historical evidence.
- Osmiophilic body and parasitophorous vacuole boundary independent subreview: Suarez genuine PMC HTML Methods5–9/Results19 withFig1caption/completeDiscussion24 read. S3JATS404 is not body. Parent-section extra output is not claimed as complete analysis of remaining Methods/Results. No figure pixels, supplemental files/raw proteomics or independent statistical reanalysis.15-minute assay does not exclude every early kinetic/strain-dependent effect.
- Osmiophilic body and parasitophorous vacuole boundary independent subreview: Schnider genuine JATS Results1.1/1.2, completeDiscussion2, Methods3.6/3.9 plus embedded captions read. Actual organism is P.berghei ANKA mCherryHsp70; P.falciparum comparisons remain separate.61proximity candidates do not equal61validated PVM constituents. No figure pixels, supplement files or raw data inspected.
- Osmiophilic body and parasitophorous vacuole boundary independent subreview: Lingelbach1998/Clough2017 are complete secondary abstracts only. Publisher403/200redirect shell are not full review bodies or newly inspected primary mechanisms. No unread-text refutation or universal nutrient-permeability claim.
- Osmiophilic body and parasitophorous vacuole boundary independent subreview: A0A059WIJ2 is an unreviewed193-aa G1 fragment with predicted protein existence, not full-length experimental3D7Pfg377. Native1COVERED node is identifier representation, not source conflict reconciliation. ExactInterPro204 is inconclusive; bounded reviewed-gene0results and PANTHERcrossreferences do not establish exhaustive family absence or exact grounding.
- Osmiophilic body and parasitophorous vacuole boundary independent subreview: PV and lumen native commands pass on0examples/0typednodes. Optional inventory absence does not negate positive narrative molecular claims or require new components. No image assets or image modality/licence claims occur in assigned records.
- Osmiophilic body and parasitophorous vacuole boundary independent subreview: Fresh official catalogue from same-PR micro reviewer independently reread completely at original18:41Z fetch time; no matched Plasmodium/Toxoplasma/apicomplexan host. Osmiophilic/PV trigger coverage from actual molecular assertions; lumen genuine morphology/topology exclusion. No unrelated strain proxy or inferred negative biology. Historical00:49Z runner remains unavailable, no fresh invocation.
- Osmiophilic body and parasitophorous vacuole boundary independent subreview: Root owns global gates, issue dedup/publication, immutable successor and finalCI/queue. This report binds independent science and scratch native preflight only. Neighbor PVM is used solely for exact boundary context; its record and any separate findings are outside this assigned review.
- Four chromatophore membrane-boundary independent subreview: Four complete unchanged boundary records independently reviewed; no scientific findings, no inherited findings/actions and no bundle defects in this slice. Their original clean observations remain immutable historical evidence. This scratch source report is for the explicit mixed-cohort successor; it is not a separate clean review bundle saved to the repository.
- Four chromatophore membrane-boundary independent subreview: GO and UniProt location classifications differ for some broader plastid parent relationships. Actual UniProt immediate isA/partOf entries support those relationships; no absent GO direct edge or part_of relation is inferred from an is_a-only ancestor list. Generic GO membrane prose is interpreted alongside its explicit inner/outer/thylakoid children and SL0352 fallback definition.
- Four chromatophore membrane-boundary independent subreview: All maintained citations in these four records are anatomy/localization authorities. Nowack2012 genuine primary body was retained from18:08:44.263032Z and independently reread at Resultssec2/3 with Fig1/2 captions and Methodssec14 only. No image pixels, supplementary data, lipid chemistry or individual envelope assembly necessity assessed. CCAC0185 is a subisolate of M0880/a; no other strain generalized.
- Four chromatophore membrane-boundary independent subreview: Gabr2020 fresh genuine canonicalPMC S2/Fig1caption is a secondary review, not primary experimental support. Earlier PR2372 metadata/abstract retains its actual retrieval time. Qualitative photosynthetic/heterotrophic variation supports VARIABLE, not a current complete species inventory or prevalence census.
- Four chromatophore membrane-boundary independent subreview: Current SL0353 resolves as stroma and may optionally enrich the label-only node. This does not establish that a dated historical inaccessible-accession note was false, require history rewriting or settle an unexamined broader issue.
- Four chromatophore membrane-boundary independent subreview: All four physical/material records are genuine structured-source exclusions; empty protein inventories are not the deciding criterion. Fresh official catalogue has no matching Paulinella host. No unmatched bacterial proxy or downstream module query performed. Historical00:49Z adapter PermissionError remains separately dated and is not a new execution.
- Four chromatophore membrane-boundary independent subreview: Current native eight protein commands pass with zero examples and zero GENE_OR_PROTEIN nodes. Their generic verify-success text does not establish complete protein/family coverage. All68 original hashes are provenance checks; unfrozen historical neighboring records were not newly scientifically assessed.
- Four chromatophore membrane-boundary independent subreview: No records, immutable review pairs, history, generated files, Git or GitHub state changed. Root owns cohort QC/CI/publication/queue checks; no future CI or merge is certified by this source report.
- Historical observations remain immutable; their old checks are not represented as current-head execution.
- The adapter runner was not rerun after the canary established OS access failure. Catalogue-based coverage is assessed directly; fresh and reused responses retain actual access timestamps.
- Native label checks include 923 no-adapter skips. Native identifier checks include 909 PMID transport failures and 254 skipped identifiers; bounded supplemental checks independently resolve the 909 PMIDs.
- Scientific record-curation findings stay in separate issues; no record is edited by this review PR.
- Final trusted-base post-save review-check, exact-head independent acceptance, final-head CI and merge-group CI occur after saving this immutable observation and are not represented here as already completed.
- All ten original YAML/Markdown pairs remain unchanged. Current main was merged normally and pushed without force. All ten target hashes match their original frozen inputs; no stale-refresh issue is invented.
- This explicit issue-bearing ten-record cohort follows native persistence policy. Inherited scientific findings retain stable keys and exact predecessor repository/review/finding identities; any new finding has no invented predecessor.
- Issue2755 tracks four unsupported expression-only applicability exclusions: thylakoid, thylakoid membrane, osmiophilic body and whole parasitophorous vacuole. The PV trigger is its positive BioID/PVM-associated protein assertion, not an invented nutrient mechanism. All ten originals contained explicit exclusions; none was missing.
- Six records have genuine physical/material-topology scope: the four chromatophore envelope boundary records, thylakoid lumen and PV lumen. Molecular import, photosynthetic, lumenal-protein or transport machinery is explicitly excluded or withheld. A broader source description alone does not imply a compartment-specific mechanism.
- Source commit bdd5beb85634420b1d99c91138a9121631087f89 is retained by tag review-base/pr2373-current-record-followup-20261103.
- CLAUDE.md aliases AGENTS.md; canonical regular AGENTS.md bytes are frozen. Every used local context input is frozen before its assessment.
- Fresh and reused source snapshots retain actual access times and inspection tiers. Native identifier identity does not independently establish structure membership, experimental intervention scope or assembly necessity.
- All twenty native protein commands returned zero. Osmiophilic body has one unreviewed A0A059WIJ2 example and one COVERED typed node; the native result is separate from the fragment scope and source-specific egress/counterevidence assessment. The other nine records have zero examples and zero typed molecular nodes. Optional example absence alone is not a scientific defect.
- Current CausalNode schema permits protein families and complexes as GENE_OR_PROTEIN nodes. Label-only collective lipid material and explicitly unresolved peptidoglycan composition are distinct from erroneously grounding a molecular component to an entire membrane structure.
- Related issues2753/2754 concern the whole chromatophore record and do not dispose of the present thylakoid-record findings. Native-validator2514 remains open and reused; no scientific record or resolver is edited.
- The osmiophilic-body finding concerns present functional/causal assertions contradicted by cited counterevidence, not a requirement to erase historical rationale. Separately authorized curation must preserve append-only rationale and use appended context or current-state notes.
- Final trusted-base review-check, exact-head independent acceptance, final-head CI and merge-group CI occur after this immutable observation and are not represented as already completed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T184731Z-pr2373-current-record-followup
kind: batch
repository: CultureBotAI/CellStructureMech
title: 'PR 2373: current-input review of ten records and adversarial follow-up'
started_at: '2026-11-03T18:39:37.063967Z'
finished_at: '2026-11-03T18:47:31Z'
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
summary: 'Current-input adversarial follow-up for the complete ten-record cohort after
  merging main. All ten original target hashes still match, so no stale refresh is
  required. Four unsupported expression-only structured-source exclusions are corrected;
  six genuine physical/material-topology exclusions are preserved. Four inherited
  findings remain open (three major and one minor) across three records: thylakoid
  membrane-component identity and source attribution, osmiophilic-body egress counterevidence,
  and parasitophorous-vacuole canonical-example species attribution. Seven targets
  retain qualified positive assessments. All original review observations and scientific
  records remain unchanged.'
source:
  git_revision: bdd5beb85634420b1d99c91138a9121631087f89
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
  - path: data/structures/membrane_organelle/organellar_chromatophore.yaml
    sha256: b217af7ad434f269a5b8cba2428be5cd988746a75c34a999d7b69909160fcba4
    role: context
  - path: data/structures/membrane_organelle/organellar_chromatophore_inner_membrane.yaml
    sha256: e3c244a36b1484e5d3ca95aa114de0a719660aa4d76ae1811ed12584b3d72b1e
    role: target
  - path: data/structures/membrane_organelle/organellar_chromatophore_intermembrane_space.yaml
    sha256: f67ae10cda248a93eba761943f430c0ea5e6d4550dcf9514611822866d2c98ed
    role: target
  - path: data/structures/membrane_organelle/organellar_chromatophore_membrane.yaml
    sha256: 179b7a8a2519cb216889baed1305e54b1de332688cbb7bac1c24857f1209a794
    role: target
  - path: data/structures/membrane_organelle/organellar_chromatophore_outer_membrane.yaml
    sha256: f7d415a8e211d48ef9ecf5f0bb1b96a0ac3336c1ce6498d78d9bf0033bce3c11
    role: target
  - path: data/structures/membrane_organelle/organellar_chromatophore_thylakoid.yaml
    sha256: 6ce01ac746d2a475719c41e8eea903b510d96648cff04a1338248feb3558731a
    role: target
  - path: data/structures/membrane_organelle/organellar_chromatophore_thylakoid_lumen.yaml
    sha256: 6d012bda5b45cabee640a9a066a9ceb0f0a61e1b26d13214370ad299b185c2fa
    role: target
  - path: data/structures/membrane_organelle/organellar_chromatophore_thylakoid_membrane.yaml
    sha256: 67a0433476fdb5ca77a1a30bb921d4d80603a5ae1c61869162edf87f07d6364b
    role: target
  - path: data/structures/membrane_organelle/osmiophilic_body.yaml
    sha256: 12985dc29b3e81008d138f3de6e0e10b93090ff200e538a105f24a7c171bfafc
    role: target
  - path: data/structures/membrane_organelle/parasitophorous_vacuole.yaml
    sha256: bc5b288dc20d549717192249a6d0889856bdaf66fe33b61cd213b503f4d6f610
    role: target
  - path: data/structures/membrane_organelle/parasitophorous_vacuole_lumen.yaml
    sha256: 4a2a0820584215f4a76152f44d66e365ed67a663527da333d2e6c00d24bc244f
    role: target
  - path: data/structures/membrane_organelle/parasitophorous_vacuole_membrane.yaml
    sha256: fceffba04e82c2b88ce9fc1a9366c8931296169b4146291996ebe84f3dc213da
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
  - path: reviews/structured/20261022T030049Z-organellar-chromatophore-inner-membrane-audit/review.md
    sha256: 57d4d8eb45de36f36e4e46d9bbfbfc166f5338bec82326b12ff43fea3349767b
    role: context
  - path: reviews/structured/20261022T030049Z-organellar-chromatophore-inner-membrane-audit/review.yaml
    sha256: a3d2e2d1e5513e7c7f67424c3c8bffe16540dc97cdf9d1cf02c3c4b8113c1ef6
    role: context
  - path: reviews/structured/20261022T030050Z-organellar-chromatophore-intermembrane-space-audit/review.md
    sha256: 9c44847bc699d99d4122f12b03dce2c2f93ff2bfee9f7827866a304f79d8d70a
    role: context
  - path: reviews/structured/20261022T030050Z-organellar-chromatophore-intermembrane-space-audit/review.yaml
    sha256: a70e222696f0636c07d2f95bb8125369a4455821a3db1333d69b9e4d7d4603df
    role: context
  - path: reviews/structured/20261022T030051Z-organellar-chromatophore-membrane-audit/review.md
    sha256: 1385449e0e675990e2d872b5cb889ba989a737285b751694d6435a171861d071
    role: context
  - path: reviews/structured/20261022T030051Z-organellar-chromatophore-membrane-audit/review.yaml
    sha256: f2253bcdd27a440466a7435616878f98e75481daf0e96d3504086f9464d4542e
    role: context
  - path: reviews/structured/20261022T030052Z-organellar-chromatophore-outer-membrane-audit/review.md
    sha256: 82cbf54d047fd212e3cc8fe96e5f90466690e7eb7b01cac33140124124a6546a
    role: context
  - path: reviews/structured/20261022T030052Z-organellar-chromatophore-outer-membrane-audit/review.yaml
    sha256: bd2d739dd21cc8a719072fb015e3489d95c1d4162321116aaeb74be8f1114903
    role: context
  - path: reviews/structured/20261022T030053Z-organellar-chromatophore-thylakoid-audit/review.md
    sha256: 17e4b3e9ced4166723f7730deaf16eb52828a7a5ecb2e2769d0d34fc52800747
    role: context
  - path: reviews/structured/20261022T030053Z-organellar-chromatophore-thylakoid-audit/review.yaml
    sha256: 44a19fa8fea6581c937c842764788ee153bcf27a887619009aaa3471d3593a85
    role: context
  - path: reviews/structured/20261022T030054Z-organellar-chromatophore-thylakoid-lumen-audit/review.md
    sha256: 8018d88dffa09659b7e0940605c1c1a6e7f41b41d371d5df067de6885963283a
    role: context
  - path: reviews/structured/20261022T030054Z-organellar-chromatophore-thylakoid-lumen-audit/review.yaml
    sha256: 1da3555206cfb3e0766e2569f4dc465dc9f34d8dd7bb15906b414f2f6d637acf
    role: context
  - path: reviews/structured/20261022T030055Z-organellar-chromatophore-thylakoid-membrane-audit/review.md
    sha256: c159bcb498eef9c78ca3191f0564abf3ec1ca4121d7cbe3ac549b3253a5614a0
    role: context
  - path: reviews/structured/20261022T030055Z-organellar-chromatophore-thylakoid-membrane-audit/review.yaml
    sha256: 84fe876ec2a41c3ff909a9db1d55c6b99462177b31c64a24d7fa0aaf7ef88ecd
    role: context
  - path: reviews/structured/20261022T030055Z-osmiophilic-body-audit/review.md
    sha256: b5bfba064ab47a4e755ca82fbee0e211ec2cc548cc4c341ec3e17174b87bbef7
    role: context
  - path: reviews/structured/20261022T030055Z-osmiophilic-body-audit/review.yaml
    sha256: 19f0e9ef81cc68c474070bbff51c31d5d6e0f95354aa78fe0632de49aaf0038e
    role: context
  - path: reviews/structured/20261022T030057Z-parasitophorous-vacuole-audit/review.md
    sha256: 969abfb546cf428e81ce75bd279d42db0ee9494792a04d0f6d56cfc14594e405
    role: context
  - path: reviews/structured/20261022T030057Z-parasitophorous-vacuole-audit/review.yaml
    sha256: 29741e03b22cd0add2a9183d1fd828a20ec5a1a2404524582fde3f342b0814a1
    role: context
  - path: reviews/structured/20261022T030057Z-parasitophorous-vacuole-lumen-audit/review.md
    sha256: f9ca994f55fd48dcfd7690a0ed6714d797b2f15d6e8fb7bb18620c22bc504922
    role: context
  - path: reviews/structured/20261022T030057Z-parasitophorous-vacuole-lumen-audit/review.yaml
    sha256: 30b6e039312bb9dae5829d7823213003b3d3603da706b941a200cee35405ae2c
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
- target_id: GO:0070113
  path: data/structures/membrane_organelle/organellar_chromatophore_inner_membrane.yaml
  label: organellar chromatophore inner membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/organellar_chromatophore_inner_membrane.yaml
    role: maintained scientific record
- target_id: GO:0070115
  path: data/structures/membrane_organelle/organellar_chromatophore_intermembrane_space.yaml
  label: organellar chromatophore intermembrane space
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/organellar_chromatophore_intermembrane_space.yaml
    role: maintained scientific record
- target_id: GO:0070112
  path: data/structures/membrane_organelle/organellar_chromatophore_membrane.yaml
  label: organellar chromatophore membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/organellar_chromatophore_membrane.yaml
    role: maintained scientific record
- target_id: GO:0070114
  path: data/structures/membrane_organelle/organellar_chromatophore_outer_membrane.yaml
  label: organellar chromatophore outer membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/organellar_chromatophore_outer_membrane.yaml
    role: maintained scientific record
- target_id: GO:0070116
  path: data/structures/membrane_organelle/organellar_chromatophore_thylakoid.yaml
  label: organellar chromatophore thylakoid
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/organellar_chromatophore_thylakoid.yaml
    role: maintained scientific record
- target_id: GO:0070117
  path: data/structures/membrane_organelle/organellar_chromatophore_thylakoid_lumen.yaml
  label: organellar chromatophore thylakoid lumen
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/organellar_chromatophore_thylakoid_lumen.yaml
    role: maintained scientific record
- target_id: GO:0070118
  path: data/structures/membrane_organelle/organellar_chromatophore_thylakoid_membrane.yaml
  label: organellar chromatophore thylakoid membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/organellar_chromatophore_thylakoid_membrane.yaml
    role: maintained scientific record
- target_id: GO:0044310
  path: data/structures/membrane_organelle/osmiophilic_body.yaml
  label: osmiophilic body
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/osmiophilic_body.yaml
    role: maintained scientific record
- target_id: cellstructuremech:parasitophorous_vacuole
  path: data/structures/membrane_organelle/parasitophorous_vacuole.yaml
  label: parasitophorous vacuole
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/parasitophorous_vacuole.yaml
    role: maintained scientific record
- target_id: cellstructuremech:parasitophorous_vacuole_lumen
  path: data/structures/membrane_organelle/parasitophorous_vacuole_lumen.yaml
  label: parasitophorous vacuole lumen
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/parasitophorous_vacuole_lumen.yaml
    role: maintained scientific record
scope:
  description: Exact ten-record PR cohort reassessed against current main fa4d81142ca76aa4b656afbbf0ac2caa3e16c952.
    Changed inputs are substantively reassessed. Scientific records remain unchanged.
  selection: Complete cohort of ten maintained records reviewed in original PR head
    36e49e748537472bbfdb4ac0fa6b864a40ecd661.
  coverage: full
  population_size: 10
  reviewed_target_ids:
  - GO:0070113
  - GO:0070115
  - GO:0070112
  - GO:0070114
  - GO:0070116
  - GO:0070117
  - GO:0070118
  - GO:0044310
  - cellstructuremech:parasitophorous_vacuole
  - cellstructuremech:parasitophorous_vacuole_lumen
checks:
- check_id: qc
  name: Full native QC
  status: passed
  required: true
  target_ids:
  - GO:0070113
  - GO:0070115
  - GO:0070112
  - GO:0070114
  - GO:0070116
  - GO:0070117
  - GO:0070118
  - GO:0044310
  - cellstructuremech:parasitophorous_vacuole
  - cellstructuremech:parasitophorous_vacuole_lumen
  command: just qc
  exit_code: 0
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  scope_note: Actual local execution at main-merge head bdd5beb85634420b1d99c91138a9121631087f89.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-qc
- check_id: labels
  name: Native label correspondence
  status: passed
  required: true
  target_ids:
  - GO:0070113
  - GO:0070115
  - GO:0070112
  - GO:0070114
  - GO:0070116
  - GO:0070117
  - GO:0070118
  - GO:0044310
  - cellstructuremech:parasitophorous_vacuole
  - cellstructuremech:parasitophorous_vacuole_lumen
  command: just validate-products
  exit_code: 0
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  scope_note: Actual local execution at main-merge head bdd5beb85634420b1d99c91138a9121631087f89.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-labels
- check_id: trait-links
  name: TraitMech references
  status: passed
  required: true
  target_ids:
  - GO:0070113
  - GO:0070115
  - GO:0070112
  - GO:0070114
  - GO:0070116
  - GO:0070117
  - GO:0070118
  - GO:0044310
  - cellstructuremech:parasitophorous_vacuole
  - cellstructuremech:parasitophorous_vacuole_lumen
  command: just check-trait-links --check
  exit_code: 0
  summary: Native TraitMech link check passed.
  scope_note: Actual local execution at main-merge head bdd5beb85634420b1d99c91138a9121631087f89.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-trait-links
- check_id: vendored
  name: Pinned governed files
  status: passed
  required: true
  target_ids:
  - GO:0070113
  - GO:0070115
  - GO:0070112
  - GO:0070114
  - GO:0070116
  - GO:0070117
  - GO:0070118
  - GO:0044310
  - cellstructuremech:parasitophorous_vacuole
  - cellstructuremech:parasitophorous_vacuole_lumen
  command: just vendored-check
  exit_code: 0
  summary: Pinned governed files match; native vendored check passed.
  scope_note: Actual local execution at main-merge head bdd5beb85634420b1d99c91138a9121631087f89.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-vendored
- check_id: curies
  name: Native identifier resolver
  status: passed
  required: true
  target_ids:
  - GO:0070113
  - GO:0070115
  - GO:0070112
  - GO:0070114
  - GO:0070116
  - GO:0070117
  - GO:0070118
  - GO:0044310
  - cellstructuremech:parasitophorous_vacuole
  - cellstructuremech:parasitophorous_vacuole_lumen
  command: just check-curies
  exit_code: 0
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  scope_note: Actual local execution at main-merge head bdd5beb85634420b1d99c91138a9121631087f89.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-curies
- check_id: focused-0
  name: validate GO:0070113
  status: passed
  required: true
  target_ids:
  - GO:0070113
  command: just validate data/structures/membrane_organelle/organellar_chromatophore_inner_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-1
  name: validate-strict GO:0070113
  status: passed
  required: true
  target_ids:
  - GO:0070113
  command: just validate-strict data/structures/membrane_organelle/organellar_chromatophore_inner_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-2
  name: validate GO:0070115
  status: passed
  required: true
  target_ids:
  - GO:0070115
  command: just validate data/structures/membrane_organelle/organellar_chromatophore_intermembrane_space.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-3
  name: validate-strict GO:0070115
  status: passed
  required: true
  target_ids:
  - GO:0070115
  command: just validate-strict data/structures/membrane_organelle/organellar_chromatophore_intermembrane_space.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-4
  name: validate GO:0070112
  status: passed
  required: true
  target_ids:
  - GO:0070112
  command: just validate data/structures/membrane_organelle/organellar_chromatophore_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-5
  name: validate-strict GO:0070112
  status: passed
  required: true
  target_ids:
  - GO:0070112
  command: just validate-strict data/structures/membrane_organelle/organellar_chromatophore_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-6
  name: validate GO:0070114
  status: passed
  required: true
  target_ids:
  - GO:0070114
  command: just validate data/structures/membrane_organelle/organellar_chromatophore_outer_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-7
  name: validate-strict GO:0070114
  status: passed
  required: true
  target_ids:
  - GO:0070114
  command: just validate-strict data/structures/membrane_organelle/organellar_chromatophore_outer_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-8
  name: validate GO:0070116
  status: passed
  required: true
  target_ids:
  - GO:0070116
  command: just validate data/structures/membrane_organelle/organellar_chromatophore_thylakoid.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-9
  name: validate-strict GO:0070116
  status: passed
  required: true
  target_ids:
  - GO:0070116
  command: just validate-strict data/structures/membrane_organelle/organellar_chromatophore_thylakoid.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-10
  name: validate GO:0070117
  status: passed
  required: true
  target_ids:
  - GO:0070117
  command: just validate data/structures/membrane_organelle/organellar_chromatophore_thylakoid_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-11
  name: validate-strict GO:0070117
  status: passed
  required: true
  target_ids:
  - GO:0070117
  command: just validate-strict data/structures/membrane_organelle/organellar_chromatophore_thylakoid_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-12
  name: validate GO:0070118
  status: passed
  required: true
  target_ids:
  - GO:0070118
  command: just validate data/structures/membrane_organelle/organellar_chromatophore_thylakoid_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-13
  name: validate-strict GO:0070118
  status: passed
  required: true
  target_ids:
  - GO:0070118
  command: just validate-strict data/structures/membrane_organelle/organellar_chromatophore_thylakoid_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-14
  name: validate GO:0044310
  status: passed
  required: true
  target_ids:
  - GO:0044310
  command: just validate data/structures/membrane_organelle/osmiophilic_body.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-15
  name: validate-strict GO:0044310
  status: passed
  required: true
  target_ids:
  - GO:0044310
  command: just validate-strict data/structures/membrane_organelle/osmiophilic_body.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-16
  name: validate cellstructuremech:parasitophorous_vacuole
  status: passed
  required: true
  target_ids:
  - cellstructuremech:parasitophorous_vacuole
  command: just validate data/structures/membrane_organelle/parasitophorous_vacuole.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-17
  name: validate-strict cellstructuremech:parasitophorous_vacuole
  status: passed
  required: true
  target_ids:
  - cellstructuremech:parasitophorous_vacuole
  command: just validate-strict data/structures/membrane_organelle/parasitophorous_vacuole.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-18
  name: validate cellstructuremech:parasitophorous_vacuole_lumen
  status: passed
  required: true
  target_ids:
  - cellstructuremech:parasitophorous_vacuole_lumen
  command: just validate data/structures/membrane_organelle/parasitophorous_vacuole_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-19
  name: validate-strict cellstructuremech:parasitophorous_vacuole_lumen
  status: passed
  required: true
  target_ids:
  - cellstructuremech:parasitophorous_vacuole_lumen
  command: just validate-strict data/structures/membrane_organelle/parasitophorous_vacuole_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: supplemental-pmid
  name: Supplemental bounded PMID authority checks
  status: passed
  required: true
  target_ids:
  - GO:0070113
  - GO:0070115
  - GO:0070112
  - GO:0070114
  - GO:0070116
  - GO:0070117
  - GO:0070118
  - GO:0044310
  - cellstructuremech:parasitophorous_vacuole
  - cellstructuremech:parasitophorous_vacuole_lumen
  command: .venv/bin/python /private/tmp/cellstructure-batches-2346-2397-20261103/check_pmid_chunks.py
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373
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
  - GO:0070113
  - GO:0070115
  - GO:0070112
  - GO:0070114
  - GO:0070116
  - GO:0070117
  - GO:0070118
  - GO:0044310
  - cellstructuremech:parasitophorous_vacuole
  - cellstructuremech:parasitophorous_vacuole_lumen
  summary: 'Four records make positive molecular claims and require source applicability
    assessment: chromatophore thylakoid and thylakoid membrane assert photosynthetic
    light-reaction complexes; osmiophilic body asserts Pfg377 and emergence/egress;
    whole parasitophorous vacuole makes a positive BioID/PVM-associated protein assertion.
    Current official iModulonDB catalogue coverage is checked for the relevant hosts/strains;
    unmatched datasets are not proxies and noncoverage is not biological absence.
    Four chromatophore envelope-boundary records plus thylakoid lumen and PV lumen
    retain genuine physical/topology exclusions. Historical00:49Z runner unavailability
    stays historical, with actual public-source fallback coverage and access limits
    recorded.'
  evidence_ids:
  - septin-catalogue
  - plaque-catalogue
  - micro-catalogue
- check_id: independent-scientific-review
  name: Independent claim-level source review
  status: passed
  required: true
  target_ids:
  - GO:0070113
  - GO:0070115
  - GO:0070112
  - GO:0070114
  - GO:0070116
  - GO:0070117
  - GO:0070118
  - GO:0044310
  - cellstructuremech:parasitophorous_vacuole
  - cellstructuremech:parasitophorous_vacuole_lumen
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
  - septin-SL0354
  - septin-SL0355
  - septin-SL0356
  - septin-tax39716
  - septin-GO0070116-isa
  - septin-GO0070117-isa
  - septin-GO0070118-isa
  - septin-tax39717
  - septin-nowack2014-crossref
  - septin-nowack2012-prefixed
  - plaque-policy
  - plaque-rubric
  - plaque-graph-rubric
  - plaque-protein-contract
  - plaque-schema-policy
  - plaque-go
  - plaque-SL-0193
  - plaque-SL-0194
  - plaque-SL-0341
  - plaque-tax5794
  - plaque-tax5811
  - plaque-tax5833
  - plaque-tax5821
  - plaque-pfg377
  - plaque-alano1995-pmid
  - plaque-dekoning2008-meta
  - plaque-suarez2016-meta
  - plaque-schnider2018-meta
  - plaque-lingelbach1998-meta
  - plaque-clough2017-meta
  - plaque-dekoning2008-repository
  - plaque-suarez2016-pmc
  - plaque-schnider2018-body
  - plaque-catalogue
  - micro-policy
  - micro-component-policy
  - micro-graph-policy
  - micro-go
  - micro-go-0070112-isa
  - micro-go-0070113-isa
  - micro-go-0070114-isa
  - micro-go-0070115-isa
  - micro-SL0351
  - micro-SL0352
  - micro-SL0359
  - micro-SL0360
  - micro-SL0361
  - micro-SL0353
  - micro-tax39716
  - micro-gabr2020-meta
  - micro-nowack2012-meta
  - micro-nowack2012-body
  - micro-gabr2020-canonical
- check_id: historical-adapter-runner
  name: Retained historical adapter runner availability
  status: unavailable
  required: false
  target_ids:
  - GO:0070113
  - GO:0070115
  - GO:0070112
  - GO:0070114
  - GO:0070116
  - GO:0070117
  - GO:0070118
  - GO:0044310
  - cellstructuremech:parasitophorous_vacuole
  - cellstructuremech:parasitophorous_vacuole_lumen
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
- check_id: organellar_chromatophore_inner_membrane-uniprot-verify
  name: Native organellar chromatophore inner membrane UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0070113
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/organellar_chromatophore_inner_membrane.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples or typed molecular
    nodes. Positive molecular/pathway assertions and justified physical-scope exclusions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-organellar_chromatophore_inner_membrane-verify
- check_id: organellar_chromatophore_inner_membrane-uniprot-causal
  name: Native organellar chromatophore inner membrane UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0070113
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/organellar_chromatophore_inner_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples or typed molecular
    nodes. Positive molecular/pathway assertions and justified physical-scope exclusions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-organellar_chromatophore_inner_membrane-causal
- check_id: organellar_chromatophore_intermembrane_space-uniprot-verify
  name: Native organellar chromatophore intermembrane space UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0070115
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/organellar_chromatophore_intermembrane_space.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples or typed molecular
    nodes. Positive molecular/pathway assertions and justified physical-scope exclusions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-organellar_chromatophore_intermembrane_space-verify
- check_id: organellar_chromatophore_intermembrane_space-uniprot-causal
  name: Native organellar chromatophore intermembrane space UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0070115
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/organellar_chromatophore_intermembrane_space.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples or typed molecular
    nodes. Positive molecular/pathway assertions and justified physical-scope exclusions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-organellar_chromatophore_intermembrane_space-causal
- check_id: organellar_chromatophore_membrane-uniprot-verify
  name: Native organellar chromatophore membrane UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0070112
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/organellar_chromatophore_membrane.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples or typed molecular
    nodes. Positive molecular/pathway assertions and justified physical-scope exclusions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-organellar_chromatophore_membrane-verify
- check_id: organellar_chromatophore_membrane-uniprot-causal
  name: Native organellar chromatophore membrane UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0070112
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/organellar_chromatophore_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples or typed molecular
    nodes. Positive molecular/pathway assertions and justified physical-scope exclusions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-organellar_chromatophore_membrane-causal
- check_id: organellar_chromatophore_outer_membrane-uniprot-verify
  name: Native organellar chromatophore outer membrane UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0070114
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/organellar_chromatophore_outer_membrane.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples or typed molecular
    nodes. Positive molecular/pathway assertions and justified physical-scope exclusions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-organellar_chromatophore_outer_membrane-verify
- check_id: organellar_chromatophore_outer_membrane-uniprot-causal
  name: Native organellar chromatophore outer membrane UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0070114
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/organellar_chromatophore_outer_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples or typed molecular
    nodes. Positive molecular/pathway assertions and justified physical-scope exclusions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-organellar_chromatophore_outer_membrane-causal
- check_id: organellar_chromatophore_thylakoid-uniprot-verify
  name: Native organellar chromatophore thylakoid UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0070116
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/organellar_chromatophore_thylakoid.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples or typed molecular
    nodes. Positive molecular/pathway assertions and justified physical-scope exclusions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-organellar_chromatophore_thylakoid-verify
- check_id: organellar_chromatophore_thylakoid-uniprot-causal
  name: Native organellar chromatophore thylakoid UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0070116
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/organellar_chromatophore_thylakoid.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples or typed molecular
    nodes. Positive molecular/pathway assertions and justified physical-scope exclusions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-organellar_chromatophore_thylakoid-causal
- check_id: organellar_chromatophore_thylakoid_lumen-uniprot-verify
  name: Native organellar chromatophore thylakoid lumen UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0070117
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/organellar_chromatophore_thylakoid_lumen.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples or typed molecular
    nodes. Positive molecular/pathway assertions and justified physical-scope exclusions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-organellar_chromatophore_thylakoid_lumen-verify
- check_id: organellar_chromatophore_thylakoid_lumen-uniprot-causal
  name: Native organellar chromatophore thylakoid lumen UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0070117
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/organellar_chromatophore_thylakoid_lumen.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples or typed molecular
    nodes. Positive molecular/pathway assertions and justified physical-scope exclusions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-organellar_chromatophore_thylakoid_lumen-causal
- check_id: organellar_chromatophore_thylakoid_membrane-uniprot-verify
  name: Native organellar chromatophore thylakoid membrane UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0070118
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/organellar_chromatophore_thylakoid_membrane.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples or typed molecular
    nodes. Positive molecular/pathway assertions and justified physical-scope exclusions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-organellar_chromatophore_thylakoid_membrane-verify
- check_id: organellar_chromatophore_thylakoid_membrane-uniprot-causal
  name: Native organellar chromatophore thylakoid membrane UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0070118
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/organellar_chromatophore_thylakoid_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples or typed molecular
    nodes. Positive molecular/pathway assertions and justified physical-scope exclusions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-organellar_chromatophore_thylakoid_membrane-causal
- check_id: osmiophilic_body-uniprot-verify
  name: Native osmiophilic body UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0044310
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/osmiophilic_body.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. One unreviewed A0A059WIJ2/Pfg377
    example and one COVERED typed node. Native identifier correspondence is separate
    from fragment scope, localization, source-specific genetic phenotypes and contradictory
    egress evidence.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-osmiophilic_body-verify
- check_id: osmiophilic_body-uniprot-causal
  name: Native osmiophilic body UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0044310
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/osmiophilic_body.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. One unreviewed A0A059WIJ2/Pfg377
    example and one COVERED typed node. Native identifier correspondence is separate
    from fragment scope, localization, source-specific genetic phenotypes and contradictory
    egress evidence.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-osmiophilic_body-causal
- check_id: parasitophorous_vacuole-uniprot-verify
  name: Native parasitophorous vacuole UniProt verify check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:parasitophorous_vacuole
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/parasitophorous_vacuole.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples or typed molecular
    nodes. Positive molecular/pathway assertions and justified physical-scope exclusions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-parasitophorous_vacuole-verify
- check_id: parasitophorous_vacuole-uniprot-causal
  name: Native parasitophorous vacuole UniProt causal check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:parasitophorous_vacuole
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/parasitophorous_vacuole.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples or typed molecular
    nodes. Positive molecular/pathway assertions and justified physical-scope exclusions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-parasitophorous_vacuole-causal
- check_id: parasitophorous_vacuole_lumen-uniprot-verify
  name: Native parasitophorous vacuole lumen UniProt verify check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:parasitophorous_vacuole_lumen
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/parasitophorous_vacuole_lumen.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples or typed molecular
    nodes. Positive molecular/pathway assertions and justified physical-scope exclusions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-parasitophorous_vacuole_lumen-verify
- check_id: parasitophorous_vacuole_lumen-uniprot-causal
  name: Native parasitophorous vacuole lumen UniProt causal check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:parasitophorous_vacuole_lumen
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/parasitophorous_vacuole_lumen.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples or typed molecular
    nodes. Positive molecular/pathway assertions and justified physical-scope exclusions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-parasitophorous_vacuole_lumen-causal
evidence:
- evidence_id: current-record-0
  kind: record_content
  reference: data/structures/membrane_organelle/organellar_chromatophore_inner_membrane.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T18:47:31Z'
  support: context_only
  summary: Original frozen SHA256 e3c244a36b1484e5d3ca95aa114de0a719660aa4d76ae1811ed12584b3d72b1e;
    current SHA256 e3c244a36b1484e5d3ca95aa114de0a719660aa4d76ae1811ed12584b3d72b1e.
    Record bytes unchanged since the original review.
  snapshot_sha256: e3c244a36b1484e5d3ca95aa114de0a719660aa4d76ae1811ed12584b3d72b1e
- evidence_id: original-review-0
  kind: prior_review
  reference: reviews/structured/20261022T030049Z-organellar-chromatophore-inner-membrane-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T18:47:31Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: a3d2e2d1e5513e7c7f67424c3c8bffe16540dc97cdf9d1cf02c3c4b8113c1ef6
- evidence_id: current-record-1
  kind: record_content
  reference: data/structures/membrane_organelle/organellar_chromatophore_intermembrane_space.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T18:47:31Z'
  support: context_only
  summary: Original frozen SHA256 f67ae10cda248a93eba761943f430c0ea5e6d4550dcf9514611822866d2c98ed;
    current SHA256 f67ae10cda248a93eba761943f430c0ea5e6d4550dcf9514611822866d2c98ed.
    Record bytes unchanged since the original review.
  snapshot_sha256: f67ae10cda248a93eba761943f430c0ea5e6d4550dcf9514611822866d2c98ed
- evidence_id: original-review-1
  kind: prior_review
  reference: reviews/structured/20261022T030050Z-organellar-chromatophore-intermembrane-space-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T18:47:31Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: a70e222696f0636c07d2f95bb8125369a4455821a3db1333d69b9e4d7d4603df
- evidence_id: current-record-2
  kind: record_content
  reference: data/structures/membrane_organelle/organellar_chromatophore_membrane.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T18:47:31Z'
  support: context_only
  summary: Original frozen SHA256 179b7a8a2519cb216889baed1305e54b1de332688cbb7bac1c24857f1209a794;
    current SHA256 179b7a8a2519cb216889baed1305e54b1de332688cbb7bac1c24857f1209a794.
    Record bytes unchanged since the original review.
  snapshot_sha256: 179b7a8a2519cb216889baed1305e54b1de332688cbb7bac1c24857f1209a794
- evidence_id: original-review-2
  kind: prior_review
  reference: reviews/structured/20261022T030051Z-organellar-chromatophore-membrane-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T18:47:31Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: f2253bcdd27a440466a7435616878f98e75481daf0e96d3504086f9464d4542e
- evidence_id: current-record-3
  kind: record_content
  reference: data/structures/membrane_organelle/organellar_chromatophore_outer_membrane.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T18:47:31Z'
  support: context_only
  summary: Original frozen SHA256 f7d415a8e211d48ef9ecf5f0bb1b96a0ac3336c1ce6498d78d9bf0033bce3c11;
    current SHA256 f7d415a8e211d48ef9ecf5f0bb1b96a0ac3336c1ce6498d78d9bf0033bce3c11.
    Record bytes unchanged since the original review.
  snapshot_sha256: f7d415a8e211d48ef9ecf5f0bb1b96a0ac3336c1ce6498d78d9bf0033bce3c11
- evidence_id: original-review-3
  kind: prior_review
  reference: reviews/structured/20261022T030052Z-organellar-chromatophore-outer-membrane-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T18:47:31Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: bd2d739dd21cc8a719072fb015e3489d95c1d4162321116aaeb74be8f1114903
- evidence_id: current-record-4
  kind: record_content
  reference: data/structures/membrane_organelle/organellar_chromatophore_thylakoid.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T18:47:31Z'
  support: context_only
  summary: Original frozen SHA256 6ce01ac746d2a475719c41e8eea903b510d96648cff04a1338248feb3558731a;
    current SHA256 6ce01ac746d2a475719c41e8eea903b510d96648cff04a1338248feb3558731a.
    Record bytes unchanged since the original review.
  snapshot_sha256: 6ce01ac746d2a475719c41e8eea903b510d96648cff04a1338248feb3558731a
- evidence_id: original-review-4
  kind: prior_review
  reference: reviews/structured/20261022T030053Z-organellar-chromatophore-thylakoid-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T18:47:31Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 44a19fa8fea6581c937c842764788ee153bcf27a887619009aaa3471d3593a85
- evidence_id: current-record-5
  kind: record_content
  reference: data/structures/membrane_organelle/organellar_chromatophore_thylakoid_lumen.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T18:47:31Z'
  support: context_only
  summary: Original frozen SHA256 6d012bda5b45cabee640a9a066a9ceb0f0a61e1b26d13214370ad299b185c2fa;
    current SHA256 6d012bda5b45cabee640a9a066a9ceb0f0a61e1b26d13214370ad299b185c2fa.
    Record bytes unchanged since the original review.
  snapshot_sha256: 6d012bda5b45cabee640a9a066a9ceb0f0a61e1b26d13214370ad299b185c2fa
- evidence_id: original-review-5
  kind: prior_review
  reference: reviews/structured/20261022T030054Z-organellar-chromatophore-thylakoid-lumen-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T18:47:31Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 1da3555206cfb3e0766e2569f4dc465dc9f34d8dd7bb15906b414f2f6d637acf
- evidence_id: current-record-6
  kind: record_content
  reference: data/structures/membrane_organelle/organellar_chromatophore_thylakoid_membrane.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T18:47:31Z'
  support: context_only
  summary: Original frozen SHA256 67a0433476fdb5ca77a1a30bb921d4d80603a5ae1c61869162edf87f07d6364b;
    current SHA256 67a0433476fdb5ca77a1a30bb921d4d80603a5ae1c61869162edf87f07d6364b.
    Record bytes unchanged since the original review.
  snapshot_sha256: 67a0433476fdb5ca77a1a30bb921d4d80603a5ae1c61869162edf87f07d6364b
- evidence_id: original-review-6
  kind: prior_review
  reference: reviews/structured/20261022T030055Z-organellar-chromatophore-thylakoid-membrane-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T18:47:31Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 84fe876ec2a41c3ff909a9db1d55c6b99462177b31c64a24d7fa0aaf7ef88ecd
- evidence_id: current-record-7
  kind: record_content
  reference: data/structures/membrane_organelle/osmiophilic_body.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T18:47:31Z'
  support: context_only
  summary: Original frozen SHA256 12985dc29b3e81008d138f3de6e0e10b93090ff200e538a105f24a7c171bfafc;
    current SHA256 12985dc29b3e81008d138f3de6e0e10b93090ff200e538a105f24a7c171bfafc.
    Record bytes unchanged since the original review.
  snapshot_sha256: 12985dc29b3e81008d138f3de6e0e10b93090ff200e538a105f24a7c171bfafc
- evidence_id: original-review-7
  kind: prior_review
  reference: reviews/structured/20261022T030055Z-osmiophilic-body-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T18:47:31Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 19f0e9ef81cc68c474070bbff51c31d5d6e0f95354aa78fe0632de49aaf0038e
- evidence_id: current-record-8
  kind: record_content
  reference: data/structures/membrane_organelle/parasitophorous_vacuole.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T18:47:31Z'
  support: context_only
  summary: Original frozen SHA256 bc5b288dc20d549717192249a6d0889856bdaf66fe33b61cd213b503f4d6f610;
    current SHA256 bc5b288dc20d549717192249a6d0889856bdaf66fe33b61cd213b503f4d6f610.
    Record bytes unchanged since the original review.
  snapshot_sha256: bc5b288dc20d549717192249a6d0889856bdaf66fe33b61cd213b503f4d6f610
- evidence_id: original-review-8
  kind: prior_review
  reference: reviews/structured/20261022T030057Z-parasitophorous-vacuole-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T18:47:31Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 29741e03b22cd0add2a9183d1fd828a20ec5a1a2404524582fde3f342b0814a1
- evidence_id: current-record-9
  kind: record_content
  reference: data/structures/membrane_organelle/parasitophorous_vacuole_lumen.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T18:47:31Z'
  support: context_only
  summary: Original frozen SHA256 4a2a0820584215f4a76152f44d66e365ed67a663527da333d2e6c00d24bc244f;
    current SHA256 4a2a0820584215f4a76152f44d66e365ed67a663527da333d2e6c00d24bc244f.
    Record bytes unchanged since the original review.
  snapshot_sha256: 4a2a0820584215f4a76152f44d66e365ed67a663527da333d2e6c00d24bc244f
- evidence_id: original-review-9
  kind: prior_review
  reference: reviews/structured/20261022T030057Z-parasitophorous-vacuole-lumen-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T18:47:31Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 30b6e039312bb9dae5829d7823213003b3d3603da706b941a200cee35405ae2c
- evidence_id: septin-review-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Whole-record assertions, structured sources and severity rubric
  summary: Positive molecular/pathway assertions require a real applicability assessment;
    absence of expression claims alone is not an exemption. Keep source scope, uncertainty
    and original finding identity; record curation is separate.
  accessed_at: '2026-11-03T18:45:01.914264Z'
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
  accessed_at: '2026-11-03T18:45:01.914264Z'
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
  accessed_at: '2026-11-03T18:45:01.914264Z'
  support: supports
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: septin-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Graph nodes, component correspondence, source scope and necessity
  summary: Descriptive boundary graphs can remain NONMECHANISTIC; source-specific
    localization, molecular identity and organelle-formation necessity must not be
    conflated.
  accessed_at: '2026-11-03T18:45:01.914264Z'
  support: supports
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: septin-protein-policy
  kind: authority
  reference: .claude/skills/uniprot-protein-examples/SKILL.md
  locator: Step2 generic classes and native coverage report
  summary: Generic class components are explicitly recognized. A zero-example inventory
    or NO_GENE_SYMBOLS node is a stated coverage limit, not proof that the protein
    class does not exist or that its members form one stable complex.
  accessed_at: '2026-11-03T18:45:01.914264Z'
  support: supports
  snapshot_sha256: 6462894c8257823bae2b175c34693cd42f11ff9269a3829c15b9286ba6d7c876
- evidence_id: septin-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0070116,GO:0070117,GO:0070118,GO:0009579,GO:0031977,GO:0031978,GO:0042651,GO:0055035,GO:0070112,GO:0019684,GO:0070111
  locator: 'All eleven exact GO entries: identifiers, definitions, synonyms, comments
    and immediate child relations'
  summary: GO0070116 is a thylakoid in an organellar chromatophore; GO0070117 is its
    enclosed volume and GO0070118 its lipid-bilayer membrane. GO0070118 does not itself
    say that the membrane carries light-reaction complexes. GO0019684 is the light-reaction
    process. Whole anatomical membrane identifiers are not exact chemical lipid identities.
    Generic GO0009579 comment excludes the word organelle while native repository
    category guidance explicitly includes thylakoids; this vocabulary tension is retained
    without inventing a type error.
  accessed_at: '2026-11-03T18:40:47.735479Z'
  support: supports
  snapshot_sha256: f846aa619b2a7e4ceacbf8a6e8cf6a73a092c9b6e742d76555714f57a03fd265
- evidence_id: septin-SL0354
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0354.json
  locator: Complete exact UniProt location JSON, including nested isA/partOf fields
    and GO cross-references
  summary: Exact thylakoid definition explicitly describes internal interconnected
    membranes carrying complexes for photosynthetic light reactions; its identity,
    Paulinella range and whole-chromatophore parthood match. Nested parent molecular
    prose is not automatically assigned to a child spatial compartment; location protein
    statistics do not establish biological absence.
  accessed_at: '2026-11-03T18:40:47.735999Z'
  support: supports
  snapshot_sha256: a4810ddcc1c8f3cbb0e2162c5b38ab395c056ca74c7774f1ec075ede165e3903
- evidence_id: septin-SL0355
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0355.json
  locator: Complete exact UniProt location JSON, including nested isA/partOf fields
    and GO cross-references
  summary: Exact lumen is bounded by thylakoid membrane, maps GO0070117, isA plastid
    thylakoid lumen SL0309/GO0031978 and partOf thylakoid; Paulinella range does not
    imply every genus member has chromatophores. Nested parent molecular prose is
    not automatically assigned to a child spatial compartment; location protein statistics
    do not establish biological absence.
  accessed_at: '2026-11-03T18:40:47.736192Z'
  support: supports
  snapshot_sha256: 868b20f9aad65696a286aee87b5f4e6e8d9c3d39be381e46d4ff76feea319ae8
- evidence_id: septin-SL0356
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0356.json
  locator: Complete exact UniProt location JSON, including nested isA/partOf fields
    and GO cross-references
  summary: Exact membrane maps GO0070118, describes light-reaction complexes, isA
    plastid thylakoid membrane SL0216/GO0055035 and partOf thylakoid; Paulinella range
    is qualitative. Nested parent molecular prose is not automatically assigned to
    a child spatial compartment; location protein statistics do not establish biological
    absence.
  accessed_at: '2026-11-03T18:40:47.736250Z'
  support: supports
  snapshot_sha256: fd631a05c9cdbdd6ee8bc4fa220ede8d59ad460cdaecbc15e98f38709d644934
- evidence_id: septin-tax39716
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/39716.json
  locator: Complete current taxonomy identity, active status, rank and lineage
  summary: NCBITaxon39716 is active Paulinella at genus rank. Taxon identity alone
    does not establish numerical frequency or universal organelle presence.
  accessed_at: '2026-11-03T18:40:47.736298Z'
  support: supports
  snapshot_sha256: 2e74a7cc0c3a0476f9b5b94549623cc90db407aa0cacdc8014996ee13cfa258e
- evidence_id: septin-GO0070116-isa
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0070116/ancestors?relations=is_a
  locator: Complete exact QuickGO ancestors response with relations=is_a
  summary: GO0009579 is among thylakoid is_a ancestors. This response is a bounded
    ontology hierarchy observation, not an experimental mechanism or exhaustive source
    consensus.
  accessed_at: '2026-11-03T18:40:48.336246Z'
  support: supports
  snapshot_sha256: 2a2f77cbbdf186428226847de78ed299545c690fbf53f5cb7d42e2eddbe9f08d
- evidence_id: septin-GO0070117-isa
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0070117/ancestors?relations=is_a
  locator: Complete exact QuickGO ancestors response with relations=is_a
  summary: GO0031977 generic thylakoid lumen occurs, but GO0031978 plastid thylakoid
    lumen is not among the returned is_a ancestors; the latter parent has separate
    positive support in SL0355. This response is a bounded ontology hierarchy observation,
    not an experimental mechanism or exhaustive source consensus.
  accessed_at: '2026-11-03T18:40:48.347293Z'
  support: supports
  snapshot_sha256: 746deeddeaaa48dba6dc2523fd3be3cc7ca63f8c45b4a4b8f5569ffccc7877f3
- evidence_id: septin-GO0070118-isa
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0070118/ancestors?relations=is_a
  locator: Complete exact QuickGO ancestors response with relations=is_a
  summary: GO0042651 generic thylakoid membrane and GO0070112 chromatophore membrane
    occur; GO0055035 plastid thylakoid membrane is not among returned is_a ancestors,
    but SL0356 explicitly supplies that classification. This response is a bounded
    ontology hierarchy observation, not an experimental mechanism or exhaustive source
    consensus.
  accessed_at: '2026-11-03T18:40:48.491481Z'
  support: supports
  snapshot_sha256: 964663439387924de7f28043478cf2e40ffbc6a9f9516a5965227e537d1e92be
- evidence_id: septin-catalogue
  kind: search
  reference: https://imodulondb.org/api/datasets
  locator: Complete current official organism/dataset catalogue
  summary: No Paulinella, P. chromatophora or CCAC0185 host/strain appears in the
    inspected catalogue. Molecular light-reaction assertions in thylakoid and membrane
    require this applicability assessment; the lumen independently excludes molecular
    mechanisms. No matching host dataset warrants downstream gene/module checks, and
    Synechococcus or another free-living cyanobacterium is not substituted for a Paulinella
    organelle. Catalogue noncoverage is not negative biological evidence.
  accessed_at: '2026-11-03T18:40:48.333560Z'
  support: supports
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  search_scope: GET https://imodulondb.org/api/datasets at 2026-11-03T18:40:48.333560Z;
    complete response, all20 organism rows and28 organism-dataset pairs (22 distinct
    dataset strings), no filters/truncation. Inspected organism keys/names/descriptions
    and dataset keys for Paulinella, chromatophora and CCAC0185; no date restriction
    or inferred absence outside this catalogue snapshot.
- evidence_id: septin-tax39717
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/39717.json
  locator: 'Previously fetched exact taxonomy JSON independently re-read: identity,
    rank and Paulinella parent'
  summary: NCBITaxon39717 is Paulinella chromatophora species. Identity does not by
    itself establish species-wide frequency. Cached public snapshot retains its actual
    original fetch timestamp; no fresh body retrieval is claimed.
  accessed_at: '2026-11-03T18:03:01.259538Z'
  support: supports
  snapshot_sha256: f3534e3c32299238a36f87d7ba474db869e62a1636bb45879426bb0f4081f420
- evidence_id: septin-nowack2014-crossref
  kind: authority
  reference: https://api.crossref.org/works/10.5586/asbp.2014.049
  locator: Previously fetched Crossref exact DOI metadata and complete deposited abstract
    re-read; full secondary body not read
  summary: DOI10.5586/asbp.2014.049 is Eva C. M. Nowack2014 Paulinella chromatophora
    - rethinking the transition from endosymbiont to organelle. Deposited secondary
    abstract supports photosynthetic chromatophore evolutionary context; it is not
    a numerical prevalence census or direct new structural experiment. Cached public
    snapshot retains its actual original fetch timestamp; no fresh body retrieval
    is claimed.
  accessed_at: '2026-11-03T18:03:03.520052Z'
  support: supports
  snapshot_sha256: 7a5635c186a67f8d0f6b1eebbe0d69651d31f4f794592f79583b8106e2e2e16d
- evidence_id: septin-nowack2012-prefixed
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3325729/
  locator: Previously fetched genuine PMC3325729 HTML independently re-read at Results
    first two sections (PsaE localization and PsaE/PsaK1/PsaK2 association with PSI),
    Fig1/2 text captions and Methods Strain and Growth Conditions paragraph
  summary: Immunogold localization associates PsaE with thylakoids; PSI purification
    with immunoblot, mass-spectrometric/Edman characterization supports selected PSI
    subunit association. Study uses P. chromatophora CCAC0185 subisolate M0880/a,
    grown at17C in Waris-H medium under14h light/10h dark. Bounded positive molecular/localization
    evidence does not enumerate all light complexes or demonstrate each constituent
    necessary for thylakoid formation. Figure captions were read, not source pixels/supplements/raw
    data. Cached public snapshot retains its actual original fetch timestamp; no fresh
    body retrieval is claimed.
  accessed_at: '2026-11-03T18:08:44.263032Z'
  support: supports
  snapshot_sha256: 3c62e25e8dde341faf854bc462eb3e03a4cf927ce0761d0888bde710bcf07bfb
- evidence_id: septin-context-organellar_chromatophore
  kind: record_content
  reference: data/structures/membrane_organelle/organellar_chromatophore.yaml
  locator: Frozen identity, label, definition, parent_structures, part_of, has_part
    and xrefs only
  summary: Whole chromatophore boundary context was frozen before read. Reciprocal
    thylakoid identity/parthood supports local structural relations. No independent
    whole-record verdict or disposition of its distinct scientific issues is claimed.
  accessed_at: '2026-11-03T18:45:01.914264Z'
  support: supports
  snapshot_sha256: b217af7ad434f269a5b8cba2428be5cd988746a75c34a999d7b69909160fcba4
- evidence_id: septin-adapter-runner-historical
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical attempted runner only; no fresh invocation
  summary: Actual2026-11-03T00:49:00.848907Z–00:49:00.863225Z attempt ended exit1
    PermissionError reading pyvenv.cfg. This availability receipt is historical and
    separate from the fresh successful official catalogue fetch and record-specific
    applicability judgment.
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: supports
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: septin-retrieval-source-receipts
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/adversary-septin/source-receipts.json
  locator: Actual retrieval or cached-source reinspection times and exact saved hashes
  summary: Nine current official requests succeeded. Three previously fetched public
    snapshots retain original access timestamps and explicit bounded reinspection
    scope. No metadata, secondary abstract or text caption is represented as a fresh
    complete primary-body or pixel audit.
  accessed_at: '2026-11-03T18:45:01.914264Z'
  support: supports
  snapshot_sha256: 4ed6ad0644d97051ea5058dc28e710d8a41d22bc2f071e725fee82263e1bcf64
- evidence_id: septin-retrieval-reused-source-receipts
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/adversary-septin/reused-source-receipts.json
  locator: Actual retrieval or cached-source reinspection times and exact saved hashes
  summary: Nine current official requests succeeded. Three previously fetched public
    snapshots retain original access timestamps and explicit bounded reinspection
    scope. No metadata, secondary abstract or text caption is represented as a fresh
    complete primary-body or pixel audit.
  accessed_at: '2026-11-03T18:45:01.914264Z'
  support: supports
  snapshot_sha256: 9c4c95c7ab8a2a23fd19469684a83421fa8c68d1e79545eb1145d25bc6b28095
- evidence_id: septin-record-organellar_chromatophore_thylakoid
  kind: record_content
  reference: data/structures/membrane_organelle/organellar_chromatophore_thylakoid.yaml
  locator: Complete current record at bdd5beb85634420b1d99c91138a9121631087f89
  summary: Every identity, history, synonym, hierarchy, component, scope, canonical
    example, evidence, discussion and complete graph field read. No individual protein
    example/gene-symbol inventory, typed molecular node, UniProtKB graph xref, maintained
    image, numerical measurement, associated trait or verbatim snippet occurs.
  accessed_at: '2026-11-03T18:45:01.914264Z'
  support: supports
  snapshot_sha256: 6ce01ac746d2a475719c41e8eea903b510d96648cff04a1338248feb3558731a
- evidence_id: septin-original-organellar_chromatophore_thylakoid
  kind: prior_review
  reference: reviews/structured/20261022T030053Z-organellar-chromatophore-thylakoid-audit/review.yaml
  locator: Original YAML/Markdown scope, exact findings/actions, historical checks
    and limitations
  summary: Original pair remains immutable; frozen target hash matches current bytes.
    Original verdict and finding lineage were independently reassessed; old check
    disclosures are not recast as current executions.
  accessed_at: '2026-11-03T18:45:01.914264Z'
  support: supports
  snapshot_sha256: 44a19fa8fea6581c937c842764788ee153bcf27a887619009aaa3471d3593a85
- evidence_id: septin-original-validation-organellar_chromatophore_thylakoid
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/adversary-septin/original-checks.json
  locator: Actual original native validation/render plus frozen/current target hash
  summary: Native validate/render exit0 and Markdown byte equality; frozen target
    hash agrees with current target.
  accessed_at: '2026-11-03T18:41:01.268873Z'
  support: supports
  snapshot_sha256: 2e47b06139aa0b886efa9801a61d3ae38232a189cbd08e7103fbbe86f6c13674
- evidence_id: septin-native-organellar_chromatophore_thylakoid-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_thylakoid-uniprot-verify-receipt.json
  locator: Actual receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_thylakoid-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: Exit0. Actual record has zero protein examples, zero GENE_OR_PROTEIN nodes
    and no UniProtKB graph xrefs. Native success validates the empty represented identifier
    scope; it does not prove molecular inventory completeness or all biological claims.
  accessed_at: '2026-11-03T18:40:42.960212Z'
  support: supports
  snapshot_sha256: 862565df7054ac2831bd9f124413461a7afac28cb61e9fd9248f83dcbb7e4e61
- evidence_id: septin-native-organellar_chromatophore_thylakoid-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_thylakoid-uniprot-causal-receipt.json
  locator: Actual receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_thylakoid-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: Exit0. Actual record has zero protein examples, zero GENE_OR_PROTEIN nodes
    and no UniProtKB graph xrefs. Native success validates the empty represented identifier
    scope; it does not prove molecular inventory completeness or all biological claims.
  accessed_at: '2026-11-03T18:40:43.379906Z'
  support: supports
  snapshot_sha256: 14796b67f1a30df6f6ef75b9354d8a548be4c78fb49ae53d7cd80425db28edb8
- evidence_id: septin-record-organellar_chromatophore_thylakoid_lumen
  kind: record_content
  reference: data/structures/membrane_organelle/organellar_chromatophore_thylakoid_lumen.yaml
  locator: Complete current record at bdd5beb85634420b1d99c91138a9121631087f89
  summary: Every identity, history, synonym, hierarchy, component, scope, canonical
    example, evidence, discussion and complete graph field read. No individual protein
    example/gene-symbol inventory, typed molecular node, UniProtKB graph xref, maintained
    image, numerical measurement, associated trait or verbatim snippet occurs.
  accessed_at: '2026-11-03T18:45:01.914264Z'
  support: supports
  snapshot_sha256: 6d012bda5b45cabee640a9a066a9ceb0f0a61e1b26d13214370ad299b185c2fa
- evidence_id: septin-original-organellar_chromatophore_thylakoid_lumen
  kind: prior_review
  reference: reviews/structured/20261022T030054Z-organellar-chromatophore-thylakoid-lumen-audit/review.yaml
  locator: Original YAML/Markdown scope, exact findings/actions, historical checks
    and limitations
  summary: Original pair remains immutable; frozen target hash matches current bytes.
    Original verdict and finding lineage were independently reassessed; old check
    disclosures are not recast as current executions.
  accessed_at: '2026-11-03T18:45:01.914264Z'
  support: supports
  snapshot_sha256: 1da3555206cfb3e0766e2569f4dc465dc9f34d8dd7bb15906b414f2f6d637acf
- evidence_id: septin-original-validation-organellar_chromatophore_thylakoid_lumen
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/adversary-septin/original-checks.json
  locator: Actual original native validation/render plus frozen/current target hash
  summary: Native validate/render exit0 and Markdown byte equality; frozen target
    hash agrees with current target.
  accessed_at: '2026-11-03T18:41:02.469635Z'
  support: supports
  snapshot_sha256: 2e47b06139aa0b886efa9801a61d3ae38232a189cbd08e7103fbbe86f6c13674
- evidence_id: septin-native-organellar_chromatophore_thylakoid_lumen-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_thylakoid_lumen-uniprot-verify-receipt.json
  locator: Actual receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_thylakoid_lumen-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: Exit0. Actual record has zero protein examples, zero GENE_OR_PROTEIN nodes
    and no UniProtKB graph xrefs. Native success validates the empty represented identifier
    scope; it does not prove molecular inventory completeness or all biological claims.
  accessed_at: '2026-11-03T18:40:43.806086Z'
  support: supports
  snapshot_sha256: b3ae9570e859c5933e38bec92e1e91f14db890486b5934bac5ac6d5a95349117
- evidence_id: septin-native-organellar_chromatophore_thylakoid_lumen-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_thylakoid_lumen-uniprot-causal-receipt.json
  locator: Actual receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_thylakoid_lumen-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: Exit0. Actual record has zero protein examples, zero GENE_OR_PROTEIN nodes
    and no UniProtKB graph xrefs. Native success validates the empty represented identifier
    scope; it does not prove molecular inventory completeness or all biological claims.
  accessed_at: '2026-11-03T18:40:44.234481Z'
  support: supports
  snapshot_sha256: 21f7741f56aaa02e95d8faff3313d357b726469d2b258096abce1f8d6cd74d44
- evidence_id: septin-record-organellar_chromatophore_thylakoid_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/organellar_chromatophore_thylakoid_membrane.yaml
  locator: Complete current record at bdd5beb85634420b1d99c91138a9121631087f89
  summary: Every identity, history, synonym, hierarchy, component, scope, canonical
    example, evidence, discussion and complete graph field read. No individual protein
    example/gene-symbol inventory, typed molecular node, UniProtKB graph xref, maintained
    image, numerical measurement, associated trait or verbatim snippet occurs.
  accessed_at: '2026-11-03T18:45:01.914264Z'
  support: supports
  snapshot_sha256: 67a0433476fdb5ca77a1a30bb921d4d80603a5ae1c61869162edf87f07d6364b
- evidence_id: septin-original-organellar_chromatophore_thylakoid_membrane
  kind: prior_review
  reference: reviews/structured/20261022T030055Z-organellar-chromatophore-thylakoid-membrane-audit/review.yaml
  locator: Original YAML/Markdown scope, exact findings/actions, historical checks
    and limitations
  summary: Original pair remains immutable; frozen target hash matches current bytes.
    Original verdict and finding lineage were independently reassessed; old check
    disclosures are not recast as current executions.
  accessed_at: '2026-11-03T18:45:01.914264Z'
  support: supports
  snapshot_sha256: 84fe876ec2a41c3ff909a9db1d55c6b99462177b31c64a24d7fa0aaf7ef88ecd
- evidence_id: septin-original-validation-organellar_chromatophore_thylakoid_membrane
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/adversary-septin/original-checks.json
  locator: Actual original native validation/render plus frozen/current target hash
  summary: Native validate/render exit0 and Markdown byte equality; frozen target
    hash agrees with current target.
  accessed_at: '2026-11-03T18:41:03.672211Z'
  support: supports
  snapshot_sha256: 2e47b06139aa0b886efa9801a61d3ae38232a189cbd08e7103fbbe86f6c13674
- evidence_id: septin-native-organellar_chromatophore_thylakoid_membrane-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_thylakoid_membrane-uniprot-verify-receipt.json
  locator: Actual receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_thylakoid_membrane-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: Exit0. Actual record has zero protein examples, zero GENE_OR_PROTEIN nodes
    and no UniProtKB graph xrefs. Native success validates the empty represented identifier
    scope; it does not prove molecular inventory completeness or all biological claims.
  accessed_at: '2026-11-03T18:40:44.660016Z'
  support: supports
  snapshot_sha256: 07e037cc10ae0af404c3e1491d34efb1bd2ed4f671e243b33f245e157c77da37
- evidence_id: septin-native-organellar_chromatophore_thylakoid_membrane-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_thylakoid_membrane-uniprot-causal-receipt.json
  locator: Actual receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_thylakoid_membrane-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: Exit0. Actual record has zero protein examples, zero GENE_OR_PROTEIN nodes
    and no UniProtKB graph xrefs. Native success validates the empty represented identifier
    scope; it does not prove molecular inventory completeness or all biological claims.
  accessed_at: '2026-11-03T18:40:45.078308Z'
  support: supports
  snapshot_sha256: d69dd45069c0e531bb1f7b4bf1b165aed5b783f3bf9414ba289029c40376f769
- evidence_id: plaque-current-7
  kind: record_content
  reference: data/structures/membrane_organelle/osmiophilic_body.yaml
  locator: Entire current maintained record at bdd5beb85634420b1d99c91138a9121631087f89;
    all fields, graphs, discussions and history
  summary: Read complete exact target. Current bytes equal original target freeze;
    scientific reassessment is current, not a stale-input refresh.
  accessed_at: '2026-11-03T18:45:15.493119Z'
  support: supports
  snapshot_sha256: 12985dc29b3e81008d138f3de6e0e10b93090ff200e538a105f24a7c171bfafc
- evidence_id: plaque-original-7
  kind: prior_review
  reference: reviews/structured/20261022T030055Z-osmiophilic-body-audit/review.yaml
  locator: Exact staleness-selected original YAML and native Markdown; all evidence,
    assessments, checks, finding/action and source fields
  summary: Original observations remain immutable. Native validation/render and all15
    original frozen input hashes verified separately for this target.
  accessed_at: '2026-11-03T18:45:15.493119Z'
  support: supports
  snapshot_sha256: 19f0e9ef81cc68c474070bbff51c31d5d6e0f95354aa78fe0632de49aaf0038e
- evidence_id: plaque-current-8
  kind: record_content
  reference: data/structures/membrane_organelle/parasitophorous_vacuole.yaml
  locator: Entire current maintained record at bdd5beb85634420b1d99c91138a9121631087f89;
    all fields, graphs, discussions and history
  summary: Read complete exact target. Current bytes equal original target freeze;
    scientific reassessment is current, not a stale-input refresh.
  accessed_at: '2026-11-03T18:45:15.493119Z'
  support: supports
  snapshot_sha256: bc5b288dc20d549717192249a6d0889856bdaf66fe33b61cd213b503f4d6f610
- evidence_id: plaque-original-8
  kind: prior_review
  reference: reviews/structured/20261022T030057Z-parasitophorous-vacuole-audit/review.yaml
  locator: Exact staleness-selected original YAML and native Markdown; all evidence,
    assessments, checks, finding/action and source fields
  summary: Original observations remain immutable. Native validation/render and all15
    original frozen input hashes verified separately for this target.
  accessed_at: '2026-11-03T18:45:15.493119Z'
  support: supports
  snapshot_sha256: 29741e03b22cd0add2a9183d1fd828a20ec5a1a2404524582fde3f342b0814a1
- evidence_id: plaque-current-9
  kind: record_content
  reference: data/structures/membrane_organelle/parasitophorous_vacuole_lumen.yaml
  locator: Entire current maintained record at bdd5beb85634420b1d99c91138a9121631087f89;
    all fields, graphs, discussions and history
  summary: Read complete exact target. Current bytes equal original target freeze;
    scientific reassessment is current, not a stale-input refresh.
  accessed_at: '2026-11-03T18:45:15.493119Z'
  support: supports
  snapshot_sha256: 4a2a0820584215f4a76152f44d66e365ed67a663527da333d2e6c00d24bc244f
- evidence_id: plaque-original-9
  kind: prior_review
  reference: reviews/structured/20261022T030057Z-parasitophorous-vacuole-lumen-audit/review.yaml
  locator: Exact staleness-selected original YAML and native Markdown; all evidence,
    assessments, checks, finding/action and source fields
  summary: Original observations remain immutable. Native validation/render and all15
    original frozen input hashes verified separately for this target.
  accessed_at: '2026-11-03T18:45:15.493119Z'
  support: supports
  snapshot_sha256: 30b6e039312bb9dae5829d7823213003b3d3603da706b941a200cee35405ae2c
- evidence_id: plaque-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Fresh current Structured Source Cross-Checks and evidence rules; unchanged
    native instructions
  summary: Full positive protein/pathway claims trigger applicability; no expression
    assertion is not a sufficient exemption. Actual morphology-only targets can remain
    excluded.
  accessed_at: '2026-11-03T18:45:15.493119Z'
  support: context_only
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: plaque-rubric
  kind: authority
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Previously read exact frozen checklist bytes unchanged
  summary: Identity, source-specific science, taxon, model granularity, necessity
    and accessibility are separate assessments; no optional inventory finding.
  accessed_at: '2026-11-03T18:45:15.493119Z'
  support: context_only
  snapshot_sha256: e6b9e4b16a58c54402bed7bbee2c8b94a91d37562e8b0ee8b94ff0c829184a70
- evidence_id: plaque-graph-rubric
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Previously read frozen graph policy unchanged
  summary: Nonmechanistic designation does not excuse a material unqualified functional
    conflict. Localization and constitutive material are distinct from formation necessity.
  accessed_at: '2026-11-03T18:45:15.493119Z'
  support: context_only
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: plaque-protein-contract
  kind: authority
  reference: .claude/skills/uniprot-protein-examples/SKILL.md
  locator: Previously read frozen native example contract unchanged
  summary: Examples identify specific instances; a fragment/unreviewed example need
    not supply a full protein mechanism. COVERED means represented identifier coverage,
    not scientific completeness.
  accessed_at: '2026-11-03T18:45:15.493119Z'
  support: context_only
  snapshot_sha256: 6462894c8257823bae2b175c34693cd42f11ff9269a3829c15b9286ba6d7c876
- evidence_id: plaque-schema-policy
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Current StructuralComponent and CausalNode enums/contract bytes unchanged
  summary: LIPID label-only generic membrane material is distinct from using a whole-membrane
    GO identity as a molecular chemical grounding. Protein complexes/families are
    permitted GENE_OR_PROTEIN nodes.
  accessed_at: '2026-11-03T18:45:15.493119Z'
  support: context_only
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: plaque-context-pvm
  kind: record_content
  reference: data/structures/membrane_organelle/parasitophorous_vacuole_membrane.yaml
  locator: Whole frozen neighbor read after root expanded inspect; bounded local boundary
    identity/topology context only
  summary: Exact local PVM identifier and PV parthood resolve. Neighbor canonical-example
    evidence is not adjudicated or resolved by this assigned-target review.
  accessed_at: '2026-11-03T18:45:15.493119Z'
  support: context_only
  snapshot_sha256: fceffba04e82c2b88ce9fc1a9366c8931296169b4146291996ebe84f3dc213da
- evidence_id: plaque-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0044310,GO:0031410,GO:0020003,GO:0020004,GO:0020005
  locator: Complete exact5-term QuickGO response, all definitions/synonyms/comments/typed
    children
  summary: GO0044310 exact osmiophilic body/postulated-release definition and direct0031410
    is_a are supported. GO0020003/4/5 are broader symbiont vacuole/space/membrane
    identities with direct typed part children. Lexical exact PV synonyms do not override
    broader native biological definitions.
  accessed_at: '2026-11-03T18:41:18.788049Z'
  support: supports
  snapshot_sha256: a37dd96d97e166dab3be745574a3dd2bacbb0393353fe1f256d3cb6de8a35043
- evidence_id: plaque-SL-0193
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0193.json
  locator: Complete current UniProt location JSON; exact definition, synonyms, mappings
    and typed isA/partOf
  summary: Native locations support narrower apicomplexan PV, exact surrounding PVM
    and exact lumen; lumen/PVM partOf is distinct from broad GO parentage and molecular
    composition.
  accessed_at: '2026-11-03T18:41:18.788891Z'
  support: supports
  snapshot_sha256: cb9c8cc4e3f7cd3af9100ecc94eab5c05ba6eedd56c152d10301377e82642988
- evidence_id: plaque-SL-0194
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0194.json
  locator: Complete current UniProt location JSON; exact definition, synonyms, mappings
    and typed isA/partOf
  summary: Native locations support narrower apicomplexan PV, exact surrounding PVM
    and exact lumen; lumen/PVM partOf is distinct from broad GO parentage and molecular
    composition.
  accessed_at: '2026-11-03T18:41:19.376960Z'
  support: supports
  snapshot_sha256: 4bf6005753182d32a68bbb20ed4d7e75a92745c7f24d7ecdf19d78b23465fc28
- evidence_id: plaque-SL-0341
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0341.json
  locator: Complete current UniProt location JSON; exact definition, synonyms, mappings
    and typed isA/partOf
  summary: Native locations support narrower apicomplexan PV, exact surrounding PVM
    and exact lumen; lumen/PVM partOf is distinct from broad GO parentage and molecular
    composition.
  accessed_at: '2026-11-03T18:41:19.378116Z'
  support: supports
  snapshot_sha256: 9a3abc3189a97bf45ef3653b1ae2c96ac782aa6aa6dd896309db34c0137a3111
- evidence_id: plaque-tax5794
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5794
  locator: Complete current ENA taxon identity/rank/lineage/alternate names
  summary: Exact Apicomplexa, Toxoplasma gondii, Plasmodium falciparum or Plasmodium
    berghei identity verified; neither taxonomic identity nor orthology substitutes
    for the experimental organism/strain.
  accessed_at: '2026-11-03T18:41:18.788390Z'
  support: supports
  snapshot_sha256: 617b42c27ae95a801b69abf63e1a545eff8565fd0af2f4a81be359d3fb6b3cbf
- evidence_id: plaque-tax5811
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5811
  locator: Complete current ENA taxon identity/rank/lineage/alternate names
  summary: Exact Apicomplexa, Toxoplasma gondii, Plasmodium falciparum or Plasmodium
    berghei identity verified; neither taxonomic identity nor orthology substitutes
    for the experimental organism/strain.
  accessed_at: '2026-11-03T18:41:18.788450Z'
  support: supports
  snapshot_sha256: 11679825fa4d00b18d5848862450ab6b3770aaa47ad6676d1196d9df61124b16
- evidence_id: plaque-tax5833
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5833
  locator: Complete current ENA taxon identity/rank/lineage/alternate names
  summary: Exact Apicomplexa, Toxoplasma gondii, Plasmodium falciparum or Plasmodium
    berghei identity verified; neither taxonomic identity nor orthology substitutes
    for the experimental organism/strain.
  accessed_at: '2026-11-03T18:41:18.788508Z'
  support: supports
  snapshot_sha256: 47c9da135299ea0515b9cbddde80166e0e7256bcf1daac4cdf87f8ae3e0ecd11
- evidence_id: plaque-tax5821
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5821
  locator: Complete current ENA taxon identity/rank/lineage/alternate names
  summary: Exact Apicomplexa, Toxoplasma gondii, Plasmodium falciparum or Plasmodium
    berghei identity verified; neither taxonomic identity nor orthology substitutes
    for the experimental organism/strain.
  accessed_at: '2026-11-03T18:41:18.788553Z'
  support: supports
  snapshot_sha256: 3d37c533e4f23e90562929a45d50b533bcb0d9412ba0e7f1d27a4b7a9ed2ea12
- evidence_id: plaque-pfg377
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/A0A059WIJ2.json
  locator: Complete current A0A059WIJ2 JSON including entry status, protein description,
    gene, sequence, reference strain and crossreferences
  summary: UNREVIEWED TrEMBL Pfg377/pfg377, taxon5833,193-aa Fragment, predicted protein
    evidence, G1 sequence background. Partial gene example remains identity-only,
    not the full377-kDa experimental protein or the3D7 knockout strain. Native PANTHER
    annotations are not automatically adopted as exact source-neutral grounding.
  accessed_at: '2026-11-03T18:41:18.788214Z'
  support: supports
  snapshot_sha256: 78925197c3e458f597d9e39f5d510c1c8706c965c48e0532397a5d1f49c4dd3f
- evidence_id: plaque-pfg377-interpro
  kind: search
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/A0A059WIJ2/?page_size=200
  locator: Exact accession association request page_size200; HTTP204 zero bytes
  summary: This response supplies no inspectable family list; it does not establish
    absence of a Pfg377 family or justify guessing a grounding.
  accessed_at: '2026-11-03T18:41:18.788327Z'
  support: context_only
  search_scope: InterPro entry/interpro/protein/uniprot/A0A059WIJ2 exact accession
    request, page_size200 at 2026-11-03T18:41:18.788327Z; HTTP204,0bytes, no pagination/body
    evidence.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: plaque-pfg377-reviewed-search
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene%3Apfg377%29%20AND%20%28organism_id%3A5833%29%20AND%20%28reviewed%3Atrue%29&format=json&size=100
  locator: Exact native gene:pfg377 AND organism_id:5833 AND reviewed:true; size100
  summary: Zero returned reviewed entries within this exact query. Does not refute
    unreviewed accession identity or prove absence under other aliases/family namespaces.
  accessed_at: '2026-11-03T18:42:00.358617Z'
  support: context_only
  search_scope: UniProtKB exact gene/taxon/reviewed query in URL, size100 at 2026-11-03T18:42:00.358617Z;
    returned results[]; bounded alias-sensitive query only.
  snapshot_sha256: 5021e624e752b001ce3e3846e8f158ed4aeb93a4c9a72fdb35a0c5b14a0eea84
- evidence_id: plaque-alano1995-meta
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1016%2F0166-6851%2895%2902491-3&format=json&resultType=core&pageSize=25
  locator: Exact DOI query with punctuation; pageSize25; zero hits
  summary: No result from this DOI search surface is not a missing-paper finding.
    Exact PMID8719156 subsequently returns the valid DOI/title and complete primary
    abstract.
  accessed_at: '2026-11-03T18:41:19.385449Z'
  support: context_only
  search_scope: EuropePMC exact DOI or PMID query in URL; pageSize25, at 2026-11-03T18:41:19.385449Z;
    0 metadata results inspected; complete returned abstract only unless separately
    scoped body evidence.
  snapshot_sha256: ec754fda4c795b5f77cd13603c7b8820bfb39d199087cb1eceb7213d6d39e269
- evidence_id: plaque-alano1995-pmid
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8719156%20AND%20SRC%3AMED&format=json&resultType=core&pageSize=25
  locator: Exact native bibliographic identity and complete primary abstract inspected
  summary: Title/authors/year/DOI/PMID checked. Alano supports3D7 cDNA, full377-kDa
    gene product and immunoelectron localization;2008 reports reduced emergence and
    infection;2016 reports contrary egress result;2018 explicitly reports P.berghei
    BioID. Abstract scope is distinct from separately read bodies.
  accessed_at: '2026-11-03T18:42:00.102887Z'
  support: supports
  search_scope: EuropePMC exact DOI or PMID query in URL; pageSize25, at 2026-11-03T18:42:00.102887Z;
    1 metadata results inspected; complete returned abstract only unless separately
    scoped body evidence.
  snapshot_sha256: e7e90ce4d911c1887c2f842d7eef8b53893c4570bdf4519af150a92b36f46c68
- evidence_id: plaque-dekoning2008-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1111%2Fj.1365-2958.2007.06039.x&format=json&resultType=core&pageSize=25
  locator: Exact native bibliographic identity and complete primary abstract inspected
  summary: Title/authors/year/DOI/PMID checked. Alano supports3D7 cDNA, full377-kDa
    gene product and immunoelectron localization;2008 reports reduced emergence and
    infection;2016 reports contrary egress result;2018 explicitly reports P.berghei
    BioID. Abstract scope is distinct from separately read bodies.
  accessed_at: '2026-11-03T18:41:19.392783Z'
  support: supports
  search_scope: EuropePMC exact DOI or PMID query in URL; pageSize25, at 2026-11-03T18:41:19.392783Z;
    1 metadata results inspected; complete returned abstract only unless separately
    scoped body evidence.
  snapshot_sha256: b62011b660943205a3861915db96f175d177629531d295e905c356e6d39b4f8e
- evidence_id: plaque-suarez2016-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1074%2Fmcp.M116.060681&format=json&resultType=core&pageSize=25
  locator: Exact native bibliographic identity and complete primary abstract inspected
  summary: Title/authors/year/DOI/PMID checked. Alano supports3D7 cDNA, full377-kDa
    gene product and immunoelectron localization;2008 reports reduced emergence and
    infection;2016 reports contrary egress result;2018 explicitly reports P.berghei
    BioID. Abstract scope is distinct from separately read bodies.
  accessed_at: '2026-11-03T18:41:19.401791Z'
  support: supports
  search_scope: EuropePMC exact DOI or PMID query in URL; pageSize25, at 2026-11-03T18:41:19.401791Z;
    1 metadata results inspected; complete returned abstract only unless separately
    scoped body evidence.
  snapshot_sha256: 7e2df3a9674a9a37a1950280e29cf9d73cffb0386cf6e0ce71290b36192a4349
- evidence_id: plaque-schnider2018-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128%2FmSphere.00522-17&format=json&resultType=core&pageSize=25
  locator: Exact native bibliographic identity and complete primary abstract inspected
  summary: Title/authors/year/DOI/PMID checked. Alano supports3D7 cDNA, full377-kDa
    gene product and immunoelectron localization;2008 reports reduced emergence and
    infection;2016 reports contrary egress result;2018 explicitly reports P.berghei
    BioID. Abstract scope is distinct from separately read bodies.
  accessed_at: '2026-11-03T18:41:19.525886Z'
  support: supports
  search_scope: EuropePMC exact DOI or PMID query in URL; pageSize25, at 2026-11-03T18:41:19.525886Z;
    1 metadata results inspected; complete returned abstract only unless separately
    scoped body evidence.
  snapshot_sha256: a26c2a3487f720e0de26e0a0c892babf16aedc16985d8f5c7dc22bbb792adf75
- evidence_id: plaque-lingelbach1998-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1242%2Fjcs.111.11.1467&format=json&resultType=core&pageSize=25
  locator: Complete native bibliographic metadata and abstract; SECONDARY REVIEW
  summary: Lingelbach describes invasion-associated PVM formation around Plasmodium/Toxoplasma.
    Clough supports the Toxoplasma replicative niche/interface. These are secondary
    syntheses, not newly inspected primary mechanism experiments or full review bodies.
  accessed_at: '2026-11-03T18:41:19.403029Z'
  support: supports
  search_scope: EuropePMC exact DOI or PMID query in URL; pageSize25, at 2026-11-03T18:41:19.403029Z;
    1 metadata results inspected; complete returned abstract only unless separately
    scoped body evidence.
  snapshot_sha256: 6b9eec294c99e8412b64453bcfcf68c83854acb45595b9591fde9850efcf8514
- evidence_id: plaque-clough2017-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1016%2Fj.pt.2017.02.007&format=json&resultType=core&pageSize=25
  locator: Complete native bibliographic metadata and abstract; SECONDARY REVIEW
  summary: Lingelbach describes invasion-associated PVM formation around Plasmodium/Toxoplasma.
    Clough supports the Toxoplasma replicative niche/interface. These are secondary
    syntheses, not newly inspected primary mechanism experiments or full review bodies.
  accessed_at: '2026-11-03T18:41:19.420976Z'
  support: supports
  search_scope: EuropePMC exact DOI or PMID query in URL; pageSize25, at 2026-11-03T18:41:19.420976Z;
    1 metadata results inspected; complete returned abstract only unless separately
    scoped body evidence.
  snapshot_sha256: 521123ddd61ffc2a314a1ab7befda839d63f4557c933dcee2cc3ac66199f663d
- evidence_id: plaque-dekoning2008-repository
  kind: authority
  reference: https://eprints.gla.ac.uk/4379/
  locator: University Glasgow repository metadata and complete abstract; explicit
    full-text availability statement
  summary: Matches2008 authors/title/DOI/claim scope; full text explicitly unavailable
    from repository. Wiley PDF403 is not read as article body. The reported historical
    emergence phenotype remains genuine evidence, requiring reconciliation rather
    than erasure.
  accessed_at: '2026-11-03T18:42:00.103201Z'
  support: supports
  snapshot_sha256: 69126cc0b171ffd3e5f924fb2eb865f431faa86737023fdd257cb36c7acf56dc
- evidence_id: plaque-suarez2016-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC5054347/
  locator: Genuine PMC5054347 HTML; Methods sec5–9, Results sec19 with Figure1 caption,
    complete Discussion sec24 read. Additional parent-section output is not claimed
    as complete analysis of other Methods/Results. No figure pixels, supplements or
    raw proteomics.
  summary: New3D7 pfg377KO clones5-2/8-20 are OB-depleted with abnormal residual granules.
    WGA/XA assay at15min, at least4experiments/200gametes each, finds no egress difference;
    clone5-2 has severe Ngousso A.gambiae infection/oocyst defect. Authors explicitly
    fail to reproduce2008 egress result and leave post-egress arrest unknown. Normal-body
    biogenesis and transmission association survive; a universal no-egress-role conclusion
    across all timing/strains does not follow.
  accessed_at: '2026-11-03T18:42:00.103617Z'
  support: supports
  snapshot_sha256: 60b47c036d16f6f4b38683cd671c491da0f27dca5b89443009c25a707529e7bd
- evidence_id: plaque-schnider2018-body
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5784244.1/PMC5784244.1.xml
  locator: Genuine PMC5784244.1 JATS; title/DOI, Results s1.1/s1.2 including embedded
    captions, complete Discussion s2, Methods s3.6/s3.9. No source figure pixels,
    supplemental files, or quantitative reanalysis.
  summary: EXP1-BirA*-V5 BioID uses P.berghei ANKA mCherryHsp70 blood-stage schizonts,18h150µM
    biotin.61candidate list is not61proven PVM residents; source notes off-target
    labeling and7follow-up candidates with3novel PVM localizations. P.falciparum references
    are ortholog/prior-study comparisons, not the performed survey organism.
  accessed_at: '2026-11-03T18:42:00.109955Z'
  support: supports
  snapshot_sha256: 6620bb99b97b1902508bd0dbb91c058c45d0f41580cadeed6c318e456f1ca35e
- evidence_id: plaque-catalogue
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Same-PR fresh complete official catalogue, all20organism rows/28organism-dataset
    pairs independently read; original retrieval time retained
  summary: All represented hosts are bacteria/archaea, no Plasmodium/Toxoplasma/apicomplexan
    dataset. Osmiophilic protein/egress/transmission and whole-PV BioID/PVM-protein
    assertions require applicability followed by bounded host noncoverage. PV lumen
    is genuinely topology-only. No foreign-host downstream module proxy or negative
    biology.
  accessed_at: '2026-11-03T18:41:02.406063Z'
  support: supports
  search_scope: Official /api/datasets complete response at 2026-11-03T18:41:02.406063Z;
    all returned organism/dataset pairs inspected for exact target hosts; no downstream
    gene/module query applicable.
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: plaque-access-routes
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/adversary-plaque/additional-receipts.json
  locator: Actual additional request statuses and snapshot hashes
  summary: Alano publisher403, Wiley PDF403, Suarez S3 JATS404, Lingelbach publisher403,
    Clough DOI route200 redirect shell are not full texts. Genuine Suarez PMC HTML/Schnider
    JATS are separately scoped successful bodies. Alano DOI0hits is resolved through
    exact PMID, not an absence claim.
  accessed_at: '2026-11-03T18:45:15.493119Z'
  support: context_only
  snapshot_sha256: 89075f6ad76b5dfc96e6f2bcff05ca46b32b711d193f7f07cefae42b5599dd4f
- evidence_id: plaque-historical-runner
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical00:49Z unavailable runner receipt and retained stdout/stderr
  summary: Historical PermissionError accessing pyvenv.cfg; not rerun or represented
    as successful. Current public catalogue source fallback is independently inspected.
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: plaque-original-checks
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/adversary-plaque/original-checks.json
  locator: Actual three original native validation/render pairs and retained source/current
    hashes
  summary: All3 originals validate/render exactly;15 historical inputs each match
    retained source; all3 current target hashes unchanged.
  accessed_at: '2026-11-03T18:42:15.060799Z'
  support: supports
  snapshot_sha256: 1ba313b1c43c9d189963d979af83d9adccda169694a92d5ff0c577082799570a
- evidence_id: plaque-native-osmiophilic_body-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/osmiophilic_body.yaml
    --verify
  locator: Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/osmiophilic_body-uniprot-verify-receipt.json
    and stdoutSHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: Actual osmiophilic inventory has1UNREVIEWED Pfg377 fragment example and1COVERED
    typed node; native coverage is identifier representation, not reconciliation of
    egress evidence.
  accessed_at: '2026-11-03T18:40:46.223528Z'
  support: supports
  snapshot_sha256: fefad5a7551e7716aaea9c8662d589309fa53aab840e5ca637e3e0bf2e7ac9b9
- evidence_id: plaque-native-osmiophilic_body-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/osmiophilic_body.yaml
    --causal-graphs
  locator: Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/osmiophilic_body-uniprot-causal-receipt.json
    and stdoutSHA256 8bdeb0fe45330c8ed5561de769ee40e4812f9112e072ee6467a5a2d6ba734b2f
  summary: Actual osmiophilic inventory has1UNREVIEWED Pfg377 fragment example and1COVERED
    typed node; native coverage is identifier representation, not reconciliation of
    egress evidence.
  accessed_at: '2026-11-03T18:40:46.635001Z'
  support: supports
  snapshot_sha256: 7406fb442a441bbf31182d330f24210bd617d254f3575cd5fa0632cb8e8ca07a
- evidence_id: plaque-native-parasitophorous_vacuole-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/parasitophorous_vacuole.yaml
    --verify
  locator: Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/parasitophorous_vacuole-uniprot-verify-receipt.json
    and stdoutSHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: Actual inventory has0examples and0GENE_OR_PROTEINnodes; native pass is
    empty represented accession/node coverage, not validation of narrative BioID or
    all molecular claims.
  accessed_at: '2026-11-03T18:40:47.042747Z'
  support: supports
  snapshot_sha256: 6aff7da74d8eeac6009bf322121f644aa34854d7367a1540e0e31d6ad902e869
- evidence_id: plaque-native-parasitophorous_vacuole-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/parasitophorous_vacuole.yaml
    --causal-graphs
  locator: Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/parasitophorous_vacuole-uniprot-causal-receipt.json
    and stdoutSHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: Actual inventory has0examples and0GENE_OR_PROTEINnodes; native pass is
    empty represented accession/node coverage, not validation of narrative BioID or
    all molecular claims.
  accessed_at: '2026-11-03T18:40:47.473896Z'
  support: supports
  snapshot_sha256: 1927b64ddeb8538ca32cc9a633bc8314ee21bd9392a3307d6169cbf0235ad606
- evidence_id: plaque-native-parasitophorous_vacuole_lumen-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/parasitophorous_vacuole_lumen.yaml
    --verify
  locator: Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/parasitophorous_vacuole_lumen-uniprot-verify-receipt.json
    and stdoutSHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: Actual inventory has0examples and0GENE_OR_PROTEINnodes; native pass is
    empty represented accession/node coverage, not validation of narrative BioID or
    all molecular claims.
  accessed_at: '2026-11-03T18:40:47.906652Z'
  support: supports
  snapshot_sha256: ee05d760343b60995185bf514d3c7454f866c72d3725536bb6a7557513bbe6f4
- evidence_id: plaque-native-parasitophorous_vacuole_lumen-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/parasitophorous_vacuole_lumen.yaml
    --causal-graphs
  locator: Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/parasitophorous_vacuole_lumen-uniprot-causal-receipt.json
    and stdoutSHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: Actual inventory has0examples and0GENE_OR_PROTEINnodes; native pass is
    empty represented accession/node coverage, not validation of narrative BioID or
    all molecular claims.
  accessed_at: '2026-11-03T18:40:48.340570Z'
  support: supports
  snapshot_sha256: f48c292ad9f7bffe15cd4a30ded94e01c91238c38c848b7084a5fc6d1d98b973
- evidence_id: micro-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Native skill/profile/config/checklist and structured-source cross-check
    contract
  accessed_at: '2026-11-03T18:45:32.673092Z'
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
  summary: Actual protein/pathway assertions trigger host applicability assessment;
    material/topology-only records with molecular mechanisms withheld are genuine
    exclusions. Optional slots and historical clean bundles do not justify invented
    findings.
  support: context_only
- evidence_id: micro-component-policy
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent391-460, ComponentTypeEnum, EssentialityEnum and native
    CURATION components guidance
  accessed_at: '2026-11-03T18:45:32.673092Z'
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
  summary: Label-only collective bilayer or residual peptidoglycan material is distinct
    from using a whole anatomical GO membrane as chemical grounding. Exact molecular
    identities must not be guessed. Essentiality concerns structure formation, not
    cell viability.
  support: context_only
- evidence_id: micro-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Whole graph scope, source-specific evidence and node/component-reference
    contract; add-cell-structure guidance
  accessed_at: '2026-11-03T18:45:32.673092Z'
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
  summary: NONMECHANISTIC topology is not an experimentally established assembly or
    transport pathway. Every asserted edge is assessed at its actual source scope.
    No unsupported complete protein inventory is inferred from native empty passes.
  support: context_only
- evidence_id: micro-record-organellar_chromatophore_inner_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/organellar_chromatophore_inner_membrane.yaml
  locator: Entire record including history, definitions, taxonomy, all components/evidence,
    every graph node/edge and discussions
  accessed_at: '2026-11-03T18:45:32.673092Z'
  snapshot_sha256: e3c244a36b1484e5d3ca95aa114de0a719660aa4d76ae1811ed12584b3d72b1e
  summary: Complete current target independently reviewed; exact original frozen target
    hash unchanged. No scientific record mutation.
  support: supports
- evidence_id: micro-prior-organellar_chromatophore_inner_membrane
  kind: prior_review
  reference: reviews/structured/20261022T030049Z-organellar-chromatophore-inner-membrane-audit/review.yaml
  locator: Original native identity/provenance/checks/evidence/assessments/limitations;
    original Markdown checked by actual deterministic renderer
  accessed_at: '2026-11-03T18:45:32.673092Z'
  snapshot_sha256: a3d2e2d1e5513e7c7f67424c3c8bffe16540dc97cdf9d1cf02c3c4b8113c1ef6
  summary: Original pass_with_limitations, no findings or request-curation actions.
    Explicit expression-only applicability row is present; complete current physical
    scope independently supports genuine exclusion. Historical accesses and commands
    are not current executions.
  support: context_only
- evidence_id: micro-native-organellar_chromatophore_inner_membrane-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_inner_membrane-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/organellar_chromatophore_inner_membrane.yaml
    --verify; full log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_inner_membrane-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T18:40:39.591748Z'
  snapshot_sha256: 21c2f5898f98918c5a6b459fccb78a92cb15223fab409595ae12b48df1344bd8
  summary: Exit0 at source head. Independently read record has zero protein_examples
    and zero GENE_OR_PROTEIN nodes; causal report explicitly counts zero. Generic
    verification success text is not proof of a populated molecular inventory, family
    grounding or biochemical completeness.
  support: supports
- evidence_id: micro-native-organellar_chromatophore_inner_membrane-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_inner_membrane-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/organellar_chromatophore_inner_membrane.yaml
    --causal-graphs; full log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_inner_membrane-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-03T18:40:39.997530Z'
  snapshot_sha256: 5f32e7d6f8eb25bcab7e47138d21df4619a8b87438afdee26e22ef3d5b55e8dd
  summary: Exit0 at source head. Independently read record has zero protein_examples
    and zero GENE_OR_PROTEIN nodes; causal report explicitly counts zero. Generic
    verification success text is not proof of a populated molecular inventory, family
    grounding or biochemical completeness.
  support: supports
- evidence_id: micro-record-organellar_chromatophore_intermembrane_space
  kind: record_content
  reference: data/structures/membrane_organelle/organellar_chromatophore_intermembrane_space.yaml
  locator: Entire record including history, definitions, taxonomy, all components/evidence,
    every graph node/edge and discussions
  accessed_at: '2026-11-03T18:45:32.673092Z'
  snapshot_sha256: f67ae10cda248a93eba761943f430c0ea5e6d4550dcf9514611822866d2c98ed
  summary: Complete current target independently reviewed; exact original frozen target
    hash unchanged. No scientific record mutation.
  support: supports
- evidence_id: micro-prior-organellar_chromatophore_intermembrane_space
  kind: prior_review
  reference: reviews/structured/20261022T030050Z-organellar-chromatophore-intermembrane-space-audit/review.yaml
  locator: Original native identity/provenance/checks/evidence/assessments/limitations;
    original Markdown checked by actual deterministic renderer
  accessed_at: '2026-11-03T18:45:32.673092Z'
  snapshot_sha256: a70e222696f0636c07d2f95bb8125369a4455821a3db1333d69b9e4d7d4603df
  summary: Original pass_with_limitations, no findings or request-curation actions.
    Explicit expression-only applicability row is present; complete current physical
    scope independently supports genuine exclusion. Historical accesses and commands
    are not current executions.
  support: context_only
- evidence_id: micro-native-organellar_chromatophore_intermembrane_space-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_intermembrane_space-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/organellar_chromatophore_intermembrane_space.yaml
    --verify; full log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_intermembrane_space-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T18:40:40.418107Z'
  snapshot_sha256: ba310abb3d467c4b1cf455122cce45793ec4fd677a723d5c873d1644a9a0a0c7
  summary: Exit0 at source head. Independently read record has zero protein_examples
    and zero GENE_OR_PROTEIN nodes; causal report explicitly counts zero. Generic
    verification success text is not proof of a populated molecular inventory, family
    grounding or biochemical completeness.
  support: supports
- evidence_id: micro-native-organellar_chromatophore_intermembrane_space-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_intermembrane_space-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/organellar_chromatophore_intermembrane_space.yaml
    --causal-graphs; full log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_intermembrane_space-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-03T18:40:40.837079Z'
  snapshot_sha256: 81f66424b1e0df0b356c6a275880b0e72d6a047a87e4402f25e75cccc98b59de
  summary: Exit0 at source head. Independently read record has zero protein_examples
    and zero GENE_OR_PROTEIN nodes; causal report explicitly counts zero. Generic
    verification success text is not proof of a populated molecular inventory, family
    grounding or biochemical completeness.
  support: supports
- evidence_id: micro-record-organellar_chromatophore_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/organellar_chromatophore_membrane.yaml
  locator: Entire record including history, definitions, taxonomy, all components/evidence,
    every graph node/edge and discussions
  accessed_at: '2026-11-03T18:45:32.673092Z'
  snapshot_sha256: 179b7a8a2519cb216889baed1305e54b1de332688cbb7bac1c24857f1209a794
  summary: Complete current target independently reviewed; exact original frozen target
    hash unchanged. No scientific record mutation.
  support: supports
- evidence_id: micro-prior-organellar_chromatophore_membrane
  kind: prior_review
  reference: reviews/structured/20261022T030051Z-organellar-chromatophore-membrane-audit/review.yaml
  locator: Original native identity/provenance/checks/evidence/assessments/limitations;
    original Markdown checked by actual deterministic renderer
  accessed_at: '2026-11-03T18:45:32.673092Z'
  snapshot_sha256: f2253bcdd27a440466a7435616878f98e75481daf0e96d3504086f9464d4542e
  summary: Original pass_with_limitations, no findings or request-curation actions.
    Explicit expression-only applicability row is present; complete current physical
    scope independently supports genuine exclusion. Historical accesses and commands
    are not current executions.
  support: context_only
- evidence_id: micro-native-organellar_chromatophore_membrane-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_membrane-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/organellar_chromatophore_membrane.yaml
    --verify; full log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_membrane-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T18:40:41.260873Z'
  snapshot_sha256: 4a0c7b8670ac126eafab1eaa74af64156dda65b7a34f65bfe220f5fa255c0164
  summary: Exit0 at source head. Independently read record has zero protein_examples
    and zero GENE_OR_PROTEIN nodes; causal report explicitly counts zero. Generic
    verification success text is not proof of a populated molecular inventory, family
    grounding or biochemical completeness.
  support: supports
- evidence_id: micro-native-organellar_chromatophore_membrane-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_membrane-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/organellar_chromatophore_membrane.yaml
    --causal-graphs; full log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_membrane-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-03T18:40:41.713527Z'
  snapshot_sha256: be16dfe8edb5cc208f39e199a2bc36d21d9fe4822359355075535e54dd5b00c2
  summary: Exit0 at source head. Independently read record has zero protein_examples
    and zero GENE_OR_PROTEIN nodes; causal report explicitly counts zero. Generic
    verification success text is not proof of a populated molecular inventory, family
    grounding or biochemical completeness.
  support: supports
- evidence_id: micro-record-organellar_chromatophore_outer_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/organellar_chromatophore_outer_membrane.yaml
  locator: Entire record including history, definitions, taxonomy, all components/evidence,
    every graph node/edge and discussions
  accessed_at: '2026-11-03T18:45:32.673092Z'
  snapshot_sha256: f7d415a8e211d48ef9ecf5f0bb1b96a0ac3336c1ce6498d78d9bf0033bce3c11
  summary: Complete current target independently reviewed; exact original frozen target
    hash unchanged. No scientific record mutation.
  support: supports
- evidence_id: micro-prior-organellar_chromatophore_outer_membrane
  kind: prior_review
  reference: reviews/structured/20261022T030052Z-organellar-chromatophore-outer-membrane-audit/review.yaml
  locator: Original native identity/provenance/checks/evidence/assessments/limitations;
    original Markdown checked by actual deterministic renderer
  accessed_at: '2026-11-03T18:45:32.673092Z'
  snapshot_sha256: bd2d739dd21cc8a719072fb015e3489d95c1d4162321116aaeb74be8f1114903
  summary: Original pass_with_limitations, no findings or request-curation actions.
    Explicit expression-only applicability row is present; complete current physical
    scope independently supports genuine exclusion. Historical accesses and commands
    are not current executions.
  support: context_only
- evidence_id: micro-native-organellar_chromatophore_outer_membrane-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_outer_membrane-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/organellar_chromatophore_outer_membrane.yaml
    --verify; full log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_outer_membrane-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T18:40:42.127098Z'
  snapshot_sha256: e7509ff33dceef6095a7129fc6535740d9cdb93b549e53f35c9f90d160d33000
  summary: Exit0 at source head. Independently read record has zero protein_examples
    and zero GENE_OR_PROTEIN nodes; causal report explicitly counts zero. Generic
    verification success text is not proof of a populated molecular inventory, family
    grounding or biochemical completeness.
  support: supports
- evidence_id: micro-native-organellar_chromatophore_outer_membrane-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_outer_membrane-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/organellar_chromatophore_outer_membrane.yaml
    --causal-graphs; full log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/organellar_chromatophore_outer_membrane-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-03T18:40:42.539170Z'
  snapshot_sha256: a2b645dba71fa0b3607ee3d792f40a1530619d8ecb552beeed9e09825659b657
  summary: Exit0 at source head. Independently read record has zero protein_examples
    and zero GENE_OR_PROTEIN nodes; causal report explicitly counts zero. Generic
    verification success text is not proof of a populated molecular inventory, family
    grounding or biochemical completeness.
  support: supports
- evidence_id: micro-original-pairs
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/adversary-microtubule/original-checks.json
  locator: Four actual native validate calls and four render --content calls with
    exact Markdown comparison
  accessed_at: '2026-11-03T18:42:31.733998Z'
  snapshot_sha256: 075dea20bee5c4ae3e264d73ccfc0f2977d5774e5d11564e5e70f5fa806d0c9e
  summary: All four original YAML documents validate and all four committed Markdown
    artifacts exactly match their deterministic render.
  support: supports
- evidence_id: micro-original-inputs
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/adversary-microtubule/original-frozen-inputs.json
  locator: All68 historical frozen input entries at original retained source revision
  accessed_at: '2026-11-03T18:45:32.673092Z'
  snapshot_sha256: 18c416238ac989394893aaad6a215c3f86830db3a0be011857f9559f55d82f90
  summary: All original source hashes verify; current four target hashes unchanged.
    Historical context hashing is provenance validation, not a new scientific judgment
    of unfrozen neighboring records.
  support: supports
- evidence_id: micro-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0070111,GO:0070112,GO:0070113,GO:0070114,GO:0070115,GO:0070116,GO:0070117,GO:0070118,GO:0009527,GO:0009528,GO:0009529,GO:0030659
  locator: 'Complete12 requested active terms: id/name/definition/synonyms/isObsolete
    and typed children; exact queried list in URL'
  accessed_at: '2026-11-03T18:41:01.617440Z'
  snapshot_sha256: f9aac8bb38630a7042be2f1e74d9d7bae2b148d0a96f695e31b862b99e5ba5aa
  summary: GO0070112/13/14/15 identify generic membrane, inner membrane, outer membrane
    and intermembrane space. GO0070112 directly has0070113/14/18 is_a children; GO0030659
    directly has0070112 is_a child. GO0070111 directly has0070112/14/15 part_of children;
    no direct inner relation fabricated. Parent plastid anatomy terms are active;
    differing hierarchy claims are attributed to UniProt, not invented GO edges.
  support: supports
- evidence_id: micro-go-0070112-isa
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0070112/ancestors?relations=is_a
  locator: Complete exact-term ancestors request with relations=is_a; transitive ancestry
    not immediate-parent or parthood proof
  accessed_at: '2026-11-03T18:41:01.617714Z'
  snapshot_sha256: c098937855de2e7e3c9085ac74f1ddaa945727690154a344dd0a24c58c8c3eac
  summary: Native is_a ancestors for GO:0070112 are GO:0030659, GO:0070112, GO:0012506,
    GO:0016020, GO:0110165, GO:0005575, GO:0031090. Broader plastid parents absent
    from this exact response are not asserted as GO edges; native UniProt immediate
    relationships are separately inspected.
  support: supports
- evidence_id: micro-go-0070113-isa
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0070113/ancestors?relations=is_a
  locator: Complete exact-term ancestors request with relations=is_a; transitive ancestry
    not immediate-parent or parthood proof
  accessed_at: '2026-11-03T18:41:01.617793Z'
  snapshot_sha256: 9b5f898b36e6d0a3cc26e0405c9f3c9667b74025840d6853a4c136021a5f2776
  summary: Native is_a ancestors for GO:0070113 are GO:0030659, GO:0070112, GO:0012506,
    GO:0016020, GO:0070113, GO:0110165, GO:0005575, GO:0031090. Broader plastid parents
    absent from this exact response are not asserted as GO edges; native UniProt immediate
    relationships are separately inspected.
  support: supports
- evidence_id: micro-go-0070114-isa
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0070114/ancestors?relations=is_a
  locator: Complete exact-term ancestors request with relations=is_a; transitive ancestry
    not immediate-parent or parthood proof
  accessed_at: '2026-11-03T18:41:01.617843Z'
  snapshot_sha256: 7908fedd7723d9c1577c8ade5098fea7b3f03346e17e40b89d66593d68eaa793
  summary: Native is_a ancestors for GO:0070114 are GO:0030659, GO:0070112, GO:0098588,
    GO:0012506, GO:0016020, GO:0043661, GO:0070114, GO:0110165, GO:0005575, GO:0031090,
    GO:0030666. Broader plastid parents absent from this exact response are not asserted
    as GO edges; native UniProt immediate relationships are separately inspected.
  support: supports
- evidence_id: micro-go-0070115-isa
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0070115/ancestors?relations=is_a
  locator: Complete exact-term ancestors request with relations=is_a; transitive ancestry
    not immediate-parent or parthood proof
  accessed_at: '2026-11-03T18:41:01.617888Z'
  snapshot_sha256: fee3da7c17097dc4ab78e4ecfbba8aa8a0685e2f892cc348aba55beed4bd3841
  summary: Native is_a ancestors for GO:0070115 are GO:0070115, GO:0110165, GO:0005575.
    Broader plastid parents absent from this exact response are not asserted as GO
    edges; native UniProt immediate relationships are separately inspected.
  support: supports
- evidence_id: micro-SL0351
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0351.json
  locator: Top-level native id/name/definition/category/GO mappings, immediate isA/partOf
    entries and corresponding parent GO cross-references; statistics not evidence
    of biological absence
  accessed_at: '2026-11-03T18:41:01.617929Z'
  snapshot_sha256: 8a511ebab3aeb225c94971707064b4de8201b1bc8f6672c0e32f550ee72ae5c2
  summary: Exact GO0070111 mapping and definition explicitly state two surrounding
    membranes, residual peptidoglycan between them and internal thylakoids. This authority
    supports anatomical context; its broader biosynthetic discussion is not imported
    as a pathway assertion into the four physical records.
  support: supports
- evidence_id: micro-SL0352
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0352.json
  locator: Top-level native id/name/definition/category/GO mappings, immediate isA/partOf
    entries and corresponding parent GO cross-references; statistics not evidence
    of biological absence
  accessed_at: '2026-11-03T18:41:02.370361Z'
  snapshot_sha256: 3bbd1251c9b67c87fdd3a88c0fb7e326a36c0c823f30fe6a9825472786bfc8dc
  summary: Exact GO0070112 mapping, definition explicitly covers unspecified outer/inner/thylakoid
    localization, immediate isA plastid membrane and partOf organellar chromatophore.
    Its generic fallback scope is distinct from identifying any particular membrane
    or protein.
  support: supports
- evidence_id: micro-SL0359
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0359.json
  locator: Top-level native id/name/definition/category/GO mappings, immediate isA/partOf
    entries and corresponding parent GO cross-references; statistics not evidence
    of biological absence
  accessed_at: '2026-11-03T18:41:02.377320Z'
  snapshot_sha256: a725d4ba4dd92252b47d539cdfe536c3d87161af6c86a1c8f3c6df79449d88f2
  summary: Exact GO0070113 mapping and definition of stroma/intermembrane-space separation;
    immediate isA plastid inner membraneGO0009528 and chromatophore membraneGO0070112,
    partOf chromatophoreGO0070111. Paulinella-specific description is not a prevalence
    census.
  support: supports
- evidence_id: micro-SL0360
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0360.json
  locator: Top-level native id/name/definition/category/GO mappings, immediate isA/partOf
    entries and corresponding parent GO cross-references; statistics not evidence
    of biological absence
  accessed_at: '2026-11-03T18:41:02.385958Z'
  snapshot_sha256: 923752b7db9bd69e696b92d034c0ca9e793e171e320c7cb7de62b9119587f026
  summary: Exact GO0070115 mapping and region between inner/outer membranes; immediate
    isA plastid intermembrane spaceGO0009529 and partOf chromatophoreGO0070111. It
    denotes neither stroma nor thylakoid lumen.
  support: supports
- evidence_id: micro-SL0361
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0361.json
  locator: Top-level native id/name/definition/category/GO mappings, immediate isA/partOf
    entries and corresponding parent GO cross-references; statistics not evidence
    of biological absence
  accessed_at: '2026-11-03T18:41:02.402767Z'
  snapshot_sha256: 77901571712764f863b88e816b81fa7bbec57c9e05e4d1b6eb0336945c3d359e
  summary: Exact GO0070114 mapping and cytoplasm-facing membrane definition; immediate
    isA plastid outer membraneGO0009527 and chromatophore membraneGO0070112, partOf
    chromatophoreGO0070111.
  support: supports
- evidence_id: micro-SL0353
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0353.json
  locator: Top-level native id/name/definition/category/GO mappings, immediate isA/partOf
    entries and corresponding parent GO cross-references; statistics not evidence
    of biological absence
  accessed_at: '2026-11-03T18:43:21.336446Z'
  snapshot_sha256: 63dd5e9dcf2a9794f4f96241e3d5147d8e92129cfa769e9a79bd327551b69be5
  summary: Current exact location identifies chromatophore stroma excluding thylakoid
    space; immediate isA plastid stroma, partOf chromatophore, no top-level GO mapping.
    Optional enrichment does not refute the dated historical unresolved-accession
    removal or require rewriting append-only history.
  support: supports
- evidence_id: micro-tax39716
  kind: database
  reference: https://rest.uniprot.org/taxonomy/39716.json
  locator: Complete scientificName/taxonId/rank/active and parent/lineage fields
  accessed_at: '2026-11-03T18:41:02.403738Z'
  snapshot_sha256: 2e74a7cc0c3a0476f9b5b94549623cc90db407aa0cacdc8014996ee13cfa258e
  summary: Current authority identifies Paulinella39716 at genus rank within Eukaryota/Rhizaria/Cercozoa.
    This verifies identity, not universal occurrence or quantitative prevalence.
  support: supports
- evidence_id: micro-catalogue
  kind: search
  reference: https://imodulondb.org/api/datasets
  locator: Complete official /api/datasets response; all20 organism rows and28 organism/dataset
    pairs inspected
  accessed_at: '2026-11-03T18:41:02.406063Z'
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  summary: No Paulinella, chromatophora, micropora, longichromatophora or matching
    eukaryotic-host entry is present. The four targets already have genuine physical
    exclusions; this supplemental catalogue check does not invent pathway claims or
    justify a bacterial proxy. Noncoverage is not biological negative evidence.
  support: supports
  search_scope: Official iModulonDB /api/datasets at 2026-11-03T18:41:02.406063Z;
    unpaginated HTTP200 full20 organism rows/28 organism-dataset pairs; inspect id/name/description/datasets
    for Paulinella and named photosynthetic-host taxa. Coverage confined to this returned
    catalogue and date; no global dataset-absence claim, unmatched gene query or module
    summary.
- evidence_id: micro-historical-runner
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical command /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb datasets; actual00:49Z exit1/PermissionError reading pyvenv.cfg
  accessed_at: '2026-11-03T00:49:00.863225Z'
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  summary: Historical optional runner unavailable receipt retained as historical context,
    not rerun or current success. Current official catalogue fallback was freshly
    read; no necessary matched-host downstream query exists for these physical targets.
  support: context_only
- evidence_id: micro-gabr2020-meta
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1111%2Fjpy.13003%22&format=json&resultType=core&pageSize=25
  locator: Retained actual PR2372 retrieval; independently reread exact DOI core result
    identity/authors/publication type and complete abstract; pageSize25 unique MED
    result
  accessed_at: '2026-11-03T18:03:02.726782Z'
  snapshot_sha256: c87f440e2e07ee1d17591fe114f793f02bdbaec963b6148d60775f9ecfa34a13
  summary: Paulinella, a model for understanding plastid primary endosymbiosis. DOI10.1111/jpy.13003
    PMID32289879. Secondary review, context only; abstract does not replace full-body
    scope.
  support: context_only
- evidence_id: micro-nowack2012-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1073%2Fpnas.1118800109%22&format=json&resultType=core&pageSize=25
  locator: Retained actual PR2372 retrieval; independently reread exact DOI core result
    identity/authors/publication type and complete abstract; pageSize25 unique MED
    result
  accessed_at: '2026-11-03T18:03:02.474695Z'
  snapshot_sha256: 951c112a9828dbd2f97cd034e856f0cfaf5593109d5f793c785a532001a486d5
  summary: Trafficking of protein into the recently established photosynthetic organelles
    of Paulinella chromatophora. DOI10.1073/pnas.1118800109 PMID22371600. Primary
    import study; metadata/abstract distinct from bounded body reread.
  support: context_only
- evidence_id: micro-nowack2012-body
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3325729/
  locator: 'Retained genuine canonicalPMC HTML fetched18:08:44Z in PR2372, independently
    reread now: Resultssec2/3 with Fig1/2 captions and Methodssec14 Strain and Growth
    Conditions; no pixels or supplementary data'
  accessed_at: '2026-11-03T18:08:44.263032Z'
  snapshot_sha256: 3c62e25e8dde341faf854bc462eb3e03a4cf927ce0761d0888bde710bcf07bfb
  summary: Primary P.chromatophora CCAC0185, a subisolate of M0880/a, shows chromatophores/thylakoids
    and localized PsaE plus PSI association in stated experiments. This corroborates
    organism/organelle context, not specific envelope lipid composition, residual-wall
    chemistry or individual formation necessity. No boundary protein imported from
    thylakoid localization.
  support: context_only
- evidence_id: micro-gabr2020-canonical
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC7734844/
  locator: Genuine canonicalPMC secondary-review body, complete S2 The Paulinella
    Model and embedded Figure1 caption only; no figure pixels
  accessed_at: '2026-11-03T18:43:21.336696Z'
  snapshot_sha256: f79b1ff8863a8b2e46d4397f850465ee435f2dbd860885242377d9e889a49352
  summary: Secondary context distinguishes photosynthetic Paulinella lineages from
    heterotrophic relatives lacking chromatophores. Supports qualitative VARIABLE
    within the genus, not a numerical prevalence census or current exhaustive species
    list. Fresh body retrieval distinguished from reused earlier metadata.
  support: context_only
- evidence_id: check-qc
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/qc.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T18:45:47.429837Z'
  support: supports
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  snapshot_sha256: 9623a63ed87068a48c1debbff2ff3179d63c89c6fd2e339795a2da2b92444d5d
- evidence_id: check-labels
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/labels.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T18:41:08.322780Z'
  support: supports
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  snapshot_sha256: 6cdfb05df9a27194f05a5fd7f851783f817ac1523ca0bbfa54fe0e0d18775905
- evidence_id: check-trait-links
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/trait-links.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T18:40:42.139208Z'
  support: supports
  summary: Native TraitMech link check passed.
  snapshot_sha256: 8b336cdefbbd3daf6da8787990efdbe346c95e2c8361d50b7eb68a18f2d5a44a
- evidence_id: check-vendored
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/vendored.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T18:40:42.736286Z'
  support: supports
  summary: Pinned governed files match; native vendored check passed.
  snapshot_sha256: b1f169d103aaefa930745468bcca171e5867b9cc49e4e74311e458097e3252a6
- evidence_id: check-curies
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/curies.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T18:40:47.017989Z'
  support: supports
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  snapshot_sha256: bc12b1285f5747707643f7a98e03dbb3a6c88fb062ad49f99db9cb42ececf3d2
- evidence_id: focused
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/focused-results.json
  locator: All twenty actual target schema/strict command outputs
  accessed_at: '2026-11-03T18:47:31Z'
  support: supports
  summary: Ten schema and ten strict commands returned exit zero.
  snapshot_sha256: 16fac573f8f68bfd63ba078f5de842be198938cf5dd2f842ccc20386767ade40
- evidence_id: supplemental-pmid
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2373/pmid-chunks-receipt.json
  locator: Complete native-report PMID set checked with unchanged resolver in batches
    of at most fifty
  accessed_at: '2026-11-03T18:41:45.313804Z'
  support: supports
  summary: 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers
    remain unverified.
  snapshot_sha256: 4d385ac0065c45feaa8cd97f0af0ca449fb01390552a5a6deac4424e3abbee1c
- evidence_id: historical-adapter-runner-availability
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical runner invocation receipt, exact SHA256 reverified during PR2373
    synthesis
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  summary: Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS
    PermissionError reading the configured runner pyvenv.cfg. This is a retained historical
    availability observation, not a fresh attempt or a scientific validation failure.
    Native policy permits inspected source-catalogue fallback.
assessments:
- assessment_id: septin-organellar_chromatophore_thylakoid-schema
  area: schema
  topic: Original native schema/render and unchanged input
  outcome: supported
  summary: Original validate/render exit0 and Markdown exact; current record matches
    the review frozen hash. No assigned target is stale. Schema validity is distinct
    from the scientific judgment.
  target_ids:
  - GO:0070116
  evidence_ids:
  - septin-record-organellar_chromatophore_thylakoid
  - septin-original-validation-organellar_chromatophore_thylakoid
- assessment_id: septin-organellar_chromatophore_thylakoid-identity
  area: identity
  topic: Exact identity, synonyms and anatomy
  outcome: supported
  summary: Exact GO0070116 definition matches; thylakoid GO0009579 is an is_a ancestor,
    whole chromatophore GO0070111 is part_of, lumen/membrane are constituent parts,
    and SL0354 is the exact location xref.
  target_ids:
  - GO:0070116
  evidence_ids:
  - septin-record-organellar_chromatophore_thylakoid
  - septin-go
  - septin-SL0354
  - septin-GO0070116-isa
  - septin-context-organellar_chromatophore
- assessment_id: septin-organellar_chromatophore_thylakoid-classification-limits
  area: scope
  topic: Ontology versus native classification scope
  outcome: supported
  summary: Source hierarchy and textual definitions need separate attribution. GO
    generic thylakoid comment says it is not considered an organelle, whereas the
    repository native category explicitly includes thylakoids. The physical membrane-bounded
    lumen and native model support the retained structure_kind without an enum-only
    finding. GO0070112 definition emphasizes enclosing bilayers while its hierarchy
    also includes internal thylakoid membranes; current explicit hierarchy/SL support
    is retained without silently rewriting the source.
  target_ids:
  - GO:0070116
  evidence_ids:
  - septin-record-organellar_chromatophore_thylakoid
  - septin-go
  - septin-GO0070116-isa
  - septin-GO0070118-isa
  - septin-schema-policy
  - septin-SL0354
- assessment_id: septin-organellar_chromatophore_thylakoid-taxa
  area: scope
  topic: Taxon identity and qualitative presence
  outcome: supported
  summary: P. chromatophora39717 species and canonical model identity agree with authority.
    Nowack2014 is secondary deposited-abstract context; Nowack2012 directly studies
    thylakoids/PSI in CCAC0185 M0880/a. COMMON is read qualitatively, not as a measured
    prevalence percentage or every-strain guarantee.
  target_ids:
  - GO:0070116
  evidence_ids:
  - septin-record-organellar_chromatophore_thylakoid
  - septin-tax39716
  - septin-tax39717
  - septin-SL0354
  - septin-nowack2014-crossref
  - septin-nowack2012-prefixed
- assessment_id: septin-organellar_chromatophore_thylakoid-materials
  area: grounding
  topic: Whole structure and collective lipid material
  outcome: concern
  summary: A LIPID component is exactly grounded to whole membrane GO0070118 and linked
    from a STRUCTURE graph node. This is inherited F1, a confirmed whole-structure
    versus molecular-material identity mismatch. UNKNOWN essentiality does not cure
    the typing/grounding error.
  target_ids:
  - GO:0070116
  evidence_ids:
  - septin-record-organellar_chromatophore_thylakoid
  - septin-go
  - septin-SL0354
  - septin-curation-policy
  - septin-schema-policy
- assessment_id: septin-organellar_chromatophore_thylakoid-light-complexes
  area: evidence
  topic: Positive photosynthetic light-complex evidence
  outcome: supported
  summary: SL0354/SL0356 explicitly describe light-reaction complexes. Re-read Nowack2012
    primary Results support PsaE thylakoid association and selected imported PSI subunits
    associating with purified PSI in one cultured P. chromatophora subisolate. These
    observations support the modest light-reaction-site claim without enumerating
    the complete photosystem/electron-transport chain.
  target_ids:
  - GO:0070116
  evidence_ids:
  - septin-record-organellar_chromatophore_thylakoid
  - septin-SL0354
  - septin-SL0356
  - septin-nowack2012-prefixed
  - septin-go
- assessment_id: septin-organellar_chromatophore_thylakoid-source-attribution
  area: evidence
  topic: Exact source placement
  outcome: concern
  summary: 'Inherited F2 persists at the component evidence and supports-edge evidence:
    GO0070118 defines a bilayer but does not state that it carries light-reaction
    complexes. Keep the true biology and cite SL0354/SL0356 or the scoped primary
    PSI result for that clause.'
  target_ids:
  - GO:0070116
  evidence_ids:
  - septin-record-organellar_chromatophore_thylakoid
  - septin-go
  - septin-SL0354
  - septin-SL0356
  - septin-nowack2012-prefixed
- assessment_id: septin-organellar_chromatophore_thylakoid-necessity
  area: evidence
  topic: Formation and complete composition remain unknown
  outcome: unknown
  summary: Neither exact location authority nor the bounded primary localization/purification
    experiment establishes every lipid/protein identity, stoichiometry, cross-strain
    conservation or individual necessity for thylakoid formation. No missing optional
    protein examples or automatic protein-complex type defect is inferred.
  target_ids:
  - GO:0070116
  evidence_ids:
  - septin-record-organellar_chromatophore_thylakoid
  - septin-nowack2012-prefixed
  - septin-protein-policy
  - septin-schema-policy
- assessment_id: septin-organellar_chromatophore_thylakoid-graph
  area: graph
  topic: Complete descriptive graph and declared limits
  outcome: concern
  summary: 'Three NONMECHANISTIC edges: membrane bounds lumen, supports light reactions
    and is part of thylakoid. Topology and modest functional relation are supported;
    F1 component correspondence and F2 source note remain the two explicit corrections.'
  target_ids:
  - GO:0070116
  evidence_ids:
  - septin-record-organellar_chromatophore_thylakoid
  - septin-graph-policy
  - septin-go
  - septin-SL0354
  - septin-SL0355
  - septin-SL0356
- assessment_id: septin-organellar_chromatophore_thylakoid-native
  area: provenance
  topic: Actual native protein verification coverage
  outcome: supported
  summary: Both actual commands exit0 and independent full-record inventory confirms
    zero examples, zero typed molecular nodes and zero UniProtKB graph xrefs. Generic
    verify text alone is not treated as inventory evidence; empty native coverage
    is not biological completeness.
  target_ids:
  - GO:0070116
  evidence_ids:
  - septin-record-organellar_chromatophore_thylakoid
  - septin-native-organellar_chromatophore_thylakoid-verify
  - septin-native-organellar_chromatophore_thylakoid-causal
- assessment_id: septin-organellar_chromatophore_thylakoid-adapter
  area: scope
  topic: Corrected positive pathway applicability assessment
  outcome: supported
  summary: Record positively asserts photosynthetic light-reaction complexes in component/function/graph
    narrative despite no individual protein inventory. Original absence-of-expression
    rationale is insufficient. Fresh full official catalogue contains no matched Paulinella
    host/strain, so source-specific SL/primary checks are the bounded fallback; no
    free-living cyanobacterial proxy or gene/module query is substituted. This completes
    applicability assessment, not a new native runner execution.
  target_ids:
  - GO:0070116
  evidence_ids:
  - septin-record-organellar_chromatophore_thylakoid
  - septin-original-organellar_chromatophore_thylakoid
  - septin-review-policy
  - septin-catalogue
  - septin-adapter-runner-historical
  - septin-nowack2012-prefixed
  - septin-SL0354
- assessment_id: septin-organellar_chromatophore_thylakoid-omitted-domains
  area: scope
  topic: No unrepresented image, measurement or protein assertion
  outcome: not_applicable
  summary: No maintained image or licence claim, numeric measurement, associated trait,
    verbatim snippet, individual gene/protein identity or representative protein example
    occurs. Current source read includes text captions only, not pixels, raw data
    or supplements. These optional domains are not filled by inference.
  target_ids:
  - GO:0070116
  evidence_ids:
  - septin-record-organellar_chromatophore_thylakoid
  - septin-protein-policy
- assessment_id: septin-organellar_chromatophore_thylakoid-history
  area: provenance
  topic: History and context are not new issue dispositions
  outcome: supported
  summary: Record retains PROPOSED status and historical curation events. Existing
    boundary/grounding discussion is read in its exact field scope. Frozen whole chromatophore
    is boundary context only; distinct whole-record issues or previous historical
    closures are not newly resolved by this review.
  target_ids:
  - GO:0070116
  evidence_ids:
  - septin-record-organellar_chromatophore_thylakoid
  - septin-context-organellar_chromatophore
- assessment_id: septin-organellar_chromatophore_thylakoid-verdict
  area: completeness
  topic: Current scientific verdict
  outcome: concern
  summary: 'needs_curation: retain exact inherited F1 major grounding and F2 minor
    source attribution, with two separately authorized curation actions. No new scientific
    finding.'
  target_ids:
  - GO:0070116
  evidence_ids:
  - septin-record-organellar_chromatophore_thylakoid
  - septin-original-organellar_chromatophore_thylakoid
  - septin-go
  - septin-SL0354
  - septin-nowack2012-prefixed
  - septin-curation-policy
- assessment_id: septin-organellar_chromatophore_thylakoid_lumen-schema
  area: schema
  topic: Original native schema/render and unchanged input
  outcome: supported
  summary: Original validate/render exit0 and Markdown exact; current record matches
    the review frozen hash. No assigned target is stale. Schema validity is distinct
    from the scientific judgment.
  target_ids:
  - GO:0070117
  evidence_ids:
  - septin-record-organellar_chromatophore_thylakoid_lumen
  - septin-original-validation-organellar_chromatophore_thylakoid_lumen
- assessment_id: septin-organellar_chromatophore_thylakoid_lumen-identity
  area: identity
  topic: Exact identity, synonyms and anatomy
  outcome: supported
  summary: Exact GO0070117 definition and Paulinella-type synonym match. GO0031978
    plastid lumen parent is positively supported by SL0355 isA, even though it is
    absent from current GO is_a ancestry. Whole thylakoid parthood is separate from
    class membership.
  target_ids:
  - GO:0070117
  evidence_ids:
  - septin-record-organellar_chromatophore_thylakoid_lumen
  - septin-go
  - septin-SL0355
  - septin-GO0070117-isa
  - septin-context-organellar_chromatophore
- assessment_id: septin-organellar_chromatophore_thylakoid_lumen-classification-limits
  area: scope
  topic: Ontology versus native classification scope
  outcome: supported
  summary: Source hierarchy and textual definitions need separate attribution. GO
    generic thylakoid comment says it is not considered an organelle, whereas the
    repository native category explicitly includes thylakoids. The physical membrane-bounded
    lumen and native model support the retained structure_kind without an enum-only
    finding. GO0070112 definition emphasizes enclosing bilayers while its hierarchy
    also includes internal thylakoid membranes; current explicit hierarchy/SL support
    is retained without silently rewriting the source.
  target_ids:
  - GO:0070117
  evidence_ids:
  - septin-record-organellar_chromatophore_thylakoid_lumen
  - septin-go
  - septin-GO0070116-isa
  - septin-GO0070118-isa
  - septin-schema-policy
  - septin-SL0355
- assessment_id: septin-organellar_chromatophore_thylakoid_lumen-taxa
  area: scope
  topic: Taxon identity and qualitative presence
  outcome: supported
  summary: Paulinella39716 is a genus. Exact SL range supports the bounded organism
    context, and VARIABLE notes explicitly avoid asserting every genus member carries
    chromatophores. No numerical prevalence or all-species universal claim is introduced.
  target_ids:
  - GO:0070117
  evidence_ids:
  - septin-record-organellar_chromatophore_thylakoid_lumen
  - septin-tax39716
  - septin-tax39717
  - septin-SL0355
  - septin-nowack2014-crossref
  - septin-nowack2012-prefixed
- assessment_id: septin-organellar_chromatophore_thylakoid_lumen-materials
  area: grounding
  topic: Whole structure and collective lipid material
  outcome: supported
  summary: No component inventory is asserted. Boundary membrane remains a STRUCTURE
    node without component_ref; it is not misrepresented as lumen material. Historical
    resolved boundary interpretation is consistent with current fields.
  target_ids:
  - GO:0070117
  evidence_ids:
  - septin-record-organellar_chromatophore_thylakoid_lumen
  - septin-go
  - septin-SL0355
  - septin-curation-policy
  - septin-schema-policy
- assessment_id: septin-organellar_chromatophore_thylakoid_lumen-graph
  area: graph
  topic: Complete descriptive graph and declared limits
  outcome: supported
  summary: 'One NONMECHANISTIC edge: membrane encloses lumen. GO0070117 andSL0355
    support the exact boundary; scope explicitly withholds lumenal proteins and photosynthetic
    proton-transport mechanisms. No source is silently promoted into a transport pathway.'
  target_ids:
  - GO:0070117
  evidence_ids:
  - septin-record-organellar_chromatophore_thylakoid_lumen
  - septin-graph-policy
  - septin-go
  - septin-SL0354
  - septin-SL0355
  - septin-SL0356
- assessment_id: septin-organellar_chromatophore_thylakoid_lumen-native
  area: provenance
  topic: Actual native protein verification coverage
  outcome: supported
  summary: Both actual commands exit0 and independent full-record inventory confirms
    zero examples, zero typed molecular nodes and zero UniProtKB graph xrefs. Generic
    verify text alone is not treated as inventory evidence; empty native coverage
    is not biological completeness.
  target_ids:
  - GO:0070117
  evidence_ids:
  - septin-record-organellar_chromatophore_thylakoid_lumen
  - septin-native-organellar_chromatophore_thylakoid_lumen-verify
  - septin-native-organellar_chromatophore_thylakoid_lumen-causal
- assessment_id: septin-organellar_chromatophore_thylakoid_lumen-adapter
  area: scope
  topic: Genuine spatial-only applicability exclusion
  outcome: not_applicable
  summary: Full record asserts identity, spatial enclosure and qualitative occurrence
    only; it explicitly excludes lumenal proteins and photosynthetic proton transport.
    Therefore its original N/A outcome is genuine, clarified with actual scope instead
    of expression-only shorthand. Nested SL parent molecular prose is not an asserted
    child-record mechanism. No applicability defect or irrelevant gene query is manufactured.
  target_ids:
  - GO:0070117
  evidence_ids:
  - septin-record-organellar_chromatophore_thylakoid_lumen
  - septin-original-organellar_chromatophore_thylakoid_lumen
  - septin-review-policy
  - septin-catalogue
  - septin-adapter-runner-historical
- assessment_id: septin-organellar_chromatophore_thylakoid_lumen-omitted-domains
  area: scope
  topic: No unrepresented image, measurement or protein assertion
  outcome: not_applicable
  summary: No maintained image or licence claim, numeric measurement, associated trait,
    verbatim snippet, individual gene/protein identity or representative protein example
    occurs. Current source read includes text captions only, not pixels, raw data
    or supplements. These optional domains are not filled by inference.
  target_ids:
  - GO:0070117
  evidence_ids:
  - septin-record-organellar_chromatophore_thylakoid_lumen
  - septin-protein-policy
- assessment_id: septin-organellar_chromatophore_thylakoid_lumen-history
  area: provenance
  topic: History and context are not new issue dispositions
  outcome: supported
  summary: Record retains PROPOSED status and historical curation events. Existing
    boundary/grounding discussion is read in its exact field scope. Frozen whole chromatophore
    is boundary context only; distinct whole-record issues or previous historical
    closures are not newly resolved by this review.
  target_ids:
  - GO:0070117
  evidence_ids:
  - septin-record-organellar_chromatophore_thylakoid_lumen
  - septin-context-organellar_chromatophore
- assessment_id: septin-organellar_chromatophore_thylakoid_lumen-verdict
  area: completeness
  topic: Current scientific verdict
  outcome: supported
  summary: 'pass_with_limitations: current identity, topology and explicitly bounded
    assertions are supported; no inherited or new scientific finding. Retain source-tier,
    occurrence, native-empty-inventory and optional composition limits.'
  target_ids:
  - GO:0070117
  evidence_ids:
  - septin-record-organellar_chromatophore_thylakoid_lumen
  - septin-original-organellar_chromatophore_thylakoid_lumen
  - septin-go
  - septin-SL0355
  - septin-nowack2012-prefixed
  - septin-curation-policy
- assessment_id: septin-organellar_chromatophore_thylakoid_membrane-schema
  area: schema
  topic: Original native schema/render and unchanged input
  outcome: supported
  summary: Original validate/render exit0 and Markdown exact; current record matches
    the review frozen hash. No assigned target is stale. Schema validity is distinct
    from the scientific judgment.
  target_ids:
  - GO:0070118
  evidence_ids:
  - septin-record-organellar_chromatophore_thylakoid_membrane
  - septin-original-validation-organellar_chromatophore_thylakoid_membrane
- assessment_id: septin-organellar_chromatophore_thylakoid_membrane-identity
  area: identity
  topic: Exact identity, synonyms and anatomy
  outcome: supported
  summary: Exact GO0070118 definition and Paulinella-type synonym match. GO0042651
    andGO0070112 are present in GO is_a ancestry; additional GO0055035 plastid membrane
    parent is explicitly supported by SL0356 isA. Whole thylakoid parthood is distinct.
  target_ids:
  - GO:0070118
  evidence_ids:
  - septin-record-organellar_chromatophore_thylakoid_membrane
  - septin-go
  - septin-SL0356
  - septin-GO0070118-isa
  - septin-context-organellar_chromatophore
- assessment_id: septin-organellar_chromatophore_thylakoid_membrane-classification-limits
  area: scope
  topic: Ontology versus native classification scope
  outcome: supported
  summary: Source hierarchy and textual definitions need separate attribution. GO
    generic thylakoid comment says it is not considered an organelle, whereas the
    repository native category explicitly includes thylakoids. The physical membrane-bounded
    lumen and native model support the retained structure_kind without an enum-only
    finding. GO0070112 definition emphasizes enclosing bilayers while its hierarchy
    also includes internal thylakoid membranes; current explicit hierarchy/SL support
    is retained without silently rewriting the source.
  target_ids:
  - GO:0070118
  evidence_ids:
  - septin-record-organellar_chromatophore_thylakoid_membrane
  - septin-go
  - septin-GO0070116-isa
  - septin-GO0070118-isa
  - septin-schema-policy
  - septin-SL0356
- assessment_id: septin-organellar_chromatophore_thylakoid_membrane-taxa
  area: scope
  topic: Taxon identity and qualitative presence
  outcome: supported
  summary: Paulinella39716 is a genus. Exact SL range supports the bounded organism
    context, and VARIABLE notes explicitly avoid asserting every genus member carries
    chromatophores. No numerical prevalence or all-species universal claim is introduced.
  target_ids:
  - GO:0070118
  evidence_ids:
  - septin-record-organellar_chromatophore_thylakoid_membrane
  - septin-tax39716
  - septin-tax39717
  - septin-SL0356
  - septin-nowack2014-crossref
  - septin-nowack2012-prefixed
- assessment_id: septin-organellar_chromatophore_thylakoid_membrane-materials
  area: grounding
  topic: Whole structure and collective lipid material
  outcome: supported
  summary: One REVIEWED_LABEL_ONLY LIPID row explicitly denotes collective bilayer
    material and does not use whole-membrane GO as chemical grounding. ESSENTIAL refers
    to constitutive collective membrane material, not individual lipid/protein depletion
    or formation necessity. Exact chemical identity remains an explicit TODO without
    a fabricated CURIE.
  target_ids:
  - GO:0070118
  evidence_ids:
  - septin-record-organellar_chromatophore_thylakoid_membrane
  - septin-go
  - septin-SL0356
  - septin-curation-policy
  - septin-schema-policy
- assessment_id: septin-organellar_chromatophore_thylakoid_membrane-light-complexes
  area: evidence
  topic: Positive photosynthetic light-complex evidence
  outcome: supported
  summary: SL0354/SL0356 explicitly describe light-reaction complexes. Re-read Nowack2012
    primary Results support PsaE thylakoid association and selected imported PSI subunits
    associating with purified PSI in one cultured P. chromatophora subisolate. These
    observations support the modest light-reaction-site claim without enumerating
    the complete photosystem/electron-transport chain.
  target_ids:
  - GO:0070118
  evidence_ids:
  - septin-record-organellar_chromatophore_thylakoid_membrane
  - septin-SL0354
  - septin-SL0356
  - septin-nowack2012-prefixed
  - septin-go
- assessment_id: septin-organellar_chromatophore_thylakoid_membrane-source-attribution
  area: evidence
  topic: Exact source placement
  outcome: supported
  summary: Component and supports-edge use GO0070118 only for the bilayer definition
    and explicitly cite SL0356 for light-reaction complexes. This exact source distinction
    avoids the separate whole-thylakoid record finding.
  target_ids:
  - GO:0070118
  evidence_ids:
  - septin-record-organellar_chromatophore_thylakoid_membrane
  - septin-go
  - septin-SL0354
  - septin-SL0356
  - septin-nowack2012-prefixed
- assessment_id: septin-organellar_chromatophore_thylakoid_membrane-necessity
  area: evidence
  topic: Formation and complete composition remain unknown
  outcome: unknown
  summary: Neither exact location authority nor the bounded primary localization/purification
    experiment establishes every lipid/protein identity, stoichiometry, cross-strain
    conservation or individual necessity for thylakoid formation. No missing optional
    protein examples or automatic protein-complex type defect is inferred.
  target_ids:
  - GO:0070118
  evidence_ids:
  - septin-record-organellar_chromatophore_thylakoid_membrane
  - septin-nowack2012-prefixed
  - septin-protein-policy
  - septin-schema-policy
- assessment_id: septin-organellar_chromatophore_thylakoid_membrane-graph
  area: graph
  topic: Complete descriptive graph and declared limits
  outcome: supported
  summary: 'Two NONMECHANISTIC edges: membrane bounds lumen and supports light reactions.
    GO supports topology andSL0356 the functional clause. The scope explicitly withholds
    a complete photosystem/electron-transport inventory.'
  target_ids:
  - GO:0070118
  evidence_ids:
  - septin-record-organellar_chromatophore_thylakoid_membrane
  - septin-graph-policy
  - septin-go
  - septin-SL0354
  - septin-SL0355
  - septin-SL0356
- assessment_id: septin-organellar_chromatophore_thylakoid_membrane-native
  area: provenance
  topic: Actual native protein verification coverage
  outcome: supported
  summary: Both actual commands exit0 and independent full-record inventory confirms
    zero examples, zero typed molecular nodes and zero UniProtKB graph xrefs. Generic
    verify text alone is not treated as inventory evidence; empty native coverage
    is not biological completeness.
  target_ids:
  - GO:0070118
  evidence_ids:
  - septin-record-organellar_chromatophore_thylakoid_membrane
  - septin-native-organellar_chromatophore_thylakoid_membrane-verify
  - septin-native-organellar_chromatophore_thylakoid_membrane-causal
- assessment_id: septin-organellar_chromatophore_thylakoid_membrane-adapter
  area: scope
  topic: Corrected positive pathway applicability assessment
  outcome: supported
  summary: Record positively asserts photosynthetic light-reaction complexes in component/function/graph
    narrative despite no individual protein inventory. Original absence-of-expression
    rationale is insufficient. Fresh full official catalogue contains no matched Paulinella
    host/strain, so source-specific SL/primary checks are the bounded fallback; no
    free-living cyanobacterial proxy or gene/module query is substituted. This completes
    applicability assessment, not a new native runner execution.
  target_ids:
  - GO:0070118
  evidence_ids:
  - septin-record-organellar_chromatophore_thylakoid_membrane
  - septin-original-organellar_chromatophore_thylakoid_membrane
  - septin-review-policy
  - septin-catalogue
  - septin-adapter-runner-historical
  - septin-nowack2012-prefixed
  - septin-SL0356
- assessment_id: septin-organellar_chromatophore_thylakoid_membrane-omitted-domains
  area: scope
  topic: No unrepresented image, measurement or protein assertion
  outcome: not_applicable
  summary: No maintained image or licence claim, numeric measurement, associated trait,
    verbatim snippet, individual gene/protein identity or representative protein example
    occurs. Current source read includes text captions only, not pixels, raw data
    or supplements. These optional domains are not filled by inference.
  target_ids:
  - GO:0070118
  evidence_ids:
  - septin-record-organellar_chromatophore_thylakoid_membrane
  - septin-protein-policy
- assessment_id: septin-organellar_chromatophore_thylakoid_membrane-history
  area: provenance
  topic: History and context are not new issue dispositions
  outcome: supported
  summary: Record retains PROPOSED status and historical curation events. Existing
    boundary/grounding discussion is read in its exact field scope. Frozen whole chromatophore
    is boundary context only; distinct whole-record issues or previous historical
    closures are not newly resolved by this review.
  target_ids:
  - GO:0070118
  evidence_ids:
  - septin-record-organellar_chromatophore_thylakoid_membrane
  - septin-context-organellar_chromatophore
- assessment_id: septin-organellar_chromatophore_thylakoid_membrane-verdict
  area: completeness
  topic: Current scientific verdict
  outcome: supported
  summary: 'pass_with_limitations: current identity, topology and explicitly bounded
    assertions are supported; no inherited or new scientific finding. Retain source-tier,
    occurrence, native-empty-inventory and optional composition limits.'
  target_ids:
  - GO:0070118
  evidence_ids:
  - septin-record-organellar_chromatophore_thylakoid_membrane
  - septin-original-organellar_chromatophore_thylakoid_membrane
  - septin-go
  - septin-SL0356
  - septin-nowack2012-prefixed
  - septin-curation-policy
- assessment_id: plaque-t7-schema
  area: schema
  topic: Immutable original and current source checks
  outcome: supported
  summary: Exact target unchanged. Original pair passes native validation/deterministic
    rendering and15historical hashes; current accession coverage retains actual empty/populated
    scope. Root owns full local gates and publication.
  target_ids:
  - GO:0044310
  evidence_ids:
  - plaque-current-7
  - plaque-original-7
  - plaque-original-checks
  - plaque-native-osmiophilic_body-verify
  - plaque-native-osmiophilic_body-causal
- assessment_id: plaque-t8-schema
  area: schema
  topic: Immutable original and current source checks
  outcome: supported
  summary: Exact target unchanged. Original pair passes native validation/deterministic
    rendering and15historical hashes; current accession coverage retains actual empty/populated
    scope. Root owns full local gates and publication.
  target_ids:
  - cellstructuremech:parasitophorous_vacuole
  evidence_ids:
  - plaque-current-8
  - plaque-original-8
  - plaque-original-checks
  - plaque-native-parasitophorous_vacuole-verify
  - plaque-native-parasitophorous_vacuole-causal
- assessment_id: plaque-t9-schema
  area: schema
  topic: Immutable original and current source checks
  outcome: supported
  summary: Exact target unchanged. Original pair passes native validation/deterministic
    rendering and15historical hashes; current accession coverage retains actual empty/populated
    scope. Root owns full local gates and publication.
  target_ids:
  - cellstructuremech:parasitophorous_vacuole_lumen
  evidence_ids:
  - plaque-current-9
  - plaque-original-9
  - plaque-original-checks
  - plaque-native-parasitophorous_vacuole_lumen-verify
  - plaque-native-parasitophorous_vacuole_lumen-causal
- assessment_id: plaque-t7-identity
  area: identity
  topic: Exact osmiophilic secretory vesicle
  outcome: supported
  summary: GO0044310 exact current definition and direct0031410 parent agree. Record
    denotes organelle, not protein or phenotype. The definition explicitly calls content-release
    aid postulated; this historical ontology wording is not itself a demonstrated-mechanism
    claim.
  target_ids:
  - GO:0044310
  evidence_ids:
  - plaque-current-7
  - plaque-go
  - plaque-dekoning2008-meta
- assessment_id: plaque-t7-material
  area: grounding
  topic: Boundary material and protein component
  outcome: supported
  summary: Label-only collective membrane has no incorrectly applied whole-membrane
    chemical CURIE. Pfg377 association is supported by1995 primary abstract immunoelectron
    localization and2016 body. No precise lipid species or complete protein inventory
    is claimed.
  target_ids:
  - GO:0044310
  evidence_ids:
  - plaque-current-7
  - plaque-go
  - plaque-alano1995-pmid
  - plaque-suarez2016-pmc
  - plaque-schema-policy
- assessment_id: plaque-t7-protein
  area: grounding
  topic: Actual Pfg377 accession identity and limits
  outcome: supported
  summary: A0A059WIJ2 matches pfg377/taxon5833/UNREVIEWED.193-aa G1 fragment is not
    full-length experimental3D7 protein, but maintained example explicitly only establishes
    gene identity. No mandatory replacement or new instance defect follows.
  target_ids:
  - GO:0044310
  evidence_ids:
  - plaque-current-7
  - plaque-pfg377
  - plaque-protein-contract
- assessment_id: plaque-t7-family
  area: grounding
  topic: Family mapping remains bounded unknown
  outcome: unknown
  summary: Exact InterPro association request204 provides no usable family list; reviewed-gene
    query returns0. PANTHER crossreferences are not verified here as exact source-neutral
    class. No guessed grounding or exhaustive family-absence claim.
  target_ids:
  - GO:0044310
  evidence_ids:
  - plaque-current-7
  - plaque-pfg377
  - plaque-pfg377-interpro
  - plaque-pfg377-reviewed-search
- assessment_id: plaque-t7-necessity
  area: scope
  topic: Normal complement versus absolute formation
  outcome: supported
  summary: 'Membrane ESSENTIAL is definitional boundary, not experimentally demonstrated
    particular lipid necessity. Protein UNKNOWN essentiality remains conservative:
    depleted bodies and residual abnormal granules distinguish normal complement from
    absolute no-organelle formation.'
  target_ids:
  - GO:0044310
  evidence_ids:
  - plaque-current-7
  - plaque-go
  - plaque-suarez2016-pmc
- assessment_id: plaque-t7-taxon
  area: scope
  topic: Female-gametocyte and experimental strain context
  outcome: supported
  summary: Species5833 correct; COMMON explicitly scoped mature female gametocytes,
    not all cells.1995/2016 experiments are3D7 context; native sequenceG1 is separately
    labeled representative identity.2008 historical canonical example is tied to its
    specific source.
  target_ids:
  - GO:0044310
  evidence_ids:
  - plaque-current-7
  - plaque-tax5833
  - plaque-alano1995-pmid
  - plaque-dekoning2008-meta
  - plaque-suarez2016-pmc
  - plaque-pfg377
- assessment_id: plaque-t7-F1
  area: graph
  topic: Inherited unqualified egress explanation conflicts with cited evidence
  outcome: concern
  summary: Record functions0/general graph description/edge3 and emergence explanation
    for oocyst defect do not reconcile its cited2016 normal-egress finding in independent
    OB-depleted clones. NONMECHANISTIC label avoids physical secretion proof but not
    this material functional overstatement. Preserve exact inheritedmajor key,2008
    observation and qualified2016 timing.
  target_ids:
  - GO:0044310
  evidence_ids:
  - plaque-current-7
  - plaque-original-7
  - plaque-dekoning2008-meta
  - plaque-suarez2016-pmc
  - plaque-graph-rubric
- assessment_id: plaque-t7-other-edges
  area: graph
  topic: Supported edges and infection association survive
  outcome: supported
  summary: Membrane bounds organelle, Pfg377 associates with it and supports normal-body
    complement; these edges remain supported. Both studies report strong mosquito
    infection impairment.2016 does not prove an alternative direct post-egress mechanism
    or refute all possible kinetic/strain-dependent contributions.
  target_ids:
  - GO:0044310
  evidence_ids:
  - plaque-current-7
  - plaque-go
  - plaque-alano1995-pmid
  - plaque-dekoning2008-meta
  - plaque-suarez2016-pmc
- assessment_id: plaque-t7-adapter
  area: evidence
  topic: Positive protein and transmission pathway triggers
  outcome: supported
  summary: Pfg377 gene/accession, knockout phenotype and egress/transmission claims
    trigger native structured-source assessment. Current catalogue has no matched
    Plasmodium host; downstream queries not applicable after real coverage check.
    Original no-expression exemption needs linked-review correction.
  target_ids:
  - GO:0044310
  evidence_ids:
  - plaque-current-7
  - plaque-original-7
  - plaque-policy
  - plaque-catalogue
  - plaque-historical-runner
- assessment_id: plaque-t7-limits
  area: evidence
  topic: Primary access and phenotype bounds
  outcome: unknown
  summary: Alano/deKoning full bodies not obtained, complete primary abstracts read.
    Suarez declared Methods/Results/Discussion plusFig1caption only; no pixels/supplements/raw
    proteomics.15-minute assay does not resolve every transient kinetic effect. Additional
    OB proteins are optional, not invented completeness findings.
  target_ids:
  - GO:0044310
  evidence_ids:
  - plaque-alano1995-pmid
  - plaque-dekoning2008-meta
  - plaque-dekoning2008-repository
  - plaque-suarez2016-pmc
  - plaque-access-routes
- assessment_id: plaque-t8-identity
  area: identity
  topic: Exact apicomplexan PV versus broad GO
  outcome: supported
  summary: SL0194 specifically scopes host-cell vacuole to most apicomplexans. Broader
    GO0020003 definition includes general symbionts despite exact lexical PV synonym,
    so local narrow identity plus GO parent remains defensible.
  target_ids:
  - cellstructuremech:parasitophorous_vacuole
  evidence_ids:
  - plaque-current-8
  - plaque-SL-0194
  - plaque-go
- assessment_id: plaque-t8-topology
  area: graph
  topic: Whole vacuole membrane and lumen boundaries
  outcome: supported
  summary: Local PVM and lumen identifiers resolve in frozen contexts. Single NONMECHANISTIC
    bounds edge and has_part links agree with exact SL0193/0341; no secretory mechanism
    or molecular component essentiality is asserted by graph.
  target_ids:
  - cellstructuremech:parasitophorous_vacuole
  evidence_ids:
  - plaque-current-8
  - plaque-current-9
  - plaque-context-pvm
  - plaque-SL-0193
  - plaque-SL-0194
  - plaque-SL-0341
  - plaque-go
- assessment_id: plaque-t8-occurrence
  area: scope
  topic: Qualitative niche and Toxoplasma example
  outcome: supported
  summary: Apicomplexa COMMON is expressly most-parasite qualitative scope, not universal
    every stage. Clough secondary abstract supports Toxoplasma interface/replication
    niche; Lingelbach secondary abstract supports invasion-associated surrounding
    membrane. No complete primary nutrient/permeability mechanism is certified.
  target_ids:
  - cellstructuremech:parasitophorous_vacuole
  evidence_ids:
  - plaque-current-8
  - plaque-tax5794
  - plaque-tax5811
  - plaque-SL-0194
  - plaque-clough2017-meta
  - plaque-lingelbach1998-meta
- assessment_id: plaque-t8-F1
  area: evidence
  topic: Inherited BioID experimental taxon mismatch
  outcome: concern
  summary: Canonical example1 says P.falciparum BioID with Schnider2018. Exact primary
    abstract/JATS identify P.berghei ANKA mCherryHsp70 blood-stage experiment. P.falciparum
    orthologs and earlier literature are separate comparisons, not experiment provenance;
    preserve inheritedmajor key.
  target_ids:
  - cellstructuremech:parasitophorous_vacuole
  evidence_ids:
  - plaque-current-8
  - plaque-original-8
  - plaque-tax5833
  - plaque-tax5821
  - plaque-schnider2018-meta
  - plaque-schnider2018-body
- assessment_id: plaque-t8-candidate-scope
  area: evidence
  topic: Proximity candidates are not complete composition or necessity
  outcome: supported
  summary: Schnider lists61candidates; off-target PV/PPM labeling and secretion transit
    are explicit. This validates bounded survey provenance, not membership/necessity
    of all candidates in whole PV or every species. Correcting taxon does not entail
    importing61components or new causal mechanisms.
  target_ids:
  - cellstructuremech:parasitophorous_vacuole
  evidence_ids:
  - plaque-current-8
  - plaque-schnider2018-body
  - plaque-rubric
- assessment_id: plaque-t8-adapter
  area: evidence
  topic: Positive BioID PVM protein assertion triggers coverage
  outcome: supported
  summary: Although no molecular component inventory exists and graph is topology-only,
    canonical example positively asserts a PVM protein survey and replication niche.
    Whole-record molecular assertion triggers applicability. Official catalogue has
    no Plasmodium/Toxoplasma match; no foreign-host query/negative inference.
  target_ids:
  - cellstructuremech:parasitophorous_vacuole
  evidence_ids:
  - plaque-current-8
  - plaque-original-8
  - plaque-policy
  - plaque-catalogue
  - plaque-historical-runner
- assessment_id: plaque-t8-history
  area: provenance
  topic: Historical fixes and neighboring evidence remain separate
  outcome: supported
  summary: Historical820–822 and resolved membrane-identity TODO are not terminally
    re-adjudicated. Frozen neighbor used for exact boundary context only; this successor
    fixes no neighbor record or broader issue. Original scientific observations remain
    immutable.
  target_ids:
  - cellstructuremech:parasitophorous_vacuole
  evidence_ids:
  - plaque-current-8
  - plaque-original-8
  - plaque-context-pvm
- assessment_id: plaque-t8-limits
  area: evidence
  topic: Primary versus secondary source coverage
  outcome: unknown
  summary: Schnider only declared Results/Discussion/Methods and embedded captions
    read; no pixels/supplementary files or quantitative reanalysis. Lingelbach/Clough
    are complete secondary abstracts only; blocked/redirect pages do not certify full
    text.
  target_ids:
  - cellstructuremech:parasitophorous_vacuole
  evidence_ids:
  - plaque-schnider2018-body
  - plaque-clough2017-meta
  - plaque-lingelbach1998-meta
  - plaque-access-routes
- assessment_id: plaque-t9-identity
  area: identity
  topic: Exact PV lumen with broader vacuolar-space parent
  outcome: supported
  summary: SL0341 exact definition/synonym and partOfPV agree. GO0020004 broadly denotes
    space between symbiont plasma membrane and enclosing vacuole membrane. Neither
    broad synonym nor definition warrants collapsing narrow local apicomplexan lumen
    identity.
  target_ids:
  - cellstructuremech:parasitophorous_vacuole_lumen
  evidence_ids:
  - plaque-current-9
  - plaque-SL-0341
  - plaque-SL-0194
  - plaque-go
- assessment_id: plaque-t9-topology
  area: graph
  topic: One descriptive lumen parthood edge
  outcome: supported
  summary: Internal compartment and local PV parthood are explicit in native location
    authority; bounded region is not the whole membrane or parasite. Graph specifically
    excludes residence, nutrient access and remodeling mechanisms.
  target_ids:
  - cellstructuremech:parasitophorous_vacuole_lumen
  evidence_ids:
  - plaque-current-9
  - plaque-current-8
  - plaque-SL-0341
  - plaque-SL-0194
  - plaque-context-pvm
- assessment_id: plaque-t9-taxon
  area: scope
  topic: Qualitative apicomplexan context
  outcome: supported
  summary: ENA verifies phylum5794. COMMON explicitly inherits most-apicomplexan location
    definition; not every stage/cell or a quantitative frequency. No canonical strain,
    protein essentiality or dimensions asserted.
  target_ids:
  - cellstructuremech:parasitophorous_vacuole_lumen
  evidence_ids:
  - plaque-current-9
  - plaque-tax5794
  - plaque-SL-0194
  - plaque-SL-0341
- assessment_id: plaque-t9-adapter
  area: evidence
  topic: Genuine physical and topology exclusion
  outcome: not_applicable
  summary: Whole positive content concerns exact region, boundaries and qualitative
    host context. Molecular mechanisms/functions were explicitly removed/excluded;
    neighboring protein survey is not inherited as lumen content. Original exclusion
    remains appropriate with precise scope rationale, no bundle defect.
  target_ids:
  - cellstructuremech:parasitophorous_vacuole_lumen
  evidence_ids:
  - plaque-current-9
  - plaque-original-9
  - plaque-policy
  - plaque-SL-0341
  - plaque-catalogue
- assessment_id: plaque-t9-completeness
  area: evidence
  topic: No mandatory molecular contents or mechanism
  outcome: supported
  summary: Empty optional components/functions/examples are not material defects in
    deliberately limited region record. Historical824/825 mentions are provenance,
    not current blanket closure or re-adjudication. Lumen has no inherited scientific
    finding.
  target_ids:
  - cellstructuremech:parasitophorous_vacuole_lumen
  evidence_ids:
  - plaque-current-9
  - plaque-original-9
  - plaque-rubric
  - plaque-schema-policy
- assessment_id: micro-organellar_chromatophore_inner_membrane-identity
  area: identity
  topic: Exact identity, synonyms, subtype and parthood
  outcome: supported
  summary: GO0070113 and SL0359 exactly identify the inner stroma-facing bilayer.
    GO supports chromatophore-membrane subclass; UniProt explicitly supplies plastid-inner-membrane
    parent and chromatophore parthood. No absent GO plastid edge is fabricated.
  target_ids:
  - GO:0070113
  evidence_ids:
  - micro-record-organellar_chromatophore_inner_membrane
  - micro-go
  - micro-SL0359
  - micro-go-0070113-isa
  - micro-SL0351
- assessment_id: micro-organellar_chromatophore_inner_membrane-composition
  area: grounding
  topic: Material constituent distinct from complete anatomical identity
  outcome: supported
  summary: Single LIPID/CONSTITUENT is the collective bilayer material, REVIEWED_LABEL_ONLY
    with notes and no whole-membrane GO chemical grounding. Anatomical GO identities
    remain on the record/structure nodes. No precise lipid complement is invented.
  target_ids:
  - GO:0070113
  evidence_ids:
  - micro-record-organellar_chromatophore_inner_membrane
  - micro-component-policy
  - micro-SL0359
  - micro-SL0351
  - micro-go
- assessment_id: micro-organellar_chromatophore_inner_membrane-necessity
  area: evidence
  topic: Constitutive material versus experimental formation necessity
  outcome: unknown
  summary: ESSENTIAL is supported only for the defining collective bilayer, not an
    individual lipid species or protein. No particular molecular formation requirement
    is asserted or established by these sources.
  target_ids:
  - GO:0070113
  evidence_ids:
  - micro-record-organellar_chromatophore_inner_membrane
  - micro-component-policy
  - micro-go
  - micro-SL0359
  - micro-nowack2012-body
- assessment_id: micro-organellar_chromatophore_inner_membrane-graph
  area: graph
  topic: Every edge, node and scope
  outcome: supported
  summary: 'Two NONMECHANISTIC edges: inner membrane bounds stroma and delimits intermembrane
    space. SL0359 expressly describes the separation. Label-only stroma node is coherent;
    current SL0353 is optional enrichment, not a new source claim or historical correction.'
  target_ids:
  - GO:0070113
  evidence_ids:
  - micro-record-organellar_chromatophore_inner_membrane
  - micro-graph-policy
  - micro-go
  - micro-SL0359
  - micro-SL0351
  - micro-SL0353
- assessment_id: micro-organellar_chromatophore_inner_membrane-taxon
  area: scope
  topic: Verified genus and qualitative variable occurrence
  outcome: supported
  summary: Paulinella39716 genus is correct. Explicit VARIABLE avoids claiming every
    species has chromatophores; secondary Gabr S2 distinguishes photosynthetic and
    heterotrophic lineages. Primary Nowack culture is CCAC0185/subisolateM0880/a,
    not a genus-wide sample. No frequency estimate or experimental strain substitution.
  target_ids:
  - GO:0070113
  evidence_ids:
  - micro-record-organellar_chromatophore_inner_membrane
  - micro-tax39716
  - micro-SL0359
  - micro-gabr2020-canonical
  - micro-nowack2012-body
- assessment_id: micro-organellar_chromatophore_inner_membrane-adapter
  area: evidence
  topic: Whole-record structured-source applicability
  outcome: not_applicable
  summary: Full target asserts material anatomy and localization scope, with no named
    protein/regulator/pathway/stress-response claim. Inner/outer explicitly withhold
    import and photosynthetic machinery; generic fallback scope is not an asserted
    protein inventory. The original exclusion is genuine despite its generic expression-only
    explanation.
  target_ids:
  - GO:0070113
  evidence_ids:
  - micro-record-organellar_chromatophore_inner_membrane
  - micro-prior-organellar_chromatophore_inner_membrane
  - micro-policy
  - micro-catalogue
  - micro-historical-runner
- assessment_id: micro-organellar_chromatophore_inner_membrane-sources
  area: evidence
  topic: Exact authorities and bounded primary/secondary context
  outcome: supported
  summary: All maintained citations are GO/UniProt-location authorities for anatomical
    identity/topology. Current primary Nowack body reread is only the declared sections/captions,
    with actual earlier retrieval time; Gabr fresh S2 body is secondary context. No
    source pixels, unlisted sections, molecular assembly assay or compulsory protein
    completeness claimed.
  target_ids:
  - GO:0070113
  evidence_ids:
  - micro-record-organellar_chromatophore_inner_membrane
  - micro-go
  - micro-SL0359
  - micro-SL0351
  - micro-nowack2012-body
  - micro-nowack2012-meta
  - micro-gabr2020-canonical
  - micro-gabr2020-meta
- assessment_id: micro-organellar_chromatophore_inner_membrane-native
  area: schema
  topic: Original hashes, native validation/render and current protein coverage
  outcome: supported
  summary: All68 old input entries verify at retained source, all4 old pairs validate/render
    exactly and target hash remains unchanged. Current verify/causal commands exit0
    with zero examples and zero typed protein nodes; not evidence of molecular completeness.
  target_ids:
  - GO:0070113
  evidence_ids:
  - micro-prior-organellar_chromatophore_inner_membrane
  - micro-original-inputs
  - micro-original-pairs
  - micro-native-organellar_chromatophore_inner_membrane-verify
  - micro-native-organellar_chromatophore_inner_membrane-causal
- assessment_id: micro-organellar_chromatophore_inner_membrane-history
  area: provenance
  topic: Historical rationale and scientific status
  outcome: supported
  summary: Full record history/discussions retained; PROPOSED status unchanged. Label-only
    material grounding TODOs remain bounded optional identity questions; no empty-slot
    defect or whole-issue resolution inferred. Historical removal of unavailableSL0353
    is not retroactively false because it resolves now.
  target_ids:
  - GO:0070113
  evidence_ids:
  - micro-record-organellar_chromatophore_inner_membrane
  - micro-prior-organellar_chromatophore_inner_membrane
  - micro-policy
  - micro-component-policy
  - micro-SL0353
- assessment_id: micro-organellar_chromatophore_inner_membrane-coverage
  area: completeness
  topic: Complete record, absent optional claim surfaces and verdict
  outcome: supported
  summary: 'Entire current record read: no images, physical-measurement objects, individual
    protein accessions, gene symbols, complex-composition inventory or verbatim quotations
    require extra checks. No supported scientific or review-bundle defect observed.
    Qualified pass retains chemical, assembly, prevalence and source-access limits;
    no inherited findings exist.'
  target_ids:
  - GO:0070113
  evidence_ids:
  - micro-record-organellar_chromatophore_inner_membrane
  - micro-prior-organellar_chromatophore_inner_membrane
  - micro-policy
  - micro-original-pairs
- assessment_id: micro-organellar_chromatophore_intermembrane_space-identity
  area: identity
  topic: Exact identity, synonyms, subtype and parthood
  outcome: supported
  summary: GO0070115 and SL0360 exactly identify the region between two envelope bilayers.
    UniProt supplies plastid-intermembrane-space parent; GO and UniProt support chromatophore
    containment. Stroma and thylakoid lumen remain distinct.
  target_ids:
  - GO:0070115
  evidence_ids:
  - micro-record-organellar_chromatophore_intermembrane_space
  - micro-go
  - micro-SL0360
  - micro-go-0070115-isa
  - micro-SL0351
- assessment_id: micro-organellar_chromatophore_intermembrane_space-composition
  area: grounding
  topic: Material constituent distinct from complete anatomical identity
  outcome: supported
  summary: Residual wall is PEPTIDOGLYCAN/CONSTITUENT, REVIEWED_LABEL_ONLY with explicit
    rationale and no guessed chemical or whole-space CURIE. Source places residual
    peptidoglycan between membranes; exact layer chemistry remains unasserted.
  target_ids:
  - GO:0070115
  evidence_ids:
  - micro-record-organellar_chromatophore_intermembrane_space
  - micro-component-policy
  - micro-SL0360
  - micro-SL0351
  - micro-go
- assessment_id: micro-organellar_chromatophore_intermembrane_space-necessity
  area: evidence
  topic: Constitutive material versus experimental formation necessity
  outcome: unknown
  summary: 'UNKNOWN essentiality is retained for the residual wall: placement does
    not establish whether the intermembrane space forms without it.'
  target_ids:
  - GO:0070115
  evidence_ids:
  - micro-record-organellar_chromatophore_intermembrane_space
  - micro-component-policy
  - micro-go
  - micro-SL0360
  - micro-nowack2012-body
- assessment_id: micro-organellar_chromatophore_intermembrane_space-graph
  area: graph
  topic: Every edge, node and scope
  outcome: supported
  summary: 'Three NONMECHANISTIC edges: outer/inner membranes delimit the space and
    residual peptidoglycan resides there. SL0351 supports the layer placement, SL0359/0360
    and GO0070115 support boundaries. Component_ref points to the labeled wall material,
    not to the entire compartment as chemistry.'
  target_ids:
  - GO:0070115
  evidence_ids:
  - micro-record-organellar_chromatophore_intermembrane_space
  - micro-graph-policy
  - micro-go
  - micro-SL0360
  - micro-SL0351
  - micro-SL0359
- assessment_id: micro-organellar_chromatophore_intermembrane_space-taxon
  area: scope
  topic: Verified genus and qualitative variable occurrence
  outcome: supported
  summary: Paulinella39716 genus is correct. Explicit VARIABLE avoids claiming every
    species has chromatophores; secondary Gabr S2 distinguishes photosynthetic and
    heterotrophic lineages. Primary Nowack culture is CCAC0185/subisolateM0880/a,
    not a genus-wide sample. No frequency estimate or experimental strain substitution.
  target_ids:
  - GO:0070115
  evidence_ids:
  - micro-record-organellar_chromatophore_intermembrane_space
  - micro-tax39716
  - micro-SL0360
  - micro-gabr2020-canonical
  - micro-nowack2012-body
- assessment_id: micro-organellar_chromatophore_intermembrane_space-adapter
  area: evidence
  topic: Whole-record structured-source applicability
  outcome: not_applicable
  summary: Full target asserts only physical boundaries and residual-wall placement;
    positively withholds import/remodeling/protein inventories. SL0351 background
    description of the parent photosynthetic organelle does not convert this compartment-topology
    record into a pathway assertion.
  target_ids:
  - GO:0070115
  evidence_ids:
  - micro-record-organellar_chromatophore_intermembrane_space
  - micro-prior-organellar_chromatophore_intermembrane_space
  - micro-policy
  - micro-catalogue
  - micro-historical-runner
- assessment_id: micro-organellar_chromatophore_intermembrane_space-sources
  area: evidence
  topic: Exact authorities and bounded primary/secondary context
  outcome: supported
  summary: All maintained citations are GO/UniProt-location authorities for anatomical
    identity/topology. Current primary Nowack body reread is only the declared sections/captions,
    with actual earlier retrieval time; Gabr fresh S2 body is secondary context. No
    source pixels, unlisted sections, molecular assembly assay or compulsory protein
    completeness claimed.
  target_ids:
  - GO:0070115
  evidence_ids:
  - micro-record-organellar_chromatophore_intermembrane_space
  - micro-go
  - micro-SL0360
  - micro-SL0351
  - micro-nowack2012-body
  - micro-nowack2012-meta
  - micro-gabr2020-canonical
  - micro-gabr2020-meta
- assessment_id: micro-organellar_chromatophore_intermembrane_space-native
  area: schema
  topic: Original hashes, native validation/render and current protein coverage
  outcome: supported
  summary: All68 old input entries verify at retained source, all4 old pairs validate/render
    exactly and target hash remains unchanged. Current verify/causal commands exit0
    with zero examples and zero typed protein nodes; not evidence of molecular completeness.
  target_ids:
  - GO:0070115
  evidence_ids:
  - micro-prior-organellar_chromatophore_intermembrane_space
  - micro-original-inputs
  - micro-original-pairs
  - micro-native-organellar_chromatophore_intermembrane_space-verify
  - micro-native-organellar_chromatophore_intermembrane_space-causal
- assessment_id: micro-organellar_chromatophore_intermembrane_space-history
  area: provenance
  topic: Historical rationale and scientific status
  outcome: supported
  summary: Full record history/discussions retained; PROPOSED status unchanged. Label-only
    material grounding TODOs remain bounded optional identity questions; no empty-slot
    defect or whole-issue resolution inferred. No historical closed issue is terminally
    disposed by this review.
  target_ids:
  - GO:0070115
  evidence_ids:
  - micro-record-organellar_chromatophore_intermembrane_space
  - micro-prior-organellar_chromatophore_intermembrane_space
  - micro-policy
  - micro-component-policy
- assessment_id: micro-organellar_chromatophore_intermembrane_space-coverage
  area: completeness
  topic: Complete record, absent optional claim surfaces and verdict
  outcome: supported
  summary: 'Entire current record read: no images, physical-measurement objects, individual
    protein accessions, gene symbols, complex-composition inventory or verbatim quotations
    require extra checks. No supported scientific or review-bundle defect observed.
    Qualified pass retains chemical, assembly, prevalence and source-access limits;
    no inherited findings exist.'
  target_ids:
  - GO:0070115
  evidence_ids:
  - micro-record-organellar_chromatophore_intermembrane_space
  - micro-prior-organellar_chromatophore_intermembrane_space
  - micro-policy
  - micro-original-pairs
- assessment_id: micro-organellar_chromatophore_membrane-identity
  area: identity
  topic: Exact identity, synonyms, subtype and parthood
  outcome: supported
  summary: GO0070112 and SL0352 exactly identify generic membrane localization. GO
    definition says surrounding bilayers but its own explicit is_a children and SL0352
    include thylakoid membrane in the fallback class; this is not a new unsupported
    biological generalization. GO0030659 parent and chromatophore parthood verified.
  target_ids:
  - GO:0070112
  evidence_ids:
  - micro-record-organellar_chromatophore_membrane
  - micro-go
  - micro-SL0352
  - micro-go-0070112-isa
  - micro-SL0351
- assessment_id: micro-organellar_chromatophore_membrane-composition
  area: grounding
  topic: Material constituent distinct from complete anatomical identity
  outcome: supported
  summary: Single LIPID/CONSTITUENT is the collective bilayer material, REVIEWED_LABEL_ONLY
    with notes and no whole-membrane GO chemical grounding. Anatomical GO identities
    remain on the record/structure nodes. No precise lipid complement is invented.
  target_ids:
  - GO:0070112
  evidence_ids:
  - micro-record-organellar_chromatophore_membrane
  - micro-component-policy
  - micro-SL0352
  - micro-SL0351
  - micro-go
- assessment_id: micro-organellar_chromatophore_membrane-necessity
  area: evidence
  topic: Constitutive material versus experimental formation necessity
  outcome: unknown
  summary: ESSENTIAL is supported only for the defining collective bilayer, not an
    individual lipid species or protein. No particular molecular formation requirement
    is asserted or established by these sources.
  target_ids:
  - GO:0070112
  evidence_ids:
  - micro-record-organellar_chromatophore_membrane
  - micro-component-policy
  - micro-go
  - micro-SL0352
  - micro-nowack2012-body
- assessment_id: micro-organellar_chromatophore_membrane-graph
  area: graph
  topic: Every edge, node and scope
  outcome: supported
  summary: 'Four NONMECHANISTIC edges: generic membrane part_of chromatophore, with
    inner, outer and thylakoid membranes as is_a subclasses. Exact GO typed children
    and SL0352 support the scope; no unknown protein localization is assigned to a
    specific membrane.'
  target_ids:
  - GO:0070112
  evidence_ids:
  - micro-record-organellar_chromatophore_membrane
  - micro-graph-policy
  - micro-go
  - micro-SL0352
  - micro-SL0351
- assessment_id: micro-organellar_chromatophore_membrane-taxon
  area: scope
  topic: Verified genus and qualitative variable occurrence
  outcome: supported
  summary: Paulinella39716 genus is correct. Explicit VARIABLE avoids claiming every
    species has chromatophores; secondary Gabr S2 distinguishes photosynthetic and
    heterotrophic lineages. Primary Nowack culture is CCAC0185/subisolateM0880/a,
    not a genus-wide sample. No frequency estimate or experimental strain substitution.
  target_ids:
  - GO:0070112
  evidence_ids:
  - micro-record-organellar_chromatophore_membrane
  - micro-tax39716
  - micro-SL0352
  - micro-gabr2020-canonical
  - micro-nowack2012-body
- assessment_id: micro-organellar_chromatophore_membrane-adapter
  area: evidence
  topic: Whole-record structured-source applicability
  outcome: not_applicable
  summary: Full target asserts material anatomy and localization scope, with no named
    protein/regulator/pathway/stress-response claim. Inner/outer explicitly withhold
    import and photosynthetic machinery; generic fallback scope is not an asserted
    protein inventory. The original exclusion is genuine despite its generic expression-only
    explanation.
  target_ids:
  - GO:0070112
  evidence_ids:
  - micro-record-organellar_chromatophore_membrane
  - micro-prior-organellar_chromatophore_membrane
  - micro-policy
  - micro-catalogue
  - micro-historical-runner
- assessment_id: micro-organellar_chromatophore_membrane-sources
  area: evidence
  topic: Exact authorities and bounded primary/secondary context
  outcome: supported
  summary: All maintained citations are GO/UniProt-location authorities for anatomical
    identity/topology. Current primary Nowack body reread is only the declared sections/captions,
    with actual earlier retrieval time; Gabr fresh S2 body is secondary context. No
    source pixels, unlisted sections, molecular assembly assay or compulsory protein
    completeness claimed.
  target_ids:
  - GO:0070112
  evidence_ids:
  - micro-record-organellar_chromatophore_membrane
  - micro-go
  - micro-SL0352
  - micro-SL0351
  - micro-nowack2012-body
  - micro-nowack2012-meta
  - micro-gabr2020-canonical
  - micro-gabr2020-meta
- assessment_id: micro-organellar_chromatophore_membrane-native
  area: schema
  topic: Original hashes, native validation/render and current protein coverage
  outcome: supported
  summary: All68 old input entries verify at retained source, all4 old pairs validate/render
    exactly and target hash remains unchanged. Current verify/causal commands exit0
    with zero examples and zero typed protein nodes; not evidence of molecular completeness.
  target_ids:
  - GO:0070112
  evidence_ids:
  - micro-prior-organellar_chromatophore_membrane
  - micro-original-inputs
  - micro-original-pairs
  - micro-native-organellar_chromatophore_membrane-verify
  - micro-native-organellar_chromatophore_membrane-causal
- assessment_id: micro-organellar_chromatophore_membrane-history
  area: provenance
  topic: Historical rationale and scientific status
  outcome: supported
  summary: Full record history/discussions retained; PROPOSED status unchanged. Label-only
    material grounding TODOs remain bounded optional identity questions; no empty-slot
    defect or whole-issue resolution inferred. Generic scope resolution remains separate
    from open material grounding.
  target_ids:
  - GO:0070112
  evidence_ids:
  - micro-record-organellar_chromatophore_membrane
  - micro-prior-organellar_chromatophore_membrane
  - micro-policy
  - micro-component-policy
- assessment_id: micro-organellar_chromatophore_membrane-coverage
  area: completeness
  topic: Complete record, absent optional claim surfaces and verdict
  outcome: supported
  summary: 'Entire current record read: no images, physical-measurement objects, individual
    protein accessions, gene symbols, complex-composition inventory or verbatim quotations
    require extra checks. No supported scientific or review-bundle defect observed.
    Qualified pass retains chemical, assembly, prevalence and source-access limits;
    no inherited findings exist.'
  target_ids:
  - GO:0070112
  evidence_ids:
  - micro-record-organellar_chromatophore_membrane
  - micro-prior-organellar_chromatophore_membrane
  - micro-policy
  - micro-original-pairs
- assessment_id: micro-organellar_chromatophore_outer_membrane-identity
  area: identity
  topic: Exact identity, synonyms, subtype and parthood
  outcome: supported
  summary: GO0070114 and SL0361 exactly identify cytoplasm-facing outer bilayer. GO
    chromatophore-membrane subclass and UniProt plastid-outer-membrane parent/parthood
    are distinct verified relationships.
  target_ids:
  - GO:0070114
  evidence_ids:
  - micro-record-organellar_chromatophore_outer_membrane
  - micro-go
  - micro-SL0361
  - micro-go-0070114-isa
  - micro-SL0351
- assessment_id: micro-organellar_chromatophore_outer_membrane-composition
  area: grounding
  topic: Material constituent distinct from complete anatomical identity
  outcome: supported
  summary: Single LIPID/CONSTITUENT is the collective bilayer material, REVIEWED_LABEL_ONLY
    with notes and no whole-membrane GO chemical grounding. Anatomical GO identities
    remain on the record/structure nodes. No precise lipid complement is invented.
  target_ids:
  - GO:0070114
  evidence_ids:
  - micro-record-organellar_chromatophore_outer_membrane
  - micro-component-policy
  - micro-SL0361
  - micro-SL0351
  - micro-go
- assessment_id: micro-organellar_chromatophore_outer_membrane-necessity
  area: evidence
  topic: Constitutive material versus experimental formation necessity
  outcome: unknown
  summary: ESSENTIAL is supported only for the defining collective bilayer, not an
    individual lipid species or protein. No particular molecular formation requirement
    is asserted or established by these sources.
  target_ids:
  - GO:0070114
  evidence_ids:
  - micro-record-organellar_chromatophore_outer_membrane
  - micro-component-policy
  - micro-go
  - micro-SL0361
  - micro-nowack2012-body
- assessment_id: micro-organellar_chromatophore_outer_membrane-graph
  area: graph
  topic: Every edge, node and scope
  outcome: supported
  summary: One NONMECHANISTIC bounds edge locates the outer host-cytoplasm-facing
    bilayer as chromatophore outer boundary. It does not equate the inner or thylakoid
    membrane with the exterior boundary or posit transport machinery.
  target_ids:
  - GO:0070114
  evidence_ids:
  - micro-record-organellar_chromatophore_outer_membrane
  - micro-graph-policy
  - micro-go
  - micro-SL0361
  - micro-SL0351
- assessment_id: micro-organellar_chromatophore_outer_membrane-taxon
  area: scope
  topic: Verified genus and qualitative variable occurrence
  outcome: supported
  summary: Paulinella39716 genus is correct. Explicit VARIABLE avoids claiming every
    species has chromatophores; secondary Gabr S2 distinguishes photosynthetic and
    heterotrophic lineages. Primary Nowack culture is CCAC0185/subisolateM0880/a,
    not a genus-wide sample. No frequency estimate or experimental strain substitution.
  target_ids:
  - GO:0070114
  evidence_ids:
  - micro-record-organellar_chromatophore_outer_membrane
  - micro-tax39716
  - micro-SL0361
  - micro-gabr2020-canonical
  - micro-nowack2012-body
- assessment_id: micro-organellar_chromatophore_outer_membrane-adapter
  area: evidence
  topic: Whole-record structured-source applicability
  outcome: not_applicable
  summary: Full target asserts material anatomy and localization scope, with no named
    protein/regulator/pathway/stress-response claim. Inner/outer explicitly withhold
    import and photosynthetic machinery; generic fallback scope is not an asserted
    protein inventory. The original exclusion is genuine despite its generic expression-only
    explanation.
  target_ids:
  - GO:0070114
  evidence_ids:
  - micro-record-organellar_chromatophore_outer_membrane
  - micro-prior-organellar_chromatophore_outer_membrane
  - micro-policy
  - micro-catalogue
  - micro-historical-runner
- assessment_id: micro-organellar_chromatophore_outer_membrane-sources
  area: evidence
  topic: Exact authorities and bounded primary/secondary context
  outcome: supported
  summary: All maintained citations are GO/UniProt-location authorities for anatomical
    identity/topology. Current primary Nowack body reread is only the declared sections/captions,
    with actual earlier retrieval time; Gabr fresh S2 body is secondary context. No
    source pixels, unlisted sections, molecular assembly assay or compulsory protein
    completeness claimed.
  target_ids:
  - GO:0070114
  evidence_ids:
  - micro-record-organellar_chromatophore_outer_membrane
  - micro-go
  - micro-SL0361
  - micro-SL0351
  - micro-nowack2012-body
  - micro-nowack2012-meta
  - micro-gabr2020-canonical
  - micro-gabr2020-meta
- assessment_id: micro-organellar_chromatophore_outer_membrane-native
  area: schema
  topic: Original hashes, native validation/render and current protein coverage
  outcome: supported
  summary: All68 old input entries verify at retained source, all4 old pairs validate/render
    exactly and target hash remains unchanged. Current verify/causal commands exit0
    with zero examples and zero typed protein nodes; not evidence of molecular completeness.
  target_ids:
  - GO:0070114
  evidence_ids:
  - micro-prior-organellar_chromatophore_outer_membrane
  - micro-original-inputs
  - micro-original-pairs
  - micro-native-organellar_chromatophore_outer_membrane-verify
  - micro-native-organellar_chromatophore_outer_membrane-causal
- assessment_id: micro-organellar_chromatophore_outer_membrane-history
  area: provenance
  topic: Historical rationale and scientific status
  outcome: supported
  summary: Full record history/discussions retained; PROPOSED status unchanged. Label-only
    material grounding TODOs remain bounded optional identity questions; no empty-slot
    defect or whole-issue resolution inferred. No historical closed issue is terminally
    disposed by this review.
  target_ids:
  - GO:0070114
  evidence_ids:
  - micro-record-organellar_chromatophore_outer_membrane
  - micro-prior-organellar_chromatophore_outer_membrane
  - micro-policy
  - micro-component-policy
- assessment_id: micro-organellar_chromatophore_outer_membrane-coverage
  area: completeness
  topic: Complete record, absent optional claim surfaces and verdict
  outcome: supported
  summary: 'Entire current record read: no images, physical-measurement objects, individual
    protein accessions, gene symbols, complex-composition inventory or verbatim quotations
    require extra checks. No supported scientific or review-bundle defect observed.
    Qualified pass retains chemical, assembly, prevalence and source-access limits;
    no inherited findings exist.'
  target_ids:
  - GO:0070114
  evidence_ids:
  - micro-record-organellar_chromatophore_outer_membrane
  - micro-prior-organellar_chromatophore_outer_membrane
  - micro-policy
  - micro-original-pairs
- assessment_id: current-input-comparison
  area: provenance
  topic: Complete frozen-input comparison and bounded refresh
  outcome: supported
  summary: 0 of ten original target hashes differ from current main. The changed content
    is substantively reassessed in the target-specific assessments; original observations
    remain historical and unchanged. All current target and used context bytes are
    frozen.
  target_ids:
  - GO:0070113
  - GO:0070115
  - GO:0070112
  - GO:0070114
  - GO:0070116
  - GO:0070117
  - GO:0070118
  - GO:0044310
  - cellstructuremech:parasitophorous_vacuole
  - cellstructuremech:parasitophorous_vacuole_lumen
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
- finding_id: septin-organellar_chromatophore_thylakoid-F1
  issue_key: chromatophore-thylakoid-whole-membrane-lipid
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Separate whole membrane identity from lipid material
  description: The LIPID component is labelled and grounded to the entire organellar
    chromatophore thylakoid membrane GO0070118. The graph structural node carries
    a component_ref to this row. GO identifies a whole anatomical membrane, not a
    lipid entity.
  target_ids:
  - GO:0070116
  field_paths:
  - components[0].component_type
  - components[0].grounding
  - causal_graphs[0].nodes[1].component_ref
  evidence_ids:
  - septin-record-organellar_chromatophore_thylakoid
  - septin-original-organellar_chromatophore_thylakoid
  - septin-go
  - septin-curation-policy
  - septin-schema-policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/organellar_chromatophore_thylakoid.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:components and narrow evidence placement
  native_severity: major
  normalization_reason: Major whole-structure versus molecular-type mismatch.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T030053Z-organellar-chromatophore-thylakoid-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2756
- finding_id: septin-organellar_chromatophore_thylakoid-F2
  issue_key: chromatophore-thylakoid-go-light-complex-attribution
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Use the source that establishes the light-complex claim
  description: The component and photosynthesis edge say GO0070118 defines a membrane
    carrying light-reaction complexes. Its native definition identifies only the bilayer
    compartment. SL0354 already cited by the function, and the independently inspected
    Nowack2012 primary study, support the biological statement.
  target_ids:
  - GO:0070116
  field_paths:
  - components[0].evidence[0].notes
  - causal_graphs[0].edges[1].evidence[0].notes
  evidence_ids:
  - septin-record-organellar_chromatophore_thylakoid
  - septin-original-organellar_chromatophore_thylakoid
  - septin-go
  - septin-SL0354
  - septin-SL0356
  - septin-nowack2012-prefixed
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/organellar_chromatophore_thylakoid.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:components and narrow evidence placement
  native_severity: minor
  normalization_reason: Minor bounded source-attribution error; photosynthetic biology
    itself has positive support.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T030053Z-organellar-chromatophore-thylakoid-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2757
- finding_id: plaque-t7-F1
  issue_key: osmiophilic-body-unreconciled-pfg377-egress-counterevidence
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Reconcile the emergence pathway with the cited2016 counterevidence
  description: The record presents reduced emergence as a general consequence of Pfg377-dependent
    body depletion and as the route to poor mosquito infection. Its own cited2016
    study generated new pfg377 knockouts with depleted bodies, observed normal measured
    egress, and retained severe mosquito infection defects. That study explicitly
    reports failure to reproduce the earlier egress phenotype. The record therefore
    needs source- and condition-specific qualification rather than the current unqualified
    functional pathway. This does not refute Pfg377 localization, normal-body biogenesis,
    mosquito infection support or the explicitly postulated GO definition.
  target_ids:
  - GO:0044310
  field_paths:
  - functions[0]
  - causal_graphs[0].title
  - causal_graphs[0].description
  - causal_graphs[0].edges[3]
  - causal_graphs[0].edges[4].evidence
  - discussions[1].rationale
  evidence_ids:
  - plaque-current-7
  - plaque-original-7
  - plaque-dekoning2008-meta
  - plaque-suarez2016-pmc
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/osmiophilic_body.yaml
    role: maintained scientific record
  rule_id: Source-specific claim support and biological scope
  native_severity: major
  normalization_reason: The contradiction changes the supported functional explanation
    and directed phenotype pathway; it is materially more than missing citation metadata.
    Exact organelle identity remains correct, so major rather than blocker.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T030055Z-osmiophilic-body-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2758
- finding_id: plaque-t8-F1
  issue_key: parasitophorous-vacuole-bioid-canonical-species-misattribution
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Correct the species attached to the cited BioID canonical example
  description: canonical_examples[1] assigns the Schnider2018 BioID survey to Plasmodium
    falciparum5833. The cited primary paper performed that survey in P. berghei blood
    stages and states the ANKA mCherryHsp70 experimental background. Its comparisons
    with P. falciparum orthologs and previous studies do not support the maintained
    claim that this survey used P. falciparum.
  target_ids:
  - cellstructuremech:parasitophorous_vacuole
  field_paths:
  - canonical_examples[1].taxon_id
  - canonical_examples[1].taxon_label
  - canonical_examples[1].note
  - canonical_examples[1].reference
  evidence_ids:
  - plaque-current-8
  - plaque-original-8
  - plaque-tax5833
  - plaque-tax5821
  - plaque-schnider2018-meta
  - plaque-schnider2018-body
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/parasitophorous_vacuole.yaml
    role: maintained scientific record
  rule_id: Source-specific claim support and biological scope
  native_severity: major
  normalization_reason: A concrete primary experiment is attached to the wrong taxon,
    materially corrupting the canonical species/evidence link. The broad PV identity
    and occurrence in both species remain valid, so major rather than blocker.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T030057Z-parasitophorous-vacuole-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2759
actions:
- action_id: septin-organellar_chromatophore_thylakoid-A1
  finding_ids:
  - septin-organellar_chromatophore_thylakoid-F1
  target_ids:
  - GO:0070116
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/organellar_chromatophore_thylakoid.yaml
    role: maintained scientific record
  description: Preserve supported membrane topology. Retain a whole structural constituent
    with an appropriate type, or describe supported lipid material separately with
    exact chemical grounding or justified reviewed-label-only status; align the component_ref
    accordingly.
  acceptance_checks:
  - Verify each amended type and source note against the exact native definition or
    primary passage.
  - After separately authorized curation, run focused schema, strict, graph and label
    validation.
- action_id: septin-organellar_chromatophore_thylakoid-A2
  finding_ids:
  - septin-organellar_chromatophore_thylakoid-F2
  target_ids:
  - GO:0070116
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/organellar_chromatophore_thylakoid.yaml
    role: maintained scientific record
  description: Restrict the GO note to its membrane definition and attach the light-complex
    claim to SL0354 and/or the relevant primary thylakoid photosystem evidence.
  acceptance_checks:
  - Verify each amended type and source note against the exact native definition or
    primary passage.
  - After separately authorized curation, run focused schema, strict, graph and label
    validation.
- action_id: plaque-t7-A1
  finding_ids:
  - plaque-t7-F1
  target_ids:
  - GO:0044310
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/osmiophilic_body.yaml
    role: maintained scientific record
  description: In separately authorized curation, explicitly distinguish the2008 emergence
    result from the2016 non-reproduction in defined3D7 knockout clones. Qualify or
    remove the general body-abundance-to-emergence assertion and its explanation of
    the oocyst defect. Preserve supported Pfg377/body biogenesis and mosquito infection
    association, and retain uncertainty about the post-egress causal step without
    inventing a replacement mechanism.
  acceptance_checks:
  - Both cited studies and their differing assay/context results are represented honestly.
  - No unqualified graph/function assertion treats poor egress as the established
    explanation of the Pfg377-associated mosquito defect.
  - Correct GO identity, membrane topology, Pfg377 membership and qualified transmission
    association remain intact.
  - Native schema, strict, identifier, protein, graph and history gates pass after
    authorized curation.
- action_id: plaque-t8-A1
  finding_ids:
  - plaque-t8-F1
  target_ids:
  - cellstructuremech:parasitophorous_vacuole
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/parasitophorous_vacuole.yaml
    role: maintained scientific record
  description: In separately authorized curation, align this canonical example with
    the actual P. berghei study, using verified taxon5821 and the appropriate experimental
    background, or replace the citation and note with independently inspected P. falciparum-specific
    experimental evidence. Preserve the broader apicomplexan identity and valid Toxoplasma
    example.
  acceptance_checks:
  - The taxon, note and cited experiment identify the same parasite species.
  - P. berghei ANKA study data are not relabeled as P. falciparum data; orthology
    is distinguished from experimental provenance.
  - PV identity, PVM/lumen boundary links and valid niche claims remain unchanged.
  - Native schema, strict, taxon/identifier and history checks pass after authorized
    curation.
limitations:
- 'Chromatophore thylakoid and two compartments independent subreview: Read-only source
  review of three unchanged thylakoid records at the exact source head. Root owns
  issue dedup/publication and repository/global/CI/queue actions. No future saved-head
  or CI attestation is made here.'
- 'Chromatophore thylakoid and two compartments independent subreview: Nine fresh
  official-source requests are distinguished from three public snapshots reused with
  verified hashes and original access times: species taxonomy, Crossref secondary
  metadata/abstract and genuine Nowack2012 PMC body. No false fresh-access or full-paper
  claim is made.'
- 'Chromatophore thylakoid and two compartments independent subreview: Nowack2012
  reinspection is bounded to the first two Results sections, Fig1/2 text captions
  and Methods Strain and Growth Conditions. It establishes selected PsaE localization
  and PSI subunit association in CCAC0185 M0880/a under recorded culture conditions,
  not the full photosystem inventory or experimental requirements for thylakoid formation.
  No source pixels, raw data or supplements were examined.'
- 'Chromatophore thylakoid and two compartments independent subreview: Nowack2014
  is exact metadata and complete deposited secondary abstract only. COMMON species
  presence is qualitative, not numerically measured; genus VARIABLE notes do not assert
  universal chromatophore occurrence. Original reviewers other broader literature
  access remains historical, not adopted as current full-body evidence.'
- 'Chromatophore thylakoid and two compartments independent subreview: GO and UniProt
  hierarchy/text attribution are kept distinct: plastid-specific lumen/membrane parents
  have explicit SL isA support even where current GO is_a ancestry does not contain
  them. Generic GO thylakoid organelle terminology and native category wording differ;
  no unsupported enum-only finding is manufactured.'
- 'Chromatophore thylakoid and two compartments independent subreview: The membrane
  record intentionally uses REVIEWED_LABEL_ONLY collective lipid material; ESSENTIAL
  denotes constitutive bilayer material, not individual lipid/protein necessity. Optional
  exact chemistry, stoichiometry and protein inventory remain unestablished without
  forcing a CURIE. The whole-thylakoid LIPID-to-whole-membrane grounding is a distinct
  confirmed inherited error.'
- 'Chromatophore thylakoid and two compartments independent subreview: All six native
  protein commands pass on independently confirmed empty represented scopes: zero
  protein examples, typed molecular nodes and UniProtKB graph xrefs. This is not universal
  molecular or scientific validation.'
- 'Chromatophore thylakoid and two compartments independent subreview: Two actual
  positive light-reaction narratives trigger corrected structured-source applicability.
  Fresh catalogue has no Paulinella host match; unrelated cyanobacteria are not proxies.
  The lumen genuinely excludes molecular mechanisms. Historical00:49Z runner failure
  is never represented as a fresh invocation or biological noncoverage test.'
- 'Chromatophore thylakoid and two compartments independent subreview: All27 actually
  used repository inputs were frozen before use:17 common rules/schema/scripts,3 targets,6
  original artifacts and1 whole-chromatophore boundary neighbor. No new closure or
  whole-record/neighbor/group issue disposition is inferred.'
- 'Osmiophilic body and parasitophorous vacuole boundary independent subreview: All3
  targets unchanged. Two exact inheritedmajor findings/actions retained with original
  keys/severities and repository/review/finding predecessors; no new scientific finding.
  Lumen remains qualified.'
- 'Osmiophilic body and parasitophorous vacuole boundary independent subreview: Original3
  pairs natively validate and render byte-for-byte;15 historical frozen inputs each
  match. All actual used current local inputs are frozen. No scientific promotion,
  record/original edit or terminal neighbor/group/history disposition.'
- 'Osmiophilic body and parasitophorous vacuole boundary independent subreview: Alano
  exact DOI query returned0 but exact PMID8719156 verified DOI/title/year/authors
  and complete primary abstract. Publisher403; full body unread. deKoning complete
  primary abstract and Glasgow metadata read; Wiley403 and repository explicitly no
  full text.2008 phenotype remains genuine historical evidence.'
- 'Osmiophilic body and parasitophorous vacuole boundary independent subreview: Suarez
  genuine PMC HTML Methods5–9/Results19 withFig1caption/completeDiscussion24 read.
  S3JATS404 is not body. Parent-section extra output is not claimed as complete analysis
  of remaining Methods/Results. No figure pixels, supplemental files/raw proteomics
  or independent statistical reanalysis.15-minute assay does not exclude every early
  kinetic/strain-dependent effect.'
- 'Osmiophilic body and parasitophorous vacuole boundary independent subreview: Schnider
  genuine JATS Results1.1/1.2, completeDiscussion2, Methods3.6/3.9 plus embedded captions
  read. Actual organism is P.berghei ANKA mCherryHsp70; P.falciparum comparisons remain
  separate.61proximity candidates do not equal61validated PVM constituents. No figure
  pixels, supplement files or raw data inspected.'
- 'Osmiophilic body and parasitophorous vacuole boundary independent subreview: Lingelbach1998/Clough2017
  are complete secondary abstracts only. Publisher403/200redirect shell are not full
  review bodies or newly inspected primary mechanisms. No unread-text refutation or
  universal nutrient-permeability claim.'
- 'Osmiophilic body and parasitophorous vacuole boundary independent subreview: A0A059WIJ2
  is an unreviewed193-aa G1 fragment with predicted protein existence, not full-length
  experimental3D7Pfg377. Native1COVERED node is identifier representation, not source
  conflict reconciliation. ExactInterPro204 is inconclusive; bounded reviewed-gene0results
  and PANTHERcrossreferences do not establish exhaustive family absence or exact grounding.'
- 'Osmiophilic body and parasitophorous vacuole boundary independent subreview: PV
  and lumen native commands pass on0examples/0typednodes. Optional inventory absence
  does not negate positive narrative molecular claims or require new components. No
  image assets or image modality/licence claims occur in assigned records.'
- 'Osmiophilic body and parasitophorous vacuole boundary independent subreview: Fresh
  official catalogue from same-PR micro reviewer independently reread completely at
  original18:41Z fetch time; no matched Plasmodium/Toxoplasma/apicomplexan host. Osmiophilic/PV
  trigger coverage from actual molecular assertions; lumen genuine morphology/topology
  exclusion. No unrelated strain proxy or inferred negative biology. Historical00:49Z
  runner remains unavailable, no fresh invocation.'
- 'Osmiophilic body and parasitophorous vacuole boundary independent subreview: Root
  owns global gates, issue dedup/publication, immutable successor and finalCI/queue.
  This report binds independent science and scratch native preflight only. Neighbor
  PVM is used solely for exact boundary context; its record and any separate findings
  are outside this assigned review.'
- 'Four chromatophore membrane-boundary independent subreview: Four complete unchanged
  boundary records independently reviewed; no scientific findings, no inherited findings/actions
  and no bundle defects in this slice. Their original clean observations remain immutable
  historical evidence. This scratch source report is for the explicit mixed-cohort
  successor; it is not a separate clean review bundle saved to the repository.'
- 'Four chromatophore membrane-boundary independent subreview: GO and UniProt location
  classifications differ for some broader plastid parent relationships. Actual UniProt
  immediate isA/partOf entries support those relationships; no absent GO direct edge
  or part_of relation is inferred from an is_a-only ancestor list. Generic GO membrane
  prose is interpreted alongside its explicit inner/outer/thylakoid children and SL0352
  fallback definition.'
- 'Four chromatophore membrane-boundary independent subreview: All maintained citations
  in these four records are anatomy/localization authorities. Nowack2012 genuine primary
  body was retained from18:08:44.263032Z and independently reread at Resultssec2/3
  with Fig1/2 captions and Methodssec14 only. No image pixels, supplementary data,
  lipid chemistry or individual envelope assembly necessity assessed. CCAC0185 is
  a subisolate of M0880/a; no other strain generalized.'
- 'Four chromatophore membrane-boundary independent subreview: Gabr2020 fresh genuine
  canonicalPMC S2/Fig1caption is a secondary review, not primary experimental support.
  Earlier PR2372 metadata/abstract retains its actual retrieval time. Qualitative
  photosynthetic/heterotrophic variation supports VARIABLE, not a current complete
  species inventory or prevalence census.'
- 'Four chromatophore membrane-boundary independent subreview: Current SL0353 resolves
  as stroma and may optionally enrich the label-only node. This does not establish
  that a dated historical inaccessible-accession note was false, require history rewriting
  or settle an unexamined broader issue.'
- 'Four chromatophore membrane-boundary independent subreview: All four physical/material
  records are genuine structured-source exclusions; empty protein inventories are
  not the deciding criterion. Fresh official catalogue has no matching Paulinella
  host. No unmatched bacterial proxy or downstream module query performed. Historical00:49Z
  adapter PermissionError remains separately dated and is not a new execution.'
- 'Four chromatophore membrane-boundary independent subreview: Current native eight
  protein commands pass with zero examples and zero GENE_OR_PROTEIN nodes. Their generic
  verify-success text does not establish complete protein/family coverage. All68 original
  hashes are provenance checks; unfrozen historical neighboring records were not newly
  scientifically assessed.'
- 'Four chromatophore membrane-boundary independent subreview: No records, immutable
  review pairs, history, generated files, Git or GitHub state changed. Root owns cohort
  QC/CI/publication/queue checks; no future CI or merge is certified by this source
  report.'
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
  and pushed without force. All ten target hashes match their original frozen inputs;
  no stale-refresh issue is invented.
- This explicit issue-bearing ten-record cohort follows native persistence policy.
  Inherited scientific findings retain stable keys and exact predecessor repository/review/finding
  identities; any new finding has no invented predecessor.
- 'Issue2755 tracks four unsupported expression-only applicability exclusions: thylakoid,
  thylakoid membrane, osmiophilic body and whole parasitophorous vacuole. The PV trigger
  is its positive BioID/PVM-associated protein assertion, not an invented nutrient
  mechanism. All ten originals contained explicit exclusions; none was missing.'
- 'Six records have genuine physical/material-topology scope: the four chromatophore
  envelope boundary records, thylakoid lumen and PV lumen. Molecular import, photosynthetic,
  lumenal-protein or transport machinery is explicitly excluded or withheld. A broader
  source description alone does not imply a compartment-specific mechanism.'
- Source commit bdd5beb85634420b1d99c91138a9121631087f89 is retained by tag review-base/pr2373-current-record-followup-20261103.
- CLAUDE.md aliases AGENTS.md; canonical regular AGENTS.md bytes are frozen. Every
  used local context input is frozen before its assessment.
- Fresh and reused source snapshots retain actual access times and inspection tiers.
  Native identifier identity does not independently establish structure membership,
  experimental intervention scope or assembly necessity.
- All twenty native protein commands returned zero. Osmiophilic body has one unreviewed
  A0A059WIJ2 example and one COVERED typed node; the native result is separate from
  the fragment scope and source-specific egress/counterevidence assessment. The other
  nine records have zero examples and zero typed molecular nodes. Optional example
  absence alone is not a scientific defect.
- Current CausalNode schema permits protein families and complexes as GENE_OR_PROTEIN
  nodes. Label-only collective lipid material and explicitly unresolved peptidoglycan
  composition are distinct from erroneously grounding a molecular component to an
  entire membrane structure.
- Related issues2753/2754 concern the whole chromatophore record and do not dispose
  of the present thylakoid-record findings. Native-validator2514 remains open and
  reused; no scientific record or resolver is edited.
- The osmiophilic-body finding concerns present functional/causal assertions contradicted
  by cited counterevidence, not a requirement to erase historical rationale. Separately
  authorized curation must preserve append-only rationale and use appended context
  or current-state notes.
- Final trusted-base review-check, exact-head independent acceptance, final-head CI
  and merge-group CI occur after this immutable observation and are not represented
  as already completed.
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T030049Z-organellar-chromatophore-inner-membrane-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T030050Z-organellar-chromatophore-intermembrane-space-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T030051Z-organellar-chromatophore-membrane-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T030052Z-organellar-chromatophore-outer-membrane-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T030053Z-organellar-chromatophore-thylakoid-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T030054Z-organellar-chromatophore-thylakoid-lumen-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T030055Z-organellar-chromatophore-thylakoid-membrane-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T030055Z-osmiophilic-body-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T030057Z-parasitophorous-vacuole-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T030057Z-parasitophorous-vacuole-lumen-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
links:
- https://github.com/CultureBotAI/CellStructureMech/pull/2373
- https://github.com/CultureBotAI/CellStructureMech/issues/2514
- https://github.com/CultureBotAI/CellStructureMech/issues/2755
- https://github.com/CultureBotAI/CellStructureMech/issues/2756
- https://github.com/CultureBotAI/CellStructureMech/issues/2757
- https://github.com/CultureBotAI/CellStructureMech/issues/2758
- https://github.com/CultureBotAI/CellStructureMech/issues/2759
```
