# PR 2361: current-input review of ten records and adversarial follow-up

- Review: 20261103T112432Z-pr2361-current-record-followup
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-11-03T11:15:33.506892Z
- Finished UTC: 2026-11-03T11:24:32Z
- Reviewer: Codex root synthesis with three independent read-only adversarial reviewers (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Current-input reassessment of all ten records in PR2361. One stale COPI-coated vesicle review is substantively refreshed. Independent source assessments retain three inherited contractile-vacuole scientific findings and correct nine structured-source applicability assessments without editing records.

## Scope And Provenance

Exact ten-record PR cohort reassessed against current main 015960951a1c255e5ed24f5edb25a816d13ec948. Changed inputs are substantively reassessed. Scientific records remain unchanged.

Selection: Complete cohort of ten maintained records reviewed in original PR head f8c275390de4faf5d59d66f73b8abd8a84b31a39.
Coverage: full; 10 reviewed / 10 in the declared population.
Source: working_tree at Git base 7081777bba0daacfa48fc6d826cdfd7138e751b4.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0031164 | data/structures/membrane_organelle/contractile_vacuolar_membrane.yaml | maintained | contractile vacuolar membrane |
| GO:0000331 | data/structures/membrane_organelle/contractile_vacuole.yaml | maintained | contractile vacuole |
| GO:0062159 | data/structures/membrane_organelle/contractile_vacuole_complex.yaml | maintained | contractile vacuole complex |
| cellstructuremech:contractile_vacuole_lumen | data/structures/membrane_organelle/contractile_vacuole_lumen.yaml | maintained | contractile vacuole lumen |
| GO:0031913 | data/structures/membrane_organelle/contractile_vacuole_pore.yaml | maintained | contractile vacuole pore |
| GO:0030137 | data/structures/membrane_organelle/copi_coated_vesicle.yaml | maintained | COPI-coated vesicle |
| cellstructuremech:copi_coated_vesicle_lumen | data/structures/membrane_organelle/copi_coated_vesicle_lumen.yaml | maintained | COPI-coated vesicle lumen |
| GO:0030663 | data/structures/membrane_organelle/copi_coated_vesicle_membrane.yaml | maintained | COPI-coated vesicle membrane |
| GO:0030134 | data/structures/membrane_organelle/copii_coated_er_to_golgi_transport_vesicle.yaml | maintained | COPII-coated ER to Golgi transport vesicle |
| cellstructuremech:copii_coated_vesicle_lumen | data/structures/membrane_organelle/copii_coated_vesicle_lumen.yaml | maintained | COPII-coated vesicle lumen |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full native QC | passed | True | GO:0031164, GO:0000331, GO:0062159, cellstructuremech:contractile_vacuole_lumen, GO:0031913, GO:0030137, cellstructuremech:copi_coated_vesicle_lumen, GO:0030663, GO:0030134, cellstructuremech:copii_coated_vesicle_lumen | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| Native label correspondence | passed | True | GO:0031164, GO:0000331, GO:0062159, cellstructuremech:contractile_vacuole_lumen, GO:0031913, GO:0030137, cellstructuremech:copi_coated_vesicle_lumen, GO:0030663, GO:0030134, cellstructuremech:copii_coated_vesicle_lumen | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| TraitMech references | passed | True | GO:0031164, GO:0000331, GO:0062159, cellstructuremech:contractile_vacuole_lumen, GO:0031913, GO:0030137, cellstructuremech:copi_coated_vesicle_lumen, GO:0030663, GO:0030134, cellstructuremech:copii_coated_vesicle_lumen | Native TraitMech link check passed. |
| Pinned governed files | passed | True | GO:0031164, GO:0000331, GO:0062159, cellstructuremech:contractile_vacuole_lumen, GO:0031913, GO:0030137, cellstructuremech:copi_coated_vesicle_lumen, GO:0030663, GO:0030134, cellstructuremech:copii_coated_vesicle_lumen | Pinned governed files match; native vendored check passed. |
| Native identifier resolver | passed | True | GO:0031164, GO:0000331, GO:0062159, cellstructuremech:contractile_vacuole_lumen, GO:0031913, GO:0030137, cellstructuremech:copi_coated_vesicle_lumen, GO:0030663, GO:0030134, cellstructuremech:copii_coated_vesicle_lumen | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| validate GO:0031164 | passed | True | GO:0031164 | Documented focused command passed. |
| validate-strict GO:0031164 | passed | True | GO:0031164 | Documented focused command passed. |
| validate GO:0000331 | passed | True | GO:0000331 | Documented focused command passed. |
| validate-strict GO:0000331 | passed | True | GO:0000331 | Documented focused command passed. |
| validate GO:0062159 | passed | True | GO:0062159 | Documented focused command passed. |
| validate-strict GO:0062159 | passed | True | GO:0062159 | Documented focused command passed. |
| validate cellstructuremech:contractile_vacuole_lumen | passed | True | cellstructuremech:contractile_vacuole_lumen | Documented focused command passed. |
| validate-strict cellstructuremech:contractile_vacuole_lumen | passed | True | cellstructuremech:contractile_vacuole_lumen | Documented focused command passed. |
| validate GO:0031913 | passed | True | GO:0031913 | Documented focused command passed. |
| validate-strict GO:0031913 | passed | True | GO:0031913 | Documented focused command passed. |
| validate GO:0030137 | passed | True | GO:0030137 | Documented focused command passed. |
| validate-strict GO:0030137 | passed | True | GO:0030137 | Documented focused command passed. |
| validate cellstructuremech:copi_coated_vesicle_lumen | passed | True | cellstructuremech:copi_coated_vesicle_lumen | Documented focused command passed. |
| validate-strict cellstructuremech:copi_coated_vesicle_lumen | passed | True | cellstructuremech:copi_coated_vesicle_lumen | Documented focused command passed. |
| validate GO:0030663 | passed | True | GO:0030663 | Documented focused command passed. |
| validate-strict GO:0030663 | passed | True | GO:0030663 | Documented focused command passed. |
| validate GO:0030134 | passed | True | GO:0030134 | Documented focused command passed. |
| validate-strict GO:0030134 | passed | True | GO:0030134 | Documented focused command passed. |
| validate cellstructuremech:copii_coated_vesicle_lumen | passed | True | cellstructuremech:copii_coated_vesicle_lumen | Documented focused command passed. |
| validate-strict cellstructuremech:copii_coated_vesicle_lumen | passed | True | cellstructuremech:copii_coated_vesicle_lumen | Documented focused command passed. |
| Supplemental bounded PMID authority checks | passed | True | GO:0031164, GO:0000331, GO:0062159, cellstructuremech:contractile_vacuole_lumen, GO:0031913, GO:0030137, cellstructuremech:copi_coated_vesicle_lumen, GO:0030663, GO:0030134, cellstructuremech:copii_coated_vesicle_lumen | 909 PMIDs all OK in bounded native requests; full-command limitations remain separate. |
| Official structured-source applicability and covered-dataset cross-checks | passed | False | GO:0031164, GO:0000331, GO:0062159, cellstructuremech:contractile_vacuole_lumen, GO:0031913, GO:0030137, cellstructuremech:copi_coated_vesicle_lumen, GO:0030663, GO:0030134, cellstructuremech:copii_coated_vesicle_lumen | Nine applicability defects are corrected: four omitted assessments for contractile vacuolar membrane, vacuole, complex and lumen, plus five unsupported expression-only exclusions across COPI vesicle/lumen/membrane and COPII transport vesicle/lumen. Osmotic-response context itself triggers the native policy even without named molecular components. Contractile vacuole pore remains genuinely excluded at topology/coarse-flow scope with unresolved molecular identities. Complete catalogue coverage has no matching relevant yeast, ciliate, algal, Amoeba, Dictyostelium, Trypanosoma or Paramecium dataset. No unrelated organism dataset or downstream module query substitutes for noncoverage. Resource noncoverage is not biological absence; retained historical runner failure is not a fresh invocation. |
| Independent claim-level source review | passed | True | GO:0031164, GO:0000331, GO:0062159, cellstructuremech:contractile_vacuole_lumen, GO:0031913, GO:0030137, cellstructuremech:copi_coated_vesicle_lumen, GO:0030663, GO:0030134, cellstructuremech:copii_coated_vesicle_lumen | Three read-only reviewers covered the complete ten-record cohort, including changed inputs, with explicit scientific findings and source-access limits. Final artifact/head acceptance occurs after saving. |
| Retained historical adapter runner availability | unavailable | False | GO:0031164, GO:0000331, GO:0062159, cellstructuremech:contractile_vacuole_lumen, GO:0030137, cellstructuremech:copi_coated_vesicle_lumen, GO:0030663, GO:0030134, cellstructuremech:copii_coated_vesicle_lumen | Historical 00:49Z invocation unavailable due to OS access restriction. Official catalogue source fallback was inspected separately; no current invocation or successful adapter execution is claimed. The actual historical exit code 1 is retained in the evidence receipt, since the native unavailable-check model has no execution exit-code field. |
| Native contractile vacuolar membrane UniProt verify check | passed | True | GO:0031164 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Missing anchors/examples, empty inventories and zero molecular graph nodes do not validate narrative molecules, localization, mechanism, taxon transfer or assembly necessity. |
| Native contractile vacuolar membrane UniProt causal check | passed | True | GO:0031164 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Missing anchors/examples, empty inventories and zero molecular graph nodes do not validate narrative molecules, localization, mechanism, taxon transfer or assembly necessity. |
| Native contractile vacuole UniProt verify check | passed | True | GO:0000331 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Missing anchors/examples, empty inventories and zero molecular graph nodes do not validate narrative molecules, localization, mechanism, taxon transfer or assembly necessity. |
| Native contractile vacuole UniProt causal check | passed | True | GO:0000331 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Missing anchors/examples, empty inventories and zero molecular graph nodes do not validate narrative molecules, localization, mechanism, taxon transfer or assembly necessity. |
| Native contractile vacuole complex UniProt verify check | passed | True | GO:0062159 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Missing anchors/examples, empty inventories and zero molecular graph nodes do not validate narrative molecules, localization, mechanism, taxon transfer or assembly necessity. |
| Native contractile vacuole complex UniProt causal check | passed | True | GO:0062159 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Missing anchors/examples, empty inventories and zero molecular graph nodes do not validate narrative molecules, localization, mechanism, taxon transfer or assembly necessity. |
| Native contractile vacuole lumen UniProt verify check | passed | True | cellstructuremech:contractile_vacuole_lumen | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Missing anchors/examples, empty inventories and zero molecular graph nodes do not validate narrative molecules, localization, mechanism, taxon transfer or assembly necessity. |
| Native contractile vacuole lumen UniProt causal check | passed | True | cellstructuremech:contractile_vacuole_lumen | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Missing anchors/examples, empty inventories and zero molecular graph nodes do not validate narrative molecules, localization, mechanism, taxon transfer or assembly necessity. |
| Native contractile vacuole pore UniProt verify check | passed | True | GO:0031913 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Missing anchors/examples, empty inventories and zero molecular graph nodes do not validate narrative molecules, localization, mechanism, taxon transfer or assembly necessity. |
| Native contractile vacuole pore UniProt causal check | passed | True | GO:0031913 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Missing anchors/examples, empty inventories and zero molecular graph nodes do not validate narrative molecules, localization, mechanism, taxon transfer or assembly necessity. |
| Native copi coated vesicle UniProt verify check | passed | True | GO:0030137 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Missing anchors/examples, empty inventories and zero molecular graph nodes do not validate narrative molecules, localization, mechanism, taxon transfer or assembly necessity. |
| Native copi coated vesicle UniProt causal check | passed | True | GO:0030137 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Missing anchors/examples, empty inventories and zero molecular graph nodes do not validate narrative molecules, localization, mechanism, taxon transfer or assembly necessity. |
| Native copi coated vesicle lumen UniProt verify check | passed | True | cellstructuremech:copi_coated_vesicle_lumen | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Missing anchors/examples, empty inventories and zero molecular graph nodes do not validate narrative molecules, localization, mechanism, taxon transfer or assembly necessity. |
| Native copi coated vesicle lumen UniProt causal check | passed | True | cellstructuremech:copi_coated_vesicle_lumen | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Missing anchors/examples, empty inventories and zero molecular graph nodes do not validate narrative molecules, localization, mechanism, taxon transfer or assembly necessity. |
| Native copi coated vesicle membrane UniProt verify check | passed | True | GO:0030663 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Missing anchors/examples, empty inventories and zero molecular graph nodes do not validate narrative molecules, localization, mechanism, taxon transfer or assembly necessity. |
| Native copi coated vesicle membrane UniProt causal check | passed | True | GO:0030663 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Missing anchors/examples, empty inventories and zero molecular graph nodes do not validate narrative molecules, localization, mechanism, taxon transfer or assembly necessity. |
| Native copii coated er to golgi transport vesicle UniProt verify check | passed | True | GO:0030134 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Missing anchors/examples, empty inventories and zero molecular graph nodes do not validate narrative molecules, localization, mechanism, taxon transfer or assembly necessity. |
| Native copii coated er to golgi transport vesicle UniProt causal check | passed | True | GO:0030134 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Missing anchors/examples, empty inventories and zero molecular graph nodes do not validate narrative molecules, localization, mechanism, taxon transfer or assembly necessity. |
| Native copii coated vesicle lumen UniProt verify check | passed | True | cellstructuremech:copii_coated_vesicle_lumen | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Missing anchors/examples, empty inventories and zero molecular graph nodes do not validate narrative molecules, localization, mechanism, taxon transfer or assembly necessity. |
| Native copii coated vesicle lumen UniProt causal check | passed | True | cellstructuremech:copii_coated_vesicle_lumen | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Missing anchors/examples, empty inventories and zero molecular graph nodes do not validate narrative molecules, localization, mechanism, taxon transfer or assembly necessity. |

## Scientific And Domain Assessments

### Native protein inventories and graph xrefs

schema: supported. Targets: cellstructuremech:contractile_vacuole_lumen.

Both commands pass with no represented protein examples or typed protein nodes. This validates empty inventories, not molecular narrative claims or biological necessity.

### Immutable original and current hashes

provenance: supported. Targets: cellstructuremech:contractile_vacuole_lumen.

Original native validate/render and every historical input hash pass; current target is byte-identical. Original findings/actions are empty. Historical record issue numbers and other cohort findings are not terminally disposed of here.

### Entire record and bounded evidence

completeness: supported. Targets: cellstructuremech:contractile_vacuole_lumen.

All target fields were read. Claim-bearing evidence assessed at stated tiers; no compulsory protein inventory, additional images or detailed quantitative/causal model is inferred. No concrete record-curation defect established. Applicability corrections belong to review bundles.

### Native protein inventories and graph xrefs

schema: supported. Targets: GO:0031913.

Both commands pass with no represented protein examples or typed protein nodes. This validates empty inventories, not molecular narrative claims or biological necessity.

### Immutable original and current hashes

provenance: supported. Targets: GO:0031913.

Original native validate/render and every historical input hash pass; current target is byte-identical. Original findings/actions are empty. Historical record issue numbers and other cohort findings are not terminally disposed of here.

### Entire record and bounded evidence

completeness: supported. Targets: GO:0031913.

All target fields were read. Claim-bearing evidence assessed at stated tiers; no compulsory protein inventory, additional images or detailed quantitative/causal model is inferred. No concrete record-curation defect established. Applicability corrections belong to review bundles.

### Native protein inventories and graph xrefs

schema: supported. Targets: GO:0030134.

Both commands pass with no represented protein examples or typed protein nodes. This validates empty inventories, not molecular narrative claims or biological necessity.

### Immutable original and current hashes

provenance: supported. Targets: GO:0030134.

Original native validate/render and every historical input hash pass; current target is byte-identical. Original findings/actions are empty. Historical record issue numbers and other cohort findings are not terminally disposed of here.

### Entire record and bounded evidence

completeness: supported. Targets: GO:0030134.

All target fields were read. Claim-bearing evidence assessed at stated tiers; no compulsory protein inventory, additional images or detailed quantitative/causal model is inferred. No concrete record-curation defect established. Applicability corrections belong to review bundles.

### Native protein inventories and graph xrefs

schema: supported. Targets: cellstructuremech:copii_coated_vesicle_lumen.

Both commands pass with no represented protein examples or typed protein nodes. This validates empty inventories, not molecular narrative claims or biological necessity.

### Immutable original and current hashes

provenance: supported. Targets: cellstructuremech:copii_coated_vesicle_lumen.

Original native validate/render and every historical input hash pass; current target is byte-identical. Original findings/actions are empty. Historical record issue numbers and other cohort findings are not terminally disposed of here.

### Entire record and bounded evidence

completeness: supported. Targets: cellstructuremech:copii_coated_vesicle_lumen.

All target fields were read. Claim-bearing evidence assessed at stated tiers; no compulsory protein inventory, additional images or detailed quantitative/causal model is inferred. No concrete record-curation defect established. Applicability corrections belong to review bundles.

### Local lumen identity and exact topology

identity: supported. Targets: cellstructuremech:contractile_vacuole_lumen.

Exact SL0320 definition/synonym supports the local enclosed compartment, broader vacuolar-lumen parent and whole-vacuole parthood. Membrane, whole vacuole and whole complex remain distinct. Bounded GO search does not establish exhaustive absence.

### Patchy occurrence and exact source models

scope: supported. Targets: cellstructuremech:contractile_vacuole_lumen.

More secondary abstract supports uneven freshwater/soil eukaryotic occurrence; RARE is qualitative, not a numerical census. Current taxa verify Eukaryota, Paramecium multimicronucleatum and Chlamydomonas reinhardtii. Gronlien example specifically concerns microelectrode potentials in compressed Paramecium; Komsic experiments use CC3395 and UVM4 derivatives rather than every algal strain.

### Filling, discharge and precise osmotic measurement scope

evidence: supported. Targets: cellstructuremech:contractile_vacuole_lumen.

Allen review and Komsic body support cyclic lumen filling/expansion and discharge. Komsic CV size tracks cell size/growth, while contraction interval responds to medium osmolarity. The target states volume measurements under varied osmolarity and separately osmolarity-responsive cycles; it does not assert that volume tracks osmolarity. This wording remains within measured Table1/Results scope and does not inherit a sibling whole-record overclaim.

### Direct measurements versus modeled lumen properties

evidence: unknown. Targets: cellstructuremech:contractile_vacuole_lumen.

Komsic explicitly could not directly determine lumen osmolarity; gradients/permeability are modeled. The target makes no direct osmolarity or channel-necessity claim. Figure captions/body, not image pixels or supplemental movies, were used.

### Lumen parthood and boundary

graph: supported. Targets: cellstructuremech:contractile_vacuole_lumen.

Both NONMECHANISTIC edges, lumen partOf whole and membrane bounds lumen, follow exact GO/SL topology. No channel mechanism or whole-organelle regulatory network is duplicated. Existing resolved boundary discussion is consistent with current content, without recertifying an external historical issue.

### Enclosed region with no forced constituent inventory

grounding: supported. Targets: cellstructuremech:contractile_vacuole_lumen.

The lumen is a spatial region, not its membrane or molecular transport machinery. No named constituent or formation-essential protein is asserted. Empty components are appropriate to the claim scope.

### Explicit osmotic-response applicability

scope: supported. Targets: cellstructuremech:contractile_vacuole_lumen.

The record explicitly invokes osmolarity-responsive filling/discharge and osmoregulation. Stress-response/trait context triggers applicability despite no proteins. Original has no structured-source row. Fresh full catalogue has no relevant eukaryotic host, so no matched gene/module query applies; historical runner limitation remains separately dated.

### Stable pore versus transient opening or whole vacuole

identity: supported. Targets: GO:0031913.

Exact active GO0031913 definition and typed is_a/part_of relations agree. A persistent site is distinguished from its transient discharge opening and from the whole CV. MULTIPROTEIN_COMPLEX is ontology classification, not a claimed experimentally resolved subunit list.

### Species-qualified secondary model and genus primary synopsis

scope: supported. Targets: GO:0031913.

Current taxon verifies T.thermophila5911. Record explicitly presents Frankel as review-level model support. McKanna synopsis supports Paramecium genus ultrastructure only; no missing species is invented and older T.pyriformis citations are not relabeled thermophila experiments.

### Unresolved pore molecular composition

grounding: unknown. Targets: GO:0031913.

Frankel text and McKanna synopsis describe cortical membrane/diaphragm and microtubule organization, but do not establish a complete molecular inventory or exact essential subunit. Existing open composition TODO correctly withholds protein IDs; absence of molecular inventory alone is not a defect.

### Coarse parthood and liquid-flow function

graph: supported. Targets: GO:0031913.

Two partOf edges and descriptive regulation of liquid flow follow GO definition and inspected morphology. NONMECHANISTIC scope makes no actin necessity, force-generation, gating-rate or subunit-dependency claim.

### Genuine topology and coarse-flow exclusion

scope: not_applicable. Targets: GO:0031913.

No named gene, locus, protein identity, regulator, explicit stress-response pathway or transcriptomic assignment is made. Generic liquid-flow control and the ontology complex label do not establish a candidate molecular query. Original N/A outcome is retained with this concrete rationale, not counted as a defect solely because its sentence mentioned absence of expression inference. Catalogue also has no relevant ciliate host.

### Accessible secondary chapter and primary synopsis

provenance: supported. Targets: GO:0031913.

Frankel genuine institutional PDF was read only at named complete CV/pore sections and opening positioning paragraphs. McKanna is publisher-deposited primary synopsis, not full article. API bibliographic stub and publisher challenge pages are not bodies. No microscopy pixels or complete-book review claimed.

### Yeast occurrence and experimental specificity

scope: supported. Targets: GO:0030134.

Current ENA verifies S.cerevisiae4932. Barlowe abstract supports native ER-derived COPII transport intermediates; Matsuoka body includes native microsomes and distinct synthetic-liposome experiments with named yeast preparations. COMMON remains qualitative model-system context, not a population census or universal cell-state assertion.

### Reconstitution versus universal formation necessity

evidence: unknown. Targets: GO:0030134.

Sec/Sar1 machinery is positively supported as COPII coat/budding context. Synthetic-liposome conditions, altered concentrations and GMP-PNP differ from physiological native transport; success in reconstitution is not proof of each molecule being universally necessary in vivo. No individual essentiality assertion is made on these targets.

### Named Sec/Sar molecular applicability

scope: supported. Targets: GO:0030134.

Both target narratives explicitly name Sec/Sar machinery despite sparse direct components. Original expression-only N/A rationales therefore miss the actual molecular trigger. Fresh complete catalogue lacks S.cerevisiae; no unmatched strain/species module evidence is substituted and no biological absence follows. Historical runner is unavailable at its original time, not freshly rerun.

### Primary abstract and genuine fresh primary body

provenance: supported. Targets: GO:0030134.

Barlowe1994 is used at complete primary abstract tier only; publisher routes returned challenges. Fresh institutional Matsuoka1998 PDF was read pp263–274, including Methods, Tables and captions; no raw data/figure-pixel or live-cell lumen audit. The PDF was freshly fetched here, not represented as an old cached receipt.

### Yeast occurrence and experimental specificity

scope: supported. Targets: cellstructuremech:copii_coated_vesicle_lumen.

Current ENA verifies S.cerevisiae4932. Barlowe abstract supports native ER-derived COPII transport intermediates; Matsuoka body includes native microsomes and distinct synthetic-liposome experiments with named yeast preparations. COMMON remains qualitative model-system context, not a population census or universal cell-state assertion.

### Reconstitution versus universal formation necessity

evidence: unknown. Targets: cellstructuremech:copii_coated_vesicle_lumen.

Sec/Sar1 machinery is positively supported as COPII coat/budding context. Synthetic-liposome conditions, altered concentrations and GMP-PNP differ from physiological native transport; success in reconstitution is not proof of each molecule being universally necessary in vivo. No individual essentiality assertion is made on these targets.

### Named Sec/Sar molecular applicability

scope: supported. Targets: cellstructuremech:copii_coated_vesicle_lumen.

Both target narratives explicitly name Sec/Sar machinery despite sparse direct components. Original expression-only N/A rationales therefore miss the actual molecular trigger. Fresh complete catalogue lacks S.cerevisiae; no unmatched strain/species module evidence is substituted and no biological absence follows. Historical runner is unavailable at its original time, not freshly rerun.

### Primary abstract and genuine fresh primary body

provenance: supported. Targets: cellstructuremech:copii_coated_vesicle_lumen.

Barlowe1994 is used at complete primary abstract tier only; publisher routes returned challenges. Fresh institutional Matsuoka1998 PDF was read pp263–274, including Methods, Tables and captions; no raw data/figure-pixel or live-cell lumen audit. The PDF was freshly fetched here, not represented as an old cached receipt.

### Whole COPII vesicle distinct from its coat

identity: supported. Targets: GO:0030134.

GO0030134 exactly denotes the COPII-coated ER-to-Golgi vesicle with Sec23/24 and Sec13/31 heterodimer coat narrative. Coated-vesicle parent, coat structural part, and exact/related synonym types agree. The whole membrane-bounded organelle is not reduced to a protein complex.

### Constituent coat context without redundant inventories

grounding: supported. Targets: GO:0030134.

Named coat subcomplexes are supported by source definitions and primary experiments. They remain coat/budding context, not a mandatory duplicate inventory of components on the whole-vesicle record. No represented protein accession exists to falsely certify.

### Transport function distinguished from budding

evidence: supported. Targets: GO:0030134.

GO0006888 represents ER-to-Golgi transport, whereas GO0090114 represents ER-membrane evagination/budding. The record correctly attributes transport to vesicle and budding context to coat. Barlowe GTP vesicles can target/fuse; GMP-PNP products cannot, so evidence does not license universal transport competence of synthetic coated buds.

### Five descriptive transport-topology edges

graph: supported. Targets: GO:0030134.

Coat partOf whole, ER membrane evagination into vesicle, vesicle cargo transport to Golgi, coat participation in budding, and vesicle participation in transport align with exact GO and primary scopes. NONMECHANISTIC graph does not claim vesicle self-formation or complete molecular mechanism. Historical record issue numbers remain context only.

### SL-defined local lumen and exact candidate conflict

identity: unknown. Targets: cellstructuremech:copii_coated_vesicle_lumen.

SL0322 exactly defines this lumen and supports synonyms, cytoplasmic-vesicle-lumen parent and whole-vesicle parthood. Active GO0106173 exact label conflicts with its endocytic definition. Preserve that unresolved authority conflict rather than force a GO replacement or claim the candidate is absent.

### Enclosed lumen distinct from machinery

grounding: supported. Targets: cellstructuremech:copii_coated_vesicle_lumen.

The enclosed region has no required constituent cargo/protein inventory. Sec/Sar machinery describes formation context rather than lumen constitution. Primary synthetic trapped-solute experiment supports closed lumen formation in its own assay, not direct live-yeast lumen morphology or every cargo composition.

### Lumen parthood and membrane boundary

graph: supported. Targets: cellstructuremech:copii_coated_vesicle_lumen.

The two NONMECHANISTIC edges are lumen partOf whole and ER-to-Golgi-vesicle membrane bounds lumen. Exact SL0322 and GO0012507 support the geometry without importing cargo selection, fusion or individual assembly necessity.

### Exact structure, membrane and lumen boundaries

identity: supported. Targets: GO:0030137.

The whole vesicle is a membrane-bounded organelle; its membrane is a bilayer and its lumen a bounded region. Exact native definitions and hierarchy agree. Coatomer remains the coat complex, not a whole-vesicle synonym. The lumen candidate caveat is explicit below.

### Yeast experimental scope and source tiers

scope: supported. Targets: GO:0030137.

Sandmann supports a yeast early-secretory/COPI model through coatomer-mutant, binding and vesicle assays. Canonical wording does not assert a specific strain/quantitative preparation. COMMON is qualitative occurrence; membrane/lumen occurrence follows the bounded-vesicle model and authority definitions, not a separately measured population frequency. E. coli expression is not assigned as the structure host.

### Component versus topology representation

grounding: supported. Targets: GO:0030137.

Coat and bilayer are structural parts. Keeping coatomer/Arf constituents on the coat neighbor avoids duplicating its molecular inventory. Waters abstract and scoped Yu model support this boundary, not universal subunit necessity.

### Every current directed edge and bounded semantics

graph: supported. Targets: GO:0030137.

Six NONMECHANISTIC edges retain coat/bilayer parthood, Golgi evagination, budding and retrograde participation. The new process-to-ER edge adds a destination, matching GO0006890 directed substances Golgi→ER and COPI carrier scope. Broad proteins/lipids are consistent with source transport context, not a lipid-species flux assay or fusion mechanism.

### Primary versus authority/secondary source scope

evidence: supported. Targets: GO:0030137.

Source-specific statements remain separated: Sandmann selected primary body sections; native exact authority definitions; Waters primary abstract only where cited; retained Yu scoped body for coat recruitment. The 2018 review is explicitly secondary context and does not substitute for direct experimental lipid flux or resolve the lumen definition conflict.

### Structured-source applicability reassessed

provenance: supported. Targets: GO:0030137.

Native molecular/pathway trigger is present in coatomer/Arf or coatomer-dependent retrograde-retrieval narrative. Original expression-only exclusion is insufficient. Complete current official catalogue has no matching yeast dataset, so downstream matching-gene/module checks are inapplicable. Historical runner failure is separately dated and no biological absence inferred.

### Native original pairs, frozen inputs and limited protein checks

schema: supported. Targets: GO:0030137.

Original YAML validates and Markdown renders exactly. Original target hash differs only by the documented history/edge additions; current content has been substantively reassessed. Both current native protein commands pass empty inventories/zero molecular nodes; they cannot certify prose mechanisms.

### Entire maintained record and bounded verdict

completeness: supported. Targets: GO:0030137.

All maintained fields, notes, discussions, source references and graph edges were assessed. No image, quantitative property, snippet or protein inventory is asserted by this target. Empty optional fields and acknowledged label-only material do not establish defects. Original observations remain immutable, with no original findings or request-curation actions to carry forward; historical record issue closures are not re-disposed.

### Exact structure, membrane and lumen boundaries

identity: supported. Targets: cellstructuremech:copi_coated_vesicle_lumen.

The whole vesicle is a membrane-bounded organelle; its membrane is a bilayer and its lumen a bounded region. Exact native definitions and hierarchy agree. Coatomer remains the coat complex, not a whole-vesicle synonym. The lumen candidate caveat is explicit below.

### Yeast experimental scope and source tiers

scope: supported. Targets: cellstructuremech:copi_coated_vesicle_lumen.

Sandmann supports a yeast early-secretory/COPI model through coatomer-mutant, binding and vesicle assays. Canonical wording does not assert a specific strain/quantitative preparation. COMMON is qualitative occurrence; membrane/lumen occurrence follows the bounded-vesicle model and authority definitions, not a separately measured population frequency. E. coli expression is not assigned as the structure host.

### Component versus topology representation

grounding: supported. Targets: cellstructuremech:copi_coated_vesicle_lumen.

The lumen is a region rather than a molecular component; no exact family or cargo inventory is required.

### Every current directed edge and bounded semantics

graph: supported. Targets: cellstructuremech:copi_coated_vesicle_lumen.

Two NONMECHANISTIC edges state bounded lumen inside the whole vesicle and its membrane boundary. No cargo sorting, coat assembly or fusion is asserted.

### Primary versus authority/secondary source scope

evidence: supported. Targets: cellstructuremech:copi_coated_vesicle_lumen.

Source-specific statements remain separated: Sandmann selected primary body sections; native exact authority definitions; Waters primary abstract only where cited; retained Yu scoped body for coat recruitment. The 2018 review is explicitly secondary context and does not substitute for direct experimental lipid flux or resolve the lumen definition conflict.

### Structured-source applicability reassessed

provenance: supported. Targets: cellstructuremech:copi_coated_vesicle_lumen.

Native molecular/pathway trigger is present in coatomer/Arf or coatomer-dependent retrograde-retrieval narrative. Original expression-only exclusion is insufficient. Complete current official catalogue has no matching yeast dataset, so downstream matching-gene/module checks are inapplicable. Historical runner failure is separately dated and no biological absence inferred.

### Native original pairs, frozen inputs and limited protein checks

schema: supported. Targets: cellstructuremech:copi_coated_vesicle_lumen.

Original YAML validates and Markdown renders exactly. Original frozen target hash equals current main. Both current native protein commands pass empty inventories/zero molecular nodes; they cannot certify prose mechanisms.

### Entire maintained record and bounded verdict

completeness: supported. Targets: cellstructuremech:copi_coated_vesicle_lumen.

All maintained fields, notes, discussions, source references and graph edges were assessed. No image, quantitative property, snippet or protein inventory is asserted by this target. Empty optional fields and acknowledged label-only material do not establish defects. Original observations remain immutable, with no original findings or request-curation actions to carry forward; historical record issue closures are not re-disposed.

### Exact structure, membrane and lumen boundaries

identity: supported. Targets: GO:0030663.

The whole vesicle is a membrane-bounded organelle; its membrane is a bilayer and its lumen a bounded region. Exact native definitions and hierarchy agree. Coatomer remains the coat complex, not a whole-vesicle synonym. The lumen candidate caveat is explicit below.

### Yeast experimental scope and source tiers

scope: supported. Targets: GO:0030663.

Sandmann supports a yeast early-secretory/COPI model through coatomer-mutant, binding and vesicle assays. Canonical wording does not assert a specific strain/quantitative preparation. COMMON is qualitative occurrence; membrane/lumen occurrence follows the bounded-vesicle model and authority definitions, not a separately measured population frequency. E. coli expression is not assigned as the structure host.

### Component versus topology representation

grounding: supported. Targets: GO:0030663.

The direct LIPID row describes collective bilayer material. Label-only grounding and component_ref avoid inventing a molecular lipid identity. Coat parthood is compatible with keeping coatomer/Arf out of the lipid constituent list; no individual lipid necessity is demonstrated.

### Every current directed edge and bounded semantics

graph: supported. Targets: GO:0030663.

Three NONMECHANISTIC edges state bilayer parthood/boundary and Golgi membrane donation. GO0035964 directly specifies evagination; no separate assembly mechanism or constituent necessity follows.

### Primary versus authority/secondary source scope

evidence: supported. Targets: GO:0030663.

Source-specific statements remain separated: Sandmann selected primary body sections; native exact authority definitions; Waters primary abstract only where cited; retained Yu scoped body for coat recruitment. The 2018 review is explicitly secondary context and does not substitute for direct experimental lipid flux or resolve the lumen definition conflict.

### Structured-source applicability reassessed

provenance: supported. Targets: GO:0030663.

Native molecular/pathway trigger is present in coatomer/Arf or coatomer-dependent retrograde-retrieval narrative. Original expression-only exclusion is insufficient. Complete current official catalogue has no matching yeast dataset, so downstream matching-gene/module checks are inapplicable. Historical runner failure is separately dated and no biological absence inferred.

### Native original pairs, frozen inputs and limited protein checks

schema: supported. Targets: GO:0030663.

Original YAML validates and Markdown renders exactly. Original frozen target hash equals current main. Both current native protein commands pass empty inventories/zero molecular nodes; they cannot certify prose mechanisms.

### Entire maintained record and bounded verdict

completeness: supported. Targets: GO:0030663.

All maintained fields, notes, discussions, source references and graph edges were assessed. No image, quantitative property, snippet or protein inventory is asserted by this target. Empty optional fields and acknowledged label-only material do not establish defects. Original observations remain immutable, with no original findings or request-curation actions to carry forward; historical record issue closures are not re-disposed.

### Same-label GO candidate remains definition-limited

grounding: unknown. Targets: cellstructuremech:copi_coated_vesicle_lumen.

GO0106172 is active and returned by current search, but both exact QuickGO and OLS descriptions specify an endocytic vesicle. SL-0321 and the local target denote general COPI lumen. Secondary definition-citation abstract describes Golgi/ER traffic but does not resolve this inconsistency. Retain unknown exact equivalence; no mandatory remapping or universal absence claim follows.

### Collective bilayer versus individual lipid requirement

grounding: unknown. Targets: GO:0030663.

The ESSENTIAL component denotes the collective bilayer constituting the membrane. No individual lipid species, deletion test or replacement necessity is specified or inferred from the ontology/vesicle assays.

### Original validation, deterministic rendering and input currentness

schema: supported. Targets: GO:0031164.

Original bundle validates/renders exactly and its frozen target hash matches current bytes and the original source revision. Native inventory checks pass with their actual coverage limits, not as certification of all scientific assertions.

### Actual protein inventory coverage

provenance: supported. Targets: GO:0031164.

No protein examples or UniProtKB protein xrefs. The two protein nodes comprise one NO_GENE_SYMBOLS aquaporin component and one UNANCHORED_NO_UNIPROT perivacuolar V-ATPase context node. Exit0 does not verify species-specific identity, localization or necessity.

### No target images, measurements or verbatim snippets

scope: not_applicable. Targets: GO:0031164.

None is declared in this maintained target. Primary body/caption text inspection does not constitute figure-pixel, supplementary movie or raw-data reanalysis.

### Original validation, deterministic rendering and input currentness

schema: supported. Targets: GO:0000331.

Original bundle validates/renders exactly and its frozen target hash matches current bytes and the original source revision. Native inventory checks pass with their actual coverage limits, not as certification of all scientific assertions.

### Actual protein inventory coverage

provenance: supported. Targets: GO:0000331.

Six protein examples verify. The V-ATPase node is COVERED by four examples; the aquaporin node is PARTIAL_EXAMPLES with MIP1 missing. This is inventory/identity coverage, not proof that aqpA/aqpB reside in a CV or that MIP1 lacks a biological counterpart.

### No target images, measurements or verbatim snippets

scope: not_applicable. Targets: GO:0000331.

None is declared in this maintained target. Primary body/caption text inspection does not constitute figure-pixel, supplementary movie or raw-data reanalysis.

### Original validation, deterministic rendering and input currentness

schema: supported. Targets: GO:0062159.

Original bundle validates/renders exactly and its frozen target hash matches current bytes and the original source revision. Native inventory checks pass with their actual coverage limits, not as certification of all scientific assertions.

### Actual protein inventory coverage

provenance: supported. Targets: GO:0062159.

Empty protein example/xref inventory and zero GENE_OR_PROTEIN nodes. Exit0 does not independently validate the molecular details intentionally assigned to child records or the osmoregulatory pathway.

### No target images, measurements or verbatim snippets

scope: not_applicable. Targets: GO:0062159.

None is declared in this maintained target. Primary body/caption text inspection does not constitute figure-pixel, supplementary movie or raw-data reanalysis.

### Patchy eukaryotic occurrence and qualitative rarity

scope: supported. Targets: GO:0031164.

ENA confirms Eukaryota and each named species. More secondary abstract and selected Docampo body support patchy distribution with diverse architectures; RARE is qualitative, not a measured fraction or a claim of uniform molecular conservation.

### Molecular and osmoregulatory-response applicability

scope: not_applicable. Targets: GO:0031164.

Membrane and whole record assert channel/pump roles; whole additionally names exact genes and hypo-osmotic stress response. Complex positively asserts osmoregulatory water expulsion/fluid segregation, while molecular detail remains on children. These scopes merit applicability assessment. The complete fresh catalogue lacks matched model organisms, so downstream queries are not applicable; historical runner failure is separately dated.

### Structure formation versus transport function

scope: unknown. Targets: GO:0031164.

Generic membrane material is constitutionally essential where declared. Molecular components retain UNKNOWN formation necessity. Localization, pump inhibition, water flux, or spore-survival phenotypes do not establish a universal requirement for forming the whole structure.

### Membrane, bladder, lumen, pore, spongiome and whole-complex boundaries

consistency: supported. Targets: GO:0031164.

Exact native identities keep the bladder separate from its bounding membrane and lumen and from the composite bladder/spongiome apparatus. Pore context remains a separate anchored structure. Frozen neighbors were inspected only at boundary fields; no neighbor or historical grouped/category issue is resolved.

### Current source bodies, abstract limits and historical observations

provenance: supported. Targets: GO:0031164.

Current Komsic/Bülow primary bodies and selected Docampo secondary sections were actually read at declared extents. Nishihara, Clarke, Nolta, Gronlien, Rohloff and Mitra primary support is complete abstract only; More and Allen are secondary abstracts. Current failed public routes are disclosed. Original October observations remain historical.

### Patchy eukaryotic occurrence and qualitative rarity

scope: supported. Targets: GO:0000331.

ENA confirms Eukaryota and each named species. More secondary abstract and selected Docampo body support patchy distribution with diverse architectures; RARE is qualitative, not a measured fraction or a claim of uniform molecular conservation.

### Molecular and osmoregulatory-response applicability

scope: not_applicable. Targets: GO:0000331.

Membrane and whole record assert channel/pump roles; whole additionally names exact genes and hypo-osmotic stress response. Complex positively asserts osmoregulatory water expulsion/fluid segregation, while molecular detail remains on children. These scopes merit applicability assessment. The complete fresh catalogue lacks matched model organisms, so downstream queries are not applicable; historical runner failure is separately dated.

### Structure formation versus transport function

scope: unknown. Targets: GO:0000331.

Generic membrane material is constitutionally essential where declared. Molecular components retain UNKNOWN formation necessity. Localization, pump inhibition, water flux, or spore-survival phenotypes do not establish a universal requirement for forming the whole structure.

### Membrane, bladder, lumen, pore, spongiome and whole-complex boundaries

consistency: supported. Targets: GO:0000331.

Exact native identities keep the bladder separate from its bounding membrane and lumen and from the composite bladder/spongiome apparatus. Pore context remains a separate anchored structure. Frozen neighbors were inspected only at boundary fields; no neighbor or historical grouped/category issue is resolved.

### Current source bodies, abstract limits and historical observations

provenance: supported. Targets: GO:0000331.

Current Komsic/Bülow primary bodies and selected Docampo secondary sections were actually read at declared extents. Nishihara, Clarke, Nolta, Gronlien, Rohloff and Mitra primary support is complete abstract only; More and Allen are secondary abstracts. Current failed public routes are disclosed. Original October observations remain historical.

### Patchy eukaryotic occurrence and qualitative rarity

scope: supported. Targets: GO:0062159.

ENA confirms Eukaryota and each named species. More secondary abstract and selected Docampo body support patchy distribution with diverse architectures; RARE is qualitative, not a measured fraction or a claim of uniform molecular conservation.

### Molecular and osmoregulatory-response applicability

scope: not_applicable. Targets: GO:0062159.

Membrane and whole record assert channel/pump roles; whole additionally names exact genes and hypo-osmotic stress response. Complex positively asserts osmoregulatory water expulsion/fluid segregation, while molecular detail remains on children. These scopes merit applicability assessment. The complete fresh catalogue lacks matched model organisms, so downstream queries are not applicable; historical runner failure is separately dated.

### Structure formation versus transport function

scope: unknown. Targets: GO:0062159.

Generic membrane material is constitutionally essential where declared. Molecular components retain UNKNOWN formation necessity. Localization, pump inhibition, water flux, or spore-survival phenotypes do not establish a universal requirement for forming the whole structure.

### Membrane, bladder, lumen, pore, spongiome and whole-complex boundaries

consistency: supported. Targets: GO:0062159.

Exact native identities keep the bladder separate from its bounding membrane and lumen and from the composite bladder/spongiome apparatus. Pore context remains a separate anchored structure. Frozen neighbors were inspected only at boundary fields; no neighbor or historical grouped/category issue is resolved.

### Current source bodies, abstract limits and historical observations

provenance: supported. Targets: GO:0062159.

Current Komsic/Bülow primary bodies and selected Docampo secondary sections were actually read at declared extents. Nishihara, Clarke, Nolta, Gronlien, Rohloff and Mitra primary support is complete abstract only; More and Allen are secondary abstracts. Current failed public routes are disclosed. Original October observations remain historical.

### Exact bilayer, synonym and hierarchy

identity: supported. Targets: GO:0031164.

GO0031164 and SL0074 agree on contractile vacuolar membrane identity/synonym, vacuolar-membrane parent and contractile-vacuole parthood. Broader location-database complex prose does not collapse the membrane/bladder/apparatus distinction.

### Constitutional bilayer and supported aquaporin class

grounding: supported. Targets: GO:0031164.

The generic bilayer is label-only constitutional material, not an exact lipid molecule grounded to a whole-location GO term. Nishihara directly supports ApAQP at the Amoeba CV membrane and surrounding vesicles. No guessed species-specific accession or unsupported claim that all broad MIP family members localize to CVs is introduced.

### Amoeba localization and perivacuolar pump context

scope: supported. Targets: GO:0031164.

Taxon5775 is Amoeba proteus. The canonical sentence is read with the explicit graph/component boundary: ApAQP labels CV membrane/perivacuolar vesicles, V-ATPase labels surrounding vesicles. The record has already excluded the pump from direct membrane components, and its graph respects this source localization.

### Five scoped filling-context edges

graph: supported. Targets: GO:0031164.

Membrane bounds vacuole; pump resides in perivacuolar vesicles; possible ion-gradient contribution, ApAQP water permeability and filling support remain source-scoped. The unanchored pump is context, not a claimed constituent of this one bilayer. Gradient generation is a source hypothesis and a complete systole mechanism is not asserted.

### Qualified positive membrane review

consistency: supported. Targets: GO:0031164.

pass_with_limitations is supported for identity, Amoeba channel localization, carefully separated perivacuolar pump context and nonmechanistic filling graph. No original or new concrete scientific record correction is established; molecular formation dependency and complete native identity coverage remain unknown.

### Bladder identity and synonym qualifier

identity: concern. Targets: GO:0000331.

Exact GO0000331 identity, complex parthood and membrane part remain supported. SL0073 supports CV. However central bladder is RELATED in the cited current GO authority, so the maintained EXACT qualifier remains inherited F3.

### V-ATPase subunit examples and source scope

grounding: supported. Targets: GO:0000331.

Four reviewed Dictyostelium accessions and bounded gene queries match vatA/B/C/M. Clarke supports VatM-directed assembly and CVC membrane targeting; Nolta and Allen distinguish pump-rich spongiome and pump-poor bladder. Record descriptions use system-level membranes, and no homogeneous pump distribution or formation necessity is inferred. Broad GO0016471 is not a substitute for an experimentally localized cross-lineage subset.

### Taxon-paired CV localization and inherited F1

evidence: concern. Targets: GO:0000331.

Amoeba ApAQP and Chlamydomonas MIP1 support CV-associated aquaporins at their own taxa. Dictyostelium aqpA sources concern development/spore dormancy; AqpB primary localization is to unidentified vacuoles and membrane protrusions, with a CV-like role only proposed by analogy. Identity-only examples do not establish CV constituent membership. Mutant water conductance is not demonstrated wild-type AqpB conductance.

### Supported MIP1 localization with unresolved accession/transport assay scope

scope: supported. Targets: GO:0000331.

Komsic reports immunogold and GFP localization at CV membranes in CC3395/UVM4-derived strains. Exact current MIP1/taxon3055 query returns no entry; this does not refute localization or justify guessing an accession. Modeled CV water permeability, questioned GFP construct functionality and direct localization are separate evidence types.

### Inherited F2 and repeated discharge-edge source note

evidence: concern. Targets: GO:0000331.

Komsic Results distinguish CV size correlated with cell size from contraction interval dependent on medium osmolarity. The canonical note overstates both responding to external osmolarity; the final discharge-edge evidence note repeats osmolarity-dependent size changes. Both fields belong to the same inherited F2, without changing the valid water-expulsion function or measured-size context.

### Dictyostelium and T.cruzi model-specific findings

scope: supported. Targets: GO:0000331.

Dictyostelium V-ATPase dynamics are supported by Clarke primary abstract; T.cruzi acidocalcisome/CVC involvement in hypo-osmotic recovery is supported by Rohloff primary abstract. Neither model establishes shared invariant machinery in all eukaryotes.

### Six filling/discharge edges with explicit inherited concerns

graph: concern. Targets: GO:0000331.

The anatomical enclosure and general pump/channel-assisted osmotic filling/discharge model have source support at declared nonmechanistic/hypothesis scope. The aquaporin node inherits unsupported aqpA/aqpB constituent specificity (F1), and discharge-edge evidence repeats F2. Transient filled-vacuole state is deliberately not given the exact GO class grounding. A full force-generating systole mechanism remains unasserted.

### Needs curation with preserved three-finding lineage

consistency: concern. Targets: GO:0000331.

needs_curation remains warranted by F1 major membership support, F2 minor osmolarity/size wording (including its repeated graph note), and F3 minor synonym scope. Scientific identity and general osmoregulation remain supported. Exact predecessor repository/review/finding identities are retained; no finding is silently resolved by native command success.

### Composite apparatus distinct from membrane-bounded bladder

identity: supported. Targets: GO:0062159.

GO0062159 explicitly denotes the non-membrane-bounded composite apparatus and has related synonym CVC, GO0043232 parent and bladder/spongiome parts. OTHER preserves this composite scope rather than asserting one enclosing bilayer around the entire apparatus. This does not deny membranes on its constituent bladder/tubules.

### Dictyostelium bipartite fractions and Paramecium radial arms

scope: supported. Targets: GO:0062159.

Nolta primary abstract supports separable bladder/spongiome membrane fractions in Dictyostelium; Gronlien supports decorated-spongiome electrogenic fluid segregation in P.multimicronucleatum. The record does not transfer a fixed ciliate radial-arm architecture to all protists or treat transport inhibition as failure to form the complex.

### Three organelle-level parthood/function edges

graph: supported. Targets: GO:0062159.

Bladder and spongiome are parts of the complex, which carries out periodic water expulsion. Exact GO relations and the bipartite primary evidence support these edges. Molecular pump/channel and electrophysiological details remain assigned to children, without claiming a full conserved force-generation mechanism.

### Qualified positive whole-complex review

consistency: supported. Targets: GO:0062159.

pass_with_limitations remains supported for exact composite identity, source-qualified model examples, child boundaries and general osmoregulation. No original or new scientific finding is established for this record. Broad eukaryotic prevalence and full conservation/mechanism remain unproven.

### Complete frozen-input comparison and bounded refresh

provenance: supported. Targets: GO:0031164, GO:0000331, GO:0062159, cellstructuremech:contractile_vacuole_lumen, GO:0031913, GO:0030137, cellstructuremech:copi_coated_vesicle_lumen, GO:0030663, GO:0030134, cellstructuremech:copii_coated_vesicle_lumen.

1 of ten original target hashes differ from current main. The changed content is substantively reassessed in the target-specific assessments; original observations remain historical and unchanged. All current target and used context bytes are frozen.

## Findings

### septin-F1: Dictyostelium aqpA and aqpB lack demonstrated CV membership in the cited evidence

major / open / confirmed; issue key: contractile-vacuole-aqpa-aqpb-membership-support.

The contractile_vacuole_aquaporins constituent declares aqpA and aqpB and supplies their verified Dictyostelium examples. The identity-only disclaimers correctly limit what accessions prove but leave that constituent assignment unsupported. AqpA sources concern late development and spore dormancy. The AqpB primary paper localizes GFP constructs to unspecified vacuoles and plasma membrane/protrusions, then proposes a CV-like role by analogy; it does not experimentally identify the vacuoles as contractile vacuoles. Water permeability was demonstrated for a loop-deletion mutant rather than the tested wild-type protein. Amoeba ApAQP and Chlamydomonas MIP1 evidence supports the broader component without proving these two assignments.

### septin-F2: Chlamydomonas example conflates CV size regulation with osmolarity response

minor / open / confirmed; issue key: contractile-vacuole-chlamydomonas-size-osmolarity-note.

The canonical note says both CV size and pulse frequency respond to changing external osmolarity. Komsic-Buchmann2014 Results explicitly report that CV size did not correlate with medium osmotic strength: CV size correlated with cell size, while contraction interval depended on medium osmolarity. The two adaptations are distinguished in the paper. The broader function and measured-size/interval evidence remain supported. The same overstatement is repeated in the final discharge-edge evidence note, which describes osmolarity-dependent pulse-frequency and size changes. This successor includes that repeated field under the same F2 lineage, not as a separate finding.

### septin-F3: Central bladder synonym scope exceeds the cited GO mapping

minor / open / confirmed; issue key: contractile-vacuole-central-bladder-synonym-scope.

The record labels central bladder EXACT_SYNONYM and names GO:0000331 as its source. Both captured current term and ancestry responses classify central bladder as a related synonym. The label is biologically pertinent, but the exactness qualifier is not supported by the cited authority.

## Recommended Actions And Acceptance Checks

### septin-A1

Under separately authorized curation, remove aqpA/aqpB and their identity-only examples from the established CV-constituent gene/example list unless direct CV-localization evidence is supplied. Retain the supported generic aquaporin class and evidenced MIP1/ApAQP context. If useful, preserve AqpB as an explicitly tentative hypothesis in a source-backed discussion, with unspecified-vacuole localization and mutant-versus-wild-type functional scope. Record the reason so symbol seeding cannot silently restore the unsupported assignment.

- Every retained named aquaporin in the CV constituent has a taxon-paired source supporting CV membership, not only identity, developmental expression or generic vacuolar location.
- The von Bülow2012 data are not described as direct CV localization or as demonstrated wild-type AqpB water conductance.
- The aquaporin graph remains at supported class/taxon scope, and MIP1 is not assigned a guessed accession.
- Use the guarded writer and required curation/history events; run native schema/strict, UniProt verification, CURIE/product, history and generated-page checks plus qc after any curation.

### septin-A2

Under separately authorized curation, revise the Chlamydomonas canonical note to distinguish CV size adaptation during cell growth from contraction-interval or pulse-frequency adaptation to external osmolarity. Preserve the valid model and source, and retain generic descriptions of measured size and interval only without implying both depend on medium osmolarity. Correct the repeated osmolarity-dependent size wording in the final discharge-edge evidence note as part of the same change.

- The canonical note accurately states the distinct Results relationships: CV size versus cell size, contraction interval versus medium osmolarity.
- The final discharge-edge evidence note also distinguishes osmolarity-dependent contraction interval from size/cell-growth correlation; it does not repeat the canonical-note overstatement.
- No direct lumen-osmolarity measurement or independent wild-type MIP1 water-channel assay is inferred from the modeling/localization study.
- Use the guarded writer and required curation/history events; run native schema/strict, history, render and qc gates after curation.

### septin-A3

Under separately authorized curation, change central bladder to RELATED_SYNONYM to match the cited GO authority, or supply and explicitly cite independent support for exact equivalence at this record scope. Retain the main GO identity and label.

- The central bladder synonym qualifier agrees with its cited authority or a separately justified exact mapping.
- Use the guarded writer and required history events; run schema/strict, identifier-label, history, render and qc checks after curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| current-record-0 | data/structures/membrane_organelle/contractile_vacuolar_membrane.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 a73ad7ccfc67c7c39a41d555109a229de1c469dec8eff0d808a3cddaa0aa383c; current SHA256 a73ad7ccfc67c7c39a41d555109a229de1c469dec8eff0d808a3cddaa0aa383c. Record bytes unchanged since the original review. |
| original-review-0 | reviews/structured/20261022T005251Z-contractile-vacuolar-membrane-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-1 | data/structures/membrane_organelle/contractile_vacuole.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 d1057e9c19ff100f054c73da52b597742dadde491f2a007cd7b648b8a7b626bb; current SHA256 d1057e9c19ff100f054c73da52b597742dadde491f2a007cd7b648b8a7b626bb. Record bytes unchanged since the original review. |
| original-review-1 | reviews/structured/20261022T005252Z-contractile-vacuole-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-2 | data/structures/membrane_organelle/contractile_vacuole_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 5d37be1aa899c1bfd20611faeafefb842a96e8a21144dea9e010b2c89d4b7a1c; current SHA256 5d37be1aa899c1bfd20611faeafefb842a96e8a21144dea9e010b2c89d4b7a1c. Record bytes unchanged since the original review. |
| original-review-2 | reviews/structured/20261022T005253Z-contractile-vacuole-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-3 | data/structures/membrane_organelle/contractile_vacuole_lumen.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 9c85ec352245d16e963b9d86d4d1cf0b41d499b956b0b2d05611dca3a4341622; current SHA256 9c85ec352245d16e963b9d86d4d1cf0b41d499b956b0b2d05611dca3a4341622. Record bytes unchanged since the original review. |
| original-review-3 | reviews/structured/20261022T005253Z-contractile-vacuole-lumen-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-4 | data/structures/membrane_organelle/contractile_vacuole_pore.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 e6b016675a36c215388bfd9053da4af4b1ec407c47c197f8a2217f9ba66cc294; current SHA256 e6b016675a36c215388bfd9053da4af4b1ec407c47c197f8a2217f9ba66cc294. Record bytes unchanged since the original review. |
| original-review-4 | reviews/structured/20261022T005254Z-contractile-vacuole-pore-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-5 | data/structures/membrane_organelle/copi_coated_vesicle.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 c8cf402aeadf4fea155d4735ed1df973e319b23d46664cd7ec286ba385c1a250; current SHA256 d542d1063731ec276cf5e771752715152ad950ee3fd1819f24e1a792036f2981. Changed record reassessed against current sources. |
| original-review-5 | reviews/structured/20261022T005255Z-copi-coated-vesicle-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-6 | data/structures/membrane_organelle/copi_coated_vesicle_lumen.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 f4da3395ba3aa5bfa65d859069e5b2f5d15303f81d7da6048291813188d9bcfa; current SHA256 f4da3395ba3aa5bfa65d859069e5b2f5d15303f81d7da6048291813188d9bcfa. Record bytes unchanged since the original review. |
| original-review-6 | reviews/structured/20261022T005255Z-copi-coated-vesicle-lumen-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-7 | data/structures/membrane_organelle/copi_coated_vesicle_membrane.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 70dbc868044797a3911de45524d13ccbedb5bf9cc671824b0dcade909ab4922f; current SHA256 70dbc868044797a3911de45524d13ccbedb5bf9cc671824b0dcade909ab4922f. Record bytes unchanged since the original review. |
| original-review-7 | reviews/structured/20261022T005256Z-copi-coated-vesicle-membrane-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-8 | data/structures/membrane_organelle/copii_coated_er_to_golgi_transport_vesicle.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 141713f26c4f5cc6a2e6c6cb232bf45e194df53bcd60aa4769cc4343ac6599bf; current SHA256 141713f26c4f5cc6a2e6c6cb232bf45e194df53bcd60aa4769cc4343ac6599bf. Record bytes unchanged since the original review. |
| original-review-8 | reviews/structured/20261022T005257Z-copii-coated-er-to-golgi-transport-vesicle-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-9 | data/structures/membrane_organelle/copii_coated_vesicle_lumen.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 d75ae8e81d2fc08979408842f74ef1ad621e87108044faf2dcc6ca216e5e7782; current SHA256 d75ae8e81d2fc08979408842f74ef1ad621e87108044faf2dcc6ca216e5e7782. Record bytes unchanged since the original review. |
| original-review-9 | reviews/structured/20261022T005258Z-copii-coated-vesicle-lumen-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| plaque-current-3 | data/structures/membrane_organelle/contractile_vacuole_lumen.yaml; Entire maintained record at source 7081777bba0daacfa48fc6d826cdfd7138e751b4; all fields, histories, discussions and graphs | supports | Complete current target read. Hash is unchanged from original frozen target; PROPOSED status remains and no record curation is performed. |
| plaque-original-3 | reviews/structured/20261022T005253Z-contractile-vacuole-lumen-audit/review.yaml; Original authoritative YAML, rendered Markdown, all frozen inputs, assessments, checks, findings/actions and limitations | supports | Original validates and renders byte-identically. All historical frozen inputs match original source commits; current target hash also matches. Original verdict pass_with_limitations, with no findings or curation actions. |
| plaque-current-4 | data/structures/membrane_organelle/contractile_vacuole_pore.yaml; Entire maintained record at source 7081777bba0daacfa48fc6d826cdfd7138e751b4; all fields, histories, discussions and graphs | supports | Complete current target read. Hash is unchanged from original frozen target; PROPOSED status remains and no record curation is performed. |
| plaque-original-4 | reviews/structured/20261022T005254Z-contractile-vacuole-pore-audit/review.yaml; Original authoritative YAML, rendered Markdown, all frozen inputs, assessments, checks, findings/actions and limitations | supports | Original validates and renders byte-identically. All historical frozen inputs match original source commits; current target hash also matches. Original verdict pass_with_limitations, with no findings or curation actions. |
| plaque-current-8 | data/structures/membrane_organelle/copii_coated_er_to_golgi_transport_vesicle.yaml; Entire maintained record at source 7081777bba0daacfa48fc6d826cdfd7138e751b4; all fields, histories, discussions and graphs | supports | Complete current target read. Hash is unchanged from original frozen target; PROPOSED status remains and no record curation is performed. |
| plaque-original-8 | reviews/structured/20261022T005257Z-copii-coated-er-to-golgi-transport-vesicle-audit/review.yaml; Original authoritative YAML, rendered Markdown, all frozen inputs, assessments, checks, findings/actions and limitations | supports | Original validates and renders byte-identically. All historical frozen inputs match original source commits; current target hash also matches. Original verdict pass_with_limitations, with no findings or curation actions. |
| plaque-current-9 | data/structures/membrane_organelle/copii_coated_vesicle_lumen.yaml; Entire maintained record at source 7081777bba0daacfa48fc6d826cdfd7138e751b4; all fields, histories, discussions and graphs | supports | Complete current target read. Hash is unchanged from original frozen target; PROPOSED status remains and no record curation is performed. |
| plaque-original-9 | reviews/structured/20261022T005258Z-copii-coated-vesicle-lumen-audit/review.yaml; Original authoritative YAML, rendered Markdown, all frozen inputs, assessments, checks, findings/actions and limitations | supports | Original validates and renders byte-identically. All historical frozen inputs match original source commits; current target hash also matches. Original verdict pass_with_limitations, with no findings or curation actions. |
| plaque-policy | .claude/skills/review-yaml-record/SKILL.md; Frozen native evidence, structure identity, component, graph and structured-source applicability contract | context_only | Named molecular, pathway, stress-response or trait narratives trigger applicability assessment; absence of expression inference alone does not justify exemption. Structural topology without those assertions can be genuinely excluded. |
| plaque-rubric | .claude/skills/curate-yaml-record/references/review-checklist.md; Frozen native evidence, structure identity, component, graph and structured-source applicability contract | context_only | Named molecular, pathway, stress-response or trait narratives trigger applicability assessment; absence of expression inference alone does not justify exemption. Structural topology without those assertions can be genuinely excluded. |
| plaque-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Frozen native evidence, structure identity, component, graph and structured-source applicability contract | context_only | Named molecular, pathway, stress-response or trait narratives trigger applicability assessment; absence of expression inference alone does not justify exemption. Structural topology without those assertions can be genuinely excluded. |
| plaque-schema-policy | src/cellstructuremech/schema/cellstructuremech.yaml; Frozen native evidence, structure identity, component, graph and structured-source applicability contract | context_only | Named molecular, pathway, stress-response or trait narratives trigger applicability assessment; absence of expression inference alone does not justify exemption. Structural topology without those assertions can be genuinely excluded. |
| plaque-neighbor-0 | data/structures/membrane_organelle/contractile_vacuolar_membrane.yaml; Identifier, label, definition, structure_kind, parent_structures, part_of and has_part only | context_only | Frozen cohort context distinguishes contractile vacuolar membrane, whole vacuole and vacuole complex. No independent full-science review, historical resolution or sibling finding disposition is inferred. |
| plaque-neighbor-1 | data/structures/membrane_organelle/contractile_vacuole.yaml; Identifier, label, definition, structure_kind, parent_structures, part_of and has_part only | context_only | Frozen cohort context distinguishes contractile vacuolar membrane, whole vacuole and vacuole complex. No independent full-science review, historical resolution or sibling finding disposition is inferred. |
| plaque-neighbor-2 | data/structures/membrane_organelle/contractile_vacuole_complex.yaml; Identifier, label, definition, structure_kind, parent_structures, part_of and has_part only | context_only | Frozen cohort context distinguishes contractile vacuolar membrane, whole vacuole and vacuole complex. No independent full-science review, historical resolution or sibling finding disposition is inferred. |
| plaque-contractile-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031164,GO:0005774,GO:0000331,GO:0062159,GO:0062160,GO:0043232,GO:0005775,GO:0031913,GO:0098797,GO:0005856; All ten requested active GO terms: exact names, definitions, typed children and immediate parent/parthood distinctions | supports | GO0005775 is the broader vacuolar lumen;0000331 the containing contractile vacuole;0031164 its membrane. Whole vacuole, its complex0062159 and spongiome0062160 are distinct. Same-PR public snapshot independently reread; original actual fetch time retained. |
| plaque-contractile-agent-SL-0320 | https://rest.uniprot.org/locations/SL-0320.json; Exact definition, synonym, direct isA/partOf and GO correspondences distinguished from nested ancestor objects | supports | SL0320 defines the contractile-vacuole compartment bounded by its membrane; exact contractile vacuolar lumen synonym, vacuolar-lumen parent and whole-vacuole parthood match. Nested SL0073 wording does not erase the separate GO whole/complex identities. |
| plaque-contractile-agent-go-lumen-search | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=contractile%20vacuole%20lumen&amp;limit=100; All100 returned first-page IDs and labels; exact query and total hit count | context_only | No exact contractile-vacuole-lumen label among this bounded returned page. Broader vacuolar lumen and specific unrelated lumina are not exact replacements. No exhaustive ontology absence is claimed. |
| plaque-contractile-agent-tax-2759 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759; Exact current taxId, scientificName, rank, lineage and alternative names | supports | Authority identifies Eukaryota 2759. Taxonomy alone does not establish occurrence, strain identity or numerical prevalence. Same-PR shared source timestamps, where applicable, are retained. |
| plaque-contractile-agent-tax-44030 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/44030; Exact current taxId, scientificName, rank, lineage and alternative names | supports | Authority identifies Paramecium multimicronucleatum 44030. Taxonomy alone does not establish occurrence, strain identity or numerical prevalence. Same-PR shared source timestamps, where applicable, are retained. |
| plaque-contractile-agent-tax-3055 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3055; Exact current taxId, scientificName, rank, lineage and alternative names | supports | Authority identifies Chlamydomonas reinhardtii 3055. Taxonomy alone does not establish occurrence, strain identity or numerical prevalence. Same-PR shared source timestamps, where applicable, are retained. |
| plaque-root24-sources-NCBITaxon-5911 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5911; Exact current taxId, scientificName, rank, lineage and alternative names | supports | Authority identifies Tetrahymena thermophila 5911. Taxonomy alone does not establish occurrence, strain identity or numerical prevalence. Same-PR shared source timestamps, where applicable, are retained. |
| plaque-copii-agent-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Exact current taxId, scientificName, rank, lineage and alternative names | supports | Authority identifies Saccharomyces cerevisiae 4932. Taxonomy alone does not establish occurrence, strain identity or numerical prevalence. Same-PR shared source timestamps, where applicable, are retained. |
| plaque-contractile-agent-more2024-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016%2Fj.ejop.2024.126078; Complete secondary-review abstract and exact title/authors/year/DOI metadata | supports | More2024 describes diversity and uneven occurrence of contractile vacuoles among eukaryotes, including freshwater/soil context. It is secondary abstract evidence, not an inspected full body or a quantitative prevalence census. Shared same-PR public snapshot independently inspected. |
| plaque-contractile-agent-allen2002-title | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=TITLE%3A%22Osmoregulation%20and%20contractile%20vacuoles%20of%20protozoa%22; Complete secondary-review abstract and exact title/DOI/authors/year metadata | supports | Allen/Naitoh2002 describes compartmental filling followed by periodic liquid discharge and distinct collecting/reservoir systems. It supports broad cyclic function, not a uniform architecture or exact component inventory across protists. Shared snapshot independently reread; body unavailable. |
| plaque-contractile-agent-gronlien2002-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1242%2Fjeb.205.20.3261; Complete primary abstract plus exact title/authors/year/DOI metadata | supports | Gronlien2002 used a microelectrode in the CV against a cytosolic reference in mechanically compressed Paramecium multimicronucleatum; measured filling-associated membrane-potential dynamics. The lumen example stays within that scope, without asserting universal species behavior or direct lumen osmolarity measurement. Primary abstract only. |
| plaque-contractile-agent-komsic2014-pmc-numeric | https://pmc.ncbi.nlm.nih.gov/articles/4248701/; Primary HTML Abstract, Introduction, Methods, Results, Discussion, Table1 and Figure1–9 captions as text; Results Water uptake into the CV reread directly from section3-4 | supports | Komsic2014 measures cell/CV sizes and contraction intervals across osmotic media in CC3395 and examines UVM4 derivatives. CV volume correlates with cell size/growth, not medium osmolarity; interval tracks osmolarity. Lumen osmolarity/permeability are modeled, not directly measured. The lumen wording describes measurements under altered osmolarity and separately osmolarity-responsive cycles, not a causal size–osmolarity relationship. Shared same-PR body independently read with original retrieval timestamp; no figure pixels, supplemental movies or raw-data reanalysis. |
| plaque-root24-sources-pore-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005856,GO:0031164,GO:0031913,GO:0098797; All four exact term identities/definitions; direct typed child relations, active status and GO0031913 definition PMID10503189 | supports | GO0031913 is the stable liquid-flow-regulating contractile vacuole pore. GO0098797 has the pore as an is_a child; GO0031164 and GO0005856 have it as a part_of child. Broad ontology complex classification does not supply an experimentally identified subunit inventory. |
| plaque-root24-sources-pore-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031913/ancestors?relations=is_a,part_of; Bounded is_a,part_of ancestor response as mixed closure | context_only | Mixed ancestor closure is only context. Exact relation types are checked against direct typed child entries in the separate four-term source, not inferred from this untyped ancestor list. |
| plaque-root24-sources-frankel2000-pmid | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID:10503189%20AND%20SRC:MED; Exact identifier query: title, authors, year, DOI/PMID and available abstract | supports | Bibliography verified: Cell biology of Tetrahymena thermophila.; Frankel J.; 2000. Primary/secondary body scopes are separately declared. Exact identifiers do not imply full-body access. |
| plaque-root24-sources-frankel2000-quoteddoi | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI:%2210.1016/S0091-679X(08)61528-9%22; Exact identifier query: title, authors, year, DOI/PMID and available abstract | supports | Bibliography verified: Cell biology of Tetrahymena thermophila.; Frankel J.; 2000. Primary/secondary body scopes are separately declared. Exact identifiers do not imply full-body access. |
| plaque-root24-sources-doi-10.1111_j.1550-7408.1973.tb03587.x | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1111/j.1550-7408.1973.tb03587.x; Exact identifier query: title, authors, year, DOI/PMID and available abstract | supports | Bibliography verified: Fine structure of the contractile vacuole pore in Paramecium.; McKanna JA.; 1973. Primary/secondary body scopes are separately declared. Exact identifiers do not imply full-body access. |
| plaque-copii-agent-PMID-9568718 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A9568718%20AND%20SRC%3AMED; Exact identifier query: title, authors, year, DOI/PMID and available abstract | supports | Bibliography verified: COPII-coated vesicle formation reconstituted with purified coat proteins and chemically defined liposomes.; Matsuoka K, Orci L, Amherdt M, Bednarek SY, Hamamoto S, Schekman R, Yeung T.; 1998. Primary/secondary body scopes are separately declared. Exact identifiers do not imply full-body access. |
| plaque-root24-sources-doi-10.1016_S0091-679X_08_61528-9 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/S0091-679X%2808%2961528-9; Actual zero-result response from unquoted DOI syntax; corrected quoted query separately succeeds | context_only | Zero hits from this syntax are an access/query limitation, not evidence that the DOI or chapter is absent. |
| plaque-root24-sources-frankel2000-university-pdf | https://chemotaxis.semmelweis.hu/CHTXhpg/Bookshelf/Tetrahymena/Tetrahymena_thermophila_Methods_2000.pdf; Genuine institutional book PDF: Chapter2 identity, complete II.F Contractile-Vacuole System pp51–52 and III.B.1.b Contractile Vacuole Pore and Cytoproct; opening V.B.1.b positioning paragraphs | supports | Secondary Frankel chapter on Tetrahymena thermophila describes persistent cortical discharge sites, circular/radial microtubules and apposed-membrane diaphragm. Tetrahymena thermophila is a review-supported model example; older cited work on T.pyriformis is not relabeled as new thermophila primary observations. Only named chapter sections, not the full book or figure pixels, were inspected. |
| plaque-root24-sources-mckanna1973-crossref | https://api.crossref.org/works/10.1111/j.1550-7408.1973.tb03587.x; Publisher-deposited complete primary synopsis/abstract, title, authors, journal, year and DOI | supports | McKanna1973 describes Paramecium pore cylindrical structure, diastolic diaphragm, systolic opening, contiguous membrane and microtubule annulus/radial bands. It supports genus-level structural context; the synopsis does not identify an experimental species or demonstrate a universal molecular pore inventory. Full article inaccessible. |
| plaque-copii-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030134,GO:0030135,GO:0030127,GO:0090114,GO:0006888,GO:0005789,GO:0005794,GO:0060205,GO:0012507; All nine requested active terms, definitions, synonyms and exact typed child relations | supports | GO0030134 identifies whole COPII-coated ER-to-Golgi vesicle;0030135 parent and0030127 coat distinction agree. GO0090114 is ER-membrane evagination in budding;0006888 is ER-to-Golgi transport, not the vesicle forming itself. GO0012507 membrane surrounds the ER-to-Golgi vesicle;0060205 is the broader cytoplasmic vesicle lumen. |
| plaque-copii-agent-SL-0322 | https://rest.uniprot.org/locations/SL-0322.json; Exact definition, complete synonyms, direct isA/partOf and direct GO crossreferences distinguished from nested parents | supports | SL0322 defines COPII-coated vesicle lumen, with Coat protein complexes II lumen and ER to Golgi transport vesicle lumen synonyms, cytoplasmic-vesicle-lumen parent and whole COPII-vesicle parthood. No direct exact GO crossreference is supplied. |
| plaque-copii-agent-go-lumen-candidates | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0106172,GO:0106173,GO:0106174; Exact active candidate terms0106172–0106174; labels, definitions and definition citations | supports | GO0106173 has exact COPII-coated vesicle lumen label but defines a COPII-coated endocytic vesicle interior, conflicting with this ER-to-Golgi scope. The active conflict remains unknown; the local SL-based identity is not forced into a semantically inconsistent GO term. No claim that the candidate is absent or resolved. |
| plaque-copii-agent-PMID-8004676 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A8004676%20AND%20SRC%3AMED; Complete primary abstract and exact bibliography | supports | Barlowe1994 reconstitutes ER budding using Sar1p, Sec13 complex and Sec23 complex. GTP-generated vesicles target/fuse with Golgi, whereas GMP-PNP vesicles fail targeting/fusion. Abstract supports coated transport intermediates and nucleotide-sensitive competence, not all synthetic vesicles being physiologically fusion-competent. Primary abstract only. |
| plaque-copii-agent-matsuoka1998-author | https://bednareklab.biochem.wisc.edu/wp-content/uploads/sites/1623/2022/02/1998_Matsuoka_etal_Cell.pdf; Genuine fresh institutional author PDF pp263–274: Summary, Introduction, Results, Discussion, Experimental Procedures, Tables1–2 and Figure1–8 captions as text | supports | Matsuoka1998 distinguishes native urea-washed ER microsome budding and defined synthetic-liposome reconstitution with Sar1p/Sec23-24/Sec13-31. Synthetic conditions and nucleotide analog are not universal in-vivo necessity. Figure8 luminal HPTS/DPX retention supports closure without rupture/resealing in the synthetic assay; it is not live-yeast lumen microscopy or proof of every cargo route. No figure pixel/raw-data reanalysis. |
| plaque-access-more2024-publisher | https://doi.org/10.1016/j.ejop.2024.126078; Actual native HTTP response and format/content examined solely for access tier | context_only | HTTP200. Redirect, challenge or error response is not an inspected scientific full body. Successful secondary Frankel and primary Matsuoka bodies are separately identified; other bounded claims retain abstract/synopsis tiers. |
| plaque-access-gronlien2002-publisher | https://doi.org/10.1242/jeb.205.20.3261; Actual native HTTP response and format/content examined solely for access tier | context_only | HTTP403. Redirect, challenge or error response is not an inspected scientific full body. Successful secondary Frankel and primary Matsuoka bodies are separately identified; other bounded claims retain abstract/synopsis tiers. |
| plaque-access-allen2002-publisher | https://doi.org/10.1016/S0074-7696(02)15015-7; Actual native HTTP response and format/content examined solely for access tier | context_only | HTTP200. Redirect, challenge or error response is not an inspected scientific full body. Successful secondary Frankel and primary Matsuoka bodies are separately identified; other bounded claims retain abstract/synopsis tiers. |
| plaque-root24-sources-frankel2000-publisher | https://www.sciencedirect.com/science/chapter/abs/pii/S0091679X08615289; Actual native HTTP response and format/content examined solely for access tier | context_only | HTTP403. Redirect, challenge or error response is not an inspected scientific full body. Successful secondary Frankel and primary Matsuoka bodies are separately identified; other bounded claims retain abstract/synopsis tiers. |
| plaque-root24-sources-frankel2000-api | https://api.elsevier.com/content/article/pii/S0091679X08615289?httpAccept=text/xml; Actual native HTTP response and format/content examined solely for access tier | context_only | HTTP200. Elsevier API supplies bibliographic metadata, not the scientific chapter body. Successful secondary Frankel and primary Matsuoka bodies are separately identified; other bounded claims retain abstract/synopsis tiers. |
| plaque-root24-sources-mckanna1973-publisher | https://onlinelibrary.wiley.com/doi/10.1111/j.1550-7408.1973.tb03587.x; Actual native HTTP response and format/content examined solely for access tier | context_only | HTTP403. Redirect, challenge or error response is not an inspected scientific full body. Successful secondary Frankel and primary Matsuoka bodies are separately identified; other bounded claims retain abstract/synopsis tiers. |
| plaque-root24-sources-mckanna1973-pdf | https://onlinelibrary.wiley.com/doi/pdf/10.1111/j.1550-7408.1973.tb03587.x; Actual native HTTP response and format/content examined solely for access tier | context_only | HTTP403. Redirect, challenge or error response is not an inspected scientific full body. Successful secondary Frankel and primary Matsuoka bodies are separately identified; other bounded claims retain abstract/synopsis tiers. |
| plaque-root24-sources-mckanna1973-tdm | https://api.wiley.com/onlinelibrary/tdm/v1/articles/10.1111%2Fj.1550-7408.1973.tb03587.x; Actual native HTTP response and format/content examined solely for access tier | context_only | HTTP400. Redirect, challenge or error response is not an inspected scientific full body. Successful secondary Frankel and primary Matsuoka bodies are separately identified; other bounded claims retain abstract/synopsis tiers. |
| plaque-copii-agent-barlowe1994-publisher | https://www.cell.com/article/0092867494901384/pdf; Actual native HTTP response and format/content examined solely for access tier | context_only | HTTP403. Redirect, challenge or error response is not an inspected scientific full body. Successful secondary Frankel and primary Matsuoka bodies are separately identified; other bounded claims retain abstract/synopsis tiers. |
| plaque-copii-agent-barlowe1994-sciencedirect | https://www.sciencedirect.com/science/article/pii/0092867494901384; Actual native HTTP response and format/content examined solely for access tier | context_only | HTTP403. Redirect, challenge or error response is not an inspected scientific full body. Successful secondary Frankel and primary Matsuoka bodies are separately identified; other bounded claims retain abstract/synopsis tiers. |
| plaque-catalogue | https://imodulondb.org/api/datasets; Complete current /api/datasets response, all20 organism rows and their dataset lists; no pagination | supports | No dataset organism matches Saccharomyces cerevisiae, Chlamydomonas reinhardtii, Paramecium or Tetrahymena. Downstream matched-organism searches/summaries therefore do not apply. Unrelated bacterial/archaeal catalogue contexts and absence from this database cannot establish biological absence. |
| plaque-historical-runner | /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources imodulondb datasets; Historical00:49Z receipt and exact stdout/stderr independently reread and hash-verified | context_only | Historical runner exited1 before datasets due OS PermissionError reading pyvenv.cfg. Not a fresh invocation or successful execution; current official catalogue is source fallback. |
| plaque-original-checks | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/adversary-plaque/original-checks.json; Four read-only native validate/render executions and every historical frozen input at original source revision | supports | All four validate and Markdown is byte-exact. Historical inputs18/17/12/12 all match; all four current target hashes unchanged. Original findings/actions empty. |
| plaque-native-contractile_vacuole_lumen-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/contractile_vacuole_lumen.yaml --verify; Actual root-owned native command receipt and stdout independently read/hash-verified | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| plaque-native-contractile_vacuole_lumen-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/contractile_vacuole_lumen.yaml --causal-graphs; Actual root-owned native command receipt and stdout independently read/hash-verified | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| plaque-native-contractile_vacuole_pore-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/contractile_vacuole_pore.yaml --verify; Actual root-owned native command receipt and stdout independently read/hash-verified | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| plaque-native-contractile_vacuole_pore-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/contractile_vacuole_pore.yaml --causal-graphs; Actual root-owned native command receipt and stdout independently read/hash-verified | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| plaque-native-copii_coated_er_to_golgi_transport_vesicle-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/copii_coated_er_to_golgi_transport_vesicle.yaml --verify; Actual root-owned native command receipt and stdout independently read/hash-verified | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| plaque-native-copii_coated_er_to_golgi_transport_vesicle-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/copii_coated_er_to_golgi_transport_vesicle.yaml --causal-graphs; Actual root-owned native command receipt and stdout independently read/hash-verified | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| plaque-native-copii_coated_vesicle_lumen-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/copii_coated_vesicle_lumen.yaml --verify; Actual root-owned native command receipt and stdout independently read/hash-verified | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| plaque-native-copii_coated_vesicle_lumen-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/copii_coated_vesicle_lumen.yaml --causal-graphs; Actual root-owned native command receipt and stdout independently read/hash-verified | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| micro-review-policy | .claude/skills/review-yaml-record/SKILL.md; Complete native record-review workflow and structured-source applicability reread | context_only | Actual molecular/pathway narratives trigger applicability assessment even without expression claims. No unmatched dataset or empty query establishes biological absence. |
| micro-review-config | conf/record_review.yaml; Complete current native configuration reread | context_only | Declared routes and four local rubrics remain unchanged. The authoritative configuration is included among frozen inputs. |
| micro-review-profile | docs/record-review-profile.md; Complete local profile reread; related shared contract and common frozen policy bytes checked against prior inspected versions | context_only | Mixed issue-bearing cohorts may retain qualified positive assessments. No record mutation, status promotion, fabricated finding or terminal predecessor disposition follows from a clean assessment. |
| micro-review-checklist | .claude/skills/curate-yaml-record/references/review-checklist.md; Complete field-by-field rubric reread | context_only | Identity, taxon, claim-level source scope, exact partonomy and supported directed edges assessed separately from validation. |
| micro-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Complete scope and graph contract reread; unchanged add-cell-structure graph policy and native schema retained | context_only | NONMECHANISTIC topology and destination descriptions do not establish fusion machinery, kinetic mechanism or specific assembly necessity. |
| micro-native-schema | src/cellstructuremech/schema/cellstructuremech.yaml; Previously inspected unchanged EssentialityEnum, CausalNode.component_ref and source-scope rules | context_only | Collective lipid bilayer constitution is distinct from necessity of individual lipid species; a membrane defined as that bilayer may use its collective component_ref. |
| micro-review-schema | schema/record_review.yaml; Unchanged native schema checked through actual original and scratch-envelope validation | context_only | Native assessment area schema; bounded search_scope; complete lineage if a finding is present. No original scientific finding exists in these three bundles. |
| micro-neighbor-copi_vesicle_coat | data/structures/other/copi_vesicle_coat.yaml; Only identifier, label, definition, kind, hierarchy/parthood and component identifier/label/type/role/grounding fields | supports | Frozen before read. Boundary context for coat versus vesicle, bilayer donor and ER destination; other scientific claims and any neighbor findings are not reviewed or resolved. |
| micro-neighbor-endoplasmic_reticulum | data/structures/membrane_organelle/endoplasmic_reticulum.yaml; Only identifier, label, definition, kind, hierarchy/parthood and component identifier/label/type/role/grounding fields | supports | Frozen before read. Boundary context for coat versus vesicle, bilayer donor and ER destination; other scientific claims and any neighbor findings are not reviewed or resolved. |
| micro-neighbor-golgi_membrane | data/structures/membrane_organelle/golgi_membrane.yaml; Only identifier, label, definition, kind, hierarchy/parthood and component identifier/label/type/role/grounding fields | supports | Frozen before read. Boundary context for coat versus vesicle, bilayer donor and ER destination; other scientific claims and any neighbor findings are not reviewed or resolved. |
| micro-record-copi_coated_vesicle | data/structures/membrane_organelle/copi_coated_vesicle.yaml; Complete current YAML at 7081777bba0daacfa48fc6d826cdfd7138e751b4 | supports | All current fields, history, definition, relations, examples, functions, evidence, graph edges and discussions read. The whole-vesicle history and destination edge changed; all other content remains identical. |
| micro-prior-copi_coated_vesicle | reviews/structured/20261022T005255Z-copi-coated-vesicle-audit/review.yaml; Entire immutable original YAML, derived Markdown and native validation/render | supports | Original qualified scientific pass has no findings/actions. Its expression-only adapter exclusion is insufficient under native policy. Historical checks retain their actual dates; none is recertified as current. |
| micro-record-copi_coated_vesicle_lumen | data/structures/membrane_organelle/copi_coated_vesicle_lumen.yaml; Complete current YAML at 7081777bba0daacfa48fc6d826cdfd7138e751b4 | supports | All current fields, history, definition, relations, examples, functions, evidence, graph edges and discussions read. Original target hash remains current. |
| micro-prior-copi_coated_vesicle_lumen | reviews/structured/20261022T005255Z-copi-coated-vesicle-lumen-audit/review.yaml; Entire immutable original YAML, derived Markdown and native validation/render | supports | Original qualified scientific pass has no findings/actions. Its expression-only adapter exclusion is insufficient under native policy. Historical checks retain their actual dates; none is recertified as current. |
| micro-record-copi_coated_vesicle_membrane | data/structures/membrane_organelle/copi_coated_vesicle_membrane.yaml; Complete current YAML at 7081777bba0daacfa48fc6d826cdfd7138e751b4 | supports | All current fields, history, definition, relations, examples, functions, evidence, graph edges and discussions read. Original target hash remains current. |
| micro-prior-copi_coated_vesicle_membrane | reviews/structured/20261022T005256Z-copi-coated-vesicle-membrane-audit/review.yaml; Entire immutable original YAML, derived Markdown and native validation/render | supports | Original qualified scientific pass has no findings/actions. Its expression-only adapter exclusion is insufficient under native policy. Historical checks retain their actual dates; none is recertified as current. |
| micro-original-validation-inputs | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/adversary-microtubule/original-validation-inputs.json; Three original native validate/render commands and original/source/HEAD SHA256 comparisons | supports | All original pairs validate and render byte-identically. Exactly the whole COPI vesicle input is stale; lumen and membrane hashes remain equal. |
| micro-stale-diff | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/adversary-microtubule/copi-stale.diff; Exact original frozen source 9c0446c4c0dd4b458787c43a499e4ceab5e179a6 to 7081777bba0daacfa48fc6d826cdfd7138e751b4 target diff | supports | Only one curation-history event and the process-to-ER destination edge were added. Current reassessment is substantive; original immutable graph assessment covers five edges, current graph six. |
| micro-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030137,GO:0005798,GO:0030135,GO:0030126,GO:0030663,GO:0006890,GO:0035964,GO:0000139,GO:0005783,GO:0060205,GO:0030660,GO:0030662,GO:0106172; All 13 exact returned terms: active status, names, definitions, synonyms and relevant is_a/part_of children | supports | Exact whole-vesicle/membrane identities and hierarchy remain valid. GO0006890 explicitly describes directed substances Golgi to ER, including COPI; GO0035964 defines Golgi evagination. GO0106172 still adds an endocytic qualifier. Coatomer is related for whole vesicle and exact for coat; coating parthood is not direct lipid constituency. |
| micro-SL-0321 | https://rest.uniprot.org/locations/SL-0321.json; Complete exact SL-0321 identity/definition, isA and partOf entries with GO mappings | supports | Defines the general COPI vesicle compartment bounded by its membrane, under cytoplasmic-vesicle lumen and part of COPI vesicle. The zero annotated protein count is not biological absence. The surrounding structures and the lumen remain distinct. |
| micro-NCBITaxon-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Exact taxId/scientificName/rank/lineage | supports | Current authority identifies Saccharomyces cerevisiae at species rank. It does not establish a strain, prevalence or mechanism. |
| micro-sandmann2003-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1091%2Fmbc.e02-11-0736; Exact DOI10.1091/mbc.e02-11-0736, PMID12925749, authors and complete primary abstract | partial | The yeast study reports coatomer-mutant suppression and KKXX-dependent binding/vesicle results; actual assays and their limits are assessed from the body. |
| micro-sandmann2003-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC181553/; Fresh genuine PMC HTML: complete abstract and Introduction sec1; Methods sec3 including Table1, sec7 Protein-binding Assay, sec14 Budding Assay; complete Results sec16 and sec20–23 including captions Figures1,5–7; complete Discussion sec25 | supports | Yeast suppression, binding and vesicle assays support the stated early-secretory COPI context. Cytosol-only experiments cannot separate COPI/COPII; purified-coat assays can. Cargo packaging and proposed regulatory mechanisms remain qualified. Neither lipid flux nor the lumen was separately quantified; no pixels/raw data were reanalysed. |
| micro-sandmann2003-jats | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC181553/fullTextXML; Actual HTTP500 XML response only | context_only | XML route was unavailable; independently obtained genuine PMC HTML supplied the inspected body. This response provides no scientific support. |
| micro-waters1991-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1038%2F349248a0; Exact DOI10.1038/349248a0, PMID1898986, authors and complete primary abstract | partial | Purified cytosolic coatomer contains Golgi transport-vesicle coat proteins. This supports historical coat-complex naming rather than a yeast-specific experiment, universal modern stoichiometry or whole-vesicle synonym. |
| micro-waters1991-publisher | https://www.nature.com/articles/349248a0; HTTP200 body is a Client Challenge page, not article or abstract | context_only | Current publisher response supplies no scientific text. Only the separately inspected complete primary abstract is used; no present full-body access claimed. |
| micro-go0106172-ols | https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FGO_0106172; Complete exact GO0106172 OLS entry, active status, description, definition citation and creation provenance | supports | OLS independently repeats the endocytic qualifier. This unresolved authority wording prevents an unqualified exact mapping of the broader SL-0321/local general lumen target. |
| micro-lumen-citation-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A29535154%20AND%20SRC%3AMED; PMID29535154 / DOI10.1242/jcs.209890; complete abstract and bibliographic type Review | context_only | Arakel and Schwappach2018 is secondary literature: its abstract describes COPI lipid/protein sorting and Golgi-to-ER retrieval. Context only; it does not resolve the GO endocytic qualifier and no body/poster was read. |
| micro-lumen-search | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=COPI-coated%20vesicle%20lumen&amp;limit=100&amp;page=1; Current QuickGO literal query COPI-coated vesicle lumen; first100 returned IDs/names; exact candidate inspected separately | supports | Same-label GO0106172 is present, but its definition remains narrower/inconsistent. No exhaustive absence is asserted. |
| micro-catalogue | https://imodulondb.org/api/datasets; Complete official GET /api/datasets response: all returned organism identifiers/names and dataset arrays | supports | Returned catalogue has no Saccharomyces cerevisiae dataset. No matched downstream gene/module query applies; absence is catalogue coverage only. E. coli recombinant expression in a source is not the yeast structure taxon. |
| micro-doi-10.1016_j.cell.2012.01.015 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.cell.2012.01.015; Exact metadata and complete primary abstract; DOI10.1016/j.cell.2012.01.015; title A structure-based mechanism for Arf1-dependent recruitment of coatomer to membranes.; retained actual 10:50Z snapshot from immediately prior review, hash reverified; declared prior sections retained and Introduction reread here | partial | Complete primary abstract reports Arf1/coatomer structural and biochemical recruitment model. Actual mammalian/yeast construct scopes and model limits are retained in the separately inspected body. No fresh download or broader Methods/figure scope is claimed. |
| micro-yu2012-s3 | https://pmc-oa-opendata.s3.amazonaws.com/PMC3285272.1/PMC3285272.1.xml; DOI10.1016/j.cell.2012.01.015; complete Introduction; Results Experimental Approach and A Model for Arf1-Dependent Recruitment of Coatomer to Membranes; retained actual 10:50Z snapshot from immediately prior review, hash reverified; declared prior sections retained and Introduction reread here | supports | Genuine primary JATS. Mammalian coatomer subcomplexes with defined human/yeast truncated Arf1 constructs support a bounded recruitment model. COPI, COPII and clathrin/AP systems are distinguished; proposed conformational effects remain proposals. Not direct accession-specific evidence for every yeast coat example, nor complete Methods/raw-data audit. No fresh download or broader Methods/figure scope is claimed. |
| micro-historical-adapter-runner | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Retained actual 00:49Z invocation receipt; no current runner execution | context_only | Historical adapter invocation failed with PermissionError accessing pyvenv.cfg. Native policy permits inspected-source fallback; current catalogue evidence is separate. This is not a new failure or successful runner execution. |
| micro-native-copi_coated_vesicle-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/copi_coated_vesicle-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/copi_coated_vesicle.yaml --verify; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/copi_coated_vesicle-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0 at current source, 2026-11-03T11:16:59.603974+00:00 to 2026-11-03T11:16:59.992031+00:00. Empty protein-example inventory and zero GENE_OR_PROTEIN nodes. This does not verify narrative proteins, source taxon, pathway mechanism or formation necessity. |
| micro-native-copi_coated_vesicle-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/copi_coated_vesicle-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/copi_coated_vesicle.yaml --causal-graphs; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/copi_coated_vesicle-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Actual exit0 at current source, 2026-11-03T11:17:00.026285+00:00 to 2026-11-03T11:17:00.429865+00:00. Empty protein-example inventory and zero GENE_OR_PROTEIN nodes. This does not verify narrative proteins, source taxon, pathway mechanism or formation necessity. |
| micro-native-copi_coated_vesicle_lumen-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/copi_coated_vesicle_lumen-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/copi_coated_vesicle_lumen.yaml --verify; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/copi_coated_vesicle_lumen-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0 at current source, 2026-11-03T11:17:00.462678+00:00 to 2026-11-03T11:17:00.846573+00:00. Empty protein-example inventory and zero GENE_OR_PROTEIN nodes. This does not verify narrative proteins, source taxon, pathway mechanism or formation necessity. |
| micro-native-copi_coated_vesicle_lumen-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/copi_coated_vesicle_lumen-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/copi_coated_vesicle_lumen.yaml --causal-graphs; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/copi_coated_vesicle_lumen-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Actual exit0 at current source, 2026-11-03T11:17:00.878680+00:00 to 2026-11-03T11:17:01.260228+00:00. Empty protein-example inventory and zero GENE_OR_PROTEIN nodes. This does not verify narrative proteins, source taxon, pathway mechanism or formation necessity. |
| micro-native-copi_coated_vesicle_membrane-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/copi_coated_vesicle_membrane-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/copi_coated_vesicle_membrane.yaml --verify; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/copi_coated_vesicle_membrane-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0 at current source, 2026-11-03T11:17:01.291893+00:00 to 2026-11-03T11:17:01.675302+00:00. Empty protein-example inventory and zero GENE_OR_PROTEIN nodes. This does not verify narrative proteins, source taxon, pathway mechanism or formation necessity. |
| micro-native-copi_coated_vesicle_membrane-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/copi_coated_vesicle_membrane-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/copi_coated_vesicle_membrane.yaml --causal-graphs; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/copi_coated_vesicle_membrane-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Actual exit0 at current source, 2026-11-03T11:17:01.708657+00:00 to 2026-11-03T11:17:02.086997+00:00. Empty protein-example inventory and zero GENE_OR_PROTEIN nodes. This does not verify narrative proteins, source taxon, pathway mechanism or formation necessity. |
| septin-review-policy | .claude/skills/review-yaml-record/SKILL.md; Structured Source Cross-Checks and immutable review workflow | supports | Actual molecular and osmoregulatory pathway/response assertions merit applicability assessment; absence of expression claims is not an exemption. Missing organism coverage is not negative biology. |
| septin-curation-policy | docs/CURATION.md; Structure identity, protein examples, constituent evidence, source scope | supports | Protein identity does not establish constituent localization or necessity. Substructure, material, functional protein class and complete organelle are distinct. |
| septin-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; NONMECHANISTIC topology, evidence, protein anchoring and process endpoints | supports | Protein nodes and typed anatomical nodes must retain their source scope; a NONMECHANISTIC label does not turn a model or speculative mechanism into direct experimental proof. |
| septin-record-contractile_vacuolar_membrane | data/structures/membrane_organelle/contractile_vacuolar_membrane.yaml; Entire current maintained record at 7081777bba0daacfa48fc6d826cdfd7138e751b4 | supports | Full identity, history, synonymy, definition, component/gene/protein examples, taxon examples, function, every graph edge, evidence and discussions read. No attached image, numerical physical property or verbatim snippet is declared. |
| septin-original-contractile_vacuolar_membrane | reviews/structured/20261022T005251Z-contractile-vacuolar-membrane-audit/review.yaml; Entire original YAML/Markdown observation; source hashes, checks, evidence tiers, assessments, findings/actions and limitations | supports | Historical record bytes remain current. Whole vacuole has F1 major and F2/F3 minor open findings; membrane and complex have no scientific findings. No historical source access or gate is reclassified as current execution. |
| septin-original-validation-contractile_vacuolar_membrane | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/adversary-septin/original-checks.json; 20261022T005251Z-contractile-vacuolar-membrane-audit native validate/render and source/current frozen-hash comparison | supports | Both original commands exit0 and rendered Markdown is byte-identical. Historical source bytes equal original frozen/current target hashes. |
| septin-native-contractile_vacuolar_membrane-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/contractile_vacuolar_membrane-uniprot-verify-receipt.json; Actual root command receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/contractile_vacuolar_membrane-uniprot-verify.log | supports | Exit0. No protein examples or UniProtKB protein xrefs. The two protein nodes comprise one NO_GENE_SYMBOLS aquaporin component and one UNANCHORED_NO_UNIPROT perivacuolar V-ATPase context node. Exit0 does not verify species-specific identity, localization or necessity. |
| septin-native-contractile_vacuolar_membrane-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/contractile_vacuolar_membrane-uniprot-causal-receipt.json; Actual root command receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/contractile_vacuolar_membrane-uniprot-causal.log | supports | Exit0. No protein examples or UniProtKB protein xrefs. The two protein nodes comprise one NO_GENE_SYMBOLS aquaporin component and one UNANCHORED_NO_UNIPROT perivacuolar V-ATPase context node. Exit0 does not verify species-specific identity, localization or necessity. |
| septin-record-contractile_vacuole | data/structures/membrane_organelle/contractile_vacuole.yaml; Entire current maintained record at 7081777bba0daacfa48fc6d826cdfd7138e751b4 | supports | Full identity, history, synonymy, definition, component/gene/protein examples, taxon examples, function, every graph edge, evidence and discussions read. No attached image, numerical physical property or verbatim snippet is declared. |
| septin-original-contractile_vacuole | reviews/structured/20261022T005252Z-contractile-vacuole-audit/review.yaml; Entire original YAML/Markdown observation; source hashes, checks, evidence tiers, assessments, findings/actions and limitations | supports | Historical record bytes remain current. Whole vacuole has F1 major and F2/F3 minor open findings; membrane and complex have no scientific findings. No historical source access or gate is reclassified as current execution. |
| septin-original-validation-contractile_vacuole | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/adversary-septin/original-checks.json; 20261022T005252Z-contractile-vacuole-audit native validate/render and source/current frozen-hash comparison | supports | Both original commands exit0 and rendered Markdown is byte-identical. Historical source bytes equal original frozen/current target hashes. |
| septin-native-contractile_vacuole-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/contractile_vacuole-uniprot-verify-receipt.json; Actual root command receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/contractile_vacuole-uniprot-verify.log | supports | Exit0. Six protein examples verify. The V-ATPase node is COVERED by four examples; the aquaporin node is PARTIAL_EXAMPLES with MIP1 missing. This is inventory/identity coverage, not proof that aqpA/aqpB reside in a CV or that MIP1 lacks a biological counterpart. |
| septin-native-contractile_vacuole-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/contractile_vacuole-uniprot-causal-receipt.json; Actual root command receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/contractile_vacuole-uniprot-causal.log | supports | Exit0. Six protein examples verify. The V-ATPase node is COVERED by four examples; the aquaporin node is PARTIAL_EXAMPLES with MIP1 missing. This is inventory/identity coverage, not proof that aqpA/aqpB reside in a CV or that MIP1 lacks a biological counterpart. |
| septin-record-contractile_vacuole_complex | data/structures/membrane_organelle/contractile_vacuole_complex.yaml; Entire current maintained record at 7081777bba0daacfa48fc6d826cdfd7138e751b4 | supports | Full identity, history, synonymy, definition, component/gene/protein examples, taxon examples, function, every graph edge, evidence and discussions read. No attached image, numerical physical property or verbatim snippet is declared. |
| septin-original-contractile_vacuole_complex | reviews/structured/20261022T005253Z-contractile-vacuole-complex-audit/review.yaml; Entire original YAML/Markdown observation; source hashes, checks, evidence tiers, assessments, findings/actions and limitations | supports | Historical record bytes remain current. Whole vacuole has F1 major and F2/F3 minor open findings; membrane and complex have no scientific findings. No historical source access or gate is reclassified as current execution. |
| septin-original-validation-contractile_vacuole_complex | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/adversary-septin/original-checks.json; 20261022T005253Z-contractile-vacuole-complex-audit native validate/render and source/current frozen-hash comparison | supports | Both original commands exit0 and rendered Markdown is byte-identical. Historical source bytes equal original frozen/current target hashes. |
| septin-native-contractile_vacuole_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/contractile_vacuole_complex-uniprot-verify-receipt.json; Actual root command receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/contractile_vacuole_complex-uniprot-verify.log | supports | Exit0. Empty protein example/xref inventory and zero GENE_OR_PROTEIN nodes. Exit0 does not independently validate the molecular details intentionally assigned to child records or the osmoregulatory pathway. |
| septin-native-contractile_vacuole_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/contractile_vacuole_complex-uniprot-causal-receipt.json; Actual root command receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/contractile_vacuole_complex-uniprot-causal.log | supports | Exit0. Empty protein example/xref inventory and zero GENE_OR_PROTEIN nodes. Exit0 does not independently validate the molecular details intentionally assigned to child records or the osmoregulatory pathway. |
| septin-context-spongiome | data/structures/membrane_organelle/spongiome.yaml; Only identity, definition, structure_kind, parent_structures, part_of and has_part | supports | Frozen before inspection; boundary context only. No independent whole-neighbor review, molecular accession verification or terminal disposition of its findings is asserted. |
| septin-context-contractile_vacuole_lumen | data/structures/membrane_organelle/contractile_vacuole_lumen.yaml; Only identity, definition, structure_kind, parent_structures, part_of and has_part | supports | Frozen before inspection; boundary context only. No independent whole-neighbor review, molecular accession verification or terminal disposition of its findings is asserted. |
| septin-context-contractile_vacuole_pore | data/structures/membrane_organelle/contractile_vacuole_pore.yaml; Only identity, definition, structure_kind, parent_structures, part_of and has_part | supports | Frozen before inspection; boundary context only. No independent whole-neighbor review, molecular accession verification or terminal disposition of its findings is asserted. |
| septin-contractile-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031164,GO:0005774,GO:0000331,GO:0062159,GO:0062160,GO:0043232,GO:0005775,GO:0031913,GO:0098797,GO:0005856; All ten returned exact terms: active identities, definitions, synonyms and relevant typed child relations; unrelated child branches not used | supports | Membrane GO0031164, vacuole GO0000331, whole complex GO0062159 and spongiome GO0062160 are distinct. Membrane is a vacuolar-membrane subtype and vacuole part; whole vacuole and spongiome are complex parts. GO calls central bladder related, not exact; CVC is also related for the complex. Complex definition and GO0043232 parent are non-membrane-bounded at composite-system scope. |
| septin-contractile-agent-ancestors-0031164 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031164/ancestors?relations=is_a,part_of; Complete requested is_a/part_of ancestor closure for exact target | supports | Corroborates native hierarchy; ancestor closure is not a direct molecular mechanism or every individual immediate parent relation. |
| septin-contractile-agent-ancestors-0000331 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000331/ancestors?relations=is_a,part_of; Complete requested is_a/part_of ancestor closure for exact target | supports | Corroborates native hierarchy; ancestor closure is not a direct molecular mechanism or every individual immediate parent relation. |
| septin-contractile-agent-ancestors-0062159 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0062159/ancestors?relations=is_a,part_of; Complete requested is_a/part_of ancestor closure for exact target | supports | Corroborates native hierarchy; ancestor closure is not a direct molecular mechanism or every individual immediate parent relation. |
| septin-contractile-agent-go-vacuole-parent | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005773; Exact GO0005773 definition and relevant direct child GO0000331 | supports | GO confirms contractile vacuole as a vacuole subtype. Omission of this optional explicit maintained parent does not change the exact GO identity or by itself establish a concrete review defect. |
| septin-contractile-agent-go-vatpase | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0016471; Exact GO0016471 active identity, definition and V1/V0 parts | supports | Native term denotes the broad vacuolar proton-transporting V-type ATPase complex. It is a source-neutral candidate class, not direct proof of CV membership or exact cross-lineage CV-localized subset identity. |
| septin-contractile-agent-SL-0073 | https://rest.uniprot.org/locations/SL-0073.json; Native id/name/definition, synonyms, exact GO mapping and immediate isA/partOf | supports | SL0073 maps to GO0000331 and includes CV among its synonyms. Its prose also describes the whole CVC apparatus; that broader prose is not substituted for the precise GO0000331 bladder/GO0062159 complex distinction. |
| septin-contractile-agent-SL-0074 | https://rest.uniprot.org/locations/SL-0074.json; Native id/name/definition, synonyms, exact GO mapping and immediate isA/partOf | supports | SL0074 maps exactly to GO0031164 with contractile vacuolar membrane synonym, vacuole-membrane parent and contractile-vacuole partOf. Its introductory complex wording is not used to merge anatomical levels. |
| septin-contractile-agent-tax-2759 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759; Complete taxId, scientificName, rank and lineage | supports | Native taxon2759 is Eukaryota (domain). This is identity verification, not experiment-specific strain or prevalence evidence. |
| septin-contractile-agent-tax-5775 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5775; Complete taxId, scientificName, rank and lineage | supports | Native taxon5775 is Amoeba proteus (species). This is identity verification, not experiment-specific strain or prevalence evidence. |
| septin-contractile-agent-tax-44689 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/44689; Complete taxId, scientificName, rank and lineage | supports | Native taxon44689 is Dictyostelium discoideum (species). This is identity verification, not experiment-specific strain or prevalence evidence. |
| septin-contractile-agent-tax-3055 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3055; Complete taxId, scientificName, rank and lineage | supports | Native taxon3055 is Chlamydomonas reinhardtii (species). This is identity verification, not experiment-specific strain or prevalence evidence. |
| septin-contractile-agent-tax-5693 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5693; Complete taxId, scientificName, rank and lineage | supports | Native taxon5693 is Trypanosoma cruzi (species). This is identity verification, not experiment-specific strain or prevalence evidence. |
| septin-contractile-agent-tax-44030 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/44030; Complete taxId, scientificName, rank and lineage | supports | Native taxon44030 is Paramecium multimicronucleatum (species). This is identity verification, not experiment-specific strain or prevalence evidence. |
| septin-contractile-agent-more2024-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016%2Fj.ejop.2024.126078; Europe PMC exact cited DOI or PMID/title result: complete abstract plus title/authors/identifiers/journal/date | supports | Secondary review abstract describes patchy eukaryotic occurrence and variable CV structure/function/machinery. No numerical all-Eukaryota frequency or specific aqpA/aqpB localization is established by this abstract. |
| septin-contractile-agent-nishihara2008-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1042%2FBC20070091; Europe PMC exact cited DOI or PMID/title result: complete abstract plus title/authors/identifiers/journal/date | supports | Complete primary abstract identifies Amoeba ApAQP, oocyte water-channel function and immunolocalization to CV membrane/perivacuolar vesicles. V-ATPase is detected on surrounding vesicle membranes; osmotic-gradient generation is an interpretation/hypothesis, not direct localization of all pumps to the single CV bilayer. |
| septin-contractile-agent-clarke2002-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1242%2Fjcs.115.14.2893; Europe PMC exact cited DOI or PMID/title result: complete abstract plus title/authors/identifiers/journal/date | supports | Complete primary abstract identifies Dictyostelium VatM-GFP targeting and assembly-competent V-ATPase at CV and endolysosomal membranes, with distinct vesiculotubular/endosomal dynamics. This does not establish uniform density of every subunit in every bladder or require a complete systole force model. |
| septin-contractile-agent-rohloff2004-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1074%2Fjbc.M410372200; Europe PMC exact cited DOI or PMID/title result: complete abstract plus title/authors/identifiers/journal/date | supports | Complete primary abstract supports T. cruzi acidocalcisome/CVC involvement in hypo-osmotic volume recovery, aquaporin translocation and isolated bladder proton transport. This is not proof of identical response machinery in every protist. |
| septin-contractile-agent-allen2002-title | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=TITLE%3A%22Osmoregulation%20and%20contractile%20vacuoles%20of%20protozoa%22; Europe PMC exact cited DOI or PMID/title result: complete abstract plus title/authors/identifiers/journal/date | supports | Secondary review abstract explicitly distinguishes pump-rich vesiculotubular membrane from a reservoir membrane lacking V-ATPase holoenzymes, and describes filling/rounding/discharge. Broad cycle support is not an assay of individual channel membership or a universally settled contraction mechanism. |
| septin-contractile-agent-bulow2012-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A22262860%20AND%20SRC%3AMED; Europe PMC exact cited DOI or PMID/title result: complete abstract plus title/authors/identifiers/journal/date | supports | Complete primary abstract distinguishes wild-type AqpB with no detected water/glycerol/urea conductance in tested oocytes from the active loop-deletion mutant. GFP constructs label unspecified vacuoles, plasma membrane and protrusions; osmoregulatory relevance is tentative. |
| septin-contractile-agent-aqpA2000-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A10876090%20AND%20SRC%3AMED; Europe PMC exact cited DOI or PMID/title result: complete abstract plus title/authors/identifiers/journal/date | supports | Mitra et al.2000 complete primary abstract describes developmentally regulated aqpA, prespore expression and loss of prolonged spore viability/dormancy. It does not experimentally locate AqpA to contractile vacuoles. |
| septin-contractile-agent-nolta1994-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A8294479%20AND%20SRC%3AMED; Europe PMC exact cited DOI or PMID/title result: complete abstract plus title/authors/identifiers/journal/date | supports | Complete primary abstract describes purified Dictyostelium bladder and spongiome membranes, pump-rich spongiome and pump-poor bladders, with possible primary energy-transduction role. This supports bipartite complex scope; pump-poor does not mean complete absence. |
| septin-contractile-agent-gronlien2002-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1242%2Fjeb.205.20.3261; Europe PMC exact cited DOI or PMID/title result: complete abstract plus title/authors/identifiers/journal/date | supports | Complete primary abstract reports Paramecium multimicronucleatum microelectrode potentials, osmotic adaptation, decorated radial-arm V-ATPase labeling and concanamycin effects. It supports electrogenic spongiome/fluid segregation in that ciliate; functional inhibition is not an organelle-formation knockout. |
| septin-contractile-agent-komsic2014-pmc-numeric | https://pmc.ncbi.nlm.nih.gov/articles/4248701/; Genuine current PMC4248701 HTML: Abstract; Methods Strains used; Results Osmoregulation in CC3395, Regulation of CV activity, Water uptake into CV, Aquaporins in Chlamydomonas and MIP1 localization; Discussion Aquaporins and CV function; associated Table1 and captions as text | supports | Direct Results distinguish CV size/cell-size relation from contraction-interval/medium-osmolarity relation; cell and CV size were not correlated with medium osmotic strength. CC3395/UVM4-derived reporter strains and adaptation conditions are explicit. MIP1 immunogold/GFP localization supports CV association; lumen osmolarity and permeability are modeled, not directly measured, and GFP fusion functionality is questioned. These primary data do not establish Dictyostelium aqpA/aqpB membership or wild-type MIP1 water conductance by a separate direct assay. |
| septin-contractile-agent-bulow2012-pmc-numeric | https://pmc.ncbi.nlm.nih.gov/articles/3293572/; Genuine current PMC3293572 HTML: complete Abstract, Results and Discussion, including Figures2–4 captions as text; no full Experimental Procedures or pixels claimed | supports | AqpB was cloned from D.discoideum AX2 amoebae. Tested wild-type/tagged or untagged variants did not conduct water above controls in oocytes; Δ208–219 did in oocytes and proteoliposomes. Anti-AqpB antiserum was unsuitable for immunolocalization, so N/C-terminal GFP constructs were used. Results call observed structures vacuolar, not identified CVs; Discussion explicitly suggests a CV-like function by analogy. This supports the bounded inherited membership finding, not biological absence. |
| septin-contractile-agent-docampo2013-s3 | https://pmc-oa-opendata.s3.amazonaws.com/PMC3818246.1/PMC3818246.1.xml; Genuine current JATS PMC3818246: sections3.3 History (source label),3.2 Structure and composition,3.4 Role in osmoregulation only; no image pixels or cited-primary-paper audit | supports | Secondary synthesis distinguishes central bladder and surrounding spongiome, compiles lineage-specific pumps/channels and describes uncertain/alternative osmolyte and contraction models. Anatomical organization and general water-expulsion context are supported; the synthesis is not direct evidence for all named proteins or every proposed mechanistic step. |
| septin-contractile-agent-aquaporin-family | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000425/; Exact accession/name/type, complete non-LLM description and family hierarchy; description llm flags false | supports | IPR000425 Major intrinsic protein is a diverse family including aquaporins and glycerol facilitators; it is broader than a CV-localized functional subset. |
| septin-contractile-agent-aquaporin-transporter | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR034294/; Exact accession/name/type, complete non-LLM description and family hierarchy; description llm flags false | supports | IPR034294 Aquaporin transporter represents orthodox aquaporins, not every algal/protist MIP subgroup or the CV-localized subset. A generic family match is not structure-localization evidence. |
| septin-contractile-agent-UniProtKB-P54647 | https://rest.uniprot.org/uniprotkb/P54647.json; Exact reviewed accession, gene tokens, protein name, organism, functional/subcellular comments and evidence codes | supports | Current reviewed P54647 identifies vatA in Dictyostelium taxon44689. Pump subunit identity/complex role is verified; location comments and evidence codes are distinguished from a direct assay of each subunit in every CV subcompartment. |
| septin-contractile-agent-UniProtKB-Q76NU1 | https://rest.uniprot.org/uniprotkb/Q76NU1.json; Exact reviewed accession, gene tokens, protein name, organism, functional/subcellular comments and evidence codes | supports | Current reviewed Q76NU1 identifies vatB in Dictyostelium taxon44689. Pump subunit identity/complex role is verified; location comments and evidence codes are distinguished from a direct assay of each subunit in every CV subcompartment. |
| septin-contractile-agent-UniProtKB-P54648 | https://rest.uniprot.org/uniprotkb/P54648.json; Exact reviewed accession, gene tokens, protein name, organism, functional/subcellular comments and evidence codes | supports | Current reviewed P54648 identifies vatC in Dictyostelium taxon44689. Pump subunit identity/complex role is verified; location comments and evidence codes are distinguished from a direct assay of each subunit in every CV subcompartment. |
| septin-contractile-agent-UniProtKB-Q54E04 | https://rest.uniprot.org/uniprotkb/Q54E04.json; Exact reviewed accession, gene tokens, protein name, organism, functional/subcellular comments and evidence codes | supports | Current reviewed Q54E04 identifies vatM in Dictyostelium taxon44689. Pump subunit identity/complex role is verified; location comments and evidence codes are distinguished from a direct assay of each subunit in every CV subcompartment. |
| septin-contractile-agent-UniProtKB-Q9U8P7 | https://rest.uniprot.org/uniprotkb/Q9U8P7.json; Exact reviewed accession, gene tokens, protein name, organism, functional/subcellular comments and evidence codes | supports | Current reviewed Q9U8P7 identifies aqpA in Dictyostelium taxon44689. AqpA annotations concern putative channel activity and spore survival, with cell-membrane localization by similarity; no CV membership is established. |
| septin-contractile-agent-UniProtKB-Q54WT8 | https://rest.uniprot.org/uniprotkb/Q54WT8.json; Exact reviewed accession, gene tokens, protein name, organism, functional/subcellular comments and evidence codes | supports | Current reviewed Q54WT8 identifies aqpB in Dictyostelium taxon44689. AqpB annotations explicitly retain impermeable tested wild type, generic vacuoles and plasma-membrane protrusions; direct CV localization is not asserted. |
| septin-contractile-agent-query-vatA-44689 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=100&amp;query=%28gene_exact%3AvatA%29%20AND%20%28taxonomy_id%3A44689%29%20AND%20%28reviewed%3Atrue%29; Complete returned exact-symbol/taxon/reviewed response and primary gene token | supports | One current returned reviewed match P54647 for vatA; establishes bounded present query uniqueness/identity, not historical query execution or CV localization. |
| septin-contractile-agent-query-vatB-44689 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=100&amp;query=%28gene_exact%3AvatB%29%20AND%20%28taxonomy_id%3A44689%29%20AND%20%28reviewed%3Atrue%29; Complete returned exact-symbol/taxon/reviewed response and primary gene token | supports | One current returned reviewed match Q76NU1 for vatB; establishes bounded present query uniqueness/identity, not historical query execution or CV localization. |
| septin-contractile-agent-query-vatC-44689 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=100&amp;query=%28gene_exact%3AvatC%29%20AND%20%28taxonomy_id%3A44689%29%20AND%20%28reviewed%3Atrue%29; Complete returned exact-symbol/taxon/reviewed response and primary gene token | supports | One current returned reviewed match P54648 for vatC; establishes bounded present query uniqueness/identity, not historical query execution or CV localization. |
| septin-contractile-agent-query-vatM-44689 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=100&amp;query=%28gene_exact%3AvatM%29%20AND%20%28taxonomy_id%3A44689%29%20AND%20%28reviewed%3Atrue%29; Complete returned exact-symbol/taxon/reviewed response and primary gene token | supports | One current returned reviewed match Q54E04 for vatM; establishes bounded present query uniqueness/identity, not historical query execution or CV localization. |
| septin-contractile-agent-query-aqpA-44689 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=100&amp;query=%28gene_exact%3AaqpA%29%20AND%20%28taxonomy_id%3A44689%29%20AND%20%28reviewed%3Atrue%29; Complete returned exact-symbol/taxon/reviewed response and primary gene token | supports | One current returned reviewed match Q9U8P7 for aqpA; establishes bounded present query uniqueness/identity, not historical query execution or CV localization. |
| septin-contractile-agent-query-aqpB-44689 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=100&amp;query=%28gene_exact%3AaqpB%29%20AND%20%28taxonomy_id%3A44689%29%20AND%20%28reviewed%3Atrue%29; Complete returned exact-symbol/taxon/reviewed response and primary gene token | supports | One current returned reviewed match Q54WT8 for aqpB; establishes bounded present query uniqueness/identity, not historical query execution or CV localization. |
| septin-contractile-agent-query-MIP1-3055-all | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=100&amp;query=%28gene_exact%3AMIP1%29%20AND%20%28taxonomy_id%3A3055%29; Complete returned exact MIP1/taxon3055 query with no reviewed filter | supports | Zero results for this exact current query does not establish protein absence, lack of other accession names, or disprove primary MIP1 CV localization. No accession is guessed. |
| septin-catalogue | https://imodulondb.org/api/datasets; Complete official organism/dataset list, every id/name and dataset key | supports | No matching Amoeba, Dictyostelium, Chlamydomonas, Trypanosoma or Paramecium organism/dataset is returned. Molecular/osmoregulatory response applicability was assessed; no unmatched-organism gene/module lookup or biological absence inference is justified. |
| septin-historical-adapter-runner | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Actual canary invocation00:49:00.848907Z–00:49:00.863225Z | supports | Historical datasets invocation exited1 with PermissionError reading runner pyvenv.cfg. This is retained availability evidence, not a fresh invocation or current successful adapter run; official source fallback was separately fetched. |
| septin-source-access | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/adversary-septin/source-receipts.json; Actual request URLs, timestamps, outcomes and successful-response hashes | supports | Numeric Komsic/Bülow PMC HTML and Docampo S3 JATS are genuine bodies. Guessed Komsic/Bülow S3 .1 paths returned404; More/Nishihara/Clarke publisher routes returned403. Failed routes are not source text. Other indicated primary studies are assessed only via complete native abstracts. |
| check-qc | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/qc.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| check-labels | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/labels.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| check-trait-links | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/trait-links.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Native TraitMech link check passed. |
| check-vendored | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/vendored.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Pinned governed files match; native vendored check passed. |
| check-curies | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/curies.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| focused | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/focused-results.json; All twenty actual target schema/strict command outputs | supports | Ten schema and ten strict commands returned exit zero. |
| supplemental-pmid | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/pmid-chunks-receipt.json; Complete native-report PMID set checked with unchanged resolver in batches of at most fifty | supports | 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers remain unverified. |
| historical-adapter-runner-availability | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical runner invocation receipt, cross-checked against exact stdout/stderr hashes; reread during PR2361 synthesis | context_only | Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS PermissionError reading the configured runner pyvenv.cfg. This is a retained historical availability observation, not a fresh attempt or a scientific validation failure. Native policy permits inspected source-catalogue fallback. |

## Limits And Additional Notes

- Contractile vacuole lumen/pore and COPII transport vesicle/lumen independent subreview: Assigned four records only, all current target hashes unchanged; three already-frozen mutual CV targets were used only for boundary fields. No neighbor, group, category or historical external issue is terminally resolved.
- Contractile vacuole lumen/pore and COPII transport vesicle/lumen independent subreview: Komsic2014 genuine primary HTML scientific body and Table1/captions were independently inspected from same-PR shared snapshot with actual original timestamp. No images, movies, supplemental experiments or raw measurements reanalyzed. Its CC3395 and UVM4 contexts are distinguished from universal Chlamydomonas claims.
- Contractile vacuole lumen/pore and COPII transport vesicle/lumen independent subreview: Komsic CV size correlates with cell size/growth, interval with osmolarity; modeled lumen osmolarity is not measured. The lumen text describes measurements under varied conditions and does not claim a causal volume–osmolarity relationship. Sibling record findings do not transfer automatically.
- Contractile vacuole lumen/pore and COPII transport vesicle/lumen independent subreview: Gronlien primary abstract supports the compressed-Paramecium microelectrode example; More2024 and Allen2002 remain secondary abstracts, not inspected full bodies. DOI redirect/challenge pages do not upgrade access tier. RARE/COMMON are qualitative context, not prevalence counts.
- Contractile vacuole lumen/pore and COPII transport vesicle/lumen independent subreview: Frankel secondary chapter was inspected at complete named CV and pore sections and opening positioning paragraphs, not the entire book or image pixels. McKanna1973 is publisher-deposited primary synopsis only; no experimental species or exact protein composition is invented.
- Contractile vacuole lumen/pore and COPII transport vesicle/lumen independent subreview: Barlowe1994 is complete primary abstract only. Matsuoka1998 fresh institutional PDF scientific text pp263–274 includes Methods/Tables/captions; no images or raw data reanalyzed. Native ER and synthetic-liposome/nucleotide conditions remain distinct; in-vitro formation is not universal in-vivo necessity.
- Contractile vacuole lumen/pore and COPII transport vesicle/lumen independent subreview: GO contractile-lumen search read only first100 of398 hits. Exact candidate GO0106173 label/definition conflict is retained as unknown, without forced mapping, exhaustive absence or historical issue resolution.
- Contractile vacuole lumen/pore and COPII transport vesicle/lumen independent subreview: Three applicability defects are specific: contractile-lumen omission for explicit osmotic-response context, and two COPII expression-only exemptions despite named machinery. Pore is genuinely excluded at topology/coarse-flow scope with unasserted molecular composition.
- Contractile vacuole lumen/pore and COPII transport vesicle/lumen independent subreview: Fresh complete catalogue has no matching yeast/ciliate/algal organism; no downstream matched query applies or biological absence follows. Historical00:49Z runner PermissionError remains historical, not a new failure or successful invocation.
- Contractile vacuole lumen/pore and COPII transport vesicle/lumen independent subreview: All eight native protein commands pass empty represented inventories and zero typed protein nodes. They do not validate narrative molecular identities, formation necessity or scientific source support. Root owns full QC, issue handling and all repository/GitHub changes.
- COPI vesicle, lumen and membrane independent subreview: Assigned scope is three COPI records. Whole vesicle stale additions were reassessed; other two targets are unchanged. Three neighbor records are bounded identity/partonomy/component context only; their scientific or category findings are not disposed of.
- COPI vesicle, lumen and membrane independent subreview: Sandmann fresh primary HTML was read only in the exact declared Abstract/Introduction, Methods and Results/Discussion sections. Other body sections, figure pixels, supplementary/raw microscopy and assay data were not reanalysed. Genetic suppression and packaging assays are not direct measurements of every trafficking step or population frequency.
- COPI vesicle, lumen and membrane independent subreview: Waters1991 is complete primary abstract/bibliography only. Current publisher HTTP200 is a Client Challenge, not readable article text. Sandmann XML HTTP500 is an access limitation covered by independently readable genuine primary HTML.
- COPI vesicle, lumen and membrane independent subreview: Yu2012 retains actual 10:50Z snapshots from PR2360, hash verified; previously inspected Introduction/Experimental Approach/model sections remain the scope and Introduction was reread. No new download, full Methods or image audit claimed. Mammalian coatomer with defined human/yeast constructs is not direct yeast-specific assembly necessity.
- COPI vesicle, lumen and membrane independent subreview: GO0006890 supports general directed transport destination. The refreshed proteins/lipids description is broad contextual cargo scope, not a particular lipid-species flux measurement, exclusively COPI route, fusion mechanism or coat-retention assertion.
- COPI vesicle, lumen and membrane independent subreview: Same-label GO0106172 remains definition-limited by endocytic wording in QuickGO and OLS; exact equivalence to general SL-0321/local lumen is unknown. The current query inspected first100 of618 hits, not every ontology term. No exact-term absence or historical mapping-error claim is made.
- COPI vesicle, lumen and membrane independent subreview: Arakel/Schwappach2018 is secondary abstract context only; no body/poster read and no resolution of the native definition inconsistency inferred.
- COPI vesicle, lumen and membrane independent subreview: All six native protein commands pass empty protein inventories and zero GENE_OR_PROTEIN nodes; they do not verify narrative molecules or source scope. No unsupported accession/family absence is asserted.
- COPI vesicle, lumen and membrane independent subreview: Catalogue coverage check is complete only for the returned current array; no matching yeast dataset means no applicable downstream gene/module query. Historical runner failure at00:49Z remains historical; no fresh execution is claimed.
- COPI vesicle, lumen and membrane independent subreview: No target images, numerical properties or snippets require additional audit. All original findings/actions arrays are empty. Root owns corpus gates, issue deduplication/publication, successor writing and final CI; this report makes no future CI claim.
- Contractile vacuolar membrane, whole vacuole and complex independent subreview: Assigned membrane/whole-vacuole/complex records only. All are unchanged from frozen original source bytes, and all original validation/render checks pass. Whole-vacuole F1–F3 remain open; F2 includes a verified repeated graph-note occurrence under the same stable key.
- Contractile vacuolar membrane, whole vacuole and complex independent subreview: Komsic current genuine primary HTML was read only at declared Abstract, Strains used Methods, specified Results, Aquaporins and CV function Discussion, Table1 and associated text captions. CC3395/UVM4-derived strain and osmotic-adaptation scope is retained. No image pixels, supplementary movies or raw-data audit.
- Contractile vacuolar membrane, whole vacuole and complex independent subreview: Bülow current genuine primary HTML was read at complete Abstract, Results and Discussion with text captions, not full Experimental Procedures or pixels. The AqpB hypothesis, unspecified vacuoles, GFP-fusion localization and mutant-versus-wild-type transport result remain distinct. This is insufficient cited membership support, not proof of biological absence.
- Contractile vacuolar membrane, whole vacuole and complex independent subreview: Nishihara, Clarke, Nolta, Gronlien, Rohloff and Mitra2000 were read as complete native primary abstracts only. More2024 and Allen2002 are secondary abstract context. Unread publisher bodies and guessed S3 routes returned403/404; no full-body access is invented.
- Contractile vacuolar membrane, whole vacuole and complex independent subreview: Docampo2013 is a current genuine secondary JATS body, inspected only at sections History, Structure and composition, and Role in osmoregulation. Cited-primary experiments, raw images and the complete article were not independently audited. Proposed osmolyte and systole mechanisms remain hypotheses.
- Contractile vacuolar membrane, whole vacuole and complex independent subreview: Six UniProt accessions and six exact reviewed symbol/taxon queries support current identity and bounded uniqueness only. MIP1 exact query zero hits does not establish absence or justify guessing an accession. Broad InterPro MIP/aquaporin classes are not exact CV-localized subset or localization evidence.
- Contractile vacuolar membrane, whole vacuole and complex independent subreview: Native membrane inventory has one NO_GENE_SYMBOLS and one UNANCHORED_NO_UNIPROT node; whole vacuole has one COVERED and one PARTIAL_EXAMPLES node, missing MIP1; complex has empty inventory/zero protein nodes. All six commands exit0, without resolving scientific concerns or proving mechanistic/formation claims.
- Contractile vacuolar membrane, whole vacuole and complex independent subreview: Actual molecular and osmoregulatory-response scope merits structured-source applicability for all three targets. No matching model organism is present in the fresh complete catalogue; no unrelated downstream query is substituted. Historical runner PermissionError remains00:49Z, not a fresh invocation.
- Contractile vacuolar membrane, whole vacuole and complex independent subreview: Eukaryotic rarity is qualitative. Strain/model localization, transport function and osmotic adaptation do not establish universal constituent membership or molecular necessity for structure formation. Composite CVC and bladder/bilayer/anatomical parts remain distinct despite broader source terminology.
- Contractile vacuolar membrane, whole vacuole and complex independent subreview: Three frozen neighbors were read only at declared boundary fields. No neighbor/group/category issue is terminally resolved. Root owns global gates, issue deduplication/publication, repository/GitHub writes and final CI/queue checks.
- Historical observations remain immutable; their old checks are not represented as current-head execution.
- The adapter runner was not rerun after the canary established OS access failure. Catalogue-based coverage is assessed directly; fresh and reused responses retain actual access timestamps.
- Native label checks include 923 no-adapter skips. Native identifier checks include 909 PMID transport failures and 254 skipped identifiers; bounded supplemental checks independently resolve the 909 PMIDs.
- Scientific record-curation findings stay in separate issues; no record is edited by this review PR.
- Final trusted-base post-save review-check, exact-head independent acceptance, final-head CI and merge-group CI occur after saving this immutable observation and are not represented here as already completed.
- All ten original YAML/Markdown pairs remain unchanged. Current main was merged normally and pushed without force.
- This explicit issue-bearing ten-record cohort follows the native persistence policy. Each inherited scientific finding retains exact predecessor identity.
- Issue #2668 tracks the one stale target: COPI-coated vesicle gained a history entry and a Golgi-to-ER retrograde transport destination edge. Current GO0006890 and primary COPI evidence support its bounded transport destination; broad proteins/lipids cargo context does not establish a particular lipid flux, fusion mechanism or exclusively COPI route.
- Issue #2669 tracks nine applicability defects: omitted assessments for contractile vacuolar membrane, whole vacuole, complex and lumen; five unsupported expression-only exclusions for the three COPI and two COPII targets. Contractile vacuole pore remains a genuine exclusion at topology and coarse flow-control scope without asserted molecular composition.
- Source commit 7081777bba0daacfa48fc6d826cdfd7138e751b4 is retained by tag review-base/pr2361-current-record-followup-20261103.
- CLAUDE.md is an alias of AGENTS.md; canonical regular AGENTS.md bytes are frozen.
- All 51 used local inputs were frozen before assessment, including four neighbor records, native configuration, graph/protein policies and verifier source. Neighbors are context only, not additional targets or dispositions of their findings.
- Fresh and reused public-source snapshots retain actual access dates and inspection tiers. Native authority identity does not independently establish localization, mechanistic action or assembly necessity.
- All twenty native protein commands returned zero, with incomplete coverage explicitly retained. Contractile-vacuolar membrane V-ATPase is UNANCHORED_NO_UNIPROT and aquaporins NO_GENE_SYMBOLS. Whole-vacuole V-ATPase is covered by four represented accessions; aquaporins are PARTIAL_EXAMPLES with MIP1 missing. Empty inventories or zero typed protein nodes in other targets do not validate narrative molecules. Execution success does not establish contractile-vacuole membership.
- The major contractile-vacuole finding concerns insufficient AqpA/AqpB membership support. The two minor findings concern osmolarity-dependent size wording, including its repeated discharge-edge evidence note, and treating the related central-bladder synonym as exact. Source-supported distinctions between size/cell growth and contraction interval/osmolarity are preserved.
- The contractile-vacuole lumen wording describes volume measurements under varied conditions without asserting a causal volume-to-osmolarity relationship; an independent source reread supports that bounded scope. The sibling whole-vacuole finding is not automatically transferred.
- Current GO0106172 and GO0106173 have exact COPI/COPII lumen labels but conflicting endocytic definition wording. Mapping uncertainty is preserved; neither forced retargeting nor exhaustive ontology absence is claimed.
- All three inherited scientific findings remain open for separate record curation. Nine targets retain qualified positive scientific assessments. No record is edited.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T112432Z-pr2361-current-record-followup
kind: batch
repository: CultureBotAI/CellStructureMech
title: 'PR 2361: current-input review of ten records and adversarial follow-up'
started_at: '2026-11-03T11:15:33.506892Z'
finished_at: '2026-11-03T11:24:32Z'
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
summary: Current-input reassessment of all ten records in PR2361. One stale COPI-coated
  vesicle review is substantively refreshed. Independent source assessments retain
  three inherited contractile-vacuole scientific findings and correct nine structured-source
  applicability assessments without editing records.
source:
  git_revision: 7081777bba0daacfa48fc6d826cdfd7138e751b4
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
  - path: data/structures/membrane_organelle/contractile_vacuolar_membrane.yaml
    sha256: a73ad7ccfc67c7c39a41d555109a229de1c469dec8eff0d808a3cddaa0aa383c
    role: target
  - path: data/structures/membrane_organelle/contractile_vacuole.yaml
    sha256: d1057e9c19ff100f054c73da52b597742dadde491f2a007cd7b648b8a7b626bb
    role: target
  - path: data/structures/membrane_organelle/contractile_vacuole_complex.yaml
    sha256: 5d37be1aa899c1bfd20611faeafefb842a96e8a21144dea9e010b2c89d4b7a1c
    role: target
  - path: data/structures/membrane_organelle/contractile_vacuole_lumen.yaml
    sha256: 9c85ec352245d16e963b9d86d4d1cf0b41d499b956b0b2d05611dca3a4341622
    role: target
  - path: data/structures/membrane_organelle/contractile_vacuole_pore.yaml
    sha256: e6b016675a36c215388bfd9053da4af4b1ec407c47c197f8a2217f9ba66cc294
    role: target
  - path: data/structures/membrane_organelle/copi_coated_vesicle.yaml
    sha256: d542d1063731ec276cf5e771752715152ad950ee3fd1819f24e1a792036f2981
    role: target
  - path: data/structures/membrane_organelle/copi_coated_vesicle_lumen.yaml
    sha256: f4da3395ba3aa5bfa65d859069e5b2f5d15303f81d7da6048291813188d9bcfa
    role: target
  - path: data/structures/membrane_organelle/copi_coated_vesicle_membrane.yaml
    sha256: 70dbc868044797a3911de45524d13ccbedb5bf9cc671824b0dcade909ab4922f
    role: target
  - path: data/structures/membrane_organelle/copii_coated_er_to_golgi_transport_vesicle.yaml
    sha256: 141713f26c4f5cc6a2e6c6cb232bf45e194df53bcd60aa4769cc4343ac6599bf
    role: target
  - path: data/structures/membrane_organelle/copii_coated_vesicle_lumen.yaml
    sha256: d75ae8e81d2fc08979408842f74ef1ad621e87108044faf2dcc6ca216e5e7782
    role: target
  - path: data/structures/membrane_organelle/endoplasmic_reticulum.yaml
    sha256: eade1489e38ea7ee989edc3bf5c583e58041b4bfd0ffb9b4acbd666cd98c0160
    role: context
  - path: data/structures/membrane_organelle/golgi_membrane.yaml
    sha256: 22a35f67a05738d876923e98adfe54cde34ee23c9009667f48676dca83ba708c
    role: context
  - path: data/structures/membrane_organelle/spongiome.yaml
    sha256: 4bdc11a86d247b6a45549a41c9aac3b25946b046f3b54d269fab634ca9d44019
    role: context
  - path: data/structures/other/copi_vesicle_coat.yaml
    sha256: 1b264ad3800f2c5c8c78d327f63a32bdc73888a003e3be3fcad778bb9f993195
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
  - path: reviews/structured/20261022T005251Z-contractile-vacuolar-membrane-audit/review.md
    sha256: 55b3020d7198524fba0328ccd78a3af880db33fb0efbbfa17439cbde42332108
    role: context
  - path: reviews/structured/20261022T005251Z-contractile-vacuolar-membrane-audit/review.yaml
    sha256: 0277dc12a05fdf291f94a1fc983a973c151af82e33f3a6375bea7e4900406ad8
    role: context
  - path: reviews/structured/20261022T005252Z-contractile-vacuole-audit/review.md
    sha256: dbd551f4864a44d2d9f1b1f3c255dd4ac72c2748da25869330d689e506c32da9
    role: context
  - path: reviews/structured/20261022T005252Z-contractile-vacuole-audit/review.yaml
    sha256: a49af232ae1b9a295c0885c7b34b7598c296a7a58c97f574f5060dc5dbd7d274
    role: context
  - path: reviews/structured/20261022T005253Z-contractile-vacuole-complex-audit/review.md
    sha256: d31e2c0f81bd257cf304cabd2249a18dbb2d3f29b02c82ba680b9d7129ef6f4a
    role: context
  - path: reviews/structured/20261022T005253Z-contractile-vacuole-complex-audit/review.yaml
    sha256: 014d1929ae5fa35fbf1e8bde740d1b27fccb3f5eb0088e93434a8e6be43baac2
    role: context
  - path: reviews/structured/20261022T005253Z-contractile-vacuole-lumen-audit/review.md
    sha256: 4bf21919f4bb16f37b6eee658c98e931406cc916ce73364feb343496fa2d5a01
    role: context
  - path: reviews/structured/20261022T005253Z-contractile-vacuole-lumen-audit/review.yaml
    sha256: 41e6d3fb48280dc9ff59b67b9d1c7f24f788238da006beb62ee7fbcd2026b014
    role: context
  - path: reviews/structured/20261022T005254Z-contractile-vacuole-pore-audit/review.md
    sha256: dd82295a679e78c764d4bf715e5e5488d5bf43075b28edb3c3de7e8062fc5497
    role: context
  - path: reviews/structured/20261022T005254Z-contractile-vacuole-pore-audit/review.yaml
    sha256: 5fd85190f80c5a4cbb92129bc5c78f4f731e2c37f6e269541ef56d19661e7329
    role: context
  - path: reviews/structured/20261022T005255Z-copi-coated-vesicle-audit/review.md
    sha256: 057410aab79dd710bea99a378f71e04207260bf3d3f3c6ff68d03d28534e3b42
    role: context
  - path: reviews/structured/20261022T005255Z-copi-coated-vesicle-audit/review.yaml
    sha256: 69afa3c09645dc5c26a0b183faaad7e1a68596333cddbd44c6b99603ce7b93e3
    role: context
  - path: reviews/structured/20261022T005255Z-copi-coated-vesicle-lumen-audit/review.md
    sha256: 356cdd42d2769b53742a3619086db79891dfd4c24071a3dd2ebe188a64f75c94
    role: context
  - path: reviews/structured/20261022T005255Z-copi-coated-vesicle-lumen-audit/review.yaml
    sha256: 603b2c78ebc683f9133c8fd353aa17cc1de2766aec9d4e2066a259df2cb6789d
    role: context
  - path: reviews/structured/20261022T005256Z-copi-coated-vesicle-membrane-audit/review.md
    sha256: ce5d95d26084e46a315108b7d8caf2c99079e74171d2a091fda5e15f3687c03b
    role: context
  - path: reviews/structured/20261022T005256Z-copi-coated-vesicle-membrane-audit/review.yaml
    sha256: 07c380bffaa4ad7419dab5e93152ad58d831f9b6b06b2f46c5a13418689b0571
    role: context
  - path: reviews/structured/20261022T005257Z-copii-coated-er-to-golgi-transport-vesicle-audit/review.md
    sha256: b737c7f2e31b8b86e90d8e7be6d981197a580906d01760dfd3e7f8917f2b097a
    role: context
  - path: reviews/structured/20261022T005257Z-copii-coated-er-to-golgi-transport-vesicle-audit/review.yaml
    sha256: f7831dc05724e26491c81ef3c0ae1f2081f9e7930c2719d1cc183c641abc984d
    role: context
  - path: reviews/structured/20261022T005258Z-copii-coated-vesicle-lumen-audit/review.md
    sha256: d1fc9e41cef525699f5fe942de40bdc34bb231df9ceed7661fc38a01521dd3bf
    role: context
  - path: reviews/structured/20261022T005258Z-copii-coated-vesicle-lumen-audit/review.yaml
    sha256: 845568d3b865725c92b2382779d89fa342e12252cf7fa80f4dd929e87b5df3a3
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
- target_id: GO:0031164
  path: data/structures/membrane_organelle/contractile_vacuolar_membrane.yaml
  label: contractile vacuolar membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/contractile_vacuolar_membrane.yaml
    role: maintained scientific record
- target_id: GO:0000331
  path: data/structures/membrane_organelle/contractile_vacuole.yaml
  label: contractile vacuole
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/contractile_vacuole.yaml
    role: maintained scientific record
- target_id: GO:0062159
  path: data/structures/membrane_organelle/contractile_vacuole_complex.yaml
  label: contractile vacuole complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/contractile_vacuole_complex.yaml
    role: maintained scientific record
- target_id: cellstructuremech:contractile_vacuole_lumen
  path: data/structures/membrane_organelle/contractile_vacuole_lumen.yaml
  label: contractile vacuole lumen
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/contractile_vacuole_lumen.yaml
    role: maintained scientific record
- target_id: GO:0031913
  path: data/structures/membrane_organelle/contractile_vacuole_pore.yaml
  label: contractile vacuole pore
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/contractile_vacuole_pore.yaml
    role: maintained scientific record
- target_id: GO:0030137
  path: data/structures/membrane_organelle/copi_coated_vesicle.yaml
  label: COPI-coated vesicle
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/copi_coated_vesicle.yaml
    role: maintained scientific record
- target_id: cellstructuremech:copi_coated_vesicle_lumen
  path: data/structures/membrane_organelle/copi_coated_vesicle_lumen.yaml
  label: COPI-coated vesicle lumen
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/copi_coated_vesicle_lumen.yaml
    role: maintained scientific record
- target_id: GO:0030663
  path: data/structures/membrane_organelle/copi_coated_vesicle_membrane.yaml
  label: COPI-coated vesicle membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/copi_coated_vesicle_membrane.yaml
    role: maintained scientific record
- target_id: GO:0030134
  path: data/structures/membrane_organelle/copii_coated_er_to_golgi_transport_vesicle.yaml
  label: COPII-coated ER to Golgi transport vesicle
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/copii_coated_er_to_golgi_transport_vesicle.yaml
    role: maintained scientific record
- target_id: cellstructuremech:copii_coated_vesicle_lumen
  path: data/structures/membrane_organelle/copii_coated_vesicle_lumen.yaml
  label: COPII-coated vesicle lumen
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/copii_coated_vesicle_lumen.yaml
    role: maintained scientific record
scope:
  description: Exact ten-record PR cohort reassessed against current main 015960951a1c255e5ed24f5edb25a816d13ec948.
    Changed inputs are substantively reassessed. Scientific records remain unchanged.
  selection: Complete cohort of ten maintained records reviewed in original PR head
    f8c275390de4faf5d59d66f73b8abd8a84b31a39.
  coverage: full
  population_size: 10
  reviewed_target_ids:
  - GO:0031164
  - GO:0000331
  - GO:0062159
  - cellstructuremech:contractile_vacuole_lumen
  - GO:0031913
  - GO:0030137
  - cellstructuremech:copi_coated_vesicle_lumen
  - GO:0030663
  - GO:0030134
  - cellstructuremech:copii_coated_vesicle_lumen
checks:
- check_id: qc
  name: Full native QC
  status: passed
  required: true
  target_ids:
  - GO:0031164
  - GO:0000331
  - GO:0062159
  - cellstructuremech:contractile_vacuole_lumen
  - GO:0031913
  - GO:0030137
  - cellstructuremech:copi_coated_vesicle_lumen
  - GO:0030663
  - GO:0030134
  - cellstructuremech:copii_coated_vesicle_lumen
  command: just qc
  exit_code: 0
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  scope_note: Actual local execution at main-merge head 7081777bba0daacfa48fc6d826cdfd7138e751b4.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-qc
- check_id: labels
  name: Native label correspondence
  status: passed
  required: true
  target_ids:
  - GO:0031164
  - GO:0000331
  - GO:0062159
  - cellstructuremech:contractile_vacuole_lumen
  - GO:0031913
  - GO:0030137
  - cellstructuremech:copi_coated_vesicle_lumen
  - GO:0030663
  - GO:0030134
  - cellstructuremech:copii_coated_vesicle_lumen
  command: just validate-products
  exit_code: 0
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  scope_note: Actual local execution at main-merge head 7081777bba0daacfa48fc6d826cdfd7138e751b4.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-labels
- check_id: trait-links
  name: TraitMech references
  status: passed
  required: true
  target_ids:
  - GO:0031164
  - GO:0000331
  - GO:0062159
  - cellstructuremech:contractile_vacuole_lumen
  - GO:0031913
  - GO:0030137
  - cellstructuremech:copi_coated_vesicle_lumen
  - GO:0030663
  - GO:0030134
  - cellstructuremech:copii_coated_vesicle_lumen
  command: just check-trait-links --check
  exit_code: 0
  summary: Native TraitMech link check passed.
  scope_note: Actual local execution at main-merge head 7081777bba0daacfa48fc6d826cdfd7138e751b4.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-trait-links
- check_id: vendored
  name: Pinned governed files
  status: passed
  required: true
  target_ids:
  - GO:0031164
  - GO:0000331
  - GO:0062159
  - cellstructuremech:contractile_vacuole_lumen
  - GO:0031913
  - GO:0030137
  - cellstructuremech:copi_coated_vesicle_lumen
  - GO:0030663
  - GO:0030134
  - cellstructuremech:copii_coated_vesicle_lumen
  command: just vendored-check
  exit_code: 0
  summary: Pinned governed files match; native vendored check passed.
  scope_note: Actual local execution at main-merge head 7081777bba0daacfa48fc6d826cdfd7138e751b4.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-vendored
- check_id: curies
  name: Native identifier resolver
  status: passed
  required: true
  target_ids:
  - GO:0031164
  - GO:0000331
  - GO:0062159
  - cellstructuremech:contractile_vacuole_lumen
  - GO:0031913
  - GO:0030137
  - cellstructuremech:copi_coated_vesicle_lumen
  - GO:0030663
  - GO:0030134
  - cellstructuremech:copii_coated_vesicle_lumen
  command: just check-curies-strict
  exit_code: 0
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  scope_note: Actual local execution at main-merge head 7081777bba0daacfa48fc6d826cdfd7138e751b4.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-curies
- check_id: focused-0
  name: validate GO:0031164
  status: passed
  required: true
  target_ids:
  - GO:0031164
  command: just validate data/structures/membrane_organelle/contractile_vacuolar_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-1
  name: validate-strict GO:0031164
  status: passed
  required: true
  target_ids:
  - GO:0031164
  command: just validate-strict data/structures/membrane_organelle/contractile_vacuolar_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-2
  name: validate GO:0000331
  status: passed
  required: true
  target_ids:
  - GO:0000331
  command: just validate data/structures/membrane_organelle/contractile_vacuole.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-3
  name: validate-strict GO:0000331
  status: passed
  required: true
  target_ids:
  - GO:0000331
  command: just validate-strict data/structures/membrane_organelle/contractile_vacuole.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-4
  name: validate GO:0062159
  status: passed
  required: true
  target_ids:
  - GO:0062159
  command: just validate data/structures/membrane_organelle/contractile_vacuole_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-5
  name: validate-strict GO:0062159
  status: passed
  required: true
  target_ids:
  - GO:0062159
  command: just validate-strict data/structures/membrane_organelle/contractile_vacuole_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-6
  name: validate cellstructuremech:contractile_vacuole_lumen
  status: passed
  required: true
  target_ids:
  - cellstructuremech:contractile_vacuole_lumen
  command: just validate data/structures/membrane_organelle/contractile_vacuole_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-7
  name: validate-strict cellstructuremech:contractile_vacuole_lumen
  status: passed
  required: true
  target_ids:
  - cellstructuremech:contractile_vacuole_lumen
  command: just validate-strict data/structures/membrane_organelle/contractile_vacuole_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-8
  name: validate GO:0031913
  status: passed
  required: true
  target_ids:
  - GO:0031913
  command: just validate data/structures/membrane_organelle/contractile_vacuole_pore.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-9
  name: validate-strict GO:0031913
  status: passed
  required: true
  target_ids:
  - GO:0031913
  command: just validate-strict data/structures/membrane_organelle/contractile_vacuole_pore.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-10
  name: validate GO:0030137
  status: passed
  required: true
  target_ids:
  - GO:0030137
  command: just validate data/structures/membrane_organelle/copi_coated_vesicle.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-11
  name: validate-strict GO:0030137
  status: passed
  required: true
  target_ids:
  - GO:0030137
  command: just validate-strict data/structures/membrane_organelle/copi_coated_vesicle.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-12
  name: validate cellstructuremech:copi_coated_vesicle_lumen
  status: passed
  required: true
  target_ids:
  - cellstructuremech:copi_coated_vesicle_lumen
  command: just validate data/structures/membrane_organelle/copi_coated_vesicle_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-13
  name: validate-strict cellstructuremech:copi_coated_vesicle_lumen
  status: passed
  required: true
  target_ids:
  - cellstructuremech:copi_coated_vesicle_lumen
  command: just validate-strict data/structures/membrane_organelle/copi_coated_vesicle_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-14
  name: validate GO:0030663
  status: passed
  required: true
  target_ids:
  - GO:0030663
  command: just validate data/structures/membrane_organelle/copi_coated_vesicle_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-15
  name: validate-strict GO:0030663
  status: passed
  required: true
  target_ids:
  - GO:0030663
  command: just validate-strict data/structures/membrane_organelle/copi_coated_vesicle_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-16
  name: validate GO:0030134
  status: passed
  required: true
  target_ids:
  - GO:0030134
  command: just validate data/structures/membrane_organelle/copii_coated_er_to_golgi_transport_vesicle.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-17
  name: validate-strict GO:0030134
  status: passed
  required: true
  target_ids:
  - GO:0030134
  command: just validate-strict data/structures/membrane_organelle/copii_coated_er_to_golgi_transport_vesicle.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-18
  name: validate cellstructuremech:copii_coated_vesicle_lumen
  status: passed
  required: true
  target_ids:
  - cellstructuremech:copii_coated_vesicle_lumen
  command: just validate data/structures/membrane_organelle/copii_coated_vesicle_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-19
  name: validate-strict cellstructuremech:copii_coated_vesicle_lumen
  status: passed
  required: true
  target_ids:
  - cellstructuremech:copii_coated_vesicle_lumen
  command: just validate-strict data/structures/membrane_organelle/copii_coated_vesicle_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: supplemental-pmid
  name: Supplemental bounded PMID authority checks
  status: passed
  required: true
  target_ids:
  - GO:0031164
  - GO:0000331
  - GO:0062159
  - cellstructuremech:contractile_vacuole_lumen
  - GO:0031913
  - GO:0030137
  - cellstructuremech:copi_coated_vesicle_lumen
  - GO:0030663
  - GO:0030134
  - cellstructuremech:copii_coated_vesicle_lumen
  command: .venv/bin/python /private/tmp/cellstructure-batches-2346-2397-20261103/check_pmid_chunks.py
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361
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
  - GO:0031164
  - GO:0000331
  - GO:0062159
  - cellstructuremech:contractile_vacuole_lumen
  - GO:0031913
  - GO:0030137
  - cellstructuremech:copi_coated_vesicle_lumen
  - GO:0030663
  - GO:0030134
  - cellstructuremech:copii_coated_vesicle_lumen
  summary: 'Nine applicability defects are corrected: four omitted assessments for
    contractile vacuolar membrane, vacuole, complex and lumen, plus five unsupported
    expression-only exclusions across COPI vesicle/lumen/membrane and COPII transport
    vesicle/lumen. Osmotic-response context itself triggers the native policy even
    without named molecular components. Contractile vacuole pore remains genuinely
    excluded at topology/coarse-flow scope with unresolved molecular identities. Complete
    catalogue coverage has no matching relevant yeast, ciliate, algal, Amoeba, Dictyostelium,
    Trypanosoma or Paramecium dataset. No unrelated organism dataset or downstream
    module query substitutes for noncoverage. Resource noncoverage is not biological
    absence; retained historical runner failure is not a fresh invocation.'
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
  - GO:0031164
  - GO:0000331
  - GO:0062159
  - cellstructuremech:contractile_vacuole_lumen
  - GO:0031913
  - GO:0030137
  - cellstructuremech:copi_coated_vesicle_lumen
  - GO:0030663
  - GO:0030134
  - cellstructuremech:copii_coated_vesicle_lumen
  summary: Three read-only reviewers covered the complete ten-record cohort, including
    changed inputs, with explicit scientific findings and source-access limits. Final
    artifact/head acceptance occurs after saving.
  evidence_ids:
  - plaque-policy
  - plaque-rubric
  - plaque-graph-policy
  - plaque-schema-policy
  - plaque-contractile-agent-go
  - plaque-contractile-agent-SL-0320
  - plaque-contractile-agent-tax-2759
  - plaque-contractile-agent-tax-44030
  - plaque-contractile-agent-tax-3055
  - plaque-root24-sources-NCBITaxon-5911
  - plaque-copii-agent-tax4932
  - plaque-contractile-agent-more2024-meta
  - plaque-contractile-agent-allen2002-title
  - plaque-contractile-agent-gronlien2002-meta
  - plaque-contractile-agent-komsic2014-pmc-numeric
  - plaque-root24-sources-pore-go
  - plaque-root24-sources-pore-ancestors
  - plaque-root24-sources-frankel2000-pmid
  - plaque-root24-sources-frankel2000-quoteddoi
  - plaque-root24-sources-doi-10.1111_j.1550-7408.1973.tb03587.x
  - plaque-copii-agent-PMID-9568718
  - plaque-root24-sources-frankel2000-university-pdf
  - plaque-root24-sources-mckanna1973-crossref
  - plaque-copii-agent-go
  - plaque-copii-agent-SL-0322
  - plaque-copii-agent-go-lumen-candidates
  - plaque-copii-agent-PMID-8004676
  - plaque-copii-agent-matsuoka1998-author
  - plaque-access-more2024-publisher
  - plaque-access-gronlien2002-publisher
  - plaque-access-allen2002-publisher
  - plaque-root24-sources-frankel2000-publisher
  - plaque-root24-sources-frankel2000-api
  - plaque-root24-sources-mckanna1973-publisher
  - plaque-root24-sources-mckanna1973-pdf
  - plaque-root24-sources-mckanna1973-tdm
  - plaque-copii-agent-barlowe1994-publisher
  - plaque-copii-agent-barlowe1994-sciencedirect
  - plaque-catalogue
  - micro-review-policy
  - micro-review-config
  - micro-review-profile
  - micro-review-checklist
  - micro-graph-policy
  - micro-native-schema
  - micro-review-schema
  - micro-go
  - micro-SL-0321
  - micro-NCBITaxon-4932
  - micro-sandmann2003-meta
  - micro-sandmann2003-pmc
  - micro-sandmann2003-jats
  - micro-waters1991-meta
  - micro-waters1991-publisher
  - micro-go0106172-ols
  - micro-lumen-citation-meta
  - micro-doi-10.1016_j.cell.2012.01.015
  - micro-yu2012-s3
  - septin-review-policy
  - septin-curation-policy
  - septin-graph-policy
  - septin-contractile-agent-go
  - septin-contractile-agent-ancestors-0031164
  - septin-contractile-agent-ancestors-0000331
  - septin-contractile-agent-ancestors-0062159
  - septin-contractile-agent-go-vacuole-parent
  - septin-contractile-agent-go-vatpase
  - septin-contractile-agent-SL-0073
  - septin-contractile-agent-SL-0074
  - septin-contractile-agent-tax-2759
  - septin-contractile-agent-tax-5775
  - septin-contractile-agent-tax-44689
  - septin-contractile-agent-tax-3055
  - septin-contractile-agent-tax-5693
  - septin-contractile-agent-tax-44030
  - septin-contractile-agent-more2024-meta
  - septin-contractile-agent-nishihara2008-meta
  - septin-contractile-agent-clarke2002-meta
  - septin-contractile-agent-rohloff2004-meta
  - septin-contractile-agent-allen2002-title
  - septin-contractile-agent-bulow2012-meta
  - septin-contractile-agent-aqpA2000-meta
  - septin-contractile-agent-nolta1994-meta
  - septin-contractile-agent-gronlien2002-meta
  - septin-contractile-agent-komsic2014-pmc-numeric
  - septin-contractile-agent-bulow2012-pmc-numeric
  - septin-contractile-agent-docampo2013-s3
  - septin-contractile-agent-aquaporin-family
  - septin-contractile-agent-aquaporin-transporter
  - septin-contractile-agent-UniProtKB-P54647
  - septin-contractile-agent-UniProtKB-Q76NU1
  - septin-contractile-agent-UniProtKB-P54648
  - septin-contractile-agent-UniProtKB-Q54E04
  - septin-contractile-agent-UniProtKB-Q9U8P7
  - septin-contractile-agent-UniProtKB-Q54WT8
- check_id: historical-adapter-runner
  name: Retained historical adapter runner availability
  status: unavailable
  required: false
  target_ids:
  - GO:0031164
  - GO:0000331
  - GO:0062159
  - cellstructuremech:contractile_vacuole_lumen
  - GO:0030137
  - cellstructuremech:copi_coated_vesicle_lumen
  - GO:0030663
  - GO:0030134
  - cellstructuremech:copii_coated_vesicle_lumen
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
- check_id: contractile_vacuolar_membrane-uniprot-verify
  name: Native contractile vacuolar membrane UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0031164
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/contractile_vacuolar_membrane.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Missing anchors/examples, empty inventories
    and zero molecular graph nodes do not validate narrative molecules, localization,
    mechanism, taxon transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-contractile_vacuolar_membrane-verify
- check_id: contractile_vacuolar_membrane-uniprot-causal
  name: Native contractile vacuolar membrane UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0031164
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/contractile_vacuolar_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Missing anchors/examples, empty inventories
    and zero molecular graph nodes do not validate narrative molecules, localization,
    mechanism, taxon transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-contractile_vacuolar_membrane-causal
- check_id: contractile_vacuole-uniprot-verify
  name: Native contractile vacuole UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0000331
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/contractile_vacuole.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Missing anchors/examples, empty inventories
    and zero molecular graph nodes do not validate narrative molecules, localization,
    mechanism, taxon transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-contractile_vacuole-verify
- check_id: contractile_vacuole-uniprot-causal
  name: Native contractile vacuole UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0000331
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/contractile_vacuole.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Missing anchors/examples, empty inventories
    and zero molecular graph nodes do not validate narrative molecules, localization,
    mechanism, taxon transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-contractile_vacuole-causal
- check_id: contractile_vacuole_complex-uniprot-verify
  name: Native contractile vacuole complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0062159
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/contractile_vacuole_complex.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Missing anchors/examples, empty inventories
    and zero molecular graph nodes do not validate narrative molecules, localization,
    mechanism, taxon transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-contractile_vacuole_complex-verify
- check_id: contractile_vacuole_complex-uniprot-causal
  name: Native contractile vacuole complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0062159
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/contractile_vacuole_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Missing anchors/examples, empty inventories
    and zero molecular graph nodes do not validate narrative molecules, localization,
    mechanism, taxon transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-contractile_vacuole_complex-causal
- check_id: contractile_vacuole_lumen-uniprot-verify
  name: Native contractile vacuole lumen UniProt verify check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:contractile_vacuole_lumen
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/contractile_vacuole_lumen.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Missing anchors/examples, empty inventories
    and zero molecular graph nodes do not validate narrative molecules, localization,
    mechanism, taxon transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-contractile_vacuole_lumen-verify
- check_id: contractile_vacuole_lumen-uniprot-causal
  name: Native contractile vacuole lumen UniProt causal check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:contractile_vacuole_lumen
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/contractile_vacuole_lumen.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Missing anchors/examples, empty inventories
    and zero molecular graph nodes do not validate narrative molecules, localization,
    mechanism, taxon transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-contractile_vacuole_lumen-causal
- check_id: contractile_vacuole_pore-uniprot-verify
  name: Native contractile vacuole pore UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0031913
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/contractile_vacuole_pore.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Missing anchors/examples, empty inventories
    and zero molecular graph nodes do not validate narrative molecules, localization,
    mechanism, taxon transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-contractile_vacuole_pore-verify
- check_id: contractile_vacuole_pore-uniprot-causal
  name: Native contractile vacuole pore UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0031913
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/contractile_vacuole_pore.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Missing anchors/examples, empty inventories
    and zero molecular graph nodes do not validate narrative molecules, localization,
    mechanism, taxon transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-contractile_vacuole_pore-causal
- check_id: copi_coated_vesicle-uniprot-verify
  name: Native copi coated vesicle UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0030137
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/copi_coated_vesicle.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Missing anchors/examples, empty inventories
    and zero molecular graph nodes do not validate narrative molecules, localization,
    mechanism, taxon transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-copi_coated_vesicle-verify
- check_id: copi_coated_vesicle-uniprot-causal
  name: Native copi coated vesicle UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0030137
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/copi_coated_vesicle.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Missing anchors/examples, empty inventories
    and zero molecular graph nodes do not validate narrative molecules, localization,
    mechanism, taxon transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-copi_coated_vesicle-causal
- check_id: copi_coated_vesicle_lumen-uniprot-verify
  name: Native copi coated vesicle lumen UniProt verify check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:copi_coated_vesicle_lumen
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/copi_coated_vesicle_lumen.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Missing anchors/examples, empty inventories
    and zero molecular graph nodes do not validate narrative molecules, localization,
    mechanism, taxon transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-copi_coated_vesicle_lumen-verify
- check_id: copi_coated_vesicle_lumen-uniprot-causal
  name: Native copi coated vesicle lumen UniProt causal check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:copi_coated_vesicle_lumen
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/copi_coated_vesicle_lumen.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Missing anchors/examples, empty inventories
    and zero molecular graph nodes do not validate narrative molecules, localization,
    mechanism, taxon transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-copi_coated_vesicle_lumen-causal
- check_id: copi_coated_vesicle_membrane-uniprot-verify
  name: Native copi coated vesicle membrane UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0030663
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/copi_coated_vesicle_membrane.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Missing anchors/examples, empty inventories
    and zero molecular graph nodes do not validate narrative molecules, localization,
    mechanism, taxon transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-copi_coated_vesicle_membrane-verify
- check_id: copi_coated_vesicle_membrane-uniprot-causal
  name: Native copi coated vesicle membrane UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0030663
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/copi_coated_vesicle_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Missing anchors/examples, empty inventories
    and zero molecular graph nodes do not validate narrative molecules, localization,
    mechanism, taxon transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-copi_coated_vesicle_membrane-causal
- check_id: copii_coated_er_to_golgi_transport_vesicle-uniprot-verify
  name: Native copii coated er to golgi transport vesicle UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0030134
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/copii_coated_er_to_golgi_transport_vesicle.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Missing anchors/examples, empty inventories
    and zero molecular graph nodes do not validate narrative molecules, localization,
    mechanism, taxon transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-copii_coated_er_to_golgi_transport_vesicle-verify
- check_id: copii_coated_er_to_golgi_transport_vesicle-uniprot-causal
  name: Native copii coated er to golgi transport vesicle UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0030134
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/copii_coated_er_to_golgi_transport_vesicle.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Missing anchors/examples, empty inventories
    and zero molecular graph nodes do not validate narrative molecules, localization,
    mechanism, taxon transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-copii_coated_er_to_golgi_transport_vesicle-causal
- check_id: copii_coated_vesicle_lumen-uniprot-verify
  name: Native copii coated vesicle lumen UniProt verify check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:copii_coated_vesicle_lumen
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/copii_coated_vesicle_lumen.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Missing anchors/examples, empty inventories
    and zero molecular graph nodes do not validate narrative molecules, localization,
    mechanism, taxon transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-copii_coated_vesicle_lumen-verify
- check_id: copii_coated_vesicle_lumen-uniprot-causal
  name: Native copii coated vesicle lumen UniProt causal check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:copii_coated_vesicle_lumen
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/copii_coated_vesicle_lumen.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Missing anchors/examples, empty inventories
    and zero molecular graph nodes do not validate narrative molecules, localization,
    mechanism, taxon transfer or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-copii_coated_vesicle_lumen-causal
evidence:
- evidence_id: current-record-0
  kind: record_content
  reference: data/structures/membrane_organelle/contractile_vacuolar_membrane.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T11:24:32Z'
  support: context_only
  summary: Original frozen SHA256 a73ad7ccfc67c7c39a41d555109a229de1c469dec8eff0d808a3cddaa0aa383c;
    current SHA256 a73ad7ccfc67c7c39a41d555109a229de1c469dec8eff0d808a3cddaa0aa383c.
    Record bytes unchanged since the original review.
  snapshot_sha256: a73ad7ccfc67c7c39a41d555109a229de1c469dec8eff0d808a3cddaa0aa383c
- evidence_id: original-review-0
  kind: prior_review
  reference: reviews/structured/20261022T005251Z-contractile-vacuolar-membrane-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T11:24:32Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 0277dc12a05fdf291f94a1fc983a973c151af82e33f3a6375bea7e4900406ad8
- evidence_id: current-record-1
  kind: record_content
  reference: data/structures/membrane_organelle/contractile_vacuole.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T11:24:32Z'
  support: context_only
  summary: Original frozen SHA256 d1057e9c19ff100f054c73da52b597742dadde491f2a007cd7b648b8a7b626bb;
    current SHA256 d1057e9c19ff100f054c73da52b597742dadde491f2a007cd7b648b8a7b626bb.
    Record bytes unchanged since the original review.
  snapshot_sha256: d1057e9c19ff100f054c73da52b597742dadde491f2a007cd7b648b8a7b626bb
- evidence_id: original-review-1
  kind: prior_review
  reference: reviews/structured/20261022T005252Z-contractile-vacuole-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T11:24:32Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: a49af232ae1b9a295c0885c7b34b7598c296a7a58c97f574f5060dc5dbd7d274
- evidence_id: current-record-2
  kind: record_content
  reference: data/structures/membrane_organelle/contractile_vacuole_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T11:24:32Z'
  support: context_only
  summary: Original frozen SHA256 5d37be1aa899c1bfd20611faeafefb842a96e8a21144dea9e010b2c89d4b7a1c;
    current SHA256 5d37be1aa899c1bfd20611faeafefb842a96e8a21144dea9e010b2c89d4b7a1c.
    Record bytes unchanged since the original review.
  snapshot_sha256: 5d37be1aa899c1bfd20611faeafefb842a96e8a21144dea9e010b2c89d4b7a1c
- evidence_id: original-review-2
  kind: prior_review
  reference: reviews/structured/20261022T005253Z-contractile-vacuole-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T11:24:32Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 014d1929ae5fa35fbf1e8bde740d1b27fccb3f5eb0088e93434a8e6be43baac2
- evidence_id: current-record-3
  kind: record_content
  reference: data/structures/membrane_organelle/contractile_vacuole_lumen.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T11:24:32Z'
  support: context_only
  summary: Original frozen SHA256 9c85ec352245d16e963b9d86d4d1cf0b41d499b956b0b2d05611dca3a4341622;
    current SHA256 9c85ec352245d16e963b9d86d4d1cf0b41d499b956b0b2d05611dca3a4341622.
    Record bytes unchanged since the original review.
  snapshot_sha256: 9c85ec352245d16e963b9d86d4d1cf0b41d499b956b0b2d05611dca3a4341622
- evidence_id: original-review-3
  kind: prior_review
  reference: reviews/structured/20261022T005253Z-contractile-vacuole-lumen-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T11:24:32Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 41e6d3fb48280dc9ff59b67b9d1c7f24f788238da006beb62ee7fbcd2026b014
- evidence_id: current-record-4
  kind: record_content
  reference: data/structures/membrane_organelle/contractile_vacuole_pore.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T11:24:32Z'
  support: context_only
  summary: Original frozen SHA256 e6b016675a36c215388bfd9053da4af4b1ec407c47c197f8a2217f9ba66cc294;
    current SHA256 e6b016675a36c215388bfd9053da4af4b1ec407c47c197f8a2217f9ba66cc294.
    Record bytes unchanged since the original review.
  snapshot_sha256: e6b016675a36c215388bfd9053da4af4b1ec407c47c197f8a2217f9ba66cc294
- evidence_id: original-review-4
  kind: prior_review
  reference: reviews/structured/20261022T005254Z-contractile-vacuole-pore-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T11:24:32Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 5fd85190f80c5a4cbb92129bc5c78f4f731e2c37f6e269541ef56d19661e7329
- evidence_id: current-record-5
  kind: record_content
  reference: data/structures/membrane_organelle/copi_coated_vesicle.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T11:24:32Z'
  support: context_only
  summary: Original frozen SHA256 c8cf402aeadf4fea155d4735ed1df973e319b23d46664cd7ec286ba385c1a250;
    current SHA256 d542d1063731ec276cf5e771752715152ad950ee3fd1819f24e1a792036f2981.
    Changed record reassessed against current sources.
  snapshot_sha256: d542d1063731ec276cf5e771752715152ad950ee3fd1819f24e1a792036f2981
- evidence_id: original-review-5
  kind: prior_review
  reference: reviews/structured/20261022T005255Z-copi-coated-vesicle-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T11:24:32Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 69afa3c09645dc5c26a0b183faaad7e1a68596333cddbd44c6b99603ce7b93e3
- evidence_id: current-record-6
  kind: record_content
  reference: data/structures/membrane_organelle/copi_coated_vesicle_lumen.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T11:24:32Z'
  support: context_only
  summary: Original frozen SHA256 f4da3395ba3aa5bfa65d859069e5b2f5d15303f81d7da6048291813188d9bcfa;
    current SHA256 f4da3395ba3aa5bfa65d859069e5b2f5d15303f81d7da6048291813188d9bcfa.
    Record bytes unchanged since the original review.
  snapshot_sha256: f4da3395ba3aa5bfa65d859069e5b2f5d15303f81d7da6048291813188d9bcfa
- evidence_id: original-review-6
  kind: prior_review
  reference: reviews/structured/20261022T005255Z-copi-coated-vesicle-lumen-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T11:24:32Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 603b2c78ebc683f9133c8fd353aa17cc1de2766aec9d4e2066a259df2cb6789d
- evidence_id: current-record-7
  kind: record_content
  reference: data/structures/membrane_organelle/copi_coated_vesicle_membrane.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T11:24:32Z'
  support: context_only
  summary: Original frozen SHA256 70dbc868044797a3911de45524d13ccbedb5bf9cc671824b0dcade909ab4922f;
    current SHA256 70dbc868044797a3911de45524d13ccbedb5bf9cc671824b0dcade909ab4922f.
    Record bytes unchanged since the original review.
  snapshot_sha256: 70dbc868044797a3911de45524d13ccbedb5bf9cc671824b0dcade909ab4922f
- evidence_id: original-review-7
  kind: prior_review
  reference: reviews/structured/20261022T005256Z-copi-coated-vesicle-membrane-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T11:24:32Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 07c380bffaa4ad7419dab5e93152ad58d831f9b6b06b2f46c5a13418689b0571
- evidence_id: current-record-8
  kind: record_content
  reference: data/structures/membrane_organelle/copii_coated_er_to_golgi_transport_vesicle.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T11:24:32Z'
  support: context_only
  summary: Original frozen SHA256 141713f26c4f5cc6a2e6c6cb232bf45e194df53bcd60aa4769cc4343ac6599bf;
    current SHA256 141713f26c4f5cc6a2e6c6cb232bf45e194df53bcd60aa4769cc4343ac6599bf.
    Record bytes unchanged since the original review.
  snapshot_sha256: 141713f26c4f5cc6a2e6c6cb232bf45e194df53bcd60aa4769cc4343ac6599bf
- evidence_id: original-review-8
  kind: prior_review
  reference: reviews/structured/20261022T005257Z-copii-coated-er-to-golgi-transport-vesicle-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T11:24:32Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: f7831dc05724e26491c81ef3c0ae1f2081f9e7930c2719d1cc183c641abc984d
- evidence_id: current-record-9
  kind: record_content
  reference: data/structures/membrane_organelle/copii_coated_vesicle_lumen.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T11:24:32Z'
  support: context_only
  summary: Original frozen SHA256 d75ae8e81d2fc08979408842f74ef1ad621e87108044faf2dcc6ca216e5e7782;
    current SHA256 d75ae8e81d2fc08979408842f74ef1ad621e87108044faf2dcc6ca216e5e7782.
    Record bytes unchanged since the original review.
  snapshot_sha256: d75ae8e81d2fc08979408842f74ef1ad621e87108044faf2dcc6ca216e5e7782
- evidence_id: original-review-9
  kind: prior_review
  reference: reviews/structured/20261022T005258Z-copii-coated-vesicle-lumen-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T11:24:32Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 845568d3b865725c92b2382779d89fa342e12252cf7fa80f4dd929e87b5df3a3
- evidence_id: plaque-current-3
  kind: record_content
  reference: data/structures/membrane_organelle/contractile_vacuole_lumen.yaml
  locator: Entire maintained record at source 7081777bba0daacfa48fc6d826cdfd7138e751b4;
    all fields, histories, discussions and graphs
  summary: Complete current target read. Hash is unchanged from original frozen target;
    PROPOSED status remains and no record curation is performed.
  accessed_at: '2026-11-03T11:22:45.443173Z'
  support: supports
  snapshot_sha256: 9c85ec352245d16e963b9d86d4d1cf0b41d499b956b0b2d05611dca3a4341622
- evidence_id: plaque-original-3
  kind: prior_review
  reference: reviews/structured/20261022T005253Z-contractile-vacuole-lumen-audit/review.yaml
  locator: Original authoritative YAML, rendered Markdown, all frozen inputs, assessments,
    checks, findings/actions and limitations
  summary: Original validates and renders byte-identically. All historical frozen
    inputs match original source commits; current target hash also matches. Original
    verdict pass_with_limitations, with no findings or curation actions.
  accessed_at: '2026-11-03T11:22:45.443173Z'
  support: supports
  snapshot_sha256: 41e6d3fb48280dc9ff59b67b9d1c7f24f788238da006beb62ee7fbcd2026b014
- evidence_id: plaque-current-4
  kind: record_content
  reference: data/structures/membrane_organelle/contractile_vacuole_pore.yaml
  locator: Entire maintained record at source 7081777bba0daacfa48fc6d826cdfd7138e751b4;
    all fields, histories, discussions and graphs
  summary: Complete current target read. Hash is unchanged from original frozen target;
    PROPOSED status remains and no record curation is performed.
  accessed_at: '2026-11-03T11:22:45.443173Z'
  support: supports
  snapshot_sha256: e6b016675a36c215388bfd9053da4af4b1ec407c47c197f8a2217f9ba66cc294
- evidence_id: plaque-original-4
  kind: prior_review
  reference: reviews/structured/20261022T005254Z-contractile-vacuole-pore-audit/review.yaml
  locator: Original authoritative YAML, rendered Markdown, all frozen inputs, assessments,
    checks, findings/actions and limitations
  summary: Original validates and renders byte-identically. All historical frozen
    inputs match original source commits; current target hash also matches. Original
    verdict pass_with_limitations, with no findings or curation actions.
  accessed_at: '2026-11-03T11:22:45.443173Z'
  support: supports
  snapshot_sha256: 5fd85190f80c5a4cbb92129bc5c78f4f731e2c37f6e269541ef56d19661e7329
- evidence_id: plaque-current-8
  kind: record_content
  reference: data/structures/membrane_organelle/copii_coated_er_to_golgi_transport_vesicle.yaml
  locator: Entire maintained record at source 7081777bba0daacfa48fc6d826cdfd7138e751b4;
    all fields, histories, discussions and graphs
  summary: Complete current target read. Hash is unchanged from original frozen target;
    PROPOSED status remains and no record curation is performed.
  accessed_at: '2026-11-03T11:22:45.443173Z'
  support: supports
  snapshot_sha256: 141713f26c4f5cc6a2e6c6cb232bf45e194df53bcd60aa4769cc4343ac6599bf
- evidence_id: plaque-original-8
  kind: prior_review
  reference: reviews/structured/20261022T005257Z-copii-coated-er-to-golgi-transport-vesicle-audit/review.yaml
  locator: Original authoritative YAML, rendered Markdown, all frozen inputs, assessments,
    checks, findings/actions and limitations
  summary: Original validates and renders byte-identically. All historical frozen
    inputs match original source commits; current target hash also matches. Original
    verdict pass_with_limitations, with no findings or curation actions.
  accessed_at: '2026-11-03T11:22:45.443173Z'
  support: supports
  snapshot_sha256: f7831dc05724e26491c81ef3c0ae1f2081f9e7930c2719d1cc183c641abc984d
- evidence_id: plaque-current-9
  kind: record_content
  reference: data/structures/membrane_organelle/copii_coated_vesicle_lumen.yaml
  locator: Entire maintained record at source 7081777bba0daacfa48fc6d826cdfd7138e751b4;
    all fields, histories, discussions and graphs
  summary: Complete current target read. Hash is unchanged from original frozen target;
    PROPOSED status remains and no record curation is performed.
  accessed_at: '2026-11-03T11:22:45.443173Z'
  support: supports
  snapshot_sha256: d75ae8e81d2fc08979408842f74ef1ad621e87108044faf2dcc6ca216e5e7782
- evidence_id: plaque-original-9
  kind: prior_review
  reference: reviews/structured/20261022T005258Z-copii-coated-vesicle-lumen-audit/review.yaml
  locator: Original authoritative YAML, rendered Markdown, all frozen inputs, assessments,
    checks, findings/actions and limitations
  summary: Original validates and renders byte-identically. All historical frozen
    inputs match original source commits; current target hash also matches. Original
    verdict pass_with_limitations, with no findings or curation actions.
  accessed_at: '2026-11-03T11:22:45.443173Z'
  support: supports
  snapshot_sha256: 845568d3b865725c92b2382779d89fa342e12252cf7fa80f4dd929e87b5df3a3
- evidence_id: plaque-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Frozen native evidence, structure identity, component, graph and structured-source
    applicability contract
  summary: Named molecular, pathway, stress-response or trait narratives trigger applicability
    assessment; absence of expression inference alone does not justify exemption.
    Structural topology without those assertions can be genuinely excluded.
  accessed_at: '2026-11-03T11:22:45.443173Z'
  support: context_only
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: plaque-rubric
  kind: authority
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Frozen native evidence, structure identity, component, graph and structured-source
    applicability contract
  summary: Named molecular, pathway, stress-response or trait narratives trigger applicability
    assessment; absence of expression inference alone does not justify exemption.
    Structural topology without those assertions can be genuinely excluded.
  accessed_at: '2026-11-03T11:22:45.443173Z'
  support: context_only
  snapshot_sha256: e6b9e4b16a58c54402bed7bbee2c8b94a91d37562e8b0ee8b94ff0c829184a70
- evidence_id: plaque-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Frozen native evidence, structure identity, component, graph and structured-source
    applicability contract
  summary: Named molecular, pathway, stress-response or trait narratives trigger applicability
    assessment; absence of expression inference alone does not justify exemption.
    Structural topology without those assertions can be genuinely excluded.
  accessed_at: '2026-11-03T11:22:45.443173Z'
  support: context_only
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: plaque-schema-policy
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Frozen native evidence, structure identity, component, graph and structured-source
    applicability contract
  summary: Named molecular, pathway, stress-response or trait narratives trigger applicability
    assessment; absence of expression inference alone does not justify exemption.
    Structural topology without those assertions can be genuinely excluded.
  accessed_at: '2026-11-03T11:22:45.443173Z'
  support: context_only
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: plaque-neighbor-0
  kind: record_content
  reference: data/structures/membrane_organelle/contractile_vacuolar_membrane.yaml
  locator: Identifier, label, definition, structure_kind, parent_structures, part_of
    and has_part only
  summary: Frozen cohort context distinguishes contractile vacuolar membrane, whole
    vacuole and vacuole complex. No independent full-science review, historical resolution
    or sibling finding disposition is inferred.
  accessed_at: '2026-11-03T11:22:45.443173Z'
  support: context_only
  snapshot_sha256: a73ad7ccfc67c7c39a41d555109a229de1c469dec8eff0d808a3cddaa0aa383c
- evidence_id: plaque-neighbor-1
  kind: record_content
  reference: data/structures/membrane_organelle/contractile_vacuole.yaml
  locator: Identifier, label, definition, structure_kind, parent_structures, part_of
    and has_part only
  summary: Frozen cohort context distinguishes contractile vacuolar membrane, whole
    vacuole and vacuole complex. No independent full-science review, historical resolution
    or sibling finding disposition is inferred.
  accessed_at: '2026-11-03T11:22:45.443173Z'
  support: context_only
  snapshot_sha256: d1057e9c19ff100f054c73da52b597742dadde491f2a007cd7b648b8a7b626bb
- evidence_id: plaque-neighbor-2
  kind: record_content
  reference: data/structures/membrane_organelle/contractile_vacuole_complex.yaml
  locator: Identifier, label, definition, structure_kind, parent_structures, part_of
    and has_part only
  summary: Frozen cohort context distinguishes contractile vacuolar membrane, whole
    vacuole and vacuole complex. No independent full-science review, historical resolution
    or sibling finding disposition is inferred.
  accessed_at: '2026-11-03T11:22:45.443173Z'
  support: context_only
  snapshot_sha256: 5d37be1aa899c1bfd20611faeafefb842a96e8a21144dea9e010b2c89d4b7a1c
- evidence_id: plaque-contractile-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031164,GO:0005774,GO:0000331,GO:0062159,GO:0062160,GO:0043232,GO:0005775,GO:0031913,GO:0098797,GO:0005856
  locator: 'All ten requested active GO terms: exact names, definitions, typed children
    and immediate parent/parthood distinctions'
  summary: GO0005775 is the broader vacuolar lumen;0000331 the containing contractile
    vacuole;0031164 its membrane. Whole vacuole, its complex0062159 and spongiome0062160
    are distinct. Same-PR public snapshot independently reread; original actual fetch
    time retained.
  accessed_at: '2026-11-03T11:16:55.831372Z'
  support: supports
  snapshot_sha256: 3001e9aa0de9d2828e1a1a727af2c84d192398885fe3080a1f75b13f34bad99a
- evidence_id: plaque-contractile-agent-SL-0320
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0320.json
  locator: Exact definition, synonym, direct isA/partOf and GO correspondences distinguished
    from nested ancestor objects
  summary: SL0320 defines the contractile-vacuole compartment bounded by its membrane;
    exact contractile vacuolar lumen synonym, vacuolar-lumen parent and whole-vacuole
    parthood match. Nested SL0073 wording does not erase the separate GO whole/complex
    identities.
  accessed_at: '2026-11-03T11:17:04.701084Z'
  support: supports
  snapshot_sha256: 15bcef9dacd1cd9ae0614f3ab9da225a2e53c0259e083d3535f5b223fd9d9771
- evidence_id: plaque-contractile-agent-go-lumen-search
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=contractile%20vacuole%20lumen&limit=100
  locator: All100 returned first-page IDs and labels; exact query and total hit count
  summary: No exact contractile-vacuole-lumen label among this bounded returned page.
    Broader vacuolar lumen and specific unrelated lumina are not exact replacements.
    No exhaustive ontology absence is claimed.
  accessed_at: '2026-11-03T11:17:04.701141Z'
  support: context_only
  search_scope: QuickGO search; query=contractile vacuole lumen; accessed 2026-11-03T11:17:04.701141Z;
    page1,limit100;398 total hits; all first100 inspected, remaining pages not queried.
  snapshot_sha256: 47df92545b845b05013e72ad32873b1d1ef78e80fa1c628d17f48efbebe62ba3
- evidence_id: plaque-contractile-agent-tax-2759
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759
  locator: Exact current taxId, scientificName, rank, lineage and alternative names
  summary: Authority identifies Eukaryota 2759. Taxonomy alone does not establish
    occurrence, strain identity or numerical prevalence. Same-PR shared source timestamps,
    where applicable, are retained.
  accessed_at: '2026-11-03T11:16:55.831775Z'
  support: supports
  snapshot_sha256: 61a68c76c70762c97e0b218568ab037d9a30c0207847247e9e055b5764a61634
- evidence_id: plaque-contractile-agent-tax-44030
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/44030
  locator: Exact current taxId, scientificName, rank, lineage and alternative names
  summary: Authority identifies Paramecium multimicronucleatum 44030. Taxonomy alone
    does not establish occurrence, strain identity or numerical prevalence. Same-PR
    shared source timestamps, where applicable, are retained.
  accessed_at: '2026-11-03T11:17:03.988574Z'
  support: supports
  snapshot_sha256: 4be4e352120325ebd0564f246f7c6af841f2f1a81fbf3b2f6db5c11d7c0393d7
- evidence_id: plaque-contractile-agent-tax-3055
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3055
  locator: Exact current taxId, scientificName, rank, lineage and alternative names
  summary: Authority identifies Chlamydomonas reinhardtii 3055. Taxonomy alone does
    not establish occurrence, strain identity or numerical prevalence. Same-PR shared
    source timestamps, where applicable, are retained.
  accessed_at: '2026-11-03T11:16:58.508907Z'
  support: supports
  snapshot_sha256: a24c8f85014097148d9e865ea324b01b8d04f6bae27e893834f8abb5bd8b6a1f
- evidence_id: plaque-root24-sources-NCBITaxon-5911
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5911
  locator: Exact current taxId, scientificName, rank, lineage and alternative names
  summary: Authority identifies Tetrahymena thermophila 5911. Taxonomy alone does
    not establish occurrence, strain identity or numerical prevalence. Same-PR shared
    source timestamps, where applicable, are retained.
  accessed_at: '2026-11-03T11:17:04.708287Z'
  support: supports
  snapshot_sha256: e848a1295088ad42e73c4c2c42d45869b4c9c2b10858e2c32086dc67b066a8c5
- evidence_id: plaque-copii-agent-tax4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Exact current taxId, scientificName, rank, lineage and alternative names
  summary: Authority identifies Saccharomyces cerevisiae 4932. Taxonomy alone does
    not establish occurrence, strain identity or numerical prevalence. Same-PR shared
    source timestamps, where applicable, are retained.
  accessed_at: '2026-11-03T11:17:05.711046Z'
  support: supports
  snapshot_sha256: d930c884e1154be4c050977652c0d6baf3666d183a90fa17ead8d01cce2c770f
- evidence_id: plaque-contractile-agent-more2024-meta
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016%2Fj.ejop.2024.126078
  locator: Complete secondary-review abstract and exact title/authors/year/DOI metadata
  summary: More2024 describes diversity and uneven occurrence of contractile vacuoles
    among eukaryotes, including freshwater/soil context. It is secondary abstract
    evidence, not an inspected full body or a quantitative prevalence census. Shared
    same-PR public snapshot independently inspected.
  accessed_at: '2026-11-03T11:16:55.831678Z'
  support: supports
  snapshot_sha256: 46fafe4ca983c67438501002db300546d269a9ff60db3c0d5987d25f94cfd119
- evidence_id: plaque-contractile-agent-allen2002-title
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=TITLE%3A%22Osmoregulation%20and%20contractile%20vacuoles%20of%20protozoa%22
  locator: Complete secondary-review abstract and exact title/DOI/authors/year metadata
  summary: Allen/Naitoh2002 describes compartmental filling followed by periodic liquid
    discharge and distinct collecting/reservoir systems. It supports broad cyclic
    function, not a uniform architecture or exact component inventory across protists.
    Shared snapshot independently reread; body unavailable.
  accessed_at: '2026-11-03T11:16:57.467646Z'
  support: supports
  snapshot_sha256: ea88a1f4d0631757324caecc2046764fa6193a4578dde07f8f2f20b0c3f4ee39
- evidence_id: plaque-contractile-agent-gronlien2002-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1242%2Fjeb.205.20.3261
  locator: Complete primary abstract plus exact title/authors/year/DOI metadata
  summary: Gronlien2002 used a microelectrode in the CV against a cytosolic reference
    in mechanically compressed Paramecium multimicronucleatum; measured filling-associated
    membrane-potential dynamics. The lumen example stays within that scope, without
    asserting universal species behavior or direct lumen osmolarity measurement. Primary
    abstract only.
  accessed_at: '2026-11-03T11:17:03.654464Z'
  support: supports
  snapshot_sha256: ab401a043a983f8df0b7e1d4febcc3a466046facdaf6c68035ffad0dc0993bfd
- evidence_id: plaque-contractile-agent-komsic2014-pmc-numeric
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/4248701/
  locator: Primary HTML Abstract, Introduction, Methods, Results, Discussion, Table1
    and Figure1–9 captions as text; Results Water uptake into the CV reread directly
    from section3-4
  summary: Komsic2014 measures cell/CV sizes and contraction intervals across osmotic
    media in CC3395 and examines UVM4 derivatives. CV volume correlates with cell
    size/growth, not medium osmolarity; interval tracks osmolarity. Lumen osmolarity/permeability
    are modeled, not directly measured. The lumen wording describes measurements under
    altered osmolarity and separately osmolarity-responsive cycles, not a causal size–osmolarity
    relationship. Shared same-PR body independently read with original retrieval timestamp;
    no figure pixels, supplemental movies or raw-data reanalysis.
  accessed_at: '2026-11-03T11:16:57.763169Z'
  support: supports
  snapshot_sha256: dd945cffbbbc689e28c5a0a7e4ca794d3427a5973a43702dd796d65513506da4
- evidence_id: plaque-root24-sources-pore-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005856,GO:0031164,GO:0031913,GO:0098797
  locator: All four exact term identities/definitions; direct typed child relations,
    active status and GO0031913 definition PMID10503189
  summary: GO0031913 is the stable liquid-flow-regulating contractile vacuole pore.
    GO0098797 has the pore as an is_a child; GO0031164 and GO0005856 have it as a
    part_of child. Broad ontology complex classification does not supply an experimentally
    identified subunit inventory.
  accessed_at: '2026-11-03T11:17:04.702968Z'
  support: supports
  snapshot_sha256: d14b3bddf05a15bf4e17af18864ef860a59a9c2fcce46291f06f4ee3968fb30b
- evidence_id: plaque-root24-sources-pore-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031913/ancestors?relations=is_a,part_of
  locator: Bounded is_a,part_of ancestor response as mixed closure
  summary: Mixed ancestor closure is only context. Exact relation types are checked
    against direct typed child entries in the separate four-term source, not inferred
    from this untyped ancestor list.
  accessed_at: '2026-11-03T11:17:04.706483Z'
  support: context_only
  snapshot_sha256: 4a11f0c59e8fe1713f53f5ab5b209a6561842f348916b347ddea43698938070f
- evidence_id: plaque-root24-sources-frankel2000-pmid
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID:10503189%20AND%20SRC:MED
  locator: 'Exact identifier query: title, authors, year, DOI/PMID and available abstract'
  summary: 'Bibliography verified: Cell biology of Tetrahymena thermophila.; Frankel
    J.; 2000. Primary/secondary body scopes are separately declared. Exact identifiers
    do not imply full-body access.'
  accessed_at: '2026-11-03T11:17:04.883929Z'
  support: supports
  snapshot_sha256: bbddf4df91f90d17e89a02811f28cfcfe6a92033c26e8e1b89d730bc86f186ee
- evidence_id: plaque-root24-sources-frankel2000-quoteddoi
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI:%2210.1016/S0091-679X(08)61528-9%22
  locator: 'Exact identifier query: title, authors, year, DOI/PMID and available abstract'
  summary: 'Bibliography verified: Cell biology of Tetrahymena thermophila.; Frankel
    J.; 2000. Primary/secondary body scopes are separately declared. Exact identifiers
    do not imply full-body access.'
  accessed_at: '2026-11-03T11:17:05.071571Z'
  support: supports
  snapshot_sha256: fe3ae541b1471f03cb8561839e7120df46c9586b5384310f026cadad5e6e9fc8
- evidence_id: plaque-root24-sources-doi-10.1111_j.1550-7408.1973.tb03587.x
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1111/j.1550-7408.1973.tb03587.x
  locator: 'Exact identifier query: title, authors, year, DOI/PMID and available abstract'
  summary: 'Bibliography verified: Fine structure of the contractile vacuole pore
    in Paramecium.; McKanna JA.; 1973. Primary/secondary body scopes are separately
    declared. Exact identifiers do not imply full-body access.'
  accessed_at: '2026-11-03T11:17:05.305363Z'
  support: supports
  snapshot_sha256: 83bffb09f8dcbe167c359d9d51c21c0bc5a3e1e2bace220af7898423cfef3c8c
- evidence_id: plaque-copii-agent-PMID-9568718
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A9568718%20AND%20SRC%3AMED
  locator: 'Exact identifier query: title, authors, year, DOI/PMID and available abstract'
  summary: 'Bibliography verified: COPII-coated vesicle formation reconstituted with
    purified coat proteins and chemically defined liposomes.; Matsuoka K, Orci L,
    Amherdt M, Bednarek SY, Hamamoto S, Schekman R, Yeung T.; 1998. Primary/secondary
    body scopes are separately declared. Exact identifiers do not imply full-body
    access.'
  accessed_at: '2026-11-03T11:17:05.893698Z'
  support: supports
  snapshot_sha256: 0cdaf91dc4f4bf9261f55530522a8ed41116b930c39ac656de0d729c318bf1c0
- evidence_id: plaque-root24-sources-doi-10.1016_S0091-679X_08_61528-9
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/S0091-679X%2808%2961528-9
  locator: Actual zero-result response from unquoted DOI syntax; corrected quoted
    query separately succeeds
  summary: Zero hits from this syntax are an access/query limitation, not evidence
    that the DOI or chapter is absent.
  accessed_at: '2026-11-03T11:17:05.118867Z'
  support: context_only
  search_scope: EuropePMC exact unquoted DOI query 10.1016/S0091-679X(08)61528-9;
    accessed 2026-11-03T11:17:05.118867Z; one native returned page,default page size25,0hits;
    quoted exact DOI query performed separately.
  snapshot_sha256: e386d67df522635be61ce827a274a5dcbc85954283a3b8da7c477edc5a485e40
- evidence_id: plaque-root24-sources-frankel2000-university-pdf
  kind: authority
  reference: https://chemotaxis.semmelweis.hu/CHTXhpg/Bookshelf/Tetrahymena/Tetrahymena_thermophila_Methods_2000.pdf
  locator: 'Genuine institutional book PDF: Chapter2 identity, complete II.F Contractile-Vacuole
    System pp51–52 and III.B.1.b Contractile Vacuole Pore and Cytoproct; opening V.B.1.b
    positioning paragraphs'
  summary: Secondary Frankel chapter on Tetrahymena thermophila describes persistent
    cortical discharge sites, circular/radial microtubules and apposed-membrane diaphragm.
    Tetrahymena thermophila is a review-supported model example; older cited work
    on T.pyriformis is not relabeled as new thermophila primary observations. Only
    named chapter sections, not the full book or figure pixels, were inspected.
  accessed_at: '2026-11-03T11:17:05.294755Z'
  support: supports
  snapshot_sha256: 48598713aee2c6aabd3c6aaf8f3085f7fc12824dd5c9fa0592f71ccc9716c615
- evidence_id: plaque-root24-sources-mckanna1973-crossref
  kind: primary_source
  reference: https://api.crossref.org/works/10.1111/j.1550-7408.1973.tb03587.x
  locator: Publisher-deposited complete primary synopsis/abstract, title, authors,
    journal, year and DOI
  summary: McKanna1973 describes Paramecium pore cylindrical structure, diastolic
    diaphragm, systolic opening, contiguous membrane and microtubule annulus/radial
    bands. It supports genus-level structural context; the synopsis does not identify
    an experimental species or demonstrate a universal molecular pore inventory. Full
    article inaccessible.
  accessed_at: '2026-11-03T11:17:05.310539Z'
  support: supports
  snapshot_sha256: 51856ef9e197e03ac04ff19bea4f69dcb5120796b7ae78b99d21969173378035
- evidence_id: plaque-copii-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030134,GO:0030135,GO:0030127,GO:0090114,GO:0006888,GO:0005789,GO:0005794,GO:0060205,GO:0012507
  locator: All nine requested active terms, definitions, synonyms and exact typed
    child relations
  summary: GO0030134 identifies whole COPII-coated ER-to-Golgi vesicle;0030135 parent
    and0030127 coat distinction agree. GO0090114 is ER-membrane evagination in budding;0006888
    is ER-to-Golgi transport, not the vesicle forming itself. GO0012507 membrane surrounds
    the ER-to-Golgi vesicle;0060205 is the broader cytoplasmic vesicle lumen.
  accessed_at: '2026-11-03T11:17:05.618220Z'
  support: supports
  snapshot_sha256: 3b391d054f6f355480cf0c55d0e10b4ea88dd6b250c3683c60587ddc62cb77c6
- evidence_id: plaque-copii-agent-SL-0322
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0322.json
  locator: Exact definition, complete synonyms, direct isA/partOf and direct GO crossreferences
    distinguished from nested parents
  summary: SL0322 defines COPII-coated vesicle lumen, with Coat protein complexes
    II lumen and ER to Golgi transport vesicle lumen synonyms, cytoplasmic-vesicle-lumen
    parent and whole COPII-vesicle parthood. No direct exact GO crossreference is
    supplied.
  accessed_at: '2026-11-03T11:17:06.100815Z'
  support: supports
  snapshot_sha256: 1e9227774ff93659e52c60dde84a590d43591d0e4ac5d3c190b446db015b889f
- evidence_id: plaque-copii-agent-go-lumen-candidates
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0106172,GO:0106173,GO:0106174
  locator: Exact active candidate terms0106172–0106174; labels, definitions and definition
    citations
  summary: GO0106173 has exact COPII-coated vesicle lumen label but defines a COPII-coated
    endocytic vesicle interior, conflicting with this ER-to-Golgi scope. The active
    conflict remains unknown; the local SL-based identity is not forced into a semantically
    inconsistent GO term. No claim that the candidate is absent or resolved.
  accessed_at: '2026-11-03T11:17:06.166650Z'
  support: supports
  snapshot_sha256: dc88a9d584e1ae86bb88b94724aaa7e1052ffad58276ca960ebdbc5b51e1c782
- evidence_id: plaque-copii-agent-PMID-8004676
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A8004676%20AND%20SRC%3AMED
  locator: Complete primary abstract and exact bibliography
  summary: Barlowe1994 reconstitutes ER budding using Sar1p, Sec13 complex and Sec23
    complex. GTP-generated vesicles target/fuse with Golgi, whereas GMP-PNP vesicles
    fail targeting/fusion. Abstract supports coated transport intermediates and nucleotide-sensitive
    competence, not all synthetic vesicles being physiologically fusion-competent.
    Primary abstract only.
  accessed_at: '2026-11-03T11:17:05.841870Z'
  support: supports
  snapshot_sha256: f3ff438cc130518602efe6aa0252c6d5634fafad949d62cf23e3a6e837819fc7
- evidence_id: plaque-copii-agent-matsuoka1998-author
  kind: primary_source
  reference: https://bednareklab.biochem.wisc.edu/wp-content/uploads/sites/1623/2022/02/1998_Matsuoka_etal_Cell.pdf
  locator: 'Genuine fresh institutional author PDF pp263–274: Summary, Introduction,
    Results, Discussion, Experimental Procedures, Tables1–2 and Figure1–8 captions
    as text'
  summary: Matsuoka1998 distinguishes native urea-washed ER microsome budding and
    defined synthetic-liposome reconstitution with Sar1p/Sec23-24/Sec13-31. Synthetic
    conditions and nucleotide analog are not universal in-vivo necessity. Figure8
    luminal HPTS/DPX retention supports closure without rupture/resealing in the synthetic
    assay; it is not live-yeast lumen microscopy or proof of every cargo route. No
    figure pixel/raw-data reanalysis.
  accessed_at: '2026-11-03T11:17:05.946103Z'
  support: supports
  snapshot_sha256: 4c7e8eafea53f213b25b339d684115bd65a1af9e79d86b9e1222050aa52b0efa
- evidence_id: plaque-access-more2024-publisher
  kind: authority
  reference: https://doi.org/10.1016/j.ejop.2024.126078
  locator: Actual native HTTP response and format/content examined solely for access
    tier
  summary: HTTP200. Redirect, challenge or error response is not an inspected scientific
    full body. Successful secondary Frankel and primary Matsuoka bodies are separately
    identified; other bounded claims retain abstract/synopsis tiers.
  accessed_at: '2026-11-03T11:17:04.700852Z'
  support: context_only
  snapshot_sha256: 39c152a279323c8fddcea53c5aed455c7f3a0f3d51945c4e1b1c8f4f76ed25bb
- evidence_id: plaque-access-gronlien2002-publisher
  kind: authority
  reference: https://doi.org/10.1242/jeb.205.20.3261
  locator: Actual native HTTP response and format/content examined solely for access
    tier
  summary: HTTP403. Redirect, challenge or error response is not an inspected scientific
    full body. Successful secondary Frankel and primary Matsuoka bodies are separately
    identified; other bounded claims retain abstract/synopsis tiers.
  accessed_at: '2026-11-03T11:17:04.701200Z'
  support: context_only
  snapshot_sha256: 7b1b08ea57a145d68b03064a27018f86c4e736c2b6ce665d62df59db4be310d4
- evidence_id: plaque-access-allen2002-publisher
  kind: authority
  reference: https://doi.org/10.1016/S0074-7696(02)15015-7
  locator: Actual native HTTP response and format/content examined solely for access
    tier
  summary: HTTP200. Redirect, challenge or error response is not an inspected scientific
    full body. Successful secondary Frankel and primary Matsuoka bodies are separately
    identified; other bounded claims retain abstract/synopsis tiers.
  accessed_at: '2026-11-03T11:17:04.701525Z'
  support: context_only
  snapshot_sha256: ecc1d4f218b8c031ef1815831f798766028a220881b3654576ab30109c15bfbc
- evidence_id: plaque-root24-sources-frankel2000-publisher
  kind: authority
  reference: https://www.sciencedirect.com/science/chapter/abs/pii/S0091679X08615289
  locator: Actual native HTTP response and format/content examined solely for access
    tier
  summary: HTTP403. Redirect, challenge or error response is not an inspected scientific
    full body. Successful secondary Frankel and primary Matsuoka bodies are separately
    identified; other bounded claims retain abstract/synopsis tiers.
  accessed_at: '2026-11-03T11:17:05.338705Z'
  support: context_only
  snapshot_sha256: c09c1c0d3049c8d5bca79881bee39f2748b89b205ec495a97ab921efc197c222
- evidence_id: plaque-root24-sources-frankel2000-api
  kind: authority
  reference: https://api.elsevier.com/content/article/pii/S0091679X08615289?httpAccept=text/xml
  locator: Actual native HTTP response and format/content examined solely for access
    tier
  summary: HTTP200. Elsevier API supplies bibliographic metadata, not the scientific
    chapter body. Successful secondary Frankel and primary Matsuoka bodies are separately
    identified; other bounded claims retain abstract/synopsis tiers.
  accessed_at: '2026-11-03T11:17:05.429316Z'
  support: context_only
  snapshot_sha256: 5250385de297cf06660172d016d3d68e6cfaab2ec2061267016a220e066e38c4
- evidence_id: plaque-root24-sources-mckanna1973-publisher
  kind: authority
  reference: https://onlinelibrary.wiley.com/doi/10.1111/j.1550-7408.1973.tb03587.x
  locator: Actual native HTTP response and format/content examined solely for access
    tier
  summary: HTTP403. Redirect, challenge or error response is not an inspected scientific
    full body. Successful secondary Frankel and primary Matsuoka bodies are separately
    identified; other bounded claims retain abstract/synopsis tiers.
  accessed_at: '2026-11-03T11:17:05.536304Z'
  support: context_only
  snapshot_sha256: 1a901cae45c51682b3bbf776d456d3eb96a4796299be60fbb167bfe45f59d9db
- evidence_id: plaque-root24-sources-mckanna1973-pdf
  kind: authority
  reference: https://onlinelibrary.wiley.com/doi/pdf/10.1111/j.1550-7408.1973.tb03587.x
  locator: Actual native HTTP response and format/content examined solely for access
    tier
  summary: HTTP403. Redirect, challenge or error response is not an inspected scientific
    full body. Successful secondary Frankel and primary Matsuoka bodies are separately
    identified; other bounded claims retain abstract/synopsis tiers.
  accessed_at: '2026-11-03T11:17:05.574319Z'
  support: context_only
  snapshot_sha256: 2c723d7cf213a6b3539974e2b1573f1aeed012ccabe13fba7fc69008f66c52d0
- evidence_id: plaque-root24-sources-mckanna1973-tdm
  kind: authority
  reference: https://api.wiley.com/onlinelibrary/tdm/v1/articles/10.1111%2Fj.1550-7408.1973.tb03587.x
  locator: Actual native HTTP response and format/content examined solely for access
    tier
  summary: HTTP400. Redirect, challenge or error response is not an inspected scientific
    full body. Successful secondary Frankel and primary Matsuoka bodies are separately
    identified; other bounded claims retain abstract/synopsis tiers.
  accessed_at: '2026-11-03T11:17:05.578499Z'
  support: context_only
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: plaque-copii-agent-barlowe1994-publisher
  kind: authority
  reference: https://www.cell.com/article/0092867494901384/pdf
  locator: Actual native HTTP response and format/content examined solely for access
    tier
  summary: HTTP403. Redirect, challenge or error response is not an inspected scientific
    full body. Successful secondary Frankel and primary Matsuoka bodies are separately
    identified; other bounded claims retain abstract/synopsis tiers.
  accessed_at: '2026-11-03T11:17:05.960800Z'
  support: context_only
  snapshot_sha256: 4330f3efadc1fa34125ff3d8af9a23b57eda03c6a655d4d289f062042e2c9a0a
- evidence_id: plaque-copii-agent-barlowe1994-sciencedirect
  kind: authority
  reference: https://www.sciencedirect.com/science/article/pii/0092867494901384
  locator: Actual native HTTP response and format/content examined solely for access
    tier
  summary: HTTP403. Redirect, challenge or error response is not an inspected scientific
    full body. Successful secondary Frankel and primary Matsuoka bodies are separately
    identified; other bounded claims retain abstract/synopsis tiers.
  accessed_at: '2026-11-03T11:17:05.966998Z'
  support: context_only
  snapshot_sha256: ec73aacca36fa8b5186a5d65b0d8bc3290a0c51c8fd3454ec420bf8b35856c0f
- evidence_id: plaque-catalogue
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Complete current /api/datasets response, all20 organism rows and their
    dataset lists; no pagination
  summary: No dataset organism matches Saccharomyces cerevisiae, Chlamydomonas reinhardtii,
    Paramecium or Tetrahymena. Downstream matched-organism searches/summaries therefore
    do not apply. Unrelated bacterial/archaeal catalogue contexts and absence from
    this database cannot establish biological absence.
  accessed_at: '2026-11-03T11:17:06.247231Z'
  support: supports
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: plaque-historical-runner
  kind: validation
  reference: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb datasets
  locator: Historical00:49Z receipt and exact stdout/stderr independently reread and
    hash-verified
  summary: Historical runner exited1 before datasets due OS PermissionError reading
    pyvenv.cfg. Not a fresh invocation or successful execution; current official catalogue
    is source fallback.
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: plaque-original-checks
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/adversary-plaque/original-checks.json
  locator: Four read-only native validate/render executions and every historical frozen
    input at original source revision
  summary: All four validate and Markdown is byte-exact. Historical inputs18/17/12/12
    all match; all four current target hashes unchanged. Original findings/actions
    empty.
  accessed_at: '2026-11-03T11:20:22.909266Z'
  support: supports
  snapshot_sha256: a5db029b9a1524eb4b5ccb1a9d4b4ea082dbed4719ec8d10a0e5c7740a44eb8f
- evidence_id: plaque-native-contractile_vacuole_lumen-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/contractile_vacuole_lumen.yaml
    --verify
  locator: Actual root-owned native command receipt and stdout independently read/hash-verified
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  accessed_at: '2026-11-03T11:16:58.343053Z'
  support: supports
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: plaque-native-contractile_vacuole_lumen-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/contractile_vacuole_lumen.yaml
    --causal-graphs
  locator: Actual root-owned native command receipt and stdout independently read/hash-verified
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
  accessed_at: '2026-11-03T11:16:58.743661Z'
  support: supports
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
- evidence_id: plaque-native-contractile_vacuole_pore-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/contractile_vacuole_pore.yaml
    --verify
  locator: Actual root-owned native command receipt and stdout independently read/hash-verified
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  accessed_at: '2026-11-03T11:16:59.154175Z'
  support: supports
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: plaque-native-contractile_vacuole_pore-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/contractile_vacuole_pore.yaml
    --causal-graphs
  locator: Actual root-owned native command receipt and stdout independently read/hash-verified
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
  accessed_at: '2026-11-03T11:16:59.571617Z'
  support: supports
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
- evidence_id: plaque-native-copii_coated_er_to_golgi_transport_vesicle-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/copii_coated_er_to_golgi_transport_vesicle.yaml
    --verify
  locator: Actual root-owned native command receipt and stdout independently read/hash-verified
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  accessed_at: '2026-11-03T11:17:02.503950Z'
  support: supports
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: plaque-native-copii_coated_er_to_golgi_transport_vesicle-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/copii_coated_er_to_golgi_transport_vesicle.yaml
    --causal-graphs
  locator: Actual root-owned native command receipt and stdout independently read/hash-verified
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
  accessed_at: '2026-11-03T11:17:02.909976Z'
  support: supports
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
- evidence_id: plaque-native-copii_coated_vesicle_lumen-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/copii_coated_vesicle_lumen.yaml
    --verify
  locator: Actual root-owned native command receipt and stdout independently read/hash-verified
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  accessed_at: '2026-11-03T11:17:03.401034Z'
  support: supports
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: plaque-native-copii_coated_vesicle_lumen-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/copii_coated_vesicle_lumen.yaml
    --causal-graphs
  locator: Actual root-owned native command receipt and stdout independently read/hash-verified
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
  accessed_at: '2026-11-03T11:17:03.825646Z'
  support: supports
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
- evidence_id: micro-review-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Complete native record-review workflow and structured-source applicability
    reread
  accessed_at: '2026-11-03T11:20:03.208844Z'
  summary: Actual molecular/pathway narratives trigger applicability assessment even
    without expression claims. No unmatched dataset or empty query establishes biological
    absence.
  support: context_only
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: micro-review-config
  kind: authority
  reference: conf/record_review.yaml
  locator: Complete current native configuration reread
  accessed_at: '2026-11-03T11:20:03.208844Z'
  summary: Declared routes and four local rubrics remain unchanged. The authoritative
    configuration is included among frozen inputs.
  support: context_only
  snapshot_sha256: d3334a12b8a616a7638f1195748085d2b543fba7df67ad4ff8fcc0ac18f2d3ee
- evidence_id: micro-review-profile
  kind: authority
  reference: docs/record-review-profile.md
  locator: Complete local profile reread; related shared contract and common frozen
    policy bytes checked against prior inspected versions
  accessed_at: '2026-11-03T11:20:03.208844Z'
  summary: Mixed issue-bearing cohorts may retain qualified positive assessments.
    No record mutation, status promotion, fabricated finding or terminal predecessor
    disposition follows from a clean assessment.
  support: context_only
  snapshot_sha256: 6a49c8d35f0a94082a9ad0b8bd8c6a929d85de8339141955f3779bd7ab0eb7e4
- evidence_id: micro-review-checklist
  kind: authority
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Complete field-by-field rubric reread
  accessed_at: '2026-11-03T11:20:03.208844Z'
  summary: Identity, taxon, claim-level source scope, exact partonomy and supported
    directed edges assessed separately from validation.
  support: context_only
  snapshot_sha256: e6b9e4b16a58c54402bed7bbee2c8b94a91d37562e8b0ee8b94ff0c829184a70
- evidence_id: micro-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Complete scope and graph contract reread; unchanged add-cell-structure
    graph policy and native schema retained
  accessed_at: '2026-11-03T11:20:03.208844Z'
  summary: NONMECHANISTIC topology and destination descriptions do not establish fusion
    machinery, kinetic mechanism or specific assembly necessity.
  support: context_only
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: micro-native-schema
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Previously inspected unchanged EssentialityEnum, CausalNode.component_ref
    and source-scope rules
  accessed_at: '2026-11-03T11:20:03.208844Z'
  summary: Collective lipid bilayer constitution is distinct from necessity of individual
    lipid species; a membrane defined as that bilayer may use its collective component_ref.
  support: context_only
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: micro-review-schema
  kind: authority
  reference: schema/record_review.yaml
  locator: Unchanged native schema checked through actual original and scratch-envelope
    validation
  accessed_at: '2026-11-03T11:20:03.208844Z'
  summary: Native assessment area schema; bounded search_scope; complete lineage if
    a finding is present. No original scientific finding exists in these three bundles.
  support: context_only
  snapshot_sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
- evidence_id: micro-neighbor-copi_vesicle_coat
  kind: record_content
  reference: data/structures/other/copi_vesicle_coat.yaml
  locator: Only identifier, label, definition, kind, hierarchy/parthood and component
    identifier/label/type/role/grounding fields
  accessed_at: '2026-11-03T11:20:03.208844Z'
  summary: Frozen before read. Boundary context for coat versus vesicle, bilayer donor
    and ER destination; other scientific claims and any neighbor findings are not
    reviewed or resolved.
  support: supports
  snapshot_sha256: 1b264ad3800f2c5c8c78d327f63a32bdc73888a003e3be3fcad778bb9f993195
- evidence_id: micro-neighbor-endoplasmic_reticulum
  kind: record_content
  reference: data/structures/membrane_organelle/endoplasmic_reticulum.yaml
  locator: Only identifier, label, definition, kind, hierarchy/parthood and component
    identifier/label/type/role/grounding fields
  accessed_at: '2026-11-03T11:20:03.208844Z'
  summary: Frozen before read. Boundary context for coat versus vesicle, bilayer donor
    and ER destination; other scientific claims and any neighbor findings are not
    reviewed or resolved.
  support: supports
  snapshot_sha256: eade1489e38ea7ee989edc3bf5c583e58041b4bfd0ffb9b4acbd666cd98c0160
- evidence_id: micro-neighbor-golgi_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/golgi_membrane.yaml
  locator: Only identifier, label, definition, kind, hierarchy/parthood and component
    identifier/label/type/role/grounding fields
  accessed_at: '2026-11-03T11:20:03.208844Z'
  summary: Frozen before read. Boundary context for coat versus vesicle, bilayer donor
    and ER destination; other scientific claims and any neighbor findings are not
    reviewed or resolved.
  support: supports
  snapshot_sha256: 22a35f67a05738d876923e98adfe54cde34ee23c9009667f48676dca83ba708c
- evidence_id: micro-record-copi_coated_vesicle
  kind: record_content
  reference: data/structures/membrane_organelle/copi_coated_vesicle.yaml
  locator: Complete current YAML at 7081777bba0daacfa48fc6d826cdfd7138e751b4
  accessed_at: '2026-11-03T11:20:03.208844Z'
  summary: All current fields, history, definition, relations, examples, functions,
    evidence, graph edges and discussions read. The whole-vesicle history and destination
    edge changed; all other content remains identical.
  support: supports
  snapshot_sha256: d542d1063731ec276cf5e771752715152ad950ee3fd1819f24e1a792036f2981
- evidence_id: micro-prior-copi_coated_vesicle
  kind: prior_review
  reference: reviews/structured/20261022T005255Z-copi-coated-vesicle-audit/review.yaml
  locator: Entire immutable original YAML, derived Markdown and native validation/render
  accessed_at: '2026-11-03T11:20:03.208844Z'
  summary: Original qualified scientific pass has no findings/actions. Its expression-only
    adapter exclusion is insufficient under native policy. Historical checks retain
    their actual dates; none is recertified as current.
  support: supports
  snapshot_sha256: 69afa3c09645dc5c26a0b183faaad7e1a68596333cddbd44c6b99603ce7b93e3
- evidence_id: micro-record-copi_coated_vesicle_lumen
  kind: record_content
  reference: data/structures/membrane_organelle/copi_coated_vesicle_lumen.yaml
  locator: Complete current YAML at 7081777bba0daacfa48fc6d826cdfd7138e751b4
  accessed_at: '2026-11-03T11:20:03.208844Z'
  summary: All current fields, history, definition, relations, examples, functions,
    evidence, graph edges and discussions read. Original target hash remains current.
  support: supports
  snapshot_sha256: f4da3395ba3aa5bfa65d859069e5b2f5d15303f81d7da6048291813188d9bcfa
- evidence_id: micro-prior-copi_coated_vesicle_lumen
  kind: prior_review
  reference: reviews/structured/20261022T005255Z-copi-coated-vesicle-lumen-audit/review.yaml
  locator: Entire immutable original YAML, derived Markdown and native validation/render
  accessed_at: '2026-11-03T11:20:03.208844Z'
  summary: Original qualified scientific pass has no findings/actions. Its expression-only
    adapter exclusion is insufficient under native policy. Historical checks retain
    their actual dates; none is recertified as current.
  support: supports
  snapshot_sha256: 603b2c78ebc683f9133c8fd353aa17cc1de2766aec9d4e2066a259df2cb6789d
- evidence_id: micro-record-copi_coated_vesicle_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/copi_coated_vesicle_membrane.yaml
  locator: Complete current YAML at 7081777bba0daacfa48fc6d826cdfd7138e751b4
  accessed_at: '2026-11-03T11:20:03.208844Z'
  summary: All current fields, history, definition, relations, examples, functions,
    evidence, graph edges and discussions read. Original target hash remains current.
  support: supports
  snapshot_sha256: 70dbc868044797a3911de45524d13ccbedb5bf9cc671824b0dcade909ab4922f
- evidence_id: micro-prior-copi_coated_vesicle_membrane
  kind: prior_review
  reference: reviews/structured/20261022T005256Z-copi-coated-vesicle-membrane-audit/review.yaml
  locator: Entire immutable original YAML, derived Markdown and native validation/render
  accessed_at: '2026-11-03T11:20:03.208844Z'
  summary: Original qualified scientific pass has no findings/actions. Its expression-only
    adapter exclusion is insufficient under native policy. Historical checks retain
    their actual dates; none is recertified as current.
  support: supports
  snapshot_sha256: 07c380bffaa4ad7419dab5e93152ad58d831f9b6b06b2f46c5a13418689b0571
- evidence_id: micro-original-validation-inputs
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/adversary-microtubule/original-validation-inputs.json
  locator: Three original native validate/render commands and original/source/HEAD
    SHA256 comparisons
  accessed_at: '2026-11-03T11:20:03.208844Z'
  summary: All original pairs validate and render byte-identically. Exactly the whole
    COPI vesicle input is stale; lumen and membrane hashes remain equal.
  support: supports
  snapshot_sha256: 93bcf750ed51bf813e3535d29275a4a7559be89766d38279c74d85d792c38609
- evidence_id: micro-stale-diff
  kind: record_content
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/adversary-microtubule/copi-stale.diff
  locator: Exact original frozen source 9c0446c4c0dd4b458787c43a499e4ceab5e179a6 to
    7081777bba0daacfa48fc6d826cdfd7138e751b4 target diff
  accessed_at: '2026-11-03T11:20:03.208844Z'
  summary: Only one curation-history event and the process-to-ER destination edge
    were added. Current reassessment is substantive; original immutable graph assessment
    covers five edges, current graph six.
  support: supports
  snapshot_sha256: f728512b0068667b96d3e97a9587c70fd2661c013cf14c3511c0e38cbb199d5e
- evidence_id: micro-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030137,GO:0005798,GO:0030135,GO:0030126,GO:0030663,GO:0006890,GO:0035964,GO:0000139,GO:0005783,GO:0060205,GO:0030660,GO:0030662,GO:0106172
  locator: 'All 13 exact returned terms: active status, names, definitions, synonyms
    and relevant is_a/part_of children'
  accessed_at: '2026-11-03T11:17:13.250063Z'
  summary: Exact whole-vesicle/membrane identities and hierarchy remain valid. GO0006890
    explicitly describes directed substances Golgi to ER, including COPI; GO0035964
    defines Golgi evagination. GO0106172 still adds an endocytic qualifier. Coatomer
    is related for whole vesicle and exact for coat; coating parthood is not direct
    lipid constituency.
  support: supports
  snapshot_sha256: 0d9cdaeb3faedf06e166a6e2569ce2011439a8a3d026ef468247aa2f3ed38567
- evidence_id: micro-SL-0321
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0321.json
  locator: Complete exact SL-0321 identity/definition, isA and partOf entries with
    GO mappings
  accessed_at: '2026-11-03T11:17:13.250310Z'
  summary: Defines the general COPI vesicle compartment bounded by its membrane, under
    cytoplasmic-vesicle lumen and part of COPI vesicle. The zero annotated protein
    count is not biological absence. The surrounding structures and the lumen remain
    distinct.
  support: supports
  snapshot_sha256: 28c0259c7431ce1edd0502efbb0f843e90c5f6f86b94cc0e59fe694f3a55a72d
- evidence_id: micro-NCBITaxon-4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Exact taxId/scientificName/rank/lineage
  accessed_at: '2026-11-03T11:17:13.250395Z'
  summary: Current authority identifies Saccharomyces cerevisiae at species rank.
    It does not establish a strain, prevalence or mechanism.
  support: supports
  snapshot_sha256: 38f43dd1593a1d47416228ae385464f30aeb8302c3aadb45b3588d03744bc814
- evidence_id: micro-sandmann2003-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1091%2Fmbc.e02-11-0736
  locator: Exact DOI10.1091/mbc.e02-11-0736, PMID12925749, authors and complete primary
    abstract
  accessed_at: '2026-11-03T11:17:13.250455Z'
  summary: The yeast study reports coatomer-mutant suppression and KKXX-dependent
    binding/vesicle results; actual assays and their limits are assessed from the
    body.
  support: partial
  snapshot_sha256: 5731926327c9dc1caf338e255c6599c1831aa082c9dcaf1a8d5e447c09e6e4f9
- evidence_id: micro-sandmann2003-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC181553/
  locator: 'Fresh genuine PMC HTML: complete abstract and Introduction sec1; Methods
    sec3 including Table1, sec7 Protein-binding Assay, sec14 Budding Assay; complete
    Results sec16 and sec20–23 including captions Figures1,5–7; complete Discussion
    sec25'
  accessed_at: '2026-11-03T11:17:14.014410Z'
  summary: Yeast suppression, binding and vesicle assays support the stated early-secretory
    COPI context. Cytosol-only experiments cannot separate COPI/COPII; purified-coat
    assays can. Cargo packaging and proposed regulatory mechanisms remain qualified.
    Neither lipid flux nor the lumen was separately quantified; no pixels/raw data
    were reanalysed.
  support: supports
  snapshot_sha256: 943ba49049d35d0d2f967e13f48760e4cd3e9ed8b519763517e7036f6ed46c64
- evidence_id: micro-sandmann2003-jats
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC181553/fullTextXML
  locator: Actual HTTP500 XML response only
  accessed_at: '2026-11-03T11:17:14.014516Z'
  summary: XML route was unavailable; independently obtained genuine PMC HTML supplied
    the inspected body. This response provides no scientific support.
  support: context_only
  snapshot_sha256: c0e988d13b45291f20f58bb62d031f551cb72a27e4c006610643e28ffdf5aa9b
- evidence_id: micro-waters1991-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1038%2F349248a0
  locator: Exact DOI10.1038/349248a0, PMID1898986, authors and complete primary abstract
  accessed_at: '2026-11-03T11:17:13.250500Z'
  summary: Purified cytosolic coatomer contains Golgi transport-vesicle coat proteins.
    This supports historical coat-complex naming rather than a yeast-specific experiment,
    universal modern stoichiometry or whole-vesicle synonym.
  support: partial
  snapshot_sha256: 3e43f878d50ac2de9872db7f7d40d491953149c1244b1cd0a4b036b0a8cbd481
- evidence_id: micro-waters1991-publisher
  kind: authority
  reference: https://www.nature.com/articles/349248a0
  locator: HTTP200 body is a Client Challenge page, not article or abstract
  accessed_at: '2026-11-03T11:17:14.050444Z'
  summary: Current publisher response supplies no scientific text. Only the separately
    inspected complete primary abstract is used; no present full-body access claimed.
  support: context_only
  snapshot_sha256: 32ed63159c77e21ee19ca1b9aa3213ccf0218eb59539560b132a8e68ef0e18ea
- evidence_id: micro-go0106172-ols
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FGO_0106172
  locator: Complete exact GO0106172 OLS entry, active status, description, definition
    citation and creation provenance
  accessed_at: '2026-11-03T11:17:14.067466Z'
  summary: OLS independently repeats the endocytic qualifier. This unresolved authority
    wording prevents an unqualified exact mapping of the broader SL-0321/local general
    lumen target.
  support: supports
  snapshot_sha256: 390fe03ff170c659744a42c0de6bc1e051460b0bb4ce84f5e43ba31292b372a0
- evidence_id: micro-lumen-citation-meta
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A29535154%20AND%20SRC%3AMED
  locator: PMID29535154 / DOI10.1242/jcs.209890; complete abstract and bibliographic
    type Review
  accessed_at: '2026-11-03T11:17:13.250537Z'
  summary: 'Arakel and Schwappach2018 is secondary literature: its abstract describes
    COPI lipid/protein sorting and Golgi-to-ER retrieval. Context only; it does not
    resolve the GO endocytic qualifier and no body/poster was read.'
  support: context_only
  snapshot_sha256: fac769117890b29133121efcda29a5ac1aa770e1953843e270b38a712e43777a
- evidence_id: micro-lumen-search
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=COPI-coated%20vesicle%20lumen&limit=100&page=1
  locator: Current QuickGO literal query COPI-coated vesicle lumen; first100 returned
    IDs/names; exact candidate inspected separately
  accessed_at: '2026-11-03T11:17:14.131978Z'
  summary: Same-label GO0106172 is present, but its definition remains narrower/inconsistent.
    No exhaustive absence is asserted.
  support: supports
  snapshot_sha256: e0b593dd4f403329e96d55445bcb2e160a4e22e54ec9e3723cdcd29a33b7501b
  search_scope: QuickGO ontology search on 2026-11-03T11:17:14.131978Z; literal query
    "COPI-coated vesicle lumen", page1, limit100. Inspected returned100 of618 hits;
    no later six pages examined. Positive candidate followed via exact native QuickGO
    and OLS records; not an exact-phrase or exhaustive absence query.
- evidence_id: micro-catalogue
  kind: search
  reference: https://imodulondb.org/api/datasets
  locator: 'Complete official GET /api/datasets response: all returned organism identifiers/names
    and dataset arrays'
  accessed_at: '2026-11-03T11:17:14.100109Z'
  summary: Returned catalogue has no Saccharomyces cerevisiae dataset. No matched
    downstream gene/module query applies; absence is catalogue coverage only. E. coli
    recombinant expression in a source is not the yeast structure taxon.
  support: supports
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  search_scope: Official iModulonDB /api/datasets GET on 2026-11-03T11:17:14.100109Z;
    complete returned array of20 organism rows/28 organism-dataset pairs, no pagination
    shown. Compared all names/IDs against Saccharomyces cerevisiae/Saccharomyces/yeast
    and source-relevant mammalian context. No matched organism/dataset; no unrelated
    bacterial expression-host modules substituted.
- evidence_id: micro-doi-10.1016_j.cell.2012.01.015
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.cell.2012.01.015
  locator: Exact metadata and complete primary abstract; DOI10.1016/j.cell.2012.01.015;
    title A structure-based mechanism for Arf1-dependent recruitment of coatomer to
    membranes.; retained actual 10:50Z snapshot from immediately prior review, hash
    reverified; declared prior sections retained and Introduction reread here
  accessed_at: '2026-11-03T10:50:10.136772Z'
  snapshot_sha256: 720deee8d2fa1906684b6741443d65dbcafb8234d7e28b5fb4945db432ec4fe8
  summary: Complete primary abstract reports Arf1/coatomer structural and biochemical
    recruitment model. Actual mammalian/yeast construct scopes and model limits are
    retained in the separately inspected body. No fresh download or broader Methods/figure
    scope is claimed.
  support: partial
- evidence_id: micro-yu2012-s3
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3285272.1/PMC3285272.1.xml
  locator: DOI10.1016/j.cell.2012.01.015; complete Introduction; Results Experimental
    Approach and A Model for Arf1-Dependent Recruitment of Coatomer to Membranes;
    retained actual 10:50Z snapshot from immediately prior review, hash reverified;
    declared prior sections retained and Introduction reread here
  accessed_at: '2026-11-03T10:50:10.213884Z'
  snapshot_sha256: a7adecb3e84137dcc05565185633b97cd4c07fc8e2556c98e9922152c7d34ea6
  summary: Genuine primary JATS. Mammalian coatomer subcomplexes with defined human/yeast
    truncated Arf1 constructs support a bounded recruitment model. COPI, COPII and
    clathrin/AP systems are distinguished; proposed conformational effects remain
    proposals. Not direct accession-specific evidence for every yeast coat example,
    nor complete Methods/raw-data audit. No fresh download or broader Methods/figure
    scope is claimed.
  support: supports
- evidence_id: micro-historical-adapter-runner
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Retained actual 00:49Z invocation receipt; no current runner execution
  accessed_at: '2026-11-03T00:49:00.863225Z'
  summary: Historical adapter invocation failed with PermissionError accessing pyvenv.cfg.
    Native policy permits inspected-source fallback; current catalogue evidence is
    separate. This is not a new failure or successful runner execution.
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: micro-native-copi_coated_vesicle-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/copi_coated_vesicle-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/copi_coated_vesicle.yaml
    --verify; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/copi_coated_vesicle-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T11:16:59.992031Z'
  summary: Actual exit0 at current source, 2026-11-03T11:16:59.603974+00:00 to 2026-11-03T11:16:59.992031+00:00.
    Empty protein-example inventory and zero GENE_OR_PROTEIN nodes. This does not
    verify narrative proteins, source taxon, pathway mechanism or formation necessity.
  support: supports
  snapshot_sha256: 8964b075ee23ae14104768c30cb3de01b8160fc41d1a1e51e760c2ef2a4de0e6
- evidence_id: micro-native-copi_coated_vesicle-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/copi_coated_vesicle-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/copi_coated_vesicle.yaml
    --causal-graphs; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/copi_coated_vesicle-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-03T11:17:00.429865Z'
  summary: Actual exit0 at current source, 2026-11-03T11:17:00.026285+00:00 to 2026-11-03T11:17:00.429865+00:00.
    Empty protein-example inventory and zero GENE_OR_PROTEIN nodes. This does not
    verify narrative proteins, source taxon, pathway mechanism or formation necessity.
  support: supports
  snapshot_sha256: 5d1b039b822041679f6b3550a0de119072ca3597fb18fc5163da96266b9e7a33
- evidence_id: micro-native-copi_coated_vesicle_lumen-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/copi_coated_vesicle_lumen-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/copi_coated_vesicle_lumen.yaml
    --verify; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/copi_coated_vesicle_lumen-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T11:17:00.846573Z'
  summary: Actual exit0 at current source, 2026-11-03T11:17:00.462678+00:00 to 2026-11-03T11:17:00.846573+00:00.
    Empty protein-example inventory and zero GENE_OR_PROTEIN nodes. This does not
    verify narrative proteins, source taxon, pathway mechanism or formation necessity.
  support: supports
  snapshot_sha256: 99ed515def9db1d45a6e67a79fc5c16460200824c21df53cdfeb38221eef6680
- evidence_id: micro-native-copi_coated_vesicle_lumen-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/copi_coated_vesicle_lumen-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/copi_coated_vesicle_lumen.yaml
    --causal-graphs; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/copi_coated_vesicle_lumen-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-03T11:17:01.260228Z'
  summary: Actual exit0 at current source, 2026-11-03T11:17:00.878680+00:00 to 2026-11-03T11:17:01.260228+00:00.
    Empty protein-example inventory and zero GENE_OR_PROTEIN nodes. This does not
    verify narrative proteins, source taxon, pathway mechanism or formation necessity.
  support: supports
  snapshot_sha256: fc9533267f78a7d5863f03c8cd8709869c1f927d41c0a396fba4ae55af916df4
- evidence_id: micro-native-copi_coated_vesicle_membrane-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/copi_coated_vesicle_membrane-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/copi_coated_vesicle_membrane.yaml
    --verify; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/copi_coated_vesicle_membrane-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T11:17:01.675302Z'
  summary: Actual exit0 at current source, 2026-11-03T11:17:01.291893+00:00 to 2026-11-03T11:17:01.675302+00:00.
    Empty protein-example inventory and zero GENE_OR_PROTEIN nodes. This does not
    verify narrative proteins, source taxon, pathway mechanism or formation necessity.
  support: supports
  snapshot_sha256: 913e25d17cfe2ab59007e7e4a7878073e417a827f7e7ee07fcca1e233c27841c
- evidence_id: micro-native-copi_coated_vesicle_membrane-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/copi_coated_vesicle_membrane-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/copi_coated_vesicle_membrane.yaml
    --causal-graphs; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/copi_coated_vesicle_membrane-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-03T11:17:02.086997Z'
  summary: Actual exit0 at current source, 2026-11-03T11:17:01.708657+00:00 to 2026-11-03T11:17:02.086997+00:00.
    Empty protein-example inventory and zero GENE_OR_PROTEIN nodes. This does not
    verify narrative proteins, source taxon, pathway mechanism or formation necessity.
  support: supports
  snapshot_sha256: 336f5a3624fba78fe97672b0bc544835e1aba5977f7bb4a82c6a2bebe43514c0
- evidence_id: septin-review-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Structured Source Cross-Checks and immutable review workflow
  summary: Actual molecular and osmoregulatory pathway/response assertions merit applicability
    assessment; absence of expression claims is not an exemption. Missing organism
    coverage is not negative biology.
  accessed_at: '2026-11-03T11:21:49.751322Z'
  support: supports
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: septin-curation-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Structure identity, protein examples, constituent evidence, source scope
  summary: Protein identity does not establish constituent localization or necessity.
    Substructure, material, functional protein class and complete organelle are distinct.
  accessed_at: '2026-11-03T11:21:49.751322Z'
  support: supports
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
- evidence_id: septin-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: NONMECHANISTIC topology, evidence, protein anchoring and process endpoints
  summary: Protein nodes and typed anatomical nodes must retain their source scope;
    a NONMECHANISTIC label does not turn a model or speculative mechanism into direct
    experimental proof.
  accessed_at: '2026-11-03T11:21:49.751322Z'
  support: supports
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: septin-record-contractile_vacuolar_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/contractile_vacuolar_membrane.yaml
  locator: Entire current maintained record at 7081777bba0daacfa48fc6d826cdfd7138e751b4
  summary: Full identity, history, synonymy, definition, component/gene/protein examples,
    taxon examples, function, every graph edge, evidence and discussions read. No
    attached image, numerical physical property or verbatim snippet is declared.
  accessed_at: '2026-11-03T11:21:49.751322Z'
  support: supports
  snapshot_sha256: a73ad7ccfc67c7c39a41d555109a229de1c469dec8eff0d808a3cddaa0aa383c
- evidence_id: septin-original-contractile_vacuolar_membrane
  kind: prior_review
  reference: reviews/structured/20261022T005251Z-contractile-vacuolar-membrane-audit/review.yaml
  locator: Entire original YAML/Markdown observation; source hashes, checks, evidence
    tiers, assessments, findings/actions and limitations
  summary: Historical record bytes remain current. Whole vacuole has F1 major and
    F2/F3 minor open findings; membrane and complex have no scientific findings. No
    historical source access or gate is reclassified as current execution.
  accessed_at: '2026-11-03T11:21:49.751322Z'
  support: supports
  snapshot_sha256: 0277dc12a05fdf291f94a1fc983a973c151af82e33f3a6375bea7e4900406ad8
- evidence_id: septin-original-validation-contractile_vacuolar_membrane
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/adversary-septin/original-checks.json
  locator: 20261022T005251Z-contractile-vacuolar-membrane-audit native validate/render
    and source/current frozen-hash comparison
  summary: Both original commands exit0 and rendered Markdown is byte-identical. Historical
    source bytes equal original frozen/current target hashes.
  accessed_at: '2026-11-03T11:17:07.641139Z'
  support: supports
  snapshot_sha256: 98a5fe5b84e5e4cb80e16ad197b9871a60c4eb179a1c987a5ca613ba6eb5506c
- evidence_id: septin-native-contractile_vacuolar_membrane-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/contractile_vacuolar_membrane-uniprot-verify-receipt.json
  locator: Actual root command receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/contractile_vacuolar_membrane-uniprot-verify.log
  summary: Exit0. No protein examples or UniProtKB protein xrefs. The two protein
    nodes comprise one NO_GENE_SYMBOLS aquaporin component and one UNANCHORED_NO_UNIPROT
    perivacuolar V-ATPase context node. Exit0 does not verify species-specific identity,
    localization or necessity.
  accessed_at: '2026-11-03T11:16:55.045477Z'
  support: supports
  snapshot_sha256: 274f2e3e9e9bd937fd7452511d53eee1b10af80cd721370c924f1e3aac925b7d
- evidence_id: septin-native-contractile_vacuolar_membrane-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/contractile_vacuolar_membrane-uniprot-causal-receipt.json
  locator: Actual root command receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/contractile_vacuolar_membrane-uniprot-causal.log
  summary: Exit0. No protein examples or UniProtKB protein xrefs. The two protein
    nodes comprise one NO_GENE_SYMBOLS aquaporin component and one UNANCHORED_NO_UNIPROT
    perivacuolar V-ATPase context node. Exit0 does not verify species-specific identity,
    localization or necessity.
  accessed_at: '2026-11-03T11:16:55.415538Z'
  support: supports
  snapshot_sha256: a3d48d6cd791ac2b571f250ef3051553fb995bfc328059fc2d31f057260848ec
- evidence_id: septin-record-contractile_vacuole
  kind: record_content
  reference: data/structures/membrane_organelle/contractile_vacuole.yaml
  locator: Entire current maintained record at 7081777bba0daacfa48fc6d826cdfd7138e751b4
  summary: Full identity, history, synonymy, definition, component/gene/protein examples,
    taxon examples, function, every graph edge, evidence and discussions read. No
    attached image, numerical physical property or verbatim snippet is declared.
  accessed_at: '2026-11-03T11:21:49.751322Z'
  support: supports
  snapshot_sha256: d1057e9c19ff100f054c73da52b597742dadde491f2a007cd7b648b8a7b626bb
- evidence_id: septin-original-contractile_vacuole
  kind: prior_review
  reference: reviews/structured/20261022T005252Z-contractile-vacuole-audit/review.yaml
  locator: Entire original YAML/Markdown observation; source hashes, checks, evidence
    tiers, assessments, findings/actions and limitations
  summary: Historical record bytes remain current. Whole vacuole has F1 major and
    F2/F3 minor open findings; membrane and complex have no scientific findings. No
    historical source access or gate is reclassified as current execution.
  accessed_at: '2026-11-03T11:21:49.751322Z'
  support: supports
  snapshot_sha256: a49af232ae1b9a295c0885c7b34b7598c296a7a58c97f574f5060dc5dbd7d274
- evidence_id: septin-original-validation-contractile_vacuole
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/adversary-septin/original-checks.json
  locator: 20261022T005252Z-contractile-vacuole-audit native validate/render and source/current
    frozen-hash comparison
  summary: Both original commands exit0 and rendered Markdown is byte-identical. Historical
    source bytes equal original frozen/current target hashes.
  accessed_at: '2026-11-03T11:17:08.852872Z'
  support: supports
  snapshot_sha256: 98a5fe5b84e5e4cb80e16ad197b9871a60c4eb179a1c987a5ca613ba6eb5506c
- evidence_id: septin-native-contractile_vacuole-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/contractile_vacuole-uniprot-verify-receipt.json
  locator: Actual root command receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/contractile_vacuole-uniprot-verify.log
  summary: Exit0. Six protein examples verify. The V-ATPase node is COVERED by four
    examples; the aquaporin node is PARTIAL_EXAMPLES with MIP1 missing. This is inventory/identity
    coverage, not proof that aqpA/aqpB reside in a CV or that MIP1 lacks a biological
    counterpart.
  accessed_at: '2026-11-03T11:16:56.739012Z'
  support: supports
  snapshot_sha256: 75f99c7b0f294ed0c316594595c911ed50ff63b9853e8213e66d8e945af1b66d
- evidence_id: septin-native-contractile_vacuole-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/contractile_vacuole-uniprot-causal-receipt.json
  locator: Actual root command receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/contractile_vacuole-uniprot-causal.log
  summary: Exit0. Six protein examples verify. The V-ATPase node is COVERED by four
    examples; the aquaporin node is PARTIAL_EXAMPLES with MIP1 missing. This is inventory/identity
    coverage, not proof that aqpA/aqpB reside in a CV or that MIP1 lacks a biological
    counterpart.
  accessed_at: '2026-11-03T11:16:57.139263Z'
  support: supports
  snapshot_sha256: 64f41eb30d3d03ab9065adb626a61d6d54c796adf916b60e1e6b1047f4edf732
- evidence_id: septin-record-contractile_vacuole_complex
  kind: record_content
  reference: data/structures/membrane_organelle/contractile_vacuole_complex.yaml
  locator: Entire current maintained record at 7081777bba0daacfa48fc6d826cdfd7138e751b4
  summary: Full identity, history, synonymy, definition, component/gene/protein examples,
    taxon examples, function, every graph edge, evidence and discussions read. No
    attached image, numerical physical property or verbatim snippet is declared.
  accessed_at: '2026-11-03T11:21:49.751322Z'
  support: supports
  snapshot_sha256: 5d37be1aa899c1bfd20611faeafefb842a96e8a21144dea9e010b2c89d4b7a1c
- evidence_id: septin-original-contractile_vacuole_complex
  kind: prior_review
  reference: reviews/structured/20261022T005253Z-contractile-vacuole-complex-audit/review.yaml
  locator: Entire original YAML/Markdown observation; source hashes, checks, evidence
    tiers, assessments, findings/actions and limitations
  summary: Historical record bytes remain current. Whole vacuole has F1 major and
    F2/F3 minor open findings; membrane and complex have no scientific findings. No
    historical source access or gate is reclassified as current execution.
  accessed_at: '2026-11-03T11:21:49.751322Z'
  support: supports
  snapshot_sha256: 014d1929ae5fa35fbf1e8bde740d1b27fccb3f5eb0088e93434a8e6be43baac2
- evidence_id: septin-original-validation-contractile_vacuole_complex
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/adversary-septin/original-checks.json
  locator: 20261022T005253Z-contractile-vacuole-complex-audit native validate/render
    and source/current frozen-hash comparison
  summary: Both original commands exit0 and rendered Markdown is byte-identical. Historical
    source bytes equal original frozen/current target hashes.
  accessed_at: '2026-11-03T11:17:09.987048Z'
  support: supports
  snapshot_sha256: 98a5fe5b84e5e4cb80e16ad197b9871a60c4eb179a1c987a5ca613ba6eb5506c
- evidence_id: septin-native-contractile_vacuole_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/contractile_vacuole_complex-uniprot-verify-receipt.json
  locator: Actual root command receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/contractile_vacuole_complex-uniprot-verify.log
  summary: Exit0. Empty protein example/xref inventory and zero GENE_OR_PROTEIN nodes.
    Exit0 does not independently validate the molecular details intentionally assigned
    to child records or the osmoregulatory pathway.
  accessed_at: '2026-11-03T11:16:57.530152Z'
  support: supports
  snapshot_sha256: 269d722affaa79d9a788871cd3ec0246f7eb360b3c1786195a1d06e1aa858c42
- evidence_id: septin-native-contractile_vacuole_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/contractile_vacuole_complex-uniprot-causal-receipt.json
  locator: Actual root command receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/contractile_vacuole_complex-uniprot-causal.log
  summary: Exit0. Empty protein example/xref inventory and zero GENE_OR_PROTEIN nodes.
    Exit0 does not independently validate the molecular details intentionally assigned
    to child records or the osmoregulatory pathway.
  accessed_at: '2026-11-03T11:16:57.947746Z'
  support: supports
  snapshot_sha256: 73f1dffc26614acdf3e5884b4bd2e71f962822324e0fadb269af84f0b3aa7a50
- evidence_id: septin-context-spongiome
  kind: record_content
  reference: data/structures/membrane_organelle/spongiome.yaml
  locator: Only identity, definition, structure_kind, parent_structures, part_of and
    has_part
  summary: Frozen before inspection; boundary context only. No independent whole-neighbor
    review, molecular accession verification or terminal disposition of its findings
    is asserted.
  accessed_at: '2026-11-03T11:21:49.751322Z'
  support: supports
  snapshot_sha256: 4bdc11a86d247b6a45549a41c9aac3b25946b046f3b54d269fab634ca9d44019
- evidence_id: septin-context-contractile_vacuole_lumen
  kind: record_content
  reference: data/structures/membrane_organelle/contractile_vacuole_lumen.yaml
  locator: Only identity, definition, structure_kind, parent_structures, part_of and
    has_part
  summary: Frozen before inspection; boundary context only. No independent whole-neighbor
    review, molecular accession verification or terminal disposition of its findings
    is asserted.
  accessed_at: '2026-11-03T11:21:49.751322Z'
  support: supports
  snapshot_sha256: 9c85ec352245d16e963b9d86d4d1cf0b41d499b956b0b2d05611dca3a4341622
- evidence_id: septin-context-contractile_vacuole_pore
  kind: record_content
  reference: data/structures/membrane_organelle/contractile_vacuole_pore.yaml
  locator: Only identity, definition, structure_kind, parent_structures, part_of and
    has_part
  summary: Frozen before inspection; boundary context only. No independent whole-neighbor
    review, molecular accession verification or terminal disposition of its findings
    is asserted.
  accessed_at: '2026-11-03T11:21:49.751322Z'
  support: supports
  snapshot_sha256: e6b016675a36c215388bfd9053da4af4b1ec407c47c197f8a2217f9ba66cc294
- evidence_id: septin-contractile-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031164,GO:0005774,GO:0000331,GO:0062159,GO:0062160,GO:0043232,GO:0005775,GO:0031913,GO:0098797,GO:0005856
  locator: 'All ten returned exact terms: active identities, definitions, synonyms
    and relevant typed child relations; unrelated child branches not used'
  summary: Membrane GO0031164, vacuole GO0000331, whole complex GO0062159 and spongiome
    GO0062160 are distinct. Membrane is a vacuolar-membrane subtype and vacuole part;
    whole vacuole and spongiome are complex parts. GO calls central bladder related,
    not exact; CVC is also related for the complex. Complex definition and GO0043232
    parent are non-membrane-bounded at composite-system scope.
  accessed_at: '2026-11-03T11:16:55.831372Z'
  support: supports
  snapshot_sha256: 3001e9aa0de9d2828e1a1a727af2c84d192398885fe3080a1f75b13f34bad99a
- evidence_id: septin-contractile-agent-ancestors-0031164
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031164/ancestors?relations=is_a,part_of
  locator: Complete requested is_a/part_of ancestor closure for exact target
  summary: Corroborates native hierarchy; ancestor closure is not a direct molecular
    mechanism or every individual immediate parent relation.
  accessed_at: '2026-11-03T11:16:55.831917Z'
  support: supports
  snapshot_sha256: f22b8952534967bd65c4f69eddbf38b736d8d0d95040c36eef0d9904faa3fd05
- evidence_id: septin-contractile-agent-ancestors-0000331
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000331/ancestors?relations=is_a,part_of
  locator: Complete requested is_a/part_of ancestor closure for exact target
  summary: Corroborates native hierarchy; ancestor closure is not a direct molecular
    mechanism or every individual immediate parent relation.
  accessed_at: '2026-11-03T11:16:57.392252Z'
  support: supports
  snapshot_sha256: a8bc7dcb4eefe50c5b9efcc30d1234894cffffb457fa5b6be34527920b84bec6
- evidence_id: septin-contractile-agent-ancestors-0062159
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0062159/ancestors?relations=is_a,part_of
  locator: Complete requested is_a/part_of ancestor closure for exact target
  summary: Corroborates native hierarchy; ancestor closure is not a direct molecular
    mechanism or every individual immediate parent relation.
  accessed_at: '2026-11-03T11:17:03.044042Z'
  support: supports
  snapshot_sha256: 514c75dccbc6096ad72c1c6fc2465500b2f0984d83e0cbf436287dd88f890191
- evidence_id: septin-contractile-agent-go-vacuole-parent
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005773
  locator: Exact GO0005773 definition and relevant direct child GO0000331
  summary: GO confirms contractile vacuole as a vacuole subtype. Omission of this
    optional explicit maintained parent does not change the exact GO identity or by
    itself establish a concrete review defect.
  accessed_at: '2026-11-03T11:16:57.389001Z'
  support: supports
  snapshot_sha256: 38c7ec1de8258690b42a7da3161b0b9b1b8c92130fd28255c8c861785c402ec1
- evidence_id: septin-contractile-agent-go-vatpase
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0016471
  locator: Exact GO0016471 active identity, definition and V1/V0 parts
  summary: Native term denotes the broad vacuolar proton-transporting V-type ATPase
    complex. It is a source-neutral candidate class, not direct proof of CV membership
    or exact cross-lineage CV-localized subset identity.
  accessed_at: '2026-11-03T11:17:03.013833Z'
  support: supports
  snapshot_sha256: 43c760bfd14f3b2e02fca6b1cebe4547576402f89282fb18da04bc8e2c5d2f36
- evidence_id: septin-contractile-agent-SL-0073
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0073.json
  locator: Native id/name/definition, synonyms, exact GO mapping and immediate isA/partOf
  summary: SL0073 maps to GO0000331 and includes CV among its synonyms. Its prose
    also describes the whole CVC apparatus; that broader prose is not substituted
    for the precise GO0000331 bladder/GO0062159 complex distinction.
  accessed_at: '2026-11-03T11:16:57.152935Z'
  support: supports
  snapshot_sha256: bf50970299f0daf4a713091ca09dc75c5bfa17bbd69397afeac2da5420d8920e
- evidence_id: septin-contractile-agent-SL-0074
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0074.json
  locator: Native id/name/definition, synonyms, exact GO mapping and immediate isA/partOf
  summary: SL0074 maps exactly to GO0031164 with contractile vacuolar membrane synonym,
    vacuole-membrane parent and contractile-vacuole partOf. Its introductory complex
    wording is not used to merge anatomical levels.
  accessed_at: '2026-11-03T11:16:55.831840Z'
  support: supports
  snapshot_sha256: e5b4dd1762995584fbaef9f6cb52e7e5b03172867ffe1871434c9be645b6d4c7
- evidence_id: septin-contractile-agent-tax-2759
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759
  locator: Complete taxId, scientificName, rank and lineage
  summary: Native taxon2759 is Eukaryota (domain). This is identity verification,
    not experiment-specific strain or prevalence evidence.
  accessed_at: '2026-11-03T11:16:55.831775Z'
  support: supports
  snapshot_sha256: 61a68c76c70762c97e0b218568ab037d9a30c0207847247e9e055b5764a61634
- evidence_id: septin-contractile-agent-tax-5775
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5775
  locator: Complete taxId, scientificName, rank and lineage
  summary: Native taxon5775 is Amoeba proteus (species). This is identity verification,
    not experiment-specific strain or prevalence evidence.
  accessed_at: '2026-11-03T11:16:56.756007Z'
  support: supports
  snapshot_sha256: b91863cf93b4016b0e73391853e987c931012811589adac9c125bcd288c2c8ef
- evidence_id: septin-contractile-agent-tax-44689
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/44689
  locator: Complete taxId, scientificName, rank and lineage
  summary: Native taxon44689 is Dictyostelium discoideum (species). This is identity
    verification, not experiment-specific strain or prevalence evidence.
  accessed_at: '2026-11-03T11:16:58.311398Z'
  support: supports
  snapshot_sha256: f7bfea542a721125d862d08a5f8dd0986c1c19034b45f1fb92adf8c8d045efca
- evidence_id: septin-contractile-agent-tax-3055
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3055
  locator: Complete taxId, scientificName, rank and lineage
  summary: Native taxon3055 is Chlamydomonas reinhardtii (species). This is identity
    verification, not experiment-specific strain or prevalence evidence.
  accessed_at: '2026-11-03T11:16:58.508907Z'
  support: supports
  snapshot_sha256: a24c8f85014097148d9e865ea324b01b8d04f6bae27e893834f8abb5bd8b6a1f
- evidence_id: septin-contractile-agent-tax-5693
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5693
  locator: Complete taxId, scientificName, rank and lineage
  summary: Native taxon5693 is Trypanosoma cruzi (species). This is identity verification,
    not experiment-specific strain or prevalence evidence.
  accessed_at: '2026-11-03T11:16:58.575307Z'
  support: supports
  snapshot_sha256: d85474c78d866ba5b5b5b7f67fdec1433f8ca89addf1c52013fa2308d5919294
- evidence_id: septin-contractile-agent-tax-44030
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/44030
  locator: Complete taxId, scientificName, rank and lineage
  summary: Native taxon44030 is Paramecium multimicronucleatum (species). This is
    identity verification, not experiment-specific strain or prevalence evidence.
  accessed_at: '2026-11-03T11:17:03.988574Z'
  support: supports
  snapshot_sha256: 4be4e352120325ebd0564f246f7c6af841f2f1a81fbf3b2f6db5c11d7c0393d7
- evidence_id: septin-contractile-agent-more2024-meta
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016%2Fj.ejop.2024.126078
  locator: 'Europe PMC exact cited DOI or PMID/title result: complete abstract plus
    title/authors/identifiers/journal/date'
  summary: Secondary review abstract describes patchy eukaryotic occurrence and variable
    CV structure/function/machinery. No numerical all-Eukaryota frequency or specific
    aqpA/aqpB localization is established by this abstract.
  accessed_at: '2026-11-03T11:16:55.831678Z'
  support: supports
  snapshot_sha256: 46fafe4ca983c67438501002db300546d269a9ff60db3c0d5987d25f94cfd119
  search_scope: Europe PMC REST query exactly as encoded in reference; format=json
    and resultType=core, one returned response page, no date filter. Only the matched
    cited article inspected at 2026-11-03T11:16:55.831678Z. No broad literature-absence
    claim.
- evidence_id: septin-contractile-agent-nishihara2008-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1042%2FBC20070091
  locator: 'Europe PMC exact cited DOI or PMID/title result: complete abstract plus
    title/authors/identifiers/journal/date'
  summary: Complete primary abstract identifies Amoeba ApAQP, oocyte water-channel
    function and immunolocalization to CV membrane/perivacuolar vesicles. V-ATPase
    is detected on surrounding vesicle membranes; osmotic-gradient generation is an
    interpretation/hypothesis, not direct localization of all pumps to the single
    CV bilayer.
  accessed_at: '2026-11-03T11:16:56.444070Z'
  support: supports
  snapshot_sha256: 09e903af86ac0a60d82022d68eaa03ba192bcb689f6917dd21167f61c363095b
  search_scope: Europe PMC REST query exactly as encoded in reference; format=json
    and resultType=core, one returned response page, no date filter. Only the matched
    cited article inspected at 2026-11-03T11:16:56.444070Z. No broad literature-absence
    claim.
- evidence_id: septin-contractile-agent-clarke2002-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1242%2Fjcs.115.14.2893
  locator: 'Europe PMC exact cited DOI or PMID/title result: complete abstract plus
    title/authors/identifiers/journal/date'
  summary: Complete primary abstract identifies Dictyostelium VatM-GFP targeting and
    assembly-competent V-ATPase at CV and endolysosomal membranes, with distinct vesiculotubular/endosomal
    dynamics. This does not establish uniform density of every subunit in every bladder
    or require a complete systole force model.
  accessed_at: '2026-11-03T11:16:56.751569Z'
  support: supports
  snapshot_sha256: 2a37a596e7f4e7c579dffee743c4f268011dc6eec63559b0f9ff9072e24c677e
  search_scope: Europe PMC REST query exactly as encoded in reference; format=json
    and resultType=core, one returned response page, no date filter. Only the matched
    cited article inspected at 2026-11-03T11:16:56.751569Z. No broad literature-absence
    claim.
- evidence_id: septin-contractile-agent-rohloff2004-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1074%2Fjbc.M410372200
  locator: 'Europe PMC exact cited DOI or PMID/title result: complete abstract plus
    title/authors/identifiers/journal/date'
  summary: Complete primary abstract supports T. cruzi acidocalcisome/CVC involvement
    in hypo-osmotic volume recovery, aquaporin translocation and isolated bladder
    proton transport. This is not proof of identical response machinery in every protist.
  accessed_at: '2026-11-03T11:16:57.455128Z'
  support: supports
  snapshot_sha256: a2d84b841737fa7e9a58a86e7276b2c22a522934808df2a750ec556219141861
  search_scope: Europe PMC REST query exactly as encoded in reference; format=json
    and resultType=core, one returned response page, no date filter. Only the matched
    cited article inspected at 2026-11-03T11:16:57.455128Z. No broad literature-absence
    claim.
- evidence_id: septin-contractile-agent-allen2002-title
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=TITLE%3A%22Osmoregulation%20and%20contractile%20vacuoles%20of%20protozoa%22
  locator: 'Europe PMC exact cited DOI or PMID/title result: complete abstract plus
    title/authors/identifiers/journal/date'
  summary: Secondary review abstract explicitly distinguishes pump-rich vesiculotubular
    membrane from a reservoir membrane lacking V-ATPase holoenzymes, and describes
    filling/rounding/discharge. Broad cycle support is not an assay of individual
    channel membership or a universally settled contraction mechanism.
  accessed_at: '2026-11-03T11:16:57.467646Z'
  support: supports
  snapshot_sha256: ea88a1f4d0631757324caecc2046764fa6193a4578dde07f8f2f20b0c3f4ee39
  search_scope: Europe PMC REST query exactly as encoded in reference; format=json
    and resultType=core, one returned response page, no date filter. Only the matched
    cited article inspected at 2026-11-03T11:16:57.467646Z. No broad literature-absence
    claim.
- evidence_id: septin-contractile-agent-bulow2012-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A22262860%20AND%20SRC%3AMED
  locator: 'Europe PMC exact cited DOI or PMID/title result: complete abstract plus
    title/authors/identifiers/journal/date'
  summary: Complete primary abstract distinguishes wild-type AqpB with no detected
    water/glycerol/urea conductance in tested oocytes from the active loop-deletion
    mutant. GFP constructs label unspecified vacuoles, plasma membrane and protrusions;
    osmoregulatory relevance is tentative.
  accessed_at: '2026-11-03T11:16:58.114249Z'
  support: supports
  snapshot_sha256: 9105d20a4d18414f53cc30551ac108682ed15473c07a8848864807ac00a7c0e1
  search_scope: Europe PMC REST query exactly as encoded in reference; format=json
    and resultType=core, one returned response page, no date filter. Only the matched
    cited article inspected at 2026-11-03T11:16:58.114249Z. No broad literature-absence
    claim.
- evidence_id: septin-contractile-agent-aqpA2000-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A10876090%20AND%20SRC%3AMED
  locator: 'Europe PMC exact cited DOI or PMID/title result: complete abstract plus
    title/authors/identifiers/journal/date'
  summary: Mitra et al.2000 complete primary abstract describes developmentally regulated
    aqpA, prespore expression and loss of prolonged spore viability/dormancy. It does
    not experimentally locate AqpA to contractile vacuoles.
  accessed_at: '2026-11-03T11:16:58.151569Z'
  support: supports
  snapshot_sha256: e667546898fad53f13a9f73d86674f213995da2e732a72307795cb59bd27d63b
  search_scope: Europe PMC REST query exactly as encoded in reference; format=json
    and resultType=core, one returned response page, no date filter. Only the matched
    cited article inspected at 2026-11-03T11:16:58.151569Z. No broad literature-absence
    claim.
- evidence_id: septin-contractile-agent-nolta1994-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A8294479%20AND%20SRC%3AMED
  locator: 'Europe PMC exact cited DOI or PMID/title result: complete abstract plus
    title/authors/identifiers/journal/date'
  summary: Complete primary abstract describes purified Dictyostelium bladder and
    spongiome membranes, pump-rich spongiome and pump-poor bladders, with possible
    primary energy-transduction role. This supports bipartite complex scope; pump-poor
    does not mean complete absence.
  accessed_at: '2026-11-03T11:17:03.608052Z'
  support: supports
  snapshot_sha256: d29beee964bad19b97cb72a6acb0084f79ae625b8c3bd042920b60002bd868a9
  search_scope: Europe PMC REST query exactly as encoded in reference; format=json
    and resultType=core, one returned response page, no date filter. Only the matched
    cited article inspected at 2026-11-03T11:17:03.608052Z. No broad literature-absence
    claim.
- evidence_id: septin-contractile-agent-gronlien2002-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1242%2Fjeb.205.20.3261
  locator: 'Europe PMC exact cited DOI or PMID/title result: complete abstract plus
    title/authors/identifiers/journal/date'
  summary: Complete primary abstract reports Paramecium multimicronucleatum microelectrode
    potentials, osmotic adaptation, decorated radial-arm V-ATPase labeling and concanamycin
    effects. It supports electrogenic spongiome/fluid segregation in that ciliate;
    functional inhibition is not an organelle-formation knockout.
  accessed_at: '2026-11-03T11:17:03.654464Z'
  support: supports
  snapshot_sha256: ab401a043a983f8df0b7e1d4febcc3a466046facdaf6c68035ffad0dc0993bfd
  search_scope: Europe PMC REST query exactly as encoded in reference; format=json
    and resultType=core, one returned response page, no date filter. Only the matched
    cited article inspected at 2026-11-03T11:17:03.654464Z. No broad literature-absence
    claim.
- evidence_id: septin-contractile-agent-komsic2014-pmc-numeric
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/4248701/
  locator: 'Genuine current PMC4248701 HTML: Abstract; Methods Strains used; Results
    Osmoregulation in CC3395, Regulation of CV activity, Water uptake into CV, Aquaporins
    in Chlamydomonas and MIP1 localization; Discussion Aquaporins and CV function;
    associated Table1 and captions as text'
  summary: Direct Results distinguish CV size/cell-size relation from contraction-interval/medium-osmolarity
    relation; cell and CV size were not correlated with medium osmotic strength. CC3395/UVM4-derived
    reporter strains and adaptation conditions are explicit. MIP1 immunogold/GFP localization
    supports CV association; lumen osmolarity and permeability are modeled, not directly
    measured, and GFP fusion functionality is questioned. These primary data do not
    establish Dictyostelium aqpA/aqpB membership or wild-type MIP1 water conductance
    by a separate direct assay.
  accessed_at: '2026-11-03T11:16:57.763169Z'
  support: supports
  snapshot_sha256: dd945cffbbbc689e28c5a0a7e4ca794d3427a5973a43702dd796d65513506da4
- evidence_id: septin-contractile-agent-bulow2012-pmc-numeric
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/3293572/
  locator: 'Genuine current PMC3293572 HTML: complete Abstract, Results and Discussion,
    including Figures2–4 captions as text; no full Experimental Procedures or pixels
    claimed'
  summary: AqpB was cloned from D.discoideum AX2 amoebae. Tested wild-type/tagged
    or untagged variants did not conduct water above controls in oocytes; Δ208–219
    did in oocytes and proteoliposomes. Anti-AqpB antiserum was unsuitable for immunolocalization,
    so N/C-terminal GFP constructs were used. Results call observed structures vacuolar,
    not identified CVs; Discussion explicitly suggests a CV-like function by analogy.
    This supports the bounded inherited membership finding, not biological absence.
  accessed_at: '2026-11-03T11:16:57.998289Z'
  support: supports
  snapshot_sha256: a874a379e6f94e1586ddfac9fac8b25c896a799aca9cfef644ca133a7b47e13e
- evidence_id: septin-contractile-agent-docampo2013-s3
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3818246.1/PMC3818246.1.xml
  locator: 'Genuine current JATS PMC3818246: sections3.3 History (source label),3.2
    Structure and composition,3.4 Role in osmoregulation only; no image pixels or
    cited-primary-paper audit'
  summary: Secondary synthesis distinguishes central bladder and surrounding spongiome,
    compiles lineage-specific pumps/channels and describes uncertain/alternative osmolyte
    and contraction models. Anatomical organization and general water-expulsion context
    are supported; the synthesis is not direct evidence for all named proteins or
    every proposed mechanistic step.
  accessed_at: '2026-11-03T11:16:57.984983Z'
  support: supports
  snapshot_sha256: 86c6b8220f007a31f585e81365fafb50db47b5610b3cc968f244acdd164d3741
- evidence_id: septin-contractile-agent-aquaporin-family
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000425/
  locator: Exact accession/name/type, complete non-LLM description and family hierarchy;
    description llm flags false
  summary: IPR000425 Major intrinsic protein is a diverse family including aquaporins
    and glycerol facilitators; it is broader than a CV-localized functional subset.
  accessed_at: '2026-11-03T11:16:56.765714Z'
  support: supports
  snapshot_sha256: ac574678948d33658edc435fb00f2d7419ea7dc2139f55433760ca9a82beb6bc
- evidence_id: septin-contractile-agent-aquaporin-transporter
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR034294/
  locator: Exact accession/name/type, complete non-LLM description and family hierarchy;
    description llm flags false
  summary: IPR034294 Aquaporin transporter represents orthodox aquaporins, not every
    algal/protist MIP subgroup or the CV-localized subset. A generic family match
    is not structure-localization evidence.
  accessed_at: '2026-11-03T11:16:56.792446Z'
  support: supports
  snapshot_sha256: 8fba533b27cdd65a82e92543d49f6daac0ac43385922a92b1c580d323109a76b
- evidence_id: septin-contractile-agent-UniProtKB-P54647
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P54647.json
  locator: Exact reviewed accession, gene tokens, protein name, organism, functional/subcellular
    comments and evidence codes
  summary: Current reviewed P54647 identifies vatA in Dictyostelium taxon44689. Pump
    subunit identity/complex role is verified; location comments and evidence codes
    are distinguished from a direct assay of each subunit in every CV subcompartment.
  accessed_at: '2026-11-03T11:16:58.730136Z'
  support: supports
  snapshot_sha256: 5aa848d69318cee34c696cf4e2dbca39cd7e8080ebc456bc473ec2a0532013a0
- evidence_id: septin-contractile-agent-UniProtKB-Q76NU1
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q76NU1.json
  locator: Exact reviewed accession, gene tokens, protein name, organism, functional/subcellular
    comments and evidence codes
  summary: Current reviewed Q76NU1 identifies vatB in Dictyostelium taxon44689. Pump
    subunit identity/complex role is verified; location comments and evidence codes
    are distinguished from a direct assay of each subunit in every CV subcompartment.
  accessed_at: '2026-11-03T11:16:58.965352Z'
  support: supports
  snapshot_sha256: 484196af4048c2df60bf0e618e372458df7ba5a7778b2f32288f73a1f328bb6d
- evidence_id: septin-contractile-agent-UniProtKB-P54648
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P54648.json
  locator: Exact reviewed accession, gene tokens, protein name, organism, functional/subcellular
    comments and evidence codes
  summary: Current reviewed P54648 identifies vatC in Dictyostelium taxon44689. Pump
    subunit identity/complex role is verified; location comments and evidence codes
    are distinguished from a direct assay of each subunit in every CV subcompartment.
  accessed_at: '2026-11-03T11:16:59.238812Z'
  support: supports
  snapshot_sha256: db4310ad9862f746a114c8af73f1363a6d432cf1329c0464fd20f4efb395feb9
- evidence_id: septin-contractile-agent-UniProtKB-Q54E04
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q54E04.json
  locator: Exact reviewed accession, gene tokens, protein name, organism, functional/subcellular
    comments and evidence codes
  summary: Current reviewed Q54E04 identifies vatM in Dictyostelium taxon44689. Pump
    subunit identity/complex role is verified; location comments and evidence codes
    are distinguished from a direct assay of each subunit in every CV subcompartment.
  accessed_at: '2026-11-03T11:16:59.512148Z'
  support: supports
  snapshot_sha256: 169ff6e42d6dcdd8abffa5ff7466a09eeabda4b1cf8b39bd2bc757a0a118fa8d
- evidence_id: septin-contractile-agent-UniProtKB-Q9U8P7
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q9U8P7.json
  locator: Exact reviewed accession, gene tokens, protein name, organism, functional/subcellular
    comments and evidence codes
  summary: Current reviewed Q9U8P7 identifies aqpA in Dictyostelium taxon44689. AqpA
    annotations concern putative channel activity and spore survival, with cell-membrane
    localization by similarity; no CV membership is established.
  accessed_at: '2026-11-03T11:17:00.112077Z'
  support: supports
  snapshot_sha256: 2409bd820504db30b75d137e0e271f109c7d362aff873366d06e2e25e7d487b8
- evidence_id: septin-contractile-agent-UniProtKB-Q54WT8
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q54WT8.json
  locator: Exact reviewed accession, gene tokens, protein name, organism, functional/subcellular
    comments and evidence codes
  summary: Current reviewed Q54WT8 identifies aqpB in Dictyostelium taxon44689. AqpB
    annotations explicitly retain impermeable tested wild type, generic vacuoles and
    plasma-membrane protrusions; direct CV localization is not asserted.
  accessed_at: '2026-11-03T11:17:00.933188Z'
  support: supports
  snapshot_sha256: 3e0bd4d141af3060c05bf394af2cd4466eb7d8a6bec6eac097862726c0a48716
- evidence_id: septin-contractile-agent-query-vatA-44689
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=100&query=%28gene_exact%3AvatA%29%20AND%20%28taxonomy_id%3A44689%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete returned exact-symbol/taxon/reviewed response and primary gene
    token
  summary: One current returned reviewed match P54647 for vatA; establishes bounded
    present query uniqueness/identity, not historical query execution or CV localization.
  accessed_at: '2026-11-03T11:16:58.800352Z'
  support: supports
  snapshot_sha256: 2c12da1e577bb5870984d56cf5bcd170fbdb89f3172708ffd84ae12b049181c9
  search_scope: UniProt REST search at 2026-11-03T11:16:58.800352Z; (gene_exact:vatA)
    AND (taxonomy_id:44689) AND (reviewed:true), format=json,size=100, one returned
    page containing one result. No alternative taxon substitution or general absence
    inference.
- evidence_id: septin-contractile-agent-query-vatB-44689
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=100&query=%28gene_exact%3AvatB%29%20AND%20%28taxonomy_id%3A44689%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete returned exact-symbol/taxon/reviewed response and primary gene
    token
  summary: One current returned reviewed match Q76NU1 for vatB; establishes bounded
    present query uniqueness/identity, not historical query execution or CV localization.
  accessed_at: '2026-11-03T11:16:59.198003Z'
  support: supports
  snapshot_sha256: f9527eae42063733d601f599bd144adebe9c130843078b50f9d8de535d4ff25d
  search_scope: UniProt REST search at 2026-11-03T11:16:59.198003Z; (gene_exact:vatB)
    AND (taxonomy_id:44689) AND (reviewed:true), format=json,size=100, one returned
    page containing one result. No alternative taxon substitution or general absence
    inference.
- evidence_id: septin-contractile-agent-query-vatC-44689
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=100&query=%28gene_exact%3AvatC%29%20AND%20%28taxonomy_id%3A44689%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete returned exact-symbol/taxon/reviewed response and primary gene
    token
  summary: One current returned reviewed match P54648 for vatC; establishes bounded
    present query uniqueness/identity, not historical query execution or CV localization.
  accessed_at: '2026-11-03T11:16:59.366153Z'
  support: supports
  snapshot_sha256: 8a15ae741468663769fb0eeb265a150c3f9360f41949cf2b46a9db2e19537553
  search_scope: UniProt REST search at 2026-11-03T11:16:59.366153Z; (gene_exact:vatC)
    AND (taxonomy_id:44689) AND (reviewed:true), format=json,size=100, one returned
    page containing one result. No alternative taxon substitution or general absence
    inference.
- evidence_id: septin-contractile-agent-query-vatM-44689
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=100&query=%28gene_exact%3AvatM%29%20AND%20%28taxonomy_id%3A44689%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete returned exact-symbol/taxon/reviewed response and primary gene
    token
  summary: One current returned reviewed match Q54E04 for vatM; establishes bounded
    present query uniqueness/identity, not historical query execution or CV localization.
  accessed_at: '2026-11-03T11:16:59.870480Z'
  support: supports
  snapshot_sha256: 7c969239729bc25a8916bb4db884580dd8f251d720b83222b316582d55b961a9
  search_scope: UniProt REST search at 2026-11-03T11:16:59.870480Z; (gene_exact:vatM)
    AND (taxonomy_id:44689) AND (reviewed:true), format=json,size=100, one returned
    page containing one result. No alternative taxon substitution or general absence
    inference.
- evidence_id: septin-contractile-agent-query-aqpA-44689
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=100&query=%28gene_exact%3AaqpA%29%20AND%20%28taxonomy_id%3A44689%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete returned exact-symbol/taxon/reviewed response and primary gene
    token
  summary: One current returned reviewed match Q9U8P7 for aqpA; establishes bounded
    present query uniqueness/identity, not historical query execution or CV localization.
  accessed_at: '2026-11-03T11:17:00.869744Z'
  support: supports
  snapshot_sha256: e80456d7a26107ef43ce58350268cbdcd94f51d261dac3639e4f2f1849add8db
  search_scope: UniProt REST search at 2026-11-03T11:17:00.869744Z; (gene_exact:aqpA)
    AND (taxonomy_id:44689) AND (reviewed:true), format=json,size=100, one returned
    page containing one result. No alternative taxon substitution or general absence
    inference.
- evidence_id: septin-contractile-agent-query-aqpB-44689
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=100&query=%28gene_exact%3AaqpB%29%20AND%20%28taxonomy_id%3A44689%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete returned exact-symbol/taxon/reviewed response and primary gene
    token
  summary: One current returned reviewed match Q54WT8 for aqpB; establishes bounded
    present query uniqueness/identity, not historical query execution or CV localization.
  accessed_at: '2026-11-03T11:17:02.028317Z'
  support: supports
  snapshot_sha256: 3a083c57f44816802e99be4216651711f86c02866b0f782a4a80fa2702e549bd
  search_scope: UniProt REST search at 2026-11-03T11:17:02.028317Z; (gene_exact:aqpB)
    AND (taxonomy_id:44689) AND (reviewed:true), format=json,size=100, one returned
    page containing one result. No alternative taxon substitution or general absence
    inference.
- evidence_id: septin-contractile-agent-query-MIP1-3055-all
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=100&query=%28gene_exact%3AMIP1%29%20AND%20%28taxonomy_id%3A3055%29
  locator: Complete returned exact MIP1/taxon3055 query with no reviewed filter
  summary: Zero results for this exact current query does not establish protein absence,
    lack of other accession names, or disprove primary MIP1 CV localization. No accession
    is guessed.
  accessed_at: '2026-11-03T11:17:02.032974Z'
  support: supports
  snapshot_sha256: 5021e624e752b001ce3e3846e8f158ed4aeb93a4c9a72fdb35a0c5b14a0eea84
  search_scope: UniProt REST search at 2026-11-03T11:17:02.032974Z; (gene_exact:MIP1)
    AND (taxonomy_id:3055), format=json,size=100, all review states, first returned
    empty page. Scope is this symbol/taxon query only.
- evidence_id: septin-catalogue
  kind: search
  reference: https://imodulondb.org/api/datasets
  locator: Complete official organism/dataset list, every id/name and dataset key
  summary: No matching Amoeba, Dictyostelium, Chlamydomonas, Trypanosoma or Paramecium
    organism/dataset is returned. Molecular/osmoregulatory response applicability
    was assessed; no unmatched-organism gene/module lookup or biological absence inference
    is justified.
  accessed_at: '2026-11-03T11:17:04.389157Z'
  support: supports
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  search_scope: Official iModulonDB GET /api/datasets at 2026-11-03T11:17:04.389157Z;
    complete returned organism list and all associated dataset keys inspected for
    the five target model genera and Eukaryota context. No date filter or unrelated
    downstream query.
- evidence_id: septin-historical-adapter-runner
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Actual canary invocation00:49:00.848907Z–00:49:00.863225Z
  summary: Historical datasets invocation exited1 with PermissionError reading runner
    pyvenv.cfg. This is retained availability evidence, not a fresh invocation or
    current successful adapter run; official source fallback was separately fetched.
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: supports
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: septin-source-access
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/adversary-septin/source-receipts.json
  locator: Actual request URLs, timestamps, outcomes and successful-response hashes
  summary: Numeric Komsic/Bülow PMC HTML and Docampo S3 JATS are genuine bodies. Guessed
    Komsic/Bülow S3 .1 paths returned404; More/Nishihara/Clarke publisher routes returned403.
    Failed routes are not source text. Other indicated primary studies are assessed
    only via complete native abstracts.
  accessed_at: '2026-11-03T11:21:49.751322Z'
  support: supports
  snapshot_sha256: 3dda68cc0d11fa457fabf98e37390cebada1b913772cc34ca27196e447bf3e8a
- evidence_id: check-qc
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/qc.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T11:22:19.889321Z'
  support: supports
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  snapshot_sha256: edb43423d06f9e82e319c11527d887dbcf3522cb6080f3ce03e406eebd6c586c
- evidence_id: check-labels
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/labels.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T11:17:22.819578Z'
  support: supports
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  snapshot_sha256: 6cdfb05df9a27194f05a5fd7f851783f817ac1523ca0bbfa54fe0e0d18775905
- evidence_id: check-trait-links
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/trait-links.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T11:17:03.448444Z'
  support: supports
  summary: Native TraitMech link check passed.
  snapshot_sha256: 8b336cdefbbd3daf6da8787990efdbe346c95e2c8361d50b7eb68a18f2d5a44a
- evidence_id: check-vendored
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/vendored.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T11:17:02.943104Z'
  support: supports
  summary: Pinned governed files match; native vendored check passed.
  snapshot_sha256: b1f169d103aaefa930745468bcca171e5867b9cc49e4e74311e458097e3252a6
- evidence_id: check-curies
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/curies.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T11:17:26.192428Z'
  support: supports
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  snapshot_sha256: fb3be251020aac118f6df680372ae7aaa32c2a1dd3366648cde95494f19d9dd2
- evidence_id: focused
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/focused-results.json
  locator: All twenty actual target schema/strict command outputs
  accessed_at: '2026-11-03T11:24:32Z'
  support: supports
  summary: Ten schema and ten strict commands returned exit zero.
  snapshot_sha256: e41b3f105e9559ec5d054cfd4b895ae3e3a988a561f2b2d0d6fa887ffdbfb770
- evidence_id: supplemental-pmid
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2361/pmid-chunks-receipt.json
  locator: Complete native-report PMID set checked with unchanged resolver in batches
    of at most fifty
  accessed_at: '2026-11-03T11:18:00.944478Z'
  support: supports
  summary: 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers
    remain unverified.
  snapshot_sha256: faacaa8fa62dace550bbb9cf4edabeda3be78641aaac138aec45f5586e0882b1
- evidence_id: historical-adapter-runner-availability
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical runner invocation receipt, cross-checked against exact stdout/stderr
    hashes; reread during PR2361 synthesis
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  summary: Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS
    PermissionError reading the configured runner pyvenv.cfg. This is a retained historical
    availability observation, not a fresh attempt or a scientific validation failure.
    Native policy permits inspected source-catalogue fallback.
assessments:
- assessment_id: plaque-t3-native
  area: schema
  topic: Native protein inventories and graph xrefs
  outcome: supported
  summary: Both commands pass with no represented protein examples or typed protein
    nodes. This validates empty inventories, not molecular narrative claims or biological
    necessity.
  target_ids:
  - cellstructuremech:contractile_vacuole_lumen
  evidence_ids:
  - plaque-current-3
  - plaque-native-contractile_vacuole_lumen-verify
  - plaque-native-contractile_vacuole_lumen-causal
- assessment_id: plaque-t3-original-provenance
  area: provenance
  topic: Immutable original and current hashes
  outcome: supported
  summary: Original native validate/render and every historical input hash pass; current
    target is byte-identical. Original findings/actions are empty. Historical record
    issue numbers and other cohort findings are not terminally disposed of here.
  target_ids:
  - cellstructuremech:contractile_vacuole_lumen
  evidence_ids:
  - plaque-current-3
  - plaque-original-3
  - plaque-original-checks
- assessment_id: plaque-t3-coverage
  area: completeness
  topic: Entire record and bounded evidence
  outcome: supported
  summary: All target fields were read. Claim-bearing evidence assessed at stated
    tiers; no compulsory protein inventory, additional images or detailed quantitative/causal
    model is inferred. No concrete record-curation defect established. Applicability
    corrections belong to review bundles.
  target_ids:
  - cellstructuremech:contractile_vacuole_lumen
  evidence_ids:
  - plaque-current-3
  - plaque-policy
  - plaque-rubric
- assessment_id: plaque-t4-native
  area: schema
  topic: Native protein inventories and graph xrefs
  outcome: supported
  summary: Both commands pass with no represented protein examples or typed protein
    nodes. This validates empty inventories, not molecular narrative claims or biological
    necessity.
  target_ids:
  - GO:0031913
  evidence_ids:
  - plaque-current-4
  - plaque-native-contractile_vacuole_pore-verify
  - plaque-native-contractile_vacuole_pore-causal
- assessment_id: plaque-t4-original-provenance
  area: provenance
  topic: Immutable original and current hashes
  outcome: supported
  summary: Original native validate/render and every historical input hash pass; current
    target is byte-identical. Original findings/actions are empty. Historical record
    issue numbers and other cohort findings are not terminally disposed of here.
  target_ids:
  - GO:0031913
  evidence_ids:
  - plaque-current-4
  - plaque-original-4
  - plaque-original-checks
- assessment_id: plaque-t4-coverage
  area: completeness
  topic: Entire record and bounded evidence
  outcome: supported
  summary: All target fields were read. Claim-bearing evidence assessed at stated
    tiers; no compulsory protein inventory, additional images or detailed quantitative/causal
    model is inferred. No concrete record-curation defect established. Applicability
    corrections belong to review bundles.
  target_ids:
  - GO:0031913
  evidence_ids:
  - plaque-current-4
  - plaque-policy
  - plaque-rubric
- assessment_id: plaque-t8-native
  area: schema
  topic: Native protein inventories and graph xrefs
  outcome: supported
  summary: Both commands pass with no represented protein examples or typed protein
    nodes. This validates empty inventories, not molecular narrative claims or biological
    necessity.
  target_ids:
  - GO:0030134
  evidence_ids:
  - plaque-current-8
  - plaque-native-copii_coated_er_to_golgi_transport_vesicle-verify
  - plaque-native-copii_coated_er_to_golgi_transport_vesicle-causal
- assessment_id: plaque-t8-original-provenance
  area: provenance
  topic: Immutable original and current hashes
  outcome: supported
  summary: Original native validate/render and every historical input hash pass; current
    target is byte-identical. Original findings/actions are empty. Historical record
    issue numbers and other cohort findings are not terminally disposed of here.
  target_ids:
  - GO:0030134
  evidence_ids:
  - plaque-current-8
  - plaque-original-8
  - plaque-original-checks
- assessment_id: plaque-t8-coverage
  area: completeness
  topic: Entire record and bounded evidence
  outcome: supported
  summary: All target fields were read. Claim-bearing evidence assessed at stated
    tiers; no compulsory protein inventory, additional images or detailed quantitative/causal
    model is inferred. No concrete record-curation defect established. Applicability
    corrections belong to review bundles.
  target_ids:
  - GO:0030134
  evidence_ids:
  - plaque-current-8
  - plaque-policy
  - plaque-rubric
- assessment_id: plaque-t9-native
  area: schema
  topic: Native protein inventories and graph xrefs
  outcome: supported
  summary: Both commands pass with no represented protein examples or typed protein
    nodes. This validates empty inventories, not molecular narrative claims or biological
    necessity.
  target_ids:
  - cellstructuremech:copii_coated_vesicle_lumen
  evidence_ids:
  - plaque-current-9
  - plaque-native-copii_coated_vesicle_lumen-verify
  - plaque-native-copii_coated_vesicle_lumen-causal
- assessment_id: plaque-t9-original-provenance
  area: provenance
  topic: Immutable original and current hashes
  outcome: supported
  summary: Original native validate/render and every historical input hash pass; current
    target is byte-identical. Original findings/actions are empty. Historical record
    issue numbers and other cohort findings are not terminally disposed of here.
  target_ids:
  - cellstructuremech:copii_coated_vesicle_lumen
  evidence_ids:
  - plaque-current-9
  - plaque-original-9
  - plaque-original-checks
- assessment_id: plaque-t9-coverage
  area: completeness
  topic: Entire record and bounded evidence
  outcome: supported
  summary: All target fields were read. Claim-bearing evidence assessed at stated
    tiers; no compulsory protein inventory, additional images or detailed quantitative/causal
    model is inferred. No concrete record-curation defect established. Applicability
    corrections belong to review bundles.
  target_ids:
  - cellstructuremech:copii_coated_vesicle_lumen
  evidence_ids:
  - plaque-current-9
  - plaque-policy
  - plaque-rubric
- assessment_id: plaque-t3-identity
  area: identity
  topic: Local lumen identity and exact topology
  outcome: supported
  summary: Exact SL0320 definition/synonym supports the local enclosed compartment,
    broader vacuolar-lumen parent and whole-vacuole parthood. Membrane, whole vacuole
    and whole complex remain distinct. Bounded GO search does not establish exhaustive
    absence.
  target_ids:
  - cellstructuremech:contractile_vacuole_lumen
  evidence_ids:
  - plaque-current-3
  - plaque-contractile-agent-go
  - plaque-contractile-agent-SL-0320
  - plaque-contractile-agent-go-lumen-search
  - plaque-neighbor-0
  - plaque-neighbor-1
  - plaque-neighbor-2
- assessment_id: plaque-t3-scope
  area: scope
  topic: Patchy occurrence and exact source models
  outcome: supported
  summary: More secondary abstract supports uneven freshwater/soil eukaryotic occurrence;
    RARE is qualitative, not a numerical census. Current taxa verify Eukaryota, Paramecium
    multimicronucleatum and Chlamydomonas reinhardtii. Gronlien example specifically
    concerns microelectrode potentials in compressed Paramecium; Komsic experiments
    use CC3395 and UVM4 derivatives rather than every algal strain.
  target_ids:
  - cellstructuremech:contractile_vacuole_lumen
  evidence_ids:
  - plaque-current-3
  - plaque-contractile-agent-go
  - plaque-contractile-agent-SL-0320
  - plaque-contractile-agent-more2024-meta
  - plaque-contractile-agent-tax-2759
  - plaque-contractile-agent-tax-44030
  - plaque-contractile-agent-tax-3055
  - plaque-contractile-agent-gronlien2002-meta
  - plaque-contractile-agent-komsic2014-pmc-numeric
- assessment_id: plaque-t3-function
  area: evidence
  topic: Filling, discharge and precise osmotic measurement scope
  outcome: supported
  summary: Allen review and Komsic body support cyclic lumen filling/expansion and
    discharge. Komsic CV size tracks cell size/growth, while contraction interval
    responds to medium osmolarity. The target states volume measurements under varied
    osmolarity and separately osmolarity-responsive cycles; it does not assert that
    volume tracks osmolarity. This wording remains within measured Table1/Results
    scope and does not inherit a sibling whole-record overclaim.
  target_ids:
  - cellstructuremech:contractile_vacuole_lumen
  evidence_ids:
  - plaque-current-3
  - plaque-contractile-agent-go
  - plaque-contractile-agent-SL-0320
  - plaque-contractile-agent-allen2002-title
  - plaque-contractile-agent-komsic2014-pmc-numeric
- assessment_id: plaque-t3-osmolarity
  area: evidence
  topic: Direct measurements versus modeled lumen properties
  outcome: unknown
  summary: Komsic explicitly could not directly determine lumen osmolarity; gradients/permeability
    are modeled. The target makes no direct osmolarity or channel-necessity claim.
    Figure captions/body, not image pixels or supplemental movies, were used.
  target_ids:
  - cellstructuremech:contractile_vacuole_lumen
  evidence_ids:
  - plaque-current-3
  - plaque-contractile-agent-go
  - plaque-contractile-agent-SL-0320
  - plaque-contractile-agent-komsic2014-pmc-numeric
- assessment_id: plaque-t3-graph
  area: graph
  topic: Lumen parthood and boundary
  outcome: supported
  summary: Both NONMECHANISTIC edges, lumen partOf whole and membrane bounds lumen,
    follow exact GO/SL topology. No channel mechanism or whole-organelle regulatory
    network is duplicated. Existing resolved boundary discussion is consistent with
    current content, without recertifying an external historical issue.
  target_ids:
  - cellstructuremech:contractile_vacuole_lumen
  evidence_ids:
  - plaque-current-3
  - plaque-contractile-agent-go
  - plaque-contractile-agent-SL-0320
  - plaque-graph-policy
- assessment_id: plaque-t3-composition
  area: grounding
  topic: Enclosed region with no forced constituent inventory
  outcome: supported
  summary: The lumen is a spatial region, not its membrane or molecular transport
    machinery. No named constituent or formation-essential protein is asserted. Empty
    components are appropriate to the claim scope.
  target_ids:
  - cellstructuremech:contractile_vacuole_lumen
  evidence_ids:
  - plaque-current-3
  - plaque-contractile-agent-go
  - plaque-contractile-agent-SL-0320
- assessment_id: plaque-t3-adapter
  area: scope
  topic: Explicit osmotic-response applicability
  outcome: supported
  summary: The record explicitly invokes osmolarity-responsive filling/discharge and
    osmoregulation. Stress-response/trait context triggers applicability despite no
    proteins. Original has no structured-source row. Fresh full catalogue has no relevant
    eukaryotic host, so no matched gene/module query applies; historical runner limitation
    remains separately dated.
  target_ids:
  - cellstructuremech:contractile_vacuole_lumen
  evidence_ids:
  - plaque-current-3
  - plaque-contractile-agent-go
  - plaque-contractile-agent-SL-0320
  - plaque-original-3
  - plaque-policy
  - plaque-catalogue
  - plaque-historical-runner
- assessment_id: plaque-t4-identity
  area: identity
  topic: Stable pore versus transient opening or whole vacuole
  outcome: supported
  summary: Exact active GO0031913 definition and typed is_a/part_of relations agree.
    A persistent site is distinguished from its transient discharge opening and from
    the whole CV. MULTIPROTEIN_COMPLEX is ontology classification, not a claimed experimentally
    resolved subunit list.
  target_ids:
  - GO:0031913
  evidence_ids:
  - plaque-current-4
  - plaque-root24-sources-pore-go
  - plaque-root24-sources-frankel2000-university-pdf
  - plaque-root24-sources-mckanna1973-crossref
  - plaque-root24-sources-pore-ancestors
- assessment_id: plaque-t4-scope
  area: scope
  topic: Species-qualified secondary model and genus primary synopsis
  outcome: supported
  summary: Current taxon verifies T.thermophila5911. Record explicitly presents Frankel
    as review-level model support. McKanna synopsis supports Paramecium genus ultrastructure
    only; no missing species is invented and older T.pyriformis citations are not
    relabeled thermophila experiments.
  target_ids:
  - GO:0031913
  evidence_ids:
  - plaque-current-4
  - plaque-root24-sources-pore-go
  - plaque-root24-sources-frankel2000-university-pdf
  - plaque-root24-sources-mckanna1973-crossref
  - plaque-root24-sources-NCBITaxon-5911
  - plaque-root24-sources-frankel2000-pmid
  - plaque-root24-sources-frankel2000-quoteddoi
- assessment_id: plaque-t4-composition
  area: grounding
  topic: Unresolved pore molecular composition
  outcome: unknown
  summary: Frankel text and McKanna synopsis describe cortical membrane/diaphragm
    and microtubule organization, but do not establish a complete molecular inventory
    or exact essential subunit. Existing open composition TODO correctly withholds
    protein IDs; absence of molecular inventory alone is not a defect.
  target_ids:
  - GO:0031913
  evidence_ids:
  - plaque-current-4
  - plaque-root24-sources-pore-go
  - plaque-root24-sources-frankel2000-university-pdf
  - plaque-root24-sources-mckanna1973-crossref
- assessment_id: plaque-t4-graph
  area: graph
  topic: Coarse parthood and liquid-flow function
  outcome: supported
  summary: Two partOf edges and descriptive regulation of liquid flow follow GO definition
    and inspected morphology. NONMECHANISTIC scope makes no actin necessity, force-generation,
    gating-rate or subunit-dependency claim.
  target_ids:
  - GO:0031913
  evidence_ids:
  - plaque-current-4
  - plaque-root24-sources-pore-go
  - plaque-root24-sources-frankel2000-university-pdf
  - plaque-root24-sources-mckanna1973-crossref
  - plaque-graph-policy
- assessment_id: plaque-t4-adapter
  area: scope
  topic: Genuine topology and coarse-flow exclusion
  outcome: not_applicable
  summary: No named gene, locus, protein identity, regulator, explicit stress-response
    pathway or transcriptomic assignment is made. Generic liquid-flow control and
    the ontology complex label do not establish a candidate molecular query. Original
    N/A outcome is retained with this concrete rationale, not counted as a defect
    solely because its sentence mentioned absence of expression inference. Catalogue
    also has no relevant ciliate host.
  target_ids:
  - GO:0031913
  evidence_ids:
  - plaque-current-4
  - plaque-root24-sources-pore-go
  - plaque-root24-sources-frankel2000-university-pdf
  - plaque-root24-sources-mckanna1973-crossref
  - plaque-original-4
  - plaque-policy
  - plaque-catalogue
- assessment_id: plaque-t4-source-tiers
  area: provenance
  topic: Accessible secondary chapter and primary synopsis
  outcome: supported
  summary: Frankel genuine institutional PDF was read only at named complete CV/pore
    sections and opening positioning paragraphs. McKanna is publisher-deposited primary
    synopsis, not full article. API bibliographic stub and publisher challenge pages
    are not bodies. No microscopy pixels or complete-book review claimed.
  target_ids:
  - GO:0031913
  evidence_ids:
  - plaque-current-4
  - plaque-root24-sources-pore-go
  - plaque-root24-sources-frankel2000-university-pdf
  - plaque-root24-sources-mckanna1973-crossref
  - plaque-root24-sources-frankel2000-api
  - plaque-root24-sources-mckanna1973-pdf
- assessment_id: plaque-t8-scope
  area: scope
  topic: Yeast occurrence and experimental specificity
  outcome: supported
  summary: Current ENA verifies S.cerevisiae4932. Barlowe abstract supports native
    ER-derived COPII transport intermediates; Matsuoka body includes native microsomes
    and distinct synthetic-liposome experiments with named yeast preparations. COMMON
    remains qualitative model-system context, not a population census or universal
    cell-state assertion.
  target_ids:
  - GO:0030134
  evidence_ids:
  - plaque-current-8
  - plaque-copii-agent-go
  - plaque-copii-agent-PMID-8004676
  - plaque-copii-agent-matsuoka1998-author
  - plaque-copii-agent-tax4932
- assessment_id: plaque-t8-necessity
  area: evidence
  topic: Reconstitution versus universal formation necessity
  outcome: unknown
  summary: Sec/Sar1 machinery is positively supported as COPII coat/budding context.
    Synthetic-liposome conditions, altered concentrations and GMP-PNP differ from
    physiological native transport; success in reconstitution is not proof of each
    molecule being universally necessary in vivo. No individual essentiality assertion
    is made on these targets.
  target_ids:
  - GO:0030134
  evidence_ids:
  - plaque-current-8
  - plaque-copii-agent-go
  - plaque-copii-agent-PMID-8004676
  - plaque-copii-agent-matsuoka1998-author
- assessment_id: plaque-t8-adapter
  area: scope
  topic: Named Sec/Sar molecular applicability
  outcome: supported
  summary: Both target narratives explicitly name Sec/Sar machinery despite sparse
    direct components. Original expression-only N/A rationales therefore miss the
    actual molecular trigger. Fresh complete catalogue lacks S.cerevisiae; no unmatched
    strain/species module evidence is substituted and no biological absence follows.
    Historical runner is unavailable at its original time, not freshly rerun.
  target_ids:
  - GO:0030134
  evidence_ids:
  - plaque-current-8
  - plaque-copii-agent-go
  - plaque-copii-agent-PMID-8004676
  - plaque-copii-agent-matsuoka1998-author
  - plaque-original-8
  - plaque-policy
  - plaque-catalogue
  - plaque-historical-runner
- assessment_id: plaque-t8-source-tiers
  area: provenance
  topic: Primary abstract and genuine fresh primary body
  outcome: supported
  summary: Barlowe1994 is used at complete primary abstract tier only; publisher routes
    returned challenges. Fresh institutional Matsuoka1998 PDF was read pp263–274,
    including Methods, Tables and captions; no raw data/figure-pixel or live-cell
    lumen audit. The PDF was freshly fetched here, not represented as an old cached
    receipt.
  target_ids:
  - GO:0030134
  evidence_ids:
  - plaque-current-8
  - plaque-copii-agent-go
  - plaque-copii-agent-PMID-8004676
  - plaque-copii-agent-matsuoka1998-author
  - plaque-copii-agent-barlowe1994-publisher
  - plaque-copii-agent-barlowe1994-sciencedirect
  - plaque-copii-agent-PMID-9568718
- assessment_id: plaque-t9-scope
  area: scope
  topic: Yeast occurrence and experimental specificity
  outcome: supported
  summary: Current ENA verifies S.cerevisiae4932. Barlowe abstract supports native
    ER-derived COPII transport intermediates; Matsuoka body includes native microsomes
    and distinct synthetic-liposome experiments with named yeast preparations. COMMON
    remains qualitative model-system context, not a population census or universal
    cell-state assertion.
  target_ids:
  - cellstructuremech:copii_coated_vesicle_lumen
  evidence_ids:
  - plaque-current-9
  - plaque-copii-agent-go
  - plaque-copii-agent-PMID-8004676
  - plaque-copii-agent-matsuoka1998-author
  - plaque-copii-agent-tax4932
- assessment_id: plaque-t9-necessity
  area: evidence
  topic: Reconstitution versus universal formation necessity
  outcome: unknown
  summary: Sec/Sar1 machinery is positively supported as COPII coat/budding context.
    Synthetic-liposome conditions, altered concentrations and GMP-PNP differ from
    physiological native transport; success in reconstitution is not proof of each
    molecule being universally necessary in vivo. No individual essentiality assertion
    is made on these targets.
  target_ids:
  - cellstructuremech:copii_coated_vesicle_lumen
  evidence_ids:
  - plaque-current-9
  - plaque-copii-agent-go
  - plaque-copii-agent-PMID-8004676
  - plaque-copii-agent-matsuoka1998-author
- assessment_id: plaque-t9-adapter
  area: scope
  topic: Named Sec/Sar molecular applicability
  outcome: supported
  summary: Both target narratives explicitly name Sec/Sar machinery despite sparse
    direct components. Original expression-only N/A rationales therefore miss the
    actual molecular trigger. Fresh complete catalogue lacks S.cerevisiae; no unmatched
    strain/species module evidence is substituted and no biological absence follows.
    Historical runner is unavailable at its original time, not freshly rerun.
  target_ids:
  - cellstructuremech:copii_coated_vesicle_lumen
  evidence_ids:
  - plaque-current-9
  - plaque-copii-agent-go
  - plaque-copii-agent-PMID-8004676
  - plaque-copii-agent-matsuoka1998-author
  - plaque-original-9
  - plaque-policy
  - plaque-catalogue
  - plaque-historical-runner
- assessment_id: plaque-t9-source-tiers
  area: provenance
  topic: Primary abstract and genuine fresh primary body
  outcome: supported
  summary: Barlowe1994 is used at complete primary abstract tier only; publisher routes
    returned challenges. Fresh institutional Matsuoka1998 PDF was read pp263–274,
    including Methods, Tables and captions; no raw data/figure-pixel or live-cell
    lumen audit. The PDF was freshly fetched here, not represented as an old cached
    receipt.
  target_ids:
  - cellstructuremech:copii_coated_vesicle_lumen
  evidence_ids:
  - plaque-current-9
  - plaque-copii-agent-go
  - plaque-copii-agent-PMID-8004676
  - plaque-copii-agent-matsuoka1998-author
  - plaque-copii-agent-barlowe1994-publisher
  - plaque-copii-agent-barlowe1994-sciencedirect
  - plaque-copii-agent-PMID-9568718
- assessment_id: plaque-t8-identity
  area: identity
  topic: Whole COPII vesicle distinct from its coat
  outcome: supported
  summary: GO0030134 exactly denotes the COPII-coated ER-to-Golgi vesicle with Sec23/24
    and Sec13/31 heterodimer coat narrative. Coated-vesicle parent, coat structural
    part, and exact/related synonym types agree. The whole membrane-bounded organelle
    is not reduced to a protein complex.
  target_ids:
  - GO:0030134
  evidence_ids:
  - plaque-current-8
  - plaque-copii-agent-go
- assessment_id: plaque-t8-composition
  area: grounding
  topic: Constituent coat context without redundant inventories
  outcome: supported
  summary: Named coat subcomplexes are supported by source definitions and primary
    experiments. They remain coat/budding context, not a mandatory duplicate inventory
    of components on the whole-vesicle record. No represented protein accession exists
    to falsely certify.
  target_ids:
  - GO:0030134
  evidence_ids:
  - plaque-current-8
  - plaque-copii-agent-go
  - plaque-copii-agent-PMID-8004676
  - plaque-copii-agent-matsuoka1998-author
- assessment_id: plaque-t8-function
  area: evidence
  topic: Transport function distinguished from budding
  outcome: supported
  summary: GO0006888 represents ER-to-Golgi transport, whereas GO0090114 represents
    ER-membrane evagination/budding. The record correctly attributes transport to
    vesicle and budding context to coat. Barlowe GTP vesicles can target/fuse; GMP-PNP
    products cannot, so evidence does not license universal transport competence of
    synthetic coated buds.
  target_ids:
  - GO:0030134
  evidence_ids:
  - plaque-current-8
  - plaque-copii-agent-go
  - plaque-copii-agent-PMID-8004676
  - plaque-copii-agent-matsuoka1998-author
- assessment_id: plaque-t8-graph
  area: graph
  topic: Five descriptive transport-topology edges
  outcome: supported
  summary: Coat partOf whole, ER membrane evagination into vesicle, vesicle cargo
    transport to Golgi, coat participation in budding, and vesicle participation in
    transport align with exact GO and primary scopes. NONMECHANISTIC graph does not
    claim vesicle self-formation or complete molecular mechanism. Historical record
    issue numbers remain context only.
  target_ids:
  - GO:0030134
  evidence_ids:
  - plaque-current-8
  - plaque-copii-agent-go
  - plaque-copii-agent-PMID-8004676
  - plaque-copii-agent-matsuoka1998-author
  - plaque-graph-policy
- assessment_id: plaque-t9-identity
  area: identity
  topic: SL-defined local lumen and exact candidate conflict
  outcome: unknown
  summary: SL0322 exactly defines this lumen and supports synonyms, cytoplasmic-vesicle-lumen
    parent and whole-vesicle parthood. Active GO0106173 exact label conflicts with
    its endocytic definition. Preserve that unresolved authority conflict rather than
    force a GO replacement or claim the candidate is absent.
  target_ids:
  - cellstructuremech:copii_coated_vesicle_lumen
  evidence_ids:
  - plaque-current-9
  - plaque-copii-agent-SL-0322
  - plaque-copii-agent-go
  - plaque-copii-agent-go-lumen-candidates
- assessment_id: plaque-t9-composition
  area: grounding
  topic: Enclosed lumen distinct from machinery
  outcome: supported
  summary: The enclosed region has no required constituent cargo/protein inventory.
    Sec/Sar machinery describes formation context rather than lumen constitution.
    Primary synthetic trapped-solute experiment supports closed lumen formation in
    its own assay, not direct live-yeast lumen morphology or every cargo composition.
  target_ids:
  - cellstructuremech:copii_coated_vesicle_lumen
  evidence_ids:
  - plaque-current-9
  - plaque-copii-agent-SL-0322
  - plaque-copii-agent-matsuoka1998-author
- assessment_id: plaque-t9-graph
  area: graph
  topic: Lumen parthood and membrane boundary
  outcome: supported
  summary: The two NONMECHANISTIC edges are lumen partOf whole and ER-to-Golgi-vesicle
    membrane bounds lumen. Exact SL0322 and GO0012507 support the geometry without
    importing cargo selection, fusion or individual assembly necessity.
  target_ids:
  - cellstructuremech:copii_coated_vesicle_lumen
  evidence_ids:
  - plaque-current-9
  - plaque-copii-agent-SL-0322
  - plaque-copii-agent-go
  - plaque-graph-policy
- assessment_id: micro-copi_coated_vesicle-identity
  area: identity
  topic: Exact structure, membrane and lumen boundaries
  outcome: supported
  summary: The whole vesicle is a membrane-bounded organelle; its membrane is a bilayer
    and its lumen a bounded region. Exact native definitions and hierarchy agree.
    Coatomer remains the coat complex, not a whole-vesicle synonym. The lumen candidate
    caveat is explicit below.
  target_ids:
  - GO:0030137
  evidence_ids:
  - micro-record-copi_coated_vesicle
  - micro-go
  - micro-SL-0321
  - micro-review-checklist
- assessment_id: micro-copi_coated_vesicle-scope
  area: scope
  topic: Yeast experimental scope and source tiers
  outcome: supported
  summary: Sandmann supports a yeast early-secretory/COPI model through coatomer-mutant,
    binding and vesicle assays. Canonical wording does not assert a specific strain/quantitative
    preparation. COMMON is qualitative occurrence; membrane/lumen occurrence follows
    the bounded-vesicle model and authority definitions, not a separately measured
    population frequency. E. coli expression is not assigned as the structure host.
  target_ids:
  - GO:0030137
  evidence_ids:
  - micro-record-copi_coated_vesicle
  - micro-sandmann2003-pmc
  - micro-sandmann2003-meta
  - micro-NCBITaxon-4932
  - micro-go
  - micro-SL-0321
- assessment_id: micro-copi_coated_vesicle-composition
  area: grounding
  topic: Component versus topology representation
  outcome: supported
  summary: Coat and bilayer are structural parts. Keeping coatomer/Arf constituents
    on the coat neighbor avoids duplicating its molecular inventory. Waters abstract
    and scoped Yu model support this boundary, not universal subunit necessity.
  target_ids:
  - GO:0030137
  evidence_ids:
  - micro-record-copi_coated_vesicle
  - micro-go
  - micro-SL-0321
  - micro-neighbor-copi_vesicle_coat
  - micro-native-schema
  - micro-waters1991-meta
  - micro-yu2012-s3
- assessment_id: micro-copi_coated_vesicle-graph
  area: graph
  topic: Every current directed edge and bounded semantics
  outcome: supported
  summary: Six NONMECHANISTIC edges retain coat/bilayer parthood, Golgi evagination,
    budding and retrograde participation. The new process-to-ER edge adds a destination,
    matching GO0006890 directed substances Golgi→ER and COPI carrier scope. Broad
    proteins/lipids are consistent with source transport context, not a lipid-species
    flux assay or fusion mechanism.
  target_ids:
  - GO:0030137
  evidence_ids:
  - micro-record-copi_coated_vesicle
  - micro-go
  - micro-SL-0321
  - micro-graph-policy
  - micro-sandmann2003-pmc
  - micro-stale-diff
  - micro-yu2012-s3
  - micro-neighbor-endoplasmic_reticulum
  - micro-neighbor-golgi_membrane
- assessment_id: micro-copi_coated_vesicle-sources
  area: evidence
  topic: Primary versus authority/secondary source scope
  outcome: supported
  summary: 'Source-specific statements remain separated: Sandmann selected primary
    body sections; native exact authority definitions; Waters primary abstract only
    where cited; retained Yu scoped body for coat recruitment. The 2018 review is
    explicitly secondary context and does not substitute for direct experimental lipid
    flux or resolve the lumen definition conflict.'
  target_ids:
  - GO:0030137
  evidence_ids:
  - micro-record-copi_coated_vesicle
  - micro-sandmann2003-pmc
  - micro-go
  - micro-lumen-citation-meta
  - micro-waters1991-meta
  - micro-waters1991-publisher
  - micro-yu2012-s3
- assessment_id: micro-copi_coated_vesicle-adapter
  area: provenance
  topic: Structured-source applicability reassessed
  outcome: supported
  summary: Native molecular/pathway trigger is present in coatomer/Arf or coatomer-dependent
    retrograde-retrieval narrative. Original expression-only exclusion is insufficient.
    Complete current official catalogue has no matching yeast dataset, so downstream
    matching-gene/module checks are inapplicable. Historical runner failure is separately
    dated and no biological absence inferred.
  target_ids:
  - GO:0030137
  evidence_ids:
  - micro-record-copi_coated_vesicle
  - micro-prior-copi_coated_vesicle
  - micro-review-policy
  - micro-review-config
  - micro-catalogue
  - micro-historical-adapter-runner
- assessment_id: micro-copi_coated_vesicle-schema
  area: schema
  topic: Native original pairs, frozen inputs and limited protein checks
  outcome: supported
  summary: Original YAML validates and Markdown renders exactly. Original target hash
    differs only by the documented history/edge additions; current content has been
    substantively reassessed. Both current native protein commands pass empty inventories/zero
    molecular nodes; they cannot certify prose mechanisms.
  target_ids:
  - GO:0030137
  evidence_ids:
  - micro-record-copi_coated_vesicle
  - micro-prior-copi_coated_vesicle
  - micro-original-validation-inputs
  - micro-native-copi_coated_vesicle-verify
  - micro-native-copi_coated_vesicle-causal
  - micro-stale-diff
- assessment_id: micro-copi_coated_vesicle-coverage
  area: completeness
  topic: Entire maintained record and bounded verdict
  outcome: supported
  summary: All maintained fields, notes, discussions, source references and graph
    edges were assessed. No image, quantitative property, snippet or protein inventory
    is asserted by this target. Empty optional fields and acknowledged label-only
    material do not establish defects. Original observations remain immutable, with
    no original findings or request-curation actions to carry forward; historical
    record issue closures are not re-disposed.
  target_ids:
  - GO:0030137
  evidence_ids:
  - micro-record-copi_coated_vesicle
  - micro-prior-copi_coated_vesicle
  - micro-review-profile
  - micro-go
  - micro-sandmann2003-pmc
- assessment_id: micro-copi_coated_vesicle_lumen-identity
  area: identity
  topic: Exact structure, membrane and lumen boundaries
  outcome: supported
  summary: The whole vesicle is a membrane-bounded organelle; its membrane is a bilayer
    and its lumen a bounded region. Exact native definitions and hierarchy agree.
    Coatomer remains the coat complex, not a whole-vesicle synonym. The lumen candidate
    caveat is explicit below.
  target_ids:
  - cellstructuremech:copi_coated_vesicle_lumen
  evidence_ids:
  - micro-record-copi_coated_vesicle_lumen
  - micro-go
  - micro-SL-0321
  - micro-review-checklist
- assessment_id: micro-copi_coated_vesicle_lumen-scope
  area: scope
  topic: Yeast experimental scope and source tiers
  outcome: supported
  summary: Sandmann supports a yeast early-secretory/COPI model through coatomer-mutant,
    binding and vesicle assays. Canonical wording does not assert a specific strain/quantitative
    preparation. COMMON is qualitative occurrence; membrane/lumen occurrence follows
    the bounded-vesicle model and authority definitions, not a separately measured
    population frequency. E. coli expression is not assigned as the structure host.
  target_ids:
  - cellstructuremech:copi_coated_vesicle_lumen
  evidence_ids:
  - micro-record-copi_coated_vesicle_lumen
  - micro-sandmann2003-pmc
  - micro-sandmann2003-meta
  - micro-NCBITaxon-4932
  - micro-go
  - micro-SL-0321
- assessment_id: micro-copi_coated_vesicle_lumen-composition
  area: grounding
  topic: Component versus topology representation
  outcome: supported
  summary: The lumen is a region rather than a molecular component; no exact family
    or cargo inventory is required.
  target_ids:
  - cellstructuremech:copi_coated_vesicle_lumen
  evidence_ids:
  - micro-record-copi_coated_vesicle_lumen
  - micro-go
  - micro-SL-0321
  - micro-neighbor-copi_vesicle_coat
  - micro-native-schema
- assessment_id: micro-copi_coated_vesicle_lumen-graph
  area: graph
  topic: Every current directed edge and bounded semantics
  outcome: supported
  summary: Two NONMECHANISTIC edges state bounded lumen inside the whole vesicle and
    its membrane boundary. No cargo sorting, coat assembly or fusion is asserted.
  target_ids:
  - cellstructuremech:copi_coated_vesicle_lumen
  evidence_ids:
  - micro-record-copi_coated_vesicle_lumen
  - micro-go
  - micro-SL-0321
  - micro-graph-policy
  - micro-sandmann2003-pmc
- assessment_id: micro-copi_coated_vesicle_lumen-sources
  area: evidence
  topic: Primary versus authority/secondary source scope
  outcome: supported
  summary: 'Source-specific statements remain separated: Sandmann selected primary
    body sections; native exact authority definitions; Waters primary abstract only
    where cited; retained Yu scoped body for coat recruitment. The 2018 review is
    explicitly secondary context and does not substitute for direct experimental lipid
    flux or resolve the lumen definition conflict.'
  target_ids:
  - cellstructuremech:copi_coated_vesicle_lumen
  evidence_ids:
  - micro-record-copi_coated_vesicle_lumen
  - micro-sandmann2003-pmc
  - micro-go
  - micro-lumen-citation-meta
- assessment_id: micro-copi_coated_vesicle_lumen-adapter
  area: provenance
  topic: Structured-source applicability reassessed
  outcome: supported
  summary: Native molecular/pathway trigger is present in coatomer/Arf or coatomer-dependent
    retrograde-retrieval narrative. Original expression-only exclusion is insufficient.
    Complete current official catalogue has no matching yeast dataset, so downstream
    matching-gene/module checks are inapplicable. Historical runner failure is separately
    dated and no biological absence inferred.
  target_ids:
  - cellstructuremech:copi_coated_vesicle_lumen
  evidence_ids:
  - micro-record-copi_coated_vesicle_lumen
  - micro-prior-copi_coated_vesicle_lumen
  - micro-review-policy
  - micro-review-config
  - micro-catalogue
  - micro-historical-adapter-runner
- assessment_id: micro-copi_coated_vesicle_lumen-schema
  area: schema
  topic: Native original pairs, frozen inputs and limited protein checks
  outcome: supported
  summary: Original YAML validates and Markdown renders exactly. Original frozen target
    hash equals current main. Both current native protein commands pass empty inventories/zero
    molecular nodes; they cannot certify prose mechanisms.
  target_ids:
  - cellstructuremech:copi_coated_vesicle_lumen
  evidence_ids:
  - micro-record-copi_coated_vesicle_lumen
  - micro-prior-copi_coated_vesicle_lumen
  - micro-original-validation-inputs
  - micro-native-copi_coated_vesicle_lumen-verify
  - micro-native-copi_coated_vesicle_lumen-causal
- assessment_id: micro-copi_coated_vesicle_lumen-coverage
  area: completeness
  topic: Entire maintained record and bounded verdict
  outcome: supported
  summary: All maintained fields, notes, discussions, source references and graph
    edges were assessed. No image, quantitative property, snippet or protein inventory
    is asserted by this target. Empty optional fields and acknowledged label-only
    material do not establish defects. Original observations remain immutable, with
    no original findings or request-curation actions to carry forward; historical
    record issue closures are not re-disposed.
  target_ids:
  - cellstructuremech:copi_coated_vesicle_lumen
  evidence_ids:
  - micro-record-copi_coated_vesicle_lumen
  - micro-prior-copi_coated_vesicle_lumen
  - micro-review-profile
  - micro-go
  - micro-sandmann2003-pmc
- assessment_id: micro-copi_coated_vesicle_membrane-identity
  area: identity
  topic: Exact structure, membrane and lumen boundaries
  outcome: supported
  summary: The whole vesicle is a membrane-bounded organelle; its membrane is a bilayer
    and its lumen a bounded region. Exact native definitions and hierarchy agree.
    Coatomer remains the coat complex, not a whole-vesicle synonym. The lumen candidate
    caveat is explicit below.
  target_ids:
  - GO:0030663
  evidence_ids:
  - micro-record-copi_coated_vesicle_membrane
  - micro-go
  - micro-SL-0321
  - micro-review-checklist
- assessment_id: micro-copi_coated_vesicle_membrane-scope
  area: scope
  topic: Yeast experimental scope and source tiers
  outcome: supported
  summary: Sandmann supports a yeast early-secretory/COPI model through coatomer-mutant,
    binding and vesicle assays. Canonical wording does not assert a specific strain/quantitative
    preparation. COMMON is qualitative occurrence; membrane/lumen occurrence follows
    the bounded-vesicle model and authority definitions, not a separately measured
    population frequency. E. coli expression is not assigned as the structure host.
  target_ids:
  - GO:0030663
  evidence_ids:
  - micro-record-copi_coated_vesicle_membrane
  - micro-sandmann2003-pmc
  - micro-sandmann2003-meta
  - micro-NCBITaxon-4932
  - micro-go
  - micro-SL-0321
- assessment_id: micro-copi_coated_vesicle_membrane-composition
  area: grounding
  topic: Component versus topology representation
  outcome: supported
  summary: The direct LIPID row describes collective bilayer material. Label-only
    grounding and component_ref avoid inventing a molecular lipid identity. Coat parthood
    is compatible with keeping coatomer/Arf out of the lipid constituent list; no
    individual lipid necessity is demonstrated.
  target_ids:
  - GO:0030663
  evidence_ids:
  - micro-record-copi_coated_vesicle_membrane
  - micro-go
  - micro-SL-0321
  - micro-neighbor-copi_vesicle_coat
  - micro-native-schema
- assessment_id: micro-copi_coated_vesicle_membrane-graph
  area: graph
  topic: Every current directed edge and bounded semantics
  outcome: supported
  summary: Three NONMECHANISTIC edges state bilayer parthood/boundary and Golgi membrane
    donation. GO0035964 directly specifies evagination; no separate assembly mechanism
    or constituent necessity follows.
  target_ids:
  - GO:0030663
  evidence_ids:
  - micro-record-copi_coated_vesicle_membrane
  - micro-go
  - micro-SL-0321
  - micro-graph-policy
  - micro-sandmann2003-pmc
- assessment_id: micro-copi_coated_vesicle_membrane-sources
  area: evidence
  topic: Primary versus authority/secondary source scope
  outcome: supported
  summary: 'Source-specific statements remain separated: Sandmann selected primary
    body sections; native exact authority definitions; Waters primary abstract only
    where cited; retained Yu scoped body for coat recruitment. The 2018 review is
    explicitly secondary context and does not substitute for direct experimental lipid
    flux or resolve the lumen definition conflict.'
  target_ids:
  - GO:0030663
  evidence_ids:
  - micro-record-copi_coated_vesicle_membrane
  - micro-sandmann2003-pmc
  - micro-go
  - micro-lumen-citation-meta
- assessment_id: micro-copi_coated_vesicle_membrane-adapter
  area: provenance
  topic: Structured-source applicability reassessed
  outcome: supported
  summary: Native molecular/pathway trigger is present in coatomer/Arf or coatomer-dependent
    retrograde-retrieval narrative. Original expression-only exclusion is insufficient.
    Complete current official catalogue has no matching yeast dataset, so downstream
    matching-gene/module checks are inapplicable. Historical runner failure is separately
    dated and no biological absence inferred.
  target_ids:
  - GO:0030663
  evidence_ids:
  - micro-record-copi_coated_vesicle_membrane
  - micro-prior-copi_coated_vesicle_membrane
  - micro-review-policy
  - micro-review-config
  - micro-catalogue
  - micro-historical-adapter-runner
- assessment_id: micro-copi_coated_vesicle_membrane-schema
  area: schema
  topic: Native original pairs, frozen inputs and limited protein checks
  outcome: supported
  summary: Original YAML validates and Markdown renders exactly. Original frozen target
    hash equals current main. Both current native protein commands pass empty inventories/zero
    molecular nodes; they cannot certify prose mechanisms.
  target_ids:
  - GO:0030663
  evidence_ids:
  - micro-record-copi_coated_vesicle_membrane
  - micro-prior-copi_coated_vesicle_membrane
  - micro-original-validation-inputs
  - micro-native-copi_coated_vesicle_membrane-verify
  - micro-native-copi_coated_vesicle_membrane-causal
- assessment_id: micro-copi_coated_vesicle_membrane-coverage
  area: completeness
  topic: Entire maintained record and bounded verdict
  outcome: supported
  summary: All maintained fields, notes, discussions, source references and graph
    edges were assessed. No image, quantitative property, snippet or protein inventory
    is asserted by this target. Empty optional fields and acknowledged label-only
    material do not establish defects. Original observations remain immutable, with
    no original findings or request-curation actions to carry forward; historical
    record issue closures are not re-disposed.
  target_ids:
  - GO:0030663
  evidence_ids:
  - micro-record-copi_coated_vesicle_membrane
  - micro-prior-copi_coated_vesicle_membrane
  - micro-review-profile
  - micro-go
  - micro-sandmann2003-pmc
- assessment_id: micro-lumen-go-equivalence
  area: grounding
  topic: Same-label GO candidate remains definition-limited
  outcome: unknown
  summary: GO0106172 is active and returned by current search, but both exact QuickGO
    and OLS descriptions specify an endocytic vesicle. SL-0321 and the local target
    denote general COPI lumen. Secondary definition-citation abstract describes Golgi/ER
    traffic but does not resolve this inconsistency. Retain unknown exact equivalence;
    no mandatory remapping or universal absence claim follows.
  target_ids:
  - cellstructuremech:copi_coated_vesicle_lumen
  evidence_ids:
  - micro-go
  - micro-go0106172-ols
  - micro-SL-0321
  - micro-lumen-search
  - micro-lumen-citation-meta
- assessment_id: micro-membrane-specific-lipid-necessity
  area: grounding
  topic: Collective bilayer versus individual lipid requirement
  outcome: unknown
  summary: The ESSENTIAL component denotes the collective bilayer constituting the
    membrane. No individual lipid species, deletion test or replacement necessity
    is specified or inferred from the ontology/vesicle assays.
  target_ids:
  - GO:0030663
  evidence_ids:
  - micro-record-copi_coated_vesicle_membrane
  - micro-go
  - micro-native-schema
  - micro-sandmann2003-pmc
- assessment_id: septin-contractile_vacuolar_membrane-schema
  area: schema
  topic: Original validation, deterministic rendering and input currentness
  outcome: supported
  summary: Original bundle validates/renders exactly and its frozen target hash matches
    current bytes and the original source revision. Native inventory checks pass with
    their actual coverage limits, not as certification of all scientific assertions.
  target_ids:
  - GO:0031164
  evidence_ids:
  - septin-record-contractile_vacuolar_membrane
  - septin-original-validation-contractile_vacuolar_membrane
  - septin-native-contractile_vacuolar_membrane-verify
  - septin-native-contractile_vacuolar_membrane-causal
- assessment_id: septin-contractile_vacuolar_membrane-native-scope
  area: provenance
  topic: Actual protein inventory coverage
  outcome: supported
  summary: No protein examples or UniProtKB protein xrefs. The two protein nodes comprise
    one NO_GENE_SYMBOLS aquaporin component and one UNANCHORED_NO_UNIPROT perivacuolar
    V-ATPase context node. Exit0 does not verify species-specific identity, localization
    or necessity.
  target_ids:
  - GO:0031164
  evidence_ids:
  - septin-record-contractile_vacuolar_membrane
  - septin-native-contractile_vacuolar_membrane-verify
  - septin-native-contractile_vacuolar_membrane-causal
- assessment_id: septin-contractile_vacuolar_membrane-images
  area: scope
  topic: No target images, measurements or verbatim snippets
  outcome: not_applicable
  summary: None is declared in this maintained target. Primary body/caption text inspection
    does not constitute figure-pixel, supplementary movie or raw-data reanalysis.
  target_ids:
  - GO:0031164
  evidence_ids:
  - septin-record-contractile_vacuolar_membrane
- assessment_id: septin-contractile_vacuole-schema
  area: schema
  topic: Original validation, deterministic rendering and input currentness
  outcome: supported
  summary: Original bundle validates/renders exactly and its frozen target hash matches
    current bytes and the original source revision. Native inventory checks pass with
    their actual coverage limits, not as certification of all scientific assertions.
  target_ids:
  - GO:0000331
  evidence_ids:
  - septin-record-contractile_vacuole
  - septin-original-validation-contractile_vacuole
  - septin-native-contractile_vacuole-verify
  - septin-native-contractile_vacuole-causal
- assessment_id: septin-contractile_vacuole-native-scope
  area: provenance
  topic: Actual protein inventory coverage
  outcome: supported
  summary: Six protein examples verify. The V-ATPase node is COVERED by four examples;
    the aquaporin node is PARTIAL_EXAMPLES with MIP1 missing. This is inventory/identity
    coverage, not proof that aqpA/aqpB reside in a CV or that MIP1 lacks a biological
    counterpart.
  target_ids:
  - GO:0000331
  evidence_ids:
  - septin-record-contractile_vacuole
  - septin-native-contractile_vacuole-verify
  - septin-native-contractile_vacuole-causal
- assessment_id: septin-contractile_vacuole-images
  area: scope
  topic: No target images, measurements or verbatim snippets
  outcome: not_applicable
  summary: None is declared in this maintained target. Primary body/caption text inspection
    does not constitute figure-pixel, supplementary movie or raw-data reanalysis.
  target_ids:
  - GO:0000331
  evidence_ids:
  - septin-record-contractile_vacuole
- assessment_id: septin-contractile_vacuole_complex-schema
  area: schema
  topic: Original validation, deterministic rendering and input currentness
  outcome: supported
  summary: Original bundle validates/renders exactly and its frozen target hash matches
    current bytes and the original source revision. Native inventory checks pass with
    their actual coverage limits, not as certification of all scientific assertions.
  target_ids:
  - GO:0062159
  evidence_ids:
  - septin-record-contractile_vacuole_complex
  - septin-original-validation-contractile_vacuole_complex
  - septin-native-contractile_vacuole_complex-verify
  - septin-native-contractile_vacuole_complex-causal
- assessment_id: septin-contractile_vacuole_complex-native-scope
  area: provenance
  topic: Actual protein inventory coverage
  outcome: supported
  summary: Empty protein example/xref inventory and zero GENE_OR_PROTEIN nodes. Exit0
    does not independently validate the molecular details intentionally assigned to
    child records or the osmoregulatory pathway.
  target_ids:
  - GO:0062159
  evidence_ids:
  - septin-record-contractile_vacuole_complex
  - septin-native-contractile_vacuole_complex-verify
  - septin-native-contractile_vacuole_complex-causal
- assessment_id: septin-contractile_vacuole_complex-images
  area: scope
  topic: No target images, measurements or verbatim snippets
  outcome: not_applicable
  summary: None is declared in this maintained target. Primary body/caption text inspection
    does not constitute figure-pixel, supplementary movie or raw-data reanalysis.
  target_ids:
  - GO:0062159
  evidence_ids:
  - septin-record-contractile_vacuole_complex
- assessment_id: septin-contractile_vacuolar_membrane-taxa
  area: scope
  topic: Patchy eukaryotic occurrence and qualitative rarity
  outcome: supported
  summary: ENA confirms Eukaryota and each named species. More secondary abstract
    and selected Docampo body support patchy distribution with diverse architectures;
    RARE is qualitative, not a measured fraction or a claim of uniform molecular conservation.
  target_ids:
  - GO:0031164
  evidence_ids:
  - septin-record-contractile_vacuolar_membrane
  - septin-contractile-agent-tax-2759
  - septin-contractile-agent-more2024-meta
  - septin-contractile-agent-docampo2013-s3
- assessment_id: septin-contractile_vacuolar_membrane-adapter
  area: scope
  topic: Molecular and osmoregulatory-response applicability
  outcome: not_applicable
  summary: Membrane and whole record assert channel/pump roles; whole additionally
    names exact genes and hypo-osmotic stress response. Complex positively asserts
    osmoregulatory water expulsion/fluid segregation, while molecular detail remains
    on children. These scopes merit applicability assessment. The complete fresh catalogue
    lacks matched model organisms, so downstream queries are not applicable; historical
    runner failure is separately dated.
  target_ids:
  - GO:0031164
  evidence_ids:
  - septin-record-contractile_vacuolar_membrane
  - septin-review-policy
  - septin-catalogue
  - septin-historical-adapter-runner
- assessment_id: septin-contractile_vacuolar_membrane-necessity
  area: scope
  topic: Structure formation versus transport function
  outcome: unknown
  summary: Generic membrane material is constitutionally essential where declared.
    Molecular components retain UNKNOWN formation necessity. Localization, pump inhibition,
    water flux, or spore-survival phenotypes do not establish a universal requirement
    for forming the whole structure.
  target_ids:
  - GO:0031164
  evidence_ids:
  - septin-record-contractile_vacuolar_membrane
  - septin-curation-policy
  - septin-contractile-agent-nishihara2008-meta
  - septin-contractile-agent-gronlien2002-meta
- assessment_id: septin-contractile_vacuolar_membrane-boundary-context
  area: consistency
  topic: Membrane, bladder, lumen, pore, spongiome and whole-complex boundaries
  outcome: supported
  summary: Exact native identities keep the bladder separate from its bounding membrane
    and lumen and from the composite bladder/spongiome apparatus. Pore context remains
    a separate anchored structure. Frozen neighbors were inspected only at boundary
    fields; no neighbor or historical grouped/category issue is resolved.
  target_ids:
  - GO:0031164
  evidence_ids:
  - septin-record-contractile_vacuolar_membrane
  - septin-contractile-agent-go
  - septin-context-spongiome
  - septin-context-contractile_vacuole_lumen
  - septin-context-contractile_vacuole_pore
- assessment_id: septin-contractile_vacuolar_membrane-source-tiers
  area: provenance
  topic: Current source bodies, abstract limits and historical observations
  outcome: supported
  summary: Current Komsic/Bülow primary bodies and selected Docampo secondary sections
    were actually read at declared extents. Nishihara, Clarke, Nolta, Gronlien, Rohloff
    and Mitra primary support is complete abstract only; More and Allen are secondary
    abstracts. Current failed public routes are disclosed. Original October observations
    remain historical.
  target_ids:
  - GO:0031164
  evidence_ids:
  - septin-record-contractile_vacuolar_membrane
  - septin-contractile-agent-komsic2014-pmc-numeric
  - septin-contractile-agent-bulow2012-pmc-numeric
  - septin-contractile-agent-docampo2013-s3
  - septin-source-access
- assessment_id: septin-contractile_vacuole-taxa
  area: scope
  topic: Patchy eukaryotic occurrence and qualitative rarity
  outcome: supported
  summary: ENA confirms Eukaryota and each named species. More secondary abstract
    and selected Docampo body support patchy distribution with diverse architectures;
    RARE is qualitative, not a measured fraction or a claim of uniform molecular conservation.
  target_ids:
  - GO:0000331
  evidence_ids:
  - septin-record-contractile_vacuole
  - septin-contractile-agent-tax-2759
  - septin-contractile-agent-more2024-meta
  - septin-contractile-agent-docampo2013-s3
- assessment_id: septin-contractile_vacuole-adapter
  area: scope
  topic: Molecular and osmoregulatory-response applicability
  outcome: not_applicable
  summary: Membrane and whole record assert channel/pump roles; whole additionally
    names exact genes and hypo-osmotic stress response. Complex positively asserts
    osmoregulatory water expulsion/fluid segregation, while molecular detail remains
    on children. These scopes merit applicability assessment. The complete fresh catalogue
    lacks matched model organisms, so downstream queries are not applicable; historical
    runner failure is separately dated.
  target_ids:
  - GO:0000331
  evidence_ids:
  - septin-record-contractile_vacuole
  - septin-review-policy
  - septin-catalogue
  - septin-historical-adapter-runner
- assessment_id: septin-contractile_vacuole-necessity
  area: scope
  topic: Structure formation versus transport function
  outcome: unknown
  summary: Generic membrane material is constitutionally essential where declared.
    Molecular components retain UNKNOWN formation necessity. Localization, pump inhibition,
    water flux, or spore-survival phenotypes do not establish a universal requirement
    for forming the whole structure.
  target_ids:
  - GO:0000331
  evidence_ids:
  - septin-record-contractile_vacuole
  - septin-curation-policy
  - septin-contractile-agent-nishihara2008-meta
  - septin-contractile-agent-gronlien2002-meta
- assessment_id: septin-contractile_vacuole-boundary-context
  area: consistency
  topic: Membrane, bladder, lumen, pore, spongiome and whole-complex boundaries
  outcome: supported
  summary: Exact native identities keep the bladder separate from its bounding membrane
    and lumen and from the composite bladder/spongiome apparatus. Pore context remains
    a separate anchored structure. Frozen neighbors were inspected only at boundary
    fields; no neighbor or historical grouped/category issue is resolved.
  target_ids:
  - GO:0000331
  evidence_ids:
  - septin-record-contractile_vacuole
  - septin-contractile-agent-go
  - septin-context-spongiome
  - septin-context-contractile_vacuole_lumen
  - septin-context-contractile_vacuole_pore
- assessment_id: septin-contractile_vacuole-source-tiers
  area: provenance
  topic: Current source bodies, abstract limits and historical observations
  outcome: supported
  summary: Current Komsic/Bülow primary bodies and selected Docampo secondary sections
    were actually read at declared extents. Nishihara, Clarke, Nolta, Gronlien, Rohloff
    and Mitra primary support is complete abstract only; More and Allen are secondary
    abstracts. Current failed public routes are disclosed. Original October observations
    remain historical.
  target_ids:
  - GO:0000331
  evidence_ids:
  - septin-record-contractile_vacuole
  - septin-contractile-agent-komsic2014-pmc-numeric
  - septin-contractile-agent-bulow2012-pmc-numeric
  - septin-contractile-agent-docampo2013-s3
  - septin-source-access
- assessment_id: septin-contractile_vacuole_complex-taxa
  area: scope
  topic: Patchy eukaryotic occurrence and qualitative rarity
  outcome: supported
  summary: ENA confirms Eukaryota and each named species. More secondary abstract
    and selected Docampo body support patchy distribution with diverse architectures;
    RARE is qualitative, not a measured fraction or a claim of uniform molecular conservation.
  target_ids:
  - GO:0062159
  evidence_ids:
  - septin-record-contractile_vacuole_complex
  - septin-contractile-agent-tax-2759
  - septin-contractile-agent-more2024-meta
  - septin-contractile-agent-docampo2013-s3
- assessment_id: septin-contractile_vacuole_complex-adapter
  area: scope
  topic: Molecular and osmoregulatory-response applicability
  outcome: not_applicable
  summary: Membrane and whole record assert channel/pump roles; whole additionally
    names exact genes and hypo-osmotic stress response. Complex positively asserts
    osmoregulatory water expulsion/fluid segregation, while molecular detail remains
    on children. These scopes merit applicability assessment. The complete fresh catalogue
    lacks matched model organisms, so downstream queries are not applicable; historical
    runner failure is separately dated.
  target_ids:
  - GO:0062159
  evidence_ids:
  - septin-record-contractile_vacuole_complex
  - septin-review-policy
  - septin-catalogue
  - septin-historical-adapter-runner
- assessment_id: septin-contractile_vacuole_complex-necessity
  area: scope
  topic: Structure formation versus transport function
  outcome: unknown
  summary: Generic membrane material is constitutionally essential where declared.
    Molecular components retain UNKNOWN formation necessity. Localization, pump inhibition,
    water flux, or spore-survival phenotypes do not establish a universal requirement
    for forming the whole structure.
  target_ids:
  - GO:0062159
  evidence_ids:
  - septin-record-contractile_vacuole_complex
  - septin-curation-policy
  - septin-contractile-agent-nishihara2008-meta
  - septin-contractile-agent-gronlien2002-meta
- assessment_id: septin-contractile_vacuole_complex-boundary-context
  area: consistency
  topic: Membrane, bladder, lumen, pore, spongiome and whole-complex boundaries
  outcome: supported
  summary: Exact native identities keep the bladder separate from its bounding membrane
    and lumen and from the composite bladder/spongiome apparatus. Pore context remains
    a separate anchored structure. Frozen neighbors were inspected only at boundary
    fields; no neighbor or historical grouped/category issue is resolved.
  target_ids:
  - GO:0062159
  evidence_ids:
  - septin-record-contractile_vacuole_complex
  - septin-contractile-agent-go
  - septin-context-spongiome
  - septin-context-contractile_vacuole_lumen
  - septin-context-contractile_vacuole_pore
- assessment_id: septin-contractile_vacuole_complex-source-tiers
  area: provenance
  topic: Current source bodies, abstract limits and historical observations
  outcome: supported
  summary: Current Komsic/Bülow primary bodies and selected Docampo secondary sections
    were actually read at declared extents. Nishihara, Clarke, Nolta, Gronlien, Rohloff
    and Mitra primary support is complete abstract only; More and Allen are secondary
    abstracts. Current failed public routes are disclosed. Original October observations
    remain historical.
  target_ids:
  - GO:0062159
  evidence_ids:
  - septin-record-contractile_vacuole_complex
  - septin-contractile-agent-komsic2014-pmc-numeric
  - septin-contractile-agent-bulow2012-pmc-numeric
  - septin-contractile-agent-docampo2013-s3
  - septin-source-access
- assessment_id: septin-contractile_vacuolar_membrane-identity
  area: identity
  topic: Exact bilayer, synonym and hierarchy
  outcome: supported
  summary: GO0031164 and SL0074 agree on contractile vacuolar membrane identity/synonym,
    vacuolar-membrane parent and contractile-vacuole parthood. Broader location-database
    complex prose does not collapse the membrane/bladder/apparatus distinction.
  target_ids:
  - GO:0031164
  evidence_ids:
  - septin-record-contractile_vacuolar_membrane
  - septin-contractile-agent-go
  - septin-contractile-agent-SL-0074
  - septin-contractile-agent-ancestors-0031164
- assessment_id: septin-contractile_vacuolar_membrane-composition
  area: grounding
  topic: Constitutional bilayer and supported aquaporin class
  outcome: supported
  summary: The generic bilayer is label-only constitutional material, not an exact
    lipid molecule grounded to a whole-location GO term. Nishihara directly supports
    ApAQP at the Amoeba CV membrane and surrounding vesicles. No guessed species-specific
    accession or unsupported claim that all broad MIP family members localize to CVs
    is introduced.
  target_ids:
  - GO:0031164
  evidence_ids:
  - septin-record-contractile_vacuolar_membrane
  - septin-contractile-agent-go
  - septin-contractile-agent-nishihara2008-meta
  - septin-contractile-agent-aquaporin-family
  - septin-contractile-agent-aquaporin-transporter
- assessment_id: septin-contractile_vacuolar_membrane-example
  area: scope
  topic: Amoeba localization and perivacuolar pump context
  outcome: supported
  summary: 'Taxon5775 is Amoeba proteus. The canonical sentence is read with the explicit
    graph/component boundary: ApAQP labels CV membrane/perivacuolar vesicles, V-ATPase
    labels surrounding vesicles. The record has already excluded the pump from direct
    membrane components, and its graph respects this source localization.'
  target_ids:
  - GO:0031164
  evidence_ids:
  - septin-record-contractile_vacuolar_membrane
  - septin-contractile-agent-tax-5775
  - septin-contractile-agent-nishihara2008-meta
- assessment_id: septin-contractile_vacuolar_membrane-graph
  area: graph
  topic: Five scoped filling-context edges
  outcome: supported
  summary: Membrane bounds vacuole; pump resides in perivacuolar vesicles; possible
    ion-gradient contribution, ApAQP water permeability and filling support remain
    source-scoped. The unanchored pump is context, not a claimed constituent of this
    one bilayer. Gradient generation is a source hypothesis and a complete systole
    mechanism is not asserted.
  target_ids:
  - GO:0031164
  evidence_ids:
  - septin-record-contractile_vacuolar_membrane
  - septin-contractile-agent-go
  - septin-contractile-agent-nishihara2008-meta
  - septin-graph-policy
- assessment_id: septin-contractile_vacuolar_membrane-verdict
  area: consistency
  topic: Qualified positive membrane review
  outcome: supported
  summary: pass_with_limitations is supported for identity, Amoeba channel localization,
    carefully separated perivacuolar pump context and nonmechanistic filling graph.
    No original or new concrete scientific record correction is established; molecular
    formation dependency and complete native identity coverage remain unknown.
  target_ids:
  - GO:0031164
  evidence_ids:
  - septin-record-contractile_vacuolar_membrane
  - septin-original-contractile_vacuolar_membrane
  - septin-contractile-agent-go
  - septin-contractile-agent-nishihara2008-meta
- assessment_id: septin-contractile_vacuole-identity
  area: identity
  topic: Bladder identity and synonym qualifier
  outcome: concern
  summary: Exact GO0000331 identity, complex parthood and membrane part remain supported.
    SL0073 supports CV. However central bladder is RELATED in the cited current GO
    authority, so the maintained EXACT qualifier remains inherited F3.
  target_ids:
  - GO:0000331
  evidence_ids:
  - septin-record-contractile_vacuole
  - septin-contractile-agent-go
  - septin-contractile-agent-SL-0073
  - septin-contractile-agent-ancestors-0000331
- assessment_id: septin-contractile_vacuole-pump
  area: grounding
  topic: V-ATPase subunit examples and source scope
  outcome: supported
  summary: Four reviewed Dictyostelium accessions and bounded gene queries match vatA/B/C/M.
    Clarke supports VatM-directed assembly and CVC membrane targeting; Nolta and Allen
    distinguish pump-rich spongiome and pump-poor bladder. Record descriptions use
    system-level membranes, and no homogeneous pump distribution or formation necessity
    is inferred. Broad GO0016471 is not a substitute for an experimentally localized
    cross-lineage subset.
  target_ids:
  - GO:0000331
  evidence_ids:
  - septin-record-contractile_vacuole
  - septin-contractile-agent-clarke2002-meta
  - septin-contractile-agent-nolta1994-meta
  - septin-contractile-agent-allen2002-title
  - septin-contractile-agent-go-vatpase
  - septin-contractile-agent-UniProtKB-P54647
  - septin-contractile-agent-UniProtKB-Q76NU1
  - septin-contractile-agent-UniProtKB-P54648
  - septin-contractile-agent-UniProtKB-Q54E04
- assessment_id: septin-contractile_vacuole-aquaporin-membership
  area: evidence
  topic: Taxon-paired CV localization and inherited F1
  outcome: concern
  summary: Amoeba ApAQP and Chlamydomonas MIP1 support CV-associated aquaporins at
    their own taxa. Dictyostelium aqpA sources concern development/spore dormancy;
    AqpB primary localization is to unidentified vacuoles and membrane protrusions,
    with a CV-like role only proposed by analogy. Identity-only examples do not establish
    CV constituent membership. Mutant water conductance is not demonstrated wild-type
    AqpB conductance.
  target_ids:
  - GO:0000331
  evidence_ids:
  - septin-record-contractile_vacuole
  - septin-contractile-agent-nishihara2008-meta
  - septin-contractile-agent-komsic2014-pmc-numeric
  - septin-contractile-agent-bulow2012-pmc-numeric
  - septin-contractile-agent-aqpA2000-meta
  - septin-contractile-agent-UniProtKB-Q9U8P7
  - septin-contractile-agent-UniProtKB-Q54WT8
- assessment_id: septin-contractile_vacuole-mip1
  area: scope
  topic: Supported MIP1 localization with unresolved accession/transport assay scope
  outcome: supported
  summary: Komsic reports immunogold and GFP localization at CV membranes in CC3395/UVM4-derived
    strains. Exact current MIP1/taxon3055 query returns no entry; this does not refute
    localization or justify guessing an accession. Modeled CV water permeability,
    questioned GFP construct functionality and direct localization are separate evidence
    types.
  target_ids:
  - GO:0000331
  evidence_ids:
  - septin-record-contractile_vacuole
  - septin-contractile-agent-komsic2014-pmc-numeric
  - septin-contractile-agent-query-MIP1-3055-all
  - septin-contractile-agent-tax-3055
- assessment_id: septin-contractile_vacuole-osmolarity
  area: evidence
  topic: Inherited F2 and repeated discharge-edge source note
  outcome: concern
  summary: Komsic Results distinguish CV size correlated with cell size from contraction
    interval dependent on medium osmolarity. The canonical note overstates both responding
    to external osmolarity; the final discharge-edge evidence note repeats osmolarity-dependent
    size changes. Both fields belong to the same inherited F2, without changing the
    valid water-expulsion function or measured-size context.
  target_ids:
  - GO:0000331
  evidence_ids:
  - septin-record-contractile_vacuole
  - septin-contractile-agent-komsic2014-pmc-numeric
- assessment_id: septin-contractile_vacuole-other-examples
  area: scope
  topic: Dictyostelium and T.cruzi model-specific findings
  outcome: supported
  summary: Dictyostelium V-ATPase dynamics are supported by Clarke primary abstract;
    T.cruzi acidocalcisome/CVC involvement in hypo-osmotic recovery is supported by
    Rohloff primary abstract. Neither model establishes shared invariant machinery
    in all eukaryotes.
  target_ids:
  - GO:0000331
  evidence_ids:
  - septin-record-contractile_vacuole
  - septin-contractile-agent-clarke2002-meta
  - septin-contractile-agent-rohloff2004-meta
  - septin-contractile-agent-tax-44689
  - septin-contractile-agent-tax-5693
- assessment_id: septin-contractile_vacuole-graph
  area: graph
  topic: Six filling/discharge edges with explicit inherited concerns
  outcome: concern
  summary: The anatomical enclosure and general pump/channel-assisted osmotic filling/discharge
    model have source support at declared nonmechanistic/hypothesis scope. The aquaporin
    node inherits unsupported aqpA/aqpB constituent specificity (F1), and discharge-edge
    evidence repeats F2. Transient filled-vacuole state is deliberately not given
    the exact GO class grounding. A full force-generating systole mechanism remains
    unasserted.
  target_ids:
  - GO:0000331
  evidence_ids:
  - septin-record-contractile_vacuole
  - septin-contractile-agent-go
  - septin-contractile-agent-nishihara2008-meta
  - septin-contractile-agent-clarke2002-meta
  - septin-contractile-agent-komsic2014-pmc-numeric
  - septin-contractile-agent-bulow2012-pmc-numeric
  - septin-contractile-agent-allen2002-title
  - septin-graph-policy
- assessment_id: septin-contractile_vacuole-verdict
  area: consistency
  topic: Needs curation with preserved three-finding lineage
  outcome: concern
  summary: needs_curation remains warranted by F1 major membership support, F2 minor
    osmolarity/size wording (including its repeated graph note), and F3 minor synonym
    scope. Scientific identity and general osmoregulation remain supported. Exact
    predecessor repository/review/finding identities are retained; no finding is silently
    resolved by native command success.
  target_ids:
  - GO:0000331
  evidence_ids:
  - septin-record-contractile_vacuole
  - septin-original-contractile_vacuole
  - septin-contractile-agent-go
  - septin-contractile-agent-komsic2014-pmc-numeric
  - septin-contractile-agent-bulow2012-pmc-numeric
- assessment_id: septin-contractile_vacuole_complex-identity
  area: identity
  topic: Composite apparatus distinct from membrane-bounded bladder
  outcome: supported
  summary: GO0062159 explicitly denotes the non-membrane-bounded composite apparatus
    and has related synonym CVC, GO0043232 parent and bladder/spongiome parts. OTHER
    preserves this composite scope rather than asserting one enclosing bilayer around
    the entire apparatus. This does not deny membranes on its constituent bladder/tubules.
  target_ids:
  - GO:0062159
  evidence_ids:
  - septin-record-contractile_vacuole_complex
  - septin-contractile-agent-go
  - septin-contractile-agent-ancestors-0062159
  - septin-contractile-agent-docampo2013-s3
  - septin-context-spongiome
- assessment_id: septin-contractile_vacuole_complex-examples
  area: scope
  topic: Dictyostelium bipartite fractions and Paramecium radial arms
  outcome: supported
  summary: Nolta primary abstract supports separable bladder/spongiome membrane fractions
    in Dictyostelium; Gronlien supports decorated-spongiome electrogenic fluid segregation
    in P.multimicronucleatum. The record does not transfer a fixed ciliate radial-arm
    architecture to all protists or treat transport inhibition as failure to form
    the complex.
  target_ids:
  - GO:0062159
  evidence_ids:
  - septin-record-contractile_vacuole_complex
  - septin-contractile-agent-nolta1994-meta
  - septin-contractile-agent-gronlien2002-meta
  - septin-contractile-agent-tax-44689
  - septin-contractile-agent-tax-44030
- assessment_id: septin-contractile_vacuole_complex-graph
  area: graph
  topic: Three organelle-level parthood/function edges
  outcome: supported
  summary: Bladder and spongiome are parts of the complex, which carries out periodic
    water expulsion. Exact GO relations and the bipartite primary evidence support
    these edges. Molecular pump/channel and electrophysiological details remain assigned
    to children, without claiming a full conserved force-generation mechanism.
  target_ids:
  - GO:0062159
  evidence_ids:
  - septin-record-contractile_vacuole_complex
  - septin-contractile-agent-go
  - septin-contractile-agent-nolta1994-meta
  - septin-contractile-agent-docampo2013-s3
  - septin-graph-policy
- assessment_id: septin-contractile_vacuole_complex-verdict
  area: consistency
  topic: Qualified positive whole-complex review
  outcome: supported
  summary: pass_with_limitations remains supported for exact composite identity, source-qualified
    model examples, child boundaries and general osmoregulation. No original or new
    scientific finding is established for this record. Broad eukaryotic prevalence
    and full conservation/mechanism remain unproven.
  target_ids:
  - GO:0062159
  evidence_ids:
  - septin-record-contractile_vacuole_complex
  - septin-original-contractile_vacuole_complex
  - septin-contractile-agent-go
  - septin-contractile-agent-nolta1994-meta
  - septin-contractile-agent-gronlien2002-meta
  - septin-contractile-agent-docampo2013-s3
- assessment_id: current-input-comparison
  area: provenance
  topic: Complete frozen-input comparison and bounded refresh
  outcome: supported
  summary: 1 of ten original target hashes differ from current main. The changed content
    is substantively reassessed in the target-specific assessments; original observations
    remain historical and unchanged. All current target and used context bytes are
    frozen.
  target_ids:
  - GO:0031164
  - GO:0000331
  - GO:0062159
  - cellstructuremech:contractile_vacuole_lumen
  - GO:0031913
  - GO:0030137
  - cellstructuremech:copi_coated_vesicle_lumen
  - GO:0030663
  - GO:0030134
  - cellstructuremech:copii_coated_vesicle_lumen
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
- finding_id: septin-F1
  issue_key: contractile-vacuole-aqpa-aqpb-membership-support
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Dictyostelium aqpA and aqpB lack demonstrated CV membership in the cited
    evidence
  description: The contractile_vacuole_aquaporins constituent declares aqpA and aqpB
    and supplies their verified Dictyostelium examples. The identity-only disclaimers
    correctly limit what accessions prove but leave that constituent assignment unsupported.
    AqpA sources concern late development and spore dormancy. The AqpB primary paper
    localizes GFP constructs to unspecified vacuoles and plasma membrane/protrusions,
    then proposes a CV-like role by analogy; it does not experimentally identify the
    vacuoles as contractile vacuoles. Water permeability was demonstrated for a loop-deletion
    mutant rather than the tested wild-type protein. Amoeba ApAQP and Chlamydomonas
    MIP1 evidence supports the broader component without proving these two assignments.
  target_ids:
  - GO:0000331
  field_paths:
  - components[component_id=contractile_vacuole_aquaporins].gene_symbols
  - components[component_id=contractile_vacuole_aquaporins].protein_examples
  - causal_graphs[graph_id=proton_gradient_water_filling_and_discharge].nodes[node_id=aquaporins]
  evidence_ids:
  - septin-contractile-agent-bulow2012-pmc-numeric
  - septin-contractile-agent-aqpA2000-meta
  - septin-contractile-agent-komsic2014-pmc-numeric
  - septin-contractile-agent-nishihara2008-meta
  - septin-contractile-agent-UniProtKB-Q9U8P7
  - septin-contractile-agent-UniProtKB-Q54WT8
  - septin-record-contractile_vacuole
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/contractile_vacuole.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Components; review-checklist:Component evidence and protein
    examples
  native_severity: major
  normalization_reason: The affected fields assert constituent membership and transfer
    a channel role to named proteins; accession verification alone cannot repair the
    missing structure-specific support.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T005252Z-contractile-vacuole-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2670
- finding_id: septin-F2
  issue_key: contractile-vacuole-chlamydomonas-size-osmolarity-note
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Chlamydomonas example conflates CV size regulation with osmolarity response
  description: 'The canonical note says both CV size and pulse frequency respond to
    changing external osmolarity. Komsic-Buchmann2014 Results explicitly report that
    CV size did not correlate with medium osmotic strength: CV size correlated with
    cell size, while contraction interval depended on medium osmolarity. The two adaptations
    are distinguished in the paper. The broader function and measured-size/interval
    evidence remain supported. The same overstatement is repeated in the final discharge-edge
    evidence note, which describes osmolarity-dependent pulse-frequency and size changes.
    This successor includes that repeated field under the same F2 lineage, not as
    a separate finding.'
  target_ids:
  - GO:0000331
  field_paths:
  - canonical_examples[taxon_id=NCBITaxon:3055].note
  - causal_graphs[graph_id=proton_gradient_water_filling_and_discharge].edges[subject=water_filled_contractile_vacuole,predicate=discharges].evidence[0].notes
  evidence_ids:
  - septin-contractile-agent-komsic2014-pmc-numeric
  - septin-record-contractile_vacuole
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/contractile_vacuole.yaml
    role: maintained scientific record
  rule_id: review-checklist:Canonical examples; literature-evidence:claim-specific
    support
  native_severity: minor
  normalization_reason: Bounded repeated wording overstatement in canonical example
    and final graph-edge evidence note; record identity, valid model choice and general
    osmoregulatory function remain supported.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T005252Z-contractile-vacuole-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2671
- finding_id: septin-F3
  issue_key: contractile-vacuole-central-bladder-synonym-scope
  category: nomenclature
  severity: minor
  status: open
  certainty: confirmed
  title: Central bladder synonym scope exceeds the cited GO mapping
  description: The record labels central bladder EXACT_SYNONYM and names GO:0000331
    as its source. Both captured current term and ancestry responses classify central
    bladder as a related synonym. The label is biologically pertinent, but the exactness
    qualifier is not supported by the cited authority.
  target_ids:
  - GO:0000331
  field_paths:
  - synonyms[synonym_text=central bladder].synonym_type
  evidence_ids:
  - septin-contractile-agent-go
  - septin-contractile-agent-ancestors-0000331
  - septin-record-contractile_vacuole
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/contractile_vacuole.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Identifier and synonym provenance; review-checklist:Identity
  native_severity: minor
  normalization_reason: Localized source-to-synonym-scope mismatch; canonical GO identity
    and general bladder/CVC boundaries remain valid.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T005252Z-contractile-vacuole-audit
    finding_id: F3
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2672
actions:
- action_id: septin-A1
  finding_ids:
  - septin-F1
  target_ids:
  - GO:0000331
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/contractile_vacuole.yaml
    role: maintained scientific record
  description: Under separately authorized curation, remove aqpA/aqpB and their identity-only
    examples from the established CV-constituent gene/example list unless direct CV-localization
    evidence is supplied. Retain the supported generic aquaporin class and evidenced
    MIP1/ApAQP context. If useful, preserve AqpB as an explicitly tentative hypothesis
    in a source-backed discussion, with unspecified-vacuole localization and mutant-versus-wild-type
    functional scope. Record the reason so symbol seeding cannot silently restore
    the unsupported assignment.
  acceptance_checks:
  - Every retained named aquaporin in the CV constituent has a taxon-paired source
    supporting CV membership, not only identity, developmental expression or generic
    vacuolar location.
  - The von Bülow2012 data are not described as direct CV localization or as demonstrated
    wild-type AqpB water conductance.
  - The aquaporin graph remains at supported class/taxon scope, and MIP1 is not assigned
    a guessed accession.
  - Use the guarded writer and required curation/history events; run native schema/strict,
    UniProt verification, CURIE/product, history and generated-page checks plus qc
    after any curation.
  generator: Maintained scientific YAML; just render derives pages.
- action_id: septin-A2
  finding_ids:
  - septin-F2
  target_ids:
  - GO:0000331
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/contractile_vacuole.yaml
    role: maintained scientific record
  description: Under separately authorized curation, revise the Chlamydomonas canonical
    note to distinguish CV size adaptation during cell growth from contraction-interval
    or pulse-frequency adaptation to external osmolarity. Preserve the valid model
    and source, and retain generic descriptions of measured size and interval only
    without implying both depend on medium osmolarity. Correct the repeated osmolarity-dependent
    size wording in the final discharge-edge evidence note as part of the same change.
  acceptance_checks:
  - 'The canonical note accurately states the distinct Results relationships: CV size
    versus cell size, contraction interval versus medium osmolarity.'
  - The final discharge-edge evidence note also distinguishes osmolarity-dependent
    contraction interval from size/cell-growth correlation; it does not repeat the
    canonical-note overstatement.
  - No direct lumen-osmolarity measurement or independent wild-type MIP1 water-channel
    assay is inferred from the modeling/localization study.
  - Use the guarded writer and required curation/history events; run native schema/strict,
    history, render and qc gates after curation.
  generator: Maintained scientific YAML; just render derives pages.
- action_id: septin-A3
  finding_ids:
  - septin-F3
  target_ids:
  - GO:0000331
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/contractile_vacuole.yaml
    role: maintained scientific record
  description: Under separately authorized curation, change central bladder to RELATED_SYNONYM
    to match the cited GO authority, or supply and explicitly cite independent support
    for exact equivalence at this record scope. Retain the main GO identity and label.
  acceptance_checks:
  - The central bladder synonym qualifier agrees with its cited authority or a separately
    justified exact mapping.
  - Use the guarded writer and required history events; run schema/strict, identifier-label,
    history, render and qc checks after curation.
  generator: Maintained scientific YAML; just render derives pages.
limitations:
- 'Contractile vacuole lumen/pore and COPII transport vesicle/lumen independent subreview:
  Assigned four records only, all current target hashes unchanged; three already-frozen
  mutual CV targets were used only for boundary fields. No neighbor, group, category
  or historical external issue is terminally resolved.'
- 'Contractile vacuole lumen/pore and COPII transport vesicle/lumen independent subreview:
  Komsic2014 genuine primary HTML scientific body and Table1/captions were independently
  inspected from same-PR shared snapshot with actual original timestamp. No images,
  movies, supplemental experiments or raw measurements reanalyzed. Its CC3395 and
  UVM4 contexts are distinguished from universal Chlamydomonas claims.'
- 'Contractile vacuole lumen/pore and COPII transport vesicle/lumen independent subreview:
  Komsic CV size correlates with cell size/growth, interval with osmolarity; modeled
  lumen osmolarity is not measured. The lumen text describes measurements under varied
  conditions and does not claim a causal volume–osmolarity relationship. Sibling record
  findings do not transfer automatically.'
- 'Contractile vacuole lumen/pore and COPII transport vesicle/lumen independent subreview:
  Gronlien primary abstract supports the compressed-Paramecium microelectrode example;
  More2024 and Allen2002 remain secondary abstracts, not inspected full bodies. DOI
  redirect/challenge pages do not upgrade access tier. RARE/COMMON are qualitative
  context, not prevalence counts.'
- 'Contractile vacuole lumen/pore and COPII transport vesicle/lumen independent subreview:
  Frankel secondary chapter was inspected at complete named CV and pore sections and
  opening positioning paragraphs, not the entire book or image pixels. McKanna1973
  is publisher-deposited primary synopsis only; no experimental species or exact protein
  composition is invented.'
- 'Contractile vacuole lumen/pore and COPII transport vesicle/lumen independent subreview:
  Barlowe1994 is complete primary abstract only. Matsuoka1998 fresh institutional
  PDF scientific text pp263–274 includes Methods/Tables/captions; no images or raw
  data reanalyzed. Native ER and synthetic-liposome/nucleotide conditions remain distinct;
  in-vitro formation is not universal in-vivo necessity.'
- 'Contractile vacuole lumen/pore and COPII transport vesicle/lumen independent subreview:
  GO contractile-lumen search read only first100 of398 hits. Exact candidate GO0106173
  label/definition conflict is retained as unknown, without forced mapping, exhaustive
  absence or historical issue resolution.'
- 'Contractile vacuole lumen/pore and COPII transport vesicle/lumen independent subreview:
  Three applicability defects are specific: contractile-lumen omission for explicit
  osmotic-response context, and two COPII expression-only exemptions despite named
  machinery. Pore is genuinely excluded at topology/coarse-flow scope with unasserted
  molecular composition.'
- 'Contractile vacuole lumen/pore and COPII transport vesicle/lumen independent subreview:
  Fresh complete catalogue has no matching yeast/ciliate/algal organism; no downstream
  matched query applies or biological absence follows. Historical00:49Z runner PermissionError
  remains historical, not a new failure or successful invocation.'
- 'Contractile vacuole lumen/pore and COPII transport vesicle/lumen independent subreview:
  All eight native protein commands pass empty represented inventories and zero typed
  protein nodes. They do not validate narrative molecular identities, formation necessity
  or scientific source support. Root owns full QC, issue handling and all repository/GitHub
  changes.'
- 'COPI vesicle, lumen and membrane independent subreview: Assigned scope is three
  COPI records. Whole vesicle stale additions were reassessed; other two targets are
  unchanged. Three neighbor records are bounded identity/partonomy/component context
  only; their scientific or category findings are not disposed of.'
- 'COPI vesicle, lumen and membrane independent subreview: Sandmann fresh primary
  HTML was read only in the exact declared Abstract/Introduction, Methods and Results/Discussion
  sections. Other body sections, figure pixels, supplementary/raw microscopy and assay
  data were not reanalysed. Genetic suppression and packaging assays are not direct
  measurements of every trafficking step or population frequency.'
- 'COPI vesicle, lumen and membrane independent subreview: Waters1991 is complete
  primary abstract/bibliography only. Current publisher HTTP200 is a Client Challenge,
  not readable article text. Sandmann XML HTTP500 is an access limitation covered
  by independently readable genuine primary HTML.'
- 'COPI vesicle, lumen and membrane independent subreview: Yu2012 retains actual 10:50Z
  snapshots from PR2360, hash verified; previously inspected Introduction/Experimental
  Approach/model sections remain the scope and Introduction was reread. No new download,
  full Methods or image audit claimed. Mammalian coatomer with defined human/yeast
  constructs is not direct yeast-specific assembly necessity.'
- 'COPI vesicle, lumen and membrane independent subreview: GO0006890 supports general
  directed transport destination. The refreshed proteins/lipids description is broad
  contextual cargo scope, not a particular lipid-species flux measurement, exclusively
  COPI route, fusion mechanism or coat-retention assertion.'
- 'COPI vesicle, lumen and membrane independent subreview: Same-label GO0106172 remains
  definition-limited by endocytic wording in QuickGO and OLS; exact equivalence to
  general SL-0321/local lumen is unknown. The current query inspected first100 of618
  hits, not every ontology term. No exact-term absence or historical mapping-error
  claim is made.'
- 'COPI vesicle, lumen and membrane independent subreview: Arakel/Schwappach2018 is
  secondary abstract context only; no body/poster read and no resolution of the native
  definition inconsistency inferred.'
- 'COPI vesicle, lumen and membrane independent subreview: All six native protein
  commands pass empty protein inventories and zero GENE_OR_PROTEIN nodes; they do
  not verify narrative molecules or source scope. No unsupported accession/family
  absence is asserted.'
- 'COPI vesicle, lumen and membrane independent subreview: Catalogue coverage check
  is complete only for the returned current array; no matching yeast dataset means
  no applicable downstream gene/module query. Historical runner failure at00:49Z remains
  historical; no fresh execution is claimed.'
- 'COPI vesicle, lumen and membrane independent subreview: No target images, numerical
  properties or snippets require additional audit. All original findings/actions arrays
  are empty. Root owns corpus gates, issue deduplication/publication, successor writing
  and final CI; this report makes no future CI claim.'
- 'Contractile vacuolar membrane, whole vacuole and complex independent subreview:
  Assigned membrane/whole-vacuole/complex records only. All are unchanged from frozen
  original source bytes, and all original validation/render checks pass. Whole-vacuole
  F1–F3 remain open; F2 includes a verified repeated graph-note occurrence under the
  same stable key.'
- 'Contractile vacuolar membrane, whole vacuole and complex independent subreview:
  Komsic current genuine primary HTML was read only at declared Abstract, Strains
  used Methods, specified Results, Aquaporins and CV function Discussion, Table1 and
  associated text captions. CC3395/UVM4-derived strain and osmotic-adaptation scope
  is retained. No image pixels, supplementary movies or raw-data audit.'
- 'Contractile vacuolar membrane, whole vacuole and complex independent subreview:
  Bülow current genuine primary HTML was read at complete Abstract, Results and Discussion
  with text captions, not full Experimental Procedures or pixels. The AqpB hypothesis,
  unspecified vacuoles, GFP-fusion localization and mutant-versus-wild-type transport
  result remain distinct. This is insufficient cited membership support, not proof
  of biological absence.'
- 'Contractile vacuolar membrane, whole vacuole and complex independent subreview:
  Nishihara, Clarke, Nolta, Gronlien, Rohloff and Mitra2000 were read as complete
  native primary abstracts only. More2024 and Allen2002 are secondary abstract context.
  Unread publisher bodies and guessed S3 routes returned403/404; no full-body access
  is invented.'
- 'Contractile vacuolar membrane, whole vacuole and complex independent subreview:
  Docampo2013 is a current genuine secondary JATS body, inspected only at sections
  History, Structure and composition, and Role in osmoregulation. Cited-primary experiments,
  raw images and the complete article were not independently audited. Proposed osmolyte
  and systole mechanisms remain hypotheses.'
- 'Contractile vacuolar membrane, whole vacuole and complex independent subreview:
  Six UniProt accessions and six exact reviewed symbol/taxon queries support current
  identity and bounded uniqueness only. MIP1 exact query zero hits does not establish
  absence or justify guessing an accession. Broad InterPro MIP/aquaporin classes are
  not exact CV-localized subset or localization evidence.'
- 'Contractile vacuolar membrane, whole vacuole and complex independent subreview:
  Native membrane inventory has one NO_GENE_SYMBOLS and one UNANCHORED_NO_UNIPROT
  node; whole vacuole has one COVERED and one PARTIAL_EXAMPLES node, missing MIP1;
  complex has empty inventory/zero protein nodes. All six commands exit0, without
  resolving scientific concerns or proving mechanistic/formation claims.'
- 'Contractile vacuolar membrane, whole vacuole and complex independent subreview:
  Actual molecular and osmoregulatory-response scope merits structured-source applicability
  for all three targets. No matching model organism is present in the fresh complete
  catalogue; no unrelated downstream query is substituted. Historical runner PermissionError
  remains00:49Z, not a fresh invocation.'
- 'Contractile vacuolar membrane, whole vacuole and complex independent subreview:
  Eukaryotic rarity is qualitative. Strain/model localization, transport function
  and osmotic adaptation do not establish universal constituent membership or molecular
  necessity for structure formation. Composite CVC and bladder/bilayer/anatomical
  parts remain distinct despite broader source terminology.'
- 'Contractile vacuolar membrane, whole vacuole and complex independent subreview:
  Three frozen neighbors were read only at declared boundary fields. No neighbor/group/category
  issue is terminally resolved. Root owns global gates, issue deduplication/publication,
  repository/GitHub writes and final CI/queue checks.'
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
- 'Issue #2668 tracks the one stale target: COPI-coated vesicle gained a history entry
  and a Golgi-to-ER retrograde transport destination edge. Current GO0006890 and primary
  COPI evidence support its bounded transport destination; broad proteins/lipids cargo
  context does not establish a particular lipid flux, fusion mechanism or exclusively
  COPI route.'
- 'Issue #2669 tracks nine applicability defects: omitted assessments for contractile
  vacuolar membrane, whole vacuole, complex and lumen; five unsupported expression-only
  exclusions for the three COPI and two COPII targets. Contractile vacuole pore remains
  a genuine exclusion at topology and coarse flow-control scope without asserted molecular
  composition.'
- Source commit 7081777bba0daacfa48fc6d826cdfd7138e751b4 is retained by tag review-base/pr2361-current-record-followup-20261103.
- CLAUDE.md is an alias of AGENTS.md; canonical regular AGENTS.md bytes are frozen.
- All 51 used local inputs were frozen before assessment, including four neighbor
  records, native configuration, graph/protein policies and verifier source. Neighbors
  are context only, not additional targets or dispositions of their findings.
- Fresh and reused public-source snapshots retain actual access dates and inspection
  tiers. Native authority identity does not independently establish localization,
  mechanistic action or assembly necessity.
- All twenty native protein commands returned zero, with incomplete coverage explicitly
  retained. Contractile-vacuolar membrane V-ATPase is UNANCHORED_NO_UNIPROT and aquaporins
  NO_GENE_SYMBOLS. Whole-vacuole V-ATPase is covered by four represented accessions;
  aquaporins are PARTIAL_EXAMPLES with MIP1 missing. Empty inventories or zero typed
  protein nodes in other targets do not validate narrative molecules. Execution success
  does not establish contractile-vacuole membership.
- The major contractile-vacuole finding concerns insufficient AqpA/AqpB membership
  support. The two minor findings concern osmolarity-dependent size wording, including
  its repeated discharge-edge evidence note, and treating the related central-bladder
  synonym as exact. Source-supported distinctions between size/cell growth and contraction
  interval/osmolarity are preserved.
- The contractile-vacuole lumen wording describes volume measurements under varied
  conditions without asserting a causal volume-to-osmolarity relationship; an independent
  source reread supports that bounded scope. The sibling whole-vacuole finding is
  not automatically transferred.
- Current GO0106172 and GO0106173 have exact COPI/COPII lumen labels but conflicting
  endocytic definition wording. Mapping uncertainty is preserved; neither forced retargeting
  nor exhaustive ontology absence is claimed.
- All three inherited scientific findings remain open for separate record curation.
  Nine targets retain qualified positive scientific assessments. No record is edited.
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T005251Z-contractile-vacuolar-membrane-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T005252Z-contractile-vacuole-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T005253Z-contractile-vacuole-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T005253Z-contractile-vacuole-lumen-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T005254Z-contractile-vacuole-pore-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T005255Z-copi-coated-vesicle-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T005255Z-copi-coated-vesicle-lumen-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T005256Z-copi-coated-vesicle-membrane-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T005257Z-copii-coated-er-to-golgi-transport-vesicle-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T005258Z-copii-coated-vesicle-lumen-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
links:
- https://github.com/CultureBotAI/CellStructureMech/pull/2361
- https://github.com/CultureBotAI/CellStructureMech/issues/2514
- https://github.com/CultureBotAI/CellStructureMech/issues/2668
- https://github.com/CultureBotAI/CellStructureMech/issues/2669
- https://github.com/CultureBotAI/CellStructureMech/issues/2670
- https://github.com/CultureBotAI/CellStructureMech/issues/2671
- https://github.com/CultureBotAI/CellStructureMech/issues/2672
```
